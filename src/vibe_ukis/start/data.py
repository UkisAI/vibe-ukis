import os
from typing import Literal
from pathlib import Path
from importlib.resources import files

agent_rules = {
    "Cursor": ".cursor/rules/",  # Directory for rules
    "Claude Code": ".claude/skills/",  # Directory for skills
    "Windsurf": ".windsurf/rules/",  # Directory for rules
    "Antigravity": ".antigravity/rules/",  # Directory for rules
}


LibraryName = Literal["LlamaIndex", "Chainlit", "Firecrawl", "Qdrant"]


# Use importlib.resources to locate documentation files
# This works both in development and when the package is installed
def _get_doc_path(filename: str) -> str:
    """Get the path to a documentation file, handling both dev and installed modes."""
    # Try installed package location first
    try:
        doc_path = files("vibe_ukis").joinpath("documentation", filename)
        path_str = str(doc_path)
        if os.path.exists(path_str):
            return path_str
    except (TypeError, FileNotFoundError, AttributeError):
        pass

    # Fallback to development location (project root)
    package_root = Path(__file__).parent.parent.parent.parent
    dev_path = package_root / "documentation" / filename
    if dev_path.exists():
        return str(dev_path)

    # If neither exists, return the dev path (will be caught by error handling later)
    return str(dev_path)


services: dict[LibraryName, str] = {
    "LlamaIndex": _get_doc_path("llamaindex.md"),
    "Chainlit": _get_doc_path("chainlit.md"),
    "Firecrawl": _get_doc_path("firecrawl.md"),
    "Qdrant": _get_doc_path("qdrant.md"),
}
