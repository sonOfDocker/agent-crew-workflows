# STORY: Add README Usage Notes for Story Workflow

## Problem Statement
New users of the Agent Crew project may not know how to run the Story Readiness workflow. Currently, the instructions are spread across multiple documents or are missing from the main README.

## Goal
Add a "Usage" section to the root README.md that clearly explains how to run the story workflow with a sample command.

## Non-Goals
- Documenting every internal agent detail.
- Adding documentation for future workflows not yet implemented.
- Creating a full tutorial website.

## Requirements
- Clear, copy-pasteable command.
- Explanation of required input files (`--context-file` and `--story-file`).
- Mention of the output directory and generated artifacts.

## Acceptance Criteria
- [ ] Root README.md contains a "Usage" or "Getting Started" section.
- [ ] A sample command using `python scripts/run_story_workflow.py` is present.
- [ ] The six standard output artifacts are listed.
- [ ] The human-review requirement is explicitly mentioned.

## Suggested Tasks
1. Identify the best location in README.md for the usage notes.
2. Draft the usage instructions.
3. Verify the sample command matches the current implementation.
4. Apply the changes to README.md.
