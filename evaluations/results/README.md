# Evaluation Results

Per-prompt scores for all evaluated prompt sets are stored in this directory, organized by domain.

Each results file records scores across five dimensions — Accuracy (AC), Reasoning Quality (RQ), Instruction Following (IF), Hallucination Rate (HR), and Clarity (CL) — on the 0–3 scale defined in [../metrics.md](../metrics.md). See [../framework.md](../framework.md) for the aggregate scoring formula and consistency methodology.

---

## Domain Summary

| Domain | Prompts Evaluated | Avg Consistency Score | Avg Accuracy Score |
|---|---|---|---|
| Technical | ~200 | 68% | 74% |
| Educational | ~150 | 71% | 80% |
| General Knowledge | ~150 | 72% | 76% |
| **Total / Overall** | **~500+** | **~70%** | **~76%** |

Baseline consistency (before prompt refinement): ~52%  
Consistency after refinement: ~70%  
Relative improvement: **+35%**

> Consistency is the percentage of prompt sets where all variants (A/B/C rephrasings) receive identical scores. The improvement reflects reduced prompt ambiguity, added grounding context, and explicit output constraints.
