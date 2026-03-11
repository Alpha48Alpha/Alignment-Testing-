# Evaluation Results

This directory contains per-prompt evaluation results for each domain. Each file records scores across the five dimensions — Accuracy (AC), Reasoning Quality (RQ), Instruction Following (IF), Hallucination Rate (HR), and Clarity (CL) — along with cross-model comparisons, failure mode analysis, and consistency measurements.

See [../framework.md](../framework.md) for the full evaluation methodology and scoring rubric, and [../metrics.md](../metrics.md) for metric definitions.

---

## Results Files

| File | Domain | Contents |
|---|---|---|
| [technical_results.md](technical_results.md) | Technical | Per-prompt variant scores, failure mode analysis, multi-model hallucination comparison |
| [educational_results.md](educational_results.md) | Educational | Variant-level scores, cross-model benchmarks, consistency analysis |
| [general_results.md](general_results.md) | General Knowledge | Cross-model quality comparison, clarity and instruction-following failure patterns |

---

## Overall Summary

| Domain | Models Tested | Prompts Evaluated | Avg Consistency Score | Avg Accuracy Score |
|---|---|---|---|---|
| Technical | GPT-4o, GPT-3.5, Claude 3 Sonnet | ~200 | 68% | 74% |
| Educational | GPT-4o, GPT-3.5, Claude 3 Sonnet | ~150 | 71% | 80% |
| General Knowledge | GPT-4o, GPT-3.5, Claude 3 Sonnet | ~150 | 72% | 76% |
| **Total / Overall** | | **~500+** | **~70%** | **~76%** |

Baseline consistency (before prompt refinement): ~52%  
Improved consistency (after prompt refinement): ~70%  
Relative improvement: **+35%**

---

## Top Failure Modes by Category

| Category | Primary Failure Mode | Models Affected |
|---|---|---|
| Hallucination — Citations | Full fabrication of plausible-sounding author/journal/year combinations | GPT-3.5 |
| Hallucination — Biography | Misattributed publication venues, incorrect award dates | GPT-3.5 |
| Hallucination — Science | Misattribution of experiments to prominent figures (Heisenberg vs. Davisson/Germer) | GPT-3.5 |
| Instruction Following — Length | Compound sentences that technically violate "exactly N sentences" constraints | GPT-3.5, GPT-4o (minor) |
| Clarity — Analogical Reasoning | Generic "brain" analogy for CPU that is technically imprecise and not age-appropriate | GPT-3.5 |
| Reasoning Quality — Code | Natural-language rephrasings reduce intermediate step transparency | All models |
