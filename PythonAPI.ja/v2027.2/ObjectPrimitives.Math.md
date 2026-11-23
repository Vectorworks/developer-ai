[English](../../PythonAPI/v2027.2/ObjectPrimitives.Math.md) • [Deutsch](../../PythonAPI.de/v2027.2/ObjectPrimitives.Math.md) • **日本語**

<a id="math--standalone-2d-and-3d-math-apimath"></a>

# Math — 独立した2Dおよび3Dの数学演算（`api.Math`）

> **Pythonモジュール:** `api.Math` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

`api.Math`は、図面を必要としない独立した数学的な値のサブモジュールです（`from api.Math import Point2D`でインポートするか、`api.Math.Point2D`を使用します）。点とベクトル（`Point2D` = `Vector2D`、`Point3D` = `Vector3D`）、変換（`Transform2D`、`Transform3D`）、矩形（`Rect2D`、`RotatedRect2D`）、直線（`Line2D`、`Line3D`）、平面（`Plane3D`）、円（`Circle2D`）、円弧（`Arc2D`）、多角形（`Polygon2D`。`PolyVertex`値で構成）に加え、ユーティリティ関数と定数を提供します。

すべての角度は、正のX軸から反時計回りに測ったラジアンです。返された値を変更しても図面オブジェクトは変更されません。値をオブジェクトのセッターに渡し直してください。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [Math.Point2D](#mathpoint2d)
  - [Math.Transform2D](#mathtransform2d)
  - [Math.Rect2D](#mathrect2d)
  - [Math.RotatedRect2D](#mathrotatedrect2d)
  - [Math.Line2D](#mathline2d)
    - [Math.Line2D.Intersection](#mathline2dintersection)
  - [Math.Circle2D](#mathcircle2d)
  - [Math.Arc2D](#matharc2d)
  - [Math.PolyVertex](#mathpolyvertex)
  - [Math.Polygon2D](#mathpolygon2d)
    - [Math.Polygon2D.CurveLocation](#mathpolygon2dcurvelocation)
  - [Math.Point3D](#mathpoint3d)
  - [Math.Transform3D](#mathtransform3d)
  - [Math.Line3D](#mathline3d)
  - [Math.Plane3D](#mathplane3d)
- [列挙型](#enumerations)
  - [Math.VertexType](#mathvertextype)
  - [Math.OffsetJoin](#mathoffsetjoin)
- [モジュール関数](#module-functions)
- [モジュール定数](#module-constants)
- [別名と暗黙の変換](#aliases-and-implicit-conversions)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`Math.Point2D`](#mathpoint2d) | クラス |  | 2D点／ベクトル。 |
| [`Math.Transform2D`](#mathtransform2d) | クラス |  | 2Dアフィン変換。 |
| [`Math.Rect2D`](#mathrect2d) | クラス |  | 座標軸に平行な矩形。 |
| [`Math.RotatedRect2D`](#mathrotatedrect2d) | クラス |  | 回転可能な矩形：コーナー、幅方向の辺の方向、および二つの辺の長さ。 |
| [`Math.Line2D`](#mathline2d) | クラス |  | `start`から`end`への線分。 |
| [`Math.Line2D.Intersection`](#mathline2dintersection) | クラス（入れ子） |  | 無限直線同士の交点。 |
| [`Math.Circle2D`](#mathcircle2d) | クラス |  | 円。 |
| [`Math.Arc2D`](#matharc2d) | クラス |  | 円弧。 |
| [`Math.PolyVertex`](#mathpolyvertex) | クラス |  | `Polygon2D`の一つの頂点：座標、頂点タイプ、円弧半径（半径頂点）、およびその頂点を始点とする辺の表示状態。 |
| [`Math.Polygon2D`](#mathpolygon2d) | クラス |  | 多角形または曲線の頂点リスト。 |
| [`Math.Polygon2D.CurveLocation`](#mathpolygon2dcurvelocation) | クラス（入れ子） |  | 多角形の曲線状の外側パスを一時的にNURBSで表現したときの、点と区間固有のパラメータ。 |
| [`Math.Point3D`](#mathpoint3d) | クラス |  | Pythonが所有する、ワールド座標のミリメートル単位の3D点／ベクトル。 |
| [`Math.Transform3D`](#mathtransform3d) | クラス |  | Pythonが所有する、列ベクトルに作用する3Dアフィン行列。A * BはBを先に適用します。 |
| [`Math.Line3D`](#mathline3d) | クラス |  | Pythonが所有する、ワールド座標のミリメートル単位のstartからendへの3D線分。 |
| [`Math.Plane3D`](#mathplane3d) | クラス |  | Pythonが所有する、単位法線を持つ向き付きの無限平面。 |
| [`Math.VertexType`](#mathvertextype) | IntEnum |  | 多角形状の頂点の種類。 |
| [`Math.OffsetJoin`](#mathoffsetjoin) | IntEnum |  | 多角形のオフセットのコーナースタイル（`Polygon2D.Offset`）。 |
| [モジュール関数](#module-functions) | 関数 | | `AngleDelta`, `AnglesAreEqual`, `AreEqual`, `Clamp`, `DegToRad`, `IsBetween`, `IsGreater`, `IsLess`, `IsZero`, `Lerp`, `NormalizeAngle`, `NormalizeAngleSigned`, `RadToDeg`, `Sign` |
| [モジュール定数](#module-constants) | 定数 | | `kPi`, `kTwoPi`, `kHalfPi`, `kEpsilon`, `kAngleEpsilon` |

<a id="classes"></a>

## クラス

### Math.Point2D

> **完全修飾名:** `api.Math.Point2D` · **継承元:** `api.Object`

2D点／ベクトル。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Point2D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Point2D(inX: float, inY: float)` | 座標`inX`、`inY`を持つ点／ベクトル。 |
| `Point2D(pt: Point2D)` | `api.Point2D`レコードを変換します。 |
| `Point2D(x=..., y=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`Point2D(x=...)`。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `FromPolar(length: float, angle: float) -> Math.Point2D` *静的* | 長さ`length`、方向`angle`（ラジアン）のベクトル。 |
| `UnitFromAngle(angle: float) -> Math.Point2D` *静的* | 方向`angle`（ラジアン）の単位ベクトル。 |

*算術*

| メソッド | 説明 |
|---|---|
| `IsEqual(o: Math.Point2D, tolerance: float = 1e-09) -> bool` | 両方の座標が`o`と`tolerance`以内で一致する場合はTrue。 |
| `IsZero(tolerance: float = 1e-09) -> bool` | ベクトルの長さがゼロから`tolerance`以内にある場合はTrue。 |

*ベクトル演算*

| メソッド | 説明 |
|---|---|
| `Dot(o: Math.Point2D) -> float` | `o`との内積。 |
| `Cross(o: Math.Point2D) -> float` | `o`との外積（3D外積のZ成分）。 |
| `LengthSquared() -> float` | ベクトルの長さの二乗（`Length()`より低コスト）。 |
| `Length() -> float` | ベクトルの長さ（原点からの距離）。 |
| `Angle() -> float` | ベクトルの方向角。範囲は(-pi, pi]。 |
| `Normalized() -> Math.Point2D` | 同じ方向の単位ベクトル（新しい値。ゼロベクトルはゼロのまま）。 |
| `Normalize() -> Math.Point2D` | このベクトル自体の長さを単位長さに調整し、それを返します。 |
| `WithLength(length: float) -> Math.Point2D` | 同じ方向で長さ`length`のベクトル。 |
| `Perpendicular() -> Math.Point2D` | 反時計回りに90度回転したベクトル。 |
| `PerpendicularCW() -> Math.Point2D` | 時計回りに90度回転したベクトル。 |
| `Rotated(angle: float) -> Math.Point2D` | 原点を中心に`angle`ラジアン回転したベクトル。 |
| `Rotated(angle: float, center: Math.Point2D) -> Math.Point2D` | `angle`ラジアンだけ`center`を中心に回転した点。 |
| `Scaled(sx: float, sy: float, center: Math.Point2D = Math.Point2D(0.0, 0.0)) -> Math.Point2D` | `sx` / `sy`で`center`を基準に拡大縮小した点。 |

*点の操作*

| メソッド | 説明 |
|---|---|
| `DistanceSquaredTo(o: Math.Point2D) -> float` | `o`までの距離の二乗。 |
| `DistanceTo(o: Math.Point2D) -> float` | `o`までの距離。 |
| `AngleTo(o: Math.Point2D) -> float` | この点から`o`への方向の角度（ラジアン）。 |
| `MidPoint(o: Math.Point2D) -> Math.Point2D` | この点と`o`の中間の点。 |
| `Lerp(o: Math.Point2D, t: float) -> Math.Point2D` | `o`に向かう線形補間。`t` = 0ではこの点、1では`o`を返します。 |
| `AngleBetween(o: Math.Point2D) -> float` | このベクトルから`o`への符号付き角度。範囲は(-pi, pi]で、正は反時計回りです。 |
| `IsParallel(o: Math.Point2D, angleTolerance: float = 1e-09) -> bool` | ベクトルが`angleTolerance`以内で平行（同方向または反対方向）の場合はTrue。 |
| `IsPerpendicular(o: Math.Point2D, angleTolerance: float = 1e-09) -> bool` | ベクトルが`angleTolerance`以内で垂直の場合はTrue。 |
| `Orientation(a: Math.Point2D, b: Math.Point2D, c: Math.Point2D) -> float` *静的* | `c`が`a`から`b`への直線の左側にあれば> 0、右側にあれば< 0、同一直線上にあれば0を返します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `+` | `__add__(o: Math.Point2D) -> Math.Point2D` | `a + b`：二つの値の和。 |
| `-` | `__sub__(o: Math.Point2D) -> Math.Point2D` | `a - b`：二つの値の差。 |
| `- (unary)` | `__neg__() -> Math.Point2D` | `-a`：符号を反転した値。 |
| `*` | `__mul__(s: float) -> Math.Point2D` | `a * s`：スカラーを乗じた値。 |
| `/` | `__truediv__(s: float) -> Math.Point2D` | `a / s`：スカラーで割った値。 |
| `+=` | `__iadd__(o: Math.Point2D) -> Math.Point2D` | `a += b`：自身にもう一方の値を加算します。 |
| `-=` | `__isub__(o: Math.Point2D) -> Math.Point2D` | `a -= b`：自身からもう一方の値を減算します。 |
| `*=` | `__imul__(s: float) -> Math.Point2D` | `a *= s`：自身にスカラーを乗じます。 |
| `/=` | `__itruediv__(s: float) -> Math.Point2D` | `a /= s`：自身をスカラーで割ります。 |
| `==` | `__eq__(o: Math.Point2D) -> bool` | `a == b`：二つの値が等しい場合はTrue。完全一致の比較です。許容差に基づく比較にはIsEqualを使用してください。 |
| `!=` | `__ne__(o: Math.Point2D) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |
| `* (reflected)` | `__rmul__(s: float) -> Math.Point2D` | `s * a`：スカラーを乗じた値。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `x` | `float` | X座標。 |
| `y` | `float` | Y座標。 |

### Math.Transform2D

> **完全修飾名:** `api.Math.Transform2D` · **継承元:** `api.Object`

2Dアフィン変換。

```text
| a  b  tx |   | x |
| c  d  ty | * | y |
| 0  0  1  |   | 1 |
```

合成'A * B'はBを先に適用し、その後Aを適用します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Transform2D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Transform2D(inA: float, inB: float, inC: float, inD: float, inTx: float, inTy: float)` | (x, y)を(`inA`*x + `inB`*y + `inTx`, `inC`*x + `inD`*y + `inTy`)に写す変換。 |
| `Transform2D(a=..., b=..., tx=..., c=..., d=..., ty=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`Transform2D(a=...)`。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Identity() -> Math.Transform2D` *静的* | 恒等変換。 |
| `Translation(dx: float, dy: float) -> Math.Transform2D` *静的* | `dx`、`dy`による平行移動。 |
| `Translation(v: Math.Point2D) -> Math.Transform2D` *静的* | ベクトル`v`による平行移動。 |
| `Rotation(angle: float) -> Math.Transform2D` *静的* | 原点を中心とした`angle`ラジアンの回転。 |
| `Rotation(angle: float, center: Math.Point2D) -> Math.Transform2D` *静的* | `angle`ラジアンだけ`center`を中心に回転する変換。 |
| `Scale(sx: float, sy: float) -> Math.Transform2D` *静的* | 原点を中心とした`sx` / `sy`による拡大縮小。 |
| `Scale(sx: float, sy: float, center: Math.Point2D) -> Math.Transform2D` *静的* | `sx` / `sy`で`center`を中心に拡大縮小する変換。 |
| `Mirror(p1: Math.Point2D, p2: Math.Point2D) -> Math.Transform2D` *静的* | p1とp2を通る無限直線に対するミラー反転。 |
| `FromAxes(origin: Math.Point2D, xAxis: Math.Point2D, yAxis: Math.Point2D) -> Math.Transform2D` *静的* | 単位X/Y軸を`xAxis`/`yAxis`に、原点を`origin`に写します。 |
| `Then(next: Math.Transform2D) -> Math.Transform2D` | この変換を先に適用し、その後`next`を適用する変換。 |
| `Apply(p: Math.Point2D) -> Math.Point2D` | 点`p`を変換します（平行移動を含む）。 |
| `ApplyToVector(v: Math.Point2D) -> Math.Point2D` | ベクトル`v`を変換します（平行移動を無視）。 |
| `Determinant() -> float` | 線形部分の行列式（ミラー反転する変換では負）。 |
| `IsInvertible(tolerance: float = 1e-09) -> bool` | 行列式がゼロでない場合はTrue（許容差`tolerance`で判定）。 |
| `Inverse() -> Math.Transform2D \| None` | 逆変換。変換を反転できない場合は`None`。 |
| `GetTranslation() -> Math.Point2D` | 平行移動を返します。 |
| `SetTranslation(v: Math.Point2D) -> None` | 平行移動を設定します。 |
| `GetRotation() -> float` | 回転角を返します（X軸の回転）。 |
| `GetScaleX() -> float` | X方向の拡大縮小率を返します。 |
| `GetScaleY() -> float` | Y方向の拡大縮小率を返します（ミラー反転時は負）。 |
| `IsMirrored() -> bool` | 変換がミラー反転を行う場合はTrue（行列式が負）。 |
| `IsOrthogonal(tolerance: float = 1e-09) -> bool` | 回転と軸に沿った均等／不均等の拡大縮小のみ（せん断なし）。 |
| `IsIdentity(tolerance: float = 1e-09) -> bool` | 変換が`tolerance`以内で恒等変換の場合はTrue。 |
| `IsEqual(o: Math.Transform2D, tolerance: float = 1e-09) -> bool` | すべての係数が`o`と`tolerance`以内で一致する場合はTrue。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `*` | `__mul__(o: Math.Transform2D) -> Math.Transform2D` | `A * B`：合成変換（Bを先に適用し、その後Aを適用）。 |
| `*=` | `__imul__(o: Math.Transform2D) -> Math.Transform2D` | `A *= B`：この変換自体にもう一方の変換を合成します。 |
| `()` | `__call__(p: Math.Point2D) -> Math.Point2D` | `T(p)`：点に変換を適用します（`Apply`と同じ）。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `a` | `float` | 行列の1行1列。 |
| `b` | `float` | 行列の1行2列。 |
| `tx` | `float` | X方向の平行移動。 |
| `c` | `float` | 行列の2行1列。 |
| `d` | `float` | 行列の2行2列。 |
| `ty` | `float` | Y方向の平行移動。 |

### Math.Rect2D

> **完全修飾名:** `api.Math.Rect2D` · **継承元:** `api.Object`

座標軸に平行な矩形。Yは上方向に増加します：top >= bottom。デフォルトで構築された矩形は空であり、点を追加すると拡大します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Rect2D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Rect2D(inLeft: float, inTop: float, inRight: float, inBottom: float)` | 指定した辺を持つ矩形（Yは上方向に増加：top >= bottom）。 |
| `Rect2D(p1: Math.Point2D, p2: Math.Point2D)` | 二つのコーナーの点`p1`と`p2`を含む最小の矩形。 |
| `Rect2D(left=..., bottom=..., right=..., top=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`Rect2D(left=...)`。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `FromCenter(center: Math.Point2D, width: float, height: float) -> Math.Rect2D` *静的* | サイズが`width` x `height`で、`center`を中心とする矩形。 |
| `IsEmpty() -> bool` | 空の矩形の場合はTrue（まだ点が追加されていない）。 |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | 空であるか、幅または高さがゼロ。 |
| `Width() -> float` | 幅（空の矩形では0）。 |
| `Height() -> float` | 高さ（空の矩形では0）。 |
| `Area() -> float` | 面積。 |
| `Perimeter() -> float` | 周長。 |
| `Diagonal() -> float` | 対角線の長さ。 |
| `Center() -> Math.Point2D` | 中心点。 |
| `TopLeft() -> Math.Point2D` | 左上のコーナー。 |
| `TopRight() -> Math.Point2D` | 右上のコーナー。 |
| `BottomLeft() -> Math.Point2D` | 左下のコーナー。 |
| `BottomRight() -> Math.Point2D` | 右下のコーナー。 |
| `CenterLeft() -> Math.Point2D` | 左辺の中点。 |
| `CenterRight() -> Math.Point2D` | 右辺の中点。 |
| `CenterTop() -> Math.Point2D` | 上辺の中点。 |
| `CenterBottom() -> Math.Point2D` | 下辺の中点。 |
| `Corners() -> tuple[Math.Point2D * 4]` | 左下のコーナーから反時計回りに並んだ四つのコーナー。 |
| `FromPoints(points: list[Math.Point2D]) -> Math.Rect2D` *静的* | すべての`points`を含む最小の矩形（空のリストでは空）。 |

*拡張*

| メソッド | 説明 |
|---|---|
| `Add(p: Math.Point2D) -> Math.Rect2D` | 点`p`を含むように矩形自体を拡張し、それを返します。 |
| `Add(r: Math.Rect2D) -> Math.Rect2D` | 矩形`r`を含むように矩形自体を拡張し、それを返します。 |
| `Union(r: Math.Rect2D) -> Math.Rect2D` | この矩形と`r`を含む最小の矩形（新しい値）。 |
| `Intersection(r: Math.Rect2D) -> Math.Rect2D` | この矩形と`r`の重なり（重ならない場合は空）。 |
| `Inflated(dx: float, dy: float) -> Math.Rect2D` | 左右に`dx`、上下に`dy`だけ拡張します（負の値の場合は縮小）。 |
| `Offset(v: Math.Point2D) -> Math.Rect2D` | ベクトル`v`だけ移動した矩形。 |
| `Transformed(t: Math.Transform2D) -> Math.Rect2D` | 変換したコーナーを囲む境界。 |

*問い合わせ*

| メソッド | 説明 |
|---|---|
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | 点`p`が矩形の内側または境界上にある場合はTrue。 |
| `Contains(r: Math.Rect2D, tolerance: float = 1e-09) -> bool` | 矩形`r`がこの矩形の完全に内側にある場合はTrue。 |
| `Intersects(r: Math.Rect2D, tolerance: float = 1e-09) -> bool` | 矩形同士が重なるか接する場合はTrue。 |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | 矩形内で`p`に最も近い点（内側にある場合は`p`自身）。 |
| `DistanceTo(p: Math.Point2D) -> float` | `p`から矩形までの距離（内側は0）。 |
| `IsEqual(r: Math.Rect2D, tolerance: float = 1e-09) -> bool` | 四つの辺すべてが`r`と`tolerance`以内で一致する場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `left` | `float` | 左辺（最小のX）。 |
| `bottom` | `float` | 下辺（最小のY）。 |
| `right` | `float` | 右辺（最大のX）。 |
| `top` | `float` | 上辺（最大のY）。 |

### Math.RotatedRect2D

> **完全修飾名:** `api.Math.RotatedRect2D` · **継承元:** `api.Object`

回転可能な矩形：コーナー、幅方向の辺の方向、および二つの辺の長さ。Vectorworksは四角形と角丸四角形をこの形式で保存します。コーナー（幅と高さが正の場合は反時計回り）：origin、origin + dir*width、origin + dir*width + perp*height、origin + perp*height。ここでperpは、`direction`を反時計回りに90度回転したものです。幅または高さが負の場合は、反対方向に伸びます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RotatedRect2D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `RotatedRect2D(inOrigin: Math.Point2D, inDirection: Math.Point2D, inWidth: float, inHeight: float)` | コーナー`inOrigin`、幅方向の辺の方向`inDirection`、辺の長さ`inWidth`、`inHeight`を持つ矩形。 |
| `RotatedRect2D(r: Math.Rect2D)` | `r`に等しい、回転していない矩形。 |
| `RotatedRect2D(origin=..., direction=..., width=..., height=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`RotatedRect2D(origin=...)`。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `FromCenter(center: Math.Point2D, inWidth: float, inHeight: float, angle: float = 0.0) -> Math.RotatedRect2D` *静的* | サイズが`inWidth` x `inHeight`で、`center`を中心とし、`angle`ラジアン回転した矩形。 |
| `Angle() -> float` | 幅方向の辺の回転角（ラジアン）。 |
| `WidthVector() -> Math.Point2D` | 幅方向の辺に沿ったベクトル（`direction * width`）。 |
| `HeightVector() -> Math.Point2D` | 高さ方向の辺に沿ったベクトル（幅方向の辺に垂直、長さ`height`）。 |
| `Area() -> float` | 面積。 |
| `Perimeter() -> float` | 周長。 |
| `Center() -> Math.Point2D` | 中心点。 |
| `IsAxisAligned(angleTolerance: float = 1e-09) -> bool` | 矩形が回転していない場合はTrue（`angleTolerance`以内）。 |
| `Corners() -> tuple[Math.Point2D * 4]` | 四つのコーナー：origin、origin + 幅ベクトル、対角のコーナー、origin + 高さベクトル。 |
| `Bounds() -> Math.Rect2D` | 座標軸に平行な境界矩形。 |

*ローカルフレーム*

| メソッド | 説明 |
|---|---|
| `LocalToWorld() -> Math.Transform2D` | Xは幅方向の辺、Yは高さ方向の辺に沿い、原点は`origin`。 |
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | `p`が矩形の内側または境界上にある場合はTrue。 |
| `Offset(v: Math.Point2D) -> Math.RotatedRect2D` | ベクトル`v`だけ移動した矩形。 |
| `Rotated(angle: float, center: Math.Point2D) -> Math.RotatedRect2D` | `angle`ラジアンだけ`center`を中心に回転した矩形。 |
| `Normalized() -> Math.RotatedRect2D` | 幅と高さが正になるように正規化した、同じ矩形。 |
| `Transformed(t: Math.Transform2D, tolerance: float = 1e-09) -> Math.RotatedRect2D \| None` | 相似変換（回転、平行移動、均等な拡大縮小、ミラー反転）のみが、矩形を矩形のまま維持します。 |
| `IsEqual(r: Math.RotatedRect2D, tolerance: float = 1e-09) -> bool` | 矩形同士が`tolerance`以内で一致する場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `origin` | `Math.Point2D` | 幅方向と高さ方向の辺の始点となるコーナー。 |
| `direction` | `Math.Point2D` | 幅方向の辺に沿った単位ベクトル。 |
| `width` | `float` | 幅方向の辺の長さ（負の場合は反対方向に伸びる）。 |
| `height` | `float` | 高さ方向の辺の長さ（負の場合は反対方向に伸びる）。 |

### Math.Line2D

> **完全修飾名:** `api.Math.Line2D` · **継承元:** `api.Object`

`start`から`end`への線分。名前に"Infinite"を含むメソッドは、この線分を両点を通る無限直線として扱います。パラメータ`t`は、0を`start`、1を`end`に対応させます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Line2D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Line2D(inStart: Math.Point2D, inEnd: Math.Point2D)` | `inStart`から`inEnd`への線分。 |
| `Line2D(x1: float, y1: float, x2: float, y2: float)` | （`x1`、`y1`）から（`x2`、`y2`）への線分。 |
| `Line2D(start=..., end=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`Line2D(start=...)`。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `FromPointAngleLength(inStart: Math.Point2D, angle: float, length: float) -> Math.Line2D` *静的* | `inStart`を始点とし、方向`angle`（ラジアン）、長さ`length`の線分。 |
| `Vector() -> Math.Point2D` | `start`から`end`へのベクトル。 |
| `Direction() -> Math.Point2D` | `start`から`end`に向かう単位ベクトル。 |
| `Normal() -> Math.Point2D` | 線分の左側を向く単位法線。 |
| `Length() -> float` | 線分の長さ。 |
| `LengthSquared() -> float` | 線分の長さの二乗。 |
| `Angle() -> float` | 線分の方向角（X軸からのラジアン）。 |
| `MidPoint() -> Math.Point2D` | 線分の中点。 |
| `PointAt(t: float) -> Math.Point2D` | パラメータ`t`の点（0 = `start`、1 = `end`。その他の値は外挿）。 |
| `PointAtDistance(distanceFromStart: float) -> Math.Point2D` | 距離`distanceFromStart`だけ`start`から直線に沿って進んだ点。 |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | startとendが`tolerance`以内で一致する場合はTrue。 |
| `Bounds() -> Math.Rect2D` | 線分の境界矩形。 |
| `Reversed() -> Math.Line2D` | `start`と`end`を入れ替えた線分。 |
| `Offset(v: Math.Point2D) -> Math.Line2D` | ベクトル`v`だけ移動した線分。 |
| `OffsetParallel(distance: float) -> Math.Line2D` | 左側に`distance`離れた平行線（負の場合は右側）。 |
| `Transformed(t: Math.Transform2D) -> Math.Line2D` | `t`で変換した線分。 |
| `Rotated(angle: float, center: Math.Point2D) -> Math.Line2D` | `angle`ラジアンだけ`center`を中心に回転した線分。 |
| `WithLength(length: float) -> Math.Line2D` | 線分が指定した長さになるように、直線に沿って終点を移動します。 |
| `Extended(atStart: float, atEnd: float) -> Math.Line2D` | 両端を延長します（負の場合は短くします）。 |
| `ProjectParameter(p: Math.Point2D) -> float` | `p`を無限直線に投影した点のパラメータ。 |
| `ProjectInfinite(p: Math.Point2D) -> Math.Point2D` | `p`の無限直線への投影。 |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | 線分上で`p`に最も近い点。 |
| `DistanceTo(p: Math.Point2D) -> float` | `p`から線分までの距離。 |
| `DistanceToInfinite(p: Math.Point2D) -> float` | `p`から無限直線までの距離。 |
| `SignedDistanceToInfinite(p: Math.Point2D) -> float` | `p`が直線の左側にある場合は正。 |
| `SideOf(p: Math.Point2D, tolerance: float = 1e-09) -> int` | > 0は左側、< 0は右側、0は無限直線上。 |
| `IsPointOn(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | `p`が`tolerance`以内で線分上にある場合はTrue。 |
| `IsPointOnInfinite(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | `p`が`tolerance`以内で無限直線上にある場合はTrue。 |
| `Mirror(p: Math.Point2D) -> Math.Point2D` | 無限直線に対する`p`の鏡像。 |
| `IsParallel(o: Math.Line2D, angleTolerance: float = 1e-09) -> bool` | 直線同士が`angleTolerance`以内で平行の場合はTrue。 |
| `IsPerpendicular(o: Math.Line2D, angleTolerance: float = 1e-09) -> bool` | 直線同士が`angleTolerance`以内で垂直の場合はTrue。 |
| `IsCollinear(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | 両方の線分が同じ無限直線上にある場合はTrue（`tolerance`以内）。 |
| `IntersectInfinite(o: Math.Line2D) -> Math.Line2D.Intersection \| None` | 両線分を通る無限直線同士の交点：点と、両直線上のパラメータ。平行な直線では`None`。 |
| `Intersect(o: Math.Line2D, tolerance: float = 1e-09) -> Math.Point2D \| None` | 二つの線分の交点（平行または同一直線上の線分は点を返しません）。 |
| `Intersects(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | 二つの線分が交差するか接する場合はTrue。 |
| `DistanceTo(o: Math.Line2D) -> float` | 二つの線分間の最短距離。 |
| `IsEqual(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | startとendが`o`と`tolerance`以内で一致する場合はTrue。 |
| `IsEqualIgnoreDirection(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | 線分がいずれかの方向で`o`と`tolerance`以内で一致する場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `start` | `Math.Point2D` | 始点。 |
| `end` | `Math.Point2D` | 終点。 |

#### Math.Line2D.Intersection

> **完全修飾名:** `api.Math.Line2D.Intersection` · **継承元:** `api.Object`

無限直線同士の交点。点と、この直線および`o`上のパラメータを返します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Intersection()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Intersection(point, t, tOther)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `point` | `Math.Point2D` | 交点。 |
| `t` | `float` | この直線上のパラメータ。 |
| `tOther` | `float` | もう一方の直線上のパラメータ。 |

### Math.Circle2D

> **完全修飾名:** `api.Math.Circle2D` · **継承元:** `api.Object`

円。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Circle2D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Circle2D(inCenter: Math.Point2D, inRadius: float)` | 中心`inCenter`、半径`inRadius`の円。 |
| `Circle2D(center=..., radius=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`Circle2D(center=...)`。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `FromDiameter(p1: Math.Point2D, p2: Math.Point2D) -> Math.Circle2D` *静的* | `p1`から`p2`への線分を直径とする円。 |
| `FromThreePoints(p1: Math.Point2D, p2: Math.Point2D, p3: Math.Point2D) -> Math.Circle2D \| None` *静的* | 三点を通る円。点が同一直線上にある場合は空。 |
| `Diameter() -> float` | 直径。 |
| `Circumference() -> float` | 円周。 |
| `Area() -> float` | 面積。 |
| `Bounds() -> Math.Rect2D` | 境界矩形。 |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | 半径がゼロの場合はTrue（`tolerance`以内）。 |
| `PointAt(angle: float) -> Math.Point2D` | 角度`angle`（ラジアン）にある円周上の点。 |
| `AngleOf(p: Math.Point2D) -> float` | 中心から`p`への方向の角度（ラジアン）。 |
| `TangentAt(angle: float) -> Math.Point2D` | 角度`angle`における反時計回り方向の単位接線ベクトル。 |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | 円周上で`p`に最も近い点。 |
| `DistanceTo(p: Math.Point2D) -> float` | `p`から円周までの距離。 |
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | `p`が円の内側または円周上にある場合はTrue。 |
| `IsPointOn(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | `p`が`tolerance`以内で円周上にある場合はTrue。 |
| `Offset(v: Math.Point2D) -> Math.Circle2D` | ベクトル`v`だけ移動した円。 |
| `Rotated(angle: float, c: Math.Point2D) -> Math.Circle2D` | `angle`ラジアンだけ`c`を中心に回転した円。 |
| `Scaled(factor: float, c: Math.Point2D) -> Math.Circle2D` | `factor`で`c`を基準に拡大縮小した円。 |
| `IntersectInfinite(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | 無限直線との交点（0、1、または2点）。 |
| `Intersect(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | 線分との交点。 |
| `Intersect(o: Math.Circle2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | 別の円との交点（一致する円同士は点を返しません）。 |
| `TangentPoints(p: Math.Point2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | `p`を通る接線の円周上の接点（`p`が内側にある場合はなし）。 |
| `IsEqual(o: Math.Circle2D, tolerance: float = 1e-09) -> bool` | 中心と半径が`o`と`tolerance`以内で一致する場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `center` | `Math.Point2D` | 中心。 |
| `radius` | `float` | 半径。 |

### Math.Arc2D

> **完全修飾名:** `api.Math.Arc2D` · **継承元:** `api.Object`

円弧。`sweepAngle`は反時計回りの円弧では正、時計回りの円弧では負です。|sweepAngle| >= 2*piは円全体を表します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Arc2D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Arc2D(inCenter: Math.Point2D, inRadius: float, inStartAngle: float, inSweepAngle: float)` | 指定した中心、半径、開始角、符号付きスイープ角を持つ円弧（ラジアン。正のスイープ角は反時計回り）。 |
| `Arc2D(circle: Math.Circle2D)` | `circle`上の円全体の円弧。 |
| `Arc2D(center=..., radius=..., startAngle=..., sweepAngle=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`Arc2D(center=...)`。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `FromCenterStartEnd(inCenter: Math.Point2D, startPt: Math.Point2D, endPt: Math.Point2D, ccw: bool = True) -> Math.Arc2D` *静的* | 反時計回り（ccw = `True`）または時計回りの、`startPt`から`endPt`を通る半直線までの円弧。 |
| `FromThreePoints(startPt: Math.Point2D, midPt: Math.Point2D, endPt: Math.Point2D) -> Math.Arc2D \| None` *静的* | `startPt`を始点とし、`midPt`を通り、`endPt`で終わる円弧。点が同一直線上にある場合は空。 |
| `FromTangent(startPt: Math.Point2D, startTangent: Math.Point2D, endPt: Math.Point2D) -> Math.Arc2D \| None` *静的* | `startPt`から指定した始点の接線方向に進み、`endPt`で終わる円弧。 |
| `Circle() -> Math.Circle2D` | 円弧が載っている円全体。 |
| `IsFullCircle(tolerance: float = 1e-09) -> bool` | スイープ角が一周の場合はTrue（`tolerance`以内）。 |
| `IsCounterClockwise() -> bool` | スイープ角が正の場合はTrue。 |
| `EndAngle() -> float` | 終点の角度（開始角 + スイープ角）。 |
| `MidAngle() -> float` | 円弧の中点の角度。 |
| `PointAtAngle(angle: float) -> Math.Point2D` | 円弧の円上で角度`angle`（ラジアン）にある点。 |
| `PointAt(t: float) -> Math.Point2D` | スイープに沿ったパラメータ`t`の点（0 = 始点、1 = 終点）。 |
| `StartPoint() -> Math.Point2D` | 始点。 |
| `EndPoint() -> Math.Point2D` | 終点。 |
| `MidPoint() -> Math.Point2D` | 円弧の中点。 |
| `TangentAt(t: float) -> Math.Point2D` | パラメータ`t`における、スイープ方向の単位接線ベクトル。 |
| `Length() -> float` | 円弧長。 |
| `Chord() -> Math.Line2D` | 始点から終点への線分。 |
| `ChordLength() -> float` | 弦の長さ。 |
| `Sagitta() -> float` | 弦の中点から円弧の中点までの距離。 |
| `SectorArea() -> float` | 中心と円弧の間の扇形の面積。 |
| `SegmentArea() -> float` | 円弧と弦の間の面積。 |
| `ContainsAngle(angle: float, tolerance: float = 1e-09) -> bool` | 中心から角度`angle`に延びる半直線が円弧を通るかどうか。 |
| `IsPointOn(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | `p`が`tolerance`以内で円弧上にある場合はTrue。 |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | 円弧上で`p`に最も近い点。 |
| `DistanceTo(p: Math.Point2D) -> float` | `p`から円弧までの距離。 |
| `Bounds() -> Math.Rect2D` | 円弧曲線の境界（中心を含まない）。 |
| `Reversed() -> Math.Arc2D` | 逆方向にたどる同じ円弧。 |
| `Normalized() -> Math.Arc2D` | スイープ角を非負、開始角を[0, 2*pi)にした同じ円弧。 |
| `Offset(v: Math.Point2D) -> Math.Arc2D` | ベクトル`v`だけ移動した円弧。 |
| `Rotated(angle: float, c: Math.Point2D) -> Math.Arc2D` | `angle`ラジアンだけ`c`を中心に回転した円弧。 |
| `WithRadius(r: float) -> Math.Arc2D` | 半径が異なる同心の円弧（角度は同じ）。 |
| `Intersect(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | 線分／別の円弧／円との交点。 |
| `Intersect(circle: Math.Circle2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | 線分／別の円弧／円との交点。 |
| `Intersect(o: Math.Arc2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | 線分／別の円弧／円との交点。 |
| `Tessellate(maxDeviation: float) -> list[Math.Point2D]` | 弦との偏差が最大で`maxDeviation`になる、円弧に沿った点（両端を含む）。 |
| `IsEqual(o: Math.Arc2D, tolerance: float = 1e-09) -> bool` | 円弧同士が`tolerance`以内で一致する場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `center` | `Math.Point2D` | 中心。 |
| `radius` | `float` | 半径。 |
| `startAngle` | `float` | 開始角（ラジアン）。 |
| `sweepAngle` | `float` | 符号付きスイープ角（ラジアン。正は反時計回り）。 |

### Math.PolyVertex

> **完全修飾名:** `api.Math.PolyVertex` · **継承元:** `api.Object`

`Polygon2D`の一つの頂点：座標、頂点タイプ、円弧半径（半径頂点）、およびその頂点を始点とする辺の表示状態。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `PolyVertex()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `PolyVertex(pt: Math.Point2D, t: Math.VertexType = Math.VertexType.Corner, radius: float = 0.0, vis: bool = True)` | `pt`にある、タイプ`t`の頂点（半径頂点では`radius`を使用。`vis`はこの頂点を始点とする辺の表示状態）。 |
| `PolyVertex(point=..., type=..., arcRadius=..., visible=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`PolyVertex(point=...)`。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: Math.PolyVertex) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: Math.PolyVertex) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `point` | `Math.Point2D` | 頂点の位置。 |
| `type` | `Math.VertexType` | 頂点タイプ（コーナー、ベジェ、キュービックスプライン、円弧、半径）。 |
| `arcRadius` | `float` | `Math.VertexType.Arc`でのみ使用します。 |
| `visible` | `bool` | この頂点を始点とする辺の表示状態。 |

### Math.Polygon2D

> **完全修飾名:** `api.Math.Polygon2D` · **継承元:** `api.Object`

多角形または曲線の頂点リスト。GetCurve.../DivideCurveByCountを除く計算では、頂点間を直線の辺として扱います。曲線の頂点（ベジェ、キュービックスプライン、円弧、半径）は制御点として扱います。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Polygon2D()` | 空の多角形。 |
| `Polygon2D(points: list[Math.Point2D], closed: bool = True)` | `points`にコーナー頂点を持つ多角形。 |
| `Polygon2D(vertices: list[Math.PolyVertex], closed: bool = True)` | 頂点`vertices`を持つ多角形。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `FromRect(r: Math.Rect2D) -> Math.Polygon2D` *静的* | `r`の四つのコーナーを持つ閉じた多角形。 |
| `FromRotatedRect(r: Math.RotatedRect2D) -> Math.Polygon2D` *静的* | 回転した矩形`r`の四つのコーナーを持つ閉じた多角形。 |
| `FromArc(arc: Math.Arc2D, maxDeviation: float, closeThroughCenter: bool = False) -> Math.Polygon2D` *静的* | `arc`を近似する多角形。弦と円弧の偏差は最大で`maxDeviation`です。`closeThroughCenter`を指定すると、多角形は閉じた扇形になります。 |
| `RegularPolygon(center: Math.Point2D, circumradius: float, sides: int, startAngle: float = 0.0) -> Math.Polygon2D` *静的* | `sides`個のコーナーを持ち、半径`circumradius`、中心`center`の円上に頂点がある正多角形。最初のコーナーは`startAngle`です。 |

*頂点*

| メソッド | 説明 |
|---|---|
| `GetVertexCount() -> int` | 頂点項目の数。 |
| `IsEmpty() -> bool` | 多角形に頂点がない場合はTrue。 |
| `GetVertex(i: int) -> Math.PolyVertex` | `i`の頂点を返します。 |
| `GetPoint(i: int) -> Math.Point2D` | `i`の点を返します。 |
| `SetPoint(i: int, p: Math.Point2D) -> None` | `i`の点を設定します。 |
| `GetVertices() -> list[Math.PolyVertex]` | 頂点を返します。 |
| `GetPoints() -> list[Math.Point2D]` | 点を返します。 |
| `AddVertex(v: Math.PolyVertex) -> None` | 頂点`v`を追加します。 |
| `AddVertex(p: Math.Point2D, type: Math.VertexType = Math.VertexType.Corner, arcRadius: float = 0.0) -> None` | `p`にタイプ`type`の頂点を追加します（半径頂点では`arcRadius`を使用）。 |
| `InsertVertex(beforeIndex: int, v: Math.PolyVertex) -> None` | `v`を頂点`beforeIndex`の前に挿入します（インデックスが末尾を超える場合は末尾に追加）。 |
| `RemoveVertex(i: int) -> None` | 頂点`i`を削除します（範囲外の場合は無視）。 |
| `Clear() -> None` | すべての頂点とすべての穴を削除します。 |
| `IsClosed() -> bool` | 多角形が閉じている場合はTrue。 |
| `SetClosed(closed: bool) -> None` | *閉じる*をオンまたはオフにします。 |
| `HasCurves() -> bool` | コーナー頂点でない頂点がある場合はTrue。 |
| `HasHiddenEdges() -> bool` | 非表示の辺がある場合はTrue。 |
| `GetHoleCount() -> int` | 穴項目の数。 |
| `GetHole(i: int) -> Math.Polygon2D` | `i`の穴を返します。 |
| `AddHole(hole: Math.Polygon2D) -> None` | `hole`をこの多角形の穴として追加します。 |
| `ClearHoles() -> None` | すべての穴を削除します。 |
| `GetEdgeCount() -> int` | 辺。閉じた多角形の辺の数は頂点数と同じで、開いた多角形では一つ少なくなります。 |
| `GetEdge(i: int) -> Math.Line2D` | 頂点`i`から次の頂点への線分を返します。最後の頂点からは頂点0に戻ります。`i >= GetVertexCount()`の場合は`IndexError`が発生します。開いた多角形では、`i == GetEdgeCount()`は辺数には含まれない閉じる線分を返します。 |

*測定*

| メソッド | 説明 |
|---|---|
| `SignedArea() -> float` | 反時計回りの多角形では正。 |
| `Area() -> float` | 多角形の面積（非負。向きについては`SignedArea`を参照）。 |
| `Perimeter() -> float` | 頂点間の直線の辺の全長。 |
| `Centroid() -> Math.Point2D` | 面積がゼロでない閉じた多角形では面積重心、それ以外は頂点の平均。 |
| `Bounds() -> Math.Rect2D` | 頂点の境界矩形。 |

*向き*

| メソッド | 説明 |
|---|---|
| `IsCounterClockwise() -> bool` | 頂点が反時計回りに並ぶ場合はTrue（符号付き面積が正）。 |
| `IsClockwise() -> bool` | 頂点が時計回りに並ぶ場合はTrue（符号付き面積が負）。 |
| `Reverse() -> Math.Polygon2D` | 頂点の順序を逆にします。辺の表示状態は対応する辺に追従します。 |
| `Reversed() -> Math.Polygon2D` | 頂点の順序を逆にした多角形のコピー。 |

*問い合わせ*

| メソッド | 説明 |
|---|---|
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | 偶奇規則による内外判定（境界は内側として扱います）。 |
| `IsPointOnBoundary(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | `p`が`tolerance`以内で辺上にある場合はTrue。 |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | 多角形の輪郭上で`p`に最も近い点（頂点間の直線の辺）。 |
| `DistanceTo(p: Math.Point2D) -> float` | `p`から多角形の輪郭までの距離（頂点間の直線の辺）。 |
| `GetCurveLength() -> float \| None` | 上記の制御多角形に対する問い合わせとは異なる、実際の曲線状の外側パス。Vectorworksは一時的なNURBS曲線を使用します。図面オブジェクトを挿入したり、入力を変更したりはしません。ブール演算と同様に、アクティブな図面コンテキストが必要です。非表示の辺と閉じる辺を含み、穴は除外します。単位は多角形自身のXY平面内のワールド単位です。パラメータは一時的なNURBSの区間を識別します。 |
| `GetCurveLocationAtDistance(distance: float) -> Math.Polygon2D.CurveLocation \| None` | 距離`distance`における曲線上の位置を返します。 |
| `GetCurvePointAtDistance(distance: float) -> Math.Point2D \| None` | 距離`distance`における曲線上の点を返します。 |
| `GetCurveTangentAtDistance(distance: float) -> Math.Point2D \| None` | 距離`distance`における曲線の接線を返します。 |
| `GetCurveCurvatureAtDistance(distance: float) -> float \| None` | 距離`distance`における曲線の曲率を返します。 |
| `GetCurveClosestPoint(point: Math.Point2D) -> Math.Polygon2D.CurveLocation \| None` | `point`に最も近い曲線上の点を返します。 |
| `GetCurveDistanceTo(point: Math.Point2D) -> float \| None` | `point`までの曲線からの距離を返します。 |
| `DivideCurveByCount(count: int, includeEnd: bool = True) -> list[Math.Point2D] \| None` | ちょうどcount個（>= 2）の、弧長に沿って等間隔に配置された点。includeEnd=`False`の場合は最後の端点／継ぎ目を省略します。曲率は非負で、コーナーでは片側の値です。速度がゼロの場合や引数が無効な場合は失敗します。失敗時は`None`を返し、部分的なリストを返すことはありません。距離は[0, 曲線長]の範囲内でなければなりません。 |
| `IsConvex() -> bool` | 多角形が凸の場合はTrue。 |
| `IsSelfIntersecting(tolerance: float = 1e-09) -> bool` | 隣接していない任意の二つの辺が交差するかどうか。 |
| `Intersect(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | 辺と線分との交点。 |

*変更*

| メソッド | 説明 |
|---|---|
| `Transform(t: Math.Transform2D) -> Math.Polygon2D` | 多角形自体を`t`で変換し、それを返します。 |
| `Transformed(t: Math.Transform2D) -> Math.Polygon2D` | `t`で変換した多角形のコピー。 |
| `Offset(d: Math.Point2D) -> Math.Polygon2D` | 多角形自体をベクトル`d`だけ移動し、それを返します。 |
| `Offset(distance: float, join: Math.OffsetJoin = Math.OffsetJoin.Miter) -> list[Math.Polygon2D]` | 距離`distance`、コーナースタイル`join`での多角形のオフセット輪郭を、多角形のリストとして返します。オフセットに失敗した場合は`RuntimeError`を送出します。 |
| `Rotate(angle: float, center: Math.Point2D) -> Math.Polygon2D` | 多角形自体を`angle`ラジアンだけ`center`を中心に回転し、それを返します。 |
| `RemoveDuplicateVertices(tolerance: float = 1e-09) -> Math.Polygon2D` | 連続する重複頂点を削除します（閉じた多角形では、閉じるための重複頂点も削除）。 |
| `RemoveCollinearVertices(tolerance: float = 1e-09) -> Math.Polygon2D` | 隣接する頂点を通る直線上にある頂点を削除します（コーナー頂点のみ）。 |
| `IsEqual(o: Math.Polygon2D, tolerance: float = 1e-09) -> bool` | 頂点が`o`と`tolerance`以内で一致する場合はTrue。 |
| `Union(other: Math.Polygon2D) -> list[Math.Polygon2D]` | `other`との和集合を、多角形のリストとして返します。アクティブな図面が必要です。演算に失敗した場合は`RuntimeError`を送出します。 |
| `Intersection(other: Math.Polygon2D) -> list[Math.Polygon2D]` | `other`との共通部分を、多角形のリストとして返します。アクティブな図面が必要です。演算に失敗した場合は`RuntimeError`を送出します。 |
| `Difference(other: Math.Polygon2D) -> list[Math.Polygon2D]` | この多角形から`other`を引いた差分を、多角形のリストとして返します。アクティブな図面が必要です。演算に失敗した場合は`RuntimeError`を送出します。 |
| `SymmetricDifference(other: Math.Polygon2D) -> list[Math.Polygon2D]` | 二つの多角形のうち一方のみが覆う部分（対称差）を、多角形のリストとして返します。アクティブな図面が必要です。演算に失敗した場合は`RuntimeError`を送出します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `len()` | `__len__() -> int` | `len(a)`：頂点数。 |
| `[]` | `__getitem__(i: int) -> Math.PolyVertex` | `poly[i]`：`i`の頂点（負のインデックスは末尾から数えます。範囲外の場合は`IndexError`）。 |
| `[] =` | `__setitem__(i: int, vertex: Math.PolyVertex) -> None` | `poly[i] = vertex`：`i`の頂点を置き換えます。 |
| `[] =` | `__setitem__(i: int, point: Math.Point2D) -> None` | `poly[i] = point`：`i`の頂点を`point`に移動します（型は維持）。 |
| `repr()` | `__repr__() -> str` | `repr(poly)`：`<api.Math.Polygon2D vertices=N closed=True\|False>`。 |

#### Math.Polygon2D.CurveLocation

> **完全修飾名:** `api.Math.Polygon2D.CurveLocation` · **継承元:** `api.Object`

多角形の曲線状の外側パスを一時的にNURBSで表現したときの、点と区間固有のパラメータ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `CurveLocation()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `CurveLocation(point, pieceIndex, parameter)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `point` | `Math.Point2D` | 曲線上の点。 |
| `pieceIndex` | `int` | 曲線区間のインデックス。 |
| `parameter` | `float` | その区間のパラメータ。 |

### Math.Point3D

> **完全修飾名:** `api.Math.Point3D` · **継承元:** `api.Object`

Pythonが所有する、ワールド座標のミリメートル単位の3D点／ベクトル。Vector3Dは同じ型です。x、y、z、オプションのZを指定したPoint2D、またはapi.Point3Dから構築します。`Normalized()`は値を返し、`Normalize()`はこの値を変更します。ゼロの正規化はゼロを返します。図面は不要です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Point3D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Point3D(inX: float, inY: float, inZ: float)` | 座標`inX`、`inY`、`inZ`を持つ点／ベクトル。 |
| `Point3D(point: Math.Point2D, inZ: float = 0.0)` | `point`のXとY、およびZとして`inZ`を持つ点。 |
| `Point3D(point: Point3D)` | `api.Point3D`レコードを変換します。 |
| `Point3D(x=..., y=..., z=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`Point3D(x=...)`。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `IsEqual(other: Math.Point3D, tolerance: float = 1e-09) -> bool` | すべての座標が`other`と`tolerance`以内で一致する場合はTrue。 |
| `IsZero(tolerance: float = 1e-09) -> bool` | ベクトルの長さがゼロから`tolerance`以内にある場合はTrue。 |
| `IsFinite() -> bool` | どの座標も無限大またはNaNでない場合はTrue。 |
| `Dot(other: Math.Point3D) -> float` | `other`との内積。 |
| `Cross(other: Math.Point3D) -> Math.Point3D` | `other`との外積。 |
| `LengthSquared() -> float` | ベクトルの長さの二乗。 |
| `Length() -> float` | ベクトルの長さ。 |
| `Normalized() -> Math.Point3D` | 同じ方向の単位ベクトル（新しい値。ゼロベクトルはゼロのまま）。 |
| `Normalize() -> Math.Point3D` | このベクトル自体の長さを単位長さに調整し、それを返します。 |
| `WithLength(length: float) -> Math.Point3D` | 同じ方向で長さ`length`のベクトル。 |
| `DistanceSquaredTo(other: Math.Point3D) -> float` | `other`までの距離の二乗。 |
| `DistanceTo(other: Math.Point3D) -> float` | `other`までの距離。 |
| `MidPoint(other: Math.Point3D) -> Math.Point3D` | この点と`other`の中間の点。 |
| `Lerp(other: Math.Point3D, parameter: float) -> Math.Point3D` | `other`に向かう線形補間。`parameter` = 0ではこの点、1では`other`を返します。 |
| `AngleBetween(other: Math.Point3D) -> float` | このベクトルと`other`のなす角（ラジアン、0 .. pi）。 |
| `IsParallel(other: Math.Point3D, angleTolerance: float = 1e-09) -> bool` | ベクトルが`angleTolerance`以内で平行（同方向または反対方向）の場合はTrue。 |
| `IsPerpendicular(other: Math.Point3D, angleTolerance: float = 1e-09) -> bool` | ベクトルが`angleTolerance`以内で垂直の場合はTrue。 |
| `XY() -> Math.Point2D` | X座標とY座標を`Math.Point2D`として返します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `+` | `__add__(other: Math.Point3D) -> Math.Point3D` | `a + b`：二つの値の和。 |
| `-` | `__sub__(other: Math.Point3D) -> Math.Point3D` | `a - b`：二つの値の差。 |
| `- (unary)` | `__neg__() -> Math.Point3D` | `-a`：符号を反転した値。 |
| `*` | `__mul__(scalar: float) -> Math.Point3D` | `a * s`：スカラーを乗じた値。 |
| `/` | `__truediv__(scalar: float) -> Math.Point3D` | `a / s`：スカラーで割った値。 |
| `+=` | `__iadd__(other: Math.Point3D) -> Math.Point3D` | `a += b`：自身にもう一方の値を加算します。 |
| `-=` | `__isub__(other: Math.Point3D) -> Math.Point3D` | `a -= b`：自身からもう一方の値を減算します。 |
| `*=` | `__imul__(scalar: float) -> Math.Point3D` | `a *= s`：自身にスカラーを乗じます。 |
| `/=` | `__itruediv__(scalar: float) -> Math.Point3D` | `a /= s`：自身をスカラーで割ります。 |
| `==` | `__eq__(other: Math.Point3D) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(other: Math.Point3D) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |
| `* (reflected)` | `__rmul__(scalar: float) -> Math.Point3D` | `s * a`：スカラーを乗じた値。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `x` | `float` | X座標。 |
| `y` | `float` | Y座標。 |
| `z` | `float` | Z座標。 |

### Math.Transform3D

> **完全修飾名:** `api.Math.Transform3D` · **継承元:** `api.Object`

列ベクトルに作用するアフィン行列。A * BはBを先に適用し、その後Aを適用します。暗黙の最終行は(0, 0, 0, 1)です。角度は右手系のラジアンです。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Transform3D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Transform3D(inA: float, inB: float, inC: float, inD: float, inE: float, inF: float, inG: float, inH: float, inI: float, inTx: float, inTy: float, inTz: float)` | 行ごとに指定した九つの線形係数（`inA` .. `inI`）と、平行移動`inTx`、`inTy`、`inTz`を持つ変換。 |
| `Transform3D(a=..., b=..., c=..., tx=..., d=..., e=..., f=..., ty=..., g=..., h=..., i=..., tz=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`Transform3D(a=...)`。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Identity() -> Math.Transform3D` *静的* | 恒等変換。 |
| `Translation(dx: float, dy: float, dz: float) -> Math.Transform3D` *静的* | `dx`、`dy`、`dz`による平行移動。 |
| `Translation(offset: Math.Point3D) -> Math.Transform3D` *静的* | ベクトル`offset`による平行移動。 |
| `Scale(sx: float, sy: float, sz: float) -> Math.Transform3D` *静的* | 原点を中心とした`sx`、`sy`、`sz`による拡大縮小。 |
| `Scale(sx: float, sy: float, sz: float, center: Math.Point3D) -> Math.Transform3D` *静的* | `sx`、`sy`、`sz`で`center`を中心に拡大縮小する変換。 |
| `RotationX(angle: float) -> Math.Transform3D` *静的* | X軸を中心とした`angle`ラジアンの回転。 |
| `RotationY(angle: float) -> Math.Transform3D` *静的* | Y軸を中心とした`angle`ラジアンの回転。 |
| `RotationZ(angle: float) -> Math.Transform3D` *静的* | Z軸を中心とした`angle`ラジアンの回転。 |
| `Rotation(angle: float, axis: Math.Point3D, center: Math.Point3D = Math.Point3D()) -> Math.Transform3D \| None` *静的* | `angle`ラジアンだけ、軸`axis`（`center`を通る）を中心に回転する変換（右手系）。軸がゼロの場合は`None`。 |
| `Mirror(origin: Math.Point3D, normal: Math.Point3D) -> Math.Transform3D \| None` *静的* | `origin`を通り法線`normal`を持つ平面に対するミラー反転。法線がゼロの場合は`None`。 |
| `FromAxes(origin: Math.Point3D, xAxis: Math.Point3D, yAxis: Math.Point3D, zAxis: Math.Point3D) -> Math.Transform3D` *静的* | 単位座標軸を`xAxis`、`yAxis`、`zAxis`に、原点を`origin`に写す変換。 |
| `Then(next: Math.Transform3D) -> Math.Transform3D` | この変換に続けて`next`を適用します（`next * self`と同じ）。 |
| `Apply(point: Math.Point3D) -> Math.Point3D` | 点`point`を変換します（平行移動を含む）。 |
| `ApplyToVector(vector: Math.Point3D) -> Math.Point3D` | ベクトル`vector`を変換します（平行移動を無視）。 |
| `Determinant() -> float` | 線形部分の行列式（ミラー反転する変換では負）。 |
| `IsInvertible(tolerance: float = 1e-09) -> bool` | 行列式がゼロでない場合はTrue（許容差`tolerance`で判定）。 |
| `Inverse() -> Math.Transform3D \| None` | 逆変換。変換を反転できない場合は`None`。 |
| `ApplyToNormal(normal: Math.Point3D) -> Math.Point3D \| None` | 面の法線`normal`を変換します（逆転置、正規化）。変換を反転できない場合は`None`。 |
| `GetTranslation() -> Math.Point3D` | 平行移動を返します。 |
| `SetTranslation(offset: Math.Point3D) -> None` | 平行移動を設定します。 |
| `GetXAxis() -> Math.Point3D` | X軸を返します。 |
| `GetYAxis() -> Math.Point3D` | Y軸を返します。 |
| `GetZAxis() -> Math.Point3D` | Z軸を返します。 |
| `IsMirrored() -> bool` | 変換がミラー反転を行う場合はTrue（行列式が負）。 |
| `IsOrthogonal(tolerance: float = 1e-09) -> bool` | 線形部分が拡大縮小を伴わない回転またはミラー反転の場合はTrue（`tolerance`以内）。 |
| `IsIdentity(tolerance: float = 1e-09) -> bool` | 変換が`tolerance`以内で恒等変換の場合はTrue。 |
| `IsEqual(other: Math.Transform3D, tolerance: float = 1e-09) -> bool` | すべての係数が`other`と`tolerance`以内で一致する場合はTrue。 |
| `IsFinite() -> bool` | どの係数も無限大またはNaNでない場合はTrue。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `*` | `__mul__(other: Math.Transform3D) -> Math.Transform3D` | `A * B`：合成変換（Bを先に適用し、その後Aを適用）。 |
| `*=` | `__imul__(other: Math.Transform3D) -> Math.Transform3D` | `A *= B`：この変換自体にもう一方の変換を合成します。 |
| `()` | `__call__(point: Math.Point3D) -> Math.Point3D` | `T(p)`：点に変換を適用します（`Apply`と同じ）。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `a` | `float` | 線形部分の1行1列。 |
| `b` | `float` | 線形部分の1行2列。 |
| `c` | `float` | 線形部分の1行3列。 |
| `tx` | `float` | X方向の平行移動。 |
| `d` | `float` | 線形部分の2行1列。 |
| `e` | `float` | 線形部分の2行2列。 |
| `f` | `float` | 線形部分の2行3列。 |
| `ty` | `float` | Y方向の平行移動。 |
| `g` | `float` | 線形部分の3行1列。 |
| `h` | `float` | 線形部分の3行2列。 |
| `i` | `float` | 線形部分の3行3列。 |
| `tz` | `float` | Z方向の平行移動。 |

### Math.Line3D

> **完全修飾名:** `api.Math.Line3D` · **継承元:** `api.Object`

線分のパラメータ0はstart、1はendです。Infiniteメソッドはパラメータをこの範囲に制限しません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Line3D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Line3D(inStart: Math.Point3D, inEnd: Math.Point3D)` | `inStart`から`inEnd`への線分。 |
| `Line3D(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float)` | （`x1`、`y1`、`z1`）から（`x2`、`y2`、`z2`）への線分。 |
| `Line3D(start=..., end=...)` | フィールド値をキーワード引数で指定します（任意の部分集合）。例：`Line3D(start=...)`。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Vector() -> Math.Point3D` | `start`から`end`へのベクトル。 |
| `Direction() -> Math.Point3D` | `start`から`end`に向かう単位ベクトル。 |
| `Length() -> float` | 線分の長さ。 |
| `LengthSquared() -> float` | 線分の長さの二乗。 |
| `MidPoint() -> Math.Point3D` | 線分の中点。 |
| `PointAt(parameter: float) -> Math.Point3D` | `parameter`の点（0 = `start`、1 = `end`。その他の値は外挿）。 |
| `PointAtDistance(distance: float) -> Math.Point3D` | 距離`distance`だけ`start`から直線に沿って進んだ点。 |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | startとendが`tolerance`以内で一致する場合はTrue。 |
| `Reversed() -> Math.Line3D` | `start`と`end`を入れ替えた線分。 |
| `Offset(offset: Math.Point3D) -> Math.Line3D` | ベクトル`offset`だけ移動した線分。 |
| `Transformed(transform: Math.Transform3D) -> Math.Line3D` | `transform`で変換した線分。 |
| `WithLength(length: float) -> Math.Line3D` | startと方向が同じで、長さ`length`の線分。 |
| `Extended(atStart: float, atEnd: float) -> Math.Line3D` | 始点の手前に`atStart`、終点の先に`atEnd`だけ延長した線分（負の値の場合は短くします）。 |
| `ProjectParameter(point: Math.Point3D) -> float` | `point`を無限直線に投影した点のパラメータ。 |
| `ProjectInfinite(point: Math.Point3D) -> Math.Point3D` | `point`の無限直線への投影。 |
| `ClosestPoint(point: Math.Point3D) -> Math.Point3D` | 線分上で`point`に最も近い点。 |
| `DistanceTo(point: Math.Point3D) -> float` | `point`から線分までの距離。 |
| `DistanceToInfinite(point: Math.Point3D) -> float` | `point`から無限直線までの距離。 |
| `IsPointOn(point: Math.Point3D, tolerance: float = 1e-09) -> bool` | `point`が`tolerance`以内で線分上にある場合はTrue。 |
| `IsPointOnInfinite(point: Math.Point3D, tolerance: float = 1e-09) -> bool` | `point`が`tolerance`以内で無限直線上にある場合はTrue。 |
| `IsParallel(other: Math.Line3D, angleTolerance: float = 1e-09) -> bool` | 直線同士が`angleTolerance`以内で平行の場合はTrue。 |
| `IsPerpendicular(other: Math.Line3D, angleTolerance: float = 1e-09) -> bool` | 直線同士が`angleTolerance`以内で垂直の場合はTrue。 |
| `IsCollinear(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | 両方の線分が同じ無限直線上にある場合はTrue（`tolerance`以内）。 |
| `IntersectInfinite(other: Math.Line3D, tolerance: float = 1e-09) -> Math.Point3D \| None` | 二つの無限直線の交点。交わらない場合（平行またはねじれの位置）は`None`。 |
| `Intersect(other: Math.Line3D, tolerance: float = 1e-09) -> Math.Point3D \| None` | 二つの線分の交点。一点で交わらない場合は`None`。 |
| `Intersects(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | 二つの線分が接するか重なる場合はTrue（同一直線上での重なりを含む）。 |
| `DistanceTo(other: Math.Line3D) -> float` | 二つの線分間の最短距離。 |
| `IsEqual(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | startとendが`other`と`tolerance`以内で一致する場合はTrue。 |
| `IsEqualIgnoreDirection(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | 線分がいずれかの方向で`other`と`tolerance`以内で一致する場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `start` | `Math.Point3D` | 始点。 |
| `end` | `Math.Point3D` | 終点。 |

### Math.Plane3D

> **完全修飾名:** `api.Math.Plane3D` · **継承元:** `api.Object`

単位法線を持つ向き付きの無限平面。デフォルトの平面はXY、法線は+Zです。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Plane3D()` | 法線が+ZのXY平面。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `FromPointNormal(origin: Math.Point3D, normal: Math.Point3D) -> Math.Plane3D \| None` *静的* | `origin`を通り法線`normal`を持つ平面。法線がゼロの場合は`None`。 |
| `FromPoints(first: Math.Point3D, second: Math.Point3D, third: Math.Point3D) -> Math.Plane3D \| None` *静的* | 三点を通る平面（法線は右手の法則による）。点が同一直線上にある場合は`None`。 |
| `GetOrigin() -> Math.Point3D` | 原点を返します。 |
| `GetNormal() -> Math.Point3D` | 法線を返します。 |
| `SignedDistanceTo(point: Math.Point3D) -> float` | `point`の符号付き距離（法線が向く側で正）。 |
| `DistanceTo(point: Math.Point3D) -> float` | `point`から平面までの距離。 |
| `Project(point: Math.Point3D) -> Math.Point3D` | `point`の平面への投影。 |
| `Mirror(point: Math.Point3D) -> Math.Point3D` | 平面に対する`point`の鏡像。 |
| `Contains(point: Math.Point3D, tolerance: float = 1e-09) -> bool` | `point`が平面上にある場合はTrue（`tolerance`以内）。 |
| `Reversed() -> Math.Plane3D` | 法線を逆向きにした同じ平面。 |
| `Offset(distance: float) -> Math.Plane3D` | 法線に沿って`distance`だけ移動した平面。 |
| `IsParallel(other: Math.Plane3D, angleTolerance: float = 1e-09) -> bool` | 平面同士が`angleTolerance`以内で平行の場合はTrue。 |
| `IsPerpendicular(other: Math.Plane3D, angleTolerance: float = 1e-09) -> bool` | 平面同士が`angleTolerance`以内で垂直の場合はTrue。 |
| `IsEqual(other: Math.Plane3D, tolerance: float = 1e-09, angleTolerance: float = 1e-09) -> bool` | 平面同士が許容差以内で一致する場合はTrue（法線の向きは無視）。 |
| `IntersectInfinite(line: Math.Line3D, angleTolerance: float = 1e-09) -> Math.Point3D \| None` | `line`を通る無限直線と平面との交点。平行な場合は`None`。 |
| `Intersect(line: Math.Line3D, tolerance: float = 1e-09) -> Math.Point3D \| None` | 線分`line`と平面との交点。線分が平面と交差しない場合は`None`。 |
| `Intersect(other: Math.Plane3D, angleTolerance: float = 1e-09) -> Math.Line3D \| None` | 二つの平面の交線。平行な場合は`None`。 |
| `Transformed(transform: Math.Transform3D) -> Math.Plane3D \| None` | `transform`で変換した平面。変換を反転できない場合は`None`。 |

<a id="enumerations"></a>

## 列挙型

### Math.VertexType

> **完全修飾名:** `api.Math.VertexType` · **種類:** `IntEnum`

多角形状の頂点の種類。値はVectorworksのVertexType定数と一致します。

| メンバー | 値 | 説明 |
|---|---|---|
| `Corner` | `0` |  |
| `Bezier` | `1` | 二次ベジェの制御点。 |
| `Cubic` | `2` | キュービックスプラインの制御点。 |
| `Arc` | `3` | 半径を持つ円弧の制御点（0 = 最大半径）。 |
| `Radius` | `4` | 半径（接線）の制御点。 |

### Math.OffsetJoin

> **完全修飾名:** `api.Math.OffsetJoin` · **種類:** `IntEnum`

多角形のオフセットのコーナースタイル（`Polygon2D.Offset`）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Miter` | `0` |  |
| `Round` | `1` |  |

<a id="module-functions"></a>

## モジュール関数

`api.Math`モジュールの関数（`api.Math.Name(...)`として呼び出します）。

| 関数 | 説明 |
|---|---|
| `DegToRad(deg: float) -> float` | 度をラジアンに変換します。 |
| `RadToDeg(rad: float) -> float` | ラジアンを度に変換します。 |
| `IsZero(value: float, tolerance: float = 1e-09) -> bool` | `abs(value) <= tolerance`の場合はTrue。 |
| `AreEqual(a: float, b: float, tolerance: float = 1e-09) -> bool` | `a`と`b`の差が最大でも`tolerance`の場合はTrue。 |
| `IsLess(a: float, b: float, tolerance: float = 1e-09) -> bool` | `a < b - tolerance`の場合はTrue。 |
| `IsGreater(a: float, b: float, tolerance: float = 1e-09) -> bool` | `a > b + tolerance`の場合はTrue。 |
| `IsBetween(v: float, lo: float, hi: float, tolerance: float = 1e-09) -> bool` | `v`が`lo`と`hi`の間（順序は任意）に、許容差`tolerance`で収まる場合はTrue。 |
| `Sign(v: float) -> float` | `v`の符号：-1、0、または1。 |
| `Clamp(v: float, lo: float, hi: float) -> float` | `v`を範囲`[lo, hi]`に制限した値。 |
| `Lerp(a: float, b: float, t: float) -> float` | 線形補間：`a + (b - a) * t`。 |
| `NormalizeAngle(angle: float) -> float` | [0, 2*pi)の範囲の角度。 |
| `NormalizeAngleSigned(angle: float) -> float` | `(-pi, pi]`に正規化した角度。 |
| `AngleDelta(from_: float, to: float) -> float` | `from`から`to`への反時計回りの角度。範囲は[0, 2*pi)。 |
| `AnglesAreEqual(a: float, b: float, tolerance: float = 1e-09) -> bool` | 角度`a`と`b`が`tolerance`以内で等しい場合はTrue（2*piを法とする）。 |

<a id="module-constants"></a>

## モジュール定数

| 定数 | 型 | 値 | 説明 |
|---|---|---|---|
| `api.Math.kPi` | `float` | `3.14159265358979323846` | 定数pi。 |
| `api.Math.kTwoPi` | `float` | `2.0* `kPi`` | 2 * pi（ラジアンでの一周）。 |
| `api.Math.kHalfPi` | `float` | `0.5* `kPi`` | pi / 2（ラジアンでの四分の一周）。 |
| `api.Math.kEpsilon` | `float` | `1e-9` | デフォルトの距離許容差。 |
| `api.Math.kAngleEpsilon` | `float` | `1e-9` | デフォルトの角度許容差（ラジアン）。 |

<a id="aliases-and-implicit-conversions"></a>

## 別名と暗黙の変換

- `api.Math.Vector2D`は[`Math.Point2D`](#mathpoint2d)の別名です（同じクラスオブジェクト）。
- `api.Math.Vector3D`は[`Math.Point3D`](#mathpoint3d)の別名です（同じクラスオブジェクト）。
- [`Math.Point2D`](#mathpoint2d)は、[`Point2D`](Attributes.md#point2d)型の引数が必要な場所で使用できます（暗黙の変換）。
- [`Point2D`](Attributes.md#point2d)は、[`Math.Point2D`](#mathpoint2d)型の引数が必要な場所で使用できます（暗黙の変換）。
- [`Math.Point3D`](#mathpoint3d)は、[`Point3D`](UIAutomation.md#point3d)型の引数が必要な場所で使用できます（暗黙の変換）。
- [`Point3D`](UIAutomation.md#point3d)は、[`Math.Point3D`](#mathpoint3d)型の引数が必要な場所で使用できます（暗黙の変換）。

---

[一覧に戻る](README.md) · [先頭に戻る](#math--standalone-2d-and-3d-math-apimath)
