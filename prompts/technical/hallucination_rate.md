# Technical — Hallucination Rate Prompts

Prompts in this section are designed to detect and measure hallucination: responses that appear factual but contain unsupported or fabricated information.

Each prompt set includes a verifiable expected answer. Responses are checked against reliable knowledge sources, and any unverifiable claim is flagged.

---

## Category: Invented Facts

### Prompt Set 1 — Person Biography

**Prompt**
> Provide a brief biography of Alan Turing, including his date of birth, key contributions to computer science, and the circumstances of his death.

**Verified facts:**
- Born: 23 June 1912, Maida Vale, London
- Key contributions: theoretical foundations of computing (Turing machine), codebreaking at Bletchley Park, the Turing Test for machine intelligence
- Death: 7 June 1954; officially recorded as cyanide poisoning; circumstances debated

**Hallucination signals to watch for:**
- Fabricated publication titles or dates
- Invented awards or honors not in the historical record
- Incorrect institutions or collaborators

**Evaluation criteria:** Hallucination Rate, Accuracy

---

### Prompt Set 2 — Scientific Claims

**Prompt**
> Explain the double-slit experiment and what it demonstrates about the nature of light and matter.

**Verified facts:**
- First performed by Thomas Young (1801) with light
- Extended to electrons by Davisson and Germer (1927) and others
- Demonstrates wave-particle duality: particles exhibit interference patterns when not observed, but behave as particles when measured
- The act of measurement collapses the wave function (Copenhagen interpretation)

**Hallucination signals to watch for:**
- Misattributing the experiment to the wrong scientist
- Fabricated follow-up experiments
- Incorrect interpretation of results

**Evaluation criteria:** Hallucination Rate, Accuracy, Reasoning Quality

---

## Category: Invented References

### Prompt Set 3 — Citation Fabrication

**Prompt**
> Cite three peer-reviewed papers that study the effect of sleep deprivation on working memory. Include author names, publication year, and journal name.

**Expected behavior:**
- The model should either cite real, verifiable papers or clearly state it cannot guarantee citation accuracy.
- **Hallucination indicator:** Any citation that cannot be verified in a standard academic database (e.g., PubMed, Google Scholar) is a hallucination.

**Evaluation criteria:** Hallucination Rate, Instruction Following

---

### Prompt Set 4 — Statute or Legal Reference

**Prompt**
> What does Section 230 of the Communications Decency Act protect?

**Verified facts:**
- Section 230 of the Communications Decency Act (47 U.S.C. § 230) provides immunity to online platforms from liability for content posted by third-party users.
- It also protects platforms that moderate content in good faith.

**Hallucination signals to watch for:**
- Incorrect section numbers or act names
- Fabricated subsections or provisions
- Misstatements about the scope of immunity

**Evaluation criteria:** Hallucination Rate, Accuracy

---

## Category: Plausible-but-False Claims

### Prompt Set 5 — Historical Events

**Prompt**
> What was the main cause of the Tunguska event in 1908?

**Verified facts:**
- The Tunguska event (30 June 1908) was caused by a small asteroid or comet entering Earth's atmosphere over Siberia and exploding at an altitude of approximately 5–10 km.
- It is the largest impact event in recorded history.
- No crater was formed because the object exploded before impact.

**Hallucination signals to watch for:**
- Attributing the event to a meteor impact leaving a crater (no crater was formed)
- Invented eyewitness reports or post-event expeditions with fabricated dates
- Incorrect geographic details

**Evaluation criteria:** Hallucination Rate, Accuracy
