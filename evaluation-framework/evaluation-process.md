# Evaluation Process

**Purpose:** Step-by-step workflow for running a prompt evaluation.

---

## Overview

Evaluation runs follow this sequence:

1. Select the prompt set
2. Run prompts against the model
3. Score each response
4. Compute aggregate scores
5. Log results

---

## Step 1: Select the Prompt Set

Choose the prompt set to evaluate. Note:
- Domain (technical / educational / general)
- Metrics applicable to this set
- Number of variants per prompt

Confirm that each variant has a defined reference answer before running.

---

## Step 2: Run Prompts Against the Model

For each variant in the prompt set:
- Use temperature = 0 for deterministic responses (or temperature = 1 with 3+ runs for stochastic models)
- Use no system prompt unless testing system prompt behavior specifically
- Record the full response text, not just the conclusion

If running at temperature > 0, run each variant at least 3 times and use the median score.

---

## Step 3: Score Each Response

For each response, score each applicable metric using the rubric in [`scoring-rubric.md`](scoring-rubric.md).

Record:
- Prompt ID and variant label (A/B/C)
- Score per dimension
- Notes on specific issues (e.g., which claim was hallucinated, which constraint was violated)

Do not use the aggregate score as a shortcut during scoring. Score each dimension independently.

---

## Step 4: Compute Aggregate Scores

For each prompt set:
1. Compute per-variant aggregate scores
2. Compute mean score across variants (consistency check)
3. Compute variance across variants — flag if > 0.5 on any dimension

For the full evaluation run:
1. Compute average aggregate score per domain
2. Compute average per-dimension score across all prompts

---

## Step 5: Log Results

Create a results entry in `experiments/` or `evaluations/results/` with:
- Date and model version
- Prompt set IDs evaluated
- Per-prompt scores
- Aggregate summary statistics
- Notes on any anomalies or unexpected behaviors

---

## Quality Checks

Before finalizing an evaluation run:

- [ ] All variants were scored independently (not influenced by knowledge of other variant scores)
- [ ] All flagged hallucinations have specific claims documented
- [ ] All constraint violations have the specific constraint identified
- [ ] Scoring decisions are consistent across similar cases (re-check if in doubt)
- [ ] Results are stored with model version and date
