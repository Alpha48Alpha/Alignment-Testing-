"""
evaluation_pipeline_example.py
--------------------------------
End-to-end demonstration of a prompt evaluation workflow.

Pipeline stages:
  1. Load prompts          – read prompt definitions (hard-coded samples here)
  2. Generate responses    – call the model (mock responses used here)
  3. Score responses       – apply the scoring framework from
                             prompt_testing_framework.py
  4. Save results          – write a JSON results file to
                             ../evaluations/results/

Run this script directly to see the pipeline in action:

    python3 evaluation_pipeline_example.py

No external dependencies are required.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone

from prompt_testing_framework import Prompt, aggregate_score, score_response


# ---------------------------------------------------------------------------
# Stage 1 – Load prompts
# ---------------------------------------------------------------------------

def load_sample_prompts() -> list[Prompt]:
    """Return a small set of representative prompts for demonstration.

    In a real pipeline, this function would read from the ``prompts/``
    directory or a database.  The samples here mirror the domains and
    metric subsets used in evaluations/metrics.md.
    """
    return [
        Prompt(
            id="tech-001-A",
            domain="technical",
            text=(
                "Explain what a hash collision is in the context of hash tables, "
                "and describe one common strategy to resolve it."
            ),
            expected_answer=(
                "A hash collision occurs when two keys map to the same bucket. "
                "Common resolution strategies include chaining (linked lists per "
                "bucket) and open addressing (probing for the next free slot)."
            ),
            applicable_metrics=[
                "accuracy",
                "reasoning_quality",
                "clarity",
            ],
        ),
        Prompt(
            id="edu-001-A",
            domain="educational",
            text=(
                "In three sentences or fewer, explain Newton's second law of motion "
                "to a high-school student."
            ),
            expected_answer=(
                "Force equals mass times acceleration (F = ma). "
                "A heavier object needs more force to achieve the same acceleration. "
                "The law explains why pushing a car is harder than pushing a bicycle."
            ),
            applicable_metrics=[
                "accuracy",
                "instruction_following",
                "clarity",
            ],
        ),
        Prompt(
            id="gen-001-A",
            domain="general",
            text="What is the capital of France, and what river runs through it?",
            expected_answer="Paris is the capital of France. The Seine river runs through it.",
            applicable_metrics=[
                "accuracy",
                "hallucination_rate",
                "clarity",
            ],
        ),
    ]


# ---------------------------------------------------------------------------
# Stage 2 – Generate responses (mock)
# ---------------------------------------------------------------------------

def generate_mock_response(prompt: Prompt) -> str:
    """Return a canned response for the given prompt.

    Replace this function with a real API call (e.g. OpenAI, Anthropic,
    or a local model) to evaluate actual model outputs.
    """
    mock_responses: dict[str, str] = {
        "tech-001-A": (
            "A hash collision happens when two different keys produce the same "
            "hash value and therefore target the same bucket in a hash table. "
            "One common resolution strategy is *separate chaining*: each bucket "
            "holds a linked list of all key-value pairs that hash to that slot, "
            "so collisions are handled by appending to the list."
        ),
        "edu-001-A": (
            "Newton's second law states that the net force acting on an object "
            "equals its mass multiplied by its acceleration (F = ma). "
            "This means that a heavier object requires more force to speed up at "
            "the same rate as a lighter one."
        ),
        "gen-001-A": (
            "The capital of France is Paris. "
            "The Seine river flows through the heart of the city."
        ),
    }
    # Fall back to the expected answer if no mock is registered
    return mock_responses.get(prompt.id, prompt.expected_answer)


# ---------------------------------------------------------------------------
# Stage 3 – Score responses
# ---------------------------------------------------------------------------

def run_scoring(
    prompts: list[Prompt],
    responses: dict[str, str],
) -> list[dict]:
    """Score each response and return a list of result records.

    Each record contains:
      - prompt_id, domain, prompt_text, response
      - per-dimension scores
      - aggregate_pct: overall quality percentage
    """
    results = []

    for prompt in prompts:
        response = responses.get(prompt.id, "")
        dim_scores = score_response(prompt, response)
        agg = aggregate_score(dim_scores)

        results.append(
            {
                "prompt_id": prompt.id,
                "domain": prompt.domain,
                "prompt_text": prompt.text,
                "response": response,
                "scores": dim_scores,
                "aggregate_pct": agg,
            }
        )

    return results


# ---------------------------------------------------------------------------
# Stage 4 – Save results
# ---------------------------------------------------------------------------

def save_results(results: list[dict], output_path: str) -> None:
    """Persist *results* as a JSON file at *output_path*.

    The file includes a timestamp so successive runs do not overwrite
    earlier results if callers use a timestamped filename.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_prompts": len(results),
        "results": results,
    }

    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)

    print(f"Results saved to: {output_path}")


# ---------------------------------------------------------------------------
# Pipeline entry point
# ---------------------------------------------------------------------------

def run_pipeline(output_path: str | None = None) -> list[dict]:
    """Execute all four pipeline stages and return the scored results.

    Parameters
    ----------
    output_path:
        Where to write the JSON results file.  Defaults to
        ``../evaluations/results/pipeline_example_<timestamp>.json``
        relative to this script's location.
    """
    # Stage 1 – Load
    prompts = load_sample_prompts()
    print(f"Loaded {len(prompts)} prompts.")

    # Stage 2 – Generate
    responses: dict[str, str] = {
        p.id: generate_mock_response(p) for p in prompts
    }
    print(f"Generated {len(responses)} responses (mock).")

    # Stage 3 – Score
    results = run_scoring(prompts, responses)

    # Print a brief summary to stdout
    print("\n--- Scoring summary ---")
    for r in results:
        scores_str = ", ".join(f"{k}={v}" for k, v in r["scores"].items())
        print(f"  {r['prompt_id']:12s}  aggregate={r['aggregate_pct']:5.1f}%  [{scores_str}]")

    # Stage 4 – Save
    if output_path is None:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        results_dir = os.path.join(script_dir, "..", "evaluations", "results")
        output_path = os.path.join(results_dir, f"pipeline_example_{timestamp}.json")

    save_results(results, output_path)
    return results


# ---------------------------------------------------------------------------
# Script entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run_pipeline()
