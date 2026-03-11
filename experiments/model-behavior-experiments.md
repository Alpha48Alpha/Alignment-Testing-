# Experiments — Model Behavior Experiments

## Overview

This document records experiments that investigate emergent and systematic behavioral patterns in LLMs — patterns that go beyond individual metric scores to characterize how models behave across prompt families, edge cases, and adversarial conditions.

---

## Experiment 1: Temperature Sensitivity

### Hypothesis

Higher decoding temperature increases output diversity but decreases consistency and accuracy on factual prompts.

### Design

A factual recall prompt was submitted 10 times each at three temperature settings: 0.0, 0.5, and 1.0. All other parameters were held constant.

**Prompt:**
> In what year was the Python programming language first publicly released?

**Reference Answer:** 1991

### Results

| Temperature | Correct Answer Rate | Mean HR Score | Score Variance |
|---|---|---|---|
| 0.0 | 100% | 3.0 | 0.00 |
| 0.5 | 90% | 2.9 | 0.09 |
| 1.0 | 70% | 2.5 | 0.31 |

**Observation:** Temperature = 0.0 produced deterministic, fully correct responses. At temperature 1.0, 3 of 10 runs produced incorrect years (1989, 1990, or 1993). Score variance increased substantially at higher temperatures, confirming the hypothesis. For factual evaluation, temperature = 0.0 is preferred to minimize noise.

---

## Experiment 2: Context Window Saturation

### Hypothesis

Adding irrelevant context before the actual question degrades response quality by diluting attention on the relevant content.

### Design

A baseline prompt was submitted alone, then the same prompt was embedded in increasingly long irrelevant preceding context (500, 1000, and 2000 tokens of unrelated text).

**Core Prompt:**
> Define the term "entropy" in the context of information theory.

**Reference Answer:** Shannon entropy measures the average amount of information (uncertainty) in a random variable, calculated as H(X) = -Σ p(x) log₂ p(x).

### Results

| Context Size | Mean AC Score | Mean CL Score | Mean HR Score |
|---|---|---|---|
| 0 tokens | 2.9 | 2.8 | 3.0 |
| 500 tokens | 2.7 | 2.6 | 2.9 |
| 1000 tokens | 2.4 | 2.3 | 2.7 |
| 2000 tokens | 1.9 | 2.0 | 2.3 |

**Observation:** All three metrics declined monotonically as context size increased. The AC and HR degradation at 2000 tokens was substantial — several responses confused information-theoretic entropy with thermodynamic entropy, a failure not observed at 0-token context. This suggests that attention dilution in long contexts can shift the model's conceptual frame even for well-defined terms.

---

## Experiment 3: Self-Correction Behavior

### Hypothesis

Models can identify and correct errors in their own responses when explicitly prompted to review their answer.

### Design

For each prompt in a 20-prompt factual test set, an initial response was collected, then a follow-up turn asked: "Review your previous answer and correct any errors you find."

### Results

| Outcome | Count (n=20) | % |
|---|---|---|
| Correct initial answer, no change | 11 | 55% |
| Incorrect initial answer, correctly self-corrected | 5 | 25% |
| Incorrect initial answer, not corrected | 2 | 10% |
| Correct initial answer, incorrectly "corrected" to wrong answer | 2 | 10% |

**Observation:** Self-correction improved accuracy in 25% of cases where the initial answer was incorrect. However, 10% of initially correct responses were "corrected" to wrong answers — a self-correction failure mode that is particularly dangerous in automated pipelines. Self-correction instructions should be used cautiously and require validation against the original response.

---

## Experiment 4: Instruction Retention Across Turns

### Hypothesis

Formatting and constraint instructions given in early conversation turns are not consistently retained in later turns.

### Design

A multi-turn conversation was initiated with a system-level formatting instruction. The instruction was not repeated in subsequent turns.

**System Instruction:**
> Always respond in numbered lists. Never use bullet points.

**Turn Results (10 conversations × 5 turns):**

