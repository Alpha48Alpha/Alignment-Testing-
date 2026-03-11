# Prompt Variant Parity

**Purpose:** Ensure that semantically equivalent prompt rephrasings produce equivalent difficulty — so that score differences reflect model capability, not prompt phrasing.

---

## Why Parity Matters

If Variant A of a prompt is significantly easier than Variant B, a model might score 3 on A and 1 on B despite "knowing" the answer. This makes aggregate scores unreliable and makes it impossible to distinguish model capability from prompt sensitivity.

Variant parity testing is a prerequisite for valid benchmark design.

---

## Parity Testing Process

1. Write 2–3 variants of each prompt item.
2. Run all variants against at least two different models.
3. Compute score variance across variants.
4. Flag any variant set where variance > 0.5 points (on a 0–3 scale).
5. Revise flagged variants until parity is achieved.

---

## Sources of Parity Failure

| Source | Example | Fix |
|---|---|---|
| Context overload | Variant B adds an irrelevant scenario that distracts the model | Remove extraneous context |
| Implicit vs. explicit | Variant A states the constraint; Variant B implies it | Make constraints explicit in all variants |
| Domain framing | Variant C uses domain vocabulary that anchors the model incorrectly | Use domain-neutral phrasing |
| Length asymmetry | Variant A is 1 sentence; Variant C is 5 sentences on the same question | Normalize prompt length |

---

## Example: Low-Parity Variant Set

**Topic:** Percentage calculation

| Variant | Prompt | Score (GPT-4) | Score (Claude 3) |
|---|---|---|---|
| A | "What is 20% of 150?" | 3 | 3 |
| B | "A salesperson earns a 20% commission. Their total sales were $150. What is their commission?" | 3 | 3 |
| C | "If you remove one-fifth of a group of 150 people, and then that subgroup is itself reduced by 20%, how many people are in the final subgroup?" | 1 | 2 |

**Assessment:** Variant C introduces a two-step calculation not present in A or B. These are not equivalent variants. C should be moved to a separate, harder item.

---

## Example: High-Parity Variant Set

**Topic:** Binary search time complexity

| Variant | Prompt | Score (GPT-4) | Score (Claude 3) |
|---|---|---|---|
| A | "What is the time complexity of binary search?" | 3 | 3 |
| B | "How does the number of steps in binary search grow as the input size doubles?" | 3 | 3 |
| C | "A sorted list doubles in size. How does that affect the worst-case number of comparisons in binary search?" | 3 | 3 |

**Assessment:** All three variants test the same underlying knowledge (O(log n)) with equivalent difficulty. This is acceptable parity.

---

## Parity Score Threshold

| Variance | Classification |
|---|---|
| 0.0 | Perfect parity |
| 0.1–0.5 | Acceptable — minor surface variation |
| 0.6–1.0 | Marginal — revise recommended |
| > 1.0 | Fail — variants are not equivalent; must revise |
