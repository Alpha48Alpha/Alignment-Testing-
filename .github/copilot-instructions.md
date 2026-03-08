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

### Prompts & Evaluations
- All prompts live under `prompts/` organized by domain (`technical/`, `educational/`, `general/`).
- Evaluation definitions are in `evaluations/metrics.md` and `evaluations/framework.md`.
- Results go in `evaluations/results/`.
- Prompt attack test cases live in `prompt-attack-lab/`.

### Code Style
- Use plain Markdown (`.md`) for all documentation files.
- Use semantic HTML5 and vanilla CSS/JavaScript (no build tools or frameworks) for the portfolio page.
- Keep JavaScript self-contained in `index.html` using `<script>` tags.

### Conventions
- Commit messages should be short and descriptive (imperative mood).
- Do not introduce new dependencies or package managers.
- Do not modify `.github/agents/` — those files are reserved for agent-specific configurations.
