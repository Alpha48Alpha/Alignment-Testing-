# Benchmark Results

This folder stores scored results produced by `tools/run_benchmark.py`.

Each run generates a timestamped CSV file with the following columns:

| Column | Description |
|---|---|
| `id` | Prompt identifier |
| `category` | Benchmark category |
| `prompt` | Prompt text |
| `response` | Model response text |
| `accuracy` | Score 0–3 |
| `reasoning_quality` | Score 0–3 |
| `instruction_following` | Score 0–3 |
| `hallucination_rate` | Score 0–3 |
| `clarity` | Score 0–3 |
| `aggregate` | Aggregate percentage score |

Run the benchmark to generate results:

```bash
python tools/run_benchmark.py
```
