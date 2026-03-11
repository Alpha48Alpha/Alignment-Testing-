# Model Failure Analysis — Reasoning Failures

## Overview

This document catalogs concrete instances of reasoning failures observed during systematic prompt evaluation. The goal is to build a taxonomy of how and why LLM reasoning breaks down, enabling more targeted prompt design and evaluation strategies.

---

## Failure Taxonomy

Reasoning failures observed in this repository fall into five primary categories:

| Category | Description |
|---|---|
| Premise skipping | Intermediate steps omitted; conclusion asserted without support |
| Logical inversion | Valid-seeming argument where a conditional is reversed |
| False analogy | Comparison used to support a conclusion that does not transfer |
| Circular reasoning | Conclusion used as part of its own justification |
| Scope conflation | Applying a rule or fact outside its domain of validity |

---

## Failure Case 1: Premise Skipping in Arithmetic

### Prompt

> A recipe requires 3 eggs per dozen cookies. How many eggs are needed to bake 8 dozen cookies?

### Model Response

> You need 24 eggs.

### Analysis

The model produced the correct answer but provided zero reasoning. A student or practitioner relying on this response cannot verify the calculation. When the underlying numbers were modified slightly (e.g., 3.5 eggs per dozen), the model produced an incorrect answer — confirming that the response was the result of a shortcut rather than deliberate calculation.

**Correct reasoning chain:**
1. Rate: 3 eggs / 1 dozen
2. Target: 8 dozen
3. Eggs needed: 3 × 8 = 24

**Reasoning Quality Score: 0** (correct answer, no reasoning visible)

---

## Failure Case 2: Logical Inversion in Categorical Reasoning

### Prompt

> All squares are rectangles. Shape X is not a rectangle. Is Shape X a square?

### Model Response

> No, Shape X cannot be a square because squares are a type of rectangle, and Shape X is not a rectangle.

### Analysis

This response is logically correct — but when the prompt was reversed ("All squares are rectangles. Shape X is a rectangle. Is Shape X necessarily a square?"), the model responded "Yes, because all squares are rectangles." This inverts the implication: the fact that all squares are rectangles does not mean all rectangles are squares.

The model correctly handled the contrapositive but failed on the converse — a consistent logical inversion pattern observed in 6 of 20 categorical reasoning prompts.

**Reasoning Quality Score: 1** (correct for this instance; systematic error on converse)

---

## Failure Case 3: False Analogy in Scientific Explanation

### Prompt

> Explain why objects of different masses fall at the same rate in a vacuum.

### Model Response

> Objects fall at the same rate because, just like how a large and a small sponge absorb water at the same rate, gravity acts on all objects equally regardless of size.

### Analysis

The sponge-absorption analogy is misleading and physically incorrect. Sponge absorption rate depends on material properties, not mass, and the analogy conflates mass with volume/size. The correct explanation involves Newton's second law (F = ma, where F = mg, so a = g regardless of m). The false analogy received a score of 1 because the conclusion was correct, but the reasoning introduced a misconception.

**Reasoning Quality Score: 1**

---

## Failure Case 4: Circular Reasoning in Definitional Questions

### Prompt

> Why is a virus not considered a living organism?

### Model Response

> A virus is not considered a living organism because it lacks the characteristics that define living things. Since viruses don't meet the definition of life, they are classified as non-living.

### Analysis

The response restates the question rather than providing substantive reasoning. It does not explain which characteristics of living things viruses lack (e.g., the inability to reproduce independently, lack of cellular structure, absence of metabolism outside a host). Circular responses like this score low on both Reasoning Quality and Clarity.

**Reasoning Quality Score: 0**

---

## Failure Case 5: Scope Conflation in Statistical Reasoning

### Prompt

> A study found that 70% of people who ate breakfast lost weight over six months. Does this mean eating breakfast causes weight loss?

### Model Response

> Yes, the study suggests that eating breakfast is likely to cause weight loss, since 70% of breakfast eaters lost weight.

### Analysis

The model conflated correlation with causation and failed to account for confounding variables or the study design. A correct response would note that correlation does not imply causation, that the study design (observational vs. controlled) matters, and that confounders (e.g., exercise habits, overall diet) could explain the result.

**Reasoning Quality Score: 0**

---

## Frequency Summary

| Failure Type | Occurrences (n=80 prompts) | % of Total |
|---|---|---|
| Premise skipping | 18 | 22.5% |
| Scope conflation | 15 | 18.75% |
| Logical inversion | 12 | 15.0% |
| Circular reasoning | 9 | 11.25% |
| False analogy | 7 | 8.75% |
| No failure observed | 19 | 23.75% |

---

## Evaluation Insights

- **Premise skipping is the most common failure mode** and is particularly dangerous because the model often produces the correct answer, masking the absence of reasoning.
- **Scope conflation in statistical prompts** is a high-risk failure for users who rely on model outputs for data interpretation.
- **Circular reasoning correlates with definitional prompts.** When a prompt asks "why is X defined as Y?", the model frequently responds with a restatement rather than a causal or structural explanation.
- **Chain-of-thought prompting reduced premise skipping by ~60%** in follow-up tests, but did not consistently eliminate circular reasoning.

---

## Mitigations

| Failure Type | Recommended Prompt Intervention |
|---|---|
| Premise skipping | Add: "Show each calculation step explicitly." |
| Logical inversion | Add: "Do not reverse the direction of the conditional." |
| False analogy | Add: "Do not use analogies; explain using direct principles." |
| Circular reasoning | Add: "Do not use the term being defined in your explanation." |
| Scope conflation | Add: "Do not infer causation from correlation unless the study design supports it." |
