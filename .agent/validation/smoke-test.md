# Smoke Test Suite

Quick validation that all workflows can at least be imported and have the expected structure.

## How to Run

Run these checks against each workflow listed in CATALOG.md with status "Done" or "Deployed".

## Setup

Install shared dependencies from the project root:
```bash
pip install -r requirements.txt
```

## Per-Workflow Checks

For each workflow in `workflows/`:

### Structure Check
- [ ] `README.md` exists and is non-empty
- [ ] `main.py` exists and is valid Python (compiles without errors)

### Import Check
```bash
cd workflows/{name}
python -c "import main"
```
Should complete without import errors (may fail on missing env vars — that's OK for a smoke test).

### Dependency Check
```bash
pip install -r requirements.txt --dry-run
```
All shared dependencies should resolve without conflicts.

## Results

| Workflow | Structure | Import | Last Checked |
|----------|-----------|--------|-------------|
| *(none yet)* | | | |
