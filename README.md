[![PyPI](https://img.shields.io/pypi/v/sn-api-helper-mcp)](https://pypi.org/project/sn-api-helper-mcp/)
[![License](https://img.shields.io/github/license/signnow/sn-api-helper-mcp)](https://github.com/signnow/sn-api-helper-mcp/blob/main/LICENSE.md)

# SignNow Api Helper MCP

MCP server for SignNow API helper tools (stdio only).

mcp-name: io.github.signnow/sn-api-helper-mcp

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

## 🔌 Integrations & Setup

You can use this server with any MCP client. Below are the configurations for the most popular IDEs and apps.

### 1. Claude Desktop

To use SignNow tools directly inside Claude app:

1.  Open your config file:
    * **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
    * **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
2.  Add the following to the `mcpServers` object:

```json
{
  "mcpServers": {
    "signnow-api-helper": {
      "command": "uvx",
      "args": ["sn-api-helper-mcp"]
    }
  }
}

```

3. Restart Claude Desktop.

### 2. Cursor AI

Cursor now supports MCP natively.

1. Open **Cursor Settings** (Cmd/Ctrl + ,).
2. Go to **Features** > **MCP Servers**.
3. Click **+ Add New MCP Server**.
4. Add the following to the `mcpServers` object:

```json
{
  "mcpServers": {
    "signnow-api-helper": {
      "command": "uvx",
      "args": ["sn-api-helper-mcp"]
    }
  }
}

```


### 3. Visual Studio Code (via Cline)

VS Code uses the **Cline** extension (or similar MCP clients) to interact with MCP servers.

1. Install the **Cline** extension from the VS Code Marketplace.
2. Open Cline settings (click the gear icon inside the Cline chat window) -> **MCP Servers**.
3. Add the configuration JSON:

```json
{
  "signnow-api-helper": {
      "command": "uvx",
      "args": ["sn-api-helper-mcp"]
    }
}

```


## Features

- Transport: stdio only
- Tools: `get_signnow_api_info` - Get information about SignNow API
