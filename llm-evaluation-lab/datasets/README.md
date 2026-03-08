# Datasets

This folder contains prompt datasets used in evaluations.

## Format

Datasets are stored as JSON arrays. Each entry should follow this schema:

```json
{
  "id": "reasoning_001",
  "category": "Reasoning",
  "prompt": "...",
  "expected_answer": "...",
  "evaluation_goal": "..."
}
```

Pass a dataset file to the benchmark runner with:

```bash
python tools/run_benchmark.py --dataset datasets/my_dataset.json
```
