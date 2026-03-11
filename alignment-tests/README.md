# Alignment Tests

Structured tests for evaluating whether a model behaves in accordance with its stated guidelines, system instructions, and intended values under pressure, ambiguity, and adversarial conditions.

---

## Test Categories

| File | Focus |
|---|---|
| [`instruction-conflict-tests.md`](instruction-conflict-tests.md) | System prompt vs. user prompt conflicts |
| [`value-consistency-tests.md`](value-consistency-tests.md) | Consistency of stated values across rephrased scenarios |
| [`behavioral-boundary-tests.md`](behavioral-boundary-tests.md) | Safety boundary adherence under escalating requests |

---

## What Alignment Testing Covers

**Alignment** in this context means: does the model do what it is supposed to do, not do what it is not supposed to do, and remain consistent in its behavior regardless of how a request is framed?

Three dimensions are tested:

1. **Instruction alignment** — Does the model follow its system prompt when user instructions conflict?
2. **Value consistency** — Does the model apply the same judgment to semantically equivalent scenarios presented differently?
3. **Behavioral boundaries** — Does the model maintain safety limits under escalating or reframed requests?

---

## Evaluation Approach

Each test records:

- The system prompt (if applicable)
- The user prompt
- The expected behavior
- The observed behavior
- A pass/fail classification
- Notes on any partial compliance or edge case behavior
