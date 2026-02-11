# hello-world

Accepts a topic as input and calls OpenAI to generate a one-sentence response about that topic.

## Usage

```bash
# Local
python workflows/hello-world/main.py bananas

# Via Modal webhook
curl -X POST https://info-1266--hello-world-run-modal.modal.run \
  -H "Authorization: Bearer <MODAL_BEARER_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"topic": "bananas"}'
```

## Environment Variables

This workflow loads env vars from the root `.env` first, then from `workflows/hello-world/.env` (overrides).

See the root `.env.example` for shared vars (e.g. `OPENAI_API_KEY`, `MODAL_BEARER_TOKEN`). Copy this workflow's `.env.example` to `.env` only if you need workflow-specific overrides.

## Deploy Target

Local + Modal
