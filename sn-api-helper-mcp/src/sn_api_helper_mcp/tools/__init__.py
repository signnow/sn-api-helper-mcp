"""Tool registration entrypoint."""

from typing import Any

from . import get_skills_info


def register_tools(mcp: Any) -> None:
    get_skills_info.bind(mcp)