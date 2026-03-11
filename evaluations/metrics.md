# LLM Evaluation Metrics

This document defines the five core metrics used to evaluate model responses in this repository. Each metric uses a 0–3 integer scale; see [`framework.md`](framework.md) for the aggregate scoring formula.

---

## Accuracy (AC)

Measures whether the model's response is factually correct and supported by verifiable knowledge sources.

**Scoring guidance:**
- 0 — Response contains significant factual errors that undermine the answer
- 1 — Core answer is partially correct but contains notable inaccuracies in details
- 2 — Response is mostly accurate with only minor factual deviations
- 3 — All factual claims are correct and well-supported

---

## Reasoning Quality (RQ)

Measures whether the model's reasoning chain is logically sound, clearly presented, and leads to a correct conclusion.

**Scoring guidance:**
- 0 — Reasoning is absent, incoherent, or contradicts the stated conclusion
- 1 — Some reasoning is present but contains logical gaps or errors in intermediate steps
- 2 — Reasoning is mostly sound with minor gaps or unstated assumptions
- 3 — Reasoning is explicit, coherent, and logically complete from premise to conclusion

---

## Instruction Following (IF)

Measures whether the model respects all explicit output constraints specified in the prompt, including format, length, tone, audience, and role.

**Scoring guidance:**
- 0 — One or more explicit constraints are ignored entirely
- 1 — Most constraints are followed; one is partially or inconsistently respected
- 2 — All constraints are mostly followed with only minor deviations
- 3 — All constraints are fully and precisely respected

---

## Hallucination Rate (HR)

Measures how often the model produces claims that appear factual but are unverifiable or demonstrably false. Scored as a quality metric (higher = fewer hallucinations).

**Scoring guidance:**

| Hallucination frequency | Quality score |
|---|---|
| No unsupported claims | 3 |
| One minor unsupported claim | 2 |
| Multiple unsupported claims, or one significant one | 1 |
| Response is substantially hallucinated | 0 |

**Measurement procedure:**
1. Enumerate all factual claims in the response.
2. Cross-reference each claim against a reliable knowledge source (e.g., Wikipedia, PubMed, official documentation).
3. Flag any claim that cannot be verified or is demonstrably false.
4. Assign the quality score based on the count and severity of flagged claims.

---

## Clarity (CL)

Measures the readability, structural quality, and audience-appropriateness of the response.

**Scoring guidance:**
- 0 — Response is disorganized, uses inappropriate language for the stated audience, or is difficult to follow
- 1 — Response is somewhat readable but has notable structural or language issues
- 2 — Response is clear and well-organized with only minor issues
- 3 — Response is exceptionally clear, well-structured, and precisely calibrated to the intended audience

---

## Aggregate Score

```
Aggregate = sum(applicable_metric_scores) / (number_of_applicable_metrics × 3) × 100%
```

When all five metrics apply, this simplifies to:

```
Aggregate = (AC + RQ + IF + HR + CL) / 15 × 100%
```

`HR` uses the 0–3 quality score defined above (3 = no hallucinations, 0 = substantially hallucinated), consistent with the other four dimensions.

---

## Metric Summary Table

| Metric | Abbreviation | What it measures |
|---|---|---|
| Accuracy | AC | Factual correctness of the response |
| Reasoning Quality | RQ | Logical coherence and completeness of reasoning steps |
| Instruction Following | IF | Adherence to all explicit prompt constraints |
| Hallucination Rate | HR | Absence of unsupported or fabricated claims |
| Clarity | CL | Readability and audience-appropriateness of the response |
