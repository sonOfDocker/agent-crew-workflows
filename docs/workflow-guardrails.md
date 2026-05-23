# Workflow Guardrails

This document defines the explicit guardrails and human checkpoints for the MVP agent-orchestrated development workflow. These rules ensure the workflow remains advisory, evidence-driven, and under human control.

## Guardrail Philosophy

The MVP workflow is treated as advisory planning support. Agents provide analysis, suggestions, and planning artifacts, but they do not perform final actions or make final decisions.

**Agents may:**
- Analyze story content and project context.
- Identify risks, assumptions, and open questions.
- Suggest acceptance criteria and test scenarios.
- Propose architecture and implementation steps.
- Review available evidence and recommend next steps.

**Agents must not independently:**
- Claim implementation is complete or tests passed.
- Approve a story as "Done".
- Modify repository files outside the configured output directory.
- Create commits or push branches.
- Open or merge pull requests.
- Close GitHub issues.
- Make final architecture or scope decisions.
- Override human approval requirements.

---

## 1. Evidence Guardrails

**Purpose:** Prevent agents from making claims that require proof unless proof is available.

**Rules:**
- Agents must not claim tests passed unless actual test output is provided.
- Agents must not claim builds passed unless actual build output is provided.
- Agents must not claim code was implemented unless the workflow has evidence of file changes.
- Agents must not claim acceptance criteria are satisfied unless evidence is available.
- Agents must separate recommendations from verified facts.
- Review artifacts must include an `Evidence Reviewed` section where applicable.

**Prohibited wording without evidence:**
- "All tests passed."
- "The implementation is complete."
- "This story is done."
- "Acceptance criteria are fully satisfied."

---

## 2. Assumption Guardrails

**Purpose:** Prevent agents from treating inferred details as facts.

**Rules:**
- Agents must label assumptions clearly.
- Agents must not invent missing project requirements or nonexistent files.
- Agents must not silently fill in important missing information.
- Agents must list open questions when the story lacks required detail.
- Artifacts must include `Assumptions` or `Open Questions` sections where relevant.

---

## 3. Scope Guardrails

**Purpose:** Keep the workflow focused on the current story and Epic 1 boundaries.

**Rules:**
- Agents must identify scope creep and flag work that belongs in a future story or epic.
- Agents must not add major capabilities to a story without calling them out.
- Agents must distinguish required work from optional improvements.
- The workflow must defer non-MVP capabilities unless separately approved.

---

## 4. Human Checkpoint Guardrails

**Purpose:** Make human decision points explicit.

Human approval is required before:
- Treating a story as implementation-ready.
- Accepting a major architecture decision.
- Changing source files.
- Running destructive commands.
- Claiming tests passed or marking AC as satisfied.
- Marking a story complete.
- Performing any repository-changing action (commit, push, open PR, merge PR).
- Closing GitHub issues or updating GitHub Projects.
- Expanding story scope beyond the approved requirement.

---

## 5. Repository Safety Guardrails

**Purpose:** Protect the repository from unintended modifications.

**Rules:**
- The MVP runner may write generated artifacts **only** to the configured output directory.
- The runner must not modify source code files.
- The runner must not create commits, push branches, or call GitHub write APIs.
- Any future repository-changing capability must be implemented in a separate story with explicit human approval rules.

---

## 6. Review Guardrails

**Purpose:** Ensure the Reviewer Agent provides cautious, evidence-based feedback.

**Rules:**
- The Reviewer Agent must identify what artifacts and evidence were reviewed.
- The Reviewer Agent must map review status back to acceptance criteria.
- The Reviewer Agent must use cautious statuses (e.g., `not yet verifiable`) when evidence is missing.
- Final recommendations must be limited to: `approve for next step`, `changes requested`, `blocked`, `needs human decision`, or `not yet verifiable`.

---

## Deferred Capabilities (Epic 1)

The following capabilities are explicitly deferred from Epic 1 and are outside the current workflow scope:
- GitHub write automation (Issues, Projects, PRs).
- Autonomous code changes or commits.
- MCP server integration.
- Remote execution.
- Multi-repository orchestration.
- Long-term run history database.
- UI-based workflow management.
