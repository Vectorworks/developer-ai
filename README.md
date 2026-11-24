**English** • [Deutsch](README.de.md) • [日本語](README.ja.md)

# Developing for Vectorworks with AI

AI can help you work with Vectorworks drawings in two complementary ways:

- **Fixed scripts — Python API:** Use AI to develop a script that defines the operations performed in Vectorworks. Once reviewed and tested, the script can be reused for a predictable workflow.
- **MCP connection — scripts and drawing tools:** Connect an AI client directly to Vectorworks. It can help create, save, and run Python scripts, or use MCP tools to work with the drawing. When using the tools directly rather than a predefined script, the AI chooses actions based on the request and drawing context, so the sequence can vary.

## Python API

Use the Python API to create fixed scripts for Vectorworks. AI tools can help you write scripts that you can review, test, and run, giving you a defined workflow whose results depend on the script, its inputs, and the document state.

See the [Python API documentation](PythonAPI/README.md) to learn about the API and its AI context for script development.

## MCP Server

> [!NOTE]
> Customers can request [access to the beta here](https://www3.vectorworks.net/mcp-server-public-beta-group). Once you fill out the form, you’ll be admitted to the Vectorworks MCP Server Public Beta Group. And as a member of this private group on the [Vectorworks Forum](https://forum.vectorworks.net/), you’ll be able to share insights, tips and tricks, or seek guidance from peers and experts.

The Vectorworks MCP server lets compatible AI clients connect directly to Vectorworks through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), an open standard for connecting AI applications to external capabilities and context. The connection supports both script development and execution, and direct interaction with drawings through a broad set of MCP tools.

Highlights:

- **Runs locally**: The server runs on your machine and communicates with clients over HTTP, connecting them to your running Vectorworks instance rather than routing requests through a hosted MCP service.
- **Supports scripting**: An AI client can use the Python API to create, save, and run scripts directly in Vectorworks.
- **Works with drawings**: MCP tools cover document context, drawing objects and geometry, resources, interface access, and product-specific workflows. When the AI uses these tools directly, it selects actions based on the request and available context rather than following a fixed script.

See the [MCP Server documentation](MCP/README.md) to learn about the connection and available tools.

## MCP Setup for External AI Clients

For instructions on installing and configuring MCP support in GitHub Copilot, Claude Desktop, and Claude Code, see the [Tools README](Tools/READ_ME.md).
