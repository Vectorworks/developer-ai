[English](../../PythonAPI/v2027.2/DocumentAccess.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/DocumentAccess.md)

# DocumentAccess — Dokument, Ebenen, Geschosse und Einstellungen

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

`api.Document` ist der Einstiegspunkt der API: eine zustandslose Zugriffsschnittstelle für die aktive Zeichnung. Erzeugen Sie sie bei Bedarf mit `api.Document()` und greifen Sie damit auf die aktivierten Objekte, Ebenen, Geschosse, Klassen, Objekte, die Ansicht, Einheiten, die Rückgängig-Funktion und die typisierten Einstellungssichten (`DisplaySettings`, `EditingSettings`, `SnapSettings`, `GridSettings`, `StackLayersSettings`, `UnitSettings`, `TextDefaults`, `DefaultAttributes`, `ProgramVariables`) zu.

Im Folgenden verwendete Vectorworks-Begriffe: Eine **Ebene** ist eine Konstruktionsebene (eine Weltkoordinatenebene mit einem bestimmten Maßstab) oder eine Layoutebene (eine druckbare Seite); ein **Geschoss** ist ein Stockwerk des Gebäudes auf einer bestimmten Höhe, das die Konstruktionsebenen seiner Referenzhöhen zusammenfasst; ein **Referenzhöhentyp** ist der Name einer Geschossreferenzhöhe (zum Beispiel „Boden/Decke“); eine **Klasse** ist ein benannter Stilcontainer, dessen Attribute Objekte mit der Einstellung „gemäß Klasse“ übernehmen; ein **Container** ist alles, was Objekte enthält (eine Ebene, eine Gruppe, eine Symboldefinition, ein Ansichtsbereich).

