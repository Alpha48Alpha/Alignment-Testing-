#!/usr/bin/env python3
"""
tools/run_benchmark.py — LLM Evaluation Lab benchmark runner.

Loads a benchmark JSON file, runs each prompt against a model runner, scores
responses using the item rubric, writes a JSON results artifact, and prints a
concise pass/fail summary.

Modes
-----
mock (default)
    No API key required.  Uses a built-in oracle that derives the correct
    numeric answer from the rubric so the benchmark always passes in CI and
    demo runs.

openai
    Calls an OpenAI-compatible chat completions endpoint using only Python
    stdlib (urllib).  Requires the following environment variables:

        OPENAI_BASE_URL   e.g. https://api.openai.com/v1
        OPENAI_API_KEY    e.g. sk-...
        OPENAI_MODEL      e.g. gpt-4o

Usage
-----
    # Mock mode (no credentials needed)
    python tools/run_benchmark.py \\
        --benchmark benchmarks/reasoning/widgets.json \\
        --out results/widgets_results.json

    # OpenAI-compatible endpoint
    OPENAI_BASE_URL=https://api.openai.com/v1 \\
    OPENAI_API_KEY=sk-... \\
    OPENAI_MODEL=gpt-4o \\
    python tools/run_benchmark.py \\
        --benchmark benchmarks/reasoning/widgets.json \\
        --out results/widgets_results.json \\
        --mode openai
"""

import argparse
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


# ---------------------------------------------------------------------------
# Scoring helpers
# ---------------------------------------------------------------------------

def _extract_first_number(text: str) -> float | None:
    """Return the first integer or decimal number found in *text*, or None."""
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    return float(match.group()) if match else None


def score_response(response: str, rubric: dict) -> bool:
    """Return True if *response* satisfies *rubric*."""
    rtype = rubric.get("type", "exact")
    value = rubric.get("value")
    tolerance = rubric.get("tolerance", 0)

    if rtype == "numeric":
        parsed = _extract_first_number(response)
        if parsed is None:
            return False
        return abs(parsed - float(value)) <= tolerance

    if rtype == "contains":
        return str(value).lower() in response.lower()

    # default: exact (case-insensitive, stripped)
    return response.strip().lower() == str(value).strip().lower()


# ---------------------------------------------------------------------------
# Model runners
# ---------------------------------------------------------------------------

def run_mock(prompt: str, item: dict) -> str:
    """
    Mock runner — returns the correct answer derived from the rubric so that
    benchmarks pass without any API credentials.  This is intentional: the
    mock mode exists to validate tooling and demonstrate artifacts, not to
    evaluate a real model.
    """
    rubric = item.get("rubric", {})
    rtype = rubric.get("type", "exact")
    value = rubric.get("value")

    if rtype == "numeric":
        # Wrap the correct value in a sentence so the scorer must parse it.
        return f"The answer is {value}."
    if rtype == "contains":
        return f"The response contains the keyword: {value}."
    # exact
    return str(value)


def run_openai(prompt: str, item: dict, base_url: str, api_key: str, model: str) -> str:
    """
    Call an OpenAI-compatible chat completions endpoint using urllib (no
    third-party dependencies).  Returns the assistant message content.
    """
    url = base_url.rstrip("/") + "/chat/completions"
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from model endpoint: {body}") from exc

    return data["choices"][0]["message"]["content"]


# ---------------------------------------------------------------------------
# Main benchmark loop
# ---------------------------------------------------------------------------

def run_benchmark(benchmark_path: str, out_path: str, mode: str) -> None:
    """Load the benchmark, run every item, score responses, write results."""

    # --- load benchmark ---
    with open(benchmark_path, encoding="utf-8") as fh:
        items = json.load(fh)

    if not isinstance(items, list) or len(items) == 0:
        print("ERROR: benchmark file must be a non-empty JSON array.", file=sys.stderr)
        sys.exit(1)

    # --- resolve OpenAI credentials if needed ---
    openai_base_url = os.environ.get("OPENAI_BASE_URL", "").strip()
    openai_api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    openai_model = os.environ.get("OPENAI_MODEL", "gpt-4o").strip()

    if mode == "openai":
        missing = [
            name for name, val in [
                ("OPENAI_BASE_URL", openai_base_url),
                ("OPENAI_API_KEY", openai_api_key),
            ]
            if not val
        ]
        if missing:
            print(
                f"ERROR: --mode openai requires environment variables: {', '.join(missing)}",
                file=sys.stderr,
            )
            sys.exit(1)

    # --- run items ---
    result_items: list[dict] = []
    passed = 0

    print(f"\nRunning benchmark: {benchmark_path}  [mode={mode}]")
    print(f"{'ID':<20} {'PASS':<6} {'EXPECTED':<12} {'RESPONSE'}")
    print("-" * 72)

    for item in items:
        item_id = item.get("id", "?")
        prompt = item.get("prompt", "")
        expected = str(item.get("expected_answer", ""))
        rubric = item.get("rubric", {"type": "exact", "value": expected})

        # Run the prompt through the selected runner.
        if mode == "mock":
            response = run_mock(prompt, item)
        else:
            response = run_openai(prompt, item, openai_base_url, openai_api_key, openai_model)

        ok = score_response(response, rubric)
        if ok:
            passed += 1

        # Truncate response for display (keep output readable).
        display_resp = (response[:40] + "…") if len(response) > 41 else response
        print(f"{item_id:<20} {'✓' if ok else '✗':<6} {expected:<12} {display_resp}")

        result_items.append({
            "id": item_id,
            "prompt": prompt,
            "response": response,
            "expected": expected,
            "pass": ok,
            "rubric_type": rubric.get("type", "exact"),
        })

    total = len(result_items)
    score_pct = round(passed / total * 100, 1) if total > 0 else 0.0

    print("-" * 72)
    print(f"Result: {passed}/{total} passed  ({score_pct}%)\n")

    # --- write artifact ---
    artifact = {
        "benchmark": benchmark_path,
        "mode": mode,
        "model": openai_model if mode == "openai" else "mock",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "summary": {
            "total": total,
            "passed": passed,
            "failed": total - passed,
            "score_pct": score_pct,
        },
        "items": result_items,
    }

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(artifact, fh, indent=2)

    print(f"Results written to: {out_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run an LLM Evaluation Lab benchmark and write a results artifact.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--benchmark",
        required=True,
        metavar="FILE",
        help="Path to the benchmark JSON file.",
    )
    parser.add_argument(
        "--out",
        required=True,
        metavar="FILE",
        help="Path for the output results JSON artifact.",
    )
    parser.add_argument(
        "--mode",
        choices=["mock", "openai"],
        default="mock",
        help="Runner mode: 'mock' (default, no credentials) or 'openai'.",
    )
    return parser


if __name__ == "__main__":
    args = _build_parser().parse_args()
    run_benchmark(args.benchmark, args.out, args.mode)
