[English](../../PythonAPI/v2027.2/ObjectsArchitect.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/ObjectsArchitect.md)

# ObjectsArchitect — Wände, Dächer, Böden/Decken, Fenster, Türen, Stützen, Treppen

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Klassen der wichtigsten Architekturobjekte. `ArchitectObject` ist ihre gemeinsame Basisklasse (sie erweitert `PrimitiveObject` um den Zugriff auf die Parameter von Plug-in-Objekten; bei Wänden und Dächern liefern diese Zugriffsmethoden keine Werte).

Wände (`WallObject`) und Dächer (`RoofObject`) sind native Vectorworks-Objekte. Böden/Decken, Fenster, Türen, Stützen und Treppen sind Plug-in-Objekte, die anhand ihres universellen Namens ("Slab", "Window", "Door", "Column2", "Stairs CW") erkannt werden; die statische Methode `Is(h)` jeder Klasse prüft diesen.

Konventionen: `Is(h)` prüft die Objektart, `Create(...)` erzeugt eine neue Instanz auf der aktiven Ebene / im aktuellen Container, typisierte Lesemethoden geben bei einem ungültigen Objekt oder einem fehlenden Feld `None` zurück, typisierte Schreibmethoden bei Erfolg `True`. `WindowObject.Create` und `DoorObject.Create` platzieren eine frei stehende Instanz an einem Punkt.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [ArchitectObject](#architectobject)
  - [WallObject](#wallobject)
    - [WallObject.Heights](#wallobjectheights)
    - [WallObject.HeightBound](#wallobjectheightbound)
    - [WallObject.Caps](#wallobjectcaps)
    - [WallObject.BoundStatus](#wallobjectboundstatus)
    - [WallObject.BoundKind](#wallobjectboundkind)
  - [SlabObject](#slabobject)
  - [RoofObject](#roofobject)
    - [RoofObject.Attributes](#roofobjectattributes)
    - [RoofObject.Accessories](#roofobjectaccessories)
    - [RoofObject.Edge](#roofobjectedge)
    - [RoofObject.MiterType](#roofobjectmitertype)
  - [WindowObject](#windowobject)
  - [DoorObject](#doorobject)
  - [ColumnObject](#columnobject)
  - [StairObject](#stairobject)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`ArchitectObject`](#architectobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Gemeinsame Basisklasse der Architect-Objektklassen (Wand, Boden/Decke, Dach, Fenster, Tür, Stütze, Treppe). |
| [`WallObject`](#wallobject) | Klasse | [`ArchitectObject`](#architectobject) | Wand (`ObjectType.Wall`) - eine gerade oder runde Wand, in die Fenster, Türen und andere Wandobjekte eingesetzt werden können. |
| [`WallObject.Heights`](#wallobjectheights) | Klasse (verschachtelt) |  | Höhen (Welteinheiten) relativ zur Ebenenbasishöhe (0 = Oberkante der Ebene, negativ = darunter). |
| [`WallObject.HeightBound`](#wallobjectheightbound) | Klasse (verschachtelt) |  | Bezug der Wandunter- oder -oberkante: woran sich ihre Höhe orientiert. |
| [`WallObject.Caps`](#wallobjectcaps) | Klasse (verschachtelt) |  | Endabschlüsse. |
| [`WallObject.BoundStatus`](#wallobjectboundstatus) | IntEnum (verschachtelt) |  | Status eines Wandhöhenbezugs (`WallObject.HeightBound.fStatus`). |
| [`WallObject.BoundKind`](#wallobjectboundkind) | IntEnum (verschachtelt) |  | Woran sich ein Wandhöhenbezug orientiert: an der Ebenenbasishöhe, der Ebenenwandhöhe oder einer Geschossreferenzhöhe. |
| [`SlabObject`](#slabobject) | Klasse | [`ArchitectObject`](#architectobject) | Boden/Decke – ein horizontales Element (Boden, Dachdecke, Geschossdecke, ...), das durch ein 2D-Begrenzungsprofil definiert und um seine Dicke vertikal extrudiert wird. |
| [`RoofObject`](#roofobject) | Klasse | [`ArchitectObject`](#architectobject) | Dach (`ObjectType.RoofContainer`) – ein polygonales Dach, das durch eine Liste von Kanten definiert wird. |
| [`RoofObject.Attributes`](#roofobjectattributes) | Klasse (verschachtelt) |  | Attribute des gesamten Dachs. |
| [`RoofObject.Accessories`](#roofobjectaccessories) | Klasse (verschachtelt) |  | Dachelemente entlang des Umfangs. |
| [`RoofObject.Edge`](#roofobjectedge) | Klasse (verschachtelt) |  | Dachkanten (Polygoneckpunkt + Neigung und Überstand pro Kante) in der Reihenfolge des Dachumrisses. |
| [`RoofObject.MiterType`](#roofobjectmitertype) | IntEnum (verschachtelt) |  | Gehrungsarten für die Dachkanten (Verbindung zweier benachbarter geneigter Flächen). |
| [`WindowObject`](#windowobject) | Klasse | [`ArchitectObject`](#architectobject) | Plug-in-Objekt Fenster (universeller Name "Window") aus dem Plug-in Architectural Objects. |
| [`DoorObject`](#doorobject) | Klasse | [`ArchitectObject`](#architectobject) | Plug-in-Objekt Tür (universeller Name "Door") aus dem Plug-in Architectural Objects. |
| [`ColumnObject`](#columnobject) | Klasse | [`ArchitectObject`](#architectobject) | Plug-in-Objekt Stütze – die Vectorworks-Stütze, universeller Name "Column2". |
| [`StairObject`](#stairobject) | Klasse | [`ArchitectObject`](#architectobject) | Plug-in-Objekt Treppe – die Vectorworks-Treppe, universeller Name "Stairs CW". |

## Klassen

### ArchitectObject

> **Vollständiger Name:** `api.ArchitectObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Gemeinsame Basisklasse der Architect-Objektklassen (Wand, Boden/Decke, Dach, Fenster, Tür, Stütze, Treppe).

Die Architekturobjekte lassen sich in zwei Gruppen einteilen:

- Native Containerobjekte mit eigenen Objekttypen (Wand = `ObjectType.Wall`, Dach = `ObjectType.RoofContainer`). Jedes bietet typisierte Zugriffsmethoden (Höhen, Dicke, Stil, ...). Sie sind KEINE Plug-in-Objekte; daher liefern die nachfolgenden Zugriffsmethoden auf die Parameterdatenbank leere Werte / False.
- Plug-in-Objekte, in der API auch parametrische Objekte genannt (Boden/Decke "Slab", Fenster "Window", Tür "Door", Stütze "Column2", Treppe "Stairs CW"). Diese speichern ihre Konfiguration in einer Datenbank; die nachfolgenden Parameterzugriffsmethoden dienen hauptsächlich zum Lesen / Schreiben dieser Felder. Boden/Decke bietet außerdem typisierte Zugriffsmethoden; ein Bodenobjekt (`ObjectType.Slab` der Bodenart) ist ein natives Boden/Decke-Objekt ohne Datenbank.

Jede Unterklasse erbt die allgemeine API von PrimitiveObject (Identität, Klasse, Attribute, Hierarchie, Begrenzungen, Verschieben/Drehen/Skalieren/Spiegeln, Löschen, ...). Konventionen:

- Lesemethoden geben bei einem ungültigen Objekt oder fehlenden Parameter `None` zurück.
- Schreibmethoden geben bei Erfolg `True` und bei einem ungültigen Objekt oder fehlenden Parameter `False` zurück.
- Längen werden in Welteinheiten angegeben, Winkel im Bogenmaß (sofern ein bestimmter Parameter nicht ausdrücklich in Grad dokumentiert ist), Zeichenfolgen sind UTF-8-kodiert.

Grundlagen des Parameterzugriffs (Get/SetParam*):

- Gilt nur für Plug-in-Objekte (Böden/Decken, Fenster, Türen, Stützen, Treppen). Bei einer Wand, einem Dach oder einem Bodenobjekt geben die Parameterzugriffsmethoden None / False zurück, da das zugrunde liegende Objekt keine Parameterdatenbank besitzt.
- Die Klassen Window, Door, Column und Stair führen die verfügbaren Parameternamen in ihrer „Vollständigen Parameterreferenz“ auf; `GetParamNames()` listet die Parameter jedes dieser Objekte auf, auch die von Boden/Decke. Verwenden Sie diese Namen unverändert (Groß-/Kleinschreibung beachten, UTF-8) mit GetParamString / SetParamString / GetParamReal / ..., um Felder zu lesen oder zu schreiben, für die die Unterklasse keine eigene typisierte Zugriffsmethode anbietet.
- Für Parametertypen werden in den Tabellen folgende Kennzeichnungen verwendet:

- Zeichenfolge — Text (UTF-8) - GetParamString / SetParamString
- int — 32-Bit-Ganzzahl - GetParamInt / SetParamInt
- bool — boolescher Wert (kann als Zeichenfolge "True"/"False" gespeichert sein) - GetParamBool / SetParamBool
- reell — Gleitkommawert (Weltkoordinate, Winkel in Grad, einfache Zahl, Fläche, ...) - GetParamReal / SetParamReal
- Auswahlliste — Auswahl einer Zeichenkette aus N Möglichkeiten - GetParamString / SetParamString; gültige Werte stehen neben dem Parameter

- Namen, die mit "__" beginnen, bezeichnen den internen Zustand des Plug-ins; sie sind lesbar, sollten jedoch normalerweise nicht direkt beschrieben werden.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ArchitectObject(h: Handle)` | Verweist auf ein beliebiges Objekt `h` als generisches `ArchitectObject`; `IsValid()` prüft nur, ob das Handle nicht null ist. Prüfen Sie die Objektart mit `GetParametricName()` oder mit `Is(h)` einer konkreten Klasse. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `GetParametricName() -> str \| None` | Universeller (parametrischer) Name des Objekts, z. B. "Slab", "Window", "Door", "Column2", "Stairs CW". Leer bei nativen Wand- / Dachobjekten, Bodenobjekten und Handles, die auf kein Plug-in-Objekt verweisen. |
| `HasParam(univParamName: str) -> bool` | Ob dieses Plug-in-Objekt ein Feld mit dem angegebenen universellen Namen besitzt. Gibt bei nativen Wand- / Dachobjekten und Bodenobjekten immer `False` zurück. |
| `GetParamNames() -> list[str]` | Geordnete Liste aller (universellen) Parameternamen, die das Plug-in dieses Objekts definiert. Leer bei nativen Wand- / Dachobjekten und Bodenobjekten. |
| `GetParamString(univParamName: str) -> str \| None` | Allgemeine Feldzugriffsmethoden mit Zeichenfolgen als Schlüsseln. Bevorzugen Sie die typisierten, benannten Zugriffsmethoden der Unterklassen, sofern vorhanden. Verwenden Sie diese Methoden für Parameter ohne eigene Zugriffsmethode. |
| `SetParamString(univParamName: str, value: str) -> bool` | Setzt den Zeichenfolgenwert des Parameters. Allgemeine Feldzugriffsmethoden mit Zeichenfolgen als Schlüsseln. Bevorzugen Sie die typisierten, benannten Zugriffsmethoden der Unterklassen, sofern vorhanden. Verwenden Sie diese Methoden für Parameter ohne eigene Zugriffsmethode. |
| `GetParamReal(univParamName: str) -> float \| None` | Gibt den Parameterwert vom Typ real für `univParamName` zurück. |
| `SetParamReal(univParamName: str, value: float) -> bool` | Setzt den Parameterwert vom Typ real. |
| `GetParamBool(univParamName: str) -> bool \| None` | Ob *Boolescher Parameter* für `univParamName` aktiviert ist. |
| `SetParamBool(univParamName: str, value: bool) -> bool` | Setzt den booleschen Parameterwert. |
| `GetParamInt(univParamName: str) -> int \| None` | Gibt den ganzzahligen Parameterwert für `univParamName` zurück. |
| `SetParamInt(univParamName: str, value: int) -> bool` | Setzt den ganzzahligen Parameterwert. |

*Objektstil*

| Methode | Beschreibung |
|---|---|
| `GetPluginStyleName() -> str \| None` | Name des Objektstils (Zubehör) des Objekts; leer, wenn das Objekt keinen Stil hat, kein Plug-in-Objekt ist (native Wand- / Dachobjekte, Bodenobjekte) oder ungültig ist. |
| `IsParamSetByStyle(univParamName: str) -> bool` | Ob der Objektstil des Objekts den Parameter `univParamName` festlegt: Der Stil übernimmt ihn „nach Stil“, „nach Katalog“ (auch ein Parameter des vom Stil verwendeten Katalogs) oder „gemischt“ (ein Zustand in den Stildialogen, der als durch den Stil festgelegt behandelt wird). `False` bei einem Parameter, den das Objekt „nach Instanz“ übernimmt, bei einem Objekt ohne Stil und bei einem Objekt, das kein Plug-in-Objekt ist. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### WallObject

> **Vollständiger Name:** `api.WallObject` · **Erbt von:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Wand (`ObjectType.Wall`) - eine gerade oder runde Wand, in die Fenster, Türen und andere Wandobjekte eingesetzt werden können.

Eine Wand besitzt Höhen an beiden Enden (Ober- und Unterkante relativ zur Ebenenbasishöhe), eine Dicke, einen optionalen Wandstil (der ihre Schalen steuert), linke / rechte / runde Abschlüsse sowie mehrere berechnete Flächen / Längen / Höhen, die nur lesbar sind. Öffnungen und eingesetzte Objekte sind als untergeordnete Objekte der Wand gespeichert.

Eine Wand ist KEIN Plug-in-Objekt; die von ArchitectObject geerbten allgemeinen Get/SetParam*-Zugriffsmethoden liefern leere Werte / False. Verwenden Sie die nachfolgenden typisierten Zugriffsmethoden und für die grafischen Attribute das geerbte ObjectAttributes der Wand.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `WallObject(h: Handle)` | Verweist auf die vorhandene Wand `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(start: Math.Point2D, end: Math.Point2D, thickness: float = 0.0) -> WallObject` *statisch* | Erzeugt eine gerade Wand zwischen `start` und `end` auf der aktiven Ebene / im aktuellen Container. Bei `thickness` = 0 wird die Dicke aus den aktiven Wandeinstellungen verwendet. |
| `CreateRound(start: Math.Point2D, onArc: Math.Point2D, end: Math.Point2D, thickness: float = 0.0) -> WallObject` *statisch* | Erstellt eine runde Wand durch die drei angegebenen Punkte (Startpunkt, ein Punkt auf dem Kreisbogen, Endpunkt). |
| `Duplicate() -> WallObject` | Dupliziert die Wand in der Zeichnung und gibt die Kopie zurück. |

*Geometrie*

| Methode | Beschreibung |
|---|---|
| `GetLine() -> Math.Line2D \| None` | Linie vom Start- zum Endpunkt der Wand. Leer bei einer runden Wand. |
| `SetLine(start: Math.Point2D, end: Math.Point2D) -> bool` | Setzt die Linie. Linie vom Anfang bis zum Ende der Wand. Bei einer runden Wand leer. |
| `GetStartPoint() -> Math.Point2D \| None` | Gibt den Anfangspunkt zurück. |
| `GetEndPoint() -> Math.Point2D \| None` | Gibt den Endpunkt zurück. |
| `GetLength() -> float \| None` | Gibt die Länge zurück (Welteinheiten, geradlinige Länge). |
| `GetAngle() -> float \| None` | Gibt den Winkel zurück (Bogenmaß, Richtung vom Anfang zum Ende). |
| `SetThickness(thickness: float) -> bool` | Dicke (Welteinheiten). Das Setzen der Dicke löst die Verknüpfung der Wand mit ihrem Wandstil. |
| `GetHeights() -> WallObject.Heights \| None` | Gibt die Höhen zurück. |
| `SetHeights(heights: WallObject.Heights) -> bool` | Setzt die Höhen. |
| `SetHeights(startTop: float, startBottom: float, endTop: float, endBottom: float) -> bool` | Setzt die Höhen. |
| `GetHeightBound(isTop: bool) -> WallObject.HeightBound` | Gibt den Höhenbezug für `isTop` zurück. |
| `SetHeightBounds(bottomBound: WallObject.HeightBound, topBound: WallObject.HeightBound) -> bool` | Verknüpft die Unter- und Oberkante der Wand mit ihren Höhenbezügen und passt die Höhen daran an (Oberkanten- / Unterkantenbezug der Wand in der Infopalette). Bei Ebenenbezügen werden fRelativeStory und fLevelType ignoriert und als 0 bzw. leer gespeichert. Schlägt fehl, wenn ein Bezug für die Wand nicht existiert (z. B. wenn ihre Ebene keinem Geschoss angehört oder das Geschoss keine entsprechende Referenzhöhe besitzt) oder wenn die Oberkante nicht über der Unterkante liegen würde. Ein gespeicherter Bezug, der fehlt (ältere Dateien) oder nicht mehr existiert, wird zunächst durch einen Bezug auf die Ebenenbasishöhe auf der aktuellen Wandhöhe ersetzt, von der aus die Verschiebung gemessen wird. Wie die anderen Schreibmethoden registriert diese Methode keinen Rückgängig-Schritt: Rufen Sie zuerst `Document.AddBothSwapObject` auf. |
| `SetHeightBound(isTop: bool, bound: WallObject.HeightBound) -> bool` | Verknüpft die Oberkante (isTop) oder die Unterkante der Wand wie SetHeightBounds; die andere Kante behält ihren Bezug. |
| `GetAverageHeight() -> float \| None` | Gibt die mittlere Höhe zurück. |
| `GetCaps() -> WallObject.Caps \| None` | Gibt die Abschlüsse zurück. |
| `SetCaps(caps: WallObject.Caps) -> bool` | Setzt die Abschlüsse. |
| `GetStyle() -> int \| None` | Wandstil (Zubehör vom Typ `ObjectType.WallStyle`). 0 = ohne Stil (frei festgelegte Dicke / Schalen). |
| `SetStyle(wallStyle: int, selectedOffset: float = 0.0, replacingOffset: float = 0.0) -> bool` | Setzt den Stil. Wandstil (`ObjectType.WallStyle`-Zubehör). 0 = ohne Stil (Dicke / Schalen frei einstellbar). |
| `IsCurtainWall() -> bool \| None` | Kennzeichnung als Fassade (eine Wand, die als Rahmenwerk eines Fassadensystems dient). |
| `SetIsCurtainWall(isCurtainWall: bool) -> bool` | Schaltet *Fassade* ein oder aus. |

Geerbt: alle Elemente von [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### WallObject.Heights

> **Vollständiger Name:** `api.WallObject.Heights` · **Erbt von:** `api.Object`

Höhen (Welteinheiten) relativ zur Konstruktionsebene (0 = Ebenenoberkante, negativ = darunter). Eine Wand kann durch unterschiedliche Start-/Endhöhen verjüngt werden.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Heights()` | Standardwert (Felder mit ihren Standardwerten). |
| `Heights(startTop, startBottom, endTop, endBottom)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `startTop` | `float` | Höhe der Oberkante am Wandanfang. |
| `startBottom` | `float` | Höhe der Unterkante am Wandanfang. |
| `endTop` | `float` | Höhe der Oberkante am Wandende. |
| `endBottom` | `float` | Höhe der Unterkante am Wandende. |

#### WallObject.HeightBound

> **Vollständiger Name:** `api.WallObject.HeightBound` · **Erbt von:** `api.Object`

Bezug der Wandunter- oder -oberkante: woran sich ihre Höhe orientiert. GetHeightBound gibt ihn zurück; SetHeightBound(s) nehmen ihn entgegen und verwenden dabei fKind, fRelativeStory, fLevelType und fOffset (fStatus und fElevation sind nur lesbare Ergebnisse).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `HeightBound()` | Standardwert (Felder mit ihren Standardwerten). |
| `HeightBound(fStatus, fKind, fRelativeStory, fLevelType, fOffset, fElevation)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fStatus` | `WallObject.BoundStatus` | Ob der Bezug fehlt, nicht aufgelöst, ungültig oder gültig ist. |
| `fKind` | `WallObject.BoundKind` | Ebenenbasishöhe, Ebenenwandhöhe oder eine Geschossreferenzhöhe. |
| `fRelativeStory` | `int` | Story: -1 das Geschoss darunter, 0 das Geschoss der Wandebene, 1 das Geschoss darüber. |
| `fLevelType` | `str` | Story: der Referenzhöhentyp der Referenzhöhe in diesem Geschoss. |
| `fOffset` | `float` | Welteinheiten, die zur Bezugshöhe addiert werden. |
| `fElevation` | `float \| None` | Aufgelöste Bezugshöhe (Welt-Z-Koordinate einschließlich Versatz), wenn fStatus den Wert Valid hat. |

#### WallObject.Caps

> **Vollständiger Name:** `api.WallObject.Caps` · **Erbt von:** `api.Object`

Endabschlüsse.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Caps()` | Standardwert (Felder mit ihren Standardwerten). |
| `Caps(leftCap, rightCap, round)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `leftCap` | `bool` | Den Wandanfang abschließen. |
| `rightCap` | `bool` | Das Wandende abschließen. |
| `round` | `bool` | Der Abschluss ist abgerundet. |

#### WallObject.BoundStatus

> **Vollständiger Name:** `api.WallObject.BoundStatus` · **Art:** `IntEnum`

Status eines Wandhöhenbezugs (`WallObject.HeightBound.fStatus`).

| Element | Wert | Beschreibung |
|---|---|---|
| `Missing` | `0` |  |
| `Unresolved` | `1` |  |
| `Invalid` | `2` |  |
| `Valid` | `3` |  |

#### WallObject.BoundKind

> **Vollständiger Name:** `api.WallObject.BoundKind` · **Art:** `IntEnum`

Woran sich ein Wandhöhenbezug orientiert: an der Ebenenbasishöhe, der Ebenenwandhöhe oder einer Geschossreferenzhöhe.

| Element | Wert | Beschreibung |
|---|---|---|
| `Unknown` | `0` |  |
| `LayerElevation` | `1` |  |
| `LayerWallHeight` | `2` |  |
| `Story` | `3` |  |

### SlabObject

> **Vollständiger Name:** `api.SlabObject` · **Erbt von:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Boden/Decke – ein horizontales Element (Boden, Dachdecke, Geschossdecke, ...), das durch ein 2D-Begrenzungsprofil definiert und um seine Dicke vertikal extrudiert wird. Zwei Objektarten gelten als Boden/Decke:

- das von Vectorworks erzeugte Plug-in-Objekt Boden/Decke (`ObjectType.Parametric`, universeller Name "Slab");
- ein Bodenobjekt (`ObjectType.Slab` der Bodenart, mit dem Befehl zum Anlegen von Böden erzeugt). Dachflächen und ältere Stützen sind ebenfalls `ObjectType.Slab`-Objekte, aber keine Boden/Decke-Objekte.

Ein Boden/Decke-Objekt besitzt eine Höhe und einen Stil (ein Boden/Deckenstil), der seine Schalen steuert. Durch Boden/Decke-Modifikatoren lassen sich Löcher in der Begrenzung hinzufügen.

Das Plug-in-Objekt Boden/Decke besitzt eine Parameterdatenbank: Die von ArchitectObject geerbten allgemeinen Get/SetParam*-Zugriffsmethoden lesen und schreiben seine Parameter (`GetParamNames()` listet sie auf). Bei einem Bodenobjekt liefern sie leere Werte / False.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `SlabObject(h: Handle)` | Verweist auf das vorhandene Boden/Decke-Objekt `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(hProfile: Handle) -> SlabObject` *statisch* | Erzeugt ein Plug-in-Objekt Boden/Decke mit dem angegebenen 2D-Profil als Begrenzung: einem Polygon, einer Polylinie, einer Ellipse (Kreis) oder einem Kreisbogen. Das Profil-Handle wird vom Boden/Decke-Objekt übernommen. Gibt bei einer anderen Profilart oder bei einem Fehler ein ungültiges Objekt zurück. |
| `Duplicate() -> SlabObject` | Dupliziert das Boden/Decke-Objekt in der Zeichnung und gibt die Kopie zurück. |
| `GetHeight() -> float \| None` | Höhe der Bezugskante des Boden/Decke-Objekts in Welteinheiten: die Ober- oder Unterkante seiner Kernschale, wie im Boden/Deckenstil festgelegt; SetHeight verschiebt das Boden/Decke-Objekt vertikal. Nur für das Plug-in-Objekt Boden/Decke: Bei einem Bodenobjekt liefert die Lesemethode einen leeren Wert und die Schreibmethode `False`. |
| `SetHeight(height: float) -> bool` | Setzt die Höhe. Höhe der Bezugskante des Boden/Decke-Objekts in Welteinheiten: die Ober- oder Unterkante seiner Kernschale, wie im Boden/Deckenstil festgelegt; SetHeight verschiebt das Boden/Decke-Objekt vertikal. Nur für das Plug-in-Objekt Boden/Decke: Bei einem Bodenobjekt liefert die Lesemethode einen leeren Wert und die Schreibmethode `False`. |
| `GetStyle() -> int \| None` | Boden/Deckenstil (Zubehör); 0 = ohne Stil. SetStyle(0) entfernt die Stilzuweisung und behält die aktuellen Schalen bei; das Zuweisen eines Stils ersetzt die Schalenkonfiguration durch die Schalen des Stils. Die Schreibmethode gibt `False` zurück und ändert das Boden/Decke-Objekt nicht, wenn der Index keinen Boden/Deckenstil der Zeichnung bezeichnet; sie gibt außerdem `False` zurück, wenn das Objekt anschließend nicht den Stil besitzt. |
| `SetStyle(slabStyle: int) -> bool` | Setzt den Stil. Boden/Deckenstil (Zubehör); 0 = ohne Stil. SetStyle(0) entfernt die Stilzuweisung und behält die aktuellen Schalen bei; das Zuweisen eines Stils ersetzt die Schalenkonfiguration durch die Schalen des Stils. Die Schreibmethode gibt `False` zurück und ändert das Boden/Decke-Objekt nicht, wenn der Index keinen Boden/Deckenstil der Zeichnung bezeichnet; sie gibt außerdem `False` zurück, wenn das Objekt anschließend nicht den Stil besitzt. |
| `AddModifier(hProfile: Handle, isSubtract: bool, componentID: int = -1, clipToBoundary: bool = True) -> bool` | Fügt dem Boden/Decke-Objekt einen Modifikator (ein 2D-Profil) hinzu.<br>• Wenn `isSubtract` den Wert `True` hat, bildet das Profil ein durchgehendes Loch im Boden/Decke-Objekt.<br>• `componentID` bestimmt eine einzelne Schale (< 0 für das gesamte Boden/Decke-Objekt).<br>• `clipToBoundary` beschneidet das Profil an der Begrenzung des Boden/Decke-Objekts. |

Geerbt: alle Elemente von [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### RoofObject

> **Vollständiger Name:** `api.RoofObject` · **Erbt von:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Dach (`ObjectType.RoofContainer`) – ein polygonales Dach, das durch eine Liste von Kanten definiert wird. Jede Kante hat einen Einfügepunkt, eine Neigung, einen Vorsprung (Dachüberstand) und eine Traufhöhe. Dachelemente (Dachraum, Verkleidung, Traufblende) können entlang des Umfangs eingefügt werden.

Ein Dach ist KEIN Plug-in-Objekt; die von ArchitectObject geerbten allgemeinen Get/SetParam*-Zugriffsmethoden liefern leere Werte / False.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RoofObject(h: Handle)` | Verweist auf das vorhandene Dach `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(generateGableWalls: bool, bearingInset: float, roofThickness: float, miterType: RoofObject.MiterType, verticalMiter: float) -> RoofObject` *statisch* | Erzeugt ein neues Dach.<br>• `generateGableWalls` verlängert die zugehörigen Wände automatisch bis zur Dachunterseite.<br>• `bearingInset` Abstand von der Wand zum Dachauflagerpunkt in Welteinheiten.<br>• `roofThickness` Dicke der Dachdecke in Welteinheiten.<br>• `miterType` siehe `RoofObject.MiterType`.<br>• `verticalMiter` vertikaler Anteil einer doppelten Gehrung in Welteinheiten.<br>Das neue Dach hat keinen Dachraum, keine Verkleidung und keine Traufblende; SetAccessories fügt sie hinzu. |
| `Duplicate() -> RoofObject` | Dupliziert das Dach in der Zeichnung und gibt die Kopie zurück. |
| `GetAttributes() -> RoofObject.Attributes \| None` | Gibt die Attribute zurück. |
| `SetAttributes(attributes: RoofObject.Attributes) -> bool` | Setzt die Attribute. |
| `SetAccessories(accessories: RoofObject.Accessories) -> bool` | Setzt die Zusatzelemente. |
| `GetEdgeCount() -> int \| None` | Anzahl der Kanteneinträge (Anzahl der Kanten bzw. Eckpunkte des Dachumrisses). |
| `GetEdge(index: int) -> RoofObject.Edge \| None` | Gibt die Kante an Position `index` zurück (0-basierter Index). |
| `SetEdge(index: int, edge: RoofObject.Edge) -> bool` | Setzt die Kante an Position `index`. |
| `AppendEdge(edge: RoofObject.Edge) -> bool` | Fügt die Kante `edge` (Einfügepunkt, Neigung, Überstand, Traufhöhe) am Ende des Dachs hinzu. |
| `RemoveEdge(index: int) -> bool` | Entfernt die Kante an Position `index`. |

Geerbt: alle Elemente von [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### RoofObject.Attributes

> **Vollständiger Name:** `api.RoofObject.Attributes` · **Erbt von:** `api.Object`

Attribute des gesamten Dachs.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Attributes()` | Standardwert (Felder mit ihren Standardwerten). |
| `Attributes(generateGableWalls, bearingInset, roofThickness, miterType, verticalMiter)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `generateGableWalls` | `bool` | Ob Giebelwände erzeugt werden. |
| `bearingInset` | `float` | Auflagerversatz. |
| `roofThickness` | `float` | Dachdicke. |
| `miterType` | `RoofObject.MiterType` | Gehrungsart der Dachkanten. |
| `verticalMiter` | `float` | Wert für die vertikale Gehrung. |

#### RoofObject.Accessories

> **Vollständiger Name:** `api.RoofObject.Accessories` · **Erbt von:** `api.Object`

Dachelemente entlang des Umfangs.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Accessories()` | Standardwert (Felder mit ihren Standardwerten). |
| `Accessories(insertAttic, insertSoffit, insertFascia, fasciaWidth, fasciaHeight, atticHeight, recess, rakeThickness, trimDepth)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `insertAttic` | `bool` | Ob ein Dachraum eingefügt wird. |
| `insertSoffit` | `bool` | Ob eine Verkleidung eingefügt wird. |
| `insertFascia` | `bool` | Ob eine Traufblende eingefügt wird. |
| `fasciaWidth` | `float` | Welteinheiten. |
| `fasciaHeight` | `float` | Höhe der Traufblende. |
| `atticHeight` | `float` | Höhe des Dachraums. |
| `recess` | `float` | Rücksprung. |
| `rakeThickness` | `float` | Ortgangstärke. |
| `trimDepth` | `float` | Verkleidungstiefe. |

#### RoofObject.Edge

> **Vollständiger Name:** `api.RoofObject.Edge` · **Erbt von:** `api.Object`

Dachkanten (Polygoneckpunkt + Neigung und Überstand pro Kante) in der Reihenfolge des Dachumrisses. Die Traufhöhe bezieht sich auf die Basishöhe der Konstruktionsebene des Dachs; SetEdge und AppendEdge interpretieren sie ebenso.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Edge()` | Standardwert (Felder mit ihren Standardwerten). |
| `Edge(insertionPoint, slope, projection, eaveHeight)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `insertionPoint` | `Math.Point2D` | Einfügepunkt der Kante. |
| `slope` | `float` | Grad. |
| `projection` | `float` | Welteinheiten – Traufüberstand. |
| `eaveHeight` | `float` | Welteinheiten, relativ zur Ebenenbasishöhe. |

#### RoofObject.MiterType

> **Vollständiger Name:** `api.RoofObject.MiterType` · **Art:** `IntEnum`

Gehrungsarten für die Dachkanten (Verbindung zweier benachbarter geneigter Flächen).

| Element | Wert | Beschreibung |
|---|---|---|
| `Vertical` | `1` | Vertikaler Schnitt. |
| `Horizontal` | `2` | Horizontaler Schnitt. |
| `Double` | `3` | Doppelte Gehrung (der Schnitt hat sowohl einen vertikalen als auch einen horizontalen Teil). |

### WindowObject

> **Vollständiger Name:** `api.WindowObject` · **Erbt von:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Fenster (universeller Name "Window") aus dem Plug-in Architectural Objects.

Ein Fenster wird an einer bestimmten Position entlang einer Wand (`ObjectType.Wall`) und auf einer bestimmten Höhe eingesetzt. Es besitzt Parameter für Rahmen / Flügel / Sprossen / Verglasung / Fensterbank / Bekleidung / Sturz / Fensterläden.

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten) Gesamtgröße und Platzierung

- "Width" — reell — Fenstergröße wie in der Infopalette angezeigt, gemessen gemäß "SizeReference" (GetWidth / SetWidth)
- "Height" — reell — (GetHeight / SetHeight)
- "SizeReference" — Auswahlliste — Sash Opening / Unit Size / Rough Opening: was "Width" / "Height" messen
- "OverallWidth" — reell — Elementmaß, das das Fenster beim Neuberechnen aus "Width" / "Height" berechnet (GetOverallWidth); ein hier geschriebener Wert wird bei der Neuberechnung ersetzt
- "OverallHeight" — reell — (GetOverallHeight)
- "Elevation" — reell — Höhe der Fensteroberkante oder Fensterbank über der Ebenenbasishöhe, gemäß "ElevationSetAt" (GetElevation; GetSillHeight / GetHeadHeight)
- "ElevationSetAt" — Auswahlliste — Head of Window / Sill of Window
- "OffsetInWall" — reell — horizontaler Versatz gegenüber dem Einfügepunkt in der Wand
- "UseWallDepth" — bool — Rahmentiefe an die Wanddicke anpassen
- "TopShape" — Auswahlliste — Square / Round / Segment / Sloped from Left / Sloped from Right / Gable / Ellipse / Gothic / Half Round from Left / Half Round from Right / Half Segment from Left / Half Segment from Right / Half Ellipse from Left / Half Ellipse from Right / Half Gothic from Left / Half Gothic from Right
- "Rise", "Spring" — reell — Parameter für gebogene / giebelartige Abschlüsse
- "WindowShape" — Auswahlliste — Rectangle / Circle / Oval / Half Circle / Half Oval / Diamond / Hexagon - Top Flat / Hexagon - Side Flat / Octagon
- "RoundWallOffset" — reell — Versatz gegenüber einer runden Wand
- "SpanWall" — bool — Fenster erstreckt sich über die gesamte Wand
- "CornerWindow" — bool — Eckfensterkonfiguration verwenden
- "CornerWindowOp" — Auswahlliste — Opening / Cased Opening / Flush Glass / Flush Glass - No Sash / Mitered Sash / Corner Post
- "CornerPostSize", "CornerPostOffset" — reell

Konfiguration

- "Configuration" — Auswahlliste — Opening / Cased Opening / Awning / Casement / Fixed Glass / Folding / Hopper / Hung / Sliding / Tilt/Turn / Vertical Pivot / Custom
- "CasementOperation" — Auswahlliste — Single / Bi-Part (Drehflügelkonfiguration)
- "FixedGlassOperation" — Auswahlliste — Sash / No Sash (Festverglasung)
- "HungOperation" — Auswahlliste — Single / Double (Vertikalschiebeflügelkonfiguration)
- "SashOperation" — Auswahlliste — veraltet; durch "Configuration" und die typspezifischen Öffnungsarten ersetzt
- "CustSashOpPopup" — Auswahlliste — benutzerdefinierte Flügelöffnungsart
- "CustSashOp", "CustSashLock" — Zeichenfolge
- "CustSashWdth", "CustSashHght" — Zeichenfolge — benutzerdefinierte Aufteilung der Flügelbreiten / -höhen
- "CustomSash" — bool
- "CustSashSel" — Zeichenfolge
- "CustSashWidth", "CustSashHeight" — reell
- "Rows", "Cols" — int — Abmessungen des benutzerdefinierten Flügelrasters
- "UnequalSash" — bool
- "SashScaleFactor" — reell
- "HingeDirection" — bool — Anschlagseite umkehren
- "HingePref" — int
- "Show3DOpen" — bool
- "OpenAngle" — reell — Grad

Oberlicht

- "Transom" — bool
- "TransWidth", "TransDepth" — reell — Breite / Tiefe des Oberlichtkämpfers
- "TransomGlazingClass" — Auswahlliste — Klassenname
- "NumVTranMuntins", "NumHTranMuntins" — int
- "TranMuntinWidth", "TranMuntinOffset", "TranMuntinDepth" — reell
- "TranMuntinPattern" — Auswahlliste — Colonial / Prairie / Prairie w/sunburst / Colonial w/sunburst / Renaissance
- "TranNumOfRays" — int
- "TransomMuntins" — bool
- "MullionWidth", "MullionDepth" — reell

Fassadenkonfiguration

- "CurtainWallWindow" — bool
- "CWSashOperation" — Auswahlliste — Fixed Glass / Fixed Glass - No Sash / Casement / Bi-parting Casement / Horizontal Slider / Awning / Hopper / Tilt/Turn / Vertical Pivot

Blendrahmen / Flügelrahmen

- "JambWidth" — reell — Ansichtsbreite des Blendrahmens
- "JambDepth" — reell — Blendrahmentiefe (in die Wand hinein)
- "SashWidth", "SashDepth" — reell
- "ShimGap" — reell
- "MasonMod" — reell — Versatz zum Mauerwerksraster
- "UseJambExtension" — bool
- "JambExtenWidth" — reell

Sprossen

- "MuntinPattern" — Auswahlliste — Colonial / Prairie / Prairie w/sunburst / Colonial w/sunburst / Renaissance
- "MuntinApplication" — Auswahlliste — None / All / Top / Bottom / Transom / Top\Bottom / Top\Transom / Bot\Transom
- "NumVMuntins", "NumHMuntins" — int
- "MuntinWidth", "MuntinOffset", "MuntinDepth" — reell
- "NumOfRays" — int
- "TopSashMuntins", "BottomSashMuntins", "TransomMuntins" — bool
- "CustomTopMuntins" — bool
- "TopSashHorizBars" — int
- "CustMuntins" — Zeichenfolge
- "CustMullDepth", "CustMullWidth" — reell

Außenfensterbank / Innenfensterbank

- "SillStyle" — Auswahlliste — Timber / Masonry / Brick / Open Profile Beside Frame / Open Profile Below Frame / Closed Profile
- "IncludeSill" — bool
- "SillDepth", "SillHeight", "SillLip", "SillRise", "SillKeep", "SillExt" — reell
- "StoolLip", "StoolNose" — reell

Bekleidung

- "IntTrim", "ExtTrim" — bool
- "IntTrimWidth", "IntTrimDepth", "ExtTrimWidth", "ExtTrimDepth" — reell
- "TrimUnderStool", "TrimUnderSill" — bool

Laibungsschrägen (Winkel der inneren / äußeren Wandöffnung)

- "IntSplay", "ExtSplay" — bool
- "UseIntSplayAngle", "UseExtSplayAngle" — bool
- "IntSplayAngle", "ExtSplayAngle" — reell (Grad)
- "IntSplayDiag", "ExtSplayDiag" — reell
- "UseIntSplayWidth", "UseExtSplayWidth" — bool
- "IntSplayWidth", "ExtSplayWidth" — reell
- "IntSplayDepth", "ExtSplayDepth" — reell

Sturz

- "Lintels" — bool
- "LintelThick" — reell
- "IntLintelProt", "ExtLintelProt" — reell
- "UseLintelAngle" — bool
- "LintelAngle" — reell (Grad)
- "UseLintelDrop" — bool
- "LintelDrop" — reell
- "LintelClass" — Auswahlliste — Klassenname

Fensterläden

- "IntShutters", "ExtShutters" — bool
- "IntShtThick", "ExtShtThick" — reell
- "IntShtMllWidth", "ExtShtMllWidth" — reell
- "IntShtDivWSash", "ExtShtDivWSash" — bool
- "IntShtEqualDiv", "ExtShtEqualDiv" — bool
- "IntShtNumPanels", "ExtShtNumPanels" — int
- "IntShtIsPanel", "ExtShtIsPanel" — bool
- "IntShtIsCustom", "ExtShtIsCustom" — bool
- "IntShtCustomIndex", "ExtShtCustomIndex" — int
- "UseCustIntShutterWidth", "UseCustExtShutterWidth" — bool
- "CustIntShutterWidth", "CustExtShutterWidth" — reell

ID / Listen / Beschriftung

- "OnSchedule" — bool
- "IDPrefix", "IDLabel", "IDSuffix" — Zeichenfolge
- "IDLabelSize" — reell
- "IDLabelShape" — Auswahlliste — None / Rectangle / Round / Hexagon
- "IDLabelClass" — Auswahlliste — Klassenname
- "KeepIDHoriz" — bool
- "ShowIDLeader" — bool
- "IDLeaderLW" — int — Liniendicke
- "UseMarker" — bool
- "MarkerIDx" — int
- "MarkerStyle" — int
- "MarkerAngle" — int (Grad)
- "MarkerSize" — reell
- "MarkerWidth" — reell
- "MarkerThick", "MarkerThickB" — reell / int
- "TagInElevation" — bool
- "Tag3DHorzOffset", "Tag3DVertOffset" — reell

Anzahl der Schalen (Rahmen)

- "NumOfIntCavities", "NumOfExtCavities" — int

Klassen (pro Bestandteil)

- "IntSashClass", "ExtSashClass" — Auswahlliste — Klassenname
- "IntJTClass", "ExtJTClass" — Auswahlliste — Klassenname (Blendrahmen + Bekleidung)
- "IntShutterClass", "ExtShutterClass" — Auswahlliste — Klassenname
- "SillClass", "StoolClass" — Auswahlliste — Klassenname
- "GlazingClass", "TransomGlazingClass" — Auswahlliste — Klassenname
- "IntTransomClass", "ExtTransomClass" — Auswahlliste — Klassenname
- "HingeClass" — Auswahlliste — Klassenname
- "Sills2DClass", "CeilingMainClass", "NonPlotClass" — Auswahlliste — Klassenname

Metadaten (für Listen)

- "WindowDesc" — Zeichenfolge — Kurzbeschreibung
- "Model", "ManufSupplier", "StockNo", "GlassDesc" — Zeichenfolge
- "HeadDetail", "JambDetail", "SillDetail" — Zeichenfolge
- "Accessories" — Zeichenfolge
- "Egress" — Zeichenfolge / bool
- "WindowMaterial", "WindowFinish", "FrameType", "FrameMaterial", "FrameFinish", "WindowSill" — Zeichenfolge
- "Location" — Zeichenfolge
- "LintelType" — Zeichenfolge
- "UserFld1..UserFld10" — Zeichenfolge — benutzerdefinierte Felder für Listen

Darstellungsoptionen

- "PlanDetail" — bool — Details in der Grundrissdarstellung zeichnen
- "DrawWallLines" — bool
- "Clerestory" — bool
- "LW_LS_OverRide" — bool
- "IsDoor" — bool — internes Kennzeichen (als Tür verwendetes Fenster)
- "Flipped" — bool
- "WrapPointsSwapped" — bool
- "ShowShimGap" — bool
- "ShowInteriorHinge" — bool
- "Set2DAttribsBy" — Auswahlliste — Object / Line Style / Class
- "PenStyle", "FillStyle" — Auswahlliste — None / Solid / Line Type / By Object / By Class (Stift), zusätzlich Hatch / Tile / Gradient / By Material (Füllung)
- "LastRenderMode", "Last3DView" — int
- "NGA2" — reell (Fläche, nur lesbar)
- "ControlPoint01X..ControlPoint03Y" — reell (Weltkoordinaten)

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `WindowObject(h: Handle)` | Verweist auf das vorhandene Fenster `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D) -> WindowObject` *statisch* | Erzeugt ein Fenster an `position`. Es wird üblicherweise anschließend über WallObject in eine Wand eingesetzt. |
| `Duplicate() -> WindowObject` | Dupliziert das Fenster in der Zeichnung und gibt die Kopie zurück. |

*Größe (Welteinheiten)*

| Methode | Beschreibung |
|---|---|
| `GetWidth() -> float \| None` | "Width" / "Height" geben die Fenstergröße wie in der Infopalette angezeigt an, gemessen gemäß dem Größenbezug: lichte Flügelöffnung ("Sash Opening"), Element ("Unit Size") oder Rohbauöffnung ("Rough Opening"). Bei der Neuberechnung ermittelt das Fenster daraus sein Elementmaß (GetOverallWidth / GetOverallHeight): Rufen Sie nach den Schreibmethoden `Reset()` auf. Die Schreibmethoden geben `False` zurück und schreiben nichts, wenn das Objekt ungültig ist, der Wert keine positive endliche Zahl ist oder der Parameter durch den Objektstil des Fensters festgelegt wird (IsParamSetByStyle). Vectorworks misst ein Fenster mit der Konfiguration Öffnung als Rohbauöffnung und passt ein Fenster in einer Fassade an sein Füllungsfeld an, unabhängig von diesen Werten. |
| `SetWidth(value: float) -> bool` | Setzt die Breite. "Width" / "Height" geben die Fenstergröße wie in der Infopalette angezeigt an, gemessen gemäß dem Größenbezug: lichte Flügelöffnung ("Sash Opening"), Element ("Unit Size") oder Rohbauöffnung ("Rough Opening"). Bei der Neuberechnung ermittelt das Fenster daraus sein Elementmaß (GetOverallWidth / GetOverallHeight): Rufen Sie nach den Schreibmethoden `Reset()` auf. Die Schreibmethoden geben `False` zurück und schreiben nichts, wenn das Objekt ungültig ist, der Wert keine positive endliche Zahl ist oder der Parameter durch den Objektstil des Fensters festgelegt wird (IsParamSetByStyle). Vectorworks misst ein Fenster mit der Konfiguration Öffnung als Rohbauöffnung und passt ein Fenster in einer Fassade an sein Füllungsfeld an, unabhängig von diesen Werten. |
| `GetHeight() -> float \| None` | Gibt die Höhe zurück. |
| `SetHeight(value: float) -> bool` | Setzt die Höhe. |
| `GetSizeReference() -> str \| None` | Was GetWidth / GetHeight messen: "Sash Opening" (lichte Flügelöffnung), "Unit Size" (Elementmaß) oder "Rough Opening" (Rohbauöffnung), festgelegt durch den Parameter "SizeReference". SetSizeReference schreibt nur den Wert der Auswahlliste: "Width", "Height" und "Elevation" behalten ihre Werte, die das Fenster bei der nächsten Neuberechnung im neuen Bezug interpretiert. Dadurch ändert sich die Fenstergröße (die Infopalette rechnet die Größe hingegen um). Setzen Sie die Größe anschließend. Die Methode gibt `False` zurück und schreibt nichts, wenn ein anderer Wert übergeben wird oder der Stil den Parameter festlegt. |
| `SetSizeReference(value: str) -> bool` | Setzt den Größenbezug. Was GetWidth / GetHeight messen: "Sash Opening" (lichte Flügelöffnung), "Unit Size" (Elementmaß) oder "Rough Opening" (Rohbauöffnung), festgelegt durch den Parameter "SizeReference". SetSizeReference schreibt nur den Wert der Auswahlliste: "Width", "Height" und "Elevation" behalten ihre Werte, die das Fenster bei der nächsten Neuberechnung im neuen Bezug interpretiert. Dadurch ändert sich die Fenstergröße (die Infopalette rechnet die Größe hingegen um). Setzen Sie die Größe anschließend. Die Methode gibt `False` zurück und schreibt nichts, wenn ein anderer Wert übergeben wird oder der Stil den Parameter festlegt. |
| `GetOverallWidth() -> float \| None` | Das Elementmaß, wie es das Fenster bei der letzten Neuberechnung ermittelt hat (Parameter "OverallWidth" / "OverallHeight"). SetOverallWidth / SetOverallHeight schreiben die Breite / Höhe im aktuellen Größenbezug, die bei der nächsten Neuberechnung das Elementmaß `value` ergibt: `value` selbst für "Unit Size", `value` abzüglich der doppelten Blendrahmenbreite ("JambWidth") für "Sash Opening". Sie geben `False` zurück und schreiben nichts, wenn dies nicht exakt möglich ist: bei "Rough Opening" (das Fenster kann seine Montagefugen von der Wand oder voneinander übernehmen), bei der Höhe eines Fensters mit "Sash Opening" und Oberlicht (die Oberlichthöhe hängt von der oberen Form ab), bei einem Fenster mit der Konfiguration Öffnung, einem Eckfenster, einem Fenster in einer Fassade oder in einer Fenster- / Türkombination (Vectorworks bestimmt deren Größe selbst), bei einem Wert, der keine positive Größe ergibt, und wenn SetWidth / SetHeight den Wert `False` zurückgeben. |
| `SetOverallWidth(value: float) -> bool` | Setzt die Gesamtbreite. Das Elementmaß, wie es das Fenster bei der letzten Neuberechnung ermittelt hat (Parameter "OverallWidth" / "OverallHeight"). SetOverallWidth / SetOverallHeight schreiben die Breite / Höhe im aktuellen Größenbezug, die bei der nächsten Neuberechnung das Elementmaß `value` ergibt: `value` selbst für "Unit Size", `value` abzüglich der doppelten Blendrahmenbreite ("JambWidth") für "Sash Opening". Sie geben `False` zurück und schreiben nichts, wenn dies nicht exakt möglich ist: bei "Rough Opening" (das Fenster kann seine Montagefugen von der Wand oder voneinander übernehmen), bei der Höhe eines Fensters mit "Sash Opening" und Oberlicht (die Oberlichthöhe hängt von der oberen Form ab), bei einem Fenster mit der Konfiguration Öffnung, einem Eckfenster, einem Fenster in einer Fassade oder in einer Fenster- / Türkombination (Vectorworks bestimmt deren Größe selbst), bei einem Wert, der keine positive Größe ergibt, und wenn SetWidth / SetHeight den Wert `False` zurückgeben. |
| `GetOverallHeight() -> float \| None` | Gibt die Gesamthöhe zurück. |
| `SetOverallHeight(value: float) -> bool` | Setzt die Gesamthöhe. |

*Höhenlage (Welteinheiten)*

| Methode | Beschreibung |
|---|---|
| `GetElevation() -> float \| None` | Höhen über der Ebenenbasishöhe; bei einem Fenster in einer Wand über der um die Höhe seiner Wandöffnung angehobenen Ebenenbasishöhe (normalerweise 0), nicht über der Wandunterkante. "Elevation" ist der unveränderte Wert aus der Infopalette: die Höhe der Fensteroberkante oder Fensterbank gemäß "ElevationSetAt" ("Head of Window" oder "Sill of Window"); GetElevation / SetElevation lesen und schreiben ihn. GetSillHeight / GetHeadHeight lesen die Fensterbank- / Oberkantenhöhe unabhängig von "ElevationSetAt", entsprechend der Umrechnung von "Elevation" durch die Palette beim Wechsel zwischen beiden: Oberkante = Fensterbank + Height. SetSillHeight schreibt "Elevation" für den aktuellen Wert von "ElevationSetAt" (Fensterbank + Height bei "Head of Window") mit dem Wert von "Height" zum Zeitpunkt des Aufrufs: Setzen Sie zuerst die Höhe; "ElevationSetAt" bleibt erhalten. SetElevation und SetSillHeight geben `False` zurück und schreiben nichts, wenn der Wert nicht endlich ist oder der Objektstil "Elevation" festlegt; SetSillHeight auch dann, wenn "Height" oder "ElevationSetAt" nicht gelesen werden können. |
| `SetElevation(value: float) -> bool` | Setzt die Höhenlage. Höhen über der Ebenenbasishöhe; bei einem Fenster in einer Wand über der um die Höhe seiner Wandöffnung angehobenen Ebenenbasishöhe (normalerweise 0), nicht über der Wandunterkante. "Elevation" ist der unveränderte Wert aus der Infopalette: die Höhe der Fensteroberkante oder Fensterbank gemäß "ElevationSetAt" ("Head of Window" oder "Sill of Window"); GetElevation / SetElevation lesen und schreiben ihn. GetSillHeight / GetHeadHeight lesen die Fensterbank- / Oberkantenhöhe unabhängig von "ElevationSetAt", entsprechend der Umrechnung von "Elevation" durch die Palette beim Wechsel zwischen beiden: Oberkante = Fensterbank + Height. SetSillHeight schreibt "Elevation" für den aktuellen Wert von "ElevationSetAt" (Fensterbank + Height bei "Head of Window") mit dem Wert von "Height" zum Zeitpunkt des Aufrufs: Setzen Sie zuerst die Höhe; "ElevationSetAt" bleibt erhalten. SetElevation und SetSillHeight geben `False` zurück und schreiben nichts, wenn der Wert nicht endlich ist oder der Objektstil "Elevation" festlegt; SetSillHeight auch dann, wenn "Height" oder "ElevationSetAt" nicht gelesen werden können. |
| `GetElevationSetAt() -> str \| None` | Gibt den Bezugspunkt der Höhenangabe zurück. |
| `GetSillHeight() -> float \| None` | Gibt die Fensterbankhöhe zurück. |
| `SetSillHeight(value: float) -> bool` | Setzt die Fensterbankhöhe. |
| `GetHeadHeight() -> float \| None` | Gibt die Höhe der Fensteroberkante zurück. |

*Konfiguration*

| Methode | Beschreibung |
|---|---|
| `GetConfiguration() -> str \| None` | Gibt die Konfiguration zurück. |
| `GetCasementOperation() -> str \| None` | Gibt die Öffnungsart des Drehflügels zurück. |
| `GetFixedGlassOperation() -> str \| None` | Gibt die Ausführung der Festverglasung zurück. |
| `GetHungOperation() -> str \| None` | Gibt die Öffnungsart des Vertikalschiebeflügels zurück. |

*Veraltet*

| Methode | Beschreibung |
|---|---|
| `GetSashOperation() -> str \| None` | Als "SashOperation" gespeichert; durch `GetConfiguration()` und die Lesemethoden für die typspezifischen Öffnungsarten ersetzt. |
| `SetSashOperation(value: str) -> bool` | Setzt die Flügelöffnungsart. Als "SashOperation" gespeichert; durch `GetConfiguration()` und die Lesemethoden für die typspezifischen Öffnungsarten ersetzt. |
| `GetTopShape() -> str \| None` | Gibt die obere Form zurück. |
| `SetTopShape(value: str) -> bool` | Setzt die obere Form. |

*Rahmen / Flügel*

| Methode | Beschreibung |
|---|---|
| `GetJambWidth() -> float \| None` | Gibt die Blendrahmenbreite zurück. |
| `SetJambWidth(value: float) -> bool` | Setzt die Blendrahmenbreite. |
| `GetJambDepth() -> float \| None` | Gibt die Blendrahmentiefe zurück. |
| `SetJambDepth(value: float) -> bool` | Setzt die Blendrahmentiefe. |

*Fensterbank*

| Methode | Beschreibung |
|---|---|
| `GetIncludeSill() -> bool \| None` | Ob *Fensterbank hinzufügen* eingeschaltet ist. |
| `SetIncludeSill(value: bool) -> bool` | Schaltet *Fensterbank hinzufügen* ein oder aus. |
| `GetSillStyle() -> str \| None` | Gibt die Fensterbankausführung zurück. |
| `SetSillStyle(value: str) -> bool` | Setzt die Fensterbankausführung. |

*Listen*

| Methode | Beschreibung |
|---|---|
| `GetOnSchedule() -> bool \| None` | Ob *In Liste aufnehmen* eingeschaltet ist. |
| `SetOnSchedule(value: bool) -> bool` | Schaltet *In Liste aufnehmen* ein oder aus. |
| `GetIDLabel() -> str \| None` | Gibt die ID-Beschriftung zurück. |
| `SetIDLabel(value: str) -> bool` | Setzt die ID-Beschriftung. |
| `GetDescription() -> str \| None` | Gibt die Beschreibung zurück. |
| `SetDescription(value: str) -> bool` | Setzt die Beschreibung. |

*Öffnung*

| Methode | Beschreibung |
|---|---|
| `GetInteriorSide() -> str \| None` | Gibt die Innenseite zurück. |
| `GetFlipped() -> bool \| None` | Ob *Gespiegelt* eingeschaltet ist. |
| `GetHingeDirection() -> bool \| None` | Ob *Anschlagrichtung* eingeschaltet ist. |
| `GetShow3DOpen() -> bool \| None` | Ob *In 3D geöffnet zeigen* eingeschaltet ist. |
| `GetOpenAngle() -> float \| None` | Gibt den Öffnungswinkel zurück. |
| `GetAwningOpenDirection() -> str \| None` | Parameter für Flügelanschlag und Öffnungsrichtung (Auswahllisten). |
| `GetCasementHingeSide() -> str \| None` | Gibt die Anschlagseite des Drehflügels zurück. |
| `GetCasementOpenDirection() -> str \| None` | Gibt die Öffnungsrichtung des Drehflügels zurück. |
| `GetHopperOpenDirection() -> str \| None` | Gibt die Öffnungsrichtung des Kippflügels zurück. |
| `GetTiltTurnHingeSide() -> str \| None` | Gibt die Anschlagseite des Drehkippflügels zurück. |
| `GetTiltTurnOpenDirection() -> str \| None` | Gibt die Öffnungsrichtung des Drehkippflügels zurück. |
| `GetVerticalPivotOpensOutToward() -> str \| None` | Gibt zurück, zu welcher Seite sich der Wendeflügel nach außen öffnet. |

Geerbt: alle Elemente von [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### DoorObject

> **Vollständiger Name:** `api.DoorObject` · **Erbt von:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Tür (universeller Name "Door") aus dem Plug-in Architectural Objects.

Eine Tür wird in eine Wand (`ObjectType.Wall`) eingesetzt. Sie besitzt Parameter für Rahmen / Türblatt / Zarge / Sturz / Schwelle / Bekleidung / Seitenlicht / Sichtfenster / Sprossen.

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten) Gesamtgröße und Platzierung

- "Width" — reell — Türgröße wie in der Infopalette angezeigt, gemessen gemäß "SizeReference" (GetWidth / SetWidth)
- "Height" — reell — (GetHeight / SetHeight)
- "SizeReference" — Auswahlliste — Leaf Size / Unit Size / Rough Opening: was "Width" / "Height" messen
- "DoorWidth" — reell — Türblattmaß, das die Tür bei der Neuberechnung aus "Width" / "Height" berechnet (GetLeafWidth); ein hier geschriebener Wert wird bei der Neuberechnung ersetzt
- "DoorHeight" — reell — (GetLeafHeight)
- "OffsetInWall" — reell — horizontaler Versatz gegenüber dem Einfügepunkt in der Wand
- "UseWallDepth" — bool — Rahmentiefe an die Wanddicke anpassen
- "TopShape" — Auswahlliste — Square / Round / Segment / Sloped from Left / Sloped from Right / Gable / Ellipse / Gothic
- "Rise", "Spring" — reell — Parameter für gebogene / giebelartige Abschlüsse

Konfiguration

- "Configuration" — Auswahlliste — Opening / Cased Opening / Barn / Double Acting / Double Egress / Folding / Overhead / Pocket / Sliding / Swing
- "SwingOperation" — Auswahlliste — Single / Bi-part / Pivot Single / Pivot Double Bi-part (Drehflügeltürkonfiguration)
- "Operation" — Auswahlliste — veraltet; durch "SwingOperation" ersetzt
- "PlanDetail" — bool
- "DetailLevel" — Auswahlliste — Low / Medium / High
- "Show3DHinge" — bool
- "DrawWallLines" — bool
- "LW_LS_OverRide" — bool
- "3DOpen" — bool
- "OpenAngle" — reell — Grad

Oberlicht

- "Transom" — bool
- "TranMullDepth", "TranMullWidth" — reell — Abmessungen des Oberlichtkämpfers
- "TranSashWidth", "TranSashDepth" — reell

Zarge

- "JambWidth", "JambDepth" — reell
- "AstragalWidth", "AstragalDepth" — reell
- "ShimGap" — reell
- "MasonMod" — reell

Bekleidung

- "IntTrim", "ExtTrim" — bool
- "IntTrimWidth", "IntTrimDepth", "ExtTrimWidth", "ExtTrimDepth" — reell

Anzahl der Schalen (Rahmen)

- "NumIntComps", "NumExtComps" — int

Listen / ID

- "OnSched" — bool
- "IDPrefix", "IDLabel", "IDSuffix" — Zeichenfolge
- "IDLabelSize" — reell
- "IDLabelShape" — Auswahlliste — None / Rectangle / Round / Hexagon
- "KeepIDHoriz" — bool
- "ShowIDLeader" — bool
- "UseMarker" — bool

Türblatt

- "LeafType" — Auswahlliste — Solid / Glass / Panel / Custom
- "DoorThickness" — reell
- "TopStileWidth", "LRStileWidth", "MidStileWidth", "BottomStileWidth" — reell
- "NumPanelsV", "NumPanelsH" — int
- "SetTopPanel" — bool
- "TopPanelHeight" — reell

Sprossen (in der Türblattverglasung)

- "MuntinStyle" — Auswahlliste — Colonial / Prairie
- "DoorMuntinWidth" — reell
- "DoorVMuntins", "DoorHMuntins" — int
- "Muntins" — bool
- "GlassMuntin" — Auswahlliste — Colonial / Prairie / Colonial w/Sunburst / Prairie w/ Sunburst / Renaissance
- "NumVMuntins", "NumHMuntins" — int
- "MuntinWidth" — reell

Seitenlichter

- "SideLights" — bool
- "LeftLiteWidth", "RightLiteWidth" — reell
- "SashWidth", "SashDepth" — reell
- "SLMullWidth", "SLMullDepth" — reell

Sturz

- "Lintel" — bool
- "IntLintelProt", "ExtLintelProt" — reell
- "LintelThick" — reell
- "UseLintelAngle" — bool
- "LintelAngle" — reell (Grad)
- "UseLintelDrop" — bool
- "LintelDrop" — reell
- "LintelClass" — Auswahlliste — Klassenname

Schwelle

- "Threshold" — bool
- "IntTHDepth", "ExtTHDepth", "OverallTHDepth" — reell
- "OffJambCenter" — reell
- "ThreshThick", "ThreshNose" — reell
- "ThresholdClass" — Auswahlliste — Klassenname

Laibungsschrägen

- "IntSplay", "ExtSplay" — bool
- "UseIntSplayAngle", "UseExtSplayAngle" — bool
- "IntSplayAngle", "ExtSplayAngle" — reell (Grad)
- "IntSplayDiag", "ExtSplayDiag" — reell
- "UseIntSplayWidth", "UseExtSplayWidth" — bool
- "IntSplayWidth", "ExtSplayWidth" — reell
- "IntSplayDepth", "ExtSplayDepth" — reell

Symbolersetzung (ein Symbol als Türblatt verwenden)

- "UseSymDef" — bool
- "SymbolName" — Zeichenfolge — Name des Symbols

Liniendicken / -arten (pro Bestandteil)

- "Part", "LWPart" — Zeichenfolge — welcher Bestandteil in der Infopalette bearbeitet wird
- "JambLW", "JambLS", "TrimLW", "TrimLS", "LeafLW", "LeafLS" — int
- "SwingLW", "SwingLS", "SashLW", "SashLS", "GlassLW", "GlassLS", "AstragalLW", "AstragalLS" — int
- "DetailLW" — int

Klassen (pro Bestandteil)

- "PartClass" — Auswahlliste — Klassenname für den aktuell ausgewählten Bestandteil
- "IntPanelClass", "ExtPanelClass" — Auswahlliste — Klassenname
- "IntSRClass", "ExtSRClass" — Auswahlliste — Klassenname (innere / äußere Längs- und Querfriese)
- "IntJambClass", "ExtJambClass" — Auswahlliste — Klassenname
- "IntTrimClass", "ExtTrimClass" — Auswahlliste — Klassenname
- "IntSashClass", "ExtSashClass" — Auswahlliste — Klassenname
- "SwingTrajectory" — Auswahlliste — Klassenname des Öffnungsbogens
- "GlazingClass" — Auswahlliste — Klassenname
- "SideLGlazingClass" — Auswahlliste — Klassenname (Seitenlichtverglasung)

Größenbestimmung

- "ROWidth", "ROHeight" — reell — Größe der Rohbauöffnung
- "MOWidth", "MOHeight" — reell — Größe der Mauerwerksöffnung
- "NGA" — reell — Nettoglasfläche (nur lesbar)

Metadaten (für Listen)

- "Manuf", "Model", "SKU" — Zeichenfolge
- "Accessories" — Zeichenfolge
- "HeadDetail", "JambDetail", "ThreshDetail" — Zeichenfolge
- "FrameFR", "DoorFR" — Zeichenfolge — Feuerwiderstandsklassen
- "Notes" — Zeichenfolge
- "UserFld1..UserFld10" — Zeichenfolge — benutzerdefinierte Felder

Scheunenschiebetür-Variante (Configuration = "Barn")

- "BarnShowRail" — Auswahlliste — None / 2D / 3D / 2D and 3D
- "BarnRailType" — Auswahlliste — Box / Flat / Round
- "BarnShowRailMounts" — Auswahlliste — None / 3D
- "BarnBracketType" — Auswahlliste — None / U / Z
- "BarnShowLeafHangers" — Auswahlliste — None / 3D
- "BarnHangerMounting" — Auswahlliste — Leaf Front / Leaf Top

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DoorObject(h: Handle)` | Verweist auf die vorhandene Tür `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D) -> DoorObject` *statisch* | Erzeugt eine Tür an `position`. Sie wird üblicherweise anschließend über WallObject in eine Wand eingesetzt. |
| `Duplicate() -> DoorObject` | Dupliziert die Tür in der Zeichnung und gibt die Kopie zurück. |

*Größe (Welteinheiten)*

| Methode | Beschreibung |
|---|---|
| `GetWidth() -> float \| None` | "Width" / "Height" geben die Türgröße wie in der Infopalette angezeigt an, gemessen gemäß dem Größenbezug: Türblatt ("Leaf Size"), Element einschließlich Rahmen ("Unit Size") oder Rohbauöffnung ("Rough Opening"). Bei der Neuberechnung ermittelt die Tür daraus ihr Türblattmaß (GetLeafWidth / GetLeafHeight): Rufen Sie nach den Schreibmethoden `Reset()` auf. GetWidth / GetHeight lesen die von den Schreibmethoden geschriebenen Werte; in früheren Versionen dieser API lasen sie das Türblattmaß, das jetzt GetLeafWidth / GetLeafHeight lesen. Die Schreibmethoden geben `False` zurück und schreiben nichts, wenn das Objekt ungültig ist, der Wert keine positive endliche Zahl ist oder der Parameter durch den Objektstil der Tür festgelegt wird (IsParamSetByStyle). Vectorworks misst eine Tür mit der Konfiguration Öffnung als Rohbauöffnung und passt eine Tür in einer Fassade an ihr Füllungsfeld an, unabhängig von diesen Werten. |
| `SetWidth(value: float) -> bool` | Setzt die Breite. "Width" / "Height" geben die Türgröße wie in der Infopalette angezeigt an, gemessen gemäß dem Größenbezug: Türblatt ("Leaf Size"), Element einschließlich Rahmen ("Unit Size") oder Rohbauöffnung ("Rough Opening"). Bei der Neuberechnung ermittelt die Tür daraus ihr Türblattmaß (GetLeafWidth / GetLeafHeight): Rufen Sie nach den Schreibmethoden `Reset()` auf. GetWidth / GetHeight lesen die von den Schreibmethoden geschriebenen Werte; in früheren Versionen dieser API lasen sie das Türblattmaß, das jetzt GetLeafWidth / GetLeafHeight lesen. Die Schreibmethoden geben `False` zurück und schreiben nichts, wenn das Objekt ungültig ist, der Wert keine positive endliche Zahl ist oder der Parameter durch den Objektstil der Tür festgelegt wird (IsParamSetByStyle). Vectorworks misst eine Tür mit der Konfiguration Öffnung als Rohbauöffnung und passt eine Tür in einer Fassade an ihr Füllungsfeld an, unabhängig von diesen Werten. |
| `GetHeight() -> float \| None` | Gibt die Höhe zurück. |
| `SetHeight(value: float) -> bool` | Setzt die Höhe. |
| `GetLeafWidth() -> float \| None` | Das Türblattmaß, wie es die Tür bei der letzten Neuberechnung ermittelt hat (Parameter "DoorWidth" / "DoorHeight"). |
| `GetLeafHeight() -> float \| None` | Gibt die Türblatthöhe zurück. |
| `GetSizeReference() -> str \| None` | Was GetWidth / GetHeight messen: "Leaf Size" (Türblattmaß), "Unit Size" (Elementmaß) oder "Rough Opening" (Rohbauöffnung), festgelegt durch den Parameter "SizeReference". SetSizeReference schreibt nur den Wert der Auswahlliste: "Width" und "Height" behalten ihre Werte, die die Tür bei der nächsten Neuberechnung im neuen Bezug interpretiert. Dadurch ändert sich die Türgröße (die Infopalette rechnet die Größe hingegen um). Setzen Sie die Größe anschließend. Die Methode gibt `False` zurück und schreibt nichts, wenn ein anderer Wert übergeben wird oder der Stil den Parameter festlegt. |
| `SetSizeReference(value: str) -> bool` | Setzt den Größenbezug. Was GetWidth / GetHeight messen: "Leaf Size" (Türblattmaß), "Unit Size" (Elementmaß) oder "Rough Opening" (Rohbauöffnung), festgelegt durch den Parameter "SizeReference". SetSizeReference schreibt nur den Wert der Auswahlliste: "Width" und "Height" behalten ihre Werte, die die Tür bei der nächsten Neuberechnung im neuen Bezug interpretiert. Dadurch ändert sich die Türgröße (die Infopalette rechnet die Größe hingegen um). Setzen Sie die Größe anschließend. Die Methode gibt `False` zurück und schreibt nichts, wenn ein anderer Wert übergeben wird oder der Stil den Parameter festlegt. |
| `GetThickness() -> float \| None` | Türblattdicke (Welteinheiten, Parameter "DoorThickness"). |
| `SetThickness(value: float) -> bool` | Setzt die Dicke. Türblattdicke (Welteinheiten, Parameter "DoorThickness"). |
| `GetConfig() -> str \| None` | Veralteter Parameter "Config"; `GetConfiguration()` liest die Auswahlliste "Configuration". |
| `SetConfig(value: str) -> bool` | Setzt die Konfiguration. Veralteter Parameter "Config"; `GetConfiguration()` liest die Auswahlliste "Configuration". |
| `GetConfiguration() -> str \| None` | Gibt die Konfiguration zurück. |
| `GetTopShape() -> str \| None` | Gibt die obere Form zurück. |
| `SetTopShape(value: str) -> bool` | Setzt die obere Form. |
| `GetLeafType() -> str \| None` | Gibt den Türblatttyp zurück. |
| `SetLeafType(value: str) -> bool` | Setzt den Türblatttyp. |

*Listen*

| Methode | Beschreibung |
|---|---|
| `GetOnSchedule() -> bool \| None` | Ob *In Liste aufnehmen* eingeschaltet ist. |
| `SetOnSchedule(value: bool) -> bool` | Schaltet *In Liste aufnehmen* ein oder aus. |
| `GetIDLabel() -> str \| None` | Gibt die ID-Beschriftung zurück. |
| `SetIDLabel(value: str) -> bool` | Setzt die ID-Beschriftung. |
| `GetSwingDirection() -> str \| None` | Öffnung (Schwenkbewegung des Türblatts; SwingOperation, SwingDirection und SwingHingeSide gelten für die Konfiguration "Swing"). |
| `GetSwingHingeSide() -> str \| None` | Gibt die Anschlagseite der Drehflügeltür zurück. |
| `GetInteriorSide() -> str \| None` | Gibt die Innenseite zurück. |
| `GetIsFlipped() -> bool \| None` | Ob *Gespiegelt* eingeschaltet ist. |
| `GetOpenAngle() -> float \| None` | Gibt den Öffnungswinkel zurück. |
| `GetSwingOperation() -> str \| None` | Gibt die Öffnungsart der Drehflügeltür zurück. |

*Veraltet*

| Methode | Beschreibung |
|---|---|
| `GetOperation() -> str \| None` | Als "Operation" gespeichert; durch `GetSwingOperation()` ersetzt. |
| `Get3DOpen() -> bool \| None` | Ob *In 3D geöffnet* eingeschaltet ist. |

Geerbt: alle Elemente von [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### ColumnObject

> **Vollständiger Name:** `api.ColumnObject` · **Erbt von:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Stütze – die Vectorworks-Stütze, universeller Name "Column2". `Is()` akzeptiert auch das ältere Plug-in-Objekt "Column" aus älteren Dateien, dessen Parameter abweichen können. `Create()` erzeugt ein Column2-Objekt oder ein älteres Column-Objekt, wenn nur dieses Plug-in installiert ist.

Eine Stütze ist ein vertikales tragendes Element mit einem architektonischen Schaft (rechteckig oder oval), einem optionalen Fuß und Kapitell sowie in Vectorworks Architect einer optionalen tragenden Komponente (siehe "Use Component").

Column2 ist ein mit Vectorworks geliefertes skriptbasiertes Plug-in (Column2.vso; es verwendet dasselbe Skript wie Pilaster2). Die nachfolgenden Parameternamen sind universelle Namen, die das Plug-in definiert und der IFC-Export von Vectorworks liest; verwenden Sie die allgemeinen Zugriffsmethoden GetParam.../SetParam... von ArchitectObject zum Lesen / Schreiben dieser Parameter und `HasParam()` / `GetParamNames()` zum Prüfen eines Objekts.

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten) Komponenten (Vectorworks Architect)

- "Use Component" — Auswahlliste — Architectural Only / Structural Only / Architectural and Structural

Gesamtgröße (Welteinheiten)

- "OA Height" — reell — Höhe der architektonischen Komponente
- "Struct Height" — reell — Höhe der tragenden Komponente
- "NewHeight" — reell — Höheneingabe bei einer einzelnen Komponente

Architektonischer Schaft (Welteinheiten)

- "ShaftType" — Auswahlliste — Rectangular / Oval; es gibt keinen benutzerdefinierten Schafttyp
- "Shaft Width" — reell
- "Shaft Depth" — reell
- "Shaft Radius" — reell — Eckenradius eines rechteckigen Schafts. Runde Schäfte verwenden gleiche Werte für "Shaft Width" und "Shaft Depth" mit "ShaftType" = "Oval".
- "Taper" — Auswahlliste — `None` oder die Art der Verjüngung
- "Taper Width", "Taper Depth" — reell
- "Arch Offset X", "Arch Offset Y", "Arch Offset Z" — reell

Fuß

- "Use Base" — bool
- "BaseType" — Auswahlliste
- "Base Height", "Base Width", "Base Depth", "Base Radius" — reell
- "Base Divisions" — int

Kapitell

- "Use Capital" — bool
- "CapitalType" — Auswahlliste — z. B. Oval Mushroom / Rectangular Mushroom
- "Capital Height", "Capital Width", "Capital Depth", "Capital Radius" — reell

Tragende Komponente (das Stahlprofil wird hier konfiguriert, nicht über ShaftType)

- "Struct Type" — Auswahlliste — z. B. Stahl
- "Struct Shape", "Steel Shape" — Auswahlliste
- "Struct Width", "Struct Depth", "Struct Radius" — reell
- "Struct Rotation", "Struct Clearance" — reell
- "Use Base Plate", "Use Top Plate" — bool
- "BP Width", "BP Depth", "BP Thickness", "BP Radius" — reell — Fußplatte
- "TP Width", "TP Depth", "TP Thickness", "TP Radius" — reell — Kopfplatte
- "BP Shape", "TP Shape" — Auswahlliste

Klasse und Kennzeichnung

- "Arch Class" — Auswahlliste — Klassenname
- "Column ID" — Zeichenfolge

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ColumnObject(h: Handle)` | Verweist auf die vorhandene Stütze `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D) -> ColumnObject` *statisch* | Erzeugt eine Stütze an `position` auf der aktiven Ebene / im aktuellen Container: ein Column2-Objekt oder ein älteres Column-Objekt, wenn nur dieses Plug-in installiert ist. Gibt ein ungültiges Objekt zurück, wenn keines von beiden installiert ist. |
| `Duplicate() -> ColumnObject` | Dupliziert die Stütze in der Zeichnung und gibt die Kopie zurück. |
| `GetTotalHeight() -> float \| None` | Höhe der aktiven Einzelkomponente (Welteinheiten): OA Height oder Struct Height ("Use Component"). Zusammengesetzte Stützen (architektonisch und tragend) haben unabhängig verknüpfte Komponenten: Die Lesemethode liefert einen leeren Wert und die Schreibmethode schlägt fehl. Die Schreibmethode aktualisiert außerdem NewHeight und den vorhandenen Versatz des Oberkantenbezugs, wobei dessen Referenz erhalten bleibt. |
| `SetTotalHeight(value: float) -> bool` | Setzt die Gesamthöhe. Höhe der aktiven Einzelkomponente (Welteinheiten): OA Height oder Struct Height ("Use Component"). Zusammengesetzte Stützen (architektonisch und tragend) haben unabhängig verknüpfte Komponenten: Die Lesemethode liefert einen leeren Wert und die Schreibmethode schlägt fehl. Die Schreibmethode aktualisiert außerdem NewHeight und den vorhandenen Versatz des Oberkantenbezugs, wobei dessen Referenz erhalten bleibt. |
| `GetShaftWidth() -> float \| None` | Rechteckiger Schaft (Welteinheiten). |
| `SetShaftWidth(value: float) -> bool` | Setzt die Schaftbreite (rechteckiger Schaft, Welteinheiten). |
| `GetShaftDepth() -> float \| None` | Gibt die Schafttiefe zurück. |
| `SetShaftDepth(value: float) -> bool` | Setzt die Schafttiefe. |
| `GetShaftDiameter() -> float \| None` | Runder Schaft (Welteinheiten). Bei nicht kreisförmigen Schäften liefert die Lesemethode einen leeren Wert; die Schreibmethode wählt Oval und setzt sowohl die Breite als auch die Tiefe auf den Durchmesser. |
| `SetShaftDiameter(value: float) -> bool` | Setzt den Schaftdurchmesser. Runder Schaft (Welteinheiten). Bei nicht kreisförmigen Schäften liefert die Lesemethode einen leeren Wert; die Schreibmethode wählt Oval und setzt sowohl die Breite als auch die Tiefe auf den Durchmesser. |
| `GetShape() -> str \| None` | Native Schaftform ("Rectangular" / "Oval"); die Schreibmethode akzeptiert auch "Round" als Alias für Oval. "Custom" gibt `False` zurück, ohne etwas zu ändern: Der native architektonische Schaft hat keinen benutzerdefinierten Modus. |
| `SetShape(value: str) -> bool` | Setzt die Form. Native Schaftform ("Rectangular" / "Oval"); die Schreibmethode akzeptiert auch "Round" als Alias für Oval. "Custom" gibt `False` zurück, ohne etwas zu ändern: Der native architektonische Schaft hat keinen benutzerdefinierten Modus. |

Geerbt: alle Elemente von [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### StairObject

> **Vollständiger Name:** `api.StairObject` · **Erbt von:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Treppe – die Vectorworks-Treppe, universeller Name "Stairs CW".

Stairs CW speichert seine Konfiguration (Form, Läufe, Podeste, Breiten, Geländer) in eigenen Einstellungen und spiegelt die Hauptwerte in den nachfolgenden Parametern wider. Bei jeder Neuberechnung liest es TotalRise, Orientation, UpperLayer und die Parameter für die Grundrissdarstellung zurück sowie WalkLineLength, TreadLength, RiserHeight und NumberOfRisers, sofern diese positiv sind; anschließend berechnet es die Treppe neu und schreibt die berechneten Werte. Setzen Sie daher die Werte, rufen Sie `Reset()` auf und lesen Sie die neu berechneten Werte zurück. StairWidth wird nicht zurückgelesen.

Ältere Treppenobjekte werden nicht unterstützt: Vectorworks wandelt beim Öffnen einer Datei das Objekt "Stair" aus Versionen vor 2010 in "Simple Stair" oder "Custom Stair" um und installiert kein Plug-in "Stair2". Verwenden Sie dafür ParametricObject.

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten) Hauptwerte (Welteinheiten)

- "TotalRise" — reell — Treppenhöhe (obere minus untere Höhe)
- "WalkLineLength" — reell — Länge der Lauflinie (gesamte Lauflänge)
- "StairWidth" — reell — erste Treppenbreite; berechnet, nicht zurückgelesen
- "TreadLength" — reell — Auftrittstiefe
- "RiserHeight" — reell
- "NumberOfRisers" — int
- "Orientation" — Auswahlliste — RightHand / LeftHand
- "UpperLayer" — Auswahlliste — Ebenenname des oberen Geschosses

Berechnete Größen (werden bei jeder Neuberechnung geschrieben)

- "StairArea" — reell — Fläche
- "NosingLength", "TreadLengthAtOffset" — reell
- "Flight1Length" ... "Flight4Length" — reell — Lauflinienlänge jedes Laufs
- "Flight1WalkingLineOffset" ... "Flight4WalkingLineOffset" — reell
- "Flight1NumberOfRiser" ... "Flight4NumberOfRiser" — int
- "Flight1NumberOfTreads" ... "Flight4NumberOfTreads" — int

Grundrissdarstellung: Jeder Name existiert für beide Detaillierungsgrade und endet auf Detailed oder Schematic

- "BreakModeLowerFloorDetailed" — Auswahlliste — NoBreak / SolidSolid / SolidNone / NoneSolid / SolidDashed / DashedSolid / NoneDashed / DashedNone
- "BreakElevationDetailed" — reell
- "BreakLineAngleDetailed" — reell — Grad
- "BreakLinesSeparationMMDetailed" — reell — Millimeter
- "ShowGuardrailOfInsideRailingDetailed" — bool
- "ShowGuardrailOfOutsideRailingDetailed" — bool

Intern

- "ControlPoint01X" ... "ControlPoint14Y" — reell — Positionen der Textbeschriftungen
- "InternalVersionNumberOfRecordFormat" — int

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `StairObject(h: Handle)` | Verweist auf die vorhandene Treppe `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D) -> StairObject` *statisch* | Erzeugt eine Treppe des Typs Stairs CW mit ihrer Standardkonfiguration an `position` auf der aktiven Ebene / im aktuellen Container. Gibt ein ungültiges Objekt zurück, wenn das Plug-in nicht installiert ist. |
| `Duplicate() -> StairObject` | Dupliziert die Treppe in der Zeichnung und gibt die Kopie zurück. |
| `GetTotalRun() -> float \| None` | Gesamtgeometrie (Welteinheiten): TotalRun ist "WalkLineLength", TotalRise ist "TotalRise", StairWidth ist "StairWidth", TreadDepth ist "TreadLength" und RiserHeight ist "RiserHeight". Die Schreibmethoden nehmen positive Werte entgegen, die die Treppe bei `Reset()` anwendet. StairWidth ist die erste Treppenbreite, die Stairs CW nicht zurückliest: SetStairWidth gibt `False` zurück. |
| `SetTotalRun(value: float) -> bool` | Setzt die gesamte Lauflänge. Gesamtgeometrie (Welteinheiten): TotalRun ist "WalkLineLength", TotalRise ist "TotalRise", StairWidth ist "StairWidth", TreadDepth ist "TreadLength" und RiserHeight ist "RiserHeight". Die Schreibmethoden nehmen positive Werte entgegen, die die Treppe bei `Reset()` anwendet. StairWidth ist die erste Treppenbreite, die Stairs CW nicht zurückliest: SetStairWidth gibt `False` zurück. |
| `GetTotalRise() -> float \| None` | Gibt die gesamte Treppenhöhe zurück. |
| `SetTotalRise(value: float) -> bool` | Setzt die gesamte Treppenhöhe. |
| `GetStairWidth() -> float \| None` | Gibt die Treppenbreite zurück. |
| `SetStairWidth(value: float) -> bool` | Setzt die Treppenbreite. |
| `GetTreadDepth() -> float \| None` | Gibt die Auftrittstiefe zurück. |
| `SetTreadDepth(value: float) -> bool` | Setzt die Auftrittstiefe. |
| `GetRiserHeight() -> float \| None` | Gibt die Steigungshöhe zurück. |
| `SetRiserHeight(value: float) -> bool` | Setzt die Steigungshöhe. |
| `GetNumTreads() -> int \| None` | Anzahlen. NumRisers ist "NumberOfRisers" (1 bis 32767). Stairs CW hat keine Gesamtanzahl der Auftritte: GetNumTreads ist leer und SetNumTreads gibt `False` zurück. |
| `SetNumTreads(value: int) -> bool` | Setzt die Anzahl der Auftritte. Anzahlen. NumRisers ist "NumberOfRisers" (1 bis 32767). Stairs CW hat keine Gesamtanzahl der Auftritte: GetNumTreads ist leer und SetNumTreads gibt `False` zurück. |
| `GetNumRisers() -> int \| None` | Gibt die Anzahl der Steigungen zurück. |
| `SetNumRisers(value: int) -> bool` | Setzt die Anzahl der Steigungen. |

*Konfiguration und Handläufe*

| Methode | Beschreibung |
|---|---|
| `GetConfiguration() -> str \| None` | Stairs CW speichert diese in seinen Einstellungen, nicht in Parametern. Die Lesemethoden liefern leere Werte und die Schreibmethoden geben `False` zurück. |
| `SetConfiguration(value: str) -> bool` | Setzt die Konfiguration. Stairs CW speichert diese in seinen Einstellungen, nicht in Parametern. Die Lesemethoden liefern leere Werte und die Schreibmethoden geben `False` zurück. |
| `GetHandrailLeft() -> bool \| None` | Handläufe (siehe oben). |
| `SetHandrailLeft(value: bool) -> bool` | Schaltet *Handlauf links* ein oder aus (Handläufe, siehe oben). |
| `GetHandrailRight() -> bool \| None` | Ob *Handlauf rechts* eingeschaltet ist. |
| `SetHandrailRight(value: bool) -> bool` | Schaltet *Handlauf rechts* ein oder aus. |

Geerbt: alle Elemente von [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

---

[Zurück zum Index](README.md) · [Nach oben](#objectsarchitect--wände-dächer-bödendecken-fenster-türen-stützen-treppen)