Gemeinsame Konventionen: Abfragemethoden geben `None` zurück, wenn sich ein Wert nicht ermitteln lässt; Änderungsmethoden und Aktionen geben bei einem Fehler `False` zurück. Längen und Koordinaten werden in Welteinheiten, Winkel in Radiant (gegen den Uhrzeigersinn) angegeben, Zeichenketten sind UTF-8-kodiert. Objekthandles sind `api.Handle`-Objekte (`vs.Handle`); übergeben Sie `None` für ein Null-Handle. Verwenden Sie `Document.As(type, h)`, um zu einem Handle ein typisiertes Objekt zu erhalten.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [TextStyleData](#textstyledata)
  - [ProgramVariables](#programvariables)
  - [DisplaySettings](#displaysettings)
  - [EditingSettings](#editingsettings)
  - [SnapSettings](#snapsettings)
  - [GridSettings](#gridsettings)
  - [StackLayersSettings](#stacklayerssettings)
  - [UnitSettings](#unitsettings)
  - [TextDefaults](#textdefaults)
  - [DefaultAttributes](#defaultattributes)
  - [LayerContents](#layercontents)
  - [Layer](#layer)
  - [StoryLevel](#storylevel)
  - [StoryLevelTemplate](#storyleveltemplate)
  - [Story](#story)
  - [Document](#document)
- [Aufzählungen](#aufzählungen)
  - [Traverse](#traverse)
  - [Descend](#descend)
  - [LayerType](#layertype)
  - [LayerVisibility](#layervisibility)
  - [VisibilityOptions](#visibilityoptions)
  - [StoryElevationChangeMode](#storyelevationchangemode)
  - [UndoMethod](#undomethod)
  - [AngularUnit](#angularunit)
  - [TextJustification](#textjustification)
  - [TextVerticalAlignment](#textverticalalignment)
  - [TextLineSpacing](#textlinespacing)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`TextStyleData`](#textstyledata) | Klasse |  | Textstileinstellungen eines Texts (fett, kursiv, unterstrichen, Kontur, Schatten), wie sie von `TextDefaults.GetStyle` / `SetStyle` verwendet werden. |
| [`ProgramVariables`](#programvariables) | Klasse |  | Typisierter Zugriff auf niedriger Ebene auf beliebige Vectorworks-Programmvariablen (anwendungsweite oder dokumentbezogene Einstellungen) anhand eines numerischen Selektors. |
| [`DisplaySettings`](#displaysettings) | Klasse |  | Anzeigeeinstellungen. |
| [`EditingSettings`](#editingsettings) | Klasse |  | Bearbeitungs- und Sitzungseinstellungen. |
| [`SnapSettings`](#snapsettings) | Klasse |  | Zeigerfang-Einstellungen (Intelligenter Zeiger). |
| [`GridSettings`](#gridsettings) | Klasse |  | Rastereinstellungen. |
| [`StackLayersSettings`](#stacklayerssettings) | Klasse |  | Einstellungen für die Modellansicht. |
| [`UnitSettings`](#unitsettings) | Klasse |  | Primäre oder sekundäre Bemaßungseinheiten des aktiven Dokuments. |
| [`TextDefaults`](#textdefaults) | Klasse |  | Text-Vorgabeeinstellungen für neue Textobjekte. |
| [`DefaultAttributes`](#defaultattributes) | Klasse |  | Standardattribute für neue Objekte (die Attributpalette, wenn kein Objekt aktiviert ist). |
| [`LayerContents`](#layercontents) | Klasse |  | Objektanzahl und Begrenzung der Objekte auf der obersten Stufe einer Ebene. |
| [`Layer`](#layer) | Klasse |  | Eine Ebene (Konstruktions- oder Layoutebene). |
| [`StoryLevel`](#storylevel) | Klasse |  | Eine Referenzhöhe eines Geschosses: eine benannte Höhe (ihr Referenzhöhentyp) relativ zur Geschossbasishöhe, optional mit der Konstruktionsebene dieser Referenzhöhe. |
| [`StoryLevelTemplate`](#storyleveltemplate) | Klasse |  | Eine Referenzhöhenvorgabe (Dialogfenster „Organisation“ > Reiter „Geschosse 3D“ > „Referenzhöhenvorgaben“): eine Vorlage für Geschossreferenzhöhen. |
| [`Story`](#story) | Klasse |  | Ein Geschoss: ein Stockwerk des Gebäudes auf einer bestimmten Höhe. |
| [`Document`](#document) | Klasse |  | Zustandslose Zugriffsschnittstelle für das aktive Vectorworks-Dokument. |
| [`Traverse`](#traverse) | IntEnum |  | Welche Objektmenge beim Durchlaufen des Dokuments besucht wird. |
| [`Descend`](#descend) | IntFlag |  | Wie tief beim Durchlaufen in Containerobjekte (Gruppen, Symbole, Ansichtsbereiche, ...) abgestiegen wird. |
| [`LayerType`](#layertype) | IntEnum |  | Art einer Ebene. |
| [`LayerVisibility`](#layervisibility) | IntEnum |  | Sichtbarkeit einer Ebene (wie in der Navigationspalette angezeigt). |
| [`VisibilityOptions`](#visibilityoptions) | IntEnum |  | Wie andere als die aktive Ebene oder Klasse dargestellt werden. |
| [`StoryElevationChangeMode`](#storyelevationchangemode) | IntEnum |  | Welche Geschosse `Story.SetElevation` verschiebt (die Optionen des Dialogfensters „Geschossbasishöhe ändern“). |
| [`UndoMethod`](#undomethod) | IntEnum |  | Rückgängig-Methode, die an `Document.StartUndoEvent` übergeben wird. |
| [`AngularUnit`](#angularunit) | IntEnum |  | Einheit, in der Winkel angezeigt werden (`UnitSettings.GetAngularUnit`). |
| [`TextJustification`](#textjustification) | IntEnum |  | Horizontale Ausrichtung neuer Texte (`TextDefaults`). |
| [`TextVerticalAlignment`](#textverticalalignment) | IntEnum |  | Vertikale Ausrichtung neuer Texte (`TextDefaults`). |
| [`TextLineSpacing`](#textlinespacing) | IntEnum |  | Zeilenabstand neuer Texte (`TextDefaults`); `Custom` verwendet den Durchschuss von `TextDefaults.GetLeading`. |

## Klassen

### TextStyleData

> **Vollständiger Name:** `api.TextStyleData` · **Erbt von:** `api.Object`

Textstileinstellungen eines Texts (fett, kursiv, unterstrichen, Kontur, Schatten), wie sie von `TextDefaults.GetStyle` / `SetStyle` verwendet werden. Mit `ToBits` / `FromBits` lassen sie sich in die Vectorworks-Stilbitmaske und daraus zurück konvertieren.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `TextStyleData()` | Standardwert (Felder mit ihren Standardwerten). |
| `TextStyleData(bold, italic, underline, outline, shadow)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `ToBits() -> int` | Fasst die fünf Textstileinstellungen in der Vectorworks-Stilbitmaske zusammen (fett 1, kursiv 2, unterstrichen 4, Kontur 8, Schatten 16). |
| `FromBits(bits: int) -> TextStyleData` *statisch* | Erzeugt ein TextStyleData aus einer Vectorworks-Stilbitmaske (fett 1, kursiv 2, unterstrichen 4, Kontur 8, Schatten 16). |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `==` | `__eq__(o: TextStyleData) -> bool` | `a == b`: True, wenn die beiden Werte gleich sind. |
| `!=` | `__ne__(o: TextStyleData) -> bool` | `a != b`: True, wenn sich die beiden Werte unterscheiden. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `bold` | `bool` | Fett. |
| `italic` | `bool` | Kursiv. |
| `underline` | `bool` | Unterstrichen. |
| `outline` | `bool` | Kontur. |
| `shadow` | `bool` | Schatten. |

### ProgramVariables

> **Vollständiger Name:** `api.ProgramVariables` · **Erbt von:** `api.Object`

Direkter, typisierter Zugriff auf beliebige Vectorworks-Programmvariablen (programmweite oder dokumentbezogene Einstellungen) über numerische Selektoren. Die meisten Einstellungen lassen sich bequemer über die typisierten Einstellungsklassen (`DisplaySettings`, `EditingSettings`, `SnapSettings`, `GridSettings`, `StackLayersSettings`, `UnitSettings` und `TextDefaults`) abfragen und ändern; verwenden Sie diese Klasse nur für Einstellungen ohne benannte Zugriffsmethode. Jeder Selektor hat einen Werttyp; verwenden Sie die dazu passende Zugriffsmethode:

| Zugriffsmethode | Werttyp des Selektors |
|---|---|
| `GetBool` / `SetBool` | Boolescher Wert (`bool`) |
| `GetUInt8` / `SetUInt8` | Vorzeichenlose 8-Bit-Ganzzahl (0 bis 255) |
| `GetInt8` / `SetInt8` | Vorzeichenbehaftete 8-Bit-Ganzzahl (-128 bis 127) |
| `GetInt16` / `SetInt16` | 16-Bit-Ganzzahl |
| `GetInt32` / `SetInt32` | 32-Bit-Ganzzahl |
| `GetDouble` / `SetDouble` | Reelle Zahl (`float`): Längen, Winkel und andere reelle Werte |
| `GetString` / `SetString` | Text (`str`) |

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ProgramVariables()` | Zustandsloses Objekt; jede Methode ist statisch und kann direkt an der Klasse aufgerufen werden. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetBool(selector: int) -> bool \| None` *statisch* | Wert der booleschen Programmvariablen `selector`. |
| `SetBool(selector: int, value: bool) -> bool` *statisch* | Setzt die boolesche Programmvariable `selector`. |
| `GetUInt8(selector: int) -> int \| None` *statisch* | Wert der vorzeichenlosen 8-Bit-Programmvariablen `selector`. |
| `SetUInt8(selector: int, value: int) -> bool` *statisch* | Setzt die vorzeichenlose 8-Bit-Programmvariable `selector`. |
| `GetInt8(selector: int) -> int \| None` *statisch* | Wert der vorzeichenbehafteten 8-Bit-Programmvariablen `selector`. |
| `SetInt8(selector: int, value: int) -> bool` *statisch* | Setzt die vorzeichenbehaftete 8-Bit-Programmvariable `selector`. |
| `GetInt16(selector: int) -> int \| None` *statisch* | Wert der 16-Bit-Programmvariablen `selector`. |
| `SetInt16(selector: int, value: int) -> bool` *statisch* | Setzt die 16-Bit-Programmvariable `selector`. |
| `GetInt32(selector: int) -> int \| None` *statisch* | Wert der 32-Bit-Programmvariablen `selector`. |
| `SetInt32(selector: int, value: int) -> bool` *statisch* | Setzt die 32-Bit-Programmvariable `selector`. |
| `GetDouble(selector: int) -> float \| None` *statisch* | Wert der Programmvariablen `selector` für reelle Zahlen. |
| `SetDouble(selector: int, value: float) -> bool` *statisch* | Setzt die Programmvariable `selector` für reelle Zahlen. |
| `GetString(selector: int) -> str \| None` *statisch* | Wert der Textprogrammvariablen `selector`. |
| `SetString(selector: int, value: str) -> bool` *statisch* | Setzt die Textprogrammvariable `selector`. |

### DisplaySettings

> **Vollständiger Name:** `api.DisplaySettings` · **Erbt von:** `api.Object`

Anzeigeeinstellungen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DisplaySettings()` | Zustandslose Sicht auf die Anzeigeeinstellungen des aktiven Dokuments. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetBlackAndWhiteOnly() -> bool \| None` | Ob *Nur Schwarzweiß* eingeschaltet ist. |
| `SetBlackAndWhiteOnly(value: bool) -> bool` | Schaltet *Nur Schwarzweiß* ein oder aus. |
| `GetUseLayerColors() -> bool \| None` | Ob *Ebenenfarben verwenden* eingeschaltet ist. |
| `SetUseLayerColors(value: bool) -> bool` | Schaltet *Ebenenfarben verwenden* ein oder aus. |
| `GetZoomLineThickness() -> bool \| None` | Ob *Linienstärken beim Zoomen anpassen* eingeschaltet ist. |
| `SetZoomLineThickness(value: bool) -> bool` | Schaltet *Linienstärken beim Zoomen anpassen* ein oder aus. |
| `GetBlackBackground() -> bool \| None` | Ob *Schwarzer Hintergrund* eingeschaltet ist. |
| `SetBlackBackground(value: bool) -> bool` | Schaltet *Schwarzer Hintergrund* ein oder aus. |
| `GetShowRulers() -> bool \| None` | Ob *Lineale anzeigen* eingeschaltet ist. |
| `SetShowRulers(value: bool) -> bool` | Schaltet *Lineale anzeigen* ein oder aus. |
| `GetShowScrollBars() -> bool \| None` | Ob *Bildlaufleisten anzeigen* eingeschaltet ist. |
| `SetShowScrollBars(value: bool) -> bool` | Schaltet *Bildlaufleisten anzeigen* ein oder aus. |
| `GetShowPageBoundary() -> bool \| None` | Ob *Seitenbegrenzung anzeigen* eingeschaltet ist. |
| `SetShowPageBoundary(value: bool) -> bool` | Schaltet *Seitenbegrenzung anzeigen* ein oder aus. |
| `GetShowPageBreaks() -> bool \| None` | Ob *Seitenumbrüche anzeigen* eingeschaltet ist. |
| `SetShowPageBreaks(value: bool) -> bool` | Schaltet *Seitenumbrüche anzeigen* ein oder aus. |
| `GetShowOthersInGroup() -> bool \| None` | Ob *Andere Objekte beim Bearbeiten von Gruppen anzeigen* eingeschaltet ist. |
| `SetShowOthersInGroup(value: bool) -> bool` | Schaltet *Andere Objekte beim Bearbeiten von Gruppen anzeigen* ein oder aus. |
| `GetShowOthersInGroupGrayed() -> bool \| None` | Ob *Andere Objekte beim Bearbeiten von Gruppen grau anzeigen* eingeschaltet ist. |
| `SetShowOthersInGroupGrayed(value: bool) -> bool` | Schaltet *Andere Objekte beim Bearbeiten von Gruppen grau anzeigen* ein oder aus. |
| `GetEightSelectionHandles() -> bool \| None` | Ob *Acht Modifikationspunkte* eingeschaltet ist. |
| `SetEightSelectionHandles(value: bool) -> bool` | Schaltet *Acht Modifikationspunkte* ein oder aus. |
| `GetFullScreenCursor() -> bool \| None` | Ob *Bildschirmfüllendes Fadenkreuz* eingeschaltet ist. |
| `SetFullScreenCursor(value: bool) -> bool` | Schaltet *Bildschirmfüllendes Fadenkreuz* ein oder aus. |
| `GetNoFillBehindText() -> bool \| None` | Ob *Keine Füllung hinter Text* eingeschaltet ist. |
| `SetNoFillBehindText(value: bool) -> bool` | Schaltet *Keine Füllung hinter Text* ein oder aus. |
| `GetAdjustFlippedText() -> bool \| None` | Ob *Gespiegelten Text anpassen* eingeschaltet ist. |
| `SetAdjustFlippedText(value: bool) -> bool` | Schaltet *Gespiegelten Text anpassen* ein oder aus. |
| `GetXRayMode() -> bool \| None` | Ob *Röntgenmodus* eingeschaltet ist. |
| `SetXRayMode(value: bool) -> bool` | Schaltet *Röntgenmodus* ein oder aus. |
| `GetDisplayHiddenObjectsGhosted() -> bool \| None` | Ob *Ausgeblendete Objekte schemenhaft anzeigen* eingeschaltet ist. |
| `SetDisplayHiddenObjectsGhosted(value: bool) -> bool` | Schaltet *Ausgeblendete Objekte schemenhaft anzeigen* ein oder aus. |
| `GetShowInternalOriginMarker() -> bool \| None` | Ob *Markierung des internen Nullpunkts anzeigen* eingeschaltet ist. |
| `SetShowInternalOriginMarker(value: bool) -> bool` | Schaltet *Markierung des internen Nullpunkts anzeigen* ein oder aus. |
| `GetAllowDropShadows() -> bool \| None` | Ob *Schlagschatten zulassen* eingeschaltet ist. |
| `SetAllowDropShadows(value: bool) -> bool` | Schaltet *Schlagschatten zulassen* ein oder aus. |
| `GetPerspectiveCropped() -> bool \| None` | Ob *Perspektive begrenzen* eingeschaltet ist. |
| `SetPerspectiveCropped(value: bool) -> bool` | Schaltet *Perspektive begrenzen* ein oder aus. |
| `Get2DConversionResolution() -> int \| None` | Rohwerte der entsprechenden Einblendmenüs für Einstellungen. |
| `Set2DConversionResolution(value: int) -> bool` | Setzt die 2D-Konvertierungsauflösung. Rohwerte der entsprechenden Einblendmenüs für Einstellungen. |
| `Get3DConversionResolution() -> int \| None` | Gibt die 3D-Konvertierungsauflösung zurück. |
| `Set3DConversionResolution(value: int) -> bool` | Setzt die 3D-Konvertierungsauflösung. |
| `GetDisplayLightObjects() -> int \| None` | Gibt die Einstellung zur Anzeige von Lichtquellen zurück. |
| `SetDisplayLightObjects(value: int) -> bool` | Setzt die Einstellung zur Anzeige von Lichtquellen. |
| `GetRotatedTextDisplay() -> int \| None` | Gibt die Einstellung zur Anzeige gedrehten Texts zurück. |
| `SetRotatedTextDisplay(value: int) -> bool` | Setzt die Einstellung zur Anzeige gedrehten Texts. |
| `GetDisplayBitmaps() -> int \| None` | Gibt die Einstellung zur Anzeige von Rasterbildern zurück. |
| `SetDisplayBitmaps(value: int) -> bool` | Setzt die Einstellung zur Anzeige von Rasterbildern. |
| `GetHiddenLineShade() -> int \| None` | Gibt die Schattierung verdeckter Linien zurück. |
| `SetHiddenLineShade(value: int) -> bool` | Setzt die Schattierung verdeckter Linien. |
| `GetDisplay3DLoci() -> int \| None` | Gibt die Einstellung zur Anzeige von 3D-Punkten zurück. |
| `SetDisplay3DLoci(value: int) -> bool` | Setzt die Einstellung zur Anzeige von 3D-Punkten. |
| `GetDefaultRenderMode() -> int \| None` | Gibt die Standard-Darstellungsart zurück. |
| `SetDefaultRenderMode(value: int) -> bool` | Setzt die Standard-Darstellungsart. |
| `GetDefaultProjection() -> int \| None` | Gibt die Standardprojektion zurück. |
| `SetDefaultProjection(value: int) -> bool` | Setzt die Standardprojektion. |
| `Get3DRotationResponse() -> int \| None` | Gibt die Reaktionsempfindlichkeit bei 3D-Drehungen zurück (1..5). |
| `Set3DRotationResponse(value: int) -> bool` | Setzt die Reaktionsempfindlichkeit bei 3D-Drehungen. |

### EditingSettings

> **Vollständiger Name:** `api.EditingSettings` · **Erbt von:** `api.Object`

Bearbeitungs- und Sitzungseinstellungen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `EditingSettings()` | Zustandslose Sicht auf die Bearbeitungs- und Sitzungseinstellungen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetClickDrag() -> bool \| None` | Ob *Klicken und Ziehen* eingeschaltet ist. |
| `SetClickDrag(value: bool) -> bool` | Schaltet *Klicken und Ziehen* ein oder aus. |
| `GetOffsetDuplicates() -> bool \| None` | Ob *Duplikate versetzen* eingeschaltet ist. |
| `SetOffsetDuplicates(value: bool) -> bool` | Schaltet *Duplikate versetzen* ein oder aus. |
| `GetAssociateDimensions() -> bool \| None` | Ob *Assoziative Bemaßungen* eingeschaltet ist. |
| `SetAssociateDimensions(value: bool) -> bool` | Schaltet *Assoziative Bemaßungen* ein oder aus. |
| `GetAutoAssociateDimensions() -> bool \| None` | Ob *Bemaßungen automatisch verknüpfen* eingeschaltet ist. |
| `SetAutoAssociateDimensions(value: bool) -> bool` | Schaltet *Bemaßungen automatisch verknüpfen* ein oder aus. |
| `GetCreateDimensionsInDimensionClass() -> bool \| None` | Ob *Bemaßungen in der Klasse „Bemaßung“ erzeugen* eingeschaltet ist. |
| `SetCreateDimensionsInDimensionClass(value: bool) -> bool` | Schaltet *Bemaßungen in der Klasse „Bemaßung“ erzeugen* ein oder aus. |
| `GetWallAutoJoin() -> bool \| None` | Ob *Wände automatisch verbinden* eingeschaltet ist. |
| `SetWallAutoJoin(value: bool) -> bool` | Schaltet *Wände automatisch verbinden* ein oder aus. |
| `GetUndoViewChanges() -> bool \| None` | Ob *Ansichtsänderungen rückgängig machen* eingeschaltet ist. |
| `SetUndoViewChanges(value: bool) -> bool` | Schaltet *Ansichtsänderungen rückgängig machen* ein oder aus. |
| `GetDuplicateTagsWithObjects() -> bool \| None` | Ob *Datenstempel mit Objekten duplizieren* eingeschaltet ist. |
| `SetDuplicateTagsWithObjects(value: bool) -> bool` | Schaltet *Datenstempel mit Objekten duplizieren* ein oder aus. |
| `GetOccludedPickingAndSnapping() -> bool \| None` | Ob *Verdeckte Objekte aktivieren und fangen* eingeschaltet ist. |
| `SetOccludedPickingAndSnapping(value: bool) -> bool` | Schaltet *Verdeckte Objekte aktivieren und fangen* ein oder aus. |
| `GetMaxUndos() -> int \| None` | Gibt die maximale Anzahl der Rückgängig-Schritte zurück. |
| `SetMaxUndos(value: int) -> bool` | Setzt die maximale Anzahl der Rückgängig-Schritte. |
| `GetAutoSaveInterval() -> int \| None` | Gibt das Intervall für automatisches Speichern zurück. |
| `SetAutoSaveInterval(value: int) -> bool` | Setzt das Intervall für automatisches Speichern. |
| `GetBackupInterval() -> int \| None` | Gibt das Sicherungsintervall zurück. |
| `SetBackupInterval(value: int) -> bool` | Setzt das Sicherungsintervall. |
| `GetLineWeightUnit() -> int \| None` | Gibt die Einheit der Linienstärke zurück. |
| `SetLineWeightUnit(value: int) -> bool` | Setzt die Einheit der Linienstärke. |
| `GetDimensionStandard() -> int \| None` | Gibt den Bemaßungsstandard zurück. |
| `SetDimensionStandard(value: int) -> bool` | Setzt den Bemaßungsstandard. |
| `GetCustomMoveDistance() -> float \| None` | Gibt den benutzerdefinierten Verschiebeabstand zurück. |
| `SetCustomMoveDistance(value: float) -> bool` | Setzt den benutzerdefinierten Verschiebeabstand. |

### SnapSettings

> **Vollständiger Name:** `api.SnapSettings` · **Erbt von:** `api.Object`

Zeigerfang-Einstellungen (Intelligenter Zeiger).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `SnapSettings()` | Zustandslose Sicht auf die Zeigerfang-Einstellungen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `GetSnapToGrid() -> bool \| None` | Ob *Am Raster ausrichten* eingeschaltet ist. |
| `SetSnapToGrid(value: bool) -> bool` | Schaltet *Am Raster ausrichten* ein oder aus. |
| `GetSnapToObjects() -> bool \| None` | Ob *An Objekten ausrichten* eingeschaltet ist. |
| `SetSnapToObjects(value: bool) -> bool` | Schaltet *An Objekten ausrichten* ein oder aus. |
| `GetSnapToLoci() -> bool \| None` | Ob das Ausrichten an Punktobjekten eingeschaltet ist. |
| `SetSnapToLoci(value: bool) -> bool` | Schaltet das Ausrichten an Punktobjekten ein oder aus. |
| `GetSnapToEdgePoints() -> bool \| None` | Ob *An Kantenpunkten ausrichten* eingeschaltet ist. |
| `SetSnapToEdgePoints(value: bool) -> bool` | Schaltet *An Kantenpunkten ausrichten* ein oder aus. |
| `GetSnapToSelectionOnly() -> bool \| None` | Ob *Nur an aktivierten Objekten ausrichten* eingeschaltet ist. |
| `SetSnapToSelectionOnly(value: bool) -> bool` | Schaltet *Nur an aktivierten Objekten ausrichten* ein oder aus. |
| `GetSnapToAngle() -> bool \| None` | Ob *An Winkeln ausrichten* eingeschaltet ist. |
| `SetSnapToAngle(value: bool) -> bool` | Schaltet *An Winkeln ausrichten* ein oder aus. |
| `GetSnapToIntersection() -> bool \| None` | Ob *An Schnittpunkten ausrichten* eingeschaltet ist. |
| `SetSnapToIntersection(value: bool) -> bool` | Schaltet *An Schnittpunkten ausrichten* ein oder aus. |
| `GetSmartPoints() -> bool \| None` | Ob *An Ausrichtpunkt ausrichten* eingeschaltet ist. |
| `SetSmartPoints(value: bool) -> bool` | Schaltet *An Ausrichtpunkt ausrichten* ein oder aus. |
| `GetSnapToDistance() -> bool \| None` | Ob *An Teilstück ausrichten* eingeschaltet ist. |
| `SetSnapToDistance(value: bool) -> bool` | Schaltet *An Teilstück ausrichten* ein oder aus. |
| `GetSmartEdge() -> bool \| None` | Ob *An Ausrichtkante ausrichten* eingeschaltet ist. |
| `SetSmartEdge(value: bool) -> bool` | Schaltet *An Ausrichtkante ausrichten* ein oder aus. |
| `GetConstrainTangent() -> bool \| None` | Ob *Tangential ausrichten* eingeschaltet ist. |
| `SetConstrainTangent(value: bool) -> bool` | Schaltet *Tangential ausrichten* ein oder aus. |
| `GetSnapToEndPoint() -> bool \| None` | Ob *An Endpunkten ausrichten* eingeschaltet ist. |
| `SetSnapToEndPoint(value: bool) -> bool` | Schaltet *An Endpunkten ausrichten* ein oder aus. |
| `GetSnapToMidPoint() -> bool \| None` | Ob *An Mittelpunkten ausrichten* eingeschaltet ist. |
| `SetSnapToMidPoint(value: bool) -> bool` | Schaltet *An Mittelpunkten ausrichten* ein oder aus. |
| `GetSnapToCenter() -> bool \| None` | Ob *An Zentren ausrichten* eingeschaltet ist. |
| `SetSnapToCenter(value: bool) -> bool` | Schaltet *An Zentren ausrichten* ein oder aus. |
| `GetSnapToQuadrant() -> bool \| None` | Ob *An Quadranten ausrichten* eingeschaltet ist. |
| `SetSnapToQuadrant(value: bool) -> bool` | Schaltet *An Quadranten ausrichten* ein oder aus. |
| `GetSnapToInsertionPoint() -> bool \| None` | Ob *An Einfügepunkten ausrichten* eingeschaltet ist. |
| `SetSnapToInsertionPoint(value: bool) -> bool` | Schaltet *An Einfügepunkten ausrichten* ein oder aus. |
| `GetSnapToVertex() -> bool \| None` | Ob *An Eckpunkten ausrichten* eingeschaltet ist. |
| `SetSnapToVertex(value: bool) -> bool` | Schaltet *An Eckpunkten ausrichten* ein oder aus. |
| `GetSnapToEdge() -> bool \| None` | Ob *An Kanten ausrichten* eingeschaltet ist. |
| `SetSnapToEdge(value: bool) -> bool` | Schaltet *An Kanten ausrichten* ein oder aus. |
| `GetSnapToMasterPoints() -> bool \| None` | Ob *An Hauptfangpunkten ausrichten* eingeschaltet ist. |
| `SetSnapToMasterPoints(value: bool) -> bool` | Schaltet *An Hauptfangpunkten ausrichten* ein oder aus. |
| `GetSnapToRelativeAngles() -> bool \| None` | Ob *An relativen Winkeln ausrichten* eingeschaltet ist. |
| `SetSnapToRelativeAngles(value: bool) -> bool` | Schaltet *An relativen Winkeln ausrichten* ein oder aus. |
| `GetSnapToAlternateCoordinateSystem() -> bool \| None` | Ob *Am alternativen Koordinatensystem ausrichten* eingeschaltet ist. |
| `SetSnapToAlternateCoordinateSystem(value: bool) -> bool` | Schaltet *Am alternativen Koordinatensystem ausrichten* ein oder aus. |
| `GetSnapToAnglesFromAxes() -> bool \| None` | Ob *An Winkeln relativ zu den Achsen ausrichten* eingeschaltet ist (schreibgeschützt). |
| `GetSnapToCombinedPageArea() -> bool \| None` | Ob *Am gesamten Seitenbereich ausrichten* eingeschaltet ist. |
| `SetSnapToCombinedPageArea(value: bool) -> bool` | Schaltet *Am gesamten Seitenbereich ausrichten* ein oder aus. |
| `GetSnapToIndividualPages() -> bool \| None` | Ob *An einzelnen Seiten ausrichten* eingeschaltet ist. |
| `SetSnapToIndividualPages(value: bool) -> bool` | Schaltet *An einzelnen Seiten ausrichten* ein oder aus. |
| `GetFloatingDatum() -> bool \| None` | Ob *Temporärer Nullpunkt* eingeschaltet ist. |
| `SetFloatingDatum(value: bool) -> bool` | Schaltet *Temporärer Nullpunkt* ein oder aus. |
| `GetShowSnapBox() -> bool \| None` | Ob *Fangbereich anzeigen* eingeschaltet ist. |
| `SetShowSnapBox(value: bool) -> bool` | Schaltet *Fangbereich anzeigen* ein oder aus. |
| `GetShowSelectionBox() -> bool \| None` | Ob *Aktivierungsbereich anzeigen* eingeschaltet ist. |
| `SetShowSelectionBox(value: bool) -> bool` | Schaltet *Aktivierungsbereich anzeigen* ein oder aus. |
| `GetSnapRadiusPixels() -> int \| None` | Gibt den Fangradius in Pixeln zurück. |
| `SetSnapRadiusPixels(value: int) -> bool` | Setzt den Fangradius in Pixeln. |
| `GetSnapBoxRadius() -> float \| None` | Gibt den Radius des Fangbereichs zurück. |
| `SetSnapBoxRadius(value: float) -> bool` | Setzt den Radius des Fangbereichs. |
| `GetSelectionRadius() -> float \| None` | Gibt den Aktivierungsradius zurück. |
| `SetSelectionRadius(value: float) -> bool` | Setzt den Aktivierungsradius. |

*Winkel*

| Methode | Beschreibung |
|---|---|
| `GetSnapAngles() -> str \| None` | Gibt die Fangwinkel zurück. Durch Kommas getrennte Liste in Grad, z. B. „30,45,60“. |
| `SetSnapAngles(degreesList: str) -> bool` | Setzt die Fangwinkel. |
| `GetRelativeAngle() -> float \| None` | Gibt den relativen Winkel zurück (Radiant). |
| `SetRelativeAngle(radians: float) -> bool` | Setzt den relativen Winkel. |
| `GetAlternateCoordinateSystemAngle() -> float \| None` | Gibt den Winkel des alternativen Koordinatensystems zurück (Radiant). |
| `SetAlternateCoordinateSystemAngle(radians: float) -> bool` | Setzt den Winkel des alternativen Koordinatensystems. |

*Optionen für den Kantenfang*

| Methode | Beschreibung |
|---|---|
| `GetUseEdgeOffset() -> bool \| None` | Ob *Kantenversatz verwenden* eingeschaltet ist. |
| `SetUseEdgeOffset(value: bool) -> bool` | Schaltet *Kantenversatz verwenden* ein oder aus. |
| `GetEdgeOffsetDistance() -> float \| None` | Gibt den Kantenversatzabstand zurück. |
| `SetEdgeOffsetDistance(value: float) -> bool` | Setzt den Kantenversatzabstand. |
| `GetUseProportionalDivision() -> bool \| None` | Ob *Proportionale Teilung verwenden* eingeschaltet ist. |
| `SetUseProportionalDivision(value: bool) -> bool` | Schaltet *Proportionale Teilung verwenden* ein oder aus. |
| `GetProportionalPercent() -> float \| None` | Gibt den Prozentsatz der proportionalen Teilung zurück. |
| `SetProportionalPercent(value: float) -> bool` | Setzt den Prozentsatz der proportionalen Teilung. |
| `GetUseMultipleDivisions() -> bool \| None` | Ob *Mehrfachteilungen verwenden* eingeschaltet ist. |
| `SetUseMultipleDivisions(value: bool) -> bool` | Schaltet *Mehrfachteilungen verwenden* ein oder aus. |
| `GetDivisionDistance() -> float \| None` | Gibt den Teilungsabstand zurück. |
| `SetDivisionDistance(value: float) -> bool` | Setzt den Teilungsabstand. |

### GridSettings

> **Vollständiger Name:** `api.GridSettings` · **Erbt von:** `api.Object`

Rastereinstellungen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `GridSettings()` | Zustandslose Sicht auf die Rastereinstellungen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetShowGrid() -> bool \| None` | Ob *Raster anzeigen* eingeschaltet ist. |
| `SetShowGrid(value: bool) -> bool` | Schaltet *Raster anzeigen* ein oder aus. |
| `GetPrintGrid() -> bool \| None` | Ob *Raster drucken* eingeschaltet ist. |
| `SetPrintGrid(value: bool) -> bool` | Schaltet *Raster drucken* ein oder aus. |
| `GetSnapToGrid() -> bool \| None` | Ob *Am Raster ausrichten* eingeschaltet ist. |
| `SetSnapToGrid(value: bool) -> bool` | Schaltet *Am Raster ausrichten* ein oder aus. |
| `GetSnapGridX() -> float \| None` | Gibt den X-Abstand des Ausrichtrasters zurück. |
| `SetSnapGridX(value: float) -> bool` | Setzt den X-Abstand des Ausrichtrasters. |
| `GetSnapGridY() -> float \| None` | Gibt den Y-Abstand des Ausrichtrasters zurück. |
| `SetSnapGridY(value: float) -> bool` | Setzt den Y-Abstand des Ausrichtrasters. |
| `GetReferenceGridX() -> float \| None` | Gibt den X-Abstand des sichtbaren Rasters zurück. |
| `SetReferenceGridX(value: float) -> bool` | Setzt den X-Abstand des sichtbaren Rasters. |
| `GetReferenceGridY() -> float \| None` | Gibt den Y-Abstand des sichtbaren Rasters zurück. |
| `SetReferenceGridY(value: float) -> bool` | Setzt den Y-Abstand des sichtbaren Rasters. |
| `GetSheetLayerSnapGridX() -> float \| None` | Gibt den X-Abstand des Ausrichtrasters auf Layoutebenen zurück. |
| `SetSheetLayerSnapGridX(value: float) -> bool` | Setzt den X-Abstand des Ausrichtrasters auf Layoutebenen. |
| `GetSheetLayerSnapGridY() -> float \| None` | Gibt den Y-Abstand des Ausrichtrasters auf Layoutebenen zurück. |
| `SetSheetLayerSnapGridY(value: float) -> bool` | Setzt den Y-Abstand des Ausrichtrasters auf Layoutebenen. |
| `GetAngle() -> float \| None` | Gibt den Winkel zurück (Radiant). |
| `SetAngle(radians: float) -> bool` | Setzt den Winkel. |
| `GetAngleY() -> float \| None` | Gibt den Y-Winkel zurück (Radiant). |
| `SetAngleY(radians: float) -> bool` | Setzt den Y-Winkel. |

### StackLayersSettings

> **Vollständiger Name:** `api.StackLayersSettings` · **Erbt von:** `api.Object`

Einstellungen für die Modellansicht.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `StackLayersSettings()` | Zustandslose Sicht auf die Einstellungen der Modellansicht. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetEnabled() -> bool \| None` | Ob *Aktiviert* eingeschaltet ist. |
| `SetEnabled(value: bool) -> bool` | Schaltet *Aktiviert* ein oder aus. |
| `GetCreate2DObjects() -> bool \| None` | Ob *2D-Objekte erzeugen* eingeschaltet ist. |
| `SetCreate2DObjects(value: bool) -> bool` | Schaltet *2D-Objekte erzeugen* ein oder aus. |
| `GetIgnoreOtherScales() -> bool \| None` | Ob *Andere Maßstäbe ignorieren* eingeschaltet ist. |
| `SetIgnoreOtherScales(value: bool) -> bool` | Schaltet *Andere Maßstäbe ignorieren* ein oder aus. |
| `GetRestoreViews() -> bool \| None` | Ob *Ansichten wiederherstellen* eingeschaltet ist. |
| `SetRestoreViews(value: bool) -> bool` | Schaltet *Ansichten wiederherstellen* ein oder aus. |
| `GetCenterView() -> bool \| None` | Ob *Ansicht zentrieren* eingeschaltet ist. |
| `SetCenterView(value: bool) -> bool` | Schaltet *Ansicht zentrieren* ein oder aus. |
| `GetShowPageBoundary() -> bool \| None` | Ob *Seitenbegrenzung anzeigen* eingeschaltet ist. |
| `SetShowPageBoundary(value: bool) -> bool` | Schaltet *Seitenbegrenzung anzeigen* ein oder aus. |
| `GetOnlyActiveLayer2DObjects() -> bool \| None` | Ob *Nur 2D-Objekte der aktiven Ebene* eingeschaltet ist. |
| `SetOnlyActiveLayer2DObjects(value: bool) -> bool` | Schaltet *Nur 2D-Objekte der aktiven Ebene* ein oder aus. |
| `GetOnlyStoryLayers() -> bool \| None` | Ob *Nur Geschossebenen* eingeschaltet ist. |
| `SetOnlyStoryLayers(value: bool) -> bool` | Schaltet *Nur Geschossebenen* ein oder aus. |

### UnitSettings

> **Vollständiger Name:** `api.UnitSettings` · **Erbt von:** `api.Object`

Primäre oder sekundäre Bemaßungseinheiten des aktiven Dokuments.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `UnitSettings(primary: bool = True)` | Sicht auf die primären Einheiten (`primary=True`) oder auf die sekundären Einheiten. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `IsPrimary() -> bool` | True für die primären Einheiten, False für die sekundären Einheiten. |
| `GetName() -> str \| None` | Gibt den Namen zurück. |
| `SetName(value: str) -> bool` | Setzt den Namen. |
| `GetMark() -> str \| None` | Gibt das Einheitenzeichen zurück. |
| `SetMark(value: str) -> bool` | Setzt das Einheitenzeichen. |
| `GetUnitsPerInch() -> float \| None` | Gibt die Anzahl der Einheiten pro Zoll zurück. |
| `SetUnitsPerInch(value: float) -> bool` | Setzt die Anzahl der Einheiten pro Zoll. |
| `GetStyle() -> int \| None` | Gibt den Stil zurück (Rohwert des Einheitenstils). |
| `SetStyle(value: int) -> bool` | Setzt den Stil. |
| `GetIsMetric() -> bool \| None` | Ob *Metrisch* eingeschaltet ist. |
| `IsMetric() -> bool \| None` | True, wenn die Einheiten metrisch sind (wie `GetIsMetric`). |
| `SetIsMetric(value: bool) -> bool` | Schaltet *Metrisch* ein oder aus. |
| `GetShowUnitMark() -> bool \| None` | Ob *Einheitenzeichen anzeigen* eingeschaltet ist. |
| `SetShowUnitMark(value: bool) -> bool` | Schaltet *Einheitenzeichen anzeigen* ein oder aus. |
| `GetLeadingZero() -> bool \| None` | Ob *Führende Null* eingeschaltet ist. |
| `SetLeadingZero(value: bool) -> bool` | Schaltet *Führende Null* ein oder aus. |
| `GetTrailingZeros() -> bool \| None` | Ob *Nachgestellte Nullen* eingeschaltet ist. |
| `SetTrailingZeros(value: bool) -> bool` | Schaltet *Nachgestellte Nullen* ein oder aus. |
| `GetDisplayAsFraction() -> bool \| None` | Ob *Als Bruch anzeigen* eingeschaltet ist. |
| `SetDisplayAsFraction(value: bool) -> bool` | Schaltet *Als Bruch anzeigen* ein oder aus. |
| `GetShowThousandsSeparator() -> bool \| None` | Ob *Tausendertrennzeichen anzeigen* eingeschaltet ist. |
| `SetShowThousandsSeparator(value: bool) -> bool` | Schaltet *Tausendertrennzeichen anzeigen* ein oder aus. |
| `GetDecimalDisplayPrecision() -> int \| None` | Gibt die Dezimalgenauigkeit der Anzeige zurück. |
| `SetDecimalDisplayPrecision(value: int) -> bool` | Setzt die Dezimalgenauigkeit der Anzeige. |
| `GetDecimalDimensionPrecision() -> int \| None` | Gibt die Dezimalgenauigkeit von Bemaßungen zurück. |
| `SetDecimalDimensionPrecision(value: int) -> bool` | Setzt die Dezimalgenauigkeit von Bemaßungen. |
| `GetFractionalDisplayPrecision() -> int \| None` | Gibt die Genauigkeit der Bruchanzeige zurück. |
| `SetFractionalDisplayPrecision(value: int) -> bool` | Setzt die Genauigkeit der Bruchanzeige. |
| `GetFractionalDimensionPrecision() -> int \| None` | Gibt die Genauigkeit von Bemaßungen in Bruchdarstellung zurück. |
| `SetFractionalDimensionPrecision(value: int) -> bool` | Setzt die Genauigkeit von Bemaßungen in Bruchdarstellung. |
| `GetAngularUnit() -> AngularUnit \| None` | Gibt die Winkeleinheit zurück. |
| `SetAngularUnit(value: AngularUnit) -> bool` | Setzt die Winkeleinheit. |
| `GetWorldUnitsPerUnit() -> float \| None` | Nur primäre Einheiten (None / False für die sekundären Einheiten) (schreibgeschützt). |
| `GetSquareUnitDivision() -> int \| None` | Gibt die Unterteilung der Quadrateinheit zurück. |
| `SetSquareUnitDivision(value: int) -> bool` | Setzt die Unterteilung der Quadrateinheit. |
| `GetSquareUnitMark() -> str \| None` | Gibt das Zeichen der Quadrateinheit zurück. |
| `SetSquareUnitMark(value: str) -> bool` | Setzt das Zeichen der Quadrateinheit. |
| `GetAreaUnitName() -> str \| None` | Gibt den Namen der Flächeneinheit zurück. |
| `SetAreaUnitName(value: str) -> bool` | Setzt den Namen der Flächeneinheit. |
| `GetAreaUnitMark() -> str \| None` | Gibt das Zeichen der Flächeneinheit zurück. |
| `SetAreaUnitMark(value: str) -> bool` | Setzt das Zeichen der Flächeneinheit. |
| `GetAreaUnitsPerSquareInch() -> float \| None` | Gibt die Anzahl der Flächeneinheiten pro Quadratzoll zurück. |
| `SetAreaUnitsPerSquareInch(value: float) -> bool` | Setzt die Anzahl der Flächeneinheiten pro Quadratzoll. |
| `GetAreaDecimalPrecision() -> int \| None` | Gibt die Dezimalgenauigkeit für Flächen zurück. |
| `SetAreaDecimalPrecision(value: int) -> bool` | Setzt die Dezimalgenauigkeit für Flächen. |
| `GetVolumeUnitName() -> str \| None` | Gibt den Namen der Volumeneinheit zurück. |
| `SetVolumeUnitName(value: str) -> bool` | Setzt den Namen der Volumeneinheit. |
| `GetVolumeUnitMark() -> str \| None` | Gibt das Zeichen der Volumeneinheit zurück. |
| `SetVolumeUnitMark(value: str) -> bool` | Setzt das Zeichen der Volumeneinheit. |
| `GetVolumeUnitsPerCubicInch() -> float \| None` | Gibt die Anzahl der Volumeneinheiten pro Kubikzoll zurück. |
| `SetVolumeUnitsPerCubicInch(value: float) -> bool` | Setzt die Anzahl der Volumeneinheiten pro Kubikzoll. |
| `GetVolumeDecimalPrecision() -> int \| None` | Gibt die Dezimalgenauigkeit für Volumen zurück. |
| `SetVolumeDecimalPrecision(value: int) -> bool` | Setzt die Dezimalgenauigkeit für Volumen. |
| `GetDocumentAngularUnit() -> AngularUnit \| None` | Winkeleinstellungen des Dokuments (gemeinsam für primäre und sekundäre Einheiten). |
| `SetDocumentAngularUnit(value: AngularUnit) -> bool` | Setzt die Winkeleinheit des Dokuments (Winkeleinstellungen des Dokuments, gemeinsam für primäre und sekundäre Einheiten). |
| `GetDocumentAngularPrecision() -> int \| None` | Gibt die Winkelgenauigkeit des Dokuments zurück. |
| `SetDocumentAngularPrecision(value: int) -> bool` | Setzt die Winkelgenauigkeit des Dokuments. |

### TextDefaults

> **Vollständiger Name:** `api.TextDefaults` · **Erbt von:** `api.Object`

Text-Vorgabeeinstellungen für neue Textobjekte.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `TextDefaults()` | Zustandslose Sicht auf die Standard-Texteinstellungen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetFontName() -> str \| None` | Gibt den Namen der Schriftart zurück. |
| `SetFontName(value: str) -> bool` | Setzt den Namen der Schriftart. |
| `GetSize() -> float \| None` | Gibt die Größe zurück (Welteinheiten). |
| `SetSize(value: float) -> bool` | Setzt die Größe. |
| `GetStyle() -> TextStyleData \| None` | Gibt den Stil zurück. |
| `SetStyle(value: TextStyleData) -> bool` | Setzt den Stil. |
| `GetJustification() -> TextJustification \| None` | Gibt die horizontale Ausrichtung zurück. |
| `SetJustification(value: TextJustification) -> bool` | Setzt die horizontale Ausrichtung. |
| `GetVerticalAlignment() -> TextVerticalAlignment \| None` | Gibt die vertikale Ausrichtung zurück. |
| `SetVerticalAlignment(value: TextVerticalAlignment) -> bool` | Setzt die vertikale Ausrichtung. |
| `GetLineSpacing() -> TextLineSpacing \| None` | Gibt den Zeilenabstand zurück. |
| `SetLineSpacing(value: TextLineSpacing) -> bool` | Setzt den Zeilenabstand. |
| `GetLeading() -> float \| None` | Gibt den Durchschuss (benutzerdefinierten Zeilenabstand) zurück. |
| `SetLeading(value: float) -> bool` | Setzt den Durchschuss. |

### DefaultAttributes

> **Vollständiger Name:** `api.DefaultAttributes` · **Erbt von:** `api.Object`

Standardattribute für neue Objekte (die Attributpalette, wenn nichts aktiviert ist). Die Methoden `SetXxxByClass()` lassen das Attribut der aktiven Klasse folgen; das Setzen eines ausdrücklichen Werts hebt die entsprechende Kennzeichnung „nach Klasse“ auf.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `DefaultAttributes()` | Zustandslose Sicht auf die Standardattribute für neue Objekte. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `GetColors() -> ObjectColors \| None` | Farben. |
| `SetColors(colors: ObjectColors) -> bool` | Setzt die Farben. |
| `GetPenColorsByClass() -> bool \| None` | Ob *Stiftfarben gemäß Klasse* eingeschaltet ist. |
| `SetPenColorsByClass() -> bool` | Setzt die Einstellung „Stiftfarben gemäß Klasse“. |
| `GetFillColorsByClass() -> bool \| None` | Ob *Füllfarben gemäß Klasse* eingeschaltet ist. |
| `SetFillColorsByClass() -> bool` | Setzt die Einstellung „Füllfarben gemäß Klasse“. |

*Stift*

| Methode | Beschreibung |
|---|---|
| `GetPenStyle() -> int \| None` | Unverarbeiteter Stiftstil; dieselben Werte wie bei `PenAttributes.GetStyle`. |
| `SetPenStyle(style: int) -> bool` | Setzt den Stiftstil (Stiftstil-Rohwert, gleiche Werte wie bei `PenAttributes.GetStyle`). |
| `GetPenStyleByClass() -> bool \| None` | Ob *Stiftstil gemäß Klasse* eingeschaltet ist. |
| `SetPenStyleByClass() -> bool` | Setzt die Einstellung „Stiftstil gemäß Klasse“. |
| `GetLineWeightMils() -> int \| None` | Gibt die Linienstärke in Tausendstel Zoll zurück. |
| `SetLineWeightMils(mils: int) -> bool` | Setzt die Linienstärke in Tausendstel Zoll. |
| `GetLineWeightByClass() -> bool \| None` | Ob *Linienstärke gemäß Klasse* eingeschaltet ist. |
| `SetLineWeightByClass() -> bool` | Setzt die Einstellung „Linienstärke gemäß Klasse“. |

*Füllung*

| Methode | Beschreibung |
|---|---|
| `GetFillStyle() -> int \| None` | Unverarbeiteter Füllstil; dieselben Werte wie bei `FillAttributes.GetStyle`. |
| `SetFillStyle(style: int) -> bool` | Setzt den Füllstil (Füllstil-Rohwert, gleiche Werte wie bei `FillAttributes.GetStyle`). |
| `GetFillStyleByClass() -> bool \| None` | Ob *Füllstil gemäß Klasse* eingeschaltet ist. |
| `SetFillStyleByClass() -> bool` | Setzt die Einstellung „Füllstil gemäß Klasse“. |
| `GetFillTypeRaw() -> int \| None` | Gibt den Rohwert der Füllungsart zurück (schreibgeschützt). |
| `GetHatch() -> int \| None` | Gibt die Schraffur zurück. |
| `SetHatch(hatch: int) -> bool` | Setzt die Schraffur. |
| `GetGradient() -> int \| None` | Gibt den Farbverlauf zurück. |
| `SetGradient(gradient: int) -> bool` | Setzt den Farbverlauf. |
| `GetImageFill() -> int \| None` | Gibt die Bildfüllung zurück. |
| `SetImageFill(image: int) -> bool` | Setzt die Bildfüllung. |
| `GetTile() -> int \| None` | Gibt das Mosaik zurück. |
| `SetTile(tile: int) -> bool` | Setzt das Mosaik. |

*Deckkraft*

| Methode | Beschreibung |
|---|---|
| `GetPenOpacity() -> int \| None` | Gibt die Deckkraft des Stifts zurück. |
| `GetFillOpacity() -> int \| None` | Gibt die Deckkraft der Füllung zurück. |
| `SetOpacity(pen: int, fill: int) -> bool` | Setzt die Deckkraft. |
| `GetPenOpacityByClass() -> bool \| None` | Ob *Stiftdeckkraft gemäß Klasse* eingeschaltet ist. |
| `GetFillOpacityByClass() -> bool \| None` | Ob *Fülldeckkraft gemäß Klasse* eingeschaltet ist. |
| `SetOpacityByClass(penByClass: bool, fillByClass: bool) -> bool` | Setzt die Einstellung „Deckkraft gemäß Klasse“. |

*Linienendzeichen*

| Methode | Beschreibung |
|---|---|
| `GetBeginningMarker() -> Marker \| None` | Gibt das Linienendzeichen am Anfang zurück. |
| `SetBeginningMarker(marker: Marker) -> bool` | Setzt das Linienendzeichen am Anfang. |
| `GetEndMarker() -> Marker \| None` | Gibt das Linienendzeichen am Ende zurück. |
| `SetEndMarker(marker: Marker) -> bool` | Setzt das Linienendzeichen am Ende. |
| `GetMarkersByClass() -> bool \| None` | Ob *Linienendzeichen gemäß Klasse* eingeschaltet ist. |
| `SetMarkersByClass() -> bool` | Setzt die Einstellung „Linienendzeichen gemäß Klasse“. |
| `GetDocumentDropShadow() -> DropShadow \| None` | Schlagschatten des Dokuments (Dokumenteinstellungen). |
| `GetClass() -> ClassAttributes` | Klasse für neue Objekte und neue Bemaßungen. |
| `SetClass(theClass: ClassAttributes) -> bool` | Setzt die Klasse (Klasse für neue Objekte und neue Bemaßungen). |
| `GetDimensionClass() -> ClassAttributes` | Gibt die Klasse „Bemaßung“ zurück. |
| `SetDimensionClass(theClass: ClassAttributes) -> bool` | Setzt die Bemaßungsklasse. |

### LayerContents

> **Vollständiger Name:** `api.LayerContents` · **Erbt von:** `api.Object`

Objektanzahl und Begrenzung der Objekte auf der obersten Stufe einer Ebene.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `LayerContents()` | Standardwert (Felder mit ihren Standardwerten). |
| `LayerContents(fObjectCount, fBounds)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fObjectCount` | `int` | Anzahl der Objekte auf der obersten Hierarchiestufe. |
| `fBounds` | `Math.Rect2D \| None` | Begrenzungen der Objekte auf der obersten Hierarchiestufe; `None` bei einer leeren Ebene. |

### Layer

> **Vollständiger Name:** `api.Layer` · **Erbt von:** `api.Object`

Eine Ebene (Konstruktions- oder Layoutebene). Die Erzeugung aus einem Handle, das keine Ebene bezeichnet, ergibt ein ungültiges Objekt (`IsValid()` == `False`).

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Layer(hLayer: Handle)` | Verweist auf die vorhandene Ebene `hLayer`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `GetHandle() -> Handle` | Handle der Ebene. |
| `IsValid() -> bool` | True, wenn dieses Objekt auf eine vorhandene Ebene verweist. |

*Identität*

| Methode | Beschreibung |
|---|---|
| `GetName() -> str \| None` | Gibt den Namen zurück. |
| `SetName(name: str) -> bool` | Setzt den Namen. |
| `GetType() -> LayerType \| None` | Gibt den Typ zurück. |
| `IsDesignLayer() -> bool` | True für eine Konstruktionsebene. |
| `IsSheetLayer() -> bool` | True für eine Layoutebene. |
| `GetNext() -> Layer` | Gibt das nächste Element zurück. |
| `GetPrevious() -> Layer` | Gibt das vorherige Element zurück. |

*Zustand*

| Methode | Beschreibung |
|---|---|
| `IsActive() -> bool` | True, wenn dies die aktive Ebene ist. |
| `Activate() -> bool` | Macht diese Ebene zur aktiven Ebene. |
| `GetVisibility() -> LayerVisibility \| None` | Gibt die Sichtbarkeit zurück. |
| `SetVisibility(visibility: LayerVisibility) -> bool` | Setzt die Sichtbarkeit. |

*Eigenschaften von Konstruktionsebenen*

| Methode | Beschreibung |
|---|---|
| `GetScale() -> float \| None` | Gibt den Maßstab zurück (1:scale). |
| `SetScale(scale: float) -> bool` | Setzt den Maßstab. |
| `GetElevation() -> float \| None` | Gibt die Höhenlage zurück (Welteinheiten). |
| `SetElevation(elevation: float) -> bool` | Setzt die Höhenlage. |
| `GetThickness() -> float \| None` | Gibt die Dicke zurück (Welteinheiten). |
| `SetThickness(thickness: float) -> bool` | Setzt die Dicke. |
| `GetRenderMode() -> int \| None` | Gibt die Darstellungsart zurück (Rohwert der Darstellungsart). |
| `GetProjection() -> int \| None` | Gibt die Projektion zurück (Rohwert der Projektion). |
| `GetStory() -> Story` | Geschoss einer Konstruktionsebene. Eine Konstruktionsebene gehört höchstens einem Geschoss an und hat höchstens einen Referenzhöhentyp: den Namen ihrer Referenzhöhe im Geschoss (siehe Story). Änderungen aktualisieren die Geschossreferenzhöhen, erfassen die Ebene und die Geschossdaten für die Rückgängig-Funktion und aktualisieren die an die Geschosse gebundenen Objekte (z. B. Wände). Das Geschoss der Ebene; ungültig, wenn die Ebene keinem Geschoss angehört. |
| `GetLevelType() -> str \| None` | Referenzhöhentyp der Ebene; leer, wenn sie keinen hat, `None` bei einem ungültigen Objekt. |
| `SetLevelType(levelType: str) -> bool` | Innerhalb eines Geschosses wird die Ebene auf die Referenzhöhe dieses Typs verschoben, wie bei AssociateWithStory(`GetStory()`, levelType); ein leerer Wert entfernt den Referenzhöhentyp (die Ebene behält ihr Geschoss und ihre Höhenlage, das Geschoss verliert die Referenzhöhe). Ein Referenzhöhentyp, der im Dokument noch nicht vorhanden ist, wird hinzugefügt. Nur für Konstruktionsebenen. |
| `AssociateWithStory(story: Story, levelType: str = '') -> bool` | Ordnet die Konstruktionsebene dem Geschoss `story` mit dem Referenzhöhentyp `levelType` zu (leer: aktueller Referenzhöhentyp der Ebene); ein vorheriges Geschoss der Ebene verliert deren Referenzhöhe. Die Ebene wird auf die Höhenlage der Referenzhöhe verschoben: den Versatz der Geschossreferenzhöhe dieses Typs, andernfalls den der ersten Referenzhöhenvorgabe dieses Typs, andernfalls 0. Schlägt fehl, wenn eine andere Ebene des Geschosses diesen Referenzhöhentyp hat oder kein Referenzhöhentyp angegeben ist. Ein Referenzhöhentyp, der im Dokument noch nicht vorhanden ist, wird hinzugefügt. |
| `DetachFromStory() -> bool` | Entfernt die Konstruktionsebene aus ihrem Geschoss: Sie behält ihre Höhenlage und verliert ihr Geschoss und ihren Referenzhöhentyp; das Geschoss verliert die Referenzhöhe. `True`, wenn die Ebene keinem Geschoss angehört. |

*Eigenschaften von Layoutebenen*

| Methode | Beschreibung |
|---|---|
| `GetDescription() -> str \| None` | Gibt die Beschreibung zurück (Layouttitel). |
| `SetDescription(description: str) -> bool` | Setzt die Beschreibung. |
| `GetDPI() -> int \| None` | Gibt die DPI zurück. |
| `SetDPI(dpi: int) -> bool` | Setzt die DPI. |
| `GetFirstObject() -> Handle` | Inhalt (Objekte auf der obersten Hierarchiestufe). Wie VectorScript FInLayer / NextObj erfassen diese Methoden nur Zeichnungsobjekte: Rückgängig-Platzhalter gelöschter Objekte und die Abschlussmarkierung der Objektliste werden übersprungen. Bei einer leeren Ebene ist das erste / letzte Objekt null. ForEachObject ermittelt das nächste Objekt vor dem Aufruf der Rückruffunktion, sodass diese das aktuelle Objekt löschen oder verschieben darf. |
| `GetLastObject() -> Handle` | Gibt das letzte Objekt zurück. |
| `ForEachObject(callback: callable(Handle)) -> None` | Ruft `callback` für jedes Objekt auf der obersten Hierarchiestufe der Ebene auf. Inhalt (Objekte auf der obersten Hierarchiestufe). Wie VectorScript FInLayer / NextObj erfassen diese Methoden nur Zeichnungsobjekte: Rückgängig-Platzhalter gelöschter Objekte und die Abschlussmarkierung der Objektliste werden übersprungen. Bei einer leeren Ebene ist das erste / letzte Objekt null. ForEachObject ermittelt das nächste Objekt vor dem Aufruf der Rückruffunktion, sodass diese das aktuelle Objekt löschen oder verschieben darf. |
| `GetObjects() -> list[Handle]` | Gibt die Objekte zurück. |
| `GetObjectCount() -> int` | Anzahl der Objekteinträge. |
| `GetBounds() -> Math.Rect2D \| None` | Gibt die Begrenzungen zurück (Begrenzungen der Objekte auf der obersten Hierarchiestufe). |
| `GetContents() -> LayerContents` | Gibt den Inhalt zurück (Objektanzahl und Begrenzungen in einem Durchlauf). |
| `GetObjectsOf(type: type) -> object` | Objekte auf der obersten Hierarchiestufe der Ebene, die Instanzen der Klasse `type` sind, als Liste von `type`-Objekten, z. B. `layer.GetObjectsOf(api.RectangleObject)`. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True, wenn das Objekt gültig ist (entspricht `IsValid()`). |
| `==` | `__eq__(o: Layer) -> bool` | `a == b`: True, wenn beide Objekte auf dieselbe Ebene verweisen. |
| `!=` | `__ne__(o: Layer) -> bool` | `a != b`: True, wenn die Objekte auf unterschiedliche Ebenen verweisen. |

### StoryLevel

> **Vollständiger Name:** `api.StoryLevel` · **Erbt von:** `api.Object`

Eine Referenzhöhe eines Geschosses: eine benannte Höhe (ihr Referenzhöhentyp) relativ zur Geschossbasishöhe, optional mit der Konstruktionsebene dieser Referenzhöhe.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `StoryLevel()` | Standardwert (Felder mit ihren Standardwerten). |
| `StoryLevel(fLevelType, fElevationOffset, fElevation, fLayerName, fLayer)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fLevelType` | `str` | Referenzhöhentyp, innerhalb des Geschosses eindeutig, z. B. „Boden/Decke“ oder „OK-FB“. |
| `fElevationOffset` | `float` | Welteinheiten, relativ zur Geschossbasishöhe. |
| `fElevation` | `float` | Welteinheiten: Geschossbasishöhe + fElevationOffset. |
| `fLayerName` | `str` | Name der Ebene dieser Referenzhöhe; leer bei einer Referenzhöhe ohne Ebene. |
| `fLayer` | `Layer` | Die Konstruktionsebene des Geschosses mit diesem Referenzhöhentyp; ungültig, wenn keine vorhanden ist. |

### StoryLevelTemplate

> **Vollständiger Name:** `api.StoryLevelTemplate` · **Erbt von:** `api.Object`

Eine Referenzhöhenvorgabe (Dialogfenster „Organisation“ > Reiter „Geschosse 3D“ > „Referenzhöhenvorgaben“): eine Vorlage für Geschossreferenzhöhen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `StoryLevelTemplate()` | Standardwert (Felder mit ihren Standardwerten). |
| `StoryLevelTemplate(fIndex, fLevelType, fElevationOffset, fLayerName, fScaleFactor, fDefaultWallHeight)` | Feldwerte: alle Felder als Positionsargumente (in dieser Reihenfolge) oder beliebige Felder als Schlüsselwortargumente. |

**Felder**

| Feld | Typ | Beschreibung |
|---|---|---|
| `fIndex` | `int` | Position in den Referenzhöhenvorgaben, beginnend bei 1. |
| `fLevelType` | `str` | Referenzhöhentyp der daraus erzeugten Referenzhöhen. |
| `fElevationOffset` | `float` | Welteinheiten, relativ zur Geschossbasishöhe. |
| `fLayerName` | `str` | Ebenenname ohne Geschossnamenszusatz; leer: Die Referenzhöhen haben keine Ebene. |
| `fScaleFactor` | `float` | Maßstab der Ebene (1:fScaleFactor). |
| `fDefaultWallHeight` | `float` | Welteinheiten; Wandhöhe der Ebene. |

### Story

> **Vollständiger Name:** `api.Story` · **Erbt von:** `api.Object`

Ein Geschoss: ein Stockwerk des Gebäudes auf einer bestimmten Höhe. Seine Referenzhöhen (StoryLevel) sind Höhen relativ zur Geschossbasishöhe, jeweils mit einem Referenzhöhentyp und optional einer Konstruktionsebene. Wenn sich die Geschossbasishöhe ändert, folgen seine Ebenen und die an seine Referenzhöhen gebundenen Objekte. Geschosse sind Dokumentdaten, keine Zeichnungsobjekte. Die Erzeugung aus einem Handle, das kein Geschoss bezeichnet, ergibt ein ungültiges Objekt (`IsValid()` == `False`).

Rückgängig: Wie die Dialogfenster für Geschosse im Dialogfenster „Organisation“ erfassen die Änderungsmethoden ihre Änderungen im aktuellen Rückgängig-Ereignis (öffnen Sie eines mit `Document.StartUndoEvent`): die Geschossdaten, die Ebenen, die sie ändern, erzeugen oder löschen, und die von ihnen aktualisierten Objekte, die an die geänderten Geschosse, Referenzhöhen und Ebenen gebunden sind. Registrieren Sie Geschosse oder Ebenen, die diese Methoden erzeugen, nicht erneut mit `Document.AddAfterSwapObject` / AddBothSwapObject.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Story(hStory: Handle)` | Verweist auf das vorhandene Geschoss `hStory`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `GetHandle() -> Handle` | Handle des Geschosses. |
| `IsValid() -> bool` | True, wenn dieses Objekt auf ein vorhandenes Geschoss verweist. |
| `Create(name: str, elevation: float, affix: str = '', isPrefix: bool = False) -> Story` *statisch* | Erzeugt ein Geschoss ohne Referenzhöhen auf `elevation` (Welteinheiten); fügen Sie mit AddLevel / AddLevelFromTemplate Referenzhöhen hinzu. `affix` ist das Präfix oder Suffix der Namen der Ebenen, die aus Referenzhöhenvorgaben für das Geschoss erzeugt werden. Jedes Geschoss benötigt einen eigenen Namenszusatz (Vergleich ohne Berücksichtigung der Groß-/Kleinschreibung); auch ein leerer Namenszusatz zählt als einer. `isPrefix` wird wie im Dialogfenster „Neues Geschoss“ weitergegeben, aber von Vectorworks nicht gespeichert (siehe UsesPrefix). Schlägt fehl (ungültiges Objekt), wenn `name` leer oder länger als 63 Zeichen ist oder ein anderes Objekt bezeichnet, wenn `affix` von einem anderen Geschoss verwendet wird oder wenn ein anderes Geschoss diese Höhenlage hat. |

*Identität*

| Methode | Beschreibung |
|---|---|
| `GetName() -> str \| None` | Gibt den Namen zurück. |
| `SetName(name: str) -> bool` | Schlägt bei einem leeren Namen, einem Namen mit mehr als 63 Zeichen oder dem Namen eines anderen Objekts fehl. Wie das Dialogfenster „Geschoss bearbeiten“ benennt die Methode das Geschoss auch in den IFC-Daten um und aktualisiert die Objekte, die den Namen anzeigen. |
| `GetAffix() -> str \| None` | Präfix oder Suffix der Namen der Ebenen, die aus Referenzhöhenvorgaben für das Geschoss erzeugt werden. |
| `SetAffix(affix: str) -> bool` | Schlägt fehl, wenn ein anderes Geschoss `affix` verwendet (ohne Berücksichtigung der Groß-/Kleinschreibung, also auch bei einer reinen Änderung der Schreibweise). Die Namen vorhandener Ebenen ändern sich nicht. |
| `UsesPrefix() -> bool \| None` | Ob die Ebenennamen des Geschosses mit dem Namenszusatz beginnen. Vectorworks speichert dies nicht, sondern leitet es aus den Ebenennamen der Referenzhöhen ab: `True`, wenn keine Referenzhöhe eine Ebene hat. |
| `GetElevation() -> float \| None` | Höhenlage (Welteinheiten). |
| `SetElevation(elevation: float, mode: StoryElevationChangeMode = StoryElevationChangeMode.Single) -> bool` | Verschiebt das Geschoss und je nach `mode` die Geschosse darüber / darunter um elevation - `GetElevation()`; die Konstruktionsebenen der verschobenen Geschosse werden mitverschoben. Schlägt ohne Änderung fehl, wenn ein verschobenes Geschoss die Höhenlage eines nicht verschobenen Geschosses erhalten würde: Zwei Geschosse dürfen nicht dieselbe Höhenlage haben. |
| `GetStoryAbove() -> Story` | Das nach Höhenlage nächste Geschoss darüber / darunter; ungültig, wenn keines vorhanden ist. |
| `GetStoryBelow() -> Story` | Gibt das darunterliegende Geschoss zurück. |
| `Delete(deleteLayers: bool = False) -> bool` | Löscht das Geschoss; das Objekt wird ungültig. Seine Konstruktionsebenen bleiben ohne Geschoss und Referenzhöhentyp erhalten, sofern sie nicht durch `deleteLayers` gelöscht werden; dies schlägt fehl, wenn sie sämtliche Konstruktionsebenen des Dokuments umfassen. |
| `GetLevels() -> list[StoryLevel]` | Referenzhöhen, nach Höhenversatz sortiert. |
| `GetLevel(levelType: str) -> StoryLevel \| None` | Die Referenzhöhe mit diesem Referenzhöhentyp (Vergleich ohne Berücksichtigung der Groß-/Kleinschreibung, wie in Vectorworks); `None`, wenn keine vorhanden ist. |
| `AddLevel(levelType: str, elevationOffset: float, layerName: str = '', createLayerIfMissing: bool = True, scale: float = 0.0) -> bool` | Fügt die Referenzhöhe `levelType` bei `elevationOffset` hinzu (Welteinheiten, relativ zur Geschossbasishöhe). Ohne `layerName` hat die Referenzhöhe keine Ebene. Andernfalls ist ihre Ebene die Konstruktionsebene `layerName`: Eine vorhandene Ebene ohne Referenzhöhentyp wird dem Geschoss auf der Höhe der Referenzhöhe zugeordnet; eine fehlende Ebene wird mit `scale` erzeugt, wenn `createLayerIfMissing` gesetzt ist (0: Maßstab der aktiven Ebene; die aktive Ebene bleibt aktiv). Schlägt fehl, wenn das Geschoss den Referenzhöhentyp bereits hat oder `layerName` eine Layoutebene, eine Ebene mit Referenzhöhentyp oder ein anderes Objekt bezeichnet. Ein Referenzhöhentyp, der im Dokument noch nicht vorhanden ist, wird hinzugefügt. |
| `AddLevelFromTemplate(index: int) -> bool` | Fügt wie in Vectorworks die Referenzhöhe der Referenzhöhenvorgabe `index` hinzu (beginnend bei 1, siehe `Document.GetStoryLevelTemplates`): Wenn die Vorlage einen Ebenennamen hat, wird ihre Ebene als <Ebenenname>-<Namenszusatz> mit dem Maßstab und der Wandhöhe der Vorlage erzeugt; die aktive Ebene bleibt aktiv. Schlägt fehl, wenn das Geschoss diesen Referenzhöhentyp bereits hat. |
| `SetLevelElevationOffset(levelType: str, elevationOffset: float) -> bool` | Verschiebt die Referenzhöhe und ihre Ebene samt Objekten auf `elevationOffset` (Welteinheiten, relativ zum Geschoss). |
| `RemoveLevel(levelType: str, deleteLayer: bool = False) -> bool` | Entfernt die Referenzhöhe. Ihre Ebene bleibt ohne Geschoss und Referenzhöhentyp erhalten, sofern sie nicht durch `deleteLayer` gelöscht wird; dies schlägt fehl, wenn sie die einzige Konstruktionsebene des Dokuments ist. |
| `GetLayers() -> list[Layer]` | Konstruktionsebenen im Geschoss, in der Reihenfolge der Ebenenliste des Dokuments. |
| `GetLayerForLevelType(levelType: str) -> Layer` | Die Konstruktionsebene des Geschosses mit diesem Referenzhöhentyp; ungültig, wenn keine vorhanden ist. |

**Operatoren und Python-Protokolle**

| Operator | Methode | Beschreibung |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True, wenn das Objekt gültig ist (entspricht `IsValid()`). |
| `==` | `__eq__(o: Story) -> bool` | `a == b`: True, wenn beide Objekte auf dasselbe Geschoss verweisen. |
| `!=` | `__ne__(o: Story) -> bool` | `a != b`: True, wenn die Objekte auf unterschiedliche Geschosse verweisen. |

### Document

> **Vollständiger Name:** `api.Document` · **Erbt von:** `api.Object`

Zustandslose Zugriffsschnittstelle für das aktive Vectorworks-Dokument. Bietet Zugriff auf die aktivierten Objekte, Ebenen, Geschosse, Klassen, Objekte, die Ansicht, Einheiten, Standardattribute und Einstellungen. Erzeugen Sie sie bei Bedarf (zwischen Aufrufen wird kein Zustand gespeichert):

```python
import api

doc = api.Document()
if api.Document.IsOpen():                   # there is an active document
    for h in doc.GetSelection():               # iterate the current selection
        rect = api.Document.As(api.RectangleObject, h)
        if rect:
            rect.SetSize(1.0, 2.0)
```

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `Document()` | Zustandslose Zugriffsschnittstelle für das aktive Dokument (zwischen Aufrufen wird kein Zustand gespeichert). |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `IsOpen() -> bool` *statisch* | Ob derzeit ein geöffnetes, aktives Dokument vorhanden ist. Alle anderen Methoden setzen voraus, dass dieser Wert `True` ist. |

*Einstellungen*

| Methode | Beschreibung |
|---|---|
| `Display() -> DisplaySettings` | Die Anzeigeeinstellungen (`DisplaySettings`). |
| `Editing() -> EditingSettings` | Die Bearbeitungs- und Sitzungseinstellungen (`EditingSettings`). |
| `Snapping() -> SnapSettings` | Die Zeigerfang-Einstellungen (`SnapSettings`). |
| `Grid() -> GridSettings` | Die Rastereinstellungen (`GridSettings`). |
| `StackLayers() -> StackLayersSettings` | Die Einstellungen der Modellansicht (`StackLayersSettings`). |
| `PrimaryUnits() -> UnitSettings` | Die primären Bemaßungseinheiten des Dokuments (`UnitSettings`). |
| `SecondaryUnits() -> UnitSettings` | Die sekundären Bemaßungseinheiten des Dokuments (`UnitSettings`). |
| `TextDefaults() -> TextDefaults` | Die Standard-Texteinstellungen für neue Textobjekte (`TextDefaults`). |
| `DefaultAttributes() -> DefaultAttributes` | Die Standardattribute für neue Objekte (`DefaultAttributes`). |

*Aktivierte Objekte*

| Methode | Beschreibung |
|---|---|
| `GetSelectionCount() -> int` | Diese Methoden erfassen die aktivierten Objekte so, wie die Vectorworks-Bearbeitungsbefehle sie sehen: nur auf den bearbeitbaren Ebenen (der aktiven Ebene sowie anderen Ebenen, wenn die Ebenenoptionen deren Bearbeitung zulassen). Verwenden Sie sie für alle Aktionen, die aktivierte Objekte bearbeiten. |
| `HasSelection() -> bool` | True, wenn mindestens ein Objekt aktiviert ist. |
| `GetFirstSelected() -> Handle` | Gibt das erste aktivierte Objekt zurück. |
| `GetSelection(descend: Descend = Descend.None_) -> list[Handle]` | Gibt die aktivierten Objekte für `descend` zurück. |
| `ForEachSelected(callback: callable(Handle), descend: Descend = Descend.None_) -> None` | Ruft `callback` für jedes aktivierte Objekt auf. Diese Methoden erfassen die aktivierten Objekte so, wie die Vectorworks-Bearbeitungsbefehle sie sehen: nur auf den bearbeitbaren Ebenen (der aktiven Ebene sowie anderen Ebenen, wenn die Ebenenoptionen deren Bearbeitung zulassen). Verwenden Sie sie für alle Aktionen, die aktivierte Objekte bearbeiten. |
| `GetSelectionBounds() -> Math.Rect2D \| None` | Gibt die Begrenzungen der aktivierten Objekte zurück. |
| `GetSelectionCountOnAllLayers() -> int` | Dasselbe, jedoch auf allen Ebenen der Zeichnung: Ein Objekt bleibt aktiviert, wenn der Benutzer die Ebene wechselt; daher erfassen diese Methoden die vollständige Aktivierung. Nur zum Lesen – die folgenden Bearbeitungsaktionen wirken weiterhin nur auf bearbeitbare Ebenen. |
| `GetSelectionOnAllLayers(descend: Descend = Descend.None_) -> list[Handle]` | Gibt die aktivierten Objekte auf allen Ebenen für `descend` zurück. |
| `ForEachSelectedOnAllLayers(callback: callable(Handle), descend: Descend = Descend.None_) -> None` | Ruft `callback` für jedes aktivierte Objekt auf jeder Ebene auf. Dasselbe, jedoch auf allen Ebenen der Zeichnung: Ein Objekt bleibt aktiviert, wenn der Benutzer die Ebene wechselt; daher erfassen diese Methoden die vollständige Aktivierung. Nur zum Lesen – die folgenden Bearbeitungsaktionen wirken weiterhin nur auf bearbeitbare Ebenen. |
| `GetSelectionBoundsOnAllLayers() -> Math.Rect2D \| None` | Gibt die Begrenzungen der aktivierten Objekte auf allen Ebenen zurück. |
| `IsSelected(h: Handle) -> bool` | True, wenn das Objekt `h` aktiviert ist. |
| `Select(h: Handle, select: bool = True) -> bool` | Aktiviert das Objekt `h` (bzw. deaktiviert es mit `select=False`). |
| `Select(object: PrimitiveObject, select: bool = True) -> bool` | Aktiviert `object` (bzw. deaktiviert es mit `select=False`). |
| `Deselect(h: Handle) -> bool` | Deaktiviert das Objekt `h`. |
| `Select(objects: list[Handle]) -> int` | Fügt die Objekte `objects` zur Aktivierung hinzu; gibt zurück, wie viele aktiviert wurden. |
| `SetSelection(objects: list[Handle]) -> int` | Setzt die Aktivierung (ersetzt die bisherige Aktivierung). |
| `SelectAll() -> None` | Aktiviert alle Objekte (wie „Bearbeiten“ > „Alles aktivieren“). |
| `DeselectAll() -> None` | Hebt die Aktivierung auf. |
| `GetSelectionOf(type: type, descend: Descend = Descend.None_) -> object` | Aktivierte Objekte, die Instanzen der Klasse `type` sind, als Liste von `type`-Objekten, z. B. `doc.GetSelectionOf(api.Line2DObject)`. |

*Aktionen für aktivierte Objekte*

| Methode | Beschreibung |
|---|---|
| `MoveSelection(offset: Math.Point2D) -> bool` | Verschiebt die aktivierten Objekte um `offset` (Welteinheiten). |
| `RotateSelection(angle: float, center: Math.Point2D) -> bool` | Dreht die aktivierten Objekte um `angle` (Radiant, gegen den Uhrzeigersinn) um den Mittelpunkt `center`. |
| `ScaleSelection(scaleX: float, scaleY: float, center: Math.Point2D) -> bool` | Skaliert die aktivierten Objekte mit `scaleX` / `scaleY` um `center`. |
| `DuplicateSelection(offset: Math.Point2D = Math.Point2D()) -> bool` | Dupliziert die aktivierten Objekte und versetzt die Kopien um `offset`. |
| `GroupSelection() -> Handle` | Gruppiert die aktivierten Objekte; gibt das Handle der neuen Gruppe zurück (null, wenn kein Objekt aktiviert ist). |
| `DeleteSelection(useUndo: bool = True) -> int` | Löscht die aktivierten Objekte (für Rückgängig erfasst, sofern `useUndo` nicht `False` ist); gibt zurück, wie viele gelöscht wurden. |
| `SetSelectionClass(theClass: ClassAttributes, useClassAttributes: bool = False) -> bool` | Setzt die Klasse der aktivierten Objekte. |

*Objekte*

| Methode | Beschreibung |
|---|---|
| `ForEachObject(what: Traverse, callback: callable(Handle), descend: Descend = Descend.None_) -> None` | Besucht jedes Objekt, das `what` entspricht (siehe Traverse). `descend` steuert, ob beim Durchlaufen in Container wie Gruppen, Symbole und Ansichtsbereiche abgestiegen wird (siehe Descend). Die Rückruffunktion wird synchron ausgeführt. |
| `GetObjects(what: Traverse, descend: Descend = Descend.None_) -> list[Handle]` | Sammelt alle Objekte, die `what` entsprechen (siehe ForEachObject). |
| `GetLayerContents(what: Traverse) -> dict[Handle, LayerContents]` | Objektanzahl und Begrenzungen der Objekte auf der obersten Hierarchiestufe, die `what` besucht, mit Ebenenhandles als Schlüssel; Ebenen ohne solche Objekte fehlen. |
| `GetObjectsAtPoint(pt: Math.Point2D, radius: float, what: Traverse = Traverse.Visible, descend: Descend = Descend.None_) -> list[Handle]` | Sammelt Objekte, deren Geometrie innerhalb von `radius` Welteinheiten um `pt` liegt (wie eine Trefferprüfung bei einem Mausklick). |
| `GetObjectsInCriteria(criteria: str) -> list[Handle]` | Sammelt Objekte, die einer Vectorworks-Kriterienzeichenkette entsprechen (dieselbe Syntax wie in VectorScript / Kriteriendialogen), z. B. "(T=RECT)" für alle Rechtecke oder "(C='My Class')" für alle Objekte in der Klasse 'My Class'. |
| `GetCriteriaError(criteria: str) -> str \| None` | Grund, weshalb `criteria` nicht kompiliert werden kann (GetObjectsInCriteria findet dann nichts); `None`, wenn die Kompilierung gelingt. |
| `GetObjectType(h: Handle) -> ObjectType` *statisch* | Objekttyp (Art des geometrischen / strukturellen Objekts). Nur für einen Teil von ObjectType gibt es typisierte Klassen. |
| `AttributesOf(h: Handle) -> ObjectAttributes` *statisch* | Grafische Attribute (Stift, Füllung, Linienendzeichen, Schlagschatten, Klasse, ...) eines beliebigen Objekts. |
| `ClassOf(h: Handle) -> ClassAttributes` *statisch* | Klasse des Objekts `h`. |
| `LayerOf(h: Handle) -> Layer` *statisch* | Die Ebene, die das Objekt letztlich enthält (sucht aufwärts über Gruppen, Symbole, ... nach einer Ebene). |
| `FindByName(name: str) -> Handle` | Suche nach Objekten anhand ihrer Identität. Gibt null zurück, wenn kein Objekt übereinstimmt. |
| `FindByUuid(uuid: str) -> Handle` | Das Objekt mit der dauerhaften UUID `uuid`; ein Null-Handle, wenn keines übereinstimmt. |
| `FindByIndex(index: int) -> Handle` | Das Objekt mit dem internen Index `index`; ein Null-Handle, wenn keines übereinstimmt. |
| `GetUuid(h: Handle) -> str \| None` | Persistente UUID des Objekts, die beim Speichern/Laden unverändert bleibt. |
| `As(type: type, h: Handle) -> object` *statisch* | Das Handle `h` als typisiertes Objekt: eine Instanz der Klasse `type` (zum Beispiel `api.ArcObject`), wenn `type.Is(h)` zutrifft, andernfalls `None`. Beispiel: `arc = api.Document.As(api.ArcObject, h)`. |
| `GetObjectsOf(type: type, what: Traverse = Traverse.All, descend: Descend = Descend.None_) -> object` | Alle Objekte, die `what` entsprechen und Instanzen der Klasse `type` sind, als Liste von `type`-Objekten, z. B. `doc.GetObjectsOf(api.RectangleObject)`. |

*Ebenen*

| Methode | Beschreibung |
|---|---|
| `GetActiveLayer() -> Layer` | Gibt die aktive Ebene zurück. |
| `SetActiveLayer(layer: Layer) -> bool` | Setzt die aktive Ebene. |
| `FindLayer(name: str) -> Layer` | Die Ebene mit dem Namen `name`; ein ungültiges `Layer`-Objekt, wenn keine vorhanden ist. |
| `ForEachLayer(callback: callable(Layer)) -> None` | Ruft `callback` für jede Ebene des Dokuments auf. |
| `GetLayers() -> list[Layer]` | Gibt die Ebenen zurück. |
| `GetLayers(type: LayerType) -> list[Layer]` | Gibt die Ebenen für `type` zurück. |
| `CreateDesignLayer(name: str, scale: float = 1.0) -> Layer` | Erzeugt eine Konstruktionsebene mit dem Namen `name` und dem Maßstab 1:`scale`. |
| `CreateSheetLayer(name: str) -> Layer` | Erzeugt eine Layoutebene mit dem Namen `name`. |
| `GetLayerOptions() -> VisibilityOptions \| None` | Gibt die Ebenenoptionen zurück. |
| `SetLayerOptions(options: VisibilityOptions) -> bool` | Setzt die Ebenenoptionen. |
| `GetActiveLayerScale() -> float \| None` | Gibt den Maßstab der aktiven Ebene zurück. |

*Geschosse*

| Methode | Beschreibung |
|---|---|
| `GetStories() -> list[Story]` | Geschosse des Dokuments, nach Höhenlage sortiert (das unterste zuerst). Siehe Story, auch zum Rückgängig-Verhalten. |
| `FindStory(name: str) -> Story` | Das Geschoss mit dem Namen `name`; ungültig, wenn keines vorhanden ist. |
| `CreateStory(name: str, elevation: float, affix: str = '', isPrefix: bool = False) -> Story` | Erzeugt ein Geschoss mit dem Namen `name` auf `elevation` (wie `Story.Create`); `affix` wird den Namen seiner Referenzhöhenebenen hinzugefügt. Schlägt fehl (ungültiges Objekt) bei einem leeren, zu langen oder bereits verwendeten Namen, einem bereits verwendeten Namenszusatz oder einer bereits belegten Höhenlage. |
| `GetLevelTypes() -> list[str]` | Referenzhöhentypen (Dialogfenster „Organisation“ > Reiter „Geschosse 3D“ > „Referenzhöhentypen“): die Namen von Geschossreferenzhöhen in Dokumentreihenfolge. Namen sind höchstens 63 Zeichen lang. Vectorworks vergleicht sie ohne Berücksichtigung der Groß-/Kleinschreibung; die Geschossmethoden behalten die im Dokument oder Geschoss bereits verwendete Schreibweise bei. Änderungen lassen sich rückgängig machen. |
| `AddLevelType(name: str) -> bool` | Schlägt fehl, wenn der Name bereits vorhanden ist (ohne Berücksichtigung der Groß-/Kleinschreibung). |
| `RenameLevelType(oldName: str, newName: str) -> bool` | Benennt den Referenzhöhentyp auch in Ebenen, Geschossreferenzhöhen, Referenzhöhenvorgaben und geschossgebundenen Objekten um. Schlägt fehl, wenn `newName` bereits vorhanden ist (ohne Berücksichtigung der Groß-/Kleinschreibung), also auch bei einer reinen Änderung der Schreibweise. Rückgängig stellt den Referenzhöhentyp in den Geschossbindungen von Objekten und in Horizontalschnitten nicht wieder her: Vectorworks benennt ihn dort wie im Dialogfenster „Referenzhöhentypen“ um, ohne diese Änderungen zu erfassen. Benennen Sie ihn stattdessen wieder zurück. |
| `DeleteLevelType(name: str) -> bool` | Wie im Dialogfenster „Referenzhöhentypen“: Ebenen und Referenzhöhenvorgaben mit diesem Referenzhöhentyp verlieren ihn; Geschossreferenzhöhen behalten ihn. |
| `GetStoryLevelTemplates() -> list[StoryLevelTemplate]` | Referenzhöhenvorgaben (Dialogfenster „Organisation“ > Reiter „Geschosse 3D“ > „Referenzhöhenvorgaben“), die Vorlagen für Geschossreferenzhöhen. Indizes beginnen bei 1; GetStoryLevelTemplates gibt sie in Indexreihenfolge zurück. Änderungen lassen sich rückgängig machen. |
| `AddStoryLevelTemplate(levelType: str, elevationOffset: float, layerName: str = '', scaleFactor: float = 0.0, defaultWallHeight: float = 0.0) -> int \| None` | Fügt eine Referenzhöhenvorgabe hinzu und gibt ihren Index zurück: Vectorworks fügt sie an erster Stelle ein (Index 1). Mit dem Wert 0 für `scaleFactor` wird der Maßstab der aktiven Ebene verwendet. Schlägt fehl, wenn eine Referenzhöhenvorgabe denselben Referenzhöhentyp und Höhenversatz hat. Ein Referenzhöhentyp, der im Dokument noch nicht vorhanden ist, wird hinzugefügt. |
| `DeleteStoryLevelTemplate(index: int) -> bool` | Löscht die Referenzhöhenvorgabe am Index `index`. |
| `ResetDefaultStoryLevels(deleteExisting: bool) -> bool` | Fügt die Referenzhöhenvorgaben und Referenzhöhentypen der Vectorworks-Vorgaben erneut hinzu (im Dokument vorhandene Referenzhöhentypen bleiben erhalten). `deleteExisting` löscht zunächst die aktuellen Referenzhöhenvorgaben; andernfalls werden die Vorgaben hinzugefügt, wodurch doppelte Referenzhöhenvorgaben entstehen können. |

*Klassen*

| Methode | Beschreibung |
|---|---|
| `GetActiveClass() -> ClassAttributes` | Gibt die aktive Klasse zurück. |
| `SetActiveClass(theClass: ClassAttributes) -> bool` | Setzt die aktive Klasse. |
| `FindClass(name: str) -> ClassAttributes` | Die Klasse mit dem Namen `name`; ein ungültiges `ClassAttributes`-Objekt, wenn keine vorhanden ist. |
| `CreateClass(name: str) -> ClassAttributes` | Erzeugt eine Klasse mit dem Namen `name` (oder gibt die vorhandene zurück). |
| `GetClasses(includeGuestClasses: bool = False) -> list[ClassAttributes]` | Gibt die Klassen für `includeGuestClasses` zurück. |
| `GetClassOptions() -> VisibilityOptions \| None` | Gibt die Klassenoptionen zurück. |
| `SetClassOptions(options: VisibilityOptions) -> bool` | Setzt die Klassenoptionen. |

*Container*

| Methode | Beschreibung |
|---|---|
| `GetDrawingHeader() -> Handle` | Wurzelobjekt der Zeichnung. Wird selten direkt benötigt. |
| `GetDefaultContainer() -> Handle` | Der Container, der neu erzeugte Objekte aufnimmt (die aktive Ebene oder die gerade bearbeitete Gruppe / Symboldefinition). |
| `IsInsideGroup() -> bool \| None` | `True`, wenn der Benutzer gerade den Inhalt einer Gruppe bearbeitet (innerhalb einer mit „Gruppe bearbeiten“ begonnenen Bearbeitungssitzung). |
| `GetEditedGroup() -> Handle` | Die derzeit bearbeitete Gruppe (null, wenn keine Gruppe bearbeitet wird). |
| `GetActiveSymbolDefinition() -> Handle` | Die gerade bearbeitete Symboldefinition (null, wenn keine bearbeitet wird). |
| `SetActiveSymbolDefinition(hSymbolDefinition: Handle) -> bool` | Setzt die aktive Symboldefinition. Die gerade bearbeitete Symboldefinition (null, wenn keine bearbeitet wird). |

*Ansicht und Seite*

| Methode | Beschreibung |
|---|---|
| `GetPageBounds() -> Math.Rect2D \| None` | Rechteck, das die druckbaren Seiten der Zeichnung abdeckt, in Weltkoordinaten. |

*Benutzernullpunkt*

| Methode | Beschreibung |
|---|---|
| `GetUserOrigin() -> Math.Point2D \| None` | Der Punkt in Weltkoordinaten, der im Benutzerkoordinatensystem bei (0, 0) erscheint. |
| `SetUserOrigin(origin: Math.Point2D) -> bool` | Setzt den Benutzernullpunkt. Der Punkt in Weltkoordinaten, der im Benutzerkoordinatensystem bei (0, 0) erscheint. |
| `GetViewCenter() -> Math.Point2D \| None` | Punkt in der Mitte der aktuellen Ansicht, in Weltkoordinaten. |
| `SetViewCenter(center: Math.Point2D) -> bool` | Setzt den Ansichtsmittelpunkt. Punkt in der Mitte der aktuellen Ansicht, in Weltkoordinaten. |

*Zoomfaktor*

| Methode | Beschreibung |
|---|---|
| `SetZoom(zoomFactor: float) -> bool` | 1.0 = 100 %, 2.0 = 200 % (doppelt so groß auf dem Bildschirm), 0.5 = 50 %. |
| `IsPlanRotated() -> bool \| None` | True, wenn die Plandrehung der Ansicht ungleich null ist. |
| `GetPlanRotationAngle() -> float \| None` | Gibt den Winkel der Plandrehung zurück (Radiant, gegen den Uhrzeigersinn). |
| `Redraw(area: Math.Rect2D) -> bool` | Markiert das Rechteck `area` in Weltkoordinaten zum Neuzeichnen. Rufen Sie die Methode nach Änderungen auf, die nicht von der API selbst vorgenommen wurden. |

*Einheiten*

| Methode | Beschreibung |
|---|---|
| `WorldToUnits(worldLength: float) -> float \| None` | Konvertiert zwischen den von der API verwendeten internen Welteinheiten und den in der Benutzeroberfläche angezeigten primären Dokumenteinheiten. |
| `UnitsToWorld(unitsLength: float) -> float \| None` | Konvertiert `unitsLength` von Dokumenteinheiten in Welteinheiten. Konvertiert zwischen den von der API verwendeten internen Welteinheiten und den in der Benutzeroberfläche angezeigten primären Dokumenteinheiten. |

*Rückgängig*

| Methode | Beschreibung |
|---|---|
| `StartUndoEvent(method: UndoMethod = UndoMethod.SwapObjects, isRevertible: bool = False) -> None` | Öffnet ein Rückgängig-Ereignis und wählt dessen Methode (üblicherweise `UndoMethod.SwapObjects`). Vor jeder Änderung aufrufen. `isRevertible` ermöglicht es `RevertUndoEvent()`, das Ereignis zurückzunehmen (siehe oben). Vectorworks baut das Ereignis dann auch bei ausgeschalteter Rückgängig-Funktion auf (null Rückgängig-Stufen); beim Abschluss wird ein solches Ereignis verworfen. Dies gilt für SwapObjects und ReplaceSelection: `UndoMethod.None_` beginnt kein Ereignis. |
| `NameUndoEvent(name: str) -> None` | Benennt das aktuelle Rückgängig-Ereignis, sodass es im Menü „Bearbeiten“ als „Rückgängig <name>“ erscheint. Innerhalb des Ereignisses vor der Änderung aufrufen. |
| `EndUndoEvent() -> None` | Schließt das aktuelle Rückgängig-Ereignis sofort ab. Vectorworks beendet es auch automatisch, wenn der Vorgang abgeschlossen ist. |
| `RevertUndoEvent() -> bool` | Nimmt das gerade aufgebaute Ereignis zurück: Macht die darin erfassten Änderungen rückgängig und entfernt es aus der Rückgängig-Liste (siehe oben). Rufen Sie die Methode bei einem mit `isRevertible=True` gestarteten Ereignis anstelle von `EndUndoEvent()` auf. Gibt `False` zurück, wenn gerade kein Ereignis aufgebaut wird. Andernfalls wird `True` zurückgegeben, auch wenn das Ereignis nicht zurückgenommen werden konnte (dies ist nicht möglich, wenn es nicht mit `isRevertible=True` gestartet wurde). Tut nichts und gibt `False` zurück, solange die ausführende Anwendung die Rückgängig-Funktion des laufenden Skripts verwaltet. |
| `IsBuildingUndoEvent() -> bool` | Ob gerade ein Rückgängig-Ereignis aufgebaut wird: begonnen, aber noch nicht beendet. Der Wert ist `True` für das mit StartUndoEvent geöffnete Ereignis, aber auch für ein Ereignis, das Vectorworks für den laufenden Befehl oder das laufende Skript geöffnet hat, sowie für ein verborgenes Ereignis, das ein Änderungen für Rückgängig erfassender API-Aufruf begonnen hat, weil kein Ereignis offen war. |
| `AddAfterSwapObject(object: Handle) -> bool` | Objektregistrierung für Rückgängig – nur innerhalb eines `UndoMethod.SwapObjects`-Ereignisses (oder ReplaceSelection) sinnvoll. Registrieren Sie ein gerade ERZEUGTES und zur Zeichnung hinzugefügtes Objekt, damit die Rückgängig-Funktion es wieder entfernt. Übergeben Sie ein Null-Handle, um alle aktuell aktivierten Objekte zu registrieren (z. B. direkt nach DuplicateSelection). |
| `AddBothSwapObject(object: Handle) -> bool` | Registrieren Sie ein Objekt, das Sie GLEICH ÄNDERN MÖCHTEN, damit die Rückgängig-Funktion seinen vorherigen Zustand wiederherstellt; eine Kopie wird im Rückgängig-Datensatz gespeichert. VOR der Änderung aufrufen. Übergeben Sie ein Null-Handle für alle aktuell aktivierten Objekte. |
| `AddBeforeSwapObject(object: Handle) -> bool` | Registrieren Sie ein Objekt, das Sie gleich LÖSCHEN möchten. Veraltet: `Delete()` erfasst die Löschung bereits für Rückgängig, daher wird dies selten benötigt. Übergeben Sie ein Null-Handle für alle aktivierten Objekte. |
| `AddBeforeMoveObject(object: Handle) -> bool` | Registrieren Sie ein Objekt, das Sie mit `PrimitiveObject.MoveToContainer` aus seinem Container (Ebene, Gruppe, Symboldefinition) in einen anderen VERSCHIEBEN, damit die Rückgängig-Funktion es an seine ursprüngliche Stelle zurücksetzt: AddBeforeMoveObject VOR dem Verschieben, AddAfterMoveObject danach, jeweils mit dem Objekt. Die Methoden erfassen die Position des Objekts in der Zeichnung, nicht seinen Zustand. Erfassen Sie für das verschobene Objekt im Ereignis nur dieses Aufrufpaar (die Kombination mit AddBothSwapObject für dasselbe Objekt in einem Ereignis ist keine geprüfte Aufruffolge): Nehmen Sie andere Änderungen am Objekt in einem eigenen Rückgängig-Ereignis vor. Ein neues Objekt, das noch nicht in der Zeichnung ist (zum Beispiel das Ergebnis einer booleschen Operation), wird stattdessen mit MoveToContainer eingefügt und mit AddAfterSwapObject registriert. Übergeben Sie ein Null-Handle für alle aktuell aktivierten Objekte. |
| `AddAfterMoveObject(object: Handle) -> bool` | Registriert `object` unmittelbar nach dem Verschieben in einen anderen Container für Rückgängig. Registrieren Sie ein Objekt, das Sie mit `PrimitiveObject.MoveToContainer` aus seinem Container (Ebene, Gruppe, Symboldefinition) in einen anderen VERSCHIEBEN, damit die Rückgängig-Funktion es an seine ursprüngliche Stelle zurücksetzt: AddBeforeMoveObject VOR dem Verschieben, AddAfterMoveObject danach, jeweils mit dem Objekt. Die Methoden erfassen die Position des Objekts in der Zeichnung, nicht seinen Zustand. Erfassen Sie für das verschobene Objekt im Ereignis nur dieses Aufrufpaar (die Kombination mit AddBothSwapObject für dasselbe Objekt in einem Ereignis ist keine geprüfte Aufruffolge): Nehmen Sie andere Änderungen am Objekt in einem eigenen Rückgängig-Ereignis vor. Ein neues Objekt, das noch nicht in der Zeichnung ist (zum Beispiel das Ergebnis einer booleschen Operation), wird stattdessen mit MoveToContainer eingefügt und mit AddAfterSwapObject registriert. Übergeben Sie ein Null-Handle für alle aktuell aktivierten Objekte. |

## Aufzählungen

### Traverse

> **Vollständiger Name:** `api.Traverse` · **Art:** `IntEnum`

Welche Objektmenge beim Durchlaufen des Dokuments besucht wird. Wird an `Document.ForEachObject` / GetObjects / GetObjectsAtPoint übergeben.

| Element | Wert | Beschreibung |
|---|---|---|
| `Selected` | `0` | Nur aktuell aktivierte Objekte auf der obersten Hierarchiestufe. |
| `Editable` | `1` | Nicht gesperrte Objekte auf sichtbaren, bearbeitbaren Ebenen und in sichtbaren, bearbeitbaren Klassen. |
| `Visible` | `2` | Objekte, die derzeit auf dem Bildschirm dargestellt werden (sichtbare Ebene + sichtbare Klasse). |
| `Drawing` | `3` | Alle Objekte in der Zeichnung (alle Ebenen), ausgenommen Zubehör. |
| `SymbolDefinitions` | `4` | Nur Symboldefinitionen (die wiederverwendbaren Vorlagen im Zubehör-Manager). |
| `SelectedAndEditable` | `5` | Aktivierte, sichtbare und nicht gesperrte Objekte auf bearbeitbaren Ebenen. |
| `All` | `6` | Alle Zeichnungsobjekte sowie Symboldefinitionen und deren Inhalte. |
| `AllAndResources` | `7` | Wie All, zusätzlich Zubehörobjekte (Schraffuren, Farbverläufe, Symboldefinitionen, ...) |

### Descend

> **Vollständiger Name:** `api.Descend` · **Art:** `IntFlag` (Einträge werden mit `|` kombiniert)

Wie tief beim Durchlaufen in Containerobjekte (Gruppen, Symbole, Ansichtsbereiche, ...) abgestiegen wird. Die Werte sind Bitkennzeichen: Kombinieren Sie Einträge mit `|`, um in mehrere Containerarten abzusteigen, zum Beispiel `api.Descend.Groups | api.Descend.Viewports`.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` | Nur Objekte auf der obersten Hierarchiestufe besuchen, in keine Container absteigen. |
| `Groups` | `32` | In Gruppen absteigen. |
| `All` | `64` | In alle Containerarten absteigen (Gruppen, Symbole, Plug-in-Objekte, ...) |
| `Viewports` | `128` | In Ansichtsbereiche absteigen (Ansichtsbereiche auf Layoutebenen). |
| `AuxiliaryLists` | `256` | An besuchte Objekte angehängte Hilfsobjekte einbeziehen. |

### LayerType

> **Vollständiger Name:** `api.LayerType` · **Art:** `IntEnum`

Art einer Ebene.

| Element | Wert | Beschreibung |
|---|---|---|
| `Unknown` | `0` |  |
| `Design` | `1` | Eine Konstruktionsebene in Weltkoordinaten (reguläre Zeichenfläche). |
| `Sheet` | `2` | Eine Layoutebene (eine druckbare Seite, die Ansichtsbereiche enthält). |
| `GuestDesign` | `3` | Eine aus einem anderen Dokument importierte/referenzierte Konstruktionsebene. |

### LayerVisibility

> **Vollständiger Name:** `api.LayerVisibility` · **Art:** `IntEnum`

Sichtbarkeit einer Ebene (wie in der Navigationspalette angezeigt).

| Element | Wert | Beschreibung |
|---|---|---|
| `Invisible` | `-1` | Ausgeblendet. |
| `Normal` | `0` | Normal dargestellt. |
| `Grayed` | `2` | Angezeigt, aber grau dargestellt, um zu kennzeichnen, dass dies nicht die aktive Ebene ist. |

### VisibilityOptions

> **Vollständiger Name:** `api.VisibilityOptions` · **Art:** `IntEnum`

Wie andere als die aktive Ebene oder Klasse dargestellt werden. Wird von `Document.SetLayerOptions` und `Document.SetClassOptions` verwendet.

| Element | Wert | Beschreibung |
|---|---|---|
| `ActiveOnly` | `1` | Nur die aktive Ebene/Klasse anzeigen. |
| `GrayOthers` | `2` | Andere grau anzeigen (nicht bearbeitbar, kein Zeigerfang möglich). |
| `ShowOthers` | `3` | Andere normal anzeigen (sichtbar, aber nicht bearbeitbar, kein Zeigerfang möglich). |
| `ShowSnapOthers` | `4` | Andere normal anzeigen und Zeigerfang an ihnen zulassen (weiterhin nicht bearbeitbar). |
| `ShowSnapModifyOthers` | `5` | Andere normal anzeigen und Zeigerfang sowie Bearbeitung zulassen. |
| `GraySnapOthers` | `6` | Andere grau anzeigen, aber Zeigerfang an ihnen zulassen. |

### StoryElevationChangeMode

> **Vollständiger Name:** `api.StoryElevationChangeMode` · **Art:** `IntEnum`

Welche Geschosse `Story.SetElevation` verschiebt (die Optionen des Dialogfensters „Geschossbasishöhe ändern“). Jedes betroffene Geschoss wird um denselben Abstand verschoben, und seine Konstruktionsebenen werden mitverschoben.

| Element | Wert | Beschreibung |
|---|---|---|
| `Single` | `0` | Nur dieses Geschoss. |
| `CurrentAndAbove` | `1` | Dieses Geschoss und alle darüberliegenden Geschosse. |
| `CurrentAndBelow` | `2` | Dieses Geschoss und alle darunterliegenden Geschosse. |
| `All` | `3` | Alle Geschosse des Dokuments. |

### UndoMethod

> **Vollständiger Name:** `api.UndoMethod` · **Art:** `IntEnum`

Rückgängig-Methode, die an `Document.StartUndoEvent` übergeben wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` | Deaktiviert Rückgängig und leert die Rückgängig-Tabelle für den Vorgang (sparsam verwenden). |
| `ReplaceSelection` | `17` | Merkt sich die aktuelle Aktivierung; die Rückgängig-Funktion stellt sie wieder her. |
| `SwapObjects` | `21` | Rückgängig auf Objektebene: Registrieren Sie die Objekte, die Sie erzeugen / ändern / löschen – die übliche Wahl. |

### AngularUnit

> **Vollständiger Name:** `api.AngularUnit` · **Art:** `IntEnum`

Einheit, in der Winkel angezeigt werden (`UnitSettings.GetAngularUnit`).

| Element | Wert | Beschreibung |
|---|---|---|
| `Degrees` | `0` |  |
| `Radians` | `1` |  |
| `Gradians` | `2` |  |

### TextJustification

> **Vollständiger Name:** `api.TextJustification` · **Art:** `IntEnum`

Horizontale Ausrichtung neuer Texte (`TextDefaults`).

| Element | Wert | Beschreibung |
|---|---|---|
| `Left` | `1` |  |
| `Center` | `2` |  |
| `Right` | `3` |  |

### TextVerticalAlignment

> **Vollständiger Name:** `api.TextVerticalAlignment` · **Art:** `IntEnum`

Vertikale Ausrichtung neuer Texte (`TextDefaults`).

| Element | Wert | Beschreibung |
|---|---|---|
| `TopOfBox` | `1` |  |
| `TopBaseline` | `2` |  |
| `CenterOfBox` | `3` |  |
| `BottomBaseline` | `4` |  |
| `BottomOfBox` | `5` |  |

### TextLineSpacing

> **Vollständiger Name:** `api.TextLineSpacing` · **Art:** `IntEnum`

Zeilenabstand neuer Texte (`TextDefaults`); `Custom` verwendet den Durchschuss von `TextDefaults.GetLeading`.

| Element | Wert | Beschreibung |
|---|---|---|
| `Custom` | `0` | Siehe `TextDefaults.GetLeading`. |
| `Single` | `2` |  |
| `OneAndHalf` | `3` |  |
| `Double` | `4` |  |

---

[Zurück zum Index](README.md) · [Nach oben](#documentaccess--dokument-ebenen-geschosse-und-einstellungen)
