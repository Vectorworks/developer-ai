[English](../../PythonAPI/v2027.2/Resources.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/Resources.md)

# Resources — Zubehör, Zubehörlisten und typisiertes Zubehör

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Zubehörklassen (die Funktionen des Zubehör-Managers in der API). `Resource` steht für ein Zubehör beliebigen Typs (Name, Beschreibung, Ordner, Inhalt, Lebensdauer). `ResourceList` listet Zubehör eines Typs aus der aktuellen Zeichnung oder aus externen Inhalten (Vectorworks-Bibliotheken, einer Datei, einem anderen geöffneten Dokument) auf und importiert es in die Zeichnung. `TypedResource` ist die Basisklasse der typisierten Zubehörklassen; ein typisiertes Zubehörobjekt ist ungültig, wenn sein Handle nicht tatsächlich auf Zubehör seines Typs verweist, sodass es niemals auf das falsche Zubehör einwirken kann.

Die typisierten Klassen ergänzen die Funktionen, die nur ihr jeweiliger Typ besitzt: Schraffuren, Farbverläufe, Mosaike und Bildfüllungen; Linienarten; Symboldefinitionen; Texturen, Renderstile und Hintergründe; Datenbanken; Tabellen; Text-, Wand-, Boden/Decken-, Dach- und Ansichtsbereichstile; Materialien; Datenvisualisierungen und Zubehörordner. Klassen sind ebenfalls Zubehör, werden aber von [`ClassAttributes`](Attributes.md#classattributes) abgedeckt.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
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
- [Aufzählungen](#aufzählungen)
  - [ResourceType](#resourcetype)
  - [ContentFolder](#contentfolder)
  - [ImportConflict](#importconflict)
  - [RecordFieldType](#recordfieldtype)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`Resource`](#resource) | Klasse |  | Ein Zubehör, identifiziert durch sein Handle. |
| [`ResourceList`](#resourcelist) | Klasse |  | Eine Liste von Zubehör eines Typs aus der aktuellen Zeichnung oder aus externen Inhalten. |
| [`ResourceList.Entry`](#resourcelistentry) | Klasse (verschachtelt) |  | Ein Eintrag der Liste. |
| [`ResourceList.ImportResult`](#resourcelistimportresult) | Klasse (verschachtelt) |  | Ergebnis von ImportWithResult: das Zubehör in der Zeichnung und ob dieser Aufruf es hineinkopiert hat (`False`, wenn das bereits in der Zeichnung vorhandene Zubehör zurückgegeben wird). |
| [`TypedResource`](#typedresource) | Klasse | [`Resource`](#resource) | Auf einen ResourceType beschränktes Zubehör. |
| [`HatchLevel`](#hatchlevel) | Klasse |  | Eine Linienfamilie einer Schraffur. |
| [`Hatch`](#hatch) | Klasse | [`TypedResource`](#typedresource) | Vektorschraffurfüllung (`ObjectType.HatchDefinition`): eine Menge von Linienfamilien, die sich über die gefüllte Fläche wiederholen. |
| [`GradientSegment`](#gradientsegment) | Klasse |  | Ein Farbstopp eines Farbverlaufs. |
| [`Gradient`](#gradient) | Klasse | [`TypedResource`](#typedresource) | Verlaufsfüllung (`ObjectType.GradientDefinition`): ein Übergang zwischen zwei oder mehr Farbpunkten. |
| [`Tile`](#tile) | Klasse | [`TypedResource`](#typedresource) | Mosaikfüllung (`ObjectType.TileDefinition`): eine Gruppe von 2D-Objekten, die sich auf einem Raster über die gefüllte Fläche wiederholt. |
| [`ImageFill`](#imagefill) | Klasse | [`TypedResource`](#typedresource) | Bildzubehör (`ObjectType.ImageDefinition`): eine Bitmap, die als Bildfüllung, Bildobjekt oder Texturbild verwendet wird. |
| [`ImageFill.Compression`](#imagefillcompression) | IntEnum (verschachtelt) |  | Komprimierung, mit der das Bild gespeichert wird. |
| [`LineType`](#linetype) | Klasse | [`TypedResource`](#typedresource) | Linienart-Zubehör. |
| [`RecordField`](#recordfield) | Klasse |  | Ein Feld einer Datenbank. |
| [`RecordFormat`](#recordformat) | Klasse | [`TypedResource`](#typedresource) | Datenbank. |
| [`Texture`](#texture) | Klasse | [`TypedResource`](#typedresource) | Textur (`ObjectType.Texture`): Farbe, Reflexion, Transparenz und Relief einer gerenderten Oberfläche. |
| [`Texture.Part`](#texturepart) | IntEnum (verschachtelt) |  | Teil eines Objekts, auf den eine Textur angewendet wird. |
| [`RenderStyle`](#renderstyle) | Klasse | [`TypedResource`](#typedresource) | Renderstil (`ObjectType.RenderStyle`): eine gespeicherte Konfiguration der Rendereinstellungen, die auf einen Ansichtsbereich oder eine Ebene angewendet wird. |
| [`RenderBackground`](#renderbackground) | Klasse | [`TypedResource`](#typedresource) | Renderworks-Hintergrund (`ObjectType.RenderBackground`): die Darstellung hinter dem Modell beim Rendern. |
| [`RenderBackground.Kind`](#renderbackgroundkind) | IntEnum (verschachtelt) |  | Art des Hintergrunds, mit dem neues Zubehör erzeugt wird. |
| [`TextStyle`](#textstyle) | Klasse | [`TypedResource`](#typedresource) | Textstil (`ObjectType.TextStyle`): Schriftart, Größe und Textattribute für Textobjekte und Bemaßungen. |
| [`WallStyle`](#wallstyle) | Klasse | [`TypedResource`](#typedresource) | Wandstil (`ObjectType.WallStyle`): Schalen, Dicke und Attribute einer Wand. |
| [`SlabStyle`](#slabstyle) | Klasse | [`TypedResource`](#typedresource) | Boden/Deckenstil (`ObjectType.SlabStyle`): Schalen und Attribute eines Bodens bzw. einer Decke. |
| [`RoofStyle`](#roofstyle) | Klasse | [`TypedResource`](#typedresource) | Dachstil (`ObjectType.RoofStyle`): Schalen und Attribute eines Dachs. |
| [`ViewportStyle`](#viewportstyle) | Klasse | [`TypedResource`](#typedresource) | Ansichtsbereichstil (`ObjectType.ViewportStyle`): die gespeicherten Einstellungen eines Ansichtsbereichs auf einer Layoutebene. |
| [`BuildingMaterial`](#buildingmaterial) | Klasse | [`TypedResource`](#typedresource) | Material (Baumaterial, `ObjectType.BuildingMaterial`): das physische Material einer Wand-, Boden/Decken- oder Dachschicht. |
| [`DataVisualization`](#datavisualization) | Klasse | [`TypedResource`](#typedresource) | Datenvisualisierung (`ObjectType.DataVisualization`): eine Regel, die die grafischen Attribute von Objekten überschreibt, die einem Kriterium entsprechen, angewendet auf einen Ansichtsbereich oder ... |
| [`ResourceFolderPath`](#resourcefolderpath) | Klasse |  | Ordner eines mit `ResourceFolder.CreatePathFolders` erzeugten Pfads: alle Ordner des Pfads und diejenigen, die der Aufruf angelegt hat, jeweils mit dem äußersten beginnend. |
| [`ResourceFolder`](#resourcefolder) | Klasse | [`TypedResource`](#typedresource) | Zubehörordner (`ObjectType.Folder`): gruppiert Zubehör desselben Typs im Zubehör-Manager. |
| [`SymbolDefinition`](#symboldefinition) | Klasse | [`TypedResource`](#typedresource) | Symboldefinition. |
| [`SymbolDefinition.GeometryType`](#symboldefinitiongeometrytype) | IntEnum (verschachtelt) |  | Was das Symbol darstellen kann: nur 2D, nur 3D oder beides (ein hybrides Symbol zeigt seinen 2D-Teil in der Planansicht). |
| [`SymbolDefinition.InsertMode`](#symboldefinitioninsertmode) | IntEnum (verschachtelt) |  | Position des Symbols relativ zur Wand, in die es eingesetzt wird. |
| [`SymbolDefinition.BreakMode`](#symboldefinitionbreakmode) | IntEnum (verschachtelt) |  | Wie die Wand an der Einfügestelle des Symbols ausgeschnitten wird. |
| [`WorksheetCell`](#worksheetcell) | Klasse |  | Eine Tabellenzelle. |
| [`WorksheetCellContent`](#worksheetcellcontent) | Klasse |  | Eine Zelle mit ihrem Inhalt. |
| [`Worksheet`](#worksheet) | Klasse | [`TypedResource`](#typedresource) | Tabelle. |
| [`ResourceType`](#resourcetype) | IntEnum |  | Typ eines Zubehörs. |
| [`ContentFolder`](#contentfolder) | IntEnum |  | Standard-Inhaltsordner von Vectorworks für externes Zubehör (Bibliothek / Vorgaben). |
| [`ImportConflict`](#importconflict) | IntEnum |  | Wie ein Namenskonflikt gelöst wird, wenn Zubehör in die aktuelle Zeichnung importiert wird und dort bereits gleichnamiges Zubehör vorhanden ist. |
| [`RecordFieldType`](#recordfieldtype) | IntEnum |  | Datentyp eines Datenbankfelds. |

## Klassen

### Resource

> **Vollständiger Name:** `api.Resource` · **Erbt von:** `api.Object`

Ein Zubehör, identifiziert durch sein Handle. Wie jede Objektklasse dieser API ist es eine schlanke Sicht: Sein Kopieren kopiert nicht das Zubehör, und das Löschen des Python-Objekts löscht nicht das Zubehör. Wird es aus einem Handle erzeugt, das nicht auf Zubehör verweist, entsteht ein ungültiges Objekt (`IsValid()` == `False`); Abfragemethoden geben dann `None` und Setzmethoden / Operationen `False` zurück. Zeichenfolgen sind UTF-8-kodiert.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Resource(hResource: Handle)` | Verweist auf das vorhandene Zubehör `hResource`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

*Typ*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | `True`, wenn das Handle Zubehör eines der Typen von ResourceType ist. |
| `TypeOf(h: Handle) -> ResourceType` *statisch* | Zubehörtyp des Handles `h`. |
| `GetTypeName(type: ResourceType) -> str` *statisch* | Stabiler Name eines Zubehörtyps in lowerCamelCase-Schreibweise ("symbolDefinition", "hatch", "texture", ...). Gibt für `ResourceType.Unknown` eine leere Zeichenfolge zurück. |
| `GetTypeFromName(typeName: str) -> ResourceType` *statisch* | Wertet einen von GetTypeName erzeugten Typnamen aus (ohne Berücksichtigung der Groß-/Kleinschreibung). Gibt Unknown zurück, wenn er nicht übereinstimmt. |
| `GetAllTypes() -> list[ResourceType]` *statisch* | Alle von dieser API unterstützten Zubehörtypen, in der oben gezeigten Reihenfolge. |

*Nachschlagen*

| Methode | Beschreibung |
|---|---|
| `FromName(name: str) -> Resource` *statisch* | Zubehör der aktuellen Zeichnung mit diesem Namen; ungültig, wenn keines vorhanden ist. |
| `FromIndex(index: int) -> Resource` *statisch* | Zubehör mit diesem internen Index (Schraffur- / Farbverlaufs- / Mosaik- / Bild- / Linienart- / Texturindizes). |

*Identität*

| Methode | Beschreibung |
|---|---|
| `GetHandle() -> Handle` | Handle des Zubehörs. |
| `IsValid() -> bool` | True, wenn dieses Objekt auf vorhandenes Zubehör verweist. |
| `GetResourceType() -> ResourceType` | Gibt den Zubehörtyp zurück. |
| `GetObjectType() -> ObjectType` | Gibt den Objekttyp zurück. |
| `GetResourceTypeName() -> str` | Gibt den Namen des Zubehörtyps zurück. |
| `GetName() -> str \| None` | Gibt den Namen zurück. |
| `SetName(name: str) -> bool` | Benennt das Zubehör um; schlägt fehl, wenn ein anderes Objekt den Namen bereits verwendet. |
| `GetDescription() -> str \| None` | Gibt die Beschreibung zurück. |
| `SetDescription(description: str) -> bool` | Setzt die Beschreibung. |
| `GetInternalIndex() -> int \| None` | Gibt den internen Index zurück. |
| `GetUuid() -> str \| None` | Persistente UUID des Zubehörs, die über Sitzungen hinweg unverändert bleibt. |

*Zubehörordner*

| Methode | Beschreibung |
|---|---|
| `GetFolder() -> Handle` | Zubehörordner, der dieses Zubehör enthält; Null-Handle, wenn es auf der obersten Ebene des Zubehör-Managers liegt. |
| `GetFolderName() -> str \| None` | Gibt den Ordnernamen zurück. |
| `MoveToFolder(hFolder: Handle) -> bool` | Verschiebt das Zubehör nach `hFolder` (ein Zubehör des Typs `ResourceType.Folder`). |

*Inhalt*

| Methode | Beschreibung |
|---|---|
| `IsContainer() -> bool` | `True` für Zubehör, das andere Objekte enthält: Symboldefinitionen und Zubehörordner. |
| `GetContents() -> list[Handle]` | Objekte innerhalb des Zubehörs (die Geometrie einer Symboldefinition, das Zubehör eines Ordners). |
| `GetContentCount() -> int` | Anzahl der enthaltenen Elemente. |
| `ForEachContent(callback: callable(Handle)) -> None` | Ruft `callback` mit jedem Objekt innerhalb des Zubehörs auf. Objekte innerhalb des Zubehörs (die Geometrie einer Symboldefinition, das Zubehör eines Ordners). |

*Attribute*

| Methode | Beschreibung |
|---|---|
| `Attributes() -> ObjectAttributes` | Grafische Attribute für Zubehörtypen, die solche besitzen. |

*Lebensdauer*

| Methode | Beschreibung |
|---|---|
| `Duplicate() -> Resource` | Kopie des Zubehörs im selben Dokument und Ordner; ungültig bei Fehlschlag. |
| `Delete(useUndo: bool = True) -> bool` | Löscht das Zubehör aus dem Dokument; das Objekt wird ungültig. Objekte, die es verwenden, verlieren die Zubehörzuordnung. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True, wenn das Objekt gültig ist (entspricht `IsValid()`). |
| `==` | `__eq__(o: Resource) -> bool` | `a == b`: True, wenn beide Objekte auf dasselbe Zubehör verweisen. |
| `!=` | `__ne__(o: Resource) -> bool` | `a != b`: True, wenn die Objekte auf unterschiedliches Zubehör verweisen. |

### ResourceList

> **Vollständiger Name:** `api.ResourceList` · **Erbt von:** `api.Object`

Eine Liste von Zubehör eines Typs aus der aktuellen Zeichnung oder aus externen Inhalten. Sie kann nicht kopiert werden: Sie hält eine Vectorworks-Zubehörliste und gibt sie frei, wenn das Python-Objekt gelöscht wird.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ResourceList()` | Leere, ungültige Liste; füllen Sie sie mit einer der `Build...`-Methoden. |
| `ResourceList(type: ResourceType)` | Leere Liste dieses Typs. |

**Methoden**

*Aufbauen*

| Methode | Beschreibung |
|---|---|
| `BuildFromDocument(type: ResourceType, sort: bool = True) -> bool` | Zubehör des Typs `type`, das in der aktuellen Zeichnung definiert ist. |
| `BuildFromFolder(type: ResourceType, folder: ContentFolder, subFolder: str = '', includeDocument: bool = False, sort: bool = True) -> bool` | Zubehör des Typs `type` in einem Standard-Inhaltsordner von Vectorworks (externe Inhalte / Vorgabeinhalte). `subFolder` beschränkt die Suche auf einen Unterordner (oder Teilpfad) darin; eine leere Angabe bedeutet den gesamten Ordner. Mit `includeDocument` wird auch das Zubehör der aktuellen Zeichnung aufgelistet. |
| `BuildFromFolderIndex(type: ResourceType, folderIndex: int, subFolder: str = '', sort: bool = True) -> bool` | Dasselbe für eine Ordnerkennung, die in ContentFolder nicht benannt ist. Ein positiver `folderIndex` listet zusätzlich das Zubehör der aktuellen Zeichnung auf, ein negativer nur den Ordner und 0 nur die Zeichnung. |
| `BuildFromFile(type: ResourceType, filePath: str) -> bool` | Zubehör des Typs `type` in einer Vectorworks-Datei, angegeben durch ihren vollständigen Pfad im Format des Betriebssystems. |
| `BuildFromOpenDocument(type: ResourceType, openDocumentIndex: int, sort: bool = True) -> bool` | Zubehör des Typs `type` in einem anderen aktuell geöffneten Dokument (siehe die Liste der geöffneten Dateien in Vectorworks). |
| `FromDocument(type: ResourceType, sort: bool = True) -> ResourceList` *statisch* | Entsprechende Erzeugungsmethoden zu den Build...-Methoden. |
| `FromFolder(type: ResourceType, folder: ContentFolder, subFolder: str = '', includeDocument: bool = False, sort: bool = True) -> ResourceList` *statisch* | Neue Liste des Zubehörs vom Typ `type` im Inhaltsordner `folder`. Erzeugende Entsprechungen der Build...-Methoden. |
| `FromFolderIndex(type: ResourceType, folderIndex: int, subFolder: str = '', sort: bool = True) -> ResourceList` *statisch* | Neue Liste des Zubehörs vom Typ `type` im Inhaltsordner mit dem Index `folderIndex`. Erzeugende Entsprechungen der Build...-Methoden. |
| `FromFile(type: ResourceType, filePath: str) -> ResourceList` *statisch* | Neue Liste des Zubehörs vom Typ `type` in der Vectorworks-Datei `filePath`. Erzeugende Entsprechungen der Build...-Methoden. |
| `FromOpenDocument(type: ResourceType, openDocumentIndex: int, sort: bool = True) -> ResourceList` *statisch* | Neue Liste des Zubehörs vom Typ `type` in einem anderen geöffneten Dokument. Erzeugende Entsprechungen der Build...-Methoden. |
| `Dispose() -> None` | Gibt die Vectorworks-Zubehörliste frei. Wird automatisch aufgerufen, wenn das Python-Objekt gelöscht wird. |

*Identität*

| Methode | Beschreibung |
|---|---|
| `IsValid() -> bool` | True, wenn dieses Objekt auf eine vorhandene Zubehörliste verweist. |
| `GetListID() -> int` | Rohe ID der Vectorworks-Zubehörliste für Aufrufe auf niedriger Ebene, die sie noch benötigen. |
| `GetResourceType() -> ResourceType` | Gibt den Zubehörtyp zurück. |

*Inhaltsordner*

| Methode | Beschreibung |
|---|---|
| `GetContentFolderName(folder: ContentFolder) -> str` *statisch* | Stabiler Name eines Inhaltsordners in lowerCamelCase-Schreibweise ("hatches", "textures", "objectStyles", ...). |
| `GetContentFolderFromName(folderName: str) -> ContentFolder` *statisch* | Wertet einen von GetContentFolderName erzeugten Namen aus (ohne Berücksichtigung der Groß-/Kleinschreibung); `None`, wenn er nicht übereinstimmt. |
| `GetAllContentFolders() -> list[ContentFolder]` *statisch* | Gibt alle Inhaltsordner zurück. |

*Einträge*

| Methode | Beschreibung |
|---|---|
| `GetCount() -> int` | Gibt die Anzahl zurück. |
| `IsEmpty() -> bool` | True, wenn die Liste keine Einträge enthält. |
| `GetResource(index: int) -> Resource` | Zubehör am Index `index`; ungültig, solange der Eintrag zu externen Inhalten gehört, die noch nicht importiert wurden. |
| `GetName(index: int) -> str \| None` | Name, wie er im Zubehör-Manager angezeigt wird (bei externen Inhalten kann er den Namen der Quelldatei enthalten). |
| `GetActualName(index: int) -> str \| None` | Tatsächlicher Zubehörname, den es beim Import erhält. |
| `GetFolderName(index: int) -> str \| None` | Name des Zubehörordners, zu dem der Eintrag gehört; leer auf oberster Ebene. |
| `IsInDocument(index: int) -> bool` | Ob das Zubehör bereits in der aktuellen Zeichnung vorhanden ist. |
| `GetEntry(index: int) -> ResourceList.Entry \| None` | Gibt den Eintrag am Index `index` zurück. |
| `GetEntries() -> list[ResourceList.Entry]` | Gibt die Einträge zurück. |
| `ForEach(callback: callable(ResourceList.Entry)) -> None` | Ruft `callback` mit jedem Eintrag der Liste auf. |
| `Find(name: str) -> int` | Index des Eintrags, dessen tatsächlicher Name – oder, falls nicht gefunden, dessen angezeigter Name – `name` ist. Gibt `kNotFound` zurück, wenn kein Eintrag übereinstimmt. |
| `Contains(name: str) -> bool` | True, wenn ein Eintrag den tatsächlichen oder angezeigten Namen `name` hat. |

*Importieren*

| Methode | Beschreibung |
|---|---|
| `Import(index: int, onConflict: ImportConflict = ImportConflict.Rename) -> Resource` | Kopiert das Zubehör in die aktuelle Zeichnung und gibt es zurück. Bereits importiertes Zubehör wird unverändert zurückgegeben. Der Aufruf ändert das Dokument und muss daher innerhalb eines Rückgängig-Ereignisses erfolgen. Vectorworks registriert importiertes Zubehör selbst für die Rückgängig-Funktion: Registrieren Sie es nicht erneut mit `Document.AddAfterSwapObject`. |
| `Import(name: str, onConflict: ImportConflict = ImportConflict.Rename) -> Resource` | Kopiert das Zubehör in die aktuelle Zeichnung und gibt es zurück. Bereits importiertes Zubehör wird unverändert zurückgegeben. Der Aufruf ändert das Dokument und muss daher innerhalb eines Rückgängig-Ereignisses erfolgen. Vectorworks registriert importiertes Zubehör selbst für die Rückgängig-Funktion: Registrieren Sie es nicht erneut mit `Document.AddAfterSwapObject`. |
| `ImportWithResult(index: int, onConflict: ImportConflict = ImportConflict.Rename) -> ResourceList.ImportResult` | Import, der zusätzlich angibt, ob das Zubehör in die Zeichnung kopiert oder das bereits vorhandene zurückgegeben wurde. Es gelten dieselben Regeln wie für Import. |
| `SetClassRenamePrefix(prefix: str) -> None` | Präfix, das den Namen der Klassen vorangestellt wird, die mit importiertem Zubehör hinzukommen. Standardmäßig leer. |
| `GetClassRenamePrefix() -> str` | Gibt das Präfix zum Umbenennen der Klassen zurück. Präfix, das den Namen der Klassen vorangestellt wird, die mit importiertem Zubehör hinzukommen. Standardmäßig leer. |

*Liste bearbeiten*

| Methode | Beschreibung |
|---|---|
| `Add(hResource: Handle) -> int` | Fügt der Liste Zubehör der aktuellen Zeichnung hinzu; gibt seinen Index oder `kNotFound` zurück. |
| `Remove(index: int) -> bool` | Entfernt den Eintrag aus der Liste. Das Zubehör selbst wird nicht gelöscht. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True, wenn das Objekt gültig ist (entspricht `IsValid()`). |

**Konstanten**

| Konstante | Typ | Wert | Beschreibung |
|---|---|---|---|
| `ResourceList.kNotFound` | `int` | `2**64 - 1` | Von Find zurückgegebener Wert, wenn kein Eintrag übereinstimmt. |

#### ResourceList.Entry

> **Vollständiger Name:** `api.ResourceList.Entry` · **Erbt von:** `api.Object`

Ein Eintrag der Liste.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Entry()` | Standardwert (Felder mit ihren Standardwerten). |
| `Entry(index, name, actualName, folderName, handle, isInDocument)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `index` | `int` | 0-basierter Index in dieser Liste. |
| `name` | `str` | Name, wie er im Zubehör-Manager angezeigt wird. |
| `actualName` | `str` | Tatsächlicher Zubehörname (ohne den zur Unterscheidung ergänzten Dateinamen). |
| `folderName` | `str` | Übergeordneter Ordner des Zubehörs; auf der obersten Ebene leer. |
| `handle` | `Handle` | Null-Handle, solange sich das Zubehör nicht in der aktuellen Zeichnung befindet. |
| `isInDocument` | `bool` | `False` für externe Inhalte, die noch importiert werden müssen. |

#### ResourceList.ImportResult

> **Vollständiger Name:** `api.ResourceList.ImportResult` · **Erbt von:** `api.Object`

Ergebnis von ImportWithResult.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ImportResult()` | Standardwert (Felder mit ihren Standardwerten). |
| `ImportResult(handle, isImported)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `handle` | `Handle` | Das Zubehör in der aktuellen Zeichnung; Null-Handle, wenn der Import fehlgeschlagen ist. |
| `isImported` | `bool` | `True`, wenn dieser Aufruf das Zubehör in die Zeichnung kopiert hat (umbenannt. |

### TypedResource

> **Vollständiger Name:** `api.TypedResource` · **Erbt von:** [`Resource`](#resource) → `api.Object`

Auf einen ResourceType beschränktes Zubehör. Alles, was Resource bietet – Name, Beschreibung, Ordner, Duplizieren, Löschen – ist auch für die typisierten Klassen verfügbar.

**Konstruktoren**

Kann nicht direkt in Python instanziiert werden: Instanzen werden von anderen API-Funktionen zurückgegeben.

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetExpectedType() -> ResourceType` | Zubehörtyp, auf den diese Klasse beschränkt ist. |

Geerbt: alle Elemente von [`Resource`](#resource).

### HatchLevel

> **Vollständiger Name:** `api.HatchLevel` · **Erbt von:** `api.Object`

Eine Linienfamilie einer Schraffur. `startPoint` und `repeatVector` definieren die erste Linie der Familie: Die Linie verläuft entlang `repeatVector`, dessen Länge die Wiederholungslänge des Strichmusters ist. Die Familie wird als parallele Linien bei `startPoint` + n * `offsetVector` wiederholt. `dashFactor` ist der gezeichnete Anteil jeder Wiederholung (0 .. 1, 1 = durchgezogene Linie). Abstände werden in Welteinheiten angegeben, wenn die Schraffur im Weltkoordinatenraum arbeitet, und in papierbezogenen Einheiten (mm auf der Zeichnung), wenn sie diese verwendet – siehe `Hatch.GetUsePageUnits`.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `HatchLevel()` | Standardwert (Felder mit ihren Standardwerten). |
| `HatchLevel(startPoint, repeatVector, dashFactor, offsetVector, color, lineWeightMils)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `startPoint` | `Point2D` | Ursprung der Linienfamilie. |
| `repeatVector` | `Point2D` | Richtung der Linien und Wiederholungslänge des Strichmusters entlang der Linien. |
| `dashFactor` | `float` | Gezeichneter Anteil jeder Wiederholung, 1 = durchgezogene Linie (Vectorworks erwartet > 0). |
| `offsetVector` | `Point2D` | Abstand von einer parallelen Linie der Familie zur nächsten. |
| `color` | `ColorRGB` | Stiftfarbe der Linien. |
| `lineWeightMils` | `int` | Liniendicke in mil (1/1000 Zoll). |

### Hatch

> **Vollständiger Name:** `api.Hatch` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Vektorschraffurfüllung (`ObjectType.HatchDefinition`): eine Menge von Linienfamilien, die sich über die gefüllte Fläche wiederholen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Hatch(h: Handle)` | Verweist auf die vorhandene Schraffur `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> Hatch` *statisch* | Die Schraffur namens `name`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `FromIndex(index: int) -> Hatch` *statisch* | Die Schraffur mit dem internen Index `index`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `Create(name: str, usePageUnits: bool = False, transparent: bool = True, backgroundColor: ColorRGB = ColorRGB()) -> Hatch` *statisch* | Erzeugt eine leere Schraffur. Wenn `name` bereits vergeben ist, wird eine Zahl angehängt. |

*Einstellungen*

| Methode | Beschreibung |
|---|---|
| `GetUsePageUnits() -> bool \| None` | `True`, wenn die Schraffur auf der gedruckten Seite statt in Welteinheiten gemessen wird. |
| `SetUsePageUnits(value: bool) -> bool` | Schaltet *Papierbezogene Einheiten verwenden* ein oder aus. `True`, wenn die Schraffur auf der gedruckten Seite statt in Welteinheiten gemessen wird. |
| `GetTransparent() -> bool \| None` | `True`, wenn die Fläche hinter den Schraffurlinien transparent bleibt, statt mit dem Hintergrund gefüllt zu werden. |
| `SetTransparent(value: bool) -> bool` | Schaltet *Transparent* ein oder aus. `True`, wenn die Fläche hinter den Schraffurlinien transparent bleibt, statt mit dem Hintergrund gefüllt zu werden. |
| `GetRotateInWalls() -> bool \| None` | Ob die Schraffur der Drehung der Wand / des Symbols folgt, in der bzw. dem sie gezeichnet wird. |
| `SetRotateInWalls(value: bool) -> bool` | Schaltet *In Wänden mitdrehen* ein oder aus. Ob die Schraffur der Drehung der Wand / des Symbols folgt, in der bzw. dem sie gezeichnet wird. |
| `GetRotateInSymbols() -> bool \| None` | Ob *In Symbolen mitdrehen* eingeschaltet ist. |
| `SetRotateInSymbols(value: bool) -> bool` | Schaltet *In Symbolen mitdrehen* ein oder aus. |

*Ebenen*

| Methode | Beschreibung |
|---|---|
| `GetLevelCount() -> int` | Ebenen (Linienfamilien) sind 0-basiert. Es gibt keine feste Obergrenze für die Anzahl der Ebenen einer Schraffur. |
| `GetLevel(index: int) -> HatchLevel \| None` | Gibt die Ebene am Index `index` zurück. |
| `GetLevels() -> list[HatchLevel]` | Gibt die Ebenen zurück. |
| `SetLevel(index: int, level: HatchLevel) -> bool` | Ersetzt die Ebene am Index `index`; Anhängen ist bei index == `GetLevelCount()` zulässig. |
| `AddLevel(level: HatchLevel) -> bool` | Hängt die Ebene `level` an. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### GradientSegment

> **Vollständiger Name:** `api.GradientSegment` · **Erbt von:** `api.Object`

Ein Farbstopp eines Farbverlaufs. `spotPosition` ist die Position der Farbe (0 .. 1 über den gesamten Farbverlauf), und `midpointPosition` ist die Position, an der der Übergang zum nächsten Farbstopp zur Hälfte erfolgt ist (0 .. 1 zwischen den beiden Stopps).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `GradientSegment()` | Standardwert (Felder mit ihren Standardwerten). |
| `GradientSegment(spotPosition, midpointPosition, color, opacity)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `spotPosition` | `float` | Position des Farbstopps entlang des Farbverlaufs (0 .. 1). |
| `midpointPosition` | `float` | Position des Mittelpunkts zum nächsten Farbstopp (0 .. 1). |
| `color` | `ColorRGB` | Farbe des Farbstopps. |
| `opacity` | `int` | 0 = vollständig transparent, 100 = deckend. |

### Gradient

> **Vollständiger Name:** `api.Gradient` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Verlaufsfüllung (`ObjectType.GradientDefinition`): ein Übergang zwischen zwei oder mehr Farbpunkten.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Gradient(h: Handle)` | Verweist auf den vorhandenen Farbverlauf `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> Gradient` *statisch* | Der Farbverlauf namens `name`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `FromIndex(index: int) -> Gradient` *statisch* | Der Farbverlauf mit dem internen Index `index`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `Create(name: str) -> Gradient` *statisch* | Erzeugt einen Farbverlauf mit den zwei standardmäßigen Farbstopps. An einen bereits vergebenen Namen wird eine Zahl angehängt. |
| `GetSegmentCount() -> int` | Farbstopps sind 0-basiert und nach Farbposition geordnet, von 0 bis `GetSegmentCount()` - 1. |
| `GetSegment(index: int) -> GradientSegment \| None` | Gibt das Segment am Index `index` zurück. |
| `GetSegments() -> list[GradientSegment]` | Gibt die Segmente zurück. |
| `SetSegment(index: int, segment: GradientSegment) -> bool` | Eine Änderung der Farbposition kann die Farbstopps neu sortieren, sodass sich der Stopp anschließend an einem anderen Index befinden kann. |
| `InsertSegment(segment: GradientSegment) -> int \| None` | Fügt einen Farbstopp hinzu; der Farbverlauf hält seine Stopps sortiert, daher wird der 0-basierte Index des neuen Stopps zurückgegeben. Gibt `None` zurück, wenn der Stopp nicht hinzugefügt wurde. |
| `RemoveSegment(index: int) -> bool` | Entfernt den Farbstopp am Index `index`. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### Tile

> **Vollständiger Name:** `api.Tile` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Mosaikfüllung (`ObjectType.TileDefinition`): eine Gruppe von 2D-Objekten, die sich auf einem Raster über die gefüllte Fläche wiederholt.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Tile(h: Handle)` | Verweist auf das vorhandene Mosaik `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> Tile` *statisch* | Das Mosaik namens `name`; ein ungültiges Objekt, wenn keines vorhanden ist. |
| `FromIndex(index: int) -> Tile` *statisch* | Das Mosaik mit dem internen Index `index`; ein ungültiges Objekt, wenn keines vorhanden ist. |
| `Create(name: str) -> Tile` *statisch* | Erstellt ein leeres Mosaik. An einen bereits vergebenen Namen wird eine Zahl angehängt. |

*Geometrie*

| Methode | Beschreibung |
|---|---|
| `GetGeometryGroup() -> Handle` | Gruppe mit den 2D-Objekten, die das Mosaik wiederholt; fügen Sie mit AddGeometry Geometrie hinzu. |
| `GetGeometry() -> list[Handle]` | Gibt die Geometrie zurück. |
| `AddGeometry(hObject: Handle) -> bool` | Verschiebt ein vorhandenes 2D-Objekt in das Mosaik. |

*Einstellungen*

| Methode | Beschreibung |
|---|---|
| `GetOffset() -> Point2D \| None` | Ursprung des Mosaikrasters und Schrittweite von einer Wiederholung zur nächsten. |
| `SetOffset(value: Point2D) -> bool` | Legt den Versatz fest. Ursprung des Mosaikrasters und Schrittweite von einer Wiederholung zur nächsten. |
| `GetRepetition() -> Point2D \| None` | Gibt die Wiederholung zurück. |
| `SetRepetition(value: Point2D) -> bool` | Legt die Wiederholung fest. |
| `GetUsePageUnits() -> bool \| None` | `True`, wenn das Mosaik auf der gedruckten Seite statt in Welteinheiten gemessen wird. |
| `SetUsePageUnits(value: bool) -> bool` | Schaltet *Papierbezogene Einheiten verwenden* ein oder aus. `True`, wenn das Mosaik auf der gedruckten Seite statt in Welteinheiten gemessen wird. |
| `GetTransparentBackground() -> bool \| None` | Ob *Transparenter Hintergrund* eingeschaltet ist. |
| `SetTransparentBackground(value: bool) -> bool` | Schaltet *Transparenter Hintergrund* ein oder aus. |
| `GetBackgroundColor() -> ColorRGB \| None` | Gibt die Hintergrundfarbe zurück. |
| `SetBackgroundColor(color: ColorRGB) -> bool` | Legt die Hintergrundfarbe fest. |
| `GetRotateInWalls() -> bool \| None` | Ob *In Wänden mitdrehen* eingeschaltet ist. |
| `SetRotateInWalls(value: bool) -> bool` | Schaltet *In Wänden mitdrehen* ein oder aus. |
| `GetRotateInSymbols() -> bool \| None` | Ob *In Symbolen mitdrehen* eingeschaltet ist. |
| `SetRotateInSymbols(value: bool) -> bool` | Schaltet *In Symbolen mitdrehen* ein oder aus. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### ImageFill

> **Vollständiger Name:** `api.ImageFill` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Bildzubehör (`ObjectType.ImageDefinition`): eine Bitmap, die als Bildfüllung, Bildobjekt oder Texturbild verwendet wird.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ImageFill(h: Handle)` | Verweist auf die vorhandene Bildfüllung `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> ImageFill` *statisch* | Die Bildfüllung namens `name`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `FromIndex(index: int) -> ImageFill` *statisch* | Die Bildfüllung mit dem internen Index `index`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `GetWidthPixels() -> int \| None` | Gibt die Breite in Pixeln zurück. |
| `GetHeightPixels() -> int \| None` | Gibt die Höhe in Pixeln zurück. |
| `GetCompression() -> ImageFill.Compression \| None` | Gibt die Komprimierung zurück. |
| `SetCompression(value: ImageFill.Compression) -> bool` | Legt die Komprimierung fest. |
| `CreateFromPngData(pngData: bytes) -> ImageFill` *statisch* | Erzeugt eine Bildfüllung aus dem Inhalt einer PNG-Datei (`bytes`). |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

#### ImageFill.Compression

> **Vollständiger Name:** `api.ImageFill.Compression` · **Art:** `IntEnum`

Komprimierung, mit der das Bild gespeichert wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` |  |
| `Jpeg` | `1` |  |
| `Png` | `2` |  |
| `PngMonochrome` | `3` |  |

### LineType

> **Vollständiger Name:** `api.LineType` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Linienart-Zubehör. Es gibt zwei Arten:

- einfach — ein Strichmuster: abwechselnde Strich- und Lückenlängen (siehe GetDashPattern). komplex – eine Gruppe von 2D-Objekten, die sich entlang der Linie wiederholt (siehe GetGeometry).

Objekte verweisen über ihren Stiftstil auf eine Linienart; siehe `PenAttributes.SetLineType`.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `LineType(h: Handle)` | Verweist auf die vorhandene Linienart `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> LineType` *statisch* | Die Linienart namens `name`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `FromIndex(index: int) -> LineType` *statisch* | Die Linienart mit dem internen Index `index`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `CreateSimple(dashPattern: list[float], scaleWithLineWeight: bool = False) -> LineType` *statisch* | Sucht oder erzeugt eine einfache Linienart mit diesem Strichmuster: abwechselnde Strich- und Lückenlängen, höchstens 16 Einträge. `scaleWithLineWeight` skaliert das Muster mit der Liniendicke des Objekts. Vectorworks verwendet eine vorhandene passende Linienart wieder – auch aus den Vorgabeinhalten –, statt ein Duplikat zu erzeugen; daher kann das zurückgegebene Zubehör einen anderen Namen tragen. |
| `CreateComplex(name: str) -> LineType` *statisch* | Erstellt eine leere komplexe Linienart; fügen Sie die wiederholten 2D-Objekte mit AddGeometry hinzu. |

*Art*

| Methode | Beschreibung |
|---|---|
| `IsSimple() -> bool \| None` | True für eine einfache (gestrichelte) Linienart. |
| `IsComplex() -> bool \| None` | True für eine komplexe Linienart (wiederholte Geometrie). |

*Einfache Linienart*

| Methode | Beschreibung |
|---|---|
| `GetDashPattern() -> list[float]` | Abwechselnde Strich- und Lückenlängen; leer bei einer komplexen Linienart. |
| `GetScaleWithLineWeight() -> bool \| None` | Ob *Mit Liniendicke skalieren* eingeschaltet ist. |

*Komplexe Linienart*

| Methode | Beschreibung |
|---|---|
| `GetGeometryGroup() -> Handle` | Gruppe mit den entlang der Linie wiederholten 2D-Objekten; null bei einer einfachen Linienart. |
| `GetGeometry() -> list[Handle]` | Gibt die Geometrie zurück. |
| `AddGeometry(hObject: Handle) -> bool` | Verschiebt ein vorhandenes 2D-Objekt in die Linienart. |
| `GetGapSize() -> float \| None` | Lücke zwischen zwei Wiederholungen der Geometrie, in Welteinheiten (oder in papierbezogenen Einheiten bei papierbezogener Darstellung). |
| `SetGapSize(value: float) -> bool` | Legt die Lückengröße fest. Lücke zwischen zwei Wiederholungen der Geometrie, in Welteinheiten (oder in papierbezogenen Einheiten bei papierbezogener Darstellung). |
| `GetUsePageUnits() -> bool \| None` | `True`, wenn die Linienart auf der gedruckten Seite statt in Welteinheiten gemessen wird. |
| `SetUsePageUnits(value: bool) -> bool` | Schaltet *Papierbezogene Einheiten verwenden* ein oder aus. `True`, wenn die Linienart auf der gedruckten Seite statt in Welteinheiten gemessen wird. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### RecordField

> **Vollständiger Name:** `api.RecordField` · **Erbt von:** `api.Object`

Ein Feld einer Datenbank.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RecordField()` | Standardwert (Felder mit ihren Standardwerten). |
| `RecordField(name, localizedName, type, defaultValue)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `name` | `str` | Universeller (nicht lokalisierter) Name, den APIs verwenden. |
| `localizedName` | `str` | In der Benutzeroberfläche angezeigter Name. |
| `type` | `RecordFieldType` | Feldtyp. |
| `defaultValue` | `str` | Anfangswert neuer Datenbankeinträge, als Text. |

### RecordFormat

> **Vollständiger Name:** `api.RecordFormat` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Datenbank. Beim Verknüpfen mit einem Objekt wird daran ein Datenbankeintrag erzeugt – ein Satz von Werten für diese Felder; siehe Document zum Lesen und Schreiben der Werte eines verknüpften Datenbankeintrags.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RecordFormat(h: Handle)` | Verweist auf die vorhandene Datenbank `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> RecordFormat` *statisch* | Die Datenbank namens `name`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `FromIndex(index: int) -> RecordFormat` *statisch* | Die Datenbank mit dem internen Index `index`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `Create(name: str) -> RecordFormat` *statisch* | Erstellt eine leere Datenbank; gibt die vorhandene zurück, wenn der Name bereits vergeben ist. |
| `IsInternalName(name: str) -> bool` *statisch* | `True` für Namen, die für interne Datenbanken reserviert sind: Präfix "NNA_" oder "__NNA", ohne Berücksichtigung der Groß-/Kleinschreibung. |
| `GetFieldTypeName(type: RecordFieldType) -> str` *statisch* | Stabiler Name eines Feldtyps in lowerCamelCase-Schreibweise ("integer", "text", "popUp", ...). |
| `GetFieldTypeFromName(typeName: str) -> RecordFieldType` *statisch* | Gibt den Feldtyp zum Namen `typeName` zurück. |
| `GetAllFieldTypes() -> list[RecordFieldType]` *statisch* | Gibt alle Feldtypen zurück. |

*Formateinstellungen*

| Methode | Beschreibung |
|---|---|
| `GetLocalizedName() -> str \| None` | Gibt den lokalisierten Namen zurück. |
| `SetLocalizedName(name: str) -> bool` | Legt den lokalisierten Namen fest. |
| `IsParametric() -> bool \| None` | Eine parametrische Datenbank gehört zu einem Plug-in-Objekt und darf nicht bearbeitet werden. |
| `GetVisible() -> bool \| None` | Ausgeblendete Datenbanken erscheinen nicht im Datenbereich der Infopalette. |
| `SetVisible(value: bool) -> bool` | Schaltet *Sichtbar* ein oder aus. Ausgeblendete Datenbanken erscheinen nicht im Datenbereich der Infopalette. |

*Felder*

| Methode | Beschreibung |
|---|---|
| `GetFieldCount() -> int` | Anzahl der Felder. |
| `GetField(index: int) -> RecordField \| None` | Gibt das Feld am Index `index` zurück. |
| `GetFields() -> list[RecordField]` | Gibt die Felder zurück. |
| `FindField(fieldName: str) -> int` | Index des Felds namens `fieldName`; `kNotFound`, wenn keines vorhanden ist. |
| `HasField(fieldName: str) -> bool` | True, wenn die Datenbank ein Feld namens `fieldName` hat. |
| `AddField(name: str, type: RecordFieldType, defaultValue: str = '', updateExistingRecords: bool = True) -> int` | Fügt ein Feld hinzu. `defaultValue` wird gemäß `type` wie ein vom Benutzer eingegebener Wert ausgewertet; eine leere Zeichenfolge verwendet den Leerwert des Typs. Texttypen behalten die Zeichenfolge; `RecordFieldType.Boolean` akzeptiert die Zeichenfolge "True" oder "False"; `RecordFieldType.Color` erwartet "red,green,blue" (jeweils 0 .. 65535); `RecordFieldType.Class`, `BuildingMaterial`, `Texture` und `SymbolDefinition` erwarten den Namen vorhandenen Zubehörs dieses Typs; `Fill` und `PenStyle` erwarten den Namen einer Schraffur, eines Mosaiks, eines Farbverlaufs, eines Bilds oder einer Linienart. `updateExistingRecords` fügt das Feld den bereits mit Objekten verknüpften Datenbankeinträgen mit `defaultValue` als Wert hinzu. Gibt den Index des neuen Felds zurück, oder `kNotFound`, wenn `defaultValue` für `type` ungültig ist, der Typ nicht hinzugefügt werden kann (`Radio`, `ControlPoint`, `LayerPopUp` und die ausschließlich für Plug-ins vorgesehenen Typen) oder das Feld nicht erzeugt wird. |
| `RemoveField(fieldName: str) -> bool` | Entfernt das Feld namens `fieldName`. |
| `RenameField(index: int, name: str) -> bool` | Benennt das Feld am Index `index` in `name` um. |
| `GetFieldDefaultValue(fieldName: str) -> str \| None` | Vorgabewert eines Felds als Text. |
| `SetFieldDefaultValue(fieldName: str, value: str) -> bool` | Legt den Standardwert des Felds fest. Standardwert eines Felds, als Text. |

*Auswahlmöglichkeiten im Einblendmenü*

| Methode | Beschreibung |
|---|---|
| `GetFieldChoices(fieldName: str) -> list[str]` | Auswahlmöglichkeiten eines PopUp-Felds in ihrer Reihenfolge. |
| `SetFieldChoices(fieldName: str, choices: list[str]) -> bool` | Ersetzt die Auswahlmöglichkeiten eines PopUp-Felds. |

**Konstanten**

| Konstante | Typ | Wert | Beschreibung |
|---|---|---|---|
| `RecordFormat.kNotFound` | `int` | `2**64 - 1` | Index des Felds mit diesem universellen Namen; `kNotFound`, wenn keines vorhanden ist. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### Texture

> **Vollständiger Name:** `api.Texture` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Textur (`ObjectType.Texture`): Farbe, Reflexion, Transparenz und Relief einer gerenderten Oberfläche.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Texture(h: Handle)` | Verweist auf die vorhandene Textur `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> Texture` *statisch* | Die Textur namens `name`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `FromIndex(index: int) -> Texture` *statisch* | Die Textur mit dem internen Index `index`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `Create(name: str) -> Texture` *statisch* | Erstellt eine leere Textur. Ist ein Name bereits vergeben, wird eine Zahl angehängt. |
| `GetSize() -> float \| None` | Reale Größe, die das Texturbild abdeckt, in Welteinheiten. |
| `SetSize(value: float) -> bool` | Legt die Größe fest. Reale Größe, die das Texturbild abdeckt, in Welteinheiten. |
| `GetUVAspectRatio() -> float \| None` | Verhältnis der U- zur V-Ausdehnung des Texturbilds. |
| `ApplyToObject(hObject: Handle, part: Texture.Part = Texture.Part.Overall) -> bool` | Weist die Textur einem Objekt (oder einem seiner Teile) zu. |
| `UpdateThumbnail() -> bool` | Aktualisiert nach einer Änderung der Textur die Vorschau im Zubehör-Manager. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

#### Texture.Part

> **Vollständiger Name:** `api.Texture.Part` · **Art:** `IntEnum`

Teil eines Objekts, auf den eine Textur angewendet wird. Objekte ohne Teile verwenden Overall.

| Element | Wert | Beschreibung |
|---|---|---|
| `Overall` | `0` | Das gesamte Objekt. |
| `ExtrudeTop` | `1` |  |
| `ExtrudeBottom` | `2` |  |
| `ExtrudeSides` | `3` | Extrusionskörper und Rotationskörper. |
| `WallLeft` | `4` |  |
| `WallRight` | `5` |  |
| `WallTop` | `6` |  |
| `WallBottom` | `7` | Wände. |
| `SlabTop` | `8` |  |
| `SlabBottom` | `9` |  |
| `SlabSides` | `10` | Böden/Decken. |
| `RoofTop` | `11` |  |
| `RoofBottom` | `12` |  |
| `RoofSides` | `13` | Dächer. |

### RenderStyle

> **Vollständiger Name:** `api.RenderStyle` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Renderstil (`ObjectType.RenderStyle`): eine gespeicherte Konfiguration der Rendereinstellungen, die auf einen Ansichtsbereich oder eine Ebene angewendet wird.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RenderStyle(h: Handle)` | Verweist auf den vorhandenen Renderstil `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> RenderStyle` *statisch* | Der Renderstil namens `name`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `FromIndex(index: int) -> RenderStyle` *statisch* | Der Renderstil mit dem internen Index `index`; ein ungültiges Objekt, wenn keiner vorhanden ist. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### RenderBackground

> **Vollständiger Name:** `api.RenderBackground` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Renderworks-Hintergrund (`ObjectType.RenderBackground`): die Darstellung hinter dem Modell beim Rendern.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RenderBackground(h: Handle)` | Verweist auf den vorhandenen Renderworks-Hintergrund `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> RenderBackground` *statisch* | Der Renderworks-Hintergrund namens `name`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `FromIndex(index: int) -> RenderBackground` *statisch* | Der Renderworks-Hintergrund mit dem internen Index `index`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `Create(name: str, kind: RenderBackground.Kind) -> RenderBackground` *statisch* | Erstellt einen Hintergrund dieses Typs. Ist ein Name bereits vergeben, wird eine Zahl angehängt. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

#### RenderBackground.Kind

> **Vollständiger Name:** `api.RenderBackground.Kind` · **Art:** `IntEnum`

Art des Hintergrunds, mit dem neues Zubehör erzeugt wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `Clouds` | `0` |  |
| `OneColor` | `1` |  |
| `TwoColor` | `2` |  |
| `PhysicalSky` | `3` |  |

### TextStyle

> **Vollständiger Name:** `api.TextStyle` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Textstil (`ObjectType.TextStyle`): Schriftart, Größe und Textattribute für Textobjekte und Bemaßungen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `TextStyle(h: Handle)` | Verweist auf den vorhandenen Textstil `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> TextStyle` *statisch* | Der Textstil namens `name`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `FromIndex(index: int) -> TextStyle` *statisch* | Der Textstil mit dem internen Index `index`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `Create(name: str) -> TextStyle` *statisch* | Erstellt einen Textstil; gibt den vorhandenen zurück, wenn der Name bereits vergeben ist. |
| `ApplyToObject(hObject: Handle) -> bool` | Wendet den Stil auf ein Textobjekt (oder ein beliebiges Objekt mit Textattributen) an. |
| `OfObject(hObject: Handle) -> TextStyle` *statisch* | Textstil, dem ein Objekt folgt; ungültig, wenn das Objekt eigene Textattribute verwendet. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### WallStyle

> **Vollständiger Name:** `api.WallStyle` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Wandstil (`ObjectType.WallStyle`): Schalen, Dicke und Attribute einer Wand.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `WallStyle(h: Handle)` | Verweist auf den vorhandenen Wandstil `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> WallStyle` *statisch* | Der Wandstil namens `name`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `FromIndex(index: int) -> WallStyle` *statisch* | Der Wandstil mit dem internen Index `index`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `Create(name: str) -> WallStyle` *statisch* | Erstellt einen Wandstil; gibt den vorhandenen zurück, wenn der Name bereits vergeben ist. |
| `ApplyToObject(hWall: Handle, selectedOffset: float = 0.0, replacingOffset: float = 0.0) -> bool` | Wendet den Stil auf eine Wand an. Die beiden Versätze geben an, welche Linie der alten Wand und welche Linie des neuen Stils ihre Position beibehalten, gemessen von der Wandmitte in Welteinheiten; 0 erhält die Mittellinie. |
| `OfObject(hWall: Handle) -> WallStyle` *statisch* | Der Wandstil, dem die Wand `hWall` folgt (ungültig, wenn sie keinen hat). |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### SlabStyle

> **Vollständiger Name:** `api.SlabStyle` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Boden/Deckenstil (`ObjectType.SlabStyle`): Schalen und Attribute eines Bodens bzw. einer Decke.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `SlabStyle(h: Handle)` | Verweist auf den vorhandenen Boden/Deckenstil `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> SlabStyle` *statisch* | Der Boden/Deckenstil namens `name`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `FromIndex(index: int) -> SlabStyle` *statisch* | Der Boden/Deckenstil mit dem internen Index `index`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `Create(name: str) -> SlabStyle` *statisch* | Erstellt einen Boden/Deckenstil; gibt den vorhandenen zurück, wenn der Name bereits vergeben ist. |
| `ApplyToObject(hSlab: Handle) -> bool` | Wendet diesen Boden/Deckenstil auf das Boden/Decken-Objekt `hSlab` an. |
| `OfObject(hSlab: Handle) -> SlabStyle` *statisch* | Der Boden/Deckenstil, dem das Boden/Decken-Objekt `hSlab` folgt (ungültig, wenn es keinen hat). |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### RoofStyle

> **Vollständiger Name:** `api.RoofStyle` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Dachstil (`ObjectType.RoofStyle`): Schalen und Attribute eines Dachs.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RoofStyle(h: Handle)` | Verweist auf den vorhandenen Dachstil `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> RoofStyle` *statisch* | Der Dachstil namens `name`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `FromIndex(index: int) -> RoofStyle` *statisch* | Der Dachstil mit dem internen Index `index`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `Create(name: str) -> RoofStyle` *statisch* | Erstellt einen Dachstil; gibt den vorhandenen zurück, wenn der Name bereits vergeben ist. |
| `ApplyToObject(hRoof: Handle) -> bool` | Wendet diesen Dachstil auf das Dach `hRoof` an. |
| `OfObject(hRoof: Handle) -> RoofStyle` *statisch* | Der Dachstil, dem das Dach `hRoof` folgt (ungültig, wenn es keinen hat). |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### ViewportStyle

> **Vollständiger Name:** `api.ViewportStyle` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Ansichtsbereichstil (`ObjectType.ViewportStyle`): die gespeicherten Einstellungen eines Ansichtsbereichs auf einer Layoutebene.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ViewportStyle(h: Handle)` | Verweist auf den vorhandenen Ansichtsbereichstil `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> ViewportStyle` *statisch* | Der Ansichtsbereichstil namens `name`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `FromIndex(index: int) -> ViewportStyle` *statisch* | Der Ansichtsbereichstil mit dem internen Index `index`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `ApplyToObject(hViewport: Handle) -> bool` | Wendet diesen Ansichtsbereichstil auf den Ansichtsbereich `hViewport` an. |
| `OfObject(hViewport: Handle) -> ViewportStyle` *statisch* | Der Ansichtsbereichstil, dem der Ansichtsbereich `hViewport` folgt (ungültig, wenn er keinen hat). |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### BuildingMaterial

> **Vollständiger Name:** `api.BuildingMaterial` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Material (Baumaterial, `ObjectType.BuildingMaterial`): das physische Material einer Wand-, Boden/Decken- oder Dachschale. Es enthält die Attribute und Daten (Feuerwiderstand, Wärmekennwerte, ...) dieses Materials.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `BuildingMaterial(h: Handle)` | Verweist auf das vorhandene Material `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> BuildingMaterial` *statisch* | Das Material namens `name`; ein ungültiges Objekt, wenn keines vorhanden ist. |
| `FromIndex(index: int) -> BuildingMaterial` *statisch* | Das Material mit dem internen Index `index`; ein ungültiges Objekt, wenn keines vorhanden ist. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### DataVisualization

> **Vollständiger Name:** `api.DataVisualization` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Datenvisualisierung (`ObjectType.DataVisualization`): eine Regel, die die grafischen Attribute von Objekten überschreibt, die einem Kriterium entsprechen; sie wird auf einen Ansichtsbereich oder auf die Konstruktionsebenen angewendet. Vectorworks identifiziert Datenvisualisierungen anhand ihres Namens, daher arbeitet diese Klasse mit Namen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DataVisualization(h: Handle)` | Verweist auf die vorhandene Datenvisualisierung `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> DataVisualization` *statisch* | Die Datenvisualisierung namens `name`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `GetAllNames() -> list[str]` *statisch* | Namen aller Datenvisualisierungen des aktuellen Dokuments. |
| `Rename(oldName: str, newName: str) -> bool` *statisch* | Benennt die Datenvisualisierung `oldName` in `newName` um. |
| `DeleteByName(name: str) -> bool` *statisch* | Löscht die Datenvisualisierung namens `name`. |
| `GetActiveOn(hObject: Handle) -> list[str]` *statisch* | Namen der auf einem Objekt aktiven Datenvisualisierungen (einem Ansichtsbereich, einer gesicherten Darstellung oder einer Ebene). |
| `Activate(hObject: Handle, name: str, activate: bool) -> bool` *statisch* | Schaltet eine Datenvisualisierung für dieses Objekt ein oder aus. |
| `SetObjectExcluded(hObject: Handle, exclude: bool) -> bool` *statisch* | Schließt ein Objekt von allen Datenvisualisierungen aus. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### ResourceFolderPath

> **Vollständiger Name:** `api.ResourceFolderPath` · **Erbt von:** `api.Object`

Ordner eines mit `ResourceFolder.CreatePathFolders` erzeugten Pfads.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ResourceFolderPath()` | Standardwert (Felder mit ihren Standardwerten). |
| `ResourceFolderPath(folders, createdFolders)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `folders` | `list[Handle]` | Alle Ordner des Pfads, mit dem äußersten beginnend; bei einem Fehlschlag leer. |
| `createdFolders` | `list[Handle]` | Die von diesem Aufruf angelegten Ordner, mit dem äußersten beginnend. |

### ResourceFolder

> **Vollständiger Name:** `api.ResourceFolder` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Zubehörordner (`ObjectType.Folder`): gruppiert Zubehör desselben Typs im Zubehör-Manager.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ResourceFolder(h: Handle)` | Verweist auf den vorhandenen Zubehörordner `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> ResourceFolder` *statisch* | Der Zubehörordner namens `name`; ein ungültiges Objekt, wenn keiner vorhanden ist. |
| `Create(name: str, forType: ResourceType) -> ResourceFolder` *statisch* | Erzeugt einen Ordner auf der obersten Ebene für Zubehör dieses Typs. Schlägt fehl (ungültiger Ordner), wenn der Name bereits vergeben ist; Zubehörnamen sind innerhalb eines Dokuments eindeutig. Die Rückgängig-Funktion wird nicht registriert: Registrieren Sie den neuen Ordner mit `Document.AddAfterSwapObject`. |
| `CreatePath(folderPath: str, forType: ResourceType) -> ResourceFolder` *statisch* | Erzeugt eine Kette verschachtelter Ordner aus einem Pfad wie "Türen/Innen"; gibt den innersten Ordner zurück. Die Regeln finden Sie bei CreatePathFolders. |
| `CreatePathFolders(folderPath: str, forType: ResourceType) -> ResourceFolderPath` *statisch* | Erzeugt eine Kette verschachtelter Ordner aus einem Pfad wie "Türen/Innen" und gibt alle zurück. Ein Ordner des Pfads, der für `forType` bereits an genau dieser Stelle existiert, wird wiederverwendet. Schlägt fehl (leeres Ergebnis), wenn ein Name des Pfads anderweitig vergeben ist, auch durch einen Ordner an anderer Stelle oder für einen anderen Typ; die bis dahin angelegten Ordner werden dann wieder entfernt. Leere Namen ("A//B", ein führender oder abschließender '/') werden übersprungen. Die Rückgängig-Funktion wird nicht registriert: Registrieren Sie nur den ersten Eintrag von `createdFolders` (den äußersten neuen Ordner) mit `Document.AddAfterSwapObject`. Er enthält die anderen neuen Ordner, und das Registrieren eines Ordners markiert auch seinen Inhalt als eingefügt; würde ein tiefer liegender neuer Ordner ebenfalls registriert, würde er zweimal eingefügt. Registrieren Sie niemals die wiederverwendeten Ordner. |
| `GetContentType() -> ResourceType \| None` | Typ des Zubehörs, das der Ordner enthält. |
| `GetResources() -> list[Handle]` | Zubehör im Ordner. |
| `Add(hResource: Handle) -> bool` | Verschiebt ein Zubehör in diesen Ordner. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

### SymbolDefinition

> **Vollständiger Name:** `api.SymbolDefinition` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Symboldefinition. Ihr Inhalt besteht aus den Objekten, die das Symbol zeichnet; jede Instanz in der Zeichnung zeigt denselben Inhalt, sodass dessen Bearbeitung alle Instanzen gleichzeitig aktualisiert. Ein Pflanzenstil, ein Plankopf-Stil und andere Objektstile sind ebenfalls Symboldefinitionen – sie enthalten als einzigen Inhalt ein Plug-in-Objekt (siehe `PlantObject.EnsurePlantStyle`).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `SymbolDefinition(h: Handle)` | Verweist auf die vorhandene Symboldefinition `h`; prüfen Sie vor der Verwendung `IsValid()`. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> SymbolDefinition` *statisch* | Die Symboldefinition namens `name`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `FromIndex(index: int) -> SymbolDefinition` *statisch* | Die Symboldefinition mit dem internen Index `index`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `Create(name: str) -> SymbolDefinition` *statisch* | Erzeugt eine leere Symboldefinition. An einen bereits vergebenen Namen wird eine Zahl angehängt; lesen Sie den Namen daher mit `GetName()` wieder aus. |
| `GetActive() -> SymbolDefinition` *statisch* | Symboldefinition, aus der neue Symbolinstanzen erstellt werden. |
| `SetActive() -> bool` | Legt die aktive Symboldefinition fest. Symboldefinition, aus der neue Symbolinstanzen erzeugt werden. |

*Art*

| Methode | Beschreibung |
|---|---|
| `GetGeometryType() -> SymbolDefinition.GeometryType \| None` | Gibt den Geometrietyp zurück. |
| `CanInsertIntoWalls() -> bool \| None` | `True`, wenn das Symbol in eine Wand eingesetzt werden darf (es besitzt einen Wandeinfügepunkt). |
| `ContainsLight() -> bool \| None` | True, wenn die Symboldefinition eine Lichtquelle enthält. |

*Einfügeverhalten*

| Methode | Beschreibung |
|---|---|
| `GetInsertMode() -> SymbolDefinition.InsertMode \| None` | Gibt den Einfügemodus zurück. |
| `SetInsertMode(value: SymbolDefinition.InsertMode) -> bool` | Legt den Einfügemodus fest. |
| `GetBreakMode() -> SymbolDefinition.BreakMode \| None` | Gibt den Wandunterbrechungsmodus zurück. |
| `SetBreakMode(value: SymbolDefinition.BreakMode) -> bool` | Legt den Wandunterbrechungsmodus fest. |
| `GetPageBased() -> bool \| None` | Papierbezogene Symbole behalten ihre Größe auf der gedruckten Seite statt in Welteinheiten bei. |
| `SetPageBased(value: bool) -> bool` | Schaltet *Papierbezogen* ein oder aus. Papierbezogene Symbole behalten ihre Größe auf der gedruckten Seite statt in Welteinheiten bei. |
| `GetInsertAsGroup() -> bool \| None` | `True`, wenn beim Einfügen des Symbols eine Kopie seines Inhalts statt einer Symbolinstanz platziert wird. |
| `SetInsertAsGroup(value: bool) -> bool` | Schaltet *Als Gruppe einfügen* ein oder aus. `True`, wenn beim Einfügen des Symbols eine Kopie seines Inhalts statt einer Symbolinstanz platziert wird. |

*Inhalt*

| Methode | Beschreibung |
|---|---|
| `GetGeometry() -> list[Handle]` | Die vom Symbol gezeichneten Objekte (wie bei `Resource.GetContents`). |
| `AddGeometry(hObject: Handle) -> bool` | Verschiebt ein vorhandenes Objekt in die Symboldefinition. |
| `ResetInstances() -> bool` | Zeichnet nach einer Änderung des Inhalts jede Instanz neu. |

*Instanzen*

| Methode | Beschreibung |
|---|---|
| `Insert(position: Point2D, rotationRadians: float = 0.0) -> Handle` | Erzeugt eine Symbolinstanz bei `position` auf der aktiven Ebene / im aktuellen Container; Null-Handle bei einem Fehlschlag. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

#### SymbolDefinition.GeometryType

> **Vollständiger Name:** `api.SymbolDefinition.GeometryType` · **Art:** `IntEnum`

Was das Symbol darstellen kann: nur 2D, nur 3D oder beides (ein hybrides Symbol zeigt seinen 2D-Teil in der Planansicht).

| Element | Wert | Beschreibung |
|---|---|---|
| `Unknown` | `0` |  |
| `TwoD` | `1` |  |
| `ThreeD` | `2` |  |
| `Hybrid` | `3` |  |

#### SymbolDefinition.InsertMode

> **Vollständiger Name:** `api.SymbolDefinition.InsertMode` · **Art:** `IntEnum`

Position des Symbols relativ zur Wand, in die es eingesetzt wird.

| Element | Wert | Beschreibung |
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

> **Vollständiger Name:** `api.SymbolDefinition.BreakMode` · **Art:** `IntEnum`

Wie die Wand an der Einfügestelle des Symbols ausgeschnitten wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `FullWithCaps` | `0` |  |
| `FullNoCaps` | `1` |  |
| `Half` | `2` |  |
| `None_` | `3` |  |

### WorksheetCell

> **Vollständiger Name:** `api.WorksheetCell` · **Erbt von:** `api.Object`

Eine Tabellenzelle. Zeilen und Spalten sind 1-basiert, wie die dem Benutzer angezeigten Zeilennummern und Spaltenbuchstaben; Spalte 1 ist "A".

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `WorksheetCell()` | Standardwert (Felder mit ihren Standardwerten). |
| `WorksheetCell(row, column)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `row` | `int` | Zeile (1-basiert). |
| `column` | `int` | Spalte (1-basiert). |

### WorksheetCellContent

> **Vollständiger Name:** `api.WorksheetCellContent` · **Erbt von:** `api.Object`

Eine Zelle mit ihrem Inhalt.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `WorksheetCellContent()` | Standardwert (Felder mit ihren Standardwerten). |
| `WorksheetCellContent(cell, formula, text)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `cell` | `WorksheetCell` | Die Zelle. |
| `formula` | `str` | Die der Zelle zugewiesene Eingabe; leer bei einer Zelle, die einen Literalwert enthält. |
| `text` | `str` | Was die Zelle nach der letzten Neuberechnung anzeigt. |

### Worksheet

> **Vollständiger Name:** `api.Worksheet` · **Erbt von:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Tabelle. Eine Tabelle ist Zubehör und kann auch als Tabellengrafik auf einer Ebene platziert werden.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Worksheet(h: Handle)` | Verweist auf die vorhandene Tabelle `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `FromName(name: str) -> Worksheet` *statisch* | Die Tabelle mit dem Namen `name`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `FromIndex(index: int) -> Worksheet` *statisch* | Die Tabelle mit dem internen Index `index`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `Create(name: str, rows: int = 20, columns: int = 10) -> Worksheet` *statisch* | Erstellt eine leere Tabelle; gibt die vorhandene zurück, wenn der Name bereits vergeben ist. |

*Größe*

| Methode | Beschreibung |
|---|---|
| `GetRowCount() -> int \| None` | Anzahl der Zeilen. |
| `GetColumnCount() -> int \| None` | Anzahl der Spalten. |
| `IsValidCell(cell: WorksheetCell) -> bool` | True, wenn die Zelle `cell` in der Tabelle vorhanden ist. |

*Zellen*

| Methode | Beschreibung |
|---|---|
| `GetCellFormula(cell: WorksheetCell) -> str \| None` | Formel einer Zelle; eine Zelle mit einem Literalwert gibt eine leere Zeichenfolge zurück. |
| `SetCellFormula(cell: WorksheetCell, formula: str) -> bool` | Weist einer Zelle oder jeder Zelle eines Bereichs eine Formel (zum Beispiel "=COUNT(ALL)") oder einen Literalwert zu. |
| `SetRangeFormula(topLeft: WorksheetCell, bottomRight: WorksheetCell, formula: str) -> bool` | Legt die Formel für den Bereich fest. |
| `GetCellText(cell: WorksheetCell) -> str \| None` | Text, den die Zelle aktuell anzeigt. Rufen Sie nach Änderungen an der Zeichnung zuerst Recalculate auf. |
| `GetCellValue(cell: WorksheetCell) -> float \| None` | Numerischer Wert einer Zelle; leer, wenn die Zelle keine Zahl enthält. |
| `GetCells(topLeft: WorksheetCell, bottomRight: WorksheetCell) -> list[WorksheetCellContent]` | Liest einen rechteckigen Zellenblock zeilenweise. Zellen ohne Formel und ohne Text werden übersprungen. |
| `ClearCells(topLeft: WorksheetCell, bottomRight: WorksheetCell) -> bool` | Leert die Zellen des Blocks von `topLeft` bis `bottomRight`. |

*Struktur*

| Methode | Beschreibung |
|---|---|
| `InsertRows(beforeRow: int, count: int = 1) -> bool` | Fügt `count` Zeilen vor der Zeile `beforeRow` ein. |
| `InsertColumns(beforeColumn: int, count: int = 1) -> bool` | Fügt `count` Spalten vor der Spalte `beforeColumn` ein. |
| `DeleteRows(startRow: int, count: int = 1) -> bool` | Löscht `count` Zeilen ab der Zeile `startRow`. |
| `DeleteColumns(startColumn: int, count: int = 1) -> bool` | Löscht `count` Spalten ab der Spalte `startColumn`. |
| `Recalculate() -> bool` | Wertet alle Formeln erneut aus. Führen Sie dies nach Änderungen an der Zeichnung und vor dem Lesen von Zelltext aus. |
| `CreateImage(topLeftCorner: Point2D) -> Handle` | Platziert die Tabelle auf der aktiven Ebene, damit sie in der Zeichnung sichtbar ist; gibt die Tabellengrafik zurück. |

Geerbt: alle Elemente von [`TypedResource`](#typedresource), [`Resource`](#resource).

## Aufzählungen

### ResourceType

> **Vollständiger Name:** `api.ResourceType` · **Art:** `IntEnum`

Typ eines Zubehörs. Die Werte sind die Objekttypen (dieselben Werte wie die entsprechenden ObjectType-Konstanten), sodass ein Zubehörtyp an jede API übergeben werden kann, die einen Objekttyp erwartet.

| Element | Wert | Beschreibung |
|---|---|---|
| `Unknown` | `0` | Das Objekt ist kein Zubehör. |
| `SymbolDefinition` | `16` | Wiederverwendbare Objektvorlage; wird in Form von Symbolinstanzen in die Zeichnung eingesetzt. |
| `Worksheet` | `18` | Tabelle / Bericht. |
| `BuildingMaterial` | `19` | Material einer Wand-, Boden/Decken- oder Dachschicht. |
| `ViewportStyle` | `36` |  |
| `DataVisualization` | `37` | Regelbasierte grafische Übersteuerung eines Ansichtsbereichs / einer Ebene. |
| `RecordFormat` | `47` | Datenbankdefinition (die mit Objekten verknüpfte Datenbank). |
| `Hatch` | `66` | Vektorschraffurfüllung. |
| `Folder` | `92` | Zubehörordner, der anderes Zubehör im Zubehör-Manager gruppiert. |
| `Class` | `94` | Klassendefinition (siehe ClassAttributes für ihre Attribute). |
| `LineType` | `96` | Einfache oder komplexe Linienart (gestrichelter / gemusterter Stift). |
| `Texture` | `97` | Textur. |
| `RoofStyle` | `102` |  |
| `RenderStyle` | `106` | Renderstil. |
| `SlabStyle` | `107` |  |
| `Tile` | `108` | Mosaikfüllung. |
| `TextStyle` | `109` |  |
| `RenderBackground` | `115` | Renderworks-Hintergrund. |
| `ImageFill` | `119` | Bilddefinition, die als Bildfüllung / Bildobjekt verwendet wird. |
| `Gradient` | `120` | Farbverlaufsfüllung. |
| `WallStyle` | `127` |  |

### ContentFolder

> **Vollständiger Name:** `api.ContentFolder` · **Art:** `IntEnum`

Standard-Inhaltsordner von Vectorworks für externes Zubehör (Bibliothek / Vorgaben). Die Werte sind die Vectorworks-Ordnerkennungen; übergeben Sie andere Kennungen über BuildFromFolderIndex.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` | Kein Bibliotheksordner: nur die aktuelle Zeichnung. |
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

> **Vollständiger Name:** `api.ImportConflict` · **Art:** `IntEnum`

Wie ein Namenskonflikt gelöst wird, wenn Zubehör in die aktuelle Zeichnung importiert wird und dort bereits gleichnamiges Zubehör vorhanden ist.

| Element | Wert | Beschreibung |
|---|---|---|
| `DoNotImport` | `0` | Vorhandenes Zubehör beibehalten und nichts importieren. |
| `Replace` | `1` | Vorhandenes Zubehör überschreiben. |
| `Rename` | `2` | Unter einem neuen, eindeutigen Namen importieren. |
| `AskWithUI` | `3` | Den Standarddialog von Vectorworks für Konflikte anzeigen (nur in interaktiven Sitzungen). |

### RecordFieldType

> **Vollständiger Name:** `api.RecordFieldType` · **Art:** `IntEnum`

Datentyp eines Datenbankfelds.

| Element | Wert | Beschreibung |
|---|---|---|
| `Unknown` | `0` |  |
| `Integer` | `1` |  |
| `Boolean` | `2` |  |
| `Real` | `3` |  |
| `Text` | `4` |  |
| `Dimension` | `7` | Eine Länge, angezeigt in Dokumenteinheiten. |
| `PopUp` | `8` | Text mit einer Liste vordefinierter Auswahlmöglichkeiten. |
| `Radio` | `9` |  |
| `CoordLocX` | `10` | Nur für Plug-in-Parameter. |
| `CoordLocY` | `11` | Nur für Plug-in-Parameter. |
| `StaticText` | `14` | Beschriftung, am Objekt nicht bearbeitbar. |
| `ControlPoint` | `15` |  |
| `DimStdPopUp` | `16` | Nur für Plug-in-Parameter. |
| `PrecisionPopUp` | `17` | Nur für Plug-in-Parameter. |
| `ClassPopUp` | `18` |  |
| `LayerPopUp` | `19` |  |
| `Angle` | `20` |  |
| `Area` | `21` |  |
| `Volume` | `22` |  |
| `Class` | `23` | Interner Index einer Klasse. |
| `BuildingMaterial` | `24` | Interner Index eines Materials. |
| `Fill` | `25` |  |
| `PenStyle` | `26` |  |
| `PenWeight` | `27` |  |
| `Color` | `28` |  |
| `Texture` | `29` | Interner Index einer Textur. |
| `SymbolDefinition` | `30` | Interner Index einer Symboldefinition. |

---

[Zurück zum Index](README.md) · [Nach oben](#resources--zubehör-zubehörlisten-und-typisiertes-zubehör)
