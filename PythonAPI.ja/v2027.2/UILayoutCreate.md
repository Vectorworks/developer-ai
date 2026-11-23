[English](../../PythonAPI/v2027.2/UILayoutCreate.md) • [Deutsch](../../PythonAPI.de/v2027.2/UILayoutCreate.md) • **日本語**

<a id="uilayoutcreate--alerts-standard-dialogs-and-layout-dialogs"></a>

# UILayoutCreate — アラート、標準ダイアログ、レイアウトダイアログ

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

ユーザーインターフェイスのクラス群：`Alerts`（メッセージボックス、質問、警告、エラー）、`StandardDialogs`（一つまたは二つの値を編集するか、リストから選択するための既成のダイアログ）、`LayoutDialog`（コントロールを一つずつ配置して構築し、Pythonでイベントハンドラーを記述する任意のモーダルダイアログ）。値型の`DialogEvent`と`ListBrowserEvent`、およびダイアログの列挙型もこのグループに属します。

ダイアログはモーダルです。`Run()`はユーザーがダイアログを閉じると戻ります。`Run()`の後もコントロールの値を読み取れます。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [DialogEvent](#dialogevent)
  - [ListBrowserEvent](#listbrowserevent)
  - [DialogSize](#dialogsize)
  - [Alerts](#alerts)
  - [TextPair](#textpair)
  - [StandardDialogs](#standarddialogs)
  - [LayoutDialog](#layoutdialog)
- [列挙型](#enumerations)
  - [DialogResult](#dialogresult)
  - [AlertButton](#alertbutton)
  - [EditRealType](#editrealtype)
  - [StaticTextStyle](#statictextstyle)
  - [CheckState](#checkstate)
  - [DialogEventType](#dialogeventtype)
  - [ListBrowserControlType](#listbrowsercontroltype)
  - [ListBrowserDisplayType](#listbrowserdisplaytype)
  - [ListBrowserEventType](#listbrowsereventtype)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`DialogEvent`](#dialogevent) | クラス |  | レイアウトダイアログのハンドラーに渡される一つのイベント。 |
| [`ListBrowserEvent`](#listbrowserevent) | クラス |  | 最後のリストブラウザイベントの詳細。 |
| [`DialogSize`](#dialogsize) | クラス |  | ダイアログのサイズ。ピクセル単位。 |
| [`Alerts`](#alerts) | クラス |  | Vectorworks標準のアラート：情報、エラー、質問のアラート（静的関数のみ）。 |
| [`TextPair`](#textpair) | クラス |  | 二つのテキスト欄を持つダイアログに入力された値。 |
| [`StandardDialogs`](#standarddialogs) | クラス |  | 一つまたは二つの値を編集するか、リストから選択するための既成のダイアログ（静的関数のみ）。 |
| [`LayoutDialog`](#layoutdialog) | クラス |  | コードでコントロールを一つずつ配置して構築する、モーダルなレイアウトマネージャダイアログ。 |
| [`DialogResult`](#dialogresult) | IntEnum |  | ダイアログまたはアラートが閉じられた方法。 |
| [`AlertButton`](#alertbutton) | IntEnum |  | 質問アラートのデフォルトボタン。 |
| [`EditRealType`](#editrealtype) | IntEnum |  | 実数編集フィールドに表示する値の種類。 |
| [`StaticTextStyle`](#statictextstyle) | IntEnum |  | 固定テキストのフォントスタイル。 |
| [`CheckState`](#checkstate) | IntEnum |  | 三状態チェックボックス、リストブラウザのセル、またはツリー項目のチェックボックスの状態。 |
| [`DialogEventType`](#dialogeventtype) | IntEnum |  | ダイアログイベントの種類（DialogEventを参照）。 |
| [`ListBrowserControlType`](#listbrowsercontroltype) | IntEnum |  | リストブラウザの列の動作。 |
| [`ListBrowserDisplayType`](#listbrowserdisplaytype) | IntEnum |  | リストブラウザの列に表示する内容。 |
| [`ListBrowserEventType`](#listbrowsereventtype) | IntEnum |  | リストブラウザで発生した内容（`LayoutDialog.GetListBrowserEvent`を参照）。 |

<a id="classes"></a>

## クラス

### DialogEvent

> **完全修飾名:** `api.DialogEvent` · **継承元:** `api.Object`

レイアウトダイアログのハンドラーに渡される一つのイベント。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DialogEvent()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `DialogEvent(fDialogID, fControlID, fEvent, fData, fIsNegative)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fDialogID` | `int` | ダイアログのレイアウトマネージャID。 |
| `fControlID` | `int` | Controlイベントを発生させたコントロール。Okでは1、Cancelでは2、それ以外では0。 |
| `fEvent` | `DialogEventType` | イベントの種類。 |
| `fData` | `int` | コントロール固有の値（新しいスライダー位置、0x00RRGGBB形式の選択色など）、またはOtherのメッセージコード。 |
| `fIsNegative` | `bool` | レイアウトマネージャがコントロールイベントを負のIDで通知したことを示します（二次的なアクション。リストブラウザのダブルクリックなど）。 |

### ListBrowserEvent

> **完全修飾名:** `api.ListBrowserEvent` · **継承元:** `api.Object`

最後のリストブラウザイベントの詳細。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ListBrowserEvent()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ListBrowserEvent(fEvent, fRow, fColumn)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fEvent` | `ListBrowserEventType` | リストブラウザイベントの種類。 |
| `fRow` | `int` | イベントの行（0始まり）。 |
| `fColumn` | `int` | イベントの列（0始まり）。 |

### DialogSize

> **完全修飾名:** `api.DialogSize` · **継承元:** `api.Object`

ダイアログのサイズ。ピクセル単位。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DialogSize()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `DialogSize(fWidth, fHeight)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fWidth` | `int` | ピクセル単位の幅。 |
| `fHeight` | `int` | ピクセル単位の高さ。 |

### Alerts

> **完全修飾名:** `api.Alerts` · **継承元:** `api.Object`

Vectorworks標準のアラート：情報、エラー、質問のアラート（静的関数のみ）。

**コンストラクタ**

Pythonからはインスタンス化できません。クラスの静的メソッドを使用してください（`api.Alerts.Method(...)`）。

**メソッド**

| メソッド | 説明 |
|---|---|
| `Inform(text: str, advice: str = '', isMinor: bool = False, category: str = '', item: str = '', checkboxText: str = '') -> None` *静的* | OKボタンを持つ情報アラート。軽微なアラートは目立ちにくい表示になります（アイコンの強調なし）。 |
| `Critical(text: str, advice: str = '') -> None` *静的* | OKボタンを持つエラーアラート。 |
| `Question(question: str, advice: str = '', defaultButton: AlertButton = AlertButton.Ok, okText: str = '', cancelText: str = '', buttonAText: str = '', buttonBText: str = '', category: str = '', item: str = '', checkboxText: str = '') -> DialogResult` *静的* | 質問アラート。ボタンのテキストが空の場合はデフォルトのラベルを使用します。ボタンAとBはテキストがある場合のみ表示します。Ok、Cancel、ButtonAまたはButtonBを返します。 |
| `Confirm(question: str, advice: str = '', okText: str = '', cancelText: str = '', isOkDefault: bool = True) -> bool` *静的* | 二つのボタンを持つ質問アラート（例：okTextは"Yes"、cancelTextは"No"）。OKボタンが選択された場合は`True`を返します。 |
| `InformWithLink(text: str, adviceBeforeLink: str, linkTitle: str, linkURL: str, adviceAfterLink: str = '', isMinor: bool = False, category: str = '', item: str = '', checkboxText: str = '') -> None` *静的* | 案内にハイパーリンクを含む情報アラート：adviceBeforeLink、`[linkTitle](linkURL)`、adviceAfterLink。 |
| `CriticalWithLink(text: str, adviceBeforeLink: str, linkTitle: str, linkURL: str, adviceAfterLink: str = '') -> None` *静的* | 案内にハイパーリンクを含むエラーアラート。 |
| `AreAlertsAllowed() -> bool` *静的* | アラートが抑制されている場合は`False`（バッチモードや自動テストモードでの実行中など）。 |

### TextPair

> **完全修飾名:** `api.TextPair` · **継承元:** `api.Object`

二つのテキスト欄を持つダイアログに入力された値。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `TextPair()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `TextPair(fFirst, fSecond)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `==` | `__eq__(o: TextPair) -> bool` | `a == b`：二つの値が等しい場合はTrue。 |
| `!=` | `__ne__(o: TextPair) -> bool` | `a != b`：二つの値が異なる場合はTrue。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `fFirst` | `str` | 最初のフィールドのテキスト。 |
| `fSecond` | `str` | 二番目のフィールドのテキスト。 |

### StandardDialogs

> **完全修飾名:** `api.StandardDialogs` · **継承元:** `api.Object`

一つまたは二つの値を編集するか、リストから選択するための既成のダイアログ（静的関数のみ）。

**コンストラクタ**

Pythonからはインスタンス化できません。クラスの静的メソッドを使用してください（`api.StandardDialogs.Method(...)`）。

**メソッド**

| メソッド | 説明 |
|---|---|
| `EditText(title: str, label: str, value: str = '', okText: str = '', cancelText: str = '', helpText: str = '', isEmptyAllowed: bool = True) -> str \| None` *静的* | 一つの単一行テキストフィールド。isEmptyAllowedが`False`の場合、フィールドが空の間はOKが無効のままになります。 |
| `EditMultilineText(title: str, label: str, value: str = '', width: int = 40, height: int = 10, okText: str = '', cancelText: str = '', helpText: str = '', isEmptyAllowed: bool = True) -> str \| None` *静的* | 一つの複数行テキストフィールド。幅は標準文字数、高さは行数。 |
| `EditTwoTexts(title: str, label1: str, label2: str, value1: str = '', value2: str = '', helpText1: str = '', helpText2: str = '', okText: str = '', cancelText: str = '') -> TextPair \| None` *静的* | 二つの単一行テキストフィールド。 |
| `EditInteger(title: str, label: str, value: int = 0, okText: str = '', cancelText: str = '', helpText: str = '') -> int \| None` *静的* | 一つのフィールドを持つダイアログで整数の入力を求めます。ユーザーがキャンセルした場合は`None`。 |
| `EditReal(title: str, label: str, value: float = 0.0, okText: str = '', cancelText: str = '', helpText: str = '') -> float \| None` *静的* | 通常の実数。 |
| `EditDimension(title: str, label: str, value: float = 0.0, okText: str = '', cancelText: str = '', helpText: str = '') -> float \| None` *静的* | ワールド単位の長さ。表示と入力にはファイルの単位を使用します。 |
| `EditAngle(title: str, label: str, value: float = 0.0, okText: str = '', cancelText: str = '', helpText: str = '') -> float \| None` *静的* | 度単位の角度。 |
| `EditPoint2D(title: str, label: str, value: Point2D = Point2D(), okText: str = '', cancelText: str = '', helpText: str = '') -> Point2D \| None` *静的* | XとYのフィールド。 |
| `EditPoint3D(title: str, label: str, value: Point3D = Point3D(), okText: str = '', cancelText: str = '', helpText: str = '') -> Point3D \| None` *静的* | X、Y、Zのフィールド。 |
| `ChooseFromList(title: str, label: str, choices: list[str], selectedIndex: int = 0, okText: str = '', cancelText: str = '') -> int \| None` *静的* | 選択肢のリスト。選択された項目の0始まりのインデックスを返します。selectedIndexが-1の場合は何も選択しません。 |
| `ChooseManyFromList(title: str, label: str, choices: list[str], selectedIndices: list[int] = [], okText: str = '', cancelText: str = '') -> list[int] \| None` *静的* | 複数選択可能な選択肢のリスト。選択された項目の0始まりのインデックスを返します。 |

### LayoutDialog

> **完全修飾名:** `api.LayoutDialog` · **継承元:** `api.Object`

コードでコントロールを一つずつ配置して構築する、モーダルなレイアウトマネージャダイアログ。ライフサイクル（一回限り：ダイアログは最大一回実行できます）：

1. **生成** — OKボタンと、必要に応じてキャンセルボタンを持つレイアウトを作成します。
2. **コントロールを追加** — 各コントロールに対して`Add<Control>(controlID, ...)`を呼び出します。IDは呼び出し側で選択します（3 .. 9999）。
3. **コントロールを配置** — 左上のコントロールに`SetFirstItem(controlID)`を使用し、次に`PlaceBelow` / `PlaceRight`で他のコントロールとの相対位置を指定します。グループボックス、タブペイン、切り替えペインの子は、`SetFirstGroupItem(groupControlID, controlID)`で配置を開始します。`BindEdges`と`Align*`はサイズ変更を制御します。
4. **ハンドラーを登録** — `OnSetup`、`OnControl(controlID, handler)`、`OnOk`、`OnCancel`など（すべて任意。ハンドラーは`DialogEvent`を受け取るPythonの呼び出し可能オブジェクト）。
5. **実行** — ダイアログを表示し、閉じるまで処理をブロックします。`DialogResult.Ok`または`DialogResult.Cancel`を返します。
6. **値を読み取る** — `Get...`関数は`Run`の後も使用できます。ダイアログが閉じるときに、すべてのコントロールの値が取得されます。

値を操作する関数（`Set...`、`Select...`、`Add...Item`など）は、コントロールの追加後であればいつでも呼び出せます。ダイアログの表示前に行った呼び出しはキューに登録され、Setupハンドラーが実行される直前に順番に適用されます。`Get...`関数は、ダイアログが表示される前は`None`を返します。

選択肢、リストブラウザの行／列、タブペインのインデックスは0始まりです。ツリー項目は`AddTreeItem`が返すIDで識別し、ルートの親は-1です。`controlID`、`referenceControlID`、`groupControlID`、`paneControlID`、`tabControlID`、`swapControlID`はコントロールを識別します。`alignmentGroupID`は、コントロールではなく、共有の辺揃え識別子です。`itemID`と`parentID`はツリーコントロール内の項目を識別します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `LayoutDialog(title: str, okText: str = '', cancelText: str = '', hasCancel: bool = True, isWidthResizable: bool = False, isHeightResizable: bool = False)` | okText/cancelTextが空の場合は、デフォルトの"OK"/"Cancel"ラベルを使用します。hasCancelが`False`の場合はOKボタンのみを表示します。 |

**メソッド**

*ライフサイクル*

| メソッド | 説明 |
|---|---|
| `IsValid() -> bool` | このオブジェクトが既存のレイアウトダイアログを参照している場合はTrue（レイアウトが作成済みで未実行、または実行中）。 |
| `GetDialogID() -> int` | ダイアログIDを返します（レイアウトマネージャID。レイアウトを作成できなかった場合は0）。 |
| `IsRunning() -> bool` | Setupイベントから`Run`が戻るまでの間はTrue。 |
| `WasRun() -> bool` | `Run`が戻った場合はTrue。 |
| `Run(helpID: str = '') -> DialogResult` | ダイアログを表示し、閉じるまで処理をブロックします。`DialogResult.Ok`または`DialogResult.Cancel`を返します。ダイアログがすでに実行済み、またはレイアウトが無効な場合は`DialogResult.None_`を返します。`helpID`はコンテキストヘルプの識別子です。 |
| `Close(isOk: bool = True) -> bool` | イベントハンドラーから、OK（isOk）またはキャンセルが押された場合と同じように実行中のダイアログを閉じます。OnOk / OnCancelハンドラーは呼び出されません。イベントハンドラーの外では`False`を返します。 |
| `CancelClose() -> None` | OnOkまたはOnCancelハンドラーから呼び出し、ダイアログを開いたままにします（検証エラー後など）。 |

*イベントハンドラー*

| メソッド | 説明 |
|---|---|
| `OnSetup(handler: callable(DialogEvent)) -> None` | ダイアログの設定時、表示される直前に呼び出す`handler`を登録します。 |
| `OnSetdown(handler: callable(DialogEvent)) -> None` | ダイアログを閉じるときに呼び出す`handler`を登録します。 |
| `OnOk(handler: callable(DialogEvent)) -> None` | OKが押されたときに呼び出す`handler`を登録します（その中で`CancelClose()`を呼び出すと、ダイアログを開いたままにできます）。 |
| `OnCancel(handler: callable(DialogEvent)) -> None` | キャンセルが押されたときに呼び出す`handler`を登録します（その中で`CancelClose()`を呼び出すと、ダイアログを開いたままにできます）。 |
| `OnResize(handler: callable(DialogEvent)) -> None` | ダイアログのサイズが変更されたときに呼び出す`handler`を登録します。 |
| `OnEditLostFocus(handler: callable(DialogEvent)) -> None` | 編集フィールドがフォーカスを失ったときに呼び出す`handler`を登録します。 |
| `OnControl(controlID: int, handler: callable(DialogEvent)) -> None` | `handler`を登録します。コントロール`controlID`が変更またはクリックされたときに呼び出されます。 |
| `OnAnyEvent(handler: callable(DialogEvent)) -> None` | TimerとOtherを含むすべてのイベントで、個別のハンドラーより前に呼び出されます。 |
| `GetListBrowserEvent(controlID: int) -> ListBrowserEvent` | リストブラウザの最後のイベントの詳細（そのOnControlハンドラー内で有効）。 |

*配置（Runの前）*

| メソッド | 説明 |
|---|---|
| `SetFirstItem(controlID: int) -> bool` | コントロール`controlID`の最初の項目を設定します。 |
| `SetFirstGroupItem(groupControlID: int, controlID: int) -> bool` | コントロール`controlID`のグループ内の最初の項目を設定します。 |
| `PlaceBelow(referenceControlID: int, controlID: int, indent: int = 0, spacing: int = 0) -> bool` | インデントは標準文字数、間隔は行数（下に配置）または文字数（右に配置）。 |
| `PlaceRight(referenceControlID: int, controlID: int, indent: int = 0, spacing: int = 0) -> bool` | `controlID`を`referenceControlID`の右に配置します。インデントは標準文字数、間隔は行数（下に配置）または文字数（右に配置）。 |
| `BindEdges(controlID: int, isLeft: bool, isRight: bool, isTop: bool, isBottom: bool) -> bool` | サイズ変更可能なダイアログのサイズが変わるときに、ダイアログの辺に追従する辺。 |
| `BindProportional(controlID: int, isLeft: bool, isRight: bool, isTop: bool, isBottom: bool) -> bool` | `BindEdges`と同様ですが、サイズ変更可能なダイアログのサイズが変わるときに、`controlID`の選択された辺が比例して移動します。 |
| `AlignLeft(controlID: int, alignmentGroupID: int, isResizing: bool = False) -> bool` | controlIDを、別のコントロールではなく、指定した辺の整列グループに割り当てます。同じalignmentGroupIDを持つコントロールは、対応する辺を互いに揃えます。alignmentGroupIDを持つコントロールやグループボックスが存在する必要はありません。符号付き16ビットの正のIDを選択してください。isResizingが`False`の場合はコントロールを移動し、`True`の場合は揃えを満たすようにサイズを変更します。 |
| `AlignRight(controlID: int, alignmentGroupID: int, isResizing: bool = False) -> bool` | `controlID`の右辺を、整列グループ`alignmentGroupID`（コントロールではなく整列用の識別子）の他のメンバーに揃えます。 |
| `AlignBottom(controlID: int, alignmentGroupID: int, isResizing: bool = False) -> bool` | `controlID`の下辺を、整列グループ`alignmentGroupID`（コントロールではなく整列用の識別子）の他のメンバーに揃えます。 |
| `SetControlSize(controlID: int, widthInPixels: int, heightInPixels: int) -> bool` | コントロール`controlID`のサイズを設定します。 |

*ダイアログ*

| メソッド | 説明 |
|---|---|
| `SetDialogSize(size: DialogSize) -> bool` | ダイアログのサイズを設定します。 |
| `GetDialogSize() -> DialogSize \| None` | ダイアログのサイズを返します。 |
| `SetDialogPosition(left: int, top: int) -> bool` | ダイアログの位置を設定します。 |

*コントロールの作成（Runの前）*

| メソッド | 説明 |
|---|---|
| `AddStaticText(controlID: int, text: str, width: int = -1, style: StaticTextStyle = StaticTextStyle.Regular) -> bool` | 固定テキストを追加します（`width`は文字数、-1 = テキストに合わせる）。スタイルは`style`です。 |
| `AddCenteredStaticText(controlID: int, text: str, width: int = -1) -> bool` | 中央揃えの固定テキストを追加します（`width`は文字数、-1 = テキストに合わせる）。 |
| `AddRightStaticText(controlID: int, text: str, width: int = -1) -> bool` | 右揃えの固定テキストを追加します（`width`は文字数、-1 = テキストに合わせる）。 |
| `AddEditText(controlID: int, text: str = '', width: int = 20, heightInLines: int = 1) -> bool` | 初期値が`text`のテキストフィールドを追加します（`width`は文字数、複数行フィールドの場合は`heightInLines` > 1）。 |
| `AddEditInteger(controlID: int, value: int = 0, width: int = 10) -> bool` | 初期値が`value`の整数フィールドを追加します。 |
| `AddEditReal(controlID: int, value: float = 0.0, type: EditRealType = EditRealType.Real, width: int = 10) -> bool` | 初期値が`value`の実数フィールドを追加します。`type`で通常の数値、寸法、角度などを選択します。 |
| `AddEditPassword(controlID: int, width: int = 20) -> bool` | パスワードフィールドを追加します（テキストは非表示）。 |
| `AddSearchBox(controlID: int, prompt: str = '', width: int = 20) -> bool` | 空の場合に`prompt`を表示する検索ボックスを追加します。 |
| `AddPushButton(controlID: int, text: str) -> bool` | `text`をラベルとするプッシュボタンを追加します。 |
| `AddCheckBox(controlID: int, text: str) -> bool` | `text`をラベルとするチェックボックスを追加します。 |
| `AddThreeStateCheckBox(controlID: int, text: str) -> bool` | 未確定状態も持つチェックボックスを追加します。 |
| `AddRadioButton(controlID: int, text: str) -> bool` | `text`をラベルとするラジオボタンを追加します。 |
| `AddGroupBox(controlID: int, text: str = '', hasFrame: bool = True) -> bool` | `text`をタイトルとするグループボックス（他のコントロールのコンテナ）を、枠付きまたは枠なしで追加します。 |
| `AddCheckBoxGroupBox(controlID: int, text: str, hasFrame: bool = True) -> bool` | タイトルにチェックボックスを持つグループボックスを追加します。チェックボックスによって内容が有効になります。 |
| `AddRadioButtonGroupBox(controlID: int, text: str, hasFrame: bool = True) -> bool` | タイトルにラジオボタンを持つグループボックスを追加します。 |
| `AddPullDownMenu(controlID: int, width: int = 20) -> bool` | プルダウンメニューを追加します（`AddChoice` / `SetChoices`で項目を設定）。 |
| `AddListBox(controlID: int, width: int = 20, heightInLines: int = 8, isMultiSelect: bool = False) -> bool` | リストボックスを追加します（複数選択には`isMultiSelect`を使用）。 |
| `AddListBrowser(controlID: int, width: int = 40, heightInLines: int = 10) -> bool` | リストブラウザを追加します（列を持つ表。リストブラウザの関数を参照）。 |
| `AddTreeControl(controlID: int, width: int = 40, heightInLines: int = 10) -> bool` | ツリーコントロールを追加します（ツリーの関数を参照）。 |
| `AddTabControl(controlID: int) -> bool` | タブコントロールを追加します。ペインは`AddTabPane`で追加します。 |
| `AddTabPane(tabControlID: int, paneControlID: int) -> bool` | グループボックスpaneControlIDを、タブコントロールのペインとして追加します（そのテキストがタブラベルになります）。 |
| `AddSwapControl(controlID: int) -> bool` | 切り替えコントロール（一度に一つのペインを表示）を追加します。ペインは`AddSwapPane`で追加します。 |
| `AddSwapPane(swapControlID: int, paneControlID: int) -> bool` | グループボックスpaneControlIDを、切り替えコントロールのペインとして追加します。 |
| `AddSeparator(controlID: int, widthInPixels: int = 0) -> bool` | 水平の区切り線を追加します（`widthInPixels`が0 = デフォルトの幅）。 |
| `AddColorPopup(controlID: int, width: int = -1) -> bool` | 色のポップアップ（ファイルのカラーパレット）を追加します。 |
| `AddPatternPopup(controlID: int) -> bool` | 模様のポップアップを追加します。 |
| `AddLineWeightPopup(controlID: int) -> bool` | 線の太さのポップアップを追加します。 |
| `AddClassPullDown(controlID: int, width: int = 30, isShowingDefaultItems: bool = True) -> bool` | ファイルのクラスを一覧表示するプルダウンを追加します（`isShowingDefaultItems`の場合はデフォルト項目を含む）。 |
| `AddLayerPullDown(controlID: int, width: int = 30, isShowingDefaultItems: bool = True) -> bool` | ファイルのレイヤを一覧表示するプルダウンを追加します（`isShowingDefaultItems`の場合はデフォルト項目を含む）。 |
| `AddColorButton(controlID: int, color: ColorRGB = ColorRGB()) -> bool` | システムのカラーピッカーを開くプッシュボタン。選択した色は`DialogEvent.fData`で通知されます。 |
| `AddSlider(controlID: int, maximum: int = 100) -> bool` | 0から`maximum`までの範囲のスライダーを追加します。 |
| `AddImage(controlID: int, widthInPixels: int, heightInPixels: int, imageSpecifier: str) -> bool` | ImageSpecifier："Vectorworks/Images/Name.png"などのリソース画像のパス。 |
| `HasControl(controlID: int) -> bool` | IDが`controlID`のコントロールが追加されている場合はTrue。 |

*任意のコントロール*

| メソッド | 説明 |
|---|---|
| `Enable(controlID: int, isEnabled: bool = True) -> bool` | コントロール`controlID`を有効または無効にします。 |
| `Show(controlID: int, isVisible: bool = True) -> bool` | コントロール`controlID`を表示または非表示にします。 |
| `IsEnabled(controlID: int) -> bool \| None` | コントロール`controlID`が有効な場合はTrue。 |
| `IsVisible(controlID: int) -> bool \| None` | コントロール`controlID`が表示されている場合はTrue。 |
| `SetFocus(controlID: int) -> bool` | コントロール`controlID`にフォーカスを設定します。 |
| `SetHelpText(controlID: int, helpText: str) -> bool` | コントロール`controlID`のヘルプテキストを設定します。 |
| `SetToolTip(controlID: int, toolTip: str, subToolTip: str = '') -> bool` | コントロール`controlID`のツールチップを設定します。 |
| `SetIndeterminate(controlID: int, isIndeterminate: bool = True) -> bool` | コントロール`controlID`の未確定状態を設定します。 |

*テキスト：固定テキスト、編集フィールド、ボタン、チェックボックス、グループボックス*

| メソッド | 説明 |
|---|---|
| `SetText(controlID: int, text: str) -> bool` | コントロール`controlID`のテキストを設定します。 |
| `GetText(controlID: int) -> str \| None` | コントロール`controlID`のテキストを返します。 |
| `SetTextEditable(controlID: int, isEditable: bool) -> bool` | コントロール`controlID`のテキストを編集可能にするかどうかを設定します。 |
| `SelectAllText(controlID: int) -> bool` | 編集フィールド`controlID`のテキスト全体を選択します。 |
| `SetTextSelection(controlID: int, start: int, end: int) -> bool` | コントロール`controlID`のテキスト選択範囲を設定します。 |
| `SetStaticTextStyle(controlID: int, style: StaticTextStyle) -> bool` | コントロール`controlID`の固定テキストのスタイルを設定します。 |
| `SetStaticTextColor(controlID: int, color: ColorRGB) -> bool` | コントロール`controlID`の固定テキストの色を設定します。 |

*チェックボックス、ラジオボタン、チェックボックス／ラジオグループボックス*

| メソッド | 説明 |
|---|---|
| `SetBool(controlID: int, value: bool) -> bool` | コントロール`controlID`のブール値を設定します。 |
| `GetBool(controlID: int) -> bool \| None` | コントロール`controlID`の*ブール値*がオンかどうか。 |
| `SetCheckState(controlID: int, state: CheckState) -> bool` | コントロール`controlID`のチェック状態を設定します。 |
| `GetCheckState(controlID: int) -> CheckState \| None` | コントロール`controlID`のチェック状態を返します。 |

*数値*

| メソッド | 説明 |
|---|---|
| `SetInteger(controlID: int, value: int) -> bool` | コントロール`controlID`の整数値を設定します。 |
| `GetInteger(controlID: int) -> int \| None` | コントロール`controlID`の整数値を返します。 |
| `SetReal(controlID: int, value: float) -> bool` | 長さと座標はワールド単位、角度は度単位です（型はAddEditRealに指定したもの）。 |
| `GetReal(controlID: int) -> float \| None` | コントロール`controlID`の実数値を返します。長さと座標はワールド単位、角度は度単位です（型はAddEditRealに指定したもの）。 |

*選択肢：プルダウンメニュー、リストボックス、クラス／レイヤのプルダウン*

| メソッド | 説明 |
|---|---|
| `AddChoice(controlID: int, text: str, index: int = -1) -> bool` | インデックス-1は末尾に追加します。 |
| `SetChoices(controlID: int, choices: list[str]) -> bool` | コントロール`controlID`の選択肢を設定します。 |
| `RemoveChoice(controlID: int, index: int) -> bool` | プルダウンメニューまたはリストボックスの`index`の選択肢を削除します。 |
| `RemoveAllChoices(controlID: int) -> bool` | プルダウンメニューまたはリストボックスのすべての選択肢を削除します。 |
| `GetChoiceCount(controlID: int) -> int \| None` | コントロール`controlID`の選択肢の項目数。 |
| `GetChoiceText(controlID: int, index: int) -> str \| None` | `controlID`、`index`に対応する選択肢のテキストを返します。 |
| `FindChoice(controlID: int, text: str) -> int \| None` | テキストが`text`の選択肢のインデックス。存在しない場合は`None`。 |
| `SelectChoice(controlID: int, index: int, isSelected: bool = True) -> bool` | 選択肢を選択します（`isSelected=False`の場合は選択解除）。対象は`index`の選択肢です。 |
| `SelectChoiceByText(controlID: int, text: str) -> bool` | テキストが`text`の選択肢を選択します。 |
| `GetSelectedChoice(controlID: int) -> int \| None` | 選択されている最初のインデックス。何も選択されていない場合は-1。 |
| `GetSelectedChoiceText(controlID: int) -> str \| None` | コントロール`controlID`の選択された選択肢のテキストを返します。 |
| `GetSelectedChoices(controlID: int) -> list[int] \| None` | 複数選択リストボックスで選択されているすべてのインデックス。 |

*属性コントロール*

| メソッド | 説明 |
|---|---|
| `SetColorButton(controlID: int, color: ColorRGB) -> bool` | コントロール`controlID`のカラーボタンを設定します。 |
| `GetColorButton(controlID: int) -> ColorRGB \| None` | コントロール`controlID`のカラーボタンを返します。 |
| `SetColorIndex(controlID: int, colorIndex: int) -> bool` | ファイルのカラーテーブルのインデックス（色のポップアップ）。 |
| `GetColorIndex(controlID: int) -> int \| None` | コントロール`controlID`のカラーインデックスを返します。ファイルのカラーテーブルのインデックスです（色のポップアップ）。 |

*模様のポップアップ*

| メソッド | 説明 |
|---|---|
| `SetPatternIndex(controlID: int, patternIndex: int) -> bool` | 模様のインデックス（0はなし、1は背景、2は前景など）。 |
| `GetPatternIndex(controlID: int) -> int \| None` | コントロール`controlID`の模様のインデックスを返します。模様のインデックス（0はなし、1は背景、2は前景など）です。 |
| `SetLineWeight(controlID: int, lineWeight: int) -> bool` | 線の太さのポップアップ。ミル単位。 |
| `GetLineWeight(controlID: int) -> int \| None` | コントロール`controlID`の線の太さを返します。線の太さのポップアップで、ミル単位です。 |

*スライダーとイメージ*

| メソッド | 説明 |
|---|---|
| `SetSliderValue(controlID: int, value: int) -> bool` | コントロール`controlID`のスライダー値を設定します。 |
| `GetSliderValue(controlID: int) -> int \| None` | コントロール`controlID`のスライダー値を返します。 |
| `SetSliderLiveUpdate(controlID: int, isLive: bool) -> bool` | コントロール`controlID`のスライダーのリアルタイム更新を設定します。 |
| `SetSliderTickMarks(controlID: int, count: int) -> bool` | コントロール`controlID`のスライダーの目盛りを設定します。 |
| `SetImage(controlID: int, imageSpecifier: str) -> bool` | コントロール`controlID`のイメージを設定します。 |

*タブコントロールと切り替えコントロール*

| メソッド | 説明 |
|---|---|
| `ShowTabPane(tabControlID: int, paneControlID: int) -> bool` | ペイン`paneControlID`を、タブコントロール`tabControlID`の最前面に表示します。 |
| `ShowSwapPane(swapControlID: int, paneControlID: int) -> bool` | ペイン`paneControlID`を、切り替えコントロール`swapControlID`で表示します。 |
| `GetActivePane(controlID: int) -> int \| None` | 表示されているペインのグループボックスのコントロールID。 |

*リストブラウザ*

| メソッド | 説明 |
|---|---|
| `AddListBrowserColumn(controlID: int, header: str, widthInPixels: int = 100, column: int = -1) -> bool` | 列-1は末尾に追加します。幅はピクセル単位です。コントロールがリストブラウザでない場合は`False`を返します。 |
| `RemoveListBrowserColumn(controlID: int, column: int) -> bool` | リストブラウザの列`column`を削除します。 |
| `GetListBrowserColumnCount(controlID: int) -> int \| None` | コントロール`controlID`のリストブラウザの列項目数。 |
| `SetListBrowserColumnWidth(controlID: int, column: int, widthInPixels: int) -> bool` | コントロール`controlID`のリストブラウザの列幅を設定します。 |
| `SetListBrowserColumnControl(controlID: int, column: int, controlType: ListBrowserControlType) -> bool` | コントロール`controlID`のリストブラウザの列コントロールを設定します。 |
| `SetListBrowserColumnDisplay(controlID: int, column: int, itemDisplay: ListBrowserDisplayType, editDisplay: ListBrowserDisplayType = ListBrowserDisplayType.TextOnly) -> bool` | コントロール`controlID`のリストブラウザの列表示を設定します。 |
| `AddListBrowserColumnChoice(controlID: int, column: int, text: str, imageOn: int = -1, imageOff: int = -1, data: int = 0) -> bool` | MultiState / SingleInstance / Radioのセルが取ることのできる値。失敗した場合は`False`を返します。 |
| `SetListBrowserCellChoice(controlID: int, row: int, column: int, choiceIndex: int) -> bool` | AddListBrowserColumnChoiceで追加した値の一つをセルに設定します。 |
| `AddListBrowserRow(controlID: int, text: str, row: int = -1) -> bool` | 行-1は末尾に追加します。textは最初の列のテキストです。 |
| `AddListBrowserRowCells(controlID: int, cells: list[str]) -> bool` | 列ごとに一つのテキストを持つ行を末尾に追加します。 |
| `RemoveListBrowserRow(controlID: int, row: int) -> bool` | リストブラウザの行`row`を削除します。 |
| `RemoveAllListBrowserRows(controlID: int) -> bool` | リストブラウザのすべての行を削除します。 |
| `GetListBrowserRowCount(controlID: int) -> int \| None` | コントロール`controlID`のリストブラウザの行項目数。 |
| `SetListBrowserCell(controlID: int, row: int, column: int, text: str, imageIndex: int = -1) -> bool` | コントロール`controlID`のリストブラウザのセルを設定します。 |
| `GetListBrowserCell(controlID: int, row: int, column: int) -> str \| None` | `controlID`、`row`、`column`に対応するリストブラウザのセルを返します。 |
| `SetListBrowserCellData(controlID: int, row: int, column: int, data: int) -> bool` | コントロール`controlID`のリストブラウザのセルデータを設定します。 |
| `GetListBrowserCellData(controlID: int, row: int, column: int) -> int \| None` | `controlID`、`row`、`column`に対応するリストブラウザのセルデータを返します。 |
| `SetListBrowserCellCheckState(controlID: int, row: int, column: int, state: CheckState) -> bool` | コントロール`controlID`のリストブラウザのセルのチェック状態を設定します。 |
| `GetListBrowserCellCheckState(controlID: int, row: int, column: int) -> CheckState \| None` | `controlID`、`row`、`column`に対応するリストブラウザのセルのチェック状態を返します。 |
| `SetListBrowserCellTextColor(controlID: int, row: int, column: int, color: ColorRGB) -> bool` | コントロール`controlID`のリストブラウザのセルの文字色を設定します。 |
| `SetListBrowserCellReadOnly(controlID: int, row: int, column: int, isReadOnly: bool = True) -> bool` | コントロール`controlID`のリストブラウザのセルの読み取り専用設定を行います。 |
| `SetListBrowserReadOnly(controlID: int, isReadOnly: bool = True) -> bool` | コントロール`controlID`のリストブラウザの読み取り専用設定を行います。 |
| `SelectListBrowserRows(controlID: int, firstRow: int, lastRow: int, isSelected: bool = True) -> bool` | 行`firstRow` .. `lastRow`を選択（または選択解除）します。 |
| `IsListBrowserRowSelected(controlID: int, row: int) -> bool \| None` | リストブラウザの行`row`が選択されている場合はTrue。 |
| `GetListBrowserSelectedRows(controlID: int) -> list[int] \| None` | コントロール`controlID`のリストブラウザで選択されている行を返します。 |
| `EnableListBrowserSorting(controlID: int, isEnabled: bool = True) -> bool` | 列見出しのクリックによる行の並べ替えをユーザーに許可します。 |
| `SetListBrowserSortColumn(controlID: int, column: int, isAscending: bool = True) -> bool` | コントロール`controlID`のリストブラウザの並べ替え列を設定します。 |
| `EnableListBrowserSingleSelection(controlID: int, isEnabled: bool = True) -> bool` | リストブラウザで選択できる行を一つに制限します。 |
| `EnableListBrowserDragAndDrop(controlID: int, isEnabled: bool = True) -> bool` | ドラッグ＆ドロップによる行の並べ替えをユーザーに許可します。 |
| `ShowListBrowserHeader(controlID: int, isVisible: bool = True) -> bool` | 列見出し行を表示または非表示にします。 |
| `EnsureListBrowserRowVisible(controlID: int, row: int) -> bool` | 行`row`が表示されるようにリストブラウザをスクロールします。 |
| `EnableListBrowserUpdates(controlID: int, isEnabled: bool) -> bool` | 多数の行を変更する間、再描画を一時停止します。再開するには`True`を指定して再度呼び出し、RefreshListBrowserも呼び出してください。 |
| `RefreshListBrowser(controlID: int) -> bool` | リストブラウザを再描画します（`EnableListBrowserUpdates`で更新を一時停止した後）。 |

*ツリーコントロール*

| メソッド | 説明 |
|---|---|
| `AddTreeItem(controlID: int, text: str, parentID: int = -1) -> int \| None` | parentIDの下に項目を末尾追加します（-1 = ルート）。新しい項目IDを返します。ダイアログが実行中でない場合は`None`を返します（ツリー項目を追加できるのはSetupハンドラー以降のみ）。 |
| `RemoveTreeItem(controlID: int, itemID: int) -> bool` | ツリー項目`itemID`とその子を削除します。 |
| `RemoveAllTreeItems(controlID: int) -> bool` | すべてのツリー項目を削除します。 |
| `GetTreeItemText(controlID: int, itemID: int) -> str \| None` | `controlID`、`itemID`に対応するツリー項目のテキストを返します。 |
| `GetTreeItemParent(controlID: int, itemID: int) -> int \| None` | `controlID`、`itemID`に対応するツリー項目の親を返します。 |
| `GetTreeItemChildren(controlID: int, itemID: int) -> list[int] \| None` | `controlID`、`itemID`に対応するツリー項目の子を返します。 |
| `SetTreeItemData(controlID: int, itemID: int, data: int) -> bool` | コントロール`controlID`のツリー項目のデータを設定します。 |
| `GetTreeItemData(controlID: int, itemID: int) -> int \| None` | `controlID`、`itemID`に対応するツリー項目のデータを返します。 |
| `SetTreeItemCheckState(controlID: int, itemID: int, state: CheckState, isClickable: bool = True) -> bool` | コントロール`controlID`のツリー項目のチェック状態を設定します。 |
| `GetTreeItemCheckState(controlID: int, itemID: int) -> CheckState \| None` | `controlID`、`itemID`に対応するツリー項目のチェック状態を返します。 |
| `ExpandTreeItem(controlID: int, itemID: int, isExpanded: bool = True) -> bool` | ツリー項目を展開します（`isExpanded=False`の場合は折りたたみ）。対象は`itemID`です。 |
| `IsTreeItemExpanded(controlID: int, itemID: int) -> bool \| None` | ツリー項目`itemID`が展開されている場合はTrue。 |
| `SelectTreeItem(controlID: int, itemID: int) -> bool` | ツリー項目`itemID`を選択します。 |
| `GetSelectedTreeItem(controlID: int) -> int \| None` | 何も選択されていない場合は-1。 |
| `GetSelectedTreeItems(controlID: int) -> list[int] \| None` | コントロール`controlID`の選択されているツリー項目を返します。 |
| `EnableTreeMultiSelection(controlID: int, isEnabled: bool = True) -> bool` | 複数のツリー項目の選択を許可します。 |

<a id="enumerations"></a>

## 列挙型

### DialogResult

> **完全修飾名:** `api.DialogResult` · **種類:** `IntEnum`

ダイアログまたはアラートが閉じられた方法。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` | ダイアログを表示できませんでした。 |
| `Ok` | `1` | デフォルト（OK）ボタン。 |
| `Cancel` | `2` | キャンセルボタン、Escape、または閉じるボックス。 |
| `ButtonA` | `3` | 質問アラートのカスタムボタンA。 |
| `ButtonB` | `4` | 質問アラートのカスタムボタンB。 |

### AlertButton

> **完全修飾名:** `api.AlertButton` · **種類:** `IntEnum`

質問アラートのデフォルトボタン。

| メンバー | 値 | 説明 |
|---|---|---|
| `Cancel` | `0` |  |
| `Ok` | `1` |  |
| `ButtonA` | `2` |  |
| `ButtonB` | `3` |  |

### EditRealType

> **完全修飾名:** `api.EditRealType` · **種類:** `IntEnum`

実数編集フィールドに表示する値の種類。長さと座標はワールド単位（mm）で渡します。フィールドはファイルの単位で表示および解析します。

| メンバー | 値 | 説明 |
|---|---|---|
| `Real` | `1` | 通常の数値。 |
| `Angle` | `2` | 度単位の角度。 |
| `Dimension` | `3` | ワールド単位の長さ。 |
| `CoordinateX` | `4` | X座標（ユーザー原点を考慮）。 |
| `CoordinateY` | `5` | Y座標（ユーザー原点を考慮）。 |

### StaticTextStyle

> **完全修飾名:** `api.StaticTextStyle` · **種類:** `IntEnum`

固定テキストのフォントスタイル。

| メンバー | 値 | 説明 |
|---|---|---|
| `Regular` | `0` |  |
| `Caption` | `1` |  |
| `Bold` | `2` |  |
| `Reduced` | `3` | 小さいシステムフォント（macOS）。Windowsでは通常のサイズ。 |

### CheckState

> **完全修飾名:** `api.CheckState` · **種類:** `IntEnum`

三状態チェックボックス、リストブラウザのセル、またはツリー項目のチェックボックスの状態。

| メンバー | 値 | 説明 |
|---|---|---|
| `Off` | `0` |  |
| `On` | `1` |  |
| `Mixed` | `2` |  |

### DialogEventType

> **完全修飾名:** `api.DialogEventType` · **種類:** `IntEnum`

ダイアログイベントの種類（DialogEventを参照）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Setup` | `0` | ダイアログが表示される直前。ここでコントロールを初期化します。 |
| `Setdown` | `1` | ダイアログが破棄される直前。 |
| `Ok` | `2` | OK（デフォルト）ボタンが押されました。開いたままにするには`LayoutDialog.CancelClose`を呼び出します。 |
| `Cancel` | `3` | キャンセルボタンが押されました。開いたままにするには`LayoutDialog.CancelClose`を呼び出します。 |
| `Control` | `4` | コントロールが変更またはクリックされました（fControlID、fData）。 |
| `Resize` | `5` | ユーザーがダイアログのサイズを変更しました。 |
| `Timer` | `6` | タイマーの通知。 |
| `EditLostFocus` | `7` | 編集フィールドがキーボードフォーカスを失いました。 |
| `Other` | `8` | その他のレイアウトマネージャメッセージ（fDataが生のメッセージコードを保持）。 |

### ListBrowserControlType

> **完全修飾名:** `api.ListBrowserControlType` · **種類:** `IntEnum`

リストブラウザの列の動作。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `1` | 通常のテキストまたは画像のセル。 |
| `Radio` | `2` | 列ごとに一つのチェックされたセル。 |
| `MultiState` | `3` | クリックすると列のデータ項目を順に切り替えます。 |
| `SingleInstance` | `4` | クリックするとセルを列のデータ項目0と1の間で切り替えます。 |
| `NoClick` | `5` | セルはクリックに反応しません。 |
| `Number` | `6` | 編集可能な数値セル。 |
| `MultipleImages` | `7` | セルごとに複数の画像。 |
| `DiscTriangle` | `8` | 展開／折りたたみの三角形（階層化された行）。 |

### ListBrowserDisplayType

> **完全修飾名:** `api.ListBrowserDisplayType` · **種類:** `IntEnum`

リストブラウザの列に表示する内容。

| メンバー | 値 | 説明 |
|---|---|---|
| `ImageOnly` | `1` |  |
| `TextOnly` | `2` |  |
| `ImageAndText` | `3` |  |

### ListBrowserEventType

> **完全修飾名:** `api.ListBrowserEventType` · **種類:** `IntEnum`

リストブラウザで発生した内容（`LayoutDialog.GetListBrowserEvent`を参照）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Unknown` | `0` |  |
| `DataChangeClick` | `1` |  |
| `DataChangeAllClick` | `2` |  |
| `SelectionChangeClick` | `3` |  |
| `DoubleClick` | `4` |  |
| `DeleteKeyPressed` | `5` |  |
| `UpKey` | `6` |  |
| `DownKey` | `7` |  |
| `AlphaNumericKey` | `8` |  |
| `SortOccurred` | `9` |  |
| `SelectionMultChangeClick` | `10` |  |
| `EnterKey` | `11` |  |
| `DataChangeRecursiveClick` | `12` |  |
| `DoubleAllClick` | `13` |  |
| `DoubleRecursiveClick` | `14` |  |
| `ReceivingDragAndDrop` | `15` |  |
| `DragAndDrop` | `16` |  |

---

[一覧に戻る](README.md) · [先頭に戻る](#uilayoutcreate--alerts-standard-dialogs-and-layout-dialogs)
