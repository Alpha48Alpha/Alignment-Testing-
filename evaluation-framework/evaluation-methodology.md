# LLM Evaluation Methodology

This framework evaluates model responses across several dimensions to enable systematic, reproducible assessment of language model behavior.

---

## Evaluation Dimensions

### Accuracy

Measures factual correctness of model responses.

Evaluates whether information produced by the model is correct and supported by reliable knowledge sources.

**Scoring:** 0 (significant factual errors) — 3 (fully accurate and well-supported)

---

### Reasoning

Evaluates the logical quality of explanation steps.

Focuses on whether the model's reasoning process is clear, coherent, and logically structured from premise to conclusion.

**Scoring:** 0 (absent or incoherent) — 3 (clear, complete, and logically sound)

---

### Instruction Following

Tests whether prompt constraints are respected.

Constraints may include format requirements, response length limits, tone specifications, audience targeting, and role adherence.

**Scoring:** 0 (constraints ignored) — 3 (all constraints fully respected)

---

### Clarity

Measures explanation readability and structure.

A high-quality response uses understandable language, presents structured explanations, and adapts to the intended audience.

**Scoring:** 0 (unclear or poorly structured) — 3 (exceptionally clear and well-structured)

---

### Hallucination Risk

Tracks unsupported or fabricated claims.

Hallucinations occur when a model produces information that appears factual but lacks reliable evidence or is demonstrably false.

**Scoring:** 0 (substantially hallucinated) — 3 (no unsupported claims)

---

## Aggregate Score

```
Aggregate = sum(applicable_dimension_scores) / (number_of_applicable_dimensions × 3) × 100%
```

When all five dimensions apply, the maximum total is 15 points (100%).

---

## Evaluation Process

1. Select a prompt set from the relevant domain folder (`prompts/`).
2. Run each prompt variant independently against the target model.
3. Score each response on all applicable dimensions using the 0–3 scale.
4. Compute per-variant aggregate scores.
5. Calculate variance across variants to assess consistency.
6. Record results in `evaluations/results/`.

---

## Consistency Measurement

A prompt set is considered **consistent** when score variance across its variants is ≤ 0.5 on each dimension.

High consistency indicates that prompt meaning is unambiguous and that the model reliably interprets it the same way regardless of phrasing.

---

## Relationship to Other Documents

| Document | Purpose |
|---|---|
| `evaluation-checklist.md` | Step-by-step checklist for conducting an evaluation |
| `quality-metrics.md` | Detailed scoring guidance for each dimension |
| `evaluations/metrics.md` | Core metric definitions used across the repository |
| `evaluations/framework.md` | Scoring rubric and results summary |
