# Agent OS Evaluation Results

Evaluation results for prompt sets in `prompts/technical/agent_os.md`.

All prompt sets are scored on applicable dimensions using the 0–3 scale defined in [`../metrics.md`](../metrics.md). Aggregate scores use the formula from [`../framework.md`](../framework.md).

---

## Summary

| Prompt Set | Topic | Applicable Metrics | Notes |
|---|---|---|---|
| 1 | Core Purpose | AC, RQ, CL | Tests conceptual separation of Agent OS from agent applications |
| 2 | Layered Stack | AC, IF, CL | Tests recall and ordering of all twelve layers |
| 3 | Agent Kernel | AC, RQ, CL | Tests kernel module identification and OS analogy |
| 4 | Memory Horizon Types | AC, RQ, IF | Tests classification of five memory types |
| 5 | Memory Write and Read Paths | AC, RQ, CL | Tests sequential process understanding |
| 6 | Governance Tiers | AC, IF, RQ | Tests tier definitions and escalation logic |
| 7 | Governance Insertion Points | AC, RQ, CL | Tests policy enforcement placement rationale |
| 8 | Coordination Modes | AC, IF, RQ | Tests mode definitions and appropriate selection |
| 9 | Agent Types | AC, IF, CL | Tests identification of twelve agent classes |
| 10 | Scheduler Responsibilities | AC, RQ, IF | Tests scheduling mechanics and resource controls |
| 11 | Agent Identity and Permissions | AC, RQ, CL | Tests security model and threat mitigation |
| 12 | Self-Improving Agent OS | AC, RQ, IF | Tests improvement loop and governance boundaries |
| 13 | Canonical Data Records | AC, IF, CL | Tests data model field-level recall |
| 14 | Phased Build Plan | AC, RQ, IF | Tests phased implementation ordering and rationale |

---

## Scoring Reference

| Score | Meaning |
|---|---|
| 0 | Fails to meet the criterion |
| 1 | Partially meets the criterion |
| 2 | Mostly meets the criterion |
| 3 | Fully meets the criterion |

Aggregate per prompt set:

```
Aggregate = sum(applicable_metric_scores) / (number_of_applicable_metrics × 3) × 100%
```

---

## Notes on Evaluation

- **Accuracy** is particularly important for the governance tier and memory type prompts, where exact ordering or enumeration is expected.
- **Reasoning Quality** is weighted heavily for prompts 5, 7, and 12, which require process tracing and causal justification.
- **Instruction Following** is critical for list-style prompts (2, 4, 9, 13) where the model must enumerate all items in the expected answer.
- **Hallucination Rate** is implicitly tested across all prompts: any fabricated layer names, tier counts, or agent types not in the reference design are flagged.
- **Clarity** is evaluated on whether the model structures multi-part answers (e.g., write path vs. read path in Prompt Set 5) in a readable, well-organized way.
