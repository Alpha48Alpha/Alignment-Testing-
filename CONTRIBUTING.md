# Contributing to Alignment-Testing-

Thank you for your interest in contributing! We welcome contributions from everyone.

## How to Contribute

### Reporting Issues

If you find a problem or have a suggestion, please open an issue with:

- A clear and descriptive title
- A detailed description of the issue or suggestion
- Steps to reproduce (if applicable)
- Expected behavior vs. actual behavior
- Any relevant context or examples

### Adding New Prompts

1. Choose the appropriate domain folder under `prompts/` (`technical/`, `educational/`, or `general/`).
2. Edit or create the relevant metric file (e.g., `accuracy.md`, `reasoning_quality.md`).
3. Follow the existing prompt set format:
   - Include at least two variants (Variant A, Variant B, etc.) as blockquotes
   - Provide an **Expected answer**
   - List relevant **Evaluation criteria** (Accuracy, Reasoning Quality, Instruction Following, Hallucination Rate, Clarity)
4. Update `evaluations/results/` with any new evaluation data.

### Submitting Pull Requests

1. Fork the repository
2. Create a new branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Commit your changes with a clear, descriptive commit message:
   ```bash
   git commit -m "Add feature: description of your change"
   ```
5. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a pull request against the `main` branch

### Prompt File Format

Each prompt file follows this structure:

- A top-level `#` heading naming the domain and metric (e.g., `# Technical — Reasoning Quality Prompts`).
- Prompts are grouped into named **Prompt Sets** with multiple **Variants** representing equivalent rephrasings.
- Each variant is a blockquote `>` containing the prompt text.
- Each prompt set includes an **Expected answer** and **Evaluation criteria**.

### Scoring

Each prompt response is scored 0–3 on each applicable metric. See [`evaluations/metrics.md`](evaluations/metrics.md) for per-metric scoring guidance and [`evaluations/framework.md`](evaluations/framework.md) for the full methodology.

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
