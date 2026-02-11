# CLAUDE.md

Standalone workflow scripts and deployable functions. Each workflow lives in its own directory under `workflows/`.

## Running Python
Always use `.venv/Scripts/python.exe` instead of bare `python` when running scripts or installing packages via Bash.

## Conventions
- Python 3.14+
- Each workflow is independent — no shared state between workflows unless explicitly noted
- Secrets via `.env` files (never committed) or Modal secrets
- Use Pydantic for structured data and validation
- Raw SDK calls only — no heavyweight frameworks unless the workflow specifically needs one
- **Single root `requirements.txt`** — all Python dependencies live in the project root, shared across workflows

## Workflow Development
Use `/new-workflow` to scaffold, `/build` to implement, `/list-workflows` to see what's runnable, `/onboard` for full project state.

## Windows Notes
- On Windows with MINGW/Git Bash, some commands produce no output. Use PowerShell or Python subprocess wrappers.
- `modal deploy` needs the UTF-8 Python wrapper — see the build skill's [modal-patterns.md](.claude/skills/build/reference/modal-patterns.md).
