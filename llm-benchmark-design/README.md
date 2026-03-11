# LLM Benchmark Design

**Purpose:** Notes on methodology for designing evaluation benchmarks that produce reliable, interpretable, and reproducible results.

---

## Core Principles

A well-designed benchmark must satisfy four properties:

| Property | Description |
|---|---|
| **Validity** | The benchmark measures what it claims to measure |
| **Reliability** | Results are consistent across repeated runs and evaluators |
| **Discriminability** | The benchmark distinguishes meaningfully between model quality levels |
| **Non-contamination** | Test items are not in model training data |

---

## Files

| File | Topic |
|---|---|
| [`design-principles.md`](design-principles.md) | Core methodology for benchmark construction |
| [`prompt-variant-parity.md`](prompt-variant-parity.md) | Ensuring equivalent difficulty across prompt rephrasings |
| [`contamination-detection.md`](contamination-detection.md) | Methods for detecting training data contamination |

---

## Common Benchmark Design Mistakes

1. **Anchoring on model capability, not task difficulty** — Benchmarks built by testing "what models can do" are biased toward current model strengths and will become saturated quickly.

2. **Neglecting variant parity** — If Variant A of a prompt is harder than Variant B, observed score differences reflect prompt difficulty, not model capability.

3. **Single-pass evaluation** — Running each prompt once introduces sampling noise. Multiple passes with temperature > 0 are needed for stable estimates.

4. **No human baseline** — Without a human expert baseline, it is unclear whether a 70% benchmark score is good or poor.

5. **Conflating dimensions** — A single aggregate score hides which dimension failed. A model can score 70% overall while hallucinating badly if other dimensions compensate.
