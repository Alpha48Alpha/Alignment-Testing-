# Benchmark Design Principles

**Purpose:** Methodology for constructing LLM evaluation benchmarks that produce valid, reliable, and reproducible results.

---

## Step 1: Define the Construct

Before writing prompts, define precisely what you are measuring and what you are not.

**Example — Reasoning Quality:**

| Included | Excluded |
|---|---|
| Multi-step deductive reasoning | Domain knowledge recall |
| Error detection in logical arguments | Calculation accuracy |
| Causal chain identification | Instruction following |

If your benchmark items test multiple constructs simultaneously, scores become uninterpretable: you cannot distinguish a reasoning failure from a knowledge failure.

---

## Step 2: Specify the Reference Answer

Every benchmark item needs a reference answer defined before evaluation. Reference answers should:

- Be grounded in verifiable sources (for factual items)
- Be specified at the appropriate level of abstraction (not overly prescriptive)
- Include acceptable variations where multiple valid responses exist

**Example:**

| Prompt | Reference answer | Acceptable variations |
|---|---|---|
| "What is the capital of Australia?" | Canberra | None — single correct answer |
| "Explain the concept of recursion" | A function that calls itself, with a base case | Multiple valid explanations accepted |

---

## Step 3: Design for Difficulty Distribution

A useful benchmark has items spread across difficulty levels:

- **Easy (expected pass rate > 80%)** — Establishes a floor; models that fail these are broken
- **Medium (expected pass rate 40–80%)** — Primary discriminating range
- **Hard (expected pass rate < 40%)** — Separates strong from weak models; tests limits

If all items are easy, the benchmark cannot distinguish good from excellent models. If all items are hard, it cannot distinguish poor from mediocre models.

---

## Step 4: Test for Variant Parity

For each prompt, create 2–3 semantically equivalent rephrasings. Run all variants against the same model. If score variance across variants exceeds 1.0 point (on a 0–3 scale), the variants are not equivalent and one or more needs revision.

**Example — Low parity (problematic):**

| Variant | Score |
|---|---|
| "What is 15% of 80?" | 3 |
| "A store offers a 15 percent discount on an $80 item. How much is the discount?" | 1 |

The underlying question is identical but the second variant includes a real-world context that introduces additional parsing steps. The variants are not equivalent in difficulty.

---

## Step 5: Establish a Human Baseline

Run the benchmark on a sample of human experts before deploying against models. This provides:

- A performance ceiling (what is achievable by an expert)
- A sanity check on item quality (items that humans fail consistently may be poorly specified)
- A reference point for interpreting model scores

---

## Step 6: Document and Version the Benchmark

Every benchmark should have a version number and a changelog. This is necessary for:

- Detecting regressions when items are modified
- Comparing scores across model versions
- Reproducing results from earlier evaluations

Minimum documentation per benchmark version:

- Date created
- Number of items per category
- Reference answers (or reference answer generation method)
- Evaluator instructions
- Scoring rubric
