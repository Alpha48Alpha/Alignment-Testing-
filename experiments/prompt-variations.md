# Experiments — Prompt Variations

## Overview

This document records the results of structured prompt variation experiments conducted to understand how surface-level changes to prompt phrasing affect model output quality. The goal is not to test different questions, but to test how different ways of asking the same question influence evaluation scores.

---

## Experimental Design

Each experiment holds the underlying question constant while varying one prompt dimension at a time:

| Dimension | Example Variation |
|---|---|
| Phrasing style | Imperative vs. interrogative |
| Specificity | Vague vs. detailed constraint specification |
| Role assignment | No role vs. expert persona |
| Output format | Unspecified vs. explicitly specified |
| Hedge language | Direct request vs. hedged request |

Each variation is run 5 times to control for stochastic variance. Results are reported as mean scores on applicable metrics.

---

## Experiment 1: Imperative vs. Interrogative Phrasing

### Question: Binary search time complexity

**Variant A (Imperative):**
> Explain the time complexity of binary search.

**Variant B (Interrogative):**
> What is the time complexity of binary search, and why?

**Results:**

| Metric | Variant A (Mean) | Variant B (Mean) | Difference |
|---|---|---|---|
| Accuracy | 2.8 | 2.9 | +0.1 |
| Reasoning Quality | 2.1 | 2.6 | +0.5 |
| Clarity | 2.4 | 2.5 | +0.1 |

**Observation:** The interrogative form ("and why?") produced meaningfully higher Reasoning Quality scores. The direct "why" appears to elicit explanation structure more reliably than the imperative "explain," which sometimes produced only the answer without reasoning.

---

## Experiment 2: Vague vs. Detailed Constraint Specification

### Question: Summarize the water cycle

**Variant A (Vague):**
> Summarize the water cycle briefly.

**Variant B (Detailed):**
> Summarize the water cycle in exactly 3 sentences. Include: evaporation, condensation, and precipitation.

**Results:**

| Metric | Variant A (Mean) | Variant B (Mean) | Difference |
|---|---|---|---|
| Instruction Following | 1.8 | 2.9 | +1.1 |
| Accuracy | 2.7 | 2.8 | +0.1 |
| Clarity | 2.5 | 2.6 | +0.1 |

**Observation:** Detailed constraint specification produced a dramatic improvement in Instruction Following (+1.1). Accuracy and Clarity were relatively unaffected, confirming that constraint specificity primarily improves IF without degrading content quality.

---

## Experiment 3: No Role vs. Expert Persona

### Question: Explain machine learning overfitting

**Variant A (No role):**
> Explain what overfitting is in machine learning.

**Variant B (Expert persona):**
> You are a machine learning researcher. Explain what overfitting is to a data science student.

**Results:**

| Metric | Variant A (Mean) | Variant B (Mean) | Difference |
|---|---|---|---|
| Accuracy | 2.6 | 2.9 | +0.3 |
| Reasoning Quality | 2.2 | 2.6 | +0.4 |
| Hallucination Rate | 2.7 | 2.9 | +0.2 |
| Clarity | 2.4 | 2.8 | +0.4 |

**Observation:** Expert persona assignment improved all measured metrics. The largest gains were in Reasoning Quality and Clarity, suggesting that persona assignment activates a more structured and pedagogically oriented response mode.

---

## Experiment 4: Unspecified vs. Explicitly Specified Output Format

### Question: List the causes of WWI

**Variant A (Format unspecified):**
> What were the main causes of World War I?

**Variant B (Format specified):**
> List the five main causes of World War I using a numbered list. One sentence per item. No introduction or conclusion.

**Results:**

| Metric | Variant A (Mean) | Variant B (Mean) | Difference |
|---|---|---|---|
| Instruction Following | 1.6 | 2.7 | +1.1 |
| Clarity | 2.3 | 2.8 | +0.5 |
| Accuracy | 2.7 | 2.8 | +0.1 |

**Observation:** Explicit format specification significantly improved IF and also raised Clarity by +0.5. Variant A frequently included introductory and concluding sentences that were not requested, while Variant B's explicit prohibition ("no introduction or conclusion") was largely respected.

---

## Experiment 5: Direct vs. Hedged Request

### Question: Current best practices in password security

**Variant A (Direct):**
> What are the current best practices for password security?

**Variant B (Hedged):**
> If you know them, what might be some generally accepted practices for password security?

**Results:**

| Metric | Variant A (Mean) | Variant B (Mean) | Difference |
|---|---|---|---|
| Accuracy | 2.7 | 2.3 | -0.4 |
| Hallucination Rate | 2.8 | 2.4 | -0.4 |
| Clarity | 2.8 | 2.3 | -0.5 |

**Observation:** Hedged phrasing produced lower quality across all measured dimensions. The qualification "if you know them" and "might be" appears to introduce response uncertainty, resulting in less specific and less well-organized answers. Hedging is not recommended when precise, reliable information is the goal.

---

## Cross-Experiment Summary

| Variation Type | Primary Metric Affected | Direction | Mean Magnitude |
|---|---|---|---|
| Interrogative vs. imperative | Reasoning Quality | +0.5 | Moderate |
| Detailed constraints | Instruction Following | +1.1 | Large |
| Expert persona | Reasoning Quality, Clarity | +0.4 | Moderate |
| Explicit format | IF, Clarity | +1.1, +0.5 | Large |
| Hedged request | Accuracy, CL, HR | -0.4 | Moderate (negative) |

---

## Evaluation Insights

- **Constraint specification has the largest impact on measurable outcomes** across all experiments. Adding explicit format and content requirements to an unspecified prompt raised IF scores by +1.1 in two independent experiments.
- **Interrogative phrasing is a low-cost improvement** for prompts where reasoning transparency is important. "Why?" consistently elicited more explicit reasoning chains than imperative "explain."
- **Expert persona assignment improves multiple metrics simultaneously.** It is particularly valuable when both domain accuracy and pedagogical clarity are required.
- **Hedged requests degrade quality.** Uncertainty language in the prompt appears to trigger uncertainty in the response. For evaluation purposes, requests should be stated directly.

---

## Recommendations for Prompt Authors

1. Use interrogative or "why/how" framing when Reasoning Quality is a target metric.
2. Always specify format, length, and required sections explicitly.
3. Assign a subject-matter expert persona when domain-specific depth is required.
4. Avoid hedge language in prompts intended to elicit precise factual information.
5. Test both a "minimal" and a "maximal" variant of each prompt to quantify the impact of constraint specification.
