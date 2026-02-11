# Plan: {workflow-name}

**Complexity:** Simple | Medium | Complex
**Deploy Target:** Local | Local + Modal
**Modal Mode:** N/A | Webhook | Scheduled | Manual | Webhook + Scheduled | Webhook + Manual
**Status:** Planned

## Overview

{What this workflow does in 2-3 sentences. What problem does it solve?}

## Inputs

- {What data/files/APIs does it consume?}

## Outputs

- {What does it produce? Files, API responses, side effects?}

## Dependencies

- {New Python packages to add to root requirements.txt}
- {External services: APIs, databases, etc.}
- {Environment variables required}

## Implementation Tasks

### Task 1: {Description}
- [ ] {Subtask}
- [ ] {Subtask}
- **Validate:** {How to verify this task is done correctly}

### Task 2: {Description}
- [ ] {Subtask}
- [ ] {Subtask}
- **Validate:** {How to verify this task is done correctly}

## Validation

### Smoke Test
- {Minimal test to verify the workflow runs end-to-end}

### Edge Cases
- {What happens with empty input?}
- {What happens if an API is down?}
- {What happens with malformed data?}

## Modal Deployment Checklist (if Deploy Target is Local + Modal)

- [ ] `.env` loading is guarded (no bare `parents[2]` — will crash on Modal)
- [ ] Modal mode(s) declared — determines which entry points to create
- [ ] If webhook mode: using `@modal.fastapi_endpoint` (not deprecated `@modal.web_endpoint`)
- [ ] If webhook mode: `fastapi[standard]` included in the Modal image
- [ ] If webhook mode: bearer token auth via `webhook-auth` secret + `MODAL_BEARER_TOKEN` env var
- [ ] If webhook mode: tested all three auth cases: no token (422), wrong token (401), correct token (200)
- [ ] If scheduled mode: `modal.Cron` used (not `modal.Period` which resets on redeploy)
- [ ] If scheduled/manual mode: no fastapi or webhook-auth needed — keep it simple
- [ ] All pip dependencies in the Modal image
- [ ] Shared `image` variable when multiple Modal functions exist
- [ ] Deployed using Python subprocess wrapper on Windows

## Notes

- {Any gotchas, design decisions, or context for the builder}
