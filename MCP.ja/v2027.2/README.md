[English](../../MCP/v2027.2/README.md) • [Deutsch](../../MCP.de/v2027.2/README.md) • **日本語**

# Vectorworks MCPサーバー — Vectorworks 2027 Update 2 ツールリファレンス

このリファレンスでは、Vectorworks MCPサーバーのツールについて、各ツールの動作、受け取る引数、返す内容を説明します。154個のツールは18のツールグループに整理されており、これに加えて、Coreグループの常に利用できる3つのメタツールがあります。分野ごとに1ページがあり、各ページの冒頭に目次があり、すべてのグループとツールが同じ構成で説明されています。

MCPの概要とサーバーの動作については、[Vectorworks MCPサーバー](../README.md)を参照してください。

<a id="table-of-contents"></a>

## 目次

- [はじめに](#getting-started)
- [共通の規則](#conventions)
- [ツール構成](#tool-tree)
- [カテゴリ別の目次](#contents-by-category)
  - [共通の規則と形式](#shared-conventions-and-formats)
  - [ファイルと選択](#document-and-selection)
  - [オブジェクトとジオメトリ](#objects-and-geometry)
  - [注釈](#annotation)
  - [業種別オブジェクト](#industry-objects)
  - [リソースとデータ](#resources-and-data)
  - [自動化とユーザーインターフェイス](#automation-and-user-interface)
- [A–Z索引](#index-az)
- [ページの構成](#page-layout)
- [統計](#statistics)

<a id="getting-started"></a>

## はじめに

1. Vectorworksで**ツール > MCPサーバー > MCPサーバーを起動...**を選択し（Viewerを除く標準の作業画面の場合）、ツールモードとポート（デフォルト8765）を選んで、**サーバーを起動**をクリックします。ダイアログにはサーバーURL（例: `http://localhost:8765`）が表示され、**URLをコピー**でコピーできます。ポートが使用中の場合、サーバーは最大9個の別のポートを試し、実際に使用しているポートがダイアログに表示されます。MCPクライアントにURLをHTTP MCPサーバーとして追加し、Vectorworksでファイルを開きます。ファイルが開いていない場合、ツールは`no active Vectorworks document`を返します。ダイアログとサーバーについては、[起動と接続](../README.md#start-and-connect)を参照してください。
2. ツール一覧（`tools/list`）には、有効なグループのツールだけが表示されます: [Core](Common.md#core-group)のメタツールと、初期状態で有効なグループである[Document](DocumentAccess.md#document)、[Selection](DocumentAccess.md#selection)、[IFC](IFC.md#ifc)、[Objects](ObjectPrimitives.md#objects)です。選んだツールモードによって、サーバーが提供するグループが決まります: **すべてのツールを有効化**（デフォルト）ではすべてのグループ、**スクリプトツールを除くすべてを有効化**では[Scripting](Scripting.md#scripting)以外のすべてのグループ、**スクリプトツールのみを有効化**ではCoreのメタツールとScriptingグループだけが提供され、Scriptingグループはすぐに有効になります。[ツールグループと有効化](Common.md#tool-groups-and-activation)を参照してください。
3. [`listToolGroups`](Common.md#listtoolgroups)ですべてのグループを確認し、[`activateToolGroups`](Common.md#activatetoolgroups)で[Architecture](ObjectsArchitect.md#architecture)など必要なグループを有効にします。その後、ツール一覧を更新します。
4. ツールを呼び出します。図面を変更する成功した各呼び出しは1つの取り消しステップ（`MCP: <tool>`、スクリプトは`MCP: script`）になり、1回の「編集 > 取り消し」で元に戻せます。対話型ツールとメニューコマンドは、ユーザー入力と同様に独自の取り消しステップを記録します。複数の編集の呼び出しを1つの取り消しステップにするには、[`runToolBatch`](Common.md#runtoolbatch)を使用します。runToolBatchは、独自の取り消しステップを記録するツール（`activateTool`、`setToolMode`、`setToolModes`、`sendToolPointer`、`sendToolAction`、`setOIPValues`、`pressOIPButton`、`runMenuCommand`）、スクリプトを実行する`runPythonScript`と`runScript`、メタツール、および無効なグループのツールを拒否します。[取り消し](Common.md#undo)を参照してください。

たとえば、Architectureグループを有効にして壁を作成します。

```json
{
  "name": "activateToolGroups",
  "arguments": {"groups": ["architecture"]}
}
```

```json
{
  "name": "createWall",
  "arguments": {
    "start": {"x": 0, "y": 0},
    "end": {"x": 5000, "y": 0},
    "thickness": 200
  }
}
```

`createWall`は新しい壁の[オブジェクト参照](Common.md#object-references)を返し、後続の呼び出しではその`uuid`を使用します。長さは図面の単位です（この例ではミリメートル）。

<a id="conventions"></a>

## 共通の規則

[Common](Common.md)ページは、すべてのツールが従う規則を説明し、[Attributes](Attributes.md)はマーカーとドロップシャドウの形式を説明します。

| 項目 | 規則 |
|---|---|
| [ツールグループと有効化](Common.md#tool-groups-and-activation) | 有効なグループのツールだけが一覧に表示されます。`activateToolGroups`は、サーバーが停止されるまで、すべてのクライアントに対してグループを有効にします。 |
| [結果とエラー](Common.md#results-and-errors) | すべてのツールは1つのJSONオブジェクトを返します。失敗した場合は`{ "err": "..." }`を返します。 |
| [オブジェクト参照](Common.md#object-references) | オブジェクトは`uuid`（推奨）、`name`、`index`で渡され、`uuid`、`type`、`typeName`、`name`とともに返されます。 |
| [点、矩形、色](Common.md#points-rectangles-and-colors) | `{ x, y }`、`{ left, top, right, bottom }`、および各チャンネル0～255の`{ r, g, b }`。 |
| [単位と角度](Common.md#units-and-angles) | ツールに特記がない限り、長さはワールド単位（図面の単位）、角度はラジアンです。 |
| [作成オプション](Common.md#creation-options) | ほとんどの作成ツールは、`class`、`useClassAttributes`、`name`、`select`を受け付けます。 |
| [適用した設定](Common.md#applied-settings) | 複数の設定を書き込むツールは、それぞれの結果を`applied`で報告します。 |
| [プラグインパラメータ](Common.md#plug-in-parameters) | プラグインオブジェクトのパラメータは、`params`を使ってユニバーサル名で読み書きします。 |
| [ページ分割](Common.md#paging) | 長いリストは`limit`、`offset`、`countOnly`を受け取り、`count`、`truncated`、`nextOffset`を報告します。 |
| [作用と安全性レベル](Common.md#effects-and-safety-levels) | 各ツールは、読み取り専用、編集、対話操作、スクリプト実行のいずれかで、安全性レベルは低、中、高のいずれかです。 |
| [取り消し](Common.md#undo) | 各編集の呼び出しは、`MCP: <tool>`という1つの取り消しステップ（スクリプトは`MCP: script`）になります。失敗した編集の呼び出しは元に戻され、`rolledBack`を報告します。対話型ツールは、独自の取り消しステップを記録します。 |
| [マーカーとドロップシャドウ](Attributes.md) | 部分指定のオブジェクトです: 指定したメンバーだけが変更されます。 |

<a id="tool-tree"></a>

## ツール構成

このリファレンスのページと、それぞれが説明するツールグループを、ツールフォルダの順に示します。*有効*と記載したグループは、初期状態で有効です。

```text
Vectorworks MCPサーバー
├── Attributes                    → Attributes.md       マーカー、ドロップシャドウ
├── Common                        → Common.md           共通の規則
│   └── Core                      (3ツール、常に有効)
├── DocumentAccess                → DocumentAccess.md
│   ├── Document                  (17ツール、有効)
│   └── Selection                 (3ツール、有効)
├── IFC                           → IFC.md
│   ├── IFC                       (4ツール、有効)
│   └── IFC Data Mapping          (2ツール)
├── MenuAccess                    → MenuAccess.md
│   └── Menus                     (4ツール)
├── ObjectPrimitives              → ObjectPrimitives.md
│   ├── Draw2D                    (15ツール)
│   └── Objects                   (12ツール、有効)
├── Objects3D                     → Objects3D.md
│   └── 3D Modeling               (16ツール)
├── ObjectsAnnotation             → ObjectsAnnotation.md
│   ├── Annotation                (8ツール)
│   └── Dimensioning              (8ツール)
├── ObjectsArchitect              → ObjectsArchitect.md
│   └── Architecture              (9ツール)
├── ObjectsConnectCAD             → ObjectsConnectCAD.md
│   └── ConnectCAD                (10ツール)
├── ObjectsLandmark               → ObjectsLandmark.md
│   └── Landmark                  (10ツール)
├── ObjectsSpotlight              → ObjectsSpotlight.md
│   └── Spotlight                 (5ツール)
├── OIPAccess                     → OIPAccess.md
│   └── Object Info               (3ツール)
├── Resources                     → Resources.md
│   └── Resources                 (11ツール)
├── Scripting                     → Scripting.md
│   └── Scripting                 (7ツール)
└── ToolAccess                    → ToolAccess.md
    └── InteractiveTools          (10ツール)
```

<a id="contents-by-category"></a>

## カテゴリ別の目次

すべてのページ、グループ、ツールを分野別に掲載しています。各ツールはその説明にリンクしています。

<a id="shared-conventions-and-formats"></a>

### 共通の規則と形式

すべてのツールの呼び出し方法と、共通の値の形式を説明します。

- **[Common](Common.md)** — Vectorworks MCPサーバーのすべてのツールが従う規則です: 呼び出しと結果、オブジェクト参照、点と色、単位、作成オプション、適用した設定、プラグインパラメータ、ページ分割、作用、安全性レベル、取り消し。
  - **[Core](Common.md#core-group)** (`core`, 3ツール, 常に有効) — ツールグループを検出して有効にし、複数のツール呼び出しを1つの取り消しステップとして実行します。
    - [`listToolGroups`](Common.md#listtoolgroups) — 有効、無効を問わずすべてのツールグループを、有効状態と、必要に応じてそのツールとともに一覧表示します。
    - [`activateToolGroups`](Common.md#activatetoolgroups) — サーバーが停止されるまで、ツールグループを有効にして、そのツールをツール一覧に表示します。
    - [`runToolBatch`](Common.md#runtoolbatch) — 複数のツール呼び出しを、全成功または全取り消しの1つの取り消しステップとして実行します。
  - 共通の規則: [ツールの呼び出し](Common.md#calling-a-tool) · [結果とエラー](Common.md#results-and-errors) · [オブジェクト参照](Common.md#object-references) · [点、矩形、色](Common.md#points-rectangles-and-colors) · [単位と角度](Common.md#units-and-angles) · [作成オプション](Common.md#creation-options) · [適用した設定](Common.md#applied-settings) · [プラグインパラメータ](Common.md#plug-in-parameters) · [ページ分割](Common.md#paging) · [作用と安全性レベル](Common.md#effects-and-safety-levels) · [取り消し](Common.md#undo)
- **[Attributes](Attributes.md)** — マーカーとドロップシャドウの値の形式です。クラスとオブジェクトのグラフィック属性を読み書きするツールで共通して使用します。
  - 形式: [マーカー](Attributes.md#line-end-markers) · [ドロップシャドウ](Attributes.md#drop-shadow)

<a id="document-and-selection"></a>

### ファイルと選択

図面全体: レイヤ、ストーリ、クラス、単位、ビュー、設定、および選択内容を扱います。

- **[DocumentAccess](DocumentAccess.md)** — アクティブな図面全体と現在の選択内容を扱うツールです。ファイルの概要、レイヤ、ストーリ、クラス、単位、ビュー、ファイル設定、および選択オブジェクトの一括編集を提供します。
  - **[Document](DocumentAccess.md#document)** (`document`, 17ツール, 初期状態で有効) — アクティブな図面を扱います: ファイルの概要、レイヤ、ストーリ、クラス、単位、ビュー、ファイル設定。
    - [`getDocumentInfo`](DocumentAccess.md#getdocumentinfo) — アクティブファイルの概要として、ファイル、件数、用紙の境界、ビューの中心、ユーザー原点を返します。
    - [`getLayers`](DocumentAccess.md#getlayers) — レイヤを、種類、表示状態、縮尺、高さ、オブジェクト数、境界と共に一覧表示します。
    - [`createLayer`](DocumentAccess.md#createlayer) — デザインレイヤまたはシートレイヤを作成します。
    - [`editLayer`](DocumentAccess.md#editlayer) — レイヤの名前、表示状態、縮尺、高さ、厚さなどのプロパティを変更します。
    - [`getStories`](DocumentAccess.md#getstories) — ストーリ（建物の階）をレベルと共に、低い順で一覧表示します。
    - [`createStory`](DocumentAccess.md#createstory) — 1つ以上のストーリをレベルと共に作成します。
    - [`editStory`](DocumentAccess.md#editstory) — ストーリ、ファイルのレベルタイプ、またはストーリレベル初期設定を変更します。
    - [`getClasses`](DocumentAccess.md#getclasses) — ファイルのクラスを一覧表示し、特別なクラスの名前を返します。
    - [`createClass`](DocumentAccess.md#createclass) — クラスを作成するか、同名の既存クラスを返します。
    - [`editClass`](DocumentAccess.md#editclass) — クラスの説明、表示状態、線、面、マーカー、ドロップシャドウなどを変更します。
    - [`setActiveContext`](DocumentAccess.md#setactivecontext) — アクティブレイヤとクラス、およびその他のレイヤとクラスの表示方法を設定します。
    - [`getUnits`](DocumentAccess.md#getunits) — ファイルの主単位と補助単位の設定を返します。
    - [`setUnits`](DocumentAccess.md#setunits) — ファイルの主単位または補助単位の設定を変更します。
    - [`convertUnits`](DocumentAccess.md#convertunits) — ワールド単位とファイルの単位の間で長さを変換します。
    - [`setView`](DocumentAccess.md#setview) — ビューの移動、ズームの設定、ユーザー原点の移動、用紙の再描画を行います。
    - [`getPreferences`](DocumentAccess.md#getpreferences) — ファイル設定の1つのカテゴリを読み取ります。
    - [`setPreferences`](DocumentAccess.md#setpreferences) — 1つのカテゴリのファイル設定を書き込みます。
  - **[Selection](DocumentAccess.md#selection)** (`selection`, 3ツール, 初期状態で有効) — 現在の選択内容を一覧表示し、移動、回転、拡大縮小、複製、グループ化、削除、クラス変更を一括で行います。
    - [`getSelection`](DocumentAccess.md#getselection) — 全レイヤの選択オブジェクトと選択範囲の境界を一覧表示します。
    - [`selectObjects`](DocumentAccess.md#selectobjects) — 検索条件やUUIDでオブジェクトを選択、選択解除するか、すべてを選択、選択解除します。
    - [`editSelection`](DocumentAccess.md#editselection) — 選択内容を移動、回転、拡大縮小、複製、グループ化、削除、クラス変更します。

<a id="objects-and-geometry"></a>

### オブジェクトとジオメトリ

あらゆるオブジェクト、2Dプリミティブ、文字列オブジェクト、3Dジオメトリを扱います。

- **[ObjectPrimitives](ObjectPrimitives.md)** — 図面内のあらゆるオブジェクトを扱うツール（検索、調査、スタイル設定、変形、プラグインパラメータ、レコード）と、2Dプリミティブおよび文字列オブジェクトの作成、編集、測定、合成を行うツールです。
  - **[Draw2D](ObjectPrimitives.md#draw2d)** (`draw2d`, 15ツール, 初期状態では無効) — 2Dプリミティブの作成、編集、測定、合成と、文字列オブジェクトの作成、読み取り、編集を行います。
    - [`createLine`](ObjectPrimitives.md#createline) — 2点間に直線を作成します。
    - [`createRectangle`](ObjectPrimitives.md#createrectangle) — 四角形を作成し、必要に応じて回転や角丸を設定します。
    - [`createCircle`](ObjectPrimitives.md#createcircle) — 中心と半径、または通過する3点から円を作成します。
    - [`createArc`](ObjectPrimitives.md#createarc) — 中心、半径、角度、または通過する3点から円弧を作成します。
    - [`createPolygon`](ObjectPrimitives.md#createpolygon) — 点から多角形を作成するか、正多角形を作成します。
    - [`createPolyline`](ObjectPrimitives.md#createpolyline) — 任意の種類の頂点から曲線を作成するか、丸みのある図形を作成します。
    - [`createLocus`](ObjectPrimitives.md#createlocus) — 2D 基準点（参照点）を作成します。
    - [`getGeometry`](ObjectPrimitives.md#getgeometry) — 2Dプリミティブの種類固有の形状を読み取ります。
    - [`setGeometry`](ObjectPrimitives.md#setgeometry) — 2Dプリミティブの形状を編集します。
    - [`editVertices`](ObjectPrimitives.md#editvertices) — 多角形または曲線の頂点を追加、挿入、変更、削除、順序反転、置換します。
    - [`queryGeometry`](ObjectPrimitives.md#querygeometry) — 2Dプリミティブの最近点、距離、包含、交差、接線、および曲線に沿った測定に関する幾何学的な問い合わせに応答します。
    - [`combineShapes`](ObjectPrimitives.md#combineshapes) — 和集合、共通部分、差分、対称差のブーリアン演算で2つの2D図形を合成します。
    - [`createText`](ObjectPrimitives.md#createtext) — 文字列オブジェクトを作成します。
    - [`getText`](ObjectPrimitives.md#gettext) — 文字列オブジェクトの内容、文字書式、スタイル、レイアウトを読み取ります。
    - [`editText`](ObjectPrimitives.md#edittext) — 文字列オブジェクトの内容と書式を編集します。
  - **[Objects](ObjectPrimitives.md#objects)** (`objects`, 12ツール, 初期状態で有効) — あらゆるオブジェクトの検索、調査、編集を行い、属性、変形、コンテナ、プラグインパラメータ、レコードを扱います。
    - [`findObjects`](ObjectPrimitives.md#findobjects) — 条件文字列に一致するオブジェクトを検索します。
    - [`getObjectsAtPoint`](ObjectPrimitives.md#getobjectsatpoint) — 指定した点にあるオブジェクトを検索します。
    - [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo) — オブジェクトの識別情報、クラス、レイヤ、境界、状態、コンテナを返します。
    - [`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes) — オブジェクトのグラフィック属性を返します。
    - [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) — 線、面、不透明度、マーカー、ドロップシャドウなど、オブジェクトのグラフィック属性を設定します。
    - [`copyAttributes`](ObjectPrimitives.md#copyattributes) — あるオブジェクトのグラフィック属性を他のオブジェクトにコピーします。
    - [`editObject`](ObjectPrimitives.md#editobject) — オブジェクトの移動、回転、拡大縮小、ミラー反転、複製、グループ構成の変更、変換、リセット、削除、または名前とクラスの変更を行います。
    - [`getObjectParameters`](ObjectPrimitives.md#getobjectparameters) — プラグインオブジェクトのパラメータを読み取ります。
    - [`getObjectRecords`](ObjectPrimitives.md#getobjectrecords) — オブジェクトに付加されたデータレコードを読み取ります。
    - [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) — プラグインオブジェクトの1つ以上のパラメータを書き込みます。
    - [`getPluginDefinition`](ObjectPrimitives.md#getplugindefinition) — インストール済みのプラグインオブジェクトの種類、パラメータ、ポップアップの選択肢を示します。
    - [`createPluginObject`](ObjectPrimitives.md#createpluginobject) — 専用の作成ツールがないプラグインオブジェクトを作成します。
- **[Objects3D](Objects3D.md)** — ソリッド、3D 多角形、メッシュ、NURBS曲線と曲面、サーフェスモデルの3D形状を作成、読み取り、編集するツールです。
  - **[3D Modeling](Objects3D.md#3d-modeling)** (`3d-modeling`, 16ツール, 初期状態では無効) — ソリッド、3D 多角形、メッシュ、NURBS曲線と曲面、サーフェスモデルを作成、読み取り、編集します。
    - [`createExtrude`](Objects3D.md#createextrude) — 押し出し、多段押し出し、またはテーパ押し出しを作成します。
    - [`createSolidPrimitive`](Objects3D.md#createsolidprimitive) — 球、楕円体、半球、円錐、直方体、円筒、トーラスを作成します。
    - [`createSweep`](Objects3D.md#createsweep) — 回転体（軸の周りに回転させた2D断面）を作成します。
    - [`combineSolids`](Objects3D.md#combinesolids) — 和集合、共通部分、差分の演算で2つのソリッドを汎用ソリッドに合成します。
    - [`createShell`](Objects3D.md#createshell) — NURBS曲面に厚みを付けるか、ソリッドを中空にして、シェルを作成します。
    - [`convertSolid`](Objects3D.md#convertsolid) — ソリッドを汎用ソリッドまたはメッシュに変換したコピーを作成します。
    - [`getSolid`](Objects3D.md#getsolid) — ソリッドの種類、3D境界、パラメータ、汎用ソリッドの履歴を読み取ります。
    - [`editSolid`](Objects3D.md#editsolid) — ソリッドの移動、回転、拡大縮小、向きの変更、サイズ変更を行います。
    - [`create3DPolygon`](Objects3D.md#create3dpolygon) — 3D点、指定した高さの2D点、または矩形から3D 多角形を作成します。
    - [`createMesh`](Objects3D.md#createmesh) — 頂点と面、多角形、または3D 多角形のグループからメッシュを作成します。
    - [`createNurbsCurve`](Objects3D.md#createnurbscurve) — 制御点または補間点からNURBS曲線を作成します。
    - [`createNurbsSurface`](Objects3D.md#createnurbssurface) — 制御点ネットからNURBS曲面を作成します。
    - [`createSurfaceModel`](Objects3D.md#createsurfacemodel) — 既存のオブジェクトから、ロフト（多段曲面）、レールスイープ、回転、パス押し出しのサーフェスモデルを作成します。
    - [`get3DGeometry`](Objects3D.md#get3dgeometry) — 3D 多角形、メッシュ、NURBS曲線、NURBS曲面を読み取ります。
    - [`edit3DGeometry`](Objects3D.md#edit3dgeometry) — 3D 多角形、メッシュ、NURBS曲線、NURBS曲面を編集します。
    - [`convertTo3D`](Objects3D.md#convertto3d) — オブジェクトのコピーを3D 多角形、メッシュ、または汎用ソリッドに変換します。

<a id="annotation"></a>

### 注釈

データタグ、図面枠、寸法を扱います。

- **[ObjectsAnnotation](ObjectsAnnotation.md)** — データタグ、図面枠と表題欄のプロジェクトデータ、およびセンターマークを含む寸法など、注釈を扱うツールです。
  - **[Annotation](ObjectsAnnotation.md#annotation)** (`annotation`, 8ツール, 初期状態では無効) — データタグ、図面枠、およびファイルの表題欄のプロジェクトデータを扱います。
    - [`createDataTag`](ObjectsAnnotation.md#createdatatag) — データタグを作成し、必要に応じてオブジェクトに関連付けます。
    - [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock) — 図面枠を作成します。
    - [`getAnnotationObject`](ObjectsAnnotation.md#getannotationobject) — データタグまたは図面枠を読み取ります。
    - [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject) — データタグまたは図面枠を編集します。
    - [`tagObject`](ObjectsAnnotation.md#tagobject) — データタグをオブジェクトに関連付けるか、関連付けを解除します。
    - [`getObjectTags`](ObjectsAnnotation.md#getobjecttags) — オブジェクトに関連付けられているデータタグを一覧表示します。
    - [`getProjectData`](ObjectsAnnotation.md#getprojectdata) — ファイルの表題欄のプロジェクトデータを読み取ります。
    - [`setProjectData`](ObjectsAnnotation.md#setprojectdata) — ファイルの表題欄のプロジェクトデータを書き込みます。
  - **[Dimensioning](ObjectsAnnotation.md#dimensioning)** (`dimensioning`, 8ツール, 初期状態では無効) — 直線寸法、角度寸法、円弧長寸法、円寸法、およびセンターマークを扱います。
    - [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension) — 縦横、水平、垂直、斜め、または累進の直線寸法を作成します。
    - [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension) — 角度寸法を作成します。
    - [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension) — 円弧長寸法を作成します。
    - [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension) — 半径寸法または直径寸法を作成します。
    - [`createCenterMark`](ObjectsAnnotation.md#createcentermark) — 円形の部分のセンターマークを作成します。
    - [`getDimension`](ObjectsAnnotation.md#getdimension) — 寸法線オブジェクトの種類、測定点、値、および文字の設定を読み取ります。
    - [`setDimension`](ObjectsAnnotation.md#setdimension) — 寸法線オブジェクトを編集します。
    - [`getObjectDimensions`](ObjectsAnnotation.md#getobjectdimensions) — オブジェクトに関連付けられている寸法線オブジェクトを一覧表示します。

<a id="industry-objects"></a>

### 業種別オブジェクト

建築、造園、エンタテインメント照明、AVシステムのオブジェクトを扱います。

- **[ObjectsArchitect](ObjectsArchitect.md)** — BIMの建築要素である壁、スラブ、屋根、ドア、窓、柱、階段のためのツールです。
  - **[Architecture](ObjectsArchitect.md#architecture)** (`architecture`, 9ツール, 初期状態では無効) — BIMの建築要素：壁、スラブ、屋根、ドア、窓、柱、階段。
    - [`createWall`](ObjectsArchitect.md#createwall) — 直線壁または円弧壁を作成します。
    - [`createSlab`](ObjectsArchitect.md#createslab) — 2D境界オブジェクトからスラブを作成します。
    - [`createRoof`](ObjectsArchitect.md#createroof) — 多角形の屋根を作成します。
    - [`createDoor`](ObjectsArchitect.md#createdoor) — 単独のドアを作成します。
    - [`createWindow`](ObjectsArchitect.md#createwindow) — 単独の窓を作成します。
    - [`createColumn`](ObjectsArchitect.md#createcolumn) — 柱を作成します。
    - [`createStair`](ObjectsArchitect.md#createstair) — 階段を作成します。
    - [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject) — 壁、スラブ、屋根、ドア、窓、柱、階段のプロパティを読み取ります。
    - [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject) — 壁、スラブ、屋根、ドア、窓、柱、階段を編集します。
- **[ObjectsLandmark](ObjectsLandmark.md)** — 敷地とランドスケープのオブジェクト（植栽、舗床、ランドスケープエリア、地形モデル、造成図形、レベルオブジェクト、境界線、既存樹木）のためのツールです。
  - **[Landmark](ObjectsLandmark.md#landmark)** (`landmark`, 10ツール, 初期状態では無効) — 植栽、舗床、ランドスケープエリア、地形モデル、造成図形、レベルオブジェクト、境界線、既存樹木。
    - [`createPlant`](ObjectsLandmark.md#createplant) — 点の位置またはパスに沿って植栽を作成します。
    - [`createHardscape`](ObjectsLandmark.md#createhardscape) — 2Dパスオブジェクトから舗床を作成します。
    - [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea) — 2Dパスオブジェクトからランドスケープエリアを作成します。
    - [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier) — 2Dパスオブジェクトから造成図形を作成します。
    - [`createPropertyLine`](ObjectsLandmark.md#createpropertyline) — 閉じた2Dパスオブジェクトから境界線を作成します。
    - [`createSiteModel`](ObjectsLandmark.md#createsitemodel) — 空の地形モデルを作成します。
    - [`createStake`](ObjectsLandmark.md#createstake) — レベルオブジェクト（高さを示す点）を作成します。
    - [`createExistingTree`](ObjectsLandmark.md#createexistingtree) — 既存樹木を作成します。
    - [`getLandmarkObject`](ObjectsLandmark.md#getlandmarkobject) — 敷地またはランドスケープのオブジェクトのプロパティを読み取ります。
    - [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject) — 敷地またはランドスケープのオブジェクトを編集します。
- **[ObjectsSpotlight](ObjectsSpotlight.md)** — SpotlightのLighting Deviceと、それらが使用するGDTF（General Device Type Format）器具タイプのためのツールです。
  - **[Spotlight](ObjectsSpotlight.md#spotlight)** (`spotlight`, 5ツール, 初期状態では無効) — SpotlightのLighting Deviceと、それらが使用するGDTF器具タイプ。
    - [`listGDTFs`](ObjectsSpotlight.md#listgdtfs) — 使用可能なGDTF器具タイプとそのDMXモードの一覧を返します。
    - [`importGDTF`](ObjectsSpotlight.md#importgdtf) — .gdtfファイルをGDTF器具タイプとして図面に取り込みます。
    - [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice) — 必要に応じてGDTF器具タイプを指定して、Lighting Deviceを作成します。
    - [`getLightingDevice`](ObjectsSpotlight.md#getlightingdevice) — Lighting Deviceを読み取ります。
    - [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice) — Lighting Deviceを編集します。
- **[ObjectsConnectCAD](ObjectsConnectCAD.md)** — ConnectCADの配線略図のDevice、そのSocketとDevice Type、およびそれらが使用するSignal TypeとConnector Typeのためのツールです。
  - **[ConnectCAD](ObjectsConnectCAD.md#connectcad)** (`connectcad`, 10ツール, 初期状態では無効) — JSONのDevice記述データから構築する、ConnectCADの配線略図のDevice、Socket、Device Type。
    - [`listConnectCADSignals`](ObjectsConnectCAD.md#listconnectcadsignals) — ConnectCADのSignal Typeの一覧を返します。
    - [`listConnectCADConnectors`](ObjectsConnectCAD.md#listconnectcadconnectors) — ConnectCADのConnector Typeとそのピンの一覧を返します。
    - [`validateConnectCADDevice`](ObjectsConnectCAD.md#validateconnectcaddevice) — 何も作成せずにDevice記述データを検証します。
    - [`createConnectCADDevice`](ObjectsConnectCAD.md#createconnectcaddevice) — Device記述データから全Socketを含む配線略図のDeviceを作成します。
    - [`createConnectCADDevices`](ObjectsConnectCAD.md#createconnectcaddevices) — 1回の操作で複数の配線略図のDeviceを横一列に作成します。
    - [`getConnectCADDevice`](ObjectsConnectCAD.md#getconnectcaddevice) — ConnectCADのDeviceとそのSocketを読み取ります。
    - [`addConnectCADSocket`](ObjectsConnectCAD.md#addconnectcadsocket) — DeviceにSocketを追加します。
    - [`setConnectCADSocket`](ObjectsConnectCAD.md#setconnectcadsocket) — Socketを編集します。
    - [`createConnectCADDeviceType`](ObjectsConnectCAD.md#createconnectcaddevicetype) — DeviceのDevice Typeシンボルを作成します。
    - [`getConnectCADDeviceType`](ObjectsConnectCAD.md#getconnectcaddevicetype) — Device TypeのシンボルのDevice Definitionレコードを読み取ります。

<a id="resources-and-data"></a>

### リソースとデータ

リソース、ワークシート、IFCデータを扱います。

- **[Resources](Resources.md)** — 図面のリソースと外部コンテンツ（ライブラリ、ディスク上のファイル、開いている他のファイル）のリソース、およびワークシートのためのツールです。
  - **[Resources](Resources.md#resources)** (`resources`, 11ツール, 初期状態では無効) — リソースを一覧表示、取り込み、作成、確認、編集、適用し、ワークシートを読み取り、編集します。
    - [`getResourceTypes`](Resources.md#getresourcetypes) — リソースタイプと標準コンテンツフォルダを一覧表示します。
    - [`getResources`](Resources.md#getresources) — 図面、ライブラリ、ディスク上のファイル、または開いている他のファイルから、1つのタイプのリソースを一覧表示します。
    - [`getResource`](Resources.md#getresource) — 図面のリソースを1つ読み取ります。
    - [`importResource`](Resources.md#importresource) — 外部のリソースを図面に取り込みます。
    - [`editResource`](Resources.md#editresource) — リソースの名前変更、説明の設定、移動、複製、削除を行います。
    - [`createResource`](Resources.md#createresource) — 空のリソースを作成します。
    - [`getResourceDetails`](Resources.md#getresourcedetails) — ハッチングのレベル、グラデーションの変化点、ラインタイプの破線など、リソースの内容を読み取ります。
    - [`setResourceDetails`](Resources.md#setresourcedetails) — リソースの内容を変更します。
    - [`applyResource`](Resources.md#applyresource) — テクスチャ、スタイル、データの可視化をオブジェクトに適用します。
    - [`getWorksheet`](Resources.md#getworksheet) — ワークシートのサイズ、セル、書式、データベース行を読み取ります。
    - [`editWorksheet`](Resources.md#editworksheet) — アクションのリストでワークシートを変更します。
- **[IFC](IFC.md)** — 図面のIFC（Industry Foundation Classes）データへの読み取り専用アクセスです。オブジェクトのIFCエンティティとプロパティセット、プロパティセットの定義、およびファイルのデータマネージャのIFCマッピングを扱います。
  - **[IFC](IFC.md#ifc)** (`ifc`, 4ツール, 初期状態で有効) — 読み取り専用のIFCデータ: オブジェクトのIFCエンティティとプロパティセット、IFCプロパティセットの定義（標準とカスタム）、およびファイルのカスタムプロパティセットです。
    - [`getObjectIFCData`](IFC.md#getobjectifcdata) — IFC取り出しで計算されるとおりに、オブジェクトのIFCデータを読み取ります。
    - [`getIFCPsetDefinition`](IFC.md#getifcpsetdefinition) — IFCプロパティセットの定義を名前で1つ読み取ります。
    - [`listIFCPsets`](IFC.md#listifcpsets) — IFCエンティティタイプに適用できるIFCプロパティセットを一覧表示します。
    - [`listIFCCustomPsets`](IFC.md#listifccustompsets) — ファイルのカスタムIFCプロパティセット定義を一覧表示します。
  - **[IFC Data Mapping](IFC.md#ifc-data-mapping)** (`ifc-data-mapping`, 2ツール, 初期状態では無効) — アクティブファイルのデータマネージャのIFCマッピング定義を読み取ります。
    - [`listIFCMappingObjects`](IFC.md#listifcmappingobjects) — アクティブなデータマネージャのマッピングの、マッピングオブジェクトを一覧表示します。
    - [`getIFCMapping`](IFC.md#getifcmapping) — 1つのマッピングオブジェクトのデータマネージャのマッピングを読み取ります。

<a id="automation-and-user-interface"></a>

### 自動化とユーザーインターフェイス

スクリプト、対話型ツール、オブジェクト情報パレット、メニューコマンドを扱います。

- **[Scripting](Scripting.md)** — Vectorworks内でのPythonスクリプトの実行、Pythonスクリプトリソースの読み取りと保存、およびスクリプトで使用するPythonの`api`モジュールの参照を行うツールです。
  - **[Scripting](Scripting.md#scripting)** (`scripting`, 7ツール, 初期状態では無効) — Pythonスクリプトの実行、Pythonスクリプトリソースの読み取りと保存、およびPythonの`api`モジュールの参照を行います。
    - [`listScripts`](Scripting.md#listscripts) — ファイルのスクリプトリソースを一覧表示します。
    - [`getScript`](Scripting.md#getscript) — スクリプトリソースを実行せずに読み取ります。
    - [`saveScript`](Scripting.md#savescript) — Pythonスクリプトリソースを実行せずに作成または更新します。
    - [`describePythonApi`](Scripting.md#describepythonapi) — Pythonの`api`モジュール、またはその名前の1つのヘルプテキストを返します。
    - [`getPythonApiGuide`](Scripting.md#getpythonapiguide) — Pythonスクリプトを作成するためのガイドの1セクションを返します。
    - [`runPythonScript`](Scripting.md#runpythonscript) — Vectorworks内でPythonコードを実行します。
    - [`runScript`](Scripting.md#runscript) — 保存済みのPythonスクリプトリソースを実行します。
- **[ToolAccess](ToolAccess.md)** — ツールパレットの対話型Vectorworksツールを、ユーザーと同じように操作するツールです: ツールをアクティブにし、モードを設定し、図面内をクリックします。
  - **[InteractiveTools](ToolAccess.md#interactivetools)** (`interactivetools`, 10ツール, 初期状態では無効) — ツールパレットの対話型Vectorworksツールを、ユーザーと同じように操作します。
    - [`getTools`](ToolAccess.md#gettools) — Vectorworksのツールを一覧表示します。
    - [`getTool`](ToolAccess.md#gettool) — 定義されたツールバーボタンと共に1つのツールを返します。
    - [`getActiveTool`](ToolAccess.md#getactivetool) — アクティブツールの状態を返します。
    - [`activateTool`](ToolAccess.md#activatetool) — ツールをアクティブにします。
    - [`getToolModes`](ToolAccess.md#gettoolmodes) — アクティブツールの現在のツールバーを読み取ります。
    - [`setToolMode`](ToolAccess.md#settoolmode) — アクティブツールのモードを1つ変更します。
    - [`setToolModes`](ToolAccess.md#settoolmodes) — アクティブツールのモードを複数設定します。
    - [`sendToolPointer`](ToolAccess.md#sendtoolpointer) — アクティブツールで図面内をクリック、ダブルクリック、ホバー、ドラッグします。
    - [`sendToolAction`](ToolAccess.md#sendtoolaction) — アクティブツールの操作を完了またはキャンセルするか、最後の点を削除します。
    - [`convertToolCoordinates`](ToolAccess.md#converttoolcoordinates) — モデル空間とアクティブペインのビューの間で点を変換します。
- **[OIPAccess](OIPAccess.md)** — 現在の選択に対するオブジェクト情報パレットを、ユーザーと同じように読み取り、操作するツールです。
  - **[Object Info](OIPAccess.md#object-info)** (`object-info`, 3ツール, 初期状態では無効) — 現在の選択に対するオブジェクト情報パレットを、ユーザーと同じように読み取り、操作します。
    - [`getOIPControls`](OIPAccess.md#getoipcontrols) — オブジェクト情報パレットの1つのタブのコントロールを一覧表示します。
    - [`setOIPValues`](OIPAccess.md#setoipvalues) — ユーザーと同じように、オブジェクト情報パレットのコントロールを設定します。
    - [`pressOIPButton`](OIPAccess.md#pressoipbutton) — オブジェクト情報パレットのボタンを押します。
- **[MenuAccess](MenuAccess.md)** — Vectorworksのメニューを読み取り、コマンドを実行できるかどうかを確認し、ユーザーが選択した場合と同じようにメニューコマンドを実行するツールです。
  - **[Menus](MenuAccess.md#menus)** (`menus`, 4ツール, 初期状態では無効) — メニューコマンドの検索、メニューバーの読み取り、コマンドを現在実行できるかどうかの確認、およびその実行を行います。
    - [`findMenuCommands`](MenuAccess.md#findmenucommands) — インストール済みのメニューコマンドを、テキストと作業画面で検索します。
    - [`getMenus`](MenuAccess.md#getmenus) — 現在の作業画面のメニューバー、1つのメニュー、またはチャンクメニューの項目を読み取ります。
    - [`getMenuStatus`](MenuAccess.md#getmenustatus) — メニューコマンドまたはチャンクメニュー項目を現在実行できるかどうか、できない場合はその理由を返します。
    - [`runMenuCommand`](MenuAccess.md#runmenucommand) — ユーザーが選択した場合と同じように、メニューコマンドまたはチャンクメニュー項目を実行します。

<a id="index-az"></a>

## A–Z索引

[A](#index-a) · [C](#index-c) · [D](#index-d) · [E](#index-e) · [F](#index-f) · [G](#index-g) · [I](#index-i) · [L](#index-l) · [P](#index-p) · [Q](#index-q) · [R](#index-r) · [S](#index-s) · [T](#index-t) · [V](#index-v)

<a id="index-a"></a>

### 索引 A

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`activateTool`](ToolAccess.md#activatetool) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | ツールをアクティブにします。 |
| [`activateToolGroups`](Common.md#activatetoolgroups) | [Core](Common.md#core-group) | [Common](Common.md) | サーバーが停止されるまで、ツールグループを有効にして、そのツールをツール一覧に表示します。 |
| [`addConnectCADSocket`](ObjectsConnectCAD.md#addconnectcadsocket) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | DeviceにSocketを追加します。 |
| [`applyResource`](Resources.md#applyresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | テクスチャ、スタイル、データの可視化をオブジェクトに適用します。 |

<a id="index-c"></a>

### 索引 C

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`combineShapes`](ObjectPrimitives.md#combineshapes) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 和集合、共通部分、差分、対称差のブーリアン演算で2つの2D図形を合成します。 |
| [`combineSolids`](Objects3D.md#combinesolids) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 和集合、共通部分、差分の演算で2つのソリッドを汎用ソリッドに合成します。 |
| [`convertSolid`](Objects3D.md#convertsolid) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | ソリッドを汎用ソリッドまたはメッシュに変換したコピーを作成します。 |
| [`convertTo3D`](Objects3D.md#convertto3d) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | オブジェクトのコピーを3D 多角形、メッシュ、または汎用ソリッドに変換します。 |
| [`convertToolCoordinates`](ToolAccess.md#converttoolcoordinates) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | モデル空間とアクティブペインのビューの間で点を変換します。 |
| [`convertUnits`](DocumentAccess.md#convertunits) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | ワールド単位とファイルの単位の間で長さを変換します。 |
| [`copyAttributes`](ObjectPrimitives.md#copyattributes) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | あるオブジェクトのグラフィック属性を他のオブジェクトにコピーします。 |
| [`create3DPolygon`](Objects3D.md#create3dpolygon) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 3D点、指定した高さの2D点、または矩形から3D 多角形を作成します。 |
| [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | 角度寸法を作成します。 |
| [`createArc`](ObjectPrimitives.md#createarc) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 中心、半径、角度、または通過する3点から円弧を作成します。 |
| [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | 円弧長寸法を作成します。 |
| [`createCenterMark`](ObjectsAnnotation.md#createcentermark) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | 円形の部分のセンターマークを作成します。 |
| [`createCircle`](ObjectPrimitives.md#createcircle) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 中心と半径、または通過する3点から円を作成します。 |
| [`createClass`](DocumentAccess.md#createclass) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | クラスを作成するか、同名の既存クラスを返します。 |
| [`createColumn`](ObjectsArchitect.md#createcolumn) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | 柱を作成します。 |
| [`createConnectCADDevice`](ObjectsConnectCAD.md#createconnectcaddevice) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Device記述データから全Socketを含む配線略図のDeviceを作成します。 |
| [`createConnectCADDevices`](ObjectsConnectCAD.md#createconnectcaddevices) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | 1回の操作で複数の配線略図のDeviceを横一列に作成します。 |
| [`createConnectCADDeviceType`](ObjectsConnectCAD.md#createconnectcaddevicetype) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | DeviceのDevice Typeシンボルを作成します。 |
| [`createDataTag`](ObjectsAnnotation.md#createdatatag) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | データタグを作成し、必要に応じてオブジェクトに関連付けます。 |
| [`createDoor`](ObjectsArchitect.md#createdoor) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | 単独のドアを作成します。 |
| [`createExistingTree`](ObjectsLandmark.md#createexistingtree) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | 既存樹木を作成します。 |
| [`createExtrude`](Objects3D.md#createextrude) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 押し出し、多段押し出し、またはテーパ押し出しを作成します。 |
| [`createHardscape`](ObjectsLandmark.md#createhardscape) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | 2Dパスオブジェクトから舗床を作成します。 |
| [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | 2Dパスオブジェクトからランドスケープエリアを作成します。 |
| [`createLayer`](DocumentAccess.md#createlayer) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | デザインレイヤまたはシートレイヤを作成します。 |
| [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | 必要に応じてGDTF器具タイプを指定して、Lighting Deviceを作成します。 |
| [`createLine`](ObjectPrimitives.md#createline) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 2点間に直線を作成します。 |
| [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | 縦横、水平、垂直、斜め、または累進の直線寸法を作成します。 |
| [`createLocus`](ObjectPrimitives.md#createlocus) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 2D 基準点（参照点）を作成します。 |
| [`createMesh`](Objects3D.md#createmesh) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 頂点と面、多角形、または3D 多角形のグループからメッシュを作成します。 |
| [`createNurbsCurve`](Objects3D.md#createnurbscurve) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 制御点または補間点からNURBS曲線を作成します。 |
| [`createNurbsSurface`](Objects3D.md#createnurbssurface) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 制御点ネットからNURBS曲面を作成します。 |
| [`createPlant`](ObjectsLandmark.md#createplant) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | 点の位置またはパスに沿って植栽を作成します。 |
| [`createPluginObject`](ObjectPrimitives.md#createpluginobject) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | 専用の作成ツールがないプラグインオブジェクトを作成します。 |
| [`createPolygon`](ObjectPrimitives.md#createpolygon) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 点から多角形を作成するか、正多角形を作成します。 |
| [`createPolyline`](ObjectPrimitives.md#createpolyline) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 任意の種類の頂点から曲線を作成するか、丸みのある図形を作成します。 |
| [`createPropertyLine`](ObjectsLandmark.md#createpropertyline) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | 閉じた2Dパスオブジェクトから境界線を作成します。 |
| [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | 半径寸法または直径寸法を作成します。 |
| [`createRectangle`](ObjectPrimitives.md#createrectangle) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 四角形を作成し、必要に応じて回転や角丸を設定します。 |
| [`createResource`](Resources.md#createresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | 空のリソースを作成します。 |
| [`createRoof`](ObjectsArchitect.md#createroof) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | 多角形の屋根を作成します。 |
| [`createShell`](Objects3D.md#createshell) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | NURBS曲面に厚みを付けるか、ソリッドを中空にして、シェルを作成します。 |
| [`createSiteModel`](ObjectsLandmark.md#createsitemodel) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | 空の地形モデルを作成します。 |
| [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | 2Dパスオブジェクトから造成図形を作成します。 |
| [`createSlab`](ObjectsArchitect.md#createslab) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | 2D境界オブジェクトからスラブを作成します。 |
| [`createSolidPrimitive`](Objects3D.md#createsolidprimitive) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 球、楕円体、半球、円錐、直方体、円筒、トーラスを作成します。 |
| [`createStair`](ObjectsArchitect.md#createstair) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | 階段を作成します。 |
| [`createStake`](ObjectsLandmark.md#createstake) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | レベルオブジェクト（高さを示す点）を作成します。 |
| [`createStory`](DocumentAccess.md#createstory) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | 1つ以上のストーリをレベルと共に作成します。 |
| [`createSurfaceModel`](Objects3D.md#createsurfacemodel) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 既存のオブジェクトから、ロフト（多段曲面）、レールスイープ、回転、パス押し出しのサーフェスモデルを作成します。 |
| [`createSweep`](Objects3D.md#createsweep) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 回転体（軸の周りに回転させた2D断面）を作成します。 |
| [`createText`](ObjectPrimitives.md#createtext) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 文字列オブジェクトを作成します。 |
| [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | 図面枠を作成します。 |
| [`createWall`](ObjectsArchitect.md#createwall) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | 直線壁または円弧壁を作成します。 |
| [`createWindow`](ObjectsArchitect.md#createwindow) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | 単独の窓を作成します。 |

<a id="index-d"></a>

### 索引 D

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`describePythonApi`](Scripting.md#describepythonapi) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Pythonの`api`モジュール、またはその名前の1つのヘルプテキストを返します。 |

<a id="index-e"></a>

### 索引 E

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`edit3DGeometry`](Objects3D.md#edit3dgeometry) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 3D 多角形、メッシュ、NURBS曲線、NURBS曲面を編集します。 |
| [`editClass`](DocumentAccess.md#editclass) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | クラスの説明、表示状態、線、面、マーカー、ドロップシャドウなどを変更します。 |
| [`editLayer`](DocumentAccess.md#editlayer) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | レイヤの名前、表示状態、縮尺、高さ、厚さなどのプロパティを変更します。 |
| [`editObject`](ObjectPrimitives.md#editobject) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | オブジェクトの移動、回転、拡大縮小、ミラー反転、複製、グループ構成の変更、変換、リセット、削除、または名前とクラスの変更を行います。 |
| [`editResource`](Resources.md#editresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | リソースの名前変更、説明の設定、移動、複製、削除を行います。 |
| [`editSelection`](DocumentAccess.md#editselection) | [Selection](DocumentAccess.md#selection) | [DocumentAccess](DocumentAccess.md) | 選択内容を移動、回転、拡大縮小、複製、グループ化、削除、クラス変更します。 |
| [`editSolid`](Objects3D.md#editsolid) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | ソリッドの移動、回転、拡大縮小、向きの変更、サイズ変更を行います。 |
| [`editStory`](DocumentAccess.md#editstory) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | ストーリ、ファイルのレベルタイプ、またはストーリレベル初期設定を変更します。 |
| [`editText`](ObjectPrimitives.md#edittext) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 文字列オブジェクトの内容と書式を編集します。 |
| [`editVertices`](ObjectPrimitives.md#editvertices) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 多角形または曲線の頂点を追加、挿入、変更、削除、順序反転、置換します。 |
| [`editWorksheet`](Resources.md#editworksheet) | [Resources](Resources.md#resources) | [Resources](Resources.md) | アクションのリストでワークシートを変更します。 |

<a id="index-f"></a>

### 索引 F

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`findMenuCommands`](MenuAccess.md#findmenucommands) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | インストール済みのメニューコマンドを、テキストと作業画面で検索します。 |
| [`findObjects`](ObjectPrimitives.md#findobjects) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | 条件文字列に一致するオブジェクトを検索します。 |

<a id="index-g"></a>

### 索引 G

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`get3DGeometry`](Objects3D.md#get3dgeometry) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | 3D 多角形、メッシュ、NURBS曲線、NURBS曲面を読み取ります。 |
| [`getActiveTool`](ToolAccess.md#getactivetool) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | アクティブツールの状態を返します。 |
| [`getAnnotationObject`](ObjectsAnnotation.md#getannotationobject) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | データタグまたは図面枠を読み取ります。 |
| [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | 壁、スラブ、屋根、ドア、窓、柱、階段のプロパティを読み取ります。 |
| [`getClasses`](DocumentAccess.md#getclasses) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | ファイルのクラスを一覧表示し、特別なクラスの名前を返します。 |
| [`getConnectCADDevice`](ObjectsConnectCAD.md#getconnectcaddevice) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCADのDeviceとそのSocketを読み取ります。 |
| [`getConnectCADDeviceType`](ObjectsConnectCAD.md#getconnectcaddevicetype) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Device TypeのシンボルのDevice Definitionレコードを読み取ります。 |
| [`getDimension`](ObjectsAnnotation.md#getdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | 寸法線オブジェクトの種類、測定点、値、および文字の設定を読み取ります。 |
| [`getDocumentInfo`](DocumentAccess.md#getdocumentinfo) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | アクティブファイルの概要として、ファイル、件数、用紙の境界、ビューの中心、ユーザー原点を返します。 |
| [`getGeometry`](ObjectPrimitives.md#getgeometry) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 2Dプリミティブの種類固有の形状を読み取ります。 |
| [`getIFCMapping`](IFC.md#getifcmapping) | [IFC Data Mapping](IFC.md#ifc-data-mapping) | [IFC](IFC.md) | 1つのマッピングオブジェクトのデータマネージャのマッピングを読み取ります。 |
| [`getIFCPsetDefinition`](IFC.md#getifcpsetdefinition) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | IFCプロパティセットの定義を名前で1つ読み取ります。 |
| [`getLandmarkObject`](ObjectsLandmark.md#getlandmarkobject) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | 敷地またはランドスケープのオブジェクトのプロパティを読み取ります。 |
| [`getLayers`](DocumentAccess.md#getlayers) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | レイヤを、種類、表示状態、縮尺、高さ、オブジェクト数、境界と共に一覧表示します。 |
| [`getLightingDevice`](ObjectsSpotlight.md#getlightingdevice) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Lighting Deviceを読み取ります。 |
| [`getMenus`](MenuAccess.md#getmenus) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | 現在の作業画面のメニューバー、1つのメニュー、またはチャンクメニューの項目を読み取ります。 |
| [`getMenuStatus`](MenuAccess.md#getmenustatus) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | メニューコマンドまたはチャンクメニュー項目を現在実行できるかどうか、できない場合はその理由を返します。 |
| [`getObjectAttributes`](ObjectPrimitives.md#getobjectattributes) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | オブジェクトのグラフィック属性を返します。 |
| [`getObjectDimensions`](ObjectsAnnotation.md#getobjectdimensions) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | オブジェクトに関連付けられている寸法線オブジェクトを一覧表示します。 |
| [`getObjectIFCData`](IFC.md#getobjectifcdata) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | IFC取り出しで計算されるとおりに、オブジェクトのIFCデータを読み取ります。 |
| [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | オブジェクトの識別情報、クラス、レイヤ、境界、状態、コンテナを返します。 |
| [`getObjectParameters`](ObjectPrimitives.md#getobjectparameters) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | プラグインオブジェクトのパラメータを読み取ります。 |
| [`getObjectRecords`](ObjectPrimitives.md#getobjectrecords) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | オブジェクトに付加されたデータレコードを読み取ります。 |
| [`getObjectsAtPoint`](ObjectPrimitives.md#getobjectsatpoint) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | 指定した点にあるオブジェクトを検索します。 |
| [`getObjectTags`](ObjectsAnnotation.md#getobjecttags) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | オブジェクトに関連付けられているデータタグを一覧表示します。 |
| [`getOIPControls`](OIPAccess.md#getoipcontrols) | [Object Info](OIPAccess.md#object-info) | [OIPAccess](OIPAccess.md) | オブジェクト情報パレットの1つのタブのコントロールを一覧表示します。 |
| [`getPluginDefinition`](ObjectPrimitives.md#getplugindefinition) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | インストール済みのプラグインオブジェクトの種類、パラメータ、ポップアップの選択肢を示します。 |
| [`getPreferences`](DocumentAccess.md#getpreferences) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | ファイル設定の1つのカテゴリを読み取ります。 |
| [`getProjectData`](ObjectsAnnotation.md#getprojectdata) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | ファイルの表題欄のプロジェクトデータを読み取ります。 |
| [`getPythonApiGuide`](Scripting.md#getpythonapiguide) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Pythonスクリプトを作成するためのガイドの1セクションを返します。 |
| [`getResource`](Resources.md#getresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | 図面のリソースを1つ読み取ります。 |
| [`getResourceDetails`](Resources.md#getresourcedetails) | [Resources](Resources.md#resources) | [Resources](Resources.md) | ハッチングのレベル、グラデーションの変化点、ラインタイプの破線など、リソースの内容を読み取ります。 |
| [`getResources`](Resources.md#getresources) | [Resources](Resources.md#resources) | [Resources](Resources.md) | 図面、ライブラリ、ディスク上のファイル、または開いている他のファイルから、1つのタイプのリソースを一覧表示します。 |
| [`getResourceTypes`](Resources.md#getresourcetypes) | [Resources](Resources.md#resources) | [Resources](Resources.md) | リソースタイプと標準コンテンツフォルダを一覧表示します。 |
| [`getScript`](Scripting.md#getscript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | スクリプトリソースを実行せずに読み取ります。 |
| [`getSelection`](DocumentAccess.md#getselection) | [Selection](DocumentAccess.md#selection) | [DocumentAccess](DocumentAccess.md) | 全レイヤの選択オブジェクトと選択範囲の境界を一覧表示します。 |
| [`getSolid`](Objects3D.md#getsolid) | [3D Modeling](Objects3D.md#3d-modeling) | [Objects3D](Objects3D.md) | ソリッドの種類、3D境界、パラメータ、汎用ソリッドの履歴を読み取ります。 |
| [`getStories`](DocumentAccess.md#getstories) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | ストーリ（建物の階）をレベルと共に、低い順で一覧表示します。 |
| [`getText`](ObjectPrimitives.md#gettext) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 文字列オブジェクトの内容、文字書式、スタイル、レイアウトを読み取ります。 |
| [`getTool`](ToolAccess.md#gettool) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | 定義されたツールバーボタンと共に1つのツールを返します。 |
| [`getToolModes`](ToolAccess.md#gettoolmodes) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | アクティブツールの現在のツールバーを読み取ります。 |
| [`getTools`](ToolAccess.md#gettools) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | Vectorworksのツールを一覧表示します。 |
| [`getUnits`](DocumentAccess.md#getunits) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | ファイルの主単位と補助単位の設定を返します。 |
| [`getWorksheet`](Resources.md#getworksheet) | [Resources](Resources.md#resources) | [Resources](Resources.md) | ワークシートのサイズ、セル、書式、データベース行を読み取ります。 |

<a id="index-i"></a>

### 索引 I

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`importGDTF`](ObjectsSpotlight.md#importgdtf) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | .gdtfファイルをGDTF器具タイプとして図面に取り込みます。 |
| [`importResource`](Resources.md#importresource) | [Resources](Resources.md#resources) | [Resources](Resources.md) | 外部のリソースを図面に取り込みます。 |

<a id="index-l"></a>

### 索引 L

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`listConnectCADConnectors`](ObjectsConnectCAD.md#listconnectcadconnectors) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCADのConnector Typeとそのピンの一覧を返します。 |
| [`listConnectCADSignals`](ObjectsConnectCAD.md#listconnectcadsignals) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCADのSignal Typeの一覧を返します。 |
| [`listGDTFs`](ObjectsSpotlight.md#listgdtfs) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | 使用可能なGDTF器具タイプとそのDMXモードの一覧を返します。 |
| [`listIFCCustomPsets`](IFC.md#listifccustompsets) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | ファイルのカスタムIFCプロパティセット定義を一覧表示します。 |
| [`listIFCMappingObjects`](IFC.md#listifcmappingobjects) | [IFC Data Mapping](IFC.md#ifc-data-mapping) | [IFC](IFC.md) | アクティブなデータマネージャのマッピングの、マッピングオブジェクトを一覧表示します。 |
| [`listIFCPsets`](IFC.md#listifcpsets) | [IFC](IFC.md#ifc) | [IFC](IFC.md) | IFCエンティティタイプに適用できるIFCプロパティセットを一覧表示します。 |
| [`listScripts`](Scripting.md#listscripts) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | ファイルのスクリプトリソースを一覧表示します。 |
| [`listToolGroups`](Common.md#listtoolgroups) | [Core](Common.md#core-group) | [Common](Common.md) | 有効、無効を問わずすべてのツールグループを、有効状態と、必要に応じてそのツールとともに一覧表示します。 |

<a id="index-p"></a>

### 索引 P

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`pressOIPButton`](OIPAccess.md#pressoipbutton) | [Object Info](OIPAccess.md#object-info) | [OIPAccess](OIPAccess.md) | オブジェクト情報パレットのボタンを押します。 |

<a id="index-q"></a>

### 索引 Q

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`queryGeometry`](ObjectPrimitives.md#querygeometry) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 2Dプリミティブの最近点、距離、包含、交差、接線、および曲線に沿った測定に関する幾何学的な問い合わせに応答します。 |

<a id="index-r"></a>

### 索引 R

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`runMenuCommand`](MenuAccess.md#runmenucommand) | [Menus](MenuAccess.md#menus) | [MenuAccess](MenuAccess.md) | ユーザーが選択した場合と同じように、メニューコマンドまたはチャンクメニュー項目を実行します。 |
| [`runPythonScript`](Scripting.md#runpythonscript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Vectorworks内でPythonコードを実行します。 |
| [`runScript`](Scripting.md#runscript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | 保存済みのPythonスクリプトリソースを実行します。 |
| [`runToolBatch`](Common.md#runtoolbatch) | [Core](Common.md#core-group) | [Common](Common.md) | 複数のツール呼び出しを、全成功または全取り消しの1つの取り消しステップとして実行します。 |

<a id="index-s"></a>

### 索引 S

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`saveScript`](Scripting.md#savescript) | [Scripting](Scripting.md#scripting) | [Scripting](Scripting.md) | Pythonスクリプトリソースを実行せずに作成または更新します。 |
| [`selectObjects`](DocumentAccess.md#selectobjects) | [Selection](DocumentAccess.md#selection) | [DocumentAccess](DocumentAccess.md) | 検索条件やUUIDでオブジェクトを選択、選択解除するか、すべてを選択、選択解除します。 |
| [`sendToolAction`](ToolAccess.md#sendtoolaction) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | アクティブツールの操作を完了またはキャンセルするか、最後の点を削除します。 |
| [`sendToolPointer`](ToolAccess.md#sendtoolpointer) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | アクティブツールで図面内をクリック、ダブルクリック、ホバー、ドラッグします。 |
| [`setActiveContext`](DocumentAccess.md#setactivecontext) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | アクティブレイヤとクラス、およびその他のレイヤとクラスの表示方法を設定します。 |
| [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | データタグまたは図面枠を編集します。 |
| [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject) | [Architecture](ObjectsArchitect.md#architecture) | [ObjectsArchitect](ObjectsArchitect.md) | 壁、スラブ、屋根、ドア、窓、柱、階段を編集します。 |
| [`setConnectCADSocket`](ObjectsConnectCAD.md#setconnectcadsocket) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Socketを編集します。 |
| [`setDimension`](ObjectsAnnotation.md#setdimension) | [Dimensioning](ObjectsAnnotation.md#dimensioning) | [ObjectsAnnotation](ObjectsAnnotation.md) | 寸法線オブジェクトを編集します。 |
| [`setGeometry`](ObjectPrimitives.md#setgeometry) | [Draw2D](ObjectPrimitives.md#draw2d) | [ObjectPrimitives](ObjectPrimitives.md) | 2Dプリミティブの形状を編集します。 |
| [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject) | [Landmark](ObjectsLandmark.md#landmark) | [ObjectsLandmark](ObjectsLandmark.md) | 敷地またはランドスケープのオブジェクトを編集します。 |
| [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice) | [Spotlight](ObjectsSpotlight.md#spotlight) | [ObjectsSpotlight](ObjectsSpotlight.md) | Lighting Deviceを編集します。 |
| [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | 線、面、不透明度、マーカー、ドロップシャドウなど、オブジェクトのグラフィック属性を設定します。 |
| [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) | [Objects](ObjectPrimitives.md#objects) | [ObjectPrimitives](ObjectPrimitives.md) | プラグインオブジェクトの1つ以上のパラメータを書き込みます。 |
| [`setOIPValues`](OIPAccess.md#setoipvalues) | [Object Info](OIPAccess.md#object-info) | [OIPAccess](OIPAccess.md) | ユーザーと同じように、オブジェクト情報パレットのコントロールを設定します。 |
| [`setPreferences`](DocumentAccess.md#setpreferences) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | 1つのカテゴリのファイル設定を書き込みます。 |
| [`setProjectData`](ObjectsAnnotation.md#setprojectdata) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | ファイルの表題欄のプロジェクトデータを書き込みます。 |
| [`setResourceDetails`](Resources.md#setresourcedetails) | [Resources](Resources.md#resources) | [Resources](Resources.md) | リソースの内容を変更します。 |
| [`setToolMode`](ToolAccess.md#settoolmode) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | アクティブツールのモードを1つ変更します。 |
| [`setToolModes`](ToolAccess.md#settoolmodes) | [InteractiveTools](ToolAccess.md#interactivetools) | [ToolAccess](ToolAccess.md) | アクティブツールのモードを複数設定します。 |
| [`setUnits`](DocumentAccess.md#setunits) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | ファイルの主単位または補助単位の設定を変更します。 |
| [`setView`](DocumentAccess.md#setview) | [Document](DocumentAccess.md#document) | [DocumentAccess](DocumentAccess.md) | ビューの移動、ズームの設定、ユーザー原点の移動、用紙の再描画を行います。 |

<a id="index-t"></a>

### 索引 T

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`tagObject`](ObjectsAnnotation.md#tagobject) | [Annotation](ObjectsAnnotation.md#annotation) | [ObjectsAnnotation](ObjectsAnnotation.md) | データタグをオブジェクトに関連付けるか、関連付けを解除します。 |

<a id="index-v"></a>

### 索引 V

| ツール | グループ | ページ | 概要 |
|---|---|---|---|
| [`validateConnectCADDevice`](ObjectsConnectCAD.md#validateconnectcaddevice) | [ConnectCAD](ObjectsConnectCAD.md#connectcad) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | 何も作成せずにDevice記述データを検証します。 |

<a id="page-layout"></a>

## ページの構成

ツールフォルダの各ページは、次の共通の構成になっています。

1. **タイトル** — フォルダとその主題、サーバーとVectorworksのバージョン、およびこの一覧に戻るリンク。
2. **目次** — ページのすべてのグループとすべてのツール。
3. **概要** — グループごとに1行: グループID、初期状態で有効かどうか、安全性レベル、ツール数、1行の概要。
4. **グループ** — 各グループについて: グループID、有効状態と安全性レベル、概要、サーバーが報告する説明、および作用、安全性レベル、概要を含むツールの表。
5. **ツール** — 各ツールについて: 1行の概要、作用、安全性レベル、取り消しの動作、`runToolBatch`内で実行できるかどうか、サーバーが報告する**詳細**、および**パラメータ**表（名前、型、必須、説明）。オブジェクトパラメータのメンバーは`parameter.member`、配列項目のメンバーは`parameter[].member`として記載しています。判明している場合は、**結果**セクションに結果のキーを、**エラー**に失敗を記載し、**注**で説明に記載されていない動作を補足しています。

共通の形式は[Common](Common.md)と[Attributes](Attributes.md)にリンクしています。たとえば、[点](Common.md#points)、[色](Common.md#colors)、[マーカー](Attributes.md#line-end-markers)です。

<a id="statistics"></a>

## 統計

| ページ | グループ数 | ツール数 | パラメータ数 | 読み取り専用 | 編集 | 対話操作 | スクリプト実行 |
|---|---|---|---|---|---|---|---|
| [DocumentAccess](DocumentAccess.md) | 2 | 20 | 129 | 8 | 12 | 0 | 0 |
| [IFC](IFC.md) | 2 | 6 | 8 | 6 | 0 | 0 | 0 |
| [MenuAccess](MenuAccess.md) | 1 | 4 | 19 | 3 | 0 | 1 | 0 |
| [ObjectPrimitives](ObjectPrimitives.md) | 2 | 27 | 273 | 10 | 17 | 0 | 0 |
| [Objects3D](Objects3D.md) | 1 | 16 | 193 | 2 | 14 | 0 | 0 |
| [ObjectsAnnotation](ObjectsAnnotation.md) | 2 | 16 | 338 | 5 | 11 | 0 | 0 |
| [ObjectsArchitect](ObjectsArchitect.md) | 1 | 9 | 127 | 1 | 8 | 0 | 0 |
| [ObjectsConnectCAD](ObjectsConnectCAD.md) | 1 | 10 | 39 | 5 | 5 | 0 | 0 |
| [ObjectsLandmark](ObjectsLandmark.md) | 1 | 10 | 190 | 1 | 9 | 0 | 0 |
| [ObjectsSpotlight](ObjectsSpotlight.md) | 1 | 5 | 30 | 2 | 3 | 0 | 0 |
| [OIPAccess](OIPAccess.md) | 1 | 3 | 14 | 1 | 0 | 2 | 0 |
| [Resources](Resources.md) | 1 | 11 | 122 | 5 | 6 | 0 | 0 |
| [Scripting](Scripting.md) | 1 | 7 | 11 | 4 | 1 | 0 | 2 |
| [ToolAccess](ToolAccess.md) | 1 | 10 | 44 | 5 | 0 | 5 | 0 |
| **合計** | **18** | **154** | **1537** | **58** | **86** | **8** | **2** |

パラメータ数は、各ツールの最上位のパラメータの数です。オブジェクトパラメータのメンバーと配列項目のメンバー（`parameter.member`、`parameter[].member`）は数えていません。対話操作には、メニューコマンドのツールも含まれます。[Core](Common.md#core-group)グループは、常に利用できる3つのメタツール（読み取り専用の`listToolGroups`、セッション設定の`activateToolGroups`、バッチ編集の`runToolBatch`）と、5つの最上位のパラメータを追加します。
