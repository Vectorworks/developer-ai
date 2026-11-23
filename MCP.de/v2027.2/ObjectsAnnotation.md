[English](../../MCP/v2027.2/ObjectsAnnotation.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/ObjectsAnnotation.md)

# ObjectsAnnotation — Beschriftungen und Bemaßungen

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Inhaltsverzeichnis](README.md)

Werkzeuge für Beschriftungen: Datenstempel, Plankopf-Rahmen und Plankopf-Projektdaten sowie Bemaßungen mit Mittelpunktmarkierungen.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Annotation](#annotation)
  - [createDataTag](#createdatatag)
  - [createTitleBlock](#createtitleblock)
  - [getAnnotationObject](#getannotationobject)
  - [setAnnotationObject](#setannotationobject)
  - [tagObject](#tagobject)
  - [getObjectTags](#getobjecttags)
  - [getProjectData](#getprojectdata)
  - [setProjectData](#setprojectdata)
- [Dimensioning](#dimensioning)
  - [createLinearDimension](#createlineardimension)
  - [createAngularDimension](#createangulardimension)
  - [createArcLengthDimension](#createarclengthdimension)
  - [createRadialDimension](#createradialdimension)
  - [createCenterMark](#createcentermark)
  - [getDimension](#getdimension)
  - [setDimension](#setdimension)
  - [getObjectDimensions](#getobjectdimensions)

## Überblick

Dieser Ordner enthält 2 Werkzeuggruppen mit insgesamt 16 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Sicherheitsstufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [Annotation](#annotation) | `annotation` | Nein | mittel | 8 | Datenstempel, Plankopf-Rahmen und die Plankopf-Projektdaten des Dokuments. |
| [Dimensioning](#dimensioning) | `dimensioning` | Nein | mittel | 8 | Lineare, Winkel-, Bogenlängen- und Radiusbemaßungen sowie Mittelpunktmarkierungen. |

## Annotation

> **Gruppe:** `Annotation` · **Gruppen-ID:** `annotation` · **Standardmäßig aktiv:** Nein · **Sicherheitsstufe:** mittel · **Werkzeuge:** 8

**Datenstempel, Plankopf-Rahmen und die Plankopf-Projektdaten des Dokuments.**

Die Zeichnung mit Datenstempeln und Plankopf-Rahmen beschriften. Ein Datenstempel beschriftet ein Objekt mit daraus ausgelesenen Daten (Datensatzfelder, Plug-in-Parameter, Klasse usw.); ein Plankopf-Rahmen zeichnet den Blattrahmen, das Raster und den Plankopf, in dem Projekt-, Blatt-, Revisions- und Ausgabedaten gedruckt werden. Beide Objekte übernehmen ihre grafische Darstellung aus einem Objektstil, den diese Werkzeuge bei Bedarf aus dem Vectorworks-Inhalt importieren.

Jede Änderung wird als eigener benannter, rückgängig zu machender Vectorworks-Vorgang ausgeführt.

| Werkzeug | Auswirkung | Sicherheitsstufe | Zusammenfassung |
|---|---|---|---|
| [`createDataTag`](#createdatatag) | Bearbeiten | mittel | Erstellt einen Datenstempel, optional einem Objekt zugeordnet. |
| [`createTitleBlock`](#createtitleblock) | Bearbeiten | mittel | Erstellt einen Plankopf-Rahmen. |
| [`getAnnotationObject`](#getannotationobject) | Nur lesend | niedrig | Liest einen Datenstempel oder Plankopf-Rahmen aus. |
| [`setAnnotationObject`](#setannotationobject) | Bearbeiten | mittel | Bearbeitet einen Datenstempel oder Plankopf-Rahmen. |
| [`tagObject`](#tagobject) | Bearbeiten | mittel | Ordnet einem Objekt einen Datenstempel zu oder löst die Zuordnung. |
| [`getObjectTags`](#getobjecttags) | Nur lesend | niedrig | Listet die einem Objekt zugeordneten Datenstempel auf. |
| [`getProjectData`](#getprojectdata) | Nur lesend | niedrig | Liest die Plankopf-Projektdaten des Dokuments aus. |
| [`setProjectData`](#setprojectdata) | Bearbeiten | mittel | Schreibt die Plankopf-Projektdaten des Dokuments. |

### createDataTag

Erstellt einen Datenstempel, optional einem Objekt zugeordnet.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: createDataTag" · **Bei runToolBatch:** Ja

**Details**

Erstellt einen Datenstempel an `position`. `taggedObjectUuid` gibt das Objekt an, aus dem der Datenstempel seine Daten ausliest (ohne Angabe bleibt er zunächst leer; später mit tagObject zuweisen). Das optionale `style` benennt den Datenstempelstil (eine Symboldefinition), der das Textlayout des Stempels vorgibt; wenn der Stil noch nicht in der Zeichnung vorhanden ist, wird er aus dem Vectorworks-Inhalt importiert. Wird der Stil ausgelassen oder nicht gefunden, wird ein verfügbarer Stil verwendet – der tatsächlich angewendete Stil wird unter `style` zurückgegeben.

Optional sind `useLeader`, `leaderLength`, `leaderAngle` (Bogenmaß), `leaderEnd` (der Punkt, auf den die Hinweislinie zeigt) und rohe Plug-in-`params`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `taggedObjectUuid` | string |  | UUID des Objekts, dessen Daten das Daten-Tag ausliest. Nur UUIDs werden akzeptiert. |
| `style` | string |  | Eine Symboldefinition. |
| `useLeader` | boolean |  | Gibt an, ob das Daten-Tag eine Führungslinie hat. |
| `leaderLength` | number |  | Länge der Führungslinie in Welteinheiten. |
| `leaderAngle` | number |  | Bogenmaß. |
| `leaderEnd` | [Punkt](Common.md#punkte) |  | Der Punkt, auf den die Hinweislinie zeigt. |
| `params` | object |  | Rohe Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `style` | Name des angewendeten Stils. Weicht vom angeforderten `style` ab, wenn dieser nicht gefunden wurde. Wird ausgelassen, wenn der Name nicht gelesen werden kann. |
| `taggedObject` | Referenz des Objekts, an das das Daten-Tag angefügt ist. Nur vorhanden, wenn eine Verknüpfung besteht. |


### createTitleBlock

Erstellt einen Plankopf-Rahmen.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: createTitleBlock" · **Bei runToolBatch:** Ja

**Details**

Erstellt einen Plankopf-Rahmen an `position`, normalerweise auf einer Layoutebene. Das optionale `style` benennt den Plankopf-Rahmenstil, der die Plankopfgrafik vorgibt; wenn der Stil noch nicht in der Zeichnung vorhanden ist, wird er aus dem Vectorworks-Plankopf-Inhalt importiert. Wird der Stil ausgelassen oder nicht gefunden, wird ein verfügbarer Stil verwendet – der tatsächlich angewendete Stil wird unter `style` zurückgegeben.

Optional sind `sheetSize` (z. B. "ANSI D", "ISO A1"), `sheetWidth`/`sheetHeight` für eine benutzerdefinierte Größe, `showGrids`, ein Objekt `sheetData` mit Feldnamen/Wert-Paaren (Blatttitel, Blattnummer, gezeichnet von usw.) und rohe Plug-in-`params`.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `style` | string |  | Name des Plankopf-Rahmenstils (einer Symboldefinition). Wird bei Bedarf aus dem Plankopf-Inhalt von Vectorworks importiert. Wenn der Stil fehlt oder nicht gefunden wird, wird ein verfügbarer Stil verwendet. |
| `sheetSize` | string |  | Name eines vordefinierten Blattformats, zum Beispiel `ANSI D` oder `ISO A1`. |
| `sheetWidth` | number |  | Breite eines benutzerdefinierten Blattformats in Welteinheiten. Nur relevant, wenn das Objekt ein benutzerdefiniertes Format verwendet. |
| `sheetHeight` | number |  | Höhe eines benutzerdefinierten Blattformats in Welteinheiten. Nur relevant, wenn das Objekt ein benutzerdefiniertes Format verwendet. |
| `showGrids` | boolean |  | Gibt an, ob die Raster der Blattzonen angezeigt werden. |
| `sheetData` | object |  | Blattdaten `{ "<field name>": value }`. Geschrieben werden nur Felder des Blattdatenformats des Dokuments; [`getAnnotationObject`](#getannotationobject) führt sie als `sheetDataFieldNames` auf. Ein Wert, der keine Zeichenfolge ist, wird als JSON-Text gespeichert. |
| `params` | object |  | Rohe Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

Die Objektreferenz des neuen Plankopf-Rahmens (siehe [Objektreferenzen](Common.md#objektreferenzen)) und `style`, der Name des angewendeten Stils. Weicht vom angeforderten `style` ab, wenn dieser nicht gefunden wurde; wird ausgelassen, wenn der Name nicht gelesen werden kann. Es gibt kein `applied`. Fehler: `failed to create title block border: no title block border style is available in the drawing or in the Vectorworks content (a title block needs a style to get its graphics from)`. Ein fehlgeschlagener Aufruf wird zurückgerollt (`rolledBack`).


### getAnnotationObject

Liest einen Datenstempel oder Plankopf-Rahmen aus.

> **Auswirkung:** Nur lesend · **Sicherheitsstufe:** niedrig · **Rückgängig:** keiner · **Bei runToolBatch:** Zulässig

**Details**

Liest einen Datenstempel oder Plankopf-Rahmen anhand von UUID, Name oder Index aus. Beide melden den Namen `style`, `isStyled` und die Stilressource (eine Symboldefinition) unter `styleResource`. Ein Datenstempel meldet seine Hinweislinie (`useLeader`, `leaderType`, `leaderLength`, `leaderAngle`, `shoulderLength`, `useMarker`, `leaderEnd`), seine Platzierung (`offset`, `horizontalPosition`, `moveBehaviour`, `alignToWalls`), Eignungskriterien, das beschriftete Objekt und die aktuell gedruckten `data`.

Ein Plankopf-Rahmen meldet seine Blattgröße und `margins`, das Raster (`showGrids`, `horizontalZones`, `verticalZones`, `drawCropMarks`), `useAsTitleBlock`, `isActiveTitleBlock`, den Nordpfeil (`displayNorthArrow`, `northAngle`), den Zeichnungsstempel (`displayDrawingStamp`, `drawingStampText`), Blatt-ID, -titel und -datum, `sheetData` mit den `sheetDataFieldNames` des Blattdatensatzformats sowie die `projectData` und `revisions` des Dokuments.

Einstellungen verwenden dieselben Schlüssel, Einheiten und Enum-Werte wie setAnnotationObject.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `kind` | `DataTag` oder `TitleBlockBorder`. |
| `style`, `isStyled`, `styleResource` | The style name, whether the object is styled, and the style resource (a symbol definition). |
| `taggedObject` | Nur für Daten-Tags und nur bei bestehender Verknüpfung: Referenz des markierten Objekts. |
| `data` | Nur für Daten-Tags: `{ "<label>": "<printed text>" }`, die aktuell vom Tag ausgegebenen Daten. |
| `sheetID`, `sheetTitle`, `sheetDate` | Title block border only. |
| `latestIssueDate` | Nur für Plankopf-Rahmen und nur, wenn eine Ausgabe erstellt wurde. |
| `sheetData` | Nur für Plankopf-Rahmen: `{ "<field>": "<value>" }` des Blattdatenformats. `sheetDataFieldNames` listet die Feldnamen auf. |
| `projectData` | Nur für Plankopf-Rahmen: dokumentweite Projektdaten, dieselben `projectData`, die [`getProjectData`](#getprojectdata) zurückgibt. |
| `revisions` | Nur für Plankopf-Rahmen: Array aus `{ number, date, note, publishDate, recipients }`. |


### setAnnotationObject

Bearbeitet einen Datenstempel oder Plankopf-Rahmen.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: setAnnotationObject" · **Bei runToolBatch:** Ja

**Details**

Bearbeitet einen Datenstempel oder Plankopf-Rahmen anhand von UUID.

**Beide Arten:** `style` (wird bei Bedarf importiert) oder `removeStyle`: true, um das Objekt vom Stil zu lösen – dies wird zuerst angewendet; danach behält jeder Parameter seinen aktuellen Wert und kann für die einzelne Instanz bearbeitet werden.

**Datenstempel:** `useLeader`, `leaderType`, `leaderLength`, `leaderAngle` (Bogenmaß), `shoulderLength`, `useMarker` (Markierung am Ende der Hinweislinie), `leaderEnd`, `offset`, `horizontalPosition` (Seite der Hinweislinie, auf der der Text steht), `moveBehaviour` (was beim Ziehen des Stempels verschoben wird), `alignToWalls`, `useCriteria`, `criteria`.

**Plankopf-Rahmen:** `sheetSize`, `sheetWidth`, `sheetHeight`, `margins` (eine ausgelassene Seite behält ihren Wert), `showGrids`, `horizontalZones`, `verticalZones`, `drawCropMarks`, `useAsTitleBlock`, `isActiveTitleBlock` (der Plankopf, dessen Blattdaten das Dokument ausliest; einer je Blatt), `displayNorthArrow`, `northAngle` (Bogenmaß), `displayDrawingStamp`, `drawingStampText` (wird gedruckt, wenn der Parameter 'Stamp Text' den benutzerdefinierten Eintrag auswählt), die Objekte `sheetData` und `projectData` mit Feldnamen/Wert-Paaren. Ein Objekt `params` legt rohe Plug-in-Parameter fest. `applied` gibt für jede Einstellung an, ob sie geschrieben wurde.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `style` | string |  | Wird bei Bedarf importiert. |
| `useLeader` | boolean |  | Wird für Datenstempel verwendet. |
| `leaderLength` | number |  | Wird für Datenstempel verwendet. |
| `leaderAngle` | number |  | Wird für Datenstempel verwendet. Bogenmaß. |
| `shoulderLength` | number |  | Wird für Datenstempel verwendet. |
| `leaderEnd` | [Punkt](Common.md#punkte) |  | Wird für Datenstempel verwendet. |
| `offset` | [Punkt](Common.md#punkte) |  | Wird für Datenstempel verwendet. |
| `useCriteria` | boolean |  | Wird für Datenstempel verwendet. |
| `criteria` | string |  | Wird für Datenstempel verwendet. |
| `removeStyle` | boolean |  | Für beide Objekttypen. `true` löst das Objekt vor dem Schreiben der übrigen Einstellungen von seinem Stil: Jeder Parameter behält seinen Wert und kann danach für die Instanz bearbeitet werden. `false` bewirkt nichts. Ein `style` im selben Aufruf wendet erneut einen Stil an. |
| `leaderType` | string |  | Wird für Datenstempel verwendet. Einer von: `line`, `arc`, `bezier`. |
| `useMarker` | boolean |  | Wird für Datenstempel verwendet. Markierung am Ende der Hinweislinie. |
| `horizontalPosition` | string |  | Wird für Datenstempel verwendet. Einer von: `left`, `right`, `auto`. |
| `moveBehaviour` | string |  | Wird für Datenstempel verwendet. Einer von: `entireTag`, `leaderEnd`. |
| `alignToWalls` | boolean |  | Wird für Datenstempel verwendet. |
| `sheetSize` | string |  | Wird für Plankopf-Rahmen verwendet. |
| `sheetWidth` | number |  | Wird für Plankopf-Rahmen verwendet. |
| `sheetHeight` | number |  | Wird für Plankopf-Rahmen verwendet. |
| `showGrids` | boolean |  | Wird für Plankopf-Rahmen verwendet. |
| `horizontalZones` | integer |  | Wird für Plankopf-Rahmen verwendet. |
| `verticalZones` | integer |  | Wird für Plankopf-Rahmen verwendet. |
| `useAsTitleBlock` | boolean |  | Wird für Plankopf-Rahmen verwendet. |
| `northAngle` | number |  | Wird für Plankopf-Rahmen verwendet. Bogenmaß. |
| `margins` | [Rechteck](Common.md#rechtecke) |  | Wird für Plankopf-Rahmen verwendet. Eine ausgelassene Seite behält ihren Wert. |
| `drawCropMarks` | boolean |  | Wird für Plankopf-Rahmen verwendet. |
| `isActiveTitleBlock` | boolean |  | Wird für Plankopf-Rahmen verwendet. Der Plankopf, dessen Blattdaten das Dokument ausliest; einer je Blatt. |
| `displayNorthArrow` | boolean |  | Wird für Plankopf-Rahmen verwendet. |
| `displayDrawingStamp` | boolean |  | Wird für Plankopf-Rahmen verwendet. |
| `drawingStampText` | string |  | Wird für Plankopf-Rahmen verwendet. Wird gedruckt, wenn der Parameter 'Stamp Text' den benutzerdefinierten Eintrag auswählt. |
| `sheetData` | object |  | Wird für Plankopf-Rahmen verwendet. |
| `projectData` | object |  | Für den Plankopf-Rahmen. Name-Wert-Paare der dokumentweiten Projektdaten, die alle Planköpfe gemeinsam haben. Schreibt dieselben Daten wie [`setProjectData`](#setprojectdata): Nur Felder des Projektdatenformats werden geschrieben; Werte, die keine Zeichenfolgen sind, werden als JSON-Text gespeichert. |
| `params` | object |  | Rohe Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |

**Ergebnis**

| Eintrag | Beschreibung |
|---|---|
| `<setting>` | `true`, wenn Vectorworks den Wert übernommen hat; `false`, wenn der Wert abgelehnt oder nicht in den Typ der Einstellung konvertiert werden konnte. |
| `removeStyle` | Nur wenn `removeStyle` `true` war: Gibt an, ob das Objekt von seinem Stil gelöst wurde. |
| `sheetData` | Nur für Plankopf-Rahmen: `{ "<field name>": true or false }`, ein Eintrag pro angegebenem Feld. |
| `projectData` | Nur für Plankopf-Rahmen: dasselbe für die Projektdaten. |
| `params` | `{ "<name>": true or false }` für die rohen Plug-in-Parameter. |


### tagObject

Ordnet einem Objekt einen Datenstempel zu oder löst die Zuordnung.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: tagObject" · **Bei runToolBatch:** Ja

**Details**

Ordnet den anhand von UUID/Name/Index angegebenen Datenstempel dem durch `objectUuid` angegebenen Objekt zu, damit der Stempel seine Daten daraus ausliest, oder löst die Zuordnung mit `action` gleich "detach" wieder.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `objectUuid` | string |  | UUID des Zielobjekts. |
| `action` | string |  | Einer von: `attach`, `detach`. |

**Ergebnis**

| Aktion | Ergebnis |
|---|---|
| attach | `{ "attached": true, "taggedObject": <object reference> }`. The tag now reads its data from the object; its former association is replaced. |
| detach | `{ "detached": <boolean> }`: `true` when the tag had a tagged object to detach (Vectorworks does not report whether it detached it); `false` when it had none. |


### getObjectTags

Listet die einem Objekt zugeordneten Datenstempel auf.

> **Auswirkung:** Nur lesend · **Sicherheitsstufe:** niedrig · **Rückgängig:** keiner · **Bei runToolBatch:** Zulässig

**Details**

Listet die Datenstempel auf, die dem anhand von UUID, Name oder Index angegebenen Objekt zugeordnet sind, und meldet, ob Objekte dieser Art überhaupt beschriftet werden können.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `object` | Objektreferenz (siehe [Objektreferenzen](Common.md#objektreferenzen)). |
| `canBeTagged` | Gibt an, ob ein Daten-Tag an Objekte dieser Art angefügt werden kann. |
| `tags` | Array der Referenzen von Daten-Tags, die an das Objekt angefügt sind; leer, wenn keine vorhanden sind. |


### getProjectData

Liest die Plankopf-Projektdaten des Dokuments aus.

> **Auswirkung:** Nur lesend · **Sicherheitsstufe:** niedrig · **Rückgängig:** keiner · **Bei runToolBatch:** Zulässig

**Details**

Liest die Plankopf-Projektdaten des Dokuments aus: benannte Felder, die von allen Planköpfen gemeinsam verwendet werden, z. B. Projektname, Auftraggeber und Adresse. Gibt `projectData` (Feldnamen/Wert-Paare) und `projectDataFieldNames` (die Felder des Projekt-Datenformats des Dokuments in der Formatreihenfolge) zurück. Das Werkzeug benötigt keine Argumente.

**Parameter**

Dieses Werkzeug benötigt keine Parameter.

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `projectData` | Name-Wert-Paare der Projektdaten. |
| `projectDataFieldNames` | Array der Feldnamen des Projektdatenformats in Formatreihenfolge. |


### setProjectData

Schreibt die Plankopf-Projektdaten des Dokuments.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: setProjectData" · **Bei runToolBatch:** Ja

**Details**

Schreibt die Plankopf-Projektdaten des Dokuments. `projectData` ist ein Objekt aus Feldnamen/Wert-Paaren; es werden nur Felder geschrieben, die bereits im Projekt-Datenformat vorhanden sind (siehe getProjectData). Anschließend werden alle Planköpfe in der Zeichnung aktualisiert.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `projectData` | object | Ja | Name-Wert-Paare der Felder `{ "<field name>": value }`. Geschrieben werden nur Felder des Projektdatenformats (siehe [`getProjectData`](#getprojectdata)). Werte, die keine Zeichenfolgen sind, werden als JSON-Text gespeichert. |

**Ergebnis**

`{ "applied": { "<field name>": true or false } }`, ein Eintrag pro angegebenem Feld. Ein Feld, das nicht im Projektdatenformat vorkommt, hat den Wert `false` und wird nicht erstellt. Fehler: `provide 'projectData' as an object of field name / value pairs` (das Argument fehlt oder ist kein Objekt). Ein fehlgeschlagener Aufruf wird zurückgerollt (`rolledBack`).


## Dimensioning

> **Gruppe:** `Dimensioning` · **Gruppen-ID:** `dimensioning` · **Standardmäßig aktiv:** Nein · **Sicherheitsstufe:** mittel · **Werkzeuge:** 8

**Lineare, Winkel-, Bogenlängen- und Radiusbemaßungen sowie Mittelpunktmarkierungen.**

Die Zeichnung mit Bemaßungen versehen: lineare (gebundene, horizontale, vertikale, ungebundene/schräge und Ordinatenbemaßungen), Winkel-, Bogenlängen- und Radius-/Durchmesserbemaßungen sowie Mittelpunktmarkierungen. Eine Bemaßung ist ein natives Vectorworks-Objekt, kein Plug-in-Objekt: Sie misst zwei Weltpunkte (bei einer Winkelbemaßung einen Eckpunkt und zwei Schenkel, bei einer Radiusbemaßung einen Mittelpunkt und einen Kreis) und gibt den Messwert anhand eines Bemaßungsstandards aus.

Die Art einer Bemaßung wird beim Erstellen festgelegt – eine lineare Bemaßung kann nicht nachträglich zu einer Winkelbemaßung werden. Wählen Sie daher von Anfang an das passende Erstellungswerkzeug. Der Bemaßungsstandard (eine im Dokument gespeicherte ISO-/ANSI-/Architektur- oder benutzerdefinierte Vorgabe) bestimmt die Maßlinien-Endmarkierungen, Hilfslinienlängen, Textgröße und Formatierung des Werts. Diese Längen sind Papiermaße, sodass eine Bemaßung unabhängig vom Ebenenmaßstab dieselbe Druckgröße beibehält; `offset`, Punktkoordinaten und Messwert werden immer in Welteinheiten angegeben.

Mit `unit` wird festgelegt, welche Dokumenteinstellung für Bemaßungseinheiten den Wert formatiert. Text kann mit `leaderText`/`trailerText`/`noteText` ersetzt oder ergänzt werden; außerdem kann neben dem ersten Wert ein zweiter Wert in einer sekundären Einheit ausgegeben werden. Eine Bemaßung kann assoziativ sein: Mit `associate` wird sie an die Geometrie unter ihren Endpunkten gebunden (`associateSelectedOnly` beschränkt dies auf die ausgewählten Objekte) und folgt ihr, wenn diese Geometrie verschoben wird.

Alle Winkel in dieser Gruppe werden im Bogenmaß angegeben. Eine Mittelpunktmarkierung ist kein Bemaßungsobjekt, sondern eine Gruppe von Liniensegmenten in der Bemaßungsklasse; sie wird daher mit den allgemeinen Objektwerkzeugen ausgelesen und bearbeitet. Jede Änderung wird als eigener benannter, rückgängig zu machender Vectorworks-Vorgang ausgeführt. Die Erstellungswerkzeuge geben außerdem `applied` (true/false je geschriebener Einstellung, einschließlich `associate`) zurück, wenn Einstellungen angegeben wurden.

| Werkzeug | Auswirkung | Sicherheitsstufe | Zusammenfassung |
|---|---|---|---|
| [`createLinearDimension`](#createlineardimension) | Bearbeiten | mittel | Erstellt eine gebundene, horizontale, vertikale, ungebundene oder Ordinatenbemaßung. |
| [`createAngularDimension`](#createangulardimension) | Bearbeiten | mittel | Erstellt eine Winkelbemaßung. |
| [`createArcLengthDimension`](#createarclengthdimension) | Bearbeiten | mittel | Erstellt eine Bogenlängenbemaßung. |
| [`createRadialDimension`](#createradialdimension) | Bearbeiten | mittel | Erstellt eine Radius- oder Durchmesserbemaßung. |
| [`createCenterMark`](#createcentermark) | Bearbeiten | mittel | Erstellt eine Mittelpunktmarkierung für ein rundes Element. |
| [`getDimension`](#getdimension) | Nur lesend | niedrig | Liest Art, Messpunkte, Wert und Texteinstellungen einer Bemaßung aus. |
| [`setDimension`](#setdimension) | Bearbeiten | mittel | Bearbeitet eine Bemaßung. |
| [`getObjectDimensions`](#getobjectdimensions) | Nur lesend | niedrig | Listet die einem Objekt zugeordneten Bemaßungen auf. |

### createLinearDimension

Erstellt eine gebundene, horizontale, vertikale, ungebundene oder Ordinatenbemaßung.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: createLinearDimension" · **Bei runToolBatch:** Ja

**Details**

Erstellt eine lineare Bemaßung des Abstands zwischen `start` und `end`; die Maßlinie liegt im Abstand `offset` (Welteinheiten) von den Punkten. `mode` legt die Art fest: "constrained" (Standardwert) misst den auf eine feste Richtung projizierten Abstand – `angle` (Bogenmaß) gibt diese Richtung an, andernfalls folgt sie von start nach end; "horizontal" und "vertical" sind die achsenparallelen Kurzformen; "unconstrained" (schräg) misst den tatsächlichen Abstand entlang start → end; "ordinate" misst `end` vom Bezugspunkt `start` entlang `angle`.

Die beiden Punkte dürfen nicht zusammenfallen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `start` | [Punkt](Common.md#punkte) | Ja | Erster Messpunkt in Welteinheiten. |
| `end` | [Punkt](Common.md#punkte) | Ja | Zweiter Messpunkt in Welteinheiten. |
| `offset` | number |  | Abstand der Maßlinie von der Messgeometrie in Welteinheiten. |
| `angle` | number |  | Winkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `mode` | string |  | Einer von: `constrained`, `horizontal`, `vertical`, `unconstrained`, `ordinate`. |
| `startWitness` | boolean |  | Hilfslinie am Anfang anzeigen. |
| `endWitness` | boolean |  | Hilfslinie am Ende anzeigen. |
| `witnessOverride` | integer |  | Hilfslinien: 0 gemäß Standard, 1 eine benutzerdefinierte Länge, 2 Länge je Hilfslinie, 3 einen benutzerdefinierten Abstand, 4 Abstand je Hilfslinie. |
| `startWitnessLength` | number |  | Benutzerdefinierte Länge der Hilfslinie am Anfang. |
| `endWitnessLength` | number |  | Benutzerdefinierte Länge der Hilfslinie am Ende. |
| `startWitnessOffset` | number |  | Benutzerdefinierter Abstand der Hilfslinie am Anfang. |
| `endWitnessOffset` | number |  | Benutzerdefinierter Abstand der Hilfslinie am Ende. |
| `arrowsInside` | boolean |  | Pfeile innerhalb der Hilfslinien platzieren. |
| `leaderLine` | boolean |  | Maßlinie anzeigen. |
| `showValue` | boolean |  | Messwert ausgeben. |
| `leaderText` | string |  | Vor dem Wert ausgegebener Text. |
| `trailerText` | string |  | Nach dem Wert ausgegebener Text. |
| `boxText` | boolean |  | Wert mit einem Rahmen versehen. |
| `precision` | integer |  | Dezimalstellen; Bruchmaße: 0–6 = 1/1 bis 1/64; Winkel: 1 Grad, 2 Grad/Minute, 3 Grad/Minute/Sekunde. |
| `showSecondaryValue` | boolean |  | Wert zusätzlich in der sekundären Einheit ausgeben. |
| `secondaryLeaderText` | string |  | Vor dem sekundären Wert ausgegebener Text. |
| `secondaryTrailerText` | string |  | Nach dem sekundären Wert ausgegebener Text. |
| `secondaryBoxText` | boolean |  | Sekundären Wert mit einem Rahmen versehen. |
| `secondaryPrecision` | integer |  | Genauigkeit des sekundären Werts (wie `precision`). |
| `noteText` | string |  | Der Bemaßung hinzugefügter Hinweistext. |
| `textPositionAutomatic` | boolean |  | Textposition automatisch festlegen. |
| `textInside` | boolean |  | Text innerhalb der Hilfslinien platzieren. |
| `textFlipped` | boolean |  | Text spiegeln. |
| `textRotation` | integer |  | Textdrehung: 0 ausgerichtet, 1 horizontal, 2 horizontal/vertikal. |
| `textOffsetAlongLine` | number |  | Textabstand entlang der Maßlinie. |
| `textOffsetAboveLine` | number |  | Textabstand oberhalb der Maßlinie. |
| `fontSize` | number |  | Schriftgröße in Punkten. |
| `fontStyle` | integer |  | Summe aus 1 fett, 2 kursiv, 4 unterstrichen. |
| `textStyle` | string |  | Name oder Ressourcen-UUID eines Textstils; eine leere Zeichenfolge bedeutet keinen Stil. |
| `toleranceType` | integer |  | Toleranz: 0 keine, 1 einfach, 2 doppelt, 3 Grenzmaß. |
| `tolerancePlus` | number |  | Oberer Toleranzwert. |
| `toleranceMinus` | number |  | Unterer Toleranzwert. |
| `standard` | string |  | Name des Bemaßungsstandards. |
| `standardIndex` | integer |  | Bemaßungsstandard nach Index: größer 0 integriert, kleiner 0 benutzerdefiniert. |
| `unit` | integer |  | 0 für Dokumenteinheiten, andernfalls der Index einer Einstellung für Bemaßungseinheiten. |
| `associate` | boolean |  | Bemaßung an die Geometrie unter ihren Endpunkten binden. |
| `associateSelectedOnly` | boolean |  | Mit `associate`: nur an ausgewählte Objekte binden. |
| `params` | object |  | Rohe Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `value` | Ausgegebener Wert: Abstand zwischen den Punkten, bei einer eingeschränkten Bemaßung auf die Richtung der Maßlinie projiziert. |
| `direction` | Richtung der Maßlinie in Radiant von der X-Achse (bei uneingeschränkter Bemaßung von `start` nach `end`). |
| `applied` | Für jede geschriebene Einstellung; `start` und `end` werden gemeinsam als `points` gemeldet. |


### createAngularDimension

Erstellt eine Winkelbemaßung.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: createAngularDimension" · **Bei runToolBatch:** Ja

**Details**

Erstellt am `vertex` eine Winkelbemaßung des gegen den Uhrzeigersinn gemessenen Winkels zwischen den beiden Schenkeln; der Bogen liegt im Abstand `offset` (Welteinheiten) vom Eckpunkt. Die Schenkel werden entweder als `firstLegPoint`/`secondLegPoint` (ein beliebiger Punkt auf dem jeweiligen Schenkel) oder als `startAngle`/`endAngle` im Bogenmaß zusammen mit einer `legLength` angegeben. Bei `referenceAngle` true misst die Bemaßung einen einzelnen Schenkel zum Bezugswinkel und zeichnet nur eine Hilfslinie. Der Messwert wird als `value` im Bogenmaß zurückgegeben.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `vertex` | [Punkt](Common.md#punkte) | Ja | Bei Winkelbemaßungen: der Eckpunkt des Winkels. |
| `firstLegPoint` | [Punkt](Common.md#punkte) |  | Beliebiger Punkt auf dem ersten Schenkel. |
| `secondLegPoint` | [Punkt](Common.md#punkte) |  | Ein beliebiger Punkt auf dem jeweiligen Schenkel. |
| `startAngle` | number |  | Startwinkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `endAngle` | number |  | Endwinkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `legLength` | number |  | Bei Angabe von `startAngle` und `endAngle`: Schenkellänge in Welteinheiten. Standard 1; muss größer als 0 sein. |
| `offset` | number |  | Abstand der Maßlinie von der Messgeometrie in Welteinheiten. |
| `referenceAngle` | boolean |  | Bei Winkelbemaßungen: einen einzelnen Schenkel zum Bezugswinkel messen. |
| `startWitness` | boolean |  | Hilfslinie am Anfang anzeigen. |
| `endWitness` | boolean |  | Hilfslinie am Ende anzeigen. |
| `witnessOverride` | integer |  | Hilfslinien: 0 gemäß Standard, 1 eine benutzerdefinierte Länge, 2 Länge je Hilfslinie, 3 einen benutzerdefinierten Abstand, 4 Abstand je Hilfslinie. |
| `startWitnessLength` | number |  | Benutzerdefinierte Länge der Hilfslinie am Anfang. |
| `endWitnessLength` | number |  | Benutzerdefinierte Länge der Hilfslinie am Ende. |
| `startWitnessOffset` | number |  | Benutzerdefinierter Abstand der Hilfslinie am Anfang. |
| `endWitnessOffset` | number |  | Benutzerdefinierter Abstand der Hilfslinie am Ende. |
| `arrowsInside` | boolean |  | Pfeile innerhalb der Hilfslinien platzieren. |
| `leaderLine` | boolean |  | Maßlinie anzeigen. |
| `showValue` | boolean |  | Messwert ausgeben. |
| `leaderText` | string |  | Vor dem Wert ausgegebener Text. |
| `trailerText` | string |  | Nach dem Wert ausgegebener Text. |
| `boxText` | boolean |  | Wert mit einem Rahmen versehen. |
| `precision` | integer |  | Dezimalstellen; Bruchmaße: 0–6 = 1/1 bis 1/64; Winkel: 1 Grad, 2 Grad/Minute, 3 Grad/Minute/Sekunde. |
| `showSecondaryValue` | boolean |  | Wert zusätzlich in der sekundären Einheit ausgeben. |
| `secondaryLeaderText` | string |  | Vor dem sekundären Wert ausgegebener Text. |
| `secondaryTrailerText` | string |  | Nach dem sekundären Wert ausgegebener Text. |
| `secondaryBoxText` | boolean |  | Sekundären Wert mit einem Rahmen versehen. |
| `secondaryPrecision` | integer |  | Genauigkeit des sekundären Werts (wie `precision`). |
| `noteText` | string |  | Der Bemaßung hinzugefügter Hinweistext. |
| `textPositionAutomatic` | boolean |  | Textposition automatisch festlegen. |
| `textInside` | boolean |  | Text innerhalb der Hilfslinien platzieren. |
| `textFlipped` | boolean |  | Text spiegeln. |
| `textRotation` | integer |  | Textdrehung: 0 ausgerichtet, 1 horizontal, 2 horizontal/vertikal. |
| `textOffsetAlongLine` | number |  | Textabstand entlang der Maßlinie. |
| `textOffsetAboveLine` | number |  | Textabstand oberhalb der Maßlinie. |
| `fontSize` | number |  | Schriftgröße in Punkten. |
| `fontStyle` | integer |  | Summe aus 1 fett, 2 kursiv, 4 unterstrichen. |
| `textStyle` | string |  | Name oder Ressourcen-UUID eines Textstils; eine leere Zeichenfolge bedeutet keinen Stil. |
| `toleranceType` | integer |  | Toleranz: 0 keine, 1 einfach, 2 doppelt, 3 Grenzmaß. |
| `tolerancePlus` | number |  | Oberer Toleranzwert. |
| `toleranceMinus` | number |  | Unterer Toleranzwert. |
| `standard` | string |  | Name des Bemaßungsstandards. |
| `standardIndex` | integer |  | Bemaßungsstandard nach Index: größer 0 integriert, kleiner 0 benutzerdefiniert. |
| `unit` | integer |  | 0 für Dokumenteinheiten, andernfalls der Index einer Einstellung für Bemaßungseinheiten. |
| `associate` | boolean |  | Bemaßung an die Geometrie unter ihren Endpunkten binden. |
| `associateSelectedOnly` | boolean |  | Mit `associate`: nur an ausgewählte Objekte binden. |
| `params` | object |  | Rohe Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `vertex` | Scheitelpunkt in Welteinheiten. |
| `startAngle` | Anfangswinkel des gemessenen Winkels in Radiant. |
| `endAngle` | Endwinkel des gemessenen Winkels in Radiant. |
| `value` | Gemessener Winkel in Radiant, gegen den Uhrzeigersinn vom ersten zum zweiten Schenkel, im Bereich [0, 2π). |
| `referenceAngle` | Gibt an, ob die Bemaßung relativ zur Bezugsrichtung gemessen wird. |
| `applied` | Für jede geschriebene Einstellung. |


### createArcLengthDimension

Erstellt eine Bogenlängenbemaßung.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: createArcLengthDimension" · **Bei runToolBatch:** Ja

**Details**

Erstellt eine Bogenlängenbemaßung der Länge entlang eines Bogens; der Bemaßungsbogen liegt im Abstand `offset` (Welteinheiten) außerhalb des Bogens. Der Bogen wird entweder mit `start`, `end` und `center` angegeben (`clockwise` bestimmt, welcher der beiden Bögen zwischen den Punkten gemessen wird) oder mit `center`, `radius`, `startAngle` und `sweepAngle` im Bogenmaß (ein negativer Drehwinkel verläuft im Uhrzeigersinn).

`witnessPerpendicularToChord` zeichnet die Hilfslinien senkrecht zur Sehne statt radial; `arcIndicator` (Standardwert true) setzt das Bogensymbol vor den Wert.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `start` | [Punkt](Common.md#punkte) |  | Erster Messpunkt in Welteinheiten. |
| `end` | [Punkt](Common.md#punkte) |  | Zweiter Messpunkt in Welteinheiten. |
| `center` | [Punkt](Common.md#punkte) | Ja | Mit `clockwise` wird festgelegt, welcher der beiden Bögen zwischen den Punkten gemessen wird. |
| `radius` | number |  | Radius in Welteinheiten. |
| `startAngle` | number |  | Startwinkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `sweepAngle` | number |  | Drehwinkel im Bogenmaß; positive Werte drehen gegen den Uhrzeigersinn. |
| `offset` | number |  | Abstand der Maßlinie von der Messgeometrie in Welteinheiten. |
| `clockwise` | boolean |  | Den Bogen zwischen den Punkten im Uhrzeigersinn messen. |
| `witnessPerpendicularToChord` | boolean |  | Hilfslinien senkrecht zur Sehne statt radial zeichnen. Standard `false`. |
| `arcIndicator` | boolean |  | Das Bogensymbol vor dem Wert ausgeben. Standard `true`. |
| `startWitness` | boolean |  | Hilfslinie am Anfang anzeigen. |
| `endWitness` | boolean |  | Hilfslinie am Ende anzeigen. |
| `witnessOverride` | integer |  | Hilfslinien: 0 gemäß Standard, 1 eine benutzerdefinierte Länge, 2 Länge je Hilfslinie, 3 einen benutzerdefinierten Abstand, 4 Abstand je Hilfslinie. |
| `startWitnessLength` | number |  | Benutzerdefinierte Länge der Hilfslinie am Anfang. |
| `endWitnessLength` | number |  | Benutzerdefinierte Länge der Hilfslinie am Ende. |
| `startWitnessOffset` | number |  | Benutzerdefinierter Abstand der Hilfslinie am Anfang. |
| `endWitnessOffset` | number |  | Benutzerdefinierter Abstand der Hilfslinie am Ende. |
| `arrowsInside` | boolean |  | Pfeile innerhalb der Hilfslinien platzieren. |
| `leaderLine` | boolean |  | Maßlinie anzeigen. |
| `showValue` | boolean |  | Messwert ausgeben. |
| `leaderText` | string |  | Vor dem Wert ausgegebener Text. |
| `trailerText` | string |  | Nach dem Wert ausgegebener Text. |
| `boxText` | boolean |  | Wert mit einem Rahmen versehen. |
| `precision` | integer |  | Dezimalstellen; Bruchmaße: 0–6 = 1/1 bis 1/64; Winkel: 1 Grad, 2 Grad/Minute, 3 Grad/Minute/Sekunde. |
| `showSecondaryValue` | boolean |  | Wert zusätzlich in der sekundären Einheit ausgeben. |
| `secondaryLeaderText` | string |  | Vor dem sekundären Wert ausgegebener Text. |
| `secondaryTrailerText` | string |  | Nach dem sekundären Wert ausgegebener Text. |
| `secondaryBoxText` | boolean |  | Sekundären Wert mit einem Rahmen versehen. |
| `secondaryPrecision` | integer |  | Genauigkeit des sekundären Werts (wie `precision`). |
| `noteText` | string |  | Der Bemaßung hinzugefügter Hinweistext. |
| `textPositionAutomatic` | boolean |  | Textposition automatisch festlegen. |
| `textInside` | boolean |  | Text innerhalb der Hilfslinien platzieren. |
| `textFlipped` | boolean |  | Text spiegeln. |
| `textRotation` | integer |  | Textdrehung: 0 ausgerichtet, 1 horizontal, 2 horizontal/vertikal. |
| `textOffsetAlongLine` | number |  | Textabstand entlang der Maßlinie. |
| `textOffsetAboveLine` | number |  | Textabstand oberhalb der Maßlinie. |
| `fontSize` | number |  | Schriftgröße in Punkten. |
| `fontStyle` | integer |  | Summe aus 1 fett, 2 kursiv, 4 unterstrichen. |
| `textStyle` | string |  | Name oder Ressourcen-UUID eines Textstils; eine leere Zeichenfolge bedeutet keinen Stil. |
| `toleranceType` | integer |  | Toleranz: 0 keine, 1 einfach, 2 doppelt, 3 Grenzmaß. |
| `tolerancePlus` | number |  | Oberer Toleranzwert. |
| `toleranceMinus` | number |  | Unterer Toleranzwert. |
| `standard` | string |  | Name des Bemaßungsstandards. |
| `standardIndex` | integer |  | Bemaßungsstandard nach Index: größer 0 integriert, kleiner 0 benutzerdefiniert. |
| `unit` | integer |  | 0 für Dokumenteinheiten, andernfalls der Index einer Einstellung für Bemaßungseinheiten. |
| `associate` | boolean |  | Bemaßung an die Geometrie unter ihren Endpunkten binden. |
| `associateSelectedOnly` | boolean |  | Mit `associate`: nur an ausgewählte Objekte binden. |
| `params` | object |  | Rohe Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `center` | Mittelpunkt des Bogens in Welteinheiten. |
| `radius` | Radius des Bogens in Welteinheiten. |
| `startAngle` | Anfangswinkel des gemessenen Bogens in Radiant. |
| `sweepAngle` | Signierter Winkelbereich des gemessenen Bogens in Radiant (negativ bedeutet im Uhrzeigersinn). |
| `value` | Ausgegebener Wert: Bogenlänge in Welteinheiten. |
| `applied` | Für jede geschriebene Einstellung. |


### createRadialDimension

Erstellt eine Radius- oder Durchmesserbemaßung.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: createRadialDimension" · **Bei runToolBatch:** Ja

**Details**

Erstellt eine Radiusbemaßung für einen Kreis mit Mittelpunkt `center`; die Maßlinie liegt im Abstand `offset` (Welteinheiten) außerhalb des Kreises. `mode` "radial" (Standardwert) gibt den Radius aus, "diametrical" den Kreisdurchmesser. Der Kreis wird entweder mit `radius` (oder `diameter`) und dem Winkel `angle` im Bogenmaß angegeben, in dem die Maßlinie vom Mittelpunkt ausgeht, oder mit `pointOnCircle`, auf den die Maßlinie zeigt. `compact` zeichnet die verkürzte Radiusdarstellung, die am Kreis endet, statt bis zum Mittelpunkt zu verlaufen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `center` | [Punkt](Common.md#punkte) | Ja | Mittelpunkt. |
| `radius` | number |  | Radius in Welteinheiten. |
| `diameter` | number |  | Durchmesser in Welteinheiten. |
| `angle` | number |  | Winkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `pointOnCircle` | [Punkt](Common.md#punkte) |  | Punkt auf dem Kreis, auf den die Führungslinie zeigt, in Welteinheiten. Hat Vorrang vor `radius`, `diameter` und `angle`. |
| `offset` | number |  | Abstand der Maßlinie von der Messgeometrie in Welteinheiten. |
| `compact` | boolean |  | Radiusbemaßungen: verkürzte Darstellung, die am Kreis endet. |
| `mode` | string |  | Einer von: `radial`, `diametrical`. |
| `startWitness` | boolean |  | Hilfslinie am Anfang anzeigen. |
| `endWitness` | boolean |  | Hilfslinie am Ende anzeigen. |
| `witnessOverride` | integer |  | Hilfslinien: 0 gemäß Standard, 1 eine benutzerdefinierte Länge, 2 Länge je Hilfslinie, 3 einen benutzerdefinierten Abstand, 4 Abstand je Hilfslinie. |
| `startWitnessLength` | number |  | Benutzerdefinierte Länge der Hilfslinie am Anfang. |
| `endWitnessLength` | number |  | Benutzerdefinierte Länge der Hilfslinie am Ende. |
| `startWitnessOffset` | number |  | Benutzerdefinierter Abstand der Hilfslinie am Anfang. |
| `endWitnessOffset` | number |  | Benutzerdefinierter Abstand der Hilfslinie am Ende. |
| `arrowsInside` | boolean |  | Pfeile innerhalb der Hilfslinien platzieren. |
| `leaderLine` | boolean |  | Maßlinie anzeigen. |
| `showValue` | boolean |  | Messwert ausgeben. |
| `leaderText` | string |  | Vor dem Wert ausgegebener Text. |
| `trailerText` | string |  | Nach dem Wert ausgegebener Text. |
| `boxText` | boolean |  | Wert mit einem Rahmen versehen. |
| `precision` | integer |  | Dezimalstellen; Bruchmaße: 0–6 = 1/1 bis 1/64; Winkel: 1 Grad, 2 Grad/Minute, 3 Grad/Minute/Sekunde. |
| `showSecondaryValue` | boolean |  | Wert zusätzlich in der sekundären Einheit ausgeben. |
| `secondaryLeaderText` | string |  | Vor dem sekundären Wert ausgegebener Text. |
| `secondaryTrailerText` | string |  | Nach dem sekundären Wert ausgegebener Text. |
| `secondaryBoxText` | boolean |  | Sekundären Wert mit einem Rahmen versehen. |
| `secondaryPrecision` | integer |  | Genauigkeit des sekundären Werts (wie `precision`). |
| `noteText` | string |  | Der Bemaßung hinzugefügter Hinweistext. |
| `textPositionAutomatic` | boolean |  | Textposition automatisch festlegen. |
| `textInside` | boolean |  | Text innerhalb der Hilfslinien platzieren. |
| `textFlipped` | boolean |  | Text spiegeln. |
| `textRotation` | integer |  | Textdrehung: 0 ausgerichtet, 1 horizontal, 2 horizontal/vertikal. |
| `textOffsetAlongLine` | number |  | Textabstand entlang der Maßlinie. |
| `textOffsetAboveLine` | number |  | Textabstand oberhalb der Maßlinie. |
| `fontSize` | number |  | Schriftgröße in Punkten. |
| `fontStyle` | integer |  | Summe aus 1 fett, 2 kursiv, 4 unterstrichen. |
| `textStyle` | string |  | Name oder Ressourcen-UUID eines Textstils; eine leere Zeichenfolge bedeutet keinen Stil. |
| `toleranceType` | integer |  | Toleranz: 0 keine, 1 einfach, 2 doppelt, 3 Grenzmaß. |
| `tolerancePlus` | number |  | Oberer Toleranzwert. |
| `toleranceMinus` | number |  | Unterer Toleranzwert. |
| `standard` | string |  | Name des Bemaßungsstandards. |
| `standardIndex` | integer |  | Bemaßungsstandard nach Index: größer 0 integriert, kleiner 0 benutzerdefiniert. |
| `unit` | integer |  | 0 für Dokumenteinheiten, andernfalls der Index einer Einstellung für Bemaßungseinheiten. |
| `associate` | boolean |  | Bemaßung an die Geometrie unter ihren Endpunkten binden. |
| `associateSelectedOnly` | boolean |  | Mit `associate`: nur an ausgewählte Objekte binden. |
| `params` | object |  | Rohe Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `diametrical` | `true` für eine Durchmesserbemaßung. |
| `center` | Mittelpunkt des Kreises in Welteinheiten. |
| `radius` | Radius in Welteinheiten. |
| `diameter` | Durchmesser in Welteinheiten. |
| `angle` | Richtung der Bemaßung in Radiant von der X-Achse. |
| `value` | Ausgegebener Wert: Durchmesser bei einer Durchmesserbemaßung, andernfalls Radius. |
| `applied` | Für jede geschriebene Einstellung. |


### createCenterMark

Erstellt eine Mittelpunktmarkierung für ein rundes Element.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: createCenterMark" · **Bei runToolBatch:** Ja

**Details**

Erstellt eine Mittelpunktmarkierung: ein Kreuz, optional mit vier Verlängerungssegmenten, das den Mittelpunkt eines runden Elements kennzeichnet. Sie ist eine Gruppe von Linien in der Bemaßungsklasse, kein Bemaßungsobjekt. Mit `objectUuid` wird der Mittelpunkt des Begrenzungsrahmens eines vorhandenen Objekts markiert; alternativ werden `center` und `radius` des Elements angegeben. Ohne explizite Größen stammen die Längen von Kreuz, Lücke und Verlängerungen aus dem aktiven Bemaßungsstandard und werden auf den Ebenenmaßstab umgerechnet.

`spokeLength`, `gap` und `extension` überschreiben diese Werte mit Längen in Welteinheiten; die Verlängerungssegmente entfallen, wenn der Kreis zu klein für sie ist.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `center` | [Punkt](Common.md#punkte) |  | Mittelpunkt. |
| `radius` | number |  | Radius in Welteinheiten. |
| `objectUuid` | string |  | UUID des Zielobjekts. |
| `spokeLength` | number |  | Länge jedes Kreuzarms vom Mittelpunkt aus (das gesamte Kreuz ist doppelt so lang), in Welteinheiten; muss größer als 0 sein. Ohne diesen Wert werden `gap` und `extension` ignoriert. |
| `gap` | number |  | Abstand zwischen dem Ende eines Kreuzarms und dem Anfang eines Verlängerungssegments, in Welteinheiten. Nur mit `spokeLength` verwendet; ein fehlender Wert gilt als 0. |
| `extension` | number |  | Überstand der Verlängerungssegmente über den Kreis hinaus, in Welteinheiten. Nur mit `spokeLength` verwendet; ein fehlender Wert gilt als 0. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird angelegt, falls sie noch nicht vorhanden ist. Siehe [Optionen zur Erstellung](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `center` | Mittelpunkt der Markierung in Welteinheiten. |
| `segmentCount` | Anzahl der Liniensegmente in der Gruppe: 2 nur für das Kreuz, 6 mit den vier Verlängerungssegmenten. |


### getDimension

Liest Art, Messpunkte, Wert und Texteinstellungen einer Bemaßung aus.

> **Auswirkung:** Nur lesend · **Sicherheitsstufe:** niedrig · **Rückgängig:** keiner · **Bei runToolBatch:** Zulässig

**Details**

Liest eine Bemaßung anhand von UUID, Name oder Index aus: ihre Art `kind` (constrainedLinear, unconstrainedLinear, ordinate, radial, diametrical, angular oder arcLength), Messpunkte, `offset` und `measuredLength`, die Einstellungen für Hilfslinien und Pfeile, den ausgegebenen Text und die Genauigkeit für primären und sekundären Wert, Textposition und Schrift, Toleranz, Bemaßungsstandard und Einheiteneinstellung (Ganzzahlcodes wie in setDimension) sowie die artspezifischen Felder: `value` und `direction` bei einer linearen Bemaßung, `vertex`/`startAngle`/`endAngle` bei einer Winkelbemaßung, `center`/`radius`/`sweepAngle` bei einer Bogenlängenbemaßung und `center`/`radius`/`diameter`/`angle` bei einer Radiusbemaßung.

Alle Winkel werden im Bogenmaß angegeben. Mittelpunktmarkierungen sind nicht gekennzeichnete Gruppen und können mit dieser Abfrage nicht erkannt werden.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `kind` | `constrainedLinear`, `unconstrainedLinear`, `ordinate`, `radial`, `diametrical`, `angular`, `arcLength` oder `unknown`. |
| `start`, `end` | The measured points, in world units. For an angular dimension they are the two leg points; for a radial or diametrical dimension, `start` is the center and `end` the point on the circle; for an arc length dimension, the two points on the arc. |
| `offset` | Abstand zwischen den gemessenen Punkten und der Maßlinie in Welteinheiten. Positiv: Maßlinie links von der Richtung `start` nach `end`; negativ: rechts davon. |
| `measuredLength` | Geradliniger Abstand zwischen `start` und `end` in Welteinheiten. Eine eingeschränkte lineare Bemaßung gibt die Projektion dieses Abstands auf ihre Richtung aus (siehe `value`). |
| the settings | Every setting that [`setDimension`](#setdimension) writes, under the name of its parameter: `startWitness`, `endWitness`, `witnessOverride`, `startWitnessLength`, `endWitnessLength`, `startWitnessOffset`, `endWitnessOffset`, `arrowsInside`, `leaderLine`, `showValue`, `leaderText`, `trailerText`, `boxText`, `precision`, `showSecondaryValue`, `secondaryLeaderText`, `secondaryTrailerText`, `secondaryBoxText`, `secondaryPrecision`, `noteText`, `textPositionAutomatic`, `textInside`, `textFlipped`, `textRotation`, `textOffsetAlongLine`, `textOffsetAboveLine`, `fontSize`, `fontStyle`, `textStyle`, `toleranceType`, `tolerancePlus`, `toleranceMinus`, `standard`, `standardIndex`, `unit`. `textStyle` is the name of the text style (an empty string for none, or when the style cannot be found). `witnessOverride`, `precision`, `secondaryPrecision`, `textRotation`, `fontStyle`, `toleranceType`, `standardIndex` and `unit` are integer codes, as in [`setDimension`](#setdimension). |
| linear dimensions | `constrained` (boolean), `direction` (radians) and `value` (the measured distance projected on the direction of the dimension line, in world units). |
| angular dimensions | `vertex`, `startAngle` and `endAngle` (radians), `value` (radians, counter-clockwise from the first leg to the second, from 0 up to 2π) and `referenceAngle`. |
| arc length dimensions | `center`, `radius`, `startAngle`, `sweepAngle` (radians; negative: clockwise), `value` (the length along the arc, in world units), `clockwise`, `witnessPerpendicularToChord` and `arcIndicator`. |
| radial dimensions | `diametrical`, `center`, `radius`, `diameter`, `angle` (radians, from the X axis), `value` (the diameter for a diametrical dimension, the radius otherwise) and `compact`. |


### setDimension

Bearbeitet eine Bemaßung.

> **Auswirkung:** Bearbeiten · **Sicherheitsstufe:** mittel · **Rückgängig:** ein Schritt "MCP: setDimension" · **Bei runToolBatch:** Ja

**Details**

Bearbeitet eine Bemaßung anhand von UUID, Name oder Index. Jede gemeinsame Einstellung kann geschrieben werden: Messpunkte `start`/`end`, `offset`, Hilfslinien, `arrowsInside`/`leaderLine`, der ausgegebene Text (`showValue`, `leaderText`, `trailerText`, `boxText`, `precision` und die entsprechenden Felder mit Präfix 'secondary', `noteText`), Textposition und Schrift, Toleranz, `standard` und `unit`.

**Ganzzahlcodes:** `witnessOverride`: 0 gemäß Standard, 1 eine benutzerdefinierte Länge, 2 Länge je Hilfslinie, 3 einen benutzerdefinierten Abstand, 4 Abstand je Hilfslinie; `precision`: Dezimalstellen (Bruchmaße: 0–6 = 1/1–1/64; Winkel: 1 Grad, 2 Grad/Minute, 3 Grad/Minute/Sekunde); `textRotation`: 0 ausgerichtet, 1 horizontal, 2 horizontal/vertikal; `fontStyle`: Summe aus 1 fett, 2 kursiv, 4 unterstrichen (`fontSize` wird in Punkten angegeben); `toleranceType`: 0 keine, 1 einfach, 2 doppelt, 3 Grenzmaß; `standardIndex` &gt; 0 integrierter, &lt; 0 benutzerdefinierter Standard; `unit`: 0 Dokumenteinheiten, andernfalls der Index einer Einstellung für Bemaßungseinheiten.

**Artspezifische Felder:** `direction` (Bogenmaß) bei einer linearen Bemaßung, `vertex` und `referenceAngle` bei einer Winkelbemaßung, `center`/`radius`/`diameter`/`angle`/`compact` bei einer Radiusbemaßung. `associate`: true bindet die Bemaßung an die Geometrie unter ihren Endpunkten (`associateSelectedOnly` beschränkt dies auf die ausgewählten Objekte; eine Zuordnung kann nicht entfernt werden). Die Art einer Bemaßung kann nicht geändert werden. Ein Objekt `params` legt rohe Plug-in-Parameter fest.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `start` | [Punkt](Common.md#punkte) |  | Erster Messpunkt in Welteinheiten. |
| `end` | [Punkt](Common.md#punkte) |  | Zweiter Messpunkt in Welteinheiten. |
| `offset` | number |  | Abstand der Maßlinie von der Messgeometrie in Welteinheiten. |
| `startWitness` | boolean |  | Hilfslinie am Anfang anzeigen. |
| `endWitness` | boolean |  | Hilfslinie am Ende anzeigen. |
| `witnessOverride` | integer |  | Hilfslinien: 0 gemäß Standard, 1 eine benutzerdefinierte Länge, 2 Länge je Hilfslinie, 3 einen benutzerdefinierten Abstand, 4 Abstand je Hilfslinie. |
| `startWitnessLength` | number |  | Benutzerdefinierte Länge der Hilfslinie am Anfang. |
| `endWitnessLength` | number |  | Benutzerdefinierte Länge der Hilfslinie am Ende. |
| `startWitnessOffset` | number |  | Benutzerdefinierter Abstand der Hilfslinie am Anfang. |
| `endWitnessOffset` | number |  | Benutzerdefinierter Abstand der Hilfslinie am Ende. |
| `arrowsInside` | boolean |  | Pfeile innerhalb der Hilfslinien platzieren. |
| `leaderLine` | boolean |  | Maßlinie anzeigen. |
| `showValue` | boolean |  | Messwert ausgeben. |
| `leaderText` | string |  | Vor dem Wert ausgegebener Text. |
| `trailerText` | string |  | Nach dem Wert ausgegebener Text. |
| `boxText` | boolean |  | Wert mit einem Rahmen versehen. |
| `precision` | integer |  | Dezimalstellen; Bruchmaße: 0–6 = 1/1 bis 1/64; Winkel: 1 Grad, 2 Grad/Minute, 3 Grad/Minute/Sekunde. |
| `showSecondaryValue` | boolean |  | Wert zusätzlich in der sekundären Einheit ausgeben. |
| `secondaryLeaderText` | string |  | Vor dem sekundären Wert ausgegebener Text. |
| `secondaryTrailerText` | string |  | Nach dem sekundären Wert ausgegebener Text. |
| `secondaryBoxText` | boolean |  | Sekundären Wert mit einem Rahmen versehen. |
| `secondaryPrecision` | integer |  | Genauigkeit des sekundären Werts (wie `precision`). |
| `noteText` | string |  | Der Bemaßung hinzugefügter Hinweistext. |
| `textPositionAutomatic` | boolean |  | Textposition automatisch festlegen. |
| `textInside` | boolean |  | Text innerhalb der Hilfslinien platzieren. |
| `textFlipped` | boolean |  | Text spiegeln. |
| `textRotation` | integer |  | Textdrehung: 0 ausgerichtet, 1 horizontal, 2 horizontal/vertikal. |
| `textOffsetAlongLine` | number |  | Textabstand entlang der Maßlinie. |
| `textOffsetAboveLine` | number |  | Textabstand oberhalb der Maßlinie. |
| `fontSize` | number |  | Schriftgröße in Punkten. |
| `fontStyle` | integer |  | Summe aus 1 fett, 2 kursiv, 4 unterstrichen. |
| `textStyle` | string |  | Name oder Ressourcen-UUID eines Textstils; eine leere Zeichenfolge bedeutet keinen Stil. |
| `toleranceType` | integer |  | Toleranz: 0 keine, 1 einfach, 2 doppelt, 3 Grenzmaß. |
| `tolerancePlus` | number |  | Oberer Toleranzwert. |
| `toleranceMinus` | number |  | Unterer Toleranzwert. |
| `standard` | string |  | Name des Bemaßungsstandards. |
| `standardIndex` | integer |  | Bemaßungsstandard nach Index: größer 0 integriert, kleiner 0 benutzerdefiniert. |
| `unit` | integer |  | 0 für Dokumenteinheiten, andernfalls der Index einer Einstellung für Bemaßungseinheiten. |
| `associate` | boolean |  | Bemaßung an die Geometrie unter ihren Endpunkten binden. |
| `associateSelectedOnly` | boolean |  | Mit `associate`: nur an ausgewählte Objekte binden. |
| `direction` | number |  | Lineare Bemaßungen: Messrichtung im Bogenmaß. |
| `vertex` | [Punkt](Common.md#punkte) |  | Winkelbemaßungen: Eckpunkt des Winkels. |
| `referenceAngle` | boolean |  | Winkelbemaßungen: einen einzelnen Schenkel zum Bezugswinkel messen. |
| `center` | [Punkt](Common.md#punkte) |  | Mittelpunkt. |
| `radius` | number |  | Radius in Welteinheiten. |
| `diameter` | number |  | Durchmesser in Welteinheiten. |
| `angle` | number |  | Winkel im Bogenmaß, gegen den Uhrzeigersinn. |
| `compact` | boolean |  | Radiusbemaßungen: verkürzte Darstellung, die am Kreis endet. |
| `params` | object |  | Rohe Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Immer vorhanden und leer, wenn keine Einstellung angegeben wurde. Ein Eintrag pro angegebener Einstellung: `true`, wenn geschrieben, andernfalls `false` bei Ablehnung (siehe Gruppenhinweise). Gemeinsam angegebene `start` und `end` werden als `points` gemeldet; einzeln als `start` oder `end`. `params` ist ein verschachteltes Objekt mit `true` oder `false` je Parametername. |


### getObjectDimensions

Listet die einem Objekt zugeordneten Bemaßungen auf.

> **Auswirkung:** Nur lesend · **Sicherheitsstufe:** niedrig · **Rückgängig:** keiner · **Bei runToolBatch:** Zulässig

**Details**

Listet die Bemaßungen auf, die dem anhand von UUID, Name oder Index angegebenen Objekt zugeordnet sind, d. h. die Bemaßungen, die dem Objekt folgen, wenn es verschoben oder in der Größe geändert wird. Jede aufgeführte Bemaßung enthält ihre Art `kind` (wie in getDimension).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `object` | Objektreferenz des Objekts (siehe [Objektreferenzen](Common.md#objektreferenzen)). |
| `dimensions` | Ein Eintrag pro zugeordneter Bemaßung: ihre Objektreferenz und ihr `kind` (wie bei [`getDimension`](#getdimension)). Leer, wenn keine Bemaßung zugeordnet ist. Es gibt keine Seitennavigation. |
