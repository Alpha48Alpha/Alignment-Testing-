# Case Studies

This directory contains structured analyses of LLM behavior observed during evaluation runs. Each sub-directory focuses on a specific failure class or behavioral pattern.

---

## Contents

| Directory | Description |
|---|---|
| [`model-failure-analysis/`](model-failure-analysis/README.md) | Catalog of recurring model failure modes with examples and diagnostic notes |

---

## Purpose

Case studies in this repository serve three functions:

1. **Failure documentation** — Record specific failure instances that are informative beyond their individual occurrence, particularly when they reveal a systematic model weakness.
2. **Evaluation calibration** — Inform the design of evaluation rubrics and prompt sets by identifying where current metrics fail to capture real-world reliability issues.
3. **Mitigation tracking** — Document which prompt engineering interventions reduced a failure mode, and by how much.

---

## Related

- [`../evaluation-framework/README.md`](../evaluation-framework/README.md) — Scoring methodology and rubric
- [`../prompt-attack-lab/`](../prompt-attack-lab/) — Adversarial prompt testing
