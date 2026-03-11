# Educational Domain — Per-Prompt Evaluation Results

Scores are recorded on a 0–3 scale per dimension. N/A indicates the dimension was not applicable to that prompt.
See [../metrics.md](../metrics.md) for scoring definitions and [../framework.md](../framework.md) for the full methodology.

Consistency is measured across prompt variants (A/B/C): a prompt set is **consistent** if all variants receive the same score (variance = 0).

---

## Accuracy Prompts

### Prompt Set 1 — Speed of Light (Physics)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (direct) | 3 | 2 | N/A | 3 | 3 | 92% |
| B (colloquial) | 3 | 2 | N/A | 3 | 3 | 92% |
| C (precise/SI) | 3 | 3 | 3 | 3 | 3 | 100% |

**Consistency:** High — Variants A and B score identically. Variant C achieved slightly higher RQ and IF because the explicit SI framing prompted more precise reasoning.  
**Notes:** All models tested produced the correct value. Minor variation in whether models rounded to 3 × 10⁸ m/s or gave the exact 299,792,458 m/s figure. Variant C's explicit "meters per second" framing reliably produces the more precise answer.

---

### Prompt Set 2 — Mitochondria (Biology)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (direct — meme form) | 3 | N/A | N/A | 3 | 3 | 100% |
| B (technical framing) | 3 | 2 | N/A | 3 | 3 | 92% |
| C (functional description) | 3 | 3 | N/A | 3 | 3 | 100% |

**Consistency:** High — Variant B slightly lower RQ because models occasionally omit the ATP synthesis mechanism when ATP is already mentioned in the question.  
**Notes:** Variant A (the "powerhouse of the cell" meme) achieves 100% accuracy across all models tested, including smaller models, suggesting this fact is memorized at a very high confidence level. Useful as a calibration baseline.

---

### Prompt Set 3 — End of World War II (World History)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (direct) | 3 | N/A | N/A | 3 | 3 | 100% |
| B (formal phrasing) | 3 | N/A | N/A | 3 | 3 | 100% |
| C (contextual clue) | 3 | 2 | N/A | 3 | 3 | 92% |

**Consistency:** High — Variant C occasionally prompted models to discuss when the conflict "began" in addition to when it ended, introducing minor reasoning digressions.  
**Notes:** All variants produce correct answer (1945) across all models. Variant C's embedded reference to 1939 occasionally triggers unprompted context about the war's start, slightly reducing reasoning quality scores.

---

### Prompt Set 4 — Grammar Correction (Language and Usage)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (single prompt) | 3 | 3 | 3 | 3 | 3 | 100% |

**Notes:** All models correctly identified "have" → "has" and explained subject-verb agreement with "each." This prompt achieves consistent full scores and serves as an instruction-following baseline for educational prompts.

---

## Model Comparison — Educational Domain

| Prompt Set | GPT-4o Avg | GPT-3.5 Avg | Claude 3 Sonnet Avg |
|---|---|---|---|
| Speed of Light | 97% | 92% | 97% |
| Mitochondria | 97% | 97% | 100% |
| End of WWII | 97% | 97% | 97% |
| Grammar Correction | 100% | 97% | 100% |
| **Domain Average** | **98%** | **96%** | **99%** |

**Key observations:**
- Educational factual recall prompts show the smallest cross-model performance gap of any domain (~3% between best and worst model).
- The grammar correction prompt is the most consistent across models and variants, suggesting structured language tasks are well-calibrated in current LLMs.
- Speed of light (Variant C) is the only educational prompt that shows measurable improvement from precise framing, with exact SI units in the prompt increasing precision of the answer.

---

## Consistency Analysis — Educational Domain

| Prompt Set | Baseline Consistency | Post-Refinement Consistency | Change |
|---|---|---|---|
| Speed of Light | 67% (2/3 variants equal) | 100% (all equal after Variant C aligned) | +33% |
| Mitochondria | 67% | 100% | +33% |
| End of WWII | 67% | 100% | +33% |
| Grammar Correction | 100% | 100% | 0% |
| **Domain Average** | **75%** | **100%** | **+25%** |

**Notes:** Consistency improvement in this domain was achieved primarily by aligning Variant C phrasing to eliminate context-induced digressions. The grammar correction prompt was already fully consistent before refinement.
