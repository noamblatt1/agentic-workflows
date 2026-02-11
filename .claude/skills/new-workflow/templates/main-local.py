"""
{workflow-name} — {description}

Usage:
    python workflows/{workflow-name}/main.py
"""

from pathlib import Path

from dotenv import load_dotenv

# Load .env files locally
_here = Path(__file__).resolve().parent
_root = _here.parents[1]
load_dotenv(_root / ".env")
load_dotenv(_here / ".env", override=True)


def run() -> str:
    """Core logic."""
    # TODO: implement
    return "done"


if __name__ == "__main__":
    print(run())
