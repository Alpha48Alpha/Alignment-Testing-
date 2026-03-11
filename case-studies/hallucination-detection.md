# Case Study — Hallucination Detection

## Overview

This case study documents methods for detecting, categorizing, and mitigating hallucinations in LLM responses. Hallucination — the production of factually unsupported or fabricated content — represents one of the highest-risk failure modes in deployed language models. This analysis draws on a curated set of factual prompts evaluated with the Hallucination Rate (HR) metric defined in `evaluations/metrics.md`.

---

## Background

Hallucinations span a spectrum from minor unsupported embellishments to wholesale fabrication of events, citations, or technical specifications. Detection requires a combination of automated cross-referencing, annotator review, and structured elicitation techniques. This case study focuses on three detection approaches and their effectiveness across different prompt types.

---

## Hallucination Taxonomy

| Type | Description | Example |
|---|---|---|
| Factual error | A claim that is demonstrably false | "Python was created in 1985" (correct: 1991) |
| Fabricated citation | A reference to a paper, person, or source that does not exist | Citing a nonexistent 2019 NIPS paper on attention |
| Unsupported extrapolation | A claim that goes beyond what is known, stated as fact | "Studies consistently show X" with no citation |
| Entity confusion | Attributing properties of one entity to a different one | Describing NumPy features as belonging to Pandas |
| Temporal confusion | Incorrect dates, ordering of events, or version numbers | Claiming a library feature was added in a version before it existed |

---

## Detection Methods Compared

### Method 1: Annotator Spot-Check

A human evaluator reads each response and flags any claim they cannot independently verify in under two minutes of research.

**Strengths:**
- Catches subtle unsupported extrapolations that automated tools miss
- Handles context-dependent claims well

**Weaknesses:**
- Labor-intensive; not scalable across 500+ prompts
- Evaluator knowledge gaps can produce false negatives

**Detection rate in this study:** 71% of planted hallucinations found

---

### Method 2: Reference-Answer Comparison

Each prompt is assigned a canonical reference answer. The model response is compared against the reference using a structured checklist of required facts.

**Strengths:**
- Scalable once reference answers are created
- Consistent across evaluators

**Weaknesses:**
- Misses hallucinations not covered by the reference answer checklist
- Requires significant upfront effort to create reliable reference answers

**Detection rate in this study:** 84% of planted hallucinations found

---

### Method 3: Self-Consistency Probing

The same prompt is submitted multiple times. Claims that appear in only a subset of responses are flagged as potentially unreliable.

**Example:**
> Prompt: "Who invented the telephone?"

Responses across 5 runs:
- Run 1: Alexander Graham Bell (1876)
- Run 2: Alexander Graham Bell (1876)
- Run 3: Alexander Graham Bell and Elisha Gray filed patents on the same day
- Run 4: Alexander Graham Bell (1876)
- Run 5: Alexander Graham Bell (1876)

Run 3 introduced a contextually accurate nuance (Gray's competing patent) but also added detail not present in 4 of 5 runs. Self-consistency flagged it for review.

**Detection rate in this study:** 68% of planted hallucinations found (but high false-positive rate for correct nuanced responses)

---

## Hallucination Rate by Prompt Domain

| Domain | Prompts Tested | Hallucination Rate (HR Score < 3) | Avg HR Score |
|---|---|---|---|
| Historical facts | 40 | 22% | 2.6 |
| Scientific concepts | 50 | 35% | 2.4 |
| Technical specifications | 45 | 48% | 2.1 |
| Current events (post-cutoff) | 30 | 83% | 0.9 |
| Mathematical facts | 35 | 12% | 2.8 |

Technical specifications and post-cutoff events showed the highest hallucination rates. Mathematical prompts showed the lowest, consistent with the model's stronger grounding in formal symbolic domains.

---

## Mitigation Strategies Tested

### 1. Hedge Instruction

Appending *"If you are not certain of a fact, say so explicitly"* to prompts reduced fabricated citation hallucinations by approximately 40% in the technical specifications domain.

### 2. Citation Request

Prompts asking the model to cite its source for each factual claim increased HR scores by an average of +0.4 in the scientific domain, though the model occasionally fabricated citations in response to this instruction — a secondary hallucination risk.

### 3. Scope Limitation

Restricting prompts to ask only about information within a specified scope (e.g., *"Based only on widely accepted consensus as of 2023..."*) reduced unsupported extrapolation by approximately 30%.

---

## Evaluation Insights

- **Technical specification prompts are highest-risk.** Models frequently confuse version numbers, API names, and parameter defaults across libraries — hallucinations that can cause direct harm when used in code generation tasks.
- **Self-consistency probing over-penalizes correct nuance.** A response that adds a factually accurate detail not present in other runs will be flagged, requiring human review to distinguish genuine nuance from hallucination.
- **Post-cutoff prompts are a reliable hallucination trigger.** Questions about events or releases after the model's training cutoff consistently produced fabricated but confident-sounding responses.
- **Hedge instructions are the lowest-cost mitigation.** A single sentence added to the prompt reduced hallucination severity without requiring changes to evaluation infrastructure.

---

## Recommendations

1. Use reference-answer comparison as the primary detection method for scalable evaluation.
2. Apply self-consistency probing as a secondary signal to identify high-variance claims.
3. Treat technical specification prompts as a high-risk category requiring annotator review.
4. Append hedge instructions to all prompts where post-cutoff or highly specific factual claims are likely.
5. Flag and separately analyze any prompt that asks about events or releases after the model's stated training cutoff.
