# Technical Prompts

LLM evaluation prompts for technical domains — programming, mathematics, logic puzzles, and system reasoning.

## Contents

| File | Metric | Description |
|---|---|---|
| [`reasoning_quality.md`](reasoning_quality.md) | Reasoning Quality | Logic, math, and code-reasoning prompt sets |
| [`hallucination_rate.md`](hallucination_rate.md) | Hallucination Rate | Prompts designed to surface fabricated or unsupported claims |
| [`instruction_following.md`](instruction_following.md) | Instruction Following | Prompts with explicit format, length, and role constraints |

## Prompt Format

Each file contains one or more **Prompt Sets**. Every set includes:

- Multiple **Variants** (A, B, C) — equivalent rephrasings of the same question
- An **Expected answer** — the ground-truth or reference response
- **Evaluation criteria** — the applicable metrics from the five-metric framework

## Evaluation Metrics

Prompts are scored 0–3 on each applicable metric:

| Metric | Abbreviation |
|---|---|
| Accuracy | AC |
| Reasoning Quality | RQ |
| Instruction Following | IF |
| Hallucination Rate | HR |
| Clarity | CL |

See the [evaluation framework](../../evaluations/framework.md) for full scoring guidance.
