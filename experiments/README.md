# Experiments

This directory contains lab notebooks and write-ups for individual evaluation experiments.

## Expected Structure

Each experiment lives in its own subdirectory named by date and slug:

```
experiments/
  YYYY-MM-DD-<slug>/
    README.md        # Hypothesis, method, findings, and conclusions
    prompts.md       # Prompt variants used in this experiment (optional)
    results.md       # Observed model responses and scores (optional)
```

## Experiment Note Format

Each `README.md` inside an experiment folder should include:

| Section | Description |
|---|---|
| **Hypothesis** | What behavior or property is being tested |
| **Method** | Prompt design approach and evaluation procedure |
| **Models Tested** | Which models were evaluated (and versions if known) |
| **Findings** | Observed results and scores |
| **Conclusions** | What the results imply about model alignment or capability |

## Naming Convention

Use ISO date prefix + descriptive slug, e.g.:

- `2025-01-15-widget-counting-deduction/`
- `2025-02-03-instruction-format-compliance/`
- `2025-03-01-hallucination-probe-science/`
