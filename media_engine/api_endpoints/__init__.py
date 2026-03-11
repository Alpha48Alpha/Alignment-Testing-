"""
media_engine.api_endpoints
==========================
Monetizable REST API layer for the Media Engine.

Design
------
Built with the Python standard library's ``http.server`` module so the module
has **zero third-party dependencies** for the core API scaffolding.  Each
endpoint is a named handler registered on a central ``Router``; the
``MediaEngineAPIServer`` glues the router to an ``HTTPServer`` instance.

For production deployments the same handler logic can be wired into FastAPI,
Flask, or Django with minimal changes — the ``Router`` and handler functions
are framework-agnostic.

Endpoints
---------
POST /api/v1/ingest
    Accepts a JSON body ``{"source": "<path_or_url>"}`` and returns a
    ``MediaObject`` summary (without raw bytes).

POST /api/v1/process
    Accepts ``{"source": "<path_or_url>", "operations": [...], "options": {…}}``
    and returns a ``ProcessingResult`` summary.

POST /api/v1/analyze
    Accepts ``{"source": "<path_or_url>"}`` and returns an ``AnalysisResult``
    dict.

GET /api/v1/health
    Returns ``{"status": "ok", "version": "1.0.0"}``.

GET /api/v1/operations
    Returns the list of available processing operations.

Monetisation hooks
------------------
``APIKeyMiddleware``
    Validates ``X-API-Key`` headers.  Returns 401 for missing keys and 403 for
    keys that are not in the allowed set.  In production back this with a
    database lookup or a JWT validation service.

``UsageTracker``
    Counts API calls per API key.  Designed to feed into a billing system
    (e.g. Stripe metered billing, AWS Marketplace).  Replace the in-memory
    dict with a Redis / DynamoDB store for multi-instance deployments.

Example
-------
>>> from media_engine.api_endpoints import create_app
>>> app = create_app(api_keys={"test-key-123"}, host="127.0.0.1", port=8080)
>>> app.run()   # blocks — use app.run_background() for tests
"""

from __future__ import annotations

import json
import threading
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Callable, Dict, Optional, Set
from urllib.parse import urlparse

from media_engine import __version__
from media_engine.ai_tagger import MediaAnalyzer
from media_engine.ingestion import MediaIngestionAdapter
from media_engine.processing import MediaProcessingPipeline, ProcessingOptions

# ---------------------------------------------------------------------------
# Monetisation: API key middleware & usage tracker
# ---------------------------------------------------------------------------


class UsageTracker:
    """
    Thread-safe in-memory API call counter per API key.

    In production swap the ``_counts`` dict for a Redis ``INCR`` call or a
    DynamoDB atomic counter so that all replicas share the same tally.
    """

    def __init__(self) -> None:
        self._counts: Dict[str, int] = defaultdict(int)
        self._lock = threading.Lock()

    def record(self, api_key: str) -> None:
        with self._lock:
            self._counts[api_key] += 1

    def get_count(self, api_key: str) -> int:
        with self._lock:
            return self._counts[api_key]

    def summary(self) -> Dict[str, int]:
        with self._lock:
            return dict(self._counts)


class APIKeyMiddleware:
    """
    Validates the ``X-API-Key`` request header.

    Parameters
    ----------
    allowed_keys : Set of valid API key strings.  Pass an empty set to disable
                   key checking (development mode).
    """

    def __init__(self, allowed_keys: Optional[Set[str]] = None) -> None:
        self._keys: Set[str] = set(allowed_keys) if allowed_keys else set()
        self._auth_enabled = bool(allowed_keys)

    def validate(self, key: Optional[str]) -> tuple[bool, str]:
        """Return (is_valid, error_message)."""
        if not self._auth_enabled:
            return True, ""
        if key is None:
            return False, "Missing X-API-Key header"
        if key not in self._keys:
            return False, "Invalid or expired API key"
        return True, ""


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------

HandlerFn = Callable[["RequestContext"], Dict[str, Any]]


class RequestContext:
    """Thin abstraction over a raw HTTP request for use by route handlers."""

    def __init__(self, method: str, path: str, body: bytes, headers: Dict[str, str]) -> None:
        self.method = method
        self.path = path
        self.headers = headers
        self._body = body

    def json(self) -> Any:
        """Parse request body as JSON."""
        return json.loads(self._body.decode()) if self._body else {}


class Router:
    """
    Minimal HTTP router.

    Routes are registered as ``(METHOD, path_prefix)`` tuples.  The first
    matching route wins.
    """

    def __init__(self) -> None:
        self._routes: list[tuple[str, str, HandlerFn]] = []

    def add(self, method: str, path: str, handler: HandlerFn) -> None:
        self._routes.append((method.upper(), path, handler))

    def dispatch(self, ctx: RequestContext) -> tuple[int, Dict[str, Any]]:
        for method, path, handler in self._routes:
            if ctx.method == method and ctx.path == path:
                try:
                    return 200, handler(ctx)
                except (KeyError, ValueError) as exc:
                    return 400, {"error": str(exc)}
                except FileNotFoundError as exc:
                    return 404, {"error": str(exc)}
                except Exception as exc:  # noqa: BLE001
                    return 500, {"error": f"Internal server error: {exc}"}
        return 404, {"error": f"Route not found: {ctx.method} {ctx.path}"}


# ---------------------------------------------------------------------------
# Endpoint handler functions
# ---------------------------------------------------------------------------


