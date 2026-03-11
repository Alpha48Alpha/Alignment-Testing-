# Model Failure Analysis — Instruction-Following Failures

## Overview

This document analyzes cases where language models failed to adhere to explicit prompt constraints. Instruction-following failures are evaluated using the Instruction Following (IF) metric defined in `evaluations/metrics.md`. They are particularly consequential in production settings where output format, length, or tone is required to meet downstream integration requirements.

---

## Categories of Instruction-Following Failure

| Category | Description |
|---|---|
| Format violation | Output uses a different structure than specified (e.g., prose instead of a list) |
| Length violation | Response exceeds or falls short of a word or sentence count constraint |
| Tone mismatch | Formal language requested but casual language produced, or vice versa |
| Partial completion | The model addresses only some parts of a multi-part instruction |
| Constraint addition | The model introduces unrequested elements (e.g., unsolicited caveats) |
| Constraint omission | A required section or element is absent from the output |

---

## Failure Case 1: Format Violation

### Prompt

> List the five main causes of World War I. Use a numbered list with one sentence per item. Do not include introductory or concluding sentences.

### Model Response

> World War I had many complex causes that historians have analyzed for decades. The main causes include: 1. The system of military alliances between European powers. 2. Intense nationalism across European nations. 3. Imperial competition for overseas territories and resources. 4. The arms race, particularly between Britain and Germany. 5. The assassination of Archduke Franz Ferdinand, which served as the immediate trigger. These factors combined to create the conditions for a devastating global conflict.

### Analysis

The model added both an introductory sentence and a concluding sentence, directly violating the explicit constraint. The numbered list was present and the content was accurate, but the extraneous framing lowered the IF score.

**IF Score: 2** (five required items present; two prohibited elements added)

---

## Failure Case 2: Length Violation

### Prompt

> Summarize the water cycle in exactly three sentences.

### Model Response

> Water evaporates from oceans, lakes, and rivers when heated by the sun, turning from liquid to water vapor. This vapor rises into the atmosphere, where it cools and condenses around tiny dust particles to form clouds. When water droplets in clouds combine and grow heavy enough, they fall back to Earth as precipitation — rain, snow, or hail — and the cycle begins again. Water that falls on land may be absorbed by soil, run off into rivers, or be taken up by plants, eventually returning to the atmosphere through transpiration.

### Analysis

The response contains four sentences, violating the "exactly three sentences" constraint. The fourth sentence, while informative, was not requested. This failure type is common when the model interprets additional detail as helpful rather than as a constraint violation.

**IF Score: 1** (three-sentence constraint violated; content accurate; structure otherwise appropriate)

---

## Failure Case 3: Tone Mismatch

### Prompt

> Explain the concept of compound interest in a formal, academic tone suitable for a university economics textbook.

### Model Response

> So, compound interest is basically when you earn interest not just on your original money but also on the interest you've already earned. Think of it like a snowball rolling downhill — it gets bigger as it picks up more snow. Pretty cool, right?

### Analysis

The response used informal language ("basically," "Pretty cool, right?"), a colloquial analogy, and a conversational sentence structure — all incompatible with a formal academic tone. The core concept was correct, but the response would be entirely unsuitable for a textbook.

**IF Score: 0** (tone constraint completely unmet)

---

## Failure Case 4: Partial Completion

### Prompt

> Provide three things: (1) a definition of machine learning, (2) one real-world application, and (3) one limitation of current machine learning systems.

### Model Response

> Machine learning is a subset of artificial intelligence where systems learn from data to improve their performance over time without being explicitly programmed. It is widely used in recommendation systems, such as those used by streaming services to suggest content.

### Analysis

The model provided the definition (1) and a real-world application (2) but omitted the limitation (3). This is a partial completion failure — common when the model treats a multi-part instruction as complete after fulfilling the most prominent parts.

**IF Score: 1** (two of three required parts present)

---

## Failure Case 5: Constraint Addition

### Prompt

> Translate the following sentence to Spanish: "The library closes at 9 PM." Provide only the translation.

### Model Response

> Here is the translation: "La biblioteca cierra a las 9 PM." Note: In some Spanish-speaking regions, "PM" may be expressed as part of a 24-hour clock.

### Analysis

The model added an unsolicited note about regional variation despite the instruction specifying "only the translation." The note itself is factually accurate, but it violates the output scope constraint.

**IF Score: 2** (correct translation provided; unrequested addendum included)

---

## Frequency Summary

| Failure Category | Occurrences (n=100 prompts) | % of Total |
|---|---|---|
| Constraint addition | 29 | 29% |
| Partial completion | 22 | 22% |
| Format violation | 19 | 19% |
| Length violation | 15 | 15% |
| Tone mismatch | 10 | 10% |
| No failure observed | 5 | 5% |

Constraint addition was the most prevalent failure, suggesting that models have a strong prior toward providing more context than requested. Tone mismatch, while least common, was the most severe when it occurred (consistently IF Score: 0).

---

## Evaluation Insights

- **Constraint addition is underweighted in naive evaluations.** Evaluators focused on content accuracy may overlook added caveats and disclaimers that violate scope instructions.
- **Multi-part instructions should be numbered.** Unnumbered lists of requirements had a partial completion rate approximately twice that of explicitly numbered requirements.
- **Tone constraints require explicit anchoring.** Providing a reference example of the target tone ("Write in the same style as the following passage: ...") reduced tone mismatch failures by approximately 50% in follow-up testing.
- **"Only" and "exactly" are high-value constraint words.** Prompts that included these terms had a 35% lower constraint-addition rate compared to prompts that used weaker phrasings like "please include."

---

## Recommended Prompt Patterns

| Failure Type | Recommended Fix |
|---|---|
| Format violation | Specify prohibited elements explicitly: "Do not include introductions or conclusions." |
| Length violation | Use "exactly N sentences" rather than "about N sentences" |
| Tone mismatch | Provide a tone anchor or reference passage |
| Partial completion | Number all required parts; end with "Ensure all N parts are present." |
| Constraint addition | Use "Provide only X" rather than "Provide X" |
