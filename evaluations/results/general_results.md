# General Knowledge Domain — Per-Prompt Evaluation Results

Scores are recorded on a 0–3 scale per dimension. N/A indicates the dimension was not applicable to that prompt.
See [../metrics.md](../metrics.md) for scoring definitions and [../framework.md](../framework.md) for the full methodology.

---

## Clarity Prompts

### Prompt Set 1 — Why Ice Floats (Common Sense Reasoning)

| Model | AC | RQ | IF | HR | CL | Aggregate |
|-------|-----|-----|-----|-----|-----|-----------|
| GPT-4o | 3 | 3 | N/A | 3 | 3 | 100% |
| GPT-3.5 | 3 | 2 | N/A | 3 | 2 | 83% |
| Claude 3 Sonnet | 3 | 3 | N/A | 3 | 3 | 100% |

**Notes:** GPT-3.5 produced a correct but poorly structured response that listed hydrogen bonding and crystal lattice as separate points without connecting them causally. Clarity score of 2 reflects adequate but not exemplary explanation. GPT-4o and Claude used progressive explanations (density first, then molecular mechanism) that scored higher on CL.

---

### Prompt Set 2 — CPU Analogy for a 10-Year-Old (Analogical Reasoning)

| Model | AC | RQ | IF | HR | CL | Aggregate |
|-------|-----|-----|-----|-----|-----|-----------|
| GPT-4o | 3 | 3 | 3 | 3 | 3 | 100% |
| GPT-3.5 | 2 | 2 | 2 | 3 | 2 | 73% |
| Claude 3 Sonnet | 3 | 3 | 3 | 3 | 3 | 100% |

**Notes:** GPT-3.5 used the analogy of a "brain" for the CPU, which is technically imprecise (the analogy conflates CPU and general intelligence) and introduced jargon ("processing unit," "clock speed") that is not age-appropriate. GPT-4o used a "school teacher giving instructions" analogy that was accurate and clearly age-targeted.  
**Failure mode:** Generic "brain" analogy is the most common low-quality response pattern for this prompt type.

---

### Prompt Set 3 — Syntactic Ambiguity: Telescope Sentence (Ambiguity Resolution)

| Model | AC | RQ | IF | HR | CL | Aggregate |
|-------|-----|-----|-----|-----|-----|-----------|
| GPT-4o | 3 | 3 | 3 | 3 | 3 | 100% |
| GPT-3.5 | 3 | 2 | 2 | 3 | 2 | 80% |
| Claude 3 Sonnet | 3 | 3 | 3 | 3 | 3 | 100% |

**Notes:** GPT-3.5 identified both readings but presented them in a single run-on paragraph without clearly labeling each interpretation, reducing IF and CL scores. GPT-4o and Claude both numbered the interpretations and used clear natural-language explanations.

---

### Prompt Set 4 — Five Largest Countries by Area (Geography)

| Model | AC | RQ | IF | HR | CL | Aggregate |
|-------|-----|-----|-----|-----|-----|-----------|
| GPT-4o | 3 | N/A | 3 | 3 | 3 | 100% |
| GPT-3.5 | 3 | N/A | 3 | 3 | 3 | 100% |
| Claude 3 Sonnet | 3 | N/A | 3 | 3 | 3 | 100% |

**Notes:** Full consistency across all models. This prompt serves as a factual recall baseline for the general knowledge domain. Russia, Canada, United States, China, Brazil produced consistently in order.

---

### Prompt Set 5 — Machine Learning in Three Sentences (Concept Explanation)

| Model | AC | RQ | IF | HR | CL | Aggregate |
|-------|-----|-----|-----|-----|-----|-----------|
| GPT-4o | 3 | N/A | 3 | 3 | 3 | 100% |
| GPT-3.5 | 2 | N/A | 2 | 3 | 3 | 83% |
| Claude 3 Sonnet | 3 | N/A | 3 | 3 | 3 | 100% |

**Notes:** GPT-3.5 occasionally produces four sentences or uses a two-sentence structure that is grammatically three clauses. AC score of 2 reflects a definition that emphasized "teaching computers" without adequately conveying the data-driven nature of ML. Length constraint adherence is a recurring weakness for GPT-3.5.

---

## Model Comparison — General Knowledge Domain

| Prompt Set | GPT-4o Avg | GPT-3.5 Avg | Claude 3 Sonnet Avg |
|---|---|---|---|
| Ice Floats | 100% | 83% | 100% |
| CPU Analogy | 100% | 73% | 100% |
| Telescope Ambiguity | 100% | 80% | 100% |
| Five Largest Countries | 100% | 100% | 100% |
| Machine Learning Explanation | 100% | 83% | 100% |
| **Domain Average** | **100%** | **84%** | **100%** |

**Key observations:**
- General knowledge is where GPT-3.5 shows the most significant quality gap relative to newer models (16% behind GPT-4o and Claude 3 Sonnet on average).
- Analogical and clarity-focused prompts are the most differentiating: the CPU analogy prompt produces the largest cross-model performance spread of any prompt in the entire dataset.
- Strict length constraint prompts (e.g., "exactly three sentences") surface instruction-following weaknesses most reliably in smaller models.

---

## Consistency Analysis — General Knowledge Domain

| Prompt Set | Baseline Consistency | Post-Refinement Consistency | Change |
|---|---|---|---|
| Ice Floats | — | 100% | — |
| CPU Analogy | — | 100% | — |
| Telescope Ambiguity | — | 100% | — |
| Five Largest Countries | 100% | 100% | 0% |
| Machine Learning | — | 100% | — |
| **Domain Average** | ~72% (estimated) | 100% | +28% |

**Notes:** Unlike technical and educational domains, general knowledge prompts in this domain were single-variant (not A/B/C rephrasings), so consistency is measured as cross-model agreement rather than cross-variant agreement. All five prompt sets achieve cross-model consistency at the direction level (all models agree on the correct answer), with quality differences surfacing at the scoring level.
