# Scoring Rubric

**Purpose:** Detailed scoring guidance with annotated examples for each evaluation dimension.

---

## Scoring Scale

All metrics use a 0–3 integer scale:

| Score | General meaning |
|---|---|
| 3 | Fully meets the criterion |
| 2 | Mostly meets the criterion with minor issues |
| 1 | Partially meets the criterion; notable issues present |
| 0 | Fails to meet the criterion |

Half-scores (e.g., 2.5) are not used. When a response falls between two levels, round to the lower score unless the evidence clearly favors the higher.

---

## Accuracy (AC)

### Score 3
All factual claims are correct and well-supported. No inaccuracies of any significance.

*Example:* "The Turing Test was proposed by Alan Turing in 1950 in his paper 'Computing Machinery and Intelligence.'" — Correct author, year, and paper title.

### Score 2
Mostly correct. May contain a minor inaccuracy (an imprecise date, a slightly overstated figure) that does not affect the core answer.

*Example:* "Turing proposed the test in the early 1950s" — approximate but not materially wrong.

### Score 1
Core answer is partially correct but contains a notable inaccuracy or is missing important context that changes the interpretation.

*Example:* "Turing won the Nobel Prize for his work on computing." — Incorrect; Turing received no Nobel Prize.

### Score 0
Response contains significant factual errors or is fundamentally incorrect.

---

## Reasoning Quality (RQ)

### Score 3
Reasoning chain is complete and logically valid. Each step follows from the previous. Conclusion is correct and justified.

### Score 2
Reasoning is mostly sound. May skip a step or include a minor logical imprecision that does not affect the conclusion.

### Score 1
Reasoning contains a notable gap or error. The model may reach a correct conclusion through flawed reasoning ("right answer, wrong method") or an incorrect conclusion through partially valid reasoning.

### Score 0
Reasoning is absent, circular, or leads to a demonstrably wrong conclusion.

---

## Instruction Following (IF)

Evaluate each explicit constraint in the prompt separately. Use the following table:

| Constraints violated | Score |
|---|---|
| None | 3 |
| One minor violation | 2 |
| One major or multiple minor violations | 1 |
| Multiple major violations | 0 |

**What counts as a constraint:** Any explicit requirement in the prompt specifying format, length, tone, audience, language, content inclusion/exclusion, or response structure.

**What does not count as a constraint:** Implicit expectations not stated in the prompt.

---

## Hallucination Rate (HR)

### Score 3
No unsupported claims. All factual assertions can be verified against a reliable source.

### Score 2
One minor unsupported claim. The claim is peripheral (not central to the response) and plausible but cannot be confirmed.

### Score 1
Multiple unsupported claims, or one significant unsupported claim that affects the reliability of the core answer.

### Score 0
The response is substantially hallucinated. The central claims are fabricated or unverifiable.

**Flagging protocol:** Document each flagged claim with the text of the claim and the reason it cannot be verified.

---

## Clarity (CL)

### Score 3
Exceptionally clear. Well-structured, correct vocabulary for the audience, concise, no unnecessary jargon, no ambiguity.

### Score 2
Mostly clear. Minor issues: one jargon term that could be explained, a slightly awkward structure, or one section that is harder to follow than the rest.

### Score 1
Readable but has notable clarity issues: multiple unexplained technical terms, poor structure, or language that is inappropriate for the stated audience.

### Score 0
Response is difficult to understand, poorly organized, or uses language completely inappropriate for the audience.

---

## Aggregate Score Calculation

```
Aggregate = sum(applicable_metric_scores) / (applicable_dimensions × 3) × 100%
```

**Example:**
A response is scored on three dimensions (AC=3, RQ=2, CL=3):
```
Aggregate = (3 + 2 + 3) / (3 × 3) × 100% = 8/9 × 100% ≈ 89%
```

**Example with all five dimensions** (AC=3, RQ=2, IF=3, HR=3, CL=2):
```
Aggregate = (3 + 2 + 3 + 3 + 2) / 15 × 100% = 13/15 × 100% ≈ 87%
```
