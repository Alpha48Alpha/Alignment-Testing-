# Evaluation Metrics

This document defines the five core metrics used to evaluate model responses in this repository.

---

## Accuracy (AC)

Measures factual correctness of responses.

Evaluates whether information produced by the model is correct and supported by reliable knowledge.

**Scoring guidance:**
- 0 — Response contains significant factual errors
- 1 — Response is partially correct but contains notable inaccuracies
- 2 — Response is mostly correct with minor inaccuracies
- 3 — Response is fully accurate and well-supported

**Example (Score 3):**
- Prompt: "What year did the Berlin Wall fall?"
- Response: "The Berlin Wall fell in 1989, with the first sections opened on November 9th of that year."
- Assessment: Correct year and date. Score: 3.

**Example (Score 1):**
- Prompt: "What year did the Berlin Wall fall?"
- Response: "The Berlin Wall came down in the late 1980s, around 1988 or so."
- Assessment: Approximate but inaccurate year. Score: 1.

---

## Reasoning Quality (RQ)

Evaluates logical steps used in explanations.

**Scoring guidance:**
- 0 — Reasoning is absent, incoherent, or leads to an incorrect conclusion
- 1 — Some reasoning is present but contains logical gaps or errors
- 2 — Reasoning is mostly sound with minor gaps
- 3 — Reasoning is clear, coherent, and logically complete

**Example (Score 3):**
- Prompt: "If all A are B, and all B are C, is it necessarily true that all A are C?"
- Response: "Yes. Since every A is a B, and every B is a C, by transitivity every A must also be a C. This is a valid syllogism."
- Assessment: Identifies the logical principle correctly and applies it. Score: 3.

**Example (Score 0):**
- Same prompt. Response: "It depends on the context. Sometimes A can be C, sometimes not."
- Assessment: No reasoning; incorrect conclusion. Score: 0.

---

## Instruction Following (IF)

Measures whether the model follows prompt constraints.

**Scoring guidance:**
- 0 — One or more explicit constraints are ignored
- 1 — Most constraints are followed; one is partially violated
- 2 — All constraints are mostly followed with minor deviations
- 3 — All constraints are fully and precisely respected

**Example constraints:** format, length, tone, audience, language, prohibited elements.

**Example (Score 0):**
- Prompt: "Explain neural networks in exactly three bullet points."
- Response: A five-paragraph essay.
- Assessment: Format and length constraints both violated. Score: 0.

---

## Hallucination Rate (HR)

Tracks how often the model generates unsupported claims. Scored as a quality measure (higher = better).

**Scoring guidance:**

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
4. Assign a quality score based on frequency and severity.

**High-risk prompt types:** Citation requests, biographical questions, requests for specific statistics, legal or regulatory references.

---

## Clarity (CL)

Measures readability and explanation quality.

**Scoring guidance:**
- 0 — Response is unclear, poorly structured, or uses inappropriate language for the audience
- 1 — Response is somewhat readable but has notable clarity issues
- 2 — Response is mostly clear and well-structured with minor issues
- 3 — Response is exceptionally clear, well-structured, and audience-appropriate

**Example (Score 3):**
- Prompt: "Explain how HTTPS works to a non-technical audience."
- Response uses an analogy (sealed envelope), avoids acronyms, explains the key concept (encryption) without technical detail, and is well-structured.

**Example (Score 1):**
- Same prompt. Response uses terms like "asymmetric key exchange," "TLS handshake," and "certificate authority" without explanation.

---

## Aggregate Score

```
Aggregate = sum(applicable_metric_scores) / (applicable_dimensions × 3) × 100%
```

For a response scored on all five dimensions: divide the sum by 15.  
For a response scored on three dimensions: divide the sum by 9.

---

## Metric Summary Table

| Metric | Abbreviation | Scale | What it measures |
|---|---|---|---|
| Accuracy | AC | 0–3 | Factual correctness |
| Reasoning Quality | RQ | 0–3 | Logical coherence and reasoning steps |
| Instruction Following | IF | 0–3 | Adherence to explicit constraints |
| Hallucination Rate | HR | 0–3 (inverted) | Frequency of unsupported claims |
| Clarity | CL | 0–3 | Readability and explanation quality |
