# Case Study: Multi-Constraint Instruction Failure

**Purpose:** Measure how instruction-following compliance degrades as the number of simultaneous format constraints increases.

---

## Observation

Models follow single constraints reliably but show measurable compliance drop when three or more constraints are specified in the same prompt. The constraint most commonly dropped is the last one stated, suggesting the model underweights constraints near the end of long prompts.

---

## Test Setup

All variants ask the model to explain the same concept (gradient descent). Constraints are added incrementally:

| Variant | Constraints | Pass Rate |
|---|---|---|
| A | 1 constraint: max 3 sentences | ~95% |
| B | 2 constraints: max 3 sentences, no math notation | ~88% |
| C | 3 constraints: max 3 sentences, no math notation, write for a non-technical audience | ~71% |
| D | 4 constraints: above + use a real-world analogy | ~54% |

---

## Prompts

**Variant A:**
> Explain gradient descent in no more than three sentences.

**Variant B:**
> Explain gradient descent in no more than three sentences. Do not use any mathematical notation.

**Variant C:**
> Explain gradient descent in no more than three sentences. Do not use mathematical notation. Write for a non-technical audience with no machine learning background.

**Variant D:**
> Explain gradient descent in no more than three sentences. Do not use mathematical notation. Write for a non-technical audience with no machine learning background. Use a real-world analogy.

---

## Observed Failure Patterns

- **Length violation**: Response exceeds three sentences (most frequent failure in C and D)
- **Notation leak**: Mathematical symbols appear despite the prohibition
- **Analogy omission**: The analogy constraint is dropped most often when it is the last constraint listed

---

## Analysis

Constraint dropping correlates with:
- Constraint position (later = more likely to be ignored)
- Constraint specificity (vague constraints like "write clearly" are dropped before concrete ones)
- Conflict between constraints (brevity vs. analogy creates tension the model resolves by ignoring one)

Reordering constraints — placing the most critical ones last — does not reliably fix the issue. The underlying problem is that the model does not appear to check all constraints before generating.

---

## Severity

**P3 — Medium.** Instruction violations in this category are non-harmful but reduce reliability in production contexts (document generation, structured outputs, constrained summarization).

---

## Takeaway

Multi-constraint prompt testing is necessary to surface reliability limits that single-constraint tests will not catch. Prompts intended for production use should be tested under the full constraint set, not each constraint in isolation.
