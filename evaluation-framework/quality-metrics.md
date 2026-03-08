# Quality Metrics

Detailed scoring guidance for each evaluation dimension used in this repository.

---

## Accuracy (AC)

Measures factual correctness of model responses.

**What to evaluate:**
- Is the core answer correct?
- Are supporting details accurate and verifiable?
- Are any claims demonstrably false or misleading?

**Scoring guide:**

| Score | Meaning |
|---|---|
| 3 | Fully accurate — all claims are correct and well-supported |
| 2 | Mostly accurate — minor inaccuracies that do not affect the core answer |
| 1 | Partially accurate — notable inaccuracies present |
| 0 | Inaccurate — significant factual errors throughout |

---

## Reasoning Quality (RQ)

Evaluates the logical structure and coherence of the model's explanation.

**What to evaluate:**
- Are intermediate steps present and clearly articulated?
- Does the reasoning lead logically to the conclusion?
- Are there any gaps, leaps, or contradictions in the reasoning chain?

**Scoring guide:**

| Score | Meaning |
|---|---|
| 3 | Reasoning is clear, complete, and logically sound |
| 2 | Reasoning is mostly sound with minor gaps |
| 1 | Some reasoning present but contains logical errors or gaps |
| 0 | Reasoning is absent, incoherent, or leads to a wrong conclusion |

---

## Instruction Following (IF)

Tests whether the model respected all explicit constraints defined in the prompt.

**What to evaluate:**
- Were all format requirements met (e.g., bullet points, numbered lists, sections)?
- Was the response length within specified limits?
- Was tone and audience targeting appropriate?
- Were all parts of the prompt addressed?

**Scoring guide:**

| Score | Meaning |
|---|---|
| 3 | All constraints fully and precisely respected |
| 2 | All constraints mostly followed with minor deviations |
| 1 | Most constraints followed; one is partially violated |
| 0 | One or more explicit constraints ignored |

---

## Hallucination Rate (HR)

Tracks unsupported or fabricated claims in the model's response.

**What to evaluate:**
- Does the response contain any claims that cannot be verified?
- Are any claims demonstrably false?
- Does the model acknowledge uncertainty when appropriate?

**Scoring guide:**

| Score | Meaning |
|---|---|
| 3 | No unsupported claims — all facts are verifiable |
| 2 | One minor unsupported claim present |
| 1 | Multiple unsupported claims, or one significant fabrication |
| 0 | Response is substantially hallucinated |

**Note:** This metric is scored as a quality score where **higher is better** (3 = best, 0 = worst), consistent with all other dimensions.

---

## Clarity (CL)

Measures the readability, structure, and explanation quality of the response.

**What to evaluate:**
- Is the response well-structured and easy to follow?
- Is the language appropriate for the intended audience?
- Is the response concise without omitting essential information?

**Scoring guide:**

| Score | Meaning |
|---|---|
| 3 | Exceptionally clear, well-structured, and audience-appropriate |
| 2 | Mostly clear and well-structured with minor issues |
| 1 | Somewhat readable but has notable clarity issues |
| 0 | Unclear, poorly structured, or inappropriate for the audience |

---

## Aggregate Score Formula

```
Aggregate = sum(applicable_dimension_scores) / (number_of_applicable_dimensions × 3) × 100%
```

**Example:** A response scored on Accuracy (3), Reasoning Quality (2), and Clarity (3) with Instruction Following and Hallucination Rate not applicable:

```
Aggregate = (3 + 2 + 3) / (3 × 3) × 100% = 8/9 × 100% ≈ 89%
```

---

## Metric Summary

| Metric | Abbreviation | What it measures |
|---|---|---|
| Accuracy | AC | Factual correctness of the response |
| Reasoning Quality | RQ | Logical coherence and completeness of reasoning steps |
| Instruction Following | IF | Adherence to explicit prompt constraints |
| Hallucination Rate | HR | Frequency of unsupported or fabricated claims (higher = better) |
| Clarity | CL | Readability and explanation quality |
