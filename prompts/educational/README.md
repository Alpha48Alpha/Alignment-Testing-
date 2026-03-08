# Educational Prompts

LLM evaluation prompts for educational domains — science, history, language, and conceptual explanations.

## Contents

| File | Metric | Description |
|---|---|---|
| [`accuracy.md`](accuracy.md) | Accuracy | Prompts testing factual correctness across science, history, and language |

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
