[English](README.md) • [Deutsch](README.de.md) • **日本語**

# AIを活用したVectorworks開発

AIは、互いに補完し合う2つの方法で、Vectorworksの図面での作業を支援できます。

- **固定スクリプト — Python API:** AIを使って、Vectorworksで実行する処理を定義したスクリプトを作成できます。内容を確認してテストした後、予測可能なワークフローとして繰り返し利用できます。
- **MCP接続 — スクリプトと図面操作ツール:** AIクライアントをVectorworksに直接接続できます。Pythonスクリプトの作成、保存、実行を支援したり、MCPツールを使って図面を操作したりできます。事前に定義したスクリプトを使わずにツールを直接使用する場合、AIは依頼内容と図面の状況に応じて操作を選ぶため、実行する操作の順序は変わることがあります。

## Python API

Python APIを使って、Vectorworks用の固定スクリプトを作成できます。AIツールを使うと、確認、テスト、実行できるスクリプトを作成できます。スクリプト、その入力値、ファイルの状態によって結果が決まる、明確なワークフローが得られます。

APIとスクリプト開発向けのAIコンテキストについては、[Python APIドキュメント](PythonAPI.ja/README.md)をご覧ください。

## MCPサーバー

> [!NOTE]
> お客様は、[こちらからベータ版へのアクセスを申請できます](https://www3.vectorworks.net/mcp-server-public-beta-group)。フォームに記入すると、Vectorworks MCP Server Public Beta Groupに参加できます。この[Vectorworks Forum](https://forum.vectorworks.net/)の非公開グループのメンバーとして、知見やヒント、コツを共有したり、他のメンバーや専門家に相談したりできます。

Vectorworks MCPサーバーを使うと、互換性のあるAIクライアントを[Model Context Protocol（MCP）](https://modelcontextprotocol.io)経由でVectorworksに直接接続できます。MCPは、AIアプリケーションを外部の機能やコンテキストに接続するためのオープンな標準規格です。この接続では、スクリプトの開発と実行に加え、幅広いMCPツールによる図面の直接操作も行えます。

主な特長:

- **ローカルで動作:** サーバーはお使いのコンピューター上で実行され、HTTPでクライアントと通信します。リクエストをホスト型MCPサービス経由で送るのではなく、起動中のVectorworksにクライアントを接続します。
- **スクリプトに対応:** AIクライアントはPython APIを使って、Vectorworks内でスクリプトを直接作成、保存、実行できます。
- **図面を操作:** MCPツールは、ファイルのコンテキスト、図面オブジェクトとジオメトリ、リソース、インターフェイスへのアクセス、製品固有のワークフローなどを扱います。AIがこれらのツールを直接使用する場合、固定スクリプトに従うのではなく、依頼内容と利用可能なコンテキストに応じて操作を選択します。

接続方法と利用可能なツールについては、[MCPサーバーのドキュメント](MCP.ja/README.md)をご覧ください。

## 外部AIクライアントのMCP設定

GitHub Copilot、Claude Desktop、Claude CodeでMCPサポートをインストールして設定する手順については、[ToolsのREADME](Tools/READ_ME.ja.md)をご覧ください。
