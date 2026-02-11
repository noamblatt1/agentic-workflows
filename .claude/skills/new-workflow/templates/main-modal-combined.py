"""
{workflow-name} — {description}

Usage:
    python workflows/{workflow-name}/main.py
    modal deploy workflows/{workflow-name}/main.py
"""

import os
from pathlib import Path

import fastapi
import modal
from dotenv import load_dotenv

# Load .env files locally only (on Modal, secrets are injected as env vars)
_here = Path(__file__).resolve().parent
if (_here / ".env").exists() or len(_here.parents) > 2:
    _root = _here.parents[1]
    load_dotenv(_root / ".env")
    load_dotenv(_here / ".env", override=True)

app = modal.App("{workflow-name}")
image = modal.Image.debian_slim(python_version="3.14").pip_install(
    "fastapi[standard]",
    # TODO: add workflow-specific packages
)


def run() -> str:
    """Core logic — shared by all entry points, no Modal dependency."""
    # TODO: implement
    return "done"


@app.function(
    secrets=[
        modal.Secret.from_name("webhook-auth"),
        # TODO: add workflow-specific secrets
    ],
    image=image,
)
@modal.fastapi_endpoint(method="POST")
def run_modal(authorization: str = fastapi.Header()):
    """Secured webhook — validates bearer token, then runs."""
    expected = os.getenv("MODAL_BEARER_TOKEN")
    if authorization != f"Bearer {expected}":
        raise fastapi.HTTPException(status_code=401, detail="Unauthorized")
    return {"result": run()}


@app.function(
    schedule=modal.Cron("0 9 * * *"),  # TODO: adjust schedule
    image=image,
)
def run_scheduled():
    """Runs on cron. Also triggerable via Modal dashboard 'Run now'."""
    result = run()
    print(result)
    return result


if __name__ == "__main__":
    print(run())
