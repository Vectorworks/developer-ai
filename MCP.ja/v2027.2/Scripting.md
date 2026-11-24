[English](../../MCP/v2027.2/Scripting.md) • [Deutsch](../../MCP.de/v2027.2/Scripting.md) • **日本語**

# Scripting — Pythonスクリプト

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

Vectorworks内でのPythonスクリプトの実行、Pythonスクリプトリソースの読み取りと保存、およびスクリプトで使用するPythonの`api`モジュールの参照を行うツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [Scripting](#scripting)
  - [listScripts](#listscripts)
  - [getScript](#getscript)
  - [saveScript](#savescript)
  - [describePythonApi](#describepythonapi)
  - [getPythonApiGuide](#getpythonapiguide)
  - [runPythonScript](#runpythonscript)
  - [runScript](#runscript)

<a id="overview"></a>

## 概要

このフォルダには1つのツールグループがあり、合計7個のツールを提供します。

| グループ | グループID | 初期状態で有効 | リスクレベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [Scripting](#scripting) | `scripting` | いいえ | 高 | 7 | Pythonスクリプトの実行、Pythonスクリプトリソースの読み取りと保存、およびPythonの`api`モジュールの参照を行います。 |

## Scripting

> **グループ:** `Scripting` · **グループID:** `scripting` · **初期状態で有効:** いいえ · **リスクレベル:** 高 · **ツール数:** 7

**Pythonスクリプトの実行、Pythonスクリプトリソースの読み取りと保存、およびPythonの`api`モジュールの参照を行います。**

Vectorworks内でPythonスクリプトを実行し、アクティブファイルのPythonスクリプトリソースを読み取り、保存し、スクリプトで使用するPythonの`api`モジュールを参照します。runPythonScriptはPythonコードを、runScriptは保存済みのPythonスクリプトリソースを実行します。listScriptsとgetScriptはスクリプトリソース（名前、言語、パレット、テキスト）を読み取ります。saveScriptは、Pythonスクリプトリソースを実行せずに作成または更新します。describePythonApiは、`api`のクラス、列挙型、関数、メンバーのヘルプテキストを返し、名前を指定しない場合は`api`と`api.Math`の名前を一覧表示します。getPythonApiGuideは、これらのスクリプトを作成するためのガイドを1回の呼び出しにつき1セクション返します。スクリプトを作成する前に読んでください。

スクリプトは、`vs`モジュールではなく、Pythonの`api`モジュール専用に記述してください（import apiの後、api.Document()などのクラスを使用）。このモジュールの名前にはC++の接頭辞がないため（api.CDocumentではなくapi.Document）、使用する前にすべてのクラスをdescribePythonApiで調べてください。結果をJSON（json.dumps）として出力すると、`output`で受け取れます。各実行は「MCP: script」という1つの取り消しステップになります（変更を登録しない実行では、取り消しステップは残りません）。スクリプト自身の取り消しイベントの呼び出しは無視されるため、スクリプトは作成したもの（doc.AddAfterSwapObject(obj.GetHandle())）と変更するもの（変更前にdoc.AddBothSwapObject(handle)）を登録する必要があります。登録しないと、取り消しで元に戻せません。

失敗した実行は元に戻される（`rolledBack`）ため、登録したものは何も残りません。スクリプトを修正して再度実行してください。スクリプトが登録しなかった変更は元に戻せません。スクリプトはユーザー入力（GetPt、ダイアログ）を決して待ってはいけません。また、無限ループはVectorworksを停止させます。他のスクリプトの実行中や取り消しイベントが開いている間は、実行が拒否されます。また、250行を超え、何かを削除するかレコードフォーマットを変更するスクリプトは、ユーザーがVectorworksで確認した後にのみ実行されます。

スクリプトは、今すぐ実行する場合も、後でパレットから実行する場合も、ユーザーの権限で動作します。実行のたびにユーザーに確認してスクリプトが何をするかを説明し、何をどこに保存したかをユーザーに伝えてください。このため、このグループのリスクレベルは`high`で、初期状態では無効です。ユーザーがスクリプトの実行、読み取り、作成、文書化を求めた場合にのみ使用してください。各saveScriptは、名前付きで取り消し可能な、独立したVectorworksの操作です。

> **注:** このグループが提供されるかどうかは、サーバーのツールモードによって決まります。「スクリプトツールのみを有効化」では、Core以外で唯一のグループになり、最初から有効です。「スクリプトツールを除くすべてを有効化」では、まったく提供されません。[ツールグループと有効化](Common.md#tool-groups-and-activation)を参照してください。

| ツール | 作用 | リスク | 概要 |
|---|---|---|---|
| [`listScripts`](#listscripts) | 読み取り専用 | 低 | ファイルのスクリプトリソースを一覧表示します。 |
| [`getScript`](#getscript) | 読み取り専用 | 低 | スクリプトリソースを実行せずに読み取ります。 |
| [`saveScript`](#savescript) | 編集 | 中 | Pythonスクリプトリソースを実行せずに作成または更新します。 |
| [`describePythonApi`](#describepythonapi) | 読み取り専用 | 低 | Pythonの`api`モジュール、またはその名前の1つのヘルプテキストを返します。 |
| [`getPythonApiGuide`](#getpythonapiguide) | 読み取り専用 | 低 | Pythonスクリプトを作成するためのガイドの1セクションを返します。 |
| [`runPythonScript`](#runpythonscript) | スクリプト実行 | 高 | Vectorworks内でPythonコードを実行します。 |
| [`runScript`](#runscript) | スクリプト実行 | 高 | 保存済みのPythonスクリプトリソースを実行します。 |

### listScripts

ファイルのスクリプトリソースを一覧表示します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

アクティブファイルのスクリプトリソースを名前順に一覧表示します: `name`、`language`（`python`または`vectorscript`）、`palette`（スクリプトを含むスクリプトパレットの名前）。`limit`（デフォルト200）と`offset`でページ分割されます。`count`は総数、`truncated`は続きがあるかどうかを示し、`countOnly`は件数だけを返します。何も実行も変更もされません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `limit` | integer |  | ページ分割: 返す項目の最大数（1以上）。デフォルトは200です。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割: スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割: 項目を含めず、件数だけを返します。 |

**結果**

| キー | 説明 |
|---|---|
| `scripts` | このページのスクリプトリソース。名前順の`{ "name", "language", "palette" }`のリストです。`language`は、読み取れない場合は`unknown`です。`countOnly`の場合は省略されます。 |
| `count`, `returned`, `offset`, `limit`, `truncated`, `nextOffset` | ページ分割のキー（[ページ分割](Common.md#paging)を参照）。 |

### getScript

スクリプトリソースを実行せずに読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

スクリプトリソース`name`（1～63文字）を読み取ります: `name`、`language`（`python`または`vectorscript`）、`palette`、およびLF改行の`text`。スクリプトは実行されません。エラー: `name`がない、空、文字列ではない、または63文字を超える場合。その名前のスクリプトリソースがない場合（同じ名前の登録ビューやその他のオブジェクトはスクリプトではありません）。スクリプトのテキストが256 KBを超える場合。

> **注:** スペースだけの`name`や、制御文字を含む`name`は、空の場合と同様に拒否されます。読み取りのエラーは、`script not found: <name>`、`the text of the script cannot be read: <name>`、`the script is larger than 256 KB (<n> bytes) and cannot be returned: <name>`です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string | はい | 1～63文字。 |

### saveScript

Pythonスクリプトリソースを実行せずに作成または更新します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ「MCP: saveScript」 · **runToolBatch内:** はい

**詳細**

Pythonスクリプトリソース`name`（1～63文字）を、`code`（UTF-8で最大256 KB、NUL文字なし）で作成または更新します。実行はしません。コードはPythonの`api`モジュール専用に記述してください。新しいスクリプトは、スクリプトパレット`palette`（1～63文字、デフォルト'MCP Scripts'）に作成されます。パレットがない場合は作成されて開かれます（`paletteCreated`: true）。

その名前のスクリプトが存在する場合は、テキストだけが置き換えられます。スクリプトのパレットと言語は維持され、指定した`palette`は無視されます（`paletteIgnored`: true）。既存のVectorScriptスクリプトは変更されません。`name`、`language`、`palette`、`created`、`codeLength`（`code`のUTF-8バイト数）を返します。スクリプトパレットは、Vectorworksでスクリプトが編集されるか、ファイルが開き直されるまで、以前に実行したスクリプトのコンパイル済みのコピーを実行し続けることがあります。

**エラー:** `name`、`code`、`palette`がない、文字列ではない、または制限を超える場合。`name`が別のオブジェクト（スクリプトパレットを含む）で使用されている場合。`palette`が`name`と同じ場合、またはスクリプトパレットではないオブジェクトの名前の場合。既存のスクリプトがVectorScriptスクリプトの場合。

> **注:** `palette`は省略可能です（デフォルト'MCP Scripts'）。エラーの文では「ない」場合も挙げていますが、形式のエラーは`palette`を指定した場合にのみ適用されます。新しいスクリプトを作成する場合、パレット（指定したもの、または'MCP Scripts'）と同じ`name`は、大文字小文字にかかわらず拒否されます。スクリプトパレット以外のオブジェクトが持つパレット名も拒否されます。既存のスクリプトでは、この2つの確認は省略されます。スペースだけの`name`や`palette`、または制御文字を含むものは拒否されます。スクリプトが存在し、`palette`を指定した場合（スクリプトを含むパレットを指定した場合も）、結果は`created`: false、`paletteIgnored`: true、および`note`を含みます。`paletteCreated`（true）は、新しいスクリプトのためにパレットが作成された場合にのみ返されます。空の`code`は受け付けられます。変更時のエラーは、`a script cannot have the name of its palette ('<palette>'); change 'name' or 'palette'`、`the name is the name of a script palette: <name>`、`the name is already used by another object of the document: <name>`、`the palette name is used by an object that is not a script palette: <palette>`、`failed to create the script '<name>' in the palette '<palette>'`、`the language of the script cannot be read: <name>`、`the script is a VectorScript script and is not changed (saveScript only changes Python scripts): <name>`、`failed to replace the text of the script: <name>`です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string | はい | 1～63文字。 |
| `code` | string | はい | UTF-8で最大256 KB。NUL文字は使用できません。 |
| `palette` | string |  | 1～63文字。デフォルトは'MCP Scripts'です。 |

### describePythonApi

Pythonの`api`モジュール、またはその名前の1つのヘルプテキストを返します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

スクリプトで使用するPythonの`api`モジュールを、固定の読み取り専用Pythonスクリプトで調べます。引数の内容がコードとして実行されることはありません。`name`（省略可能）は、`api`モジュールから解決されるドット区切りの名前で、先頭の`api.`は省略可能です: 数字で始まらない英字、数字、`_`からなる1～8個の部分で、最大128文字です。Pythonの名前にC++の接頭辞はありません: `CDocument`ではなく、`Document`、`Document.StartUndoEvent`、`WallObject.HeightBound`、`Math.Point2D`です。

`text`を返します: そのクラス、列挙型、関数、メンバーのヘルプを、pydocが出力するプレーンテキストで返します（定数は値を示し、サブモジュール`Math`は名前を一覧表示します）。256 KBで切り詰められます（`truncated`: true）。`name`を指定しない場合、`text`は`api`モジュールと`api.Math`モジュールの名前を種類別（モジュール、クラス、列挙型、関数、定数）に一覧表示します。クラス名を探すのに使用してください。

**エラー:** `name`が文字列ではないか、有効なドット区切りの名前ではない場合（スクリプトの実行前に拒否）。'unknown api name'。Pythonエンジンが現在実行できない場合（ファイルがない、他のスクリプトの実行中、エンジンが利用できない）、または検索に失敗した場合。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string |  | `api`モジュールから解決されるドット区切りの名前で、先頭の`api.`は省略可能です: 数字で始まらない英字、数字、`_`からなる1～8個の部分で、最大128文字です。省略すると、`text`はモジュールの名前を一覧表示します。空の文字列または`null`は、`name`なしとして扱われます。128文字には先頭の`api.`も含まれます。 |

**結果**

| キー | 説明 |
|---|---|
| `name` | 検索した名前（先頭の`api.`を除く）。`name`を指定した場合のみ。 |
| `text` | ヘルプテキスト。 |
| `truncated` | `text`が256 KBで切り詰められた場合は`true`。 |

### getPythonApiGuide

Pythonスクリプトを作成するためのガイドの1セクションを返します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

`api`モジュールを使用するVectorworksのPythonスクリプトを作成するためのガイドを、1回の呼び出しにつき1セクション、LF改行のMarkdownテキストで返します。何も実行も変更もされません。最初は`section`なしで呼び出してください。その場合、`text`はガイドの冒頭（タイトル、目次、はじめに）、`sections`はセクション1～6の一覧（`section`、`title`、およびテキストのサイズである`bytes`）で、`reference`はセクション7の参照先を示します。

セクション: 1 ルール、2 機能の場所、3 取り消し（最後にMCP経由で実行するスクリプトのルールを記載。最初のrunPythonScriptの前にセクション1と3を読んでください）、4 レシピ、5 ツール、メニュー、オブジェクト情報パレット、6 注意点。`section`（1～6の整数）を指定すると、そのセクションを返します: `section`、`title`、`text`（見出し'## n. 'から次のセクションまで）。

`text`が256 KBで切り詰められた場合、`truncated`はtrueです。セクション7（リファレンス）は返されません。ガイドがセクション7を参照している箇所や、別の.mdページにリンクしている箇所では、describePythonApiでクラス、関数、メンバーを調べてください。

**エラー:** `section`が1～6の整数ではない場合。セクション7。ガイドを利用できない場合（Vectorworksのアプリケーションリソースにない、有効なUTF-8ではない、または番号付きセクションのいずれかがない）。その場合はdescribePythonApiを使用してください。

> **注:** `null`の`section`は省略として扱われます。エラーは、`'section' must be an integer from 1 to 6`（`"3"`などの文字列や2.5などの数値の場合も）、`Section 7 (Reference) is not returned: look classes, functions and members up with describePythonApi`、`the Python api guide is not available: <reason>`です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `section` | integer |  | 1～6の整数。 |

### runPythonScript

Vectorworks内でPythonコードを実行します。

> **作用:** スクリプト実行 · **リスク:** 高 · **取り消し:** 1ステップ「MCP: script」（スクリプトが変更を登録しなかった場合はなし） · **runToolBatch内:** 不可

**詳細**

`code`をVectorworks内でPythonスクリプトとして実行します: UTF-8で最大256 KB、NUL文字なし。

**高リスク:** 実行のたびに、スクリプトが何をするかをユーザーに伝え、許可を求めてください。コードはPythonの`api`モジュール専用に記述し（import api。`vs`は使用しない）、その名前をdescribePythonApiで調べてください（C++の接頭辞なし: api.CDocumentではなくapi.Document）。結果をJSONとして出力する（print(json.dumps(...))）と、`output`で受け取れます。最初の実行の前に、getPythonApiGuideでガイドのセクション1と3を読んでください。セクション3の最後には、MCP経由で実行するスクリプトのルールが記載されています。

**取り消し:** 実行全体が「MCP: script」という1つの取り消しステップになり（スクリプトが変更を登録しなかった場合はなし。Vectorworksは空のステップを残しません）、スクリプト自身のStartUndoEvent、NameUndoEvent、EndUndoEvent、RevertUndoEventの呼び出しは無視されます。スクリプトは、作成したもの（作成後にdoc.AddAfterSwapObject(obj.GetHandle())）と変更するもの（変更の前にdoc.AddBothSwapObject(handle)）を登録する必要があります。登録しないと、取り消しで元に戻せません。Delete()は登録不要です。失敗した実行は元に戻される（`rolledBack`: true、取り消しステップなし）ため、登録したものは何も残りません。スクリプトを修正して再度実行してください。スクリプトが登録しなかった変更は元に戻せません。ユーザー入力（GetPt、ダイアログ）は決して待たないでください。待つと、実行は`Waiting`として終了し、ユーザーが完了するまでどのスクリプトも実行できません。スクリプトはVectorworksのメインスレッドで実行されるため、無限ループはVectorworksを停止させます。他のスクリプトの実行中や、取り消しイベントが開いている間（Vectorworksの別の操作が進行中です。後で再試行してください）は、スクリプトは実行されません（`NotStarted`、取り消しステップなし）。250行を超え、何かを削除するかレコードフォーマットを変更するスクリプトは、ユーザーがVectorworksの警告で実行を選択した後にのみ実行されます。キャンセルした場合、または現在警告を表示できない場合は、理由とともに`NotStarted`を返します。この確認を回避しないでください。`status`（Succeeded、Failed、NotStarted、Waiting）、`output`（出力されたテキスト）、`errors`（トレースバック）を返し、それぞれ256 KBで切り詰められます（`outputTruncated`、`errorsTruncated`）。さらに、`undoStep`（実行で取り消しステップ`undoName`が残った場合はtrue。変更を登録しなかった場合、失敗した場合、開始しなかった場合はfalse）、失敗した実行や開始しなかった実行の`rolledBack`（登録したものが元に戻された場合はtrue）、スクリプトが失敗したか実行されなかった場合の`err`、Waitingの場合の`note`、および実行後も取り消しイベントが開いている場合の`warning`を返します。

**エラー:** `code`がない、空、文字列ではない、256 KBを超える、またはNUL文字を含む場合。

> **注:** `rolledBack`は、開始した実行についてのみ返されます。開始前に拒否された実行（他のスクリプトの実行中、取り消しイベントが開いている、ユーザーが確認をキャンセルした、または警告が抑制されている）は、`status`が`NotStarted`で`err`がありますが、`rolledBack`はありません。何も開かれていないため、何も元に戻されていません。

> **注:** 無視されるのは`api.Document`の取り消しメソッドだけです。`vs`モジュールの取り消しの呼び出しはVectorworksに直接届くため、それを使用するスクリプトは、実行の取り消しステップの名前を変更したり、取り消しステップを終了したりできます。`warning`は、実行後もまだ開いている取り消しイベントを報告します。

> **注:** 実行の`err`は、`the script failed: `、`the script does not compile: `、または`the script did not run: `で始まり、その後に理由が続きます。300バイトで切り詰められます。

> **注:** 確認は、コメントと文字列を含むスクリプトの、大文字小文字を区別する単純なテキスト検索です。250行を超え（CRLF、CR、LFがそれぞれ行の終わり）、`.Delete(`、`DeleteSelection(`、`vs.DelObject`、`vs.DelRecord`、`RecordFormat.Create(`、`AddField(`、`RemoveField(`、`RenameField(`、`SetFieldDefaultValue(`、`SetFieldChoices(`のいずれかを含むスクリプトにのみ適用されます。

> **注:** このツールは、実行前後の取り消し履歴を取り消しイベントのIDで比較します: `undoName`は実行で追加された最新の取り消しステップで、通常は`MCP: script`です（`vs`モジュールの取り消しの呼び出しでステップの名前を変更するスクリプトでは、新しい名前が報告されます）。取り消し履歴を読み取れない場合は、ステップがあるものとみなされ、`undoStep`はtrueになります。成功した実行の後に`undoStep`がfalseの場合、編集 &gt; 取り消しは実行前のステップを元に戻します。`Waiting`として終了した実行も、その取り消しステップを終了します。入力の後にスクリプトが行う変更は、そのステップに含まれません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `code` | string | はい | 空ではなく、UTF-8で最大256 KB、NUL文字なし。 |

### runScript

保存済みのPythonスクリプトリソースを実行します。

> **作用:** スクリプト実行 · **リスク:** 高 · **取り消し:** 1ステップ「MCP: script」（スクリプトが変更を登録しなかった場合はなし） · **runToolBatch内:** 不可

**詳細**

保存済みのPythonスクリプトリソース`name`（1～63文字。saveScriptで保存したものなど）の現在のテキストを、runPythonScriptが`code`を実行するのと同じ方法で実行します: 変更を登録した場合は「MCP: script」という1つの取り消しステップになり、失敗した実行は元に戻される（`rolledBack`）ため、登録したものは何も残りません。スクリプトを修正（saveScript）して再度実行してください。スクリプトが登録しなかった変更は元に戻せません。

スクリプトに対するルール、拒否、確認（スクリプトのテキストを検査します）、および結果は同じで、結果には`name`が加わります。

**高リスク:** 実行のたびに、どのスクリプトを実行し、それが何をするかをユーザーに伝え、許可を求めてください。

**エラー:** `name`がない、空、文字列ではない、または63文字を超える場合。その名前のスクリプトリソースがない場合（同じ名前の登録ビューやその他のオブジェクトはスクリプトではありません）。スクリプトがVectorScriptスクリプトの場合（実行されるのはPythonスクリプトだけです）。

> **注:** スペースだけの`name`や、制御文字を含む`name`は、空の場合と同様に拒否されます。エラーのテキストは、`script not found: <name>`、`the script cannot be read: <name>`、`the script is a VectorScript script and is not run (runScript runs only Python scripts): <name>`です。確認の警告が開いている間にスクリプトが削除されたか名前が変更された場合、結果は`The script '<name>' was deleted or renamed before it could run.`を伴う`NotStarted`になります。結果には`name`も含まれます。`rolledBack`、`vs`モジュールの取り消しの呼び出し、確認の検索、`undoStep`についての[runPythonScript](#runpythonscript)の注は、ここにも適用されます。空の保存済みスクリプト（`The script is empty.`）や、確認中に削除または名前が変更されたスクリプトは、取り消しステップが開かれた後に`NotStarted`で終了するため、その結果には`rolledBack`が含まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string | はい | 1～63文字。 |
