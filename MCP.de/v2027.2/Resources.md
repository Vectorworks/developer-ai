[English](../../MCP/v2027.2/Resources.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/Resources.md)

# Resources — Ressourcen und Tabellenblätter

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Werkzeuge für Ressourcen der Zeichnung und externer Inhalte (Bibliotheken, Dateien, andere Dokumente) sowie für Tabellenblätter.

## Inhaltsverzeichnis

- [Überblick](#überblick)
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

## Überblick

Dieser Ordner enthält 1 Werkzeuggruppe mit insgesamt 11 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Risikostufe | Anzahl der Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [Resources](#resources) | `resources` | Nein | mittel | 11 | Listet Ressourcen auf, importiert, erstellt, untersucht, bearbeitet und wendet sie an; liest und bearbeitet Tabellenblätter. |

## Resources

> **Gruppe:** `Resources` · **Gruppen-ID:** `resources` · **Standardmäßig aktiv:** Nein · **Risikostufe:** mittel · **Werkzeuge:** 11

**Listet Ressourcen auf, importiert, erstellt, untersucht, bearbeitet und wendet sie an; liest und bearbeitet Tabellenblätter.**

Listet Vectorworks-Ressourcen auf, untersucht, importiert und bearbeitet sie: Symbolddefinitionen, Schraffuren, Farbverläufe, Bildfüllungen, Kacheln, Linientypen, Texturen, Renderstile und Hintergründe, Datensatzformate, Tabellenblätter, Textstile, Wand-/Decken-/Dach-/Ansichtsbereichstile, Datenvisualisierungen, Baustoffe, Klassen und Ressourcenordner. Ressourcen können aus der aktuellen Zeichnung oder externen Inhalten (Vectorworks-Bibliotheken, einer Datei auf dem Datenträger oder einem anderen geöffneten Dokument) aufgelistet und in die Zeichnung importiert werden.

Beachten Sie, dass Pflanzenstile, Plankopf-Rahmenstile und Datenstempelstile keine eigenen Ressourcentypen sind: Jeder davon ist eine `symbolDefinition`, die in einem Inhaltsordner (plantStyles / plantLibraries, titleBlocks, objectStyles) gespeichert ist. Listen Sie sie daher mit resourceType `symbolDefinition` und dem entsprechenden `folder` auf und importieren Sie sie so. Das Schema von getResources führt bereits alle Namen von `resourceType` und `folder` auf; rufen Sie getResourceTypes nur auf, um den Knotentyp der einzelnen Ressourcentypen zu sehen.

IFC-Eigenschaftssätze, Standard- und benutzerdefinierte, werden über die IFC-Gruppe (listIFCPsets, getIFCPsetDefinition) verwaltet, nicht über Datensatzformate. Zuordnungen des IFC Data Manager und IFC-Exporteinstellungen sind über die Ressourcen- oder IFC-Werkzeuge nicht zugänglich; getObjectIFCData meldet nur das zugeordnete IFC-Objekt eines Objekts und welche seiner IFC-Werte aus einer Zuordnung stammen. Tabellenblätter werden mit getWorksheet und editWorksheet vollständig gelesen und bearbeitet: Zellformate, Rahmen, verbundene Zellen, Spaltenbreiten, Zeilenhöhen, Datenbankzeilen und deren Unterzeilen sowie Neuberechnung.

Jede Änderung wird als eigener benannter, rückgängig zu machender Vectorworks-Vorgang ausgeführt.

| Werkzeug | Wirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`getResourceTypes`](#getresourcetypes) | Nur lesend | niedrig | Listet die Ressourcentypen und die standardmäßigen Inhaltsordner auf. |
| [`getResources`](#getresources) | Nur lesend | niedrig | Listet Ressourcen eines Typs aus der Zeichnung, einer Bibliothek, einer Datei oder einem anderen Dokument auf. |
| [`getResource`](#getresource) | Nur lesend | niedrig | Liest eine Ressource der Zeichnung aus. |
| [`importResource`](#importresource) | Bearbeitung | mittel | Importiert eine externe Ressource in die Zeichnung. |
| [`editResource`](#editresource) | Bearbeitung | mittel | Benennt eine Ressource um, beschreibt, verschiebt, dupliziert oder löscht sie. |
| [`createResource`](#createresource) | Bearbeitung | mittel | Erstellt eine leere Ressource. |
| [`getResourceDetails`](#getresourcedetails) | Nur lesend | niedrig | Liest den Inhalt einer Ressource aus: Schraffurebenen, Farbverlaufsstopps, Linientypstriche und mehr. |
| [`setResourceDetails`](#setresourcedetails) | Bearbeitung | mittel | Ändert den Inhalt einer Ressource. |
| [`applyResource`](#applyresource) | Bearbeitung | mittel | Weist einem Objekt eine Textur, einen Stil oder eine Datenvisualisierung zu. |
| [`getWorksheet`](#getworksheet) | Nur lesend | niedrig | Liest ein Tabellenblatt aus: Größe, Zellen, Formate und Datenbankzeilen. |
| [`editWorksheet`](#editworksheet) | Bearbeitung | mittel | Ändert ein Tabellenblatt mit einer Liste von Aktionen. |

### getResourceTypes

Listet die Ressourcentypen und die standardmäßigen Inhaltsordner auf.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Listet die von dieser API unterstützten Ressourcentypen (Werte von `resourceType` mit ihrem Knotentyp) und die Namen der standardmäßigen Vectorworks-Inhaltsordner (Werte von `folder`) auf. Benötigt keine Argumente.

**Parameter**

Dieses Werkzeug benötigt keine Parameter.

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `resourceTypes` | Ressourcentypen, jeweils `{ name, type }`: `name` ist der Wert für das Argument `resourceType`, `type` die Knotentypnummer. |
| `contentFolders` | Namen der Standard-Inhaltsordner: Werte für das Argument `folder` von [getResources](#getresources). |


### getResources

Listet Ressourcen eines Typs aus der Zeichnung, einer Bibliothek, einer Datei oder einem anderen Dokument auf.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Listet Ressourcen eines einzelnen `resourceType` auf. `source` wählt ihre Quelle aus: „document“ (aktuelle Zeichnung, Standardwert), „library“ (ein mit `folder` angegebener Standard-Inhaltsordner, optional eingegrenzt durch `subFolder` und ergänzt durch `includeDocument`), „file“ (eine Vectorworks-Datei mit vollständigem nativem `filePath`) oder „openDocument“ (`openDocumentIndex`).

Jeder Eintrag enthält den Listen-`index`, `name`, `actualName`, `folder` und die Angabe, ob die Ressource `isInDocument` ist. Mit `limit` (Standardwert 200) und `offset` wird die Liste seitenweise ausgegeben: `count` ist die Gesamtzahl der Ressourcen, `returned` die Anzahl der aufgelisteten Ressourcen und `truncated` ist true, wenn weitere folgen (`nextOffset`); `countOnly` gibt nur `count` zurück. Interne IFC-Datensatzformate werden herausgefiltert, bevor Anzahlen und Limits angewendet werden.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `resourceType` | string | Ja | Art der Ressource. Pflanzenstile, Plankopfstile und Datenstempelstile sind keine eigenen Typen: Es sind „symbolDefinition“-Ressourcen in den Inhaltsordnern plantStyles / plantLibraries, titleBlocks und objectStyles. Einer von: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`. |
| `source` | string |  | Einer von: `document`, `library`, `file`, `openDocument`. |
| `folder` | string |  | Der standardmäßige Vectorworks-Inhaltsordner, aus dem bei source „library“ aufgelistet wird. Einer von: `objectLibraries`, `libraries`, `defaults`, `textures`, `gradients`, `hatches`, `imageFills`, `plantStyles`, `renderBackgrounds`, `titleBlocks`, `reports`, `sketchStyles`, `tiles`, `textStyles`, `renderStyles`, `lineTypes`, `recordFormats`, `objectStyles`, `materials`, `wallStyles`, `roofStyles`, `slabStyles`, `plantLibraries`. |
| `subFolder` | string |  | Unterordner des Inhaltsordners `folder`; schränkt die Liste ein, wenn `source` `library` ist. |
| `filePath` | string |  | Vollständiger Dateipfad. |
| `openDocumentIndex` | integer |  | Gibt an, welches geöffnete Dokument aufgelistet wird, wenn `source` `openDocument` ist. |
| `includeDocument` | boolean |  | Listet zusätzlich die Ressourcen der aktuellen Zeichnung auf, wenn `source` `library` ist. |
| `sort` | boolean |  | Sortiert die Liste (Standard `true`). Wird bei `source` `file` nicht verwendet. |
| `limit` | integer |  | Seitennavigation: die maximale Anzahl zurückzugebender Elemente (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: die Anzahl zu überspringender Elemente (Standardwert 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahlen, nicht die Elemente zurück. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `resources` | Seite der Einträge; bei `countOnly` ausgelassen. Jeder Eintrag enthält `index` (Position in der Liste), `name`, `actualName`, `folder` (nur wenn nicht leer) und `isInDocument`; `uuid` nur, wenn `isInDocument` `true` ist. |
| `resourceType` | Name des aufgelisteten Ressourcentyps. |
| `count`, `returned`, `offset`, `limit`, `truncated`, `nextOffset` | Die Seite, wie unter [Seitennavigation](Common.md#seitennavigation) beschrieben. |


### getResource

Liest eine Ressource der Zeichnung aus.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Liest eine Ressource der aktuellen Zeichnung anhand von uuid, name oder internem index aus: Typ, Name, Beschreibung, Ressourcenordner (`folder`-Name und `parentFolder`-Referenz) sowie bei Symbolddefinitionen und Ressourcenordnern die darin enthaltenen Objekte. Mit `objectUuid` werden stattdessen die von diesem Objekt verwendeten Ressourcen zurückgegeben: `styles` – der Text-, Wand-, Decken-, Dach- oder Ansichtsbereichstil, dem es folgt (leer, wenn es eigene Einstellungen verwendet) – und `activeDataVisualizations` – die auf einem Ansichtsbereich, einer gespeicherten Ansicht oder einer Konstruktionsebene aktiven Datenvisualisierungen (nur wenn vorhanden).

Interne IFC-Datensatzformate werden abgelehnt; verwenden Sie stattdessen die IFC-Werkzeuge.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `objectUuid` | string |  | UUID des Zielobjekts. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `object` | Objekt (siehe [Objektreferenzen](Common.md#objektreferenzen)). |
| `styles` | Ressourcen, denen das Objekt folgt, als Ressourcenreferenzen in dieser Reihenfolge: Textstil, Wandstil, Plattenstil, Dachstil, Ansichtsbereichsstil. Leer, wenn es keinem Stil folgt. |
| `activeDataVisualizations` | Namen der für das Objekt aktiven Datenvisualisierungen. Wird ausgelassen, wenn keine vorhanden sind. |

| Schlüssel | Beschreibung |
|---|---|
| `parentFolder` | Ressourcenordner, der die Ressource enthält, als Ressourcenreferenz. Wird auf oberster Ebene ausgelassen. |
| `contents` | Bei einer Symboldefinition oder einem Ressourcenordner: enthaltene Objekte als Objektreferenzen. |


### importResource

Importiert eine externe Ressource in die Zeichnung.

> **Wirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: importResource“ · **In runToolBatch:** ja

**Einzelheiten**

Importiert eine externe Ressource in die aktuelle Zeichnung und gibt sie zurück. Erstellen Sie die Liste wie bei getResources und wählen Sie die Ressource dann über `name` oder ihren Listen-`index` aus. `onConflict` bestimmt, was geschieht, wenn die Zeichnung bereits eine Ressource mit diesem Namen enthält: rename (umbenennen, Standardwert), replace (ersetzen), doNotImport (nicht importieren) oder askWithUI (über die Benutzeroberfläche abfragen). Das Ergebnis enthält `imported`: false, wenn die bereits in der Zeichnung vorhandene Ressource zurückgegeben wurde (sie war schon in der Zeichnung vorhanden oder doNotImport wurde bei einem Namenskonflikt gewählt).

`classRenamePrefix` stellt den Klassen, die mit der Ressource importiert werden, ein Präfix voran. Interne IFC-Datensatzformate werden abgelehnt; verwenden Sie stattdessen die IFC-Werkzeuge.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `resourceType` | string | Ja | Art der Ressource. Pflanzenstile, Plankopfstile und Datenstempelstile sind keine eigenen Typen: Es sind „symbolDefinition“-Ressourcen in den Inhaltsordnern plantStyles / plantLibraries, titleBlocks und objectStyles. Einer von: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`. |
| `source` | string |  | Einer von: `document`, `library`, `file`, `openDocument`. |
| `folder` | string |  | Der standardmäßige Vectorworks-Inhaltsordner, aus dem bei source „library“ aufgelistet wird. Einer von: `objectLibraries`, `libraries`, `defaults`, `textures`, `gradients`, `hatches`, `imageFills`, `plantStyles`, `renderBackgrounds`, `titleBlocks`, `reports`, `sketchStyles`, `tiles`, `textStyles`, `renderStyles`, `lineTypes`, `recordFormats`, `objectStyles`, `materials`, `wallStyles`, `roofStyles`, `slabStyles`, `plantLibraries`. |
| `subFolder` | string |  | Unterordner des Inhaltsordners `folder`; schränkt die Liste ein, wenn `source` `library` ist. |
| `filePath` | string |  | Vollständiger Dateipfad. |
| `openDocumentIndex` | integer |  | Gibt an, welches geöffnete Dokument aufgelistet wird, wenn `source` `openDocument` ist. |
| `includeDocument` | boolean |  | Listet zusätzlich die Ressourcen der aktuellen Zeichnung auf, wenn `source` `library` ist. |
| `sort` | boolean |  | Sortiert die Liste (Standard `true`). Wird bei `source` `file` nicht verwendet. |
| `name` | string |  | Name der zu importierenden Ressource; hat Vorrang vor `index`. |
| `index` | integer |  | Listenindex der Ressource (siehe [getResources](#getresources)); wird nur verwendet, wenn `name` fehlt. |
| `onConflict` | string |  | Einer von: `rename`, `replace`, `doNotImport`, `askWithUI`. |
| `classRenamePrefix` | string |  | Präfix für die Namen der mit der Ressource importierten Klassen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `imported` | `false`, wenn stattdessen die bereits in der Zeichnung vorhandene Ressource zurückgegeben wurde (sie war schon vorhanden oder `doNotImport` verursachte einen Namenskonflikt). |
| `note` | Nur wenn `imported` `false` ist: `the resource was already in the drawing; it was returned instead of being imported`. |


### editResource

Benennt eine Ressource um, beschreibt, verschiebt, dupliziert oder löscht sie.

> **Wirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: editResource“ · **In runToolBatch:** ja

**Einzelheiten**

Bearbeitet eine Ressource der aktuellen Zeichnung, identifiziert über uuid, name oder internen index. `action`: modify (ändern; Standardwert – mit `newName` umbenennen, `description` festlegen, in den durch `folder` bezeichneten Ressourcenordner verschieben), duplicate (duplizieren, optional mit `newName` benennen) oder delete (löschen). Interne IFC-Datensatzformate werden abgelehnt; verwenden Sie stattdessen die IFC-Werkzeuge.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `action` | string |  | Einer von: `modify`, `duplicate`, `delete`. |
| `newName` | string |  | Der neue Name. |
| `description` | string |  | Beschreibungstext. |
| `folder` | string |  | Name eines bestehenden Ressourcenordners, in den die Ressource verschoben wird (`modify`). Ein leerer Name oder ein Name ohne Objekt führt zum Fehler (`resource folder not found: <folder>`); daher kann keine Ressource in die oberste Ebene verschoben werden. Ist der Name kein Ressourcenordner, wird `applied.folder` als `false` gemeldet. |

**Ergebnis**

| Aktion | Ergebnis |
|---|---|
| `modify` (default) | `resource` (the resource reference, see [getResource](#getresource)) and `applied`: for each of `newName`, `description` and `folder` that was given, whether it was written. |
| `duplicate` | Ressourcenreferenz der Kopie. Mit `newName` erhält die Kopie diesen Namen; wenn der Name nicht gesetzt werden kann (z. B. weil er bereits vergeben ist), behält die Kopie den beim Duplizieren zugewiesenen Namen; dies wird nicht gemeldet. |
| `delete` | `deleted`: `false`, wenn nichts gelöscht wurde. Dies ist kein Fehler. |


### createResource

Erstellt eine leere Ressource.

> **Wirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: createResource“ · **In runToolBatch:** ja

**Einzelheiten**

Erstellt in der aktuellen Zeichnung eine leere Ressource des `resourceType` mit dem Namen `name`. Wenn der Name bereits vergeben ist, hängt Vectorworks bei den meisten Typen eine Zahl an; lesen Sie den zurückgegebenen Namen daher erneut aus. Text-, Wand-, Decken- und Dachstile sowie Datensatzformate geben stattdessen die vorhandene Ressource dieses Typs zurück, wobei `created`: false im Ergebnis steht; ein einzelner bereits vergebener Ordnername führt zu einem Fehler.

**Zusätzliche Argumente je Typ:** hatch – `usePageUnits`, `transparent`, `backgroundColor`; lineType – `dashPattern` (abwechselnde Linien- und Lückenlängen; erstellt einen einfachen Linientyp) zusammen mit `scaleWithLineWeight` oder kein Muster für einen komplexen Linientyp; renderBackground – `kind`; worksheet – `rows`, `columns`; folder – `contentType` (der darin enthaltene Ressourcentyp; ein Name mit „/“ erstellt verschachtelte Ordner, verwendet vorhandene Ordner des Pfads für diesen Typ an dieser Stelle wieder und schlägt fehl, wenn ein anderer Eintrag den Namen im Pfad belegt); imageFill – `pngBase64` (Bytes einer PNG-Datei, Base64-kodiert) und das erforderliche `folder` (der Ressourcenordner für Bildfüllungen, in dem das Bild abgelegt wird; wird bei Bedarf erstellt); dessen `name` darf noch nicht vergeben sein. Bei nicht aufgeführten Typen (texture, symbolDefinition, recordFormat, gradient, tile, textStyle, wallStyle, slabStyle, roofStyle) ist nur der Name erforderlich; die übrigen müssen mit importResource importiert werden. Interne IFC-Datensatzformate werden abgelehnt; verwenden Sie stattdessen die IFC-Werkzeuge.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `resourceType` | string | Ja | Art der Ressource. Pflanzenstile, Plankopfstile und Datenstempelstile sind keine eigenen Typen: Es sind „symbolDefinition“-Ressourcen in den Inhaltsordnern plantStyles / plantLibraries, titleBlocks und objectStyles. Einer von: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`. |
| `name` | string | Ja | Name der neuen Ressource. Bei einem Ordner bezeichnet ein Name mit `/` einen Pfad verschachtelter Ordner. Für einen einfachen Linientyp ignoriert. Für `imageFill`: darf von keinem anderen Objekt verwendet werden und nicht mit `folder` übereinstimmen. |
| `description` | string |  | Beschreibungstext. |
| `usePageUnits` | boolean |  | Schraffur: Gibt an, ob die Schraffur in Papiereinheiten bemessen wird (Standard `false`). |
| `transparent` | boolean |  | Schraffur: Einstellung `transparent` der Schraffur (Standard `true`). |
| `backgroundColor` | [Farbe](Common.md#farben) |  | Schraffur: Hintergrundfarbe. |
| `dashPattern` | array of number |  | Abwechselnde Linien- und Lückenlängen; erstellt einen einfachen Linientyp. |
| `scaleWithLineWeight` | boolean |  | Linientyp mit `dashPattern`: Gibt an, ob die Striche mit der Linienstärke skaliert werden. |
| `kind` | string |  | Einer von: `clouds`, `oneColor`, `twoColor`, `physicalSky`. |
| `rows` | integer |  | Tabelle: Anzahl der Zeilen (Standard 20, mindestens 1). |
| `columns` | integer |  | Tabelle: Anzahl der Spalten (Standard 10, mindestens 1). |
| `contentType` | string |  | Art der Ressource. Pflanzenstile, Plankopfstile und Datenstempelstile sind keine eigenen Typen: Es sind „symbolDefinition“-Ressourcen in den Inhaltsordnern plantStyles / plantLibraries, titleBlocks und objectStyles. Einer von: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`. |
| `pngBase64` | string |  | Bytes einer PNG-Datei, Base64-kodiert. |
| `folder` | string |  | Der Ressourcenordner für Bildfüllungen, in dem das Bild abgelegt wird; wird bei Bedarf erstellt. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `created` | `false`, wenn stattdessen die vorhandene Ressource dieses Namens zurückgegeben wurde (Stile, Datensatzformate, Tabellen). Bei einem einfachen Linientyp nicht vorhanden. |
| `note` | Nur wenn die vorhandene Ressource zurückgegeben wurde: `a <type> resource named '<name>' already exists; it was returned instead of a new one`. Bei einem einfachen Linientyp: Hinweis, dass das Ergebnis möglicherweise ein vorhandener Linientyp mit demselben Muster ist. |
| `details` | Angaben, die [getResourceDetails](#getresourcedetails) für die Ressource zurückgibt: typisierte Einstellungen. |


### getResourceDetails

Liest den Inhalt einer Ressource aus: Schraffurebenen, Farbverlaufsstopps, Linientypstriche und mehr.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Liest über den Namen hinaus aus, was eine Ressource enthält: Ebenen und Einstellungen einer Schraffur, Farbstopps eines Farbverlaufs, Abstand, Geometrieanzahl und `geometryGroup` einer Kachel, Pixelgröße einer Bildfüllung, Strichmuster eines einfachen Linientyps oder Geometrieanzahl und `geometryGroup` eines komplexen Linientyps, Art und Einfügeeinstellungen einer Symbolddefinition sowie ob sie das `active` Symbol ist, Größe einer Textur, Felder eines Datensatzformats (der `type` eines Felds ist ein Vectorworks-Datensatzfeldtyp wie text, integer oder popUp und kein IFC-Typ), Größe und Zellen eines Tabellenblatts, Inhalt eines Ressourcenordners oder die `activeDataVisualizations` eines Ansichtsbereichstils.

`geometryGroup` verweist auf die Gruppe mit den wiederholten 2D-Objekten. Für ein Tabellenblatt übergeben Sie `topLeft` und/oder `bottomRight`, um die Zellen dieses Bereichs auszulesen (Formel, angezeigter Text und bei einer Zahl der unformatierte `value`); andernfalls wird nur die Größe zurückgegeben. getWorksheet liest auch Formate, Größen, verbundene Zellen und Datenbank-Unterzeilen aus. Für eine dataVisualization werden nur die Namen aller Datenvisualisierungen im Dokument zurückgegeben (keine Kriterien oder Zuordnung); Ressourcen der Typen buildingMaterial, class, renderBackground, renderStyle, roofStyle, slabStyle, textStyle und wallStyle geben ein leeres `details` zurück.

Grafikattribute (Stift, Füllung usw.) einer Ressource, die solche Attribute besitzt, können mit getObjectAttributes / setObjectAttributes der Gruppe Objects über die Ressourcen-uuid gelesen und festgelegt werden. Interne IFC-Datensatzformate werden abgelehnt; verwenden Sie stattdessen die IFC-Werkzeuge.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `topLeft` | object |  | Tabelle: erste Zelle des zu lesenden Bereichs als `{ row, column }`. Wenn nur `bottomRight` angegeben ist, Standard Zeile 1, Spalte 1. |
| `topLeft.row` | integer |  | Zeile der Zelle (1 ist die erste Zeile). |
| `topLeft.column` | integer |  | Spalte der Zelle (1 ist die erste Spalte). |
| `bottomRight` | object |  | Tabelle: letzte Zelle des zu lesenden Bereichs als `{ row, column }`. Wenn nur `topLeft` angegeben ist, Standard letzte Zeile und Spalte. |
| `bottomRight.row` | integer |  | Zeile der Zelle (1 ist die erste Zeile). |
| `bottomRight.column` | integer |  | Spalte der Zelle (1 ist die erste Spalte). |

**Ergebnis**

| Typ | Schlüssel von `details` |
|---|---|
| `hatch` | `usePageUnits`, `transparent`, `rotateInWalls`, `rotateInSymbols`, `levels`: ein Eintrag pro Ebene mit `startPoint`, `repeatVector`, `offsetVector`, `dashFactor`, `color` und `lineWeightMils`. |
| `gradient` | `segments`: ein Eintrag pro Farbstopp mit `spotPosition`, `midpointPosition`, `color` und `opacity`. |
| `tile` | `offset`, `repetition`, `usePageUnits`, `transparentBackground`, `backgroundColor`, `rotateInWalls`, `rotateInSymbols`, `geometryCount` und `geometryGroup` (Objektreferenz, wenn die Kachel eine hat). |
| `imageFill` | `widthPixels`, `heightPixels`, `compression`. |
| `lineType` | `simple`; ein einfacher Linientyp enthält zusätzlich `dashPattern` und `scaleWithLineWeight`, ein komplexer `gapSize`, `usePageUnits`, `geometryCount` und `geometryGroup`. |
| `symbolDefinition` | `geometryType`, `canInsertIntoWalls`, `containsLight`, `pageBased`, `insertAsGroup`, `insertMode`, `breakMode`, `active`. |
| `texture` | `size`, `uvAspectRatio`. |
| `recordFormat` | `localizedName`, `parametric`, `visible`, `fields`: ein Eintrag pro Feld mit `name`, `localizedName`, `type`, `defaultValue` und bei einem `popUp`-Feld `choices`. |
| `worksheet` | `rows`, `columns`; mit `topLeft` oder `bottomRight` außerdem `cells`: Zellen des Bereichs mit Formel oder Text (leere Zellen und Zellen jenseits von `rows` bzw. `columns` werden ausgelassen; `cells` ist leer, wenn Zeile oder Spalte von `topLeft` bzw. `bottomRight` kleiner als 1 ist oder `bottomRight` oberhalb bzw. links von `topLeft` liegt). Jede Zelle enthält `row`, `column`, `formula`, `text` und bei einer Zahl `value`. |
| `folder` | `contentType` (Ressourcentyp, den der Ordner enthält) und `resources` (enthaltene Ressourcen als Ressourcenreferenzen; interne IFC-Datensatzformate werden ausgelassen). |
| `viewportStyle` | `activeDataVisualizations`. |
| `dataVisualization` | `allNames`. |
| any other type | `{}` (empty) |


### setResourceDetails

Ändert den Inhalt einer Ressource.

> **Wirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: setResourceDetails“ · **In runToolBatch:** ja

**Einzelheiten**

Ändert den Inhalt einer Ressource, identifiziert über uuid, name oder internen index.

**Je Typ:** hatch – `usePageUnits`, `transparent`, `rotateInWalls`, `rotateInSymbols`, `levels` (jeweils mit startPoint, repeatVector (Richtung der Linien und Wiederholungslänge des Strichmusters), offsetVector (Abstand zur nächsten parallelen Linie), dashFactor (gezeichneter Anteil jeder Wiederholung, 1 = durchgezogen), color, lineWeightMils; eine Ebene hinter der letzten wird angefügt), `addLevels` (Ebenen mit denselben Feldern, nach der letzten angefügt); gradient – `removeSegments` (0-basierte Indizes der zu entfernenden Stopps, vor `segments` angewendet), `segments` (spotPosition, midpointPosition, color, opacity); tile – `offset`, `repetition`, `usePageUnits`, `transparentBackground`, `backgroundColor`, `rotateInWalls`, `rotateInSymbols`, `addGeometryUuid`; lineType – `gapSize`, `usePageUnits`, `addGeometryUuid`; symbolDefinition – `pageBased`, `insertAsGroup`, `insertMode`, `breakMode`, `addGeometryUuid`, `resetInstances`, `active` (true macht das Symbol zum aktiven Symbol, von dem neue Symbolinstanzen erstellt werden); texture – `size`, `updateThumbnail`; imageFill – `compression`; recordFormat – `localizedName`, `visible`, `addFields` (name, type, defaultValue, choices), `removeFields`, `renameFields` (name, newName) oder `fieldName` mit `defaultValue` und/oder `choices` (ersetzt die Auswahlen eines popUp-Feldes); worksheet – `clearCells` (Bereich `{ topLeft, bottomRight }`, dessen Inhalte und Formatierung vor dem Festlegen von `cells` gelöscht werden), `cells` (row, column, formula; mit `bottomRight` wird die Formel auf jede Zelle von row/column bis dorthin angewendet), `insertRows`/`insertColumns`/`deleteRows`/`deleteColumns` mit `count` und `recalculate` (standardmäßig aktiviert; editWorksheet legt zusätzlich Formate, Rahmen, verbundene Zellen, Größen und Datenbankzeilen fest); folder – `addResourceUuid`. Verwenden Sie editResource, um eine Ressource umzubenennen, zu beschreiben, zu duplizieren oder zu löschen. Interne IFC-Datensatzformate werden abgelehnt; verwenden Sie stattdessen die IFC-Werkzeuge.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `usePageUnits` | boolean |  | Schraffur, Kachel und Linientyp: `true` bemisst das Muster auf der gedruckten Seite statt in Welteinheiten. |
| `transparent` | boolean |  | Schraffur: `true` lässt den Bereich hinter den Schraffurlinien transparent, statt ihn mit dem Hintergrund zu füllen. |
| `rotateInWalls` | boolean |  | Schraffur und Kachel: Gibt an, ob das Muster der Drehung der Wand folgt, in der es gezeichnet wird. |
| `rotateInSymbols` | boolean |  | Schraffur und Kachel: Gibt an, ob das Muster der Drehung des Symbols folgt, in dem es gezeichnet wird. |
| `levels` | array of object |  | Schraffur: Element `i` setzt Ebene `i` (siehe erste Anmerkung). Elemente: `startPoint`, `repeatVector`, `offsetVector` ([Punkte](Common.md#punkte)), `dashFactor` (Zahl), `color` ([Farbe](Common.md#farben)), `lineWeightMils` (Ganzzahl in mils = 1/1000 Zoll). |
| `addLevels` | array of object |  | Ebenen mit denselben Feldern, nach der letzten angefügt. |
| `segments` | array of object |  | Felder jedes Elements: `spotPosition`, `midpointPosition`, `color`, `opacity`. |
| `removeSegments` | array of integer |  | 0-basierte Indizes der zu entfernenden Stopps, vor `segments` angewendet. |
| `offset` | [Punkt](Common.md#punkte) |  | Kachel: Ursprung des Kachelrasters. |
| `repetition` | [Punkt](Common.md#punkte) |  | Kachel: Schrittweite von einer Wiederholung zur nächsten. |
| `transparentBackground` | boolean |  | Kachel: Gibt an, ob der Kachelhintergrund transparent ist. |
| `backgroundColor` | [Farbe](Common.md#farben) |  | Kachel: Hintergrundfarbe. |
| `gapSize` | number |  | Linientyp: Abstand zwischen zwei Geometriewiederholungen in Welteinheiten (bei einem Linientyp mit Papiereinheiten in Papiereinheiten). |
| `addGeometryUuid` | string |  | Kachel, Linientyp und Symboldefinition: UUID eines vorhandenen Objekts, das in die Geometrie der Ressource verschoben wird. `applied.addGeometry` ist `false`, wenn das Objekt nicht gefunden oder nicht hinzugefügt werden kann. |
| `pageBased` | boolean |  | Symboldefinition: `true` behält die Symbolgröße auf der gedruckten Seite bei statt in Welteinheiten. |
| `insertAsGroup` | boolean |  | Symboldefinition: `true` fügt eine Kopie des Symbolinhalts statt einer Symbolinstanz ein. |
| `resetInstances` | boolean |  | Symboldefinition: `true` setzt Instanzen der Definition zurück; `false` bewirkt nichts. |
| `active` | boolean |  | true macht das Symbol zum aktiven Symbol, von dem neue Symbolinstanzen erstellt werden. |
| `insertMode` | string |  | Einer von: `edge`, `center`, `leftEdge`, `rightEdge`, `coreComponentCenter`, `coreComponentLeftEdge`, `coreComponentRightEdge`, `wallInsertLocation`, `wallClosureInsertLocation`. |
| `breakMode` | string |  | Einer von: `fullWithCaps`, `fullNoCaps`, `half`, `none`. |
| `size` | number |  | Textur: reale Größe, die das Texturbild in Welteinheiten abdeckt. |
| `updateThumbnail` | boolean |  | Textur: `true` aktualisiert die Vorschau der Textur im Ressourcen-Manager; `false` bewirkt nichts. |
| `compression` | string |  | Einer von: `none`, `jpeg`, `png`, `pngMonochrome`. |
| `localizedName` | string |  | Datensatzformat: lokalisierter Name des Formats. |
| `visible` | boolean |  | Datensatzformat: `false` blendet das Format im Datenbereich der Objekt-Info-Palette aus. |
| `addFields` | array of object |  | Felder jedes Elements: `name`, `type`, `defaultValue`, `choices`. |
| `addFields[].name` | string |  | Name des neuen Felds. Das Feld wird nicht hinzugefügt (`added: false`), wenn der Name leer ist oder das Format bereits ein Feld dieses Namens enthält. |
| `addFields[].type` | string |  | Einer von: `integer`, `boolean`, `real`, `text`, `dimension`, `popUp`, `radio`, `staticText`, `controlPoint`, `classPopUp`, `layerPopUp`, `angle`, `area`, `volume`, `class`, `buildingMaterial`, `fill`, `penStyle`, `penWeight`, `color`, `texture`, `symbolDefinition`. |
| `addFields[].defaultValue` | string |  | Standardwert als Text. Felder vom Typ `text`, `popUp`, `staticText` und `classPopUp` übernehmen ihn unverändert; andere Typen lesen ihn wie einen vom Benutzer eingegebenen Vectorworks-Wert (Zahl, Flag, Name einer vorhandenen Ressource oder Farbe). Ein für den Typ ungültiger Wert lässt das Hinzufügen scheitern (`added: false`); eine leere Zeichenfolge wird immer akzeptiert. |
| `addFields[].choices` | array of string |  | Auswahlmöglichkeiten eines `popUp`-Felds; werden gesetzt, nachdem das Feld hinzugefügt wurde. |
| `removeFields` | array of string |  | Namen der zu entfernenden Felder; Einträge, die keine Zeichenfolgen sind, werden übersprungen. |
| `renameFields` | array of object |  | Felder jedes Elements: `name`, `newName`. |
| `renameFields[].name` | string |  | Aktueller Feldname. |
| `renameFields[].newName` | string |  | Neuer Name. `renamed` ist `false`, wenn das Feld nicht existiert, `newName` bereits ein Feld ist oder das Umbenennen fehlschlägt. |
| `fieldName` | string |  | Vorhandenes Feld, dessen `defaultValue` und/oder `choices` ersetzt werden. |
| `defaultValue` | string |  | Neuer Standardwert für `fieldName` als Text, konvertiert vom Feldtyp über die Datensatzformat-API (nicht durch die strengere Auswertung von `addFields[].defaultValue`). `applied.defaultValue` ist `true`, sobald das Feld vorhanden ist, selbst wenn der Text nicht konvertiert werden kann und der Standardwert unverändert bleibt. |
| `choices` | array of string |  | Ersetzt die Auswahlen eines popUp-Feldes. |
| `clearCells` | object |  | Bereich `{ topLeft, bottomRight }`, dessen Inhalte und Formatierung vor dem Festlegen von `cells` gelöscht werden. |
| `clearCells.topLeft` | object |  | Erste Zelle des Bereichs; ohne Angabe Zeile 1, Spalte 1. |
| `clearCells.topLeft.row` | integer |  | Zeile, 1-basiert (ohne Angabe 1). |
| `clearCells.topLeft.column` | integer |  | Spalte, 1-basiert (ohne Angabe 1). |
| `clearCells.bottomRight` | object |  | Letzte Zelle des Bereichs; ohne Angabe die erste Zelle. |
| `clearCells.bottomRight.row` | integer |  | Zeile, 1-basiert (ohne Angabe die Zeile von `topLeft`). |
| `clearCells.bottomRight.column` | integer |  | Spalte, 1-basiert (ohne Angabe die Spalte von `topLeft`). |
| `cells` | array of object |  | Zeile, Spalte, Formel; mit `bottomRight` wird die Formel auf jede Zelle von row/column bis dorthin angewendet. |
| `cells[].row` | integer |  | Zeile, 1-basiert (ohne Angabe 1). |
| `cells[].column` | integer |  | Spalte, 1-basiert (ohne Angabe 1). |
| `cells[].formula` | string |  | Formel für diese Zelle oder für jede Zelle des Bereichs, wenn `bottomRight` angegeben ist. |
| `cells[].bottomRight` | object |  | Letzte Zelle des Bereichs; ohne Angabe die Zelle selbst. |
| `cells[].bottomRight.row` | integer |  | Zeile, 1-basiert (ohne Angabe die Zeile der Zelle). |
| `cells[].bottomRight.column` | integer |  | Spalte, 1-basiert (ohne Angabe die Spalte der Zelle). |
| `insertRows` | integer |  | Tabelle: Zeile, vor der `count` Zeilen eingefügt werden. |
| `insertColumns` | integer |  | Tabelle: Spalte, vor der `count` Spalten eingefügt werden. |
| `deleteRows` | integer |  | Tabelle: erste der `count` zu löschenden Zeilen. |
| `deleteColumns` | integer |  | Tabelle: erste der `count` zu löschenden Spalten. |
| `count` | integer |  | Anzahl der Zeilen oder Spalten für `insertRows`, `insertColumns`, `deleteRows` und `deleteColumns` (Standard 1). Bei jedem der Felder ist `applied` `false`, wenn Zeile bzw. Spalte oder `count` nicht größer als 0 ist. |
| `recalculate` | boolean |  | Berechnet das Tabellenblatt nach der Änderung neu; standardmäßig aktiviert. |
| `addResourceUuid` | string |  | Ordner: UUID einer vorhandenen Ressource, die in den Ordner verschoben wird (`applied.addResource`). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Angaben, was für jedes angegebene Argument geschrieben wurde (siehe Tabelle unten). |
| `details` | Angaben zur Ressource nach der Änderung, mit den Schlüsseln, die [getResourceDetails](#getresourcedetails) für ihren Typ zurückgibt. |

| Argument | Eintrag in `applied` |
|---|---|
| `usePageUnits`, `transparent`, `rotateInWalls`, `rotateInSymbols`, `offset`, `repetition`, `transparentBackground`, `backgroundColor`, `gapSize`, `pageBased`, `insertAsGroup`, `insertMode`, `breakMode`, `size`, `compression`, `localizedName`, `visible` | A boolean: true when the value was written. `insertMode` and `breakMode` are false for a name that is not in the list. |
| `levels`, `addLevels`, `segments` | An array with a boolean per item, in order. |
| `removeSegments` | Array aus `{ index, removed }`. Die Indizes werden vom höchsten zum niedrigsten verarbeitet. |
| `addGeometryUuid`, `addResourceUuid` | A boolean. |
| `resetInstances`, `active`, `updateThumbnail` | A boolean, present only when the argument is `true`. |
| `addFields` | Array aus `{ name, added }`. |
| `removeFields` | Array aus `{ name, removed }`. |
| `renameFields` | Array aus `{ name, newName, renamed }`. |
| `defaultValue`, `choices` | A boolean, for the field `fieldName`. |
| `insertRows`, `insertColumns`, `deleteRows`, `deleteColumns`, `clearCells` | A boolean. |
| `cells` | Array aus `{ row, column, set }`, ein Eintrag je Element. |
| `recalculate` | Boolean; wird ausgelassen, sofern `recalculate` nicht `false` ist. |


### applyResource

Weist einem Objekt eine Textur, einen Stil oder eine Datenvisualisierung zu.

> **Wirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: applyResource“ · **In runToolBatch:** ja

**Einzelheiten**

Weist dem über `objectUuid` angegebenen Objekt eine Ressource der aktuellen Zeichnung (angegeben über `resourceUuid` oder `resourceName`) zu: eine Textur (optional für einen einzelnen `part` des Objekts), einen Textstil, einen Wandstil (wobei `selectedOffset` und `replacingOffset` bestimmen, welche Linie an ihrer Position bleibt), einen Decken-, Dach- oder Ansichtsbereichstil oder eine Datenvisualisierung (`activate` deaktiviert sie bei false; `excludeObject` schließt das Objekt bei true aus allen Datenvisualisierungen aus oder lässt es bei false wieder zu).

Eine Symbolddefinition wird stattdessen instanziiert: Sie wird bei `position` mit `rotation` im Bogenmaß in die Zeichnung eingesetzt. Ein Tabellenblatt wird auf der aktiven Konstruktionsebene als Tabellenblattbild platziert, dessen obere linke Ecke bei `position` liegt; wenn es bereits platziert ist, wird stattdessen sein Bild dorthin verschoben (`moved` ist true). Für keines der beiden wird `objectUuid` benötigt. Interne IFC-Datensatzformate werden abgelehnt; verwenden Sie stattdessen die IFC-Werkzeuge.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `resourceUuid` | string |  | UUID der anzuwendenden Ressource. Hat Vorrang vor `resourceName`. |
| `resourceName` | string |  | Name der Ressource. Wird nur verwendet, wenn `resourceUuid` fehlt; eine leere oder unbekannte UUID führt zu `resource not found`. |
| `objectUuid` | string |  | UUID des Zielobjekts. |
| `part` | string |  | Einer von: `overall`, `extrudeTop`, `extrudeBottom`, `extrudeSides`, `wallLeft`, `wallRight`, `wallTop`, `wallBottom`, `slabTop`, `slabBottom`, `slabSides`, `roofTop`, `roofBottom`, `roofSides`. |
| `selectedOffset` | number |  | Wandstil: legt zusammen mit `replacingOffset` fest, welche Wandlinie an Ort und Stelle bleibt (Standard 0). |
| `replacingOffset` | number |  | Wandstil: legt zusammen mit `selectedOffset` fest, welche Wandlinie an Ort und Stelle bleibt (Standard 0). |
| `activate` | boolean |  | Datenvisualisierung: `false` deaktiviert die Datenvisualisierung für das Objekt (Standard `true`). Wird ignoriert, wenn `excludeObject` angegeben ist. |
| `excludeObject` | boolean |  | Datenvisualisierung: `true` nimmt das Objekt aus allen Datenvisualisierungen heraus, `false` schließt es wieder ein. |
| `position` | [Punkt](Common.md#punkte) |  | Einfügepunkt. |
| `rotation` | number |  | Symboldefinition: Drehung der Instanz in Radiant (Standard 0). |

**Ergebnis**

| Ressource | `object` und die weiteren Schlüssel |
|---|---|
| Symbol definition | `object` is the new symbol instance. There are no other keys. |
| Worksheet | `object` is the worksheet image. `moved` is `true` when the worksheet was already placed and its image was moved, and `false` when a new image was created. |
| Any other resource | `object` is the target object. `applied` is `true`. |


### getWorksheet

Liest ein Tabellenblatt aus: Größe, Zellen, Formate und Datenbankzeilen.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Liest eine Tabellenblattressource detailliert aus: ihre Größe (`rows`, `columns`), `autoRecalculate`, das auf einer Konstruktionsebene platzierte Tabellenblatt-`image` (falls vorhanden) und die Zellen eines Bereichs. Zellen haben `{ row, column }`-Koordinaten mit 1 als Startwert (Spalte 1 ist A); der Bereich geht von `topLeft` bis `bottomRight` (Standardwert: gesamtes Tabellenblatt). Jede Zelle enthält ihre `formula` (Definition: ein Literal oder eine mit „=“ beginnende Formel), den angezeigten `text` und bei Zahlen den `value`; Texte und Werte stammen von der letzten Neuberechnung (editWorksheet berechnet neu).

Eine Zelle, deren Formel auf eine Neuberechnung wartet, hat `needsRecalculation`: true statt `value`, da das Auslesen des Werts Vectorworks dazu veranlassen würde, das Tabellenblatt neu zu berechnen. Zellen ohne Formel oder Text werden ausgelassen, sofern `includeEmpty` nicht true ist. `include` ergänzt „formats“ (`numberFormat`, `textFormat`, `fill`, `borders` pro Zelle sowie bei einer verbundenen Zelle `merged` mit ihrem Bereich; die Schlüssel entsprechen denen von editWorksheet, wobei bei einer Schrift ohne Namen `fontIndex` statt `font` verwendet wird), „sizes“ (`columnWidths` und `rowHeights` des Bereichs in Tabellenblattpixeln) und „database“ (`databaseRows`: Datenbankzeilen des Bereichs samt `criteria` und `subrowCount`).

`subrowsOf` (die Zeile einer Datenbankzeile) listet die `subrows` dieser Zeile anstelle der Zellen auf: eine pro Objekt, das den Kriterien entspricht, jeweils mit `text` und `value` der Spalten des Bereichs. `limit` (Standardwert 200 Zellen oder 100 Unterzeilen), `offset` und `countOnly` blättern durch Zellen oder Unterzeilen. Übergeben Sie `uuid`, `name` oder `index` des Tabellenblatts oder die `uuid` eines auf einer Konstruktionsebene platzierten Tabellenblatts. createResource erstellt ein Tabellenblatt, applyResource platziert es auf einer Konstruktionsebene und getResourceDetails / setResourceDetails lesen und setzen auch einfache Zellen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `topLeft` | object |  | Erste Zelle des Bereichs als `{ row, column }`; beide Werte erforderlich. Ohne Angabe Zeile 1, Spalte 1. |
| `topLeft.row` | integer |  | Zeile, 1-basiert. |
| `topLeft.column` | integer |  | Spalte, 1-basiert (Spalte 1 ist A). |
| `bottomRight` | object |  | Letzte Zelle des Bereichs als `{ row, column }`; beide Werte erforderlich. Ohne Angabe die letzte Zelle der Tabelle. Darf nicht oberhalb oder links von `topLeft` liegen. |
| `bottomRight.row` | integer |  | Zeile, 1-basiert. |
| `bottomRight.column` | integer |  | Spalte, 1-basiert. |
| `include` | array of string |  | Jedes Element ist eines von: `formats`, `sizes`, `database`. |
| `includeEmpty` | boolean |  | `true` listet auch Zellen ohne Formel und Text auf. Nicht zulässig zusammen mit `subrowsOf`. |
| `subrowsOf` | integer |  | Die Zeile einer Datenbankzeile. |
| `limit` | integer |  | Seitennavigation: die maximale Anzahl zurückzugebender Elemente (mindestens 1). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: die Anzahl zu überspringender Elemente (Standardwert 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahlen, nicht die Elemente zurück. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `worksheet` | Ressourcenreferenz des Tabellenblatts (siehe [getResource](#getresource)). |
| `rows`, `columns` | The size of the worksheet. |
| `autoRecalculate` | Gibt an, ob das Tabellenblatt automatisch neu berechnet wird. |
| `image` | Objektreferenz des Tabellenblattbilds. Nur vorhanden, wenn das Tabellenblatt auf einer Ebene liegt. |
| `topLeft`, `bottomRight` | The range, each `{ row, column }`. |

| Schlüssel | Beschreibung |
|---|---|
| `columnWidths` | Mit `sizes`: `{ column, width }` für jede Spalte des Bereichs mit angegebener Breite, in Tabellenblatt-Pixeln. |
| `rowHeights` | Mit `sizes`: `{ row, height, locked }` für jede Zeile des Bereichs mit angegebener Höhe, in Tabellenblatt-Pixeln. |
| `databaseRows` | Mit `database`: `{ row, criteria, subrowCount }` für jede Datenbankzeile im Bereich. |


### editWorksheet

Ändert ein Tabellenblatt mit einer Liste von Aktionen.

> **Wirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: editWorksheet“ · **In runToolBatch:** ja

**Einzelheiten**

Ändert eine Tabellenblattressource mit einer Liste von `actions` (1 bis 100), die der Reihe nach als ein rückgängig zu machender Schritt angewendet werden: Schlägt eine Aktion fehl, schlägt der Aufruf fehl und das Tabellenblatt bleibt unverändert. Zellen haben `{ row, column }`-Koordinaten mit 1 als Startwert (Spalte 1 ist A); ein Bereich besteht aus `topLeft` und einem optionalen `bottomRight` (Standardwert: `topLeft`). Jede Aktion ist ein Objekt mit `action` und den zugehörigen Argumenten: setFormula (Bereich, `formula`: ein Literal oder eine mit „=“ beginnende Formel wie =SUM(A1..A3), die für jede Zelle des Bereichs gilt); clear (Bereich: Inhalte und Formate); insertRows / insertColumns (`before`, `count`, Standardwert 1); deleteRows / deleteColumns (`start`, `count`, Standardwert 1; ein Tabellenblatt behält mindestens eine Zeile und eine Spalte); setNumberFormat (Bereich, `numberStyle`, `accuracy`, `leader`, `trailer`); setTextFormat (Bereich, `font` (Schriftname), `size` (Punkt), `bold`, `italic`, `underline`, `outline`, `shadow`, `alignment`, `verticalAlignment`, `angle` (ganze Grad), `color`, `wrap`); setFill (Bereich, `fillStyle`, `background`, `foreground`, `pattern`; „solid“ benötigt `background`, „pattern“ benötigt `pattern`, `foreground` und `background`); diese drei Aktionen ändern nur die angegebenen Felder, Zelle für Zelle, höchstens 10000 Zellen pro Aktion (setTextFormat lässt Zellen aus, die durch eine Verbindung ausgeblendet sind und keine eigene Schrift haben; für andere Zellen ohne Schrift, etwa nach dem Aufheben einer Verbindung, ist `font` erforderlich); setBorders (Bereich, `top`, `left`, `bottom`, `right`, `outline`, `insideHorizontal`, `insideVertical`: zeichnet diese Rahmen; Rahmen können nicht entfernt werden, da ein false-Wert einen Rahmen unverändert lässt); merge (ein Bereich aus mindestens zwei Zellen) / unmerge (Bereich); setColumnWidth (`column`, `lastColumn`, `width`) und setRowHeight (`row`, `lastRow`, `height`, `lockHeight` (Standardwert true), `includeSubrows`) in Tabellenblattpixeln; autoFitRowHeights (`row`, `lastRow`); setDatabaseCriteria (`row`, `criteria` wie =DATABASE((T=RECT)), wodurch die Zeile zu einer Datenbankzeile mit einer Unterzeile pro gefundenem Objekt wird; leere `criteria` machen sie wieder zu einer normalen Zeile); recalculate; setAutoRecalculate (`enabled`).

`recalculate` (Standardwert true) berechnet das Tabellenblatt nach den Aktionen neu; bei einer Neuberechnung werden auch die Skripte von RUNSCRIPT-Formeln ausgeführt. Das Ergebnis enthält die neuen `rows` und `columns` sowie einen `applied`-Eintrag pro Aktion; lesen Sie die Zellen mit getWorksheet erneut aus.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `actions` | array of object | Ja | 1 bis 100 Elemente. |
| `actions[].action` | string | Ja | Einer von: `setFormula`, `clear`, `insertRows`, `insertColumns`, `deleteRows`, `deleteColumns`, `setNumberFormat`, `setTextFormat`, `setFill`, `setBorders`, `merge`, `unmerge`, `setColumnWidth`, `setRowHeight`, `autoFitRowHeights`, `setDatabaseCriteria`, `recalculate`, `setAutoRecalculate`. |
| `actions[].topLeft` | object |  | Erste Zelle des Bereichs als `{ row, column }`; beide Werte erforderlich. Wird benötigt von `setFormula`, `clear`, `setNumberFormat`, `setTextFormat`, `setFill`, `setBorders`, `merge` und `unmerge`. |
| `actions[].topLeft.row` | integer |  | Zeile, 1-basiert. |
| `actions[].topLeft.column` | integer |  | Spalte, 1-basiert (Spalte 1 ist A). |
| `actions[].bottomRight` | object |  | Letzte Zelle des Bereichs als `{ row, column }`. Ohne Angabe umfasst der Bereich nur die Zelle `topLeft`. Darf nicht oberhalb oder links von `topLeft` liegen. |
| `actions[].bottomRight.row` | integer |  | Zeile, 1-basiert. |
| `actions[].bottomRight.column` | integer |  | Spalte, 1-basiert. |
| `actions[].formula` | string |  | `setFormula`: erforderlich. Literalwert oder Formel mit vorangestelltem `=`, z. B. `=SUM(A1..A3)`; wird auf jede Zelle des Bereichs angewendet. |
| `actions[].before` | integer |  | `insertRows` und `insertColumns`: erforderlich. Zeile bzw. Spalte, vor der die neuen Zeilen oder Spalten eingefügt werden; 1 bis Anzahl der Zeilen bzw. Spalten plus 1. |
| `actions[].start` | integer |  | `deleteRows` und `deleteColumns`: erforderlich. Erste zu löschende Zeile bzw. Spalte; 1 bis Anzahl der Zeilen bzw. Spalten. |
| `actions[].count` | integer |  | `insertRows` und `insertColumns`: Anzahl der einzufügenden Zeilen oder Spalten, 1 bis 32767 (Standard 1). `deleteRows` und `deleteColumns`: Anzahl der ab `start` zu löschenden Elemente (Standard 1); das Tabellenblatt behält mindestens eine Zeile und eine Spalte. |
| `actions[].numberStyle` | string |  | Einer von: `general`, `decimal`, `decimalWithCommas`, `scientific`, `fractional`, `dimension`, `angle`, `date`, `conditional`, `generalFraction`, `dimensionWithDivider`, `area`, `volume`, `text`, `percentage`. |
| `actions[].accuracy` | integer |  | `setNumberFormat`: Genauigkeit des Zahlenformats, 0 bis 127. Die Bedeutung hängt vom Zahlenstil ab und entspricht nicht immer der Anzahl der Dezimalstellen. |
| `actions[].leader` | string |  | `setNumberFormat`: Präfix des Zahlenformats. |
| `actions[].trailer` | string |  | `setNumberFormat`: Suffix des Zahlenformats. |
| `actions[].font` | string |  | `setTextFormat`: Name einer Vectorworks bekannten Schriftart. Erforderlich für eine Zelle ohne eigene Schriftart, z. B. nach erneutem Aufteilen einer zusammengeführten Zelle. |
| `actions[].size` | integer |  | `setTextFormat`: Schriftgröße in Punkten, 1 bis 32767. |
| `actions[].bold` | boolean |  | `setTextFormat`: `true` aktiviert Fettdruck, `false` entfernt ihn. Ohne Angabe unverändert. |
| `actions[].italic` | boolean |  | `setTextFormat`: `true` aktiviert Kursivschrift, `false` entfernt sie. Ohne Angabe unverändert. |
| `actions[].underline` | boolean |  | `setTextFormat`: `true` aktiviert Unterstreichung, `false` entfernt sie. Ohne Angabe unverändert. |
| `actions[].outline` | boolean |  | `setTextFormat`: `true` aktiviert den Umriss-Textstil, `false` entfernt ihn; ohne Angabe unverändert. `setBorders`: `true` zeichnet den Außenrahmen des Bereichs (Standard `false`). |
| `actions[].shadow` | boolean |  | `setTextFormat`: `true` aktiviert den Schatten-Textstil, `false` entfernt ihn. Ohne Angabe unverändert. |
| `actions[].alignment` | string |  | Einer von: `general`, `left`, `center`, `right`. |
| `actions[].verticalAlignment` | string |  | Einer von: `general`, `top`, `center`, `bottom`. |
| `actions[].angle` | integer |  | `setTextFormat`: Textwinkel in ganzen Grad, -360 bis 360. |
| `actions[].color` | [Farbe](Common.md#farben) |  | `setTextFormat`: Textfarbe. Wird in die nächstgelegene Farbe der Dokumentpalette konvertiert; `getWorksheet` gibt diese Farbe zurück. |
| `actions[].wrap` | boolean |  | `setTextFormat`: Gibt an, ob der Text in der Zelle umgebrochen wird. |
| `actions[].fillStyle` | string |  | Einer von: `none`, `solid`, `pattern`. |
| `actions[].background` | [Farbe](Common.md#farben) |  | `setFill`: Hintergrundfarbe. Für `fillStyle` `solid` und `pattern` erforderlich. Wird in die nächstgelegene Farbe der Dokumentpalette konvertiert. |
| `actions[].foreground` | [Farbe](Common.md#farben) |  | `setFill`: Vordergrundfarbe des Musters. Für `fillStyle` `pattern` erforderlich. Wird in die nächstgelegene Farbe der Dokumentpalette konvertiert. |
| `actions[].pattern` | integer |  | `setFill`: Füllmuster, 0 bis 32767. Für `fillStyle` `pattern` erforderlich. |
| `actions[].top` | boolean |  | `setBorders`: `true` zeichnet die obere Kante des Bereichs (Standard `false`). |
| `actions[].left` | boolean |  | `setBorders`: `true` zeichnet die linke Kante des Bereichs (Standard `false`). |
| `actions[].bottom` | boolean |  | `setBorders`: `true` zeichnet die untere Kante des Bereichs (Standard `false`). |
| `actions[].right` | boolean |  | `setBorders`: `true` zeichnet die rechte Kante des Bereichs (Standard `false`). |
| `actions[].insideHorizontal` | boolean |  | `setBorders`: `true` zeichnet die horizontalen Linien zwischen den Zeilen des Bereichs (Standard `false`). |
| `actions[].insideVertical` | boolean |  | `setBorders`: `true` zeichnet die vertikalen Linien zwischen den Spalten des Bereichs (Standard `false`). |
| `actions[].column` | integer |  | `setColumnWidth`: erforderlich. Erste anzupassende Spalte, 1 bis Anzahl der Spalten. |
| `actions[].lastColumn` | integer |  | `setColumnWidth`: letzte anzupassende Spalte, von `column` bis zur Anzahl der Spalten (Standard `column`). |
| `actions[].width` | integer |  | `setColumnWidth`: erforderlich. Breite in Tabellenblatt-Pixeln, 1 bis 32767. |
| `actions[].row` | integer |  | `setRowHeight` und `autoFitRowHeights`: erforderlich. Erste zu ändernde Zeile, 1 bis Anzahl der Zeilen. `setDatabaseCriteria`: erforderlich. Zeile, der die Kriterien zugewiesen werden, 1 bis Anzahl der Zeilen. |
| `actions[].lastRow` | integer |  | `setRowHeight` und `autoFitRowHeights`: letzte zu ändernde Zeile, von `row` bis zur Anzahl der Zeilen (Standard `row`). |
| `actions[].height` | integer |  | `setRowHeight`: erforderlich. Höhe in Tabellenblatt-Pixeln, 1 bis 32767. |
| `actions[].lockHeight` | boolean |  | `setRowHeight`: Gibt an, ob die neue Höhe gesperrt ist (Standard `true`). `getWorksheet` meldet dies als `locked`. |
| `actions[].includeSubrows` | boolean |  | `setRowHeight`: `true` passt auch die Unterzeilen von Datenbankzeilen im Bereich an (Standard `false`). |
| `actions[].criteria` | string |  | `setDatabaseCriteria`: erforderlich. Datenbankdefinition, z. B. `=DATABASE((T=RECT))`. Eine leere Zeichenfolge macht die Zeile zu einer normalen Zeile. |
| `actions[].enabled` | boolean |  | `setAutoRecalculate`: erforderlich. `true` aktiviert die automatische Neuberechnung des Tabellenblatts, `false` deaktiviert sie. |
| `recalculate` | boolean |  | `true` (Standard) berechnet die Tabelle nach den Aktionen neu; `false` überspringt dies. Die Aktion `recalculate` berechnet sie innerhalb der Aktionsliste neu. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `worksheet` | Ressourcenreferenz des Tabellenblatts (siehe [getResource](#getresource)). |
| `rows`, `columns` | The size of the worksheet after the actions. |
| `applied` | Ein Eintrag pro Aktion in der Reihenfolge von `actions`. Jeder enthält `action` (Aktionsname) und die in der folgenden Tabelle aufgeführten Schlüssel. |
| `recalculated` | `true`, wenn das Tabellenblatt nach den Aktionen neu berechnet wurde; `false`, wenn `recalculate` `false` ist oder die Neuberechnung fehlgeschlagen ist. |

| Aktion | Schlüssel |
|---|---|
| `setFormula`, `clear`, `setBorders`, `merge`, `unmerge` | `topLeft` and `bottomRight`: the range, each `{ row, column }`. |
| `setNumberFormat`, `setTextFormat`, `setFill` | `cells`: the number of cells in the range; `topLeft` and `bottomRight`. |
| `insertRows`, `deleteRows` | `rows`: the number of rows after the action. |
| `insertColumns`, `deleteColumns` | `columns`: the number of columns after the action. |
| `setDatabaseCriteria` | `row` und `isDatabaseRow`: Gibt an, ob die Zeile nun eine Datenbankzeile ist. |
| `setAutoRecalculate` | `enabled`. |
| `setColumnWidth`, `setRowHeight`, `autoFitRowHeights`, `recalculate` | None. |
