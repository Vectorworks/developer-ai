[English](../../PythonAPI/v2027.2/Scripting.md) • [Deutsch](../../PythonAPI.de/v2027.2/Scripting.md) • **日本語**

<a id="scripting--script-resources-and-script-palettes"></a>

# Scripting — スクリプトリソースとスクリプトパレット

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

スクリプトのクラス群。`ScriptResource`は現在のファイルに保存されたVectorScriptまたはPythonスクリプトで、作成、検索、読み取り、変更、削除ができます。`ScriptPalette`はスクリプトパレットであり、スクリプトリソースの名前付きグループです。Vectorworksでは、フローティングパレットとして、またリソースマネージャ内のスクリプトのフォルダとして表示されます。

このAPIを通じてスクリプトの作成、読み取り、変更、整理ができます。スクリプトの実行はこのAPIの対象ではありません。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [ScriptResource](#scriptresource)
  - [ScriptPalette](#scriptpalette)
- [列挙型](#enumerations)
  - [ScriptLanguage](#scriptlanguage)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`ScriptResource`](#scriptresource) | クラス |  | ハンドルで識別される一つのスクリプトリソース。 |
| [`ScriptPalette`](#scriptpalette) | クラス |  | ハンドルで識別される一つのスクリプトパレット。 |
| [`ScriptLanguage`](#scriptlanguage) | IntEnum |  | スクリプトの言語。 |

<a id="classes"></a>

## クラス

### ScriptResource

> **完全修飾名:** `api.ScriptResource` · **継承元:** `api.Object`

ハンドルで識別される一つのスクリプトリソース。このAPIのすべてのオブジェクトクラスと同様に軽量なビューであり、これをコピーしてもスクリプトはコピーされず、これを破棄してもスクリプトは削除されません。スクリプトリソースでないハンドルから生成すると、無効なオブジェクトになります（`IsValid()` == `False`）。その場合、ゲッターは`None`を返し、セッター／操作は`False`を返します。文字列はUTF-8で、スクリプトのテキストは"\n"を改行に使用します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ScriptResource(hScript: Handle)` | 既存のスクリプト`hScript`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*型*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | ハンドルがスクリプトリソースの場合は`True`（登録ビューは含みません）。 |

*検索*

| メソッド | 説明 |
|---|---|
| `FromName(name: str) -> ScriptResource` *静的* | 現在のファイルにある、その名前のスクリプトリソース。存在しない場合は無効。 |
| `GetAll() -> list[ScriptResource]` *静的* | 現在のファイルのすべてのスクリプトリソース。名前順。 |

*作成*

| メソッド | 説明 |
|---|---|
| `Create(name: str, paletteName: str, text: str, language: ScriptLanguage) -> ScriptResource` *静的* | スクリプトパレット`paletteName`内にスクリプトリソースを作成します。パレットがない場合は、先に作成して開きます。`name`または`paletteName`が空または63文字を超える場合、両者が同じ場合、ファイル内のオブジェクトがすでに`name`を使用している場合、あるいは`paletteName`がスクリプトパレット以外のオブジェクトの名前である場合は失敗します（無効なオブジェクト）。取り消し：Vectorworksは新しいパレットを登録しますが、新しいスクリプトは登録しません。取り消しイベント内でスクリプトを`Document.AddAfterSwapObject`により登録し、パレットは再度登録しないでください。 |

*識別情報*

| メソッド | 説明 |
|---|---|
| `GetHandle() -> Handle` | スクリプトのハンドル。 |
| `IsValid() -> bool` | このオブジェクトが既存のスクリプトを参照している場合はTrue。 |
| `GetName() -> str \| None` | 名前を返します。 |
| `SetName(name: str) -> bool` | スクリプトの名前を変更します。名前が63文字を超える場合、または別のオブジェクトがすでに使用している場合は失敗します。 |

*スクリプト*

| メソッド | 説明 |
|---|---|
| `GetLanguage() -> ScriptLanguage \| None` | 言語を返します。 |
| `GetText() -> str \| None` | テキストを返します。 |
| `SetText(text: str) -> bool` | テキストを置き換え、言語は維持します。スクリプトパレットは実行したスクリプトのコンパイル済みコピーを保持し、ユーザーがパレットから再度実行すると、そのコピーを実行します。これは、Vectorworksでスクリプトが編集されるか、ファイルが再度開かれるまで続きます。Executeは常に現在のテキストを実行します。 |
| `SetText(text: str, language: ScriptLanguage) -> bool` | テキストと言語を置き換えます（上記のSetTextを参照）。 |

*スクリプトパレット*

| メソッド | 説明 |
|---|---|
| `GetPalette() -> ScriptPalette` | スクリプトを含むパレット。 |

*ライフサイクル*

| メソッド | 説明 |
|---|---|
| `Delete(useUndo: bool = True) -> bool` | ファイルからスクリプトを削除し、このオブジェクトを無効にします。実行中のスクリプトが削除対象である可能性があるため、スクリプトの実行中は失敗します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`：オブジェクトが有効な場合はTrue（`IsValid()`と同じ）。 |
| `==` | `__eq__(o: ScriptResource) -> bool` | `a == b`：両方のオブジェクトが同じスクリプトを参照している場合はTrue。 |
| `!=` | `__ne__(o: ScriptResource) -> bool` | `a != b`：オブジェクトが異なるスクリプトを参照している場合はTrue。 |

### ScriptPalette

> **完全修飾名:** `api.ScriptPalette` · **継承元:** `api.Object`

ハンドルで識別される一つのスクリプトパレット。ScriptResourceと同様に軽量です。スクリプトパレットでないハンドルから生成すると、無効なオブジェクトになります（`IsValid()` == `False`）。その場合、ゲッターは`None`を返し、セッター／操作は`False`を返します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ScriptPalette(hPalette: Handle)` | 既存のスクリプトパレット`hPalette`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*型*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | ハンドルがスクリプトパレットの場合は`True`（登録ビューパレットは含みません）。 |

*検索*

| メソッド | 説明 |
|---|---|
| `FromName(name: str) -> ScriptPalette` *静的* | 現在のファイルにある、その名前のスクリプトパレット。存在しない場合は無効。 |
| `GetAll() -> list[ScriptPalette]` *静的* | 現在のファイルのすべてのスクリプトパレット。名前順。 |

*識別情報*

| メソッド | 説明 |
|---|---|
| `GetHandle() -> Handle` | スクリプトパレットのハンドル。 |
| `IsValid() -> bool` | このオブジェクトが既存のスクリプトパレットを参照している場合はTrue。 |
| `GetName() -> str \| None` | 名前を返します。 |
| `SetName(name: str) -> bool` | パレットの名前を変更します。名前が63文字を超える場合、または別のオブジェクトがすでに使用している場合は失敗します。 |

*スクリプト*

| メソッド | 説明 |
|---|---|
| `GetScripts() -> list[ScriptResource]` | パレットのスクリプトリソース。パレット内の順序。 |
| `GetScriptCount() -> int` | スクリプト項目の数。 |

*表示*

| メソッド | 説明 |
|---|---|
| `SetOpen(isOpen: bool) -> bool` | フローティングパレットを表示（`True`）または閉じます（`False`）。 |

*ライフサイクル*

| メソッド | 説明 |
|---|---|
| `Delete(useUndo: bool = True) -> bool` | パレットとそのすべてのスクリプトを削除し、このオブジェクトを無効にします。実行中のスクリプトが削除対象の一つである可能性があるため、スクリプトの実行中は失敗します。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`：オブジェクトが有効な場合はTrue（`IsValid()`と同じ）。 |
| `==` | `__eq__(o: ScriptPalette) -> bool` | `a == b`：両方のオブジェクトが同じスクリプトパレットを参照している場合はTrue。 |
| `!=` | `__ne__(o: ScriptPalette) -> bool` | `a != b`：オブジェクトが異なるスクリプトパレットを参照している場合はTrue。 |

<a id="enumerations"></a>

## 列挙型

### ScriptLanguage

> **完全修飾名:** `api.ScriptLanguage` · **種類:** `IntEnum`

スクリプトの言語。

| メンバー | 値 | 説明 |
|---|---|---|
| `VectorScript` | `0` | Pascalに似たVectorworksのスクリプト言語。 |
| `Python` | `1` | Vectorworksの"vs"および"api"モジュールを使用するPython。 |

---

[一覧に戻る](README.md) · [先頭に戻る](#scripting--script-resources-and-script-palettes)
