[English](../../MCP/v2027.2/Common.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/Common.md)

# Allgemeines — gemeinsame Konventionen

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Konventionen, denen alle Werkzeuge des Vectorworks-MCP-Servers folgen: Aufrufe und Ergebnisse, Objektreferenzen, Punkte und Farben, Einheiten, Optionen zur Erstellung, angewendete Einstellungen, Plug-in-Parameter, Seitennavigation, Auswirkungen, Risikostufen und Rückgängigmachen.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Werkzeuggruppen und Aktivierung](#werkzeuggruppen-und-aktivierung)
- [Core-Gruppe](#core-gruppe)
  - [listToolGroups](#listtoolgroups)
  - [activateToolGroups](#activatetoolgroups)
  - [runToolBatch](#runtoolbatch)
- [Ein Tool aufrufen](#ein-tool-aufrufen)
- [Ergebnisse und Fehler](#ergebnisse-und-fehler)
- [Objektreferenzen](#objektreferenzen)
- [Punkte, Rechtecke und Farben](#punkte-rechtecke-und-farben)
  - [Punkte](#punkte)
  - [Rechtecke](#rechtecke)
  - [Farben](#farben)
- [Einheiten und Winkel](#einheiten-und-winkel)
- [Optionen zur Erstellung](#optionen-zur-erstellung)
- [Angewendete Einstellungen](#angewendete-einstellungen)
- [Plug-in-Parameter](#plug-in-parameter)
  - [Parameter auslesen](#parameter-auslesen)
  - [Parameter schreiben](#parameter-schreiben)
- [Seitennavigation](#seitennavigation)
- [Auswirkungen und Risikostufen](#auswirkungen-und-risikostufen)
- [Rückgängig machen](#rückgängig-machen)

## Überblick

| Thema | Inhalt |
|---|---|
| [Werkzeuggruppen und Aktivierung](#werkzeuggruppen-und-aktivierung) | Welche Werkzeuge verfügbar sind und wie Gruppen aktiviert werden. |
| [Core-Gruppe](#core-gruppe) | Die drei Meta-Werkzeuge, die immer verfügbar sind: `listToolGroups`, `activateToolGroups`, `runToolBatch`. |
| [Ein Tool aufrufen](#ein-tool-aufrufen) | Aufbau eines Aufrufs und seines Ergebnisses, mit einem Beispiel. |
| [Ergebnisse und Fehler](#ergebnisse-und-fehler) | Ergebnisobjekte, Fehlermeldungen und zurückgerollte Aufrufe. |
| [Objektreferenzen](#objektreferenzen) | Wie Werkzeuge Objekte in ihren Argumenten und Ergebnissen identifizieren. |
| [Punkte, Rechtecke und Farben](#punkte-rechtecke-und-farben) | Die gemeinsamen Werteformate für Geometrie und Farbe. |
| [Einheiten und Winkel](#einheiten-und-winkel) | Welteinheiten, Radiant und einige Ausnahmen. |
| [Optionen zur Erstellung](#optionen-zur-erstellung) | Die Optionen, die jedes Erstellungswerkzeug akzeptiert: Klasse, Name und Auswahl. |
| [Angewendete Einstellungen](#angewendete-einstellungen) | Wie Werkzeuge Einstellung für Einstellung melden, was sie geschrieben haben. |
| [Plug-in-Parameter](#plug-in-parameter) | Parameter von Plug-in-Objekten auslesen und schreiben. |
| [Seitennavigation](#seitennavigation) | Wie lange Listen seitenweise zurückgegeben werden. |
| [Auswirkungen und Risikostufen](#auswirkungen-und-risikostufen) | Was ein Werkzeug ändern darf und wie Clients damit umgehen sollten. |
| [Rückgängig machen](#rückgängig-machen) | Wie die Änderungen eines Werkzeugaufrufs für „Bearbeiten > Rückgängig“ aufgezeichnet werden. |

## Werkzeuggruppen und Aktivierung

Die Werkzeuge sind in Werkzeuggruppen organisiert. Die Werkzeugliste des Servers (`tools/list`) zeigt nur die Werkzeuge der **aktiven** Gruppen. Ein Werkzeug, das in der Liste fehlt, wird daher nicht notwendigerweise nicht unterstützt.

- Standardmäßig sind 4 Gruppen aktiv: Document, Selection, IFC, Objects. Die **Core**-Gruppe ist immer aktiv.
- Die anderen Gruppen werden mit [`activateToolGroups`](#activatetoolgroups) aktiviert und bleiben für den Rest der Sitzung aktiv. Aktualisieren Sie danach die Werkzeugliste (Clients, die die Benachrichtigung `list_changed` verarbeiten, erledigen dies automatisch).
- [`listToolGroups`](#listtoolgroups) listet alle Gruppen auf, unabhängig davon, ob sie aktiv sind. Mit `includeTools` werden auch die Namen und Beschreibungen ihrer Werkzeuge angezeigt.
- Gruppen können über ihren Anzeigenamen oder ihre Gruppen-ID angegeben werden; beides wird akzeptiert.

- Der **Werkzeugmodus** im Dialog „MCP-Server starten“ bestimmt, welche Gruppen der Server überhaupt anbietet:
  - **Alle Werkzeuge aktivieren** (Standard): Alle Gruppen werden angeboten.
  - **Alle Werkzeuge ohne Skriptwerkzeuge aktivieren**: Die Gruppe [Scripting](Scripting.md#scripting) mit ihren 7 Werkzeugen wird nicht registriert. Sie erscheint nicht in `listToolGroups`, und `activateToolGroups` meldet sie unter `not_found`.
  - **Nur Skriptwerkzeuge aktivieren**: Nur die Gruppe Scripting (zusätzlich zu Core) wird angeboten und sofort aktiviert.
| Gruppe | Gruppen-ID | Seite | Standardmäßig aktiv | Risikostufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|---|
| [Core](#core-gruppe) | `core` | [Allgemeines](#core-gruppe) | Immer | low | 3 | Werkzeuggruppen ermitteln und aktivieren und mehrere Werkzeugaufrufe als einen Rückgängig-Schritt ausführen. |
| [Document](DocumentAccess.md#document) | `document` | [DocumentAccess](DocumentAccess.md) | Ja | low | 17 | Die aktive Zeichnung: Dokumentübersicht, Ebenen, Geschosse, Klassen, Einheiten, Ansicht und Dokumenteinstellungen. |
| [Selection](DocumentAccess.md#selection) | `selection` | [DocumentAccess](DocumentAccess.md) | Ja | medium | 3 | Die aktuelle Auswahl auflisten und mehrere Objekte gesammelt verschieben, drehen, skalieren, duplizieren, gruppieren, löschen oder neu klassifizieren. |
| [IFC](IFC.md#ifc) | `ifc` | [IFC](IFC.md) | Ja | low | 4 | IFC-Daten schreibgeschützt auslesen: IFC-Entität und Eigenschaftensätze von Objekten sowie die Definitionen der Eigenschaftensätze des Dokuments. |
| [IFC Data Mapping](IFC.md#ifc-data-mapping) | `ifc-data-mapping` | [IFC](IFC.md) | Nein | low | 2 | Die IFC-Data-Manager-Zuordnungsdefinitionen des aktiven Dokuments auslesen. |
| [Menus](MenuAccess.md#menus) | `menus` | [MenuAccess](MenuAccess.md) | Nein | high | 4 | Menübefehle finden, die Menüleiste auslesen, prüfen, ob ein Befehl jetzt ausgeführt werden kann, und ihn ausführen. |
| [Draw2D](ObjectPrimitives.md#draw2d) | `draw2d` | [ObjectPrimitives](ObjectPrimitives.md) | Nein | low | 15 | 2D-Grundelemente erstellen, bearbeiten, messen und kombinieren sowie Textobjekte erstellen, auslesen und bearbeiten. |
| [Objects](ObjectPrimitives.md#objects) | `objects` | [ObjectPrimitives](ObjectPrimitives.md) | Ja | medium | 12 | Beliebige Objekte finden, prüfen und bearbeiten: Attribute, Transformationen, Container, Plug-in-Parameter und Datensätze. |
| [3D Modeling](Objects3D.md#3d-modeling) | `3d-modeling` | [Objects3D](Objects3D.md) | Nein | medium | 16 | Volumenkörper, 3D-Polygone, Netze, NURBS-Kurven und -Flächen sowie Flächenmodelle erstellen, auslesen und bearbeiten. |
| [Annotation](ObjectsAnnotation.md#annotation) | `annotation` | [ObjectsAnnotation](ObjectsAnnotation.md) | Nein | medium | 8 | Datenstempel, Plankopfrahmen und die Plankopf-Projektdaten des Dokuments. |
| [Dimensioning](ObjectsAnnotation.md#dimensioning) | `dimensioning` | [ObjectsAnnotation](ObjectsAnnotation.md) | Nein | medium | 8 | Lineare, Winkel-, Bogenlängen- und Radialbemaßungen sowie Zentrierungsmarkierungen. |
| [Architecture](ObjectsArchitect.md#architecture) | `architecture` | [ObjectsArchitect](ObjectsArchitect.md) | Nein | medium | 9 | BIM-Bauteile: Wände, Boden/Decke, Dächer, Türen, Fenster, Stützen und Treppen. |
| [ConnectCAD](ObjectsConnectCAD.md#connectcad) | `connectcad` | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Nein | medium | 10 | ConnectCAD-Schaltplan-Geräte, Anschlüsse und Gerätetypen, erstellt anhand von JSON-Gerätebeschreibungen. |
| [Landmark](ObjectsLandmark.md#landmark) | `landmark` | [ObjectsLandmark](ObjectsLandmark.md) | Nein | medium | 10 | Pflanzen, befestigte Flächen, Landschaftsflächen, Geländemodelle, Geländemodifikatoren, Höhenpunkte, Grundstücksgrenzen und Bestandsbäume. |
| [Spotlight](ObjectsSpotlight.md#spotlight) | `spotlight` | [ObjectsSpotlight](ObjectsSpotlight.md) | Nein | medium | 5 | Spotlight-Beleuchtungsgeräte und die von ihnen verwendeten GDTF-Scheinwerfertypen. |
| [Object Info](OIPAccess.md#object-info) | `object-info` | [OIPAccess](OIPAccess.md) | Nein | medium | 3 | Die Infopalette für die aktuelle Auswahl wie ein Benutzer auslesen und bedienen. |
| [Resources](Resources.md#resources) | `resources` | [Resources](Resources.md) | Nein | medium | 11 | Ressourcen auflisten, importieren, erstellen, prüfen, bearbeiten und anwenden; Tabellenblätter auslesen und bearbeiten. |
| [Scripting](Scripting.md#scripting) | `scripting` | [Scripting](Scripting.md) | Nein | high | 7 | Python-Skripte ausführen, Python-Skriptressourcen auslesen und speichern sowie das Python-Modul `api` nachschlagen. |
| [InteractiveTools](ToolAccess.md#interactivetools) | `interactivetools` | [ToolAccess](ToolAccess.md) | Nein | high | 10 | Die interaktiven Vectorworks-Werkzeuge der Werkzeugpaletten wie ein Benutzer bedienen. |

## Core-Gruppe

> **Gruppe:** `Core` · **Gruppen-ID:** `core` · **Aktiv:** immer · **Risikostufe:** low · **Werkzeuge:** 3

**Werkzeuggruppen ermitteln und aktivieren und mehrere Werkzeugaufrufe als einen Rückgängig-Schritt ausführen.**

Die Meta-Werkzeuge der Core-Gruppe sind immer verfügbar. Sie verwalten die Werkzeugliste und gruppieren Werkzeugaufrufe; sie können nicht innerhalb von [`runToolBatch`](#runtoolbatch) aufgerufen werden.

| Werkzeug | Auswirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`listToolGroups`](#listtoolgroups) | Nur lesend | low | Alle Werkzeuggruppen, aktive und inaktive, mit ihrem Aktivierungsstatus und optional ihren Werkzeugen auflisten. |
| [`activateToolGroups`](#activatetoolgroups) | Sitzungseinstellung | low | Werkzeuggruppen für den Rest der Sitzung aktivieren, damit ihre Werkzeuge in der Werkzeugliste erscheinen. |
| [`runToolBatch`](#runtoolbatch) | Bearbeiten (Batch) | medium | Mehrere Werkzeugaufrufe als einen Rückgängig-Schritt ausführen – entweder alle oder keinen. |

### listToolGroups

Alle Werkzeuggruppen, aktive und inaktive, mit ihrem Aktivierungsstatus und optional ihren Werkzeugen auflisten.

> **Auswirkung:** Nur lesend · **Risiko:** low · **Rückgängig:** keiner · **In runToolBatch:** nein

**Details**

Aktive UND inaktive Werkzeuggruppen mit ihren Metadaten und ihrem Aktivierungsstatus auflisten. Bevor Sie eine Funktion als nicht unterstützt einstufen, prüfen Sie relevante Gruppen mit `group` (Anzeigename oder groupId) und `includeTools` auf true, um ihre Werkzeugnamen und Beschreibungen ohne Aktivierung oder Schemas auszulesen. Aktivieren Sie die benötigte Gruppe und aktualisieren Sie anschließend tools/list, bevor Sie ihre Werkzeuge verwenden. Dass ein Werkzeug in der aktiven Werkzeugliste fehlt, bedeutet nicht, dass es nicht unterstützt wird.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `group` | string |  | Optionale Gruppe, angegeben über Anzeigename oder groupId, die geprüft werden soll. |
| `includeTools` | boolean |  | Werkzeugnamen und Beschreibungen auch für inaktive Gruppen einschließen; keine Schemas. Standardwert: `false`. |

**Ergebnis**

{ "groups": [...] }, ein Eintrag pro Gruppe. Die Core-Gruppe steht an erster Stelle; die Reihenfolge der übrigen Gruppen ist nicht festgelegt. Ohne `group` werden alle Gruppen zurückgegeben, mit `group` nur die angegebene.

| Schlüssel | Beschreibung |
|---|---|
| `groupId` | Die Gruppen-ID, zum Beispiel `3d-modeling`. |
| `displayName` | Der Gruppenname, zum Beispiel `3D Modeling`. |
| `shortDescription` | Wann die Gruppe aktiviert werden sollte. |
| `safetyLevel` | `low`, `medium` oder `high`. |
| `currentlyActive` | `true`, wenn die Werkzeuge der Gruppe in der Werkzeugliste stehen. |
| `toolCount` | Anzahl der Werkzeuge in der Gruppe. |
| `tools` | Nur mit `includeTools`: eine Liste mit `{ "name", "description", "safetyLevel" }`. Hat ein Werkzeug keine eigene Risikostufe, gilt die Risikostufe seiner Gruppe. |

Fehler: `listToolGroups requires an arguments object`, `includeTools must be a boolean`, `group must be a display name or groupId string` und `Unknown tool group: <value>`.
**Beispielargumente**

```json
{
  "group": "architecture",
  "includeTools": true
}
```

### activateToolGroups

Werkzeuggruppen für den Rest der Sitzung aktivieren, damit ihre Werkzeuge in der Werkzeugliste erscheinen.

> **Auswirkung:** Sitzungseinstellung · **Risiko:** low · **Rückgängig:** keiner (die Zeichnung wird nicht geändert) · **In runToolBatch:** nein

**Details**

Eine oder mehrere Werkzeuggruppen für den Rest der Sitzung aktivieren, sodass ihre Werkzeuge in nachfolgenden tools/list-Anfragen verfügbar sind. Jeder Eintrag kann entweder der Anzeigename der Gruppe oder ihre von listToolGroups gemeldete Gruppen-ID sein. Aktualisieren Sie tools/list nach der Aktivierung (oder lassen Sie es durch die list_changed-Verarbeitung Ihres Clients aktualisieren), bevor Sie neu verfügbare Werkzeuge aufrufen. Die Aktivierung ändert die Verfügbarkeit von Werkzeugen, nicht den Zeichnungsinhalt, und berechtigt nicht zur Verwendung von Bearbeitungswerkzeugen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `groups` | array of string | Ja | Anzeigenamen oder Gruppen-IDs der zu aktivierenden Gruppen. |

**Ergebnis**

`{ "activated": [...], "already_active": [...], "not_found": [...] }`.

- `activated` und `already_active` enthalten die Anzeigenamen der Gruppen.
- `not_found` wiederholt Einträge, die keine Gruppe bezeichnen, zum Beispiel die Gruppe Scripting im Werkzeugmodus „Alle Werkzeuge ohne Skriptwerkzeuge aktivieren“.
- Einträge, die keine Zeichenfolgen sind, werden übersprungen; doppelt angegebene Gruppen werden nur einmal gemeldet.
- Ohne ein Array `groups` lautet das Ergebnis `{ "err": "activateToolGroups requires a 'groups' array" }`.
- Akzeptiert der Client `text/event-stream`, antwortet der Server als Ereignisstrom: zuerst mit der Nachricht `notifications/tools/list_changed`, dann mit dem Ergebnis. Andernfalls sendet er eine einfache JSON-RPC-Antwort; der Client muss die Werkzeugliste selbst aktualisieren. Dies gilt für jeden Aufruf von `activateToolGroups`, auch wenn sich keine Gruppe geändert hat oder das Ergebnis `err` enthält.
**Beispielargumente**

```json
{
  "groups": ["architecture", "Dimensioning"]
}
```

### runToolBatch

Mehrere Werkzeugaufrufe als einen Rückgängig-Schritt ausführen – entweder alle oder keinen.

> **Auswirkung:** Bearbeiten (Batch) · **Risiko:** medium · **Rückgängig:** ein Schritt „MCP: &lt;name&gt;“ für den gesamten Batch · **In runToolBatch:** nein

**Details**

Mehrere Werkzeugaufrufe als EINEN Vectorworks-Rückgängig-Schritt „MCP: &lt;name&gt;“ ausführen – entweder alle oder keinen. Verwenden Sie dies für eine Aufgabe auf Benutzerebene, die aus unabhängigen Aufrufen besteht, zum Beispiel „diese 4 Wände und den Boden erstellen“, damit ein einziger Rückgängig-Schritt die gesamte Aufgabe rückgängig macht. `calls` werden in dieser Reihenfolge ausgeführt, jeder Eintrag hat wie bei einem direkten Aufruf die Form { tool, arguments } (arguments ist standardmäßig {}); höchstens 50. Ein Aufruf kann keine Ergebnisse früherer Aufrufe desselben Batches verwenden, zum Beispiel die UUID eines darin erstellten Objekts. Verwenden Sie dafür ein einzelnes runPythonScript.

Liefert `undoStep` mit dem Wert true, `undoName` und `results` ({ tool, result } für jeden Aufruf). Wenn ein Aufruf fehlschlägt (`err` in seinem Ergebnis oder eine Ausnahme), wird der Batch angehalten und alles, was er ausgeführt hat, rückgängig gemacht: `err` nennt den Aufruf, `failedCall` ist dessen Nummer (ab 1), `rolledBack` gibt an, ob das Zurückrollen ausgeführt wurde, `undoStep` ist false und `results` endet mit dem fehlgeschlagenen Aufruf. `warning` wird hinzugefügt, wenn danach noch ein Rückgängig-Ereignis offen ist.

Nur Werkzeuge aus aktiven Gruppen.

**Abgelehnt, bevor etwas ausgeführt wird:** Werkzeuge mit hohem Risiko (safetyLevel=high oder destructiveHint=true: erst den Benutzer fragen, dann einzeln aufrufen), interaktive Werkzeuge (sie zeichnen ihren eigenen Rückgängig-Schritt auf) und Meta-Werkzeuge, einschließlich runToolBatch; jeder Batch, solange kein Dokument geöffnet ist oder ein anderer Vectorworks-Vorgang läuft. Vectorworks ist beschäftigt, bis der Batch beendet ist. Schreibgeschützte Werkzeuge sind zulässig, aber nicht erforderlich.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string | Ja | Name des Rückgängig-Schritts „MCP: &lt;name&gt;“: darf nicht leer sein und keine Steuerzeichen enthalten; zum Beispiel „Wände und Boden erstellen“. 1 bis 63 Zeichen. |
| `calls` | array of object | Ja | Die Werkzeugaufrufe, die in dieser Reihenfolge ausgeführt werden. 1 bis 50 Einträge. |
| `calls[].tool` | string | Ja | Name eines Werkzeugs aus einer aktiven Gruppe. |
| `calls[].arguments` | object |  | Argumente des Werkzeugs wie bei einem direkten Aufruf; Standardwert {}. |

**Ergebnis**

| Ergebnisfall | Ergebnis |
|---|---|
| Alle Aufrufe erfolgreich | `{ "undoStep": true, "undoName": "MCP: <name>", "results": [ { "tool", "result" }, ... ] }` |
| Ein Aufruf fehlgeschlagen | `{ "err": "call <n> (<tool>) failed: <err of the call>", "failedCall": <n>, "rolledBack": <true or false>, "undoStep": false, "results": [ ... ] }`. Der Batch stoppt bei diesem Aufruf, und `results` endet damit. |
| Batch abgelehnt | `{ "err": "<reason>", "undoStep": false }`. Es wurde nichts ausgeführt; das Ergebnis enthält weder `results`, `failedCall` noch `rolledBack`. |

- Ein Aufruf schlägt fehl, wenn sein Ergebnis ein oberstes `err` enthält oder eine Ausnahme ausgelöst wird. Eine abgefangene Ausnahme wird als `exception: <message>` oder `unhandled exception` gemeldet.
- `rolledBack` ist `true`, wenn das Rückgängig-Ereignis des Batches zurückgesetzt wurde. Es ist `false`, wenn kein Rückgängig-Ereignis mehr offen war und daher nichts zurückgesetzt werden konnte.
- `warning` („Nach dem Batch ist noch ein Rückgängig-Ereignis offen: Änderungen bis zu dessen Ende durch Vectorworks können ihm hinzugefügt werden.“) wird einem erfolgreichen oder fehlgeschlagenen Ergebnis hinzugefügt, wenn danach noch ein Rückgängig-Ereignis offen ist.
- Der gesamte Batch wird vor der Ausführung geprüft, und zwar in dieser Reihenfolge: `name`, `calls` (der erste nicht ausführbare Aufruf wird benannt) und der Status von Vectorworks. Gründe für eine Ablehnung:

| `err` eines abgelehnten Batches | Ursache |
|---|---|
| `'name' must be a string` | `name` fehlt oder ist keine Zeichenfolge. |
| `'name' must not be empty or blank` | `name` ist leer oder enthält nur Leerzeichen. |
| `'name' must not contain control characters` | `name` enthält ein Steuerzeichen. |
| `'name' must have at most 63 characters` | `name` ist länger als 63 Zeichen. |
| `'calls' must be an array of 1 to 50 calls { tool, arguments }` | `calls` fehlt, ist kein Array, ist leer oder enthält mehr als 50 Elemente. |
| `call <n> (<tool>): must be an object with a string 'tool'` | Der Aufruf ist kein Objekt mit einer Zeichenfolge `tool`. |
| `call <n> (<tool>): 'arguments' must be an object` | `arguments` ist kein Objekt. |
| `call <n> (<tool>): unknown tool` | Es gibt kein Werkzeug mit diesem Namen. |
| `call <n> (<tool>): the tool is in an inactive group; activate it via activateToolGroups` | Die Gruppe des Werkzeugs ist nicht aktiv. |
| `call <n> (<tool>): only provider tools can run in a batch, not the meta-tools (listToolGroups, activateToolGroups, runToolBatch)` | Das Werkzeug ist ein Meta-Werkzeug der Core-Gruppe. |
| `call <n> (<tool>): high-risk tools cannot run in a batch: ask the user, then call the tool on its own` | Das Werkzeug hat `destructiveHint` oder die Risikostufe `high` (eigene oder, falls nicht vorhanden, die seiner Gruppe): `runPythonScript`, `runScript` und `runMenuCommand`. |
| `call <n> (<tool>): interactive tools record their own undo steps and cannot run in a batch: call the tool on its own` | Das Werkzeug zeichnet eigene Rückgängig-Schritte auf: `activateTool`, `setToolMode`, `setToolModes`, `sendToolPointer`, `sendToolAction`, `setOIPValues` und `pressOIPButton`. |
| `no document is open` | Keine Zeichnung ist geöffnet. |
| `an undo event is already open: another Vectorworks operation is in progress; try again when it has finished` | Ein weiteres Rückgängig-Ereignis wird gerade erstellt. |

`<n>` ist die 1-basierte Nummer des Aufrufs. `(<tool>)` wird ausgelassen, wenn der Aufruf keinen Werkzeugnamen enthält.
**Beispielargumente** (zwei Wände in einem Rückgängig-Schritt; die Gruppe Architecture muss aktiv sein)

```json
{
  "name": "Create walls",
  "calls": [
    {
      "tool": "createWall",
      "arguments": {"start": {"x": 0, "y": 0}, "end": {"x": 5000, "y": 0}}
    },
    {
      "tool": "createWall",
      "arguments": {"start": {"x": 5000, "y": 0}, "end": {"x": 5000, "y": 4000}}
    }
  ]
}
```

## Ein Tool aufrufen

Ein Tool wird mit der MCP-Anfrage `tools/call` aufgerufen: mit dem Tool-`name` und einem Objekt `arguments`. Nicht benötigte Argumente werden weggelassen. Jedes Tool liefert ein JSON-Objekt zurück.

Zum Beispiel die Rechtecke der Zeichnung abrufen, jeweils zwei auf einmal:

```json
{
  "name": "findObjects",
  "arguments": {"criteria": "(T=RECT)", "limit": 2}
}
```

Das Ergebnis mit Platzhaltern für die UUIDs:

```json
{
  "count": 3,
  "limit": 2,
  "nextOffset": 2,
  "notSearched": ["INSYMBOL", "INOBJECT", "INVIEWPORT", "INOBJPATH", "INOBJPROFILE"],
  "objects": [
    {"type": 3, "typeName": "Rectangle", "uuid": "<uuid 1>"},
    {
      "name": "Plot outline",
      "type": 3,
      "typeName": "Rectangle",
      "uuid": "<uuid 2>"
    }
  ],
  "offset": 0,
  "returned": 2,
  "truncated": true
}
```

`count` ist die Anzahl aller Treffer, `objects` enthält diese Seite mit [Objektreferenzen](#objektreferenzen) und `nextOffset` ist der `offset` der nächsten Seite (siehe [Seitennavigation](#seitennavigation)). `notSearched` listet die Bereiche auf, die nicht in den Suchkriterien enthalten waren, beispielsweise das Innere von Symboldefinitionen.

## Ergebnisse und Fehler

- Jedes Tool liefert ein JSON-Objekt zurück. Die Schlüssel des Objekts werden bei jedem Tool beschrieben.
- Ein fehlgeschlagener Aufruf liefert ein Objekt mit `err`, einer Meldung, die den Fehler beschreibt. Zum Beispiel:

```json
{
  "err": "object not found (provide 'uuid', 'name' or 'index')"
}
```

- Argumente werden geprüft, bevor etwas geändert wird. Meldungen nennen das Argument, zum Beispiel `'limit' must be a number`, `'countOnly' must be true or false`, `'limit' must be at least 1` oder `'offset' must not be negative`.
- Wenn ein Aufruf, der die Zeichnung bearbeitet, fehlschlägt, werden seine Änderungen zurückgerollt und das Ergebnis enthält `rolledBack`. Siehe [Rückgängig machen](#rückgängig-machen).
- Werkzeuge, die mehrere Einstellungen schreiben, melden unter `applied` für jede Einstellung, was geschrieben wurde. Siehe [Angewendete Einstellungen](#angewendete-einstellungen).


| `err` | Ursache |
|---|---|
| `no active Vectorworks document` | Es ist kein Dokument geöffnet. Jedes Werkzeug außerhalb der [Core-Gruppe](#core-gruppe) benötigt ein geöffnetes Dokument, einschließlich `convertUnits`. Die Meta-Werkzeuge [`listToolGroups`](#listtoolgroups) und [`activateToolGroups`](#activatetoolgroups) benötigen keines. |
| `exception: &lt;text&gt;` oder `unhandled exception` | Das Werkzeug hat eine Ausnahme ausgelöst. Der Aufruf gilt als fehlgeschlagen (siehe `rolledBack`). |

| Code | Bedeutung |
|---|---|
| `-32700` | Der Inhalt ist kein gültiges JSON. |
| `-32601` | `Method not found: &lt;method&gt;`. |
| `-32602` | Ungültige Parameter: `tools/call requires a 'name' parameter`, `Tool '&lt;name&gt;' is in an inactive group; activate it via activateToolGroups.` oder `Unknown tool: &lt;name&gt;`. |
| `-32603` | Interner Fehler, auch wenn `params` von `tools/call` kein Objekt oder `name` keine Zeichenfolge ist. |

## Objektreferenzen

Werkzeuge, die mit einem vorhandenen Objekt arbeiten, nehmen dieses über eines von drei Argumenten entgegen:

| Argument | Typ | Bedeutung |
|---|---|---|
| `uuid` | string | Die UUID des Objekts, wie von den Werkzeugen gemeldet. Die bevorzugte Methode. |
| `name` | string | Der genaue Vectorworks-Name des Objekts (Infopalette, Feld „Name“). |
| `index` | integer | Der interne Index des Objekts. |

Der Server versucht zuerst `uuid`, dann `name` und anschließend `index` und verwendet den ersten Wert, der ein Objekt findet. Wenn keiner ein Objekt findet, schlägt der Aufruf mit `object not found (provide 'uuid', 'name' or 'index')` fehl. Einige Werkzeuge benennen das Argument nach seiner Rolle, zum Beispiel `targetUuid`, `pathUuid` oder `profileUuid`; diese erwarten eine UUID.

Werkzeuge, die Objekte zurückgeben (Suchergebnisse, erstellte Objekte, Gruppenmitglieder), melden sie als **Objektreferenzen**:

| Schlüssel | Typ | Bedeutung |
|---|---|---|
| `uuid` | string | Die UUID des Objekts. |
| `type` | integer | Der numerische Vectorworks-Objekttyp, zum Beispiel 2 für eine Linie, 3 für ein Rechteck und 86 für ein Plug-in-Objekt. |
| `typeName` | string | Der Typname, nur für gängige Typen: Line, Rectangle, Oval, Polygon, Arc, FreehandPolygon, Text, Group, RoundedRectangle, Symbol, SymbolDefinition, Locus, Polyline, Extrude, Mesh und Layer. |
| `parametricName` | string | Nur bei Plug-in-Objekten: der universelle Name des Plug-ins, zum Beispiel `Door`. |
| `localizedParametricName` | string | Nur bei Plug-in-Objekten: der Name des Plug-ins in der Vectorworks-Sprache, sofern das Plug-in installiert ist. |
| `name` | string | Der Objektname, sofern vorhanden. |

Verwenden Sie in einem nachfolgenden Aufruf die `uuid` einer Referenz.

## Punkte, Rechtecke und Farben

### Punkte

Ein 2D-Punkt ist ein Objekt `{ "x": 0, "y": 0 }` in Welteinheiten; auch die Array-Form `[x, y]` wird akzeptiert. Ein 3D-Punkt ergänzt `z`: `{ "x": 0, "y": 0, "z": 0 }`.

3D-Werkzeuge verwenden Ebenenkoordinaten: `z` ist relativ zur Höhe der Konstruktionsebene. Wenn ein Werkzeug `bounds3D` meldet, sind dessen Z-Werte absolute Welthöhen.

### Rechtecke

Ein Rechteck ist `{ "left": 0, "top": 1000, "right": 2000, "bottom": 0 }` in Welteinheiten, wobei `top` oberhalb von `bottom` liegt. Von Werkzeugen gemeldete Begrenzungen ergänzen `width`, `height` und `center` (einen Punkt):

```json
{
  "left": 0,
  "top": 1000,
  "right": 2000,
  "bottom": 0,
  "width": 2000,
  "height": 1000,
  "center": {"x": 1000, "y": 500}
}
```

### Farben

Eine Farbe ist `{ "r": 255, "g": 128, "b": 0 }` mit Kanälen von 0 bis 255; auch die Array-Form `[r, g, b]` wird akzeptiert. Werte außerhalb von 0 bis 255 werden begrenzt. Attribute, die auch die Dokumentfarbpalette verwenden können, haben neben dem RGB-Wert einen eigenen Indexschlüssel, zum Beispiel `foreColorIndex` neben `foreColor`; wenn beide angegeben sind und beide geändert werden, hat der Index Vorrang.

## Einheiten und Winkel

Sofern ein Tool nichts anderes angibt:

| Wert | Einheit |
|---|---|
| Koordinaten, Längen, Entfernungen, Versätze | Welteinheiten: die Einheiten der Zeichnung. Mit `getUnits` auslesen; mit `convertUnits` umrechnen. |
| Winkel, Drehungen | Radiant, gegen den Uhrzeigersinn positiv. |
| Text | UTF-8-Zeichenfolgen. |
| Farben | RGB, 0 bis 255 je Kanal (siehe [Farben](#farben)). |

Die Ausnahmen sind in den Toolbeschreibungen aufgeführt. Die wichtigsten sind:

| Wert | Einheit |
|---|---|
| Schriftgrößen | Punkt. |
| Winkel der Linienabschlussmarkierung | Ganze Grad (siehe [Linienabschlussmarkierungen](Attributes.md#linienendmarkierungen)). |
| Länge und Breite der Linienabschlussmarkierung | Seitendruck in Zoll. |
| Winkel des Schlagschattens | Grad (siehe [Schlagschatten](Attributes.md#schlagschatten)). |
| Versatz und Weichzeichnungsradius des Schlagschattens | Seitendruck in Zoll oder Welteinheiten, je nach Angabe unter `units`. |
| Dachneigungen | Grad. |
| Als typisierte Werte ausgelesene Plug-in-Parameter | Längen in Welteinheiten, Winkel in Grad (siehe [Plug-in-Parameter](#plug-in-parameter)). |
| Werte der Infopalette | In der Form, in der ein Benutzer sie eingibt, und in den Einheiten, die die Palette anzeigt. |

## Optionen zur Erstellung

Die Werkzeuge, die Objekte erstellen, akzeptieren vier optionale Optionen zur Erstellung. Sie werden nach dem Erstellen auf das neue Objekt angewendet; anschließend gibt das Tool seine [Objektreferenz](#objektreferenzen) zurück.

| Option | Typ | Bedeutung |
|---|---|---|
| `class` | string | Die Klasse des neuen Objekts. Eine noch nicht vorhandene Klasse wird erstellt. |
| `useClassAttributes` | boolean | Mit `class`: außerdem die grafischen Attribute des Objekts auf „Nach Klasse“ setzen. |
| `name` | string | Der Name des neuen Objekts. |
| `select` | boolean | Das neue Objekt auswählen. |

Werkzeuge mit diesen Optionen (45): [`createLine`](ObjectPrimitives.md#createline), [`createRectangle`](ObjectPrimitives.md#createrectangle), [`createCircle`](ObjectPrimitives.md#createcircle), [`createArc`](ObjectPrimitives.md#createarc), [`createPolygon`](ObjectPrimitives.md#createpolygon), [`createPolyline`](ObjectPrimitives.md#createpolyline), [`createLocus`](ObjectPrimitives.md#createlocus), [`combineShapes`](ObjectPrimitives.md#combineshapes), [`createText`](ObjectPrimitives.md#createtext), [`createPluginObject`](ObjectPrimitives.md#createpluginobject), [`createExtrude`](Objects3D.md#createextrude), [`createSolidPrimitive`](Objects3D.md#createsolidprimitive), [`createSweep`](Objects3D.md#createsweep), [`combineSolids`](Objects3D.md#combinesolids), [`createShell`](Objects3D.md#createshell), [`convertSolid`](Objects3D.md#convertsolid), [`create3DPolygon`](Objects3D.md#create3dpolygon), [`createMesh`](Objects3D.md#createmesh), [`createNurbsCurve`](Objects3D.md#createnurbscurve), [`createNurbsSurface`](Objects3D.md#createnurbssurface), [`createSurfaceModel`](Objects3D.md#createsurfacemodel), [`convertTo3D`](Objects3D.md#convertto3d), [`createDataTag`](ObjectsAnnotation.md#createdatatag), [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock), [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension), [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension), [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension), [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension), [`createCenterMark`](ObjectsAnnotation.md#createcentermark), [`createWall`](ObjectsArchitect.md#createwall), [`createSlab`](ObjectsArchitect.md#createslab), [`createRoof`](ObjectsArchitect.md#createroof), [`createDoor`](ObjectsArchitect.md#createdoor), [`createWindow`](ObjectsArchitect.md#createwindow), [`createColumn`](ObjectsArchitect.md#createcolumn), [`createStair`](ObjectsArchitect.md#createstair), [`createPlant`](ObjectsLandmark.md#createplant), [`createHardscape`](ObjectsLandmark.md#createhardscape), [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea), [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier), [`createPropertyLine`](ObjectsLandmark.md#createpropertyline), [`createSiteModel`](ObjectsLandmark.md#createsitemodel), [`createStake`](ObjectsLandmark.md#createstake), [`createExistingTree`](ObjectsLandmark.md#createexistingtree), [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice).

## Angewendete Einstellungen

Werkzeuge, die mehrere Einstellungen in einem Aufruf schreiben, melden unter `applied` das Ergebnis jeder einzelnen Einstellung: ein Objekt mit einem Eintrag für jede angegebene Einstellung, `true`, wenn sie geschrieben wurde, und `false`, wenn nicht (zum Beispiel, weil der Wert nicht passt oder das Objekt die Einstellung nicht unterstützt). Ein Aufruf kann daher erfolgreich sein, obwohl einzelne Einstellungen abgelehnt wurden. Prüfen Sie bei Bedarf `applied`.

Zum Beispiel liefert [`editLayer`](DocumentAccess.md#editlayer) mit diesen Argumenten:

```json
{
  "name": "Design Layer-1",
  "elevation": 3000,
  "scale": 50
}
```

die aktualisierte Ebene mit:

```json
{
  "applied": {"elevation": true, "scale": true}
}
```

Werkzeuge, die `applied` melden (27): [`editLayer`](DocumentAccess.md#editlayer), [`editStory`](DocumentAccess.md#editstory), [`editVertices`](ObjectPrimitives.md#editvertices), [`createText`](ObjectPrimitives.md#createtext), [`editText`](ObjectPrimitives.md#edittext), [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter), [`createPluginObject`](ObjectPrimitives.md#createpluginobject), [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject), [`createWall`](ObjectsArchitect.md#createwall), [`createSlab`](ObjectsArchitect.md#createslab), [`createDoor`](ObjectsArchitect.md#createdoor), [`createWindow`](ObjectsArchitect.md#createwindow), [`createStair`](ObjectsArchitect.md#createstair), [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject), [`setConnectCADSocket`](ObjectsConnectCAD.md#setconnectcadsocket), [`createPlant`](ObjectsLandmark.md#createplant), [`createHardscape`](ObjectsLandmark.md#createhardscape), [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea), [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier), [`createPropertyLine`](ObjectsLandmark.md#createpropertyline), [`createSiteModel`](ObjectsLandmark.md#createsitemodel), [`createStake`](ObjectsLandmark.md#createstake), [`createExistingTree`](ObjectsLandmark.md#createexistingtree), [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject), [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice), [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice), [`editWorksheet`](Resources.md#editworksheet).

## Plug-in-Parameter

Plug-in-Objekte (Türen, Fenster, Pflanzen, Beleuchtungsgeräte, Datenstempel und viele weitere) speichern ihre Einstellungen in Parametern, die mit ihren universellen (nicht lokalisierten) Namen bezeichnet werden. Verwenden Sie [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo), um zu sehen, um welches Plug-in es sich bei einem Objekt handelt (`parametricName`), und [`getPluginDefinition`](ObjectPrimitives.md#getplugindefinition), um die Parameter des Plug-ins auszulesen.

### Parameter auslesen

- [`getObjectParameters`](ObjectPrimitives.md#getobjectparameters) gibt alle Parameter oder die in `names` angegebenen als Anzeigetext zurück. Mit `includeDefinitions` werden für jeden Parameter außerdem Typ, lokalisierter Name und die Auswahlmöglichkeiten eines Popup-Menüs zurückgegeben.
- Das Argument `params` von [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject), [`getLandmarkObject`](ObjectsLandmark.md#getlandmarkobject) und [`getLightingDevice`](ObjectsSpotlight.md#getlightingdevice) nimmt ein Array von Parameternamen entgegen und gibt ihre exakten, typisierten Werte zurück:

| Parametertyp | JSON-Wert |
|---|---|
| Reelle Zahl, Maß, Koordinate, Winkel, Fläche, Volumen | number: Längen in Welteinheiten, Winkel in Grad |
| Ganzzahl, Popup-Menü für Maßnormen | integer |
| Boolean | `true` oder `false` |
| Jeder andere Typ (Text, Popup-Menü, ...) | string |

### Parameter schreiben

- [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) schreibt einen Parameter (`name` und `value`; der Typ stammt aus der Parameterdefinition oder aus `type`: `real`/`number`, `int`/`integer`, `bool`/`boolean`, andernfalls Text) oder mit `params` mehrere auf einmal.
- Ein `params`-Objekt `{ "ParamName": value }` schreibt Parameter anhand ihres universellen Namens in [`createPluginObject`](ObjectPrimitives.md#createpluginobject), [`createDataTag`](ObjectsAnnotation.md#createdatatag), [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock), [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject), [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension), [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension), [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension), [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension), [`setDimension`](ObjectsAnnotation.md#setdimension), [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject), [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject), [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice), [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice).
- [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) und [`createPluginObject`](ObjectPrimitives.md#createpluginobject) schreiben Werte auf dieselbe Weise: Numerische Parameter akzeptieren auch numerische Zeichenfolgen wie `"5"`. Ein Wert, der sich nicht in den Parametertyp umwandeln lässt, wird nicht geschrieben und mit `false` gemeldet; anschließend wird das Objekt neu generiert.
- [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject) nimmt reelle Zahlen in Welteinheiten entgegen, so wie [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject) sie mit `params` ausliest. Ein ausgelesener Wert kann daher unverändert zurückgeschrieben werden.

## Seitennavigation

Werkzeuge, die lange Listen zurückgeben können, geben diese seitenweise zurück. Sie nehmen dieselben Argumente für die Seitennavigation entgegen:

| Argument | Typ | Bedeutung |
|---|---|---|
| `limit` | integer | Die maximale Anzahl der Elemente auf dieser Seite; mindestens 1. Der Standardwert hängt vom Tool ab (siehe unten). |
| `offset` | integer | Die Anzahl der zu überspringenden Elemente; darf nicht negativ sein. Standardwert 0. |
| `countOnly` | boolean | Nur die Anzahl und die Schlüssel für die Seitennavigation zurückgeben, ohne die Elemente. Standardwert false. |

und melden neben den Elementen dieselben Schlüssel für die Seitennavigation:

| Schlüssel | Bedeutung |
|---|---|
| `count` | Die Gesamtzahl der Elemente (oder Treffer). |
| `returned` | Die Anzahl der Elemente auf dieser Seite. |
| `offset` | Der Versatz dieser Seite. |
| `limit` | Der verwendete Grenzwert. |
| `truncated` | `true`, wenn weitere Elemente folgen. |
| `nextOffset` | Der `offset` der nächsten Seite; nur vorhanden, wenn `truncated` den Wert true hat. |

Um eine vollständige Liste auszulesen, rufen Sie das Tool erneut mit `offset` auf `nextOffset` auf, bis `truncated` den Wert false hat. Verwenden Sie `countOnly`, um zu zählen oder die Existenz zu prüfen.

**Werkzeuge mit Seitennavigation**

| Werkzeug | Schlüssel für Elemente | Standardgrenzwert |
|---|---|---|
| [`listIFCMappingObjects`](IFC.md#listifcmappingobjects) | `objects` | 200 |
| [`findMenuCommands`](MenuAccess.md#findmenucommands) | `commands` | 50 |
| [`getMenus`](MenuAccess.md#getmenus) | `menus`, `entries` oder `items` | 100 |
| [`findObjects`](ObjectPrimitives.md#findobjects) | `objects` | 200 |
| [`getObjectsAtPoint`](ObjectPrimitives.md#getobjectsatpoint) | `objects` | 50 |
| [`get3DGeometry`](Objects3D.md#get3dgeometry) | `items`, in jeder Liste | 100 |
| [`listConnectCADSignals`](ObjectsConnectCAD.md#listconnectcadsignals) | `signals` | 500 |
| [`listConnectCADConnectors`](ObjectsConnectCAD.md#listconnectcadconnectors) | `connectors` | 500 |
| [`listGDTFs`](ObjectsSpotlight.md#listgdtfs) | `gdtfs` | 200 |
| [`getOIPControls`](OIPAccess.md#getoipcontrols) | `controls` | 100 |
| [`getResources`](Resources.md#getresources) | `resources` | 200 |
| [`getWorksheet`](Resources.md#getworksheet) | `cells` oder `subrows` | 200 cells, 100 subrows |
| [`listScripts`](Scripting.md#listscripts) | `scripts` | 200 |
| [`getTools`](ToolAccess.md#gettools) | `tools` | 100 |

**Listen mit Seitennavigation innerhalb eines Ergebnisses**

Einige Ergebnisse enthalten eine Liste, die mit eigenen Argumenten für die Seitennavigation aufgeteilt wird. Jede solche Liste ist ein Objekt mit den Schlüsseln für die Seitennavigation und den Elementen:

| Werkzeug | Liste | Argumente | Schlüssel für Elemente | Standardgrenzwert |
|---|---|---|---|---|
| [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo) | `members` | `memberLimit`, `memberOffset` | `objects` | 50 |
| [`getText`](ObjectPrimitives.md#gettext) | `lines` | `lineLimit`, `lineOffset` | `items` | 100 |
| [`getText`](ObjectPrimitives.md#gettext) | `styleRuns` | `runLimit`, `runOffset` | `items` | 100 |

## Auswirkungen und Risikostufen

Jedes Tool hat eine **Auswirkung**, die angibt, was es ändern darf, und eine **Risikostufe**, die beschreibt, mit welcher Vorsicht ein Client damit umgehen sollte. Beide Angaben werden bei jedem Tool angezeigt. Die Werkzeugliste meldet die Auswirkung über die standardmäßigen Tool-Annotationen `readOnlyHint` und `destructiveHint` an MCP-Clients. Eine höhere Risikostufe bedeutet, dass ein Aufruf mehr ändern kann oder schwerer rückgängig zu machen ist; der Server meldet sie im Feld `safetyLevel`.

| Auswirkung | Bedeutung | Risikostufe | Annotationen | Rückgängig | In runToolBatch | Werkzeuge |
|---|---|---|---|---|---|---|
| Nur lesend | Liest die Zeichnung oder den Anwendungsstatus aus und ändert nichts. | low | `readOnlyHint`: true | keiner | zulässig | 58 |
| Bearbeiten | Ändert die Zeichnung. Mit „Rückgängig“ wird die Änderung rückgängig gemacht. | low oder medium | `readOnlyHint`: false | ein Schritt „MCP: &lt;tool&gt;“ | ja | 86 |
| Interaktiv | Bedient die Benutzeroberfläche wie ein Benutzer: Werkzeugpaletten oder Infopalette. | medium | `readOnlyHint`: false | Von Vectorworks wie eine Benutzereingabe aufgezeichnet | nein | 7 |
| Interaktiv, destruktiv | Führt einen Menübefehl so aus, als hätte der Benutzer ihn ausgewählt. | high | `readOnlyHint`: false, `destructiveHint`: true | Vom Menübefehl aufgezeichnet | nein | 1 |
| Skriptausführung | Führt ein Python-Skript aus, das alles tun kann, was ein Skript tun kann. | high | `readOnlyHint`: false, `destructiveHint`: true | ein Schritt „MCP: script“ | nein | 2 |

**Risikostufen**

- **low**: Auslesen, Sitzungsänderungen (zum Beispiel, welche Werkzeuggruppen aktiv sind) und einfache Bearbeitungen der Dokumenteinstellungen sowie von 2D-Grundelementen und Text ([Document](DocumentAccess.md#document), [IFC](IFC.md#ifc), [IFC Data Mapping](IFC.md#ifc-data-mapping), [Draw2D](ObjectPrimitives.md#draw2d)). „Bearbeiten > Rückgängig“ macht die Änderungen rückgängig.
- **medium**: Bearbeitungen von Objekten, 3D-Geometrie, Anmerkungen und Branchenobjekten, Ressourcen und Tabellenblättern sowie die interaktiven Werkzeuge für Werkzeugpaletten und die Infopalette. „Bearbeiten > Rückgängig“ macht sie rückgängig.
- **high**: Menübefehle und Skripte, die weitreichende Änderungen vornehmen können, die schwer vorhersehbar sind. Clients sollten vor jedem Aufruf den Benutzer fragen. Diese Werkzeuge können nicht innerhalb von [`runToolBatch`](#runtoolbatch) ausgeführt werden.

Für jede Gruppe ist auf ihrer Seite eine Risikostufe angegeben. Ein Tool meldet seine eigene Stufe: Schreibgeschützte Werkzeuge sind immer low, interaktive Werkzeuge medium, Menübefehle und Skripte high und für die übrigen Bearbeitungswerkzeuge gilt die Stufe ihrer Gruppe, sofern das Tool nicht selbst eine festlegt.

**Werkzeuge mit besonderer Auswirkung**

- Interaktiv: [`setOIPValues`](OIPAccess.md#setoipvalues), [`pressOIPButton`](OIPAccess.md#pressoipbutton), [`activateTool`](ToolAccess.md#activatetool), [`setToolMode`](ToolAccess.md#settoolmode), [`setToolModes`](ToolAccess.md#settoolmodes), [`sendToolPointer`](ToolAccess.md#sendtoolpointer), [`sendToolAction`](ToolAccess.md#sendtoolaction).
- Interaktiv, destruktiv: [`runMenuCommand`](MenuAccess.md#runmenucommand).
- Skriptausführung: [`runPythonScript`](Scripting.md#runpythonscript), [`runScript`](Scripting.md#runscript).

## Rückgängig machen

- **Bearbeitungswerkzeuge**: Jeder erfolgreiche Aufruf ist ein Rückgängig-Schritt mit dem Namen `MCP: <tool>`, zum Beispiel `MCP: createWall`. „Bearbeiten > Rückgängig“ macht ihn rückgängig, und Vectorworks zeigt den Namen in seiner Statusmeldung an.
- **Fehlgeschlagene Aufrufe**: Wenn ein Bearbeitungsaufruf fehlschlägt, wird alles, was er geändert hat, zurückgerollt und das Ergebnis enthält `rolledBack`. Es bleibt nichts unvollständig ausgeführt.
- **Schreibgeschützte Werkzeuge** fügen keinen Rückgängig-Schritt hinzu.
- **Batches**: [`runToolBatch`](#runtoolbatch) führt mehrere Aufrufe als einen Rückgängig-Schritt `MCP: <name>` aus – entweder alle oder keinen. Innerhalb eines Batches wird jeder Aufruf Teil dieses Schritts. Wenn einer fehlschlägt, wird der Batch angehalten und alles, was er ausgeführt hat, zurückgerollt.
- **Interaktive Werkzeuge** ([`runMenuCommand`](MenuAccess.md#runmenucommand), [`setOIPValues`](OIPAccess.md#setoipvalues), [`pressOIPButton`](OIPAccess.md#pressoipbutton), [`activateTool`](ToolAccess.md#activatetool), [`setToolMode`](ToolAccess.md#settoolmode), [`setToolModes`](ToolAccess.md#settoolmodes), [`sendToolPointer`](ToolAccess.md#sendtoolpointer), [`sendToolAction`](ToolAccess.md#sendtoolaction)) werden von Vectorworks wie die eigenen Aktionen des Benutzers aufgezeichnet. „Bearbeiten > Rückgängig“ macht sie daher auf dieselbe Weise rückgängig wie für den Benutzer.
- **Skripte** ([`runPythonScript`](Scripting.md#runpythonscript), [`runScript`](Scripting.md#runscript)) werden in einem Rückgängig-Schritt `MCP: script` ausgeführt. Der Schritt bleibt nach einer erfolgreichen Ausführung oder einer Ausführung, die auf Benutzereingaben wartet, erhalten; nach einer fehlgeschlagenen Ausführung (`rolledBack`) wird er zurückgerollt.
