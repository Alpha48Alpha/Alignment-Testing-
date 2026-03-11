# Evaluation Framework

**Purpose:** Core methodology, metric definitions, and scoring rubric for all evaluation work in this repository.

---

## Files

| File | Contents |
|---|---|
| [`metrics.md`](metrics.md) | Definitions and scoring guidance for all five evaluation metrics |
| [`scoring-rubric.md`](scoring-rubric.md) | Scoring rubric with examples for each dimension |
| [`evaluation-process.md`](evaluation-process.md) | Step-by-step evaluation workflow |

---

## Five Core Metrics

| Metric | Abbreviation | What it measures |
|---|---|---|
| Accuracy | AC | Factual correctness of the response |
| Reasoning Quality | RQ | Logical coherence and structure of reasoning steps |
| Instruction Following | IF | Adherence to explicit prompt constraints |
| Hallucination Rate | HR | Frequency of unsupported or fabricated claims (inverted: 3 = no hallucinations) |
| Clarity | CL | Readability and quality of explanation |

Each metric is scored 0–3. The aggregate score across applicable metrics is:

```
Aggregate = sum(applicable_metric_scores) / (applicable_dimensions × 3) × 100%
```

---

## Consistency Measurement

Response consistency is measured by running semantically equivalent prompt variants and comparing scores:

1. Run all variants of a prompt set independently
2. Score each variant on applicable dimensions
3. Compute variance across variant scores
4. A consistent prompt set has variance ≤ 0.5 on any dimension

High variance across variants indicates either prompt sensitivity (the model is over-fitting to surface form) or poorly specified variants (the variants are not actually equivalent in difficulty).
