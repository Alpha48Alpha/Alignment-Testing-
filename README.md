# LLM Alignment & Safety Testing

A systematic evaluation suite for LLM safety, robustness, and alignment — covering 500+ prompts across technical, educational, and general knowledge domains.

---

## What This Is

This repository measures how reliably a language model behaves across five dimensions: factual accuracy, logical reasoning, instruction adherence, hallucination resistance, and output clarity. Prompts are written in matched variant sets (A/B/C rephrasings of the same question) to isolate inconsistency caused by phrasing rather than knowledge gaps.

**Key result:** iterative prompt refinement raised response consistency from ~52% to ~70% — a **+35% relative improvement** — measured across 500+ prompt-variant sets.

---

## Evaluation Metrics

| Metric | What It Measures |
|---|---|
| **Accuracy (AC)** | Factual correctness, supported by verifiable knowledge |
| **Reasoning Quality (RQ)** | Logical coherence and completeness of the reasoning chain |
| **Instruction Following (IF)** | Adherence to explicit constraints: format, length, tone, audience |
| **Hallucination Rate (HR)** | Frequency of unsupported or fabricated claims |
| **Clarity (CL)** | Readability, structure, and audience-appropriateness |

Each metric is scored 0–3. The aggregate score is:

```
Aggregate = sum(applicable_scores) / (applicable_dimensions × 3) × 100%
```

Full scoring guidance: [`evaluations/metrics.md`](evaluations/metrics.md)

---

## Prompt Domains

| Domain | Prompts | Focus Areas |
|---|---|---|
| Technical | ~200 | Programming, algorithms, mathematics, system reasoning |
| Educational | ~150 | Science, history, language, conceptual explanation |
| General Knowledge | ~150 | Common sense, world knowledge, analogical reasoning |

---

## Results

| Domain | Avg Consistency | Avg Accuracy |
|---|---|---|
| Technical | 68% | 74% |
| Educational | 71% | 80% |
| General Knowledge | 72% | 76% |
| **Overall** | **~70%** | **~76%** |

Baseline consistency (pre-refinement): ~52%  
Improved consistency (post-refinement): ~70%  
Relative improvement: **+35%**

> Consistency = percentage of prompt-variant sets where all variants receive the same score. A set is consistent when phrasing variation does not affect the model's output quality.

---

## Adversarial Testing

[`prompt-attack-lab/`](prompt-attack-lab/) contains structured test cases for:

- **Jailbreak attacks** — instruction override, roleplay bypass, hypothetical framing, obfuscated instructions
- **Prompt injection** — injecting instructions via user-controlled content (documents, translations, tool inputs)
- **Defense strategies** — input validation, instruction hierarchy enforcement, output monitoring, prompt isolation

---

## Repository Structure

```
prompts/
  technical/        # Reasoning, hallucination, instruction-following prompts
  educational/      # Accuracy-focused prompts across science, history, language
  general/          # Clarity and world-knowledge prompts
evaluations/
  metrics.md        # Scoring definitions for all 5 metrics
  framework.md      # Evaluation methodology and consistency measurement
  results/          # Per-domain results and summary tables
prompt-attack-lab/
  jailbreak-tests.md        # Adversarial jailbreak test cases
  prompt-injection-tests.md # Prompt injection attack test cases
  defense-strategies.md     # Mitigation techniques and defense patterns
```
