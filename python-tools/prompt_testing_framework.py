"""
prompt_testing_framework.py
----------------------------
Core building blocks for prompt testing and evaluation.

This module defines:
  - Prompt          : a lightweight container for a prompt and its metadata
  - score_response  : scores a single response across up to five dimensions
  - aggregate_score : computes the overall percentage score for a result dict

Scoring dimensions (0–3 each, aligned with evaluations/metrics.md):
  accuracy            – factual correctness
  reasoning_quality   – logical coherence of the explanation
  instruction_following – adherence to explicit constraints
  hallucination_rate  – absence of unsupported claims (3 = none, 0 = many)
  clarity             – readability and structure
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Prompt:
    """Represents a single evaluation prompt with its metadata."""

    id: str                          # Unique identifier, e.g. "tech-001-A"
    domain: str                      # e.g. "technical", "educational", "general"
    text: str                        # The prompt text sent to the model
    expected_answer: str             # Reference answer used by scorers
    applicable_metrics: list[str] = field(
        default_factory=lambda: [
            "accuracy",
            "reasoning_quality",
            "instruction_following",
            "hallucination_rate",
            "clarity",
        ]
    )


# ---------------------------------------------------------------------------
# Scoring helpers
# ---------------------------------------------------------------------------

# All valid scoring dimensions and their valid range
VALID_DIMENSIONS = {
    "accuracy",
    "reasoning_quality",
    "instruction_following",
    "hallucination_rate",
    "clarity",
}

SCORE_MIN = 0
SCORE_MAX = 3


def score_response(
    prompt: Prompt,
    response: str,
    scorer_fn=None,
) -> dict[str, int]:
    """Score *response* against *prompt* on each applicable metric.

    Parameters
    ----------
    prompt:
        The :class:`Prompt` being evaluated.
    response:
        The model-generated (or mock) response text.
    scorer_fn:
        Optional callable with signature
        ``(dimension: str, prompt: Prompt, response: str) -> int``.
        Receives each applicable dimension and must return an integer 0–3.
        When *None*, a placeholder scorer that returns 2 for every
        dimension is used — useful for skeleton pipelines before a real
        scorer is wired in.

    Returns
    -------
    dict mapping each applicable metric name to its 0–3 score.
    """
    if scorer_fn is None:
        scorer_fn = _placeholder_scorer

    scores: dict[str, int] = {}
    for dimension in prompt.applicable_metrics:
        if dimension not in VALID_DIMENSIONS:
            raise ValueError(
                f"Unknown metric '{dimension}'. "
                f"Valid options: {sorted(VALID_DIMENSIONS)}"
            )
        raw = scorer_fn(dimension, prompt, response)
        scores[dimension] = max(SCORE_MIN, min(SCORE_MAX, int(raw)))

    return scores


def aggregate_score(scores: dict[str, int]) -> float:
    """Return the aggregate score as a percentage (0–100).

    Formula (from evaluations/metrics.md):
        Aggregate = sum(scores) / (n_applicable * 3) * 100
    """
    if not scores:
        return 0.0
    total = sum(scores.values())
    max_possible = len(scores) * SCORE_MAX
    return round(total / max_possible * 100, 1)


# ---------------------------------------------------------------------------
# Placeholder scorer
# ---------------------------------------------------------------------------

def _placeholder_scorer(dimension: str, prompt: Prompt, response: str) -> int:
    """Placeholder scorer — returns a neutral mid-range score of 2.

    Replace this with a real scoring function (rule-based, model-based,
    or human annotation) in a production pipeline.
    """
    # Suppress unused-variable warnings; real scorers would inspect these.
    _ = dimension, prompt, response
    return 2
