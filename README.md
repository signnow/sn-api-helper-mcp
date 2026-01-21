# SignNow API Helper MCP
[![PyPI](https://img.shields.io/pypi/v/sn-api-helper-mcp)](https://pypi.org/project/sn-api-helper-mcp/)
[![License](https://img.shields.io/github/license/signnow/sn-api-helper-mcp)](https://github.com/signnow/sn-api-helper-mcp/blob/main/LICENSE.md)

An MCP server for SignNow API helper tools (stdio only).

mcp-name: io.github.signnow/sn-api-helper-mcp

## Purpose & Capabilities

The SignNow API Helper MCP server is a custom Model Context Protocol server designed specifically to assist with SignNow API integration. It acts as an intelligent assistant that understands the SignNow API ecosystem to provide contextual help for developers.

**Core Functions:**

- **API Documentation Access:** Retrieve and display SignNow API documentation, endpoints, and parameters.
- **Code Examples:** Generate and provide sample code for common SignNow API operations.
- **Authentication Help:** Assist with SignNow API authentication methods and token management.
- **Integration Guidance:** Provide best practices for implementing SignNow e-signature workflows.
- **Error Resolution:** Help troubleshoot common SignNow API issues and error codes.

**Use Cases:**

- **Document Signing Workflows:** Help implement complex signing processes with multiple signers.
- **API Integration:** Generate code for uploading documents, creating signature requests, and tracking status.
- **Development Support:** Provide real-time assistance during SignNow API development.
- **Best Practices:** Ensure proper implementation of SignNow security and compliance requirements.

---

## 📦 Installation

To install locally for development:
`pip install -e .`

## 🚀 Run

You can run the server using Python or `uvx`:

**Method 1: Python module**`python -m sn_api_helper_mcp serve`

**Method 2: Installed CLI entry point**`sn-api-helper-mcp serve`

**Method 3: UVX** `uvx sn-api-helper-mcp`

---

## 🔌 Integrations & Setup

You can use this server with any MCP client. Below are the configurations for the most popular IDEs and apps.

### 1. Claude Desktop

To use SignNow tools directly inside the Claude app:

1. Open your config file:
    - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
    - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the following to the `mcpServers` object:

```jsx
{
  "mcpServers": {
    "signnow-api-helper": {
      "command": "uvx",
      "args": [
        "sn-api-helper-mcp"
      ]
    }
  }
}
```

1. Restart Claude Desktop.

### 2. Cursor AI

Cursor supports MCP natively.

1. Open **Cursor Settings** (`Cmd/Ctrl + ,`).
2. Go to **Features** > **MCP Servers**.
3. Click **+ Add New MCP Server**.
4. Add the following to the `mcpServers` object:

```jsx
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

1. Install the **Cline** extension from the VS Code Marketplace.
2. Open Cline settings (click the gear icon inside the Cline chat window) -> **MCP Servers**.
3. Add the configuration JSON:

```jsx
{
  "signnow-api-helper": {
    "command": "uvx",
    "args": [
      "sn-api-helper-mcp"
    ]
  }
}
```

## ✨ Features
- **Transport:** stdio only
- **Available Tools:**
    - `get_signnow_api_info` - Fetching API reference documentation.
