# General Knowledge Prompts

LLM evaluation prompts for general knowledge domains — everyday reasoning, common sense, and world knowledge.

## Contents

| File | Metric | Description |
|---|---|---|
| [`clarity.md`](clarity.md) | Clarity | Prompts evaluating readability, structure, and audience-appropriate explanation |

## Prompt Format

Each file contains one or more **Prompt Sets**. Every set includes:

- A **Prompt** (and **Variants** where applicable) — equivalent rephrasings of the same question
- An **Expected answer** or **Reference answer** — the ground-truth or reference response
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
