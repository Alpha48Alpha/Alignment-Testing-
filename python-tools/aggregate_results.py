"""
aggregate_results.py

Compute per-domain and per-metric aggregate statistics from a scored results
file produced by score_responses.py.

Usage:
    python aggregate_results.py --input scores.json
    python aggregate_results.py --input scores.json --output summary.json

Output (printed to stdout and optionally written to JSON):
    Per-domain breakdown:
        Domain          | N | Avg AC | Avg RQ | Avg IF | Avg HR | Avg CL | Avg Agg
        technical       | 40| 2.6    | 2.4    | 2.8    | 2.5    | 2.7    | 85.3%
        educational     | 30| 2.7    | 2.5    | 2.9    | 2.8    | 2.9    | 89.1%
        general         | 30| 2.5    | 2.3    | 2.7    | 2.6    | 2.8    | 84.7%
        OVERALL         |100| 2.6    | 2.4    | 2.8    | 2.6    | 2.8    | 86.1%
"""

import argparse
import json
from collections import defaultdict


METRICS = ["AC", "RQ", "IF", "HR", "CL"]


def avg(values: list[float]) -> float | None:
    if not values:
        return None
    return round(sum(values) / len(values), 2)


def compute_domain_stats(items: list[dict]) -> dict:
    """Return per-domain and overall statistics."""
    by_domain: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        domain = item.get("domain", "unknown")
        by_domain[domain].append(item)

    stats: dict[str, dict] = {}
    all_items = list(items)

    domains_to_process = list(by_domain.items()) + [("OVERALL", all_items)]

    for domain, domain_items in domains_to_process:
        metric_values: dict[str, list[float]] = {m: [] for m in METRICS}
        aggregates: list[float] = []

        for item in domain_items:
            scores = item.get("scores", {})
            for metric in METRICS:
                score = scores.get(metric)
                if score is not None:
                    metric_values[metric].append(float(score))
            agg = item.get("aggregate")
            if agg is not None:
                aggregates.append(float(agg))

        stats[domain] = {
            "n": len(domain_items),
            **{f"avg_{m}": avg(metric_values[m]) for m in METRICS},
            "avg_aggregate": avg(aggregates),
        }

    return stats


def print_table(stats: dict) -> None:
    header = f"{'Domain':<16} {'N':>5} {'AC':>6} {'RQ':>6} {'IF':>6} {'HR':>6} {'CL':>6} {'Agg%':>8}"
    print(header)
    print("-" * len(header))

    domains = [d for d in stats if d != "OVERALL"] + ["OVERALL"]
    for domain in domains:
        s = stats[domain]
        def fmt(v):
            return f"{v:.2f}" if v is not None else "  N/A"
        def fmt_pct(v):
            return f"{v:.1f}%" if v is not None else "   N/A"
        row = (
            f"{domain:<16} {s['n']:>5} "
            f"{fmt(s['avg_AC']):>6} "
            f"{fmt(s['avg_RQ']):>6} "
            f"{fmt(s['avg_IF']):>6} "
            f"{fmt(s['avg_HR']):>6} "
            f"{fmt(s['avg_CL']):>6} "
            f"{fmt_pct(s['avg_aggregate']):>8}"
        )
        if domain == "OVERALL":
            print("-" * len(header))
        print(row)


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate scored evaluation results")
    parser.add_argument("--input", required=True, help="Path to scored results JSON file")
    parser.add_argument("--output", help="Optional path to write summary JSON file")
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        items = json.load(f)

    if not items:
        print("No items found in input file.")
        return

    scored_items = [item for item in items if "scores" in item]
    if not scored_items:
        print("No scored items found. Run score_responses.py first.")
        return

    print(f"\nAggregating {len(scored_items)} scored items...\n")
    stats = compute_domain_stats(scored_items)
    print_table(stats)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        print(f"\nSummary written to {args.output}")


if __name__ == "__main__":
    main()
