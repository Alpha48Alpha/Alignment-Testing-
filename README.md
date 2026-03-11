# LLM Evaluation Research — Alignment Testing

A structured collection of prompts, evaluation frameworks, adversarial tests, and Python tools for measuring LLM behavior across five core dimensions: accuracy, reasoning quality, instruction following, hallucination rate, and clarity.

Built to be used as a reference for designing rigorous LLM evaluations — not as a model leaderboard.

---

## What's Here

| Directory | Contents |
|---|---|
| [`evaluation-framework/`](evaluation-framework/README.md) | Scoring rubric, calibration examples, and evaluation record format |
| [`alignment-tests/`](alignment-tests/README.md) | Behavioral alignment tests covering honesty, value alignment, factual integrity, and bias |
| [`case-studies/`](case-studies/README.md) | Structured analysis of recurring failure modes with examples and diagnostic notes |
| [`prompt-attack-lab/`](prompt-attack-lab/) | Jailbreak tests, prompt injection tests, and defense strategies |
| [`llm-benchmark-design/`](llm-benchmark-design/README.md) | Principles and templates for designing contamination-resistant, construct-valid benchmarks |
| [`experiments/`](experiments/README.md) | Controlled experiments measuring the effect of specific prompt engineering techniques |
| [`python-tools/`](python-tools/README.md) | Python tools for running prompt sets, scoring responses, and measuring consistency |
| [`evaluations/`](evaluations/) | Metric definitions, scoring framework, and per-domain evaluation results |
| [`prompts/`](prompts/) | 500+ prompts organized by domain (technical, educational, general knowledge) |

---

## Five Evaluation Dimensions

| Dimension | Abbreviation | What it measures |
|---|---|---|
| Accuracy | AC | Factual correctness of model responses |
| Reasoning Quality | RQ | Logical coherence and completeness of reasoning steps |
| Instruction Following | IF | Adherence to explicit constraints (format, length, tone, audience) |
| Hallucination Rate | HR | Frequency of unsupported or fabricated claims |
| Clarity | CL | Readability and audience-appropriateness of responses |

Each dimension is scored 0–3. See [`evaluation-framework/README.md`](evaluation-framework/README.md) for the full rubric.

---

## Key Results

| Metric | Baseline | After Refinement | Change |
|---|---|---|---|
| Response consistency | ~52% | ~70% | +35% relative |
| Avg accuracy (technical) | — | 74% | — |
| Avg accuracy (educational) | — | 80% | — |

Consistency is the percentage of prompt variant sets where all variants receive equivalent scores. A 35% relative improvement means 35% more prompt sets achieved full consistency after iterative prompt refinement.

---

## Documented Failure Modes

Five recurring failure patterns are documented with examples in [`case-studies/model-failure-analysis/`](case-studies/model-failure-analysis/README.md):

1. **Confident confabulation** — Plausible-sounding but incorrect specifics stated with false precision
2. **Instruction drift** — Later constraints in multi-constraint prompts dropped or weakened
3. **Reasoning shortcut** — Heuristic answer given without algebraic or logical verification
4. **Sycophantic agreement** — Correct positions abandoned under user pushback
5. **Context window degradation** — Instruction following declining for instructions placed late in long contexts

---

## Prompt Attack Coverage

The [`prompt-attack-lab/`](prompt-attack-lab/) directory covers:

- **Jailbreaks:** instruction override, persona assignment, fictional framing, hypothetical framing, continuation attacks, gradual escalation
- **Injection attacks:** basic injection, credential exfiltration, tool-use hijacking, identity injection, encoding obfuscation
- **Defense strategies:** instruction hierarchy, data/instruction separation, input validation, output monitoring, minimal privilege

---

## Evaluation Methodology

Full methodology: [`evaluation-framework/README.md`](evaluation-framework/README.md)  
Metric definitions: [`evaluations/metrics.md`](evaluations/metrics.md)  
Benchmark design principles: [`llm-benchmark-design/README.md`](llm-benchmark-design/README.md)

