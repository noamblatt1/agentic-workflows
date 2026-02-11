# Agentic Workflows

A collection of standalone, AI-powered workflow scripts and deployable functions built with [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Each workflow lives in its own directory under `workflows/` and can run locally or be deployed to [Modal](https://modal.com) as a serverless endpoint.

The project is designed to be developed interactively with Claude Code using **skills** — reusable prompt templates that handle scaffolding, building, and managing workflows so you can focus on the logic.

## Project Structure

```
.agent/
  plans/              # Implementation plans (one per workflow)
  validation/         # Shared validation utilities
.claude/
  skills/             # Claude Code skills (invoked with /skill-name)
    build/            # /build — execute a workflow plan
    new-workflow/     # /new-workflow — scaffold a new workflow
    onboard/         # /onboard — get oriented in the codebase
    list-workflows/  # /list-workflows — show all runnable workflows
    workflow-conventions/  # /workflow-conventions — reference for project patterns
workflows/
  {workflow-name}/    # Each workflow directory
    README.md
    main.py
    .env.example
requirements.txt      # Shared Python dependencies (all workflows)
CATALOG.md            # Index of all workflows and their status
CLAUDE.md             # AI agent instructions and conventions
```

## Getting Started

### 1. Install dependencies

```bash
python bootstrap.py
```

This creates a `.venv` virtual environment and installs everything from the root `requirements.txt`.

### 2. Set up environment variables

Copy the example env file and fill in your API keys:

```bash
cp .env.example .env
```

### 3. Create a new workflow

In Claude Code, run:

```
/new-workflow my-workflow-name
```

This scaffolds a new directory under `workflows/`, creates a plan template in `.agent/plans/`, and adds an entry to `CATALOG.md`. Fill in the plan with your implementation details.

### 4. Build the workflow

```
/build my-workflow-name
```

Claude reads the plan and implements the workflow end-to-end — writing code, installing dependencies, running validation, and updating the catalog.

### 5. Run locally

```bash
.venv/Scripts/python.exe workflows/{name}/main.py
```

### 6. Deploy to Modal (optional)

Workflows with a Modal deploy target include a `run_modal()` function that can be deployed as a serverless endpoint:

```bash
modal deploy workflows/{name}/main.py
```

## Skills

Skills are Claude Code prompt templates that automate common development tasks. Invoke them in a Claude Code session with `/{skill-name}`.

| Skill | Description |
|-------|-------------|
| `/new-workflow <name>` | Scaffold a new workflow with directory structure, templates, and a plan file |
| `/build <name>` | Execute a workflow's plan — implements, tests, and updates the catalog |
| `/list-workflows` | Show all workflows with their status, args, and deploy targets |
| `/onboard` | Get a full overview of the project's current state |
| `/workflow-conventions` | Reference guide for project structure, env patterns, and development flow |

## Environment Variables

Env vars use a two-tier system:

1. **Root `.env`** — shared variables (API keys, bearer tokens) loaded first. Copy `.env.example` to `.env`.
2. **Workflow `.env`** — optional per-workflow overrides loaded second. Only needed for workflow-specific config.

Secrets are never committed. For Modal deployments, use Modal secrets.

## See Also

- [CATALOG.md](CATALOG.md) — Status of all workflows
- [CLAUDE.md](CLAUDE.md) — Development conventions
