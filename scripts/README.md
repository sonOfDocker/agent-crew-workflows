# Scripts

This directory contains utility scripts for Agent Crew Workflows.

Scripts should support repeatable local workflow tasks such as building context bundles, preparing story inputs, running validation checks, or supporting future CrewAI execution.

## Purpose

The `scripts/` directory should contain small, inspectable scripts that make the workflow easier to run.

Scripts may include:

- Context bundle generation
- Story input preparation
- Local workflow runners
- Test helpers
- Markdown validation helpers
- GitHub issue export helpers
- CrewAI execution wrappers

## Script Principles

Scripts should follow these principles:

- Be safe to run locally.
- Avoid destructive actions by default.
- Print clear output.
- Fail clearly when required inputs are missing.
- Avoid hardcoded machine-specific paths.
- Keep generated files out of source control unless they are examples.
- Work from the repository root when possible.
- Support repeatable agent workflow execution.

## Planned Scripts

Expected future scripts include:

- `build-context.sh`
- `build-context.ps1`
- `run-story-workflow.sh`
- `run-story-workflow.ps1`

## Generated Files

Generated files should usually not be committed unless they are examples.

Common generated files may include:

- `context-bundle.md`
- `run-output.md`
- `agent-output.md`

These files are ignored by default in `.gitignore`.

## Current Status

No production scripts are active yet.

This directory is reserved for context bundling and workflow helper scripts that will be added in later stories.