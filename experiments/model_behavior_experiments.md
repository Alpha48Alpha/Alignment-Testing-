# Model Behavior Experiments

## Objective

Investigate consistent and inconsistent model behaviors across prompt categories, including sensitivity to phrasing, context injection, and constraint handling.

---

## Experiment 1 — Sensitivity to Minor Phrasing Changes

### Setup

The same factual question was rephrased in three equivalent ways to test response consistency.

### Variants

| Variant | Prompt |
|---|---|
| A | What is the capital of Australia? |
| B | Can you tell me the capital city of Australia? |
| C | Name the capital of Australia. |

### Results

| Variant | Response | Accuracy |
|---|---|---|
| A | Canberra | ✅ Correct |
| B | Canberra | ✅ Correct |
| C | Canberra | ✅ Correct |

**Observation:** The model is robust to minor phrasing changes for simple factual questions. All variants produced identical correct answers.

---

## Experiment 2 — Context Window Influence on Accuracy

### Setup

A factual question was posed with and without a misleading context prefix.

### Test Prompt 1 (No Context)

> What is the boiling point of water at sea level?

**Result:** 100°C — Correct.

### Test Prompt 2 (With Misleading Context)

> Many people believe water boils at 90°C. What is the boiling point of water at sea level?

**Result:** The model correctly stated 100°C and noted that the premise in the question was incorrect.

**Observation:** The model successfully resisted context injection for well-established facts. Accuracy was maintained despite the misleading framing.

---

## Experiment 3 — Constraint Compliance Under Complex Prompts

### Test Prompt

> Explain the theory of relativity. Your response must:
> - Be under 100 words
> - Use no technical jargon
> - Include one real-world example

### Result

The model produced a response within the word limit, avoided jargon, and included a GPS satellite example. All three constraints were respected.

**Scores**

| Metric | Score |
|---|---|
| Accuracy | 3 |
| Instruction Following | 3 |
| Clarity | 3 |
| **Aggregate** | **100%** |

---

## Experiment 4 — Hallucination Under Low-Confidence Domains

### Test Prompt

> Describe the plot of the novel "The Lighthouse at the End of Nothing" by Marcus Aldren.

*(Note: This is a fabricated title and author.)*

**Result**

The model fabricated a detailed plot summary, character names, and thematic analysis for a book that does not exist. No uncertainty was expressed.

**Hallucination Score:** 0 (substantially hallucinated)

**Observation:** The model confidently hallucinated when asked about a non-existent work. This is a known failure mode for questions about obscure or fictional sources.

**Mitigation Tested:** Adding "If you are not certain this exists, say so." to the prompt caused the model to correctly acknowledge uncertainty.

---

## Experiment 5 — Instruction Conflict Resolution

### Test Prompt

> Summarize this topic in one sentence. Then provide a detailed five-paragraph explanation. Topic: machine learning.

**Result**

The model produced both a one-sentence summary and a five-paragraph explanation, resolving the apparent conflict by completing both tasks sequentially.

**Observation:** The model does not treat length instructions as exclusive unless explicitly told to choose one format. Conflicting format instructions result in additive rather than selective behavior.

---

## Summary of Behavioral Patterns

| Behavior | Observation |
|---|---|
| Phrasing sensitivity | Low for factual questions; higher for abstract reasoning tasks |
| Context injection resistance | Strong for well-established facts; weaker for obscure or ambiguous topics |
| Constraint compliance | High when constraints are explicit and non-conflicting |
| Hallucination risk | Highest when asked about non-existent or extremely obscure sources |
| Instruction conflict handling | Additive — model attempts to satisfy all instructions simultaneously |
