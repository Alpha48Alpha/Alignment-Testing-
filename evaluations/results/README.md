# Evaluation Results

This directory contains evaluation results for prompt sets in this repository.

Results are organized by domain and evaluation run. Each results file records per-prompt scores across the five dimensions: Accuracy (AC), Reasoning Quality (RQ), Instruction Following (IF), Hallucination Rate (HR), and Clarity (CL).

See [../framework.md](../framework.md) for the full evaluation methodology and scoring rubric.

---

## Summary

| Domain | Prompts Evaluated | Avg Consistency Score | Avg Accuracy Score |
|---|---|---|---|
| Technical | ~200 | 68% | 74% |
| Educational | ~150 | 71% | 80% |
| General Knowledge | ~150 | 72% | 76% |
| Technical — Agent Dispatch (Media Workflow) | 27 | 94% | 93% |
| **Total / Overall** | **~500+** | **~70%** | **~76%** |

Baseline consistency (before prompt refinement): ~52%  
Improved consistency (after prompt refinement): ~70%  
Relative improvement: **+35%**

---

## Agent Dispatch Results

Results for the Agent OS — Agent Dispatch and Media-Building Workflow prompt set are in [`agent_dispatch_results.md`](agent_dispatch_results.md).
