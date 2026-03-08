# Tools

This directory contains runnable Python scripts for benchmarking, scoring, and analysis.

## Available Scripts

### `run_benchmark.py`

Loads a benchmark JSON file, runs each prompt against a model (or built-in mock), scores responses against the rubric, writes a JSON results artifact, and prints a concise summary.

**Usage:**

```bash
python tools/run_benchmark.py [OPTIONS]
```

**Options:**

| Option | Default | Description |
|---|---|---|
| `--benchmark FILE` | (required) | Path to benchmark JSON file |
| `--out FILE` | (required) | Path for the results JSON artifact |
| `--mode MODE` | `mock` | Runner mode: `mock` or `openai` |

**Modes:**

- **`mock`** — No API key required. Uses a built-in oracle that returns the correct answer derived from each item's rubric (numeric, contains, or exact). Good for CI and demos.
- **`openai`** — Calls an OpenAI-compatible chat completions endpoint. Requires environment variables:

  ```bash
  export OPENAI_BASE_URL=https://api.openai.com/v1
  export OPENAI_API_KEY=sk-...
  export OPENAI_MODEL=gpt-4o
  ```

**Examples:**

```bash
# Mock mode (default) — no credentials needed
python tools/run_benchmark.py \
  --benchmark benchmarks/reasoning/widgets.json \
  --out results/widgets_results.json

# OpenAI-compatible endpoint
OPENAI_BASE_URL=https://api.openai.com/v1 \
OPENAI_API_KEY=sk-... \
OPENAI_MODEL=gpt-4o \
python tools/run_benchmark.py \
  --benchmark benchmarks/reasoning/widgets.json \
  --out results/widgets_results.json \
  --mode openai
```

## Adding New Scripts

Place new scripts in this directory. Every script should:

1. Include a `#!/usr/bin/env python3` shebang.
2. Be documented with a module-level docstring explaining purpose and usage.
3. Be dependency-free (Python stdlib only) unless a dependency is unavoidable and documented here.
4. Print a concise summary to stdout on success.
