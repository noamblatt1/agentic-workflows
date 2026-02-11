"""hello-world: Accepts a topic and calls OpenAI to generate a one-sentence response."""

import os
import sys
from pathlib import Path

import fastapi
import modal
from dotenv import load_dotenv
from openai import OpenAI

# Load .env files locally only (on Modal, secrets are injected as env vars)
_here = Path(__file__).resolve().parent
if (_here / ".env").exists() or len(_here.parents) > 2:
    _root = _here.parents[1]
    load_dotenv(_root / ".env")
    load_dotenv(_here / ".env", override=True)

app = modal.App("hello-world")


def run(topic: str) -> str:
    """Core logic — no Modal dependency, works locally."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY is not set. Copy .env.example to .env and fill in your key.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Respond with exactly one sentence about the given topic."},
            {"role": "user", "content": topic},
        ],
    )
    return response.choices[0].message.content


@app.function(
    secrets=[
        modal.Secret.from_name("openai-secret"),
        modal.Secret.from_name("webhook-auth"),
    ],
    image=modal.Image.debian_slim(python_version="3.14").pip_install("openai", "fastapi[standard]"),
)
@modal.fastapi_endpoint(method="POST")
def run_modal(body: dict, authorization: str = fastapi.Header()):
    """Secured webhook — validates bearer token, then runs."""
    expected = os.getenv("MODAL_BEARER_TOKEN")
    if authorization != f"Bearer {expected}":
        raise fastapi.HTTPException(status_code=401, detail="Unauthorized")
    return {"result": run(body["topic"])}


if __name__ == "__main__":
    if len(sys.argv) > 1:
        topic = sys.argv[1]
    else:
        topic = input("Enter a topic: ").strip()
        if not topic:
            print("Error: Topic cannot be empty.")
            sys.exit(1)

    result = run(topic)
    print(result)
