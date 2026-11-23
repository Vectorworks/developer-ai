[English](../../PythonAPI/v2027.2/ObjectsLandmark.md) • [Deutsch](../../PythonAPI.de/v2027.2/ObjectsLandmark.md) • **日本語**

<a id="objectslandmark--plants-site-models-hardscapes-and-other-landscape-objects"></a>

# ObjectsLandmark — 植栽、地形モデル、舗床、その他のランドスケープオブジェクト

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

Landmarkのプラグインオブジェクトのクラスです。`LandmarkObject`は共通の基底クラスです（汎用のパラメータアクセス）。個別のクラスは、`PlantObject`（"Plant"）、`LandscapeAreaObject`（"Landscape Area"）、`SiteModelObject`（"DTM6"、現況と計画の面を持つ地形モデル）、`SiteModifierObject`（"Site Modifiers"）、`StakeObject`（"Stake Object"）、`HardscapeObject`（"Hardscape"）、`PropertyLineObject`（"Property Line"）、`ExistingTreeObject`（"Existing Tree"）です。

すべてのLandmarkオブジェクトはプラグインオブジェクトで、レコードのユニバーサル名で区別します。`Is(h)`はその名前を判定し、`Create(...)`はアクティブレイヤ／コンテナに新しいインスタンスを作成します。ゲッターはオブジェクトが無効な場合やパラメータがない場合に`None`を返し、セッターは成功時に`True`を返します。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [LandmarkObject](#landmarkobject)
  - [PlantObject](#plantobject)
    - [PlantObject.Config](#plantobjectconfig)
    - [PlantObject.TagDisplay](#plantobjecttagdisplay)
  - [LandscapeAreaObject](#landscapeareaobject)
    - [LandscapeAreaObject.PlantDisplay2D](#landscapeareaobjectplantdisplay2d)
    - [LandscapeAreaObject.DrawingMode](#landscapeareaobjectdrawingmode)
    - [LandscapeAreaObject.AreaUnits](#landscapeareaobjectareaunits)
  - [SiteModelObject](#sitemodelobject)
    - [SiteModelObject.Display2D](#sitemodelobjectdisplay2d)
    - [SiteModelObject.Display3D](#sitemodelobjectdisplay3d)
  - [SiteModifierObject](#sitemodifierobject)
    - [SiteModifierObject.Config](#sitemodifierobjectconfig)
    - [SiteModifierObject.ApplyTo](#sitemodifierobjectapplyto)
  - [StakeObject](#stakeobject)
    - [StakeObject.Mode](#stakeobjectmode)
    - [StakeObject.SiteModel](#stakeobjectsitemodel)
  - [HardscapeObject](#hardscapeobject)
    - [HardscapeObject.Mode3D](#hardscapeobjectmode3d)
  - [PropertyLineObject](#propertylineobject)
    - [PropertyLineObject.AreaUnits](#propertylineobjectareaunits)
  - [ExistingTreeObject](#existingtreeobject)
    - [ExistingTreeObject.Origin](#existingtreeobjectorigin)
    - [ExistingTreeObject.TreeProtection](#existingtreeobjecttreeprotection)
    - [ExistingTreeObject.Condition](#existingtreeobjectcondition)
    - [ExistingTreeObject.SULE](#existingtreeobjectsule)
    - [ExistingTreeObject.Significance](#existingtreeobjectsignificance)
    - [ExistingTreeObject.Action](#existingtreeobjectaction)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`LandmarkObject`](#landmarkobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Landmarkプラグインオブジェクトのクラス（植栽、ランドスケープエリア、地形モデル、造成図形、レベルオブジェクト、舗床、境界線、既存樹木）に共通する基底クラスです。 |
| [`PlantObject`](#plantobject) | クラス | [`LandmarkObject`](#landmarkobject) | Landmarkプラグインの植栽プラグインオブジェクトです（ユニバーサル名は"Plant"）。 |
| [`PlantObject.Config`](#plantobjectconfig) | IntEnum（入れ子） |  | 構成と表示 |
| [`PlantObject.TagDisplay`](#plantobjecttagdisplay) | IntEnum（入れ子） |  | 植栽ラベルの表示位置。 |
| [`LandscapeAreaObject`](#landscapeareaobject) | クラス | [`LandmarkObject`](#landmarkobject) | Landmarkプラグインのランドスケープエリアプラグインオブジェクトです（ユニバーサル名は"Landscape Area"）。 |
| [`LandscapeAreaObject.PlantDisplay2D`](#landscapeareaobjectplantdisplay2d) | IntEnum（入れ子） |  | ランドスケープエリアの植栽の2D表示方法。 |
| [`LandscapeAreaObject.DrawingMode`](#landscapeareaobjectdrawingmode) | IntEnum（入れ子） |  | オブジェクトをランドスケープエリアとして描画するか、生け垣として描画するか。 |
| [`LandscapeAreaObject.AreaUnits`](#landscapeareaobjectareaunits) | IntEnum（入れ子） |  | ランドスケープエリアの面積の表示単位。 |
| [`SiteModelObject`](#sitemodelobject) | クラス | [`LandmarkObject`](#landmarkobject) | Landmarkプラグインの地形モデルプラグインオブジェクトです（ユニバーサル名は"DTM6"）。 |
| [`SiteModelObject.Display2D`](#sitemodelobjectdisplay2d) | IntEnum（入れ子） |  | 2D／3D表示の選択 |
| [`SiteModelObject.Display3D`](#sitemodelobjectdisplay3d) | IntEnum（入れ子） |  | 地形モデルの3D表示の内容。 |
| [`SiteModifierObject`](#sitemodifierobject) | クラス | [`LandmarkObject`](#landmarkobject) | Landmarkプラグインの造成図形プラグインオブジェクトです（ユニバーサル名は"Site Modifiers"）。 |
| [`SiteModifierObject.Config`](#sitemodifierobjectconfig) | IntEnum（入れ子） |  | 造成図形の変形方式です（"Config"）。 |
| [`SiteModifierObject.ApplyTo`](#sitemodifierobjectapplyto) | IntEnum（入れ子） |  | 造成図形が適用される地形モデルの面。 |
| [`StakeObject`](#stakeobject) | クラス | [`LandmarkObject`](#landmarkobject) | Landmarkプラグインのレベルオブジェクトプラグインオブジェクトです（ユニバーサル名は"Stake Object"）。 |
| [`StakeObject.Mode`](#stakeobjectmode) | IntEnum（入れ子） |  | 地形モデルに対するレベルオブジェクトの役割。 |
| [`StakeObject.SiteModel`](#stakeobjectsitemodel) | IntEnum（入れ子） |  | レベルオブジェクトが参照する地形モデルの面。 |
| [`HardscapeObject`](#hardscapeobject) | クラス | [`LandmarkObject`](#landmarkobject) | Landmarkプラグインの舗床プラグインオブジェクトです（ユニバーサル名は"Hardscape"）。 |
| [`HardscapeObject.Mode3D`](#hardscapeobjectmode3d) | IntEnum（入れ子） |  | 舗床の3Dモード。 |
| [`PropertyLineObject`](#propertylineobject) | クラス | [`LandmarkObject`](#landmarkobject) | Landmarkプラグインの境界線プラグインオブジェクトです（ユニバーサル名は"Property Line"）。 |
| [`PropertyLineObject.AreaUnits`](#propertylineobjectareaunits) | IntEnum（入れ子） |  | "Area Units Imperial"と"Area Units Metric"の両方のパラメータが対応する面積単位の選択肢。 |
| [`ExistingTreeObject`](#existingtreeobject) | クラス | [`LandmarkObject`](#landmarkobject) | Landmarkプラグインの既存樹木プラグインオブジェクトです（ユニバーサル名は"Existing Tree"）。 |
| [`ExistingTreeObject.Origin`](#existingtreeobjectorigin) | IntEnum（入れ子） |  | 既存樹木の樹種の原産区分。 |
| [`ExistingTreeObject.TreeProtection`](#existingtreeobjecttreeprotection) | IntEnum（入れ子） |  | 樹木保護範囲の表示 |
| [`ExistingTreeObject.Condition`](#existingtreeobjectcondition) | IntEnum（入れ子） |  | 樹木医による評価 |
| [`ExistingTreeObject.SULE`](#existingtreeobjectsule) | IntEnum（入れ子） |  | 安全に利用できる予測余命 |
| [`ExistingTreeObject.Significance`](#existingtreeobjectsignificance) | IntEnum（入れ子） |  | 既存樹木の重要度評価。 |
| [`ExistingTreeObject.Action`](#existingtreeobjectaction) | IntEnum（入れ子） |  | 既存樹木に対する計画措置。 |

<a id="classes"></a>

## クラス

### LandmarkObject

> **完全修飾名:** `api.LandmarkObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Landmarkプラグインオブジェクトのクラス（植栽、ランドスケープエリア、地形モデル、造成図形、レベルオブジェクト、舗床、境界線、既存樹木）に共通する基底クラスです。

LandmarkオブジェクトはVectorworksのプラグインオブジェクトです（Landscape／Vectorworks Landmarkモジュールが登録したプラグインのインスタンスで、APIではパラメトリックオブジェクトとも呼ばれます）。すべてのLandmarkオブジェクトは、"Plant"、"Hardscape"、"Existing Tree"などのユニバーサル（パラメトリック）名で識別されます。後述のクラスは、静的な`Is()`でユニバーサル名を確認し、プラグインの種類を区別します。

このクラスはPrimitiveObjectを継承するため、すべての汎用アクセサー（識別情報、クラス、属性、階層、境界、移動／回転／拡大縮小／反転、削除など）を使用できます。さらに、オブジェクトのパラメトリックレコードのフィールドに、文字列をキーとする統一的な方法でアクセスできます。各サブクラスは、それぞれのプラグインで特に便利なフィールド用の名前付きゲッター／セッターを追加します。

PrimitiveObjectから引き継がれる規約：

- ゲッターは、オブジェクトが無効な場合やパラメータがない場合に`None`を返します。
- セッターは成功時に`True`を返し、オブジェクトが無効な場合やパラメータがない場合に`False`を返します。
- 長さはワールド単位、角度はラジアン、文字列はUTF-8です。

パラメータアクセスの基本（Get/SetParam*）：

- すべてのLandmarkオブジェクトは、名前付きフィールド（「パラメータ」）を持つレコードとしてデータを格納します。各サブクラスの「全パラメータリファレンス」に、利用可能なすべてのパラメータ名が一覧表示されています。サブクラスに専用の型付きアクセサーがないフィールドの読み書きには、GetParamString / SetParamString / GetParamReal / ...でそれらの名前をそのまま使用してください（大文字と小文字を区別し、UTF-8を使用）。
- 表内のパラメータ型には、次のタグを使用します：

- string — テキスト（UTF-8）- GetParamString / SetParamString
- int — 32ビット整数 - GetParamInt / SetParamInt
- bool — ブール値 - GetParamBool / SetParamBool
- real — 浮動小数点数（ワールド座標、度単位の角度、面積、体積、通常の数値など）- GetParamReal / SetParamReal
- popup — N個の文字列から一つを選択 - GetParamString / SetParamString。有効な値はパラメータの隣に記載されています

- ゲッターが`None`、またはセッターが`False`を返す場合、オブジェクトが無効か、パラメータ名がそのオブジェクトに存在しません。`HasParam()`で事前に確認してください。
- 二重アンダースコア（"__"）で始まるパラメータ名はプラグインの内部状態です。読み取りはできますが、通常は直接変更しても意味がありません。
- 「読み取り専用」または「計算値」と記載されたパラメータは、プラグインのリセット時に更新されます。通常、書き込んでも効果は持続しません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `LandmarkObject(h: Handle)` | 任意のオブジェクト`h`を汎用の`LandmarkObject`として参照します。`IsValid()`はハンドルがnullでないことだけを確認します。オブジェクトの種類は`GetParametricName()`または具象クラスの`Is(h)`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetParametricName() -> str \| None` | このオブジェクトのユニバーサル（パラメトリック）名です。例："Plant"または"Hardscape"。オブジェクトが無効な場合や、元のハンドルがプラグインオブジェクトではない場合は空です。 |
| `HasParam(univParamName: str) -> bool` | このプラグインオブジェクトが、指定されたユニバーサル名のフィールドを持つかどうか。 |
| `GetParamNames() -> list[str]` | このオブジェクトのプラグインで定義されたすべてのパラメータ（ユニバーサル）名の順序付きリストです。 |
| `GetParamType(univParamName: str) -> RecordFieldType \| None` | パラメータのデータ型です。パラメータが存在しない場合は`None`です。 |
| `GetParamString(univParamName: str) -> str \| None` | 文字列をキーとする汎用のフィールドアクセサーです。サブクラスに型付きの名前付きアクセサーがある場合は、そちらを優先してください。専用アクセサーのないパラメータには、これらを使用します。パラメータが存在しない場合、ゲッターは`None`、セッターは`False`を返します。 |
| `SetParamString(univParamName: str, value: str) -> bool` | パラメータの文字列を設定します。文字列をキーとする汎用のフィールドアクセサーです。サブクラスに型付きの名前付きアクセサーがある場合は、そちらを優先してください。専用アクセサーのないパラメータには、これらを使用します。パラメータが存在しない場合、ゲッターは`None`、セッターは`False`を返します。 |
| `GetParamReal(univParamName: str) -> float \| None` | `univParamName`の実数パラメータを返します。 |
| `SetParamReal(univParamName: str, value: float) -> bool` | 実数パラメータを設定します。 |
| `GetParamBool(univParamName: str) -> bool \| None` | `univParamName`の*ブール型パラメータ*がオンかどうか。 |
| `SetParamBool(univParamName: str, value: bool) -> bool` | ブール型パラメータを設定します。 |
| `GetParamInt(univParamName: str) -> int \| None` | `univParamName`の整数パラメータを返します。 |
| `SetParamInt(univParamName: str, value: int) -> bool` | 整数パラメータを設定します。 |
| `GetPathObject() -> Handle` | パスベースのプラグインオブジェクト（舗床、ランドスケープエリア、造成図形、境界線など）のパスオブジェクトです。点ベースのプラグインオブジェクト（植栽の単一インスタンス、既存樹木、レベルオブジェクト）や無効なオブジェクトではnullを返します。 |

継承メンバー：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### PlantObject

> **完全修飾名:** `api.PlantObject` · **継承元:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Landmarkプラグインの植栽プラグインオブジェクトです（ユニバーサル名は"Plant"）。

植栽は、指定位置に配置する単一インスタンス、または同じ種の多数のインスタンスを分布させる多角形ベースのコンテナです（単独植栽、多角形の頂点に沿う植栽、多角形の辺に沿う植栽、長方形または三角形の配列の植栽）。構成は"config"パラメータで制御します。

名前付きアクセサーでアクセスできる主なパラメータ：

- "plant ID" — 植栽シンボル／スタイルのリソース名
- "spread" — 植栽の枝張り（樹冠の直径）、ワールド単位
- "height" — 植栽の高さ、ワールド単位
- "latin name" — 学名（ラテン語名）
- "common name" — 樹種名
- "PlantDescription" — 短い説明
- "comments" — 自由記入のコメント
- "tag display" — None / Left / Right / Floating（植栽に対するタグの配置）
- "config" — Single plant / Plants at poly vertices / Plants along poly edges / ...（PlantObjectを参照）
- "Show 3D Detail" — 3D図形をレンダリングするかどうか

その他のフィールドには、LandmarkObjectの汎用アクセサー（GetParamString / GetParamReal / ...）を使用してください。

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）型：string (Text/StaticText)、real (Real/CoordDisp/CoordLocX/CoordLocY/Angle/Area/Volume)、int (LongInt)、bool (Boolean)、popup（string、一覧の選択肢のいずれか）。種／識別情報

- "plant ID" — string — シンボル／スタイルのリソース名（種を識別）
- "PlantDescription" — string — オブジェクト情報パレットに表示する、人が読める説明
- "latin name" — string — 学名
- "common name" — string — 樹種名
- "comments" — string — 自由記入のコメント
- "custom ID" — string
- "isCustom" — bool — ユーザー定義の植栽（植栽データベース由来ではない）では`True`
- "onPlantList" — bool — 植栽集計表に含める
- "Category" — popup — カテゴリ（例：None / Trees / Shrubs / ...）
- "Tag Schema" — string — タグの本文テキストのスキーマ
- "TagSchemaCenter" — string — タグの中央のテキスト
- "TagSchemaBottom" — string — タグの下部のテキスト
- "SKU" — string
- "Price" — real
- "HiddenName" — string

サイズ（ワールド単位）

- "spread" — real — 枝張り
- "height" — real — 全体の高さ
- "spacing" — real — インスタンス間の間隔（多角形構成用）
- "image size" — real
- "Row spacing" — real — 配列モードでの列間の距離
- "Rate" — real — 単位あたりの植栽数（"Rate mode"を参照）
- "Percentage" — int — 分布モードで使用する割合
- "Plants per row" — int
- "Plants per column" — int
- "Plant height scale" — popup — Fixed / randAt5 / randAt10 / randAt15

構成と表示

- "config" — popup — Single plant / Plants at poly vertices / Plants along poly edges / Plants in rectangular array / Plants in triangular array
- "plant style" — popup — No sketch / No sketch w/ shadows / Light sketch / Light sketch w/ shadows / Medium sketch / Medium sketch w/ shadows / Heavy sketch / Heavy sketch w/ shadows / Cloud / Cloud w/ shadows
- "tag display" — popup — None / Left / Right / Floating
- "poly display" — popup — None / Centers-Solid / Centers-Dashed / Boundary-Solid / Boundary-Dashed / Gapped-Solid / Gapped-Dashed
- "tickmark display" — popup — None / Cross / Dot / XMark
- "tickmark size" — real — ティックマークのサイズ、ワールド単位
- "rotate mode" — popup — FALSE / AlongLine / TRUE
- "quantity measure" — popup — Count / Dripline area / Boundary area
- "Outline" — popup — No Outline / Tight Outline / One Outline / Two Outlines / Three Outlines
- "TagBubble" — popup — None / Circle / Circle (Quantity only) / Hexagon / Hexagon (Quantity only) / Rectangle / Round
- "TagApproachAngle" — real — 度
- "TagShoulderAngle" — real — 度
- "TagEnableShoulder" — bool
- "TagUseMarker" — bool
- "TagSnapCenters" — bool
- "display style" — bool
- "Show 3D Detail" — bool
- "ShowSettings" — bool
- "backGroundOnly" — bool
- "massPlants" — bool
- "Replace" — bool
- "drip cloud factor" — real
- "drip sketch factor" — popup — "1-Least sketchy" ... "9-Sketchiest"
- "tagClass" — popup — 植栽ラベルのクラス名
- "tickClass" — popup — ティックマークのクラス名
- "PolylineDisplayClass" — popup — 曲線表示のクラス
- "MassOutlineClass" — popup — 植栽群の輪郭のクラス

影と外観

- "ShadowEnable" — bool
- "ShadowAngle" — real — 度
- "ShadowOffset" — real — ワールド単位
- "ShadowFillStyle" — string
- "FillStyle" — string
- "PenStyle" — string
- "FillStyleParam", "FillSolidColor", "FillPattern", "FillHatch", "FillGrad", "FillImage"
- "FillForeColor", "FillBackColor" — int（カラーインデックス）
- "PenStyleParam", "PenSolidColor", "PenForeColor", "PenBackColor" — int（カラーインデックス）
- "PenWeight", "PenDash", "PenPattern" — int
- "SymbolFPat", "SymbolFFore", "SymbolFBack" — int
- "UseDocumentShadow" — bool

生け垣／分布のオプション

- "Hedge" — bool — 生け垣モードを有効化
- "Hedge rows" — int
- "HedgeMode" — popup
- "HedgeModeNew" — popup — Rectangular / StaggeredRow / TripleStaggeredRow
- "HedgeRowSpacingMode" — popup — SameAsPlantSpacingOrRate / Fixed
- "HedgeRowSpacing" — real — ワールド単位
- "OffsetFromPath" — real — ワールド単位
- "OffsetRows" — bool
- "XOffset", "YOffset" — real — ワールド単位
- "Plant spacing mode" — popup — Custom spacing / Distrib by Rate / Distrib by Coverage
- "Spacing mode" — popup — Same as Plant Spread / Fixed / Best Fit / Count
- "Row spacing mode" — popup — Same as spacing / ...
- "Rate mode" — popup — Plants per unit / Unit on center / Plants per Linear Unit / Plants per Linear Unit Best Fit

3D図形（手続き型生成の樹木）

- "3DGeometryCanopyShape" — int
- "3DGeometryCanopyHgt" — real — ワールド単位
- "gen_generated" — bool
- "gen_canopyShape" — string
- "gen_firstBranchHeight" — real — ワールド単位
- "gen_isFirstBranchHeightDefault" — bool
- "gen_trunkGirth" — real — ワールド単位
- "gen_canopyClass" — popup — クラス名
- "gen_trunkClass" — popup — クラス名
- "scraped_url" — string

根域（特記がない限りワールド単位）

- "classRootZones" — popup — クラス名
- "classRootExcavation" — popup — クラス名
- "showRootBall" — popup — None / 2D Only / 3D Only / 2D and 3D
- "shapeRootBall" — popup — Sphere / B & B (Ball & Burlap)
- "sizeRootBall1", "sizeRootBall2", "sizeRootBall3" — real
- "attrByClassRootBall" — bool
- "lineWeightRootBall" — int
- "lineColorRootBall" — int — カラーインデックス
- "showPlantingExcav" — popup — None / 2D Only / 3D Only / 2D and 3D
- "diamPlantingExcav" — popup — 1.5x the root ball / 2x the root ball / 3x the root ball / Custom
- "depthPlantingExcav" — popup — 1x the root ball / Custom
- "shapePlantingExcav" — popup — Round / Rectangular
- "diamValueExcav", "depthValueExcav" — real
- "attrByClassPlantingExcav" — bool
- "lineWeightPlantingExcav" — int
- "lineColorPlantingExcav" — int — カラーインデックス
- "rootBallArea", "rootBallVolume" — real（読み取り専用、計算値）
- "plantingExcArea", "plantingExcVolume" — real（読み取り専用、計算値）

維持管理／水

- "MaintenanceNotes" — string
- "PropagationNotes" — string
- "FireResilience", "FireRisk" — popup
- "IrrigationType" — popup
- "PointEmitterValue" — popup
- "PointEmitterQuantity" — int
- "PeakWaterRequirement" — real
- "PeakWaterRequirementUnits" — popup — InchesWeek / InchesMonth / LiterMinute / LiterHour / MillimeterWeek / MillimeterMonth
- "IrrigationFrequency" — int
- "IrrigationFrequencyUnits" — popup — PerDay / PerWeek / PerTwoWeeks / PerMonth
- "ActiveRegion" — popup

地形モデルとの連携

- "siteModelLayer" — popup — 地形モデルのレイヤ名
- "__notSingleAutoDTM" — bool

Laubwerkの3D図形（任意）

- "lw_Key", "lw_PlantFile", "lw_Variant" — string
- "lw_GlobalSeason" — bool
- "lw_Season" — string
- "lw_Global2D3DMat" — bool
- "lw_2DReprs", "lw_3DReprs" — string
- "lw_MaterialStyle" — string

その他／読み取り専用

- "DripArea" — real（読み取り専用、計算値）
- "TotalCanopyArea" — real（読み取り専用、計算値）
- "Version" — int — プラグインのスキーマバージョン
- "sustainability" — string — サステナビリティデータのJSONデータ塊
- "GroupAllocation" — string
- "SourcePlantList" — string
- "Factor" — real
- "Message" — string — オブジェクト情報パレットの状態／警告メッセージ
- "__ScheduledSize" — string
- "__Status" — int
- "__fade enabled", "__fade percent" — bool / int
- "ControlPoint01X..ControlPoint04Y" — real（オブジェクトのコントロールポイントのワールド座標）

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `PlantObject(h: Handle)` | 既存の植栽`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D, plantResourceName: str = '') -> PlantObject` *静的* | アクティブレイヤ／現在のコンテナの`position`に、単一インスタンスの植栽を作成します。`plantResourceName`は使用する植栽スタイルリソース（マスター植栽を保持するシンボル定義）の名前です。まだ図面内にない場合は、Vectorworksの植栽コンテンツから取り込みます。空の場合、または指定した名前のスタイルがどこにも見つからない場合は、最初に利用可能な植栽スタイルを使用します。植栽スタイルがまったく利用できない場合は無効なオブジェクトを返します。スタイルのない植栽には描画する図形がないためです。 |
| `CreateFromPath(hPath: Handle, plantResourceName: str = '') -> PlantObject` *静的* | 既存の2Dパスオブジェクトに沿って、またはその領域全体にインスタンスを分布させる、多角形ベースの植栽を作成します。その後"config"パラメータを設定して分布モードを選択してください。 |
| `EnsurePlantStyle(styleName: str = '') -> str` *静的* | 必要に応じてVectorworksの植栽コンテンツから取り込み、現在の図面で植栽スタイルを利用可能にして、その名前を返します（植栽スタイルを利用可能にできなかった場合は空）。 |
| `Duplicate() -> PlantObject` | 図面内の植栽を複製し、そのコピーを返します。 |

*植栽スタイル*

| メソッド | 説明 |
|---|---|
| `GetPlantStyle() -> str \| None` | 植栽が図形とデフォルトのデータを取得するシンボル定義です。これは、植栽とスタイルを結び付ける"PlantDescription"パラメータと同じ値です。 |
| `SetPlantStyle(styleName: str) -> bool` | 必要に応じて`styleName`を取り込み、そのすべての設定をこの植栽に適用して再生成します。 |

*識別情報／種*

| メソッド | 説明 |
|---|---|
| `GetPlantID() -> str \| None` | 植栽ID（植栽シンボル／スタイルのリソース名）を返します。 |
| `SetPlantID(value: str) -> bool` | 植栽IDを設定します。 |
| `GetLatinName() -> str \| None` | 学名を返します。 |
| `SetLatinName(value: str) -> bool` | 学名を設定します。 |
| `GetCommonName() -> str \| None` | 樹種名を返します。 |
| `SetCommonName(value: str) -> bool` | 樹種名を設定します。 |
| `GetPlantDescription() -> str \| None` | 植栽スタイルのシンボル定義名です。スタイルの取り込みと設定の引き継ぎも行うSetPlantStyleを優先してください。図面内にない名前を設定すると、植栽の図形がなくなります。 |
| `SetPlantDescription(value: str) -> bool` | 植栽の説明を設定します。植栽スタイルのシンボル定義名です。スタイルの取り込みと設定の引き継ぎも行うSetPlantStyleを優先してください。図面内にない名前を設定すると、植栽の図形がなくなります。 |
| `GetComments() -> str \| None` | コメントを返します。 |
| `SetComments(value: str) -> bool` | コメントを設定します。 |
| `GetSpread() -> float \| None` | サイズ（ワールド単位）。枝張り（樹冠の直径）です。 |
| `SetSpread(value: float) -> bool` | 広がりを設定します（サイズ（ワールド単位））。 |
| `GetHeight() -> float \| None` | 高さ（植栽の高さ）を返します。 |
| `SetHeight(value: float) -> bool` | 高さを設定します。 |
| `GetConfig() -> PlantObject.Config \| None` | 構成を返します。 |
| `SetConfig(value: PlantObject.Config) -> bool` | 構成を設定します。 |
| `GetTagDisplay() -> PlantObject.TagDisplay \| None` | タグの表示を返します。 |
| `SetTagDisplay(value: PlantObject.TagDisplay) -> bool` | タグの表示を設定します。 |
| `GetShow3DDetail() -> bool \| None` | *3Dの詳細を表示*がオンかどうか。 |
| `SetShow3DDetail(value: bool) -> bool` | *3Dの詳細を表示*のオン／オフを切り替えます。 |
| `GetSpacing() -> float \| None` | 多角形の辺に沿って、または配列構成で配置した植栽の間隔です。 |
| `SetSpacing(value: float) -> bool` | 間隔を設定します。多角形の辺に沿って、または配列構成で配置した植栽の間隔です。 |

継承メンバー：[`LandmarkObject`](#landmarkobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### PlantObject.Config

> **完全修飾名:** `api.PlantObject.Config` · **種類:** `IntEnum`

構成と表示

| メンバー | 値 | 説明 |
|---|---|---|
| `SinglePlant` | `0` |  |
| `PlantsAtPolyVertices` | `1` |  |
| `PlantsAlongPolyEdges` | `2` |  |
| `PlantsInRectangularArray` | `3` |  |
| `PlantsInTriangularArray` | `4` |  |

#### PlantObject.TagDisplay

> **完全修飾名:** `api.PlantObject.TagDisplay` · **種類:** `IntEnum`

植栽ラベルの表示位置。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` |  |
| `Left` | `1` |  |
| `Right` | `2` |  |
| `Floating` | `3` |  |

### LandscapeAreaObject

> **完全修飾名:** `api.LandscapeAreaObject` · **継承元:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Landmarkプラグインのランドスケープエリアプラグインオブジェクトです（ユニバーサル名は"Landscape Area"）。

ランドスケープエリアは、割合に従って分布させた一種以上の植栽で2Dの多角形領域を満たす、パスベースのコンテナです。投影面積／表面積と、必要な植栽の総数を計算します。

植栽リスト自体（種、割合、密度）は、プラグインが管理するインデックス付きのコレクションとして格納されます。個々の植栽項目の読み書きには、LandmarkObjectの汎用アクセサーを使用してください。

名前付きアクセサーでアクセスできる主なパラメータ：

- "name" — ユーザーに表示するランドスケープエリア名／緑地名
- "ID" — 識別タグ
- "Description" — 短い説明
- "area" — 計算された面積（読み取り専用）
- "projectedArea" — 地形モデル上の投影面積（読み取り専用）
- "numPlants" — 植栽の総数（読み取り専用）
- "Drawing Mode" — "Landscape Area"または"Hedgerow"
- "areaUnits" — 面積の表示単位（`LandscapeAreaObject.AreaUnits`を参照）
- "showPlants2D" — 植栽の2D表示ポップアップ

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）識別情報／説明

- "name" — string — 緑地／ランドスケープエリアの名前
- "ID" — string — 識別タグ
- "Description" — string
- "Style Name Formula" — string — 植栽スタイル名を生成する数式
- "Category" — popup — 例："Perennials"
- "InstanceName" — string — インスタンス名（レポート用）
- "CustomCombName", "CustomCombFormula" — string
- "Drawing Mode" — popup — "Landscape Area" / "Hedgerow"

測定値（読み取り専用、リセット時に再計算）

- "area" — real
- "projectedArea" — real
- "ProjectedAreaInLAUnits" — real
- "SurfaceAreaInLAUnits" — real
- "AreaLAUnits" — string
- "areaUnits" — popup — Square Feet / Square Meters / Acres / Hectares / Document Units
- "Hedgerow Length" — real
- "numPlants" — int — 分布させた植栽の総数
- "numAttachedPlants" — int
- "Area Vertex Count" — string — 読み取り専用、書式設定された個数
- "unitPrice" — real
- "priceCode" — string
- "AreaFactor" — real — 面積計算に使用する倍率

2D図形

- "borderStyle" — popup — "Standard" / "None"
- "billowSize" — popup — X Small / Small / Medium / Large / X Large
- "billowVar" — popup — None / Low / Medium / High
- "billowHeight" — popup — Small / Medium / Large
- "billowType" — popup — Convex / Concave
- "segLength" — popup — X Short / Short / Normal / Long / X Long
- "segThickness" — popup — X Thin / Thin / Normal / Thick / X Thick
- "Smooth external corners" — bool
- "showPlants2D" — popup — None / PlantCloud / PlantLine / PlantSymbols（またはFALSE）
- "showPlants3D" — popup — None / Plant Block / Individual Plants
- "diameterScalePopup" — popup — Fixed / Random 5% / Random 10% / Random 15%
- "diameterVisualScale" — real — パーセント
- "heightScalePopup" — popup — Fixed / Random 5% / Random 10% / Random 15%
- "heightVisualScale" — real — パーセント
- "randomizePlantRotation" — bool
- "randomizePlantPosition" — bool
- "allPlantEdgesInsideArea" — bool
- "plantBlockHeight" — real — ワールド単位

3D／地形モデル

- "3dDisplay" — popup — None / Components / 3D Polygon / Texture Bed
- "displayAs3DPolygon" — bool
- "displayOnExisting" — bool
- "hasSiteModel" — bool
- "Cut into Site Model" — bool
- "siteModelLayer" — popup — 地形モデルのレイヤ名
- "minTINElev", "maxTINElev" — real（読み取り専用）
- "__RecalcTINSurfaces", "__RecalcTINDependent" — bool（内部状態）
- "__editComponents" — bool
- "Simplification Tolerance" — real

植栽リスト／密度に基づく分布

- "distRate" — string — 分布密度モード（例："CustomPerc"）
- "percRate" — real — 分布に使用する割合
- "percType" — string — 密度の単位（sqftあたり／sqmあたり／...）
- "hiddenSymbolName", "hiddenRate", "hiddenRateType", "hiddenPercentage" — string（項目ごとの内部状態）
- "hiddenMinNumOfPlants", "hiddenTotalNumOfPlants" — string
- "BestFit" — bool
- "HedgeSpacingEnum" — popup — SameAsPlantSpacingOrRate / Fixed
- "HedgeSpacingValue" — real

生け垣のオプション

- "Width" — real
- "Row Structure" — popup — Rectangular / Staggered / Triple Staggered / Area
- "Hedge Rows" — int
- "Offset rows" — bool
- "PathOffset" — real

タグ

- "tagDisplay" — popup — None / Left / Right
- "displayMarker" — bool
- "tagClass" — popup — クラス名
- "tagLineAngle" — real — 度
- "tagTextAngle" — real — 度
- "tagHeader" — popup / string — タグのヘッダーテキストの数式
- "tagBody" — popup / string — タグの本文テキストの数式
- "controlPoint1X..controlPoint3Y" — real（タグのコントロールポイントのワールド座標）

サステナビリティ（旧式のスカラーフィールド＋2026のJSONデータ塊）

- "HasSustainability" — bool
- "HasPermeability", "IsPermeable" — bool
- "Permeability" — real
- "Permeability Unit" — popup — cm/hour / ...
- "RunoffCoef" — real
- "SRI" — real
- "Sustainability Metric" — string
- "SusPoint1", "SusPoint2", "SusPoint3" — string
- "sustainability" — string — 2026+のJSONデータ塊

その他

- "version" — int
- "__IsNew" — bool
- "GroupAllocation" — string

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `LandscapeAreaObject(h: Handle)` | 既存のランドスケープエリア`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `CreateFromPath(hPath: Handle) -> LandscapeAreaObject` *静的* | 既存の2Dパスオブジェクト（通常は多角形または曲線）からランドスケープエリアを作成します。 |
| `Duplicate() -> LandscapeAreaObject` | 図面内のランドスケープエリアを複製し、そのコピーを返します。 |

*識別情報*

| メソッド | 説明 |
|---|---|
| `GetName() -> str \| None` | 名前（"name"（緑地名）であり、オブジェクト名ではない）を返します。 |
| `SetName(value: str) -> bool` | 名前を設定します。 |
| `GetID() -> str \| None` | IDを返します。 |
| `SetID(value: str) -> bool` | IDを設定します。 |
| `GetDescription() -> str \| None` | 説明を返します。 |
| `SetDescription(value: str) -> bool` | 説明を設定します。 |
| `GetArea() -> float \| None` | 測定値（読み取り専用。オブジェクトのリセット時に計算）（現在の面積単位で表した領域の面積）。 |
| `GetProjectedArea() -> float \| None` | 投影面積を返します（地形モデル上に投影。地形モデルがない場合は0）。 |
| `GetNumPlants() -> int \| None` | 植栽数を返します（分布させた植栽インスタンスの総数）。 |
| `GetDrawingMode() -> LandscapeAreaObject.DrawingMode \| None` | 描画モードを返します。 |
| `SetDrawingMode(value: LandscapeAreaObject.DrawingMode) -> bool` | 描画モードを設定します。 |
| `GetAreaUnits() -> LandscapeAreaObject.AreaUnits \| None` | 面積単位を返します。 |
| `SetAreaUnits(value: LandscapeAreaObject.AreaUnits) -> bool` | 面積単位を設定します。 |
| `GetPlantDisplay2D() -> LandscapeAreaObject.PlantDisplay2D \| None` | 植栽の2D表示を返します。 |
| `SetPlantDisplay2D(value: LandscapeAreaObject.PlantDisplay2D) -> bool` | 植栽の2D表示を設定します。 |

*互換性アクセサー*

| メソッド | 説明 |
|---|---|
| `GetShowPlantsIn2D() -> bool \| None` | `True`は`None`以外のすべての表示を表します。`True`を設定するとPlantSymbolsを選択し、`False`を設定すると`None`を選択します。雲型／線モードを保持するには、ポップアップアクセサーを使用してください。 |
| `SetShowPlantsIn2D(show: bool) -> bool` | *植栽の2D表示*のオン／オフを切り替えます。`True`は`None`以外のすべての表示を表します。`True`を設定するとPlantSymbolsを選択し、`False`を設定すると`None`を選択します。雲型／線モードを保持するには、ポップアップアクセサーを使用してください。 |

継承メンバー：[`LandmarkObject`](#landmarkobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### LandscapeAreaObject.PlantDisplay2D

> **完全修飾名:** `api.LandscapeAreaObject.PlantDisplay2D` · **種類:** `IntEnum`

ランドスケープエリアの植栽の2D表示方法。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` |  |
| `PlantCloud` | `1` |  |
| `PlantLine` | `2` |  |
| `PlantSymbols` | `3` |  |

#### LandscapeAreaObject.DrawingMode

> **完全修飾名:** `api.LandscapeAreaObject.DrawingMode` · **種類:** `IntEnum`

オブジェクトをランドスケープエリアとして描画するか、生け垣として描画するか。

| メンバー | 値 | 説明 |
|---|---|---|
| `LandscapeArea` | `0` |  |
| `Hedgerow` | `1` |  |

#### LandscapeAreaObject.AreaUnits

> **完全修飾名:** `api.LandscapeAreaObject.AreaUnits` · **種類:** `IntEnum`

ランドスケープエリアの面積の表示単位。

| メンバー | 値 | 説明 |
|---|---|---|
| `SqFeet` | `0` |  |
| `SqMeters` | `1` |  |
| `Acres` | `2` |  |
| `Hectares` | `3` |  |
| `DocumentUnits` | `4` |  |

### SiteModelObject

> **完全修飾名:** `api.SiteModelObject` · **継承元:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Landmarkプラグインの地形モデルプラグインオブジェクトです（ユニバーサル名は"DTM6"）。

地形モデルは、ソースデータ（測量点、等高線、境界多角形など）から構築する不規則三角形網（TIN）のサーフェスです。現況地形と計画地形（適用された造成図形を反映）という二つのサーフェスを同時に保持します。

名前付きアクセサーでアクセスできる主なパラメータ：

- "2D Display" — 2Dで描画するサーフェス（Existing / Proposed / Both）
- "2D Style" — 2Dの表示スタイル（等高線、三角形、色分けした勾配など）
- "3D Display" — 3Dで描画するサーフェス（Nothing / Existing / Proposed / Cut&Fill）
- "3D Style" — 3Dの表示スタイル（メッシュ、グリッド、等高線、高さ／勾配による色分けなど）
- "Area Display Type" — 情報パネルの面積単位
- "Volume Display Type" — 情報パネルの体積単位
- "Geometry Zref" — 基準高さ
- "Show Errors" — TINのエラーマーカーを表示

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）表示の選択

- "2D Display" — popup — `kTINDisplayExistingOnly` / `kTINDisplayProposedOnly` / `kTINDisplayExistingAndProposed`
- "2D Style" — popup — k2DTINStyle2DContour / k2DTINStyle2DContourSmoothed / k2DTINStyle2DContourColoredElevations / k2DTINStyle2DTriangulatedContoursColoredSlopes / k2DTINStyle2DTriangles / k2DTINStyle2DTrianglesColoredSlopes
- "3D Display" — popup — `kTINDisplayNothing` / `kTINDisplayExistingOnly` / `kTINDisplayProposedOnly` / `kTINDisplayCutNFill`
- "3D Style" — popup — k3DTINStyleMesh / k3DTINStyleMeshColoredElev / k3DTINStyleMeshColoredSlopes / k3DTINStyleGrid / k3DTINStyleGridColoredElev / k3DTINStyleGridColoredSlope / k3DTINStyleVerticalGrid / k3DTINStyleContour / k3DTINStyleExtrudedContour / k3DTINStyleExtContColoredElev
- "2D C&F Map Overlay" — bool

面積／体積の表示値（すべて読み取り専用の書式設定済み文字列値）

- "Area Display Type" — popup — `kAreaDisplaySqM` / `kAreaDisplayDecar` / `kAreaDisplayHectars` / `kAreaDisplaySqFt` / `kAreaDisplayAcre` / `kAreaUseDocumentUnits`
- "Projected Area (Existing)" — string
- "Surface Area (Existing)" — string
- "Surface Area (Proposed)" — string
- "Volume Display Type" — popup — `kVolumeDisplayCuM` / `kVolumeDisplayCuFt` / `kVolumeDisplayCuYd` / `kVolumeUseDocumentUnits`
- "Volume (Existing)" — string
- "Volume (Proposed)" — string
- "Cut Volume" — string
- "Fill Volume" — string
- "Net C&F Volume" — string
- "Total C&F Volume" — string

図形／エラー

- "Geometry Zref" — real — ワールド単位 - 基準高さ
- "Grid Size" — real
- "Tolerance" — real
- "Depth Intervals" — real
- "Show Errors" — bool
- "dontShowErrors" — bool — （旧式）
- "Error Count" — string — 読み取り専用の書式設定済み個数
- "Site Model Name" — string — 読み取り専用の表示名

ジオイメージの重ね表示

- "GeoImageEnabled" — bool
- "GeoServerURL" — string
- "GeoServiceName" — string
- "GeoServiceType" — string
- "GeoServiceRenderFunc" — popup
- "GeoLayers" — string
- "GeoResolution" — int — タイルあたりのピクセル数
- "GeoTile" — int
- "StoreGeoimage" — bool

内部状態

- "__version", "__messageID" — int
- "__UUID" — string
- "__compsMinZ" — real
- "__SavedGeoinfo" — string

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `SiteModelObject(h: Handle)` | 既存の地形モデル`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D) -> SiteModelObject` *静的* | 地形モデルは通常、Landmarkのコマンドを使用して対話的に作成します（測量点、等高線など）。このファクトリーは`position`に空の地形モデルを作成し、呼び出し側が対応するメニューコマンドを使用するか、ソースデータグループを編集してデータを追加します。 |
| `Duplicate() -> SiteModelObject` | 図面内の地形モデルを複製し、そのコピーを返します。 |
| `Get2DDisplay() -> SiteModelObject.Display2D \| None` | 2D表示を返します。 |
| `Set2DDisplay(value: SiteModelObject.Display2D) -> bool` | 2D表示を設定します。 |
| `Get3DDisplay() -> SiteModelObject.Display3D \| None` | 3D表示を返します。 |
| `Set3DDisplay(value: SiteModelObject.Display3D) -> bool` | 3D表示を設定します。 |
| `Get2DStyle() -> str \| None` | 生の表示スタイル値です（スタイルの完全な一覧はLandmarkのドキュメントを参照）。スタイル名は"k2DTINStyle2DTriangles"や"k3DTINStyleMesh"などのASCII識別子です。 |
| `Set2DStyle(value: str) -> bool` | 2Dスタイルを設定します。生の表示スタイル値です（スタイルの完全な一覧はLandmarkのドキュメントを参照）。スタイル名は"k2DTINStyle2DTriangles"や"k3DTINStyleMesh"などのASCII識別子です。 |
| `Get3DStyle() -> str \| None` | 3Dスタイルを返します。 |
| `Set3DStyle(value: str) -> bool` | 3Dスタイルを設定します。 |
| `GetGeometryZReference() -> float \| None` | 等高線に基づく計算で使用する基準高さです（ワールド単位）。 |
| `SetGeometryZReference(value: float) -> bool` | 図形のZ基準を設定します。等高線に基づく計算で使用する基準高さです（ワールド単位）。 |
| `GetShowErrors() -> bool \| None` | *エラーを表示*がオンかどうか。 |
| `SetShowErrors(value: bool) -> bool` | *エラーを表示*のオン／オフを切り替えます。 |
| `GetProjectedAreaExisting() -> str \| None` | 読み取り専用の面積と体積の表示値です（書式設定済み文字列。未計算の場合は空）。 |
| `GetSurfaceAreaExisting() -> str \| None` | 現況の表面積を返します。 |
| `GetSurfaceAreaProposed() -> str \| None` | 計画の表面積を返します。 |
| `GetVolumeExisting() -> str \| None` | 現況の体積を返します。 |
| `GetVolumeProposed() -> str \| None` | 計画の体積を返します。 |
| `GetCutVolume() -> str \| None` | 切土量を返します。 |
| `GetFillVolume() -> str \| None` | 盛土量を返します。 |

継承メンバー：[`LandmarkObject`](#landmarkobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### SiteModelObject.Display2D

> **完全修飾名:** `api.SiteModelObject.Display2D` · **種類:** `IntEnum`

2D／3D表示の選択

| メンバー | 値 | 説明 |
|---|---|---|
| `ExistingOnly` | `0` |  |
| `ProposedOnly` | `1` |  |
| `ExistingAndProposed` | `2` |  |

#### SiteModelObject.Display3D

> **完全修飾名:** `api.SiteModelObject.Display3D` · **種類:** `IntEnum`

地形モデルの3D表示の内容。

| メンバー | 値 | 説明 |
|---|---|---|
| `Nothing` | `0` |  |
| `ExistingOnly` | `1` |  |
| `ProposedOnly` | `2` |  |
| `CutAndFill` | `3` |  |

### SiteModifierObject

> **完全修飾名:** `api.SiteModifierObject` · **継承元:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Landmarkプラグインの造成図形プラグインオブジェクトです（ユニバーサル名は"Site Modifiers"）。

造成図形は、地形モデルのサーフェスを変形するパスベースのオブジェクトです。一つの造成図形には、"Config"パラメータで選択する複数の構成候補があります。すべての構成は、"Apply To"パラメータで選択した"Existing"または"Proposed"のサーフェスに適用されます。

名前付きアクセサーでアクセスできる主なパラメータ：

- "Config" — 使用する変形方式（後述の`SiteModifierObject.Config`を参照）
- "Apply To" — 変更を適用する地形モデルのサーフェス（Existing / Proposed）
- "Show 3D" — 造成図形を3D図形として表示
- "Retain Slope Inside" — 造成図形の領域内の勾配を保持
- "Simplification Tolerance" — 頂点の簡略化の許容値、ワールド単位

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）。造成図形は、すべての構成のパラメータを同時に格納します。プラグインが実際に使用するのは、現在の"Config"の値に属するパラメータのみです。共通（すべての構成）

- "Config" — popup — Fence（=法面）/ Contour / Pad / PadwEdge（=造成面（土留め付き））/ Aligned / Path / Texture Bed / Grader（=土量の調整範囲）
- "Apply To" — popup — Existing / Proposed
- "Show 3D" — bool
- "Retain Slope Inside" — bool
- "Simplification Tolerance" — real — ワールド単位
- "Modifier Vertex Count" — string — 読み取り専用の書式設定済み個数
- "__version" — int
- "__IsNewObject" — bool
- "__WasGeometryChanged", "__WasSideDataChanged", "__IsInvalPath", "__ChangeAffectsSiteModel" — bool（内部）

法面（Config = "Fence"）

- "Define by contours" — bool
- "Use as C&F Calc Zone" — bool
- "__AreContoursConnected" — bool（内部）

造成面（Config = "Pad"）と造成面（土留め付き）（Config = "PadwEdge"）

- "Elevation" — real — ワールド単位
- "Slope Def" — popup — None / Angle / DownPerc / UpPerc / DownRatio / UpRatio
- "Slope Ang" — real — 度（Slope Def = Angleの場合に使用）
- "Slope Percent" — string — 例："5%"（Slope Def = DownPerc/UpPercの場合に使用）
- "Slope Ratio" — string — 例："1:4"（Slope Def = DownRatio/UpRatioの場合に使用）
- "ElevAtEnd" — real — ワールド単位
- "ContourAng" — real — 度
- "Slope A", "Slope B" — string
- "Show Cross Slope" — bool
- "Show Slope A Arrow" — bool
- "Show Slope B Arrow" — bool
- "Constrain Slope Down" — bool
- "Show Slope Elevations" — bool
- "Show Modifier Elevation" — bool
- "Annotation Class" — popup — クラス名
- "__DoElevateRetEdge" — bool（造成面（土留め付き）のみ）
- "__UseSlopeToolAtCreate" — bool

位置合わせ（Config = "Aligned"）

- "Align with Objects on" — popup — AllLayers / VisLayersOnly / SameLayerAsHScape / CustomSetOfLayers / SelectLayers
- "AlignWithObjectsOnOption" — int
- "Interpolate Surface" — bool
- "Interpolation Type" — popup — Concave / Convex
- "Show Profile Lines" — bool
- "Show Profile Names" — bool
- "Show Slopes" — bool
- "Show Vertex Elevation" — bool
- "Show Profile Line Markers" — bool
- "Show Stake Objects" — bool
- "Show Grade Objects" — bool
- "Start Symbol Marker Name" — string — シンボル名
- "End Symbol Marker Name" — string — シンボル名
- "Smoothness Sampling" — int
- "Falloff" — string — パーセント、例："50,00%"
- "__RecreateAlignedTIN" — bool（内部）

パス（Config = "Path"）

- "LongProf_StartElevValue" — real — ワールド単位
- "LongProf_EndElevValue" — real — ワールド単位
- "LongProf_MarkerType" — popup — None / Triangle / TriangleFilled / Circle / Dot / Cross / Circle Cross / Tick Mark
- "LongProf_MarkerFactor" — real
- "LongProf_SlopesDef" — popup — GradePerc / Ratio / Angle
- "LongProf_ShowLine", "LongProf_ShowSlopes", "LongProf_ShowVertexElev", "LongProf_ShowLineMarkers" — bool
- "LongProf_StartSymMarkerName", "LongProf_EndSymMarkerName" — string
- "TransProf_SlopesDef" — popup — GradePerc / Ratio / Angle
- "TransProf_ShowLines", "TransProf_ShowNames", "TransProf_ShowSlopes", "TransProf_ShowVertexElev", "TransProf_ShowLineMarkers" — bool
- "TransProf_StartSymMarkerName", "TransProf_EndSymMarkerName" — string
- "Prof_SlopeArrowDownward" — bool
- "__RecreatePathTIN", "__FitLongProfToSurf" — bool（内部）

オブジェクトに合わせる（Config = "Aligned"のサブモード）

- "Use Objects on" — popup — AllLayers / VisLayersOnly / SameLayerAsObject / CustomSetOfLayers / SelectLayers
- "Fit to" — popup — FitBottom / FitTop
- "__IsPathOK" — bool（内部）

テクスチャの範囲（Config = "Texture Bed"）

- "Texture Class" — popup — テクスチャの範囲として使用するクラス名

面積／体積の表示値（"Volume Display Type"ポップアップを参照）

- "Area Display Type" — popup — `kAreaDisplaySqM` / `kAreaDisplayDecar` / `kAreaDisplayHectars` / `kAreaDisplaySqFt` / `kAreaDisplayAcre` / `kAreaUseDocUnits`
- "Projected Area" — string（読み取り専用）
- "Surface Area (Existing)" — string（読み取り専用）
- "Surface Area (Proposed)" — string（読み取り専用）
- "Volume Display Type" — popup — `kVolumeDisplayCuM` / `kVolumeDisplayCuFt` / `kVolumeDisplayCuYd` / `kVolumeUseDocUnits`
- "Volume (Existing)" — string（読み取り専用）
- "Volume (Proposed)" — string（読み取り専用）
- "Cut Volume" — string（読み取り専用）
- "Fill Volume" — string（読み取り専用）
- "Net C&F Volume" — string（読み取り専用）
- "Total C&F Volume" — string（読み取り専用）

旧式（以前のVectorworksバージョンで作成されたオブジェクトが使用）

- "Zref" — real
- "Slope" — real
- "SlopeDef" — popup — None / Angle / DownPerc / Percent / DownRatio / UpRatio
- "Prop" — popup — Existing / Proposed
- "Class" — popup — クラス名
- "ControlPoint01X..ControlPoint14Y" — real（ワールド座標）
- "Show Slope Arrow" — bool

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `SiteModifierObject(h: Handle)` | 既存の造成図形`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `CreateFromPath(hPath: Handle) -> SiteModifierObject` *静的* | 既存の2Dパスオブジェクト（多角形または曲線）から造成図形を作成します。 |
| `Duplicate() -> SiteModifierObject` | 図面内の造成図形を複製し、そのコピーを返します。 |
| `GetConfig() -> SiteModifierObject.Config \| None` | 構成を返します。 |
| `SetConfig(value: SiteModifierObject.Config) -> bool` | 構成を設定します。 |
| `GetApplyTo() -> SiteModifierObject.ApplyTo \| None` | 適用先を返します。 |
| `SetApplyTo(value: SiteModifierObject.ApplyTo) -> bool` | 適用先を設定します。 |
| `GetShow3D() -> bool \| None` | *3D 表示*がオンかどうか。 |
| `SetShow3D(value: bool) -> bool` | *3D 表示*のオン／オフを切り替えます。 |
| `GetRetainSlopeInside() -> bool \| None` | *内部の勾配を保持*がオンかどうか。 |
| `SetRetainSlopeInside(value: bool) -> bool` | *内部の勾配を保持*のオン／オフを切り替えます。 |
| `GetSimplificationTolerance() -> float \| None` | 簡略化の許容値を返します。 |
| `SetSimplificationTolerance(value: float) -> bool` | 簡略化の許容値を設定します。 |

継承メンバー：[`LandmarkObject`](#landmarkobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### SiteModifierObject.Config

> **完全修飾名:** `api.SiteModifierObject.Config` · **種類:** `IntEnum`

造成図形の変形方式です（"Config"）。

| メンバー | 値 | 説明 |
|---|---|---|
| `GradeLimits` | `0` | 変更が及ぶ範囲を制限する閉じた境界。 |
| `Contour` | `1` | 一定の高さの等高線。 |
| `Pad` | `2` | 目標の高さにある平らな造成面。 |
| `RetainingPad` | `3` | 造成面（土留め付き）。 |
| `Aligned` | `4` | 辺ごとの高さと勾配を使用する位置合わせ造成面。 |
| `Path` | `5` | 縦断プロファイルを持つパス。 |
| `FitToObjects` | `6` | 多角形を通るオブジェクトの高さから補間します。 |
| `TextureBed` | `7` | 3Dのテクスチャの範囲（高さの変更なし）。 |
| `SpoilPile` | `8` | 体積／高さに達するまで、勾配を付けて材料を積み上げます。 |

#### SiteModifierObject.ApplyTo

> **完全修飾名:** `api.SiteModifierObject.ApplyTo` · **種類:** `IntEnum`

造成図形が適用される地形モデルの面。

| メンバー | 値 | 説明 |
|---|---|---|
| `Existing` | `0` |  |
| `Proposed` | `1` |  |

### StakeObject

> **完全修飾名:** `api.StakeObject` · **継承元:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Landmarkプラグインのレベルオブジェクトプラグインオブジェクトです（ユニバーサル名は"Stake Object"）。

レベルオブジェクトは、特定の位置と高さに配置するラベル付きの2D点です。"Mode"に応じて、その高さを地形モデルのソースデータとして提供する、現在の地形モデルのサーフェスに高さを合わせる、2D図形としてのみ機能する、または造成図形の点を表す、のいずれかになります。

名前付きアクセサーでアクセスできる主なパラメータ：

- "Mode" — レベルオブジェクトの役割（後述の`StakeObject.Mode`を参照）
- "Site Model" — レベルオブジェクトの対象となる地形モデルのサーフェス（"Existing"または"Proposed"）
- "ID" — 数値の識別子
- "ID Prefix" — ラベル内のIDの前に付ける接頭辞
- "ID Suffix" — ラベル内のIDの後に付ける接尾辞
- "Z Value" — 高さ（ワールド単位）
- "Data" — 自由記入の説明
- "Label ReferenceN" — レベルオブジェクトのラベルに表示するデータ

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）役割と対象の地形モデル

- "Mode" — popup — Include as site model data / Set elev to site model grade / Set elev to site model cut surface / Set elev to object spot / Use as 2D graphic only / Site modifier object
- "Previous Mode" — string — 最後に選択したMode値（プラグインが使用）
- "Site Model" — popup — Existing / Proposed

識別情報／ラベル

- "ID" — int — 数値の識別子
- "ID Prefix" — string
- "ID Suffix" — string
- "Data" — string — 自由記入の説明
- "Label Reference" — string — 旧式のラベル参照
- "Label ReferenceN" — popup — ID / Elevation / Description / ID/Elevation / ID/Description / Description/Elevation / Stationing Data / Coordinate PointNE / Coordinate PointEN / Coordinate PointXY / Coordinate PointYX / Latitude/Longitude / Longitude/Latitude / Latitude/Longitude(WGS84) / Longitude/Latitude(WGS84) / No Label / Object Spot Height
- "Label Position" — popup — Auto / Right / Left / Center
- "Style" — popup — none / Triangle / TriangleFilled / Circle / Dot / Cross / Circle Cross / Tick Mark
- "AutoIDNumber" — bool
- "InitIDNumber" — int
- "Bubble Style" — popup — None / Box / Round Rect / Cloud / Hexagonal / Circle
- "Radius Factor" — real
- "Margin" — real
- "UseAnnotation" — popup — Data Tag / Built-in Tag
- "DataTagStyle" — popup — データタグスタイルのリソース名
- "LabelText", "LabelValues" — string

高さと座標

- "Z Value" — real — ワールド単位（高さ）
- "Station Point Data" — real — ワールド単位
- "Coordinate Units" — popup — Document units / CRS units / Feet / Meters
- "ElevationUnits" — popup — Document units / Feet/Inches / Inches / Feet / Yards / Miles / Microns / Millimeters / Centimeters / Meters / Kilometers / Decimal Degrees / Degrees/Minutes/Seconds
- "CoordinatePrecM" — popup — 1 / .1 / .01 / .001 / .0001 / ... / .0000000001
- "CoordinatePrecA" — popup — 0.0 / 0.00 / 0.000 / 0.0000 / ... / 0.00000000
- "ElevationPrecM", "ElevationPrecA" — popup（CoordinatePrecM/Aと同じ選択肢）
- "ShowUnitMark" — bool
- "ShowElevationMark" — bool
- "Latitude", "Longitude", "Latitude WGS84", "Longitude WGS84" — real
- "Easting", "Northing" — real
- "Easting Display", "Northing Display" — string（読み取り専用の書式設定済み値）

表示

- "Display Leader Line" — bool
- "3D Display" — popup — None / Locus / Extrude
- "ExtrudeWidth", "ExtrudeHeight" — real（ワールド単位）
- "Scale Factor" — real
- "markOffsetX", "markOffsetY" — real（ワールド単位）
- "markRot" — real（度）
- "ControlPoint01X", "ControlPoint01Y" — real（ワールド単位）

内部／バージョン管理

- "__version" — int
- "__new" — bool
- "__toolpref" — bool
- "__dtmElevCalculated" — bool
- "__DataTagStyleName" — string

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `StakeObject(h: Handle)` | 既存のレベルオブジェクト`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D, zValue: float = 0.0) -> StakeObject` *静的* | アクティブレイヤ／現在のコンテナの`position`にレベルオブジェクトを作成します。 |
| `Duplicate() -> StakeObject` | 図面内のレベルオブジェクトを複製し、そのコピーを返します。 |
| `GetMode() -> StakeObject.Mode \| None` | モードを返します。 |
| `SetMode(value: StakeObject.Mode) -> bool` | モードを設定します。 |
| `GetSiteModel() -> StakeObject.SiteModel \| None` | 地形モデルを返します。 |
| `SetSiteModel(value: StakeObject.SiteModel) -> bool` | 地形モデルを設定します。 |
| `GetID() -> int \| None` | IDを返します。 |
| `SetID(value: int) -> bool` | IDを設定します。 |
| `GetIDPrefix() -> str \| None` | IDの接頭辞を返します。 |
| `SetIDPrefix(value: str) -> bool` | IDの接頭辞を設定します。 |
| `GetIDSuffix() -> str \| None` | IDの接尾辞を返します。 |
| `SetIDSuffix(value: str) -> bool` | IDの接尾辞を設定します。 |
| `GetZValue() -> float \| None` | Z値を返します（高さ、ワールド単位）。 |
| `SetZValue(value: float) -> bool` | Z値を設定します。 |
| `GetData() -> str \| None` | データを返します（ラベルに表示する自由記入の説明）。 |
| `SetData(value: str) -> bool` | データを設定します。 |
| `GetLabelReference() -> str \| None` | レベルオブジェクトのラベルの表示内容（ID／高さ／説明／組み合わせ／座標／...） |
| `SetLabelReference(value: str) -> bool` | ラベル参照を設定します。レベルオブジェクトのラベルの表示内容（ID／高さ／説明／組み合わせ／座標／...） |
| `GetDisplayLeaderLine() -> bool \| None` | *引出線を表示*がオンかどうか。 |
| `SetDisplayLeaderLine(value: bool) -> bool` | *引出線を表示*のオン／オフを切り替えます。 |
| `GetShowElevationMark() -> bool \| None` | *高さマークを表示*がオンかどうか。 |
| `SetShowElevationMark(value: bool) -> bool` | *高さマークを表示*のオン／オフを切り替えます。 |

継承メンバー：[`LandmarkObject`](#landmarkobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### StakeObject.Mode

> **完全修飾名:** `api.StakeObject.Mode` · **種類:** `IntEnum`

地形モデルに対するレベルオブジェクトの役割。

| メンバー | 値 | 説明 |
|---|---|---|
| `SiteModelSource` | `0` | "Include as site model data" - レベルオブジェクトのZがソース点になります。 |
| `SetToSiteModelGrade` | `1` | "Set elev to site model grade"（敷地の高さに配置（勾配））。 |
| `SetToCutSurface` | `2` | "Set elev to site model cut surface"（地形モデルの切り取り面の高さに設定）。 |
| `SetToObjectSpot` | `3` | "Set elev to object spot"（オブジェクトの測点の高さに設定）。 |
| `Graphic2DOnly` | `4` | "Use as 2D graphic only"（2D/3D情報のみ）。 |
| `SiteModifierObject` | `5` | "Site modifier object"（造成図形）。 |

#### StakeObject.SiteModel

> **完全修飾名:** `api.StakeObject.SiteModel` · **種類:** `IntEnum`

レベルオブジェクトが参照する地形モデルの面。

| メンバー | 値 | 説明 |
|---|---|---|
| `Existing` | `0` |  |
| `Proposed` | `1` |  |

### HardscapeObject

> **完全修飾名:** `api.HardscapeObject` · **継承元:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Landmarkプラグインの舗床プラグインオブジェクトです（ユニバーサル名は"Hardscape"）。

舗床は、舗装面（歩道、パティオ、車道など）を表すパスベースのオブジェクトです。境界線形式の舗床、またはパス形式の舗床（パスに沿った一定幅の帯）として使用できます。枠を含めたり、3D図形（スラブ、上面の造成面、下面の造成面、テクスチャの範囲）を生成したり、主領域／枠の面積と周長を報告したりできます。

名前付きアクセサーでアクセスできる主なパラメータ：

- "ID" — ユーザー向けの識別子／表面材の名前
- "Sketch" — スケッチスタイル（完全な一覧はプラグインを参照）
- "Tag Display" — タグの配置（None / Right / Left / Floating）
- "Tag Style" — タグに表示する情報
- "Draw 3D" — 3D図形を生成
- "Site Mod" — 造成図形として機能
- "isPathway" — パス形式（一定幅の帯）
- "Use Border" — 枠の構成要素を含める
- "Slab Thick" — スラブの厚み（ワールド単位）
- "Border Thick" — 枠の厚み（ワールド単位）
- "Path Wid" — パスの幅（ワールド単位、パス形式のみ）
- "Path Offset" — パスのオフセット（ワールド単位、パス形式のみ）
- "Main Area", "Border Area", "Footprint Area", "Perimeter" — 読み取り専用の測定値

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）。舗床は造成図形のパラメータ一式も保持します（SiteModifierObjectを参照）。これらのパラメータが有効になるのは、"Use Site Modifier"がTRUEで、舗床が造成図形を駆動する場合のみです。識別情報／説明

- "ID" — string — ユーザー向けの表面／マテリアルの識別子
- "IDN" — string — 代替IDフィールド
- "Instance Name" — string
- "Custom combination name" — string
- "Custom combination formula" — string
- "Description" — string
- "Category" — popup — 例：Paving（カテゴリ分類）
- "Style Name Formula" — string
- "__NNA_Version" — int — プラグインのスキーマバージョン
- "__xver", "__modeOffset" — int / real

モードの選択

- "Sketch" — popup — Single sketch／その他のスケッチ品質の選択肢
- "isPathway" — bool
- "Draw 3D" — bool
- "Site Mod" — bool
- "Use Border" — bool
- "Configuration" — int
- "Mode 3D" — popup (str) — "0" = None / "1" = Slab / "2" = Pad Under / "3" = Texture Bed / "4" = Pad Over
- "New Mode 3D" — popup
- "Use Site Modifier" — bool
- "Site Model Interaction" — popup — 例：ActAsSiteModifier
- "TextBedClass" — string
- "ConvertToBoundary" — bool

パス／枠の寸法（特記がない限りワールド単位）

- "Path Wid" — real — パスの幅
- "Path Offset" — real — 描画したパスからのオフセット
- "Border Wid" — real — 枠の幅
- "Bord Spacing" — real
- "Bord Path Opt" — int
- "Bord Back CIdx" — int — 枠の背景色のカラーインデックス
- "Slab Thick" — real
- "Border Thick" — real

目地／ハッチングのパターン

- "Main Rsrc Name" — string — 主領域の目地パターンのリソース名
- "Bord Rsrc Name" — string — 枠の目地パターンのリソース名
- "Main Joint Patt" — int
- "Bord Joint Patt" — int
- "Main Jt Patt Mod" — real
- "Main Jt Patt Y Mod" — real
- "Main Jt Patt Ang" — real — 度
- "Bord Jt Patt Ang" — real — 度
- "Main Jt I Scale", "Main Jt J Scale" — real
- "Bord Jt I Scale", "Bord Jt J Scale" — real
- "MainJointClass", "BorderJointClass" — popup — クラス名

放射状／パス状の舗装材のオプション（放射状またはパス状のパターンで使用する場合）

- "Radial Course Spacing" — real — ワールド単位
- "Radial Center Paver Diam" — real
- "Radial Offset Mode" — string
- "Radial Offset Width" — real
- "Radial Offset Angle" — real — 度
- "Radial Offset Shift" — real
- "Radial Inside Paver Width" — real
- "Radial Count Paver Width" — int
- "Path Paver Width" — real
- "Path Paver Length" — real
- "Path Paver Length Is Rand" — bool
- "Path Paver Rand Pct Length" — real
- "Path Paver Offset Mode" — string
- "Path Paver Offset Width" — real
- "Path Paver Offset Shift" — real

タグ

- "Tag Display" — popup — None / Right / Left / Floating
- "Tag Style" — popup — ID only / ID-Area(s) / ID-Area(s)-Perim
- "TagAlignment" — popup — Underline / Center
- "TagApproachAngle" — real — 度
- "TagShoulderAngle" — real — 度
- "TagUseMarker" — bool
- "TagSnapEdge" — bool
- "tagClass" — popup — クラス名
- "SlopeArrowClass" — popup — クラス名

測定値（読み取り専用、リセット時に計算）

- "Main Area" — real — （面積）
- "Border Area" — real
- "Footprint Area" — real
- "Perimeter" — real — ワールド単位
- "Main Perimeter" — real
- "Border Perimeter" — real
- "Main Area Fill Color" — int — カラーインデックス
- "Fill Type" — int

価格

- "Main Unit Price" — real
- "Border Unit Price" — real
- "Main Price Code" — string
- "Border Price Code" — string

コントロールポイント（ワールド単位、変形プロバイダーが制御）

- "ControlPoint01X..ControlPoint21Y" — real

サステナビリティ（旧式のスカラーフィールド＋JSONデータ塊）

- "IsPermeable" — bool
- "RunoffCoef" — real
- "Sustainability Metric" — string
- "SusPoint1", "SusPoint2", "SusPoint3" — string
- "SRI" — real
- "HasSustainability", "HasPermeability" — bool
- "Permeability" — real
- "Permeability Unit" — popup — cm/hour / ...
- "sustainability" — string — JSONデータ塊（VW2026+）

舗床が保持する造成図形のパラメータ（完全な一覧はSiteModifierObjectを参照）："Config"、"Apply To"、"Show 3D"、"Retain Slope Inside"、"Simplification Tolerance"、および造成面／位置合わせ／パス／オブジェクトに合わせる／テクスチャの範囲と、面積／体積の表示値のパラメータ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `HardscapeObject(h: Handle)` | 既存の舗床`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `CreateFromPath(hPath: Handle) -> HardscapeObject` *静的* | 既存の2Dパスオブジェクト（多角形または曲線）から舗床を作成します。 |
| `Duplicate() -> HardscapeObject` | 図面内の舗床を複製し、そのコピーを返します。 |

*識別情報*

| メソッド | 説明 |
|---|---|
| `GetID() -> str \| None` | IDを返します。 |
| `SetID(value: str) -> bool` | IDを設定します。 |
| `Get3DMode() -> HardscapeObject.Mode3D \| None` | 3Dモードを返します。 |
| `Set3DMode(value: HardscapeObject.Mode3D) -> bool` | 3Dモードを設定します。 |
| `GetDraw3D() -> bool \| None` | *3D 描画*がオンかどうか。 |
| `SetDraw3D(value: bool) -> bool` | *3D 描画*のオン／オフを切り替えます。 |
| `GetIsSiteModifier() -> bool \| None` | *造成図形*がオンかどうか。 |
| `SetIsSiteModifier(value: bool) -> bool` | *造成図形*のオン／オフを切り替えます。 |
| `GetIsPathway() -> bool \| None` | *パス*がオンかどうか。 |
| `SetIsPathway(value: bool) -> bool` | *パス*のオン／オフを切り替えます。 |
| `GetUseBorder() -> bool \| None` | *枠を使用*がオンかどうか。 |
| `SetUseBorder(value: bool) -> bool` | *枠を使用*のオン／オフを切り替えます。 |
| `GetSlabThickness() -> float \| None` | サイズ（ワールド単位）。 |
| `SetSlabThickness(value: float) -> bool` | スラブの厚みを設定します（サイズ（ワールド単位））。 |
| `GetBorderThickness() -> float \| None` | 枠の厚みを返します。 |
| `SetBorderThickness(value: float) -> bool` | 枠の厚みを設定します。 |
| `GetBorderWidth() -> float \| None` | 枠の幅を返します。 |
| `SetBorderWidth(value: float) -> bool` | 枠の幅を設定します。 |
| `GetPathwayWidth() -> float \| None` | パスの幅を返します（isPathway = `True`）。 |
| `SetPathwayWidth(value: float) -> bool` | パスの幅を設定します。 |
| `GetPathwayOffset() -> float \| None` | パスのオフセットを返します。 |
| `SetPathwayOffset(value: float) -> bool` | パスのオフセットを設定します。 |
| `GetMainArea() -> float \| None` | 測定値（読み取り専用、リセット時に計算）。 |
| `GetBorderArea() -> float \| None` | 枠の面積を返します。 |
| `GetFootprintArea() -> float \| None` | 平面投影面積を返します。 |
| `GetPerimeter() -> float \| None` | 周長を返します。 |
| `GetMainPerimeter() -> float \| None` | 主領域の周長を返します。 |
| `GetBorderPerimeter() -> float \| None` | 枠の周長を返します。 |

継承メンバー：[`LandmarkObject`](#landmarkobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### HardscapeObject.Mode3D

> **完全修飾名:** `api.HardscapeObject.Mode3D` · **種類:** `IntEnum`

舗床の3Dモードです。既存の列挙値はAPIの値であり、ネイティブのポップアップコードではありません。セッターは、現在のオブジェクトのNew Mode 3D / Use Site Modifierと、造成図形モードではConfigも同期させ、ネイティブのリセットで要求したモードが保持されるようにします。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` |  |
| `Slab` | `1` |  |
| `PadUnder` | `2` |  |
| `PadOver` | `3` |  |
| `TextureBed` | `4` |  |
| `SlabDrainage` | `5` |  |
| `AlignedSlab` | `6` |  |
| `AlignedModifOver` | `7` |  |
| `AlignedModifUnder` | `8` |  |

### PropertyLineObject

> **完全修飾名:** `api.PropertyLineObject` · **継承元:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Landmarkプラグインの境界線プラグインオブジェクトです（ユニバーサル名は"Property Line"）。

境界線は、法的な土地の区画境界を閉じた2Dパスで表します。各辺に方位／距離のラベルを付け、設定可能な単位で区画の面積と周長を計算します。

名前付きアクセサーでアクセスできる主なパラメータ：

- "Name" — ユーザー向けの区画名
- "Number" — 地番
- "Area" — 計算された面積（読み取り専用、書式設定済み）
- "Perimeter" — 計算された周長（読み取り専用、書式設定済み）
- "Show Name" — 区画に名前を表示
- "Show Number" — 区画に番号を表示
- "Show Area" — 計算された面積を表示
- "Area Units Imperial" — ファイルがインチ系の場合に使用する面積単位
- "Area Units Metric" — ファイルがメートル系の場合に使用する面積単位
- "Annotation Units" — 辺の距離ラベルの単位（Get/SetDistanceUnits）

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）識別情報

- "Name" — string
- "Number" — string

測定値（読み取り専用、書式設定済み）

- "Area" — string
- "Perimeter" — string

切り替え

- "Show Name" — bool
- "Show Number" — bool
- "Show Area" — bool
- "Reverse Direction" — bool
- "Fill Behind Text" — bool
- "FillBehindSegText" — bool
- "Tag Show Unit" — bool
- "Seg Show Unit" — bool
- "Annotate Segments" — bool
- "Draw 3D" — bool

単位と書式

- "Area Units Metric" — popup — Document Units / Square Feet / Square Yards / Square Miles / Acres / Square Meters / Square Kilometers / Hectares
- "Area Units Imperial" — popup — （Area Units Metricと同じ選択肢）
- "Annotation Units" — popup — Document Units / Feet & Inches / Inches / Feet / Yards / Miles / Microns / Millimeters / Centimeters / Meters / Kilometers
- "Decimals" — int
- "SegDecimals" — int
- "Text Rotation" — real — 度

辺／角の表示

- "Annotation Style" — popup — Angle, Distance, Curve / Angle, Distance / Distance Only
- "Angle Format" — radio — Azimuth / Bearing
- "Corner Indicator" — popup — None / Triangle / Filled Triangle / Circle / Dot / Cross / Circle Cross / Tick Mark
- "Corner Indicator Size" — real — ワールド単位
- "Report Distance" — popup — On Segment (Outside) / On Segment (Inside) / No
- "Report Angle" — popup — On Segment (Outside) / On Segment (Inside) / Bearing at Corner (Outside) / Bearing at Corner (Inside) / Interior at Corner (Outside) / Interior at Corner (Inside) / No
- "Report Curve" — popup — Yes as Table / Yes as Segment Label / No

造成図形との連携

- "Site Modifier" — popup — None / Grade Limits / Texture Bed
- "Texture Bed Class" — popup — クラス名

文字スタイルの上書き（ラベルごと）

- "Name Text Style" — popup — Un-Styled / Class Text Style
- "Number Text Style" — popup — Un-Styled / Class Text Style
- "Area Text Style" — popup — Un-Styled / Class Text Style
- "Annot Text Style" — popup — Un-Styled / Class Text Style

内部状態

- "__IsNew" — bool
- "__Simple_Dialog" — bool
- "startCurveIDsAt", "numberOfCurves" — int
- "ControlPoint01X..ControlPoint02Y" — real（ワールド座標）
- "ResetCurveDataWS" — bool

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `PropertyLineObject(h: Handle)` | 既存の境界線`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `CreateFromPath(hPath: Handle) -> PropertyLineObject` *静的* | 既存の2Dパスオブジェクト（閉じた多角形または曲線）から境界線を作成します。 |
| `Duplicate() -> PropertyLineObject` | 図面内の境界線を複製し、そのコピーを返します。 |
| `GetName() -> str \| None` | 名前を返します。 |
| `SetName(value: str) -> bool` | 名前を設定します。 |
| `GetNumber() -> str \| None` | 番号を返します。 |
| `SetNumber(value: str) -> bool` | 番号を設定します。 |
| `GetAreaText() -> str \| None` | 書式設定済みの読み取り専用の測定値です。ワールド単位の幾何学的な値には、`PrimitiveObject.GetArea` / GetPerimeterを使用してください。 |
| `GetPerimeterText() -> str \| None` | 周長のテキストを返します。 |
| `GetShowName() -> bool \| None` | *名前を表示*がオンかどうか。 |
| `SetShowName(value: bool) -> bool` | *名前を表示*のオン／オフを切り替えます。 |
| `GetShowNumber() -> bool \| None` | *番号を表示*がオンかどうか。 |
| `SetShowNumber(value: bool) -> bool` | *番号を表示*のオン／オフを切り替えます。 |
| `GetShowArea() -> bool \| None` | *面積を表示*がオンかどうか。 |
| `SetShowArea(value: bool) -> bool` | *面積を表示*のオン／オフを切り替えます。 |
| `GetAreaUnitsImperial() -> PropertyLineObject.AreaUnits \| None` | インチ系の面積単位を返します。 |
| `SetAreaUnitsImperial(value: PropertyLineObject.AreaUnits) -> bool` | インチ系の面積単位を設定します。 |
| `GetAreaUnitsMetric() -> PropertyLineObject.AreaUnits \| None` | メートル系の面積単位を返します。 |
| `SetAreaUnitsMetric(value: PropertyLineObject.AreaUnits) -> bool` | メートル系の面積単位を設定します。 |
| `GetDistanceUnits() -> str \| None` | 生の距離単位文字列です（完全な一覧はプラグインを参照。例："Feet"、"Meters"など）。 |
| `SetDistanceUnits(value: str) -> bool` | 距離単位を設定します。生の距離単位文字列です（完全な一覧はプラグインを参照。例："Feet"、"Meters"など）。 |

継承メンバー：[`LandmarkObject`](#landmarkobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### PropertyLineObject.AreaUnits

> **完全修飾名:** `api.PropertyLineObject.AreaUnits` · **種類:** `IntEnum`

"Area Units Imperial"と"Area Units Metric"の両方のパラメータが対応する面積単位の選択肢。

| メンバー | 値 | 説明 |
|---|---|---|
| `DocumentUnits` | `0` |  |
| `SquareFeet` | `1` |  |
| `SquareYards` | `2` |  |
| `SquareMiles` | `3` |  |
| `Acres` | `4` |  |
| `SquareMeters` | `5` |  |
| `SquareKilometers` | `6` |  |
| `Hectares` | `7` |  |

### ExistingTreeObject

> **完全修飾名:** `api.ExistingTreeObject` · **継承元:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Landmarkプラグインの既存樹木プラグインオブジェクトです（ユニバーサル名は"Existing Tree"）。

既存樹木は、敷地にすでに存在する一本の樹木を表します。樹種情報、サイズ（高さ、樹冠の直径、幹径）、根域データ（根鉢、重要／主要根域、樹木保護範囲）、および樹木医の方式による状態／重要度／SULE／措置の評価を保持します。

名前付きアクセサーでアクセスできる主なパラメータ：

- "Genus Species" — 学名（ラテン語名）
- "Common Name" — 樹種名
- "Tree No" — タグ／インスタンスの識別子
- "Origin" — Not Set / Endemic / Native / Exotic / Indigenous / Custom
- "Height" — 樹木全体の高さ（ワールド単位）
- "Canopy" — 樹冠の直径（ワールド単位）
- "Calliper" — 胸高直径（DBH）、ワールド単位
- "RootBall" — 根鉢の直径（ワールド単位）
- "CriticalRootZone" — 重要根域の直径（ワールド単位）
- "PrimaryRootZone" — 主要根域の直径（ワールド単位）
- "DisplayTPZ" — None / Circular Zone / Using 12*DBH
- "Condition" — Not Set / Excellent / Good / Average / Poor / Custom
- "SULE" — 耐用年数（安全に利用できる予測余命の区分）
- "Significance" — 重要度の区分
- "ActionComment" — 推奨措置（Retain / Remove / Transplant / ...）
- "Location" — 自由記入の位置の説明
- "Comments" — 自由記入の注記
- "Create3D" — 3D図形を生成

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）種／識別情報

- "Genus Species" — string — 学名（属名＋種名）
- "Common Name" — string
- "Family" — string
- "Tree No" — string — タグ／インスタンスの識別子
- "Origin" — popup — Not Set / Endemic / Native / Exotic / Indigenous / Custom
- "CustomOrigin" — string — Origin = "Custom"の場合の自由記入のOrigin値
- "Invasive" — bool
- "InvasiveSpecies" — bool — （2026+で"Invasive"を置き換え）
- "Elevation" — real — ワールド単位

サイズ（ワールド単位）

- "Height" — real — 樹木全体の高さ
- "Canopy" — real — 樹冠の直径（UseCanopyMin = `False`の場合に使用）
- "UseCanopyMin" — bool — 最小半径にCanopyMinを使用
- "CanopyMin" — real — 最小樹冠直径（不規則な樹冠）
- "CanopyRotate" — real — 度 - 樹冠の回転
- "CanopyArea" — real（読み取り専用、計算値）
- "Hgt First Branch" — real — ワールド単位
- "CrownClearance" — real
- "FirstBranchDir" — popup
- "AddIntercardinalDir" — bool — NE/SE/SW/NW方向の樹冠の半径を含める
- "Calliper" — real — DBH（胸高直径）

根域と樹木保護範囲（TPZ）、ワールド単位

- "RootBall" — real — 根鉢の直径
- "CriticalRootZone" — real — 重要根域（CRZ）の直径
- "PrimaryRootZone" — real — 主要根域（PRZ）の直径
- "RootZones" — popup — None / Critical Zone / Primary Zone / Both Zones / Root Ball
- "EditTPZ" — bool
- "DisplayTPZ" — popup — None / Display Circular Zone / Display Using 12 x DBH
- "TPZCornerRadius" — real
- "TPZRadius" — real
- "TPZArea", "AdjustedTPZArea" — real（読み取り専用）
- "MinSRZRadius" — real
- "DiamAtButtress" — real
- "StructuralRootZone" — bool
- "CalculatedSRZ" — string（読み取り専用、書式設定済み）

樹木医による評価

- "Condition" — popup — Not Set / Excellent / Good / Average / Poor / Custom
- "CustomCondition" — string — Condition = "Custom"の場合の自由記入のCondition値
- "SULE" — popup — Not Set / "Long (40+ yrs)" / "Medium (16-39 yrs)" / "Short (5-15 yrs)" / Removal / Custom
- "CustomSULE" — string
- "Significance" — popup — Not Set / Most Significant / Highly Significant / Less Significant / Least Significant / Hazardous / Custom
- "CustomSignificance" — string
- "ActionComment" — popup — Not Set / Retain / "Retain - Arborist Work Required" / "Transplant - Original Location" / "Transplant - Proposed Location" / Remove / "Remove - Within Building Footprint" / "Remove - Poor Health" / "Remove - Undesirable Species" / Custom
- "CustomAction" — string
- "TreeProtectionOrder" — bool
- "VeteranTree" — bool
- "AncientTree" — bool
- "Form" — popup — Not Set / Excellent / Good / Average / Poor
- "Structure" — popup — Not Set / Excellent / Good / Average / Poor
- "Vigour" — popup — Not Set / Excellent / Good / Average / Poor

追加データ

- "RL" — string — 水準高（高さの基準）
- "Age" — string
- "Year Planted" — string
- "DateAssessed" — string
- "Location" — string
- "Comments" — string — 自由記入の注記
- "Field1..Field10" — string — ユーザー定義の追加フィールド
- "sustainability" — string — JSONデータ塊（VW2026+）
- "VersionInfo" — string（読み取り専用）

株立ちの樹木

- "__UseMultipleStems" — bool
- "__NumStems" — int
- "__Stem1..__Stem10" — real — 各幹の直径、ワールド単位
- "__TrunkPerim" — real — 幹の周長／円周

不規則な樹冠（方向ごとの半径、ワールド単位）

- "__CustomCanopy" — bool
- "__CanopyNorth", "__CanopySouth", "__CanopyEast", "__CanopyWest" — real
- "__CanopyNorthEast", "__CanopySouthEast", "__CanopySouthWest", "__CanopyNorthWest" — real

3D図形

- "Create 3D" — bool
- "UseGenerated3DGeometry" — bool
- "UseLaubwerk3DGeometry" — bool
- "UseImageProp3DGeometry" — bool
- "ImagePropSymbol" — string — 添景のシンボル名
- "__CanopySymbolName", "__TrunkSymbolName", "__RetainSymbolName", "__RemoveSymbolName", "__TransOldSymbolName", "__TransNewSymbolName", "__CustActionSymbolName", "__TransTrunkSymName" — string（シンボルリソース名）
- "__UseSymComponents" — bool
- "__ApplyClassTextures" — bool
- "UseXForRemoveTrees" — bool — 撤去対象の樹木にXマーカーを描画
- "lw_Key", "lw_PlantFile", "lw_Variant" — string — （Laubwerkの3D樹種の選択）
- "lw_GlobalSeason" — bool
- "lw_Season" — string
- "lw_Global2D3DMat" — bool
- "lw_2DReprs", "lw_3DReprs" — string
- "lw_MaterialStyle" — string

タグ／ラベル

- "UseTag" — bool
- "__SnapTagToTrunk" — bool
- "__DisplayTagMarker" — bool
- "__EnableTagShoulder" — bool
- "__TagShoulderAngle" — real — 度
- "__TagShoulderLength" — real — ワールド単位
- "__TagDisplayType" — int
- "__IDClass" — popup — クラス名
- "__FlagNumberDLog", "__FlagNumberDLogFEO" — bool
- "ControlPoint01X..ControlPoint08Y" — real（各種コントロールポイントのワールド座標）

属性の上書き（区域ごとの色／クラス／線の太さ） "__TPZClass", "__RootClass", "__TrunkClass", "__CanopyClass", "__SigClass"		popup（クラス名） "__TPZLineWeight", "__TPZLineStyle", "__TPZLineCol"		int "__PRZLineWeight", "__PRZLineStyle", "__PRZLineCol"		int "__CRZLineWeight", "__CRZLineStyle", "__CRZLineCol"		int

- "__UseSigColours" — bool
- "__Sig1FillCol..__Sig5FillCol" — int — カラーインデックス
- "__SigColDisplay" — int
- "__TrunkType" — int

自動番号付け

- "__AutoNumberDefault" — bool
- "__AutoNumCurrent" — int
- "__AutoNumPrefix", "__AutoNumSuffix" — string
- "__AutoNumZeroDefault" — int
- "__AutoNumberDups" — bool
- "__AutoNumSepLayers" — bool
- "__AutoNumThisTree" — bool
- "__IsAppliedAsTheDocDef" — bool
- "__IsNewDocument" — bool

内部／バージョン管理

- "__UniqueID" — string
- "__LayerName" — string
- "__LineTypes" — string
- "__ETShape", "__ETShapeNum" — int
- "__CustomFieldNum" — int
- "__CustomLabels" — string

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ExistingTreeObject(h: Handle)` | 既存樹木`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D) -> ExistingTreeObject` *静的* | アクティブレイヤ／現在のコンテナの`position`に既存樹木を作成します。 |
| `Duplicate() -> ExistingTreeObject` | 図面内の既存樹木を複製し、そのコピーを返します。 |

*種／識別情報*

| メソッド | 説明 |
|---|---|
| `GetBotanicalName() -> str \| None` | 学名を返します。 |
| `SetBotanicalName(value: str) -> bool` | 学名を設定します。 |
| `GetCommonName() -> str \| None` | 樹種名を返します。 |
| `SetCommonName(value: str) -> bool` | 樹種名を設定します。 |
| `GetTreeNumber() -> str \| None` | 樹木番号（タグ／インスタンスの識別子）を返します。 |
| `SetTreeNumber(value: str) -> bool` | 樹木番号を設定します。 |
| `GetOrigin() -> ExistingTreeObject.Origin \| None` | 原産区分を返します。 |
| `SetOrigin(value: ExistingTreeObject.Origin) -> bool` | 原産区分を設定します。 |
| `GetHeight() -> float \| None` | サイズ（ワールド単位）（全体の高さ）。 |
| `SetHeight(value: float) -> bool` | 高さを設定します（サイズ（ワールド単位））。 |
| `GetCanopyDiameter() -> float \| None` | 樹冠の直径を返します。 |
| `SetCanopyDiameter(value: float) -> bool` | 樹冠の直径を設定します。 |
| `GetCaliper() -> float \| None` | 幹径を返します（DBH：胸高直径）。 |
| `SetCaliper(value: float) -> bool` | 幹径を設定します。 |
| `GetRootBallDiameter() -> float \| None` | 根域（ワールド単位）。 |
| `SetRootBallDiameter(value: float) -> bool` | 根鉢の直径を設定します（根域（ワールド単位））。 |
| `GetCriticalRootZoneDiameter() -> float \| None` | 重要根域の直径を返します。 |
| `SetCriticalRootZoneDiameter(value: float) -> bool` | 重要根域の直径を設定します。 |
| `GetPrimaryRootZoneDiameter() -> float \| None` | 主要根域の直径を返します。 |
| `SetPrimaryRootZoneDiameter(value: float) -> bool` | 主要根域の直径を設定します。 |
| `GetTreeProtectionZone() -> ExistingTreeObject.TreeProtection \| None` | 樹木保護範囲を返します。 |
| `SetTreeProtectionZone(value: ExistingTreeObject.TreeProtection) -> bool` | 樹木保護範囲を設定します。 |
| `GetCondition() -> ExistingTreeObject.Condition \| None` | 状態を返します。 |
| `SetCondition(value: ExistingTreeObject.Condition) -> bool` | 状態を設定します。 |
| `GetSULE() -> ExistingTreeObject.SULE \| None` | SULEを返します。 |
| `SetSULE(value: ExistingTreeObject.SULE) -> bool` | SULEを設定します。 |
| `GetSignificance() -> ExistingTreeObject.Significance \| None` | 重要度を返します。 |
| `SetSignificance(value: ExistingTreeObject.Significance) -> bool` | 重要度を設定します。 |
| `GetActionComment() -> ExistingTreeObject.Action \| None` | 処理/コメントを返します。 |
| `SetActionComment(value: ExistingTreeObject.Action) -> bool` | 処理/コメントを設定します。 |
| `GetLocation() -> str \| None` | 位置（自由記入の位置の説明）を返します。 |
| `SetLocation(value: str) -> bool` | 位置を設定します。 |
| `GetNotes() -> str \| None` | 注記を返します。 |
| `SetNotes(value: str) -> bool` | 注記を設定します。 |
| `GetCreate3D() -> bool \| None` | *3D作成*がオンかどうか。 |
| `SetCreate3D(value: bool) -> bool` | *3D作成*のオン／オフを切り替えます。 |

継承メンバー：[`LandmarkObject`](#landmarkobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### ExistingTreeObject.Origin

> **完全修飾名:** `api.ExistingTreeObject.Origin` · **種類:** `IntEnum`

既存樹木の樹種の原産区分。

| メンバー | 値 | 説明 |
|---|---|---|
| `NotSet` | `0` |  |
| `Endemic` | `1` |  |
| `Native` | `2` |  |
| `Exotic` | `3` |  |
| `Indigenous` | `4` |  |
| `Custom` | `5` |  |

#### ExistingTreeObject.TreeProtection

> **完全修飾名:** `api.ExistingTreeObject.TreeProtection` · **種類:** `IntEnum`

樹木保護範囲の表示

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` |  |
| `CircularZone` | `1` |  |
| `Using12DBH` | `2` |  |

#### ExistingTreeObject.Condition

> **完全修飾名:** `api.ExistingTreeObject.Condition` · **種類:** `IntEnum`

樹木医による評価

| メンバー | 値 | 説明 |
|---|---|---|
| `NotSet` | `0` |  |
| `Excellent` | `1` |  |
| `Good` | `2` |  |
| `Average` | `3` |  |
| `Poor` | `4` |  |
| `Custom` | `5` |  |

#### ExistingTreeObject.SULE

> **完全修飾名:** `api.ExistingTreeObject.SULE` · **種類:** `IntEnum`

安全に利用できる予測余命

| メンバー | 値 | 説明 |
|---|---|---|
| `NotSet` | `0` |  |
| `Long` | `1` |  |
| `Medium` | `2` |  |
| `Short` | `3` |  |
| `Removal` | `4` |  |
| `Custom` | `5` |  |

#### ExistingTreeObject.Significance

> **完全修飾名:** `api.ExistingTreeObject.Significance` · **種類:** `IntEnum`

既存樹木の重要度評価。

| メンバー | 値 | 説明 |
|---|---|---|
| `NotSet` | `0` |  |
| `MostSignificant` | `1` |  |
| `HighlySignificant` | `2` |  |
| `LessSignificant` | `3` |  |
| `LeastSignificant` | `4` |  |
| `Hazardous` | `5` |  |
| `Custom` | `6` |  |

#### ExistingTreeObject.Action

> **完全修飾名:** `api.ExistingTreeObject.Action` · **種類:** `IntEnum`

既存樹木に対する計画措置。

| メンバー | 値 | 説明 |
|---|---|---|
| `NotSet` | `0` |  |
| `Retain` | `1` |  |
| `RetainArborist` | `2` |  |
| `TransplantOriginal` | `3` |  |
| `TransplantProposed` | `4` |  |
| `Remove` | `5` |  |
| `RemoveBuildingFootprint` | `6` |  |
| `RemovePoorHealth` | `7` |  |
| `RemoveSpecies` | `8` |  |
| `Custom` | `9` |  |

---

[一覧に戻る](README.md) · [先頭に戻る](#objectslandmark--plants-site-models-hardscapes-and-other-landscape-objects)
