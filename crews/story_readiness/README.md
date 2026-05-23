# Story Readiness Crew

This directory contains the Story Readiness workflow implementation.

## Purpose

The Story Readiness crew evaluates whether a development story contains enough information for agents to execute it safely and consistently.

## Current Implementation: Input Loading

The current implementation focuses on reusable input loading and validation, ensuring that both the project context bundle and the story input are valid markdown files before any orchestration begins.

### Usage

You can validate workflow inputs using the following command:

```bash
python -m crews.story_readiness.main --context-file <context_bundle_path> --story-file <story_file_path>
```

### Components

- `inputs.py`: Contains the `WorkflowInputs` model and the `load_workflow_inputs` function.
- `main.py`: A thin CLI wrapper for input validation.
- `config/`: Directory for agent and task YAML configurations.

## Workflow Goal

This workflow is intended to help determine whether a story is ready for downstream agent roles such as:

- Architect Agent
- Test Agent
- Developer Agent
- Reviewer Agent

## Expected Responsibilities

The future Story Readiness crew may validate that a story includes:

- A clear goal
- Explicit acceptance criteria
- Relevant project context
- Expected files or areas of the repository to inspect
- Testing expectations
- Definition of Done requirements
- Constraints, assumptions, and non-goals
- Expected output artifacts

## Expected Inputs

Potential inputs may include:

- A story file or GitHub issue
- `templates/story-template.md`
- A generated context bundle
- Relevant documentation from `docs/`
- Existing project conventions and workflow contracts

## Expected Outputs

Potential outputs may include:

- A story readiness assessment
- Missing information or ambiguity findings
- Recommended story refinements
- A ready/not-ready decision
- Suggested next agent role or workflow step

## Planned Structure

A future implementation may use a structure similar to:

```text
crews/story_readiness/
├── agents.yaml
├── tasks.yaml
├── crew.py
├── main.py
└── README.md