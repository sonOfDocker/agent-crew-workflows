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
- [x] `crews/story_readiness/crew.py` is implemented and loads agents/tasks from YAML.
- [x] `crews/story_readiness/main.py` is implemented as the entry point.
- [x] The workflow successfully reads a `{project_context}` variable.
- [x] The workflow successfully reads a `{story_input}` variable.
- [ ] A sample execution can be run via command line.
- [x] Handoff artifacts (story-refinement.md, etc.) are produced in an output directory.

## Affected Areas
- `crews/story_readiness/crew.py` (new)
- `crews/story_readiness/main.py` (new)
- `crews/story_readiness/story-6.md` (updated)
- `docs/roadmap.md` (updated)
