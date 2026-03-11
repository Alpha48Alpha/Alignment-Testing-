# Evaluation Framework — Quality Metrics

## Overview

This document provides an extended reference for the quality metrics used in this repository's LLM evaluation framework. It covers the theoretical rationale behind each metric, detailed scoring guidance with annotated examples, and inter-metric relationships. For the foundational definitions, see `evaluations/metrics.md`.

---

## Metric 1: Accuracy (AC)

### Rationale

Accuracy is the foundational quality dimension. A response that is well-reasoned, clearly written, and fully instruction-compliant is still harmful if its core content is factually wrong. Accuracy is scored first to avoid contaminating other dimension scores with the halo effect of confident, fluent prose.

### Extended Scoring Guidance

| Score | Criteria | Example |
|---|---|---|
| 3 | All factual claims are correct and well-supported | "Python was created by Guido van Rossum and first released in 1991." — Both claims verifiable and correct. |
| 2 | Core answer is correct; one or two minor inaccuracies in supporting details | "Python was created by Guido van Rossum in 1989." — Creator correct; year off by 2. |
| 1 | Core answer is partially correct; significant supporting detail errors | "Python was created in 1989 as a scripting language for system administration." — Year wrong; creation purpose inaccurate. |
| 0 | Core answer is factually wrong | "Python was created by Larry Wall in 1994." — Both creator and year incorrect. |

### Scoring Notes

- Do not penalize for omission unless the omission makes a stated claim inaccurate.
- Hedged claims ("Python is generally considered...") are not penalized for being incomplete — only for being demonstrably false.

---

## Metric 2: Reasoning Quality (RQ)

### Rationale

Reasoning Quality measures the transparency and soundness of the model's inference process. A model that consistently reaches correct answers without showing valid reasoning is unreliable in novel contexts. RQ scoring requires reading the full response, not just the conclusion.

### Extended Scoring Guidance

| Score | Criteria | Example |
|---|---|---|
| 3 | All intermediate steps present, logically sound, and lead correctly to conclusion | Step-by-step binary search complexity derivation arriving at O(log n) via correct halving logic. |
| 2 | Reasoning mostly present and sound; one minor logical gap or unclear step | Correct derivation but one step skips an arithmetic operation without explanation. |
| 1 | Reasoning present but contains a significant logical error, inversion, or false analogy | Correct conclusion via inverted conditional ("since dogs are warm-blooded, they must be mammals"). |
| 0 | No reasoning shown, or reasoning is circular, incoherent, or leads to wrong conclusion | "The answer is 42." — No steps; or circular: "X is true because X." |

### Scoring Notes

