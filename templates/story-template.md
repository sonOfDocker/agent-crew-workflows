# Story Template

Use this template to define implementation-ready stories for Agent Crew Workflows.

A good story should be clear enough for agents to refine, design, test, implement, review, and hand back to a human for approval.

## Story Title

[Short action-oriented title]

Example:

Define Standard Story Contract for Agents

## Story Type

Choose one:

- Epic
- Story
- Task
- Spike
- Bug
- Chore

## Status

Choose one:

- Draft
- Ready for Refinement
- Ready for Architecture Review
- Ready for Test Strategy
- Ready for Development
- In Development
- In Review
- Blocked
- Done

## Status Definitions

- **_Draft_**: Initial idea; not ready for agent execution.
- **_Ready for Refinement_**: Goal is known, but scope and AC may need tightening.
- **_Ready for Architecture Review_**: Scope and AC are clear enough for technical impact review.
- **_Ready for Test Strategy_**: Architecture direction is clear enough to define validation.
- **_Ready for Development_**: AC, affected areas, test strategy, and scope are clear enough to implement.
- **_In Development_**: Implementation is underway.
- **_In Review_**: Implementation is complete and awaiting review.
- **_Blocked_**: Work cannot continue without resolving an external dependency or open question.
- **_Done_**: AC, verification, review, and human approval are complete.
## Summary

Briefly describe what needs to be done.

Keep this section focused on the goal, not the implementation details.

## Problem / Context

Explain why this story exists.

Include relevant background, current pain points, project context, or previous decisions.

## Inputs / References

List source material the agents should use.

- GitHub Issue:
- Related PR:
- Context Bundle:
- Related Docs:
- Related ADRs:
- Related Stories:

## Goal

Describe the desired outcome.

By the end of this story, what should be true?

## Non-Goals

List what is intentionally out of scope.

This helps prevent agents from expanding the story beyond what was requested.

Examples:

- Do not implement CrewAI runtime execution in this story.
- Do not connect to GitHub APIs in this story.
- Do not add production deployment configuration in this story.

## User / Developer Value

Explain why this work matters.

Examples:

- Makes future agent workflows more consistent.
- Reduces ambiguity before implementation begins.
- Creates a reusable template for GitHub issues.
- Helps agents understand story readiness before coding.

## Acceptance Criteria

The story is complete when:

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
- [ ] Criterion 4

Acceptance criteria should be specific, observable, and testable.

Avoid vague criteria like:

- The system works well.
- The code is clean.
- The workflow is better.

Prefer clear criteria like:

- The repository contains a documented story template under `templates/story-template.md`.
- The template includes sections for summary, goals, non-goals, acceptance criteria, testing notes, and definition of done.
- The README references the story template as part of the initial workflow.

## Requirements

List specific functional or documentation requirements.

### Functional Requirements

- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3

### Documentation Requirements

- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3

### Testing Requirements

- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3

Requirement:
- The template must include a section for agent responsibilities.

Acceptance Criterion:
- A reviewer can identify responsibilities for Story Refiner, Architect, Test Strategy, Developer, and Reviewer Agents.

## Proposed Approach

Describe the expected approach if known.

This section can be filled in by a human, Story Refiner Agent, or Architect Agent.

If the approach is unknown, write:

To be determined during architecture review.

## Affected Areas

List files, folders, modules, or concepts likely affected by this story.

Examples:

- `README.md`
- `docs/agent-roles.md`
- `templates/story-template.md`
- `scripts/build-context.sh`
- `scripts/build-context.ps1`

## Agent Responsibilities

### Story Refiner Agent

Expected responsibilities:

- Clarify story goal
- Tighten scope
- Improve acceptance criteria
- Identify open questions
- Identify assumptions

### Architect Agent

Expected responsibilities:

- Identify affected areas
- Recommend technical approach
- Identify architecture risks
- Decide whether an ADR is needed

### Test Strategy Agent

Expected responsibilities:

- Map acceptance criteria to validation steps
- Identify test cases
- Identify edge cases
- Define manual verification where automated tests are not needed

### Developer Agent

Expected responsibilities:

- Implement the story
- Add or update tests if needed
- Follow project conventions
- Keep the change focused
- Document verification steps

### Reviewer Agent

Expected responsibilities:

- Review implementation against acceptance criteria
- Check scope control
- Check test coverage or verification
- Identify required fixes
- Identify optional improvements

## Open Questions

List questions that must be answered before or during implementation.

- [ ] Question 1
- [ ] Question 2
- [ ] Question 3

If there are no open questions, write:

None at this time.

## Assumptions

List assumptions being made.

- Assumption 1
- Assumption 2
- Assumption 3

If there are no assumptions, write:

None at this time.

## Risks / Tradeoffs

List known risks or tradeoffs.

Examples:

- The story may become too broad if CrewAI runtime setup is included.
- The template may need to evolve after the first real workflow run.
- Too much documentation can slow down early iteration.

## Test Strategy

Describe how this story should be validated.

For documentation-only stories, validation may include:

- Confirming required files exist
- Confirming required sections are present
- Confirming links or references are accurate
- Confirming markdown renders correctly
- Confirming the story supports the intended workflow

For code stories, validation may include:

- Unit tests
- Integration tests
- CLI checks
- Script execution
- Manual verification

## Review Checklist

Before this story is considered done, confirm:

- [ ] Scope stayed focused
- [ ] Acceptance criteria were satisfied
- [ ] Required files were added or updated
- [ ] Documentation is clear
- [ ] Tests or verification steps were completed
- [ ] No unrelated changes were included
- [ ] Follow-up work is documented if needed

## Definition of Done

This story is done when:

- [ ] The story goal has been satisfied
- [ ] All acceptance criteria are complete
- [ ] Required documentation has been added or updated
- [ ] Required tests or validation steps have been completed
- [ ] The reviewer has checked the work
- [ ] Human approval has been given
- [ ] A clear commit message has been prepared

## Implementation Notes

Use this section for notes discovered during implementation.

Examples:

- Files changed
- Design choices
- Commands run
- Test output
- Deviations from the original approach

## Verification

Document how the work was verified.

Examples:

```text
Verified markdown renders correctly in IDE preview.
Confirmed file exists at templates/story-template.md.
Confirmed README references the template.
```

## Follow-Up Work

List any future work that should be handled in separate stories.

- [ ] Follow-up 1
- [ ] Follow-up 2
- [ ] Follow-up 3

If there is no follow-up work, write:

None at this time.