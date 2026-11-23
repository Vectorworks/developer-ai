[English](../../MCP/v2027.2/ObjectsLandmark.md) • [Deutsch](../../MCP.de/v2027.2/ObjectsLandmark.md) • **日本語**

# ObjectsLandmark — 敷地とランドスケープ

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

敷地とランドスケープのオブジェクト（植栽、舗床、ランドスケープエリア、地形モデル、造成図形、レベルオブジェクト、境界線、既存樹木）のためのツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [Landmark](#landmark)
  - [createPlant](#createplant)
  - [createHardscape](#createhardscape)
  - [createLandscapeArea](#createlandscapearea)
  - [createSiteModifier](#createsitemodifier)
  - [createPropertyLine](#createpropertyline)
  - [createSiteModel](#createsitemodel)
  - [createStake](#createstake)
  - [createExistingTree](#createexistingtree)
  - [getLandmarkObject](#getlandmarkobject)
  - [setLandmarkObject](#setlandmarkobject)

<a id="overview"></a>

## 概要

このフォルダには1個のツールグループがあり、合計10個のツールが含まれています。

| グループ | グループID | 初期状態で有効 | 安全性レベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [Landmark](#landmark) | `landmark` | いいえ | 中 | 10 | 植栽、舗床、ランドスケープエリア、地形モデル、造成図形、レベルオブジェクト、境界線、既存樹木。 |

## Landmark

> **グループ:** `Landmark` · **グループID:** `landmark` · **初期状態で有効:** いいえ · **安全性レベル:** 中 · **ツール数:** 10

**植栽、舗床、ランドスケープエリア、地形モデル、造成図形、レベルオブジェクト、境界線、既存樹木。**

敷地とランドスケープのオブジェクト（植栽、舗床、ランドスケープエリア、地形モデル、造成図形、レベルオブジェクト、境界線、既存樹木）を、型付きの設定や面積／体積の読み取り値も含めて作成、確認、編集します。パスベースのオブジェクトは、既存の多角形／曲線から作成します。各変更は、固有の名前を持つ、取り消し可能なVectorworksの操作として実行されます。

> **注:** 長さと高さ（Z方向の高さを含む）はワールド単位です。点もワールド単位です（[点](Common.md#points)を参照）。
>
> **注:** `pathUuid`を指定した`createPlant`、および`createHardscape`、`createLandscapeArea`、`createSiteModifier`、`createPropertyLine`が成功すると、元の多角形または曲線は消費されます。新しいオブジェクトがそれを取り込み、`getLandmarkObject`はそれを`pathObject`として返します。早い段階で失敗した呼び出しでは、パスは元のまま残ります。1つの輪郭から複数のオブジェクトを作成するには、先にパスを複製してください（[`editObject`](ObjectPrimitives.md#editobject)のアクション`duplicate`を参照）。これらのツールには必ず`pathUuid`を指定してください。指定しない場合、パスベースの4つのツールは`uuid`、`name`、`index`でパスを検索するため、作成オプションの`name`でパスオブジェクトが選ばれてしまいます。
>
> **注:** 作成ツールの結果の`applied`には、ツールの説明で「`setLandmarkObject`と同じ方法で設定」とされている型付きプロパティだけが含まれます。主な引数（`position`、`pathUuid`、`plantResource`、`latinName`、`commonName`、`spread`、`height`、`z`、`data`、`botanicalName`、`canopyDiameter`、`caliper`）と作成オプションは、`applied`の項目なしで書き込まれます。型付きプロパティを指定しなかった場合、`applied`は省略されます。JSONの型が異なる主な引数（たとえば数値に対する数値文字列）は、エラーなしで`0`または空の文字列として書き込まれます。`setLandmarkObject`はそれに対して`true`を報告します。

| ツール | 作用 | 安全性 | 概要 |
|---|---|---|---|
| [`createPlant`](#createplant) | 編集 | 中 | 点の位置またはパスに沿って植栽を作成します。 |
| [`createHardscape`](#createhardscape) | 編集 | 中 | 2Dパスオブジェクトから舗床を作成します。 |
| [`createLandscapeArea`](#createlandscapearea) | 編集 | 中 | 2Dパスオブジェクトからランドスケープエリアを作成します。 |
| [`createSiteModifier`](#createsitemodifier) | 編集 | 中 | 2Dパスオブジェクトから造成図形を作成します。 |
| [`createPropertyLine`](#createpropertyline) | 編集 | 中 | 閉じた2Dパスオブジェクトから境界線を作成します。 |
| [`createSiteModel`](#createsitemodel) | 編集 | 中 | 空の地形モデルを作成します。 |
| [`createStake`](#createstake) | 編集 | 中 | レベルオブジェクト（高さを示す点）を作成します。 |
| [`createExistingTree`](#createexistingtree) | 編集 | 中 | 既存樹木を作成します。 |
| [`getLandmarkObject`](#getlandmarkobject) | 読み取り専用 | 低 | 敷地またはランドスケープのオブジェクトのプロパティを読み取ります。 |
| [`setLandmarkObject`](#setlandmarkobject) | 編集 | 中 | 敷地またはランドスケープのオブジェクトを編集します。 |

### createPlant

点の位置またはパスに沿って植栽を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createPlant" · **runToolBatch内:** はい

**詳細**

植栽を`position`に作成します（または`pathUuid`に沿って分布させます）。任意の`plantResource`には、使用する植栽スタイル（シンボル定義）の名前を指定します。図面内にまだない場合は、Vectorworksの植栽コンテンツから取り込みます。省略した場合や見つからない場合は、最初に使用可能な植栽スタイルを使用します。実際に適用したスタイルを`plantStyle`として返します。`latinName`、`commonName`、`spread`、`height`は任意です。

任意の`config`（`pathUuid`とともに指定：plantsAtPolyVertices、plantsAlongPolyEdges、plantsInRectangularArray、plantsInTriangularArray）、`spacing`（植栽間の距離）、`plantID`、`comments`、`tagDisplay`、`show3DDetail`は、setLandmarkObjectと同じ方法で設定し、`applied`で適用結果を示します。

> **注:** `position`も`pathUuid`も指定しない場合、植栽は原点(0, 0)に配置されます。両方を指定した場合は`pathUuid`が優先されます。`pathUuid`を指定して成功した呼び出しはパスオブジェクトを消費するため（グループの注を参照）、輪郭を残すには先に複製してください。
>
> **注:** 不明な`plantResource`は拒否されません。ツールは、その名前の植栽スタイルを図面内で検索し、次にその名前のスタイルを植栽コンテンツ（`plantStyles`、次に`plantLibraries`）から取り込みます。何も見つからない場合は、コンテンツの最初の植栽スタイルを取り込んで使用します。この代替処理では、図面内の植栽スタイルは参照されません。`plantResource`を省略した場合は図面の最初の植栽スタイルを使用し、なければコンテンツの最初のスタイルを使用します。どのスタイルが使用されたかは、結果の`plantStyle`で確認してください。
>
> **注:** 不明な`pathUuid`は`path object not found`として報告されません。呼び出しは"no plant style is available"のエラー（結果を参照）で失敗しますが、この場合、このエラーは誤解を招きます。
>
> **注:** `plantResource`、`latinName`、`commonName`、`spread`、`height`は、`applied`の項目なしで書き込まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) |  | 挿入点（ワールド単位）。`pathUuid`を指定した場合は無視されます。どちらも指定しない場合は原点(0, 0)になります。 |
| `pathUuid` | string |  | パスを提供するオブジェクトのUUID。パスオブジェクトは新しい植栽に消費されます。 |
| `plantResource` | string |  | 使用する植栽スタイル（シンボル定義）の名前。必要に応じて植栽コンテンツから取り込みます。 |
| `latinName` | string |  | 学名。 |
| `commonName` | string |  | 樹種名。 |
| `spread` | number |  | 枝張り（樹冠の直径）。 |
| `height` | number |  | 高さ（ワールド単位）。 |
| `plantID` | string |  | 種を識別します。 |
| `comments` | string |  |  |
| `config` | string |  | 次のいずれか：`singlePlant`、`plantsAtPolyVertices`、`plantsAlongPolyEdges`、`plantsInRectangularArray`、`plantsInTriangularArray`。 |
| `tagDisplay` | string |  | 次のいずれか：`none`、`left`、`right`、`floating`。 |
| `show3DDetail` | boolean |  |  |
| `spacing` | number |  | 植栽間の距離。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい植栽のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `plantStyle` | 使用した植栽スタイルの名前。`plantResource`とは異なる場合があります。 |
| `applied` | 指定されて書き込まれた`config`、`spacing`、`plantID`、`comments`、`tagDisplay`、`show3DDetail`ごとに`true`。書き込まれなかった項目は`false`です。どれも指定されていない場合は省略されます。 |

エラー：`failed to create plant: no plant style is available. …`（`requestedStyle`（`plantResource`を指定した場合のみ）と`symbolDefinitionsFound`（図面内、およびコンテンツフォルダ`plantStyles`と`plantLibraries`内のシンボル定義の数）を含みます）。失敗した呼び出しはロールバックされ（`rolledBack`）、植栽は残りません。

### createHardscape

2Dパスオブジェクトから舗床を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createHardscape" · **runToolBatch内:** はい

**詳細**

`pathUuid`で指定した既存の2Dパスオブジェクトから、舗床（舗装された面）を作成します。任意の`mode3D`、`draw3D`、`isSiteModifier`、`isPathway`と`pathwayWidth` / `pathwayOffset`（パスに沿った固定幅の帯状部分）、`useBorder`、`borderWidth`、`borderThickness`、`slabThickness`は、setLandmarkObjectと同じ方法で設定し、`applied`で適用結果を示します。

> **注:** 成功した呼び出しはパスオブジェクトを消費します（グループの注を参照）。舗床の`id`は作成時には設定されません。`setLandmarkObject`で設定してください。作成オプションの`name`は、Vectorworksのオブジェクト名だけを設定します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `pathUuid` | string | はい | パスを提供するオブジェクトのUUID。パスオブジェクトは新しい舗床に消費されます。 |
| `mode3D` | string |  | 次のいずれか：`none`、`slab`、`padUnder`、`padOver`、`textureBed`、`slabDrainage`、`alignedSlab`、`alignedModifOver`、`alignedModifUnder`。 |
| `draw3D` | boolean |  |  |
| `isSiteModifier` | boolean |  |  |
| `isPathway` | boolean |  | パスに沿った固定幅の帯状部分。 |
| `useBorder` | boolean |  |  |
| `slabThickness` | number |  |  |
| `borderThickness` | number |  |  |
| `borderWidth` | number |  |  |
| `pathwayWidth` | number |  |  |
| `pathwayOffset` | number |  |  |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい舗床のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定されて書き込まれた`mode3D`、`draw3D`、`isSiteModifier`、`isPathway`、`useBorder`、`slabThickness`、`borderThickness`、`borderWidth`、`pathwayWidth`、`pathwayOffset`ごとに`true`。書き込まれなかった項目は`false`です。どれも指定されていない場合は省略されます。 |

エラー：`path object not found (provide 'pathUuid' of a polygon/polyline)`、`failed to create object`。失敗した呼び出しはロールバックされ（`rolledBack`）、舗床は残りません。

### createLandscapeArea

2Dパスオブジェクトからランドスケープエリアを作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createLandscapeArea" · **runToolBatch内:** はい

**詳細**

`pathUuid`で指定した既存の2Dパスオブジェクトから、ランドスケープエリア（植栽領域）を作成します。任意の`id`、`description`、`drawingMode`、`areaUnits`、`plantDisplay2D`（または互換性用の`showPlantsIn2D`）は、setLandmarkObjectと同じ方法で設定し、`applied`で適用結果を示します。

> **注:** 成功した呼び出しはパスオブジェクトを消費します（グループの注を参照）。エリア名は作成時には設定されません。作成オプションの`name`はVectorworksのオブジェクト名だけを設定するため、エリア名を設定するには、新しいオブジェクトの`uuid`と`name`を指定して`setLandmarkObject`を使用してください。
>
> **注:** `showPlantsIn2D`と`plantDisplay2D`を一緒に指定しないでください。どちらも`applied`で`false`を報告し、どちらも書き込まれません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `pathUuid` | string | はい | パスを提供するオブジェクトのUUID。パスオブジェクトは新しいランドスケープエリアに消費されます。 |
| `id` | string |  | ランドスケープエリアのID（テキスト）。 |
| `description` | string |  | 説明文。 |
| `drawingMode` | string |  | 次のいずれか：`landscapeArea`、`hedgerow`。 |
| `areaUnits` | string |  | 次のいずれか：`sqFeet`、`sqMeters`、`acres`、`hectares`、`documentUnits`。 |
| `showPlantsIn2D` | boolean |  | `plantDisplay2D`の互換形式です。`true`は`plantSymbols`、`false`は`none`を選択します。両方を指定しないでください。 |
| `plantDisplay2D` | string |  | 次のいずれか：`none`、`plantCloud`、`plantLine`、`plantSymbols`。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しいランドスケープエリアのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定されて書き込まれた`id`、`description`、`drawingMode`、`areaUnits`、`plantDisplay2D`、`showPlantsIn2D`ごとに`true`。書き込まれなかった項目は`false`です（両方の表示プロパティを同時に指定すると、どちらも`false`を報告します）。どれも指定されていない場合は省略されます。 |

エラー：`path object not found (provide 'pathUuid' of a polygon/polyline)`、`failed to create object`。失敗した呼び出しはロールバックされ（`rolledBack`）、ランドスケープエリアは残りません。

### createSiteModifier

2Dパスオブジェクトから造成図形を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createSiteModifier" · **runToolBatch内:** はい

**詳細**

`pathUuid`で指定した既存の2Dパスオブジェクトから、造成図形を作成します。任意の`config`（例：pad、gradeLimits）、`applyTo`、`show3D`、`retainSlopeInside`、`simplificationTolerance`は、setLandmarkObjectと同じ方法で設定し、`applied`で適用結果を示します。

> **注:** 成功した呼び出しはパスオブジェクトを消費します（グループの注を参照）。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `pathUuid` | string | はい | パスを提供するオブジェクトのUUID。パスオブジェクトは新しい造成図形に消費されます。 |
| `config` | string |  | 次のいずれか：`gradeLimits`、`contour`、`pad`、`retainingPad`、`aligned`、`path`、`fitToObjects`、`textureBed`、`spoilPile`。 |
| `applyTo` | string |  | 次のいずれか：`existing`、`proposed`。 |
| `show3D` | boolean |  |  |
| `retainSlopeInside` | boolean |  |  |
| `simplificationTolerance` | number |  |  |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい造成図形のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定されて書き込まれた`config`、`applyTo`、`show3D`、`retainSlopeInside`、`simplificationTolerance`ごとに`true`。書き込まれなかった項目は`false`です。どれも指定されていない場合は省略されます。 |

エラー：`path object not found (provide 'pathUuid' of a polygon/polyline)`、`failed to create object`。失敗した呼び出しはロールバックされ（`rolledBack`）、造成図形は残りません。

### createPropertyLine

閉じた2Dパスオブジェクトから境界線を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createPropertyLine" · **runToolBatch内:** はい

**詳細**

`pathUuid`で指定した既存の閉じた2Dパスオブジェクトから、境界線（区画の境界）を作成します。任意の`showName`、`showNumber`、`showArea`、`areaUnitsImperial`、`areaUnitsMetric`、`distanceUnits`は、setLandmarkObjectと同じ方法で設定し、`applied`で適用結果を示します。

> **注:** 成功した呼び出しはパスオブジェクトを消費します（グループの注を参照）。ツールはパスが閉じているかどうかを確認しません。区画の名前と番号は作成時には設定されません。作成オプションの`name`はVectorworksのオブジェクト名だけを設定するため、新しいオブジェクトの`uuid`と、`name`および`number`を指定して`setLandmarkObject`を使用してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `pathUuid` | string | はい | パスを提供するオブジェクトのUUID。パスオブジェクトは新しい境界線に消費されます。 |
| `showName` | boolean |  |  |
| `showNumber` | boolean |  |  |
| `showArea` | boolean |  |  |
| `areaUnitsImperial` | string |  | 次のいずれか：`documentUnits`、`squareFeet`、`squareYards`、`squareMiles`、`acres`、`squareMeters`、`squareKilometers`、`hectares`。 |
| `areaUnitsMetric` | string |  | 次のいずれか：`documentUnits`、`squareFeet`、`squareYards`、`squareMiles`、`acres`、`squareMeters`、`squareKilometers`、`hectares`。 |
| `distanceUnits` | string |  | 次のいずれか：`Document Units`、`Feet & Inches`、`Inches`、`Feet`、`Yards`、`Miles`、`Microns`、`Millimeters`、`Centimeters`、`Meters`、`Kilometers`。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい境界線のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定されて書き込まれた`showName`、`showNumber`、`showArea`、`areaUnitsImperial`、`areaUnitsMetric`、`distanceUnits`ごとに`true`。書き込まれなかった項目は`false`です。どれも指定されていない場合は省略されます。 |

エラー：`path object not found (provide 'pathUuid' of a polygon/polyline)`、`failed to create object`。失敗した呼び出しはロールバックされ（`rolledBack`）、境界線は残りません。

### createSiteModel

空の地形モデルを作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createSiteModel" · **runToolBatch内:** はい

**詳細**

空の地形モデル／地形オブジェクトを`position`に作成します。後から測量データやLandmarkのコマンドで内容を追加してください。任意の`display2D`、`display3D`、`style2D`、`style3D`、`geometryZReference`、`showErrors`は、setLandmarkObjectと同じ方法で設定し、`applied`で適用結果を示します。

> **注:** `position`は必須とされていますが、ツールはそれを強制しません。指定されていない場合や点でない場合、地形モデルは原点(0, 0)に配置されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点（ワールド単位）。 |
| `display2D` | string |  | 次のいずれか：`existingOnly`、`proposedOnly`、`existingAndProposed`。 |
| `display3D` | string |  | 次のいずれか：`nothing`、`existingOnly`、`proposedOnly`、`cutAndFill`。 |
| `style2D` | string |  | 次のいずれか：`k2DTINStyle2DContour`、`k2DTINStyle2DContourSmoothed`、`k2DTINStyle2DContourColoredElevations`、`k2DTINStyle2DTriangulatedContoursColoredSlopes`、`k2DTINStyle2DTriangles`、`k2DTINStyle2DTrianglesColoredSlopes`。 |
| `style3D` | string |  | 次のいずれか：`k3DTINStyleMesh`、`k3DTINStyleMeshColoredElev`、`k3DTINStyleMeshColoredSlopes`、`k3DTINStyleGrid`、`k3DTINStyleGridColoredElev`、`k3DTINStyleGridColoredSlope`、`k3DTINStyleVerticalGrid`、`k3DTINStyleContour`、`k3DTINStyleExtrudedContour`、`k3DTINStyleExtContColoredElev`。 |
| `geometryZReference` | number |  | 等高線の基準高さ。 |
| `showErrors` | boolean |  |  |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい地形モデルのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定されて書き込まれた`display2D`、`display3D`、`style2D`、`style3D`、`geometryZReference`、`showErrors`ごとに`true`。書き込まれなかった項目は`false`です。どれも指定されていない場合は省略されます。 |

エラー：`failed to create object`。失敗した呼び出しはロールバックされ（`rolledBack`）、地形モデルは残りません。

### createStake

レベルオブジェクト（高さを示す点）を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createStake" · **runToolBatch内:** はい

**詳細**

レベルオブジェクト（高さを示す点）を`position`に作成します。高さ`z`とラベル`data`は任意です。任意の`mode`、`siteModel`、`id`、`idPrefix`、`idSuffix`、`labelReference`、`displayLeaderLine`、`showElevationMark`は、setLandmarkObjectと同じ方法で設定し、`applied`で適用結果を示します。

> **注:** `position`は必須とされていますが、ツールはそれを強制しません。指定されていない場合や点でない場合、レベルオブジェクトは(0, 0)に配置されます。`z`のデフォルトは0です。`z`と`data`は、`applied`の項目なしで書き込まれます。
>
> **注:** `data`はレベルオブジェクトの説明（ラベルテキスト）です。引数`description`は、ランドスケープエリアでのみ読み取られます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点（ワールド単位）。 |
| `z` | number |  | Z値（高さ）。ワールド単位。デフォルトは0です。 |
| `data` | string |  | レベルオブジェクトのラベルテキスト（説明）。 |
| `mode` | string |  | 次のいずれか：`siteModelSource`、`setToSiteModelGrade`、`setToCutSurface`、`setToObjectSpot`、`graphic2DOnly`、`siteModifierObject`。 |
| `siteModel` | string |  | 次のいずれか：`existing`、`proposed`。 |
| `id` | integer |  | レベルオブジェクトの整数のID。整数または`"12"`のような数値文字列は書き込まれます。それ以外の値は書き込まれません（`applied`で`false`）。 |
| `idPrefix` | string |  |  |
| `idSuffix` | string |  |  |
| `labelReference` | string |  | 次のいずれか：`ID`、`Elevation`、`Description`、`ID/Elevation`、`ID/Description`、`Description/Elevation`、`Stationing Data`、`Coordinate PointNE`、`Coordinate PointEN`、`Coordinate PointXY`、`Coordinate PointYX`、`Latitude/Longitude`、`Longitude/Latitude`、`Latitude/Longitude(WGS84)`、`Longitude/Latitude(WGS84)`、`No Label`、`Object Spot Height`。 |
| `displayLeaderLine` | boolean |  |  |
| `showElevationMark` | boolean |  |  |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しいレベルオブジェクトのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定されて書き込まれた`mode`、`siteModel`、`id`、`idPrefix`、`idSuffix`、`labelReference`、`displayLeaderLine`、`showElevationMark`ごとに`true`。書き込まれなかった項目は`false`です。どれも指定されていない場合は省略されます。 |

エラー：`failed to create stake`。失敗した呼び出しはロールバックされ（`rolledBack`）、レベルオブジェクトは残りません。

### createExistingTree

既存樹木を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createExistingTree" · **runToolBatch内:** はい

**詳細**

既存樹木オブジェクトを`position`に作成します。`botanicalName`、`commonName`、`height`、`canopyDiameter`、`caliper`（胸高直径、DBH）は任意です。setLandmarkObjectのその他の既存樹木プロパティ（treeNumber、origin、根域の直径、treeProtectionZone、condition、sule、significance、actionComment、location、notes、create3D）も同じ方法で設定し、`applied`で適用結果を示します。

> **注:** `position`は必須とされていますが、ツールはそれを強制しません。指定されていない場合や点でない場合、樹木は(0, 0)に配置されます。`botanicalName`、`commonName`、`height`、`canopyDiameter`、`caliper`は、`applied`の項目なしで書き込まれます。
>
> **注:** 現在、`create3D`は書き込まれません。`applied.create3D`は常に`false`で、`getLandmarkObject`は`create3D`を返しません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点（ワールド単位）。 |
| `botanicalName` | string |  |  |
| `commonName` | string |  |  |
| `height` | number |  | 高さ（ワールド単位）。 |
| `canopyDiameter` | number |  |  |
| `caliper` | number |  | 幹の直径（胸高直径、DBH）。 |
| `treeNumber` | string |  |  |
| `origin` | string |  | 次のいずれか：`notSet`、`endemic`、`native`、`exotic`、`indigenous`、`custom`。 |
| `rootBallDiameter` | number |  |  |
| `criticalRootZoneDiameter` | number |  |  |
| `primaryRootZoneDiameter` | number |  |  |
| `treeProtectionZone` | string |  | 次のいずれか：`none`、`circularZone`、`using12DBH`。 |
| `condition` | string |  | 次のいずれか：`notSet`、`excellent`、`good`、`average`、`poor`、`custom`。 |
| `sule` | string |  | 次のいずれか：`notSet`、`long`、`medium`、`short`、`removal`、`custom`。 |
| `significance` | string |  | 次のいずれか：`notSet`、`mostSignificant`、`highlySignificant`、`lessSignificant`、`leastSignificant`、`hazardous`、`custom`。 |
| `actionComment` | string |  | 次のいずれか：`notSet`、`retain`、`retainArborist`、`transplantOriginal`、`transplantProposed`、`remove`、`removeBuildingFootprint`、`removePoorHealth`、`removeSpecies`、`custom`。 |
| `location` | string |  |  |
| `notes` | string |  |  |
| `create3D` | boolean |  | 現在は書き込まれません。`applied.create3D`は常に`false`です。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい既存樹木のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定されて書き込まれた`treeNumber`、`origin`、`rootBallDiameter`、`criticalRootZoneDiameter`、`primaryRootZoneDiameter`、`treeProtectionZone`、`condition`、`sule`、`significance`、`actionComment`、`location`、`notes`ごとに`true`。書き込まれなかった項目は`false`です。`create3D`は常に`false`です。どれも指定されていない場合は省略されます。 |

エラー：`failed to create existing tree`。失敗した呼び出しはロールバックされ（`rolledBack`）、既存樹木は残りません。

### getLandmarkObject

敷地またはランドスケープのオブジェクトのプロパティを読み取ります。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

植栽、舗床、ランドスケープエリア、既存樹木、レベルオブジェクト、境界線、地形モデル、造成図形の型付きプロパティを読み取ります。返される情報は`kind`、setLandmarkObjectで書き込むフィールド（植栽のスタイルは`plantStyle`として返す）、および読み取り専用の値です。読み取り専用の値は、舗床のmainArea、borderArea、footprintArea（メートル系のファイルではsq m、インチ系のファイルではsq ft）とperimeter、mainPerimeter、borderPerimeter（ワールド単位）、ランドスケープエリアの`area`（そのareaUnitsによる単位）、projectedArea（地形モデルへの投影面積。地形モデルがなければ0）、numPlants、境界線のareaTextとperimeterText、地形モデルのprojectedAreaExisting、surfaceAreaExisting、surfaceAreaProposed、volumeExisting、volumeProposed、cutVolume、fillVolume（書式付きテキスト。計算されるまでは空）です。

パスベースのオブジェクトは、2Dパスの参照である`pathObject`も返します。任意の`params`には、未加工の型付き値として返すプラグインパラメータ名を列挙します（getObjectParametersを参照）。値は数値（長さはワールド単位、角度は度）、真偽値、テキストです。

> **注:** ランドスケープエリアと境界線では、`name`はVectorworksのオブジェクト名ではなく、エリア名または区画名です。空の場合も含め、オブジェクト参照の`name`に置き換わります。既存樹木では、`create3D`は返されません。
>
> **注:** 上記の説明では、`area`は`areaUnits`の単位で、地形モデルがない場合`projectedArea`は0とされています。プラグインは両方の値を平方ミリメートルで保存し、地形モデルがない場合の`projectedArea`はパスの平面面積です。面積の単位での値が必要な場合は、`params`でプラグインパラメータ`SurfaceAreaInLAUnits`と`ProjectedAreaInLAUnits`を要求してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `params` | array of string |  | 型付き値として返すプラグインパラメータの名前。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |

**結果**

オブジェクトのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `kind` | `Plant`、`Hardscape`、`LandscapeArea`、`ExistingTree`、`Stake`、`PropertyLine`、`SiteModel`、`SiteModifier`のいずれか。 |
| 各種類のフィールド | その種類で`setLandmarkObject`が書き込むフィールドと、詳細に記載された読み取り専用の値。読み取れない値は省略されます。 |
| `pathObject` | パスベースのオブジェクトの2Dパスのオブジェクト参照。パスを持たないオブジェクトでは省略されます。 |
| `params` | `params`を配列で指定した場合のみ。要求された各名前を未加工の型付き値に対応付けるオブジェクトです。テキストでない名前と不明なパラメータの名前は、エラーにならずにスキップされます。 |

エラー：`object not found`、`not a landmark object`。

### setLandmarkObject

敷地またはランドスケープのオブジェクトを編集します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: setLandmarkObject" · **runToolBatch内:** はい

**詳細**

uuidでLandmarkオブジェクトを編集します。以下に示す、種類に対応したフィールドを指定します（getLandmarkObjectは同じキーで読み取ります）。`applied`は、フィールドごとに書き込まれたかどうかを示します（不明な選択肢は拒否されます）。

**植栽：** plantResource（別の植栽スタイルに切り替え、必要に応じて取り込む。読み取り時は`plantStyle`）、latinName、commonName、plantID（種を識別）、comments、spread（枝張り）、height、spacing（多角形／曲線の辺に沿った配置、または配列内の植栽間の距離）、config、tagDisplay、show3DDetail。

**舗床：** id（テキスト）、mode3D、draw3D、isSiteModifier、isPathway（パスに沿った固定幅の帯状部分）とpathwayWidth / pathwayOffset、useBorder、borderWidth、borderThickness、slabThickness。

**ランドスケープエリア：** name（エリア名。オブジェクト名ではない）、id（テキスト）、description、drawingMode、areaUnits、plantDisplay2D（none、plantCloud、plantLine、plantSymbols）。互換性用のshowPlantsIn2Dは、植栽を表示するいずれかのモードではtrueを返します。trueを書き込むとplantSymbols、falseを書き込むとnoneを選択します。両方の表示プロパティを指定しないでください。同時に指定すると両方とも失敗します。

**既存樹木：** botanicalName、commonName、treeNumber、origin、height、canopyDiameter、caliper（胸高直径、DBH）、rootBallDiameter、criticalRootZoneDiameter、primaryRootZoneDiameter、treeProtectionZone、condition、sule（耐用年数：安全に有用性を保てる推定年数）、significance、actionComment、location、notes、create3D。`custom`を選択した場合は、CustomOrigin / CustomCondition / CustomSULE / CustomSignificance / CustomActionパラメータの自由記述テキストを使用します（`params`で設定）。

**レベルオブジェクト：** z（高さ）、data（説明）、mode（地形モデルに対する役割）、siteModel（対象とする表面）、id（整数）、idPrefix、idSuffix、labelReference（ラベルの内容）、displayLeaderLine、showElevationMark。

**境界線：** name、number、showName、showNumber、showArea、areaUnitsImperial / areaUnitsMetric（インチ系／メートル系のファイルにおける面積の単位）、distanceUnits（区間のラベル）。

**地形モデル：** display2D / display3D（描画する表面）、style2D、style3D、geometryZReference（等高線の基準高さ）、showErrors。

**造成図形：** config（fitToObjectsはalignedとして保存）、applyTo（変更する表面）、show3D、retainSlopeInside、simplificationTolerance。長さはワールド単位です。選択肢はスキーマに列挙されています。`params`オブジェクトで未加工のプラグインパラメータを設定します。

> **注:** オブジェクトは`uuid`、`name`、`index`の順に検索されます。`name`は、ランドスケープエリアのエリア名、および境界線の区画名としても書き込まれます（その行を参照）。
>
> **注:** オブジェクトの種類に属さないフィールドは、`applied`の項目なしで無視されます。8種類のLandmarkオブジェクトのほか、ツールは他のプラグインオブジェクトも受け付けますが、その場合は`params`だけが有効です。プラグインオブジェクトでないオブジェクトでは`not a landmark object`になります。
>
> **注:** 「不明な選択肢は拒否されます」は選択肢のフィールドにのみ当てはまります。不明な`plantResource`は拒否されません。代替の植栽スタイルが見つかると`applied.plantResource`は`true`になるため（`createPlant`を参照）、使用中の植栽スタイルは`getLandmarkObject`で`plantStyle`を読み取って確認してください。JSONの型が異なる値を持つ主なフィールドは、`0`または空のテキストとして書き込まれ、`true`と報告されます（グループの注を参照）。
>
> **注:** 詳細には`fitToObjects`は`aligned`として保存されるとありますが、実際にはそうなりません。`fitToObjects`は`fitToObjects`として保存され、そのまま読み取られます。現在、`create3D`は書き込まれません。`applied.create3D`は常に`false`です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | `uuid`がない場合の名前による参照。ランドスケープエリア（エリア名。オブジェクト名ではない）と境界線（区画名）にも使用されます。同じ値が書き込まれるため、その名前だけを変更するには`uuid`を指定してください。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `plantResource` | string |  | 植栽に使用します。別の植栽スタイルに切り替え、必要に応じて取り込みます。読み取り時は`plantStyle`です。不明な名前は拒否されません。スタイルを切り替えると、スタイルのすべての設定（名前、植栽ID、枝張り、高さ、config、…）が引き継がれ、現在の設定が上書きされます。保持したいフィールドは同じ呼び出しで指定してください。`createPlant`の`plantResource`と同じ方法で解決されます（代替の植栽スタイルを見つけることも取り込むこともできない場合は`false`）。 |
| `latinName` | string |  | 植栽に使用します。 |
| `commonName` | string |  | 植栽、既存樹木に使用します。 |
| `spread` | number |  | 植栽に使用します。枝張り（樹冠の直径。ワールド単位）。 |
| `height` | number |  | 植栽、既存樹木に使用します。高さ（ワールド単位）。 |
| `number` | string |  | 境界線に使用します。 |
| `botanicalName` | string |  | 既存樹木に使用します。 |
| `canopyDiameter` | number |  | 既存樹木に使用します。 |
| `caliper` | number |  | 既存樹木に使用します。幹の直径（胸高直径、DBH）。 |
| `z` | number |  | レベルオブジェクトに使用します。Z値（高さ）。ワールド単位。 |
| `data` | string |  | レベルオブジェクトに使用します。説明（ラベルテキスト）。 |
| `params` | object |  | 未加工のプラグインパラメータ`{ "ParamName": value }`。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |
| `plantID` | string |  | 植栽に使用します。種を識別します。 |
| `comments` | string |  | 植栽に使用します。 |
| `config` | string |  | 植栽、造成図形に使用します。植栽では次のいずれか：`singlePlant`、`plantsAtPolyVertices`、`plantsAlongPolyEdges`、`plantsInRectangularArray`、`plantsInTriangularArray`。造成図形では次のいずれか：`gradeLimits`、`contour`、`pad`、`retainingPad`、`aligned`、`path`、`fitToObjects`、`textureBed`、`spoilPile`。 |
| `tagDisplay` | string |  | 植栽に使用します。次のいずれか：`none`、`left`、`right`、`floating`。 |
| `show3DDetail` | boolean |  | 植栽に使用します。 |
| `spacing` | number |  | 植栽に使用します。多角形／曲線の辺に沿った配置、または配列内の植栽間の距離。 |
| `mode3D` | string |  | 舗床に使用します。次のいずれか：`none`、`slab`、`padUnder`、`padOver`、`textureBed`、`slabDrainage`、`alignedSlab`、`alignedModifOver`、`alignedModifUnder`。 |
| `draw3D` | boolean |  | 舗床に使用します。 |
| `isSiteModifier` | boolean |  | 舗床に使用します。 |
| `isPathway` | boolean |  | 舗床に使用します。パスに沿った固定幅の帯状部分。 |
| `useBorder` | boolean |  | 舗床に使用します。 |
| `slabThickness` | number |  | 舗床に使用します。 |
| `borderThickness` | number |  | 舗床に使用します。 |
| `borderWidth` | number |  | 舗床に使用します。 |
| `pathwayWidth` | number |  | 舗床に使用します。 |
| `pathwayOffset` | number |  | 舗床に使用します。 |
| `id` | string or integer |  | 舗床とランドスケープエリア（テキスト）、およびレベルオブジェクト（整数。`"12"`のような数値文字列も受け付けます）に使用します。舗床とランドスケープエリアではテキストでない値は書き込まれず（`applied`で`false`）、レベルオブジェクトでは整数でない値は書き込まれません。 |
| `description` | string |  | ランドスケープエリアに使用します。説明文。レベルオブジェクトには`description`はありません。その説明は`data`です。 |
| `drawingMode` | string |  | ランドスケープエリアに使用します。次のいずれか：`landscapeArea`、`hedgerow`。 |
| `areaUnits` | string |  | ランドスケープエリアに使用します。次のいずれか：`sqFeet`、`sqMeters`、`acres`、`hectares`、`documentUnits`。 |
| `showPlantsIn2D` | boolean |  | ランドスケープエリアに使用します。`plantDisplay2D`の互換形式です。`true`は`plantSymbols`、`false`は`none`を選択します。両方を指定しないでください。両方とも`false`を報告し、どちらも書き込まれません。 |
| `plantDisplay2D` | string |  | ランドスケープエリアに使用します。次のいずれか：`none`、`plantCloud`、`plantLine`、`plantSymbols`。 |
| `treeNumber` | string |  | 既存樹木に使用します。 |
| `origin` | string |  | 既存樹木に使用します。次のいずれか：`notSet`、`endemic`、`native`、`exotic`、`indigenous`、`custom`。 |
| `rootBallDiameter` | number |  | 既存樹木に使用します。 |
| `criticalRootZoneDiameter` | number |  | 既存樹木に使用します。 |
| `primaryRootZoneDiameter` | number |  | 既存樹木に使用します。 |
| `treeProtectionZone` | string |  | 既存樹木に使用します。次のいずれか：`none`、`circularZone`、`using12DBH`。 |
| `condition` | string |  | 既存樹木に使用します。次のいずれか：`notSet`、`excellent`、`good`、`average`、`poor`、`custom`。 |
| `sule` | string |  | 既存樹木に使用します。次のいずれか：`notSet`、`long`、`medium`、`short`、`removal`、`custom`。 |
| `significance` | string |  | 既存樹木に使用します。次のいずれか：`notSet`、`mostSignificant`、`highlySignificant`、`lessSignificant`、`leastSignificant`、`hazardous`、`custom`。 |
| `actionComment` | string |  | 既存樹木に使用します。次のいずれか：`notSet`、`retain`、`retainArborist`、`transplantOriginal`、`transplantProposed`、`remove`、`removeBuildingFootprint`、`removePoorHealth`、`removeSpecies`、`custom`。 |
| `location` | string |  | 既存樹木に使用します。 |
| `notes` | string |  | 既存樹木に使用します。 |
| `create3D` | boolean |  | 既存樹木に使用します。現在は書き込まれません。`applied.create3D`は常に`false`です。 |
| `mode` | string |  | レベルオブジェクトに使用します。次のいずれか：`siteModelSource`、`setToSiteModelGrade`、`setToCutSurface`、`setToObjectSpot`、`graphic2DOnly`、`siteModifierObject`。 |
| `siteModel` | string |  | レベルオブジェクトに使用します。次のいずれか：`existing`、`proposed`。 |
| `idPrefix` | string |  | レベルオブジェクトに使用します。 |
| `idSuffix` | string |  | レベルオブジェクトに使用します。 |
| `labelReference` | string |  | レベルオブジェクトに使用します。次のいずれか：`ID`、`Elevation`、`Description`、`ID/Elevation`、`ID/Description`、`Description/Elevation`、`Stationing Data`、`Coordinate PointNE`、`Coordinate PointEN`、`Coordinate PointXY`、`Coordinate PointYX`、`Latitude/Longitude`、`Longitude/Latitude`、`Latitude/Longitude(WGS84)`、`Longitude/Latitude(WGS84)`、`No Label`、`Object Spot Height`。 |
| `displayLeaderLine` | boolean |  | レベルオブジェクトに使用します。 |
| `showElevationMark` | boolean |  | レベルオブジェクトに使用します。 |
| `showName` | boolean |  | 境界線に使用します。 |
| `showNumber` | boolean |  | 境界線に使用します。 |
| `showArea` | boolean |  | 境界線に使用します。 |
| `areaUnitsImperial` | string |  | 境界線に使用します。次のいずれか：`documentUnits`、`squareFeet`、`squareYards`、`squareMiles`、`acres`、`squareMeters`、`squareKilometers`、`hectares`。 |
| `areaUnitsMetric` | string |  | 境界線に使用します。次のいずれか：`documentUnits`、`squareFeet`、`squareYards`、`squareMiles`、`acres`、`squareMeters`、`squareKilometers`、`hectares`。 |
| `distanceUnits` | string |  | 境界線に使用します。次のいずれか：`Document Units`、`Feet & Inches`、`Inches`、`Feet`、`Yards`、`Miles`、`Microns`、`Millimeters`、`Centimeters`、`Meters`、`Kilometers`。 |
| `display2D` | string |  | 地形モデルに使用します。次のいずれか：`existingOnly`、`proposedOnly`、`existingAndProposed`。 |
| `display3D` | string |  | 地形モデルに使用します。次のいずれか：`nothing`、`existingOnly`、`proposedOnly`、`cutAndFill`。 |
| `style2D` | string |  | 地形モデルに使用します。次のいずれか：`k2DTINStyle2DContour`、`k2DTINStyle2DContourSmoothed`、`k2DTINStyle2DContourColoredElevations`、`k2DTINStyle2DTriangulatedContoursColoredSlopes`、`k2DTINStyle2DTriangles`、`k2DTINStyle2DTrianglesColoredSlopes`。 |
| `style3D` | string |  | 地形モデルに使用します。次のいずれか：`k3DTINStyleMesh`、`k3DTINStyleMeshColoredElev`、`k3DTINStyleMeshColoredSlopes`、`k3DTINStyleGrid`、`k3DTINStyleGridColoredElev`、`k3DTINStyleGridColoredSlope`、`k3DTINStyleVerticalGrid`、`k3DTINStyleContour`、`k3DTINStyleExtrudedContour`、`k3DTINStyleExtContColoredElev`。 |
| `geometryZReference` | number |  | 地形モデルに使用します。等高線の基準高さ。 |
| `showErrors` | boolean |  | 地形モデルに使用します。 |
| `applyTo` | string |  | 造成図形に使用します。次のいずれか：`existing`、`proposed`。 |
| `show3D` | boolean |  | 造成図形に使用します。 |
| `retainSlopeInside` | boolean |  | 造成図形に使用します。 |
| `simplificationTolerance` | number |  | 造成図形に使用します。 |

**結果**

`applied`のみを返します。オブジェクト参照は返しません。

| キー | 説明 |
|---|---|
| `applied` | 指定されたフィールドごとに、書き込まれた場合は`true`、書き込まれなかった場合は`false`。 |
| `applied.params` | `params`をオブジェクトで指定した場合のみ。各パラメータ名について、値が書き込まれた場合は`true`、書き込まれなかった場合は`false`。 |

エラー：`object not found`、`not a landmark object`。失敗した呼び出しはロールバックされ（`rolledBack`）、何も変更されません。
