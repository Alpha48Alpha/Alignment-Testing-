# 🧪 LLM Evaluation Lab

> **An AI Evaluation Research Dashboard** — experiments analyzing reasoning, instruction following, knowledge accuracy, and prompt robustness across large language models.

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Prompts](https://img.shields.io/badge/prompts-500%2B-green.svg)](#prompt-categories)
[![Consistency](https://img.shields.io/badge/consistency%20improvement-35%25-brightgreen.svg)](#results)

---

## 🎯 Purpose

This lab systematically evaluates LLM behavior using structured prompt suites, automated benchmarking tools, and reproducible scoring rubrics. The goal is to build a rigorous, recruiter-legible record of model alignment research: what models get right, where they fail, and how prompt design affects quality.

---

## 🔬 Current Experiments

| Experiment | Focus | Status |
|---|---|---|
| [Widget Reasoning](benchmarks/reasoning/widgets.json) | Multi-step object-counting and deduction | ✅ Active |
| Instruction Following Suite | Format, length, and constraint compliance | ✅ Active |
| Hallucination Probe | Fabricated facts in knowledge-dense prompts | 🔄 In Progress |
| Jailbreak Resistance | Safety policy adherence under adversarial prompts | ✅ Active |
| Prompt Injection Defense | Injected-instruction detection and rejection | ✅ Active |

---

## 📊 Benchmark Categories

- **Reasoning** — Multi-step deduction, object counting, spatial logic, and causal inference
- **Instruction Following** — Format adherence, length constraints, tone matching, audience targeting
- **Factual Accuracy** — Knowledge retrieval correctness across science, history, and technical domains
- **Hallucination Rate** — Unsupported claim frequency in knowledge-dense responses
- **Robustness** — Behavior consistency across prompt paraphrases and adversarial variants

---

## 📝 Example Benchmark Prompt

```json
{
  "id": "widgets-001",
  "prompt": "A factory produces widgets in batches. Each batch contains 12 widgets. If 5 batches are produced on Monday and 3 batches on Tuesday, how many widgets are produced in total?",
  "expected_answer": "96",
  "rubric": {
    "type": "numeric",
    "value": 96,
    "tolerance": 0
  }
}
```

Run this benchmark with:

```bash
python tools/run_benchmark.py \
  --benchmark benchmarks/reasoning/widgets.json \
  --out results/widgets_results.json
```

---

## 📏 Evaluation Metrics

Each response is scored **0–3** on each applicable metric:

| Metric | What it measures |
|---|---|
| **Accuracy** | Is the content factually correct and supported by reliable knowledge? |
| **Reasoning Quality** | Is the reasoning clear, coherent, and logically structured? |
| **Instruction Following** | Does the response respect all explicit constraints (format, length, tone)? |
| **Hallucination Rate** | Does the response avoid unsupported or fabricated claims? |
| **Clarity** | Is the response well-structured and readable for the intended audience? |

**Aggregate score:**

```
Aggregate = sum(applicable_metric_scores) / (num_applicable_metrics × 3) × 100%
```

See [`evaluations/metrics.md`](evaluations/metrics.md) for full per-metric rubrics.

---

## ⚙️ Tools

All benchmarking scripts live in [`tools/`](tools/README.md).

### `tools/run_benchmark.py`

Loads a benchmark JSON, runs prompts against a model (or a built-in mock), scores responses, writes a results artifact, and prints a summary.

**Quickstart (no API keys required — uses mock mode):**

```bash
python tools/run_benchmark.py \
  --benchmark benchmarks/reasoning/widgets.json \
  --out results/widgets_results.json
```

**Against an OpenAI-compatible endpoint:**

```bash
export OPENAI_BASE_URL=https://api.openai.com/v1
export OPENAI_API_KEY=sk-...
export OPENAI_MODEL=gpt-4o

python tools/run_benchmark.py \
  --benchmark benchmarks/reasoning/widgets.json \
  --out results/widgets_results.json \
  --mode openai
```

See [`tools/README.md`](tools/README.md) for full usage.

---

## 📁 Repository Structure

```
benchmarks/
  reasoning/        # Multi-step reasoning benchmark suites (JSON)
datasets/           # Curated prompt datasets and source notes
evaluations/
  metrics.md        # Per-metric scoring rubrics (0–3 scale)
  framework.md      # Full evaluation methodology
  results/          # Legacy evaluation result notes
experiments/        # Lab notebooks and experiment write-ups
prompt-attack-lab/
  jailbreak-tests.md        # Jailbreak test cases and expected safe behaviors
  prompt-injection-tests.md # Prompt injection attack cases
  defense-strategies.md     # Defense techniques and mitigations
prompts/
  technical/        # Technical domain prompts
  educational/      # Educational domain prompts
  general/          # General knowledge prompts
results/            # Benchmark results artifacts (JSON)
tools/              # Runnable benchmarking scripts
```

---

## 📈 Results

| Metric | Baseline | Improved | Delta |
|---|---|---|---|
| Response Consistency | ~52% | ~70% | **+35% relative improvement** |
| Widget Reasoning (mock) | — | See [`results/`](results/) | Latest run |

> Consistency is the percentage of prompt variant sets where all variants receive the same score. A 35% relative improvement means 35% more prompt sets achieved full consistency after iterative prompt refinement.

---

## 🚀 Quickstart

```bash
# Clone and run the benchmark in dependency-free mock mode
git clone https://github.com/Alpha48Alpha/Alignment-Testing-.git
cd Alignment-Testing-

python tools/run_benchmark.py \
  --benchmark benchmarks/reasoning/widgets.json \
  --out results/widgets_results.json
```
