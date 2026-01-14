[![PyPI](https://img.shields.io/pypi/v/sn-api-helper-mcp)](https://pypi.org/project/sn-api-helper-mcp/)
[![Python Versions](https://img.shields.io/pypi/pyversions/sn-api-helper-mcp)](https://pypi.org/project/sn-api-helper-mcp/)
[![License](https://img.shields.io/github/license/signnow/sn-api-helper-mcp)](https://github.com/signnow/sn-api-helper-mcp/blob/main/LICENSE.md)

# SignNow Api Helper MCP

MCP server for SignNow API helper tools (stdio only).

## Installation

```bash
pip install -e .
```

## Run

```bash
python -m sn_api_helper_mcp serve
```

or

```bash
sn-api-helper-mcp serve
```

or

```bash
uvx sn-api-helper-mcp
```

## Features

- Transport: stdio only
- Tools: `get_signnow_api_info` - Get information about SignNow API
