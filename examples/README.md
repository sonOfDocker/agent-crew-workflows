# Examples

This directory contains example inputs and outputs for Agent Crew Workflows.

Examples should make it easier to understand how stories, context bundles, workflow runs, and review outputs are expected to look before full automation is added.

## Purpose

The `examples/` directory is used for sample files that demonstrate the workflow without requiring a real project or live GitHub issue.

Examples may include:

- Sample story files
- Sample context bundles
- Sample workflow inputs
- Sample agent handoffs
- Sample review outputs
- Sample commit messages

## Planned Structure

```text
examples/
├── stories/
│   └── example-story.md
├── context-bundle.example.md
├── handoffs/
│   └── example-handoff.md
└── reviews/
    └── example-review.md
```

## Usage

Example files should be safe to commit.

Do not include real secrets, private project data, credentials, API keys, or sensitive information in this directory.

## Current Status

This directory is reserved for sample workflow assets.

The first useful examples should be added after the story template and context bundling approach are defined.