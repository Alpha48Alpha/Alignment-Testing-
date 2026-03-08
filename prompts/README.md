# Prompts

500+ LLM evaluation prompts organized by domain. Each domain folder is structured as a self-contained collection that can be extracted into its own repository.

## Domain Collections

| Domain | Folder | Focus |
|---|---|---|
| Technical | [`technical/`](technical/) | Programming, mathematics, logic puzzles, and system reasoning |
| Educational | [`educational/`](educational/) | Science, history, language, and conceptual explanations |
| General Knowledge | [`general/`](general/) | Everyday reasoning, common sense, and world knowledge |

## Prompt Format

Each prompt file follows this structure:

- A top-level `#` heading naming the domain and metric.
- Prompts grouped into named **Prompt Sets** with multiple **Variants** (A, B, C) — equivalent rephrasings.
- Each set includes an **Expected answer** and **Evaluation criteria**.

## Evaluation

Each response is scored 0–3 on each applicable metric. See [`../evaluations/metrics.md`](../evaluations/metrics.md) for metric definitions and [`../evaluations/framework.md`](../evaluations/framework.md) for the full scoring methodology.

## Results

Aggregate scores and per-domain results are stored in [`../evaluations/results/`](../evaluations/results/).
