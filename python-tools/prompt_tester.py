"""
prompt_tester.py

Run a prompt set against a list of variants and collect responses.

Usage:
    python3 prompt_tester.py

For live API calls, set the OPENAI_API_KEY environment variable. Without it,
the script runs in demo mode and returns simulated responses for illustration.

See evaluations/framework.md for the scoring methodology used with these results.
"""

import os
import json
import time
from typing import Optional


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

class PromptSet:
    """A named group of semantically equivalent prompt variants."""

    def __init__(self, name: str, variants: list[str], expected_answer: str = ""):
        self.name = name
        self.variants = variants
        self.expected_answer = expected_answer

    def __repr__(self) -> str:
        return f"PromptSet(name={self.name!r}, variants={len(self.variants)})"


class Response:
    """A single model response to a prompt variant."""

    def __init__(self, prompt_set_name: str, variant_index: int, prompt: str, text: str):
        self.prompt_set_name = prompt_set_name
        self.variant_index = variant_index
        self.prompt = prompt
        self.text = text

    def __repr__(self) -> str:
        return (
            f"Response(set={self.prompt_set_name!r}, "
            f"variant={self.variant_index}, "
            f"text={self.text[:60]!r}...)"
        )


# ---------------------------------------------------------------------------
# LLM client (demo mode when no API key is set)
# ---------------------------------------------------------------------------

def call_model(prompt: str, model: str = "gpt-4o", temperature: float = 0.3) -> str:
    """
    Call an OpenAI-compatible model with the given prompt.

    Falls back to demo mode if OPENAI_API_KEY is not set.
    """
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        return _demo_response(prompt)

    try:
        import openai
        client = openai.OpenAI(api_key=api_key)
        completion = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
        )
        return completion.choices[0].message.content.strip()
    except Exception as exc:
        raise RuntimeError(f"API call failed: {exc}") from exc


def _demo_response(prompt: str) -> str:
    """
    Return a simulated response for demo mode.

    In a real evaluation pipeline, this would be replaced by an actual model call.
    The simulated responses demonstrate what a well-formed and a poorly-formed
    response look like for the same prompt.
    """
    if "boiling point" in prompt.lower():
        return "Water boils at 100°C (212°F) at standard atmospheric pressure (1 atm / 101.325 kPa)."
    if "gradient descent" in prompt.lower() and "three sentences" in prompt.lower():
        return (
            "Gradient descent is an optimization algorithm that iteratively adjusts "
            "model parameters to minimize a measure of how wrong the model's predictions are. "
            "At each step, it calculates the direction of steepest improvement and moves "
            "the parameters a small amount in that direction. "
            "Repeating this process eventually brings the model to a configuration where "
            "its predictions are as accurate as the training data allows."
        )
    if "bat and ball" in prompt.lower() or "notebook and pen" in prompt.lower():
        return (
            "Let the cost of the smaller item be x.\n"
            "Then the larger item costs x + (the difference given).\n"
            "Together they equal the total: x + (x + difference) = total\n"
            "Solving: 2x = total - difference, so x = (total - difference) / 2.\n"
            "Applying the numbers gives the correct answer."
        )
    return f"[Demo response for: {prompt[:80]}...]"


# ---------------------------------------------------------------------------
# Prompt runner
# ---------------------------------------------------------------------------

def run_prompt_set(
    prompt_set: PromptSet,
    model: str = "gpt-4o",
    temperature: float = 0.3,
    delay_seconds: float = 0.5,
) -> list[Response]:
    """
    Run all variants in a prompt set and return collected responses.

    Args:
        prompt_set: The PromptSet to run.
        model: Model identifier to pass to the API.
        temperature: Sampling temperature.
        delay_seconds: Seconds to wait between API calls to avoid rate limiting.

    Returns:
        A list of Response objects, one per variant.
    """
    responses = []
    for i, variant in enumerate(prompt_set.variants):
        text = call_model(variant, model=model, temperature=temperature)
        responses.append(Response(
            prompt_set_name=prompt_set.name,
            variant_index=i,
            prompt=variant,
            text=text,
        ))
        if i < len(prompt_set.variants) - 1:
            time.sleep(delay_seconds)
    return responses


def run_all_prompt_sets(
    prompt_sets: list[PromptSet],
    model: str = "gpt-4o",
    temperature: float = 0.3,
) -> dict[str, list[Response]]:
    """
    Run all prompt sets and return a dict mapping set name to responses.
    """
    results: dict[str, list[Response]] = {}
    for ps in prompt_sets:
        print(f"Running: {ps.name}")
        results[ps.name] = run_prompt_set(ps, model=model, temperature=temperature)
    return results


# ---------------------------------------------------------------------------
# Demo prompt sets
# ---------------------------------------------------------------------------

DEMO_PROMPT_SETS = [
    PromptSet(
        name="water_boiling_point",
        variants=[
            "What is the boiling point of water at sea level?",
            "At standard atmospheric pressure, at what temperature does water boil?",
        ],
        expected_answer="100°C / 212°F at 1 atm",
    ),
    PromptSet(
        name="gradient_descent_explanation",
        variants=[
            (
                "Explain gradient descent in three sentences. "
                "Do not use mathematical notation. "
                "Target audience: a non-technical product manager."
            ),
            (
                "In exactly three sentences, describe how gradient descent works. "
                "Avoid equations or notation. "
                "Assume your reader has no machine learning background."
            ),
        ],
        expected_answer=(
            "An iterative optimization algorithm that adjusts model parameters "
            "to minimize prediction error by following the direction of steepest improvement."
        ),
    ),
    PromptSet(
        name="crt_arithmetic",
        variants=[
            (
                "A bat and a ball cost $1.10 in total. "
                "The bat costs $1.00 more than the ball. "
                "How much does the ball cost? Show your working."
            ),
            (
                "A notebook and pen cost $2.20 in total. "
                "The notebook costs $2.00 more than the pen. "
                "How much does the pen cost? Show each step."
            ),
        ],
        expected_answer="$0.05 / $0.10 respectively",
    ),
]


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def print_results(results: dict[str, list[Response]]) -> None:
    """Print collected responses in a readable format."""
    for set_name, responses in results.items():
        print(f"\n{'=' * 60}")
        print(f"Prompt Set: {set_name}")
        print("=" * 60)
        for resp in responses:
            print(f"\n  Variant {resp.variant_index + 1}:")
            print(f"  Prompt:   {resp.prompt[:100]}...")
            print(f"  Response: {resp.text[:200]}...")

    print()


def save_results_json(results: dict[str, list[Response]], path: str) -> None:
    """Save collected responses to a JSON file."""
    serializable = {
        set_name: [
            {
                "variant_index": r.variant_index,
                "prompt": r.prompt,
                "response": r.text,
            }
            for r in responses
        ]
        for set_name, responses in results.items()
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2)
    print(f"Results saved to {path}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Running demo prompt sets (no API key required).\n")
    print("Set OPENAI_API_KEY to run against a live model.\n")

    results = run_all_prompt_sets(DEMO_PROMPT_SETS)
    print_results(results)
