# LLM Alignment & Evaluation Testing

**Elizabeth Rothschild**
AI Evaluation Specialist | Prompt Engineer | LLM Research Writer

---

## About This Repository

This repository documents systematic work in LLM evaluation and alignment testing. It contains structured prompt sets, scoring rubrics, adversarial test cases, and evaluation results covering three domains: technical reasoning, educational content, and general knowledge. The goal is to provide a reproducible framework for measuring and improving model behavior across well-defined metrics.

---

## Focus Areas

- **Prompt Engineering** — Designing prompt variants that isolate specific behaviors and expose inconsistencies in model outputs.
- **Alignment Testing** — Evaluating model responses against safety, accuracy, and instruction-following criteria.
- **Hallucination Detection** — Identifying and documenting patterns where models produce unsupported or fabricated claims.
- **Adversarial Robustness** — Testing model resistance to jailbreak attempts and prompt injection attacks.
- **Evaluation Methodology** — Building scoring rubrics and measurement frameworks that produce consistent, reproducible results.

---

## Repository Structure

```
prompts/
  technical/        # Programming, mathematics, logic, and system reasoning prompts
  educational/      # Science, history, language, and conceptual explanation prompts
  general/          # Everyday reasoning, common sense, and world knowledge prompts
evaluations/
  metrics.md        # Definitions for all 5 LLM evaluation metrics
  framework.md      # Scoring rubric and full evaluation methodology
  results/          # Evaluation results and analysis
prompt-attack-lab/
  jailbreak-tests.md        # Jailbreak prompt test cases and expected safe behaviors
  prompt-injection-tests.md # Prompt injection attack test cases
  defense-strategies.md     # Recommended mitigations and defense strategies
```

---

## Selected Project Highlights

**Prompt Variant Consistency Testing**
Each prompt set includes multiple rephrasings of the same question (Variants A, B, C). Variants are scored independently and then compared to measure whether the model produces consistent quality regardless of surface-level phrasing. This methodology surfaces fragile behaviors that single-prompt testing misses.

**Adversarial Prompt Lab**
The `prompt-attack-lab/` directory contains structured test cases for jailbreak attempts and prompt injection attacks, each paired with an evaluation goal and the expected safe model behavior. Defense strategies are documented alongside the attack patterns.

**Five-Metric Evaluation Framework**
All prompts are scored against five metrics — Accuracy, Reasoning Quality, Instruction Following, Hallucination Rate, and Clarity — using a 0–3 scale per metric. Aggregate scores are calculated as a percentage of maximum possible points, enabling cross-domain comparison.

---

## Background

This project grew out of a need for structured, repeatable LLM evaluation rather than ad hoc testing. Over the course of this work, I designed and evaluated **500+ prompts** across three domains — technical reasoning, educational content, and general knowledge. Iterative prompt refinement based on scoring results led to a **35% improvement in response consistency** — measured as the share of prompt variant sets where all variants received equivalent scores. Methodology details are in [`evaluations/framework.md`](evaluations/framework.md).

---

## Current Focus

- Expanding the adversarial test suite with more nuanced injection patterns
- Improving cross-domain consistency metrics and scoring tooling
- Documenting failure modes specific to instruction-following under constraint stacking
- Exploring lightweight automated scoring approaches for large prompt batches

---

## Contact

Elizabeth Rothschild
hecallsmequeen1@gmail.com
