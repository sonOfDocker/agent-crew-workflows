# Architecture Decisions

This directory contains architecture decision records for Agent Crew Workflows.

Architecture decisions should be documented when a choice affects the project structure, workflow design, automation strategy, integration model, security boundary, or long-term maintainability of the system.

## Purpose

The `docs/decisions/` directory exists to keep important decisions visible.

Agent Crew Workflows should avoid hidden decisions that only live in chat history, local notes, or agent output.

When the project makes a meaningful decision, it should be captured here so future humans and agents can understand the reasoning.

## When to Add an ADR

Add an architecture decision record when deciding things such as:

- Which agent orchestration framework to use
- How project context should be bundled
- How stories should be passed into workflows
- Whether agents can write files directly
- Whether agents can run commands
- Whether agents can access GitHub
- Whether agents can create commits or pull requests
- Which MCP integrations are allowed
- How secrets and credentials are handled
- How workflow outputs are stored
- How human approval is enforced

## ADR Format

Each ADR should generally include:

- Title
- Status
- Context
- Decision
- Consequences
- Alternatives considered
- Follow-up work

## Naming Convention

Use a numbered filename format:

```text
ADR-001-short-title.md
ADR-002-short-title.md
ADR-003-short-title.md
```

Use lowercase words separated by hyphens after the ADR number.

## Status Values

Common ADR statuses include:

- Proposed
- Accepted
- Superseded
- Deprecated

## Current Status

No architecture decisions have been recorded yet.

The first ADR should be added when the project makes a durable decision about the initial CrewAI workflow design, context loading strategy, or MCP integration boundary.