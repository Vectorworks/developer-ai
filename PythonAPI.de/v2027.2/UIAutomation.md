[English](../../PythonAPI/v2027.2/UIAutomation.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/UIAutomation.md)

# UIAutomation — Werkzeuge, die Methodenzeile, Menüs und die Infopalette

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Klassen zur Automatisierung der Benutzeroberfläche. `ToolAccess` ist der Werkzeugkatalog (Werkzeuge aktivieren), `ModeBar` liest und ändert die Methoden des aktiven Werkzeugs, und `ToolControl` steuert das aktive Werkzeug durch Klicken, Ziehen, Mausbewegungen und Tasten. `MenuAccess` listet Menübefehle und Menüblockeinträge auf und führt sie aus. `OIPAccess` listet, liest und bedient die Bedienelemente, die die Infopalette für die aktivierten Objekte anzeigt.

Konventionen: Abfragemethoden geben `None` zurück, wenn ein Wert nicht ermittelt werden kann, Setzmethoden/Aktionen geben bei Erfolg `True` zurück; Namensvergleiche berücksichtigen die Groß-/Kleinschreibung nicht; alle Indizes sind 0-basiert, einschließlich Methodenindizes und Indizes von Menüblockeinträgen. Die Bedienung der Benutzeroberfläche verhält sich genau wie Benutzereingaben: Werkzeuge können ihre Methodenzeile (`ModeBar`) neu aufbauen, Befehle zeigen ihre Dialoge an und richten ihre eigene Rückgängig-Funktion ein, Änderungen in der Infopalette bauen die Palette neu auf — lesen Sie Werte nach einer Änderung erneut aus, statt sie zwischenzuspeichern, und führen Sie keine Menübefehle innerhalb eines mit `Document.StartUndoEvent` gestarteten Rückgängig-Ereignisses aus.

