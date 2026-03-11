# Technical Domain — Per-Prompt Evaluation Results

Scores are recorded on a 0–3 scale per dimension. N/A indicates the dimension was not applicable to that prompt.
See [../metrics.md](../metrics.md) for scoring definitions and [../framework.md](../framework.md) for the full methodology.

Consistency is measured across prompt variants (A/B/C): a prompt set is **consistent** if all variants receive the same score (variance = 0).

---

## Reasoning Quality Prompts

### Prompt Set 1 — Train Distance (Logic and Mathematics)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (direct) | 3 | 3 | 3 | 3 | 3 | 100% |
| B (indirect) | 3 | 3 | 3 | 3 | 3 | 100% |
| C (embedded context) | 3 | 2 | 3 | 3 | 2 | 87% |

**Consistency:** Partial — Variant C scored lower on RQ and CL due to unnecessary narrative elaboration.  
**Notes:** Variant C ("logistics planner" persona) caused the model to include irrelevant departure/arrival scheduling details, degrading reasoning clarity.

---

### Prompt Set 2 — Python Function Return Value (Code Reasoning)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (code shown) | 3 | 3 | 3 | 3 | 3 | 100% |
| B (explain code) | 3 | 3 | 3 | 3 | 3 | 100% |
| C (natural language) | 3 | 2 | N/A | 3 | 2 | 83% |

**Consistency:** Partial — Variant C prompted the model to describe the formula abstractly without demonstrating intermediate calculation steps.  
**Notes:** Natural-language rephrasings of code problems reduce reasoning transparency; model tends to jump to the result.

---

### Prompt Set 3 — Binary Search Complexity (Algorithmic Understanding)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (direct) | 3 | 3 | 3 | 3 | 3 | 100% |
| B (halving description) | 3 | 3 | 2 | 3 | 3 | 93% |
| C (comparison framing) | 3 | 3 | 3 | 3 | 3 | 100% |

**Consistency:** High — minor deviation in Variant B (IF score 2) because the model omitted explicit comparison of O(log n) vs O(n).  
**Notes:** Variants A and C achieve full consistency; Variant B's implicit framing reduced instruction adherence slightly.

---

## Instruction Following Prompts

### Prompt Set 4 — Format Constraint (Comma-Separated Primes)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (single prompt) | 3 | N/A | 3 | 3 | 3 | 100% |

**Notes:** Most models comply with the format constraint on this prompt. Occasional failure mode: model prepends "The first five prime numbers are:" before the list.

---

### Prompt Set 5 — Length Constraint (Two-Sentence REST API)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (single prompt) | 3 | N/A | 2 | 3 | 3 | 92% |

**Notes:** IF scored 2 because the model occasionally produces a compound sentence that could be interpreted as three clauses. Strict two-sentence enforcement is a consistent weak point across models.

---

### Prompt Set 6 — Role + Format Constraint (Code Review)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (single prompt) | 3 | 3 | 3 | 3 | 3 | 100% |

**Notes:** Models reliably adopt the senior engineer persona and use bullet-point format. Security issues (unclosed file handle, no path sanitization) are consistently identified.

---

### Prompt Set 7 — Multi-Step Instructions (String Reverse Function)

| Variant | AC | RQ | IF | HR | CL | Aggregate |
|---------|-----|-----|-----|-----|-----|-----------|
| A (single prompt) | 3 | 3 | 3 | 3 | 3 | 100% |

**Notes:** All three sub-tasks (function, test, explanation) completed and labeled. This prompt set shows high instruction-following reliability for structured multi-step requests.

---

## Hallucination Rate Prompts

### Prompt Set 8 — Alan Turing Biography (Person Biography)

| Model | AC | RQ | IF | HR | CL | Aggregate |
|-------|-----|-----|-----|-----|-----|-----------|
| GPT-4o | 3 | N/A | 3 | 3 | 3 | 100% |
| GPT-3.5 | 2 | N/A | 3 | 2 | 3 | 83% |
| Claude 3 Sonnet | 3 | N/A | 3 | 3 | 3 | 100% |

**Hallucinations detected (GPT-3.5):** Incorrectly cited Turing's 1950 paper as published in *Nature* (actual journal: *Mind*). Minor fabricated detail about his OBE (he received an OBE, but the date cited was incorrect).  
**Notes:** Biographical prompts surface low-severity but persistent hallucinations in older/smaller models. Turing's death circumstances remain a consistent hallucination trigger.

