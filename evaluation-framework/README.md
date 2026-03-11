# Evaluation Framework

This document is the primary reference for how model responses are evaluated in this repository.

For per-metric definitions and scoring guidance, see [`../evaluations/metrics.md`](../evaluations/metrics.md).
For benchmark design methodology, see [`../llm-benchmark-design/README.md`](../llm-benchmark-design/README.md).

---

## Scoring Scale

All metrics are scored on a 0–3 integer scale:

| Score | Meaning |
|---|---|
| 0 | Fails to meet the criterion |
| 1 | Partially meets the criterion with notable deficiencies |
| 2 | Mostly meets the criterion with minor deficiencies |
| 3 | Fully meets the criterion |

Fractional scores are not used. When a response sits between two score levels, choose the lower score and document the reasoning.

---

## Five Evaluation Dimensions

### Accuracy (AC)

Is the core answer factually correct? Are supporting details accurate and well-supported?

Apply when: The prompt has a verifiable ground-truth answer.

Common failure: Partial accuracy — the model reaches the right conclusion through a chain of reasoning that contains a factual error midway through. Score based on the overall factual quality of the response, not only the final answer.

---

### Reasoning Quality (RQ)

Is the reasoning chain logically coherent? Do intermediate steps support the conclusion?

Apply when: The prompt requires multi-step derivation, deduction, or analysis.

Common failure: The correct answer is stated without a derivation, or with a derivation that contains a logical gap. A correct answer reached through flawed reasoning scores 2/3 at most.

Scoring note: Do not apply this metric to simple factual recall tasks. A question like "What is the capital of France?" does not require visible reasoning.

---

### Instruction Following (IF)

Are all explicit constraints respected? Does the response address all parts of the prompt?

Apply when: The prompt specifies constraints on format, length, tone, audience, or scope.

Common failure: Instruction drift — early constraints are followed but later constraints are dropped. Score per constraint and average.

Decomposition approach: List each explicit constraint in the prompt. Score each constraint 0 (violated), 1 (partially followed), or 2 (fully followed). The IF score is: `sum / (number_of_constraints × 2) × 3`, rounded to nearest integer.

---

### Hallucination Rate (HR)

Does the response contain unsupported or fabricated claims?

Apply when: The response makes factual assertions that can be verified against reliable sources.

Scoring note: Score 3 when no unsupported claims are present; score 0 when the response is substantially fabricated. See [`../evaluations/metrics.md`](../evaluations/metrics.md) for the full frequency-to-score mapping.

Verification process:
1. Extract all factual claims from the response.
2. Cross-reference each claim against a reliable source (documentation, textbook, verified reference).
3. Flag claims that cannot be verified or are demonstrably false.
4. Assign score based on frequency and severity of flagged claims.

---

### Clarity (CL)

Is the response well-structured, readable, and appropriate for the intended audience?

Apply when: Response quality affects whether the content is usable and understandable.

Common failure: A technically accurate response that is structured as a wall of text without headers, bullet points, or natural language transitions. Also applies when the register is mismatched (overly technical for a non-expert audience, or overly simplified for a technical one).

---

## Aggregate Score

```
Aggregate = sum(applicable_metric_scores) / (number_of_applicable_metrics × 3) × 100%
```

When all five metrics apply: divide by 15.
When a subset applies: divide by (n × 3) where n is the number of applicable metrics.

---

## Consistency Measurement

Consistency measures how stable a model's performance is across semantically equivalent prompt variants.

**Procedure:**
1. Run each variant in a prompt set independently.
2. Score each variant response on applicable metrics.
3. Compute the absolute difference in aggregate scores across variants.
4. A prompt set is **consistent** if the score difference is ≤ 0.5 points (on the 0–3 scale) across all variants.

**Reporting:**
- **Prompt-level consistency rate**: percentage of prompt sets where all variants received the same aggregate score.
- **Score variance**: mean variance in aggregate scores across all prompt sets.

---

## Evaluator Calibration

Before scoring a new prompt set, evaluators should:

1. Read the metric definitions in [`../evaluations/metrics.md`](../evaluations/metrics.md).
2. Score three calibration examples from the examples section below.
3. Compare scores against reference scores. Scores must match within ±1 point per dimension.
4. Discuss any discrepancies before proceeding with independent evaluation.

### Calibration Example 1

**Prompt:** Explain what a pointer is in C programming. Target audience: a first-year computer science student.

**Response to score:** "A pointer is a variable that stores the memory address of another variable. Think of it like a sticky note that tells you which shelf in a library holds the book you want — the sticky note itself isn't the book, it just tells you where to find it. In C, you declare a pointer with an asterisk: `int *p;` means p is a pointer to an integer."

Reference scores: AC=3, RQ=N/A, IF=3 (audience constraint met), HR=3, CL=3.

---

### Calibration Example 2

**Prompt:** In exactly two sentences, explain why the sky appears blue.

**Response to score:** "The sky appears blue because of a phenomenon called Rayleigh scattering, where shorter blue wavelengths of sunlight are scattered more by the atmosphere than longer wavelengths. This scattered blue light reaches your eyes from all directions, making the entire sky appear blue."

Reference scores: AC=3, RQ=N/A, IF=3 (exactly two sentences, constraint met), HR=3, CL=3.

---

### Calibration Example 3

**Prompt:** In exactly two sentences, explain why the sky appears blue.

**Response to score:** "The sky is blue because of how light interacts with particles in the atmosphere, specifically a scattering effect that affects shorter wavelengths more than longer ones, which is why you see blue and not red or yellow when you look at the clear daytime sky, though this changes near the horizon and at sunrise and sunset when the path through the atmosphere is longer and more of the blue light is scattered away leaving the reds and oranges visible."

Reference scores: AC=2 (mostly accurate but sunset explanation slightly imprecise), RQ=N/A, IF=0 (one run-on sentence instead of two), HR=3, CL=1 (single dense sentence impairs readability).

---

## Evaluation Record Format

Each evaluation run should be recorded in `evaluations/results/` with the following fields:

```
Prompt Set ID:
Model:
Date:
Variants run:

Variant A:
  Response: [response text or truncated excerpt]
  AC: [0-3 or N/A]
  RQ: [0-3 or N/A]
  IF: [0-3 or N/A]
  HR: [0-3 or N/A]
  CL: [0-3 or N/A]
  Aggregate: [%]

Variant B:
  [same fields]

Consistency: [Consistent / Inconsistent]
Score difference: [value]
Notes: [any anomalies or notable observations]
```

---

## Related

- [`../evaluations/metrics.md`](../evaluations/metrics.md) — Per-metric definitions and scoring guidance
- [`../llm-benchmark-design/README.md`](../llm-benchmark-design/README.md) — Benchmark design principles
- [`../evaluations/results/README.md`](../evaluations/results/README.md) — Evaluation results
