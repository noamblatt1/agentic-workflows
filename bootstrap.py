"""Bootstrap script: creates .venv and installs dependencies."""

import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"
REQUIREMENTS = ROOT / "requirements.txt"

IS_WIN = sys.platform == "win32"
PIP = VENV_DIR / "Scripts" / "pip.exe" if IS_WIN else VENV_DIR / "bin" / "pip"
ACTIVATE = (
    str(VENV_DIR / "Scripts" / "activate")
    if IS_WIN
    else f"source {VENV_DIR / 'bin' / 'activate'}"
)


def main():
    if VENV_DIR.exists():
        print(f".venv already exists at {VENV_DIR}")
    else:
        print("Creating virtual environment...")
        venv.create(VENV_DIR, with_pip=True)
        print("Virtual environment created.")

    print("Installing dependencies...")
    subprocess.check_call([str(PIP), "install", "-r", str(REQUIREMENTS)])

    print()
    print("Setup complete! Activate the venv with:")
    print(f"  {ACTIVATE}")


if __name__ == "__main__":
    main()
