[English](../../MCP/v2027.2/OIPAccess.md) • [Deutsch](../../MCP.de/v2027.2/OIPAccess.md) • **日本語**

# OIPAccess — オブジェクト情報パレット

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

現在の選択に対するオブジェクト情報パレットを、ユーザーと同じように読み取り、操作するツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [Object Info](#object-info)
  - [getOIPControls](#getoipcontrols)
  - [setOIPValues](#setoipvalues)
  - [pressOIPButton](#pressoipbutton)

<a id="overview"></a>

## 概要

このフォルダには1つのツールグループがあり、合計3個のツールを提供します。

| グループ | グループID | 初期状態で有効 | 安全性レベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [Object Info](#object-info) | `object-info` | いいえ | 中 | 3 | 現在の選択に対するオブジェクト情報パレットを、ユーザーと同じように読み取り、操作します。 |

## Object Info

> **グループ:** `Object Info` · **グループID:** `object-info` · **初期状態で有効:** いいえ · **安全性レベル:** 中 · **ツール数:** 3

**現在の選択に対するオブジェクト情報パレットを、ユーザーと同じように読み取り、操作します。**

オブジェクト情報パレットをユーザーと同じように読み取り、操作します。パレットは現在の選択に対して、形状タブ（クラス、レイヤ、サイズ、プラグインオブジェクトのパラメータなど）、データタブ（レコードやその他の付加データ）、レンダータブ（テクスチャ）を、編集フィールド、チェックボックス、プルダウン、ラジオボタン、ボタンなどのコントロールとして表示します。パレットが表示されている必要はありません。

このグループは、パレットに表示され、専用ツールでは扱えないプロパティ、パレットに表示されるとおりのプラグインオブジェクトのパラメータ（プラグインがそこに追加するコントロールやボタンを含む）、データタブのレコードフィールドとレンダータブのテクスチャに使用するほか、ユーザーがオブジェクト情報パレットの使用を求めた場合に使用します。他のグループの専用ツールで変更できる場合は、そちらを優先してください。たとえば、プラグインのパラメータにはsetObjectParameter（作成時はcreatePluginObjectの`params`）、名前、クラス、変形にはeditObject、線と面にはsetObjectAttributes、テクスチャにはapplyResourceを使用します。これらの呼び出しはそれぞれ1つの取り消しステップ「MCP: &lt;tool&gt;」になり、失敗するとロールバックされ、runToolBatch内で実行できます。

ワークフロー:

1. selectObjects（Selectionグループ）でオブジェクトを選択します。変更は選択全体に適用されます。
2. getOIPControlsで`pane`のコントロールを一覧表示します: shape（デフォルト）、data、render。
3. setOIPValuesで値を設定し、pressOIPButtonでボタンを押します。コントロールは、`label`（そのラベルを持つ最初の表示されているコントロール。大文字小文字を区別せず、末尾の「:」と空白は無視されます）またはgetOIPControlsの`controlId`のどちらか一方だけで指定します。変更のたびにパレットが再構築され、コントロールのIDが変わる可能性があるため、ラベルを優先してください。
4. 変更後は、getOIPControlsでコントロールを読み取り直してください。

値は、ユーザーが入力するように指定します。単位のない数値は、他のグループが使用するワールド単位とラジアンではなく、ファイルの単位（getUnits）として扱われるため、明示するには単位を付けてください（例: "200mm"）。Vectorworksが読み取れないテキストを指定すると警告が表示されることがあり、警告はダイアログと同様にユーザーの操作を待ちます。プラグインオブジェクトは直ちに再生成されます。

取り消し: パレットでの変更は、それぞれVectorworksの独立した取り消しステップになり、その名前はユーザーによる編集と同様にVectorworksが付けます。「MCP: &lt;tool&gt;」にはなりません。setOIPValuesとpressOIPButtonはrunToolBatch内では実行できず、設定が失敗しても、それ以前の設定は元に戻りません。

ダイアログ: ボタンや選択肢は、モーダルダイアログまたは警告を開く場合があります。その場合、呼び出しはユーザーがそれを閉じるまで待機し、その間Vectorworksは他のMCP呼び出しに応答しないため、MCPクライアントがタイムアウトする可能性があります。「...」で終わるボタンのラベルや選択肢名はダイアログを開き（getOIPControlsの`opensDialog`）、`allowDialog`: true（デフォルトfalse）が必要です。ダイアログが開くことと、ユーザーがそこでダイアログを閉じる必要があることを伝えてから指定してください。

| ツール | 作用 | 安全性 | 概要 |
|---|---|---|---|
| [`getOIPControls`](#getoipcontrols) | 読み取り専用 | 低 | オブジェクト情報パレットの1つのタブのコントロールを一覧表示します。 |
| [`setOIPValues`](#setoipvalues) | 対話操作 | 中 | ユーザーと同じように、オブジェクト情報パレットのコントロールを設定します。 |
| [`pressOIPButton`](#pressoipbutton) | 対話操作 | 中 | オブジェクト情報パレットのボタンを押します。 |

### getOIPControls

オブジェクト情報パレットの1つのタブのコントロールを一覧表示します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

オブジェクト情報パレットの1つのタブに、現在の選択に対して表示されるコントロールを一覧表示します。最初にタブが更新されるため、selectObjectsの直後でも一覧は選択と一致します。`pane`: shape（デフォルト）、data、render。`search`は、ラベルにそのテキストを含むコントロールだけを残します（大文字小文字を区別しません）。`includeHidden`（デフォルトfalse）は、非表示のコントロールも一覧に含めます。`maxChoices`（0以上、デフォルト50）は、一覧に含めるコントロールの`choices`の数を制限します（`choiceCount`は全数のままです）。`limit`（デフォルト100）と`offset`で一覧をページ分割します。`countOnly`（デフォルトfalse）は、`count`とその他のページ分割のキーを返し、`controls`は返しません。

`pane`、`available`（true）、`selectionCount`、`count`（`search`に一致するコントロールの数）、`controls`（このページ）、およびページ分割のキー（続きがある場合は`truncated`がtrue）を返します。何も選択されていない場合など、コントロールのないタブはエラーではありません: `available`がfalse、`count`が0、`controls`が空になり、`hint`が付きます。各コントロールには、`controlId`、`type`（editText、staticText、checkBox、radioGroup、pullDown、searchablePullDown、button、classPullDown、layerPullDown、other）、`label`、`value`（テキスト）、`enabled`、`readOnly`、`indeterminate`（選択したオブジェクトで値が異なる）があります。さらに、includeHiddenを指定した場合は`visible`、親コントロールがある場合は`parentId`、不定ではないチェックボックスには`checked`、radioGroupと4種類のプルダウンには`choices`、`choiceCount`、`selectedChoice`（0から始まる）、ラベルがダイアログを開くボタンには`opensDialog`: true、otherタイプには`coreTypeId`があります。

> **注:** コントロールは`controlId`の昇順で一覧表示されます。`value`はコントロールに表示されるテキストです: 編集フィールドのテキスト、staticTextのラベル、チェックボックスでは`on`、`off`、または空（不定）、radioGroupと4種類のプルダウンでは選択された項目です。その他のタイプでは空です。`readOnly`がtrueになり得るのは編集フィールドだけです。
>
> searchablePullDownでは、パレットが項目を一覧表示しないため、`choices`は常に空です。それでも`choiceCount`と`selectedChoice`は設定されます。項目が選択されていない場合、`selectedChoice`は省略されます。
>
> `search`とsetOIPValuesの選択肢名で大文字小文字が区別されないのは、A～Zの文字だけです。その他の文字は、パレットに表示されるとおりに入力してください。setOIPValuesとpressOIPButtonの`label`は、Vectorworksの大文字小文字を区別しないテキスト比較で比較されます。
>
> コントロールのないタブは、`pane`、`available` false、`selectionCount`、`count` 0、`controls`（`countOnly`の場合も含め、常に空のリスト）、`hint`だけを返し、`returned`、`offset`、`limit`、`truncated`は返しません。`hint`は`The <pane> pane of the Object Info palette shows no controls: select objects first (Selection group, selectObjects)`です。タブのすべてのコントロールが非表示で、`includeHidden`がfalseの場合も、この結果になります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `pane` | string |  | 次のいずれか: `shape`, `data`, `render`。デフォルト: `shape`。 |
| `search` | string |  | テキストフィルタ: ラベルにこのテキストを含むコントロールだけを残します（A～Zの文字だけ大文字小文字を区別しません）。 |
| `includeHidden` | boolean |  | 非表示のコントロールも一覧に含めます。その場合、各コントロールに`visible`が付きます。デフォルトfalse。 |
| `maxChoices` | integer |  | 0以上、デフォルト50。1つのコントロールについて一覧に含める`choices`の最大数です。`choiceCount`は全数のままです。 |
| `limit` | integer |  | ページ分割: 返す項目の最大数（1以上）。デフォルト: 100。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割: スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割: 項目を含めず、件数だけを返します。 |

エラー: `'pane' must be shape, data or render`、`'search' must be a string`、`'maxChoices' must be a whole number of 0 or more`、`'includeHidden' must be true or false`、およびページ分割のエラー（[ページ分割](Common.md#paging)を参照）。

### setOIPValues

ユーザーと同じように、オブジェクト情報パレットのコントロールを設定します。

> **作用:** 対話操作 · **安全性:** 中 · **取り消し:** ユーザー入力と同様にVectorworksが記録 · **runToolBatch内:** 不可

**詳細**

ユーザーと同じように、オブジェクト情報パレットのコントロールを順番に設定します。`settings`: 1～50個のエントリ { `label`または`controlId`、`value`、`pane`（省略可能。デフォルトは呼び出しの`pane`で、そのデフォルトはshape） }。`allowDialog`（デフォルトfalse）。コントロールのタイプごとの`value`: editText - 入力するテキスト、または数値（記述どおりに入力）。checkBox - 真偽値、またはon/off、yes/no、1/0、toggle。radioGroupと4種類のプルダウン - 選択肢名または0から始まるインデックス。searchablePullDownは項目を一覧表示しないため、そのインデックスを指定するには`allowDialog`: trueが必要です（項目がダイアログを開く可能性があるため）。

何かを変更する前に、すべての設定が確認されます。不明、非表示、無効、または読み取り専用のコントロール、staticTextまたはotherのコントロール、ボタン（pressOIPButtonを使用）、コントロールに適合しない値、および`allowDialog`: trueなしでダイアログを開く選択肢の場合、呼び出しは何も変更せずに拒否されます。そのため、前の設定によって初めて表示または有効になるコントロールも拒否されます。そのようなコントロールは、後の呼び出しで設定してください。

その後、設定が順番に適用されます。各コントロールは設定の直前に再度検索され（前の設定がパレットを再構築する可能性があるため）、新しい値が読み戻されます。呼び出しは最初の失敗で停止します。`pane`、`results` [{ index, label, controlId, ok, value（読み戻した値）またはerr }]、`appliedCount`、`allApplied`、`notAttemptedCount`を返します。最初の設定が失敗した場合は、最上位の`err`が追加されます。後の設定が失敗した場合、それ以前の設定は適用されたままです（`allApplied`はfalse、最上位の`err`はなし）。

「MCP: setOIPValues」という取り消しステップもロールバックもありません。適用された各設定が、それぞれVectorworksの取り消しステップになります。

> **注:** `value`の読み取り方法（コントロールのタイプ別）:
>
> - editText: 文字列（記述どおりに入力）または数値（読み戻せる最短のテキストとして記述。例: `200`、`0.5`）。その他のJSONの型は拒否されます。
> - checkBox: JSONの真偽値、または文字列`on`、`off`、`true`、`false`、`yes`、`no`、`1`、`0`、`toggle`のいずれか（大文字小文字を区別しません）。`1`などのJSONの数値は拒否されます。`toggle`は不定のチェックボックスをオンにします。
> - radioGroup、pullDown、classPullDown、layerPullDown: まず、一覧にある選択肢名（A～Zの文字は大文字小文字を区別しません）として試されます。それ以外の場合は、JSONの数値または数字だけの文字列で指定した`choiceCount`未満の整数が、0から始まるインデックスになります。
> - searchablePullDown: 空でない文字列は常に項目のテキストとして扱われ（`"3"`も同様）、Vectorworksは設定の適用時にその項目を検索します。インデックスは、`choiceCount`未満のJSONの数値でなければなりません。
> - テキストが`...`で終わる選択肢と、searchablePullDownへのインデックスには、`allowDialog`: trueが必要です。
>
> **注:** 最初の変更前の確認では、コントロールと値の形式を確認します。Vectorworksが編集フィールドのテキストやsearchablePullDownの項目テキストを受け付けるかどうかはわからないため、そのような値は、それ以前の設定が適用された後、適用時に失敗することがあります（そのエントリは`ok`がfalseで、`allApplied`はfalseになります）。確認での拒否は`err`だけを返し、`err`は`; nothing was changed`で終わります。
>
> **注:** `results`には、試行された設定ごとに1つのエントリがあります。失敗の後の設定は試行されません（`notAttemptedCount`）。`label`と`controlId`は、最初の変更前の確認で見つかったコントロールのものです。`label`で指定した設定では、パレットを再構築した前の設定によってコントロールのIDが変わることがあるため、`results`の`controlId`を使用する前に、getOIPControlsでコントロールを読み取り直してください。`value`は再構築されたパレットから読み戻され、コントロールが表示されなくなった場合は省略されます。最上位の`pane`は呼び出しの`pane`で、設定の`pane`はそのエントリでは繰り返されません。最初の設定が失敗した場合、`err`は理由の後に`; nothing was changed`が続くものになります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `pane` | string |  | 次のいずれか: `shape`, `data`, `render`。デフォルト: `shape`。 |
| `settings` | array of object | はい | 1～50項目。順番に適用されます。 |
| `settings[].label` | string |  | コントロールのラベル: そのラベルを持つ最初の表示されているコントロール（大文字小文字を区別しません。前後の空白と末尾の`:`は無視され、ラベル内の空白は区別されます）。`label`と`controlId`のうち、ちょうど1つが必要です。 |
| `settings[].controlId` | integer |  | getOIPControlsの`controlId`。非表示のコントロールも見つけますが、その場合は拒否されます。`label`と`controlId`のうち、ちょうど1つが必要です。 |
| `settings[].value` | string or number or boolean | はい | 新しい値。読み取り方法はコントロールのタイプによって異なります（上記の注を参照）。 |
| `settings[].pane` | string |  | 次のいずれか: `shape`, `data`, `render`。デフォルト: 呼び出しの`pane`。 |
| `allowDialog` | boolean |  | デフォルトfalse。ダイアログを開く選択肢（テキストが`...`または`…`で終わる）と、searchablePullDownでインデックスによって選ぶ項目に必要です。 |

エラー: `'pane' must be shape, data or render`、`'allowDialog' must be true or false`。確認では、`err`は`; nothing was changed`で終わります。たとえば`'settings' is missing: give an array of 1 to 50 objects with 'label' or 'controlId' and 'value'`、または設定を`settings[<index>]`として示し、何が誤っているかを示します: `value`がない、`give 'label' or 'controlId'`（または`..., not both`）、`no control labeled '<label>' in the <pane> pane`（または`no control with controlId <id> in the <pane> pane`）、非表示、無効、読み取り専用、ボタン、staticText、またはotherタイプのコントロール、コントロールに適合しない値、`allowDialog`: trueなしでダイアログを開く選択肢。適用中（`results[].err`内。`settings[<index>]`のプレフィックスなし）: `Vectorworks did not accept <value> for '<label>'`（`<value>`は`value`のJSONテキストで、文字列は二重引用符で囲まれます。前の設定がコントロールを無効にした場合、編集フィールドを読み取り専用にした場合、または`controlId`で指定したコントロールを非表示にした場合にも返されます）、`no control labeled '<label>' in the <pane> pane`（前の設定がコントロールを削除または非表示にした場合）または`no control with controlId <id> in the <pane> pane`（前の設定がコントロールを削除した場合）、およびコントロールのタイプが変わった場合や、`controlId`で指定したコントロールのラベルが変わった場合は`the Object Info palette changed after an earlier setting; read the controls again with getOIPControls`。

### pressOIPButton

オブジェクト情報パレットのボタンを押します。

> **作用:** 対話操作 · **安全性:** 中 · **取り消し:** ユーザー入力と同様にVectorworksが記録 · **runToolBatch内:** 不可

**詳細**

ユーザーがクリックするのと同じように、オブジェクト情報パレットのボタンを押します。`pane`（デフォルトshape）内のボタンを`label`または`controlId`で指定します。タブにコントロールがない場合、コントロールが不明、非表示、無効、またはボタンではない場合、またはボタンがダイアログを開き（ラベルが「...」で終わる。getOIPControlsの`opensDialog`）、`allowDialog`がtrueでない場合は、何も押さずに拒否されます。その場合は、ダイアログが開くことと、ユーザーがそこでダイアログを閉じる必要があることを伝えてから、`allowDialog`: trueで再度呼び出してください。

`pane`、`label`、`controlId`、`pressed`: trueを返します。ボタンを押すとパレットが再構築される場合があるため、その後コントロールを読み取り直してください。

> **注:** `label`と`controlId`は、setOIPValuesと同様に使用します: どちらか一方だけが必要です。`label`は、そのラベルを持つ最初の表示されているコントロールを見つけます。`controlId`は非表示のコントロールも見つけますが、その場合は拒否されます。
>
> 拒否は`err`だけを返し、`err`は`; nothing was pressed`で終わります: `<control> is hidden`、`<control> is disabled`、`<control> is not a button (type <type>)`、`<control> opens a dialog in Vectorworks: tell the user that it will open and that they must close it there, then call again with 'allowDialog': true`、コントロールを表示しないタブ、および指定が誤っているか見つからないコントロール（`give 'label' or 'controlId'`または`..., not both`、`'label' must be a non-empty string`、`'controlId' must be an integer`、`no control labeled '<label>' in the <pane> pane`、`no control with controlId <id> in the <pane> pane`）。`<control>`は`'<label>'`、またはラベルが空の場合は`controlId <id>`です。Vectorworksがボタンの押下を受け付けない場合、`err`はその末尾のない`<control> could not be pressed`になります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `pane` | string |  | 次のいずれか: `shape`, `data`, `render`。デフォルト: `shape`。 |
| `label` | string |  | ボタンのラベル: そのラベルを持つ最初の表示されているコントロール（大文字小文字を区別しません。前後の空白と末尾の`:`は無視され、ラベル内の空白は区別されます）。`label`と`controlId`のうち、ちょうど1つが必要です。 |
| `controlId` | integer |  | getOIPControlsの`controlId`。非表示のコントロールも見つけますが、その場合は拒否されます。`label`と`controlId`のうち、ちょうど1つが必要です。 |
| `allowDialog` | boolean |  | デフォルトfalse。ボタンのラベルが`...`または`…`で終わる場合に必要です。 |

エラー: `'pane' must be shape, data or render`、`'allowDialog' must be true or false`（何かを検索する前に返されます）。
