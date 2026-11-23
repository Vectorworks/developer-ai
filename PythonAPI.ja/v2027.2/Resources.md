[English](../../PythonAPI/v2027.2/Resources.md) • [Deutsch](../../PythonAPI.de/v2027.2/Resources.md) • **日本語**

<a id="resources--resources-resource-lists-and-typed-resources"></a>

# Resources — リソース、リソースリスト、型付きリソース

> **Pythonモジュール:** `api` · **バージョン:** Vectorworks 2027 Update 2

[一覧に戻る](README.md)

リソースのクラス群（APIのリソースマネージャに相当する部分）。`Resource`は任意の種類の一つのリソース（名前、説明、フォルダ、内容、ライフサイクル）です。`ResourceList`は、現在の図面または外部コンテンツ（Vectorworksライブラリ、ファイル、開いている別のファイル）にある一種類のリソースを一覧表示し、図面に取り込みます。`TypedResource`は型付きリソースクラスの基底クラスです。型付きリソースオブジェクトは、ハンドルが実際にその種類のリソースを表していない限り無効となるため、誤った種類のリソースを操作することはありません。

型付きクラスは、その種類に固有の機能を追加します。対象は、ハッチング、グラデーション、タイル、イメージによる面、ラインタイプ、シンボル定義、テクスチャ、レンダリングスタイルと背景テクスチャ、レコードフォーマット、ワークシート、文字・壁・スラブ・屋根・ビューポートのスタイル、マテリアル、データの可視化、リソースフォルダです。クラスもリソースですが、[`ClassAttributes`](Attributes.md#classattributes)で扱います。

<a id="table-of-contents"></a>

## 目次

- [概要](#overview)
- [クラス](#classes)
  - [Resource](#resource)
  - [ResourceList](#resourcelist)
    - [ResourceList.Entry](#resourcelistentry)
    - [ResourceList.ImportResult](#resourcelistimportresult)
  - [TypedResource](#typedresource)
  - [HatchLevel](#hatchlevel)
  - [Hatch](#hatch)
  - [GradientSegment](#gradientsegment)
  - [Gradient](#gradient)
  - [Tile](#tile)
  - [ImageFill](#imagefill)
    - [ImageFill.Compression](#imagefillcompression)
  - [LineType](#linetype)
  - [RecordField](#recordfield)
  - [RecordFormat](#recordformat)
  - [Texture](#texture)
    - [Texture.Part](#texturepart)
  - [RenderStyle](#renderstyle)
  - [RenderBackground](#renderbackground)
    - [RenderBackground.Kind](#renderbackgroundkind)
  - [TextStyle](#textstyle)
  - [WallStyle](#wallstyle)
  - [SlabStyle](#slabstyle)
  - [RoofStyle](#roofstyle)
  - [ViewportStyle](#viewportstyle)
  - [BuildingMaterial](#buildingmaterial)
  - [DataVisualization](#datavisualization)
  - [ResourceFolderPath](#resourcefolderpath)
  - [ResourceFolder](#resourcefolder)
  - [SymbolDefinition](#symboldefinition)
    - [SymbolDefinition.GeometryType](#symboldefinitiongeometrytype)
    - [SymbolDefinition.InsertMode](#symboldefinitioninsertmode)
    - [SymbolDefinition.BreakMode](#symboldefinitionbreakmode)
  - [WorksheetCell](#worksheetcell)
  - [WorksheetCellContent](#worksheetcellcontent)
  - [Worksheet](#worksheet)
- [列挙型](#enumerations)
  - [ResourceType](#resourcetype)
  - [ContentFolder](#contentfolder)
  - [ImportConflict](#importconflict)
  - [RecordFieldType](#recordfieldtype)

<a id="overview"></a>

## 概要

| 名前 | 種類 | 継承元 | 概要 |
|---|---|---|---|
| [`Resource`](#resource) | クラス |  | ハンドルで識別される一つのリソース。 |
| [`ResourceList`](#resourcelist) | クラス |  | 現在の図面または外部コンテンツにある、一種類のリソースのリスト。 |
| [`ResourceList.Entry`](#resourcelistentry) | クラス（入れ子） |  | リストの一つのエントリ。 |
| [`ResourceList.ImportResult`](#resourcelistimportresult) | クラス（入れ子） |  | ImportWithResultの結果：図面内のリソースと、この呼び出しでコピーされたかどうか（すでに図面にあるリソースが返された場合は`False`）。 |
| [`TypedResource`](#typedresource) | クラス | [`Resource`](#resource) | 一つのResourceTypeに限定されたリソース。 |
| [`HatchLevel`](#hatchlevel) | クラス |  | ハッチングの一つの線群。 |
| [`Hatch`](#hatch) | クラス | [`TypedResource`](#typedresource) | ベクターハッチングによる面（`ObjectType.HatchDefinition`）：塗りつぶす領域全体で繰り返される線群の集合。 |
| [`GradientSegment`](#gradientsegment) | クラス |  | グラデーションの一つの変化点。 |
| [`Gradient`](#gradient) | クラス | [`TypedResource`](#typedresource) | グラデーションによる面（`ObjectType.GradientDefinition`）：二つ以上の変化点間の混合。 |
| [`Tile`](#tile) | クラス | [`TypedResource`](#typedresource) | タイルによる面（`ObjectType.TileDefinition`）：塗りつぶす領域全体で、グリッドに沿って繰り返される2Dオブジェクトのグループ。 |
| [`ImageFill`](#imagefill) | クラス | [`TypedResource`](#typedresource) | イメージリソース（`ObjectType.ImageDefinition`）：イメージによる面、添景、またはテクスチャ画像として使用するビットマップ。 |
| [`ImageFill.Compression`](#imagefillcompression) | IntEnum（入れ子） |  | 画像の保存に使用される圧縮方式。 |
| [`LineType`](#linetype) | クラス | [`TypedResource`](#typedresource) | ラインタイプリソース。 |
| [`RecordField`](#recordfield) | クラス |  | レコードフォーマットの一つのフィールド。 |
| [`RecordFormat`](#recordformat) | クラス | [`TypedResource`](#typedresource) | レコードフォーマット。 |
| [`Texture`](#texture) | クラス | [`TypedResource`](#typedresource) | テクスチャ（`ObjectType.Texture`）：レンダリングする面の色、反射、透明度、バンプ。 |
| [`Texture.Part`](#texturepart) | IntEnum（入れ子） |  | テクスチャを適用するオブジェクトの部分。 |
| [`RenderStyle`](#renderstyle) | クラス | [`TypedResource`](#typedresource) | レンダリングスタイル（`ObjectType.RenderStyle`）：ビューポートまたはレイヤに適用する、保存されたレンダリング設定。 |
| [`RenderBackground`](#renderbackground) | クラス | [`TypedResource`](#typedresource) | 背景テクスチャ（`ObjectType.RenderBackground`）：レンダリング時にモデルの背後に表示するもの。 |
| [`RenderBackground.Kind`](#renderbackgroundkind) | IntEnum（入れ子） |  | 新しいリソースを作成するときの背景の種類。 |
| [`TextStyle`](#textstyle) | クラス | [`TypedResource`](#typedresource) | 文字スタイル（`ObjectType.TextStyle`）：文字列オブジェクトと寸法に適用するフォント、サイズ、文字属性。 |
| [`WallStyle`](#wallstyle) | クラス | [`TypedResource`](#typedresource) | 壁スタイル（`ObjectType.WallStyle`）：壁の構成要素、厚さ、属性。 |
| [`SlabStyle`](#slabstyle) | クラス | [`TypedResource`](#typedresource) | スラブスタイル（`ObjectType.SlabStyle`）：スラブの構成要素と属性。 |
| [`RoofStyle`](#roofstyle) | クラス | [`TypedResource`](#typedresource) | 屋根スタイル（`ObjectType.RoofStyle`）：屋根の構成要素と属性。 |
| [`ViewportStyle`](#viewportstyle) | クラス | [`TypedResource`](#typedresource) | ビューポートスタイル（`ObjectType.ViewportStyle`）：シートレイヤビューポートの保存された設定。 |
| [`BuildingMaterial`](#buildingmaterial) | クラス | [`TypedResource`](#typedresource) | マテリアル（建材、`ObjectType.BuildingMaterial`）：壁、スラブ、屋根の構成要素の物理的な材料。 |
| [`DataVisualization`](#datavisualization) | クラス | [`TypedResource`](#typedresource) | データの可視化（`ObjectType.DataVisualization`）：検索条件に一致するオブジェクトのグラフィック属性を上書きするルール。ビューポートまたは... |
| [`ResourceFolderPath`](#resourcefolderpath) | クラス |  | `ResourceFolder.CreatePathFolders`が作成したパスのフォルダ：パス内のすべてのフォルダと、その呼び出しが作成したフォルダを、外側から順に示します。 |
| [`ResourceFolder`](#resourcefolder) | クラス | [`TypedResource`](#typedresource) | リソースフォルダ（`ObjectType.Folder`）：リソースマネージャで一種類のリソースをまとめます。 |
| [`SymbolDefinition`](#symboldefinition) | クラス | [`TypedResource`](#typedresource) | シンボル定義。 |
| [`SymbolDefinition.GeometryType`](#symboldefinitiongeometrytype) | IntEnum（入れ子） |  | シンボルが描画できるもの：2Dのみ、3Dのみ、または両方（ハイブリッドシンボルは平面ビューで2D部分を表示します）。 |
| [`SymbolDefinition.InsertMode`](#symboldefinitioninsertmode) | IntEnum（入れ子） |  | シンボルを挿入する壁に対する、シンボルの配置位置。 |
| [`SymbolDefinition.BreakMode`](#symboldefinitionbreakmode) | IntEnum（入れ子） |  | シンボルの挿入箇所で壁を切り欠く方法。 |
| [`WorksheetCell`](#worksheetcell) | クラス |  | ワークシートのセル。 |
| [`WorksheetCellContent`](#worksheetcellcontent) | クラス |  | 内容を持つ一つのセル。 |
| [`Worksheet`](#worksheet) | クラス | [`TypedResource`](#typedresource) | ワークシート。 |
| [`ResourceType`](#resourcetype) | IntEnum |  | リソースの種類。 |
| [`ContentFolder`](#contentfolder) | IntEnum |  | 外部（ライブラリ／デフォルト）リソースを格納するVectorworksの標準コンテンツフォルダ（標準リソースのフォルダ）。 |
| [`ImportConflict`](#importconflict) | IntEnum |  | 現在の図面にリソースを取り込む際、同名のリソースがすでに存在する場合の名前の競合の解決方法。 |
| [`RecordFieldType`](#recordfieldtype) | IntEnum |  | レコードフィールドのデータ型。 |

<a id="classes"></a>

## クラス

### Resource

> **完全修飾名:** `api.Resource` · **継承元:** `api.Object`

ハンドルで識別される一つのリソース。このAPIのすべてのオブジェクトクラスと同様に軽量なビューであり、これをコピーしてもリソースはコピーされず、これを破棄してもリソースは削除されません。リソースでないハンドルから生成すると、無効なオブジェクトになります（`IsValid()` == `False`）。その場合、ゲッターは`None`を返し、セッター／操作は`False`を返します。文字列はUTF-8です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Resource(hResource: Handle)` | 既存のリソース`hResource`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*型*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | ハンドルがResourceTypeのいずれかの種類のリソースである場合は`True`。 |
| `TypeOf(h: Handle) -> ResourceType` *静的* | ハンドル`h`のリソースタイプ。 |
| `GetTypeName(type: ResourceType) -> str` *静的* | リソースタイプの安定したローワーキャメルケース名（"symbolDefinition"、"hatch"、"texture"など）。`ResourceType.Unknown`の場合は空の文字列を返します。 |
| `GetTypeFromName(typeName: str) -> ResourceType` *静的* | GetTypeNameが返すタイプ名を解析します（大文字小文字を区別しません）。一致しない場合はUnknownを返します。 |
| `GetAllTypes() -> list[ResourceType]` *静的* | このAPIが認識するすべてのリソースタイプ。上記の順序で返します。 |

*検索*

| メソッド | 説明 |
|---|---|
| `FromName(name: str) -> Resource` *静的* | 現在の図面にある、その名前のリソース。存在しない場合は無効。 |
| `FromIndex(index: int) -> Resource` *静的* | その内部インデックスを持つリソース（ハッチング／グラデーション／タイル／イメージ／ラインタイプ／テクスチャのインデックス）。 |

*識別情報*

| メソッド | 説明 |
|---|---|
| `GetHandle() -> Handle` | リソースのハンドル。 |
| `IsValid() -> bool` | このオブジェクトが既存のリソースを参照している場合はTrue。 |
| `GetResourceType() -> ResourceType` | リソースタイプを返します。 |
| `GetObjectType() -> ObjectType` | オブジェクトタイプを返します。 |
| `GetResourceTypeName() -> str` | リソースタイプ名を返します。 |
| `GetName() -> str \| None` | 名前を返します。 |
| `SetName(name: str) -> bool` | リソースの名前を変更します。別のオブジェクトがすでにその名前を使用している場合は失敗します。 |
| `GetDescription() -> str \| None` | 説明を返します。 |
| `SetDescription(description: str) -> bool` | 説明を設定します。 |
| `GetInternalIndex() -> int \| None` | 内部インデックスを返します。 |
| `GetUuid() -> str \| None` | リソースの永続UUID。セッションをまたいでも変わりません。 |

*リソースフォルダ*

| メソッド | 説明 |
|---|---|
| `GetFolder() -> Handle` | このリソースを含むフォルダリソース。リソースマネージャの最上位にある場合はヌル。 |
| `GetFolderName() -> str \| None` | フォルダ名を返します。 |
| `MoveToFolder(hFolder: Handle) -> bool` | リソースを`hFolder`（`ResourceType.Folder`リソース）に移動します。 |

*内容*

| メソッド | 説明 |
|---|---|
| `IsContainer() -> bool` | 他のオブジェクトを含むリソース（シンボル定義とリソースフォルダ）の場合は`True`。 |
| `GetContents() -> list[Handle]` | リソース内のオブジェクト（シンボル定義の形状、フォルダ内のリソース）。 |
| `GetContentCount() -> int` | 内容の項目数。 |
| `ForEachContent(callback: callable(Handle)) -> None` | リソース内の各オブジェクトを渡して`callback`を呼び出します。リソース内のオブジェクト（シンボル定義の形状、フォルダ内のリソース）を対象とします。 |

*属性*

| メソッド | 説明 |
|---|---|
| `Attributes() -> ObjectAttributes` | グラフィック属性を持つ種類のリソースの、グラフィック属性。 |

*ライフサイクル*

| メソッド | 説明 |
|---|---|
| `Duplicate() -> Resource` | 同じファイルとフォルダ内のリソースのコピー。失敗した場合は無効。 |
| `Delete(useUndo: bool = True) -> bool` | ファイルからリソースを削除し、このオブジェクトを無効にします。そのリソースを使用しているオブジェクトは、リソースを失います。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`：オブジェクトが有効な場合はTrue（`IsValid()`と同じ）。 |
| `==` | `__eq__(o: Resource) -> bool` | `a == b`：両方のオブジェクトが同じリソースを参照している場合はTrue。 |
| `!=` | `__ne__(o: Resource) -> bool` | `a != b`：オブジェクトが異なるリソースを参照している場合はTrue。 |

### ResourceList

> **完全修飾名:** `api.ResourceList` · **継承元:** `api.Object`

現在の図面または外部コンテンツにある、一種類のリソースのリスト。コピーはできません。Vectorworksのリソースリストを保持し、Pythonオブジェクトが削除されると解放します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ResourceList()` | 空の無効なリスト。`Build...`メソッドのいずれかで内容を設定してください。 |
| `ResourceList(type: ResourceType)` | そのタイプの空のリスト。 |

**メソッド**

*構築*

| メソッド | 説明 |
|---|---|
| `BuildFromDocument(type: ResourceType, sort: bool = True) -> bool` | 現在の図面で定義されている`type`のリソース。 |
| `BuildFromFolder(type: ResourceType, folder: ContentFolder, subFolder: str = '', includeDocument: bool = False, sort: bool = True) -> bool` | Vectorworksの標準コンテンツフォルダ（外部／標準リソース）内の`type`のリソース。`subFolder`は検索範囲をそのサブフォルダ（または部分パス）に限定し、空の場合はフォルダ全体を対象とします。`includeDocument`を指定すると、現在の図面のリソースも一覧に含めます。 |
| `BuildFromFolderIndex(type: ResourceType, folderIndex: int, subFolder: str = '', sort: bool = True) -> bool` | 同様の処理ですが、ContentFolderに名前のないフォルダ指定子を対象とします。`folderIndex`が正の場合は現在の図面のリソースも一覧に含め、負の場合はフォルダのみ、0の場合は図面のみを対象とします。 |
| `BuildFromFile(type: ResourceType, filePath: str) -> bool` | ネイティブ形式のフルパスで指定された一つのVectorworksファイル内の、`type`のリソース。 |
| `BuildFromOpenDocument(type: ResourceType, openDocumentIndex: int, sort: bool = True) -> bool` | 現在開かれている別のファイルの`type`のリソース（Vectorworksの開いているファイルのリストを参照）。 |
| `FromDocument(type: ResourceType, sort: bool = True) -> ResourceList` *静的* | Build...メソッドに相当するファクトリメソッド。 |
| `FromFolder(type: ResourceType, folder: ContentFolder, subFolder: str = '', includeDocument: bool = False, sort: bool = True) -> ResourceList` *静的* | `type`のリソースをコンテンツフォルダ`folder`から取得した新しいリスト。Build...メソッドに相当するファクトリメソッドです。 |
| `FromFolderIndex(type: ResourceType, folderIndex: int, subFolder: str = '', sort: bool = True) -> ResourceList` *静的* | `type`のリソースをインデックス`folderIndex`のコンテンツフォルダから取得した新しいリスト。Build...メソッドに相当するファクトリメソッドです。 |
| `FromFile(type: ResourceType, filePath: str) -> ResourceList` *静的* | `type`のリソースをVectorworksファイル`filePath`から取得した新しいリスト。Build...メソッドに相当するファクトリメソッドです。 |
| `FromOpenDocument(type: ResourceType, openDocumentIndex: int, sort: bool = True) -> ResourceList` *静的* | 開いている別のファイルにある`type`のリソースの新しいリスト。Build...メソッドに相当するファクトリメソッドです。 |
| `Dispose() -> None` | Vectorworksのリソースリストを解放します。Pythonオブジェクトが削除されると自動的に呼び出されます。 |

*識別情報*

| メソッド | 説明 |
|---|---|
| `IsValid() -> bool` | このオブジェクトが既存のリソースリストを参照している場合はTrue。 |
| `GetListID() -> int` | 引き続き必要とする低レベル呼び出し用の、Vectorworksリソースリストの生のID。 |
| `GetResourceType() -> ResourceType` | リソースタイプを返します。 |

*コンテンツフォルダ*

| メソッド | 説明 |
|---|---|
| `GetContentFolderName(folder: ContentFolder) -> str` *静的* | コンテンツフォルダの安定したローワーキャメルケース名（"hatches"、"textures"、"objectStyles"など）。 |
| `GetContentFolderFromName(folderName: str) -> ContentFolder` *静的* | GetContentFolderNameが返す名前を解析します（大文字小文字を区別しません）。一致しない場合は`None`。 |
| `GetAllContentFolders() -> list[ContentFolder]` *静的* | すべてのコンテンツフォルダを返します。 |

*エントリ*

| メソッド | 説明 |
|---|---|
| `GetCount() -> int` | 数を返します。 |
| `IsEmpty() -> bool` | リストにエントリがない場合はTrue。 |
| `GetResource(index: int) -> Resource` | `index`にあるリソース。エントリがまだ取り込まれていない外部コンテンツである間は無効。 |
| `GetName(index: int) -> str \| None` | リソースマネージャに表示される名前（外部コンテンツでは、元のファイル名が含まれることがあります）。 |
| `GetActualName(index: int) -> str \| None` | リソースの実際の名前。取り込み後の名前です。 |
| `GetFolderName(index: int) -> str \| None` | エントリが属するリソースフォルダの名前。最上位では空。 |
| `IsInDocument(index: int) -> bool` | リソースがすでに現在の図面に存在するかどうか。 |
| `GetEntry(index: int) -> ResourceList.Entry \| None` | `index`のエントリを返します。 |
| `GetEntries() -> list[ResourceList.Entry]` | エントリを返します。 |
| `ForEach(callback: callable(ResourceList.Entry)) -> None` | リストの各エントリを渡して`callback`を呼び出します。 |
| `Find(name: str) -> int` | 実際の名前、またはそれで見つからない場合は表示名が`name`であるエントリのインデックス。一致するものがない場合は`kNotFound`を返します。 |
| `Contains(name: str) -> bool` | 実際の名前または表示名が`name`であるエントリがある場合はTrue。 |

*取り込み*

| メソッド | 説明 |
|---|---|
| `Import(index: int, onConflict: ImportConflict = ImportConflict.Rename) -> Resource` | リソースを現在の図面にコピーして返します。すでに取り込まれたリソースはそのまま返します。この呼び出しはファイルを変更するため、取り消しイベント内で実行する必要があります。Vectorworksは、取り込んだリソースを取り消し用に自動登録します。`Document.AddAfterSwapObject`で再度登録しないでください。 |
| `Import(name: str, onConflict: ImportConflict = ImportConflict.Rename) -> Resource` | リソースを現在の図面にコピーして返します。すでに取り込まれたリソースはそのまま返します。この呼び出しはファイルを変更するため、取り消しイベント内で実行する必要があります。Vectorworksは、取り込んだリソースを取り消し用に自動登録します。`Document.AddAfterSwapObject`で再度登録しないでください。 |
| `ImportWithResult(index: int, onConflict: ImportConflict = ImportConflict.Rename) -> ResourceList.ImportResult` | リソースが図面にコピーされたのか、すでに存在するリソースが返されたのかも通知する取り込み。Importと同じ規則が適用されます。 |
| `SetClassRenamePrefix(prefix: str) -> None` | 取り込まれたリソースに付随するクラスの名前に付ける接頭辞。デフォルトは空。 |
| `GetClassRenamePrefix() -> str` | クラス名変更用の接頭辞を返します。取り込まれたリソースに付随するクラスの名前に付ける接頭辞です。デフォルトは空。 |

*リストの編集*

| メソッド | 説明 |
|---|---|
| `Add(hResource: Handle) -> int` | 現在の図面のリソースをリストに追加します。そのインデックスまたは`kNotFound`を返します。 |
| `Remove(index: int) -> bool` | リストからエントリを削除します。リソース自体は削除されません。 |

**演算子とPythonプロトコル**

| 演算子 | メソッド | 説明 |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`：オブジェクトが有効な場合はTrue（`IsValid()`と同じ）。 |

**定数**

| 定数 | 型 | 値 | 説明 |
|---|---|---|---|
| `ResourceList.kNotFound` | `int` | `2**64 - 1` | 一致するエントリがない場合にFindが返す値。 |

#### ResourceList.Entry

> **完全修飾名:** `api.ResourceList.Entry` · **継承元:** `api.Object`

リストの一つのエントリ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Entry()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `Entry(index, name, actualName, folderName, handle, isInDocument)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `index` | `int` | このリスト内の0始まりのインデックス。 |
| `name` | `str` | リソースマネージャに表示される名前。 |
| `actualName` | `str` | 実際のリソース名（識別のためのファイル名を含みません）。 |
| `folderName` | `str` | リソースの親フォルダ。最上位では空。 |
| `handle` | `Handle` | リソースが現在の図面にない間はヌル。 |
| `isInDocument` | `bool` | まだ取り込む必要がある外部コンテンツの場合は`False`。 |

#### ResourceList.ImportResult

> **完全修飾名:** `api.ResourceList.ImportResult` · **継承元:** `api.Object`

ImportWithResultの結果。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ImportResult()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ImportResult(handle, isImported)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `handle` | `Handle` | 現在の図面内のリソース。取り込みに失敗した場合はヌル。 |
| `isImported` | `bool` | この呼び出しでリソースを図面にコピーした場合は`True`（名前変更。 |

### TypedResource

> **完全修飾名:** `api.TypedResource` · **継承元:** [`Resource`](#resource) → `api.Object`

一つのResourceTypeに限定されたリソース。Resourceが提供するすべての機能（名前、説明、フォルダ、複製、削除）は、型付きクラスでも使用できます。

**コンストラクタ**

Pythonからはインスタンス化できません。インスタンスは他のAPI関数から返されます。

**メソッド**

| メソッド | 説明 |
|---|---|
| `GetExpectedType() -> ResourceType` | このクラスが対象とするリソースタイプ。 |

継承：[`Resource`](#resource)のすべて。

### HatchLevel

> **完全修飾名:** `api.HatchLevel` · **継承元:** `api.Object`

ハッチングの一つの線群。`startPoint`と`repeatVector`は、線群の最初の線を定義します。線は`repeatVector`に沿って伸び、その長さが破線パターンの繰り返し長になります。線群は`startPoint` + n * `offsetVector`の位置に平行線として繰り返されます。`dashFactor`は、各繰り返しのうち描画する割合です（0 .. 1、1 = 実線）。距離は、ハッチングがワールド空間で動作する場合はワールド単位、*縮尺無視*（用紙単位を使用）の場合は用紙単位（図面上のmm）です。`Hatch.GetUsePageUnits`を参照してください。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `HatchLevel()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `HatchLevel(startPoint, repeatVector, dashFactor, offsetVector, color, lineWeightMils)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `startPoint` | `Point2D` | 線群の原点。 |
| `repeatVector` | `Point2D` | 線の方向と、線に沿った破線パターンの繰り返し長。 |
| `dashFactor` | `float` | 各繰り返しのうち描画する割合。1 = 実線（Vectorworksでは> 0が必要）。 |
| `offsetVector` | `Point2D` | 線群内のある平行線から次の平行線までの間隔。 |
| `color` | `ColorRGB` | 線の色。 |
| `lineWeightMils` | `int` | ミル単位（1/1000インチ）の線の太さ。 |

### Hatch

> **完全修飾名:** `api.Hatch` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

ベクターハッチングによる面（`ObjectType.HatchDefinition`）：塗りつぶす領域全体で繰り返される線群の集合。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Hatch(h: Handle)` | 既存のハッチング`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> Hatch` *静的* | `name`という名前のハッチングリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> Hatch` *静的* | 内部インデックス`index`を持つハッチングリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str, usePageUnits: bool = False, transparent: bool = True, backgroundColor: ColorRGB = ColorRGB()) -> Hatch` *静的* | 空のハッチングを作成します。`name`がすでに使用されている場合は番号を付加します。 |

*設定*

| メソッド | 説明 |
|---|---|
| `GetUsePageUnits() -> bool \| None` | ハッチングをワールド単位ではなく印刷用紙上で測定する場合は`True`。 |
| `SetUsePageUnits(value: bool) -> bool` | *縮尺無視*（用紙単位を使用）をオンまたはオフにします。ハッチングをワールド単位ではなく印刷用紙上で測定する場合は`True`。 |
| `GetTransparent() -> bool \| None` | ハッチング線の背後の領域を背景色で塗りつぶさず、透明なままにする場合は`True`。 |
| `SetTransparent(value: bool) -> bool` | *透明*をオンまたはオフにします。ハッチング線の背後の領域を背景色で塗りつぶさず、透明なままにする場合は`True`。 |
| `GetRotateInWalls() -> bool \| None` | ハッチングが、描画先の壁／シンボルの回転に追従するかどうか。 |
| `SetRotateInWalls(value: bool) -> bool` | *壁内で回転*をオンまたはオフにします。ハッチングが、描画先の壁／シンボルの回転に追従するかどうかを指定します。 |
| `GetRotateInSymbols() -> bool \| None` | *シンボル内で回転*がオンかどうか。 |
| `SetRotateInSymbols(value: bool) -> bool` | *シンボル内で回転*をオンまたはオフにします。 |

*レベル*

| メソッド | 説明 |
|---|---|
| `GetLevelCount() -> int` | レベル（線群）は0始まりです。一つのハッチングに含められる数に固定の上限はありません。 |
| `GetLevel(index: int) -> HatchLevel \| None` | `index`のレベルを返します。 |
| `GetLevels() -> list[HatchLevel]` | レベルを返します。 |
| `SetLevel(index: int, level: HatchLevel) -> bool` | `index`のレベルを置き換えます。index == `GetLevelCount()`の場合は末尾への追加が可能です。 |
| `AddLevel(level: HatchLevel) -> bool` | レベル`level`を末尾に追加します。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### GradientSegment

> **完全修飾名:** `api.GradientSegment` · **継承元:** `api.Object`

グラデーションの一つの変化点。`spotPosition`は色の位置（グラデーション全体の0 .. 1）、`midpointPosition`は次の変化点との混合が半分になる位置（二つの変化点間の0 .. 1）です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `GradientSegment()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `GradientSegment(spotPosition, midpointPosition, color, opacity)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `spotPosition` | `float` | グラデーション上の変化点の位置（0 .. 1）。 |
| `midpointPosition` | `float` | 次の変化点までの中間点の位置（0 .. 1）。 |
| `color` | `ColorRGB` | 変化点の色。 |
| `opacity` | `int` | 0 = 完全に透明、100 = 不透明。 |

### Gradient

> **完全修飾名:** `api.Gradient` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

グラデーションによる面（`ObjectType.GradientDefinition`）：二つ以上の変化点間の混合。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Gradient(h: Handle)` | 既存のグラデーション`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> Gradient` *静的* | `name`という名前のグラデーションリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> Gradient` *静的* | 内部インデックス`index`を持つグラデーションリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str) -> Gradient` *静的* | デフォルトの二つの変化点を持つグラデーションを作成します。名前がすでに使用されている場合は番号を付加します。 |
| `GetSegmentCount() -> int` | 変化点は0始まりで、位置順に0から`GetSegmentCount()` - 1まで並びます。 |
| `GetSegment(index: int) -> GradientSegment \| None` | `index`のセグメントを返します。 |
| `GetSegments() -> list[GradientSegment]` | セグメントを返します。 |
| `SetSegment(index: int, segment: GradientSegment) -> bool` | 変化点の位置を変更すると並べ替えが発生し、その変化点が別のインデックスになることがあります。 |
| `InsertSegment(segment: GradientSegment) -> int \| None` | 変化点を追加します。グラデーションは変化点を常に並べ替えるため、新しい変化点の0始まりのインデックスを返します。変化点が追加されなかった場合は`None`を返します。 |
| `RemoveSegment(index: int) -> bool` | `index`の変化点を削除します。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### Tile

> **完全修飾名:** `api.Tile` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

タイルによる面（`ObjectType.TileDefinition`）：塗りつぶす領域全体で、グリッドに沿って繰り返される2Dオブジェクトのグループ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Tile(h: Handle)` | 既存のタイル`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> Tile` *静的* | `name`という名前のタイルリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> Tile` *静的* | 内部インデックス`index`を持つタイルリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str) -> Tile` *静的* | 空のタイルを作成します。名前がすでに使用されている場合は番号を付加します。 |

*形状*

| メソッド | 説明 |
|---|---|
| `GetGeometryGroup() -> Handle` | タイルが繰り返す2Dオブジェクトを格納するグループ。AddGeometryで形状を追加します。 |
| `GetGeometry() -> list[Handle]` | 形状を返します。 |
| `AddGeometry(hObject: Handle) -> bool` | 既存の2Dオブジェクトをタイルに移動します。 |

*設定*

| メソッド | 説明 |
|---|---|
| `GetOffset() -> Point2D \| None` | タイルグリッドの原点と、繰り返しから次の繰り返しまでの移動量。 |
| `SetOffset(value: Point2D) -> bool` | オフセットを設定します。タイルグリッドの原点と、繰り返しから次の繰り返しまでの移動量です。 |
| `GetRepetition() -> Point2D \| None` | 繰り返しを返します。 |
| `SetRepetition(value: Point2D) -> bool` | 繰り返しを設定します。 |
| `GetUsePageUnits() -> bool \| None` | タイルをワールド単位ではなく印刷用紙上で測定する場合は`True`。 |
| `SetUsePageUnits(value: bool) -> bool` | *縮尺無視*（用紙単位を使用）をオンまたはオフにします。タイルをワールド単位ではなく印刷用紙上で測定する場合は`True`。 |
| `GetTransparentBackground() -> bool \| None` | *背景を透明にする*がオンかどうか。 |
| `SetTransparentBackground(value: bool) -> bool` | *背景を透明にする*をオンまたはオフにします。 |
| `GetBackgroundColor() -> ColorRGB \| None` | 背景色を返します。 |
| `SetBackgroundColor(color: ColorRGB) -> bool` | 背景色を設定します。 |
| `GetRotateInWalls() -> bool \| None` | *壁内で回転*がオンかどうか。 |
| `SetRotateInWalls(value: bool) -> bool` | *壁内で回転*をオンまたはオフにします。 |
| `GetRotateInSymbols() -> bool \| None` | *シンボル内で回転*がオンかどうか。 |
| `SetRotateInSymbols(value: bool) -> bool` | *シンボル内で回転*をオンまたはオフにします。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### ImageFill

> **完全修飾名:** `api.ImageFill` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

イメージリソース（`ObjectType.ImageDefinition`）：イメージによる面、添景、またはテクスチャ画像として使用するビットマップ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ImageFill(h: Handle)` | 既存のイメージによる面`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> ImageFill` *静的* | `name`という名前のイメージによる面のリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> ImageFill` *静的* | 内部インデックス`index`を持つイメージによる面のリソース。存在しない場合は無効なオブジェクト。 |
| `GetWidthPixels() -> int \| None` | 幅をピクセル単位で返します。 |
| `GetHeightPixels() -> int \| None` | 高さをピクセル単位で返します。 |
| `GetCompression() -> ImageFill.Compression \| None` | 圧縮方式を返します。 |
| `SetCompression(value: ImageFill.Compression) -> bool` | 圧縮方式を設定します。 |
| `CreateFromPngData(pngData: bytes) -> ImageFill` *静的* | PNGファイルの内容（`bytes`）から、イメージによる面のリソースを作成します。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

#### ImageFill.Compression

> **完全修飾名:** `api.ImageFill.Compression` · **種類:** `IntEnum`

画像の保存に使用される圧縮方式。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` |  |
| `Jpeg` | `1` |  |
| `Png` | `2` |  |
| `PngMonochrome` | `3` |  |

### LineType

> **完全修飾名:** `api.LineType` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

ラインタイプリソース。二つの種類があります：

- 単純 — 破線パターン：線と空白の長さを交互に指定します（GetDashPatternを参照）。複雑 - 線に沿って繰り返される2Dオブジェクトのグループです（GetGeometryを参照）。

オブジェクトは線スタイルを通じてラインタイプを参照します。`PenAttributes.SetLineType`を参照してください。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `LineType(h: Handle)` | 既存のラインタイプ`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> LineType` *静的* | `name`という名前のラインタイプリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> LineType` *静的* | 内部インデックス`index`を持つラインタイプリソース。存在しない場合は無効なオブジェクト。 |
| `CreateSimple(dashPattern: list[float], scaleWithLineWeight: bool = False) -> LineType` *静的* | 指定した破線パターンの単一のラインタイプを検索または作成します。線と空白の長さを交互に指定し、最大16項目です。`scaleWithLineWeight`は、オブジェクトの線の太さに合わせてパターンを拡大縮小します。Vectorworksは重複を作成せず、標準リソース内のものを含め、一致する既存のラインタイプを再利用するため、返されるリソースの名前が異なる場合があります。 |
| `CreateComplex(name: str) -> LineType` *静的* | 空の複合のラインタイプを作成します。繰り返す2DオブジェクトをAddGeometryで追加します。 |

*種類*

| メソッド | 説明 |
|---|---|
| `IsSimple() -> bool \| None` | 単一の（破線の）ラインタイプの場合はTrue。 |
| `IsComplex() -> bool \| None` | 複合のラインタイプ（繰り返す形状）の場合はTrue。 |

*単一のラインタイプ*

| メソッド | 説明 |
|---|---|
| `GetDashPattern() -> list[float]` | 交互に並ぶ線と空白の長さ。複合のラインタイプでは空。 |
| `GetScaleWithLineWeight() -> bool \| None` | *線の太さに連動*がオンかどうか。 |

*複合のラインタイプ*

| メソッド | 説明 |
|---|---|
| `GetGeometryGroup() -> Handle` | 線に沿って繰り返される2Dオブジェクトを格納するグループ。単一のラインタイプではヌル。 |
| `GetGeometry() -> list[Handle]` | 形状を返します。 |
| `AddGeometry(hObject: Handle) -> bool` | 既存の2Dオブジェクトをラインタイプに移動します。 |
| `GetGapSize() -> float \| None` | 繰り返される形状同士の間隔。ワールド単位（*縮尺無視*の場合は用紙単位）。 |
| `SetGapSize(value: float) -> bool` | 間隔を設定します。繰り返される形状同士の間隔で、ワールド単位（*縮尺無視*の場合は用紙単位）です。 |
| `GetUsePageUnits() -> bool \| None` | ラインタイプをワールド単位ではなく印刷用紙上で測定する場合は`True`。 |
| `SetUsePageUnits(value: bool) -> bool` | *縮尺無視*（用紙単位を使用）をオンまたはオフにします。ラインタイプをワールド単位ではなく印刷用紙上で測定する場合は`True`。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### RecordField

> **完全修飾名:** `api.RecordField` · **継承元:** `api.Object`

レコードフォーマットの一つのフィールド。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RecordField()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `RecordField(name, localizedName, type, defaultValue)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `name` | `str` | ユニバーサル名（ローカライズされない名前）。APIが使用する名前です。 |
| `localizedName` | `str` | ユーザーインターフェイスに表示される名前。 |
| `type` | `RecordFieldType` | フィールドの型。 |
| `defaultValue` | `str` | 新しいレコードの初期値。文字列で表します。 |

### RecordFormat

> **完全修飾名:** `api.RecordFormat` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

レコードフォーマット。オブジェクトに連結すると、そのオブジェクト上にレコード（これらのフィールドの値の集合）が作成されます。連結されたレコードの値の読み書きについてはDocumentを参照してください。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RecordFormat(h: Handle)` | 既存のレコードフォーマット`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> RecordFormat` *静的* | `name`という名前のレコードフォーマットリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> RecordFormat` *静的* | 内部インデックス`index`を持つレコードフォーマットリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str) -> RecordFormat` *静的* | 空のレコードフォーマットを作成します。名前がすでに使用されている場合は既存のものを返します。 |
| `IsInternalName(name: str) -> bool` *静的* | 内部レコードフォーマット用に予約された名前の場合は`True`。接頭辞が"NNA_"または"__NNA"の名前で、大文字小文字を区別しません。 |
| `GetFieldTypeName(type: RecordFieldType) -> str` *静的* | フィールド型の安定したローワーキャメルケース名（"integer"、"text"、"popUp"など）。 |
| `GetFieldTypeFromName(typeName: str) -> RecordFieldType` *静的* | `typeName`の名前に対応するフィールド型を返します。 |
| `GetAllFieldTypes() -> list[RecordFieldType]` *静的* | すべてのフィールド型を返します。 |

*フォーマット設定*

| メソッド | 説明 |
|---|---|
| `GetLocalizedName() -> str \| None` | ローカライズされた名前を返します。 |
| `SetLocalizedName(name: str) -> bool` | ローカライズされた名前を設定します。 |
| `IsParametric() -> bool \| None` | パラメトリックフォーマットはプラグインオブジェクトに属するため、編集してはいけません。 |
| `GetVisible() -> bool \| None` | 非表示のフォーマットは、オブジェクト情報パレットのデータタブに表示されません。 |
| `SetVisible(value: bool) -> bool` | *表示*をオンまたはオフにします。非表示のフォーマットは、オブジェクト情報パレットのデータタブに表示されません。 |

*フィールド*

| メソッド | 説明 |
|---|---|
| `GetFieldCount() -> int` | フィールド項目の数。 |
| `GetField(index: int) -> RecordField \| None` | `index`のフィールドを返します。 |
| `GetFields() -> list[RecordField]` | フィールドを返します。 |
| `FindField(fieldName: str) -> int` | `fieldName`という名前のフィールドのインデックス。存在しない場合は`kNotFound`。 |
| `HasField(fieldName: str) -> bool` | レコードフォーマットに`fieldName`という名前のフィールドがある場合はTrue。 |
| `AddField(name: str, type: RecordFieldType, defaultValue: str = '', updateExistingRecords: bool = True) -> int` | フィールドを追加します。`defaultValue`は、ユーザーが入力した値と同じ方法で`type`に従って解析されます。空の文字列は、その型の空の値を使用します。文字列型は文字列をそのまま保持し、`RecordFieldType.Boolean`は文字列"True"または"False"、`RecordFieldType.Color`は"red,green,blue"（それぞれ0 .. 65535）を受け取ります。`RecordFieldType.Class`、`BuildingMaterial`、`Texture`、`SymbolDefinition`は、その種類の既存のリソース名を受け取り、`Fill`と`PenStyle`はハッチング、タイル、グラデーション、イメージ、ラインタイプのリソース名を受け取ります。`updateExistingRecords`は、すでにオブジェクトに連結されたレコードにもフィールドを追加し、その値に`defaultValue`を使用します。新しいフィールドのインデックス、または`kNotFound`を返します。後者は、`defaultValue`が`type`に対して無効な場合、その型を追加できない場合（`Radio`、`ControlPoint`、`LayerPopUp`、およびプラグイン専用の型）、またはフィールドが作成されなかった場合です。 |
| `RemoveField(fieldName: str) -> bool` | `fieldName`という名前のフィールドを削除します。 |
| `RenameField(index: int, name: str) -> bool` | `index`のフィールドの名前を`name`に変更します。 |
| `GetFieldDefaultValue(fieldName: str) -> str \| None` | フィールドのデフォルト値。文字列で表します。 |
| `SetFieldDefaultValue(fieldName: str, value: str) -> bool` | フィールドのデフォルト値を設定します。フィールドのデフォルト値を文字列で表します。 |

*ポップアップの選択肢*

| メソッド | 説明 |
|---|---|
| `GetFieldChoices(fieldName: str) -> list[str]` | PopUpフィールドの選択肢。順番に返します。 |
| `SetFieldChoices(fieldName: str, choices: list[str]) -> bool` | PopUpフィールドの選択肢を置き換えます。 |

**定数**

| 定数 | 型 | 値 | 説明 |
|---|---|---|---|
| `RecordFormat.kNotFound` | `int` | `2**64 - 1` | そのユニバーサル名を持つフィールドのインデックス。存在しない場合は`kNotFound`。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### Texture

> **完全修飾名:** `api.Texture` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

テクスチャ（`ObjectType.Texture`）：レンダリングする面の色、反射、透明度、バンプ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Texture(h: Handle)` | 既存のテクスチャ`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> Texture` *静的* | `name`という名前のテクスチャリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> Texture` *静的* | 内部インデックス`index`を持つテクスチャリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str) -> Texture` *静的* | 空のテクスチャを作成します。名前がすでに使用されている場合は番号を付加します。 |
| `GetSize() -> float \| None` | テクスチャ画像が覆う実際の大きさ。ワールド単位。 |
| `SetSize(value: float) -> bool` | サイズを設定します。テクスチャ画像が覆う実際の大きさで、ワールド単位です。 |
| `GetUVAspectRatio() -> float \| None` | テクスチャ画像のU方向とV方向の範囲の比。 |
| `ApplyToObject(hObject: Handle, part: Texture.Part = Texture.Part.Overall) -> bool` | オブジェクト（またはその一部分）にテクスチャを割り当てます。 |
| `UpdateThumbnail() -> bool` | テクスチャの変更後にリソースマネージャのプレビューを更新します。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

#### Texture.Part

> **完全修飾名:** `api.Texture.Part` · **種類:** `IntEnum`

テクスチャを適用するオブジェクトの部分。部分を持たないオブジェクトはOverallを使用します。

| メンバー | 値 | 説明 |
|---|---|---|
| `Overall` | `0` | オブジェクト全体。 |
| `ExtrudeTop` | `1` |  |
| `ExtrudeBottom` | `2` |  |
| `ExtrudeSides` | `3` | 押し出しと回転体。 |
| `WallLeft` | `4` |  |
| `WallRight` | `5` |  |
| `WallTop` | `6` |  |
| `WallBottom` | `7` | 壁。 |
| `SlabTop` | `8` |  |
| `SlabBottom` | `9` |  |
| `SlabSides` | `10` | スラブ。 |
| `RoofTop` | `11` |  |
| `RoofBottom` | `12` |  |
| `RoofSides` | `13` | 屋根。 |

### RenderStyle

> **完全修飾名:** `api.RenderStyle` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

レンダリングスタイル（`ObjectType.RenderStyle`）：ビューポートまたはレイヤに適用する、保存されたレンダリング設定。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RenderStyle(h: Handle)` | 既存のレンダリングスタイル`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> RenderStyle` *静的* | `name`という名前のレンダリングスタイルリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> RenderStyle` *静的* | 内部インデックス`index`を持つレンダリングスタイルリソース。存在しない場合は無効なオブジェクト。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### RenderBackground

> **完全修飾名:** `api.RenderBackground` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

背景テクスチャ（`ObjectType.RenderBackground`）：レンダリング時にモデルの背後に表示するもの。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RenderBackground(h: Handle)` | 既存の背景テクスチャ`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> RenderBackground` *静的* | `name`という名前の背景テクスチャリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> RenderBackground` *静的* | 内部インデックス`index`を持つ背景テクスチャリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str, kind: RenderBackground.Kind) -> RenderBackground` *静的* | その種類の背景を作成します。名前がすでに使用されている場合は番号を付加します。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

#### RenderBackground.Kind

> **完全修飾名:** `api.RenderBackground.Kind` · **種類:** `IntEnum`

新しいリソースを作成するときの背景の種類。

| メンバー | 値 | 説明 |
|---|---|---|
| `Clouds` | `0` |  |
| `OneColor` | `1` |  |
| `TwoColor` | `2` |  |
| `PhysicalSky` | `3` |  |

### TextStyle

> **完全修飾名:** `api.TextStyle` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

文字スタイル（`ObjectType.TextStyle`）：文字列オブジェクトと寸法に適用するフォント、サイズ、文字属性。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `TextStyle(h: Handle)` | 既存の文字スタイル`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> TextStyle` *静的* | `name`という名前の文字スタイルリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> TextStyle` *静的* | 内部インデックス`index`を持つ文字スタイルリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str) -> TextStyle` *静的* | 文字スタイルを作成します。名前がすでに使用されている場合は既存のものを返します。 |
| `ApplyToObject(hObject: Handle) -> bool` | 文字列オブジェクト（または文字属性を持つ任意のオブジェクト）にスタイルを適用します。 |
| `OfObject(hObject: Handle) -> TextStyle` *静的* | オブジェクトが従う文字スタイル。オブジェクトが独自の文字属性を使用している場合は無効。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### WallStyle

> **完全修飾名:** `api.WallStyle` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

壁スタイル（`ObjectType.WallStyle`）：壁の構成要素、厚さ、属性。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `WallStyle(h: Handle)` | 既存の壁スタイル`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> WallStyle` *静的* | `name`という名前の壁スタイルリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> WallStyle` *静的* | 内部インデックス`index`を持つ壁スタイルリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str) -> WallStyle` *静的* | 壁スタイルを作成します。名前がすでに使用されている場合は既存のものを返します。 |
| `ApplyToObject(hWall: Handle, selectedOffset: float = 0.0, replacingOffset: float = 0.0) -> bool` | 壁にスタイルを適用します。二つのオフセットは、元の壁のどの線と新しいスタイルのどの線の位置を維持するかを、壁の中心からワールド単位で指定します。0は中心線を維持します。 |
| `OfObject(hWall: Handle) -> WallStyle` *静的* | 壁`hWall`が従う壁スタイル（ない場合は無効）。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### SlabStyle

> **完全修飾名:** `api.SlabStyle` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

スラブスタイル（`ObjectType.SlabStyle`）：スラブの構成要素と属性。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `SlabStyle(h: Handle)` | 既存のスラブスタイル`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> SlabStyle` *静的* | `name`という名前のスラブスタイルリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> SlabStyle` *静的* | 内部インデックス`index`を持つスラブスタイルリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str) -> SlabStyle` *静的* | スラブスタイルを作成します。名前がすでに使用されている場合は既存のものを返します。 |
| `ApplyToObject(hSlab: Handle) -> bool` | このスラブスタイルをスラブ`hSlab`に適用します。 |
| `OfObject(hSlab: Handle) -> SlabStyle` *静的* | スラブ`hSlab`が従うスラブスタイル（ない場合は無効）。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### RoofStyle

> **完全修飾名:** `api.RoofStyle` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

屋根スタイル（`ObjectType.RoofStyle`）：屋根の構成要素と属性。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `RoofStyle(h: Handle)` | 既存の屋根スタイル`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> RoofStyle` *静的* | `name`という名前の屋根スタイルリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> RoofStyle` *静的* | 内部インデックス`index`を持つ屋根スタイルリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str) -> RoofStyle` *静的* | 屋根スタイルを作成します。名前がすでに使用されている場合は既存のものを返します。 |
| `ApplyToObject(hRoof: Handle) -> bool` | この屋根スタイルを屋根`hRoof`に適用します。 |
| `OfObject(hRoof: Handle) -> RoofStyle` *静的* | 屋根`hRoof`が従う屋根スタイル（ない場合は無効）。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### ViewportStyle

> **完全修飾名:** `api.ViewportStyle` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

ビューポートスタイル（`ObjectType.ViewportStyle`）：シートレイヤビューポートの保存された設定。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ViewportStyle(h: Handle)` | 既存のビューポートスタイル`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> ViewportStyle` *静的* | `name`という名前のビューポートスタイルリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> ViewportStyle` *静的* | 内部インデックス`index`を持つビューポートスタイルリソース。存在しない場合は無効なオブジェクト。 |
| `ApplyToObject(hViewport: Handle) -> bool` | このビューポートスタイルをビューポート`hViewport`に適用します。 |
| `OfObject(hViewport: Handle) -> ViewportStyle` *静的* | ビューポート`hViewport`が従うビューポートスタイル（ない場合は無効）。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### BuildingMaterial

> **完全修飾名:** `api.BuildingMaterial` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

マテリアル（建材、`ObjectType.BuildingMaterial`）：壁、スラブ、屋根の構成要素の物理的な材料。その材料の属性とデータ（耐火性能、熱特性など）を保持します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `BuildingMaterial(h: Handle)` | 既存のマテリアル`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> BuildingMaterial` *静的* | `name`という名前のマテリアルリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> BuildingMaterial` *静的* | 内部インデックス`index`を持つマテリアルリソース。存在しない場合は無効なオブジェクト。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### DataVisualization

> **完全修飾名:** `api.DataVisualization` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

データの可視化（`ObjectType.DataVisualization`）：検索条件に一致するオブジェクトのグラフィック属性を上書きするルールで、ビューポートまたはデザインレイヤに適用します。Vectorworksはデータの可視化を名前で識別するため、このクラスは名前を使用して操作します。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `DataVisualization(h: Handle)` | 既存のデータの可視化`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> DataVisualization` *静的* | `name`という名前のデータの可視化リソース。存在しない場合は無効なオブジェクト。 |
| `GetAllNames() -> list[str]` *静的* | 現在のファイルのすべてのデータの可視化の名前。 |
| `Rename(oldName: str, newName: str) -> bool` *静的* | データの可視化の名前を`oldName`から`newName`に変更します。 |
| `DeleteByName(name: str) -> bool` *静的* | `name`という名前のデータの可視化を削除します。 |
| `GetActiveOn(hObject: Handle) -> list[str]` *静的* | オブジェクト（ビューポート、登録ビュー、レイヤ）で有効なデータの可視化の名前。 |
| `Activate(hObject: Handle, name: str, activate: bool) -> bool` *静的* | そのオブジェクトのデータの可視化をオンまたはオフにします。 |
| `SetObjectExcluded(hObject: Handle, exclude: bool) -> bool` *静的* | オブジェクトをすべてのデータの可視化の対象から除外します。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### ResourceFolderPath

> **完全修飾名:** `api.ResourceFolderPath` · **継承元:** `api.Object`

`ResourceFolder.CreatePathFolders`が作成したパスのフォルダ。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ResourceFolderPath()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `ResourceFolderPath(folders, createdFolders)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `folders` | `list[Handle]` | パス内のすべてのフォルダを外側から順に返します。失敗した場合は空。 |
| `createdFolders` | `list[Handle]` | この呼び出しが作成したフォルダ。外側から順。 |

### ResourceFolder

> **完全修飾名:** `api.ResourceFolder` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

リソースフォルダ（`ObjectType.Folder`）：リソースマネージャで一種類のリソースをまとめます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `ResourceFolder(h: Handle)` | 既存のリソースフォルダ`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> ResourceFolder` *静的* | `name`という名前のリソースフォルダリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str, forType: ResourceType) -> ResourceFolder` *静的* | その種類のリソース用に最上位フォルダを作成します。名前がすでに使用されている場合は失敗します（無効なフォルダ）。リソース名はファイル内で一意です。取り消し用の登録は行われないため、新しいフォルダを`Document.AddAfterSwapObject`で登録してください。 |
| `CreatePath(folderPath: str, forType: ResourceType) -> ResourceFolder` *静的* | "Doors/Interior"などのパスから、一連の入れ子のフォルダを作成し、最も内側のフォルダを返します。規則についてはCreatePathFoldersを参照してください。 |
| `CreatePathFolders(folderPath: str, forType: ResourceType) -> ResourceFolderPath` *静的* | "Doors/Interior"などのパスから、一連の入れ子のフォルダを作成し、そのすべてを返します。パス内のフォルダが、`forType`用としてその位置にすでに存在する場合は再利用します。パス内の名前が、それ以外のもの（別の場所や別の種類のフォルダを含む）に使用されている場合は失敗し（空の結果）、それまでに作成したフォルダも削除します。空の名前（"A//B"、先頭または末尾の'/'）はスキップします。取り消し用の登録は行われません。`createdFolders`の最初のフォルダ（最も外側の新しいフォルダ）のみを`Document.AddAfterSwapObject`で登録してください。そのフォルダは他の新しいフォルダを含み、フォルダを登録するとその内容も挿入済みとしてマークされるため、さらに内側の新しいフォルダも登録すると、二重に挿入されてしまいます。再利用したフォルダは決して登録しないでください。 |
| `GetContentType() -> ResourceType \| None` | フォルダに格納するリソースの種類。 |
| `GetResources() -> list[Handle]` | フォルダ内のリソース。 |
| `Add(hResource: Handle) -> bool` | リソースをこのフォルダに移動します。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

### SymbolDefinition

> **完全修飾名:** `api.SymbolDefinition` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

シンボル定義。その内容はシンボルが描画するオブジェクトです。図面内のすべてのインスタンスは同じ内容を表示するため、内容を編集するとすべてのインスタンスが一度に更新されます。植栽スタイル、図面枠スタイル、その他のプラグインスタイルもシンボル定義です。その唯一の内容として一つのプラグインオブジェクトを格納します（`PlantObject.EnsurePlantStyle`を参照）。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `SymbolDefinition(h: Handle)` | 既存のシンボル定義`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> SymbolDefinition` *静的* | `name`という名前のシンボル定義リソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> SymbolDefinition` *静的* | 内部インデックス`index`を持つシンボル定義リソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str) -> SymbolDefinition` *静的* | 空のシンボル定義を作成します。名前がすでに使用されている場合は番号が付加されるため、`GetName()`で名前を読み直してください。 |
| `GetActive() -> SymbolDefinition` *静的* | 新しいシンボルインスタンスの作成元となるシンボル定義。 |
| `SetActive() -> bool` | アクティブなものを設定します。新しいシンボルインスタンスの作成元となるシンボル定義です。 |

*種類*

| メソッド | 説明 |
|---|---|
| `GetGeometryType() -> SymbolDefinition.GeometryType \| None` | 形状の種類を返します。 |
| `CanInsertIntoWalls() -> bool \| None` | シンボルを壁に挿入できる場合（壁挿入点を持つ場合）は`True`。 |
| `ContainsLight() -> bool \| None` | シンボル定義が光源を含む場合はTrue。 |

*挿入時の動作*

| メソッド | 説明 |
|---|---|
| `GetInsertMode() -> SymbolDefinition.InsertMode \| None` | 挿入モードを返します。 |
| `SetInsertMode(value: SymbolDefinition.InsertMode) -> bool` | 挿入モードを設定します。 |
| `GetBreakMode() -> SymbolDefinition.BreakMode \| None` | 切り欠きモードを返します。 |
| `SetBreakMode(value: SymbolDefinition.BreakMode) -> bool` | 切り欠きモードを設定します。 |
| `GetPageBased() -> bool \| None` | 実寸表示優先-縮尺無視（ページ単位）のシンボルは、ワールド単位ではなく印刷用紙上のサイズを維持します。 |
| `SetPageBased(value: bool) -> bool` | *実寸表示優先-縮尺無視*をオンまたはオフにします。この設定のシンボルは、ワールド単位ではなく印刷用紙上のサイズを維持します。 |
| `GetInsertAsGroup() -> bool \| None` | シンボルの挿入時に、シンボルインスタンスの代わりにその内容のコピーを配置する場合は`True`。 |
| `SetInsertAsGroup(value: bool) -> bool` | *グループ図形に変換*をオンまたはオフにします。シンボルの挿入時に、シンボルインスタンスの代わりにその内容のコピーを配置する場合は`True`。 |

*内容*

| メソッド | 説明 |
|---|---|
| `GetGeometry() -> list[Handle]` | シンボルが描画するオブジェクト（`Resource.GetContents`と同じ）。 |
| `AddGeometry(hObject: Handle) -> bool` | 既存のオブジェクトをシンボル定義に移動します。 |
| `ResetInstances() -> bool` | 内容の変更後にすべてのインスタンスを再描画します。 |

*インスタンス*

| メソッド | 説明 |
|---|---|
| `Insert(position: Point2D, rotationRadians: float = 0.0) -> Handle` | アクティブレイヤ／現在のコンテナの`position`にシンボルインスタンスを作成します。失敗した場合はヌル。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

#### SymbolDefinition.GeometryType

> **完全修飾名:** `api.SymbolDefinition.GeometryType` · **種類:** `IntEnum`

シンボルが描画できるもの：2Dのみ、3Dのみ、または両方（ハイブリッドシンボルは平面ビューで2D部分を表示します）。

| メンバー | 値 | 説明 |
|---|---|---|
| `Unknown` | `0` |  |
| `TwoD` | `1` |  |
| `ThreeD` | `2` |  |
| `Hybrid` | `3` |  |

#### SymbolDefinition.InsertMode

> **完全修飾名:** `api.SymbolDefinition.InsertMode` · **種類:** `IntEnum`

シンボルを挿入する壁に対する、シンボルの配置位置。

| メンバー | 値 | 説明 |
|---|---|---|
| `Edge` | `0` |  |
| `Center` | `1` |  |
| `LeftEdge` | `2` |  |
| `RightEdge` | `3` |  |
| `CoreComponentCenter` | `4` |  |
| `CoreComponentLeftEdge` | `5` |  |
| `CoreComponentRightEdge` | `6` |  |
| `WallInsertLocation` | `7` |  |
| `WallClosureInsertLocation` | `8` |  |

#### SymbolDefinition.BreakMode

> **完全修飾名:** `api.SymbolDefinition.BreakMode` · **種類:** `IntEnum`

シンボルの挿入箇所で壁を切り欠く方法。

| メンバー | 値 | 説明 |
|---|---|---|
| `FullWithCaps` | `0` |  |
| `FullNoCaps` | `1` |  |
| `Half` | `2` |  |
| `None_` | `3` |  |

### WorksheetCell

> **完全修飾名:** `api.WorksheetCell` · **継承元:** `api.Object`

ワークシートのセル。行と列は、ユーザーに表示される行番号と列の文字と同様に1始まりです。列1は"A"です。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `WorksheetCell()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `WorksheetCell(row, column)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `row` | `int` | 行（1始まり）。 |
| `column` | `int` | 列（1始まり）。 |

### WorksheetCellContent

> **完全修飾名:** `api.WorksheetCellContent` · **継承元:** `api.Object`

内容を持つ一つのセル。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `WorksheetCellContent()` | デフォルト値（各フィールドはデフォルトの値）。 |
| `WorksheetCellContent(cell, formula, text)` | フィールド値：すべてのフィールドを（この順序で）位置引数として指定するか、任意のフィールドをキーワード引数として指定します。 |

**フィールド**

| フィールド | 型 | 説明 |
|---|---|---|
| `cell` | `WorksheetCell` | セル。 |
| `formula` | `str` | セルに設定された内容。リテラルを保持するセルでは空。 |
| `text` | `str` | 最後の再計算後にセルが表示する内容。 |

### Worksheet

> **完全修飾名:** `api.Worksheet` · **継承元:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

ワークシート。ワークシートはリソースであり、ワークシートイメージとしてレイヤ上に配置することもできます。

**コンストラクタ**

| コンストラクタ | 説明 |
|---|---|
| `Worksheet(h: Handle)` | 既存のワークシート`h`を参照します。使用前に`IsValid()`を確認してください。 |

**メソッド**

*一般*

| メソッド | 説明 |
|---|---|
| `Is(h: Handle) -> bool` *静的* | `h`がこのクラスの表す種類のオブジェクトを参照している場合はTrue。 |
| `FromName(name: str) -> Worksheet` *静的* | `name`という名前のワークシートリソース。存在しない場合は無効なオブジェクト。 |
| `FromIndex(index: int) -> Worksheet` *静的* | 内部インデックス`index`を持つワークシートリソース。存在しない場合は無効なオブジェクト。 |
| `Create(name: str, rows: int = 20, columns: int = 10) -> Worksheet` *静的* | 空のワークシートを作成します。名前がすでに使用されている場合は既存のものを返します。 |

*サイズ*

| メソッド | 説明 |
|---|---|
| `GetRowCount() -> int \| None` | 行項目の数。 |
| `GetColumnCount() -> int \| None` | 列項目の数。 |
| `IsValidCell(cell: WorksheetCell) -> bool` | セル`cell`がワークシートに存在する場合はTrue。 |

*セル*

| メソッド | 説明 |
|---|---|
| `GetCellFormula(cell: WorksheetCell) -> str \| None` | セルの数式。リテラル値を保持するセルでは空の文字列を返します。 |
| `SetCellFormula(cell: WorksheetCell, formula: str) -> bool` | 一つのセル、または範囲内のすべてのセルに、数式（例："=COUNT(ALL)"）またはリテラルを割り当てます。 |
| `SetRangeFormula(topLeft: WorksheetCell, bottomRight: WorksheetCell, formula: str) -> bool` | 範囲の数式を設定します。 |
| `GetCellText(cell: WorksheetCell) -> str \| None` | セルに現在表示されている文字列。図面が変更された場合は、先にRecalculateを呼び出してください。 |
| `GetCellValue(cell: WorksheetCell) -> float \| None` | セルの数値。セルが数値を保持していない場合は空。 |
| `GetCells(topLeft: WorksheetCell, bottomRight: WorksheetCell) -> list[WorksheetCellContent]` | 長方形のセル範囲を行ごとに読み取ります。数式も文字列もないセルはスキップします。 |
| `ClearCells(topLeft: WorksheetCell, bottomRight: WorksheetCell) -> bool` | `topLeft`から`bottomRight`までの範囲のセルを消去します。 |

*構造*

| メソッド | 説明 |
|---|---|
| `InsertRows(beforeRow: int, count: int = 1) -> bool` | `count`行を、行`beforeRow`の前に挿入します。 |
| `InsertColumns(beforeColumn: int, count: int = 1) -> bool` | `count`列を、列`beforeColumn`の前に挿入します。 |
| `DeleteRows(startRow: int, count: int = 1) -> bool` | `count`行を、行`startRow`から削除します。 |
| `DeleteColumns(startColumn: int, count: int = 1) -> bool` | `count`列を、列`startColumn`から削除します。 |
| `Recalculate() -> bool` | すべての数式を再評価します。図面の変更後、セルの文字列を読み取る前に実行してください。 |
| `CreateImage(topLeftCorner: Point2D) -> Handle` | 図面内で表示できるよう、ワークシートをアクティブレイヤに配置します。イメージオブジェクトを返します。 |

継承：[`TypedResource`](#typedresource)、[`Resource`](#resource)のすべて。

<a id="enumerations"></a>

## 列挙型

### ResourceType

> **完全修飾名:** `api.ResourceType` · **種類:** `IntEnum`

リソースの種類。値はオブジェクトタイプ（対応するObjectType定数と同じ値）なので、オブジェクトタイプを受け取る任意のAPIにリソースタイプを渡せます。

| メンバー | 値 | 説明 |
|---|---|---|
| `Unknown` | `0` | このオブジェクトはリソースではありません。 |
| `SymbolDefinition` | `16` | 再利用可能なオブジェクトテンプレート。図面にはシンボルインスタンスとして配置されます。 |
| `Worksheet` | `18` | 表計算／レポート。 |
| `BuildingMaterial` | `19` | 壁、スラブ、屋根の構成要素のマテリアル。 |
| `ViewportStyle` | `36` |  |
| `DataVisualization` | `37` | ルールに基づくビューポート／レイヤのグラフィック属性の上書き。 |
| `RecordFormat` | `47` | データレコード定義（オブジェクトに連結するフォーマット）。 |
| `Hatch` | `66` | ベクターハッチングによる面。 |
| `Folder` | `92` | リソースマネージャで他のリソースをまとめるリソースフォルダ。 |
| `Class` | `94` | クラス定義（属性についてはClassAttributesを参照）。 |
| `LineType` | `96` | 単一または複合のラインタイプ（破線／パターン付きの線）。 |
| `Texture` | `97` | テクスチャ。 |
| `RoofStyle` | `102` |  |
| `RenderStyle` | `106` | レンダリングスタイル。 |
| `SlabStyle` | `107` |  |
| `Tile` | `108` | タイルによる面。 |
| `TextStyle` | `109` |  |
| `RenderBackground` | `115` | 背景テクスチャ。 |
| `ImageFill` | `119` | イメージによる面／添景として使用するイメージ定義。 |
| `Gradient` | `120` | グラデーションによる面。 |
| `WallStyle` | `127` |  |

### ContentFolder

> **完全修飾名:** `api.ContentFolder` · **種類:** `IntEnum`

外部（ライブラリ／デフォルト）リソースを格納するVectorworksの標準コンテンツフォルダ。値はVectorworksのフォルダ指定子です。その他の指定子はBuildFromFolderIndexに渡します。

| メンバー | 値 | 説明 |
|---|---|---|
| `None_` | `0` | ライブラリフォルダなし：現在の図面のみ。 |
| `ObjectLibraries` | `11` |  |
| `Libraries` | `13` |  |
| `Defaults` | `14` |  |
| `Textures` | `100` |  |
| `Gradients` | `103` |  |
| `Hatches` | `105` |  |
| `ImageFills` | `106` |  |
| `PlantStyles` | `107` |  |
| `RenderBackgrounds` | `109` |  |
| `TitleBlocks` | `115` |  |
| `Reports` | `120` |  |
| `SketchStyles` | `134` |  |
| `Tiles` | `163` |  |
| `TextStyles` | `164` |  |
| `RenderStyles` | `171` |  |
| `LineTypes` | `174` |  |
| `RecordFormats` | `197` |  |
| `ObjectStyles` | `217` |  |
| `Materials` | `345` |  |
| `WallStyles` | `393` |  |
| `RoofStyles` | `394` |  |
| `SlabStyles` | `395` |  |
| `PlantLibraries` | `399` |  |

### ImportConflict

> **完全修飾名:** `api.ImportConflict` · **種類:** `IntEnum`

現在の図面にリソースを取り込む際、同名のリソースがすでに存在する場合の名前の競合の解決方法。

| メンバー | 値 | 説明 |
|---|---|---|
| `DoNotImport` | `0` | 既存のリソースを維持し、何も取り込みません。 |
| `Replace` | `1` | 既存のリソースを上書きします。 |
| `Rename` | `2` | 新しい一意の名前で取り込みます。 |
| `AskWithUI` | `3` | Vectorworks標準の競合ダイアログを表示します（対話型セッションのみ）。 |

### RecordFieldType

> **完全修飾名:** `api.RecordFieldType` · **種類:** `IntEnum`

レコードフィールドのデータ型。

| メンバー | 値 | 説明 |
|---|---|---|
| `Unknown` | `0` |  |
| `Integer` | `1` |  |
| `Boolean` | `2` |  |
| `Real` | `3` |  |
| `Text` | `4` |  |
| `Dimension` | `7` | ファイルの単位で表示される長さ。 |
| `PopUp` | `8` | 定義済みの選択肢のリストを持つ文字列。 |
| `Radio` | `9` |  |
| `CoordLocX` | `10` | プラグインパラメータ専用。 |
| `CoordLocY` | `11` | プラグインパラメータ専用。 |
| `StaticText` | `14` | ラベル。オブジェクト上では編集できません。 |
| `ControlPoint` | `15` |  |
| `DimStdPopUp` | `16` | プラグインパラメータ専用。 |
| `PrecisionPopUp` | `17` | プラグインパラメータ専用。 |
| `ClassPopUp` | `18` |  |
| `LayerPopUp` | `19` |  |
| `Angle` | `20` |  |
| `Area` | `21` |  |
| `Volume` | `22` |  |
| `Class` | `23` | クラスの内部インデックス。 |
| `BuildingMaterial` | `24` | マテリアルの内部インデックス。 |
| `Fill` | `25` |  |
| `PenStyle` | `26` |  |
| `PenWeight` | `27` |  |
| `Color` | `28` |  |
| `Texture` | `29` | テクスチャの内部インデックス。 |
| `SymbolDefinition` | `30` | シンボル定義の内部インデックス。 |

---

[一覧に戻る](README.md) · [先頭に戻る](#resources--resources-resource-lists-and-typed-resources)
