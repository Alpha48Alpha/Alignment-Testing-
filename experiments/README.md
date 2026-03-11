# Experiments

This directory documents controlled experiments conducted to measure the effect of specific prompt engineering techniques on model evaluation metrics.

Each experiment follows a consistent structure: hypothesis, methodology, results, and takeaway.

---

## Experiment 1: Effect of Constraint Repetition on Instruction Following

**Date:** 2024-Q3  
**Models tested:** GPT-4o, Claude 3 Sonnet  
**Metric focus:** Instruction Following (IF)

### Hypothesis

Repeating the most restrictive constraint at the end of a multi-constraint prompt will increase full compliance rates compared to stating it only at the beginning.

### Methodology

- 20 prompt sets, each containing 3 explicit constraints (format, length, and tone/audience)
- **Control condition:** All constraints listed at the start of the prompt only
- **Treatment condition:** Constraints listed at the start, with the most restrictive constraint restated at the end

Each condition was run 5 times per prompt set. Responses were scored per constraint (0 = violated, 2 = followed). Full compliance required all three constraints to be followed.

### Results

| Condition | Full compliance rate | Avg IF score |
|---|---|---|
| Control (constraint at start only) | 54% | 2.1 / 3.0 |
| Treatment (constraint restated at end) | 78% | 2.6 / 3.0 |

The improvement was most pronounced for length constraints ("respond in exactly two sentences"), where compliance increased from 48% to 82%.

Tone/audience constraints showed smaller improvement (62% → 71%), possibly because tone is more subjective and harder to verify mechanically.

### Takeaway

Restating the most critical constraint at the end of a multi-constraint prompt meaningfully improves instruction following. This is a low-cost intervention that can be applied to any prompt without changing its semantic content. The effect is strongest for objective constraints (word count, sentence count) and weaker for subjective ones (tone, register).

---

## Experiment 2: Prompt Grounding for Hallucination Reduction

**Date:** 2024-Q3  
**Models tested:** GPT-4o, Llama 3 70B  
**Metric focus:** Hallucination Rate (HR)

### Hypothesis

Providing a reference passage within the prompt will reduce hallucination on questions about niche or ambiguous topics compared to zero-context prompting.

### Methodology

- 30 prompt sets on niche topics (obscure scientific concepts, historical events with limited training data)
- **Control condition:** Question-only prompt with no additional context
- **Treatment condition:** Prompt includes a 100–200 word reference passage drawn from a reliable source

Responses were scored on HR using the standard 0–3 scale. Additionally, evaluators counted specific fabricated claims per response.

### Results

| Condition | Avg HR score | Avg fabricated claims per response |
|---|---|---|
| Control (no context) | 1.4 / 3.0 | 2.7 |
| Treatment (with reference) | 2.7 / 3.0 | 0.4 |

Fabricated claims dropped by ~85% when a reference passage was provided. The majority of remaining fabrications in the treatment condition were peripheral details not covered by the passage.

### Takeaway

Reference passage grounding is highly effective at reducing hallucination. The model's tendency to fabricate is significantly reduced when reliable context is provided, even when the passage does not fully answer the question. The residual hallucinations tend to be peripheral rather than central claims, which is consistent with the model filling gaps outside the provided context.

Limitation: This technique requires that a reliable reference passage be available at query time, which is not always feasible in production. Retrieval-augmented generation (RAG) architectures implement this pattern at scale.

---

## Experiment 3: Few-Shot Reasoning Examples for Multi-Step Problems

**Date:** 2024-Q4  
**Models tested:** GPT-4o, Claude 3.5 Sonnet  
**Metric focus:** Reasoning Quality (RQ)

### Hypothesis

Providing one worked example that demonstrates intermediate reasoning steps will improve Reasoning Quality scores on multi-step arithmetic and logic problems compared to zero-shot prompting.

### Methodology

- 25 multi-step reasoning problems (word problems, logical syllogisms, CRT-style items)
- **Control condition:** Zero-shot — problem only
- **Treatment condition:** One-shot — one worked example showing explicit intermediate steps, followed by the problem

For scoring, responses were evaluated on whether the model showed explicit intermediate steps and whether those steps were logically correct.

### Results

| Condition | Avg RQ score | Correct final answer rate | Explicit steps shown |
|---|---|---|---|
| Control (zero-shot) | 1.8 / 3.0 | 64% | 41% |
| Treatment (one-shot with steps) | 2.5 / 3.0 | 83% | 91% |

The one-shot condition produced explicit intermediate steps in 91% of responses, up from 41% in the zero-shot condition. Correct final answer rate increased by 19 percentage points.

### Takeaway

Few-shot examples that demonstrate step-by-step reasoning strongly influence whether the model explicitly reasons through problems rather than jumping to an answer. This matters both for accuracy (models that show their work are more likely to catch arithmetic errors) and for evaluability (intermediate steps allow evaluators to score reasoning quality rather than treating the problem as a black box).

For high-stakes reasoning tasks, including at least one worked example is a reliable way to improve both performance and transparency.

---

## Experiment 4: Temperature and Response Consistency

**Date:** 2024-Q4  
**Models tested:** GPT-4o  
**Metric focus:** Consistency (cross-run stability)

### Hypothesis

Lower temperature settings will produce more consistent outputs across multiple runs of the same prompt, but may reduce response quality on open-ended tasks.

### Methodology

- 15 prompt sets (mix of factual, reasoning, and open-ended)
- Temperature settings tested: 0.0, 0.3, 0.7, 1.0
- Each prompt run 10 times per temperature setting
- Consistency measured as the standard deviation of aggregate scores across the 10 runs

### Results

| Temperature | Avg score std dev | Avg aggregate score (factual) | Avg aggregate score (open-ended) |
|---|---|---|---|
| 0.0 | 0.08 | 78% | 71% |
| 0.3 | 0.11 | 77% | 74% |
| 0.7 | 0.19 | 76% | 76% |
| 1.0 | 0.31 | 73% | 77% |

Lower temperatures produced more consistent scores, particularly for factual tasks. For open-ended tasks, temperature 0.7 and 1.0 produced comparable or slightly higher scores, likely because creative variation is valued in open-ended evaluation.

### Takeaway

For evaluation runs where consistency across reruns is important (e.g., comparing model versions), set temperature to 0.0 or 0.3. For open-ended generation quality assessments, temperature 0.7 provides a reasonable balance of quality and diversity. Never evaluate a model's open-ended generation quality at temperature 0.0 — the results will be artificially consistent but may not represent the model's typical output distribution.

---

## Experiment Log

| ID | Title | Date | Models | Primary Metric | Outcome |
|---|---|---|---|---|---|
| EXP-001 | Constraint Repetition | 2024-Q3 | GPT-4o, Claude 3 Sonnet | IF | +24pp full compliance |
| EXP-002 | Prompt Grounding for Hallucination | 2024-Q3 | GPT-4o, Llama 3 70B | HR | -85% fabricated claims |
| EXP-003 | Few-Shot Reasoning Examples | 2024-Q4 | GPT-4o, Claude 3.5 Sonnet | RQ | +19pp correct answer rate |
| EXP-004 | Temperature and Consistency | 2024-Q4 | GPT-4o | Consistency | Confirms temp=0.0 for stable eval |

---

## Related

- [`../evaluation-framework/README.md`](../evaluation-framework/README.md) — Scoring methodology used in experiments
- [`../python-tools/README.md`](../python-tools/README.md) — Python tools for automating experiment runs
- [`../llm-benchmark-design/README.md`](../llm-benchmark-design/README.md) — Benchmark design principles
