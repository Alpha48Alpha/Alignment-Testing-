# LLM Evaluation Lab

A collection of experiments analyzing how large language models reason, follow instructions, and generate knowledge.

This repository documents evaluation experiments, benchmark tests, and failure pattern analysis.

---

## Current Experiments

| Experiment | Focus | Status |
|---|---|---|
| Prompt Structure Test | Prompt optimization | Complete |
| Reasoning Benchmark | Logical reasoning accuracy | In progress |
| Hallucination Analysis | Knowledge reliability | Ongoing |

---

## Benchmark Categories

- Reasoning Tests
- Instruction Following Tests
- Knowledge Accuracy Tests
- Prompt Robustness Tests

---

## Example Benchmark Prompt

**Prompt**

> If five machines take five minutes to make five widgets, how long would 100 machines take to make 100 widgets?

**Correct Answer**

5 minutes

**Evaluation Goal**

Test logical reasoning consistency.

---

## Evaluation Metrics

- Accuracy
- Reasoning Quality
- Instruction Following
- Hallucination Rate
- Response Clarity

---

## Repository Structure

```
llm-evaluation-lab/
  experiments/    # Experiment logs and notes
  benchmarks/     # Benchmark prompt sets and definitions
  results/        # Scored results and analysis outputs
  datasets/       # Prompt datasets used in evaluations
  tools/          # Python scripts for running and scoring benchmarks
```

---

## Tools

Python scripts in the `tools/` folder demonstrate how prompts can be tested programmatically.

Run the benchmark tool:

```bash
python tools/run_benchmark.py
```

See [`tools/run_benchmark.py`](tools/run_benchmark.py) for the full implementation.

---

## Topics

`llm` · `prompt-engineering` · `ai-evaluation` · `ai-safety` · `machine-learning`
