# Case Study — Reasoning Evaluation

## Overview

This case study investigates how well large language models perform on multi-step reasoning tasks and where their reasoning chains tend to break down. The analysis draws on a set of technical and mathematical prompts evaluated across three model configurations using the Reasoning Quality (RQ) metric defined in `evaluations/metrics.md`.

---

## Background

Reasoning evaluation is one of the most diagnostically useful dimensions of LLM assessment. A model that reaches a correct final answer through flawed logic is unreliable in novel contexts; a model whose reasoning chain is transparent and sound generalizes more predictably. This case study focuses on identifying failure points in model reasoning rather than simply measuring answer accuracy.

---

## Prompt Categories Evaluated

| Category | Number of Prompts | Primary Metric |
|---|---|---|
| Mathematical word problems | 25 | Reasoning Quality |
| Multi-step logical deduction | 20 | Reasoning Quality, Accuracy |
| Causal inference questions | 15 | Reasoning Quality, Hallucination Rate |
| Scientific process explanation | 20 | Reasoning Quality, Clarity |

---

## Observed Reasoning Failure Modes

### 1. Premise Skipping

The model stated an intermediate conclusion without showing the supporting step.

**Example prompt:**
> A train travels 120 km in 2 hours. A car travels 180 km in 3 hours. Which is faster, and by how much?

**Problematic response excerpt:**
> The car is faster by 10 km/h.

**What was missing:** The model skipped the per-vehicle speed calculation (train: 60 km/h; car: 60 km/h). In fact, both are equal — the model hallucinated a difference. This illustrates how premise skipping can introduce factual errors alongside reasoning gaps.

**RQ Score: 0**

---

### 2. Correct Answer via Incorrect Path

The model arrived at the right answer but used unsound intermediate logic.

**Example prompt:**
> If all mammals are warm-blooded and all dogs are mammals, are all dogs warm-blooded?

**Problematic response excerpt:**
> Yes, because dogs are warm-blooded animals, and warm-blooded animals are mammals.

**What was missing:** The model inverted the conditional. The valid syllogism is: all mammals are warm-blooded → dogs are mammals → dogs are warm-blooded. The response stated it in reverse, which is a logical fallacy even though the conclusion happened to be correct.

**RQ Score: 1**

---

### 3. Over-Reliance on Pattern Matching

The model produced structurally correct reasoning that did not apply to the specific question.

**Example prompt:**
> A factory produces 400 units in 8 hours. How long would it take to produce 550 units at the same rate?

**Problematic response excerpt:**
> Using the rate formula: rate = units / time = 400/8 = 50 units/hour. Time = 550/50 = 10 hours. Answer: 10 hours.

This response is actually correct — however, when the same prompt type was slightly modified (changing conditions to require a rate change), the model applied the same formula template regardless, producing wrong results. This suggests the model is matching to a learned template rather than reasoning from first principles.

**RQ Score: 3 (but fragile — fails on variants)**

---

## Evaluation Results by Category

| Category | Avg RQ Score | Notes |
|---|---|---|
| Mathematical word problems | 1.9 | Premise skipping common |
| Multi-step logical deduction | 2.1 | Conditional inversion occurred in ~20% of responses |
| Causal inference questions | 1.6 | Confusion between correlation and causation |
| Scientific process explanation | 2.4 | Generally strong; gaps in edge cases |

---

## Chain-of-Thought Intervention

A subset of prompts was rerun with an explicit chain-of-thought instruction appended:

> Before giving your final answer, write out each reasoning step explicitly and number them.

**Results:**

| Category | Baseline Avg RQ | CoT Avg RQ | Improvement |
|---|---|---|---|
| Mathematical word problems | 1.9 | 2.6 | +0.7 |
| Multi-step logical deduction | 2.1 | 2.7 | +0.6 |
| Causal inference questions | 1.6 | 2.2 | +0.6 |
| Scientific process explanation | 2.4 | 2.8 | +0.4 |

Adding a chain-of-thought instruction consistently raised RQ scores across all categories. The gain was largest for prompt types where premise skipping was most common.

---

## Evaluation Insights

- **Premise skipping is the most impactful failure mode.** It affects both Reasoning Quality and Accuracy simultaneously because the model's internal shortcut often introduces a factual error.
- **Conditional inversion is subtle.** Evaluators must read the reasoning chain carefully — a response can sound sound while containing a logical inversion.
- **CoT scaffolding exposes latent reasoning.** In several cases, the explicit chain-of-thought revealed flawed intermediate steps even when the final answer was correct, enabling more accurate RQ scoring.
- **Pattern matching is hard to detect at scale.** It requires a systematic variant-testing approach to distinguish genuine reasoning from template retrieval.

---

## Recommendations

1. Score Reasoning Quality independently of Accuracy to catch cases where correct answers arise from incorrect logic.
2. Use chain-of-thought prompts in any evaluation where reasoning transparency is important.
3. Test prompt variants with modified numerical or conditional values to probe for template matching.
4. Document specific failure mode types (skipping, inversion, pattern matching) alongside numerical scores.
