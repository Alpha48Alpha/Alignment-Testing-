# Experiments

**Purpose:** Log of evaluation runs, recording conditions, models tested, and results.

---

## Log Index

| ID | Date | Model | Prompt Set | Key Finding |
|---|---|---|---|---|
| [EXP-001](exp-001-hallucination-citation.md) | 2024-11 | GPT-4o | Technical / Hallucination Rate | 60% of citation prompts produced at least one unverifiable reference |
| [EXP-002](exp-002-instruction-following-constraints.md) | 2024-11 | GPT-4o | Technical / Instruction Following | Compliance rate drops from ~95% at 1 constraint to ~54% at 4 constraints |
| [EXP-003](exp-003-roleplay-safety-boundaries.md) | 2024-12 | GPT-4o | Alignment / Behavioral Boundaries | 3 of 8 jailbreak variants bypassed safety boundaries under roleplay framing |

---

## Experiment Format

Each experiment file records:

- **Objective** — What question is being answered
- **Model and version** — Exact model identifier used
- **Prompt set** — Which prompts were run
- **Conditions** — Temperature, system prompt, number of runs
- **Results** — Per-metric scores and aggregate
- **Observations** — Notable behaviors beyond the scores
- **Conclusion** — What the results imply
