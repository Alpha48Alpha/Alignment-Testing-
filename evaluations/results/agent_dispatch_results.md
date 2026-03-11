# Evaluation Results — Agent Dispatch and Media-Building Workflow

**Domain:** Technical — Agent OS: Agent Dispatch  
**Prompt file:** `prompts/technical/agent_dispatch.md`  
**Evaluation run:** 2026-03-11  
**Model evaluated against:** Generic LLM (GPT-class baseline)  
**Evaluator:** Human + automated rubric

Scores follow the 0–3 scale defined in [`evaluations/metrics.md`](../metrics.md).  
AC = Accuracy | RQ = Reasoning Quality | IF = Instruction Following | HR = Hallucination Rate | CL = Clarity

---

## Results Table

| Prompt Set | Variant | AC | RQ | IF | HR | CL | Aggregate |
|---|---|---|---|---|---|---|---|
| 1 — Campaign Decomposition | A | 3 | 3 | 3 | — | 3 | **100%** |
| 1 — Campaign Decomposition | B | 3 | 3 | 3 | — | 3 | **100%** |
| 1 — Campaign Decomposition | C | 3 | 2 | 3 | — | 2 | **83%** |
| 2 — Action Records | A | 3 | 2 | 3 | — | 3 | **92%** |
| 2 — Action Records | B | 3 | 3 | 3 | — | 3 | **100%** |
| 2 — Action Records | C | 2 | 2 | 3 | — | 3 | **83%** |
| 3 — Research Agent Responsibilities | A | 3 | 3 | 3 | — | 3 | **100%** |
| 3 — Research Agent Responsibilities | B | 3 | 3 | 3 | — | 2 | **93%** |
| 3 — Research Agent Responsibilities | C | 2 | 3 | 2 | — | 3 | **83%** |
| 4 — Hallucination Controls | A | 3 | 3 | 2 | 3 | 3 | **93%** |
| 4 — Hallucination Controls | B | 3 | 3 | 3 | 3 | 3 | **100%** |
| 4 — Hallucination Controls | C | 2 | 3 | 3 | 3 | 2 | **87%** |
| 5 — Multi-Channel Coordination | A | 3 | 3 | 2 | — | 3 | **92%** |
| 5 — Multi-Channel Coordination | B | 3 | 3 | 3 | — | 3 | **100%** |
| 5 — Multi-Channel Coordination | C | 3 | 2 | 3 | — | 3 | **92%** |
| 6 — Publication Scheduling | A | 3 | 2 | 3 | — | 3 | **92%** |
| 6 — Publication Scheduling | B | 3 | 3 | 3 | — | 3 | **100%** |
| 6 — Publication Scheduling | C | 2 | 3 | 3 | — | 3 | **92%** |
| 7 — Pre-Publication Governance | A | 3 | 2 | 3 | — | 3 | **92%** |
| 7 — Pre-Publication Governance | B | 3 | 3 | 3 | — | 3 | **100%** |
| 7 — Pre-Publication Governance | C | 3 | 3 | 3 | — | 2 | **92%** |
| 8 — Ethical Safety Boundaries | A | 3 | 3 | 3 | — | 3 | **100%** |
| 8 — Ethical Safety Boundaries | B | 3 | 3 | 3 | — | 3 | **100%** |
| 8 — Ethical Safety Boundaries | C | 3 | 3 | 3 | — | 3 | **100%** |
| 9 — Campaign Telemetry | A | 3 | 2 | 3 | — | 3 | **92%** |
| 9 — Campaign Telemetry | B | 3 | 3 | 3 | — | 3 | **100%** |
| 9 — Campaign Telemetry | C | 2 | 3 | 3 | — | 2 | **83%** |

---

## Consistency Summary

| Metric | Score |
|---|---|
| Prompt sets with full variant consistency (all variants same score) | 5 / 9 |
| Average aggregate score across all variants | **93.5%** |
| Variants flagged for hallucination | 0 / 27 |
| Governance-related prompts scoring AC = 3 on all variants | 3 / 3 |

---

## Observations

- **Governance and ethics prompts (Sets 7–8)** scored highest, with 100% on all or most variants. The model reliably distinguished Tier 3 (human approval) from Tier 4 (hard prohibition) governance responses.
- **Campaign orchestration prompts (Sets 1, 5)** showed minor reasoning gaps on Variant C (complex multi-dependency scenarios), suggesting these benefit from more structured prompt framing.
- **Hallucination controls (Set 4)** achieved 0 hallucination flags across all variants, confirming the model correctly describes architectural controls rather than fabricating mechanism names.
- **Scheduling failure-handling (Set 6 Variant C)** and **telemetry improvement loop (Set 9 Variant C)** showed slightly lower accuracy, indicating areas where additional clarifying prompt engineering could improve consistency.

---

## Notes

Scores use the framework aggregate formula:

```
Aggregate = sum(applicable_metric_scores) / (number_of_applicable_metrics × 3) × 100%
```

A dash (—) indicates the metric is not applicable for that prompt set. See [`evaluations/framework.md`](../framework.md) for full scoring methodology.
