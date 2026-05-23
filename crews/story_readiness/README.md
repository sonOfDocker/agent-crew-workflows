# Story Readiness Crew

This directory contains the Story Readiness workflow implementation using CrewAI.

## Purpose

The Story Readiness crew is the first runnable MVP workflow. It takes a project context bundle and a story markdown file as inputs, executes a sequence of specialist agents, and produces structured markdown artifacts to help a human developer prepare a story for implementation.

**Note: The output of this workflow is advisory and requires human review.**

## Workflow Sequence

The workflow follows a sequential process:

1.  **Story Refiner**: Reviews the story and project context to clarify intent and improve acceptance criteria.
2.  **Architect**: Proposes a technical approach and identifies affected components.
3.  **Test Strategist**: Defines a validation strategy and test scenarios.
4.  **Developer**: Produces a detailed implementation plan (without modifying code).
5.  **Reviewer**: Evaluates all planning artifacts and provides a recommendation.
6.  **Final Summary**: Summarizes all outputs and lists next human actions.

## Usage

### Prerequisites

- Python 3.12+
- `crewai` and `python-dotenv` installed
- An `OPENAI_API_KEY` (or other supported LLM provider key) set in your environment or `.env` file.

### Running the Workflow

You can run the workflow from the project root using the provided script:

```powershell
python scripts/run_story_workflow.py `
  --context-file ./examples/world-cup-stats/context-bundle.md `
  --story-file ./examples/world-cup-stats/current-story.md `
  --output-dir ./outputs/story-workflow/world-cup
```

### Arguments

- `--context-file`: (Required) Path to the project context bundle markdown file.
- `--story-file`: (Required) Path to the story markdown file.
- `--output-dir`: (Optional) Directory where generated artifacts will be saved. Defaults to `./outputs/story-workflow`.

## Generated Artifacts

The workflow generates the following markdown files in the specified output directory. For full details on the required sections and content rules, see the [Workflow Artifacts Documentation](../../docs/workflow-artifacts.md).

- `story-refinement.md`
- `architecture-notes.md`
- `test-plan.md`
- `implementation-plan.md`
- `review-notes.md`
- `final-summary.md`

## Current Limitations

- **Advisory Only**: Agents do not modify source code, create commits, or open pull requests.
- **Human Review Required**: All outputs must be verified by a human developer.
- **Sequential Execution**: Tasks are currently executed one after another.

## Manual Verification

Manual verification of artifact wrapping was performed using a mock run:

Command:
```powershell
# Verified via a temporary script that simulated artifact generation 
# and verified the deterministic advisory wrapping logic.
```

Result:
- Successfully verified that all six artifacts are correctly wrapped with the mandatory advisory warning.
- Verified that input paths and output directory are correctly mapped for the final summary task via unit tests.

## Components

- `crew.py`: Defines the `StoryReadinessCrew` class and CrewAI orchestration.
- `inputs.py`: Handles input loading and validation logic.
- `main.py`: CLI entry point for the workflow.
- `config/agents.yaml`: YAML configuration for agent roles, goals, and backstories.
- `config/tasks.yaml`: YAML configuration for task descriptions and expected outputs.
