[English](../../MCP/v2027.2/ObjectsAnnotation.md) • [Deutsch](../../MCP.de/v2027.2/ObjectsAnnotation.md) • **日本語**

# ObjectsAnnotation — 注釈と寸法

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

データタグ、図面枠と表題欄のプロジェクトデータ、およびセンターマークを含む寸法など、注釈を扱うツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [Annotation](#annotation)
  - [createDataTag](#createdatatag)
  - [createTitleBlock](#createtitleblock)
  - [getAnnotationObject](#getannotationobject)
  - [setAnnotationObject](#setannotationobject)
  - [tagObject](#tagobject)
  - [getObjectTags](#getobjecttags)
  - [getProjectData](#getprojectdata)
  - [setProjectData](#setprojectdata)
- [Dimensioning](#dimensioning)
  - [createLinearDimension](#createlineardimension)
  - [createAngularDimension](#createangulardimension)
  - [createArcLengthDimension](#createarclengthdimension)
  - [createRadialDimension](#createradialdimension)
  - [createCenterMark](#createcentermark)
  - [getDimension](#getdimension)
  - [setDimension](#setdimension)
  - [getObjectDimensions](#getobjectdimensions)

<a id="overview"></a>

## 概要

このフォルダには、2個のツールグループに合計16個のツールが含まれています。

| グループ | グループID | 初期状態で有効 | リスクレベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [Annotation](#annotation) | `annotation` | いいえ | 中 | 8 | データタグ、図面枠、およびファイルの表題欄のプロジェクトデータを扱います。 |
| [Dimensioning](#dimensioning) | `dimensioning` | いいえ | 中 | 8 | 直線寸法、角度寸法、円弧長寸法、円寸法、およびセンターマークを扱います。 |

## Annotation

> **グループ:** `Annotation` · **グループID:** `annotation` · **初期状態で有効:** いいえ · **リスクレベル:** 中 · **ツール数:** 8

**データタグ、図面枠、およびファイルの表題欄のプロジェクトデータを扱います。**

データタグと図面枠を使って図面に注釈を付けます。データタグは、オブジェクトから読み取ったデータ（レコードフィールド、プラグインパラメータ、クラスなど）でそのオブジェクトにラベルを付けます。図面枠は、シートの枠、区域/グリッド、およびプロジェクトデータ、図面情報、改訂情報、版情報を表示する表題欄を描画します。どちらのオブジェクトも、グラフィックスはプラグインスタイルから取得します。図面にスタイルがまだない場合、これらのツールはVectorworksのコンテンツから該当するスタイルを見つけて取り込みます。

各変更は、固有の名前を持つ、取り消し可能なVectorworksの操作として実行されます。

| ツール | 作用 | リスク | 概要 |
|---|---|---|---|
| [`createDataTag`](#createdatatag) | 編集 | 中 | データタグを作成し、必要に応じてオブジェクトに関連付けます。 |
| [`createTitleBlock`](#createtitleblock) | 編集 | 中 | 図面枠を作成します。 |
| [`getAnnotationObject`](#getannotationobject) | 読み取り専用 | 低 | データタグまたは図面枠を読み取ります。 |
| [`setAnnotationObject`](#setannotationobject) | 編集 | 中 | データタグまたは図面枠を編集します。 |
| [`tagObject`](#tagobject) | 編集 | 中 | データタグをオブジェクトに関連付けるか、関連付けを解除します。 |
| [`getObjectTags`](#getobjecttags) | 読み取り専用 | 低 | オブジェクトに関連付けられているデータタグを一覧表示します。 |
| [`getProjectData`](#getprojectdata) | 読み取り専用 | 低 | ファイルの表題欄のプロジェクトデータを読み取ります。 |
| [`setProjectData`](#setprojectdata) | 編集 | 中 | ファイルの表題欄のプロジェクトデータを書き込みます。 |

### createDataTag

データタグを作成し、必要に応じてオブジェクトに関連付けます。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createDataTag" · **runToolBatch内:** はい

**詳細**

`position`にデータタグを作成します。`taggedObjectUuid`は、タグがデータを読み取る対象のオブジェクトです（指定しない場合、タグは空の状態で作成されます。後でtagObjectを使用してください）。省略可能な`style`は、タグの文字レイアウトを提供するデータタグスタイル（シンボル定義）の名前です。図面にまだない場合はVectorworksのコンテンツから取り込まれます。省略した場合や見つからない場合は、利用可能なスタイルが使用されます。実際に適用されたスタイルは`style`として返されます。

`useLeader`、`leaderLength`、`leaderAngle`（ラジアン）、`leaderEnd`（引出線が指す点）、およびプラグインの生の`params`は省略可能です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点。 |
| `taggedObjectUuid` | string |  | タグがデータを読み取る対象オブジェクトのUUID。UUIDのみ指定できます。 |
| `style` | string |  | データタグスタイル（シンボル定義）の名前。必要に応じて取り込まれます。省略した場合や見つからない場合は、利用可能なスタイルが使用されます。 |
| `useLeader` | boolean |  | タグに引出線を表示するかどうか。 |
| `leaderLength` | number |  | 引出線の長さ（ワールド単位）。 |
| `leaderAngle` | number |  | ラジアン。 |
| `leaderEnd` | [点](Common.md#points) |  | 引出線が指す点。 |
| `params` | object |  | プラグインの生のパラメータ`{ "ParamName": value }`。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。各書き込みの結果は報告されません。拒否された名前や値は、エラーにならずに無視されます。オブジェクトでない`params`は無視されます。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

**結果**

新しいデータタグのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と次のキーを返します。

| キー | 説明 |
|---|---|
| `style` | 適用されたスタイルの名前。要求した`style`が見つからなかった場合は、その名前とは異なります。名前を読み取れない場合は省略されます。 |
| `taggedObject` | タグが関連付けられているオブジェクトの参照。タグが関連付けられている場合のみ。 |

`applied`は返されません。エラー：`object to tag not found`（`taggedObjectUuid`を持つオブジェクトがない）、`failed to create data tag: a usable data tag style is required in the drawing or Vectorworks content, and any requested tagged object must support association`（タグを付けられないオブジェクトの場合もこのエラーになります。[`getObjectTags`](#getobjecttags)の`canBeTagged`を参照）、`failed to set data tag leader properties`（Vectorworksが`useLeader`、`leaderLength`、`leaderAngle`、または`leaderEnd`を拒否した。新しいタグは削除されます）。失敗した呼び出しはロールバックされます（`rolledBack`）。

### createTitleBlock

図面枠を作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createTitleBlock" · **runToolBatch内:** はい

**詳細**

`position`に図面枠を作成します。通常はシートレイヤ上に作成します。省略可能な`style`は、表題欄のグラフィックスを提供する図面枠スタイルの名前です。図面にまだない場合はVectorworksの表題欄コンテンツから取り込まれます。省略した場合や見つからない場合は、利用可能なスタイルが使用されます。実際に適用されたスタイルは`style`として返されます。

`sheetSize`（例："ANSI D"、"ISO A1"）、カスタムサイズの`sheetWidth`/`sheetHeight`、`showGrids`、フィールド名と値の組を格納した`sheetData`オブジェクト（シートレイヤタイトル、シートレイヤ番号、設計者名など）、およびプラグインの生の`params`は省略可能です。

> **注:** Vectorworksが値を受け付けたかどうかは確認しません。図面情報のフォーマットにない`sheetData`フィールドなど、拒否された値はエラーにならずに無視されます。`sheetData`または`params`がオブジェクトでない場合も無視されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点。 |
| `style` | string |  | 図面枠スタイル（シンボル定義）の名前。必要に応じてVectorworksの表題欄コンテンツから取り込まれます。省略した場合や見つからない場合は、利用可能なスタイルが使用されます。 |
| `sheetSize` | string |  | 定義済みの枠のサイズ名。例：`ANSI D`、`ISO A1`。 |
| `sheetWidth` | number |  | カスタムの枠のサイズの幅（ワールド単位）。オブジェクトがカスタムサイズを使用する場合にのみ意味があります。 |
| `sheetHeight` | number |  | カスタムの枠のサイズの高さ（ワールド単位）。オブジェクトがカスタムサイズを使用する場合にのみ意味があります。 |
| `showGrids` | boolean |  | 区域/グリッドを表示するかどうか。 |
| `sheetData` | object |  | 図面情報`{ "<field name>": value }`。ファイルの図面情報のフォーマットにあるフィールドのみ書き込まれます。[`getAnnotationObject`](#getannotationobject)はそれらを`sheetDataFieldNames`として一覧表示します。文字列でない値はJSONテキストとして保存されます。 |
| `params` | object |  | プラグインの生のパラメータ`{ "ParamName": value }`。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。各書き込みの結果は報告されません。拒否された名前や値は、エラーにならずに無視されます。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

**結果**

新しい図面枠のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、実際に適用されたスタイル名`style`を返します。指定した`style`が見つからない場合は別の名前になり、名前を読み取れない場合は省略されます。`applied`は返されません。エラー：`failed to create title block border: no title block border style is available in the drawing or in the Vectorworks content (a title block needs a style to get its graphics from)`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### getAnnotationObject

データタグまたは図面枠を読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

uuid、name、またはindexでデータタグまたは図面枠を読み取ります。どちらも`style`名、`isStyled`、およびスタイルリソース（シンボル定義）を`styleResource`として返します。データタグは、引出線（`useLeader`、`leaderType`、`leaderLength`、`leaderAngle`、`shoulderLength`、`useMarker`、`leaderEnd`）、配置（`offset`、`horizontalPosition`、`moveBehaviour`、`alignToWalls`）、適合性の条件、タグの対象オブジェクト、および現在表示している`data`を返します。

図面枠は、枠のサイズと`margins`、区域/グリッド（`showGrids`、`horizontalZones`、`verticalZones`、`drawCropMarks`）、`useAsTitleBlock`、`isActiveTitleBlock`、方位記号（`displayNorthArrow`、`northAngle`）、図面スタンプ（`displayDrawingStamp`、`drawingStampText`）、シートレイヤのID/タイトル/日付、`sheetData`と図面情報のフォーマットの`sheetDataFieldNames`、およびファイルの`projectData`と`revisions`を返します。

設定にはsetAnnotationObjectと同じキー、単位、および列挙値を使用します。

> **注:** キー`kind`、`isStyled`、`styleResource`、`taggedObject`、`data`、`sheetID`、`sheetTitle`、`sheetDate`、`latestIssueDate`、`revisions`、`sheetDataFieldNames`は、オブジェクトを説明するだけのキーです。[`setAnnotationObject`](#setannotationobject)はこれらを無視します。`taggedObject`を変更するには[`tagObject`](#tagobject)を使用してください。適合性の条件は`useCriteria`と`criteria`として、枠のサイズは`sheetSize`、`sheetWidth`、`sheetHeight`として返されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |

**結果**

オブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と以下のキーを返します。Vectorworksが読み取れない値（タグに引出線がない場合の`leaderEnd`など）は省略されます。

| キー | 説明 |
|---|---|
| `kind` | `DataTag`または`TitleBlockBorder`。 |
| `style`、`isStyled`、`styleResource` | スタイル名、オブジェクトがスタイルを使用しているかどうか、およびスタイルリソース（シンボル定義）。 |
| `taggedObject` | データタグのみ。関連付けられている場合にのみ、タグの対象オブジェクトの参照。 |
| `data` | データタグのみ。`{ "<label>": "<printed text>" }`、タグが現在表示しているデータ。 |
| `sheetID`、`sheetTitle`、`sheetDate` | 図面枠のみ。 |
| `latestIssueDate` | 図面枠のみ。版情報がある場合のみ。 |
| `sheetData` | 図面枠のみ。図面情報のフォーマットの`{ "<field>": "<value>" }`。フィールド名は`sheetDataFieldNames`に一覧表示されます。 |
| `projectData` | 図面枠のみ。ファイル全体のプロジェクトデータ。[`getProjectData`](#getprojectdata)が返す`projectData`と同じです。 |
| `revisions` | 図面枠のみ。`{ number, date, note, publishDate, recipients }`の配列。 |

その他のキーは上記の詳細に記載されています。長さはワールド単位、角度はラジアンです。エラー：`object not found`、`not an annotation object (expected a Data Tag or a Title Block Border)`。

### setAnnotationObject

データタグまたは図面枠を編集します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: setAnnotationObject" · **runToolBatch内:** はい

**詳細**

uuidでデータタグまたは図面枠を編集します。

**両方の種類に共通：** `style`（必要に応じて取り込まれます）、または`removeStyle`: trueでオブジェクトとスタイルの関連付けを解除します。この設定は最初に適用されます。その後、各パラメータは現在の値を保持したまま、インスタンスごとに編集可能になります。

**データタグ：** `useLeader`、`leaderType`、`leaderLength`、`leaderAngle`（ラジアン）、`shoulderLength`、`useMarker`（引出線の先端のマーカー）、`leaderEnd`、`offset`、`horizontalPosition`（引出線のどちら側に文字を置くか）、`moveBehaviour`（タグをドラッグしたときに移動する部分）、`alignToWalls`、`useCriteria`、`criteria`。

**図面枠：** `sheetSize`、`sheetWidth`、`sheetHeight`、`margins`（省略した辺は現在の値を保持）、`showGrids`、`horizontalZones`、`verticalZones`、`drawCropMarks`、`useAsTitleBlock`、`isActiveTitleBlock`（ファイルが図面情報を読み取る表題欄。シートごとに1つ）、`displayNorthArrow`、`northAngle`（ラジアン）、`displayDrawingStamp`、`drawingStampText`（'Stamp Text'パラメータ（「スタンプの文字」）でカスタムの項目を選択した場合に表示）、フィールド名と値の組を格納した`sheetData`および`projectData`オブジェクト。`params`オブジェクトでプラグインの生のパラメータを設定します。各設定が書き込まれたかどうかは`applied`で返されます。

> **注:** オブジェクトは`uuid`、`name`、`index`の順に検索されます。詳細には`uuid`だけを記載しています。オブジェクトの種類にない設定は無視されます。データタグは`sheetSize`などの図面枠のキーを無視し、図面枠はデータタグのキーを無視します。

> **注:** 型が正しくない値の扱いは、キーによって異なります。`leaderType`、`useMarker`、`horizontalPosition`、`moveBehaviour`、`alignToWalls`、`drawCropMarks`、`isActiveTitleBlock`、`displayNorthArrow`、`displayDrawingStamp`は、値の型が正しくない場合（不明な列挙名も含みます）、何も書き込まずに`false`を報告します。`removeStyle`、`margins`、`sheetData`、`projectData`、`params`（それぞれの行を参照）を除くその他のキーは、チェックせずに値を変換します。欠落しているか型が正しくない数値は0、真偽値は`false`、文字列は空の文字列、点は原点になります。その値が書き込まれ、`applied`はVectorworksがそれを受け付けたかどうか（通常は`true`）を報告します。真偽値でない`removeStyle`は`false`として扱われます。何も解除されず、`applied`に`removeStyle`の項目はありません。各キーは、記載されている型で送信してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `style` | string |  | スタイル（シンボル定義）の名前。図面内のスタイルが優先され、次にVectorworksのコンテンツが使用されます（必要に応じて取り込まれます）。どこにも見つからない名前でも失敗せず、代わりにそのオブジェクトの種類の別のスタイルが適用され、`applied.style`は`true`のままです。`false`になるのは、利用可能なスタイルがまったくない場合だけです。 |
| `useLeader` | boolean |  | データタグで使用します。 |
| `leaderLength` | number |  | データタグで使用します。ワールド単位。 |
| `leaderAngle` | number |  | データタグで使用します。ラジアン。 |
| `shoulderLength` | number |  | データタグで使用します。ワールド単位。 |
| `leaderEnd` | [点](Common.md#points) |  | データタグで使用します。 |
| `offset` | [点](Common.md#points) |  | データタグで使用します。 |
| `useCriteria` | boolean |  | データタグで使用します。 |
| `criteria` | string |  | データタグで使用します。 |
| `removeStyle` | boolean |  | 両方の種類で使用します。`true`では、他の設定を書き込む前にスタイルとの関連付けを解除します。すべてのパラメータは値を保持し、その後インスタンスごとに編集できます。`false`は何もしません。同じ呼び出しで`style`を指定すると、スタイルが再び適用されます。 |
| `leaderType` | string |  | データタグで使用します。`line`、`arc`、`bezier`のいずれか。 |
| `useMarker` | boolean |  | データタグで使用します。引出線の先端のマーカー。 |
| `horizontalPosition` | string |  | データタグで使用します。`left`、`right`、`auto`のいずれか。 |
| `moveBehaviour` | string |  | データタグで使用します。`entireTag`、`leaderEnd`のいずれか。 |
| `alignToWalls` | boolean |  | データタグで使用します。 |
| `sheetSize` | string |  | 図面枠で使用します。定義済みの枠のサイズ名。例：`ANSI D`、`ISO A1`。 |
| `sheetWidth` | number |  | 図面枠で使用します。ワールド単位。オブジェクトがカスタムの枠のサイズを使用する場合にのみ意味があります。 |
| `sheetHeight` | number |  | 図面枠で使用します。ワールド単位。オブジェクトがカスタムの枠のサイズを使用する場合にのみ意味があります。 |
| `showGrids` | boolean |  | 図面枠で使用します。 |
| `horizontalZones` | integer |  | 図面枠で使用します。 |
| `verticalZones` | integer |  | 図面枠で使用します。 |
| `useAsTitleBlock` | boolean |  | 図面枠で使用します。 |
| `northAngle` | number |  | 図面枠で使用します。ラジアン。 |
| `margins` | object |  | 図面枠で使用します。4辺の余白の幅`{ "left": n, "right": n, "top": n, "bottom": n }`（ワールド単位）。[矩形](Common.md#rectangles)ではありません。`top`と`bottom`は位置ではなく幅です。省略した辺は現在の値を保持します。`margins`がオブジェクトでない場合、または数値でない辺がある場合は何も書き込まれず、`applied.margins`は`false`になります。 |
| `drawCropMarks` | boolean |  | 図面枠で使用します。 |
| `isActiveTitleBlock` | boolean |  | 図面枠で使用します。ファイルが図面情報を読み取る表題欄で、シートごとに1つです。 |
| `displayNorthArrow` | boolean |  | 図面枠で使用します。 |
| `displayDrawingStamp` | boolean |  | 図面枠で使用します。 |
| `drawingStampText` | string |  | 図面枠で使用します。'Stamp Text'パラメータ（「スタンプの文字」）でカスタムの項目を選択した場合に表示されます。 |
| `sheetData` | object |  | 図面枠で使用します。図面情報`{ "<field name>": value }`。図面情報のフォーマットにないフィールドは書き込まれません（`applied.sheetData`ではそのフィールドが`false`になります）。[`getAnnotationObject`](#getannotationobject)はフィールドを`sheetDataFieldNames`として一覧表示します。文字列でない値はJSONテキストとして保存されます。 |
| `projectData` | object |  | 図面枠で使用します。すべての表題欄で共有される、ファイル全体のプロジェクトデータのフィールド名と値の組。[`setProjectData`](#setprojectdata)と同じデータを書き込みます。プロジェクトデータのフォーマットにあるフィールドのみ書き込まれ、文字列でない値はJSONテキストとして保存されます。 |
| `params` | object |  | プラグインの生のパラメータ`{ "ParamName": value }`。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |

**結果**

`{ "applied": { … } }`を返します。`applied`には、指定した設定ごとに1つの項目があります。

| エントリ | 説明 |
|---|---|
| `<setting>` | Vectorworksが値を受け付けた場合は`true`。拒否した場合、または設定の型に値を変換できなかった場合は`false`。 |
| `removeStyle` | `removeStyle`が`true`の場合のみ。オブジェクトとスタイルの関連付けが解除されたかどうか。 |
| `sheetData` | 図面枠のみ。指定した各フィールドに1項目ずつの`{ "<field name>": true or false }`。 |
| `projectData` | 図面枠のみ。プロジェクトデータについての同じ形式。 |
| `params` | 生のプラグインパラメータについての`{ "<name>": true or false }`。 |

オブジェクトの種類にない設定には項目がありません。オブジェクトでない`sheetData`、`projectData`、`params`は無視されます。すべての項目が`false`でも、呼び出しは成功します。エラー：`object not found`、`not an annotation object (expected a Data Tag or a Title Block Border)`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### tagObject

データタグをオブジェクトに関連付けるか、関連付けを解除します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: tagObject" · **runToolBatch内:** はい

**詳細**

uuid/name/indexで指定したデータタグを`objectUuid`で指定したオブジェクトに関連付け、タグがそのオブジェクトからデータを読み取るようにします。また、`action`を"detach"に設定すると関連付けを解除できます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `objectUuid` | string |  | 対象オブジェクトのUUID。関連付ける場合は必須で、UUIDのみ指定できます。関連付けの解除には使用しません。 |
| `action` | string |  | 次のいずれか：`attach`、`detach`。デフォルトは`attach`で、その他の値も関連付けとして扱われます。 |

**結果**

| アクション | 結果 |
|---|---|
| attach | `{ "attached": true, "taggedObject": <object reference> }`。タグは対象オブジェクトからデータを読み取るようになります。以前の関連付けは置き換えられます。 |
| detach | `{ "detached": <boolean> }`。タグに関連付けられたオブジェクトがあった場合は`true`（Vectorworksは関連付けを解除したかどうかを報告しません）。関連付けがなかった場合は`false`。 |

エラー：`data tag not found`（参照に該当するオブジェクトがない、またはオブジェクトがデータタグではない）、`object to tag not found (provide 'objectUuid')`、`this kind of object cannot be tagged by a data tag`（[`getObjectTags`](#getobjecttags)の`canBeTagged`を参照）、`failed to attach the data tag to the object`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### getObjectTags

オブジェクトに関連付けられているデータタグを一覧表示します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

uuid、name、またはindexで指定したオブジェクトに関連付けられているデータタグを一覧表示し、その種類のオブジェクトにそもそもタグを付けられるかどうかも返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |

**結果**

| キー | 説明 |
|---|---|
| `object` | オブジェクトの参照（[オブジェクト参照](Common.md#object-references)を参照）。 |
| `canBeTagged` | この種類のオブジェクトにデータタグを関連付けられるかどうか。 |
| `tags` | オブジェクトに関連付けられているデータタグの参照の配列。ない場合は空です。 |

エラー：`object not found`。

### getProjectData

ファイルの表題欄のプロジェクトデータを読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

ファイルの表題欄のプロジェクトデータ、つまり物件名、施主、住所など、すべての表題欄で共有される名前付きフィールドを読み取ります。`projectData`（フィールド名と値の組）と`projectDataFieldNames`（ファイルのプロジェクトデータのフォーマットのフィールド。フォーマットの順序どおり）を返します。引数はありません。

**パラメータ**

このツールにはパラメータはありません。

**結果**

| キー | 説明 |
|---|---|
| `projectData` | プロジェクトデータのフィールド名と値の組。 |
| `projectDataFieldNames` | プロジェクトデータのフォーマットのフィールド名の配列（フォーマットの順序）。 |

エラー：`this document has no title block project data (it is created with the first title block border)`。フィールドのないプロジェクトデータの場合も、このエラーになります。

### setProjectData

ファイルの表題欄のプロジェクトデータを書き込みます。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: setProjectData" · **runToolBatch内:** はい

**詳細**

ファイルの表題欄のプロジェクトデータを書き込みます。`projectData`は、フィールド名と値の組を格納したオブジェクトです。プロジェクトデータのフォーマットにすでに存在するフィールド（getProjectDataを参照）だけが書き込まれます。その後、図面内のすべての表題欄が更新されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `projectData` | object | はい | フィールド名と値の組`{ "<field name>": value }`。プロジェクトデータのフォーマットにあるフィールド（[`getProjectData`](#getprojectdata)を参照）のみ書き込まれます。文字列でない値はJSONテキストとして保存されます。 |

**結果**

`{ "applied": { "<field name>": true or false } }`を返します。指定した各フィールドに1項目ずつ含まれます。プロジェクトデータのフォーマットにないフィールドは`false`となり、作成されません。エラー：`provide 'projectData' as an object of field name / value pairs`（引数がない、またはオブジェクトではない）。失敗した呼び出しはロールバックされます（`rolledBack`）。

## Dimensioning

> **グループ:** `Dimensioning` · **グループID:** `dimensioning` · **初期状態で有効:** いいえ · **リスクレベル:** 中 · **ツール数:** 8

**直線寸法、角度寸法、円弧長寸法、円寸法、およびセンターマークを扱います。**

直線寸法（縦横、水平、垂直、斜め、累進）、角度寸法、円弧長寸法、半径／直径寸法、およびセンターマークを使って図面を測定し、注釈を付けます。寸法はプラグインオブジェクトではなく、Vectorworks標準のオブジェクト（寸法線オブジェクト）です。ワールド座標の2点（角度寸法では頂点と2本の辺、半径寸法では中心と円）を測定し、寸法規格に従って測定値を表示します。

寸法の種類は作成時に確定します。直線寸法を角度寸法に変更することはできないため、最初に適切な作成ツールを選んでください。寸法規格（ファイルに保存されるISO/ANSI/建築/カスタムのプリセット）は、矢印の先端、寸法補助線の長さ、文字サイズ、および値の表示形式を規定します。これらの長さは用紙上の長さなので、どのレイヤ縮尺でも寸法の印刷サイズは変わりません。一方、`offset`、点の座標、および測定値には常にワールド単位を使用します。

`unit`は、値の表示形式に使用するファイルの寸法単位設定を選択します。`leaderText`/`trailerText`/`noteText`で文字を置き換えたり追加したりでき、1つ目の値の隣に補助単位の2つ目の値を表示することもできます。寸法は連動させることができます。`associate`を使用すると、寸法の端点にある図形に関連付けられ（`associateSelectedOnly`を使用すると選択オブジェクトだけに限定）、その図形が移動すると追従します。

このグループの角度はすべてラジアンです。センターマークは寸法線オブジェクトではなく、寸法クラスに配置される線分のグループなので、汎用のオブジェクトツールで読み取り、編集します。各変更は、固有の名前を持つ、取り消し可能なVectorworksの操作として実行されます。作成ツールは、設定を指定した場合、`applied`（`associate`を含め、書き込んだ設定ごとのtrue/false）も返します。

> **注:** 作成ツールは、オブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）、[`getDimension`](#getdimension)が返すのと同じ寸法の共通キー（`kind`、`start`、`end`、`offset`、`measuredLength`、およびすべての設定）、および各ツールに記載された種類固有のいくつかのキーを返します。`applied`は、設定が書き込まれた場合にのみ含まれます。`start`と`end`を一緒に指定した場合は`points`として（片方だけの場合は`start`または`end`として）報告され、`offset`とその他の各設定は名前で報告されます。`associate`は`associate`が`true`の場合にのみ報告され、`params`、半径寸法の`compact`、角度寸法の`referenceAngle`は報告されません。`createCenterMark`は`applied`を返しません。

> **注:** `applied.associate`は、`associate`を要求した場合、何も関連付けられなかったときでも常に`true`です。寸法を関連付ける呼び出しは結果を返さないためです。関連付けを確認するには、測定したオブジェクトに対して[`getObjectDimensions`](#getobjectdimensions)を呼び出してください。[`setDimension`](#setdimension)は`associate: false`に対して`false`を報告します。関連付けを解除するツールはありません。

> **注:** 引数の型はチェックされません。型が正しくない値は空の文字列、0、`false`、または点(0, 0)として読み取られ、その代替値が設定に渡されます。そのため、代替値自体が拒否されない限り（`fontSize`、`standard`、`standardIndex`、および`setDimension`ではさらに`associate`と半径寸法の`radius` / `diameter`）、設定は適用済みとして報告されます。例えば、`"leaderText": 5`は文字を消去し、`"boxText": "yes"`は`false`を書き込み、`"start": "1,2"`は点を(0, 0)に移動します。パラメータの表に示された型で送信してください。

> **注:** 単位：`startWitnessLength`、`endWitnessLength`、`startWitnessOffset`、`endWitnessOffset`、`textOffsetAlongLine`、`textOffsetAboveLine`、`tolerancePlus`、`toleranceMinus`は、`offset`と同じくワールド単位です。用紙上の長さになるのは、寸法規格が提供する値だけです。`fontSize`はポイント単位です。

> **注:** 次の値は拒否されます。何も書き込まれず、`applied`はその設定に対して`false`を報告します。0～4の範囲外の`witnessOverride`、負の`precision`または`secondaryPrecision`、0以下の`fontSize`、負の`fontStyle`、0～2の範囲外の`textRotation`、空の`standard`、0の`standardIndex`、負の`unit`、`setDimension`での0以下の半径寸法の`radius`または`diameter`、およびどの名前付きオブジェクトにもない`textStyle`の名前（`textStyle`には名前を指定し、UUIDは指定できません。また、見つかったオブジェクトが文字スタイルかどうかはチェックされません）。0～3の範囲外の`toleranceType`は書き込まれ、適用済みとして報告されますが、その寸法は以後`toleranceType`を返しません。0～3を送信してください。`textOffsetAlongLine`を設定すると、`textPositionAutomatic`もオフになります。

| ツール | 作用 | リスク | 概要 |
|---|---|---|---|
| [`createLinearDimension`](#createlineardimension) | 編集 | 中 | 縦横、水平、垂直、斜め、または累進の直線寸法を作成します。 |
| [`createAngularDimension`](#createangulardimension) | 編集 | 中 | 角度寸法を作成します。 |
| [`createArcLengthDimension`](#createarclengthdimension) | 編集 | 中 | 円弧長寸法を作成します。 |
| [`createRadialDimension`](#createradialdimension) | 編集 | 中 | 半径寸法または直径寸法を作成します。 |
| [`createCenterMark`](#createcentermark) | 編集 | 中 | 円形の部分のセンターマークを作成します。 |
| [`getDimension`](#getdimension) | 読み取り専用 | 低 | 寸法線オブジェクトの種類、測定点、値、および文字の設定を読み取ります。 |
| [`setDimension`](#setdimension) | 編集 | 中 | 寸法線オブジェクトを編集します。 |
| [`getObjectDimensions`](#getobjectdimensions) | 読み取り専用 | 低 | オブジェクトに関連付けられている寸法線オブジェクトを一覧表示します。 |

### createLinearDimension

縦横、水平、垂直、斜め、または累進の直線寸法を作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createLinearDimension" · **runToolBatch内:** はい

**詳細**

`start`と`end`の間の距離を測定する直線寸法を作成し、寸法線をそれらの点から`offset`ワールド単位離れた位置に配置します。`mode`で種類を選択します。"constrained"（縦横、デフォルト）は固定方向に投影した距離を測定します。その方向は`angle`（ラジアン）で指定し、省略するとstart → endの方向になります。"horizontal"と"vertical"は軸に平行な方向を簡単に指定するための値です。"unconstrained"（斜め）はstart → endに沿った実際の距離を測定します。"ordinate"（累進）は基準点`start`から`end`までを`angle`の方向に沿って測定します。

2点は同じ位置であってはなりません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `start` | [点](Common.md#points) | はい | 最初の測定点。ワールド単位。 |
| `end` | [点](Common.md#points) | はい | 2番目の測定点。ワールド単位。 |
| `offset` | number |  | 測定対象の図形から寸法線までの距離。ワールド単位。正の値では寸法線はstart → endの方向の左側、負の値では右側になります。 |
| `angle` | number |  | 反時計回りの角度。ラジアン。`constrained`：測定の固定方向（省略時はstart → end）。`ordinate`：測定軸の方向（省略時は0、つまり+X軸で、start → endではありません）。その他のモードでは無視されます。 |
| `mode` | string |  | 次のいずれか：`constrained`（縦横、デフォルト）、`horizontal`、`vertical`、`unconstrained`（斜め。別名として`sloped`も使用できます）、`ordinate`（累進）。その他の値は失敗します。 |
| `startWitness` | boolean |  | 最初の寸法補助線（始点の寸法補助線を表示します）。 |
| `endWitness` | boolean |  | 最後の寸法補助線（終点の寸法補助線を表示します）。 |
| `witnessOverride` | integer |  | 寸法補助線：0はなし（寸法規格に従う）、1はカスタム長さ（単一）、2はカスタム長さ（複数）、3はカスタムオフセット（単一）、4はカスタムオフセット（複数）。 |
| `startWitnessLength` | number |  | 始点の寸法補助線のカスタム長さ。 |
| `endWitnessLength` | number |  | 終点の寸法補助線のカスタム長さ。 |
| `startWitnessOffset` | number |  | 始点の寸法補助線のカスタムオフセット。 |
| `endWitnessOffset` | number |  | 終点の寸法補助線のカスタムオフセット。 |
| `arrowsInside` | boolean |  | 寸法線は常に内側（矢印を寸法補助線の内側に配置します）。 |
| `leaderLine` | boolean |  | 引出線を表示します。 |
| `showValue` | boolean |  | 測定値を表示します。 |
| `leaderText` | string |  | 前記号（値の前に表示する文字）。 |
| `trailerText` | string |  | 後記号（値の後に表示する文字）。 |
| `boxText` | boolean |  | ボックステキスト（値の周囲に枠を描画します）。 |
| `precision` | integer |  | 小数点以下の桁数。分数単位：0-6 = 1/1～1/64。角度：1は度、2は度/分、3は度/分/秒。 |
| `showSecondaryValue` | boolean |  | 補助単位の値も表示します。 |
| `secondaryLeaderText` | string |  | 補助単位の前記号（補助単位の値の前に表示する文字）。 |
| `secondaryTrailerText` | string |  | 補助単位の後記号（補助単位の値の後に表示する文字）。 |
| `secondaryBoxText` | boolean |  | 補助寸法のボックステキスト（補助単位の値の周囲に枠を描画します）。 |
| `secondaryPrecision` | integer |  | 補助単位の値の精度（`precision`と同様）。 |
| `noteText` | string |  | 寸法に追加する注記の文字。 |
| `textPositionAutomatic` | boolean |  | 文字自動位置（文字を自動配置します）。 |
| `textInside` | boolean |  | 文字を寸法補助線の内側に配置します。 |
| `textFlipped` | boolean |  | 文字を反転します。 |
| `textRotation` | integer |  | 文字の回転：0は一直線（寸法線に揃える）、1は水平、2は水平/垂直。 |
| `textOffsetAlongLine` | number |  | 寸法線に沿った文字のオフセット。 |
| `textOffsetAboveLine` | number |  | 寸法線の上方への文字のオフセット。 |
| `fontSize` | number |  | フォントサイズ。ポイント単位。 |
| `fontStyle` | integer |  | 1（ボールド）、2（イタリック）、4（アンダーライン）の合計。 |
| `textStyle` | string |  | 文字スタイルリソースの名前。なしにする場合は空の文字列。UUIDは指定できません。その名前の名前付きオブジェクトがない場合、`applied.textStyle`は`false`です。 |
| `toleranceType` | integer |  | 公差：0はなし、1は上下等公差、2は上下別公差、3は許容限界。 |
| `tolerancePlus` | number |  | 上側の公差値。 |
| `toleranceMinus` | number |  | 下側の公差値。 |
| `standard` | string |  | 寸法規格の名前。 |
| `standardIndex` | integer |  | インデックスによる寸法規格の指定。0より大きい値は組み込み、0より小さい値はカスタム。 |
| `unit` | integer |  | 0はファイルの単位。それ以外は寸法単位設定のインデックス。 |
| `associate` | boolean |  | 寸法の端点にある図形に寸法を関連付けます。結果では常に適用済みとして報告されます（[Dimensioning](#dimensioning)グループの注記を参照）。 |
| `associateSelectedOnly` | boolean |  | `associate`と併用し、選択オブジェクトのみに関連付けます。 |
| `params` | object |  | プラグインの生のパラメータ`{ "ParamName": value }`。寸法はプラグインパラメータを持たないVectorworks標準のオブジェクトなので、ここでの既知の用途はなく、作成ツールは結果を報告しません。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

**結果**

新しい寸法のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）、寸法の共通キー（[Dimensioning](#dimensioning)グループの注記を参照）、および次のキーを返します。

| キー | 説明 |
|---|---|
| `value` | 表示値。点間の距離です。縦横（拘束）寸法では、寸法線の方向に投影した値です。 |
| `direction` | 寸法線の方向。X軸からのラジアン角（斜め（非拘束）寸法の場合はstart → end）。 |
| `applied` | 書き込まれた設定ごとの結果。`start`と`end`はまとめて`points`として報告されます。 |

エラー：`unknown mode: <mode> (expected constrained, horizontal, vertical, unconstrained or ordinate)`、`failed to create the linear dimension (the two points must not coincide)`、`failed to create the dimension`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### createAngularDimension

角度寸法を作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createAngularDimension" · **runToolBatch内:** はい

**詳細**

2本の辺の間の反時計回りの角度を測定する角度寸法を`vertex`に作成し、その円弧を頂点から`offset`ワールド単位離れた位置に配置します。辺は`firstLegPoint`/`secondLegPoint`（各辺上の任意の点）で指定するか、ラジアンの`startAngle`/`endAngle`と`legLength`を組み合わせて指定します。`referenceAngle`がtrueの場合、寸法は基準方向に対する1本の辺の角度を測定し、寸法補助線を1本だけ描画します。測定値はラジアンの`value`として返されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `vertex` | [点](Common.md#points) | はい | 角度寸法：角の頂点。 |
| `firstLegPoint` | [点](Common.md#points) |  | 1本目の辺上の任意の点。 |
| `secondLegPoint` | [点](Common.md#points) |  | 2本目の辺上の任意の点。 |
| `startAngle` | number |  | 反時計回りの開始角度。ラジアン。 |
| `endAngle` | number |  | 反時計回りの終了角度。ラジアン。 |
| `legLength` | number |  | `startAngle`と`endAngle`を指定する場合の辺の長さ（ワールド単位）。デフォルトは1で、0より大きい値が必要です。 |
| `offset` | number |  | 測定対象の図形から寸法線までの距離。ワールド単位。 |
| `referenceAngle` | boolean |  | 角度寸法：基準方向に対する1本の辺の角度を測定します。 |
| `startWitness` | boolean |  | 最初の寸法補助線（始点の寸法補助線を表示します）。 |
| `endWitness` | boolean |  | 最後の寸法補助線（終点の寸法補助線を表示します）。 |
| `witnessOverride` | integer |  | 寸法補助線：0はなし（寸法規格に従う）、1はカスタム長さ（単一）、2はカスタム長さ（複数）、3はカスタムオフセット（単一）、4はカスタムオフセット（複数）。 |
| `startWitnessLength` | number |  | 始点の寸法補助線のカスタム長さ。 |
| `endWitnessLength` | number |  | 終点の寸法補助線のカスタム長さ。 |
| `startWitnessOffset` | number |  | 始点の寸法補助線のカスタムオフセット。 |
| `endWitnessOffset` | number |  | 終点の寸法補助線のカスタムオフセット。 |
| `arrowsInside` | boolean |  | 寸法線は常に内側（矢印を寸法補助線の内側に配置します）。 |
| `leaderLine` | boolean |  | 引出線を表示します。 |
| `showValue` | boolean |  | 測定値を表示します。 |
| `leaderText` | string |  | 前記号（値の前に表示する文字）。 |
| `trailerText` | string |  | 後記号（値の後に表示する文字）。 |
| `boxText` | boolean |  | ボックステキスト（値の周囲に枠を描画します）。 |
| `precision` | integer |  | 小数点以下の桁数。分数単位：0-6 = 1/1～1/64。角度：1は度、2は度/分、3は度/分/秒。 |
| `showSecondaryValue` | boolean |  | 補助単位の値も表示します。 |
| `secondaryLeaderText` | string |  | 補助単位の前記号（補助単位の値の前に表示する文字）。 |
| `secondaryTrailerText` | string |  | 補助単位の後記号（補助単位の値の後に表示する文字）。 |
| `secondaryBoxText` | boolean |  | 補助寸法のボックステキスト（補助単位の値の周囲に枠を描画します）。 |
| `secondaryPrecision` | integer |  | 補助単位の値の精度（`precision`と同様）。 |
| `noteText` | string |  | 寸法に追加する注記の文字。 |
| `textPositionAutomatic` | boolean |  | 文字自動位置（文字を自動配置します）。 |
| `textInside` | boolean |  | 文字を寸法補助線の内側に配置します。 |
| `textFlipped` | boolean |  | 文字を反転します。 |
| `textRotation` | integer |  | 文字の回転：0は一直線（寸法線に揃える）、1は水平、2は水平/垂直。 |
| `textOffsetAlongLine` | number |  | 寸法線に沿った文字のオフセット。 |
| `textOffsetAboveLine` | number |  | 寸法線の上方への文字のオフセット。 |
| `fontSize` | number |  | フォントサイズ。ポイント単位。 |
| `fontStyle` | integer |  | 1（ボールド）、2（イタリック）、4（アンダーライン）の合計。 |
| `textStyle` | string |  | 文字スタイルリソースの名前。なしにする場合は空の文字列。UUIDは指定できません。その名前の名前付きオブジェクトがない場合、`applied.textStyle`は`false`です。 |
| `toleranceType` | integer |  | 公差：0はなし、1は上下等公差、2は上下別公差、3は許容限界。 |
| `tolerancePlus` | number |  | 上側の公差値。 |
| `toleranceMinus` | number |  | 下側の公差値。 |
| `standard` | string |  | 寸法規格の名前。 |
| `standardIndex` | integer |  | インデックスによる寸法規格の指定。0より大きい値は組み込み、0より小さい値はカスタム。 |
| `unit` | integer |  | 0はファイルの単位。それ以外は寸法単位設定のインデックス。 |
| `associate` | boolean |  | 寸法の端点にある図形に寸法を関連付けます。結果では常に適用済みとして報告されます（[Dimensioning](#dimensioning)グループの注記を参照）。 |
| `associateSelectedOnly` | boolean |  | `associate`と併用し、選択オブジェクトのみに関連付けます。 |
| `params` | object |  | プラグインの生のパラメータ`{ "ParamName": value }`。寸法はプラグインパラメータを持たないVectorworks標準のオブジェクトなので、ここでの既知の用途はなく、作成ツールは結果を報告しません。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

辺は`startAngle`と`endAngle`の組、または`firstLegPoint`と`secondLegPoint`の組で指定します。角度が両方ある場合は角度が使用されます。片方だけの場合、またはどちらもない場合は、辺上の点が使用されます。

**結果**

新しい寸法のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）、寸法の共通キー（[Dimensioning](#dimensioning)グループの注記を参照。`start`と`end`は2本の辺上の点です）、および次のキーを返します。

| キー | 説明 |
|---|---|
| `vertex` | 頂点（ワールド単位）。 |
| `startAngle` | 測定した角度の開始角（ラジアン）。 |
| `endAngle` | 測定した角度の終了角（ラジアン）。 |
| `value` | 測定した角度。1本目の辺から2本目の辺への反時計回りのラジアン角で、範囲は[0, 2π)です。 |
| `referenceAngle` | 寸法が基準方向に対して測定するかどうか。 |
| `applied` | 書き込まれた設定ごとの結果。 |

エラー：`failed to create the angular dimension (the vertex and the two leg points must be distinct)`（`legLength`が0以下の場合も含む）、`failed to create the dimension`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### createArcLengthDimension

円弧長寸法を作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createArcLengthDimension" · **runToolBatch内:** はい

**詳細**

円弧に沿った長さを測定する円弧長寸法を作成し、寸法の円弧を測定対象の円弧の外側に`offset`ワールド単位離して配置します。円弧は`start`、`end`、`center`で指定するか（点の間にある2つの円弧のどちらを測定するかは`clockwise`で選択）、`center`、`radius`、およびラジアンの`startAngle`と`sweepAngle`で指定します（円弧角が負の場合は時計回り）。

`witnessPerpendicularToChord`は、寸法補助線を半径方向ではなく弦に垂直に描画します。`arcIndicator`（デフォルトはtrue）は、値の前に円弧インジケータを表示します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `start` | [点](Common.md#points) |  | 最初の測定点。ワールド単位。`end`および`center`と組み合わせて使用します。 |
| `end` | [点](Common.md#points) |  | 2番目の測定点。ワールド単位。`start`および`center`と組み合わせて使用します。 |
| `center` | [点](Common.md#points) | はい | 円弧の中心（ワールド単位）。 |
| `radius` | number |  | 半径（ワールド単位）。0より大きい値が必要です。`startAngle`および`sweepAngle`と組み合わせて使用します。 |
| `startAngle` | number |  | 反時計回りの開始角度。ラジアン。 |
| `sweepAngle` | number |  | 円弧角（ラジアン）。正の値は反時計回り、負の値は時計回りです。0は指定できません。 |
| `offset` | number |  | 測定対象の図形から寸法線までの距離。ワールド単位。 |
| `clockwise` | boolean |  | `start`、`end`、`center`と組み合わせて使用し、点の間の時計回りの円弧を測定します。 |
| `witnessPerpendicularToChord` | boolean |  | 寸法補助線を半径方向ではなく弦に垂直に描画します。デフォルトはfalse。 |
| `arcIndicator` | boolean |  | 値の前に円弧インジケータを表示します。デフォルトはtrue。 |
| `startWitness` | boolean |  | 最初の寸法補助線（始点の寸法補助線を表示します）。 |
| `endWitness` | boolean |  | 最後の寸法補助線（終点の寸法補助線を表示します）。 |
| `witnessOverride` | integer |  | 寸法補助線：0はなし（寸法規格に従う）、1はカスタム長さ（単一）、2はカスタム長さ（複数）、3はカスタムオフセット（単一）、4はカスタムオフセット（複数）。 |
| `startWitnessLength` | number |  | 始点の寸法補助線のカスタム長さ。 |
| `endWitnessLength` | number |  | 終点の寸法補助線のカスタム長さ。 |
| `startWitnessOffset` | number |  | 始点の寸法補助線のカスタムオフセット。 |
| `endWitnessOffset` | number |  | 終点の寸法補助線のカスタムオフセット。 |
| `arrowsInside` | boolean |  | 寸法線は常に内側（矢印を寸法補助線の内側に配置します）。 |
| `leaderLine` | boolean |  | 引出線を表示します。 |
| `showValue` | boolean |  | 測定値を表示します。 |
| `leaderText` | string |  | 前記号（値の前に表示する文字）。 |
| `trailerText` | string |  | 後記号（値の後に表示する文字）。 |
| `boxText` | boolean |  | ボックステキスト（値の周囲に枠を描画します）。 |
| `precision` | integer |  | 小数点以下の桁数。分数単位：0-6 = 1/1～1/64。角度：1は度、2は度/分、3は度/分/秒。 |
| `showSecondaryValue` | boolean |  | 補助単位の値も表示します。 |
| `secondaryLeaderText` | string |  | 補助単位の前記号（補助単位の値の前に表示する文字）。 |
| `secondaryTrailerText` | string |  | 補助単位の後記号（補助単位の値の後に表示する文字）。 |
| `secondaryBoxText` | boolean |  | 補助寸法のボックステキスト（補助単位の値の周囲に枠を描画します）。 |
| `secondaryPrecision` | integer |  | 補助単位の値の精度（`precision`と同様）。 |
| `noteText` | string |  | 寸法に追加する注記の文字。 |
| `textPositionAutomatic` | boolean |  | 文字自動位置（文字を自動配置します）。 |
| `textInside` | boolean |  | 文字を寸法補助線の内側に配置します。 |
| `textFlipped` | boolean |  | 文字を反転します。 |
| `textRotation` | integer |  | 文字の回転：0は一直線（寸法線に揃える）、1は水平、2は水平/垂直。 |
| `textOffsetAlongLine` | number |  | 寸法線に沿った文字のオフセット。 |
| `textOffsetAboveLine` | number |  | 寸法線の上方への文字のオフセット。 |
| `fontSize` | number |  | フォントサイズ。ポイント単位。 |
| `fontStyle` | integer |  | 1（ボールド）、2（イタリック）、4（アンダーライン）の合計。 |
| `textStyle` | string |  | 文字スタイルリソースの名前。なしにする場合は空の文字列。UUIDは指定できません。その名前の名前付きオブジェクトがない場合、`applied.textStyle`は`false`です。 |
| `toleranceType` | integer |  | 公差：0はなし、1は上下等公差、2は上下別公差、3は許容限界。 |
| `tolerancePlus` | number |  | 上側の公差値。 |
| `toleranceMinus` | number |  | 下側の公差値。 |
| `standard` | string |  | 寸法規格の名前。 |
| `standardIndex` | integer |  | インデックスによる寸法規格の指定。0より大きい値は組み込み、0より小さい値はカスタム。 |
| `unit` | integer |  | 0はファイルの単位。それ以外は寸法単位設定のインデックス。 |
| `associate` | boolean |  | 寸法の端点にある図形に寸法を関連付けます。結果では常に適用済みとして報告されます（[Dimensioning](#dimensioning)グループの注記を参照）。 |
| `associateSelectedOnly` | boolean |  | `associate`と併用し、選択オブジェクトのみに関連付けます。 |
| `params` | object |  | プラグインの生のパラメータ`{ "ParamName": value }`。寸法はプラグインパラメータを持たないVectorworks標準のオブジェクトなので、ここでの既知の用途はなく、作成ツールは結果を報告しません。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

`radius`、`startAngle`、`sweepAngle`がすべて指定されている場合は、円弧の2番目の形式（`center`、`radius`、`startAngle`、`sweepAngle`）が使用されます。それ以外の場合は1番目の形式（`start`、`end`、`center`）が使用され、欠落している点は(0, 0)として扱われます。

**結果**

新しい寸法のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）、寸法の共通キー（[Dimensioning](#dimensioning)グループの注記を参照）、および次のキーを返します。

| キー | 説明 |
|---|---|
| `center` | 円弧の中心（ワールド単位）。 |
| `radius` | 円弧の半径（ワールド単位）。 |
| `startAngle` | 測定した円弧の開始角（ラジアン）。 |
| `sweepAngle` | 測定した円弧の符号付きの円弧角（ラジアン、負の値は時計回り）。 |
| `value` | 表示値。円弧に沿った長さ（ワールド単位）。 |
| `applied` | 書き込まれた設定ごとの結果。 |

エラー：`failed to create the arc length dimension (provide either 'start', 'end' and 'center', or 'center', 'radius', 'startAngle' and 'sweepAngle')`（`radius`が0以下の場合や`sweepAngle`が0の場合も含む）、`failed to create the dimension`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### createRadialDimension

半径寸法または直径寸法を作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createRadialDimension" · **runToolBatch内:** はい

**詳細**

`center`を中心とする円の半径寸法を作成し、その引出線を円の外側に`offset`ワールド単位離して配置します。`mode`が"radial"（デフォルト）の場合は半径を表示し、"diametrical"の場合は円を横切る直径を表示します。円は、`radius`（または`diameter`）と、引出線が中心から伸びる方向を示すラジアンの`angle`で指定するか、引出線が指す`pointOnCircle`で指定します。`compact`は、中心まで伸ばさずに円周で止まる短縮形式の半径寸法を描画します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `center` | [点](Common.md#points) | はい | 円の中心（ワールド単位）。 |
| `radius` | number |  | 半径（ワールド単位）。0より大きい値が必要です。`diameter`または`pointOnCircle`を指定した場合は無視されます。 |
| `diameter` | number |  | 直径（ワールド単位）。その半分が半径になります。`radius`より優先されます。`pointOnCircle`を指定した場合は無視されます。 |
| `angle` | number |  | 引出線が中心から伸びる方向の、反時計回りの角度（ラジアン）。デフォルトは0。`pointOnCircle`を指定した場合は無視されます。 |
| `pointOnCircle` | [点](Common.md#points) |  | 引出線が指す円上の点（ワールド単位）。`radius`、`diameter`、`angle`より優先されます。 |
| `offset` | number |  | 測定対象の図形から寸法線までの距離。ワールド単位。 |
| `compact` | boolean |  | 半径寸法：寸法線をコンパクト表示（円周で止まる短縮形式）。寸法の作成後に設定され、結果には報告されません。 |
| `mode` | string |  | 次のいずれか：`radial`（デフォルト）、`diametrical`。`radius`と`diameter`も、それぞれ`radial`と`diametrical`の別名として使用できます。その他の値は失敗します。 |
| `startWitness` | boolean |  | 最初の寸法補助線（始点の寸法補助線を表示します）。 |
| `endWitness` | boolean |  | 最後の寸法補助線（終点の寸法補助線を表示します）。 |
| `witnessOverride` | integer |  | 寸法補助線：0はなし（寸法規格に従う）、1はカスタム長さ（単一）、2はカスタム長さ（複数）、3はカスタムオフセット（単一）、4はカスタムオフセット（複数）。 |
| `startWitnessLength` | number |  | 始点の寸法補助線のカスタム長さ。 |
| `endWitnessLength` | number |  | 終点の寸法補助線のカスタム長さ。 |
| `startWitnessOffset` | number |  | 始点の寸法補助線のカスタムオフセット。 |
| `endWitnessOffset` | number |  | 終点の寸法補助線のカスタムオフセット。 |
| `arrowsInside` | boolean |  | 寸法線は常に内側（矢印を寸法補助線の内側に配置します）。 |
| `leaderLine` | boolean |  | 引出線を表示します。 |
| `showValue` | boolean |  | 測定値を表示します。 |
| `leaderText` | string |  | 前記号（値の前に表示する文字）。 |
| `trailerText` | string |  | 後記号（値の後に表示する文字）。 |
| `boxText` | boolean |  | ボックステキスト（値の周囲に枠を描画します）。 |
| `precision` | integer |  | 小数点以下の桁数。分数単位：0-6 = 1/1～1/64。角度：1は度、2は度/分、3は度/分/秒。 |
| `showSecondaryValue` | boolean |  | 補助単位の値も表示します。 |
| `secondaryLeaderText` | string |  | 補助単位の前記号（補助単位の値の前に表示する文字）。 |
| `secondaryTrailerText` | string |  | 補助単位の後記号（補助単位の値の後に表示する文字）。 |
| `secondaryBoxText` | boolean |  | 補助寸法のボックステキスト（補助単位の値の周囲に枠を描画します）。 |
| `secondaryPrecision` | integer |  | 補助単位の値の精度（`precision`と同様）。 |
| `noteText` | string |  | 寸法に追加する注記の文字。 |
| `textPositionAutomatic` | boolean |  | 文字自動位置（文字を自動配置します）。 |
| `textInside` | boolean |  | 文字を寸法補助線の内側に配置します。 |
| `textFlipped` | boolean |  | 文字を反転します。 |
| `textRotation` | integer |  | 文字の回転：0は一直線（寸法線に揃える）、1は水平、2は水平/垂直。 |
| `textOffsetAlongLine` | number |  | 寸法線に沿った文字のオフセット。 |
| `textOffsetAboveLine` | number |  | 寸法線の上方への文字のオフセット。 |
| `fontSize` | number |  | フォントサイズ。ポイント単位。 |
| `fontStyle` | integer |  | 1（ボールド）、2（イタリック）、4（アンダーライン）の合計。 |
| `textStyle` | string |  | 文字スタイルリソースの名前。なしにする場合は空の文字列。UUIDは指定できません。その名前の名前付きオブジェクトがない場合、`applied.textStyle`は`false`です。 |
| `toleranceType` | integer |  | 公差：0はなし、1は上下等公差、2は上下別公差、3は許容限界。 |
| `tolerancePlus` | number |  | 上側の公差値。 |
| `toleranceMinus` | number |  | 下側の公差値。 |
| `standard` | string |  | 寸法規格の名前。 |
| `standardIndex` | integer |  | インデックスによる寸法規格の指定。0より大きい値は組み込み、0より小さい値はカスタム。 |
| `unit` | integer |  | 0はファイルの単位。それ以外は寸法単位設定のインデックス。 |
| `associate` | boolean |  | 寸法の端点にある図形に寸法を関連付けます。結果では常に適用済みとして報告されます（[Dimensioning](#dimensioning)グループの注記を参照）。 |
| `associateSelectedOnly` | boolean |  | `associate`と併用し、選択オブジェクトのみに関連付けます。 |
| `params` | object |  | プラグインの生のパラメータ`{ "ParamName": value }`。寸法はプラグインパラメータを持たないVectorworks標準のオブジェクトなので、ここでの既知の用途はなく、作成ツールは結果を報告しません。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

円は、`pointOnCircle`、または`radius`か`diameter`と`angle`の組み合わせで指定します。`pointOnCircle`がある場合はそれが優先されます。それ以外の場合は`diameter`が`radius`より優先され、`angle`のデフォルトは0です。

**結果**

新しい寸法のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）、寸法の共通キー（[Dimensioning](#dimensioning)グループの注記を参照）、および次のキーを返します。

| キー | 説明 |
|---|---|
| `diametrical` | 直径寸法の場合は`true`。 |
| `center` | 円の中心（ワールド単位）。 |
| `radius` | 半径（ワールド単位）。 |
| `diameter` | 直径（ワールド単位）。 |
| `angle` | 寸法を描画する方向。X軸からのラジアン角。 |
| `value` | 表示値。直径寸法の場合は直径、それ以外は半径。 |
| `applied` | 書き込まれた設定ごとの結果。 |

エラー：`unknown mode: <mode> (expected radial or diametrical)`、`failed to create the radial dimension (provide 'center' plus 'radius' / 'diameter' and 'angle', or 'center' plus 'pointOnCircle'; the radius must not be zero)`、`failed to create the dimension`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### createCenterMark

円形の部分のセンターマークを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createCenterMark" · **runToolBatch内:** はい

**詳細**

センターマーク、つまり円形の部分の中心を示す十字（必要に応じて4本の延長線分付き）を作成します。これは寸法クラスに配置される線のグループであり、寸法線オブジェクトではありません。既存オブジェクトのバウンディングボックスの中心を示すには`objectUuid`を指定し、それ以外の場合は`center`と円形部分の`radius`を指定します。サイズを明示しない場合、十字、隙間、延長線分の長さはアクティブな寸法規格から取得され、レイヤの縮尺に合わせて調整されます。

`spokeLength`、`gap`、`extension`は、これらをワールド単位の長さで上書きします。円が小さすぎて延長線分を描けない場合、延長線分は省略されます。

> **注:** グループが寸法クラスに配置されるのは、ファイル設定の「寸法を指定クラスに作成する」がオンの場合だけです。それ以外の場合は、アクティブクラスに配置されます。作成オプションの`class`は、どちらよりも優先されます。`spokeLength`を指定しない場合、サイズは寸法規格から取得されます。延長線分が描画されるのは、`radius`が0より大きく、`spokeLength`と`gap`の合計が`radius`より小さい場合だけです。センターマークは寸法線オブジェクトではないため、[`getDimension`](#getdimension)と[`setDimension`](#setdimension)では扱えません。[`editObject`](ObjectPrimitives.md#editobject)で編集してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `center` | [点](Common.md#points) |  | 円形部分の中心（ワールド単位）。デフォルトは(0, 0)。`objectUuid`を指定した場合は無視されます。 |
| `radius` | number |  | 円形部分の半径（ワールド単位）。デフォルトは0で、その場合は十字だけになります。`objectUuid`を指定した場合は無視され、半径はオブジェクトのバウンディングボックスの短い辺の半分になります。 |
| `objectUuid` | string |  | マークを付けるオブジェクトのUUID。マークはそのバウンディングボックスの中心に配置されます。この場合、`center`、`radius`、`spokeLength`、`gap`、`extension`は無視されます。不明なUUIDを指定すると失敗します。 |
| `spokeLength` | number |  | 十字の中心から各腕の端までの長さ（ワールド単位）。十字全体の長さはその2倍です。0より大きい値が必要です。指定しない場合、`gap`と`extension`は無視されます。 |
| `gap` | number |  | 腕の端と延長線分の始点との間隔（ワールド単位）。`spokeLength`を指定した場合にのみ使用されます。値がない場合は0として扱われます。 |
| `extension` | number |  | 延長線分が円を越えて伸びる長さ（ワールド単位）。`spokeLength`を指定した場合にのみ使用されます。値がない場合は0として扱われます。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

**結果**

新しいグループのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と次のキーを返します。

| キー | 説明 |
|---|---|
| `center` | マークの中心（ワールド単位）。 |
| `segmentCount` | グループ内の線分の数。十字のみの場合は2、4本の延長線分がある場合は6。 |

`applied`は返されません。エラー：`object to mark not found`（不明な`objectUuid`）、`failed to create the center mark`（`spokeLength`が0以下の場合など）。失敗した呼び出しはロールバックされます（`rolledBack`）。

### getDimension

寸法線オブジェクトの種類、測定点、値、および文字の設定を読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

uuid、name、またはindexで寸法線オブジェクトを読み取ります。`kind`（constrainedLinear、unconstrainedLinear、ordinate、radial、diametrical、angular、arcLength）、測定点、`offset`と`measuredLength`、寸法補助線と矢印の設定、主単位と補助単位の両方の値について表示する文字と精度、文字の配置とフォント、公差、寸法規格と単位設定（setDimensionと同じ整数コード）、および種類固有のフィールドを返します。種類固有のフィールドは、直線寸法では`value`と`direction`、角度寸法では`vertex`/`startAngle`/`endAngle`、円弧長寸法では`center`/`radius`/`sweepAngle`、半径寸法では`center`/`radius`/`diameter`/`angle`です。

角度はすべてラジアンです。センターマークは識別用の印がないグループなので、このクエリでは識別できません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |

**結果**

寸法のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と以下のキーを返します。値を読み取れないキーは省略されます。

| キー | 説明 |
|---|---|
| `kind` | `constrainedLinear`、`unconstrainedLinear`、`ordinate`、`radial`、`diametrical`、`angular`、`arcLength`、`unknown`のいずれか。 |
| `start`、`end` | 測定点（ワールド単位）。角度寸法では2本の辺上の点、半径寸法または直径寸法では`start`が中心で`end`が円上の点、円弧長寸法では円弧上の2点です。 |
| `offset` | 測定点と寸法線の間隔（ワールド単位）。正の値では寸法線はstart → endの方向の左側、負の値では右側にあります。 |
| `measuredLength` | `start`と`end`の直線距離（ワールド単位）。縦横（拘束）の直線寸法では、この距離をその方向に投影した値が表示されます（`value`を参照）。 |
| 寸法の設定 | [`setDimension`](#setdimension)が書き込む各設定を、そのパラメータ名で返します：`startWitness`、`endWitness`、`witnessOverride`、`startWitnessLength`、`endWitnessLength`、`startWitnessOffset`、`endWitnessOffset`、`arrowsInside`、`leaderLine`、`showValue`、`leaderText`、`trailerText`、`boxText`、`precision`、`showSecondaryValue`、`secondaryLeaderText`、`secondaryTrailerText`、`secondaryBoxText`、`secondaryPrecision`、`noteText`、`textPositionAutomatic`、`textInside`、`textFlipped`、`textRotation`、`textOffsetAlongLine`、`textOffsetAboveLine`、`fontSize`、`fontStyle`、`textStyle`、`toleranceType`、`tolerancePlus`、`toleranceMinus`、`standard`、`standardIndex`、`unit`。`textStyle`は文字スタイルの名前です（なしの場合、またはスタイルが見つからない場合は空の文字列）。`witnessOverride`、`precision`、`secondaryPrecision`、`textRotation`、`fontStyle`、`toleranceType`、`standardIndex`、`unit`は、[`setDimension`](#setdimension)と同じ整数コードです。 |
| 直線寸法 | `constrained`（真偽値）、`direction`（ラジアン）、`value`（寸法線の方向に投影した測定距離、ワールド単位）。 |
| 角度寸法 | `vertex`、`startAngle`と`endAngle`（ラジアン）、`value`（ラジアン。1本目の辺から2本目の辺への反時計回りで、0以上2π未満）、`referenceAngle`。 |
| 円弧長寸法 | `center`、`radius`、`startAngle`、`sweepAngle`（ラジアン。負の値は時計回り）、`value`（円弧に沿った長さ、ワールド単位）、`clockwise`、`witnessPerpendicularToChord`、`arcIndicator`。 |
| 半径寸法 | `diametrical`、`center`、`radius`、`diameter`、`angle`（X軸からのラジアン角）、`value`（直径寸法では直径、それ以外は半径）、`compact`。 |

エラー：`object not found`、`not a dimension object`（センターマークは線のグループなので認識されません）。

### setDimension

寸法線オブジェクトを編集します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: setDimension" · **runToolBatch内:** はい

**詳細**

uuid、name、またはindexで寸法線オブジェクトを編集します。測定点`start`/`end`、`offset`、寸法補助線、`arrowsInside`/`leaderLine`、表示する文字（`showValue`、`leaderText`、`trailerText`、`boxText`、`precision`と、それぞれに対応する'secondary\*'の設定、`noteText`）、文字の配置とフォント、公差、`standard`、`unit`など、すべての共通設定を書き込めます。

**整数コード：** `witnessOverride`は0がなし（寸法規格に従う）、1がカスタム長さ（単一）、2がカスタム長さ（複数）、3がカスタムオフセット（単一）、4がカスタムオフセット（複数）。`precision`は小数点以下の桁数（分数単位：0-6 = 1/1-1/64。角度：1は度、2は度/分、3は度/分/秒）。`textRotation`は0が一直線（寸法線に揃える）、1が水平、2が水平/垂直。`fontStyle`は1（ボールド）、2（イタリック）、4（アンダーライン）の合計（`fontSize`はポイント単位）。`toleranceType`は0がなし、1が上下等公差、2が上下別公差、3が許容限界。`standardIndex`は&gt; 0が組み込み、&lt; 0がカスタムの寸法規格。`unit`は0がファイルの単位、それ以外は寸法単位設定のインデックス。

**種類固有のフィールド：** 直線寸法では`direction`（ラジアン）、角度寸法では`vertex`と`referenceAngle`、半径寸法では`center`/`radius`/`diameter`/`angle`/`compact`。`associate`: trueは、寸法の端点にある図形に寸法を関連付けます（`associateSelectedOnly`を使用すると選択オブジェクトだけに限定されます。関連付けは解除できません）。寸法の種類は変更できません。`params`オブジェクトでプラグインの生のパラメータを設定します。

> **注:** 寸法の種類に属さない種類固有のフィールド（直線寸法に対する`vertex`など）は無視され、`applied`にも含まれません。円弧長寸法には種類固有のフィールドはありません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `start` | [点](Common.md#points) |  | 最初の測定点（ワールド単位）。角度寸法では辺上の点、半径寸法または直径寸法では中心（`end`は円上の点）、円弧長寸法では円弧上の点です。`end`と一緒に指定すると両方が同時に設定され、`points`として報告されます。 |
| `end` | [点](Common.md#points) |  | 2番目の測定点（ワールド単位）。`start`を参照してください。 |
| `offset` | number |  | 測定点と寸法線の間隔（ワールド単位）。正の値では寸法線はstart → endの方向の左側、負の値では右側にあります。 |
| `startWitness` | boolean |  | 最初の寸法補助線（始点の寸法補助線を表示します）。 |
| `endWitness` | boolean |  | 最後の寸法補助線（終点の寸法補助線を表示します）。 |
| `witnessOverride` | integer |  | 寸法補助線：0はなし（寸法規格に従う）、1はカスタム長さ（単一）、2はカスタム長さ（複数）、3はカスタムオフセット（単一）、4はカスタムオフセット（複数）。 |
| `startWitnessLength` | number |  | 始点の寸法補助線のカスタム長さ。 |
| `endWitnessLength` | number |  | 終点の寸法補助線のカスタム長さ。 |
| `startWitnessOffset` | number |  | 始点の寸法補助線のカスタムオフセット。 |
| `endWitnessOffset` | number |  | 終点の寸法補助線のカスタムオフセット。 |
| `arrowsInside` | boolean |  | 寸法線は常に内側（矢印を寸法補助線の内側に配置します）。 |
| `leaderLine` | boolean |  | 引出線を表示します。 |
| `showValue` | boolean |  | 測定値を表示します。 |
| `leaderText` | string |  | 前記号（値の前に表示する文字）。 |
| `trailerText` | string |  | 後記号（値の後に表示する文字）。 |
| `boxText` | boolean |  | ボックステキスト（値の周囲に枠を描画します）。 |
| `precision` | integer |  | 小数点以下の桁数。分数単位：0-6 = 1/1～1/64。角度：1は度、2は度/分、3は度/分/秒。 |
| `showSecondaryValue` | boolean |  | 補助単位の値も表示します。 |
| `secondaryLeaderText` | string |  | 補助単位の前記号（補助単位の値の前に表示する文字）。 |
| `secondaryTrailerText` | string |  | 補助単位の後記号（補助単位の値の後に表示する文字）。 |
| `secondaryBoxText` | boolean |  | 補助寸法のボックステキスト（補助単位の値の周囲に枠を描画します）。 |
| `secondaryPrecision` | integer |  | 補助単位の値の精度（`precision`と同様）。 |
| `noteText` | string |  | 寸法に追加する注記の文字。 |
| `textPositionAutomatic` | boolean |  | 文字自動位置（文字を自動配置します）。 |
| `textInside` | boolean |  | 文字を寸法補助線の内側に配置します。 |
| `textFlipped` | boolean |  | 文字を反転します。 |
| `textRotation` | integer |  | 文字の回転：0は一直線（寸法線に揃える）、1は水平、2は水平/垂直。 |
| `textOffsetAlongLine` | number |  | 寸法線に沿った文字のオフセット。 |
| `textOffsetAboveLine` | number |  | 寸法線の上方への文字のオフセット。 |
| `fontSize` | number |  | フォントサイズ。ポイント単位。 |
| `fontStyle` | integer |  | 1（ボールド）、2（イタリック）、4（アンダーライン）の合計。 |
| `textStyle` | string |  | 文字スタイルリソースの名前。なしにする場合は空の文字列。UUIDは指定できません。その名前の名前付きオブジェクトがない場合、`applied.textStyle`は`false`です。 |
| `toleranceType` | integer |  | 公差：0はなし、1は上下等公差、2は上下別公差、3は許容限界。 |
| `tolerancePlus` | number |  | 上側の公差値。 |
| `toleranceMinus` | number |  | 下側の公差値。 |
| `standard` | string |  | 寸法規格の名前。 |
| `standardIndex` | integer |  | インデックスによる寸法規格の指定。0より大きい値は組み込み、0より小さい値はカスタム。 |
| `unit` | integer |  | 0はファイルの単位。それ以外は寸法単位設定のインデックス。 |
| `associate` | boolean |  | `true`は、寸法の端点にある図形に寸法を関連付けます。`false`は何もせず、`false`として報告されます。関連付けを解除するツールはありません。関連付けを要求した場合は常に`true`が報告されます（グループの注記を参照）。 |
| `associateSelectedOnly` | boolean |  | `associate`と併用し、選択オブジェクトのみに関連付けます。 |
| `direction` | number |  | 直線寸法：測定方向（ラジアン）。 |
| `vertex` | [点](Common.md#points) |  | 角度寸法：角の頂点。 |
| `referenceAngle` | boolean |  | 角度寸法：基準方向に対する1本の辺の角度を測定します。 |
| `center` | [点](Common.md#points) |  | 半径寸法：円の中心（`start`の点、ワールド単位）。中心だけを移動し、円上の点は動かないため、半径と角度が変わります。`radius`または`diameter`と`angle`を一緒に指定してください。`start`と`end`の後に書き込まれます。 |
| `radius` | number |  | 半径寸法：半径（ワールド単位）。0より大きい値（それ以外は`false`）。 |
| `diameter` | number |  | 半径寸法：直径（ワールド単位）。`radius`の後に適用されるため、両方を指定すると直径が最後に書き込まれる値になります。0より大きい値（それ以外は`false`）。 |
| `angle` | number |  | 半径寸法：寸法を描画する方向。X軸からのラジアン角。 |
| `compact` | boolean |  | 半径寸法：寸法線をコンパクト表示（円周で止まる短縮形式）。 |
| `params` | object |  | プラグインの生のパラメータ`{ "ParamName": value }`。寸法はプラグインパラメータを持たないVectorworks標準のオブジェクトなので、ここで設定できる既知のパラメータはありません。結果はパラメータ名ごとに`applied.params`で報告されます。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |

**結果**

| キー | 説明 |
|---|---|
| `applied` | 常に含まれ、設定が指定されていない場合は空です。指定された設定ごとに1項目あり、書き込まれた場合は`true`、拒否された場合は`false`です（グループの注記を参照）。`start`と`end`を一緒に指定した場合は`points`として、片方だけの場合は`start`または`end`として報告されます。`params`は、パラメータ名ごとに`true`または`false`を持つネストしたオブジェクトです。 |

結果にはオブジェクト参照は含まれません。エラー：`object not found`、`not a dimension object (a center mark is a group of lines - edit it with editObject)`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### getObjectDimensions

オブジェクトに関連付けられている寸法線オブジェクトを一覧表示します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

uuid、name、またはindexで指定したオブジェクトに関連付けられている寸法、つまりそのオブジェクトが移動したりサイズを変更したりしたときに追従する寸法を一覧表示します。一覧の各寸法には`kind`（getDimensionと同じ）が含まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |

**結果**

| キー | 説明 |
|---|---|
| `object` | 対象オブジェクトのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）。 |
| `dimensions` | 関連付けられている寸法ごとに1項目：そのオブジェクト参照と`kind`（[`getDimension`](#getdimension)と同じ形式）。関連付けられている寸法がない場合は空です。ページ分割はありません。 |

このツールは、関連付け（`associate`を参照）によってオブジェクトに結び付けられている寸法を一覧表示します。壁に挿入されたプラグインオブジェクトの場合は、そのオブジェクトが壁に作る切り欠きに結び付けられた寸法も一覧表示します。エラー：`object not found`。
