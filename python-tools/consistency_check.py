"""
consistency_check.py

Compute consistency scores across prompt variants.

Consistency measures how stable a model's performance is across semantically
equivalent prompt variants. A prompt set is considered consistent if the
difference in aggregate scores across variants is <= 0.5 points on the 0-3 scale.

See evaluation-framework/README.md for the full consistency methodology.

Usage:
    python3 consistency_check.py
"""

import statistics
from typing import Optional
from evaluator import Score, EvaluatedResponse, compute_consistency


# ---------------------------------------------------------------------------
# Consistency analysis
# ---------------------------------------------------------------------------

def analyze_consistency(
    results: dict[str, list[EvaluatedResponse]]
) -> dict[str, dict]:
    """
    Compute per-prompt-set and overall consistency statistics.

    Returns a dict mapping set name to its consistency analysis, plus an
    'overall' key with aggregate statistics.
    """
    analysis: dict[str, dict] = {}
    consistent_count = 0
    all_max_diffs: list[float] = []

    for set_name, responses in results.items():
        consistency = compute_consistency(responses)
        analysis[set_name] = consistency
        if consistency["consistent"]:
            consistent_count += 1
        all_max_diffs.append(consistency["max_difference"])

    total = len(results)
    analysis["overall"] = {
        "total_prompt_sets": total,
        "consistent_sets": consistent_count,
        "consistency_rate": round(consistent_count / total * 100, 1) if total > 0 else 0.0,
        "mean_max_difference": round(statistics.mean(all_max_diffs), 3) if all_max_diffs else 0.0,
        "stdev_max_difference": (
            round(statistics.stdev(all_max_diffs), 3) if len(all_max_diffs) > 1 else 0.0
        ),
    }

    return analysis


def print_consistency_report(analysis: dict[str, dict]) -> None:
    """Print a formatted consistency report."""
    print("\n" + "=" * 60)
    print("CONSISTENCY REPORT")
    print("=" * 60)

    overall = analysis.get("overall", {})

    for set_name, data in analysis.items():
        if set_name == "overall":
            continue
        status = "✓ CONSISTENT" if data["consistent"] else "✗ INCONSISTENT"
        print(f"\n  {set_name}")
        print(f"    Status:         {status}")
        print(f"    Aggregates:     {data['aggregates']}")
        print(f"    Max diff (0-3): {data['max_difference']}")

    print("\n" + "-" * 60)
    print("Overall")
    print(f"  Prompt sets evaluated:  {overall.get('total_prompt_sets', 0)}")
    print(f"  Consistent sets:        {overall.get('consistent_sets', 0)}")
    print(f"  Consistency rate:       {overall.get('consistency_rate', 0.0)}%")
    print(f"  Mean max diff (0-3):    {overall.get('mean_max_difference', 0.0)}")
    print(f"  Stdev max diff (0-3):   {overall.get('stdev_max_difference', 0.0)}")
    print()


# ---------------------------------------------------------------------------
# Example data: simulate a comparison of baseline vs. improved prompt sets
# ---------------------------------------------------------------------------

def make_scored_responses(
    set_name: str,
    variant_scores: list[tuple[Optional[int], Optional[int], Optional[int], Optional[int], Optional[int]]],
) -> list[EvaluatedResponse]:
    """Helper to build EvaluatedResponse objects from (AC, RQ, IF, HR, CL) tuples."""
    responses = []
    for i, (ac, rq, inf, hr, cl) in enumerate(variant_scores):
        responses.append(EvaluatedResponse(
            prompt_set_name=set_name,
            variant_index=i,
            prompt=f"[prompt variant {i + 1}]",
            response=f"[response variant {i + 1}]",
            score=Score(
                accuracy=ac,
                reasoning_quality=rq,
                instruction_following=inf,
                hallucination_rate=hr,
                clarity=cl,
            ),
        ))
    return responses


# Simulated baseline results (before prompt refinement)
BASELINE_RESULTS: dict[str, list[EvaluatedResponse]] = {
    "fact_recall_01": make_scored_responses(
        "fact_recall_01", [(3, None, 3, 3, 3), (3, None, 2, 3, 3)]
    ),
    "reasoning_02": make_scored_responses(
        "reasoning_02", [(2, 1, 2, 3, 2), (3, 3, 3, 3, 3)]
    ),
    "instruction_03": make_scored_responses(
        "instruction_03", [(3, None, 1, 3, 2), (3, None, 3, 3, 3)]
    ),
    "hallucination_04": make_scored_responses(
        "hallucination_04", [(2, None, 3, 1, 2), (2, None, 3, 2, 2)]
    ),
    "multi_constraint_05": make_scored_responses(
        "multi_constraint_05", [(3, 2, 1, 3, 2), (3, 2, 2, 3, 2)]
    ),
}

# Simulated improved results (after prompt refinement)
IMPROVED_RESULTS: dict[str, list[EvaluatedResponse]] = {
    "fact_recall_01": make_scored_responses(
        "fact_recall_01", [(3, None, 3, 3, 3), (3, None, 3, 3, 3)]
    ),
    "reasoning_02": make_scored_responses(
        "reasoning_02", [(3, 3, 3, 3, 3), (3, 3, 3, 3, 3)]
    ),
    "instruction_03": make_scored_responses(
        "instruction_03", [(3, None, 3, 3, 3), (3, None, 3, 3, 3)]
    ),
    "hallucination_04": make_scored_responses(
        "hallucination_04", [(2, None, 3, 2, 2), (2, None, 3, 2, 2)]
    ),
    "multi_constraint_05": make_scored_responses(
        "multi_constraint_05", [(3, 2, 3, 3, 3), (3, 2, 3, 3, 3)]
    ),
}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Baseline consistency (before prompt refinement):")
    baseline_analysis = analyze_consistency(BASELINE_RESULTS)
    print_consistency_report(baseline_analysis)

    print("Improved consistency (after prompt refinement):")
    improved_analysis = analyze_consistency(IMPROVED_RESULTS)
    print_consistency_report(improved_analysis)

    baseline_rate = baseline_analysis["overall"]["consistency_rate"]
    improved_rate = improved_analysis["overall"]["consistency_rate"]
    if baseline_rate > 0:
        relative_improvement = round((improved_rate - baseline_rate) / baseline_rate * 100, 1)
        print(
            f"Relative improvement in consistency rate: "
            f"+{relative_improvement}% "
            f"({baseline_rate}% → {improved_rate}%)"
        )
