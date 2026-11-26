[English](READ_ME.md) • **Deutsch** • [日本語](READ_ME.ja.md)

## Inhalt

- [MCP-Server in Vectorworks starten](#mcp-server-in-vectorworks-starten)
- [GitHub Copilot Desktop](#github-copilot-desktop)
- [GitHub Copilot in VS Code](#github-copilot-in-vs-code)
- [Claude Desktop](#claude-desktop)
- [Claude Code](#claude-code)

# Einen KI-Client mit Vectorworks verbinden

## MCP-Server in Vectorworks starten

1. Öffnen Sie in Vectorworks eine Zeichnung auf dem Computer, auf dem auch Ihr KI-Client läuft.
2. Wählen Sie **Tools > MCP Server > Start MCP Server...** und anschließend **Start Server**.
3. Klicken Sie auf **Copy URL**. Verwenden Sie die HTTP-URL aus dem Dialog: Ist der gewünschte Port belegt, kann Vectorworks einen anderen wählen. Lassen Sie den Server laufen, solange Sie den Client verwenden.

## GitHub Copilot Desktop

GitHub Copilot Desktop verbindet sich direkt mit der HTTP-URL. Dafür benötigen Sie weder ein Plugin noch ein Bundle.

1. Öffnen Sie in GitHub Copilot Desktop den Bereich **Customize**.
2. Klicken Sie auf **+ Add** und wählen Sie anschließend **Add MCP Server**.
3. Fügen Sie die aus Vectorworks kopierte URL ein, geben Sie dem Server den Namen `vectorworks` und speichern Sie. Wählen Sie **HTTP**, falls nach dem Servertyp gefragt wird.
4. Bitten Sie Copilot in einem neuen Chat, die Ebenen der aktiven Zeichnung aufzulisten, um die Verbindung zu prüfen.

## GitHub Copilot in VS Code

Auch Copilot in VS Code verbindet sich direkt mit der HTTP-URL. Dafür benötigen Sie weder ein Plugin noch ein Bundle.

1. Führen Sie in der Befehlspalette von VS Code **MCP: Add Server** aus und wählen Sie **HTTP**.
2. Fügen Sie die aus Vectorworks kopierte URL ein, geben Sie dem Server den Namen `vectorworks` und wählen Sie den Speicherort für die Konfiguration.
3. Führen Sie **MCP: List Servers** aus, wählen Sie `vectorworks` und starten Sie den Eintrag bei Bedarf. Bitten Sie Copilot Chat, die Ebenen der aktiven Zeichnung aufzulisten, um die Verbindung zu prüfen.

## Claude Desktop

1. Laden Sie die Vectorworks-Erweiterung für Ihren Computer herunter: [Bundle für macOS](files/mac/vworks_mcp_server.mcpb) oder [Bundle für Windows](files/win/vworks_mcp_server.mcpb).
2. Öffnen Sie in Claude Desktop **Settings > Desktop App > Extensions > Advanced settings > Install Extension...**, wählen Sie die heruntergeladene `.mcpb`-Datei und bestätigen Sie die Installation.
3. Fügen Sie in den Erweiterungseinstellungen die kopierte URL unter **Vectorworks MCP server address** ein und speichern Sie die Einstellung. Bitten Sie Claude in einem neuen Chat, die Ebenen der aktiven Zeichnung aufzulisten.

## Claude Code

Claude Code verwendet dasselbe Bundle in einem lokalen Plugin. Claude Desktop muss dafür nicht installiert sein.

1. Führen Sie im Terminal `claude plugin init vectorworks` aus. Der Befehl gibt den Pfad zu Ihrem persönlichen Plugin-Ordner `vectorworks` aus.
2. Kopieren Sie das [Bundle für macOS](files/mac/vworks_mcp_server.mcpb) oder das [Bundle für Windows](files/win/vworks_mcp_server.mcpb) in diesen Ordner, **neben** `.claude-plugin`, nicht in diesen Unterordner. Entpacken Sie das Bundle nicht und behalten Sie den Dateinamen bei.
3. Verwenden Sie im Plugin-Ordner für `.claude-plugin/plugin.json` folgenden Inhalt:

   ```json
   {
     "name": "vectorworks",
     "mcpServers": "./vworks_mcp_server.mcpb"
   }
   ```

4. Starten Sie eine neue Claude-Code-Sitzung. Führen Sie `/plugin` aus, wählen Sie **Installed > vectorworks > Configure** und fügen Sie die kopierte URL unter **Vectorworks MCP server address** ein. Prüfen Sie mit `/mcp`, ob der Vectorworks-Server verbunden ist.
