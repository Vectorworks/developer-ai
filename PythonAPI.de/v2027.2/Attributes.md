[English](../../PythonAPI/v2027.2/Attributes.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/Attributes.md)

# Attributes — Grafische Attribute und Klassen

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Attributklassen beschreiben das Aussehen von Objekten. `ObjectAttributes` fasst alle grafischen Attribute eines Objekts zusammen (`Pen()`, `Fill()`, `FillMapping()`, `Markers()`, `DropShadow()`); `PenAttributes` umfasst die Linienattribute (Farben, Stil, Linienstärke, Deckkraft), `FillAttributes` die Füllattribute (Farben, Stil, Deckkraft), `FillMappingAttributes` die Ausrichtung von Schraffur-, Mosaik-, Farbverlaufs- und Bildfüllungen, `MarkerAttributes` die Linienendzeichen am Anfang und Ende und `DropShadowAttributes` den Schlagschatten. `ClassAttributes` stellt eine Klassendefinition dar: einen benannten, gespeicherten Satz von Attributen, den mehrere Objekte gemeinsam verwenden.

Die Werttypen `ColorRGB`, `ColorPair`, `ObjectColors`, `Marker`, `DropShadow`, `WallTextures`, `RoofTextures` und `Point2D`, die Attributaufzählungen und die Modulkonstante `api.kMaxOpacity` gehören ebenfalls zu dieser Gruppe.

