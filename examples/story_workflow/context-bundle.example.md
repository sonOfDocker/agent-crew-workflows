# Example Project Context: Agent Crew Workflows

This file provides a sample project context for the golden path demo. It is a simplified version of a project context bundle.

## Project Name
Agent Crew Workflows

## Project Goal
Build a set of CrewAI-powered agent workflows that help developers refine stories, plan architecture, and prepare for implementation with clear human-in-the-loop guardrails.

## MVP Workflow Summary
The MVP workflow (Story Readiness) consists of a sequence of agents:
1. **Story Refiner**: Improves story clarity and identifies gaps.
2. **Architect**: Provides high-level design guidance and identifies impacted areas.
3. **Test Strategist**: Creates a test plan mapped to acceptance criteria.
4. **Developer**: Creates a step-by-step implementation plan.
5. **Reviewer**: Reviews all previous artifacts for consistency and quality.
6. **Summary Agent**: Produces a final run summary with required human actions.

## Agent Roles
- **Story Refiner**: Focuses on clarity, requirements, and AC.
- **Architect**: Focuses on design, risks, and project impact.
- **Test Strategist**: Focuses on validation, edge cases, and evidence.
- **Developer**: Focuses on implementation steps and file changes.
- **Reviewer**: Focuses on quality control and AC satisfaction.

## Artifact Expectations
The workflow generates six standard markdown artifacts:
- `story-refinement.md`
- `architecture-notes.md`
- `test-plan.md`
- `implementation-plan.md`
- `review-notes.md`
- `final-summary.md`

## Guardrail Expectations
- All artifacts must contain a human-review warning.
- Agents must not claim code is finished or tests passed.
- High-risk actions (like committing code) are out of scope for the MVP.
- All artifacts are advisory and require human confirmation.

## Known Limitations
- No real-time code execution in MVP.
- No automatic GitHub integration.
- LLM output may vary between runs.
- Requires manual review of all generated plans.
