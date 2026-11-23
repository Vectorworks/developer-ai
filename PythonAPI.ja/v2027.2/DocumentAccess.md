[English](../../PythonAPI/v2027.2/DocumentAccess.md) • [Deutsch](../../PythonAPI.de/v2027.2/DocumentAccess.md) • **日本語**

<a id="documentaccess--document-layers-stories-and-preferences"></a>

# DocumentAccess — ファイル、レイヤ、ストーリ、環境設定

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

`api.Document`はAPIの入り口であり、アクティブな図面に対する状態を保持しないファサードです。必要に応じて`api.Document()`で生成し、選択内容、レイヤ、ストーリ、クラス、オブジェクト、ビュー、単位、取り消し、および型付きの設定ビュー（`DisplaySettings`、`EditingSettings`、`SnapSettings`、`GridSettings`、`StackLayersSettings`、`UnitSettings`、`TextDefaults`、`DefaultAttributes`、`ProgramVariables`）にアクセスします。

以下で使用するVectorworksの用語：**レイヤ**はデザインレイヤ（所定の縮尺を持つワールド座標平面）またはシートレイヤ（印刷可能なページ）です。**ストーリ**は、一定の基準高さにある建物の階で、その階の各レベルのデザインレイヤをまとめます。**レベルタイプ**はストーリレベルの名前（例："Slab"）です。**クラス**は名前付きのスタイルコンテナで、オブジェクトはその「クラスに従う」属性を継承します。**コンテナ**はオブジェクトを格納するもの（レイヤ、グループ、シンボル定義、ビューポート）です。

