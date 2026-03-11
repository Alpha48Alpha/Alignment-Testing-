# LLM Evaluation Lab

A structured repository for evaluating language model behavior across safety, reasoning, alignment, and robustness dimensions. Built to support systematic prompt engineering, model failure analysis, and benchmark design.

---

## What This Repository Does

This lab documents hands-on evaluation work across the following areas:

| Area | Description |
|---|---|
| **Alignment Testing** | Probing model adherence to intended behavior under instruction conflicts and edge cases |
| **Prompt Attack Lab** | Adversarial prompts testing jailbreak resistance, injection robustness, and policy bypass |
| **Model Failure Analysis** | Structured documentation of failure modes: hallucination, refusal errors, sycophancy, specification gaming |
| **Benchmark Design** | Methodology for constructing evaluation sets with controlled difficulty, variant parity, and measurable metrics |
| **Evaluation Framework** | Scoring rubric and aggregation methodology applied consistently across 500+ prompts |
| **Experiments** | Logged experiment runs tracking model behavior across conditions |
| **Case Studies** | Detailed analyses of specific evaluation findings |
| **Python Tools** | Lightweight scripts for prompt testing, scoring, and result aggregation |

---

## Repository Structure

```
case-studies/               # Deep-dive analyses of specific evaluation findings
model-failure-analysis/     # Failure taxonomies and documented failure patterns
alignment-tests/            # Structured tests for alignment and behavior compliance
llm-benchmark-design/       # Notes on benchmark construction and evaluation design
prompt-attack-lab/          # Adversarial prompts: jailbreaks, injections, defense strategies
evaluation-framework/       # Scoring rubric, metric definitions, and methodology
experiments/                # Logged evaluation runs with conditions and results
python-tools/               # Python scripts for prompt testing and score aggregation
prompts/                    # Prompt sets organized by domain and metric
  technical/
  educational/
  general/
evaluations/                # Legacy evaluation files and result summaries
```

---

## Evaluation Metrics

Each prompt response is scored 0–3 on each applicable dimension:

| Metric | Abbreviation | What it measures |
|---|---|---|
| Accuracy | AC | Factual correctness |
| Reasoning Quality | RQ | Logical coherence of reasoning steps |
| Instruction Following | IF | Adherence to explicit constraints |
| Hallucination Rate | HR | Frequency of unsupported claims (inverted: 3 = none) |
| Clarity | CL | Readability and explanation quality |

**Aggregate score:**
```
Aggregate = sum(applicable_metric_scores) / (applicable_dimensions × 3) × 100%
```

Full definitions: [`evaluation-framework/metrics.md`](evaluation-framework/metrics.md)  
Scoring methodology: [`evaluation-framework/scoring-rubric.md`](evaluation-framework/scoring-rubric.md)

---

## Key Findings

| Observation | Detail |
|---|---|
| Hallucination risk is highest in citation-heavy prompts | Models fabricate author names and publication years even when factual context is available |
| Roleplay framing consistently degrades safety boundary adherence | Models that refused direct jailbreak attempts complied when the same request was wrapped in fiction |
| Variant parity exposes prompt sensitivity | Score variance ≥1.0 across semantically equivalent variants indicates over-fitting to surface form |
| Instruction-following degrades under multi-constraint prompts | Compliance rate drops when prompts specify 3+ simultaneous format constraints |

---

## Prompt Corpus

500+ prompts across three domains:

| Domain | Focus |
|---|---|
| Technical | Programming, mathematics, algorithmic reasoning, code interpretation |
| Educational | Science, history, language, conceptual explanation |
| General Knowledge | Common sense, analogical reasoning, world knowledge |

Baseline consistency (before prompt refinement): ~52%  
After iterative refinement: ~70%  
Relative improvement: **+35%**

---

## Navigation

- [`alignment-tests/`](alignment-tests/) — Behavior compliance and safety boundary tests
- [`prompt-attack-lab/`](prompt-attack-lab/) — Adversarial prompt test cases and defenses
- [`model-failure-analysis/`](model-failure-analysis/) — Documented failure patterns with examples
- [`llm-benchmark-design/`](llm-benchmark-design/) — Benchmark construction methodology
- [`evaluation-framework/`](evaluation-framework/) — Metrics, rubric, and scoring approach
- [`experiments/`](experiments/) — Logged evaluation runs
- [`case-studies/`](case-studies/) — Specific analysis write-ups
- [`python-tools/`](python-tools/) — Scoring and testing utilities
