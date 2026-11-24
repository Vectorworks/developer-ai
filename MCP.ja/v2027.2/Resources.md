[English](../../MCP/v2027.2/Resources.md) • [Deutsch](../../MCP.de/v2027.2/Resources.md) • **日本語**

# Resources — リソースとワークシート

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

図面のリソースと外部コンテンツ（ライブラリ、ディスク上のファイル、開いている他のファイル）のリソース、およびワークシートのためのツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [Resources](#resources)
  - [getResourceTypes](#getresourcetypes)
  - [getResources](#getresources)
  - [getResource](#getresource)
  - [importResource](#importresource)
  - [editResource](#editresource)
  - [createResource](#createresource)
  - [getResourceDetails](#getresourcedetails)
  - [setResourceDetails](#setresourcedetails)
  - [applyResource](#applyresource)
  - [getWorksheet](#getworksheet)
  - [editWorksheet](#editworksheet)

<a id="overview"></a>

## 概要

このフォルダには1つのツールグループがあり、合計11個のツールを提供します。

| グループ | グループID | 初期状態で有効 | リスクレベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [Resources](#resources) | `resources` | いいえ | 中 | 11 | リソースを一覧表示、取り込み、作成、確認、編集、適用し、ワークシートを読み取り、編集します。 |

## Resources

> **グループ:** `Resources` · **グループID:** `resources` · **初期状態で有効:** いいえ · **リスクレベル:** 中 · **ツール数:** 11

**リソースを一覧表示、取り込み、作成、確認、編集、適用し、ワークシートを読み取り、編集します。**

Vectorworksのリソースを一覧表示、確認、取り込み、編集します: シンボル定義、ハッチング、グラデーション、イメージ、タイル、ラインタイプ、テクスチャ、レンダリングスタイルと背景テクスチャ、レコードフォーマット、ワークシート、文字スタイル、壁／スラブ／屋根／ビューポートのスタイル、データの可視化、マテリアル、クラス、リソースフォルダ。リソースは現在の図面または外部コンテンツ（Vectorworksライブラリ、ディスク上のファイル、開いている他のファイル）から一覧表示し、図面に取り込みます。

植栽スタイル、図面枠スタイル、データタグスタイルは独立したリソースタイプではないことに注意してください。いずれもコンテンツフォルダ（plantStyles / plantLibraries、titleBlocks、objectStyles）に保存されている`symbolDefinition`なので、resourceTypeを`symbolDefinition`にし、対応する`folder`を指定して一覧表示と取り込みを行います。getResourcesのスキーマには、すべての`resourceType`と`folder`の名前が既に列挙されています。getResourceTypesは、各リソースタイプのノードタイプを確認する場合にだけ呼び出してください。

標準またはカスタムのIFCプロパティセットは、レコードフォーマットではなくIFCグループ（listIFCPsets、getIFCPsetDefinition）で扱います。データマネージャのIFCマッピングとIFC取り出し設定は、ResourcesやIFCのツールでは公開されていません。getObjectIFCDataは、オブジェクトにマッピングされたIFCエンティティと、そのIFC値のうちマッピングから得られるものだけを返します。ワークシートは、getWorksheetとeditWorksheetで完全に読み取り、編集できます: セルの書式、枠線、統合したセル、列幅、行の高さ、データベース行とそのサブ行、再計算。

各変更は、名前付きで取り消し可能な独立したVectorworksの操作として実行されます。

> **注:** getResources、importResource、createResourceの`resourceType`は、大文字小文字を区別せずに、getResourceTypesが列挙する名前と次の別名に照合されます: `plantStyle`、`plant`、`titleBlockStyle`、`titleBlock`、`dataTagStyle`、`dataTag`、`symbol`、`objectStyle`（すべて`symbolDefinition`の意味）、`record`と`format`（`recordFormat`）、`material`（`buildingMaterial`）、`image`（`imageFill`）、`font`（`textStyle`）、`background`（`renderBackground`）。末尾の`s`は1つだけ無視されます（`textures`は`texture`）。`hatches`は受け付けられないため、`hatch`を使用してください。不明な名前は失敗し、メッセージに有効な名前が列挙されます。

| ツール | 作用 | リスク | 概要 |
|---|---|---|---|
| [`getResourceTypes`](#getresourcetypes) | 読み取り専用 | 低 | リソースタイプと標準コンテンツフォルダを一覧表示します。 |
| [`getResources`](#getresources) | 読み取り専用 | 低 | 図面、ライブラリ、ディスク上のファイル、または開いている他のファイルから、1つのタイプのリソースを一覧表示します。 |
| [`getResource`](#getresource) | 読み取り専用 | 低 | 図面のリソースを1つ読み取ります。 |
| [`importResource`](#importresource) | 編集 | 中 | 外部のリソースを図面に取り込みます。 |
| [`editResource`](#editresource) | 編集 | 中 | リソースの名前変更、説明の設定、移動、複製、削除を行います。 |
| [`createResource`](#createresource) | 編集 | 中 | 空のリソースを作成します。 |
| [`getResourceDetails`](#getresourcedetails) | 読み取り専用 | 低 | ハッチングのレベル、グラデーションの変化点、ラインタイプの破線など、リソースの内容を読み取ります。 |
| [`setResourceDetails`](#setresourcedetails) | 編集 | 中 | リソースの内容を変更します。 |
| [`applyResource`](#applyresource) | 編集 | 中 | テクスチャ、スタイル、データの可視化をオブジェクトに適用します。 |
| [`getWorksheet`](#getworksheet) | 読み取り専用 | 低 | ワークシートのサイズ、セル、書式、データベース行を読み取ります。 |
| [`editWorksheet`](#editworksheet) | 編集 | 中 | アクションのリストでワークシートを変更します。 |

### getResourceTypes

リソースタイプと標準コンテンツフォルダを一覧表示します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

このAPIが認識するリソースタイプ（`resourceType`の値とそのノードタイプ）と、Vectorworksの標準コンテンツフォルダの名前（`folder`の値）を一覧表示します。引数はありません。

**パラメータ**

このツールにパラメータはありません。

**結果**

| キー | 説明 |
|---|---|
| `resourceTypes` | リソースタイプ。それぞれ`{ name, type }`の形式で、`name`は`resourceType`引数の値、`type`はノードタイプの番号です。 |
| `contentFolders` | 標準コンテンツフォルダ（標準リソースのフォルダ）の名前: [getResources](#getresources)の`folder`引数の値です。 |

### getResources

図面、ライブラリ、ディスク上のファイル、または開いている他のファイルから、1つのタイプのリソースを一覧表示します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

1つの`resourceType`のリソースを一覧表示します。`source`で取得元を選択します: "document"（現在の図面。デフォルト）、"library"（`folder`で指定する標準コンテンツフォルダ。`subFolder`で絞り込み、`includeDocument`で現在の図面のリソースも加えることができます）、"file"（OS形式の完全パス`filePath`で指定する1つのVectorworksファイル）、"openDocument"（`openDocumentIndex`）。

各項目は、一覧内の`index`、`name`、`actualName`、`folder`、および`isInDocument`（図面にあるかどうか）を返します。`limit`（デフォルト200）と`offset`で一覧をページ分割します: `count`はリソースの総数、`returned`は一覧表示した数で、続きがある場合は`truncated`がtrueになります（`nextOffset`）。`countOnly`は`count`だけを返します。内部用のIFCレコードフォーマットは、件数と上限を適用する前に除外されます。

> **注:** `countOnly`で省略されるのは`resources`の一覧だけです: 結果には引き続き`count`、`returned`（0）、`offset`、`limit`、`truncated`、`resourceType`が含まれます。`nextOffset`は`truncated`がtrueの場合にだけ含まれます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `resourceType` | string | はい | リソースの種類。植栽スタイル、図面枠スタイル、データタグスタイルは独立したタイプではなく、plantStyles / plantLibraries、titleBlocks、objectStylesのコンテンツフォルダに保存されている"symbolDefinition"リソースです。次のいずれか: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`。 |
| `source` | string |  | 次のいずれか: `document`, `library`, `file`, `openDocument`。 |
| `folder` | string |  | sourceが"library"の場合に一覧表示する、Vectorworksの標準コンテンツフォルダ。次のいずれか: `objectLibraries`, `libraries`, `defaults`, `textures`, `gradients`, `hatches`, `imageFills`, `plantStyles`, `renderBackgrounds`, `titleBlocks`, `reports`, `sketchStyles`, `tiles`, `textStyles`, `renderStyles`, `lineTypes`, `recordFormats`, `objectStyles`, `materials`, `wallStyles`, `roofStyles`, `slabStyles`, `plantLibraries`。 |
| `subFolder` | string |  | コンテンツフォルダ`folder`のサブフォルダ。`source`が`library`の場合に一覧を絞り込みます。 |
| `filePath` | string |  | ファイルの完全パス。 |
| `openDocumentIndex` | integer |  | `source`が`openDocument`の場合に一覧表示する、開いているファイル。 |
| `includeDocument` | boolean |  | `source`が`library`の場合に、現在の図面のリソースも一覧表示します。 |
| `sort` | boolean |  | 一覧を並べ替えます（デフォルトtrue）。`source`が`file`の場合は使用されません。 |
| `limit` | integer |  | ページ分割: 返す項目の最大数（1以上）。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割: スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割: 項目を含めず、件数だけを返します。 |

**結果**

| キー | 説明 |
|---|---|
| `resources` | 項目のページ。`countOnly`では省略されます。各項目には`index`（一覧内の位置）、`name`、`actualName`、`folder`（空でない場合のみ）、`isInDocument`が含まれます。`uuid`は`isInDocument`がtrueの場合にだけ含まれます。 |
| `resourceType` | 一覧表示したリソースタイプの名前。 |
| `count`、`returned`、`offset`、`limit`、`truncated`、`nextOffset` | [ページ分割](Common.md#paging)で説明しているページ情報。 |

エラー: `unknown resourceType '<x>'`と`unknown content folder '<x>'; expected one of: <names>`、`unknown source: <x>`、`'folder' is required when source is 'library'; expected one of: <names>`、`filePath is required when source is 'file'`、`failed to build the resource list`（コンテンツがインストールされていないか、ファイルを開けなかった可能性があるというヒント付き）。

### getResource

図面のリソースを1つ読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

現在の図面のリソースを、uuid、名前、または内部インデックスで1つ読み取ります: タイプ、名前、説明、リソースフォルダ（`folder`の名前と`parentFolder`の参照）、およびシンボル定義とリソースフォルダの場合はそれに含まれるオブジェクト。代わりに`objectUuid`を指定すると、そのオブジェクトが使用しているリソースを返します: `styles`（オブジェクトが従う文字、壁、スラブ、屋根、ビューポートのスタイル。独自の設定を使用している場合は空）と`activeDataVisualizations`（ビューポート、登録ビュー、デザインレイヤで有効なデータの可視化。ある場合のみ）。

内部用のIFCレコードフォーマットは拒否されます。代わりにIFCツールを使用してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `objectUuid` | string |  | 対象オブジェクトのUUID。 |

**結果**

`objectUuid`を指定した場合（`uuid`、`name`、`index`より優先されます）:

| キー | 説明 |
|---|---|
| `object` | オブジェクト（[オブジェクト参照](Common.md#object-references)を参照）。 |
| `styles` | オブジェクトが従うリソース。文字スタイル、壁スタイル、スラブスタイル、屋根スタイル、ビューポートスタイルの順のリソース参照です。従うものがない場合は空です。 |
| `activeDataVisualizations` | オブジェクトで有効なデータの可視化の名前。ない場合は省略されます。 |

それ以外の場合は、リソース参照と次のキー:

| キー | 説明 |
|---|---|
| `parentFolder` | リソースを格納しているリソースフォルダ（リソース参照）。最上位の場合は省略されます。 |
| `contents` | シンボル定義またはリソースフォルダの場合: それに含まれるオブジェクト（オブジェクト参照）。 |

リソース参照は、オブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）に、`resourceType`、`description`（空でない場合）、`folder`（リソースフォルダの名前。空でない場合）、`internalIndex`（リソースにある場合）、`contentCount`（シンボル定義とリソースフォルダ）を加えたものです。このページの他のツールも同じ参照を返します。

エラー: `resource not found`、`not a resource`、`object not found: <uuid>`、内部用のIFCレコードフォーマットの拒否。

### importResource

外部のリソースを図面に取り込みます。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ「MCP: importResource」 · **runToolBatch内:** はい

**詳細**

外部のリソースを現在の図面に取り込み、そのリソースを返します。getResourcesと同じ方法で一覧を作成し、`name`または一覧内の`index`でリソースを選択します。`onConflict`は、図面に同じ名前のリソースが既にある場合の処理を決めます: rename（デフォルト）、replace、doNotImport、askWithUI。図面に既にあったリソースが返された場合（元から図面にあった場合、または名前の競合時にdoNotImportを指定した場合）、結果の`imported`はfalseです。

`classRenamePrefix`は、リソースと共に取り込まれるクラスに接頭辞を付けます。内部用のIFCレコードフォーマットは拒否されます。代わりにIFCツールを使用してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `resourceType` | string | はい | リソースの種類。植栽スタイル、図面枠スタイル、データタグスタイルは独立したタイプではなく、plantStyles / plantLibraries、titleBlocks、objectStylesのコンテンツフォルダに保存されている"symbolDefinition"リソースです。次のいずれか: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`。 |
| `source` | string |  | 次のいずれか: `document`, `library`, `file`, `openDocument`。 |
| `folder` | string |  | sourceが"library"の場合に一覧表示する、Vectorworksの標準コンテンツフォルダ。次のいずれか: `objectLibraries`, `libraries`, `defaults`, `textures`, `gradients`, `hatches`, `imageFills`, `plantStyles`, `renderBackgrounds`, `titleBlocks`, `reports`, `sketchStyles`, `tiles`, `textStyles`, `renderStyles`, `lineTypes`, `recordFormats`, `objectStyles`, `materials`, `wallStyles`, `roofStyles`, `slabStyles`, `plantLibraries`。 |
| `subFolder` | string |  | コンテンツフォルダ`folder`のサブフォルダ。`source`が`library`の場合に一覧を絞り込みます。 |
| `filePath` | string |  | ファイルの完全パス。 |
| `openDocumentIndex` | integer |  | `source`が`openDocument`の場合に一覧表示する、開いているファイル。 |
| `includeDocument` | boolean |  | `source`が`library`の場合に、現在の図面のリソースも一覧表示します。 |
| `sort` | boolean |  | 一覧を並べ替えます（デフォルトtrue）。`source`が`file`の場合は使用されません。 |
| `name` | string |  | 取り込むリソースの名前。`index`より優先されます。 |
| `index` | integer |  | リソースの一覧内の`index`（[getResources](#getresources)を参照）。`name`がない場合に使用されます。 |
| `onConflict` | string |  | 次のいずれか: `rename`, `replace`, `doNotImport`, `askWithUI`。 |
| `classRenamePrefix` | string |  | リソースと共に取り込まれるクラスの名前に付ける接頭辞。 |

**結果**

取り込んだリソースのリソース参照（[getResource](#getresource)を参照）と、次のキー:

| キー | 説明 |
|---|---|
| `imported` | 図面に既にあったリソースが代わりに返された場合はfalse（元から図面にあった場合、または`doNotImport`で名前が競合した場合）。 |
| `note` | `imported`がfalseの場合のみ: `the resource was already in the drawing; it was returned instead of being imported`。 |

エラー: 一覧の引数についてのgetResourcesのエラー、`name or index is required`、`resource not found`（一覧にその`name`または`index`の項目がない）、`failed to import the resource`、内部用のIFCレコードフォーマットの拒否。失敗した呼び出しはロールバックされます（`rolledBack`）。

### editResource

リソースの名前変更、説明の設定、移動、複製、削除を行います。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ「MCP: editResource」 · **runToolBatch内:** はい

**詳細**

現在の図面のリソースを、uuid、名前、または内部インデックスで指定して1つ編集します。`action`: modify（デフォルト。`newName`で名前を変更し、`description`を設定し、`folder`で指定した名前のリソースフォルダに移動）、duplicate（`newName`で名前を付けることも可能）、delete。内部用のIFCレコードフォーマットは拒否されます。代わりにIFCツールを使用してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `action` | string |  | 次のいずれか: `modify`, `duplicate`, `delete`。 |
| `newName` | string |  | 新しい名前。 |
| `description` | string |  | 説明文。 |
| `folder` | string |  | リソースの移動先となる既存のリソースフォルダの名前（`modify`）。空の名前、またはどのオブジェクトにもない名前は失敗する（`resource folder not found: <folder>`）ため、これでリソースを最上位に移動することはできません。リソースフォルダでないオブジェクトの名前では、`applied.folder`がfalseになります。 |

**結果**

| アクション | 結果 |
|---|---|
| `modify`（デフォルト） | `resource`（リソース参照。[getResource](#getresource)を参照）と`applied`: 指定した`newName`、`description`、`folder`のそれぞれについて、書き込まれたかどうか。 |
| `duplicate` | 複製のリソース参照。`newName`を指定すると複製にその名前が付きます。名前を設定できない場合（既に使われているなど）、複製は複製時に付けられた名前のままになり、このことは報告されません。 |
| `delete` | `deleted`: 何も削除されなかった場合はfalse。これはエラーではありません。 |

エラー: `resource not found`、`not a resource`、`unknown action: <action>`、`resource folder not found: <folder>`、`failed to duplicate the resource`、内部用のIFCレコードフォーマットの拒否。失敗した呼び出しはロールバックされます（`rolledBack`）。

### createResource

空のリソースを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ「MCP: createResource」 · **runToolBatch内:** はい

**詳細**

現在の図面に、`resourceType`の空のリソースを`name`という名前で作成します。名前が既に使われている場合、ほとんどのタイプではVectorworksが番号を付加するため、返された名前を確認してください。文字、壁、スラブ、屋根のスタイルとレコードフォーマットでは、代わりにそのタイプの既存のリソースを返し、結果の`created`はfalseになります。既に使われている単一のフォルダ名は失敗します。

**タイプ別の追加引数:** hatch - `usePageUnits`、`transparent`、`backgroundColor`。lineType - `dashPattern`（線と空白の長さを交互に指定。単一のラインタイプを作成）と`scaleWithLineWeight`、または複合のラインタイプではパターンなし。renderBackground - `kind`。worksheet - `rows`、`columns`。folder - `contentType`（フォルダに格納するリソースタイプ。'/'を含む名前は入れ子のフォルダを作成し、その場所に同じタイプのフォルダとして既にあるパス内のフォルダは再利用し、パス内の名前が他のものに使われている場合は失敗します）。imageFill - `pngBase64`（PNGファイルのバイト列をbase64エンコードしたもの）と必須の`folder`（イメージを受け取る、イメージ用のリソースフォルダ。存在しない場合は作成）。その`name`は使用中であってはなりません。ここに挙げていないタイプ（texture、symbolDefinition、recordFormat、gradient、tile、textStyle、wallStyle、slabStyle、roofStyle）は名前だけが必要です。それ以外のタイプはimportResourceで取り込む必要があります。内部用のIFCレコードフォーマットは拒否されます。代わりにIFCツールを使用してください。

> **注:** ワークシートでも、`name`が既存のワークシートに使われている場合はそのワークシートを返します（`created`はfalse）。この場合も`rows`と`columns`は1以上である必要がありますが、値は使用されません。新しいワークシートは、`rows`と`columns`で指定しない限り20行10列です。どちらも1以上である必要があります。
>
> **注:** 単一のラインタイプ（`dashPattern`を指定）には名前がありません: スキーマでは必須ですが、`name`は無視されます。単一のラインタイプは破線パターンごとに共有されるため、結果は同じパターンを持つ既存のラインタイプである場合があります。新規かどうかは報告されません: 結果には`created`キーがなく、`note`だけがあります。`dashPattern`の数値でない項目はスキップされます。数値が1つもないパターンや、10個を超える数値を持つパターンは失敗します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `resourceType` | string | はい | リソースの種類。植栽スタイル、図面枠スタイル、データタグスタイルは独立したタイプではなく、plantStyles / plantLibraries、titleBlocks、objectStylesのコンテンツフォルダに保存されている"symbolDefinition"リソースです。次のいずれか: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`。 |
| `name` | string | はい | 新しいリソースの名前。フォルダの場合、'/'を含む名前は入れ子のフォルダのパスです。単一のラインタイプでは無視されます。imageFill: 他のどのオブジェクトにも使われていない名前で、`folder`とも異なる必要があります。 |
| `description` | string |  | 説明文。 |
| `usePageUnits` | boolean |  | ハッチング: ハッチングをページ単位（縮尺無視）でサイズ設定するかどうか（デフォルトfalse）。 |
| `transparent` | boolean |  | ハッチング: ハッチングの`transparent`設定（デフォルトtrue）。 |
| `backgroundColor` | [色](Common.md#colors) |  | ハッチング: 背景色。 |
| `dashPattern` | array of number |  | 線と空白の長さを交互に指定します（1～10個の数値）。単一のラインタイプを作成します。 |
| `scaleWithLineWeight` | boolean |  | `dashPattern`を指定したラインタイプ: 破線を線の太さに連動させるかどうか。 |
| `kind` | string |  | 次のいずれか: `clouds`, `oneColor`, `twoColor`, `physicalSky`。デフォルト`oneColor`。 |
| `rows` | integer |  | ワークシート: 行数（デフォルト20、1以上）。 |
| `columns` | integer |  | ワークシート: 列数（デフォルト10、1以上）。 |
| `contentType` | string |  | フォルダ（`resourceType`が`folder`の場合は必須）: フォルダに格納するリソースタイプ。指定がないか不明な値の場合は`unknown contentType '<x>'; expected one of: ...`で失敗します。次のいずれか: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`。 |
| `pngBase64` | string |  | PNGファイルのバイト列をbase64エンコードしたもの。データURLの接頭辞（`data:image/png;base64,`）も受け付けます。 |
| `folder` | string |  | イメージを受け取る、イメージ用のリソースフォルダ。存在しない場合は作成されます。 |

**結果**

リソースのリソース参照（[getResource](#getresource)を参照）と、次のキー:

| キー | 説明 |
|---|---|
| `created` | 同じ名前の既存のリソースが返された場合はfalse（スタイル、レコードフォーマット、ワークシート）。単一のラインタイプでは含まれません。 |
| `note` | 既存のリソースが返された場合のみ: `a <type> resource named '<name>' already exists; it was returned instead of a new one`。単一のラインタイプの場合: 結果が同じパターンを持つ既存のラインタイプである可能性があること。 |
| `details` | [getResourceDetails](#getresourcedetails)がリソースについて返す内容: リソースタイプ別の設定。 |

エラー: `unknown resourceType '<x>'`と`unknown contentType '<x>'`（メッセージに有効な名前が列挙されます）、`unknown render background kind: <x>`、`creating a <type> resource is not supported; import one instead`、`failed to create the <type> resource`、`an imageFill needs 'folder': the name of a resource folder for image fills (created when missing)`（`folder`がイメージ用のリソースフォルダでないオブジェクトを指す場合も）、`'pngBase64' must hold a PNG file encoded as base64`、`an imageFill needs a 'name' that no other object uses`、`failed to create an image fill from the PNG data`、`failed to register the new folders of '<name>' with Undo; they were removed again`、`failed to register the new folder '<name>' with Undo; it was removed again`、内部用のIFCレコードフォーマットの拒否、設定できない`description`。失敗した呼び出しはロールバックされます（`rolledBack`）。

新しいリソースを取り消しに登録できない場合、呼び出しは失敗します。新しいフォルダ（またはパスの新しいフォルダ）は再び削除されます。その他の新しいリソースは、呼び出しが`err`と`rolledBack`を返しても図面に残ります: メッセージは`was created but could not be registered with Undo, so it stays in the document`となります。

### getResourceDetails

ハッチングのレベル、グラデーションの変化点、ラインタイプの破線など、リソースの内容を読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

1つのリソースが名前以外に持つ内容を読み取ります: ハッチングのレベルと設定、グラデーションの変化点、タイルの間隔、図形の数と`geometryGroup`、イメージのピクセルサイズ、単一のラインタイプの破線パターン、または複合のラインタイプの図形の数と`geometryGroup`、シンボル定義の種類と挿入設定および`active`なシンボルかどうか、テクスチャのサイズ、レコードフォーマットのフィールド（フィールドの`type`はtext、integer、popUpなどのVectorworksのレコードフィールドタイプで、IFCタイプではありません）、ワークシートのサイズとセル、リソースフォルダの内容、ビューポートスタイルの`activeDataVisualizations`。

`geometryGroup`は、繰り返される2Dオブジェクトを格納するグループを参照します。ワークシートでは、`topLeft`と`bottomRight`の一方または両方を渡すと、その範囲のセル（数式、表示テキスト、および数値の場合は書式なしの`value`）を読み取ります。指定しない場合はサイズだけを返します。getWorksheetは、書式、サイズ、統合したセル、データベースのサブ行も読み取ります。dataVisualizationでは、ファイル内のすべてのデータの可視化の名前だけを返します（検索条件やマッピングは含みません）。buildingMaterial、class、renderBackground、renderStyle、roofStyle、slabStyle、textStyle、wallStyleのリソースでは、空の`details`を返します。

グラフィック属性（線、面など）を持つリソースの属性は、リソースのuuidを指定して、ObjectsグループのgetObjectAttributes / setObjectAttributesで読み取り、設定します。内部用のIFCレコードフォーマットは拒否されます。代わりにIFCツールを使用してください。

> **注:** ワークシートでは、最初に範囲内のすべてのセルの`formula`と`text`を読み取り、次に数値の各セルの`value`を読み取ります。再計算待ちのセルの`value`を読み取ると、Vectorworksはまずワークシート全体を再計算し、その際RUNSCRIPT数式のスクリプトも実行されます。その後の`value`は最新ですが、セルの`text`はその再計算前の表示テキストのままの場合があります。getWorksheetは再計算しません: そのようなセルについては`value`の代わりに`needsRecalculation`を返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `topLeft` | object |  | ワークシート: 読み取る範囲の最初のセル（`{ row, column }`の形式）。`bottomRight`だけを指定した場合のデフォルトは行1、列1。 |
| `topLeft.row` | integer |  | セルの行（1が最初の行）。 |
| `topLeft.column` | integer |  | セルの列（1が最初の列）。 |
| `bottomRight` | object |  | ワークシート: 読み取る範囲の最後のセル（`{ row, column }`の形式）。`topLeft`だけを指定した場合のデフォルトは最後の行と列。 |
| `bottomRight.row` | integer |  | セルの行（1が最初の行）。 |
| `bottomRight.column` | integer |  | セルの列（1が最初の列）。 |

**結果**

リソースのリソース参照（[getResource](#getresource)を参照）と`details`。`details`のキーはリソースのタイプによって異なり、値を読み取れたキーだけが含まれます。

| 種類 | `details`のキー |
|---|---|
| `hatch` | `usePageUnits`、`transparent`、`rotateInWalls`、`rotateInSymbols`、`levels`: レベルごとに1項目で、`startPoint`、`repeatVector`、`offsetVector`、`dashFactor`、`color`、`lineWeightMils`を持ちます。 |
| `gradient` | `segments`: 変化点ごとに1項目で、`spotPosition`、`midpointPosition`、`color`、`opacity`を持ちます。 |
| `tile` | `offset`、`repetition`、`usePageUnits`、`transparentBackground`、`backgroundColor`、`rotateInWalls`、`rotateInSymbols`、`geometryCount`、`geometryGroup`（タイルにある場合はオブジェクト参照）。 |
| `imageFill` | `widthPixels`、`heightPixels`、`compression`。 |
| `lineType` | `simple`。単一のラインタイプでは`dashPattern`と`scaleWithLineWeight`、複合のラインタイプでは`gapSize`、`usePageUnits`、`geometryCount`、`geometryGroup`が加わります。 |
| `symbolDefinition` | `geometryType`、`canInsertIntoWalls`、`containsLight`、`pageBased`、`insertAsGroup`、`insertMode`、`breakMode`、`active`。 |
| `texture` | `size`、`uvAspectRatio`。 |
| `recordFormat` | `localizedName`、`parametric`、`visible`、`fields`: フィールドごとに1項目で、`name`、`localizedName`、`type`、`defaultValue`、およびポップアップフィールドでは`choices`を持ちます。 |
| `worksheet` | `rows`、`columns`。`topLeft`または`bottomRight`を指定すると`cells`も含まれます: 範囲内で数式またはテキストを持つセル（空のセルと、`rows`または`columns`を超えるセルは省略されます。`topLeft`または`bottomRight`の行または列が1未満の場合、または`bottomRight`が`topLeft`より上か左にある場合、`cells`は空です）。各セルは`row`、`column`、`formula`、`text`、および数値の場合は`value`を持ちます。 |
| `folder` | `contentType`（格納するリソースタイプ）と`resources`（格納するリソースのリソース参照。内部用のIFCレコードフォーマットは省略されます）。 |
| `viewportStyle` | `activeDataVisualizations`。 |
| `dataVisualization` | `allNames`。 |
| その他のタイプ | `{}`（空）。 |

エラー: `resource not found`、`not a resource`、内部用のIFCレコードフォーマットの拒否。

### setResourceDetails

リソースの内容を変更します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ「MCP: setResourceDetails」 · **runToolBatch内:** はい

**詳細**

uuid、名前、または内部インデックスで指定したリソースの内容を変更します。

**タイプ別:** hatch - `usePageUnits`、`transparent`、`rotateInWalls`、`rotateInSymbols`、`levels`（各レベルはstartPoint、repeatVector（線の方向と破線パターンの繰り返しの長さ）、offsetVector（次の平行線までの間隔）、dashFactor（各繰り返しのうち描画する割合。1 = 実線）、color、lineWeightMilsを持ち、最後のレベルを超えるレベルは末尾に追加）、`addLevels`（同じフィールドを持つレベル。最後のレベルの後に追加）。gradient - `removeSegments`（削除する変化点の0始まりのインデックス。`segments`の前に適用）、`segments`（spotPosition、midpointPosition、color、opacity）。tile - `offset`、`repetition`、`usePageUnits`、`transparentBackground`、`backgroundColor`、`rotateInWalls`、`rotateInSymbols`、`addGeometryUuid`。lineType - `gapSize`、`usePageUnits`、`addGeometryUuid`。symbolDefinition - `pageBased`、`insertAsGroup`、`insertMode`、`breakMode`、`addGeometryUuid`、`resetInstances`、`active`（trueにすると、新しいシンボルインスタンスの作成元となるアクティブなシンボルになります）。texture - `size`、`updateThumbnail`。imageFill - `compression`。recordFormat - `localizedName`、`visible`、`addFields`（name、type、defaultValue、choices）、`removeFields`、`renameFields`（name、newName）、または`fieldName`と`defaultValue`、`choices`の一方または両方（popUpフィールドの選択肢を置き換えます）。worksheet - `clearCells`（`cells`を設定する前に内容と書式を消去する{ topLeft, bottomRight }の範囲）、`cells`（row、column、formula。`bottomRight`を指定すると、row/columnからそこまでのすべてのセルに数式を設定）、`count`と共に指定する`insertRows`／`insertColumns`／`deleteRows`／`deleteColumns`、および`recalculate`（デフォルトでオン。editWorksheetでは書式、枠線、統合したセル、サイズ、データベース行も設定できます）。folder - `addResourceUuid`。リソースの名前変更、説明の設定、複製、削除には、代わりにeditResourceを使用してください。内部用のIFCレコードフォーマットは拒否されます。代わりにIFCツールを使用してください。

> **注:** `levels`では、項目`i`が0始まりのインデックス`i`のレベルに適用されます。指定しないメンバーは現在の値を維持します。最後のレベルの直後のインデックスはレベルを追加し、追加したレベルの指定しないメンバーは`addLevels`と同様に0になります。それより大きいインデックスは設定されません（`applied.levels`で`false`）。`addLevels`は常に末尾に追加し、指定しないメンバーはすべて0になるため、`dashFactor`を指定してください（1 = 実線。Vectorworksは0より大きい値を想定しています）。
>
> **注:** `segments`では、項目`i`が0始まりのインデックス`i`の変化点に適用されます。指定しないメンバーは現在の値を維持し、最後の変化点を超えるインデックスは新しい変化点を挿入します。新しい変化点の指定しないメンバーのデフォルトは、`spotPosition` 0、`midpointPosition` 0.5、`color`は黒（`{ "r": 0, "g": 0, "b": 0 }`）、`opacity` 100です（4つすべてを指定してください）。`removeSegments`が先に実行されるため、`segments`のインデックスは残った変化点を指します。Vectorworksは変化点を`spotPosition`の順に並べて保持します: 新しい`spotPosition`が隣の変化点を越える変化点と、新しい変化点は、次の項目が適用される前に並べ替え後の位置へ移動するため、後の項目は並べ替え後の変化点を指します。`segments`は`spotPosition`の昇順で指定してください。
>
> **注:** `addFields[].type`には`radio`、`controlPoint`、`layerPopUp`が列挙されていますが、これらのタイプのフィールドは追加されません（`added: false`）。不明なタイプ名はエラーになります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `usePageUnits` | boolean |  | ハッチング、タイル、ラインタイプ: `true`では、パターンをワールド単位ではなく印刷した用紙上の単位（縮尺無視）で測定します。 |
| `transparent` | boolean |  | ハッチング: `true`では、ハッチングの線の背後の領域を背景で塗りつぶさずに透明にします。 |
| `rotateInWalls` | boolean |  | ハッチングとタイル: パターンを、描画先の壁の回転に合わせるかどうか。 |
| `rotateInSymbols` | boolean |  | ハッチングとタイル: パターンを、描画先のシンボルの回転に合わせるかどうか。 |
| `levels` | array of object |  | ハッチング: 項目`i`がレベル`i`を設定します（1つ目の注を参照）。項目のメンバー: `startPoint`、`repeatVector`、`offsetVector`（[点](Common.md#points)）、`dashFactor`（数値）、`color`（[色](Common.md#colors)）、`lineWeightMils`（整数。ミル単位、1ミル = 1/1000インチ）。 |
| `addLevels` | array of object |  | 同じフィールドを持つレベル。最後のレベルの後に追加されます。指定しないメンバーは0になります（`dashFactor`を指定してください）。 |
| `segments` | array of object |  | グラデーション: 項目`i`が変化点`i`を設定します（2つ目の注を参照）。項目のメンバー: `spotPosition`、`midpointPosition`（数値）、`color`（[色](Common.md#colors)）、`opacity`（整数）。 |
| `removeSegments` | array of integer |  | 削除する変化点の0始まりのインデックス。`segments`の前に適用されます。重複した項目と、負の値または整数でない項目は無視されます。 |
| `offset` | [点](Common.md#points) |  | タイル: タイルのグリッドの原点。 |
| `repetition` | [点](Common.md#points) |  | タイル: ある繰り返しから次の繰り返しまでの移動量。 |
| `transparentBackground` | boolean |  | タイル: タイルの背景を透明にするかどうか。 |
| `backgroundColor` | [色](Common.md#colors) |  | タイル: 背景色。 |
| `gapSize` | number |  | ラインタイプ: 図形の2つの繰り返しの間隔（ワールド単位。ラインタイプが縮尺無視（ページ単位）を使用する場合はページ単位）。 |
| `addGeometryUuid` | string |  | タイル、ラインタイプ、シンボル定義: リソースの図形に移動する既存のオブジェクトのUUID。オブジェクトが見つからないか追加できない場合、`applied.addGeometry`はfalseです。 |
| `pageBased` | boolean |  | シンボル定義: `true`では、シンボルをワールド単位ではなく、印刷した用紙上のサイズで保ちます（「実寸表示優先-縮尺無視」）。 |
| `insertAsGroup` | boolean |  | シンボル定義: `true`では、シンボルインスタンスではなく、シンボルの内容の複製を挿入します。 |
| `resetInstances` | boolean |  | シンボル定義: `true`で定義のインスタンスをリセットします。`false`では何もしません。 |
| `active` | boolean |  | trueにすると、新しいシンボルインスタンスの作成元となるアクティブなシンボルになります。 |
| `insertMode` | string |  | 次のいずれか: `edge`, `center`, `leftEdge`, `rightEdge`, `coreComponentCenter`, `coreComponentLeftEdge`, `coreComponentRightEdge`, `wallInsertLocation`, `wallClosureInsertLocation`。 |
| `breakMode` | string |  | 次のいずれか: `fullWithCaps`, `fullNoCaps`, `half`, `none`。 |
| `size` | number |  | テクスチャ: テクスチャのイメージが覆う実寸（ワールド単位）。 |
| `updateThumbnail` | boolean |  | テクスチャ: `true`でリソースマネージャのテクスチャのプレビューを更新します。`false`では何もしません。 |
| `compression` | string |  | 次のいずれか: `none`, `jpeg`, `png`, `pngMonochrome`。 |
| `localizedName` | string |  | レコードフォーマット: フォーマットのローカライズ名。 |
| `visible` | boolean |  | レコードフォーマット: `false`では、オブジェクト情報パレットのデータタブにレコードフォーマットを表示しません。 |
| `addFields` | array of object |  | 項目のメンバー: `name`、`type`（省略時は`text`）、`defaultValue`、`choices`。 |
| `addFields[].name` | string |  | 新しいフィールドの名前。名前が空の場合、またはフォーマットに同じ名前のフィールドが既にある場合、フィールドは追加されません（`added: false`）。 |
| `addFields[].type` | string |  | 次のいずれか: `integer`, `boolean`, `real`, `text`, `dimension`, `popUp`, `radio`, `staticText`, `controlPoint`, `classPopUp`, `layerPopUp`, `angle`, `area`, `volume`, `class`, `buildingMaterial`, `fill`, `penStyle`, `penWeight`, `color`, `texture`, `symbolDefinition`。`radio`、`controlPoint`、`layerPopUp`は列挙されていますが、追加されることはありません。 |
| `addFields[].defaultValue` | string |  | テキストで指定するデフォルト値。`text`、`popUp`、`staticText`、`classPopUp`フィールドではそのまま保持し、その他のタイプでは、ユーザーが入力した値と同じ方法でVectorworksが読み取ります（数値、フラグ、既存のリソースの名前、色）。タイプに合わない値では追加に失敗します（`added: false`）。空の文字列は常に受け付けられます。 |
| `addFields[].choices` | array of string |  | ポップアップフィールドの選択肢。フィールドを追加した後に設定されます。 |
| `removeFields` | array of string |  | 削除するフィールドの名前。文字列でない項目はスキップされます。 |
| `renameFields` | array of object |  | 項目のメンバー: `name`、`newName`。 |
| `renameFields[].name` | string |  | フィールドの現在の名前。 |
| `renameFields[].newName` | string |  | 新しい名前。フィールドが存在しない場合、`newName`が既にフィールドの名前である場合、または名前の変更に失敗した場合、`renamed`はfalseです。 |
| `fieldName` | string |  | `defaultValue`と`choices`の一方または両方を置き換える既存のフィールド。 |
| `defaultValue` | string |  | `fieldName`の新しいデフォルト値（テキスト）。レコードフォーマットのAPIを通じてフィールドのタイプに変換されます（`addFields[].defaultValue`のような厳密な解析ではありません）。フィールドが存在すれば、テキストを変換できずデフォルト値が変わらない場合でも、`applied.defaultValue`はtrueです。 |
| `choices` | array of string |  | ポップアップフィールド`fieldName`の選択肢を置き換えます。フィールドのタイプは確認されないため、既存のフィールドであれば`applied.choices`はtrueです。 |
| `clearCells` | object |  | `cells`を設定する前に内容と書式を消去する{ topLeft, bottomRight }の範囲。 |
| `clearCells.topLeft` | object |  | 範囲の最初のセル。省略時は行1、列1。 |
| `clearCells.topLeft.row` | integer |  | 行（1始まり。省略時は1）。 |
| `clearCells.topLeft.column` | integer |  | 列（1始まり。省略時は1）。 |
| `clearCells.bottomRight` | object |  | 範囲の最後のセル。省略時は最初のセル。 |
| `clearCells.bottomRight.row` | integer |  | 行（1始まり。省略時は`topLeft`の行）。 |
| `clearCells.bottomRight.column` | integer |  | 列（1始まり。省略時は`topLeft`の列）。 |
| `cells` | array of object |  | row、column、formula。`bottomRight`を指定すると、row/columnからそこまでのすべてのセルに数式を設定します。 |
| `cells[].row` | integer |  | 行（1始まり。省略時は1）。 |
| `cells[].column` | integer |  | 列（1始まり。省略時は1）。 |
| `cells[].formula` | string |  | セルに設定する数式。`bottomRight`を指定した場合は範囲内のすべてのセルに設定します。 |
| `cells[].bottomRight` | object |  | 範囲の最後のセル。省略時はそのセル自体。 |
| `cells[].bottomRight.row` | integer |  | 行（1始まり。省略時はそのセルの行）。 |
| `cells[].bottomRight.column` | integer |  | 列（1始まり。省略時はそのセルの列）。 |
| `insertRows` | integer |  | ワークシート: その前に`count`行を挿入する行。 |
| `insertColumns` | integer |  | ワークシート: その前に`count`列を挿入する列。 |
| `deleteRows` | integer |  | ワークシート: 削除する`count`行のうち最初の行。 |
| `deleteColumns` | integer |  | ワークシート: 削除する`count`列のうち最初の列。 |
| `count` | integer |  | `insertRows`、`insertColumns`、`deleteRows`、`deleteColumns`の行数または列数（デフォルト1）。行または列、あるいは`count`が0より大きくない場合、それぞれの`applied`はfalseです。 |
| `recalculate` | boolean |  | 変更後にワークシートを再計算します。デフォルトでオン。 |
| `addResourceUuid` | string |  | フォルダ: フォルダに移動する既存のリソースのUUID（`applied.addResource`）。 |

**結果**

変更したリソースのリソース参照（[getResource](#getresource)を参照）と、次のキー:

| キー | 説明 |
|---|---|
| `applied` | 指定した引数ごとに、書き込まれた内容（下の表を参照）。 |
| `details` | 変更後のリソースの詳細。リソースの種類について[getResourceDetails](#getresourcedetails)が返すキーを持ちます。 |

`applied`の項目は引数と同じ名前です。ただし`addGeometryUuid`（項目`addGeometry`）と`addResourceUuid`（項目`addResource`）は除きます:

| 引数 | appliedの項目 |
|---|---|
| `usePageUnits`、`transparent`、`rotateInWalls`、`rotateInSymbols`、`offset`、`repetition`、`transparentBackground`、`backgroundColor`、`gapSize`、`pageBased`、`insertAsGroup`、`insertMode`、`breakMode`、`size`、`compression`、`localizedName`、`visible` | 真偽値: 値を書き込んだ場合はtrue。`insertMode`と`breakMode`は、一覧にない名前ではfalseです。 |
| `levels`、`addLevels`、`segments` | 項目ごとの真偽値を順に並べた配列。 |
| `removeSegments` | `{ index, removed }`の配列。インデックスは大きいものから順に処理されます。 |
| `addGeometryUuid`、`addResourceUuid` | 真偽値。 |
| `resetInstances`、`active`、`updateThumbnail` | 真偽値。引数が`true`の場合にだけ含まれます。 |
| `addFields` | `{ name, added }`の配列。 |
| `removeFields` | `{ name, removed }`の配列。 |
| `renameFields` | `{ name, newName, renamed }`の配列。 |
| `defaultValue`、`choices` | フィールド`fieldName`についての真偽値。 |
| `insertRows`、`insertColumns`、`deleteRows`、`deleteColumns`、`clearCells` | 真偽値。 |
| `cells` | `{ row, column, set }`の配列。項目ごとに1つです。 |
| `recalculate` | 真偽値。`recalculate`がfalseでない限り含まれます。 |

ワークシートは次の順で変更されます: `insertRows`、`insertColumns`、`deleteRows`、`deleteColumns`、`clearCells`、`cells`、最後に再計算。そのため`clearCells`と`cells`は、挿入と削除の後の行と列を指します。

エラー: `resource not found`、`not a resource`、`unknown compression: <x>`、`unknown record field type: <x>`、`the <type> resource has no typed settings; use editResource`（そのリソースタイプには、このツールで設定できる項目がありません）、内部用のIFCレコードフォーマットの拒否。失敗した呼び出しはロールバックされます（`rolledBack`）。

### applyResource

テクスチャ、スタイル、データの可視化をオブジェクトに適用します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ「MCP: applyResource」 · **runToolBatch内:** はい

**詳細**

現在の図面のリソース（`resourceUuid`または`resourceName`で指定）を、`objectUuid`で指定したオブジェクトに適用します: テクスチャ（オブジェクトの1つの`part`だけに適用することも可能）、文字スタイル、壁スタイル（`selectedOffset`と`replacingOffset`で、どの線の位置を維持するかを決定）、スラブ、屋根、ビューポートのスタイル、またはデータの可視化（`activate`がfalseの場合はオフにします。代わりに`excludeObject`を指定すると、trueではオブジェクトをすべてのデータの可視化から除外し、falseでは再び対象に含めます）。

シンボル定義の場合は、代わりにインスタンスを作成します: 図面の`position`に、ラジアン単位の`rotation`で挿入します。ワークシートは、アクティブレイヤにワークシートイメージとして、左上隅を`position`に合わせて配置します。既に配置されているワークシートの場合は、代わりにそのイメージをそこへ移動します（`moved`がtrue）。どちらも`objectUuid`は必要ありません。内部用のIFCレコードフォーマットは拒否されます。代わりにIFCツールを使用してください。

> **注:** `resourceUuid`は`resourceName`より優先されます。シンボル定義とワークシートを除くすべてのリソースには`objectUuid`が必要です。`excludeObject`でもデータの可視化を`resourceUuid`または`resourceName`で指定する必要がありますが、すべてのデータの可視化についてオブジェクトに作用します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `resourceUuid` | string |  | 適用するリソースのUUID。`resourceName`より優先されます。 |
| `resourceName` | string |  | リソースの名前。`resourceUuid`がない場合にだけ使用されます。空または不明な`resourceUuid`では`resource not found`になります。 |
| `objectUuid` | string |  | 対象オブジェクトのUUID。シンボル定義とワークシートでは使用されません。 |
| `part` | string |  | テクスチャ: テクスチャを適用するオブジェクトの部分（デフォルト`overall`）。次のいずれか: `overall`, `extrudeTop`, `extrudeBottom`, `extrudeSides`, `wallLeft`, `wallRight`, `wallTop`, `wallBottom`, `slabTop`, `slabBottom`, `slabSides`, `roofTop`, `roofBottom`, `roofSides`。 |
| `selectedOffset` | number |  | 壁スタイル: `replacingOffset`と組み合わせて、壁のどの線の位置を維持するかを決めます（デフォルト0）。 |
| `replacingOffset` | number |  | 壁スタイル: `selectedOffset`と組み合わせて、壁のどの線の位置を維持するかを決めます（デフォルト0）。 |
| `activate` | boolean |  | データの可視化: `false`でオブジェクトのデータの可視化をオフにします（デフォルト`true`）。`excludeObject`を指定した場合は無視されます。 |
| `excludeObject` | boolean |  | データの可視化: `true`ではオブジェクトをすべてのデータの可視化から除外し、`false`では再び対象に含めます。 |
| `position` | [点](Common.md#points) |  | シンボル定義: インスタンスの挿入点。ワークシート: ワークシートイメージの左上隅。デフォルト(0, 0)。 |
| `rotation` | number |  | シンボル定義: インスタンスの回転角（ラジアン、デフォルト0）。 |

**結果**

`resource`はリソース参照（[getResource](#getresource)を参照）、`object`は作成または変更したオブジェクトのオブジェクト参照です（[オブジェクト参照](Common.md#object-references)を参照）。その他のキーはリソースによって異なります:

| リソース | `object`とその他のキー |
|---|---|
| シンボル定義 | `object`は新しいシンボルインスタンスです。その他のキーはありません。 |
| ワークシート | `object`はワークシートイメージです。ワークシートが既に配置されていてそのイメージを移動した場合は`moved`が`true`、新しいイメージを作成した場合は`false`です。 |
| その他のリソース | `object`は対象オブジェクトです。`applied`は`true`です。 |

エラー: `resource not found`、`not a resource`、内部用のIFCレコードフォーマットの拒否、`failed to insert the symbol`、`failed to place the worksheet in the drawing`、`object not found`（`objectUuid`がないか、どのオブジェクトも指していない）、`unknown texture part: <x>`、`a <type> resource cannot be applied to an object`（そのリソースタイプには適用の操作がありません）、`failed to apply the resource to the object`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### getWorksheet

ワークシートのサイズ、セル、書式、データベース行を読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

ワークシートリソースを詳細に読み取ります: サイズ（`rows`、`columns`）、`autoRecalculate`、レイヤに配置されたワークシートの`image`（ある場合）、および範囲のセル。セルは{ row, column }で指定し、1始まりです（列1はA）。範囲は`topLeft`から`bottomRight`までです（デフォルト: ワークシート全体）。各セルは`formula`（定義: リテラル、または'='で始まる数式）、表示される`text`、および数値の場合は`value`を持ちます。テキストと値は前回の再計算時のものです（editWorksheetは再計算します）。

数式が再計算待ちのセルは、`value`の代わりに`needsRecalculation`: trueを持ちます。値を読み取るとVectorworksがワークシートを再計算してしまうためです。数式もテキストもないセルは、`includeEmpty`がtrueでない限り省略されます。`include`は次を追加します: "formats"（セルごとの`numberFormat`、`textFormat`、`fill`、`borders`、および統合したセルではその範囲を持つ`merged`。キーはeditWorksheetが受け付けるものと同じですが、名前のないフォントでは`font`の代わりに`fontIndex`）、"sizes"（範囲の`columnWidths`と`rowHeights`。ワークシートのピクセル単位）、"database"（`databaseRows`: 範囲内のデータベース行と、その`criteria`および`subrowCount`）。

`subrowsOf`（データベース行の行番号）を指定すると、セルの代わりにその行の`subrows`を一覧表示します: 検索条件で見つかったオブジェクトごとに1つで、それぞれ範囲内の列の`text`と`value`を持ちます。`limit`（デフォルトは200セルまたは100サブ行）、`offset`、`countOnly`で、セルまたはサブ行をページ分割します。ワークシートの`uuid`、`name`、`index`、またはレイヤに配置されたワークシートの`uuid`を渡してください。createResourceはワークシートを作成し、applyResourceはワークシートをレイヤに配置します。getResourceDetails / setResourceDetailsでも、通常のセルを読み取り、設定できます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `topLeft` | object |  | 範囲の最初のセル（`{ row, column }`。両方が必要です）。省略時は行1、列1。 |
| `topLeft.row` | integer |  | 行（1始まり）。 |
| `topLeft.column` | integer |  | 列（1始まり。列1はA）。 |
| `bottomRight` | object |  | 範囲の最後のセル（`{ row, column }`。両方が必要です）。省略時はワークシートの最後のセル。`topLeft`より上または左にはできません。 |
| `bottomRight.row` | integer |  | 行（1始まり）。 |
| `bottomRight.column` | integer |  | 列（1始まり）。 |
| `include` | array of string |  | 各項目は次のいずれか: `formats`, `sizes`, `database`。`subrowsOf`とは併用できません。 |
| `includeEmpty` | boolean |  | `true`では、数式もテキストもないセルも一覧表示します。`subrowsOf`とは併用できません。 |
| `subrowsOf` | integer |  | データベース行の行番号（1から行数まで）。セルの代わりに、その行のサブ行を一覧表示します。 |
| `limit` | integer |  | ページ分割: 返すセル（デフォルト200）またはサブ行（デフォルト100）の最大数（1以上）。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割: スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割: 項目を含めず、件数だけを返します。 |

**結果**

ワークシートと、読み取った範囲:

| キー | 説明 |
|---|---|
| `worksheet` | ワークシートのリソース参照（[getResource](#getresource)を参照）。 |
| `rows`、`columns` | ワークシートのサイズ。 |
| `autoRecalculate` | ワークシートが自動的に再計算されるかどうか。 |
| `image` | ワークシートイメージのオブジェクト参照。ワークシートがレイヤに配置されている場合のみ。 |
| `topLeft`、`bottomRight` | 範囲。それぞれ`{ row, column }`。 |

`subrowsOf`を指定しない場合、結果はセルのページです（[ページ分割](Common.md#paging)を参照）: `count`は一覧表示したセルの数で、セルは`cells`に含まれます。`countOnly`の場合は省略されます。`include`を指定すると、結果には次のキーも含まれます:

| キー | 説明 |
|---|---|
| `columnWidths` | `sizes`指定時: 幅を持つ範囲内の各列について`{ column, width }`（ワークシートのピクセル単位）。 |
| `rowHeights` | `sizes`指定時: 高さを持つ範囲内の各行について`{ row, height, locked }`（ワークシートのピクセル単位）。 |
| `databaseRows` | `database`指定時: 範囲内の各データベース行について`{ row, criteria, subrowCount }`。 |

`countOnly`の場合、`columnWidths`、`rowHeights`、`databaseRows`は省略されます。

`cells`の各項目は`row`、`column`、`formula`、`text`、および数値の場合は`value`を持ちます。再計算待ちのセルは`needsRecalculation: true`を持ち、`value`はありません。`formats`を指定すると、項目は`numberFormat`、`textFormat`、`fill`、`borders`、`merged`（`{ topLeft, bottomRight }`）も持ちます。いずれもセルにある場合だけです。

`subrowsOf`を指定すると、結果には`subrowsOf`（その行）と、`subrows`にその行のサブ行のページが含まれます。`count`はサブ行の数です。各項目は`subrow`（1始まり。項目0がサブ行1）と`cells`を持ちます: サブ行にある範囲内の各列について`{ column, text }`、および数値の場合は`value`。

エラー: `no worksheet found: pass the 'uuid', 'name' or 'index' of a worksheet resource, or the 'uuid' of a worksheet placed on a layer`、`the object found is not a worksheet resource or a worksheet placed on a layer`、`'include' must be an array of: formats, sizes, database`、`'includeEmpty' must be true or false`、`'subrowsOf' cannot be used with 'include' or 'includeEmpty'`、`'topLeft' must be a cell { "row", "column" } of whole numbers`（`bottomRight`も同様）、`'topLeft' is outside the worksheet: row <n>, column <n>; the worksheet has <n> rows and <n> columns`（`bottomRight`も同様）、`'bottomRight' must not be above or left of 'topLeft'`、`'subrowsOf' must be a whole number from 1 to <rows>`、`row <n> is not a database row`。`'limit' must be at least 1`などのページ分割の引数のエラーは、[結果とエラー](Common.md#results-and-errors)で説明しています。

### editWorksheet

アクションのリストでワークシートを変更します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ「MCP: editWorksheet」 · **runToolBatch内:** はい

**詳細**

ワークシートリソースを`actions`のリスト（1～100個）で変更します。アクションは順番に適用され、取り消し可能な1つのステップになります: 1つでも失敗すると呼び出しは失敗し、ワークシートは変更されません。セルは{ row, column }で指定し、1始まりです（列1はA）。範囲は`topLeft`と省略可能な`bottomRight`（デフォルト: `topLeft`）で指定します。各アクションは`action`とその引数を持つオブジェクトです: setFormula（範囲、`formula`: リテラル、または=SUM(A1..A3)のように'='で始まる数式。範囲内のすべてのセルに設定）、clear（範囲: 内容と書式）、insertRows / insertColumns（`before`、`count`。デフォルト1）、deleteRows / deleteColumns（`start`、`count`。デフォルト1。ワークシートには少なくとも1行と1列が残ります）、setNumberFormat（範囲、`numberStyle`、`accuracy`、`leader`、`trailer`）、setTextFormat（範囲、`font`（フォント名）、`size`（ポイント）、`bold`、`italic`、`underline`、`outline`、`shadow`、`alignment`、`verticalAlignment`、`angle`（整数の度数）、`color`、`wrap`）、setFill（範囲、`fillStyle`、`background`、`foreground`、`pattern`。"solid"には`background`が、"pattern"には`pattern`、`foreground`、`background`が必要）。この3つは、指定したフィールドだけをセルごとに変更し、1つのアクションで最大10000セルを処理します（setTextFormatは、統合によって隠れていて独自のフォントを持たないセルを除外し、その他の独自のフォントを持たないセル、たとえば統合後に再分割されたセルでは`font`を必要とします）。setBorders（範囲、`top`、`left`、`bottom`、`right`、`outline`、`insideHorizontal`、`insideVertical`: これらの枠線を描画します。falseのフラグは枠線をそのままにするため、枠線を削除することはできません）、merge（2つ以上のセルの範囲）／unmerge（範囲）、ワークシートのピクセル単位のsetColumnWidth（`column`、`lastColumn`、`width`）とsetRowHeight（`row`、`lastRow`、`height`、`lockHeight`（デフォルトtrue）、`includeSubrows`）、autoFitRowHeights（`row`、`lastRow`）、setDatabaseCriteria（`row`と、=DATABASE((T=RECT))などの`criteria`。その行を、見つかったオブジェクトごとに1つのサブ行を持つデータベース行にします。空の`criteria`は通常の行に戻します）、recalculate、setAutoRecalculate（`enabled`）。

`recalculate`（デフォルトtrue）は、アクションの後にワークシートを再計算します。再計算では、RUNSCRIPT数式のスクリプトも実行されます。結果には新しい`rows`と`columns`、およびアクションごとの`applied`項目が含まれます。セルはgetWorksheetで読み直してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `actions` | array of object | はい | 1～100個の項目。 |
| `actions[].action` | string | はい | 次のいずれか: `setFormula`, `clear`, `insertRows`, `insertColumns`, `deleteRows`, `deleteColumns`, `setNumberFormat`, `setTextFormat`, `setFill`, `setBorders`, `merge`, `unmerge`, `setColumnWidth`, `setRowHeight`, `autoFitRowHeights`, `setDatabaseCriteria`, `recalculate`, `setAutoRecalculate`。 |
| `actions[].topLeft` | object |  | 範囲の最初のセル（`{ row, column }`。両方が必要です）。`setFormula`、`clear`、`setNumberFormat`、`setTextFormat`、`setFill`、`setBorders`、`merge`、`unmerge`で必要です。 |
| `actions[].topLeft.row` | integer |  | 行（1始まり）。 |
| `actions[].topLeft.column` | integer |  | 列（1始まり。列1はA）。 |
| `actions[].bottomRight` | object |  | 範囲の最後のセル（`{ row, column }`）。省略時は`topLeft`の単一のセルが範囲になります。`topLeft`より上または左にはできません。 |
| `actions[].bottomRight.row` | integer |  | 行（1始まり）。 |
| `actions[].bottomRight.column` | integer |  | 列（1始まり）。 |
| `actions[].formula` | string |  | `setFormula`: 必須。リテラル、または`=SUM(A1..A3)`のように`=`で始まる数式。範囲内のすべてのセルに設定されます。 |
| `actions[].before` | integer |  | `insertRows`と`insertColumns`: 必須。新しい行または列をこの行または列の前に挿入します。1から行数または列数+1まで。 |
| `actions[].start` | integer |  | `deleteRows`と`deleteColumns`: 必須。削除する最初の行または列。1から行数または列数まで。 |
| `actions[].count` | integer |  | `insertRows`と`insertColumns`: 挿入する数（1～32767、デフォルト1）。`deleteRows`と`deleteColumns`: `start`から削除する数（デフォルト1）。ワークシートには少なくとも1行と1列が残ります。 |
| `actions[].numberStyle` | string |  | `setNumberFormat`: 数字の表示形式のスタイル。次のいずれか: `general`, `decimal`, `decimalWithCommas`, `scientific`, `fractional`, `dimension`, `angle`, `date`, `conditional`, `generalFraction`, `dimensionWithDivider`, `area`, `volume`, `text`, `percentage`。 |
| `actions[].accuracy` | integer |  | `setNumberFormat`: 数字の表示形式の精度（0～127）。意味はスタイルによって異なり、小数点以下の桁数とは限りません。 |
| `actions[].leader` | string |  | `setNumberFormat`: 数字の表示形式の前記号。 |
| `actions[].trailer` | string |  | `setNumberFormat`: 数字の表示形式の後記号。 |
| `actions[].font` | string |  | `setTextFormat`: Vectorworksが認識するフォントの名前。統合後に再分割されたセルなど、独自のフォントを持たないセルでは必要です。 |
| `actions[].size` | integer |  | `setTextFormat`: フォントサイズ（ポイント、1～32767）。 |
| `actions[].bold` | boolean |  | `setTextFormat`: `true`でボールドを設定し、`false`で解除します。省略すると変更しません。 |
| `actions[].italic` | boolean |  | `setTextFormat`: `true`でイタリックを設定し、`false`で解除します。省略すると変更しません。 |
| `actions[].underline` | boolean |  | `setTextFormat`: `true`でアンダーラインを設定し、`false`で解除します。省略すると変更しません。 |
| `actions[].outline` | boolean |  | `setTextFormat`: `true`でアウトラインの文字スタイルを設定し、`false`で解除します。省略すると変更しません。`setBorders`: `true`で範囲の外枠を描画します（デフォルト`false`）。 |
| `actions[].shadow` | boolean |  | `setTextFormat`: `true`でシャドウの文字スタイルを設定し、`false`で解除します。省略すると変更しません。 |
| `actions[].alignment` | string |  | `setTextFormat`: 水平方向の配置。次のいずれか: `general`, `left`, `center`, `right`。 |
| `actions[].verticalAlignment` | string |  | `setTextFormat`: 垂直方向の配置。次のいずれか: `general`, `top`, `center`, `bottom`。 |
| `actions[].angle` | integer |  | `setTextFormat`: 文字の角度（整数の度数、-360～360）。 |
| `actions[].color` | [色](Common.md#colors) |  | `setTextFormat`: 文字色。ファイルのカラーパレットで最も近い色に変換されます。`getWorksheet`はその色を返します。 |
| `actions[].wrap` | boolean |  | `setTextFormat`: セル内で文字を折り返すかどうか。 |
| `actions[].fillStyle` | string |  | `setFill`: 面の種類。次のいずれか: `none`, `solid`, `pattern`。 |
| `actions[].background` | [色](Common.md#colors) |  | `setFill`: 背景色。`fillStyle`が`solid`と`pattern`の場合に必要です。ファイルのカラーパレットで最も近い色に変換されます。 |
| `actions[].foreground` | [色](Common.md#colors) |  | `setFill`: 模様の前景色。`fillStyle`が`pattern`の場合に必要です。ファイルのカラーパレットで最も近い色に変換されます。 |
| `actions[].pattern` | integer |  | `setFill`: 面の模様（0～32767）。`fillStyle`が`pattern`の場合に必要です。 |
| `actions[].top` | boolean |  | `setBorders`: `true`で範囲の上辺を描画します（デフォルト`false`）。 |
| `actions[].left` | boolean |  | `setBorders`: `true`で範囲の左辺を描画します（デフォルト`false`）。 |
| `actions[].bottom` | boolean |  | `setBorders`: `true`で範囲の下辺を描画します（デフォルト`false`）。 |
| `actions[].right` | boolean |  | `setBorders`: `true`で範囲の右辺を描画します（デフォルト`false`）。 |
| `actions[].insideHorizontal` | boolean |  | `setBorders`: `true`で範囲内の行の間の水平の枠線を描画します（デフォルト`false`）。 |
| `actions[].insideVertical` | boolean |  | `setBorders`: `true`で範囲内の列の間の垂直の枠線を描画します（デフォルト`false`）。 |
| `actions[].column` | integer |  | `setColumnWidth`: 必須。サイズを変更する最初の列。1から列数まで。 |
| `actions[].lastColumn` | integer |  | `setColumnWidth`: サイズを変更する最後の列。`column`から列数まで（デフォルト`column`）。 |
| `actions[].width` | integer |  | `setColumnWidth`: 必須。幅（ワークシートのピクセル単位、1～32767）。 |
| `actions[].row` | integer |  | `setRowHeight`と`autoFitRowHeights`: 必須。変更する最初の行。1から行数まで。`setDatabaseCriteria`: 必須。検索条件を設定する行。1から行数まで。 |
| `actions[].lastRow` | integer |  | `setRowHeight`と`autoFitRowHeights`: 変更する最後の行。`row`から行数まで（デフォルト`row`）。 |
| `actions[].height` | integer |  | `setRowHeight`: 必須。高さ（ワークシートのピクセル単位、1～32767）。 |
| `actions[].lockHeight` | boolean |  | `setRowHeight`: 新しい高さを固定するかどうか（デフォルト`true`）。`getWorksheet`はこれを`locked`として返します。 |
| `actions[].includeSubrows` | boolean |  | `setRowHeight`: `true`では、範囲内のデータベース行のサブ行もサイズを変更します（デフォルト`false`）。 |
| `actions[].criteria` | string |  | `setDatabaseCriteria`: 必須。`=DATABASE((T=RECT))`などのデータベースの定義。空の文字列はその行を通常の行にします。 |
| `actions[].enabled` | boolean |  | `setAutoRecalculate`: 必須。`true`でワークシートの自動再計算をオンにし、`false`でオフにします。 |
| `recalculate` | boolean |  | `true`（デフォルト）ではアクションの後にワークシートを再計算し、`false`では再計算しません。`recalculate`アクションは、リストの途中でワークシートを再計算します。 |

**結果**

アクション適用後のワークシート:

| キー | 説明 |
|---|---|
| `worksheet` | ワークシートのリソース参照（[getResource](#getresource)を参照）。 |
| `rows`、`columns` | アクション適用後のワークシートのサイズ。 |
| `applied` | アクションごとに1項目（`actions`の順）。各項目は`action`（アクションの名前）と、次の表に挙げるキーを持ちます。 |
| `recalculated` | アクションの後にワークシートが再計算された場合は`true`。`recalculate`が`false`の場合、または再計算に失敗した場合は`false`。 |

`applied`の項目が`action`以外に持つキー:

| アクション | キー |
|---|---|
| `setFormula`、`clear`、`setBorders`、`merge`、`unmerge` | `topLeft`と`bottomRight`: 範囲。それぞれ`{ row, column }`。 |
| `setNumberFormat`、`setTextFormat`、`setFill` | `cells`: 範囲内のセルの数。`topLeft`と`bottomRight`。 |
| `insertRows`、`deleteRows` | `rows`: アクション後の行数。 |
| `insertColumns`、`deleteColumns` | `columns`: アクション後の列数。 |
| `setDatabaseCriteria` | `row`と`isDatabaseRow`: その行がデータベース行になったかどうか。 |
| `setAutoRecalculate` | `enabled`。 |
| `setColumnWidth`、`setRowHeight`、`autoFitRowHeights`、`recalculate` | なし。 |

何かを変更する前に、呼び出しはワークシート、`recalculate`、アクションのリストを確認します。エラー: `no worksheet found: pass the 'uuid', 'name' or 'index' of a worksheet resource, or the 'uuid' of a worksheet placed on a layer`、`the object found is not a worksheet resource or a worksheet placed on a layer`、`'recalculate' must be true or false`、`'actions' must be an array of 1 to 100 actions`、`actions[<i>]: 'action' must be one of: <names>`。

失敗したアクションがあると、呼び出しはただちに終了します。呼び出しはロールバックされ（`rolledBack`。[結果とエラー](Common.md#results-and-errors)を参照）、ワークシートは呼び出し前の状態のままになります。エラーは`actions[<i>] (<action>): `で始まります。`<i>`は`actions`内のアクションの位置で、0から数えます。引数のエラー: `'topLeft' must be a cell { "row", "column" } of whole numbers`（`bottomRight`も同様）、`'topLeft' is outside the worksheet: row <n>, column <n>; the worksheet has <n> rows and <n> columns`（`bottomRight`も同様）、`'bottomRight' must not be above or left of 'topLeft'`、`'topLeft' and 'bottomRight' must span at least two cells`（`merge`）、`'<key>' must be a whole number from <min> to <max>`、`'<key>' must be true or false`、`'<key>' must be a string`、`'<key>' must be one of: <names>`（`numberStyle`、`alignment`、`verticalAlignment`、`fillStyle`）、`'<key>' must be a color { "r", "g", "b" } with values from 0 to 255`、`'font' must be the name of a font that Vectorworks knows`、`give at least one of: numberStyle, accuracy, leader, trailer`（`setTextFormat`と`setFill`も同じ形で自身の引数を挙げます）、`'fillStyle' "solid" needs 'background'`、`'fillStyle' "pattern" needs 'pattern', 'foreground' and 'background'`、`the range has <n> cells; at most 10000 cells are formatted in one action`、`row <r>, column <c> uses the default font of the worksheet (as cells that were merged away do): give 'font' too`、`a worksheet keeps at least one row`（`column`も同様）。

Vectorworksが変更を拒否した場合、エラーは`Vectorworks did not`で始まり、その変更を示します。例: `Vectorworks did not insert the rows (a worksheet has a maximum number of rows)`、`Vectorworks did not merge the cells: the range must not cut through merged cells or hold a database row`、`Vectorworks did not set the database criteria: a row with merged cells cannot become a database row, and the criteria must be a database definition such as =DATABASE((T=RECT))`、`Vectorworks did not recalculate the worksheet`。

上限: 1回の呼び出しで100アクション、1つの書式アクションで10000セル、`count`、`width`、`height`は最大32767。
