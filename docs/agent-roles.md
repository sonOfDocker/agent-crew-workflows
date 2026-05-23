# Agent Roles

This document defines the initial agent roles for Agent Crew Workflows.

The purpose of these roles is to keep responsibilities clear as work moves from rough idea to implementation-ready story, code changes, tests, review, and commit.

These roles may eventually be implemented through CrewAI, but they should first be treated as workflow contracts.

## Core Principle

Agents should not all behave like general-purpose developers.

Each agent should have a clear responsibility, a clear handoff, and clear limits.

The workflow should avoid blurred ownership between planning, architecture, testing, implementation, and review.

## Current MVP Status

For the initial MVP, these roles define the expected workflow contract only. They do not imply that all agents are currently automated, implemented, or integrated with external tools.

## Initial Agent Workflow

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

## 1. Story Refiner Agent

### Purpose

The Story Refiner Agent turns a rough idea, vague requirement, GitHub issue, or human note into an implementation-ready story.

This agent is responsible for making the work clear before design or development begins.

### Task Boundaries

- **Entry Gate**: Receipt of a draft story, rough requirement, or GitHub issue.
- **Exit Gate**: A refined story that follows the standard template and has all mandatory sections filled (Summary, Goals, AC, etc.).
- **Constraint**: Must not proceed if the goal is fundamentally ambiguous; should flag for human clarification instead.

### Owns

The Story Refiner Agent owns:

- Clarifying the goal of the story
- Identifying the user or developer value
- Defining acceptance criteria
- Identifying assumptions
- Identifying open questions
- Separating in-scope work from out-of-scope work
- Ensuring the story can be implemented in a reasonably small change
- Producing a clean story document or GitHub issue body

### Does Not Own

The Story Refiner Agent does not own:

- Final architecture decisions
- Writing production code
- Writing final tests
- Approving the implementation
- Expanding the story beyond the requested scope without flagging it

### Inputs

Typical inputs include:

- Rough idea
- GitHub issue
- Project context bundle
- Existing documentation
- Human notes
- Current roadmap or epic

### Outputs

Typical outputs include:

- Refined story title
- Story summary
- Acceptance criteria
- Technical notes
- Out-of-scope section
- Open questions
- Definition of done

Expected handoff artifact: refined-story.md or GitHub issue body.

### Quality Bar

A story is ready to hand off when:

- The goal is clear
- Acceptance criteria are testable
- Scope is narrow enough to implement
- Ambiguities are called out
- Dependencies are identified
- The next agent can reason about architecture without guessing the intent

## 2. Architect Agent

### Purpose

The Architect Agent reviews the refined story and proposes the technical approach.

This agent is responsible for helping choose the right design before implementation begins.

### Task Boundaries

- **Entry Gate**: A refined story with clear acceptance criteria.
- **Exit Gate**: Architecture notes that define affected components and implementation approach.
- **Constraint**: Must not change story scope; must flag if the refined story is technically unfeasible.

### Owns

The Architect Agent owns:

- Reviewing the story for technical impact
- Identifying affected components
- Proposing an implementation approach
- Identifying architectural risks
- Identifying data flow or integration concerns
- Suggesting file or module placement
- Identifying whether an ADR is needed
- Flagging design tradeoffs

### Does Not Own

The Architect Agent does not own:

- Rewriting the story unless scope issues are found
- Writing production code
- Writing final tests
- Approving the finished implementation
- Making hidden architecture decisions without documenting them

### Inputs

Typical inputs include:

- Refined story
- Project context bundle
- Existing architecture documentation
- Existing ADRs
- Relevant source tree or file summaries

### Outputs

Typical outputs include:

- Recommended implementation approach
- Affected files or modules
- Architecture notes
- Risks and tradeoffs
- Suggested test focus areas
- ADR recommendation if needed

Expected handoff artifact: architecture-notes.md.

### Quality Bar

The architecture handoff is ready when:

- The implementation direction is clear
- Major tradeoffs are identified
- The expected file or module locations are known
- Risks are visible
- The developer agent can proceed without inventing the design from scratch

## 3. Test Strategy Agent

### Purpose

The Test Strategy Agent defines what should be tested before implementation begins.

This agent is responsible for test intent, coverage expectations, edge cases, and validation strategy.

### Task Boundaries

- **Entry Gate**: A refined story and architecture notes.
- **Exit Gate**: A test strategy that maps AC to validation steps and identifies edge cases.
- **Constraint**: Must ensure every AC has at least one validation path.

### Owns

The Test Strategy Agent owns:

- Identifying test scenarios
- Mapping acceptance criteria to tests
- Defining unit test expectations
- Defining integration test expectations when needed
- Identifying edge cases
- Identifying regression risks
- Recommending test names or test structure
- Clarifying how the work should be verified

### Does Not Own

The Test Strategy Agent does not own:

- Final production implementation
- Rewriting the story scope
- Approving the finished implementation alone
- Creating broad test plans unrelated to the story
- Adding unnecessary test complexity

### Inputs

Typical inputs include:

