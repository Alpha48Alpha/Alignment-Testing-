# Datasets

This directory holds curated prompt datasets and notes on their sources, licenses, and intended use.

## Dataset Policy

- All datasets used in this lab must be documented here with provenance information.
- Prefer open-licensed sources (CC-BY, CC0, public domain). Document the license for every dataset.
- Do not commit large binary files; store raw data in cloud storage and link here.
- Derived/preprocessed datasets may be committed if they are small (< 1 MB per file).

## Directory Layout

```
datasets/
  <dataset-slug>/
    README.md       # Source, license, description, and preprocessing notes
    data.json       # Processed data file (if small enough to commit)
```

## Dataset Note Format

Each `README.md` inside a dataset folder should include:

| Field | Description |
|---|---|
| **Source** | Original URL or citation |
| **License** | License type and URL |
| **Description** | What the dataset contains and how it was collected |
| **Preprocessing** | Any transformations applied before committing |
| **Usage** | Which benchmarks or experiments use this dataset |

## Example

```
datasets/
  widget-counting/
    README.md     # Hand-crafted widget arithmetic problems
    data.json     # 20 widget counting prompts with ground-truth answers
```
