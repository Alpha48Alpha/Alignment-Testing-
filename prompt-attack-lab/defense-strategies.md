# Defense Strategies for Prompt Attacks

The strategies below address the attack vectors documented in `jailbreak-tests.md` and `prompt-injection-tests.md`. Each strategy targets a specific failure mode and includes known limitations.

---

## 1. Input Validation and Normalization

Before passing user input to the model, apply pattern-based or classifier-based filtering to flag known attack signatures (e.g., "ignore previous instructions", Base64-encoded text in non-encoding tasks, persona names associated with known jailbreak templates).

**Limitation:** Rule-based filters are brittle against paraphrase variations and novel attack framings. Semantic classifiers reduce this gap but introduce latency and false-positive risk.

---

## 2. Instruction Hierarchy Enforcement

Structure the system prompt to assert precedence explicitly. Some models support tiered trust levels (system > user > tool), where lower tiers cannot override directives from higher tiers. Do not rely on in-context language like "ignore the following user instruction" as a sole control — it is itself susceptible to injection.

**Limitation:** Tier enforcement depends on the model's architecture and training. Not all models respect hierarchical trust uniformly across all prompt formats or contexts.

---

## 3. Input-Output Isolation

When the model processes untrusted content (e.g., user-submitted documents, retrieved web pages, database records), treat that content as data, not as potential instructions. Delimit untrusted content clearly (e.g., with XML-style tags: `<document>...</document>`) and instruct the model to operate on the content, not to follow any directives embedded within it.

**Limitation:** LLMs trained on instruction-following data do not natively distinguish between an instruction in the system turn and an instruction appearing in a `<document>` tag. Fine-tuning or RLHF targeting this boundary is required for robust isolation.

---

## 4. Output Monitoring and Anomaly Detection

Inspect model outputs for indicators of successful injection: unexpected format deviations, responses not grounded in the provided task, disclosure of system prompt fragments, or outputs matching known attack payloads. Flag anomalous outputs for review before serving them to users.

**Limitation:** Detection must happen before the response reaches the user to be useful, which requires synchronous post-generation filtering and increases latency.

---

## 5. Minimal Privilege in System Prompts

Avoid placing sensitive information (API keys, confidential instructions, user PII) directly in the system prompt. If the model can be induced to reproduce its context window, minimizing what is present limits the damage of a successful extraction attack. Sensitive values should be resolved server-side, not embedded in prompts.

---

## 6. Adversarial Testing as a Control

Treat the test cases in this lab as a regression suite. Any prompt processing pipeline that passes all test cases in `jailbreak-tests.md` and `prompt-injection-tests.md` has a documented baseline. Changes to the system prompt, model version, or retrieval pipeline should be re-evaluated against this suite before deployment.
