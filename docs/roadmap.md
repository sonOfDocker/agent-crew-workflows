# Roadmap

This roadmap defines the early direction for Agent Crew Workflows.

The project should start with simple, inspectable workflow contracts before adding deeper automation.

## Roadmap Principles

Agent Crew Workflows should evolve according to these principles:

- Start with clear documentation before runtime automation.
- Keep each milestone small enough to review and commit cleanly.
- Prefer reusable workflow contracts over one-off prompts.
- Keep agent responsibilities separated.
- Treat human approval as a required quality gate.
- Build toward real project usefulness, not just demos.
- Add automation only after the manual workflow is understandable.

## Milestone 1: Foundation

Goal: Establish the initial project structure and workflow documentation.

This milestone creates the baseline repo content needed before implementing CrewAI runtime behavior.

### Scope

- Define the project purpose in the root README.
- Document the initial agent roles.
- Document the development workflow.
- Add a standard story template.
- Establish the starting folder structure.
- Add placeholder directories where needed.
- Prepare the repo for future CrewAI implementation.

### Expected Files

- README.md
- docs/agent-roles.md
- docs/workflow-overview.md
- docs/roadmap.md
- templates/story-template.md
- .env.example
- pyproject.toml
- .gitignore

### Done When

- The repository purpose is clear.
- The initial folder structure exists.
- Core agent roles are documented.
- The development workflow is documented.
- A reusable story template exists.
- The project is ready for the first CrewAI setup story.

## Milestone 2: Context Bundling

Goal: Create repeatable scripts for preparing project context for agents.

This milestone should make it easy to gather relevant markdown documentation into a single context bundle that can be passed into an agent workflow.

### Scope

- Add a Bash context bundle script.
- Add a PowerShell context bundle script.
- Exclude generated, dependency, and build directories.
- Include markdown files from the project.
- Normalize section headers and relative paths.
- Keep output deterministic enough for review.
- Document how to use the scripts.

### Expected Files

- scripts/build-context.sh
- scripts/build-context.ps1
- docs/context-bundling.md
- examples/context-bundle.example.md

### Done When

- Context can be bundled from the repo root.
- Generated output is readable.
- Common generated folders are excluded.
- Script behavior is documented.
- The bundle can be used as input to a future agent workflow.

## Milestone 3: Story Input Contract

Goal: Define how stories are passed into the workflow.

This milestone should standardize how a story file or GitHub issue body becomes agent input.

### Scope

- Define required story fields.
- Add an example story file.
- Document story readiness rules.
- Define how story input combines with project context.
- Identify minimum story data needed by each agent.

### Expected Files

- docs/story-contract.md
- examples/stories/example-story.md
- templates/story-template.md
- crews/story_readiness/README.md

### Done When

- A story can be written using the standard template.
- The required story sections are clear.
- Agents can determine whether a story is ready for the next phase.
- Missing context or unclear acceptance criteria can be flagged.

## Milestone 4: CrewAI MVP

Goal: Implement the first minimal CrewAI workflow.

This milestone should translate the documented workflow into a basic CrewAI implementation.

### Scope

- Add initial CrewAI project structure.
- Define initial agents.
- Define initial tasks.
- Load project context from a markdown bundle.
- Load story input from a markdown file.
- Run a simple story refinement workflow.
- Keep the first implementation intentionally small.

### Expected Files

- crews/development/
- crews/development/agents.yaml
- crews/development/tasks.yaml
- crews/development/crew.py
- crews/development/main.py
- docs/crewai-mvp.md

### Done When

- A local CrewAI command can run against a story file.
- The workflow can read a context bundle.
- The workflow can produce a story refinement output.
- Setup steps are documented.
- Known limitations are documented.

## Milestone 5: Multi-Agent Development Workflow

Goal: Expand the CrewAI MVP into the full development workflow.

This milestone should introduce the full sequence of agents defined in the workflow documentation.

