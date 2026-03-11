# Evaluation Results

This directory contains evaluation results for prompt sets in this repository.

Results are organized by domain. Each results file records per-prompt scores across the five dimensions: Accuracy (AC), Reasoning Quality (RQ), Instruction Following (IF), Hallucination Rate (HR), and Clarity (CL), scored 0–3.

See [../framework.md](../framework.md) for the full evaluation methodology and scoring rubric, and [../metrics.md](../metrics.md) for per-metric definitions.

---

## Summary

| Domain | Prompts Evaluated | Avg Consistency | Avg Accuracy | Avg Aggregate |
|---|---|---|---|---|
| Technical | ~200 | 68% | 74% | 71% |
| Educational | ~150 | 71% | 80% | 76% |
| General Knowledge | ~150 | 72% | 76% | 74% |
| **Total / Overall** | **~500+** | **~70%** | **~76%** | **~73%** |

Baseline consistency (before prompt refinement): ~52%  
Improved consistency (after prompt refinement): ~70%  
Relative improvement: **+35%**

---

## Consistency Definition

A prompt-variant set is **consistent** when all variants (A, B, C rephrasings of the same question) receive the same aggregate score — i.e., the score variance across variants is ≤ 0.5.

Consistency was improved by:
1. Removing ambiguous phrasing that led the model to interpret the question differently across variants
2. Adding explicit grounding context to anchor the expected answer
3. Specifying output constraints (format, length, scope) that reduce response variability

---

## Files in This Directory

Results files will be named by domain and evaluation run date, e.g.:

```
technical-2024-q4.md
educational-2024-q4.md
general-2024-q4.md
```

Each file lists prompt set IDs, per-dimension scores, and consistency flags.
