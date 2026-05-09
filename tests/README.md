# Tests

This directory contains tests for Agent Crew Workflows.

Tests should validate scripts, workflow helpers, context bundling behavior, and future CrewAI orchestration code.

## Purpose

The `tests/` directory exists to keep the workflow reliable as automation is added.

Early tests may focus on:

- Context bundle generation
- File filtering rules
- Story input parsing
- Workflow helper behavior
- Configuration loading
- CrewAI wrapper behavior

## Testing Principles

Tests should follow these principles:

- Keep tests focused and easy to understand.
- Test workflow behavior that could break silently.
- Prefer deterministic inputs and outputs.
- Avoid requiring live API keys for normal test runs.
- Avoid requiring network access for normal test runs.
- Keep integration tests separate from fast unit tests when possible.
- Treat test output as part of the workflow quality gate.

## Planned Test Areas

Expected future test areas include:

- Context bundling scripts
- Story template validation
- Environment configuration loading
- Agent workflow input loading
- CrewAI task configuration
- Review output formatting

## Test Command

The expected test command is:

```text
pytest
```

## Current Status

No automated tests are active yet.

This directory is reserved for tests that will be added as scripts and runtime workflow code are introduced.