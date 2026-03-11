# Evaluation Framework

This document describes the methodology used to score and compare prompt responses in this repository.

For metric definitions, see [metrics.md](metrics.md).

---

## Scoring Rubric

Each prompt response is scored **0–3** per applicable dimension:

| Score | Meaning |
|---|---|
| 0 | Fails to meet the criterion |
| 1 | Partially meets the criterion |
| 2 | Mostly meets the criterion |
| 3 | Fully meets the criterion |

---

## Dimensions

### 1. Accuracy (AC)
- Is the core answer factually correct?
- Are supporting details accurate and verifiable against a reliable knowledge source?

### 2. Reasoning Quality (RQ)
- Is the reasoning chain logically coherent?
- Are intermediate steps correct and clearly presented?
- Does the model reach the correct conclusion through valid reasoning?

### 3. Instruction Following (IF)
- Are all explicit constraints respected (format, length, tone, audience, role)?
- Does the response address all parts of the prompt?
- Are prohibited elements absent from the output?

### 4. Hallucination Rate (HR)
- Does the response contain unsupported or fabricated claims?
- Can all factual assertions be verified against a reliable knowledge source?
- Scored 3 (no hallucinations) down to 0 (substantially hallucinated).

### 5. Clarity (CL)
- Is the response well-structured and easy to follow?
- Is the language clear and appropriate for the intended audience?
- Is the response concise without omitting essential information?

---

## Aggregate Score

```
Aggregate = sum(applicable_scores) / (applicable_dimensions × 3) × 100%
```

When all five dimensions apply, the denominator is 15. For prompts where only a subset apply, divide by `applicable_dimensions × 3`.

---

## Consistency Measurement

Each prompt set contains multiple variants (A, B, C) — semantically equivalent rephrasings of the same question. Response consistency measures whether model output quality is stable across phrasing variation.

**Procedure:**
1. Run each variant independently against the model.
2. Score each response on all applicable dimensions.
3. Compute the variance in aggregate scores across variants.
4. A prompt set is **consistent** when score variance ≤ 0.5 across all variants.

**What was improved:**  
The +35% consistency gain was achieved by iteratively refining prompts to reduce ambiguity, add grounding context, and specify explicit output constraints — isolating phrasing variation from knowledge-gap variation.

---

## Results Summary

| Domain | Prompts Evaluated | Avg Consistency | Avg Accuracy |
|---|---|---|---|
| Technical | ~200 | 68% | 74% |
| Educational | ~150 | 71% | 80% |
| General Knowledge | ~150 | 72% | 76% |
| **Total** | **~500+** | **~70%** | **~76%** |

Baseline consistency (before prompt refinement): ~52%  
Improved consistency (after prompt refinement): ~70%  
Relative improvement: **+35%**

Per-prompt scores are stored in [`results/`](results/).