- Refined story
- Architecture notes
- Project context bundle
- Existing test conventions
- Existing test files or summaries

### Outputs

Typical outputs include:

- Test strategy
- Acceptance criteria to test mapping
- Recommended test cases
- Edge cases
- Manual verification steps if needed

Expected handoff artifact: test-strategy.md.

### Quality Bar

The test strategy is ready when:

- Each acceptance criterion has a validation path
- Important edge cases are identified
- The test scope is appropriate for the story
- The developer agent knows what tests must pass
- The reviewer agent knows what to check later

## 4. Developer Agent

### Purpose

The Developer Agent implements the story according to the refined requirements, architecture notes, and test strategy.

This agent is responsible for producing the code and test changes needed to satisfy the story.

### Task Boundaries

- **Entry Gate**: Implementation-ready story (Refined AC + Architecture + Test Strategy).
- **Exit Gate**: Code changes, tests, and an implementation summary.
- **Constraint**: Must stay within the defined architecture and scope; must ensure all tests pass.

### Owns

The Developer Agent owns:

- Implementing the requested change
- Creating or updating tests required by the story
- Following the architecture guidance
- Following project conventions
- Keeping the change small and focused
- Updating documentation when required by the story
- Reporting what changed
- Reporting how the work was verified

### Does Not Own

The Developer Agent does not own:

- Changing the story goal without approval
- Ignoring the test strategy
- Silently changing architecture direction
- Expanding scope because a related improvement is tempting
- Declaring the work approved
- Making final commit decisions

### Inputs

Typical inputs include:

- Refined story
- Architecture notes
- Test strategy
- Project context bundle
- Relevant source files
- Existing conventions

### Outputs

Typical outputs include:

- Code changes
- Test changes
- Documentation updates if needed
- Implementation summary
- Verification summary
- Known limitations or follow-up notes

Expected handoff artifact: implementation-summary.md plus code diff.

### Quality Bar

The implementation is ready for review when:

- Acceptance criteria are addressed
- Required tests are added or updated
- Existing behavior is not broken
- Scope remains focused
- The implementation follows project conventions
- The change can be reviewed by another agent or human

## 5. Reviewer Agent

### Purpose

The Reviewer Agent evaluates the completed work against the story, architecture notes, test strategy, and project standards.

This agent is responsible for quality review before human approval.

### Task Boundaries

- **Entry Gate**: Completed implementation (Code + Tests + Implementation Summary).
- **Exit Gate**: A review report with a recommendation for approval, revision, or rejection.
- **Constraint**: Must explicitly verify every AC; must check for regressions and style compliance.

### Owns

The Reviewer Agent owns:

- Checking whether acceptance criteria were satisfied
- Checking whether the implementation stayed in scope
- Reviewing test coverage
- Reviewing architecture alignment
- Identifying correctness issues
- Identifying maintainability concerns
- Identifying missing documentation
- Recommending approval, revision, or rejection

### Does Not Own

The Reviewer Agent does not own:

- Making final human approval decisions
- Expanding the story scope
- Rewriting large parts of the implementation unless asked
- Ignoring failed tests or missing verification
- Approving work only because it compiles

### Inputs

Typical inputs include:

- Refined story
- Architecture notes
- Test strategy
- Code diff
- Test output
- Documentation changes
- Project context bundle

### Outputs

Typical outputs include:

- Review summary
- Acceptance criteria checklist
- Test coverage assessment
- Issues found
- Required changes
- Optional improvements
- Recommendation

Expected handoff artifact: review-report.md.

### Quality Bar

A review is complete when:

- The story is checked against the actual changes
- Tests and verification are considered
- Risks are clearly stated
- Required fixes are separated from optional improvements
- The human reviewer has enough information to make a decision

## Human Owner

The human owner remains responsible for final judgment.

Agents can recommend, implement, and review, but they should not be treated as the final authority.

The human owner is responsible for:

- Confirming the story is worth doing
- Approving final scope
- Approving architecture decisions
- Reviewing final code
- Running or confirming verification
- Creating commits
- Opening pull requests
- Merging work
- Deciding whether work is production-worthy

## Handoff Expectations

Each agent should produce output that the next agent can use directly.

A good handoff should include:

- What was reviewed
- What decisions were made
- What assumptions remain
- What files or concepts are relevant
- What the next agent should focus on
- What the next agent should avoid changing

## Escalation Rules

An agent should stop and flag the issue when:

- The story goal is unclear
- Acceptance criteria conflict
- Required context is missing
- The requested change appears unsafe
- The implementation requires a major architecture decision
- The work is much larger than expected
- Tests cannot reasonably validate the change
- The agent would need to guess instead of reason from context
- The work may expose secrets, credentials, private data, or unsafe tool access

## Definition of Done for Agent Workflow

A story is complete only when:

- The story has clear acceptance criteria
- Architecture impact has been considered
- Test expectations have been defined
- Implementation addresses the acceptance criteria
- Tests have been added or updated as appropriate
- Verification has been performed or clearly documented
- Review has been completed
- Human approval has been given
- The final commit message accurately describes the work