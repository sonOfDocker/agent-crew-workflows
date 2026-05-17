# Architecture

This directory contains architecture documentation for Agent Crew Workflows.

Architecture documentation should explain how the workflow is structured, how major components relate to each other, and how future automation should be introduced.

## Purpose

The `docs/architecture/` directory exists to document the shape of the system before it becomes too complex.

Agent Crew Workflows should be easy to understand from the documentation alone.

The architecture documentation should help answer:

- What are the major parts of the system?
- How do agents interact?
- How is context passed into the workflow?
- How are stories passed into the workflow?
- Where does CrewAI fit?
- Where do MCP integrations fit?
- What should remain under human control?
- What should not be automated yet?

## Initial Architecture Concept

The initial architecture is intentionally simple.

```text
Project Documentation ──→ Context Bundle
                                  ↓
Story Input ─────────────────→ Agent Workflow
                                  ↓
                            Agent Outputs
                                  ↓
                            Human Review
                                  ↓
                         Commit / Pull Request
```

## Major Components

### Project Documentation

Project documentation defines the goals, roles, workflow, roadmap, decisions, and usage expectations.

Documentation should be readable by humans and usable as agent context.

### Context Bundle

The context bundle is a generated markdown file that collects relevant project documentation into a single input for agents.

The context bundle should help agents reason from actual project context instead of relying on chat memory or assumptions.

### Story Input

The story input defines the specific unit of work.

It may come from:

- A markdown story file
- A GitHub issue body
- A project board item
- A human-written note

The story input should include goals, non-goals, acceptance criteria, requirements, and definition of done.

### Agent Workflow

The agent workflow coordinates the phases of work.

The planned phases are:

1. Story refinement
2. Architecture review
3. Test strategy
4. Development
5. Review
6. Human approval

The exact responsibilities for each phase are defined in `docs/agent-roles.md`.

### Agent Outputs

Agent outputs should be structured and reviewable.

Outputs may include:

- Refined stories
- Architecture notes
- Test strategies
- Implementation summaries
- Review summaries
- Commit message drafts

### Human Review

Human review is a required quality gate.

Agents can assist with the work, but the human owner decides whether the output is correct, safe, useful, and ready to commit.

## CrewAI Role

CrewAI is expected to provide the initial runtime orchestration layer.

In the early milestones, CrewAI should be used to coordinate documented agent roles and tasks.

CrewAI should not be treated as the source of truth for the workflow.

The source of truth should remain the documentation and templates until the runtime behavior is stable.

## MCP Role

MCP integrations may eventually give agents access to external tools.

Possible integrations include:

- GitHub
- Filesystem
- Documentation search
- Test runners
- Project boards
- Local development tools

MCP should be introduced carefully.

Read-only access should come before write access.

Human approval should remain required for commits, pull requests, merges, deployments, and other high-impact actions.

## Safety Boundary

The initial system should avoid uncontrolled automation.

Agents should not automatically:

- Commit code
- Push branches
- Merge pull requests
- Delete files
- Modify GitHub issues
- Change secrets
- Deploy applications
- Run destructive commands

These actions require explicit human approval.

## Current Status

The architecture is still in the foundation phase.

The current priority is documenting the workflow and boundaries before implementing runtime orchestration.