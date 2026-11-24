[English](../../MCP/v2027.2/ObjectsConnectCAD.md) • [Deutsch](../../MCP.de/v2027.2/ObjectsConnectCAD.md) • **日本語**

# ObjectsConnectCAD — ConnectCADのDevice

> **サーバー:** Vectorworks MCP · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

ConnectCADの配線略図のDevice、そのSocketとDevice Type、およびそれらが使用するSignal TypeとConnector Typeのためのツールです。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [ConnectCAD](#connectcad)
  - [listConnectCADSignals](#listconnectcadsignals)
  - [listConnectCADConnectors](#listconnectcadconnectors)
  - [validateConnectCADDevice](#validateconnectcaddevice)
  - [createConnectCADDevice](#createconnectcaddevice)
  - [createConnectCADDevices](#createconnectcaddevices)
  - [getConnectCADDevice](#getconnectcaddevice)
  - [addConnectCADSocket](#addconnectcadsocket)
  - [setConnectCADSocket](#setconnectcadsocket)
  - [createConnectCADDeviceType](#createconnectcaddevicetype)
  - [getConnectCADDeviceType](#getconnectcaddevicetype)

<a id="overview"></a>

## 概要

このフォルダには1個のツールグループがあり、合計10個のツールが含まれています。

| グループ | グループID | 初期状態で有効 | リスクレベル | ツール数 | 概要 |
|---|---|---|---|---|---|
| [ConnectCAD](#connectcad) | `connectcad` | いいえ | 中 | 10 | JSONのDevice記述データから構築する、ConnectCADの配線略図のDevice、Socket、Device Type。 |

## ConnectCAD

> **グループ:** `ConnectCAD` · **グループID:** `connectcad` · **初期状態で有効:** いいえ · **リスクレベル:** 中 · **ツール数:** 10

**JSONのDevice記述データから構築する、ConnectCADの配線略図のDevice、Socket、Device Type。**

スクリプトを使用せずにConnectCADの配線略図のDeviceを作成、確認します。JSONのDevice記述データから全Socketを含むDeviceを作成し、DeviceのSocketの追加や編集、Device Typeのシンボル（Device Definitionレコード）の作成、および使用するSignal TypeとConnector Typeの確認を行います。Device記述データ（1個のJSONオブジェクト）は、name、tag、description、make、model、category、width_r（`non-rack` | `half-rack` | `full-rack`）、width、height、depth（mm。ラック搭載のDeviceの高さは44.45 mmを1単位とする整数ラックユニット）、power（W）、weight（kg）、is_modular（bool）、n_slots（int。モジュール式の場合にのみ&gt; 0）で構成します。name、tag、make、model、width_r、is_modular、n_slotsは必須です。'socket groups': [ { qty (1-50), type, name, signal, connector, orientation, pinout: [ { pinID, name, sourceID } ], extra_data } ]。

**Socketタイプ：** IN、OUT、IO（それぞれ1個のSocket）、およびLOOP / IOloop（'&lt;name&gt;' + '&lt;name&gt;\_LP'のペア）。向きはL、R、X（フィードスルー）で、LOOPとIOloopはLまたはRのみです。FUSEとBUSはSocketではありません。qty &gt; 1の場合は'&lt;name&gt; 1'..'&lt;name&gt; n'を作成します（ConnectCADのデフォルトの番号付け）。Socket名はDevice内で一意である必要があり、'+'を含めることや、末尾を`_LP`にすることはできません。SignalとConnectorには、listConnectCADSignals / listConnectCADConnectorsが返すものを使用してください。pinoutにはそのConnectorのピンを列挙し、pinIDはDevice内で一意にします。記述データは最初に検証され、無効な場合は何も作成されません。各変更は、固有の名前を持つ、取り消し可能なVectorworksの操作として実行されます。

> **注:** ConnectCADのツールにはConnectCADプラグインが必要です。プラグインがない場合、`listConnectCADSignals`、`listConnectCADConnectors`、`validateConnectCADDevice`、`createConnectCADDevice`、`createConnectCADDevices`は`err`テキスト`ConnectCAD is not available (the ConnectCAD plug-in is not installed)`で失敗します。2つの一覧ツールでは、ページ分割のエラーが先に報告されます。`addConnectCADSocket`は同じテキストを`errors`に列挙します。`getConnectCADDevice`、`setConnectCADSocket`、`createConnectCADDeviceType`、`getConnectCADDeviceType`はプラグインの有無を確認しません。プラグインがない場合、`setConnectCADSocket`はすべての`signal`と`connector`を拒否し（`applied`で`false`）、`createConnectCADDeviceType`はメーカーとモデルを持つDeviceについて`ConnectCAD returned no device type '<make> <model>': ...`を`errors`で報告します。
>
> **注:** `createConnectCADDevice`、`createConnectCADDevices`、`createConnectCADDeviceType`は[作成オプション](Common.md#creation-options)をいずれも受け付けません。`class`、`name`、`useClassAttributes`、`select`は適用されず、ConnectCADプラグインがオブジェクトをアクティブレイヤに作成します。
>
> **注:** Device記述データには、上記の説明以上の要件があります。各Socket Groupには`qty`、`type`、`name`、`signal`、`connector`、`orientation`の6つのキーがすべて必要で、`label_symbol`も受け付けます。すべてのルールは[validateConnectCADDevice](#validateconnectcaddevice)に記載されています。
>
> **注:** 型が異なる引数は、エラーなしで代替値になります。点でない`position`または`origin`は(0, 0)、数値でない`gap`は0、真偽値でない`createDeviceType`または`createDeviceTypes`はfalse、文字列でないテキストフィルタまたはSocketの値は空になります。型の誤りを報告するのは`limit`、`offset`、`countOnly`だけです。

| ツール | 作用 | リスク | 概要 |
|---|---|---|---|
| [`listConnectCADSignals`](#listconnectcadsignals) | 読み取り専用 | 低 | ConnectCADのSignal Typeの一覧を返します。 |
| [`listConnectCADConnectors`](#listconnectcadconnectors) | 読み取り専用 | 低 | ConnectCADのConnector Typeとそのピンの一覧を返します。 |
| [`validateConnectCADDevice`](#validateconnectcaddevice) | 読み取り専用 | 低 | 何も作成せずにDevice記述データを検証します。 |
| [`createConnectCADDevice`](#createconnectcaddevice) | 編集 | 中 | Device記述データから全Socketを含む配線略図のDeviceを作成します。 |
| [`createConnectCADDevices`](#createconnectcaddevices) | 編集 | 中 | 1回の操作で複数の配線略図のDeviceを横一列に作成します。 |
| [`getConnectCADDevice`](#getconnectcaddevice) | 読み取り専用 | 低 | ConnectCADのDeviceとそのSocketを読み取ります。 |
| [`addConnectCADSocket`](#addconnectcadsocket) | 編集 | 中 | DeviceにSocketを追加します。 |
| [`setConnectCADSocket`](#setconnectcadsocket) | 編集 | 中 | Socketを編集します。 |
| [`createConnectCADDeviceType`](#createconnectcaddevicetype) | 編集 | 中 | DeviceのDevice Typeシンボルを作成します。 |
| [`getConnectCADDeviceType`](#getconnectcaddevicetype) | 読み取り専用 | 低 | Device TypeのシンボルのDevice Definitionレコードを読み取ります。 |

### listConnectCADSignals

ConnectCADのSignal Typeの一覧を返します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

ConnectCADのSignal Typeの一覧を返します。各項目は`name`（Socketの`signal`として使用）、`category`、`description`、`defaultConnector`、推奨される`connectors`です。`category`と`search`によるフィルタは任意です（大文字と小文字を区別しない部分一致）。`limit`（デフォルト500）と`offset`でページ分割します。`countOnly`を指定すると件数のみを返します。

> **注:** `countOnly`を指定すると、`signals`配列を含めずにページ分割キー（`count`、`returned`、`offset`、`limit`、`truncated`）を返します。`category`はSignalのカテゴリの一部、`search`はSignalの`name`または`description`の一部です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `category` | string |  | フィルタ：このテキストをカテゴリに含むSignalのみを残します（大文字と小文字を区別しません）。 |
| `search` | string |  | テキストフィルタ：このテキストを名前または説明に含むSignalのみを残します（大文字と小文字を区別しません）。 |
| `limit` | integer |  | ページ分割：返す項目の最大数（1以上）。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割：スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割：項目を含めず、件数のみを返します。 |

**結果**

ページ分割キー（`count`、`returned`、`offset`、`limit`、`truncated`、およびリストが切り詰められた場合は`nextOffset`。[ページ分割](Common.md#paging)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `signals` | Signal Typeの配列（`countOnly`の場合は省略）。各項目は`name`、`category`、`description`、`defaultConnector`、`connectors`（推奨されるConnector名）です。 |

エラー：ページ分割のエラー（[ページ分割](Common.md#paging)を参照）、`ConnectCAD is not available (the ConnectCAD plug-in is not installed)`。

### listConnectCADConnectors

ConnectCADのConnector Typeとそのピンの一覧を返します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

ConnectCADのConnector Typeの一覧を返します。各項目は`name`（Socketの`connector`として使用）、`localizedName`、`category`、`pins`（Socket Groupの`pinout`に使用するピン名を順番に並べたもの）です。`search`は任意です。`limit`（デフォルト500）と`offset`でページ分割します。`countOnly`を指定すると件数のみを返します。

> **注:** `countOnly`を指定すると、`connectors`配列を含めずにページ分割キー（`count`、`returned`、`offset`、`limit`、`truncated`）を返します。`search`はConnectorの`name`、`localizedName`、`category`のいずれかの一部です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `search` | string |  | テキストフィルタ：このテキストを名前、ローカライズ名、カテゴリのいずれかに含むConnectorのみを残します（大文字と小文字を区別しません）。 |
| `limit` | integer |  | ページ分割：返す項目の最大数（1以上）。[ページ分割](Common.md#paging)を参照してください。 |
| `offset` | integer |  | ページ分割：スキップする項目数（デフォルト0）。 |
| `countOnly` | boolean |  | ページ分割：項目を含めず、件数のみを返します。 |

**結果**

ページ分割キー（[ページ分割](Common.md#paging)を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `connectors` | Connector Typeの配列（`countOnly`の場合は省略）。各項目は`name`、`localizedName`、`category`、`pins`（ピン名を順番に並べたもの）です。 |

エラー：`listConnectCADSignals`と同じです。

### validateConnectCADDevice

何も作成せずにDevice記述データを検証します。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

何も作成せずにDevice記述データを検証します。`isValid`、`errors`（Deviceが不正になる、またはプラグインが失敗する原因）、`warnings`（Device Typeにのみ保持されるデータ：category、pinout、extra_data、uuid、source）を返します。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `device` | object or string | はい | JSONオブジェクトまたはJSONテキスト形式のDevice記述データ（グループの説明を参照）。 |

**結果**

| キー | 説明 |
|---|---|
| `isValid` | `errors`が空の場合は`true`。 |
| `errors` | テキストの配列（常に含まれます）。Deviceが不正になる、またはプラグインが失敗する原因。 |
| `warnings` | テキストの配列（常に含まれます）。Device Typeにのみ保持されるデータ。 |

無効な記述データは通常の結果であり、`err`にはなりません。エラー：`ConnectCAD is not available (the ConnectCAD plug-in is not installed)`。

**検証ルール**

作成ツールも同じルールを使用します。Socket Groupに関するメッセージは`socket group <n> (<name>)`で始まります（nは1から数えます）。

- 記述データは1個のJSONオブジェクトで、オブジェクトまたはJSONテキストとして指定します。Deviceの配列は拒否されます（`the device must be one JSON object (an array of devices is not accepted)`）。
- 文字列：`name`、`tag`、`description`、`make`、`model`、`category`、`width_r`、`label_symbol`（`'<key>' must be a string`）。数値：`width`、`height`、`depth`、`power`、`weight`（`'<key>' must be a number (mm, W or kg)`）。`is_modular`は真偽値（`'is_modular' must be a boolean`）、`n_slots`は整数（`'n_slots' must be an integer`）です。その他のキーは無視されます。
- `name`、`tag`、`make`、`model`は空にできません（`'<key>' is required`）。`width_r`は`non-rack`、`half-rack`、`full-rack`のいずれかです。`height`を持つラック搭載のDeviceには、整数のラックユニット（0.1 mm以内でn × 44.45 mm）の高さが必要です（`a rack device needs a height of whole rack units (n x 44.45 mm)`）。`height`がない場合はエラーになりません。`n_slots`は整数で、モジュール式のDeviceでは0より大きく、それ以外では0以下です（`'n_slots' must be greater than 0 for a modular device and 0 otherwise`）。
- `socket groups`は任意で、オブジェクトの配列である必要があります。各グループには`qty`、`type`、`name`、`signal`、`connector`、`orientation`がすべて必要です（`<where>: missing '<key>' (the plug-in would throw)`）。`qty`は1～50の整数です。`uuid`と`source`は任意の文字列です。
- `type`は`IN`、`OUT`、`IO`（それぞれ1個のSocket）、`LOOP`、`IOloop`（`<name>` + `<name>_LP`のペア）のいずれかです。`FUSE`と`BUS`は拒否されます（`type FUSE is an internal-wiring component, not a socket (a Socket is IN, OUT or IO)`）。`orientation`は`L`、`R`、`X`のいずれかで、`LOOP`と`IOloop`には`X`を指定できません。
- Socket名は空にできず、`+`（ConnectCADの番号付けのオフセット）を含めることや、末尾を`_LP`にすることはできません。生成される名前（`<name>`、または`<name> 1`..`<name> n`、およびループの場合は`<name>_LP`）はDevice内で一意である必要があります（`socket name '<n>' is used <count> times in the device`）。
- `signal`と`connector`はConnectCADが認識するものである必要があります（`signal '<x>' is not a ConnectCAD signal type`、`connector '<x>' is not a ConnectCAD connector type`）。`???`は常に拒否されます。名前は`listConnectCADSignals`と`listConnectCADConnectors`から取得してください。
- `pinout`（任意）は、文字列の`name`と任意の整数`pinID`、`sourceID`（0～65535）を持つオブジェクトの配列です。ピン名は、そのConnectorのピンと同じ順序で一致する必要があります（`the pinout does not match the pins of connector <name>`）。`pinID`はDevice内で1回だけ使用でき（`pinID <n> is used twice in the device`）、すべての`sourceID`はDeviceの`pinID`である必要があります（`sourceID <n> is not a pinID of the device`）。
- `extra_data`（任意）はオブジェクトです。文字列：`power_factor`、`rating`。真偽値：`link_through`。数値：`avg_consumption`、`max_consumption`、`max_voltage`、`min_voltage`、`ampere`、`maximum_power`、`voltage`、`x`、`y`、`z`、`x_scale`、`y_scale`、`z_scale`、`x_offset`、`y_offset`、`z_rotation`。それ以外のキーはエラーになります（`extra_data '<key>' is not a ConnectCAD key`）。
- エラーではなく警告になるもの：`'category' is only kept in the device type (Device Definition record), not on the device`、および各グループについて、指定された`uuid`、`source`、`pinout`、`extra_data`のキーを示す`<where>: <keys> are only kept in the device type (Device Definition record), not on the device sockets`。

### createConnectCADDevice

Device記述データから全Socketを含む配線略図のDeviceを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createConnectCADDevice" · **runToolBatch内:** はい

**詳細**

Device記述データから全Socketを含むConnectCADの配線略図のDeviceをアクティブレイヤに作成し、挿入点を`position`に配置します。`createDeviceType`がtrueの場合は、Device Definitionレコードに完全な記述データを保持するDevice Typeのシンボル'&lt;make&gt; &lt;model&gt;'も作成します。Device（uuid、deviceName、tag、make、model、rackWidth、rackUnits、bounds、およびuuid、name、type、signal、connector、orientationを持つsockets）、`warnings`、`deviceType`を返します。

記述データが無効な場合は何も作成せず、`errors`を返します。

> **注:** ConnectCADプラグインはDeviceをアクティブレイヤの原点に作成し、その後ツールが`position`に移動します。`deviceName`は記述データの`name`で指定したConnectCADのDevice名です。オブジェクト参照の`name`はVectorworksのオブジェクト名で、異なる場合があります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `device` | object or string | はい | JSONオブジェクトまたはJSONテキスト形式のDevice記述データ（グループの説明を参照）。 |
| `position` | [点](Common.md#points) |  | 挿入点（デフォルトは0, 0）。 |
| `createDeviceType` | boolean |  | `true`の場合、Device Typeのシンボル'&lt;make&gt; &lt;model&gt;'も作成します（デフォルトは`false`）。 |

**結果**

新しいDevice（[getConnectCADDevice](#getconnectcaddevice)の結果を参照）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `warnings` | テキストの配列。警告がある場合のみ（`validateConnectCADDevice`の警告）。 |
| `deviceType` | `createDeviceType`がtrueの場合のみ。[createConnectCADDeviceType](#createconnectcaddevicetype)の結果（`deviceTypeName`、`isCreated`、`isFullDataStored`、`warnings`、`errors`）。 |

エラー：`ConnectCAD is not available (the ConnectCAD plug-in is not installed)`。記述データにエラーがある場合、またはプラグインがDeviceを作成しない場合、`err`は`the device was not created`となり、`errors`には`validateConnectCADDevice`のメッセージまたは`ConnectCAD did not create the device (is the ConnectCAD plug-in installed and licensed?)`が含まれます。失敗した呼び出しはロールバックされます（`rolledBack`）。

### createConnectCADDevices

1回の操作で複数の配線略図のDeviceを横一列に作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createConnectCADDevices" · **runToolBatch内:** はい

**詳細**

Device記述データの配列から、1回の操作で複数のConnectCADのDeviceを作成します。上端を`origin`に揃えて左から右へ横一列に並べ、Device間に`gap`（ファイルの単位）の間隔を設けます。`createDeviceTypes`を指定すると、それぞれのDevice Typeも作成します。すべての記述データを最初に検証し、1件でもエラーがある場合は何も作成せず、`invalid`に該当する項目をインデックスで列挙します。

> **注:** 各Deviceはアクティブレイヤの原点に作成された後、左端が`x`（最初の`x`は`origin.x`）、上端が`origin.y`になるように移動されます。Deviceを1つ配置するごとに、`x`はそのDeviceの幅と`gap`の分だけ増えます。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `devices` | array of object or string | はい | 各項目：JSONオブジェクトまたはJSONテキスト形式のDevice記述データ（グループの説明を参照）。配列は空にできません。 |
| `origin` | [点](Common.md#points) |  | 最初のDeviceの左端と、すべてのDeviceの上端の位置（デフォルトは0, 0）。 |
| `gap` | number |  | 2つのDevice間の間隔（ファイルの単位。デフォルトは0）。 |
| `createDeviceTypes` | boolean |  | `true`の場合、Device Typeのシンボルも作成します（デフォルトは`false`）。 |

**結果**

| キー | 説明 |
|---|---|
| `devices` | 記述データごとに1項目を指定順に並べた配列。各項目は[createConnectCADDevice](#createconnectcaddevice)の結果（移動後の`bounds`を含むDevice、`warnings`、`deviceType`）と同様です。Deviceが作成されなかった場合は、そのDeviceの`err`と`errors`を含みます。 |
| `partial` | 作成されなかったDeviceがある場合のみ`true`。その場合、結果には`err`も含まれ、呼び出しはロールバックされます。作成済みのDeviceも再び削除されるため、`devices`内の`uuid`は存在しなくなります（`rolledBack`を確認してください）。図面には何も残りません。 |

エラー：`ConnectCAD is not available (the ConnectCAD plug-in is not installed)`、`'devices' must be a non-empty array of device descriptions`、`no device was created: some descriptions have errors`（`invalid`に、`index`（0から数えます）と`errors`を持つオブジェクトの配列を含みます）、`not every device was created; see the 'err' / 'errors' of each entry`。失敗した呼び出しはロールバックされます（`rolledBack`）。

### getConnectCADDevice

ConnectCADのDeviceとそのSocketを読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

uuid、name、indexのいずれかでConnectCADのDeviceを読み取ります。返される情報はdeviceName、tag、description、make、model、rackWidth、rackUnits、isModular、slotCount、bounds、およびSocket（uuid、name、type、signal、connector、orientation）です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |

**結果**

Deviceの[オブジェクト参照](Common.md#object-references)と、次のキーを返します。

| キー | 説明 |
|---|---|
| `deviceName` | ConnectCADのDevice名（記述データの`name`）。参照の`name`はVectorworksのオブジェクト名です。 |
| `tag`、`description`、`make`、`model` | Deviceのテキスト。 |
| `rackWidth` | テキスト：`non-rack`、`half-rack`、`full-rack`のいずれか。 |
| `rackUnits` | テキスト：ラックユニット単位の高さ。高さが整数のラックユニットでない場合、またはラック搭載のDeviceでない場合は`---`。 |
| `isModular`、`slotCount` | Deviceがモジュール式かどうか、およびそのスロット数。 |
| `bounds` | Deviceの[矩形](Common.md#rectangles)。 |
| `sockets` | Socketの配列：`uuid`、`name`、`type`、`signal`、`connector`、`orientation`。 |

値を読み取れないキーは省略されます。エラー：`object not found`、`not a ConnectCAD device`。

### addConnectCADSocket

DeviceにSocketを追加します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: addConnectCADSocket" · **runToolBatch内:** はい

**詳細**

ConnectCADのDevice（uuid、name、indexのいずれかで指定）にSocketを追加します。指定する情報は`socketName`、`type`（IN | OUT | IO）、`signal`、`connector`、`orientation`（L | R）です。Socketはその側にあるSocketの下に配置され、Deviceが大きくなります。ループとXのSocketは、Deviceの作成時にのみ作成できます（createConnectCADDevice）。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `socketName` | string | はい | 新しいSocketの名前。空にできず、`+`を含めることや末尾を`_LP`にすることはできません。Deviceの別のSocketが使用している名前も指定できません。 |
| `type` | string | はい | 次のいずれか：`IN`、`OUT`、`IO`。 |
| `signal` | string | はい | ConnectCADのSignal Type（`listConnectCADSignals`を参照）。 |
| `connector` | string | はい | ConnectCADのConnector Type（`listConnectCADConnectors`を参照）。 |
| `orientation` | string | はい | `L`または`R`。 |

**結果**

新しいSocketを返します。

| キー | 説明 |
|---|---|
| `uuid` | 新しいSocketのUUID。 |
| `name`、`type`、`signal`、`connector`、`orientation` | `getConnectCADDevice`が列挙するのと同じ形式のSocketの値。 |

値がない、または文字列でない場合は空として扱われ、検証で失敗します。エラー：`object not found`、`not a ConnectCAD device`、`the socket was not added`（`errors`にテキストの配列を含みます。最後の3つを除き、各テキストは`socket '<name>': `で始まります。例：`type must be IN, OUT or IO (loops and X sockets only when the device is created)`、`orientation must be L or R (CC_AddSocket)`、`empty socket name`、`'+' in a socket name is a numbering offset in ConnectCAD`、`names ending in _LP are read back as loops`、`signal '<x>' is not a ConnectCAD signal type`、`connector '<x>' is not a ConnectCAD connector type`、`the device already has a socket '<name>'`、`ConnectCAD did not add the socket (is the ConnectCAD plug-in installed and licensed?)`、`ConnectCAD is not available (the ConnectCAD plug-in is not installed)`）。失敗した呼び出しはロールバックされます（`rolledBack`）。

### setConnectCADSocket

Socketを編集します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: setConnectCADSocket" · **runToolBatch内:** はい

**詳細**

uuidでConnectCADのSocketを編集します。指定する情報は`socketName`、`type`（IN | OUT | IO）、`signal`、`connector`（ConnectCADの一覧から取得）です。無効な値は書き込まれません。`applied`は、設定ごとに書き込まれたかどうかを示します。SocketとそのDeviceは再生成されます。

> **注:** `orientation`は変更できません。ループのペア（`<name>`と`<name>_LP`）のSocketでは、名前は拒否されます。空の名前、`+`を含む名前、末尾が`_LP`の名前、Deviceの別のSocketが使用している名前も拒否されます。拒否された値は書き込まれず、`applied`では理由なしに`false`になります。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string | はい | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `socketName` | string |  | Socketの新しい名前（上記の注を参照）。 |
| `type` | string |  | 次のいずれか：`IN`、`OUT`、`IO`。 |
| `signal` | string |  | ConnectCADのSignal Type（`listConnectCADSignals`を参照）。 |
| `connector` | string |  | ConnectCADの一覧から取得します。 |

**結果**

Socket（`addConnectCADSocket`が返すのと同じ`uuid`、`name`、`type`、`signal`、`connector`、`orientation`）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `applied` | 指定された`socketName`、`type`、`signal`、`connector`ごとに1項目。値が書き込まれた場合は`true`、拒否された場合または文字列でない場合は`false`。 |

すべての値が拒否されても、呼び出しは成功します。SocketとそのDeviceが再生成されるのは、値が書き込まれた場合だけです。エラー：`object not found`、`not a ConnectCAD socket`。

### createConnectCADDeviceType

DeviceのDevice Typeシンボルを作成します。

> **作用:** 編集 · **リスク:** 中 · **取り消し:** 1ステップ "MCP: createConnectCADDeviceType" · **runToolBatch内:** はい

**詳細**

Device（uuid、name、indexのいずれかで指定）から、ConnectCADのDevice Definitionレコードを持つDevice Typeのシンボル'&lt;make&gt; &lt;model&gt;'を作成します。`device`（Deviceの作成元となった記述データ）を指定すると、レコードに完全な記述データ（pinout、extra_data、uuid、source、category）を保持します。同じメーカーとモデルのDevice Typeが図面内にすでにある場合は、それを保持します。ConnectCADのライブラリにある場合は、代わりにそのDevice Typeを取り込みます（この場合、記述データは書き込まれません）。

> **注:** `uuid`、`name`、`index`は、Device Typeの作成元となるDeviceを検索します。`name`は新しいシンボルの名前ではありません。シンボルの名前は常に'&lt;make&gt; &lt;model&gt;'です。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照：新しいシンボルではなく、Deviceの名前。 |
| `index` | integer |  | 内部インデックスによる参照。 |
| `device` | object or string |  | JSONオブジェクトまたはJSONテキスト形式のDevice記述データ（グループの説明を参照）。検証はされません。Device Typeと比較されるのは、make、model、`width_r`、`n_slots`、height、depth、power、weightだけです。先に`validateConnectCADDevice`で検証してください。 |

**結果**

Device Typeのシンボル定義の[オブジェクト参照](Common.md#object-references)（シンボルがない場合は`{}`）と、次のキーを返します。

| キー | 説明 |
|---|---|
| `deviceTypeName` | 名前'&lt;make&gt; &lt;model&gt;'（メーカーまたはモデルがない場合は空）。 |
| `isCreated` | シンボルを今回作成した場合は`true`。同名のシンボルが図面にすでにある場合は`false`。 |
| `isFullDataStored` | 記述データがDevice Definitionレコードに書き込まれた場合のみ`true`。 |
| `warnings` | テキストの配列。警告がある場合のみ。 |
| `errors` | テキストの配列。エラーがある場合のみ。 |

作成できなかったDevice Typeは`errors`で報告され、通常の結果として扱われます。`err`はなく、ロールバックもされないため、`errors`を確認してください。呼び出し自体のエラー：`object not found`、`not a ConnectCAD device`。

`errors`の内容：`a device type needs the make and model of the device`、`ConnectCAD returned no device type '<make> <model>': only Generic and DA devices are supported, another object may have this name, or a library device type with another name was imported (see the Resource Manager)`。

`warnings`の内容：`a device type '<name>' was already in the drawing; it is kept and the description was not written`、`the device description was not written to the device type: <reason>`（理由は`the device description is not one JSON object`、`the make and model of the description differ from the device type`、`the device type has other data than the description (it comes from a ConnectCAD library)`のいずれか）、`the socket groups are too long for the Device Definition record and were not written`（32000文字を超える場合）、`the device type has no ConnectCAD Device Definition record`。

### getConnectCADDeviceType

Device TypeのシンボルのDevice Definitionレコードを読み取ります。

> **作用:** 読み取り専用 · **リスク:** 低 · **取り消し:** なし · **runToolBatch内:** 許可

**詳細**

Device Typeのシンボル定義（uuidまたはnameで指定）のConnectCAD Device Definitionレコードを読み取ります。返される情報はcategory、type、make、model、rackMounting、slotCount、および解析済みの`socketGroups`です。

> **注:** 結果には、オブジェクト参照の数値のオブジェクト`type`の代わりに、レコードの`type`（テキスト）が含まれます。`rackMounting`と`slotCount`は、レコードに保存されているとおりテキストです。

**パラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `uuid` | string |  | UUIDによる参照（推奨）。[オブジェクト参照](Common.md#object-references)を参照してください。 |
| `name` | string |  | 名前による参照：Device Typeのシンボル定義の名前。 |

**結果**

シンボル定義の[オブジェクト参照](Common.md#object-references)に続いて、次のキーを返します。

| キー | 説明 |
|---|---|
| `category`、`make`、`model` | Device Definitionレコードのテキスト。 |
| `type` | レコードの`Type`テキスト。オブジェクト参照の数値の`type`に置き換わります。 |
| `rackMounting` | テキスト：`non-rack`、`half-rack`、`full-rack`のいずれか。 |
| `slotCount` | スロット数（テキスト）。 |
| `socketGroups` | 配列：レコードの解析済みの`socket groups`。ない場合は`[]`。 |

エラー：`object not found`、`not a ConnectCAD device type (no ConnectCAD Device Definition record)`。
