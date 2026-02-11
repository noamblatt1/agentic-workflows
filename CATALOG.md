# Workflow Catalog

Central index of all workflows in this project. Updated by `/build` on completion.

## Workflows

| Workflow | Status | Complexity | Deploy Target | Modal Mode | Args | Description |
|----------|--------|------------|---------------|------------|------|-------------|
| hello-world | Deployed | Simple | Local + Modal | Webhook | `<topic>` — subject to generate a sentence about (optional; prompts interactively if omitted) | Accepts a topic and calls OpenAI to generate a one-sentence response |

### Deploy Target Key
- **Local** — Runs locally only (`python main.py`)
- **Local + Modal** — Runs locally and deployable to Modal

### Modal Mode Key
- **N/A** — Local-only workflow, no Modal deployment
- **Webhook** — HTTP endpoint via `@modal.fastapi_endpoint`, callable by external systems
- **Scheduled** — Runs on a cron via `modal.Cron(...)`, also triggerable via Modal dashboard "Run now"
- **Manual** — Triggered on-demand from Modal dashboard "Run now" or `modal run` CLI
- Modes can be combined (e.g., **Webhook + Scheduled**) — each mode gets its own entry point function sharing the same core `run()` logic

### Status Key
- **Planned** — Plan created, not yet built
- **In Progress** — Currently being built
- **Done** — Built, tested, and working
- **Deployed** — Live in production (Modal, cron, etc.)
- **Archived** — No longer actively used

### Complexity Key
- **Simple** — Single-pass, straightforward
- **Medium** — Some iteration expected
- **Complex** — Broken into sub-tasks
