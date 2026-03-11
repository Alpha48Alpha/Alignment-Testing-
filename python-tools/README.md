# Python Tools

**Purpose:** Lightweight Python scripts for prompt testing, response scoring, and result aggregation.

---

## Files

| File | Description |
|---|---|
| [`prompt_tester.py`](prompt_tester.py) | Run a prompt set against an OpenAI-compatible API and log responses |
| [`score_responses.py`](score_responses.py) | Score a set of logged responses against the five evaluation metrics |
| [`aggregate_results.py`](aggregate_results.py) | Compute per-domain and per-metric aggregate statistics from scored results |

---

## Requirements

```
openai>=1.0.0
```

Install with:
```bash
pip install openai
```

---

## Quick Start

```bash
# 1. Run prompts and save responses
python prompt_tester.py --input prompts.json --output responses.json --model gpt-4o

# 2. Score the responses (requires human annotation or a reference model)
python score_responses.py --input responses.json --output scores.json

# 3. Aggregate results
python aggregate_results.py --input scores.json
```

---

## Environment Variables

```
OPENAI_API_KEY   — Required for prompt_tester.py
```

Set with:
```bash
export OPENAI_API_KEY=your_key_here
```
