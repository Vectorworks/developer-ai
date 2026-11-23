[English](../../PythonAPI/v2027.2/UILayoutCreate.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/UILayoutCreate.md)

# UILayoutCreate — Meldungen, Standarddialoge und Layoutdialoge

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Benutzeroberflächenklassen: `Alerts` (Meldungsfenster, Fragen, Warnungen und Fehler), `StandardDialogs` (vorgefertigte Dialoge zum Bearbeiten eines oder zweier Werte oder zur Auswahl aus einer Liste) und `LayoutDialog` (beliebige modale Dialoge, die aus einzelnen Bedienelementen aufgebaut werden, mit in Python geschriebenen Ereignisbehandlungsfunktionen). Die Werttypen `DialogEvent` und `ListBrowserEvent` sowie die Dialogaufzählungen gehören ebenfalls zu dieser Gruppe.

Dialoge sind modal: `Run()` kehrt zurück, wenn der Benutzer den Dialog schließt. Die Werte der Bedienelemente bleiben nach `Run()` lesbar.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [DialogEvent](#dialogevent)
  - [ListBrowserEvent](#listbrowserevent)
  - [DialogSize](#dialogsize)
  - [Alerts](#alerts)
  - [TextPair](#textpair)
  - [StandardDialogs](#standarddialogs)
  - [LayoutDialog](#layoutdialog)
- [Aufzählungen](#aufzählungen)
  - [DialogResult](#dialogresult)
  - [AlertButton](#alertbutton)
  - [EditRealType](#editrealtype)
  - [StaticTextStyle](#statictextstyle)
  - [CheckState](#checkstate)
  - [DialogEventType](#dialogeventtype)
  - [ListBrowserControlType](#listbrowsercontroltype)
  - [ListBrowserDisplayType](#listbrowserdisplaytype)
  - [ListBrowserEventType](#listbrowsereventtype)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`DialogEvent`](#dialogevent) | Klasse |  | Ein Ereignis, das an die Ereignisbehandlung eines Layoutdialogs übergeben wird. |
| [`ListBrowserEvent`](#listbrowserevent) | Klasse |  | Details zum letzten Ereignis einer mehrspaltigen Liste. |
| [`DialogSize`](#dialogsize) | Klasse |  | Größe eines Dialogs in Pixeln. |
| [`Alerts`](#alerts) | Klasse |  | Standardmeldungen von Vectorworks: Informationen, Fehler und Rückfragen (nur statische Funktionen). |
| [`TextPair`](#textpair) | Klasse |  | Im Dialog mit zwei Textfeldern eingegebene Werte. |
| [`StandardDialogs`](#standarddialogs) | Klasse |  | Vorgefertigte Dialoge zum Bearbeiten eines oder zweier Werte oder zur Auswahl aus einer Liste (nur statische Funktionen). |
| [`LayoutDialog`](#layoutdialog) | Klasse |  | Modaler Dialog mit Layoutverwaltung, der im Code aus einzelnen Bedienelementen aufgebaut wird. |
| [`DialogResult`](#dialogresult) | IntEnum |  | Wie ein Dialog oder eine Meldung geschlossen wurde. |
| [`AlertButton`](#alertbutton) | IntEnum |  | Standardschaltfläche einer Rückfrage. |
| [`EditRealType`](#editrealtype) | IntEnum |  | Art des in einem Eingabefeld für reelle Zahlen angezeigten Werts. |
| [`StaticTextStyle`](#statictextstyle) | IntEnum |  | Schriftstil eines statischen Texts. |
| [`CheckState`](#checkstate) | IntEnum |  | Zustand eines Kontrollkästchens mit drei Zuständen, einer Zelle in einer mehrspaltigen Liste oder eines Kontrollkästchens in einem Baumeintrag. |
| [`DialogEventType`](#dialogeventtype) | IntEnum |  | Art eines Dialogereignisses (siehe DialogEvent). |
| [`ListBrowserControlType`](#listbrowsercontroltype) | IntEnum |  | Verhalten einer Spalte in einer mehrspaltigen Liste. |
| [`ListBrowserDisplayType`](#listbrowserdisplaytype) | IntEnum |  | Was eine Spalte in einer mehrspaltigen Liste anzeigt. |
| [`ListBrowserEventType`](#listbrowsereventtype) | IntEnum |  | Was in einer mehrspaltigen Liste geschehen ist (siehe `LayoutDialog.GetListBrowserEvent`). |

## Klassen

### DialogEvent

> **Vollständiger Name:** `api.DialogEvent` · **Erbt von:** `api.Object`

Ein Ereignis, das an die Ereignisbehandlung eines Layoutdialogs übergeben wird.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DialogEvent()` | Standardwert (Felder mit ihren Standardwerten). |
| `DialogEvent(fDialogID, fControlID, fEvent, fData, fIsNegative)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fDialogID` | `int` | ID des Dialogs in der Layoutverwaltung. |
| `fControlID` | `int` | Bedienelement, das ein Control-Ereignis ausgelöst hat; 1 für Ok, 2 für Cancel, sonst 0. |
| `fEvent` | `DialogEventType` | Art des Ereignisses. |
| `fData` | `int` | Bedienelementspezifischer Wert (z. B. die neue Schiebereglerposition, die ausgewählte Farbe als 0x00RRGGBB) oder der Meldungscode für Other. |
| `fIsNegative` | `bool` | Die Layoutverwaltung hat das Bedienelementereignis mit einer negativen ID gemeldet (sekundäre Aktion, z. B. Doppelklick in einer mehrspaltigen Liste). |

### ListBrowserEvent

> **Vollständiger Name:** `api.ListBrowserEvent` · **Erbt von:** `api.Object`

Details zum letzten Ereignis einer mehrspaltigen Liste.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ListBrowserEvent()` | Standardwert (Felder mit ihren Standardwerten). |
| `ListBrowserEvent(fEvent, fRow, fColumn)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fEvent` | `ListBrowserEventType` | Art des Ereignisses einer mehrspaltigen Liste. |
| `fRow` | `int` | Zeile des Ereignisses (0-basiert). |
| `fColumn` | `int` | Spalte des Ereignisses (0-basiert). |

### DialogSize

> **Vollständiger Name:** `api.DialogSize` · **Erbt von:** `api.Object`

Größe eines Dialogs in Pixeln.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DialogSize()` | Standardwert (Felder mit ihren Standardwerten). |
| `DialogSize(fWidth, fHeight)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fWidth` | `int` | Breite in Pixeln. |
| `fHeight` | `int` | Höhe in Pixeln. |

### Alerts

> **Vollständiger Name:** `api.Alerts` · **Erbt von:** `api.Object`

Standardmeldungen von Vectorworks: Informationen, Fehler und Rückfragen (nur statische Funktionen).

**Konstruktoren**

Kann nicht aus Python instanziiert werden: Verwenden Sie die statischen Methoden der Klasse (`api.Alerts.Method(...)`).

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Inform(text: str, advice: str = '', isMinor: bool = False, category: str = '', item: str = '', checkboxText: str = '') -> None` *statisch* | Informationsmeldung mit einer OK-Schaltfläche. Eine unauffällige Meldung tritt weniger hervor (keine Hervorhebung durch ein Symbol). |
| `Critical(text: str, advice: str = '') -> None` *statisch* | Fehlermeldung mit einer OK-Schaltfläche. |
| `Question(question: str, advice: str = '', defaultButton: AlertButton = AlertButton.Ok, okText: str = '', cancelText: str = '', buttonAText: str = '', buttonBText: str = '', category: str = '', item: str = '', checkboxText: str = '') -> DialogResult` *statisch* | Rückfrage. Leere Schaltflächentexte verwenden die Standardbeschriftungen; die Schaltflächen A und B werden nur mit einem Text angezeigt. Gibt Ok, Cancel, ButtonA oder ButtonB zurück. |
| `Confirm(question: str, advice: str = '', okText: str = '', cancelText: str = '', isOkDefault: bool = True) -> bool` *statisch* | Rückfrage mit zwei Schaltflächen (z. B. okText „Ja“, cancelText „Nein“). Gibt `True` zurück, wenn die OK-Schaltfläche gewählt wurde. |
| `InformWithLink(text: str, adviceBeforeLink: str, linkTitle: str, linkURL: str, adviceAfterLink: str = '', isMinor: bool = False, category: str = '', item: str = '', checkboxText: str = '') -> None` *statisch* | Informationsmeldung, deren Hinweis einen Hyperlink enthält: adviceBeforeLink, `[linkTitle](linkURL)`, adviceAfterLink. |
| `CriticalWithLink(text: str, adviceBeforeLink: str, linkTitle: str, linkURL: str, adviceAfterLink: str = '') -> None` *statisch* | Fehlermeldung, deren Hinweis einen Hyperlink enthält. |
| `AreAlertsAllowed() -> bool` *statisch* | `False`, wenn Meldungen unterdrückt werden (z. B. bei der Ausführung im Stapelverarbeitungsmodus oder im automatisierten Testmodus). |

### TextPair

> **Vollständiger Name:** `api.TextPair` · **Erbt von:** `api.Object`

Im Dialog mit zwei Textfeldern eingegebene Werte.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `TextPair()` | Standardwert (Felder mit ihren Standardwerten). |
| `TextPair(fFirst, fSecond)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: TextPair) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: TextPair) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fFirst` | `str` | Text des ersten Felds. |
| `fSecond` | `str` | Text des zweiten Felds. |

### StandardDialogs

> **Vollständiger Name:** `api.StandardDialogs` · **Erbt von:** `api.Object`

Vorgefertigte Dialoge zum Bearbeiten eines oder zweier Werte oder zur Auswahl aus einer Liste (nur statische Funktionen).

**Konstruktoren**

Kann nicht aus Python instanziiert werden: Verwenden Sie die statischen Methoden der Klasse (`api.StandardDialogs.Method(...)`).

**Methoden**

| Methode | Beschreibung |
|---|---|
| `EditText(title: str, label: str, value: str = '', okText: str = '', cancelText: str = '', helpText: str = '', isEmptyAllowed: bool = True) -> str \| None` *statisch* | Ein einzeiliges Textfeld. Bei isEmptyAllowed gleich `False` bleibt OK deaktiviert, solange das Feld leer ist. |
| `EditMultilineText(title: str, label: str, value: str = '', width: int = 40, height: int = 10, okText: str = '', cancelText: str = '', helpText: str = '', isEmptyAllowed: bool = True) -> str \| None` *statisch* | Ein mehrzeiliges Textfeld; Breite in Standardzeichen, Höhe in Zeilen. |
| `EditTwoTexts(title: str, label1: str, label2: str, value1: str = '', value2: str = '', helpText1: str = '', helpText2: str = '', okText: str = '', cancelText: str = '') -> TextPair \| None` *statisch* | Zwei einzeilige Textfelder. |
| `EditInteger(title: str, label: str, value: int = 0, okText: str = '', cancelText: str = '', helpText: str = '') -> int \| None` *statisch* | Fragt in einem Dialog mit einem Feld eine Ganzzahl ab; `None`, wenn der Benutzer abbricht. |
| `EditReal(title: str, label: str, value: float = 0.0, okText: str = '', cancelText: str = '', helpText: str = '') -> float \| None` *statisch* | Einfache reelle Zahl. |
| `EditDimension(title: str, label: str, value: float = 0.0, okText: str = '', cancelText: str = '', helpText: str = '') -> float \| None` *statisch* | Länge in Welteinheiten, angezeigt und eingegeben in Dokumenteinheiten. |
| `EditAngle(title: str, label: str, value: float = 0.0, okText: str = '', cancelText: str = '', helpText: str = '') -> float \| None` *statisch* | Winkel in Grad. |
| `EditPoint2D(title: str, label: str, value: Point2D = Point2D(), okText: str = '', cancelText: str = '', helpText: str = '') -> Point2D \| None` *statisch* | X- und Y-Felder. |
| `EditPoint3D(title: str, label: str, value: Point3D = Point3D(), okText: str = '', cancelText: str = '', helpText: str = '') -> Point3D \| None` *statisch* | X-, Y- und Z-Felder. |
| `ChooseFromList(title: str, label: str, choices: list[str], selectedIndex: int = 0, okText: str = '', cancelText: str = '') -> int \| None` *statisch* | Auswahlliste; gibt den 0-basierten Index des ausgewählten Eintrags zurück. selectedIndex gleich -1 wählt nichts aus. |
| `ChooseManyFromList(title: str, label: str, choices: list[str], selectedIndices: list[int] = [], okText: str = '', cancelText: str = '') -> list[int] \| None` *statisch* | Auswahlliste mit Mehrfachauswahl; gibt die 0-basierten Indizes der ausgewählten Einträge zurück. |

### LayoutDialog

> **Vollständiger Name:** `api.LayoutDialog` · **Erbt von:** `api.Object`

Modaler Dialog mit Layoutverwaltung, der im Code aus einzelnen Bedienelementen aufgebaut wird. Lebenszyklus (einmalige Verwendung: ein Dialog wird höchstens einmal ausgeführt):

1. **Erzeugen** — das Layout wird mit seiner OK- und der optionalen Abbrechen-Schaltfläche erzeugt.
2. **Bedienelemente hinzufügen** — `Add<Control>(controlID, ...)` für jedes Bedienelement. Die IDs werden vom Aufrufer gewählt (3 .. 9999).
3. **Bedienelemente positionieren** — `SetFirstItem(controlID)` für das Bedienelement oben links, dann `PlaceBelow` / `PlaceRight` relativ zu einem anderen Bedienelement. Unterelemente eines Gruppenfelds, einer Reiterseite oder einer Wechselseite beginnen mit `SetFirstGroupItem(groupControlID, controlID)`. `BindEdges` und `Align*` steuern die Größenanpassung.
4. **Ereignisbehandlung registrieren** — `OnSetup`, `OnControl(controlID, handler)`, `OnOk`, `OnCancel`, ... (alle optional; Ereignisbehandlungsfunktionen sind aufrufbare Python-Objekte, die ein `DialogEvent` empfangen).
5. **Ausführen** — zeigt den Dialog an und blockiert, bis er geschlossen wird; gibt `DialogResult.Ok` oder `DialogResult.Cancel` zurück.
6. **Werte lesen** — die `Get...`-Funktionen funktionieren auch nach `Run` weiter: Die Werte aller Bedienelemente werden beim Schließen des Dialogs erfasst.

Wertfunktionen (`Set...`, `Select...`, `Add...Item`, ...) können jederzeit nach dem Hinzufügen des Bedienelements aufgerufen werden; Aufrufe vor der Anzeige des Dialogs werden vorgemerkt und in ihrer Reihenfolge unmittelbar vor der Setup-Ereignisbehandlung angewendet. `Get...`-Funktionen geben vor der Anzeige des Dialogs `None` zurück.

Indizes von Auswahlmöglichkeiten, Zeilen/Spalten mehrspaltiger Listen und Reiterseiten sind 0-basiert. Baumeinträge werden durch die von `AddTreeItem` zurückgegebene ID identifiziert; die übergeordnete ID der Wurzel ist -1. `controlID`, `referenceControlID`, `groupControlID`, `paneControlID`, `tabControlID` und `swapControlID` identifizieren Bedienelemente; `alignmentGroupID` ist eine gemeinsame Kennung zur Kantenausrichtung, kein Bedienelement; `itemID` und `parentID` identifizieren Einträge innerhalb einer Baumansicht.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `LayoutDialog(title: str, okText: str = '', cancelText: str = '', hasCancel: bool = True, isWidthResizable: bool = False, isHeightResizable: bool = False)` | Leere Angaben für okText/cancelText verwenden die Standardbeschriftungen „OK“/„Abbrechen“; bei hasCancel gleich `False` wird nur die OK-Schaltfläche angezeigt. |

**Methoden**

*Lebenszyklus*

| Methode | Beschreibung |
|---|---|
| `IsValid() -> bool` | True, wenn dieses Objekt auf einen vorhandenen Layoutdialog verweist (das Layout wurde erzeugt und noch nicht ausgeführt oder wird gerade ausgeführt). |
| `GetDialogID() -> int` | Gibt die Dialog-ID zurück (ID der Layoutverwaltung (0, wenn das Layout nicht erzeugt werden konnte)). |
| `IsRunning() -> bool` | True zwischen dem Setup-Ereignis und der Rückkehr von `Run`. |
| `WasRun() -> bool` | True, wenn `Run` zurückgekehrt ist. |
| `Run(helpID: str = '') -> DialogResult` | Zeigt den Dialog an und blockiert, bis er geschlossen wird; gibt `DialogResult.Ok` oder `DialogResult.Cancel` zurück, oder `DialogResult.None_`, wenn der Dialog bereits ausgeführt wurde oder sein Layout ungültig ist. `helpID` ist die Kennung der kontextbezogenen Hilfe. |
| `Close(isOk: bool = True) -> bool` | Schließt den laufenden Dialog aus einer Ereignisbehandlungsfunktion, als wäre OK (isOk) oder Abbrechen gedrückt worden. Die Ereignisbehandlungsfunktionen OnOk / OnCancel werden nicht aufgerufen. Gibt außerhalb einer Ereignisbehandlungsfunktion `False` zurück. |
| `CancelClose() -> None` | Aus einer Ereignisbehandlungsfunktion für OnOk oder OnCancel: den Dialog offen halten (z. B. nach einem Validierungsfehler). |

*Ereignisbehandlungsfunktionen*

| Methode | Beschreibung |
|---|---|
| `OnSetup(handler: callable(DialogEvent)) -> None` | Registriert `handler` für den Aufruf beim Einrichten des Dialogs, unmittelbar vor dessen Anzeige. |
| `OnSetdown(handler: callable(DialogEvent)) -> None` | Registriert `handler` für den Aufruf beim Schließen des Dialogs. |
| `OnOk(handler: callable(DialogEvent)) -> None` | Registriert `handler` für den Aufruf beim Drücken von OK (rufen Sie darin `CancelClose()` auf, um den Dialog offen zu halten). |
| `OnCancel(handler: callable(DialogEvent)) -> None` | Registriert `handler` für den Aufruf beim Drücken von Abbrechen (rufen Sie darin `CancelClose()` auf, um den Dialog offen zu halten). |
| `OnResize(handler: callable(DialogEvent)) -> None` | Registriert `handler` für den Aufruf bei einer Größenänderung des Dialogs. |
| `OnEditLostFocus(handler: callable(DialogEvent)) -> None` | Registriert `handler` für den Aufruf, wenn ein Eingabefeld den Fokus verliert. |
| `OnControl(controlID: int, handler: callable(DialogEvent)) -> None` | Registriert `handler` für den Aufruf, wenn das Bedienelement `controlID` geändert oder angeklickt wird. |
| `OnAnyEvent(handler: callable(DialogEvent)) -> None` | Wird bei jedem Ereignis vor der spezifischen Ereignisbehandlungsfunktion aufgerufen, auch bei Timer und Other. |
| `GetListBrowserEvent(controlID: int) -> ListBrowserEvent` | Details zum letzten Ereignis einer mehrspaltigen Liste (gültig innerhalb ihrer OnControl-Ereignisbehandlungsfunktion). |

*Positionierung (vor Run)*

| Methode | Beschreibung |
|---|---|
| `SetFirstItem(controlID: int) -> bool` | Legt das erste Element des Bedienelements `controlID` fest. |
| `SetFirstGroupItem(groupControlID: int, controlID: int) -> bool` | Legt das erste Gruppenelement des Bedienelements `controlID` fest. |
| `PlaceBelow(referenceControlID: int, controlID: int, indent: int = 0, spacing: int = 0) -> bool` | Einrückung in Standardzeichen, Abstand in Zeilen (darunter) oder Zeichen (rechts). |
| `PlaceRight(referenceControlID: int, controlID: int, indent: int = 0, spacing: int = 0) -> bool` | Platziert `controlID` rechts von `referenceControlID`. Einrückung in Standardzeichen, Abstand in Zeilen (darunter) oder Zeichen (rechts). |
| `BindEdges(controlID: int, isLeft: bool, isRight: bool, isTop: bool, isBottom: bool) -> bool` | Welche Kanten bei der Größenänderung eines größenveränderbaren Dialogs den Dialogkanten folgen. |
| `BindProportional(controlID: int, isLeft: bool, isRight: bool, isTop: bool, isBottom: bool) -> bool` | Wie `BindEdges`, jedoch bewegen sich die gewählten Kanten von `controlID` bei einer Größenänderung eines größenveränderbaren Dialogs proportional. |
| `AlignLeft(controlID: int, alignmentGroupID: int, isResizing: bool = False) -> bool` | Ordnet controlID einer Ausrichtungsgruppe für die angegebene Kante zu, nicht einem anderen Bedienelement. Bedienelemente mit derselben alignmentGroupID richten ihre entsprechenden Kanten aneinander aus. Es muss kein Bedienelement oder Gruppenfeld mit alignmentGroupID existieren; wählen Sie eine positive ID im Bereich einer vorzeichenbehafteten 16-Bit-Zahl. Bei isResizing gleich `False` wird das Bedienelement verschoben; bei `True` wird seine Größe angepasst, um die Ausrichtung zu erfüllen. |
| `AlignRight(controlID: int, alignmentGroupID: int, isResizing: bool = False) -> bool` | Richtet die rechte Kante von `controlID` an den anderen Mitgliedern der Ausrichtungsgruppe `alignmentGroupID` aus (eine Ausrichtungskennung, kein Bedienelement). |
| `AlignBottom(controlID: int, alignmentGroupID: int, isResizing: bool = False) -> bool` | Richtet die untere Kante von `controlID` an den anderen Mitgliedern der Ausrichtungsgruppe `alignmentGroupID` aus (eine Ausrichtungskennung, kein Bedienelement). |
| `SetControlSize(controlID: int, widthInPixels: int, heightInPixels: int) -> bool` | Legt die Größe des Bedienelements `controlID` fest. |

*Dialog*

| Methode | Beschreibung |
|---|---|
| `SetDialogSize(size: DialogSize) -> bool` | Legt die Dialoggröße fest. |
| `GetDialogSize() -> DialogSize \| None` | Gibt die Dialoggröße zurück. |
| `SetDialogPosition(left: int, top: int) -> bool` | Legt die Dialogposition fest. |

*Bedienelemente erzeugen (vor Run)*

| Methode | Beschreibung |
|---|---|
| `AddStaticText(controlID: int, text: str, width: int = -1, style: StaticTextStyle = StaticTextStyle.Regular) -> bool` | Fügt einen statischen Text (`width` in Zeichen, -1 = an den Text anpassen) im Stil `style` hinzu. |
| `AddCenteredStaticText(controlID: int, text: str, width: int = -1) -> bool` | Fügt einen zentrierten statischen Text hinzu (`width` in Zeichen, -1 = an den Text anpassen). |
| `AddRightStaticText(controlID: int, text: str, width: int = -1) -> bool` | Fügt einen rechtsbündigen statischen Text hinzu (`width` in Zeichen, -1 = an den Text anpassen). |
| `AddEditText(controlID: int, text: str = '', width: int = 20, heightInLines: int = 1) -> bool` | Fügt ein Textfeld mit dem Anfangstext `text` hinzu (`width` in Zeichen, `heightInLines` > 1 für ein mehrzeiliges Feld). |
| `AddEditInteger(controlID: int, value: int = 0, width: int = 10) -> bool` | Fügt ein Ganzzahlfeld mit dem Anfangswert `value` hinzu. |
| `AddEditReal(controlID: int, value: float = 0.0, type: EditRealType = EditRealType.Real, width: int = 10) -> bool` | Fügt ein Feld für reelle Zahlen mit dem Anfangswert `value` hinzu; `type` wählt einfache Zahlen, Maße, Winkel, ... |
| `AddEditPassword(controlID: int, width: int = 20) -> bool` | Fügt ein Passwortfeld hinzu (der Text wird verborgen). |
| `AddSearchBox(controlID: int, prompt: str = '', width: int = 20) -> bool` | Fügt ein Suchfeld hinzu, das `prompt` anzeigt, solange es leer ist. |
| `AddPushButton(controlID: int, text: str) -> bool` | Fügt eine Schaltfläche mit der Beschriftung `text` hinzu. |
| `AddCheckBox(controlID: int, text: str) -> bool` | Fügt ein Kontrollkästchen mit der Beschriftung `text` hinzu. |
| `AddThreeStateCheckBox(controlID: int, text: str) -> bool` | Fügt ein Kontrollkästchen mit einem zusätzlichen unbestimmten Zustand hinzu. |
| `AddRadioButton(controlID: int, text: str) -> bool` | Fügt ein Optionsfeld mit der Beschriftung `text` hinzu. |
| `AddGroupBox(controlID: int, text: str = '', hasFrame: bool = True) -> bool` | Fügt ein Gruppenfeld (einen Container für andere Bedienelemente) mit dem Titel `text` hinzu, mit oder ohne Rahmen. |
| `AddCheckBoxGroupBox(controlID: int, text: str, hasFrame: bool = True) -> bool` | Fügt ein Gruppenfeld mit einem Kontrollkästchen im Titel hinzu; das Kontrollkästchen schaltet die enthaltenen Bedienelemente frei. |
| `AddRadioButtonGroupBox(controlID: int, text: str, hasFrame: bool = True) -> bool` | Fügt ein Gruppenfeld mit einem Optionsfeld im Titel hinzu. |
| `AddPullDownMenu(controlID: int, width: int = 20) -> bool` | Fügt ein Einblendmenü hinzu (füllen Sie es mit `AddChoice` / `SetChoices`). |
| `AddListBox(controlID: int, width: int = 20, heightInLines: int = 8, isMultiSelect: bool = False) -> bool` | Fügt ein Listenfeld hinzu (`isMultiSelect` für Mehrfachauswahl). |
| `AddListBrowser(controlID: int, width: int = 40, heightInLines: int = 10) -> bool` | Fügt eine mehrspaltige Liste hinzu (eine Tabelle mit Spalten; siehe die Funktionen für mehrspaltige Listen). |
| `AddTreeControl(controlID: int, width: int = 40, heightInLines: int = 10) -> bool` | Fügt eine Baumansicht hinzu (siehe die Baumfunktionen). |
| `AddTabControl(controlID: int) -> bool` | Fügt einen Reiterbereich hinzu; fügen Sie dessen Seiten mit `AddTabPane` hinzu. |
| `AddTabPane(tabControlID: int, paneControlID: int) -> bool` | Fügt das Gruppenfeld paneControlID (sein Text ist die Reiterbeschriftung) als Seite des Reiterbereichs hinzu. |
| `AddSwapControl(controlID: int) -> bool` | Fügt einen Wechselbereich hinzu (jeweils eine Seite sichtbar); fügen Sie dessen Seiten mit `AddSwapPane` hinzu. |
| `AddSwapPane(swapControlID: int, paneControlID: int) -> bool` | Fügt das Gruppenfeld paneControlID als Seite des Wechselbereichs hinzu. |
| `AddSeparator(controlID: int, widthInPixels: int = 0) -> bool` | Fügt eine horizontale Trennlinie hinzu (`widthInPixels` gleich 0 = Standardbreite). |
| `AddColorPopup(controlID: int, width: int = -1) -> bool` | Fügt ein Farbeinblendmenü hinzu (Farbpalette des Dokuments). |
| `AddPatternPopup(controlID: int) -> bool` | Fügt ein Mustereinblendmenü hinzu. |
| `AddLineWeightPopup(controlID: int) -> bool` | Fügt ein Liniendickeneinblendmenü hinzu. |
| `AddClassPullDown(controlID: int, width: int = 30, isShowingDefaultItems: bool = True) -> bool` | Fügt ein Einblendmenü mit den Klassen des Dokuments hinzu (mit den Standardeinträgen, wenn `isShowingDefaultItems` gesetzt ist). |
| `AddLayerPullDown(controlID: int, width: int = 30, isShowingDefaultItems: bool = True) -> bool` | Fügt ein Einblendmenü mit den Ebenen des Dokuments hinzu (mit den Standardeinträgen, wenn `isShowingDefaultItems` gesetzt ist). |
| `AddColorButton(controlID: int, color: ColorRGB = ColorRGB()) -> bool` | Schaltfläche, die die Farbauswahl des Betriebssystems öffnet; die gewählte Farbe wird in `DialogEvent.fData` gemeldet. |
| `AddSlider(controlID: int, maximum: int = 100) -> bool` | Fügt einen Schieberegler mit dem Bereich von 0 bis `maximum` hinzu. |
| `AddImage(controlID: int, widthInPixels: int, heightInPixels: int, imageSpecifier: str) -> bool` | ImageSpecifier: Pfad zu einem Ressourcenbild, etwa "Vectorworks/Images/Name.png". |
| `HasControl(controlID: int) -> bool` | True, wenn ein Bedienelement mit der ID `controlID` hinzugefügt wurde. |

*Beliebiges Bedienelement*

| Methode | Beschreibung |
|---|---|
| `Enable(controlID: int, isEnabled: bool = True) -> bool` | Aktiviert oder deaktiviert das Bedienelement `controlID`. |
| `Show(controlID: int, isVisible: bool = True) -> bool` | Zeigt das Bedienelement `controlID` an oder blendet es aus. |
| `IsEnabled(controlID: int) -> bool \| None` | True, wenn das Bedienelement `controlID` bedienbar ist. |
| `IsVisible(controlID: int) -> bool \| None` | True, wenn das Bedienelement `controlID` sichtbar ist. |
| `SetFocus(controlID: int) -> bool` | Setzt den Fokus auf das Bedienelement `controlID`. |
| `SetHelpText(controlID: int, helpText: str) -> bool` | Legt den Hilfetext des Bedienelements `controlID` fest. |
| `SetToolTip(controlID: int, toolTip: str, subToolTip: str = '') -> bool` | Legt den beim Darüberfahren angezeigten Hilfetext des Bedienelements `controlID` fest. |
| `SetIndeterminate(controlID: int, isIndeterminate: bool = True) -> bool` | Legt fest, ob das Bedienelement `controlID` einen unbestimmten Zustand hat. |

*Text: statische Texte, Eingabefelder, Schaltflächen, Kontrollkästchen, Gruppenfelder*

| Methode | Beschreibung |
|---|---|
| `SetText(controlID: int, text: str) -> bool` | Legt den Text des Bedienelements `controlID` fest. |
| `GetText(controlID: int) -> str \| None` | Gibt den Text des Bedienelements `controlID` zurück. |
| `SetTextEditable(controlID: int, isEditable: bool) -> bool` | Legt fest, ob der Text des Bedienelements `controlID` bearbeitbar ist. |
| `SelectAllText(controlID: int) -> bool` | Markiert den gesamten Text des Eingabefelds `controlID`. |
| `SetTextSelection(controlID: int, start: int, end: int) -> bool` | Legt die Textmarkierung des Bedienelements `controlID` fest. |
| `SetStaticTextStyle(controlID: int, style: StaticTextStyle) -> bool` | Legt den Stil des statischen Texts im Bedienelement `controlID` fest. |
| `SetStaticTextColor(controlID: int, color: ColorRGB) -> bool` | Legt die Farbe des statischen Texts im Bedienelement `controlID` fest. |

*Kontrollkästchen, Optionsfelder, Gruppenfelder mit Kontrollkästchen / Optionsfeld*

| Methode | Beschreibung |
|---|---|
| `SetBool(controlID: int, value: bool) -> bool` | Legt den booleschen Wert des Bedienelements `controlID` fest. |
| `GetBool(controlID: int) -> bool \| None` | Ob der *boolesche Wert* des Bedienelements `controlID` wahr ist. |
| `SetCheckState(controlID: int, state: CheckState) -> bool` | Legt den Ankreuzzustand des Bedienelements `controlID` fest. |
| `GetCheckState(controlID: int) -> CheckState \| None` | Gibt den Ankreuzzustand des Bedienelements `controlID` zurück. |

*Zahlen*

| Methode | Beschreibung |
|---|---|
| `SetInteger(controlID: int, value: int) -> bool` | Legt den Ganzzahlwert des Bedienelements `controlID` fest. |
| `GetInteger(controlID: int) -> int \| None` | Gibt den Ganzzahlwert des Bedienelements `controlID` zurück. |
| `SetReal(controlID: int, value: float) -> bool` | Längen und Koordinaten in Welteinheiten, Winkel in Grad (der Typ entspricht der Angabe für AddEditReal). |
| `GetReal(controlID: int) -> float \| None` | Gibt den reellen Wert des Bedienelements `controlID` zurück. Längen und Koordinaten in Welteinheiten, Winkel in Grad (der Typ entspricht der Angabe für AddEditReal). |

*Auswahlmöglichkeiten: Einblendmenüs, Listenfelder, Klassen-/Ebeneneinblendmenüs*

| Methode | Beschreibung |
|---|---|
| `AddChoice(controlID: int, text: str, index: int = -1) -> bool` | Index -1 hängt an. |
| `SetChoices(controlID: int, choices: list[str]) -> bool` | Legt die Auswahlmöglichkeiten des Bedienelements `controlID` fest. |
| `RemoveChoice(controlID: int, index: int) -> bool` | Entfernt die Auswahlmöglichkeit am Index `index` aus einem Einblendmenü oder Listenfeld. |
| `RemoveAllChoices(controlID: int) -> bool` | Entfernt alle Auswahlmöglichkeiten aus einem Einblendmenü oder Listenfeld. |
| `GetChoiceCount(controlID: int) -> int \| None` | Anzahl der Auswahlmöglichkeiten des Bedienelements `controlID`. |
| `GetChoiceText(controlID: int, index: int) -> str \| None` | Gibt den Text der Auswahlmöglichkeit für `controlID`, `index` zurück. |
| `FindChoice(controlID: int, text: str) -> int \| None` | Index der Auswahlmöglichkeit mit dem Text `text`; `None`, wenn keine vorhanden ist. |
| `SelectChoice(controlID: int, index: int, isSelected: bool = True) -> bool` | Wählt die Auswahlmöglichkeit am Index `index` aus (oder hebt mit `isSelected=False` die Auswahl auf). |
| `SelectChoiceByText(controlID: int, text: str) -> bool` | Wählt die Auswahlmöglichkeit mit dem Text `text` aus. |
| `GetSelectedChoice(controlID: int) -> int \| None` | Erster ausgewählter Index; -1, wenn nichts ausgewählt ist. |
| `GetSelectedChoiceText(controlID: int) -> str \| None` | Gibt den Text der ausgewählten Auswahlmöglichkeit des Bedienelements `controlID` zurück. |
| `GetSelectedChoices(controlID: int) -> list[int] \| None` | Alle ausgewählten Indizes eines Listenfelds mit Mehrfachauswahl. |

*Attribut-Bedienelemente*

| Methode | Beschreibung |
|---|---|
| `SetColorButton(controlID: int, color: ColorRGB) -> bool` | Legt die Farbe der Farbschaltfläche im Bedienelement `controlID` fest. |
| `GetColorButton(controlID: int) -> ColorRGB \| None` | Gibt die Farbe der Farbschaltfläche im Bedienelement `controlID` zurück. |
| `SetColorIndex(controlID: int, colorIndex: int) -> bool` | Index in der Farbtabelle des Dokuments (Farbeinblendmenü). |
| `GetColorIndex(controlID: int) -> int \| None` | Gibt den Farbindex des Bedienelements `controlID` zurück. Index in der Farbtabelle des Dokuments (Farbeinblendmenü). |

*Mustereinblendmenü*

| Methode | Beschreibung |
|---|---|
| `SetPatternIndex(controlID: int, patternIndex: int) -> bool` | Musterindex (0 keines, 1 Hintergrund, 2 Vordergrund, ...). |
| `GetPatternIndex(controlID: int) -> int \| None` | Gibt den Musterindex des Bedienelements `controlID` zurück. Musterindex (0 keines, 1 Hintergrund, 2 Vordergrund, ...). |
| `SetLineWeight(controlID: int, lineWeight: int) -> bool` | Liniendickeneinblendmenü, in mil. |
| `GetLineWeight(controlID: int) -> int \| None` | Gibt die Liniendicke des Bedienelements `controlID` zurück. Liniendickeneinblendmenü, in mil. |

*Schieberegler und Bild*

| Methode | Beschreibung |
|---|---|
| `SetSliderValue(controlID: int, value: int) -> bool` | Legt den Schiebereglerwert des Bedienelements `controlID` fest. |
| `GetSliderValue(controlID: int) -> int \| None` | Gibt den Schiebereglerwert des Bedienelements `controlID` zurück. |
| `SetSliderLiveUpdate(controlID: int, isLive: bool) -> bool` | Legt die laufende Aktualisierung des Schiebereglers im Bedienelement `controlID` fest. |
| `SetSliderTickMarks(controlID: int, count: int) -> bool` | Legt die Skalenmarkierungen des Schiebereglers im Bedienelement `controlID` fest. |
| `SetImage(controlID: int, imageSpecifier: str) -> bool` | Legt das Bild des Bedienelements `controlID` fest. |

*Reiter- und Wechselbereiche*

| Methode | Beschreibung |
|---|---|
| `ShowTabPane(tabControlID: int, paneControlID: int) -> bool` | Bringt die Seite `paneControlID` des Reiterbereichs `tabControlID` in den Vordergrund. |
| `ShowSwapPane(swapControlID: int, paneControlID: int) -> bool` | Zeigt die Seite `paneControlID` des Wechselbereichs `swapControlID` an. |
| `GetActivePane(controlID: int) -> int \| None` | Bedienelement-ID des Gruppenfelds der sichtbaren Seite. |

*Mehrspaltige Liste*

| Methode | Beschreibung |
|---|---|
| `AddListBrowserColumn(controlID: int, header: str, widthInPixels: int = 100, column: int = -1) -> bool` | Spalte -1 hängt an; Breite in Pixeln. Gibt `False` zurück, wenn das Bedienelement keine mehrspaltige Liste ist. |
| `RemoveListBrowserColumn(controlID: int, column: int) -> bool` | Entfernt die Spalte `column` aus der mehrspaltigen Liste. |
| `GetListBrowserColumnCount(controlID: int) -> int \| None` | Anzahl der Spalten der mehrspaltigen Liste im Bedienelement `controlID`. |
| `SetListBrowserColumnWidth(controlID: int, column: int, widthInPixels: int) -> bool` | Legt die Spaltenbreite der mehrspaltigen Liste im Bedienelement `controlID` fest. |
| `SetListBrowserColumnControl(controlID: int, column: int, controlType: ListBrowserControlType) -> bool` | Legt den Bedienelementtyp einer Spalte in der mehrspaltigen Liste `controlID` fest. |
| `SetListBrowserColumnDisplay(controlID: int, column: int, itemDisplay: ListBrowserDisplayType, editDisplay: ListBrowserDisplayType = ListBrowserDisplayType.TextOnly) -> bool` | Legt die Spaltendarstellung der mehrspaltigen Liste im Bedienelement `controlID` fest. |
| `AddListBrowserColumnChoice(controlID: int, column: int, text: str, imageOn: int = -1, imageOff: int = -1, data: int = 0) -> bool` | Wert, den eine Zelle vom Typ MultiState / SingleInstance / Radio annehmen kann; gibt bei einem Fehlschlag `False` zurück. |
| `SetListBrowserCellChoice(controlID: int, row: int, column: int, choiceIndex: int) -> bool` | Setzt die Zelle auf einen der mit AddListBrowserColumnChoice hinzugefügten Werte. |
| `AddListBrowserRow(controlID: int, text: str, row: int = -1) -> bool` | Zeile -1 hängt an. text ist der Text der ersten Spalte. |
| `AddListBrowserRowCells(controlID: int, cells: list[str]) -> bool` | Hängt eine Zeile mit einem Text je Spalte an. |
| `RemoveListBrowserRow(controlID: int, row: int) -> bool` | Entfernt die Zeile `row` aus der mehrspaltigen Liste. |
| `RemoveAllListBrowserRows(controlID: int) -> bool` | Entfernt alle Zeilen aus der mehrspaltigen Liste. |
| `GetListBrowserRowCount(controlID: int) -> int \| None` | Anzahl der Zeilen der mehrspaltigen Liste im Bedienelement `controlID`. |
| `SetListBrowserCell(controlID: int, row: int, column: int, text: str, imageIndex: int = -1) -> bool` | Legt den Zellwert der mehrspaltigen Liste im Bedienelement `controlID` fest. |
| `GetListBrowserCell(controlID: int, row: int, column: int) -> str \| None` | Gibt die Zelle der mehrspaltigen Liste für `controlID`, `row`, `column` zurück. |
| `SetListBrowserCellData(controlID: int, row: int, column: int, data: int) -> bool` | Legt die Zelldaten der mehrspaltigen Liste im Bedienelement `controlID` fest. |
| `GetListBrowserCellData(controlID: int, row: int, column: int) -> int \| None` | Gibt die Zelldaten der mehrspaltigen Liste für `controlID`, `row`, `column` zurück. |
| `SetListBrowserCellCheckState(controlID: int, row: int, column: int, state: CheckState) -> bool` | Legt den Ankreuzzustand einer Zelle der mehrspaltigen Liste im Bedienelement `controlID` fest. |
| `GetListBrowserCellCheckState(controlID: int, row: int, column: int) -> CheckState \| None` | Gibt den Ankreuzzustand der Zelle der mehrspaltigen Liste für `controlID`, `row`, `column` zurück. |
| `SetListBrowserCellTextColor(controlID: int, row: int, column: int, color: ColorRGB) -> bool` | Legt die Textfarbe einer Zelle der mehrspaltigen Liste im Bedienelement `controlID` fest. |
| `SetListBrowserCellReadOnly(controlID: int, row: int, column: int, isReadOnly: bool = True) -> bool` | Legt den Schreibschutz einer Zelle der mehrspaltigen Liste im Bedienelement `controlID` fest. |
| `SetListBrowserReadOnly(controlID: int, isReadOnly: bool = True) -> bool` | Legt den Schreibschutz der mehrspaltigen Liste im Bedienelement `controlID` fest. |
| `SelectListBrowserRows(controlID: int, firstRow: int, lastRow: int, isSelected: bool = True) -> bool` | Wählt die Zeilen `firstRow` .. `lastRow` aus (oder hebt ihre Auswahl auf). |
| `IsListBrowserRowSelected(controlID: int, row: int) -> bool \| None` | True, wenn die Zeile `row` der mehrspaltigen Liste ausgewählt ist. |
| `GetListBrowserSelectedRows(controlID: int) -> list[int] \| None` | Gibt die ausgewählten Zeilen der mehrspaltigen Liste im Bedienelement `controlID` zurück. |
| `EnableListBrowserSorting(controlID: int, isEnabled: bool = True) -> bool` | Ermöglicht dem Benutzer, die Zeilen durch Klicken auf eine Spaltenüberschrift zu sortieren. |
| `SetListBrowserSortColumn(controlID: int, column: int, isAscending: bool = True) -> bool` | Legt die Sortierspalte der mehrspaltigen Liste im Bedienelement `controlID` fest. |
| `EnableListBrowserSingleSelection(controlID: int, isEnabled: bool = True) -> bool` | Beschränkt die mehrspaltige Liste auf die Auswahl einer einzigen Zeile. |
| `EnableListBrowserDragAndDrop(controlID: int, isEnabled: bool = True) -> bool` | Ermöglicht dem Benutzer, die Zeilen durch Ziehen und Ablegen neu anzuordnen. |
| `ShowListBrowserHeader(controlID: int, isVisible: bool = True) -> bool` | Zeigt die Zeile mit den Spaltenüberschriften an oder blendet sie aus. |
| `EnsureListBrowserRowVisible(controlID: int, row: int) -> bool` | Scrollt die mehrspaltige Liste so, dass die Zeile `row` sichtbar ist. |
| `EnableListBrowserUpdates(controlID: int, isEnabled: bool) -> bool` | Setzt das Neuzeichnen aus, während viele Zeilen geändert werden; rufen Sie die Methode anschließend erneut mit `True` und zusätzlich RefreshListBrowser auf. |
| `RefreshListBrowser(controlID: int) -> bool` | Zeichnet die mehrspaltige Liste neu (nachdem Aktualisierungen mit `EnableListBrowserUpdates` ausgesetzt wurden). |

*Baumansicht*

| Methode | Beschreibung |
|---|---|
| `AddTreeItem(controlID: int, text: str, parentID: int = -1) -> int \| None` | Hängt einen Eintrag unter parentID an (-1 = Wurzel). Gibt die neue Eintrags-ID zurück, oder `None`, wenn der Dialog nicht läuft (Baumeinträge können erst ab der Setup-Ereignisbehandlung hinzugefügt werden). |
| `RemoveTreeItem(controlID: int, itemID: int) -> bool` | Entfernt den Baumeintrag `itemID` und seine Untereinträge. |
| `RemoveAllTreeItems(controlID: int) -> bool` | Entfernt alle Baumeinträge. |
| `GetTreeItemText(controlID: int, itemID: int) -> str \| None` | Gibt den Text des Baumeintrags für `controlID`, `itemID` zurück. |
| `GetTreeItemParent(controlID: int, itemID: int) -> int \| None` | Gibt den übergeordneten Baumeintrag für `controlID`, `itemID` zurück. |
| `GetTreeItemChildren(controlID: int, itemID: int) -> list[int] \| None` | Gibt die Untereinträge des Baumeintrags für `controlID`, `itemID` zurück. |
| `SetTreeItemData(controlID: int, itemID: int, data: int) -> bool` | Legt die Daten eines Baumeintrags im Bedienelement `controlID` fest. |
| `GetTreeItemData(controlID: int, itemID: int) -> int \| None` | Gibt die Daten des Baumeintrags für `controlID`, `itemID` zurück. |
| `SetTreeItemCheckState(controlID: int, itemID: int, state: CheckState, isClickable: bool = True) -> bool` | Legt den Ankreuzzustand eines Baumeintrags im Bedienelement `controlID` fest. |
| `GetTreeItemCheckState(controlID: int, itemID: int) -> CheckState \| None` | Gibt den Ankreuzzustand des Baumeintrags für `controlID`, `itemID` zurück. |
| `ExpandTreeItem(controlID: int, itemID: int, isExpanded: bool = True) -> bool` | Klappt den Baumeintrag `itemID` auf (oder mit `isExpanded=False` zu). |
| `IsTreeItemExpanded(controlID: int, itemID: int) -> bool \| None` | True, wenn der Baumeintrag `itemID` aufgeklappt ist. |
| `SelectTreeItem(controlID: int, itemID: int) -> bool` | Wählt den Baumeintrag `itemID` aus. |
| `GetSelectedTreeItem(controlID: int) -> int \| None` | -1, wenn nichts ausgewählt ist. |
| `GetSelectedTreeItems(controlID: int) -> list[int] \| None` | Gibt die ausgewählten Baumeinträge des Bedienelements `controlID` zurück. |
| `EnableTreeMultiSelection(controlID: int, isEnabled: bool = True) -> bool` | Erlaubt die Auswahl mehrerer Baumeinträge. |

## Aufzählungen

### DialogResult

> **Vollständiger Name:** `api.DialogResult` · **Art:** `IntEnum`

Wie ein Dialog oder eine Meldung geschlossen wurde.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` | Der Dialog konnte nicht angezeigt werden. |
| `Ok` | `1` | Die Standardschaltfläche (OK). |
| `Cancel` | `2` | Die Abbrechen-Schaltfläche, Escape oder die Schließen-Schaltfläche. |
| `ButtonA` | `3` | Benutzerdefinierte Schaltfläche A einer Rückfrage. |
| `ButtonB` | `4` | Benutzerdefinierte Schaltfläche B einer Rückfrage. |

### AlertButton

> **Vollständiger Name:** `api.AlertButton` · **Art:** `IntEnum`

Standardschaltfläche einer Rückfrage.

| Element | Wert | Beschreibung |
|---|---|---|
| `Cancel` | `0` |  |
| `Ok` | `1` |  |
| `ButtonA` | `2` |  |
| `ButtonB` | `3` |  |

### EditRealType

> **Vollständiger Name:** `api.EditRealType` · **Art:** `IntEnum`

Art des in einem Eingabefeld für reelle Zahlen angezeigten Werts. Längen und Koordinaten werden in Welteinheiten (mm) übergeben; das Feld zeigt sie in Dokumenteinheiten an und wertet Eingaben in diesen Einheiten aus.

| Element | Wert | Beschreibung |
|---|---|---|
| `Real` | `1` | Einfache Zahl. |
| `Angle` | `2` | Winkel in Grad. |
| `Dimension` | `3` | Länge in Welteinheiten. |
| `CoordinateX` | `4` | X-Koordinate (berücksichtigt den Benutzernullpunkt). |
| `CoordinateY` | `5` | Y-Koordinate (berücksichtigt den Benutzernullpunkt). |

### StaticTextStyle

> **Vollständiger Name:** `api.StaticTextStyle` · **Art:** `IntEnum`

Schriftstil eines statischen Texts.

| Element | Wert | Beschreibung |
|---|---|---|
| `Regular` | `0` |  |
| `Caption` | `1` |  |
| `Bold` | `2` |  |
| `Reduced` | `3` | Kleine Systemschrift (macOS), normale Größe unter Windows. |

### CheckState

> **Vollständiger Name:** `api.CheckState` · **Art:** `IntEnum`

Zustand eines Kontrollkästchens mit drei Zuständen, einer Zelle in einer mehrspaltigen Liste oder eines Kontrollkästchens in einem Baumeintrag.

| Element | Wert | Beschreibung |
|---|---|---|
| `Off` | `0` |  |
| `On` | `1` |  |
| `Mixed` | `2` |  |

### DialogEventType

> **Vollständiger Name:** `api.DialogEventType` · **Art:** `IntEnum`

Art eines Dialogereignisses (siehe DialogEvent).

| Element | Wert | Beschreibung |
|---|---|---|
| `Setup` | `0` | Der Dialog wird gleich angezeigt; initialisieren Sie hier die Bedienelemente. |
| `Setdown` | `1` | Der Dialog wird gleich gelöscht. |
| `Ok` | `2` | Die OK-Schaltfläche (Standardschaltfläche) wurde gedrückt; rufen Sie `LayoutDialog.CancelClose` auf, um den Dialog offen zu halten. |
| `Cancel` | `3` | Die Abbrechen-Schaltfläche wurde gedrückt; rufen Sie `LayoutDialog.CancelClose` auf, um den Dialog offen zu halten. |
| `Control` | `4` | Ein Bedienelement wurde geändert oder angeklickt (fControlID, fData). |
| `Resize` | `5` | Der Benutzer hat die Dialoggröße geändert. |
| `Timer` | `6` | Zeitgeberimpuls. |
| `EditLostFocus` | `7` | Ein Eingabefeld hat den Tastaturfokus verloren. |
| `Other` | `8` | Jede andere Meldung der Layoutverwaltung (fData enthält den unverarbeiteten Meldungscode). |

### ListBrowserControlType

> **Vollständiger Name:** `api.ListBrowserControlType` · **Art:** `IntEnum`

Verhalten einer Spalte in einer mehrspaltigen Liste.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `1` | Einfache Text- oder Bildzellen. |
| `Radio` | `2` | Eine angekreuzte Zelle je Spalte. |
| `MultiState` | `3` | Klicken durchläuft zyklisch die Spaltendateneinträge. |
| `SingleInstance` | `4` | Klicken schaltet die Zelle zwischen den Spaltendateneinträgen 0 und 1 um. |
| `NoClick` | `5` | Zellen reagieren nicht auf Klicks. |
| `Number` | `6` | Bearbeitbare Zahlenzellen. |
| `MultipleImages` | `7` | Mehrere Bilder je Zelle. |
| `DiscTriangle` | `8` | Dreieck zum Auf-/Zuklappen (hierarchische Zeilen). |

### ListBrowserDisplayType

> **Vollständiger Name:** `api.ListBrowserDisplayType` · **Art:** `IntEnum`

Was eine Spalte in einer mehrspaltigen Liste anzeigt.

| Element | Wert | Beschreibung |
|---|---|---|
| `ImageOnly` | `1` |  |
| `TextOnly` | `2` |  |
| `ImageAndText` | `3` |  |

### ListBrowserEventType

> **Vollständiger Name:** `api.ListBrowserEventType` · **Art:** `IntEnum`

Was in einer mehrspaltigen Liste geschehen ist (siehe `LayoutDialog.GetListBrowserEvent`).

| Element | Wert | Beschreibung |
|---|---|---|
| `Unknown` | `0` |  |
| `DataChangeClick` | `1` |  |
| `DataChangeAllClick` | `2` |  |
| `SelectionChangeClick` | `3` |  |
| `DoubleClick` | `4` |  |
| `DeleteKeyPressed` | `5` |  |
| `UpKey` | `6` |  |
| `DownKey` | `7` |  |
| `AlphaNumericKey` | `8` |  |
| `SortOccurred` | `9` |  |
| `SelectionMultChangeClick` | `10` |  |
| `EnterKey` | `11` |  |
| `DataChangeRecursiveClick` | `12` |  |
| `DoubleAllClick` | `13` |  |
| `DoubleRecursiveClick` | `14` |  |
| `ReceivingDragAndDrop` | `15` |  |
| `DragAndDrop` | `16` |  |

---

[Zurück zum Index](README.md) · [Nach oben](#uilayoutcreate--meldungen-standarddialoge-und-layoutdialoge)
