[English](../../MCP/v2027.2/DocumentAccess.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/DocumentAccess.md)

# DocumentAccess — Dokument und Auswahl

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Inhaltsverzeichnis](README.md)

Werkzeuge für die aktive Zeichnung insgesamt und die aktuelle Auswahl: die Dokumentübersicht, Konstruktionsebenen, Geschosse, Klassen, Einheiten, die Ansicht und die Dokumenteinstellungen sowie Massenbearbeitungen der ausgewählten Objekte.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Document](#document)
  - [getDocumentInfo](#getdocumentinfo)
  - [getLayers](#getlayers)
  - [createLayer](#createlayer)
  - [editLayer](#editlayer)
  - [getStories](#getstories)
  - [createStory](#createstory)
  - [editStory](#editstory)
  - [getClasses](#getclasses)
  - [createClass](#createclass)
  - [editClass](#editclass)
  - [setActiveContext](#setactivecontext)
  - [getUnits](#getunits)
  - [setUnits](#setunits)
  - [convertUnits](#convertunits)
  - [setView](#setview)
  - [getPreferences](#getpreferences)
  - [setPreferences](#setpreferences)
- [Selection](#selection)
  - [getSelection](#getselection)
  - [selectObjects](#selectobjects)
  - [editSelection](#editselection)

## Überblick

Dieser Ordner enthält 2 Werkzeuggruppen mit insgesamt 20 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Risikostufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [Document](#document) | `document` | Ja | low | 17 | Die aktive Zeichnung: Dokumentübersicht, Konstruktionsebenen, Geschosse, Klassen, Einheiten, Ansicht und Dokumenteinstellungen. |
| [Selection](#selection) | `selection` | Ja | medium | 3 | Aktuelle Auswahl auflisten und Objekte gemeinsam verschieben, drehen, skalieren, duplizieren, gruppieren, löschen oder neu klassifizieren. |

## Document

> **Gruppe:** `Document` · **Gruppen-ID:** `document` · **Standardmäßig aktiv:** Ja · **Risikostufe:** low · **Werkzeuge:** 17

**Die aktive Zeichnung: Dokumentübersicht, Konstruktionsebenen, Geschosse, Klassen, Einheiten, Ansicht und Dokumenteinstellungen.**

Untersuchen und verwalten Sie die aktive Vectorworks-Zeichnung selbst: Dokumentübersicht, Konstruktionsebenen, Geschosse, Klassen, Einheiten, Ansicht und Dokumenteinstellungen. Lesen Sie getDocumentInfo, getLayers und getClasses, wenn die Aufgabe von den Konstruktionsebenen, Klassen, Einheiten oder dem aktiven Kontext der Zeichnung abhängt. Die Ergebnisse werden live ausgelesen und bleiben gültig, bis sich die Zeichnung ändert – durch Ihre Bearbeitungen oder die des Benutzers; die Auswahl und die aktive Konstruktionsebene ändern sich häufig.

Aufbau einer Vectorworks-Zeichnung:

- Ein Dokument ist eine Zeichnungsdatei. Alles befindet sich entweder auf einer Ebene (dem Zeichnungsinhalt) oder in der Ressourcenliste des Dokuments (wiederverwendbare Definitionen – siehe Gruppe Resources).
- EBENEN sind die Container aller Geometrie. Eine KONSTRUKTIONSEBENE enthält Modellinhalte in realen Maßen: Ihre Koordinaten sind Welteinheiten, und ihr Maßstab (1:scale) bestimmt nur, wie groß die seitengestützten Grafiken, Texte und Linienstärken gedruckt werden. Eine LAYOUTEBENE ist eine druckbare Seite; sie enthält Ansichtsbereiche (beschnittene, maßstäbliche Ansichten von Konstruktionsebenen), Planköpfe und Seitenanmerkungen. Es ist immer genau eine Ebene aktiv, auf der neue Objekte erstellt werden.
- GESCHOSSE sind die Stockwerke eines Gebäudes (BIM): Jedes hat eine Höhe und Ebenen, also benannte Höhen (Ebenentypen wie `OK-FB`) mit einem Versatz zur Geschosshöhe. Eine Ebene kann eine eigene Konstruktionsebene haben, deren Höhe dann der Ebene folgt; Wände verknüpfen ihre obere und untere Begrenzung mit Ebenen. Reihenfolge des BIM-Arbeitsablaufs: Geschosse (getStories, createStory, editStory) → Stile (Gruppe Resources) → Bauteile (Gruppe Architecture) auf den Geschossebenen.
- KLASSEN sind benannte, gespeicherte Attributsätze (Stift, Füllung, Linienstärke, Deckkraft, Marker, Schlagschatten, Textur, Textstil), die ebenenübergreifend gelten. Jedes Objekt gehört genau einer Klasse an. Ein Attributsatz „nach Klasse“ folgt auf einem Objekt seiner Klasse; daher wirken sich Änderungen am Klassenstil auf jedes Objekt aus, das diesen übernimmt. Klassen steuern auch die Sichtbarkeit: Ein Objekt wird nur angezeigt, wenn sowohl seine Ebene als auch seine Klasse sichtbar ist. Die Klasse `None` ist immer vorhanden.
- OBJEKTE sind die Geometrie: 2D-Grundformen, parametrische Plug-in-Objekte (Wände, Türen, Pflanzen, Datenstempel, ...), Gruppen, Symbolinstanzen und Ansichtsbereiche. Jedes Objekt hat eine stabile uuid, eine Klasse, grafische Attribute und – bei Plug-in-Objekten – einen Parameterdatensatz. Container (Gruppen, Symboldefinitionen, Ansichtsbereichsanmerkungen) enthalten verschachtelte Objekte; neue Objekte werden in dem Container erstellt, der gerade bearbeitet wird. getDocumentInfo gibt diesen als `container` an.
- RESSOURCEN sind die wiederverwendbaren Definitionen im Dokument: Symboldefinitionen, Schraffuren, Farbverläufe, Kacheln, Bildfüllungen, Linientypen, Texturen, Datensatzformate, Tabellen, Textstile und Objektstile (Plug-in-Stile). Objekte verweisen auf sie; ein Plug-in-Objekt, das von einem Objektstil gesteuert wird, übernimmt daraus seine Parameter.
- KOORDINATEN sind Welteinheiten (die interne Längeneinheit der API); in der Benutzeroberfläche werden sie in die Dokumenteinheiten umgerechnet (verwenden Sie convertUnits). Der BENUTZERNULLPUNKT ist der Weltpunkt, den der Benutzer als (0,0) sieht. Winkel werden im Bogenmaß gegen den Uhrzeigersinn ab der X-Achse angegeben.
- RÜCKGÄNGIG: Jeder Aufruf, der die Zeichnung ändert, ist EIN Rückgängig-Schritt „MCP: &lt;tool&gt;“, den der Benutzer rückgängig machen kann (Vectorworks zeigt den Namen nach Bearbeiten &gt; Rückgängig in der Statusmeldung an). Ein fehlgeschlagener Aufruf ändert nichts (`rolledBack` im Ergebnis). Um eine Aufgabe auf Benutzerebene mit einem Rückgängig-Schritt auszuführen, erledigen Sie sie in einem einzigen runPythonScript-Aufruf (Gruppe Scripting).

| Werkzeug | Auswirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`getDocumentInfo`](#getdocumentinfo) | Nur lesend | low | Gibt eine Übersicht des aktiven Dokuments zurück: Datei, Anzahlen, Seitengrenzen, Ansichtsmitte und Benutzernullpunkt. |
| [`getLayers`](#getlayers) | Nur lesend | low | Listet die Ebenen mit Typ, Sichtbarkeit, Maßstab, Höhe, Objektanzahl und Begrenzungen auf. |
| [`createLayer`](#createlayer) | Bearbeiten | low | Erstellt eine Konstruktionsebene oder Layoutebene. |
| [`editLayer`](#editlayer) | Bearbeiten | low | Ändert Eigenschaften einer Ebene: Name, Sichtbarkeit, Maßstab, Höhe, Dicke und mehr. |
| [`getStories`](#getstories) | Nur lesend | low | Listet die Geschosse mit ihren Ebenen auf, beginnend mit dem untersten. |
| [`createStory`](#createstory) | Bearbeiten | low | Erstellt ein oder mehrere Geschosse mit ihren Ebenen. |
| [`editStory`](#editstory) | Bearbeiten | low | Ändert ein Geschoss, die Ebenentypen des Dokuments oder dessen Standard-Geschossebenen. |
| [`getClasses`](#getclasses) | Nur lesend | low | Listet die Klassen des Dokuments auf und benennt die speziellen Klassen. |
| [`createClass`](#createclass) | Bearbeiten | low | Erstellt eine Klasse oder gibt die vorhandene Klasse mit diesem Namen zurück. |
| [`editClass`](#editclass) | Bearbeiten | low | Ändert eine Klasse: Beschreibung, Sichtbarkeit, Stift, Füllung, Marker, Schlagschatten und mehr. |
| [`setActiveContext`](#setactivecontext) | Bearbeiten | low | Legt die aktive Ebene und Klasse sowie die Anzeige der übrigen Ebenen und Klassen fest. |
| [`getUnits`](#getunits) | Nur lesend | low | Gibt die Einstellungen der primären und sekundären Einheiten des Dokuments zurück. |
| [`setUnits`](#setunits) | Bearbeiten | low | Ändert die Einstellungen der primären oder sekundären Einheiten des Dokuments. |
| [`convertUnits`](#convertunits) | Nur lesend | low | Rechnet Längen zwischen Welteinheiten und Dokumenteinheiten um. |
| [`setView`](#setview) | Bearbeiten | low | Verschiebt die Ansicht, legt den Zoom fest, verschiebt den Benutzernullpunkt oder zeichnet die Seite neu. |
| [`getPreferences`](#getpreferences) | Nur lesend | low | Liest eine Kategorie der Dokumenteinstellungen aus. |
| [`setPreferences`](#setpreferences) | Bearbeiten | low | Schreibt Dokumenteinstellungen einer Kategorie. |

### getDocumentInfo

Gibt eine Übersicht des aktiven Dokuments zurück: Datei, Anzahlen, Seitengrenzen, Ansichtsmitte und Benutzernullpunkt.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Gibt eine Übersicht des aktiven Dokuments zurück: fileName (einschließlich Erweiterung), filePath (vollständiger nativer Pfad oder null bei einer nicht gespeicherten Zeichnung), Anzahlen von Auswahl/Ebenen/Klassen (selectionCount umfasst alle Ebenen, nicht nur die aktive), Seitengrenzen, Ansichtsmitte, Benutzernullpunkt, Planrotation, aktive Ebene (mit Typ und Maßstab), aktive Klasse, primäre Einheiten, Sichtbarkeitsoptionen für Ebenen/Klassen, IFC-Übersicht (`hasIFCEntities` und `ifcSchema`, wenn IFC-Unterstützung verfügbar ist) sowie den `container`, in dem neue Objekte erstellt werden (aktive Ebene oder die gerade bearbeitete Gruppe/Symboldefinition).

Keine Argumente erforderlich.

**Parameter**

Dieses Werkzeug benötigt keine Parameter.

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `isOpen` | Immer `true`. |
| `fileName`, `filePath` | Dateiname mit Erweiterung und vollständiger nativer Pfad. Bei einer nicht gespeicherten Zeichnung ist `fileName` der Dokumentname und `filePath` `null`. |
| `selectionCount`, `layerCount`, `classCount` | Ausgewählte Objekte auf allen Ebenen, Ebenen und Klassen (einschließlich Klassen referenzierter Dateien). |
| `pageBounds` | Seitengrenzen als [Rechteck](Common.md#rechtecke) in Welteinheiten. |
| `viewCenter`, `userOrigin` | Ansichtsmitte und Benutzernullpunkt als [Punkte](Common.md#punkte) in Welteinheiten. |
| `activeLayer`, `activeLayerKind`, `activeLayerScale` | Name, Typ (als `kind` in [`getLayers`](#getlayers)) und Maßstab (1:scale) der aktiven Ebene. |
| `activeClass` | Name der aktiven Klasse. |
| `primaryUnits`, `unitsPerInch` | Name der primären Einheiten und ihre Einheiten pro Zoll. |
| `planRotated`, `planRotationAngle` | Gibt an, ob der Plan gedreht ist, und nennt den Drehwinkel. |
| `layerOptions`, `classOptions` | Sichtbarkeitsoptionen für Ebenen und Klassen: `activeOnly`, `grayOthers`, `showOthers`, `showSnapOthers`, `showSnapModifyOthers` oder `graySnapOthers`. |
| `hasIFCEntities`, `ifcSchema` | Nur verfügbar, wenn IFC-Unterstützung vorhanden ist. |
| `container` | Siehe Hinweis oben. |


### getLayers

Listet die Ebenen mit Typ, Sichtbarkeit, Maßstab, Höhe, Objektanzahl und Begrenzungen auf.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Listet die Ebenen der Zeichnung mit Name, Typ (design, sheet oder guestDesign bei einer aus einer anderen Datei referenzierten Konstruktionsebene), Sichtbarkeit, Maßstab (1:scale), Höhe, Dicke, Layoutebenenbeschreibung, DPI, Render-Modus, Projektion, Objektanzahl, Begrenzungen und Angabe, ob die jeweilige Ebene aktiv ist. Für eine Konstruktionsebene in einem Geschoss werden außerdem `story` (Geschossname) und `levelType` (ihre Ebene im Geschoss; eine Ebene kann auch ohne Geschoss einen Ebenentyp haben) angegeben.

Objektanzahl und Begrenzungen beziehen sich auf die obersten Zeichnungsobjekte jeder Ebene (nicht auf interne Einträge, die Vectorworks für gelöschte Objekte beibehält) und durchsuchen alle Objekte, was bei großen Zeichnungen langsam ist; schränken Sie den Aufruf nach Möglichkeit ein. `activeOnly` gibt nur die aktive Ebene zurück. `visibleOnly` lässt unsichtbare Ebenen aus (ausgegraute Ebenen bleiben enthalten). `traverse` "allObjects" (Standard) zählt alle Objekte; "visibleObjects" zählt nur Objekte, die Vectorworks aktuell zeichnet (sichtbare Ebene und sichtbare Klasse). Eine unsichtbare Ebene hat dann objectCount 0 und keine Begrenzungen.

Die Antwort enthält `traverse`, `visibleOnly` und `activeOnly` erneut.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `activeOnly` | boolean |  | Nur die aktive Ebene zurückgeben. |
| `visibleOnly` | boolean |  | Unsichtbare Ebenen auslassen (ausgegraute Ebenen bleiben enthalten). |
| `traverse` | string |  | Einer von: `allObjects`, `visibleObjects`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `layers` | Ebenen. Jede enthält `name`, `uuid`, `kind`, `active`, `visibility` (`visible`, `grayed` oder `invisible`), `scale`, `elevation`, `thickness`, `story` und `levelType` (falls für die Konstruktionsebene vorhanden), `description` (bei Layoutebenen, sofern nicht leer), `dpi` (bei Layoutebenen), `renderMode`, `projection`, `objectCount` und `bounds` (nur, wenn es Begrenzungen gibt). |
| `traverse`, `visibleOnly`, `activeOnly` | Die von diesem Aufruf verwendeten Werte. |


### createLayer

Erstellt eine Konstruktionsebene oder Layoutebene.

> **Auswirkung:** Bearbeiten · **Risiko:** low · **Rückgängig:** ein Schritt „MCP: createLayer“ · **In runToolBatch:** ja

**Details**

Erstellt eine Ebene und gibt sie so zurück, wie getLayers sie auflistet. `type` "design" (Standard) erstellt eine Konstruktionsebene mit Weltkoordinaten, `scale` (1:scale, Standard 1), `elevation` und `thickness` (Wandhöhe der Ebene), beide in Welteinheiten; "sheet" erstellt eine druckbare Layoutebene, für die diese Argumente sowie `story`/`levelType` unzulässig sind. `story` (ein Geschossname) zusammen mit `levelType` macht die neue Konstruktionsebene zur Konstruktionsebene dieses Ebenentyps im Geschoss: Eine vorhandene Konstruktionsebene ohne Ebenentyp wird dem Geschoss auf Höhe der Ebene zugeordnet; eine fehlende Ebene wird mit dem Versatz der ersten Standard-Geschossebene dieses Typs (oder 0) hinzugefügt.

Die Höhe einer Konstruktionsebene in einem Geschoss folgt ihrer Ebene; deshalb ist `elevation` zusammen mit `story` unzulässig. Um eine Ebene mit einer neuen Konstruktionsebene bei einem bestimmten Versatz hinzuzufügen, verwenden Sie editStory `addLevels`. `levelType` ohne `story` weist der Ebene außerhalb von Geschossen einen Ebenentyp zu. Die aktive Ebene ändert sich nur bei `activate` true (neue Objekte werden auf der aktiven Ebene erstellt).

Ein unzulässiges Argument führt zum Fehlschlagen des Aufrufs, sodass keine Ebene erstellt wird.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string | Ja | Name der neuen Ebene. Existiert bereits eine Ebene mit diesem Namen, vergibt Vectorworks den nächsten freien Namen (`<name>-2`, …); lesen Sie den tatsächlich vergebenen Namen aus `name` im Ergebnis aus. |
| `type` | string |  | Einer von: `design`, `sheet`. |
| `scale` | number |  | 1:scale, Standard 1. |
| `elevation` | number |  | Höhe in Welteinheiten. |
| `thickness` | number |  | Wandhöhe der Ebene. |
| `story` | string |  | Ein Geschossname. |
| `levelType` | string |  | Mit `story` die Geschossebene, die die neue Ebene übernimmt. Ohne `story` ein Ebenentyp außerhalb von Geschossen. 1 bis 63 Zeichen. |
| `activate` | boolean |  | Standard: `false`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `created` | Immer `true`. |


### editLayer

Ändert Eigenschaften einer Ebene: Name, Sichtbarkeit, Maßstab, Höhe, Dicke und mehr.

> **Auswirkung:** Bearbeiten · **Risiko:** low · **Rückgängig:** ein Schritt „MCP: editLayer“ · **In runToolBatch:** ja

**Details**

Ändert Eigenschaften der Ebene mit dem Namen `name` (bei Auslassung die aktive Ebene): Umbenennen mit `newName`, Festlegen von `visibility` (visible|grayed|invisible), `scale` (Konstruktionsebenen, 1:scale), `elevation` und `thickness` in Welteinheiten, `description` (Plankopf) und `dpi` für Layoutebenen oder Aktivieren mit `activate` (andernfalls bleibt die aktive Ebene unverändert).

**Konstruktionsebenen:** `story` (ein Geschossname) macht die Ebene zur Konstruktionsebene des Ebenentyps `levelType` (Standard: ihr eigener Ebenentyp) dieses Geschosses und verschiebt sie auf die Höhe der Ebene; `story` "" löst sie aus ihrem Geschoss (ihre Höhe bleibt erhalten und sie verliert ihren Ebenentyp, sofern `levelType` keinen festlegt); `levelType` allein verschiebt eine Konstruktionsebene in einem Geschoss auf diese Ebene des Geschosses ("" löscht den Ebenentyp). Eine Ebene hat eine Konstruktionsebene. Die Höhe einer Konstruktionsebene in einem Geschoss folgt ihrer Ebene, daher wird `elevation` dafür abgelehnt: Ändern Sie den Ebenenversatz mit editStory `setLevels`. Die Geschossargumente werden zuerst angewendet; wenn sie abgelehnt werden, schlägt der Aufruf fehl und ändert nichts. Gibt die aktualisierte Ebene mit `applied` zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string |  | Bei Auslassung die aktive Ebene. |
| `newName` | string |  | Der neue Name. |
| `visibility` | string |  | Einer von: `visible`, `grayed`, `invisible`. |
| `scale` | number |  | Konstruktionsebenen, 1:scale. |
| `elevation` | number |  | Höhe in Welteinheiten. |
| `thickness` | number |  | Dicke in Welteinheiten. |
| `description` | string |  | Der Plankopf. |
| `dpi` | integer |  | Auflösung einer Layoutebene. |
| `story` | string |  | Ein Geschossname. |
| `levelType` | string |  | Ebene des Geschosses, die diese Ebene übernimmt (siehe Details). `""` löscht den Ebenentyp. Andernfalls 1 bis 63 Zeichen. |
| `activate` | boolean |  | Andernfalls bleibt die aktive Ebene unverändert. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Ein Eintrag pro übergebener Eigenschaft: `name` (für `newName`), `visibility`, `scale`, `elevation`, `thickness`, `description`, `dpi`, `story`, `levelType` und `activate`, wenn der Wert `true` ist (`activate` mit `false` oder ohne Angabe erzeugt keinen Eintrag). Der Wert ist `true`, wenn Vectorworks die Eigenschaft akzeptiert hat, andernfalls `false` (zum Beispiel bei einem unbekannten Wert für `visibility`). |


### getStories

Listet die Geschosse mit ihren Ebenen auf, beginnend mit dem untersten.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Listet die Geschosse der Zeichnung (die Stockwerke eines Gebäudes) nach Höhe sortiert auf, beginnend mit dem untersten. Jedes Geschoss enthält Name, uuid, Index (seine Position in dieser Reihenfolge, beginnend bei 1), affix (Präfix oder Suffix der Namen der Ebenen, die Vectorworks für das Geschoss aus Standard-Geschossebenen erzeugt), isPrefix (wird von Vectorworks anhand der Ebenennamen abgeleitet: true, wenn keine Ebene eine Konstruktionsebene hat), Höhe, storyAbove/storyBelow (Namen; null am obersten/untersten Geschoss) sowie Ebenen, nach Versatz sortiert: { levelType, offset (relativ zur Geschosshöhe), elevation (Geschosshöhe + Versatz), layerName (die Konstruktionsebene der Ebene; null, wenn keine vorhanden), layerUuid }.

`includeLevelTypes` fügt die Ebenentypen des Dokuments hinzu (Dialog Organisation &gt; Geschosse &gt; Ebenentypen); `includeDefaultLevels` fügt die Standard-Geschossebenen hinzu { index, levelType, offset, layerName (ohne Präfix oder Suffix), scale, wallHeight }, also die Vorlagen für Geschossebenen. Längen sind Welteinheiten. Geschosse werden in createStory und editStory über ihren Namen angesprochen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `includeLevelTypes` | boolean |  | `levelTypes` ergänzen, also die Ebenentypen des Dokuments. |
| `includeDefaultLevels` | boolean |  | `defaultStoryLevels` ergänzen, also die Vorlagen für Geschossebenen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `stories` | Geschosse, von unten nach oben. Jedes enthält `name`, `uuid`, `index`, `affix`, `isPrefix`, `elevation`, `storyAbove`, `storyBelow` (Namen; oben und unten jeweils `null`) und `levels`. |
| `count` | Anzahl der Geschosse. |
| `levelTypes` | Nur mit `includeLevelTypes`: Namen der Ebenentypen des Dokuments. |
| `defaultStoryLevels` | Nur mit `includeDefaultLevels`: Standard-Geschossebenen, jeweils mit `index`, `levelType`, `offset`, `layerName`, `scale` und `wallHeight`. |


### createStory

Erstellt ein oder mehrere Geschosse mit ihren Ebenen.

> **Auswirkung:** Bearbeiten · **Risiko:** low · **Rückgängig:** ein Schritt „MCP: createStory“ · **In runToolBatch:** ja

**Details**

Erstellt ein Geschoss (`name`, `elevation` auf oberster Ebene, optional `affix`, `isPrefix`, `levels`) oder mehrere in einem Aufruf (`stories`: ein Array solcher Objekte). Höhen und Versätze sind Welteinheiten. Jedes Geschoss benötigt eine eigene Höhe und ein eigenes Präfix oder Suffix (Groß-/Kleinschreibung wird ignoriert; Standard: der Geschossname). `levels` fügt Ebenen hinzu: { levelType, offset (relativ zur Geschosshöhe), layerName, createLayer, scale }.

`layerName` bezeichnet die Konstruktionsebene der Ebene: Eine vorhandene Konstruktionsebene ohne Ebenentyp wird bei der Ebenenhöhe dem Geschoss zugeordnet; eine noch nicht vorhandene Ebene wird erstellt (außer `createLayer` ist false) und erhält `scale` (1:scale; Standard: Maßstab der aktiven Ebene). Ohne `layerName` hat die Ebene keine Konstruktionsebene. Ein Ebenentyp, den das Dokument noch nicht hat, wird seinen Ebenentypen hinzugefügt.

Die aktive Ebene ändert sich nicht. Jedes Geschoss und jede Ebene wird vor dem Erstellen geprüft; eine Ablehnung lässt den Aufruf fehlschlagen, sodass nichts erstellt wird (`rolledBack`). Mit `reuseExisting` (Standard false) bleibt ein vorhandenes Geschoss unverändert (Höhe, Präfix oder Suffix, Ebenen), und nur fehlende Ebenen werden ergänzt, sodass derselbe Aufruf wiederholt werden kann. Gibt jedes Geschoss so zurück, wie getStories es auflistet, mit `created`, `reused`, `levelsAdded` und `levelsKept` sowie `levelTypesAdded` und `layersCreated`.

Der Aufruf ist ein Rückgängig-Schritt.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string |  | Geschossname: 1 bis 63 Zeichen; darf von keinem anderen Objekt verwendet werden. |
| `elevation` | number |  | Höhe in Welteinheiten. |
| `affix` | string |  | Groß-/Kleinschreibung wird ignoriert; Standard: der Geschossname. |
| `isPrefix` | boolean |  | `true`, wenn `affix` den Ebenennamen des Geschosses vorangestellt wird. Standard: `false` (Affix als Suffix). |
| `levels` | array of object |  | Die Ebenen, die dem Geschoss hinzugefügt werden. |
| `levels[].levelType` | string | Ja | 1 bis 63 Zeichen. Ein Typ, den das Dokument noch nicht enthält, wird seiner Liste der Ebenentypen hinzugefügt. |
| `levels[].offset` | number | Ja | Relativ zur Geschosshöhe, in Welteinheiten. |
| `levels[].layerName` | string |  | Die Konstruktionsebene dieser Geschossebene. Ohne Angabe hat die Geschossebene keine Ebene. |
| `levels[].createLayer` | boolean |  | Die Ebene erstellen, wenn das Dokument keine Ebene mit diesem Namen enthält. Standard: `true`. |
| `levels[].scale` | number |  | Maßstab einer erstellten Ebene (1:scale). Standardwert (oder `0`): Maßstab der aktiven Ebene. |
| `stories` | array of object |  | Mehrere Geschosse; jedes mit den Argumenten eines einzelnen Geschosses. |
| `stories[].name` | string | Ja | Geschossname: 1 bis 63 Zeichen; darf von keinem anderen Objekt verwendet werden. |
| `stories[].elevation` | number | Ja | Höhe in Welteinheiten. |
| `stories[].affix` | string |  | Beim Vergleich wird die Groß-/Kleinschreibung ignoriert; Standardwert ist der Geschossname. |
| `stories[].isPrefix` | boolean |  | `true`, wenn `affix` den Ebenennamen des Geschosses vorangestellt wird. Standard: `false` (Affix als Suffix). |
| `stories[].levels` | array of object |  | Die Ebenen, die dem Geschoss hinzugefügt werden. |
| `stories[].levels[].levelType` | string | Ja | 1 bis 63 Zeichen. Ein Typ, den das Dokument noch nicht enthält, wird seiner Liste der Ebenentypen hinzugefügt. |
| `stories[].levels[].offset` | number | Ja | Relativ zur Geschosshöhe, in Welteinheiten. |
| `stories[].levels[].layerName` | string |  | Die Konstruktionsebene dieser Geschossebene. Ohne Angabe hat die Geschossebene keine Ebene. |
| `stories[].levels[].createLayer` | boolean |  | Die Ebene erstellen, wenn das Dokument keine Ebene mit diesem Namen enthält. Standard: `true`. |
| `stories[].levels[].scale` | number |  | Maßstab einer erstellten Ebene (1:scale). Standardwert (oder `0`): Maßstab der aktiven Ebene. |
| `reuseExisting` | boolean |  | Standard: `false`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `stories` | Ein Eintrag pro Geschoss des Aufrufs, wie von `getStories` aufgelistet, mit `created` und `reused` (boolesche Werte), `levelsAdded` (vom Aufruf dem Geschoss hinzugefügte Ebenentypen) und `levelsKept` (Ebenentypen des Aufrufs, die ein wiederverwendetes Geschoss bereits enthielt). |
| `createdCount`, `reusedCount` | Anzahl der vom Aufruf erstellten Geschosse und der mit `reuseExisting` übernommenen Geschosse. |
| `levelTypesAdded` | Ebenentypen, die der Aufruf dem Dokument hinzugefügt hat. |
| `layersCreated` | Namen der vom Aufruf erstellten Ebenen. |


### editStory

Ändert ein Geschoss, die Ebenentypen des Dokuments oder dessen Standard-Geschossebenen.

> **Auswirkung:** Bearbeiten · **Risiko:** low · **Rückgängig:** ein Schritt „MCP: editStory“ · **In runToolBatch:** ja

**Details**

Ändert das Geschoss `name`, die Ebenentypen des Dokuments oder dessen Standard-Geschossebenen. Alle Änderungen eines Aufrufs werden vor der Ausführung geprüft und bilden einen Rückgängig-Schritt; eine Ablehnung lässt den gesamten Aufruf fehlschlagen, sodass nichts geändert wird (`rolledBack`). Längen sind Welteinheiten. Änderungen am Geschoss werden in dieser Reihenfolge angewendet: `affix`; `elevation` mit `mode` single (Standard: nur dieses Geschoss), currentAndAbove, currentAndBelow oder all (alle verschobenen Geschosse werden um denselben Abstand versetzt, und zwei Geschosse können nicht dieselbe Höhe haben) – die Konstruktionsebenen der verschobenen Geschosse und die an ihre Ebenen gebundenen Objekte werden mitverschoben; `removeLevels` [{ levelType, deleteLayer }] (die Konstruktionsebene der Ebene bleibt eine Konstruktionsebene ohne Geschoss und Ebenentyp, sofern `deleteLayer` sie nicht löscht; das wird für eine Ebene mit Objekten abgelehnt); `setLevels` [{ levelType, offset }] verschiebt Ebenen zusammen mit ihren Konstruktionsebenen; `addLevels` wie `levels` in createStory; und nach den anderen Änderungen des Aufrufs `newName` (wird auch in den IFC-Daten umbenannt).

`delete` true löscht das Geschoss in einem eigenen Aufruf: Seine Konstruktionsebenen mit ihren Objekten bleiben als Ebenen ohne Geschoss und Ebenentyp erhalten, sofern `deleteLayers` sie nicht löscht; das wird abgelehnt, wenn nicht alle leer sind. Ohne `name`: `levelTypes` { add: [names], rename: [{ from, to }], delete: [names] } – ein Ebenentyp einer Geschossebene kann nicht gelöscht werden (Konstruktionsebenen und Standard-Geschossebenen verlieren einen gelöschten Typ), und Rückgängig stellt einen umbenannten Ebenentyp in den Begrenzungen von Wänden nicht wieder her (benennen Sie ihn stattdessen zurück); `defaultStoryLevels` { reset: replace|append (die Vectorworks-Standards), delete: [index] (wie von getStories mit `includeDefaultLevels` gemeldet), add: [{ levelType, offset, layerName, scale, wallHeight }] (wird in der angegebenen Reihenfolge am Listenanfang hinzugefügt) }.

Gibt das Geschoss so zurück, wie getStories es auflistet, mit `applied`, `levelTypesAdded`, `layersCreated` und `levelTypes` / `defaultStoryLevels`, wenn diese geändert wurden.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string |  | Das zu ändernde Geschoss. Lassen Sie den Parameter weg, um nur `levelTypes` und `defaultStoryLevels` zu ändern. |
| `newName` | string |  | Wird auch in den IFC-Daten umbenannt. |
| `affix` | string |  | Das neue Affix des Geschosses. |
| `elevation` | number |  | Höhe in Welteinheiten. |
| `mode` | string |  | Einer von: `single`, `currentAndAbove`, `currentAndBelow`, `all`. |
| `removeLevels` | array of object |  | Die Ebenen, die aus dem Geschoss entfernt werden sollen. |
| `removeLevels[].levelType` | string | Ja | Ebenentyp einer Geschossebene. |
| `removeLevels[].deleteLayer` | boolean |  | Auch die Ebene dieser Geschossebene löschen. Nicht zulässig, wenn die Ebene Objekte enthält. Standardmäßig bleibt die Ebene erhalten. |
| `setLevels` | array of object |  | Zu verschiebende Geschossebenen mit ihren Ebenen. |
| `setLevels[].levelType` | string | Ja | Ebenentyp einer Geschossebene. |
| `setLevels[].offset` | number | Ja | Neuer Versatz relativ zur Geschosshöhe, in Welteinheiten. |
| `addLevels` | array of object |  | Hinzuzufügende Geschossebenen, wie `levels` bei `createStory`. |
| `addLevels[].levelType` | string | Ja | 1 bis 63 Zeichen. Das Geschoss darf diesen Ebenentyp noch nicht enthalten (verschieben Sie ihn mit `setLevels`). |
| `addLevels[].offset` | number | Ja | Relativ zur Geschosshöhe, in Welteinheiten. |
| `addLevels[].layerName` | string |  | Die Konstruktionsebene dieser Geschossebene. Ohne Angabe hat die Geschossebene keine Ebene. |
| `addLevels[].createLayer` | boolean |  | Die Ebene erstellen, wenn das Dokument keine Ebene mit diesem Namen enthält. Standard: `true`. |
| `addLevels[].scale` | number |  | Maßstab einer erstellten Ebene (1:scale). Standardwert (oder `0`): Maßstab der aktiven Ebene. |
| `delete` | boolean |  | `true` löscht das Geschoss. |
| `deleteLayers` | boolean |  | Mit `delete`: auch die Konstruktionsebenen des Geschosses löschen. Nur zulässig, wenn alle leer sind. |
| `levelTypes` | object |  | Änderungen an den Ebenentypen des Dokuments: `add`, `rename`, `delete`. |
| `levelTypes.add` | array of string |  | Namen der hinzuzufügenden Ebenentypen; jeweils 1 bis 63 Zeichen. |
| `levelTypes.rename` | array of object |  | Umbenennungen von Ebenentypen. |
| `levelTypes.rename[].from` | string | Ja | Der bisherige Name. |
| `levelTypes.rename[].to` | string | Ja | Der neue Name: 1 bis 63 Zeichen. |
| `levelTypes.delete` | array of string |  | Zu löschende Ebenentypen. Der Ebenentyp einer Geschossebene kann nicht gelöscht werden. |
| `defaultStoryLevels` | object |  | Änderungen der Standard-Geschossebenen: `reset` oder `delete` sowie `add`. |
| `defaultStoryLevels.reset` | string |  | Einer von: `replace`, `append`. |
| `defaultStoryLevels.delete` | array of integer |  | Indizes der zu löschenden Standard-Geschossebenen, wie von `getStories` mit `includeDefaultLevels` gemeldet. |
| `defaultStoryLevels.add` | array of object |  | Hinzuzufügende Standard-Geschossebenen; sie werden in der angegebenen Reihenfolge an den Anfang der Liste gesetzt. |
| `defaultStoryLevels.add[].levelType` | string | Ja | Ebenentyp. |
| `defaultStoryLevels.add[].offset` | number | Ja | Relativ zur Geschosshöhe, in Welteinheiten. |
| `defaultStoryLevels.add[].layerName` | string |  | Ebenenname der Geschossebene. |
| `defaultStoryLevels.add[].scale` | number |  | Maßstab der Ebene (1:scale). Standard: `0` (Maßstab der aktiven Ebene); darf nicht negativ sein. |
| `defaultStoryLevels.add[].wallHeight` | number |  | Wandhöhe der Ebene in Welteinheiten. Standard: `0`; darf nicht negativ sein. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `story` | Geschoss nach den Änderungen, wie von `getStories` aufgelistet. Nur vorhanden, wenn der Aufruf ein Geschoss geändert hat. |
| `applied` | Nur mit `story`. Ein Eintrag pro angegebener Änderung am Geschoss: `affix`, `elevation` und `newName` haben den Wert `true`; `removeLevels`, `setLevels` und `addLevels` enthalten die Ebenentypen, die entfernt, verschoben oder hinzugefügt wurden. |
| `levelTypesAdded` | Namen der vom Aufruf dem Dokument hinzugefügten Ebenentypen (leeres Array, wenn keine hinzugefügt wurden). |
| `layersCreated` | Namen der vom Aufruf erstellten Ebenen (leeres Array, wenn keine erstellt wurden). |
| `levelTypes` | Nur wenn der Aufruf `levelTypes` enthält: Namen aller Ebenentypen des Dokuments nach den Änderungen. |
| `defaultStoryLevels` | Nur wenn der Aufruf `defaultStoryLevels` enthält: Standard-Geschossebenen nach den Änderungen, wie von `getStories` mit `includeDefaultLevels` aufgelistet. |
| `deleted` | Nur mit `delete`: `true`. In diesem Fall gibt es weder `story` noch `applied`. |
| `layersDeleted`, `layersKept` | Nur mit `delete`: Namen der Konstruktionsebenen des Geschosses, gelöscht mit `deleteLayers` oder beibehalten (als Ebenen ohne Geschoss und Ebenentyp). |


### getClasses

Listet die Klassen des Dokuments auf und benennt die speziellen Klassen.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Listet die Klassen des Dokuments (die benannten Attributsätze, von denen Objekte Attribute übernehmen) mit Name, Index und Sichtbarkeit auf, außerdem `specialClasses`: die Namen der Klasse `none`, der integrierten Klasse `dimension` und der Klasse `default` des aktuellen Containers (normalerweise die aktive Klasse); createClass `guides` gibt die Klasse Guides zurück. Mit `detailed` werden außerdem Beschreibung, Kennzeichnungen für non-plot/use-at-creation, Stift (RGB-Farben und Farbtabellenindizes, lineWeightMils, opacity, raw style, styleKind, lineType), Füllung (RGB-Farben und Farbtabellenindizes, type, raw style, resource, opacity), Marker, Schlagschatten, Texturen (`texture`, `wallTextures` right/left/center, `roofTextures` top/edge/dormer) und Textstil jeder Klasse zurückgegeben.

Mit `includeGuestClasses` werden auch Klassen eingeschlossen, auf die aus anderen Dokumenten verwiesen wird.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `includeGuestClasses` | boolean |  | Gastklassen einschließen: Klassen, die aus anderen Dokumenten referenziert werden. |
| `detailed` | boolean |  | Attribute jeder Klasse hinzufügen (siehe Ergebnis). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `classes` | Klassen des Dokuments. Jede enthält `name`, `index` und `visibility`; mit `detailed` außerdem die unten aufgeführten Schlüssel. |
| `classOptions` | Anzeige der Klassen außer der aktiven Klasse: einer der `classOptions`-Werte von `setActiveContext`. Wird weggelassen, wenn der Wert nicht ausgelesen werden kann. |
| `specialClasses` | Namen der speziellen Klassen: `none`, `dimension` und `default`. |


### createClass

Erstellt eine Klasse oder gibt die vorhandene Klasse mit diesem Namen zurück.

> **Auswirkung:** Bearbeiten · **Risiko:** low · **Rückgängig:** ein Schritt „MCP: createClass“ · **In runToolBatch:** ja

**Details**

Erstellt eine Klasse und gibt die vorhandene zurück, wenn der Name bereits vergeben ist. Verwenden Sie `guides` statt `name`, um die Klasse Guides (für Hilfsobjekte) abzurufen; sie wird bei Bedarf erstellt. Optional `description`; legen Sie `activate` fest, damit die Klasse zur aktiven Klasse wird und neue Objekte darin erstellt werden. Gibt den Klassennamen und den Index zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string |  | Klassenname. Erforderlich, außer wenn `guides` auf `true` gesetzt ist. |
| `guides` | boolean |  | `true`: statt der Klasse `name` die Klasse Guides zurückgeben. |
| `description` | string |  | Beschreibungstext. |
| `activate` | boolean |  | Die Klasse als aktive Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `created` | Immer `true`, auch wenn die Klasse bereits existiert. Prüfen Sie mit `getClasses`, ob sie vorhanden ist. |
| `name` | Name der Klasse. |
| `index` | Interner Index der Klasse. Wird weggelassen, wenn er nicht ausgelesen werden kann. |


### editClass

Ändert eine Klasse: Beschreibung, Sichtbarkeit, Stift, Füllung, Marker, Schlagschatten und mehr.

> **Auswirkung:** Bearbeiten · **Risiko:** low · **Rückgängig:** ein Schritt „MCP: editClass“ · **In runToolBatch:** ja

**Details**

Ändert die Klasse `name` (bei Auslassung die aktive Klasse). Legt `description`, `visibility` (visible|grayed|invisible), `nonPlot`, `useAtCreation`, den Klassen-`pen` (foreColor, backColor, foreColorIndex, backColorIndex, lineWeightMils, opacity, style, lineType), `fill` (foreColor, backColor, foreColorIndex, backColorIndex, opacity, style, resource), gemeinsame `opacity`, `beginningMarker`/`endMarker`, `dropShadow`, `useTextures`/`texture`, `wallTextures` (right, left, center), `roofTextures` (top, edge, dormer), `useTextStyle`/`textStyle` oder `activate` fest.

Farbindizes sind Indizes in der Dokumentfarbtabelle; ein Index, der dem aktuellen der Klasse entspricht, wird ignoriert. Daher kann eine mit getClasses ausgelesene Klasse mit bearbeiteter RGB-Farbe zurückgesendet werden; wenn beide Formen geändert werden, hat der Index Vorrang. Texturteile sind Indizes von Rendertexturen (0 = keine); unvollständige Marker-, Schlagschatten- und Texturteilobjekte behalten nicht angegebene Elemente bei.

`action` "delete" entfernt die Klasse und verschiebt ihre Objekte nach None. Objekte, deren Attribute auf „nach Klasse“ eingestellt sind, übernehmen diese Werte.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string |  | Bei Auslassung die aktive Klasse. |
| `action` | string |  | Einer von: `modify`, `delete`. |
| `description` | string |  | Beschreibungstext. |
| `visibility` | string |  | Einer von: `visible`, `grayed`, `invisible`. |
| `nonPlot` | boolean |  | Objekte dieser Klasse nicht drucken. |
| `useAtCreation` | boolean |  | Objekte, die in dieser Klasse erstellt werden, übernehmen beim Erstellen deren Attribute. |
| `pen` | object |  | Stiftattribute; nur angegebene Elemente werden geändert. |
| `pen.foreColor` | [Farbe](Common.md#farben) |  | Vordergrundfarbe (RGB). |
| `pen.backColor` | [Farbe](Common.md#farben) |  | Hintergrundfarbe (RGB). |
| `pen.foreColorIndex` | integer |  | Vordergrundfarbe als Index in der Dokumentfarbtabelle. |
| `pen.backColorIndex` | integer |  | Hintergrundfarbe als Index in der Dokumentfarbtabelle. |
| `pen.lineWeightMils` | integer |  | Linienstärke in mils. |
| `pen.opacity` | integer |  | Deckkraft, 0–100. |
| `pen.style` | integer |  | Unveränderter Stilstiftwert. |
| `pen.lineType` | integer |  | Interner Index eines Linientyps. |
| `fill` | object |  | Füllungsattribute; nur angegebene Elemente werden geändert. |
| `fill.foreColor` | [Farbe](Common.md#farben) |  | Vordergrundfarbe (RGB). |
| `fill.backColor` | [Farbe](Common.md#farben) |  | Hintergrundfarbe (RGB). |
| `fill.foreColorIndex` | integer |  | Vordergrundfarbe als Index in der Dokumentfarbtabelle. |
| `fill.backColorIndex` | integer |  | Hintergrundfarbe als Index in der Dokumentfarbtabelle. |
| `fill.opacity` | integer |  | Deckkraft, 0–100. |
| `fill.style` | integer |  | Unveränderter Füllungsstilwert. |
| `fill.resource` | integer |  | Interner Index einer Schraffur, Kachel, eines Farbverlaufs oder Bilds. |
| `opacity` | integer |  | Deckkraft, 0–100. |
| `beginningMarker` | [Marker](Attributes.md#linienendmarkierungen) |  | Anfangsmarkierung der Klasse. Nicht angegebene Elemente behalten ihren bisherigen Wert. |
| `endMarker` | [Marker](Attributes.md#linienendmarkierungen) |  | Endmarkierung der Klasse. Nicht angegebene Elemente behalten ihren bisherigen Wert. |
| `dropShadow` | [Schlagschatten](Attributes.md#schlagschatten) |  | Schlagschatten der Klasse. Nicht angegebene Elemente behalten ihren bisherigen Wert. |
| `useTextures` | boolean |  | Die Texturen der Klasse verwenden. |
| `texture` | integer |  | Render-Texturindex; `0` bedeutet keine. |
| `wallTextures` | object |  | Elemente: `right`, `left`, `center`. |
| `wallTextures.right` | integer |  | Render-Texturindex für die rechte Wandseite; `0` bedeutet keine. |
| `wallTextures.left` | integer |  | Render-Texturindex für die linke Wandseite; `0` bedeutet keine. |
| `wallTextures.center` | integer |  | Render-Texturindex für die Wandmitte; `0` bedeutet keine. |
| `roofTextures` | object |  | Elemente: `top`, `edge`, `dormer`. |
| `roofTextures.top` | integer |  | Render-Texturindex für die Dachoberseite; `0` bedeutet keine. |
| `roofTextures.edge` | integer |  | Render-Texturindex für die Dachkante; `0` bedeutet keine. |
| `roofTextures.dormer` | integer |  | Render-Texturindex für die Dachgauben; `0` bedeutet keine. |
| `useTextStyle` | boolean |  | Den Textstil der Klasse verwenden. |
| `textStyle` | integer |  | Name oder Ressourcen-UUID eines Textstils; eine leere Zeichenfolge bedeutet keinen Textstil. |
| `activate` | boolean |  | Die Klasse als aktive Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Ein Eintrag pro übergebener Einstellung. Der Wert ist `true`, wenn Vectorworks die Einstellung akzeptiert hat. Die Schlüssel sind `description`, `visibility`, `nonPlot`, `useAtCreation`, `opacity`, `useTextures`, `texture`, `wallTextures`, `roofTextures` (`false`, wenn der Wert kein Objekt ist), `useTextStyle`, `textStyle`, `beginningMarker`, `endMarker`, `dropShadow`, `activate` (nur aufgeführt, wenn `true`) sowie für Stift und Füllung `penForeColor`, `penBackColor`, `lineWeightMils`, `penOpacity`, `penStyle`, `penLineType`, `penColorIndices`, `fillForeColor`, `fillBackColor`, `fillOpacity`, `fillStyle`, `fillResource` und `fillColorIndices`. |


### setActiveContext

Legt die aktive Ebene und Klasse sowie die Anzeige der übrigen Ebenen und Klassen fest.

> **Auswirkung:** Bearbeiten · **Risiko:** low · **Rückgängig:** ein Schritt „MCP: setActiveContext“ · **In runToolBatch:** ja

**Details**

Legt fest, was neue Objekte übernehmen und womit der Benutzer arbeiten kann: die aktive `layer` und/oder `class` anhand des Namens, die Anzeige nicht aktiver Ebenen und Klassen mit `layerOptions`/`classOptions` (activeOnly, grayOthers, showOthers, showSnapOthers, showSnapModifyOthers, graySnapOthers) sowie die zu bearbeitende Symboldefinition mit `symbolDefinition`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `layer` | string |  | Name der Ebene, die aktiviert werden soll. |
| `class` | string |  | Name der Klasse, die aktiviert werden soll. |
| `layerOptions` | string |  | Einer von: `activeOnly`, `grayOthers`, `showOthers`, `showSnapOthers`, `showSnapModifyOthers`, `graySnapOthers`. |
| `classOptions` | string |  | Einer von: `activeOnly`, `grayOthers`, `showOthers`, `showSnapOthers`, `showSnapModifyOthers`, `graySnapOthers`. |
| `symbolDefinition` | string |  | Name der Symboldefinition, die als aktuelle Symboldefinition festgelegt werden soll. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `layerActivated` | `true`, wenn die Ebene jetzt aktiv ist. |
| `classActivated` | `true`, wenn die Klasse jetzt aktiv ist. |
| `layerOptions` | `true`, wenn Vectorworks die Option akzeptiert hat; bei unbekanntem Optionsnamen `false`. |
| `classOptions` | `true`, wenn Vectorworks die Option akzeptiert hat; bei unbekanntem Optionsnamen `false`. |
| `symbolDefinitionActivated` | `true`, wenn die Symboldefinition jetzt die aktuelle ist; `false`, wenn der Name keiner Symboldefinition entspricht. |


### getUnits

Gibt die Einstellungen der primären und sekundären Einheiten des Dokuments zurück.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Gibt alle Einstellungen der primären und sekundären Einheiten des Dokuments zurück: Name, Zeichen, Einheiten pro Zoll, Metrik-Kennzeichen, Anzeige-/Bemaßungsgenauigkeit, Bruch- und Trennzeichenoptionen, Winkeleinheit sowie (nur bei primären Einheiten) Flächen- und Volumeneinheiten und die Winkeleinstellungen des Dokuments. Keine Argumente erforderlich.

**Parameter**

Dieses Werkzeug benötigt keine Parameter.

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `primary` | Einstellungen der primären Einheiten. |
| `secondary` | Einstellungen der sekundären Einheiten. |


### setUnits

Ändert die Einstellungen der primären oder sekundären Einheiten des Dokuments.

> **Auswirkung:** Bearbeiten · **Risiko:** low · **Rückgängig:** ein Schritt „MCP: setUnits“ · **In runToolBatch:** ja

**Details**

Ändert die Dokumenteinheiten. `which` wählt "primary" (Standard) oder "secondary". Legen Sie beliebige der Werte `name`, `mark`, `unitsPerInch`, `style`, `metric`, `showUnitMark`, `leadingZero`, `trailingZeros`, `displayAsFraction`, `showThousandsSeparator`, die Dezimal-/Bruchgenauigkeiten für Anzeige und Bemaßung, `angularUnit` (degrees|radians|gradians) und – bei primären Einheiten – Flächen-/Volumeneinheitsnamen, -zeichen, -faktoren und -genauigkeiten sowie `documentAngularUnit` und `documentAngularPrecision` fest.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `which` | string |  | Einer von: `primary`, `secondary`. |
| `name` | string |  | Name der Einheit. |
| `mark` | string |  | Einheitenzeichen, das nach einem Wert angezeigt wird. |
| `unitsPerInch` | number |  | Anzahl dieser Einheiten pro Zoll. |
| `style` | integer |  | Einheitenstil-Code, wie von `getUnits` gemeldet. |
| `metric` | boolean |  | `true` für eine metrische Einheit. |
| `showUnitMark` | boolean |  | Das Einheitenzeichen nach einem Wert anzeigen. |
| `leadingZero` | boolean |  | Bei Werten unter 1 eine führende Null anzeigen. |
| `trailingZeros` | boolean |  | Nachgestellte Nullen anzeigen. |
| `displayAsFraction` | boolean |  | Werte als Brüche anzeigen. |
| `showThousandsSeparator` | boolean |  | Tausendertrennzeichen anzeigen. |
| `decimalDisplayPrecision` | integer |  | Dezimalstellen eines angezeigten Werts. |
| `decimalDimensionPrecision` | integer |  | Dezimalstellen eines Bemaßungswerts. |
| `fractionalDisplayPrecision` | integer |  | Bruchgenauigkeit eines angezeigten Werts. |
| `fractionalDimensionPrecision` | integer |  | Bruchgenauigkeit eines Bemaßungswerts. |
| `angularUnit` | string |  | Einer von: `degrees`, `radians`, `gradians`. |
| `squareUnitDivision` | integer |  | Nur für primäre Einheiten. Teilung der Flächeneinheit. |
| `squareUnitMark` | string |  | Nur für primäre Einheiten. Zeichen der Flächeneinheit. |
| `areaUnitName` | string |  | Nur für primäre Einheiten. Name der Flächeneinheit. |
| `areaUnitMark` | string |  | Nur für primäre Einheiten. Zeichen der Flächeneinheit. |
| `areaUnitsPerSquareInch` | number |  | Nur für primäre Einheiten. Anzahl der Flächeneinheiten pro Quadratzoll. |
| `areaDecimalPrecision` | integer |  | Nur für primäre Einheiten. Dezimalstellen einer Fläche. |
| `volumeUnitName` | string |  | Nur für primäre Einheiten. Name der Volumeneinheit. |
| `volumeUnitMark` | string |  | Nur für primäre Einheiten. Zeichen der Volumeneinheit. |
| `volumeUnitsPerCubicInch` | number |  | Nur für primäre Einheiten. Anzahl der Volumeneinheiten pro Kubikzoll. |
| `volumeDecimalPrecision` | integer |  | Nur für primäre Einheiten. Dezimalstellen eines Volumens. |
| `documentAngularUnit` | string |  | Einer von: `degrees`, `radians`, `gradians`. |
| `documentAngularPrecision` | integer |  | Nur für primäre Einheiten. Dezimalstellen eines Winkels. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Ein Eintrag pro übergebener Einstellung. Der Wert ist `true`, wenn Vectorworks die Einstellung akzeptiert hat; bei unbekanntem Namen für `angularUnit` oder `documentAngularUnit` ist er `false`. |
| `units` | Einheiteneinstellungen nach den Änderungen, wie von `getUnits` aufgelistet. |


### convertUnits

Rechnet Längen zwischen Welteinheiten und Dokumenteinheiten um.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Rechnet Längen zwischen den Welteinheiten um, die alle Werkzeuge dieser API verwenden, und den Dokumenteinheiten, die in der Vectorworks-Benutzeroberfläche angezeigt werden. `worldLength` wird als `inDocumentUnits`, `unitsLength` als `inWorldUnits` zurückgegeben.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `worldLength` | number |  | Länge in Welteinheiten. |
| `unitsLength` | number |  | Länge in Dokumenteinheiten. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `inDocumentUnits` | Nur mit `worldLength`: diese Länge in Dokumenteinheiten. |
| `inWorldUnits` | Nur mit `unitsLength`: diese Länge in Welteinheiten. |
| `documentUnits` | Name der primären Dokumenteinheit. |


### setView

Verschiebt die Ansicht, legt den Zoom fest, verschiebt den Benutzernullpunkt oder zeichnet die Seite neu.

> **Auswirkung:** Bearbeiten · **Risiko:** low · **Rückgängig:** ein Schritt „MCP: setView“ · **In runToolBatch:** ja

**Details**

Ändert die Anzeige und die Position des Zeichnungsnullpunkts: `center` verschiebt die Ansicht zu einem Weltpunkt, `zoom` legt den Zoomfaktor fest (1.0 = 100%), `userOrigin` verschiebt den Weltpunkt, den der Benutzer als (0,0) sieht, und `redraw` erzwingt die Neuzeichnung des Seitenbereichs.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `center` | [Punkt](Common.md#punkte) |  | Mittelpunkt. |
| `zoom` | number |  | Zoomfaktor; `1.0` entspricht 100 %. Werte von `0` oder kleiner werden abgelehnt (`zoomSet` ist dann `false`). |
| `userOrigin` | [Punkt](Common.md#punkte) |  | Weltpunkt, den der Benutzer als `(0,0)` sieht. |
| `redraw` | boolean |  | `true` erzwingt eine Neuzeichnung des Seitenbereichs. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `centerSet` | Nur mit `center`: `true`, wenn die Ansicht verschoben wurde. |
| `zoomSet` | Nur mit `zoom`: `true`, wenn der Zoom eingestellt wurde. |
| `userOriginSet` | Nur mit `userOrigin`: immer `true`. Vectorworks verschiebt den Benutzernullpunkt nicht, während ein Container bearbeitet wird, der dies verhindert; lesen Sie ihn mit `getDocumentInfo` erneut aus. |
| `redrawn` | Nur mit `redraw` auf `true`: `true`, wenn der Seitenbereich neu gezeichnet wurde. |


### getPreferences

Liest eine Kategorie der Dokumenteinstellungen aus.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Liest die Dokumenteinstellungen einer `category`: display (Rendering und Bildschirmanzeige), editing (Sitzung, Bemaßungen, Rückgängig, automatische Speicherung), snapping (SmartCursor), grid, stackLayers, text (Standardeinstellungen für neuen Text) oder defaultAttributes (Stift-/Füllungsfarben als RGB und Farbtabellenindex, Stile, Linienstärke, Füllungsressourcen, Deckkraft, Marker, Kennzeichen „nach Klasse“, Dokument-Schlagschatten und Klassen für neue Objekte und Bemaßungen).

Lassen Sie `category` aus, um alle Einstellungen auszulesen. Mit category "variable" wird eine rohe Programmvariable gelesen, die durch `selector` und `type` angegeben wird (bool|uint8|int8|int16|int32|double|string).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `category` | string |  | Einer von: `display`, `editing`, `snapping`, `grid`, `stackLayers`, `text`, `defaultAttributes`, `variable`. |
| `selector` | integer |  | Bei `variable`: Auswahlwert der Programmvariablen. |
| `type` | string |  | Einer von: `bool`, `uint8`, `int8`, `int16`, `int32`, `double`, `string`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `display`, `editing`, `snapping`, `grid`, `stackLayers`, `text`, `defaultAttributes` | Ein Objekt für jede ausgelesene Kategorie: die angegebene Kategorie oder alle sieben, wenn `category` nicht angegeben ist. |
| `selector`, `value` | Mit `category` gleich `variable` statt der obigen Kategorien: Auswahlwert und Wert der Programmvariablen. |

| Category | Settings |
|---|---|
| `display` | Boolesche Werte: `blackAndWhiteOnly`, `useLayerColors`, `zoomLineThickness`, `blackBackground`, `showRulers`, `showScrollBars`, `showPageBoundary`, `showPageBreaks`, `showOthersInGroup`, `showOthersInGroupGrayed`, `eightSelectionHandles`, `fullScreenCursor`, `noFillBehindText`, `adjustFlippedText`, `xRayMode`, `displayHiddenObjectsGhosted`, `showInternalOriginMarker`, `allowDropShadows`, `perspectiveCropped`. Ganzzahlen: `conversionResolution2D`, `conversionResolution3D`, `displayLightObjects`, `rotatedTextDisplay`, `displayBitmaps`, `hiddenLineShade`, `display3DLoci`, `defaultRenderMode`, `defaultProjection`, `rotationResponse3D`. |
| `editing` | Boolesche Werte: `clickDrag`, `offsetDuplicates`, `associateDimensions`, `autoAssociateDimensions`, `createDimensionsInDimensionClass`, `wallAutoJoin`, `undoViewChanges`, `duplicateTagsWithObjects`, `occludedPickingAndSnapping`. Ganzzahlen: `maxUndos`, `autoSaveInterval`, `backupInterval`, `lineWeightUnit`, `dimensionStandard`. Zahl: `customMoveDistance`. |
| `snapping` | Boolesche Werte: `snapToGrid`, `snapToObjects`, `snapToLoci`, `snapToEdgePoints`, `snapToSelectionOnly`, `snapToAngle`, `snapToIntersection`, `smartPoints`, `snapToDistance`, `smartEdge`, `constrainTangent`, `snapToEndPoint`, `snapToMidPoint`, `snapToCenter`, `snapToQuadrant`, `snapToInsertionPoint`, `snapToVertex`, `snapToEdge`, `snapToMasterPoints`, `snapToRelativeAngles`, `snapToAlternateCoordinateSystem`, `snapToAnglesFromAxes` (schreibgeschützt), `snapToCombinedPageArea`, `snapToIndividualPages`, `floatingDatum`, `showSnapBox`, `showSelectionBox`, `useEdgeOffset`, `useProportionalDivision`, `useMultipleDivisions`. Ganzzahl: `snapRadiusPixels`. Zahlen: `snapBoxRadius`, `selectionRadius`, `relativeAngle`, `alternateCoordinateSystemAngle`, `edgeOffsetDistance`, `proportionalPercent`, `divisionDistance`. Zeichenfolge: `snapAngles`. |
| `grid` | Boolesche Werte: `showGrid`, `printGrid`, `snapToGrid`. Zahlen: `snapGridX`, `snapGridY`, `referenceGridX`, `referenceGridY`, `sheetLayerSnapGridX`, `sheetLayerSnapGridY`, `angle`, `angleY`. |
| `stackLayers` | Boolesche Werte: `enabled`, `create2DObjects`, `ignoreOtherScales`, `restoreViews`, `centerView`, `showPageBoundary`, `onlyActiveLayer2DObjects`, `onlyStoryLayers`. |
| `text` | `fontName` (Zeichenfolge), `size` (Zahl in Welteinheiten), `leading` (Zahl), `style` (Objekt mit den Booleschen Werten `bold`, `italic`, `underline`, `outline`, `shadow`), `justification` (`left`, `center` oder `right`), `verticalAlignment` (`topOfBox`, `topBaseline`, `centerOfBox`, `bottomBaseline` oder `bottomOfBox`), `lineSpacing` (`single`, `oneAndHalf`, `double` oder `custom`). |
| `defaultAttributes` | Farben als RGB (`penForeColor`, `penBackColor`, `fillForeColor`, `fillBackColor`) und als Farbtabellenindizes (`penForeColorIndex`, `penBackColorIndex`, `fillForeColorIndex`, `fillBackColorIndex`); `penStyle`, `lineWeightMils`, `fillStyle`, `fillType` (schreibgeschützt), `hatch`, `gradient`, `imageFill`, `tile`, `penOpacity`, `fillOpacity`; Nach-Klasse-Flags `penColorsByClass`, `fillColorsByClass`, `penStyleByClass`, `lineWeightByClass`, `fillStyleByClass`, `penOpacityByClass`, `fillOpacityByClass`, `markersByClass`; `beginningMarker` und `endMarker` ([Markierungen](Attributes.md#linienendmarkierungen)); `documentDropShadow` (schreibgeschützt, [Schlagschatten](Attributes.md#schlagschatten)); `class` und `dimensionClass` (Klassennamen). |


### setPreferences

Schreibt Dokumenteinstellungen einer Kategorie.

> **Auswirkung:** Bearbeiten · **Risiko:** low · **Rückgängig:** ein Schritt „MCP: setPreferences“ · **In runToolBatch:** ja

**Details**

Schreibt Dokumenteinstellungen. `category` wählt die Gruppe (display, editing, snapping, grid, stackLayers, text, defaultAttributes), und `values` ist ein Objekt mit den Einstellungsnamen, die getPreferences zurückgibt. Nur vorhandene Elemente werden geschrieben; das Ergebnis gibt an, welche erfolgreich waren.

**Nur lesend:** snapToAnglesFromAxes, fillType und documentDropShadow. Bei defaultAttributes werden Farben als RGB (penForeColor, ...) oder Farbtabellenindizes (penForeColorIndex, ...) angegeben; ein Index, der dem aktuellen entspricht, wird ignoriert. Daher können mit getPreferences ausgelesene Werte mit geänderter RGB-Farbe zurückgesendet werden; werden beide Formen geändert, hat der Index Vorrang. beginningMarker/endMarker übernehmen unvollständige Markerobjekte; die Kennzeichen „nach Klasse“ können – mit Ausnahme von penOpacityByClass/fillOpacityByClass – nur eingeschaltet werden (ein ausdrücklich geschriebener Wert schaltet eines aus). Mit category "variable" wird die rohe Programmvariable `selector` vom Typ `type` auf `value` gesetzt.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `category` | string | Ja | Einer von: `display`, `editing`, `snapping`, `grid`, `stackLayers`, `text`, `defaultAttributes`, `variable`. |
| `values` | object |  | Zu schreibende Einstellungen anhand der von `getPreferences` für die Kategorie aufgeführten Namen. Es werden nur die angegebenen Elemente geschrieben. |
| `selector` | integer |  | Bei `variable`: Auswahlwert der Programmvariablen. |
| `type` | string |  | Einer von: `bool`, `uint8`, `int8`, `int16`, `int32`, `double`, `string`. |
| `value` | string or number or integer or boolean |  | Bei `variable`: zu schreibender Wert; sein JSON-Typ muss zu `type` passen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für eine Kategorie: ein Eintrag pro Einstellung, die im Aufruf angegeben wurde; `true`, wenn Vectorworks sie akzeptiert hat. Für `variable`: `true`, wenn die Variable geschrieben wurde. |
| `selector` | Mit `variable`: der geschriebene Selektor. |

In `defaultAttributes` enthält `applied` diese Schlüssel: `colors` (RGB-Farben), `colorIndices` (Farbtabellenindizes; `false`, wenn ein Index keine Ganzzahl im gültigen Farbindexbereich ist), die Nach-Klasse-Flags, `penStyle`, `lineWeightMils`, `fillStyle`, `hatch`, `gradient`, `imageFill`, `tile`, `opacity` (`penOpacity` und `fillOpacity`; der ausgelassene Wert behält seine Einstellung), `opacityByClass` (`penOpacityByClass` und `fillOpacityByClass`; der ausgelassene Wert behält seine Einstellung), `beginningMarker`, `endMarker` (bei einer partiellen Markierung bleiben ausgelassene Elemente unverändert) sowie `class` und `dimensionClass` (`false`, wenn die Klasse nicht existiert). Die Kategorie `text` enthält `applied.style` für ihr `style`-Objekt; nur vorhandene Elemente werden geändert.

Fehler: `unknown 'category' (display, editing, snapping, grid, stackLayers, text, defaultAttributes, variable)`; `unknown variable 'type': <type>`.


## Selection

> **Gruppe:** `Selection` · **Gruppen-ID:** `selection` · **Standardmäßig aktiv:** Ja · **Risikostufe:** medium · **Werkzeuge:** 3

**Aktuelle Auswahl auflisten und Objekte gemeinsam verschieben, drehen, skalieren, duplizieren, gruppieren, löschen oder neu klassifizieren.**

Fragt die aktuelle Auswahl ab und bearbeitet sie: ausgewählte Objekte auflisten und sie gemeinsam verschieben, drehen, skalieren, duplizieren, gruppieren, löschen oder neu klassifizieren. Jede Bearbeitung wird als eigener benannter, rückgängig zu machender Vectorworks-Vorgang ausgeführt.

| Werkzeug | Auswirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`getSelection`](#getselection) | Nur lesend | low | Listet die ausgewählten Objekte aller Ebenen sowie die Begrenzungen der Auswahl auf. |
| [`selectObjects`](#selectobjects) | Bearbeiten | medium | Wählt Objekte anhand von Kriterien oder UUID aus bzw. ab oder wählt alle oder keine aus. |
| [`editSelection`](#editselection) | Bearbeiten | medium | Verschiebt, dreht, skaliert, dupliziert, gruppiert, löscht oder klassifiziert die Auswahl neu. |

### getSelection

Listet die ausgewählten Objekte aller Ebenen sowie die Begrenzungen der Auswahl auf.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Listet die aktuell ausgewählten Objekte (uuid, type, name) sowie die gemeinsamen Begrenzungen der Auswahl auf. Berücksichtigt die ausgewählten Objekte aller Ebenen der Zeichnung, nicht nur der aktiven. `descend` (Standard none, außerdem groups, viewports oder all) listet auch ausgewählte Objekte innerhalb dieser Container auf, z. B. während der Benutzer eine Gruppe bearbeitet; `bounds` bezieht sich auf die ausgewählten Objekte der obersten Ebene.

`workingLayers` gibt die Anzahl und Begrenzungen der Auswahl an, auf die editSelection wirkt: die ausgewählten Objekte der aktiven Ebene sowie Objekte anderer Ebenen, wenn die Ebenenoptionen deren Bearbeitung erlauben.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `descend` | string |  | Einer von: `none`, `groups`, `viewports`, `all`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `count` | Anzahl der Objekte in `objects`. |
| `objects` | Ausgewählte Objekte, jeweils als [Objektreferenz](Common.md#objektreferenzen). |
| `bounds` | Zusammengefasste [Begrenzungen](Common.md#rechtecke) der ausgewählten Objekte der obersten Ebene. Wird bei leerer Auswahl weggelassen. |
| `workingLayers` | Auswahl, auf die `editSelection` angewendet wird: `count` (Anzahl ausgewählter Objekte) und `bounds`. `bounds` wird weggelassen, wenn es keine solche Auswahl gibt. |


### selectObjects

Wählt Objekte anhand von Kriterien oder UUID aus bzw. ab oder wählt alle oder keine aus.

> **Auswirkung:** Bearbeiten · **Risiko:** medium · **Rückgängig:** ein Schritt „MCP: selectObjects“ · **In runToolBatch:** ja

**Details**

Ändert die Auswahl. Verwenden Sie `all` oder `none`, um alles auszuwählen bzw. abzuwählen, oder übergeben Sie `criteria` (eine Vectorworks-Kriterienzeichenfolge mit derselben Syntax wie bei findObjects) und/oder `uuids`. Kriterien, die sich nicht kompilieren lassen, geben einen Fehler zurück. Der Modus `mode` "replace" (Standard) oder "add" wählt die Ziele aus und gibt `selectedCount` zurück; "remove" wählt nur die Ziele ab und gibt `deselectedCount` zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `all` | boolean |  | `true` wählt alle Objekte aus. |
| `none` | boolean |  | `true` hebt die Auswahl aller Objekte auf. |
| `criteria` | string |  | Eine Vectorworks-Kriterienzeichenfolge mit derselben Syntax wie bei findObjects. |
| `uuids` | array of string |  | UUIDs der betroffenen Objekte. UUIDs ohne passendes Objekt werden ohne Fehler übersprungen. |
| `mode` | string |  | Einer von: `replace`, `add`, `remove`. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `selected` | Mit `all` oder `none`: `all` beziehungsweise `none`. |
| `selectedCount` | Mit `mode` gleich `replace` oder `add`: Anzahl der Ziele, die nach dem Aufruf ausgewählt sind (bei `add` einschließlich zuvor ausgewählter Ziele). Ein Objekt, das `criteria` entspricht und in `uuids` steht, oder eine doppelt aufgeführte UUID wird jedes Mal mitgezählt. |
| `deselectedCount` | Mit `mode` gleich `remove`: Anzahl der abgewählten Zielobjekte; zuvor nicht ausgewählte Objekte werden nicht mitgezählt. |


### editSelection

Verschiebt, dreht, skaliert, dupliziert, gruppiert, löscht oder klassifiziert die Auswahl neu.

> **Auswirkung:** Bearbeiten · **Risiko:** medium · **Rückgängig:** ein Schritt „MCP: editSelection“ · **In runToolBatch:** ja

**Details**

Wirkt auf die gesamte Auswahl der Arbeitsebenen (siehe `workingLayers` in getSelection). `action`: move (benötigt `offset`), rotate (`angle` im Bogenmaß, `center`), scale (`scaleX`,`scaleY`,`center`), duplicate (`offset`), group, delete oder setClass (`class`; `useClassAttributes` legt außerdem alle Objektattribute auf „nach Klasse“ fest). `group` verschiebt die ausgewählten Objekte in eine neue Gruppe auf der aktiven Ebene (oder in die Gruppe/Symboldefinition, die gerade bearbeitet wird), wählt die Gruppe aus und gibt sie mit `groupedCount` zurück. Ausgewählte Objekte, die eine Gruppe nicht aufnehmen kann, z. B. in Wände eingesetzte Türen und Fenster sowie Mitglieder eines Plug-in-Objekts oder eines Dachs, bleiben an ihrem Platz (`ungroupedCount`). Wenn kein ausgewähltes Objekt gruppiert werden kann, schlägt der Aufruf fehl und ändert nichts.

Bearbeiten &gt; Rückgängig macht die Gruppierung rückgängig, setzt die Objekte an ihre vorherige Position zurück und entfernt die Gruppe.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `action` | string | Ja | Einer von: `move`, `rotate`, `scale`, `duplicate`, `group`, `delete`, `setClass`. |
| `offset` | [Punkt](Common.md#punkte) |  | Nur für `move` und `duplicate`: Verschiebungsabstand in Welteinheiten. Standard: (0,0). |
| `angle` | number |  | Winkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `center` | [Punkt](Common.md#punkte) |  | Mittelpunkt. |
| `scaleX` | number |  | Nur für `scale`: Skalierungsfaktor entlang der x-Achse. Standard: 1. Ein Faktor von 0 schlägt fehl (`ok` ist dann `false`). |
| `scaleY` | number |  | Nur für `scale`: Skalierungsfaktor entlang der y-Achse. Standard: 1. Ein Faktor von 0 schlägt fehl (`ok` ist dann `false`). |
| `class` | string |  | Nur für `setClass`: Name einer vorhandenen Klasse. |
| `useClassAttributes` | boolean |  | Nur für `setClass`: Mit `true` werden außerdem alle Objektattribute anhand der Klasse festgelegt. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `ok` | Bei `move`, `rotate`, `scale` und `duplicate`: `true`, wenn Vectorworks die Aktion angewendet hat; `false` (ohne `err`), wenn auf den Arbeitsebenen nichts ausgewählt ist. Bei `setClass`: `true`, wenn jedes ausgewählte Objekt die Klasse übernommen hat, auch wenn nichts ausgewählt ist. Nach `duplicate` sind die neuen Kopien ausgewählt. |
| `deletedCount` | Bei `delete`: Anzahl der gelöschten Objekte; `0`, wenn nichts ausgewählt ist. |
| object reference, `groupedCount`, `ungroupedCount` | Bei `group`: die neue Gruppe als [Objektreferenz](Common.md#objektreferenzen), die Anzahl der in sie verschobenen Objekte und – nur wenn Objekte an ihrem bisherigen Ort bleiben – `ungroupedCount`. Die Gruppe ist anschließend ausgewählt. |
