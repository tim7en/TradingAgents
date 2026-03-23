from pathlib import Path

from dotenv import load_dotenv


def load_project_env(anchor: str | Path) -> Path | None:
    """Load the nearest project env file.

    Preference order:
    1. `.env`
    2. `.env.example`

    The search starts from the given file or directory and walks upward.
    Returns the loaded path, or None if nothing was found.
    """

    current = Path(anchor).resolve()
    if current.is_file():
        current = current.parent

    directories = [current, *current.parents]

    for filename in (".env", ".env.example"):
        for directory in directories:
            candidate = directory / filename
            if candidate.exists():
                load_dotenv(candidate, override=False)
                return candidate

    return None
