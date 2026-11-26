[English](../../PythonAPI/v2027.2/README.md) • [Deutsch](../../PythonAPI.de/v2027.2/README.md) • **日本語**

<a id="vectorworks-python-api-api--reference-for-vectorworks-2027-update-2"></a>

# Vectorworks Python API (`api`) — Vectorworks 2027 Update 2 リファレンス

このリファレンスは、VectorworksがスクリプトやAIワークフロー向けに提供するオブジェクト指向Pythonモジュール `api` を説明します。機能グループごとに1ページで構成し、すべてのページの先頭に目次を設け、各クラスを共通の形式で記載しています。

<a id="table-of-contents"></a>

## 目次

- [はじめに](#getting-started)
- [表記と使用上の規則](#conventions)
  - [モジュール](#modules)
  - [シグネチャの読み方](#reading-the-signatures)
  - [関数の呼び出し](#calling-functions)
  - [レコード](#records)
  - [列挙型](#enumerations)
  - [ハンドルとオブジェクト](#handles-and-objects)
  - [コピー、表示、ハッシュ](#copying-printing-and-hashing)
  - [コールバック](#callbacks)
  - [エラー](#errors)
- [APIツリー](#api-tree)
- [グループ別の内容](#contents-by-group)
- [A-Z索引](#index-az)
- [ページ構成](#page-layout)
- [統計](#statistics)

<a id="getting-started"></a>

## はじめに

```python
import api
from api.Math import Point2D

doc = api.Document()
if doc.IsOpen():
    for h in doc.GetSelection():
        obj = api.PrimitiveObject(h)
        print(obj.GetName(), obj.GetBounds())
```

- まず [`api.Document`](DocumentAccess.md#document) を参照してください。アクティブな図面、選択、レイヤ、ストーリ、クラス、環境設定を扱います。
- 図面オブジェクトの共通操作は [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) に記載されています。各クラスの継承情報を確認してください。たとえば、[`WorksheetObject`](ObjectsAnnotation.md#worksheetobject) は `PrimitiveObject` ではなく `TypedResource` から派生します。
- 純粋な数学値は直接サブモジュール [`api.Math`](ObjectPrimitives.Math.md) に属し、図面オブジェクトを作成しません。
- Vectorworksで `help(api.Document)` を実行すると、そのクラスのシグネチャを表示できます。

ここに記載するVectorworksの操作には `api` と `api.Math` のみを使用してください。別のインターフェイスである `vs` の呼び出しを混在させたり、未対応の機能の代替として使用したりしないでください。標準ライブラリのインポートは使用できます。存在しないAPI呼び出しを作り出すのではなく、その操作が未対応であることを説明してください。

[スクリプトリソースとパレット](Scripting.md) の管理はできますが、`api` からスクリプトを実行することはできません。すでに開いているダイアログの自動操作や、遅延実行ヘルパー `RunLater` / `RunOnEventLoop` は利用できません。[ダイアログの作成、アラート、標準ダイアログ](UILayoutCreate.md) は引き続き利用できます。使用上の規則とレシピの全体は [AI-CONTEXT.md](../../PythonAPI/v2027.2/AI-CONTEXT.md) を参照してください。

<a id="conventions"></a>

## 表記と使用上の規則

| 項目 | 規則 |
|---|---|
| 戻り値 | ゲッターは値を取得できない場合に `None` を返します。ただし、ハンドルのゲッターはnullハンドル、コレクションのゲッターは空のリスト、個数のゲッターは0を返します。図面オブジェクトの作成メソッドは失敗時に無効なオブジェクトを返します。多くのセッターと操作は `True` / `False` を返します。各シグネチャと戻り値を確認してください。 |
| 単位 | ワールド座標の長さと座標は、ファイルの単位にかかわらずミリメートルです。ファイルの単位の変換には `Document.UnitsToWorld` / `Document.WorldToUnits` を使用します。別の記載がない限り、角度は+X軸から反時計回りのラジアンです。 |
| 単位の例外 | `Marker.angle`、`DropShadow.angle`、`RoofObject.Edge.slope` は度、`Marker.length` / `Marker.width` は用紙上のインチを使用します。`*Mils` の線幅は1/1000インチです。`GetParamReal` / `SetParamReal` で直接読み書きするプラグインの角度パラメータは度、長さパラメータはワールド単位を使用します。 |
| インデックス | 0始まりです。ただし、ワークシートの行と列は1始まりです。 |
| 色 | `ColorRGB` のチャンネルは0–65535です。8ビットの値には `ColorRGB.FromRGB8` / `Red8()` を使用します。カラーインデックスはRGB値ではなく、パレットのインデックスです。不透明度は0–100です (`api.kMaxOpacity`)。 |
| 文字列 | Pythonの `str` をUTF-8で受け渡します。名前の検索は大文字と小文字を区別しませんが、プラグインのユニバーサル名は正確に渡してください。 |
| ハンドル | nullハンドルを引数として渡す場合は `None` を使用します。戻り値のnullの `api.Handle` は真偽値として偽と評価されます。`h is None` ではなく `if h:` で確認してください。オブジェクトクラスはハンドルに対する軽量なビューで、`bool(obj)` は `IsValid()` と同じです。 |
| 取り消し | 図面の変更には取り消しイベントと適切なオブジェクト登録が必要です。読み取り専用のスクリプトはイベントを開始してはいけません。`StartUndoEvent(isRevertible=True)`、ロールバック、アプリケーションが管理するイベントについては、[取り消しの手順](../../PythonAPI/v2027.2/AI-CONTEXT.md#3-undo---required-around-every-drawing-change) を参照してください。 |
| 名前 | Pythonのキーワードと衝突するメンバー名には末尾にアンダースコアが付きます (`None_`)。引数名も同様です (`from_`)。 |
| レコード | 値型はPythonが所有するコピーです。変更後にセッターへ渡してください。フィールド値から作成できます (`api.ColorRGB(red=65535)`)。 |
| 列挙型 | `IntEnum` です (`api.Descend` は `IntFlag`)。通常の整数も受け付けます。 |
| 引数 | すべての引数にキーワード名があります。デフォルト値のある引数は省略可能です。レコードの引数にはタプル、リスト、dictも渡せます。 |
| シグネチャ | `Name(param: type = default) -> result`。*静的* は静的メソッドを示します。`T \| None` は任意の戻り値です。 |

<a id="modules"></a>

### モジュール

| 名前 | 説明 |
|---|---|
| `api` | モジュール本体。`api.Document()` から始めてください。 |
| `api.Math` | 独立した2D/3D数学値を提供する `api` の直下のサブモジュール ([Math](ObjectPrimitives.Math.md))。`import api.Math` と `from api.Math import Point2D` を使用できます。`ObjectPrimitives` の下に入れ子になっているわけではありません。 |
| `api.Object` | すべての `api` クラスの基底クラス ([コピー、表示、ハッシュ](#copying-printing-and-hashing)を参照)。 |
| `api.Handle` | Vectorworksオブジェクトのハンドル。戻り値のハンドルは `None` と比較するのではなく、真偽値として確認してください。 |

<a id="reading-the-signatures"></a>

### シグネチャの読み方

シグネチャでは次の型を使用します。

| 型 | 意味 |
|---|---|
| `bool`, `int`, `float`, `str` | Pythonの組み込み値。`float` を受け取る場所に `int` を渡すこともできます。 |
| `Handle` | Vectorworksオブジェクトのハンドル (`api.Handle`)。nullハンドルを引数として渡す場合は `None` を使用します。戻り値のnullハンドルは真偽値として偽と評価されます。`GetHandle()` を持つ任意のオブジェクトも受け付けます。 |
| `T \| None` | 任意の値。`None` は「値なし」を意味します。 |
| `list[T]` | リスト (引数にはリストまたはタプルを渡せます)。 |
| `tuple[T * N]` | 正確にN個の値を持つタプル。 |
| `tuple[A, B]` | 2つの値の組。 |
| `dict[K, V]` | 辞書。 |
| `callable(A, ...)` | 列挙された引数を受け取る任意のPython呼び出し可能オブジェクト ([コールバック](#callbacks)を参照)。 |
| `bytes` | `bytes`、`bytearray`、その他のバッファー (`str` ではありません)。 |
| `type` | `api` クラス。例: `api.Document.As(api.ArcObject, h)` の `api.ArcObject`。静的な `Is(h)` とハンドルを受け取るコンストラクタを持つクラスのみが該当します。 |
| `object` | 任意のPythonオブジェクト。返される内容はメソッドの説明に記載します。 |
| 列挙型の名前 | `IntEnum` / `IntFlag` クラス。通常の整数も受け付けます。 |
| クラス名 | `api` クラス。レコードの引数はタプル、リスト、dictも受け付けます ([レコード](#records)を参照)。 |

デフォルト値はPythonの式で示します (`2**64 - 1` は「無制限」)。同じ名前が複数行にあるメソッドは、複数の引数リスト (オーバーロード) を受け付けます。

<a id="calling-functions"></a>

### 関数の呼び出し

- **オーバーロード:** 複数の引数リストを受け取るメソッドでは、最初に型の完全一致で、次にここに記載する変換を使って、最初に適合するものを選択します。レコード型でオーバーロードを区別する場合は、型を明示して作成してください。`ToolControl.Click` にタプルを渡すと `Point2D` が選択されるため、ほかの座標型には `api.Point3D(...)` または `api.ViewPoint(...)` を使用します。
- **キーワードとデフォルト値:** すべての引数は、シグネチャにある名前のキーワード引数で渡せます。デフォルト値のある引数は省略できます。
- **静的メソッド:** *静的* と記載したメソッドは、クラス (`api.ArcObject.Create(...)`) またはインスタンスから呼び出せます。同じ名前に静的とインスタンスの両方の行がある場合は、インスタンスから呼んでください。
- **変換:** レコード引数には、タプル/リスト (コンストラクタの値)、dict (フィールド値)、互換性のあるレコードを渡せます (`api.Math.Point2D` と `api.Point2D`、および `api.Math.Point3D` と `api.Point3D` はそれぞれ相互変換)。`bool` または `float` には `int`、`Handle` には `GetHandle()` メソッドを持つ任意のオブジェクトを渡せます。
- **戻り値:** 戻り値は新しいPython値です。ただし、値をその場で変更して返すメソッド (例: `Math.Point2D.Normalize()`) は同じPythonオブジェクトを返すため、呼び出しを連結できます。
- **演算子:** 比較/算術演算子は未対応のオペランドに `NotImplemented` を返し、Pythonが左右を入れ替えた演算を試せるようにします。

<a id="records"></a>

### レコード

レコード (`api.ColorRGB`、`api.WallObject.Heights`、`api.Math.Point2D` などの値型) はPythonが所有する値です。レコードを変更しても図面は変わりません。取得元に対応するセッターへ渡してください。

引数に適合するコンストラクタがない場合、フィールド値からもレコードを作成できます。すべてのフィールドを位置引数 (「フィールド」表の順序で、基底クラスのフィールドが先) で渡すか、任意のフィールドをキーワード引数で指定します。例: `api.ColorRGB(red=65535)`。コンストラクタもフィールドもないクラスはPythonから作成できません。

レコード型のフィールドは、その所有者の値への直接の参照として取得されます (`rect.origin.x = 1` は `rect` を変更)。それ以外の型 (数値、文字列、リスト、任意値) のフィールドはコピーとして取得されます。フィールドは削除できません。

<a id="enumerations"></a>

### 列挙型

列挙型は `enum.IntEnum` クラスです (`api.Descend` は `enum.IntFlag` で、`|` でメンバーを組み合わせます)。入れ子の列挙型はそのクラスに属します (`api.TextObject.HorizontalAlignment`)。Pythonキーワードと衝突するメンバー名には末尾に `_` が付きます (`api.Descend.None_`)。引数には通常の整数も渡せ、対応するメンバーのない値は整数で返ります。

<a id="handles-and-objects"></a>

### ハンドルとオブジェクト

オブジェクトのハンドルは `api.Handle` の値です。nullハンドルを引数として渡す場合は `None` を使用しますが、戻り値のハンドルは `if h:` で確認してください。nullハンドルは `None` ではありません。ハンドルに互換性があっても `api` と `vs` を混在させてはいけません。オブジェクトクラスはハンドルに対する軽量なビューで、図面の図形を所有しません。多くのクラスは静的な `Is(h)` とハンドルを受け取るコンストラクタを持ちます。異なる種類のハンドルから作成すると無効になります (`IsValid()` / `bool(obj)` は `False`)。`api.Document.As(type, h)` は型付きオブジェクトまたは `None` を返します。

基底の参照型である `PrimitiveObject(h)`、`ArchitectObject(h)`、`LandmarkObject(h)`、`AnnotationObject(h)` は、nullでない任意のハンドルを受け付けます。具体的なクラスはオブジェクトの種類を確認します。`Delete()` は呼び出し元の参照を無効にします。削除されたオブジェクトのほかの参照やハンドルを使用しないでください。

<a id="copying-printing-and-hashing"></a>

### コピー、表示、ハッシュ

すべての `api` クラスは `api.Object` から派生し、次を利用できます。

| メンバー | 説明 |
|---|---|
| `copy.copy(x)` / `copy.deepcopy(x)` | 値のコピー。オブジェクトクラスでは参照 (ハンドル) をコピーし、図面の図形は**コピーしません**。図形の複製には `Duplicate()` を使用してください。コピーできないクラス (例: `ResourceList`) では `TypeError` が発生します。 |
| `repr(x)` | レコードはフィールド (`api.ColorRGB(red=0, green=0, blue=0)`)、オブジェクトクラスはハンドル (`<api.ArcObject handle=0x...>`)、`__init__` が呼ばれていないインスタンスは `<... (not initialized)>` を表示します。 |
| `hash(x)` | オブジェクトクラスはハンドルでハッシュ化されるため、辞書のキーや集合のメンバーにできます。レコードはハッシュ化できません。図面オブジェクト、レイヤ、クラス、リソースは `==` でハンドルを比較します。値型の等価比較は「演算子」表に記載されています。それ以外のPythonオブジェクトは同一性で比較します。 |

<a id="callbacks"></a>

### コールバック

`callable(...)` 型の引数は、任意のPython呼び出し可能オブジェクトを受け取ります (例: 走査用の `Document.ForEachObject`)。同期的に呼び出され、戻り値は無視されるため、走査を途中で終了することはできません。途中で終了したい場合は、リストを返す対応メソッドを使用してください。呼び出しで例外が発生すると、残りの呼び出しはスキップされ、メソッドが戻る際に例外が伝播します。

<a id="errors"></a>

### エラー

操作の失敗は、記載された戻り値によって報告されます。必ず戻り値を確認してください。Pythonの使用方法や変換のエラー、および以下に挙げるジオメトリ操作の失敗では以下の例外が発生し、コールバック内の例外は呼び出し元に伝播します。

| 状況 | Pythonの例外 |
|---|---|
| メソッドのどの引数リストにも適合しない | `TypeError`。メソッドのすべてのシグネチャを表示します。 |
| Pythonから作成できないクラスの作成、または `__init__` が呼ばれていないインスタンスの使用 (サブクラスなど) | `TypeError`。 |
| 不適切な型の値をフィールドに設定、またはフィールドを削除 | `TypeError`。 |
| コピーできないクラスをコピー | `TypeError`。 |
| 数学値の範囲外のインデックス (例: `Polygon2D`) | `IndexError`。 |
| ジオメトリ操作の失敗: `Math.Polygon2D`の`Union`、`Intersection`、`Difference`、`SymmetricDifference`、`Offset`、`PolyObject`の`BooleanUnion`、`BooleanIntersection`、`BooleanDifference`、`BooleanSymmetricDifference`、`CombineShapes` | `RuntimeError`（メッセージ付き）。 |
| 変換できない戻り値 | `RuntimeError`。 |
| モジュールを初期化できない | `import api` で `ImportError`。 |

<a id="api-tree"></a>

## APIツリー

`Math` は `api` の直下のサブモジュールです。以下のほかの項目は、`api.Document` や `api.PrimitiveObject` のように `api` の直下に公開される名前をまとめたドキュメントのグループであり、Pythonのサブモジュールではありません。リファレンスのファイル名はPythonの名前空間を定義しません。`ObjectPrimitives.Math.md` が説明するのは `api.Math` です。

```text
api
├── Math  (api.Math)               → ObjectPrimitives.Math.md
├── DocumentAccess                 → DocumentAccess.md
├── Attributes                     → Attributes.md
├── ObjectPrimitives               → ObjectPrimitives.md
├── Objects3D                      → Objects3D.md
├── ObjectsAnnotation              → ObjectsAnnotation.md
├── ObjectsArchitect               → ObjectsArchitect.md
├── ObjectsConnectCAD              → ObjectsConnectCAD.md
├── ObjectsLandmark                → ObjectsLandmark.md
├── ObjectsSpotlight               → ObjectsSpotlight.md
├── Resources                      → Resources.md
├── Scripting                      → Scripting.md
├── UIAutomation                   → UIAutomation.md
└── UILayoutCreate                 → UILayoutCreate.md
```

<a id="contents-by-group"></a>

## グループ別の内容

- **[DocumentAccess](DocumentAccess.md)** — アクティブファイル: 選択、オブジェクト、レイヤ、ストーリ、クラス、ビュー、単位、取り消し、環境設定。
  - クラス:
    - [`TextStyleData`](DocumentAccess.md#textstyledata)
    - [`ProgramVariables`](DocumentAccess.md#programvariables)
    - [`DisplaySettings`](DocumentAccess.md#displaysettings)
    - [`EditingSettings`](DocumentAccess.md#editingsettings)
    - [`SnapSettings`](DocumentAccess.md#snapsettings)
    - [`GridSettings`](DocumentAccess.md#gridsettings)
    - [`StackLayersSettings`](DocumentAccess.md#stacklayerssettings)
    - [`UnitSettings`](DocumentAccess.md#unitsettings)
    - [`TextDefaults`](DocumentAccess.md#textdefaults)
    - [`DefaultAttributes`](DocumentAccess.md#defaultattributes)
    - [`LayerContents`](DocumentAccess.md#layercontents)
    - [`Layer`](DocumentAccess.md#layer)
    - [`StoryLevel`](DocumentAccess.md#storylevel)
    - [`StoryLevelTemplate`](DocumentAccess.md#storyleveltemplate)
    - [`Story`](DocumentAccess.md#story)
    - [`Document`](DocumentAccess.md#document)
  - 列挙型: [`Traverse`](DocumentAccess.md#traverse) · [`Descend`](DocumentAccess.md#descend) · [`LayerType`](DocumentAccess.md#layertype) · [`LayerVisibility`](DocumentAccess.md#layervisibility) · [`VisibilityOptions`](DocumentAccess.md#visibilityoptions) · [`StoryElevationChangeMode`](DocumentAccess.md#storyelevationchangemode) · [`UndoMethod`](DocumentAccess.md#undomethod) · [`AngularUnit`](DocumentAccess.md#angularunit) · [`TextJustification`](DocumentAccess.md#textjustification) · [`TextVerticalAlignment`](DocumentAccess.md#textverticalalignment) · [`TextLineSpacing`](DocumentAccess.md#textlinespacing)
- **[Attributes](Attributes.md)** — 線、面、面のマッピング、マーカー、ドロップシャドウ、オブジェクト属性、クラス、属性の値型。
  - クラス:
    - [`Point2D`](Attributes.md#point2d)
    - [`ColorRGB`](Attributes.md#colorrgb)
    - [`ColorPair`](Attributes.md#colorpair)
    - [`ObjectColors`](Attributes.md#objectcolors)
    - [`Marker`](Attributes.md#marker)
    - [`DropShadow`](Attributes.md#dropshadow)
    - [`WallTextures`](Attributes.md#walltextures)
    - [`RoofTextures`](Attributes.md#rooftextures)
    - [`AttributesBase`](Attributes.md#attributesbase)
    - [`PenAttributes`](Attributes.md#penattributes)
    - [`FillAttributes`](Attributes.md#fillattributes)
    - [`FillMappingAttributes`](Attributes.md#fillmappingattributes) — [`Frame`](Attributes.md#fillmappingattributesframe)
    - [`MarkerAttributes`](Attributes.md#markerattributes)
    - [`DropShadowAttributes`](Attributes.md#dropshadowattributes)
    - [`ClassAttributes`](Attributes.md#classattributes)
    - [`ObjectAttributes`](Attributes.md#objectattributes)
  - 列挙型: [`PenStyleKind`](Attributes.md#penstylekind) · [`FillType`](Attributes.md#filltype) · [`MarkerShape`](Attributes.md#markershape) · [`MarkerFill`](Attributes.md#markerfill) · [`MarkerBase`](Attributes.md#markerbase) · [`MarkerHalfTick`](Attributes.md#markerhalftick) · [`MarkerThicknessBasis`](Attributes.md#markerthicknessbasis) · [`MarkerThicknessUnits`](Attributes.md#markerthicknessunits) · [`DropShadowUnits`](Attributes.md#dropshadowunits) · [`ClassVisibility`](Attributes.md#classvisibility) · [`ObjectType`](Attributes.md#objecttype)
  - [モジュール定数](Attributes.md#module-constants): `kMaxOpacity`
- **[ObjectPrimitives](ObjectPrimitives.md)** — 共通のオブジェクト基底クラス (PrimitiveObject) と2Dオブジェクト: 直線、四角形、円弧、円、多角形、曲線、グループ、プラグインオブジェクト、文字列。
  - クラス:
    - [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) — [`Bounds3D`](ObjectPrimitives.md#primitiveobjectbounds3d)
    - [`Locus2DObject`](ObjectPrimitives.md#locus2dobject)
    - [`Line2DObject`](ObjectPrimitives.md#line2dobject)
    - [`RectangularObject`](ObjectPrimitives.md#rectangularobject)
    - [`RectangleObject`](ObjectPrimitives.md#rectangleobject)
    - [`CornerDiameters`](ObjectPrimitives.md#cornerdiameters)
    - [`RoundRectObject`](ObjectPrimitives.md#roundrectobject)
    - [`ArcObject`](ObjectPrimitives.md#arcobject)
    - [`CircleObject`](ObjectPrimitives.md#circleobject)
    - [`PolyObject`](ObjectPrimitives.md#polyobject) — [`BooleanOperation`](ObjectPrimitives.md#polyobjectbooleanoperation)
    - [`PolygonObject`](ObjectPrimitives.md#polygonobject)
    - [`PolylineObject`](ObjectPrimitives.md#polylineobject)
    - [`GroupObject`](ObjectPrimitives.md#groupobject)
    - [`ParametricObject`](ObjectPrimitives.md#parametricobject) — [`PluginKind`](ObjectPrimitives.md#parametricobjectpluginkind)
    - [`TextObject`](ObjectPrimitives.md#textobject) — [`StyleRun`](ObjectPrimitives.md#textobjectstylerun) · [`TabStop`](ObjectPrimitives.md#textobjecttabstop) · [`HorizontalAlignment`](ObjectPrimitives.md#textobjecthorizontalalignment) · [`VerticalAlignment`](ObjectPrimitives.md#textobjectverticalalignment) · [`Spacing`](ObjectPrimitives.md#textobjectspacing) · [`TabAlignment`](ObjectPrimitives.md#textobjecttabalignment)
- **[Math (`api.Math`)](ObjectPrimitives.Math.md)** — api.Mathサブモジュール: 点/ベクトル、変換、四角形、直線、平面、円、円弧、多角形、ユーティリティ。
  - クラス:
    - [`Math.Point2D`](ObjectPrimitives.Math.md#mathpoint2d)
    - [`Math.Transform2D`](ObjectPrimitives.Math.md#mathtransform2d)
    - [`Math.Rect2D`](ObjectPrimitives.Math.md#mathrect2d)
    - [`Math.RotatedRect2D`](ObjectPrimitives.Math.md#mathrotatedrect2d)
    - [`Math.Line2D`](ObjectPrimitives.Math.md#mathline2d) — [`Intersection`](ObjectPrimitives.Math.md#mathline2dintersection)
    - [`Math.Circle2D`](ObjectPrimitives.Math.md#mathcircle2d)
    - [`Math.Arc2D`](ObjectPrimitives.Math.md#matharc2d)
    - [`Math.PolyVertex`](ObjectPrimitives.Math.md#mathpolyvertex)
    - [`Math.Polygon2D`](ObjectPrimitives.Math.md#mathpolygon2d) — [`CurveLocation`](ObjectPrimitives.Math.md#mathpolygon2dcurvelocation)
    - [`Math.Point3D`](ObjectPrimitives.Math.md#mathpoint3d)
    - [`Math.Transform3D`](ObjectPrimitives.Math.md#mathtransform3d)
    - [`Math.Line3D`](ObjectPrimitives.Math.md#mathline3d)
    - [`Math.Plane3D`](ObjectPrimitives.Math.md#mathplane3d)
  - 列挙型: [`Math.VertexType`](ObjectPrimitives.Math.md#mathvertextype) · [`Math.OffsetJoin`](ObjectPrimitives.Math.md#mathoffsetjoin)
  - [モジュール関数](ObjectPrimitives.Math.md#module-functions): `AngleDelta`, `AnglesAreEqual`, `AreEqual`, `Clamp`, `DegToRad`, `IsBetween`, `IsGreater`, `IsLess`, `IsZero`, `Lerp`, `NormalizeAngle`, `NormalizeAngleSigned`, `RadToDeg`, `Sign`
  - [モジュール定数](ObjectPrimitives.Math.md#module-constants): `kPi`, `kTwoPi`, `kHalfPi`, `kEpsilon`, `kAngleEpsilon`
- **[Objects3D](Objects3D.md)** — 押し出し、多段押し出し、回転体、ソリッド、プリミティブ (球、円錐など)、NURBS、3D 多角形、メッシュ、シェル。
  - クラス:
    - [`ExtrudeObject`](Objects3D.md#extrudeobject) — [`Values`](Objects3D.md#extrudeobjectvalues) · [`Transform`](Objects3D.md#extrudeobjecttransform)
    - [`SweepObject`](Objects3D.md#sweepobject) — [`Values`](Objects3D.md#sweepobjectvalues)
    - [`MultiExtrudeObject`](Objects3D.md#multiextrudeobject)
    - [`SurfaceModelObject`](Objects3D.md#surfacemodelobject) — [`PathOptions`](Objects3D.md#surfacemodelobjectpathoptions)
    - [`GenericSolidObject`](Objects3D.md#genericsolidobject) — [`HistoryStep`](Objects3D.md#genericsolidobjecthistorystep) · [`Operation`](Objects3D.md#genericsolidobjectoperation)
    - [`ShellObject`](Objects3D.md#shellobject)
    - [`Polygon3DObject`](Objects3D.md#polygon3dobject) — [`Plane`](Objects3D.md#polygon3dobjectplane) · [`ClosestPoint`](Objects3D.md#polygon3dobjectclosestpoint)
    - [`MeshObject`](Objects3D.md#meshobject) — [`Face`](Objects3D.md#meshobjectface) · [`Part`](Objects3D.md#meshobjectpart) · [`Smoothing`](Objects3D.md#meshobjectsmoothing)
    - [`SolidPrimitiveObject`](Objects3D.md#solidprimitiveobject) — [`Kind`](Objects3D.md#solidprimitiveobjectkind)
    - [`SphereObject`](Objects3D.md#sphereobject)
    - [`HemisphereObject`](Objects3D.md#hemisphereobject)
    - [`ConeObject`](Objects3D.md#coneobject) — [`Radii`](Objects3D.md#coneobjectradii)
    - [`NurbsCurveObject`](Objects3D.md#nurbscurveobject) — [`Location`](Objects3D.md#nurbscurveobjectlocation)
    - [`NurbsSurfaceObject`](Objects3D.md#nurbssurfaceobject)
- **[ObjectsAnnotation](ObjectsAnnotation.md)** — 寸法 (直線、角度、円弧長、半径)、センターマーク、データタグ、図面枠、ワークシート。
  - クラス:
    - [`AnnotationObject`](ObjectsAnnotation.md#annotationobject)
    - [`DataTagObject`](ObjectsAnnotation.md#datatagobject) — [`LeaderType`](ObjectsAnnotation.md#datatagobjectleadertype) · [`HorizontalPosition`](ObjectsAnnotation.md#datatagobjecthorizontalposition) · [`MoveBehaviour`](ObjectsAnnotation.md#datatagobjectmovebehaviour)
    - [`TitleBlockBorderObject`](ObjectsAnnotation.md#titleblockborderobject) — [`Revision`](ObjectsAnnotation.md#titleblockborderobjectrevision)
    - [`DimensionObject`](ObjectsAnnotation.md#dimensionobject)
    - [`LinearDimensionObject`](ObjectsAnnotation.md#lineardimensionobject)
    - [`AngularDimensionObject`](ObjectsAnnotation.md#angulardimensionobject)
    - [`ArcLengthDimensionObject`](ObjectsAnnotation.md#arclengthdimensionobject)
    - [`RadialDimensionObject`](ObjectsAnnotation.md#radialdimensionobject)
    - [`CenterMarkObject`](ObjectsAnnotation.md#centermarkobject)
    - [`WorksheetObject`](ObjectsAnnotation.md#worksheetobject) — [`Range`](ObjectsAnnotation.md#worksheetobjectrange) · [`NumberFormat`](ObjectsAnnotation.md#worksheetobjectnumberformat) · [`TextFormat`](ObjectsAnnotation.md#worksheetobjecttextformat) · [`Fill`](ObjectsAnnotation.md#worksheetobjectfill) · [`Borders`](ObjectsAnnotation.md#worksheetobjectborders)
  - 列挙型: [`DimensionKind`](ObjectsAnnotation.md#dimensionkind) · [`DimensionTolerance`](ObjectsAnnotation.md#dimensiontolerance)
- **[ObjectsArchitect](ObjectsArchitect.md)** — 建築オブジェクト: 壁、屋根、スラブ、窓、ドア、柱、階段。
  - クラス:
    - [`ArchitectObject`](ObjectsArchitect.md#architectobject)
    - [`WallObject`](ObjectsArchitect.md#wallobject) — [`Heights`](ObjectsArchitect.md#wallobjectheights) · [`HeightBound`](ObjectsArchitect.md#wallobjectheightbound) · [`Caps`](ObjectsArchitect.md#wallobjectcaps) · [`BoundStatus`](ObjectsArchitect.md#wallobjectboundstatus) · [`BoundKind`](ObjectsArchitect.md#wallobjectboundkind)
    - [`SlabObject`](ObjectsArchitect.md#slabobject)
    - [`RoofObject`](ObjectsArchitect.md#roofobject) — [`Attributes`](ObjectsArchitect.md#roofobjectattributes) · [`Accessories`](ObjectsArchitect.md#roofobjectaccessories) · [`Edge`](ObjectsArchitect.md#roofobjectedge) · [`MiterType`](ObjectsArchitect.md#roofobjectmitertype)
    - [`WindowObject`](ObjectsArchitect.md#windowobject)
    - [`DoorObject`](ObjectsArchitect.md#doorobject)
    - [`ColumnObject`](ObjectsArchitect.md#columnobject)
    - [`StairObject`](ObjectsArchitect.md#stairobject)
- **[ObjectsConnectCAD](ObjectsConnectCAD.md)** — ConnectCADの配線略図のDevice (JSONの記述から作成)、Socket、Device Type、Signal/Connector Type。
  - クラス:
    - [`ConnectCADLibrary`](ObjectsConnectCAD.md#connectcadlibrary) — [`Signal`](ObjectsConnectCAD.md#connectcadlibrarysignal) · [`Connector`](ObjectsConnectCAD.md#connectcadlibraryconnector) · [`Validation`](ObjectsConnectCAD.md#connectcadlibraryvalidation) · [`DeviceDefinition`](ObjectsConnectCAD.md#connectcadlibrarydevicedefinition)
    - [`ConnectCADSocketObject`](ObjectsConnectCAD.md#connectcadsocketobject)
    - [`ConnectCADDeviceObject`](ObjectsConnectCAD.md#connectcaddeviceobject) — [`CreateResult`](ObjectsConnectCAD.md#connectcaddeviceobjectcreateresult) · [`AddSocketResult`](ObjectsConnectCAD.md#connectcaddeviceobjectaddsocketresult) · [`DeviceTypeResult`](ObjectsConnectCAD.md#connectcaddeviceobjectdevicetyperesult)
- **[ObjectsLandmark](ObjectsLandmark.md)** — Landmarkオブジェクト: 植栽、ランドスケープエリア、地形モデルと造成図形、レベルオブジェクト、舗床、境界線、既存樹木。
  - クラス:
    - [`LandmarkObject`](ObjectsLandmark.md#landmarkobject)
    - [`PlantObject`](ObjectsLandmark.md#plantobject) — [`Config`](ObjectsLandmark.md#plantobjectconfig) · [`TagDisplay`](ObjectsLandmark.md#plantobjecttagdisplay)
    - [`LandscapeAreaObject`](ObjectsLandmark.md#landscapeareaobject) — [`PlantDisplay2D`](ObjectsLandmark.md#landscapeareaobjectplantdisplay2d) · [`DrawingMode`](ObjectsLandmark.md#landscapeareaobjectdrawingmode) · [`AreaUnits`](ObjectsLandmark.md#landscapeareaobjectareaunits)
    - [`SiteModelObject`](ObjectsLandmark.md#sitemodelobject) — [`Display2D`](ObjectsLandmark.md#sitemodelobjectdisplay2d) · [`Display3D`](ObjectsLandmark.md#sitemodelobjectdisplay3d)
    - [`SiteModifierObject`](ObjectsLandmark.md#sitemodifierobject) — [`Config`](ObjectsLandmark.md#sitemodifierobjectconfig) · [`ApplyTo`](ObjectsLandmark.md#sitemodifierobjectapplyto)
    - [`StakeObject`](ObjectsLandmark.md#stakeobject) — [`Mode`](ObjectsLandmark.md#stakeobjectmode) · [`SiteModel`](ObjectsLandmark.md#stakeobjectsitemodel)
    - [`HardscapeObject`](ObjectsLandmark.md#hardscapeobject) — [`Mode3D`](ObjectsLandmark.md#hardscapeobjectmode3d)
    - [`PropertyLineObject`](ObjectsLandmark.md#propertylineobject) — [`AreaUnits`](ObjectsLandmark.md#propertylineobjectareaunits)
    - [`ExistingTreeObject`](ObjectsLandmark.md#existingtreeobject) — [`Origin`](ObjectsLandmark.md#existingtreeobjectorigin) · [`TreeProtection`](ObjectsLandmark.md#existingtreeobjecttreeprotection) · [`Condition`](ObjectsLandmark.md#existingtreeobjectcondition) · [`SULE`](ObjectsLandmark.md#existingtreeobjectsule) · [`Significance`](ObjectsLandmark.md#existingtreeobjectsignificance) · [`Action`](ObjectsLandmark.md#existingtreeobjectaction)
- **[ObjectsSpotlight](ObjectsSpotlight.md)** — SpotlightのLighting DeviceとGDTF器具タイプライブラリ (取り込み、利用可能なモード)。
  - クラス:
    - [`LightingDeviceObject`](ObjectsSpotlight.md#lightingdeviceobject)
    - [`GDTFLibrary`](ObjectsSpotlight.md#gdtflibrary) — [`Entry`](ObjectsSpotlight.md#gdtflibraryentry) · [`ImportResult`](ObjectsSpotlight.md#gdtflibraryimportresult)
- **[Resources](Resources.md)** — リソースマネージャ関連: 任意の種類のリソース、リソースリストと取り込み、型付きリソース (ハッチング、シンボル、スタイルなど)。
  - クラス:
    - [`Resource`](Resources.md#resource)
    - [`ResourceList`](Resources.md#resourcelist) — [`Entry`](Resources.md#resourcelistentry) · [`ImportResult`](Resources.md#resourcelistimportresult)
    - [`TypedResource`](Resources.md#typedresource)
    - [`HatchLevel`](Resources.md#hatchlevel)
    - [`Hatch`](Resources.md#hatch)
    - [`GradientSegment`](Resources.md#gradientsegment)
    - [`Gradient`](Resources.md#gradient)
    - [`Tile`](Resources.md#tile)
    - [`ImageFill`](Resources.md#imagefill) — [`Compression`](Resources.md#imagefillcompression)
    - [`LineType`](Resources.md#linetype)
    - [`RecordField`](Resources.md#recordfield)
    - [`RecordFormat`](Resources.md#recordformat)
    - [`Texture`](Resources.md#texture) — [`Part`](Resources.md#texturepart)
    - [`RenderStyle`](Resources.md#renderstyle)
    - [`RenderBackground`](Resources.md#renderbackground) — [`Kind`](Resources.md#renderbackgroundkind)
    - [`TextStyle`](Resources.md#textstyle)
    - [`WallStyle`](Resources.md#wallstyle)
    - [`SlabStyle`](Resources.md#slabstyle)
    - [`RoofStyle`](Resources.md#roofstyle)
    - [`ViewportStyle`](Resources.md#viewportstyle)
    - [`BuildingMaterial`](Resources.md#buildingmaterial)
    - [`DataVisualization`](Resources.md#datavisualization)
    - [`ResourceFolderPath`](Resources.md#resourcefolderpath)
    - [`ResourceFolder`](Resources.md#resourcefolder)
    - [`SymbolDefinition`](Resources.md#symboldefinition) — [`GeometryType`](Resources.md#symboldefinitiongeometrytype) · [`InsertMode`](Resources.md#symboldefinitioninsertmode) · [`BreakMode`](Resources.md#symboldefinitionbreakmode)
    - [`WorksheetCell`](Resources.md#worksheetcell)
    - [`WorksheetCellContent`](Resources.md#worksheetcellcontent)
    - [`Worksheet`](Resources.md#worksheet)
  - 列挙型: [`ResourceType`](Resources.md#resourcetype) · [`ContentFolder`](Resources.md#contentfolder) · [`ImportConflict`](Resources.md#importconflict) · [`RecordFieldType`](Resources.md#recordfieldtype)
- **[Scripting](Scripting.md)** — ファイルに保存されるスクリプトリソース (VectorScript / Python) とスクリプトパレット。
  - クラス:
    - [`ScriptResource`](Scripting.md#scriptresource)
    - [`ScriptPalette`](Scripting.md#scriptpalette)
  - 列挙型: [`ScriptLanguage`](Scripting.md#scriptlanguage)
- **[UIAutomation](UIAutomation.md)** — ユーザーインターフェイスの操作: ツールとアクティブ化、ツールバー（モードバー）、ツール入力、メニューコマンドとチャンクメニュー、オブジェクト情報パレットのコントロール。
  - クラス:
    - [`Point3D`](UIAutomation.md#point3d)
    - [`ViewPoint`](UIAutomation.md#viewpoint)
    - [`ViewSize`](UIAutomation.md#viewsize)
    - [`ToolPoint`](UIAutomation.md#toolpoint)
    - [`ModeButtonDefinition`](UIAutomation.md#modebuttondefinition)
    - [`Tool`](UIAutomation.md#tool)
    - [`ModeChoice`](UIAutomation.md#modechoice)
    - [`ToolMode`](UIAutomation.md#toolmode)
    - [`ModeSetting`](UIAutomation.md#modesetting)
    - [`ModeBar`](UIAutomation.md#modebar)
    - [`ToolControl`](UIAutomation.md#toolcontrol)
    - [`ToolAccess`](UIAutomation.md#toolaccess)
    - [`MenuCommand`](UIAutomation.md#menucommand)
    - [`MenuChunkItem`](UIAutomation.md#menuchunkitem)
    - [`MenuEntry`](UIAutomation.md#menuentry)
    - [`MenuAccess`](UIAutomation.md#menuaccess)
    - [`OIPControl`](UIAutomation.md#oipcontrol)
    - [`OIPSetting`](UIAutomation.md#oipsetting)
    - [`OIPAccess`](UIAutomation.md#oipaccess)
  - 列挙型: [`ToolKind`](UIAutomation.md#toolkind) · [`ToolCreationType`](UIAutomation.md#toolcreationtype) · [`ToolFilter`](UIAutomation.md#toolfilter) · [`ModeType`](UIAutomation.md#modetype) · [`ModeButtonKind`](UIAutomation.md#modebuttonkind) · [`ToolKey`](UIAutomation.md#toolkey) · [`MenuCommandKind`](UIAutomation.md#menucommandkind) · [`MenuChunkKind`](UIAutomation.md#menuchunkkind) · [`MenuFilter`](UIAutomation.md#menufilter) · [`MenuEntryType`](UIAutomation.md#menuentrytype) · [`MenuStatus`](UIAutomation.md#menustatus) · [`OIPPane`](UIAutomation.md#oippane) · [`OIPControlType`](UIAutomation.md#oipcontroltype)
- **[UILayoutCreate](UILayoutCreate.md)** — アラートと質問、既成の値入力ダイアログ、コントロールを組み合わせて作るモーダルダイアログ。
  - クラス:
    - [`DialogEvent`](UILayoutCreate.md#dialogevent)
    - [`ListBrowserEvent`](UILayoutCreate.md#listbrowserevent)
    - [`DialogSize`](UILayoutCreate.md#dialogsize)
    - [`Alerts`](UILayoutCreate.md#alerts)
    - [`TextPair`](UILayoutCreate.md#textpair)
    - [`StandardDialogs`](UILayoutCreate.md#standarddialogs)
    - [`LayoutDialog`](UILayoutCreate.md#layoutdialog)
  - 列挙型: [`DialogResult`](UILayoutCreate.md#dialogresult) · [`AlertButton`](UILayoutCreate.md#alertbutton) · [`EditRealType`](UILayoutCreate.md#editrealtype) · [`StaticTextStyle`](UILayoutCreate.md#statictextstyle) · [`CheckState`](UILayoutCreate.md#checkstate) · [`DialogEventType`](UILayoutCreate.md#dialogeventtype) · [`ListBrowserControlType`](UILayoutCreate.md#listbrowsercontroltype) · [`ListBrowserDisplayType`](UILayoutCreate.md#listbrowserdisplaytype) · [`ListBrowserEventType`](UILayoutCreate.md#listbrowsereventtype)

<a id="index-az"></a>

## A-Z索引

[A](#index-a) · [B](#index-b) · [C](#index-c) · [D](#index-d) · [E](#index-e) · [F](#index-f) · [G](#index-g) · [H](#index-h) · [I](#index-i) · [L](#index-l) · [M](#index-m) · [N](#index-n) · [O](#index-o) · [P](#index-p) · [R](#index-r) · [S](#index-s) · [T](#index-t) · [U](#index-u) · [V](#index-v) · [W](#index-w)

<a id="index-a"></a>

### 索引 A

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`AlertButton`](UILayoutCreate.md#alertbutton) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | 質問アラートのデフォルトボタン。 |
| [`Alerts`](UILayoutCreate.md#alerts) | クラス | [UILayoutCreate](UILayoutCreate.md) | Vectorworks標準のアラート：情報、エラー、質問のアラート（静的関数のみ）。 |
| [`AngularDimensionObject`](ObjectsAnnotation.md#angulardimensionobject) | クラス | [ObjectsAnnotation](ObjectsAnnotation.md) | 角度寸法です。頂点で交わる二辺の間の角度を測定します。 |
| [`AngularUnit`](DocumentAccess.md#angularunit) | IntEnum | [DocumentAccess](DocumentAccess.md) | 角度の表示単位（`UnitSettings.GetAngularUnit`）。 |
| [`AnnotationObject`](ObjectsAnnotation.md#annotationobject) | クラス | [ObjectsAnnotation](ObjectsAnnotation.md) | 注釈プラグインオブジェクトのクラス（データタグ、図面枠）に共通する基底クラスです。 |
| [`Math.Arc2D`](ObjectPrimitives.Math.md#matharc2d) | クラス | [Math](ObjectPrimitives.Math.md) | 円弧。 |
| [`ArchitectObject`](ObjectsArchitect.md#architectobject) | クラス | [ObjectsArchitect](ObjectsArchitect.md) | Architectオブジェクトのクラス（壁、スラブ、屋根、窓、ドア、柱、階段）に共通する基底クラスです。 |
| [`ArcLengthDimensionObject`](ObjectsAnnotation.md#arclengthdimensionobject) | クラス | [ObjectsAnnotation](ObjectsAnnotation.md) | 円弧長寸法：端点間の直線距離ではなく、円弧に沿った長さを計測... |
| [`ArcObject`](ObjectPrimitives.md#arcobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 円弧（`ObjectType.Arc`）。 |
| [`AttributesBase`](Attributes.md#attributesbase) | クラス | [Attributes](Attributes.md) | グラフィック属性クラスの共通基底クラス。 |

<a id="index-b"></a>

### 索引 B

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`BuildingMaterial`](Resources.md#buildingmaterial) | クラス | [Resources](Resources.md) | マテリアル（建材、`ObjectType.BuildingMaterial`）：壁、スラブ、屋根の構成要素の物理的な材料。 |

<a id="index-c"></a>

### 索引 C

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`CenterMarkObject`](ObjectsAnnotation.md#centermarkobject) | クラス | [ObjectsAnnotation](ObjectsAnnotation.md) | センターマークです。円または円弧の中心を示す十字です。 |
| [`CheckState`](UILayoutCreate.md#checkstate) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | 三状態チェックボックス、リストブラウザのセル、またはツリー項目のチェックボックスの状態。 |
| [`Math.Circle2D`](ObjectPrimitives.Math.md#mathcircle2d) | クラス | [Math](ObjectPrimitives.Math.md) | 円。 |
| [`CircleObject`](ObjectPrimitives.md#circleobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 円。 |
| [`ClassAttributes`](Attributes.md#classattributes) | クラス | [Attributes](Attributes.md) | クラス定義（`ObjectType.ClassDefinition`）：名前を付けて保存した属性設定。 |
| [`ClassVisibility`](Attributes.md#classvisibility) | IntEnum | [Attributes](Attributes.md) | クラス |
| [`ColorPair`](Attributes.md#colorpair) | クラス | [Attributes](Attributes.md) | 色インデックスで表した、線または面の前景色と背景色。 |
| [`ColorRGB`](Attributes.md#colorrgb) | クラス | [Attributes](Attributes.md) | チャンネルあたり16ビットのRGB色（0 .. |
| [`ColumnObject`](ObjectsArchitect.md#columnobject) | クラス | [ObjectsArchitect](ObjectsArchitect.md) | 柱プラグインオブジェクトです。Vectorworksの柱で、ユニバーサル名は"Column2"です。 |
| [`ConeObject`](Objects3D.md#coneobject) | クラス | [Objects3D](Objects3D.md) | 標準の円錐ソリッド。 |
| [`ConeObject.Radii`](Objects3D.md#coneobjectradii) | クラス (入れ子) | [Objects3D](Objects3D.md) | ローカルI軸とJ軸に沿った底面の半径。 |
| [`ConnectCADDeviceObject`](ObjectsConnectCAD.md#connectcaddeviceobject) | クラス | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCADの配線略図のDevice（ユニバーサル名は"Device"）です。プロファイルグループ内にSocketを持つ、名前付きのボックスです。 |
| [`ConnectCADDeviceObject.AddSocketResult`](ObjectsConnectCAD.md#connectcaddeviceobjectaddsocketresult) | クラス (入れ子) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | AddSocketの結果です。Socket（追加されなかった場合はnull）とエラーを含みます。 |
| [`ConnectCADDeviceObject.CreateResult`](ObjectsConnectCAD.md#connectcaddeviceobjectcreateresult) | クラス (入れ子) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | CreateFromJSONの結果です。Device（作成されなかった場合はnull）、エラー、警告を含みます。 |
| [`ConnectCADDeviceObject.DeviceTypeResult`](ObjectsConnectCAD.md#connectcaddeviceobjectdevicetyperesult) | クラス (入れ子) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | CreateDeviceTypeの結果：Device Typeのシンボル定義、新規作成かどうか、完全なデータが... |
| [`ConnectCADLibrary`](ObjectsConnectCAD.md#connectcadlibrary) | クラス | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Device間で共有するConnectCADデータ：Signal/Connector Type、Device記述データの検証... |
| [`ConnectCADLibrary.Connector`](ObjectsConnectCAD.md#connectcadlibraryconnector) | クラス (入れ子) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCADのConnector Typeです。 |
| [`ConnectCADLibrary.DeviceDefinition`](ObjectsConnectCAD.md#connectcadlibrarydevicedefinition) | クラス (入れ子) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Device Typeのシンボル定義のDevice Definitionレコードです。 |
| [`ConnectCADLibrary.Signal`](ObjectsConnectCAD.md#connectcadlibrarysignal) | クラス (入れ子) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | カテゴリと優先Connectorを含むConnectCADのSignal Typeです。 |
| [`ConnectCADLibrary.Validation`](ObjectsConnectCAD.md#connectcadlibraryvalidation) | クラス (入れ子) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ValidateDeviceの結果です。エラー（Deviceが不正になる）と警告（Device Typeにのみ保持されるデータ）を含みます。 |
| [`ConnectCADSocketObject`](ObjectsConnectCAD.md#connectcadsocketobject) | クラス | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCADのSocket（ユニバーサル名 "Socket"）：配線略図のDevice内にある接続点... |
| [`ContentFolder`](Resources.md#contentfolder) | IntEnum | [Resources](Resources.md) | 外部（ライブラリ／デフォルト）リソースを格納するVectorworksの標準コンテンツフォルダ。 |
| [`CornerDiameters`](ObjectPrimitives.md#cornerdiameters) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 角丸四角形の角の丸め：幅方向（alongWidth）などの角の楕円の直径... |

<a id="index-d"></a>

### 索引 D

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`DataTagObject`](ObjectsAnnotation.md#datatagobject) | クラス | [ObjectsAnnotation](ObjectsAnnotation.md) | データタグプラグインオブジェクトです（ユニバーサル名は"Data Tag"）。 |
| [`DataTagObject.HorizontalPosition`](ObjectsAnnotation.md#datatagobjecthorizontalposition) | IntEnum (入れ子) | [ObjectsAnnotation](ObjectsAnnotation.md) | タグのテキストを引出線のどちら側に配置するかを指定します（"Horizontal Position"）。 |
| [`DataTagObject.LeaderType`](ObjectsAnnotation.md#datatagobjectleadertype) | IntEnum (入れ子) | [ObjectsAnnotation](ObjectsAnnotation.md) | データタグの引出線の種類です（"Leader Type"）。 |
| [`DataTagObject.MoveBehaviour`](ObjectsAnnotation.md#datatagobjectmovebehaviour) | IntEnum (入れ子) | [ObjectsAnnotation](ObjectsAnnotation.md) | 図面でタグをドラッグした際に移動する対象です。タグ全体、または引出線の先端のみを移動します。 |
| [`DataVisualization`](Resources.md#datavisualization) | クラス | [Resources](Resources.md) | データの可視化（`ObjectType.DataVisualization`）：グラフィック属性を上書きする規則... |
| [`DefaultAttributes`](DocumentAccess.md#defaultattributes) | クラス | [DocumentAccess](DocumentAccess.md) | 新しいオブジェクトのデフォルト属性（何も選択していないときの属性パレット）。 |
| [`Descend`](DocumentAccess.md#descend) | IntFlag | [DocumentAccess](DocumentAccess.md) | コンテナオブジェクト（グループ、シンボル、ビューポートなど）の内部をどの深さまで走査するか。 |
| [`DialogEvent`](UILayoutCreate.md#dialogevent) | クラス | [UILayoutCreate](UILayoutCreate.md) | レイアウトダイアログのハンドラーに渡される一つのイベント。 |
| [`DialogEventType`](UILayoutCreate.md#dialogeventtype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | ダイアログイベントの種類（DialogEventを参照）。 |
| [`DialogResult`](UILayoutCreate.md#dialogresult) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | ダイアログまたはアラートが閉じられた方法。 |
| [`DialogSize`](UILayoutCreate.md#dialogsize) | クラス | [UILayoutCreate](UILayoutCreate.md) | ダイアログのサイズ。ピクセル単位。 |
| [`DimensionKind`](ObjectsAnnotation.md#dimensionkind) | IntEnum | [ObjectsAnnotation](ObjectsAnnotation.md) | オブジェクトの寸法の種類です。 |
| [`DimensionObject`](ObjectsAnnotation.md#dimensionobject) | クラス | [ObjectsAnnotation](ObjectsAnnotation.md) | すべての寸法線オブジェクトの基底クラスです（`ObjectType.Dimension`）。 |
| [`DimensionTolerance`](ObjectsAnnotation.md#dimensiontolerance) | IntEnum | [ObjectsAnnotation](ObjectsAnnotation.md) | 寸法の公称値からのずれの量です。測定値の隣に表示されます。 |
| [`DisplaySettings`](DocumentAccess.md#displaysettings) | クラス | [DocumentAccess](DocumentAccess.md) | 表示設定。 |
| [`Document`](DocumentAccess.md#document) | クラス | [DocumentAccess](DocumentAccess.md) | アクティブなVectorworksファイルに対する状態を保持しないファサード。 |
| [`DoorObject`](ObjectsArchitect.md#doorobject) | クラス | [ObjectsArchitect](ObjectsArchitect.md) | Architectural Objectsプラグインのドアプラグインオブジェクトです（ユニバーサル名は"Door"）。 |
| [`DropShadow`](Attributes.md#dropshadow) | クラス | [Attributes](Attributes.md) | オブジェクト、クラス、ファイルのドロップシャドウ設定：オン/オフ、単位、オフセット、ぼかし半径、角度、色... |
| [`DropShadowAttributes`](Attributes.md#dropshadowattributes) | クラス | [Attributes](Attributes.md) | オブジェクトのドロップシャドウ。 |
| [`DropShadowUnits`](Attributes.md#dropshadowunits) | IntEnum | [Attributes](Attributes.md) | ドロップシャドウ |

<a id="index-e"></a>

### 索引 E

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`EditingSettings`](DocumentAccess.md#editingsettings) | クラス | [DocumentAccess](DocumentAccess.md) | 編集とセッションの設定。 |
| [`EditRealType`](UILayoutCreate.md#editrealtype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | 実数編集フィールドに表示する値の種類。 |
| [`ExistingTreeObject`](ObjectsLandmark.md#existingtreeobject) | クラス | [ObjectsLandmark](ObjectsLandmark.md) | Landmarkプラグインの既存樹木プラグインオブジェクトです（ユニバーサル名は"Existing Tree"）。 |
| [`ExistingTreeObject.Action`](ObjectsLandmark.md#existingtreeobjectaction) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 既存樹木に対する計画措置。 |
| [`ExistingTreeObject.Condition`](ObjectsLandmark.md#existingtreeobjectcondition) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 樹木医による評価 |
| [`ExistingTreeObject.Origin`](ObjectsLandmark.md#existingtreeobjectorigin) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 既存樹木の樹種の原産区分。 |
| [`ExistingTreeObject.Significance`](ObjectsLandmark.md#existingtreeobjectsignificance) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 既存樹木の重要度評価。 |
| [`ExistingTreeObject.SULE`](ObjectsLandmark.md#existingtreeobjectsule) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 安全に利用できる予測余命 |
| [`ExistingTreeObject.TreeProtection`](ObjectsLandmark.md#existingtreeobjecttreeprotection) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 樹木保護範囲の表示 |
| [`ExtrudeObject`](Objects3D.md#extrudeobject) | クラス | [Objects3D](Objects3D.md) | 標準の押し出し（プラグインオブジェクトではない）。 |
| [`ExtrudeObject.Transform`](Objects3D.md#extrudeobjecttransform) | クラス (入れ子) | [Objects3D](Objects3D.md) | 親座標系における正規直交ローカル軸と原点（デフォルトは恒等変換）。 |
| [`ExtrudeObject.Values`](Objects3D.md#extrudeobjectvalues) | クラス (入れ子) | [Objects3D](Objects3D.md) | ワールド単位での、ローカルの底面の高さと符号付きの厚さ。 |

<a id="index-f"></a>

### 索引 F

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`FillAttributes`](Attributes.md#fillattributes) | クラス | [Attributes](Attributes.md) | オブジェクトの面属性：色、スタイル（模様 / ハッチング / タイル / グラデーション / イメージ）、不透明度、クラス別設定... |
| [`FillMappingAttributes`](Attributes.md#fillmappingattributes) | クラス | [Attributes](Attributes.md) | ハッチング、タイル、グラデーション、イメージの面のマッピング（面の座標系）：原点、軸、オフセット、回転、繰り返し... |
| [`FillMappingAttributes.Frame`](Attributes.md#fillmappingattributesframe) | クラス (入れ子) | [Attributes](Attributes.md) | ハッチング、タイル、グラデーション、イメージの面のマッピングフレーム：原点とI軸およびJ軸の終点。 |
| [`FillType`](Attributes.md#filltype) | IntEnum | [Attributes](Attributes.md) | オブジェクトの面の種類。 |

<a id="index-g"></a>

### 索引 G

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`GDTFLibrary`](ObjectsSpotlight.md#gdtflibrary) | クラス | [ObjectsSpotlight](ObjectsSpotlight.md) | Spotlightが認識するGDTF器具タイプ（General Device Type Format、DIN SPEC 15800）です。 |
| [`GDTFLibrary.Entry`](ObjectsSpotlight.md#gdtflibraryentry) | クラス (入れ子) | [ObjectsSpotlight](ObjectsSpotlight.md) | 利用可能な器具タイプの一つのDMXモード。 |
| [`GDTFLibrary.ImportResult`](ObjectsSpotlight.md#gdtflibraryimportresult) | クラス (入れ子) | [ObjectsSpotlight](ObjectsSpotlight.md) | Importの結果：GDTFのシンボル定義、GDTF名、この呼び出しで取り込んだかどうか、および... |
| [`GenericSolidObject`](Objects3D.md#genericsolidobject) | クラス | [Objects3D](Objects3D.md) | 噛み合わせるコマンド、削り取るコマンド、重なった部分を残すコマンドで作成した図形と、履歴のない汎用ソリッドを含む、標準のソリッド図形を扱います。 |
| [`GenericSolidObject.HistoryStep`](Objects3D.md#genericsolidobjecthistorystep) | クラス (入れ子) | [Objects3D](Objects3D.md) | 標準の構築ツリーの一つのノードを、先行順で扱います。 |
| [`GenericSolidObject.Operation`](Objects3D.md#genericsolidobjectoperation) | IntEnum (入れ子) | [Objects3D](Objects3D.md) | ソリッドのブール演算。 |
| [`Gradient`](Resources.md#gradient) | クラス | [Resources](Resources.md) | グラデーションによる面（`ObjectType.GradientDefinition`）：二つ以上の変化点間の混合。 |
| [`GradientSegment`](Resources.md#gradientsegment) | クラス | [Resources](Resources.md) | グラデーションの一つの変化点。 |
| [`GridSettings`](DocumentAccess.md#gridsettings) | クラス | [DocumentAccess](DocumentAccess.md) | グリッド設定。 |
| [`GroupObject`](ObjectPrimitives.md#groupobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | グループ（`ObjectType.Group`）：他のオブジェクトを格納するコンテナ。 |

<a id="index-h"></a>

### 索引 H

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`HardscapeObject`](ObjectsLandmark.md#hardscapeobject) | クラス | [ObjectsLandmark](ObjectsLandmark.md) | Landmarkプラグインの舗床プラグインオブジェクトです（ユニバーサル名は"Hardscape"）。 |
| [`HardscapeObject.Mode3D`](ObjectsLandmark.md#hardscapeobjectmode3d) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 舗床の3Dモード。 |
| [`Hatch`](Resources.md#hatch) | クラス | [Resources](Resources.md) | ベクターハッチングによる面（`ObjectType.HatchDefinition`）：塗りつぶす領域全体で繰り返される線群の集合。 |
| [`HatchLevel`](Resources.md#hatchlevel) | クラス | [Resources](Resources.md) | ハッチングの一つの線群。 |
| [`HemisphereObject`](Objects3D.md#hemisphereobject) | クラス | [Objects3D](Objects3D.md) | 半球ソリッド：中心、半径、ローカルK軸方向のドーム。図面オブジェクトの軽量なビュー... |

<a id="index-i"></a>

### 索引 I

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`ImageFill`](Resources.md#imagefill) | クラス | [Resources](Resources.md) | イメージリソース（`ObjectType.ImageDefinition`）：面のイメージ、添景などに使用するビットマップ... |
| [`ImageFill.Compression`](Resources.md#imagefillcompression) | IntEnum (入れ子) | [Resources](Resources.md) | 画像の保存に使用される圧縮方式。 |
| [`ImportConflict`](Resources.md#importconflict) | IntEnum | [Resources](Resources.md) | 現在の図面にリソースを取り込むとき、同じ名前のリソースがある場合の競合の解決方法... |

<a id="index-l"></a>

### 索引 L

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`LandmarkObject`](ObjectsLandmark.md#landmarkobject) | クラス | [ObjectsLandmark](ObjectsLandmark.md) | Landmarkのプラグインオブジェクト（植栽、ランドスケープエリア、地形モデル、造成図形、レベルオブジェクトなど）の共通基底クラス... |
| [`LandscapeAreaObject`](ObjectsLandmark.md#landscapeareaobject) | クラス | [ObjectsLandmark](ObjectsLandmark.md) | Landmarkプラグインのランドスケープエリアプラグインオブジェクトです（ユニバーサル名は"Landscape Area"）。 |
| [`LandscapeAreaObject.AreaUnits`](ObjectsLandmark.md#landscapeareaobjectareaunits) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | ランドスケープエリアの面積の表示単位。 |
| [`LandscapeAreaObject.DrawingMode`](ObjectsLandmark.md#landscapeareaobjectdrawingmode) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | オブジェクトをランドスケープエリアとして描画するか、生け垣として描画するか。 |
| [`LandscapeAreaObject.PlantDisplay2D`](ObjectsLandmark.md#landscapeareaobjectplantdisplay2d) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | ランドスケープエリアの植栽の2D表示方法。 |
| [`Layer`](DocumentAccess.md#layer) | クラス | [DocumentAccess](DocumentAccess.md) | レイヤ（デザインレイヤまたはシートレイヤ）。 |
| [`LayerContents`](DocumentAccess.md#layercontents) | クラス | [DocumentAccess](DocumentAccess.md) | レイヤの最上位オブジェクトの数と境界。 |
| [`LayerType`](DocumentAccess.md#layertype) | IntEnum | [DocumentAccess](DocumentAccess.md) | レイヤの種類。 |
| [`LayerVisibility`](DocumentAccess.md#layervisibility) | IntEnum | [DocumentAccess](DocumentAccess.md) | レイヤの表示状態（ナビゲーションパレットに表示されるもの）。 |
| [`LayoutDialog`](UILayoutCreate.md#layoutdialog) | クラス | [UILayoutCreate](UILayoutCreate.md) | コードでコントロールを一つずつ配置して構築する、モーダルなレイアウトマネージャダイアログ。 |
| [`LightingDeviceObject`](ObjectsSpotlight.md#lightingdeviceobject) | クラス | [ObjectsSpotlight](ObjectsSpotlight.md) | SpotlightプラグインのLighting Deviceプラグインオブジェクトです（ユニバーサル名は"Lighting Device"）。 |
| [`Math.Line2D`](ObjectPrimitives.Math.md#mathline2d) | クラス | [Math](ObjectPrimitives.Math.md) | `start`から`end`への線分。 |
| [`Math.Line2D.Intersection`](ObjectPrimitives.Math.md#mathline2dintersection) | クラス (入れ子) | [Math](ObjectPrimitives.Math.md) | 無限直線同士の交点。 |
| [`Line2DObject`](ObjectPrimitives.md#line2dobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 2D直線（`ObjectType.Line`）：二点間の直線の線分。 |
| [`Math.Line3D`](ObjectPrimitives.Math.md#mathline3d) | クラス | [Math](ObjectPrimitives.Math.md) | Pythonが所有する、ワールド座標のミリメートル単位のstartからendへの3D線分。 |
| [`LinearDimensionObject`](ObjectsAnnotation.md#lineardimensionobject) | クラス | [ObjectsAnnotation](ObjectsAnnotation.md) | 長さ寸法です。二点間の距離を測定します。 |
| [`LineType`](Resources.md#linetype) | クラス | [Resources](Resources.md) | ラインタイプリソース。 |
| [`ListBrowserControlType`](UILayoutCreate.md#listbrowsercontroltype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | リストブラウザの列の動作。 |
| [`ListBrowserDisplayType`](UILayoutCreate.md#listbrowserdisplaytype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | リストブラウザの列に表示する内容。 |
| [`ListBrowserEvent`](UILayoutCreate.md#listbrowserevent) | クラス | [UILayoutCreate](UILayoutCreate.md) | 最後のリストブラウザイベントの詳細。 |
| [`ListBrowserEventType`](UILayoutCreate.md#listbrowsereventtype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | リストブラウザで発生した内容（`LayoutDialog.GetListBrowserEvent`を参照）。 |
| [`Locus2DObject`](ObjectPrimitives.md#locus2dobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 2D 基準点（`ObjectType.Locus`）：参照用の点。 |

<a id="index-m"></a>

### 索引 M

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`Marker`](Attributes.md#marker) | クラス | [Attributes](Attributes.md) | 線の始点または終点のマーカー（矢印先端）：形状、面、底辺、半欠け、反転、角度（度）など... |
| [`MarkerAttributes`](Attributes.md#markerattributes) | クラス | [Attributes](Attributes.md) | オブジェクトの始点と終点のマーカー（矢印先端）。 |
| [`MarkerBase`](Attributes.md#markerbase) | IntEnum | [Attributes](Attributes.md) | マーカーの底辺の形状（シフト済みのビット値。`Marker.GetStyleValue`を参照）。 |
| [`MarkerFill`](Attributes.md#markerfill) | IntEnum | [Attributes](Attributes.md) | 以下のマーカースタイル列挙型（MarkerFill、MarkerBase、MarkerHalfTick）は、あらかじめビットシフトした値を使用... |
| [`MarkerHalfTick`](Attributes.md#markerhalftick) | IntEnum | [Attributes](Attributes.md) | マーカー全体、またはその左半分か右半分のみ（シフト済みのビット値。`Marker.GetStyleValue`を参照）。 |
| [`MarkerShape`](Attributes.md#markershape) | IntEnum | [Attributes](Attributes.md) | マーカー（矢印先端） |
| [`MarkerThicknessBasis`](Attributes.md#markerthicknessbasis) | IntEnum | [Attributes](Attributes.md) | マーカーの線の太さが従う基準。 |
| [`MarkerThicknessUnits`](Attributes.md#markerthicknessunits) | IntEnum | [Attributes](Attributes.md) | カスタムマーカーの線の太さの単位。 |
| [`MenuAccess`](UIAutomation.md#menuaccess) | クラス | [UIAutomation](UIAutomation.md) | Vectorworksのメニューシステムに対する、状態を保持しないファサード。 |
| [`MenuChunkItem`](UIAutomation.md#menuchunkitem) | クラス | [UIAutomation](UIAutomation.md) | チャンクメニューの現在の一つの項目。 |
| [`MenuChunkKind`](UIAutomation.md#menuchunkkind) | IntEnum | [UIAutomation](UIAutomation.md) | チャンクメニューの種類（上記の「チャンクメニュー」を参照）。 |
| [`MenuCommand`](UIAutomation.md#menucommand) | クラス | [UIAutomation](UIAutomation.md) | インストールされている一つのメニューコマンドの説明。 |
| [`MenuCommandKind`](UIAutomation.md#menucommandkind) | IntEnum | [UIAutomation](UIAutomation.md) | メニューコマンドの提供形態。 |
| [`MenuEntry`](UIAutomation.md#menuentry) | クラス | [UIAutomation](UIAutomation.md) | 現在の作業画面で定義された、メニューバーのメニュー内の一つのエントリ。 |
| [`MenuEntryType`](UIAutomation.md#menuentrytype) | IntEnum | [UIAutomation](UIAutomation.md) | メニューバーのメニュー内のエントリの種類。 |
| [`MenuFilter`](UIAutomation.md#menufilter) | IntEnum | [UIAutomation](UIAutomation.md) | `MenuAccess.GetMenuCommands`が返すメニューコマンドの範囲。 |
| [`MenuStatus`](UIAutomation.md#menustatus) | IntEnum | [UIAutomation](UIAutomation.md) | メニューコマンド（またはチャンクメニュー項目）を現在実行できるかどうか、および実行できない理由（`MenuAccess.GetMenuStatus`を参照）。 |
| [`MeshObject`](Objects3D.md#meshobject) | クラス | [Objects3D](Objects3D.md) | 標準のメッシュ（`ObjectType.Mesh`）：共有頂点リストと、そのインデックスを参照する多角形の面。 |
| [`MeshObject.Face`](Objects3D.md#meshobjectface) | クラス (入れ子) | [Objects3D](Objects3D.md) | part 0は全体の（テクスチャなしの）パートを意味します。`GetOverallPart()`を参照してください。 |
| [`MeshObject.Part`](Objects3D.md#meshobjectpart) | クラス (入れ子) | [Objects3D](Objects3D.md) | テクスチャパート：id、テクスチャ参照（0 = テクスチャなし）、およびそれを使用する面の数。 |
| [`MeshObject.Smoothing`](Objects3D.md#meshobjectsmoothing) | IntEnum (入れ子) | [Objects3D](Objects3D.md) | レンダリング時のメッシュのスムージング方法。 |
| [`ModeBar`](UIAutomation.md#modebar) | クラス | [UIAutomation](UIAutomation.md) | アクティブなツールのツールバー（モードバー）に対する、状態を保持しないビュー。 |
| [`ModeButtonDefinition`](UIAutomation.md#modebuttondefinition) | クラス | [UIAutomation](UIAutomation.md) | ツールが宣言するツールバーボタン（モードボタン。静的な情報で、ツールをアクティブにせずに取得可能）。 |
| [`ModeButtonKind`](UIAutomation.md#modebuttonkind) | IntEnum | [UIAutomation](UIAutomation.md) | ツールの登録時に宣言されたツールバーボタンの種類（現在のModeTypeとは異なる場合があります）。 |
| [`ModeChoice`](UIAutomation.md#modechoice) | クラス | [UIAutomation](UIAutomation.md) | ツールバーボタンのグループ（モードグループ）の1つの選択肢：ラジオボタン、Button/Toggleグループの単一ボタン、または項目... |
| [`ModeSetting`](UIAutomation.md#modesetting) | クラス | [UIAutomation](UIAutomation.md) | 汎用のテキストベースのモードAPIが使用するモード変更要求（`ModeBar.SetMode`を参照）。 |
| [`ModeType`](UIAutomation.md#modetype) | IntEnum | [UIAutomation](UIAutomation.md) | アクティブなツールのツールバーボタンのグループの種類。 |
| [`MultiExtrudeObject`](Objects3D.md#multiextrudeobject) | クラス | [Objects3D](Objects3D.md) | 標準の多段押し出し。 |

<a id="index-n"></a>

### 索引 N

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`NurbsCurveObject`](Objects3D.md#nurbscurveobject) | クラス | [Objects3D](Objects3D.md) | 標準の区分的なNURBS曲線。 |
| [`NurbsCurveObject.Location`](Objects3D.md#nurbscurveobjectlocation) | クラス (入れ子) | [Objects3D](Objects3D.md) | ゼロ始まりの区間における曲線上の点と固有のパラメータ。パラメータは弧長ではありません。 |
| [`NurbsSurfaceObject`](Objects3D.md#nurbssurfaceobject) | クラス | [Objects3D](Objects3D.md) | 標準のNURBS曲面。 |

<a id="index-o"></a>

### 索引 O

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`ObjectAttributes`](Attributes.md#objectattributes) | クラス | [Attributes](Attributes.md) | オブジェクトのすべてのグラフィック属性。 |
| [`ObjectColors`](Attributes.md#objectcolors) | クラス | [Attributes](Attributes.md) | 色インデックスで表した、オブジェクトの四つの色すべて（線の前景／背景、面の前景／背景）。 |
| [`ObjectType`](Attributes.md#objecttype) | IntEnum | [Attributes](Attributes.md) | オブジェクトの種類。 |
| [`Math.OffsetJoin`](ObjectPrimitives.Math.md#mathoffsetjoin) | IntEnum | [Math](ObjectPrimitives.Math.md) | 多角形のオフセットのコーナースタイル（`Polygon2D.Offset`）。 |
| [`OIPAccess`](UIAutomation.md#oipaccess) | クラス | [UIAutomation](UIAutomation.md) | オブジェクト情報パレットに対する、状態を保持しないファサード。 |
| [`OIPControl`](UIAutomation.md#oipcontrol) | クラス | [UIAutomation](UIAutomation.md) | オブジェクト情報パレット（OIP）の一つのコントロールの説明と現在の状態。 |
| [`OIPControlType`](UIAutomation.md#oipcontroltype) | IntEnum | [UIAutomation](UIAutomation.md) | オブジェクト情報パレット（OIP）のコントロールの種類。 |
| [`OIPPane`](UIAutomation.md#oippane) | IntEnum | [UIAutomation](UIAutomation.md) | オブジェクト情報パレットのタブ（ペイン）。 |
| [`OIPSetting`](UIAutomation.md#oipsetting) | クラス | [UIAutomation](UIAutomation.md) | 汎用のテキストベースのAPIが使用するコントロール変更要求（`OIPAccess.SetValue`を参照）。 |

<a id="index-p"></a>

### 索引 P

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`ParametricObject`](ObjectPrimitives.md#parametricobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 任意の種類の汎用プラグインオブジェクト（パラメトリックオブジェクト、`ObjectType.Parametric`）。スクリプトなどで定義... |
| [`ParametricObject.PluginKind`](ObjectPrimitives.md#parametricobjectpluginkind) | IntEnum (入れ子) | [ObjectPrimitives](ObjectPrimitives.md) | プラグインのオブジェクトの配置方法：プラグインが宣言するオブジェクトのサブタイプ。 |
| [`PenAttributes`](Attributes.md#penattributes) | クラス | [Attributes](Attributes.md) | オブジェクトの線属性：色、スタイル（模様 / ラインタイプ）、線の太さ、不透明度、クラス別設定... |
| [`PenStyleKind`](Attributes.md#penstylekind) | IntEnum | [Attributes](Attributes.md) | 未加工の線スタイル値の分類。 |
| [`Math.Plane3D`](ObjectPrimitives.Math.md#mathplane3d) | クラス | [Math](ObjectPrimitives.Math.md) | Pythonが所有する、単位法線を持つ向き付きの無限平面。 |
| [`PlantObject`](ObjectsLandmark.md#plantobject) | クラス | [ObjectsLandmark](ObjectsLandmark.md) | Landmarkプラグインの植栽プラグインオブジェクトです（ユニバーサル名は"Plant"）。 |
| [`PlantObject.Config`](ObjectsLandmark.md#plantobjectconfig) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 構成と表示 |
| [`PlantObject.TagDisplay`](ObjectsLandmark.md#plantobjecttagdisplay) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 植栽ラベルの表示位置。 |
| [`Math.Point2D`](ObjectPrimitives.Math.md#mathpoint2d) | クラス | [Math](ObjectPrimitives.Math.md) | 2D点／ベクトル。 |
| [`Point2D`](Attributes.md#point2d) | クラス | [Attributes](Attributes.md) | ダイアログと属性のAPIで使用する単純な2D点レコード（`x`、`y`はワールド単位）。 |
| [`Math.Point3D`](ObjectPrimitives.Math.md#mathpoint3d) | クラス | [Math](ObjectPrimitives.Math.md) | Pythonが所有する、ワールド座標のミリメートル単位の3D点／ベクトル。 |
| [`Point3D`](UIAutomation.md#point3d) | クラス | [UIAutomation](UIAutomation.md) | ワールド座標の3D点。 |
| [`Math.Polygon2D`](ObjectPrimitives.Math.md#mathpolygon2d) | クラス | [Math](ObjectPrimitives.Math.md) | 多角形または曲線の頂点リスト。 |
| [`Math.Polygon2D.CurveLocation`](ObjectPrimitives.Math.md#mathpolygon2dcurvelocation) | クラス (入れ子) | [Math](ObjectPrimitives.Math.md) | 多角形の曲線状の外側パスを一時的にNURBSで表現したときの、点と区間固有のパラメータ。 |
| [`Polygon3DObject`](Objects3D.md#polygon3dobject) | クラス | [Objects3D](Objects3D.md) | 標準の3D 多角形（`ObjectType.Polygon3D`）。 |
| [`Polygon3DObject.ClosestPoint`](Objects3D.md#polygon3dobjectclosestpoint) | クラス (入れ子) | [Objects3D](Objects3D.md) | 多角形パス上の最近点、その距離、辺のインデックス、および最初の頂点からのパス距離。 |
| [`Polygon3DObject.Plane`](Objects3D.md#polygon3dobjectplane) | クラス (入れ子) | [Objects3D](Objects3D.md) | 頂点の重心を通る平面。法線は頂点順（右手の法則）に従う単位ベクトルで、dは... |
| [`PolygonObject`](ObjectPrimitives.md#polygonobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 多角形（`ObjectType.Polygon`、およびフリーハンド`ObjectType.FreehandPolygon`）：頂点はコーナー頂点のみ。 |
| [`PolylineObject`](ObjectPrimitives.md#polylineobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 曲線（`ObjectType.Polyline`）：角、ベジェ、キュービック、円弧、半径などの頂点を持つ図形... |
| [`PolyObject`](ObjectPrimitives.md#polyobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 多角形クラスと曲線クラスの共通基底クラス。 |
| [`PolyObject.BooleanOperation`](ObjectPrimitives.md#polyobjectbooleanoperation) | IntEnum (入れ子) | [ObjectPrimitives](ObjectPrimitives.md) | 2Dブール関数の演算 |
| [`Math.PolyVertex`](ObjectPrimitives.Math.md#mathpolyvertex) | クラス | [Math](ObjectPrimitives.Math.md) | `Polygon2D` の1頂点：点、頂点タイプ、円弧半径（半径頂点）、表示状態... |
| [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | APIのすべてのオブジェクトクラスの共通基底クラス（2Dプリミティブと、その派生クラスである3D、注釈など）... |
| [`PrimitiveObject.Bounds3D`](ObjectPrimitives.md#primitiveobjectbounds3d) | クラス (入れ子) | [ObjectPrimitives](ObjectPrimitives.md) | ワールド単位の、座標軸に平行な3Dバウンディングボックス |
| [`ProgramVariables`](DocumentAccess.md#programvariables) | クラス | [DocumentAccess](DocumentAccess.md) | 任意のVectorworksプログラム変数（アプリケーション全体またはファイルごとの設定）への、型付きの低水準アクセス... |
| [`PropertyLineObject`](ObjectsLandmark.md#propertylineobject) | クラス | [ObjectsLandmark](ObjectsLandmark.md) | Landmarkプラグインの境界線プラグインオブジェクトです（ユニバーサル名は"Property Line"）。 |
| [`PropertyLineObject.AreaUnits`](ObjectsLandmark.md#propertylineobjectareaunits) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | "Area Units Imperial"と"Area Units Metric"の両方のパラメータが対応する面積単位の選択肢。 |

<a id="index-r"></a>

### 索引 R

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`RadialDimensionObject`](ObjectsAnnotation.md#radialdimensionobject) | クラス | [ObjectsAnnotation](ObjectsAnnotation.md) | 半径寸法および直径寸法です。円または円弧の半径または直径を測定します。 |
| [`RecordField`](Resources.md#recordfield) | クラス | [Resources](Resources.md) | レコードフォーマットの一つのフィールド。 |
| [`RecordFieldType`](Resources.md#recordfieldtype) | IntEnum | [Resources](Resources.md) | レコードフィールドのデータ型。 |
| [`RecordFormat`](Resources.md#recordformat) | クラス | [Resources](Resources.md) | レコードフォーマット。 |
| [`Math.Rect2D`](ObjectPrimitives.Math.md#mathrect2d) | クラス | [Math](ObjectPrimitives.Math.md) | 座標軸に平行な矩形。 |
| [`RectangleObject`](ObjectPrimitives.md#rectangleobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 四角形（`ObjectType.Box`）。回転している場合もあります。 |
| [`RectangularObject`](ObjectPrimitives.md#rectangularobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 四角形クラスと角丸四角形クラスの共通基底クラス。 |
| [`RenderBackground`](Resources.md#renderbackground) | クラス | [Resources](Resources.md) | 背景テクスチャ（`ObjectType.RenderBackground`）：レンダリング時にモデルの背後に表示するもの。 |
| [`RenderBackground.Kind`](Resources.md#renderbackgroundkind) | IntEnum (入れ子) | [Resources](Resources.md) | 新しいリソースを作成するときの背景の種類。 |
| [`RenderStyle`](Resources.md#renderstyle) | クラス | [Resources](Resources.md) | レンダリングスタイル（`ObjectType.RenderStyle`）：保存されたレンダリング設定。適用先は... |
| [`Resource`](Resources.md#resource) | クラス | [Resources](Resources.md) | ハンドルで識別される一つのリソース。 |
| [`ResourceFolder`](Resources.md#resourcefolder) | クラス | [Resources](Resources.md) | リソースフォルダ（`ObjectType.Folder`）：リソースマネージャで一種類のリソースをまとめます。 |
| [`ResourceFolderPath`](Resources.md#resourcefolderpath) | クラス | [Resources](Resources.md) | `ResourceFolder.CreatePathFolders` が構成したパスのフォルダ：パス内の全フォルダと、この呼び出しで... |
| [`ResourceList`](Resources.md#resourcelist) | クラス | [Resources](Resources.md) | 現在の図面または外部コンテンツにある、一種類のリソースのリスト。 |
| [`ResourceList.Entry`](Resources.md#resourcelistentry) | クラス (入れ子) | [Resources](Resources.md) | リストの一つのエントリ。 |
| [`ResourceList.ImportResult`](Resources.md#resourcelistimportresult) | クラス (入れ子) | [Resources](Resources.md) | ImportWithResultの結果：図面内のリソースと、この呼び出しでコピーしたかどうか（`False` となるのは...） |
| [`ResourceType`](Resources.md#resourcetype) | IntEnum | [Resources](Resources.md) | リソースの種類。 |
| [`RoofObject`](ObjectsArchitect.md#roofobject) | クラス | [ObjectsArchitect](ObjectsArchitect.md) | 屋根（`ObjectType.RoofContainer`）です。辺のリストで定義する多角形の屋根です。 |
| [`RoofObject.Accessories`](ObjectsArchitect.md#roofobjectaccessories) | クラス (入れ子) | [ObjectsArchitect](ObjectsArchitect.md) | 周囲に沿った屋根の装飾部品。 |
| [`RoofObject.Attributes`](ObjectsArchitect.md#roofobjectattributes) | クラス (入れ子) | [ObjectsArchitect](ObjectsArchitect.md) | 屋根全体の属性。 |
| [`RoofObject.Edge`](ObjectsArchitect.md#roofobjectedge) | クラス (入れ子) | [ObjectsArchitect](ObjectsArchitect.md) | 屋根の辺（多角形の頂点＋辺ごとの勾配と軒の出）です。屋根の輪郭に沿った順序です。 |
| [`RoofObject.MiterType`](ObjectsArchitect.md#roofobjectmitertype) | IntEnum (入れ子) | [ObjectsArchitect](ObjectsArchitect.md) | 屋根端部の形状の種類です（隣接する二つの勾配面の接合方法）。 |
| [`RoofStyle`](Resources.md#roofstyle) | クラス | [Resources](Resources.md) | 屋根スタイル（`ObjectType.RoofStyle`）：屋根の構成要素と属性。 |
| [`RoofTextures`](Attributes.md#rooftextures) | クラス | [Attributes](Attributes.md) | クラスの屋根テクスチャ（テクスチャリソースの内部インデックス、0 = なし）。 |
| [`Math.RotatedRect2D`](ObjectPrimitives.Math.md#mathrotatedrect2d) | クラス | [Math](ObjectPrimitives.Math.md) | 回転可能な矩形：コーナー、幅方向の辺の方向、および二つの辺の長さ。 |
| [`RoundRectObject`](ObjectPrimitives.md#roundrectobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 角丸四角形（`ObjectType.RoundedRectangle`）。回転している場合もあります。 |

<a id="index-s"></a>

### 索引 S

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`ScriptLanguage`](Scripting.md#scriptlanguage) | IntEnum | [Scripting](Scripting.md) | スクリプトの言語。 |
| [`ScriptPalette`](Scripting.md#scriptpalette) | クラス | [Scripting](Scripting.md) | ハンドルで識別される一つのスクリプトパレット。 |
| [`ScriptResource`](Scripting.md#scriptresource) | クラス | [Scripting](Scripting.md) | ハンドルで識別される一つのスクリプトリソース。 |
| [`ShellObject`](Objects3D.md#shellobject) | クラス | [Objects3D](Objects3D.md) | シェルソリッド：CSGオフセットノード（シェルソリッドツール、VectorScriptのCreateShell）。 |
| [`SiteModelObject`](ObjectsLandmark.md#sitemodelobject) | クラス | [ObjectsLandmark](ObjectsLandmark.md) | Landmarkプラグインの地形モデルプラグインオブジェクトです（ユニバーサル名は"DTM6"）。 |
| [`SiteModelObject.Display2D`](ObjectsLandmark.md#sitemodelobjectdisplay2d) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 2D／3D表示の選択 |
| [`SiteModelObject.Display3D`](ObjectsLandmark.md#sitemodelobjectdisplay3d) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 地形モデルの3D表示の内容。 |
| [`SiteModifierObject`](ObjectsLandmark.md#sitemodifierobject) | クラス | [ObjectsLandmark](ObjectsLandmark.md) | Landmarkプラグインの造成図形プラグインオブジェクトです（ユニバーサル名は"Site Modifiers"）。 |
| [`SiteModifierObject.ApplyTo`](ObjectsLandmark.md#sitemodifierobjectapplyto) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 造成図形が適用される地形モデルの面。 |
| [`SiteModifierObject.Config`](ObjectsLandmark.md#sitemodifierobjectconfig) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 造成図形の変形方式です（"Config"）。 |
| [`SlabObject`](ObjectsArchitect.md#slabobject) | クラス | [ObjectsArchitect](ObjectsArchitect.md) | スラブ：2Dの境界断面で定義する水平要素（床、屋根デッキ、天井デッキなど）... |
| [`SlabStyle`](Resources.md#slabstyle) | クラス | [Resources](Resources.md) | スラブスタイル（`ObjectType.SlabStyle`）：スラブの構成要素と属性。 |
| [`SnapSettings`](DocumentAccess.md#snapsettings) | クラス | [DocumentAccess](DocumentAccess.md) | スナップ（スマートカーソル）の設定。 |
| [`SolidPrimitiveObject`](Objects3D.md#solidprimitiveobject) | クラス | [Objects3D](Objects3D.md) | 標準のパラメトリックソリッドプリミティブ（`ObjectType.Solid`）、つまり球、半球、円錐の共通基底クラス。 |
| [`SolidPrimitiveObject.Kind`](Objects3D.md#solidprimitiveobjectkind) | IntEnum (入れ子) | [Objects3D](Objects3D.md) | ソリッドプリミティブの種類。 |
| [`SphereObject`](Objects3D.md#sphereobject) | クラス | [Objects3D](Objects3D.md) | 球ソリッド：中心とI/J/K方向の半径（等しくない場合は楕円体）。図面オブジェクトの軽量なビュー... |
| [`StackLayersSettings`](DocumentAccess.md#stacklayerssettings) | クラス | [DocumentAccess](DocumentAccess.md) | 統合ビュー（スタックレイヤ）の設定。 |
| [`StairObject`](ObjectsArchitect.md#stairobject) | クラス | [ObjectsArchitect](ObjectsArchitect.md) | 階段プラグインオブジェクトです。Vectorworksの階段で、ユニバーサル名は"Stairs CW"です。 |
| [`StakeObject`](ObjectsLandmark.md#stakeobject) | クラス | [ObjectsLandmark](ObjectsLandmark.md) | Landmarkプラグインのレベルオブジェクトプラグインオブジェクトです（ユニバーサル名は"Stake Object"）。 |
| [`StakeObject.Mode`](ObjectsLandmark.md#stakeobjectmode) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | 地形モデルに対するレベルオブジェクトの役割。 |
| [`StakeObject.SiteModel`](ObjectsLandmark.md#stakeobjectsitemodel) | IntEnum (入れ子) | [ObjectsLandmark](ObjectsLandmark.md) | レベルオブジェクトが参照する地形モデルの面。 |
| [`StandardDialogs`](UILayoutCreate.md#standarddialogs) | クラス | [UILayoutCreate](UILayoutCreate.md) | 一つまたは二つの値を編集するか、リストから選択するための既成のダイアログ（静的関数のみ）。 |
| [`StaticTextStyle`](UILayoutCreate.md#statictextstyle) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | 固定テキストのフォントスタイル。 |
| [`Story`](DocumentAccess.md#story) | クラス | [DocumentAccess](DocumentAccess.md) | ストーリ：一定の基準高さにある建物の階。 |
| [`StoryElevationChangeMode`](DocumentAccess.md#storyelevationchangemode) | IntEnum | [DocumentAccess](DocumentAccess.md) | `Story.SetElevation`が移動するストーリ（ストーリの高さ変更ダイアログボックスの選択肢）。 |
| [`StoryLevel`](DocumentAccess.md#storylevel) | クラス | [DocumentAccess](DocumentAccess.md) | ストーリの1つのレベル：ストーリ高さに対する、名前（レベルタイプ）を持つ相対高さ。必要に応じて... |
| [`StoryLevelTemplate`](DocumentAccess.md#storyleveltemplate) | クラス | [DocumentAccess](DocumentAccess.md) | デフォルトのストーリレベル（オーガナイザダイアログボックス > ストーリタブ > ストーリレベル初期設定）：ストーリレベルのテンプレート。 |
| [`SurfaceModelObject`](Objects3D.md#surfacemodelobject) | クラス | [Objects3D](Objects3D.md) | モデリング結果は、NURBS曲面、CSGソリッド、またはモデリング結果のグループです。 |
| [`SurfaceModelObject.PathOptions`](Objects3D.md#surfacemodelobjectpathoptions) | クラス (入れ子) | [Objects3D](Objects3D.md) | パス押し出しの拡大縮小と断面配置のオプション。 |
| [`SweepObject`](Objects3D.md#sweepobject) | クラス | [Objects3D](Objects3D.md) | 標準の回転体。 |
| [`SweepObject.Values`](Objects3D.md#sweepobjectvalues) | クラス (入れ子) | [Objects3D](Objects3D.md) | ラジアンでの回転体の角度と、一周あたりのワールド単位でのピッチ。 |
| [`SymbolDefinition`](Resources.md#symboldefinition) | クラス | [Resources](Resources.md) | シンボル定義。 |
| [`SymbolDefinition.BreakMode`](Resources.md#symboldefinitionbreakmode) | IntEnum (入れ子) | [Resources](Resources.md) | シンボルの挿入箇所で壁を切り欠く方法。 |
| [`SymbolDefinition.GeometryType`](Resources.md#symboldefinitiongeometrytype) | IntEnum (入れ子) | [Resources](Resources.md) | シンボルが描画できるもの：2Dのみ、3Dのみ、または両方（ハイブリッドシンボルは平面ビューで2D部分を表示します）。 |
| [`SymbolDefinition.InsertMode`](Resources.md#symboldefinitioninsertmode) | IntEnum (入れ子) | [Resources](Resources.md) | シンボルを挿入する壁に対する、シンボルの配置位置。 |

<a id="index-t"></a>

### 索引 T

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`TextDefaults`](DocumentAccess.md#textdefaults) | クラス | [DocumentAccess](DocumentAccess.md) | 新しい文字列オブジェクトのデフォルトの文字設定。 |
| [`TextJustification`](DocumentAccess.md#textjustification) | IntEnum | [DocumentAccess](DocumentAccess.md) | 新しい文字の水平方向の揃え（`TextDefaults`）。 |
| [`TextLineSpacing`](DocumentAccess.md#textlinespacing) | IntEnum | [DocumentAccess](DocumentAccess.md) | 新しい文字の行間（`TextDefaults`）。`Custom`は`TextDefaults.GetLeading`の行送りを使用します。 |
| [`TextObject`](ObjectPrimitives.md#textobject) | クラス | [ObjectPrimitives](ObjectPrimitives.md) | 文字列（`ObjectType.Text`）：原点に配置する書式付きの文字列。 |
| [`TextObject.HorizontalAlignment`](ObjectPrimitives.md#textobjecthorizontalalignment) | IntEnum (入れ子) | [ObjectPrimitives](ObjectPrimitives.md) | 文字列の水平方向の配置揃え。 |
| [`TextObject.Spacing`](ObjectPrimitives.md#textobjectspacing) | IntEnum (入れ子) | [ObjectPrimitives](ObjectPrimitives.md) | 文字列の行間。`Custom`は`SetSpacing`に渡された行送りを使用します。 |
| [`TextObject.StyleRun`](ObjectPrimitives.md#textobjectstylerun) | クラス (入れ子) | [ObjectPrimitives](ObjectPrimitives.md) | 同じ書式の文字区間：開始位置、長さ、フォント、サイズ（ワールド単位とポイント）、スタイル... |
| [`TextObject.TabAlignment`](ObjectPrimitives.md#textobjecttabalignment) | IntEnum (入れ子) | [ObjectPrimitives](ObjectPrimitives.md) | タブストップでの文字列の配置揃え。 |
| [`TextObject.TabStop`](ObjectPrimitives.md#textobjecttabstop) | クラス (入れ子) | [ObjectPrimitives](ObjectPrimitives.md) | タブストップ：文字列の左端からのワールド単位のオフセットと配置揃え。 |
| [`TextObject.VerticalAlignment`](ObjectPrimitives.md#textobjectverticalalignment) | IntEnum (入れ子) | [ObjectPrimitives](ObjectPrimitives.md) | 原点を基準とする文字列の垂直方向の配置揃え。 |
| [`TextPair`](UILayoutCreate.md#textpair) | クラス | [UILayoutCreate](UILayoutCreate.md) | 二つのテキスト欄を持つダイアログに入力された値。 |
| [`TextStyle`](Resources.md#textstyle) | クラス | [Resources](Resources.md) | 文字スタイル（`ObjectType.TextStyle`）：文字列オブジェクトと寸法に適用するフォント、サイズ、文字属性。 |
| [`TextStyleData`](DocumentAccess.md#textstyledata) | クラス | [DocumentAccess](DocumentAccess.md) | 文字のテキストスタイルフラグ（ボールド、イタリック、アンダーライン、アウトライン、シャドウ）。`TextDefaults.GetStyle` /...で使用 |
| [`Texture`](Resources.md#texture) | クラス | [Resources](Resources.md) | テクスチャ（`ObjectType.Texture`）：レンダリングする面の色、反射、透明度、バンプ。 |
| [`Texture.Part`](Resources.md#texturepart) | IntEnum (入れ子) | [Resources](Resources.md) | テクスチャを適用するオブジェクトの部分。 |
| [`TextVerticalAlignment`](DocumentAccess.md#textverticalalignment) | IntEnum | [DocumentAccess](DocumentAccess.md) | 新しい文字の垂直方向の揃え（`TextDefaults`）。 |
| [`Tile`](Resources.md#tile) | クラス | [Resources](Resources.md) | タイルによる面（`ObjectType.TileDefinition`）：塗りつぶす領域全体で、グリッドに沿って繰り返される2Dオブジェクトのグループ。 |
| [`TitleBlockBorderObject`](ObjectsAnnotation.md#titleblockborderobject) | クラス | [ObjectsAnnotation](ObjectsAnnotation.md) | 図面枠プラグインオブジェクトです（ユニバーサル名は"Title Block Border"）。 |
| [`TitleBlockBorderObject.Revision`](ObjectsAnnotation.md#titleblockborderobjectrevision) | クラス (入れ子) | [ObjectsAnnotation](ObjectsAnnotation.md) | 表題欄の一つの改訂です。番号、日付、注記、発行日、受信者を含みます。 |
| [`Tool`](UIAutomation.md#tool) | クラス | [UIAutomation](UIAutomation.md) | 一つのツールの説明。 |
| [`ToolAccess`](UIAutomation.md#toolaccess) | クラス | [UIAutomation](UIAutomation.md) | Vectorworksのツールシステムに対する、状態を保持しないファサード。 |
| [`ToolControl`](UIAutomation.md#toolcontrol) | クラス | [UIAutomation](UIAutomation.md) | アクティブなツールを操作する、状態を保持しないドライバー。 |
| [`ToolCreationType`](UIAutomation.md#toolcreationtype) | IntEnum | [UIAutomation](UIAutomation.md) | オブジェクト作成にツールが使用する操作の種類。 |
| [`ToolFilter`](UIAutomation.md#toolfilter) | IntEnum | [UIAutomation](UIAutomation.md) | `ToolAccess.GetTools`が返すツールの範囲。 |
| [`ToolKey`](UIAutomation.md#toolkey) | IntEnum | [UIAutomation](UIAutomation.md) | 点の入力中にツールが反応するキー（`ToolControl.PressKey`を参照）。 |
| [`ToolKind`](UIAutomation.md#toolkind) | IntEnum | [UIAutomation](UIAutomation.md) | ツールの提供形態。 |
| [`ToolMode`](UIAutomation.md#toolmode) | クラス | [UIAutomation](UIAutomation.md) | アクティブなツールの、一つのツールバーボタンのグループの現在の状態。 |
| [`ToolPoint`](UIAutomation.md#toolpoint) | クラス | [UIAutomation](UIAutomation.md) | アクティブなツールに入力された一つの点。ツールが受け取る形式。 |
| [`Math.Transform2D`](ObjectPrimitives.Math.md#mathtransform2d) | クラス | [Math](ObjectPrimitives.Math.md) | 2Dアフィン変換。 |
| [`Math.Transform3D`](ObjectPrimitives.Math.md#mathtransform3d) | クラス | [Math](ObjectPrimitives.Math.md) | Pythonが所有する、列ベクトルに作用する3Dアフィン行列。A * BはBを先に適用します。 |
| [`Traverse`](DocumentAccess.md#traverse) | IntEnum | [DocumentAccess](DocumentAccess.md) | ファイルの走査でたどるオブジェクトの集合。 |
| [`TypedResource`](Resources.md#typedresource) | クラス | [Resources](Resources.md) | 一つのResourceTypeに限定されたリソース。 |

<a id="index-u"></a>

### 索引 U

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`UndoMethod`](DocumentAccess.md#undomethod) | IntEnum | [DocumentAccess](DocumentAccess.md) | `Document.StartUndoEvent`に渡す取り消し方式。 |
| [`UnitSettings`](DocumentAccess.md#unitsettings) | クラス | [DocumentAccess](DocumentAccess.md) | アクティブファイルの主単位または補助単位の寸法単位。 |

<a id="index-v"></a>

### 索引 V

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`Math.VertexType`](ObjectPrimitives.Math.md#mathvertextype) | IntEnum | [Math](ObjectPrimitives.Math.md) | 多角形状の頂点の種類。 |
| [`ViewPoint`](UIAutomation.md#viewpoint) | クラス | [UIAutomation](UIAutomation.md) | ピクセル単位のビュー座標の点（16ビット座標）。 |
| [`ViewportStyle`](Resources.md#viewportstyle) | クラス | [Resources](Resources.md) | ビューポートスタイル（`ObjectType.ViewportStyle`）：シートレイヤビューポートの保存された設定。 |
| [`ViewSize`](UIAutomation.md#viewsize) | クラス | [UIAutomation](UIAutomation.md) | アクティブビューウインドウのピクセル単位のサイズ。 |
| [`VisibilityOptions`](DocumentAccess.md#visibilityoptions) | IntEnum | [DocumentAccess](DocumentAccess.md) | アクティブでないレイヤまたはクラスの表示方法。 |

<a id="index-w"></a>

### 索引 W

| 名前 | 種類 | ページ | 概要 |
|---|---|---|---|
| [`WallObject`](ObjectsArchitect.md#wallobject) | クラス | [ObjectsArchitect](ObjectsArchitect.md) | 壁（`ObjectType.Wall`）です。窓、ドア、その他の壁挿入オブジェクトを配置できる、直線壁または円弧壁です。 |
| [`WallObject.BoundKind`](ObjectsArchitect.md#wallobjectboundkind) | IntEnum (入れ子) | [ObjectsArchitect](ObjectsArchitect.md) | 壁の高さの境界の追従先です。レイヤの高さ、レイヤの壁の高さ、またはストーリレベルを指定します。 |
| [`WallObject.BoundStatus`](ObjectsArchitect.md#wallobjectboundstatus) | IntEnum (入れ子) | [ObjectsArchitect](ObjectsArchitect.md) | 壁の高さの境界の状態です（`WallObject.HeightBound.fStatus`）。 |
| [`WallObject.Caps`](ObjectsArchitect.md#wallobjectcaps) | クラス (入れ子) | [ObjectsArchitect](ObjectsArchitect.md) | 端部キャップ。 |
| [`WallObject.HeightBound`](ObjectsArchitect.md#wallobjectheightbound) | クラス (入れ子) | [ObjectsArchitect](ObjectsArchitect.md) | 壁の下端または上端の境界です。高さの追従先を示します。 |
| [`WallObject.Heights`](ObjectsArchitect.md#wallobjectheights) | クラス (入れ子) | [ObjectsArchitect](ObjectsArchitect.md) | レイヤプレーンに対する高さです（ワールド単位、0 = レイヤ上面、負 = それより下）。 |
| [`WallStyle`](Resources.md#wallstyle) | クラス | [Resources](Resources.md) | 壁スタイル（`ObjectType.WallStyle`）：壁の構成要素、厚さ、属性。 |
| [`WallTextures`](Attributes.md#walltextures) | クラス | [Attributes](Attributes.md) | クラスの壁テクスチャ（テクスチャリソースの内部インデックス、0 = なし）。 |
| [`WindowObject`](ObjectsArchitect.md#windowobject) | クラス | [ObjectsArchitect](ObjectsArchitect.md) | Architectural Objectsプラグインの窓プラグインオブジェクトです（ユニバーサル名は"Window"）。 |
| [`Worksheet`](Resources.md#worksheet) | クラス | [Resources](Resources.md) | ワークシート。 |
| [`WorksheetCell`](Resources.md#worksheetcell) | クラス | [Resources](Resources.md) | ワークシートのセル。 |
| [`WorksheetCellContent`](Resources.md#worksheetcellcontent) | クラス | [Resources](Resources.md) | 内容を持つ一つのセル。 |
| [`WorksheetObject`](ObjectsAnnotation.md#worksheetobject) | クラス | [ObjectsAnnotation](ObjectsAnnotation.md) | 所有権を持たないワークシートリソースです。配置されたワークシートイメージや注釈のプラグインオブジェクトではありません。 |
| [`WorksheetObject.Borders`](ObjectsAnnotation.md#worksheetobjectborders) | クラス (入れ子) | [ObjectsAnnotation](ObjectsAnnotation.md) | セルの枠線フラグと、範囲の外枠および内側への適用フラグです。 |
| [`WorksheetObject.Fill`](ObjectsAnnotation.md#worksheetobjectfill) | クラス (入れ子) | [ObjectsAnnotation](ObjectsAnnotation.md) | ネイティブの面のスタイル、ファイルのColorRefインデックス、模様です。 |
| [`WorksheetObject.NumberFormat`](ObjectsAnnotation.md#worksheetobjectnumberformat) | クラス (入れ子) | [ObjectsAnnotation](ObjectsAnnotation.md) | ワークシート固有の数字の表示形式です。書式に応じた精度とUTF-8の前記号／後記号を含みます。 |
| [`WorksheetObject.Range`](ObjectsAnnotation.md#worksheetobjectrange) | クラス (入れ子) | [ObjectsAnnotation](ObjectsAnnotation.md) | 両端を含む、1から始まるワークシートの範囲です。 |
| [`WorksheetObject.TextFormat`](ObjectsAnnotation.md#worksheetobjecttextformat) | クラス (入れ子) | [ObjectsAnnotation](ObjectsAnnotation.md) | ワークシートのテキストです。ポイントサイズ、フォント／スタイル、配置、度単位の角度、ColorRefインデックス、折り返しを含みます。 |

<a id="page-layout"></a>

## ページ構成

すべてのグループページは、同じ構成になっています。

1. **タイトル** — グループ、Pythonモジュール、Vectorworksのバージョン。
2. **目次** — ページ内のすべてのクラス、入れ子の型、列挙型。
3. **概要** — 型ごとに1行で基底クラスと短い概要を記載。
4. **クラス** — 各クラスの完全修飾名、継承元、説明、コンストラクタ/メソッド (項目別)/演算子/フィールド/定数の表。入れ子のクラスと列挙型は所有クラスの後に続きます。継承するメソッドは、基底クラスで一度だけ記載します。
5. **列挙型** — メンバーと数値、説明。

Vectorworks内の `dir(api)` と `help(...)` で、実行中のバージョンで使用できるものを確認できます。

<a id="statistics"></a>

## 統計

| ページ | クラス | 列挙型 | メソッド | コンストラクタ | フィールド | 定数 |
|---|---|---|---|---|---|---|
| [DocumentAccess](DocumentAccess.md) | 16 | 11 | 508 | 16 | 18 | 0 |
| [Attributes](Attributes.md) | 17 | 11 | 249 | 17 | 37 | 1 |
| [ObjectPrimitives](ObjectPrimitives.md) | 18 | 6 | 329 | 16 | 17 | 12 |
| [Math](ObjectPrimitives.Math.md) | 15 | 2 | 383 | 36 | 51 | 5 |
| [Objects3D](Objects3D.md) | 25 | 3 | 303 | 25 | 38 | 0 |
| [ObjectsAnnotation](ObjectsAnnotation.md) | 16 | 5 | 291 | 16 | 32 | 0 |
| [ObjectsArchitect](ObjectsArchitect.md) | 14 | 3 | 176 | 14 | 31 | 0 |
| [ObjectsConnectCAD](ObjectsConnectCAD.md) | 10 | 0 | 34 | 10 | 31 | 0 |
| [ObjectsLandmark](ObjectsLandmark.md) | 9 | 19 | 211 | 9 | 0 | 0 |
| [ObjectsSpotlight](ObjectsSpotlight.md) | 4 | 0 | 15 | 4 | 11 | 0 |
| [Resources](Resources.md) | 30 | 10 | 270 | 30 | 29 | 2 |
| [Scripting](Scripting.md) | 2 | 1 | 30 | 2 | 0 | 0 |
| [UIAutomation](UIAutomation.md) | 19 | 13 | 75 | 19 | 81 | 0 |
| [UILayoutCreate](UILayoutCreate.md) | 7 | 9 | 182 | 5 | 12 | 0 |
| **合計** | **202** | **93** | **3056** | **219** | **388** | **20** |

メソッド数は名前単位です (同じ名前に複数の引数リストがあっても1件と数えます)。
