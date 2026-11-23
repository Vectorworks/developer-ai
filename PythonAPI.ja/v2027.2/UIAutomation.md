[English](../../PythonAPI/v2027.2/UIAutomation.md) • [Deutsch](../../PythonAPI.de/v2027.2/UIAutomation.md) • **日本語**

<a id="uiautomation--tools-the-tool-bar-menus-and-the-object-info-palette"></a>

# UIAutomation — ツール、ツールバー、メニュー、オブジェクト情報パレット

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

ユーザーインターフェイスを自動操作するクラス群。`ToolAccess`はツールの一覧（ツールのアクティブ化）を提供し、`ModeBar`はアクティブなツールのモードを読み取り、変更し、`ToolControl`はクリック、ドラッグ、マウス移動、キー入力でアクティブなツールを操作します。`MenuAccess`はメニューコマンドとチャンクメニュー項目を一覧表示し、実行します。`OIPAccess`は、選択内容に対してオブジェクト情報パレットが表示するコントロールを一覧表示し、読み取り、操作します。

規約：ゲッターは値を取得できない場合に`None`を返し、セッター／アクションは成功時に`True`を返します。名前の比較では大文字小文字を区別しません。モードインデックスとチャンクメニュー項目インデックスを含め、すべてのインデックスは0始まりです。ユーザーインターフェイスの操作はユーザー入力とまったく同じように動作します。ツールがツールバー（モードバー）を再構築することがあり、コマンドは独自のダイアログを表示して取り消しを設定し、オブジェクト情報パレットへの変更はパレットを再構築します。値をキャッシュせず、変更後に再度読み取ってください。また、`Document.StartUndoEvent`で開始した取り消しイベント内でメニューコマンドを実行しないでください。

