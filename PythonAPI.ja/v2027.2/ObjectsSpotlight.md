[English](../../PythonAPI/v2027.2/ObjectsSpotlight.md) • [Deutsch](../../PythonAPI.de/v2027.2/ObjectsSpotlight.md) • **日本語**

<a id="objectsspotlight--lighting-devices-and-gdtf-fixture-types"></a>

# ObjectsSpotlight — Lighting DeviceとGDTF器具タイプ

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

Spotlightのクラスです（Spotlightが必要）。`LightingDeviceObject`は照明配置図の器具（"Lighting Device"）で、照明器具シンボル、GDTF器具タイプ（オブジェクト情報パレットの「GDTF Fixture」と「GDTF Fixture Mode」）、またはその両方から描画します。`GDTFLibrary`はSpotlightで利用可能なGDTF器具タイプを一覧表示し、`.gdtf`ファイルを図面に取り込みます。

汎用のパラメータアクセスは[`ParametricObject`](ObjectPrimitives.md#parametricobject)から継承します。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [LightingDeviceObject](#lightingdeviceobject)
  - [GDTFLibrary](#gdtflibrary)
    - [GDTFLibrary.Entry](#gdtflibraryentry)
    - [GDTFLibrary.ImportResult](#gdtflibraryimportresult)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`LightingDeviceObject`](#lightingdeviceobject) | クラス | [`ParametricObject`](ObjectPrimitives.md#parametricobject) | SpotlightプラグインのLighting Deviceプラグインオブジェクトです（ユニバーサル名は"Lighting Device"）。 |
| [`GDTFLibrary`](#gdtflibrary) | クラス |  | Spotlightが認識するGDTF器具タイプ（General Device Type Format、DIN SPEC 15800）です。 |
| [`GDTFLibrary.Entry`](#gdtflibraryentry) | クラス（入れ子） |  | 利用可能な器具タイプの一つのDMXモード。 |
| [`GDTFLibrary.ImportResult`](#gdtflibraryimportresult) | クラス（入れ子） |  | Importの結果です。GDTFシンボル定義、そのGDTF名、この呼び出しで取り込んだかどうか、ファイルをGDTFとして読み取ったかどうかを示します。 |

<a id="classes"></a>

## クラス

### LightingDeviceObject

> **完全修飾名:** `api.LightingDeviceObject` · **継承元:** [`ParametricObject`](ObjectPrimitives.md#parametricobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

SpotlightプラグインのLighting Deviceプラグインオブジェクトです（ユニバーサル名は"Lighting Device"）。

汎用のパラメータアクセス（GetParamString / SetParamString / ...、GetParameters、GetParamChoices）はParametricObjectから継承します。

Lighting Deviceは、照明配置図の一つの器具（またはマルチセルのLighting Device）を表します。図形は照明器具シンボル（"Symbol Name"）および／またはGDTF器具タイプ（"UseGDTFGeometry"を使用する"GDTF Fixture Name"）から取得します。GDTF器具タイプはDMXモードとフットプリントも提供します。

一般的なGDTFワークフロー（利用可能な器具タイプはGDTFLibraryを参照）：

1. `GDTFLibrary.Import`(path) — - .gdtfファイルを図面に取り込みます（Lighting Deviceが使用できるのは、図面内にある器具タイプのみ）
2. `LightingDeviceObject.Create`(position) — - 照明器具シンボルのない器具
3. device.SetGDTF(gdtfName, mode) — - 器具タイプ、DMXモード、フットプリント
4. device.SetUseGDTFGeometry(`True`) — - GDTFの3Dモデルを描画します
5. device.`Reset()` — - 器具を再生成します

名前付きアクセサーでアクセスできる主なパラメータ：

- "Inst Type" — オブジェクト情報パレットとレポートに表示されるInstrument Type
- "Symbol Name" — 照明器具シンボル（ここでは読み取り専用。シンボルの割り当てはSpotlightで行います）
- "GDTF Fixture Name" — 器具タイプのGDTF名（`GDTFLibrary.Entry.gdtfName`）
- "GDTF Fixture Mode" — "<DMX mode>.<GDTF name>"。GetGDTFModeはDMXモードのみを返します
- "Num Channels" — DMX Footprint
- "UseGDTFGeometry" — GDTF器具タイプの3Dモデルを描画

GetParam.../SetParam...用の追加パラメータ（パラメータ名 | 型 | 注記）。マルチセル器具はこれらのうち複数をセルごとに格納し、レコードは最初のセルの値を保持します。

- "Device Type" — popup — Light / ...
- "Purpose", "Position", "Unit Number", "Color", "Dimmer", "Channel" — string
- "Universe", "DMX Address", "Absolute Address", "UniverseAddress" — string / int
- "Circuit Number", "Circuit Name", "System", "Breaker ID" — string
- "Wattage", "Voltage", "Weight", "Cost", "Time", "Mark" — string
- "Frame Size", "Template", "Template2", "TemplateRot1", "TemplateRot2" — string / real（度）
- "Field Angle", "Field Angle 2", "Beam Angle", "Beam Angle 2" — real（度）
- "Lamp Rotation Angle", "Fall off distance", "Throw Distance" — real
- "Draw Beam", "Draw Beam as Solid", "Use Vertical Beam", "Light On" — bool
- "Focus", "Pan", "Tilt" — string / real（度）
- "User Field 1" .. "User Field 6" — string
- "Fixture Mode", "Vision Fixture Name" — string（Visionの器具ライブラリ）
- "GDTF Fixture Type ID", "GDTF Fixture Custom ID" — string
- "Lightwright ID", "UID" — string

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `LightingDeviceObject(h: Handle)` | 既存のLighting Device`h`を参照します。使用前に`IsValid()`で確認してください。 |

**メソッド**

*全般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrueです。 |
| `Create(position: Math.Point2D, angle: float = 0.0) -> LightingDeviceObject` *静的* | アクティブレイヤ／現在のコンテナの`position`に、`angle`（ラジアン）だけ回転させた照明器具シンボルのないLighting Deviceを作成し、一度再生成します。SetGDTFでGDTF器具タイプを割り当ててから、`Reset()`を呼び出してください。 |
| `Duplicate() -> LightingDeviceObject` | 図面内のLighting Deviceを複製し、そのコピーを返します。 |
| `GetInstrumentType() -> str \| None` | Instrument Typeを返します。 |
| `SetInstrumentType(value: str) -> bool` | Instrument Typeを設定します。 |
| `GetSymbolName() -> str \| None` | 照明器具シンボルの名前です。シンボルのない器具では空です。 |

*GDTF器具タイプ*

| メソッド | 説明 |
|---|---|
| `GetGDTFName() -> str \| None` | 器具のGDTF名（`GDTFLibrary.Entry.gdtfName`）です。ない場合は空です。 |
| `GetGDTFMode() -> str \| None` | GDTF器具タイプのDMXモードです。プラグインが末尾に付けるGDTF名は含みません。 |
| `GetDMXFootprint() -> int \| None` | 器具のDMX Footprint（チャンネル数）。 |
| `SetGDTF(gdtfName: str, mode: str = '') -> bool` | GDTF器具タイプ`gdtfName`（`GDTFLibrary.GetAvailable`の取り込み済み項目）をDMXモード`mode`で割り当てます。`mode`が空の場合は器具タイプの最初のモードを使用します。リソースマネージャでGDTFを器具にドロップした場合と同様に、そのデータ（モード、フットプリントなど）を適用します。その後に`Reset()`を呼び出してください。この名前とモードの器具タイプが図面内にない場合は、器具を変更せずに`False`を返します。 |
| `GetUseGDTFGeometry() -> bool \| None` | 器具がGDTF器具タイプの3Dモデルを描画するかどうか。変更後に`Reset()`を呼び出してください。 |
| `SetUseGDTFGeometry(value: bool) -> bool` | *GDTFジオメトリを使用*のオン／オフを切り替えます。器具がGDTF器具タイプの3Dモデルを描画するかどうか。変更後に`Reset()`を呼び出してください。 |

継承メンバー：[`ParametricObject`](ObjectPrimitives.md#parametricobject)、[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject)のすべて。

### GDTFLibrary

> **完全修飾名:** `api.GDTFLibrary` · **継承元:** `api.Object`

Spotlightが認識するGDTF器具タイプ（General Device Type Format、DIN SPEC 15800）です。

利用可能な器具タイプは、図面に取り込まれたもの（GDTFシンボル定義として格納）と、ユーザーフォルダおよびアプリケーションフォルダのSpotlightデータのGDTFフォルダにある.gdtfファイルです。Spotlightはセッションごとに一度だけフォルダを読み取るため、後からそこにコピーしたファイルは再起動後にのみ一覧表示されます。Lighting Deviceで使用するには、器具タイプを先に図面に取り込む（Import）必要があります。SpotlightとGDTFのプラグインが必要です。ない場合はリストが空になり、Importは失敗します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `GDTFLibrary()` | 状態を持たないオブジェクトです。すべてのメソッドは静的で、クラス自体から呼び出せます。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `IsAvailable() -> bool` *静的* | SpotlightのGDTFサポートがインストールされているかどうか。 |
| `GetAvailable() -> list[GDTFLibrary.Entry]` *静的* | 利用可能なすべての器具タイプのすべてのDMXモードです。最初に取り込み済みのもの、次にディスク上のファイルが並びます。`LightingDeviceObject.SetGDTF`が受け入れるのは取り込み済みの器具タイプ（isInDocument）のみです。 |
| `Import(filePath: str, replaceExisting: bool = False) -> GDTFLibrary.ImportResult` *静的* | `filePath`（ネイティブ形式のフルパス）の.gdtfファイルをGDTFシンボル定義として図面に取り込みます。同じGDTFタイプIDの器具タイプがすでに図面内にある場合、`replaceExisting`が`True`なら置き換え、そうでなければ変更せずに保持します（その場合、isImportedは`False`。GetAvailableで検索してください）。ユーザーへの確認は行いません。取り消しイベントが開いている場合、新しい器具タイプは自分自身の取り消しを記録します。既存の器具タイプの置き換えはその場で変更を行い、以前の状態は取り消し用に記録されません。 |

#### GDTFLibrary.Entry

> **完全修飾名:** `api.GDTFLibrary.Entry` · **継承元:** `api.Object`

利用可能な器具タイプの一つのDMXモード。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Entry()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `Entry(gdtfName, fixtureName, manufacturer, mode, footprint, symbolDefinition, isInDocument)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `gdtfName` | `str` | `LightingDeviceObject.SetGDTF`に渡す名前。 |
| `fixtureName` | `str` | 器具タイプ名。リビジョンがある場合は末尾に"@<revision>"が付きます。 |
| `manufacturer` | `str` | 器具タイプのメーカー。 |
| `mode` | `str` | DMXモード名。 |
| `footprint` | `int` | モードのDMXチャンネル。 |
| `symbolDefinition` | `Handle` | GDTFシンボル定義です。取り込まれていないファイルではnullです。 |
| `isInDocument` | `bool` | 図面に取り込み済み。 |

#### GDTFLibrary.ImportResult

> **完全修飾名:** `api.GDTFLibrary.ImportResult` · **継承元:** `api.Object`

Importの結果。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ImportResult()` | デフォルト値です（各フィールドはデフォルトの状態）。 |
| `ImportResult(symbolDefinition, gdtfName, isImported, isValidFile)` | フィールド値です。すべてのフィールドをこの順序で位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `symbolDefinition` | `Handle` | 取り込みによって作成または置換されたGDTFシンボル定義。 |
| `gdtfName` | `str` | 取り込まれた器具タイプのGDTF名。`LightingDeviceObject.SetGDTF`用です。 |
| `isImported` | `bool` | ファイルを読み取らなかった場合、または器具タイプがすでに図面内にあり保持された場合は`False`です。 |
| `isValidFile` | `bool` | ファイルをGDTFとして読み取りました。ファイルが存在しない場合や無効な場合は`False`です。 |

---

[一覧に戻る](README.md) · [先頭に戻る](#objectsspotlight--lighting-devices-and-gdtf-fixture-types)
