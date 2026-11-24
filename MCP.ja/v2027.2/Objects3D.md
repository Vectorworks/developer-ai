[English](../../MCP/v2027.2/Objects3D.md) • [Deutsch](../../MCP.de/v2027.2/Objects3D.md) • **日本語**

# Objects3D — 3Dモデリング

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

ソリッド、3D 多角形、メッシュ、NURBS曲線と曲面、サーフェスモデルの3D形状を作成、読み取り、編集するツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [3D Modeling](#3d-modeling)
  - [createExtrude](#createextrude)
  - [createSolidPrimitive](#createsolidprimitive)
  - [createSweep](#createsweep)
  - [combineSolids](#combinesolids)
  - [createShell](#createshell)
  - [convertSolid](#convertsolid)
  - [getSolid](#getsolid)
  - [editSolid](#editsolid)
  - [create3DPolygon](#create3dpolygon)
  - [createMesh](#createmesh)
  - [createNurbsCurve](#createnurbscurve)
  - [createNurbsSurface](#createnurbssurface)
  - [createSurfaceModel](#createsurfacemodel)
  - [get3DGeometry](#get3dgeometry)
  - [edit3DGeometry](#edit3dgeometry)
  - [convertTo3D](#convertto3d)

<a id="overview"></a>

## 概要

このフォルダには、1個のツールグループに合計16個のツールが含まれています。

| グループ | グループID | 初期状態で有効 | リスクレベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [3D Modeling](#3d-modeling) | `3d-modeling` | いいえ | 中 | 16 | ソリッド、3D 多角形、メッシュ、NURBS曲線と曲面、サーフェスモデルを作成、読み取り、編集します。 |

## 3D Modeling

> **グループ:** `3D Modeling` · **グループID:** `3d-modeling` · **初期状態で有効:** いいえ · **リスクレベル:** 中 · **ツール数:** 16

**ソリッド、3D 多角形、メッシュ、NURBS曲線と曲面、サーフェスモデルを作成、読み取り、編集します。**

3Dソリッドの作成、読み取り、編集を行います。押し出し（点、矩形、2D図形、同一平面上の3D点から、または2つの3D点の間に作成。穴と3D空間での配置に対応）、多段押し出し、テーパ押し出し（createExtrude）、球、楕円体、半球、円錐、直方体、円筒、トーラス（createSolidPrimitive）、断面を軸の周りに回転させた回転体（createSweep）を作成します。ソリッドを合成して汎用ソリッドにし（combineSolids）、シェルを作成し（createShell）、ソリッドを汎用ソリッドやメッシュに変換します（convertSolid）。種類、3Dボックス、パラメータ、汎用ソリッドの履歴を読み取り（getSolid）、押し出し、多段押し出し、回転体、球、半球、円錐の移動、回転、拡大縮小、向きの変更、サイズ変更を行います（editSolid）。3D 多角形とメッシュ：3D点、2D点、または指定したZの矩形から3D 多角形を作成し（create3DPolygon）、頂点と面、多角形、または3D 多角形のグループからメッシュを作成します（createMesh）。それらの頂点、面、平面、面積、体積、スムージング、パーツを読み取り、各リストはページ単位で返されます（`limit`、`offset`、`countOnly`）（get3DGeometry）。頂点、面、閉じた状態、スムージング、パーツを編集し、簡素化、分割、移動、回転、拡大縮小を行い、3D 多角形から平面ソリッドを、メッシュから修復済みのコピーを作成します（edit3DGeometry）。あらゆる2Dまたは3Dオブジェクトを、3D 多角形のグループ、メッシュ、汎用ソリッドに変換します（convertTo3D）。

**NURBS曲線と曲面：** 制御点（重み付き）または補間点から、指定した次数の曲線を作成し（createNurbsCurve）、次数と重みを持つ制御点ネットpoints[u][v]から曲面を作成します（createNurbsSurface）。それらのピース、点、重み、ノットを読み取り、曲線を測定します：指定距離の点、最近点、指定パラメータでの接線と曲率を伴う点、等分（get3DGeometry）。点と重みを設定し、曲線で曲面をトリミングし、曲線と曲面の延長コピーとオフセットコピーを作成します（edit3DGeometry。NURBSはmove3D、rotate3D、scale3D、ノットの編集を受け付けません）。NURBS曲面によるサーフェスモデル：断面を通るロフト、1本または2本のレールに沿った断面のレールスイープ、断面の回転（その左端を軸に、またはレールに沿って軸の周りに）、パスに沿った断面の押し出し。結果はNURBS曲面、汎用ソリッド、またはそれらのグループです（createSurfaceModel）。長さはワールド単位、角度はラジアンです。指定する3D座標と返される3D座標（点、中心、座標フレーム、baseElevation、bounds3D）はすべて絶対的なワールドZです。ツールはこれらにデザインレイヤの高さを加えないため、z 0で指定したオブジェクトは、高さのあるレイヤの平面上ではなく、ワールドZ 0に置かれます。高さEのレイヤの平面上にオブジェクトを置くには、そのZ値にEを加えてください。layerElevationは、所属するデザインレイヤのEを返します（所属するデザインレイヤがない場合はnull）。新しいオブジェクトは通常アクティブレイヤに配置されます。シェルと変換の結果は元のオブジェクトのコンテナに残ることがあります。省略可能な作成オプション`select`は、結果を選択するかどうかを制御します。入力図形は変更されません。ツールはそれらをコピーします（不要になった場合は、後でeditObjectのaction deleteで削除してください）。各変更は、固有の名前を持つ、取り消し可能なVectorworksの操作として実行されます。拒否された呼び出しは何も変更しません。

> **注:** `combineSolids`、`createShell`、`convertSolid`、`convertTo3D`は、他の作成ツールと同様に、結果の選択状態を`select`に合わせます。元のオブジェクトが選択されていても、結果は`select`がtrueの場合にのみ選択されます。

> **注:** `createShell`と`convertSolid`（`genericSolid`と`mesh`の両方）は、結果を常に元のオブジェクトの直後、元のオブジェクトのコンテナ（レイヤ、シンボル定義、またはグループ）に配置します。`combineSolids`は結果を、オペランドの隣ではなく、アクティブレイヤ、または編集中のグループやシンボル定義に配置します。

| ツール | 作用 | リスク | 概要 |
|---|---|---|---|
| [`createExtrude`](#createextrude) | 編集 | 中 | 押し出し、多段押し出し、またはテーパ押し出しを作成します。 |
| [`createSolidPrimitive`](#createsolidprimitive) | 編集 | 中 | 球、楕円体、半球、円錐、直方体、円筒、トーラスを作成します。 |
| [`createSweep`](#createsweep) | 編集 | 中 | 回転体（軸の周りに回転させた2D断面）を作成します。 |
| [`combineSolids`](#combinesolids) | 編集 | 中 | 和集合、共通部分、差分の演算で2つのソリッドを汎用ソリッドに合成します。 |
| [`createShell`](#createshell) | 編集 | 中 | NURBS曲面に厚みを付けるか、ソリッドを中空にして、シェルを作成します。 |
| [`convertSolid`](#convertsolid) | 編集 | 中 | ソリッドを汎用ソリッドまたはメッシュに変換したコピーを作成します。 |
| [`getSolid`](#getsolid) | 読み取り専用 | 低 | ソリッドの種類、3D境界、パラメータ、汎用ソリッドの履歴を読み取ります。 |
| [`editSolid`](#editsolid) | 編集 | 中 | ソリッドの移動、回転、拡大縮小、向きの変更、サイズ変更を行います。 |
| [`create3DPolygon`](#create3dpolygon) | 編集 | 中 | 3D点、指定した高さの2D点、または矩形から3D 多角形を作成します。 |
| [`createMesh`](#createmesh) | 編集 | 中 | 頂点と面、多角形、または3D 多角形のグループからメッシュを作成します。 |
| [`createNurbsCurve`](#createnurbscurve) | 編集 | 中 | 制御点または補間点からNURBS曲線を作成します。 |
| [`createNurbsSurface`](#createnurbssurface) | 編集 | 中 | 制御点ネットからNURBS曲面を作成します。 |
| [`createSurfaceModel`](#createsurfacemodel) | 編集 | 中 | 既存のオブジェクトから、ロフト（多段曲面）、レールスイープ、回転、パス押し出しのサーフェスモデルを作成します。 |
| [`get3DGeometry`](#get3dgeometry) | 読み取り専用 | 低 | 3D 多角形、メッシュ、NURBS曲線、NURBS曲面を読み取ります。 |
| [`edit3DGeometry`](#edit3dgeometry) | 編集 | 中 | 3D 多角形、メッシュ、NURBS曲線、NURBS曲面を編集します。 |
| [`convertTo3D`](#convertto3d) | 編集 | 中 | オブジェクトのコピーを3D 多角形、メッシュ、または汎用ソリッドに変換します。 |

### createExtrude

押し出し、多段押し出し、またはテーパ押し出しを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createExtrude" · **runToolBatch内:** はい

**詳細**

次の断面のソースのうち、ちょうど1つから押し出しを作成します。`points`（3個以上の点{ x, y }：XY平面上の閉じた断面）、`rect` { left, top, right, bottom }（getObjectInfoの`bounds`が返す形式）、`profileUuid`（2D図形：直線、四角形、角丸四角形、長円、円弧、多角形、フリーハンド、曲線）、`points3D`（ワールドZで指定した、同一平面上の3個以上の3D点{ x, y, z }。断面はその平面上にあり、法線方向に押し出されます）、`profileUuids`（断面の順に並べた2個以上の2D図形：多段押し出し。断面は`baseElevation`から`baseElevation` + `thickness`まで等間隔に配置されます）。

`thickness`は必須です（0以外。負の厚さは反対方向に押し出します）。`baseElevation`（デフォルトは0、ワールドZ）は、points、rect、profileUuid、profileUuidsに適用されます。`between` { start, end, up? }（3D点）を`profileUuid`または`points`と併用すると、代わりに断面をstartからendへ、startを原点として押し出します（厚さは2点間の距離。断面の+Yは`up`に従い、デフォルトはワールドZ、垂直な押し出しではワールドY。`up`はend - startと平行であってはいけません）。この場合、thicknessとbaseElevationは指定しません。

`taper` { angle, height }を`profileUuid`と併用すると、側面が`height`（0以外）にわたって`angle`（ラジアン、|angle| &lt; pi/2）だけ傾斜するテーパ押し出しを作成します。結果はNURBS曲面、CSGソリッド、またはそれらのグループ（kind surfaceModel）で、thicknessやbaseElevationは指定しません。単一の押し出しは`holes`を受け付けます。断面の座標で指定する{ points }（3個以上の点）または{ uuid }（閉じた2D図形）の配列です。追加できない穴があると呼び出しは拒否されます。

`transform` { origin, uAxis, vAxis, wAxis? }は、points、rect、profileUuidから作成した単一の押し出しを3D空間に配置します。originはワールドZで指定し、ローカル軸は正規直交の単位ベクトルです（wAxisのデフォルトはuAxis x vAxis）。UUIDで指定した図形はコピーされ、変更されません。何かを作成する前に、すべての引数を検証します。オブジェクト参照、`kind`（extrude、multipleExtrude、surfaceModel）、ワールドZの`bounds3D` { min, max }、ワールド単位の`layerElevation`を返します。getSolidで押し出しを読み取れます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `points` | array of [点](Common.md#points) |  | 3個以上の点{ x, y }：XY平面上の閉じた断面。 |
| `rect` | [矩形](Common.md#rectangles) |  |  |
| `profileUuid` | string |  | 2D図形：直線、四角形、角丸四角形、長円、円弧、多角形、フリーハンド、曲線。 |
| `points3D` | array of [3D点](Common.md#points) |  | 各項目：ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `profileUuids` | array of string |  |  |
| `baseElevation` | number |  | 底面のワールドZ（デフォルトは0）。`points`、`rect`、`profileUuid`、`profileUuids`に適用されます。 |
| `thickness` | number |  | 厚さ。ワールド単位。 |
| `between` | object |  |  |
| `between.start` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `between.end` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `between.up` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `taper` | object |  |  |
| `taper.angle` | number | はい |  |
| `taper.height` | number | はい |  |
| `holes` | array of object |  |  |
| `holes[].points` | array of [点](Common.md#points) |  |  |
| `holes[].uuid` | string |  |  |
| `transform` | object |  | `points`、`rect`、`profileUuid`から作成する単一の押し出しの3D配置{ origin, uAxis, vAxis, wAxis? }。`between`、`points3D`、`profileUuids`、`taper`と併用すると拒否されます。 |
| `transform.origin` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `transform.uAxis` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `transform.vAxis` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `transform.wAxis` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createSolidPrimitive

球、楕円体、半球、円錐、直方体、円筒、トーラスを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createSolidPrimitive" · **runToolBatch内:** はい

**詳細**

`kind`で指定した種類のソリッドプリミティブを作成します。sphere（`center`と`radius`、またはワールド軸に沿った半径を持つ楕円体の場合は`radii` { x, y, z }）、hemisphere（+Z方向のドームの場合は`center`と`radius`、またはドームの頂部である`topPoint`）、cone（`baseCenter`と`radius`に加えて、+Z方向の直円錐の場合は`height`（負の高さでは-Z方向を向く）、または`tipPoint`）、box（対角の頂点`minimum`と`maximum`：押し出し）、cylinder（`baseCenter`、`radius`、`height`（0以外）でZ方向：円の押し出し）、torus（`center`、`majorRadius` &gt; `minorRadius` &gt; 0、ワールドZ軸の周り：回転体）。

点はワールドZで指定します。半径は正の値である必要があります。何かを作成する前に、すべての引数を検証します。オブジェクト参照、getSolidが返すものと同じ`kind`（sphere、hemisphere、cone。直方体や円筒はextrude、トーラスはsweep）、ワールドZの`bounds3D` { min, max }、ワールド単位の`layerElevation`を返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `kind` | string | はい | 次のいずれか：`sphere`、`hemisphere`、`cone`、`box`、`cylinder`、`torus`。 |
| `center` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `radius` | number |  | 半径。ワールド単位。 |
| `radii` | [3D点](Common.md#points) |  | 球のみ。`radius`の代わりに指定します（楕円体）：ワールドのX、Y、Z軸に沿った正の半軸の長さ{ x, y, z }（ワールド単位）。点ではないため、`z`にレイヤの高さを加えないでください。 |
| `topPoint` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `baseCenter` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `height` | number |  | 高さ。ワールド単位。 |
| `tipPoint` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `minimum` | [3D点](Common.md#points) |  | `box`用：下側の角。`maximum`の各座標は`minimum`の座標より大きい必要があります。ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `maximum` | [3D点](Common.md#points) |  | `box`用：上側の角。各座標は`minimum`の座標より大きい必要があります。ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `majorRadius` | number |  |  |
| `minorRadius` | number |  |  |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createSweep

回転体（軸の周りに回転させた2D断面）を作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createSweep" · **runToolBatch内:** はい

**詳細**

2D図形`profileUuids`（1個以上：直線、四角形、角丸四角形、長円、円弧、多角形、フリーハンド、曲線）のコピーから、回転によるソリッドまたは曲面である回転体を作成します。断面のXが半径、Yが軸方向になります。軸はYに平行で、2D 基準点`axisUuid`（コピーされます）を通るか、指定しない場合は断面の左端に沿います。新しい回転体は、ワールドYに平行な直線を軸に回転します。

`startAngle`（デフォルトは0）、`sweepAngle`（デフォルトは2\*piで1回転。負の値は反対方向に回転）、`incrementAngle`（デフォルトはpi/36。正の値で、各セグメントの角度）、`pitch`（デフォルトは0。らせんの場合の1回転あたりの軸方向の上昇量。ワールド単位）。断面と軸の基準点は2D図形で、XとYで読み取られます。bounds3Dは、回転体がワールドZのどこにあるかを示します。何かを作成する前に、すべての引数を検証します。

オブジェクト参照、`kind` sweep、ワールドZの`bounds3D` { min, max }、ワールド単位の`layerElevation`を返します。editSolidで角度とピッチを変更できます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `profileUuids` | array of string | はい | 1個以上：直線、四角形、角丸四角形、長円、円弧、多角形、フリーハンド、曲線。 |
| `axisUuid` | string |  |  |
| `startAngle` | number |  | 反時計回りの開始角度。ラジアン。 |
| `sweepAngle` | number |  | 円弧角。ラジアン。0以外。正の値は反時計回り。 |
| `incrementAngle` | number |  | 各セグメントの角度（ラジアン）：正の値で、`sweepAngle`全体で3600セグメント以下（デフォルトはpi/36）。 |
| `pitch` | number |  |  |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### combineSolids

和集合、共通部分、差分の演算で2つのソリッドを汎用ソリッドに合成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: combineSolids" · **runToolBatch内:** はい

**詳細**

`blankUuid`と`toolUuid`で指定した2つのソリッドオブジェクトを、`operation`のunion、intersection、differenceで合成します。両方の入力はコピーされ、変更されません。ロックされたソリッド、またはレイヤ、シンボル定義、それらの中のグループにないソリッドは拒否されます。結果はブーリアン演算とその履歴を持つ汎用ソリッドです。結果には、ワールドZの`bounds3D` { min, max }とワールド単位の`layerElevation`が含まれます。

> **注:** 結果には、新しいソリッドのgetSolidの値が含まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `operation` | string | はい | 次のいずれか：`union`、`intersection`、`difference`。 |
| `blankUuid` | string | はい |  |
| `toolUuid` | string | はい |  |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createShell

NURBS曲面に厚みを付けるか、ソリッドを中空にして、シェルを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createShell" · **runToolBatch内:** はい

**詳細**

NURBS曲面（厚みを付ける）またはソリッド（中空にする）からシェルを作成します。`uuid`で元のオブジェクトを指定し、`thickness`は有限で0以外の符号付きの値です。ソリッドの場合、`openFaceIndices`は取り除く面（0始まり）の空でない配列です。元のオブジェクトはコピーされ、変更されません。シェルはアクティブレイヤに配置される代わりに、元のオブジェクトのコンテナに残ることがあります。

ロックされた元のオブジェクト、またはレイヤ、シンボル定義、それらの中のグループにない元のオブジェクトは拒否されます。省略可能な作成オプション`select`は、シェルを選択するかどうかを制御します。kind shell、汎用ソリッドの履歴、取得できる場合は元のオブジェクトの現在の面に対応付けた`openFaceIndices`、ワールドZの`bounds3D` { min, max }、ワールド単位の`layerElevation`を返します。

> **注:** 結果には、新しいソリッドのgetSolidの値が含まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string | はい | 元のNURBS曲面またはソリッドのUUID（UUIDのみ。`name`は新しいシェルの名前です）。 |
| `thickness` | number | はい | 厚さ。ワールド単位。 |
| `openFaceIndices` | array of integer | ソリッドの場合 | ソリッドを元にする場合は必須：取り除く面（0始まり）の空でない配列（各インデックスはソリッドの面数未満）。NURBS曲面では拒否されます。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### convertSolid

ソリッドを汎用ソリッドまたはメッシュに変換したコピーを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: convertSolid" · **runToolBatch内:** はい

**詳細**

`sourceUuid`で指定した対応するソリッドのコピーを作成し、`genericSolid`（履歴なし）または`mesh`に変換します。元のソリッドは変更されません。汎用ソリッドの結果は、アクティブレイヤに配置される代わりに元のソリッドのコンテナに残ることがあります。レイヤ、シンボル定義、それらの中のグループにないソリッドは拒否され、`genericSolid`への変換ではロックされたソリッドも拒否されます。

省略可能な作成オプション`select`は、結果を選択するかどうかを制御します。オブジェクト参照、結果の`kind`、ワールドZの`bounds3D` { min, max }、ワールド単位の`layerElevation`を返します。汎用ソリッドの結果には、その履歴も含まれます。

> **注:** 結果には、新しいソリッドのgetSolidの値が含まれます（`convertSolid`では、`to`が`genericSolid`の場合のみ）。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `sourceUuid` | string | はい |  |
| `to` | string | はい | 次のいずれか：`genericSolid`、`mesh`。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### getSolid

ソリッドの種類、3D境界、パラメータ、汎用ソリッドの履歴を読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

uuid、name、またはindexでソリッドを読み取ります。オブジェクト参照、`kind`（extrude、multipleExtrude、sweep、sphere、hemisphere、cone、genericSolid、shell）、ワールドZの`bounds3D` { min, max }、ワールド単位の`layerElevation`（所属するデザインレイヤがない場合はnull）、およびその種類の値を返します。座標フレーム、中心、点、高さも、作成ツールと編集ツールの引数と同じくワールドZです。座標系の間での変換は行われません。extrude：baseElevation、thickness、topElevation、transform { origin, uAxis, vAxis, wAxis }、volume、profileBounds（2D。断面の座標）、holeCount、holes [{ index, bounds }]。multipleExtrude：baseElevation、thickness、topElevation、profileCount。sweep：startAngle、sweepAngle、incrementAngle、pitch、profileCount（軸の基準点は含まない）。sphereとhemisphere：center、radii { x, y, z }（ローカル軸方向）、isEllipsoid、frame { origin, uAxis, vAxis, wAxis }、axis（ローカルZ。半球のドームはこの方向を向く）、volume、surfaceArea。hemisphereではtopPointも返します。cone：baseCenter、tipPoint、height、radii { i, j }、isRightCone、isElliptical、frame、axis（底面から頂点への方向）、解析的なvolumeとsurfaceArea。非対称の円錐の面積は既存の多角形キャッシュから閉じた表面を近似したもので、取得できない場合は省略されます。直円錐では解析的な側面積が保持されます。

**汎用ソリッドとシェル：** hasHistory、判明している場合はoperation、volume、surfaceArea、およびオブジェクト参照、入れ子の深さ、オペランドのインデックス、親のUUID、入れ子の演算を持つ履歴項目を返します。シェルでは、取得できる場合はthickness、openFaceIndices（永続的な面の名前を解決した、元のオブジェクトの現在のインデックス）、sourceUuidも返します。体積と面積はワールド単位です。Vectorworksが返せない値は省略されます。

> **注:** 汎用ソリッドとシェルでは、`history`はソリッドとそのオペランドを前順（pre-order）で列挙し、`depth` 0のソリッド自体から始まります。各項目は、`depth`、`hasHistory`（汎用ソリッドでないオペランドではfalse）、およびオペランド（`depth` &gt; 0）では`operandIndex`と`parentUuid`（取得できる場合）を持つ[オブジェクト参照](Common.md#object-references)です。ブーリアン演算の汎用ソリッドの項目には`operation`（`union`、`intersection`、`difference`）が追加されます。シェルの`sourceUuid`は、シェルが保持している元のオブジェクトのコピーであり、createShellに指定した`uuid`ではありません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |

### editSolid

ソリッドの移動、回転、拡大縮小、向きの変更、サイズ変更を行います。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: editSolid" · **runToolBatch内:** はい

**詳細**

uuid、name、またはindexで対応するソリッドを編集します。1回の呼び出しは1つの取り消しステップです。次の場合は何も変更せずに拒否します：getSolidが受け付けないオブジェクト、汎用ソリッドまたはシェル（getSolidはその履歴を読み取りますが、editSolidでは編集しません）、ロックされたソリッド（先にeditObjectの`locked` falseでロックを解除してください）、レイヤ・シンボル定義・それらの中のグループにないソリッド（例：汎用ソリッドのオペランド、または壁・プラグインオブジェクト・ビューポートの中にあるもの）、その種類が受け付けない操作、正しくない値、変更のない呼び出し。

操作は次の順序で適用されます：押し出し、球、半球、円錐では`transform` { origin, uAxis, vAxis, wAxis? }（正規直交。球、半球、円錐は右手系の座標フレームを受け付けます）、`move3D` { offset }、`rotate3D` { center, axis, angle }（ラジアン。軸の周りに右手系）。球、半球、円錐では`scale3D` { center, factor &gt; 0 }と`axis`（ローカルZをこの方向に向ける）。押し出しと多段押し出しでは`baseElevation`、`thickness`、`topElevation`（厚さを設定。`thickness`との併用不可）。押し出しでは`removeHoles`（getSolidの`holes`のインデックス）または`removeAllHoles` true、その後`addHoles`（createExtrudeの`holes`と同じ）。球と半球：`center`、その後`radius`または`radii` { x, y, z }。半球：`topPoint`（ドームをその点に向け、半径をその点までの距離に設定）。円錐：`baseCenter`（円錐を移動）、`keepRight`を伴う`tipPoint`（デフォルトはtrue：直円錐を保つように円錐が回転。falseは底面の平面を保持し、斜円錐にする）、`height`（直円錐にする。負の値で反転）、`radius`または`radii` { i, j }。回転体：`startAngle`、`sweepAngle`、`incrementAngle`、`pitch`。

オブジェクト参照、`changed`（適用された引数を順に列挙）、および変更後のgetSolidの値を返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `transform` | object |  |  |
| `transform.origin` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `transform.uAxis` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `transform.vAxis` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `transform.wAxis` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `move3D` | object |  |  |
| `move3D.offset` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `rotate3D` | object |  |  |
| `rotate3D.center` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `rotate3D.axis` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `rotate3D.angle` | number | はい |  |
| `scale3D` | object |  |  |
| `scale3D.center` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `scale3D.factor` | number | はい |  |
| `axis` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `baseElevation` | number |  | 底面のワールドZ（押し出しまたは多段押し出しの場合）。 |
| `thickness` | number |  | 厚さ。ワールド単位。 |
| `topElevation` | number |  | 厚さを設定します。`thickness`との併用不可。 |
| `removeHoles` | array of integer |  | getSolidの`holes`のインデックス。 |
| `removeAllHoles` | boolean |  |  |
| `addHoles` | array of object |  | createExtrudeの`holes`と同じ。 |
| `addHoles[].points` | array of [点](Common.md#points) |  |  |
| `addHoles[].uuid` | string |  |  |
| `center` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `radius` | number |  | 半径。ワールド単位。 |
| `radii` | object |  | 球と半球：{ x, y, z }。円錐：{ i, j }。 |
| `radii.x` | number |  |  |
| `radii.y` | number |  |  |
| `radii.z` | number |  |  |
| `radii.i` | number |  |  |
| `radii.j` | number |  |  |
| `topPoint` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `baseCenter` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `tipPoint` | [3D点](Common.md#points) |  | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `keepRight` | boolean |  | 円錐で`tipPoint`と併用：デフォルトはtrueで、直円錐を保つように円錐が回転します。falseは底面の平面を保持します（斜円錐）。単独では編集になりません。 |
| `height` | number |  | 直円錐にします。負の値で反転します。 |
| `startAngle` | number |  | 反時計回りの開始角度。ラジアン。 |
| `sweepAngle` | number |  | 円弧角。ラジアン。0以外。正の値は反時計回り。 |
| `incrementAngle` | number |  | 各セグメントの角度（ラジアン）：正の値で、`sweepAngle`全体で3600セグメント以下。 |
| `pitch` | number |  |  |

### create3DPolygon

3D点、指定した高さの2D点、または矩形から3D 多角形を作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: create3DPolygon" · **runToolBatch内:** はい

**詳細**

次のソースのうち、ちょうど1つから3D 多角形を作成します。`points`（2～32767個の3D点{ x, y, z }。ワールドZ）、`points2D`（ワールドZが`z`（デフォルトは0）の平面上にある2～32767個の点{ x, y }）、または`z`の位置の`rect` { left, top, right, bottom }（getObjectInfoの`bounds`が返す形式）。`closed`（デフォルトはtrue）はpointsとpoints2Dに適用されます。rectは常に閉じており、`z`は`points`には適用されません。

何かを作成する前に、すべての引数を検証します。多角形はアクティブレイヤに配置されます。オブジェクト参照、`kind` polygon3D、`vertexCount`、`closed`、ワールドZの`bounds3D` { min, max }、`layerElevation`（所属するデザインレイヤのワールドZでの高さ。ない場合はnull）を返します。get3DGeometryで多角形を読み取り、edit3DGeometryで編集できます。

> **注:** `z`と`points`の併用（各点は独自のzを持つため）、および`closed` falseと`rect`の併用は拒否されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `points` | array of [3D点](Common.md#points) |  | 各項目：ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `points2D` | array of [点](Common.md#points) |  | ワールドZが`z`（デフォルトは0）の平面上にある2～32767個の点{ x, y }。 |
| `rect` | [矩形](Common.md#rectangles) |  |  |
| `z` | number |  | Z値（高さ）。ワールド単位。 |
| `closed` | boolean |  | 図形が閉じているかどうか。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createMesh

頂点と面、多角形、または3D 多角形のグループからメッシュを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createMesh" · **runToolBatch内:** はい

**詳細**

次のソースのうち、ちょうど1つからメッシュを作成します。`vertices`（3個以上の3D点{ x, y, z }。ワールドZ）と`faces`（面の配列。各面は`vertices`への0始まりのインデックスを3個以上含む配列で、外側から見て反時計回り）、`polygons`（多角形の配列。各多角形はワールドZの3個以上の3D点。同じ位置の点は共有頂点として結合されます）、または`groupUuid`（3D 多角形とそのグループだけを含むグループ。例：convertTo3Dの`polygons`の結果。メッシュはコピーから作成されてグループの直後に配置され、グループはそのまま残ります）。

ロックされたグループ、またはレイヤ、シンボル定義、それらの中のグループにないグループは拒否されます。何かを作成する前に、すべての引数を検証します。頂点または多角形から作成したメッシュはアクティブレイヤに配置されます。オブジェクト参照、`kind` mesh、`vertexCount`、`faceCount`、`isClosed`（隙間なく閉じているか）、ワールドZの`bounds3D` { min, max }、ワールド単位の`layerElevation`を返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `vertices` | array of [3D点](Common.md#points) |  | 各項目：ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `faces` | array of array of integer |  | 面の配列。各面は`vertices`への0始まりのインデックスを3個以上含む配列で、外側から見て反時計回りです。面はオブジェクト{ vertexIndices, part? }にすることもできます。`part`のデフォルトは0（全体のパーツ）です。 |
| `polygons` | array of array of [3D点](Common.md#points) |  | 多角形の配列。各多角形はワールドZの3個以上の3D点で、同じ位置の点は共有頂点として結合されます。 |
| `groupUuid` | string |  |  |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createNurbsCurve

制御点または補間点からNURBS曲線を作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createNurbsCurve" · **runToolBatch内:** はい

**詳細**

`points`（3D点{ x, y, z }。ワールドZ。2～1000個。ただし次数2以上の補間点の曲線では998個まで。Vectorworksはこの曲線に補間点より2個多い制御点を与えます）からNURBS曲線を作成します。`pointKind`はcontrol（デフォルト：点は制御点で、曲線はすべての点を通らずにそれらに沿います）またはfit（曲線はすべての点を通ります）です。`degree`（1～28の整数。デフォルトは3。次数dの制御点の曲線には少なくともd + 1個の点が必要）、`weights`（制御点のみ：各点に0.0001～100の重みを1つ。重みが大きいほど曲線がその点に引き寄せられます）。

何かを作成する前に、すべての引数を検証します。曲線はアクティブレイヤに配置されます。オブジェクト参照、`kind` nurbsCurve、`pieceCount`、`degree`、`pointCount`と`controlPointCount`（最初のピースの値）、`length`（取得できない場合はnull）、ワールドZの`bounds3D` { min, max }、`layerElevation`（所属するデザインレイヤのワールドZでの高さ。ない場合はnull）を返します。get3DGeometryで曲線を読み取り・測定し、edit3DGeometryで編集できます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `points` | array of [3D点](Common.md#points) | はい | 各項目：ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `pointKind` | string |  | 次のいずれか：`control`、`fit`。 |
| `degree` | integer |  | 1～28の整数。デフォルトは3。次数dの制御点の曲線には少なくともd + 1個の点が必要です。 |
| `weights` | array of number |  | 制御点のみ：各点に0.0001～100の重みを1つ指定します。重みが大きいほど曲線がその点に引き寄せられます。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createNurbsSurface

制御点ネットからNURBS曲面を作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createNurbsSurface" · **runToolBatch内:** はい

**詳細**

制御点ネット`points`からNURBS曲面を作成します。制御点ネットは2行以上の配列で、各行はワールドZの2個以上の3D点{ x, y, z }からなる配列であり、すべての行の長さは同じです。points[u][v]は行uの点vです（行数と各行の点数はそれぞれ32767以下）。`uDegree`と`vDegree`：1～28の整数。点がn個の方向ではn - 1までの次数を指定でき、デフォルトは3とn - 1の小さい方です。

`weights`（省略可能。`points`と同じ形：各制御点に0.0001～100の重み）。何かを作成する前に、すべての引数を検証します。曲面はアクティブレイヤに配置されます。オブジェクト参照、`kind` nurbsSurface、`uPointCount`、`vPointCount`、`uDegree`、`vDegree`、ワールドZの`bounds3D` { min, max }、ワールド単位の`layerElevation`を返します。get3DGeometryで曲面を読み取り、edit3DGeometryで編集できます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `points` | array of array of [3D点](Common.md#points) | はい | 順序どおりの点。 |
| `uDegree` | integer |  |  |
| `vDegree` | integer |  |  |
| `weights` | array of array of number |  |  |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### createSurfaceModel

既存のオブジェクトから、ロフト（多段曲面）、レールスイープ、回転、パス押し出しのサーフェスモデルを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createSurfaceModel" · **runToolBatch内:** はい

**詳細**

既存のオブジェクトのコピーから、`kind`のサーフェスモデルを作成します。元のオブジェクトは変更されません。loft：`sectionUuids`（順序どおりの2個以上の断面。各断面はNURBS曲線または3D 基準点で、少なくとも1つは曲線）を通して張ったNURBS曲面。`ruled`（デフォルトはfalse：滑らか。true：隣接する断面間を直線で結ぶ。断面が2つの場合は常に直線で結ぶロフトになります）と`closed`（デフォルトはfalse。trueでは最後の断面から最初の断面へロフトを戻すため、3個以上の断面がループ状（例：軸の周り）に並んでいる必要があります。断面が一列に並んでいると閉じる部分がロフトを横切り、Vectorworksはロフトを作成しません）。railSweep：`sectionUuids`（1個以上のNURBS曲線）を、NURBS曲線`railUuid`と、指定した場合は2本目のレール`secondRailUuid`に沿ってスイープします。

**loftとrailSweep：** `solid`（デフォルトはfalse：端が開いた曲面。true：閉じたロフトを除いて端面を付け、1つの汎用ソリッドに縫い合わせます。断面は閉じた曲線で、結果が閉じる必要があり、そうでない場合は何も作成されません）。revolve：2D図形`profileUuid`（直線、四角形、角丸四角形、長円、円弧、多角形、フリーハンド、曲線）を、createSweepが`axisUuid`なしで断面を回転させるのと同様に回転します（断面のXが半径、Yが軸方向で、軸は断面の左端、ワールドYに平行）。createSweepの`startAngle`（デフォルトは0）、`sweepAngle`（デフォルトは2\*pi）、`incrementAngle`（デフォルトはpi/36）、`pitch`（デフォルトは0）を使用し、createSweepの回転体と同じ形状と位置を、NURBS曲面で作成します。または、`railUuid`と必須の`axisUuid`を指定すると（断面、レール、軸はそれぞれ2D図形、NURBS曲線、3D 多角形のいずれか。角度とピッチは指定不可）、断面をレールに沿って軸の周りに回転します。軸は直線である必要があり、断面は軸と交差せずに軸と同じ平面上になければならず、レールはその平面から外れる必要があります（平面上のレールは、その平面に垂直な平面上にあります）。extrudeAlongPath：`profileUuid`（自己交差しない、平面上の2D図形、NURBS曲線、3D 多角形）を、NURBS曲線`pathUuid`に沿ってスイープします。`scale`（0より大きい値。デフォルトは1。デフォルトの線形の拡大縮小では、1で断面のサイズを保持）、`exponentialScale`（デフォルトはfalse：断面はパスに沿って線形に拡大縮小。true：指数的に拡大縮小）、`lockProfilePlane`（デフォルトはfalse。trueでは固定方向（VectorworksがパスをXY平面に回転させた後のZ）でスイープし、断面はその方向に対する向きを保持）、`fixProfile`（デフォルトはfalse。trueでは断面をパスの始点に回転させずに描画された位置のままスイープし、その場合、パスの始まりは断面の平面と平行であってはいけません）。閉じたパスや角のあるパスに沿う場合は、`exponentialScale`なしの`scale` 1のみが機能します。別の種類の引数や、2つの入力に同じオブジェクトを指定することは拒否されます。何かを作成する前に、すべての引数を検証します。結果はアクティブレイヤに配置されます。オブジェクト参照、`kind`（nurbsSurface。Vectorworksが複合曲面からソリッドを作成した場合はgenericSolid。複数の結果ではgroupで、`members` [{ reference, kind }]を伴う）、ワールドZの`bounds3D` { min, max }（NURBS曲面では、トリミングで切り取られた部分も含めたすべての制御点からVectorworksが求めたボックスのため、曲面より大きくなることがあります）、ワールド単位の`layerElevation`を返します。get3DGeometryでNURBS曲面を、getSolidで汎用ソリッドを読み取れます。

> **注:** これらのいずれでもない結果の`kind`は`surfaceModel`です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `kind` | string | はい | 次のいずれか：`loft`、`railSweep`、`revolve`、`extrudeAlongPath`。 |
| `sectionUuids` | array of string |  | `loft`：順序どおりの2個以上の断面（`closed`の場合は3個以上）。各断面はNURBS曲線または3D 基準点で、少なくとも1つは曲線。`railSweep`：1個以上のNURBS曲線。 |
| `ruled` | boolean |  |  |
| `closed` | boolean |  | 図形が閉じているかどうか。 |
| `solid` | boolean |  |  |
| `railUuid` | string |  | `railSweep`：NURBS曲線。`revolve`：2D図形、NURBS曲線、または3D 多角形（`axisUuid`と併用）。 |
| `secondRailUuid` | string |  | `railSweep`のみ：2本目のNURBS曲線のレール。 |
| `profileUuid` | string |  | `railUuid`なしの`revolve`：直線、四角形、角丸四角形、長円、円弧、多角形、フリーハンド、曲線。`railUuid`ありの`revolve`と`extrudeAlongPath`：2D図形、NURBS曲線、または3D 多角形（`extrudeAlongPath`では平面上にあり、自己交差しないもの）。 |
| `axisUuid` | string |  |  |
| `startAngle` | number |  | 反時計回りの開始角度。ラジアン。 |
| `sweepAngle` | number |  | 円弧角。ラジアン。0以外。正の値は反時計回り。 |
| `incrementAngle` | number |  | 各セグメントの角度（ラジアン）：正の値で、`sweepAngle`全体で3600セグメント以下（デフォルトはpi/36）。 |
| `pitch` | number |  |  |
| `pathUuid` | string |  | `extrudeAlongPath`：パスとなるNURBS曲線のUUID。 |
| `scale` | number |  | 0より大きい値。デフォルトは1。デフォルトの線形の拡大縮小では、1で断面のサイズを保持します。 |
| `exponentialScale` | boolean |  |  |
| `lockProfilePlane` | boolean |  |  |
| `fixProfile` | boolean |  |  |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |

### get3DGeometry

3D 多角形、メッシュ、NURBS曲線、NURBS曲面を読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

uuid、name、またはindexで3D 多角形、メッシュ、NURBS曲線、NURBS曲面を読み取ります（ソリッドはgetSolidで読み取ります）。頂点、点、`bounds3D` { min, max }はワールドZを使用します。`layerElevation`は所属するデザインレイヤのワールドZでの高さです（ない場合はnull）。角度はラジアンです。`limit`（デフォルトは100）、`offset`、`countOnly`は各リストに適用されます。リストは{ count, returned, offset, limit, truncated, nextOffset（打ち切られた場合）, items }です（countOnlyの場合はitemsなし）。3D 多角形：kind polygon3D、vertexCount、closed、planar、normal（単位ベクトル。頂点の順序に対して右手系。取得できない場合はnull）、plane { point, normal, d }（normal . p + d = 0。取得できない場合はnull）、area（開いている場合はnull）、length（閉じている場合は閉じる辺を含む）、bounds3D、layerElevation、`vertices`（項目は{ x, y, z }）。

**メッシュ：** kind mesh、vertexCount、faceCount、isClosed（隙間なく閉じているか）、surfaceArea、volume（閉じていない場合はnull）、smoothing（none、documentPreference、customCrease、imported）、creaseAngle（ラジアン。取得できない場合はnull）、parts [{ id, texture, faceCount }]（part 0は全体のパーツ。texture 0はなし）、bounds3D、layerElevation、`vertices`（項目は{ x, y, z }）、`faces`（項目は{ vertexIndices, part }）。

**NURBS曲線：** kind nurbsCurve、pieceCount、degree、pointCountとcontrolPointCount（最初のピースの値）、length（取得できない場合はnull）、bounds3D、layerElevation、pieces [{ index, degree, pointCount, controlPointCount, knotCount }]、およびピース`piece`（デフォルトは0）の`piece`、`points`（項目は{ x, y, z, weight }：ピースを定義する点、つまりその補間点または制御点。`weight`は、そのインデックスの制御点がある場合はその重み）、`knots`（すべて）。曲線の測定は、それぞれ1～100項目の配列で指定し、Vectorworksが結果を返せない位置ではnullになります：`atDistance` [0から長さまでの距離]は`pointsAtDistance` [{ distance, point, piece, parameter }]を返し、`closestTo` [3D点]は`closestPoints` [{ to, point, distance, piece, parameter }]を返し、`evaluate` [{ piece?（デフォルトは0）, parameter }]は`evaluated` [{ piece, parameter, point, tangent（単位ベクトル）, curvature（1 / ワールド単位） }]を返し、`divide` { count（2～1000）, includeEnd?（デフォルトはtrue：両端を含む） }は、曲線に沿って等間隔に並ぶcount個の点`divisionPoints`を返します（Vectorworksが等分できない場合はエラー）。パラメータはピース固有のノットパラメータ（その`knots`の範囲内）であり、円弧の長さではありません。

**NURBS曲面：** kind nurbsSurface、uPointCount、vPointCount、uDegree、vDegree、uKnotsとvKnots（すべて）、bounds3D、layerElevation、および制御点ネットをu優先の順で並べた`points`（項目iはpoints[i / vPointCount][i % vPointCount]：{ u, v, x, y, z, weight }）。`evaluate` [{ u, v }]（uKnotsとvKnotsの範囲内の1～100個のパラメータ）は`evaluated` [{ u, v, point }]を返します。`piece`、`atDistance`、`closestTo`、`divide`はNURBS曲線にのみ、`evaluate`はNURBS曲線と曲面に適用されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `limit` | integer |  | ページ分割：返す項目の最大数（1以上）。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割：スキップする項目数（デフォルトは0）。 |
| `countOnly` | boolean |  | ページ分割：項目を含めず、件数だけを返します。 |
| `piece` | integer |  | NURBS曲線で使用します。 |
| `atDistance` | array of number |  |  |
| `closestTo` | array of [3D点](Common.md#points) |  | 各項目：ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `evaluate` | array of object |  |  |
| `evaluate[].piece` | integer |  |  |
| `evaluate[].parameter` | number |  |  |
| `evaluate[].u` | number |  |  |
| `evaluate[].v` | number |  |  |
| `divide` | object |  |  |
| `divide.count` | integer | はい |  |
| `divide.includeEnd` | boolean |  |  |

### edit3DGeometry

3D 多角形、メッシュ、NURBS曲線、NURBS曲面を編集します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: edit3DGeometry" · **runToolBatch内:** はい

**詳細**

uuid、name、またはindexで3D 多角形、メッシュ、NURBS曲線、NURBS曲面を編集します。1回の呼び出しは1つの取り消しステップです（ソリッドはeditSolidで編集します）。点とbounds3DはワールドZを使用し、角度はラジアン、インデックスは0始まりです。次の場合は何も変更せずに拒否します：別の種類のオブジェクト、ロックされたオブジェクト（先にeditObjectの`locked` falseでロックを解除してください）、レイヤ・シンボル定義・それらの中のグループにないオブジェクト、その種類が受け付けない操作、操作のない呼び出し、作成操作と他の操作の併用、正しくない値。

操作は次の順序で適用されます：`vertices`（すべてを置換。多角形は2～32767個の3D点を受け付けます。メッシュは`faces`とともに指定すると頂点数を変更でき、その場合は法線とUVが消去されます。`faces`なしでは頂点数を保持）、`faces`（メッシュ：[{ vertexIndices, part? }]。面を置換）、`setVertex` { index, point }、`insertVertex` { index, point }（多角形：indexの前に挿入。index = vertexCountで末尾に追加）、`deleteVertex` { index }（多角形：少なくとも2個の頂点を保持）、`addFace` { vertexIndices, part? }、`deleteFace` { index }と`setFacePart` { index, part }（メッシュ）、`closed`（多角形）、`reverse` true（多角形）または`flipFaces` true（メッシュ）、`cleanup` { tolerance? }（多角形：重複した頂点と一直線上の頂点を除去）、`simplify`（多角形は{ maxDeviation &gt; 0 }：Douglas-Peucker法。メッシュは{ quality }：保持する詳細の割合（%）。0 &lt; quality &lt; 100。値が小さいほど多くの面を除去）、`segment` { maxSegmentLength &gt; 0 }（多角形：長い辺を細分化）、`smoothing`（メッシュ：none、documentPreference、customCrease）、`creaseAngle`（メッシュ：0～pi。スムージングをcustomCreaseに切り替え）、`addPart` { texture? }（メッシュ：テクスチャリソースの参照を持つパーツ。0はなし。そのidを`addedPart`として返す）、`setPartTexture` { part, texture }（メッシュ）、最後に多角形とメッシュの両方に対して`move3D` { offset }、`rotate3D` { center, axis, angle }（軸の周りに右手系）、`scale3D` { center, factor &gt; 0 }。

**NURBS曲線と曲面：** `setPoint`（曲線は{ piece?（デフォルトは0）, index, point }：そのピースのget3DGeometryの`points`の点。曲面は{ u, v, point }：制御点ネットの制御点）、`setWeight`（曲線は{ piece?, index, weight }で、indexは制御点のインデックス。曲面は{ u, v, weight }。weightは0.0001～100。補間点で定義された曲線のピースは重みを受け付けません）、その後`trimByCurve` { curveUuid }（曲面：NURBS曲線のコピーがそのトリム境界になり、曲線は残ります）。NURBSはmove3D、rotate3D、scale3Dを受け付けず（NURBSの3D変換はありません）、ノットは編集されません（runPythonScriptでは可能）。作成操作は、それぞれその呼び出しの唯一の操作として指定し、元のオブジェクトは変更しません：`toPlanarSolid` { thickness }（0以外。3個以上の頂点を持つ閉じた平面上の多角形）は、多角形をその法線方向に押し出した汎用ソリッドをアクティブレイヤに作成します。`repair` true（メッシュ）は、修復したメッシュを元のメッシュの直後に作成します。`extend` { distance &gt; 0, atStart?（デフォルトはfalse：終点）, linear?（デフォルトはfalse）, direction（曲面のみで必須：uまたはv） }と`offset` { distance }（0以外）は、NURBS曲線または曲面の延長コピーまたはオフセットコピーをアクティブレイヤに作成します。オブジェクト参照、`changed`（適用された操作を順に列挙）、`kind`、`vertexCount`、`closed`（多角形）または`faceCount`と`isClosed`（メッシュ）、`pieceCount`、`degree`、`pointCount`、`controlPointCount`、`length`（曲線）または`uPointCount`、`vPointCount`、`uDegree`、`vDegree`（曲面）、`bounds3D`、`layerElevation`を返します。`toPlanarSolid`は`created`（新しいソリッドの参照とgetSolidの値）を、`repair`は新しいメッシュの配列である`created`（Vectorworksが何も作成しなかった場合は空）を、`extend`と`offset`は`created`（新しい曲線または曲面の参照とこれらの値）を追加します。

> **注:** `toPlanarSolid`、`repair`、`extend`、`offset`が作成するオブジェクトには、作成オプション（`class`、`name`、`select`、`useClassAttributes`）は適用されません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `vertices` | array of [3D点](Common.md#points) |  | 各項目：ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `faces` | array of object |  | メッシュ：[{ vertexIndices, part? }]。面を置換します。面は3個以上の頂点インデックスの単純な配列でもかまいません。 |
| `faces[].vertexIndices` | array of integer | はい |  |
| `faces[].part` | integer |  |  |
| `setVertex` | object |  |  |
| `setVertex.index` | integer | はい |  |
| `setVertex.point` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `insertVertex` | object |  |  |
| `insertVertex.index` | integer | はい |  |
| `insertVertex.point` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `deleteVertex` | object |  |  |
| `deleteVertex.index` | integer | はい |  |
| `addFace` | object |  | メッシュ：{ vertexIndices, part? }、または3個以上の頂点インデックスの単純な配列。 |
| `addFace.vertexIndices` | array of integer | はい |  |
| `addFace.part` | integer |  |  |
| `deleteFace` | object |  |  |
| `deleteFace.index` | integer | はい |  |
| `setFacePart` | object |  |  |
| `setFacePart.index` | integer | はい |  |
| `setFacePart.part` | integer | はい |  |
| `closed` | boolean |  | 図形が閉じているかどうか。 |
| `reverse` | boolean |  | 多角形：trueで頂点の順序を反転します。falseは拒否されます。 |
| `flipFaces` | boolean |  | メッシュ：trueで面を反転します。falseは拒否されます。 |
| `cleanup` | object |  |  |
| `cleanup.tolerance` | number |  |  |
| `simplify` | object |  |  |
| `simplify.maxDeviation` | number |  |  |
| `simplify.quality` | number |  |  |
| `segment` | object |  |  |
| `segment.maxSegmentLength` | number | はい |  |
| `smoothing` | string |  | 次のいずれか：`none`、`documentPreference`、`customCrease`。 |
| `creaseAngle` | number |  | メッシュ：0～pi。スムージングをcustomCreaseに切り替えるため、併せて指定する`smoothing`はcustomCreaseである必要があります。 |
| `addPart` | object |  |  |
| `addPart.texture` | integer |  |  |
| `setPartTexture` | object |  |  |
| `setPartTexture.part` | integer | はい |  |
| `setPartTexture.texture` | integer | はい |  |
| `move3D` | object |  |  |
| `move3D.offset` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `rotate3D` | object |  |  |
| `rotate3D.center` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `rotate3D.axis` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `rotate3D.angle` | number | はい |  |
| `scale3D` | object |  |  |
| `scale3D.center` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `scale3D.factor` | number | はい |  |
| `setPoint` | object |  |  |
| `setPoint.piece` | integer |  |  |
| `setPoint.index` | integer |  |  |
| `setPoint.u` | integer |  |  |
| `setPoint.v` | integer |  |  |
| `setPoint.point` | [3D点](Common.md#points) | はい | ワールド単位の3D点またはベクトル{ x, y, z }。点のZはbounds3Dと同じく絶対的なワールドZで、ツールはデザインレイヤの高さを加えません。ベクトルはレイヤの高さに依存しません。 |
| `setWeight` | object |  |  |
| `setWeight.piece` | integer |  |  |
| `setWeight.index` | integer |  |  |
| `setWeight.u` | integer |  |  |
| `setWeight.v` | integer |  |  |
| `setWeight.weight` | number | はい |  |
| `trimByCurve` | object |  |  |
| `trimByCurve.curveUuid` | string | はい |  |
| `toPlanarSolid` | object |  |  |
| `toPlanarSolid.thickness` | number | はい |  |
| `repair` | boolean |  | メッシュ：trueでメッシュを修復します。falseは拒否されます。 |
| `extend` | object |  |  |
| `extend.distance` | number | はい |  |
| `extend.atStart` | boolean |  |  |
| `extend.linear` | boolean |  |  |
| `extend.direction` | string |  | 次のいずれか：`u`、`v`。 |
| `offset` | object |  |  |
| `offset.distance` | number | はい |  |

### convertTo3D

オブジェクトのコピーを3D 多角形、メッシュ、または汎用ソリッドに変換します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: convertTo3D" · **runToolBatch内:** はい

**詳細**

2Dまたは3Dオブジェクト`sourceUuid`のコピーを`to`に変換します：`polygons`（3D 多角形のグループ）、`mesh`、または`genericSolid`（履歴なし。2Dオブジェクトは拒否されるため、`polygons`または`mesh`に変換するか、押し出してください）。convertSolidはソリッドのみを受け付け、convertTo3Dはあらゆる2Dまたは3Dオブジェクトを受け付けます。元のオブジェクトは変更されず、結果はそのコンテナ内で元のオブジェクトの直後に配置されます。レイヤ、シンボル定義、それらの中のグループにない元のオブジェクトは拒否され、`genericSolid`ではロックされた元のオブジェクトも拒否されます。

省略可能な作成オプション`select`は、結果を選択するかどうかを制御します。オブジェクト参照、`kind`（group、mesh、genericSolid）、ワールドZの`bounds3D` { min, max }、ワールド単位の`layerElevation`を返します。グループでは`polygonCount`が、メッシュでは`vertexCount`、`faceCount`、`isClosed`が、汎用ソリッドではそのgetSolidの値が追加されます。createMeshの`groupUuid`で、そのようなグループからメッシュを作成できます。get3DGeometryで3D 多角形とメッシュを読み取れます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `sourceUuid` | string | はい |  |
| `to` | string | はい | 次のいずれか：`polygons`、`mesh`、`genericSolid`。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成されます。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`と併用すると、新しいオブジェクトの属性もクラスに従うように設定します。 |