Eingebaute Werkzeuge und Befehle verwenden eine negative Zahl als universellen Namen (zum Beispiel "-207"); für diese wird auch der englische Name akzeptiert. Modellkoordinaten werden in Welteinheiten angegeben; Ansichtskoordinaten in Pixeln ab der linken oberen Ecke des Ansichtsfensters (y wächst nach unten).

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [Point3D](#point3d)
  - [ViewPoint](#viewpoint)
  - [ViewSize](#viewsize)
  - [ToolPoint](#toolpoint)
  - [ModeButtonDefinition](#modebuttondefinition)
  - [Tool](#tool)
  - [ModeChoice](#modechoice)
  - [ToolMode](#toolmode)
  - [ModeSetting](#modesetting)
  - [ModeBar](#modebar)
  - [ToolControl](#toolcontrol)
  - [ToolAccess](#toolaccess)
  - [MenuCommand](#menucommand)
  - [MenuChunkItem](#menuchunkitem)
  - [MenuEntry](#menuentry)
  - [MenuAccess](#menuaccess)
  - [OIPControl](#oipcontrol)
  - [OIPSetting](#oipsetting)
  - [OIPAccess](#oipaccess)
- [Aufzählungen](#aufzählungen)
  - [ToolKind](#toolkind)
  - [ToolCreationType](#toolcreationtype)
  - [ToolFilter](#toolfilter)
  - [ModeType](#modetype)
  - [ModeButtonKind](#modebuttonkind)
  - [ToolKey](#toolkey)
  - [MenuCommandKind](#menucommandkind)
  - [MenuChunkKind](#menuchunkkind)
  - [MenuFilter](#menufilter)
  - [MenuEntryType](#menuentrytype)
  - [MenuStatus](#menustatus)
  - [OIPPane](#oippane)
  - [OIPControlType](#oipcontroltype)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`Point3D`](#point3d) | Klasse |  | 3D-Punkt in Weltkoordinaten. |
| [`ViewPoint`](#viewpoint) | Klasse |  | Punkt in Ansichtskoordinaten in Pixeln (16-Bit-Koordinaten). |
| [`ViewSize`](#viewsize) | Klasse |  | Größe des aktiven Ansichtsfensters in Pixeln. |
| [`ToolPoint`](#toolpoint) | Klasse |  | Ein in das aktive Werkzeug eingegebener Punkt in der Form, in der das Werkzeug ihn empfängt. |
| [`ModeButtonDefinition`](#modebuttondefinition) | Klasse |  | Eine vom Werkzeug deklarierte Methodenschaltfläche (statische Informationen, die ohne Aktivierung des Werkzeugs verfügbar sind). |
| [`Tool`](#tool) | Klasse |  | Beschreibung eines Werkzeugs. |
| [`ModeChoice`](#modechoice) | Klasse |  | Eine Auswahlmöglichkeit einer Methodengruppe: eine Optionsschaltfläche, die einzelne Schaltfläche einer Button-/Toggle-Gruppe oder ein Eintrag einer PullDown- / ComboBox- / SearchablePullDown-Gruppe. |
| [`ToolMode`](#toolmode) | Klasse |  | Aktueller Zustand einer Methodengruppe des aktiven Werkzeugs. |
| [`ModeSetting`](#modesetting) | Klasse |  | Eine Anforderung zum Methodenwechsel für die allgemeine textbasierte Methoden-API (siehe `ModeBar.SetMode`). |
| [`ModeBar`](#modebar) | Klasse |  | Zustandslose Sicht auf die Methodenzeile (`ModeBar`) des aktiven Werkzeugs. |
| [`ToolControl`](#toolcontrol) | Klasse |  | Zustandslose Steuerung des aktiven Werkzeugs. |
| [`ToolAccess`](#toolaccess) | Klasse |  | Zustandslose Schnittstelle zum Vectorworks-Werkzeugsystem. |
| [`MenuCommand`](#menucommand) | Klasse |  | Beschreibung eines installierten Menübefehls. |
| [`MenuChunkItem`](#menuchunkitem) | Klasse |  | Ein aktueller Eintrag eines Menüblocks. |
| [`MenuEntry`](#menuentry) | Klasse |  | Ein Eintrag eines Menüs in der Menüleiste gemäß der aktuellen Arbeitsumgebung. |
| [`MenuAccess`](#menuaccess) | Klasse |  | Zustandslose Schnittstelle zum Vectorworks-Menüsystem. |
| [`OIPControl`](#oipcontrol) | Klasse |  | Beschreibung und aktueller Zustand eines Bedienelements der Infopalette. |
| [`OIPSetting`](#oipsetting) | Klasse |  | Eine Änderungsanforderung für ein Bedienelement, die von der allgemeinen, textbasierten API verwendet wird (siehe `OIPAccess.SetValue`). |
| [`OIPAccess`](#oipaccess) | Klasse |  | Zustandslose Schnittstelle zur Infopalette. |
| [`ToolKind`](#toolkind) | IntEnum |  | Wie ein Werkzeug bereitgestellt wird. |
| [`ToolCreationType`](#toolcreationtype) | IntEnum |  | Welche Art der Interaktion das Werkzeug zum Erzeugen von Objekten verwendet. |
| [`ToolFilter`](#toolfilter) | IntEnum |  | Welche Werkzeuge `ToolAccess.GetTools` zurückgibt. |
| [`ModeType`](#modetype) | IntEnum |  | Art einer Methodengruppe in der Methodenzeile des aktiven Werkzeugs. |
| [`ModeButtonKind`](#modebuttonkind) | IntEnum |  | Art einer Methodenschaltfläche, wie sie ein Werkzeug bei seiner Registrierung deklariert (kann vom aktuellen ModeType abweichen). |
| [`ToolKey`](#toolkey) | IntEnum |  | Tasten, auf die Werkzeuge bei der Punkteingabe reagieren (siehe `ToolControl.PressKey`). |
| [`MenuCommandKind`](#menucommandkind) | IntEnum |  | Wie ein Menübefehl bereitgestellt wird. |
| [`MenuChunkKind`](#menuchunkkind) | IntEnum |  | Art eines Menüblocks (siehe „Menüblock“ oben). |
| [`MenuFilter`](#menufilter) | IntEnum |  | Welche Menübefehle `MenuAccess.GetMenuCommands` zurückgibt. |
| [`MenuEntryType`](#menuentrytype) | IntEnum |  | Art eines Eintrags in einem Menü der Menüleiste. |
| [`MenuStatus`](#menustatus) | IntEnum |  | Ob ein Menübefehl (oder ein Menüblockeintrag) jetzt ausgeführt werden kann und gegebenenfalls warum nicht (siehe `MenuAccess.GetMenuStatus`). |
| [`OIPPane`](#oippane) | IntEnum |  | Bereich (Reiter) der Infopalette. |
| [`OIPControlType`](#oipcontroltype) | IntEnum |  | Art eines Bedienelements der Infopalette. |

## Klassen

### Point3D

> **Vollständiger Name:** `api.Point3D` · **Erbt von:** `api.Object`

3D-Punkt in Weltkoordinaten.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Point3D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Point3D(x, y, z)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: Point3D) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: Point3D) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `x` | `float` | X-Koordinate (Welteinheiten). |
| `y` | `float` | Y-Koordinate (Welteinheiten). |
| `z` | `float` | Z-Koordinate (Welteinheiten). |

### ViewPoint

> **Vollständiger Name:** `api.ViewPoint` · **Erbt von:** `api.Object`

Punkt in Ansichtskoordinaten in Pixeln (16-Bit-Koordinaten).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ViewPoint()` | Standardwert (Felder mit ihren Standardwerten). |
| `ViewPoint(x, y)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: ViewPoint) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: ViewPoint) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `x` | `int` | Horizontale Pixelposition vom linken Rand des aktiven Ansichtsfensters aus. |
| `y` | `int` | Vertikale Pixelposition vom oberen Rand des aktiven Ansichtsfensters aus (wächst nach unten). |

### ViewSize

> **Vollständiger Name:** `api.ViewSize` · **Erbt von:** `api.Object`

Größe des aktiven Ansichtsfensters in Pixeln.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ViewSize()` | Standardwert (Felder mit ihren Standardwerten). |
| `ViewSize(fWidth, fHeight)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fWidth` | `int` | Breite des aktiven Ansichtsfensters in Pixeln. |
| `fHeight` | `int` | Höhe des aktiven Ansichtsfensters in Pixeln. |

### ToolPoint

> **Vollständiger Name:** `api.ToolPoint` · **Erbt von:** `api.Object`

Ein in das aktive Werkzeug eingegebener Punkt in der Form, in der das Werkzeug ihn empfängt.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ToolPoint()` | Standardwert (Felder mit ihren Standardwerten). |
| `ToolPoint(fPoint2D, fPoint3D, fViewPoint)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fPoint2D` | `Math.Point2D` | Punkt auf der Bildschirmebene für 2D-Werkzeuge (mit dem Plan gedreht), Punkt auf der Arbeitsebene für 3D-Werkzeuge. |
| `fPoint3D` | `Point3D` | Modellpunkt. |
| `fViewPoint` | `ViewPoint` | Position des Klicks in der Ansicht. |

### ModeButtonDefinition

> **Vollständiger Name:** `api.ModeButtonDefinition` · **Erbt von:** `api.Object`

Eine von einem Werkzeug deklarierte Methodenschaltfläche (statische Information, ohne Aktivieren des Werkzeugs verfügbar). Nur Werkzeuge, die ihre Schaltflächen in der Methodenzeile deklarieren, stellen diese Informationen bereit.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ModeButtonDefinition()` | Standardwert (Felder mit ihren Standardwerten). |
| `ModeButtonDefinition(fName, fHelpText, fKind)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fName` | `str` | Name der Schaltfläche. |
| `fHelpText` | `str` | Hilfetext der Schaltfläche. |
| `fKind` | `ModeButtonKind` | Art der Schaltfläche. |

### Tool

> **Vollständiger Name:** `api.Tool` · **Erbt von:** `api.Object`

Beschreibung eines Werkzeugs.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Tool()` | Standardwert (Felder mit ihren Standardwerten). |
| `Tool(fUniversalName, fName, fDisplayName, fCategory, fHelpText, fShortcut, fKind, fCreationType, fIsInWorkspace, fCanActivate, fIsActive, fModeButtons)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fUniversalName` | `str` | Eindeutige Kennung; übergeben Sie sie an ActivateTool / FindTool. |
| `fName` | `str` | Benutzerfreundlicher englischer Name (bei Plug-in-Werkzeugen gleich fUniversalName). |
| `fDisplayName` | `str` | Lokalisierter Name, der in der Werkzeugpalette angezeigt wird. |
| `fCategory` | `str` | Plug-in-Kategorie (bei den meisten eingebauten Werkzeugen leer). |
| `fHelpText` | `str` | Kurzbeschreibung des Werkzeugs. |
| `fShortcut` | `str` | Tastenkürzel in der aktuellen Arbeitsumgebung (kann leer sein). |
| `fKind` | `ToolKind` | Art des Werkzeugs. |
| `fCreationType` | `ToolCreationType` | Wie das Werkzeug Objekte erzeugt. |
| `fIsInWorkspace` | `bool` | In einer Werkzeugpalette der aktuellen Arbeitsumgebung enthalten. |
| `fCanActivate` | `bool` | ActivateTool kann es jetzt aktivieren. |
| `fIsActive` | `bool` | Derzeit das aktive Werkzeug. |
| `fModeButtons` | `list[ModeButtonDefinition]` | Deklarierte Methodenschaltflächen (siehe ModeButtonDefinition). |

### ModeChoice

> **Vollständiger Name:** `api.ModeChoice` · **Erbt von:** `api.Object`

Eine Auswahlmöglichkeit einer Methodengruppe: eine Optionsschaltfläche, die einzelne Schaltfläche einer Button-/Toggle-Gruppe oder ein Eintrag einer PullDown- / ComboBox- / SearchablePullDown-Gruppe.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ModeChoice()` | Standardwert (Felder mit ihren Standardwerten). |
| `ModeChoice(fName, fHelpText, fImage, fId)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fName` | `str` | Methodenname oder Eintragstext (kann bei unbenannten Schaltflächen eingebauter Werkzeuge leer sein). |
| `fHelpText` | `str` | Hilfetext beim Darüberfahren (nur bei Schaltflächen). |
| `fImage` | `str` | Kennung der Bildressource (nur bei Schaltflächen), z. B. "Vectorworks/ModeViewBar/Options.png". |
| `fId` | `str` | Eintrags-ID (nur bei SearchablePullDown). |

### ToolMode

> **Vollständiger Name:** `api.ToolMode` · **Erbt von:** `api.Object`

Aktueller Zustand einer Methodengruppe des aktiven Werkzeugs.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ToolMode()` | Standardwert (Felder mit ihren Standardwerten). |
| `ToolMode(fIndex, fType, fIsEnabled, fLabel, fChoices, fChoiceCount, fSelectedChoice, fIsOn, fValue)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fIndex` | `int` | Position in der Methodenzeile (0-basiert). |
| `fType` | `ModeType` | Typ der Methodengruppe (Optionsfelder, Schaltfläche, Umschalter, Einblendmenü, ...). |
| `fIsEnabled` | `bool` | Ob die Methodengruppe bedienbar ist. |
| `fLabel` | `str` | Beschriftung des Bedienelements oder der Methodenname bei unbeschrifteten Schaltflächen. |
| `fChoices` | `list[ModeChoice]` | Siehe ModeChoice; leer bei EditText und ResourcePopup. |
| `fChoiceCount` | `int` | Gesamtzahl der Auswahlmöglichkeiten (fChoices kann gekürzt sein). |
| `fSelectedChoice` | `int \| None` | Für Radio, PullDown, ComboBox, SearchablePullDown. |
| `fIsOn` | `bool \| None` | Für Toggle. |
| `fValue` | `str` | Aktueller Wert als Text (siehe `ModeBar.GetModeValue`). |

### ModeSetting

> **Vollständiger Name:** `api.ModeSetting` · **Erbt von:** `api.Object`

Eine Anforderung zum Methodenwechsel für die allgemeine textbasierte Methoden-API (siehe `ModeBar.SetMode`).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ModeSetting()` | Standardwert (Felder mit ihren Standardwerten). |
| `ModeSetting(fModeIndex, fValue)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fModeIndex` | `int` | Index der Methodengruppe (0-basiert). |
| `fValue` | `str` | Wert, der wie bei `ModeBar.SetMode` interpretiert wird. |

### ModeBar

> **Vollständiger Name:** `api.ModeBar` · **Erbt von:** `api.Object`

Zustandslose Sicht auf die Methodenzeile (`ModeBar`) des aktiven Werkzeugs. Rufen Sie sie mit `ToolAccess.ModeBar()` ab. Jede Methode erfordert ein geöffnetes Dokument (`Document.IsOpen()`).

Zwei Möglichkeiten zum Ändern von Methoden:

- typisiert: — SelectRadio, PressButton, SetToggle, SelectItem, SetText, SelectResource
- allgemein: SetMode(index, "text") interpretiert den Text gemäß dem Methodentyp, und SelectChoice(index, n) wählt die n-te Auswahlmöglichkeit eines beliebigen Methodentyps.

Deaktivierte Methoden können nicht geändert werden. Änderungen werden genau wie Benutzerinteraktionen in der Methodenzeile angewendet.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ModeBar()` | Zustandslose Sicht auf die Methodenzeile des aktiven Werkzeugs (entspricht `ToolAccess().ModeBar()`). |

**Methoden**

*Lesen*

| Methode | Beschreibung |
|---|---|
| `GetModeCount() -> int` | Anzahl der Methodeneinträge. |
| `GetModes(maxChoices: int = 2**64 - 1) -> list[ToolMode]` | MaxChoices begrenzt fChoices jeder Methode (fChoiceCount enthält stets die vollständige Anzahl). |
| `GetMode(modeIndex: int, maxChoices: int = 2**64 - 1) -> ToolMode \| None` | Gibt die Methode für `modeIndex`, `maxChoices` zurück. |
| `GetModeType(modeIndex: int) -> ModeType \| None` | Gibt den Methodentyp am Index `modeIndex` zurück. |
| `FindMode(name: str) -> int \| None` | Index der ersten Methode, deren Beschriftung oder eine ihrer Auswahlmöglichkeiten mit `name` übereinstimmt (ohne Berücksichtigung der Groß-/Kleinschreibung). |
| `GetModeValue(modeIndex: int) -> str \| None` | Aktueller Wert als Text:<br>• Radio — Name der ausgewählten Schaltfläche (oder ihr Index, wenn sie keinen Namen hat), Toggle – "on"/"off", Button – leer,<br>• PullDown/SearchablePullDown — Text des ausgewählten Eintrags, EditText/ComboBox – Feldtext,<br>• ResourcePopup — Name des ausgewählten Zubehörs. |

*Typisierte Änderungen*

| Methode | Beschreibung |
|---|---|
| `SelectRadio(modeIndex: int, choiceIndex: int) -> bool` | Wählt die Schaltfläche `choiceIndex` der Optionsfeldgruppe am Methodenindex `modeIndex` aus. |
| `PressButton(modeIndex: int) -> bool` | Betätigt die Methodenschaltfläche am Index `modeIndex`. |
| `SetToggle(modeIndex: int, isOn: bool) -> bool` | Legt den Umschaltzustand am Index `modeIndex` fest. |
| `SelectItem(modeIndex: int, itemIndex: int) -> bool` | Wählt den Eintrag `itemIndex` der Methode `modeIndex` vom Typ Einblendmenü, Kombinationsfeld oder durchsuchbares Einblendmenü aus. |
| `SelectItem(modeIndex: int, itemNameOrId: str) -> bool` | PullDown, ComboBox oder SearchablePullDown: sucht nach dem Eintragstext oder, bei SearchablePullDown, nach der Eintrags-ID. |
| `SetText(modeIndex: int, text: str) -> bool` | EditText oder ComboBox. |

*ResourcePopup*

| Methode | Beschreibung |
|---|---|
| `SelectResource(modeIndex: int, resourceName: str) -> bool` | Wählt Zubehör anhand seines Namens aus, ohne das Zubehör-Auswahlmenü anzuzeigen. |

*Allgemeine Änderungen*

| Methode | Beschreibung |
|---|---|
| `SelectChoice(modeIndex: int, choiceIndex: int) -> bool` | Wählt die n-te Auswahlmöglichkeit: Radio – Schaltfläche n, Button – betätigen (n wird ignoriert), Toggle – n != 0 bedeutet eingeschaltet, PullDown/ComboBox/SearchablePullDown – Eintrag n. Für EditText und ResourcePopup nicht unterstützt. |
| `SetMode(modeIndex: int, value: str) -> bool` | Interpretiert `value` gemäß dem Methodentyp:<br>• Radio — Schaltflächenname, Bildkennung oder 0-basierter Index<br>• Button — betätigt die Schaltfläche (Wert wird ignoriert)<br>• Toggle — "on"/"off", "True"/"False", "yes"/"no", "1"/"0" oder "toggle"<br>• PullDown — Eintragstext oder 0-basierter Index<br>• SearchablePullDown — Eintragstext, Eintrags-ID oder 0-basierter Index<br>• ComboBox — Eintragstext, andernfalls wird der Text in das Feld eingegeben<br>• EditText — der einzugebende Text<br>• ResourcePopup — Zubehörname. |
| `SetModes(settings: list[ModeSetting]) -> bool` | Wendet die Einstellungen der Reihe nach an; bricht beim ersten Fehlschlag ab und gibt `False` zurück. |

### ToolControl

> **Vollständiger Name:** `api.ToolControl` · **Erbt von:** `api.Object`

Zustandslose Steuerung des aktiven Werkzeugs. Rufen Sie sie nach dem Aktivieren eines Werkzeugs mit `ToolAccess.Control()` ab. Jede Eingabe wird genau wie eine echte Maus- oder Tastatureingabe verarbeitet, sodass sich das aktive Werkzeug so verhält, als hätte der Benutzer es bedient (Vorschauen, Rückgängig-Funktion, vom Werkzeug beim Abschluss angezeigte Dialoge, ...).

Koordinaten:

- Modellkoordinaten (`Math.Point2D`, `Point3D`) werden exakt übernommen: Der Zeigerfang des Intelligenten Zeigers wird ausgesetzt, und das Werkzeug erhält den angegebenen Punkt, auch wenn er nicht sichtbar ist. 2D-Punkte liegen auf der Konstruktionsebene (z = 0). Werkzeuge, die Objekte unter dem Mauszeiger erfassen (Aktivieren, Umformen, ...), benötigen zusätzlich einen im aktiven Ansichtsfenster sichtbaren Punkt (siehe `ModelToView`); andernfalls wird der Mauszeiger in der Mitte des Ansichtsfensters platziert.
- Ansichtskoordinaten (`ViewPoint`) verhalten sich wie ein echter Klick auf dieses Pixel, einschließlich des Zeigerfangs des Intelligenten Zeigers. Sie müssen innerhalb des aktiven Ansichtsfensters liegen (siehe `GetViewSize`).

Typische Verwendung (zwei Klicks zeichnen im Klick-Klick-Modus ein Rechteck):

```python
import api
from api.Math import Point2D

tools = api.ToolAccess()
if tools.ActivateTool("Rectangle"):
    control = tools.Control()
    control.Click(Point2D(0.0, 0.0))
    control.Click(Point2D(1000.0, 500.0))
```

Werkzeuge mit mehreren Punkten (z. B. die Werkzeuge Polylinie und Wand) werden mit `Finish()` oder einem `DoubleClick` auf den letzten Punkt abgeschlossen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ToolControl()` | Zustandslose Steuerung des aktiven Werkzeugs (entspricht `ToolAccess().Control()`). |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `IsAvailable() -> bool` *statisch* | Ob ein aktives Ansichtsfenster vorhanden ist, das Eingaben empfangen kann. |

*Werkzeugpunkte*

| Methode | Beschreibung |
|---|---|
| `GetToolPointCount() -> int` | Bisher in das aktive Werkzeug eingegebene Punkte; leer, wenn das Werkzeug nicht in Verwendung ist. |
| `GetToolPoints() -> list[ToolPoint]` | Gibt die Werkzeugpunkte zurück. |
| `GetCurrentPoint() -> ToolPoint \| None` | Aktueller Punkt des aktiven Werkzeugs unter dem Mauszeiger. |
| `IsToolInProgress() -> bool` | True, wenn für das aktive Werkzeug Punkte eingegeben wurden (eine Werkzeugaktion läuft). |

*Koordinaten*

| Methode | Beschreibung |
|---|---|
| `GetViewSize() -> ViewSize \| None` | Gibt die Ansichtsgröße zurück. |
| `ModelToView(modelPoint: Math.Point2D) -> ViewPoint \| None` | Ansichtsposition eines Modellpunkts; `None`, wenn er außerhalb des aktiven Ansichtsfensters liegt. |
| `ModelToView(modelPoint: Point3D) -> ViewPoint \| None` | Ansichtsposition eines Modellpunkts; `None`, wenn er außerhalb des aktiven Ansichtsfensters liegt. |
| `ViewToModel(viewPoint: ViewPoint) -> Math.Point2D \| None` | 2D-Modellpunkt unter einer Ansichtsposition (in der Planansicht auf der Konstruktionsebene, sonst auf der Bildschirmebene). |

*Mauszeigereingaben*

| Methode | Beschreibung |
|---|---|
| `MoveTo(modelPoint: Math.Point2D) -> bool` | Bewegt den Mauszeiger ohne Klick; Werkzeuge aktualisieren ihre Vorschau (Gummiband) auf die neue Position. |
| `MoveTo(modelPoint: Point3D) -> bool` | Bewegt den Mauszeiger ohne Klick; Werkzeuge aktualisieren ihre Vorschau (Gummiband) auf die neue Position. |
| `MoveTo(viewPoint: ViewPoint) -> bool` | Bewegt den Mauszeiger ohne Klick; Werkzeuge aktualisieren ihre Vorschau (Gummiband) auf die neue Position. |
| `Click(modelPoint: Math.Point2D) -> bool` | Linksklick (Maustaste drücken + loslassen) – fügt in der Regel einen Werkzeugpunkt hinzu. |
| `Click(modelPoint: Point3D) -> bool` | Linksklick (Maustaste drücken + loslassen) – fügt in der Regel einen Werkzeugpunkt hinzu. |
| `Click(viewPoint: ViewPoint) -> bool` | Linksklick (Maustaste drücken + loslassen) – fügt in der Regel einen Werkzeugpunkt hinzu. |
| `DoubleClick(modelPoint: Math.Point2D) -> bool` | Doppelklick – schließt Werkzeuge mit mehreren Punkten ab oder bearbeitet das Objekt unter dem Mauszeiger (Werkzeug „Aktivieren“). |
| `DoubleClick(modelPoint: Point3D) -> bool` | Doppelklick – schließt Werkzeuge mit mehreren Punkten ab oder bearbeitet das Objekt unter dem Mauszeiger (Werkzeug „Aktivieren“). |
| `DoubleClick(viewPoint: ViewPoint) -> bool` | Doppelklick – schließt Werkzeuge mit mehreren Punkten ab oder bearbeitet das Objekt unter dem Mauszeiger (Werkzeug „Aktivieren“). |
| `Drag(from_: Math.Point2D, to: Math.Point2D) -> bool` | Maustaste bei `from` drücken, bewegen und bei `to` loslassen (Klick-Ziehen-Zeichenmodus, Aktivieren mit Auswahlrahmen, Ziehen von Objekten). |
| `Drag(from_: Point3D, to: Point3D) -> bool` | Maustaste bei `from` drücken, bewegen und bei `to` loslassen (Klick-Ziehen-Zeichenmodus, Aktivieren mit Auswahlrahmen, Ziehen von Objekten). |
| `Drag(from_: ViewPoint, to: ViewPoint) -> bool` | Maustaste bei `from` drücken, bewegen und bei `to` loslassen (Klick-Ziehen-Zeichenmodus, Aktivieren mit Auswahlrahmen, Ziehen von Objekten). |

*Tastatur- und Werkzeugaktionen*

| Methode | Beschreibung |
|---|---|
| `PressKey(key: ToolKey) -> bool` | Sendet die Taste genau so, als würde der Benutzer sie über der Zeichnung drücken. |
| `Finish() -> bool` | Schließt die aktuelle Werkzeugaktion ab (Eingabetaste). |
| `Cancel() -> bool` | Entfernt alle Werkzeugpunkte und startet die Werkzeugaktion neu; ändert die Auswahl nicht. |
| `RemoveLastPoint() -> bool` | Entfernt den zuletzt gesetzten Werkzeugpunkt. |

### ToolAccess

> **Vollständiger Name:** `api.ToolAccess` · **Erbt von:** `api.Object`

Zustandslose Schnittstelle zum Werkzeugsystem von Vectorworks. Erzeugen Sie sie bei Bedarf:

```python
import api

tools = api.ToolAccess()
for tool in tools.GetTools(api.ToolFilter.Activatable):   # what can be used now
    print(tool.fUniversalName, tool.fName)
if tools.ActivateTool("Rectangle"):                     # universal or friendly name
    for mode in tools.ModeBar().GetModes():            # inspect the mode bar
        print(mode)
    tools.ModeBar().SetMode(0, "Rotated Rectangle Mode")   # change a mode generically
```

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ToolAccess()` | Zustandslose Schnittstelle zum Werkzeugsystem. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `IsAvailable() -> bool` *statisch* | Ob Werkzeuge aktiviert und Methoden geändert werden können (setzt ein geöffnetes Dokument voraus). |

*Katalog*

| Methode | Beschreibung |
|---|---|
| `GetTools(filter: ToolFilter = ToolFilter.All) -> list[Tool]` | Gibt die Werkzeuge für `filter` zurück. |
| `FindTool(name: str) -> Tool \| None` | Sucht ein Werkzeug anhand des universellen Namens, des benutzerfreundlichen Namens oder des lokalisierten Anzeigenamens (in dieser Rangfolge). |
| `IsToolInWorkspace(name: str) -> bool` | True, wenn das Werkzeug `name` in einer Werkzeugpalette der aktuellen Arbeitsumgebung enthalten ist. |
| `CanActivateTool(name: str) -> bool` | True, wenn `ActivateTool(name)` das Werkzeug jetzt aktivieren kann. |

*Aktives Werkzeug*

| Methode | Beschreibung |
|---|---|
| `GetActiveTool() -> Tool \| None` | Gibt das aktive Werkzeug zurück. |
| `GetActiveToolUniversalName() -> str \| None` | Gibt den universellen Namen des aktiven Werkzeugs zurück. |
| `IsToolActive(name: str) -> bool` | True, wenn das Werkzeug `name` das aktive Werkzeug ist. |
| `GetActiveToolHelpMessage() -> str \| None` | Anweisungstext, den das aktive Werkzeug dem Benutzer derzeit anzeigt (z. B. „Klicken Sie, um den Startpunkt festzulegen“). |

*Aktivierung*

| Methode | Beschreibung |
|---|---|
| `ActivateTool(name: str) -> bool` | Aktiviert das Werkzeug `name` (universeller, benutzerfreundlicher oder Anzeigename). |
| `ActivateTool(name: str, modeSettings: list[ModeSetting]) -> bool` | Aktiviert das Werkzeug und wendet anschließend die Methodeneinstellungen an (siehe `ModeBar.SetModes`). |
| `ActivateTool(name: str, modeIndex: int, choiceIndex: int) -> bool` | Aktiviert das Werkzeug und wählt anschließend die n-te Auswahlmöglichkeit einer Methode (siehe `ModeBar.SelectChoice`). |
| `ActivateSelectionTool() -> bool` | Kehrt zum standardmäßigen Aktivieren-Werkzeug zurück. |

*Methoden*

| Methode | Beschreibung |
|---|---|
| `ModeBar() -> ModeBar` | Die Methodenzeile des aktiven Werkzeugs. |

*Eingabe*

| Methode | Beschreibung |
|---|---|
| `Control() -> ToolControl` | Die Steuerung des aktiven Werkzeugs (Klicken, Ziehen, Tasten). |

### MenuCommand

> **Vollständiger Name:** `api.MenuCommand` · **Erbt von:** `api.Object`

Beschreibung eines installierten Menübefehls.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `MenuCommand()` | Standardwert (Felder mit ihren Standardwerten). |
| `MenuCommand(fUniversalName, fName, fDisplayName, fCategory, fHelpText, fShortcut, fKind, fIsChunk, fIsInWorkspace, fIsEnabled)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fUniversalName` | `str` | Eindeutige Kennung; übergeben Sie sie an ExecuteMenu / FindMenuCommand. |
| `fName` | `str` | Benutzerfreundlicher englischer Name (bei Plug-in-Befehlen gleich fUniversalName). |
| `fDisplayName` | `str` | Lokalisierter Titel, der in den Menüs angezeigt wird. |
| `fCategory` | `str` | Kategorie des Befehls im Editor für Arbeitsumgebungen. |
| `fHelpText` | `str` | Kurzbeschreibung des Befehls. |
| `fShortcut` | `str` | Tastenkürzel in der aktuellen Arbeitsumgebung (kann leer sein). |
| `fKind` | `MenuCommandKind` | Art des Befehls (normaler Befehl oder Menüblock). |
| `fIsChunk` | `bool` | Stellt eine Gruppe von Einträgen bereit (siehe `MenuAccess.GetChunkItems`). |
| `fIsInWorkspace` | `bool` | In den Menüs der aktuellen Arbeitsumgebung enthalten. |
| `fIsEnabled` | `bool` | ExecuteMenu kann ihn jetzt ausführen (bei einem Menüblock: mindestens einen seiner Einträge). |

### MenuChunkItem

> **Vollständiger Name:** `api.MenuChunkItem` · **Erbt von:** `api.Object`

Ein aktueller Eintrag eines Menüblocks.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `MenuChunkItem()` | Standardwert (Felder mit ihren Standardwerten). |
| `MenuChunkItem(fIndex, fText, fIsEnabled, fIsChecked)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fIndex` | `int` | Position im Menüblock (0-basiert). |
| `fText` | `str` | Eintragstext, wie er im Menü angezeigt wird. |
| `fIsEnabled` | `bool` | ExecuteMenu kann ihn jetzt ausführen. |
| `fIsChecked` | `bool` | Das Menü zeigt ein Häkchen an (auf dem Mac immer `False`, da dieser Zustand dort nicht gemeldet wird). |

### MenuEntry

> **Vollständiger Name:** `api.MenuEntry` · **Erbt von:** `api.Object`

Ein Eintrag eines Menüs in der Menüleiste gemäß der aktuellen Arbeitsumgebung.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `MenuEntry()` | Standardwert (Felder mit ihren Standardwerten). |
| `MenuEntry(fType, fMenuPath, fText, fUniversalName, fChunkKind, fChunkItemIndex, fShortcut, fIsEnabled, fIsChecked)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fType` | `MenuEntryType` | Art des Eintrags (Befehl, Menüblockeintrag, Untermenü oder Trennlinie). |
| `fMenuPath` | `list[str]` | Titel der Menüs, die den Eintrag enthalten, ausgehend von der Menüleiste (z. B. {"Datei", "Export"}). |
| `fText` | `str` | Im Menü angezeigter Titel (bei Trennlinien leer). |
| `fUniversalName` | `str` | Command, ChunkItem: universeller Name des Befehls oder des Menüblocks. |
| `fChunkKind` | `MenuChunkKind` | ChunkItem: Art des Menüblocks. |
| `fChunkItemIndex` | `int \| None` | ChunkItem: Index des Eintrags im Menüblock. |
| `fShortcut` | `str` | Tastenkürzel (kann leer sein). |
| `fIsEnabled` | `bool` | Command, ChunkItem: ExecuteMenuEntry kann ihn jetzt ausführen. |
| `fIsChecked` | `bool` | Command, ChunkItem: Das Menü zeigt ein Häkchen an (siehe `MenuChunkItem.fIsChecked`). |

### MenuAccess

> **Vollständiger Name:** `api.MenuAccess` · **Erbt von:** `api.Object`

Zustandslose Schnittstelle zum Menüsystem von Vectorworks. Erzeugen Sie sie bei Bedarf:

```python
import api

menus = api.MenuAccess()
for entry in menus.GetMenuEntries("Modify"):          # what the Modify menu offers
    print(entry)
if menus.GetMenuStatus("Select All") == api.MenuStatus.Ready:   # universal, friendly or display name
    menus.ExecuteMenu("Select All")
for item in menus.GetChunkItems("Recent Docs"):      # current items of a chunk
    print(item)
menus.ExecuteMenu("Standard Views", "Top/Plan")           # a chunk item by its text
```

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `MenuAccess()` | Zustandslose Schnittstelle zum Menüsystem. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `IsAvailable() -> bool` *statisch* | Ob Menübefehle jetzt ausgeführt werden können: Die Menüleiste ist eingerichtet und es wird gerade kein Plug-in-Objekt neu generiert. |

*Katalog*

| Methode | Beschreibung |
|---|---|
| `GetMenuCommands(filter: MenuFilter = MenuFilter.All) -> list[MenuCommand]` | Gibt die Menübefehle für `filter` zurück. |
| `FindMenuCommand(name: str) -> MenuCommand \| None` | Sucht einen Befehl anhand des universellen Namens, des benutzerfreundlichen Namens oder des lokalisierten Anzeigenamens (in dieser Rangfolge). Bei gleicher Rangfolge hat ein in der Arbeitsumgebung enthaltener Befehl Vorrang. |
| `IsMenuCommandInWorkspace(name: str) -> bool` | True, wenn der Befehl `name` in den Menüs der aktuellen Arbeitsumgebung enthalten ist. |

*Menüleiste der aktuellen Arbeitsumgebung*

| Methode | Beschreibung |
|---|---|
| `GetMenuTitles() -> list[str]` | Titel der Menüs in der Menüleiste, von links nach rechts. |
| `GetMenuEntries() -> list[MenuEntry]` | Alle Einträge der Menüleiste in Menüreihenfolge mit Tiefensuche: Auf einen Submenu-Eintrag folgen die Einträge seines Untermenüs, und Menüblöcke werden in ihre aktuellen Einträge aufgelöst. |
| `GetMenuEntries(menuTitle: str) -> list[MenuEntry]` | Die Einträge eines Menüs der Menüleiste (siehe GetMenuTitles), einschließlich seiner Untermenüs. |
| `FindMenuEntry(path: list[str]) -> MenuEntry \| None` | Der Eintrag, dessen Menüpfad und Text `path` entsprechen, z. B. {"Ändern", "Ausrichten", "Linksbündig"}. |

*Menüblöcke*

| Methode | Beschreibung |
|---|---|
| `GetChunkItems(name: str) -> list[MenuChunkItem]` | Aktuelle Einträge eines in der Arbeitsumgebung enthaltenen Menüblocks, wie sie in der Menüleiste angezeigt werden (siehe „Menüblock“ oben). Trennlinien und Platzhalter ohne Text werden ausgelassen (fIndex behält die Position der Einträge bei). Leer, wenn `name` kein in der Arbeitsumgebung enthaltener Menüblock ist. |
| `FindChunkItem(name: str, itemText: str) -> int \| None` | Index des Menüblockeintrags, dessen Text mit `itemText` übereinstimmt. |

*Ausführung*

| Methode | Beschreibung |
|---|---|
| `GetMenuStatus(name: str) -> MenuStatus` | Ob ExecuteMenu den Befehl (oder den Menüblockeintrag) jetzt ausführen würde und gegebenenfalls warum nicht. Ohne Index wird ein Menüblock akzeptiert, wenn er genau einen Eintrag hat. |
| `GetMenuStatus(name: str, chunkItemIndex: int) -> MenuStatus` | Ob ExecuteMenu den Befehl (oder den Menüblockeintrag) jetzt ausführen würde und gegebenenfalls warum nicht. Ohne Index wird ein Menüblock akzeptiert, wenn er genau einen Eintrag hat. |
| `CanExecuteMenu(name: str) -> bool` | True, wenn `ExecuteMenu(name)` den Befehl jetzt ausführen kann. |
| `ExecuteMenu(name: str) -> bool` | Führt einen normalen Befehl oder den einzigen Eintrag eines Menüblocks aus. Verwenden Sie GetMenuStatus, um zu erfahren, warum er nicht ausgeführt wurde. |
| `ExecuteMenu(name: str, chunkItemIndex: int) -> bool` | Führt einen Menüblockeintrag aus, angegeben durch Index oder Text. |
| `ExecuteMenu(name: str, chunkItemText: str) -> bool` | Führt einen Menüblockeintrag aus, angegeben durch Index oder Text. |
| `ExecuteMenuEntry(entry: MenuEntry) -> bool` | Führt einen Eintrag des Typs Command oder ChunkItem aus GetMenuEntries aus. |

### OIPControl

> **Vollständiger Name:** `api.OIPControl` · **Erbt von:** `api.Object`

Beschreibung und aktueller Zustand eines Bedienelements der Infopalette.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `OIPControl()` | Standardwert (Felder mit ihren Standardwerten). |
| `OIPControl(fId, fPane, fType, fCoreTypeId, fParentId, fLabel, fValue, fChoices, fChoiceCount, fSelectedChoice, fIsChecked, fIsEnabled, fIsVisible, fIsReadOnly, fIsIndeterminate)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fId` | `int` | ID des Bedienelements; gültig, bis die Infopalette neu aufgebaut wird. |
| `fPane` | `OIPPane` | Bereich des Bedienelements. |
| `fType` | `OIPControlType` | Typ des Bedienelements. |
| `fCoreTypeId` | `int` | Interne Typ-ID des Bedienelements (zur Diagnose). |
| `fParentId` | `int` | ID des übergeordneten Bedienelements (0, wenn keines vorhanden ist). |
| `fLabel` | `str` | Eingabeaufforderung / Beschriftung neben dem Bedienelement. |
| `fValue` | `str` | Aktueller Wert als Text (siehe `OIPAccess.GetValue`). |
| `fChoices` | `list[str]` | RadioGroup, PullDown, ClassPullDown, LayerPullDown. |
| `fChoiceCount` | `int` | Gesamtzahl der Auswahlmöglichkeiten (fChoices kann gekürzt sein). |
| `fSelectedChoice` | `int \| None` | RadioGroup, PullDown, SearchablePullDown, ClassPullDown, LayerPullDown. |
| `fIsChecked` | `bool \| None` | CheckBox (leer bei unbestimmtem Zustand). |
| `fIsEnabled` | `bool` | Ob das Bedienelement bedienbar ist. |
| `fIsVisible` | `bool` | Ob das Bedienelement sichtbar ist. |
| `fIsReadOnly` | `bool` | EditText, das nur einen Wert anzeigt. |
| `fIsIndeterminate` | `bool` | Mehrfachauswahl mit unterschiedlichen Werten. |

### OIPSetting

> **Vollständiger Name:** `api.OIPSetting` · **Erbt von:** `api.Object`

Eine Änderungsanforderung für ein Bedienelement, die von der allgemeinen, textbasierten API verwendet wird (siehe `OIPAccess.SetValue`).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `OIPSetting()` | Standardwert (Felder mit ihren Standardwerten). |
| `OIPSetting(fPane, fControlId, fValue)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fPane` | `OIPPane` | Bereich des Bedienelements. |
| `fControlId` | `int` | ID des Bedienelements. |
| `fValue` | `str` | Wert, der wie bei `OIPAccess.SetValue` interpretiert wird. |

### OIPAccess

> **Vollständiger Name:** `api.OIPAccess` · **Erbt von:** `api.Object`

Zustandslose Schnittstelle zur Infopalette. Erzeugen Sie sie bei Bedarf:

```python
import api

oip = api.OIPAccess()
for control in oip.GetControls(api.OIPPane.Shape):     # what the OIP shows now
    print(control)
control_id = oip.FindControl(api.OIPPane.Shape, "Width")   # find a control by its label
if control_id is not None:
    oip.SetValue(api.OIPPane.Shape, control_id, "200")     # change it as the user would
```

Zwei Möglichkeiten zum Ändern von Bedienelementen:

- typisiert: `SetText`, `SetChecked`, `SelectChoice`, `PressButton`
- allgemein: `SetValue(pane, id, "text")` interpretiert den Text gemäß dem Bedienelementtyp.

Deaktivierte, ausgeblendete und schreibgeschützte Bedienelemente können nicht geändert werden.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `OIPAccess()` | Zustandslose Schnittstelle zur Infopalette. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `IsAvailable() -> bool` *statisch* | Ob auf die Infopalette zugegriffen werden kann (setzt ein geöffnetes Dokument voraus). |
| `IsPaneAvailable(pane: OIPPane) -> bool` | Ob der Bereich derzeit Bedienelemente anzeigt (erfordert aktivierte Objekte oder bei manchen Bereichen Dokumentvorgaben). |

*Lesen*

| Methode | Beschreibung |
|---|---|
| `GetControls(pane: OIPPane = OIPPane.Shape, maxChoices: int = 2**64 - 1, includeHidden: bool = False) -> list[OIPControl]` | Bedienelemente des Bereichs in ID-Reihenfolge. maxChoices begrenzt fChoices jedes Bedienelements (fChoiceCount enthält immer die vollständige Anzahl). Ausgeblendete Bedienelemente werden übersprungen, es sei denn, includeHidden ist `True`. |
| `GetControl(pane: OIPPane, controlId: int, maxChoices: int = 2**64 - 1) -> OIPControl \| None` | Gibt das Bedienelement für `pane`, `controlId`, `maxChoices` zurück. |
| `FindControl(pane: OIPPane, label: str) -> int \| None` | ID des ersten sichtbaren Bedienelements, dessen Beschriftung mit `label` übereinstimmt (ohne Berücksichtigung der Groß-/Kleinschreibung; ein abschließender ':' wird ignoriert). |
| `GetValue(pane: OIPPane, controlId: int) -> str \| None` | Aktueller Wert als Text:<br>• EditText — Feldtext, StaticText – Beschriftung, CheckBox – "on"/"off" (leer bei unbestimmtem Zustand), Button – leer,<br>• RadioGroup/PullDown/SearchablePullDown/ClassPullDown/LayerPullDown — Text des ausgewählten Eintrags, Other – leer. |

*EditText*

| Methode | Beschreibung |
|---|---|
| `SetText(pane: OIPPane, controlId: int, text: str) -> bool` | Der Text wird so eingegeben, wie ihn der Benutzer tippen würde (Einheiten und mathematische Ausdrücke werden von Vectorworks ausgewertet). |
| `SetChecked(pane: OIPPane, controlId: int, isChecked: bool) -> bool` | Legt den Ankreuzzustand fest. |
| `SelectChoice(pane: OIPPane, controlId: int, choiceIndex: int) -> bool` | RadioGroup, PullDown, SearchablePullDown, ClassPullDown, LayerPullDown. |
| `SelectChoice(pane: OIPPane, controlId: int, choiceName: str) -> bool` | RadioGroup, PullDown, SearchablePullDown, ClassPullDown, LayerPullDown. |

*Schaltfläche*

| Methode | Beschreibung |
|---|---|
| `PressButton(pane: OIPPane, controlId: int) -> bool` | Drückt die Schaltfläche und lässt sie wieder los (kann Elemente der Benutzeroberfläche anzeigen). |

*Allgemeine Änderungen*

| Methode | Beschreibung |
|---|---|
| `SetValue(pane: OIPPane, controlId: int, value: str) -> bool` | Interpretiert `value` gemäß dem Bedienelementtyp:<br>• EditText — der einzugebende Text<br>• CheckBox — "on"/"off", "True"/"False", "yes"/"no", "1"/"0" oder "toggle"<br>• RadioGroup/PullDown/SearchablePullDown/ClassPullDown/LayerPullDown — Eintragstext, andernfalls 0-basierter Index<br>• Button — betätigt die Schaltfläche (Wert wird ignoriert)<br>• StaticText/Other — nicht unterstützt. |
| `SetValues(settings: list[OIPSetting]) -> bool` | Wendet die Einstellungen der Reihe nach an; hält beim ersten Fehlschlag an und gibt `False` zurück. Die IDs der Bedienelemente müssen unmittelbar zuvor gelesen werden, da jede Änderung die Infopalette neu aufbauen kann. |

*Direktzugriff*

| Methode | Beschreibung |
|---|---|
| `NotifyChanged(pane: OIPPane, controlId: int, changeInfo: int) -> bool` | Löst für ein beliebiges Bedienelement das Ereignis „Bedienelement geändert“ mit unverarbeiteten Änderungsinformationen aus (0 für eine einfache Wertänderung; zusammengesetzte Bedienelemente verwenden eigene Änderungscodes). Der Wert muss in der Infopalette bereits gesetzt sein. Verwenden Sie dies für Bedienelemente vom Typ `OIPControlType.Other`. |
| `Refresh(pane: OIPPane) -> bool` | Baut den Bereich anhand der aktuell aktivierten Objekte neu auf. |

## Aufzählungen

### ToolKind

> **Vollständiger Name:** `api.ToolKind` · **Art:** `IntEnum`

Wie ein Werkzeug bereitgestellt wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `Unknown` | `0` |  |
| `InternalClassic` | `1` | In Vectorworks eingebaut (klassisches Werkzeug). |
| `InternalExtension` | `2` | In Vectorworks eingebaut (Erweiterungswerkzeug). |
| `ScriptPlugin` | `3` | VectorScript- / Python-Plug-in-Werkzeug. |
| `ExtensionPlugin` | `4` | Werkzeug eines externen Plug-in-Moduls. |

### ToolCreationType

> **Vollständiger Name:** `api.ToolCreationType` · **Art:** `IntEnum`

Welche Art der Interaktion das Werkzeug zum Erzeugen von Objekten verwendet.

| Element | Wert | Beschreibung |
|---|---|---|
| `Normal` | `0` | Ein reguläres Werkzeug (eigene Klickverarbeitung). |
| `Point` | `1` | Ein Klick platziert ein Punktobjekt. |
| `Line` | `2` | Zwei Klicks definieren ein linienartiges Objekt. |
| `Box` | `3` | Zwei Klicks definieren ein rechteckartiges Objekt. |
| `Path2D` | `4` | Klicks definieren ein 2D-Pfadobjekt. |
| `Path3D` | `5` | Klicks definieren ein 3D-Pfadobjekt. |
| `Custom` | `6` | Benutzerdefinierte Objekterzeugung. |

### ToolFilter

> **Vollständiger Name:** `api.ToolFilter` · **Art:** `IntEnum`

Welche Werkzeuge `ToolAccess.GetTools` zurückgibt.

| Element | Wert | Beschreibung |
|---|---|---|
| `All` | `0` | Alle in Vectorworks installierten Werkzeuge, einschließlich derjenigen, die nicht in der Arbeitsumgebung enthalten sind. |
| `Activatable` | `1` | Nur Werkzeuge, die ActivateTool jetzt aktivieren kann. |
| `InWorkspace` | `2` | Nur Werkzeuge, die in den Werkzeugpaletten der aktuellen Arbeitsumgebung enthalten sind. |

### ModeType

> **Vollständiger Name:** `api.ModeType` · **Art:** `IntEnum`

Art einer Methodengruppe in der Methodenzeile des aktiven Werkzeugs.

| Element | Wert | Beschreibung |
|---|---|---|
| `Radio` | `0` | Gruppe sich gegenseitig ausschließender Schaltflächen; genau eine ist ausgewählt. |
| `Button` | `1` | Schaltfläche, die eine Aktion ausführt (kann Elemente der Benutzeroberfläche anzeigen, z. B. das Dialogfenster mit den Einstellungen des Werkzeugs). |
| `Toggle` | `2` | Ein-/Aus-Schaltfläche. |
| `PullDown` | `3` | Einblendmenü mit einer festen Eintragsliste. |
| `EditText` | `4` | Beschriftetes Eingabefeld. |
| `ResourcePopup` | `5` | Zubehör-Auswahlmenü (Symbole, Stile, Texturen, ...), in dem anhand des Zubehörnamens ausgewählt wird. |
| `SearchablePullDown` | `6` | Einblendmenü mit Suche; Einträge werden durch Name oder ID identifiziert. |
| `ComboBox` | `7` | Eingabefeld mit einer Liste vorgeschlagener Einträge. |

### ModeButtonKind

> **Vollständiger Name:** `api.ModeButtonKind` · **Art:** `IntEnum`

Art einer Methodenschaltfläche, wie sie ein Werkzeug bei seiner Registrierung deklariert (kann vom aktuellen ModeType abweichen).

| Element | Wert | Beschreibung |
|---|---|---|
| `Radio` | `0` |  |
| `Button` | `1` |  |
| `Preferences` | `2` | Öffnet das Dialogfenster mit den Einstellungen des Werkzeugs. |
| `Check` | `3` | Umschaltfläche. |
| `EditText` | `4` |  |
| `PullDown` | `5` |  |

### ToolKey

> **Vollständiger Name:** `api.ToolKey` · **Art:** `IntEnum`

Tasten, auf die Werkzeuge bei der Punkteingabe reagieren (siehe `ToolControl.PressKey`).

| Element | Wert | Beschreibung |
|---|---|---|
| `Return` | `0` | Schließt die Aktion von Werkzeugen ab, die auf Return/Enter reagieren (z. B. Werkzeuge mit mehreren Punkten). |
| `Escape` | `1` | Entfernt alle Werkzeugpunkte; sind keine Werkzeugpunkte vorhanden, hebt dies wie die entsprechende Taste auch die Objektaktivierung auf. |
| `Backspace` | `2` | Entfernt den letzten Werkzeugpunkt. |

### MenuCommandKind

> **Vollständiger Name:** `api.MenuCommandKind` · **Art:** `IntEnum`

Wie ein Menübefehl bereitgestellt wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `Unknown` | `0` |  |
| `Internal` | `1` | In Vectorworks eingebaut; der universelle Name ist eine negative Zahl (z. B. "-28"). |
| `ScriptPlugin` | `2` | VectorScript- / Python-Plug-in-Menübefehl (.vsm-Datei). |
| `ExtensionPlugin` | `3` | Menübefehl eines externen Plug-in-Moduls. |

### MenuChunkKind

> **Vollständiger Name:** `api.MenuChunkKind` · **Art:** `IntEnum`

Art eines Menüblocks (siehe „Menüblock“ oben).

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` | Kein Menüblock: ein normaler Befehl. |
| `Regular` | `1` | Eine feste Eintragsliste. |
| `Dynamic` | `2` | Einträge, die beim Aufbau der Menüleiste erzeugt werden (z. B. die installierten Arbeitsumgebungen). |
| `Variable` | `3` | Einträge, die sich während der Ausführung von Vectorworks ändern (z. B. die zuletzt verwendeten Dateien, die geöffneten Dokumente). |

### MenuFilter

> **Vollständiger Name:** `api.MenuFilter` · **Art:** `IntEnum`

Welche Menübefehle `MenuAccess.GetMenuCommands` zurückgibt.

| Element | Wert | Beschreibung |
|---|---|---|
| `All` | `0` | Alle in Vectorworks installierten Menübefehle, einschließlich derjenigen, die nicht in der Arbeitsumgebung enthalten sind. |
| `Executable` | `1` | Nur Befehle, bei denen fIsEnabled gesetzt ist (ExecuteMenu kann sie jetzt ausführen; bei einem Menüblock: mindestens einen seiner Einträge). |
| `InWorkspace` | `2` | Nur Befehle, die in den Menüs der aktuellen Arbeitsumgebung enthalten sind. |

### MenuEntryType

> **Vollständiger Name:** `api.MenuEntryType` · **Art:** `IntEnum`

Art eines Eintrags in einem Menü der Menüleiste.

| Element | Wert | Beschreibung |
|---|---|---|
| `Command` | `0` | Ein normaler Befehl. |
| `ChunkItem` | `1` | Ein Eintrag eines Menüblocks. |
| `Submenu` | `2` | Öffnet ein Untermenü; dessen Einträge folgen auf diesen Eintrag. |
| `Separator` | `3` | Eine Trennlinie. |

### MenuStatus

> **Vollständiger Name:** `api.MenuStatus` · **Art:** `IntEnum`

Ob ein Menübefehl (oder ein Menüblockeintrag) jetzt ausgeführt werden kann und gegebenenfalls warum nicht (siehe `MenuAccess.GetMenuStatus`).

| Element | Wert | Beschreibung |
|---|---|---|
| `Ready` | `0` | ExecuteMenu kann ihn jetzt ausführen. |
| `Unavailable` | `1` | Derzeit kann kein Befehl ausgeführt werden: Die Menüleiste ist nicht eingerichtet, oder ein Plug-in-Objekt wird gerade neu berechnet. |
| `NotFound` | `2` | Kein installierter Menübefehl hat diesen Namen. |
| `NotInWorkspace` | `3` | Installiert, aber nicht in den Menüs der aktuellen Arbeitsumgebung enthalten. |
| `Disabled` | `4` | Im aktuellen Zustand deaktiviert (benötigt ein geöffnetes Dokument, aktivierte Objekte, ...) |
| `ChunkItemRequired` | `5` | Ein Menüblock mit mehreren Einträgen: Übergeben Sie den Index oder den Text des Eintrags. |
| `ChunkItemNotFound` | `6` | Der Menüblock enthält keinen Eintrag mit diesem Index oder Text, oder der Befehl ist kein Menüblock. |

### OIPPane

> **Vollständiger Name:** `api.OIPPane` · **Art:** `IntEnum`

Bereich (Reiter) der Infopalette.

| Element | Wert | Beschreibung |
|---|---|---|
| `Shape` | `0` | Geometrische und parametrische Eigenschaften. |
| `Data` | `1` | Datenbankeinträge und andere verknüpfte Daten. |
| `Render` | `2` | Texturen. |

### OIPControlType

> **Vollständiger Name:** `api.OIPControlType` · **Art:** `IntEnum`

Art eines Bedienelements der Infopalette.

| Element | Wert | Beschreibung |
|---|---|---|
| `EditText` | `0` | Eingabefeld (Zahlen, Maße, Winkel und Text), möglicherweise schreibgeschützt. |
| `StaticText` | `1` | Beschriftung oder Trennlinie. |
| `CheckBox` | `2` | Kontrollkästchen zum Ein-/Ausschalten. |
| `RadioGroup` | `3` | Optionsfelder oder Schaltflächen; genau eines bzw. eine ist ausgewählt. |
| `PullDown` | `4` | Einblendmenü (Auswahlmenü, Kombinationsfeld oder Menüschaltfläche) mit einer festen Eintragsliste. |
| `SearchablePullDown` | `5` | Einblendmenü mit Suche. |
| `Button` | `6` | Schaltfläche, die eine Aktion ausführt (kann Elemente der Benutzeroberfläche anzeigen). |
| `ClassPullDown` | `7` | Das Klasseneinblendmenü. |
| `LayerPullDown` | `8` | Das Ebeneneinblendmenü. |
| `Other` | `9` | Jedes andere Bedienelement (Rechteckposition, 3D-Position, Farbe, Liste, ...); siehe `OIPAccess.NotifyChanged`. |

---

[Zurück zum Index](README.md) · [Nach oben](#uiautomation--werkzeuge-die-methodenzeile-menüs-und-die-infopalette)
