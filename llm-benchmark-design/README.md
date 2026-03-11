# LLM Benchmark Design

This document describes the principles and methodology used to design evaluation benchmarks in this repository. It covers prompt construction, variant generation, scoring rubric design, and common pitfalls.

---

## Purpose

A well-designed benchmark measures what it claims to measure. Poor benchmark design produces scores that reflect prompt surface features, evaluation artefacts, or model memorization rather than genuine capability.

The goal of this document is to make evaluation design decisions explicit so that benchmarks can be critiqued, replicated, and improved.

---

## Design Principles

### 1. Construct Validity

Each benchmark task should test a clearly defined capability. Before writing prompts, specify:

- What the model must *know* to answer correctly (knowledge requirement)
- What the model must *do* to answer correctly (reasoning requirement)
- What a correct answer looks like (evaluation criterion)

**Example — well-specified:**
- Capability: Multi-step arithmetic reasoning
- Knowledge requirement: Basic arithmetic operations
- Reasoning requirement: Parse a word problem, identify the correct operations, execute them in the right order
- Evaluation criterion: Numerical answer matches expected value; intermediate steps are shown and correct

**Example — poorly specified:**
- Capability: "Smartness"
- Evaluation criterion: "Sounds right"

---

### 2. Prompt Variants for Robustness

Single-prompt benchmarks are unreliable. A model that answers one formulation correctly but fails on semantically equivalent rephrasings does not reliably possess the tested capability.

Each benchmark prompt set should include at least two variants that:
- Use different surface phrasing
- Preserve identical semantic content and difficulty
- Do not introduce new knowledge requirements

Variants allow the computation of a **consistency score** — the degree to which model performance generalizes across equivalent prompts rather than latching onto specific surface features.

**Example prompt set — arithmetic word problems:**

> **Variant A:** Maria has 24 apples. She gives away a third of them to her neighbors and eats 3 herself. How many apples remain?
>
> **Variant B:** A crate holds 24 apples. 8 are distributed to nearby households and 3 are discarded as damaged. How many are left in the crate?

Both variants require the same computation (24 − 8 − 3 = 13). A model that answers one correctly but not the other is relying on surface pattern rather than arithmetic reasoning.

---

### 3. Metric Decomposition

Benchmarks should evaluate specific metrics, not conflate them. A single aggregate score obscures which capability is failing.

For each prompt set, identify which of the five metrics apply:

| Metric | When to apply |
|---|---|
| Accuracy (AC) | When there is a verifiable correct answer |
| Reasoning Quality (RQ) | When the prompt requires multi-step derivation |
| Instruction Following (IF) | When the prompt specifies explicit output constraints |
| Hallucination Rate (HR) | When the response makes factual claims that can be verified |
| Clarity (CL) | When response quality affects comprehensibility |

Not all metrics apply to every task. Applying Reasoning Quality to a simple factual recall prompt inflates scores artificially.

---

### 4. Contamination Avoidance

Benchmark tasks should not be present in model training data in identical form. Common mitigation strategies:

- Use novel scenarios with the same underlying structure as known tasks
- Modify named entities in well-known problems
- Construct tasks from domain-specific knowledge that is less likely to appear verbatim in web-scraped training corpora

**Example — modified CRT item:**
Original (widely circulated): "A bat and ball cost $1.10..."
Modified: "A notebook and pen cost $2.20 in total. The notebook costs $2.00 more than the pen. How much does the pen cost?"

Modifying surface details while preserving the underlying reasoning structure tests the capability more reliably.

---

### 5. Reference Answer Documentation

Every benchmark task should include:

- A reference answer (for objective tasks)
- Evaluation criteria (for subjective or open-ended tasks)
- Common incorrect answers and why they are wrong

Documenting common incorrect answers is especially useful for reasoning tasks. If the expected failure mode is known in advance, evaluators can check for it specifically rather than free-form scoring.

---

## Benchmark Structure Template

```
## [Benchmark Name]

**Capability tested:** [One-sentence description]

**Applicable metrics:** [AC | RQ | IF | HR | CL — select all that apply]

**Difficulty:** [Easy | Medium | Hard]

### Prompt Set

**Variant A:**
> [Prompt text]

**Variant B:**
> [Prompt text]

**Reference answer:**
[Correct answer with explanation]

**Common incorrect responses:**
- [Incorrect answer 1] — [Why it's wrong]
- [Incorrect answer 2] — [Why it's wrong]

**Evaluation notes:**
[Any scoring nuances specific to this task]
```

---

## Anti-Patterns in Benchmark Design

| Anti-Pattern | Problem | Mitigation |
|---|---|---|
| Single-prompt evaluation | High variance; surface sensitivity | Use ≥2 variants per task |
| Vague evaluation criteria | Low inter-rater agreement | Specify what a 0, 1, 2, and 3 score looks like |
| Conflated metrics | Cannot identify which capability is failing | Score each metric separately |
| Tasks identical to training data | Tests memorization, not generalization | Modify surface details of known tasks |
| Overly long prompts | Masks instruction following failures | Keep prompts concise; isolate one constraint at a time |
| Correct answer depends on prompt framing | Tests phrasing bias, not capability | Verify that both variants have the same ground truth answer |

---

## Scoring Reference

Each response is scored 0–3 per applicable metric. The aggregate score across a prompt set is:

```
Aggregate = sum(applicable_metric_scores) / (number_of_applicable_metrics × 3) × 100%
```

See [`../evaluation-framework/README.md`](../evaluation-framework/README.md) for the full scoring rubric and inter-rater calibration guidance.

---

## Related

- [`../evaluation-framework/README.md`](../evaluation-framework/README.md) — Scoring methodology
- [`../evaluations/metrics.md`](../evaluations/metrics.md) — Per-metric definitions and scoring guidance
- [`../case-studies/model-failure-analysis/README.md`](../case-studies/model-failure-analysis/README.md) — Failure modes that inform benchmark design
