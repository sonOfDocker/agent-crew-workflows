# Agent Workflow

This document defines the initial development workflow for Agent Crew Workflows.

The workflow describes how a rough idea moves through refinement, architecture, test planning, implementation, review, and human approval.

## Workflow Goal

The goal of this workflow is to make AI-assisted development more reliable by giving each phase a clear purpose, input, output, and quality bar.

The workflow should help prevent common problems such as:

- Agents coding before the story is clear
- Architecture decisions being made silently
- Tests being treated as an afterthought
- Review being reduced to a quick summary
- Scope expanding without approval
- Commits being made without clear verification

## High-Level Flow

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

## Phase 1: Idea or Rough Requirement

### Purpose

Capture the initial request, problem, feature idea, bug, improvement, or experiment.

At this point, the idea may be incomplete.

### Inputs

Possible inputs include:

- Human note
- GitHub issue
- Project board card
- Conversation summary
- Product idea
- Bug report
- Technical improvement
- Existing project pain point

### Outputs

The output of this phase is a rough work item that can be refined into a clear story.

### Quality Bar

The rough requirement is ready for refinement when:

- The basic intent is understandable
- The project or system context is known
- The human owner can explain why the work matters

## Phase 2: Story Refinement

### Purpose

Turn the rough work item into an implementation-ready story.

### Primary Agent

Story Refiner Agent

### Inputs

The Story Refiner Agent should receive:

- Rough requirement
- Project context bundle
- Relevant roadmap or epic
- Existing documentation
- Human constraints or preferences

### Outputs

The Story Refiner Agent should produce:

- Clear story title
- Summary
- Problem / context
- Goal
- Non-goals
- Acceptance criteria
- Open questions
- Assumptions
- Definition of done

### Quality Bar

The story is ready for architecture review when:

- The goal is clear
- The acceptance criteria are specific and testable
- The scope is narrow enough for one focused change
- Non-goals are documented
- Open questions are either answered or explicitly called out
- The story does not require the next agent to guess the intent

## Phase 3: Architecture Review

### Purpose

Determine the technical approach before implementation begins.

### Primary Agent

Architect Agent

### Inputs

The Architect Agent should receive:

- Refined story
- Project context bundle
- Existing architecture documentation
- Existing ADRs
- Relevant file tree or source summaries

### Outputs

The Architect Agent should produce:

- Recommended approach
- Affected files or modules
- Architecture risks
- Tradeoffs
- Data flow or integration notes
- ADR recommendation if needed
- Handoff notes for the Test Strategy Agent and Developer Agent

### Quality Bar

The story is ready for test strategy when:

- The implementation direction is clear
- Affected areas are identified
- Major risks and tradeoffs are visible
- Any need for an ADR is identified
- The design stays within the story scope

## Phase 4: Test Strategy

### Purpose

Define how the story should be validated.

### Primary Agent

Test Strategy Agent

### Inputs

The Test Strategy Agent should receive:

- Refined story
- Architecture notes
- Project context bundle
- Existing test conventions
- Relevant source or test summaries

### Outputs

The Test Strategy Agent should produce:

- Acceptance criteria to test mapping
- Recommended unit tests
- Recommended integration tests if needed
- Edge cases
- Regression risks
- Manual verification steps if appropriate

### Quality Bar

The story is ready for development when:

- Each acceptance criterion has a validation path
- The test scope is appropriate for the size of the story
- Important edge cases are identified
- Manual verification is documented where automated tests are not useful
- The Developer Agent knows what must be proven before review

## Phase 5: Development

### Purpose

Implement the story according to the refined requirements, architecture notes, and test strategy.

### Primary Agent

Developer Agent

### Inputs

The Developer Agent should receive:

- Refined story
- Architecture notes
- Test strategy
- Project context bundle
- Relevant source files
- Existing project conventions

### Outputs

The Developer Agent should produce:

- Code changes
- Test changes
- Documentation updates if needed
- Implementation notes
- Verification notes
- Known limitations or follow-up recommendations

### Quality Bar

The story is ready for review when:

- Acceptance criteria are addressed
- Required tests or validation steps have been completed
- The change stays within scope
- Project conventions are followed
- Known limitations are documented
- The implementation can be reviewed against the original story

## Phase 6: Review

### Purpose

Evaluate whether the completed work satisfies the story and is ready for human approval.

### Primary Agent

Reviewer Agent

### Inputs

The Reviewer Agent should receive:

- Refined story
- Architecture notes
- Test strategy
- Code diff
- Test output or verification notes
- Project context bundle

### Outputs

The Reviewer Agent should produce:

- Review summary
- Acceptance criteria checklist
- Test coverage assessment
- Scope assessment
- Architecture alignment assessment
- Required fixes
- Optional improvements
- Recommendation

### Quality Bar

The story is ready for human approval when:

- Acceptance criteria have been checked against the actual changes
- Tests or verification steps have been reviewed
- Required fixes are clearly separated from optional improvements
- Risks are documented
- The recommendation is clear

## Phase 7: Human Approval and Commit

### Purpose

The human owner makes the final decision.

Agents can assist, but the human owner approves the work.

### Inputs

The human owner should review:

- Refined story
- Architecture notes
- Test strategy
- Implementation summary
- Review summary
- Code diff
- Test results
- Commit message

### Outputs

The human owner may produce:

- Approval
- Requested changes
- Commit
- Pull request
- Follow-up story
- Rejection or rollback

### Quality Bar

The story is complete when:

- The human owner approves the work
- The commit message accurately describes the change
- Any follow-up work is captured separately
- The project remains in a clean state

## Context Bundle Expectations

Each workflow run should use a context bundle when possible.

The context bundle should help agents understand:

- Project goals
- Current architecture
- Existing decisions
- Relevant templates
- Existing workflows
- Coding or documentation conventions
- Current story context

The context bundle should be treated as read-only input unless a story explicitly asks to update it.

## Story Input Expectations

Each workflow run should include a story file or GitHub issue body.

The story input should define:

- What is being worked on
- Why it matters
- What is in scope
- What is out of scope
- How completion will be judged
- What validation is expected

## Handoff Format

Each phase should provide a short handoff to the next phase.

A good handoff includes:

- What was decided
- What assumptions were made
- What risks remain
- What files or areas matter
- What the next agent should focus on
- What the next agent should avoid changing

## Escalation Rules

The workflow should stop or ask for human input when:

- The story goal is unclear
- Acceptance criteria conflict
- Required context is missing
- A major architecture decision is needed
- A security or safety concern appears
- The implementation is larger than expected
- The tests cannot reasonably validate the change
- An agent would need to guess instead of reason from context

## Workflow Definition of Done

A workflow run is complete when:

- The story has been refined
- Architecture impact has been considered
- Test expectations have been defined
- Implementation has been completed if applicable
- Verification has been performed or documented
- Review has been completed
- Human approval has been given
- The final commit message is ready