**English** • [Deutsch](READ_ME.de.md) • [日本語](READ_ME.ja.md)

## Contents

- [Start the MCP server in Vectorworks](#start-the-mcp-server-in-vectorworks)
- [GitHub Copilot Desktop](#github-copilot-desktop)
- [GitHub Copilot in VS Code](#github-copilot-in-vs-code)
- [Claude Desktop](#claude-desktop)
- [Claude Code](#claude-code)

# Connect an AI client to Vectorworks

## Start the MCP server in Vectorworks

1. Open a drawing in Vectorworks on the same computer as your AI client.
2. Choose **Tools > MCP Server > Start MCP Server...**, then **Start Server**.
3. Click **Copy URL**. Use the HTTP URL shown in the dialog: Vectorworks may choose a different port if the requested one is busy. Keep the server running while you use the client.

## GitHub Copilot Desktop

GitHub Copilot Desktop connects directly to the HTTP URL. No plugin or bundle is needed.

1. In GitHub Copilot Desktop, open the **Customize** pane.
2. Click **+ Add**, then select **Add MCP Server**.
3. Paste the URL copied from Vectorworks, name the server `vectorworks`, and save. If you are asked for the server type, choose **HTTP**.
4. In a new chat, ask Copilot to list the layers in the active drawing to check the connection.

## GitHub Copilot in VS Code

Copilot in VS Code also connects directly to the HTTP URL. No plugin or bundle is needed.

1. In the VS Code Command Palette, run **MCP: Add Server** and select **HTTP**.
2. Paste the URL copied from Vectorworks, name the server `vectorworks`, and choose where to save the configuration.
3. Run **MCP: List Servers**, select `vectorworks`, and start it if needed. In Copilot Chat, ask it to list the layers in the active drawing to check the connection.

## Claude Desktop

1. Download the Vectorworks extension for your computer: [macOS bundle](files/mac/vworks_mcp_server.mcpb) or [Windows bundle](files/win/vworks_mcp_server.mcpb).
2. In Claude Desktop, open **Settings > Extensions > Advanced settings > Install Extension...**, select the downloaded `.mcpb` file, and confirm the installation.
3. In the extension settings, paste the copied URL into **Vectorworks MCP server address** and save. In a new chat, ask Claude to list the layers in the active drawing.

## Claude Code

Claude Code uses the same bundle inside a local plugin. You do not need to install Claude Desktop.

1. In a terminal, run `claude plugin init vectorworks`. It prints the path to your personal `vectorworks` plugin folder.
2. Copy the [macOS bundle](files/mac/vworks_mcp_server.mcpb) or [Windows bundle](files/win/vworks_mcp_server.mcpb) into that folder, **next to** `.claude-plugin`, not inside it. Leave the bundle zipped and keep its filename.
3. In the plugin folder, set `.claude-plugin/plugin.json` to:

   ```json
   {
     "name": "vectorworks",
     "mcpServers": "./vworks_mcp_server.mcpb"
   }
   ```

4. Start a new Claude Code session. Run `/plugin`, select **Installed > vectorworks > Configure**, and paste the copied URL into **Vectorworks MCP server address**. Run `/mcp` to confirm that the Vectorworks server is connected.