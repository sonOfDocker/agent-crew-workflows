# MCP

This directory is reserved for Model Context Protocol integration notes, configuration, examples, and future adapters.

MCP integrations should be added carefully because they may give agents access to tools, files, repositories, terminals, project boards, or other systems.

## Purpose

The `mcp/` directory should help document and organize future MCP usage for Agent Crew Workflows.

Potential MCP integrations may include:

- GitHub issue and pull request access
- Filesystem access
- Documentation search
- Test runner access
- Local development environment access
- Project management tools
- Knowledge base tools

Initial workflows should rely on prepared context bundles before granting agents direct MCP tool access.

## Safety Principles

MCP integrations should follow these principles:

- Prefer read-only access first.
- Require explicit human approval for write actions.
- Avoid giving agents broad permissions before the workflow is proven.
- Document every tool an agent can access.
- Document what each tool is allowed to do.
- Keep secrets out of committed files.
- Treat repository, terminal, and GitHub write access as high-risk.
- Keep human approval as the final gate before commits, pull requests, merges, or deployments.

## Planned Structure

```text
mcp/
├── README.md
├── github/
│   └── README.md
├── filesystem/
│   └── README.md
└── examples/
    └── README.md
```

## Current Status

No MCP integrations are active yet.

This directory is reserved for future MCP exploration after the basic workflow contracts and CrewAI MVP are in place.