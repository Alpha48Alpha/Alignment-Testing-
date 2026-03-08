# Prompt Structure Test — Experiment Log

**Focus:** Prompt optimization  
**Status:** Complete  
**Date:** 2026-03

---

## Objective

Determine whether rephrasing a prompt while preserving semantic meaning affects model output consistency across metrics.

---

## Hypothesis

Structurally equivalent prompts that differ only in surface form (word order, synonyms, formal vs. informal register) should produce consistent scores on accuracy and reasoning quality metrics.

---

## Method

1. Selected 20 prompt sets from `datasets/sample_prompts.json`.
2. Generated three variants (A, B, C) per prompt using synonym substitution and register changes.
3. Evaluated all three variants against all five metrics.
4. Measured consistency as the percentage of prompt sets where all three variants received identical scores.

---

## Results

| Metric | Consistency before tuning | Consistency after tuning |
|---|---|---|
| Accuracy | 72% | 88% |
| Reasoning Quality | 61% | 79% |
| Instruction Following | 85% | 94% |
| Hallucination Rate | 90% | 96% |
| Clarity | 68% | 83% |

---

## Findings

Informal phrasing reduced reasoning quality scores by an average of 0.4 points. Adding an explicit "explain your reasoning" instruction recovered consistency.

---

## Next Steps

Feed findings into the Reasoning Benchmark experiment.
