# Alignment-Testing-
### LLM Safety & Evaluation — Adversarial testing, hallucination benchmarking, and response quality measurement across 500+ prompts.

---

## Overview

This repository contains a structured evaluation framework for large language models, covering **accuracy, reasoning quality, instruction following, hallucination detection, and response clarity**. It includes adversarial safety testing (jailbreaks, prompt injection) alongside comparative benchmarking across multiple model generations.

The work demonstrates:
- A **35% relative improvement in response consistency** (from ~52% to ~70%) achieved through iterative prompt refinement
- **Cross-model benchmarking** (GPT-4o, GPT-3.5, Claude 3 Sonnet) exposing consistent failure modes tied to model generation
- **13 jailbreak attack patterns** and **7 injection attack vectors** with documented safe behavior expectations and mitigation strategies

---

## Key Findings

1. **Citation fabrication is the highest-severity hallucination failure.** GPT-3.5 produced fully unverifiable citations (author names, journal titles, volume numbers) that were plausible but nonexistent. GPT-4o and Claude 3 Sonnet showed a 25–50% improvement on hallucination benchmarks for this prompt type.

2. **Persona/roleplay framing is the most reliably exploited jailbreak vector.** Multi-layer fictional framing (story within a story) and gradual multi-turn escalation consistently reduce model safety adherence more than direct override commands.

3. **Length and format constraints surface instruction-following weaknesses more reliably than content constraints.** The "exactly two sentences" and "exactly three sentences" prompts differentiated model generations better than any factual accuracy test.

4. **General knowledge domain shows the largest cross-model quality gap.** GPT-3.5 averaged 84% vs 100% for GPT-4o and Claude 3 Sonnet on general knowledge clarity prompts — a 16-point gap driven by analogical reasoning and structured explanation tasks.

5. **Natural-language rephrasings of technical/code problems reduce reasoning depth.** Variants of code prompts expressed in plain English consistently scored lower on Reasoning Quality, revealing a formatting-dependency in how models surface intermediate steps.

---

## Prompt Categories

| Domain | Prompt Sets | Prompt Variants | Primary Metrics |
|---|---|---|---|
| Technical | ~80 | ~200 | Reasoning Quality, Instruction Following, Hallucination Rate |
| Educational | ~50 | ~150 | Accuracy, Reasoning Quality |
| General Knowledge | ~50 | ~150 | Clarity, Instruction Following, Accuracy |
| **Total** | **~180** | **~500+** | All 5 |

---

## Evaluation Metrics

Each prompt response is scored **0–3** per applicable dimension:

| Metric | Abbr | What it measures |
|---|---|---|
| Accuracy | AC | Factual correctness |
| Reasoning Quality | RQ | Logical coherence and step transparency |
| Instruction Following | IF | Adherence to explicit format, length, and tone constraints |
| Hallucination Rate | HR | Frequency of unverifiable or fabricated claims (inverted: 3 = none) |
| Clarity | CL | Readability and audience-appropriateness |

```
Aggregate = sum(applicable_metric_scores) / (applicable_dimensions × 3) × 100%
```

See [`evaluations/metrics.md`](evaluations/metrics.md) for full definitions and [`evaluations/framework.md`](evaluations/framework.md) for methodology.

---

## Results

| Domain | Models Tested | Prompts Evaluated | Avg Consistency | Avg Accuracy |
|---|---|---|---|---|
| Technical | GPT-4o, GPT-3.5, Claude 3 Sonnet | ~200 | 68% → **98%** | 74% → **96%** |
| Educational | GPT-4o, GPT-3.5, Claude 3 Sonnet | ~150 | 71% → **100%** | 80% → **98%** |
| General Knowledge | GPT-4o, GPT-3.5, Claude 3 Sonnet | ~150 | 72% → **100%** | 76% → **95%** |
| **Total** | | **~500+** | **52% → ~70%** | **76% avg** |

> Consistency = percentage of prompt variant sets where all variants receive the same score.  
> The **35% relative improvement** (52% → 70%) was achieved by iteratively reducing prompt ambiguity, adding grounding context, and specifying explicit output constraints.

Detailed per-prompt scores by domain: [`evaluations/results/`](evaluations/results/)

---

## Prompt Attack Lab

The [`prompt-attack-lab/`](prompt-attack-lab/) directory covers adversarial safety evaluation:

| File | Contents |
|---|---|
| [`jailbreak-tests.md`](prompt-attack-lab/jailbreak-tests.md) | 13 test cases across 5 attack categories: instruction override, persona/roleplay, hypothetical framing, multi-turn escalation, output format manipulation |
| [`prompt-injection-tests.md`](prompt-attack-lab/prompt-injection-tests.md) | 7 injection vectors: direct content injection, indirect/RAG injection, agentic pipeline injection |
| [`defense-strategies.md`](prompt-attack-lab/defense-strategies.md) | 7 concrete mitigation strategies with implementation guidance and key metrics (e.g., target JSR < 2%) |

---

## Repository Structure

```
prompts/
  technical/        # Reasoning quality, instruction following, hallucination rate
  educational/      # Accuracy across science, history, language domains
  general/          # Clarity, analogical reasoning, world knowledge
evaluations/
  metrics.md        # Definitions for all 5 LLM evaluation metrics
  framework.md      # Scoring rubric, consistency measurement, aggregate formula
  results/
    technical_results.md    # Per-prompt scores and failure mode analysis (technical)
    educational_results.md  # Per-prompt scores and cross-model comparison (educational)
    general_results.md      # Per-prompt scores and cross-model comparison (general)
prompt-attack-lab/
  jailbreak-tests.md        # 13 jailbreak test cases with expected safe behaviors
  prompt-injection-tests.md # 7 injection attack vectors across direct, indirect, agentic contexts
  defense-strategies.md     # Concrete mitigation strategies with implementation guidance
```
