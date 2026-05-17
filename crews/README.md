# Crews

This directory contains CrewAI crew definitions and workflow implementations.

The initial project should define the workflow contracts in documentation before adding runtime automation here.

## Purpose

The `crews/` directory is where executable agent workflows will live.

Future crew implementations may include:

- Story refinement crew
- Architecture review crew
- Test strategy crew
- Development crew
- Review crew
- End-to-end development workflow crew

## Planned Structure

The expected first crew implementation is:

```text
crews/
└── development/
    ├── agents.yaml
    ├── tasks.yaml
    ├── crew.py
    ├── main.py
    └── README.md
```

## Current Status

No production crew implementation exists yet.

This directory is reserved for the future CrewAI MVP milestone.