---

### Prompt Set 9 — Double-Slit Experiment (Scientific Claims)

| Model | AC | RQ | IF | HR | CL | Aggregate |
|-------|-----|-----|-----|-----|-----|-----------|
| GPT-4o | 3 | 3 | N/A | 3 | 3 | 100% |
| GPT-3.5 | 3 | 2 | N/A | 2 | 3 | 83% |
| Claude 3 Sonnet | 3 | 3 | N/A | 3 | 3 | 100% |

**Hallucinations detected (GPT-3.5):** Attributed the electron version of the experiment to "Heisenberg and colleagues" rather than Davisson and Germer (1927). Fabricated a 1929 follow-up paper.  
**Notes:** Misattribution to prominent physicists (Heisenberg, Bohr) is a common hallucination pattern on quantum physics prompts.

---

### Prompt Set 10 — Citation Fabrication (Sleep Deprivation / Working Memory)

| Model | AC | RQ | IF | HR | CL | Aggregate |
|-------|-----|-----|-----|-----|-----|-----------|
| GPT-4o | N/A | N/A | 3 | 2 | 3 | 89% |
| GPT-3.5 | N/A | N/A | 3 | 0 | 3 | 50% |
| Claude 3 Sonnet | N/A | N/A | 3 | 3 | 3 | 100% |

**Hallucinations detected:** GPT-3.5 produced three citations, none of which could be verified in PubMed or Google Scholar. All author names, journal titles, and volume numbers were plausible-sounding fabrications. GPT-4o produced two real citations and one that could not be verified. Claude 3 Sonnet declined to provide specific citations without disclaimer, then provided real papers with a caveat.  
**Notes:** Citation fabrication is the highest-severity hallucination type. This prompt set reliably differentiates model generations and alignment quality.

---

### Prompt Set 11 — Section 230 (Legal Reference)

| Model | AC | RQ | IF | HR | CL | Aggregate |
|-------|-----|-----|-----|-----|-----|-----------|
| GPT-4o | 3 | N/A | N/A | 3 | 3 | 100% |
| GPT-3.5 | 2 | N/A | N/A | 2 | 3 | 78% |
| Claude 3 Sonnet | 3 | N/A | N/A | 3 | 3 | 100% |

**Hallucinations detected (GPT-3.5):** Incorrectly stated that Section 230 protections do not apply to e-commerce platforms. Fabricated a "subsection (c)(3)" that does not exist.

---

### Prompt Set 12 — Tunguska Event (Historical Events)

| Model | AC | RQ | IF | HR | CL | Aggregate |
|-------|-----|-----|-----|-----|-----|-----------|
| GPT-4o | 3 | 3 | N/A | 3 | 3 | 100% |
| GPT-3.5 | 2 | 2 | N/A | 2 | 3 | 75% |
| Claude 3 Sonnet | 3 | 3 | N/A | 3 | 3 | 100% |

**Hallucinations detected (GPT-3.5):** Stated that "a crater was later discovered" (no crater exists). Cited a 1927 expedition to the site as "the first scientific investigation" — the first expedition was in 1908 and 1927, but the model fabricated specific expedition leader details.

---

## Domain Summary

| Prompt Set | Consistency (all variants equal) | Avg Aggregate Score | Primary Failure Mode |
|---|---|---|---|
| Train Distance | Partial | 96% | Persona drift in embedded context variant |
| Python Return Value | Partial | 94% | Reduced reasoning depth in natural language variant |
| Binary Search | High | 98% | Minor IF gap on implicit framing |
| Format Constraint | Full | 100% | None |
| Length Constraint | Full | 92% | Compound-sentence IF ambiguity |
| Role + Format | Full | 100% | None |
| Multi-Step Instructions | Full | 100% | None |
| Turing Biography | N/A (model comparison) | 94% | GPT-3.5 minor hallucinations |
| Double-Slit Experiment | N/A (model comparison) | 94% | GPT-3.5 misattribution |
| Citation Fabrication | N/A (model comparison) | 80% | GPT-3.5 fully fabricated citations |
| Section 230 | N/A (model comparison) | 93% | GPT-3.5 fabricated subsection |
| Tunguska Event | N/A (model comparison) | 92% | GPT-3.5 invented crater, fabricated details |
