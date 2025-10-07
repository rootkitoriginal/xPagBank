from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def ensure_dir(path: Path) -> Path:
    """Create the directory tree for *path* if it does not exist and return the path."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_json(path: Path, data: Any) -> None:
    """Persist a Python object as UTF-8 JSON on disk."""
    ensure_dir(path.parent)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def write_text(path: Path, content: str, *, encoding: str = "utf-8") -> None:
    """Write text data to disk, creating parents when needed."""
    ensure_dir(path.parent)
    path.write_text(content, encoding=encoding)
