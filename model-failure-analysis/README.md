# Model Failure Analysis

Documentation of recurring failure modes observed during evaluation. Each file covers a specific failure category with representative examples, detection methods, and notes on severity.

---

## Failure Categories

| File | Failure Type |
|---|---|
| [`hallucination-patterns.md`](hallucination-patterns.md) | Fabricated facts, citations, and entities |
| [`refusal-errors.md`](refusal-errors.md) | Over-refusal and under-refusal cases |
| [`sycophancy.md`](sycophancy.md) | Agreement bias and capitulation under social pressure |
| [`specification-gaming.md`](specification-gaming.md) | Technically compliant but intent-violating responses |

---

## Taxonomy

```
Model Failures
├── Factual Errors
│   ├── Hallucination (unsupported claims)
│   └── Confabulation (coherent but false narratives)
├── Instruction Failures
│   ├── Over-refusal (refusing benign requests)
│   ├── Under-refusal (complying with harmful requests)
│   └── Constraint violation (ignoring format/length/tone)
├── Reasoning Failures
│   ├── Logical gaps
│   ├── Wrong conclusion from correct premises
│   └── Circular reasoning
└── Alignment Failures
    ├── Sycophancy
    ├── Specification gaming
    └── Goal misgeneralization
```

---

## Severity Scale

| Level | Description |
|---|---|
| **P1 — Critical** | Safety boundary violated; harmful content produced |
| **P2 — High** | Materially false information presented with confidence |
| **P3 — Medium** | Instruction violated or reasoning flawed but not harmful |
| **P4 — Low** | Minor clarity or formatting issue |
