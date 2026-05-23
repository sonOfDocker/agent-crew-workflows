# Story Workflow Golden Path Demo

This directory contains a "golden path" demo that demonstrates the MVP story readiness workflow from input files to generated artifacts.

## Purpose

The goal of this demo is to provide a concrete, reproducible example of how the workflow works. It helps developers and reviewers understand:
- What input files should look like.
- How to execute the workflow runner.
- What output artifacts are produced.
- How guardrails and human-review requirements appear in practice.

## Prerequisites

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Ensure you have your LLM API keys configured as per the project's root README.)*

## Running the Demo

Run the following command from the repository root:

```bash
python scripts/run_story_workflow.py --context-file examples/story_workflow/context-bundle.example.md --story-file examples/story_workflow/story.example.md --output-dir outputs/story-workflow/example
```

## Expected Outputs

Upon successful completion, the workflow will generate the following artifacts in `outputs/story-workflow/example/`:

1.  **`story-refinement.md`**: Improved story clarity, requirements, and acceptance criteria review.
2.  **`architecture-notes.md`**: Architectural direction, impacted areas, and risk assessment.
3.  **`test-plan.md`**: Validation strategy and test cases mapped to acceptance criteria.
4.  **`implementation-plan.md`**: Sequential steps and file changes needed for implementation.
5.  **`review-notes.md`**: Quality review of all generated artifacts.
6.  **`final-summary.md`**: High-level run summary and required human actions.

For a detailed description of each artifact, see [Expected Output README](./expected-output/README.md).

## What This Demo Proves

- **Input Loading**: Confirms the runner can correctly parse markdown context and story files.
- **Agent Sequence**: Demonstrates the successful handoff between the Story Refiner, Architect, Test Strategist, Developer, and Reviewer agents.
- **Artifact Generation**: Verifies that all six standard artifacts are created with the correct names.
- **Guardrail Visibility**: Shows that artifacts include the required advisory warnings and do not make unsupported claims.
- **Portfolio Value**: Provides a clear example of the project's value for planning and refining development work.

## Limitations

- **Non-Deterministic**: LLM outputs may vary slightly between runs, though the structure and artifacts remain consistent.
- **No Code Changes**: This demo (and the MVP workflow) does not automatically modify source code or commit changes.
- **Advisory Only**: All generated plans are suggestions and require human review and approval.
