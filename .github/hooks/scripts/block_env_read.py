#!/usr/bin/env python3
"""Deny agent tool calls that attempt to read environment files."""

from __future__ import annotations

import json
import sys
from pathlib import PurePath

READ_TOOLS = {"read_file", "grep_search", "file_search"}
BLOCK_REASON = (
    "Reading .env files is blocked by project policy. "
    "Use environment variables or a secrets manager instead."
)


def is_environment_file(value: object) -> bool:
    """Return whether a value names .env or a .env.<name> file."""
    if not isinstance(value, str):
        return False

    filename = PurePath(value.replace("\\", "/")).name.casefold()
    return filename == ".env" or filename.startswith(".env.")


def contains_environment_file(value: object) -> bool:
    """Recursively find protected file paths in tool input."""
    if isinstance(value, dict):
        return any(contains_environment_file(item) for item in value.values())
    if isinstance(value, list):
        return any(contains_environment_file(item) for item in value)
    return is_environment_file(value)


def main() -> int:
    """Read hook event and deny protected file reads."""
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    tool_name = event.get("tool_name", "")
    tool_input = event.get("tool_input", {})
    if tool_name not in READ_TOOLS or not contains_environment_file(tool_input):
        return 0

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": BLOCK_REASON,
                }
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
