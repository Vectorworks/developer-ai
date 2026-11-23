[English](../../MCP/v2027.2/MenuAccess.md) • [Deutsch](../../MCP.de/v2027.2/MenuAccess.md) • **日本語**

# MenuAccess — メニューコマンド

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

Vectorworksのメニューを読み取り、コマンドを実行できるかどうかを確認し、ユーザーが選択した場合と同じようにメニューコマンドを実行するツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [Menus](#menus)
  - [findMenuCommands](#findmenucommands)
  - [getMenus](#getmenus)
  - [getMenuStatus](#getmenustatus)
  - [runMenuCommand](#runmenucommand)

<a id="overview"></a>

## 概要

このフォルダには1つのツールグループがあり、合計4個のツールを提供します。

| グループ | グループID | 初期状態で有効 | 安全性レベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [Menus](#menus) | `menus` | いいえ | 高 | 4 | メニューコマンドの検索、メニューバーの読み取り、コマンドを現在実行できるかどうかの確認、およびその実行を行います。 |

## Menus

> **グループ:** `Menus` · **グループID:** `menus` · **初期状態で有効:** いいえ · **安全性レベル:** 高 · **ツール数:** 4

**メニューコマンドの検索、メニューバーの読み取り、コマンドを現在実行できるかどうかの確認、およびその実行を行います。**

Vectorworksのメニューを読み取り、そのコマンドを実行します。対象は、インストール済みのメニューコマンド、現在の作業画面のメニューバーにあるメニューとそのサブメニュー、コマンド、チャンクメニュー項目、コマンドやチャンクメニュー項目が現在有効かどうかやチェックされているかどうか、およびユーザーが選択した場合と同じようにコマンドまたはチャンクメニュー項目を実行するrunMenuCommandです。このグループを使用すると、ある作業のためのコマンドをVectorworksが提供しているかどうかとその場所（ユーザーを案内するため）、コマンドの機能、現在の状態（開いているファイル、選択など）で実行できるかどうか、チェックされているかどうか（表示オプションなど）、および最近使ったファイル、標準ビュー、開いているファイルなどのチャンクメニューの現在の項目を調べられます。findMenuCommands、getMenus、getMenuStatusは読み取りのみで、図面は何も変更されません（取り消しステップなし）。runMenuCommandは高リスクです。メニューコマンドはデータを変更、削除したり、ダイアログを開いたりする可能性があり、独自の取り消しステップを記録します。呼び出しのたびにユーザーに確認してください。

他のグループの専用ツールで行える変更には、そちらを優先してください。

名前: コマンドには、`universalName`（安定した識別名。組み込みコマンドでは"-28"などの負の数）、`name`（英語名。プラグインコマンドではuniversalNameと同じ）、`displayName`（メニューに表示されるローカライズされたタイトル）があります。ツールはどれでも受け付け、大文字小文字を区別せず、末尾の「...」はあってもなくても構いません。universalNameを優先してください。メニューのタイトルとエントリのテキストは、ユーザーに表示されるとおりにローカライズされています。

インストール済みと作業画面内: findMenuCommandsはインストール済みのすべてのコマンドを一覧表示します。`inWorkspace`は、現在の作業画面のメニューにそのコマンドが含まれるかどうかを示します。有効になり得るのは作業画面内のコマンドだけで、項目を持つのも作業画面内のチャンクメニューだけです。

**チャンクメニュー:** チャンクメニューは、一群のメニュー項目（最近使ったファイル、標準ビューなど）を提供するコマンドです。項目は、そのチャンクメニューのuniversalNameと、0から始まるインデックスまたはテキストで指定します。チャンクメニューには、regular（固定の項目）、dynamic（メニューバーとともに構築される項目）、variable（Vectorworksの実行中に変化する項目）があります。項目のテキストとチェックマークは、Vectorworksが最後にメニューを更新した時点のものです。更新はユーザーがメニューを開いたときに行われるため、古い場合があります。`enabled`は常に最新の状態です。Macでは、チャンクメニュー項目に`checked`はありません。

ワークフロー:

1. findMenuCommandsの`search`で候補のコマンドを検索します。
2. getMenusの`search`または`menu`で、それらのメニュー内の場所を確認します。getMenusの`chunk`はチャンクメニューの項目を一覧表示します。
3. getMenuStatusで、コマンドまたはチャンクメニュー項目を現在実行できるかどうか、できない場合はその理由を確認します。
4. ユーザーの同意を得た後、runMenuCommandで実行します。

| ツール | 作用 | 安全性 | 概要 |
|---|---|---|---|
| [`findMenuCommands`](#findmenucommands) | 読み取り専用 | 低 | インストール済みのメニューコマンドを、テキストと作業画面で検索します。 |
| [`getMenus`](#getmenus) | 読み取り専用 | 低 | 現在の作業画面のメニューバー、1つのメニュー、またはチャンクメニューの項目を読み取ります。 |
| [`getMenuStatus`](#getmenustatus) | 読み取り専用 | 低 | メニューコマンドまたはチャンクメニュー項目を現在実行できるかどうか、できない場合はその理由を返します。 |
| [`runMenuCommand`](#runmenucommand) | 対話操作（破壊的） | 高 | ユーザーが選択した場合と同じように、メニューコマンドまたはチャンクメニュー項目を実行します。 |

### findMenuCommands

インストール済みのメニューコマンドを、テキストと作業画面で検索します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

インストール済みのメニューコマンドを検索します。`search`は、universalName、name、displayName、category、helpTextにそのテキストを含むコマンドだけを残します（大文字小文字を区別しません）。`filter`: all（デフォルト。インストール済みのすべてのコマンド）、inWorkspace（現在の作業画面のメニュー内）、またはenabled（Vectorworksが現在実行できるもの。チャンクメニューの場合は少なくとも1つの項目）。または、`name`でuniversalName、name、displayNameによって1つのコマンドを検索します（大文字小文字を区別せず、末尾の「...」は省略可能。同順位の場合は作業画面内のコマンドが優先されます）。`name`は`search`や`filter`と併用できません。

`limit`（デフォルト50）と`offset`で一覧をページ分割します。`countOnly`（デフォルトfalse）は、`commands`を含めずにページ分割のキーを返します。`commands`（このページ）、`count`（一致したすべての数）、`returned`、`offset`、`limit`、`truncated`、続きがある場合は`nextOffset`、および`filter`（`name`を指定した場合は`name`）を返します。どのコマンドにもない`name`はエラーではなく、`count`が0になり、`hint`が付きます。

各コマンドには、`universalName`、`name`、`displayName`、`category`（作業画面の編集でのカテゴリ）、`helpText`、`kind`（internal、scriptPlugin、extensionPlugin、unknown）、`isChunk`、`inWorkspace`、`enabled`があり、作業画面でショートカットが割り当てられている場合は`shortcut`もあります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string |  | universalName、name、displayNameで1つのコマンドを検索します（大文字小文字を区別しません）。末尾の「...」はdisplayNameに対してのみ省略または追加でき、universalNameとnameは大文字小文字以外が一致する必要があります。`search`や`filter`とは併用できません。 |
| `search` | string |  | テキストフィルタ: universalName、name、displayName、category、helpTextにこのテキストを含むコマンドだけを残します（ASCII文字の大文字小文字を区別しません）。 |
| `filter` | string |  | 次のいずれか: `all`, `inWorkspace`, `enabled`。デフォルト: `all`。 |
| `limit` | integer |  | ページ分割: 返す項目の最大数（1以上）。デフォルト: 50。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割: スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割: 項目を含めず、件数だけを返します。 |

エラー: `'filter' must be all, inWorkspace or enabled`、`'name' cannot be used with 'search' or 'filter'`、および空または文字列以外の値に対する`'name' must be a non-empty string`または`'search' must be a non-empty string`。

### getMenus

現在の作業画面のメニューバー、1つのメニュー、またはチャンクメニューの項目を読み取ります。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

現在の作業画面のメニューバーを読み取ります。何も実行しません。

**引数なし:** `menus`として、メニューバーのメニューのタイトルを左から右の順に返します。`menu`（`menus`に含まれるタイトル。大文字小文字を区別しません）は、そのメニューのエントリを深さ優先で一覧表示します。サブメニューのエントリの後にはそのサブメニューのエントリが、チャンクメニューの後にはその現在の項目が続き、区切り線は省略されます。`search`は、すべてのメニュー、または`menu`内だけで、テキストまたはuniversalNameにそのテキストを含むエントリだけを残します（大文字小文字を区別しません）。`chunk`（作業画面内のチャンクメニューのuniversalName、name、displayName。`menu`や`search`とは併用不可）は、そのチャンクメニューの現在の項目を一覧表示します。`limit`（デフォルト100）と`offset`で一覧をページ分割し、`countOnly`（デフォルトfalse）はページ分割のキーだけを返します。`menus`、`entries`、`items`のいずれか（このページ）と、`count`、`returned`、`offset`、`limit`、`truncated`、続きがある場合は`nextOffset`を返します。また、`menu`を指定した場合は`menu`、チャンクメニューの場合は`chunk`（findMenuCommandsと同じ形式のコマンド）も返します。エントリには、`type`（command、chunkItem、submenu）、`menuPath`（エントリを含むメニューのタイトル。メニューバーから下に向かう順。例: ["File", "Export"]）、`text`があります。コマンドとチャンクメニュー項目にはさらに`universalName`、`enabled`、`checked`があり、チャンクメニュー項目には`chunkKind`（regular、dynamic、variable）と`chunkItemIndex`があり、ショートカットがあるエントリには`shortcut`があります。`chunk`の項目には、`index`（チャンクメニュー内での0から始まる位置。区切り線の位置はスキップされます）、`text`、`enabled`、`checked`があります。Macでは、チャンクメニュー項目に`checked`はありません。

**エラー:** メニューバーにない`menu`、どのコマンドの名前でもない`chunk`、チャンクメニューではない`chunk`、または作業画面内にない`chunk`。

> **注:** 存在してもエントリがまったくない`menu`も失敗し、エラーにはメニューのタイトルが列挙されます: `no menu titled '<menu>' in the menu bar, or the menu is empty; its menus: <titles>`（区切り線だけのメニューの場合は、代わりに空の`entries`リストと`count` 0を返します）。`menu`のタイトルは、末尾の「...」の有無にかかわらず一致します。universalNameのないエントリでは、`universalName`は省略されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `menu` | string |  | `menus`に含まれるタイトル。大文字小文字を区別しません。末尾の「...」は省略できます。 |
| `search` | string |  | テキストフィルタ: すべてのメニュー、または`menu`内だけで、テキストまたはuniversalNameにこのテキストを含むエントリだけを残します（ASCII文字の大文字小文字を区別しません）。 |
| `chunk` | string |  | 作業画面内のチャンクメニューのuniversalName、name、displayName。`menu`や`search`とは併用できません。 |
| `limit` | integer |  | ページ分割: 返す項目の最大数（1以上）。デフォルト: 100。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割: スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割: 項目を含めず、件数だけを返します。 |

エラー: `'chunk' cannot be used with 'menu' or 'search'`、空または文字列以外の`menu`、`search`、`chunk`に対する`'<key>' must be a non-empty string`、`'<chunk>' is the menu command '<universalName>', not a chunk: getMenuStatus tells whether it can run`、`the chunk '<universalName>' is not placed in the menus of the current workspace, so it shows no items`、`no installed menu command is named '<chunk>': search for it with findMenuCommands 'search'`。

### getMenuStatus

メニューコマンドまたはチャンクメニュー項目を現在実行できるかどうか、できない場合はその理由を返します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

Vectorworksがメニューコマンドまたはチャンクメニュー項目を現在実行できるかどうか、できない場合はその理由を返します。何も実行しません。`name`: コマンドまたはチャンクメニューのuniversalName（推奨）、name、displayName。チャンクメニューでは、`chunkItemIndex`（getMenusの`index`または`chunkItemIndex`）または`chunkItemText`（大文字小文字を区別しません）で項目を指定します。項目が1つだけのチャンクメニューでは、どちらも不要です。`name`、`status`、`enabled`（readyの場合はtrue）、`reason`、その名前のコマンドがある場合は`command`（findMenuCommandsと同じ形式）を返します。readyまたはdisabledの場合は`checked`（メニューにチェックマークが表示されるかどうか。Macのチャンクメニュー項目にはありません）、チャンクメニュー項目の場合はさらに`chunkItemIndex`と`chunkItemText`を返します。

`status`: ready、disabled（別の状態が必要。開いているファイル、選択など）、notInWorkspace（インストール済みだが、現在の作業画面のメニューにない）、notFound、chunkItemRequired（複数の項目を持つチャンクメニュー。1つを指定してください）、chunkItemNotFound（該当する項目がない、またはコマンドがチャンクメニューではない）、unavailable（現在はどのコマンドも実行できない。メニューバーが設定されていないか、プラグインオブジェクトの再生成中）。

> **注:** `chunkItemNotFound`は、現時点で項目がないチャンクメニュー（項目を指定しない場合）と、チャンクメニューではないコマンドに`chunkItemIndex`を指定した場合の状態でもあります。`checked`は、そのコマンドを実行する最初のメニューバーのエントリから読み取られ、エントリがない場合（コンテキストメニューにだけ配置されたコマンドなど）は省略されます。すべてのCoreツールと同様に、ファイルが開いていない場合、呼び出しは`no active Vectorworks document`で失敗します（[結果とエラー](Common.md#results-and-errors)を参照）。そのため、開いているファイルがないことを理由に`disabled`と報告されるコマンドはありません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string | はい | コマンドまたはチャンクメニューのuniversalName（推奨）、name、displayName。 |
| `chunkItemIndex` | integer |  | getMenusの`index`または`chunkItemIndex`（0以上）。`chunkItemText`とは併用できません。 |
| `chunkItemText` | string |  | 項目のテキスト（大文字小文字を区別しません）。末尾の「...」は省略できます。`chunkItemIndex`とは併用できません。 |

エラー: `'name' must be a non-empty string`、`'chunkItemText' must be a non-empty string`、`'chunkItemIndex' must be a whole number of 0 or more`、`'chunkItemIndex' and 'chunkItemText' cannot be used together`。

### runMenuCommand

ユーザーが選択した場合と同じように、メニューコマンドまたはチャンクメニュー項目を実行します。

> **作用:** 対話操作（破壊的） · **安全性:** 高 · **取り消し:** メニューコマンドが記録 · **runToolBatch内:** 不可

**詳細**

ユーザーがメニューバーで選択した場合と同じように、Vectorworksのメニューコマンドまたはチャンクメニュー項目を実行します。

**高リスク:** 実行するコマンドとその動作をユーザーに伝え、同意を得た後にのみ実行してください。`name`: getMenuStatusと同様に、コマンドまたはチャンクメニューのuniversalName（推奨）、name、displayName。チャンクメニューでは、`chunkItemIndex`または`chunkItemText`で項目を指定します（項目が1つだけのチャンクメニューではどちらも不要）。getMenuStatusがreadyを報告する場合にのみ実行されます。それ以外の場合は何も実行されず、結果には`err`、`ran` false、およびgetMenuStatusのキー（`status`、`reason`、`command`など）が含まれます。

**ダイアログ:** 呼び出しは、コマンドが開いたダイアログと警告をユーザーが閉じた後にのみ戻り、その間は他の呼び出しに応答しません。タイトルが「...」で終わるコマンドやチャンクメニュー項目はダイアログを開きます。SDKプラグインコマンド（kindがextensionPlugin）は、「...」がなくてもダイアログを開く場合があります。これらは、`allowDialog`がtrueでない限り拒否されます。`allowDialog`は、ダイアログが開くことと、ユーザーがVectorworksでそれを閉じる必要があることを伝えてから指定してください。それでも、どのコマンドも警告を表示する場合があります（ライセンスに含まれていないコマンドなど）。

**実行前に拒否されるもの:** ファイルを開く、保存する、プリントする、閉じる、切り替える、またはVectorworksを終了するコマンド（新規、開く、最近使ったファイル、ホームスクリーン、閉じる、保存、すべて保存、元に戻す、Vectorworksファイル取り出し、プリント、終了、ウインドウメニューの開いているファイルなど）、プロジェクト共有ファイルの更新、取り消しとやり直し、カットとコピー（ユーザーのクリップボードを置き換えるため）、最近使用したコマンドの再実行、スクリプトを実行、プラグインマネージャ、作業画面の切り替え、VectorScriptまたはPythonのプラグインコマンド（kindがscriptPlugin）。また、ツール操作の実行中や取り消しイベントが開いている間は、readyのコマンドも拒否されます。

**取り消し:** コマンドはVectorworksでの操作と同じく独自の取り消しステップを記録し、「MCP: runMenuCommand」にはなりません。失敗した呼び出しはロールバックされず、このツールはrunToolBatch内では実行できません。`ran` true、`command`、チャンクメニュー項目の場合は`chunkItemIndex`と`chunkItemText`、`undoSteps`（コマンドが追加した取り消しステップの名前。新しい順。追加がなければ空）、`documentBefore`と`documentAfter`（アクティブファイルのファイル名。ファイルが開いていない場合、`documentAfter`はnull）と`documentChanged`、`activeTool`（実行後のアクティブツールのuniversalName）と`activeToolChanged`、`waitingForInput`（コマンドが取り消しステップを開いたままにしたか、アクティブツールを変更した場合はtrue。一時ツールのクリックなど、Vectorworksで入力を待っている可能性があります。そこで操作を完了またはキャンセルするようユーザーに伝え、それまでは他の変更を行わないでください）、およびファイルが変わった場合や入力待ちの場合は`hint`を返します。ファイルが変わった場合は`undoSteps`が省略され、以降の呼び出しは新しいアクティブファイルに作用します。実行後は、メニュー、選択、オブジェクトを読み取り直してください。

> **注:** 拒否とダイアログのルールが最初に確認され、どれも`err`だけを返します。`ran`も、上の段落で挙げたgetMenuStatusのキーも含まれません。テキストは、`'<title>' (<universalName>) is not run by runMenuCommand: it <reason>; ask the user to choose it in Vectorworks`、`'<dialogTitle>' opens a dialog in Vectorworks: tell the user that it will open and that they must close it there, then call again with 'allowDialog': true`、`'<title>' is an SDK plug-in command, which can open a dialog in Vectorworks: ...`です。この順序のため、タイトルが「...」で終わる無効なコマンドは、状態が報告される前に`allowDialog`を求めます。そのため、先にgetMenuStatusを呼び出してください。タイトルが「...」で終わるとは、末尾のスペース、タブ、改行を除いたテキストが、3つのピリオドまたは省略記号「…」で終わることです。このルールは、チャンクメニュー項目のテキストと、コマンドのnameおよびdisplayNameに適用されます。拒否されるコマンドには、スクリプトの実行のほか、スクリプトのロック（暗号化）も含まれます。
>
> これらの確認を通過し、readyではないか見つからないコマンドだけが、getMenuStatusのキーと、`ran` false、`err`（`<reason>; nothing was run`）を返します。さらに2つの拒否は`err`だけを返します: `a tool action is in progress in Vectorworks: the user must finish or cancel it first; nothing was run`と`an undo event is open in Vectorworks (another operation is in progress): a menu command records its own undo step and cannot run inside it; nothing was run`です。Vectorworksが拒否または中止した実行は、状態のキーなしで、`err`（`'<title>' did not run: Vectorworks refused or stopped it, for example a command that the license does not include (an alert tells the user)`）と`ran` falseを返します。
>
> 最初のクリックを待っている一時ツールは、ツール操作の実行中かどうかの確認では検出されないため、待機中に後続の呼び出しが拒否されることはありません。`waitingForInput`がtrueになった後は、ユーザーがVectorworksでツールを完了またはキャンセルするまで、次の呼び出しを行わないでください。すべてのCoreツールと同様に、ファイルが開いていない場合、呼び出しは`no active Vectorworks document`で失敗します（[結果とエラー](Common.md#results-and-errors)を参照）。
>
> `undoSteps`は、実行前後の取り消しステップを、名前ではなく取り消しイベントのIDで比較します。コマンドが追加し、まだ取り消し履歴に残っているすべてのステップの名前を返します（取り消し履歴が保持するのは、最大で環境設定の「取り消し回数を設定」の数までです）。名前が以前のステップと同じ場合も含まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string | はい | コマンドまたはチャンクメニューのuniversalName（推奨）、name、displayName。getMenuStatusと同様です。 |
| `chunkItemIndex` | integer |  | getMenusの`index`または`chunkItemIndex`（0以上）。`chunkItemText`とは併用できません。 |
| `chunkItemText` | string |  | 項目のテキスト（大文字小文字を区別しません）。末尾の「...」は省略できます。`chunkItemIndex`とは併用できません。 |
| `allowDialog` | boolean |  | デフォルト: false。ダイアログを開く、または開く可能性があるコマンドを実行するには、trueにする必要があります。タイトルが「...」または「…」で終わるか、kindがextensionPluginの場合が該当します。 |

**結果**

実行された場合:

| キー | 説明 |
|---|---|
| `name` | 渡された`name`。 |
| `ran` | `true`。 |
| `command` | findMenuCommandsと同じ形式のコマンド。 |
| `chunkItemIndex`, `chunkItemText` | チャンクメニュー項目の場合のみ: 実行した項目。 |
| `documentBefore` | 実行前のアクティブファイルのファイル名（未保存のファイルの場合は名称未設定のファイル名）。 |
| `documentAfter` | 実行後のアクティブファイルのファイル名（未保存のファイルの場合は名称未設定のファイル名）。ファイルが開いていない場合は`null`。 |
| `documentChanged` | アクティブファイルが実行前と異なる場合は`true`: 別のファイル、ファイルなし（`documentAfter`が`null`）、同じファイルを開き直した場合、または同じファイルが別のファイルパスにある場合（新しい名前で保存された場合など）。 |
| `undoSteps` | コマンドが追加した取り消しステップの名前。新しい順です（追加がなければ空）。ファイルが変わった場合と、取り消しステップを読み取れない場合は省略されます。 |
| `activeTool` | 実行後のアクティブツールのuniversalName。アクティブツールがない場合は`null`。 |
| `activeToolChanged` | 実行によってアクティブツールが変わった場合は`true`。 |
| `waitingForInput` | コマンドが取り消しイベントを開いたままにしたか、アクティブツールを変更した場合は`true`。 |
| `hint` | 伝えることがある場合のみ: ファイルの変更または入力待ち。 |

エラー: `'allowDialog' must be true or false`、getMenuStatusの引数のエラー、および上記の注で説明した拒否、readyではない結果、失敗した実行。
