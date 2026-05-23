# STORY #6: Implement Context and Story Input Loading

## Story Type
- Milestone

## Status
- In Progress

## Summary
Implement the capability for the Story Readiness Crew to load project context from a markdown bundle and story input from a markdown file.

## Problem / Context
Currently, the agents are documented but not executable. We need a way to pass the accumulated project knowledge (context) and the specific work request (story) into the CrewAI workflow so the agents can perform their tasks based on real project data.

## Goal
Enable the Story Readiness Crew to run locally, reading from `context-bundle.md` and `current-story.md` (or similar files), and producing the expected handoff artifacts.

## Acceptance Criteria
- [x] `crews/story_readiness/inputs.py` implemented with `WorkflowInputs` model and `load_workflow_inputs` function.
- [x] Robust validation (rejects directories, empty files, unreadable files).
- [x] `crews/story_readiness/main.py` refactored to use the reusable input loader.
- [x] CLI provides concise success summary with paths and size counts.
- [x] Focused test coverage added in `tests/test_inputs.py`.
- [x] Documentation updated in `crews/story_readiness/README.md`.

## Affected Areas
- `crews/story_readiness/inputs.py` (new)
- `crews/story_readiness/main.py` (updated)
- `crews/story_readiness/story-6.md` (updated)
- `docs/roadmap.md` (updated)
- `tests/test_inputs.py` (new)
