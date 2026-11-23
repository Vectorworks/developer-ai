[English](../../MCP/v2027.2/IFC.md) • [Deutsch](../../MCP.de/v2027.2/IFC.md) • **日本語**

# IFC — IFCデータとデータマネージャのマッピング

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

図面のIFC（Industry Foundation Classes）データへの読み取り専用アクセスです。オブジェクトのIFCエンティティとプロパティセット、プロパティセットの定義、およびファイルのデータマネージャのIFCマッピングを扱います。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [IFC](#ifc)
  - [getObjectIFCData](#getobjectifcdata)
  - [getIFCPsetDefinition](#getifcpsetdefinition)
  - [listIFCPsets](#listifcpsets)
  - [listIFCCustomPsets](#listifccustompsets)
- [IFC Data Mapping](#ifc-data-mapping)
  - [listIFCMappingObjects](#listifcmappingobjects)
  - [getIFCMapping](#getifcmapping)

<a id="overview"></a>

## 概要

このフォルダには2つのツールグループがあり、合計6個のツールを提供します。

| グループ | グループID | 初期状態で有効 | 安全性レベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [IFC](#ifc) | `ifc` | はい | 低 | 4 | 読み取り専用のIFCデータ: オブジェクトのIFCエンティティとプロパティセット、IFCプロパティセットの定義（標準とカスタム）、およびファイルのカスタムプロパティセットです。 |
| [IFC Data Mapping](#ifc-data-mapping) | `ifc-data-mapping` | いいえ | 低 | 2 | アクティブファイルのデータマネージャのIFCマッピング定義を読み取ります。 |

## IFC

> **グループ:** `IFC` · **グループID:** `ifc` · **初期状態で有効:** はい · **安全性レベル:** 低 · **ツール数:** 4

**読み取り専用のIFCデータ: オブジェクトのIFCエンティティとプロパティセット、IFCプロパティセットの定義（標準とカスタム）、およびファイルのカスタムプロパティセットです。**

IFCサポートライブラリだけを通じた、IFCデータへの読み取り専用アクセスです。対象は、オブジェクトへのエンティティの割り当て、プロパティセット、エンティティとプロパティの値、カスタムプロパティセットの定義です。IFCの値はデータマネージャから取得され、このグループでは変更できません。これらのツールは、内部の生のIFCレコードを直接公開したり編集したりすることはありません。IFCを扱う場合は、汎用のオブジェクト／リソースのレコードツールではなく、これらのツールを使用してください。

IFCサポートを利用できない場合は、明示的なエラーを返します。getObjectIFCDataは、IFC取り出しで計算されるとおりにオブジェクトのIFCデータを報告します。listIFCCustomPsetsはアクティブファイルのカスタムプロパティセットを一覧表示し、カスタムセットが存在するかどうかを完全に確認できる唯一の方法です。getIFCPsetDefinitionは読み込まれた定義を1つ確認し、listIFCPsetsは1つのエンティティタイプを対象とします。

データマネージャのマッピング定義は、無効な「IFC Data Mapping」グループにあります。このグループは、ユーザーがデータマッピングについて尋ねた場合にのみ使用してください。読み取りの失敗は`err`の結果であり、データが存在しないことを意味するものではありません。

| ツール | 作用 | 安全性 | 概要 |
|---|---|---|---|
| [`getObjectIFCData`](#getobjectifcdata) | 読み取り専用 | 低 | IFC取り出しで計算されるとおりに、オブジェクトのIFCデータを読み取ります。 |
| [`getIFCPsetDefinition`](#getifcpsetdefinition) | 読み取り専用 | 低 | IFCプロパティセットの定義を名前で1つ読み取ります。 |
| [`listIFCPsets`](#listifcpsets) | 読み取り専用 | 低 | IFCエンティティタイプに適用できるIFCプロパティセットを一覧表示します。 |
| [`listIFCCustomPsets`](#listifccustompsets) | 読み取り専用 | 低 | ファイルのカスタムIFCプロパティセット定義を一覧表示します。 |

### getObjectIFCData

IFC取り出しで計算されるとおりに、オブジェクトのIFCデータを読み取ります。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

`uuid`で指定したオブジェクトのIFCデータを、付加されたIFCレコードとデータマネージャのマッピングからIFC取り出しで計算されるとおりに読み取ります（プラグインパラメータ、レコード、スタイル、条件式からの値を含みます）。結果は、`hasIFC`、`entity`、`schema`、IFCの`guid`、エンティティの`attributes`、および`custom`とプロパティ（名前、値の型、IFCタイプ、設定されている場合は値）を持つ、取り出されるプロパティセット（`psets`）です。

取り出し設定、MVDフィルタ、レイヤ／ストーリのマッピングは適用されません。また、IFC取り出しがドア／窓の部品、シンボルタイプ、階段、壁の構成要素に対して書き出す追加部分は再現されません。プロパティセットは、取り出し時に書き出される場合にのみ一覧に含まれます。返された`type`／`ifcType`を使用し、エンティティ名（IfcSlabなど）から型を推測しないでください。

結果は現在の状態だけを示すため、値や型が変更されたかどうかはわかりません。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string | はい | オブジェクトのUUID。このツールは`name`や`index`を受け付けません。 |

**結果**

| キー | 説明 |
|---|---|
| `object` | オブジェクト参照（[オブジェクト参照](Common.md#object-references)を参照）。 |
| `hasIFC` | 取り出しで計算されるとおり、オブジェクトにIFCエンティティがある場合は`true`。 |
| `scope` | データの対象範囲を示す固定テキスト。 |
| `attributes` | エンティティの属性。プロパティのリストです（下記参照）。他のIFCインスタンスを参照する属性は除外されます。`hasIFC`が`false`の場合は空です。 |
| `psets` | 取り出されるプロパティセット。`{ "name", "custom", "properties" }`のリストです。`properties`はプロパティのリストです（下記参照）。`hasIFC`が`false`の場合は空です。 |
| `readErrors` | 現在は常に空のリストです。読み取りの失敗は`err`の結果になります。 |
| `entity` | IFCエンティティ名。`hasIFC`が`true`の場合のみ。 |
| `schema` | アクティブなIFCスキーマ: `IFC2x2`、`IFC2x3`、`IFC4`、`IFC4x3`のいずれか。`hasIFC`が`true`の場合のみ。`getDocumentInfo`はIFC4スキーマを`IFC2x4`として報告します。 |
| `guid` | IFC GUID。オブジェクトにGUIDがある場合のみ。 |

各プロパティには`name`と`type`があり、判明している場合は`ifcType`と`value`もあります。`type`はシンボルによる値の型（例: `kIfcType_STRING`、`kIfcType_DOUBLE`）、または`unknown`です。`ifcType`は定義に含まれるIFCデータ型の名前です（例: `IfcLabel`）。`value`は常に文字列で、空の場合と、他のIFCインスタンスへの参照の場合は省略されます。他のIFCインスタンスを参照するエンティティの属性は、`attributes`から完全に除外されます。`psets`では、そのようなプロパティは`value`なしで一覧に含まれます。

エラー: `'uuid' is required`、`object not found`、`IFC support is unavailable in this Vectorworks session`、`failed to read the object's IFC data`（IFCのドキュメントやスキームがアクティブでない場合など）。

### getIFCPsetDefinition

IFCプロパティセットの定義を名前で1つ読み取ります。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

`name`でIFCプロパティセットの定義を1つ読み取ります。定義されているかどうか、カスタムかどうか、およびプロパティ名を返します。定義が見つからない場合は、空の結果ではなく明示的に報告します。`scope`は検索対象を示します。`defined`がfalseの場合、IFCサポートライブラリにはその名前の標準定義もカスタム定義もありません。これはレコードフォーマットやオブジェクトデータの検索ではありません。

似た名前のプロパティセットやレコードフォーマットは別のものです。ファイルにカスタムプロパティセットがあるかどうかを確認するには、listIFCCustomPsetsを使用してください。

> **注:** 名前はIFC2x3、IFC4、IFC4x3の定義から検索されますが、`custom`と`propertyNames`はアクティブなIFCスキーマからのみ読み取られます。別のスキーマにだけ存在する標準プロパティセットでは、`defined: false`ではなく、エラー`failed to read IFC property set definition: <name>`が返されます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | string | はい | プロパティセットの名前（例: `Pset_WallCommon`）。 |

**結果**

| キー | 説明 |
|---|---|
| `name` | 指定された名前。 |
| `scope` | 検索対象を示す固定テキスト。 |
| `defined` | IFCサポートライブラリにその名前の定義がある場合は`true`。 |
| `custom` | `defined`が`true`の場合のみ: カスタムプロパティセットの場合は`true`。 |
| `propertyNames` | `defined`が`true`の場合のみ: プロパティの名前。文字列のリストです。 |

エラー: `'name' is required`、`IFC support is unavailable in this Vectorworks session`、`failed to determine whether IFC property set is defined: <name>`、`failed to determine whether IFC property set is custom: <name>`、`failed to read IFC property set definition: <name>`。

### listIFCPsets

IFCエンティティタイプに適用できるIFCプロパティセットを一覧表示します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

1つのエンティティタイプに適用できるIFCプロパティセットを一覧表示します。`entity`のデフォルトは`IfcBuildingElementProxy`です。`customOnly`を設定すると、カスタムプロパティセットだけを返します。IFCスキーマとそのエンティティのデータマネージャのマッピングから、`entity`に適用できるセットだけが返されます。これはファイルのプロパティセットの一覧ではありません。ファイルのカスタムセットには、listIFCCustomPsetsを使用してください。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `customOnly` | boolean |  | カスタムプロパティセットだけを返します。デフォルト: `false`。 |
| `entity` | string |  | IFCエンティティタイプ（例: `IfcWall`）。デフォルト: `IfcBuildingElementProxy`。 |

**結果**

| キー | 説明 |
|---|---|
| `entity` | 使用されたエンティティ: `entity`引数、または引数がないか文字列でない場合は`IfcBuildingElementProxy`。 |
| `customOnly` | 使用された値。 |
| `psets` | 適用できるプロパティセット。`{ "name", "custom" }`のリストです。 |

エラー: `IFC support is unavailable in this Vectorworks session`、`failed to list IFC property sets for entity: <entity>`（アクティブなIFCスキーマにそのエンティティがない場合、または`entity`が空の文字列の場合）、`failed to determine whether IFC property set is custom: <name>`。

### listIFCCustomPsets

ファイルのカスタムIFCプロパティセット定義を一覧表示します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

アクティブファイルのカスタムIFCプロパティセット定義を、各プロパティのIFCタイプと、セットが有効かどうかとともに一覧表示します。成功した結果に含まれないセットは、そのファイルには定義されていません。`err`の結果は、存在するかどうかを判断できないことを意味します。引数はありません。

**パラメータ**

このツールにパラメータはありません。

**結果**

| キー | 説明 |
|---|---|
| `scope` | 固定テキスト: `custom property-set definitions of the active document`。 |
| `customPsets` | カスタムプロパティセット。`{ "name", "enabled", "properties" }`のリストです。`properties`は`{ "name", "ifcType", "unit" }`のリストです。`unit`はプロパティに単位がある場合のみ含まれ、`Length`、`Area`、`SolidAngle`、`Mass`、`Time`、`Temperature`、`Luminosity`、`Power`、`ThermalTransmittance`、`Dimension`、`Volume`、`Angle`のいずれかです。 |

エラー: `IFC support is unavailable in this Vectorworks session`、`the custom property sets of the active document could not be read; presence cannot be determined`（IFCデータがアクティブファイルにバインドされていない場合など）。

## IFC Data Mapping

> **グループ:** `IFC Data Mapping` · **グループID:** `ifc-data-mapping` · **初期状態で有効:** いいえ · **安全性レベル:** 低 · **ツール数:** 2

**アクティブファイルのデータマネージャのIFCマッピング定義を読み取ります。**

アクティブファイルのデータマネージャのIFCマッピング定義を読み取ります。対象は、マッピングされているオブジェクト、その条件、IFCエントリ、プロパティセット、および各フィールドに値を与える条件式です。これらのツールは、ユーザーがデータマッピングやデータマネージャについて尋ねた場合にのみ使用してください。オブジェクトのIFCの値には、IFCグループのgetObjectIFCDataを使用してください。

| ツール | 作用 | 安全性 | 概要 |
|---|---|---|---|
| [`listIFCMappingObjects`](#listifcmappingobjects) | 読み取り専用 | 低 | アクティブなデータマネージャのマッピングの、マッピングオブジェクトを一覧表示します。 |
| [`getIFCMapping`](#getifcmapping) | 読み取り専用 | 低 | 1つのマッピングオブジェクトのデータマネージャのマッピングを読み取ります。 |

### listIFCMappingObjects

アクティブなデータマネージャのマッピングの、マッピングオブジェクトを一覧表示します。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

アクティブなデータマネージャのマッピングのマッピングオブジェクトを、`name`、`enabled`、`condition`、`category`とともに一覧表示します。`limit`（デフォルト200）と`offset`でページ分割され、`count`は総数、`truncated`は続きがあるかどうかを示します。エントリを取得するには、名前をgetIFCMappingに渡します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `limit` | integer |  | ページ分割: 返す項目の最大数（1以上）。デフォルト: 200。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割: スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割: 項目を含めず、件数だけを返します。 |

**結果**

ページ分割のキー（[ページ分割](Common.md#paging)を参照）と、このページのマッピングオブジェクトである`objects`。各オブジェクトには次のキーがあります。

| キー | 説明 |
|---|---|
| `index` | マッピング内でのオブジェクトの位置。 |
| `name` | オブジェクトの名前。`getIFCMapping`の`objectName`に渡します。 |
| `enabled` | オブジェクトが有効な場合は`true`。 |
| `condition` | オブジェクトの条件。条件がある場合のみ。 |
| `category` | オブジェクトに保存されたカテゴリがある場合のみ: `classBasedLegacy`、`symbolDefinition`、`plugInThirdPartyLegacy`、`plugInBuiltInLegacy`、`ifcEntity`、`criteriaBased`、`parametricObjects`、`modelHierarchy`、`zones`、`systems`、`groups`、`unknown`のいずれか。 |

読み取れないオブジェクトには、`index`と`readFailed: true`だけが含まれます。オブジェクトのないマッピングでは、エラーではなく空のリストになります。エラー: `IFC support is unavailable in this Vectorworks session`、およびページ分割のエラー（[ページ分割](Common.md#paging)を参照）。

### getIFCMapping

1つのマッピングオブジェクトのデータマネージャのマッピングを読み取ります。

> **作用:** 読み取り専用 · **安全性:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

1つのマッピングオブジェクト`objectName`（listIFCMappingObjectsが返す名前）のデータマネージャのマッピングを読み取ります。結果にはその条件とIFCエントリが含まれ、各エントリには`type`（primary、secondary、unknownのいずれか）、有効状態、フィールド（値の型、マッピングの条件式、有効、任意、空）、および条件とフィールドを持つプロパティセットがあります。不明な名前ではエラーを返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `objectName` | string | はい | マッピングオブジェクトの名前。listIFCMappingObjectsが返す名前です。 |

**結果**

| キー | 説明 |
|---|---|
| `objectName` | 指定された名前。 |
| `enabled` | マッピングオブジェクトが有効な場合は`true`。 |
| `condition` | マッピングオブジェクトの条件。条件がある場合のみ。 |
| `entries` | オブジェクトのIFCエントリ。各エントリには下記のキーがあります。 |

| エントリのキー | 説明 |
|---|---|
| `name` | エントリの名前。 |
| `type` | `primary`（データマネージャのメイン）、`secondary`（サブ）、`unknown`のいずれか。 |
| `enabled` | エントリが有効な場合は`true`。 |
| `fields` | エントリのフィールド。 |
| `psets` | エントリのプロパティセット。`{ "name", "enabled", "fields", "condition" }`のリストです。`condition`はプロパティセットに条件がある場合のみ含まれます。 |

各フィールドには、`name`、`enabled`、`optional`、`empty`（データマネージャでのフィールドのフラグ）があり、判明している場合は`type`（`getObjectIFCData`と同様のシンボルによる値の型）と`mapping`（条件式。空の場合は省略）もあります。

エラー: `IFC support is unavailable in this Vectorworks session`、`'objectName' is required`、`no Data Manager mapping for object: <name>`。
