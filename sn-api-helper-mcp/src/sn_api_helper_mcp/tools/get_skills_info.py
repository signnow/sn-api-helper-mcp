"""Get SignNow API information tool implementation."""

from typing import Annotated, Any

import httpx
from fastmcp import Context
from pydantic import Field


def bind(mcp: Any) -> None:
    @mcp.tool(
        name="get_signnow_api_info",
        description="Get information about SignNow API. This is documentation for API usage.",
        tags=["signnow", "api", "documentation"],
    )
    def get_signnow_api_info(
        ctx: Context,
        query: Annotated[
            str,
            Field(description="Query string to search for API information (e.g., 'free form invite')"),
        ],
    ) -> str:
        """
        Make a POST request to SignNow API information endpoint and return the result.

        Args:
            query: Query string to search for API information

        Returns:
            JSON response from the API as a string
        """
        url = "https://integrations-copilot.signnow.com/api/skills/getInfo"
        payload = {"query": query}

        response = httpx.post(
            url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30.0,
        )
        response.raise_for_status()
        return response.text
