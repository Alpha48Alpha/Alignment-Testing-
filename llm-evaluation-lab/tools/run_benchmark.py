"""
run_benchmark.py — Simple LLM benchmark runner.

Loads prompts from a dataset file, runs placeholder evaluation logic,
stores results, and prints a scored summary.

Usage:
    python tools/run_benchmark.py [--dataset PATH] [--output PATH]

The script is intentionally model-agnostic: replace the `evaluate_response`
stub with a real API call (OpenAI, Anthropic, etc.) to score live responses.
"""

import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# Default paths (relative to the repo root)
# ---------------------------------------------------------------------------
DEFAULT_DATASET = os.path.join(
    os.path.dirname(__file__), "..", "datasets", "sample_prompts.json"
)
DEFAULT_OUTPUT = os.path.join(
    os.path.dirname(__file__), "..", "results", "benchmark_results.csv"
)


# ---------------------------------------------------------------------------
# Evaluation metrics
# ---------------------------------------------------------------------------
METRICS = [
    "accuracy",
    "reasoning_quality",
    "instruction_following",
    "hallucination_rate",
    "clarity",
]


def score_response(prompt: dict, response: str) -> dict[str, int]:
    """
    Score a single response across all evaluation metrics (0–3 each).

    Replace this stub with real scoring logic or a judge-model call.
    Currently returns the expected scores from the prompt definition when
    available, otherwise defaults to 0.

    Args:
        prompt: Prompt dict containing optional ``expected_scores`` mapping
                metric names to integer scores 0–3.
        response: The model's response text (unused by this stub).

    Returns:
        dict mapping each metric name to an integer score in the range 0–3.
    """
    expected = prompt.get("expected_scores", {})
    return {metric: int(expected.get(metric, 0)) for metric in METRICS}


def aggregate_score(scores: dict[str, int]) -> float:
    """Return an aggregate percentage score across all applicable metrics."""
    applicable = [v for v in scores.values() if v >= 0]
    if not applicable:
        return 0.0
    return sum(applicable) / (len(applicable) * 3) * 100


def evaluate_response(prompt: dict) -> str:
    """
    Obtain a model response for the given prompt.

    Replace this stub with a real API call, e.g.:
        import openai
        completion = openai.chat.completions.create(...)
        return completion.choices[0].message.content

    Args:
        prompt: Prompt dict containing the ``prompt`` text and an optional
                ``sample_response`` field used by this stub.

    Returns:
        The model's response as a plain string.
    """
    return prompt.get("sample_response", "")


# ---------------------------------------------------------------------------
# Dataset helpers
# ---------------------------------------------------------------------------
def load_dataset(path: str) -> list[dict]:
    """Load prompts from a JSON file.  Returns an empty list on failure."""
    if not os.path.exists(path):
        print(f"[warn] Dataset not found: {path}", file=sys.stderr)
        return []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        print("[warn] Dataset must be a JSON array.", file=sys.stderr)
        return []
    return data


def save_results(results: list[dict], path: str) -> None:
    """Write scored results to a CSV file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fieldnames = ["id", "category", "prompt", "response"] + METRICS + ["aggregate"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"[info] Results saved to {path}")


# ---------------------------------------------------------------------------
# Main benchmark loop
# ---------------------------------------------------------------------------
def run_benchmark(dataset_path: str, output_path: str) -> list[dict]:
    """Load prompts, evaluate responses, score them, and return results."""
    prompts = load_dataset(dataset_path)
    if not prompts:
        print("[info] No prompts to evaluate.")
        return []

    results = []
    print(f"[info] Running benchmark on {len(prompts)} prompt(s)…\n")

    for prompt in prompts:
        prompt_id = prompt.get("id", "unknown")
        category = prompt.get("category", "general")
        text = prompt.get("prompt", "")

        response = evaluate_response(prompt)
        scores = score_response(prompt, response)
        agg = aggregate_score(scores)

        row = {
            "id": prompt_id,
            "category": category,
            "prompt": text,
            "response": response,
            **scores,
            "aggregate": round(agg, 1),
        }
        results.append(row)

        print(
            f"  [{prompt_id}] {category} — aggregate: {agg:.1f}%"
            f"  scores: {scores}"
        )

    print()
    return results


def print_summary(results: list[dict]) -> None:
    """Print a simple summary table to stdout."""
    if not results:
        return
    avg_agg = sum(r["aggregate"] for r in results) / len(results)
    by_category: dict[str, list[float]] = {}
    for r in results:
        by_category.setdefault(r["category"], []).append(r["aggregate"])

    print("=" * 50)
    print("Benchmark Summary")
    print(f"  Timestamp : {datetime.now(timezone.utc).isoformat()}")
    print(f"  Prompts   : {len(results)}")
    print(f"  Avg score : {avg_agg:.1f}%")
    print()
    print("  By category:")
    for cat, scores in sorted(by_category.items()):
        print(f"    {cat:<25} {sum(scores)/len(scores):.1f}%")
    print("=" * 50)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run LLM evaluation benchmarks and store scored results."
    )
    parser.add_argument(
        "--dataset",
        default=DEFAULT_DATASET,
        help="Path to the JSON prompt dataset (default: datasets/sample_prompts.json)",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="Path for the CSV results file (default: results/benchmark_results.csv)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    results = run_benchmark(args.dataset, args.output)
    print_summary(results)
    if results:
        save_results(results, args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
