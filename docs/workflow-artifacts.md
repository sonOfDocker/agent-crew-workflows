# Workflow Artifacts

This document defines the standard markdown output artifacts produced by the MVP agent workflow. Consistent artifacts make workflow output predictable, reviewable, and useful across different project stories.

## Global Artifact Rules

All generated artifacts must follow these rules. Detailed guardrail rules can be found in [Workflow Guardrails](./workflow-guardrails.md).

### Rule 1: Human review warning
Each artifact must include a visible note that the output is advisory and requires human review.
**Recommended wording:**
> Note: This artifact is AI-generated planning support. It is not proof of implementation, test success, or story completion. Human review is required.

### Rule 2: No unsupported completion claims
Artifacts must not claim implementation is complete, tests passed, acceptance criteria are satisfied, or pull requests are ready to merge unless actual evidence is provided.

### Rule 2a: Evidence Reviewed section
The `review-notes.md` artifact must include an `Evidence Reviewed` section that lists what evidence was available (or states if none).

### Rule 3: Assumptions must be labeled
Any inferred or uncertain detail must be listed under an assumptions section or clearly labeled as an assumption.

### Rule 4: Missing information must be surfaced
Agents should identify missing information instead of silently inventing details.

### Rule 5: Evidence must be separated from recommendations
Artifacts must distinguish between evidence reviewed, recommendations, assumptions, open questions, and human decisions needed.

### Rule 5a: Required Human Actions section
The `final-summary.md` artifact must include a `Required Human Actions` section listing specific actions or decisions needed from the human owner.

### Rule 6: Acceptance criteria must remain visible
Where relevant, artifacts should map recommendations back to acceptance criteria. The test plan and review notes must explicitly reference acceptance criteria.

### Rule 7: Markdown must be stable and readable
Artifacts should use consistent markdown headings, bullets, and simple formatting.

### Rule 8: Output files must use stable names
The workflow uses the following stable artifact file names:
- `story-refinement.md`
- `architecture-notes.md`
- `test-plan.md`
- `implementation-plan.md`
- `review-notes.md`
- `final-summary.md`

### Rule 9: Repository safety
Generated artifacts must only be written to the configured output directory. The workflow runner must not modify source code or documentation files outside the output directory.

---

## Artifact 1: `story-refinement.md`

### Purpose
Captures the Story Refiner Agent’s improved understanding of the story. Helps the human owner determine whether the story is clear enough for implementation planning.

### Required Sections
- `# Story Refinement`
- `## Source Story Summary`: Briefly summarize the original story.
- `## Refined Story Summary`: Clearer version of the story goal and expected outcome.
- `## Requirements`: Functional and non-functional requirements.
- `## Acceptance Criteria Review`: Review clarity and completeness; suggest improvements if needed.
- `## Assumptions`: List inferred but unverified details.
- `## Open Questions`: Questions requiring human clarification.
- `## Out of Scope`: Items not included in the current story.
- `## Readiness Assessment`: State if story is ready, partially ready, or not ready.
- `## Human Review Needed`: Specific decisions or confirmations needed.

---

## Artifact 2: `architecture-notes.md`

### Purpose
Captures the Architect Agent’s design review and implementation-shaping guidance. Helps understand project impact, risks, and design boundaries.

### Required Sections
- `# Architecture Notes`
- `## Architecture Summary`: Recommended architectural direction.
- `## Relevant Context`: Important project context used.
- `## Impacted Areas`: Files, packages, modules, folders, or docs affected.
- `## Proposed Approach`: Recommended approach to guide implementation.
- `## Alternatives Considered`: Reasonable alternatives and why they weren't selected.
- `## Risks and Tradeoffs`: Complexity, maintainability, or scope concerns.
- `## Documentation Impact`: Required updates to docs, ADRs, or READMEs.
- `## Human Review Needed`: Decisions requiring human confirmation.

---

## Artifact 3: `test-plan.md`

### Purpose
Captures the Test Strategist Agent’s plan for validating the story. Translates requirements into concrete test scenarios.

### Required Sections
- `# Test Plan`
- `## Test Strategy Summary`: Overall testing approach.
- `## Acceptance Criteria Mapping`: Map each AC to one or more validation steps.
- `## Required Tests`: Tests required for completion.
- `## Optional Tests`: Useful but non-required tests.
- `## Edge Cases`: Failure modes, boundary cases, or unusual inputs.
- `## Suggested Test Commands`: Example: `pytest`.
- `## Required Evidence`: Evidence needed (e.g., test output, artifacts).
- `## Human Review Needed`: Decisions requiring human confirmation.

---

## Artifact 4: `implementation-plan.md`

### Purpose
Captures the Developer Agent’s planned implementation sequence. Guides the work without claiming it is already completed.

### Required Sections
- `# Implementation Plan`
- `## Implementation Summary`: Intended implementation approach.
- `## Planned File Changes`: Expected files/directories to create or update.
- `## Step-by-Step Plan`: Ordered implementation steps.
- `## Test Execution Plan`: When and how tests should be run.
- `## Risks and Blockers`: Implementation risks or dependencies.
- `## Assumptions`: Assumptions affecting the plan.
- `## Completion Evidence Needed`: Artifacts or results needed before completion.
- `## Human Approval Needed Before Changes`: Explicit statement of required approval.

---

## Artifact 5: `review-notes.md`

### Purpose
Captures the Reviewer Agent’s review of the generated workflow artifacts or completed work.

### Required Sections
- `# Review Notes`
- `## Review Summary`: Review outcome summary.
- `## Artifacts Reviewed`: List of artifacts (e.g., `test-plan.md`).
- `## Acceptance Criteria Status`: Status of each AC (e.g., satisfied, unclear).
- `## Evidence Reviewed`: List of evidence available (or state if none).
- `## Issues Found`: Problems, inconsistencies, or unsupported claims.
- `## Required Changes`: Changes required before approval.
- `## Suggested Improvements`: Non-blocking improvements.
- `## Final Recommendation`: Use one of: `approve for next step`, `changes requested`, `blocked`, or `needs human decision`.
- `## Human Decision Needed`: Decisions the human owner must make.

---

## Artifact 6: `final-summary.md`

### Purpose
Captures a concise summary of the full workflow run.

### Required Sections
- `# Final Summary`
- `## Workflow Run Summary`: What the workflow did.
- `## Inputs Used`: Context file, story file, output directory, and timestamp.
- `## Artifacts Generated`: List of generated file names.
- `## Key Findings`: Most important findings.
- `## Open Questions`: Unresolved questions from across artifacts.
- `## Required Human Actions`: Actions the human owner should take next.
- `## Limitations`: State limitations (e.g., no code was changed).
- `## Recommended Next Step`: One clear next step.