組み込みのツールとコマンドは、負の数をユニバーサル名として使用します（例："-207"）。これらについては英語名も使用できます。モデル座標はワールド単位です。ビュー座標はビューウインドウの左上隅からのピクセル数です（yは下向きに増加）。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [Point3D](#point3d)
  - [ViewPoint](#viewpoint)
  - [ViewSize](#viewsize)
  - [ToolPoint](#toolpoint)
  - [ModeButtonDefinition](#modebuttondefinition)
  - [Tool](#tool)
  - [ModeChoice](#modechoice)
  - [ToolMode](#toolmode)
  - [ModeSetting](#modesetting)
  - [ModeBar](#modebar)
  - [ToolControl](#toolcontrol)
  - [ToolAccess](#toolaccess)
  - [MenuCommand](#menucommand)
  - [MenuChunkItem](#menuchunkitem)
  - [MenuEntry](#menuentry)
  - [MenuAccess](#menuaccess)
  - [OIPControl](#oipcontrol)
  - [OIPSetting](#oipsetting)
  - [OIPAccess](#oipaccess)
- [列挙型](#enumerations)
  - [ToolKind](#toolkind)
  - [ToolCreationType](#toolcreationtype)
  - [ToolFilter](#toolfilter)
  - [ModeType](#modetype)
  - [ModeButtonKind](#modebuttonkind)
  - [ToolKey](#toolkey)
  - [MenuCommandKind](#menucommandkind)
  - [MenuChunkKind](#menuchunkkind)
  - [MenuFilter](#menufilter)
  - [MenuEntryType](#menuentrytype)
  - [MenuStatus](#menustatus)
  - [OIPPane](#oippane)
  - [OIPControlType](#oipcontroltype)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`Point3D`](#point3d) | クラス |  | ワールド座標の3D点。 |
| [`ViewPoint`](#viewpoint) | クラス |  | ピクセル単位のビュー座標の点（16ビット座標）。 |
| [`ViewSize`](#viewsize) | クラス |  | アクティブビューウインドウのピクセル単位のサイズ。 |
| [`ToolPoint`](#toolpoint) | クラス |  | アクティブなツールに入力された一つの点。ツールが受け取る形式。 |
| [`ModeButtonDefinition`](#modebuttondefinition) | クラス |  | ツールが宣言するツールバーボタン（モードボタン。静的な情報で、ツールをアクティブにせずに取得可能）。 |
| [`Tool`](#tool) | クラス |  | 一つのツールの説明。 |
| [`ModeChoice`](#modechoice) | クラス |  | ツールバーボタンのグループ（モードグループ）の一つの選択肢。ラジオボタン、Button/Toggleグループの単一ボタン、またはPullDown / ComboBox / SearchablePullDownグループの項目です。 |
| [`ToolMode`](#toolmode) | クラス |  | アクティブなツールの、一つのツールバーボタンのグループの現在の状態。 |
| [`ModeSetting`](#modesetting) | クラス |  | 汎用のテキストベースのモードAPIが使用するモード変更要求（`ModeBar.SetMode`を参照）。 |
| [`ModeBar`](#modebar) | クラス |  | アクティブなツールのツールバー（モードバー）に対する、状態を保持しないビュー。 |
| [`ToolControl`](#toolcontrol) | クラス |  | アクティブなツールを操作する、状態を保持しないドライバー。 |
| [`ToolAccess`](#toolaccess) | クラス |  | Vectorworksのツールシステムに対する、状態を保持しないファサード。 |
| [`MenuCommand`](#menucommand) | クラス |  | インストールされている一つのメニューコマンドの説明。 |
| [`MenuChunkItem`](#menuchunkitem) | クラス |  | チャンクメニューの現在の一つの項目。 |
| [`MenuEntry`](#menuentry) | クラス |  | 現在の作業画面で定義された、メニューバーのメニュー内の一つのエントリ。 |
| [`MenuAccess`](#menuaccess) | クラス |  | Vectorworksのメニューシステムに対する、状態を保持しないファサード。 |
| [`OIPControl`](#oipcontrol) | クラス |  | オブジェクト情報パレット（OIP）の一つのコントロールの説明と現在の状態。 |
| [`OIPSetting`](#oipsetting) | クラス |  | 汎用のテキストベースのAPIが使用するコントロール変更要求（`OIPAccess.SetValue`を参照）。 |
| [`OIPAccess`](#oipaccess) | クラス |  | オブジェクト情報パレットに対する、状態を保持しないファサード。 |
| [`ToolKind`](#toolkind) | IntEnum |  | ツールの提供形態。 |
| [`ToolCreationType`](#toolcreationtype) | IntEnum |  | オブジェクト作成にツールが使用する操作の種類。 |
| [`ToolFilter`](#toolfilter) | IntEnum |  | `ToolAccess.GetTools`が返すツールの範囲。 |
| [`ModeType`](#modetype) | IntEnum |  | アクティブなツールのツールバーボタンのグループの種類。 |
| [`ModeButtonKind`](#modebuttonkind) | IntEnum |  | ツールの登録時に宣言されたツールバーボタンの種類（現在のModeTypeとは異なる場合があります）。 |
| [`ToolKey`](#toolkey) | IntEnum |  | 点の入力中にツールが反応するキー（`ToolControl.PressKey`を参照）。 |
| [`MenuCommandKind`](#menucommandkind) | IntEnum |  | メニューコマンドの提供形態。 |
| [`MenuChunkKind`](#menuchunkkind) | IntEnum |  | チャンクメニューの種類（上記の「チャンクメニュー」を参照）。 |
| [`MenuFilter`](#menufilter) | IntEnum |  | `MenuAccess.GetMenuCommands`が返すメニューコマンドの範囲。 |
| [`MenuEntryType`](#menuentrytype) | IntEnum |  | メニューバーのメニュー内のエントリの種類。 |
| [`MenuStatus`](#menustatus) | IntEnum |  | メニューコマンド（またはチャンクメニュー項目）を現在実行できるかどうか、および実行できない理由（`MenuAccess.GetMenuStatus`を参照）。 |
| [`OIPPane`](#oippane) | IntEnum |  | オブジェクト情報パレットのタブ（ペイン）。 |
| [`OIPControlType`](#oipcontroltype) | IntEnum |  | オブジェクト情報パレット（OIP）のコントロールの種類。 |

<a id="classes"></a>

## クラス

### Point3D

> **完全修飾名:** `api.Point3D` · **継承元:** `api.Object`

ワールド座標の3D点。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Point3D()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Point3D(x, y, z)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: Point3D) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: Point3D) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `x` | `float` | X座標（ワールド単位）。 |
| `y` | `float` | Y座標（ワールド単位）。 |
| `z` | `float` | Z座標（ワールド単位）。 |

### ViewPoint

> **完全修飾名:** `api.ViewPoint` · **継承元:** `api.Object`

ピクセル単位のビュー座標の点（16ビット座標）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ViewPoint()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ViewPoint(x, y)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: ViewPoint) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: ViewPoint) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `x` | `int` | アクティブビューウインドウの左端からの水平方向のピクセル位置。 |
| `y` | `int` | アクティブビューウインドウの上端からの垂直方向のピクセル位置（下向きに増加）。 |

### ViewSize

> **完全修飾名:** `api.ViewSize` · **継承元:** `api.Object`

アクティブビューウインドウのピクセル単位のサイズ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ViewSize()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ViewSize(fWidth, fHeight)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fWidth` | `int` | アクティブビューウインドウのピクセル単位の幅。 |
| `fHeight` | `int` | アクティブビューウインドウのピクセル単位の高さ。 |

### ToolPoint

> **完全修飾名:** `api.ToolPoint` · **継承元:** `api.Object`

アクティブなツールに入力された一つの点。ツールが受け取る形式。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ToolPoint()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ToolPoint(fPoint2D, fPoint3D, fViewPoint)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fPoint2D` | `Math.Point2D` | 2Dツールではスクリーンプレーン上の点（平面とともに回転）、3Dツールではワーキングプレーン上の点。 |
| `fPoint3D` | `Point3D` | モデル上の点。 |
| `fViewPoint` | `ViewPoint` | クリックのビュー内での位置。 |

### ModeButtonDefinition

> **完全修飾名:** `api.ModeButtonDefinition` · **継承元:** `api.Object`

ツールが宣言するツールバーボタン（静的な情報で、ツールをアクティブにせずに取得可能）。ツールバーボタンを宣言しているツールのみが、この情報を提供します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ModeButtonDefinition()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ModeButtonDefinition(fName, fHelpText, fKind)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fName` | `str` | ボタンの名前。 |
| `fHelpText` | `str` | ボタンのヘルプテキスト。 |
| `fKind` | `ModeButtonKind` | ボタンの種類。 |

### Tool

> **完全修飾名:** `api.Tool` · **継承元:** `api.Object`

一つのツールの説明。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Tool()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Tool(fUniversalName, fName, fDisplayName, fCategory, fHelpText, fShortcut, fKind, fCreationType, fIsInWorkspace, fCanActivate, fIsActive, fModeButtons)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fUniversalName` | `str` | 一意の識別情報。ActivateTool / FindToolに渡します。 |
| `fName` | `str` | わかりやすい英語名（プラグインツールではfUniversalNameと同じ）。 |
| `fDisplayName` | `str` | ツールパレットに表示されるローカライズされた名前。 |
| `fCategory` | `str` | プラグインのカテゴリ（ほとんどの組み込みツールでは空）。 |
| `fHelpText` | `str` | ツールの短い説明。 |
| `fShortcut` | `str` | 現在の作業画面でのキーボードショートカット（空の場合があります）。 |
| `fKind` | `ToolKind` | ツールの種類。 |
| `fCreationType` | `ToolCreationType` | ツールによるオブジェクトの作成方法。 |
| `fIsInWorkspace` | `bool` | 現在の作業画面のツールパレットに配置されているかどうか。 |
| `fCanActivate` | `bool` | ActivateToolで現在アクティブにできるかどうか。 |
| `fIsActive` | `bool` | 現在アクティブなツールかどうか。 |
| `fModeButtons` | `list[ModeButtonDefinition]` | 宣言されたツールバーボタン（ModeButtonDefinitionを参照）。 |

### ModeChoice

> **完全修飾名:** `api.ModeChoice` · **継承元:** `api.Object`

ツールバーボタンのグループの一つの選択肢。ラジオボタン、Button/Toggleグループの単一ボタン、またはPullDown / ComboBox / SearchablePullDownグループの項目です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ModeChoice()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ModeChoice(fName, fHelpText, fImage, fId)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fName` | `str` | モード名または項目のテキスト（組み込みツールの名前のないボタンでは空の場合があります）。 |
| `fHelpText` | `str` | ツールチップのテキスト（ボタンのみ）。 |
| `fImage` | `str` | イメージリソース指定子（ボタンのみ）。例："Vectorworks/ModeViewBar/Options.png"。 |
| `fId` | `str` | 項目ID（SearchablePullDownのみ）。 |

### ToolMode

> **完全修飾名:** `api.ToolMode` · **継承元:** `api.Object`

アクティブなツールの、一つのツールバーボタンのグループの現在の状態。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ToolMode()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ToolMode(fIndex, fType, fIsEnabled, fLabel, fChoices, fChoiceCount, fSelectedChoice, fIsOn, fValue)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fIndex` | `int` | ツールバー上の位置（0始まり）。 |
| `fType` | `ModeType` | ツールバーボタンのグループの種類（ラジオ、ボタン、トグル、プルダウンなど）。 |
| `fIsEnabled` | `bool` | ツールバーボタンのグループが有効かどうか。 |
| `fLabel` | `str` | コントロールのラベル、またはラベルのないボタンではモード名。 |
| `fChoices` | `list[ModeChoice]` | ModeChoiceを参照。EditTextとResourcePopupでは空。 |
| `fChoiceCount` | `int` | 選択肢の総数（fChoicesは省略されている場合があります）。 |
| `fSelectedChoice` | `int \| None` | Radio、PullDown、ComboBox、SearchablePullDown。 |
| `fIsOn` | `bool \| None` | Toggle。 |
| `fValue` | `str` | 現在の値をテキストで表したもの（`ModeBar.GetModeValue`を参照）。 |

### ModeSetting

> **完全修飾名:** `api.ModeSetting` · **継承元:** `api.Object`

汎用のテキストベースのモードAPIが使用するモード変更要求（`ModeBar.SetMode`を参照）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ModeSetting()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ModeSetting(fModeIndex, fValue)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fModeIndex` | `int` | ツールバーボタンのグループのインデックス（0始まり）。 |
| `fValue` | `str` | `ModeBar.SetMode`と同じ方法で解釈される値。 |

### ModeBar

> **完全修飾名:** `api.ModeBar` · **継承元:** `api.Object`

アクティブなツールのツールバー（モードバー）に対する、状態を保持しないビュー。`ToolAccess.ModeBar()`で取得します。すべてのメソッドに、開かれたファイルが必要です（`Document.IsOpen()`）。

モードを変更する二つの方法：

- 型付き： — SelectRadio、PressButton、SetToggle、SelectItem、SetText、SelectResource
- 汎用：SetMode(index, "text")はモードの種類に従ってテキストを解釈し、SelectChoice(index, n)は任意のモードの種類のn番目の選択肢を選択します。

無効なモードは変更できません。変更は、ツールバー上でのユーザー操作とまったく同じように適用されます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ModeBar()` | アクティブなツールのツールバーに対する、状態を保持しないビュー（`ToolAccess().ModeBar()`と同じ）。 |

**メソッド**

*読み取り*

| メソッド | 説明 |
|---|---|
| `GetModeCount() -> int` | モード項目の数。 |
| `GetModes(maxChoices: int = 2**64 - 1) -> list[ToolMode]` | MaxChoicesは各モードのfChoicesを制限します（fChoiceCountは常に全件数を保持します）。 |
| `GetMode(modeIndex: int, maxChoices: int = 2**64 - 1) -> ToolMode \| None` | `modeIndex`、`maxChoices`に応じたモードを返します。 |
| `GetModeType(modeIndex: int) -> ModeType \| None` | `modeIndex`のモードの種類を返します。 |
| `FindMode(name: str) -> int \| None` | ラベルまたはいずれかの選択肢が`name`に一致する最初のモードのインデックス（大文字小文字を区別しません）。 |
| `GetModeValue(modeIndex: int) -> str \| None` | 現在の値をテキストで表したもの：<br>• Radio — 選択されているボタンの名前（名前がない場合はインデックス）、Toggle - "on"/"off"、Button - 空、<br>• PullDown/SearchablePullDown — 選択されている項目のテキスト、EditText/ComboBox - フィールドのテキスト、<br>• ResourcePopup — 選択されているリソースの名前。 |

*型付きの変更*

| メソッド | 説明 |
|---|---|
| `SelectRadio(modeIndex: int, choiceIndex: int) -> bool` | ボタン`choiceIndex`を、ラジオグループモード`modeIndex`で選択します。 |
| `PressButton(modeIndex: int) -> bool` | プッシュボタンモード`modeIndex`を押します。 |
| `SetToggle(modeIndex: int, isOn: bool) -> bool` | `modeIndex`のトグルを設定します。 |
| `SelectItem(modeIndex: int, itemIndex: int) -> bool` | 項目`itemIndex`を、プルダウン、コンボボックス、または検索可能なプルダウンのモード`modeIndex`で選択します。 |
| `SelectItem(modeIndex: int, itemNameOrId: str) -> bool` | PullDown、ComboBoxまたはSearchablePullDown：項目のテキストと照合します。SearchablePullDownでは項目IDとも照合します。 |
| `SetText(modeIndex: int, text: str) -> bool` | EditTextまたはComboBox。 |

*ResourcePopup*

| メソッド | 説明 |
|---|---|
| `SelectResource(modeIndex: int, resourceName: str) -> bool` | ポップアップを表示せずに、名前でリソースを選択します。 |

*汎用の変更*

| メソッド | 説明 |
|---|---|
| `SelectChoice(modeIndex: int, choiceIndex: int) -> bool` | n番目の選択肢を選択します。Radio - ボタンn、Button - 押下（nは無視）、Toggle - n != 0はオン、PullDown/ComboBox/SearchablePullDown - 項目n。EditTextとResourcePopupではサポートされません。 |
| `SetMode(modeIndex: int, value: str) -> bool` | モードの種類に従って`value`を解釈します：<br>• Radio — ボタン名、イメージ指定子、または0始まりのインデックス<br>• Button — ボタンを押す（値は無視）<br>• Toggle — "on"/"off"、"True"/"False"、"yes"/"no"、"1"/"0"または"toggle"<br>• PullDown — 項目のテキストまたは0始まりのインデックス<br>• SearchablePullDown — 項目のテキスト、項目ID、または0始まりのインデックス<br>• ComboBox — 項目のテキスト。それ以外はフィールドにテキストを入力<br>• EditText — 入力するテキスト<br>• ResourcePopup — リソース名。 |
| `SetModes(settings: list[ModeSetting]) -> bool` | 設定を順番に適用します。最初の失敗で停止し、`False`を返します。 |

### ToolControl

> **完全修飾名:** `api.ToolControl` · **継承元:** `api.Object`

アクティブなツールを操作する、状態を保持しないドライバー。ツールをアクティブにしてから`ToolAccess.Control()`で取得します。すべての入力は実際のマウスやキーボードの入力とまったく同じように処理されるため、アクティブなツールはユーザーが操作した場合と同じように動作します（プレビュー、取り消し、完了時にツールが表示するダイアログなど）。

座標：

- モデル座標（`Math.Point2D`、`Point3D`）は正確に適用されます。スマートカーソルのスナップは一時停止し、ツールは指定した点が表示されていない場合でもその点を受け取ります。2D点はレイヤプレーン上にあります（z = 0）。カーソルの下のオブジェクトを選択するツール（セレクション、変形など）では、さらにその点がアクティブなペイン内に表示されている必要があります（`ModelToView`を参照）。それ以外の場合、ポインタはペインの中央に配置されます。
- ビュー座標（`ViewPoint`）は、そのピクセルを実際にクリックした場合と同じように動作し、スマートカーソルのスナップも適用されます。アクティブなペイン内にある必要があります（`GetViewSize`を参照）。

一般的な使用例（クリック-クリックモードで二回クリックして四角形を描画）：

```python
import api
from api.Math import Point2D

tools = api.ToolAccess()
if tools.ActivateTool("Rectangle"):
    control = tools.Control()
    control.Click(Point2D(0.0, 0.0))
    control.Click(Point2D(1000.0, 500.0))
```

複数点を入力するツール（曲線ツールや壁ツールなど）は、`Finish()`または最後の点での`DoubleClick`で完了します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ToolControl()` | アクティブなツールを操作する、状態を保持しないドライバー（`ToolAccess().Control()`と同じ）。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `IsAvailable() -> bool` *静的* | 入力を受け付けるアクティブビューウインドウがあるかどうか。 |

*ツールの点*

| メソッド | 説明 |
|---|---|
| `GetToolPointCount() -> int` | アクティブなツールにこれまで入力した点。ツールが待機中の場合は空。 |
| `GetToolPoints() -> list[ToolPoint]` | ツールの点を返します。 |
| `GetCurrentPoint() -> ToolPoint \| None` | アクティブなツールの現在の（ホバー）点。 |
| `IsToolInProgress() -> bool` | アクティブなツールに点が入力されている場合はTrue（ツール操作が進行中）。 |

*座標*

| メソッド | 説明 |
|---|---|
| `GetViewSize() -> ViewSize \| None` | ビューのサイズを返します。 |
| `ModelToView(modelPoint: Math.Point2D) -> ViewPoint \| None` | モデル上の点のビュー内での位置。アクティブなペインの外側にある場合は`None`。 |
| `ModelToView(modelPoint: Point3D) -> ViewPoint \| None` | モデル上の点のビュー内での位置。アクティブなペインの外側にある場合は`None`。 |
| `ViewToModel(viewPoint: ViewPoint) -> Math.Point2D \| None` | ビュー内の位置の下にある2Dモデル点（平面ビューではレイヤプレーン上、それ以外ではスクリーンプレーン上）。 |

*ポインタ入力*

| メソッド | 説明 |
|---|---|
| `MoveTo(modelPoint: Math.Point2D) -> bool` | クリックせずにポインタを移動します。ツールはプレビュー（ラバーバンド）を新しい位置に更新します。 |
| `MoveTo(modelPoint: Point3D) -> bool` | クリックせずにポインタを移動します。ツールはプレビュー（ラバーバンド）を新しい位置に更新します。 |
| `MoveTo(viewPoint: ViewPoint) -> bool` | クリックせずにポインタを移動します。ツールはプレビュー（ラバーバンド）を新しい位置に更新します。 |
| `Click(modelPoint: Math.Point2D) -> bool` | 左クリック（マウス押下 + 解放）。通常、ツールの点を一つ追加します。 |
| `Click(modelPoint: Point3D) -> bool` | 左クリック（マウス押下 + 解放）。通常、ツールの点を一つ追加します。 |
| `Click(viewPoint: ViewPoint) -> bool` | 左クリック（マウス押下 + 解放）。通常、ツールの点を一つ追加します。 |
| `DoubleClick(modelPoint: Math.Point2D) -> bool` | ダブルクリック。複数点を入力するツールを完了するか、ポインタの下のオブジェクトを編集します（セレクションツール）。 |
| `DoubleClick(modelPoint: Point3D) -> bool` | ダブルクリック。複数点を入力するツールを完了するか、ポインタの下のオブジェクトを編集します（セレクションツール）。 |
| `DoubleClick(viewPoint: ViewPoint) -> bool` | ダブルクリック。複数点を入力するツールを完了するか、ポインタの下のオブジェクトを編集します（セレクションツール）。 |
| `Drag(from_: Math.Point2D, to: Math.Point2D) -> bool` | `from`でマウスを押下し、移動して`to`で解放します（クリック-ドラッグ描画モード、範囲選択、オブジェクトのドラッグ）。 |
| `Drag(from_: Point3D, to: Point3D) -> bool` | `from`でマウスを押下し、移動して`to`で解放します（クリック-ドラッグ描画モード、範囲選択、オブジェクトのドラッグ）。 |
| `Drag(from_: ViewPoint, to: ViewPoint) -> bool` | `from`でマウスを押下し、移動して`to`で解放します（クリック-ドラッグ描画モード、範囲選択、オブジェクトのドラッグ）。 |

*キーボードとツールのアクション*

| メソッド | 説明 |
|---|---|
| `PressKey(key: ToolKey) -> bool` | ユーザーが図面上でキーを押す場合とまったく同じようにキー入力を送信します。 |
| `Finish() -> bool` | 現在のツール操作を完了します（Returnキー）。 |
| `Cancel() -> bool` | ツールのすべての点を削除し、ツール操作を再開します。選択内容は変更しません。 |
| `RemoveLastPoint() -> bool` | ツールの最後に入力した点を削除します。 |

### ToolAccess

> **完全修飾名:** `api.ToolAccess` · **継承元:** `api.Object`

Vectorworksのツールシステムに対する、状態を保持しないファサード。必要に応じて生成します：

```python
import api

tools = api.ToolAccess()
for tool in tools.GetTools(api.ToolFilter.Activatable):   # what can be used now
    print(tool.fUniversalName, tool.fName)
if tools.ActivateTool("Rectangle"):                     # universal or friendly name
    for mode in tools.ModeBar().GetModes():            # inspect the mode bar
        print(mode)
    tools.ModeBar().SetMode(0, "Rotated Rectangle Mode")   # change a mode generically
```

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ToolAccess()` | ツールシステムに対する、状態を保持しないファサード。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `IsAvailable() -> bool` *静的* | ツールのアクティブ化とモードの変更が可能かどうか（開かれたファイルが必要）。 |

*一覧*

| メソッド | 説明 |
|---|---|
| `GetTools(filter: ToolFilter = ToolFilter.All) -> list[Tool]` | `filter`に応じたツールを返します。 |
| `FindTool(name: str) -> Tool \| None` | ユニバーサル名、わかりやすい名前、ローカライズされた表示名の順に優先してツールを検索します。 |
| `IsToolInWorkspace(name: str) -> bool` | ツール`name`が現在の作業画面のツールパレットに配置されている場合はTrue。 |
| `CanActivateTool(name: str) -> bool` | `ActivateTool(name)`で現在ツールをアクティブにできる場合はTrue。 |

*アクティブなツール*

| メソッド | 説明 |
|---|---|
| `GetActiveTool() -> Tool \| None` | アクティブなツールを返します。 |
| `GetActiveToolUniversalName() -> str \| None` | アクティブなツールのユニバーサル名を返します。 |
| `IsToolActive(name: str) -> bool` | ツール`name`がアクティブなツールの場合はTrue。 |
| `GetActiveToolHelpMessage() -> str \| None` | アクティブなツールが現在ユーザーに表示している操作案内のテキスト（例：「クリックして始点を設定」）。 |

*アクティブ化*

| メソッド | 説明 |
|---|---|
| `ActivateTool(name: str) -> bool` | ツール`name`をアクティブにします（ユニバーサル名、わかりやすい名前、または表示名）。 |
| `ActivateTool(name: str, modeSettings: list[ModeSetting]) -> bool` | ツールをアクティブにしてから、モード設定を適用します（`ModeBar.SetModes`を参照）。 |
| `ActivateTool(name: str, modeIndex: int, choiceIndex: int) -> bool` | ツールをアクティブにしてから、モードのn番目の選択肢を選択します（`ModeBar.SelectChoice`を参照）。 |
| `ActivateSelectionTool() -> bool` | デフォルトのセレクションツールに戻ります。 |

*モード*

| メソッド | 説明 |
|---|---|
| `ModeBar() -> ModeBar` | アクティブなツールのツールバー。 |

*入力*

| メソッド | 説明 |
|---|---|
| `Control() -> ToolControl` | アクティブなツールのドライバー（クリック、ドラッグ、キー入力）。 |

### MenuCommand

> **完全修飾名:** `api.MenuCommand` · **継承元:** `api.Object`

インストールされている一つのメニューコマンドの説明。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `MenuCommand()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `MenuCommand(fUniversalName, fName, fDisplayName, fCategory, fHelpText, fShortcut, fKind, fIsChunk, fIsInWorkspace, fIsEnabled)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fUniversalName` | `str` | 一意の識別情報。ExecuteMenu / FindMenuCommandに渡します。 |
| `fName` | `str` | わかりやすい英語名（プラグインコマンドではfUniversalNameと同じ）。 |
| `fDisplayName` | `str` | メニューに表示されるローカライズされたタイトル。 |
| `fCategory` | `str` | 作業画面の編集でのコマンドのカテゴリ。 |
| `fHelpText` | `str` | コマンドの短い説明。 |
| `fShortcut` | `str` | 現在の作業画面でのキーボードショートカット（空の場合があります）。 |
| `fKind` | `MenuCommandKind` | コマンドの種類（通常のコマンドまたはチャンクメニュー）。 |
| `fIsChunk` | `bool` | 項目のグループを提供します（`MenuAccess.GetChunkItems`を参照）。 |
| `fIsInWorkspace` | `bool` | 現在の作業画面のメニューに配置されているかどうか。 |
| `fIsEnabled` | `bool` | ExecuteMenuで現在実行できるかどうか（チャンクメニューの場合は、その項目の少なくとも一つ）。 |

### MenuChunkItem

> **完全修飾名:** `api.MenuChunkItem` · **継承元:** `api.Object`

チャンクメニューの現在の一つの項目。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `MenuChunkItem()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `MenuChunkItem(fIndex, fText, fIsEnabled, fIsChecked)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fIndex` | `int` | チャンクメニュー内の位置（0始まり）。 |
| `fText` | `str` | メニューに表示される項目のテキスト。 |
| `fIsEnabled` | `bool` | ExecuteMenuで現在実行できるかどうか。 |
| `fIsChecked` | `bool` | メニューにチェックマークが表示されるかどうか（Macではシェルが通知しないため、常に`False`）。 |

### MenuEntry

> **完全修飾名:** `api.MenuEntry` · **継承元:** `api.Object`

現在の作業画面で定義された、メニューバーのメニュー内の一つのエントリ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `MenuEntry()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `MenuEntry(fType, fMenuPath, fText, fUniversalName, fChunkKind, fChunkItemIndex, fShortcut, fIsEnabled, fIsChecked)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fType` | `MenuEntryType` | エントリの種類（コマンド、チャンクメニュー項目、サブメニュー、区切り）。 |
| `fMenuPath` | `list[str]` | エントリを含むメニューのタイトルを、メニューバーから下の階層へ順に示したもの（例：{"File", "Export"}）。 |
| `fText` | `str` | メニューに表示されるタイトル（区切りでは空）。 |
| `fUniversalName` | `str` | Command、ChunkItem：コマンドまたはチャンクメニューのユニバーサル名。 |
| `fChunkKind` | `MenuChunkKind` | ChunkItem：チャンクメニューの種類。 |
| `fChunkItemIndex` | `int \| None` | ChunkItem：チャンクメニュー内の項目のインデックス。 |
| `fShortcut` | `str` | キーボードショートカット（空の場合があります）。 |
| `fIsEnabled` | `bool` | Command、ChunkItem：ExecuteMenuEntryで現在実行できるかどうか。 |
| `fIsChecked` | `bool` | Command、ChunkItem：メニューにチェックマークが表示されるかどうか（`MenuChunkItem.fIsChecked`を参照）。 |

### MenuAccess

> **完全修飾名:** `api.MenuAccess` · **継承元:** `api.Object`

Vectorworksのメニューシステムに対する、状態を保持しないファサード。必要に応じて生成します：

```python
import api

menus = api.MenuAccess()
for entry in menus.GetMenuEntries("Modify"):          # what the Modify menu offers
    print(entry)
if menus.GetMenuStatus("Select All") == api.MenuStatus.Ready:   # universal, friendly or display name
    menus.ExecuteMenu("Select All")
for item in menus.GetChunkItems("Recent Docs"):      # current items of a chunk
    print(item)
menus.ExecuteMenu("Standard Views", "Top/Plan")           # a chunk item by its text
```

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `MenuAccess()` | メニューシステムに対する、状態を保持しないファサード。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `IsAvailable() -> bool` *静的* | 現在メニューコマンドを実行できるかどうか。メニューバーが設定済みで、プラグインオブジェクトが再生成中でないことが条件です。 |

*一覧*

| メソッド | 説明 |
|---|---|
| `GetMenuCommands(filter: MenuFilter = MenuFilter.All) -> list[MenuCommand]` | `filter`に応じたメニューコマンドを返します。 |
| `FindMenuCommand(name: str) -> MenuCommand \| None` | ユニバーサル名、わかりやすい名前、ローカライズされた表示名の順に優先してコマンドを検索します。優先度が同じ場合は、作業画面に配置されているコマンドが優先されます。 |
| `IsMenuCommandInWorkspace(name: str) -> bool` | コマンド`name`が現在の作業画面のメニューに配置されている場合はTrue。 |

*現在の作業画面のメニューバー*

| メソッド | 説明 |
|---|---|
| `GetMenuTitles() -> list[str]` | メニューバーのメニューのタイトル。左から右の順。 |
| `GetMenuEntries() -> list[MenuEntry]` | メニューバーのすべてのエントリを、メニュー順の深さ優先で返します。Submenuエントリの後にはそのサブメニューのエントリが続き、チャンクメニューは現在の項目に展開されます。 |
| `GetMenuEntries(menuTitle: str) -> list[MenuEntry]` | メニューバーの一つのメニューのエントリ（GetMenuTitlesを参照）。そのサブメニューも含みます。 |
| `FindMenuEntry(path: list[str]) -> MenuEntry \| None` | メニューパスとテキストが`path`に一致するエントリ。例：{"Modify", "Align", "Align Left"}。 |

*チャンクメニュー*

| メソッド | 説明 |
|---|---|
| `GetChunkItems(name: str) -> list[MenuChunkItem]` | 作業画面に配置されているチャンクメニューの現在の項目を、メニューバーに表示されるとおりに返します（上記の「チャンクメニュー」を参照）。区切りとテキストのないプレースホルダーは除外します（fIndexは項目の位置を維持します）。`name`が作業画面に配置されたチャンクメニューでない場合は空。 |
| `FindChunkItem(name: str, itemText: str) -> int \| None` | テキストが`itemText`に一致するチャンクメニュー項目のインデックス。 |

*実行*

| メソッド | 説明 |
|---|---|
| `GetMenuStatus(name: str) -> MenuStatus` | ExecuteMenuが現在コマンド（またはチャンクメニュー項目）を実行できるかどうか、および実行できない理由。インデックスを指定しない場合、チャンクメニューの項目がちょうど一つであれば受け付けます。 |
| `GetMenuStatus(name: str, chunkItemIndex: int) -> MenuStatus` | ExecuteMenuが現在コマンド（またはチャンクメニュー項目）を実行できるかどうか、および実行できない理由。インデックスを指定しない場合、チャンクメニューの項目がちょうど一つであれば受け付けます。 |
| `CanExecuteMenu(name: str) -> bool` | `ExecuteMenu(name)`で現在コマンドを実行できる場合はTrue。 |
| `ExecuteMenu(name: str) -> bool` | 通常のコマンド、またはチャンクメニューの唯一の項目を実行します。実行されなかった理由を確認するにはGetMenuStatusを使用してください。 |
| `ExecuteMenu(name: str, chunkItemIndex: int) -> bool` | インデックスまたはテキストで指定したチャンクメニューの項目を実行します。 |
| `ExecuteMenu(name: str, chunkItemText: str) -> bool` | インデックスまたはテキストで指定したチャンクメニューの項目を実行します。 |
| `ExecuteMenuEntry(entry: MenuEntry) -> bool` | GetMenuEntriesのCommandまたはChunkItemエントリを実行します。 |

### OIPControl

> **完全修飾名:** `api.OIPControl` · **継承元:** `api.Object`

オブジェクト情報パレット（OIP）の一つのコントロールの説明と現在の状態。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `OIPControl()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `OIPControl(fId, fPane, fType, fCoreTypeId, fParentId, fLabel, fValue, fChoices, fChoiceCount, fSelectedChoice, fIsChecked, fIsEnabled, fIsVisible, fIsReadOnly, fIsIndeterminate)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fId` | `int` | コントロールID。オブジェクト情報パレットが再構築されるまで有効。 |
| `fPane` | `OIPPane` | コントロールのタブ。 |
| `fType` | `OIPControlType` | コントロールの種類。 |
| `fCoreTypeId` | `int` | コントロールの内部タイプID（診断用）。 |
| `fParentId` | `int` | 親コントロールのID（ない場合は0）。 |
| `fLabel` | `str` | コントロールの横に表示されるプロンプト／ラベル。 |
| `fValue` | `str` | 現在の値をテキストで表したもの（`OIPAccess.GetValue`を参照）。 |
| `fChoices` | `list[str]` | RadioGroup、PullDown、ClassPullDown、LayerPullDown。 |
| `fChoiceCount` | `int` | 選択肢の総数（fChoicesは省略されている場合があります）。 |
| `fSelectedChoice` | `int \| None` | RadioGroup、PullDown、SearchablePullDown、ClassPullDown、LayerPullDown。 |
| `fIsChecked` | `bool \| None` | CheckBox（未確定状態の場合は空）。 |
| `fIsEnabled` | `bool` | コントロールが有効かどうか。 |
| `fIsVisible` | `bool` | コントロールが表示されているかどうか。 |
| `fIsReadOnly` | `bool` | 値を表示するだけのEditText。 |
| `fIsIndeterminate` | `bool` | 値が異なる複数のオブジェクトの選択。 |

### OIPSetting

> **完全修飾名:** `api.OIPSetting` · **継承元:** `api.Object`

汎用のテキストベースのAPIが使用するコントロール変更要求（`OIPAccess.SetValue`を参照）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `OIPSetting()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `OIPSetting(fPane, fControlId, fValue)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fPane` | `OIPPane` | コントロールのタブ。 |
| `fControlId` | `int` | コントロールのID。 |
| `fValue` | `str` | `OIPAccess.SetValue`と同じ方法で解釈される値。 |

### OIPAccess

> **完全修飾名:** `api.OIPAccess` · **継承元:** `api.Object`

オブジェクト情報パレットに対する、状態を保持しないファサード。必要に応じて生成します：

```python
import api

oip = api.OIPAccess()
for control in oip.GetControls(api.OIPPane.Shape):     # what the OIP shows now
    print(control)
control_id = oip.FindControl(api.OIPPane.Shape, "Width")   # find a control by its label
if control_id is not None:
    oip.SetValue(api.OIPPane.Shape, control_id, "200")     # change it as the user would
```

コントロールを変更する二つの方法：

- 型付き：`SetText`、`SetChecked`、`SelectChoice`、`PressButton`
- 汎用：`SetValue(pane, id, "text")`は、コントロールの種類に従ってテキストを解釈します。

無効、非表示、読み取り専用のコントロールは変更できません。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `OIPAccess()` | オブジェクト情報パレットに対する、状態を保持しないファサード。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `IsAvailable() -> bool` *静的* | オブジェクト情報パレットにアクセスできるかどうか（開かれたファイルが必要）。 |
| `IsPaneAvailable(pane: OIPPane) -> bool` | タブに現在コントロールが表示されているかどうか（選択内容、または一部のタブではファイルのデフォルト設定が必要）。 |

*読み取り*

| メソッド | 説明 |
|---|---|
| `GetControls(pane: OIPPane = OIPPane.Shape, maxChoices: int = 2**64 - 1, includeHidden: bool = False) -> list[OIPControl]` | タブのコントロールをID順に返します。maxChoicesは各コントロールのfChoicesを制限します（fChoiceCountは常に全件数を保持します）。includeHiddenが`True`でない限り、非表示のコントロールはスキップします。 |
| `GetControl(pane: OIPPane, controlId: int, maxChoices: int = 2**64 - 1) -> OIPControl \| None` | `pane`、`controlId`、`maxChoices`に応じたコントロールを返します。 |
| `FindControl(pane: OIPPane, label: str) -> int \| None` | ラベルが`label`に一致する、最初の表示コントロールのID（大文字小文字を区別せず、末尾の':'は無視します）。 |
| `GetValue(pane: OIPPane, controlId: int) -> str \| None` | 現在の値をテキストで表したもの：<br>• EditText — フィールドのテキスト、StaticText - ラベル、CheckBox - "on"/"off"（未確定状態の場合は空）、Button - 空、<br>• RadioGroup/PullDown/SearchablePullDown/ClassPullDown/LayerPullDown — 選択されている項目のテキスト、Other - 空。 |

*EditText*

| メソッド | 説明 |
|---|---|
| `SetText(pane: OIPPane, controlId: int, text: str) -> bool` | ユーザーが入力する場合と同じようにテキストを入力します（単位と数式はVectorworksが評価します）。 |
| `SetChecked(pane: OIPPane, controlId: int, isChecked: bool) -> bool` | チェック状態を設定します。 |
| `SelectChoice(pane: OIPPane, controlId: int, choiceIndex: int) -> bool` | RadioGroup、PullDown、SearchablePullDown、ClassPullDown、LayerPullDown。 |
| `SelectChoice(pane: OIPPane, controlId: int, choiceName: str) -> bool` | RadioGroup、PullDown、SearchablePullDown、ClassPullDown、LayerPullDown。 |

*Button*

| メソッド | 説明 |
|---|---|
| `PressButton(pane: OIPPane, controlId: int) -> bool` | ボタンを押して離します（UIが表示される場合があります）。 |

*汎用の変更*

| メソッド | 説明 |
|---|---|
| `SetValue(pane: OIPPane, controlId: int, value: str) -> bool` | コントロールの種類に従って`value`を解釈します：<br>• EditText — 入力するテキスト<br>• CheckBox — "on"/"off"、"True"/"False"、"yes"/"no"、"1"/"0"または"toggle"<br>• RadioGroup/PullDown/SearchablePullDown/ClassPullDown/LayerPullDown — 項目のテキスト。それ以外は0始まりのインデックス<br>• Button — ボタンを押す（値は無視）<br>• StaticText/Other — 非対応。 |
| `SetValues(settings: list[OIPSetting]) -> bool` | 設定を順番に適用します。最初の失敗で停止し、`False`を返します。変更のたびにオブジェクト情報パレットが再構築される可能性があるため、コントロールIDは直前に読み取る必要があります。 |

*生の値によるアクセス*

| メソッド | 説明 |
|---|---|
| `NotifyChanged(pane: OIPPane, controlId: int, changeInfo: int) -> bool` | 任意のコントロールに対して、生の変更情報を使用して「ウィジェット変更」イベントを発生させます（単純な値の変更は0。複合コントロールは独自の変更コードを使用します）。値はあらかじめオブジェクト情報パレットに設定されている必要があります。`OIPControlType.Other`コントロールに使用してください。 |
| `Refresh(pane: OIPPane) -> bool` | 現在の選択内容からタブを再構築します。 |

<a id="enumerations"></a>

## 列挙型

### ToolKind

> **完全修飾名:** `api.ToolKind` · **種類:** `IntEnum`

ツールの提供形態。

| メンバー | 値 | 説明 |
|---|---|---|
| `Unknown` | `0` |  |
| `InternalClassic` | `1` | Vectorworksに組み込まれています（従来型ツール）。 |
| `InternalExtension` | `2` | Vectorworksに組み込まれています（拡張ツール）。 |
| `ScriptPlugin` | `3` | VectorScript / Pythonのプラグインツール。 |
| `ExtensionPlugin` | `4` | 外部プラグインモジュールのツール。 |

### ToolCreationType

> **完全修飾名:** `api.ToolCreationType` · **種類:** `IntEnum`

オブジェクト作成にツールが使用する操作の種類。

| メンバー | 値 | 説明 |
|---|---|---|
| `Normal` | `0` | 通常のツール（独自のクリック処理）。 |
| `Point` | `1` | 一回のクリックで点オブジェクトを配置します。 |
| `Line` | `2` | 二回のクリックで線状のオブジェクトを定義します。 |
| `Box` | `3` | 二回のクリックで長方形状のオブジェクトを定義します。 |
| `Path2D` | `4` | クリックで2Dパスオブジェクトを定義します。 |
| `Path3D` | `5` | クリックで3Dパスオブジェクトを定義します。 |
| `Custom` | `6` | 独自のオブジェクト作成。 |

### ToolFilter

> **完全修飾名:** `api.ToolFilter` · **種類:** `IntEnum`

`ToolAccess.GetTools`が返すツールの範囲。

| メンバー | 値 | 説明 |
|---|---|---|
| `All` | `0` | 作業画面にないツールを含め、Vectorworksにインストールされているすべてのツール。 |
| `Activatable` | `1` | ActivateToolで現在アクティブにできるツールのみ。 |
| `InWorkspace` | `2` | 現在の作業画面のツールパレットに配置されているツールのみ。 |

### ModeType

> **完全修飾名:** `api.ModeType` · **種類:** `IntEnum`

アクティブなツールのツールバーボタンのグループの種類。

| メンバー | 値 | 説明 |
|---|---|---|
| `Radio` | `0` | 排他的なボタンのグループ。必ず一つだけが選択されます。 |
| `Button` | `1` | アクションを実行するプッシュボタン（ツールの設定ダイアログボックスなどのUIが表示される場合があります）。 |
| `Toggle` | `2` | オン／オフボタン。 |
| `PullDown` | `3` | 固定の項目リストを持つプルダウンメニュー。 |
| `EditText` | `4` | ラベル付きの編集フィールド。 |
| `ResourcePopup` | `5` | リソース名で選択するリソースポップアップ（シンボル、スタイル、テクスチャなど）。 |
| `SearchablePullDown` | `6` | 検索可能なプルダウン。項目は名前またはIDで識別します。 |
| `ComboBox` | `7` | 候補項目のリストを持つ編集フィールド。 |

### ModeButtonKind

> **完全修飾名:** `api.ModeButtonKind` · **種類:** `IntEnum`

ツールの登録時に宣言されたツールバーボタンの種類（現在のModeTypeとは異なる場合があります）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Radio` | `0` |  |
| `Button` | `1` |  |
| `Preferences` | `2` | ツールの設定ダイアログボックスを開きます。 |
| `Check` | `3` | トグルボタン。 |
| `EditText` | `4` |  |
| `PullDown` | `5` |  |

### ToolKey

> **完全修飾名:** `api.ToolKey` · **種類:** `IntEnum`

点の入力中にツールが反応するキー（`ToolControl.PressKey`を参照）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Return` | `0` | Return/Enterで完了するツールの操作を完了します（複数点を入力するツールなど）。 |
| `Escape` | `1` | ツールのすべての点を削除します。ツールの点がない場合は、ユーザーのキー操作と同様に選択も解除します。 |
| `Backspace` | `2` | ツールの最後の点を削除します。 |

### MenuCommandKind

> **完全修飾名:** `api.MenuCommandKind` · **種類:** `IntEnum`

メニューコマンドの提供形態。

| メンバー | 値 | 説明 |
|---|---|---|
| `Unknown` | `0` |  |
| `Internal` | `1` | Vectorworksに組み込まれています。ユニバーサル名は負の数です（例："-28"）。 |
| `ScriptPlugin` | `2` | VectorScript / Pythonのプラグインメニューコマンド（.vsmファイル）。 |
| `ExtensionPlugin` | `3` | 外部プラグインモジュールのメニューコマンド。 |

### MenuChunkKind

> **完全修飾名:** `api.MenuChunkKind` · **種類:** `IntEnum`

チャンクメニューの種類（上記の「チャンクメニュー」を参照）。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` | チャンクメニューではなく、通常のコマンド。 |
| `Regular` | `1` | 固定の項目リスト。 |
| `Dynamic` | `2` | メニューバーの構築時に構築される項目（インストール済みの作業画面など）。 |
| `Variable` | `3` | Vectorworksの実行中に変わる項目（最近使ったファイル、開いているファイルなど）。 |

### MenuFilter

> **完全修飾名:** `api.MenuFilter` · **種類:** `IntEnum`

`MenuAccess.GetMenuCommands`が返すメニューコマンドの範囲。

| メンバー | 値 | 説明 |
|---|---|---|
| `All` | `0` | 作業画面にないコマンドを含め、Vectorworksにインストールされているすべてのメニューコマンド。 |
| `Executable` | `1` | fIsEnabledが設定されているコマンドのみ（ExecuteMenuで現在実行可能。チャンクメニューの場合は、その項目の少なくとも一つ）。 |
| `InWorkspace` | `2` | 現在の作業画面のメニューに配置されているコマンドのみ。 |

### MenuEntryType

> **完全修飾名:** `api.MenuEntryType` · **種類:** `IntEnum`

メニューバーのメニュー内のエントリの種類。

| メンバー | 値 | 説明 |
|---|---|---|
| `Command` | `0` | 通常のコマンド。 |
| `ChunkItem` | `1` | チャンクメニューの一つの項目。 |
| `Submenu` | `2` | サブメニューを開きます。その後にサブメニューのエントリが続きます。 |
| `Separator` | `3` | 区切り線。 |

### MenuStatus

> **完全修飾名:** `api.MenuStatus` · **種類:** `IntEnum`

メニューコマンド（またはチャンクメニュー項目）を現在実行できるかどうか、および実行できない理由（`MenuAccess.GetMenuStatus`を参照）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Ready` | `0` | ExecuteMenuで現在実行できるかどうか。 |
| `Unavailable` | `1` | 現在はどのコマンドも実行できません。メニューバーが未設定か、プラグインオブジェクトが再生成中です。 |
| `NotFound` | `2` | この名前のメニューコマンドはインストールされていません。 |
| `NotInWorkspace` | `3` | インストール済みですが、現在の作業画面のメニューに配置されていません。 |
| `Disabled` | `4` | 現在の状態では無効（開かれたファイル、選択内容などが必要）。 |
| `ChunkItemRequired` | `5` | 複数の項目を持つチャンクメニュー。項目のインデックスまたはテキストを渡してください。 |
| `ChunkItemNotFound` | `6` | チャンクメニューにこのインデックスまたはテキストの項目がないか、コマンドがチャンクメニューではありません。 |

### OIPPane

> **完全修飾名:** `api.OIPPane` · **種類:** `IntEnum`

オブジェクト情報パレットのタブ（ペイン）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Shape` | `0` | 形状とパラメータのプロパティ。 |
| `Data` | `1` | レコードおよびその他の連結データ。 |
| `Render` | `2` | テクスチャ。 |

### OIPControlType

> **完全修飾名:** `api.OIPControlType` · **種類:** `IntEnum`

オブジェクト情報パレット（OIP）のコントロールの種類。

| メンバー | 値 | 説明 |
|---|---|---|
| `EditText` | `0` | 編集フィールド（数値、寸法、角度、テキスト）。読み取り専用の場合があります。 |
| `StaticText` | `1` | ラベルまたは区切り。 |
| `CheckBox` | `2` | オン／オフのチェックボックス。 |
| `RadioGroup` | `3` | ラジオボタンまたはプッシュボタン。必ず一つだけが選択されます。 |
| `PullDown` | `4` | 固定の項目リストを持つプルダウンメニュー（ポップアップ、コンボボックス、メニューボタン）。 |
| `SearchablePullDown` | `5` | 検索可能なプルダウン。 |
| `Button` | `6` | アクションを実行するプッシュボタン（UIが表示される場合があります）。 |
| `ClassPullDown` | `7` | クラスのプルダウン。 |
| `LayerPullDown` | `8` | レイヤのプルダウン。 |
| `Other` | `9` | その他のコントロール（ボックス位置、3D位置、色、リストなど）。`OIPAccess.NotifyChanged`を参照してください。 |

---

[一覧に戻る](README.md) · [先頭に戻る](#uiautomation--tools-the-tool-bar-menus-and-the-object-info-palette)
