# Media Engine Evaluation Results

Evaluation results for prompt sets in `prompts/technical/media_engine.md`.

All prompt sets are scored on applicable dimensions using the 0–3 scale defined in [`../metrics.md`](../metrics.md). Aggregate scores use the formula from [`../framework.md`](../framework.md).

---

## Summary

| Prompt Set | Topic                          | Applicable Metrics | Notes                                                        |
|---|---|---|---|
| 1          | Core Purpose and Layers        | AC, RQ, CL         | Tests four-layer architecture recall and data-flow understanding |
| 2          | Supported Media Formats        | AC, IF, CL         | Tests format enumeration across image/audio/video categories  |
| 3          | MediaObject Fields             | AC, IF, HR         | Tests data-model field-level recall and deduplication logic   |
| 4          | Ingestion Intake Modes         | AC, RQ, IF         | Tests mode selection and error-path reasoning                 |
| 5          | Pipeline Operations            | AC, RQ, CL         | Tests operation enumeration and custom registration           |
| 6          | ProcessingResult Fields        | AC, RQ, IF         | Tests result model recall and diagnostic reasoning            |
| 7          | Analyser Routing               | AC, RQ, CL         | Tests facade pattern understanding and routing logic          |
| 8          | Production ML Integration      | AC, RQ, IF         | Tests stub-override pattern and trade-off analysis            |
| 9          | REST API Endpoints             | AC, IF, CL         | Tests endpoint enumeration and HTTP error codes               |
| 10         | Monetisation Architecture      | AC, RQ, CL         | Tests billing primitives and multi-instance scaling concerns  |
| 11         | Agent OS Layer 8 Integration   | AC, RQ, CL         | Tests cross-system integration rationale and data flow        |

---

## Scoring Reference

| Score | Meaning                        |
|---|---|
| 0     | Fails to meet the criterion    |
| 1     | Partially meets the criterion  |
| 2     | Mostly meets the criterion     |
| 3     | Fully meets the criterion      |

Aggregate per prompt set:

```
Aggregate = sum(applicable_metric_scores) / (number_of_applicable_metrics × 3) × 100%
```

---

## Notes on Evaluation

- **Accuracy** is critical for all prompt sets that enumerate specific field names, format lists, or endpoint paths where the expected answer is precisely defined (sets 1–5, 9).
- **Reasoning Quality** is weighted heavily for sets 4, 7, 8, 10, and 11, which require causal or design-level justification (e.g. why Layer 8 is the correct integration point).
- **Instruction Following** is critical for list-style prompts (2, 3, 5, 9) where the model must enumerate all items in the expected answer without omission.
- **Hallucination Rate** is implicitly tested across all prompts: fabricated field names, invented operation names, or non-existent API endpoints not defined in the Media Engine design are flagged as hallucinations.
- **Clarity** is evaluated on whether the model organises multi-part answers (e.g. per-layer descriptions in set 1, per-mode comparisons in set 4) in a readable, well-structured way.
