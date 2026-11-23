[English](../../PythonAPI/v2027.2/Objects3D.md) • [Deutsch](../../PythonAPI.de/v2027.2/Objects3D.md) • **日本語**

<a id="objects3d--3d-objects"></a>

# Objects3D — 3Dオブジェクト

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

3Dオブジェクトのクラス：押し出し、多段押し出し、回転体、ソリッド図形（噛み合わせるコマンド、削り取るコマンド、重なった部分を残すコマンドで作成し、モデリングの履歴を保持する図形と、履歴のない汎用ソリッド）、ソリッドプリミティブ（球、半球、円錐、...）、NURBS曲線と曲面、3D 多角形、メッシュ、シェルソリッド、サーフェスモデル。すべて[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)を継承するため、オブジェクトに共通する操作（名前、クラス、レイヤ、属性、境界、移動、削除、...）はそこで説明しています。

座標は3Dモデル空間内のワールド単位、角度はラジアンです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [ExtrudeObject](#extrudeobject)
    - [ExtrudeObject.Values](#extrudeobjectvalues)
    - [ExtrudeObject.Transform](#extrudeobjecttransform)
  - [SweepObject](#sweepobject)
    - [SweepObject.Values](#sweepobjectvalues)
  - [MultiExtrudeObject](#multiextrudeobject)
  - [SurfaceModelObject](#surfacemodelobject)
    - [SurfaceModelObject.PathOptions](#surfacemodelobjectpathoptions)
  - [GenericSolidObject](#genericsolidobject)
    - [GenericSolidObject.HistoryStep](#genericsolidobjecthistorystep)
    - [GenericSolidObject.Operation](#genericsolidobjectoperation)
  - [ShellObject](#shellobject)
  - [Polygon3DObject](#polygon3dobject)
    - [Polygon3DObject.Plane](#polygon3dobjectplane)
    - [Polygon3DObject.ClosestPoint](#polygon3dobjectclosestpoint)
  - [MeshObject](#meshobject)
    - [MeshObject.Face](#meshobjectface)
    - [MeshObject.Part](#meshobjectpart)
    - [MeshObject.Smoothing](#meshobjectsmoothing)
  - [SolidPrimitiveObject](#solidprimitiveobject)
    - [SolidPrimitiveObject.Kind](#solidprimitiveobjectkind)
  - [SphereObject](#sphereobject)
  - [HemisphereObject](#hemisphereobject)
  - [ConeObject](#coneobject)
    - [ConeObject.Radii](#coneobjectradii)
  - [NurbsCurveObject](#nurbscurveobject)
    - [NurbsCurveObject.Location](#nurbscurveobjectlocation)
  - [NurbsSurfaceObject](#nurbssurfaceobject)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`ExtrudeObject`](#extrudeobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | 標準の押し出し（プラグインオブジェクトではない）。 |
| [`ExtrudeObject.Values`](#extrudeobjectvalues) | クラス（入れ子） |  | ワールド単位での、ローカルの底面の高さと符号付きの厚さ。 |
| [`ExtrudeObject.Transform`](#extrudeobjecttransform) | クラス（入れ子） |  | 親座標系における正規直交ローカル軸と原点（デフォルトは恒等変換）。 |
| [`SweepObject`](#sweepobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | 標準の回転体。 |
| [`SweepObject.Values`](#sweepobjectvalues) | クラス（入れ子） |  | ラジアンでの回転体の角度と、一周あたりのワールド単位でのピッチ。 |
| [`MultiExtrudeObject`](#multiextrudeobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | 標準の多段押し出し。 |
| [`SurfaceModelObject`](#surfacemodelobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | モデリング結果は、NURBS曲面、CSGソリッド、またはモデリング結果のグループです。 |
| [`SurfaceModelObject.PathOptions`](#surfacemodelobjectpathoptions) | クラス（入れ子） |  | パス押し出しの拡大縮小と断面配置のオプション。 |
| [`GenericSolidObject`](#genericsolidobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | 噛み合わせるコマンド、削り取るコマンド、重なった部分を残すコマンドで作成した図形と、履歴のない汎用ソリッドを含む、標準のソリッド図形を扱います。 |
| [`GenericSolidObject.HistoryStep`](#genericsolidobjecthistorystep) | クラス（入れ子） |  | 標準の構築ツリーの一つのノードを、先行順で扱います。 |
| [`GenericSolidObject.Operation`](#genericsolidobjectoperation) | IntEnum（入れ子） |  | ソリッドのブール演算。 |
| [`ShellObject`](#shellobject) | クラス | [`GenericSolidObject`](#genericsolidobject) | シェルソリッド：CSGオフセットノード（シェルソリッドツール、VectorScriptのCreateShell）。 |
| [`Polygon3DObject`](#polygon3dobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | 標準の3D 多角形（`ObjectType.Polygon3D`）。 |
| [`Polygon3DObject.Plane`](#polygon3dobjectplane) | クラス（入れ子） |  | 頂点重心を通る平面。normalは頂点の順序（右手の法則）に従う単位ベクトルで、dが満たす式はnormal . |
| [`Polygon3DObject.ClosestPoint`](#polygon3dobjectclosestpoint) | クラス（入れ子） |  | 多角形パス上の最近点、その距離、辺のインデックス、および最初の頂点からのパス距離。 |
| [`MeshObject`](#meshobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | 標準のメッシュ（`ObjectType.Mesh`）：共有頂点リストと、そのインデックスを参照する多角形の面。 |
| [`MeshObject.Face`](#meshobjectface) | クラス（入れ子） |  | part 0は全体の（テクスチャなしの）パートを意味します。`GetOverallPart()`を参照してください。 |
| [`MeshObject.Part`](#meshobjectpart) | クラス（入れ子） |  | テクスチャパート：id、テクスチャ参照（0 = テクスチャなし）、およびそれを使用する面の数。 |
| [`MeshObject.Smoothing`](#meshobjectsmoothing) | IntEnum（入れ子） |  | レンダリング時のメッシュのスムージング方法。 |
| [`SolidPrimitiveObject`](#solidprimitiveobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | 標準のパラメトリックソリッドプリミティブ（`ObjectType.Solid`）、つまり球、半球、円錐の共通基底クラス。 |
| [`SolidPrimitiveObject.Kind`](#solidprimitiveobjectkind) | IntEnum（入れ子） |  | ソリッドプリミティブの種類。 |
| [`SphereObject`](#sphereobject) | クラス | [`SolidPrimitiveObject`](#solidprimitiveobject) | 標準の球ソリッド：中心とI/J/Kの半径（半径が不均等な場合は楕円体）。図面オブジェクトの軽量なビュー。 |
| [`HemisphereObject`](#hemisphereobject) | クラス | [`SphereObject`](#sphereobject) | 標準の半球ソリッド：中心、半径、およびローカルK軸方向を向くドーム。図面オブジェクトの軽量なビュー。 |
| [`ConeObject`](#coneobject) | クラス | [`SolidPrimitiveObject`](#solidprimitiveobject) | 標準の円錐ソリッド。 |
| [`ConeObject.Radii`](#coneobjectradii) | クラス（入れ子） |  | ローカルI軸とJ軸に沿った底面の半径。 |
| [`NurbsCurveObject`](#nurbscurveobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | 標準の区分的なNURBS曲線。 |
| [`NurbsCurveObject.Location`](#nurbscurveobjectlocation) | クラス（入れ子） |  | ゼロ始まりの区間における曲線上の点と固有のパラメータ。パラメータは弧長ではありません。 |
| [`NurbsSurfaceObject`](#nurbssurfaceobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | 標準のNURBS曲面。 |

<a id="classes"></a>

## クラス

### ExtrudeObject

> **完全修飾名:** `api.ExtrudeObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準の押し出し（プラグインオブジェクトではない）。寸法と断面座標はオブジェクト行列のローカル座標で、長さはワールド単位です。既存の押し出しを参照しても、それが変更されることはありません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ExtrudeObject(h: Handle)` | 既存の押し出し`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(hProfile: Handle, baseElevation: float, thickness: float, keepOriginal: bool = False) -> ExtrudeObject` *静的* | ハンドルで指定する断面は、標準の2D図形でなければなりません。成功すると押し出し内に移動しますが、keepOriginalが`True`の場合はコピーを使用します。失敗した場合、元の図形は変更されません。 |
| `Create(profile: Math.Polygon2D, thickness: float) -> ExtrudeObject` *静的* | ハンドルで指定する断面は、標準の2D図形でなければなりません。成功すると押し出し内に移動しますが、keepOriginalが`True`の場合はコピーを使用します。失敗した場合、元の図形は変更されません。 |
| `Create(profile: Math.Polygon2D, baseElevation: float, thickness: float) -> ExtrudeObject` *静的* | ハンドルで指定する断面は、標準の2D図形でなければなりません。成功すると押し出し内に移動しますが、keepOriginalが`True`の場合はコピーを使用します。失敗した場合、元の図形は変更されません。 |
| `Create(points: list[Math.Point2D], baseElevation: float, thickness: float, closed: bool = True) -> ExtrudeObject` *静的* | ハンドルで指定する断面は、標準の2D図形でなければなりません。成功すると押し出し内に移動しますが、keepOriginalが`True`の場合はコピーを使用します。失敗した場合、元の図形は変更されません。 |
| `Create(rect: Math.Rect2D, baseElevation: float, thickness: float) -> ExtrudeObject` *静的* | ハンドルで指定する断面は、標準の2D図形でなければなりません。成功すると押し出し内に移動しますが、keepOriginalが`True`の場合はコピーを使用します。失敗した場合、元の図形は変更されません。 |
| `CreatePlanar(points: list[Point3D], thickness: float) -> ExtrudeObject` *静的* | 閉じた平面状の3D境界。その平面によって配置が決まります。 |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, keepOriginal: bool = False) -> ExtrudeObject` *静的* | ローカルZはstart -> endに従います。オプションのupベクトルは、断面平面に投影されてローカル+Yを定義します。押し出し方向と平行であってはなりません。 |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, up: Point3D, keepOriginal: bool = False) -> ExtrudeObject` *静的* | ローカルZはstart -> endに従います。オプションのupベクトルは、断面平面に投影されてローカル+Yを定義します。押し出し方向と平行であってはなりません。 |
| `Duplicate() -> ExtrudeObject` | 図面内の押し出しを複製し、コピーを返します。 |
| `GetExtrudeValues() -> ExtrudeObject.Values \| None` | 押し出しの値を返します。 |
| `SetExtrudeValues(baseElevation: float, thickness: float) -> bool` | 押し出しの値を設定します。 |
| `SetExtrudeValues(values: ExtrudeObject.Values) -> bool` | 押し出しの値を設定します。 |
| `GetBaseElevation() -> float \| None` | 底面の高さを返します。 |
| `SetBaseElevation(baseElevation: float) -> bool` | 底面の高さを設定します（厚さは維持）。 |
| `GetThickness() -> float \| None` | 厚さを返します。 |
| `SetThickness(thickness: float) -> bool` | 厚さを設定します（底面の高さは維持）。 |
| `GetTopElevation() -> float \| None` | 上面の高さを返します。 |
| `SetTopElevation(topElevation: float) -> bool` | 上面の高さを設定します（底面の高さは維持）。 |
| `GetBaseObject() -> Handle` | 所有権を持たない断面／穴のハンドル。これらのハンドルを通じた編集には`Reset()`が必要です。 |
| `SetBaseObject(hProfile: Handle, keepOriginal: bool = False) -> bool` | 底面オブジェクトを設定します。所有権を持たない断面／穴のハンドル。これらのハンドルを通じた編集には`Reset()`が必要です。 |
| `GetBasePolygon() -> Math.Polygon2D \| None` | 底面の多角形を返します。 |
| `SetBasePolygon(profile: Math.Polygon2D) -> bool` | 底面の多角形を設定します（断面と穴の両方を置き換えます）。 |
| `GetHoleObjects() -> list[Handle]` | 穴オブジェクトを返します。 |
| `GetHoleCount() -> int` | 穴項目の数。 |
| `GetHoleObject(index: int) -> Handle` | `index`の穴オブジェクトを返します。 |
| `AddHoleObject(hProfile: Handle, keepOriginal: bool = False) -> bool` | 2Dオブジェクト`hProfile`を断面の穴として追加します（`keepOriginal`の場合はそのコピー）。所有権を持たない断面／穴のハンドル。これらのハンドルを通じた編集には`Reset()`が必要です。 |
| `AddHoleObject(profile: Math.Polygon2D) -> bool` | 形状`profile`の穴を追加します。所有権を持たない断面／穴のハンドル。これらのハンドルを通じた編集には`Reset()`が必要です。 |
| `RemoveHole(index: int) -> bool` | `index`の穴を削除します。所有権を持たない断面／穴のハンドル。これらのハンドルを通じた編集には`Reset()`が必要です。 |
| `RemoveAllHoles() -> bool` | すべての穴を削除します。所有権を持たない断面／穴のハンドル。これらのハンドルを通じた編集には`Reset()`が必要です。 |
| `GetTransform() -> ExtrudeObject.Transform \| None` | 変換を返します。 |
| `SetTransform(transform: ExtrudeObject.Transform) -> bool` | 変換を設定します（正規直交でない軸は拒否）。 |
| `Move3D(offset: Point3D) -> bool` | 押し出しを3Dで`offset`だけ移動します。 |
| `GetVolume() -> float \| None` | 体積を返します（ワールド単位の三乗）。 |

継承：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

#### ExtrudeObject.Values

> **完全修飾名:** `api.ExtrudeObject.Values` · **継承元:** `api.Object`

ワールド単位での、ローカルの底面の高さと符号付きの厚さ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Values()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Values(baseElevation, thickness)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `baseElevation` | `float` | 押し出しの底面の高さ。 |
| `thickness` | `float` | 押し出しの高さ。 |

#### ExtrudeObject.Transform

> **完全修飾名:** `api.ExtrudeObject.Transform` · **継承元:** `api.Object`

親座標系における正規直交ローカル軸と原点（デフォルトは恒等変換）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Transform()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Transform(origin, uAxis, vAxis, wAxis)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `origin` | `Point3D` | ローカルフレームの原点。 |
| `uAxis` | `Point3D` | ローカルX軸。 |
| `vAxis` | `Point3D` | ローカルY軸。 |
| `wAxis` | `Point3D` | ローカルZ軸（押し出し方向）。 |

### SweepObject

> **完全修飾名:** `api.SweepObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準の回転体。断面のXは半径方向、Yは軸方向で、回転体の軸はローカルYです。角度ゼロで半径方向はローカル+Zとなり、正の角度ではローカル+Xに向かって回転します。角度はラジアン、ピッチは一周あたりのワールド単位です。入力は常にコピーされます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `SweepObject(h: Handle)` | 既存の回転体`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(profile: Handle) -> SweepObject` *静的* | 2Dオブジェクト`profile`から、デフォルトの回転体の値で回転体を作成します。 |
| `Create(profile: Handle, values: SweepObject.Values) -> SweepObject` *静的* | 2Dオブジェクト`profile`から、回転体の値`values`で回転体を作成します。 |
| `Create(profiles: list[Handle], values: SweepObject.Values) -> SweepObject` *静的* | オプションの2D 基準点で軸を指定します。指定しない場合、Vectorworksは断面の左端を使用します。 |
| `AreValidValues(values: SweepObject.Values) -> bool` *静的* | `values`が`Create`に対して有効な回転体の値である場合はTrue。 |
| `Duplicate() -> SweepObject` | 図面内の回転体を複製し、コピーを返します。 |
| `GetSweepValues() -> SweepObject.Values \| None` | 回転体の値を返します。 |
| `SetSweepValues(values: SweepObject.Values) -> bool` | 回転体の値を設定します。 |
| `GetProfiles() -> list[Handle]` | 断面を返します。 |

継承：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

#### SweepObject.Values

> **完全修飾名:** `api.SweepObject.Values` · **継承元:** `api.Object`

ラジアンでの回転体の角度と、一周あたりのワールド単位でのピッチ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Values()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Values(startAngle, sweepAngle, incrementAngle, pitch)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `startAngle` | `float` | 回転体の開始角（ラジアン）。 |
| `sweepAngle` | `float` | 回転する角度（ラジアン、デフォルトは一周。符号が方向を示します）。 |
| `incrementAngle` | `float` | 正の大きさ。sweepAngleの符号が方向を決定します。 |
| `pitch` | `float` | 正の大きさ。sweepAngleの符号が方向を決定します。 |

### MultiExtrudeObject

> **完全修飾名:** `api.MultiExtrudeObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準の多段押し出し。断面はセクション順にコピーされ、baseElevationからbaseElevation + thicknessまでの間に等間隔で配置されます。少なくとも二つの標準の2D断面が必要です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `MultiExtrudeObject(h: Handle)` | 既存の多段押し出し`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(profiles: list[Handle], baseElevation: float, thickness: float) -> MultiExtrudeObject` *静的* | 2Dの`profiles`（ハンドルのリスト）から、高さ`baseElevation`、厚さ`thickness`の多段押し出しを作成します。 |
| `Duplicate() -> MultiExtrudeObject` | 図面内の多段押し出しを複製し、コピーを返します。 |
| `GetExtrudeValues() -> ExtrudeObject.Values \| None` | 押し出しの値を返します。 |
| `SetExtrudeValues(baseElevation: float, thickness: float) -> bool` | 押し出しの値を設定します。 |
| `GetProfiles() -> list[Handle]` | 断面を返します。 |

継承：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

### SurfaceModelObject

> **完全修飾名:** `api.SurfaceModelObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

モデリング結果は、NURBS曲面、CSGソリッド、またはモデリング結果のグループです。これは結果の形状の判定であり、永続的なフィーチャー／由来の種類ではありません。ファクトリはすべての入力オブジェクトを保持し、現在のコンテナに一つの結果を配置します。座標と長さはワールド単位、すべての角度はラジアンです。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `SurfaceModelObject(h: Handle)` | 既存のサーフェスモデル`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `CreateLoft(sections: list[Handle], ruled: bool = False, closed: bool = False, solid: bool = False) -> SurfaceModelObject` *静的* | 順序付けられたNURBS曲線または3D 基準点。閉じた多段曲面には少なくとも三つのセクションが必要です。solidは端面キャップと縫合を要求します。縫合に失敗した場合は失敗を報告し、グループとして返すことはありません。 |
| `CreateRailSweep(sections: list[Handle], rail: Handle, secondRail: Handle = None, solid: bool = False) -> SurfaceModelObject` *静的* | 一本または二本のNURBSレール。セクションは、レールに沿った順序のNURBS曲線です。 |
| `CreateRevolve(profile: Handle, values: SweepObject.Values = SweepObject.Values()) -> SurfaceModelObject` *静的* | 標準の回転体の断面／軸の規約を使用し、その後、結果をNURBSに変換します。 |
| `CreateRevolveWithRail(profile: Handle, rail: Handle, axis: Handle) -> SurfaceModelObject` *静的* | 軸は直線の曲線でなければなりません。Vectorworksは交差と断面／レールの適合性を検証します。 |
| `CreateExtrudeAlongPath(path: Handle, profile: Handle) -> SurfaceModelObject` *静的* | パスはNURBS曲線でなければなりません。結果は、履歴のないCSGソリッド／シートです。 |
| `CreateExtrudeAlongPath(path: Handle, profile: Handle, options: SurfaceModelObject.PathOptions) -> SurfaceModelObject` *静的* | パスはNURBS曲線でなければなりません。結果は、履歴のないCSGソリッド／シートです。 |
| `CreateTaperedExtrude(profile: Handle, angle: float, height: float) -> SurfaceModelObject` *静的* | 2Dの`profile`から、テーパ角`angle`、高さ`height`のテーパ押し出しを作成します。 |
| `CreateCylinder(baseCenter: Point3D, radius: float, height: float) -> ExtrudeObject` *静的* | 底面の中心`baseCenter`、半径`radius`、高さ`height`の円筒（円の押し出し）を作成します。 |
| `CreateBox(minimum: Point3D, maximum: Point3D) -> ExtrudeObject` *静的* | コーナー`minimum`からコーナー`maximum`までの、座標軸に平行な直方体（四角形の押し出し）を作成します。 |
| `CreateTorus(center: Point3D, majorRadius: float, minorRadius: float) -> SweepObject` *静的* | ワールドZを軸とするリングトーラス。majorRadius > minorRadius > 0。 |
| `Duplicate() -> SurfaceModelObject` | 図面内のサーフェスモデルを複製し、コピーを返します。 |

継承：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

#### SurfaceModelObject.PathOptions

> **完全修飾名:** `api.SurfaceModelObject.PathOptions` · **継承元:** `api.Object`

パス押し出しの拡大縮小と断面配置のオプション。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `PathOptions()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `PathOptions(isExponentialScale, scale, isProfilePlaneLocked, isProfileFixed)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `isExponentialScale` | `bool` | パスに沿って断面を線形ではなく指数的に拡大縮小します。 |
| `scale` | `float` | パスの終点における断面の拡大縮小率。 |
| `isProfilePlaneLocked` | `bool` | パスに沿って移動する間、断面平面をロックしたままにします。 |
| `isProfileFixed` | `bool` | 断面を固定したままにします（パスに沿って回転しない）。 |

### GenericSolidObject

> **完全修飾名:** `api.GenericSolidObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

噛み合わせるコマンド、削り取るコマンド、重なった部分を残すコマンドで作成した図形と、履歴のない汎用ソリッドを含む、標準のソリッド図形を扱います。人工的な履歴は保存せず、ファイルの実際のオペランドツリーを使用します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `GenericSolidObject(h: Handle)` | 既存の汎用ソリッド`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `IsGenericSolid(h: Handle) -> bool` *静的* | `h`が汎用ソリッド（CSGソリッド）の場合はTrue。 |
| `Create(hSolid: Handle, keepOriginal: bool = True) -> GenericSolidObject` *静的* | 既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreateBoolean(operation: GenericSolidObject.Operation, hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *静的* | ソリッドのブール演算`operation`を`hBlank`と`hTool`に適用した結果を作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreateUnion(hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *静的* | `hBlank`と`hTool`の和集合を作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreateIntersection(hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *静的* | `hBlank`と`hTool`の共通部分を作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreateDifference(hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *静的* | `hBlank`から`hTool`を引いた差分を作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreateFromExtrude(hProfile: Handle, baseElevation: float, thickness: float, keepOriginal: bool = True) -> GenericSolidObject` *静的* | 2Dオブジェクト`hProfile`を`baseElevation`から`thickness`だけ押し出してソリッドを作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreateFromExtrude(profile: Math.Polygon2D, baseElevation: float, thickness: float) -> GenericSolidObject` *静的* | 多角形`profile`を`baseElevation`から`thickness`だけ押し出してソリッドを作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreateFromExtrude(rect: Math.Rect2D, baseElevation: float, thickness: float) -> GenericSolidObject` *静的* | 四角形`rect`を`baseElevation`から`thickness`だけ押し出してソリッドを作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreateFromExtrude(points: list[Math.Point2D], baseElevation: float, thickness: float, closed: bool = True) -> GenericSolidObject` *静的* | `points`を通る多角形を`baseElevation`から`thickness`だけ押し出してソリッドを作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreatePlanar(points: list[Point3D], thickness: float) -> GenericSolidObject` *静的* | 平面状の3D 多角形`points`から、厚さ`thickness`のソリッドを作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, keepOriginal: bool = True) -> GenericSolidObject` *静的* | 断面`hProfile`を`start`から`end`まで押し出してソリッドを作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, up: Point3D, keepOriginal: bool = True) -> GenericSolidObject` *静的* | 断面`hProfile`を`start`から`end`まで押し出し、`up`で断面の向きを決めてソリッドを作成します。既存のCSGソリッドはそのまま使用するか、複製します。他のソリッドプリミティブは、プリミティブを保持した単一オペランドの和集合になります。成功時、keepOriginal=`False`では入力を履歴内に移動します。失敗時、入力は変更されません。作成結果は入力のコンテナに残りますが、二入力のブール演算結果はアクティブコンテナに挿入されます。 |
| `CanConvertToGenericSolid(h: Handle) -> bool` *静的* | ConvertToGenericSolidが受け付けるオブジェクトの場合は`True`。対象はCSGソリッド（シェルを含む）、押し出し、回転体、メッシュ、ソリッドプリミティブ（球、半球、円錐、...）、少なくとも三つの頂点を持つ閉じた3D 多角形、およびその他の有効なCSGプリミティブ（壁、スラブ、NURBS、シンボル、...）です。 |

*VectorScriptのConvertToGenericSolidと同様*

| メソッド | 説明 |
|---|---|
| `ConvertToGenericSolid(hObject: Handle, keepOriginal: bool = True) -> GenericSolidObject` *静的* | 履歴のない汎用ソリッドを構築します。標準の変換機能が直接受け付けない種類は、まず単一オペランドの和集合にします。結果は元のオブジェクトの隣に配置されます。keepOriginal=`False`の場合、成功時に元のオブジェクトを削除します（別のソリッドの履歴内に入れ子になっているオペランドには使用しないでください）。結果に対してこの処理を逆に戻すことはできません。 |
| `Duplicate() -> GenericSolidObject` | 図面内の汎用ソリッドを複製し、コピーを返します。 |
| `GetAction() -> int \| None` | アクションを返します。 |
| `GetOperation() -> GenericSolidObject.Operation \| None` | 演算を返します。 |
| `HasHistory() -> bool \| None` | ソリッドがモデリング履歴を保持している場合はTrue。 |
| `SetOperation(operation: GenericSolidObject.Operation) -> bool` | 演算を設定します。 |
| `GetOperands() -> list[Handle]` | オペランドを返します。 |
| `GetOperandCount() -> int` | オペランド項目の数。 |
| `GetOperand(index: int) -> Handle` | `index`のオペランドを返します。 |
| `SetOperand(index: int, hSolid: Handle) -> bool` | 指定したソリッドを、元のオペランド座標でこのスロットにコピーします。編集できるのはブール演算ノードのみです。置き換えられたオペランドのハンドルは、成功した場合にのみ無効になります。 |
| `GetHistory() -> list[GenericSolidObject.HistoryStep]` | 履歴を返します。 |
| `Rebuild() -> bool` | 継承した`Reset()`とは異なり、履歴のハンドルを編集した後に標準のCSGキャッシュを再構築します。編集をまとめて実行した後、最も外側のソリッドを再構築してください。`False`の場合も編集はそのまま残ります。 |

*不可逆*

| メソッド | 説明 |
|---|---|
| `ClearHistory() -> bool` | すべてのオペランドとフィーチャーデータを削除し、それらのハンドルを無効にします。 |
| `GetTransform() -> ExtrudeObject.Transform \| None` | 変換を返します。 |
| `SetTransform(transform: ExtrudeObject.Transform) -> bool` | 変換を設定します。 |
| `GetScale() -> Point3D \| None` | 縮尺を返します。 |
| `SetScale(scale: Point3D) -> bool` | 縮尺を設定します。 |
| `Move3D(offset: Point3D) -> bool` | ソリッドを3Dで`offset`だけ移動します。 |
| `GetVolume() -> float \| None` | 体積を返します。 |
| `GetSurfaceArea() -> float \| None` | 表面積を返します。 |
| `ConvertToMesh(keepOriginal: bool = True) -> MeshObject` | ソリッドをテセレーションしてメッシュを作成し、その直後に配置します。keepOriginalが`True`でない限り、ソリッドを削除します。別のソリッドの履歴内に入れ子になっているソリッドでは、keepOriginal = `True`が必要です。 |

継承：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

#### GenericSolidObject.HistoryStep

> **完全修飾名:** `api.GenericSolidObject.HistoryStep` · **継承元:** `api.Object`

標準の構築ツリーの一つのノードを、先行順で扱います。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `HistoryStep()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `HistoryStep(object, parent, operandIndex, depth, action, operation, hasHistory)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `object` | `Handle` | このステップのオブジェクトのハンドル。 |
| `parent` | `Handle` | 親ステップのハンドル。 |
| `operandIndex` | `int` | 親の中でのオペランドのインデックス。 |
| `depth` | `int` | 履歴ツリー内でのステップの深さ。 |
| `action` | `int` | ステップの未加工のアクションコード（存在しない場合は-1）。 |
| `operation` | `GenericSolidObject.Operation \| None` | ステップのソリッド演算。ブール演算でない場合は`None`。 |
| `hasHistory` | `bool` | ステップが独自の履歴を持つかどうか。 |

#### GenericSolidObject.Operation

> **完全修飾名:** `api.GenericSolidObject.Operation` · **種類:** `IntEnum`

ソリッドのブール演算。

| メンバー | 値 | 説明 |
|---|---|---|
| `Union` | `0` |  |
| `Intersection` | `1` |  |
| `Difference` | `2` |  |

### ShellObject

> **完全修飾名:** `api.ShellObject` · **継承元:** [`GenericSolidObject`](#genericsolidobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

シェルソリッド：CSGオフセットノード（シェルソリッドツール、VectorScriptのCreateShell）。オペランドはちょうど一つ（元の曲面またはソリッド）で、厚さと選択した面を履歴として保持します。NURBS曲面には厚みを付け、ソリッドは選択した面を除去して中空にします（開いた面）。保存される厚さは符号付きで、負の値は反対側にオフセットします（オブジェクト情報パレットの「オフセット側」）。継承したブール演算の編集（SetOperation / SetOperand）はシェルノードには適用されません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ShellObject(h: Handle)` | 既存のシェルソリッド`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | オフセットアクションを持つCSGノード。直前の再構築に失敗したノードも含みます。 |
| `Create(hSurface: Handle, thickness: float, keepOriginal: bool = True) -> ShellObject` *静的* | `thickness`は有限かつゼロ以外でなければなりません。負の値は反対側に厚みを付けます。結果は元のオブジェクトの位置に挿入され、元のオブジェクトはシェルのオペランドになります。keepOriginalの場合は、代わりに元のオブジェクトのコピーを使用します。失敗時、入力は変更されません。シェルと元のオブジェクトのコピーを取り消し用に記録し、既存のイベントに参加します。返されたシェルを再度登録しないでください。元のオブジェクトが新規作成されたものである場合は、この呼び出しの前に登録する必要があります。 |
| `CreateFromSolid(hSolid: Handle, openFaceIndices: list[int], thickness: float, keepOriginal: bool = True) -> ShellObject` *静的* | ソリッドを中空にします。`openFaceIndices`は、シェルから除去する面の0始まりのインデックスです（GetFaceCountを参照）。 |
| `GetFaceCount(h: Handle) -> int \| None` *静的* | CreateFromSolidで指定可能な面の数。 |
| `Duplicate() -> ShellObject` | 図面内のシェルソリッドを複製し、コピーを返します。 |
| `IsFailed() -> bool \| None` | シェルを構築できなかった場合はTrue。 |
| `GetThickness() -> float \| None` | 厚さの大きさ。どちら側かはIsReversedが返します。 |
| `SetThickness(thickness: float) -> bool` | 側を維持した正の大きさ。再構築に失敗した場合は以前の値に戻します。 |
| `IsReversed() -> bool \| None` | 曲面の反対側にシェルが構築されている場合はTrue。 |
| `SetReversed(isReversed: bool) -> bool` | *反転*をオンまたはオフにします。 |
| `GetSource() -> Handle` | 厚みを付けた曲面、または中空にしたソリッド（唯一のオペランド）。 |
| `IsMonikerBased() -> bool \| None` | 元のオブジェクトが対応している場合、面は永続的なモニカーで追跡されます。それ以外はインデックスで追跡されます。 |
| `GetSelectedFaceIndices() -> list[int]` | 選択した面のインデックスを返します。 |
| `GetSelectedFaceMonikers() -> list[str]` | 選択した面のモニカーを返します。 |
| `ResolveSelectedFaceIndices() -> list[int] \| None` | モニカーとして保存した選択を含む、現在の元の面の0始まりのインデックス。ソート済みで重複はありません。元のオブジェクトを読み取れない場合、またはいずれかの選択した面を解決できなくなった場合は取得できません。 |

継承：[`GenericSolidObject`](#genericsolidobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

### Polygon3DObject

> **完全修飾名:** `api.Polygon3DObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準の3D 多角形（`ObjectType.Polygon3D`）。頂点は親座標系のコーナー点（ワールド単位）です。3D 多角形には円弧／ベジェ頂点も、辺ごとの表示状態もありません。インデックスは0始まりです。3D 多角形は常に少なくとも二つの頂点を維持します。既存の多角形を参照しても、それが変更されることはありません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Polygon3DObject(h: Handle)` | 既存の3D 多角形`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(points: list[Point3D], closed: bool = True) -> Polygon3DObject` *静的* | 2..32767個の有限な点が必要です。新しい多角形はアクティブレイヤに挿入されます。 |

*コーナー点のみ*

| メソッド | 説明 |
|---|---|
| `Create(polygon: Math.Polygon2D, z: float = 0.0) -> Polygon3DObject` *静的* | 2D多角形の円弧／ベジェ頂点のデータは無視されます。 |
| `Create(rect: Math.Rect2D, z: float = 0.0) -> Polygon3DObject` *静的* | 2D多角形の円弧／ベジェ頂点のデータは無視されます。 |
| `ConvertToGroup(hObject: Handle, keepOriginal: bool = True) -> Handle` *静的* | 任意の2D/3Dオブジェクトを3D 多角形に変換します（ConvertTo3DPolygons）。多角形を格納するグループ、またはnullを返します。keepOriginalが`True`でない限り、元のオブジェクトを削除します。 |
| `GetPolygonsIn(hContainer: Handle) -> list[Handle]` *静的* | コンテナ（グループ、レイヤ、シンボル、...）内の3D 多角形。入れ子のグループ内のものも含みます。 |
| `Duplicate() -> Polygon3DObject` | 図面内の3D 多角形を複製し、コピーを返します。 |

*頂点*

| メソッド | 説明 |
|---|---|
| `GetVertexCount() -> int` | 頂点項目の数。 |
| `GetVertex(index: int) -> Point3D \| None` | `index`の頂点を返します。 |
| `SetVertex(index: int, point: Point3D) -> bool` | `index`の頂点を設定します。 |
| `GetVertices() -> list[Point3D]` | 頂点を返します。 |
| `SetVertices(points: list[Point3D]) -> bool` | 頂点を設定します（2..32767点）。 |
| `AddVertex(point: Point3D) -> bool` | 頂点`point`を追加します。 |
| `AddVertices(points: list[Point3D], reverse: bool = False) -> bool` | 頂点`points`を追加します（`reverse`が`True`の場合は逆順）。 |
| `InsertVertex(beforeIndex: int, point: Point3D) -> bool` | `point`を頂点`beforeIndex`の前に挿入します（0 .. 頂点数）。 |
| `DeleteVertex(index: int) -> bool` | `index`の頂点を削除します。残りの頂点が二つしかない場合は失敗します。 |
| `IsClosed() -> bool` | 多角形が閉じている場合はTrue。 |
| `SetClosed(closed: bool) -> bool` | *閉じる*をオンまたはオフにします。 |

*形状*

| メソッド | 説明 |
|---|---|
| `GetPolygon2D() -> Math.Polygon2D \| None` | 2D多角形を返します（XY投影、閉じるフラグは維持）。 |
| `IsClockwise() -> bool \| None` | XY投影が時計回りの場合はTrue（Newell法線のzの符号）。 |
| `Reverse() -> bool` | 頂点の順序を逆にします（多角形の法線を反転）。 |
| `IsPlanar(tolerance: float = 1e-09) -> bool \| None` | すべての頂点が`tolerance`以内で一つの平面上にある場合はTrue。 |
| `IsValidPolygon(tolerance: float = 1e-09) -> bool \| None` | 多角形が有効となるのに十分な、互いに異なる頂点を持つ場合はTrue（`tolerance`以内で判定）。 |
| `GetNormal() -> Point3D \| None` | 法線を返します（単位長さのNewell法線）。 |
| `GetPlane() -> Polygon3DObject.Plane \| None` | 平面を返します。 |
| `GetPlaneTransform() -> ExtrudeObject.Transform \| None` | 平面の変換を返します（Wが多角形の法線に沿うローカルフレーム）。 |
| `GetVertexCentroid() -> Point3D \| None` | 測定値（ワールド単位）。3D境界、中心（Get3DCntr）、サイズ（Get3DInfo）はPrimitiveObjectで取得します（頂点の平均）。 |
| `GetLength() -> float \| None` | 長さを返します（閉じている場合は閉じる辺を含む）。 |
| `GetSegmentLength(segmentIndex: int) -> float \| None` | `segmentIndex`のセグメントの長さを返します。 |
| `GetArea() -> float \| None` | 面積を返します（閉じた多角形の平面面積（Newell））。 |
| `GetPointAtDistance(distance: float) -> Point3D \| None` | 距離`distance`にある点を返します（パスに沿った距離）。 |
| `GetClosestPoint(point: Point3D) -> Polygon3DObject.ClosestPoint \| None` | `point`に最も近い点を返します。 |
| `GetDistanceTo(point: Point3D) -> float \| None` | `point`までの距離を返します。 |
| `GetDistanceToPlane(point: Point3D) -> float \| None` | `point`の平面までの距離を返します（符号付き）。 |
| `IntersectLine(start: Point3D, direction: Point3D) -> Point3D \| None` | `start`を通り`direction`に沿う直線と、多角形の平面との交点。 |

*編集*

| メソッド | 説明 |
|---|---|
| `Cleanup(tolerance: float = 1e-09) -> bool` | 重複頂点と同一直線上の頂点を削除します（`tolerance`以内）。 |
| `CleanupFeaturePreserving(collinearTolerance: float, closenessTolerance: float) -> bool` | 形状を維持しながら、同一直線上の頂点（`collinearTolerance`）と、ほぼ一致する頂点（`closenessTolerance`）を削除します。 |
| `Simplify(maxDeviation: float) -> bool` | Douglas-Peuckerアルゴリズムで多角形を単純化します。偏差は最大で`maxDeviation`です。 |
| `Segment(maxSegmentLength: float) -> bool` | `maxSegmentLength`より長い辺を細分割します。 |
| `Transform(transform: ExtrudeObject.Transform) -> bool` | `transform`で多角形を変換します（ローカル座標を親空間に写します）。 |
| `Move3D(offset: Point3D) -> bool` | 多角形を3Dで`offset`だけ移動します。 |
| `Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool` | 多角形を`angleDegrees`（度）だけ、軸`axis`（`center`を通る）を中心に回転します。 |
| `Scale3D(center: Point3D, factors: Point3D) -> bool` | 多角形を`factors`（軸ごと）で、`center`を基準に拡大縮小します。 |

*汎用ソリッドとの連携*

| メソッド | 説明 |
|---|---|
| `IsValidSolidOperand() -> bool` | 少なくとも三つの頂点を持つ閉じた多角形のみが有効なオペランドです。keepOriginal = `False`の場合、この多角形を新しいソリッドの履歴内に移動します。 |
| `ToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | 多角形を汎用ソリッドに変換します。少なくとも三つの頂点を持つ閉じた多角形のみが有効なオペランドです。keepOriginal = `False`の場合、この多角形を新しいソリッドの履歴内に移動します。 |
| `Union(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | ソリッド`hTool`との和集合を汎用ソリッドとして返します。少なくとも三つの頂点を持つ閉じた多角形のみが有効なオペランドです。keepOriginal = `False`の場合、この多角形を新しいソリッドの履歴内に移動します。 |
| `Subtract(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | ソリッド`hTool`を差し引いた差分を汎用ソリッドとして返します。少なくとも三つの頂点を持つ閉じた多角形のみが有効なオペランドです。keepOriginal = `False`の場合、この多角形を新しいソリッドの履歴内に移動します。 |
| `Intersect(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | ソリッド`hTool`との共通部分を汎用ソリッドとして返します。少なくとも三つの頂点を持つ閉じた多角形のみが有効なオペランドです。keepOriginal = `False`の場合、この多角形を新しいソリッドの履歴内に移動します。 |
| `ConvertToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | 履歴のない汎用ソリッド（ConvertToGenericSolidと同様）。keepOriginal = `False`の場合、この多角形を削除します。 |
| `ToPlanarSolid(thickness: float) -> GenericSolidObject` | 多角形の頂点を面とし、その法線に沿ってthicknessだけ押し出した平面状のソリッド。 |

継承：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

#### Polygon3DObject.Plane

> **完全修飾名:** `api.Polygon3DObject.Plane` · **継承元:** `api.Object`

頂点重心を通る平面。normalは頂点の順序（右手の法則）に従う単位ベクトルで、dは平面上の点pに対してnormal . p + d = 0を満たします。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Plane()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Plane(point, normal, d)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `point` | `Point3D` | 頂点重心（平面上の一点）。 |
| `normal` | `Point3D` | 頂点の順序（右手の法則）に従う単位法線。 |
| `d` | `float` | 平面定数：`normal . p + d = 0`を平面上の点`p`に対して満たします。 |

#### Polygon3DObject.ClosestPoint

> **完全修飾名:** `api.Polygon3DObject.ClosestPoint` · **継承元:** `api.Object`

多角形パス上の最近点、その距離、辺のインデックス、および最初の頂点からのパス距離。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ClosestPoint()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ClosestPoint(point, distance, segmentIndex, distanceAlong)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `point` | `Point3D` | 最近点。 |
| `distance` | `float` | 最近点までの距離。 |
| `segmentIndex` | `int` | 頂点segmentIndexから次の頂点への辺。 |
| `distanceAlong` | `float` | 最初の頂点からpointまでのパス長。 |

### MeshObject

> **完全修飾名:** `api.MeshObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準のメッシュ（`ObjectType.Mesh`）：共有頂点リストと、そのインデックスを参照する多角形の面。頂点と面のインデックスは0始まりです。オプションとして、頂点ごとの法線とUV座標、およびテクスチャパート（独自のテクスチャを持つ面のグループ）をサポートします。メッシュは汎用ソリッドの有効なオペランドです。ToGenericSolid/Union/Subtract/Intersectはメッシュからソリッドを構築し、`GenericSolidObject.ConvertToMesh`はソリッドをメッシュに戻します。面リストの書き換え（SetFaces、SetGeometry、DeleteFace、FlipFaces）では、面のパートは維持しますが、面ごとの属性（クラス、面、線）はメッシュのデフォルトにリセットします。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `MeshObject(h: Handle)` | 既存のメッシュ`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `GetOverallPart() -> int` *静的* | 全体のパートを返します。 |
| `Create(vertices: list[Point3D], faces: list[list[int]]) -> MeshObject` *静的* | 面には少なくとも三つの有効な頂点インデックスが必要です。メッシュはアクティブレイヤに挿入されます。 |
| `Create(vertices: list[Point3D], faces: list[MeshObject.Face]) -> MeshObject` *静的* | 面には少なくとも三つの有効な頂点インデックスが必要です。メッシュはアクティブレイヤに挿入されます。 |
| `CreateFromPolygons(polygons: list[list[Point3D]]) -> MeshObject` *静的* | 各多角形が一つの面になります。一致する点は結合して共有頂点にします。 |
| `CreateFromGroup(hGroup: Handle) -> MeshObject` *静的* | 3D 多角形のグループをその場で変換します（入れ子のグループは先に平坦化）。グループのハンドルがメッシュのハンドルになります。グループに他のオブジェクトが含まれる場合、変更せずに失敗します。 |
| `CreateFromObject(hObject: Handle, keepOriginal: bool = True) -> MeshObject` *静的* | 任意の3Dオブジェクト（ソリッド、押し出し、汎用ソリッド、...）を、3D 多角形を介してメッシュにします。メッシュは元のオブジェクトの直後に配置され、keepOriginalが`True`でない限り、元のオブジェクトを削除します。汎用ソリッドの履歴内にあるオペランドは、keepOriginal = `True`の場合にのみ変換できます。 |
| `GetMeshesIn(hContainer: Handle) -> list[Handle]` *静的* | コンテナ（グループ、レイヤ、シンボル、...）の直接のメンバーであるメッシュ。 |
| `GetMeshOperands(hSolid: Handle) -> list[Handle]` *静的* | 汎用ソリッドの履歴内の任意の場所で使用されているメッシュ。 |
| `Duplicate() -> MeshObject` | 図面内のメッシュを複製し、コピーを返します。 |

*頂点*

| メソッド | 説明 |
|---|---|
| `GetVertexCount() -> int` | 頂点項目の数。 |
| `GetVertex(index: int) -> Point3D \| None` | `index`の頂点を返します。 |
| `SetVertex(index: int, point: Point3D) -> bool` | `index`の頂点を設定します。 |
| `GetVertices() -> list[Point3D]` | 頂点を返します。 |
| `SetVertices(points: list[Point3D]) -> bool` | 頂点を設定します（頂点数は同じ）。 |
| `HasNormals() -> bool` | 頂点ごとの法線とUV座標（頂点あたり一つのエントリ）。 |
| `GetNormals() -> list[Point3D]` | 法線を返します（頂点ごとの法線とUV座標（頂点あたり一つのエントリ））。 |
| `SetNormals(normals: list[Point3D]) -> bool` | 法線を設定します（頂点ごとの法線とUV座標（頂点あたり一つのエントリ）。書き込み時に正規化）。 |
| `ClearNormals() -> bool` | 頂点ごとの法線を削除します。 |
| `HasUVs() -> bool` | メッシュが頂点ごとのUV座標を持つ場合はTrue。 |
| `GetUVs() -> list[Math.Point2D]` | UV座標を返します。 |
| `SetUVs(uvs: list[Math.Point2D]) -> bool` | UV座標を設定します。 |
| `ClearUVs() -> bool` | 頂点ごとのUV座標を削除します（すべての面を全体のパートにリセットする処理も行います）。 |

*面*

| メソッド | 説明 |
|---|---|
| `GetFaceCount() -> int` | 面項目の数。 |
| `GetFace(index: int) -> MeshObject.Face \| None` | `index`の面を返します。 |
| `GetFaces() -> list[MeshObject.Face]` | 面を返します。 |
| `SetFaces(faces: list[MeshObject.Face]) -> bool` | 面を設定します。 |
| `AddFace(vertexIndices: list[int], part: int = 0) -> bool` | 頂点`vertexIndices`を通る面を、テクスチャパート`part`に追加します（面の属性は維持）。 |
| `DeleteFace(index: int) -> bool` | `index`の面を削除します。 |
| `SetGeometry(vertices: list[Point3D], faces: list[MeshObject.Face]) -> bool` | 頂点と面を同時に置き換えます（頂点数は変わってもかまいません）。頂点数が変わる場合、法線とUV座標はクリアされます。 |
| `SetFacePart(faceIndex: int, part: int) -> bool` | `faceIndex`の面のパートを設定します。 |
| `GetFaceNormal(faceIndex: int) -> Point3D \| None` | `faceIndex`の面の法線を返します（単位長さのNewell法線）。 |
| `GetFaceArea(faceIndex: int) -> float \| None` | `faceIndex`の面積を返します。 |
| `GetFaceCenter(faceIndex: int) -> Point3D \| None` | `faceIndex`の面の中心を返します（面の頂点の平均）。 |

*テクスチャパート*

| メソッド | 説明 |
|---|---|
| `GetParts() -> list[MeshObject.Part]` | パートを返します。 |
| `AddPart(texture: int = 0) -> int \| None` | テクスチャパートを追加し（テクスチャインデックス`texture`、0 = なし）、新しいパートのインデックスを返します。 |
| `GetPartTexture(part: int) -> int \| None` | `part`のパートテクスチャを返します。 |
| `SetPartTexture(part: int, texture: int) -> bool` | パートテクスチャを設定します。 |

*スムージング*

| メソッド | 説明 |
|---|---|
| `GetSmoothing() -> MeshObject.Smoothing \| None` | スムージングを返します。 |
| `SetSmoothing(smoothing: MeshObject.Smoothing) -> bool` | スムージングを設定します。 |
| `GetCreaseAngle() -> float \| None` | 折り目角度を返します。 |
| `SetCreaseAngle(degrees: float) -> bool` | 折り目角度を設定します（0..180、CustomCreaseに切り替えます）。 |

*トポロジ*

| メソッド | 説明 |
|---|---|
| `IsClosed() -> bool` | メッシュが閉じている場合はTrue（水密：各辺は互いに逆向きの二つの面で共有される）。 |
| `FlipFaces() -> bool` | 面の頂点の巡回方向と頂点法線を反転します。 |

*操作*

| メソッド | 説明 |
|---|---|
| `Simplify(qualityPercent: float) -> bool` | メッシュ自体を、細部が`qualityPercent`パーセントになるまで単純化します（0 < quality < 100）。 |
| `Repair() -> list[Handle]` | 修復したメッシュはこのメッシュの後に挿入します。このメッシュは変更されません。 |
| `ConvertToGroup() -> Handle` | このメッシュをその場で3D 多角形のグループに変換します。このオブジェクトは無効になります。 |
| `ToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | 汎用ソリッドとの連携。keepOriginal = `False`の場合、このメッシュを新しいソリッドの履歴内に移動するため、その後オブジェクトは履歴のオペランドを参照します。 |
| `Union(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | ソリッド`hTool`との和集合を汎用ソリッドとして返します。汎用ソリッドとの連携。keepOriginal = `False`の場合、このメッシュを新しいソリッドの履歴内に移動するため、その後オブジェクトは履歴のオペランドを参照します。 |
| `Subtract(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | ソリッド`hTool`を差し引いた差分を汎用ソリッドとして返します。汎用ソリッドとの連携。keepOriginal = `False`の場合、このメッシュを新しいソリッドの履歴内に移動するため、その後オブジェクトは履歴のオペランドを参照します。 |
| `Intersect(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | ソリッド`hTool`との共通部分を汎用ソリッドとして返します。汎用ソリッドとの連携。keepOriginal = `False`の場合、このメッシュを新しいソリッドの履歴内に移動するため、その後オブジェクトは履歴のオペランドを参照します。 |
| `ConvertToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | 履歴のない汎用ソリッド（ConvertToGenericSolidと同様）。keepOriginal = `False`の場合、このメッシュを削除します。 |
| `Transform(transform: ExtrudeObject.Transform) -> bool` | 変換（頂点法線は追従し、ミラー反転では面の頂点の巡回方向も反転します）（ローカル座標を親空間に写します）。 |
| `Move3D(offset: Point3D) -> bool` | メッシュを`offset`だけ移動します。変換（頂点法線は追従し、ミラー反転では面の頂点の巡回方向も反転します）。 |
| `Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool` | メッシュを`angleDegrees`（度）だけ、軸`axis`（`center`を通る）を中心に回転します。変換（頂点法線は追従し、ミラー反転では面の頂点の巡回方向も反転します）。 |
| `Scale3D(center: Point3D, factors: Point3D) -> bool` | メッシュを`factors`（軸ごと）で、`center`を基準に拡大縮小します。変換（頂点法線は追従し、ミラー反転では面の頂点の巡回方向も反転します）。 |
| `GetSurfaceArea() -> float \| None` | 測定値（ワールド単位）。3D境界、中心、サイズはPrimitiveObjectで取得します。 |
| `GetVolume() -> float \| None` | 体積を返します（閉じたメッシュで意味を持ちます）。 |

継承：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

#### MeshObject.Face

> **完全修飾名:** `api.MeshObject.Face` · **継承元:** `api.Object`

パート0は全体の（テクスチャなしの）パートを意味します。`GetOverallPart()`を参照してください。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Face()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Face(vertexIndices, part)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `vertexIndices` | `list[int]` | 面の頂点のインデックス。 |
| `part` | `int` | 面のテクスチャパートのインデックス。 |

#### MeshObject.Part

> **完全修飾名:** `api.MeshObject.Part` · **継承元:** `api.Object`

テクスチャパート：id、テクスチャ参照（0 = テクスチャなし）、およびそれを使用する面の数。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Part()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Part(id, texture, faceCount)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `id` | `int` | パートID。 |
| `texture` | `int` | テクスチャリソース参照。テクスチャなしの場合は0。 |
| `faceCount` | `int` | パート内の面の数。 |

#### MeshObject.Smoothing

> **完全修飾名:** `api.MeshObject.Smoothing` · **種類:** `IntEnum`

レンダリング時のメッシュのスムージング方法。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` |  |
| `DocumentPreference` | `1` |  |
| `CustomCrease` | `2` |  |
| `Imported` | `3` |  |

### SolidPrimitiveObject

> **完全修飾名:** `api.SolidPrimitiveObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準のパラメトリックソリッドプリミティブ（`ObjectType.Solid`）、つまり球、半球、円錐の共通基底クラス。各プリミティブは、ローカルフレーム（原点 + 正規直交I/J/K軸）と、そのパラメータとして保存されます：

- 球／半球：origin = center、K = 上向きの軸（半球のドームは+K方向を向く）
- 円錐：origin = 底面中心、K = 底面から頂点に向かう軸

プリミティブは汎用ソリッドの有効なオペランドです。汎用ソリッドの履歴内にあるプリミティブを編集した後は、最も外側のソリッドで`GenericSolidObject.Rebuild()`を呼び出してください。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `SolidPrimitiveObject(h: Handle)` | 既存のソリッドプリミティブ`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `GetKindOf(h: Handle) -> SolidPrimitiveObject.Kind \| None` *静的* | `h`の種類を返します。 |
| `GetPrimitivesIn(hContainer: Handle) -> list[Handle]` *静的* | コンテナ（グループ、レイヤ、...）の直接のメンバーである球、半球、円錐プリミティブ |
| `GetPrimitiveOperands(hSolid: Handle) -> list[Handle]` *静的* | 汎用ソリッドの履歴内の任意の場所で使用されているプリミティブ。 |
| `GetKind() -> SolidPrimitiveObject.Kind \| None` | 種類を返します。 |

*ローカルフレーム*

| メソッド | 説明 |
|---|---|
| `GetFrame() -> ExtrudeObject.Transform \| None` | 原点、uAxis = I、vAxis = J、wAxis = K（単位ベクトル）。 |
| `SetFrame(origin: Point3D, iAxis: Point3D, jAxis: Point3D) -> bool` | 原点を移動し、プリミティブの向きを変更します。iAxisとjAxisを正規直交化し、K = I x Jとします。 |
| `GetAxis() -> Point3D \| None` | 軸を返します。 |
| `SetAxis(axis: Point3D) -> bool` | Kが`axis`に沿うように、プリミティブを原点の周りに回転します（最短の回転）。 |
| `Move3D(offset: Point3D) -> bool` | 剛体変換と均等な拡大縮小（プリミティブは種類を維持）。 |
| `Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool` | `angleDegrees`（度）だけ、軸`axis`（`center`を通る）を中心に回転します。剛体変換と均等な拡大縮小（プリミティブは種類を維持）。 |
| `Scale3D(center: Point3D, factor: float) -> bool` | `factor`（> 0）で、`center`を基準に均等に拡大縮小します。剛体変換と均等な拡大縮小（プリミティブは種類を維持）。 |
| `GetVolume() -> float \| None` | 測定値（ワールド単位）。 |
| `GetSurfaceArea() -> float \| None` | 表面積を返します。 |
| `ToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | 汎用ソリッドとの連携。keepOriginal = `False`の場合、このプリミティブを新しいソリッドの履歴内に移動するため、その後オブジェクトは履歴のオペランドを参照します。 |
| `Union(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | ソリッド`hTool`との和集合を汎用ソリッドとして返します。汎用ソリッドとの連携。keepOriginal = `False`の場合、このプリミティブを新しいソリッドの履歴内に移動するため、その後オブジェクトは履歴のオペランドを参照します。 |
| `Subtract(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | ソリッド`hTool`を差し引いた差分を汎用ソリッドとして返します。汎用ソリッドとの連携。keepOriginal = `False`の場合、このプリミティブを新しいソリッドの履歴内に移動するため、その後オブジェクトは履歴のオペランドを参照します。 |
| `Intersect(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | ソリッド`hTool`との共通部分を汎用ソリッドとして返します。汎用ソリッドとの連携。keepOriginal = `False`の場合、このプリミティブを新しいソリッドの履歴内に移動するため、その後オブジェクトは履歴のオペランドを参照します。 |
| `ConvertToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | 履歴のない汎用ソリッド（ConvertToGenericSolidと同様）。keepOriginal = `False`の場合、このプリミティブを削除します。 |
| `ToMesh(keepOriginal: bool = True) -> MeshObject` | プリミティブをテセレーションしてメッシュを作成し、その直後に配置します。 |

継承：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

#### SolidPrimitiveObject.Kind

> **完全修飾名:** `api.SolidPrimitiveObject.Kind` · **種類:** `IntEnum`

ソリッドプリミティブの種類。

| メンバー | 値 | 説明 |
|---|---|---|
| `Sphere` | `0` |  |
| `Hemisphere` | `1` |  |
| `Cone` | `2` |  |

### SphereObject

> **完全修飾名:** `api.SphereObject` · **継承元:** [`SolidPrimitiveObject`](#solidprimitiveobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準の球ソリッド。半径はローカルI/J/K軸に沿って測定するため、半径が不均等な場合は楕円体になります。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `SphereObject(h: Handle)` | 既存の球`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(center: Point3D, radius: float) -> SphereObject` *静的* | 指定した`center`と`radius`で球を作成します。 |
| `CreateEllipsoid(center: Point3D, radii: Point3D) -> SphereObject` *静的* | 座標軸に平行な楕円体。radii = (I方向の半径, J方向の半径, K方向の半径)。 |
| `Duplicate() -> SphereObject` | 図面内の球を複製し、コピーを返します。 |
| `GetCenter() -> Point3D \| None` | 中心を返します。 |
| `SetCenter(center: Point3D) -> bool` | 中心を設定します。 |
| `GetRadius() -> float \| None` | GetRadiusはI方向の半径を返し、SetRadiusは三つすべての半径を設定します。 |
| `SetRadius(radius: float) -> bool` | 半径を設定します。GetRadiusはI方向の半径を返し、SetRadiusは三つすべての半径を設定します。 |
| `GetRadii() -> Point3D \| None` | 各半径を返します。 |
| `SetRadii(radii: Point3D) -> bool` | 各半径を設定します。 |
| `IsEllipsoid() -> bool` | 球が不均等に拡大縮小されている場合はTrue（楕円体）。 |

継承：[`SolidPrimitiveObject`](#solidprimitiveobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

### HemisphereObject

> **完全修飾名:** `api.HemisphereObject` · **継承元:** [`SphereObject`](#sphereobject) → [`SolidPrimitiveObject`](#solidprimitiveobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準の半球ソリッド。ドームは中心からローカルK軸方向を向きます

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `HemisphereObject(h: Handle)` | 既存の半球`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(center: Point3D, topPoint: Point3D) -> HemisphereObject` *静的* | `center`を中心とし、頂部（極）が`topPoint`にある半球を作成します。 |
| `Create(center: Point3D, radius: float) -> HemisphereObject` *静的* | 指定した`center`と`radius`で、上向きの半球を作成します。 |
| `Duplicate() -> HemisphereObject` | 図面内の半球を複製し、コピーを返します。 |
| `GetTopPoint() -> Point3D \| None` | 中心 + K * K方向の半径。 |
| `SetTopPoint(topPoint: Point3D) -> bool` | ドームをtopPointに向け、均等な半径 = \|topPoint - center\|を設定します。 |

継承：[`SphereObject`](#sphereobject)、[`SolidPrimitiveObject`](#solidprimitiveobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

### ConeObject

> **完全修飾名:** `api.ConeObject` · **継承元:** [`SolidPrimitiveObject`](#solidprimitiveobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準の円錐ソリッド。底面は、ローカルI/J平面内で底面中心（フレーム原点）を中心とする楕円です。頂点はオブジェクト空間に保存されるため、底面中心を移動すると円錐全体が移動します。直円錐の頂点はローカルK軸上にあり、斜円錐の頂点は底面平面の上側または下側の任意の位置にあります。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ConeObject(h: Handle)` | 既存の円錐`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(baseCenter: Point3D, tipPoint: Point3D, radius: float) -> ConeObject` *静的* | 半径`radius`、中心`baseCenter`の底円と、`tipPoint`の頂点を持つ円錐を作成します。 |
| `Create(baseCenter: Point3D, radius: float, height: float) -> ConeObject` *静的* | 半径`radius`、中心`baseCenter`の底円と、`tipPoint`の頂点を持つ円錐を作成します。 |
| `Duplicate() -> ConeObject` | 図面内の円錐を複製し、コピーを返します。 |
| `GetBaseCenter() -> Point3D \| None` | 底面中心を返します。 |
| `SetBaseCenter(baseCenter: Point3D) -> bool` | 底面中心を設定します。 |
| `GetTipPoint() -> Point3D \| None` | ワールド座標での頂点。keepRight = `True`は、直円錐のままになるように円錐の向きを変更します。`False`は底面平面を維持し、必要に応じて円錐を斜円錐にします。 |
| `SetTipPoint(tipPoint: Point3D, keepRight: bool = True) -> bool` | 頂点を設定します。ワールド座標での頂点。keepRight = `True`は、直円錐のままになるように円錐の向きを変更します。`False`は底面平面を維持し、必要に応じて円錐を斜円錐にします。 |
| `GetLocalTipPoint() -> Point3D \| None` | ローカルフレーム（I、J、K）での頂点。 |
| `SetLocalTipPoint(localTipPoint: Point3D) -> bool` | ローカルの頂点を設定します（ローカルフレーム（I、J、K）での頂点）。 |
| `IsRightCone() -> bool` | 頂点が底面中心を通る軸上にある場合はTrue。 |
| `GetHeight() -> float \| None` | 底面平面から頂点までの距離。SetHeightは円錐を直円錐にします。高さが負の場合、円錐を底面の反対側に反転します。 |
| `SetHeight(height: float) -> bool` | 高さを設定します。底面平面から頂点までの距離。SetHeightは円錐を直円錐にします。高さが負の場合、円錐を底面の反対側に反転します。 |
| `GetRadius() -> float \| None` | GetRadiusはI方向の半径を返し、SetRadiusは底面の両方の半径を設定します。 |
| `SetRadius(radius: float) -> bool` | 半径を設定します。GetRadiusはI方向の半径を返し、SetRadiusは底面の両方の半径を設定します。 |
| `GetRadii() -> ConeObject.Radii \| None` | 各半径を返します。 |
| `SetRadii(radii: ConeObject.Radii) -> bool` | 各半径を設定します。 |
| `IsElliptical() -> bool` | 底面が円ではなく楕円の場合はTrue。 |

継承：[`SolidPrimitiveObject`](#solidprimitiveobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

#### ConeObject.Radii

> **完全修飾名:** `api.ConeObject.Radii` · **継承元:** `api.Object`

ローカルI軸とJ軸に沿った底面の半径。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Radii()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Radii(i, j)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `i` | `float` | ローカルI軸に沿った底面の半径。 |
| `j` | `float` | ローカルJ軸に沿った底面の半径。 |

### NurbsCurveObject

> **完全修飾名:** `api.NurbsCurveObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準の区分的なNURBS曲線。区間、点、ノットのインデックスは0始まりです。座標と距離はワールド単位です。インスタンスは図面オブジェクトの軽量なビューです。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `NurbsCurveObject(h: Handle)` | 既存のNURBS曲線`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(points: list[Point3D], degree: int, byControlPoints: bool = True) -> NurbsCurveObject` *静的* | 制御点または補間点の曲線を作成します。最初の点で標準の曲線を作成し、残りの点は標準のNURBS点操作を使用して挿入します。 |
| `Duplicate() -> NurbsCurveObject` | 図面内のNURBS曲線を複製し、コピーを返します。 |
| `GetPieceCount() -> int` | 区間項目の数。 |
| `GetPointCount(pieceIndex: int = 0) -> int` | `pieceIndex`の点項目の数。 |
| `GetControlPointCount(pieceIndex: int = 0) -> int` | `pieceIndex`の制御点項目の数。 |
| `GetDegree(pieceIndex: int = 0) -> int \| None` | `pieceIndex`の次数を返します。 |
| `GetPoint(pieceIndex: int, pointIndex: int) -> Point3D \| None` | `pieceIndex`、`pointIndex`の点を返します。 |
| `SetPoint(pieceIndex: int, pointIndex: int, point: Point3D) -> bool` | `pieceIndex`の点を設定します。 |
| `GetWeight(pieceIndex: int, controlPointIndex: int) -> float \| None` | `pieceIndex`、`controlPointIndex`のウェイトを返します。 |
| `SetWeight(pieceIndex: int, controlPointIndex: int, weight: float) -> bool` | `pieceIndex`のウェイトを設定します。 |
| `GetKnotCount(pieceIndex: int = 0) -> int` | `pieceIndex`のノット項目の数。 |
| `GetKnot(pieceIndex: int, knotIndex: int) -> float \| None` | `pieceIndex`、`knotIndex`のノットを返します。 |
| `SetKnot(pieceIndex: int, knotIndex: int, knot: float) -> bool` | `pieceIndex`のノットを設定します。 |
| `Evaluate(pieceIndex: int, parameter: float) -> Point3D \| None` | 区間`pieceIndex`のパラメータ`parameter`における点。 |
| `GetLength() -> float \| None` | 画面に投影した距離ではなく、ワールド座標での読み取り専用の解析。パラメータは区間ごとの固有のノットパラメータであり、正規化した弧長ではありません。区間の接続点では、距離による検索は前側の長さがゼロでない区間を選択します。 |
| `GetLocationAtDistance(distance: float) -> NurbsCurveObject.Location \| None` | 距離`distance`にある位置を返します。 |
| `GetPointAtDistance(distance: float) -> Point3D \| None` | 距離`distance`にある点を返します。 |
| `GetClosestPoint(point: Point3D) -> NurbsCurveObject.Location \| None` | `point`に最も近い点を返します。 |
| `GetDistanceTo(point: Point3D) -> float \| None` | `point`までの距離を返します。 |
| `GetTangent(pieceIndex: int, parameter: float) -> Point3D \| None` | 単位接線ベクトルと非負の曲率（ワールド単位の逆数）。ノットでは右側微分を使用しますが、区間の終点では左側微分を使用します。速度がゼロの点には接線も曲率もなく、`None`を返します。 |
| `GetCurvature(pieceIndex: int, parameter: float) -> float \| None` | `pieceIndex`、`parameter`の曲率を返します。 |
| `DivideByCount(count: int, includeEnd: bool = True) -> list[Point3D] \| None` | ちょうどcount個（>= 2）の、弧長に沿って等間隔に配置された点。includeEndは閉じた曲線であっても両端点を含めます。`False`は終点／継ぎ目を省略します。周回処理や範囲への制限は行いません。無効／退化した曲線、有限でない／範囲外の距離、および処理の失敗では`None`を返します。 |
| `Extend(distance: float, atStart: bool, linear: bool) -> NurbsCurveObject` | 標準の操作は結果をアクティブレイヤに挿入し、この曲線は変更しません。 |
| `Offset(distance: float) -> NurbsCurveObject` | `distance`だけオフセットした曲線を作成します。標準の操作は結果をアクティブレイヤに挿入し、この曲線は変更しません。 |

継承：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

#### NurbsCurveObject.Location

> **完全修飾名:** `api.NurbsCurveObject.Location` · **継承元:** `api.Object`

ゼロ始まりの区間における曲線上の点と固有のパラメータ。パラメータは弧長ではありません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Location()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Location(point, pieceIndex, parameter)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `point` | `Point3D` | 曲線上の点。 |
| `pieceIndex` | `int` | 曲線区間のインデックス。 |
| `parameter` | `float` | その区間のパラメータ。 |

### NurbsSurfaceObject

> **完全修飾名:** `api.NurbsSurfaceObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

標準のNURBS曲面。制御ネットの座標と距離はワールド単位です。U/Vの点とノットのインデックスは0始まりです。インスタンスは図面オブジェクトの軽量なビューです。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `NurbsSurfaceObject(h: Handle)` | 既存のNURBS曲面`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(uPointCount: int, vPointCount: int, uDegree: int, vDegree: int) -> NurbsSurfaceObject` *静的* | `uPointCount` x `vPointCount`個の制御点と、次数`uDegree` / `vDegree`を持つNURBS曲面を作成します。 |
| `CreateFromCurvesNetwork() -> bool` *静的* | 選択した交差する曲線を使用し、消費します。元のオブジェクトはすべて破棄してください。標準の失敗時クリーンアップでも入力が削除される場合があります。呼び出す前に取り消しを登録してください。 |
| `Duplicate() -> NurbsSurfaceObject` | 図面内のNURBS曲面を複製し、コピーを返します。 |
| `GetUPointCount() -> int` | U方向の点項目の数。 |
| `GetVPointCount() -> int` | V方向の点項目の数。 |
| `GetUDegree() -> int \| None` | U方向の次数を返します。 |
| `GetVDegree() -> int \| None` | V方向の次数を返します。 |
| `GetPoint(uIndex: int, vIndex: int) -> Point3D \| None` | `uIndex`、`vIndex`の点を返します。 |
| `SetPoint(uIndex: int, vIndex: int, point: Point3D) -> bool` | `uIndex`の点を設定します。 |
| `GetWeight(uIndex: int, vIndex: int) -> float \| None` | `uIndex`、`vIndex`のウェイトを返します。 |
| `SetWeight(uIndex: int, vIndex: int, weight: float) -> bool` | `uIndex`のウェイトを設定します。 |
| `GetUKnotCount() -> int` | U方向のノット項目の数。 |
| `GetVKnotCount() -> int` | V方向のノット項目の数。 |
| `GetUKnot(knotIndex: int) -> float \| None` | `knotIndex`のU方向のノットを返します。 |
| `GetVKnot(knotIndex: int) -> float \| None` | `knotIndex`のV方向のノットを返します。 |
| `SetUKnot(knotIndex: int, knot: float) -> bool` | `knotIndex`のU方向のノットを設定します。 |
| `SetVKnot(knotIndex: int, knot: float) -> bool` | `knotIndex`のV方向のノットを設定します。 |
| `Evaluate(u: float, v: float) -> Point3D \| None` | パラメータ`u`、`v`における曲面上の点。 |
| `TrimByCurve(curve: NurbsCurveObject) -> bool` | TrimNurbsSurfaceは、曲線を曲面のトリム境界として取り付けます。 |
| `Extend(distance: float, atStart: bool, linear: bool, uDirection: bool) -> NurbsSurfaceObject` | 標準の操作は結果をアクティブレイヤに挿入し、この曲面は変更しません。 |
| `Offset(distance: float) -> NurbsSurfaceObject` | `distance`だけオフセットした曲面を作成します。標準の操作は結果をアクティブレイヤに挿入し、この曲面は変更しません。 |

継承：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべてのメンバー。

---

[一覧に戻る](README.md) · [先頭に戻る](#objects3d--3d-objects)
