# EXP-001: Hallucination Rate in Citation Prompts

**Date:** November 2024  
**Model:** GPT-4o (gpt-4o-2024-08-06)  
**Prompt set:** Technical / Hallucination Rate  
**Objective:** Measure how frequently the model fabricates academic citations when asked to provide peer-reviewed references.

---

## Conditions

- Temperature: 0
- System prompt: None
- Runs per prompt: 1 (deterministic at temp=0)
- Prompts run: 12 citation requests across domains (neuroscience, ML, medicine, history)

---

## Results

| Category | Prompts | Citations requested | Unverifiable citations | Fabrication rate |
|---|---|---|---|---|
| Neuroscience | 3 | 9 | 6 | 67% |
| Machine learning | 3 | 9 | 4 | 44% |
| Medicine | 3 | 9 | 7 | 78% |
| History | 3 | 9 | 5 | 56% |
| **Total** | **12** | **36** | **22** | **61%** |

---

## Observations

- Fabricated citations were structurally plausible: correct journal name formats, author name patterns, reasonable year ranges.
- In 8 of 22 fabricated citations, the author names were real researchers in the field — but the paper title and/or year was invented.
- The model provided no disclaimer about citation reliability in 10 of 12 prompts.
- In 2 prompts, the model added a caveat: "Please verify these citations as I may not have access to the most current publications." These 2 prompts still contained fabricated references.

---

## Conclusion

Citation requests are a high-risk hallucination vector. The model produces structurally plausible but factually unreliable citations at a rate of ~60%. The fabrications are difficult to detect without cross-referencing against an academic database because they use real author names and plausible journal formats.

**Recommendation:** Prompts that require citations should be accompanied by explicit instruction to state uncertainty, and outputs should not be used without database verification.
