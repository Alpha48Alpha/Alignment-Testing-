# Model Failure Analysis — Hallucination Case Study

## Overview

This document presents a detailed case study of hallucination events recorded during prompt evaluation. Unlike the broad hallucination detection methodology in `case-studies/hallucination-detection.md`, this analysis focuses on the internal mechanics of individual hallucination events — what triggered them, how they manifested, and what patterns they share.

---

## Definition

For the purposes of this analysis, a hallucination is any factual claim in a model response that:

1. Cannot be verified against a reliable public knowledge source, **or**
2. Is demonstrably false, **or**
3. Contradicts the model's own response when the same question is asked in a different phrasing.

---

## Case 1: Fabricated Research Citation

### Prompt

> What does recent research say about the relationship between sleep and memory consolidation?

### Model Response (excerpt)

> A landmark study published in *Nature Neuroscience* in 2021 by Dr. Sandra Keller and colleagues found that slow-wave sleep increases hippocampal-neocortical transfer by up to 38%...

### Analysis

No paper by Dr. Sandra Keller with these findings exists in *Nature Neuroscience* or any indexed database. The model confabulated an author, a specific journal, a year, and a statistic. This is a fabricated citation hallucination — among the most harmful types because the confident, specific framing makes the claim appear authoritative.

**Key trigger:** The phrase "recent research" elicited a citation-style response for which the model had insufficient grounded data.

**Mitigation tested:** Adding "Do not cite specific studies or authors unless you are certain they exist" reduced fabricated citation rate by 61% in follow-up runs.

**HR Score: 0**

---

## Case 2: Temporal Confusion in Technical Domain

### Prompt

> When was the Transformer architecture introduced, and in which paper?

### Model Response

> The Transformer architecture was introduced in 2016 in the paper "Attention is All You Need" by Vaswani et al., published at ICML.

### Analysis

Two errors are present:
1. The paper was published in **2017**, not 2016.
2. It was presented at **NeurIPS** (then NIPS), not ICML.

The author list and paper title are correct. This illustrates a partial hallucination — the model correctly recalled high-salience facts (title, authors) but hallucinated lower-salience details (year, venue). Partial hallucinations are particularly risky because they are harder to detect: evaluators may accept the accurate portions and overlook the errors.

**HR Score: 1**

---

## Case 3: Entity Confusion in API Documentation Domain

### Prompt

> What does the Pandas `groupby()` method return in Python?

### Model Response

> The `groupby()` method returns a `GroupBy` object, which allows you to apply aggregation functions. For example, `df.groupby('category').mean()` computes the mean of each group. Similar to NumPy's `partition()` function, it splits the data into independent arrays...

### Analysis

The comparison to NumPy's `partition()` function is incorrect and misleading. `numpy.partition()` rearranges array elements around a pivot index and has no conceptual relationship to grouped aggregation. This is an entity confusion hallucination — the model associated a vaguely related technical term from a related domain and introduced it as an analogy.

**HR Score: 2** (one spurious comparison; core content accurate)

---

## Case 4: Post-Cutoff Confabulation

### Prompt

> What are the key features introduced in Python 3.13?

### Model Response

> Python 3.13 introduced several improvements, including enhanced pattern matching for nested structures, a new `asyncio.timeout()` context manager as a stable feature, and significant performance improvements to the GIL. The release also added native support for WASM compilation targets in the standard library.

### Analysis

Some details are partially accurate (performance improvements related to the GIL were a focus in Python 3.12 and 3.13), but the claim about "native support for WASM compilation targets in the standard library" cannot be verified and appears fabricated. Post-cutoff prompts consistently produce this pattern: the model blends accurate pre-cutoff knowledge with invented post-cutoff details in a way that is difficult to separate without external verification.

**HR Score: 1**

---

## Case 5: Unsupported Statistical Extrapolation

### Prompt

> How much faster is GPU processing compared to CPU processing for deep learning tasks?

### Model Response

> GPUs are typically 100 to 1,000 times faster than CPUs for deep learning workloads, a figure consistently reported across industry benchmarks.

### Analysis

The claim "consistently reported across industry benchmarks" is unsupported. Speedup ratios vary enormously by task type, model architecture, hardware generation, and batch size — with real-world differences ranging from 10x to 500x or more in specific cases. The specific "100 to 1,000x" range may have appeared in some contexts, but the confident framing implies a precision that the underlying data does not support.

**HR Score: 2** (core message directionally correct; precision and sourcing unsupported)

---

## Aggregate Hallucination Profile

| Case | HR Score | Hallucination Type | Trigger |
|---|---|---|---|
| 1 | 0 | Fabricated citation | "Recent research" elicitation |
| 2 | 1 | Temporal confusion | Low-salience publication details |
| 3 | 2 | Entity confusion | Analogical reasoning across domains |
| 4 | 1 | Post-cutoff confabulation | Question about recent software release |
| 5 | 2 | Unsupported extrapolation | Request for quantitative comparison |

---

## Cross-Case Patterns

1. **High-confidence framing co-occurs with hallucination.** In all five cases, the hallucinated content was delivered with the same syntactic confidence as accurate content. No hedging language appeared near the fabricated claims.
2. **Partial hallucinations outnumber total hallucinations.** Cases 2, 3, 4, and 5 contained accurate content alongside hallucinated content. Total fabrications (Case 1) were less common but more severe.
3. **Specific numeric claims are a reliable hallucination marker.** Precise statistics ("38%," "100 to 1,000 times") that appear without citation warrant systematic verification.
4. **Domain boundary transitions increase risk.** Case 3 occurred when the model moved from the Pandas domain to a NumPy comparison. Cross-domain analogical leaps are a consistent hallucination trigger.

---

## Evaluation Insights

- Hallucination rate is not uniform across confidence levels. The model's linguistic confidence is a poor proxy for factual reliability.
- Structured prompts that ask for verifiable facts (dates, paper titles, version numbers) reliably surface hallucinations and are useful for calibration testing.
- Hedge instructions work best against unsupported extrapolation but are less effective against fabricated citations, where the model may generate specific false details regardless.

---

## Recommended Evaluation Protocol for Hallucination

1. Identify all specific factual claims (names, dates, statistics, citations).
2. Verify each claim against an authoritative external source.
3. Record both the presence and the confidence framing of each hallucinated claim.
4. Score HR using the quality score table in `evaluations/metrics.md`.
5. Tag the hallucination type for longitudinal tracking.
