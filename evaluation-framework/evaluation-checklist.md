# Evaluation Framework — Evaluation Checklist

## Overview

This checklist provides a structured reference for evaluators conducting prompt evaluations in this repository. It is designed to be used alongside the scoring rubric in `evaluations/framework.md` and the methodology in `evaluation-framework/evaluation-methodology.md`.

Complete each section in order for every evaluation session.

---

## Pre-Evaluation Setup

### Prompt Readiness

- [ ] Prompt text is finalized and stored in the correct domain folder under `prompts/`
- [ ] At least one variant (Variant B) has been created
- [ ] Target metrics for this prompt are identified
- [ ] A reference answer is available for Accuracy and Hallucination Rate scoring
- [ ] Target audience is defined (required for Clarity scoring)
- [ ] Prompt does not overlap with more than 10% of existing benchmark entries

### Model Configuration

- [ ] Model identifier and version recorded
- [ ] Temperature setting recorded
- [ ] Top-p setting recorded
- [ ] System prompt content recorded (or "none" if no system prompt)
- [ ] Context window configuration recorded

---

## Response Collection

- [ ] Prompt submitted independently for each variant
- [ ] Minimum of 5 runs collected per variant
- [ ] All responses recorded (no cherry-picking or discards without documentation)
- [ ] Any truncated responses flagged and documented with reason
- [ ] Any model refusals flagged and documented

---

## Scoring Checklist

Complete the following for each collected response before assigning scores.

### Accuracy (AC)

- [ ] Reference answer reviewed before scoring
- [ ] All factual claims in the response identified
- [ ] Each factual claim compared against the reference answer
- [ ] Score assigned: 0 (significant errors) / 1 (partial; notable inaccuracies) / 2 (mostly correct; minor inaccuracies) / 3 (fully accurate)
- [ ] Errors documented in qualitative notes

### Hallucination Rate (HR)

- [ ] All specific factual claims enumerated (names, dates, statistics, citations)
- [ ] Each claim verified against a reliable external source
- [ ] Unsupported or fabricated claims flagged and documented
- [ ] HR quality score assigned: 3 (no unsupported claims) / 2 (one minor) / 1 (multiple or one significant) / 0 (substantially hallucinated)

### Reasoning Quality (RQ)

- [ ] Full reasoning chain read (not just final answer)
- [ ] Each intermediate step evaluated for logical soundness
- [ ] Any premise skipping, logical inversion, or circular reasoning noted
- [ ] Correct final answer via incorrect reasoning scored ≤ 1 (not 3)
- [ ] Score assigned: 0 (absent/incoherent) / 1 (present with gaps) / 2 (mostly sound; minor gaps) / 3 (clear, coherent, complete)

### Instruction Following (IF)

- [ ] All explicit constraints in the prompt enumerated
- [ ] Each constraint checked against the response (format, length, tone, structure, prohibited elements)
- [ ] Number of violated constraints documented
- [ ] Score assigned: 0 (one or more constraints ignored) / 1 (most followed; one partially violated) / 2 (all mostly followed; minor deviations) / 3 (all constraints fully respected)

### Clarity (CL)

- [ ] Response evaluated relative to the specified target audience
- [ ] Structure and organization assessed
- [ ] Jargon checked for appropriateness to audience
- [ ] Conciseness assessed (no essential information omitted; no excessive padding)
- [ ] Score assigned: 0 (unclear/poorly structured) / 1 (somewhat readable; notable issues) / 2 (mostly clear; minor issues) / 3 (exceptionally clear and well-structured)

---

## Aggregation

- [ ] Per-response aggregate computed for each run: `sum(scores) / (applicable_metrics × 3) × 100%`
- [ ] Mean aggregate computed across all runs for each variant
- [ ] Consistency Index (CI) computed from the 5-run score variance
- [ ] Robustness Score (RS) computed from the variant aggregate comparison
- [ ] Weighted aggregate computed if domain-adjusted weights apply

---

## Inter-Annotator Agreement

- [ ] Second annotator has scored the same responses independently
- [ ] Cohen's Kappa (κ) computed for each metric
- [ ] κ ≥ 0.80: proceed with mean scores
- [ ] κ 0.60–0.79: third annotator adjudication completed
- [ ] κ < 0.60: rubric revision initiated (evaluation paused until resolved)

---

## Results Recording

- [ ] All per-response scores recorded in `evaluations/results/`
- [ ] Aggregate, CI, and RS scores recorded
- [ ] Qualitative notes for all notable observations recorded
- [ ] Model configuration recorded alongside results
- [ ] Any flagged items (truncations, refusals, ambiguities) documented

---

## Post-Evaluation Review

- [ ] Prompts with CI < 0.5 flagged for revision
- [ ] Prompts with RS < 0.70 flagged for variant review
- [ ] Over-refusals identified and tracked separately from quality failures
- [ ] Patterns in failure modes documented for rubric and prompt improvement
- [ ] Results summary updated in `evaluations/framework.md` if domain-level aggregates changed

---

## Quick Reference: Score Meanings

| Score | Meaning |
|---|---|
| 0 | Fails to meet the criterion |
| 1 | Partially meets the criterion |
| 2 | Mostly meets the criterion |
| 3 | Fully meets the criterion |

---

## Quick Reference: CI and RS Thresholds

| Metric | Threshold | Classification |
|---|---|---|
| CI | ≥ 0.80 | Highly consistent |
| CI | 0.50–0.79 | Moderately consistent |
| CI | < 0.50 | Inconsistent — prompt review required |
| RS | ≥ 0.85 | Robust |
| RS | 0.70–0.84 | Moderately robust |
| RS | < 0.70 | Fragile — variant review required |
