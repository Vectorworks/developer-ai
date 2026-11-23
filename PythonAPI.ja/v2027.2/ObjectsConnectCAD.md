[English](../../PythonAPI/v2027.2/ObjectsConnectCAD.md) • [Deutsch](../../PythonAPI.de/v2027.2/ObjectsConnectCAD.md) • **日本語**

<a id="objectsconnectcad--connectcad-devices-and-sockets"></a>

# ObjectsConnectCAD — ConnectCADのDeviceとSocket

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

ConnectCADのクラスです（ConnectCADが必要）。`ConnectCADDeviceObject`はSocketを備えた配線略図のDevice（ユニバーサル名は"Device"）で、JSONのDevice記述データから作成します。完全な記述を格納するDevice Typeのシンボルも作成できます。`ConnectCADSocketObject`はDeviceの接続点です（"Socket"：IN、OUT、IO。ループはSocketの組）。`ConnectCADLibrary`はSignalとConnectorの種類を一覧表示し、Device記述データを検証し、Device TypeのDevice Definitionレコードを読み取ります。

汎用のパラメータアクセスは[`ParametricObject`](ObjectPrimitives.md#parametricobject)から継承します。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [ConnectCADLibrary](#connectcadlibrary)
    - [ConnectCADLibrary.Signal](#connectcadlibrarysignal)
    - [ConnectCADLibrary.Connector](#connectcadlibraryconnector)
    - [ConnectCADLibrary.Validation](#connectcadlibraryvalidation)
    - [ConnectCADLibrary.DeviceDefinition](#connectcadlibrarydevicedefinition)
  - [ConnectCADSocketObject](#connectcadsocketobject)
  - [ConnectCADDeviceObject](#connectcaddeviceobject)
    - [ConnectCADDeviceObject.CreateResult](#connectcaddeviceobjectcreateresult)
    - [ConnectCADDeviceObject.AddSocketResult](#connectcaddeviceobjectaddsocketresult)
    - [ConnectCADDeviceObject.DeviceTypeResult](#connectcaddeviceobjectdevicetyperesult)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`ConnectCADLibrary`](#connectcadlibrary) | クラス |  | Device間で共有するConnectCADのデータです。SignalとConnectorの種類、Device記述データ（JSON）の検証、および...のDevice Definitionレコード。 |
| [`ConnectCADLibrary.Signal`](#connectcadlibrarysignal) | クラス（入れ子） |  | カテゴリと優先Connectorを含むConnectCADのSignal Typeです。 |
| [`ConnectCADLibrary.Connector`](#connectcadlibraryconnector) | クラス（入れ子） |  | ConnectCADのConnector Typeです。 |
| [`ConnectCADLibrary.Validation`](#connectcadlibraryvalidation) | クラス（入れ子） |  | ValidateDeviceの結果です。エラー（Deviceが不正になる）と警告（Device Typeにのみ保持されるデータ）を含みます。 |
| [`ConnectCADLibrary.DeviceDefinition`](#connectcadlibrarydevicedefinition) | クラス（入れ子） |  | Device Typeのシンボル定義のDevice Definitionレコードです。 |
| [`ConnectCADSocketObject`](#connectcadsocketobject) | クラス | [`ParametricObject`](ObjectPrimitives.md#parametricobject) | ConnectCADのSocket（ユニバーサル名は"Socket"）です。Deviceのプロファイルグループ内にある、配線略図のDeviceの接続点です。 |
| [`ConnectCADDeviceObject`](#connectcaddeviceobject) | クラス | [`ParametricObject`](ObjectPrimitives.md#parametricobject) | ConnectCADの配線略図のDevice（ユニバーサル名は"Device"）です。プロファイルグループ内にSocketを持つ、名前付きのボックスです。 |
| [`ConnectCADDeviceObject.CreateResult`](#connectcaddeviceobjectcreateresult) | クラス（入れ子） |  | CreateFromJSONの結果です。Device（作成されなかった場合はnull）、エラー、警告を含みます。 |
| [`ConnectCADDeviceObject.AddSocketResult`](#connectcaddeviceobjectaddsocketresult) | クラス（入れ子） |  | AddSocketの結果です。Socket（追加されなかった場合はnull）とエラーを含みます。 |
| [`ConnectCADDeviceObject.DeviceTypeResult`](#connectcaddeviceobjectdevicetyperesult) | クラス（入れ子） |  | CreateDeviceTypeの結果です。Device Typeのシンボル定義、新規かどうか、完全な記述がレコードに含まれるかどうかを示します。 |

<a id="classes"></a>

## クラス

### ConnectCADLibrary

> **完全修飾名:** `api.ConnectCADLibrary` · **継承元:** `api.Object`

Device間で共有するConnectCADのデータです。SignalとConnectorの種類、Device記述データ（JSON）の検証、Device TypeのシンボルのDevice Definitionレコードを含みます。

Device記述データは、ConnectCADのCC_DeviceFromJSONが読み取る形式の一つのJSONオブジェクトです：{ "name", "tag", "description", "make", "model", "category", "width_r": "non-rack" | "half-rack" | "full-rack", "width", "height", "depth" (mm), "power" (W), "weight" (kg), "is_modular" (bool), "n_slots" (int), "socket groups": [ { "qty", "type", "name", "signal", "connector", "orientation", "pinout": [ { "pinID", "name", "sourceID" } ], "extra_data": { ... }, "uuid", "source" } ] } 必須：name、tag、make、model、width_r、is_modular、n_slots（モジュール式の場合のみ> 0）。ラックDeviceの高さは整数のラックユニット（n x 44.45 mm）です。Socket Groupの種類：IN、OUT、IO（それぞれ一つのSocket）とLOOP / IOloop（"<name>" + "<name>_LP"の組：IN + OUT / IO + IO）。向き：L、R、X（貫通型）。ループはLまたはRのみです。FUSEとBUSはDevice Typeの内部配線構成要素で、Socketではありません。qty 1..50は"<name> 1".."<name> n"を作成します。SignalとConnectorはGetSignalsとGetConnectorsから取得します。pinoutにはConnectorのピンを一覧表示し、pinIDsはDevice内で一意です。ConnectCADプラグインとライセンスが必要で、ない場合はIsAvailableが`False`となり、リストは空になります。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ConnectCADLibrary()` | 状態を持たないオブジェクトです。すべてのメソッドは静的で、クラス自体から呼び出せます。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `IsAvailable() -> bool` *静的* | ConnectCADプラグインがインストールされているかどうか（Deviceの作成にはライセンスも必要）。 |

*Signal Type*

| メソッド | 説明 |
|---|---|
| `GetSignals() -> list[ConnectCADLibrary.Signal]` *静的* | アプリケーション、ワークグループ、ユーザーフォルダにあるConnectCADのSignalファイルを、ConnectCADが統合した状態で示します。このセッションでConnectCADが認識しているSignalだけを一覧表示します。 |
| `GetConnectors() -> list[ConnectCADLibrary.Connector]` *静的* | ピンを含むConnector Type。 |
| `ValidateDevice(deviceJson: str) -> ConnectCADLibrary.Validation` *静的* | CC_DeviceFromJSONとSocketの要件に従って、Device記述データ（一つのJSONオブジェクト）を確認します。 |
| `GetDeviceDefinition(symbolDefinition: Handle) -> ConnectCADLibrary.DeviceDefinition` *静的* | Device Typeのシンボル定義のDevice Definitionレコードです。`symbolDefinition`、category、type、make、model、rackMounting、slotCount、socketGroupsを含み、レコードがない場合は`symbolDefinition`が`None`です。 |

#### ConnectCADLibrary.Signal

> **完全修飾名:** `api.ConnectCADLibrary.Signal` · **継承元:** `api.Object`

ConnectCADのSignal Typeです。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Signal()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Signal(name, category, description, defaultConnector, connectors)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `name` | `str` | ユニバーサル名。例："HDMI"。 |
| `category` | `str` | 例："Video"。 |
| `description` | `str` | Signal Typeの説明。 |
| `defaultConnector` | `str` | SignalのデフォルトのConnector Type。 |
| `connectors` | `list[str]` | 優先Connector（すべてGetConnectorsに含まれます）。 |

#### ConnectCADLibrary.Connector

> **完全修飾名:** `api.ConnectCADLibrary.Connector` · **継承元:** `api.Object`

ConnectCADのConnector Typeです。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Connector()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Connector(name, localizedName, category, pins)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `name` | `str` | ユニバーサル名。例："XLR3F"。 |
| `localizedName` | `str` | ローカライズされた表示名。 |
| `category` | `str` | ローカライズされたフォルダ。 |
| `pins` | `list[str]` | Socket Groupの"pinout"用の、順番に並んだピン名。 |

#### ConnectCADLibrary.Validation

> **完全修飾名:** `api.ConnectCADLibrary.Validation` · **継承元:** `api.Object`

ValidateDeviceの結果。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Validation()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Validation(errors, warnings, isValid)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `errors` | `list[str]` | Deviceが不正になる、またはプラグインが失敗する内容。 |
| `warnings` | `list[str]` | Device Typeにのみ保持されるデータ。 |
| `isValid` | `bool` | 記述が有効かどうか。 |

#### ConnectCADLibrary.DeviceDefinition

> **完全修飾名:** `api.ConnectCADLibrary.DeviceDefinition` · **継承元:** `api.Object`

Device Typeのシンボル定義のDevice Definitionレコードです。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DeviceDefinition()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `DeviceDefinition(symbolDefinition, category, type, make, model, rackMounting, slotCount, socketGroups)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `symbolDefinition` | `Handle` | Device Typeのシンボル定義。 |
| `category` | `str` | Deviceのカテゴリ。 |
| `type` | `str` | Deviceのタイプ。 |
| `make` | `str` | メーカー。 |
| `model` | `str` | モデル。 |
| `rackMounting` | `str` | ラックなし、ハーフラック、フルラック。 |
| `slotCount` | `str` | スロット数（モジュール式のDevice）。 |
| `socketGroups` | `str` | JSON: { "socket groups": [ ... ] }. |

### ConnectCADSocketObject

> **完全修飾名:** `api.ConnectCADSocketObject` · **継承元:** [`ParametricObject`](ObjectPrimitives.md#parametricobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

ConnectCADのSocket（ユニバーサル名は"Socket"）です。Deviceのプロファイルグループ内にある、配線略図のDeviceの接続点です。種類はIN、OUT、IOです。ループは"<name>"と"<name>_LP"のSocketの組です。図形は種類と向きに従います（Connectorシンボルは"skt_con_<type>"、Xの場合は"skt_con_classic_<type>"）。セッターは値（種類IN/OUT/IO、ConnectCADのSignalとConnectorのタイプ）を検証し、SocketとそのDeviceを再生成します。Socketを変更する前に、取り消し用にDeviceを登録してください（`Document.AddBothSwapObject`）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ConnectCADSocketObject(h: Handle)` | 既存のConnectCAD Socket`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Duplicate() -> ConnectCADSocketObject` | 図面内のConnectCAD Socketを複製し、そのコピーを返します。 |
| `GetDevice() -> Handle` | Socketを所有するDeviceです。SocketがDevice内にない場合はnullです。 |
| `GetSocketName() -> str \| None` | Socket名を返します。 |
| `SetSocketName(name: str) -> bool` | 空にしたり、'+'（番号付けのオフセット）を含めたり、末尾を"_LP"（ループの出力）にしたり、Device内の別のSocketが使用する名前にしたりすることはできません。ループのSocketは名前を変更できません。 |
| `GetTag() -> str \| None` | タグを返します。 |
| `GetSocketType() -> str \| None` | IN、OUT、またはIO。 |
| `SetSocketType(type: str) -> bool` | Socketの種類を設定します。IN、OUT、またはIO。 |
| `GetSignal() -> str \| None` | Signalを返します。 |
| `SetSignal(signal: str) -> bool` | `ConnectCADLibrary.GetSignals`のSignal Type。 |
| `GetConnector() -> str \| None` | Connectorを返します。 |
| `SetConnector(connector: str) -> bool` | `ConnectCADLibrary.GetConnectors`のConnector Type。 |
| `GetOrientation() -> str \| None` | L、R、またはX。Deviceの作成時に設定します（Socketのシンボルはこの値に依存）。 |
| `IsLoopOutput() -> bool` | このSocketがループの出力"<name>_LP"かどうか。 |

継承メンバー：[`ParametricObject`](ObjectPrimitives.md#parametricobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### ConnectCADDeviceObject

> **完全修飾名:** `api.ConnectCADDeviceObject` · **継承元:** [`ParametricObject`](ObjectPrimitives.md#parametricobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

ConnectCADの配線略図のDevice（ユニバーサル名は"Device"）です。プロファイルグループ内にSocketを持つ、名前付きのボックスです。

CreateFromJSONはDevice記述データ（JSONについてはConnectCADLibraryを参照）を`ConnectCADLibrary.ValidateDevice`で確認した後、その記述からDeviceとSocketを作成します。記述が無効な場合は何も作成しません。Deviceは名前、タグ、説明、メーカー、モデル、ラック幅／ユニット、モジュール式／スロット、電力、重量を保持します。category、pinout、extra_data、uuid、sourceはDevice Type（CreateDeviceType）にのみ格納されます。

取り消し：CreateFromJSONは新しいDevice自体を記録します。AddSocketやSocketの編集を行う前に、取り消し用にDeviceを登録してください（`Document.AddBothSwapObject`）。ConnectCADプラグインとライセンスが必要です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ConnectCADDeviceObject(h: Handle)` | 既存のConnectCAD Device`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `CreateFromJSON(deviceJson: str, position: Math.Point2D) -> ConnectCADDeviceObject.CreateResult` *静的* | Device記述データ（一つのJSONオブジェクト）から、挿入点を`position`として、アクティブレイヤにDeviceとSocketを作成します。記述にエラーがある場合は何も作成しません。 |
| `Duplicate() -> ConnectCADDeviceObject` | 図面内のConnectCAD Deviceを複製し、そのコピーを返します。 |
| `GetDeviceName() -> str \| None` | Device名を返します。 |
| `GetTag() -> str \| None` | タグを返します。 |
| `GetDescription() -> str \| None` | 説明を返します。 |
| `GetMake() -> str \| None` | メーカーを返します。 |
| `GetModel() -> str \| None` | モデルを返します。 |
| `GetRackWidth() -> str \| None` | ラックなし、ハーフラック、またはフルラック。 |
| `GetRackUnits() -> str \| None` | 高さから算出したラックユニット数です（整数ユニットでない場合やラックDeviceでない場合は"---"）。 |
| `IsModular() -> bool \| None` | Deviceがモジュール式（カード用スロットを持つ）の場合はTrueです。 |
| `GetSlotCount() -> int \| None` | スロット項目の数。 |
| `GetSockets() -> list[ConnectCADSocketObject]` | 図面上の順序で並んだDeviceのSocketです。ループは二つのSocket（"<name>"と"<name>_LP"）です。 |
| `AddSocket(name: str, type: str, signal: str, connector: str, orientation: str) -> ConnectCADDeviceObject.AddSocketResult` | L側またはR側の既存のSocketの下にIN、OUT、IOのSocketを追加し、Deviceを拡大します。結果には追加された`socket`と`errors`が含まれます。Socketが追加されなかった場合、`socket`は`None`です。ループとX SocketはDeviceと同時にのみ作成できます（`CreateFromJSON`）。 |
| `CreateDeviceType(deviceJson: str = '') -> ConnectCADDeviceObject.DeviceTypeResult` | このDeviceから、"ConnectCAD Device Definition"レコードを持つDevice Typeのシンボル定義"<make> <model>"を作成します（ConnectCAD CC_DeviceType）。`deviceJson`（Device作成に使用した記述）を指定すると、レコードはpinout、extra_data、uuid、source、categoryを含む完全な記述を保持します。同じメーカーとモデルのDevice Typeがすでに図面内にある場合は変更せずに保持します。ConnectCADライブラリにある場合は、新規作成せずに取り込みます。 |

継承メンバー：[`ParametricObject`](ObjectPrimitives.md#parametricobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

#### ConnectCADDeviceObject.CreateResult

> **完全修飾名:** `api.ConnectCADDeviceObject.CreateResult` · **継承元:** `api.Object`

CreateFromJSONの結果。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `CreateResult()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `CreateResult(device, errors, warnings)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `device` | `Handle` | 何も作成されなかった場合はnull。 |
| `errors` | `list[str]` | Deviceが作成されなかった理由。 |
| `warnings` | `list[str]` | Device Typeにのみ保持されるデータ。 |

#### ConnectCADDeviceObject.AddSocketResult

> **完全修飾名:** `api.ConnectCADDeviceObject.AddSocketResult` · **継承元:** `api.Object`

AddSocketの結果。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `AddSocketResult()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `AddSocketResult(socket, errors)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `socket` | `Handle` | Socketが追加されなかった場合はnull。 |
| `errors` | `list[str]` | エラーメッセージ。 |

#### ConnectCADDeviceObject.DeviceTypeResult

> **完全修飾名:** `api.ConnectCADDeviceObject.DeviceTypeResult` · **継承元:** `api.Object`

CreateDeviceTypeの結果。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DeviceTypeResult()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `DeviceTypeResult(symbolDefinition, name, isCreated, isFullDataStored, errors, warnings)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `symbolDefinition` | `Handle` | Device Typeのシンボル定義です。失敗時はnullです。 |
| `name` | `str` | "<make> <model>"。 |
| `isCreated` | `bool` | `False`：同じメーカーとモデルのDevice Typeがすでに図面内にあり、保持されました。 |
| `isFullDataStored` | `bool` | Device記述データ（pinout、extra_data、categoryなど）がそのレコードに含まれています。 |
| `errors` | `list[str]` | エラーメッセージ。 |
| `warnings` | `list[str]` | 警告メッセージ。 |

---

[一覧に戻る](README.md) · [先頭に戻る](#objectsconnectcad--connectcad-devices-and-sockets)
