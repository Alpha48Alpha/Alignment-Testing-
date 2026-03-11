# EXP-002: Instruction Following Under Multiple Constraints

**Date:** November 2024  
**Model:** GPT-4o (gpt-4o-2024-08-06)  
**Prompt set:** Technical / Instruction Following  
**Objective:** Measure how compliance rate changes as the number of simultaneous constraints increases from 1 to 4.

---

## Conditions

- Temperature: 0
- System prompt: None
- Runs per variant: 1
- Constraint sets: 4 variants of 10 different prompt topics = 40 total responses
- Scoring: binary pass/fail per constraint per response

---

## Results

| Constraint count | Prompts | Full compliance | Partial compliance | Non-compliance |
|---|---|---|---|---|
| 1 constraint | 10 | 9 (90%) | 1 (10%) | 0 (0%) |
| 2 constraints | 10 | 8 (80%) | 2 (20%) | 0 (0%) |
| 3 constraints | 10 | 6 (60%) | 3 (30%) | 1 (10%) |
| 4 constraints | 10 | 4 (40%) | 4 (40%) | 2 (20%) |

**Full compliance** = all constraints satisfied  
**Partial compliance** = at least one constraint satisfied, at least one violated  
**Non-compliance** = zero or one constraint satisfied

---

## Constraint Failure Distribution

Which constraints were most frequently dropped?

| Constraint type | Violation rate |
|---|---|
| Maximum length | 38% |
| Audience level ("for a non-technical audience") | 31% |
| Analogy requirement | 45% |
| No mathematical notation | 22% |

Constraints appearing **last** in the prompt were violated ~2× more often than constraints appearing **first**.

---

## Observations

- Length was the most commonly violated constraint class when prompt length was the last stated constraint.
- Moving the length constraint to the first position in the prompt reduced violations for that constraint by approximately 40%.
- The model never acknowledged that it had violated a constraint. Responses appeared confident and complete.

---

## Conclusion

Multi-constraint compliance degrades measurably beyond two simultaneous constraints. Constraint position matters: later constraints are dropped more often. Prompts with three or more constraints should be tested in isolation and in combination before deployment.
