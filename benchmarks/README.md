# Benchmarks

This directory contains structured benchmark suites used by the automated scoring tools in [`tools/`](../tools/README.md).

## Format

Each benchmark is a JSON file containing an array of items. Every item must include:

```json
{
  "id": "unique-string-id",
  "prompt": "The prompt text sent to the model.",
  "expected_answer": "The correct answer (string).",
  "rubric": {
    "type": "numeric | contains | exact",
    "value": "<expected value>",
    "tolerance": 0
  }
}
```

### Rubric Types

| Type | Behavior |
|---|---|
| `numeric` | Parses the first number in the model response and compares to `value` within `tolerance` |
| `contains` | Checks whether `value` appears (case-insensitive) anywhere in the response |
| `exact` | Requires the response to exactly equal `value` (case-insensitive, trimmed) |

## Directory Layout

```
benchmarks/
  reasoning/        # Multi-step deduction, counting, causal inference
  instruction/      # Format, length, and constraint compliance checks
  factual/          # Knowledge retrieval and accuracy probes
  robustness/       # Paraphrase consistency and adversarial variants
```

## Running a Benchmark

```bash
python tools/run_benchmark.py \
  --benchmark benchmarks/reasoning/widgets.json \
  --out results/widgets_results.json
```

See [`tools/README.md`](../tools/README.md) for full CLI options.
