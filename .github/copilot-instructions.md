# Copilot Instructions

## Repository Overview

This is the **Alignment-Testing-** repository — a collection of 500+ prompts designed to evaluate LLM safety, robustness, and alignment across technical, educational, and general knowledge domains.

## Agent Instructions

When working in this repository, Copilot should:

### Portfolio
- Maintain and update `index.html` at the root of the repository as the owner's portfolio page.
- The portfolio automatically fetches and displays public GitHub repositories for the owner (`Alpha48Alpha`) using the GitHub REST API.
- When adding new features to the portfolio, keep the styling consistent with the existing dark-theme, card-based layout.
- The portfolio should always reflect the most up-to-date list of repositories without requiring manual edits — new repos appear automatically via the API fetch.
- To preview the portfolio locally, open `index.html` directly in a browser or serve it with `python3 -m http.server` from the repository root.

### Prompts & Evaluations
- All prompts live under `prompts/` organized by domain (`technical/`, `educational/`, `general/`).
- Evaluation definitions are in `evaluations/metrics.md` and `evaluations/framework.md`.
- Results go in `evaluations/results/`.
- Prompt attack test cases live in `prompt-attack-lab/`.

#### Prompt File Format
Each prompt file follows this structure:
- A top-level `#` heading naming the domain and metric (e.g., `# Technical — Reasoning Quality Prompts`).
- Prompts are grouped into named **Prompt Sets** with multiple **Variants** (Variant A, B, C) representing equivalent rephrasings.
- Each prompt set includes an **Expected answer** and **Evaluation criteria** (one or more of: Accuracy, Reasoning Quality, Instruction Following, Hallucination Rate, Clarity).
- Each variant is a blockquote `>` containing the prompt text.

#### Adding New Prompts
1. Choose the appropriate domain folder under `prompts/` (`technical/`, `educational/`, or `general/`).
2. Edit or create the relevant metric file (e.g., `accuracy.md`, `reasoning_quality.md`).
3. Follow the existing prompt set format: include at least two variants, an expected answer, and evaluation criteria.
4. Update `evaluations/results/` with any new evaluation data.

#### Scoring
Each prompt response is scored 0–3 on each applicable metric. The aggregate score is:
```
Aggregate = sum(applicable_metric_scores) / (number_of_applicable_metrics × 3) × 100%
```
See `evaluations/metrics.md` for per-metric scoring guidance and `evaluations/framework.md` for the full methodology.

### Prompt Attack Lab
- `prompt-attack-lab/jailbreak-tests.md` — adversarial prompts that attempt to override model safety policies.
- `prompt-attack-lab/prompt-injection-tests.md` — prompts that attempt to inject instructions into model context.
- `prompt-attack-lab/defense-strategies.md` — recommended mitigations and defense techniques.
- When adding new attack test cases, include: the **Prompt**, an **Evaluation Goal**, and the **Expected Safe Behavior**.

### Code Style
- Use plain Markdown (`.md`) for all documentation files.
- Use semantic HTML5 and vanilla CSS/JavaScript (no build tools or frameworks) for the portfolio page.
- Keep JavaScript self-contained in `index.html` using `<script>` tags.

### Conventions
- Commit messages should be short and descriptive (imperative mood).
- Do not introduce new dependencies or package managers.
- Do not modify `.github/agents/` — those files are reserved for agent-specific configurations.
