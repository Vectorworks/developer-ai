[English](../../PythonAPI/v2027.2/ObjectsAnnotation.md) • [Deutsch](../../PythonAPI.de/v2027.2/ObjectsAnnotation.md) • **日本語**

<a id="objectsannotation--dimensions-data-tags-title-block-borders-and-worksheets"></a>

# ObjectsAnnotation — 寸法、データタグ、図面枠、ワークシート

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

注釈のクラスです。注釈オブジェクトは建物ではなく図面を記述します。オブジェクトやファイルからデータを読み取り、シートに表示します。

`AnnotationObject`はプラグインベースの注釈の基底クラスです（`DataTagObject`はオブジェクトから読み取ったデータでラベルを付け、`TitleBlockBorderObject`はシートの枠、枠の区域/グリッド、表題欄を表します）。どちらもオブジェクトの**スタイル**から図形を取得するため、`Create`関数はスタイルを解決し（図面にない場合はVectorworksのコンテンツから取り込み）、利用できるスタイルがない場合は失敗します。

寸法は注釈のもう一つの要素です。`DimensionObject`はすべての寸法に共通する設定を保持し、`LinearDimensionObject`、`AngularDimensionObject`、`ArcLengthDimensionObject`、`RadialDimensionObject`は距離、角度、円弧長、半径／直径を測定します。データタグや図面枠とは異なり、寸法はプラグインレコードやスタイルを持たないネイティブオブジェクトで、参照する寸法規格によって外観が決まります。`CenterMarkObject`は円または円弧の中心を示す十字です（寸法ではなく線のグループ）。`WorksheetObject`はワークシートリソースを編集します。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [AnnotationObject](#annotationobject)
  - [DataTagObject](#datatagobject)
    - [DataTagObject.LeaderType](#datatagobjectleadertype)
    - [DataTagObject.HorizontalPosition](#datatagobjecthorizontalposition)
    - [DataTagObject.MoveBehaviour](#datatagobjectmovebehaviour)
  - [TitleBlockBorderObject](#titleblockborderobject)
    - [TitleBlockBorderObject.Revision](#titleblockborderobjectrevision)
  - [DimensionObject](#dimensionobject)
  - [LinearDimensionObject](#lineardimensionobject)
  - [AngularDimensionObject](#angulardimensionobject)
  - [ArcLengthDimensionObject](#arclengthdimensionobject)
  - [RadialDimensionObject](#radialdimensionobject)
  - [CenterMarkObject](#centermarkobject)
  - [WorksheetObject](#worksheetobject)
    - [WorksheetObject.Range](#worksheetobjectrange)
    - [WorksheetObject.NumberFormat](#worksheetobjectnumberformat)
    - [WorksheetObject.TextFormat](#worksheetobjecttextformat)
    - [WorksheetObject.Fill](#worksheetobjectfill)
    - [WorksheetObject.Borders](#worksheetobjectborders)
- [列挙型](#enumerations)
  - [DimensionKind](#dimensionkind)
  - [DimensionTolerance](#dimensiontolerance)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`AnnotationObject`](#annotationobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | 注釈プラグインオブジェクトのクラス（データタグ、図面枠）に共通する基底クラスです。 |
| [`DataTagObject`](#datatagobject) | クラス | [`AnnotationObject`](#annotationobject) | データタグプラグインオブジェクトです（ユニバーサル名は"Data Tag"）。 |
| [`DataTagObject.LeaderType`](#datatagobjectleadertype) | IntEnum（入れ子） |  | データタグの引出線の種類です（"Leader Type"）。 |
| [`DataTagObject.HorizontalPosition`](#datatagobjecthorizontalposition) | IntEnum（入れ子） |  | タグのテキストを引出線のどちら側に配置するかを指定します（"Horizontal Position"）。 |
| [`DataTagObject.MoveBehaviour`](#datatagobjectmovebehaviour) | IntEnum（入れ子） |  | 図面でタグをドラッグした際に移動する対象です。タグ全体、または引出線の先端のみを移動します。 |
| [`TitleBlockBorderObject`](#titleblockborderobject) | クラス | [`AnnotationObject`](#annotationobject) | 図面枠プラグインオブジェクトです（ユニバーサル名は"Title Block Border"）。 |
| [`TitleBlockBorderObject.Revision`](#titleblockborderobjectrevision) | クラス（入れ子） |  | 表題欄の一つの改訂です。番号、日付、注記、発行日、受信者を含みます。 |
| [`DimensionObject`](#dimensionobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | すべての寸法線オブジェクトの基底クラスです（`ObjectType.Dimension`）。 |
| [`LinearDimensionObject`](#lineardimensionobject) | クラス | [`DimensionObject`](#dimensionobject) | 長さ寸法です。二点間の距離を測定します。 |
| [`AngularDimensionObject`](#angulardimensionobject) | クラス | [`DimensionObject`](#dimensionobject) | 角度寸法です。頂点で交わる二辺の間の角度を測定します。 |
| [`ArcLengthDimensionObject`](#arclengthdimensionobject) | クラス | [`DimensionObject`](#dimensionobject) | 円弧長寸法です。長さ寸法が示す両端間の直線距離ではなく、円弧に沿った長さを測定します。 |
| [`RadialDimensionObject`](#radialdimensionobject) | クラス | [`DimensionObject`](#dimensionobject) | 半径寸法および直径寸法です。円または円弧の半径または直径を測定します。 |
| [`CenterMarkObject`](#centermarkobject) | クラス | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | センターマークです。円または円弧の中心を示す十字です。 |
| [`WorksheetObject`](#worksheetobject) | クラス | [`TypedResource`](Resources.md#typedresource) | 所有権を持たないワークシートリソースです。配置されたワークシートイメージや注釈のプラグインオブジェクトではありません。 |
| [`WorksheetObject.Range`](#worksheetobjectrange) | クラス（入れ子） |  | 両端を含む、1から始まるワークシートの範囲です。 |
| [`WorksheetObject.NumberFormat`](#worksheetobjectnumberformat) | クラス（入れ子） |  | ワークシート固有の数字の表示形式です。書式に応じた精度とUTF-8の前記号／後記号を含みます。 |
| [`WorksheetObject.TextFormat`](#worksheetobjecttextformat) | クラス（入れ子） |  | ワークシートのテキストです。ポイントサイズ、フォント／スタイル、配置、度単位の角度、ColorRefインデックス、折り返しを含みます。 |
| [`WorksheetObject.Fill`](#worksheetobjectfill) | クラス（入れ子） |  | ネイティブの面のスタイル、ファイルのColorRefインデックス、模様です。 |
| [`WorksheetObject.Borders`](#worksheetobjectborders) | クラス（入れ子） |  | セルの枠線フラグと、範囲の外枠および内側への適用フラグです。 |
| [`DimensionKind`](#dimensionkind) | IntEnum |  | オブジェクトの寸法の種類です。 |
| [`DimensionTolerance`](#dimensiontolerance) | IntEnum |  | 寸法の公称値からのずれの量です。測定値の隣に表示されます。 |

<a id="classes"></a>

## クラス

### AnnotationObject

> **完全修飾名:** `api.AnnotationObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

注釈プラグインオブジェクトのクラス（データタグ、図面枠）に共通する基底クラスです。

注釈オブジェクトは建物の一部分ではなく、図面を記述します。オブジェクトやファイルからデータを読み取り、シートに表示します。どちらの注釈オブジェクトもVectorworksのプラグインオブジェクト（APIではパラメトリックオブジェクトとも呼ばれます）であり、ユニバーサル（パラメトリック）名の"Data Tag"と"Title Block Border"で識別されます。

これら二つがArchitect／Landmarkのクラスと異なるのは、図形のほぼすべてがプラグインスタイル（オブジェクトスタイル）から取得される点です。これは、プラグインのマスターインスタンスと、そのスタイルを使用するすべてのオブジェクトに適用されるテキストおよび図形のレイアウトを保持するシンボル定義です。スタイルのないデータタグにはテキストレイアウトがなく、スタイルのない図面枠には表題欄の図形がありません。そのため、両クラスはオブジェクトの作成時にスタイルを解決し（`DataTagObject.Create`と`TitleBlockBorderObject.Create`を参照）、GetStyleName / SetStyleを通してスタイルにアクセスできるようにします。

PrimitiveObjectから引き継がれる規約：

- ゲッターは、オブジェクトが無効な場合やパラメータがない場合に`None`を返します。
- セッターは成功時に`True`を返し、オブジェクトが無効な場合やパラメータがない場合に`False`を返します。
- 長さはワールド単位、角度はラジアン、文字列はUTF-8です。

パラメータアクセスの基本（Get/SetParam*）：

- すべての注釈オブジェクトは、名前付きフィールド（「パラメータ」）を持つレコードとしてデータを格納します。各サブクラスの「全パラメータリファレンス」に、便利なパラメータ名が一覧表示されています。サブクラスに専用の型付きアクセサーがないフィールドの読み書きには、GetParamString / SetParamString / GetParamReal / ...でそれらの名前をそのまま使用してください（大文字と小文字を区別し、UTF-8を使用）。
- 表内のパラメータ型には、次のタグを使用します：

- string — テキスト（UTF-8）- GetParamString / SetParamString
- int — 32ビット整数 - GetParamInt / SetParamInt
- bool — ブール値 - GetParamBool / SetParamBool
- real — 浮動小数点数（ワールド座標、度単位の角度、通常の数値など）- GetParamReal / SetParamReal
- popup — N個の文字列から一つを選択 - GetParamString / SetParamString。有効な値はパラメータの隣に記載されています

- 二重アンダースコア（"__"）で始まるパラメータ名はプラグインの内部状態です。読み取りはできますが、通常は直接変更しても意味がありません。
- オブジェクトで「スタイルを使用」に設定されたパラメータは、スタイルのシンボル定義から読み取られます。そのパラメータを「インスタンスを使用」に切り替えるまでは、インスタンスに書き込んでも効果は持続しません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `AnnotationObject(h: Handle)` | 任意のオブジェクト`h`を汎用の`AnnotationObject`として参照します。`IsValid()`はハンドルがnullでないことだけを確認します。オブジェクトの種類は`GetParametricName()`または具象クラスの`Is(h)`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `GetParametricName() -> str \| None` | このオブジェクトのユニバーサル（パラメトリック）名で、"Data Tag"または"Title Block Border"です。オブジェクトが無効な場合や、元のハンドルがプラグインオブジェクトではない場合は空です。 |
| `HasParam(univParamName: str) -> bool` | このプラグインオブジェクトが、指定されたユニバーサル名のフィールドを持つかどうか。 |
| `GetParamNames() -> list[str]` | このオブジェクトのプラグインで定義されたすべてのパラメータ（ユニバーサル）名の順序付きリストです。 |
| `GetParamString(univParamName: str) -> str \| None` | 文字列をキーとする汎用のフィールドアクセサーです。サブクラスに型付きの名前付きアクセサーがある場合は、そちらを優先してください。専用アクセサーのないパラメータには、これらを使用します。パラメータが存在しない場合、ゲッターは`None`、セッターは`False`を返します。 |
| `SetParamString(univParamName: str, value: str) -> bool` | パラメータの文字列を設定します。文字列をキーとする汎用のフィールドアクセサーです。サブクラスに型付きの名前付きアクセサーがある場合は、そちらを優先してください。専用アクセサーのないパラメータには、これらを使用します。パラメータが存在しない場合、ゲッターは`None`、セッターは`False`を返します。 |
| `GetParamReal(univParamName: str) -> float \| None` | `univParamName`の実数パラメータを返します。 |
| `SetParamReal(univParamName: str, value: float) -> bool` | 実数パラメータを設定します。 |
| `GetParamBool(univParamName: str) -> bool \| None` | `univParamName`の*ブール型パラメータ*がオンかどうか。 |
| `SetParamBool(univParamName: str, value: bool) -> bool` | ブール型パラメータを設定します。 |
| `GetParamInt(univParamName: str) -> int \| None` | `univParamName`の整数パラメータを返します。 |
| `SetParamInt(univParamName: str, value: int) -> bool` | 整数パラメータを設定します。 |

*プラグインスタイル*

| メソッド | 説明 |
|---|---|
| `GetStyleHandle() -> Handle` | オブジェクトに関連付けられたスタイルのシンボル定義です。スタイルがない場合はnullです。 |
| `GetStyleName() -> str \| None` | そのスタイルリソースの名前です。スタイルがない場合やオブジェクトが無効な場合は`None`です。 |
| `IsStyled() -> bool` | オブジェクトがプラグインスタイルを使用している場合はTrueです。 |
| `SetStyle(styleName: str) -> bool` | 現在の図面の`styleName`という名前のスタイルリソースにオブジェクトを関連付け、スタイルで指定されるパラメータ値を引き継ぎます。そのリソースが存在しない場合やプラグインスタイルではない場合は失敗します。サブクラスには、最初にVectorworksのコンテンツからスタイルを取り込む静的なEnsure*`Style()`が追加されています。 |
| `SetStyle(hStyleSymbolDefinition: Handle) -> bool` | 現在の図面の`styleName`という名前のスタイルリソースにオブジェクトを関連付け、スタイルで指定されるパラメータ値を引き継ぎます。そのリソースが存在しない場合やプラグインスタイルではない場合は失敗します。サブクラスには、最初にVectorworksのコンテンツからスタイルを取り込む静的なEnsure*`Style()`が追加されています。 |
| `RemoveStyle() -> bool` | オブジェクトとスタイルの関連付けを解除します。すべてのパラメータが「インスタンスを使用」になり、現在の値を保持します。 |

継承メンバー：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### DataTagObject

> **完全修飾名:** `api.DataTagObject` · **継承元:** [`AnnotationObject`](#annotationobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

データタグプラグインオブジェクトです（ユニバーサル名は"Data Tag"）。

データタグは、オブジェクトから読み取ったデータでそのオブジェクトにラベルを付けます。データにはレコードフィールド、プラグインパラメータ、クラス、属性、ワークシートの数式などがあります。タグのテキストレイアウト、すなわちどのフィールドをどのように配置し、どの囲みの中に表示するかは、すべてタグのスタイル（プラグインスタイルのシンボル定義）に格納されます。そのため、スタイルのないデータタグには何も表示されません。これが、`Create()`が常にスタイルを解決し（図面にない場合はVectorworksのコンテンツから取り込み）、どこにも利用可能なデータタグスタイルがない場合に失敗する理由です。

タグを使用するためのもう一つの要素は、記述対象のオブジェクトとの関連付けです。タグは関連付けられたオブジェクトからデータを読み取り、そのオブジェクトが移動すると追従します。`Create()`はタグを付けるオブジェクトを受け取ります。後から変更するにはAttachTo / DetachFromを使用します。

名前付きアクセサーでアクセスできる主なパラメータ：

- "Use Leader" — タグを付けたオブジェクトへの引出線を描画するかどうか
- "Leader Type" — その引出線の種類（後述の`DataTagObject.LeaderType`を参照）
- "Leader Length" — 引出線の長さ、ワールド単位
- "Leader Angle" — 引出線の角度（アクセサーではラジアン、生のパラメータでは度を使用）
- "Shoulder Length" — 引出線とテキストの間にある水平線の長さ
- "Horizontal Position" — 引出線のどちら側にテキストを配置するか（`DataTagObject.HorizontalPosition`を参照）
- "Move Behaviour" — タグをドラッグした際の移動対象（`DataTagObject.MoveBehaviour`を参照）
- "X Offset"/"Y Offset" — タグを付けたオブジェクトからのタグのオフセット、ワールド単位

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）引出線と水平線

- "Use Leader" — bool
- "Leader Type" — popup — Line / Arc / Bezier
- "Leader Length" — real — ワールド単位
- "Leader Angle" — real — 度
- "Leader Radius" — real — ワールド単位（円弧の引出線）
- "Shoulder Length" — real — ワールド単位
- "Use Marker" — bool — 引出線の端にマーカーを描画
- "Clip Leader" — bool
- "Leader/Shoulder Class" — string — 引出線と水平線の図形のクラス
- "__Marker", "__Marker Style", "__Marker Angle", "__Marker Size", "__Marker Width", "__Marker Thickness Basis", "__Marker Thickness" — マーカーの定義（内部）
- "__Bezier Length Factor 1/2", "__Bezier Offset1/2" — ベジェ引出線の形状（内部）
- "__LeaderEndX", "__LeaderEndY" — real — 関連付けられていない引出線のローカル座標（Get/SetLeaderEndを使用）

配置

- "Horizontal Position" — popup — Left / Right / Auto
- "Move Behaviour" — popup — Entire Tag / Leader End
- "Offset Mode" — popup — Global / Local
- "X Offset", "Y Offset" — real — ワールド単位
- "Align to Walls" — bool
- "Wall Alignment" — popup — Unconstrained / Center Line / Left Edge / Right Edge
- "World-based" — bool — ビューではなくワールドに合わせてタグの向きを保持
- "MirrorElements" — bool
- "Allow Mult Att Points" — bool
- "__RefOffsetX/Y/Z", "__RefCenterX/Y/Z", "__MoveOffsetX/Y/Z" — real（内部の配置状態）
- "__RefWallOffset", "__IsRefWallLeftSide", "__RefOffsetFromWall", "__RefWallCenterOffse", "__IsRefWallCenterLeftSide", "__RefCenterOffsetFromWall" — （内部）

拡大縮小

- "Scaling" — popup — None / Symmetric / Asymmetric
- "Scale Text" — bool
- "X Scale", "Y Scale" — real

適合性（このタグを関連付けられるオブジェクト）

- "UseCriteriaEligibility" — bool
- "__CriteriaEligibility" — string — Vectorworksの検索条件、例："((ALL))"
- "SubpartMode" — bool — オブジェクト自体ではなく、その部分にタグを付ける
- "EnableOverlappingVerticalChains" — bool

ダイアログ／内部状態

- "Always Display ETD Dialog" — bool
- "__Edit Tag Layout" — string — （オブジェクト情報パレット内の固定テキストのプレースホルダー）
- "__Was Moved", "__Is For Updating", "__Is For Moving", "__Was Rotated From OIP" — bool
- "__IsCompensateAngleUsed", "__IsBubbleFlipped" — bool
- "__Version" — int

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DataTagObject(h: Handle)` | 既存のデータタグ`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D, styleName: str = '', hObjectToTag: Handle = None) -> DataTagObject` *静的* | `position`に、`hObjectToTag`にタグを付けるデータタグを作成します（独立したタグではnullを指定できます）。`styleName`でデータタグスタイルを選択します。まず図面内で検索し、まだ存在しない場合はVectorworksのデータタグコンテンツから取り込みます。利用可能な任意のスタイルを使用するには空にしてください。データタグスタイルがまったく見つからない場合は無効なオブジェクトを返します。スタイルのないタグにはテキストレイアウトがなく、表示されないためです。 |
| `EnsureStyle(styleName: str = '') -> str` *静的* | 必要に応じてVectorworksのコンテンツから取り込み、`styleName`という名前のデータタグスタイルを現在の図面で利用可能にします。利用可能になったスタイルの名前（要求したスタイルが存在しない場合は、その名前と異なることがあります）、またはスタイルがない場合は空の文字列を返します。 |
| `Duplicate() -> DataTagObject` | 図面内のデータタグを複製し、そのコピーを返します。 |

*関連付け*

| メソッド | 説明 |
|---|---|
| `GetTaggedObject() -> Handle` | このタグのデータ読み取り元となるオブジェクトです。何にも関連付けられていないタグではnullです。 |
| `AttachTo(hObject: Handle) -> bool` | タグを`hObject`に関連付け（現在の関連付けを置き換え）、タグのテキストを更新します。 |
| `DetachFrom(hObject: Handle = None) -> bool` | タグと`hObject`の関連付けを解除します。現在のタグ付け対象との関連付けを解除するにはnullを渡してください。 |
| `CanBeTagged(hObject: Handle) -> bool` *静的* | `hObject`が、データタグを関連付けられる種類のオブジェクトかどうか。 |
| `GetTagsOfObject(hObject: Handle) -> list[Handle]` *静的* | `hObject`に関連付けられているすべてのデータタグです。 |

*内容*

| メソッド | 説明 |
|---|---|
| `GetExtractedData() -> list[tuple[str, str]]` | タグが現在表示しているデータを、(label, value)の組として示します。ラベルはタグレイアウトで定義されたフィールドラベルで、値はタグを付けたオブジェクトについて実際に表示されるテキストです。 |
| `Update() -> bool` | タグを付けたオブジェクトからデータを再度読み取り、タグを再描画します。 |

*引出線*

| メソッド | 説明 |
|---|---|
| `GetUseLeader() -> bool \| None` | *引出線を表示*がオンかどうか。 |
| `SetUseLeader(value: bool) -> bool` | *引出線を表示*のオン／オフを切り替えます。 |
| `GetLeaderType() -> DataTagObject.LeaderType \| None` | 引出線の種類を返します。 |
| `SetLeaderType(value: DataTagObject.LeaderType) -> bool` | 引出線の種類を設定します。 |
| `GetLeaderLength() -> float \| None` | 引出線の長さを返します（ワールド単位）。 |
| `SetLeaderLength(value: float) -> bool` | 引出線の長さを設定します。 |
| `GetLeaderAngle() -> float \| None` | 引出線の角度を返します（ラジアン）。 |
| `SetLeaderAngle(radians: float) -> bool` | 引出線の角度を設定します。 |
| `GetShoulderLength() -> float \| None` | 水平線の長さを返します（ワールド単位）。 |
| `SetShoulderLength(value: float) -> bool` | 水平線の長さを設定します。 |
| `GetUseMarker() -> bool \| None` | *マーカーを使用*がオンかどうか。 |
| `SetUseMarker(value: bool) -> bool` | *マーカーを使用*のオン／オフを切り替えます。 |
| `GetLeaderEnd() -> Math.Point2D \| None` | 引出線の先端です。ワールド単位で指定します。設定すると、タグのテキストを移動せずに引出線の端を移動します。関連付けられたタグと関連付けられていないタグのいずれでも、グローバル／モデルXY座標を使用します。取得には、有効な引出線とネイティブの引出線プロバイダーが必要です。囲んでいるプラグインオブジェクトが傾いている場合は空です（プロバイダーはXYのみ対応）。 |
| `SetLeaderEnd(position: Math.Point2D) -> bool` | 引出線の端を設定します。引出線の先端です。ワールド単位で指定します。設定すると、タグのテキストを移動せずに引出線の端を移動します。関連付けられたタグと関連付けられていないタグのいずれでも、グローバル／モデルXY座標を使用します。取得には、有効な引出線とネイティブの引出線プロバイダーが必要です。囲んでいるプラグインオブジェクトが傾いている場合は空です（プロバイダーはXYのみ対応）。 |

*配置*

| メソッド | 説明 |
|---|---|
| `GetHorizontalPosition() -> DataTagObject.HorizontalPosition \| None` | 水平位置を返します。 |
| `SetHorizontalPosition(value: DataTagObject.HorizontalPosition) -> bool` | 水平位置を設定します。 |
| `GetMoveBehaviour() -> DataTagObject.MoveBehaviour \| None` | 移動動作を返します。 |
| `SetMoveBehaviour(value: DataTagObject.MoveBehaviour) -> bool` | 移動動作を設定します。 |
| `GetOffset() -> Math.Point2D \| None` | タグを付けたオブジェクトからのタグのオフセットです。ワールド単位で指定します。 |
| `SetOffset(offset: Math.Point2D) -> bool` | オフセットを設定します。タグを付けたオブジェクトからのタグのオフセットです。ワールド単位で指定します。 |
| `GetAlignToWalls() -> bool \| None` | *壁/オブジェクトに揃える*がオンかどうか。 |
| `SetAlignToWalls(value: bool) -> bool` | *壁/オブジェクトに揃える*のオン／オフを切り替えます。 |

*適合性*

| メソッド | 説明 |
|---|---|
| `GetUseCriteriaEligibility() -> bool \| None` | タグを関連付けられるオブジェクトを、検索条件文字列で制限するかどうか。 |
| `SetUseCriteriaEligibility(value: bool) -> bool` | *適合性の条件を使用*のオン／オフを切り替えます。タグを関連付けられるオブジェクトを、検索条件文字列で制限するかどうか。 |
| `GetEligibilityCriteria() -> str \| None` | 制限がオンの場合に使用されるVectorworksの検索条件文字列です。例："((ALL))"または"((PON=`Door`))"。 |
| `SetEligibilityCriteria(criteria: str) -> bool` | 適合性の条件を設定します。制限がオンの場合に使用されるVectorworksの検索条件文字列です。例："((ALL))"または"((PON=`Door`))"。 |

継承メンバー：[`AnnotationObject`](#annotationobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### DataTagObject.LeaderType

> **完全修飾名:** `api.DataTagObject.LeaderType` · **種類:** `IntEnum`

データタグの引出線の種類です（"Leader Type"）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Line` | `0` |  |
| `Arc` | `1` |  |
| `Bezier` | `2` |  |

#### DataTagObject.HorizontalPosition

> **完全修飾名:** `api.DataTagObject.HorizontalPosition` · **種類:** `IntEnum`

タグのテキストを引出線のどちら側に配置するかを指定します（"Horizontal Position"）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Left` | `0` |  |
| `Right` | `1` |  |
| `Auto` | `2` |  |

#### DataTagObject.MoveBehaviour

> **完全修飾名:** `api.DataTagObject.MoveBehaviour` · **種類:** `IntEnum`

図面でタグをドラッグした際に移動する対象です。タグ全体、または引出線の先端のみを移動します。

| メンバー | 値 | 説明 |
|---|---|---|
| `EntireTag` | `0` |  |
| `LeaderEnd` | `1` |  |

### TitleBlockBorderObject

> **完全修飾名:** `api.TitleBlockBorderObject` · **継承元:** [`AnnotationObject`](#annotationobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

図面枠プラグインオブジェクトです（ユニバーサル名は"Title Block Border"）。

図面枠はシートの枠です。余白と枠の区域/グリッドを備えたシートの枠に加え、隅に配置され、物件名、施主、シートレイヤ番号、縮尺、版情報および改訂情報の履歴などを表示するテキストブロックである表題欄自体を含みます。通常はシートレイヤに、シートごとに一つ配置します。

データタグと同様、図形はスタイル（プラグインスタイルのシンボル定義）に格納されます。スタイルによって表題欄の外観と表示するフィールドが決まります。スタイルのない図面枠は空の枠しか描画しません。そのため、`Create()`はスタイルを解決し（図面にない場合はVectorworksの図面枠コンテンツから取り込み）、利用できるスタイルがない場合は失敗します。

表題欄に表示するデータは、次の三か所から取得します：

- オブジェクト自体のパラメータ（枠のサイズ、余白、区域、方位記号、図面スタンプなど）。後述の型付きアクセサーおよびGet/SetParam...を使用してアクセスします。
- 図面情報。図面枠ごとに格納される名前付きフィールドの集合です（シートレイヤタイトル、シートレイヤ番号、設計者名、確認者など）。GetSheetData / SetSheetDataを参照してください。
- プロジェクトデータ。ファイルごとに一度だけ格納され、すべての図面枠で共有する名前付きフィールドの集合です（物件名、施主、住所など）。静的なGetProjectData / SetProjectDataを参照してください。

改訂情報と版情報はGetRevisions / GetIssueDatesで読み取ります。

GetParam.../SetParam...の全パラメータリファレンス（パラメータ名 | 型 | 注記／選択肢）シート

- "Sheet Size ID" — int — 定義済み枠のサイズのインデックス。カスタムサイズは-1
- "Sheet Size Name" — string — 例："ANSI D"、"ISO A1"
- "Sheet Width", "Sheet Height" — real — ワールド単位（カスタムサイズ）
- "Sheet Orientation" — popup — portrait / landscape
- "Sheet Fit Method" — popup — 枠をページに合わせる方法
- "Lock To Page Center" — bool
- "Sheet Margin Left/Right/Top/Bottom" — real — ワールド単位
- "Sheet Hide Border" — bool
- "Border Use Object Line Weight" — bool
- "Border Line Weight" — real
- "Sheet Fill Border" — bool
- "Display Format" — popup
- "Units" — popup — 枠のサイズの表示単位
- "Show unit mark" — bool
- "Use custom name" — bool

シートの区域（枠に沿って表示されるA/B/C - 1/2/3グリッド） "Show Grids", "Show Grid Lines", "Show Grid Lines Extensions"	bool

- "Vertical Zones", "Horizontal Zones" — int
- "Grid Text Order", "Grid Number Order" — popup
- "Grid Label Size" — real
- "Grid Marker Line Length" — real
- "Draw Crop Marks" — bool
- "Crop Marks Line Weight" — real
- "Fold Mark" — popup
- "Fold Mark Class" — string
- "Margin Width", "Folded Width", "Folded Height" — real
- "Zoom In to Title Block" — bool
- "Graphics Scale" — real
- "__Version" — int

表題欄

- "Use As Title Block" — bool — 枠だけでなく表題欄も描画
- "Title Block Position" — popup — 表題欄を配置するシートの隅
- "Title Block Margin" — real
- "Scale Factor" — real
- "Use Layout Text Attributes" — bool
- "Countersignature" — bool
- "This Title Block Is Active" — bool — ファイルの図面情報を供給する表題欄
- "Use Auto Drawing Coordination" — bool

図面情報／改訂情報／版情報

- "Plot Date Format" — popup
- "Scale" — string
- "Date" — string
- "Current Revision Number" — string
- "Show Revisions Count" — int — 表示する改訂行の数
- "Revision Line Spacing" — real
- "Revision Direction" — popup — up / down
- "Current Issue Number" — string
- "Show Issues Count" — int
- "Issue Line Spacing" — real
- "Issue Direction" — popup
- "Issue Increment", "Revision Increment" — int
- "Issue Mark", "Revision Mark" — string

方位記号

- "Display North Arrow" — bool
- "North Arrow Symbol" — string — シンボル定義名
- "North Angle" — real — 度（GetNorthAngle/SetNorthAngleではラジアンを使用）
- "North Scale Factor" — real
- "Selected Heliodon City", "Selected Heliodon Country" — string
- "Use Heliodon Rotation Angle" — bool
- "Show MN Declination" — bool
- "Declination Degree Offset" — real — 度
- "North Default Position X", "North Default Position Y" — real — ワールド単位

図面スタンプ（「仮図面 - 施工用ではありません」の重ね表示）

- "Display Drawing Stamp" — bool
- "Stamp Text" — popup — 定義済みのスタンプテキスト
- "Custom Text" — string — "Stamp Text"でカスタム項目を選択した場合に使用
- "Stamp Text Style" — string
- "Stamp Text Size" — real
- "Stamp Text Size Unit" — popup
- "Use ALL CAPS" — bool
- "Append Date" — bool
- "Stamp Date" — string
- "Stamp Angle" — real — 度
- "Stamp Default Position X", "Stamp Default Position Y" — real — ワールド単位

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `TitleBlockBorderObject(h: Handle)` | 既存の図面枠`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D, styleName: str = '') -> TitleBlockBorderObject` *静的* | 左下隅の領域が`position`に来るように図面枠を作成します。`styleName`で図面枠スタイルを選択します。まず図面内で検索し、まだ存在しない場合はVectorworksの図面枠コンテンツから取り込みます。利用可能な任意のスタイルを使用するには空にしてください。図面枠スタイルが見つからない場合は無効なオブジェクトを返します。スタイルのない図面枠には表題欄の図形がないためです。 |
| `EnsureStyle(styleName: str = '') -> str` *静的* | 必要に応じてVectorworksのコンテンツから取り込み、`styleName`という名前の図面枠スタイルを現在の図面で利用可能にします。利用可能になったスタイルの名前（要求したスタイルが存在しない場合は、その名前と異なることがあります）を返します。スタイルがない場合は空です。 |
| `Duplicate() -> TitleBlockBorderObject` | 図面内の図面枠を複製し、そのコピーを返します。 |

*シート*

| メソッド | 説明 |
|---|---|
| `GetSheetSizeName() -> str \| None` | 定義済み枠のサイズの名前です。例："ANSI D"または"ISO A1"。 |
| `SetSheetSizeName(name: str) -> bool` | 枠のサイズ名を設定します。定義済み枠のサイズの名前です。例："ANSI D"または"ISO A1"。 |
| `GetSheetWidth() -> float \| None` | カスタムの枠のサイズです。ワールド単位で指定します。オブジェクトがカスタムサイズを使用している場合にのみ意味があります。 |
| `SetSheetWidth(value: float) -> bool` | 枠の幅を設定します。カスタムの枠のサイズです。ワールド単位で指定します。オブジェクトがカスタムサイズを使用している場合にのみ意味があります。 |
| `GetSheetHeight() -> float \| None` | シートの高さを返します。 |
| `SetSheetHeight(value: float) -> bool` | シートの高さを設定します。 |
| `GetMarginLeft() -> float \| None` | シートの余白です。ワールド単位で指定します。 |
| `GetMarginRight() -> float \| None` | 右余白を返します。 |
| `GetMarginTop() -> float \| None` | 上余白を返します。 |
| `GetMarginBottom() -> float \| None` | 下余白を返します。 |
| `SetMargins(left: float, right: float, top: float, bottom: float) -> bool` | 余白を設定します。 |

*枠の区域/グリッド*

| メソッド | 説明 |
|---|---|
| `GetShowGrids() -> bool \| None` | *区域番号を表示*がオンかどうか。 |
| `SetShowGrids(value: bool) -> bool` | *区域番号を表示*のオン／オフを切り替えます。 |
| `GetHorizontalZones() -> int \| None` | 水平方向の区域を返します。 |
| `SetHorizontalZones(count: int) -> bool` | 水平方向の区域を設定します。 |
| `GetVerticalZones() -> int \| None` | 垂直方向の区域を返します。 |
| `SetVerticalZones(count: int) -> bool` | 垂直方向の区域を設定します。 |
| `GetDrawCropMarks() -> bool \| None` | *外枠表示*がオンかどうか。 |
| `SetDrawCropMarks(value: bool) -> bool` | *外枠表示*のオン／オフを切り替えます。 |

*表題欄*

| メソッド | 説明 |
|---|---|
| `GetUseAsTitleBlock() -> bool \| None` | オブジェクトが表題欄を描画するか、シートの枠のみを描画するか。 |
| `SetUseAsTitleBlock(value: bool) -> bool` | *表題欄のみ使用*のオン／オフを切り替えます。オブジェクトが表題欄を描画するか、シートの枠のみを描画するか。 |
| `GetIsActiveTitleBlock() -> bool \| None` | ファイルの図面情報読み取り元となる表題欄かどうか（シートごとに一つ）。 |
| `SetIsActiveTitleBlock(value: bool) -> bool` | *アクティブな表題欄*のオン／オフを切り替えます。ファイルの図面情報読み取り元となる表題欄かどうか（シートごとに一つ）。 |

*方位記号*

| メソッド | 説明 |
|---|---|
| `GetDisplayNorthArrow() -> bool \| None` | *方位記号を表示*がオンかどうか。 |
| `SetDisplayNorthArrow(value: bool) -> bool` | *方位記号を表示*のオン／オフを切り替えます。 |
| `GetNorthAngle() -> float \| None` | 北の角度を返します（ラジアン）。 |
| `SetNorthAngle(radians: float) -> bool` | 北の角度を設定します。 |

*図面スタンプ*

| メソッド | 説明 |
|---|---|
| `GetDisplayDrawingStamp() -> bool \| None` | *図面スタンプを表示*がオンかどうか。 |
| `SetDisplayDrawingStamp(value: bool) -> bool` | *図面スタンプを表示*のオン／オフを切り替えます。 |
| `GetDrawingStampText() -> str \| None` | スタンプに表示する自由入力のテキストです。スタンプテキストをカスタム項目に設定した場合に使用します。 |
| `SetDrawingStampText(text: str) -> bool` | 図面スタンプのテキストを設定します。スタンプに表示する自由入力のテキストです。スタンプテキストをカスタム項目に設定した場合に使用します。 |

*図面情報*

| メソッド | 説明 |
|---|---|
| `GetSheetDataFieldNames() -> list[str]` | 図面情報のフィールド名を返します。 |
| `GetSheetData(fieldName: str) -> str \| None` | `fieldName`の図面情報を返します。 |
| `SetSheetData(fieldName: str, value: str) -> bool` | 図面情報を設定します。 |
| `GetAllSheetData() -> list[tuple[str, str]]` | この表題欄のすべての図面情報フィールドを、（フィールド名、値）の組として示します。 |

*プロジェクトデータ*

| メソッド | 説明 |
|---|---|
| `GetProjectDataFieldNames() -> list[str]` *静的* | プロジェクトデータのフィールド名を返します。 |
| `GetProjectData(fieldName: str) -> str \| None` *静的* | `fieldName`のプロジェクトデータを返します。 |
| `SetProjectData(fieldName: str, value: str) -> bool` *静的* | プロジェクトデータを設定します。 |
| `GetAllProjectData() -> list[tuple[str, str]]` *静的* | すべてのプロジェクトデータを返します。 |

*改訂情報と版情報*

| メソッド | 説明 |
|---|---|
| `GetRevisions() -> list[TitleBlockBorderObject.Revision]` | この表題欄に表示される改訂履歴です。古い順に並びます。 |
| `GetSheetID() -> str \| None` | 表題欄が現在表示しているシートの識別情報です。 |
| `GetSheetTitle() -> str \| None` | シートレイヤタイトルを返します。 |
| `GetSheetDate() -> str \| None` | シートの日付を返します。 |
| `GetLatestIssueDate() -> str \| None` | この表題欄の最新の発行日です。一度も発行されていない場合は空です。 |
| `UpdateData(updateAutomaticData: bool = True) -> bool` *静的* | ファイルのデータを図面内のすべての図面枠に再度読み込み、再描画します。`updateAutomaticData`を指定すると、Vectorworksが自動管理する値（ファイル名、ページ番号、シート数、印刷日など）も更新します。 |

継承メンバー：[`AnnotationObject`](#annotationobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### TitleBlockBorderObject.Revision

> **完全修飾名:** `api.TitleBlockBorderObject.Revision` · **継承元:** `api.Object`

表題欄の一つの改訂です。番号、日付、注記、発行日、受信者を含みます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Revision()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Revision(fNumber, fDate, fNote, fPublishDate, fRecipients)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fNumber` | `str` | 改訂番号。 |
| `fDate` | `str` | 改訂日。 |
| `fNote` | `str` | 改訂の注記。 |
| `fPublishDate` | `str` | 発行日。 |
| `fRecipients` | `str` | 受信者。 |

### DimensionObject

> **完全修飾名:** `api.DimensionObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

すべての寸法線オブジェクトの基底クラスです（`ObjectType.Dimension`）。

寸法はVectorworksのネイティブオブジェクトであり、プラグインオブジェクトではありません。パラメータレコードやプラグインスタイルはありません。測定点、表示するテキスト、寸法補助線を描画するかどうかなど、すべての情報はオブジェクト変数に格納され、このクラスの名前付きアクセサーを通してアクセスできます。

寸法は次の三つの情報に基づいて描画されます：

1. 寸法自体の図形情報（測定点、および測定点から寸法線までのオフセット）。
2. 参照する寸法規格（GetStandardName）。矢印のスタイルとサイズ、寸法補助線の間隔と突出量、テキストの配置などです。これらはすべて用紙上の長さであり、縮尺が考慮されます。
3. 単位設定。デフォルトではファイルの主単位／補助単位を使用し、名前付き寸法単位設定が割り当てられている場合はその設定（GetUnitSetting）を使用します。

寸法の規格や単位を変更しても、測定対象は変わらず、外観のみが変わります。

寸法には測定値（GetShowValue）が表示され、その前後に任意の前記号と後記号が付きます。値の表示をオフにして前記号を設定すると、寸法は単純なラベルになります。「secondary」アクセサーは、二つ目の（二重寸法の）単位表示に対する同じ設定です。

寸法は連動させることができます。`Associate()`が成功すると、寸法はスナップ先のオブジェクトを測定し続け、そのオブジェクトが変更されると自動的に更新します。連動性はオブジェクトだけでなく、ファイルのプロパティ（「寸法を図形の大きさと連動させる」ファイル設定）でもあります。

このAPIの角度はすべてラジアン、長さはすべてワールド単位です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DimensionObject(h: Handle)` | 既存の寸法`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクト（任意の寸法線オブジェクト）を参照している場合はTrueです。 |
| `KindOf(h: Handle) -> DimensionKind` *静的* | 寸法の種類です。`h`が寸法ではない場合はUnknownです。 |
| `Duplicate() -> DimensionObject` | 図面内の寸法を複製し、そのコピーを返します。 |

*識別情報*

| メソッド | 説明 |
|---|---|
| `GetKind() -> DimensionKind \| None` | 種類を返します。 |
| `GetKindName() -> str \| None` | 種類の名前を返します。 |
| `GetKindName(kind: DimensionKind) -> str` *静的* | `kind`の種類名を返します。 |

*測定対象の図形*

| メソッド | 説明 |
|---|---|
| `GetStartPoint() -> Math.Point2D \| None` | 寸法の測定対象となる二点です。角度寸法では二辺上の点で、頂点は別に保持されます（AngularDimensionObjectを参照）。半径寸法および円弧長寸法では、円／円弧上の点です。 |
| `SetStartPoint(pt: Math.Point2D) -> bool` | 始点を設定します。寸法の測定対象となる二点です。角度寸法では二辺上の点で、頂点は別に保持されます（AngularDimensionObjectを参照）。半径寸法および円弧長寸法では、円／円弧上の点です。 |
| `GetEndPoint() -> Math.Point2D \| None` | 終点を返します。 |
| `SetEndPoint(pt: Math.Point2D) -> bool` | 終点を設定します。 |
| `SetPoints(start: Math.Point2D, end: Math.Point2D) -> bool` | 点を設定します。 |
| `GetOffset() -> float \| None` | 測定点と寸法線自体の間の距離です。正のオフセットではstart -> endの方向の左側、負のオフセットでは右側に寸法線を配置します。 |
| `SetOffset(offset: float) -> bool` | オフセットを設定します。測定点と寸法線自体の間の距離です。正のオフセットではstart -> endの方向の左側、負のオフセットでは右側に寸法線を配置します。 |
| `GetMeasuredLength() -> float \| None` | 二つの測定点の間の直線距離です。ワールド単位で返します。これは斜め寸法が表示する長さです。縦横寸法では、この距離を固定方向に投影した値を表示します。 |

*寸法補助線（延長線）*

| メソッド | 説明 |
|---|---|
| `GetStartWitness() -> bool \| None` | *最初の寸法補助線*がオンかどうか。 |
| `SetStartWitness(show: bool) -> bool` | *最初の寸法補助線*のオン／オフを切り替えます。 |
| `GetEndWitness() -> bool \| None` | *最後の寸法補助線*がオンかどうか。 |
| `SetEndWitness(show: bool) -> bool` | *最後の寸法補助線*のオン／オフを切り替えます。 |
| `GetWitnessOverride() -> int \| None` | 0 = 寸法規格を使用、1 = 両方の寸法補助線に共通のカスタム長さ、2 = 寸法補助線ごとのカスタム長さ、3 = 両方に共通のカスタムオフセット、4 = 寸法補助線ごとのカスタムオフセット。 |
| `SetWitnessOverride(mode: int) -> bool` | 寸法補助線の上書き設定を設定します。0 = 寸法規格を使用、1 = 両方の寸法補助線に共通のカスタム長さ、2 = 寸法補助線ごとのカスタム長さ、3 = 両方に共通のカスタムオフセット、4 = 寸法補助線ごとのカスタムオフセット。 |
| `GetStartWitnessLength() -> float \| None` | 最初の寸法補助線の長さを返します（ワールド単位、カスタム上書き）。 |
| `SetStartWitnessLength(length: float) -> bool` | 最初の寸法補助線の長さを設定します。 |
| `GetEndWitnessLength() -> float \| None` | 最後の寸法補助線の長さを返します。 |
| `SetEndWitnessLength(length: float) -> bool` | 最後の寸法補助線の長さを設定します。 |
| `GetStartWitnessOffset() -> float \| None` | 最初の寸法補助線のオフセットを返します（ワールド単位、カスタム上書き）。 |
| `SetStartWitnessOffset(offset: float) -> bool` | 最初の寸法補助線のオフセットを設定します。 |
| `GetEndWitnessOffset() -> float \| None` | 最後の寸法補助線のオフセットを返します。 |
| `SetEndWitnessOffset(offset: float) -> bool` | 最後の寸法補助線のオフセットを設定します。 |

*矢印と引出線*

| メソッド | 説明 |
|---|---|
| `GetArrowsInside() -> bool \| None` | 矢印の先端が外側ではなく内側（寸法補助線の間）を向いている場合は`True`です。 |
| `SetArrowsInside(inside: bool) -> bool` | *寸法線は常に内側*のオン／オフを切り替えます。矢印の先端が外側ではなく内側（寸法補助線の間）を向いている場合は`True`です。 |
| `GetLeaderLine() -> bool \| None` | テキストが寸法補助線の間に収まらない場合に、引出線でテキストと寸法線を結びます。主に半径寸法や小さな長さ寸法で使用します。 |
| `SetLeaderLine(use: bool) -> bool` | *引出線を表示*のオン／オフを切り替えます。テキストが寸法補助線の間に収まらない場合に、引出線でテキストと寸法線を結びます。主に半径寸法や小さな長さ寸法で使用します。 |

*表示テキスト*

| メソッド | 説明 |
|---|---|
| `GetShowValue() -> bool \| None` | 測定値を表示するかどうか。オフにして前記号を指定すると、単純な注釈ラベルになります。 |
| `SetShowValue(show: bool) -> bool` | *寸法値の表示*のオン／オフを切り替えます。測定値を表示するかどうか。オフにして前記号を指定すると、単純な注釈ラベルになります。 |
| `GetLeaderText() -> str \| None` | 前記号（値の前に表示）を返します。 |
| `SetLeaderText(text: str) -> bool` | 前記号を設定します。 |
| `GetTrailerText() -> str \| None` | 後記号（値の後に表示）を返します。 |
| `SetTrailerText(text: str) -> bool` | 後記号を設定します。 |
| `GetBoxText() -> bool \| None` | *ボックステキスト*がオンかどうか（テキストの周囲に枠を描画）。 |
| `SetBoxText(box: bool) -> bool` | *ボックステキスト*のオン／オフを切り替えます。 |
| `GetPrecision() -> int \| None` | 小数単位では小数点以下の桁数、分数単位では二のべき指数（0 = 1/1 ... 6 = 1/64）です。角度寸法では1 = 度のみ、2 = 度／分、3 = 度／分／秒です。 |
| `SetPrecision(precision: int) -> bool` | 精度を設定します。小数単位では小数点以下の桁数、分数単位では二のべき指数（0 = 1/1 ... 6 = 1/64）です。角度寸法では1 = 度のみ、2 = 度／分、3 = 度／分／秒です。 |
| `GetShowSecondaryValue() -> bool \| None` | 補助（二重寸法）単位の表示です。二つ目の測定値に対する同じ四つの設定です。 |
| `SetShowSecondaryValue(show: bool) -> bool` | *補助寸法値の表示*のオン／オフを切り替えます。補助（二重寸法）単位の表示です。二つ目の測定値に対する同じ四つの設定です。 |
| `GetSecondaryLeaderText() -> str \| None` | 補助寸法の前記号を返します。 |
| `SetSecondaryLeaderText(text: str) -> bool` | 補助寸法の前記号を設定します。 |
| `GetSecondaryTrailerText() -> str \| None` | 補助寸法の後記号を返します。 |
| `SetSecondaryTrailerText(text: str) -> bool` | 補助寸法の後記号を設定します。 |
| `GetSecondaryBoxText() -> bool \| None` | *補助寸法のボックステキスト*がオンかどうか。 |
| `SetSecondaryBoxText(box: bool) -> bool` | *補助寸法のボックステキスト*のオン／オフを切り替えます。 |
| `GetSecondaryPrecision() -> int \| None` | 補助寸法の精度を返します。 |
| `SetSecondaryPrecision(precision: int) -> bool` | 補助寸法の精度を設定します。 |
| `GetNoteText() -> str \| None` | 寸法が保持する注記テキストです。一部の規格では測定値の下に表示されます。 |
| `SetNoteText(text: str) -> bool` | 注記テキストを設定します。寸法が保持する注記テキストです。一部の規格では測定値の下に表示されます。 |

*テキストの配置*

| メソッド | 説明 |
|---|---|
| `GetTextPositionAutomatic() -> bool \| None` | Vectorworksがテキストを自動配置する場合は`True`、固定位置へドラッグされている場合は`False`です。 |
| `SetTextPositionAutomatic(automatic: bool) -> bool` | *文字自動位置*のオン／オフを切り替えます。Vectorworksがテキストを自動配置する場合は`True`、固定位置へドラッグされている場合は`False`です。 |
| `GetTextInside() -> bool \| None` | *テキストを内側に配置*がオンかどうか（寸法補助線の間にテキストを配置）。 |
| `SetTextInside(inside: bool) -> bool` | *テキストを内側に配置*のオン／オフを切り替えます。 |
| `GetTextFlipped() -> bool \| None` | *文字を反転*がオンかどうか。 |
| `SetTextFlipped(flipped: bool) -> bool` | *文字を反転*のオン／オフを切り替えます。 |
| `GetTextRotation() -> int \| None` | 0 = 寸法線に沿って配置、1 = 水平のみ、2 = 水平／垂直。 |
| `SetTextRotation(rotation: int) -> bool` | テキストの回転を設定します。0 = 寸法線に沿って配置、1 = 水平のみ、2 = 水平／垂直。 |
| `GetTextOffsetAlongLine() -> float \| None` | 始点（負）または終点（正）からテキストまでの距離です。ワールド単位で指定します。 |
| `SetTextOffsetAlongLine(offset: float) -> bool` | 線に沿ったテキストのオフセットを設定します。始点（負）または終点（正）からテキストまでの距離です。ワールド単位で指定します。 |
| `GetTextOffsetAboveLine() -> float \| None` | 寸法線から上方のテキストまでの距離です。ワールド単位で指定します。 |
| `SetTextOffsetAboveLine(offset: float) -> bool` | 線から上方へのテキストのオフセットを設定します。寸法線から上方のテキストまでの距離です。ワールド単位で指定します。 |

*テキストのフォント*

| メソッド | 説明 |
|---|---|
| `GetFontSize() -> float \| None` | フォントサイズを返します（ポイント）。 |
| `SetFontSize(points: float) -> bool` | フォントサイズを設定します。 |
| `GetFontStyle() -> int \| None` | 1 = ボールド、2 = イタリック、4 = アンダーラインの合計です。 |
| `SetFontStyle(style: int) -> bool` | フォントスタイルを設定します。1 = ボールド、2 = イタリック、4 = アンダーラインの合計です。 |
| `GetTextStyleName() -> str \| None` | 寸法テキストに適用する文字スタイルリソースの名前です。寸法が独自のフォント設定を使用する場合は空です。 |
| `SetTextStyleName(name: str) -> bool` | 文字スタイル名を設定します。寸法テキストに適用する文字スタイルリソースの名前です。寸法が独自のフォント設定を使用する場合は空です。 |

*公差*

| メソッド | 説明 |
|---|---|
| `GetToleranceType() -> DimensionTolerance \| None` | 公差の種類を返します。 |
| `SetToleranceType(type: DimensionTolerance) -> bool` | 公差の種類を設定します。 |
| `GetTolerancePlus() -> float \| None` | プラス側の公差を返します（ワールド単位）。 |
| `SetTolerancePlus(value: float) -> bool` | プラス側の公差を設定します。 |
| `GetToleranceMinus() -> float \| None` | マイナス側の公差を返します（ワールド単位）。 |
| `SetToleranceMinus(value: float) -> bool` | マイナス側の公差を設定します。 |

*規格と単位*

| メソッド | 説明 |
|---|---|
| `GetStandardName() -> str \| None` | オブジェクトが参照する寸法規格の名前です（"ASME"、"ISO"、カスタム規格など）。描画する寸法の用紙上の長さに関するすべての詳細は、この規格によって決まります。 |
| `SetStandardName(name: str) -> bool` | 規格名を設定します。オブジェクトが参照する寸法規格の名前です（"ASME"、"ISO"、カスタム規格など）。描画する寸法の用紙上の長さに関するすべての詳細は、この規格によって決まります。 |
| `GetStandardIndex() -> int \| None` | 規格のインデックスです。> 0は組み込み規格、< 0はカスタム（ファイル）規格です。 |
| `SetStandardIndex(index: int) -> bool` | 規格のインデックスを設定します。規格のインデックスです。> 0は組み込み規格、< 0はカスタム（ファイル）規格です。 |
| `GetUnitSetting() -> int \| None` | 0 = ファイルの単位を使用。それ以外は、名前付き寸法単位設定リソースのインデックスです。 |
| `SetUnitSetting(index: int) -> bool` | 単位設定を設定します。0 = ファイルの単位を使用。それ以外は、名前付き寸法単位設定リソースのインデックスです。 |

*連動性*

| メソッド | 説明 |
|---|---|
| `Associate(selectedObjectsOnly: bool = False) -> bool` | 寸法を測定対象のオブジェクトに関連付け、追従させます。`selectedObjectsOnly`を指定すると、関連付け先の検索を現在の選択範囲に制限します。すべての寸法が関連付け可能とは限りません。関連付けが拒否された場合は`False`を返します。 |
| `GetDimensionsOf(hObject: Handle) -> list[Handle]` *静的* | 寸法を関連付けられるオブジェクト：現在`hObject`を測定している寸法です。 |

継承メンバー：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### LinearDimensionObject

> **完全修飾名:** `api.LinearDimensionObject` · **継承元:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

長さ寸法です。二点間の距離を測定します。

二つの形式があり、二つの測定点が寸法線に揃っていない場合の動作が異なります：

縦横寸法（固定角度）- CreateConstrained / CreateHorizontal / CreateVertical 寸法線は作成時の方向を保持します。表示値は二点間の距離をその方向に投影した値です。したがって、傾斜した壁に対する水平寸法は、壁の長さではなく水平方向の距離を示します。これは縦横寸法ツールが描画するもので、通常、平面図の寸法にはこの形式を使用します。

斜め寸法（非拘束）- CreateUnconstrained 寸法線は二点を結ぶ線に平行で、表示値は常に二点間の実距離です。これは斜め寸法ツールが描画するものです。

どちらもオフセットを受け取ります。これは測定点から寸法線までの距離で、ワールド単位で指定します。正のオフセットではstart -> endの方向の左側、負のオフセットでは右側に配置します。

三つ目の形式である累進寸法は、共通の基準面に対して各点を測定し、基準面からのオフセットのみを表示します。CreateOrdinateで作成します。

長さ寸法は連動させることができます（`DimensionObject.Associate`を参照）。スナップ先のオブジェクトに関連付けると、そのオブジェクトが変更されるたびに再測定します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `LinearDimensionObject(h: Handle)` | 既存の長さ寸法`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*すべての長さ寸法*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | 縦横寸法、斜め寸法、または累進寸法。 |
| `CreateConstrained(start: Math.Point2D, end: Math.Point2D, direction: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *静的* | 明示的に指定した方向に沿った縦横寸法です。`direction`は寸法線の方向です。ゼロベクトルの場合は`start`から`end`への方向を使用します。二点が一致する場合は失敗します。 |
| `CreateConstrained(start: Math.Point2D, end: Math.Point2D, angle: float, offset: float = 0.0) -> LinearDimensionObject` *静的* | 寸法線をX軸から`angle`ラジアン回転した縦横寸法です。 |
| `CreateHorizontal(start: Math.Point2D, end: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *静的* | 二点間の水平／垂直距離を測定する縦横寸法です。 |
| `CreateVertical(start: Math.Point2D, end: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *静的* | `start`と`end`の間の垂直距離を測定する縦横寸法を作成し、`offset`の位置に配置します。 |
| `CreateUnconstrained(start: Math.Point2D, end: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *静的* | 斜め寸法（非拘束）です。寸法線はstart -> endに沿い、値は二点間の実距離です。二点が一致する場合は失敗します。 |

*累進寸法*

| メソッド | 説明 |
|---|---|
| `CreateOrdinate(datum: Math.Point2D, point: Math.Point2D, direction: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *静的* | `start`は基準面、`end`は測定点です。 |
| `Duplicate() -> LinearDimensionObject` | 図面内の長さ寸法を複製し、そのコピーを返します。 |
| `IsConstrained() -> bool \| None` | 縦横寸法（固定角度）の場合は`True`、斜め寸法の場合は`False`です。 |
| `GetDirectionAngle() -> float \| None` | 寸法線の方向を、X軸からの角度としてラジアンで示します。斜め寸法の場合は、始点から終点への方向です。 |
| `SetDirectionAngle(angle: float) -> bool` | 縦横寸法でのみ意味があります。測定点を移動せずに寸法線を回転させ、寸法の表示値を変更します。 |
| `GetValue() -> float \| None` | 寸法の表示値です。測定点間の距離で、縦横寸法の場合は寸法線の方向に投影した値になります。 |

継承メンバー：[`DimensionObject`](#dimensionobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### AngularDimensionObject

> **完全修飾名:** `api.AngularDimensionObject` · **継承元:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

角度寸法です。頂点で交わる二辺の間の角度を測定します。

寸法は、二辺が交わる頂点と各辺上の点という三点、および辺の間に描画する寸法の円弧の半径を決めるオフセットで定義されます。表示値は第一の辺から第二の辺まで反時計回りに測った角度なので、二辺上の点を入れ替えると、元の角度を360度から引いた角度になります。

角度寸法は基準角度にすることもできます。この場合、寸法補助線は一本だけ描画され、二辺間の角度ではなく、基準方向に対する一辺の角度を測定します。Vectorworksはデフォルトで基準角度寸法を作成するため、`Create()`ではこの設定をオフにし、`CreateReferenceAngle()`ではオンのままにします。

このクラスの角度アクセサーは、APIのほかの部分と同様にラジアンを使用します。一方、角度の精度は寸法の規約に従い、1 = 度のみ、2 = 度＋分、3 = 度＋分＋秒、5..12 = その数の小数桁数です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `AngularDimensionObject(h: Handle)` | 既存の角度寸法`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(vertex: Math.Point2D, firstLegPoint: Math.Point2D, secondLegPoint: Math.Point2D, offset: float = 0.0) -> AngularDimensionObject` *静的* | `firstLegPoint`から`secondLegPoint`までの、`vertex`を中心とした角度で、頂点から`offset`ワールド単位離れた位置に描画します。三点のうち任意の二点が一致する場合は失敗します。 |
| `Create(vertex: Math.Point2D, startAngle: float, endAngle: float, legLength: float, offset: float = 0.0) -> AngularDimensionObject` *静的* | 同じ寸法ですが、頂点、二辺の方向（ラジアン）、辺の長さから作成します。 |

*基準角度形式*

| メソッド | 説明 |
|---|---|
| `CreateReferenceAngle(vertex: Math.Point2D, firstLegPoint: Math.Point2D, secondLegPoint: Math.Point2D, offset: float = 0.0) -> AngularDimensionObject` *静的* | 一本の寸法補助線を使用し、基準方向に対する一辺の角度を測定します。 |
| `Duplicate() -> AngularDimensionObject` | 図面内の角度寸法を複製し、そのコピーを返します。 |
| `GetVertex() -> Math.Point2D \| None` | 二辺が交わる頂点です。Vectorworksはこの頂点を、二辺上の点を保持する始点／終点ではなく、寸法ボックスに保持します。 |
| `SetVertex(vertex: Math.Point2D) -> bool` | 頂点を設定します。二辺が交わる頂点です。Vectorworksはこの頂点を、二辺上の点を保持する始点／終点ではなく、寸法ボックスに保持します。 |
| `GetStartAngle() -> float \| None` | 二辺の方向です。X軸からの角度をラジアンで示します。 |
| `GetEndAngle() -> float \| None` | 終了角度を返します。 |
| `GetValue() -> float \| None` | 第一の辺から第二の辺まで反時計回りに測った角度をラジアンで示します。範囲は[0, 2*pi)です。 |
| `GetReferenceAngle() -> bool \| None` | 一本の寸法補助線で、基準方向に対する角度を測定するかどうか。 |
| `SetReferenceAngle(reference: bool) -> bool` | *基準角度*のオン／オフを切り替えます。一本の寸法補助線で、基準方向に対する角度を測定するかどうか。 |

継承メンバー：[`DimensionObject`](#dimensionobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### ArcLengthDimensionObject

> **完全修飾名:** `api.ArcLengthDimensionObject` · **継承元:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

円弧長寸法です。長さ寸法が示す両端間の直線距離ではなく、円弧に沿った長さを測定します。

測定範囲の両端点と、その両端点が位置する円弧の中心によって定義されます。中心は、二点がどのように接続されるかを寸法に示します。円上の任意の二点間には二つの円弧が存在するため、`clockwise`で測定する方を選択します。

描画方法は三つの切り替え設定で決まります。Vectorworksは三つとも作成時に固定します（その後は読み取り専用です。変更するには寸法を再作成してください）：

- clockwise — 両端点間の二つの円弧のうち、測定する方
- witnessPerpChord — 中心から放射状にではなく、弦に垂直な寸法補助線
- arcIndicator — 値が円弧長であることを示す円弧インジケータを描画

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ArcLengthDimensionObject(h: Handle)` | 既存の円弧長寸法`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(start: Math.Point2D, end: Math.Point2D, center: Math.Point2D, offset: float = 0.0, clockwise: bool = False, witnessPerpendicularToChord: bool = False, arcIndicator: bool = True) -> ArcLengthDimensionObject` *静的* | `start`から`end`まで、`center`を中心とする円弧に沿って測定します。点同士が一致する場合や、点が中心と一致する場合は失敗します。 |
| `Create(center: Math.Point2D, radius: float, startAngle: float, sweepAngle: float, offset: float = 0.0, witnessPerpendicularToChord: bool = False, arcIndicator: bool = True) -> ArcLengthDimensionObject` *静的* | 同じ寸法を円弧として表します。中心、半径、ラジアン単位の開始角度／円弧角度を指定します。円弧角度が負の場合は時計回りの円弧を測定します。 |
| `Duplicate() -> ArcLengthDimensionObject` | 図面内の円弧長寸法を複製し、そのコピーを返します。 |
| `GetCenter() -> Math.Point2D \| None` | 測定する円弧の中心です。Vectorworksはこれを寸法ボックスに保持し、始点／終点には測定範囲の両端点を保持します。 |
| `GetRadius() -> float \| None` | 半径を返します。 |
| `GetStartAngle() -> float \| None` | 測定する円弧の開始角度と符号付き円弧角度です。ラジアンで示します。 |
| `GetSweepAngle() -> float \| None` | 円弧角度を返します。 |
| `GetValue() -> float \| None` | 寸法の表示値です。円弧に沿った長さをワールド単位で示します。 |
| `IsClockwise() -> bool \| None` | 作成時に固定される描画オプションです（オブジェクトでは読み取り専用）。 |
| `IsWitnessPerpendicularToChord() -> bool \| None` | 寸法補助線が弦に垂直な場合はTrueです。 |
| `HasArcIndicator() -> bool \| None` | 寸法に円弧インジケータを表示する場合はTrueです。 |

継承メンバー：[`DimensionObject`](#dimensionobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### RadialDimensionObject

> **完全修飾名:** `api.RadialDimensionObject` · **継承元:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

半径寸法および直径寸法です。円または円弧の半径または直径を測定します。

どちらの種類も、円の中心と円周上の点から作成し、その点によって寸法の描画方向が決まります。異なるのは、測定して表示する対象だけです：

- 半径寸法 — 中心から（または引出線を使用して外側から）円周まで描画し、通常は先頭に"R"を付けて半径を表示します。直径寸法は円を横断して描画し、通常は先頭に直径記号を付けて直径を表示します。

この前記号を変更するにはSetLeaderTextを使用します。前記号は寸法の種類から自動的に決まるものではありません。

オフセットはテキスト（および引出線）を円から離す方向に移動します。半径寸法では、正のオフセットで測定値を円の外側に移動します。

「寸法線をコンパクト表示」（Get/SetCompact）は、短縮した半径表記です。中心まで達する線の代わりに、矢印の先端が付いた短い線だけを円周に描画します。円が小さく、寸法が収まらない場合に使用します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RadialDimensionObject(h: Handle)` | 既存の半径寸法`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | 任意の半径寸法または直径寸法。 |
| `CreateRadial(center: Math.Point2D, radius: float, angle: float, offset: float = 0.0) -> RadialDimensionObject` *静的* | `centre`/`radius`で表される円の半径寸法です。`angle`ラジアンの方向に描画します。 |
| `CreateRadial(center: Math.Point2D, pointOnCircle: Math.Point2D, offset: float = 0.0) -> RadialDimensionObject` *静的* | `pointOnCircle`を通り、`center`を中心とする円の半径寸法です。 |
| `CreateDiametrical(center: Math.Point2D, radius: float, angle: float, offset: float = 0.0) -> RadialDimensionObject` *静的* | 直径寸法です。引数は同じです。 |
| `CreateDiametrical(center: Math.Point2D, pointOnCircle: Math.Point2D, offset: float = 0.0) -> RadialDimensionObject` *静的* | 直径寸法です。引数は同じです。 |
| `Duplicate() -> RadialDimensionObject` | 図面内の半径寸法を複製し、そのコピーを返します。 |
| `IsDiametrical() -> bool \| None` | 寸法が直径を表示する場合は`True`、半径を表示する場合は`False`です。 |
| `GetCenter() -> Math.Point2D \| None` | 寸法が測定する円です。中心が始点、円周上の点が終点です。 |
| `SetCenter(center: Math.Point2D) -> bool` | 中心を設定します。寸法が測定する円です。中心が始点、円周上の点が終点です。 |
| `GetRadius() -> float \| None` | 半径を返します。 |
| `SetRadius(radius: float) -> bool` | 半径を設定します（中心と方向は保持）。 |
| `GetDiameter() -> float \| None` | 直径を返します。 |
| `SetDiameter(diameter: float) -> bool` | 直径を設定します。 |
| `GetAngle() -> float \| None` | 寸法の描画方向です。X軸からの角度をラジアンで示します。 |
| `SetAngle(angle: float) -> bool` | 角度を設定します。寸法の描画方向です。X軸からの角度をラジアンで示します。中心と半径は保持されます。 |
| `GetValue() -> float \| None` | 寸法の表示値です。直径寸法では直径、それ以外では半径です。 |
| `GetCompact() -> bool \| None` | 短縮した半径表記です。中心までの線の代わりに、矢印の先端が付いた短い線を使用します。 |
| `SetCompact(compact: bool) -> bool` | *寸法線をコンパクト表示*のオン／オフを切り替えます。短縮した半径表記です。中心までの線の代わりに、矢印の先端が付いた短い線を使用します。 |

継承メンバー：[`DimensionObject`](#dimensionobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### CenterMarkObject

> **完全修飾名:** `api.CenterMarkObject` · **継承元:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

センターマークです。円または円弧の中心を示す十字です。

このグループのほかのすべてのオブジェクトとは異なり、センターマークは寸法線オブジェクトではありません。Vectorworksはセンターマークツールと同じように、単純な線分のグループとして作成します：

- 中心で小さな十字を形成する水平および垂直の線分。それぞれの長さはスポーク一つ分です。
- 任意で、円周まで（およびその少し先まで）伸びる四つの延長線分。十字との間には間隔を設けます。十字と間隔の両方が収まる大きさの円の場合にのみ追加します。これはツールが適用する規則と同じです。

通常の図形なので、測定値は保持せず、再生成するものもありません。移動や拡大縮小を行うと、線が移動または拡大縮小するだけです。

形状を決める用紙上の三つの長さ（スポークの長さ、間隔、延長線の突出量）はアクティブな寸法規格から取得するため、1:50のレイヤに描いたセンターマークも1:100のレイヤに描いたものと用紙上では同じサイズになります。`Create()`はこれらを規格から読み取ります。`CreateWithSizes()`では、代わりに明示的なワールド長さを指定し、完全に制御できます。

ツールと同様に、「寸法を指定クラスに作成する」ファイル設定がオンの場合は寸法クラスに、そうでない場合はアクティブなクラスにグループを配置します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `CenterMarkObject(h: Handle)` | 既存のセンターマーク`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | ネイティブのセンターマークは識別用の印のないグループなので、`Is()`は慎重を期して`False`を返します。`Create()`が返したオブジェクトを保持するか、センターマークと分かっているグループのハンドルから構築してください。 |
| `Create(center: Math.Point2D, radius: float = 0.0) -> CenterMarkObject` *静的* | `center`/`radius`で表される円のセンターマークです。アクティブな寸法規格に基づいてサイズを設定します。半径がゼロまたは負の場合は、延長線分のない十字のみを描画します。 |
| `CreateFor(hObject: Handle) -> CenterMarkObject` *静的* | 既存の円、円弧、長円、その他のオブジェクトのセンターマークです。オブジェクトの境界ボックスの中心に配置し、そのボックスに合わせてサイズを設定します。 |
| `CreateWithSizes(center: Math.Point2D, radius: float, spokeLength: float, gap: float, extension: float) -> CenterMarkObject` *静的* | ワールド長さを明示的に指定するセンターマークです。`spokeLength`は十字のスポーク一つの長さ、`gap`は十字と延長線分の間隔、`extension`は延長線分が円周から突出する距離です。円が小さすぎる場合、延長線は省略します。 |
| `Duplicate() -> CenterMarkObject` | 図面内のセンターマークを複製し、そのコピーを返します。 |
| `GetCenter() -> Math.Point2D \| None` | 十字の中心。 |
| `GetSegmentCount() -> int \| None` | マークを構成する線分の数です。十字のみの場合は2、延長線がある場合は最大6です。 |

継承メンバー：[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### WorksheetObject

> **完全修飾名:** `api.WorksheetObject` · **継承元:** [`TypedResource`](Resources.md#typedresource) → [`Resource`](Resources.md#resource) → `api.Object`

所有権を持たないワークシートリソースです。配置されたワークシートイメージや注釈のプラグインオブジェクトではありません。行、列、データベースのサブ行のすべてのインデックスは、0から始まる図形APIとは異なり、ワークシート固有の1から始まる方式です（列1 = A）。範囲は両端を含みます。文字列はUTF-8です。Vectorworksは符号付き16ビットのインデックス／サイズを使用し、Pythonはその表現範囲外の値を拒否します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `WorksheetObject(h: Handle)` | 既存のワークシート`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `FromName(name: str) -> WorksheetObject` *静的* | `name`という名前のワークシートリソースです。存在しない場合は無効なオブジェクトです。 |

*作成のみ*

| メソッド | 説明 |
|---|---|
| `Create(name: str, rows: int = 20, columns: int = 10) -> WorksheetObject` *静的* | 名前が使用済みの場合は、別のワークシートであっても失敗します。検索にはFromNameを使用してください。 |
| `Duplicate() -> WorksheetObject` | 図面内のワークシートを複製し、そのコピーを返します。 |
| `GetRowCount() -> int \| None` | 行項目の数。 |
| `GetColumnCount() -> int \| None` | 列項目の数。 |
| `IsValidCell(row: int, column: int) -> bool` | `row` / `column`のセルがワークシートに存在する場合はTrueです。 |
| `IsValidRange(range: WorksheetObject.Range) -> bool` | `range`のすべてのセルがワークシートに存在する場合はTrueです。 |
| `InsertRows(beforeRow: int, count: int = 1) -> bool` | `count`行を`beforeRow`行の前に挿入します。 |
| `InsertColumns(beforeColumn: int, count: int = 1) -> bool` | `count`列を`beforeColumn`列の前に挿入します。 |
| `DeleteRows(startRow: int, count: int = 1) -> bool` | `count`行を`startRow`行から削除します。 |
| `DeleteColumns(startColumn: int, count: int = 1) -> bool` | `count`列を`startColumn`列から削除します。 |
| `GetCellFormula(row: int, column: int) -> str \| None` | リテラルを含む定義文字列です。そのままVectorworksに渡されます。Vectorworksが数式を正規化することがあります。 |
| `SetCellFormula(row: int, column: int, formula: str) -> bool` | セルの数式を設定します。リテラルを含む定義文字列です。そのままVectorworksに渡されます。Vectorworksが数式を正規化することがあります。 |
| `SetRangeFormula(range: WorksheetObject.Range, formula: str) -> bool` | 範囲の数式を設定します。 |
| `GetCellText(row: int, column: int) -> str \| None` | `row`、`column`のセルテキストを返します。 |
| `GetCellValue(row: int, column: int) -> float \| None` | 数値ではないセルやエラーのセルでは、誤解を招くゼロではなく空を返します。値は最後の再計算結果を反映します。 |
| `ClearCells(range: WorksheetObject.Range) -> bool` | `range`内のセルの内容を消去します。 |
| `IsDatabaseRow(row: int) -> bool \| None` | `row`がデータベース行の場合はTrueです。 |
| `GetDatabaseCriteria(row: int) -> str \| None` | `row`のデータベース検索条件を返します。 |
| `SetDatabaseCriteria(row: int, criteria: str) -> bool` | 内部形式を解釈しないネイティブの定義です。例："=DATABASE(ALL)"。空を指定するとスプレッドシート行に変換します。ここでは検索条件を解析しません。Vectorworksが適用できない場合（統合された行など）は`False`です。 |
| `GetSubrowCount(row: int) -> int \| None` | `row`のサブ行項目の数。 |
| `GetSubrowCellText(row: int, column: int, subrow: int) -> str \| None` | `row`、`column`、`subrow`のサブ行セルテキストを返します。 |
| `GetSubrowCellValue(row: int, column: int, subrow: int) -> float \| None` | `row`、`column`、`subrow`のサブ行セル値を返します。 |
| `GetColumnWidth(column: int) -> int \| None` | 幅／高さはワークシート固有のピクセル単位であり、モデル／ワールド単位ではありません。 |
| `SetColumnWidth(firstColumn: int, lastColumn: int, width: int) -> bool` | 列幅を設定します。幅／高さはワークシート固有のピクセル単位であり、モデル／ワールド単位ではありません。 |
| `GetRowHeight(row: int) -> int \| None` | `row`の行の高さを返します。 |
| `GetRowHeightLocked(row: int) -> bool \| None` | `row`の*行の高さを固定*がオンかどうか。 |
| `SetRowHeight(firstRow: int, lastRow: int, height: int, lockHeight: bool = True, includeSubrows: bool = False) -> bool` | 行の高さを設定します。 |
| `AutoFitRowHeights(firstRow: int, lastRow: int) -> bool` | `firstRow` .. `lastRow`の行の高さを内容に合わせます。 |
| `GetSubrowHeight(row: int, subrow: int) -> int \| None` | `row`、`subrow`のサブ行の高さを返します。 |
| `GetCellNumberFormat(row: int, column: int) -> WorksheetObject.NumberFormat \| None` | `row`、`column`のセルの数字の表示形式を返します。 |
| `SetNumberFormat(range: WorksheetObject.Range, format: WorksheetObject.NumberFormat) -> bool` | 数字の表示形式を設定します。 |
| `GetCellTextFormat(row: int, column: int) -> WorksheetObject.TextFormat \| None` | `row`、`column`のセルのテキスト書式を返します。 |
| `SetTextFormat(range: WorksheetObject.Range, format: WorksheetObject.TextFormat) -> bool` | テキスト書式を設定します。 |
| `GetCellFill(row: int, column: int) -> WorksheetObject.Fill \| None` | `row`、`column`のセルの面設定を返します。 |
| `SetFill(range: WorksheetObject.Range, fill: WorksheetObject.Fill) -> bool` | 面設定を設定します。 |
| `GetCellBorders(row: int, column: int) -> WorksheetObject.Borders \| None` | `row`、`column`のセルの枠線を返します。 |
| `SetBorders(range: WorksheetObject.Range, borders: WorksheetObject.Borders) -> bool` | 枠線を設定します。 |
| `GetMergedCellRange(row: int, column: int) -> WorksheetObject.Range \| None` | `row`、`column`の統合セルの範囲を返します。 |
| `MergeCells(range: WorksheetObject.Range) -> bool` | `range`内のセルを一つのセルに統合します。 |
| `UnmergeCells(range: WorksheetObject.Range) -> bool` | `range`内の統合セルを分割します。 |
| `Recalculate() -> bool` | ワークシートを再計算します。 |
| `GetAutoRecalculate() -> bool \| None` | *自動再計算*がオンかどうか。 |
| `SetAutoRecalculate(enabled: bool) -> bool` | *自動再計算*のオン／オフを切り替えます。 |
| `CreateImage(topLeftCorner: Point2D) -> Handle` | ワークシートイメージのハンドルは図面オブジェクトです。WorksheetObjectとして使用しないでください。最初の既存ワークシートイメージを再配置するか、存在しない場合はアクティブレイヤに作成します。「必ず別のワークシートイメージを作成する」ファクトリーではありません。 |
| `GetImage() -> Handle` | ワークシートイメージを返します。最初に関連付けられたワークシートイメージで、存在しない場合はnullです。 |
| `FromImage(image: Handle) -> WorksheetObject` *静的* | ワークシートイメージ`image`（図面に配置されたオブジェクト）が表示しているワークシートリソースです。 |

継承メンバー：[`TypedResource`](Resources.md#typedresource)、[`Resource`](Resources.md#resource)のすべて。

#### WorksheetObject.Range

> **完全修飾名:** `api.WorksheetObject.Range` · **継承元:** `api.Object`

両端を含む、1から始まるワークシートの範囲です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Range()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Range(firstRow, firstColumn, lastRow, lastColumn)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `firstRow` | `int` | 最初の行（1から始まる）。 |
| `firstColumn` | `int` | 最初の列（1から始まる）。 |
| `lastRow` | `int` | 最後の行（範囲に含む）。 |
| `lastColumn` | `int` | 最後の列（範囲に含む）。 |

#### WorksheetObject.NumberFormat

> **完全修飾名:** `api.WorksheetObject.NumberFormat` · **継承元:** `api.Object`

ワークシート固有の数字の表示形式です。書式に応じた精度とUTF-8の前記号／後記号を含みます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `NumberFormat()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `NumberFormat(style, accuracy, leader, trailer)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `style` | `int` | 0 標準、1 小数点、2 コンマ区切りの小数、3 指数、4 分数、5 寸法、6 角度、7 日付、8 条件付き、9 一般分数、10 区切り付き寸法、11 面積、12 体積、13 文字、14 パーセンテージ。 |
| `accuracy` | `int` | 書式に依存するネイティブの精度です。常に小数桁数を表すわけではありません。 |
| `leader` | `str` | 0 標準、1 小数点、2 コンマ区切りの小数、3 指数、4 分数、5 寸法、6 角度、7 日付、8 条件付き、9 一般分数、10 区切り付き寸法、11 面積、12 体積、13 文字、14 パーセンテージ。 |
| `trailer` | `str` | 0 標準、1 小数点、2 コンマ区切りの小数、3 指数、4 分数、5 寸法、6 角度、7 日付、8 条件付き、9 一般分数、10 区切り付き寸法、11 面積、12 体積、13 文字、14 パーセンテージ。 |

#### WorksheetObject.TextFormat

> **完全修飾名:** `api.WorksheetObject.TextFormat` · **継承元:** `api.Object`

ワークシートのテキストです。ポイントサイズ、フォント／スタイル、配置、度単位の角度、ColorRefインデックス、折り返しを含みます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `TextFormat()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `TextFormat(fontIndex, size, style, alignment, verticalAlignment, angle, color, wrap)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fontIndex` | `int` | ファイルのフォントテーブルのインデックス。 |
| `size` | `int` | ポイント。 |
| `style` | `int` | ネイティブの文字スタイルビット（ボールド=1、イタリック=2、アンダーライン=4など）。 |
| `alignment` | `int` | 0 標準、1 左、2 中央、3 右。 |
| `verticalAlignment` | `int` | 0 標準、1 上、3 中央、5 下。 |
| `angle` | `int` | ワークシート固有のテキスト角度です。ラジアンではなく度単位です。 |
| `color` | `int` | ファイルのColorRefインデックスです。RGBではありません。 |
| `wrap` | `bool` | セル内でテキストを折り返すかどうか。 |

#### WorksheetObject.Fill

> **完全修飾名:** `api.WorksheetObject.Fill` · **継承元:** `api.Object`

ネイティブの面のスタイル、ファイルのColorRefインデックス、模様です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Fill()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Fill(style, background, foreground, pattern)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `style` | `int` | 0 なし、1 カラー、2 模様。 |
| `background` | `int` | 背景色（カラーインデックス）。 |
| `foreground` | `int` | ファイルのColorRefインデックス。 |
| `pattern` | `int` | ネイティブの面模様です。スタイル2の場合にのみ使用します。 |

#### WorksheetObject.Borders

> **完全修飾名:** `api.WorksheetObject.Borders` · **継承元:** `api.Object`

セルの枠線フラグと、範囲の外枠および内側への適用フラグです。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Borders()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Borders(top, left, bottom, right, outline, insideHorizontal, insideVertical)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `top` | `bool` | 上の枠線。 |
| `left` | `bool` | 左の枠線。 |
| `bottom` | `bool` | 下の枠線。 |
| `right` | `bool` | 右の枠線。 |
| `outline` | `bool` | 範囲への適用オプションです。単一セルのゲッターでは、これらは`False`のままです。 |
| `insideHorizontal` | `bool` | 範囲への適用オプションです。単一セルのゲッターでは、これらは`False`のままです。 |
| `insideVertical` | `bool` | 範囲への適用オプションです。単一セルのゲッターでは、これらは`False`のままです。 |

<a id="enumerations"></a>

## 列挙型

### DimensionKind

> **完全修飾名:** `api.DimensionKind` · **種類:** `IntEnum`

オブジェクトの寸法の種類です。オブジェクトに格納され、寸法の測定方法と描画方法を決定します。作成後は変更できません（代わりに適切な種類で作成してください）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Unknown` | `-1` |  |
| `ConstrainedLinear` | `0` | 長さ寸法、固定方向：寸法線は作成時に指定した方向（水平、垂直、または任意の回転角度）を保持し、二点をその方向に投影して測定します。fix_ang。 |
| `UnconstrainedLinear` | `1` | 長さ寸法、自由方向：寸法線は二つの測定点を結ぶ線に沿うため、常に二点間の実距離を示します。sloped。 |
| `Ordinate` | `2` | 共通の基準面から測定する長さ寸法です。その基準面からのオフセットのみを表示します。 |
| `Radial` | `3` | 円／円弧の半径。 |
| `Diametrical` | `4` | 円／円弧の直径。 |
| `Angular` | `5` | 頂点を中心とする二辺間の角度。 |
| `ArcLength` | `6` | 円弧に沿った長さ。 |

### DimensionTolerance

> **完全修飾名:** `api.DimensionTolerance` · **種類:** `IntEnum`

寸法の公称値からのずれの量です。測定値の隣に表示されます。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` |  |
| `Single` | `1` | 単一の+/-値。 |
| `Double` | `2` | 個別のプラス値とマイナス値。 |
| `Limit` | `3` | 公称値の代わりに上限と下限を表示。 |

---

[一覧に戻る](README.md) · [先頭に戻る](#objectsannotation--dimensions-data-tags-title-block-borders-and-worksheets)
