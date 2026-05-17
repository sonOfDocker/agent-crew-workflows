# Agent Crew Workflows

Agent Crew Workflows is a production-oriented AI development workflow project.

The goal is to create a reusable agent-assisted engineering system that helps take project ideas from rough concept to implementation-ready stories, code changes, tests, reviews, and commits.

This project is intended to support real software development work across multiple projects, including early-stage ideas, personal tools, internal systems, experiments, and projects that may eventually mature into production-grade applications or businesses.

## Project Goals

The primary goals of this project are:

1. Define a clear agent-orchestrated development workflow.
2. Keep project context readable, versioned, and easy to pass into agents.
3. Standardize how ideas become implementation-ready stories.
4. Separate agent responsibilities so planning, testing, implementation, and review remain clear.
5. Build toward a CrewAI-based workflow that can execute repeatable development tasks.
6. Support future MCP integrations for tools such as GitHub, filesystems, documentation, test runners, and project boards.
7. Improve development speed without sacrificing engineering discipline, testability, or human judgment.

## Why This Project Exists

AI tools are useful, but they become inconsistent when they lack structure.

This project exists to provide that structure.

Agent Crew Workflows should help answer questions like:

- What are we building?
- Why are we building it?
- What story should be worked on next?
- What context does the agent need?
- What should be tested?
- What should the developer agent implement?
- What should the reviewer agent verify?
- What should be committed?

The goal is not to let agents randomly generate code.

The goal is to build a disciplined workflow where agents operate inside clear boundaries using project context, story definitions, tests, and human review.

## Initial Workflow Concept

The intended workflow is:

```text
Idea / Rough Requirement
        ↓
Story Refiner Agent
        ↓
Architect Agent
        ↓
Test Strategy Agent
        ↓
Developer Agent
        ↓
Reviewer Agent
        ↓
Human Approval / Commit
```

The workflow should help turn vague ideas into implementation-ready stories with:

- Clear goals
- Acceptance criteria
- Technical notes
- Testing expectations
- Definition of done
- Context references
- Review checklist

## Repository Structure

```text
agent-crew-workflows/
├── crews/
├── docs/
├── examples/
├── mcp/
├── scripts/
├── templates/
├── tests/
├── .env.example
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Directory Purpose

### crews/

Contains CrewAI-specific crew definitions.

This directory should eventually contain the actual CrewAI configuration, agents, tasks, and orchestration code.

### docs/

Contains project documentation intended for humans and agents.

This includes architecture notes, agent role definitions, workflow documentation, ADRs, and roadmap files.

### examples/

Contains sample story files, context bundles, and example workflow inputs.

### mcp/

Contains future MCP-related configuration, adapters, or integration notes.

### scripts/

Contains utility scripts for preparing context, bundling markdown files, running workflow helpers, or supporting local development.

### templates/

Contains reusable templates for stories, prompts, reviews, and workflow inputs.

### tests/

Contains tests for scripts, workflow helpers, or future orchestration code.

## Current Scope

The first milestone is not to build a fully automated agent system.

The first milestone is to establish the project structure and documentation needed to support a reliable MVP workflow.

The initial MVP should answer:

- What agents exist?
- What does each agent own?
- What does each agent not own?
- What does a well-formed story look like?
- How is project context gathered?
- How is story context passed into the workflow?
- What files belong in the first version of the repo?

## Initial Agent Roles

The first planned agents are:

1. Story Refiner Agent
2. Architect Agent
3. Test Strategy Agent
4. Developer Agent
5. Reviewer Agent

These roles may later be implemented in CrewAI, but they should first be defined clearly in markdown before automation is added.

## Development Philosophy

This project should follow these principles:

- Keep the workflow simple before making it powerful.
- Prefer markdown contracts before code automation.
- Make every agent role explicit.
- Make story readiness visible.
- Do not let agents silently change requirements.
- Keep humans responsible for final judgment.
- Favor small commits tied to specific stories.
- Treat tests, documentation, and review as first-class parts of the workflow.
- Build workflows that can support real projects, not just demos.
- Assume early ideas may become serious systems if they mature.

## Near-Term Roadmap

Near-term work includes:

1. Create the initial repository structure.
2. Add agent role definitions.
3. Add a standard story template.
4. Add context bundle scripts.
5. Add example story input files.
6. Add an MVP CrewAI development crew.
7. Run the workflow against a simple test story.
8. Integrate GitHub issue/story input.
9. Integrate project context loading.
10. Add review and quality gates.

## Human Review Boundary

Agents can assist with planning, coding, testing, reviewing, and summarizing.

However, agents should not be treated as the final authority.

A human reviewer is responsible for:

- Approving story scope
- Approving architecture decisions
- Reviewing code changes
- Running or verifying tests
- Making commits
- Merging pull requests
- Deciding whether output is production-worthy

## Status

This project is in its initial setup phase.

The current focus is creating the foundational documentation and workflow contracts needed before implementing the CrewAI orchestration layer.

## What to Review Next

Reviewers should look at:

1. `docs/agent-roles.md` to understand the planned agent responsibilities.
2. `templates/story-template.md` to understand the story contract agents will work from.
3. `docs/workflow-overview.md` to understand the intended human/agent workflow.
4. `docs/roadmap.md` to understand the planned implementation sequence.
5. `scripts/README.md` to understand future context-bundling support.