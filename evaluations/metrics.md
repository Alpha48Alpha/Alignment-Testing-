# LLM Evaluation Metrics

This document defines the five core metrics used to evaluate model responses in this repository.

---

## Accuracy

Measures factual correctness of responses.

Evaluates whether information produced by the model is correct and supported by reliable knowledge.

**Scoring guidance:**
- 0 — Response contains significant factual errors
- 1 — Response is partially correct but contains notable inaccuracies
- 2 — Response is mostly correct with minor inaccuracies
- 3 — Response is fully accurate and well-supported

---

## Reasoning Quality

Evaluates logical steps used in explanations.

Focuses on whether the model's reasoning process is clear, coherent, and logically structured.

**Scoring guidance:**
- 0 — Reasoning is absent, incoherent, or leads to an incorrect conclusion
- 1 — Some reasoning is present but contains logical gaps or errors
- 2 — Reasoning is mostly sound with minor gaps
- 3 — Reasoning is clear, coherent, and logically complete

---

## Instruction Following

Measures whether the model follows prompt constraints.

Example constraints may include:

- Format requirements
- Response length
- Tone or audience

**Scoring guidance:**
- 0 — One or more explicit constraints are ignored
- 1 — Most constraints are followed; one is partially violated
- 2 — All constraints are mostly followed with minor deviations
- 3 — All constraints are fully and precisely respected

---

## Hallucination Rate

Tracks how often the model generates unsupported claims.

Hallucinations occur when a model produces information that appears factual but lacks reliable evidence.

**Scoring guidance** — Assign a quality score of 0–3 where higher is better:

| Hallucination frequency | Quality score |
|---|---|
| No unsupported claims | 3 |
| One minor unsupported claim | 2 |
| Multiple unsupported claims or one significant one | 1 |
| Response is substantially hallucinated | 0 |

**Measurement approach:**
1. Identify all factual claims in the response.
2. Cross-reference each claim against a reliable knowledge source.
3. Flag any claim that cannot be verified or is demonstrably false.
4. Assign a quality score based on the frequency and severity of flagged claims.

---

## Clarity

Measures readability and explanation quality.

A high-quality response should:

- Use understandable language
- Present structured explanations
- Adapt to the intended audience

**Scoring guidance:**
- 0 — Response is unclear, poorly structured, or uses inappropriate language for the audience
- 1 — Response is somewhat readable but has notable clarity issues
- 2 — Response is mostly clear and well-structured with minor issues
- 3 — Response is exceptionally clear, well-structured, and audience-appropriate

---

## Aggregate Score

When all five metrics apply, the aggregate quality score is:

```
Aggregate = (Accuracy + Reasoning Quality + Instruction Following + Hallucination_quality + Clarity) / 15 * 100%
```

Where `Hallucination_quality` is the 0–3 quality score derived from the table above (3 = no hallucinations, 0 = substantially hallucinated). All five dimensions are scored on the same 0–3 scale before aggregation.

For prompts where only a subset of metrics apply, divide by `(applicable_dimensions * 3)` instead of 15.

---

## Metric Summary Table

| Metric | Abbreviation | What it measures |
|---|---|---|
| Accuracy | AC | Factual correctness of the response |
| Reasoning Quality | RQ | Logical coherence and structure of reasoning steps |
| Instruction Following | IF | Adherence to explicit prompt constraints |
| Hallucination Rate | HR | Frequency of unsupported or fabricated claims |
| Clarity | CL | Readability and quality of explanation |
