# LLM Evaluation Metrics

Definitions for the five core metrics used to score model responses in this repository. Each metric is scored **0–3**, where 3 is fully correct and 0 fails the criterion entirely.

---

## Accuracy (AC)

Measures factual correctness. A response scores 3 when every claim is verifiable and well-supported; it scores 0 when it contains significant factual errors.

| Score | Meaning |
|---|---|
| 3 | Fully accurate and well-supported |
| 2 | Mostly correct with minor inaccuracies |
| 1 | Partially correct with notable errors |
| 0 | Contains significant factual errors |

---

## Reasoning Quality (RQ)

Measures logical coherence. Evaluates whether the reasoning chain is clear, complete, and leads to the correct conclusion.

| Score | Meaning |
|---|---|
| 3 | Reasoning is clear, coherent, and logically complete |
| 2 | Mostly sound reasoning with minor gaps |
| 1 | Some reasoning present but with logical gaps or errors |
| 0 | Reasoning absent, incoherent, or leading to a wrong conclusion |

---

## Instruction Following (IF)

Measures adherence to explicit prompt constraints — format, length, tone, audience, and role.

| Score | Meaning |
|---|---|
| 3 | All constraints fully and precisely respected |
| 2 | All constraints mostly followed with minor deviations |
| 1 | Most constraints followed; one is partially violated |
| 0 | One or more explicit constraints are ignored |

---

## Hallucination Rate (HR)

Tracks unsupported or fabricated claims. Higher scores mean fewer hallucinations.

| Score | Meaning |
|---|---|
| 3 | No unsupported claims |
| 2 | One minor unsupported claim |
| 1 | Multiple unsupported claims or one significant one |
| 0 | Response is substantially hallucinated |

**Measurement approach:**
1. Identify all factual claims in the response.
2. Cross-reference each claim against a reliable knowledge source.
3. Flag any claim that cannot be verified or is demonstrably false.
4. Assign a score based on the frequency and severity of flagged claims.

---

## Clarity (CL)

Measures readability, structure, and audience-appropriateness.

| Score | Meaning |
|---|---|
| 3 | Exceptionally clear, well-structured, and audience-appropriate |
| 2 | Mostly clear with minor issues |
| 1 | Somewhat readable with notable clarity issues |
| 0 | Unclear, poorly structured, or inappropriate for the audience |

---

## Aggregate Score

```
Aggregate = sum(applicable_scores) / (applicable_dimensions × 3) × 100%
```

When all five metrics apply, the denominator is 15. For prompts where only a subset apply, divide by `applicable_dimensions × 3`.

---

## Metric Summary

| Metric | Abbreviation | Measures |
|---|---|---|
| Accuracy | AC | Factual correctness |
| Reasoning Quality | RQ | Logical coherence and completeness |
| Instruction Following | IF | Adherence to explicit prompt constraints |
| Hallucination Rate | HR | Frequency of unsupported or fabricated claims |
| Clarity | CL | Readability and audience-appropriateness |
