# Python Tools

Simple Python utilities for running prompt evaluation workflows. These tools are designed to be readable and self-contained — they demonstrate evaluation patterns rather than providing a production-ready framework.

All tools require Python 3.9 or later. No external dependencies are needed unless you supply an API key for live LLM calls.

---

## Files

| File | Description |
|---|---|
| [`prompt_tester.py`](prompt_tester.py) | Run a prompt set against a list of variants and collect responses |
| [`evaluator.py`](evaluator.py) | Score collected responses on the five evaluation metrics |
| [`consistency_check.py`](consistency_check.py) | Compute consistency scores across prompt variants |
| [`hallucination_detector.py`](hallucination_detector.py) | Flag suspicious factual claims for human review |

---

## Usage

### Running the prompt tester

```bash
python3 prompt_tester.py
```

The script runs a built-in demo that does not require an API key. To use it with a real LLM API, set the `OPENAI_API_KEY` environment variable and pass your prompt set as a list of strings.

### Running the evaluator

```bash
python3 evaluator.py
```

Scores a set of example responses against each of the five evaluation dimensions. Outputs a per-response score table and an aggregate consistency rate.

---

## Design Notes

These tools are intentionally minimal. They make the evaluation logic explicit so that the scoring criteria can be reviewed, critiqued, and modified. A production evaluation pipeline would add database storage, parallelism, and a proper API client wrapper, but those additions would obscure the core evaluation logic.

The scoring functions in `evaluator.py` implement the rubric defined in [`../evaluation-framework/README.md`](../evaluation-framework/README.md).
