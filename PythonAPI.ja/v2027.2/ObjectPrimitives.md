[English](../../PythonAPI/v2027.2/ObjectPrimitives.md) • [Deutsch](../../PythonAPI.de/v2027.2/ObjectPrimitives.md) • **日本語**

<a id="objectprimitives--2d-primitive-objects"></a>

# ObjectPrimitives — 2Dプリミティブオブジェクト

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

2Dオブジェクトのクラス。各オブジェクトクラスは図面オブジェクトの軽量なビューです。Pythonオブジェクトをコピーしても図面オブジェクトはコピーされず、削除しても図面オブジェクトは削除されません。

`PrimitiveObject`はAPIの**すべて**のオブジェクトクラス（3D、注釈、建築、造園、Spotlight、ConnectCADのオブジェクトを含む）の共通基底クラスです。識別、階層、状態、属性、変換はそこで一度だけ説明しています。`ParametricObject`は任意のプラグインオブジェクトを表します（専用のクラスがない場合に使用します）。`PolyObject`は`PolygonObject`と`PolylineObject`の共通基底クラスであり、`RectangularObject`は四角形クラスの共通基底クラスです。

値を取得できない場合、ゲッターは`None`を返し、失敗した場合、セッターは`False`を返します。座標はワールド単位、角度はラジアン（X軸から反時計回り）です。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [PrimitiveObject](#primitiveobject)
    - [PrimitiveObject.Bounds3D](#primitiveobjectbounds3d)
  - [Locus2DObject](#locus2dobject)
  - [Line2DObject](#line2dobject)
  - [RectangularObject](#rectangularobject)
  - [RectangleObject](#rectangleobject)
  - [CornerDiameters](#cornerdiameters)
  - [RoundRectObject](#roundrectobject)
  - [ArcObject](#arcobject)
  - [CircleObject](#circleobject)
  - [PolyObject](#polyobject)
    - [PolyObject.BooleanOperation](#polyobjectbooleanoperation)
  - [PolygonObject](#polygonobject)
  - [PolylineObject](#polylineobject)
  - [GroupObject](#groupobject)
  - [ParametricObject](#parametricobject)
    - [ParametricObject.PluginKind](#parametricobjectpluginkind)
  - [TextObject](#textobject)
    - [TextObject.StyleRun](#textobjectstylerun)
    - [TextObject.TabStop](#textobjecttabstop)
    - [TextObject.HorizontalAlignment](#textobjecthorizontalalignment)
    - [TextObject.VerticalAlignment](#textobjectverticalalignment)
    - [TextObject.Spacing](#textobjectspacing)
    - [TextObject.TabAlignment](#textobjecttabalignment)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`PrimitiveObject`](#primitiveobject) | クラス |  | APIのすべてのオブジェクトクラスの共通基底クラス（2Dプリミティブ、およびそれらのサブクラスを通じた3D、注釈、建築、造園、Spotlight、ConnectCAD... |
| [`PrimitiveObject.Bounds3D`](#primitiveobjectbounds3d) | クラス（入れ子） |  | ワールド単位の、座標軸に平行な3Dバウンディングボックス |
| [`Locus2DObject`](#locus2dobject) | クラス | [`PrimitiveObject`](#primitiveobject) | 2D 基準点（`ObjectType.Locus`）：参照用の点。 |
| [`Line2DObject`](#line2dobject) | クラス | [`PrimitiveObject`](#primitiveobject) | 2D直線（`ObjectType.Line`）：二点間の直線の線分。 |
| [`RectangularObject`](#rectangularobject) | クラス | [`PrimitiveObject`](#primitiveobject) | 四角形クラスと角丸四角形クラスの共通基底クラス。 |
| [`RectangleObject`](#rectangleobject) | クラス | [`RectangularObject`](#rectangularobject) | 四角形（`ObjectType.Box`）。回転している場合もあります。 |
| [`CornerDiameters`](#cornerdiameters) | クラス |  | 角丸四角形の角の丸み：幅方向の辺（alongWidth）と高さ方向の辺（alongHeight）に沿った、角の楕円の直径。 |
| [`RoundRectObject`](#roundrectobject) | クラス | [`RectangularObject`](#rectangularobject) | 角丸四角形（`ObjectType.RoundedRectangle`）。回転している場合もあります。 |
| [`ArcObject`](#arcobject) | クラス | [`PrimitiveObject`](#primitiveobject) | 円弧（`ObjectType.Arc`）。 |
| [`CircleObject`](#circleobject) | クラス | [`PrimitiveObject`](#primitiveobject) | 円。 |
| [`PolyObject`](#polyobject) | クラス | [`PrimitiveObject`](#primitiveobject) | 多角形クラスと曲線クラスの共通基底クラス。 |
| [`PolyObject.BooleanOperation`](#polyobjectbooleanoperation) | IntEnum（入れ子） |  | 2Dブール関数の演算 |
| [`PolygonObject`](#polygonobject) | クラス | [`PolyObject`](#polyobject) | 多角形（`ObjectType.Polygon`、およびフリーハンド`ObjectType.FreehandPolygon`）：頂点はコーナー頂点のみ。 |
| [`PolylineObject`](#polylineobject) | クラス | [`PolyObject`](#polyobject) | 曲線（`ObjectType.Polyline`）：頂点をコーナー、ベジェ、キュービックスプライン、円弧、または半径の頂点にできる多角形状。 |
| [`GroupObject`](#groupobject) | クラス | [`PrimitiveObject`](#primitiveobject) | グループ（`ObjectType.Group`）：他のオブジェクトを格納するコンテナ。 |
| [`ParametricObject`](#parametricobject) | クラス | [`PrimitiveObject`](#primitiveobject) | スクリプトまたはコンパイル済みプラグインで定義された、任意の種類の汎用プラグインオブジェクト（パラメトリックオブジェクト、`ObjectType.Parametric`）。 |
| [`ParametricObject.PluginKind`](#parametricobjectpluginkind) | IntEnum（入れ子） |  | プラグインのオブジェクトの配置方法：プラグインが宣言するオブジェクトのサブタイプ。 |
| [`TextObject`](#textobject) | クラス | [`PrimitiveObject`](#primitiveobject) | 文字列（`ObjectType.Text`）：原点に配置する書式付きの文字列。 |
| [`TextObject.StyleRun`](#textobjectstylerun) | クラス（入れ子） |  | 同じ書式を共有する文字の連続範囲：開始位置、長さ、フォント、サイズ（ワールド単位とポイント）、スタイルフラグ、色、文字スタイル、トラッキング。 |
| [`TextObject.TabStop`](#textobjecttabstop) | クラス（入れ子） |  | タブストップ：文字列の左端からのワールド単位のオフセットと配置揃え。 |
| [`TextObject.HorizontalAlignment`](#textobjecthorizontalalignment) | IntEnum（入れ子） |  | 文字列の水平方向の配置揃え。 |
| [`TextObject.VerticalAlignment`](#textobjectverticalalignment) | IntEnum（入れ子） |  | 原点を基準とする文字列の垂直方向の配置揃え。 |
| [`TextObject.Spacing`](#textobjectspacing) | IntEnum（入れ子） |  | 文字列の行間。`Custom`は`SetSpacing`に渡された行送りを使用します。 |
| [`TextObject.TabAlignment`](#textobjecttabalignment) | IntEnum（入れ子） |  | タブストップでの文字列の配置揃え。 |

<a id="classes"></a>

## クラス

### PrimitiveObject

> **完全修飾名:** `api.PrimitiveObject` · **継承元:** `api.Object`

APIのすべてのオブジェクトクラスの共通基底クラス（2Dプリミティブ、およびそれらのサブクラスを通じた3D、注釈、建築、造園、Spotlight、ConnectCADのオブジェクト）。インスタンスは、ハンドルを通じて図面オブジェクトを参照する軽量なビューです。インスタンスをコピーしても図面オブジェクトはコピーされず、破棄しても図面オブジェクトは削除されません。未加工のハンドルを操作するには：

- まず種類を確認します：`if api.Line2DObject.Is(h): ...`
- または`api.Document.As(api.Line2DObject, h)`を使用します。型付きオブジェクト、または`None`が返されます。
- `api.PrimitiveObject(h)`は任意のオブジェクトハンドルを受け付けます。

別の種類のハンドルから型付きオブジェクトを構築すると、無効なオブジェクトになります（`IsValid()`は`False`）。その場合、ゲッターは`None`を返し、セッター／操作は`False`を返します。API全体の規約：

- 座標はワールド（モデル）単位、角度はX軸から反時計回りのラジアン、文字列はUTF-8です。
- 値を取得できない場合、値のゲッターは`None`を返します。セッターと操作は`bool`を返します。失敗した場合、ハンドルのゲッターはnullハンドルを返し、ファクトリは無効なオブジェクトを返します。
- 変換操作（Move、Rotate、Scale、Mirror）によって、Vectorworksが図面オブジェクトのハンドルを置き換える場合があります。Pythonオブジェクトは新しいハンドルに自動的に追従します。変換前に作成したコピーは更新する必要があります。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `PrimitiveObject(h: Handle)` | 任意の図面オブジェクト`h`を汎用の`PrimitiveObject`として参照します。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `GetHandle() -> Handle` | 図面オブジェクトのハンドル。 |
| `IsValid() -> bool` | このオブジェクトが既存の図面オブジェクトを参照している場合はTrue。 |
| `GetObjectType() -> ObjectType` | オブジェクトの種類を返します。 |

*識別*

| メソッド | 説明 |
|---|---|
| `GetName() -> str \| None` | 名前を返します。 |
| `SetName(name: str) -> bool` | 名前を設定します（その名前を別のオブジェクトが使用している場合は失敗します）。 |
| `GetInternalIndex() -> int \| None` | 内部インデックスを返します。 |

*階層*

| メソッド | 説明 |
|---|---|
| `GetParent() -> Handle` | 親を返します。レイヤ、グループ、シンボル定義、... |
| `GetNext() -> Handle` | 同じリスト内の隣接オブジェクト（VectorScriptのNextObj / PrevObj）。最後のオブジェクトの後／最初のオブジェクトの前ではnullです。 |
| `GetPrevious() -> Handle` | 前のオブジェクトを返します。 |
| `MoveToContainer(container: Handle) -> bool` | オブジェクトをコンテナ（レイヤ、グループ、...）内に移動します。他の操作と同様、取り消しは記録しません。図面内のオブジェクトの移動を取り消せるようにするには、操作前に`Document.AddBeforeMoveObject`、操作後に`Document.AddAfterMoveObject`を呼び出してください。この操作で挿入する新規オブジェクトは、`Document.AddAfterSwapObject`で登録します。この操作はオブジェクトのリンクを付け替えるだけです。ドアや窓を壁に挿入したり、壁から取り出したりすることはありません。オブジェクトを壁、プラグインオブジェクト、自分自身、または自身のメンバーの中へ移動したり、これらの中から外へ移動したりすると、ファイルを破損する可能性があります。レイヤ、グループ、シンボル定義の間でのみ移動してください。シンボルのチェックも行いません。あるシンボルのインスタンス、または任意の深さでそのインスタンスを含むシンボルのインスタンスを、そのシンボル定義（またはその中のグループ）内に移動すると、シンボルが自分自身の中に入れ子になり、無限ループになります。 |
| `GetFirstMember() -> Handle` | メンバー（VectorScriptのFInGroup / LInGroupによる走査）。すべてのオブジェクトタイプを走査できます。メンバーを持たないオブジェクト（直線、四角形、...）は、null／空のリストを返します。 |
| `GetLastMember() -> Handle` | 最後のメンバーを返します。 |
| `ForEachMember(callback: callable(Handle)) -> None` | 直接のメンバーのみ。次のメンバーは`callback`の実行前に取得されるため、コールバック内で現在のメンバーを削除または移動できます。 |
| `GetMembers() -> list[Handle]` | メンバーを返します。 |

*状態*

| メソッド | 説明 |
|---|---|
| `IsVisible() -> bool \| None` | 所属するクラスとレイヤの表示状態を考慮して、オブジェクトが表示される場合はTrue。 |
| `SetVisible(visible: bool) -> bool` | *表示*をオンまたはオフにします。 |
| `IsLocked() -> bool \| None` | オブジェクトがロックされている場合はTrue。 |
| `SetLocked(locked: bool) -> bool` | *ロック*をオンまたはオフにします。 |
| `IsSelected() -> bool \| None` | オブジェクトが選択されている場合はTrue。 |
| `SetSelected(selected: bool) -> bool` | *選択*をオンまたはオフにします。 |

*クラス*

| メソッド | 説明 |
|---|---|
| `GetClass() -> ClassAttributes` | クラスを返します。 |
| `SetClass(theClass: ClassAttributes, useClassAttributes: bool = False) -> bool` | オブジェクトを`theClass`に割り当てます。`useClassAttributes`が`True`の場合、オブジェクトのすべての属性を「クラス属性」に設定します。 |
| `Attributes() -> ObjectAttributes` | グラフィック属性（線、面、マーカー、ドロップシャドウ、...） |

*測定*

| メソッド | 説明 |
|---|---|
| `GetBounds() -> Math.Rect2D \| None` | 境界を返します。 |
| `GetArea() -> float \| None` | 面積を返します。 |
| `GetPerimeter() -> float \| None` | 周長を返します。 |
| `GetBounds3D(layerRelative: bool = False) -> PrimitiveObject.Bounds3D \| None` | すべてのオブジェクトで利用できる、`minimum`と`maximum`のコーナー（`Point3D`）を持つ3D境界を返します（2Dオブジェクトはz = 0の平らなボックスを返します）。`layerRelative`が`False`の場合は実際のワールドZを返し、`True`の場合は従来のレイヤの高さを差し引いて、VectorScriptのGet3DCntrと一致させます。無効なオブジェクト、または範囲を持たないオブジェクトの場合は`None`。 |
| `GetCenter3D(layerRelative: bool = False) -> Point3D \| None` | 3Dバウンディングボックスの中心（layerRelative = `True`でのVectorScriptのGet3DCntr）。 |
| `GetSize3D() -> Point3D \| None` | 3Dバウンディングボックスの寸法：x = 幅、y = 高さ、z = 奥行き（VectorScriptのGet3DInfo）。 |
| `Move(offset: Math.Point2D) -> bool` | 変換（操作によってはオブジェクトハンドルが変わる場合があります。オブジェクトはその変更に追従します）。 |
| `Move(dx: float, dy: float) -> bool` | 変換（操作によってはオブジェクトハンドルが変わる場合があります。オブジェクトはその変更に追従します）。 |
| `Rotate(angle: float, center: Math.Point2D) -> bool` | オブジェクトを`angle`ラジアンだけ、`center`を中心に回転します。変換（操作によってはオブジェクトハンドルが変わる場合があります。オブジェクトはその変更に追従します）。 |
| `Scale(scaleX: float, scaleY: float, center: Math.Point2D) -> bool` | オブジェクトを`scaleX` / `scaleY`で、`center`を基準に拡大縮小します。変換（操作によってはオブジェクトハンドルが変わる場合があります。オブジェクトはその変更に追従します）。 |
| `Mirror(axisStart: Math.Point2D, axisEnd: Math.Point2D) -> bool` | オブジェクトを`axisStart`から`axisEnd`への軸に対してミラー反転します。変換（操作によってはオブジェクトハンドルが変わる場合があります。オブジェクトはその変更に追従します）。 |

*ライフサイクル*

| メソッド | 説明 |
|---|---|
| `Reset() -> None` | オブジェクトが外部で変更されたことを描画エンジンに通知します。複数の低レベル編集をまとめて実行した後、またはオブジェクトが再生成を必要とするプラグインオブジェクトの場合に呼び出してください。 |
| `Delete(useUndo: bool = True) -> bool` | ファイルからオブジェクトを削除します。オブジェクトは無効になります。 |
| `ConvertToPolygon(keepOriginal: bool = False, resolution: int = 0) -> PolygonObject` | 新しい多角形／曲線オブジェクトへの変換。`keepOriginal`を指定しない場合、その場での変換であっても、このオブジェクトは結果に置き換えられ、無効になります。変換に失敗した場合、元のオブジェクトは変更されません。`resolution`が0の場合は、ファイルの円周の分割数を使用します。 |
| `ConvertToPolyline(keepOriginal: bool = False) -> PolylineObject` | オブジェクトを曲線に変換します。新しい多角形／曲線オブジェクトへの変換。`keepOriginal`を指定しない場合、その場での変換であっても、このオブジェクトは結果に置き換えられ、無効になります。変換に失敗した場合、元のオブジェクトは変更されません。`resolution`が0の場合は、ファイルの円周の分割数を使用します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`：オブジェクトが有効な場合はTrue（`IsValid()`と同じ）。 |
| `==` | `__eq__(o: PrimitiveObject) -> bool` | `a == b`：両方のオブジェクトが同じ図面オブジェクトを参照している場合はTrue。 |
| `!=` | `__ne__(o: PrimitiveObject) -> bool` | `a != b`：オブジェクトが異なる図面オブジェクトを参照している場合はTrue。 |

#### PrimitiveObject.Bounds3D

> **完全修飾名:** `api.PrimitiveObject.Bounds3D` · **継承元:** `api.Object`

ワールド単位の、座標軸に平行な3Dバウンディングボックス

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Bounds3D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Bounds3D(minimum, maximum)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `minimum` | `Point3D` | 最小座標のコーナー。 |
| `maximum` | `Point3D` | 最大座標のコーナー。 |

### Locus2DObject

> **完全修飾名:** `api.Locus2DObject` · **継承元:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

2D 基準点（`ObjectType.Locus`）：参照用の点。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Locus2DObject(h: Handle)` | 既存の2D 基準点`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(position: Math.Point2D) -> Locus2DObject` *静的* | アクティブレイヤ／現在のコンテナに基準点を作成します。 |
| `Duplicate() -> Locus2DObject` | 図面内の2D 基準点を複製し、コピーを返します。 |
| `GetPosition() -> Math.Point2D \| None` | 位置を返します。 |
| `SetPosition(position: Math.Point2D) -> bool` | 位置を設定します。 |
| `GetMasterSnapPoint() -> bool \| None` | 基準点がシンボル定義内にある場合のスナップ点の動作。 |
| `SetMasterSnapPoint(isMasterSnap: bool) -> bool` | *マスタースナップポイント*をオンまたはオフにします（基準点がシンボル定義内にある場合のスナップ点の動作）。 |
| `GetShowMasterSnapOutsideSnapBox() -> bool \| None` | *スナップボックスの外でもマスタースナップを表示*がオンかどうか。 |
| `SetShowMasterSnapOutsideSnapBox(show: bool) -> bool` | *スナップボックスの外でもマスタースナップを表示*をオンまたはオフにします。 |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | 基準点から`pt`までの距離。 |

継承：[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

### Line2DObject

> **完全修飾名:** `api.Line2DObject` · **継承元:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

2D直線（`ObjectType.Line`）：二点間の直線の線分。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Line2DObject(h: Handle)` | 既存の直線`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(start: Math.Point2D, end: Math.Point2D) -> Line2DObject` *静的* | アクティブレイヤ／現在のコンテナに直線を作成します。 |
| `Create(line: Math.Line2D) -> Line2DObject` *静的* | アクティブレイヤ／現在のコンテナに直線を作成します。 |
| `Duplicate() -> Line2DObject` | 図面内の直線を複製し、コピーを返します。 |

*ジオメトリ*

| メソッド | 説明 |
|---|---|
| `GetLine() -> Math.Line2D \| None` | 直線を返します。 |
| `SetLine(line: Math.Line2D) -> bool` | 直線を設定します。 |
| `SetLine(start: Math.Point2D, end: Math.Point2D) -> bool` | 直線を設定します。 |
| `GetStartPoint() -> Math.Point2D \| None` | 始点を返します。 |
| `SetStartPoint(pt: Math.Point2D) -> bool` | 始点を設定します。 |
| `GetEndPoint() -> Math.Point2D \| None` | 終点を返します。 |
| `SetEndPoint(pt: Math.Point2D) -> bool` | 終点を設定します。 |

*派生値*

| メソッド | 説明 |
|---|---|
| `GetLength() -> float \| None` | 長さを返します。 |
| `SetLength(length: float) -> bool` | 長さを設定します（始点と方向は維持します）。 |
| `GetAngle() -> float \| None` | 角度を返します（始点から終点への方向）。 |
| `SetAngle(angle: float) -> bool` | 角度を設定します（始点を中心に回転し、長さを維持します）。 |
| `GetMidPoint() -> Math.Point2D \| None` | 中点を返します。 |
| `GetDirection() -> Math.Point2D \| None` | 方向を返します（始点から終点への単位ベクトル）。 |

*操作*

| メソッド | 説明 |
|---|---|
| `Reverse() -> bool` | 始点と終点を入れ替えます。 |
| `Extend(atStart: float, atEnd: float) -> bool` | 直線を始点の手前に`atStart`、終点の先に`atEnd`だけ延長します（負の値の場合は短くします）。 |
| `OffsetParallel(distance: float) -> bool` | 直線を`distance`だけ平行移動します（正の値の場合は始点 -> 終点の左側）。 |

*問い合わせ*

| メソッド | 説明 |
|---|---|
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | 線分上で`pt`に最も近い点。 |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | `pt`から線分までの最短距離。 |
| `Intersect(other: Line2DObject) -> Math.Point2D \| None` | 別の直線オブジェクトとの交点（線分同士）。 |

継承：[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

### RectangularObject

> **完全修飾名:** `api.RectangularObject` · **継承元:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

四角形クラスと角丸四角形クラスの共通基底クラス。ジオメトリは回転可能な四角形（`Math.RotatedRect2D`）で、コーナー（原点）、幅方向の辺の方向、幅、高さからなります。

**コンストラクタ**

Pythonからインスタンス化することはできません。インスタンスは他のAPI関数から返されます。

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `GetRect() -> Math.RotatedRect2D \| None` | ジオメトリ。 |
| `SetRect(rect: Math.RotatedRect2D) -> bool` | 矩形を設定します。 |
| `GetOrigin() -> Math.Point2D \| None` | 原点を返します。 |
| `GetDirection() -> Math.Point2D \| None` | 方向を返します（幅方向の辺に沿った単位ベクトル）。 |
| `GetWidth() -> float \| None` | 幅を返します。 |
| `SetWidth(width: float) -> bool` | 幅を設定します（原点のコーナーは維持します）。 |
| `GetHeight() -> float \| None` | 高さを返します。 |
| `SetHeight(height: float) -> bool` | 高さを設定します（原点のコーナーは維持します）。 |
| `SetSize(width: float, height: float, keepCenter: bool = True) -> bool` | サイズを設定します。 |
| `GetCenter() -> Math.Point2D \| None` | 中心を返します。 |
| `SetCenter(center: Math.Point2D) -> bool` | 中心を設定します（オブジェクトを移動します）。 |
| `GetAngle() -> float \| None` | 角度を返します（幅方向の辺の角度）。 |
| `SetAngle(angle: float) -> bool` | 角度を設定します（中心の周りに回転します）。 |
| `IsAxisAligned() -> bool \| None` | 四角形が回転していない場合はTrue（辺が座標軸に平行）。 |
| `GetCorners() -> tuple[Math.Point2D * 4] \| None` | 原点から反時計回りに並んだコーナー（幅と高さが正の場合）。 |
| `SetBounds(bounds: Math.Rect2D) -> bool` | 回転していない四角形を設定します。 |

*問い合わせ*

| メソッド | 説明 |
|---|---|
| `Contains(pt: Math.Point2D) -> bool` | `pt`が四角形の内側（または境界上）にある場合はTrue。 |
| `GetPolygon() -> Math.Polygon2D \| None` | 多角形を返します（四つのコーナー。角の丸みは無視されます）。 |

継承：[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

### RectangleObject

> **完全修飾名:** `api.RectangleObject` · **継承元:** [`RectangularObject`](#rectangularobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

四角形（`ObjectType.Box`）。回転している場合もあります。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RectangleObject(h: Handle)` | 既存の四角形`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(rect: Math.RotatedRect2D) -> RectangleObject` *静的* | アクティブレイヤ／現在のコンテナに四角形を作成します。幅と高さはゼロであってはなりません。 |
| `Create(bounds: Math.Rect2D) -> RectangleObject` *静的* | アクティブレイヤ／現在のコンテナに四角形を作成します。幅と高さはゼロであってはなりません。 |
| `Create(center: Math.Point2D, width: float, height: float, angle: float = 0.0) -> RectangleObject` *静的* | アクティブレイヤ／現在のコンテナに四角形を作成します。幅と高さはゼロであってはなりません。 |
| `Duplicate() -> RectangleObject` | 図面内の四角形を複製し、コピーを返します。 |
| `IsSquare() -> bool \| None` | 幅と高さが等しい場合はTrue。 |

継承：[`RectangularObject`](#rectangularobject)、[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

### CornerDiameters

> **完全修飾名:** `api.CornerDiameters` · **継承元:** `api.Object`

角丸四角形の角の丸み：幅方向の辺（alongWidth）と高さ方向の辺（alongHeight）に沿った、角の楕円の直径。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `CornerDiameters()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `CornerDiameters(alongWidth, alongHeight)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: CornerDiameters) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: CornerDiameters) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `alongWidth` | `float` | 幅方向の辺に沿った角の直径。 |
| `alongHeight` | `float` | 高さ方向の辺に沿った角の直径。 |

### RoundRectObject

> **完全修飾名:** `api.RoundRectObject` · **継承元:** [`RectangularObject`](#rectangularobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

角丸四角形（`ObjectType.RoundedRectangle`）。回転している場合もあります。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RoundRectObject(h: Handle)` | 既存の角丸四角形`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(rect: Math.RotatedRect2D, corners: CornerDiameters, proportional: bool = False) -> RoundRectObject` *静的* | アクティブレイヤ／現在のコンテナに角丸四角形を作成します。幅と高さはゼロであってはなりません。`proportional`を指定すると、対話的にサイズを変更した際、四角形に合わせて角の直径も拡大縮小されます。 |
| `Create(bounds: Math.Rect2D, corners: CornerDiameters, proportional: bool = False) -> RoundRectObject` *静的* | アクティブレイヤ／現在のコンテナに角丸四角形を作成します。幅と高さはゼロであってはなりません。`proportional`を指定すると、対話的にサイズを変更した際、四角形に合わせて角の直径も拡大縮小されます。 |
| `Create(center: Math.Point2D, width: float, height: float, cornerRadius: float, angle: float = 0.0) -> RoundRectObject` *静的* | アクティブレイヤ／現在のコンテナに角丸四角形を作成します。幅と高さはゼロであってはなりません。`proportional`を指定すると、対話的にサイズを変更した際、四角形に合わせて角の直径も拡大縮小されます。 |
| `Duplicate() -> RoundRectObject` | 図面内の角丸四角形を複製し、コピーを返します。 |

*角の丸み*

| メソッド | 説明 |
|---|---|
| `GetCornerDiameters() -> CornerDiameters \| None` | 角の直径を返します。 |
| `SetCornerDiameters(corners: CornerDiameters) -> bool` | 角の直径を設定します。 |
| `GetCornerRadius() -> float \| None` | 円形の角の半径（角が楕円形の場合は平均）。 |
| `SetCornerRadius(radius: float) -> bool` | 角の半径を設定します（円形の角の半径（角が楕円形の場合は平均））。 |
| `HasCircularCorners() -> bool \| None` | 角が円形の場合はTrue（角の幅と高さが等しい）。 |

継承：[`RectangularObject`](#rectangularobject)、[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

### ArcObject

> **完全修飾名:** `api.ArcObject` · **継承元:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

円弧（`ObjectType.Arc`）。角度はX軸から反時計回りのラジアンです。ファイルは常に円弧を反時計回りに保存します。セッターに渡された負の円弧角は正規化されるため、`GetSweepAngle()`は常に正です。円全体も円弧です。CircleObjectも参照してください。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ArcObject(h: Handle)` | 既存の円弧`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue（円全体を含む任意の`ObjectType.Arc`）。 |
| `Create(arc: Math.Arc2D) -> ArcObject` *静的* | アクティブレイヤ／現在のコンテナに円弧を作成します。半径と円弧角はゼロであってはなりません。 |
| `Create(center: Math.Point2D, radius: float, startAngle: float, sweepAngle: float) -> ArcObject` *静的* | アクティブレイヤ／現在のコンテナに円弧を作成します。半径と円弧角はゼロであってはなりません。 |
| `CreateThreePoints(start: Math.Point2D, onArc: Math.Point2D, end: Math.Point2D) -> ArcObject` *静的* | アクティブレイヤ／現在のコンテナに、三点`start`、`onArc`、`end`を通る円弧を作成します。 |
| `Duplicate() -> ArcObject` | 図面内の円弧を複製し、コピーを返します。 |

*ジオメトリ*

| メソッド | 説明 |
|---|---|
| `GetArc() -> Math.Arc2D \| None` | 円弧を返します。 |
| `SetArc(arc: Math.Arc2D) -> bool` | 円弧を設定します。 |
| `GetCenter() -> Math.Point2D \| None` | 中心を返します。 |
| `SetCenter(center: Math.Point2D) -> bool` | 中心を設定します。 |
| `GetRadius() -> float \| None` | 半径を返します。 |
| `SetRadius(radius: float) -> bool` | 半径を設定します。 |
| `GetStartAngle() -> float \| None` | 開始角を返します。 |
| `SetStartAngle(angle: float) -> bool` | 開始角を設定します（終了角は維持します）。 |
| `GetSweepAngle() -> float \| None` | 円弧角を返します。 |
| `SetSweepAngle(sweep: float) -> bool` | 円弧角を設定します（開始角は維持します）。 |
| `GetEndAngle() -> float \| None` | 終了角を返します。 |
| `SetEndAngle(angle: float) -> bool` | 終了角を設定します（開始角は維持します）。 |
| `SetAngles(startAngle: float, sweepAngle: float) -> bool` | 角度を設定します。 |
| `GetStartPoint() -> Math.Point2D \| None` | 始点を返します。 |
| `GetEndPoint() -> Math.Point2D \| None` | 終点を返します。 |
| `GetMidPoint() -> Math.Point2D \| None` | 中点を返します。 |
| `GetChord() -> Math.Line2D \| None` | 弦を返します。 |

*測定値*

| メソッド | 説明 |
|---|---|
| `GetLength() -> float \| None` | 長さを返します。 |
| `GetChordLength() -> float \| None` | 弦の長さを返します。 |
| `GetSagitta() -> float \| None` | 矢高を返します。 |
| `IsCircle() -> bool \| None` | 円弧が円全体の場合はTrue。 |

*問い合わせ*

| メソッド | 説明 |
|---|---|
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | 円弧上で`pt`に最も近い点。 |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | `pt`から円弧までの最短距離。 |
| `Intersect(other: ArcObject) -> list[Math.Point2D]` | 円弧`other`との交点。 |
| `Intersect(line: Math.Line2D) -> list[Math.Point2D]` | 線分`line`との交点。 |

継承：[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

### CircleObject

> **完全修飾名:** `api.CircleObject` · **継承元:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

円。ファイル内では、円は円弧角が360度の円弧（`ObjectType.Arc`）です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `CircleObject(h: Handle)` | 既存の円`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue（全周の円弧角を持つ`ObjectType.Arc`）。 |
| `Create(circle: Math.Circle2D) -> CircleObject` *静的* | アクティブレイヤ／現在のコンテナに円を作成します。半径は正でなければなりません。 |
| `Create(center: Math.Point2D, radius: float) -> CircleObject` *静的* | アクティブレイヤ／現在のコンテナに円を作成します。半径は正でなければなりません。 |
| `CreateThreePoints(p1: Math.Point2D, p2: Math.Point2D, p3: Math.Point2D) -> CircleObject` *静的* | アクティブレイヤ／現在のコンテナに、三点`p1`、`p2`、`p3`を通る円を作成します。 |
| `Duplicate() -> CircleObject` | 図面内の円を複製し、コピーを返します。 |
| `AsArc() -> ArcObject` | 同じオブジェクトを`ArcObject`として参照します（円は全周の円弧角を持つ円弧です）。 |

*ジオメトリ*

| メソッド | 説明 |
|---|---|
| `GetCircle() -> Math.Circle2D \| None` | 円を返します。 |
| `SetCircle(circle: Math.Circle2D) -> bool` | 円を設定します。 |
| `GetCenter() -> Math.Point2D \| None` | 中心を返します。 |
| `SetCenter(center: Math.Point2D) -> bool` | 中心を設定します。 |
| `GetRadius() -> float \| None` | 半径を返します。 |
| `SetRadius(radius: float) -> bool` | 半径を設定します。 |
| `GetDiameter() -> float \| None` | 直径を返します。 |
| `SetDiameter(diameter: float) -> bool` | 直径を設定します。 |

*測定値*

| メソッド | 説明 |
|---|---|
| `GetCircumference() -> float \| None` | 円周を返します。 |

*問い合わせ*

| メソッド | 説明 |
|---|---|
| `Contains(pt: Math.Point2D) -> bool` | `pt`が円の内側（または円周上）にある場合はTrue。 |
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | 円周上で`pt`に最も近い点。 |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | `pt`から円周までの距離。 |
| `PointAt(angle: float) -> Math.Point2D \| None` | 角度`angle`にある円周上の点（X軸から反時計回りのラジアン）。 |
| `Intersect(other: CircleObject) -> list[Math.Point2D]` | 円`other`との交点。 |
| `Intersect(line: Math.Line2D) -> list[Math.Point2D]` | 線分`line`との交点。 |
| `GetTangentPoints(from_: Math.Point2D) -> list[Math.Point2D]` | `from_`に対する接点を返します。 |

継承：[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

### PolyObject

> **完全修飾名:** `api.PolyObject` · **継承元:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

多角形クラスと曲線クラスの共通基底クラス。頂点インデックスは0始まりです。頂点の表示状態は、その頂点を始点とする辺の表示状態を表します。

**コンストラクタ**

Pythonからインスタンス化することはできません。インスタンスは他のAPI関数から返されます。

**メソッド**

*頂点*

| メソッド | 説明 |
|---|---|
| `GetVertexCount() -> int` | 頂点項目の数。 |
| `GetVertex(index: int) -> Math.PolyVertex \| None` | `index`の頂点を返します。 |
| `GetVertexPoint(index: int) -> Math.Point2D \| None` | `index`の頂点の座標を返します。 |
| `SetVertexPoint(index: int, pt: Math.Point2D) -> bool` | `index`の頂点の座標を設定します（頂点タイプは維持します）。 |
| `GetVertexPoints() -> list[Math.Point2D]` | 頂点の座標を返します。 |
| `DeleteVertex(index: int) -> bool` | `index`の頂点を削除します。 |
| `DeleteAllVertices() -> bool` | すべての頂点を削除します。 |

*辺の表示状態*

| メソッド | 説明 |
|---|---|
| `GetVertexVisible(index: int) -> bool \| None` | `index`で*頂点を表示*がオンかどうか。 |
| `SetVertexVisible(index: int, visible: bool) -> bool` | `index`の頂点の表示状態を設定します。 |
| `SetAllVerticesVisible(visible: bool) -> bool` | *すべての頂点を表示*をオンまたはオフにします。 |

*閉じた形状／開いた形状*

| メソッド | 説明 |
|---|---|
| `IsClosed() -> bool \| None` | 図形が閉じている場合はTrue。 |
| `SetClosed(closed: bool) -> bool` | *閉じる*をオンまたはオフにします。 |

*ジオメトリ全体*

| メソッド | 説明 |
|---|---|
| `GetPolygon() -> Math.Polygon2D \| None` | 多角形を返します。 |

*向き*

| メソッド | 説明 |
|---|---|
| `IsClockwise() -> bool \| None` | 頂点が時計回りに並んでいる場合はTrue。 |
| `Reverse() -> bool` | 辺の表示状態を維持したまま、頂点の順序を逆にします。 |
| `SetClockwise(clockwise: bool) -> bool` | *時計回り*をオンまたはオフにします。 |
| `GetPolyArea() -> float \| None` | 測定（基底クラスのGetArea / GetPerimeterも、汎用オブジェクトの呼び出しを通じて同じ結果を返します）。 |
| `GetPolyPerimeter() -> float \| None` | 多角形の周長を返します。 |
| `GetCurveLength() -> float \| None` | オブジェクトのローカルXY平面内の、実際の曲線状の外側パス。これらは図面を変更せず、非表示の辺や閉じる辺を含み、穴を除外し、制御多角形の長さを使用しません。距離の範囲、一時的なNURBSパラメータ、端点の扱いについては、`Math.Polygon2D`を参照してください。 |
| `GetCurveLocationAtDistance(distance: float) -> Math.Polygon2D.CurveLocation \| None` | 距離`distance`における曲線上の位置を返します。 |
| `GetCurvePointAtDistance(distance: float) -> Math.Point2D \| None` | 距離`distance`における曲線上の点を返します。 |
| `GetCurveTangentAtDistance(distance: float) -> Math.Point2D \| None` | 距離`distance`における曲線の接線を返します。 |
| `GetCurveCurvatureAtDistance(distance: float) -> float \| None` | 距離`distance`における曲線の曲率を返します。 |
| `GetCurveClosestPoint(point: Math.Point2D) -> Math.Polygon2D.CurveLocation \| None` | `point`に最も近い曲線上の点を返します。 |
| `GetCurveDistanceTo(point: Math.Point2D) -> float \| None` | `point`までの曲線からの距離を返します。 |
| `DivideCurveByCount(count: int, includeEnd: bool = True) -> list[Math.Point2D] \| None` | 実際の曲線状のパスに沿って等間隔に配置された、ちょうど`count`（>= 2）個の点（`includeEnd=False`の場合は最後の端点／継ぎ目を省略）。失敗した場合は`None`。オブジェクトのローカルXY平面内の、実際の曲線状の外側パス。これらは図面を変更せず、非表示の辺や閉じる辺を含み、穴を除外し、制御多角形の長さを使用しません。距離の範囲、一時的なNURBSパラメータ、端点の扱いについては、`Math.Polygon2D`を参照してください。 |
| `Contains(pt: Math.Point2D) -> bool` | 頂点を結ぶ多角形に対する問い合わせ（曲線の頂点は制御点として扱います）。 |
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | 頂点を結ぶ多角形上で`pt`に最も近い点。頂点を結ぶ多角形に対する問い合わせ（曲線の頂点は制御点として扱います）。 |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | `pt`から頂点を結ぶ多角形までの距離。頂点を結ぶ多角形に対する問い合わせ（曲線の頂点は制御点として扱います）。 |
| `GetCentroid() -> Math.Point2D \| None` | 重心を返します。 |
| `IsConvex() -> bool \| None` | 図形が凸の場合はTrue。 |
| `IsSelfIntersecting() -> bool \| None` | 隣接していない二つの辺が交差する場合はTrue。 |
| `Intersect(line: Math.Line2D) -> list[Math.Point2D]` | 頂点を結ぶ多角形と線分`line`との交点。頂点を結ぶ多角形に対する問い合わせ（曲線の頂点は制御点として扱います）。 |
| `BooleanUnion(other: PolyObject) -> list[Handle]` | `other`との和集合：この図形の属性を持つ、コンテナに属さない結果ハンドルのリスト（空の場合もあります）。両方の入力は変更されません。結果を`PrimitiveObject(h).MoveToContainer(...)`で挿入するか、削除してください。入力が無効な場合は`RuntimeError`を送出します。 |
| `BooleanIntersection(other: PolyObject) -> list[Handle]` | `other`との共通部分：コンテナに属さない結果ハンドルのリスト（空の場合もあります）。両方の入力は変更されません。入力が無効な場合は`RuntimeError`を送出します。 |
| `BooleanDifference(other: PolyObject) -> list[Handle]` | この図形から`other`を引いた差分：コンテナに属さない結果ハンドルのリスト（空の場合もあります）。両方の入力は変更されません。入力が無効な場合は`RuntimeError`を送出します。 |
| `BooleanSymmetricDifference(other: PolyObject) -> list[Handle]` | 二つの図形のうち一方のみが覆う部分（対称差）：コンテナに属さない結果ハンドルのリスト（空の場合もあります）。両方の入力は変更されません。入力が無効な場合は`RuntimeError`を送出します。 |
| `IsCombinableShape(h: Handle) -> bool` *静的* | CombineShapesが`h`をオペランドとして受け付けるかどうか（2Dブール演算で扱える2D図形）。 |
| `AreShapesInOnePlane(first: Handle, second: Handle) -> bool` *静的* | CombineShapesで必要とされるように、`first`と`second`が一つの平面内にあるかどうか（同じ平面参照ID）。 |
| `AlignShapePlanes(first: Handle, second: Handle) -> bool` *静的* | 加工 > 貼り合わせ／切り欠き／抜き取りが図形を合成する前に行うように、同一平面上の二つの図形を一つの平面に移動します。その後、両方の図形が一つの平面内にあれば`True`（すでにそうであった場合も含む）。同一平面上にない場合、または図形がnull、合成できない、もしくは同じオブジェクトである場合は`False`。移動する図形の平面を変更し、取り消しを記録しません。呼び出す前に両方の図形を登録してください（`Document.AddBothSwapObject`）。 |
| `CombineShapes(operation: PolyObject.BooleanOperation, first: Handle, second: Handle) -> list[Handle]` *静的* | 2D図形`first`と`second`を`operation`で合成します。`first`の属性を持つ、コンテナに属さない結果ハンドルのリスト（空の場合もあります）を返し、入力は変更されません。入力が無効な場合（nullまたは合成できない図形、同じオブジェクトを二度指定、異なる平面内の図形、不明な演算）は`RuntimeError`を送出します。 |

継承：[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

#### PolyObject.BooleanOperation

> **完全修飾名:** `api.PolyObject.BooleanOperation` · **種類:** `IntEnum`

2Dブール関数の演算

| メンバー | 値 | 説明 |
|---|---|---|
| `Union` | `0` |  |
| `Intersection` | `1` |  |
| `Difference` | `2` | `first`から`second`を引いた差分。 |
| `SymmetricDifference` | `3` | 二つの図形のうち一方のみが覆う部分（対称差）。 |

### PolygonObject

> **完全修飾名:** `api.PolygonObject` · **継承元:** [`PolyObject`](#polyobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

多角形（`ObjectType.Polygon`、およびフリーハンド`ObjectType.FreehandPolygon`）：頂点はコーナー頂点のみ。曲線の頂点にはPolylineObjectを使用してください。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `PolygonObject(h: Handle)` | 既存の多角形`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(poly: Math.Polygon2D) -> PolygonObject` *静的* | アクティブレイヤ／現在のコンテナに多角形を作成します（少なくとも二つの頂点）。`poly`の曲線の頂点はコーナーとして追加されます。 |
| `Create(points: list[Math.Point2D], closed: bool = True) -> PolygonObject` *静的* | アクティブレイヤ／現在のコンテナに多角形を作成します（少なくとも二つの頂点）。`poly`の曲線の頂点はコーナーとして追加されます。 |
| `Create(rect: Math.Rect2D) -> PolygonObject` *静的* | アクティブレイヤ／現在のコンテナに多角形を作成します（少なくとも二つの頂点）。`poly`の曲線の頂点はコーナーとして追加されます。 |
| `CreateRegular(center: Math.Point2D, circumradius: float, sides: int, startAngle: float = 0.0) -> PolygonObject` *静的* | アクティブレイヤ／現在のコンテナに、`sides`個のコーナーを持ち、半径`circumradius`、中心`center`の円上に頂点がある正多角形を作成します（最初のコーナーは`startAngle`）。 |
| `Duplicate() -> PolygonObject` | 図面内の多角形を複製し、コピーを返します。 |
| `IsFreehand() -> bool \| None` | 多角形がフリーハンド（`ObjectType.FreehandPolygon`）の場合はTrue。 |

*頂点*

| メソッド | 説明 |
|---|---|
| `AddVertex(pt: Math.Point2D, visible: bool = True) -> bool` | `pt`に頂点を追加します。`visible`は、次の頂点への辺を描画するかどうかを制御します。 |
| `InsertVertex(beforeIndex: int, pt: Math.Point2D, visible: bool = True) -> bool` | `pt`にある頂点を頂点`beforeIndex`の前に挿入します。`visible`は辺の表示状態を制御します。 |
| `SetPolygon(poly: Math.Polygon2D) -> bool` | すべての頂点と閉じるフラグを置き換えます（曲線の頂点はコーナーとして設定されます）。 |
| `SetVertexPoints(points: list[Math.Point2D]) -> bool` | 頂点の座標を設定します（閉じるフラグは維持します）。 |

継承：[`PolyObject`](#polyobject)、[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

### PolylineObject

> **完全修飾名:** `api.PolylineObject` · **継承元:** [`PolyObject`](#polyobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

曲線（`ObjectType.Polyline`）：頂点をコーナー、ベジェ、キュービックスプライン、円弧、または半径の頂点にできる多角形状。頂点の座標は制御点です。曲線が通るのはコーナー頂点のみです（および、収まる場合は半径がゼロでない円弧頂点）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `PolylineObject(h: Handle)` | 既存の曲線`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(poly: Math.Polygon2D) -> PolylineObject` *静的* | アクティブレイヤ／現在のコンテナに曲線を作成します（少なくとも二つの頂点）。すべての頂点がコーナーであっても、結果は常に曲線です。 |
| `CreateCircle(center: Math.Point2D, radius: float) -> PolylineObject` *静的* | 円を形成する四つの半径頂点からなる閉じた曲線。 |
| `CreateFilletedRect(rect: Math.Rect2D, cornerRadius: float) -> PolylineObject` *静的* | 角をフィレットした四角形の閉じた曲線。 |
| `Duplicate() -> PolylineObject` | 図面内の曲線を複製し、コピーを返します。 |

*型付き頂点*

| メソッド | 説明 |
|---|---|
| `AddVertex(vertex: Math.PolyVertex) -> bool` | 頂点`vertex`を追加します（座標、頂点タイプ、円弧半径、辺の表示状態）。 |
| `AddVertex(pt: Math.Point2D, type: Math.VertexType = Math.VertexType.Corner, arcRadius: float = 0.0) -> bool` | `pt`に頂点タイプ`type`の頂点を追加します（半径頂点では`arcRadius`を使用）。 |
| `InsertVertex(beforeIndex: int, vertex: Math.PolyVertex) -> bool` | 頂点`vertex`を頂点`beforeIndex`の前に挿入します。 |
| `SetVertex(index: int, vertex: Math.PolyVertex) -> bool` | `index`の頂点を設定します。 |
| `GetVertexType(index: int) -> Math.VertexType \| None` | `index`の頂点タイプを返します。 |
| `SetVertexType(index: int, type: Math.VertexType) -> bool` | `index`の頂点タイプを設定します。 |
| `GetVertexArcRadius(index: int) -> float \| None` | `index`の頂点の円弧半径を返します（円弧頂点以外の頂点は0）。 |
| `SetVertexArcRadius(index: int, radius: float) -> bool` | `index`の頂点の円弧半径を設定します（その頂点を円弧頂点にします）。 |
| `GetVertexMaxRadius(index: int) -> float \| None` | 円弧頂点が隣接する頂点の間に収まる最大半径。 |
| `GetControlVertex(index: int) -> Math.PolyVertex \| None` | ファイルに保存された制御頂点（円弧頂点では、フィレットを定義する点）。 |
| `HasCurves() -> bool \| None` | 曲線が曲線の頂点（ベジェ、キュービックスプライン、円弧、または半径）を持つ場合はTrue。 |

*すべての頂点と閉じるフラグの置き換え*

| メソッド | 説明 |
|---|---|
| `SetPolygon(poly: Math.Polygon2D) -> bool` | 多角形を設定します。 |

継承：[`PolyObject`](#polyobject)、[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

### GroupObject

> **完全修飾名:** `api.GroupObject` · **継承元:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

グループ（`ObjectType.Group`）：他のオブジェクトを格納するコンテナ。メンバーはPrimitiveObjectのメンバーAPI（GetFirstMember、ForEachMember、GetMembers、...）で走査します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `GroupObject(h: Handle)` | 既存のグループ`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create() -> GroupObject` *静的* | アクティブレイヤ／現在のコンテナに空のグループを作成します。 |
| `Create(members: list[Handle]) -> GroupObject` *静的* | アクティブレイヤ／現在のコンテナにグループを作成し、その中に`members`を移動します。nullハンドルはスキップされます。 |
| `CreateFromSelection() -> GroupObject` *静的* | アクティブレイヤの選択オブジェクトをグループ化します（VectorScriptのGroup）。 |
| `Duplicate() -> GroupObject` | 図面内のグループを複製し、コピーを返します。 |
| `GetMemberCount() -> int \| None` | メンバー項目の数。 |
| `AddMember(h: Handle) -> bool` | `h`をグループ内の最後のメンバーとして移動し、グループの境界を更新します。 |
| `Ungroup() -> bool` | メンバーをグループのコンテナに移動し、グループを削除します。オブジェクトは無効になります。 |

継承：[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

### ParametricObject

> **完全修飾名:** `api.ParametricObject` · **継承元:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

スクリプトまたはコンパイル済みプラグインで定義された、任意の種類の汎用プラグインオブジェクト（パラメトリックオブジェクト、`ObjectType.Parametric`）。

このクラスは、そのプラグインに専用のクラスがない場合にのみ使用してください。専用のクラス（PlantObject、WindowObject、DataTagObject、...）はパラメータの意味を理解し、値を検証して、オブジェクトの整合性を維持します。このクラスは、未加工のパラメトリックレコードのフィールドをユニバーサル名で読み書きするだけです。

GetParameterDefinitions(universalName)（インスタンス不要）、またはインスタンスの`GetParameters()`でプラグインのパラメータを調べ、GetPluginKind(universalName)でオブジェクトの配置方法を調べてから、型付きのGet/SetParam*アクセサーを使用してください：

- string — 任意のフィールドタイプを文字列として扱う — GetParamString / SetParamString
- real — Real、Dimension、CoordLocX/Y、Angle、Area、Volume — GetParamReal / SetParamReal
- bool — Boolean — GetParamBool / SetParamBool
- int — Integer、DimStdPopUp — GetParamInt / SetParamInt
- popUp — N個から一つを選ぶ文字列。選択肢はGetParamChoicesで取得（インスタンスがない場合はGetDefinitionChoices） GetParamString / SetParamString

オブジェクトが無効な場合、パラメータが存在しない場合、またはその型がアクセサーと一致しない場合、型付きゲッターは`None`、セッターは`False`を返します。長さはワールド単位です。Angleフィールドは保存されたとおりの度単位です。パラメータを変更した後は、プラグインがジオメトリを再生成するように`Reset()`を呼び出してください。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ParametricObject(h: Handle)` | 既存のプラグインオブジェクト`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | 任意のプラグインオブジェクトの場合は`True`。 |
| `IsNamed(h: Handle, universalName: str) -> bool` *静的* | そのユニバーサル名（例："Door"）のプラグインオブジェクトの場合は`True`。 |
| `Create(universalName: str, location: Math.Point2D, angle: float = 0.0) -> ParametricObject` *静的* | アクティブレイヤ／現在のコンテナに、点に基づくプラグインオブジェクトを作成します。`angle`はラジアンです。 |
| `CreateFromPath(universalName: str, hPath: Handle) -> ParametricObject` *静的* | `hPath`（2Dの多角形状）をパスとして使用する、パスに基づくプラグインオブジェクトを作成します。 |
| `Duplicate() -> ParametricObject` | 図面内のプラグインオブジェクトを複製し、コピーを返します。 |

*プラグイン定義（ユニバーサル名を指定、インスタンス不要）*

| メソッド | 説明 |
|---|---|
| `GetDefinitionFormat(universalName: str) -> RecordFormat` *静的* | プラグインのパラメトリックレコードフォーマット。そのユニバーサル名のプラグインがインストールされていない場合は無効です。アクティブファイルにまだない場合は、フォーマットを追加します。 |
| `GetParameterDefinitions(universalName: str) -> list[RecordField]` *静的* | プラグインのパラメータを宣言順に返します。ユニバーサル名とローカライズされた名前、型、デフォルト値を含みます。そのユニバーサル名のプラグインがインストールされていない場合は空です。 |
| `GetDefinitionChoices(universalName: str, univParamName: str) -> list[str]` *静的* | プラグインのPopUpパラメータ`univParamName`のユニバーサルな選択肢を、そのプラグインのオブジェクトに対するGetParamChoicesと同じ順序で返します。プラグインやパラメータが不明な場合、またはパラメータがPopUpでない場合は空です。GetDefinitionFormatと同様に、プラグインのフォーマットがアクティブファイルにまだない場合、指定された`universalName`をそのまま名前として追加します。正確なユニバーサル名を渡してください（GetPluginKindを参照）。 |
| `GetPluginKind(universalName: str) -> ParametricObject.PluginKind \| None` *静的* | 正確にそのユニバーサル名を持つプラグインオブジェクトの種類を、Vectorworksのインストール済みプラグインの表から取得します。大文字と小文字は区別されます。Vectorworksは大文字と小文字を区別せずにプラグインを検索しますが、定義するフォーマットには指定された名前を付けるため、正確なユニバーサル名のみを受け付けます。正確にその名前のプラグインオブジェクトがインストールされていない場合（不明な名前、大文字と小文字が異なる名前、またはメニューコマンドやツール）は空です。ファイルは一切変更しません。 |

*プラグインのユニバーサル名（例："Door"）*

| メソッド | 説明 |
|---|---|
| `GetParametricName() -> str \| None` | パラメトリック名を返します。 |
| `GetParameters() -> list[RecordField]` | このオブジェクトのプラグインのパラメータ。GetParameterDefinitionsを参照してください。 |
| `GetParamNames() -> list[str]` | パラメータ名を返します。 |
| `HasParam(univParamName: str) -> bool` | オブジェクトがユニバーサル名`univParamName`のパラメータを持つ場合はTrue。 |
| `GetParamType(univParamName: str) -> RecordFieldType \| None` | `univParamName`のパラメータの型を返します。 |
| `GetParamChoices(univParamName: str) -> list[str]` | PopUpパラメータのユニバーサルな選択肢を順に返します。他のパラメータの場合は空です。 |
| `GetParamString(univParamName: str) -> str \| None` | `univParamName`のパラメータの文字列を返します。 |
| `SetParamString(univParamName: str, value: str) -> bool` | パラメータの文字列を設定します。 |
| `GetParamReal(univParamName: str) -> float \| None` | `univParamName`のパラメータの実数値を返します。 |
| `SetParamReal(univParamName: str, value: float) -> bool` | パラメータの実数値を設定します。 |
| `GetParamBool(univParamName: str) -> bool \| None` | `univParamName`で*パラメータの真偽値*がオンかどうか。 |
| `SetParamBool(univParamName: str, value: bool) -> bool` | パラメータの真偽値を設定します。 |
| `GetParamInt(univParamName: str) -> int \| None` | `univParamName`のパラメータの整数値を返します。 |
| `SetParamInt(univParamName: str, value: int) -> bool` | パラメータの整数値を設定します。 |
| `GetPathObject() -> Handle` | パスに基づくプラグインオブジェクトのパスオブジェクト。点に基づくものの場合はnullです。 |

継承：[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

#### ParametricObject.PluginKind

> **完全修飾名:** `api.ParametricObject.PluginKind` · **種類:** `IntEnum`

プラグインのオブジェクトの配置方法：プラグインが宣言するオブジェクトのサブタイプ。

| メンバー | 値 | 説明 |
|---|---|---|
| `Point` | `0` | 回転を指定して点に挿入します。例：ドアや植栽（ハイブリッドシンボルのようなプラグイン）。 |
| `Linear` | `1` | 始点から終点への直線として描画します。 |
| `Rectangle` | `2` | 四角形として描画します。 |
| `Path2D` | `3` | 引き継ぐ2Dパスに基づいて構築します：CreateFromPath（Vectorworksはそのパスを曲線にします）。 |
| `Path3D` | `4` | 引き継ぐ3Dパスに基づいて構築します：CreateFromPath（NURBS曲線、3D 多角形、...） |
| `Custom` | `5` | プラグインが自分自身の挿入を処理します。 |

### TextObject

> **完全修飾名:** `api.TextObject` · **継承元:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

文字列（`ObjectType.Text`）：原点に配置する書式付きの文字列。文字インデックスは0始まりで、UTF-16コード単位を数えます（基本多言語面の外の文字は二単位を占めます）。文字列はUTF-8で受け渡し、行は"\r"で区切ります（GetNewLineを参照）。書式のセッターは範囲[first, first + count)に作用します。`count`は文字列の末尾までに制限されるため、デフォルトの(0, `kToEnd`)では文字列全体に書式を適用します。名前に"Points"とあるものを除き、サイズはワールド単位です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `TextObject(h: Handle)` | 既存の文字列`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスで表す種類のオブジェクトを参照している場合はTrue。 |
| `Create(text: str, origin: Math.Point2D, width: float = 0.0) -> TextObject` *静的* | アクティブレイヤ／現在のコンテナに、ファイルのデフォルト文字属性を使用する文字列オブジェクトを作成します。`width` > 0の場合は、固定幅（折り返し）の文字列オブジェクトを作成します。 |
| `Duplicate() -> TextObject` | 図面内の文字列を複製し、コピーを返します。 |
| `CreateUnlinkedCopy() -> TextObject` | 書式は維持するものの、レコードフィールドにはリンクされていない文字列のコピー。 |

*内容*

| メソッド | 説明 |
|---|---|
| `GetText() -> str \| None` | 文字列を返します。 |
| `SetText(text: str, clearFormatting: bool = False) -> bool` | 文字列を置き換えます。`clearFormatting`はすべての文字の書式を最初の文字の書式にリセットします。 |
| `GetLength() -> int \| None` | 長さを返します。 |
| `InsertText(text: str, beforeIndex: int) -> bool` | 文字`beforeIndex`の前に挿入します（`GetLength()`の場合は末尾に追加）。新しい文字列は隣接する文字の書式を継承します。 |
| `AppendText(text: str) -> bool` | 文字列の末尾に`text`を追加します。新しい文字列は最後の文字の書式を継承します。 |
| `DeleteText(first: int = 0, count: int = kToEnd) -> bool` | `count`文字を`first`から削除します（デフォルト：文字列全体）。 |
| `GetNewLine() -> str` *静的* | 文字列オブジェクトで使用する行区切り："\r"。 |

*配置*

| メソッド | 説明 |
|---|---|
| `GetOrigin() -> Math.Point2D \| None` | 原点を返します。 |
| `SetOrigin(origin: Math.Point2D) -> bool` | 原点を設定します。 |
| `GetAngle() -> float \| None` | ラジアンの回転角（反時計回り）。 |
| `IsFlipped() -> bool \| None` | 文字列が反転している場合はTrue（上下にミラー反転）。 |
| `SetOrientation(angle: float, flipped: bool = False) -> bool` | 向きを設定します。 |
| `GetBoxCorners() -> tuple[Math.Point2D * 4] \| None` | テキストボックスのコーナー（回転している場合もあります）：左上、右上、右下、左下。 |
| `GetCharIndexAt(point: Math.Point2D) -> int \| None` | `point`に最も近い文字のインデックス。 |

*レイアウト*

| メソッド | 説明 |
|---|---|
| `GetHorizontalAlignment() -> TextObject.HorizontalAlignment \| None` | 水平方向の配置揃えを返します。 |
| `SetHorizontalAlignment(alignment: TextObject.HorizontalAlignment) -> bool` | 水平方向の配置揃えを設定します。 |
| `GetVerticalAlignment() -> TextObject.VerticalAlignment \| None` | 垂直方向の配置揃えを返します。 |
| `SetVerticalAlignment(alignment: TextObject.VerticalAlignment) -> bool` | 垂直方向の配置揃えを設定します。 |
| `GetSpacing() -> TextObject.Spacing \| None` | 行間を返します。 |
| `GetLeading() -> float \| None` | ワールド単位でのカスタム行間距離。`GetSpacing()`が`TextObject.Spacing.Custom`の場合に意味を持ちます。 |
| `SetSpacing(spacing: TextObject.Spacing, leading: float = 0.0) -> bool` | `leading`は`TextObject.Spacing.Custom`でのみ使用します。 |
| `GetWidth() -> float \| None` | ワールド単位でのテキストボックスの幅。 |
| `SetWidth(width: float) -> bool` | 折り返し幅を設定します。`IsWrapped()`が`True`の場合に適用されます。 |
| `IsWrapped() -> bool \| None` | `GetWidth()`で行を折り返す固定幅の文字列。 |
| `SetWrapped(wrapped: bool) -> bool` | *文字の折り返し*をオンまたはオフにします（`GetWidth()`で行を折り返す固定幅の文字列）。 |
| `GetLineHeight(charIndex: int = 0) -> float \| None` | 文字`charIndex`を含む行の高さ（ワールド単位）。 |
| `GetLineCount() -> int \| None` | 行（折り返し後）。 |
| `GetLineStarts() -> list[int]` | 行の開始位置を返します（各行の最初の文字のインデックス）。 |
| `GetLines() -> list[str]` | 行を返します（区切り文字を含まない各行の文字列）。 |
| `GetCharWidths() -> list[float]` | 各文字の送り幅（ワールド単位）。 |

*`charIndex`の文字書式*

| メソッド | 説明 |
|---|---|
| `GetFont(charIndex: int = 0) -> str \| None` | `charIndex`のフォントを返します。 |
| `GetFontIndex(charIndex: int = 0) -> int \| None` | `charIndex`のフォントインデックスを返します。 |
| `GetSize(charIndex: int = 0) -> float \| None` | `charIndex`のサイズを返します。 |
| `GetSizePoints(charIndex: int = 0) -> float \| None` | `charIndex`のサイズをポイント単位で返します。 |
| `GetStyle(charIndex: int = 0) -> int \| None` | `charIndex`のスタイルを返します。 |
| `GetCustomStyle(charIndex: int = 0) -> int \| None` | `charIndex`のカスタムスタイルを返します。 |
| `GetColor(charIndex: int = 0) -> ColorRGB \| None` | `charIndex`の色を返します。 |
| `GetColorIndex(charIndex: int = 0) -> int \| None` | `charIndex`の色インデックスを返します。 |

*文字間隔係数*

| メソッド | 説明 |
|---|---|
| `GetTracking(charIndex: int = 0) -> float \| None` | 1 = 標準、0.1 .. 10。 |
| `GetStyleRuns() -> list[TextObject.StyleRun]` | 文字列全体の書式が共通する連続範囲を順に返します。 |
| `SetFont(fontName: str, first: int = 0, count: int = kToEnd) -> bool` | 範囲の文字書式（範囲が空、またはフォントが不明な場合は失敗します）。 |
| `SetFontIndex(fontIndex: int, first: int = 0, count: int = kToEnd) -> bool` | `fontIndex`でフォントインデックスを設定します。 |
| `SetSize(size: float, first: int = 0, count: int = kToEnd) -> bool` | サイズを設定します。 |
| `SetSizePoints(points: float, first: int = 0, count: int = kToEnd) -> bool` | サイズをポイント単位で設定します。 |
| `SetStyle(style: int, first: int = 0, count: int = kToEnd) -> bool` | 範囲のスタイルフラグを置き換えます（`kStylePlain`でクリアします）。 |
| `SetCustomStyle(customStyle: int, first: int = 0, count: int = kToEnd) -> bool` | カスタムスタイルを設定します。 |
| `SetColor(color: ColorRGB, first: int = 0, count: int = kToEnd) -> bool` | 色を設定します。 |
| `SetColorIndex(color: int, first: int = 0, count: int = kToEnd) -> bool` | 色インデックスを設定します。 |
| `SetTracking(tracking: float, first: int = 0, count: int = kToEnd) -> bool` | `tracking`は0.1 .. 10の範囲でなければなりません。 |
| `GetTextStyleRef() -> int \| None` | 文字スタイルリソース（TextStyleを参照）。0 = 文字スタイルなし。 |
| `GetTextStyleRefAt(charIndex: int) -> int \| None` | `charIndex`の文字スタイル参照を返します。 |
| `SetTextStyleRef(textStyle: int, first: int = 0, count: int = kToEnd) -> bool` | 文字スタイル参照を設定します。文字スタイルリソース（TextStyleを参照）。0 = 文字スタイルなし。 |
| `IsTextStyleByClass() -> bool \| None` | 文字列がクラスから文字スタイルを取得する場合はTrue。 |
| `IsTextStyleByClassAt(charIndex: int) -> bool \| None` | 文字`charIndex`がクラスから文字スタイルを取得する場合はTrue。 |
| `SetTextStyleByClass(first: int = 0, count: int = kToEnd) -> bool` | 範囲をオブジェクトのクラスの文字スタイルに従わせます。 |
| `UpdateTextStyleSize() -> bool` | オブジェクトを縮尺が異なるレイヤに移動した後、文字スタイルのサイズを再調整します。 |
| `GetTabStops() -> list[TextObject.TabStop]` | タブストップ（0始まり、オフセット順）。 |
| `GetTabStopCount() -> int \| None` | タブストップ項目の数。 |
| `AddTabStop(offset: float) -> bool` | `offset`に左揃えのタブストップを追加します。 |
| `MoveTabStop(index: int, offset: float) -> bool` | タブストップ`index`を`offset`に移動します（文字列の左端からのワールド単位）。 |
| `RemoveTabStop(index: int) -> bool` | Vectorworksは最初のタブストップを維持します。インデックス0は削除できません。 |
| `GetRepeatingTabStop() -> float \| None` | 繰り返しタブストップの間隔（ワールド単位、0 = なし）。 |
| `SetRepeatingTabStop(interval: float) -> bool` | 繰り返しタブストップを設定します（繰り返しタブストップの間隔（ワールド単位、0 = なし））。 |

*フラグ*

| メソッド | 説明 |
|---|---|
| `HasTightFill() -> bool \| None` | 面がテキストボックス全体ではなく、文字列の境界のみを覆います。 |
| `SetTightFill(tightFill: bool) -> bool` | *文字部分のみアミ掛け*をオンまたはオフにします（面がテキストボックス全体ではなく、文字列の境界のみを覆います）。 |
| `IsLinkedToRecord() -> bool \| None` | シンボルのレコードフィールドにリンクされた文字列。 |
| `UnlinkFromRecord() -> bool` | 文字列をシンボルのレコードフィールドから切り離します。通常の文字列になります。 |
| `IsNoteText() -> bool \| None` | 文字列が寸法の注記である場合はTrue。 |
| `IsSIAElevationText() -> bool \| None` | 文字列がSIA高さ表記である場合はTrue。 |
| `IsRightToLeft() -> bool \| None` | 文字列が右から左に進む場合はTrue。 |
| `FormatAsSIA(centimeters: str, millimeters: str, superscriptPercent: float = 100.0) -> bool` | SIA書式（スイス式の表記：センチメートルに上付きのミリメートルを添える）。 |
| `FormatValueAsSIA(value: float, alwaysMeters: bool, superscriptPercent: float = 100.0) -> bool` | `value`（ワールド単位）をSIA文字列として書式設定します。`alwaysMeters`はメートルを強制します。 |
| `FormatSegmentAsSIA(first: int, count: int, superscriptPercent: float = 100.0) -> bool` | `count`文字を`first`からSIA表記で書式設定します（センチメートルに上付きのミリメートルを添える）。 |

*フォント*

| メソッド | 説明 |
|---|---|
| `FontIndexFromName(fontName: str) -> int \| None` *静的* | 名前が`fontName`のフォントのフォントインデックス。 |
| `FontNameFromIndex(fontIndex: int) -> str \| None` *静的* | インデックス`fontIndex`のフォントの名前。 |
| `PointsToWorld(points: float) -> float` *静的* | 用紙上のポイント単位のサイズを、ワールド単位の長さに変換します。 |
| `WorldToPoints(length: float) -> float` *静的* | ワールド単位の長さを、用紙上のポイント単位のサイズに変換します。 |

**定数**

| 定数 | 型 | 値 | 説明 |
|---|---|---|---|
| `TextObject.kStylePlain` | `int` | `0` | 文字スタイルフラグ（GetStyle / SetStyle）。'\|'で組み合わせることができます。アウトラインとシャドウはmacOSでのみ表示されます。 |
| `TextObject.kStyleBold` | `int` | `1` | 文字スタイルフラグ（GetStyle / SetStyle）。'\|'で組み合わせることができます。アウトラインとシャドウはmacOSでのみ表示されます。 |
| `TextObject.kStyleItalic` | `int` | `2` | 文字スタイルフラグ（GetStyle / SetStyle）。'\|'で組み合わせることができます。アウトラインとシャドウはmacOSでのみ表示されます。 |
| `TextObject.kStyleUnderline` | `int` | `4` | 文字スタイルフラグ（GetStyle / SetStyle）。'\|'で組み合わせることができます。アウトラインとシャドウはmacOSでのみ表示されます。 |
| `TextObject.kStyleOutline` | `int` | `8` | 文字スタイルフラグ（GetStyle / SetStyle）。'\|'で組み合わせることができます。アウトラインとシャドウはmacOSでのみ表示されます。 |
| `TextObject.kStyleShadow` | `int` | `16` | 文字スタイルフラグ（GetStyle / SetStyle）。'\|'で組み合わせることができます。アウトラインとシャドウはmacOSでのみ表示されます。 |
| `TextObject.kCustomStyleNone` | `int` | `0` | カスタムスタイルフラグ（GetCustomStyle / SetCustomStyle）。 |
| `TextObject.kCustomDiagonalFraction` | `int` | `1` | カスタムスタイルフラグ（GetCustomStyle / SetCustomStyle）。 |
| `TextObject.kCustomVerticalFraction` | `int` | `2` | カスタムスタイルフラグ（GetCustomStyle / SetCustomStyle）。 |
| `TextObject.kCustomSuperscript` | `int` | `32` | カスタムスタイルフラグ（GetCustomStyle / SetCustomStyle）。 |
| `TextObject.kCustomSubscript` | `int` | `64` | カスタムスタイルフラグ（GetCustomStyle / SetCustomStyle）。 |
| `TextObject.kToEnd` | `int` | `2**64 - 1` | 「文字列の末尾まで」を意味する範囲の文字数。 |

継承：[`PrimitiveObject`](#primitiveobject)のすべてのメンバー。

#### TextObject.StyleRun

> **完全修飾名:** `api.TextObject.StyleRun` · **継承元:** `api.Object`

同じ書式を共有する文字の連続範囲

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `StyleRun()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `StyleRun(start, length, font, fontIndex, size, sizePoints, style, customStyle, color, textStyle, tracking)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `start` | `int` | 連続範囲の最初の文字のインデックス。 |
| `length` | `int` | 連続範囲の文字数。 |
| `font` | `str` | フォント名。 |
| `fontIndex` | `int` | フォントインデックス。 |
| `size` | `float` | ワールド単位。 |
| `sizePoints` | `float` | 用紙上のポイント。 |
| `style` | `int` | `TextObject.kStyle...`フラグ。 |
| `customStyle` | `int` | `TextObject.kCustom...`フラグ。 |
| `color` | `ColorRGB` | 文字の色（色インデックス）。 |
| `textStyle` | `int` | 文字スタイルリソース。0 = なし。 |
| `tracking` | `float` | 文字間隔係数、1 = 標準。 |

#### TextObject.TabStop

> **完全修飾名:** `api.TextObject.TabStop` · **継承元:** `api.Object`

タブストップ：文字列の左端からのワールド単位のオフセットと配置揃え。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `TabStop()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `TabStop(offset, alignment)` | フィールド値：すべてのフィールドを位置引数で（この順序で）指定するか、任意のフィールドをキーワード引数で指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `offset` | `float` | 文字列の左端からのワールド単位。 |
| `alignment` | `TextObject.TabAlignment` | タブストップでの文字列の配置揃え。 |

#### TextObject.HorizontalAlignment

> **完全修飾名:** `api.TextObject.HorizontalAlignment` · **種類:** `IntEnum`

文字列の水平方向の配置揃え。

| メンバー | 値 | 説明 |
|---|---|---|
| `Left` | `1` |  |
| `Center` | `2` |  |
| `Right` | `3` |  |
| `Justify` | `4` |  |

#### TextObject.VerticalAlignment

> **完全修飾名:** `api.TextObject.VerticalAlignment` · **種類:** `IntEnum`

原点を基準とする文字列の垂直方向の配置揃え。

| メンバー | 値 | 説明 |
|---|---|---|
| `TopBox` | `1` | テキストボックスの上端。 |
| `TopBaseline` | `2` | 最初の行のベースライン。 |
| `CenterBox` | `3` |  |
| `BottomBaseline` | `4` | 最後の行のベースライン。 |
| `BottomBox` | `5` |  |

#### TextObject.Spacing

> **完全修飾名:** `api.TextObject.Spacing` · **種類:** `IntEnum`

文字列の行間。`Custom`は`SetSpacing`に渡された行送りを使用します。

| メンバー | 値 | 説明 |
|---|---|---|
| `Custom` | `0` | カスタム行送り。GetLeadingを参照してください。 |
| `Single` | `2` |  |
| `OneAndHalf` | `3` |  |
| `Double` | `4` |  |

#### TextObject.TabAlignment

> **完全修飾名:** `api.TextObject.TabAlignment` · **種類:** `IntEnum`

タブストップでの文字列の配置揃え。

| メンバー | 値 | 説明 |
|---|---|---|
| `Left` | `1` |  |
| `Right` | `2` |  |
| `Center` | `3` |  |
| `Decimal` | `4` |  |

---

[一覧に戻る](README.md) · [先頭に戻る](#objectprimitives--2d-primitive-objects)
