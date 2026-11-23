[English](../PythonAPI/README.md) • [Deutsch](../PythonAPI.de/README.md) • **日本語**

# Python APIドキュメント

各バージョンの下にある対応する<u>**AI-CONTEXT.md**</u>をAIツールにコンテキストとして渡すと、このAPIを使ったコードやスクリプトの生成に役立ちます（いわゆる「Vibe Coding」）。

Vectorworks Python `api`モジュールのリファレンスドキュメント（Vectorworksのバージョン別）:

| バージョン | リファレンス | AIコンテキスト |
| --- | --- | --- |
| Vectorworks 2027 Update 2 | [v2027.2](v2027.2/README.md) | [AI-CONTEXT.md](../PythonAPI/v2027.2/AI-CONTEXT.md) |

## MCP接続

[Vectorworks MCPサーバー](../MCP.ja/README.md)を使うと、互換性のあるAIクライアントをVectorworksに接続し、アプリケーション内でPythonスクリプトを直接作成、保存、実行できます。この接続を通じて、クライアントはPython APIを参照しながら、スクリプトを開発、テスト、実行できます。

事前に定義したスクリプトを使わず、同じ接続を通じて多数のMCPツールで図面を操作することもできます。この非決定的なワークフローでは、AIが依頼内容と現在の図面の状態に基づいて使用するツールを選ぶため、操作の順序は変わることがあります。スクリプトの開発とツールによる直接操作は、個別に行うことも、同じワークフロー内で組み合わせることもできます。
