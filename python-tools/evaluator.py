"""
evaluator.py

Score model responses on the five evaluation dimensions defined in evaluations/metrics.md:
  - Accuracy (AC)
  - Reasoning Quality (RQ)
  - Instruction Following (IF)
  - Hallucination Rate (HR)
  - Clarity (CL)

Each dimension is scored 0–3. Not all dimensions apply to every task.
Use None to indicate a dimension is not applicable.

Usage:
    python3 evaluator.py

This script demonstrates the evaluation workflow using example responses.
In a real evaluation pipeline, scores would be assigned by human evaluators
or by a separate LLM acting as a judge (with appropriate calibration).
"""

from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Score data structure
# ---------------------------------------------------------------------------

@dataclass
class Score:
    """
    Scores for a single response on the five evaluation dimensions.

    Use None for dimensions that do not apply to the task.
    All applicable scores must be in the range [0, 3].
    """
    accuracy: Optional[int] = None
    reasoning_quality: Optional[int] = None
    instruction_following: Optional[int] = None
    hallucination_rate: Optional[int] = None
    clarity: Optional[int] = None
    notes: str = ""

    def validate(self) -> None:
        """Raise ValueError if any assigned score is outside [0, 3]."""
        for name, value in self._applicable_scores():
            if not (0 <= value <= 3):
                raise ValueError(
                    f"Score for '{name}' must be in [0, 3], got {value}"
                )

    def _applicable_scores(self) -> list[tuple[str, int]]:
        pairs = [
            ("accuracy", self.accuracy),
            ("reasoning_quality", self.reasoning_quality),
            ("instruction_following", self.instruction_following),
            ("hallucination_rate", self.hallucination_rate),
            ("clarity", self.clarity),
        ]
        return [(name, val) for name, val in pairs if val is not None]

    def aggregate(self) -> Optional[float]:
        """
        Compute the aggregate score as a percentage.

        Returns None if no dimensions are applicable.
        Formula: sum(applicable_scores) / (num_applicable * 3) * 100
        """
        applicable = self._applicable_scores()
        if not applicable:
            return None
        total = sum(val for _, val in applicable)
        max_possible = len(applicable) * 3
        return round(total / max_possible * 100, 1)

    def __str__(self) -> str:
        parts = []
        labels = {
            "accuracy": "AC",
            "reasoning_quality": "RQ",
            "instruction_following": "IF",
            "hallucination_rate": "HR",
            "clarity": "CL",
        }
        for attr, abbrev in labels.items():
            val = getattr(self, attr)
            parts.append(f"{abbrev}={val if val is not None else 'N/A'}")
        agg = self.aggregate()
        agg_str = f"{agg}%" if agg is not None else "N/A"
        return f"[{', '.join(parts)}, Aggregate={agg_str}]"


# ---------------------------------------------------------------------------
# Evaluated response
# ---------------------------------------------------------------------------

@dataclass
class EvaluatedResponse:
    """A response paired with its evaluation scores."""
    prompt_set_name: str
    variant_index: int
    prompt: str
    response: str
    score: Score
    evaluator_notes: str = ""


# ---------------------------------------------------------------------------
# Consistency computation
# ---------------------------------------------------------------------------

def compute_consistency(evaluated_responses: list[EvaluatedResponse]) -> dict:
    """
    Compute consistency across variants in the same prompt set.

    Returns a dict with:
      - 'consistent': bool (True if aggregate score difference <= 0.5 points)
      - 'aggregates': list of aggregate scores per variant
      - 'max_difference': maximum absolute difference in aggregate scores
    """
    aggregates = []
    for er in evaluated_responses:
        agg = er.score.aggregate()
        if agg is not None:
            aggregates.append(agg)

    if len(aggregates) < 2:
        return {"consistent": True, "aggregates": aggregates, "max_difference": 0.0}

    # Convert from percentages to 0-3 scale for threshold comparison
    agg_on_scale = [a / 100 * 3 for a in aggregates]
    max_diff = max(agg_on_scale) - min(agg_on_scale)

    return {
        "consistent": max_diff <= 0.5,
        "aggregates": aggregates,
        "max_difference": round(max_diff, 3),
    }


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_evaluation_report(
    results: dict[str, list[EvaluatedResponse]]
) -> None:
    """Print a formatted evaluation report."""
    total_sets = len(results)
    consistent_sets = 0
    all_aggregates: list[float] = []

    print("\n" + "=" * 70)
    print("EVALUATION REPORT")
    print("=" * 70)

    for set_name, responses in results.items():
        print(f"\nPrompt Set: {set_name}")
        print("-" * 50)

        for er in responses:
            print(f"  Variant {er.variant_index + 1}: {er.score}")
            if er.evaluator_notes:
                print(f"    Notes: {er.evaluator_notes}")
            agg = er.score.aggregate()
            if agg is not None:
                all_aggregates.append(agg)

        consistency = compute_consistency(responses)
        status = "CONSISTENT" if consistency["consistent"] else "INCONSISTENT"
        print(
            f"\n  Consistency: {status} "
            f"(aggregates: {consistency['aggregates']}, "
            f"max diff on 0-3 scale: {consistency['max_difference']})"
        )
        if consistency["consistent"]:
            consistent_sets += 1

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    if all_aggregates:
        avg_aggregate = round(sum(all_aggregates) / len(all_aggregates), 1)
        print(f"Average aggregate score: {avg_aggregate}%")
    consistency_rate = round(consistent_sets / total_sets * 100, 1) if total_sets > 0 else 0.0
    print(f"Prompt sets evaluated:   {total_sets}")
    print(f"Consistent sets:         {consistent_sets} / {total_sets} ({consistency_rate}%)")
    print()


