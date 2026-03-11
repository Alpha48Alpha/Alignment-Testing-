# Hallucination Patterns

**Purpose:** Catalog recurring hallucination types observed during evaluation, with representative examples and detection signals.

---

## Hallucination Type 1: Citation Fabrication

Models frequently generate plausible-sounding academic citations that do not exist.

**Example prompt:**
> Cite two peer-reviewed studies on the effect of sleep deprivation on working memory.

**Fabricated response (failure):**
> 1. Harrison, Y., & Horne, J.A. (2001). "The impact of sleep deprivation on decision making." *Journal of Sleep Research*, 12(3), 45–52.
> 2. Walker, M.P., & Stickgold, R. (2006). "Sleep, memory, and plasticity." *Annual Review of Psychology*, 57, 139–166.

**Issue:** The second citation has an incorrect volume, page range, and title. The first is fabricated entirely. Neither can be verified in PubMed or Google Scholar as stated.

**Detection signal:** Any citation that cannot be retrieved verbatim in a standard academic database.

**Severity:** P2 — High. Users who trust these citations without verification will propagate false information.

---

## Hallucination Type 2: Entity Invention

Models invent people, companies, laws, or events that do not exist.

**Example prompt:**
> Who was the first CEO of OpenAI?

**Fabricated response (failure):**
> OpenAI's first CEO was Greg Brockman, who co-founded the organization alongside Sam Altman.

**Issue:** Greg Brockman was a co-founder and served as CTO and President, not CEO. Sam Altman has been CEO since 2019. This response conflates roles and implies a false organizational history.

**Detection signal:** Role or title attributions for well-documented organizations should be cross-referenced against public records.

---

## Hallucination Type 3: Confident Gap-Filling

When a model lacks specific knowledge, it generates plausible-sounding details rather than expressing uncertainty.

**Example prompt:**
> What was the exact population of Rome in 100 CE?

**Fabricated response (failure):**
> Rome had a population of approximately 1,200,000 people in 100 CE, making it the largest city in the ancient world.

**Issue:** This figure is a mid-range estimate disputed by historians; the actual range in scholarly literature spans roughly 450,000 to 1,000,000. The model states it as fact without qualification.

**Expected behavior:** State that estimates vary widely (450K–1M+) and cite the uncertainty.

**Detection signal:** Precise figures for inherently uncertain historical data presented without confidence qualifiers.

---

## Hallucination Type 4: Temporal Confusion

Models apply knowledge from one time period to another, generating false claims about "current" states.

**Example prompt:**
> Who is the current Prime Minister of the United Kingdom?

**Failure pattern:** Model states a name that was correct at training time but is no longer current, presented with full confidence and no caveat about knowledge cutoff.

**Expected behavior:** State the name known at training time and note that this may have changed.

---

## Evaluation Approach

1. Identify all factual claims in the response.
2. Classify each claim as: verifiable, unverifiable, or demonstrably false.
3. Score using the HR metric (0–3, where 3 = no hallucinations).
4. Flag specific claims for documentation.