**„Gemäß Klasse“:** Ein auf „gemäß Klasse“ gesetztes Attribut ignoriert den eigenen Wert des Objekts und verwendet den Wert der Klasse, der das Objekt angehört. Mit den Methoden `Get...ByClass` / `Set...ByClass` der Attributklassen lässt sich diese Einstellung abfragen und ändern.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [Point2D](#point2d)
  - [ColorRGB](#colorrgb)
  - [ColorPair](#colorpair)
  - [ObjectColors](#objectcolors)
  - [Marker](#marker)
  - [DropShadow](#dropshadow)
  - [WallTextures](#walltextures)
  - [RoofTextures](#rooftextures)
  - [AttributesBase](#attributesbase)
  - [PenAttributes](#penattributes)
  - [FillAttributes](#fillattributes)
  - [FillMappingAttributes](#fillmappingattributes)
    - [FillMappingAttributes.Frame](#fillmappingattributesframe)
  - [MarkerAttributes](#markerattributes)
  - [DropShadowAttributes](#dropshadowattributes)
  - [ClassAttributes](#classattributes)
  - [ObjectAttributes](#objectattributes)
- [Aufzählungen](#aufzählungen)
  - [PenStyleKind](#penstylekind)
  - [FillType](#filltype)
  - [MarkerShape](#markershape)
  - [MarkerFill](#markerfill)
  - [MarkerBase](#markerbase)
  - [MarkerHalfTick](#markerhalftick)
  - [MarkerThicknessBasis](#markerthicknessbasis)
  - [MarkerThicknessUnits](#markerthicknessunits)
  - [DropShadowUnits](#dropshadowunits)
  - [ClassVisibility](#classvisibility)
  - [ObjectType](#objecttype)
- [Modulkonstanten](#modulkonstanten)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`Point2D`](#point2d) | Klasse |  | Einfacher 2D-Punkt-Wertdatensatz (`x`, `y` in Welteinheiten), der von den Dialog- und Attribut-APIs verwendet wird. |
| [`ColorRGB`](#colorrgb) | Klasse |  | RGB-Farbe mit 16 Bit pro Kanal (0 .. |
| [`ColorPair`](#colorpair) | Klasse |  | Vordergrund- und Hintergrundfarbe eines Stifts oder einer Füllung als Farbindizes. |
| [`ObjectColors`](#objectcolors) | Klasse |  | Alle vier Objektfarben (Stift-Vordergrund/-Hintergrund, Füllungs-Vordergrund/-Hintergrund) als Farbindizes. |
| [`Marker`](#marker) | Klasse |  | Linienendzeichen (Pfeilspitze) am Anfang oder Ende einer Linie: Form, Füllung, Basis, Halbierung, Schaft, Winkel (Grad), Länge und Breite (Zoll auf der Seite) und Einstellungen für die Linienstärke... |
| [`DropShadow`](#dropshadow) | Klasse |  | Schlagschatteneinstellungen eines Objekts, einer Klasse oder des Dokuments: ein/aus, Einheiten, Versatz, Unschärferadius, Winkel, Farbe und Deckkraft. |
| [`WallTextures`](#walltextures) | Klasse |  | Wandtexturen einer Klasse (interne Indizes von Texturen, 0 = keine). |
| [`RoofTextures`](#rooftextures) | Klasse |  | Dachtexturen einer Klasse (interne Indizes von Texturen, 0 = keine). |
| [`AttributesBase`](#attributesbase) | Klasse |  | Gemeinsame Basisklasse der Klassen für grafische Attribute. |
| [`PenAttributes`](#penattributes) | Klasse | [`AttributesBase`](#attributesbase) | Stiftattribute (Kontur) eines Objekts: Farben, Stil (Muster / Linienart), Linienstärke, Deckkraft, Kennzeichnungen „nach Klasse“ und Linienartzuordnung (Koordinatenraum des Stifts). |
| [`FillAttributes`](#fillattributes) | Klasse | [`AttributesBase`](#attributesbase) | Füllattribute eines Objekts: Farben, Stil (Muster / Schraffur / Mosaik / Farbverlauf / Bild), Deckkraft und Einstellungen zur Übernahme von Klassenattributen. |
| [`FillMappingAttributes`](#fillmappingattributes) | Klasse | [`AttributesBase`](#attributesbase) | Ausrichtung von Schraffur-, Mosaik-, Farbverlaufs- und Bildfüllungen (Füllungsraum): Ursprung, Achsen, Versatz, Drehung, Wiederholung, Spiegelung und Umkehrung. |
| [`FillMappingAttributes.Frame`](#fillmappingattributesframe) | Klasse (verschachtelt) |  | Ausrichtungsrahmen einer Schraffur-, Mosaik-, Farbverlaufs- oder Bildfüllung: der Ursprung und die Endpunkte der I- und J-Achsen. |
| [`MarkerAttributes`](#markerattributes) | Klasse | [`AttributesBase`](#attributesbase) | Linienendzeichen (Pfeilspitzen) am Anfang und Ende eines Objekts. |
| [`DropShadowAttributes`](#dropshadowattributes) | Klasse | [`AttributesBase`](#attributesbase) | Schlagschatten eines Objekts. |
| [`ClassAttributes`](#classattributes) | Klasse | [`AttributesBase`](#attributesbase) | Eine Klassendefinition (`ObjectType.ClassDefinition`): eine benannte, gespeicherte Attributkonfiguration. |
| [`ObjectAttributes`](#objectattributes) | Klasse | [`AttributesBase`](#attributesbase) | Alle grafischen Attribute eines Objekts. |
| [`PenStyleKind`](#penstylekind) | IntEnum |  | Klassifizierung eines Stiftstil-Rohwerts. |
| [`FillType`](#filltype) | IntEnum |  | Art der Füllung eines Objekts. |
| [`MarkerShape`](#markershape) | IntEnum |  | Linienendzeichen (Pfeilspitzen) |
| [`MarkerFill`](#markerfill) | IntEnum |  | Die folgenden Aufzählungen für Linienendzeichenstile (MarkerFill, MarkerBase, MarkerHalfTick) verwenden bereits bitverschobene Werte, sodass sie durch bitweises ODER zu einem einzelnen 16-Bit-Stilwert kombiniert werden können... |
| [`MarkerBase`](#markerbase) | IntEnum |  | Form der Basis eines Linienendzeichens (bereits bitverschobene Werte, siehe `Marker.GetStyleValue`). |
| [`MarkerHalfTick`](#markerhalftick) | IntEnum |  | Ganzes Linienendzeichen oder nur dessen linke oder rechte Hälfte (bereits bitverschobene Werte, siehe `Marker.GetStyleValue`). |
| [`MarkerThicknessBasis`](#markerthicknessbasis) | IntEnum |  | Woran sich die Linienstärke eines Linienendzeichens orientiert. |
| [`MarkerThicknessUnits`](#markerthicknessunits) | IntEnum |  | Einheiten einer benutzerdefinierten Linienstärke für Linienendzeichen. |
| [`DropShadowUnits`](#dropshadowunits) | IntEnum |  | Schlagschatten |
| [`ClassVisibility`](#classvisibility) | IntEnum |  | Klassen |
| [`ObjectType`](#objecttype) | IntEnum |  | Typ eines Objekts. |
| [Modulkonstanten](#modulkonstanten) | Konstanten | | `kMaxOpacity` |

## Klassen

### Point2D

> **Vollständiger Name:** `api.Point2D` · **Erbt von:** `api.Object`

Einfacher 2D-Punkt-Wertdatensatz (`x`, `y` in Welteinheiten), der von den Dialog- und Attribut-APIs verwendet wird. Er wird implizit in `api.Math.Point2D` und daraus zurück konvertiert; dieser Typ bietet sämtliche Funktionen der Vektorrechnung.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Point2D()` | Standardwert (Felder mit ihren Standardwerten). |
| `Point2D(x, y)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: Point2D) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: Point2D) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `x` | `float` | X-Koordinate (Welteinheiten). |
| `y` | `float` | Y-Koordinate (Welteinheiten). |

### ColorRGB

> **Vollständiger Name:** `api.ColorRGB` · **Erbt von:** `api.Object`

RGB-Farbe mit 16 Bit pro Kanal (0 .. 65535), ohne Informationsverlust gegenüber der Vectorworks-Farbdarstellung.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ColorRGB()` | Standardwert (Felder mit ihren Standardwerten). |
| `ColorRGB(red, green, blue)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `FromRGB8(r: int, g: int, b: int) -> ColorRGB` *statisch* | Erzeugt eine Farbe aus 8-Bit-Kanälen (jeweils 0 .. 255). |
| `Red8() -> int` | Auf 8 Bit skalierter Rotkanal (0 .. 255). |
| `Green8() -> int` | Auf 8 Bit skalierter Grünkanal (0 .. 255). |
| `Blue8() -> int` | Auf 8 Bit skalierter Blaukanal (0 .. 255). |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: ColorRGB) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: ColorRGB) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `red` | `int` | Rotkanal (0 .. 65535). |
| `green` | `int` | Grünkanal (0 .. 65535). |
| `blue` | `int` | Blaukanal (0 .. 65535). |

### ColorPair

> **Vollständiger Name:** `api.ColorPair` · **Erbt von:** `api.Object`

Vordergrund- und Hintergrundfarbe eines Stifts oder einer Füllung als Farbindizes.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ColorPair()` | Standardwert (Felder mit ihren Standardwerten). |
| `ColorPair(fore, back)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: ColorPair) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: ColorPair) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fore` | `int` | Vordergrundfarbe (Farbindex). |
| `back` | `int` | Hintergrundfarbe (Farbindex). |

### ObjectColors

> **Vollständiger Name:** `api.ObjectColors` · **Erbt von:** `api.Object`

Alle vier Objektfarben (Stift-Vordergrund/-Hintergrund, Füllungs-Vordergrund/-Hintergrund) als Farbindizes.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ObjectColors()` | Standardwert (Felder mit ihren Standardwerten). |
| `ObjectColors(pen, fill)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: ObjectColors) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: ObjectColors) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `pen` | `ColorPair` | Vordergrund- / Hintergrundfarbe der Linie. |
| `fill` | `ColorPair` | Vordergrund- / Hintergrundfarbe der Füllung. |

### Marker

> **Vollständiger Name:** `api.Marker` · **Erbt von:** `api.Object`

Linienendzeichen (Pfeilspitze) am Anfang oder Ende einer Linie: Form, Füllung, Basis, Halbierung, Schaft, Winkel (Grad), Länge und Breite (Zoll auf der Seite) und Einstellungen für die Linienstärke.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Marker()` | Standardwert (Felder mit ihren Standardwerten). |
| `Marker(shape, fill, base, halfTick, tail, angle, length, width, thicknessBasis, thicknessUnits, thickness, visible)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetStyleValue() -> int` | Zusammengefasster Stilwert des Linienendzeichens (Form \| Füllung \| Basis \| Halbierung \| Schaft). |
| `SetStyleValue(value: int) -> None` | Setzt den Stilwert. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: Marker) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: Marker) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `shape` | `MarkerShape` | Form des Linienendzeichens. |
| `fill` | `MarkerFill` | Füllung des Linienendzeichens. |
| `base` | `MarkerBase` | Form der Basis des Linienendzeichens. |
| `halfTick` | `MarkerHalfTick` | Ganzes Linienendzeichen oder nur dessen linke oder rechte Hälfte. |
| `tail` | `bool` | Ob das Linienendzeichen einen Schaft hat. |
| `angle` | `int` | Grad. |
| `length` | `float` | Zoll auf der Seite. |
| `width` | `float` | Zoll auf der Seite. |
| `thicknessBasis` | `MarkerThicknessBasis` | Woran sich die Linienstärke des Linienendzeichens orientiert: an der Linie, am Bemaßungsstandard oder an `thickness`. |
| `thicknessUnits` | `MarkerThicknessUnits` | Einheiten von `thickness`. |
| `thickness` | `float` | Wird mit `MarkerThicknessBasis.Custom` verwendet, in thicknessUnits. |
| `visible` | `bool` | Ob das Linienendzeichen angezeigt wird. |

### DropShadow

> **Vollständiger Name:** `api.DropShadow` · **Erbt von:** `api.Object`

Schlagschatteneinstellungen eines Objekts, einer Klasse oder des Dokuments: ein/aus, Einheiten, Versatz, Unschärferadius, Winkel, Farbe und Deckkraft.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DropShadow()` | Standardwert (Felder mit ihren Standardwerten). |
| `DropShadow(useDropShadow, units, offset, blurRadius, angle, color, opacity)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: DropShadow) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: DropShadow) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `useDropShadow` | `bool` | Ob der Schlagschatten eingeschaltet ist. |
| `units` | `DropShadowUnits` | Ob `offset` und `blurRadius` Längen auf der Seite oder in Welteinheiten sind. |
| `offset` | `float` | Abstand des Schattens vom Objekt. |
| `blurRadius` | `float` | Unschärferadius des Schattens. |
| `angle` | `float` | Grad. |
| `color` | `int` | Schattenfarbe (Farbindex). |
| `opacity` | `int` | Deckkraft des Schattens (0 .. 100). |

### WallTextures

> **Vollständiger Name:** `api.WallTextures` · **Erbt von:** `api.Object`

Wandtexturen einer Klasse (interne Indizes von Texturen, 0 = keine).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `WallTextures()` | Standardwert (Felder mit ihren Standardwerten). |
| `WallTextures(right, left, center)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: WallTextures) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: WallTextures) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `right` | `int` | Textur der rechten Seite (Index der Textur, 0 = keine). |
| `left` | `int` | Textur der linken Seite (Index der Textur, 0 = keine). |
| `center` | `int` | Textur der Wandmitte (Index der Textur, 0 = keine). |

### RoofTextures

> **Vollständiger Name:** `api.RoofTextures` · **Erbt von:** `api.Object`

Dachtexturen einer Klasse (interne Indizes von Texturen, 0 = keine).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `RoofTextures()` | Standardwert (Felder mit ihren Standardwerten). |
| `RoofTextures(top, edge, dormer)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: RoofTextures) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: RoofTextures) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `top` | `int` | Textur der Dachoberseite (Index der Textur, 0 = keine). |
| `edge` | `int` | Textur der Dachkanten (Index der Textur, 0 = keine). |
| `dormer` | `int` | Textur der Dachgauben (Index der Textur, 0 = keine). |

### AttributesBase

> **Vollständiger Name:** `api.AttributesBase` · **Erbt von:** `api.Object`

Gemeinsame Basisklasse der Klassen für grafische Attribute. Eine Instanz besitzt das Objekt nicht; sie liest und schreibt lediglich dessen Attribute. Abfragemethoden geben `None` zurück, wenn das Handle null ist oder das Objekt das Attribut nicht unterstützt. Änderungsmethoden geben `False` zurück, wenn das Handle null ist oder das Objekt das Attribut nicht unterstützt.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `AttributesBase(h: Handle)` | Verweist auf die vorhandene Attributbasis `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetHandle() -> Handle` | Handle der Attributbasis. |
| `IsValid() -> bool` | True, wenn dieses Objekt auf eine vorhandene Attributbasis verweist. |
| `GetObjectType() -> ObjectType` | Gibt den Objekttyp zurück. |
| `IsGroup() -> bool` | True, wenn das Objekt eine Gruppe ist (seine Attribute gelten für die enthaltenen Objekte). |
| `GetObjectColors() -> ObjectColors \| None` | Alle vier Farben auf einmal (Stiftvordergrund/-hintergrund, Füllvordergrund/-hintergrund). |
| `SetObjectColors(colors: ObjectColors) -> bool` | Setzt die Objektfarben. Alle vier Farben gleichzeitig (Vorder- und Hintergrundfarbe der Linie sowie der Füllung). |
| `ColorIndexToRGB(index: int) -> ColorRGB` *statisch* | RGB-Farbe zum Farbindex `index` in der Farbtabelle des Dokuments. |
| `RGBToColorIndex(color: ColorRGB) -> int` *statisch* | Index des Eintrags in der Farbtabelle des Dokuments, der `color` am nächsten kommt. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True, wenn das Objekt gültig ist (entspricht `IsValid()`). |

### PenAttributes

> **Vollständiger Name:** `api.PenAttributes` · **Erbt von:** [`AttributesBase`](#attributesbase) → `api.Object`

Stiftattribute (Kontur) eines Objekts: Farben, Stil (Muster / Linienart), Linienstärke, Deckkraft, Kennzeichnungen „nach Klasse“ und Linienartzuordnung (Koordinatenraum des Stifts).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `PenAttributes(h: Handle)` | Verweist auf den vorhandenen Stift `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Farben*

| Methode | Beschreibung |
|---|---|
| `GetForeColor() -> ColorRGB \| None` | Gibt die Vordergrundfarbe zurück. |
| `SetForeColor(color: ColorRGB) -> bool` | Setzt die Vordergrundfarbe. |
| `GetBackColor() -> ColorRGB \| None` | Gibt die Hintergrundfarbe zurück. |
| `SetBackColor(color: ColorRGB) -> bool` | Setzt die Hintergrundfarbe. |
| `GetForeColorIndex() -> int \| None` | Gibt den Index der Vordergrundfarbe zurück. |
| `SetForeColorIndex(index: int) -> bool` | Setzt den Index der Vordergrundfarbe. |
| `GetBackColorIndex() -> int \| None` | Gibt den Index der Hintergrundfarbe zurück. |
| `SetBackColorIndex(index: int) -> bool` | Setzt den Index der Hintergrundfarbe. |
| `GetColors() -> ColorPair \| None` | Gibt die Farben zurück. |
| `SetColors(colors: ColorPair) -> bool` | Setzt die Farben. |
| `GetColorsByClass() -> bool \| None` | Ob *Farben gemäß Klasse* eingeschaltet ist. |
| `SetColorsByClass() -> bool` | Setzt die Einstellung „Farben gemäß Klasse“. |
| `GetStyle() -> int \| None` | Stil. Rohwert: 0 kein Stil, 1-2 durchgezogen, > 2 altes Muster, < 0 -(interner Index einer Linienart). |
| `SetStyle(style: int) -> bool` | Setzt den Stil. Stil. Rohwert: 0 kein Stil, 1-2 durchgezogen, > 2 altes Muster, < 0 -(interner Index einer Linienart). |
| `GetStyleKind() -> PenStyleKind \| None` | Gibt die Stilart zurück. |
| `GetNone() -> bool \| None` | Ob *None* eingeschaltet ist. |
| `SetNone() -> bool` | Setzt den Stil auf „Keine“ (wird rekursiv auf die Gruppenmitglieder angewendet). |
| `GetSolid() -> bool \| None` | Ob *Vollton* eingeschaltet ist. |
| `SetSolid() -> bool` | Setzt den Stil auf „Vollton“ (wird rekursiv auf die Gruppenmitglieder angewendet). |
| `GetLineType() -> int \| None` | Interner Linienartindex (positiv), leer, wenn der Stift keine Linienart verwendet. |
| `SetLineType(lineTypeIndex: int) -> bool` | Setzt die Linienart. Interner Linienartindex (positiv), leer, wenn der Stift keine Linienart verwendet. |
| `GetStyleByClass() -> bool \| None` | Ob *Stil gemäß Klasse* eingeschaltet ist. |
| `SetStyleByClass() -> bool` | Setzt die Einstellung „Stil gemäß Klasse“. |

*Linienstärke*

| Methode | Beschreibung |
|---|---|
| `GetLineWeightMils() -> int \| None` | Gibt die Linienstärke in Tausendstel Zoll zurück. |
| `SetLineWeightMils(mils: int) -> bool` | Setzt die Linienstärke in Tausendstel Zoll. |
| `GetLineWeightMillimeters() -> float \| None` | Gibt die Linienstärke in Millimetern zurück. |
| `SetLineWeightMillimeters(mm: float) -> bool` | Setzt die Linienstärke in Millimetern. |
| `GetLineWeightByClass() -> bool \| None` | Ob *Linienstärke gemäß Klasse* eingeschaltet ist. |
| `SetLineWeightByClass() -> bool` | Setzt die Einstellung „Linienstärke gemäß Klasse“. |

*Deckkraft*

| Methode | Beschreibung |
|---|---|
| `GetOpacity() -> int \| None` | Gibt die Deckkraft zurück. |
| `SetOpacity(opacity: int) -> bool` | Setzt die Deckkraft. |
| `GetOpacityByClass() -> bool \| None` | Ob *Deckkraft gemäß Klasse* eingeschaltet ist. |
| `SetOpacityByClass(byClass: bool) -> bool` | Schaltet *Deckkraft gemäß Klasse* ein oder aus. |
| `IsMappingExisting() -> bool` | Linienartzuordnung (Stiftraum). |
| `GetLocalMapping() -> bool \| None` | Ob *Lokale Ausrichtung* eingeschaltet ist. |
| `SetLocalMapping(local: bool) -> bool` | Schaltet *Lokale Ausrichtung* ein oder aus. |
| `GetFlipHorizontal() -> bool \| None` | Ob *Horizontal spiegeln* eingeschaltet ist. |
| `SetFlipHorizontal(flip: bool) -> bool` | Schaltet *Horizontal spiegeln* ein oder aus. |
| `GetFlipVertical() -> bool \| None` | Ob *Vertikal spiegeln* eingeschaltet ist. |
| `SetFlipVertical(flip: bool) -> bool` | Schaltet *Vertikal spiegeln* ein oder aus. |
| `GetScale() -> float \| None` | Gibt den Skalierungsfaktor zurück. |
| `SetScale(scale: float) -> bool` | Setzt den Maßstab. |

Geerbt: alle Elemente von [`AttributesBase`](#attributesbase).

### FillAttributes

> **Vollständiger Name:** `api.FillAttributes` · **Erbt von:** [`AttributesBase`](#attributesbase) → `api.Object`

Füllattribute eines Objekts: Farben, Stil (Muster / Schraffur / Mosaik / Verlauf / Bild), Deckkraft und Kennzeichnungen „nach Klasse“. Die Füllungszuordnung (Ursprung, Skalierung, Drehung ...) befindet sich in FillMappingAttributes.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `FillAttributes(h: Handle)` | Verweist auf die vorhandene Füllung `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Farben*

| Methode | Beschreibung |
|---|---|
| `GetForeColor() -> ColorRGB \| None` | Gibt die Vordergrundfarbe zurück. |
| `SetForeColor(color: ColorRGB) -> bool` | Setzt die Vordergrundfarbe. |
| `GetBackColor() -> ColorRGB \| None` | Gibt die Hintergrundfarbe zurück. |
| `SetBackColor(color: ColorRGB) -> bool` | Setzt die Hintergrundfarbe. |
| `GetForeColorIndex() -> int \| None` | Gibt den Index der Vordergrundfarbe zurück. |
| `SetForeColorIndex(index: int) -> bool` | Setzt den Index der Vordergrundfarbe. |
| `GetBackColorIndex() -> int \| None` | Gibt den Index der Hintergrundfarbe zurück. |
| `SetBackColorIndex(index: int) -> bool` | Setzt den Index der Hintergrundfarbe. |
| `GetColors() -> ColorPair \| None` | Gibt die Farben zurück. |
| `SetColors(colors: ColorPair) -> bool` | Setzt die Farben. |
| `GetColorsByClass() -> bool \| None` | Ob *Farben gemäß Klasse* eingeschaltet ist. |
| `SetColorsByClass() -> bool` | Setzt die Einstellung „Farben gemäß Klasse“. |
| `GetStyle() -> int \| None` | Stil. Rohwert: 0 keine Füllung, 1 Vollton, > 1 altes Muster, < 0 -(interner Index einer Schraffur, eines Mosaiks, eines Farbverlaufs oder eines Bilds). |
| `SetStyle(style: int) -> bool` | Setzt den Stil. Stil. Rohwert: 0 keine Füllung, 1 Vollton, > 1 altes Muster, < 0 -(interner Index einer Schraffur, eines Mosaiks, eines Farbverlaufs oder eines Bilds). |
| `GetType() -> FillType \| None` | Gibt den Typ zurück. |
| `GetNone() -> bool \| None` | Ob *None* eingeschaltet ist. |
| `SetNone() -> bool` | Setzt den Stil auf „Keine“ (wird rekursiv auf die Gruppenmitglieder angewendet). |
| `GetSolid() -> bool \| None` | Ob *Vollton* eingeschaltet ist. |
| `SetSolid() -> bool` | Setzt den Stil auf „Vollton“ (wird rekursiv auf die Gruppenmitglieder angewendet). |
| `GetResource() -> int \| None` | Interner Index (positiv) der Schraffur, des Mosaiks, des Farbverlaufs oder des Bilds; leer, wenn die Füllung kein Zubehör verwendet. |
| `SetResource(resourceIndex: int) -> bool` | Setzt das Zubehör. Interner Index (positiv) der Schraffur, des Mosaiks, des Farbverlaufs oder des Bilds; leer, wenn die Füllung kein Zubehör verwendet. |
| `GetStyleByClass() -> bool \| None` | Ob *Stil gemäß Klasse* eingeschaltet ist. |
| `SetStyleByClass() -> bool` | Setzt die Einstellung „Stil gemäß Klasse“. |

*Deckkraft*

| Methode | Beschreibung |
|---|---|
| `GetOpacity() -> int \| None` | Gibt die Deckkraft zurück. |
| `SetOpacity(opacity: int) -> bool` | Setzt die Deckkraft. |
| `GetOpacityByClass() -> bool \| None` | Ob *Deckkraft gemäß Klasse* eingeschaltet ist. |
| `SetOpacityByClass(byClass: bool) -> bool` | Schaltet *Deckkraft gemäß Klasse* ein oder aus. |

Geerbt: alle Elemente von [`AttributesBase`](#attributesbase).

### FillMappingAttributes

> **Vollständiger Name:** `api.FillMappingAttributes` · **Erbt von:** [`AttributesBase`](#attributesbase) → `api.Object`

Zuordnung von Schraffur-, Mosaik-, Verlaufs- und Bildfüllungen (Koordinatenraum der Füllung): Ursprung, Achsen, Versätze, Drehung, Wiederholung, Spiegelung und Umkehrung. Getter geben einen leeren Wert zurück, wenn das Objekt keine Füllungszuordnung hat; Setter erstellen die Zuordnung bei Bedarf.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `FillMappingAttributes(h: Handle)` | Verweist auf die vorhandene Füllungsausrichtung `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `IsMappingExisting() -> bool` | True, wenn das Objekt eigene Daten zur Füllungsausrichtung hat. |

*Ausrichtungsrahmen in Weltkoordinaten*

| Methode | Beschreibung |
|---|---|
| `GetOriginPoint() -> Point2D \| None` | Gibt den Ursprungspunkt zurück. |
| `SetOriginPoint(pt: Point2D) -> bool` | Setzt den Ursprungspunkt. |
| `GetIAxisEndPoint() -> Point2D \| None` | Gibt den Endpunkt der I-Achse zurück. |
| `SetIAxisEndPoint(pt: Point2D) -> bool` | Setzt den Endpunkt der I-Achse. |
| `GetJAxisEndPoint() -> Point2D \| None` | Gibt den Endpunkt der J-Achse zurück. |
| `SetJAxisEndPoint(pt: Point2D) -> bool` | Setzt den Endpunkt der J-Achse. |
| `GetFrame() -> FillMappingAttributes.Frame \| None` | Gibt den Rahmen zurück. |
| `SetFrame(frame: FillMappingAttributes.Frame) -> bool` | Setzt den Rahmen. |

*Versatz und Achsenlängen in internen Einheiten*

| Methode | Beschreibung |
|---|---|
| `GetXOffset() -> float \| None` | Gibt den X-Versatz zurück. |
| `SetXOffset(value: float) -> bool` | Setzt den X-Versatz. |
| `GetYOffset() -> float \| None` | Gibt den Y-Versatz zurück. |
| `SetYOffset(value: float) -> bool` | Setzt den Y-Versatz. |
| `GetIAxisLength() -> float \| None` | Gibt die Länge der I-Achse zurück. |
| `SetIAxisLength(value: float) -> bool` | Setzt die Länge der I-Achse. |
| `GetJAxisLength() -> float \| None` | Gibt die Länge der J-Achse zurück. |
| `SetJAxisLength(value: float) -> bool` | Setzt die Länge der J-Achse. |
| `GetXOffsetInCurrentUnits() -> float \| None` | Versatz und Achsenlängen in den aktuellen Dokumenteinheiten. |
| `SetXOffsetInCurrentUnits(value: float) -> bool` | Setzt den X-Versatz in den aktuellen Einheiten (Versatz und Achsenlängen in den aktuellen Dokumenteinheiten). |
| `GetYOffsetInCurrentUnits() -> float \| None` | Gibt den Y-Versatz in den aktuellen Einheiten zurück. |
| `SetYOffsetInCurrentUnits(value: float) -> bool` | Setzt den Y-Versatz in den aktuellen Einheiten. |
| `GetIAxisLengthInCurrentUnits() -> float \| None` | Gibt die Länge der I-Achse in den aktuellen Einheiten zurück. |
| `SetIAxisLengthInCurrentUnits(value: float) -> bool` | Setzt die Länge der I-Achse in den aktuellen Einheiten. |
| `GetJAxisLengthInCurrentUnits() -> float \| None` | Gibt die Länge der J-Achse in den aktuellen Einheiten zurück. |
| `SetJAxisLengthInCurrentUnits(value: float) -> bool` | Setzt die Länge der J-Achse in den aktuellen Einheiten. |
| `GetAngle() -> float \| None` | Drehung der Füllungsausrichtung um ihren Ursprung in Radiant. |
| `SetAngle(radians: float) -> bool` | Setzt den Winkel (Drehung der Füllungsausrichtung um ihren Ursprung in Radiant). |
| `GetRepeat() -> bool \| None` | Ob *Wiederholen* eingeschaltet ist. |
| `SetRepeat(repeat: bool) -> bool` | Schaltet *Wiederholen* ein oder aus. |
| `GetMirror() -> bool \| None` | Ob *Spiegeln* eingeschaltet ist. |
| `SetMirror(mirror: bool) -> bool` | Schaltet *Spiegeln* ein oder aus. |
| `GetFlip() -> bool \| None` | Ob *Umkehren* eingeschaltet ist. |
| `SetFlip(flip: bool) -> bool` | Schaltet *Umkehren* ein oder aus. |
| `GetMaintainAspectRatio() -> bool \| None` | Ob *Seitenverhältnis beibehalten* eingeschaltet ist. |
| `SetMaintainAspectRatio(maintain: bool) -> bool` | Schaltet *Seitenverhältnis beibehalten* ein oder aus. |

*Geometrietyp des Farbverlaufs (linear, radial, ...)*

| Methode | Beschreibung |
|---|---|
| `GetGeometryType() -> int \| None` | Gibt den Geometrietyp zurück. |
| `SetGeometryType(type: int) -> bool` | Setzt den Geometrietyp. |

*Lokale (objektbezogene) Ausrichtung gegenüber Ausrichtung in Weltkoordinaten*

| Methode | Beschreibung |
|---|---|
| `GetLocalMapping() -> bool \| None` | Ob *Lokale Ausrichtung* eingeschaltet ist. |
| `SetLocalMapping(local: bool) -> bool` | Schaltet *Lokale Ausrichtung* ein oder aus. |

Geerbt: alle Elemente von [`AttributesBase`](#attributesbase).

#### FillMappingAttributes.Frame

> **Vollständiger Name:** `api.FillMappingAttributes.Frame` · **Erbt von:** `api.Object`

Ausrichtungsrahmen einer Schraffur-, Mosaik-, Farbverlaufs- oder Bildfüllung: der Ursprung und die Endpunkte der I- und J-Achsen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Frame()` | Standardwert (Felder mit ihren Standardwerten). |
| `Frame(origin, iAxisEnd, jAxisEnd)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `origin` | `Point2D` | Ursprung der Füllungsausrichtung. |
| `iAxisEnd` | `Point2D` | Endpunkt der I-Achse (vom Ursprung aus). |
| `jAxisEnd` | `Point2D` | Endpunkt der J-Achse (vom Ursprung aus). |

### MarkerAttributes

> **Vollständiger Name:** `api.MarkerAttributes` · **Erbt von:** [`AttributesBase`](#attributesbase) → `api.Object`

Linienendzeichen (Pfeilspitzen) am Anfang und Ende eines Objekts.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `MarkerAttributes(h: Handle)` | Verweist auf das vorhandene Linienendzeichen `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetBeginningMarker() -> Marker \| None` | Gibt das Linienendzeichen am Anfang zurück. |
| `SetBeginningMarker(marker: Marker) -> bool` | Setzt das Linienendzeichen am Anfang. |
| `GetEndMarker() -> Marker \| None` | Gibt das Linienendzeichen am Ende zurück. |
| `SetEndMarker(marker: Marker) -> bool` | Setzt das Linienendzeichen am Ende. |
| `GetBeginningMarkerVisible() -> bool \| None` | Ob *Linienendzeichen am Anfang sichtbar* eingeschaltet ist. |
| `SetBeginningMarkerVisible(visible: bool) -> bool` | Schaltet *Linienendzeichen am Anfang sichtbar* ein oder aus. |
| `GetEndMarkerVisible() -> bool \| None` | Ob *Linienendzeichen am Ende sichtbar* eingeschaltet ist. |
| `SetEndMarkerVisible(visible: bool) -> bool` | Schaltet *Linienendzeichen am Ende sichtbar* ein oder aus. |
| `GetByClass() -> bool \| None` | Ob *Gemäß Klasse* eingeschaltet ist. |
| `SetByClass() -> bool` | Setzt die Einstellung „Gemäß Klasse“. |

Geerbt: alle Elemente von [`AttributesBase`](#attributesbase).

### DropShadowAttributes

> **Vollständiger Name:** `api.DropShadowAttributes` · **Erbt von:** [`AttributesBase`](#attributesbase) → `api.Object`

Schlagschatten eines Objekts.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DropShadowAttributes(h: Handle)` | Verweist auf den vorhandenen Schlagschatten `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetEnabled() -> bool \| None` | Ob *Aktiviert* eingeschaltet ist. |
| `SetEnabled(enable: bool) -> bool` | Schaltet *Aktiviert* ein oder aus. |
| `GetData() -> DropShadow \| None` | Objektspezifische Schlagschattendaten; leer, wenn das Objekt keine hat. |
| `SetData(data: DropShadow) -> bool` | Setzt die Daten. Objektspezifische Schlagschattendaten; leer, wenn das Objekt keine hat. |
| `DeleteData() -> bool` | Entfernt die objektspezifischen Schlagschattendaten (das Objekt hat dann keinen eigenen Schlagschatten). |
| `GetByClass() -> bool \| None` | Ob *Gemäß Klasse* eingeschaltet ist. |
| `SetByClass(byClass: bool) -> bool` | Schaltet *Gemäß Klasse* ein oder aus. |
| `GetColor() -> ColorRGB \| None` | Komfortmethoden auf Basis von GetData / SetData. |
| `SetColor(color: ColorRGB) -> bool` | Setzt die Farbe (Komfortmethoden auf Basis von GetData / SetData). |
| `GetOpacity() -> int \| None` | Gibt die Deckkraft zurück. |
| `SetOpacity(opacity: int) -> bool` | Setzt die Deckkraft. |

Geerbt: alle Elemente von [`AttributesBase`](#attributesbase).

### ClassAttributes

> **Vollständiger Name:** `api.ClassAttributes` · **Erbt von:** [`AttributesBase`](#attributesbase) → `api.Object`

Eine Klassendefinition (`ObjectType.ClassDefinition`): eine benannte, gespeicherte Attributkonfiguration. Objekte, die einer Klasse zugewiesen sind, verwenden deren Attribute für jedes auf „gemäß Klasse“ gesetzte Attribut (siehe die Methoden SetXxxByClass von PenAttributes, FillAttributes, MarkerAttributes, DropShadowAttributes und `ObjectAttributes.SetAllByClass`). Die Erzeugung aus einem Handle, das keine Klassendefinition bezeichnet, ergibt ein ungültiges Objekt (`IsValid()` == `False`). Zeichenketten sind UTF-8-kodiert.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ClassAttributes(hClassDefinition: Handle)` | Verweist auf die vorhandene Klasse `hClassDefinition`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Suchen und Erzeugen*

| Methode | Beschreibung |
|---|---|
| `FromIndex(classIndex: int) -> ClassAttributes` *statisch* | Die Klasse mit dem internen Index `classIndex`. |
| `FromName(name: str) -> ClassAttributes` *statisch* | Die Klasse mit dem Namen `name`; ein ungültiges Objekt, wenn keine vorhanden ist. |
| `OfObject(hObject: Handle) -> ClassAttributes` *statisch* | Die Klasse des Objekts `hObject`. |
| `Create(name: str) -> ClassAttributes` *statisch* | Erzeugt eine Klasse mit dem Namen `name`; gibt die vorhandene Klasse zurück, wenn der Name bereits vergeben ist. |
| `GetNoneClass() -> ClassAttributes` *statisch* | Gibt die Klasse „Keine“ zurück. |
| `GetDimensionClass() -> ClassAttributes` *statisch* | Gibt die Klasse „Bemaßung“ zurück. |
| `GetGuidesClass() -> ClassAttributes` *statisch* | Gibt die Klasse für Hilfslinien zurück (erzeugt sie, falls sie fehlt). |
| `GetDefaultClass() -> ClassAttributes` *statisch* | Gibt die Standardklasse zurück (Klasse des aktuellen Containers; während einer Neuberechnung die Klasse des Plug-in-Objekts). |
| `GetActiveClass() -> ClassAttributes` *statisch* | Gibt die aktive Klasse zurück (aktive Klasse des Dokuments außerhalb des aktuellen Containers). |
| `GetMaxIndex() -> int` *statisch* | Gibt den maximalen Index zurück. |
| `ForEach(includeGuestClasses: bool, callback: callable(ClassAttributes)) -> None` *statisch* | Ruft `callback` für jede Klasse des Dokuments auf (Gastklassen referenzierter Dateien nur, wenn `includeGuestClasses` den Wert `True` hat). |
| `GetAll(includeGuestClasses: bool) -> list[ClassAttributes]` *statisch* | Alle Klassen des Dokuments (einschließlich der Gastklassen referenzierter Dateien, wenn `includeGuestClasses` den Wert `True` hat). |

*Identität*

| Methode | Beschreibung |
|---|---|
| `GetIndex() -> int \| None` | Gibt den Index zurück. |
| `GetName() -> str \| None` | Gibt den Namen zurück. |
| `GetDescription() -> str \| None` | Gibt die Beschreibung zurück. |
| `SetDescription(description: str) -> bool` | Setzt die Beschreibung. |
| `MakeDefault() -> bool` | Macht diese Klasse zur aktiven Klasse (der Klasse neuer Objekte). |
| `Delete() -> bool` | Löscht die Klasse; ihre Objekte werden in die Klasse `None` verschoben. Das Objekt wird ungültig. |

*Optionen*

| Methode | Beschreibung |
|---|---|
| `GetVisibility() -> ClassVisibility \| None` | Gibt die Sichtbarkeit zurück. |
| `SetVisibility(visibility: ClassVisibility) -> bool` | Setzt die Sichtbarkeit (ohne die Objekte neu zu zeichnen oder ihre Sichtbarkeit neu zu berechnen). |
| `GetNonPlot() -> bool \| None` | Ob *Nicht drucken* eingeschaltet ist. |
| `SetNonPlot(nonPlot: bool) -> bool` | Schaltet *Nicht drucken* ein oder aus. |
| `GetUseAtCreation() -> bool \| None` | Ob neue Objekte in dieser Klasse automatisch die Klassenattribute erhalten. |
| `SetUseAtCreation(use: bool) -> bool` | Schaltet *Automatisch zuweisen* ein oder aus. Legt fest, ob neue Objekte in dieser Klasse automatisch die Klassenattribute erhalten. |
| `GetObjectColors() -> ObjectColors \| None` | Farben (überschreibt AttributesBase zum Lesen/Schreiben der Klassenfarben). |
| `SetObjectColors(colors: ObjectColors) -> bool` | Setzt die Objektfarben (Farben (überschreibt AttributesBase zum Lesen/Schreiben der Klassenfarben)). |

*Stift*

| Methode | Beschreibung |
|---|---|
| `GetPenColors() -> ColorPair \| None` | Gibt die Stiftfarben zurück. |
| `SetPenColors(colors: ColorPair) -> bool` | Setzt die Stiftfarben. |
| `GetPenForeColor() -> ColorRGB \| None` | Gibt die Vordergrundfarbe des Stifts zurück. |
| `SetPenForeColor(color: ColorRGB) -> bool` | Setzt die Vordergrundfarbe des Stifts. |
| `GetPenBackColor() -> ColorRGB \| None` | Gibt die Hintergrundfarbe des Stifts zurück. |
| `SetPenBackColor(color: ColorRGB) -> bool` | Setzt die Hintergrundfarbe des Stifts. |
| `GetPenStyle() -> int \| None` | Unverarbeiteter Stiftstil; dieselben Werte wie bei `PenAttributes.GetStyle`. |
| `SetPenStyle(style: int) -> bool` | Setzt den Stiftstil. Stiftstil-Rohwert, gleiche Werte wie bei `PenAttributes.GetStyle`. |
| `GetPenStyleKind() -> PenStyleKind \| None` | Gibt die Art des Stiftstils zurück. |
| `GetPenLineType() -> int \| None` | Gibt die Linienart des Stifts zurück. |
| `SetPenLineType(lineTypeIndex: int) -> bool` | Setzt die Linienart des Stifts. |
| `GetLineWeightMils() -> int \| None` | Gibt die Linienstärke in Tausendstel Zoll zurück. |
| `SetLineWeightMils(mils: int) -> bool` | Setzt die Linienstärke in Tausendstel Zoll. |
| `GetPenOpacity() -> int \| None` | Gibt die Deckkraft des Stifts zurück. |
| `SetPenOpacity(opacity: int) -> bool` | Setzt die Deckkraft des Stifts. |

*Füllung*

| Methode | Beschreibung |
|---|---|
| `GetFillColors() -> ColorPair \| None` | Gibt die Füllfarben zurück. |
| `SetFillColors(colors: ColorPair) -> bool` | Setzt die Füllfarben. |
| `GetFillForeColor() -> ColorRGB \| None` | Gibt die Vordergrundfarbe der Füllung zurück. |
| `SetFillForeColor(color: ColorRGB) -> bool` | Setzt die Vordergrundfarbe der Füllung. |
| `GetFillBackColor() -> ColorRGB \| None` | Gibt die Hintergrundfarbe der Füllung zurück. |
| `SetFillBackColor(color: ColorRGB) -> bool` | Setzt die Hintergrundfarbe der Füllung. |
| `GetFillStyle() -> int \| None` | Unverarbeiteter Füllstil; dieselben Werte wie bei `FillAttributes.GetStyle`. |
| `SetFillStyle(style: int) -> bool` | Setzt den Füllstil. Füllstil-Rohwert, gleiche Werte wie bei `FillAttributes.GetStyle`. |
| `GetFillType() -> FillType \| None` | Gibt die Füllungsart zurück. |
| `GetFillResource() -> int \| None` | Gibt das Füllzubehör zurück. |
| `SetFillResource(resourceIndex: int) -> bool` | Setzt das Füllzubehör. |
| `GetFillOpacity() -> int \| None` | Gibt die Deckkraft der Füllung zurück. |
| `SetFillOpacity(opacity: int) -> bool` | Setzt die Deckkraft der Füllung. |

*Deckkraft von Stift und Füllung gemeinsam*

| Methode | Beschreibung |
|---|---|
| `SetOpacity(opacity: int) -> bool` | Setzt die Deckkraft. |
| `GetBeginningMarker() -> Marker \| None` | Linienendzeichen. Die Klasse speichert nur den Stil des Linienendzeichens; `Marker.visible` wird nicht verwendet. |
| `SetBeginningMarker(marker: Marker) -> bool` | Setzt das Linienendzeichen am Anfang. Linienendzeichen. Die Klasse speichert nur den Stil des Linienendzeichens; `Marker.visible` wird nicht verwendet. |
| `GetEndMarker() -> Marker \| None` | Gibt das Linienendzeichen am Ende zurück. |
| `SetEndMarker(marker: Marker) -> bool` | Setzt das Linienendzeichen am Ende. |
| `GetDropShadow() -> DropShadow \| None` | Schlagschatten. `DropShadow.useDropShadow` schaltet den Schlagschatten der Klasse ein. |
| `SetDropShadow(data: DropShadow) -> bool` | Setzt den Schlagschatten. Schlagschatten. `DropShadow.useDropShadow` schaltet den Schlagschatten der Klasse ein. |
| `GetUseTextures() -> bool \| None` | Ob die Klasse ihre Texturen beim Anlegen von Objekten automatisch zuweist. |
| `SetUseTextures(use: bool) -> bool` | Schaltet *Texturen verwenden* ein oder aus. |
| `GetGeneralTexture() -> int \| None` | Gibt die allgemeine Textur zurück. |
| `SetGeneralTexture(texture: int) -> bool` | Setzt die allgemeine Textur. |
| `GetWallTextures() -> WallTextures \| None` | Gibt die Wandtexturen zurück. |
| `SetWallTextures(textures: WallTextures) -> bool` | Setzt die Wandtexturen. |
| `GetRoofTextures() -> RoofTextures \| None` | Gibt die Dachtexturen zurück. |
| `SetRoofTextures(textures: RoofTextures) -> bool` | Setzt die Dachtexturen. |

*Textstil*

| Methode | Beschreibung |
|---|---|
| `GetUseTextStyle() -> bool \| None` | Ob *Textstil verwenden* eingeschaltet ist. |
| `SetUseTextStyle(use: bool) -> bool` | Schaltet *Textstil verwenden* ein oder aus. |
| `GetTextStyle() -> int \| None` | Gibt den Textstil zurück. |
| `SetTextStyle(textStyle: int) -> bool` | Setzt den Textstil. |

*Objekte*

| Methode | Beschreibung |
|---|---|
| `AssignTo(hObject: Handle, useClassAttributes: bool = False, descendIntoGroups: bool = True) -> bool` | Weist das Objekt dieser Klasse zu. Wenn `useClassAttributes` den Wert `True` hat, wird jedes Attribut des Objekts auf „gemäß Klasse“ gesetzt. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: ClassAttributes) -> bool` | `a == b`: True, wenn beide Objekte auf dieselbe Klasse verweisen. |
| `!=` | `__ne__(o: ClassAttributes) -> bool` | `a != b`: True, wenn die Objekte auf unterschiedliche Zeichnungsobjekte verweisen. |

Geerbt: alle Elemente von [`AttributesBase`](#attributesbase).

### ObjectAttributes

> **Vollständiger Name:** `api.ObjectAttributes` · **Erbt von:** [`AttributesBase`](#attributesbase) → `api.Object`

Alle grafischen Attribute eines Objekts. Die Geometrie ist bewusst nicht Teil dieser API.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ObjectAttributes(h: Handle)` | Verweist auf das vorhandene Objekt `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Pen() -> PenAttributes` | Stiftattribute (Linie) des Objekts. |
| `Fill() -> FillAttributes` | Füllattribute des Objekts. |
| `FillMapping() -> FillMappingAttributes` | Füllungsausrichtung (Platzierung von Schraffur-, Mosaik-, Farbverlaufs- und Bildfüllungen) des Objekts. |
| `Markers() -> MarkerAttributes` | Linienendzeichen am Anfang und Ende des Objekts. |
| `DropShadow() -> DropShadowAttributes` | Schlagschatten des Objekts. |

*Klasse des Objekts*

| Methode | Beschreibung |
|---|---|
| `GetClass() -> ClassAttributes` | Gibt die Klasse zurück. |
| `SetClass(theClass: ClassAttributes, descendIntoGroups: bool = True) -> bool` | Setzt die Klasse. |
| `SetAllByClass() -> bool` | Setzt jedes Attribut, das dies unterstützt, auf „gemäß Klasse“: Stift- und Füllfarben sowie -stile, Linienstärke, Deckkraft, Linienendzeichen und Schlagschatten. Das Objekt zeigt anschließend die Attribute seiner Klasse. |
| `GetOpacity() -> int \| None` | Gemeinsame Deckkraft (gleich für Stift und Füllung). |
| `SetOpacity(opacity: int) -> bool` | Setzt die Deckkraft (gemeinsame Deckkraft, gleich für Stift und Füllung). |
| `GetOpacityByClass() -> bool \| None` | Ob *Deckkraft gemäß Klasse* eingeschaltet ist. |
| `SetOpacityByClass() -> bool` | Setzt die Einstellung „Deckkraft gemäß Klasse“. |
| `ApplyTo(target: Handle) -> bool` | Kopiert Farben, Stift- und Füllstil, Linienstärke, Deckkraft, Linienendzeichen und Schlagschatten auf das Zielobjekt und wendet anschließend die Einstellungen „gemäß Klasse“ an (das Setzen eines Werts kann die zugehörige Einstellung „gemäß Klasse“ zurücksetzen). |

Geerbt: alle Elemente von [`AttributesBase`](#attributesbase).

## Aufzählungen

### PenStyleKind

> **Vollständiger Name:** `api.PenStyleKind` · **Art:** `IntEnum`

Klassifizierung eines Stiftstil-Rohwerts.

- 0 — keine
- 1, 2 — durchgezogen
- > 2 — altes Pixelmuster
- < 0 — Linienart-Zubehör, Wert ist -(interner Index der Linienart)

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` |  |
| `Solid` | `1` |  |
| `Pattern` | `2` |  |
| `SimpleLineType` | `3` |  |
| `ComplexLineType` | `4` |  |
| `Unknown` | `5` |  |

### FillType

> **Vollständiger Name:** `api.FillType` · **Art:** `IntEnum`

Art der Füllung eines Objekts.

| Element | Wert | Beschreibung |
|---|---|---|
| `Unknown` | `-1` |  |
| `None_` | `1` |  |
| `Solid` | `2` |  |
| `Pattern` | `3` |  |
| `Hatch` | `4` |  |
| `Tile` | `5` |  |
| `Gradient` | `6` |  |
| `Image` | `7` |  |
| `Class` | `8` |  |

### MarkerShape

> **Vollständiger Name:** `api.MarkerShape` · **Art:** `IntEnum`

Linienendzeichen (Pfeilspitzen)

| Element | Wert | Beschreibung |
|---|---|---|
| `Arrow` | `0` |  |
| `ConcaveCurvedArrow` | `1` |  |
| `Circle` | `2` |  |
| `DimSlash` | `3` |  |
| `DimCross` | `4` |  |
| `Lasso` | `5` |  |
| `Hexagon` | `6` |  |
| `VShaped` | `7` |  |
| `Cone` | `8` |  |
| `TaperedVShaped` | `9` |  |
| `SShaped` | `10` |  |
| `Rectangle` | `11` |  |
| `DoubleLine` | `12` |  |

### MarkerFill

> **Vollständiger Name:** `api.MarkerFill` · **Art:** `IntEnum`

Die folgenden Aufzählungen für Linienendzeichenstile (MarkerFill, MarkerBase, MarkerHalfTick) verwenden bereits bitverschobene Werte, sodass sie durch bitweises ODER zu einem einzelnen 16-Bit-Stilwert kombiniert werden können (siehe `Marker.GetStyleValue`). Verwenden Sie die Aufzählungsnamen, nicht die Ganzzahlen.

| Element | Wert | Beschreibung |
|---|---|---|
| `LineColor` | `0` |  |
| `White` | `128` |  |
| `NoFill` | `256` |  |

### MarkerBase

> **Vollständiger Name:** `api.MarkerBase` · **Art:** `IntEnum`

Form der Basis eines Linienendzeichens (bereits bitverschobene Werte, siehe `Marker.GetStyleValue`).

| Element | Wert | Beschreibung |
|---|---|---|
| `Flat` | `0` |  |
| `Open` | `1024` |  |
| `Angle` | `2048` |  |
| `Arc` | `3072` |  |

### MarkerHalfTick

> **Vollständiger Name:** `api.MarkerHalfTick` · **Art:** `IntEnum`

Ganzes Linienendzeichen oder nur dessen linke oder rechte Hälfte (bereits bitverschobene Werte, siehe `Marker.GetStyleValue`).

| Element | Wert | Beschreibung |
|---|---|---|
| `Full` | `0` |  |
| `Left` | `16384` |  |
| `Right` | `24576` |  |

### MarkerThicknessBasis

> **Vollständiger Name:** `api.MarkerThicknessBasis` · **Art:** `IntEnum`

Woran sich die Linienstärke eines Linienendzeichens orientiert.

| Element | Wert | Beschreibung |
|---|---|---|
| `LineThickness` | `0` |  |
| `DimThickness` | `1` |  |
| `Custom` | `2` |  |

### MarkerThicknessUnits

> **Vollständiger Name:** `api.MarkerThicknessUnits` · **Art:** `IntEnum`

Einheiten einer benutzerdefinierten Linienstärke für Linienendzeichen.

| Element | Wert | Beschreibung |
|---|---|---|
| `Mils` | `0` |  |
| `Points` | `16` |  |
| `Millimeters` | `32` |  |

### DropShadowUnits

> **Vollständiger Name:** `api.DropShadowUnits` · **Art:** `IntEnum`

Schlagschatten

| Element | Wert | Beschreibung |
|---|---|---|
| `Page` | `0` |  |
| `World` | `1` |  |

### ClassVisibility

> **Vollständiger Name:** `api.ClassVisibility` · **Art:** `IntEnum`

Klassen

| Element | Wert | Beschreibung |
|---|---|---|
| `Invisible` | `-1` |  |
| `Visible` | `0` |  |
| `Grayed` | `2` |  |

### ObjectType

> **Vollständiger Name:** `api.ObjectType` · **Art:** `IntEnum`

Typ eines Objekts. Wird von `Document.GetObjectType` und `AttributesBase.GetObjectType` zurückgegeben. Die Liste entspricht den Vectorworks-Objekttypcodes und ist bewusst vollständig; bisher gibt es nur für einen kleinen Teil typisierte Klassen (siehe die Zuordnung unten). Alle anderen Werte sind opak – identifizieren Sie das Objekt anhand seines Typs und arbeiten Sie anschließend mit ihm als rohem Handle.

- Line → Line2DObject
- Box → RectangleObject
- RoundedRectangle → RoundRectObject
- Arc / QuarterArc → ArcObject (ein Vollkreisbogen ist über `ArcObject.Is` auch CircleObject)
- Polygon / FreehandPolygon → PolygonObject
- Polyline → PolylineObject
- Locus → Locus2DObject
- Layer → Layer
- ClassDefinition → ClassAttributes

| Element | Wert | Beschreibung |
|---|---|---|
| `Invalid` | `-1` |  |
| `Term` | `0` |  |
| `Line` | `2` |  |
| `Box` | `3` |  |
| `Oval` | `4` |  |
| `Polygon` | `5` |  |
| `Arc` | `6` |  |
| `DimUnitSettings` | `7` |  |
| `FreehandPolygon` | `8` |  |
| `Locus3D` | `9` |  |
| `Text` | `10` |  |
| `Group` | `11` |  |
| `QuarterArc` | `12` |  |
| `RoundedRectangle` | `13` |  |
| `Paint` | `14` |  |
| `Symbol` | `15` |  |
| `SymbolDefinition` | `16` |  |
| `Locus` | `17` |  |
| `Worksheet` | `18` |  |
| `BuildingMaterial` | `19` |  |
| `Polyline` | `21` |  |
| `Extrude` | `24` |  |
| `Polygon3D` | `25` |  |
| `SlabDrain` | `26` |  |
| `SlabDrainValley` | `27` |  |
| `SlabSlopeValley` | `28` |  |
| `LayerReference` | `29` |  |
| `DashPatterns` | `30` |  |
| `Layer` | `31` |  |
| `Header` | `32` |  |
| `RefList` | `33` |  |
| `Sweep` | `34` |  |
| `ClassList` | `35` |  |
| `ViewportStyle` | `36` |  |
| `DataVisualization` | `37` |  |
| `MultiExtrude` | `38` |  |
| `DimensionStandard` | `39` |  |
| `Mesh` | `40` |  |
| `SavedView` | `43` |  |
| `RenderSpec` | `44` |  |
| `Eps` | `45` |  |
| `Format` | `47` |  |
| `Record` | `48` |  |
| `ToolCommand` | `49` |  |
| `SymbolList` | `54` |  |
| `WorksheetImage` | `56` |  |
| `Data` | `57` |  |
| `RecordLink` | `58` |  |
| `WorksheetDatabase` | `60` |  |
| `LeaderList` | `62` |  |
| `Dimension` | `63` |  |
| `HatchContainer` | `65` |  |
| `HatchDefinition` | `66` |  |
| `Bsp` | `67` |  |
| `Wall` | `68` |  |
| `InnerLines` | `69` |  |
| `SlabDrainageSettings` | `70` |  |
| `Slab` | `71` |  |
| `PenSpace` | `73` |  |
| `FontTable` | `74` |  |
| `StyleRun` | `75` |  |
| `UserData` | `76` |  |
| `WorkingPlane` | `77` |  |
| `WPlaneList` | `78` |  |
| `PixelPatternList` | `79` |  |
| `ColorPalette` | `80` |  |
| `Light` | `81` |  |
| `RoofEdge` | `82` |  |
| `RoofContainer` | `83` |  |
| `CSGTree` | `84` |  |
| `BoundaryRep` | `85` |  |
| `Parametric` | `86` |  |
| `RoofAdorner` | `87` |  |
| `Subscribe` | `88` |  |
| `ObsoleteRoundWall` | `89` |  |
| `UndoPlaceholder` | `90` |  |
| `TextureSpace` | `91` |  |
| `Folder` | `92` |  |
| `TextureBitmap` | `93` |  |
| `ClassDefinition` | `94` |  |
| `Solid` | `95` |  |
| `LineTypeDefinition` | `96` |  |
| `Texture` | `97` |  |
| `ADSymbolDefinitionHandler` | `98` |  |
| `ADSymbolHandler` | `99` |  |
| `SlabEdge` | `100` |  |
| `DropShadow` | `101` |  |
| `RoofStyle` | `102` |  |
| `CurtainWallFrame` | `103` |  |
| `CurtainWallPanel` | `104` |  |
| `CurtainWallGrid` | `105` |  |
| `RenderStyle` | `106` |  |
| `SlabStyle` | `107` |  |
| `TileDefinition` | `108` |  |
| `TextStyle` | `109` |  |
| `Constraint` | `110` |  |
| `PieceWiseNurbsCurve` | `111` |  |
| `CorePrintInfo` | `112` |  |
| `NurbsSurface` | `113` |  |
| `CompositeSurface` | `114` |  |
| `RenderBackground` | `115` |  |
| `PolyBreak` | `116` |  |
| `BatchRenderJob` | `117` |  |
| `BatchRenderJobList` | `118` |  |
| `ImageDefinition` | `119` |  |
| `GradientDefinition` | `120` |  |
| `FillSpace` | `121` |  |
| `Viewport` | `122` |  |
| `ArtRWStyle` | `123` |  |
| `Association` | `124` |  |
| `AuxMarker` | `125` |  |
| `GeoReference` | `126` |  |
| `WallStyle` | `127` |  |

## Modulkonstanten

| Konstante | Typ | Wert | Beschreibung |
|---|---|---|---|
| `api.kMaxOpacity` | `int` | `100` | Maximale Deckkraft (Wertebereich der Deckkraft: 0 bis 100). |

---

[Zurück zum Index](README.md) · [Nach oben](#attributes--grafische-attribute-und-klassen)
