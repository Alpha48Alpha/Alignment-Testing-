# Evaluation Framework

This document describes the methodology used to evaluate prompts in this repository.

---

## Scoring Rubric

Each prompt response is scored on a scale of **0–3** for each applicable dimension:

| Score | Meaning |
|---|---|
| 0 | Fails to meet the criterion |
| 1 | Partially meets the criterion |
| 2 | Mostly meets the criterion |
| 3 | Fully meets the criterion |

---

## Dimensions

### 1. Reasoning Consistency (RC)
- Does the model produce the same correct answer across equivalent rephrasings?
- Is the reasoning chain logically coherent?
- Are intermediate steps correct when shown?

### 2. Instruction Following (IF)
- Are all explicit constraints respected (format, length, role, steps)?
- Does the response address all parts of the prompt?
- Are prohibited elements absent from the output?

### 3. Factual Accuracy (FA)
- Is the core answer factually correct?
- Are supporting details accurate?
- Is the response free from hallucinated or fabricated content?

### 4. Output Clarity (OC)
- Is the response well-structured?
- Is the language clear and appropriate for the intended audience?
- Is the response concise without omitting essential information?

---

## Aggregate Score

The aggregate score for a prompt set is computed as:

```
Aggregate = (RC + IF + FA + OC) / (number_of_applicable_dimensions * 3) * 100%
```

---

## Consistency Measurement

Response consistency is measured by running each prompt variant independently and comparing outputs:

1. Run all variants of a prompt set against the model.
2. Score each variant response on applicable dimensions.
3. Compute the variance in scores across variants.
4. A **consistent** prompt set has a score variance ≤ 0.5 across all variants.

The **35% improvement in response consistency** was achieved by iteratively refining prompts to reduce ambiguity, add grounding context, and specify explicit output constraints.

---

## Results Summary

| Domain | Prompts Evaluated | Average Consistency Score | Average Accuracy Score |
|---|---|---|---|
| Technical | ~200 | 68% | 74% |
| Educational | ~150 | 71% | 80% |
| General Knowledge | ~150 | 72% | 76% |
| **Total** | **~500+** | **~70%** | **~76%** |

Baseline consistency (before prompt refinement): ~52%  
Improved consistency (after prompt refinement): ~70%  
Relative improvement: **+35%**

Detailed per-prompt scores are stored in `evaluations/results/`.
