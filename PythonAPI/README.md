**English** • [Deutsch](../PythonAPI.de/README.md) • [日本語](../PythonAPI.ja/README.md)

# Python API documentation

Use the corresponding <u>**AI-CONTEXT.md**</u> below as a context for AI tool to generate code with this API, a.k.a. vibe-code scripts.

Reference documentation of the Vectorworks Python `api` module, by Vectorworks version:

| Version | Reference | AI Context |
| --- | --- | --- |
| Vectorworks 2027 Update 2 | [v2027.2](v2027.2/README.md) | [AI-CONTEXT.md](v2027.2/AI-CONTEXT.md) |

## MCP Connection

The [Vectorworks MCP server](../MCP/README.md) lets a compatible AI client connect to Vectorworks to help create, save, and execute Python scripts directly in the application. Through this connection, the client can look up the Python API and run scripts as you develop and test them.

You can also use the same connection to work with your drawing through a large set of MCP tools, without a predefined script. In this non-deterministic workflow, the AI chooses which tools to use based on your request and the drawing's current state, so the sequence of actions can vary. Script development and direct tool interaction can be used separately or combined in the same workflow.
