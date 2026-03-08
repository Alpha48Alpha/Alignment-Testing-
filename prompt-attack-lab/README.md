# Prompt Attack Lab

Adversarial prompt test cases and defense strategies for LLM safety evaluation. This collection covers jailbreak attempts, prompt injection attacks, and recommended mitigations.

## Contents

| File | Description |
|---|---|
| [`jailbreak-tests.md`](jailbreak-tests.md) | Prompts that attempt to override a model's safety policies |
| [`prompt-injection-tests.md`](prompt-injection-tests.md) | Prompts that attempt to inject malicious instructions into model context |
| [`defense-strategies.md`](defense-strategies.md) | Recommended mitigations and defense techniques |

## Test Case Format

Each test case includes:

- **Prompt** — the adversarial input
- **Evaluation Goal** — what the test is checking for
- **Expected Safe Behavior** — the response a well-aligned model should produce

## Adding New Test Cases

1. Choose the appropriate file (`jailbreak-tests.md` or `prompt-injection-tests.md`).
2. Add a new numbered test case following the existing format.
3. Include the **Prompt**, **Evaluation Goal**, and **Expected Safe Behavior**.
4. If a new defense mitigation is discovered, document it in `defense-strategies.md`.

## Relationship to Evaluation Framework

Attack test cases are evaluated against the same five-metric framework used for standard prompts. See [`../evaluations/framework.md`](../evaluations/framework.md) for scoring guidance.
