[English](../../MCP/v2027.2/ObjectPrimitives.md) • [Deutsch](../../MCP.de/v2027.2/ObjectPrimitives.md) • **日本語**

# ObjectPrimitives — オブジェクトと2D作図

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

図面内のあらゆるオブジェクトを扱うツール（検索、調査、スタイル設定、変形、プラグインパラメータ、レコード）と、2Dプリミティブおよび文字列オブジェクトの作成、編集、測定、合成を行うツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [Draw2D](#draw2d)
  - [createLine](#createline)
  - [createRectangle](#createrectangle)
  - [createCircle](#createcircle)
  - [createArc](#createarc)
  - [createPolygon](#createpolygon)
  - [createPolyline](#createpolyline)
  - [createLocus](#createlocus)
  - [getGeometry](#getgeometry)
  - [setGeometry](#setgeometry)
  - [editVertices](#editvertices)
  - [queryGeometry](#querygeometry)
  - [combineShapes](#combineshapes)
  - [createText](#createtext)
  - [getText](#gettext)
  - [editText](#edittext)
- [Objects](#objects)
  - [findObjects](#findobjects)
  - [getObjectsAtPoint](#getobjectsatpoint)
  - [getObjectInfo](#getobjectinfo)
  - [getObjectAttributes](#getobjectattributes)
  - [setObjectAttributes](#setobjectattributes)
  - [copyAttributes](#copyattributes)
  - [editObject](#editobject)
  - [getObjectParameters](#getobjectparameters)
  - [getObjectRecords](#getobjectrecords)
  - [setObjectParameter](#setobjectparameter)
  - [getPluginDefinition](#getplugindefinition)
  - [createPluginObject](#createpluginobject)

<a id="overview"></a>

## 概要

このフォルダには、2個のツールグループに合計27個のツールが含まれています。

| グループ | グループID | 初期状態で有効 | リスクレベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [Draw2D](#draw2d) | `draw2d` | いいえ | 低 | 15 | 2Dプリミティブの作成、編集、測定、合成と、文字列オブジェクトの作成、読み取り、編集を行います。 |
| [Objects](#objects) | `objects` | はい | 中 | 12 | あらゆるオブジェクトの検索、調査、編集を行い、属性、変形、コンテナ、プラグインパラメータ、レコードを扱います。 |

## Draw2D

> **グループ:** `Draw2D` · **グループID:** `draw2d` · **初期状態で有効:** いいえ · **リスクレベル:** 低 · **ツール数:** 15

**2Dプリミティブの作成、編集、測定、合成と、文字列オブジェクトの作成、読み取り、編集を行います。**

2Dプリミティブの形状（直線、四角形、角丸四角形、円、円弧、多角形、曲線、基準点）を作成、編集、測定します。2つの2D図形をブーリアン演算で合成します（combineShapes：union、intersection、difference = 最初の図形から2番目の図形を引く演算、およびsymmetricDifference。対象は直線、四角形、角丸四角形、長円、円弧と円、多角形（フリーハンドを除く）、曲線です。結果は、最初の図形の属性を持つ任意の種類の新しい2Dオブジェクトで、その図形のコンテナに配置されます。`deleteOriginals`で指定しない限り元の図形は変更されません。ただし、2番目の図形が別の平面上にある場合は、先に最初の図形の平面に移動します。結果が空の場合は、図形なしの成功となります）。また、文字列オブジェクトの作成、読み取り、編集を行い（createText、getText、editText）、その内容、文字範囲の書式、文字スタイル、位置揃え、行間、折り返し、タブストップを扱います。

座標はワールド単位、角度はラジアンです。新しいオブジェクトはアクティブレイヤに、combineShapesの結果は最初の図形のコンテナに配置されます。各変更は、固有の名前を持つ、取り消し可能なVectorworksの操作として実行されます。queryGeometryは、図面を変更せずに最近点、距離、包含、交差、接線に関する問い合わせに応答し、多角形と曲線を実際の曲線に沿って測定します（長さ、指定距離の位置の点、接線、曲率、および等分）。

| ツール | 作用 | リスク | 概要 |
|---|---|---|---|
| [`createLine`](#createline) | 編集 | 低 | 2点間に直線を作成します。 |
| [`createRectangle`](#createrectangle) | 編集 | 低 | 四角形を作成し、必要に応じて回転や角丸を設定します。 |
| [`createCircle`](#createcircle) | 編集 | 低 | 中心と半径、または通過する3点から円を作成します。 |
| [`createArc`](#createarc) | 編集 | 低 | 中心、半径、角度、または通過する3点から円弧を作成します。 |
| [`createPolygon`](#createpolygon) | 編集 | 低 | 点から多角形を作成するか、正多角形を作成します。 |
| [`createPolyline`](#createpolyline) | 編集 | 低 | 任意の種類の頂点から曲線を作成するか、丸みのある図形を作成します。 |
| [`createLocus`](#createlocus) | 編集 | 低 | 2D 基準点（参照点）を作成します。 |
| [`getGeometry`](#getgeometry) | 読み取り専用 | 低 | 2Dプリミティブの種類固有の形状を読み取ります。 |
| [`setGeometry`](#setgeometry) | 編集 | 低 | 2Dプリミティブの形状を編集します。 |
| [`editVertices`](#editvertices) | 編集 | 低 | 多角形または曲線の頂点を追加、挿入、変更、削除、順序反転、置換します。 |
| [`queryGeometry`](#querygeometry) | 読み取り専用 | 低 | 2Dプリミティブの最近点、距離、包含、交差、接線、および曲線に沿った測定に関する幾何学的な問い合わせに応答します。 |
| [`combineShapes`](#combineshapes) | 編集 | 低 | 和集合、共通部分、差分、対称差のブーリアン演算で2つの2D図形を合成します。 |
| [`createText`](#createtext) | 編集 | 低 | 文字列オブジェクトを作成します。 |
| [`getText`](#gettext) | 読み取り専用 | 低 | 文字列オブジェクトの内容、文字書式、スタイル、レイアウトを読み取ります。 |
| [`editText`](#edittext) | 編集 | 低 | 文字列オブジェクトの内容と書式を編集します。 |

### createLine

2点間に直線を作成します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: createLine" · **runToolBatch内:** はい

**詳細**

`start`と`end`の2点間に直線を作成します。

> **注:** `start`と`end`はどちらも必須です（`'start' and 'end' points are required`）。指定された値が[点](Common.md#points)でない場合は、エラーにならずに(0, 0)として読み取られます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `start` | [点](Common.md#points) | はい | 始点。 |
| `end` | [点](Common.md#points) | はい | 終点。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createRectangle

四角形を作成し、必要に応じて回転や角丸を設定します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: createRectangle" · **runToolBatch内:** はい

**詳細**

`center`を中心として、`width`と`height`を持つ四角形を作成し、省略可能な`angle`（ラジアン）で回転を指定します。正の`cornerRadius`、または楕円形の角を指定する`cornerDiameters` { alongWidth, alongHeight }（幅方向と高さ方向の辺に沿った角の直径）を指定すると、角丸四角形を作成します。`proportional`を指定すると、対話操作でサイズを変更したときに角も比例して拡大縮小されます。

> **注:** `width`と`height`は0にできません（`'width' and 'height' must be non-zero`）。`center`はチェックされません。`center`がない場合や形式が正しくない場合は(0, 0)として読み取られます。`cornerDiameters`は`cornerRadius`より優先されます。0以下の`cornerRadius`は無視され、負の角の直径は拒否されます（`'cornerDiameters' must not be negative`）。`proportional`は角丸四角形でのみ有効です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `center` | [点](Common.md#points) | はい | 中心点。 |
| `width` | number | はい | 幅。ワールド単位。 |
| `height` | number | はい | 高さ。ワールド単位。 |
| `angle` | number |  | 反時計回りの角度。ラジアン。 |
| `cornerRadius` | number |  | 角の半径。ワールド単位。0より大きい値の場合のみ角丸四角形になります。両方を指定した場合は`cornerDiameters`が優先されます。 |
| `cornerDiameters` | object |  | 楕円形の角：角の楕円の直径。`cornerRadius`より優先されます。どちらの値も負にできません。どのような形で指定しても角丸四角形になり、省略したメンバーは0になります。 |
| `cornerDiameters.alongWidth` | number |  | 幅方向の辺に沿った角の直径（ワールド単位）。デフォルトは0。 |
| `cornerDiameters.alongHeight` | number |  | 高さ方向の辺に沿った角の直径（ワールド単位）。デフォルトは0。 |
| `proportional` | boolean |  | 角丸四角形のみ：対話操作でサイズを変更したときに角も拡大縮小されます。デフォルトはfalse。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createCircle

中心と半径、または通過する3点から円を作成します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: createCircle" · **runToolBatch内:** はい

**詳細**

`center`を中心として`radius`を持つ円、または`threePoints`の3点を通る円を作成します。

> **注:** `threePoints`を指定した場合はそれが優先されます。ちょうど3つの点が必要で（点でない項目はスキップされます）、そうでない場合は`'threePoints' must hold exactly three points`になります。また、3点が一致したり一直線上に並んだりしてはいけません（`failed to create the object: the three points coincide or are collinear`）。それ以外の場合、`radius`は正の値である必要があります（`'radius' must be positive`）。`center`はチェックされず、`center`がない場合や形式が正しくない場合は(0, 0)として読み取られます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `center` | [点](Common.md#points) |  | 中心点。 |
| `radius` | number |  | 半径。ワールド単位。 |
| `threePoints` | array of [点](Common.md#points) |  | 円周上の3点。`center`と`radius`より優先されます。3項目。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createArc

中心、半径、角度、または通過する3点から円弧を作成します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: createArc" · **runToolBatch内:** はい

**詳細**

`center`を中心として、`radius`、`startAngle`、`sweepAngle`（ラジアン、反時計回り）を持つ円弧、または`threePoints` [start, 円弧上の点, end]を通る円弧を作成します。

> **注:** `threePoints`を指定した場合はそれが優先され、createCircleと同じチェックが行われます。指定しない場合、`radius`は正の値、`sweepAngle`は0以外である必要があります（`'radius' must be positive and 'sweepAngle' non-zero (radians)`）。`startAngle`のデフォルトは0で、`center`がない場合や形式が正しくない場合は(0, 0)として読み取られます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `center` | [点](Common.md#points) |  | 中心点。 |
| `radius` | number |  | 半径。ワールド単位。 |
| `startAngle` | number |  | 反時計回りの開始角度。ラジアン。 |
| `sweepAngle` | number |  | 円弧角。ラジアン。正の値は反時計回り。 |
| `threePoints` | array of [点](Common.md#points) |  | 始点、円弧上の点、終点。`center`、`radius`、角度より優先されます。3項目。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createPolygon

点から多角形を作成するか、正多角形を作成します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: createPolygon" · **runToolBatch内:** はい

**詳細**

`points`配列から多角形を作成するか（`closed`を指定可能。デフォルトはtrue）、`center`/`radius`/`sides`から正多角形を作成します（`startAngle`は省略可能）。

> **注:** `sides`を指定すると正多角形が作成され、`points`は読み取られません。その場合、3以上の`sides`と正の`radius`が必要で（`a regular polygon needs 'sides' >= 3 and 'radius' > 0`）、`center`がない場合や形式が正しくない場合は(0, 0)として読み取られます。`sides`を指定しない場合、`points`には2つ以上の点が必要で（点でない項目はスキップされます）、そうでない場合は`provide 'points' (>= 2), or 'center'/'radius'/'sides' for a regular polygon`になります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `points` | array of [点](Common.md#points) |  | 順序どおりの点（2つ以上）。`sides`を指定した場合は読み取られません。 |
| `closed` | boolean |  | 図形が閉じているかどうか。デフォルトはtrue。`points`を使う場合のみ使用されます。 |
| `center` | [点](Common.md#points) |  | 中心点。 |
| `radius` | number |  | 半径。ワールド単位。 |
| `sides` | integer |  | 正多角形の辺の数（3以上）。指定した場合、`points`は読み取られません。数値でない値は3として読み取られます。 |
| `startAngle` | number |  | 反時計回りの開始角度。ラジアン。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createPolyline

任意の種類の頂点から曲線を作成するか、丸みのある図形を作成します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: createPolyline" · **runToolBatch内:** はい

**詳細**

`vertices`配列から曲線を作成します。各頂点は{ x, y, type?, arcRadius?, visible? }で、typeはcorner|bezier|cubic|arc|radiusです。visibleがfalseの場合、次の頂点までの辺を非表示にします。`closed`は省略可能です（デフォルトはfalse）。`vertices`を指定しない場合、`center`と`radius`で4個の円弧頂点からなる閉じた円を、`center`と`width`および`height`で、角が`cornerRadius`を持つ円弧頂点となる閉じた長方形を作成します（デフォルトは0：角を丸めません。上限は短い方の辺の半分）。

> **注:** `vertices`を指定した場合はそれが優先されます。2つ以上の頂点が必要で（点を含まない項目はスキップされます）、そうでない場合は`provide 'vertices' (>= 2), each { x, y, type?, arcRadius?, visible? }, or 'center' with 'radius' (circle) or with 'width'/'height' (filleted rectangle)`になります。`vertices`を指定しない場合、`radius`は`width`と`height`より優先されます。円には正の`radius`が必要です（`'radius' must be positive`）。長方形には0以外の`width`と`height`、および負でない`cornerRadius`が必要です（`'width' and 'height' must be non-zero and 'cornerRadius' must not be negative`）。`center`がない場合や形式が正しくない場合は(0, 0)として読み取られます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `vertices` | array of object |  | 頂点を順番に指定します（2つ以上）。各項目はオブジェクトまたは点`[x, y]`です。点を含まない項目はスキップされます。 |
| `vertices[].x` | number |  | X座標（ワールド単位）。 |
| `vertices[].y` | number |  | Y座標（ワールド単位）。 |
| `vertices[].type` | string |  | 次のいずれか：`corner`、`bezier`、`cubic`、`arc`、`radius`。デフォルトは`corner`。不明な`type`は`corner`として読み取られます。 |
| `vertices[].arcRadius` | number |  | `arc`頂点の半径（ワールド単位）。他の種類の頂点では無視されます。デフォルトは0。 |
| `vertices[].visible` | boolean |  | falseの場合、次の頂点までの辺を非表示にします。デフォルトはtrue。 |
| `closed` | boolean |  | 図形が閉じているかどうか。デフォルトはfalse。`vertices`を使う場合のみ使用されます。 |
| `center` | [点](Common.md#points) |  | 中心点。 |
| `radius` | number |  | 半径。ワールド単位。 |
| `width` | number |  | 幅。ワールド単位。 |
| `height` | number |  | 高さ。ワールド単位。 |
| `cornerRadius` | number |  | 角の半径。ワールド単位。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createLocus

2D 基準点（参照点）を作成します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: createLocus" · **runToolBatch内:** はい

**詳細**

`position`に2D 基準点（参照点／スナップ点）を作成します。

> **注:** `position`はチェックされません。`position`がない場合や形式が正しくない場合は、エラーにならずに(0, 0)に基準点が作成されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### getGeometry

2Dプリミティブの種類固有の形状を読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

2Dプリミティブの種類（`kind`）固有の形状を読み取ります。

**直線：** start、end、length、angle、midPoint、direction（単位ベクトル）。

**円：** center、radius、diameter、circumference。

**円弧：** center、radius、startAngle、sweepAngle、endAngle、startPointとendPoint（弦の両端）、midPoint、length（円弧に沿った長さ）、chordLength、sagitta。

**四角形（Rectangle）と角丸四角形（RoundedRectangle）：** center、width、height、angle、origin（最初の角）、direction（幅方向の辺に沿った単位ベクトル）、corners（originから反時計回り）、isAxisAlignedに加え、isSquare（四角形）、またはcornerRadius、cornerDiameters { alongWidth, alongHeight }、hasCircularCorners（角丸四角形）。

**基準点：** position、masterSnapPoint、showMasterSnapOutsideSnapBox。

**多角形：** closed、isFreehand、points（次の点までの辺が非表示になっている点はvisibleがfalse）。

**曲線：** closed、hasCurves、vertices { x, y, type, arcRadius, maxRadius（円弧頂点に収まる最大半径）, controlPoint（保存されている制御点。x/yと異なる場合）, visible }。多角形と曲線は、頂点数、面積、周長、重心、および時計回り／凸／自己交差のフラグも返します。

> **注:** 結果は[オブジェクト参照](Common.md#object-references)のキーで始まり、その後に`kind`（`Line`、`Circle`、`Arc`、`Rectangle`、`RoundedRectangle`、`Locus`、`Polyline`、`Polygon`のいずれか）が続きます。それ以外のオブジェクトでも呼び出しは成功し、`kind`なしでオブジェクト参照だけを返します。オブジェクトが報告できない値は省略されます。頂点数のキーは`vertexCount`です。その後に`area`、`perimeter`、`centroid`、`clockwise`、`convex`、`selfIntersecting`が、それぞれ計算できた場合にのみ続きます。曲線の頂点は、`arcRadius`が0でない場合にのみそれを報告します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |

### setGeometry

2Dプリミティブの形状を編集します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: setGeometry" · **runToolBatch内:** はい

**詳細**

uuidで2Dプリミティブの形状を編集します。その種類のフィールドを指定してください。

**直線：** start、end、length、angle、extendStart/extendEnd（端を延長。負の値は短縮）、offsetParallel（横方向に移動。正の値はstart→endに対して左側）、reverse（両端を入れ替え）。

**円：** threePoints（円周上の3点）、center、radius、diameter。startAngle/sweepAngle/endAngleを指定すると円弧に変わります。

**円弧：** threePoints [start, 円弧上の点, end]、center、radius、startAngle（終了角度を保持）、sweepAngleとendAngle（開始角度を保持）。startAngleとsweepAngleを併用すると両方を設定します。

**四角形と角丸四角形：** center、angle、width/height（中心を保持）、originとdirection（最初の角と幅方向の辺を配置し、サイズを保持）、bounds { left, top, right, bottom }（回転なし）。角丸四角形ではcornerRadiusとcornerDiameters { alongWidth, alongHeight }も使用できます。

**基準点：** position、masterSnapPoint、showMasterSnapOutsideSnapBox（シンボル定義内でのスナップ動作）。多角形と曲線にはeditVerticesを使用してください。

> **注:** オブジェクトの種類が使用するフィールドだけが書き込まれます。それ以外のフィールドは無視され、`applied`に項目は追加されず、エラーにもなりません（通常の四角形での`cornerRadius`と`cornerDiameters`、円弧での`angle`、直線での`radius`など）。円では、`startAngle`、`sweepAngle`、`endAngle`は円を円弧として編集するため、円弧角が1回転のままでない限り円弧に変わります。`width`または`height`を単独で指定すると、もう一方の辺は保持されます。`threePoints`と`bounds`以外の値は型がチェックされません。指定された点が[点](Common.md#points)でない場合は(0, 0)として、指定された数値が数値でない場合は0として読み取られ（このとき`radius`、`diameter`、`sweepAngle`は`applied`が`false`になって失敗し、それ以外は0が書き込まれます）、基準点の真偽値が真偽値でない場合は`false`として読み取られます。現在の値にフォールバックするのは、`origin`、`direction`、`width`、`height`、および`cornerDiameters`のメンバーだけです。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `start` | [点](Common.md#points) |  | 直線で使用します。始点。 |
| `end` | [点](Common.md#points) |  | 直線で使用します。終点。 |
| `length` | number |  | 直線で使用します。長さ（ワールド単位）。`start`は固定され、`end`が直線に沿って移動します。長さ0の直線では`applied.length`がfalseになります。 |
| `angle` | number |  | 直線、四角形、角丸四角形で使用します。反時計回りの角度。ラジアン。直線は`start`を中心に回転して長さを保ち、四角形はその中心を中心に回転します。 |
| `extendStart` | number |  | 直線で使用します。始点側に追加する長さ（ワールド単位）。負の値は短縮します。 |
| `extendEnd` | number |  | 直線で使用します。終点側に追加する長さ（ワールド単位）。負の値は短縮します。 |
| `offsetParallel` | number |  | 直線で使用します。横方向に移動します。正の値はstart→endに対して左側です。 |
| `reverse` | boolean |  | 直線で使用します。`true`で両端を入れ替えます。`false`は無視され、`applied`に項目は追加されません。 |
| `center` | [点](Common.md#points) |  | 円、円弧、四角形、角丸四角形で使用します。中心点。 |
| `radius` | number |  | 円、円弧で使用します。半径。ワールド単位。 |
| `diameter` | number |  | 円で使用します。直径。ワールド単位。 |
| `threePoints` | array of [点](Common.md#points) |  | 円と円弧で使用します。円周上の3点。円弧の場合は始点、円弧上の点、終点。一直線上にない3点がちょうど指定された場合を除き、`applied.threePoints`はfalseになります。3項目。 |
| `startAngle` | number |  | 円、円弧で使用します。反時計回りの開始角度。ラジアン。単独で指定すると終了角度を保持し、`sweepAngle`と併用すると両方を設定します。 |
| `sweepAngle` | number |  | 円、円弧で使用します。円弧角。ラジアン。正の値は反時計回り。単独で指定すると開始角度を保持します。 |
| `endAngle` | number |  | 円と円弧で使用します。終了角度。ラジアン。開始角度は保持されます。 |
| `width` | number |  | 四角形と角丸四角形で使用します。幅。ワールド単位。 |
| `height` | number |  | 四角形と角丸四角形で使用します。高さ。ワールド単位。`width`と`height`は中心を保持し、指定しなかった方は現在の値を保持します。 |
| `origin` | [点](Common.md#points) |  | 四角形と角丸四角形で使用します。最初の角。`direction`とともに四角形を配置し、サイズを保持します。指定しなかった方は現在の値を保持します。 |
| `direction` | [点](Common.md#points) |  | 四角形と角丸四角形で使用します。幅方向の辺の向き。getGeometryが返すものと同じ単位ベクトルです。`origin`を参照してください。 |
| `bounds` | [矩形](Common.md#rectangles) |  | 四角形と角丸四角形で使用します。回転なしの矩形。`left`、`top`、`right`、`bottom`の4つすべてが数値である必要があり、そうでない場合は`applied.bounds`がfalseになります。 |
| `cornerRadius` | number |  | 角丸四角形でのみ使用し、通常の四角形では無視されます。角の半径。ワールド単位。 |
| `cornerDiameters` | object |  | 角丸四角形でのみ使用し、通常の四角形では無視されます。省略したメンバーは現在の値を保持します。 |
| `cornerDiameters.alongWidth` | number |  | 幅方向の辺に沿った角の直径（ワールド単位）。 |
| `cornerDiameters.alongHeight` | number |  | 高さ方向の辺に沿った角の直径（ワールド単位）。 |
| `position` | [点](Common.md#points) |  | 基準点で使用します。挿入点。 |
| `masterSnapPoint` | boolean |  | 基準点で使用します。マスタースナップポイントのフラグ（シンボル定義内でのスナップ動作）。 |
| `showMasterSnapOutsideSnapBox` | boolean |  | 基準点で使用します。シンボル定義内でのスナップ動作。 |

**結果**

| キー | 説明 |
|---|---|
| `applied` | 指定され、かつオブジェクトの種類で使用される値ごとに1項目。書き込まれた場合は`true`。 |

結果にはオブジェクト参照は含まれません。`applied`のキーはパラメータ名ですが、`extend`（`extendStart`と`extendEnd`）、`size`（`width`と`height`）、`frame`（`origin`と`direction`）、`angles`（`startAngle`と`sweepAngle`の併用）は例外です。

エラー：`object not found`、`this object's geometry cannot be edited with setGeometry; polygons and polylines are edited with editVertices`（直線、円、円弧、四角形、角丸四角形、基準点以外のオブジェクト）。この場合、呼び出しは何も変更しません（`rolledBack`）。

### editVertices

多角形または曲線の頂点を追加、挿入、変更、削除、順序反転、置換します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: editVertices" · **runToolBatch内:** はい

**詳細**

多角形または曲線の頂点を編集します。`action`：add（`point`を末尾に追加）、insert（`index`の前に`point`を挿入）、set（`index`の頂点の`point`、`type`、`arcRadius`、または辺の`visible`フラグを変更）、delete（`index`）、deleteAll、reverse、replace（すべての頂点を置換。すべての辺を表示する`points`から、またはcreatePolylineと同じ`vertices` { x, y, type?, arcRadius?, visible? }から指定。2個以上が必要で、閉じた状態のフラグは保持）。addとinsertでは、新しい頂点の`type`、`arcRadius`、`visible`も指定できます。

頂点の`type`（corner|bezier|cubic|arc|radius）と`arcRadius`は曲線にのみ適用されます。`closed`、`clockwise`、`allVerticesVisible`は、どのアクションでも設定できます。`applied`と、更新後の頂点数、面積、周長、重心、図形のフラグを返します。

> **注:** `action`を省略すると`set`になります。`index`は頂点を0から数え（0未満は0として扱われます）、`insert`、`set`、`delete`で使用されます。`add`は末尾に追加します。失敗した編集はエラーにならず、`applied`の該当項目が`false`になります。キー`index`は、内部インデックスによるオブジェクトの参照にも使われます（[オブジェクト参照](Common.md#object-references)を参照）。`uuid`と`name`でオブジェクトが見つからない場合は、内部インデックスが`index`のオブジェクトが代わりに編集されます。必ず有効な`uuid`を送信してください。値はチェックされません。真偽値でない`closed`、`clockwise`、`allVerticesVisible`はfalseとして、不明な`type`は`corner`として、数値でない`arcRadius`は0として読み取られ、そのまま書き込まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 頂点のインデックス（0から数える）。`insert`（新しい頂点はその前に入ります）、`set`、`delete`で使用します。内部インデックスによる参照でもあります。注を参照してください。 |
| `action` | string |  | 次のいずれか：`add`、`insert`、`set`、`delete`、`deleteAll`、`reverse`、`replace`。デフォルトは`set`。 |
| `point` | [点](Common.md#points) |  | `add`と`insert`（これらでは必須）、および`set`で使用する頂点の点。 |
| `type` | string |  | 次のいずれか：`corner`、`bezier`、`cubic`、`arc`、`radius`。曲線のみ。`add`と`insert`ではデフォルトが`corner`で、`set`では`index`の頂点を変更します。 |
| `arcRadius` | number |  | 曲線のみ。頂点の円弧半径（ワールド単位、0以上）。`add`と`insert`では`type`が`arc`の場合のみ使用されます（デフォルトは0）。`set`では、同じ呼び出しの`type`が別の種類を指定していても、頂点をその半径の`arc`頂点にします。負の値では`applied.arcRadius`がfalseになります。 |
| `visible` | boolean |  | 頂点から次の頂点までの辺を表示するかどうか。`add`と`insert`ではデフォルトがtrueで、`set`では`index`の頂点を変更します。 |
| `points` | array of [点](Common.md#points) |  | `replace`で使用する点（順序どおり）。すべての辺が表示されます。2つ以上。両方を指定した場合は`vertices`が優先されます。 |
| `vertices` | array of object |  | `replace`で使用する頂点。createPolylineと同じ形式で2つ以上指定します。点を含まない項目はスキップされます。多角形では角の頂点として扱われます。 |
| `vertices[].x` | number |  | X座標（ワールド単位）。 |
| `vertices[].y` | number |  | Y座標（ワールド単位）。 |
| `vertices[].type` | string |  | 次のいずれか：`corner`、`bezier`、`cubic`、`arc`、`radius`。デフォルトは`corner`。 |
| `vertices[].arcRadius` | number |  | 円弧の半径（ワールド単位）。`type`が`arc`の場合のみ使用されます。デフォルトは0。 |
| `vertices[].visible` | boolean |  | 次の頂点までの辺を表示するかどうか。デフォルトはtrue。 |
| `closed` | boolean |  | 図形が閉じているかどうか。どのアクションとも指定できます。`replace`自体は現在のフラグを保持します。 |
| `clockwise` | boolean |  | 頂点の順序：trueは時計回り、falseは反時計回り。どのアクションとも指定できます。 |
| `allVerticesVisible` | boolean |  | trueですべての頂点の辺を表示し、falseですべて非表示にします。どのアクションとも指定できます。 |

**結果**

オブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）、`applied`、および編集後の図形の測定値。

| キー | 説明 |
|---|---|
| `applied` | 編集と、指定された`closed`、`clockwise`、`allVerticesVisible`ごとに1項目。書き込まれた場合は`true`。編集の項目名は`action`（`add`、`insert`、`delete`、`deleteAll`、`reverse`、`replace`）です。`set`では、指定された`point`、`type`、`arcRadius`、`visible`ごとに1項目です。多角形では`type`と`arcRadius`の項目はなく、有効な点でない`point`にも項目はありません。頂点が2つ未満の`replace`は`replace: false`になります。 |
| `vertexCount` | 頂点数。 |
| `area`、`perimeter`、`centroid` | 図形の測定値。それぞれVectorworksが計算できる場合のみ含まれます。 |
| `clockwise`、`convex`、`selfIntersecting` | 図形のフラグ。それぞれVectorworksが計算できる場合のみ含まれます。 |

エラー：`object not found`、`object is not a polygon or a polyline`、`'point' is required to add or insert a vertex`、`unknown 'action' (add, insert, set, delete, deleteAll, reverse, replace)`。エラーの後、呼び出しは何も変更しません（`rolledBack`）。

### queryGeometry

2Dプリミティブの最近点、距離、包含、交差、接線、および曲線に沿った測定に関する幾何学的な問い合わせに応答します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

2Dプリミティブを変更せずに、幾何学的な問い合わせに応答します。`operation`：closestPoint（`point`を指定。オブジェクト上の最も近い`point`とその`distance`を返す）とdistanceTo（`point`を指定。`distance`を返す）は、直線、円弧、円（円周まで）、四角形、多角形、曲線、基準点が対象です。contains（`point`を指定。内部または境界上ならtrue）は、円、四角形、閉じた多角形／曲線が対象です。intersect（`points`を返す）は、オブジェクト`otherUuid`または線分`lineStart`-`lineEnd`との交差を求めます。直線、円弧、円、四角形、多角形、曲線は線分および直線オブジェクトと交差し、円弧と円は互いにも交差します。pointAt（ラジアンの`angle`を指定。`point`を返す）とtangentPoints（`point`を指定。その点を通る接線の円上の接点`points`を返す。円の内部の点からは接点なし）は円が対象です。

多角形と曲線では次の操作も使用できます。curveLength（`length`を返す）。pointAtDistance（曲線の始点からの`distance`を0から曲線の長さまでの範囲で指定。`point`、単位ベクトルの`tangent`（その位置での曲線の方向）、および`curvature`（1 / 半径。直線の辺では0）を返す。曲線に方向がない位置では接線と曲率は省略）。divide（始点から曲線に沿って等間隔に`count`個の点（2～10000）。`includeEnd`がtrue（デフォルト）の場合は最後の点を終点に置き、閉じた曲線ではその点は再び始点になる。falseの場合は長さ / countの間隔で配置し、終点を含めない。`points`を返す）。

多角形と曲線は、描画されているとおりの実際の曲線（制御点ではなく円弧とスプライン）に沿って測定されます。対象は、非表示の辺と閉じる辺を含む外周のパスで、穴は含みません。これはclosestPoint、distanceTo、curveLength、pointAtDistance、divideに適用されます。一方、containsとintersectは代わりに頂点の多角形（頂点間を直線で結び、曲線の頂点は角として扱う）を使用します。実際の曲線に対する包含判定はありません。

四角形は4つの角に沿って測定されます（角丸は無視されます）。

> **注:** 角丸四角形は四角形として扱われます。`otherUuid`を使う`intersect`は、2つのオブジェクトの一方が直線の場合（もう一方は、`intersect`が線分との交差を受け付ける任意のオブジェクトでかまいません）、または両方が円弧か円の場合に機能し、それ以外の組み合わせは拒否されます。`otherUuid`は`lineStart`と`lineEnd`より優先されます。`pointAt`と`tangentPoints`は円のみを受け付け、円弧は拒否されます。開いた多角形または曲線に対する`contains`は拒否されず、辺上の点に対しても`false`を返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `operation` | string | はい | 次のいずれか：`closestPoint`、`distanceTo`、`contains`、`intersect`、`pointAt`、`tangentPoints`、`curveLength`、`pointAtDistance`、`divide`。 |
| `point` | [点](Common.md#points) |  | closestPoint、distanceTo、contains、tangentPointsで使用する点（これらでは必須）。 |
| `otherUuid` | string |  | intersect用：もう一方のオブジェクトのUUID。UUIDのみで検索します。 |
| `lineStart` | [点](Common.md#points) |  | intersect用：線分の始点。`lineEnd`と併用します。形式が正しくない点は(0, 0)として読み取られます。 |
| `lineEnd` | [点](Common.md#points) |  | intersect用：線分の終点。`lineStart`と併用します。 |
| `angle` | number |  | pointAt用（必須）。反時計回りの角度。ラジアン。 |
| `distance` | number |  | pointAtDistance用（必須）。曲線の始点からの距離（0から曲線の長さまで、ワールド単位）。 |
| `count` | integer |  | divide用（必須）。点の数（2～10000）。 |
| `includeEnd` | boolean |  | divide用。true（デフォルト）では最後の点を曲線の終点に置き、falseでは長さ / countの間隔で点を配置し、終点を含めません。 |

**結果**

結果にはオブジェクト参照は含まれません。キーは`operation`によって異なります。

| 操作 | キー |
|---|---|
| `closestPoint` | `distance`と`point`（オブジェクト上の最も近い点）。 |
| `distanceTo` | `distance`。 |
| `contains` | `contains`（trueまたはfalse）。 |
| `intersect` | `points`（交差点）。オブジェクトが交差しない場合は空のリストです。 |
| `pointAt` | `point`。 |
| `tangentPoints` | `points`（接線が`point`を通る円上の点）。円の内部の点からは空のリストです。 |
| `curveLength` | `length`（ワールド単位）。 |
| `pointAtDistance` | `point`、単位ベクトルの`tangent`、`curvature`。曲線に方向がない位置では後の2つは省略されます。 |
| `divide` | `points`。 |

エラー：`object not found`、`unknown 'operation' (closestPoint, distanceTo, contains, intersect, pointAt, tangentPoints, curveLength, pointAtDistance, divide)`（`operation`がない場合も）、`'<operation>' needs 'point'`、`the 'otherUuid' object was not found`、`'intersect' needs 'otherUuid', or 'lineStart' and 'lineEnd'`、`'intersect' does not support this combination of objects`、`'pointAt' needs the number 'angle' (radians)`、`'<operation>' supports circles only`、`'contains' supports circles, rectangles, polygons and polylines`、`'<operation>' supports lines, arcs, circles, rectangles, polygons, polylines and loci`、`'<operation>' supports polygons and polylines only`、`'pointAtDistance' needs 'distance', a number from 0 to the length of the curve, <length> (world units)`、`'divide' needs 'count', a whole number of points from 2 to 10000`、`'includeEnd' must be true or false`、`Vectorworks could not measure the curve of the polygon or polyline: it needs two vertices or more and a curve that is not degenerate`、`failed to read the circle`（pointAt）、`Vectorworks could not find the point at 'distance' on the curve`（pointAtDistance）。

### combineShapes

和集合、共通部分、差分、対称差のブーリアン演算で2つの2D図形を合成します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: combineShapes" · **runToolBatch内:** はい

**詳細**

加工 &gt; 貼り合わせ、切り欠き、抜き取りと同様に、2つの2D図形をブーリアン演算で合成しますが、指示しない限り元の図形を保持します。`operation`：union（いずれかの図形の領域）、intersection（両方の図形に共通する領域）、difference（最初の図形から2番目の図形を引く：`firstUuid`から`secondUuid`を引く。2番目の図形が直線の場合は、最初の図形を完全に横切る箇所で最初の図形を分割）、symmetricDifference（どちらか一方だけに属する領域）。

`firstUuid`と`secondUuid`は異なる2つの図形で、直線、四角形、角丸四角形、長円、円弧と円、多角形（フリーハンドを除く）、曲線のいずれかです。文字列、グループ、シンボル、プラグインオブジェクト、3Dオブジェクトは使用できません。2つの図形は同一平面上にある必要があります。異なる平面上にある場合（例：2D/平面で、一方がスクリーンプレーン、もう一方がレイヤプレーンにある場合）、加工 &gt; 貼り合わせと同様に、先に2番目の図形を最初の図形の平面に移動します。これにより2番目の元の図形の平面が変わり、結果に`planesAligned` trueが追加されます。同一平面上に揃わない図形は拒否されます。

頂点が3個以上ある開いた多角形または曲線は直線の辺で閉じたものとして、円弧は弦で閉じたものとして扱います。直線は領域を囲まないため、differenceの2番目の図形としてのみ意味があります。最初の図形は、レイヤ、シンボル定義、またはそれらの中のグループに属する必要があります（壁、プラグインオブジェクト、ビューポート、またはそれらの中のグループは不可）。呼び出しによって2番目の図形が変更される場合（`deleteOriginals`がboth、または最初の図形の平面への移動）は、2番目の図形も同様です。

結果は任意の種類の新しい2Dオブジェクトです（通常は曲線。多角形の場合や、新しい輪郭が不要なときは図形のコピーになる場合もあります。たとえば、重なりのないdifferenceでは最初の図形のコピーになります）。最初の図形のグラフィック属性、レコード、表示状態、およびそのクラスを引き継ぎます（`class`で別のクラスを指定でき、`useClassAttributes`で属性をクラスに従わせます）。

結果は最初の図形のコンテナ内で、そのオブジェクトより前面に、ロック解除の状態で配置され、`select`を指定した場合のみ選択されます。周囲のグループの境界もそれに合わせて更新されます。元の図形は、平面の位置合わせを除き、`deleteOriginals`がfirstまたはbothでない限り変更されません（デフォルトはnone）。結果の図形がない場合、何も削除されません。ロックされた最初の図形も合成できますが、呼び出しによって削除または別の平面への移動が行われる図形がロックされている場合は拒否されます。

領域のない合成（重なりのない図形のintersection、2番目の図形が最初の図形を覆う、または最初の図形が直線であるdifference、同一図形のsymmetricDifference。Vectorworksのモデリングの失敗も同様に報告されます）は、図形なしで`note`を伴う成功となります。空のunionはエラーです。`name`は単一の結果に名前を付けます。合成結果が複数の図形になる場合や、別のオブジェクトがその名前を持っている場合は拒否されます。

何かを変更する前に、すべての引数を検証します。拒否された呼び出しは何も変更しません。1回の呼び出しは1つの取り消しステップで、取り消すと位置合わせした図形の平面も元に戻ります。`operation`、`count`、`shapes`（新しいオブジェクトの参照）、`deleted`（削除した元の図形のUUID）、`planesAligned`（図形の平面を1つに揃えた場合はtrue）、および結果がない場合は`note`を返します。

> **注:** 頂点が2つ未満の多角形または曲線、および2つの頂点が一致するか、両方が角の頂点ではない2頂点の曲線は、上記の一覧には記載されていませんが、combineShapesが受け付ける図形ではありません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `operation` | string | はい | 次のいずれか：`union`、`intersection`、`difference`、`symmetricDifference`。 |
| `firstUuid` | string | はい | 最初の図形のUUID。新しい図形はそのクラス、属性、コンテナを引き継ぎます。 |
| `secondUuid` | string | はい | 2番目の図形のUUID。`firstUuid`とは異なる必要があります。 |
| `deleteOriginals` | string |  | 次のいずれか：`none`、`first`、`both`。デフォルトは`none`。`first`は最初の図形を、`both`は両方を削除します。結果の図形がない場合は何も削除されません。 |
| `class` | string |  | 作成オプション：新しい図形のクラス。存在しない場合は作成されます。指定しない場合、新しい図形は最初の図形のクラスを保持します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しい図形の名前。合成結果が複数の図形になる場合や、別のオブジェクトがその名前を持っている場合は拒否されます。 |
| `select` | boolean |  | 作成オプション：新しい図形を選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：新しい図形の属性をそのクラス（`class`、指定がない場合は最初の図形のクラス）に従わせます。`class`は必要ありません。 |

**結果**

| キー | 説明 |
|---|---|
| `operation` | 実行した操作。 |
| `count` | 新しい図形の数。 |
| `shapes` | 新しい図形（[オブジェクト参照](Common.md#object-references)として）。 |
| `deleted` | 削除された元の図形のUUID。何も削除されなかった場合は空です。 |
| `planesAligned` | 2番目の図形を最初の図形の平面に移動した場合は`true`。それ以外の場合は省略されます。 |
| `note` | 結果がない場合のみ：その理由と、何も作成されず元の図形が（`deleteOriginals`を指定した場合も）保持されたこと。 |

エラー：`operation`の欠落、不明な`operation`または`deleteOriginals`、`the 'firstUuid' object was not found`（または`'secondUuid'`）、`'firstUuid' and 'secondUuid' are the same object: combineShapes combines two different shapes`、上記の一覧を伴う`the '<key>' object is not a shape that combineShapes takes: it takes …`、最初の図形がレイヤ・シンボル定義・それらの中のグループのいずれにもない場合、2番目の図形がそのようなコンテナになく呼び出しによって削除または別の平面へ移動される場合、呼び出しによって削除または別の平面へ移動される図形がロックされている場合（先にeditObjectの`locked` falseでロックを解除してください）、`the shapes are not coplanar: …`、`'name' must be a text`、`the name '<name>' is used by another object, …`、`'name' names one object, but the shapes combine into <count> shapes: …`、`Vectorworks gave no union of the shapes: its modeling failed, or the shapes enclose no area (lines)`、`Vectorworks refused to combine the shapes`、`Vectorworks could not insert the combined shapes into the container of the first shape`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### createText

文字列オブジェクトを作成します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: createText" · **runToolBatch内:** はい

**詳細**

`text`（UTF-8。"\n"と"\r\n"は文字列オブジェクトの行区切りである"\r"に変換。最大16383 UTF-16コード単位）から、文字列の位置揃えの基準点`origin`（ワールド単位）に文字列オブジェクトを作成します。位置揃えで決まる点がその位置に来るように文字列が配置されます。省略可能な`width`（ワールド単位、正の値）を指定すると、その幅で行を折り返す文字列オブジェクト（文字の折り返し）を作成します。

テキスト全体の書式は、明示的に指定した値が文字スタイルの値を上書きするように、次の順序で書き込まれます。`textStyle`（図面の文字スタイルの名前またはリソースUUID。getResourcesでresourceType `textStyle`を指定すると一覧を取得できます。""で指定なし）または`textStyleByClass` true（文字列がそのクラスの文字スタイルに従う）、`font`（フォント名）、`size`（ワールド単位）または`sizePoints`（ポイント）、スタイルフラグ`bold`、`italic`、`underline`、`outline`、`shadow`（outlineとshadowはmacOSでのみ表示）、`color`。

次にレイアウトを書き込みます。`horizontalAlignment`（left|center|right|justify）、`verticalAlignment`（topBox|topBaseline|centerBox|bottomBaseline|bottomBox）、`lineSpacing`（single|oneAndHalf|double、またはワールド単位の行間隔`leading`を伴うcustom）、`angle`（原点を中心とする反時計回りのラジアン）、`flipped`（上下反転）。指定しない項目には、ファイルの文字のデフォルト設定が使用されます。

何かを作成する前に、すべての引数を検証します。型の誤り、不明な名前・フォント・文字スタイル、`size`と`sizePoints`の同時指定、正でない幅・サイズ・行間隔は呼び出しを拒否し、その場合は何も作成されません。作成オプション（class、name、select、useClassAttributes）は書式の前に適用されます。オブジェクト参照と`applied`（指定された書式とレイアウトの各引数に対するtrue/false。originを含み、leadingはlineSpacingに含まれます）を返します。getTextで文字列を読み戻せます。

> **注:** `textStyle`と`textStyleByClass`を同時に指定すると拒否されます。`textStyleByClass`は`true`のみを受け付けます。`textStyle` `""`は文字スタイルを解除します。`lineSpacing` `custom`には`leading`が必要で、`leading`には`lineSpacing` `custom`が必要です。作成オプション（`class`、`name`、`select`）は書式の前に適用されるため、`class`が書式の引数を上書きすることはありません。拒否された呼び出しは何も作成しません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `text` | string | はい | テキスト（UTF-8）。"\n"で改行します。 |
| `origin` | [点](Common.md#points) | はい | 文字列の位置揃えの基準点（ワールド単位）。 |
| `width` | number |  | 折り返し幅（ワールド単位）。文字の折り返しが有効になります。 |
| `textStyle` | string |  | 文字スタイルの名前またはリソースUUID。空の文字列で指定なし。 |
| `textStyleByClass` | boolean |  | クラスの文字スタイルを使用します。 |
| `font` | string |  | フォント名。 |
| `size` | number |  | 文字サイズ（ワールド単位。`sizePoints`との併用不可）。 |
| `sizePoints` | number |  | 文字サイズ（ポイント）。 |
| `color` | [色](Common.md#colors) |  | 文字の色。 |
| `bold` | boolean |  | ボールドスタイル。 |
| `italic` | boolean |  | イタリックスタイル。 |
| `underline` | boolean |  | アンダーラインスタイル。 |
| `outline` | boolean |  | アウトラインスタイル（macOSでのみ表示）。 |
| `shadow` | boolean |  | シャドウスタイル（macOSでのみ表示）。 |
| `horizontalAlignment` | string |  | 次のいずれか：`left`、`center`、`right`、`justify`。 |
| `verticalAlignment` | string |  | 次のいずれか：`topBox`、`topBaseline`、`centerBox`、`bottomBaseline`、`bottomBox`。 |
| `lineSpacing` | string |  | 次のいずれか：`single`、`oneAndHalf`、`double`、`custom`。 |
| `leading` | number |  | カスタムの行間で使用する行間隔（ワールド単位）。 |
| `angle` | number |  | 原点を中心とする回転。反時計回り、ラジアン。 |
| `flipped` | boolean |  | 文字列を上下反転します。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

**結果**

新しい文字列オブジェクトの[オブジェクト参照](Common.md#object-references)と、次の項目を返します。

| キー | 説明 |
|---|---|
| `applied` | 書き込まれた各引数の名前の下に`true`または`false`：`origin`（常に含む）、書式の引数（`textStyle`、`textStyleByClass`、`font`、`size`、`sizePoints`、指定された各スタイルフラグ、`color`）、レイアウトの引数（`horizontalAlignment`、`verticalAlignment`、`leading`を含む`lineSpacing`、`angle`、`flipped`）。`width`は新しい文字列オブジェクトの形状を決めるもので、含まれません。 |

エラー：`'text' must be a text that is not empty`、`'text' is too long: Vectorworks edits text objects of at most 16383 UTF-16 code units`、`'origin' must be a point { x, y } in world units`、`give either 'textStyle' or 'textStyleByClass'`、`'textStyleByClass' takes true, which makes the text follow the text style of its class; 'textStyle' "" removes the text style`、`'textStyle' "<name>" is neither the name nor the UUID of a text style of the drawing (getResources lists them with resourceType 'textStyle'); "" removes the text style`、`'font' "<name>" is no font that Vectorworks knows`、`'textStyle' must be the name or the UUID of a text style, or ""`、`'font' must be the name of a font`、`give either 'size' (world units) or 'sizePoints' (points)`、正でないサイズ・幅・行間隔、`'lineSpacing' custom needs 'leading', the line distance in world units, and 'leading' needs 'lineSpacing' custom`、位置揃え・行間・スタイルフラグ・色・角度・flippedの値の型の誤りまたは不明な名前。拒否された呼び出しは何も作成しません。

### getText

文字列オブジェクトの内容、文字書式、スタイル、レイアウトを読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

uuid、name、またはindexで文字列オブジェクトを読み取ります。文字インデックスは0始まりのUTF-16コード単位です（基本多言語面の外の文字は2単位と数えます）。長さはワールド単位、角度はラジアンです。返される項目は次のとおりです。`text`（全文。行区切りは"\r"）、`length`、`lineCount`、`lines`（折り返し後の各行を{ start, text }で表し、findObjectsと同様に`lineLimit`（デフォルトは100）と`lineOffset`でページ分割：count、returned、offset、limit、truncated、nextOffset、items）。`origin`（位置揃えの基準点）、`angle`、`flipped`（上下反転）、`boxCorners`（文字ボックスの左上、右上、右下、左下。文字列とともに回転）。`horizontalAlignment`、`verticalAlignment`、`lineSpacing`（カスタムの行間の場合は`leading`を伴う）、`width`、`wrapped`。文字0の書式：`font`、`size`（ワールド単位）、`sizePoints`、`style`（フラグ名：bold、italic、underline、outline、shadow）、`customStyle`（ある場合はdiagonalFraction|verticalFraction|superscript|subscript）、`color`、`tracking`（トラッキング：文字間隔。1 = 標準）。テキスト全体の`textStyle`：{ byClass, name, uuid }、文字スタイルのないクラスの場合は{ byClass: true }、文字が異なる文字スタイルに従う場合は{ mixed: true }、指定なしの場合はnull。`styleRuns`：書式の連続範囲を順に{ start, length }で表し、同じ書式キーとその範囲の`textStyle`を持ち、`runLimit`（デフォルトは100）と`runOffset`でページ分割。`tabStops`（{ offset：文字列の左端からのワールド単位の距離, alignment：left|right|center|decimal }。offset順）、`repeatingTabStop`（等間隔のタブストップの間隔。それ以外は0）、`tightFill`（文字部分のみアミ掛け）、`isLinkedToRecord`。

名前とキーは、createTextとeditTextが受け付けるものと同じです。

> **注:** `lines`と`styleRuns`はページ分割されたリストで、それぞれ`count`、`returned`、`offset`、`limit`、`truncated`、`nextOffset`（`truncated`がtrueの場合のみ）、`items`を持つオブジェクトです。`lines`の項目は`{ start, text }`で、`start`はその行の最初の文字の文字インデックスです。2つのリストは別々にページ分割され、`getText`には`countOnly`はありません。1未満の`lineLimit`または`runLimit`、0未満のオフセット、数値でない値は`'lineLimit' must be a number of at least 1 and 'lineOffset' a number of at least 0`（書式範囲の場合は`'runLimit'`と`'runOffset'`）で拒否されます。文字列オブジェクトでないオブジェクトは`the object is not a text object: getText and editText take text objects only`で拒否されます。見つからないオブジェクトは`object not found (provide 'uuid', 'name' or 'index')`で拒否されます。空のテキスト（`length`が0）の場合、文字0の書式キー（`font`、`size`、`sizePoints`、`style`、`customStyle`、`color`、`tracking`）は省略されますが、`textStyle`と`styleRuns`は返されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `lineLimit` | integer |  | ページ内の`lines`の最大数（1以上）。デフォルトは100。 |
| `lineOffset` | integer |  | スキップする行数（負の値は不可）。デフォルトは0。 |
| `runLimit` | integer |  | ページ内の`styleRuns`の最大数（1以上）。デフォルトは100。 |
| `runOffset` | integer |  | スキップする書式範囲の数（負の値は不可）。デフォルトは0。 |

### editText

文字列オブジェクトの内容と書式を編集します。

> **作用:** 編集 · **リスク:** 低 · **取り消し:** 1ステップ "MCP: editText" · **runToolBatch内:** はい

**詳細**

uuid、name、またはindexで文字列オブジェクトを編集します。1回の呼び出しは1つの取り消しステップです。文字のインデックスと文字数は、0始まりのUTF-16コード単位です（基本多言語面の外の文字は2単位と数えます）。長さはワールド単位、角度はラジアンです。新しいテキストの"\n"と"\r\n"は、文字列オブジェクトの行区切りである"\r"に変換されます。何かを変更する前に、すべての引数を検証します。型の誤り、不明な名前・フォント・文字スタイル、テキストの外にある範囲、正でないサイズ・幅・行間隔・間隔・オフセット、空のテキスト、複数の内容変更、変更のない呼び出し、文字列オブジェクトでないオブジェクトは呼び出しを拒否し、その場合は何も変更されません。

変更は次の順序で実行されます。

1. 内容（次のうち最大1つ）：`setText`（テキスト全体を置き換え、テキストは最後の文字の書式を引き継ぎます。旧テキストと新テキストの合計は16383コード単位以内である必要があります）、`insertText` { text, at }（文字`at`の前に挿入。テキストの長さを指定すると末尾に追加。新しいテキストは直前の文字の書式を引き継ぎ、0の場合は最初の文字の書式を引き継ぎます）、`appendText`、`deleteText` { first, count }（countのデフォルトはテキストの残り全体。テキスト全体は削除できません）。

2. 内容の変更後のテキストのうち、`first`（デフォルトは0）と`count`（デフォルトは残り全体）で指定した範囲の文字書式を、次の順序で設定します。`textStyle`（図面の文字スタイルの名前またはリソースUUID。""は範囲を文字スタイルから切り離し、書式は保持）または`textStyleByClass` true（範囲が文字列オブジェクトのクラスの文字スタイルに従う）、`font`、`size`（ワールド単位）または`sizePoints`（ポイント）、スタイルフラグ`bold`、`italic`、`underline`、`outline`、`shadow`（指定したフラグだけが変わり、各文字はその他のフラグと、上付き・下付き・分数のスタイルを保持）、`color`。

3. **レイアウト：** `horizontalAlignment`と`verticalAlignment`（位置揃えを変更しても、Vectorworksと同様に文字列の位置はそのままで、位置揃えの基準点である原点が移動）、`lineSpacing`（customには`leading`が必要）、`width`（折り返し幅。その幅で文字列を折り返す）、`wrapped`（trueは現在の幅で折り返し、falseは行区切りでのみ改行。`width`との併用でfalseは不可）、`origin`（位置揃えの基準点がその位置に来るように文字列を移動）、`angle`、`flipped`。テキスト全体に適用された文字スタイルは位置揃えと行間も設定するため、レイアウトは書式の後に適用されます。

4. **タブストップ：** `repeatingTabStop`（すべてのタブストップを間隔の倍数に再配置し、左揃えにする）、`removeTabStops`（getTextの`tabStops`へのインデックス。タブストップ0は削除不可）、`moveTabStop` { index, offset }（削除後のインデックス。タブストップはoffset順を維持）、`addTabStops`（新しい左揃えタブストップのオフセット）。

5. `unlinkFromRecord` trueは、レコードフィールドにリンクされた文字列オブジェクトのリンクを解除します（それ以外の文字列オブジェクトでは拒否）。

オブジェクト参照、`applied`（指定された各引数に対するtrue/false。leadingはlineSpacingに含まれます）、`length`、`lineCount`を返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `setText` | string |  | テキスト全体を置き換えます。空にはできず、旧テキストと新テキストの合計は16383 UTF-16コード単位以下です。 |
| `insertText` | object |  | 文字の前にテキストを挿入します。`text`と`at`を指定します。 |
| `insertText.text` | string | はい | 挿入するテキスト。空にはできません。"\n"で改行します。旧テキストと合わせて16383 UTF-16コード単位以下です。 |
| `insertText.at` | integer | はい | その前にテキストが入る文字のインデックス：0は先頭、テキストの長さは末尾です。 |
| `appendText` | string |  | 末尾に追加するテキスト。空にはできず、旧テキストと合わせて16383 UTF-16コード単位以下です。 |
| `deleteText` | object |  | 文字の範囲を削除します。テキスト全体は削除できません。 |
| `deleteText.first` | integer |  | 削除する最初の文字のインデックス（テキストの長さ未満）。デフォルトは0。 |
| `deleteText.count` | integer |  | 削除する文字数（1からテキストの残りまで）。デフォルト：テキストの残り全体。 |
| `first` | integer |  | 文字書式を書き込む範囲の最初の文字（内容の変更後のテキストで数えます）。デフォルトは0。書式の引数（`textStyle`、`textStyleByClass`、`font`、`size`、`sizePoints`、スタイルフラグ、`color`）を指定した場合のみ読み取られます。 |
| `count` | integer |  | その範囲の文字数（1からテキストの残りまで）。デフォルト：テキストの残り全体。 |
| `width` | number |  | 折り返し幅（ワールド単位）。文字の折り返しが有効になります。 |
| `wrapped` | boolean |  | trueは現在の幅で折り返し、falseは行区切りでのみ改行します。`width`との併用でfalseは不可。 |
| `repeatingTabStop` | number |  | すべてのタブストップを間隔の倍数に再配置し、左揃えにします。 |
| `removeTabStops` | array of integer |  | getTextの`tabStops`へのインデックス。タブストップ0は削除できません。 |
| `moveTabStop` | object |  | タブストップを1つ移動します。`index`と`offset`を指定します。 |
| `moveTabStop.index` | integer | はい | `removeTabStops`の後に残ったタブストップの中でのインデックス。0が最初です。 |
| `moveTabStop.offset` | number | はい | 文字列の左端からの新しいオフセット（ワールド単位）。正の値。 |
| `addTabStops` | array of number |  | 新しい左揃えタブストップのオフセット。 |
| `unlinkFromRecord` | boolean |  | trueで、レコードフィールドにリンクされた文字列オブジェクト（getTextの`isLinkedToRecord`）のリンクを解除します。リンクされていない文字列オブジェクトでは拒否されます。`false`は何も変更せず、`applied`に項目も追加しません。 |
| `textStyle` | string |  | 文字スタイルの名前またはリソースUUID。空の文字列で指定なし。 |
| `textStyleByClass` | boolean |  | クラスの文字スタイルを使用します。`true`のみを受け付け、`textStyle`との併用は拒否されます。 |
| `font` | string |  | フォント名。 |
| `size` | number |  | 文字サイズ（ワールド単位。`sizePoints`との併用不可）。 |
| `sizePoints` | number |  | 文字サイズ（ポイント）。 |
| `color` | [色](Common.md#colors) |  | 文字の色。 |
| `bold` | boolean |  | ボールドスタイル。 |
| `italic` | boolean |  | イタリックスタイル。 |
| `underline` | boolean |  | アンダーラインスタイル。 |
| `outline` | boolean |  | アウトラインスタイル（macOSでのみ表示）。 |
| `shadow` | boolean |  | シャドウスタイル（macOSでのみ表示）。 |
| `horizontalAlignment` | string |  | 次のいずれか：`left`、`center`、`right`、`justify`。 |
| `verticalAlignment` | string |  | 次のいずれか：`topBox`、`topBaseline`、`centerBox`、`bottomBaseline`、`bottomBox`。 |
| `lineSpacing` | string |  | 次のいずれか：`single`、`oneAndHalf`、`double`、`custom`。 |
| `leading` | number |  | 行間隔（ワールド単位、正の値）。`lineSpacing` `custom`では必須で、それ以外では拒否されます。 |
| `origin` | [点](Common.md#points) |  | 文字列の位置揃えの基準点（ワールド単位）。 |
| `angle` | number |  | 原点を中心とする回転。反時計回り、ラジアン。 |
| `flipped` | boolean |  | 文字列を上下反転します。 |

**結果**

[オブジェクト参照](Common.md#object-references)と、次の項目を返します。

| キー | 説明 |
|---|---|
| `applied` | 指定された各引数の名前の下に`true`または`false`：`setText`、`insertText`、`appendText`または`deleteText`、書式の引数（`textStyle`、`textStyleByClass`、`font`、`size`、`sizePoints`、指定された各スタイルフラグ、`color`）、レイアウトの引数（`horizontalAlignment`、`verticalAlignment`、`leading`を含む`lineSpacing`、`width`、`wrapped`、`origin`、`angle`、`flipped`）、`repeatingTabStop`、`removeTabStops`、`moveTabStop`、`addTabStops`、`unlinkFromRecord`。`removeTabStops`と`addTabStops`はリストが空でない場合のみ、`unlinkFromRecord`は`true`の場合のみ報告されます。 |
| `length` | 呼び出し後のテキストの長さ（UTF-16コード単位）。 |
| `lineCount` | 折り返し後の行数。 |

エラー：`object not found (provide 'uuid', 'name' or 'index')`、`the object is not a text object: getText and editText take text objects only`、`give at most one of 'setText', 'insertText', 'appendText' and 'deleteText' per call`、`'<key>' must be a text that is not empty`、`'<key>' is too long …: Vectorworks edits text objects of at most 16383 UTF-16 code units`、`'insertText' must be { text, at }`と`'insertText' needs 'at', a character index from 0 (the start) to <length> (the end of the text)`、`'deleteText' must be { first, count }`と`'deleteText' is outside the text: …`と`'deleteText' cannot delete the whole text: …`、`the formatting range is outside the text: …`、`'width' wraps the text at that width; it cannot be combined with 'wrapped' false`、`tab stop 0 cannot be removed: …`、`'removeTabStops' must be an array of indices of the <n> tab stops of the text (getText 'tabStops')`、`'moveTabStop' must be { index, offset }: …`、`'addTabStops' must be an array of offsets (world units, positive)`、`'unlinkFromRecord': the text is not linked to a record field`、createTextの書式とレイアウトに関する拒否、`nothing to change: give a content, formatting, layout, tab stop or 'unlinkFromRecord' argument`。拒否された呼び出しは何も変更しません（`rolledBack`）。

## Objects

> **グループ:** `Objects` · **グループID:** `objects` · **初期状態で有効:** はい · **リスクレベル:** 中 · **ツール数:** 12

**あらゆるオブジェクトの検索、調査、編集を行い、属性、変形、コンテナ、プラグインパラメータ、レコードを扱います。**

既存のあらゆるオブジェクトを、安定したuuidで調査、編集します。条件または点の指定による検索、情報（3Dバウンディングボックス、グループ、レイヤ、その他のコンテナのメンバーを含む）とグラフィック属性の読み取り、線／面／不透明度／マーカー／ドロップシャドウの設定、オブジェクト間での属性のコピー、変形、名前の変更、クラスの変更、コンテナ間の移動（グループ内への移動を含む）、グループの解除、多角形／曲線への変換、プラグイン（PIO）パラメータの読み書き（型とポップアップの選択肢を含む）、およびあらゆるオブジェクトに付加されたユーザーデータレコードの読み取りを行います。

インストール済みのあらゆるプラグインオブジェクトの定義をユニバーサル名で読み取り（getPluginDefinition：種類、パラメータ、ポップアップの選択肢）、どのグループにも作成ツールがないプラグインオブジェクトを作成します（createPluginObject。ドア、窓、植栽、データタグなどはそれぞれ専用のツールで作成され、createPluginObjectはそのツール名を示します）。プラグインオブジェクトは`parametricName`で識別してください。型コードだけ、付加されたレコード、またはIFCエンティティから種類を推測してはいけません。

IFCデータ（IFCエンティティ、標準およびカスタムプロパティセット、IFCプロパティ型）は、getObjectRecordsやgetResourceDetailsではなく、IFCグループのツールgetObjectIFCData、getIFCPsetDefinition、listIFCPsetsで読み取ります。検索結果の`count`は一致の総数を示し、リストが途中で打ち切られた場合は`truncated`で示されます。打ち切られたリストはサンプルにすぎないため、それを根拠に総数、存在しないこと、またはすべてのオブジェクトに共通する内容を断定してはいけません。

各編集は、固有の名前を持つ、取り消し可能なVectorworksの操作として実行されます。

| ツール | 作用 | リスク | 概要 |
|---|---|---|---|
| [`findObjects`](#findobjects) | 読み取り専用 | 低 | 条件文字列に一致するオブジェクトを検索します。 |
| [`getObjectsAtPoint`](#getobjectsatpoint) | 読み取り専用 | 低 | 指定した点にあるオブジェクトを検索します。 |
| [`getObjectInfo`](#getobjectinfo) | 読み取り専用 | 低 | オブジェクトの識別情報、クラス、レイヤ、境界、状態、コンテナを返します。 |
| [`getObjectAttributes`](#getobjectattributes) | 読み取り専用 | 低 | オブジェクトのグラフィック属性を返します。 |
| [`setObjectAttributes`](#setobjectattributes) | 編集 | 中 | 線、面、不透明度、マーカー、ドロップシャドウなど、オブジェクトのグラフィック属性を設定します。 |
| [`copyAttributes`](#copyattributes) | 編集 | 中 | あるオブジェクトのグラフィック属性を他のオブジェクトにコピーします。 |
| [`editObject`](#editobject) | 編集 | 中 | オブジェクトの移動、回転、拡大縮小、ミラー反転、複製、グループ構成の変更、変換、リセット、削除、または名前とクラスの変更を行います。 |
| [`getObjectParameters`](#getobjectparameters) | 読み取り専用 | 低 | プラグインオブジェクトのパラメータを読み取ります。 |
| [`getObjectRecords`](#getobjectrecords) | 読み取り専用 | 低 | オブジェクトに付加されたデータレコードを読み取ります。 |
| [`setObjectParameter`](#setobjectparameter) | 編集 | 中 | プラグインオブジェクトの1つ以上のパラメータを書き込みます。 |
| [`getPluginDefinition`](#getplugindefinition) | 読み取り専用 | 低 | インストール済みのプラグインオブジェクトの種類、パラメータ、ポップアップの選択肢を示します。 |
| [`createPluginObject`](#createpluginobject) | 編集 | 中 | 専用の作成ツールがないプラグインオブジェクトを作成します。 |

### findObjects

条件文字列に一致するオブジェクトを検索します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

Vectorworksの条件文字列（例："(T=RECT)"、"(C='My Class')"、"ALL"）に一致するオブジェクトを検索します。`offset`（デフォルトは0）から始めて、最大`limit`件（デフォルトは200）の一致についてuuid/type/typeName/nameを返します。`count`は一致の総数、`returned`は`objects`に列挙された件数で、後続の一致がある場合は`truncated`がtrueになります。`offset`を`nextOffset`に設定して続きを取得するか、`countOnly`を指定して`count`だけを取得してください。

オフセットは図面が変更されていない間だけ有効です。件数や存在を確認するには、"ALL"を列挙するよりも、対象を絞った条件と`countOnly`の併用を優先してください。検索対象は、デザインレイヤとシートレイヤ上、グループ内、およびデザインレイヤビューポート内のオブジェクトです。`notSearched`には、条件に含まれていない検索範囲のキーワードが列挙されます。INSYMBOL（シンボル定義内）、INOBJECT（プラグインオブジェクト内）、INVIEWPORT（ビューポートの注釈とクロップグループ）、INOBJPATHとINOBJPROFILE（プラグインオブジェクトのパスグループと断面グループ）です。そこを検索するには、これらを先頭に付けてください（"INSYMBOL & INOBJECT & (T=RECT)"）。

件数0は、その検索範囲内に一致がないことだけを意味します。パラメトリックなプラグインオブジェクト（type 86）では、オブジェクトが何であるかを示す`parametricName`と`localizedParametricName`も返します（例："Window"、"Door"、"Plant"）。プラグインオブジェクトは、"(PON='Window')"のような条件で`parametricName`を使って検索してください。コンパイルできない条件は問題を示すエラーを返します。有効な条件で一致がない場合はcount 0を返します。

条件内の名前（レコード、フィールド、クラス、プラグイン）は検証されません。綴りの誤った名前や存在しない名前もコンパイルされ、count 0を返します（内部の`NNA_`レコード名はエラーで拒否されます）。"(N='...')"はVectorworksのオブジェクト名だけに、大文字と小文字を区別せずに一致します。ワイルドカードがない場合は完全一致の名前です。'\*'は任意の文字列に、'?'は1文字に一致します（"(N='\*door\*')"）。これらのワイルドカードはエスケープできません。

文字列は単一引用符で囲み、名前に含まれる引用符は2つ重ねてください（"(N='O''Brien')"）。完全一致の名前は、オブジェクトがどこにあっても見つけます。ワイルドカードパターンは、グループ内を含め、デザインレイヤとシートレイヤ上のオブジェクトを検索します。NはIFC名、IFCプロパティセットの値、レコードフィールドの値には一致しません。IFCデータはIFCグループのツールで読み取ってください。

> **注:** `countOnly`を指定した場合、結果にはページ分割のキー`count`、`returned`、`offset`、`limit`、`truncated`が含まれますが、`objects`は含まれません。したがって、結果は「`count`だけ」ではありません。`notSearched`はどの場合にも返されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `criteria` | string | はい | Vectorworksの条件文字列（例：`(T=RECT)`、`(C='My Class')`）。コンパイルできる必要があり、内部のIFCレコードフォーマットを参照してはいけません。 |
| `limit` | integer |  | ページ分割：返す項目の最大数（1以上）。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割：スキップする項目数（デフォルトは0）。 |
| `countOnly` | boolean |  | ページ分割：項目を含めず、件数だけを返します。 |

**結果**

| キー | 説明 |
|---|---|
| `count` | 一致の総数。 |
| `returned` | `objects`内のオブジェクト数（`countOnly`の場合は0）。 |
| `offset` | 使用された`offset`。 |
| `limit` | 使用された`limit`。 |
| `truncated` | このページの後にも一致がある場合は`true`。 |
| `nextOffset` | 次のページの`offset`。`truncated`が`true`の場合のみ。 |
| `objects` | 一致したオブジェクト（[オブジェクト参照](Common.md#object-references)として）。`countOnly`の場合は省略されます。 |
| `notSearched` | 条件に含まれていない検索範囲キーワードのリスト（詳細を参照）。常に含まれ、`countOnly`の場合も含まれます。 |

エラー：`criteria`がない・空・文字列でない場合は`'criteria' is required (a Vectorworks criteria string, e.g. "(T=RECT)" or "(C='My Class')")`、`criteria cannot reference internal IFC record formats; use the IFC tools instead`、`invalid criteria: <the compile error>`、およびページ分割の引数では`'limit' must be at least 1`、`'offset' must not be negative`、`'limit' must be a number`（`offset`も同様）、`'countOnly' must be true or false`。

### getObjectsAtPoint

指定した点にあるオブジェクトを検索します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

ワールド座標の`point`にあるオブジェクトを検索します。必要に応じて`radius`の範囲内を対象にします。`traverse`で検査するオブジェクト（デフォルトはvisibleObjects、allObjects、selectedObjects、editableObjects）を、`descend`で入るコンテナ（デフォルトはnone、groups、viewports、all）を選択します。不明な値はエラーを返し、適用された値は結果にそのまま返されます。`offset`から始めて最大`limit`件（デフォルトは50）のオブジェクト参照を最前面のものから順に返し、findObjectsと同様に`count`、`returned`、`truncated`、`nextOffset`を含みます。`countOnly`は`count`だけを返します。

> **注:** `countOnly`を指定した場合、結果にはページ分割のキー（`count`、0の`returned`、`offset`、`limit`、`truncated`）が含まれますが、`objects`は含まれません。`point`がない場合は拒否されます。有効な点でない`point`は(0, 0)として読み取られるため、原点で検索が行われます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `point` | [点](Common.md#points) | はい | 検査するワールド座標の点。点でない値は(0, 0)として読み取られます。 |
| `radius` | number |  | `point`の周囲のピック半径（ワールド単位）。デフォルトは0。 |
| `traverse` | string |  | 検査するオブジェクト。次のいずれか：`allObjects`、`visibleObjects`、`selectedObjects`、`editableObjects`。デフォルトは`visibleObjects`。 |
| `descend` | string |  | 入るコンテナ。次のいずれか：`none`、`groups`、`viewports`、`all`。デフォルトは`none`。 |
| `limit` | integer |  | ページ分割：返す項目の最大数（1以上）。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割：スキップする項目数（デフォルトは0）。 |
| `countOnly` | boolean |  | ページ分割：項目を含めず、件数だけを返します。 |

**結果**

| キー | 説明 |
|---|---|
| `count`、`returned`、`offset`、`limit`、`truncated`、`nextOffset`、`objects` | 見つかったオブジェクトのページ。[`findObjects`](#findobjects)と同じです（`notSearched`はありません）。 |
| `traverse` | 使用された`traverse`。 |
| `descend` | 使用された`descend`。 |

エラー：`'point' is required`、`unknown 'traverse'; use allObjects | visibleObjects | selectedObjects | editableObjects`（文字列でない`traverse`の場合も）、`unknown 'descend'; use none | groups | viewports | all`、および[`findObjects`](#findobjects)に記載されたページ分割のエラー。

### getObjectInfo

オブジェクトの識別情報、クラス、レイヤ、境界、状態、コンテナを返します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

1つのオブジェクトについて、識別情報、クラス、レイヤ、境界、面積、周長、表示／ロック／選択の状態、内部の`index`を返します。また、オブジェクト参照として、`parent`コンテナ（レイヤ、グループ、シンボル定義など）と、親の前後関係で隣接する`next` / `previous`のオブジェクトを返します（`next`は前面に描画されます）。プラグインオブジェクトでは`parametricName`と`localizedParametricName`も返します。

`bounds3D` { min: {x,y,z}, max: {x,y,z} }、`center3D` {x,y,z}、`size3D` {x,y,z}（X、Y、Z方向の範囲。zは高さ）は、ワールドZを使ったワールド単位の3Dバウンディングボックスを示します（デザインレイヤの高さを含みます。シンボル定義内では、その定義の座標です）。ボックスがz = 0で平らな場合は省略されます。これは、レイヤプレーンまたはスクリーンプレーン上の2Dオブジェクトのように高さを持たない場合（`bounds`を使用してください）や、そのようなオブジェクトだけからなるグループやレイヤの場合です。

`memberCount`は、メンバーを持つオブジェクトの直接のメンバー数です。対象はレイヤ、グループ、シンボル定義（0の場合も含む）、およびメンバーを持つその他のオブジェクトです。たとえば、壁に挿入されたオブジェクト、押し出しの断面、プラグインオブジェクトや屋根の形状です（生成された形状：オブジェクトがリセットされるとVectorworksが形状を再構築するため、その形状に対する変更は保持されません）。

`includeMembers`がtrueの場合、`members`にメンバーを前後関係の順（背面から前面）のオブジェクト参照として列挙し、findObjectsと同様にページ分割します。`memberOffset`（デフォルトは0）から最大`memberLimit`件（デフォルトは50）を返し、`count`、`returned`、`truncated`、`nextOffset`、`objects`を含みます。`name`はVectorworksの正確なオブジェクト名です。見つからなくても、レコードフィールド、IFCデータ、プラグインパラメータにその値を持つオブジェクトがないとは限りません。それらはfindObjectsの条件で検索してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `includeMembers` | boolean |  | コンテナの直接のメンバーのページである`members`を追加します。`true`または`false`である必要があります。デフォルト：`false`。 |
| `memberLimit` | integer |  | `includeMembers`指定時：ページ内のメンバーの最大数（1以上）。デフォルトは50。 |
| `memberOffset` | integer |  | `includeMembers`指定時：スキップするメンバーの数（0以上）。デフォルトは0。 |

**結果**

オブジェクト参照以外のキーは、Vectorworksが値を返さない場合は省略されます。

| キー | 説明 |
|---|---|
| `uuid`、`type`、`typeName`、`name` | [オブジェクト参照](Common.md#object-references)。プラグインオブジェクトには`parametricName`と`localizedParametricName`もあります。 |
| `bounds` | 2Dの境界[矩形](Common.md#rectangles)（ワールド単位）。 |
| `bounds3D`、`center3D`、`size3D` | 3Dバウンディングボックス、その中心とサイズ（詳細を参照）。ボックスがz = 0で平らな場合は省略されます。 |
| `area`、`perimeter` | 面積と周長（それらを持つオブジェクトの場合）。 |
| `visible`、`locked`、`selected` | オブジェクトの状態。 |
| `class`、`layer` | オブジェクトのクラス名とレイヤ名。 |
| `index` | オブジェクトの内部インデックス。 |
| `memberCount` | 直接のメンバー数（メンバーを持つオブジェクトの場合）。 |
| `members` | `memberCount`を返すオブジェクト（レイヤ、グループ、シンボル定義、または1つ以上のメンバーを持つオブジェクト）で`includeMembers`を指定した場合：メンバーのページ`{ count, returned, offset, limit, truncated, nextOffset, objects }`。`objects`は前後関係の順のオブジェクト参照です。 |
| `parent`、`next`、`previous` | コンテナと、その前後関係で隣接するオブジェクト（オブジェクト参照として）。それぞれ該当するものがない場合は省略され、図面ヘッダーが`parent`として返されることはありません。 |

エラー：`object not found (provide 'uuid', 'name' or 'index')`、`'includeMembers' must be true or false`、`'memberLimit' must be a number of at least 1 and 'memberOffset' a number of at least 0`（どちらかの型または範囲が正しくない場合）。

### getObjectAttributes

オブジェクトのグラフィック属性を返します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

オブジェクトのグラフィック属性を返します。線（RGBのforeColor/backColorとファイルのカラーテーブル内のforeColorIndex/backColorIndex、ミル/mm単位の線の太さ、生のスタイル、ラインタイプ、スタイルの種類、不透明度、クラスに従うかどうかのフラグ、ラインタイプのマッピング）、面（色とカラーインデックス、種類、スタイル、面のリソース、不透明度、クラスに従うかどうかのフラグ）、ハッチング／タイル／グラデーション／イメージの面のマッピング（原点、軸の端点、オフセット、軸の長さ、角度、繰り返し／水平反転／垂直反転など）、beginningVisible/endVisibleを伴う始点と終点のマーカー、ドロップシャドウ、opacityByClassを伴うオブジェクトの不透明度、および継承元のクラスです。

キーは、読み取り専用の線のstyleKindと面のtypeを除き、setObjectAttributesが受け付けるものと同じです。

> **注:** Vectorworksが値を返さないキーは省略されます。`pen.styleKind`と`fill.type`は整数です。`styleKind`：0 なし、1 カラー、2 模様、3 単一のラインタイプ、4 複合のラインタイプ、5 不明。`type`：-1 不明、1 なし、2 カラー、3 模様、4 ハッチング、5 タイル、6 グラデーション、7 イメージ、8 クラス。`pen.lineTypeMapping`と`fillMapping`は、オブジェクトにそのようなマッピングがある場合のみ返されます。`markers`は常に返されます。[マーカー](Attributes.md#line-end-markers)を参照してください。`dropShadow`は、オブジェクトが独自のドロップシャドウデータを持つ場合はすべてのメンバーを持ち、それ以外の場合は`enabled`だけを持ちます。どちらの場合も`byClass`が追加されます。[ドロップシャドウ](Attributes.md#drop-shadow)を参照してください。最上位には`opacity`、`opacityByClass`、`class`（クラスの名前）があります。
>
> キーは[`setObjectAttributes`](#setobjectattributes)のキーと同じですが、3つの違いがあります。`colorsByClass`には別名`byClass`がなく、`allByClass`はなく、`dropShadow`には`delete`がありません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |

エラー：`object not found`。

### setObjectAttributes

線、面、不透明度、マーカー、ドロップシャドウなど、オブジェクトのグラフィック属性を設定します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: setObjectAttributes" · **runToolBatch内:** はい

**詳細**

オブジェクトのグラフィック属性を設定します。指定したメンバーだけが変更されます。`pen`と`fill`は、foreColor/backColor（RGB）またはforeColorIndex/backColorIndex（ファイルのカラーテーブルのインデックス）、opacity 0-100、none/solid、クラスの値を使用するためのcolorsByClass（別名byClass）とstyleByClassのtrue、およびopacityByClassのtrue/falseを受け付けます。線では、`lineWeightMm`または`lineWeightMils`、`lineType`（ラインタイプの内部インデックス）、`style`（線の生のスタイル）、lineWeightByClass、`lineTypeMapping` { localMapping, flipHorizontal, flipVertical, scale }も指定できます。面では、`resource`（ハッチング／タイル／グラデーション／イメージの内部インデックス）と`style`（面の生のスタイル）も指定できます。

`fillMapping`は、ハッチング／タイル／グラデーション／イメージの面を配置します。origin、iAxisEnd、jAxisEnd（ワールド座標の点）、xOffset、yOffset、iAxisLength、jAxisLength（ワールド単位）、angle（ラジアン）、repeat、mirror、flip、maintainAspectRatio、geometryType、localMappingを使用します。`markers`は、線の始点／終点のマーカー、その表示（beginningVisible/endVisible）、またはbyClassを設定します。

`dropShadow`は真偽値またはオブジェクトです。最上位の`opacity`、`opacityByClass`、`allByClass`、`class`も使用できます。

> **注:** 指定したメンバーだけが書き込まれ、ほとんどの型はチェックされません。JSONの型が正しくない数値または真偽値は0または`false`として読み取られ、[色](Common.md#colors)でない`foreColor`または`backColor`は黒として書き込まれます。JSONの型が正しくない`pen`、`pen.lineTypeMapping`、`fill`、`fillMapping`、`markers`、`class`（または真偽値でもオブジェクトでもない`dropShadow`）は無視されます。表に示した型で送信してください。
>
> **注:** 次のフラグは`true`の場合のみ機能し、`false`は何もしません：`pen`の`none`・`solid`・`byClass`・`colorsByClass`・`styleByClass`・`lineWeightByClass`、`fill`の`none`・`solid`・`byClass`・`colorsByClass`・`styleByClass`、`markers.byClass`、最上位の`opacityByClass`と`allByClass`。次のフラグは`true`と`false`を受け付けます：`pen.opacityByClass`、`fill.opacityByClass`、`markers.beginningVisible`、`markers.endVisible`、`dropShadow`オブジェクトの`byClass`。その他の真偽値は指定どおりに書き込まれます。
>
> **注:** 指定された`foreColorIndex`または`backColorIndex`はRGB値の後に適用され、常に優先されます（[色](Common.md#colors)を参照）。`foreColorIndex`と`backColorIndex`は0～65535の整数を受け付けます（それを表す数値の文字列も受け付けます）。それ以外の値は書き込まれず、`applied`の該当項目が`false`になります。`class`は既存のクラスの名前である必要があります。クラスは作成されず、不明な名前では`applied.class`が`false`になります。JSONの数値でない最上位の`opacity`は無視されます。有効な点でない`fillMapping`の点は、`applied`に項目を追加せずにスキップされます。`delete`のない`dropShadow`オブジェクトは、`byClass`だけを含む場合でも、常にドロップシャドウデータ（既存のデータまたはデフォルトに、指定したメンバーを適用したもの）を書き込みます。[ドロップシャドウ](Attributes.md#drop-shadow)を参照してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `pen` | object |  | 線の属性。指定したメンバーだけが変更されます。 |
| `pen.foreColor` | [色](Common.md#colors) |  | 前景色（RGB）。 |
| `pen.backColor` | [色](Common.md#colors) |  | 背景色（RGB）。 |
| `pen.foreColorIndex` | integer |  | ファイルのカラーテーブルのインデックスで指定する前景色。 |
| `pen.backColorIndex` | integer |  | ファイルのカラーテーブルのインデックスで指定する背景色。 |
| `pen.lineWeightMm` | number |  | 線の太さ（ミリメートル）。 |
| `pen.lineWeightMils` | integer |  | 線の太さ（ミル）。 |
| `pen.lineType` | integer |  | ラインタイプの内部インデックス。 |
| `pen.style` | integer |  | 線の生のスタイル。 |
| `pen.opacity` | integer |  | 不透明度（0-100）。 |
| `pen.none` | boolean |  | `true`で線をなし（線を描かない）に設定します。`false`は何もしません。 |
| `pen.solid` | boolean |  | `true`で線をカラーに設定します。`false`は何もしません。 |
| `pen.byClass` | boolean |  | `pen.colorsByClass`と同じです。 |
| `pen.colorsByClass` | boolean |  | `true`で線の色をクラスから取得します。`false`は何もしません。 |
| `pen.styleByClass` | boolean |  | `true`で線のスタイルをクラスから取得します。`false`は何もしません。 |
| `pen.lineWeightByClass` | boolean |  | `true`で線の太さをクラスから取得します。`false`は何もしません。 |
| `pen.opacityByClass` | boolean |  | `true`で線の不透明度をクラスから取得し、`false`でクラスからの取得をやめます。 |
| `pen.lineTypeMapping` | object |  | 線上でのラインタイプのマッピング方法。指定したメンバーだけが変更されます。 |
| `pen.lineTypeMapping.localMapping` | boolean |  | ラインタイプのマッピングのローカルマッピングフラグ。 |
| `pen.lineTypeMapping.flipHorizontal` | boolean |  | ラインタイプを水平反転します。 |
| `pen.lineTypeMapping.flipVertical` | boolean |  | ラインタイプを垂直反転します。 |
| `pen.lineTypeMapping.scale` | number |  | ラインタイプのマッピングの尺度。 |
| `fill` | object |  | 面の属性。指定したメンバーだけが変更されます。 |
| `fill.foreColor` | [色](Common.md#colors) |  | 前景色（RGB）。 |
| `fill.backColor` | [色](Common.md#colors) |  | 背景色（RGB）。 |
| `fill.foreColorIndex` | integer |  | ファイルのカラーテーブルのインデックスで指定する前景色。 |
| `fill.backColorIndex` | integer |  | ファイルのカラーテーブルのインデックスで指定する背景色。 |
| `fill.opacity` | integer |  | 不透明度（0-100）。 |
| `fill.style` | integer |  | 面の生のスタイル。 |
| `fill.resource` | integer |  | ハッチング、タイル、グラデーション、イメージの内部インデックス。 |
| `fill.none` | boolean |  | `true`で面をなしに設定します。`false`は何もしません。 |
| `fill.solid` | boolean |  | `true`で面をカラーに設定します。`false`は何もしません。 |
| `fill.byClass` | boolean |  | `fill.colorsByClass`と同じです。 |
| `fill.colorsByClass` | boolean |  | `true`で面の色をクラスから取得します。`false`は何もしません。 |
| `fill.styleByClass` | boolean |  | `true`で面のスタイルをクラスから取得します。`false`は何もしません。 |
| `fill.opacityByClass` | boolean |  | `true`で面の不透明度をクラスから取得し、`false`でクラスからの取得をやめます。 |
| `fillMapping` | object |  | ハッチング、タイル、グラデーション、イメージの面の配置方法。指定したメンバーだけが変更されます。 |
| `fillMapping.origin` | [点](Common.md#points) |  | マッピングの原点（ワールド座標の点）。 |
| `fillMapping.iAxisEnd` | [点](Common.md#points) |  | I軸の終点（ワールド座標の点）。 |
| `fillMapping.jAxisEnd` | [点](Common.md#points) |  | J軸の終点（ワールド座標の点）。 |
| `fillMapping.xOffset` | number |  | X方向のオフセット（ワールド単位）。 |
| `fillMapping.yOffset` | number |  | Y方向のオフセット（ワールド単位）。 |
| `fillMapping.iAxisLength` | number |  | I軸の長さ（ワールド単位）。 |
| `fillMapping.jAxisLength` | number |  | J軸の長さ（ワールド単位）。 |
| `fillMapping.angle` | number |  | 角度（ラジアン）。 |
| `fillMapping.repeat` | boolean |  | 面を繰り返すかどうか。 |
| `fillMapping.mirror` | boolean |  | 面を水平反転（鏡像反転）するかどうか。 |
| `fillMapping.flip` | boolean |  | 面を垂直反転するかどうか。 |
| `fillMapping.maintainAspectRatio` | boolean |  | 面の縦横比を固定するかどうか。 |
| `fillMapping.geometryType` | integer |  | グラデーションの形状種別（直線状、放射状など）を表す整数。 |
| `fillMapping.localMapping` | boolean |  | `true`で面をオブジェクトを基準に（ローカルマッピング）、`false`でワールドを基準にマッピングします。 |
| `markers` | object |  | マーカー。指定したメンバーだけが変更されます。[マーカー](Attributes.md#line-end-markers)を参照してください。 |
| `markers.beginning` | [マーカー](Attributes.md#line-end-markers) |  | 線の始点のマーカー。書き込むと、オブジェクトの`byClass`がオフになります。 |
| `markers.end` | [マーカー](Attributes.md#line-end-markers) |  | 線の終点のマーカー。書き込むと、オブジェクトの`byClass`がオフになります。 |
| `markers.beginningVisible` | boolean |  | 始点のマーカーを表示（`true`）または非表示（`false`）にします。 |
| `markers.endVisible` | boolean |  | 終点のマーカーを表示（`true`）または非表示（`false`）にします。 |
| `markers.byClass` | boolean |  | `true`でクラスのマーカーを使用します。`false`は何もしません。 |
| `opacity` | integer |  | 不透明度（0-100）。 |
| `opacityByClass` | boolean |  | `true`でオブジェクトの不透明度をクラスから取得します。`false`は何もしません。 |
| `dropShadow` | [ドロップシャドウ](Attributes.md#drop-shadow) |  | 真偽値（ドロップシャドウのオン／オフ）、またはドロップシャドウのメンバー、`byClass`、`delete`を持つオブジェクト。 |
| `allByClass` | boolean |  | `true`で、対応するすべての属性を「クラスに従う」に設定します（線と面の色とスタイル、線の太さ、不透明度、マーカー、ドロップシャドウ）。`false`は何もしません。 |
| `class` | string |  | クラスの名前。 |

**結果**

`{ applied }`。書き込まれたメンバーごとに1項目があります。Vectorworksが値を受け付けた場合は`true`、拒否した場合は`false`です。オブジェクト自体は返されません。キーは必ずしも引数の名前と同じではありません。

| 引数 | `applied`内のキー |
|---|---|
| `pen.foreColor`、`pen.backColor` | `penForeColor`、`penBackColor` |
| `pen.foreColorIndex`、`pen.backColorIndex` | `penForeColorIndex`、`penBackColorIndex` |
| `pen.lineWeightMm`、`pen.lineWeightMils` | `lineWeightMm`、`lineWeightMils` |
| `pen.opacity` | `penOpacity` |
| `pen.style`、`pen.lineType` | `penStyle`、`penLineType` |
| `pen.none`、`pen.solid` | `penNone`、`penSolid` |
| `pen.byClass`または`pen.colorsByClass` | `penByClass` |
| `pen.styleByClass`、`pen.lineWeightByClass`、`pen.opacityByClass` | `penStyleByClass`、`lineWeightByClass`、`penOpacityByClass` |
| `pen.lineTypeMapping.localMapping`、`flipHorizontal`、`flipVertical`、`scale` | `penLocalMapping`、`penFlipHorizontal`、`penFlipVertical`、`penScale` |
| `fill.foreColor`、`fill.backColor` | `fillForeColor`、`fillBackColor` |
| `fill.foreColorIndex`、`fill.backColorIndex` | `fillForeColorIndex`、`fillBackColorIndex` |
| `fill.opacity`、`fill.style`、`fill.resource` | `fillOpacity`、`fillStyle`、`fillResource` |
| `fill.none`、`fill.solid` | `fillNone`、`fillSolid` |
| `fill.byClass`または`fill.colorsByClass` | `fillByClass` |
| `fill.styleByClass`、`fill.opacityByClass` | `fillStyleByClass`、`fillOpacityByClass` |
| `fillMapping.origin`、`iAxisEnd`、`jAxisEnd` | `mapOrigin`、`mapIAxisEnd`、`mapJAxisEnd` |
| `fillMapping.xOffset`、`yOffset`、`iAxisLength`、`jAxisLength`、`angle` | `mapXOffset`、`mapYOffset`、`mapIAxisLength`、`mapJAxisLength`、`mapAngle` |
| `fillMapping.repeat`、`mirror`、`flip`、`maintainAspectRatio`、`geometryType`、`localMapping` | `mapRepeat`、`mapMirror`、`mapFlip`、`mapAspect`、`mapGeometryType`、`mapLocalMapping` |
| `markers.beginning`、`markers.end` | `beginningMarker`、`endMarker` |
| `markers.beginningVisible`、`markers.endVisible` | `beginningMarkerVisible`、`endMarkerVisible` |
| `markers.byClass` | `markersByClass` |
| `opacity`、`opacityByClass` | `opacity`、`opacityByClass` |
| `dropShadow`（真偽値、またはメンバーを持つオブジェクト） | `dropShadow` |
| `dropShadow.byClass`、`dropShadow.delete` | `dropShadowByClass`、`dropShadowDeleted` |
| `class`、`allByClass` | `class`、`allByClass` |

`true`の場合のみ機能するフラグは、`true`が指定された場合のみ項目を持ちます。

エラー：`object not found`。これが唯一のエラーテキストです。Vectorworksが拒否した値は`applied`で`false`になり、呼び出しは成功し、その他の変更は保持されます。

### copyAttributes

あるオブジェクトのグラフィック属性を他のオブジェクトにコピーします。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: copyAttributes" · **runToolBatch内:** はい

**詳細**

コピー元オブジェクトのすべてのグラフィック属性（線、面、マーカー、ドロップシャドウ、不透明度）を、1つの`targetUuid`または複数の`targetUuids`にコピーします。`includeClass`を設定すると、コピー先もコピー元のクラスに入れます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `targetUuid` | string |  | 属性のコピー先オブジェクトのUUID。 |
| `targetUuids` | array of string |  | 属性のコピー先となる複数のオブジェクトのUUID。両方を指定した場合は`targetUuid`に追加されます。 |
| `includeClass` | boolean |  | `true`の場合、各コピー先をコピー元オブジェクトのクラスにも入れます。 |

**結果**

`{ results }`。コピー先ごとに、指定された順に1項目があります（`targetUuid`が最初）。

| キー | 説明 |
|---|---|
| `uuid` | コピー先のUUID（指定されたとおり）。 |
| `applied` | 属性がコピーされた場合は`true`、Vectorworksが拒否した場合は`false`。ここではオブジェクトではなく1つの真偽値です。 |
| `class` | `includeClass`指定時のみ：クラスが設定された場合は`true`。 |
| `err` | そのUUIDのオブジェクトがない場合は`object not found`。この場合、項目に`applied`はありません。 |

`targetUuids`のうち文字列でない項目はスキップされるため、空のリストでは空の`results`になります。

エラー：`source object not found (provide 'uuid', 'name' or 'index')`と`provide 'targetUuid' or 'targetUuids'`（どちらのキーも指定されていない場合）。見つからないコピー先はその項目でのみ報告されます。呼び出しは成功し、他のコピー先の変更は保持され、何もロールバックされません。

### editObject

オブジェクトの移動、回転、拡大縮小、ミラー反転、複製、グループ構成の変更、変換、リセット、削除、または名前とクラスの変更を行います。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: editObject" · **runToolBatch内:** はい

**詳細**

1つのオブジェクトを変形または更新します。`action`：move（`offset`）、rotate（ラジアンの`angle`、`center`）、scale（`scaleX`、`scaleY`、`center`）、mirror（`axisStart`、`axisEnd`）、duplicate（`offset`）、moveToContainer（グループまたはシンボル定義`containerUuid`の中へ、またはレイヤ`layer`上へ移動）、addToGroup（グループ`groupUuid`の中へ移動）、ungroup（グループを解除）、convertToPolygon / convertToPolyline（省略可能な`keepOriginal`、`resolution`。新しいオブジェクトを返す）、reset（プラグインオブジェクトを再生成）、delete。

アクションを指定しない場合は、`name`、`class`、`visible`、`locked`、`selected`のうち指定されたものだけを適用します。moveToContainerは、レイヤ、グループ、シンボル定義の間でのみオブジェクトを移動します。移動先はレイヤ、シンボル定義、またはそれらの中のグループである必要があり、オブジェクトが現在属するコンテナも同様です。オブジェクトとしてのレイヤ、オブジェクト自身の内部にある移動先、および壁、プラグインオブジェクト、屋根の中にあるオブジェクトやそれらの中への移動は拒否されます。ドアや窓を壁の中へ移動したり、挿入されている壁から外へ移動したりすると壁が破損するため、対応していません（ドアや窓の壁への挿入はVectorworksで行ってください）。

シンボル定義、またはその中のグループへの移動では、そのシンボルのインスタンスであるオブジェクトや、深さを問わずそれを含むオブジェクト、または深さを問わずそのインスタンスを含むシンボルのインスタンスであるオブジェクトや、それを含むオブジェクトを拒否します。シンボルが自身の中に入れ子になると無限ループが生じるためです。新しい`name`（オブジェクトを識別する自身の名前は可）、`class`、`visible`、`locked`、`selected`とは併用できません（別の呼び出しで変更してください）。拒否または失敗した移動は何も変更しません。

オブジェクトが出るグループと入るグループ、およびそれらを囲むグループの境界を更新します。移動を編集 &gt; 取り消しで元に戻すと、オブジェクトは元の場所に戻り、それらのグループの境界も元どおりになります。addToGroupはグループ`groupUuid`へのmoveToContainerで、チェック、拒否条件、取り消しも同じです。グループでない`groupUuid`（レイヤ、シンボル定義など）は拒否されます。それらにはmoveToContainerを使用してください。ungroupは、Vectorworksのグループ解除を1つのグループに対して行います。メンバーを、グループのコンテナ内でグループがあった前後関係の位置に元の順序で移動し、グループを削除して、元のメンバーを前後関係の順のオブジェクト参照（`members`）としてそのコンテナ（`parent`）とともに返します。

メンバーは選択された状態になります（他の選択されたオブジェクトも選択されたままです）。グループ自体に付加されたレコードがメンバーに引き継がれる保証はありません。グループでないオブジェクト、ロックされたグループ（先にロックを解除してください）、壁・プラグインオブジェクト・屋根の中のグループ、編集中のグループ（またはそれを含むグループ）、および新しいname、class、visible、locked、selectedの指定は拒否されます。現在の詳細レベルで非表示のメンバー（シンボル定義内で起こりえます）は、グループ解除と同様にグループとともに削除され、`deletedMemberCount`に数えられます。

グループ解除を編集 &gt; 取り消しで元に戻すと、グループがそのメンバーとともに復元されます。

> **注:** `name`には2つの用途があります。`uuid`が指定されていない場合はオブジェクトを検索し（順序は`uuid`、`name`、`index`。[オブジェクト参照](Common.md#object-references)を参照）、同時にオブジェクトの新しい名前にもなります。そのため、`name`で見つかったオブジェクトは、すでに持っている名前に「名前変更」されます。オブジェクトの名前を変更するには、`uuid`で検索し、新しい`name`を指定してください。代わりに`index`を使うと、`name`が`index`より先に試されるため、すでに新しい名前を持つオブジェクトが先に見つかります。
>
> **注:** メンバーがない場合のデフォルト：`offset`は(0, 0)、`center`はワールド原点(0, 0)、`angle`は0、`scaleX`と`scaleY`は1です。`mirror`では、`axisStart`と`axisEnd`は異なる2点である必要があります。点はワールド単位です。`duplicate`は、`offset`が指定された場合のみコピーを移動します。
>
> **注:** 一覧にない`action`は何もせず、報告もされません。呼び出しは成功し、指定されたメンバー`name`、`class`、`visible`、`locked`、`selected`だけが適用されます。`duplicate`、`convertToPolygon`、`convertToPolyline`では、これら5つのメンバーは無視されます。`convertToPolyline`は`resolution`を無視します。
>
> **注:** `class`は既存のクラスの名前である必要があります。クラスは作成されず、不明な名前では`applied.class`が`false`になります。`useClassAttributes`を`true`にすると、[`setObjectAttributes`](#setobjectattributes)の`allByClass`と同様に、オブジェクトはクラスの属性も引き継ぎます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `action` | string |  | 次のいずれか：`move`、`rotate`、`scale`、`mirror`、`duplicate`、`moveToContainer`、`addToGroup`、`ungroup`、`convertToPolygon`、`convertToPolyline`、`reset`、`delete`。 |
| `offset` | [点](Common.md#points) |  | `move`と`duplicate`の移動量（ワールド単位）。デフォルトは(0, 0)。 |
| `angle` | number |  | 反時計回りの角度。ラジアン。 |
| `center` | [点](Common.md#points) |  | `rotate`と`scale`の回転または拡大縮小の中心点。デフォルト：ワールド原点(0, 0)。 |
| `scaleX` | number |  | `scale`のX方向の倍率。デフォルトは1。 |
| `scaleY` | number |  | `scale`のY方向の倍率。デフォルトは1。 |
| `axisStart` | [点](Common.md#points) |  | `mirror`のミラー反転の軸の最初の点。 |
| `axisEnd` | [点](Common.md#points) |  | `mirror`のミラー反転の軸の2番目の点。`axisStart`と異なる必要があります。 |
| `containerUuid` | string |  | `moveToContainer`で、オブジェクトの移動先のグループまたはシンボル定義のUUID。`layer`より優先されます。 |
| `layer` | string |  | `moveToContainer`で、オブジェクトの移動先のレイヤの名前。 |
| `groupUuid` | string |  | `addToGroup`で、オブジェクトを追加するグループのUUID。 |
| `keepOriginal` | boolean |  | `convertToPolygon`と`convertToPolyline`用：`true`で元のオブジェクトを保持します。デフォルトは`false`。 |
| `resolution` | integer |  | `convertToPolygon`用：変換の解像度を表す整数（指定しない場合は0）。`convertToPolyline`では使用されません。 |
| `class` | string |  | オブジェクトを入れる既存のクラスの名前。上記の注を参照してください。 |
| `useClassAttributes` | boolean |  | `class`と併用：`true`でオブジェクトの属性もクラスに従うように設定します。 |
| `visible` | boolean |  | オブジェクトを表示（`true`）または非表示（`false`）にします。 |
| `locked` | boolean |  | オブジェクトをロック（`true`）またはロック解除（`false`）します。 |
| `selected` | boolean |  | オブジェクトを選択（`true`）または選択解除（`false`）します。 |

**結果**

結果はアクションによって異なります。

| アクション | 結果 |
|---|---|
| `delete` | `{ deleted }`：オブジェクトが削除された場合は`true`。 |
| `duplicate`、`convertToPolygon`、`convertToPolyline` | 新しいオブジェクトの[オブジェクト参照](Common.md#object-references)。 |
| `moveToContainer`、`addToGroup` | 移動したオブジェクトのオブジェクト参照。`applied`は`{ "moveToContainer": true }`または`{ "addToGroup": true }`です。 |
| `ungroup` | `{ ungrouped, parent, members, deletedMemberCount }`：`ungrouped`は`true`、`parent`は現在メンバーを保持しているコンテナ、`members`は元のメンバーの前後関係の順のオブジェクト参照です。`deletedMemberCount`は、非表示のメンバーがグループとともに削除された場合のみ返されます。 |
| `move`、`rotate`、`scale`、`mirror`、`reset`、アクションなし、または不明なアクション | `applied`を伴うオブジェクトのオブジェクト参照。アクション（`move`、`rotate`、`scale`、`mirror`、`reset`）の項目と、指定された`name`、`visible`、`locked`、`selected`、`class`ごとの項目があります。Vectorworksが値を受け付けた場合は`true`、拒否した場合は`false`です。 |

エラー：`object not found`、`failed to duplicate`、`failed to convert to a polygon`、`failed to convert to a polyline`、`container not found (provide 'containerUuid' or 'layer')`、`group not found (provide 'groupUuid')`、`Vectorworks could not move the object into the container`、およびグループでない`groupUuid`に対する`addToGroup adds objects to a group only, and 'groupUuid' is no group: move objects into a layer or a symbol definition with editObject 'moveToContainer' ('containerUuid' or 'layer')`。拒否された`moveToContainer`、`addToGroup`、`ungroup`は、理由を示す`err`を返します。`err`は呼び出しをロールバックするため（`rolledBack`）、何も変更されません。

### getObjectParameters

プラグインオブジェクトのパラメータを読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

パラメトリックなプラグインオブジェクト（PIO）のパラメータレコードのみを読み取ります。たとえばドア、窓、植栽、舗床、データタグです。まずfindObjects/getObjectInfoが`parametricName`を返すことを確認してください。パラメトリック名、パラメータ名のリスト、およびその値を文字列として返します。必要に応じて特定の`names`に限定できます。省略可能な`includeDefinitions`（デフォルトはfalse）を指定すると`definitions`が追加されます。読み取った各パラメータについて、名前ごとに`type`（integer、boolean、real、text、dimension、popUp、angle、coordLocXなど）、`localizedName`、およびpopUpの場合は受け付けるユニバーサルな`choices`を返します。`parameters`と`values`は変わりません。

省略可能な`curated`（デフォルトはfalse）を指定すると、ドアと窓の開口パラメータについて{ param, label, value, display }の`curated`配列が追加されます。labelはローカライズされたパラメータ名、displayは開口のポップアップのローカライズされた選択肢です（それ以外の場合、または取得できない場合はnull）。`values`の出力は変わりません。その他のプラグインオブジェクトは空の`curated`配列を返します。

それ以外のすべてのオブジェクト（直線、四角形、円弧、多角形、グループ、シンボル、壁など）ではエラーを返し、ユーザーデータレコード（オブジェクトに付加されたレコードフォーマット）は読み取りません。それらにはgetObjectRecordsを使用してください。

> **注:** `names`を指定した場合、結果に`parameters`のリストはなく、オブジェクトにない名前はエラーにならずに`values`と`definitions`から省かれます。`names`のうち文字列でない項目はスキップされます。`curated`は`names`を無視します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `names` | array of string |  | 読み取るパラメータの名前。デフォルト：すべてのパラメータ。上記の注を参照してください。 |
| `includeDefinitions` | boolean |  | デフォルト：`false`。結果に`definitions`を追加します。 |
| `curated` | boolean |  | デフォルト：`false`。結果に`curated`を追加します。 |

**結果**

| キー | 説明 |
|---|---|
| `parametricName` | プラグインオブジェクトのユニバーサル名。 |
| `parameters` | すべてのパラメータの名前（宣言順）。`names`を指定した場合は省略されます。 |
| `values` | テキストとしての値：`{ "<parameter>": "<value>" }`。 |
| `definitions` | `includeDefinitions`指定時のみ：読み取った各パラメータの`{ "<parameter>": { localizedName, type, choices } }`。`type`は詳細に記載された型名です。`choices`（ユニバーサルな選択肢）は`popUp`の場合のみ返されます。 |
| `curated` | `curated`指定時のみ：`{ param, label, value, display }`の配列。ドアまたは窓でないプラグインオブジェクトでは空です。 |

エラー：`object not found`、`object is not a parametric plug-in object (no parameter record)`。

### getObjectRecords

オブジェクトに付加されたデータレコードを読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

プラグインかどうかに関係なく、あらゆるオブジェクトに付加されたユーザーデータレコードを読み取ります。付加された内部用でない各レコードフォーマットについて、その名前、ローカライズされた名前、フィールド値を文字列として返します。必要に応じて、`records`で特定のレコードフォーマット名（ユニバーサル名またはローカライズされた名前。大文字と小文字を区別しない）に限定できます。内部のIFCレコードは省略されます。オブジェクトのIFCデータ（エンティティ、標準およびカスタムプロパティセット、IFCプロパティ型）はgetObjectIFCDataで、プロパティセットの定義はlistIFCPsetsとgetIFCPsetDefinitionで読み取ってください。

プラグインオブジェクトのパラメータレコードは含まれません。それにはgetObjectParametersを使用してください。レコードの値でオブジェクトを検索するには、"`('MyRecord'.'MyField' > 1)`"のような条件でfindObjectsを使用します。レコードフォーマットのフィールド定義はgetResourceDetailsで読み取ります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `records` | array of string |  | ユニバーサル名またはローカライズされた名前。大文字と小文字を区別しません。 |

**結果**

`{ object, records }`：`object`は[オブジェクト参照](Common.md#object-references)、`records`は読み取ったレコードごとに1項目を持つ配列です。

| キー | 説明 |
|---|---|
| `name` | レコードフォーマットのユニバーサル名。 |
| `localizedName` | ローカライズされた名前。レコードフォーマットに名称がない場合は省略されます。 |
| `values` | テキストとしてのフィールド値：`{ "<field>": "<value>" }`。 |

`records`の名前のうち、付加されたどのレコードにもないものは無視されます。レコードのないオブジェクトでは空の`records`になります。

エラー：`object not found`。

### setObjectParameter

プラグインオブジェクトの1つ以上のパラメータを書き込みます。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: setObjectParameter" · **runToolBatch内:** はい

**詳細**

パラメトリックなプラグインオブジェクトのパラメータを書き込みます。1つの`name`/`value`を設定するか（型はパラメータ定義から取得されるか、`type`で強制されます）、名前と値の組を格納した`params`オブジェクトを渡します。数値パラメータは数値の文字列も受け付けます（例："5"、"5.0"）。パラメータの型に変換できない値は書き込まれず、false（`ok`、または`applied`の該当項目）を報告します。その後、オブジェクトが再生成されます。

> **注:** `name`には2つの用途があります。単一パラメータの形式では書き込むパラメータの名前であり、またすべてのオブジェクトツールと同様にオブジェクトの検索にも使われます。検索は`uuid`、`name`、`index`の順で、前のもので見つからない場合に次のものが使われます。パラメータ名がオブジェクト名と取り違えられないように、オブジェクトは`uuid`で指定してください（推奨）。`params`を使う場合、`name`はオブジェクトの検索にのみ使われます。
>
> **注:** `params`がオブジェクトの場合はそれが優先され、`name`、`value`、`type`はパラメータには使われません。`name`の形式では、オブジェクトにそのパラメータがない場合は`parameter not found: <name>`で失敗します。`params`では不明な名前はエラーにならず、`applied`の該当項目が`false`になります。`false`は呼び出しの失敗ではありません。他の値は書き込まれ、オブジェクトは再生成され、呼び出しはロールバックされません。値はそのパラメータの型によって変換されます。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 単一パラメータの形式：書き込むパラメータの名前（`getObjectParameters`が返すとおり）。オブジェクトの検索にも使われます。上記の注を参照してください。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `value` | string or number or integer or boolean |  | `name`の値。型はパラメータ定義から取得されるか、`type`で強制されます。値がない場合は何も書き込まれず、`ok`は`false`になります。 |
| `type` | string |  | 次のいずれか：`string`、`real`、`int`、`bool`。`number`、`integer`、`boolean`も受け付け、それ以外のテキストでは値をテキストとして書き込みます。`name`と併用する場合のみ使用されます。 |
| `params` | object |  | プラグインの生のパラメータ`{ "ParamName": value }`。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。`name`と`value`より優先されます。オブジェクトでない`params`は無視されます。 |

**結果**

| 形式 | 結果 |
|---|---|
| `params` | `{ applied }`：`params`内の各名前について`{ "<parameter>": true or false }`。 |
| `name`と`value` | `{ ok }`：値が書き込まれた場合は`true`。 |

エラー：`object not found`、`object is not a parametric plug-in object`、`'name' (parameter name) is required, or provide a 'params' object`、および`name`の形式では`parameter not found: <name>`。

### getPluginDefinition

インストール済みのプラグインオブジェクトの種類、パラメータ、ポップアップの選択肢を示します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

インスタンスなしで、正確なユニバーサル名`universalName`（大文字と小文字を区別。findObjectsとgetObjectInfoが返す`parametricName`。例："Drawing Label2"、"Revision Cloud"）により、インストール済みのプラグインオブジェクト（PIO）を記述します。`universalName`、`localizedName`、`kind`（createPluginObjectでの配置方法：point、linear、rectangle、customは`position`を、path2D、path3Dは`pathUuid`を使用）、グループに専用の作成ツールがある場合は`dedicatedTool` { tool, group }（createPluginObjectでは拒否されるため、そのツールを使用）、および宣言順の`parameters`を返します：[{ name（createPluginObjectの`params`とsetObjectParameterが受け付けるユニバーサル名）, localizedName, type（integer、boolean、real、text、dimension、popUp、angle、coordLocXなど）, defaultValue（テキスト）, choices（popUpパラメータのユニバーサルな選択肢） }]。

不明な名前、大文字と小文字が異なる名前、インストールされていないプラグイン、メニューコマンドまたはツールに対してはエラーを返します。何も変更しません。プラグインのパラメータレコードフォーマットがファイルにない場合は、読み取るためだけに、内部の取り消しイベントの中でフォーマットを定義してそれを取り消すため、フォーマットも取り消しステップも残りません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `universalName` | string | はい | プラグインオブジェクトの正確なユニバーサル名（大文字と小文字を区別）：`findObjects`と`getObjectInfo`が返す`parametricName`です。 |

**結果**

| キー | 説明 |
|---|---|
| `universalName` | ユニバーサル名。 |
| `localizedName` | ローカライズされた名前。ない場合は省略されます。 |
| `kind` | `createPluginObject`がプラグインオブジェクトを配置する方法（詳細に記載のとおり）。 |
| `dedicatedTool` | `{ tool, group }`。このプラグインオブジェクト専用の作成ツールを持つグループがある場合のみ。 |
| `parameters` | 宣言順のパラメータ：`{ name, localizedName, type, defaultValue, choices }`。`defaultValue`はテキストです。`choices`（ユニバーサルな選択肢）は`popUp`の場合のみ返されます。 |

エラー：`'universalName' is required: the universal name of a plug-in object, e.g. the 'parametricName' that findObjects and getObjectInfo report for an existing one`と`no plug-in object '<universalName>' is installed: …`（メニューコマンドやツールの場合も含む）。名前が、専用の作成ツールを持つプラグインオブジェクトの名前で、大文字と小文字が異なる場合や、ここにインストールされていない場合は、エラーにその正確なユニバーサル名と使用するツールも示されます。

### createPluginObject

専用の作成ツールがないプラグインオブジェクトを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createPluginObject" · **runToolBatch内:** はい

**詳細**

正確なユニバーサル名`universalName`（大文字と小文字を区別。getPluginDefinitionで種類とパラメータを確認できます）でプラグインオブジェクト（PIO）を作成します。専用の作成ツールを持たないプラグインのみが対象です。ドア、窓、スラブ、柱、階段、植栽、舗床、ランドスケープエリア、造成図形、境界線、地形モデル、レベル、既存樹木、Lighting Device、ConnectCADのDeviceとSocket、データタグ、図面枠は拒否され、エラーに使用すべきツールが示されます（getPluginDefinitionの`dedicatedTool`）。

種類によって配置方法が決まります。point、linear、rectangle、customのプラグインオブジェクトは`position`（ワールド座標の点）に作成され、省略可能な`angle`（ラジアン）で回転します。path2Dまたはpath3Dのものは`pathUuid`を使用し、`position`や`angle`は使用しません。パスには、アクティブレイヤ（またはレイヤ上の編集中のグループ）の直接のメンバーである既存のオブジェクトを指定します。プラグインツールが選択した図形を扱うのと同様に、新しいオブジェクトがそれをパスとして引き継ぎます。コピーではなくオブジェクト自体を使うため、そのオブジェクトはレイヤから外れ、2D図形はVectorworksによって曲線に変換されます。

編集中のシンボル定義、またはその中のグループにあるパスは拒否されます。Vectorworksはパスがレイヤにある場合にのみパスの変更を記録するため、取り消すと新しいオブジェクトとともにパスも削除されてしまいます。レイヤ上のパスからオブジェクトを作成し、editObjectの`moveToContainer`でシンボル定義の中へ移動してください。path2Dのプラグインオブジェクトは、四角形、角丸四角形、長円、円弧、多角形、フリーハンド、曲線を受け付けます。path3Dのものは、さらに3D 多角形、NURBS曲線、NURBS曲面も受け付けます。

編集 &gt; 取り消しは新しいオブジェクトを削除し、パスを元に戻します。省略可能な`params` { "ParamName": value }は、setObjectParameterの`params`と同様にユニバーサル名でパラメータを設定し、その後オブジェクトが再生成されます。`applied`はそれぞれの結果を報告します。作成オプションclass、useClassAttributes、name、selectが適用されます。何かを変更する前にすべてを検証します。不明な名前や大文字と小文字が異なる名前、`pathUuid`や`position`の不足または余分な指定、アクティブなコンテナの外・シンボル定義内・別の形状のパスオブジェクト、不明なパラメータ名、パラメータに合わない値は呼び出しを拒否し、その場合は何も作成されません。

プラグインがその場所にオブジェクトを置くことを許可しない場合や、新しいオブジェクトが受け付けないパラメータがある場合は呼び出しが失敗し、ロールバックされます。新しいオブジェクトの参照と`kind`、パスを持つプラグインオブジェクトではその`pathObject`を返します。プラグインを使用する場合と同様に、プラグインのパラメータレコードフォーマットがファイルにない場合は追加します（拒否または失敗した呼び出しでは、それも含めてロールバックされます）。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `universalName` | string | はい | 大文字と小文字を区別します。getPluginDefinitionで種類とパラメータを確認できます。 |
| `position` | [点](Common.md#points) |  | ワールド座標の点`{ x, y }`。point、linear、rectangle、customのプラグインオブジェクトでは必須で、パスのものでは指定できません。 |
| `angle` | number |  | 反時計回りの角度。ラジアン。デフォルトは0。パスのプラグインオブジェクトでは指定できません。 |
| `pathUuid` | string |  | パスを提供するオブジェクトのUUID。`path2D`または`path3D`のプラグインオブジェクトでは必須で、それ以外の種類では指定できません。 |
| `params` | object |  | プラグインの生のパラメータ`{ "ParamName": value }`（ユニバーサル名）。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。何かを作成する前に、すべての名前と値が検証されます。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

**結果**

新しいオブジェクトの[オブジェクト参照](Common.md#object-references)に、次のキーが追加されます。

| キー | 説明 |
|---|---|
| `kind` | プラグインオブジェクトの種類：`point`、`linear`、`rectangle`、`custom`、`path2D`、`path3D`。 |
| `applied` | `params`が指定され、空でない場合のみ：各パラメータの`{ "<parameter>": true }`。書き込まれないパラメータがあると呼び出しが失敗するため、すべての項目が`true`です。 |
| `pathObject` | `path2D`または`path3D`のプラグインオブジェクトの場合のみ：そのパスオブジェクト（`pathUuid`で指定したオブジェクト）のオブジェクト参照。 |

何かが作成される前に呼び出しを拒否するエラー：

- `'universalName' is required: …`と`no plug-in object '<universalName>' is installed: …`（`getPluginDefinition`と同じ）。
- `'<universalName>' has a create tool of its own, which knows the object and keeps it consistent: use <tool> of the <group> …`。
- `path2D`または`path3D`のプラグインオブジェクトの場合：`'<universalName>' is a plug-in object of kind '<kind>': give 'pathUuid', the uuid of the object of the active layer that becomes its path …`、および`…, which its path places: give 'pathUuid' without 'position' or 'angle'`。
- その他の種類の場合：`'<universalName>' is a plug-in object of kind '<kind>': give 'position', a point { x, y } in world units`、`…, which is placed at 'position' (turned by 'angle'): it takes no 'pathUuid'`、および`'angle' must be a number (radians)`。
- 合わないパス：`path object not found ('pathUuid' is the uuid of an object of the active layer)`、`the path object is not a direct member of the active layer (or of the group being edited) …`、`the path object is not in a layer …`、および`the path object is <type>, which a plug-in object of kind '<kind>' does not take as its path: give …`。
- `'params' must be an object of universal parameter names and values: { "ParamName": value }`、`the plug-in object '<universalName>' has no parameter <names>: 'params' takes universal parameter names (getPluginDefinition lists them)`、および`these 'params' values do not fit the type of their parameter: <names> (real and integer parameters take a number or a numeric string, boolean ones true or false, the others text)`。

チェックを通過した後のエラー。どちらも呼び出しをロールバックするため（`rolledBack`）、何も残りません：

- `Vectorworks did not create the plug-in object '<universalName>', for example because the active layer, group or symbol definition does not allow this plug-in object`。
- `the new plug-in object '<universalName>' did not take the parameter(s) <names>, for example a parameter that its plug-in style sets`。この`err`には`applied`もあり、受け付けられなかった各パラメータが`false`になります。