### Scope

- Add Story Refiner Agent.
- Add Architect Agent.
- Add Test Strategy Agent.
- Add Developer Agent.
- Add Reviewer Agent.
- Define handoff outputs between agents.
- Support running the workflow by phase.
- Support running the workflow end-to-end.
- Keep human approval as the final gate.

### Expected Files

- crews/development/agents.yaml
- crews/development/tasks.yaml
- crews/development/crew.py
- crews/development/main.py
- docs/agent-handoffs.md
- docs/workflow-overview.md

### Done When

- Each agent has a defined task.
- Each phase has a clear output.
- The workflow can run with a story and context bundle.
- Outputs can be reviewed by a human.
- The workflow does not commit or merge code automatically.

## Milestone 6: GitHub Integration

Goal: Connect the workflow to GitHub issues and project planning.

This milestone should allow the workflow to use GitHub issues as story inputs and eventually update issue status or comments.

### Scope

- Research GitHub integration options.
- Decide whether to use MCP, GitHub CLI, or GitHub API.
- Read issue content as story input.
- Reference issue IDs in workflow output.
- Generate commit messages that can close issues.
- Document required permissions and safety boundaries.

### Expected Files

- docs/github-integration.md
- mcp/github/
- scripts/github/
- examples/stories/github-issue-example.md

### Done When

- A GitHub issue can be used as story input.
- Required permissions are documented.
- The workflow can produce issue-aware output.
- The workflow does not modify GitHub state without explicit human approval.

## Milestone 7: Review and Quality Gates

Goal: Strengthen verification before human approval.

This milestone should make review more useful by standardizing how tests, diffs, and acceptance criteria are checked.

### Scope

- Define review checklist format.
- Define acceptance criteria checklist format.
- Capture test commands and output.
- Capture known risks and follow-up work.
- Define approval, revision, and rejection recommendations.
- Add example review outputs.

### Expected Files

- templates/review-template.md
- docs/review-quality-gates.md
- examples/reviews/example-review.md

### Done When

- Review output is consistent.
- Required fixes are separated from optional improvements.
- Acceptance criteria are checked explicitly.
- Test verification is documented.
- Human approval remains required.

## Milestone 8: MCP Exploration

Goal: Explore MCP integrations that could make the workflow more useful.

This milestone should focus on careful experimentation, not uncontrolled automation.

### Scope

- Document useful MCP server candidates.
- Explore filesystem integration.
- Explore GitHub integration.
- Explore test runner integration.
- Explore documentation search integration.
- Define safety boundaries for tool use.
- Keep write actions human-approved by default.

### Expected Files

- docs/mcp-strategy.md
- mcp/README.md
- mcp/examples/

### Done When

- MCP use cases are documented.
- Candidate integrations are identified.
- Risks and permissions are understood.
- The project has a clear MCP adoption path.

## Backlog Ideas

Future ideas include:

- Agent output templates
- Prompt library
- Phase-specific workflow commands
- Story readiness scoring
- ADR recommendation agent
- Codebase summary generator
- Test failure analysis agent
- Pull request review assistant
- Local model experimentation
- Cost and token usage tracking
- Multi-project workspace support
- Project-specific agent profiles
- Integration with GitHub Projects
- Integration with IDE-based coding agents

## Current Focus

The current focus is completing Milestone 1: Foundation and ensuring the baseline workflow documents are clear, reviewable, and aligned.

CrewAI automation should not begin until the foundational workflow documents, story template, agent roles, and roadmap have been reviewed and accepted.Mi

## MVP Direction

The first MVP is a local, human-approved agent workflow that can:

- Read a project context bundle.
- Read a story written in the standard story template.
- Run a small story refinement or readiness workflow.
- Produce reviewable markdown output.
- Leave all code changes, commits, merges, and external system updates under human control.

The MVP is not intended to autonomously modify repositories, merge pull requests, or update GitHub state.