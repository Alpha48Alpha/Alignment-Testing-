# Experiments — Reasoning Tests

## Overview

This document records structured experiments designed to isolate and characterize reasoning behavior in large language models. Each experiment targets a specific reasoning capability — mathematical, logical, causal, or analogical — and measures performance with and without scaffolding interventions.

---

## Experimental Design

All experiments follow a controlled design:

- **Control condition:** Minimal prompt with no explicit reasoning instruction.
- **Treatment condition:** Same prompt with an added chain-of-thought (CoT) instruction.
- **Evaluation metric:** Reasoning Quality (RQ, 0–3 scale) as defined in `evaluations/metrics.md`.
- **Runs per condition:** 10 independent runs.

Control and treatment conditions are compared on mean RQ score and on the rate of specific failure modes.

---

## Experiment 1: Arithmetic Word Problems

### Task

Multi-step arithmetic requiring two or more calculation steps.

**Prompt (Control):**
> A train travels 240 km in 3 hours. A car travels 300 km in 4 hours. Which vehicle is faster, and by how much?

**Prompt (Treatment):**
> A train travels 240 km in 3 hours. A car travels 300 km in 4 hours. Which vehicle is faster, and by how much?
> Work through the calculation step by step before giving your final answer.

**Results:**

| Condition | Mean RQ | Premise Skipping Rate | Correct Answer Rate |
|---|---|---|---|
| Control | 1.6 | 60% | 80% |
| Treatment (CoT) | 2.8 | 10% | 100% |

**Observation:** Chain-of-thought instruction reduced premise skipping from 60% to 10% and eliminated incorrect answers entirely. Many control-condition responses gave the correct answer without showing any calculation steps, which scores low on RQ even when accurate.

**Reference calculation:** Train: 240/3 = 80 km/h. Car: 300/4 = 75 km/h. Train is faster by 5 km/h.

---

## Experiment 2: Syllogistic Reasoning (Categorical Deduction)

### Task

Classic syllogistic reasoning requiring valid deductive inference.

**Prompt (Control):**
> All birds have wings. Penguins are birds. Do penguins have wings?

**Prompt (Treatment):**
> All birds have wings. Penguins are birds. Do penguins have wings?
> First, state the logical form of the argument, then apply it to reach your conclusion.

**Results:**

| Condition | Mean RQ | Logical Inversion Rate | Correct Conclusion Rate |
|---|---|---|---|
| Control | 2.1 | 20% | 90% |
| Treatment (CoT) | 2.7 | 5% | 100% |

**Observation:** Most control responses correctly concluded "yes," but 20% of runs included a logical inversion in the reasoning ("penguins have wings because they can't fly, so they must have retained wing structures"). Treatment condition enforced explicit logical form statement, which reduced inversion rate from 20% to 5%.

**Correct reasoning:** Major premise: All birds have wings. Minor premise: Penguins are birds. Conclusion: Penguins have wings (even though they cannot fly).

---

## Experiment 3: Causal Inference

### Task

Distinguishing correlation from causation in a study description.

**Prompt (Control):**
> A study found that children who read more books score higher on vocabulary tests. Does reading books cause higher vocabulary scores?

**Prompt (Treatment):**
> A study found that children who read more books score higher on vocabulary tests. Does reading books cause higher vocabulary scores?
> Before concluding, consider what the study design would need to include to establish causation.

**Results:**

| Condition | Mean RQ | Scope Conflation Rate | Correct Causal Reasoning Rate |
|---|---|---|---|
| Control | 1.4 | 50% | 40% |
| Treatment (CoT) | 2.4 | 10% | 80% |

**Observation:** Causal inference was the weakest reasoning domain in control conditions. 50% of control runs committed scope conflation — treating an observational correlation as causal evidence. The treatment instruction ("consider what the study design would need to include") substantially improved responses by directing attention to confounding variables and study design requirements.

---

## Experiment 4: Analogical Reasoning

### Task

Completing a verbal analogy and explaining the relationship.

**Prompt (Control):**
> Doctor is to hospital as teacher is to ___. Explain your answer.

**Prompt (Treatment):**
> Doctor is to hospital as teacher is to ___. 
> First, identify the relationship between "doctor" and "hospital," then apply the same type of relationship to "teacher."

**Results:**

| Condition | Mean RQ | False Analogy Rate | Correct Answer Rate |
|---|---|---|---|
| Control | 2.3 | 15% | 90% |
| Treatment (CoT) | 2.8 | 5% | 98% |

**Observation:** Analogical reasoning was relatively strong in control conditions. Treatment improved RQ primarily by making the relationship type explicit, reducing instances where the model identified a different (weaker) relationship type.

**Correct answer:** School. Relationship: "professional is to the institution where they practice their profession."

---

## Experiment 5: Multi-Step Conditional Reasoning

### Task

A chained "if-then" reasoning problem requiring multiple conditional applications.

**Prompt (Control):**
> If it rains, the ground gets wet. If the ground is wet, the grass grows faster. If the grass grows faster, the lawn needs mowing more often. It is raining today. What can we conclude about lawn mowing?

**Prompt (Treatment):**
> If it rains, the ground gets wet. If the ground is wet, the grass grows faster. If the grass grows faster, the lawn needs mowing more often. It is raining today. What can we conclude about lawn mowing?
> Trace through each conditional step in order before stating your conclusion.

**Results:**

| Condition | Mean RQ | Steps Explicitly Traced (%) | Correct Conclusion Rate |
|---|---|---|---|
| Control | 1.8 | 30% | 90% |
| Treatment (CoT) | 2.9 | 95% | 100% |

**Observation:** Control responses frequently jumped to the correct conclusion without tracing intermediate steps (only 30% traced all three steps). Treatment produced near-complete step tracing (95%) and eliminated incorrect conclusions.

---

## Aggregate Results Across Experiments

| Experiment | Control Mean RQ | Treatment Mean RQ | Improvement |
|---|---|---|---|
| Arithmetic word problems | 1.6 | 2.8 | +1.2 |
| Syllogistic reasoning | 2.1 | 2.7 | +0.6 |
| Causal inference | 1.4 | 2.4 | +1.0 |
| Analogical reasoning | 2.3 | 2.8 | +0.5 |
| Multi-step conditional | 1.8 | 2.9 | +1.1 |
| **Mean** | **1.84** | **2.72** | **+0.88** |

---

## Evaluation Insights

- **Chain-of-thought instructions consistently improve Reasoning Quality.** The mean improvement across all five experiments was +0.88 points on a 0–3 scale.
- **The improvement is largest for tasks with the most steps** (arithmetic, multi-step conditional). Tasks with fewer required steps (analogical reasoning) show smaller gains.
- **Causal inference is the highest-risk reasoning domain.** It had the lowest baseline performance and the highest scope conflation rate. Explicit "consider study design" instructions are an effective and low-cost intervention.
- **Correct answer rate alone is not a sufficient proxy for Reasoning Quality.** In all five control conditions, correct answer rates were higher than mean RQ scores, confirming that models frequently reach correct conclusions through incomplete or flawed reasoning chains.

---

## Recommendations

1. Apply chain-of-thought scaffolding to all reasoning-intensive prompts, not just the most complex ones.
2. Use domain-specific CoT instructions for causal inference tasks ("consider confounding variables") rather than generic step-tracing instructions.
3. Evaluate RQ independently of final answer correctness in all automated pipelines.
4. Use step-tracing rate (% of responses that explicitly trace all required steps) as a secondary signal alongside mean RQ scores.
