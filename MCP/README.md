**English** • [Deutsch](../MCP.de/README.md) • [日本語](../MCP.ja/README.md)

# Vectorworks MCP Server

## What Is MCP?

The Model Context Protocol (MCP) is an open protocol for connecting AI applications to external capabilities and context. An MCP server describes what it can provide, and an MCP client can discover those capabilities and make requests using a common protocol.

## Vectorworks Local HTTP Server

The Vectorworks MCP server connects MCP clients to capabilities implemented in Vectorworks. The implementation is organized into capability groups and uses the Vectorworks APIs to inspect and work with document data. It covers areas such as document context, drawing objects and geometry, resources, interface access, scripting, and product-specific workflows. The individual capability catalog is documented separately; this README intentionally does not enumerate tools.

This implementation is a local HTTP MCP server. It runs on the user's machine and communicates with MCP clients over HTTP, allowing a compatible client to connect to the Vectorworks instance without routing the integration through a hosted MCP service.

| Version | Reference |
| --- | --- |
| Vectorworks 2027 Update 2 | [v2027.2](v2027.2/README.md) |

## Start and Connect

In the default workspaces (all except Viewer), choose **Tools > MCP Server > Start MCP Server...**. A custom workspace may place the commands elsewhere or not have them. The **Start MCP Server** dialog has:

- **Tools mode**: **Enable all tools** (the default), **Enable all without scripting tools** or **Enable scripting tools only**. See [Tool groups and activation](v2027.2/Common.md#tool-groups-and-activation).
- **Server port**: 1 to 65535, default 8765. If the port is busy, the server tries up to 9 more ports (never above 65535), and the dialog shows the URL with the port in use.
- **Start Server** and **Stop Server**, and **Copy URL**, which copies the server URL, for example `http://localhost:8765`.
- Links to the AI Scripting Documentation and the MCP Tools Documentation, and the version.

The mode and the port can be changed only while the server is stopped, and they are saved after a successful start. **Close** closes the dialog; a running server keeps running. **Stop Server** or **Tools > MCP Server > Stop MCP Server** stops it.

Add the URL as an HTTP MCP server in your MCP client, and open a drawing in Vectorworks: without an open drawing the tools return `no active Vectorworks document`. The server:

- listens only on `127.0.0.1` and serves one connection at a time;
- speaks JSON-RPC 2.0 over HTTP with the MCP protocol version `2024-11-05` and the methods `initialize`, `ping`, `tools/list` and `tools/call`; send requests with `POST` (any path) and `Content-Type: application/json`;
- answers `GET /` with `{service, version, protocol}`, any other `GET` with 404 and any other method with 405;
- refuses with 403 a request whose `Host` is not `127.0.0.1:<port>` or `localhost:<port>`, whose `Origin`, when sent, is not `http://` or `https://` followed by `localhost` or `127.0.0.1` and an optional `:<port>` (nothing else: `null`, `[::1]` or a path are refused), or that sends `Host` or `Origin` more than once, and with 415 a `POST` whose `Content-Type` is not a single `application/json` header;
- has no authentication: any program on this computer can call the offered tools. Choose **Enable all without scripting tools** to keep the script runs off, and stop the server when you do not use it.
- answers a notification, such as `notifications/initialized`, with HTTP 200 and an empty body, and reports `capabilities.tools.listChanged: true`; when the client accepts `text/event-stream`, the response to `activateToolGroups` is an event stream that carries `notifications/tools/list_changed` before the result.

## AI-Assisted Fixed Scripts

AI can also help you develop ("vibe-code") a fixed script for a repeatable task. Instead of letting an AI client choose actions dynamically on each run, you review and test the generated script, then reuse it without AI making decisions during execution.

This provides a deterministic workflow: the script follows predefined logic, with results depending on its inputs and the document state. See the [Python API documentation](../PythonAPI/README.md) for creating these scripts and the AI context to use when developing them.