# ---------------------------------------------------------------------------
# Example evaluation data
# ---------------------------------------------------------------------------

EXAMPLE_EVALUATIONS: dict[str, list[EvaluatedResponse]] = {
    "water_boiling_point": [
        EvaluatedResponse(
            prompt_set_name="water_boiling_point",
            variant_index=0,
            prompt="What is the boiling point of water at sea level?",
            response="Water boils at 100°C (212°F) at standard atmospheric pressure.",
            score=Score(
                accuracy=3,
                reasoning_quality=None,
                instruction_following=3,
                hallucination_rate=3,
                clarity=3,
            ),
            evaluator_notes="Correct answer, appropriate precision, concise.",
        ),
        EvaluatedResponse(
            prompt_set_name="water_boiling_point",
            variant_index=1,
            prompt="At standard atmospheric pressure, at what temperature does water boil?",
            response="At standard atmospheric pressure, water boils at 100°C or 212°F.",
            score=Score(
                accuracy=3,
                reasoning_quality=None,
                instruction_following=3,
                hallucination_rate=3,
                clarity=3,
            ),
            evaluator_notes="Equivalent correct answer.",
        ),
    ],
    "gradient_descent_explanation": [
        EvaluatedResponse(
            prompt_set_name="gradient_descent_explanation",
            variant_index=0,
            prompt=(
                "Explain gradient descent in three sentences. "
                "Do not use mathematical notation. "
                "Target audience: a non-technical product manager."
            ),
            response=(
                "Gradient descent is an optimization algorithm that adjusts model parameters "
                "to minimize a loss function by computing the gradient ∂L/∂w and moving in "
                "the direction of steepest descent. "
                "It is used in training neural networks and other machine learning models. "
                "The learning rate controls the size of each update step."
            ),
            score=Score(
                accuracy=3,
                reasoning_quality=None,
                instruction_following=1,
                hallucination_rate=3,
                clarity=2,
            ),
            evaluator_notes=(
                "IF=1: prompt required no mathematical notation, but response included ∂L/∂w. "
                "Three sentences, audience partially matched but 'loss function' and 'gradient' "
                "are technical terms not explained for a non-technical reader."
            ),
        ),
        EvaluatedResponse(
            prompt_set_name="gradient_descent_explanation",
            variant_index=1,
            prompt=(
                "In exactly three sentences, describe how gradient descent works. "
                "Avoid equations or notation. "
                "Assume your reader has no machine learning background."
            ),
            response=(
                "Gradient descent is the process by which a machine learning model learns "
                "from its mistakes by measuring how wrong its predictions are and nudging "
                "its settings in the direction that reduces that wrongness. "
                "Think of it like adjusting a recipe based on feedback: if your dish is too "
                "salty, you use a little less salt next time. "
                "Repeating this adjustment process thousands of times gradually tunes the "
                "model to make better predictions."
            ),
            score=Score(
                accuracy=3,
                reasoning_quality=None,
                instruction_following=3,
                hallucination_rate=3,
                clarity=3,
            ),
            evaluator_notes=(
                "IF=3: three sentences, no notation, accessible analogy for non-technical audience. "
                "This variant was more compliant likely due to constraint restatement at end."
            ),
        ),
    ],
    "crt_arithmetic": [
        EvaluatedResponse(
            prompt_set_name="crt_arithmetic",
            variant_index=0,
            prompt=(
                "A bat and a ball cost $1.10 in total. "
                "The bat costs $1.00 more than the ball. "
                "How much does the ball cost? Show your working."
            ),
            response=(
                "The ball costs 10 cents."
            ),
            score=Score(
                accuracy=0,
                reasoning_quality=0,
                instruction_following=1,
                hallucination_rate=3,
                clarity=3,
            ),
            evaluator_notes=(
                "AC=0: Incorrect. Correct answer is 5 cents. "
                "RQ=0: No working shown, and the intuitive answer is wrong. "
                "IF=1: 'Show your working' constraint not followed."
            ),
        ),
        EvaluatedResponse(
            prompt_set_name="crt_arithmetic",
            variant_index=1,
            prompt=(
                "A notebook and pen cost $2.20 in total. "
                "The notebook costs $2.00 more than the pen. "
                "How much does the pen cost? Show each step."
            ),
            response=(
                "Let the pen cost x.\n"
                "Then the notebook costs x + 2.00.\n"
                "Together: x + (x + 2.00) = 2.20\n"
                "2x + 2.00 = 2.20\n"
                "2x = 0.20\n"
                "x = 0.10\n\n"
                "The pen costs $0.10."
            ),
            score=Score(
                accuracy=3,
                reasoning_quality=3,
                instruction_following=3,
                hallucination_rate=3,
                clarity=3,
            ),
            evaluator_notes=(
                "Correct answer ($0.10 for this variant). "
                "All steps shown. Consistent with the modified CRT structure."
            ),
        ),
    ],
}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Running evaluation on example responses...\n")
    print("(In a real evaluation pipeline, scores are assigned by human evaluators")
    print(" or a calibrated LLM judge, not hard-coded here.)\n")
    print_evaluation_report(EXAMPLE_EVALUATIONS)