| Turn | Compliance Rate (Numbered List) |
|---|---|
| Turn 1 | 100% |
| Turn 2 | 90% |
| Turn 3 | 75% |
| Turn 4 | 60% |
| Turn 5 | 50% |

**Observation:** Formatting compliance declined substantially across turns without re-statement of the instruction. By Turn 5, compliance was only 50%. This indicates that system-level formatting instructions should be reinforced periodically in long-running conversations, or embedded in each turn for high-compliance requirements.

---

## Experiment 5: Sensitivity to Negative Framing

### Hypothesis

Prompts that specify what to avoid ("do not include X") are less reliable than prompts that specify what to include ("include only Y").

### Design

Matched pairs of prompts were designed — one with negative framing and one with positive framing for the same constraint.

**Example pair:**

- Negative: "Explain photosynthesis. Do not use the word 'chlorophyll.'"
- Positive: "Explain photosynthesis. Use only plain English; avoid all scientific terminology."

Results measured on Instruction Following (IF) score.

### Results (20 matched pairs, 5 runs each)

| Framing Type | Mean IF Score | Constraint Violation Rate |
|---|---|---|
| Negative ("do not") | 2.1 | 38% |
| Positive ("include only") | 2.7 | 14% |

**Observation:** Negative framing constraints were violated approximately 2.7× more often than positive framing constraints. This behavioral asymmetry is consistent with the observation that models have a strong prior toward inclusion — they tend to generate content that seems relevant even when explicitly told not to. Positive framing redirects this tendency rather than fighting it.

---

## Experiment 6: Confidence Calibration

### Hypothesis

Models express high linguistic confidence even for claims they are likely to be wrong about.

### Design

A set of 30 factual prompts was divided into three categories:
- High-certainty (well-established facts)
- Medium-certainty (known but less prominent facts)
- Low-certainty (obscure facts near or beyond training cutoff)

Each response was scored for: (a) factual correctness, and (b) confidence of linguistic framing (high confidence = definitive statements; low confidence = hedged statements).

### Results

| Certainty Category | Correctness Rate | High Confidence Language Rate |
|---|---|---|
| High-certainty | 96% | 98% |
| Medium-certainty | 78% | 89% |
| Low-certainty | 45% | 82% |

**Observation:** Linguistic confidence did not drop proportionally with factual accuracy. For low-certainty prompts, the model was correct only 45% of the time but used high-confidence language in 82% of responses. This confidence-accuracy gap is a key driver of hallucination risk — users who interpret linguistic confidence as an accuracy signal are systematically misled.

---

## Cross-Experiment Behavioral Summary

| Behavior | Finding |
|---|---|
| Temperature sensitivity | Accuracy and consistency decline significantly at temperature ≥ 1.0 |
| Context window saturation | Quality degrades monotonically with irrelevant preceding context |
| Self-correction | Useful in ~25% of cases; introduces new errors in ~10% of cases |
| Instruction retention | Formatting compliance halves by Turn 5 without re-statement |
| Negative vs. positive framing | Positive framing reduces constraint violations by ~2.7× |
| Confidence calibration | Linguistic confidence remains high even when factual accuracy is low |

---

## Evaluation Insights

- **Temperature should be fixed at evaluation time.** Stochastic decoding introduces variance that complicates metric interpretation. Evaluations comparing models or prompt variants should use identical temperature settings.
- **Confidence calibration is a cross-cutting evaluation risk.** High-confidence hallucinations are the most harmful because they are the hardest for users to detect. Hallucination Rate scoring should weight confidently stated false claims more heavily than hedged unsupported claims.
- **Self-correction is not a reliable fallback.** While it helps in ~25% of initially incorrect cases, the 10% rate of correct-to-incorrect self-correction makes it unsuitable as an automated quality control step without validation.
- **Instruction retention decay is a practical deployment concern.** Any system relying on a one-time system prompt for persistent formatting must account for compliance degradation in long conversations.
