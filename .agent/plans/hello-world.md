# Plan: hello-world

**Complexity:** Simple
**Deploy Target:** Local
**Status:** Planned

## Overview

Accepts a topic as input and calls the OpenAI API to generate a one-sentence response about that topic. A minimal first workflow to verify the project structure works end-to-end.

## Inputs

- A topic string (provided as a CLI argument or prompted interactively)

## Outputs

- A one-sentence response about the topic, printed to stdout

## Dependencies

- `openai`, `python-dotenv`, `pydantic` — in root `requirements.txt`
- **Environment variables:** `OPENAI_API_KEY`

## Implementation Tasks

### Task 1: Implement OpenAI call
- [ ] Import and configure the OpenAI client
- [ ] Send a chat completion request with a system prompt and the user's topic
- [ ] Return the one-sentence response
- **Validate:** Run `python workflows/hello-world/main.py "black holes"` and verify a sentence is printed

### Task 2: Add input handling
- [ ] Accept topic from CLI args or prompt the user interactively
- [ ] Validate that the topic is not empty
- **Validate:** Run with no args and verify it prompts or uses a default

## Validation

### Smoke Test
- Run `python workflows/hello-world/main.py "quantum computing"` and confirm a single sentence is returned

### Edge Cases
- What happens with an empty topic? Should use a sensible default or error
- What happens if `OPENAI_API_KEY` is missing? Should fail with a clear error message
- What happens if the OpenAI API is down? Should surface the error cleanly

## Notes

- Use `gpt-4o-mini` or similar cheap model since this is a hello-world workflow
- Keep the system prompt simple: "Respond with exactly one sentence about the given topic."
