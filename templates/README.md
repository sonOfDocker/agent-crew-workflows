# Templates

This directory contains reusable templates for Agent Crew Workflows.

Templates should make stories, prompts, reviews, handoffs, and workflow inputs consistent across projects.

## Purpose

The `templates/` directory provides standard formats that can be reused by humans and agents.

Templates may include:

- Story templates
- Prompt templates
- Review templates
- Agent handoff templates
- Architecture note templates
- Test strategy templates
- Commit message templates

## Template Principles

Templates should follow these principles:

- Be easy to copy and paste.
- Be readable in plain markdown.
- Make expectations explicit.
- Reduce ambiguity for agents.
- Keep workflow outputs consistent.
- Avoid unnecessary ceremony.
- Support real development work.

## Planned Templates

Expected templates include:

- `story-template.md`
- `review-template.md`
- `handoff-template.md`
- `test-strategy-template.md`
- `commit-message-template.md`

## Usage

Templates should be treated as starting points.

A template can be adapted to fit the story, but important sections should not be removed unless they are clearly not relevant.

When a section does not apply, prefer writing:

```text
Not applicable.
```

This is better than silently deleting the section because it makes the decision visible.

## Current Status

The first required template is `story-template.md`.

Additional templates should be added as the workflow matures.