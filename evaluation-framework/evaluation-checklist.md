# LLM Evaluation Checklist

Use this checklist to conduct a complete, reproducible evaluation of a prompt set.

---

## Pre-Evaluation Setup

- [ ] Identify the target model and version being evaluated.
- [ ] Record the evaluation date and evaluator name (or ID).
- [ ] Confirm the prompt set to be evaluated and the domain it belongs to.
- [ ] Note any applicable constraints defined in the prompt (format, length, tone, audience).

---

## Prompt Execution

- [ ] Run **Variant A** independently against the model. Record the full response.
- [ ] Run **Variant B** independently against the model. Record the full response.
- [ ] Run **Variant C** independently against the model (if applicable). Record the full response.
- [ ] Ensure each variant is run in a fresh context (no prior conversation history).

---

## Scoring — Per Variant

For each variant response, score each applicable dimension on a **0–3 scale**:

- [ ] **Accuracy (AC):** Is the core answer factually correct and well-supported?
- [ ] **Reasoning Quality (RQ):** Are logical steps clear, coherent, and complete?
- [ ] **Instruction Following (IF):** Are all explicit prompt constraints respected?
- [ ] **Hallucination Rate (HR):** Are all factual claims verifiable? (3 = no hallucinations)
- [ ] **Clarity (CL):** Is the response well-structured and easy to follow?

---

## Aggregate Score Calculation

- [ ] Sum the applicable dimension scores for each variant.
- [ ] Divide by `(number of applicable dimensions × 3)`.
- [ ] Multiply by 100% to obtain the aggregate percentage score.

```
Aggregate = sum(applicable_scores) / (applicable_dimensions × 3) × 100%
```

---

## Consistency Check

- [ ] Compare aggregate scores across all variants.
- [ ] Calculate variance in scores across variants.
- [ ] Flag the prompt set as **inconsistent** if variance exceeds **0.5** on any dimension.
- [ ] If inconsistent, note specific variants and dimensions with high variance.

---

## Hallucination Verification

- [ ] List all factual claims made in each response.
- [ ] Cross-reference each claim against a reliable knowledge source.
- [ ] Flag any claim that cannot be verified or is demonstrably false.
- [ ] Record hallucination findings in the results file.

---

## Results Recording

- [ ] Record all variant scores in `evaluations/results/`.
- [ ] Note any anomalous behaviors or unexpected model outputs.
- [ ] Record the aggregate score for the prompt set.
- [ ] Update the domain-level results summary if applicable.

---

## Post-Evaluation Review

- [ ] Review flagged inconsistencies and consider prompt refinements.
- [ ] Update `experiments/` if the evaluation reveals new behavioral patterns.
- [ ] Confirm all results are committed and documented.
