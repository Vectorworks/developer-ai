[English](../../MCP/v2027.2/ObjectsSpotlight.md) • [Deutsch](../../MCP.de/v2027.2/ObjectsSpotlight.md) • **日本語**

# ObjectsSpotlight — Lighting DeviceとGDTF器具タイプ

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

SpotlightのLighting Deviceと、それらが使用するGDTF（General Device Type Format）器具タイプのためのツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [Spotlight](#spotlight)
  - [listGDTFs](#listgdtfs)
  - [importGDTF](#importgdtf)
  - [createLightingDevice](#createlightingdevice)
  - [getLightingDevice](#getlightingdevice)
  - [setLightingDevice](#setlightingdevice)

<a id="overview"></a>

## 概要

このフォルダには1個のツールグループがあり、合計5個のツールが含まれています。

| グループ | グループID | 初期状態で有効 | 安全性レベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [Spotlight](#spotlight) | `spotlight` | いいえ | 中 | 5 | SpotlightのLighting Deviceと、それらが使用するGDTF器具タイプ。 |

## Spotlight

> **グループ:** `Spotlight` · **グループID:** `spotlight` · **初期状態で有効:** いいえ · **安全性レベル:** 中 · **ツール数:** 5

**SpotlightのLighting Deviceと、それらが使用するGDTF器具タイプ。**

SpotlightのLighting Deviceと、それらが使用するGDTF（General Device Type Format）器具タイプを作成、確認、編集します。使用可能なGDTF器具タイプとそのDMXモードの一覧取得、.gdtfファイルの図面への取り込み、GDTF器具タイプ、DMXモード（オブジェクト情報パレットの「GDTF Fixture」と「GDTF Fixture Mode」）、3Dモデルを持つLighting Deviceの作成、およびその読み取りや変更を行います。GDTF器具タイプは、listGDTFsが返す`gdtfName`で指定します。Lighting Deviceが使用できるのは図面内にある器具タイプ（isInDocument）だけなので、先に.gdtfファイルを取り込んでください。

各変更は、固有の名前を持つ、取り消し可能なVectorworksの操作として実行されます。

> **注:** `gdtfName`と`mode`は、大文字と小文字を区別して完全一致で照合されます。照合の対象は図面内の器具タイプだけです。図面内の器具タイプの場合、`gdtfName`はGDTFファイルのデータから`<Manufacturer>@<Name>.gdtf`として作成されます。まだ取り込まれていない.gdtfファイルについては、`listGDTFs`はディスク上のファイル名を表示しますが、これは異なる場合があります。`importGDTF`が返す`gdtfName`、または`documentOnly`を指定して`listGDTFs`が報告するものを使用してください。

| ツール | 作用 | 安全性 | 概要 |
|---|---|---|---|
| [`listGDTFs`](#listgdtfs) | 読み取り専用 | 低 | 使用可能なGDTF器具タイプとそのDMXモードの一覧を返します。 |
| [`importGDTF`](#importgdtf) | 編集 | 中 | .gdtfファイルをGDTF器具タイプとして図面に取り込みます。 |
| [`createLightingDevice`](#createlightingdevice) | 編集 | 中 | 必要に応じてGDTF器具タイプを指定して、Lighting Deviceを作成します。 |
| [`getLightingDevice`](#getlightingdevice) | 読み取り専用 | 低 | Lighting Deviceを読み取ります。 |
| [`setLightingDevice`](#setlightingdevice) | 編集 | 中 | Lighting Deviceを編集します。 |

### listGDTFs

使用可能なGDTF器具タイプとそのDMXモードの一覧を返します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

Spotlightで使用可能なGDTF器具タイプを、DMXモードごとに1件ずつ一覧で返します。各項目は`gdtfName`（createLightingDevice / setLightingDeviceに渡す値）、`fixtureName`（ファイルにリビジョンがある場合は'@&lt;revision&gt;'を含む）、`manufacturer`、`mode`、`footprint`（DMXチャンネル数）、`isInDocument`（図面に取り込み済みかどうか。取り込み済みの場合は`symbolDefinitionUuid`も含む）です。まず図面内の器具タイプ、次にSpotlightのGDTFフォルダ内の.gdtfファイルを返します。Spotlightがこれらのフォルダを読み取るのはセッションごとに1回です。Lighting Deviceに割り当てられるのは図面内の器具タイプだけなので、importGDTFでファイルを取り込んでください。

任意のフィルタは`manufacturer`と`search`（メーカー名、器具名、GDTF名の部分一致。大文字と小文字は区別しません）、および`documentOnly`です。`limit`（デフォルト200）と`offset`でページ分割します。`countOnly`を指定すると件数のみを返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `manufacturer` | string |  | メーカー名の一部。大文字と小文字を区別しないのはASCII文字だけです。 |
| `search` | string |  | `fixtureName`または`gdtfName`の一部。`manufacturer`の値自体は検索されません（`manufacturer`を使用してください）。大文字と小文字を区別しないのはASCII文字だけです。`manufacturer`と併用すると、両方のフィルタに一致する必要があります。 |
| `documentOnly` | boolean |  | 図面に取り込まれた器具タイプ（`isInDocument`がtrue）のみを対象にします。デフォルトはfalse。 |
| `limit` | integer |  | ページ分割：返す項目の最大数（1以上）。デフォルトは200。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割：スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割：項目を含めず、件数のみを返します。 |

**結果**

ページ分割された結果（[ページ分割](Common.md#paging)を参照）で、項目のキーは`gdtfs`です。各項目には次のキーがあります。

| キー | 説明 |
|---|---|
| `gdtfName` | `createLightingDevice`および`setLightingDevice`に渡す名前。 |
| `fixtureName` | 器具名。ファイルにリビジョンがある場合は`@<revision>`を含みます。 |
| `manufacturer` | メーカー名。 |
| `mode` | この項目のDMXモード。 |
| `footprint` | モードのDMXチャンネル数。 |
| `isInDocument` | 器具タイプが図面に取り込まれている場合は`true`。 |
| `symbolDefinitionUuid` | 器具タイプのシンボル定義のUUID。`isInDocument`が`true`の場合のみ。 |

複数のDMXモードを持つ器具タイプは、モードごとに1項目となり、どの項目も同じ`gdtfName`を持ちます。`countOnly`を指定すると`gdtfs`リストは省略されます。

エラー：`the GDTF support of Spotlight is not available`、ページ分割のエラー（[ページ分割](Common.md#paging)を参照）。

### importGDTF

.gdtfファイルをGDTF器具タイプとして図面に取り込みます。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: importGDTF" · **runToolBatch内:** はい

**詳細**

`filePath`（OS形式のフルパス）にある.gdtfファイルを、GDTF器具タイプ（GDTFリソースフォルダ内のシンボル定義）として図面に取り込みます。その参照と`gdtfName`を返します。ユーザーへの確認は行いません。同じGDTFのタイプIDを持つ器具タイプが図面内にすでにある場合は既存のものを保持します（isImportedはfalse）。読み取れないファイルはエラーになります。

> **注:** 器具タイプ自体のシンボル定義は、シンボルライブラリのルート（第一階層）に作成されます。`GDTF`シンボルフォルダに配置されるのは、その補助的なシンボル定義（`<fixtureName>_Thumbnail`など）だけです。シンボル名`<Manufacturer>@<Name>.gdtf`がすでに使われている場合、シンボル定義の名前は`<Manufacturer>@<Name>(1).gdtf`（以降も同様）に変更されますが、`gdtfName`は`<Manufacturer>@<Name>.gdtf`のままです。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `filePath` | string | はい | .gdtfファイルのOS形式のフルパス。 |

**結果**

取り込んだ場合：新しい器具タイプのシンボル定義のオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と次のキーを返します。

| キー | 説明 |
|---|---|
| `gdtfName` | `createLightingDevice`および`setLightingDevice`に渡す名前。 |
| `isImported` | `true`。 |

同じGDTFのタイプIDを持つ器具タイプが図面内にすでにある場合は、既存のものが保持され、置き換えられることはありません。その場合、結果には`isImported`（`false`）と`message`だけが含まれ、オブジェクト参照と`gdtfName`はありません。保持された器具タイプは、`documentOnly`を指定した`listGDTFs`で探してください。

エラー：`'filePath' is required: the full path of a .gdtf file`、`the GDTF support of Spotlight is not available`、`the file could not be read as GDTF: <path>`。

### createLightingDevice

必要に応じてGDTF器具タイプを指定して、Lighting Deviceを作成します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: createLightingDevice" · **runToolBatch内:** はい

**詳細**

SpotlightのLighting Device（照明シンボルなし）を`position`に作成し、`angle`（ラジアン）だけ回転させます。任意の`gdtfName`（listGDTFsまたはimportGDTFから取得した、図面内の器具タイプ）と`mode`（DMXモード。省略すると最初のモード）を指定すると、リソースマネージャで器具タイプをLighting Deviceにドロップした場合と同じようにGDTF器具タイプを割り当て、その後`useGdtfGeometry`がfalseでない限り、その3Dモデルを描画します。

`instrumentType`と未加工の`params`は任意です。`applied`は、設定ごとに書き込まれたかどうかを示します。`gdtf`がfalseの場合、指定したgdtfNameとmodeに一致する器具タイプが図面内になく、Lighting Deviceは既存のGDTF設定を保持します。`mode`がfalseの場合、`gdtfName`なしでモードが指定されています。

> **注:** `gdtfName`と`mode`は、大文字と小文字を区別して完全一致で照合されます。`mode`を省略した場合、空の場合、または文字列でない場合は、最初のDMXモードが選択されます。`gdtf`が`false`でも呼び出しは失敗せず、Lighting Deviceは器具タイプなしで作成されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `position` | [点](Common.md#points) | はい | 挿入点（ワールド単位）。xとyだけが使用されます。欠落した点や形式が正しくない点は拒否されず、0,0として読み取られます。 |
| `angle` | number |  | 反時計回りの角度（ラジアン）。デフォルトは0。 |
| `gdtfName` | string |  | listGDTFsまたはimportGDTFから取得した、図面内の器具タイプ。大文字と小文字を区別して完全一致で照合されます。 |
| `mode` | string |  | 器具タイプのDMXモード。大文字と小文字を区別して完全一致で照合されます。`gdtfName`と一緒に指定した場合にのみ使用されます。省略した場合、空の場合、または文字列でない場合は最初のモードです。 |
| `useGdtfGeometry` | boolean |  | GDTF器具タイプの3Dモデルを描画します。`gdtfName`の適用後のデフォルトはtrueです。JSONの真偽値で指定する必要があり、それ以外の値は`true`として書き込まれます。 |
| `instrumentType` | string |  | SpotlightのInstrument Type（Lighting Deviceの`Inst Type`パラメータ）。 |
| `params` | object |  | 未加工のプラグインパラメータ { "ParamName": value }（getObjectParametersを参照）。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |
| `class` | string |  | 作成オプション：新しいオブジェクトのクラス。存在しない場合は作成します。[作成オプション](Common.md#creation-options)を参照してください。 |
| `name` | string |  | 作成オプション：新しいオブジェクトの名前。 |
| `select` | boolean |  | 作成オプション：新しいオブジェクトを選択します。 |
| `useClassAttributes` | boolean |  | 作成オプション：`class`とともに指定すると、新しいオブジェクトの属性も「クラス属性を使用」に設定します。 |

**結果**

新しいLighting Deviceのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と、設定を指定した場合のみ`applied`（[適用した設定](Common.md#applied-settings)を参照）を返します。キーは`gdtf`と`mode`（上記のとおり）、`useGdtfGeometry`、`instrumentType`、`params`です。指定された設定のキーだけが含まれます。ただし、次の例外があります。`gdtfName`を指定すると`gdtf`が`mode`も兼ね、`mode`キーはありません（`mode`は`gdtfName`を指定しない場合にのみ現れ、常に`false`です）。`useGdtfGeometry`は、`gdtfName`が適用された後にも含まれます。`params`は、オブジェクトの場合にのみ含まれます。真偽値でない`useGdtfGeometry`は`true`として扱われ、文字列でない`instrumentType`は空の文字列を書き込みます。どちらも`true`を報告します。`params`の項目は、パラメータ名ごとに`true`または`false`を持つオブジェクトです。

エラー：`failed to create the lighting device (is Spotlight installed?)`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### getLightingDevice

Lighting Deviceを読み取ります。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

uuid、name、indexのいずれかでLighting Deviceを読み取ります。返される情報は`instrumentType`、`symbolName`、GDTF器具タイプの`gdtfName`とDMXの`mode`、`dmxFootprint`、`useGdtfGeometry`、`bounds`です。任意の`params`には、未加工の型付き値として返すプラグインパラメータ名を列挙します（getObjectParametersを参照）。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `params` | array of string |  | 型付き値として返すプラグインパラメータの名前。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |

**結果**

Lighting Deviceのオブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）と次のキーを返します。

| キー | 説明 |
|---|---|
| `instrumentType` | SpotlightのInstrument Type（`Inst Type`パラメータ）。 |
| `symbolName` | 照明シンボルの名前（`Symbol Name`パラメータ）。 |
| `gdtfName` | GDTF器具タイプ。`listGDTFs`が報告する形式です。 |
| `mode` | DMXモード名。`listGDTFs`が報告する形式です。 |
| `dmxFootprint` | DMXチャンネル数（`Num Channels`パラメータ）。 |
| `useGdtfGeometry` | GDTF器具タイプの3Dモデルを描画するかどうか。 |
| `bounds` | Lighting Deviceの境界。ワールド単位の[矩形](Common.md#rectangles)です。 |
| `params` | `params`を指定した場合のみ。Lighting Deviceが持つ、要求された各パラメータの型付き値を含むオブジェクトです。不明な名前は省略されます。 |

Lighting Deviceにそのパラメータがない場合、キーは省略されます。パラメータが存在しても空の場合は、空の文字列として返されます。

エラー：`object not found`、`not a lighting device`。Lighting Deviceは`uuid`、`name`、`index`の順に検索されます。

### setLightingDevice

Lighting Deviceを編集します。

> **作用:** 編集 · **安全性:** 中 · **取り消し:** 1ステップ "MCP: setLightingDevice" · **runToolBatch内:** はい

**詳細**

uuid、name、indexのいずれかでLighting Deviceを編集します。`gdtfName`（図面内の器具タイプ）と`mode`でGDTF器具タイプを割り当てます（成功した場合は、`useGdtfGeometry`がfalseでない限り、その3Dモデルの表示もオンにします）。そのほか、`useGdtfGeometry`、`instrumentType`、未加工の`params`を指定できます。Lighting Deviceは再生成されます。`applied`は、設定ごとに書き込まれたかどうかを示します。

> **注:** `gdtfName`と`mode`は、大文字と小文字を区別して完全一致で照合されます。`gdtf`が`false`の場合は、器具タイプを割り当てられなかったことを意味します。通常、Lighting Deviceは変更されません。`gdtfName`なしで指定した`mode`は書き込まれません（`applied.mode`は`false`）。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `gdtfName` | string |  | listGDTFsが報告する、図面内の器具タイプ。大文字と小文字を区別して完全一致で照合されます。 |
| `mode` | string |  | 器具タイプのDMXモード。大文字と小文字を区別して完全一致で照合されます。`gdtfName`と一緒に指定した場合にのみ書き込まれます。省略した場合、空の場合、または文字列でない場合は最初のモードです。 |
| `useGdtfGeometry` | boolean |  | GDTF器具タイプの3Dモデルを描画します。`gdtfName`の適用後のデフォルトはtrueです。指定した場合は`gdtfName`なしでも書き込まれます。JSONの真偽値で指定する必要があり、それ以外の値は`true`として書き込まれます。 |
| `instrumentType` | string |  | SpotlightのInstrument Type（Lighting Deviceの`Inst Type`パラメータ）。 |
| `params` | object |  | 未加工のプラグインパラメータ { "ParamName": value }（getObjectParametersを参照）。[プラグインパラメータ](Common.md#plug-in-parameters)を参照してください。 |

**結果**

`applied`（[適用した設定](Common.md#applied-settings)を参照）だけを返し、オブジェクト参照はありません。`applied`は空の場合でも常に含まれます。キーは`createLightingDevice`と同じく、`gdtf`と`mode`、`useGdtfGeometry`、`instrumentType`、`params`です。指定された設定のキーだけが含まれます。ただし、次の例外があります。`gdtfName`を指定すると`gdtf`が`mode`も兼ね、`mode`キーはありません（`mode`は`gdtfName`を指定しない場合にのみ現れ、常に`false`です）。`useGdtfGeometry`は、`gdtfName`が適用された後にも含まれます。`params`は、オブジェクトの場合にのみ含まれます。真偽値でない`useGdtfGeometry`は`true`として扱われ、文字列でない`instrumentType`は空の文字列を書き込みます。どちらも`true`を報告します。

エラー：`object not found`、`not a lighting device`。Lighting Deviceは`uuid`、`name`、`index`の順に検索されます。失敗した呼び出しはロールバックされます（`rolledBack`）。
