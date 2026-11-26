[English](READ_ME.md) • [Deutsch](READ_ME.de.md) • **日本語**

## 目次

- [Vectorworks で MCP サーバーを起動する](#vectorworks-で-mcp-サーバーを起動する)
- [GitHub Copilot Desktop](#github-copilot-desktop)
- [GitHub Copilot（VS Code）](#github-copilot-vs-code)
- [Claude Desktop](#claude-desktop)
- [Claude Code](#claude-code)

# AI クライアントを Vectorworks に接続する

## Vectorworks で MCP サーバーを起動する

1. AI クライアントと同じコンピューターで Vectorworks を起動し、図面を開きます。
2. **Tools > MCP Server > Start MCP Server...** を選び、**Start Server** をクリックします。
3. **Copy URL** をクリックします。指定したポートが使用中の場合、Vectorworks は別のポートを選ぶことがあるため、ダイアログに表示された HTTP URL を使います。クライアントの使用中はサーバーを起動したままにします。

## GitHub Copilot Desktop

GitHub Copilot Desktop は HTTP URL に直接接続します。プラグインやバンドルは不要です。

1. GitHub Copilot Desktop で **Customize** ペインを開きます。
2. **+ Add** をクリックし、**Add MCP Server** を選びます。
3. Vectorworks からコピーした URL を貼り付け、サーバー名に `vectorworks` を入力して保存します。サーバーの種類を尋ねられた場合は **HTTP** を選びます。
4. 新しいチャットで Copilot に「現在の図面のレイヤを一覧表示して」と依頼し、接続を確認します。

## GitHub Copilot（VS Code）

VS Code の Copilot も HTTP URL に直接接続します。プラグインやバンドルは不要です。

1. VS Code のコマンドパレットで **MCP: Add Server** を実行し、**HTTP** を選びます。
2. Vectorworks からコピーした URL を貼り付け、サーバー名に `vectorworks` を入力し、設定の保存先を選びます。
3. **MCP: List Servers** を実行して `vectorworks` を選び、停止していれば起動します。Copilot Chat で「現在の図面のレイヤを一覧表示して」と依頼し、接続を確認します。

## Claude Desktop

1. コンピューターに合う Vectorworks 拡張機能をダウンロードします：[macOS 用バンドル](files/mac/vworks_mcp_server.mcpb) または [Windows 用バンドル](files/win/vworks_mcp_server.mcpb)。
2. Claude Desktop で **Settings > Desktop App > Extensions > Advanced settings > Install Extension...** を開き、ダウンロードした `.mcpb` ファイルを選んでインストールを確定します。
3. 拡張機能の設定で **Vectorworks MCP server address** にコピーした URL を貼り付けて保存します。新しいチャットで Claude に「現在の図面のレイヤを一覧表示して」と依頼します。

## Claude Code

Claude Code では同じバンドルをローカルプラグインとして読み込みます。Claude Desktop をインストールする必要はありません。

1. ターミナルで `claude plugin init vectorworks` を実行します。個人用の `vectorworks` プラグインフォルダーのパスが表示されます。
2. [macOS 用バンドル](files/mac/vworks_mcp_server.mcpb) または [Windows 用バンドル](files/win/vworks_mcp_server.mcpb) を、そのフォルダーにコピーします。配置先は `.claude-plugin` の中ではなく、**同じ階層**です。バンドルは展開せず、ファイル名も変更しません。
3. プラグインフォルダー内の `.claude-plugin/plugin.json` を次の内容にします。

   ```json
   {
     "name": "vectorworks",
     "mcpServers": "./vworks_mcp_server.mcpb"
   }
   ```

4. Claude Code の新しいセッションで `/plugin` を実行し、**Installed > vectorworks > Configure** を選びます。**Vectorworks MCP server address** にコピーした URL を貼り付け、`/mcp` で Vectorworks サーバーが接続されていることを確認します。
