[English](../../MCP/v2027.2/ToolAccess.md) • [Deutsch](../../MCP.de/v2027.2/ToolAccess.md) • **日本語**

# ToolAccess — 対話型ツール

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

ツールパレットの対話型Vectorworksツールを、ユーザーと同じように操作するツールです: ツールをアクティブにし、モードを設定し、図面内をクリックします。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [InteractiveTools](#interactivetools)
  - [getTools](#gettools)
  - [getTool](#gettool)
  - [getActiveTool](#getactivetool)
  - [activateTool](#activatetool)
  - [getToolModes](#gettoolmodes)
  - [setToolMode](#settoolmode)
  - [setToolModes](#settoolmodes)
  - [sendToolPointer](#sendtoolpointer)
  - [sendToolAction](#sendtoolaction)
  - [convertToolCoordinates](#converttoolcoordinates)

<a id="overview"></a>

## 概要

このフォルダには1つのツールグループがあり、合計10個のツールを提供します。

| グループ | グループID | 初期状態で有効 | 安全性レベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [InteractiveTools](#interactivetools) | `interactivetools` | いいえ | 高 | 10 | ツールパレットの対話型Vectorworksツールを、ユーザーと同じように操作します。 |

## InteractiveTools

> **グループ:** `InteractiveTools` · **グループID:** `interactivetools` · **初期状態で有効:** いいえ · **安全性レベル:** 高 · **ツール数:** 10

**ツールパレットの対話型Vectorworksツールを、ユーザーと同じように操作します。**

対話型のVectorworksツール（ツールパレットの作図ツールと編集ツール: 四角形、曲線、壁、ドア、セレクション、変形、アイドロッパなど）を、ユーザーとまったく同じように使用します: ツールを探してアクティブにし、ツールバー（モードバー）でモードを設定してから、図面内でクリック、ダブルクリック、ドラッグし、操作を完了またはキャンセルします。他のグループの専用の作成／編集ツールで対応できる場合は、そちらを優先してください。このグループは、直接のAPIがないツール（プラグインツール、特殊な編集ツール）や、ユーザーがツールの操作を求めた場合に使用します。

ワークフロー:

1. getToolsに`search`（とフィルタ`activatable`）を指定してツールを探します。ツールは`universalName`で識別します（組み込みツールは`-207`などの負の数を使用し、英語の`name`も受け付けます）。getToolは、定義されたツールバーボタンと共に1つのツールを返します。
2. activateToolでツールをアクティブにし（モードを設定することも可能）、現在のツールバー、操作案内（`helpMessage`）、ツールポイントを返します。
3. モード: ツールバーには最大8個のツールバーボタンのグループがあります（ラジオボタン、プッシュボタン、トグル、プルダウン、編集フィールド、リソースポップアップ、検索可能なプルダウン、コンボボックス）。モードは0始まりの`modeIndex`、または`modeName`（ラベルか選択肢名のいずれか）で指定します。setToolModesは複数のモードをテキスト値で設定し、setToolModeは型別のすべての操作を提供します。変更後にツールバーを作り直すツールもあるため、古いインデックスを再利用せず、モードを読み直してください（getToolModes）。設定ボタンを押すとモーダルダイアログが開きます。
4. sendToolPointerで図面内の点をクリックします。`model`空間では点はワールド単位で、スナップなしで正確に適用されます。{ x, y }はレイヤプレーン上の点、{ x, y, z }は3Dの点です。`view`空間では点はアクティブペイン内のピクセル座標で、スマートカーソルのスナップを含め、実際のクリックと同じように動作します。カーソルの下のオブジェクトを取得するツール（セレクション、変形、アイドロッパなど）では、その点がペイン内に表示されている必要があります。convertToolCoordinatesで確認してください。通常、1回のクリックでツールポイントが1つ追加されます。2点ツール（四角形、直線）はクリック-クリック描画モードでは2回のクリックが必要で、複数点ツール（曲線、壁、多角形）は`finish`またはdoubleClickで完了します。
5. sendToolActionで完了（Return）、キャンセル、最後の点の削除を行います。ツールを切り替える前に、開始した操作を必ず完了またはキャンセルしてください。

結果は、getActiveTool（`toolPointCount`、`helpMessage`）とObjects／Selectionグループで確認してください。修飾キー（Shift、Alt）はサポートしていません。ツールによる変更は、「MCP: &lt;tool&gt;」としてではなく、そのツール自身がVectorworksの取り消し履歴に記録します。

> **注:** グループのレベル`high`はグループ全体に適用されます。各ツールは独自のレベルを報告します: 5つの読み取り専用ツールは`low`、ユーザーと同じようにツールを操作する5つのツールは`medium`です（下の表を参照）。
>
> **注:** 無効な引数、不明なツールやモード、アクティブにできないツール、および`sendToolPointer`と`sendToolAction`ではアクティブな作図ペインがない場合に、呼び出しは`err`を返します。アクティブツールが入力やモードの変更を受け付けない場合も呼び出しは成功し、そのことを結果で示します（`ok: false`、`allApplied: false`、または`modesApplied: false`）。ツールを操作する5つのツールは`runToolBatch`内では使用できません。サーバーはこれらのツールに取り消しイベントを開かず、ロールバックもしないため、失敗した呼び出しに`rolledBack`キーはありません。

| ツール | 作用 | 安全性 | 概要 |
|---|---|---|---|
| [`getTools`](#gettools) | 読み取り専用 | 低 | Vectorworksのツールを一覧表示します。 |
| [`getTool`](#gettool) | 読み取り専用 | 低 | 定義されたツールバーボタンと共に1つのツールを返します。 |
| [`getActiveTool`](#getactivetool) | 読み取り専用 | 低 | アクティブツールの状態を返します。 |
| [`activateTool`](#activatetool) | 対話操作 | 中 | ツールをアクティブにします。 |
| [`getToolModes`](#gettoolmodes) | 読み取り専用 | 低 | アクティブツールの現在のツールバーを読み取ります。 |
| [`setToolMode`](#settoolmode) | 対話操作 | 中 | アクティブツールのモードを1つ変更します。 |
| [`setToolModes`](#settoolmodes) | 対話操作 | 中 | アクティブツールのモードを複数設定します。 |
| [`sendToolPointer`](#sendtoolpointer) | 対話操作 | 中 | アクティブツールで図面内をクリック、ダブルクリック、ホバー、ドラッグします。 |
| [`sendToolAction`](#sendtoolaction) | 対話操作 | 中 | アクティブツールの操作を完了またはキャンセルするか、最後の点を削除します。 |
| [`convertToolCoordinates`](#converttoolcoordinates) | 読み取り専用 | 低 | モデル空間とアクティブペインのビューの間で点を変換します。 |

### getTools

Vectorworksのツールを一覧表示します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

Vectorworksのツールを一覧表示します: 組み込みツール、VectorScript／Pythonのプラグインツール、SDKプラグインツール。`filter`: all（デフォルト。作業画面にないものも含む、インストールされているすべてのツール）、activatable（現在アクティブにできるもの）、inWorkspace（ツールパレットに配置されているもの）。`search`はユニバーサル名、名前、表示名、カテゴリを照合します（大文字小文字を区別しません）。`kind`は1種類のツールだけを残します。

各ツールはuniversalName、name、displayName、category、helpText、shortcut、kind、creationType（point|line|box|path2D|path3D|custom|normal）、inWorkspace、canActivate、activeを返します。`includeModeButtons`は、ツールが定義するツールバーボタンを追加します。結果はページ分割されます（`count`は総数、`truncated`は続きがあることを示します）。

> **注:** `kind`は完全一致で比較されます: その他の値ではツールが返らず、エラーにもなりません。`search`で大文字小文字を区別しないのは、A～Zの文字だけです。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `filter` | string |  | 次のいずれか: `all`（デフォルト）, `activatable`, `inWorkspace`。その他の値はエラーです。空の文字列は`all`として扱われます。 |
| `search` | string |  | テキストフィルタ: `universalName`、`name`、`displayName`、`category`のいずれかにこのテキストを含むツールだけを残します（大文字小文字を区別しません）。 |
| `kind` | string |  | 次のいずれか: `internalClassic`, `internalExtension`, `scriptPlugin`, `extensionPlugin`, `unknown`。完全一致で比較されます。 |
| `includeModeButtons` | boolean |  | `true`では、各ツールのツールバーボタンの数（`modeButtonCount`）の代わりに、定義されたツールバーボタン（`modeButtons`）を一覧表示します。デフォルト`false`。 |
| `limit` | integer |  | ページ分割: 返す項目の最大数（1以上、デフォルト100）。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割: スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割: 項目を含めず、件数だけを返します。 |

**結果**

| キー | 説明 |
|---|---|
| `tools` | ページのツール。`displayName`の順に並べ替えられます（大文字小文字を区別しません）。`countOnly`では省略されます。 |
| `count`、`returned`、`offset`、`limit`、`truncated`、`nextOffset` | ページ分割のキー（[ページ分割](Common.md#paging)を参照）。`nextOffset`は`truncated`がtrueの場合にだけ含まれます。 |

各ツールには次のキーがあります:

| キー | 説明 |
|---|---|
| `universalName` | ツールのID。組み込みツールは`-207`などの負の数を使用します。 |
| `name` | 組み込みツールの英語名。プラグインツールでは`universalName`と同じです。 |
| `displayName` | ローカライズされた名前。 |
| `category`、`helpText`、`shortcut` | ツールのカテゴリ、ヘルプテキスト、キーボードショートカット。 |
| `kind` | `internalClassic`（クラシックツールとしてVectorworksに組み込まれたツール）、`internalExtension`（拡張ツールとしてVectorworksに組み込まれたツール）、`scriptPlugin`（VectorScriptまたはPythonのプラグインツール）、`extensionPlugin`（SDKプラグインツール）、または`unknown`。 |
| `creationType` | `point`、`line`、`box`、`path2D`、`path3D`、`custom`、`normal`のいずれか。 |
| `inWorkspace` | ツールが現在の作業画面のツールパレットに配置されている場合は`true`。 |
| `canActivate` | 現在`activateTool`でツールをアクティブにできる場合は`true`: ファイルが開いていて、ツールシステムがそのツールを列挙している場合です。`inWorkspace`には依存しません。 |
| `active` | アクティブツールの場合は`true`。 |
| `modeButtonCount` | ツールが定義するツールバーボタンの数（定義がないツールでは0）。`includeModeButtons`を指定すると`modeButtons`に置き換わります。 |
| `modeButtons` | `includeModeButtons`指定時のみ: `{ name, helpText, kind }`のリスト。`kind`は`radio`、`button`、`preferences`、`check`、`editText`、`pullDown`のいずれかです。 |

エラー: `'filter' must be all, activatable or inWorkspace`、ページ分割のエラー（[結果とエラー](Common.md#results-and-errors)を参照）。

### getTool

定義されたツールバーボタンと共に1つのツールを返します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

`name`（ユニバーサル名、組み込みツールの英語名、またはローカライズされた表示名）で見つかった1つのツールを、ツールが定義するツールバーボタン（name、helpText、kind）と共に返します。定義されたボタンは静的な情報です。現在のツールバーは、アクティブにした後にgetToolModesで読み取ります。

> **注:** `name`は次の優先順で照合されます: 完全に一致する`universalName`（大文字小文字を区別）、次に大文字小文字だけが異なる`universalName`または英語の`name`、最後に大文字小文字だけが異なるローカライズ名または`displayName`。同等に一致するツールが複数ある場合は、アクティブにできるツールが優先されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string | はい | ユニバーサル名、組み込みツールの英語名、またはローカライズされた表示名。 |

**結果**

[`getTools`](#gettools)で説明したキーを持つ1つのツールと、その`modeButtons`。

エラー: `'name' is required`、`no Vectorworks tool matches '<name>' (use getTools with 'search' to find it)`。

### getActiveTool

アクティブツールの状態を返します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

アクティブツールの状態を返します: ツール、現在の操作案内（`helpMessage`）、操作が進行中かどうか、これまでに入力したツールポイント（point2D、point3D、viewPoint）、現在のホバー点、アクティブペインのピクセル単位のサイズ、および`includeModes`がfalseでない限り現在のツールバー。`maxChoices`は、モードごとに一覧表示する選択肢の数を制限します（デフォルト50）。

> **注:** `activeTool`は、スクリプトが点を取得している間など、`getTools`が列挙しない補助ツールである場合があります。アクティブなツールがない場合は`null`です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `includeModes` | boolean |  | `false`では現在のツールバー（`modes`）を省略します。デフォルト`true`。 |
| `maxChoices` | integer |  | モードごとに一覧表示する選択肢の最大数（0以上、デフォルト50）。 |

**結果**

| キー | 説明 |
|---|---|
| `activeTool` | アクティブツールとその`modeButtons`。[`getTools`](#gettools)で説明したキーを持ちます。アクティブなツールがない場合は`null`。 |
| `helpMessage` | ツールの現在の操作案内。 |
| `inProgress` | ツールの操作が進行中かどうか。 |
| `toolPointCount` | これまでに入力したツールポイントの数。 |
| `toolPoints` | ツールポイント。それぞれ`{ point2D: { x, y }, point3D: { x, y, z }, viewPoint: { x, y } }`です。`point3D`はモデルの点、`point2D`はスクリーンプレーン上（2Dツール）またはワーキングプレーン上（3Dツール）の点、`viewPoint`はアクティブペイン内のピクセル単位の位置です。 |
| `currentPoint` | 現在のホバー点（ツールポイントの形式）。取得できる場合のみ。 |
| `viewSize` | アクティブペインのピクセル単位の`{ width, height }`。アクティブペインがある場合のみ。 |
| `modes` | 現在のツールバー: モードのリスト。各モードは[`getToolModes`](#gettoolmodes)で説明したとおりです。`includeModes`がfalseの場合は省略されます。 |

### activateTool

ツールをアクティブにします。

> **作用:** 対話操作 · **安全性:** 中 · **取り消し:** ユーザー入力と同様にVectorworksが記録 · **runToolBatch内:** 不可

**詳細**

`name`（ユニバーサル名、組み込みツールの英語名、または表示名）で指定したツール、または`selectionTool`: trueでデフォルトのセレクションツールをアクティブにします。アクティブにできるのは現在の作業画面にあるツールだけです（getToolsの`canActivate`を参照）。アクティブにした直後にモードを設定することもできます: `modes`は{ modeIndex | modeName, value }の配列（setToolModesと同じ）です。または、`modeIndex`／`modeName`と`choiceIndex`で選択肢を1つ選びます。

新しいアクティブツールの状態を、現在のツールバーと`modesApplied`と共に返します。

> **注:** 確認されるのはツールの`canActivate`で、`inWorkspace`ではありません（[`getTools`](#gettools)を参照）。`selectionTool`がtrueの場合、`name`は無視されます。それ以外の場合、`name`は[`getTool`](#gettool)と同じ方法で照合されます。ツールはアクティブになったがモードを設定できなかった場合も、呼び出しは`modesApplied: false`で成功します。
>
> **注:** `modes`は、`choiceIndex`を伴う`modeIndex`／`modeName`より優先されます。後者は[`setToolMode`](#settoolmode)の`selectChoice`と同じように動作します: 編集フィールドとリソースポップアップでは失敗し（`modesApplied: false`）、これらには`value`を伴う`modes`が必要です。`choiceIndex`がない場合は0として扱われます。`modeName`は`modeIndex`がない場合にだけ使用されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string |  | ユニバーサル名、組み込みツールの英語名、または表示名。 |
| `selectionTool` | boolean |  | `true`ではデフォルトのセレクションツールをアクティブにし、`name`を無視します。デフォルト`false`。 |
| `modes` | array of object |  | アクティブにした直後に順番に設定するモード。[`setToolModes`](#settoolmodes)の`settings`の形式です。`modeIndex`／`modeName`より優先されます。 |
| `modes[].modeIndex` | integer |  | モードの0始まりのインデックス。`modeName`より優先されます。 |
| `modes[].modeName` | string |  | モードのラベル、またはその選択肢名のいずれか。`modeIndex`がない場合にだけ使用されます。 |
| `modes[].value` | string or number or integer or boolean | はい | 新しい値。[`setToolMode`](#settoolmode)の`setValue`の`value`と同じです。`value`のない設定は空のテキストとして適用されます。 |
| `modeIndex` | integer |  | `choiceIndex`で変更する1つのモードの0始まりのインデックス。`modeName`より優先されます。 |
| `modeName` | string |  | モードのラベル、またはその選択肢名のいずれか。`modeIndex`がない場合にだけ使用されます。 |
| `choiceIndex` | integer |  | モード`modeIndex`／`modeName`で選ぶ選択肢。[`setToolMode`](#settoolmode)の`selectChoice`と同じです。デフォルト0。負の値、または数値でない値は0として扱われます。 |
| `maxChoices` | integer |  | モードごとに一覧表示する選択肢の最大数（0以上、デフォルト50）。 |

**結果**

| キー | 説明 |
|---|---|
| `activated` | `true`。ツールをアクティブにできない場合は、代わりにエラーで失敗します。 |
| `modesApplied` | モードが指定されていない場合、またはすべてのモード変更が成功した場合は`true`。それ以外は`false`。 |
| `modeResults` | `modes`指定時のみ: 設定ごとに1項目（[`setToolModes`](#settoolmodes)の`results`の形式）。 |

結果には、[`getActiveTool`](#getactivetool)のキーと現在のツールバー（`modes`）も含まれます。

エラー: `'name' is required (or set 'selectionTool' to true)`、`no Vectorworks tool matches '<name>' (use getTools with 'search' to find it)`、`'<display name>' is not in the current workspace and cannot be activated`（ツールの`canActivate`がfalse）、`'<display name>' could not be activated`、`the Selection tool could not be activated`。

### getToolModes

アクティブツールの現在のツールバーを読み取ります。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

アクティブツールの現在のツールバーを読み取ります。`modeIndex`／`modeName`を指定しない場合は、すべてのモードを返します。各モードはindex、type（radio|button|toggle|pullDown|editText|resourcePopup|searchablePullDown|comboBox）、enabled、label、value（テキストでの現在の値）、choices（name、helpText、image、id）とchoiceCount、selectedChoice、およびトグルではisOnを返します。`maxChoices`は、モードごとに一覧表示する選択肢の数を制限します（デフォルト50）。

> **注:** `modeName`は、モードのラベルまたはその選択肢名のいずれかに一致します（大文字小文字を区別しません）。`modeIndex`は`modeName`より優先されます: ツールバーの範囲外のインデックスはエラーになり、`modeName`には切り替わりません。モードはインデックス0から順に検索され、ラベルまたはいずれかの選択肢名が一致した最初のモードが使用されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `maxChoices` | integer |  | モードごとに一覧表示する選択肢の最大数（0以上、デフォルト50）。 |
| `modeIndex` | integer |  | 返すモードの0始まりのインデックス。`modeName`より優先されます。 |
| `modeName` | string |  | モードのラベル、またはその選択肢名のいずれか。`modeIndex`がない場合にだけ使用されます。 |

**結果**

`modeIndex`と`modeName`を指定しない場合:

| キー | 説明 |
|---|---|
| `modeCount` | ツールバー上のモードの数。 |
| `modes` | すべてのモードのリスト。 |

`modeIndex`または`modeName`を指定した場合、結果はそのモード自体で、`modeCount`と`modes`はありません。各モードには次のキーがあります:

| キー | 説明 |
|---|---|
| `index` | モードの0始まりのインデックス。 |
| `type` | `radio`、`button`、`toggle`、`pullDown`、`editText`、`resourcePopup`、`searchablePullDown`、`comboBox`のいずれか。 |
| `enabled` | モードを変更できるかどうか。 |
| `label` | モードのラベル。 |
| `value` | テキストでの現在の値。 |
| `choiceCount` | モードの選択肢の数。 |
| `choices` | 一覧表示する選択肢。それぞれ`{ index, name }`で、空でない場合は`helpText`、`image`、`id`も持ちます。最大`maxChoices`項目で、編集フィールドとリソースポップアップでは常に空です。 |
| `choicesTruncated` | `choices`の項目数が`choiceCount`より少ない場合は`true`。その場合にだけ含まれます。 |
| `selectedChoice` | 選択されている選択肢のインデックス。モードにある場合にだけ含まれます。 |
| `isOn` | トグルがオンかどうか。トグルの場合にだけ含まれます。 |

エラー: `no mode matches 'modeIndex' / 'modeName' (modeCount is N)`。Nはモードの数です。

### setToolMode

アクティブツールのモードを1つ変更します。

> **作用:** 対話操作 · **安全性:** 中 · **取り消し:** ユーザー入力と同様にVectorworksが記録 · **runToolBatch内:** 不可

**詳細**

`modeIndex`または`modeName`で指定したアクティブツールのモードを1つ、ユーザーがツールバーで行うのとまったく同じように変更します。`action`（デフォルトsetValue）: setValue - モードの種類に応じて解釈される`value`（radio: ボタン名またはインデックス、button: 押す、toggle: on/off/true/false/toggle、pullDown/searchablePullDown: 項目のテキスト、idまたはインデックス、comboBox: 項目または自由なテキスト、editText: テキスト、resourcePopup: リソース名）。selectChoice - 任意の種類のモードで選択肢`choiceIndex`を選ぶ。selectRadio - ラジオボタン`choiceIndex`。pressButton。setToggle - `isOn`。selectItem - `item`（テキストまたはid）または`choiceIndex`でリストの項目を選ぶ。setText - 編集フィールドまたはコンボボックスに`text`を入力。selectResource - リソースポップアップで`resourceName`を選択。

無効なモードは変更できません。`ok`と変更後のモードを返します。

> **注:** idを持つのは検索可能なプルダウンの項目だけです。プルダウンとコンボボックスの項目はテキストで照合されます（大文字小文字を区別しません）。項目のテキストまたはidは番号より先に試されるため、`"1"`はまず`1`という名前の項目を選択します。
>
> **注:** 確認は次の順で行われます: モード、`action`、アクションが必要とする引数。`modeIndex`は`modeName`より優先されます。ツールバーの範囲外のインデックスはエラーになり、`modeName`には切り替わりません。無効なモードや、モードが受け付けない値はエラーではありません: 呼び出しは`ok: false`を返します。
>
> **注:** `selectChoice`は、ラジオボタン、ボタン（`choiceIndex`は無視されます）、トグル（0はオフ、それ以外の数値はオン）、およびプルダウン、検索可能なプルダウン、コンボボックスのリストで動作します。編集フィールドとリソースポップアップでは常に失敗するため、これらには`setText`または`selectResource`を使用してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `action` | string |  | 次のいずれか: `setValue`（デフォルト）, `selectChoice`, `selectRadio`, `pressButton`, `setToggle`, `selectItem`, `setText`, `selectResource`。 |
| `value` | string or number or integer or boolean |  | `setValue`の値（このアクションでは必須）。読み取り方はモードの種類によって異なります。真偽値は`on`または`off`、数値は10進数のテキストとして扱われます。 |
| `choiceIndex` | integer |  | 選択肢の0始まりの番号。`selectChoice`と`selectRadio`では必須です。`selectItem`では`item`がない場合に使用されます。負の値、または数値でない値は0として扱われます。 |
| `isOn` | boolean |  | `setToggle`では必須。真偽値でない値は`false`として扱われます。 |
| `item` | string |  | 項目のテキスト（大文字小文字を区別しません）、または検索可能なプルダウンの項目のid。`selectItem`用で、`choiceIndex`より優先されます。 |
| `text` | string |  | `setText`では必須。 |
| `resourceName` | string |  | `selectResource`では必須。 |
| `maxChoices` | integer |  | `mode`でモードごとに一覧表示する選択肢の最大数（0以上、デフォルト50）。 |
| `modeIndex` | integer |  | モードの0始まりのインデックス。`modeName`より優先されます。 |
| `modeName` | string |  | モードのラベル、またはその選択肢名のいずれか。`modeIndex`がない場合にだけ使用されます。 |

**アクション**

| アクション | 必要な引数 | 動作 |
|---|---|---|
| `setValue` | `value` | `value`からモードを設定します。下の表を参照してください。 |
| `selectChoice` | `choiceIndex` | 選択肢を選びます。上の2つ目の注を参照してください。 |
| `selectRadio` | `choiceIndex` | この番号のラジオボタンを押します。番号が最後のボタンを超える場合は失敗します。負の値、または数値でない値は0として扱われます。 |
| `pressButton` | なし | ボタンのモードを押します。 |
| `setToggle` | `isOn` | トグルをオンまたはオフにします。既にその状態のトグルはそのままで、呼び出しは`ok: true`を返します。 |
| `selectItem` | `item`または`choiceIndex` | プルダウン、検索可能なプルダウン、コンボボックスのリストの項目を選びます。`item`（テキスト、または検索可能なプルダウンではid）は`choiceIndex`より優先されます。 |
| `setText` | `text` | 編集フィールドまたはコンボボックスにテキストを入力します。 |
| `selectResource` | `resourceName` | リソースポップアップでリソースを選択します。その後ポップアップがそのリソースを表示している場合にだけ、`ok`は`true`です。 |

`setValue`は、モードの種類に応じて`value`を読み取ります:

| モードの種類 | `value` |
|---|---|
| `radio` | 選択肢の名前またはイメージ（大文字小文字を区別しません）、または選択肢の番号。 |
| `button` | 無視されます: ボタンが押されます。 |
| `toggle` | オンは`on`、`true`、`yes`、`1`、オフは`off`、`false`、`no`、`0`。`toggle`はトグルを切り替えます。これらの語は大文字小文字を区別しません。 |
| `pullDown`、`searchablePullDown` | 項目のテキスト（大文字小文字を区別しません）、または検索可能なプルダウンではそのid。それ以外の場合は項目の番号。テキストまたはidが先に試されます。 |
| `comboBox` | 項目のテキスト（大文字小文字を区別しません）。その他のテキストはフィールドに入力されます。 |
| `editText` | 入力するテキスト。 |
| `resourcePopup` | リソースの名前。 |

**結果**

| キー | 説明 |
|---|---|
| `ok` | 変更が適用された場合は`true`。 |
| `modeCount` | ツールバー上のモードの数。 |
| `mode` | 変更後のモード。[`getToolModes`](#gettoolmodes)で説明したキーを持ちます。`maxChoices`が適用されます。 |

エラー: `no mode matches 'modeIndex' / 'modeName' (modeCount is N)`、`unknown 'action'`、`'<argument>' is required for action '<action>'`、`'item' or 'choiceIndex' is required for action 'selectItem'`。

### setToolModes

アクティブツールのモードを複数設定します。

> **作用:** 対話操作 · **安全性:** 中 · **取り消し:** ユーザー入力と同様にVectorworksが記録 · **runToolBatch内:** 不可

**詳細**

アクティブツールの複数のモードを順番に設定します: `settings`は{ modeIndex | modeName, value }の配列で、valueはsetToolModeのsetValueと同じように解釈されます。各設定は`results`（ok、newValue、err）で報告され、いずれかが失敗すると`allApplied`はfalseになります。更新したモードを返します。

> **注:** 失敗があっても、すべての設定が試されます。失敗した設定で呼び出しが失敗することはありません: `results`に示され、`allApplied`が`false`になります。各設定は[`setToolMode`](#settoolmode)と同じ方法でモードを探します: `modeIndex`は`modeName`より優先されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `settings` | array of object | はい | 順番に適用するモードの変更。`{ modeIndex | modeName, value }`の空でない配列。 |
| `settings[].modeIndex` | integer |  | モードの0始まりのインデックス。`modeName`より優先されます。 |
| `settings[].modeName` | string |  | モードのラベル、またはその選択肢名のいずれか。`modeIndex`がない場合にだけ使用されます。 |
| `settings[].value` | string or number or integer or boolean | はい | 新しい値。モードの種類に応じて、[`setToolMode`](#settoolmode)の`setValue`の`value`と同じように読み取られます。このツールは`value`のない設定を拒否しません: 空のテキストとして適用されます。 |
| `maxChoices` | integer |  | `modes`でモードごとに一覧表示する選択肢の最大数（0以上、デフォルト50）。 |

**結果**

| キー | 説明 |
|---|---|
| `allApplied` | すべての設定が適用された場合は`true`。 |
| `results` | 設定ごとに1項目（指定順）。 |
| `modes` | 更新後のツールバー: すべてのモードのリスト。各モードは[`getToolModes`](#gettoolmodes)で説明したとおりです。`maxChoices`が適用されます。 |

`results`の各項目は設定を繰り返し（オブジェクトでない設定は`{ "setting": <the value> }`として示されます）、次のキーを加えます:

| キー | 説明 |
|---|---|
| `ok` | モードが変更された場合は`true`。 |
| `modeIndex` | 見つかったモードの0始まりのインデックス。 |
| `newValue` | 変更後のモードのテキスト値。 |
| `err` | `no mode matches 'modeIndex' / 'modeName'`。モードが見つからなかった場合のみ。この場合`ok`は`false`で、`modeIndex`と`newValue`はありません。 |

エラー: `settings`がない、配列でない、または空の場合は`'settings' must be a non-empty array of { modeIndex | modeName, value }`。

### sendToolPointer

アクティブツールで図面内をクリック、ダブルクリック、ホバー、ドラッグします。

> **作用:** 対話操作 · **安全性:** 中 · **取り消し:** ユーザー入力と同様にVectorworksが記録 · **runToolBatch内:** 不可

**詳細**

ユーザーが図面で行うのと同じように、ポインタでアクティブツールを操作します。`action`: click（デフォルト）、doubleClick、move（ホバーのみ。プレビューを更新）、drag（`from`でマウスボタンを押し、`to`で離す）。`space`: model（デフォルト。ワールド単位、正確な座標、スナップなし。レイヤプレーン上の{ x, y }、または{ x, y, z }）、view（アクティブペイン内のピクセル座標。スナップあり）。1つの`point`または複数の`points`を指定します（順番に送信し、最初の失敗で停止）。`finish`: trueは、送信後にReturnを押して複数点ツールを完了します。

`sent`と、入力後のツールの状態（`toolPointCount`、`toolPoints`、`helpMessage`）を返します。

> **注:** `points`は`point`より優先されます。`drag`では`from`と`to`だけが使われます: 両方が2D（`z`なし）、両方が3D（`z`あり）、または両方がビューの点である必要があります。何かを送信する前にすべての点を読み取るため、読み取れない点があるとエラーになり、何も送信されません。ビューの点は整数のピクセルに丸められ、16ビット（-32768～32767）に収まる必要があります。
>
> **注:** 送信が途中で止まるのは、`view`空間の点がアクティブペインの外にある場合だけです。点に対するツールの応答は報告されません: `sent`は届けられたポインタ入力の数で、ツールが受け付けた点の数ではありません。ツールが何をしたかは、`toolPointCount`と`helpMessage`で確認してください。
>
> **注:** `finish`は、`move`と`drag`を含むすべてのアクションの後に適用され、`sent`が0でもReturnを押します。アクティブペインに表示されていない`model`の点は、ペインの中心に届けられます。点そのものを使うツールには正確なモデルの点が渡されますが、ポインタの下にあるものを取得するツール（セレクション、変形、アイドロッパ）はペインの中心で動作し、エラーは報告されません。点が表示されているかどうかは、[`convertToolCoordinates`](#converttoolcoordinates)の`modelToView`で確認してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `action` | string |  | 次のいずれか: `click`（デフォルト）, `doubleClick`, `move`（ホバーのみ）, `drag`。`drag`は`from`と`to`を使用し、その他のアクションは`point`または`points`を使用します。 |
| `space` | string |  | 次のいずれか: `model`（デフォルト）, `view`。`model`: ワールド単位、正確な座標、スナップは停止。`view`: アクティブペイン内のピクセル座標、実際のクリックと同じスマートカーソルのスナップあり。 |
| `point` | [3D点](Common.md#points) |  | モデル空間: レイヤプレーン上の{ x, y }、または3Dの{ x, y, z }（ワールド単位）。ビュー空間: アクティブな作図ペインの左上隅からのピクセル単位の{ x, y }。`click`、`doubleClick`、`move`で使用されます。`points`を指定した場合は無視されます。 |
| `points` | array of [3D点](Common.md#points) |  | 各項目: モデル空間: レイヤプレーン上の{ x, y }、または3Dの{ x, y, z }（ワールド単位）。ビュー空間: アクティブな作図ペインの左上隅からのピクセル単位の{ x, y }。順番に送信されます。`point`より優先されます。 |
| `from` | [3D点](Common.md#points) |  | モデル空間: レイヤプレーン上の{ x, y }、または3Dの{ x, y, z }（ワールド単位）。ビュー空間: アクティブな作図ペインの左上隅からのピクセル単位の{ x, y }。`drag`のみ: マウスボタンを押す位置。`from`と`to`は同じ種類である必要があります。 |
| `to` | [3D点](Common.md#points) |  | モデル空間: レイヤプレーン上の{ x, y }、または3Dの{ x, y, z }（ワールド単位）。ビュー空間: アクティブな作図ペインの左上隅からのピクセル単位の{ x, y }。`drag`のみ: マウスボタンを離す位置。 |
| `finish` | boolean |  | `true`では、入力後にReturnを押して複数点ツールを完了します。 |

**結果**

入力後のアクティブツールの状態。[`getActiveTool`](#getactivetool)の`modes`以外のキー（`activeTool`、`helpMessage`、`inProgress`、`toolPointCount`、`toolPoints`、`currentPoint`、`viewSize`）に、次のキーが加わります:

| キー | 説明 |
|---|---|
| `sent` | 届けられたポインタ入力の数: `move`、`click`、`doubleClick`では点ごとに1つ、`drag`では1または0。 |
| `ok` | `sent`が0より大きい場合は`true`。 |
| `finished` | `finish`が指定され、Returnキーが処理された場合は`true`。 |

エラー（確認される順）: `there is no active drawing pane to send input to`、`'action' must be move, click, doubleClick or drag`、`'space' must be model or view`、`drag`では`'drag' needs 'from' and 'to' of the same kind (both 2D, both 3D, or both view points)`、その他のアクションでは`'point' or a non-empty 'points' array is required`、または`point <N> must be { x, y } or { x, y, z } in world units`（モデル空間）か`point <N> must be { x, y } in pixels (16 bit)`（ビュー空間）。`<N>`は`points`内の0始まりの位置です。

### sendToolAction

アクティブツールの操作を完了またはキャンセルするか、最後の点を削除します。

> **作用:** 対話操作 · **安全性:** 中 · **取り消し:** ユーザー入力と同様にVectorworksが記録 · **runToolBatch内:** 不可

**詳細**

アクティブツールの操作を制御します: finish（Return。複数点ツールを完了）、cancel（選択内容を変えずに、すべてのツールポイントを削除）、removeLastPoint、または`key`にreturn、escape、backspaceを指定するpressKey（ツールポイントがない状態のescapeは、ユーザーのキー操作と同じように選択も解除します）。`ok`とツールの状態を返します。

> **注:** `finish`はReturnを押します。`cancel`は、ツールポイントがある間のEscapeと同じように、選択内容に触れずにすべてのツールポイントを消去します。`removeLastPoint`は、Backspaceと同じようにツールポイントを1つ削除します。`pressKey`は指定したキーをアクティブな作図ペインに送ります。ツールポイントがない状態の`escape`は、ユーザーのキー操作と同じように選択も解除します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `action` | string | はい | 次のいずれか: `finish`, `cancel`, `removeLastPoint`, `pressKey`。 |
| `key` | string |  | 次のいずれか: `return`, `escape`, `backspace`。`pressKey`で必要です。有効なキーがない場合、そのアクションは`'action' must be ...`のエラーで失敗します。その他のアクションでは無視されます。 |

**結果**

アクション後のアクティブツールの状態。[`getActiveTool`](#getactivetool)の`modes`以外のキーに`ok`が加わります。`ok`はアクションによって異なります:

| アクション | `ok`が`true`になる条件 |
|---|---|
| `finish` | Returnキーが処理された場合。 |
| `cancel` | ツールポイントが残っていない場合。最初からツールポイントがなかった場合も同様です。 |
| `removeLastPoint` | ツールポイントが削除された場合。ツールポイントがない場合は`false`。 |
| `pressKey` | キーが処理された場合。ツールがそのキーで何をしたかは示しません。 |

エラー: `there is no active drawing pane to send input to`、`'action' must be finish, cancel, removeLastPoint or pressKey (with 'key' return, escape or backspace)`。

### convertToolCoordinates

モデル空間とアクティブペインのビューの間で点を変換します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

モデル空間とアクティブペインのビューの間で点を変換します。`direction`のmodelToView: モデルの{ x, y }または{ x, y, z }をピクセル座標に変換し、点がペイン内に表示されていない場合はnull。viewToModel: ピクセル座標をその下にある2Dのモデルの点（2D/平面ビューではレイヤプレーン、それ以外ではスクリーンプレーン）に変換し、ペインの外ではnull。`point`または`points`を指定してください。ペインのサイズ（`viewSize`）も返します。

> **注:** 変換できない点は、その位置に`null`を返します。これはエラーではありません。呼び出しが失敗するのは、`direction`が誤っている場合か、点が指定されていない場合だけです。`points`を指定すると`point`は無視されます。`modelToView`は`{ x, y }`を2Dの点、`{ x, y, z }`を3Dの点として読み取ります。`viewToModel`は常に2Dのモデルの点を返し、`z`は返しません。アクティブな作図ペインがない場合、すべての項目が`null`になり、`viewSize`はありません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `direction` | string | はい | 次のいずれか: `modelToView`（モデルの点をアクティブペインのピクセルに変換）, `viewToModel`（ピクセルをモデルの点に変換）。 |
| `point` | [3D点](Common.md#points) |  | 変換する1つの点。`modelToView`: モデルの点（{ x, y }または{ x, y, z }、ワールド単位）。`viewToModel`: アクティブな作図ペインの左上隅からのピクセル単位の{ x, y }（整数のピクセルに丸められ、-32768～32767の範囲内である必要があります）。`points`を指定した場合は無視されます。 |
| `points` | array of [3D点](Common.md#points) |  | 変換する点。それぞれ`point`の形式です。`point`より優先されます。 |

**結果**

| キー | 説明 |
|---|---|
| `points` | 入力した点ごとに1項目（同じ順）。各項目は`{ x, y }`または`null`です。`modelToView`はピクセル座標を、`viewToModel`はワールド単位の2Dのモデルの点を返します。 |
| `viewSize` | アクティブペインのピクセル単位の`{ width, height }`。アクティブペインがある場合のみ。 |

点を読み取れない場合、変換できない場合（`modelToView`: 点がペインに表示されていない。`viewToModel`: ピクセルがペインの外にある）、またはアクティブな作図ペインがない場合、項目は`null`になります。

エラー: `'direction' must be modelToView or viewToModel`、`'point' or a non-empty 'points' array is required`。
