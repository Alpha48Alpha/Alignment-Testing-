"""
score_responses.py

Score a set of model responses against the five evaluation metrics:
    AC  Accuracy
    RQ  Reasoning Quality
    IF  Instruction Following
    HR  Hallucination Rate  (inverted: 3 = no hallucinations)
    CL  Clarity

This script provides an interactive scoring workflow. For each response, it
displays the prompt and response, then prompts the evaluator to enter scores
for each applicable metric (0–3 integer).

Usage:
    python score_responses.py --input responses.json --output scores.json

Input format (responses.json):
    Output of prompt_tester.py — a list of objects each containing at least
    'id', 'prompt', 'response', and 'metric'.

Output format (scores.json):
    Same list with an added 'scores' object per item:
    {
        "id": "PS1-A",
        "prompt": "...",
        "response": "...",
        "scores": {"AC": 3, "RQ": 2, "IF": null, "HR": 3, "CL": 3},
        "aggregate": 91.7
    }

    A null score means the metric was marked not applicable.
"""

import argparse
import json
import sys


METRICS = [
    ("AC", "Accuracy"),
    ("RQ", "Reasoning Quality"),
    ("IF", "Instruction Following"),
    ("HR", "Hallucination Rate (3=none, 0=severe)"),
    ("CL", "Clarity"),
]


def prompt_score(metric_abbr: str, metric_name: str) -> int | None:
    """
    Ask the evaluator for a score (0–3) for one metric.
    Returns None if the evaluator marks the metric as not applicable.
    """
    while True:
        raw = input(f"  {metric_abbr} — {metric_name} [0-3, or 'n' for N/A]: ").strip().lower()
        if raw in ("n", "na", "n/a", ""):
            return None
        try:
            score = int(raw)
        except ValueError:
            print("  Enter an integer 0–3 or 'n' for not applicable.")
            continue
        if 0 <= score <= 3:
            return score
        print("  Score must be 0, 1, 2, or 3.")


def compute_aggregate(scores: dict[str, int | None]) -> float | None:
    applicable = [v for v in scores.values() if v is not None]
    if not applicable:
        return None
    return round(sum(applicable) / (len(applicable) * 3) * 100, 1)


def score_item(item: dict, index: int, total: int) -> dict:
    print(f"\n{'='*60}")
    print(f"Item {index}/{total}  [{item.get('id', '?')}]")
    print(f"Domain: {item.get('domain', '?')}  |  Metric focus: {item.get('metric', '?')}")
    print(f"\nPROMPT:\n{item.get('prompt', '')}")
    print(f"\nRESPONSE:\n{item.get('response', '')}")
    print()

    scores: dict[str, int | None] = {}
    for abbr, name in METRICS:
        scores[abbr] = prompt_score(abbr, name)

    aggregate = compute_aggregate(scores)
    scored_item = {**item, "scores": scores, "aggregate": aggregate}
    print(f"  → Aggregate: {aggregate}%")
    return scored_item


def main() -> None:
    parser = argparse.ArgumentParser(description="Interactively score model responses")
    parser.add_argument("--input", required=True, help="Path to responses JSON file")
    parser.add_argument("--output", required=True, help="Path to write scored results")
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip items that already have a 'scores' key in the output file",
    )
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        items = json.load(f)

    already_scored: dict[str, dict] = {}
    if args.resume:
        try:
            with open(args.output, encoding="utf-8") as f:
                existing = json.load(f)
            already_scored = {item["id"]: item for item in existing if "scores" in item}
            print(f"Resuming: {len(already_scored)} items already scored.")
        except FileNotFoundError:
            pass

    results = []
    pending = [item for item in items if item.get("id") not in already_scored]

    print(f"\n{len(pending)} items to score. Enter scores 0–3 or 'n' for not applicable.\n")

    for i, item in enumerate(pending, start=1):
        try:
            scored = score_item(item, i, len(pending))
            results.append(scored)
            # Write incrementally so progress is not lost on interrupt
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(list(already_scored.values()) + results, f, indent=2, ensure_ascii=False)
        except KeyboardInterrupt:
            print("\n\nScoring interrupted. Progress saved.")
            sys.exit(0)

    print(f"\nScoring complete. {len(results)} new items scored. Results written to {args.output}")


if __name__ == "__main__":
    main()
