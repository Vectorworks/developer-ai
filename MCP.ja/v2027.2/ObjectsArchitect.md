[English](../../MCP/v2027.2/ObjectsArchitect.md) • [Deutsch](../../MCP.de/v2027.2/ObjectsArchitect.md) • **日本語**

# ObjectsArchitect — 建築（BIM）

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

BIMの建築要素である壁、スラブ、屋根、ドア、窓、柱、階段のためのツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [Architecture](#architecture)
  - [createWall](#createwall)
  - [createSlab](#createslab)
  - [createRoof](#createroof)
  - [createDoor](#createdoor)
  - [createWindow](#createwindow)
  - [createColumn](#createcolumn)
  - [createStair](#createstair)
  - [getArchitectureObject](#getarchitectureobject)
  - [setArchitectureObject](#setarchitectureobject)

<a id="overview"></a>

## 概要

このフォルダには1個のツールグループがあり、合計9個のツールが含まれています。

| グループ | グループID | 初期状態で有効 | 安全性レベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [Architecture](#architecture) | `architecture` | いいえ | 中 | 9 | BIMの建築要素：壁、スラブ、屋根、ドア、窓、柱、階段。 |

## Architecture

> **グループ:** `Architecture` · **グループID:** `architecture` · **初期状態で有効:** いいえ · **安全性レベル:** 中 · **ツール数:** 9

**BIMの建築要素：壁、スラブ、屋根、ドア、窓、柱、階段。**

直線壁と円弧壁、スラブ、屋根、ドア、窓、柱、階段のBIM建築オブジェクトを確認、作成、編集します。

**BIMワークフローの順序：** 最初にストーリとそのレベルを作成し（Documentグループ：getStories、createStory）、次にスタイルを用意して（Resourcesグループ）、ストーリレイヤに建築要素を作成します。壁の上端と下端は、topBound / bottomBoundでストーリレベルに関連付けます。壁の端点の高さとスタイルはgetArchitectureObjectで読み取ります。平均高さ、上端／下端の高さ基準に関するメタデータ、オフセット、検証済みの高さを取得するにはincludeHeightDetailsを指定します。長さはワールド単位、角度はラジアンですが、屋根の辺の勾配は度（2～90）です。ドアと窓は単独で作成されるため、Vectorworksで壁に挿入してください。各変更は、固有の名前を持つ、取り消し可能なVectorworksの操作として実行されます。

> **注:** 角度はラジアンですが、次の2つは度です：屋根の辺の`slope`、およびプラグインオブジェクトの角度パラメータ（`params`で書き込む角度パラメータと、`getArchitectureObject`が`includeOpening`で返す`openAngleParameter`）。`getArchitectureObject`が返す壁の`angle`はラジアンです。`applied`を返すツールは、指定された値を、値ごとまたは値のグループごとに1項目で報告します（各ツールの結果を参照）。値が書き込まれた場合は`true`、書き込まれなかった場合（たとえば型が異なる値）は`false`です。書き込みの対象にならない値は列挙されません。`createRoof`と`createColumn`は`applied`を返しません。失敗した呼び出しは`err`を返し、ロールバックされます（`rolledBack`）。[結果とエラー](Common.md#results-and-errors)を参照してください。

| ツール | 作用 | 安全性 | 概要 |
|---|---|---|---|
| [`createWall`](#createwall) | 編集 | 中 | 直線壁または円弧壁を作成します。 |
| [`createSlab`](#createslab) | 編集 | 中 | 2D境界オブジェクトからスラブを作成します。 |
| [`createRoof`](#createroof) | 編集 | 中 | 多角形の屋根を作成します。 |
| [`createDoor`](#createdoor) | 編集 | 中 | 単独のドアを作成します。 |
| [`createWindow`](#createwindow) | 編集 | 中 | 単独の窓を作成します。 |
| [`createColumn`](#createcolumn) | 編集 | 中 | 柱を作成します。 |
| [`createStair`](#createstair) | 編集 | 中 | 階段を作成します。 |
| [`getArchitectureObject`](#getarchitectureobject) | 読み取り専用 | 低 | 壁、スラブ、屋根、ドア、窓、柱、階段のプロパティを読み取ります。 |
| [`setArchitectureObject`](#setarchitectureobject) | 編集 | 中 | 壁、スラブ、屋根、ドア、窓、柱、階段を編集します。 |

### createWall

直線壁または円弧壁を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createWall" · **runToolBatch内:** はい

**詳細**

`start`から`end`までの直線壁または円弧壁を作成します。円弧壁の場合、始点と終点の間の円弧上にあり、両点を結ぶ直線上にはない点`pointOnArc`を通ります。`thickness`が0の場合は、現在の壁の設定を使用します。任意の`topHeight`/`bottomHeight`で、レイヤプレーンを基準とした壁の高さを設定します。任意の`topBound` / `bottomBound`で、オブジェクト情報パレットと同じように壁の上端／下端の高さ基準を設定します。指定形式は{ kind: story|layerElevation|layerWallHeight, levelType（ストーリの高さ基準の場合：レベルタイプ）, relativeStory（ストーリの高さ基準の場合：-1は下階、0は壁のレイヤのストーリでデフォルト、1は上階）, offset（ワールド単位、デフォルト0）}です。getArchitectureObjectの`includeHeightDetails`で読み取れます。

これらは他の値の後に適用され、壁の端点を高さ基準の高さに移動するため、topHeight/bottomHeightに置き換わります。両方を指定した呼び出しは拒否されます。壁に適用できない高さ基準（レイヤがどのストーリにも属していない、上階または下階がない、ストーリにそのレベルがない、上端が下端より上にない）の場合、呼び出しは失敗し、何も作成しません。`applied`はtopBound/bottomBoundの結果を示します。

> **注:** `topHeight`と`bottomHeight`の一方だけを指定すると、もう一方は`0`になるため、両方を指定してください。`kind`が`story`の高さ基準には、空でない`levelType`が必要です。レイヤの種類では`levelType`と`relativeStory`の値は無視されますが、文字列でない`levelType`や、-1、0、1以外の`relativeStory`は拒否されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `start` | [点](Common.md#points) | はい | 始点。 |
| `end` | [点](Common.md#points) | はい | 終点。 |
| `pointOnArc` | [点](Common.md#points) |  | 壁を円弧壁（曲線）にします。`start`と`end`の間の円弧上の点です。`start`と`end`を結ぶ線上にある点を指定すると、呼び出しは失敗します。 |
| `thickness` | number |  | 厚さ（ワールド単位）。`0`の場合は現在の壁の設定を使用します。 |
| `topHeight` | number |  | レイヤプレーンを基準とする壁上端の両端の高さ（ワールド単位）。`topHeight`か`bottomHeight`の一方だけを指定した場合、もう一方は`0`です。`topBound`または`bottomBound`とは併用できません。 |
| `bottomHeight` | number |  | レイヤプレーンを基準とする壁下端の両端の高さ（ワールド単位）。`topHeight`か`bottomHeight`の一方だけを指定した場合、もう一方は`0`です。`topBound`または`bottomBound`とは併用できません。 |
| `topBound` | object |  | オブジェクト情報パレットと同様に、壁の上端の高さ基準を設定します。`topHeight`と`bottomHeight`の代わりになります。 |
| `topBound.kind` | string | はい | 次のいずれか：`story`、`layerElevation`、`layerWallHeight`。 |
| `topBound.levelType` | string |  | ストーリのレベルタイプ。`kind`が`story`の場合は必須で、空にできません。レイヤの種類では値は無視されますが、文字列以外を指定すると、どの種類でも呼び出しが拒否されます。 |
| `topBound.relativeStory` | integer |  | 次のいずれか：`-1`、`0`、`1`。デフォルト：`0`。下階（`-1`）、壁のレイヤのストーリ（`0`）、上階（`1`）。`kind`が`story`の場合に使用します。レイヤの種類では値は無視されますが、`-1`、`0`、`1`以外の値を指定すると、どの種類でも呼び出しが拒否されます。 |
| `topBound.offset` | number |  | デフォルト：`0`。オフセット（ワールド単位）。 |
| `bottomBound` | object |  | オブジェクト情報パレットと同様に、壁の下端の高さ基準を設定します。`topHeight`と`bottomHeight`の代わりになります。 |
| `bottomBound.kind` | string | はい | 次のいずれか：`story`、`layerElevation`、`layerWallHeight`。 |
| `bottomBound.levelType` | string |  | ストーリのレベルタイプ。`kind`が`story`の場合は必須で、空にできません。レイヤの種類では値は無視されますが、文字列以外を指定すると、どの種類でも呼び出しが拒否されます。 |
| `bottomBound.relativeStory` | integer |  | 次のいずれか：`-1`、`0`、`1`。デフォルト：`0`。下階（`-1`）、壁のレイヤのストーリ（`0`）、上階（`1`）。`kind`が`story`の場合に使用します。レイヤの種類では値は無視されますが、`-1`、`0`、`1`以外の値を指定すると、どの種類でも呼び出しが拒否されます。 |
| `bottomBound.offset` | number |  | デフォルト：`0`。オフセット（ワールド単位）。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい壁のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | `topBound`と`bottomBound`のみ。指定されて書き込まれた高さ基準ごとに`true`。高さ基準を指定しなかった場合は省略されます。`thickness`、`pointOnArc`、高さは報告されません。 |

エラー：`'start' and 'end' points are required`、`failed to create round wall ('pointOnArc' must be a point { x, y } off the line from 'start' to 'end')`、`failed to create wall`、`give the heights of a wall either as 'topBound' / 'bottomBound' or as heights (topHeight, bottomHeight, startTop, ...), not both in one call`、形式が正しくない高さ基準（`'<key>' needs 'kind': story, layerElevation or layerWallHeight`、`'<key>': 'relativeStory' is -1, 0 or 1, 'offset' a number (world units) and 'levelType' a string`、`'<key>': a story bound needs 'levelType', the level of the story`）、壁に適用できない高さ基準（`Vectorworks refused the wall bounds: the top must stay above the bottom, and the wall must be on a design layer`、またはストーリの問題を示すテキスト）。失敗した呼び出しはロールバックされ（`rolledBack`）、壁は残りません。

### createSlab

2D境界オブジェクトからスラブを作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createSlab" · **runToolBatch内:** はい

**詳細**

スラブ（床／デッキ／天井。Vectorworksの`Slab`プラグインオブジェクト）を、`profileUuid`で指定した既存の2D境界オブジェクト（多角形、曲線、長円／円、円弧）から作成します。境界オブジェクトはスラブに取り込まれます。任意の`style`と`height`（スラブの基準面の高さ。スタイルの設定に応じたコア構成要素の上端または下端）を、この順序で書き込みます。`style`には図面のスラブスタイルを指定します。名前またはそのリソースのUUID（resourceTypeを`slabStyle`にしてgetResourcesで一覧を取得）は作成前に検証され、図面のスラブスタイルではない名前やUUIDの場合は呼び出しを拒否し、何も作成しません。内部インデックスでも指定でき、0は構成要素を保持したままスラブをスタイルなしにします。スラブスタイルではないインデックスはfalseと報告され、書き込まれません。

`applied`は、指定された項目ごとにtrue/falseを示します。getArchitectureObjectはstyle（インデックス）とstyleNameを返します。

> **注:** スキーマでは`profileUuid`は必須です。指定されていない場合は、同じ引数の`uuid`、`name`、`index`で境界オブジェクトを検索するため、作成オプションのつもりで指定した`name`で境界オブジェクトが選ばれることがあります。必ず`profileUuid`を指定してください。文字列の`style`は、数字だけの文字列であっても、常に名前またはリソースのUUIDとして読み取られます。内部インデックスには整数を使用してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `profileUuid` | string | はい | 輪郭形状を提供するオブジェクト（多角形、曲線、長円／円、円弧）のUUID。スラブに取り込まれます。 |
| `height` | number |  | スラブの基準面の高さ（スタイルの設定に応じたコア構成要素の上端または下端）。ワールド単位。 |
| `style` | integer or string |  | 図面のスラブスタイル：その名前またはリソースのUUID（`resourceType`を`slabStyle`にして`getResources`で一覧を取得）、または整数の内部インデックス（`0`：構成要素を保持したままスタイルなし）。スラブスタイルではない名前またはUUIDは呼び出しを拒否します。スラブスタイルではないインデックスは`false`と報告され、書き込まれません。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しいスラブのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定された`style`と`height`ごとに1項目。書き込まれた場合は`true`、書き込まれなかった場合は`false`（型が異なる値、またはスラブスタイルではない`style`インデックス）。どちらも指定されていない場合は省略されます。 |

エラー：`profile object not found (provide 'profileUuid' of a polygon/polyline boundary)`、`failed to create slab (the profile must be a polygon, polyline, oval/circle or arc)`、`'style' "<text>" is neither the name nor the UUID of a slab style of the drawing (getResources lists them with resourceType 'slabStyle')`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### createRoof

多角形の屋根を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createRoof" · **runToolBatch内:** はい

**詳細**

多角形の屋根を作成します。任意のパラメータは`generateGableWalls`、`bearingInset`、`roofThickness`、`miterType`（vertical|horizontal|double）、`verticalMiter`、および屋根の輪郭を順に並べた`edges`です。輪郭には少なくとも3個の項目{ point, slope, projection, eaveHeight }を指定します。slopeは2～90度です（Vectorworksが屋根を作成できる辺の勾配は2～90度のみ）。projection（壁外面から軒先の距離）とeaveHeight（レイヤの高さを基準とした軒先下端の高さ）はワールド単位で、デフォルトは0です。

屋根を作成する前にすべての辺を検証します。pointまたはslopeの欠落、有限数でない値、2～90の範囲外の勾配がある場合は呼び出しを拒否し、何も作成しません。新しい屋根には小屋裏、軒天井、鼻隠しはありません。getArchitectureObjectは同じ形式で辺を返します。

> **注:** 型が異なる`generateGableWalls`、`bearingInset`、`roofThickness`、`verticalMiter`は`false`または`0`として読み取られ、`horizontal`と`double`以外の`miterType`は`vertical`として読み取られます。いずれもエラーにはなりません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `generateGableWalls` | boolean |  | デフォルト：`false`。 |
| `bearingInset` | number |  | デフォルト：`0`。 |
| `roofThickness` | number |  | デフォルト：`0`。 |
| `miterType` | string |  | 次のいずれか：`vertical`、`horizontal`、`double`。デフォルト：`vertical`。 |
| `verticalMiter` | number |  | デフォルト：`0`。 |
| `edges` | array of object |  | 3～32767個の項目。 |
| `edges[].point` | [点](Common.md#points) | はい | 屋根の輪郭上の点。辺は指定順に使用されます。 |
| `edges[].slope` | number | はい | 度、2～90。最小値：`2`。最大値：`90`。 |
| `edges[].projection` | number |  | 壁外面から軒先の距離（ワールド単位）。デフォルト：`0`。 |
| `edges[].eaveHeight` | number |  | レイヤの高さを基準とした軒先下端の高さ（ワールド単位）。デフォルト：`0`。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい屋根のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）を返します。`applied`は返されません。

エラー：`'edges' must be an array of 3 to 32767 edges`、屋根の作成前に見つかった辺の問題（常に`'edges'[<i>]: `で始まります。`an edge is an object { point, slope, projection, eaveHeight } whose slope, projection and eaveHeight are numbers`、`the edge needs a 'point' { x, y }`、`the edge needs a 'slope' (degrees, 2 to 90)`、`the point, slope, projection and eaveHeight must be finite numbers`、`the slope <n> is not 2 to 90 degrees: Vectorworks builds a roof only with edge slopes from 2 to 90 degrees`）、`failed to create roof`、`Vectorworks refused the roof edge 'edges'[<i>]`。失敗した呼び出しはロールバックされ（`rolledBack`）、屋根は残りません。

### createDoor

単独のドアを作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createDoor" · **runToolBatch内:** はい

**詳細**

ドア（`Door`）パラメトリックオブジェクトを`position`に単独で作成します（Vectorworksで壁に挿入してください）。任意の`width`と`height`（正の値、ワールド単位）は、オブジェクト情報パレットに表示されるドアの寸法で、寸法押さえ（Size Reference）に従って測定されます。Vectorworksはこれらから扉寸法を計算します（getArchitectureObjectのleafWidth / leafHeight）。任意の`sizeReference`（leaf：扉寸法、unit：部材外寸、roughOpening：あら開口寸法）を最初に書き込みます。デフォルトは図面のドア設定によります。

基準を変更する`sizeReference`には、`width`と`height`の両方が必要です。ドアは保存済みの寸法を新しい基準で測定するためです。`config`（従来のConfigポップアップ）と`idLabel`は任意です。ドアのプラグインスタイルで設定されている値は変更できません。その場合は呼び出しを拒否し、何も作成しません。`applied`は、指定された値ごとにtrue/falseを示します。getArchitectureObjectは、指定どおりのwidthとheightを読み取ります。

> **注:** プラグインスタイルの検証の対象は`sizeReference`、`width`、`height`だけで、値が変わる場合に限られます。その場合は`'<key>' cannot be changed: the plug-in style '<name>' of the door sets its parameter '<param>' (edit the style instead); the call changes nothing`で拒否されます。`config`と`idLabel`はこの検証なしで書き込まれます。値は`sizeReference`、`width`、`height`、`config`、`idLabel`の順に書き込まれます。文字列でない`config`または`idLabel`は空のテキストとして書き込まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点。 |
| `width` | number |  | ワールド単位。`0`より大きい値。それ以外の値は拒否されます。 |
| `height` | number |  | ワールド単位。`0`より大きい値。それ以外の値は拒否されます。 |
| `sizeReference` | string |  | 次のいずれか：`leaf`、`unit`、`roughOpening`（扉寸法、部材外寸、あら開口寸法）。基準を変更する値には、`width`と`height`も必要です。 |
| `config` | string |  | 従来のConfigポップアップ。 |
| `idLabel` | string |  | ドアのIDラベル。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しいドアのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定された`sizeReference`、`width`、`height`、`config`、`idLabel`ごとに1項目。書き込まれた場合は`true`、ドアが値を受け付けなかった場合は`false`。どれも指定されていない場合は省略されます。 |

エラー：`failed to create door`、`'width' must be a positive number (world units)`（`'height'`も同様）、`'sizeReference' is one of leaf|unit|roughOpening`、`'sizeReference' changes what the size of the door measures: give both 'width' and 'height' with it; the call changes nothing`、`'<key>' cannot be changed: the plug-in style '<name>' of the door sets its parameter '<param>' (edit the style instead); the call changes nothing`。拒否された呼び出しはロールバックされ（`rolledBack`）、ドアは残りません。

### createWindow

単独の窓を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createWindow" · **runToolBatch内:** はい

**詳細**

窓（`Window`）パラメトリックオブジェクトを`position`に単独で作成します（Vectorworksで壁に挿入してください）。任意の`width`と`height`（正の値、ワールド単位）は、オブジェクト情報パレットに表示される窓の寸法で、寸法押さえ（Size Reference）に従って測定されます。Vectorworksはこれらから部材外寸を計算します（getArchitectureObjectのunitWidth / unitHeight）。任意の`sizeReference`（sash：窓框寸法、unit：部材外寸、roughOpening：あら開口寸法）を最初に書き込みます。デフォルトは図面の窓設定によります。基準を変更する場合は、`width`と`height`の両方が必要です。

任意の`elevation`は窓の下端の高さで、レイヤプレーンから窓の下端までの高さ（ワールド単位）です（壁内の窓でも同様で、壁の下端からの高さではありません）。寸法の後に書き込みます。窓の高さ位置の基準（Elevation Set At）の設定は維持されます。Head of Window（窓の上端。デフォルト）の場合、Vectorworksは窓の上端の高さであるelevation + heightを保存します（getArchitectureObjectはheadHeightとelevationSetAtを返します）。

`idLabel`は任意です。窓のプラグインスタイルで設定されている値は変更できません。その場合は呼び出しを拒否し、何も作成しません。`applied`は、指定された値ごとにtrue/falseを示します。getArchitectureObjectは、指定どおりのwidth、height、elevationを読み取ります。

> **注:** プラグインスタイルの検証の対象は`sizeReference`、`width`、`height`、`elevation`だけで、値が変わる場合に限られます。その場合は`'<key>' cannot be changed: the plug-in style '<name>' of the window sets its parameter '<param>' (edit the style instead); the call changes nothing`で拒否されます。`idLabel`はこの検証なしで書き込まれ、文字列でない値は空のテキストとして書き込まれます。値は`sizeReference`、`width`、`height`、`elevation`、`idLabel`の順に書き込まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点。 |
| `width` | number |  | ワールド単位。`0`より大きい値。それ以外の値は拒否されます。 |
| `height` | number |  | ワールド単位。`0`より大きい値。それ以外の値は拒否されます。 |
| `sizeReference` | string |  | 次のいずれか：`sash`、`unit`、`roughOpening`。基準を変更する値には、`width`と`height`も必要です。 |
| `elevation` | number |  | 窓の下端の高さ（レイヤプレーンからの高さ、ワールド単位）。数値である必要があります。窓に有効な高さ位置の基準（Elevation Set At：Head of WindowまたはSill of Window）と高さ（Height）がない場合は拒否されます。 |
| `idLabel` | string |  | 窓のIDラベル。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい窓のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定された`sizeReference`、`width`、`height`、`elevation`、`idLabel`ごとに1項目。書き込まれた場合は`true`、窓が値を受け付けなかった場合は`false`。どれも指定されていない場合は省略されます。 |

エラー：`failed to create window`、`'width' must be a positive number (world units)`（`'height'`も同様）、`'elevation' (the sill height) must be a number (world units)`、`'sizeReference' is one of sash|unit|roughOpening`、`'sizeReference' changes what the size of the window measures: give both 'width' and 'height' with it; the call changes nothing`、`'elevation' cannot be written: the window has no valid ElevationSetAt (Head of Window or Sill of Window) and Height`、`'<key>' cannot be changed: the plug-in style '<name>' of the window sets its parameter '<param>' (edit the style instead); the call changes nothing`。拒否された呼び出しはロールバックされ（`rolledBack`）、窓は残りません。

### createColumn

柱を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createColumn" · **runToolBatch内:** はい

**詳細**

柱（Vectorworksの`Column2`プラグインオブジェクト）を`position`に作成します。任意のパラメータは`shape`（Rectangular|Oval。RoundはOval）、`height`（有効な1つの構成要素の高さ。柱が意匠と構造の両方の構成要素を使用する場合は失敗）、`width`と`depth`（柱身）、`diameter`（丸の柱身）です。値を設定できない場合は柱を削除し、ツールは失敗します。

> **注:** `height`、`width`、`depth`、`diameter`は`0`より大きい有限数である必要があります。値は`shape`、`height`、`width`、`depth`、`diameter`の順に書き込まれるため、`diameter`は`width`と`depth`より優先されます。柱身は`Oval`になり、幅と奥行きが直径と等しくなります。`shape`には`Rectangular`、`Oval`、`Round`（`Oval`として読み取られます）を指定でき、それ以外のテキストでは呼び出しが失敗します。柱は`Column2`プラグインオブジェクトです。`Column2`がインストールされていない場合は、従来の`Column`オブジェクトになります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点。 |
| `shape` | string |  | `Rectangular`、`Oval`、`Round`（`Oval`として読み取られます）のいずれか。スキーマはテキストを制限しませんが、それ以外の値では呼び出しが失敗します。 |
| `height` | number |  | `0`より大きい値。有効な1つの構成要素の高さ。柱が意匠と構造の両方の構成要素を使用する場合は失敗します。 |
| `width` | number |  | 柱身の幅（ワールド単位）。`0`より大きい値。 |
| `depth` | number |  | 柱身の奥行き（ワールド単位）。`0`より大きい値。 |
| `diameter` | number |  | 丸の柱身の直径（ワールド単位）。`0`より大きい値。柱身を`Oval`にし、`width`と`depth`を直径と等しくします（両方より優先されます）。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい柱のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）を返します。`applied`は返されません。

エラー：`failed to create column (requires the 'Column2' plug-in object)`、`failed to set column shape`、`failed to set column height (requires a single bound component)`、`failed to set column shaft width`、`failed to set column shaft depth`、`failed to set column shaft diameter`。値の設定に失敗すると柱は削除され、失敗した呼び出しはロールバックされるため（`rolledBack`）、柱は残りません。

### createStair

階段を作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createStair" · **runToolBatch内:** はい

**詳細**

階段（Vectorworksの'Stairs CW'プラグインオブジェクトをデフォルトの構成で使用）を`position`に作成します。任意の正の値`totalRise`、`totalRun`（矢印の長さ（歩行線の長さ））、`treadDepth`、`riserHeight`を、階段のリセット前に書き込みます。階段は従属する値を再計算するため、getArchitectureObjectで読み直してください。Stairs CWの階段では`width`を設定できません。`applied`は、指定された値ごとにtrue/falseを示します。

> **注:** `width`は常に`false`と報告されます。Stairs CWは最初の階段の幅を書き込みますが、その値を読み戻しません。`totalRise`、`totalRun`、`treadDepth`、`riserHeight`は`0`より大きい有限数である必要があります。それ以外の値は`false`と報告され、階段はデフォルトの値を保持します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点。 |
| `width` | number |  | 幅（ワールド単位）。`applied`では常に`false`と報告されます。Stairs CWの階段ではこの値を設定できません。 |
| `totalRise` | number |  | 階高（ワールド単位）。`0`より大きい値。 |
| `totalRun` | number |  | 矢印の長さ（歩行線の長さ）。`0`より大きい値。 |
| `treadDepth` | number |  | 段板奥行き（ワールド単位）。`0`より大きい値。 |
| `riserHeight` | number |  | 蹴上げ寸法（ワールド単位）。`0`より大きい値。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性もクラス属性に設定します。 |

**結果**

新しい階段のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定された`width`、`totalRise`、`totalRun`、`treadDepth`、`riserHeight`ごとに1項目。書き込まれた場合は`true`、そうでない場合は`false`です。`width`は常に`false`です。どれも指定されていない場合は省略されます。 |

エラー：`failed to create stair (requires the 'Stairs CW' plug-in object)`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### getArchitectureObject

壁、スラブ、屋根、ドア、窓、柱、階段のプロパティを読み取ります。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

壁、スラブ、屋根、ドア、窓、柱、階段の型付きプロパティ（寸法、高さ、スタイル、一覧表のIDなど）を読み取ります。壁は、保存されている拘束のオフセットではなく、端点自体のZ値startTop/startBottom/endTop/endBottomをワールド単位で返します。加えて、caps { leftCap（始点側の端部）, rightCap（終点側の端部）, round }とisCurtainWallを返します。スラブ（`Slab`プラグインオブジェクト、または古いファイルの従来の床スラブノード。後者には高さもパラメータもありません）は、height、style（スラブスタイルの内部インデックス。0はスタイルなし）、styleName（そのスタイルの名前）を返します。

屋根はedgeCountとedgesを返します。edgesは屋根の輪郭を順に並べたもので、辺ごとに{ point, slope（度）, projection, eaveHeight（レイヤの高さを基準） }が1項目あり、読み取れない辺はnullです。createRoofとsetArchitectureObjectが受け取る形式と同じです。さらにgenerateGableWalls、bearingInset、roofThickness、miterType（vertical|horizontal|double）、verticalMiterを返します。

ドアはwidthとheight（オブジェクト情報パレットに表示されるドアの寸法。ワールド単位で、sizeReferenceが示すleaf|unit|roughOpeningに従って測定）、leafWidth / leafHeight（前回のリセット時にVectorworksがこれらから計算した扉寸法）、config、idLabel、thickness（扉）、topShape、leafType、onScheduleを返します。窓は同様にwidth、height、sizeReference（sash|unit|roughOpening）、unitWidth / unitHeight（Vectorworksがこれらから計算した部材外寸）、elevation（窓の下端の高さ：壁内の窓も含め、レイヤプレーンから窓の下端までの高さ）、headHeight、elevationSetAt（head|sill。この2つのうち窓がElevationパラメータとして保存する方）、idLabel、sashOperation（従来のSashOperationポップアップ）、topShape、jambWidth、jambDepth、includeSill、sillStyle、onSchedule、descriptionを返します。柱（`Column2`プラグインオブジェクト、または従来の`Column`）はshape、height、width、depth、diameterを返します。階段（'Stairs CW'プラグインオブジェクト）はwidth（最初の階段の幅）、totalRise、totalRun（矢印の長さ（歩行線の長さ））、numRisers、treadDepth、riserHeightを返します。

ポップアップ値は、プラグインが保存している値をそのまま返します。任意の`params`（プラグインパラメータ名の配列。スラブ、ドア、窓、柱、階段で使用）を指定すると、型付き値を持つ`params` { name: value }が追加されます。実数はワールド単位の数値（角度パラメータは度）、整数は整数、真偽値は真偽値、それ以外の型は文字列です。オブジェクトに存在しない名前は省略されます。

getObjectParametersの表示用文字列とは異なり、これらはsetArchitectureObjectの`params`が書き込む形式の正確な値です。任意のincludeHeightDetails（デフォルトfalse）を指定すると、壁にのみheightDetailsオブジェクトが追加されます。内容はstartHeight/endHeight（端点での上下差）、averageHeight（既存の幾何学的な平均計算をワールド単位に正規化した値）、測定値の取得可否ステータス、およびtopBound/bottomBoundです。各高さ基準にはstatus（valid|missing|unresolved|invalid）、kind（layerElevation|layerWallHeight|story|unknown）、levelType、offset、ストーリの高さ基準の場合はrelativeStory（-1は下、0は現在、1は上）が含まれます。

resolvedElevationを持つのは有効な高さ基準だけで、Vectorworksの親コンテナを基準とする規則に従います。参照が欠落している場合、代替の高さは返しません。高さ基準が欠落していても、幾何学的な高さがないことを意味するわけではありません。これらの高さ基準のレベルはストーリの一覧や絶対的なストーリ識別子ではありません（DocumentグループのgetStoriesがストーリとそのレベルの一覧を返します）。heightDetails内の長さはすべてワールド単位です。UIの単位に変換するにはconvertUnitsを使用してください。

任意のincludeOpening（デフォルトfalse）を指定すると、ドアと窓に`opening`オブジェクトが追加されます。内容はcapability（operable|fixed|notApplicable|unknown）、config（窓の形式（Configuration）ポップアップの未加工の値）またはconfiguration（ドアの形式（Configuration）ポップアップの未加工の値）、operation（ドアのSwing形式ではSwingOperation、窓では形式に応じてCasementOperation、FixedGlassOperation、HungOperation）、屋外から見たhingeSide（ドアのSwing、窓のCasementとTilt/Turn）、openDirection（ドアのSwing、窓のAwning、Casement、Hopper、Tilt/Turn。Vertical Pivotでは代わりにoutwardSideを返す）、未加工の値のhingeDirection（窓）、interiorSide、flipped、show3DOpen、openAngleParameter、およびlegacyOperation（ドア：operationに置き換えられた従来のOperationポップアップ）です。

方向のパラメータは、その形式に該当する場合にのみ出力されます。片開きのドアのSwingと、確認済みの窓の開口（Awning、Hopper、Tilt/Turn、片開きのCasement）では、opensTowardはIn/Outの値からinteriorまたはexteriorになります（Inは屋内側、Outは屋外側）。Vertical Pivotはboth、Opening、Cased Opening、Fixed GlassはnotApplicable、それ以外の開口はunknownです。

描画上の開き角度は、開閉の可否とは別に返されます。ドアの`config`プロパティは、現在は形式（Configuration）ポップアップを読み取ります。

> **注:** 上記の説明の最後の文は、ドアについては正しくありません。`config`は、`createDoor`が書き込む従来の`Config`ポップアップを返します。形式（Configuration）ポップアップは、`includeOpening`を指定した場合の`opening.configuration`としてのみ返されます。`openAngleParameter`はプラグインパラメータの未加工の値で、ラジアンではなく度です。`capability`は、ドアのSwingと、窓の形式Awning、Casement、Hopper、Tilt/Turn、Vertical Pivotでは`operable`、Fixed Glassの窓では`fixed`、OpeningとCased Openingでは`notApplicable`、それ以外（たとえばHung、Sliding、Folding、Swing以外のドア）では`unknown`です。`hingeDirection`、`flipped`、`show3DOpen`は真偽値、`interiorSide`と`legacyOperation`は文字列です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `includeHeightDetails` | boolean |  | デフォルト：`false`。壁に`heightDetails`を追加します。 |
| `includeOpening` | boolean |  | デフォルト：`false`。ドアまたは窓に`opening`を追加します。 |
| `params` | array of string |  | 型付き値として返すプラグインパラメータの名前。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。スラブ、ドア、窓、柱、階段のみ。壁と屋根は`params`を返しません。 |

**結果**

オブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と`kind`（`Wall`、`Slab`、`Roof`、`Door`、`Window`、`Column`、`Stair`のいずれか）、およびその種類のキーを返します。オブジェクトから読み取れない値は省略されます。

| 種類 | キー |
|---|---|
| `Wall` | `start`、`end`（[点](Common.md#points)）、`length`、`angle`（ラジアン）、`startTop`、`startBottom`、`endTop`、`endBottom`（ワールド単位）、`style`（壁スタイルの内部インデックス）、`caps`（`{ leftCap, rightCap, round }`）、`isCurtainWall`、および`includeHeightDetails`指定時の`heightDetails`。 |
| `Slab` | `height`、`style`（内部インデックス。`0`はスタイルなし）、`styleName`（`style`が`0`以外の場合のみ）、および要求した場合の`params`。 |
| `Roof` | `edgeCount`、`edges`、`roofThickness`、`bearingInset`、`generateGableWalls`、`verticalMiter`、`miterType`。 |
| `Door` | `opening`（`includeOpening`指定時）、`width`、`height`、`sizeReference`、`leafWidth`、`leafHeight`、`config`、`idLabel`、`thickness`、`topShape`、`leafType`、`onSchedule`、および要求した場合の`params`。 |
| `Window` | `opening`（`includeOpening`指定時）、`width`、`height`、`sizeReference`、`unitWidth`、`unitHeight`、`elevation`、`headHeight`、`elevationSetAt`、`idLabel`、`sashOperation`、`topShape`、`jambWidth`、`jambDepth`、`includeSill`、`sillStyle`、`onSchedule`、`description`、および要求した場合の`params`。 |
| `Column` | `shape`、`height`、`width`、`depth`、`diameter`（幅と奥行きが等しい`Oval`の柱身の場合のみ）、および要求した場合の`params`。 |
| `Stair` | `width`（階段の幅の最初の値）、`totalRise`、`totalRun`、`numRisers`、`treadDepth`、`riserHeight`、および要求した場合の`params`。`numTreads`、`configuration`、`handrailLeft`、`handrailRight`は返されません。 |

`heightDetails`（壁。`includeHeightDetails`指定時）には、`units`（`world`）、`startHeight`と`endHeight`（両端点の高さがどちらも有限数の場合を除き`null`）、`endpointHeightStatus`（`available`または`unavailable`）、`averageHeight`（計算できない場合は`null`）、`averageHeightStatus`（`available`または`unavailable`）、`topBound`、`bottomBound`が含まれます。高さ基準には常に`status`（`valid`、`missing`、`unresolved`、`invalid`のいずれか）があります。statusが`missing`でない場合は、`kind`（`layerElevation`、`layerWallHeight`、`story`、`unknown`のいずれか）、`levelType`、`offset`（有限数でない場合は`null`）、およびストーリの高さ基準の場合は`relativeStory`もあります。`resolvedElevation`は、statusが`valid`で、高さ基準に高さがある場合にのみ含まれます。

エラー：`object not found`、`not an architectural object (wall, slab, roof, door, window, column or stair)`。

### setArchitectureObject

壁、スラブ、屋根、ドア、窓、柱、階段を編集します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: setArchitectureObject" · **runToolBatch内:** はい

**詳細**

uuidで壁、スラブ、屋根、ドア、窓、柱、階段を編集します。getArchitectureObjectが返すキーと値を使って、種類に対応するフィールドを指定します。`applied`は、変更ごとにtrue/falseを示します。

**壁：** thickness、start/end、topHeight/bottomHeight（両端）、startTop/startBottom/endTop/endBottom（個々の端点の高さ。たとえば高さが変化する壁に使用し、`endHeights`として適用）、style（壁スタイルの内部インデックス。それ以外の値はfalseで、書き込まれない）、caps { leftCap, rightCap }（丸型の端部はサポートされなくなりました）、isCurtainWall、およびcreateWallと同じ形式のtopBound / bottomBoundを指定できます。topBound / bottomBoundは他の値の後に適用され、それぞれ高さ基準の高さの変化分だけ壁の該当する端を移動します（オブジェクト情報パレットと同様）。そのため、1回の呼び出しで高さの指定と組み合わせることはできません。壁に適用できない高さ基準がある場合は呼び出しが失敗し、何も変更しません。

**スラブ：** createSlabと同じ形式のstyle（スラブスタイルの名前またはそのリソースのUUID。図面のスラブスタイルではない場合は呼び出しを拒否し、何も変更しません。内部インデックスも指定でき、0は構成要素を保持したままスタイルなしにし、図面のスラブスタイルではないインデックスはfalseで書き込まれません）とheight（`Slab`プラグインオブジェクトのみ。従来の床スラブノードではfalse）を、この順序で書き込みます。

**屋根：** generateGableWalls、bearingInset、roofThickness（屋根に構成要素がある場合は無視）、miterType（vertical|horizontal|double）、verticalMiterをまとめて`attributes`として適用します。`accessories` { insertAttic, insertSoffit, insertFascia, fasciaWidth, fasciaHeight, atticHeight, recess, rakeThickness, trimDepth（長さはワールド単位） }は読み取りできず、全体として書き込みます。省略したメンバーはfalse/0になります。屋根の`edges`は、getArchitectureObjectが返す形式で少なくとも3個の項目を順に指定し、屋根の輪郭を置き換えます。項目で省略したメンバーは、その位置にある現在の辺の値を保持します（現在の辺より後の項目には`point`と`slope`が必要）。すべての勾配は2～90度である必要があります（Vectorworksが屋根を作成できる辺の勾配は2～90度のみ）。無効な項目がある場合は呼び出しを拒否し、何も変更しません。変更のない辺は書き直さず、追加の辺は末尾に追加し、余分な辺は末尾からその上のドーマーやトップライトとともに削除します。ある点が次の点と一致する場合や、両隣の点と同一直線上にある場合は、何も書き込みません（Vectorworksがそのような点を削除するため）。`edges`として適用し、最終的な屋根の点、勾配、壁外面から軒先の距離が指定内容と完全に一致した場合にtrueになります（Vectorworksは、切り妻側の辺の軒先下端の高さを、隣接する辺が支える高さまで引き上げることがあります）。

**ドア：** createDoorと同じ形式のwidth、height、sizeReference（leaf|unit|roughOpening）を最初にsizeReference、width、heightの順で書き込み、その後にthickness（扉）、config、topShape、leafType（Solid|Glass|Panel|Custom）、onSchedule、idLabelを書き込みます。

**窓：** createWindowと同じ形式のwidth、height、sizeReference（sash|unit|roughOpening）、elevation（窓の下端の高さ）を、最初にsizeReference、width、height、elevationの順で書き込みます（`elevation`を指定しない場合は保存済みのElevationを保持するため、Head of Windowでは高さを変更すると窓の下端が移動します）。その後にtopShape、sashOperation（従来のパラメータ）、jambWidth、jambDepth、includeSill、sillStyle（Timber|Masonry|Brick|Open Profile Beside Frame|Open Profile Below Frame|Closed Profile）、onSchedule、idLabel、descriptionを書き込みます。ドアまたは窓のプラグインスタイルで設定されている値を指定した場合は呼び出しを拒否し、何も変更しません。現在の値と等しい値は再度書き込みません。topShapeはSquare|Round|Segment|Sloped from Left|Sloped from Right|Gable|Ellipse|Gothicです。窓ではHalf Round、Half Segment、Half Ellipse、Half Gothicも使用でき、それぞれの後に' from Left'または' from Right'を付けます。

**柱：** shape、height、width、depth、diameter。

**階段（Stairs CW）：** 正の値のtotalRise、totalRun（矢印の長さ（歩行線の長さ））、treadDepth、riserHeight、およびnumRisers（1-32767）を指定します。階段は編集後のリセット時にこれらを適用し、従属する値を再計算します（読み直してください）。width、numTreads、configuration、handrailLeft、handrailRightは設定できません（appliedはfalse）。`params`オブジェクトで未加工のプラグインパラメータを設定します（実数はワールド単位で、getArchitectureObjectの`params`が読み取る形式）。

> **注:** 呼び出しを拒否する可能性のある項目は、何かを変更する前にすべて検証されるため、拒否された呼び出しは何も変更しません。対象は、壁の高さ基準（高さと一緒に指定された高さ基準も含む）、図面のスラブスタイルではないスラブの`style`、屋根の`edges`、およびドアまたは窓の寸法とプラグインスタイルの検証です（[createDoor](#createdoor)と[createWindow](#createwindow)を参照）。ドアの`sizeReference`は`leaf`、`unit`、`roughOpening`、窓は`sash`、`unit`、`roughOpening`を受け付けます。プラグインスタイルの検証の対象は`sizeReference`、`width`、`height`、および窓の`elevation`だけで、値が変わる場合に限られます。変わらない値は再度書き込まれませんが、`true`と報告されます。ドアと窓のその他の値は、この検証なしで書き込まれます。
>
> `topHeight`と`bottomHeight`は一緒に書き込まれます。一方だけを指定すると、もう一方は`0`になります。`start`と`end`は一緒に書き込まれます。一方だけを指定した場合は無視され、報告されません。文字列でない`config`または`idLabel`は空のテキストとして書き込まれ、数値でない壁の`thickness`は`0`として読み取られます。どちらの場合もエラーにはなりません。
>
> ドアの`config`と`idLabel`は、寸法の値の直後、`thickness`、`topShape`、`leafType`、`onSchedule`より前に書き込まれます。窓の`elevation`と`idLabel`は、寸法の値の直後、その他の窓の値より前に書き込まれ、`sashOperation`は`topShape`より前に書き込まれます。上記の説明とは順序が異なります。`params`はすべての種類のオブジェクトで受け付けられ、その結果は`applied.params`です。スラブ、ドア、窓、柱、階段に適用されます。プラグインパラメータを持たない壁と屋根では、すべての項目が`false`になります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `thickness` | number |  | 壁、ドアに使用します。厚さ（ワールド単位。ドアの場合は扉の厚さ）。数値でない壁の`thickness`は`0`として読み取られます。 |
| `start` | [点](Common.md#points) |  | 壁に使用します。始点。`end`と一緒の場合にのみ書き込まれます。一方だけの場合は無視され、報告されません。 |
| `end` | [点](Common.md#points) |  | 壁に使用します。終点。`start`と一緒の場合にのみ書き込まれます。一方だけの場合は無視され、報告されません。 |
| `topHeight` | number |  | 壁に使用します。両端の上端の高さ（ワールド単位）。`topHeight`か`bottomHeight`の一方だけを指定した場合、もう一方は`0`です。`heights`として報告されます。`topBound`または`bottomBound`とは併用できません。 |
| `bottomHeight` | number |  | 壁に使用します。両端の下端の高さ（ワールド単位）。`topHeight`か`bottomHeight`の一方だけを指定した場合、もう一方は`0`です。`heights`として報告されます。`topBound`または`bottomBound`とは併用できません。 |
| `style` | integer or string |  | 壁、スラブに使用します。壁には壁スタイルの内部インデックスを指定します（それ以外の値は`false`となり、書き込まれません）。スラブには、createSlabと同様に、スラブスタイルの名前、リソースのUUID、または内部インデックスを指定します。 |
| `height` | number |  | スラブ（スラブの基準面の高さ）、ドア、窓、柱に使用します。ワールド単位。柱の場合は`0`より大きい値で、有効な構成要素が1つの場合のみ。それ以外の場合は`false`です（柱が意匠と構造の両方の構成要素を使用する場合も含む）。 |
| `width` | number |  | ドア、窓、柱に使用します。幅（ワールド単位）。柱の場合は`0`より大きい値で、それ以外は`false`。 |
| `sizeReference` | string |  | ドア、窓に使用します。ドアは`leaf`、`unit`、`roughOpening`、窓は`sash`、`unit`、`roughOpening`を受け付けます。もう一方の種類の値を指定すると呼び出しは拒否されます。基準を変更する値には、`width`と`height`も必要です。 |
| `config` | string |  | ドアに使用します。従来のConfigポップアップ。文字列でない値は空のテキストとして書き込まれます。 |
| `idLabel` | string |  | ドア、窓に使用します。文字列でない値は空のテキストとして書き込まれます。 |
| `elevation` | number |  | 窓に使用します。窓の下端の高さ（ワールド単位）。数値である必要があります。 |
| `shape` | string |  | 柱に使用します。`Rectangular`、`Oval`、`Round`（`Oval`として読み取られます）のいずれか。それ以外のテキストは`false`と報告されます。 |
| `depth` | number |  | 柱に使用します。奥行き（ワールド単位）。`0`より大きい値で、それ以外は`false`。 |
| `diameter` | number |  | 柱に使用します。直径（ワールド単位）。柱身を`Oval`にし、`width`と`depth`を直径と等しくします。`0`より大きい値で、それ以外は`false`。`shape`、`width`、`depth`の後に書き込まれ、形状をOvalに、両方の寸法を直径に設定するため、これらより優先されます。 |
| `totalRise` | number |  | 階段（Stairs CW）に使用します。`0`より大きい値。 |
| `totalRun` | number |  | 階段（Stairs CW）に使用します。矢印の長さ（歩行線の長さ）。`0`より大きい値。 |
| `treadDepth` | number |  | 階段（Stairs CW）に使用します。`0`より大きい値。 |
| `riserHeight` | number |  | 階段（Stairs CW）に使用します。`0`より大きい値。 |
| `startTop` | number |  | 壁に使用します。始点の上端の高さ（ワールド単位）。`endHeights`として適用されます。 |
| `startBottom` | number |  | 壁に使用します。始点の下端の高さ（ワールド単位）。`endHeights`として適用されます。 |
| `endTop` | number |  | 壁に使用します。終点の上端の高さ（ワールド単位）。`endHeights`として適用されます。 |
| `endBottom` | number |  | 壁に使用します。終点の下端の高さ（ワールド単位）。個々の端点の高さで、たとえば高さが変化する壁に使用し、`endHeights`として適用されます。指定しなかった高さは現在の値を保持します。壁に読み取り可能な高さがない場合や値が数値でない場合は`false`です。`topBound`または`bottomBound`とは併用できません。 |
| `caps` | object |  | 壁に使用します。`{ leftCap, rightCap }`。丸型の端部は書き込まれません。オブジェクトでない場合、または端部の値が真偽値でない場合は`false`です。 |
| `caps.leftCap` | boolean |  | 壁の始点側の端部が閉じているかどうか。 |
| `caps.rightCap` | boolean |  | 壁の終点側の端部が閉じているかどうか。 |
| `isCurtainWall` | boolean |  | 壁に使用します。 |
| `topBound` | object |  | 壁に使用します。createWallと同じ形式で、壁の上端の高さ基準を設定します。他の値の後に適用されます。高さとは併用できません。 |
| `topBound.kind` | string | はい | 次のいずれか：`story`、`layerElevation`、`layerWallHeight`。 |
| `topBound.levelType` | string |  | ストーリのレベルタイプ。`kind`が`story`の場合は必須で、空にできません。レイヤの種類では値は無視されますが、文字列以外を指定すると、どの種類でも呼び出しが拒否されます。 |
| `topBound.relativeStory` | integer |  | 次のいずれか：`-1`、`0`、`1`。デフォルト：`0`。下階（`-1`）、壁のレイヤのストーリ（`0`）、上階（`1`）。`kind`が`story`の場合に使用します。レイヤの種類では値は無視されますが、`-1`、`0`、`1`以外の値を指定すると、どの種類でも呼び出しが拒否されます。 |
| `topBound.offset` | number |  | デフォルト：`0`。オフセット（ワールド単位）。 |
| `bottomBound` | object |  | 壁に使用します。createWallと同じ形式で、壁の下端の高さ基準を設定します。他の値の後に適用されます。高さとは併用できません。 |
| `bottomBound.kind` | string | はい | 次のいずれか：`story`、`layerElevation`、`layerWallHeight`。 |
| `bottomBound.levelType` | string |  | ストーリのレベルタイプ。`kind`が`story`の場合は必須で、空にできません。レイヤの種類では値は無視されますが、文字列以外を指定すると、どの種類でも呼び出しが拒否されます。 |
| `bottomBound.relativeStory` | integer |  | 次のいずれか：`-1`、`0`、`1`。デフォルト：`0`。下階（`-1`）、壁のレイヤのストーリ（`0`）、上階（`1`）。`kind`が`story`の場合に使用します。レイヤの種類では値は無視されますが、`-1`、`0`、`1`以外の値を指定すると、どの種類でも呼び出しが拒否されます。 |
| `bottomBound.offset` | number |  | デフォルト：`0`。オフセット（ワールド単位）。 |
| `generateGableWalls` | boolean |  | 屋根に使用します。屋根の他の属性と一緒に書き込まれます（`applied.attributes`）。指定しなかった属性は現在の値を保持します。 |
| `bearingInset` | number |  | 屋根に使用します。ワールド単位。 |
| `roofThickness` | number |  | 屋根に使用します。屋根に構成要素がある場合は無視されます。 |
| `miterType` | string |  | 屋根に使用します。次のいずれか：`vertical`、`horizontal`、`double`。 |
| `verticalMiter` | number |  | 屋根に使用します。 |
| `accessories` | object |  | 屋根に使用します。全体として書き込まれます。指定しなかったメンバーは`false`または`0`になります。 |
| `accessories.insertAttic` | boolean |  | 小屋裏を配置するかどうか。 |
| `accessories.insertSoffit` | boolean |  | 軒天井を配置するかどうか。 |
| `accessories.insertFascia` | boolean |  | 鼻隠しを配置するかどうか。 |
| `accessories.fasciaWidth` | number |  | 鼻隠し幅（ワールド単位）。 |
| `accessories.fasciaHeight` | number |  | 鼻隠しの高さ（ワールド単位）。 |
| `accessories.atticHeight` | number |  | 屋根裏の高さ（ワールド単位）。 |
| `accessories.recess` | number |  | オフセット（ワールド単位）。 |
| `accessories.rakeThickness` | number |  | 破風板の厚み（ワールド単位）。 |
| `accessories.trimDepth` | number |  | 軒先から軒天井内端の距離（ワールド単位）。 |
| `edges` | array of object |  | 屋根に使用します。3～32767個の項目。屋根の輪郭を置き換えます。 |
| `edges[].point` | [点](Common.md#points) |  | 屋根の輪郭上の点。省略した項目は、その位置にある現在の辺の点を保持します。現在の辺より後の項目には`point`と`slope`が必要です。 |
| `edges[].slope` | number |  | 度、2～90。最小値：`2`。最大値：`90`。 |
| `edges[].projection` | number |  | 壁外面から軒先の距離（ワールド単位）。省略した項目は現在の値を保持します。 |
| `edges[].eaveHeight` | number |  | レイヤの高さを基準とした軒先下端の高さ（ワールド単位）。省略した項目は現在の値を保持します。 |
| `topShape` | string |  | ドア、窓に使用します。値は上記の説明に記載されています。 |
| `leafType` | string |  | ドアに使用します。`Solid`、`Glass`、`Panel`、`Custom`のいずれか。スキーマはテキストを制限しません。 |
| `onSchedule` | boolean |  | ドア、窓に使用します。 |
| `sashOperation` | string |  | 窓に使用します。従来のパラメータ。 |
| `jambWidth` | number |  | 窓に使用します。 |
| `jambDepth` | number |  | 窓に使用します。 |
| `includeSill` | boolean |  | 窓に使用します。 |
| `sillStyle` | string |  | 窓に使用します。`Timber`、`Masonry`、`Brick`、`Open Profile Beside Frame`、`Open Profile Below Frame`、`Closed Profile`のいずれか。スキーマはテキストを制限しません。 |
| `description` | string |  | 窓に使用します。説明文。 |
| `numTreads` | integer |  | 階段：設定できません（未適用として報告されます）。 |
| `numRisers` | integer |  | 階段（Stairs CW）に使用します。1-32767。 |
| `configuration` | string |  | 階段：設定できません（未適用として報告されます）。 |
| `handrailLeft` | boolean |  | 階段：設定できません（未適用として報告されます）。 |
| `handrailRight` | boolean |  | 階段：設定できません（未適用として報告されます）。 |
| `params` | object |  | 未加工のプラグインパラメータ`{ "ParamName": value }`。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。スラブ、ドア、窓、柱、階段に適用されます。プラグインパラメータを持たない壁と屋根では、すべての項目が`false`になります。`applied.params`で報告されます。角度パラメータは度で書き込まれます。 |

**結果**

オブジェクト`{ "applied": { ... } }`を返します。オブジェクト参照はありません。`applied`は指定された値ごとに1項目を含み、書き込まれた場合は`true`、書き込まれなかった場合は`false`です。キーは、表に示す例外を除きパラメータ名と同じです。

| 種類 | `applied`のキー |
|---|---|
| 壁 | `thickness`、`line`（`start`と`end`。両方を指定した場合のみ）、`heights`（`topHeight`と`bottomHeight`）、`style`、`endHeights`（`startTop`、`startBottom`、`endTop`、`endBottom`）、`caps`、`isCurtainWall`、`topBound`、`bottomBound` |
| スラブ | `style`、`height` |
| 屋根 | `attributes`（`generateGableWalls`、`bearingInset`、`roofThickness`、`miterType`、`verticalMiter`をまとめて）、`accessories`、`edges` |
| ドア | `sizeReference`、`width`、`height`、`config`、`idLabel`、`thickness`、`topShape`、`leafType`、`onSchedule` |
| 窓 | `sizeReference`、`width`、`height`、`elevation`、`idLabel`、`topShape`、`sashOperation`、`jambWidth`、`jambDepth`、`includeSill`、`sillStyle`、`onSchedule`、`description` |
| 柱 | `shape`、`height`、`width`、`depth`、`diameter` |
| 階段 | `totalRise`、`totalRun`、`treadDepth`、`riserHeight`、`numRisers`、および常に`false`の`width`、`numTreads`、`configuration`、`handrailLeft`、`handrailRight` |

`applied.params`は、`params`の各名前に1項目を持つオブジェクト`{ "<name>": true|false }`です。スラブ、ドア、窓、柱、階段に適用されます。プラグインパラメータを持たない壁と屋根では、すべての項目が`false`になります。壁に読み取り可能な高さがない場合や値が数値でない場合、`endHeights`は`false`になります。指定しなかった高さは現在の値を保持します。屋根に属性がない場合、値の型が異なる場合、または`miterType`が不明な場合、`attributes`は`false`になります。指定しなかった属性は現在の値を保持します。

エラー：`object not found`、`not an architectural object (wall, slab, roof, door, window, column or stair)`、および注に記載された拒否（作成ツールと同じテキスト：[createWall](#createwall)（壁の高さ基準）、[createSlab](#createslab)（スラブスタイル）、[createRoof](#createroof)（`'edges' must be an array of 3 to 32767 edges`と辺ごとのテキスト）、[createDoor](#createdoor)と[createWindow](#createwindow)（寸法とプラグインスタイルの検証））。Vectorworksが壁の高さ基準を拒否した場合、呼び出しは`Vectorworks refused the wall bounds: the top must stay above the bottom, and the wall must be on a design layer`、またはストーリの問題を示すテキストで失敗します。失敗した呼び出しはロールバックされます（`rolledBack`）。
