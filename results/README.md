# Results

This directory stores benchmark results artifacts produced by the scoring tools.

## Artifact Format

Each results file is a JSON object written by `tools/run_benchmark.py`:

```json
{
  "benchmark": "benchmarks/reasoning/widgets.json",
  "mode": "mock",
  "model": "mock",
  "timestamp": "2025-01-15T12:00:00Z",
  "summary": {
    "total": 5,
    "passed": 4,
    "failed": 1,
    "score_pct": 80.0
  },
  "items": [
    {
      "id": "widgets-001",
      "prompt": "...",
      "response": "...",
      "expected": "96",
      "pass": true,
      "rubric_type": "numeric"
    }
  ]
}
```

## Naming Convention

Results files are named after the benchmark slug, optionally with a timestamp suffix:

```
results/
  widgets_results.json            # Latest run of the widgets benchmark
  widgets_results_20250115.json   # Archived run with date stamp
```

## Tracking Policy

- Committed results files serve as reproducible reference artifacts.
- Auto-generated dated archives may be gitignored; see the root `.gitignore`.
- At least one sample results file per benchmark should be committed to demonstrate expected output.
