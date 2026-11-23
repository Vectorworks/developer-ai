[English](../../MCP/v2027.2/DocumentAccess.md) • [Deutsch](../../MCP.de/v2027.2/DocumentAccess.md) • **日本語**

# DocumentAccess — ファイルと選択

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

アクティブな図面全体と現在の選択内容を扱うツールです。ファイルの概要、レイヤ、ストーリ、クラス、単位、ビュー、ファイル設定、および選択オブジェクトの一括編集を提供します。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [Document](#document)
  - [getDocumentInfo](#getdocumentinfo)
  - [getLayers](#getlayers)
  - [createLayer](#createlayer)
  - [editLayer](#editlayer)
  - [getStories](#getstories)
  - [createStory](#createstory)
  - [editStory](#editstory)
  - [getClasses](#getclasses)
  - [createClass](#createclass)
  - [editClass](#editclass)
  - [setActiveContext](#setactivecontext)
  - [getUnits](#getunits)
  - [setUnits](#setunits)
  - [convertUnits](#convertunits)
  - [setView](#setview)
  - [getPreferences](#getpreferences)
  - [setPreferences](#setpreferences)
- [Selection](#selection)
  - [getSelection](#getselection)
  - [selectObjects](#selectobjects)
  - [editSelection](#editselection)

<a id="overview"></a>

## 概要

このフォルダには2つのツールグループがあり、合計20個のツールを提供します。

| グループ | グループID | 初期状態で有効 | 安全性レベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [Document](#document) | `document` | はい | 低 | 17 | アクティブな図面を扱います: ファイルの概要、レイヤ、ストーリ、クラス、単位、ビュー、ファイル設定。 |
| [Selection](#selection) | `selection` | はい | 中 | 3 | 現在の選択内容を一覧表示し、移動、回転、拡大縮小、複製、グループ化、削除、クラス変更を一括で行います。 |

## Document

> **グループ:** `Document` · **グループID:** `document` · **初期状態で有効:** はい · **安全性レベル:** 低 · **ツール数:** 17

**アクティブな図面を扱います: ファイルの概要、レイヤ、ストーリ、クラス、単位、ビュー、ファイル設定。**

アクティブなVectorworks図面自体を調査、管理します。対象はファイルの概要、レイヤ、ストーリ、クラス、単位、ビュー、ファイル設定です。作業が図面のレイヤ、クラス、単位、アクティブなコンテキストに依存する場合は、getDocumentInfo、getLayers、getClassesで確認してください。結果はその時点の状態を読み取ったもので、自分またはユーザーの編集によって図面が変わるまで有効です。選択内容とアクティブレイヤは頻繁に変わります。

Vectorworks図面の構成:

- 1つのファイルが1つの図面です。すべてのものは、レイヤ（図面の内容）またはファイルのリソース一覧（再利用可能な定義。Resourcesグループを参照）のいずれかに存在します。
- レイヤはすべてのジオメトリを格納するコンテナです。デザインレイヤには実世界のモデル内容を格納します。座標はワールド単位で、縮尺（1:scale）は用紙単位（縮尺無視）のグラフィック、文字、線の太さを印刷したときの大きさだけを決めます。シートレイヤは印刷可能な用紙で、ビューポート（デザインレイヤのビューをクロップし縮尺を設定したもの）、図面枠、用紙上の注釈を格納します。一度にアクティブになるレイヤは1つだけで、新しいオブジェクトはそこに作成されます。
- ストーリは建物の階（BIM）です。それぞれ高さとレベルを持ちます。レベルは、ストーリの高さからのオフセットで定義される名前付きの高さ（`OK-FB`などのレベルタイプ）です。レベルには専用のデザインレイヤを持たせることができ、そのレイヤの高さはレベルに追従します。壁の上端と下端はレベルに連動します。BIMワークフローの順序は、ストーリ（getStories、createStory、editStory）→スタイル（Resourcesグループ）→ストーリのレイヤ上の建築要素（Architectureグループ）です。
- クラスは、レイヤを横断して使用する名前付きの保存済み属性セットです（線、面、線の太さ、不透明度、マーカー、ドロップシャドウ、テクスチャ、文字スタイル）。各オブジェクトは必ず1つのクラスに属します。オブジェクトの属性を「クラス属性を使用」に設定するとクラスに追従するため、クラスのスタイルを変更すると、そのクラスに従うすべてのオブジェクトのスタイルが変わります。クラスは表示状態も制御します。オブジェクトが描画されるのは、レイヤとクラスの両方が表示されている場合だけです。`None`クラスは常に存在します。
- オブジェクトはジオメトリです: 2D基本図形、パラメトリックなプラグインオブジェクト（壁、ドア、植栽、データタグなど）、グループ、シンボルインスタンス、ビューポート。それぞれ安定したuuid、クラス、グラフィック属性を持ち、プラグインオブジェクトにはパラメータレコードもあります。コンテナ（グループ、シンボル定義、ビューポート注釈）はオブジェクトを入れ子で格納します。新しいオブジェクトは現在編集中のコンテナに入り、getDocumentInfoはこれを`container`として返します。
- リソースは、ファイルに保存する再利用可能な定義です: シンボル定義、ハッチング、グラデーション、タイル、イメージ、ラインタイプ、テクスチャ、レコードフォーマット、ワークシート、文字スタイル、プラグインスタイル（オブジェクトスタイル）。オブジェクトはこれらを参照します。プラグインスタイルで制御されるプラグインオブジェクトは、そのスタイルからパラメータを取得します。
- 座標はワールド単位（APIが使用する内部の長さの単位）です。UIではファイルの単位に変換して表示します（convertUnitsを使用）。ユーザー原点は、ユーザーに(0,0)として見えるワールド上の点です。角度はラジアンで、X軸から反時計回りです。
- 取り消し: 図面を変更する各呼び出しは、ユーザーが取り消せる「MCP: &lt;tool&gt;」という1つの取り消しステップです（「編集 &gt; 取り消し」の後、Vectorworksのステータスメッセージに名前が表示されます）。失敗した呼び出しは何も変更しません（結果の`rolledBack`）。ユーザーの1つの作業を1つの取り消しステップにまとめるには、runPythonScriptの1回の実行で行います（Scriptingグループ）。

| ツール | 作用 | 安全性 | 概要 |
|---|---|---|---|
| [`getDocumentInfo`](#getdocumentinfo) | 読み取り専用 | 低 | アクティブファイルの概要として、ファイル、件数、用紙の境界、ビューの中心、ユーザー原点を返します。 |
| [`getLayers`](#getlayers) | 読み取り専用 | 低 | レイヤを、種類、表示状態、縮尺、高さ、オブジェクト数、境界と共に一覧表示します。 |
| [`createLayer`](#createlayer) | 編集 | 低 | デザインレイヤまたはシートレイヤを作成します。 |
| [`editLayer`](#editlayer) | 編集 | 低 | レイヤの名前、表示状態、縮尺、高さ、厚さなどのプロパティを変更します。 |
| [`getStories`](#getstories) | 読み取り専用 | 低 | ストーリ（建物の階）をレベルと共に、低い順で一覧表示します。 |
| [`createStory`](#createstory) | 編集 | 低 | 1つ以上のストーリをレベルと共に作成します。 |
| [`editStory`](#editstory) | 編集 | 低 | ストーリ、ファイルのレベルタイプ、またはストーリレベル初期設定を変更します。 |
| [`getClasses`](#getclasses) | 読み取り専用 | 低 | ファイルのクラスを一覧表示し、特別なクラスの名前を返します。 |
| [`createClass`](#createclass) | 編集 | 低 | クラスを作成するか、同名の既存クラスを返します。 |
| [`editClass`](#editclass) | 編集 | 低 | クラスの説明、表示状態、線、面、マーカー、ドロップシャドウなどを変更します。 |
| [`setActiveContext`](#setactivecontext) | 編集 | 低 | アクティブレイヤとクラス、およびその他のレイヤとクラスの表示方法を設定します。 |
| [`getUnits`](#getunits) | 読み取り専用 | 低 | ファイルの主単位と補助単位の設定を返します。 |
| [`setUnits`](#setunits) | 編集 | 低 | ファイルの主単位または補助単位の設定を変更します。 |
| [`convertUnits`](#convertunits) | 読み取り専用 | 低 | ワールド単位とファイルの単位の間で長さを変換します。 |
| [`setView`](#setview) | 編集 | 低 | ビューの移動、ズームの設定、ユーザー原点の移動、用紙の再描画を行います。 |
| [`getPreferences`](#getpreferences) | 読み取り専用 | 低 | ファイル設定の1つのカテゴリを読み取ります。 |
| [`setPreferences`](#setpreferences) | 編集 | 低 | 1つのカテゴリのファイル設定を書き込みます。 |

> **注:** このグループのツールの複数の呼び出しを、[`runToolBatch`](Common.md#runtoolbatch)で1つの取り消しステップにまとめることもできます（全成功または全取り消し）。

### getDocumentInfo

アクティブファイルの概要として、ファイル、件数、用紙の境界、ビューの中心、ユーザー原点を返します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

アクティブファイルの概要を返します: fileName（拡張子を含む）、filePath（OS形式の完全パス。未保存のファイルではnull）、選択／レイヤ／クラスの件数（selectionCountはアクティブレイヤだけでなく全レイヤが対象）、用紙の境界、ビューの中心、ユーザー原点、平面の回転、アクティブレイヤ（種類と縮尺を含む）、アクティブクラス、主単位、レイヤ／クラスの表示オプション、IFCの概要（IFCサポートが利用可能な場合の`hasIFCEntities`と`ifcSchema`）、新しいオブジェクトを作成する`container`（アクティブレイヤ、または編集中のグループ／シンボル定義）。

引数はありません。

> **注:** `container`は常に結果に含まれ、該当しないメンバーは省略されます。`default`は、新しいオブジェクトが入るコンテナ（アクティブレイヤ、または編集中のグループやシンボル定義）への[オブジェクト参照](Common.md#object-references)です。`insideGroup`はグループを編集中かどうかを示し、`editedGroup`はそのグループを参照します。`editedSymbolDefinition`はファイルの現在のシンボル（「シンボル」ツールが配置するシンボル定義）を参照します。Vectorworksはシンボル定義を編集していないときもこれを保持するため、新しいオブジェクトの作成先は`default`で確認してください。

**パラメータ**

このツールにパラメータはありません。

**結果**

| キー | 説明 |
|---|---|
| `isOpen` | 常に`true`。 |
| `fileName`、`filePath` | 拡張子を含むファイル名と、OS形式の完全パス。未保存のファイルでは`fileName`はその名前、`filePath`は`null`です。 |
| `selectionCount`、`layerCount`、`classCount` | 全レイヤの選択オブジェクト数、レイヤ数、クラス数（参照ファイルのクラスを含む）。 |
| `pageBounds` | 用紙の境界。ワールド単位の[矩形](Common.md#rectangles)です。 |
| `viewCenter`、`userOrigin` | ビューの中心とユーザー原点。ワールド単位の[点](Common.md#points)です。 |
| `activeLayer`、`activeLayerKind`、`activeLayerScale` | アクティブレイヤの名前、種類（[`getLayers`](#getlayers)の`kind`と同じ）、縮尺（1:scale）。 |
| `activeClass` | アクティブクラスの名前。 |
| `primaryUnits`、`unitsPerInch` | 主単位の名前と、1インチあたりの単位数。 |
| `planRotated`、`planRotationAngle` | 平面が回転しているかどうかと、平面の回転角度。 |
| `layerOptions`、`classOptions` | レイヤおよびクラスの表示オプション: `activeOnly`、`grayOthers`、`showOthers`、`showSnapOthers`、`showSnapModifyOthers`、`graySnapOthers`のいずれか。 |
| `hasIFCEntities`、`ifcSchema` | IFCサポートが利用可能な場合のみ。 |
| `container` | 上記の注を参照してください。 |

Vectorworksが読み取れない値は結果から省略されます。

### getLayers

レイヤを、種類、表示状態、縮尺、高さ、オブジェクト数、境界と共に一覧表示します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

図面のレイヤを、名前、uuid、種類（design、sheet、または他のファイルから参照するデザインレイヤのguestDesign）、表示状態、縮尺（1:scale）、高さ、厚さ、シートの説明、DPI、レンダリングモード、投影の方法、オブジェクト数、境界、アクティブレイヤかどうかと共に一覧表示します。オブジェクトツール（getObjectInfoなど）はレイヤを`uuid`で指定します。これらのツールの`name`はオブジェクトだけを検索し、レイヤ名は別の名前空間です。ストーリ内のデザインレイヤは、`story`（ストーリ名）と`levelType`（ストーリ内のレベル。レイヤはストーリに属さずにレベルタイプを持つこともあります）も返します。

オブジェクト数と境界は、各レイヤの最上位の図面オブジェクトを対象とし（削除済みオブジェクト用にVectorworksが保持する内部の項目は含めません）、そのすべてを走査するため、大きな図面では時間がかかります。可能なら呼び出しの対象を絞ってください。`activeOnly`はアクティブレイヤだけを返します。`visibleOnly`は非表示レイヤを除外します（グレイ表示レイヤは含みます）。`traverse`の"allObjects"（デフォルト）はすべてのオブジェクトを数え、"visibleObjects"はVectorworksが現在描画しているオブジェクト（表示レイヤかつ表示クラス）だけを数えます。そのため後者では、非表示レイヤのobjectCountは0になり、境界はありません。

応答には`traverse`、`visibleOnly`、`activeOnly`の値も含まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `activeOnly` | boolean |  | アクティブレイヤだけを返します。 |
| `visibleOnly` | boolean |  | 非表示レイヤを除外します（グレイ表示レイヤは含みます）。 |
| `traverse` | string |  | 次のいずれか: `allObjects`, `visibleObjects`。 |

**結果**

| キー | 説明 |
|---|---|
| `layers` | レイヤの一覧。各項目に`name`、`uuid`、`kind`、`active`、`visibility`（`visible`、`grayed`、`invisible`のいずれか）、`scale`、`elevation`、`thickness`、`story`と`levelType`（これらを持つデザインレイヤの場合）、`description`（シートレイヤで、空でない場合）、`dpi`（シートレイヤの場合）、`renderMode`、`projection`、`objectCount`、`bounds`（境界を求める対象がある場合のみ）が含まれます。 |
| `traverse`、`visibleOnly`、`activeOnly` | 呼び出しで使用した値。 |

エラー: `'activeOnly' must be true or false`（`visibleOnly`も同様）、`unknown 'traverse'; use allObjects | visibleObjects`。

### createLayer

デザインレイヤまたはシートレイヤを作成します。

> **作用:** 編集 · **安全性:** 低 · **取り消し:** 1ステップ「MCP: createLayer」 · **runToolBatch内:** はい

**詳細**

レイヤを作成し、getLayersと同じ形式で返します。`type`の"design"（デフォルト）は、ワールド座標のデザインレイヤを作成します。`scale`（1:scale、デフォルト1）と、ワールド単位の`elevation`および`thickness`（レイヤの壁の高さ）を指定できます。"sheet"は印刷可能なシートレイヤを作成し、これらの引数と`story`／`levelType`を拒否します。`story`（ストーリ名）と`levelType`を指定すると、新しいデザインレイヤをそのストーリのそのレベルのレイヤにします。レイヤのないレベルはそのレイヤを使い、存在しないレベルは、ストーリレベル初期設定にある同じタイプの最初のレベルのオフセット（なければ0）で追加されます。

ストーリ内のレイヤの高さはレベルに追従するため、`story`と`elevation`の併用は拒否されます。指定したオフセットのレベルを新しいレイヤと共に追加するには、editStoryの`addLevels`を使用してください。`story`なしの`levelType`は、ストーリ外でレイヤにレベルタイプを設定します。`activate`がtrueでなければアクティブレイヤは変わりません（新しいオブジェクトはアクティブレイヤに作成されます）。

引数が拒否されると呼び出しは失敗し、何も作成しません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string | はい | 新しいレイヤの名前。同じ名前のレイヤが既にある場合、Vectorworksは新しいレイヤに次の空いている名前（`<name>-2`など）を付けます。結果の`name`で確認してください。 |
| `type` | string |  | 次のいずれか: `design`, `sheet`。デフォルト: `design`。その他の値でもデザインレイヤを作成します。 |
| `scale` | number |  | デザインレイヤ: 1:scale、デフォルトは1。シートレイヤでは無視されますが、正の数である必要があります。 |
| `elevation` | number |  | 高さ（ワールド単位）。 |
| `thickness` | number |  | レイヤの壁の高さ。 |
| `story` | string |  | ストーリ名。 |
| `levelType` | string |  | `story`を指定した場合、新しいレイヤが使用するそのストーリのレベル。`story`を指定しない場合、ストーリ外のレベルタイプ。1～63文字。 |
| `activate` | boolean |  | デフォルト: `false`。 |

**結果**

新しいレイヤ（getLayersと同じ形式）に、次のキーが加わります:

| キー | 説明 |
|---|---|
| `created` | `true`。 |

エラー: `'name' is required`、`'scale' must be a positive number (1:scale)`、`'elevation' and 'thickness' must be numbers in world units, 'thickness' not negative`、`'activate' must be true or false`、`'elevation', 'thickness', 'story' and 'levelType' apply to design layers only`（シートレイヤの場合）、`'story' and 'levelType' must be strings`、`story not found: <name>`、`'levelType' must have 1 to 63 characters`、`a layer in a story needs a 'levelType'`、`level '<levelType>' of story '<story>' has the layer '<layer>' already`、`the elevation of a layer in a story follows its level: …`（`story`と`elevation`を併用した場合）、`failed to create layer`、`Vectorworks refused the 'thickness' of the new layer`（`'elevation'`と`'story' / 'levelType'`も同様）。拒否されると呼び出しは失敗し、新しいレイヤは再び削除されます（`rolledBack`）。

### editLayer

レイヤの名前、表示状態、縮尺、高さ、厚さなどのプロパティを変更します。

> **作用:** 編集 · **安全性:** 低 · **取り消し:** 1ステップ「MCP: editLayer」 · **runToolBatch内:** はい

**詳細**

`name`で指定したレイヤ（省略時はアクティブレイヤ）のプロパティを変更します。`newName`で名前を変更し、`visibility`（visible|grayed|invisible）、`scale`（デザインレイヤ、1:scale）、ワールド単位の`elevation`と`thickness`、シートレイヤの`description`（シートレイヤタイトル）と`dpi`を設定するか、`activate`でアクティブにします（それ以外ではアクティブレイヤは変わりません）。

**デザインレイヤ:** `story`（ストーリ名）は、レイヤをそのストーリのレベル`levelType`（デフォルトはレイヤ自身のレベルタイプ）のレイヤにし、レイヤはレベルの高さに移動します。`story`の""はレイヤをストーリから外します（高さは維持し、`levelType`で設定しない限りレベルタイプは失われます）。`levelType`だけを指定すると、ストーリ内のレイヤを同じストーリのそのレベルに移します（""はレベルタイプを解除します）。1つのレベルが持つレイヤは1つです。ストーリ内のレイヤの高さはレベルに追従するため、そのレイヤでは`elevation`は拒否されます。レベルのオフセットはeditStoryの`setLevels`で変更してください。ストーリ関連の引数を最初に適用し、拒否された場合は呼び出しが失敗して何も変更しません。更新したレイヤを、getLayersと同じ形式で`applied`と共に返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string |  | 省略時はアクティブレイヤ。 |
| `newName` | string |  | 新しい名前。 |
| `visibility` | string |  | 次のいずれか: `visible`, `grayed`, `invisible`。`normal`、`gray`、`hidden`も受け付けます。 |
| `scale` | number |  | デザインレイヤの縮尺、1:scale。 |
| `elevation` | number |  | 高さ（ワールド単位）。 |
| `thickness` | number |  | 厚さ（ワールド単位）。 |
| `description` | string |  | シートレイヤタイトル。 |
| `dpi` | integer |  | シートレイヤの解像度。 |
| `story` | string |  | ストーリ名。`""`はレイヤをストーリから外します。 |
| `levelType` | string |  | レイヤが使用するストーリのレベル（詳細を参照）。`""`はレベルタイプを解除します。それ以外は1～63文字。 |
| `activate` | boolean |  | 指定しなければアクティブレイヤは変わりません。 |

**結果**

更新したレイヤ（getLayersと同じ形式）に、次のキーが加わります:

| キー | 説明 |
|---|---|
| `applied` | 指定された各プロパティにつき1項目: `name`（`newName`に対応）、`visibility`、`scale`、`elevation`、`thickness`、`description`、`dpi`、`story`、`levelType`、および`true`の場合の`activate`（`activate`がfalseまたは省略の場合は項目を追加しません）。Vectorworksが値を受け付けた場合は`true`、拒否した場合（不明な`visibility`など）は`false`です。 |

エラー: `layer not found: <name>`、`'story' and 'levelType' must be strings`、`'story' and 'levelType' apply to design layers only`、`story not found: <name>`、`'levelType' must have 1 to 63 characters`、`a layer in a story needs a 'levelType'`、`level '<levelType>' of story '<story>' has the layer '<layer>' already`、`the elevation of a layer in a story follows its level`、`Vectorworks refused the 'story' / 'levelType' of layer '<name>'`。ストーリ関連の引数は何かを変更する前に確認されるため、これらのエラーではレイヤは元のままです。

### getStories

ストーリ（建物の階）をレベルと共に、低い順で一覧表示します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

図面のストーリ（建物の階）を高さの低い順に一覧表示します。各ストーリはname、uuid、index（その順序での1始まりの位置）、affix（ストーリレベル初期設定からVectorworksがストーリに作成するレイヤの名前の前記号または後記号）、isPrefix（レベルのレイヤ名からVectorworksが判定。どのレベルにもレイヤがなければtrue）、elevation、storyAbove／storyBelow（名前。最上階／最下階ではnull）、オフセット順のlevelsを返します。levelsは{ levelType, offset（ストーリの高さからの相対値）, elevation（ストーリの高さ + オフセット）, layerName（レベルのデザインレイヤ。レイヤのないレベルではnull）, layerUuid }です。

`includeLevelTypes`はファイルのレベルタイプ（オーガナイザダイアログ &gt; ストーリ &gt; レベルタイプ）を追加します。`includeDefaultLevels`は、ストーリレベルのテンプレートであるストーリレベル初期設定{ index, levelType, offset, layerName（前記号/後記号を除く）, scale, wallHeight }を追加します。長さはワールド単位です。createStoryとeditStoryではストーリを名前で指定します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `includeLevelTypes` | boolean |  | ファイルのレベルタイプを`levelTypes`として追加します。 |
| `includeDefaultLevels` | boolean |  | ストーリレベルのテンプレートを`defaultStoryLevels`として追加します。 |

**結果**

| キー | 説明 |
|---|---|
| `stories` | ストーリの一覧（低い順）。各項目に`name`、`uuid`、`index`、`affix`、`isPrefix`、`elevation`、`storyAbove`、`storyBelow`（名前。最上階と最下階では`null`）、`levels`が含まれます。 |
| `count` | ストーリの数。 |
| `levelTypes` | `includeLevelTypes`指定時のみ。ファイルのレベルタイプの名前。 |
| `defaultStoryLevels` | `includeDefaultLevels`指定時のみ。ストーリレベル初期設定。各項目（デフォルトのストーリレベル）に`index`、`levelType`、`offset`、`layerName`、`scale`、`wallHeight`が含まれます。 |

ストーリの各レベルには`levelType`、`offset`、`elevation`、`layerName`（レイヤのないレベルでは`null`）が含まれます。レイヤを持つレベルは`layerUuid`も返します。ファイルにもう存在しないレイヤをストーリがまだ参照している場合、そのレベルはその`layerName`を返し、`layerUuid`は返さず、`layerMissing`が`true`になります。

エラー: `'includeLevelTypes' must be true or false`（`includeDefaultLevels`も同様）。

### createStory

1つ以上のストーリをレベルと共に作成します。

> **作用:** 編集 · **安全性:** 低 · **取り消し:** 1ステップ「MCP: createStory」 · **runToolBatch内:** はい

**詳細**

1つのストーリ（最上位の`name`、`elevation`、省略可能な`affix`、`isPrefix`、`levels`）または複数のストーリ（`stories`: そのようなオブジェクトの配列）を1回の呼び出しで作成します。高さとオフセットはワールド単位です。各ストーリには固有の高さと固有の前記号/後記号が必要です（大文字小文字を区別せずに比較。デフォルトはストーリ名）。`levels`はレベルを追加します: { levelType, offset（ストーリの高さからの相対値）, layerName, createLayer, scale }。

`layerName`はレベルのデザインレイヤです。レベルタイプを持たない既存のデザインレイヤは、ストーリ内のレベルの高さに移動します。存在しないレイヤは、`scale`（1:scale。デフォルトはアクティブレイヤの縮尺）で作成されます（`createLayer`がfalseの場合を除く）。`layerName`がなければ、レベルはレイヤを持ちません。ファイルにないレベルタイプは、ファイルのレベルタイプに追加されます。

アクティブレイヤは変わりません。何かを作成する前にすべてのストーリとレベルを確認し、拒否があると呼び出しは失敗して何も作成しません（`rolledBack`）。`reuseExisting`（デフォルトfalse）を指定すると、既存のストーリはそのまま（高さ、前記号/後記号、レベル）保持され、不足しているレベルだけが追加されるため、同じ呼び出しを繰り返せます。各ストーリをgetStoriesと同じ形式で、`created`、`reused`、`levelsAdded`、`levelsKept`と共に返し、さらに`levelTypesAdded`と`layersCreated`を返します。

呼び出し全体が1つの取り消しステップです。

> **注:** 1つのストーリの引数（`name`、`elevation`、`affix`、`isPrefix`、`levels`）と`stories`のどちらか一方を指定し、両方は指定しないでください。レベルのレイヤは、まだレベルタイプを持たないデザインレイヤか、他のオブジェクトが使用していない名前である必要があります（後者の場合、`createLayer`がfalseでなければレイヤを作成します）。1つのレイヤを、呼び出し内の2つのレベルに割り当てることはできません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string |  | ストーリ名: 1～63文字で、他のオブジェクトが使用していない名前。 |
| `elevation` | number |  | 高さ（ワールド単位）。 |
| `affix` | string |  | 大文字小文字を区別せずに比較します。デフォルト: ストーリ名。 |
| `isPrefix` | boolean |  | `affix`がストーリのレイヤ名の前記号である場合は`true`。デフォルト: `false`（後記号）。 |
| `levels` | array of object |  | ストーリに追加するレベル。 |
| `levels[].levelType` | string | はい | 1～63文字。ファイルにないタイプは、ファイルのレベルタイプに追加されます。 |
| `levels[].offset` | number | はい | ストーリの高さからの相対値（ワールド単位）。 |
| `levels[].layerName` | string |  | レベルのデザインレイヤ。指定しない場合、レベルはレイヤを持ちません。 |
| `levels[].createLayer` | boolean |  | ファイルにその名前のレイヤがない場合に作成します。デフォルト: `true`。 |
| `levels[].scale` | number |  | 作成するレイヤの縮尺（1:scale）。デフォルト（または`0`）: アクティブレイヤの縮尺。 |
| `stories` | array of object |  | 複数のストーリ。各項目に1つのストーリの引数を指定します。 |
| `stories[].name` | string | はい | ストーリ名: 1～63文字で、他のオブジェクトが使用していない名前。 |
| `stories[].elevation` | number | はい | 高さ（ワールド単位）。 |
| `stories[].affix` | string |  | 大文字小文字を区別せずに比較します。デフォルト: ストーリ名。 |
| `stories[].isPrefix` | boolean |  | `affix`がストーリのレイヤ名の前記号である場合は`true`。デフォルト: `false`（後記号）。 |
| `stories[].levels` | array of object |  | ストーリに追加するレベル。 |
| `stories[].levels[].levelType` | string | はい | 1～63文字。ファイルにないタイプは、ファイルのレベルタイプに追加されます。 |
| `stories[].levels[].offset` | number | はい | ストーリの高さからの相対値（ワールド単位）。 |
| `stories[].levels[].layerName` | string |  | レベルのデザインレイヤ。指定しない場合、レベルはレイヤを持ちません。 |
| `stories[].levels[].createLayer` | boolean |  | ファイルにその名前のレイヤがない場合に作成します。デフォルト: `true`。 |
| `stories[].levels[].scale` | number |  | 作成するレイヤの縮尺（1:scale）。デフォルト（または`0`）: アクティブレイヤの縮尺。 |
| `reuseExisting` | boolean |  | デフォルト: `false`。 |

**結果**

| キー | 説明 |
|---|---|
| `stories` | 呼び出しで指定した各ストーリにつき1項目（getStoriesと同じ形式）。`created`と`reused`（真偽値）、`levelsAdded`（呼び出しがストーリに追加したレベルタイプ）、`levelsKept`（呼び出しで指定したレベルタイプのうち、再利用したストーリが既に持っていたもの）が加わります。 |
| `createdCount`、`reusedCount` | 呼び出しで作成したストーリ数と、`reuseExisting`で維持したストーリ数。 |
| `levelTypesAdded` | 呼び出しがファイルに追加したレベルタイプ。 |
| `layersCreated` | 呼び出しが作成したレイヤの名前。 |

エラー: `give either one story ('name', 'elevation', ...) or a 'stories' array`、`'stories' must be a non-empty array of stories`、`'reuseExisting' must be true or false`、`each story needs a 'name' of 1 to 63 characters`、`story '<name>': 'elevation' must be a number (world units)`、`story '<name>': 'affix' must be a string and 'isPrefix' true or false`、`story '<name>' is given twice`、`story '<name>' exists already; set 'reuseExisting' to keep it and add the levels it lacks`、`story '<name>': the name is used by another object`、`story '<name>': the story '<other>' has that elevation already`と前記号/後記号についての同様のエラー。レベルについては`each level needs a 'levelType' of 1 to 63 characters`、`story '<name>' level '<type>': 'offset' must be a number (world units, relative to the story elevation)`、`...: 'layerName' must be a string and 'createLayer' true or false`、`...: 'scale' must be a positive number (1:scale)`、`story '<name>': 'levels' must be an array of levels`、`the level type '<type>' is given twice`、およびそのレイヤの拒否（`is not a design layer`、`is the layer of the level '<type>' already`、`is the name of another object`、`does not exist and 'createLayer' is false`、`is given to another level, or deleted, in the same call`）。さらに`Vectorworks refused to create the story`または`Vectorworks refused the level '<type>'`。すべてのストーリとレベルを最初に確認し、拒否があると呼び出しは失敗して何も作成しません（`rolledBack`）。

### editStory

ストーリ、ファイルのレベルタイプ、またはストーリレベル初期設定を変更します。

> **作用:** 編集 · **安全性:** 低 · **取り消し:** 1ステップ「MCP: editStory」 · **runToolBatch内:** はい

**詳細**

ストーリ`name`、ファイルのレベルタイプ、またはストーリレベル初期設定を変更します。何かを変更する前に呼び出しのすべての変更を確認し、全体を1つの取り消しステップにします。拒否があると呼び出し全体が失敗し、何も変更しません（`rolledBack`）。長さはワールド単位です。ストーリへの変更は次の順で適用します: `affix`、`mode`と共に指定する`elevation`（modeはsingle（デフォルト。このストーリのみ）、currentAndAbove、currentAndBelow、all。移動するストーリはすべて同じ距離だけ移動し、2つのストーリが同じ高さになることはできません。移動するストーリのデザインレイヤと、そのレベルに連動するオブジェクトも一緒に移動します）、`removeLevels` [{ levelType, deleteLayer }]（レベルのレイヤは、ストーリもレベルタイプもないデザインレイヤとして残ります。`deleteLayer`で削除できますが、オブジェクトを含むレイヤでは拒否されます）、レベルをそのレイヤと共に移動する`setLevels` [{ levelType, offset }]、createStoryの`levels`と同じ形式の`addLevels`、そして呼び出しの他の変更の後に`newName`（IFCデータ内の名前も変更）。

`delete`をtrueにすると、単独の呼び出しでストーリを削除します。デザインレイヤはオブジェクトと共に、ストーリもレベルタイプもないレイヤとして残ります。`deleteLayers`で削除することもできますが、すべてが空でなければ拒否されます。`name`を省略した場合: `levelTypes` { add: [names], rename: [{ from, to }], delete: [names] }。ストーリレベルのレベルタイプは削除できません（削除したレベルタイプは、レイヤとデフォルトのストーリレベルから外れます）。また、レベルタイプの名前変更を取り消しても、壁の上端／下端の設定に使われた名前は復元されません（代わりに名前を元に戻してください）。`defaultStoryLevels` { reset: replace|append（Vectorworksのデフォルト）, delete: [index]（getStoriesの`includeDefaultLevels`が返すインデックス）, add: [{ levelType, offset, layerName, scale, wallHeight }]（指定順にリストの先頭へ追加）}。

ストーリをgetStoriesと同じ形式で、`applied`、`levelTypesAdded`、`layersCreated`と共に返します。`levelTypes`／`defaultStoryLevels`を変更した場合はそれらも返します。

> **注:** `name`を省略すると、レベルタイプとストーリレベル初期設定だけを変更します。変更は次の順で適用します: `levelTypes.add`、ストーリの変更（または`delete`）、`defaultStoryLevels`、`levelTypes.delete`、`newName`、最後に`levelTypes.rename`。`mode`には`elevation`が必要です。`defaultStoryLevels`には`reset`と`delete`のどちらか一方を指定し、両方は指定できません。`replace`は既存のデフォルトのストーリレベルを削除してからVectorworksのデフォルトを復元し、`append`は既存のものを保持します。`removeLevels`の項目は、レベルタイプの文字列だけでも指定できます。レイヤの削除（`deleteLayers`、`removeLevels[].deleteLayer`）は、ファイルのすべてのデザインレイヤが削除される場合も拒否されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string |  | 変更するストーリ。省略すると`levelTypes`と`defaultStoryLevels`だけを変更します。 |
| `newName` | string |  | IFCデータ内の名前も変更します。1～63文字で、他のオブジェクトの名前ではないもの。 |
| `affix` | string |  | ストーリの新しい前記号/後記号。 |
| `elevation` | number |  | 高さ（ワールド単位）。2つのストーリが同じ高さになることはできません。 |
| `mode` | string |  | 次のいずれか: `single`, `currentAndAbove`, `currentAndBelow`, `all`。デフォルト: `single`。`elevation`が必要です。 |
| `removeLevels` | array of object |  | ストーリから削除するレベル。 |
| `removeLevels[].levelType` | string | はい | ストーリのレベルのレベルタイプ。 |
| `removeLevels[].deleteLayer` | boolean |  | レベルのレイヤも削除します。オブジェクトを含むレイヤでは拒否されます。デフォルト: レイヤは残ります。 |
| `setLevels` | array of object |  | レイヤと共に移動するレベル。 |
| `setLevels[].levelType` | string | はい | ストーリのレベルのレベルタイプ。 |
| `setLevels[].offset` | number | はい | ストーリの高さからの新しいオフセット（ワールド単位）。 |
| `addLevels` | array of object |  | 追加するレベル。createStoryの`levels`と同じ形式です。 |
| `addLevels[].levelType` | string | はい | 1～63文字。ストーリがまだそのレベルを持っていない必要があります（既存のレベルは`setLevels`で移動します）。 |
| `addLevels[].offset` | number | はい | ストーリの高さからの相対値（ワールド単位）。 |
| `addLevels[].layerName` | string |  | レベルのデザインレイヤ。指定しない場合、レベルはレイヤを持ちません。 |
| `addLevels[].createLayer` | boolean |  | ファイルにその名前のレイヤがない場合に作成します。デフォルト: `true`。 |
| `addLevels[].scale` | number |  | 作成するレイヤの縮尺（1:scale）。デフォルト（または`0`）: アクティブレイヤの縮尺。 |
| `delete` | boolean |  | `true`でストーリを削除します。 |
| `deleteLayers` | boolean |  | `delete`と併用: ストーリのデザインレイヤも削除します。すべてが空でなければ拒否されます。 |
| `levelTypes` | object |  | ファイルのレベルタイプの変更: `add`、`rename`、`delete`。 |
| `levelTypes.add` | array of string |  | 追加するレベルタイプの名前（各1～63文字）。 |
| `levelTypes.rename` | array of object |  | 名前を変更するレベルタイプ。 |
| `levelTypes.rename[].from` | string | はい | 現在の名前。 |
| `levelTypes.rename[].to` | string | はい | 新しい名前（1～63文字）。 |
| `levelTypes.delete` | array of string |  | 削除するレベルタイプの名前。ストーリレベルのレベルタイプは削除できません。 |
| `defaultStoryLevels` | object |  | ストーリレベル初期設定の変更: `reset`または`delete`、および`add`。 |
| `defaultStoryLevels.reset` | string |  | 次のいずれか: `replace`, `append`。 |
| `defaultStoryLevels.delete` | array of integer |  | 削除するデフォルトのストーリレベルのインデックス（getStoriesの`includeDefaultLevels`が返す値）。 |
| `defaultStoryLevels.add` | array of object |  | 追加するデフォルトのストーリレベル。指定順にリストの先頭へ追加します。 |
| `defaultStoryLevels.add[].levelType` | string | はい | レベルタイプ。 |
| `defaultStoryLevels.add[].offset` | number | はい | ストーリの高さからの相対値（ワールド単位）。 |
| `defaultStoryLevels.add[].layerName` | string |  | レベルのレイヤ名。 |
| `defaultStoryLevels.add[].scale` | number |  | レイヤの縮尺（1:scale）。デフォルト: `0`（アクティブレイヤの縮尺）。負の値は不可。 |
| `defaultStoryLevels.add[].wallHeight` | number |  | レベルの壁の高さ（ワールド単位）。デフォルト: `0`。負の値は不可。 |

**結果**

| キー | 説明 |
|---|---|
| `story` | 変更後のストーリ（getStoriesと同じ形式）。呼び出しがストーリを変更した場合のみ。 |
| `applied` | `story`がある場合のみ。呼び出しで指定したストーリの変更ごとに1項目: `affix`、`elevation`、`newName`は`true`、`removeLevels`、`setLevels`、`addLevels`は、呼び出しが削除、移動、追加したレベルタイプの配列です。 |
| `levelTypesAdded` | 呼び出しがファイルに追加したレベルタイプの名前（ない場合は空の配列）。 |
| `layersCreated` | 呼び出しが作成したレイヤの名前（ない場合は空の配列）。 |
| `levelTypes` | 呼び出しに`levelTypes`がある場合のみ。変更後のファイルのすべてのレベルタイプの名前。 |
| `defaultStoryLevels` | 呼び出しに`defaultStoryLevels`がある場合のみ。変更後のストーリレベル初期設定（getStoriesの`includeDefaultLevels`と同じ形式）。 |
| `deleted` | `delete`の場合のみ。`true`。この場合`story`と`applied`はありません。 |
| `layersDeleted`、`layersKept` | `delete`の場合のみ。ストーリのデザインレイヤの名前。`deleteLayers`で削除したもの、または（ストーリもレベルタイプもないレイヤとして）残したもの。 |

エラー: `nothing to change: give changes of the story 'name', 'levelTypes' or 'defaultStoryLevels'`、`'delete' deletes the story in a call of its own: leave out the other changes`、`'name' (the story to change) is required for 'newName', 'affix', 'elevation', the level changes and 'delete'`、`story not found: <name>`、`story '<name>': 'elevation' must be a number (world units), and 'mode' (single, currentAndAbove, currentAndBelow or all) goes with it`、`story '<name>': 'delete' and 'deleteLayers' are true or false, and 'deleteLayers' goes with 'delete'`、`'defaultStoryLevels' takes 'reset' or 'delete', not both`、`each item of 'defaultStoryLevels.add' is { levelType, offset, layerName, scale, wallHeight }: lengths in world units, 'scale' and 'wallHeight' not negative`、`story '<name>': 'newName' must have 1 to 63 characters and must not be the name of another object`、`story '<name>': another story has the affix '<affix>' (affixes are compared ignoring case)`、`story '<name>': its layer '<layer>' holds <n> objects, and only empty layers are deleted; leave out 'deleteLayers' to keep the layers`、`story '<name>': its layers are all the design layers of the document, and Vectorworks keeps at least one`、`story '<name>': the 'elevation' would move a story onto the elevation of a story that does not move ('mode'); two stories cannot share an elevation`、`story '<name>' has no level '<type>' to remove, or it is removed twice`、`story '<name>' level '<type>': its layer '<layer>' holds <n> objects, and only an empty layer is deleted; leave out 'deleteLayer' to keep the layer`、`story '<name>' level '<type>': deleting its layer would delete the last design layer of the document`、`story '<name>' has no level '<type>' to move, or 'removeLevels' removes it, or it is moved twice`、`story '<name>' has the level '<type>' already (move it with 'setLevels')`、`the level type '<type>' exists already, or is given twice`、`the level type '<from>' cannot be renamed to '<to>': it must exist, the new name must not (a change of the letter case only is not possible), and each is changed once`、`the level type '<from>' is renamed in a call of its own: other changes of this call use it`、`the level type '<name>' cannot be deleted: it must exist and not be used by the other changes of the call`、`the level type '<name>' is a level of the story '<story>': remove the level first ('removeLevels')`、`'defaultStoryLevels.delete': there is no default story level <index>, or it is given twice`、およびVectorworksによる拒否（`Vectorworks refused to remove the level '<type>'`、`Vectorworks refused to delete the level type '<name>'`など）。すべての変更を最初に確認し、拒否があると呼び出しは失敗して何も変更しません（`rolledBack`）。

### getClasses

ファイルのクラスを一覧表示し、特別なクラスの名前を返します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

ファイルのクラス（オブジェクトが属性を継承する名前付き属性セット）を、名前、インデックス、表示状態と共に一覧表示し、さらに`specialClasses`を返します: `none`クラス、組み込みの`dimension`クラス、現在のコンテナの`default`クラス（通常はアクティブクラス）の名前です。createClassの`guides`は「補助グリッド」クラスを返します。`detailed`を指定すると、各クラスの説明、「非出力」と「属性を使う」のフラグ、線（RGB色とカラーテーブルのインデックス、lineWeightMils、opacity、元のstyle値、styleKind、lineType）、面（RGB色とカラーテーブルのインデックス、type、元のstyle値、resource、opacity）、マーカー、ドロップシャドウ、テクスチャ（`texture`、`wallTextures`のright/left/center、`roofTextures`のtop/edge/dormer）、文字スタイルも返します。

`includeGuestClasses`を指定すると、他のファイルから参照するクラスも含めます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `includeGuestClasses` | boolean |  | ゲストクラス（他のファイルから参照されているクラス）も含めます。 |
| `detailed` | boolean |  | 各クラスの属性を追加します（結果を参照）。 |

**結果**

| キー | 説明 |
|---|---|
| `classes` | ファイルのクラス。各項目に`name`、`index`、`visibility`が含まれ、`detailed`指定時は下記のキーも含まれます。 |
| `classOptions` | アクティブクラス以外のクラスの表示方法。setActiveContextの`classOptions`の名前のいずれかです。読み取れない場合は省略されます。 |
| `specialClasses` | 特別なクラスの名前: `none`、`dimension`、`default`。 |

`detailed`を指定すると、各クラスには次のキーも含まれます: `description`（空でない場合のみ）、`nonPlot`、`useAtCreation`、`pen`（`foreColor`、`backColor`、`foreColorIndex`、`backColorIndex`、`lineWeightMils`、`opacity`、`style`、`styleKind`、`lineType`）、`fill`（`foreColor`、`backColor`、`foreColorIndex`、`backColorIndex`、`type`、`style`、`resource`、`opacity`）、`beginningMarker`、`endMarker`（[Attributes](Attributes.md#line-end-markers)で説明している形式。クラスのマーカーは常に`visible`が`true`です）、`dropShadow`（[ドロップシャドウ](Attributes.md#drop-shadow)）、`useTextures`、`texture`、`wallTextures`（`right`、`left`、`center`）、`roofTextures`（`top`、`edge`、`dormer`）、`useTextStyle`、`textStyle`。テクスチャの値はテクスチャのインデックスです（0 = なし）。`textStyle`は文字スタイルリソースの内部インデックスです（0 = なし）。読み取れない値は省略されます。

### createClass

クラスを作成するか、同名の既存クラスを返します。

> **作用:** 編集 · **安全性:** 低 · **取り消し:** 1ステップ「MCP: createClass」 · **runToolBatch内:** はい

**詳細**

クラスを作成します。その名前が既に使われている場合は既存のクラスを返します。`name`の代わりに`guides`を指定すると「補助グリッド」クラス（補助グリッド図形のクラス。なければ作成）を取得します。`description`は省略可能です。`activate`を指定するとアクティブクラスになり、新しいオブジェクトはそのクラスに作成されます。クラス名とインデックスを返します。

> **注:** `guides`が`true`の場合、`name`は使用されません。`description`と`activate`は既存のクラスにも適用されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string |  | クラス名。`guides`が`true`の場合を除き必須です。 |
| `guides` | boolean |  | `true`: `name`のクラスの代わりに「補助グリッド」クラスを返します。 |
| `description` | string |  | 説明文。 |
| `activate` | boolean |  | クラスをアクティブクラスにします。 |

**結果**

| キー | 説明 |
|---|---|
| `created` | クラスが既に存在していた場合も含め、常に`true`。存在するかどうかは、先にgetClassesで確認してください。 |
| `name` | クラスの名前。 |
| `index` | クラスの内部インデックス。読み取れない場合は省略されます。 |

エラー: `'name' is required (or set 'guides')`、`failed to create class`。

### editClass

クラスの説明、表示状態、線、面、マーカー、ドロップシャドウなどを変更します。

> **作用:** 編集 · **安全性:** 低 · **取り消し:** 1ステップ「MCP: editClass」 · **runToolBatch内:** はい

**詳細**

`name`で指定したクラス（省略時はアクティブクラス）を変更します。`description`、`visibility`（visible|grayed|invisible）、`nonPlot`、`useAtCreation`、クラスの`pen`（foreColor、backColor、foreColorIndex、backColorIndex、lineWeightMils、opacity、style、lineType）、`fill`（foreColor、backColor、foreColorIndex、backColorIndex、opacity、style、resource）、共通の`opacity`、`beginningMarker`／`endMarker`、`dropShadow`、`useTextures`／`texture`、`wallTextures`（right、left、center）、`roofTextures`（top、edge、dormer）、`useTextStyle`／`textStyle`を設定するか、`activate`でアクティブにします。

色のインデックスはファイルのカラーテーブルのインデックスです。クラスの現在の値と同じインデックスは無視されるため、getClassesで読み取ったクラスのRGB色を編集してそのまま送り返せます。両方の形式が変わる場合はインデックスが優先されます。テクスチャの各部はテクスチャのインデックスです（0 = なし）。マーカー、ドロップシャドウ、テクスチャの各部のオブジェクトは部分指定でき、省略したメンバーは値を維持します。

`action`の"delete"はクラスを削除し、そのオブジェクトをNoneに移動します。属性が「クラス属性を使用」に設定されたオブジェクトは、これらの値に追従します。

> **注:** クラスのマーカーには`visible`フラグがありません。常に`visible`が`true`として返され、`beginningMarker`または`endMarker`の`visible`メンバーは無視されます。`textStyle`は文字スタイルリソースの内部インデックス（0 = なし）で、名前ではありません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string |  | 省略時はアクティブクラス。 |
| `action` | string |  | 次のいずれか: `modify`, `delete`。 |
| `description` | string |  | 説明文。 |
| `visibility` | string |  | 次のいずれか: `visible`, `grayed`, `invisible`。 |
| `nonPlot` | boolean |  | クラスのオブジェクトを印刷しません（「非出力」）。 |
| `useAtCreation` | boolean |  | クラスに作成したオブジェクトは、作成時にクラスの属性を使います（「属性を使う」）。 |
| `pen` | object |  | 線の属性。指定したメンバーだけを変更します。 |
| `pen.foreColor` | [色](Common.md#colors) |  | 前景色（RGB）。 |
| `pen.backColor` | [色](Common.md#colors) |  | 背景色（RGB）。 |
| `pen.foreColorIndex` | integer |  | ファイルのカラーテーブルのインデックスで指定する前景色。 |
| `pen.backColorIndex` | integer |  | ファイルのカラーテーブルのインデックスで指定する背景色。 |
| `pen.lineWeightMils` | integer |  | 線の太さ（ミル単位）。 |
| `pen.opacity` | integer |  | 不透明度。0～100。 |
| `pen.style` | integer |  | 線のスタイルの元の値。 |
| `pen.lineType` | integer |  | ラインタイプの内部インデックス。 |
| `fill` | object |  | 面の属性。指定したメンバーだけを変更します。 |
| `fill.foreColor` | [色](Common.md#colors) |  | 前景色（RGB）。 |
| `fill.backColor` | [色](Common.md#colors) |  | 背景色（RGB）。 |
| `fill.foreColorIndex` | integer |  | ファイルのカラーテーブルのインデックスで指定する前景色。 |
| `fill.backColorIndex` | integer |  | ファイルのカラーテーブルのインデックスで指定する背景色。 |
| `fill.opacity` | integer |  | 不透明度。0～100。 |
| `fill.style` | integer |  | 面のスタイルの元の値。 |
| `fill.resource` | integer |  | ハッチング、タイル、グラデーション、イメージの内部インデックス。 |
| `opacity` | integer |  | 不透明度。0～100。 |
| `beginningMarker` | [マーカー](Attributes.md#line-end-markers) |  | クラスの始点マーカー。省略したメンバーは値を維持します。 |
| `endMarker` | [マーカー](Attributes.md#line-end-markers) |  | クラスの終点マーカー。省略したメンバーは値を維持します。 |
| `dropShadow` | [ドロップシャドウ](Attributes.md#drop-shadow) |  | クラスのドロップシャドウ。省略したメンバーは値を維持します。 |
| `useTextures` | boolean |  | クラスのテクスチャを使用します。 |
| `texture` | integer |  | テクスチャのインデックス。0はなし。 |
| `wallTextures` | object |  | メンバー: `right`, `left`, `center`。 |
| `wallTextures.right` | integer |  | 壁の右側のテクスチャのインデックス。0はなし。 |
| `wallTextures.left` | integer |  | 壁の左側のテクスチャのインデックス。0はなし。 |
| `wallTextures.center` | integer |  | 壁の中央のテクスチャのインデックス。0はなし。 |
| `roofTextures` | object |  | メンバー: `top`, `edge`, `dormer`。 |
| `roofTextures.top` | integer |  | 屋根の上面のテクスチャのインデックス。0はなし。 |
| `roofTextures.edge` | integer |  | 屋根の縁のテクスチャのインデックス。0はなし。 |
| `roofTextures.dormer` | integer |  | 屋根のドーマーのテクスチャのインデックス。0はなし。 |
| `useTextStyle` | boolean |  | クラスの文字スタイルを使用します。 |
| `textStyle` | integer |  | 文字スタイルリソースの内部インデックス（getClassesが`detailed`で返す値）。0はなし。 |
| `activate` | boolean |  | クラスをアクティブクラスにします。 |

**結果**

`action`が`delete`の場合、結果は`deleted`です: クラスを削除した場合は`true`。

それ以外の場合は、getClassesが`detailed`で返す形式のクラスに、次のキーが加わります:

| キー | 説明 |
|---|---|
| `applied` | 指定された設定ごとに1項目。Vectorworksが設定を受け付けた場合は`true`です。キーは`description`、`visibility`、`nonPlot`、`useAtCreation`、`opacity`、`useTextures`、`texture`、`wallTextures`、`roofTextures`（値がオブジェクトでない場合は`false`）、`useTextStyle`、`textStyle`、`beginningMarker`、`endMarker`、`dropShadow`、`activate`（`true`の場合のみ記載）、および線と面についての`penForeColor`、`penBackColor`、`lineWeightMils`、`penOpacity`、`penStyle`、`penLineType`、`penColorIndices`、`fillForeColor`、`fillBackColor`、`fillOpacity`、`fillStyle`、`fillResource`、`fillColorIndices`です。 |

エラー: `class not found: <name>`（`name`を省略し、アクティブクラスが有効でない場合も）。

### setActiveContext

アクティブレイヤとクラス、およびその他のレイヤとクラスの表示方法を設定します。

> **作用:** 編集 · **安全性:** 低 · **取り消し:** 1ステップ「MCP: setActiveContext」 · **runToolBatch内:** はい

**詳細**

新しいオブジェクトが継承する設定と、ユーザーが作業できる対象を設定します: アクティブな`layer`と`class`の一方または両方を名前で指定し、`layerOptions`／`classOptions`（activeOnly、grayOthers、showOthers、showSnapOthers、showSnapModifyOthers、graySnapOthers）で非アクティブのレイヤとクラスの表示方法を指定し、`symbolDefinition`で編集するシンボル定義を指定します。

> **注:** `symbolDefinition`は現在のシンボル定義を設定します。定義を編集用に開くわけではありません。シンボル定義でない名前を指定しても呼び出しは失敗せず、`symbolDefinitionActivated`が`false`になります。引数は`layer`、`class`、`layerOptions`、`classOptions`、`symbolDefinition`の順に確認され、文字列の値だけが有効です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `layer` | string |  | アクティブにするレイヤの名前。 |
| `class` | string |  | アクティブにするクラスの名前。 |
| `layerOptions` | string |  | 次のいずれか: `activeOnly`, `grayOthers`, `showOthers`, `showSnapOthers`, `showSnapModifyOthers`, `graySnapOthers`。 |
| `classOptions` | string |  | 次のいずれか: `activeOnly`, `grayOthers`, `showOthers`, `showSnapOthers`, `showSnapModifyOthers`, `graySnapOthers`。 |
| `symbolDefinition` | string |  | 現在のシンボル定義にするシンボル定義の名前。 |

**結果**

指定した引数ごとに1つのキー:

| キー | 説明 |
|---|---|
| `layerActivated` | レイヤがアクティブになった場合は`true`。 |
| `classActivated` | クラスがアクティブになった場合は`true`。 |
| `layerOptions` | Vectorworksがオプションを受け付けた場合は`true`。不明なオプション名の場合は`false`。 |
| `classOptions` | Vectorworksがオプションを受け付けた場合は`true`。不明なオプション名の場合は`false`。 |
| `symbolDefinitionActivated` | シンボル定義が現在のシンボル定義になった場合は`true`。名前がシンボル定義でない場合は`false`。 |

エラー: `layer not found: <name>`、`class not found: <name>`、`symbol definition not found: <name>`、`provide 'layer', 'class', 'layerOptions', 'classOptions' and/or 'symbolDefinition'`。エラーが発生すると呼び出しは失敗し、Vectorworksはそれまでに呼び出しが行った変更を元に戻します（`rolledBack`）。

### getUnits

ファイルの主単位と補助単位の設定を返します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

ファイルの主単位と補助単位のすべての設定を返します: 名前、単位記号、1インチあたりの単位数、メートル系かどうかのフラグ、表示／寸法の精度、分数と区切り記号のオプション、角度の単位、および（主単位のみ）面積と体積の単位とファイルの角度設定。引数はありません。

**パラメータ**

このツールにパラメータはありません。

**結果**

| キー | 説明 |
|---|---|
| `primary` | 主単位の設定。 |
| `secondary` | 補助単位の設定。 |

どちらにも`name`、`mark`、`unitsPerInch`、`style`、`metric`、`showUnitMark`、`leadingZero`、`trailingZeros`、`displayAsFraction`、`showThousandsSeparator`、`decimalDisplayPrecision`、`decimalDimensionPrecision`、`fractionalDisplayPrecision`、`fractionalDimensionPrecision`、`angularUnit`（`degrees`、`radians`、`gradians`のいずれか）のキーがあります。主単位にはさらに`worldUnitsPerUnit`、`squareUnitDivision`、`squareUnitMark`、`areaUnitName`、`areaUnitMark`、`areaUnitsPerSquareInch`、`areaDecimalPrecision`、`volumeUnitName`、`volumeUnitMark`、`volumeUnitsPerCubicInch`、`volumeDecimalPrecision`、`documentAngularUnit`、`documentAngularPrecision`があります。読み取れない値は省略されます。

### setUnits

ファイルの主単位または補助単位の設定を変更します。

> **作用:** 編集 · **安全性:** 低 · **取り消し:** 1ステップ「MCP: setUnits」 · **runToolBatch内:** はい

**詳細**

ファイルの単位を変更します。`which`で"primary"（デフォルト）または"secondary"を選択します。`name`、`mark`、`unitsPerInch`、`style`、`metric`、`showUnitMark`、`leadingZero`、`trailingZeros`、`displayAsFraction`、`showThousandsSeparator`、小数／分数の表示精度と寸法精度、`angularUnit`（degrees|radians|gradians）、および主単位では平方／面積／体積の単位の名前、記号、換算係数、精度と`documentAngularUnit`、`documentAngularPrecision`の任意の項目を設定できます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `which` | string |  | 次のいずれか: `primary`, `secondary`。デフォルト: `primary`。 |
| `name` | string |  | 単位の名前。 |
| `mark` | string |  | 値の後に表示する単位記号。 |
| `unitsPerInch` | number |  | 1インチに相当する単位の数。 |
| `style` | integer |  | getUnitsが返す、単位のスタイルコード。 |
| `metric` | boolean |  | メートル系の単位では`true`。 |
| `showUnitMark` | boolean |  | 値の後に単位記号を表示します。 |
| `leadingZero` | boolean |  | 1未満の値に整数部の0を表示します（「整数部の0を表示」）。 |
| `trailingZeros` | boolean |  | 末尾の0を表示します（「有効桁分0を表示」）。 |
| `displayAsFraction` | boolean |  | 値を分数で表示します。 |
| `showThousandsSeparator` | boolean |  | 3桁位取りを表示します。 |
| `decimalDisplayPrecision` | integer |  | 表示値の小数点以下の桁数。 |
| `decimalDimensionPrecision` | integer |  | 寸法値の小数点以下の桁数。 |
| `fractionalDisplayPrecision` | integer |  | 表示値の分数の精度。 |
| `fractionalDimensionPrecision` | integer |  | 寸法値の分数の精度。 |
| `angularUnit` | string |  | 次のいずれか: `degrees`, `radians`, `gradians`。 |
| `squareUnitDivision` | integer |  | 主単位のみ。平方単位の除数。 |
| `squareUnitMark` | string |  | 主単位のみ。平方単位の記号。 |
| `areaUnitName` | string |  | 主単位のみ。面積単位の名前。 |
| `areaUnitMark` | string |  | 主単位のみ。面積単位の記号。 |
| `areaUnitsPerSquareInch` | number |  | 主単位のみ。1平方インチに相当する面積単位の数。 |
| `areaDecimalPrecision` | integer |  | 主単位のみ。面積の小数点以下の桁数。 |
| `volumeUnitName` | string |  | 主単位のみ。体積単位の名前。 |
| `volumeUnitMark` | string |  | 主単位のみ。体積単位の記号。 |
| `volumeUnitsPerCubicInch` | number |  | 主単位のみ。1立方インチに相当する体積単位の数。 |
| `volumeDecimalPrecision` | integer |  | 主単位のみ。体積の小数点以下の桁数。 |
| `documentAngularUnit` | string |  | 主単位のみ。次のいずれか: `degrees`, `radians`, `gradians`。 |
| `documentAngularPrecision` | integer |  | 主単位のみ。角度の小数点以下の桁数。 |

**結果**

| キー | 説明 |
|---|---|
| `applied` | 指定された設定ごとに1項目。Vectorworksが設定を受け付けた場合は`true`です。不明な`angularUnit`または`documentAngularUnit`の名前では`false`になります。 |
| `units` | 変更後の単位設定（getUnitsと同じ形式）。 |

エラー: `provide at least one unit setting to change`。

### convertUnits

ワールド単位とファイルの単位の間で長さを変換します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

このAPIのすべてのツールが使用するワールド単位と、VectorworksのUIに表示されるファイルの単位との間で長さを変換します。`worldLength`は`inDocumentUnits`として、`unitsLength`は`inWorldUnits`として返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `worldLength` | number |  | ワールド単位の長さ。 |
| `unitsLength` | number |  | ファイルの単位の長さ。 |

**結果**

| キー | 説明 |
|---|---|
| `inDocumentUnits` | `worldLength`指定時のみ。その長さをファイルの単位で表した値。 |
| `inWorldUnits` | `unitsLength`指定時のみ。その長さをワールド単位で表した値。 |
| `documentUnits` | ファイルの主単位の名前。 |

変換に失敗した場合、そのキーは省略されます。エラー: `provide 'worldLength' and/or 'unitsLength'`。

### setView

ビューの移動、ズームの設定、ユーザー原点の移動、用紙の再描画を行います。

> **作用:** 編集 · **安全性:** 低 · **取り消し:** 1ステップ「MCP: setView」 · **runToolBatch内:** はい

**詳細**

表示内容と図面の原点の位置を変更します: `center`はビューをワールド上の点へ移動し、`zoom`はズーム倍率（1.0 = 100%）を設定し、`userOrigin`はユーザーに(0,0)として見えるワールド上の点を移動し、`redraw`は用紙の領域を強制的に再描画します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `center` | [点](Common.md#points) |  | 中心点。 |
| `zoom` | number |  | ズーム倍率。1.0 = 100%。0以下の値は拒否されます（`zoomSet`が`false`）。 |
| `userOrigin` | [点](Common.md#points) |  | ユーザーに(0,0)として見えるワールド上の点。 |
| `redraw` | boolean |  | `true`で用紙の領域を強制的に再描画します。 |

**結果**

| キー | 説明 |
|---|---|
| `centerSet` | `center`指定時のみ。ビューが移動した場合は`true`。 |
| `zoomSet` | `zoom`指定時のみ。ズームが設定された場合は`true`。 |
| `userOriginSet` | `userOrigin`指定時のみ。常に`true`。ユーザー原点の移動を無効にするコンテナを編集している間は、Vectorworksはユーザー原点を移動しません。getDocumentInfoで値を読み直してください。 |
| `redrawn` | `redraw`が`true`の場合のみ。用紙の領域を再描画した場合は`true`。 |

点でない`center`や`userOrigin`、数値でない`zoom`はエラーなしでスキップされ、結果にキーはありません。エラー: 呼び出しが何も設定しない場合は`provide 'center', 'zoom', 'userOrigin' and/or 'redraw'`。

### getPreferences

ファイル設定の1つのカテゴリを読み取ります。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

`category`で指定する1つのカテゴリのファイル設定を読み取ります: display（レンダリングと画面表示）、editing（セッション、寸法、取り消し、自動保存）、snapping（スマートカーソル）、grid、stackLayers、text（新しい文字のデフォルト）、defaultAttributes（RGBとカラーテーブルのインデックスによる線／面の色、スタイル、線の太さ、面のリソース、不透明度、マーカー、クラス属性を使用するフラグ、ファイルのドロップシャドウ、新しいオブジェクトと寸法に使用するクラス）。

`category`を省略するとすべてを読み取ります。categoryが"variable"の場合は、`selector`と`type`（bool|uint8|int8|int16|int32|double|string）で指定するプログラム変数の値をそのまま読み取ります。

> **注:** `category`を省略すると、結果には名前付きの7つのカテゴリが含まれます。`variable`は指定した場合にだけ読み取ります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `category` | string |  | 次のいずれか: `display`, `editing`, `snapping`, `grid`, `stackLayers`, `text`, `defaultAttributes`, `variable`。省略すると名前付きの7つのカテゴリを読み取ります。 |
| `selector` | integer |  | `variable`の場合: プログラム変数のセレクタ。 |
| `type` | string |  | 次のいずれか: `bool`, `uint8`, `int8`, `int16`, `int32`, `double`, `string`。`variable`の場合: プログラム変数の型。デフォルト: `bool`。 |

**結果**

| キー | 説明 |
|---|---|
| `display`、`editing`、`snapping`、`grid`、`stackLayers`、`text`、`defaultAttributes` | 読み取ったカテゴリごとに1つのオブジェクト: 指定したカテゴリ、または`category`を省略した場合は7つすべて。 |
| `selector`、`value` | `category`が`variable`の場合は、上記のカテゴリの代わりに、プログラム変数のセレクタと値。 |

読み取れない設定は省略されます。エラー: `unknown 'category' (display, editing, snapping, grid, stackLayers, text, defaultAttributes, variable)`、`unknown variable 'type': <type>`、`program variable not available`。

**カテゴリごとの設定**

setPreferencesは同じ設定を同じ名前で書き込みます。

| カテゴリ | 設定 |
|---|---|
| `display` | 真偽値: `blackAndWhiteOnly`、`useLayerColors`、`zoomLineThickness`、`blackBackground`、`showRulers`、`showScrollBars`、`showPageBoundary`、`showPageBreaks`、`showOthersInGroup`、`showOthersInGroupGrayed`、`eightSelectionHandles`、`fullScreenCursor`、`noFillBehindText`、`adjustFlippedText`、`xRayMode`、`displayHiddenObjectsGhosted`、`showInternalOriginMarker`、`allowDropShadows`、`perspectiveCropped`。整数: `conversionResolution2D`、`conversionResolution3D`、`displayLightObjects`、`rotatedTextDisplay`、`displayBitmaps`、`hiddenLineShade`、`display3DLoci`、`defaultRenderMode`、`defaultProjection`、`rotationResponse3D`。 |
| `editing` | 真偽値: `clickDrag`、`offsetDuplicates`、`associateDimensions`、`autoAssociateDimensions`、`createDimensionsInDimensionClass`、`wallAutoJoin`、`undoViewChanges`、`duplicateTagsWithObjects`、`occludedPickingAndSnapping`。整数: `maxUndos`、`autoSaveInterval`、`backupInterval`、`lineWeightUnit`、`dimensionStandard`。数値: `customMoveDistance`。 |
| `snapping` | 真偽値: `snapToGrid`、`snapToObjects`、`snapToLoci`、`snapToEdgePoints`、`snapToSelectionOnly`、`snapToAngle`、`snapToIntersection`、`smartPoints`、`snapToDistance`、`smartEdge`、`constrainTangent`、`snapToEndPoint`、`snapToMidPoint`、`snapToCenter`、`snapToQuadrant`、`snapToInsertionPoint`、`snapToVertex`、`snapToEdge`、`snapToMasterPoints`、`snapToRelativeAngles`、`snapToAlternateCoordinateSystem`、`snapToAnglesFromAxes`（読み取り専用）、`snapToCombinedPageArea`、`snapToIndividualPages`、`floatingDatum`、`showSnapBox`、`showSelectionBox`、`useEdgeOffset`、`useProportionalDivision`、`useMultipleDivisions`。整数: `snapRadiusPixels`。数値: `snapBoxRadius`、`selectionRadius`、`relativeAngle`、`alternateCoordinateSystemAngle`、`edgeOffsetDistance`、`proportionalPercent`、`divisionDistance`。文字列: `snapAngles`。 |
| `grid` | 真偽値: `showGrid`、`printGrid`、`snapToGrid`。数値: `snapGridX`、`snapGridY`、`referenceGridX`、`referenceGridY`、`sheetLayerSnapGridX`、`sheetLayerSnapGridY`、`angle`、`angleY`。 |
| `stackLayers` | 真偽値: `enabled`、`create2DObjects`、`ignoreOtherScales`、`restoreViews`、`centerView`、`showPageBoundary`、`onlyActiveLayer2DObjects`、`onlyStoryLayers`。 |
| `text` | `fontName`（文字列）、`size`（数値、ワールド単位）、`leading`（数値）、`style`（真偽値`bold`、`italic`、`underline`、`outline`、`shadow`を持つオブジェクト）、`justification`（`left`、`center`、`right`のいずれか）、`verticalAlignment`（`topOfBox`、`topBaseline`、`centerOfBox`、`bottomBaseline`、`bottomOfBox`のいずれか）、`lineSpacing`（`single`、`oneAndHalf`、`double`、`custom`のいずれか）。 |
| `defaultAttributes` | RGBの色（`penForeColor`、`penBackColor`、`fillForeColor`、`fillBackColor`）とカラーテーブルのインデックスの色（`penForeColorIndex`、`penBackColorIndex`、`fillForeColorIndex`、`fillBackColorIndex`）；`penStyle`、`lineWeightMils`、`fillStyle`、`fillType`（読み取り専用）、`hatch`、`gradient`、`imageFill`、`tile`、`penOpacity`、`fillOpacity`；クラス属性を使用するフラグ`penColorsByClass`、`fillColorsByClass`、`penStyleByClass`、`lineWeightByClass`、`fillStyleByClass`、`penOpacityByClass`、`fillOpacityByClass`、`markersByClass`；`beginningMarker`と`endMarker`（[マーカー](Attributes.md#line-end-markers)）；`documentDropShadow`（読み取り専用、[ドロップシャドウ](Attributes.md#drop-shadow)）；`class`と`dimensionClass`（クラス名）。 |

### setPreferences

1つのカテゴリのファイル設定を書き込みます。

> **作用:** 編集 · **安全性:** 低 · **取り消し:** 1ステップ「MCP: setPreferences」 · **runToolBatch内:** はい

**詳細**

ファイル設定を書き込みます。`category`でグループ（display、editing、snapping、grid、stackLayers、text、defaultAttributes）を選択し、`values`はgetPreferencesが返す設定名を持つオブジェクトです。含まれるメンバーだけを書き込み、成功したものを結果で報告します。

**読み取り専用:** snapToAnglesFromAxes、fillType、documentDropShadow。defaultAttributesの色は、RGB（penForeColorなど）またはカラーテーブルのインデックス（penForeColorIndexなど）を受け付けます。現在の値と同じインデックスは無視されるため、getPreferencesで読み取った値のRGB色を編集してそのまま送り返せます。両方の形式が変わる場合はインデックスが優先されます。beginningMarker／endMarkerは部分指定のマーカーオブジェクトを受け付けます。penOpacityByClass／fillOpacityByClass以外のクラス属性を使用するフラグはオンにすることしかできません（明示的な値を書き込むとオフになります）。categoryが"variable"の場合は、`type`型のプログラム変数`selector`に`value`をそのまま書き込みます。

> **注:** 設定は`values`から読み取ります。`values`がオブジェクトでない場合は、呼び出しの最上位の引数から読み取ります。カテゴリにない設定名はエラーなしで無視され、JSON型が誤った値はエラーなしで`false`、0、または空文字列として書き込まれます。`defaultAttributes`では、クラス属性を使用するフラグ（`penColorsByClass`、`fillColorsByClass`、`penStyleByClass`、`lineWeightByClass`、`fillStyleByClass`、`markersByClass`）は値が`true`の場合にだけ書き込まれ、`applied`に報告されます。明示的な`false`は無視されます。`penOpacityByClass`と`fillOpacityByClass`は`true`または`false`を受け付けます。`variable`で`type`が`bool`の場合、真偽値でない`value`は`false`として書き込まれます。`text`では、不明な`justification`、`verticalAlignment`、`lineSpacing`の名前はそれぞれ`left`、`topOfBox`、`custom`として書き込まれ、オブジェクトでない`style`は無視されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `category` | string | はい | 次のいずれか: `display`, `editing`, `snapping`, `grid`, `stackLayers`, `text`, `defaultAttributes`, `variable`。 |
| `values` | object |  | 書き込む設定。getPreferencesがそのカテゴリについて返す名前で指定します。含まれるメンバーだけを書き込みます。 |
| `selector` | integer |  | `variable`の場合: プログラム変数のセレクタ。 |
| `type` | string |  | 次のいずれか: `bool`, `uint8`, `int8`, `int16`, `int32`, `double`, `string`。`variable`の場合: プログラム変数の型。デフォルト: `bool`。 |
| `value` | string or number or integer or boolean |  | `variable`の場合: 書き込む値。JSON型は`type`に適合する必要があります。 |

**結果**

| キー | 説明 |
|---|---|
| `applied` | カテゴリの場合: 指定された設定ごとに1項目で、Vectorworksが受け付けた場合は`true`。`variable`の場合: 変数を書き込んだ場合は`true`。 |
| `selector` | `variable`の場合: 書き込んだセレクタ。 |

`defaultAttributes`では、`applied`に次のキーがあります: `colors`（RGBの色）、`colorIndices`（カラーテーブルのインデックス。インデックスがカラーインデックスの範囲内の整数でない場合は`false`）、クラス属性を使用するフラグ、`penStyle`、`lineWeightMils`、`fillStyle`、`hatch`、`gradient`、`imageFill`、`tile`、`opacity`（`penOpacity`と`fillOpacity`。省略した方は値を維持）、`opacityByClass`（`penOpacityByClass`と`fillOpacityByClass`。省略した方は値を維持）、`beginningMarker`、`endMarker`（部分指定のマーカーでは、省略したメンバーは値を維持）、`class`と`dimensionClass`（クラスが存在しない場合は`false`）。`text`カテゴリには、`style`オブジェクトについての`applied.style`があります。含まれるメンバーだけが変わります。

エラー: `unknown 'category' (display, editing, snapping, grid, stackLayers, text, defaultAttributes, variable)`、`unknown variable 'type': <type>`。

## Selection

> **グループ:** `Selection` · **グループID:** `selection` · **初期状態で有効:** はい · **安全性レベル:** 中 · **ツール数:** 3

**現在の選択内容を一覧表示し、移動、回転、拡大縮小、複製、グループ化、削除、クラス変更を一括で行います。**

現在の選択内容を照会、操作します: 選択したオブジェクトを一覧表示し、移動、回転、拡大縮小、複製、グループ化、削除、クラス変更を一括で行います。各編集は、名前付きで取り消し可能な独立したVectorworksの操作として実行されます。

| ツール | 作用 | 安全性 | 概要 |
|---|---|---|---|
| [`getSelection`](#getselection) | 読み取り専用 | 低 | 全レイヤの選択オブジェクトと選択範囲の境界を一覧表示します。 |
| [`selectObjects`](#selectobjects) | 編集 | 中 | 検索条件やUUIDでオブジェクトを選択、選択解除するか、すべてを選択、選択解除します。 |
| [`editSelection`](#editselection) | 編集 | 中 | 選択内容を移動、回転、拡大縮小、複製、グループ化、削除、クラス変更します。 |

### getSelection

全レイヤの選択オブジェクトと選択範囲の境界を一覧表示します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

現在選択されているオブジェクト（uuid、type、name）と、選択内容全体を囲む境界を一覧表示します。アクティブレイヤだけでなく、図面の全レイヤの選択オブジェクトを対象とします。`descend`（デフォルトはnone、groups、viewports、all）を指定すると、ユーザーがグループ内部を編集中の場合など、それらのコンテナ内の選択オブジェクトも一覧表示します。`bounds`は選択された最上位のオブジェクトを対象とします。

`workingLayers`は、editSelectionが作用する選択内容の件数と境界を返します: アクティブレイヤの選択オブジェクトと、レイヤオプションでその他のレイヤの編集が許可されている場合はそれらのレイヤの選択オブジェクトです。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `descend` | string |  | 次のいずれか: `none`, `groups`, `viewports`, `all`。デフォルト: `none`。 |

**結果**

| キー | 説明 |
|---|---|
| `count` | `objects`内のオブジェクト数。 |
| `objects` | 選択されているオブジェクト。それぞれ[オブジェクト参照](Common.md#object-references)の形式です。 |
| `bounds` | 選択された最上位のオブジェクト全体の[境界](Common.md#rectangles)。何も選択されていない場合は省略されます。 |
| `workingLayers` | editSelectionが作用する選択内容: `count`（選択オブジェクト数）と`bounds`。該当する選択内容がない場合、`bounds`は省略されます。 |

エラー: `unknown 'descend'; use none | groups | viewports | all`。

### selectObjects

検索条件やUUIDでオブジェクトを選択、選択解除するか、すべてを選択、選択解除します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ「MCP: selectObjects」 · **runToolBatch内:** はい

**詳細**

選択内容を変更します。`all`または`none`ですべてを選択／選択解除するか、`criteria`（findObjectsと同じ構文のVectorworksの検索条件文字列）と`uuids`の一方または両方を指定します。コンパイルできない検索条件はエラーを返します。`mode`の"replace"（デフォルト）または"add"は対象を選択して`selectedCount`を返し、"remove"は対象だけの選択を解除して`deselectedCount`を返します。

> **注:** 最初に`all`、次に`none`を確認します。どちらかが`true`の場合、呼び出しは`criteria`、`uuids`、`mode`を無視します。それ以外の場合、対象は`criteria`に一致するオブジェクトと、`uuids`のいずれかを持つオブジェクトを合わせたものです。不明な`mode`は`replace`として動作します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `all` | boolean |  | `true`ですべてのオブジェクトを選択します。 |
| `none` | boolean |  | `true`ですべてのオブジェクトの選択を解除します。 |
| `criteria` | string |  | findObjectsと同じ構文のVectorworksの検索条件文字列。 |
| `uuids` | array of string |  | 操作対象のオブジェクトのUUID。どのオブジェクトにも一致しないUUIDは、エラーなしでスキップされます。 |
| `mode` | string |  | 次のいずれか: `replace`, `add`, `remove`。デフォルト: `replace`。 |

**結果**

| キー | 説明 |
|---|---|
| `selected` | `all`または`none`の場合: `"all"`または`"none"`。 |
| `selectedCount` | `mode`が`replace`または`add`の場合: 呼び出し後に選択されている対象の数（`add`では、呼び出し前から選択されていた対象も含む）。`criteria`に一致し`uuids`にも含まれるオブジェクトや、2回指定されたUUIDは、出現するたびに数えます。 |
| `deselectedCount` | `mode`が`remove`の場合: 選択を解除した対象オブジェクトの数。選択されていなかったオブジェクトは数えません。 |

エラー: `invalid criteria: <detail>`、一致するオブジェクトがない場合は`no target objects (provide 'criteria', 'uuids', or 'all' / 'none')`。

### editSelection

選択内容を移動、回転、拡大縮小、複製、グループ化、削除、クラス変更します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ「MCP: editSelection」 · **runToolBatch内:** はい

**詳細**

作業対象レイヤの選択内容全体を操作します（getSelectionの`workingLayers`を参照）。`action`: move（`offset`が必要）、rotate（ラジアンの`angle`、`center`）、scale（`scaleX`、`scaleY`、`center`）、duplicate（`offset`）、group、delete、setClass（`class`。`useClassAttributes`を指定すると、オブジェクトのすべての属性も「クラス属性を使用」に設定します）。`group`は、選択オブジェクトをアクティブレイヤ（または編集中のグループやシンボル定義）の新しいグループに移動し、そのグループを選択して`groupedCount`と共に返します。壁に挿入されたドアや窓、プラグインオブジェクトや屋根の構成要素など、グループに入れられない選択オブジェクトは元の場所に残ります（`ungroupedCount`）。グループ化できる選択オブジェクトが1つもない場合は、呼び出しが失敗して何も変更しません。

グループ化を「編集 &gt; 取り消し」で取り消すと、オブジェクトは元の場所に戻り、グループは削除されます。

> **注:** このツールは、操作に詳細で挙げた引数があるかどうかを確認しません。`offset`がない場合、`move`と`duplicate`は(0,0)を使用するため、オブジェクトは移動しません。`center`がない場合、`rotate`と`scale`はワールド原点(0,0)を中心に回転または拡大縮小します。`angle`のデフォルトは0、`scaleX`と`scaleY`のデフォルトは1です。このツールは、`getSelection`が`workingLayers`として返す作業対象レイヤの選択内容だけに作用します。作業対象レイヤにない選択オブジェクトは変更されません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `action` | string | はい | 次のいずれか: `move`, `rotate`, `scale`, `duplicate`, `group`, `delete`, `setClass`。 |
| `offset` | [点](Common.md#points) |  | `move`と`duplicate`: 移動する距離（ワールド単位）。デフォルト: (0,0)。 |
| `angle` | number |  | 反時計回りの角度（ラジアン）。`rotate`のみ。デフォルト: 0。 |
| `center` | [点](Common.md#points) |  | `rotate`と`scale`: 回転または拡大縮小の中心点。デフォルト: ワールド原点。 |
| `scaleX` | number |  | `scale`のみ: X方向の倍率。デフォルト: 1。倍率0は失敗します（`ok`が`false`）。 |
| `scaleY` | number |  | `scale`のみ: Y方向の倍率。デフォルト: 1。倍率0は失敗します（`ok`が`false`）。 |
| `class` | string |  | `setClass`のみ: 既存のクラスの名前。 |
| `useClassAttributes` | boolean |  | `setClass`のみ: `true`では、オブジェクトのすべての属性も「クラス属性を使用」に設定します。 |

**結果**

| キー | 説明 |
|---|---|
| `ok` | `move`、`rotate`、`scale`、`duplicate`: Vectorworksが操作を適用した場合は`true`、作業対象レイヤで何も選択されていない場合は（`err`なしで）`false`。`setClass`: 選択したすべてのオブジェクトにクラスが設定された場合は`true`。何も選択されていない場合も同様です。`duplicate`の後は、新しい複製が選択された状態になります。 |
| `deletedCount` | `delete`: 削除したオブジェクトの数。何も選択されていない場合は0。 |
| オブジェクト参照、`groupedCount`、`ungroupedCount` | `group`: 新しいグループの[オブジェクト参照](Common.md#object-references)、グループに移動したオブジェクトの数、および元の場所に残ったオブジェクトがある場合のみ`ungroupedCount`。操作後、グループが選択されます。 |

エラー: `unknown 'action'; use move | rotate | scale | duplicate | group | delete | setClass`、`setClass`で`class`が不明または空の場合は`class not found`。`group`は`failed to group the selection`で失敗します。Vectorworksがグループを作成できない場合はこのメッセージだけで、それ以外の場合は次のいずれかの理由が続きます: `nothing is selected on the working layers`、`the active container is not a layer, a group or a symbol definition`、`none of the selected objects can be moved into a group (objects inserted in a wall, such as doors and windows, and members of a plug-in object or a roof stay where they are)`、`none of the selected objects could be moved into a group`。エラーが発生すると呼び出しは元に戻されます（`rolledBack`）。
