[English](../../MCP/v2027.2/ToolAccess.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/ToolAccess.md)

# ToolAccess — Interaktive Werkzeuge

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Werkzeuge zum Bedienen der interaktiven Vectorworks-Werkzeuge in den Werkzeugpaletten wie ein Benutzer: ein Werkzeug aktivieren, seine Modi festlegen und in die Zeichnung klicken.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [InteractiveTools](#interactivetools)
  - [getTools](#gettools)
  - [getTool](#gettool)
  - [getActiveTool](#getactivetool)
  - [activateTool](#activatetool)
  - [getToolModes](#gettoolmodes)
  - [setToolMode](#settoolmode)
  - [setToolModes](#settoolmodes)
  - [sendToolPointer](#sendtoolpointer)
  - [sendToolAction](#sendtoolaction)
  - [convertToolCoordinates](#converttoolcoordinates)

## Überblick

Dieser Ordner enthält 1 Werkzeuggruppe mit insgesamt 10 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Risikostufe | Anzahl der Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [InteractiveTools](#interactivetools) | `interactivetools` | Nein | hoch | 10 | Bedient die interaktiven Vectorworks-Werkzeuge der Werkzeugpaletten wie ein Benutzer. |

## InteractiveTools

> **Gruppe:** `InteractiveTools` · **Gruppen-ID:** `interactivetools` · **Standardmäßig aktiv:** Nein · **Risikostufe:** hoch · **Werkzeuge:** 10

**Bedient die interaktiven Vectorworks-Werkzeuge der Werkzeugpaletten wie ein Benutzer.**

Verwenden Sie die interaktiven Vectorworks-Werkzeuge – die Zeichen- und Bearbeitungswerkzeuge in den Werkzeugpaletten (Rectangle, Polyline, Wall, Door, Selection, Reshape, Eyedropper usw.) – genau wie ein Benutzer: Suchen Sie ein Werkzeug, aktivieren Sie es, legen Sie seine Modi in der Modusleiste fest, klicken oder ziehen Sie in der Zeichnung und schließen Sie die Aktion ab oder brechen Sie sie ab. Bevorzugen Sie die dedizierten Werkzeuge zum Erstellen und Bearbeiten anderer Gruppen, wenn diese die Aufgabe abdecken. Verwenden Sie diese Gruppe für Werkzeuge ohne direkte API (Plug-in-Werkzeuge, spezielle Bearbeitungswerkzeuge) oder wenn der Benutzer ein Werkzeug bedienen lassen möchte.

Arbeitsablauf:

1. getTools findet ein Werkzeug mit `search` (und dem Filter `activatable`); Werkzeuge werden über `universalName` identifiziert (integrierte Werkzeuge verwenden eine negative Zahl wie `-207` und akzeptieren außerdem ihren englischen `name`). getTool gibt ein Werkzeug mit seinen deklarierten Modusschaltflächen zurück.
2. activateTool aktiviert das Werkzeug (optional mit festgelegten Modi) und gibt die aktuelle Modusleiste, den Anleitungstext (`helpMessage`) und die Werkzeugpunkte zurück.
3. Modi: Die Modusleiste enthält bis zu 8 Modusgruppen (Optionsfelder, Druckschaltflächen, Umschalter, Auswahllisten, Eingabefelder, Ressourcen-Pop-ups, durchsuchbare Auswahllisten und Kombinationsfelder). Sprechen Sie einen Modus über seinen 0-basierten `modeIndex` oder über `modeName` (Bezeichnung oder Name einer Auswahl) an. setToolModes legt mehrere Modi anhand von Textwerten fest; setToolMode unterstützt alle typisierten Operationen. Ein Werkzeug kann seine Modusleiste nach einer Änderung neu aufbauen. Lesen Sie die Modi daher erneut mit getToolModes aus, statt alte Indizes wiederzuverwenden. Eine Schaltfläche für Einstellungen öffnet einen modalen Dialog.
4. sendToolPointer klickt auf Punkte in der Zeichnung. Im `model`-Raum sind Punkte Welteinheiten und werden EXAKT angewendet (ohne Fangfunktion); `{ x, y }` liegt auf der Konstruktionsebenenfläche, `{ x, y, z }` ist ein 3D-Punkt. Im `view`-Raum sind Punkte Pixel im aktiven Ansichtsfenster und verhalten sich wie ein echter Klick einschließlich SmartCursor-Fangfunktion. Werkzeuge, die das Objekt unter dem Cursor auswählen (Selection, Reshape, Eyedropper usw.), benötigen den Punkt sichtbar im Ansichtsfenster – prüfen Sie ihn mit convertToolCoordinates. Jeder Klick fügt üblicherweise einen Werkzeugpunkt hinzu; Werkzeuge mit zwei Punkten (Rectangle, Line) benötigen im Klick-Klick-Zeichenmodus zwei Klicks, Werkzeuge mit mehreren Punkten (Polyline, Wall, Polygon) werden mit `finish` oder einem Doppelklick abgeschlossen.
5. sendToolAction schließt ab (Return), bricht ab oder entfernt den letzten Punkt. Schließen Sie eine begonnene Aktion immer ab oder brechen Sie sie ab, bevor Sie das Werkzeug wechseln.

Prüfen Sie das Ergebnis mit getActiveTool (`toolPointCount`, `helpMessage`) und den Gruppen Objects/Selection. Zusatztasten (Shift, Alt) werden nicht unterstützt. Änderungen durch ein Werkzeug werden vom Werkzeug selbst im Vectorworks-Rückgängig-Verlauf aufgezeichnet, nicht als „MCP: <tool>“.

| Werkzeug | Wirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`getTools`](#gettools) | Nur lesend | niedrig | Listet die Vectorworks-Werkzeuge auf. |
| [`getTool`](#gettool) | Nur lesend | niedrig | Gibt ein Werkzeug mit seinen deklarierten Modusschaltflächen zurück. |
| [`getActiveTool`](#getactivetool) | Nur lesend | niedrig | Gibt den Status des aktiven Werkzeugs zurück. |
| [`activateTool`](#activatetool) | Interaktiv | mittel | Aktiviert ein Werkzeug. |
| [`getToolModes`](#gettoolmodes) | Nur lesend | niedrig | Liest die aktuelle Modusleiste des aktiven Werkzeugs aus. |
| [`setToolMode`](#settoolmode) | Interaktiv | mittel | Ändert einen Modus des aktiven Werkzeugs. |
| [`setToolModes`](#settoolmodes) | Interaktiv | mittel | Legt mehrere Modi des aktiven Werkzeugs fest. |
| [`sendToolPointer`](#sendtoolpointer) | Interaktiv | mittel | Klickt, doppelklickt, bewegt den Zeiger oder zieht mit dem aktiven Werkzeug in der Zeichnung. |
| [`sendToolAction`](#sendtoolaction) | Interaktiv | mittel | Schließt die Aktion des aktiven Werkzeugs ab, bricht sie ab oder entfernt den letzten Punkt. |
| [`convertToolCoordinates`](#converttoolcoordinates) | Nur lesend | niedrig | Wandelt Punkte zwischen Modellraum und der Ansicht des aktiven Ansichtsfensters um. |

### getTools

Listet die Vectorworks-Werkzeuge auf.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Listet die Vectorworks-Werkzeuge auf: integrierte Werkzeuge, VectorScript-/Python-Plug-in-Werkzeuge und SDK-Plug-in-Werkzeuge. `filter`: all (Standardwert; alle installierten Werkzeuge, auch diejenigen außerhalb des Arbeitsbereichs), activatable (können jetzt aktiviert werden) oder inWorkspace (in den Werkzeugpaletten platziert). `search` durchsucht Universalname, Name, Anzeigename und Kategorie (ohne Beachtung der Groß-/Kleinschreibung); `kind` behält nur eine Werkzeugart bei.

Jedes Werkzeug gibt universalName, name, displayName, category, helpText, shortcut, kind, creationType (point|line|box|path2D|path3D|custom|normal), inWorkspace, canActivate und active zurück; `includeModeButtons` ergänzt die vom Werkzeug deklarierten Modusschaltflächen. Ergebnisse werden seitenweise ausgegeben (`count` ist die Gesamtzahl; `truncated` bedeutet, dass weitere folgen).

**Hinweis:** `kind` wird exakt verglichen: Jeder andere Wert liefert keine Werkzeuge und keinen Fehler. Bei `search` wird die Groß-/Kleinschreibung nur für die Buchstaben A–Z ignoriert.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `filter` | string |  | Einer von: `all` (Standardwert; ein leerer String gilt ebenfalls als `all`), `activatable`, `inWorkspace`. Andere Werte führen zu einem Fehler. |
| `search` | string |  | Textfilter: behält Einträge bei, die diesen Text enthalten (ohne Beachtung der Groß-/Kleinschreibung). |
| `kind` | string |  | Einer von: `internalClassic`, `internalExtension`, `scriptPlugin`, `extensionPlugin`, `unknown`. |
| `includeModeButtons` | boolean |  | `true` listet die für jedes Werkzeug deklarierten Modusschaltflächen (`modeButtons`) statt ihrer Anzahl (`modeButtonCount`) auf. Standard `false`. |
| `limit` | integer |  | Seitennavigation: die maximale Anzahl zurückzugebender Elemente (mindestens 1, Standardwert 100). Siehe [Seitennavigation](Common.md#seitennavigation). |
| `offset` | integer |  | Seitennavigation: die Anzahl zu überspringender Elemente (Standardwert 0). |
| `countOnly` | boolean |  | Seitennavigation: Gibt nur die Anzahlen, nicht die Elemente zurück. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `tools` | Werkzeuge der Seite, nach `displayName` (ohne Beachtung der Groß-/Kleinschreibung) sortiert. Bei `countOnly` ausgelassen. |
| `count`, `returned`, `offset`, `limit`, `truncated`, `nextOffset` | Die Seitennavigationsschlüssel (siehe [Seitennavigation](Common.md#seitennavigation)). `nextOffset` wird nur ausgegeben, wenn `truncated` auf `true` gesetzt ist. |

| Schlüssel | Beschreibung |
|---|---|
| `universalName` | ID des Werkzeugs. Integrierte Werkzeuge verwenden eine negative Zahl, zum Beispiel `-207`. |
| `name` | Englischer Name eines integrierten Werkzeugs; bei Plug-in-Werkzeugen identisch mit `universalName`. |
| `displayName` | Lokalisierter Name. |
| `category`, `helpText`, `shortcut` | Kategorie, Hilfetext und Tastaturkürzel des Werkzeugs. |
| `kind` | `internalClassic` (klassisches, in Core integriertes Werkzeug), `internalExtension` (als Erweiterung in Core integriertes Werkzeug), `scriptPlugin` (VectorScript- oder Python-Plug-in-Werkzeug), `extensionPlugin` (SDK-Plug-in-Werkzeug) oder `unknown`. |
| `creationType` | `point`, `line`, `box`, `path2D`, `path3D`, `custom` oder `normal`. |
| `inWorkspace` | `true`, wenn das Werkzeug in einer Werkzeugpalette des aktuellen Arbeitsbereichs liegt. |
| `canActivate` | `true`, wenn `activateTool` das Werkzeug jetzt aktivieren kann: Ein Dokument ist geöffnet und das Werkzeugsystem führt das Werkzeug auf. Unabhängig von `inWorkspace`. |
| `active` | `true` für das aktive Werkzeug. |
| `modeButtonCount` | Anzahl der vom Werkzeug deklarierten Modusschaltflächen (0, wenn keine deklariert sind). Wird bei `includeModeButtons` durch `modeButtons` ersetzt. |
| `modeButtons` | Nur mit `includeModeButtons`: Liste mit `{ name, helpText, kind }`. `kind` ist `radio`, `button`, `preferences`, `check`, `editText` oder `pullDown`. |


### getTool

Gibt ein Werkzeug mit seinen deklarierten Modusschaltflächen zurück.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Gibt ein Werkzeug zurück, das über `name` gefunden wird (Universalname, englischer Name eines integrierten Werkzeugs oder lokalisierter Anzeigename), einschließlich der deklarierten Modusschaltflächen (name, helpText, kind). Die deklarierten Schaltflächen sind statische Informationen; die aktuelle Modusleiste wird nach der Aktivierung mit getToolModes ausgelesen.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string | Ja | Universalname, englischer Name eines integrierten Werkzeugs oder lokalisierter Anzeigename. |

**Ergebnis**

Ein Werkzeug mit seinen `modeButtons` und den unter [`getTools`](#gettools) beschriebenen Schlüsseln.

Jedes Werkzeug enthält folgende Schlüssel:

| Schlüssel | Beschreibung |
|---|---|
| `universalName` | ID des Werkzeugs. Integrierte Werkzeuge verwenden eine negative Zahl, zum Beispiel `-207`. |
| `name` | Englischer Name eines integrierten Werkzeugs; bei Plug-in-Werkzeugen identisch mit `universalName`. |
| `displayName` | Lokalisierter Name. |
| `category`, `helpText`, `shortcut` | Kategorie, Hilfetext und Tastaturkürzel des Werkzeugs. |
| `kind` | `internalClassic` (klassisches, in Core integriertes Werkzeug), `internalExtension` (als Erweiterung in Core integriertes Werkzeug), `scriptPlugin` (VectorScript- oder Python-Plug-in-Werkzeug), `extensionPlugin` (SDK-Plug-in-Werkzeug) oder `unknown`. |
| `creationType` | `point`, `line`, `box`, `path2D`, `path3D`, `custom` oder `normal`. |
| `inWorkspace` | `true`, wenn das Werkzeug in einer Werkzeugpalette des aktuellen Arbeitsbereichs liegt. |
| `canActivate` | `true`, wenn `activateTool` das Werkzeug jetzt aktivieren kann: Ein Dokument ist geöffnet und das Werkzeugsystem führt das Werkzeug auf. Unabhängig von `inWorkspace`. |
| `active` | `true` für das aktive Werkzeug. |
| `modeButtonCount` | Anzahl der vom Werkzeug deklarierten Modusschaltflächen (0, wenn keine deklariert sind). Wird bei `includeModeButtons` durch `modeButtons` ersetzt. |
| `modeButtons` | Nur mit `includeModeButtons`: Liste mit `{ name, helpText, kind }`. `kind` ist `radio`, `button`, `preferences`, `check`, `editText` oder `pullDown`. |

Fehler: `'name' is required`; `no Vectorworks tool matches '<name>' (use getTools with 'search' to find it)` (verwenden Sie `getTools` mit `search`, um das Werkzeug zu finden).

### getActiveTool

Gibt den Status des aktiven Werkzeugs zurück.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Gibt den Status des aktiven Werkzeugs zurück: das Werkzeug, seinen aktuellen Anleitungstext (`helpMessage`), ob eine Aktion läuft, die bisher eingegebenen Werkzeugpunkte (point2D, point3D, viewPoint), den aktuellen Zeigerpunkt, die Größe des aktiven Ansichtsfensters in Pixeln und – sofern `includeModes` nicht false ist – die aktuelle Modusleiste. `maxChoices` begrenzt die aufgeführten Auswahlen pro Modus (Standardwert 50).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `includeModes` | boolean |  | `false` lässt die aktuelle Modusleiste (`modes`) weg. Standard `true`. |
| `maxChoices` | integer |  | Maximale Anzahl der für jedes Steuerelement oder jeden Modus aufgelisteten Auswahlen (0 oder größer). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `activeTool` | Aktives Werkzeug mit seinen `modeButtons`; die Schlüssel sind unter [`getTools`](#gettools) beschrieben. `null`, wenn kein Werkzeug aktiv ist. |
| `helpMessage` | Aktueller Anweisungstext des Werkzeugs. |
| `inProgress` | Gibt an, ob eine Werkzeugaktion läuft. |
| `toolPointCount` | Anzahl der bisher eingegebenen Werkzeugpunkte. |
| `toolPoints` | Werkzeugpunkte, jeweils `{ point2D: { x, y }, point3D: { x, y, z }, viewPoint: { x, y } }`. `point3D` ist der Modellpunkt, `point2D` der Punkt auf der Bildschirmebene (2D-Werkzeuge) oder Arbeitsebene (3D-Werkzeuge), `viewPoint` die Pixelposition des aktiven Fensters. |
| `currentPoint` | Aktueller Hover-Punkt im Format eines Werkzeugpunkts. Nur vorhanden, wenn verfügbar. |
| `viewSize` | `{ width, height }` des aktiven Fensters in Pixeln. Nur vorhanden, wenn ein Fenster aktiv ist. |
| `modes` | Aktuelle Modusleiste: Liste von Modi, jeweils wie unter [`getToolModes`](#gettoolmodes) beschrieben. Wird bei `includeModes` `false` ausgelassen. |


### activateTool

Aktiviert ein Werkzeug.

> **Wirkung:** Interaktiv · **Risiko:** mittel · **Rückgängig:** von Vectorworks wie Benutzereingabe aufgezeichnet · **In runToolBatch:** nein

**Einzelheiten**

Aktiviert das über `name` angegebene Werkzeug (Universalname, englischer Name eines integrierten Werkzeugs oder Anzeigename) oder mit `selectionTool`: true das standardmäßige Selection-Werkzeug. Nur Werkzeuge im aktuellen Arbeitsbereich können aktiviert werden (siehe `canActivate` in getTools). Optional können direkt nach der Aktivierung Modi festgelegt werden: `modes` ist ein Array aus `{ modeIndex | modeName, value }` (wie bei setToolModes); mit `modeIndex` oder `modeName` zusammen mit `choiceIndex` wird eine Auswahl festgelegt.

Gibt den Status des neuen aktiven Werkzeugs mit seiner aktuellen Modusleiste und `modesApplied` zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `name` | string |  | Universalname, englischer Name eines integrierten Werkzeugs oder Anzeigename. |
| `selectionTool` | boolean |  | `true` aktiviert das Standard-Auswahlwerkzeug und ignoriert `name`. Standard `false`. |
| `modes` | array of object |  | Modi, die direkt nach der Aktivierung der Reihe nach gesetzt werden, im Format der `settings` von [`setToolModes`](#settoolmodes). Hat Vorrang vor `modeIndex` und `modeName`. |
| `modes[].modeIndex` | integer |  | 0-basierter Index des Modus. Hat Vorrang vor `modeName`. |
| `modes[].modeName` | string |  | Beschriftung des Modus oder einer seiner Auswahlmöglichkeiten. Wird nur verwendet, wenn `modeIndex` fehlt. |
| `modes[].value` | string or number or integer or boolean | Ja | Neuer Wert, wie `value` von [`setToolMode`](#settoolmode) mit `setValue`. Eine Einstellung ohne `value` wird als leerer Text angewendet. |
| `modeIndex` | integer |  | 0-basierter Index des Modus, der mit `choiceIndex` geändert werden soll. Hat Vorrang vor `modeName`. |
| `modeName` | string |  | Beschriftung des Modus oder einer seiner Auswahlmöglichkeiten. Wird nur verwendet, wenn `modeIndex` fehlt. |
| `choiceIndex` | integer |  | Auswahl im Modus `modeIndex` / `modeName`, entsprechend `selectChoice` von [`setToolMode`](#settoolmode). Standard 0. Ein negativer oder nicht numerischer Wert gilt als 0. |
| `maxChoices` | integer |  | Maximale Anzahl der für jedes Steuerelement oder jeden Modus aufgelisteten Auswahlen (0 oder größer). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `activated` | `true`. Kann das Werkzeug nicht aktiviert werden, schlägt der Aufruf mit einem Fehler fehl. |
| `modesApplied` | `true`, wenn kein Modus angefordert wurde oder alle angeforderten Modusänderungen erfolgreich waren; andernfalls `false`. |
| `modeResults` | Nur mit `modes`: ein Eintrag je Einstellung im Format der `results` von [`setToolModes`](#settoolmodes). |


### getToolModes

Liest die aktuelle Modusleiste des aktiven Werkzeugs aus.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Liest die aktuelle Modusleiste des aktiven Werkzeugs aus. Ohne `modeIndex`/`modeName` werden alle Modi zurückgegeben. Jeder Modus gibt index, type (radio|button|toggle|pullDown|editText|resourcePopup|searchablePullDown|comboBox), enabled, label, value (aktueller Wert als Text), choices (name, helpText, image, id) mit choiceCount, selectedChoice und bei Umschaltern isOn zurück. `maxChoices` begrenzt die aufgeführten Auswahlen pro Modus (Standardwert 50).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `maxChoices` | integer |  | Maximale Anzahl der für jedes Steuerelement oder jeden Modus aufgelisteten Auswahlen (0 oder größer). |
| `modeIndex` | integer |  | 0-basierter Index des zurückzugebenden Modus. Hat Vorrang vor `modeName`. |
| `modeName` | string |  | Beschriftung des Modus oder einer seiner Auswahlmöglichkeiten. Wird nur verwendet, wenn `modeIndex` fehlt. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `modeCount` | Anzahl der Modi in der Modusleiste. |
| `modes` | Liste aller Modi. |

| Schlüssel | Beschreibung |
|---|---|
| `index` | 0-basierter Index des Modus. |
| `type` | `radio`, `button`, `toggle`, `pullDown`, `editText`, `resourcePopup`, `searchablePullDown` oder `comboBox`. |
| `enabled` | Gibt an, ob der Modus geändert werden kann. |
| `label` | Beschriftung des Modus. |
| `value` | Aktueller Wert als Text. |
| `choiceCount` | Anzahl der Auswahlmöglichkeiten des Modus. |
| `choices` | Aufgeführte Auswahlmöglichkeiten, jeweils `{ index, name }` sowie `helpText`, `image` und `id`, wenn diese nicht leer sind. Bis zu `maxChoices` Einträge; bei Texteingabefeldern und Ressourcen-Pop-ups immer leer. |
| `choicesTruncated` | `true`, wenn `choices` weniger Einträge als `choiceCount` enthält. Nur dann vorhanden. |
| `selectedChoice` | Index der ausgewählten Option. Nur vorhanden, wenn der Modus eine hat. |
| `isOn` | Gibt an, ob der Umschalter eingeschaltet ist. Nur für Umschalter vorhanden. |


### setToolMode

Ändert einen Modus des aktiven Werkzeugs.

> **Wirkung:** Interaktiv · **Risiko:** mittel · **Rückgängig:** von Vectorworks wie Benutzereingabe aufgezeichnet · **In runToolBatch:** nein

**Einzelheiten**

Ändert einen Modus des aktiven Werkzeugs, adressiert über `modeIndex` oder `modeName`, genau wie ein Benutzer in der Modusleiste. `action` (Standardwert setValue): setValue – `value` wird je nach Modustyp interpretiert (radio: Schaltflächenname oder Index; button: betätigen; toggle: on/off/true/false/toggle; pullDown/searchablePullDown: Elementtext, ID oder Index; comboBox: Element oder Freitext; editText: Text; resourcePopup: Ressourcenname); selectChoice – wählt `choiceIndex` eines beliebigen Modustyps aus; selectRadio – wählt das Optionsfeld `choiceIndex` aus; pressButton; setToggle – setzt `isOn`; selectItem – wählt ein Listenelement über `item` (Text oder ID) oder `choiceIndex` aus; setText – setzt `text` in ein Eingabefeld oder Kombinationsfeld; selectResource – wählt `resourceName` in einem Ressourcen-Pop-up aus.

Deaktivierte Modi können nicht geändert werden. Gibt `ok` und den Modus nach der Änderung zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `action` | string |  | Einer von: `setValue`, `selectChoice`, `selectRadio`, `pressButton`, `setToggle`, `selectItem`, `setText`, `selectResource`. |
| `value` | string or number or integer or boolean |  | Wert für `setValue` (für diese Aktion erforderlich). Die Auswertung hängt vom Modustyp ab. Ein Boolean gilt als `on` oder `off`, eine Zahl als Dezimaltext. |
| `choiceIndex` | integer |  | 0-basierter Index der Auswahl. Für `selectChoice` und `selectRadio` erforderlich; für `selectItem` verwendet, wenn `item` fehlt. Ein negativer oder nicht numerischer Wert gilt als 0. |
| `isOn` | boolean |  | Für `setToggle` erforderlich. Ein Wert, der kein Boolean ist, gilt als `false`. |
| `item` | string |  | Text oder ID. |
| `text` | string |  | Für `setText` erforderlich. |
| `resourceName` | string |  | Für `selectResource` erforderlich. |
| `maxChoices` | integer |  | Maximale Anzahl der für jedes Steuerelement oder jeden Modus aufgelisteten Auswahlen (0 oder größer). |
| `modeIndex` | integer |  | 0-basierter Index des Modus. Hat Vorrang vor `modeName`. |
| `modeName` | string |  | Beschriftung des Modus oder einer seiner Auswahlmöglichkeiten. Wird nur verwendet, wenn `modeIndex` fehlt. |


**Aktionen**

| Aktion | Benötigt | Verhalten |
|---|---|---|
| `setValue` | `value` | Setzt den Modus anhand von `value`; siehe die folgende Tabelle. |
| `selectChoice` | `choiceIndex` | Funktioniert für `radio`, `button` (`choiceIndex` wird ignoriert), `toggle` (0 bedeutet aus, jede andere Zahl ein) sowie die Listen von `pullDown`, `searchablePullDown` und `comboBox`. Bei `editText` und `resourcePopup` schlägt die Aktion stets fehl; verwenden Sie `setText` bzw. `selectResource`. |
| `selectRadio` | `choiceIndex` | Betätigt das Optionsfeld mit diesem Index. Scheitert, wenn der Index hinter dem letzten Optionsfeld liegt. Ein negativer oder nicht numerischer Wert gilt als 0. |
| `pressButton` | keine | Betätigt einen Schaltflächenmodus. |
| `setToggle` | `isOn` | Schaltet einen Umschalter ein oder aus. Ist er bereits im gewünschten Zustand, bleibt er unverändert und der Aufruf gibt `ok: true` zurück. |
| `selectItem` | `item` oder `choiceIndex` | Wählt ein Element aus der Liste eines `pullDown`, `searchablePullDown` oder `comboBox`. `item` (Text oder ID bei `searchablePullDown`) hat Vorrang vor `choiceIndex`. |
| `setText` | `text` | Gibt Text in ein Eingabefeld oder Kombinationsfeld ein. |
| `selectResource` | `resourceName` | Wählt eine Ressource in einem Ressourcen-Pop-up aus. `ok` ist nur dann `true`, wenn das Pop-up anschließend diese Ressource anzeigt. |

setValue liest `value` je nach Modustyp aus:

| Modustyp | `value` |
|---|---|
| `radio` | Name oder Bild einer Auswahl (ohne Beachtung der Groß-/Kleinschreibung) oder die Nummer der Auswahl. |
| `button` | Wird ignoriert: Die Schaltfläche wird betätigt. |
| `toggle` | `on`, `true`, `yes` oder `1` schalten ein; `off`, `false`, `no` oder `0` schalten aus; `toggle` wechselt den Zustand. Die Wörter werden ohne Beachtung der Groß-/Kleinschreibung erkannt. |
| `pullDown`, `searchablePullDown` | Text eines Elements (ohne Beachtung der Groß-/Kleinschreibung) oder bei `searchablePullDown` dessen ID; andernfalls die Elementnummer. Text oder ID wird zuerst abgeglichen. |
| `comboBox` | Text eines Elements (ohne Beachtung der Groß-/Kleinschreibung); jeder andere Text wird in das Feld eingegeben. |
| `editText` | Einzugebender Text. |
| `resourcePopup` | Name der Ressource. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `ok` | `true`, wenn die Änderung angewendet wurde. |
| `modeCount` | Anzahl der Modi in der Modusleiste. |
| `mode` | Modus nach der Änderung, mit den unter [`getToolModes`](#gettoolmodes) beschriebenen Schlüsseln. `maxChoices` wird angewendet. |


### setToolModes

Legt mehrere Modi des aktiven Werkzeugs fest.

> **Wirkung:** Interaktiv · **Risiko:** mittel · **Rückgängig:** von Vectorworks wie Benutzereingabe aufgezeichnet · **In runToolBatch:** nein

**Einzelheiten**

Legt mehrere Modi des aktiven Werkzeugs der Reihe nach fest: `settings` ist ein Array aus `{ modeIndex | modeName, value }`, wobei `value` wie bei setToolMode setValue interpretiert wird. Jede Einstellung wird in `results` aufgeführt (ok, newValue, err); `allApplied` ist false, wenn eine Einstellung fehlgeschlagen ist. Gibt die aktualisierten Modi zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `settings` | array of object | Ja | Die Modusänderungen, der Reihe nach angewendet. Ein nicht leeres Array mit `{ modeIndex | modeName, value }`. |
| `settings[].modeIndex` | integer |  | 0-basierter Index des Modus. Hat Vorrang vor `modeName`. |
| `settings[].modeName` | string |  | Beschriftung des Modus oder einer seiner Auswahlmöglichkeiten. Wird nur verwendet, wenn `modeIndex` fehlt. |
| `settings[].value` | string or number or integer or boolean | Ja | Neuer Wert; wird je nach Modustyp wie `value` von [`setToolMode`](#settoolmode) mit `setValue` ausgewertet. Das Werkzeug lehnt eine Einstellung ohne `value` nicht ab, sondern wendet sie als leeren Text an. |
| `maxChoices` | integer |  | Maximale Anzahl der für jedes Steuerelement oder jeden Modus aufgelisteten Auswahlen (0 oder größer). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `allApplied` | `true`, wenn jede Einstellung angewendet wurde. |
| `results` | Ein Eintrag je Einstellung in der angegebenen Reihenfolge. |
| `modes` | Aktualisierte Modusleiste: Liste aller Modi, jeweils wie unter [`getToolModes`](#gettoolmodes) beschrieben. `maxChoices` wird angewendet. |

| Schlüssel | Beschreibung |
|---|---|
| `ok` | `true`, wenn der Modus geändert wurde. |
| `modeIndex` | 0-basierter Index des gefundenen Modus. |
| `newValue` | Textwert des Modus nach der Änderung. |
| `err` | `no mode matches 'modeIndex' / 'modeName'`. Nur vorhanden, wenn kein Modus gefunden wurde; dann ist `ok` `false` und `modeIndex` sowie `newValue` fehlen. |


### sendToolPointer

Klickt, doppelklickt, bewegt den Zeiger oder zieht mit dem aktiven Werkzeug in der Zeichnung.

> **Wirkung:** Interaktiv · **Risiko:** mittel · **Rückgängig:** von Vectorworks wie Benutzereingabe aufgezeichnet · **In runToolBatch:** nein

**Einzelheiten**

Bedient das aktive Werkzeug wie ein Benutzer in der Zeichnung mit dem Zeiger. `action`: click (Standardwert), doubleClick, move (nur Zeigerbewegung; aktualisiert die Vorschau) oder drag (Maus drücken bei `from`, loslassen bei `to`). `space`: model (Standardwert; Welteinheiten, exakt, kein Fangen; `{ x, y }` auf der Konstruktionsebenenfläche oder `{ x, y, z }`) oder view (Pixel im aktiven Ansichtsfenster, mit Fangfunktion). Geben Sie einen `point` oder mehrere `points` an (werden der Reihe nach gesendet; bei einem Fehler wird abgebrochen); `finish`: true drückt anschließend Return, um Werkzeuge mit mehreren Punkten abzuschließen.

Gibt `sent` und den Werkzeugstatus nach der Eingabe zurück (`toolPointCount`, `toolPoints`, `helpMessage`).

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `action` | string |  | Einer von: `click`, `doubleClick`, `move`, `drag`. |
| `space` | string |  | Einer von: `model`, `view`. |
| `point` | [3D-Punkt](Common.md#punkte) |  | Modellraum: `{ x, y }` auf der Konstruktionsebenenfläche oder `{ x, y, z }` im 3D-Raum, in Welteinheiten. Ansichtsraum: `{ x, y }` in Pixeln vom oberen linken Rand des aktiven Zeichenfensters aus. |
| `points` | array of [3D point](Common.md#punkte) |  | Jedes Element: Modellraum: `{ x, y }` auf der Konstruktionsebenenfläche oder `{ x, y, z }` im 3D-Raum, in Welteinheiten. Ansichtsraum: `{ x, y }` in Pixeln vom oberen linken Rand des aktiven Zeichenfensters aus. |
| `from` | [3D-Punkt](Common.md#punkte) |  | Modellraum: `{ x, y }` auf der Konstruktionsebenenfläche oder `{ x, y, z }` im 3D-Raum, in Welteinheiten. Ansichtsraum: `{ x, y }` in Pixeln vom oberen linken Rand des aktiven Zeichenfensters aus. |
| `to` | [3D-Punkt](Common.md#punkte) |  | Modellraum: `{ x, y }` auf der Konstruktionsebenenfläche oder `{ x, y, z }` im 3D-Raum, in Welteinheiten. Ansichtsraum: `{ x, y }` in Pixeln vom oberen linken Rand des aktiven Zeichenfensters aus. |
| `finish` | boolean |  | `true` sendet nach der Eingabe die Eingabetaste, um Werkzeuge mit mehreren Punkten abzuschließen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `sent` | Anzahl der übermittelten Zeigereingaben: eine pro Punkt für `move`, `click` und `doubleClick`; bei `drag` 1 oder 0. |
| `ok` | `true`, wenn `sent` größer als 0 ist. |
| `finished` | `true`, wenn `finish` gesetzt war und die Eingabetaste verarbeitet wurde. |


### sendToolAction

Schließt die Aktion des aktiven Werkzeugs ab, bricht sie ab oder entfernt den letzten Punkt.

> **Wirkung:** Interaktiv · **Risiko:** mittel · **Rückgängig:** von Vectorworks wie Benutzereingabe aufgezeichnet · **In runToolBatch:** nein

**Einzelheiten**

Steuert die Aktion des aktiven Werkzeugs: finish (Return – schließt Werkzeuge mit mehreren Punkten ab), cancel (entfernt alle Werkzeugpunkte, ohne die Auswahl zu ändern), removeLastPoint oder pressKey mit `key` return, escape oder backspace (escape löscht wie beim Drücken der Taste durch den Benutzer auch die Auswahl, wenn keine Werkzeugpunkte vorhanden sind). Gibt `ok` und den Werkzeugstatus zurück.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `action` | string | Ja | Einer von: `finish`, `cancel`, `removeLastPoint`, `pressKey`. |
| `key` | string |  | Einer von: `return`, `escape`, `backspace`. |

**Ergebnis**

| Aktion | `ok` ist `true`, wenn |
|---|---|
| `finish` | Die Eingabetaste wurde verarbeitet. |
| `cancel` | Es sind keine Werkzeugpunkte mehr vorhanden. Das gilt auch, wenn es anfangs keine gab. |
| `removeLastPoint` | Ein Werkzeugpunkt wurde entfernt. `false`, wenn keine Werkzeugpunkte vorhanden sind. |
| `pressKey` | Die Taste wurde verarbeitet. Daraus geht nicht hervor, was das Werkzeug damit getan hat. |


### convertToolCoordinates

Wandelt Punkte zwischen Modellraum und der Ansicht des aktiven Ansichtsfensters um.

> **Wirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Einzelheiten**

Wandelt Punkte zwischen Modellraum und der Ansicht des aktiven Ansichtsfensters um. Bei `direction` modelToView werden Modellpunkte `{ x, y }` oder `{ x, y, z }` in Pixel umgewandelt; liegt der Punkt nicht im Ansichtsfenster, wird null zurückgegeben. Bei viewToModel werden Pixel in den darunterliegenden 2D-Modellpunkt umgewandelt (Konstruktionsebenenfläche in Top/Plan, andernfalls Bildschirmebene); außerhalb des Ansichtsfensters wird null zurückgegeben. Geben Sie `point` oder `points` an. Zusätzlich wird die Größe des Ansichtsfensters (`viewSize`) zurückgegeben.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `direction` | string | Ja | Einer von: `modelToView`, `viewToModel`. |
| `point` | [3D-Punkt](Common.md#punkte) |  | Modellraum: `{ x, y }` auf der Konstruktionsebenenfläche oder `{ x, y, z }` im 3D-Raum, in Welteinheiten. Ansichtsraum: `{ x, y }` in Pixeln vom oberen linken Rand des aktiven Zeichenfensters aus. |
| `points` | array of [3D point](Common.md#punkte) |  | Jedes Element: Modellraum: `{ x, y }` auf der Konstruktionsebenenfläche oder `{ x, y, z }` im 3D-Raum, in Welteinheiten. Ansichtsraum: `{ x, y }` in Pixeln vom oberen linken Rand des aktiven Zeichenfensters aus. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `points` | Ein Eintrag je Eingabepunkt, in derselben Reihenfolge. Jeder Eintrag ist `{ x, y }` oder `null`. `modelToView` liefert Pixel; `viewToModel` einen 2D-Modellpunkt in Welteinheiten. |
| `viewSize` | `{ width, height }` des aktiven Fensters in Pixeln. Nur vorhanden, wenn ein Fenster aktiv ist. |
