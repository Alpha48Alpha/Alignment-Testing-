"""
media_engine.ingestion
======================
Multi-format media ingestion layer.

Responsibilities
----------------
- Accept media from a file path, URL, or raw bytes.
- Detect and validate the media type (image / audio / video).
- Normalise incoming data into a uniform ``MediaObject`` that the rest of
  the pipeline can consume without caring about the original format.

Supported formats
-----------------
Images : JPEG, PNG, GIF, WEBP, BMP, TIFF
Audio  : MP3, WAV, FLAC, AAC, OGG
Video  : MP4, MOV, AVI, MKV, WEBM
"""

from __future__ import annotations

import hashlib
import mimetypes
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse
from urllib.request import urlopen

# ---------------------------------------------------------------------------
# Public constants
# ---------------------------------------------------------------------------

IMAGE_FORMATS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff"}
AUDIO_FORMATS = {".mp3", ".wav", ".flac", ".aac", ".ogg"}
VIDEO_FORMATS = {".mp4", ".mov", ".avi", ".mkv", ".webm"}

ALL_SUPPORTED_FORMATS = IMAGE_FORMATS | AUDIO_FORMATS | VIDEO_FORMATS


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class MediaObject:
    """
    Normalised container for an ingested media item.

    Attributes
    ----------
    media_id    : Unique SHA-256 identifier derived from file content.
    media_type  : One of "image", "audio", or "video".
    format      : Lower-case file extension (e.g. "mp4", "png").
    source      : Original file path or URL.
    size_bytes  : Size of the raw content in bytes.
    content     : Raw bytes of the media file.
    metadata    : Arbitrary key-value pairs (filename, mime_type, …).
    ingested_at : UTC timestamp of ingestion.
    """

    media_id: str
    media_type: str
    format: str
    source: str
    size_bytes: int
    content: bytes
    metadata: dict = field(default_factory=dict)
    ingested_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return (
            f"MediaObject(id={self.media_id[:8]}…, "
            f"type={self.media_type}, format={self.format}, "
            f"size={self.size_bytes:,} bytes)"
        )


# ---------------------------------------------------------------------------
# Ingestion adapter
# ---------------------------------------------------------------------------


class MediaIngestionAdapter:
    """
    Entry-point for all media ingestion.

    Supports three intake modes:

    1. ``ingest(path)``          — local file path (``str`` or ``pathlib.Path``).
    2. ``ingest_url(url)``       — remote URL (http/https).
    3. ``ingest_bytes(content, filename)`` — raw bytes with a hint filename.

    All three modes return a ``MediaObject`` ready for downstream processing.

    Example
    -------
    >>> adapter = MediaIngestionAdapter()
    >>> obj = adapter.ingest("sample.mp4")
    >>> print(obj.media_type)   # "video"
    """

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def ingest(self, path: str | os.PathLike) -> MediaObject:
        """Ingest a media file from a local path."""
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Media file not found: {file_path}")
        content = file_path.read_bytes()
        return self._build_media_object(content, str(file_path), file_path.name)

    def ingest_url(self, url: str, timeout: int = 30) -> MediaObject:
        """Ingest a media file by downloading it from a URL."""
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            raise ValueError(f"Unsupported URL scheme: {parsed.scheme!r}")
        with urlopen(url, timeout=timeout) as response:  # noqa: S310
            content = response.read()
        filename = os.path.basename(parsed.path) or "download"
        return self._build_media_object(content, url, filename)

    def ingest_bytes(self, content: bytes, filename: str) -> MediaObject:
        """Ingest raw bytes directly, using *filename* to detect the format."""
        return self._build_media_object(content, f"bytes://{filename}", filename)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _build_media_object(
        self, content: bytes, source: str, filename: str
    ) -> MediaObject:
        ext = Path(filename).suffix.lower()
        media_type = self._detect_type(ext, filename)
        if media_type is None:
            raise ValueError(
                f"Unsupported format: {ext!r}. "
                f"Supported: {', '.join(sorted(ALL_SUPPORTED_FORMATS))}"
            )
        media_id = hashlib.sha256(content).hexdigest()
        mime_type, _ = mimetypes.guess_type(filename)
        return MediaObject(
            media_id=media_id,
            media_type=media_type,
            format=ext.lstrip("."),
            source=source,
            size_bytes=len(content),
            content=content,
            metadata={"filename": filename, "mime_type": mime_type or "application/octet-stream"},
        )

    @staticmethod
    def _detect_type(ext: str, filename: str) -> Optional[str]:
        if ext in IMAGE_FORMATS:
            return "image"
        if ext in AUDIO_FORMATS:
            return "audio"
        if ext in VIDEO_FORMATS:
            return "video"
        return None
