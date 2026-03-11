# Evaluation Framework

This document describes the methodology used to score prompt responses and measure consistency across variants.

For per-metric scoring rubrics, see [metrics.md](metrics.md).

---

## Scoring Rubric

Each response is scored on a **0–3 integer scale** for every applicable dimension:

| Score | Meaning |
|---|---|
| 0 | Fails to meet the criterion |
| 1 | Partially meets the criterion |
| 2 | Mostly meets the criterion |
| 3 | Fully meets the criterion |

---

## Evaluation Dimensions

### 1. Accuracy (AC)
- Is the core answer factually correct?
- Are supporting details verifiable against a reliable knowledge source?

### 2. Reasoning Quality (RQ)
- Is the reasoning chain logically coherent from premise to conclusion?
- Are intermediate steps correct and clearly presented?
- Does the model avoid reasoning shortcuts that produce the right answer for wrong reasons?

### 3. Instruction Following (IF)
- Are all explicit constraints respected (format, length, tone, audience, role)?
- Does the response address every part of the prompt?
- Are prohibited elements (e.g., unsolicited caveats, off-topic content) absent from the output?

### 4. Hallucination Rate (HR)
- Does the response contain unsupported or fabricated claims?
- Can every factual assertion be verified against a reliable source?
- Scored 3 (no hallucinations) down to 0 (substantially hallucinated); see metrics.md for the full lookup table.

### 5. Clarity (CL)
- Is the response well-structured and easy to follow?
- Is the language appropriate for the stated audience?
- Is the response concise without omitting essential information?

---

## Aggregate Score

```
Aggregate = (AC + RQ + IF + HR + CL) / (number_of_applicable_dimensions × 3) × 100%
```

When all five dimensions apply, the denominator is 15.

---

## Consistency Measurement

Each prompt set contains 2–3 rephrasings of the same underlying question (Variant A, B, C). Consistency measures how often all variants in a set receive identical scores.

**Procedure:**
1. Run each variant independently against the model.
2. Score each response on applicable dimensions.
3. Compute the variance in scores across variants within the set.
4. A prompt set is **consistent** when score variance ≤ 0.5 across all variants.

**Improvement achieved:** Baseline consistency was ~52% of prompt sets; after iterative refinement (reducing ambiguous wording, adding grounding context, specifying explicit output constraints), consistency reached ~70% — a **+35% relative improvement**.

---

## Results Summary

| Domain | Prompts Evaluated | Avg Consistency Score | Avg Accuracy Score |
|---|---|---|---|
| Technical | ~200 | 68% | 74% |
| Educational | ~150 | 71% | 80% |
| General Knowledge | ~150 | 72% | 76% |
| **Total** | **~500+** | **~70%** | **~76%** |

Detailed per-prompt scores are stored in `evaluations/results/`.