- Correct final answer via incorrect reasoning scores 1 or below — not 3.
- A partially complete chain that covers most steps scores 2.
- Template matching (producing correct-pattern reasoning that doesn't apply to this specific question) scores 1.

---

## Metric 3: Instruction Following (IF)

### Rationale

Instruction Following measures compliance with explicit constraints in the prompt. This is the metric most directly tied to practical utility — in production settings, a response that violates format or scope constraints cannot be used even if its content is correct.

### Extended Scoring Guidance

| Score | Criteria | Example |
|---|---|---|
| 3 | All explicit constraints fully respected | Prompt: "List 3 items in bullet format." Response: Exactly 3 bullet points, no preamble. |
| 2 | All constraints mostly respected; one minor deviation | Prompt: "3 items in bullet format." Response: 3 bullets plus one-sentence introduction. |
| 1 | Most constraints respected; one constraint clearly violated | Prompt: "3 items in bullet format, under 50 words." Response: 3 bullets, 80 words. |
| 0 | One or more major constraints ignored | Prompt: "3 items in bullet format." Response: Prose paragraph with no list structure. |

### Scoring Notes

- Each violated constraint reduces the score by 1 point from 3. Multiple minor violations can compound to a low score.
- Constraint addition (adding unsolicited content) counts as a deviation but is typically less severe than constraint omission.
- Implicit constraints (inferred from context) are not scored under IF — only explicitly stated constraints.

---

## Metric 4: Hallucination Rate (HR)

### Rationale

Hallucination Rate tracks the production of unsupported or fabricated claims. Unlike Accuracy, which measures whether stated claims are correct, HR specifically targets claims that appear to be factual assertions but lack grounding in reliable knowledge.

### Extended Scoring Guidance (Quality Score — Higher is Better)

| Score | Criteria | Example |
|---|---|---|
| 3 | No unsupported claims | All specific facts in the response are verifiable against authoritative sources. |
| 2 | One minor unsupported claim | Response includes one statistic ("approximately 70% of...") that cannot be verified but is plausible. |
| 1 | Multiple unsupported claims, or one significant fabrication | Cites a specific paper that does not exist, or gives an incorrect but confidently stated date. |
| 0 | Response is substantially hallucinated | Core claims are fabricated; the response creates a false impression of factual grounding. |

### Scoring Notes

- Fabricated citations (author names, paper titles, journal names that do not exist) score 0–1 regardless of the surrounding content's accuracy.
- Hedged statements ("may," "some suggest," "is often thought to") are treated as lower-confidence claims and are given more latitude than unhedged assertions.
- Post-training-cutoff claims should be flagged but may warrant special handling if they are explicitly labeled as estimates.

---

## Metric 5: Clarity (CL)

### Rationale

Clarity measures whether the response communicates effectively to the intended audience. A factually correct, well-reasoned response that is incomprehensible to its target audience fails to achieve its purpose. Clarity is always scored relative to the audience specified or implied by the prompt.

### Extended Scoring Guidance

| Score | Criteria | Example |
|---|---|---|
| 3 | Exceptionally clear; well-structured; audience-appropriate throughout | Photosynthesis explained to a middle schooler using accessible language, a clear structure, and no unexplained jargon. |
| 2 | Mostly clear and well-structured; minor issues (occasional jargon, slightly unclear transition) | Same explanation with one unexplained technical term that a reader could infer from context. |
| 1 | Somewhat readable but notable clarity issues (poor structure, significant jargon mismatches) | Explanation using chemistry notation and reaction equations without introduction, for a general-public audience. |
| 0 | Unclear, poorly structured, or fundamentally inappropriate for the target audience | Dense technical prose on a topic the prompt specified should be explained to a 10-year-old. |

### Scoring Notes

- Clarity is audience-relative. Expert-level language for an expert audience scores 3; the same language for a general-public audience scores lower.
- Excessive length without proportional information value is a clarity issue (scores 2 or lower).
- Responses that are too brief and omit essential context also score lower on Clarity.

---

## Inter-Metric Relationships

Understanding how metrics interact prevents double-penalizing or double-counting failures:

| Scenario | Correct Scoring |
|---|---|
| Factually wrong response, clearly written | AC: 0, CL: 3 — penalize once (AC) for the error |
| Correct answer, no reasoning shown | AC: 3, RQ: 0 — penalize once (RQ) for absent reasoning |
| All facts correct but hallucinated citation | HR: 1, AC: 3 — HR captures the unsupported citation; AC captures factual content |
| Correct content, wrong format | AC/RQ/HR scored on content; IF captures the format failure |
| Completely refused (should not have been) | AC: 0, IF: 0, CL: 0; HR: 3 (no claims made) |

---

## Metric Coverage by Prompt Type

| Prompt Type | AC | RQ | IF | HR | CL |
|---|---|---|---|---|---|
| Factual recall | ✓ | — | ✓ | ✓ | ✓ |
| Multi-step reasoning | ✓ | ✓ | ✓ | ✓ | ✓ |
| Instruction-constrained task | — | — | ✓ | — | ✓ |
| Safety / refusal evaluation | — | — | ✓ | ✓ | — |
| Creative generation | — | — | ✓ | — | ✓ |

When a metric is not applicable to a prompt type, it is excluded from the aggregate denominator per the formula in `evaluations/metrics.md`.
