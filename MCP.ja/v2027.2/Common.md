[English](../../MCP/v2027.2/Common.md) • [Deutsch](../../MCP.de/v2027.2/Common.md) • **日本語**

# Common — 共通の規則

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

Vectorworks MCPサーバーのすべてのツールが従う規則です: 呼び出しと結果、オブジェクト参照、点と色、単位、作成オプション、適用した設定、プラグインパラメータ、ページ分割、作用、リスクレベル、取り消し。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [ツールグループと有効化](#tool-groups-and-activation)
- [Coreグループ](#core-group)
  - [listToolGroups](#listtoolgroups)
  - [activateToolGroups](#activatetoolgroups)
  - [runToolBatch](#runtoolbatch)
- [ツールの呼び出し](#calling-a-tool)
- [結果とエラー](#results-and-errors)
- [オブジェクト参照](#object-references)
- [点、矩形、色](#points-rectangles-and-colors)
  - [点](#points)
  - [矩形](#rectangles)
  - [色](#colors)
- [単位と角度](#units-and-angles)
- [作成オプション](#creation-options)
- [適用した設定](#applied-settings)
- [プラグインパラメータ](#plug-in-parameters)
  - [パラメータの読み取り](#reading-parameters)
  - [パラメータの書き込み](#writing-parameters)
- [ページ分割](#paging)
- [作用とリスクレベル](#effects-and-risk-levels)
- [取り消し](#undo)

<a id="overview"></a>

## 概要

| 項目 | 内容 |
|---|---|
| [ツールグループと有効化](#tool-groups-and-activation) | 利用できるツールと、グループを有効にする方法。 |
| [Coreグループ](#core-group) | 常に利用できる3つのメタツール: `listToolGroups`、`activateToolGroups`、`runToolBatch`。 |
| [ツールの呼び出し](#calling-a-tool) | 呼び出しとその結果の形式、および例。 |
| [結果とエラー](#results-and-errors) | 結果オブジェクト、エラーメッセージ、ロールバックされる呼び出し。 |
| [オブジェクト参照](#object-references) | ツールが引数と結果でオブジェクトを識別する方法。 |
| [点、矩形、色](#points-rectangles-and-colors) | ジオメトリと色に共通する値の形式。 |
| [単位と角度](#units-and-angles) | ワールド単位、ラジアン、および少数の例外。 |
| [作成オプション](#creation-options) | ほとんどの作成ツールが受け付けるオプション: クラス、名前、選択。 |
| [適用した設定](#applied-settings) | ツールが書き込んだ内容を設定ごとに報告する方法。 |
| [プラグインパラメータ](#plug-in-parameters) | プラグインオブジェクトのパラメータの読み取りと書き込み。 |
| [ページ分割](#paging) | 長いリストをページごとに返す方法。 |
| [作用とリスクレベル](#effects-and-risk-levels) | ツールが変更し得る内容と、クライアントでの扱い方。 |
| [取り消し](#undo) | ツール呼び出しによる変更を「編集 &gt; 取り消し」用に記録する方法。 |

<a id="tool-groups-and-activation"></a>

## ツールグループと有効化

ツールはツールグループに整理されています。サーバーのツール一覧（`tools/list`）には**有効な**グループのツールだけが表示されるため、一覧にないツールが必ずしも未対応とは限りません。

- 初期状態で有効なグループは4つです: Document、Selection、IFC、Objects。**Core**グループは常に有効です。
- その他のグループは[`activateToolGroups`](#activatetoolgroups)で有効にします。有効にしたグループは、サーバーが停止または再起動されるまで有効なままです。サーバーは接続ではなく有効化の状態を保持するため、有効化はすべてのクライアントに適用されます。その後、ツール一覧を更新してください（`list_changed`通知を処理するクライアントは自動的に更新します）。
- [`listToolGroups`](#listtoolgroups)は、有効、無効を問わずすべてのグループを一覧表示し、`includeTools`を指定するとそのツールの名前と説明も返します。
- グループは、表示名またはグループIDで指定します。どちらも受け付けられます。
- **MCPサーバーを起動**ダイアログで選ぶ**ツールモード**によって、サーバーがそもそもどのグループを提供するかが決まります。
  - **すべてのツールを有効化**（デフォルト）: すべてのグループが提供されます。
  - **スクリプトツールを除くすべてを有効化**: 7つのツールを持つ[Scripting](Scripting.md#scripting)グループは登録されません。`listToolGroups`には表示されず、`activateToolGroups`はこのグループを`not_found`で報告します。
  - **スクリプトツールのみを有効化**: （Coreグループのほかに）Scriptingグループだけが提供され、すぐに有効になります。

| グループ | グループID | ページ | 初期状態で有効 | リスクレベル | ツール数 | 概要 |
|---|---|---|---|---|---|---|
| [Core](#core-group) | `core` | [Common](#core-group) | 常に有効 | 低 | 3 | ツールグループを検出して有効にし、複数のツール呼び出しを1つの取り消しステップとして実行します。 |
| [Document](DocumentAccess.md#document) | `document` | [DocumentAccess](DocumentAccess.md) | はい | 低 | 17 | アクティブな図面を扱います: ファイルの概要、レイヤ、ストーリ、クラス、単位、ビュー、ファイル設定。 |
| [Selection](DocumentAccess.md#selection) | `selection` | [DocumentAccess](DocumentAccess.md) | はい | 中 | 3 | 現在の選択内容を一覧表示し、移動、回転、拡大縮小、複製、グループ化、削除、クラス変更を一括で行います。 |
| [IFC](IFC.md#ifc) | `ifc` | [IFC](IFC.md) | はい | 低 | 4 | 読み取り専用のIFCデータ: オブジェクトのIFCエンティティとプロパティセット、IFCプロパティセットの定義（標準とカスタム）、およびファイルのカスタムプロパティセットです。 |
| [IFC Data Mapping](IFC.md#ifc-data-mapping) | `ifc-data-mapping` | [IFC](IFC.md) | いいえ | 低 | 2 | アクティブファイルのデータマネージャのIFCマッピング定義を読み取ります。 |
| [Menus](MenuAccess.md#menus) | `menus` | [MenuAccess](MenuAccess.md) | いいえ | 高 | 4 | メニューコマンドの検索、メニューバーの読み取り、コマンドを現在実行できるかどうかの確認、およびその実行を行います。 |
| [Draw2D](ObjectPrimitives.md#draw2d) | `draw2d` | [ObjectPrimitives](ObjectPrimitives.md) | いいえ | 低 | 15 | 2Dプリミティブの作成、編集、測定、合成と、文字列オブジェクトの作成、読み取り、編集を行います。 |
| [Objects](ObjectPrimitives.md#objects) | `objects` | [ObjectPrimitives](ObjectPrimitives.md) | はい | 中 | 12 | あらゆるオブジェクトの検索、調査、編集を行い、属性、変形、コンテナ、プラグインパラメータ、レコードを扱います。 |
| [3D Modeling](Objects3D.md#3d-modeling) | `3d-modeling` | [Objects3D](Objects3D.md) | いいえ | 中 | 16 | ソリッド、3D 多角形、メッシュ、NURBS曲線と曲面、サーフェスモデルを作成、読み取り、編集します。 |
| [Annotation](ObjectsAnnotation.md#annotation) | `annotation` | [ObjectsAnnotation](ObjectsAnnotation.md) | いいえ | 中 | 8 | データタグ、図面枠、およびファイルの表題欄のプロジェクトデータを扱います。 |
| [Dimensioning](ObjectsAnnotation.md#dimensioning) | `dimensioning` | [ObjectsAnnotation](ObjectsAnnotation.md) | いいえ | 中 | 8 | 直線寸法、角度寸法、円弧長寸法、円寸法、およびセンターマークを扱います。 |
| [Architecture](ObjectsArchitect.md#architecture) | `architecture` | [ObjectsArchitect](ObjectsArchitect.md) | いいえ | 中 | 9 | BIMの建築要素：壁、スラブ、屋根、ドア、窓、柱、階段。 |
| [ConnectCAD](ObjectsConnectCAD.md#connectcad) | `connectcad` | [ObjectsConnectCAD](ObjectsConnectCAD.md) | いいえ | 中 | 10 | JSONのDevice記述データから構築する、ConnectCADの配線略図のDevice、Socket、Device Type。 |
| [Landmark](ObjectsLandmark.md#landmark) | `landmark` | [ObjectsLandmark](ObjectsLandmark.md) | いいえ | 中 | 10 | 植栽、舗床、ランドスケープエリア、地形モデル、造成図形、レベルオブジェクト、境界線、既存樹木。 |
| [Spotlight](ObjectsSpotlight.md#spotlight) | `spotlight` | [ObjectsSpotlight](ObjectsSpotlight.md) | いいえ | 中 | 5 | SpotlightのLighting Deviceと、それらが使用するGDTF器具タイプ。 |
| [Object Info](OIPAccess.md#object-info) | `object-info` | [OIPAccess](OIPAccess.md) | いいえ | 中 | 3 | 現在の選択に対するオブジェクト情報パレットを、ユーザーと同じように読み取り、操作します。 |
| [Resources](Resources.md#resources) | `resources` | [Resources](Resources.md) | いいえ | 中 | 11 | リソースを一覧表示、取り込み、作成、確認、編集、適用し、ワークシートを読み取り、編集します。 |
| [Scripting](Scripting.md#scripting) | `scripting` | [Scripting](Scripting.md) | いいえ | 高 | 7 | Pythonスクリプトの実行、Pythonスクリプトリソースの読み取りと保存、およびPythonの`api`モジュールの参照を行います。 |
| [InteractiveTools](ToolAccess.md#interactivetools) | `interactivetools` | [ToolAccess](ToolAccess.md) | いいえ | 高 | 10 | ツールパレットの対話型Vectorworksツールを、ユーザーと同じように操作します。 |

<a id="core-group"></a>

## Coreグループ

> **グループ:** `Core` · **グループID:** `core` · **有効状態:** 常に有効 · **リスクレベル:** 低 · **ツール数:** 3

**ツールグループを検出して有効にし、複数のツール呼び出しを1つの取り消しステップとして実行します。**

Coreグループのメタツールは常に利用できます。ツール一覧を管理し、ツール呼び出しをまとめます。[`runToolBatch`](#runtoolbatch)内からは呼び出せません。

| ツール | 作用 | リスク | 概要 |
|---|---|---|---|
| [`listToolGroups`](#listtoolgroups) | 読み取り専用 | 低 | 有効、無効を問わずすべてのツールグループを、有効状態と、必要に応じてそのツールとともに一覧表示します。 |
| [`activateToolGroups`](#activatetoolgroups) | セッション設定 | 低 | サーバーが停止されるまで、ツールグループを有効にして、そのツールをツール一覧に表示します。 |
| [`runToolBatch`](#runtoolbatch) | 編集（バッチ） | 中 | 複数のツール呼び出しを、全成功または全取り消しの1つの取り消しステップとして実行します。 |

### listToolGroups

有効、無効を問わずすべてのツールグループを、有効状態と、必要に応じてそのツールとともに一覧表示します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 不可

**詳細**

有効および無効のツールグループを、メタデータと有効状態とともに一覧表示します。機能が未対応だと判断する前に、`group`（表示名またはgroupId）と`includeTools` trueで関連するグループを調べ、有効化やスキーマなしでそのツール名と説明を確認してください。必要なグループを有効にし、tools/listを更新してから、そのツールを使用してください。有効なツール一覧にないことは、未対応を意味しません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `group` | string |  | 調べるグループの表示名またはgroupId（省略可能）。 |
| `includeTools` | boolean |  | 無効なグループについても、ツール名と説明を含めます。スキーマは含みません。デフォルト: `false`。 |

**結果**

`{ "groups": [...] }`。グループごとに1つのエントリです。Coreグループが先頭で、他のグループの順序は定義されていません。`group`を指定しない場合はすべてのグループが返され、指定した場合はそのグループだけが返されます。

| キー | 説明 |
|---|---|
| `groupId` | グループID（例: `3d-modeling`）。 |
| `displayName` | グループ名（例: `3D Modeling`）。 |
| `shortDescription` | グループを有効にするタイミング。 |
| `safetyLevel` | `low`、`medium`、`high`のいずれか。 |
| `currentlyActive` | グループのツールがツール一覧にある場合は`true`。 |
| `toolCount` | グループのツール数。 |
| `tools` | `includeTools`を指定した場合のみ: `{ "name", "description", "safetyLevel" }`のリスト。独自のリスクレベルを持たないツールには、グループのリスクレベルが設定されます。 |

エラー: `listToolGroups requires an arguments object`、`includeTools must be a boolean`、`group must be a display name or groupId string`、`Unknown tool group: <value>`。

**引数の例**

```json
{
  "group": "architecture",
  "includeTools": true
}
```

### activateToolGroups

サーバーが停止されるまで、ツールグループを有効にして、そのツールをツール一覧に表示します。

> **作用:** セッション設定 · **リスク:** 低 · **取り消し:** なし（図面は変更されません） · **runToolBatch内:** 不可

**詳細**

1つ以上のツールグループをセッションの残りの間有効にし、その後のtools/listリクエストでそのツールを公開します。各エントリには、listToolGroupsが報告するグループの表示名またはgroupIdのどちらでも指定できます。有効化の後、新しく公開されたツールを呼び出す前に、tools/listを更新してください（またはクライアントのlist_changed処理で更新させてください）。有効化はツールの利用可否を変更するもので、図面の内容は変更せず、編集ツールの使用を許可するものでもありません。

> **注:** 「セッションの残りの間」とは、サーバーが停止または再起動されるまでを意味します。有効化はクライアントの接続ではなくサーバーに属するため、すべてのクライアントに適用されます。グループを再び無効にすることはできません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `groups` | array of string | はい | 有効にするグループの表示名またはgroupId。 |

**結果**

`{ "activated": [...], "already_active": [...], "not_found": [...] }`。

- `activated`と`already_active`には、グループの表示名が列挙されます。
- `not_found`には、どのグループも指さないエントリがそのまま列挙されます（例: ツールモード「スクリプトツールを除くすべてを有効化」でのScriptingグループ）。
- 文字列ではないエントリはスキップされ、2回指定されたグループは1回だけ報告されます。
- `groups`配列がない場合、結果は`{ "err": "activateToolGroups requires a 'groups' array" }`です。
- クライアントが`text/event-stream`を受け付ける場合、サーバーはイベントストリームとして応答します: 最初に`notifications/tools/list_changed`メッセージ、次に結果です。それ以外の場合は通常のJSON-RPC応答を送るため、クライアントが自分でツール一覧を更新する必要があります。サーバーは、グループが変わらなかった場合や結果に`err`がある場合も含め、すべての`activateToolGroups`呼び出しでこれを行います。

**引数の例**

```json
{
  "groups": ["architecture", "Dimensioning"]
}
```

### runToolBatch

複数のツール呼び出しを、全成功または全取り消しの1つの取り消しステップとして実行します。

> **作用:** 編集（バッチ） · **リスク:** 中 · **取り消し:** バッチ全体で1ステップ「MCP: &lt;name&gt;」 · **runToolBatch内:** 不可

**詳細**

複数のツール呼び出しを、「MCP: &lt;name&gt;」という1つのVectorworksの取り消しステップとして、全成功または全取り消しで実行します。「この4枚の壁とスラブを作成する」など、独立した複数の呼び出しで構成される1つのユーザー作業に使用すると、1回の取り消しで作業全体を元に戻せます。`calls`は指定順に実行され、各要素はツールを直接呼び出す場合と同じ{ tool, arguments }です（argumentsのデフォルトは{}）。最大50個です。同じバッチ内で作成したオブジェクトのUUIDなど、同じバッチ内の前の呼び出しの結果を使用することはできません。その場合は、1つのrunPythonScriptを記述してください。

`undoStep` true、`undoName`、`results`（呼び出しごとの{ tool, result }）を返します。呼び出しが失敗した場合（結果に`err`がある、または例外）、バッチは停止し、それまでに行ったことはすべて元に戻されます: `err`は呼び出しを示し、`failedCall`はその1から始まる番号、`rolledBack`は元に戻す処理が実行されたかどうかを示し、`undoStep`はfalse、`results`の最後は失敗した呼び出しです。その後も取り消しイベントが開いている場合は、`warning`が追加されます。

有効なグループのツールだけを使用できます。

**実行前に拒否されるもの:** 高リスクのツール（safetyLevel=highまたはdestructiveHint=true。ユーザーに確認してから、1つずつ呼び出してください）、対話型ツール（独自の取り消しを記録するため）、およびrunToolBatchを含むメタツール。また、ファイルが開いていない間や、Vectorworksの別の操作が進行中の間は、どのバッチも拒否されます。バッチが終了するまで、Vectorworksはビジー状態です。読み取り専用ツールは使用できますが、必要ありません。

> **注:** 「1つのrunPythonScriptを記述する」という助言は、[Scripting](Scripting.md#scripting)グループを利用できる場合にのみ当てはまります。このグループは初期状態では有効ではなく、`runPythonScript`は高リスクのツールであり（最初にユーザーに確認してください）、ツールモード「スクリプトツールを除くすべてを有効化」ではこのグループはまったく提供されません。スクリプトを使用しない場合は、ツールを1つずつ呼び出してください。その場合、図面を変更する各呼び出しが、それぞれ独立した取り消しステップになります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string | はい | 取り消しステップ「MCP: &lt;name&gt;」の名前: 空白だけは不可、制御文字なし。例: 'Create walls and slab'。1～63文字。 |
| `calls` | array of object | はい | ツール呼び出し。指定順に実行されます。1～50項目。 |
| `calls[].tool` | string | はい | 有効なグループのツールの名前。 |
| `calls[].arguments` | object |  | 直接呼び出す場合と同じツールの引数。デフォルトは{}です。 |

**結果**

| 結果 | 戻り値 |
|---|---|
| すべての呼び出しが成功 | `{ "undoStep": true, "undoName": "MCP: <name>", "results": [ { "tool", "result" }, ... ] }` |
| 呼び出しが失敗 | `{ "err": "call <n> (<tool>) failed: <err of the call>", "failedCall": <n>, "rolledBack": <true or false>, "undoStep": false, "results": [ ... ] }`。バッチはその呼び出しで停止し、`results`の最後はその呼び出しになります。 |
| バッチが拒否された | `{ "err": "<reason>", "undoStep": false }`。何も実行されず、結果に`results`、`failedCall`、`rolledBack`は含まれません。 |

- 結果の最上位に`err`がある場合、または例外がスローされた場合、呼び出しは失敗です。スローされた例外は、`exception: <message>`または`unhandled exception`として報告されます。
- `rolledBack`は、バッチの取り消しイベントが元に戻された場合は`true`です。取り消しイベントがもう開いていなかったため、元に戻すものがなかった場合は`false`です。
- バッチの後も取り消しイベントが開いている場合は、成功または失敗した結果に`warning`（"An undo event is still open after the batch: changes made until Vectorworks ends it can join it."）が追加されます。
- 何かを実行する前に、バッチ全体が次の順序で確認されます: `name`、`calls`（実行できない最初の呼び出しが示されます）、Vectorworksの状態。拒否の理由は次のとおりです。

| 拒否されたバッチの`err` | 原因 |
|---|---|
| `'name' must be a string` | `name`がない、または文字列ではありません。 |
| `'name' must not be empty or blank` | `name`が空、またはスペースだけです。 |
| `'name' must not contain control characters` | `name`に制御文字が含まれています。 |
| `'name' must have at most 63 characters` | `name`が63文字を超えています。 |
| `'calls' must be an array of 1 to 50 calls { tool, arguments }` | `calls`がない、配列ではない、空、または50項目を超えています。 |
| `call <n> (<tool>): must be an object with a string 'tool'` | 呼び出しが、文字列の`tool`を持つオブジェクトではありません。 |
| `call <n> (<tool>): 'arguments' must be an object` | `arguments`がオブジェクトではありません。 |
| `call <n> (<tool>): unknown tool` | この名前のツールはありません。 |
| `call <n> (<tool>): the tool is in an inactive group; activate it via activateToolGroups` | ツールのグループが有効ではありません。 |
| `call <n> (<tool>): only provider tools can run in a batch, not the meta-tools (listToolGroups, activateToolGroups, runToolBatch)` | ツールはCoreグループのメタツールです。 |
| `call <n> (<tool>): high-risk tools cannot run in a batch: ask the user, then call the tool on its own` | ツールに`destructiveHint`がある、またはリスクレベルが`high`（ツール自身のレベル、ない場合はグループのレベル）です: `runPythonScript`、`runScript`、`runMenuCommand`。 |
| `call <n> (<tool>): interactive tools record their own undo steps and cannot run in a batch: call the tool on its own` | ツールが独自の取り消しステップを記録します: `activateTool`、`setToolMode`、`setToolModes`、`sendToolPointer`、`sendToolAction`、`setOIPValues`、`pressOIPButton`。 |
| `no document is open` | ファイルが開いていません。 |
| `an undo event is already open: another Vectorworks operation is in progress; try again when it has finished` | 別の取り消しイベントが作成中です。 |

`<n>`は呼び出しの1から始まる番号です。呼び出しにツール名がない場合、`(<tool>)`は省略されます。

**引数の例**（2枚の壁を1つの取り消しステップで作成。Architectureグループが有効である必要があります）

```json
{
  "name": "Create walls",
  "calls": [
    {
      "tool": "createWall",
      "arguments": {"start": {"x": 0, "y": 0}, "end": {"x": 5000, "y": 0}}
    },
    {
      "tool": "createWall",
      "arguments": {"start": {"x": 5000, "y": 0}, "end": {"x": 5000, "y": 4000}}
    }
  ]
}
```


<a id="calling-a-tool"></a>

## ツールの呼び出し

ツールは、MCPの`tools/call`リクエストで呼び出します: ツールの`name`と`arguments`オブジェクトです。不要な引数は省略します。すべてのツールは1つのJSONオブジェクトを返します。

たとえば、図面の四角形を2個ずつ一覧表示します。

```json
{
  "name": "findObjects",
  "arguments": {"criteria": "(T=RECT)", "limit": 2}
}
```

結果は次のとおりです。UUIDはプレースホルダで示しています。

```json
{
  "count": 3,
  "limit": 2,
  "nextOffset": 2,
  "notSearched": ["INSYMBOL", "INOBJECT", "INVIEWPORT", "INOBJPATH", "INOBJPROFILE"],
  "objects": [
    {"type": 3, "typeName": "Rectangle", "uuid": "<uuid 1>"},
    {
      "name": "Plot outline",
      "type": 3,
      "typeName": "Rectangle",
      "uuid": "<uuid 2>"
    }
  ],
  "offset": 0,
  "returned": 2,
  "truncated": true
}
```

`count`は一致したすべての数、`objects`はこのページの[オブジェクト参照](#object-references)、`nextOffset`は次のページの`offset`です（[ページ分割](#paging)を参照）。`notSearched`には、シンボル定義の内部など、検索条件に含まれなかった場所が列挙されます。

<a id="results-and-errors"></a>

## 結果とエラー

- すべてのツールは1つのJSONオブジェクトを返します。オブジェクトのキーは、各ツールで説明しています。
- 失敗した呼び出しは、問題の内容を示すメッセージ`err`を持つオブジェクトを返します。例:

```json
{
  "err": "object not found"
}
```

- サーバーは、オブジェクトをMCPの結果の最初の`content`項目のテキストとして送信します: `result.content[0].text`にJSONテキストが入ります。オブジェクトの最上位に`err`がある場合、結果には`isError: true`も含まれます。
- `arguments`はJSONオブジェクトである必要があります。それ以外は`{}`として扱われ、JSONオブジェクトを含む文字列は解析されます。これは18グループのツールに当てはまります。Coreのツール`listToolGroups`、`activateToolGroups`、`runToolBatch`は、送信されたとおりの`arguments`を受け取ります: 文字列は解析されず、オブジェクトではない値ではそれらのツールのエラーになります（例: `listToolGroups requires an arguments object`）。
- ページ分割ツールと他の一部のツールは、何かを変更する前に引数の型と範囲を確認します。メッセージは引数を示します。例: `'limit' must be a number`、`'countOnly' must be true or false`、`'limit' must be at least 1`、`'offset' must not be negative`。すべてのツールが型を確認するわけではありません: JSONの型が誤っている引数は、多くの場合、指定されなかったものとして読み取られ、デフォルトが適用されます。呼び出しの型を確認してください。
- 図面を編集する呼び出しが失敗すると、サーバーはツールが取り消し用に登録したものを元に戻し、結果に`rolledBack`を追加します: 元に戻せた場合は`true`、戻せなかった場合は`false`です。独自の取り消しステップを記録するツールは、ロールバックされません。[取り消し](#undo)を参照してください。
- 複数の設定を書き込むツールは、書き込んだ内容を設定ごとに`applied`で報告します。[適用した設定](#applied-settings)を参照してください。

次の`err`テキストは、どのツールからも返される可能性があります。

| `err` | 原因 |
|---|---|
| `no active Vectorworks document` | ファイルが開いていません。[Core](#core-group)グループ以外のすべてのツールには、`convertUnits`も含め、開いているファイルが必要です。メタツールの[`listToolGroups`](#listtoolgroups)と[`activateToolGroups`](#activatetoolgroups)には必要ありません。 |
| `exception: &lt;text&gt;`または`unhandled exception` | ツールが例外をスローしました。呼び出しは失敗として扱われます（`rolledBack`を参照）。 |

サーバーがまったく処理できないリクエストには、ツールの結果ではなく、JSON-RPCエラーで応答します。

| コード | 意味 |
|---|---|
| `-32700` | 本文が有効なJSONではありません。 |
| `-32601` | `Method not found: &lt;method&gt;`。 |
| `-32602` | 無効なパラメータ: `tools/call requires a 'name' parameter`、`Tool '&lt;name&gt;' is in an inactive group; activate it via activateToolGroups.`、または`Unknown tool: &lt;name&gt;`。 |
| `-32603` | 内部エラー。`tools/call`の`params`がオブジェクトではない場合や、`name`が文字列ではない場合も含みます。 |

<a id="object-references"></a>

## オブジェクト参照

既存の1つのオブジェクトを扱うツールは、次の3つの引数のいずれかでオブジェクトを受け取ります。

| 引数 | 型 | 意味 |
|---|---|---|
| `uuid` | string | ツールが報告するオブジェクトのUUID。推奨される指定方法です。 |
| `name` | string | オブジェクトの正確なVectorworks名（オブジェクト情報パレットの名前フィールド）。 |
| `index` | integer | オブジェクトの内部インデックス。 |

サーバーは`uuid`、`name`、`index`の順に試し、最初にオブジェクトが見つかったものを使用します。どれでも見つからない場合、呼び出しは`object not found`で失敗します。`object not found (provide 'uuid', 'name' or 'index')`のようにヒントを追加するツールや、`source object not found`、`path object not found`、`profile object not found`のようにオブジェクトの役割を示すツールもあります。`targetUuid`、`pathUuid`、`profileUuid`のように、役割に応じて引数に名前を付けるツールもあり、これらにはUUIDを指定します。2つのツールでは、`name`に別の用途もあります: [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter)では書き込むパラメータ、[`editObject`](ObjectPrimitives.md#editobject)ではオブジェクトの新しい名前でもあります。`name`は`index`より先に試されるため、これらのツールではオブジェクトを`uuid`で指定してください。

オブジェクトを返すツール（検索結果、作成したオブジェクト、グループのメンバー）は、それらを**オブジェクト参照**として報告します。

| キー | 型 | 意味 |
|---|---|---|
| `uuid` | string | オブジェクトのUUID。 |
| `type` | integer | Vectorworksの数値のオブジェクトタイプ。たとえば、直線は2、四角形は3、プラグインオブジェクトは86です。 |
| `typeName` | string | 一般的なタイプの場合のみのタイプ名: Line、Rectangle、Oval、Polygon、Arc、FreehandPolygon、Text、Group、RoundedRectangle、Symbol、SymbolDefinition、Locus、Polyline、Extrude、Mesh、Layer。 |
| `parametricName` | string | プラグインオブジェクトのみ: プラグインのユニバーサル名（例: `Door`）。 |
| `localizedParametricName` | string | プラグインオブジェクトのみ: プラグインがインストールされている場合の、Vectorworksの言語でのプラグイン名。 |
| `name` | string | オブジェクトに名前がある場合のオブジェクト名。 |

次の呼び出しでは、参照の`uuid`を使用してください。

<a id="points-rectangles-and-colors"></a>

## 点、矩形、色

<a id="points"></a>

### 点

2D点は、ワールド単位のオブジェクト`{ "x": 0, "y": 0 }`です。配列形式`[x, y]`も受け付けられますが、入力スキーマではオブジェクト形式だけが宣言されているため、オブジェクト形式を優先してください。3D点には`z`が加わります: `{ "x": 0, "y": 0, "z": 0 }`。

3D Modelingのツールは、受け取るまたは返すすべての3D点、中心、フレーム、`baseElevation`に、絶対的なワールドZを使用します。デザインレイヤの高さは加算されないため、`z` 0はワールドZ 0であり、高さが設定されたレイヤの平面ではありません。高さEのレイヤ上にオブジェクトを配置するには、そのZ値にEを加えてください。これらのツールは、Eを`layerElevation`として報告します。`bounds3D`のZ値も、絶対的なワールド高さです。

<a id="rectangles"></a>

### 矩形

矩形は、ワールド単位の`{ "left": 0, "top": 1000, "right": 2000, "bottom": 0 }`で、`top`は`bottom`より上です。ツールが報告する境界には、`width`、`height`、`center`（点）が加わります。

```json
{
  "left": 0,
  "top": 1000,
  "right": 2000,
  "bottom": 0,
  "width": 2000,
  "height": 1000,
  "center": {"x": 1000, "y": 500}
}
```

<a id="colors"></a>

### 色

色は`{ "r": 255, "g": 128, "b": 0 }`で、各チャンネルは0～255です。配列形式`[r, g, b]`も受け付けられますが、入力スキーマではオブジェクト形式だけが宣言されているため、オブジェクト形式を優先してください。0～255の範囲外の値は、範囲内に制限されます。ファイルのカラーテーブルも使用できる属性には、`foreColor`に対する`foreColorIndex`のように、RGB値とは別のインデックスキーがあります。両方を指定し、両方が現在の値と異なる場合は、インデックスが優先されます。例外は`setObjectAttributes`です。そこでは、指定した`foreColorIndex`または`backColorIndex`はRGB値の後に適用され、現在のインデックスと等しい場合でも常に優先されます。

<a id="units-and-angles"></a>

## 単位と角度

ツールに特記がない限り、次のとおりです。

| 値 | 単位 |
|---|---|
| 座標、長さ、距離、オフセット | ワールド単位: 図面の単位。`getUnits`で読み取り、`convertUnits`で変換します。 |
| 角度、回転 | ラジアン。反時計回りが正です。 |
| テキスト | UTF-8文字列。 |
| 色 | RGB。各チャンネルは0～255（[色](#colors)を参照）。 |

例外は、ツールの説明に記載しています。主なものは次のとおりです。

| 値 | 単位 |
|---|---|
| 寸法のフォントサイズ（`fontSize`）、ワークシートの文字書式のフォントサイズ（`size`）、および文字列オブジェクトの`sizePoints` | ポイント。文字列オブジェクトと文字の設定の`size`は、ワールド単位です。 |
| マーカーの角度 | 整数の度（[マーカー](Attributes.md#line-end-markers)を参照）。 |
| マーカーの長さと幅 | 用紙上のインチ。 |
| ドロップシャドウの角度 | 度（[ドロップシャドウ](Attributes.md#drop-shadow)を参照）。 |
| ドロップシャドウのオフセットとぼかしの半径 | `units`の指定に応じて、用紙上のインチまたはワールド単位。 |
| 屋根の勾配 | 度。 |
| 型付きの値として読み取るプラグインパラメータ | 長さはワールド単位、角度は度（[プラグインパラメータ](#plug-in-parameters)を参照）。 |
| オブジェクト情報パレットの値 | ユーザーが入力するように、パレットに表示される単位で入力します。 |

<a id="creation-options"></a>

## 作成オプション

オブジェクトを作成するほとんどのツールは、4つの省略可能な作成オプションを受け付けます。オプションは作成後の新しいオブジェクトに適用され、ツールはその後、そのオブジェクトの[オブジェクト参照](#object-references)を返します。型が誤っている値（文字列ではない`class`や`name`など）は、エラーなしで無視されます。`class`を指定しない場合、ツールはクラスを設定しません。例外は[`combineShapes`](ObjectPrimitives.md#combineshapes)です。その結果は最初の図形のクラスになり、`useClassAttributes`を指定すると、`class`の有無にかかわらず、結果の属性がそのクラスに従います。

| オプション | 型 | 意味 |
|---|---|---|
| `class` | string | 新しいオブジェクトのクラス。まだ存在しないクラスは作成されます。 |
| `useClassAttributes` | boolean | `class`と併用: オブジェクトのグラフィック属性も「クラス属性を使用」に設定します。 |
| `name` | string | 新しいオブジェクトの名前。 |
| `select` | boolean | 新しいオブジェクトを選択します。 |

これらのオプションを持つツール（45個）: [`createLine`](ObjectPrimitives.md#createline), [`createRectangle`](ObjectPrimitives.md#createrectangle), [`createCircle`](ObjectPrimitives.md#createcircle), [`createArc`](ObjectPrimitives.md#createarc), [`createPolygon`](ObjectPrimitives.md#createpolygon), [`createPolyline`](ObjectPrimitives.md#createpolyline), [`createLocus`](ObjectPrimitives.md#createlocus), [`combineShapes`](ObjectPrimitives.md#combineshapes), [`createText`](ObjectPrimitives.md#createtext), [`createPluginObject`](ObjectPrimitives.md#createpluginobject), [`createExtrude`](Objects3D.md#createextrude), [`createSolidPrimitive`](Objects3D.md#createsolidprimitive), [`createSweep`](Objects3D.md#createsweep), [`combineSolids`](Objects3D.md#combinesolids), [`createShell`](Objects3D.md#createshell), [`convertSolid`](Objects3D.md#convertsolid), [`create3DPolygon`](Objects3D.md#create3dpolygon), [`createMesh`](Objects3D.md#createmesh), [`createNurbsCurve`](Objects3D.md#createnurbscurve), [`createNurbsSurface`](Objects3D.md#createnurbssurface), [`createSurfaceModel`](Objects3D.md#createsurfacemodel), [`convertTo3D`](Objects3D.md#convertto3d), [`createDataTag`](ObjectsAnnotation.md#createdatatag), [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock), [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension), [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension), [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension), [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension), [`createCenterMark`](ObjectsAnnotation.md#createcentermark), [`createWall`](ObjectsArchitect.md#createwall), [`createSlab`](ObjectsArchitect.md#createslab), [`createRoof`](ObjectsArchitect.md#createroof), [`createDoor`](ObjectsArchitect.md#createdoor), [`createWindow`](ObjectsArchitect.md#createwindow), [`createColumn`](ObjectsArchitect.md#createcolumn), [`createStair`](ObjectsArchitect.md#createstair), [`createPlant`](ObjectsLandmark.md#createplant), [`createHardscape`](ObjectsLandmark.md#createhardscape), [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea), [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier), [`createPropertyLine`](ObjectsLandmark.md#createpropertyline), [`createSiteModel`](ObjectsLandmark.md#createsitemodel), [`createStake`](ObjectsLandmark.md#createstake), [`createExistingTree`](ObjectsLandmark.md#createexistingtree), [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice).

次の作成ツールは、作成オプションを受け付けません: `createLayer`、`createClass`、`createStory`、`createResource`、`createConnectCADDevice`、`createConnectCADDevices`、`createConnectCADDeviceType`。`edit3DGeometry`が作成するオブジェクト（平面ソリッド、修復したメッシュ、延長したコピーやオフセットしたコピー）も、作成オプションを受け付けません。

<a id="applied-settings"></a>

## 適用した設定

1回の呼び出しで複数の設定を書き込むツールは、各設定の結果を`applied`で報告します: 指定した設定ごとに1つのエントリを持つオブジェクトで、書き込んだ場合は`true`、書き込まなかった場合は`false`です（値が適合しない、オブジェクトがその設定に対応していないなど）。そのため、個々の設定が拒否されても、呼び出し自体は成功することがあります。重要な場合は`applied`を確認してください。

たとえば、[`editLayer`](DocumentAccess.md#editlayer)に次の引数を指定すると、

```json
{
  "name": "Design Layer-1",
  "elevation": 3000,
  "scale": 50
}
```

更新したレイヤが、次の内容とともに返されます。

```json
{
  "applied": {"elevation": true, "scale": true}
}
```

`applied`を報告するツール（43個）: [`editLayer`](DocumentAccess.md#editlayer), [`editStory`](DocumentAccess.md#editstory), [`editClass`](DocumentAccess.md#editclass), [`setUnits`](DocumentAccess.md#setunits), [`setPreferences`](DocumentAccess.md#setpreferences), [`setGeometry`](ObjectPrimitives.md#setgeometry), [`editVertices`](ObjectPrimitives.md#editvertices), [`createText`](ObjectPrimitives.md#createtext), [`editText`](ObjectPrimitives.md#edittext), [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes), [`copyAttributes`](ObjectPrimitives.md#copyattributes), [`editObject`](ObjectPrimitives.md#editobject), [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter), [`createPluginObject`](ObjectPrimitives.md#createpluginobject), [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject), [`setProjectData`](ObjectsAnnotation.md#setprojectdata), [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension), [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension), [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension), [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension), [`setDimension`](ObjectsAnnotation.md#setdimension), [`createWall`](ObjectsArchitect.md#createwall), [`createSlab`](ObjectsArchitect.md#createslab), [`createDoor`](ObjectsArchitect.md#createdoor), [`createWindow`](ObjectsArchitect.md#createwindow), [`createStair`](ObjectsArchitect.md#createstair), [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject), [`setConnectCADSocket`](ObjectsConnectCAD.md#setconnectcadsocket), [`createPlant`](ObjectsLandmark.md#createplant), [`createHardscape`](ObjectsLandmark.md#createhardscape), [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea), [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier), [`createPropertyLine`](ObjectsLandmark.md#createpropertyline), [`createSiteModel`](ObjectsLandmark.md#createsitemodel), [`createStake`](ObjectsLandmark.md#createstake), [`createExistingTree`](ObjectsLandmark.md#createexistingtree), [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject), [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice), [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice), [`editResource`](Resources.md#editresource), [`setResourceDetails`](Resources.md#setresourcedetails), [`applyResource`](Resources.md#applyresource), [`editWorksheet`](Resources.md#editworksheet).

次のツールでは、`applied`の形式が異なります。

- 作成ツールは、そのツールが報告する設定のうち少なくとも1つを呼び出しで指定した場合にのみ、`applied`を報告します。これは、[`createText`](ObjectPrimitives.md#createtext)、[`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice)、4つの`create…Dimension`ツール、およびArchitectureグループとLandmarkグループの作成ツールに当てはまります。[`createPluginObject`](ObjectPrimitives.md#createpluginobject)は、`params`を指定した場合にのみ報告します。一覧にない作成ツール（`createColumn`、`createRoof`、`createDataTag`、`createTitleBlock`、`createCenterMark`）は`applied`を報告しません。
- [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter)は、`params`を指定した場合にのみ`applied`を報告し、`name`と`value`を指定した場合は`ok`を返します。[`editStory`](DocumentAccess.md#editstory)は、`name`で指定したストーリを編集する場合にのみ（`story`とともに）報告します: `levelTypes`または`defaultStoryLevels`だけを変更する呼び出しと、`delete`を指定した呼び出しでは報告されません。[`editResource`](Resources.md#editresource)は、`action`が`modify`の場合にのみ報告します。
- キーは必ずしも引数の名前ではありません。入れ子の引数は平坦化されます: [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes)と[`editClass`](DocumentAccess.md#editclass)は、`pen.foreColor`を`penForeColor`として報告します。[`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes)の結果の説明には、すべてのキーが記載されています。そこで`true`の場合にのみ作用するフラグは、`false`の場合はエントリがありません。
- [`copyAttributes`](ObjectPrimitives.md#copyattributes)は、`results`の各エントリ内で`applied`を報告します。カテゴリ`variable`の場合、[`setPreferences`](DocumentAccess.md#setpreferences)は`applied`を`selector`の隣に1つの真偽値として報告します。[`applyResource`](Resources.md#applyresource)は、単一の値`true`を報告します（失敗は`err`になります）。[`editWorksheet`](Resources.md#editworksheet)は、アクションごとに1つのエントリを持つリストを報告します。

<a id="plug-in-parameters"></a>

## プラグインパラメータ

プラグインオブジェクト（ドア、窓、植栽、Lighting Device、データタグなど多数）は、ユニバーサル名（ローカライズされていない名前）で名前が付いたパラメータに設定を保持します。オブジェクトがどのプラグインかは[`getObjectInfo`](ObjectPrimitives.md#getobjectinfo)（`parametricName`）で、プラグインが持つパラメータは[`getPluginDefinition`](ObjectPrimitives.md#getplugindefinition)で確認できます。

<a id="reading-parameters"></a>

### パラメータの読み取り

- [`getObjectParameters`](ObjectPrimitives.md#getobjectparameters)は、すべてのパラメータ、または`names`で指定したパラメータを表示文字列として返します。`includeDefinitions`を指定すると、各パラメータの型、ローカライズされた名前、ポップアップの選択肢も返します。
- [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject)、[`getLandmarkObject`](ObjectsLandmark.md#getlandmarkobject)、[`getLightingDevice`](ObjectsSpotlight.md#getlightingdevice)の`params`引数は、パラメータ名の配列を受け取り、その正確な型付きの値を返します。

| パラメータの型 | JSON値 |
|---|---|
| 実数、寸法、座標、角度、面積、体積 | number: 長さはワールド単位、角度は度 |
| 整数、寸法規格のポップアップ | integer |
| 真偽値 | `true`または`false` |
| その他の型（テキスト、ポップアップなど） | string |

<a id="writing-parameters"></a>

### パラメータの書き込み

- [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter)は、1つのパラメータ（`name`と`value`。型はパラメータの定義、または`type`から決まります: `real`/`number`、`int`/`integer`、`bool`/`boolean`、それ以外はテキスト）、または`params`で複数のパラメータを一度に書き込みます。
- `params`オブジェクト`{ "ParamName": value }`は、次のツールでユニバーサル名によってパラメータを書き込みます: [`createPluginObject`](ObjectPrimitives.md#createpluginobject), [`createDataTag`](ObjectsAnnotation.md#createdatatag), [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock), [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject), [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension), [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension), [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension), [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension), [`setDimension`](ObjectsAnnotation.md#setdimension), [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject), [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject), [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice), [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice).
- [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter)と[`createPluginObject`](ObjectPrimitives.md#createpluginobject)は、同じ方法で値を書き込みます: 実数のパラメータは数値、または`"5"`のような数値の文字列を受け付け、整数のパラメータは整数、または整数の数値文字列を受け付け（`2.5`は適合しません）、真偽値のパラメータは`true`または`false`だけを受け付け、その他のパラメータはテキストを受け付けます。そのようなパラメータに数値や真偽値を指定すると、そのテキストとして書き込まれます（`5`は`"5"`になります）。その後、オブジェクトは再生成されます。パラメータの型に適合しない値や、不明なパラメータ名の扱いは、2つのツールで異なります。`setObjectParameter`はその値を書き込まず、`false`を報告します（`applied`内、または`ok`として）。呼び出し自体は成功し、他の値は書き込まれます。`createPluginObject`は、何かを作成する前にすべての名前と値を確認し、適合しないものが1つでもあれば呼び出し全体を拒否します（`these 'params' values do not fit the type of their parameter: …`）。そのため、何も作成されず、`applied`も報告されません。作成後の新しいオブジェクトが受け付けないパラメータ（プラグインスタイルが設定するパラメータなど）だけは、後から呼び出しを失敗させます: その`err`はパラメータを示し、結果には引き続き、それらに`false`を設定した`applied`が含まれ、呼び出しはロールバックされます（`rolledBack`）。
- [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject)は、実数をワールド単位で受け付けます。これは[`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject)が`params`で読み取る形式と同じであるため、読み取った値をそのまま書き戻せます。

<a id="paging"></a>

## ページ分割

長いリストを返す可能性があるツールは、ページごとに返します。それらのツールは、同じページ分割の引数を受け取ります。

| 引数 | 型 | 意味 |
|---|---|---|
| `limit` | integer | このページの最大項目数。1以上です。デフォルトはツールによって異なります（下記を参照）。 |
| `offset` | integer | スキップする項目数。負の値は指定できません。デフォルトは0です。 |
| `countOnly` | boolean | 項目を含めず、件数とページ分割のキーだけを返します。デフォルトはfalseです。 |

また、項目の隣に、同じページ分割のキーを報告します。

| キー | 意味 |
|---|---|
| `count` | 項目（または一致した項目）の総数。 |
| `returned` | このページの項目数。 |
| `offset` | このページのオフセット。 |
| `limit` | 使用した上限。 |
| `truncated` | 続きの項目がある場合は`true`。 |
| `nextOffset` | 次のページの`offset`。`truncated`がtrueの場合にのみ含まれます。 |

リスト全体を読み取るには、`truncated`がfalseになるまで、`offset`を`nextOffset`に設定してツールを再度呼び出します。件数を数える場合や、存在するかどうかを確認する場合は、`countOnly`を使用してください。

誤ったページ分割の引数は、何かを読み取る前に拒否されます。ページ分割のエラーは次のとおりです: `'limit' must be a number`、`'offset' must be a number`、`'countOnly' must be true or false`、`'limit' must be at least 1`、`'offset' must not be negative`。

**ページ分割されるツール**

| ツール | 項目のキー | デフォルトの上限 |
|---|---|---|
| [`listIFCMappingObjects`](IFC.md#listifcmappingobjects) | `objects` | 200 |
| [`findMenuCommands`](MenuAccess.md#findmenucommands) | `commands` | 50 |
| [`getMenus`](MenuAccess.md#getmenus) | `menus`、`entries`、または`items` | 100 |
| [`findObjects`](ObjectPrimitives.md#findobjects) | `objects` | 200 |
| [`getObjectsAtPoint`](ObjectPrimitives.md#getobjectsatpoint) | `objects` | 50 |
| [`get3DGeometry`](Objects3D.md#get3dgeometry) | 各リストの`items` | 100 |
| [`listConnectCADSignals`](ObjectsConnectCAD.md#listconnectcadsignals) | `signals` | 500 |
| [`listConnectCADConnectors`](ObjectsConnectCAD.md#listconnectcadconnectors) | `connectors` | 500 |
| [`listGDTFs`](ObjectsSpotlight.md#listgdtfs) | `gdtfs` | 200 |
| [`getOIPControls`](OIPAccess.md#getoipcontrols) | `controls` | 100 |
| [`getResources`](Resources.md#getresources) | `resources` | 200 |
| [`getWorksheet`](Resources.md#getworksheet) | `cells`または`subrows` | 200セル、100サブ行 |
| [`listScripts`](Scripting.md#listscripts) | `scripts` | 200 |
| [`getTools`](ToolAccess.md#gettools) | `tools` | 100 |

**結果内のページ分割されるリスト**

一部の結果には、専用の引数でページ分割されるリストが含まれます。そのようなリストはそれぞれ、ページ分割のキーと項目を持つオブジェクトです。

| ツール | リスト | 引数 | 項目のキー | デフォルトの上限 |
|---|---|---|---|---|
| [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo) | `members` | `memberLimit`, `memberOffset` | `objects` | 50 |
| [`getText`](ObjectPrimitives.md#gettext) | `lines` | `lineLimit`, `lineOffset` | `items` | 100 |
| [`getText`](ObjectPrimitives.md#gettext) | `styleRuns` | `runLimit`, `runOffset` | `items` | 100 |

<a id="effects-and-risk-levels"></a>

## 作用とリスクレベル

各ツールには、何を変更し得るかを示す**作用**と、クライアントがどの程度注意して扱うべきかを示す**リスクレベル**があります。どちらも各ツールに表示しています。ツール一覧は、標準のツール注釈`readOnlyHint`と`destructiveHint`によって、作用をMCPクライアントに報告します。リスクレベルが高いほど、1回の呼び出しで変更し得る内容が多く、元に戻すのが難しくなります。サーバーはこの値を`safetyLevel`フィールドで報告します。

| 作用 | 意味 | リスクレベル | 注釈 | 取り消し | runToolBatch内 | ツール数 |
|---|---|---|---|---|---|---|
| 読み取り専用 | 図面またはアプリケーションの状態を読み取り、何も変更しません。 | 低 | `readOnlyHint`: true | なし | 許可 | 58 |
| 編集 | 図面を変更します。取り消しで変更を元に戻せます。 | 低または中 | `readOnlyHint`: false | 1ステップ「MCP: &lt;tool&gt;」 | はい | 86 |
| 対話操作 | ユーザーと同じように、ユーザーインターフェイス（ツールパレットまたはオブジェクト情報パレット）を操作します。 | 中 | `readOnlyHint`: false | ユーザー入力と同様にVectorworksが記録 | 不可 | 7 |
| 対話操作（破壊的） | ユーザーが選択した場合と同じように、メニューコマンドを実行します。 | 高 | `readOnlyHint`: false, `destructiveHint`: true | メニューコマンドが記録 | 不可 | 1 |
| スクリプト実行 | Pythonスクリプトを実行します。スクリプトで可能なあらゆる操作を行えます。 | 高 | `readOnlyHint`: false, `destructiveHint`: true | 1ステップ「MCP: script」（スクリプトが変更を登録しなかった場合はなし） | 不可 | 2 |

[Coreグループ](#core-group)の3つのメタツールは、この表には含まれていません。[`listToolGroups`](#listtoolgroups)は読み取り専用です。[`activateToolGroups`](#activatetoolgroups)は**セッション設定**で、サーバーが提供するツールグループを変更しますが、図面は変更しません（注釈`readOnlyHint`: true、`destructiveHint`: false）。[`runToolBatch`](#runtoolbatch)は**編集（バッチ）**で、他のツールを1つの取り消しステップで実行します（注釈`readOnlyHint`: false、`destructiveHint`: false。リスクレベルは中）。

**リスクレベル**

- **低**: 読み取り、セッションの変更（有効なツールグループなど）、およびファイルの設定、2Dプリミティブ、文字列の通常の編集（[Document](DocumentAccess.md#document)、[IFC](IFC.md#ifc)、[IFC Data Mapping](IFC.md#ifc-data-mapping)、[Draw2D](ObjectPrimitives.md#draw2d)）。「編集 > 取り消し」で編集を元に戻せます。
- **中**: オブジェクト、3Dジオメトリ、注釈、業種別オブジェクト、リソース、ワークシートの編集、およびツールパレットとオブジェクト情報パレットを操作する対話型ツール。「編集 > 取り消し」で元に戻せます。
- **高**: メニューコマンドとスクリプト。予測が難しい広範囲の変更を行う可能性があります。クライアントは、呼び出しのたびにユーザーに確認する必要があります。これらのツールは、[`runToolBatch`](#runtoolbatch)内では実行できません。

各グループにはリスクレベルがあり、そのページに表示されています。ツールは独自のレベルを報告します: 読み取り専用ツールは常に低、対話型ツールは中、メニューコマンドとスクリプトは高で、その他の編集ツールは、ツールが独自のレベルを設定していない限り、グループのレベルになります。そのため、[InteractiveTools](ToolAccess.md#interactivetools)グループに表示されるレベル（高）は、そのどのツールのレベルでもありません: その読み取り専用ツールは低、対話型ツールは中です。

**特別な作用を持つツール**

- 対話操作: [`setOIPValues`](OIPAccess.md#setoipvalues), [`pressOIPButton`](OIPAccess.md#pressoipbutton), [`activateTool`](ToolAccess.md#activatetool), [`setToolMode`](ToolAccess.md#settoolmode), [`setToolModes`](ToolAccess.md#settoolmodes), [`sendToolPointer`](ToolAccess.md#sendtoolpointer), [`sendToolAction`](ToolAccess.md#sendtoolaction).
- 対話操作（破壊的）: [`runMenuCommand`](MenuAccess.md#runmenucommand).
- スクリプト実行: [`runPythonScript`](Scripting.md#runpythonscript), [`runScript`](Scripting.md#runscript).

<a id="undo"></a>

## 取り消し

- **編集ツール**: 成功した各呼び出しは、`MCP: <tool>`という名前の1つの取り消しステップになります（例: `MCP: createWall`）。「編集 > 取り消し」で元に戻せ、Vectorworksはステータスメッセージにその名前を表示します。
- **失敗した呼び出し**: 編集の呼び出しが失敗すると、取り消し用に登録された変更が元に戻され、結果は`rolledBack`を報告します（元に戻せた場合は`true`、戻せなかった場合は`false`）。ツールが登録しなかった変更は元に戻せません。独自の取り消しステップを記録するツール（対話型ツールと`runMenuCommand`）は、ロールバックされません。
- **読み取り専用ツール**は、取り消しステップを追加しません。
- **バッチ**: [`runToolBatch`](#runtoolbatch)は、複数の呼び出しを`MCP: <name>`という1つの取り消しステップとして、全成功または全取り消しで実行します。バッチ内の各呼び出しはそのステップに含まれます。1つが失敗するとバッチは停止し、それまでに行ったことはすべて元に戻されます。
- **対話型ツール**（[`runMenuCommand`](MenuAccess.md#runmenucommand)、[`setOIPValues`](OIPAccess.md#setoipvalues)、[`pressOIPButton`](OIPAccess.md#pressoipbutton)、[`activateTool`](ToolAccess.md#activatetool)、[`setToolMode`](ToolAccess.md#settoolmode)、[`setToolModes`](ToolAccess.md#settoolmodes)、[`sendToolPointer`](ToolAccess.md#sendtoolpointer)、[`sendToolAction`](ToolAccess.md#sendtoolaction)）は、ユーザー自身の操作と同じ方法でVectorworksに記録されるため、「編集 > 取り消し」でユーザーの操作と同様に元に戻せます。
- **スクリプト**（[`runPythonScript`](Scripting.md#runpythonscript)、[`runScript`](Scripting.md#runscript)）は、`MCP: script`という1つの取り消しステップで実行されます。成功した実行や、ユーザー入力を待つ実行の後はステップが保持され、失敗した実行の後は元に戻されます（`rolledBack`）。Vectorworksは空のステップを残さないため、変更を登録しなかった実行ではステップは残りません（`undoStep`はfalse）。スクリプト自身が、作成したものと変更するものを登録する必要があります。登録しないと、取り消しで元に戻せません。
