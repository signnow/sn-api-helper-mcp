"""CLI entrypoint for the MCP server (stdio only)."""

import logging
import sys

import typer

from ._version import __version__
from .server import create_server

app = typer.Typer(help="sn-api-helper MCP server")


@app.command()
def serve() -> None:
    """Run MCP server in standalone stdio mode."""
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)
    print(f"sn-api-helper MCP Server v{__version__}", file=sys.stderr)
    mcp = create_server()
    mcp.run(transport="stdio")


def main() -> None:
    app()
