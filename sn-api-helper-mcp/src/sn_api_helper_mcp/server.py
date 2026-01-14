"""MCP server setup and tool registration."""

from __future__ import annotations

from typing import Any

from fastmcp import FastMCP

from .tools import register_tools


def create_server() -> FastMCP[Any]:
    """Create and FastMCP server instance."""

    mcp: FastMCP[Any] = FastMCP("sn-api-helper-mcp")
    register_tools(mcp)
    return mcp
