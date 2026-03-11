# Alignment-Testing-
### A structured prompt library for evaluating LLM safety, robustness, and response quality.

---

## What This Repository Does

This repository contains **500+ prompts** spanning technical, educational, and general knowledge domains. Each prompt is designed to expose measurable differences in model behavior across five evaluation dimensions: factual accuracy, reasoning quality, instruction following, hallucination resistance, and response clarity.

Iterative refinement of prompt wording reduced ambiguity and increased grounding, producing a **35% relative improvement in cross-variant consistency** (from ~52% to ~70% of prompt sets scoring uniformly across all rephrasings).

---

## Prompt Domains

| Domain | Focus Areas |
|---|---|
| Technical | Programming, mathematics, algorithmic reasoning, code review |
| Educational | Physics, biology, history, grammar, and conceptual explanation |
| General Knowledge | Everyday reasoning, analogy, ambiguity, and world geography |

---

## Five-Metric Evaluation Framework

Each response is scored 0–3 on every applicable dimension. See [`evaluations/metrics.md`](evaluations/metrics.md) for scoring rubrics and [`evaluations/framework.md`](evaluations/framework.md) for aggregate scoring methodology.

| Dimension | Abbreviation | What It Tests |
|---|---|---|
| Accuracy | AC | Factual correctness against verifiable knowledge sources |
| Reasoning Quality | RQ | Logical coherence and soundness of intermediate steps |
| Instruction Following | IF | Adherence to explicit output constraints (format, length, tone, role) |
| Hallucination Rate | HR | Absence of unsupported or fabricated claims |
| Clarity | CL | Readability and audience-appropriateness of the response |

---

## Consistency Results

| Metric | Baseline | After Refinement | Relative Change |
|---|---|---|---|
| Cross-variant consistency | ~52% | ~70% | **+35%** |

> **How consistency is measured:** Each prompt set contains 2–3 rephrasings of the same question. Consistency is the percentage of sets where all variants receive identical scores. Improvement was achieved by reducing ambiguous wording, adding explicit grounding context, and specifying output constraints.

---

## Repository Structure

```
prompts/
  technical/        # Reasoning, code, and constraint-following prompts
  educational/      # Science, history, and language accuracy prompts
  general/          # Clarity and world-knowledge prompts
evaluations/
  metrics.md        # Per-metric scoring rubrics (0–3 scale)
  framework.md      # Aggregate scoring formula and consistency methodology
  results/          # Per-domain evaluation summaries
prompt-attack-lab/
  jailbreak-tests.md        # Adversarial prompts testing safety policy resistance
  prompt-injection-tests.md # Injection attacks and expected model behavior
  defense-strategies.md     # Concrete mitigations with implementation guidance
```