def _make_handlers(
    adapter: MediaIngestionAdapter,
    pipeline: MediaProcessingPipeline,
    analyzer: MediaAnalyzer,
) -> Router:
    router = Router()

    # ---- GET /api/v1/health ------------------------------------------------
    def health(_ctx: RequestContext) -> Dict[str, Any]:
        return {"status": "ok", "version": __version__}

    router.add("GET", "/api/v1/health", health)

    # ---- GET /api/v1/operations --------------------------------------------
    def operations(_ctx: RequestContext) -> Dict[str, Any]:
        return {"operations": pipeline.available_operations}

    router.add("GET", "/api/v1/operations", operations)

    # ---- POST /api/v1/ingest -----------------------------------------------
    def ingest(ctx: RequestContext) -> Dict[str, Any]:
        body = ctx.json()
        source: str = body["source"]
        media = adapter.ingest(source) if "://" not in source else adapter.ingest_url(source)
        return {
            "media_id": media.media_id,
            "media_type": media.media_type,
            "format": media.format,
            "size_bytes": media.size_bytes,
            "source": media.source,
            "metadata": media.metadata,
            "ingested_at": media.ingested_at.isoformat(),
        }

    router.add("POST", "/api/v1/ingest", ingest)

    # ---- POST /api/v1/process ----------------------------------------------
    def process(ctx: RequestContext) -> Dict[str, Any]:
        body = ctx.json()
        source: str = body["source"]
        ops: list[str] = body.get("operations", ["compress"])
        raw_opts: dict = body.get("options", {})
        valid_fields = set(ProcessingOptions.__dataclass_fields__)
        unknown_opts = set(raw_opts) - valid_fields
        if unknown_opts:
            raise ValueError(f"Unknown options: {sorted(unknown_opts)}. Valid: {sorted(valid_fields)}")
        opts = ProcessingOptions(**{k: v for k, v in raw_opts.items() if k in valid_fields})
        media = adapter.ingest(source)
        result = pipeline.process(media, operations=ops, options=opts)
        return {
            "source_media_id": result.source_media_id,
            "operations": result.operations,
            "output_format": result.output_format,
            "output_size_bytes": result.output_size_bytes,
            "processing_log": result.processing_log,
            "metadata": result.metadata,
        }

    router.add("POST", "/api/v1/process", process)

    # ---- POST /api/v1/analyze ----------------------------------------------
    def analyze(ctx: RequestContext) -> Dict[str, Any]:
        body = ctx.json()
        source: str = body["source"]
        media = adapter.ingest(source)
        result = analyzer.analyze(media)
        return result.to_dict()

    router.add("POST", "/api/v1/analyze", analyze)

    return router


# ---------------------------------------------------------------------------
# HTTP request handler
# ---------------------------------------------------------------------------


class _MediaEngineHandler(BaseHTTPRequestHandler):
    """``BaseHTTPRequestHandler`` subclass wired to the router + middleware."""

    # Set by MediaEngineAPIServer before first request
    router: Router
    middleware: APIKeyMiddleware
    usage: UsageTracker

    def log_message(self, fmt: str, *args: Any) -> None:  # noqa: D401
        pass  # suppress default access-log noise; replace with real logger

    def _send_json(self, status: int, data: Dict[str, Any]) -> None:
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _handle(self, method: str) -> None:
        api_key = self.headers.get("X-API-Key")
        valid, err = self.middleware.validate(api_key)
        if not valid:
            status = 401 if "Missing" in err else 403
            self._send_json(status, {"error": err})
            return
        if api_key:
            self.usage.record(api_key)

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b""
        path = urlparse(self.path).path
        ctx = RequestContext(
            method=method, path=path, body=body,
            headers=dict(self.headers),
        )
        status, response = self.router.dispatch(ctx)
        self._send_json(status, response)

    def do_GET(self) -> None:
        self._handle("GET")

    def do_POST(self) -> None:
        self._handle("POST")


# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------


class MediaEngineAPIServer:
    """
    Wraps ``HTTPServer`` with the Media Engine router.

    Parameters
    ----------
    api_keys : Set of accepted API key strings.  Pass ``None`` or empty set
               to disable authentication (useful for local development).
    host     : Bind address (default ``"0.0.0.0"``).
    port     : Listen port (default ``8080``).
    """

    def __init__(
        self,
        api_keys: Optional[Set[str]] = None,
        host: str = "0.0.0.0",
        port: int = 8080,
    ) -> None:
        self.host = host
        self.port = port
        self.usage = UsageTracker()
        middleware = APIKeyMiddleware(api_keys)

        adapter = MediaIngestionAdapter()
        pipeline = MediaProcessingPipeline()
        analyzer = MediaAnalyzer()
        router = _make_handlers(adapter, pipeline, analyzer)

        # Inject dependencies into the handler class via class attributes
        _MediaEngineHandler.router = router
        _MediaEngineHandler.middleware = middleware
        _MediaEngineHandler.usage = self.usage

        self._server = HTTPServer((host, port), _MediaEngineHandler)

    def run(self) -> None:
        """Start the server (blocks until interrupted)."""
        print(f"Media Engine API listening on http://{self.host}:{self.port}")
        try:
            self._server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down.")
        finally:
            self._server.server_close()

    def run_background(self) -> threading.Thread:
        """Start the server in a daemon thread (returns the thread)."""
        thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        thread.start()
        return thread

    def shutdown(self) -> None:
        """Stop the server."""
        self._server.shutdown()
        self._server.server_close()


def create_app(
    api_keys: Optional[Set[str]] = None,
    host: str = "0.0.0.0",
    port: int = 8080,
) -> MediaEngineAPIServer:
    """
    Factory function — create and return a ``MediaEngineAPIServer``.

    This is the recommended entry-point for all deployment scenarios.

    Example
    -------
    >>> app = create_app(api_keys={"prod-key-abc"}, port=8080)
    >>> app.run()
    """
    return MediaEngineAPIServer(api_keys=api_keys, host=host, port=port)
