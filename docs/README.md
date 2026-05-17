# Documentation

This directory contains the core documentation for Agent Crew Workflows.

The documentation in this directory should explain the project purpose, development workflow, agent roles, roadmap, architecture decisions, and future integration strategy.

## Purpose

The `docs/` directory is the main source of truth for how Agent Crew Workflows should operate.

Documentation should be useful to both humans and agents.

It should help answer:

- What workflow are we building?
- What agents are involved?
- What does each agent own?
- How does work move from idea to implementation?
- What decisions have already been made?
- What should be built next?
- What should not be automated yet?

## Current Documents

### `agent-roles.md`

Defines the initial agent roles, responsibilities, boundaries, inputs, outputs, and quality bars.

### `docs/workflow-overview.md`

Defines the end-to-end development workflow from rough idea through human approval and commit.

### `roadmap.md`

Defines the early project milestones and expected direction.

### `architecture/README.md`

Defines the current architecture direction and planned structure for future runtime implementation.

### `decisions/README.md`

Defines how architectural and workflow decisions will be recorded.
## Planned Documents

Future documentation may include:

- Architecture overview
- Context bundling strategy
- Story contract
- CrewAI MVP setup
- GitHub integration plan
- MCP strategy
- Review and quality gates
- ADRs

## Documentation Principles

Documentation should follow these principles:

- Be clear enough for a human to review quickly.
- Be structured enough for agents to use as context.
- Avoid vague process language.
- Prefer explicit ownership, inputs, outputs, and quality bars.
- Keep workflow rules practical and enforceable.
- Document decisions before automating them.
- Keep human approval visible in the workflow.

## Current Status

The current focus is establishing foundational workflow documentation before implementing the CrewAI runtime layer.