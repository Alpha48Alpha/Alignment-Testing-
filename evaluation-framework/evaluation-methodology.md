# Evaluation Framework — Evaluation Methodology

## Overview

This document describes the methodology used to systematically evaluate LLM prompt responses in this repository. It serves as the primary reference for how evaluations are designed, executed, and interpreted. For metric definitions, see `evaluations/metrics.md`. For scoring rules, see `evaluations/framework.md`.

---

## Evaluation Design Principles

1. **Reproducibility** — Evaluations must be reproducible. All prompts, model configurations, decoding parameters, and scoring rubrics are documented so that results can be replicated independently.

2. **Separability** — Each evaluation dimension (Accuracy, Reasoning Quality, etc.) is scored independently before aggregation. Evaluators should not let their impression of one dimension influence another.

3. **Ground-truth anchoring** — Evaluations of factual content require reference answers from authoritative external sources. Evaluations without ground truth are treated as exploratory and labeled accordingly.

4. **Multi-run evaluation** — Each prompt variant is evaluated across at least five independent runs to account for stochastic variance from model decoding.

5. **Minimal evaluator assumptions** — Evaluators should score based on the content of the response alone, not inferred intent. A response that contains an error is scored as erroneous even if the error is plausibly a typo.

---

## Evaluation Workflow

### Step 1: Prompt Preparation

Before evaluation begins, each prompt must have:
- A completed prompt text and at least one variant
- A list of applicable evaluation metrics
- A reference answer (for AC and HR scoring)
- A defined target audience (for CL scoring)

### Step 2: Model Configuration

Record the following for each evaluation session:
- Model identifier and version
- Temperature and top-p settings
- System prompt (if any)
- Context window configuration

### Step 3: Response Collection

Submit each prompt variant to the model independently. Collect a minimum of five responses per variant. Do not cherry-pick or discard responses unless a technical error (e.g., truncation due to token limit) occurred and is documented.

### Step 4: Scoring

Score each response independently on all applicable metrics:
1. Read the full response before assigning any score.
2. Score Accuracy first (requires external reference verification).
3. Score Hallucination Rate (cross-reference all specific factual claims).
4. Score Reasoning Quality (requires tracing the full reasoning chain).
5. Score Instruction Following (enumerate constraints and check each).
6. Score Clarity last (a holistic assessment of readability).

### Step 5: Aggregation

Compute per-response, per-prompt, per-domain, and benchmark-level aggregates following the formulas in `llm-benchmark-design/scoring-framework.md`.

### Step 6: Consistency and Robustness Calculation

Compute the Consistency Index (CI) for each prompt set using the five-run scores. Compute the Robustness Score (RS) using the variant comparison.

### Step 7: Results Recording

Record all individual scores, aggregates, CI, and RS values in `evaluations/results/`. Include qualitative notes on any notable observations.

---

## Inter-Annotator Reliability

All evaluations requiring human judgment use two independent annotators. Agreement is measured with Cohen's Kappa (κ):

| κ Range | Action |
|---|---|
| ≥ 0.80 | Accept both annotations; use mean scores |
| 0.60–0.79 | Adjudication required (third annotator resolves) |
| < 0.60 | Rubric revision required before re-annotation |

Low κ values consistently observed for a specific metric indicate that the scoring rubric for that metric needs clarification.

---

## Handling Edge Cases

### Model Refusals

When a model refuses to answer a prompt that should receive a response, record it as an over-refusal and apply the scoring rules in `llm-benchmark-design/scoring-framework.md`.

### Truncated Responses

Score truncated responses on the content present. Document the truncation and whether it occurred before or after the core answer.

### Off-Topic Responses

A response that does not address the prompt is scored AC: 0, IF: 0, CL: 0. Reasoning Quality and Hallucination Rate are not scored for off-topic responses.

### Ambiguous Prompts

If evaluators identify genuine prompt ambiguity that could reasonably produce multiple correct interpretations, the prompt is flagged for revision. Scores from the ambiguous version are retained but labeled as exploratory.

---

## Evaluation Schedule

Structured evaluations are conducted in three phases:

| Phase | Description | Frequency |
|---|---|---|
| Baseline | Initial evaluation of all prompts in a new domain | Once per domain launch |
| Iterative | Evaluation after prompt refinement iterations | After each iteration |
| Regression | Re-evaluation of stable prompts when model version changes | On each new model version |

---

## Evaluation Insights

- **Separating scoring by metric significantly improves reliability.** Evaluators who scored all metrics simultaneously showed lower κ than those who scored one metric at a time across all responses.
- **Five-run evaluation is the minimum reliable threshold.** Three-run evaluations showed CI variance approximately 40% higher than five-run evaluations.
- **Reference answer quality directly limits evaluation quality.** In domains where ground-truth reference answers were incomplete, AC scores showed the lowest inter-annotator agreement.
- **Qualitative notes alongside numerical scores substantially improve rubric iteration.** Notes identifying specific failure modes allow faster rubric refinement than numerical scores alone.

---

## Relationship to Other Documents

| Document | Relationship |
|---|---|
| `evaluations/metrics.md` | Defines the five core metrics scored in this methodology |
| `evaluations/framework.md` | Specifies the scoring rubric and aggregate formula |
| `llm-benchmark-design/scoring-framework.md` | Extends this methodology with CI, RS, and weighted aggregate formulas |
| `evaluations/results/` | Stores all scores produced by this methodology |