共通の規約：ゲッターは値を取得できない場合に`None`を返し、セッターとアクションは失敗時に`False`を返します。長さと座標はワールド単位、角度はラジアン（反時計回り）、文字列はUTF-8です。オブジェクトハンドルは`api.Handle`（`vs.Handle`）オブジェクトです。ヌルハンドルには`None`を渡します。ハンドルから型付きオブジェクトを取得するには`Document.As(type, h)`を使用します。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [TextStyleData](#textstyledata)
  - [ProgramVariables](#programvariables)
  - [DisplaySettings](#displaysettings)
  - [EditingSettings](#editingsettings)
  - [SnapSettings](#snapsettings)
  - [GridSettings](#gridsettings)
  - [StackLayersSettings](#stacklayerssettings)
  - [UnitSettings](#unitsettings)
  - [TextDefaults](#textdefaults)
  - [DefaultAttributes](#defaultattributes)
  - [LayerContents](#layercontents)
  - [Layer](#layer)
  - [StoryLevel](#storylevel)
  - [StoryLevelTemplate](#storyleveltemplate)
  - [Story](#story)
  - [Document](#document)
- [列挙型](#enumerations)
  - [Traverse](#traverse)
  - [Descend](#descend)
  - [LayerType](#layertype)
  - [LayerVisibility](#layervisibility)
  - [VisibilityOptions](#visibilityoptions)
  - [StoryElevationChangeMode](#storyelevationchangemode)
  - [UndoMethod](#undomethod)
  - [AngularUnit](#angularunit)
  - [TextJustification](#textjustification)
  - [TextVerticalAlignment](#textverticalalignment)
  - [TextLineSpacing](#textlinespacing)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`TextStyleData`](#textstyledata) | クラス |  | `TextDefaults.GetStyle` / `SetStyle`で使用する文字のスタイルフラグ（ボールド、イタリック、アンダーライン、アウトライン、シャドウ）。 |
| [`ProgramVariables`](#programvariables) | クラス |  | 数値セレクタを指定して、任意のVectorworksプログラム変数（アプリケーション全体またはファイルごとの設定）に型付きで低レベルアクセスします。 |
| [`DisplaySettings`](#displaysettings) | クラス |  | 表示設定。 |
| [`EditingSettings`](#editingsettings) | クラス |  | 編集とセッションの設定。 |
| [`SnapSettings`](#snapsettings) | クラス |  | スナップ（スマートカーソル）の設定。 |
| [`GridSettings`](#gridsettings) | クラス |  | グリッド設定。 |
| [`StackLayersSettings`](#stacklayerssettings) | クラス |  | 統合ビュー（スタックレイヤ）の設定。 |
| [`UnitSettings`](#unitsettings) | クラス |  | アクティブファイルの主単位または補助単位の寸法単位。 |
| [`TextDefaults`](#textdefaults) | クラス |  | 新しい文字列オブジェクトのデフォルトの文字設定。 |
| [`DefaultAttributes`](#defaultattributes) | クラス |  | 新しいオブジェクトのデフォルト属性（何も選択していないときの属性パレット）。 |
| [`LayerContents`](#layercontents) | クラス |  | レイヤの最上位オブジェクトの数と境界。 |
| [`Layer`](#layer) | クラス |  | レイヤ（デザインレイヤまたはシートレイヤ）。 |
| [`StoryLevel`](#storylevel) | クラス |  | ストーリの一つのレベル：ストーリの基準高さを基準とした名前付きの高さ（レベルタイプ）で、必要に応じてそのレベルのデザインレイヤを持ちます。 |
| [`StoryLevelTemplate`](#storyleveltemplate) | クラス |  | デフォルトのストーリレベル（オーガナイザダイアログボックス > ストーリタブ > ストーリレベル初期設定）：ストーリレベルのテンプレート。 |
| [`Story`](#story) | クラス |  | ストーリ：一定の基準高さにある建物の階。 |
| [`Document`](#document) | クラス |  | アクティブなVectorworksファイルに対する状態を保持しないファサード。 |
| [`Traverse`](#traverse) | IntEnum |  | ファイルの走査でたどるオブジェクトの集合。 |
| [`Descend`](#descend) | IntFlag |  | コンテナオブジェクト（グループ、シンボル、ビューポートなど）の内部をどの深さまで走査するか。 |
| [`LayerType`](#layertype) | IntEnum |  | レイヤの種類。 |
| [`LayerVisibility`](#layervisibility) | IntEnum |  | レイヤの表示状態（ナビゲーションパレットに表示されるもの）。 |
| [`VisibilityOptions`](#visibilityoptions) | IntEnum |  | アクティブでないレイヤまたはクラスの表示方法。 |
| [`StoryElevationChangeMode`](#storyelevationchangemode) | IntEnum |  | `Story.SetElevation`が移動するストーリ（ストーリの高さ変更ダイアログボックスの選択肢）。 |
| [`UndoMethod`](#undomethod) | IntEnum |  | `Document.StartUndoEvent`に渡す取り消し方式。 |
| [`AngularUnit`](#angularunit) | IntEnum |  | 角度の表示単位（`UnitSettings.GetAngularUnit`）。 |
| [`TextJustification`](#textjustification) | IntEnum |  | 新しい文字の水平方向の揃え（`TextDefaults`）。 |
| [`TextVerticalAlignment`](#textverticalalignment) | IntEnum |  | 新しい文字の垂直方向の揃え（`TextDefaults`）。 |
| [`TextLineSpacing`](#textlinespacing) | IntEnum |  | 新しい文字の行間（`TextDefaults`）。`Custom`は`TextDefaults.GetLeading`の行送りを使用します。 |

<a id="classes"></a>

## クラス

### TextStyleData

> **完全修飾名:** `api.TextStyleData` · **継承元:** `api.Object`

`TextDefaults.GetStyle` / `SetStyle`で使用する文字のスタイルフラグ（ボールド、イタリック、アンダーライン、アウトライン、シャドウ）。`ToBits` / `FromBits`でVectorworksのスタイルビット集合との相互変換を行います。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `TextStyleData()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `TextStyleData(bold, italic, underline, outline, shadow)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `ToBits() -> int` | 五つのスタイルフラグをVectorworksのスタイルビット集合にまとめます（ボールド1、イタリック2、アンダーライン4、アウトライン8、シャドウ16）。 |
| `FromBits(bits: int) -> TextStyleData` *静的* | Vectorworksのスタイルビット集合からTextStyleDataを作成します（ボールド1、イタリック2、アンダーライン4、アウトライン8、シャドウ16）。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: TextStyleData) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: TextStyleData) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `bold` | `bool` | ボールド。 |
| `italic` | `bool` | イタリック。 |
| `underline` | `bool` | アンダーライン。 |
| `outline` | `bool` | アウトライン。 |
| `shadow` | `bool` | シャドウ。 |

### ProgramVariables

> **完全修飾名:** `api.ProgramVariables` · **継承元:** `api.Object`

数値セレクタを指定して、任意のVectorworksプログラム変数（アプリケーション全体またはファイルごとの設定）に型付きで低レベルアクセスします。ほとんどの設定は、型付きの設定クラス（`DisplaySettings`、`EditingSettings`、`SnapSettings`、`GridSettings`、`StackLayersSettings`、`UnitSettings`、`TextDefaults`）を介してアクセスする方が便利です。名前付きのアクセサーがない設定にのみ、このクラスを使用してください。各セレクタには値の型があるため、それに合ったアクセサーを使用します：

| アクセサー | セレクタの値の型 |
|---|---|
| `GetBool` / `SetBool` | ブール値（`bool`） |
| `GetUInt8` / `SetUInt8` | 符号なし8ビット整数（0～255） |
| `GetInt8` / `SetInt8` | 符号付き8ビット整数（-128～127） |
| `GetInt16` / `SetInt16` | 16ビット整数 |
| `GetInt32` / `SetInt32` | 32ビット整数 |
| `GetDouble` / `SetDouble` | 実数（`float`）：長さ、角度、その他の実数値 |
| `GetString` / `SetString` | 文字列（`str`） |

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ProgramVariables()` | 状態を保持しないオブジェクトです。すべてのメソッドは静的で、クラス自体に対して呼び出せます。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetBool(selector: int) -> bool \| None` *静的* | ブール型のプログラム変数`selector`の値。 |
| `SetBool(selector: int, value: bool) -> bool` *静的* | ブール型のプログラム変数`selector`を設定します。 |
| `GetUInt8(selector: int) -> int \| None` *静的* | 符号なし8ビットのプログラム変数`selector`の値。 |
| `SetUInt8(selector: int, value: int) -> bool` *静的* | 符号なし8ビットのプログラム変数`selector`を設定します。 |
| `GetInt8(selector: int) -> int \| None` *静的* | 符号付き8ビットのプログラム変数`selector`の値。 |
| `SetInt8(selector: int, value: int) -> bool` *静的* | 符号付き8ビットのプログラム変数`selector`を設定します。 |
| `GetInt16(selector: int) -> int \| None` *静的* | 16ビットのプログラム変数`selector`の値。 |
| `SetInt16(selector: int, value: int) -> bool` *静的* | 16ビットのプログラム変数`selector`を設定します。 |
| `GetInt32(selector: int) -> int \| None` *静的* | 32ビットのプログラム変数`selector`の値。 |
| `SetInt32(selector: int, value: int) -> bool` *静的* | 32ビットのプログラム変数`selector`を設定します。 |
| `GetDouble(selector: int) -> float \| None` *静的* | 実数型のプログラム変数`selector`の値。 |
| `SetDouble(selector: int, value: float) -> bool` *静的* | 実数型のプログラム変数`selector`を設定します。 |
| `GetString(selector: int) -> str \| None` *静的* | 文字列型のプログラム変数`selector`の値。 |
| `SetString(selector: int, value: str) -> bool` *静的* | 文字列型のプログラム変数`selector`を設定します。 |

### DisplaySettings

> **完全修飾名:** `api.DisplaySettings` · **継承元:** `api.Object`

表示設定。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DisplaySettings()` | アクティブファイルの表示設定に対する、状態を保持しないビュー。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetBlackAndWhiteOnly() -> bool \| None` | *白黒表示*がオンかどうか。 |
| `SetBlackAndWhiteOnly(value: bool) -> bool` | *白黒表示*をオンまたはオフにします。 |
| `GetUseLayerColors() -> bool \| None` | *カラーレイヤ*がオンかどうか。 |
| `SetUseLayerColors(value: bool) -> bool` | *カラーレイヤ*をオンまたはオフにします。 |
| `GetZoomLineThickness() -> bool \| None` | *拡大時に線の太さを表示*がオンかどうか。 |
| `SetZoomLineThickness(value: bool) -> bool` | *拡大時に線の太さを表示*をオンまたはオフにします。 |
| `GetBlackBackground() -> bool \| None` | *背景を黒にする*がオンかどうか。 |
| `SetBlackBackground(value: bool) -> bool` | *背景を黒にする*をオンまたはオフにします。 |
| `GetShowRulers() -> bool \| None` | *ルーラー*がオンかどうか。 |
| `SetShowRulers(value: bool) -> bool` | *ルーラー*をオンまたはオフにします。 |
| `GetShowScrollBars() -> bool \| None` | *スクロールバーを表示*がオンかどうか。 |
| `SetShowScrollBars(value: bool) -> bool` | *スクロールバーを表示*をオンまたはオフにします。 |
| `GetShowPageBoundary() -> bool \| None` | *用紙の大きさを表示*がオンかどうか。 |
| `SetShowPageBoundary(value: bool) -> bool` | *用紙の大きさを表示*をオンまたはオフにします。 |
| `GetShowPageBreaks() -> bool \| None` | *用紙境界を表示*がオンかどうか。 |
| `SetShowPageBreaks(value: bool) -> bool` | *用紙境界を表示*をオンまたはオフにします。 |
| `GetShowOthersInGroup() -> bool \| None` | *編集モード時に他の図形を表示*がオンかどうか。 |
| `SetShowOthersInGroup(value: bool) -> bool` | *編集モード時に他の図形を表示*をオンまたはオフにします。 |
| `GetShowOthersInGroupGrayed() -> bool \| None` | *他の図形をグレイ表示*がオンかどうか。 |
| `SetShowOthersInGroupGrayed(value: bool) -> bool` | *他の図形をグレイ表示*をオンまたはオフにします。 |
| `GetEightSelectionHandles() -> bool \| None` | *変形ハンドルを8個表示*がオンかどうか。 |
| `SetEightSelectionHandles(value: bool) -> bool` | *変形ハンドルを8個表示*をオンまたはオフにします。 |
| `GetFullScreenCursor() -> bool \| None` | *フルスクリーンカーソル*がオンかどうか。 |
| `SetFullScreenCursor(value: bool) -> bool` | *フルスクリーンカーソル*をオンまたはオフにします。 |
| `GetNoFillBehindText() -> bool \| None` | *文字にアミをかけない*がオンかどうか。 |
| `SetNoFillBehindText(value: bool) -> bool` | *文字にアミをかけない*をオンまたはオフにします。 |
| `GetAdjustFlippedText() -> bool \| None` | *文字の反転禁止*がオンかどうか。 |
| `SetAdjustFlippedText(value: bool) -> bool` | *文字の反転禁止*をオンまたはオフにします。 |
| `GetXRayMode() -> bool \| None` | *X線選択モード*がオンかどうか。 |
| `SetXRayMode(value: bool) -> bool` | *X線選択モード*をオンまたはオフにします。 |
| `GetDisplayHiddenObjectsGhosted() -> bool \| None` | *オブジェクトをゴースト表示*がオンかどうか。 |
| `SetDisplayHiddenObjectsGhosted(value: bool) -> bool` | *オブジェクトをゴースト表示*をオンまたはオフにします。 |
| `GetShowInternalOriginMarker() -> bool \| None` | *基準原点マーカーを表示*がオンかどうか。 |
| `SetShowInternalOriginMarker(value: bool) -> bool` | *基準原点マーカーを表示*をオンまたはオフにします。 |
| `GetAllowDropShadows() -> bool \| None` | *ドロップシャドウ*がオンかどうか。 |
| `SetAllowDropShadows(value: bool) -> bool` | *ドロップシャドウ*をオンまたはオフにします。 |
| `GetPerspectiveCropped() -> bool \| None` | *透視投影ビューをクロップする*がオンかどうか。 |
| `SetPerspectiveCropped(value: bool) -> bool` | *透視投影ビューをクロップする*をオンまたはオフにします。 |
| `Get2DConversionResolution() -> int \| None` | 対応する設定ポップアップの生の値。 |
| `Set2DConversionResolution(value: int) -> bool` | 円周の分割数を設定します。対応する設定ポップアップの生の値です。 |
| `Get3DConversionResolution() -> int \| None` | 回転体の分割数を返します。 |
| `Set3DConversionResolution(value: int) -> bool` | 回転体の分割数を設定します。 |
| `GetDisplayLightObjects() -> int \| None` | 光源オブジェクトの表示を返します。 |
| `SetDisplayLightObjects(value: int) -> bool` | 光源オブジェクトの表示を設定します。 |
| `GetRotatedTextDisplay() -> int \| None` | 回転した文字の表示を返します。 |
| `SetRotatedTextDisplay(value: int) -> bool` | 回転した文字の表示を設定します。 |
| `GetDisplayBitmaps() -> int \| None` | ビットマップの表示を返します。 |
| `SetDisplayBitmaps(value: int) -> bool` | ビットマップの表示を設定します。 |
| `GetHiddenLineShade() -> int \| None` | 隠線の濃さを返します。 |
| `SetHiddenLineShade(value: int) -> bool` | 隠線の濃さを設定します。 |
| `GetDisplay3DLoci() -> int \| None` | 3D基準点の表示を返します。 |
| `SetDisplay3DLoci(value: int) -> bool` | 3D基準点の表示を設定します。 |
| `GetDefaultRenderMode() -> int \| None` | デフォルトのレンダリングモードを返します。 |
| `SetDefaultRenderMode(value: int) -> bool` | デフォルトのレンダリングモードを設定します。 |
| `GetDefaultProjection() -> int \| None` | デフォルトの投影の方法を返します。 |
| `SetDefaultProjection(value: int) -> bool` | デフォルトの投影の方法を設定します。 |
| `Get3DRotationResponse() -> int \| None` | 3D回転時の応答性（1..5）を返します。 |
| `Set3DRotationResponse(value: int) -> bool` | 3D回転時の応答性を設定します。 |

### EditingSettings

> **完全修飾名:** `api.EditingSettings` · **継承元:** `api.Object`

編集とセッションの設定。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `EditingSettings()` | 編集とセッションの設定に対する、状態を保持しないビュー。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetClickDrag() -> bool \| None` | *クリック-ドラッグ描画を有効にする*がオンかどうか。 |
| `SetClickDrag(value: bool) -> bool` | *クリック-ドラッグ描画を有効にする*をオンまたはオフにします。 |
| `GetOffsetDuplicates() -> bool \| None` | *ずれを伴う複製*がオンかどうか。 |
| `SetOffsetDuplicates(value: bool) -> bool` | *ずれを伴う複製*をオンまたはオフにします。 |
| `GetAssociateDimensions() -> bool \| None` | *寸法を図形の大きさと連動させる*がオンかどうか。 |
| `SetAssociateDimensions(value: bool) -> bool` | *寸法を図形の大きさと連動させる*をオンまたはオフにします。 |
| `GetAutoAssociateDimensions() -> bool \| None` | *一番上の図形に連動*がオンかどうか。 |
| `SetAutoAssociateDimensions(value: bool) -> bool` | *一番上の図形に連動*をオンまたはオフにします。 |
| `GetCreateDimensionsInDimensionClass() -> bool \| None` | *寸法を指定クラスに作成する*がオンかどうか。 |
| `SetCreateDimensionsInDimensionClass(value: bool) -> bool` | *寸法を指定クラスに作成する*をオンまたはオフにします。 |
| `GetWallAutoJoin() -> bool \| None` | *壁の自動結合*がオンかどうか。 |
| `SetWallAutoJoin(value: bool) -> bool` | *壁の自動結合*をオンまたはオフにします。 |
| `GetUndoViewChanges() -> bool \| None` | *ビュー変更の取り消し回数を設定*がオンかどうか。 |
| `SetUndoViewChanges(value: bool) -> bool` | *ビュー変更の取り消し回数を設定*をオンまたはオフにします。 |
| `GetDuplicateTagsWithObjects() -> bool \| None` | *オブジェクトと一緒にデータタグも複製*がオンかどうか。 |
| `SetDuplicateTagsWithObjects(value: bool) -> bool` | *オブジェクトと一緒にデータタグも複製*をオンまたはオフにします。 |
| `GetOccludedPickingAndSnapping() -> bool \| None` | *選択/スナップオクルージョンを使用*がオンかどうか。 |
| `SetOccludedPickingAndSnapping(value: bool) -> bool` | *選択/スナップオクルージョンを使用*をオンまたはオフにします。 |
| `GetMaxUndos() -> int \| None` | 取り消しの最大回数を返します。 |
| `SetMaxUndos(value: int) -> bool` | 取り消しの最大回数を設定します。 |
| `GetAutoSaveInterval() -> int \| None` | 自動保存の間隔を返します。 |
| `SetAutoSaveInterval(value: int) -> bool` | 自動保存の間隔を設定します。 |
| `GetBackupInterval() -> int \| None` | バックアップの間隔を返します。 |
| `SetBackupInterval(value: int) -> bool` | バックアップの間隔を設定します。 |
| `GetLineWeightUnit() -> int \| None` | 線の太さの単位を返します。 |
| `SetLineWeightUnit(value: int) -> bool` | 線の太さの単位を設定します。 |
| `GetDimensionStandard() -> int \| None` | 寸法規格を返します。 |
| `SetDimensionStandard(value: int) -> bool` | 寸法規格を設定します。 |
| `GetCustomMoveDistance() -> float \| None` | カスタム移動距離を返します。 |
| `SetCustomMoveDistance(value: float) -> bool` | カスタム移動距離を設定します。 |

### SnapSettings

> **完全修飾名:** `api.SnapSettings` · **継承元:** `api.Object`

スナップ（スマートカーソル）の設定。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `SnapSettings()` | スナップ設定に対する、状態を保持しないビュー。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `GetSnapToGrid() -> bool \| None` | *グリッドスナップ*がオンかどうか。 |
| `SetSnapToGrid(value: bool) -> bool` | *グリッドスナップ*をオンまたはオフにします。 |
| `GetSnapToObjects() -> bool \| None` | *図形スナップ*がオンかどうか。 |
| `SetSnapToObjects(value: bool) -> bool` | *図形スナップ*をオンまたはオフにします。 |
| `GetSnapToLoci() -> bool \| None` | *基準点スナップ*がオンかどうか。 |
| `SetSnapToLoci(value: bool) -> bool` | *基準点スナップ*をオンまたはオフにします。 |
| `GetSnapToEdgePoints() -> bool \| None` | *辺上の点にスナップ*がオンかどうか。 |
| `SetSnapToEdgePoints(value: bool) -> bool` | *辺上の点にスナップ*をオンまたはオフにします。 |
| `GetSnapToSelectionOnly() -> bool \| None` | *選択対象のみにスナップ*がオンかどうか。 |
| `SetSnapToSelectionOnly(value: bool) -> bool` | *選択対象のみにスナップ*をオンまたはオフにします。 |
| `GetSnapToAngle() -> bool \| None` | *角度スナップ*がオンかどうか。 |
| `SetSnapToAngle(value: bool) -> bool` | *角度スナップ*をオンまたはオフにします。 |
| `GetSnapToIntersection() -> bool \| None` | *交点スナップ*がオンかどうか。 |
| `SetSnapToIntersection(value: bool) -> bool` | *交点スナップ*をオンまたはオフにします。 |
| `GetSmartPoints() -> bool \| None` | *スマートポイント*がオンかどうか。 |
| `SetSmartPoints(value: bool) -> bool` | *スマートポイント*をオンまたはオフにします。 |
| `GetSnapToDistance() -> bool \| None` | *定点スナップ*がオンかどうか。 |
| `SetSnapToDistance(value: bool) -> bool` | *定点スナップ*をオンまたはオフにします。 |
| `GetSmartEdge() -> bool \| None` | *スマートエッジ*がオンかどうか。 |
| `SetSmartEdge(value: bool) -> bool` | *スマートエッジ*をオンまたはオフにします。 |
| `GetConstrainTangent() -> bool \| None` | *接線拘束*がオンかどうか。 |
| `SetConstrainTangent(value: bool) -> bool` | *接線拘束*をオンまたはオフにします。 |
| `GetSnapToEndPoint() -> bool \| None` | *端点*がオンかどうか。 |
| `SetSnapToEndPoint(value: bool) -> bool` | *端点*をオンまたはオフにします。 |
| `GetSnapToMidPoint() -> bool \| None` | *辺の中点*がオンかどうか。 |
| `SetSnapToMidPoint(value: bool) -> bool` | *辺の中点*をオンまたはオフにします。 |
| `GetSnapToCenter() -> bool \| None` | *図形の中心*がオンかどうか。 |
| `SetSnapToCenter(value: bool) -> bool` | *図形の中心*をオンまたはオフにします。 |
| `GetSnapToQuadrant() -> bool \| None` | *四分点ポイント*がオンかどうか。 |
| `SetSnapToQuadrant(value: bool) -> bool` | *四分点ポイント*をオンまたはオフにします。 |
| `GetSnapToInsertionPoint() -> bool \| None` | *挿入点*がオンかどうか。 |
| `SetSnapToInsertionPoint(value: bool) -> bool` | *挿入点*をオンまたはオフにします。 |
| `GetSnapToVertex() -> bool \| None` | *頂点*がオンかどうか。 |
| `SetSnapToVertex(value: bool) -> bool` | *頂点*をオンまたはオフにします。 |
| `GetSnapToEdge() -> bool \| None` | *辺*がオンかどうか。 |
| `SetSnapToEdge(value: bool) -> bool` | *辺*をオンまたはオフにします。 |
| `GetSnapToMasterPoints() -> bool \| None` | *マスタースナップポイント*がオンかどうか。 |
| `SetSnapToMasterPoints(value: bool) -> bool` | *マスタースナップポイント*をオンまたはオフにします。 |
| `GetSnapToRelativeAngles() -> bool \| None` | *直前のクリックに関連する図形からの角度*がオンかどうか。 |
| `SetSnapToRelativeAngles(value: bool) -> bool` | *直前のクリックに関連する図形からの角度*をオンまたはオフにします。 |
| `GetSnapToAlternateCoordinateSystem() -> bool \| None` | *特定角度スナップの追加*がオンかどうか。 |
| `SetSnapToAlternateCoordinateSystem(value: bool) -> bool` | *特定角度スナップの追加*をオンまたはオフにします。 |
| `GetSnapToAnglesFromAxes() -> bool \| None` | *軸からの角度*がオンかどうか（読み取り専用）。 |
| `GetSnapToCombinedPageArea() -> bool \| None` | *用紙全体にスナップ*がオンかどうか。 |
| `SetSnapToCombinedPageArea(value: bool) -> bool` | *用紙全体にスナップ*をオンまたはオフにします。 |
| `GetSnapToIndividualPages() -> bool \| None` | *個々のページにスナップ*がオンかどうか。 |
| `SetSnapToIndividualPages(value: bool) -> bool` | *個々のページにスナップ*をオンまたはオフにします。 |
| `GetFloatingDatum() -> bool \| None` | *フローティング起点*がオンかどうか。 |
| `SetFloatingDatum(value: bool) -> bool` | *フローティング起点*をオンまたはオフにします。 |
| `GetShowSnapBox() -> bool \| None` | *スナップボックスを表示*がオンかどうか。 |
| `SetShowSnapBox(value: bool) -> bool` | *スナップボックスを表示*をオンまたはオフにします。 |
| `GetShowSelectionBox() -> bool \| None` | *セレクションボックスを表示*がオンかどうか。 |
| `SetShowSelectionBox(value: bool) -> bool` | *セレクションボックスを表示*をオンまたはオフにします。 |
| `GetSnapRadiusPixels() -> int \| None` | スナップ半径をピクセル単位で返します。 |
| `SetSnapRadiusPixels(value: int) -> bool` | スナップ半径をピクセル単位で設定します。 |
| `GetSnapBoxRadius() -> float \| None` | スナップボックスの半径を返します。 |
| `SetSnapBoxRadius(value: float) -> bool` | スナップボックスの半径を設定します。 |
| `GetSelectionRadius() -> float \| None` | 選択半径を返します。 |
| `SetSelectionRadius(value: float) -> bool` | 選択半径を設定します。 |

*角度*

| メソッド | 説明 |
|---|---|
| `GetSnapAngles() -> str \| None` | スナップ角度を返します。度単位のカンマ区切りリストです（例："30,45,60"）。 |
| `SetSnapAngles(degreesList: str) -> bool` | スナップ角度を設定します。 |
| `GetRelativeAngle() -> float \| None` | 相対角度（ラジアン）を返します。 |
| `SetRelativeAngle(radians: float) -> bool` | 相対角度を設定します。 |
| `GetAlternateCoordinateSystemAngle() -> float \| None` | 特定角度スナップの角度（ラジアン）を返します。 |
| `SetAlternateCoordinateSystemAngle(radians: float) -> bool` | 特定角度スナップの角度を設定します。 |

*辺スナップのオプション*

| メソッド | 説明 |
|---|---|
| `GetUseEdgeOffset() -> bool \| None` | *スナップのオフセット*がオンかどうか。 |
| `SetUseEdgeOffset(value: bool) -> bool` | *スナップのオフセット*をオンまたはオフにします。 |
| `GetEdgeOffsetDistance() -> float \| None` | スナップのオフセット距離を返します。 |
| `SetEdgeOffsetDistance(value: float) -> bool` | スナップのオフセット距離を設定します。 |
| `GetUseProportionalDivision() -> bool \| None` | *パーセントで*（比例分割を使用）がオンかどうか。 |
| `SetUseProportionalDivision(value: bool) -> bool` | *パーセントで*（比例分割を使用）をオンまたはオフにします。 |
| `GetProportionalPercent() -> float \| None` | 比率をパーセントで返します。 |
| `SetProportionalPercent(value: float) -> bool` | 比率をパーセントで設定します。 |
| `GetUseMultipleDivisions() -> bool \| None` | *反復スナップ*（複数分割を使用）がオンかどうか。 |
| `SetUseMultipleDivisions(value: bool) -> bool` | *反復スナップ*（複数分割を使用）をオンまたはオフにします。 |
| `GetDivisionDistance() -> float \| None` | 分割距離を返します。 |
| `SetDivisionDistance(value: float) -> bool` | 分割距離を設定します。 |

### GridSettings

> **完全修飾名:** `api.GridSettings` · **継承元:** `api.Object`

グリッド設定。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `GridSettings()` | グリッド設定に対する、状態を保持しないビュー。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetShowGrid() -> bool \| None` | *グリッドを表示*がオンかどうか。 |
| `SetShowGrid(value: bool) -> bool` | *グリッドを表示*をオンまたはオフにします。 |
| `GetPrintGrid() -> bool \| None` | *グリッド印刷*がオンかどうか。 |
| `SetPrintGrid(value: bool) -> bool` | *グリッド印刷*をオンまたはオフにします。 |
| `GetSnapToGrid() -> bool \| None` | *グリッドスナップ*がオンかどうか。 |
| `SetSnapToGrid(value: bool) -> bool` | *グリッドスナップ*をオンまたはオフにします。 |
| `GetSnapGridX() -> float \| None` | スナップグリッドのXを返します。 |
| `SetSnapGridX(value: float) -> bool` | スナップグリッドのXを設定します。 |
| `GetSnapGridY() -> float \| None` | スナップグリッドのYを返します。 |
| `SetSnapGridY(value: float) -> bool` | スナップグリッドのYを設定します。 |
| `GetReferenceGridX() -> float \| None` | レファレンスグリッドのXを返します。 |
| `SetReferenceGridX(value: float) -> bool` | レファレンスグリッドのXを設定します。 |
| `GetReferenceGridY() -> float \| None` | レファレンスグリッドのYを返します。 |
| `SetReferenceGridY(value: float) -> bool` | レファレンスグリッドのYを設定します。 |
| `GetSheetLayerSnapGridX() -> float \| None` | シートレイヤのスナップグリッドのXを返します。 |
| `SetSheetLayerSnapGridX(value: float) -> bool` | シートレイヤのスナップグリッドのXを設定します。 |
| `GetSheetLayerSnapGridY() -> float \| None` | シートレイヤのスナップグリッドのYを返します。 |
| `SetSheetLayerSnapGridY(value: float) -> bool` | シートレイヤのスナップグリッドのYを設定します。 |
| `GetAngle() -> float \| None` | 角度（ラジアン）を返します。 |
| `SetAngle(radians: float) -> bool` | 角度を設定します。 |
| `GetAngleY() -> float \| None` | Yの角度（ラジアン）を返します。 |
| `SetAngleY(radians: float) -> bool` | Yの角度を設定します。 |

### StackLayersSettings

> **完全修飾名:** `api.StackLayersSettings` · **継承元:** `api.Object`

統合ビュー（スタックレイヤ）の設定。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `StackLayersSettings()` | 統合ビュー（スタックレイヤ）の設定に対する、状態を保持しないビュー。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetEnabled() -> bool \| None` | *有効*がオンかどうか。 |
| `SetEnabled(value: bool) -> bool` | *有効*をオンまたはオフにします。 |
| `GetCreate2DObjects() -> bool \| None` | *スクリーン（スクリーンプレーン）図形を表示*がオンかどうか。 |
| `SetCreate2DObjects(value: bool) -> bool` | *スクリーン（スクリーンプレーン）図形を表示*をオンまたはオフにします。 |
| `GetIgnoreOtherScales() -> bool \| None` | *縮尺が同じレイヤのみを表示*がオンかどうか。 |
| `SetIgnoreOtherScales(value: bool) -> bool` | *縮尺が同じレイヤのみを表示*をオンまたはオフにします。 |
| `GetRestoreViews() -> bool \| None` | *統合ビュー解除時に元の表示を回復*がオンかどうか。 |
| `SetRestoreViews(value: bool) -> bool` | *統合ビュー解除時に元の表示を回復*をオンまたはオフにします。 |
| `GetCenterView() -> bool \| None` | *アクティブレイヤを中央に表示*がオンかどうか。 |
| `SetCenterView(value: bool) -> bool` | *アクティブレイヤを中央に表示*をオンまたはオフにします。 |
| `GetShowPageBoundary() -> bool \| None` | *用紙の大きさを表示*がオンかどうか。 |
| `SetShowPageBoundary(value: bool) -> bool` | *用紙の大きさを表示*をオンまたはオフにします。 |
| `GetOnlyActiveLayer2DObjects() -> bool \| None` | *アクティブレイヤのみ表示*がオンかどうか。 |
| `SetOnlyActiveLayer2DObjects(value: bool) -> bool` | *アクティブレイヤのみ表示*をオンまたはオフにします。 |
| `GetOnlyStoryLayers() -> bool \| None` | *ストーリに属したレイヤのみ表示*がオンかどうか。 |
| `SetOnlyStoryLayers(value: bool) -> bool` | *ストーリに属したレイヤのみ表示*をオンまたはオフにします。 |

### UnitSettings

> **完全修飾名:** `api.UnitSettings` · **継承元:** `api.Object`

アクティブファイルの主単位または補助単位の寸法単位。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `UnitSettings(primary: bool = True)` | 主単位（`primary=True`）または補助単位のビュー。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `IsPrimary() -> bool` | 主単位の場合はTrue、補助単位の場合はFalse。 |
| `GetName() -> str \| None` | 名前を返します。 |
| `SetName(value: str) -> bool` | 名前を設定します。 |
| `GetMark() -> str \| None` | 記号を返します。 |
| `SetMark(value: str) -> bool` | 記号を設定します。 |
| `GetUnitsPerInch() -> float \| None` | インチあたりの単位数を返します。 |
| `SetUnitsPerInch(value: float) -> bool` | インチあたりの単位数を設定します。 |
| `GetStyle() -> int \| None` | スタイル（生の単位スタイル）を返します。 |
| `SetStyle(value: int) -> bool` | スタイルを設定します。 |
| `GetIsMetric() -> bool \| None` | *メートル系*がオンかどうか。 |
| `IsMetric() -> bool \| None` | 単位がメートル系の場合はTrue（`GetIsMetric`と同じ）。 |
| `SetIsMetric(value: bool) -> bool` | *メートル系*をオンまたはオフにします。 |
| `GetShowUnitMark() -> bool \| None` | *単位記号を表示*がオンかどうか。 |
| `SetShowUnitMark(value: bool) -> bool` | *単位記号を表示*をオンまたはオフにします。 |
| `GetLeadingZero() -> bool \| None` | *整数部の0を表示*がオンかどうか。 |
| `SetLeadingZero(value: bool) -> bool` | *整数部の0を表示*をオンまたはオフにします。 |
| `GetTrailingZeros() -> bool \| None` | *有効桁分0を表示*がオンかどうか。 |
| `SetTrailingZeros(value: bool) -> bool` | *有効桁分0を表示*をオンまたはオフにします。 |
| `GetDisplayAsFraction() -> bool \| None` | *分数で表示*がオンかどうか。 |
| `SetDisplayAsFraction(value: bool) -> bool` | *分数で表示*をオンまたはオフにします。 |
| `GetShowThousandsSeparator() -> bool \| None` | *寸法3桁位取り*がオンかどうか。 |
| `SetShowThousandsSeparator(value: bool) -> bool` | *寸法3桁位取り*をオンまたはオフにします。 |
| `GetDecimalDisplayPrecision() -> int \| None` | 小数の表示精度を返します。 |
| `SetDecimalDisplayPrecision(value: int) -> bool` | 小数の表示精度を設定します。 |
| `GetDecimalDimensionPrecision() -> int \| None` | 小数の寸法精度を返します。 |
| `SetDecimalDimensionPrecision(value: int) -> bool` | 小数の寸法精度を設定します。 |
| `GetFractionalDisplayPrecision() -> int \| None` | 分数の表示精度を返します。 |
| `SetFractionalDisplayPrecision(value: int) -> bool` | 分数の表示精度を設定します。 |
| `GetFractionalDimensionPrecision() -> int \| None` | 分数の寸法精度を返します。 |
| `SetFractionalDimensionPrecision(value: int) -> bool` | 分数の寸法精度を設定します。 |
| `GetAngularUnit() -> AngularUnit \| None` | 角度単位を返します。 |
| `SetAngularUnit(value: AngularUnit) -> bool` | 角度単位を設定します。 |
| `GetWorldUnitsPerUnit() -> float \| None` | 主単位のみ（補助単位ではNone / False）（読み取り専用）。 |
| `GetSquareUnitDivision() -> int \| None` | 平方単位の分割を返します。 |
| `SetSquareUnitDivision(value: int) -> bool` | 平方単位の分割を設定します。 |
| `GetSquareUnitMark() -> str \| None` | 平方単位の記号を返します。 |
| `SetSquareUnitMark(value: str) -> bool` | 平方単位の記号を設定します。 |
| `GetAreaUnitName() -> str \| None` | 面積単位の名前を返します。 |
| `SetAreaUnitName(value: str) -> bool` | 面積単位の名前を設定します。 |
| `GetAreaUnitMark() -> str \| None` | 面積単位の記号を返します。 |
| `SetAreaUnitMark(value: str) -> bool` | 面積単位の記号を設定します。 |
| `GetAreaUnitsPerSquareInch() -> float \| None` | 平方インチあたりの面積単位数を返します。 |
| `SetAreaUnitsPerSquareInch(value: float) -> bool` | 平方インチあたりの面積単位数を設定します。 |
| `GetAreaDecimalPrecision() -> int \| None` | 面積の小数精度を返します。 |
| `SetAreaDecimalPrecision(value: int) -> bool` | 面積の小数精度を設定します。 |
| `GetVolumeUnitName() -> str \| None` | 体積単位の名前を返します。 |
| `SetVolumeUnitName(value: str) -> bool` | 体積単位の名前を設定します。 |
| `GetVolumeUnitMark() -> str \| None` | 体積単位の記号を返します。 |
| `SetVolumeUnitMark(value: str) -> bool` | 体積単位の記号を設定します。 |
| `GetVolumeUnitsPerCubicInch() -> float \| None` | 立方インチあたりの体積単位数を返します。 |
| `SetVolumeUnitsPerCubicInch(value: float) -> bool` | 立方インチあたりの体積単位数を設定します。 |
| `GetVolumeDecimalPrecision() -> int \| None` | 体積の小数精度を返します。 |
| `SetVolumeDecimalPrecision(value: int) -> bool` | 体積の小数精度を設定します。 |
| `GetDocumentAngularUnit() -> AngularUnit \| None` | ファイルの角度設定（主単位と補助単位で共有）。 |
| `SetDocumentAngularUnit(value: AngularUnit) -> bool` | ファイルの角度単位を設定します（ファイルの角度設定は主単位と補助単位で共有）。 |
| `GetDocumentAngularPrecision() -> int \| None` | ファイルの角度精度を返します。 |
| `SetDocumentAngularPrecision(value: int) -> bool` | ファイルの角度精度を設定します。 |

### TextDefaults

> **完全修飾名:** `api.TextDefaults` · **継承元:** `api.Object`

新しい文字列オブジェクトのデフォルトの文字設定。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `TextDefaults()` | デフォルトの文字設定に対する、状態を保持しないビュー。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetFontName() -> str \| None` | フォント名を返します。 |
| `SetFontName(value: str) -> bool` | フォント名を設定します。 |
| `GetSize() -> float \| None` | サイズ（ワールド単位）を返します。 |
| `SetSize(value: float) -> bool` | サイズを設定します。 |
| `GetStyle() -> TextStyleData \| None` | スタイルを返します。 |
| `SetStyle(value: TextStyleData) -> bool` | スタイルを設定します。 |
| `GetJustification() -> TextJustification \| None` | 水平方向の揃えを返します。 |
| `SetJustification(value: TextJustification) -> bool` | 水平方向の揃えを設定します。 |
| `GetVerticalAlignment() -> TextVerticalAlignment \| None` | 垂直方向の揃えを返します。 |
| `SetVerticalAlignment(value: TextVerticalAlignment) -> bool` | 垂直方向の揃えを設定します。 |
| `GetLineSpacing() -> TextLineSpacing \| None` | 行間を返します。 |
| `SetLineSpacing(value: TextLineSpacing) -> bool` | 行間を設定します。 |
| `GetLeading() -> float \| None` | 行送り（カスタム行間）を返します。 |
| `SetLeading(value: float) -> bool` | 行送りを設定します。 |

### DefaultAttributes

> **完全修飾名:** `api.DefaultAttributes` · **継承元:** `api.Object`

新しいオブジェクトのデフォルト属性（何も選択していないときの属性パレット）。`SetXxxByClass()`メソッドは、属性をアクティブなクラスに従わせます。明示的な値を設定すると、対応する「クラスに従う」フラグが解除されます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DefaultAttributes()` | 新しいオブジェクトのデフォルト属性に対する、状態を保持しないビュー。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `GetColors() -> ObjectColors \| None` | 色。 |
| `SetColors(colors: ObjectColors) -> bool` | 色を設定します。 |
| `GetPenColorsByClass() -> bool \| None` | *線の色をクラスに従わせる*がオンかどうか。 |
| `SetPenColorsByClass() -> bool` | 線の色をクラスに従わせます。 |
| `GetFillColorsByClass() -> bool \| None` | *面の色をクラスに従わせる*がオンかどうか。 |
| `SetFillColorsByClass() -> bool` | 面の色をクラスに従わせます。 |

*線*

| メソッド | 説明 |
|---|---|
| `GetPenStyle() -> int \| None` | 生の線スタイル。`PenAttributes.GetStyle`と同じ値です。 |
| `SetPenStyle(style: int) -> bool` | 線スタイルを設定します（生の線スタイル。`PenAttributes.GetStyle`と同じ値）。 |
| `GetPenStyleByClass() -> bool \| None` | *線スタイルをクラスに従わせる*がオンかどうか。 |
| `SetPenStyleByClass() -> bool` | 線スタイルをクラスに従わせます。 |
| `GetLineWeightMils() -> int \| None` | 線の太さをミル単位で返します。 |
| `SetLineWeightMils(mils: int) -> bool` | 線の太さをミル単位で設定します。 |
| `GetLineWeightByClass() -> bool \| None` | *線の太さをクラスに従わせる*がオンかどうか。 |
| `SetLineWeightByClass() -> bool` | 線の太さをクラスに従わせます。 |

*面*

| メソッド | 説明 |
|---|---|
| `GetFillStyle() -> int \| None` | 生の面スタイル。`FillAttributes.GetStyle`と同じ値です。 |
| `SetFillStyle(style: int) -> bool` | 面スタイルを設定します（生の面スタイル。`FillAttributes.GetStyle`と同じ値）。 |
| `GetFillStyleByClass() -> bool \| None` | *面スタイルをクラスに従わせる*がオンかどうか。 |
| `SetFillStyleByClass() -> bool` | 面スタイルをクラスに従わせます。 |
| `GetFillTypeRaw() -> int \| None` | 面の種類の生の値を返します（読み取り専用）。 |
| `GetHatch() -> int \| None` | ハッチングを返します。 |
| `SetHatch(hatch: int) -> bool` | ハッチングを設定します。 |
| `GetGradient() -> int \| None` | グラデーションを返します。 |
| `SetGradient(gradient: int) -> bool` | グラデーションを設定します。 |
| `GetImageFill() -> int \| None` | イメージによる面を返します。 |
| `SetImageFill(image: int) -> bool` | イメージによる面を設定します。 |
| `GetTile() -> int \| None` | タイルを返します。 |
| `SetTile(tile: int) -> bool` | タイルを設定します。 |

*不透明度*

| メソッド | 説明 |
|---|---|
| `GetPenOpacity() -> int \| None` | 線の不透明度を返します。 |
| `GetFillOpacity() -> int \| None` | 面の不透明度を返します。 |
| `SetOpacity(pen: int, fill: int) -> bool` | 不透明度を設定します。 |
| `GetPenOpacityByClass() -> bool \| None` | *線の不透明度をクラスに従わせる*がオンかどうか。 |
| `GetFillOpacityByClass() -> bool \| None` | *面の不透明度をクラスに従わせる*がオンかどうか。 |
| `SetOpacityByClass(penByClass: bool, fillByClass: bool) -> bool` | 不透明度をクラスに従わせます。 |

*マーカー*

| メソッド | 説明 |
|---|---|
| `GetBeginningMarker() -> Marker \| None` | 始点マーカーを返します。 |
| `SetBeginningMarker(marker: Marker) -> bool` | 始点マーカーを設定します。 |
| `GetEndMarker() -> Marker \| None` | 終点マーカーを返します。 |
| `SetEndMarker(marker: Marker) -> bool` | 終点マーカーを設定します。 |
| `GetMarkersByClass() -> bool \| None` | *マーカーをクラスに従わせる*がオンかどうか。 |
| `SetMarkersByClass() -> bool` | マーカーをクラスに従わせます。 |
| `GetDocumentDropShadow() -> DropShadow \| None` | ファイルのドロップシャドウ（ファイル設定）。 |
| `GetClass() -> ClassAttributes` | 新しいオブジェクトと新しい寸法に使用するクラス。 |
| `SetClass(theClass: ClassAttributes) -> bool` | クラスを設定します（新しいオブジェクトと新しい寸法に使用するクラス）。 |
| `GetDimensionClass() -> ClassAttributes` | 寸法クラスを返します。 |
| `SetDimensionClass(theClass: ClassAttributes) -> bool` | 寸法クラスを設定します。 |

### LayerContents

> **完全修飾名:** `api.LayerContents` · **継承元:** `api.Object`

レイヤの最上位オブジェクトの数と境界。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `LayerContents()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `LayerContents(fObjectCount, fBounds)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fObjectCount` | `int` | 最上位オブジェクトの数。 |
| `fBounds` | `Math.Rect2D \| None` | 最上位オブジェクトの境界。空のレイヤでは`None`。 |

### Layer

> **完全修飾名:** `api.Layer` · **継承元:** `api.Object`

レイヤ（デザインレイヤまたはシートレイヤ）。レイヤでないハンドルから生成すると、無効なオブジェクトになります（`IsValid()` == `False`）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Layer(hLayer: Handle)` | 既存のレイヤ`hLayer`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `GetHandle() -> Handle` | レイヤのハンドル。 |
| `IsValid() -> bool` | このオブジェクトが既存のレイヤを参照している場合はTrue。 |

*識別情報*

| メソッド | 説明 |
|---|---|
| `GetName() -> str \| None` | 名前を返します。 |
| `SetName(name: str) -> bool` | 名前を設定します。 |
| `GetType() -> LayerType \| None` | 種類を返します。 |
| `IsDesignLayer() -> bool` | デザインレイヤの場合はTrue。 |
| `IsSheetLayer() -> bool` | シートレイヤの場合はTrue。 |
| `GetNext() -> Layer` | 次のものを返します。 |
| `GetPrevious() -> Layer` | 前のものを返します。 |

*状態*

| メソッド | 説明 |
|---|---|
| `IsActive() -> bool` | これがアクティブレイヤの場合はTrue。 |
| `Activate() -> bool` | このレイヤをアクティブレイヤにします。 |
| `GetVisibility() -> LayerVisibility \| None` | 表示状態を返します。 |
| `SetVisibility(visibility: LayerVisibility) -> bool` | 表示状態を設定します。 |

*デザインレイヤのプロパティ*

| メソッド | 説明 |
|---|---|
| `GetScale() -> float \| None` | 縮尺（1:scale）を返します。 |
| `SetScale(scale: float) -> bool` | 縮尺を設定します。 |
| `GetElevation() -> float \| None` | 高さ（ワールド単位）を返します。 |
| `SetElevation(elevation: float) -> bool` | 高さを設定します。 |
| `GetThickness() -> float \| None` | 厚さ（ワールド単位）を返します。 |
| `SetThickness(thickness: float) -> bool` | 厚さを設定します。 |
| `GetRenderMode() -> int \| None` | レンダリングモード（生のレンダリングモード）を返します。 |
| `GetProjection() -> int \| None` | 投影の方法（生の値）を返します。 |
| `GetStory() -> Story` | デザインレイヤのストーリ。デザインレイヤが属するストーリと、そのストーリ内でのレベル名であるレベルタイプは、それぞれ最大一つです（Storyを参照）。これらを変更するとストーリレベルが更新され、取り消しのためにレイヤとストーリデータが記録され、ストーリに連動するオブジェクト（壁など）が更新されます。レイヤのストーリを返します。レイヤがストーリに属していない場合は無効です。 |
| `GetLevelType() -> str \| None` | レイヤのレベルタイプ。設定されていない場合は空、無効なオブジェクトでは`None`。 |
| `SetLevelType(levelType: str) -> bool` | ストーリ内では、AssociateWithStory(`GetStory()`, levelType)と同様に、レイヤがそのタイプのレベルに移動します。空の場合はレベルタイプを解除します（レイヤのストーリと高さは維持され、ストーリからそのレベルが失われます）。ファイルにまだないレベルタイプは追加されます。デザインレイヤのみ。 |
| `AssociateWithStory(story: Story, levelType: str = '') -> bool` | デザインレイヤを`story`の`levelType`に配置します（空の場合：レイヤの現在のレベルタイプ）。レイヤが以前属していたストーリからは、そのレイヤのレベルが失われます。レイヤは、そのタイプのストーリレベルのオフセット、またはそのタイプの最初のデフォルトのストーリレベルのオフセット、または0に基づくレベルの高さに移動します。ストーリ内の別のレイヤがそのレベルタイプを持つ場合、またはレベルタイプがない場合は失敗します。ファイルにまだないレベルタイプは追加されます。 |
| `DetachFromStory() -> bool` | デザインレイヤをストーリから外します。高さは維持され、ストーリとレベルタイプが解除され、ストーリからそのレベルが失われます。レイヤがストーリに属していない場合は`True`。 |

*シートレイヤのプロパティ*

| メソッド | 説明 |
|---|---|
| `GetDescription() -> str \| None` | 説明（シートのタイトル）を返します。 |
| `SetDescription(description: str) -> bool` | 説明を設定します。 |
| `GetDPI() -> int \| None` | DPIを返します。 |
| `SetDPI(dpi: int) -> bool` | DPIを設定します。 |
| `GetFirstObject() -> Handle` | 内容（最上位オブジェクト）。VectorScriptのFInLayer / NextObjと同様に、図面オブジェクトのみを対象とし、削除したオブジェクトの取り消し用プレースホルダーと、オブジェクトリストの末尾を示す終端はスキップします。空のレイヤでは最初／最後のオブジェクトはヌルです。ForEachObjectはコールバック実行前に次のオブジェクトを取得するため、コールバックで現在のオブジェクトを削除または移動できます。 |
| `GetLastObject() -> Handle` | 最後のオブジェクトを返します。 |
| `ForEachObject(callback: callable(Handle)) -> None` | レイヤの各最上位オブジェクトを渡して`callback`を呼び出します。内容（最上位オブジェクト）。VectorScriptのFInLayer / NextObjと同様に、図面オブジェクトのみを対象とし、削除したオブジェクトの取り消し用プレースホルダーと、オブジェクトリストの末尾を示す終端はスキップします。空のレイヤでは最初／最後のオブジェクトはヌルです。ForEachObjectはコールバック実行前に次のオブジェクトを取得するため、コールバックで現在のオブジェクトを削除または移動できます。 |
| `GetObjects() -> list[Handle]` | オブジェクトを返します。 |
| `GetObjectCount() -> int` | オブジェクト項目の数。 |
| `GetBounds() -> Math.Rect2D \| None` | 境界（最上位オブジェクトの境界）を返します。 |
| `GetContents() -> LayerContents` | 内容を返します（一度の走査でオブジェクト数と境界を取得）。 |
| `GetObjectsOf(type: type) -> object` | レイヤの最上位オブジェクトのうち、クラス`type`のインスタンスであるものを`type`オブジェクトのリストとして返します。例：`layer.GetObjectsOf(api.RectangleObject)`。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`：オブジェクトが有効な場合はTrue（`IsValid()`と同じ）。 |
| `==` | `__eq__(o: Layer) -> bool` | `a == b`：両方のオブジェクトが同じレイヤを参照している場合はTrue。 |
| `!=` | `__ne__(o: Layer) -> bool` | `a != b`：オブジェクトが異なるレイヤを参照している場合はTrue。 |

### StoryLevel

> **完全修飾名:** `api.StoryLevel` · **継承元:** `api.Object`

ストーリの一つのレベル：ストーリの基準高さを基準とした名前付きの高さ（レベルタイプ）で、必要に応じてそのレベルのデザインレイヤを持ちます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `StoryLevel()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `StoryLevel(fLevelType, fElevationOffset, fElevation, fLayerName, fLayer)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fLevelType` | `str` | ストーリ内で一意のレベルタイプ。例："Slab"または"OK-FB"。 |
| `fElevationOffset` | `float` | ストーリの基準高さからの相対値（ワールド単位）。 |
| `fElevation` | `float` | ワールド単位：ストーリの基準高さ + fElevationOffset。 |
| `fLayerName` | `str` | レベルのレイヤ名。レイヤのないレベルでは空。 |
| `fLayer` | `Layer` | ストーリ内でこのレベルタイプを持つデザインレイヤ。存在しない場合は無効。 |

### StoryLevelTemplate

> **完全修飾名:** `api.StoryLevelTemplate` · **継承元:** `api.Object`

デフォルトのストーリレベル（オーガナイザダイアログボックス > ストーリタブ > ストーリレベル初期設定）：ストーリレベルのテンプレート。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `StoryLevelTemplate()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `StoryLevelTemplate(fIndex, fLevelType, fElevationOffset, fLayerName, fScaleFactor, fDefaultWallHeight)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fIndex` | `int` | ストーリレベル初期設定内の1始まりの位置。 |
| `fLevelType` | `str` | このテンプレートから作成されるレベルのレベルタイプ。 |
| `fElevationOffset` | `float` | ストーリの基準高さからの相対値（ワールド単位）。 |
| `fLayerName` | `str` | ストーリの前記号／後記号を含まないレイヤ名。空の場合：レベルにレイヤはありません。 |
| `fScaleFactor` | `float` | レイヤの縮尺（1:fScaleFactor）。 |
| `fDefaultWallHeight` | `float` | ワールド単位。レイヤの壁の高さ。 |

### Story

> **完全修飾名:** `api.Story` · **継承元:** `api.Object`

ストーリ：一定の基準高さにある建物の階。そのレベル（StoryLevel）はストーリの基準高さからの相対的な高さで、それぞれレベルタイプを持ち、必要に応じてデザインレイヤも持ちます。ストーリの基準高さが変わると、そのレイヤとレベルに連動するオブジェクトも追従します。ストーリはファイルのデータであり、図面オブジェクトではありません。ストーリでないハンドルから生成すると、無効なオブジェクトになります（`IsValid()` == `False`）。

取り消し：オーガナイザダイアログボックスのストーリ関連ダイアログボックスと同様に、変更メソッドは変更内容を現在の取り消しイベント（`Document.StartUndoEvent`で開始）に記録します。記録対象は、ストーリデータ、変更・作成・削除するレイヤ、および変更したストーリ、レベル、レイヤに連動して更新されるオブジェクトです。ストーリや、これらのメソッドが作成したレイヤを、`Document.AddAfterSwapObject` / AddBothSwapObjectで再度登録しないでください。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Story(hStory: Handle)` | 既存のストーリ`hStory`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `GetHandle() -> Handle` | ストーリのハンドル。 |
| `IsValid() -> bool` | このオブジェクトが既存のストーリを参照している場合はTrue。 |
| `Create(name: str, elevation: float, affix: str = '', isPrefix: bool = False) -> Story` *静的* | `elevation`（ワールド単位）に、レベルのないストーリを作成します。レベルはAddLevel / AddLevelFromTemplateで追加します。`affix`は、ストーリレベル初期設定からそのストーリ用に作成するレイヤの名前に付ける前記号または後記号です。各ストーリには固有の記号が必要です（大文字小文字を区別せずに比較）。空の記号も一つとみなします。`isPrefix`は新規 ストーリダイアログボックスと同様に渡されますが、Vectorworksには保存されません（UsesPrefixを参照）。`name`が空、63文字を超える、または別のオブジェクトの名前である場合、`affix`が別のストーリで使用されている場合、または別のストーリがその基準高さにある場合は失敗します（無効なオブジェクト）。 |

*識別情報*

| メソッド | 説明 |
|---|---|
| `GetName() -> str \| None` | 名前を返します。 |
| `SetName(name: str) -> bool` | 名前が空、63文字を超える、または別のオブジェクトの名前である場合は失敗します。ストーリの編集ダイアログボックスと同様に、IFCデータ内のストーリ名も変更し、その名前を表示するオブジェクトを更新します。 |
| `GetAffix() -> str \| None` | ストーリレベル初期設定からそのストーリ用に作成するレイヤの名前に付ける前記号または後記号。 |
| `SetAffix(affix: str) -> bool` | 別のストーリが`affix`を使用している場合は失敗します（大文字小文字を区別しないため、大文字小文字だけの変更も失敗します）。既存のレイヤ名は変わりません。 |
| `UsesPrefix() -> bool \| None` | ストーリのレイヤ名が記号で始まるかどうか。Vectorworksはこれを保存せず、各レベルのレイヤ名から推測します。どのレベルにもレイヤがない場合は`True`。 |
| `GetElevation() -> float \| None` | 高さ（ワールド単位）。 |
| `SetElevation(elevation: float, mode: StoryElevationChangeMode = StoryElevationChangeMode.Single) -> bool` | ストーリ、および`mode`に応じてその上／下のストーリを、elevation - `GetElevation()`だけ移動します。移動するストーリのデザインレイヤも一緒に移動します。移動先が移動しないストーリと同じ基準高さになる場合は、変更せずに失敗します。二つのストーリは同じ基準高さを共有できません。 |
| `GetStoryAbove() -> Story` | 基準高さ順で次に上／下にあるストーリ。存在しない場合は無効。 |
| `GetStoryBelow() -> Story` | 下のストーリを返します。 |
| `Delete(deleteLayers: bool = False) -> bool` | ストーリを削除し、このオブジェクトを無効にします。デザインレイヤはストーリとレベルタイプが解除された状態で残ります。ただし、`deleteLayers`で指定した場合は削除されます。対象がファイルのすべてのデザインレイヤである場合、その削除は失敗します。 |
| `GetLevels() -> list[StoryLevel]` | 高さのオフセット順に並べたレベル。 |
| `GetLevel(levelType: str) -> StoryLevel \| None` | このレベルタイプを持つレベル（Vectorworksと同様に大文字小文字を区別せずに比較）。存在しない場合は`None`。 |
| `AddLevel(levelType: str, elevationOffset: float, layerName: str = '', createLayerIfMissing: bool = True, scale: float = 0.0) -> bool` | `levelType`のレベルを`elevationOffset`（ワールド単位、ストーリの基準高さからの相対値）に追加します。`layerName`がなければ、レベルにレイヤはありません。それ以外の場合、レイヤはデザインレイヤ`layerName`です。レベルタイプのない既存のレイヤは、そのレベルの高さでストーリに配置されます。レイヤがない場合、`createLayerIfMissing`が指定されていれば`scale`で作成されます（0：アクティブレイヤの縮尺。アクティブレイヤは変わりません）。ストーリがそのレベルタイプをすでに持つ場合、または`layerName`がシートレイヤ、レベルタイプを持つレイヤ、あるいは別のオブジェクトの名前である場合は失敗します。ファイルにまだないレベルタイプは追加されます。 |
| `AddLevelFromTemplate(index: int) -> bool` | デフォルトのストーリレベル`index`（1始まり。`Document.GetStoryLevelTemplates`を参照）のレベルを、Vectorworksと同じ方法で追加します。テンプレートにレイヤ名がある場合、テンプレートの縮尺と壁の高さを使用して<layer name>-<affix>という名前のレイヤを作成し、アクティブレイヤは変更しません。ストーリがそのレベルタイプをすでに持つ場合は失敗します。 |
| `SetLevelElevationOffset(levelType: str, elevationOffset: float) -> bool` | レベルとそのレイヤを、オブジェクトとともに`elevationOffset`（ワールド単位、ストーリからの相対値）に移動します。 |
| `RemoveLevel(levelType: str, deleteLayer: bool = False) -> bool` | レベルを削除します。レイヤはストーリとレベルタイプが解除された状態で残ります。ただし、`deleteLayer`で指定した場合は削除されます。そのレイヤがファイルの唯一のデザインレイヤである場合、その削除は失敗します。 |
| `GetLayers() -> list[Layer]` | ストーリ内のデザインレイヤ。ファイルのレイヤリスト順。 |
| `GetLayerForLevelType(levelType: str) -> Layer` | ストーリ内でこのレベルタイプを持つデザインレイヤ。存在しない場合は無効。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`：オブジェクトが有効な場合はTrue（`IsValid()`と同じ）。 |
| `==` | `__eq__(o: Story) -> bool` | `a == b`：両方のオブジェクトが同じストーリを参照している場合はTrue。 |
| `!=` | `__ne__(o: Story) -> bool` | `a != b`：オブジェクトが異なるストーリを参照している場合はTrue。 |

### Document

> **完全修飾名:** `api.Document` · **継承元:** `api.Object`

アクティブなVectorworksファイルに対する状態を保持しないファサード。選択内容、レイヤ、ストーリ、クラス、オブジェクト、ビュー、単位、デフォルト属性、設定にアクセスできます。必要に応じて生成してください（呼び出し間で状態は保持されません）：

```python
import api

doc = api.Document()
if api.Document.IsOpen():                   # there is an active document
    for h in doc.GetSelection():               # iterate the current selection
        rect = api.Document.As(api.RectangleObject, h)
        if rect:
            rect.SetSize(1.0, 2.0)
```

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Document()` | アクティブファイルに対する状態を保持しないファサード（呼び出し間で状態は保持されません）。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `IsOpen() -> bool` *静的* | 現在、開かれたアクティブファイルがあるかどうか。他のすべてのメソッドには、これが`True`であることが必要です。 |

*設定*

| メソッド | 説明 |
|---|---|
| `Display() -> DisplaySettings` | 表示設定（`DisplaySettings`）。 |
| `Editing() -> EditingSettings` | 編集とセッションの設定（`EditingSettings`）。 |
| `Snapping() -> SnapSettings` | スナップ（スマートカーソル）の設定（`SnapSettings`）。 |
| `Grid() -> GridSettings` | グリッド設定（`GridSettings`）。 |
| `StackLayers() -> StackLayersSettings` | 統合ビュー（スタックレイヤ）の設定（`StackLayersSettings`）。 |
| `PrimaryUnits() -> UnitSettings` | ファイルの主寸法単位（`UnitSettings`）。 |
| `SecondaryUnits() -> UnitSettings` | ファイルの補助寸法単位（`UnitSettings`）。 |
| `TextDefaults() -> TextDefaults` | 新しい文字列オブジェクトのデフォルトの文字設定（`TextDefaults`）。 |
| `DefaultAttributes() -> DefaultAttributes` | 新しいオブジェクトのデフォルト属性（`DefaultAttributes`）。 |

*選択*

| メソッド | 説明 |
|---|---|
| `GetSelectionCount() -> int` | Vectorworksの編集コマンドと同じ範囲で選択内容を返します。対象は作業レイヤのみです（アクティブレイヤ、およびレイヤオプションで変更が許可されている他のレイヤ）。選択内容を編集する処理には、これらを使用してください。 |
| `HasSelection() -> bool` | 少なくとも一つのオブジェクトが選択されている場合はTrue。 |
| `GetFirstSelected() -> Handle` | 最初の選択オブジェクトを返します。 |
| `GetSelection(descend: Descend = Descend.None_) -> list[Handle]` | `descend`に応じた選択内容を返します。 |
| `ForEachSelected(callback: callable(Handle), descend: Descend = Descend.None_) -> None` | 選択されている各オブジェクトを渡して`callback`を呼び出します。Vectorworksの編集コマンドと同じ範囲で選択内容を返します。対象は作業レイヤのみです（アクティブレイヤ、およびレイヤオプションで変更が許可されている他のレイヤ）。選択内容を編集する処理には、これらを使用してください。 |
| `GetSelectionBounds() -> Math.Rect2D \| None` | 選択内容の境界を返します。 |
| `GetSelectionCountOnAllLayers() -> int` | 同様の処理ですが、図面のすべてのレイヤを対象とします。ユーザーがレイヤを切り替えてもオブジェクトは選択状態のままなので、これらは選択内容全体を返します。読み取り専用です。以下の編集操作は、引き続き作業レイヤを対象とします。 |
| `GetSelectionOnAllLayers(descend: Descend = Descend.None_) -> list[Handle]` | `descend`に応じて、すべてのレイヤの選択内容を返します。 |
| `ForEachSelectedOnAllLayers(callback: callable(Handle), descend: Descend = Descend.None_) -> None` | すべてのレイヤで選択されている各オブジェクトを渡して`callback`を呼び出します。同様の処理ですが、図面のすべてのレイヤを対象とします。ユーザーがレイヤを切り替えてもオブジェクトは選択状態のままなので、これらは選択内容全体を返します。読み取り専用です。以下の編集操作は、引き続き作業レイヤを対象とします。 |
| `GetSelectionBoundsOnAllLayers() -> Math.Rect2D \| None` | すべてのレイヤの選択内容の境界を返します。 |
| `IsSelected(h: Handle) -> bool` | オブジェクト`h`が選択されている場合はTrue。 |
| `Select(h: Handle, select: bool = True) -> bool` | オブジェクトを選択します（`select=False`の場合は選択解除）。対象は`h`です。 |
| `Select(object: PrimitiveObject, select: bool = True) -> bool` | オブジェクトを選択します（`select=False`の場合は選択解除）。対象は`object`です。 |
| `Deselect(h: Handle) -> bool` | オブジェクト`h`の選択を解除します。 |
| `Select(objects: list[Handle]) -> int` | オブジェクト`objects`を選択内容に追加します。選択された数を返します。 |
| `SetSelection(objects: list[Handle]) -> int` | 選択内容を設定します（選択内容を置き換えます）。 |
| `SelectAll() -> None` | すべてのオブジェクトを選択します（編集 > すべてを選択と同様）。 |
| `DeselectAll() -> None` | 選択を解除します。 |
| `GetSelectionOf(type: type, descend: Descend = Descend.None_) -> object` | 選択されたオブジェクトのうち、クラス`type`のインスタンスであるものを`type`オブジェクトのリストとして返します。例：`doc.GetSelectionOf(api.Line2DObject)`。 |

*選択内容に対する操作*

| メソッド | 説明 |
|---|---|
| `MoveSelection(offset: Math.Point2D) -> bool` | 選択されたオブジェクトを`offset`（ワールド単位）だけ移動します。 |
| `RotateSelection(angle: float, center: Math.Point2D) -> bool` | 選択されたオブジェクトを`angle`（ラジアン、反時計回り）だけ、`center`を中心に回転します。 |
| `ScaleSelection(scaleX: float, scaleY: float, center: Math.Point2D) -> bool` | 選択されたオブジェクトを`scaleX` / `scaleY`の倍率で、`center`を中心に拡大縮小します。 |
| `DuplicateSelection(offset: Math.Point2D = Math.Point2D()) -> bool` | 選択されたオブジェクトを複製し、複製を`offset`だけずらします。 |
| `GroupSelection() -> Handle` | 選択されたオブジェクトをグループ化します。新しいグループのハンドルを返します（何も選択されていない場合はヌル）。 |
| `DeleteSelection(useUndo: bool = True) -> int` | 選択されたオブジェクトを削除します（`useUndo`が`False`でなければ、取り消し用に記録されます）。削除された数を返します。 |
| `SetSelectionClass(theClass: ClassAttributes, useClassAttributes: bool = False) -> bool` | 選択内容のクラスを設定します。 |

*オブジェクト*

| メソッド | 説明 |
|---|---|
| `ForEachObject(what: Traverse, callback: callable(Handle), descend: Descend = Descend.None_) -> None` | `what`に一致するすべてのオブジェクトをたどります（Traverseを参照）。`descend`は、グループ、シンボル、ビューポートなどのコンテナ内を走査するかどうかを制御します（Descendを参照）。コールバックは同期的に実行されます。 |
| `GetObjects(what: Traverse, descend: Descend = Descend.None_) -> list[Handle]` | `what`に一致するすべてのオブジェクトを収集します（ForEachObjectを参照）。 |
| `GetLayerContents(what: Traverse) -> dict[Handle, LayerContents]` | `what`がたどる最上位オブジェクトの数と境界を、レイヤハンドルをキーとして返します。該当するオブジェクトのないレイヤは含まれません。 |
| `GetObjectsAtPoint(pt: Math.Point2D, radius: float, what: Traverse = Traverse.Visible, descend: Descend = Descend.None_) -> list[Handle]` | 半径`radius`ワールド単位の範囲で、`pt`からその形状までの距離が範囲内にあるオブジェクトを収集します（クリックのヒットテストと同様）。 |
| `GetObjectsInCriteria(criteria: str) -> list[Handle]` | Vectorworksの検索条件文字列（Vectorscript／検索条件ダイアログと同じ構文）に一致するオブジェクトを収集します。例："(T=RECT)"はすべての四角形、"(C='My Class')"はクラス'My Class'内のすべてのオブジェクト。 |
| `GetCriteriaError(criteria: str) -> str \| None` | `criteria`がコンパイルできない理由（その場合、GetObjectsInCriteriaは何も見つけません）。コンパイルできる場合は`None`。 |
| `GetObjectType(h: Handle) -> ObjectType` *静的* | オブジェクトタイプ（幾何学的／構造的オブジェクトの種類）。型付きクラスがあるのはObjectTypeの一部のみです。 |
| `AttributesOf(h: Handle) -> ObjectAttributes` *静的* | 任意のオブジェクトのグラフィック属性（線、面、マーカー、ドロップシャドウ、クラスなど）。 |
| `ClassOf(h: Handle) -> ClassAttributes` *静的* | オブジェクト`h`のクラス。 |
| `LayerOf(h: Handle) -> Layer` *静的* | 最終的にそのオブジェクトを含むレイヤ（レイヤが見つかるまで、グループ、シンボルなどの階層を上へたどります）。 |
| `FindByName(name: str) -> Handle` | 識別情報によるオブジェクトの検索。一致するオブジェクトがない場合はヌルを返します。 |
| `FindByUuid(uuid: str) -> Handle` | 永続UUID`uuid`を持つオブジェクト。一致するものがない場合はヌルハンドル。 |
| `FindByIndex(index: int) -> Handle` | 内部インデックス`index`を持つオブジェクト。一致するものがない場合はヌルハンドル。 |
| `GetUuid(h: Handle) -> str \| None` | オブジェクトの永続UUID。保存／読み込みを経ても変わりません。 |
| `As(type: type, h: Handle) -> object` *静的* | ハンドル`h`を型付きオブジェクトとして返します。クラス`type`（例：`api.ArcObject`）のインスタンスを`type.Is(h)`の場合に返し、それ以外は`None`を返します。例：`arc = api.Document.As(api.ArcObject, h)`。 |
| `GetObjectsOf(type: type, what: Traverse = Traverse.All, descend: Descend = Descend.None_) -> object` | `what`に一致するオブジェクトのうち、クラス`type`のインスタンスであるすべてのものを`type`オブジェクトのリストとして返します。例：`doc.GetObjectsOf(api.RectangleObject)`。 |

*レイヤ*

| メソッド | 説明 |
|---|---|
| `GetActiveLayer() -> Layer` | アクティブレイヤを返します。 |
| `SetActiveLayer(layer: Layer) -> bool` | アクティブレイヤを設定します。 |
| `FindLayer(name: str) -> Layer` | `name`という名前のレイヤ。存在しない場合は無効な`Layer`。 |
| `ForEachLayer(callback: callable(Layer)) -> None` | ファイルの各レイヤを渡して`callback`を呼び出します。 |
| `GetLayers() -> list[Layer]` | レイヤを返します。 |
| `GetLayers(type: LayerType) -> list[Layer]` | `type`に応じたレイヤを返します。 |
| `CreateDesignLayer(name: str, scale: float = 1.0) -> Layer` | `name`という名前のデザインレイヤを、縮尺1:`scale`で作成します。 |
| `CreateSheetLayer(name: str) -> Layer` | `name`という名前のシートレイヤを作成します。 |
| `GetLayerOptions() -> VisibilityOptions \| None` | レイヤオプションを返します。 |
| `SetLayerOptions(options: VisibilityOptions) -> bool` | レイヤオプションを設定します。 |
| `GetActiveLayerScale() -> float \| None` | アクティブレイヤの縮尺を返します。 |

*ストーリ*

| メソッド | 説明 |
|---|---|
| `GetStories() -> list[Story]` | ファイルのストーリを基準高さ順（低い順）で返します。取り消しの動作についてもStoryを参照してください。 |
| `FindStory(name: str) -> Story` | `name`という名前のストーリ。存在しない場合は無効。 |
| `CreateStory(name: str, elevation: float, affix: str = '', isPrefix: bool = False) -> Story` | `name`という名前のストーリを`elevation`に作成します（`Story.Create`と同じ）。`affix`は各レベルのレイヤ名に付加されます。名前が空、長すぎる、または使用済みの場合、前記号／後記号が使用済みの場合、または基準高さが使用済みの場合は失敗します（無効なオブジェクト）。 |
| `GetLevelTypes() -> list[str]` | レベルタイプ（オーガナイザダイアログボックス > ストーリタブ > レベルタイプ）：ストーリレベルの名前をファイル内の順序で返します。名前は最大63文字です。Vectorworksは大文字小文字を区別せずに比較します。ストーリのメソッドは、ファイルまたはストーリですでに使用されている表記を維持します。変更は取り消せます。 |
| `AddLevelType(name: str) -> bool` | 名前がすでに存在する場合は失敗します（大文字小文字を区別しません）。 |
| `RenameLevelType(oldName: str, newName: str) -> bool` | レイヤ、ストーリレベル、ストーリレベル初期設定、ストーリ連動オブジェクトのレベルタイプ名も変更します。`newName`がすでに存在する場合は失敗します（大文字小文字を区別しないため、大文字小文字だけの変更も失敗します）。オブジェクトのストーリ境界設定や水平断面ビューポートのレベルタイプは、取り消しでは元に戻りません。レベルタイプダイアログボックスと同様に、Vectorworksはこれらを記録せずに名前を変更するためです。代わりに、名前を元に戻してください。 |
| `DeleteLevelType(name: str) -> bool` | レベルタイプダイアログボックスと同様に、このレベルタイプを持つレイヤとストーリレベル初期設定からはそのタイプが解除されます。ストーリレベルには残ります。 |
| `GetStoryLevelTemplates() -> list[StoryLevelTemplate]` | ストーリレベル初期設定（オーガナイザダイアログボックス > ストーリタブ > ストーリレベル初期設定）。ストーリレベルのテンプレートです。インデックスは1始まりで、GetStoryLevelTemplatesはインデックス順に返します。変更は取り消せます。 |
| `AddStoryLevelTemplate(levelType: str, elevationOffset: float, layerName: str = '', scaleFactor: float = 0.0, defaultWallHeight: float = 0.0) -> int \| None` | デフォルトのストーリレベルを追加し、そのインデックスを返します。Vectorworksは先頭（インデックス1）に挿入します。`scaleFactor`が0の場合、アクティブレイヤの縮尺を使用します。同じレベルタイプと高さのオフセットを持つデフォルトのストーリレベルがある場合は失敗します。ファイルにまだないレベルタイプは追加されます。 |
| `DeleteStoryLevelTemplate(index: int) -> bool` | `index`のデフォルトのストーリレベルを削除します。 |
| `ResetDefaultStoryLevels(deleteExisting: bool) -> bool` | Vectorworksのデフォルトのストーリレベルとレベルタイプを再度追加します（ファイルにあるレベルタイプは維持されます）。`deleteExisting`は、現在のストーリレベル初期設定を先に削除します。それ以外の場合は既存のものにデフォルトを追加するため、ストーリレベル初期設定の項目が重複することがあります。 |

*クラス*

| メソッド | 説明 |
|---|---|
| `GetActiveClass() -> ClassAttributes` | アクティブクラスを返します。 |
| `SetActiveClass(theClass: ClassAttributes) -> bool` | アクティブクラスを設定します。 |
| `FindClass(name: str) -> ClassAttributes` | `name`という名前のクラス。存在しない場合は無効な`ClassAttributes`。 |
| `CreateClass(name: str) -> ClassAttributes` | `name`という名前のクラスを作成します（または既存のクラスを返します）。 |
| `GetClasses(includeGuestClasses: bool = False) -> list[ClassAttributes]` | `includeGuestClasses`に応じたクラスを返します。 |
| `GetClassOptions() -> VisibilityOptions \| None` | クラスオプションを返します。 |
| `SetClassOptions(options: VisibilityOptions) -> bool` | クラスオプションを設定します。 |

*コンテナ*

| メソッド | 説明 |
|---|---|
| `GetDrawingHeader() -> Handle` | 図面のルートオブジェクト。直接必要になることはほとんどありません。 |
| `GetDefaultContainer() -> Handle` | 新しく作成されたオブジェクトを受け入れるコンテナ（アクティブレイヤ、または編集中のグループ／シンボル定義）。 |
| `IsInsideGroup() -> bool \| None` | ユーザーが現在グループの内容を編集中（「グループに入る」編集セッション中）の場合は`True`。 |
| `GetEditedGroup() -> Handle` | 現在編集中のグループ（グループを編集していない場合はヌル）。 |
| `GetActiveSymbolDefinition() -> Handle` | 現在編集中のシンボル定義（シンボル定義を編集していない場合はヌル）。 |
| `SetActiveSymbolDefinition(hSymbolDefinition: Handle) -> bool` | アクティブなシンボル定義を設定します。現在編集中のシンボル定義です（シンボル定義を編集していない場合はヌル）。 |

*ビューと用紙*

| メソッド | 説明 |
|---|---|
| `GetPageBounds() -> Math.Rect2D \| None` | 図面の印刷可能な用紙を覆う長方形。ワールド座標。 |

*ユーザー原点*

| メソッド | 説明 |
|---|---|
| `GetUserOrigin() -> Math.Point2D \| None` | ユーザー座標系で(0, 0)として表示されるワールド上の点。 |
| `SetUserOrigin(origin: Math.Point2D) -> bool` | ユーザー原点を設定します。ユーザー座標系で(0, 0)として表示されるワールド上の点です。 |
| `GetViewCenter() -> Math.Point2D \| None` | 現在のビューの中心点。ワールド座標。 |
| `SetViewCenter(center: Math.Point2D) -> bool` | ビューの中心を設定します。現在のビューの中心点で、ワールド座標です。 |

*ズーム倍率*

| メソッド | 説明 |
|---|---|
| `SetZoom(zoomFactor: float) -> bool` | 1.0 = 100 %、2.0 = 200 %（画面上で二倍の大きさ）、0.5 = 50 %。 |
| `IsPlanRotated() -> bool \| None` | ビューの平面回転がゼロでない場合はTrue。 |
| `GetPlanRotationAngle() -> float \| None` | 平面の回転角度（ラジアン、反時計回り）を返します。 |
| `Redraw(area: Math.Rect2D) -> bool` | ワールド座標の長方形`area`を再描画が必要な領域としてマークします。API自体で行わなかった編集の後に呼び出してください。 |

*単位*

| メソッド | 説明 |
|---|---|
| `WorldToUnits(worldLength: float) -> float \| None` | APIが使用する内部ワールド単位と、UIに表示されるファイルの主単位との間で変換します。 |
| `UnitsToWorld(unitsLength: float) -> float \| None` | `unitsLength`をファイルの単位からワールド単位に変換します。APIが使用する内部ワールド単位と、UIに表示されるファイルの主単位との間で変換します。 |

*取り消し*

| メソッド | 説明 |
|---|---|
| `StartUndoEvent(method: UndoMethod = UndoMethod.SwapObjects, isRevertible: bool = False) -> None` | 取り消しイベントを開始し、その方式（通常は`UndoMethod.SwapObjects`）を選択します。変更を行う前に呼び出してください。`isRevertible`は、`RevertUndoEvent()`でイベントを元に戻せるようにします（上記参照）。その場合、取り消しがオフ（取り消し段階がゼロ）でもVectorworksはイベントを構築し、そのようなイベントは終了時に破棄します。これはSwapObjectsとReplaceSelectionに適用されます。`UndoMethod.None_`はイベントを開始しません。 |
| `NameUndoEvent(name: str) -> None` | 現在の取り消しイベントに名前を付け、編集メニューに「取り消し <name>」として表示します。イベント内で、変更前に呼び出してください。 |
| `EndUndoEvent() -> None` | 現在の取り消しイベントを直ちに終了します。Vectorworksは操作の完了時にも自動的に終了します。 |
| `RevertUndoEvent() -> bool` | 構築中のイベントを元に戻します。記録された内容を取り消し、取り消しリストから削除します（上記参照）。`EndUndoEvent()`の代わりに、`isRevertible=True`を指定して開始したイベントに対して呼び出してください。構築中のイベントがない場合は`False`を返します。それ以外の場合は`True`を返し、イベントを元に戻せなかった場合も同様です（`isRevertible=True`を指定せずに開始したイベントは元に戻せません）。実行中のスクリプトの取り消しを、そのスクリプトを実行するアプリケーションが管理している間は、何もせず`False`を返します。 |
| `IsBuildingUndoEvent() -> bool` | 取り消しイベントが構築中、すなわち開始済みでまだ終了していないかどうか。StartUndoEventで開始したイベントだけでなく、実行中のコマンドやスクリプトのためにVectorworksが開始したイベント、およびイベントが開かれていなかったために取り消しを記録するAPI呼び出しが開始した非表示のイベントでも、`True`です。 |
| `AddAfterSwapObject(object: Handle) -> bool` | 取り消し用のオブジェクト登録。`UndoMethod.SwapObjects`（またはReplaceSelection）イベント内でのみ意味があります。作成直後に図面へ追加したオブジェクトを登録すると、取り消しによって削除されます。現在選択されているすべてのオブジェクトを登録するにはヌルを渡します（例：DuplicateSelectionの直後）。 |
| `AddBothSwapObject(object: Handle) -> bool` | 変更しようとしているオブジェクトを登録すると、取り消しによって変更前の状態に復元されます。取り消し記録にはコピーが保存されます。変更前に呼び出してください。現在選択されているすべてのオブジェクトを対象にするにはヌルを渡します。 |
| `AddBeforeSwapObject(object: Handle) -> bool` | 削除しようとしているオブジェクトを登録します。非推奨：`Delete()`が削除を取り消し用に記録するため、通常は必要ありません。選択されているすべてのオブジェクトを対象にするにはヌルを渡します。 |
| `AddBeforeMoveObject(object: Handle) -> bool` | `PrimitiveObject.MoveToContainer`でコンテナ（レイヤ、グループ、シンボル定義）から別のコンテナへ移動するオブジェクトを登録すると、取り消しによって元の場所に戻ります。移動前にAddBeforeMoveObject、移動後にAddAfterMoveObjectを、どちらもそのオブジェクトを渡して呼び出します。これらはオブジェクトの状態ではなく、図面内の位置を記録します。そのイベントでは、移動するオブジェクトについてこの二つのみを記録してください（一つのイベント内で同じオブジェクトにAddBothSwapObjectを組み合わせる手順は検証されていません）。オブジェクトのその他の変更は、それ専用の取り消しイベントで行ってください。まだ図面にない新しいオブジェクト（たとえばブール演算の結果）は、代わりにMoveToContainerで挿入し、AddAfterSwapObjectで登録します。現在選択されているすべてのオブジェクトを対象にするにはヌルを渡します。 |
| `AddAfterMoveObject(object: Handle) -> bool` | 別のコンテナへ移動した直後に、`object`を取り消し用に登録します。`PrimitiveObject.MoveToContainer`でコンテナ（レイヤ、グループ、シンボル定義）から別のコンテナへ移動するオブジェクトを登録すると、取り消しによって元の場所に戻ります。移動前にAddBeforeMoveObject、移動後にAddAfterMoveObjectを、どちらもそのオブジェクトを渡して呼び出します。これらはオブジェクトの状態ではなく、図面内の位置を記録します。そのイベントでは、移動するオブジェクトについてこの二つのみを記録してください（一つのイベント内で同じオブジェクトにAddBothSwapObjectを組み合わせる手順は検証されていません）。オブジェクトのその他の変更は、それ専用の取り消しイベントで行ってください。まだ図面にない新しいオブジェクト（たとえばブール演算の結果）は、代わりにMoveToContainerで挿入し、AddAfterSwapObjectで登録します。現在選択されているすべてのオブジェクトを対象にするにはヌルを渡します。 |

<a id="enumerations"></a>

## 列挙型

### Traverse

> **完全修飾名:** `api.Traverse` · **種類:** `IntEnum`

ファイルの走査でたどるオブジェクトの集合。`Document.ForEachObject` / GetObjects / GetObjectsAtPointに渡します。

| メンバー | 値 | 説明 |
|---|---|---|
| `Selected` | `0` | 現在選択されている最上位オブジェクトのみ。 |
| `Editable` | `1` | 表示され、編集可能なレイヤとクラス上にある、ロックされていないオブジェクト。 |
| `Visible` | `2` | 現在画面上に描画されているオブジェクト（表示レイヤ + 表示クラス）。 |
| `Drawing` | `3` | リソースを除く、図面（すべてのレイヤ）のすべてのオブジェクト。 |
| `SymbolDefinitions` | `4` | シンボル定義のみ（リソースマネージャ内の再利用可能なテンプレート）。 |
| `SelectedAndEditable` | `5` | 編集可能なレイヤ上で、選択され、表示されている、ロックされていないオブジェクト。 |
| `All` | `6` | すべての図面オブジェクトに加え、シンボル定義とその内容。 |
| `AllAndResources` | `7` | Allと同様ですが、リソースオブジェクト（ハッチング、グラデーション、シンボル定義など）も含みます。 |

### Descend

> **完全修飾名:** `api.Descend` · **種類:** `IntFlag`（メンバーは`|`で組み合わせます）

コンテナオブジェクト（グループ、シンボル、ビューポートなど）の内部をどの深さまで走査するか。値はビットフラグです。複数の種類のコンテナを走査するには、`|`でメンバーを組み合わせます。例：`api.Descend.Groups | api.Descend.Viewports`。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` | 最上位オブジェクトのみをたどり、コンテナの内部には入りません。 |
| `Groups` | `32` | グループの内部を走査します。 |
| `All` | `64` | すべての種類のコンテナ（グループ、シンボル、プラグインオブジェクトなど）の内部を走査します。 |
| `Viewports` | `128` | ビューポート（シートレイヤビューポート）の内部を走査します。 |
| `AuxiliaryLists` | `256` | たどったオブジェクトに付属する補助オブジェクトを含めます。 |

### LayerType

> **完全修飾名:** `api.LayerType` · **種類:** `IntEnum`

レイヤの種類。

| メンバー | 値 | 説明 |
|---|---|---|
| `Unknown` | `0` |  |
| `Design` | `1` | ワールド座標のデザインレイヤ（通常の描画面）。 |
| `Sheet` | `2` | シートレイヤ（印刷可能なページ。ビューポートを格納）。 |
| `GuestDesign` | `3` | 別のファイルから取り込んだ／参照したデザインレイヤ。 |

### LayerVisibility

> **完全修飾名:** `api.LayerVisibility` · **種類:** `IntEnum`

レイヤの表示状態（ナビゲーションパレットに表示されるもの）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Invisible` | `-1` | 非表示。 |
| `Normal` | `0` | 通常表示。 |
| `Grayed` | `2` | 表示されますが、アクティブレイヤでないことを示すためにグレイで描画されます。 |

### VisibilityOptions

> **完全修飾名:** `api.VisibilityOptions` · **種類:** `IntEnum`

アクティブでないレイヤまたはクラスの表示方法。`Document.SetLayerOptions`と`Document.SetClassOptions`で使用します。

| メンバー | 値 | 説明 |
|---|---|---|
| `ActiveOnly` | `1` | アクティブなレイヤ／クラスのみを表示します。 |
| `GrayOthers` | `2` | 他をグレイ表示します（編集不可、スナップ不可）。 |
| `ShowOthers` | `3` | 他を通常表示します（表示のみ、編集不可、スナップ不可）。 |
| `ShowSnapOthers` | `4` | 他を通常表示し、スナップを許可します（編集は不可）。 |
| `ShowSnapModifyOthers` | `5` | 他を通常表示し、スナップと編集を許可します。 |
| `GraySnapOthers` | `6` | 他をグレイ表示しますが、スナップは許可します。 |

### StoryElevationChangeMode

> **完全修飾名:** `api.StoryElevationChangeMode` · **種類:** `IntEnum`

`Story.SetElevation`が移動するストーリ（ストーリの高さ変更ダイアログボックスの選択肢）。移動するすべてのストーリは同じ距離だけ移動し、そのデザインレイヤも一緒に移動します。

| メンバー | 値 | 説明 |
|---|---|---|
| `Single` | `0` | このストーリのみ。 |
| `CurrentAndAbove` | `1` | このストーリと、それより上のすべてのストーリ。 |
| `CurrentAndBelow` | `2` | このストーリと、それより下のすべてのストーリ。 |
| `All` | `3` | ファイルのすべてのストーリ。 |

### UndoMethod

> **完全修飾名:** `api.UndoMethod` · **種類:** `IntEnum`

`Document.StartUndoEvent`に渡す取り消し方式。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` | その操作の取り消しを無効にし、取り消しテーブルを消去します（使用は最小限にしてください）。 |
| `ReplaceSelection` | `17` | 現在の選択内容を記憶し、取り消しで復元します。 |
| `SwapObjects` | `21` | オブジェクト単位の取り消し：作成／変更／削除するオブジェクトを登録します。通常の選択肢です。 |

### AngularUnit

> **完全修飾名:** `api.AngularUnit` · **種類:** `IntEnum`

角度の表示単位（`UnitSettings.GetAngularUnit`）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Degrees` | `0` |  |
| `Radians` | `1` |  |
| `Gradians` | `2` |  |

### TextJustification

> **完全修飾名:** `api.TextJustification` · **種類:** `IntEnum`

新しい文字の水平方向の揃え（`TextDefaults`）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Left` | `1` |  |
| `Center` | `2` |  |
| `Right` | `3` |  |

### TextVerticalAlignment

> **完全修飾名:** `api.TextVerticalAlignment` · **種類:** `IntEnum`

新しい文字の垂直方向の揃え（`TextDefaults`）。

| メンバー | 値 | 説明 |
|---|---|---|
| `TopOfBox` | `1` |  |
| `TopBaseline` | `2` |  |
| `CenterOfBox` | `3` |  |
| `BottomBaseline` | `4` |  |
| `BottomOfBox` | `5` |  |

### TextLineSpacing

> **完全修飾名:** `api.TextLineSpacing` · **種類:** `IntEnum`

新しい文字の行間（`TextDefaults`）。`Custom`は`TextDefaults.GetLeading`の行送りを使用します。

| メンバー | 値 | 説明 |
|---|---|---|
| `Custom` | `0` | `TextDefaults.GetLeading`を参照してください。 |
| `Single` | `2` |  |
| `OneAndHalf` | `3` |  |
| `Double` | `4` |  |

---

[一覧に戻る](README.md) · [先頭に戻る](#documentaccess--document-layers-stories-and-preferences)
