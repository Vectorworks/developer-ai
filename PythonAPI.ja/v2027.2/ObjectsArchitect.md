[English](../../PythonAPI/v2027.2/ObjectsArchitect.md) • [Deutsch](../../PythonAPI.de/v2027.2/ObjectsArchitect.md) • **日本語**

<a id="objectsarchitect--walls-roofs-slabs-windows-doors-columns-stairs"></a>

# ObjectsArchitect — 壁、屋根、スラブ、窓、ドア、柱、階段

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

主な建築オブジェクトのクラスです。`ArchitectObject`は共通の基底クラスです（`PrimitiveObject`を拡張し、プラグインオブジェクトのパラメータにアクセスできるようにします。壁と屋根では、これらのアクセサーは何も返しません）。

壁（`WallObject`）と屋根（`RoofObject`）はVectorworksのネイティブオブジェクトです。スラブ、窓、ドア、柱、階段は、ユニバーサル名（"Slab"、"Window"、"Door"、"Column2"、"Stairs CW"）で識別されるプラグインオブジェクトで、各クラスの静的な`Is(h)`がその名前を確認します。

規約：`Is(h)`はオブジェクトの種類を判定し、`Create(...)`はアクティブレイヤ／現在のコンテナに新しいインスタンスを作成します。型付きゲッターはオブジェクトが無効な場合やフィールドがない場合に`None`を返し、型付きセッターは成功時に`True`を返します。`WindowObject.Create`と`DoorObject.Create`は、指定点に独立したインスタンスを配置します。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [ArchitectObject](#architectobject)
  - [WallObject](#wallobject)
    - [WallObject.Heights](#wallobjectheights)
    - [WallObject.HeightBound](#wallobjectheightbound)
    - [WallObject.Caps](#wallobjectcaps)
    - [WallObject.BoundStatus](#wallobjectboundstatus)
    - [WallObject.BoundKind](#wallobjectboundkind)
  - [SlabObject](#slabobject)
  - [RoofObject](#roofobject)
    - [RoofObject.Attributes](#roofobjectattributes)
    - [RoofObject.Accessories](#roofobjectaccessories)
    - [RoofObject.Edge](#roofobjectedge)
    - [RoofObject.MiterType](#roofobjectmitertype)
  - [WindowObject](#windowobject)
  - [DoorObject](#doorobject)
  - [ColumnObject](#columnobject)
  - [StairObject](#stairobject)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`ArchitectObject`](#architectobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Architectオブジェクトのクラス（壁、スラブ、屋根、窓、ドア、柱、階段）に共通する基底クラスです。 |
| [`WallObject`](#wallobject) | クラス | [`ArchitectObject`](#architectobject) | 壁（`ObjectType.Wall`）です。窓、ドア、その他の壁挿入オブジェクトを配置できる、直線壁または円弧壁です。 |
| [`WallObject.Heights`](#wallobjectheights) | クラス（入れ子） |  | レイヤプレーンに対する高さです（ワールド単位、0 = レイヤ上面、負 = それより下）。 |
| [`WallObject.HeightBound`](#wallobjectheightbound) | クラス（入れ子） |  | 壁の下端または上端の境界です。高さの追従先を示します。 |
| [`WallObject.Caps`](#wallobjectcaps) | クラス（入れ子） |  | 端部キャップ。 |
| [`WallObject.BoundStatus`](#wallobjectboundstatus) | IntEnum（入れ子） |  | 壁の高さの境界の状態です（`WallObject.HeightBound.fStatus`）。 |
| [`WallObject.BoundKind`](#wallobjectboundkind) | IntEnum（入れ子） |  | 壁の高さの境界の追従先です。レイヤの高さ、レイヤの壁の高さ、またはストーリレベルを指定します。 |
| [`SlabObject`](#slabobject) | クラス | [`ArchitectObject`](#architectobject) | スラブです。2Dの境界プロファイルで定義し、厚み分だけ垂直に押し出した水平要素（床、屋根版、天井版など）です。 |
| [`RoofObject`](#roofobject) | クラス | [`ArchitectObject`](#architectobject) | 屋根（`ObjectType.RoofContainer`）です。辺のリストで定義する多角形の屋根です。 |
| [`RoofObject.Attributes`](#roofobjectattributes) | クラス（入れ子） |  | 屋根全体の属性。 |
| [`RoofObject.Accessories`](#roofobjectaccessories) | クラス（入れ子） |  | 周囲に沿った屋根の装飾部品。 |
| [`RoofObject.Edge`](#roofobjectedge) | クラス（入れ子） |  | 屋根の辺（多角形の頂点＋辺ごとの勾配と軒の出）です。屋根の輪郭に沿った順序です。 |
| [`RoofObject.MiterType`](#roofobjectmitertype) | IntEnum（入れ子） |  | 屋根端部の形状の種類です（隣接する二つの勾配面の接合方法）。 |
| [`WindowObject`](#windowobject) | クラス | [`ArchitectObject`](#architectobject) | Architectural Objectsプラグインの窓プラグインオブジェクトです（ユニバーサル名は"Window"）。 |
| [`DoorObject`](#doorobject) | クラス | [`ArchitectObject`](#architectobject) | Architectural Objectsプラグインのドアプラグインオブジェクトです（ユニバーサル名は"Door"）。 |
| [`ColumnObject`](#columnobject) | クラス | [`ArchitectObject`](#architectobject) | 柱プラグインオブジェクトです。Vectorworksの柱で、ユニバーサル名は"Column2"です。 |
| [`StairObject`](#stairobject) | クラス | [`ArchitectObject`](#architectobject) | 階段プラグインオブジェクトです。Vectorworksの階段で、ユニバーサル名は"Stairs CW"です。 |

<a id="classes"></a>

## クラス

### ArchitectObject

> **完全修飾名:** `api.ArchitectObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Architectオブジェクトのクラス（壁、スラブ、屋根、窓、ドア、柱、階段）に共通する基底クラスです。

建築オブジェクトは二つの系列に分かれます：

- 独自のオブジェクト型を持つネイティブのコンテナオブジェクト（壁 = `ObjectType.Wall`、屋根 = `ObjectType.RoofContainer`）。それぞれに型付きアクセサー（高さ、厚み、スタイルなど）があります。プラグインオブジェクトではないため、後述のパラメトリックレコードアクセサーは空／Falseを返します。
- プラグインオブジェクト（スラブ "Slab"、窓 "Window"、ドア "Door"、柱 "Column2"、階段 "Stairs CW"。APIではパラメトリックオブジェクトとも呼ばれます）。設定はレコードに格納されます。後述のパラメトリックアクセサーは、それらのフィールドを読み書きする主な手段です。スラブには型付きアクセサーもあります。また、床（床タイプの`ObjectType.Slab`）はレコードを持たないネイティブのスラブです。

すべてのサブクラスは、汎用のPrimitiveObject API（識別情報、クラス、属性、階層、境界、移動／回転／拡大縮小／反転、削除など）を継承します。規約：

- ゲッターは、オブジェクトが無効な場合やパラメータがない場合に`None`を返します。
- セッターは成功時に`True`を返し、オブジェクトが無効な場合やパラメータがない場合に`False`を返します。
- 長さはワールド単位、角度はラジアン（特定のパラメータで度と明記されている場合を除く）、文字列はUTF-8です。

パラメータアクセスの基本（Get/SetParam*）：

- プラグインオブジェクト（スラブ、窓、ドア、柱、階段）にのみ適用します。壁、屋根、床はパラメトリックレコードを持たないため、パラメトリックアクセサーはNone / Falseを返します。
- 窓、ドア、柱、階段のクラスは、「全パラメータリファレンス」に利用可能なパラメータ名を一覧表示しています。`GetParamNames()`は、スラブを含め、これらのいずれのパラメータも一覧表示します。サブクラスに専用の型付きアクセサーがないフィールドの読み書きには、GetParamString / SetParamString / GetParamReal / ...でそれらの名前をそのまま使用してください（大文字と小文字を区別し、UTF-8を使用）。
- 表内のパラメータ型には、次のタグを使用します：

- string — テキスト（UTF-8）- GetParamString / SetParamString
- int — 32ビット整数 - GetParamInt / SetParamInt
- bool — ブール値（"True"/"False"文字列として格納されることがあります）- GetParamBool / SetParamBool
- real — 浮動小数点値（ワールド座標、度単位の角度、通常の数値、面積など）- GetParamReal / SetParamReal
- popup — N個の文字列から一つを選択 - GetParamString / SetParamString。有効な値はパラメータの隣に記載されています

- "__"で始まる名前はプラグインの内部状態です。読み取りはできますが、通常は直接書き込んでも意味がありません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ArchitectObject(h: Handle)` | 任意のオブジェクト`h`を汎用の`ArchitectObject`として参照します。`IsValid()`はハンドルがnullでないことだけを確認します。オブジェクトの種類は`GetParametricName()`または具象クラスの`Is(h)`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `GetParametricName() -> str \| None` | オブジェクトのユニバーサル（パラメトリック）名です。例："Slab"、"Window"、"Door"、"Column2"、"Stairs CW"。ネイティブの壁／屋根オブジェクト、床、プラグインオブジェクトではないハンドルの場合は空です。 |
| `HasParam(univParamName: str) -> bool` | このプラグインオブジェクトが、指定されたユニバーサル名のフィールドを持つかどうか。ネイティブの壁／屋根オブジェクトと床では、常に`False`を返します。 |
| `GetParamNames() -> list[str]` | このオブジェクトのプラグインで定義されたすべてのパラメータ（ユニバーサル）名の順序付きリストです。ネイティブの壁／屋根オブジェクトと床では空です。 |
| `GetParamString(univParamName: str) -> str \| None` | 文字列をキーとする汎用のフィールドアクセサーです。サブクラスに型付きの名前付きアクセサーがある場合は、そちらを優先してください。専用アクセサーのないパラメータには、これらを使用します。 |
| `SetParamString(univParamName: str, value: str) -> bool` | パラメータの文字列を設定します。文字列をキーとする汎用のフィールドアクセサーです。サブクラスに型付きの名前付きアクセサーがある場合は、そちらを優先してください。専用アクセサーのないパラメータには、これらを使用します。 |
| `GetParamReal(univParamName: str) -> float \| None` | `univParamName`の実数パラメータを返します。 |
| `SetParamReal(univParamName: str, value: float) -> bool` | 実数パラメータを設定します。 |
| `GetParamBool(univParamName: str) -> bool \| None` | `univParamName`の*ブール型パラメータ*がオンかどうか。 |
| `SetParamBool(univParamName: str, value: bool) -> bool` | ブール型パラメータを設定します。 |
| `GetParamInt(univParamName: str) -> int \| None` | `univParamName`の整数パラメータを返します。 |
| `SetParamInt(univParamName: str, value: int) -> bool` | 整数パラメータを設定します。 |

*プラグインスタイル*

| メソッド | 説明 |
|---|---|
| `GetPluginStyleName() -> str \| None` | オブジェクトのプラグインスタイルリソースの名前です。スタイルがない場合、プラグインオブジェクトではない場合（ネイティブの壁／屋根オブジェクト、床）、またはオブジェクトが無効な場合は空です。 |
| `IsParamSetByStyle(univParamName: str) -> bool` | オブジェクトのプラグインスタイルがパラメータ`univParamName`を設定するかどうか。スタイルは「スタイルを使用」、「カタログを使用」（スタイルが使用するカタログのパラメータでもある）、または「混合」（スタイルで設定されるものとして扱う、スタイルダイアログの状態）で値を取得します。オブジェクトで「インスタンスを使用」に設定されたパラメータ、スタイルのないオブジェクト、プラグインオブジェクトではないオブジェクトでは`False`です。 |

継承メンバー：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### WallObject

> **完全修飾名:** `api.WallObject` · **継承元:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

壁（`ObjectType.Wall`）です。窓、ドア、その他の壁挿入オブジェクトを配置できる、直線壁または円弧壁です。

壁は、両端の高さ（上端と下端、レイヤプレーンに対する相対値）、厚み、任意の壁スタイル（重層の構成要素を制御）、左／右／丸型のキャップ、および読み取り専用の各種計算面積／長さ／高さを保持します。開口部や挿入オブジェクトは壁の子オブジェクトとして格納します。

壁はプラグインオブジェクトではないため、ArchitectObjectから継承した汎用のGet/SetParam*アクセサーは空／Falseを返します。後述の型付きアクセサーを使用し、図形属性には壁が継承するObjectAttributesを使用してください。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `WallObject(h: Handle)` | 既存の壁`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(start: Math.Point2D, end: Math.Point2D, thickness: float = 0.0) -> WallObject` *静的* | アクティブレイヤ／現在のコンテナに、`start`と`end`の間の直線壁を作成します。`thickness` = 0を渡すと、アクティブな壁設定の厚みを使用します。 |
| `CreateRound(start: Math.Point2D, onArc: Math.Point2D, end: Math.Point2D, thickness: float = 0.0) -> WallObject` *静的* | 指定した三点（始点、円弧上の点、終点）を通る円弧壁を作成します。 |
| `Duplicate() -> WallObject` | 図面内の壁を複製し、そのコピーを返します。 |

*図形*

| メソッド | 説明 |
|---|---|
| `GetLine() -> Math.Line2D \| None` | 壁の始点から終点までの線です。円弧壁では空です。 |
| `SetLine(start: Math.Point2D, end: Math.Point2D) -> bool` | 線を設定します。壁の始点から終点までの線です。円弧壁では空です。 |
| `GetStartPoint() -> Math.Point2D \| None` | 始点を返します。 |
| `GetEndPoint() -> Math.Point2D \| None` | 終点を返します。 |
| `GetLength() -> float \| None` | 長さを返します（ワールド単位、直線の長さ）。 |
| `GetAngle() -> float \| None` | 角度を返します（ラジアン、始点から終点への方向）。 |
| `SetThickness(thickness: float) -> bool` | 厚みです（ワールド単位）。厚みを設定すると、壁と壁スタイルの関連付けが解除されます。 |
| `GetHeights() -> WallObject.Heights \| None` | 高さを返します。 |
| `SetHeights(heights: WallObject.Heights) -> bool` | 高さを設定します。 |
| `SetHeights(startTop: float, startBottom: float, endTop: float, endBottom: float) -> bool` | 高さを設定します。 |
| `GetHeightBound(isTop: bool) -> WallObject.HeightBound` | `isTop`の高さの境界を返します。 |
| `SetHeightBounds(bottomBound: WallObject.HeightBound, topBound: WallObject.HeightBound) -> bool` | 壁の下端と上端を境界に関連付け、それに合わせて高さを移動します（オブジェクト情報パレットの壁の上端／下端の境界）。レイヤの境界ではfRelativeStoryとfLevelTypeは無視され、それぞれ0と空で格納されます。壁に対する境界が存在しない場合（レイヤがどのストーリにも属さない、ストーリにそのレベルがないなど）、または上端が下端より上にならない場合は失敗します。格納された境界が欠落している場合（古いファイル）や、すでに存在しない場合は、まず壁の現在の高さでレイヤ高さの境界に置き換え、その位置から移動量を測定します。ほかのセッターと同様、取り消しは登録されません。先に`Document.AddBothSwapObject`を呼び出してください。 |
| `SetHeightBound(isTop: bool, bound: WallObject.HeightBound) -> bool` | SetHeightBoundsと同じ方法で壁の上端（isTop）または下端を境界に関連付けます。もう一方の端の境界は保持します。 |
| `GetAverageHeight() -> float \| None` | 平均の高さを返します。 |
| `GetCaps() -> WallObject.Caps \| None` | キャップを返します。 |
| `SetCaps(caps: WallObject.Caps) -> bool` | キャップを設定します。 |
| `GetStyle() -> int \| None` | 壁スタイル（`ObjectType.WallStyle`リソース）。0 = スタイルなし（任意の厚み／構成要素）。 |
| `SetStyle(wallStyle: int, selectedOffset: float = 0.0, replacingOffset: float = 0.0) -> bool` | スタイルを設定します。壁スタイル（`ObjectType.WallStyle`リソース）。0 = スタイルなし（任意の厚み／構成要素）。 |
| `IsCurtainWall() -> bool \| None` | カーテンウォールフラグです（カーテンウォールシステムのフレームとして使用する壁）。 |
| `SetIsCurtainWall(isCurtainWall: bool) -> bool` | *カーテンウォール*のオン／オフを切り替えます。 |

継承メンバー：[`ArchitectObject`](#architectobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### WallObject.Heights

> **完全修飾名:** `api.WallObject.Heights` · **継承元:** `api.Object`

レイヤプレーンに対する高さです（ワールド単位、0 = レイヤ上面、負 = それより下）。始点と終点の高さを異なる値にすると、壁に傾斜を付けられます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Heights()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Heights(startTop, startBottom, endTop, endBottom)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `startTop` | `float` | 壁の始点での上端の高さ。 |
| `startBottom` | `float` | 壁の始点での下端の高さ。 |
| `endTop` | `float` | 壁の終点での上端の高さ。 |
| `endBottom` | `float` | 壁の終点での下端の高さ。 |

#### WallObject.HeightBound

> **完全修飾名:** `api.WallObject.HeightBound` · **継承元:** `api.Object`

壁の下端または上端の境界です。高さの追従先を示します。GetHeightBoundが返し、SetHeightBound(s)が受け取ります。fKind、fRelativeStory、fLevelType、fOffsetを使用します（fStatusとfElevationは読み取り専用の結果）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `HeightBound()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `HeightBound(fStatus, fKind, fRelativeStory, fLevelType, fOffset, fElevation)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fStatus` | `WallObject.BoundStatus` | 境界が欠落、未解決、無効、または有効かどうか。 |
| `fKind` | `WallObject.BoundKind` | レイヤの高さ、レイヤの壁の高さ、またはストーリレベル。 |
| `fRelativeStory` | `int` | ストーリ：-1は下のストーリ、0は壁のレイヤのストーリ、1は上のストーリ。 |
| `fLevelType` | `str` | ストーリ：そのストーリ内のレベルの種類。 |
| `fOffset` | `float` | ワールド単位。境界の高さに加算されます。 |
| `fElevation` | `float \| None` | fStatusがValidの場合の、解決済みの境界の高さ（ワールドZ、オフセットを含む）。 |

#### WallObject.Caps

> **完全修飾名:** `api.WallObject.Caps` · **継承元:** `api.Object`

端部キャップ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Caps()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Caps(leftCap, rightCap, round)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `leftCap` | `bool` | 始点側の端部を閉じる。 |
| `rightCap` | `bool` | 終点側の端部を閉じる。 |
| `round` | `bool` | キャップのスタイルが丸型。 |

#### WallObject.BoundStatus

> **完全修飾名:** `api.WallObject.BoundStatus` · **種類:** `IntEnum`

壁の高さの境界の状態です（`WallObject.HeightBound.fStatus`）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Missing` | `0` |  |
| `Unresolved` | `1` |  |
| `Invalid` | `2` |  |
| `Valid` | `3` |  |

#### WallObject.BoundKind

> **完全修飾名:** `api.WallObject.BoundKind` · **種類:** `IntEnum`

壁の高さの境界の追従先です。レイヤの高さ、レイヤの壁の高さ、またはストーリレベルを指定します。

| メンバー | 値 | 説明 |
|---|---|---|
| `Unknown` | `0` |  |
| `LayerElevation` | `1` |  |
| `LayerWallHeight` | `2` |  |
| `Story` | `3` |  |

### SlabObject

> **完全修飾名:** `api.SlabObject` · **継承元:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

スラブです。2Dの境界プロファイルで定義し、厚み分だけ垂直に押し出した水平要素（床、屋根版、天井版など）です。次の二つのオブジェクトがスラブです：

- Vectorworksが作成するスラブプラグインオブジェクト（`ObjectType.Parametric`、ユニバーサル名は"Slab"）。
- 床（床タイプの`ObjectType.Slab`で、床コマンドで作成します）。屋根面と旧式の柱も`ObjectType.Slab`オブジェクトですが、スラブではありません。

スラブは、高さと、構成要素の層を制御するスタイル（スラブスタイルリソース）を保持します。スラブの変更図形を使用して、境界に穴を追加できます。

スラブプラグインオブジェクトにはパラメトリックレコードがあります。ArchitectObjectから継承した汎用のGet/SetParam*アクセサーで、そのパラメータを読み書きします（`GetParamNames()`で一覧表示）。床では、これらは空／Falseを返します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `SlabObject(h: Handle)` | 既存のスラブ`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(hProfile: Handle) -> SlabObject` *静的* | 指定された2Dプロファイル（多角形、曲線、長円（円）、または円弧）を境界とするスラブプラグインオブジェクトを作成します。プロファイルのハンドルはスラブに取り込まれます。別の種類のプロファイルの場合や失敗した場合は、無効なオブジェクトを返します。 |
| `Duplicate() -> SlabObject` | 図面内のスラブを複製し、そのコピーを返します。 |
| `GetHeight() -> float \| None` | スラブの基準面の高さです。スラブスタイルで設定した、コア構成要素の上面または下面をワールド単位で示します。SetHeightはスラブを垂直に移動します。スラブプラグインオブジェクトのみが対象です。床では、ゲッターは空、セッターは`False`を返します。 |
| `SetHeight(height: float) -> bool` | 高さを設定します。スラブの基準面の高さです。スラブスタイルで設定した、コア構成要素の上面または下面をワールド単位で示します。SetHeightはスラブを垂直に移動します。スラブプラグインオブジェクトのみが対象です。床では、ゲッターは空、セッターは`False`を返します。 |
| `GetStyle() -> int \| None` | スラブスタイル（スラブスタイルリソース）です。0 = スタイルなし。SetStyle(0)はスラブのスタイルを解除し、現在の構成要素を保持します。スタイルを設定すると、構成要素の設定をそのスタイルの構成要素で置き換えます。図面のスラブスタイルではないインデックスに対して、セッターは`False`を返し、スラブを変更しません。また、その後スラブにそのスタイルが適用されていない場合も`False`を返します。 |
| `SetStyle(slabStyle: int) -> bool` | スタイルを設定します。スラブスタイル（スラブスタイルリソース）です。0 = スタイルなし。SetStyle(0)はスラブのスタイルを解除し、現在の構成要素を保持します。スタイルを設定すると、構成要素の設定をそのスタイルの構成要素で置き換えます。図面のスラブスタイルではないインデックスに対して、セッターは`False`を返し、スラブを変更しません。また、その後スラブにそのスタイルが適用されていない場合も`False`を返します。 |
| `AddModifier(hProfile: Handle, isSubtract: bool, componentID: int = -1, clipToBoundary: bool = True) -> bool` | スラブに変更図形（2Dプロファイル）を追加します。<br>• `isSubtract`が`True`の場合、プロファイルはスラブを貫通する穴になります。<br>• `componentID`で特定の構成要素を対象にします（< 0でスラブ全体）。<br>• `clipToBoundary`はプロファイルをスラブの境界で切り取ります。 |

継承メンバー：[`ArchitectObject`](#architectobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### RoofObject

> **完全修飾名:** `api.RoofObject` · **継承元:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

屋根（`ObjectType.RoofContainer`）です。辺のリストで定義する多角形の屋根です。各辺は挿入点、勾配、突出量（軒の出）、軒先下端の高さを持ちます。周囲に屋根の装飾部品（小屋裏、軒天井、鼻隠し）を挿入できます。

屋根はプラグインオブジェクトではないため、ArchitectObjectから継承した汎用のGet/SetParam*アクセサーは空／Falseを返します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RoofObject(h: Handle)` | 既存の屋根`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(generateGableWalls: bool, bearingInset: float, roofThickness: float, miterType: RoofObject.MiterType, verticalMiter: float) -> RoofObject` *静的* | 新しい屋根を作成します。<br>• `generateGableWalls`はホストとなる壁を屋根の下面まで自動的に延長します。<br>• `bearingInset`は壁から屋根の支持点までの距離で、ワールド単位です。<br>• `roofThickness`は屋根版の厚みで、ワールド単位です。<br>• `miterType`については`RoofObject.MiterType`を参照してください。<br>• `verticalMiter`は水平・垂直の端部形状の垂直部分で、ワールド単位です。<br>新しい屋根には小屋裏、軒天井、鼻隠しはありません。SetAccessoriesで追加します。 |
| `Duplicate() -> RoofObject` | 図面内の屋根を複製し、そのコピーを返します。 |
| `GetAttributes() -> RoofObject.Attributes \| None` | 属性を返します。 |
| `SetAttributes(attributes: RoofObject.Attributes) -> bool` | 属性を設定します。 |
| `SetAccessories(accessories: RoofObject.Accessories) -> bool` | 装飾部品を設定します。 |
| `GetEdgeCount() -> int \| None` | 辺項目の数です（辺（屋根輪郭の頂点）の数）。 |
| `GetEdge(index: int) -> RoofObject.Edge \| None` | `index`の辺を返します（0から始まるインデックス）。 |
| `SetEdge(index: int, edge: RoofObject.Edge) -> bool` | `index`の辺を設定します。 |
| `AppendEdge(edge: RoofObject.Edge) -> bool` | 屋根に辺`edge`（挿入点、勾配、突出量、軒先下端の高さ）を追加します。 |
| `RemoveEdge(index: int) -> bool` | `index`の辺を削除します。 |

継承メンバー：[`ArchitectObject`](#architectobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### RoofObject.Attributes

> **完全修飾名:** `api.RoofObject.Attributes` · **継承元:** `api.Object`

屋根全体の属性。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Attributes()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Attributes(generateGableWalls, bearingInset, roofThickness, miterType, verticalMiter)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `generateGableWalls` | `bool` | 妻壁（切り妻）を生成するかどうか。 |
| `bearingInset` | `float` | 支持部分の差し込み。 |
| `roofThickness` | `float` | 屋根の厚み。 |
| `miterType` | `RoofObject.MiterType` | 屋根端部の形状の種類。 |
| `verticalMiter` | `float` | 垂直部分の長さ。 |

#### RoofObject.Accessories

> **完全修飾名:** `api.RoofObject.Accessories` · **継承元:** `api.Object`

周囲に沿った屋根の装飾部品。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Accessories()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Accessories(insertAttic, insertSoffit, insertFascia, fasciaWidth, fasciaHeight, atticHeight, recess, rakeThickness, trimDepth)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `insertAttic` | `bool` | 小屋裏を挿入するかどうか。 |
| `insertSoffit` | `bool` | 軒天井を挿入するかどうか。 |
| `insertFascia` | `bool` | 鼻隠しを挿入するかどうか。 |
| `fasciaWidth` | `float` | ワールド単位。 |
| `fasciaHeight` | `float` | 鼻隠しの高さ。 |
| `atticHeight` | `float` | 小屋裏の高さ。 |
| `recess` | `float` | 後退距離。 |
| `rakeThickness` | `float` | けらばの厚み。 |
| `trimDepth` | `float` | 縁取りの奥行き。 |

#### RoofObject.Edge

> **完全修飾名:** `api.RoofObject.Edge` · **継承元:** `api.Object`

屋根の辺（多角形の頂点＋辺ごとの勾配と軒の出）です。屋根の輪郭に沿った順序です。軒先下端の高さは屋根のデザインレイヤの高さに対する相対値で、SetEdgeとAppendEdgeでも同様に受け取ります。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Edge()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Edge(insertionPoint, slope, projection, eaveHeight)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `insertionPoint` | `Math.Point2D` | 辺の挿入点。 |
| `slope` | `float` | 度。 |
| `projection` | `float` | ワールド単位 - 軒の出。 |
| `eaveHeight` | `float` | ワールド単位、レイヤの高さに対する相対値。 |

#### RoofObject.MiterType

> **完全修飾名:** `api.RoofObject.MiterType` · **種類:** `IntEnum`

屋根端部の形状の種類です（隣接する二つの勾配面の接合方法）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Vertical` | `1` | 垂直な接合部。 |
| `Horizontal` | `2` | 水平な接合部。 |
| `Double` | `3` | 水平・垂直の端部形状（接合部に垂直部分と水平部分の両方がある）。 |

### WindowObject

> **完全修飾名:** `api.WindowObject` · **継承元:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Architectural Objectsプラグインの窓プラグインオブジェクトです（ユニバーサル名は"Window"）。

窓はホストとなる壁（`ObjectType.Wall`）の、壁に沿った特定の位置と高さに挿入します。枠／障子／桟／ガラス／窓台／額縁／まぐさ／（よろい）戸のパラメータを保持します。

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）全体のサイズと配置

- "Width" — real — オブジェクト情報パレットに表示される窓のサイズ。"SizeReference"の指定に従って測定（GetWidth / SetWidth）
- "Height" — real — （GetHeight / SetHeight）
- "SizeReference" — popup — Sash Opening / Unit Size / Rough Opening："Width" / "Height"の測定対象
- "OverallWidth" — real — 窓のリセット時に"Width" / "Height"から計算される部材外寸（GetOverallWidth）。ここに書き込んだ値はリセット時に置き換えられます
- "OverallHeight" — real — （GetOverallHeight）
- "Elevation" — real — "ElevationSetAt"の指定に従う窓の上端または窓台の高さ。レイヤプレーンからの高さ（GetElevation；GetSillHeight / GetHeadHeight）
- "ElevationSetAt" — popup — Head of Window / Sill of Window
- "OffsetInWall" — real — 壁の挿入点からの水平オフセット
- "UseWallDepth" — bool — 枠の奥行きを壁の厚みに合わせる
- "TopShape" — popup — Square / Round / Segment / Sloped from Left / Sloped from Right / Gable / Ellipse / Gothic / Half Round from Left / Half Round from Right / Half Segment from Left / Half Segment from Right / Half Ellipse from Left / Half Ellipse from Right / Half Gothic from Left / Half Gothic from Right
- "Rise", "Spring" — real — 曲線形／切り妻形の上端のパラメータ
- "WindowShape" — popup — Rectangle / Circle / Oval / Half Circle / Half Oval / Diamond / Hexagon - Top Flat / Hexagon - Side Flat / Octagon
- "RoundWallOffset" — real — ホストとなる円弧壁からのオフセット
- "SpanWall" — bool — 窓をホストとなる壁全体にわたって配置
- "CornerWindow" — bool — コーナー窓の構成を使用
- "CornerWindowOp" — popup — Opening / Cased Opening / Flush Glass / Flush Glass - No Sash / Mitered Sash / Corner Post
- "CornerPostSize", "CornerPostOffset" — real

形式

- "Configuration" — popup — Opening / Cased Opening / Awning / Casement / Fixed Glass / Folding / Hopper / Hung / Sliding / Tilt/Turn / Vertical Pivot / Custom
- "CasementOperation" — popup — Single / Bi-Part（Casement形式）
- "FixedGlassOperation" — popup — Sash / No Sash（Fixed Glass形式）
- "HungOperation" — popup — Single / Double（Hung形式）
- "SashOperation" — popup — 旧式。"Configuration"と種類ごとの開閉方式に置き換えられています
- "CustSashOpPopup" — popup — カスタム障子の開閉方式
- "CustSashOp", "CustSashLock" — string
- "CustSashWdth", "CustSashHght" — string — カスタム障子の幅／高さのレイアウト
- "CustomSash" — bool
- "CustSashSel" — string
- "CustSashWidth", "CustSashHeight" — real
- "Rows", "Cols" — int — カスタム障子のグリッド寸法
- "UnequalSash" — bool
- "SashScaleFactor" — real
- "HingeDirection" — bool — 蝶番の側を反転
- "HingePref" — int
- "Show3DOpen" — bool
- "OpenAngle" — real — 度

欄間

- "Transom" — bool
- "TransWidth", "TransDepth" — real — 欄間の方立の幅／奥行き
- "TransomGlazingClass" — popup — クラス名
- "NumVTranMuntins", "NumHTranMuntins" — int
- "TranMuntinWidth", "TranMuntinOffset", "TranMuntinDepth" — real
- "TranMuntinPattern" — popup — Colonial / Prairie / Prairie w/sunburst / Colonial w/sunburst / Renaissance
- "TranNumOfRays" — int
- "TransomMuntins" — bool
- "MullionWidth", "MullionDepth" — real

カーテンウォールの構成

- "CurtainWallWindow" — bool
- "CWSashOperation" — popup — Fixed Glass / Fixed Glass - No Sash / Casement / Bi-parting Casement / Horizontal Slider / Awning / Hopper / Tilt/Turn / Vertical Pivot

縦枠／障子枠

- "JambWidth" — real — 縦枠の見付け幅
- "JambDepth" — real — 縦枠の奥行き（壁の内部方向）
- "SashWidth", "SashDepth" — real
- "ShimGap" — real
- "MasonMod" — real — 石積みモジュールのオフセット
- "UseJambExtension" — bool
- "JambExtenWidth" — real

桟

- "MuntinPattern" — popup — Colonial / Prairie / Prairie w/sunburst / Colonial w/sunburst / Renaissance
- "MuntinApplication" — popup — None / All / Top / Bottom / Transom / Top\Bottom / Top\Transom / Bot\Transom
- "NumVMuntins", "NumHMuntins" — int
- "MuntinWidth", "MuntinOffset", "MuntinDepth" — real
- "NumOfRays" — int
- "TopSashMuntins", "BottomSashMuntins", "TransomMuntins" — bool
- "CustomTopMuntins" — bool
- "TopSashHorizBars" — int
- "CustMuntins" — string
- "CustMullDepth", "CustMullWidth" — real

窓台／内窓台

- "SillStyle" — popup — Timber / Masonry / Brick / Open Profile Beside Frame / Open Profile Below Frame / Closed Profile
- "IncludeSill" — bool
- "SillDepth", "SillHeight", "SillLip", "SillRise", "SillKeep", "SillExt" — real
- "StoolLip", "StoolNose" — real

額縁

- "IntTrim", "ExtTrim" — bool
- "IntTrimWidth", "IntTrimDepth", "ExtTrimWidth", "ExtTrimDepth" — real
- "TrimUnderStool", "TrimUnderSill" — bool

開口部の広がり（壁の内側／外側の開口角度）

- "IntSplay", "ExtSplay" — bool
- "UseIntSplayAngle", "UseExtSplayAngle" — bool
- "IntSplayAngle", "ExtSplayAngle" — real（度）
- "IntSplayDiag", "ExtSplayDiag" — real
- "UseIntSplayWidth", "UseExtSplayWidth" — bool
- "IntSplayWidth", "ExtSplayWidth" — real
- "IntSplayDepth", "ExtSplayDepth" — real

まぐさ

- "Lintels" — bool
- "LintelThick" — real
- "IntLintelProt", "ExtLintelProt" — real
- "UseLintelAngle" — bool
- "LintelAngle" — real（度）
- "UseLintelDrop" — bool
- "LintelDrop" — real
- "LintelClass" — popup — クラス名

（よろい）戸

- "IntShutters", "ExtShutters" — bool
- "IntShtThick", "ExtShtThick" — real
- "IntShtMllWidth", "ExtShtMllWidth" — real
- "IntShtDivWSash", "ExtShtDivWSash" — bool
- "IntShtEqualDiv", "ExtShtEqualDiv" — bool
- "IntShtNumPanels", "ExtShtNumPanels" — int
- "IntShtIsPanel", "ExtShtIsPanel" — bool
- "IntShtIsCustom", "ExtShtIsCustom" — bool
- "IntShtCustomIndex", "ExtShtCustomIndex" — int
- "UseCustIntShutterWidth", "UseCustExtShutterWidth" — bool
- "CustIntShutterWidth", "CustExtShutterWidth" — real

ID／集計／タグ

- "OnSchedule" — bool
- "IDPrefix", "IDLabel", "IDSuffix" — string
- "IDLabelSize" — real
- "IDLabelShape" — popup — None / Rectangle / Round / Hexagon
- "IDLabelClass" — popup — クラス名
- "KeepIDHoriz" — bool
- "ShowIDLeader" — bool
- "IDLeaderLW" — int — 線の太さ
- "UseMarker" — bool
- "MarkerIDx" — int
- "MarkerStyle" — int
- "MarkerAngle" — int（度）
- "MarkerSize" — real
- "MarkerWidth" — real
- "MarkerThick", "MarkerThickB" — real / int
- "TagInElevation" — bool
- "Tag3DHorzOffset", "Tag3DVertOffset" — real

空洞（枠）の数

- "NumOfIntCavities", "NumOfExtCavities" — int

クラス（構成要素ごと）

- "IntSashClass", "ExtSashClass" — popup — クラス名
- "IntJTClass", "ExtJTClass" — popup — クラス名（縦枠＋額縁）
- "IntShutterClass", "ExtShutterClass" — popup — クラス名
- "SillClass", "StoolClass" — popup — クラス名
- "GlazingClass", "TransomGlazingClass" — popup — クラス名
- "IntTransomClass", "ExtTransomClass" — popup — クラス名
- "HingeClass" — popup — クラス名
- "Sills2DClass", "CeilingMainClass", "NonPlotClass" — popup — クラス名

メタデータ（集計表用）

- "WindowDesc" — string — 短い説明
- "Model", "ManufSupplier", "StockNo", "GlassDesc" — string
- "HeadDetail", "JambDetail", "SillDetail" — string
- "Accessories" — string
- "Egress" — string / bool
- "WindowMaterial", "WindowFinish", "FrameType", "FrameMaterial", "FrameFinish", "WindowSill" — string
- "Location" — string
- "LintelType" — string
- "UserFld1..UserFld10" — string — 集計表用のユーザー定義フィールド

表示フラグ

- "PlanDetail" — bool — 平面ビューの詳細を描画
- "DrawWallLines" — bool
- "Clerestory" — bool
- "LW_LS_OverRide" — bool
- "IsDoor" — bool — 内部フラグ（ドアとして使用する窓）
- "Flipped" — bool
- "WrapPointsSwapped" — bool
- "ShowShimGap" — bool
- "ShowInteriorHinge" — bool
- "Set2DAttribsBy" — popup — Object / Line Style / Class
- "PenStyle", "FillStyle" — popup — None / Solid / Line Type / By Object / By Class（線）。面ではさらにHatch / Tile / Gradient / By Material
- "LastRenderMode", "Last3DView" — int
- "NGA2" — real（面積、読み取り専用）
- "ControlPoint01X..ControlPoint03Y" — real（ワールド座標）

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `WindowObject(h: Handle)` | 既存の窓`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D) -> WindowObject` *静的* | `position`に窓を作成します。通常は、その後WallObjectを使用して壁に挿入します。 |
| `Duplicate() -> WindowObject` | 図面内の窓を複製し、そのコピーを返します。 |

*サイズ（ワールド単位）*

| メソッド | 説明 |
|---|---|
| `GetWidth() -> float \| None` | "Width" / "Height"は、オブジェクト情報パレットに表示される窓のサイズです。寸法押さえの指定に従い、窓框寸法（"Sash Opening"）、部材外寸（"Unit Size"）、またはあら開口寸法（"Rough Opening"）を測定します。窓のリセット時に、これらから部材外寸（GetOverallWidth / GetOverallHeight）を計算します。セッターの後に`Reset()`を呼び出してください。オブジェクトが無効な場合、値が正の有限数ではない場合、または窓のプラグインスタイルが設定するパラメータの場合（IsParamSetByStyle）、セッターは`False`を返し、何も書き込みません。これらの値にかかわらず、VectorworksはOpening形式の窓をあら開口寸法として測定し、カーテンウォール内の窓はパネルに合わせてサイズを設定します。 |
| `SetWidth(value: float) -> bool` | 幅を設定します。"Width" / "Height"は、オブジェクト情報パレットに表示される窓のサイズです。寸法押さえの指定に従い、窓框寸法（"Sash Opening"）、部材外寸（"Unit Size"）、またはあら開口寸法（"Rough Opening"）を測定します。窓のリセット時に、これらから部材外寸（GetOverallWidth / GetOverallHeight）を計算します。セッターの後に`Reset()`を呼び出してください。オブジェクトが無効な場合、値が正の有限数ではない場合、または窓のプラグインスタイルが設定するパラメータの場合（IsParamSetByStyle）、セッターは`False`を返し、何も書き込みません。これらの値にかかわらず、VectorworksはOpening形式の窓をあら開口寸法として測定し、カーテンウォール内の窓はパネルに合わせてサイズを設定します。 |
| `GetHeight() -> float \| None` | 高さを返します。 |
| `SetHeight(value: float) -> bool` | 高さを設定します。 |
| `GetSizeReference() -> str \| None` | GetWidth / GetHeightの測定対象です。"Sash Opening"、"Unit Size"、または"Rough Opening"（パラメータ"SizeReference"）。SetSizeReferenceはポップアップのみを書き換えます。"Width"、"Height"、"Elevation"の値は保持され、次のリセットで新しい基準に従って測定されるため、窓のサイズが変わります（オブジェクト情報パレットでは、代わりにサイズを換算します）。その後にサイズを設定してください。別の値を指定した場合や、スタイルがパラメータを設定する場合は`False`を返し、何も書き込みません。 |
| `SetSizeReference(value: str) -> bool` | 寸法押さえを設定します。GetWidth / GetHeightの測定対象です。"Sash Opening"、"Unit Size"、または"Rough Opening"（パラメータ"SizeReference"）。SetSizeReferenceはポップアップのみを書き換えます。"Width"、"Height"、"Elevation"の値は保持され、次のリセットで新しい基準に従って測定されるため、窓のサイズが変わります（オブジェクト情報パレットでは、代わりにサイズを換算します）。その後にサイズを設定してください。別の値を指定した場合や、スタイルがパラメータを設定する場合は`False`を返し、何も書き込みません。 |
| `GetOverallWidth() -> float \| None` | 最後のリセット時に窓が計算した部材外寸です（パラメータ"OverallWidth" / "OverallHeight"）。SetOverallWidth / SetOverallHeightは、次のリセットで部材外寸が`value`になるように、現在の寸法押さえの幅／高さを書き込みます。"Unit Size"では`value`そのもの、"Sash Opening"では`value`から縦枠の幅（"JambWidth"）の二倍を引いた値です。この計算が正確ではない場合は`False`を返し、何も書き込みません。該当するのは、"Rough Opening"（窓が壁から、または互いの値から取付隙間を取得する場合がある）、欄間のある"Sash Opening"窓の高さ（欄間の高さは上端形状に依存）、Opening形式の窓、コーナー窓、カーテンウォールまたはドア/窓アセンブリ内の窓（Vectorworksが自動的にサイズを設定）、正のサイズにならない値、およびSetWidth / SetHeightが`False`を返す場合です。 |
| `SetOverallWidth(value: float) -> bool` | 全体幅を設定します。最後のリセット時に窓が計算した部材外寸です（パラメータ"OverallWidth" / "OverallHeight"）。SetOverallWidth / SetOverallHeightは、次のリセットで部材外寸が`value`になるように、現在の寸法押さえの幅／高さを書き込みます。"Unit Size"では`value`そのもの、"Sash Opening"では`value`から縦枠の幅（"JambWidth"）の二倍を引いた値です。この計算が正確ではない場合は`False`を返し、何も書き込みません。該当するのは、"Rough Opening"（窓が壁から、または互いの値から取付隙間を取得する場合がある）、欄間のある"Sash Opening"窓の高さ（欄間の高さは上端形状に依存）、Opening形式の窓、コーナー窓、カーテンウォールまたはドア/窓アセンブリ内の窓（Vectorworksが自動的にサイズを設定）、正のサイズにならない値、およびSetWidth / SetHeightが`False`を返す場合です。 |
| `GetOverallHeight() -> float \| None` | 全体の高さを返します。 |
| `SetOverallHeight(value: float) -> bool` | 全体の高さを設定します。 |

*高さ（ワールド単位）*

| メソッド | 説明 |
|---|---|
| `GetElevation() -> float \| None` | レイヤプレーンからの高さです。壁内の窓では、壁の下端からではなく、壁開口の高さ（通常は0）だけ上げたレイヤプレーンからの高さです。"Elevation"はオブジェクト情報パレットの生の値で、"ElevationSetAt"（"Head of Window"または"Sill of Window"）の指定に従う窓の上端または窓台の高さです。GetElevation / SetElevationで読み書きします。GetSillHeight / GetHeadHeightは"ElevationSetAt"にかかわらず窓台／上端を読み取ります。これは、ユーザーが切り替える際にパレットが"Elevation"を換算するのと同じで、head = sill + Heightです。SetSillHeightは呼び出し時の窓の"Height"を使い、現在の"ElevationSetAt"に対応する"Elevation"を書き込みます（"Head of Window"ではsill + Height）。先に高さを設定してください。"ElevationSetAt"は保持されます。SetElevationとSetSillHeightは、値が有限でない場合や、プラグインスタイルが"Elevation"を設定する場合に`False`を返し、何も書き込みません。SetSillHeightは"Height"または"ElevationSetAt"を読み取れない場合も同様です。 |
| `SetElevation(value: float) -> bool` | 高さを設定します。レイヤプレーンからの高さです。壁内の窓では、壁の下端からではなく、壁開口の高さ（通常は0）だけ上げたレイヤプレーンからの高さです。"Elevation"はオブジェクト情報パレットの生の値で、"ElevationSetAt"（"Head of Window"または"Sill of Window"）の指定に従う窓の上端または窓台の高さです。GetElevation / SetElevationで読み書きします。GetSillHeight / GetHeadHeightは"ElevationSetAt"にかかわらず窓台／上端を読み取ります。これは、ユーザーが切り替える際にパレットが"Elevation"を換算するのと同じで、head = sill + Heightです。SetSillHeightは呼び出し時の窓の"Height"を使い、現在の"ElevationSetAt"に対応する"Elevation"を書き込みます（"Head of Window"ではsill + Height）。先に高さを設定してください。"ElevationSetAt"は保持されます。SetElevationとSetSillHeightは、値が有限でない場合や、プラグインスタイルが"Elevation"を設定する場合に`False`を返し、何も書き込みません。SetSillHeightは"Height"または"ElevationSetAt"を読み取れない場合も同様です。 |
| `GetElevationSetAt() -> str \| None` | 高さの設定基準を返します。 |
| `GetSillHeight() -> float \| None` | 窓台の高さを返します。 |
| `SetSillHeight(value: float) -> bool` | 窓台の高さを設定します。 |
| `GetHeadHeight() -> float \| None` | 上端の高さを返します。 |

*形式*

| メソッド | 説明 |
|---|---|
| `GetConfiguration() -> str \| None` | 形式を返します。 |
| `GetCasementOperation() -> str \| None` | 開き窓の開閉方式を返します。 |
| `GetFixedGlassOperation() -> str \| None` | はめ殺し窓の方式を返します。 |
| `GetHungOperation() -> str \| None` | 上げ下げ窓の開閉方式を返します。 |

*旧式*

| メソッド | 説明 |
|---|---|
| `GetSashOperation() -> str \| None` | "SashOperation"として格納されます。`GetConfiguration()`と種類ごとの開閉方式ゲッターに置き換えられています。 |
| `SetSashOperation(value: str) -> bool` | 障子の開閉方式を設定します。"SashOperation"として格納されます。`GetConfiguration()`と種類ごとの開閉方式ゲッターに置き換えられています。 |
| `GetTopShape() -> str \| None` | 上端形状を返します。 |
| `SetTopShape(value: str) -> bool` | 上端形状を設定します。 |

*枠／障子*

| メソッド | 説明 |
|---|---|
| `GetJambWidth() -> float \| None` | 縦枠の幅を返します。 |
| `SetJambWidth(value: float) -> bool` | 縦枠の幅を設定します。 |
| `GetJambDepth() -> float \| None` | 縦枠の奥行きを返します。 |
| `SetJambDepth(value: float) -> bool` | 縦枠の奥行きを設定します。 |

*窓台*

| メソッド | 説明 |
|---|---|
| `GetIncludeSill() -> bool \| None` | *窓台*がオンかどうか。 |
| `SetIncludeSill(value: bool) -> bool` | *窓台*のオン／オフを切り替えます。 |
| `GetSillStyle() -> str \| None` | 窓台のスタイルを返します。 |
| `SetSillStyle(value: str) -> bool` | 窓台のスタイルを設定します。 |

*集計*

| メソッド | 説明 |
|---|---|
| `GetOnSchedule() -> bool \| None` | *一覧表に集計*がオンかどうか。 |
| `SetOnSchedule(value: bool) -> bool` | *一覧表に集計*のオン／オフを切り替えます。 |
| `GetIDLabel() -> str \| None` | IDラベルを返します。 |
| `SetIDLabel(value: str) -> bool` | IDラベルを設定します。 |
| `GetDescription() -> str \| None` | 説明を返します。 |
| `SetDescription(value: str) -> bool` | 説明を設定します。 |

*開き方*

| メソッド | 説明 |
|---|---|
| `GetInteriorSide() -> str \| None` | 内側を返します。 |
| `GetFlipped() -> bool \| None` | *反転*がオンかどうか。 |
| `GetHingeDirection() -> bool \| None` | *蝶番の方向*がオンかどうか。 |
| `GetShow3DOpen() -> bool \| None` | *3D時に開く*がオンかどうか。 |
| `GetOpenAngle() -> float \| None` | 開き角度を返します。 |
| `GetAwningOpenDirection() -> str \| None` | 障子の蝶番と開く方向のパラメータ（ポップアップ）。 |
| `GetCasementHingeSide() -> str \| None` | 開き窓の蝶番の側を返します。 |
| `GetCasementOpenDirection() -> str \| None` | 開き窓の開く方向を返します。 |
| `GetHopperOpenDirection() -> str \| None` | 内倒し窓の開く方向を返します。 |
| `GetTiltTurnHingeSide() -> str \| None` | 内倒し／内開き窓の蝶番の側を返します。 |
| `GetTiltTurnOpenDirection() -> str \| None` | 内倒し／内開き窓の開く方向を返します。 |
| `GetVerticalPivotOpensOutToward() -> str \| None` | 縦軸回転窓が外側に開く向きを返します。 |

継承メンバー：[`ArchitectObject`](#architectobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### DoorObject

> **完全修飾名:** `api.DoorObject` · **継承元:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Architectural Objectsプラグインのドアプラグインオブジェクトです（ユニバーサル名は"Door"）。

ドアはホストとなる壁（`ObjectType.Wall`）に挿入します。枠／扉／縦枠／まぐさ／沓ズリ／額縁／袖FIX／のぞき窓／桟のパラメータを保持します。

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）全体のサイズと配置

- "Width" — real — オブジェクト情報パレットに表示されるドアのサイズ。"SizeReference"の指定に従って測定（GetWidth / SetWidth）
- "Height" — real — （GetHeight / SetHeight）
- "SizeReference" — popup — Leaf Size / Unit Size / Rough Opening："Width" / "Height"の測定対象
- "DoorWidth" — real — ドアのリセット時に"Width" / "Height"から計算される扉のサイズ（GetLeafWidth）。ここに書き込んだ値はリセット時に置き換えられます
- "DoorHeight" — real — （GetLeafHeight）
- "OffsetInWall" — real — 壁の挿入点からの水平オフセット
- "UseWallDepth" — bool — 枠の奥行きを壁の厚みに合わせる
- "TopShape" — popup — Square / Round / Segment / Sloped from Left / Sloped from Right / Gable / Ellipse / Gothic
- "Rise", "Spring" — real — 曲線形／切り妻形の上端のパラメータ

形式

- "Configuration" — popup — Opening / Cased Opening / Barn / Double Acting / Double Egress / Folding / Overhead / Pocket / Sliding / Swing
- "SwingOperation" — popup — Single / Bi-part / Pivot Single / Pivot Double Bi-part（Swing形式）
- "Operation" — popup — 旧式。"SwingOperation"に置き換えられています
- "PlanDetail" — bool
- "DetailLevel" — popup — Low / Medium / High
- "Show3DHinge" — bool
- "DrawWallLines" — bool
- "LW_LS_OverRide" — bool
- "3DOpen" — bool
- "OpenAngle" — real — 度

欄間

- "Transom" — bool
- "TranMullDepth", "TranMullWidth" — real — 欄間の方立のサイズ
- "TranSashWidth", "TranSashDepth" — real

縦枠

- "JambWidth", "JambDepth" — real
- "AstragalWidth", "AstragalDepth" — real
- "ShimGap" — real
- "MasonMod" — real

額縁

- "IntTrim", "ExtTrim" — bool
- "IntTrimWidth", "IntTrimDepth", "ExtTrimWidth", "ExtTrimDepth" — real

空洞（枠）の数

- "NumIntComps", "NumExtComps" — int

集計／ID

- "OnSched" — bool
- "IDPrefix", "IDLabel", "IDSuffix" — string
- "IDLabelSize" — real
- "IDLabelShape" — popup — None / Rectangle / Round / Hexagon
- "KeepIDHoriz" — bool
- "ShowIDLeader" — bool
- "UseMarker" — bool

扉

- "LeafType" — popup — Solid / Glass / Panel / Custom
- "DoorThickness" — real
- "TopStileWidth", "LRStileWidth", "MidStileWidth", "BottomStileWidth" — real
- "NumPanelsV", "NumPanelsH" — int
- "SetTopPanel" — bool
- "TopPanelHeight" — real

桟（扉のガラス部分）

- "MuntinStyle" — popup — Colonial / Prairie
- "DoorMuntinWidth" — real
- "DoorVMuntins", "DoorHMuntins" — int
- "Muntins" — bool
- "GlassMuntin" — popup — Colonial / Prairie / Colonial w/Sunburst / Prairie w/ Sunburst / Renaissance
- "NumVMuntins", "NumHMuntins" — int
- "MuntinWidth" — real

袖FIX

- "SideLights" — bool
- "LeftLiteWidth", "RightLiteWidth" — real
- "SashWidth", "SashDepth" — real
- "SLMullWidth", "SLMullDepth" — real

まぐさ

- "Lintel" — bool
- "IntLintelProt", "ExtLintelProt" — real
- "LintelThick" — real
- "UseLintelAngle" — bool
- "LintelAngle" — real（度）
- "UseLintelDrop" — bool
- "LintelDrop" — real
- "LintelClass" — popup — クラス名

沓ズリ

- "Threshold" — bool
- "IntTHDepth", "ExtTHDepth", "OverallTHDepth" — real
- "OffJambCenter" — real
- "ThreshThick", "ThreshNose" — real
- "ThresholdClass" — popup — クラス名

開口部の広がり

- "IntSplay", "ExtSplay" — bool
- "UseIntSplayAngle", "UseExtSplayAngle" — bool
- "IntSplayAngle", "ExtSplayAngle" — real（度）
- "IntSplayDiag", "ExtSplayDiag" — real
- "UseIntSplayWidth", "UseExtSplayWidth" — bool
- "IntSplayWidth", "ExtSplayWidth" — real
- "IntSplayDepth", "ExtSplayDepth" — real

シンボルへの置き換え（扉としてシンボルを使用）

- "UseSymDef" — bool
- "SymbolName" — string — シンボルリソース名

線の太さ／スタイル（構成要素ごと）

- "Part", "LWPart" — string — オブジェクト情報パレットで編集中の部分
- "JambLW", "JambLS", "TrimLW", "TrimLS", "LeafLW", "LeafLS" — int
- "SwingLW", "SwingLS", "SashLW", "SashLS", "GlassLW", "GlassLS", "AstragalLW", "AstragalLS" — int
- "DetailLW" — int

クラス（構成要素ごと）

- "PartClass" — popup — 現在選択している部分のクラス名
- "IntPanelClass", "ExtPanelClass" — popup — クラス名
- "IntSRClass", "ExtSRClass" — popup — クラス名（内側／外側の縦框と横框）
- "IntJambClass", "ExtJambClass" — popup — クラス名
- "IntTrimClass", "ExtTrimClass" — popup — クラス名
- "IntSashClass", "ExtSashClass" — popup — クラス名
- "SwingTrajectory" — popup — 開閉円弧のクラス名
- "GlazingClass" — popup — クラス名
- "SideLGlazingClass" — popup — クラス名（袖FIXのガラス）

サイズ設定

- "ROWidth", "ROHeight" — real — あら開口寸法のサイズ
- "MOWidth", "MOHeight" — real — 石積み開口のサイズ
- "NGA" — real — ガラスの正味面積（読み取り専用）

メタデータ（集計表用）

- "Manuf", "Model", "SKU" — string
- "Accessories" — string
- "HeadDetail", "JambDetail", "ThreshDetail" — string
- "FrameFR", "DoorFR" — string — 耐火等級
- "Notes" — string
- "UserFld1..UserFld10" — string — ユーザー定義フィールド

納屋ドア形式（Configuration = "Barn"）

- "BarnShowRail" — popup — None / 2D / 3D / 2D and 3D
- "BarnRailType" — popup — Box / Flat / Round
- "BarnShowRailMounts" — popup — None / 3D
- "BarnBracketType" — popup — None / U / Z
- "BarnShowLeafHangers" — popup — None / 3D
- "BarnHangerMounting" — popup — Leaf Front / Leaf Top

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DoorObject(h: Handle)` | 既存のドア`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D) -> DoorObject` *静的* | `position`にドアを作成します。通常は、その後WallObjectを使用して壁に挿入します。 |
| `Duplicate() -> DoorObject` | 図面内のドアを複製し、そのコピーを返します。 |

*サイズ（ワールド単位）*

| メソッド | 説明 |
|---|---|
| `GetWidth() -> float \| None` | "Width" / "Height"は、オブジェクト情報パレットに表示されるドアのサイズです。寸法押さえの指定に従い、扉寸法（"Leaf Size"）、部材外寸（"Unit Size"）、またはあら開口寸法（"Rough Opening"）を測定します。ドアのリセット時に、これらから扉のサイズ（GetLeafWidth / GetLeafHeight）を計算します。セッターの後に`Reset()`を呼び出してください。GetWidth / GetHeightはセッターが書き込んだ値を読み取ります。このAPIの以前のビルドでは扉のサイズを読み取っていましたが、現在はGetLeafWidth / GetLeafHeightがそれを読み取ります。オブジェクトが無効な場合、値が正の有限数ではない場合、またはドアのプラグインスタイルが設定するパラメータの場合（IsParamSetByStyle）、セッターは`False`を返し、何も書き込みません。これらの値にかかわらず、VectorworksはOpening形式のドアをあら開口寸法として測定し、カーテンウォール内のドアはパネルに合わせてサイズを設定します。 |
| `SetWidth(value: float) -> bool` | 幅を設定します。"Width" / "Height"は、オブジェクト情報パレットに表示されるドアのサイズです。寸法押さえの指定に従い、扉寸法（"Leaf Size"）、部材外寸（"Unit Size"）、またはあら開口寸法（"Rough Opening"）を測定します。ドアのリセット時に、これらから扉のサイズ（GetLeafWidth / GetLeafHeight）を計算します。セッターの後に`Reset()`を呼び出してください。GetWidth / GetHeightはセッターが書き込んだ値を読み取ります。このAPIの以前のビルドでは扉のサイズを読み取っていましたが、現在はGetLeafWidth / GetLeafHeightがそれを読み取ります。オブジェクトが無効な場合、値が正の有限数ではない場合、またはドアのプラグインスタイルが設定するパラメータの場合（IsParamSetByStyle）、セッターは`False`を返し、何も書き込みません。これらの値にかかわらず、VectorworksはOpening形式のドアをあら開口寸法として測定し、カーテンウォール内のドアはパネルに合わせてサイズを設定します。 |
| `GetHeight() -> float \| None` | 高さを返します。 |
| `SetHeight(value: float) -> bool` | 高さを設定します。 |
| `GetLeafWidth() -> float \| None` | 最後のリセット時にドアが計算した扉のサイズです（パラメータ"DoorWidth" / "DoorHeight"）。 |
| `GetLeafHeight() -> float \| None` | 扉の高さを返します。 |
| `GetSizeReference() -> str \| None` | GetWidth / GetHeightの測定対象です。"Leaf Size"、"Unit Size"、または"Rough Opening"（パラメータ"SizeReference"）。SetSizeReferenceはポップアップのみを書き換えます。"Width"と"Height"の値は保持され、次のリセットで新しい基準に従って測定されるため、ドアのサイズが変わります（オブジェクト情報パレットでは、代わりにサイズを換算します）。その後にサイズを設定してください。別の値を指定した場合や、スタイルがパラメータを設定する場合は`False`を返し、何も書き込みません。 |
| `SetSizeReference(value: str) -> bool` | 寸法押さえを設定します。GetWidth / GetHeightの測定対象です。"Leaf Size"、"Unit Size"、または"Rough Opening"（パラメータ"SizeReference"）。SetSizeReferenceはポップアップのみを書き換えます。"Width"と"Height"の値は保持され、次のリセットで新しい基準に従って測定されるため、ドアのサイズが変わります（オブジェクト情報パレットでは、代わりにサイズを換算します）。その後にサイズを設定してください。別の値を指定した場合や、スタイルがパラメータを設定する場合は`False`を返し、何も書き込みません。 |
| `GetThickness() -> float \| None` | 扉の厚みです（ワールド単位、パラメータ"DoorThickness"）。 |
| `SetThickness(value: float) -> bool` | 厚みを設定します。扉の厚みです（ワールド単位、パラメータ"DoorThickness"）。 |
| `GetConfig() -> str \| None` | 旧式の"Config"パラメータです。`GetConfiguration()`は"Configuration"ポップアップを読み取ります。 |
| `SetConfig(value: str) -> bool` | 形式を設定します。旧式の"Config"パラメータです。`GetConfiguration()`は"Configuration"ポップアップを読み取ります。 |
| `GetConfiguration() -> str \| None` | 形式を返します。 |
| `GetTopShape() -> str \| None` | 上端形状を返します。 |
| `SetTopShape(value: str) -> bool` | 上端形状を設定します。 |
| `GetLeafType() -> str \| None` | 扉の種類を返します。 |
| `SetLeafType(value: str) -> bool` | 扉の種類を設定します。 |

*集計*

| メソッド | 説明 |
|---|---|
| `GetOnSchedule() -> bool \| None` | *一覧表に集計*がオンかどうか。 |
| `SetOnSchedule(value: bool) -> bool` | *一覧表に集計*のオン／オフを切り替えます。 |
| `GetIDLabel() -> str \| None` | IDラベルを返します。 |
| `SetIDLabel(value: str) -> bool` | IDラベルを設定します。 |
| `GetSwingDirection() -> str \| None` | 開き方（扉の開閉。SwingOperation、SwingDirection、SwingHingeSideは"Swing"形式に適用）。 |
| `GetSwingHingeSide() -> str \| None` | 開き戸の蝶番の側を返します。 |
| `GetInteriorSide() -> str \| None` | 内側を返します。 |
| `GetIsFlipped() -> bool \| None` | *反転*がオンかどうか。 |
| `GetOpenAngle() -> float \| None` | 開き角度を返します。 |
| `GetSwingOperation() -> str \| None` | 開き戸の開閉方式を返します。 |

*旧式*

| メソッド | 説明 |
|---|---|
| `GetOperation() -> str \| None` | "Operation"として格納されます。`GetSwingOperation()`に置き換えられています。 |
| `Get3DOpen() -> bool \| None` | *3D時に開く*がオンかどうか。 |

継承メンバー：[`ArchitectObject`](#architectobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### ColumnObject

> **完全修飾名:** `api.ColumnObject` · **継承元:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

柱プラグインオブジェクトです。Vectorworksの柱で、ユニバーサル名は"Column2"です。`Is()`は古いファイルの旧式の"Column"プラグインオブジェクトも受け入れますが、パラメータは異なる場合があります。`Create()`はColumn2を作成し、旧式のプラグインしかインストールされていない場合はColumnを作成します。

柱は、建築用の柱身（四角形または丸）と、任意の柱脚および柱頭を備えた垂直の構造要素です。Vectorworks Architectでは任意の構造部材も含められます（"Use Component"を参照）。

Column2はVectorworksに付属するスクリプトプラグインです（Column2.vso。スクリプトはPilaster2と共有）。後述のパラメータ名は、このプラグインが定義し、VectorworksのIFC取り出しが読み取るユニバーサルパラメータ名です。ArchitectObjectの汎用GetParam.../SetParam...アクセサーを使用して読み書きし、`HasParam()` / `GetParamNames()`でオブジェクトを調べてください。

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）構成要素（Vectorworks Architect）

- "Use Component" — popup — Architectural Only / Structural Only / Architectural and Structural

全体のサイズ（ワールド単位）

- "OA Height" — real — 建築構成要素の高さ
- "Struct Height" — real — 構造構成要素の高さ
- "NewHeight" — real — 単一構成要素の高さの入力値

建築用の柱身（ワールド単位）

- "ShaftType" — popup — Rectangular / Oval。Customの柱身タイプはありません
- "Shaft Width" — real
- "Shaft Depth" — real
- "Shaft Radius" — real — 四角形の柱身の角の半径。丸の柱身では"Shaft Width"と"Shaft Depth"を等しくし、"ShaftType" = "Oval"を使用します。
- "Taper" — popup — `None`、またはテーパーの種類
- "Taper Width", "Taper Depth" — real
- "Arch Offset X", "Arch Offset Y", "Arch Offset Z" — real

柱脚

- "Use Base" — bool
- "BaseType" — popup
- "Base Height", "Base Width", "Base Depth", "Base Radius" — real
- "Base Divisions" — int

柱頭

- "Use Capital" — bool
- "CapitalType" — popup — 例：Oval Mushroom / Rectangular Mushroom
- "Capital Height", "Capital Width", "Capital Depth", "Capital Radius" — real

構造部材（鋼材の形状はShaftTypeではなくここで設定）

- "Struct Type" — popup — 例：Steel
- "Struct Shape", "Steel Shape" — popup
- "Struct Width", "Struct Depth", "Struct Radius" — real
- "Struct Rotation", "Struct Clearance" — real
- "Use Base Plate", "Use Top Plate" — bool
- "BP Width", "BP Depth", "BP Thickness", "BP Radius" — real — ベースプレート
- "TP Width", "TP Depth", "TP Thickness", "TP Radius" — real — トッププレート
- "BP Shape", "TP Shape" — popup

クラスと識別情報

- "Arch Class" — popup — クラス名
- "Column ID" — string

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ColumnObject(h: Handle)` | 既存の柱`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D) -> ColumnObject` *静的* | アクティブレイヤ／現在のコンテナの`position`に柱を作成します。Column2を作成し、旧式のプラグインしかインストールされていない場合はColumnを作成します。どちらもインストールされていない場合は無効なオブジェクトを返します。 |
| `Duplicate() -> ColumnObject` | 図面内の柱を複製し、そのコピーを返します。 |
| `GetTotalHeight() -> float \| None` | 有効な単一構成要素の高さです（ワールド単位）。OA HeightまたはStruct Height（"Use Component"）です。複合柱（Architectural and Structural）では構成要素が個別に境界に関連付けられているため、ゲッターは空を返し、セッターは失敗します。セッターはNewHeightと既存の上端境界のオフセットも更新し、その参照先を保持します。 |
| `SetTotalHeight(value: float) -> bool` | 全体の高さを設定します。有効な単一構成要素の高さです（ワールド単位）。OA HeightまたはStruct Height（"Use Component"）です。複合柱（Architectural and Structural）では構成要素が個別に境界に関連付けられているため、ゲッターは空を返し、セッターは失敗します。セッターはNewHeightと既存の上端境界のオフセットも更新し、その参照先を保持します。 |
| `GetShaftWidth() -> float \| None` | 四角形の柱身（ワールド単位）。 |
| `SetShaftWidth(value: float) -> bool` | 柱身の幅を設定します（四角形の柱身（ワールド単位））。 |
| `GetShaftDepth() -> float \| None` | 柱身の奥行きを返します。 |
| `SetShaftDepth(value: float) -> bool` | 柱身の奥行きを設定します。 |
| `GetShaftDiameter() -> float \| None` | 丸の柱身（ワールド単位）。丸以外の柱身ではゲッターは空を返します。セッターはOvalを選択し、幅と奥行きの両方を直径に設定します。 |
| `SetShaftDiameter(value: float) -> bool` | 柱身の直径を設定します。丸の柱身（ワールド単位）。丸以外の柱身ではゲッターは空を返します。セッターはOvalを選択し、幅と奥行きの両方を直径に設定します。 |
| `GetShape() -> str \| None` | ネイティブの柱身の形状です（"Rectangular" / "Oval"）。セッターは"Round"もOvalの別名として受け入れます。"Custom"は変更を行わずに`False`を返します。ネイティブの建築用の柱身にはCustomモードがありません。 |
| `SetShape(value: str) -> bool` | 形状を設定します。ネイティブの柱身の形状です（"Rectangular" / "Oval"）。セッターは"Round"もOvalの別名として受け入れます。"Custom"は変更を行わずに`False`を返します。ネイティブの建築用の柱身にはCustomモードがありません。 |

継承メンバー：[`ArchitectObject`](#architectobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### StairObject

> **完全修飾名:** `api.StairObject` · **継承元:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

階段プラグインオブジェクトです。Vectorworksの階段で、ユニバーサル名は"Stairs CW"です。

Stairs CWは構成（形状、階段部、踊り場、幅、手摺）を独自の設定に保持し、主な値を後述のパラメータに反映します。リセットのたびにTotalRise、Orientation、UpperLayer、平面表示のパラメータを再読み込みし、さらにWalkLineLength、TreadLength、RiserHeight、NumberOfRisersが正の場合はそれらも読み込み、階段を再計算して計算値を書き込みます。そのため、値を設定し、`Reset()`を呼び出してから、再計算された値を読み取ってください。StairWidthは再読み込みしません。

古い階段オブジェクトには対応していません。Vectorworksはファイルを開く際に2010より前の"Stair"オブジェクトを"Simple Stair"または"Custom Stair"に変換し、"Stair2"プラグインはインストールしません。これらにはParametricObjectを使用してください。

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）主な値（ワールド単位）

- "TotalRise" — real — 階段の高さ（上端と下端の高さの差）
- "WalkLineLength" — real — 歩行線の長さ（水平方向の全長）
- "StairWidth" — real — 最初の階段の幅。計算値であり、再読み込みはされません
- "TreadLength" — real — 段板奥行き（踏面寸法）
- "RiserHeight" — real
- "NumberOfRisers" — int
- "Orientation" — popup — RightHand / LeftHand
- "UpperLayer" — popup — 上階のレイヤ名

計算される数量（リセットのたびに書き込み）

- "StairArea" — real — 面積
- "NosingLength", "TreadLengthAtOffset" — real
- "Flight1Length" ... "Flight4Length" — real — 各階段部の歩行線の長さ
- "Flight1WalkingLineOffset" ... "Flight4WalkingLineOffset" — real
- "Flight1NumberOfRiser" ... "Flight4NumberOfRiser" — int
- "Flight1NumberOfTreads" ... "Flight4NumberOfTreads" — int

平面表示：各名前は両方の詳細レベル用に存在し、末尾がDetailedまたはSchematicになります

- "BreakModeLowerFloorDetailed" — popup — NoBreak / SolidSolid / SolidNone / NoneSolid / SolidDashed / DashedSolid / NoneDashed / DashedNone
- "BreakElevationDetailed" — real
- "BreakLineAngleDetailed" — real — 度
- "BreakLinesSeparationMMDetailed" — real — ミリメートル
- "ShowGuardrailOfInsideRailingDetailed" — bool
- "ShowGuardrailOfOutsideRailingDetailed" — bool

内部

- "ControlPoint01X" ... "ControlPoint14Y" — real — テキストラベルの位置
- "InternalVersionNumberOfRecordFormat" — int

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `StairObject(h: Handle)` | 既存の階段`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D) -> StairObject` *静的* | アクティブレイヤ／現在のコンテナの`position`に、デフォルトの構成のStairs CW階段を作成します。プラグインがインストールされていない場合は無効なオブジェクトを返します。 |
| `Duplicate() -> StairObject` | 図面内の階段を複製し、そのコピーを返します。 |
| `GetTotalRun() -> float \| None` | 全体の形状（ワールド単位）：TotalRunは"WalkLineLength"、TotalRiseは"TotalRise"、StairWidthは"StairWidth"、TreadDepthは"TreadLength"、RiserHeightは"RiserHeight"です。セッターは正の値を受け取り、階段は`Reset()`時に適用します。StairWidthは最初の階段の幅ですが、Stairs CWはこれを再読み込みしないため、SetStairWidthは`False`を返します。 |
| `SetTotalRun(value: float) -> bool` | 水平方向の全長を設定します。全体の形状（ワールド単位）：TotalRunは"WalkLineLength"、TotalRiseは"TotalRise"、StairWidthは"StairWidth"、TreadDepthは"TreadLength"、RiserHeightは"RiserHeight"です。セッターは正の値を受け取り、階段は`Reset()`時に適用します。StairWidthは最初の階段の幅ですが、Stairs CWはこれを再読み込みしないため、SetStairWidthは`False`を返します。 |
| `GetTotalRise() -> float \| None` | 全体の上り高さを返します。 |
| `SetTotalRise(value: float) -> bool` | 全体の上り高さを設定します。 |
| `GetStairWidth() -> float \| None` | 階段の幅を返します。 |
| `SetStairWidth(value: float) -> bool` | 階段の幅を設定します。 |
| `GetTreadDepth() -> float \| None` | 段板奥行きを返します。 |
| `SetTreadDepth(value: float) -> bool` | 段板奥行きを設定します。 |
| `GetRiserHeight() -> float \| None` | 蹴上げ寸法を返します。 |
| `SetRiserHeight(value: float) -> bool` | 蹴上げ寸法を設定します。 |
| `GetNumTreads() -> int \| None` | 数。NumRisersは"NumberOfRisers"（1から32767）です。Stairs CWには全体の踏面数がないため、GetNumTreadsは空を返し、SetNumTreadsは`False`を返します。 |
| `SetNumTreads(value: int) -> bool` | 踏面数を設定します。数。NumRisersは"NumberOfRisers"（1から32767）です。Stairs CWには全体の踏面数がないため、GetNumTreadsは空を返し、SetNumTreadsは`False`を返します。 |
| `GetNumRisers() -> int \| None` | 段数を返します。 |
| `SetNumRisers(value: int) -> bool` | 段数を設定します。 |

*構成と手摺*

| メソッド | 説明 |
|---|---|
| `GetConfiguration() -> str \| None` | Stairs CWはこれらをパラメータではなく独自の設定に保持します。ゲッターは空、セッターは`False`を返します。 |
| `SetConfiguration(value: str) -> bool` | 構成を設定します。Stairs CWはこれらをパラメータではなく独自の設定に保持します。ゲッターは空、セッターは`False`を返します。 |
| `GetHandrailLeft() -> bool \| None` | 手摺（前述を参照）。 |
| `SetHandrailLeft(value: bool) -> bool` | *左手摺*のオン／オフを切り替えます（手摺（前述を参照））。 |
| `GetHandrailRight() -> bool \| None` | *右手摺*がオンかどうか。 |
| `SetHandrailRight(value: bool) -> bool` | *右手摺*のオン／オフを切り替えます。 |

継承メンバー：[`ArchitectObject`](#architectobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

---

[一覧に戻る](README.md) · [先頭に戻る](#objectsarchitect--walls-roofs-slabs-windows-doors-columns-stairs)
