[English](../../PythonAPI/v2027.2/Attributes.md) • [Deutsch](../../PythonAPI.de/v2027.2/Attributes.md) • **日本語**

<a id="attributes--graphic-attributes-and-classes"></a>

# Attributes — グラフィック属性とクラス

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

属性クラスはオブジェクトの外観を記述します。`ObjectAttributes`は一つのオブジェクトのすべてのグラフィック属性（`Pen()`、`Fill()`、`FillMapping()`、`Markers()`、`DropShadow()`）をまとめます。`PenAttributes`は線（色、スタイル、線の太さ、不透明度）、`FillAttributes`は面（色、スタイル、不透明度）、`FillMappingAttributes`はハッチング、タイル、グラデーション、イメージの面のマッピング、`MarkerAttributes`は始点と終点のマーカー、`DropShadowAttributes`はドロップシャドウを扱います。`ClassAttributes`はクラス定義、つまり多数のオブジェクトで共有する、名前を付けて保存した属性のセットを表します。

値型の`ColorRGB`、`ColorPair`、`ObjectColors`、`Marker`、`DropShadow`、`WallTextures`、`RoofTextures`、`Point2D`、属性の列挙型、およびモジュール定数`api.kMaxOpacity`もこのグループに属します。

**「クラス属性」:** 「クラス属性」に設定された属性は、オブジェクト自体の値を無視し、そのオブジェクトが属するクラスの値を使用します。属性クラスの`Get...ByClass` / `Set...ByClass`メソッドで確認および変更します。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [Point2D](#point2d)
  - [ColorRGB](#colorrgb)
  - [ColorPair](#colorpair)
  - [ObjectColors](#objectcolors)
  - [Marker](#marker)
  - [DropShadow](#dropshadow)
  - [WallTextures](#walltextures)
  - [RoofTextures](#rooftextures)
  - [AttributesBase](#attributesbase)
  - [PenAttributes](#penattributes)
  - [FillAttributes](#fillattributes)
  - [FillMappingAttributes](#fillmappingattributes)
    - [FillMappingAttributes.Frame](#fillmappingattributesframe)
  - [MarkerAttributes](#markerattributes)
  - [DropShadowAttributes](#dropshadowattributes)
  - [ClassAttributes](#classattributes)
  - [ObjectAttributes](#objectattributes)
- [列挙型](#enumerations)
  - [PenStyleKind](#penstylekind)
  - [FillType](#filltype)
  - [MarkerShape](#markershape)
  - [MarkerFill](#markerfill)
  - [MarkerBase](#markerbase)
  - [MarkerHalfTick](#markerhalftick)
  - [MarkerThicknessBasis](#markerthicknessbasis)
  - [MarkerThicknessUnits](#markerthicknessunits)
  - [DropShadowUnits](#dropshadowunits)
  - [ClassVisibility](#classvisibility)
  - [ObjectType](#objecttype)
- [モジュール定数](#module-constants)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`Point2D`](#point2d) | クラス |  | ダイアログと属性のAPIで使用する単純な2D点レコード（`x`、`y`はワールド単位）。 |
| [`ColorRGB`](#colorrgb) | クラス |  | チャンネルあたり16ビットのRGB色（0 .. |
| [`ColorPair`](#colorpair) | クラス |  | 色インデックスで表した、線または面の前景色と背景色。 |
| [`ObjectColors`](#objectcolors) | クラス |  | 色インデックスで表した、オブジェクトの四つの色すべて（線の前景／背景、面の前景／背景）。 |
| [`Marker`](#marker) | クラス |  | 線の始点または終点のマーカー（矢印先端）：形状、面、底辺、半欠け、反転、角度（度）、長さと幅（用紙上のインチ）、線の太さ... |
| [`DropShadow`](#dropshadow) | クラス |  | オブジェクト、クラス、またはファイルのドロップシャドウ設定：オン／オフ、単位、オフセット、ぼかし半径、角度、色、不透明度。 |
| [`WallTextures`](#walltextures) | クラス |  | クラスの壁テクスチャ（テクスチャリソースの内部インデックス、0 = なし）。 |
| [`RoofTextures`](#rooftextures) | クラス |  | クラスの屋根テクスチャ（テクスチャリソースの内部インデックス、0 = なし）。 |
| [`AttributesBase`](#attributesbase) | クラス |  | グラフィック属性クラスの共通基底クラス。 |
| [`PenAttributes`](#penattributes) | クラス | [`AttributesBase`](#attributesbase) | オブジェクトのペン（線）属性：色、スタイル（模様／ラインタイプ）、線の太さ、不透明度、クラス属性フラグ、およびラインタイプのマッピング（線のマッピング空間）。 |
| [`FillAttributes`](#fillattributes) | クラス | [`AttributesBase`](#attributesbase) | オブジェクトの面属性：色、スタイル（模様／ハッチング／タイル／グラデーション／イメージ）、不透明度、クラス属性フラグ。 |
| [`FillMappingAttributes`](#fillmappingattributes) | クラス | [`AttributesBase`](#attributesbase) | ハッチング、タイル、グラデーション、イメージの面のマッピング（面のマッピング空間）：原点、軸、オフセット、回転、繰り返し、ミラー、反転。 |
| [`FillMappingAttributes.Frame`](#fillmappingattributesframe) | クラス（入れ子） |  | ハッチング、タイル、グラデーション、イメージの面のマッピングフレーム：原点とI軸およびJ軸の終点。 |
| [`MarkerAttributes`](#markerattributes) | クラス | [`AttributesBase`](#attributesbase) | オブジェクトの始点と終点のマーカー（矢印先端）。 |
| [`DropShadowAttributes`](#dropshadowattributes) | クラス | [`AttributesBase`](#attributesbase) | オブジェクトのドロップシャドウ。 |
| [`ClassAttributes`](#classattributes) | クラス | [`AttributesBase`](#attributesbase) | クラス定義（`ObjectType.ClassDefinition`）：名前を付けて保存した属性設定。 |
| [`ObjectAttributes`](#objectattributes) | クラス | [`AttributesBase`](#attributesbase) | オブジェクトのすべてのグラフィック属性。 |
| [`PenStyleKind`](#penstylekind) | IntEnum |  | 未加工の線スタイル値の分類。 |
| [`FillType`](#filltype) | IntEnum |  | オブジェクトの面の種類。 |
| [`MarkerShape`](#markershape) | IntEnum |  | マーカー（矢印先端） |
| [`MarkerFill`](#markerfill) | IntEnum |  | 以下のマーカースタイル列挙型（MarkerFill、MarkerBase、MarkerHalfTick）は、ビット単位のORで単一の16ビットスタイルにまとめられるよう、あらかじめシフトした値を使用します... |
| [`MarkerBase`](#markerbase) | IntEnum |  | マーカーの底辺の形状（シフト済みのビット値。`Marker.GetStyleValue`を参照）。 |
| [`MarkerHalfTick`](#markerhalftick) | IntEnum |  | マーカー全体、またはその左半分か右半分のみ（シフト済みのビット値。`Marker.GetStyleValue`を参照）。 |
| [`MarkerThicknessBasis`](#markerthicknessbasis) | IntEnum |  | マーカーの線の太さが従う基準。 |
| [`MarkerThicknessUnits`](#markerthicknessunits) | IntEnum |  | カスタムマーカーの線の太さの単位。 |
| [`DropShadowUnits`](#dropshadowunits) | IntEnum |  | ドロップシャドウ |
| [`ClassVisibility`](#classvisibility) | IntEnum |  | クラス |
| [`ObjectType`](#objecttype) | IntEnum |  | オブジェクトの種類。 |
| [モジュール定数](#module-constants) | 定数 | | `kMaxOpacity` |

<a id="classes"></a>

## クラス

### Point2D

> **完全修飾名:** `api.Point2D` · **継承元:** `api.Object`

ダイアログと属性のAPIで使用する単純な2D点レコード（`x`、`y`はワールド単位）。完全なベクトル演算機能を備えた`api.Math.Point2D`と双方向に暗黙変換されます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Point2D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Point2D(x, y)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: Point2D) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: Point2D) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `x` | `float` | X座標（ワールド単位）。 |
| `y` | `float` | Y座標（ワールド単位）。 |

### ColorRGB

> **完全修飾名:** `api.ColorRGB` · **継承元:** `api.Object`

チャンネルあたり16ビットのRGB色（0 .. 65535）。Vectorworksの色表現との間で情報が失われません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ColorRGB()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ColorRGB(red, green, blue)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `FromRGB8(r: int, g: int, b: int) -> ColorRGB` *静的* | 8ビットのチャンネル（各0 .. 255）から色を作成します。 |
| `Red8() -> int` | 8ビットにスケーリングした赤チャンネル（0 .. 255）。 |
| `Green8() -> int` | 8ビットにスケーリングした緑チャンネル（0 .. 255）。 |
| `Blue8() -> int` | 8ビットにスケーリングした青チャンネル（0 .. 255）。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: ColorRGB) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: ColorRGB) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `red` | `int` | 赤チャンネル（0 .. 65535）。 |
| `green` | `int` | 緑チャンネル（0 .. 65535）。 |
| `blue` | `int` | 青チャンネル（0 .. 65535）。 |

### ColorPair

> **完全修飾名:** `api.ColorPair` · **継承元:** `api.Object`

色インデックスで表した、線または面の前景色と背景色。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ColorPair()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ColorPair(fore, back)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: ColorPair) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: ColorPair) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fore` | `int` | 前景色（色インデックス）。 |
| `back` | `int` | 背景色（色インデックス）。 |

### ObjectColors

> **完全修飾名:** `api.ObjectColors` · **継承元:** `api.Object`

色インデックスで表した、オブジェクトの四つの色すべて（線の前景／背景、面の前景／背景）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ObjectColors()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ObjectColors(pen, fill)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: ObjectColors) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: ObjectColors) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `pen` | `ColorPair` | 線の前景色／背景色。 |
| `fill` | `ColorPair` | 面の前景色／背景色。 |

### Marker

> **完全修飾名:** `api.Marker` · **継承元:** `api.Object`

線の始点または終点のマーカー（矢印先端）：形状、面、底辺、半欠け、反転、角度（度）、長さと幅（用紙上のインチ）、線の太さの設定。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Marker()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Marker(shape, fill, base, halfTick, tail, angle, length, width, thicknessBasis, thicknessUnits, thickness, visible)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetStyleValue() -> int` | まとめられたマーカースタイル値（shape \| fill \| base \| half tick \| tail）。 |
| `SetStyleValue(value: int) -> None` | スタイル値を設定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: Marker) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: Marker) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `shape` | `MarkerShape` | マーカーの形状。 |
| `fill` | `MarkerFill` | マーカーの面。 |
| `base` | `MarkerBase` | マーカーの底辺の形状。 |
| `halfTick` | `MarkerHalfTick` | マーカー全体、またはその左半分か右半分のみ。 |
| `tail` | `bool` | マーカーを反転させるかどうか。 |
| `angle` | `int` | 度。 |
| `length` | `float` | 用紙上のインチ。 |
| `width` | `float` | 用紙上のインチ。 |
| `thicknessBasis` | `MarkerThicknessBasis` | マーカーの線の太さが従う基準：線、寸法の標準設定、または`thickness`。 |
| `thicknessUnits` | `MarkerThicknessUnits` | `thickness`の単位。 |
| `thickness` | `float` | `MarkerThicknessBasis.Custom`で使用し、単位はthicknessUnitsです。 |
| `visible` | `bool` | マーカーを表示するかどうか。 |

### DropShadow

> **完全修飾名:** `api.DropShadow` · **継承元:** `api.Object`

オブジェクト、クラス、またはファイルのドロップシャドウ設定：オン／オフ、単位、オフセット、ぼかし半径、角度、色、不透明度。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DropShadow()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `DropShadow(useDropShadow, units, offset, blurRadius, angle, color, opacity)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: DropShadow) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: DropShadow) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `useDropShadow` | `bool` | ドロップシャドウがオンかどうか。 |
| `units` | `DropShadowUnits` | `offset`と`blurRadius`が用紙上の長さかワールド長さか。 |
| `offset` | `float` | オブジェクトから影までの距離。 |
| `blurRadius` | `float` | 影のぼかし半径。 |
| `angle` | `float` | 度。 |
| `color` | `int` | 影の色（色インデックス）。 |
| `opacity` | `int` | 影の不透明度（0 .. 100）。 |

### WallTextures

> **完全修飾名:** `api.WallTextures` · **継承元:** `api.Object`

クラスの壁テクスチャ（テクスチャリソースの内部インデックス、0 = なし）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `WallTextures()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `WallTextures(right, left, center)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: WallTextures) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: WallTextures) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `right` | `int` | 右側のテクスチャ（テクスチャインデックス、0 = なし）。 |
| `left` | `int` | 左側のテクスチャ（テクスチャインデックス、0 = なし）。 |
| `center` | `int` | 壁の中央のテクスチャ（テクスチャインデックス、0 = なし）。 |

### RoofTextures

> **完全修飾名:** `api.RoofTextures` · **継承元:** `api.Object`

クラスの屋根テクスチャ（テクスチャリソースの内部インデックス、0 = なし）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RoofTextures()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `RoofTextures(top, edge, dormer)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: RoofTextures) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: RoofTextures) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `top` | `int` | 屋根上面のテクスチャ（テクスチャインデックス、0 = なし）。 |
| `edge` | `int` | 屋根端部のテクスチャ（テクスチャインデックス、0 = なし）。 |
| `dormer` | `int` | ドーマーのテクスチャ（テクスチャインデックス、0 = なし）。 |

### AttributesBase

> **完全修飾名:** `api.AttributesBase` · **継承元:** `api.Object`

グラフィック属性クラスの共通基底クラス。インスタンスはオブジェクトを所有せず、その属性の読み書きのみを行います。ハンドルがnull、またはオブジェクトがその属性をサポートしていない場合、ゲッターは`None`を返します。ハンドルがnull、またはオブジェクトがその属性をサポートしていない場合、セッターは`False`を返します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `AttributesBase(h: Handle)` | 既存の属性基底オブジェクト`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetHandle() -> Handle` | 属性基底オブジェクトのハンドル。 |
| `IsValid() -> bool` | このオブジェクトが既存の属性基底オブジェクトを参照している場合はTrue。 |
| `GetObjectType() -> ObjectType` | オブジェクトの種類を返します。 |
| `IsGroup() -> bool` | オブジェクトがグループである場合はTrue（その属性は内部のオブジェクトに適用されます）。 |
| `GetObjectColors() -> ObjectColors \| None` | 四つの色すべてを一度に扱います（線の前景／背景、面の前景／背景）。 |
| `SetObjectColors(colors: ObjectColors) -> bool` | オブジェクトの色を設定します。四つの色すべてを一度に扱います（線の前景／背景、面の前景／背景）。 |
| `ColorIndexToRGB(index: int) -> ColorRGB` *静的* | ファイルのカラーテーブルの色インデックス`index`のRGB色。 |
| `RGBToColorIndex(color: ColorRGB) -> int` *静的* | ファイルのカラーテーブルで`color`に最も近いエントリのインデックス。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`：オブジェクトが有効な場合はTrue（`IsValid()`と同じ）。 |

### PenAttributes

> **完全修飾名:** `api.PenAttributes` · **継承元:** [`AttributesBase`](#attributesbase) → `api.Object`

オブジェクトのペン（線）属性：色、スタイル（模様／ラインタイプ）、線の太さ、不透明度、クラス属性フラグ、およびラインタイプのマッピング（線のマッピング空間）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `PenAttributes(h: Handle)` | 既存のペン`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*色*

| メソッド | 説明 |
|---|---|
| `GetForeColor() -> ColorRGB \| None` | 前景色を返します。 |
| `SetForeColor(color: ColorRGB) -> bool` | 前景色を設定します。 |
| `GetBackColor() -> ColorRGB \| None` | 背景色を返します。 |
| `SetBackColor(color: ColorRGB) -> bool` | 背景色を設定します。 |
| `GetForeColorIndex() -> int \| None` | 前景色のインデックスを返します。 |
| `SetForeColorIndex(index: int) -> bool` | 前景色のインデックスを設定します。 |
| `GetBackColorIndex() -> int \| None` | 背景色のインデックスを返します。 |
| `SetBackColorIndex(index: int) -> bool` | 背景色のインデックスを設定します。 |
| `GetColors() -> ColorPair \| None` | 色を返します。 |
| `SetColors(colors: ColorPair) -> bool` | 色を設定します。 |
| `GetColorsByClass() -> bool \| None` | *色のクラス属性*がオンかどうか。 |
| `SetColorsByClass() -> bool` | 色をクラス属性に設定します。 |
| `GetStyle() -> int \| None` | スタイル。未加工の値：0はなし、1-2はカラー、> 2は従来の模様、< 0は-（ラインタイプの内部インデックス）。 |
| `SetStyle(style: int) -> bool` | スタイルを設定します。スタイル。未加工の値：0はなし、1-2はカラー、> 2は従来の模様、< 0は-（ラインタイプの内部インデックス）。 |
| `GetStyleKind() -> PenStyleKind \| None` | スタイルの種類を返します。 |
| `GetNone() -> bool \| None` | *なし*がオンかどうか。 |
| `SetNone() -> bool` | なしに設定します（グループのメンバーに再帰的に適用されます）。 |
| `GetSolid() -> bool \| None` | *カラー*がオンかどうか。 |
| `SetSolid() -> bool` | カラーに設定します（グループのメンバーに再帰的に適用されます）。 |
| `GetLineType() -> int \| None` | ラインタイプの内部インデックス（正の値）。線がラインタイプでない場合は空です。 |
| `SetLineType(lineTypeIndex: int) -> bool` | ラインタイプを設定します。ラインタイプの内部インデックス（正の値）。線がラインタイプでない場合は空です。 |
| `GetStyleByClass() -> bool \| None` | *スタイルのクラス属性*がオンかどうか。 |
| `SetStyleByClass() -> bool` | スタイルをクラス属性に設定します。 |

*線の太さ*

| メソッド | 説明 |
|---|---|
| `GetLineWeightMils() -> int \| None` | 線の太さをミル単位で返します。 |
| `SetLineWeightMils(mils: int) -> bool` | 線の太さをミル単位で設定します。 |
| `GetLineWeightMillimeters() -> float \| None` | 線の太さをミリメートル単位で返します。 |
| `SetLineWeightMillimeters(mm: float) -> bool` | 線の太さをミリメートル単位で設定します。 |
| `GetLineWeightByClass() -> bool \| None` | *線の太さのクラス属性*がオンかどうか。 |
| `SetLineWeightByClass() -> bool` | 線の太さをクラス属性に設定します。 |

*不透明度*

| メソッド | 説明 |
|---|---|
| `GetOpacity() -> int \| None` | 不透明度を返します。 |
| `SetOpacity(opacity: int) -> bool` | 不透明度を設定します。 |
| `GetOpacityByClass() -> bool \| None` | *不透明度のクラス属性*がオンかどうか。 |
| `SetOpacityByClass(byClass: bool) -> bool` | *不透明度のクラス属性*をオンまたはオフにします。 |
| `IsMappingExisting() -> bool` | ラインタイプのマッピング（線のマッピング空間）。 |
| `GetLocalMapping() -> bool \| None` | *ローカルマッピングを使用*がオンかどうか。 |
| `SetLocalMapping(local: bool) -> bool` | *ローカルマッピングを使用*をオンまたはオフにします。 |
| `GetFlipHorizontal() -> bool \| None` | *水平反転*がオンかどうか。 |
| `SetFlipHorizontal(flip: bool) -> bool` | *水平反転*をオンまたはオフにします。 |
| `GetFlipVertical() -> bool \| None` | *垂直反転*がオンかどうか。 |
| `SetFlipVertical(flip: bool) -> bool` | *垂直反転*をオンまたはオフにします。 |
| `GetScale() -> float \| None` | 縮尺を返します。 |
| `SetScale(scale: float) -> bool` | 縮尺を設定します。 |

継承：[`AttributesBase`](#attributesbase)のすべてのメンバー。

### FillAttributes

> **完全修飾名:** `api.FillAttributes` · **継承元:** [`AttributesBase`](#attributesbase) → `api.Object`

オブジェクトの面属性：色、スタイル（模様／ハッチング／タイル／グラデーション／イメージ）、不透明度、クラス属性フラグ。面のマッピング（原点、縮尺、回転...）はFillMappingAttributesにあります。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `FillAttributes(h: Handle)` | 既存の面`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*色*

| メソッド | 説明 |
|---|---|
| `GetForeColor() -> ColorRGB \| None` | 前景色を返します。 |
| `SetForeColor(color: ColorRGB) -> bool` | 前景色を設定します。 |
| `GetBackColor() -> ColorRGB \| None` | 背景色を返します。 |
| `SetBackColor(color: ColorRGB) -> bool` | 背景色を設定します。 |
| `GetForeColorIndex() -> int \| None` | 前景色のインデックスを返します。 |
| `SetForeColorIndex(index: int) -> bool` | 前景色のインデックスを設定します。 |
| `GetBackColorIndex() -> int \| None` | 背景色のインデックスを返します。 |
| `SetBackColorIndex(index: int) -> bool` | 背景色のインデックスを設定します。 |
| `GetColors() -> ColorPair \| None` | 色を返します。 |
| `SetColors(colors: ColorPair) -> bool` | 色を設定します。 |
| `GetColorsByClass() -> bool \| None` | *色のクラス属性*がオンかどうか。 |
| `SetColorsByClass() -> bool` | 色をクラス属性に設定します。 |
| `GetStyle() -> int \| None` | スタイル。未加工の値：0はなし、1はカラー、> 1は従来の模様、< 0は-（ハッチング、タイル、グラデーション、またはイメージのリソースの内部インデックス）。 |
| `SetStyle(style: int) -> bool` | スタイルを設定します。スタイル。未加工の値：0はなし、1はカラー、> 1は従来の模様、< 0は-（ハッチング、タイル、グラデーション、またはイメージのリソースの内部インデックス）。 |
| `GetType() -> FillType \| None` | 種類を返します。 |
| `GetNone() -> bool \| None` | *なし*がオンかどうか。 |
| `SetNone() -> bool` | なしに設定します（グループのメンバーに再帰的に適用されます）。 |
| `GetSolid() -> bool \| None` | *カラー*がオンかどうか。 |
| `SetSolid() -> bool` | カラーに設定します（グループのメンバーに再帰的に適用されます）。 |
| `GetResource() -> int \| None` | ハッチング、タイル、グラデーション、またはイメージのリソースの内部インデックス（正の値）。面がリソースを使用していない場合は空です。 |
| `SetResource(resourceIndex: int) -> bool` | リソースを設定します。ハッチング、タイル、グラデーション、またはイメージのリソースの内部インデックス（正の値）。面がリソースを使用していない場合は空です。 |
| `GetStyleByClass() -> bool \| None` | *スタイルのクラス属性*がオンかどうか。 |
| `SetStyleByClass() -> bool` | スタイルをクラス属性に設定します。 |

*不透明度*

| メソッド | 説明 |
|---|---|
| `GetOpacity() -> int \| None` | 不透明度を返します。 |
| `SetOpacity(opacity: int) -> bool` | 不透明度を設定します。 |
| `GetOpacityByClass() -> bool \| None` | *不透明度のクラス属性*がオンかどうか。 |
| `SetOpacityByClass(byClass: bool) -> bool` | *不透明度のクラス属性*をオンまたはオフにします。 |

継承：[`AttributesBase`](#attributesbase)のすべてのメンバー。

### FillMappingAttributes

> **完全修飾名:** `api.FillMappingAttributes` · **継承元:** [`AttributesBase`](#attributesbase) → `api.Object`

ハッチング、タイル、グラデーション、イメージの面のマッピング（面のマッピング空間）：原点、軸、オフセット、回転、繰り返し、ミラー、反転。オブジェクトに面のマッピングがない場合、ゲッターは空の値を返します。セッターは必要に応じてマッピングを作成します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `FillMappingAttributes(h: Handle)` | 既存の面のマッピング`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `IsMappingExisting() -> bool` | オブジェクトが独自の面のマッピングデータを持つ場合はTrue。 |

*ワールド座標でのマッピングフレーム*

| メソッド | 説明 |
|---|---|
| `GetOriginPoint() -> Point2D \| None` | 原点を返します。 |
| `SetOriginPoint(pt: Point2D) -> bool` | 原点を設定します。 |
| `GetIAxisEndPoint() -> Point2D \| None` | I軸の終点を返します。 |
| `SetIAxisEndPoint(pt: Point2D) -> bool` | I軸の終点を設定します。 |
| `GetJAxisEndPoint() -> Point2D \| None` | J軸の終点を返します。 |
| `SetJAxisEndPoint(pt: Point2D) -> bool` | J軸の終点を設定します。 |
| `GetFrame() -> FillMappingAttributes.Frame \| None` | フレームを返します。 |
| `SetFrame(frame: FillMappingAttributes.Frame) -> bool` | フレームを設定します。 |

*内部単位でのオフセットと軸の長さ*

| メソッド | 説明 |
|---|---|
| `GetXOffset() -> float \| None` | Xオフセットを返します。 |
| `SetXOffset(value: float) -> bool` | Xオフセットを設定します。 |
| `GetYOffset() -> float \| None` | Yオフセットを返します。 |
| `SetYOffset(value: float) -> bool` | Yオフセットを設定します。 |
| `GetIAxisLength() -> float \| None` | I軸の長さを返します。 |
| `SetIAxisLength(value: float) -> bool` | I軸の長さを設定します。 |
| `GetJAxisLength() -> float \| None` | J軸の長さを返します。 |
| `SetJAxisLength(value: float) -> bool` | J軸の長さを設定します。 |
| `GetXOffsetInCurrentUnits() -> float \| None` | ファイルの現在の単位でのオフセットと軸の長さ。 |
| `SetXOffsetInCurrentUnits(value: float) -> bool` | 現在の単位でXオフセットを設定します（ファイルの現在の単位でのオフセットと軸の長さ）。 |
| `GetYOffsetInCurrentUnits() -> float \| None` | 現在の単位でYオフセットを返します。 |
| `SetYOffsetInCurrentUnits(value: float) -> bool` | 現在の単位でYオフセットを設定します。 |
| `GetIAxisLengthInCurrentUnits() -> float \| None` | 現在の単位でI軸の長さを返します。 |
| `SetIAxisLengthInCurrentUnits(value: float) -> bool` | 現在の単位でI軸の長さを設定します。 |
| `GetJAxisLengthInCurrentUnits() -> float \| None` | 現在の単位でJ軸の長さを返します。 |
| `SetJAxisLengthInCurrentUnits(value: float) -> bool` | 現在の単位でJ軸の長さを設定します。 |
| `GetAngle() -> float \| None` | 原点を中心としたマッピングの回転角（ラジアン）。 |
| `SetAngle(radians: float) -> bool` | 角度を設定します（原点を中心としたマッピングの回転角、ラジアン）。 |
| `GetRepeat() -> bool \| None` | *繰り返し*がオンかどうか。 |
| `SetRepeat(repeat: bool) -> bool` | *繰り返し*をオンまたはオフにします。 |
| `GetMirror() -> bool \| None` | *ミラー*がオンかどうか。 |
| `SetMirror(mirror: bool) -> bool` | *ミラー*をオンまたはオフにします。 |
| `GetFlip() -> bool \| None` | *反転*がオンかどうか。 |
| `SetFlip(flip: bool) -> bool` | *反転*をオンまたはオフにします。 |
| `GetMaintainAspectRatio() -> bool \| None` | *縦横比を固定*がオンかどうか。 |
| `SetMaintainAspectRatio(maintain: bool) -> bool` | *縦横比を固定*をオンまたはオフにします。 |

*グラデーションの形状タイプ（直線状、放射状、...）*

| メソッド | 説明 |
|---|---|
| `GetGeometryType() -> int \| None` | 形状タイプを返します。 |
| `SetGeometryType(type: int) -> bool` | 形状タイプを設定します。 |

*ローカル（オブジェクト相対）マッピングとワールドマッピング*

| メソッド | 説明 |
|---|---|
| `GetLocalMapping() -> bool \| None` | *ローカルマッピングを使用*がオンかどうか。 |
| `SetLocalMapping(local: bool) -> bool` | *ローカルマッピングを使用*をオンまたはオフにします。 |

継承：[`AttributesBase`](#attributesbase)のすべてのメンバー。

#### FillMappingAttributes.Frame

> **完全修飾名:** `api.FillMappingAttributes.Frame` · **継承元:** `api.Object`

ハッチング、タイル、グラデーション、イメージの面のマッピングフレーム：原点とI軸およびJ軸の終点。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Frame()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Frame(origin, iAxisEnd, jAxisEnd)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `origin` | `Point2D` | マッピングの原点。 |
| `iAxisEnd` | `Point2D` | I軸の終点（原点から）。 |
| `jAxisEnd` | `Point2D` | J軸の終点（原点から）。 |

### MarkerAttributes

> **完全修飾名:** `api.MarkerAttributes` · **継承元:** [`AttributesBase`](#attributesbase) → `api.Object`

オブジェクトの始点と終点のマーカー（矢印先端）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `MarkerAttributes(h: Handle)` | 既存のマーカー`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetBeginningMarker() -> Marker \| None` | 始点マーカーを返します。 |
| `SetBeginningMarker(marker: Marker) -> bool` | 始点マーカーを設定します。 |
| `GetEndMarker() -> Marker \| None` | 終点マーカーを返します。 |
| `SetEndMarker(marker: Marker) -> bool` | 終点マーカーを設定します。 |
| `GetBeginningMarkerVisible() -> bool \| None` | *始点マーカーを表示*がオンかどうか。 |
| `SetBeginningMarkerVisible(visible: bool) -> bool` | *始点マーカーを表示*をオンまたはオフにします。 |
| `GetEndMarkerVisible() -> bool \| None` | *終点マーカーを表示*がオンかどうか。 |
| `SetEndMarkerVisible(visible: bool) -> bool` | *終点マーカーを表示*をオンまたはオフにします。 |
| `GetByClass() -> bool \| None` | *クラス属性*がオンかどうか。 |
| `SetByClass() -> bool` | クラス属性に設定します。 |

継承：[`AttributesBase`](#attributesbase)のすべてのメンバー。

### DropShadowAttributes

> **完全修飾名:** `api.DropShadowAttributes` · **継承元:** [`AttributesBase`](#attributesbase) → `api.Object`

オブジェクトのドロップシャドウ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DropShadowAttributes(h: Handle)` | 既存のドロップシャドウ`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetEnabled() -> bool \| None` | *有効*がオンかどうか。 |
| `SetEnabled(enable: bool) -> bool` | *有効*をオンまたはオフにします。 |
| `GetData() -> DropShadow \| None` | オブジェクト固有のドロップシャドウデータ。オブジェクトにこのデータがない場合は空です。 |
| `SetData(data: DropShadow) -> bool` | データを設定します。オブジェクト固有のドロップシャドウデータ。オブジェクトにこのデータがない場合は空です。 |
| `DeleteData() -> bool` | オブジェクト固有のドロップシャドウデータを削除します（その後、オブジェクトには独自のドロップシャドウがなくなります）。 |
| `GetByClass() -> bool \| None` | *クラス属性*がオンかどうか。 |
| `SetByClass(byClass: bool) -> bool` | *クラス属性*をオンまたはオフにします。 |
| `GetColor() -> ColorRGB \| None` | GetData / SetDataを利用する便利なアクセサー。 |
| `SetColor(color: ColorRGB) -> bool` | 色を設定します（GetData / SetDataを利用する便利なアクセサー）。 |
| `GetOpacity() -> int \| None` | 不透明度を返します。 |
| `SetOpacity(opacity: int) -> bool` | 不透明度を設定します。 |

継承：[`AttributesBase`](#attributesbase)のすべてのメンバー。

### ClassAttributes

> **完全修飾名:** `api.ClassAttributes` · **継承元:** [`AttributesBase`](#attributesbase) → `api.Object`

クラス定義（`ObjectType.ClassDefinition`）：名前を付けて保存した属性設定。クラスに割り当てられたオブジェクトは、「クラス属性」に設定された各属性について、そのクラスの属性を使用します（PenAttributes、FillAttributes、MarkerAttributes、DropShadowAttributesのSetXxxByClassメソッド、および`ObjectAttributes.SetAllByClass`を参照）。クラス定義ではないハンドルから構築すると、無効なオブジェクトになります（`IsValid()` == `False`）。文字列はUTF-8です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ClassAttributes(hClassDefinition: Handle)` | 既存のクラス`hClassDefinition`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*検索と作成*

| メソッド | 説明 |
|---|---|
| `FromIndex(classIndex: int) -> ClassAttributes` *静的* | 内部インデックス`classIndex`のクラス。 |
| `FromName(name: str) -> ClassAttributes` *静的* | 名前が`name`のクラス。存在しない場合は無効なオブジェクト。 |
| `OfObject(hObject: Handle) -> ClassAttributes` *静的* | オブジェクト`hObject`のクラス。 |
| `Create(name: str) -> ClassAttributes` *静的* | 名前が`name`のクラスを作成します。その名前が使用済みの場合は既存のクラスを返します。 |
| `GetNoneClass() -> ClassAttributes` *静的* | 一般クラスを返します。 |
| `GetDimensionClass() -> ClassAttributes` *静的* | 寸法クラスを返します。 |
| `GetGuidesClass() -> ClassAttributes` *静的* | 「補助グリッド」クラスを返します（存在しない場合は作成します）。 |
| `GetDefaultClass() -> ClassAttributes` *静的* | デフォルトのクラスを返します（現在のコンテナのクラス。リセット中はプラグインオブジェクトのクラス）。 |
| `GetActiveClass() -> ClassAttributes` *静的* | アクティブクラスを返します（現在のコンテナの外にある、ファイルのアクティブクラス）。 |
| `GetMaxIndex() -> int` *静的* | 最大インデックスを返します。 |
| `ForEach(includeGuestClasses: bool, callback: callable(ClassAttributes)) -> None` *静的* | ファイルの各クラスを引数に`callback`を呼び出します（参照ファイルのゲストクラスは、`includeGuestClasses`が`True`の場合のみ）。 |
| `GetAll(includeGuestClasses: bool) -> list[ClassAttributes]` *静的* | ファイルのすべてのクラス（`includeGuestClasses`が`True`の場合は、参照ファイルのゲストクラスを含む）。 |

*識別*

| メソッド | 説明 |
|---|---|
| `GetIndex() -> int \| None` | インデックスを返します。 |
| `GetName() -> str \| None` | 名前を返します。 |
| `GetDescription() -> str \| None` | 説明を返します。 |
| `SetDescription(description: str) -> bool` | 説明を設定します。 |
| `MakeDefault() -> bool` | このクラスをアクティブクラス（新規オブジェクトのクラス）にします。 |
| `Delete() -> bool` | クラスを削除します。そのオブジェクトは`None`クラスに移動します。このオブジェクトは無効になります。 |

*オプション*

| メソッド | 説明 |
|---|---|
| `GetVisibility() -> ClassVisibility \| None` | 表示状態を返します。 |
| `SetVisibility(visibility: ClassVisibility) -> bool` | 表示状態を設定します（オブジェクトを再描画したり、表示状態をリセットしたりはしません）。 |
| `GetNonPlot() -> bool \| None` | *非出力*がオンかどうか。 |
| `SetNonPlot(nonPlot: bool) -> bool` | *非出力*をオンまたはオフにします。 |
| `GetUseAtCreation() -> bool \| None` | このクラスに作成する新規オブジェクトが、クラス属性を自動的に取得するかどうか。 |
| `SetUseAtCreation(use: bool) -> bool` | *属性を使う*をオンまたはオフにします。このクラスに作成する新規オブジェクトが、クラス属性を自動的に取得するかどうか。 |
| `GetObjectColors() -> ObjectColors \| None` | 色（クラスの色を読み書きするためにAttributesBaseをオーバーライドします）。 |
| `SetObjectColors(colors: ObjectColors) -> bool` | オブジェクトの色を設定します（色（クラスの色を読み書きするためにAttributesBaseをオーバーライドします））。 |

*線*

| メソッド | 説明 |
|---|---|
| `GetPenColors() -> ColorPair \| None` | 線の色を返します。 |
| `SetPenColors(colors: ColorPair) -> bool` | 線の色を設定します。 |
| `GetPenForeColor() -> ColorRGB \| None` | 線の前景色を返します。 |
| `SetPenForeColor(color: ColorRGB) -> bool` | 線の前景色を設定します。 |
| `GetPenBackColor() -> ColorRGB \| None` | 線の背景色を返します。 |
| `SetPenBackColor(color: ColorRGB) -> bool` | 線の背景色を設定します。 |
| `GetPenStyle() -> int \| None` | 未加工の線スタイル。値は`PenAttributes.GetStyle`と同じです。 |
| `SetPenStyle(style: int) -> bool` | 線スタイルを設定します。未加工の線スタイル。値は`PenAttributes.GetStyle`と同じです。 |
| `GetPenStyleKind() -> PenStyleKind \| None` | 線スタイルの種類を返します。 |
| `GetPenLineType() -> int \| None` | 線のラインタイプを返します。 |
| `SetPenLineType(lineTypeIndex: int) -> bool` | 線のラインタイプを設定します。 |
| `GetLineWeightMils() -> int \| None` | 線の太さをミル単位で返します。 |
| `SetLineWeightMils(mils: int) -> bool` | 線の太さをミル単位で設定します。 |
| `GetPenOpacity() -> int \| None` | 線の不透明度を返します。 |
| `SetPenOpacity(opacity: int) -> bool` | 線の不透明度を設定します。 |

*面*

| メソッド | 説明 |
|---|---|
| `GetFillColors() -> ColorPair \| None` | 面の色を返します。 |
| `SetFillColors(colors: ColorPair) -> bool` | 面の色を設定します。 |
| `GetFillForeColor() -> ColorRGB \| None` | 面の前景色を返します。 |
| `SetFillForeColor(color: ColorRGB) -> bool` | 面の前景色を設定します。 |
| `GetFillBackColor() -> ColorRGB \| None` | 面の背景色を返します。 |
| `SetFillBackColor(color: ColorRGB) -> bool` | 面の背景色を設定します。 |
| `GetFillStyle() -> int \| None` | 未加工の面スタイル。値は`FillAttributes.GetStyle`と同じです。 |
| `SetFillStyle(style: int) -> bool` | 面スタイルを設定します。未加工の面スタイル。値は`FillAttributes.GetStyle`と同じです。 |
| `GetFillType() -> FillType \| None` | 面の種類を返します。 |
| `GetFillResource() -> int \| None` | 面のリソースを返します。 |
| `SetFillResource(resourceIndex: int) -> bool` | 面のリソースを設定します。 |
| `GetFillOpacity() -> int \| None` | 面の不透明度を返します。 |
| `SetFillOpacity(opacity: int) -> bool` | 面の不透明度を設定します。 |

*線と面の不透明度をまとめて扱う*

| メソッド | 説明 |
|---|---|
| `SetOpacity(opacity: int) -> bool` | 不透明度を設定します。 |
| `GetBeginningMarker() -> Marker \| None` | マーカー。クラスはマーカースタイルのみを保存し、`Marker.visible`は使用しません。 |
| `SetBeginningMarker(marker: Marker) -> bool` | 始点マーカーを設定します。マーカー。クラスはマーカースタイルのみを保存し、`Marker.visible`は使用しません。 |
| `GetEndMarker() -> Marker \| None` | 終点マーカーを返します。 |
| `SetEndMarker(marker: Marker) -> bool` | 終点マーカーを設定します。 |
| `GetDropShadow() -> DropShadow \| None` | ドロップシャドウ。`DropShadow.useDropShadow`でクラスのドロップシャドウを有効にします。 |
| `SetDropShadow(data: DropShadow) -> bool` | ドロップシャドウを設定します。ドロップシャドウ。`DropShadow.useDropShadow`でクラスのドロップシャドウを有効にします。 |
| `GetUseTextures() -> bool \| None` | オブジェクトの作成時にクラスのテクスチャを適用するかどうか。 |
| `SetUseTextures(use: bool) -> bool` | 「テクスチャ」タブの*属性を使う*をオンまたはオフにします。 |
| `GetGeneralTexture() -> int \| None` | オブジェクトや構成要素のテクスチャを返します。 |
| `SetGeneralTexture(texture: int) -> bool` | オブジェクトや構成要素のテクスチャを設定します。 |
| `GetWallTextures() -> WallTextures \| None` | 壁のテクスチャを返します。 |
| `SetWallTextures(textures: WallTextures) -> bool` | 壁のテクスチャを設定します。 |
| `GetRoofTextures() -> RoofTextures \| None` | 屋根のテクスチャを返します。 |
| `SetRoofTextures(textures: RoofTextures) -> bool` | 屋根のテクスチャを設定します。 |

*文字スタイル*

| メソッド | 説明 |
|---|---|
| `GetUseTextStyle() -> bool \| None` | 「文字スタイル」タブの*属性を使う*がオンかどうか。 |
| `SetUseTextStyle(use: bool) -> bool` | 「文字スタイル」タブの*属性を使う*をオンまたはオフにします。 |
| `GetTextStyle() -> int \| None` | 文字スタイルを返します。 |
| `SetTextStyle(textStyle: int) -> bool` | 文字スタイルを設定します。 |

*オブジェクト*

| メソッド | 説明 |
|---|---|
| `AssignTo(hObject: Handle, useClassAttributes: bool = False, descendIntoGroups: bool = True) -> bool` | オブジェクトをこのクラスに割り当てます。`useClassAttributes`が`True`の場合、オブジェクトのすべての属性を「クラス属性」に設定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: ClassAttributes) -> bool` | `a == b`：両方のオブジェクトが同じクラスを参照している場合はTrue。 |
| `!=` | `__ne__(o: ClassAttributes) -> bool` | `a != b`：オブジェクトが異なる図面オブジェクトを参照している場合はTrue。 |

継承：[`AttributesBase`](#attributesbase)のすべてのメンバー。

### ObjectAttributes

> **完全修飾名:** `api.ObjectAttributes` · **継承元:** [`AttributesBase`](#attributesbase) → `api.Object`

オブジェクトのすべてのグラフィック属性。このAPIには、意図的にジオメトリを含めていません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ObjectAttributes(h: Handle)` | 既存のオブジェクト`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Pen() -> PenAttributes` | オブジェクトのペン属性（線）。 |
| `Fill() -> FillAttributes` | オブジェクトの面属性。 |
| `FillMapping() -> FillMappingAttributes` | オブジェクトの面のマッピング（ハッチング、タイル、グラデーション、イメージの面の配置）。 |
| `Markers() -> MarkerAttributes` | オブジェクトの始点と終点のマーカー。 |
| `DropShadow() -> DropShadowAttributes` | オブジェクトのドロップシャドウ。 |

*オブジェクトのクラス*

| メソッド | 説明 |
|---|---|
| `GetClass() -> ClassAttributes` | クラスを返します。 |
| `SetClass(theClass: ClassAttributes, descendIntoGroups: bool = True) -> bool` | クラスを設定します。 |
| `SetAllByClass() -> bool` | 対応するすべての属性を「クラス属性」に設定します。対象は線と面の色およびスタイル、線の太さ、不透明度、マーカー、ドロップシャドウです。その後、オブジェクトは所属クラスの属性で表示されます。 |
| `GetOpacity() -> int \| None` | 共通の不透明度（線と面で同じ値）。 |
| `SetOpacity(opacity: int) -> bool` | 不透明度を設定します（共通の不透明度（線と面で同じ値））。 |
| `GetOpacityByClass() -> bool \| None` | *不透明度のクラス属性*がオンかどうか。 |
| `SetOpacityByClass() -> bool` | 不透明度をクラス属性に設定します。 |
| `ApplyTo(target: Handle) -> bool` | 色、線と面のスタイル、線の太さ、不透明度、マーカー、ドロップシャドウを対象オブジェクトにコピーし、その後クラス属性フラグを適用します（値の設定によって、対応するクラス属性フラグがリセットされる場合があります）。 |

継承：[`AttributesBase`](#attributesbase)のすべてのメンバー。

<a id="enumerations"></a>

## 列挙型

### PenStyleKind

> **完全修飾名:** `api.PenStyleKind` · **種類:** `IntEnum`

未加工の線スタイル値の分類。

- 0 — なし
- 1, 2 — カラー
- > 2 — 従来のピクセル模様
- < 0 — ラインタイプリソース。値は-（ラインタイプの内部インデックス）

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` |  |
| `Solid` | `1` |  |
| `Pattern` | `2` |  |
| `SimpleLineType` | `3` |  |
| `ComplexLineType` | `4` |  |
| `Unknown` | `5` |  |

### FillType

> **完全修飾名:** `api.FillType` · **種類:** `IntEnum`

オブジェクトの面の種類。

| メンバー | 値 | 説明 |
|---|---|---|
| `Unknown` | `-1` |  |
| `None_` | `1` |  |
| `Solid` | `2` |  |
| `Pattern` | `3` |  |
| `Hatch` | `4` |  |
| `Tile` | `5` |  |
| `Gradient` | `6` |  |
| `Image` | `7` |  |
| `Class` | `8` |  |

### MarkerShape

> **完全修飾名:** `api.MarkerShape` · **種類:** `IntEnum`

マーカー（矢印先端）

| メンバー | 値 | 説明 |
|---|---|---|
| `Arrow` | `0` |  |
| `ConcaveCurvedArrow` | `1` |  |
| `Circle` | `2` |  |
| `DimSlash` | `3` |  |
| `DimCross` | `4` |  |
| `Lasso` | `5` |  |
| `Hexagon` | `6` |  |
| `VShaped` | `7` |  |
| `Cone` | `8` |  |
| `TaperedVShaped` | `9` |  |
| `SShaped` | `10` |  |
| `Rectangle` | `11` |  |
| `DoubleLine` | `12` |  |

### MarkerFill

> **完全修飾名:** `api.MarkerFill` · **種類:** `IntEnum`

以下のマーカースタイル列挙型（MarkerFill、MarkerBase、MarkerHalfTick）は、ビット単位のORで単一の16ビットスタイル値にまとめられるよう、あらかじめシフトした値を使用します（`Marker.GetStyleValue`を参照）。整数ではなく列挙型の名前を使用してください。

| メンバー | 値 | 説明 |
|---|---|---|
| `LineColor` | `0` |  |
| `White` | `128` |  |
| `NoFill` | `256` |  |

### MarkerBase

> **完全修飾名:** `api.MarkerBase` · **種類:** `IntEnum`

マーカーの底辺の形状（シフト済みのビット値。`Marker.GetStyleValue`を参照）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Flat` | `0` |  |
| `Open` | `1024` |  |
| `Angle` | `2048` |  |
| `Arc` | `3072` |  |

### MarkerHalfTick

> **完全修飾名:** `api.MarkerHalfTick` · **種類:** `IntEnum`

マーカー全体、またはその左半分か右半分のみ（シフト済みのビット値。`Marker.GetStyleValue`を参照）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Full` | `0` |  |
| `Left` | `16384` |  |
| `Right` | `24576` |  |

### MarkerThicknessBasis

> **完全修飾名:** `api.MarkerThicknessBasis` · **種類:** `IntEnum`

マーカーの線の太さが従う基準。

| メンバー | 値 | 説明 |
|---|---|---|
| `LineThickness` | `0` |  |
| `DimThickness` | `1` |  |
| `Custom` | `2` |  |

### MarkerThicknessUnits

> **完全修飾名:** `api.MarkerThicknessUnits` · **種類:** `IntEnum`

カスタムマーカーの線の太さの単位。

| メンバー | 値 | 説明 |
|---|---|---|
| `Mils` | `0` |  |
| `Points` | `16` |  |
| `Millimeters` | `32` |  |

### DropShadowUnits

> **完全修飾名:** `api.DropShadowUnits` · **種類:** `IntEnum`

ドロップシャドウ

| メンバー | 値 | 説明 |
|---|---|---|
| `Page` | `0` |  |
| `World` | `1` |  |

### ClassVisibility

> **完全修飾名:** `api.ClassVisibility` · **種類:** `IntEnum`

クラス

| メンバー | 値 | 説明 |
|---|---|---|
| `Invisible` | `-1` |  |
| `Visible` | `0` |  |
| `Grayed` | `2` |  |

### ObjectType

> **完全修飾名:** `api.ObjectType` · **種類:** `IntEnum`

オブジェクトの種類。`Document.GetObjectType`および`AttributesBase.GetObjectType`が返します。この一覧はVectorworksのオブジェクトタイプコードに対応しており、意図的にすべてを網羅しています。現在、型付きクラスがあるのはその一部のみです（下記の対応を参照）。それ以外の値はすべて不透明です。種類でオブジェクトを識別し、その後、未加工のHandleとして操作してください。

- Line → Line2DObject
- Box → RectangleObject
- RoundedRectangle → RoundRectObject
- Arc / QuarterArc → ArcObject（円全体の円弧は、`ArcObject.Is`を通じてCircleObjectでもあります）
- Polygon / FreehandPolygon → PolygonObject
- Polyline → PolylineObject
- Locus → Locus2DObject
- Layer → Layer
- ClassDefinition → ClassAttributes

| メンバー | 値 | 説明 |
|---|---|---|
| `Invalid` | `-1` |  |
| `Term` | `0` |  |
| `Line` | `2` |  |
| `Box` | `3` |  |
| `Oval` | `4` |  |
| `Polygon` | `5` |  |
| `Arc` | `6` |  |
| `DimUnitSettings` | `7` |  |
| `FreehandPolygon` | `8` |  |
| `Locus3D` | `9` |  |
| `Text` | `10` |  |
| `Group` | `11` |  |
| `QuarterArc` | `12` |  |
| `RoundedRectangle` | `13` |  |
| `Paint` | `14` |  |
| `Symbol` | `15` |  |
| `SymbolDefinition` | `16` |  |
| `Locus` | `17` |  |
| `Worksheet` | `18` |  |
| `BuildingMaterial` | `19` |  |
| `Polyline` | `21` |  |
| `Extrude` | `24` |  |
| `Polygon3D` | `25` |  |
| `SlabDrain` | `26` |  |
| `SlabDrainValley` | `27` |  |
| `SlabSlopeValley` | `28` |  |
| `LayerReference` | `29` |  |
| `DashPatterns` | `30` |  |
| `Layer` | `31` |  |
| `Header` | `32` |  |
| `RefList` | `33` |  |
| `Sweep` | `34` |  |
| `ClassList` | `35` |  |
| `ViewportStyle` | `36` |  |
| `DataVisualization` | `37` |  |
| `MultiExtrude` | `38` |  |
| `DimensionStandard` | `39` |  |
| `Mesh` | `40` |  |
| `SavedView` | `43` |  |
| `RenderSpec` | `44` |  |
| `Eps` | `45` |  |
| `Format` | `47` |  |
| `Record` | `48` |  |
| `ToolCommand` | `49` |  |
| `SymbolList` | `54` |  |
| `WorksheetImage` | `56` |  |
| `Data` | `57` |  |
| `RecordLink` | `58` |  |
| `WorksheetDatabase` | `60` |  |
| `LeaderList` | `62` |  |
| `Dimension` | `63` |  |
| `HatchContainer` | `65` |  |
| `HatchDefinition` | `66` |  |
| `Bsp` | `67` |  |
| `Wall` | `68` |  |
| `InnerLines` | `69` |  |
| `SlabDrainageSettings` | `70` |  |
| `Slab` | `71` |  |
| `PenSpace` | `73` |  |
| `FontTable` | `74` |  |
| `StyleRun` | `75` |  |
| `UserData` | `76` |  |
| `WorkingPlane` | `77` |  |
| `WPlaneList` | `78` |  |
| `PixelPatternList` | `79` |  |
| `ColorPalette` | `80` |  |
| `Light` | `81` |  |
| `RoofEdge` | `82` |  |
| `RoofContainer` | `83` |  |
| `CSGTree` | `84` |  |
| `BoundaryRep` | `85` |  |
| `Parametric` | `86` |  |
| `RoofAdorner` | `87` |  |
| `Subscribe` | `88` |  |
| `ObsoleteRoundWall` | `89` |  |
| `UndoPlaceholder` | `90` |  |
| `TextureSpace` | `91` |  |
| `Folder` | `92` |  |
| `TextureBitmap` | `93` |  |
| `ClassDefinition` | `94` |  |
| `Solid` | `95` |  |
| `LineTypeDefinition` | `96` |  |
| `Texture` | `97` |  |
| `ADSymbolDefinitionHandler` | `98` |  |
| `ADSymbolHandler` | `99` |  |
| `SlabEdge` | `100` |  |
| `DropShadow` | `101` |  |
| `RoofStyle` | `102` |  |
| `CurtainWallFrame` | `103` |  |
| `CurtainWallPanel` | `104` |  |
| `CurtainWallGrid` | `105` |  |
| `RenderStyle` | `106` |  |
| `SlabStyle` | `107` |  |
| `TileDefinition` | `108` |  |
| `TextStyle` | `109` |  |
| `Constraint` | `110` |  |
| `PieceWiseNurbsCurve` | `111` |  |
| `CorePrintInfo` | `112` |  |
| `NurbsSurface` | `113` |  |
| `CompositeSurface` | `114` |  |
| `RenderBackground` | `115` |  |
| `PolyBreak` | `116` |  |
| `BatchRenderJob` | `117` |  |
| `BatchRenderJobList` | `118` |  |
| `ImageDefinition` | `119` |  |
| `GradientDefinition` | `120` |  |
| `FillSpace` | `121` |  |
| `Viewport` | `122` |  |
| `ArtRWStyle` | `123` |  |
| `Association` | `124` |  |
| `AuxMarker` | `125` |  |
| `GeoReference` | `126` |  |
| `WallStyle` | `127` |  |

<a id="module-constants"></a>

## モジュール定数

| 定数 | 型 | 値 | 説明 |
|---|---|---|---|
| `api.kMaxOpacity` | `int` | `100` | 最大不透明度（不透明度の範囲は0から100）。 |

---

[一覧に戻る](README.md) · [先頭に戻る](#attributes--graphic-attributes-and-classes)
