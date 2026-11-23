[English](../../PythonAPI/v2027.2/ObjectsLandmark.md) • **Deutsch** • [日本語](../../PythonAPI.ja/v2027.2/ObjectsLandmark.md)

# ObjectsLandmark — Pflanzen, Geländemodelle, Belag/Weg-Objekte und weitere Landschaftsobjekte

> **Python-Modul:** `api` · **Version:** Vectorworks 2027 Update 2

[Zurück zum Index](README.md)

Die Klassen der Landmark-Plug-in-Objekte. `LandmarkObject` ist ihre gemeinsame Basisklasse (allgemeiner Parameterzugriff). Die konkreten Klassen sind `PlantObject` ("Plant"), `LandscapeAreaObject` ("Landscape Area"), `SiteModelObject` ("DTM6", ein Geländemodell mit Oberflächen für den Ist- und Soll-Zustand), `SiteModifierObject` ("Site Modifiers"), `StakeObject` ("Stake Object"), `HardscapeObject` ("Hardscape"), `PropertyLineObject` ("Property Line") und `ExistingTreeObject` ("Existing Tree").

Alle Landmark-Objekte sind Plug-in-Objekte, die anhand des universellen Namens ihrer Datenbank unterschieden werden. `Is(h)` prüft diesen Namen, `Create(...)` erzeugt eine neue Instanz auf der aktiven Ebene / im aktuellen Container, Lesemethoden geben bei einem ungültigen Objekt oder einem fehlenden Parameter `None` zurück und Schreibmethoden bei Erfolg `True`.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Klassen](#klassen)
  - [LandmarkObject](#landmarkobject)
  - [PlantObject](#plantobject)
    - [PlantObject.Config](#plantobjectconfig)
    - [PlantObject.TagDisplay](#plantobjecttagdisplay)
  - [LandscapeAreaObject](#landscapeareaobject)
    - [LandscapeAreaObject.PlantDisplay2D](#landscapeareaobjectplantdisplay2d)
    - [LandscapeAreaObject.DrawingMode](#landscapeareaobjectdrawingmode)
    - [LandscapeAreaObject.AreaUnits](#landscapeareaobjectareaunits)
  - [SiteModelObject](#sitemodelobject)
    - [SiteModelObject.Display2D](#sitemodelobjectdisplay2d)
    - [SiteModelObject.Display3D](#sitemodelobjectdisplay3d)
  - [SiteModifierObject](#sitemodifierobject)
    - [SiteModifierObject.Config](#sitemodifierobjectconfig)
    - [SiteModifierObject.ApplyTo](#sitemodifierobjectapplyto)
  - [StakeObject](#stakeobject)
    - [StakeObject.Mode](#stakeobjectmode)
    - [StakeObject.SiteModel](#stakeobjectsitemodel)
  - [HardscapeObject](#hardscapeobject)
    - [HardscapeObject.Mode3D](#hardscapeobjectmode3d)
  - [PropertyLineObject](#propertylineobject)
    - [PropertyLineObject.AreaUnits](#propertylineobjectareaunits)
  - [ExistingTreeObject](#existingtreeobject)
    - [ExistingTreeObject.Origin](#existingtreeobjectorigin)
    - [ExistingTreeObject.TreeProtection](#existingtreeobjecttreeprotection)
    - [ExistingTreeObject.Condition](#existingtreeobjectcondition)
    - [ExistingTreeObject.SULE](#existingtreeobjectsule)
    - [ExistingTreeObject.Significance](#existingtreeobjectsignificance)
    - [ExistingTreeObject.Action](#existingtreeobjectaction)

## Überblick

| Name | Art | Erbt von | Zusammenfassung |
|---|---|---|---|
| [`LandmarkObject`](#landmarkobject) | Klasse | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Gemeinsame Basisklasse der Landmark-Plug-in-Objektklassen (Pflanze, Flächenpflanzung, Geländemodell, Geländemodifikator, Vermessungspunkt, Belag/Weg, Grenzlinie, Kataster-Baum). |
| [`PlantObject`](#plantobject) | Klasse | [`LandmarkObject`](#landmarkobject) | Plug-in-Objekt Pflanze (universeller Name "Plant") aus dem Landmark-Plug-in. |
| [`PlantObject.Config`](#plantobjectconfig) | IntEnum (verschachtelt) |  | Konfiguration und Darstellung |
| [`PlantObject.TagDisplay`](#plantobjecttagdisplay) | IntEnum (verschachtelt) |  | Wo die Pflanzenbeschriftung angezeigt wird. |
| [`LandscapeAreaObject`](#landscapeareaobject) | Klasse | [`LandmarkObject`](#landmarkobject) | Plug-in-Objekt Flächenpflanzung (universeller Name "Landscape Area") aus dem Plug-in Landmark. |
| [`LandscapeAreaObject.PlantDisplay2D`](#landscapeareaobjectplantdisplay2d) | IntEnum (verschachtelt) |  | Wie die Pflanzen einer Flächenpflanzung in 2D dargestellt werden. |
| [`LandscapeAreaObject.DrawingMode`](#landscapeareaobjectdrawingmode) | IntEnum (verschachtelt) |  | Ob das Objekt als Flächenpflanzung oder als Hecke gezeichnet wird. |
| [`LandscapeAreaObject.AreaUnits`](#landscapeareaobjectareaunits) | IntEnum (verschachtelt) |  | Einheiten, in denen die Fläche einer Flächenpflanzung angezeigt wird. |
| [`SiteModelObject`](#sitemodelobject) | Klasse | [`LandmarkObject`](#landmarkobject) | Plug-in-Objekt Geländemodell (universeller Name "DTM6") aus dem Plug-in Landmark. |
| [`SiteModelObject.Display2D`](#sitemodelobjectdisplay2d) | IntEnum (verschachtelt) |  | Auswahl der 2D- / 3D-Darstellung |
| [`SiteModelObject.Display3D`](#sitemodelobjectdisplay3d) | IntEnum (verschachtelt) |  | Was die 3D-Darstellung eines Geländemodells zeigt. |
| [`SiteModifierObject`](#sitemodifierobject) | Klasse | [`LandmarkObject`](#landmarkobject) | Plug-in-Objekt Geländemodifikator (universeller Name "Site Modifiers") aus dem Plug-in Landmark. |
| [`SiteModifierObject.Config`](#sitemodifierobjectconfig) | IntEnum (verschachtelt) |  | Umformungsmethode eines Geländemodifikators ("Config"). |
| [`SiteModifierObject.ApplyTo`](#sitemodifierobjectapplyto) | IntEnum (verschachtelt) |  | Auf welche Oberfläche des Geländemodells ein Geländemodifikator angewendet wird. |
| [`StakeObject`](#stakeobject) | Klasse | [`LandmarkObject`](#landmarkobject) | Plug-in-Objekt Vermessungspunkt (universeller Name "Stake Object") aus dem Plug-in Landmark. |
| [`StakeObject.Mode`](#stakeobjectmode) | IntEnum (verschachtelt) |  | Funktion des Vermessungspunkts in Bezug auf das Geländemodell. |
| [`StakeObject.SiteModel`](#stakeobjectsitemodel) | IntEnum (verschachtelt) |  | Auf welche Oberfläche des Geländemodells sich ein Vermessungspunkt bezieht. |
| [`HardscapeObject`](#hardscapeobject) | Klasse | [`LandmarkObject`](#landmarkobject) | Plug-in-Objekt Belag/Weg (universeller Name "Hardscape") aus dem Plug-in Landmark. |
| [`HardscapeObject.Mode3D`](#hardscapeobjectmode3d) | IntEnum (verschachtelt) |  | 3D-Modus des Belag/Weg-Objekts. |
| [`PropertyLineObject`](#propertylineobject) | Klasse | [`LandmarkObject`](#landmarkobject) | Plug-in-Objekt Grenzlinie (universeller Name "Property Line") aus dem Plug-in Landmark. |
| [`PropertyLineObject.AreaUnits`](#propertylineobjectareaunits) | IntEnum (verschachtelt) |  | Flächeneinheiten, die sowohl von "Area Units Imperial" als auch von "Area Units Metric" unterstützt werden. |
| [`ExistingTreeObject`](#existingtreeobject) | Klasse | [`LandmarkObject`](#landmarkobject) | Plug-in-Objekt Baumkataster (universeller Name "Existing Tree") aus dem Plug-in Landmark. |
| [`ExistingTreeObject.Origin`](#existingtreeobjectorigin) | IntEnum (verschachtelt) |  | Herkunft der Art eines Kataster-Baums. |
| [`ExistingTreeObject.TreeProtection`](#existingtreeobjecttreeprotection) | IntEnum (verschachtelt) |  | Darstellung des Baumschutzbereichs |
| [`ExistingTreeObject.Condition`](#existingtreeobjectcondition) | IntEnum (verschachtelt) |  | Baumpflegerische Beurteilung |
| [`ExistingTreeObject.SULE`](#existingtreeobjectsule) | IntEnum (verschachtelt) |  | Voraussichtliche sichere Reststandzeit |
| [`ExistingTreeObject.Significance`](#existingtreeobjectsignificance) | IntEnum (verschachtelt) |  | Bewertung der Bedeutung eines Kataster-Baums. |
| [`ExistingTreeObject.Action`](#existingtreeobjectaction) | IntEnum (verschachtelt) |  | Vorgeschlagene Maßnahme für einen Kataster-Baum. |

## Klassen

### LandmarkObject

> **Vollständiger Name:** `api.LandmarkObject` · **Erbt von:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Gemeinsame Basisklasse der Landmark-Plug-in-Objektklassen (Pflanze, Flächenpflanzung, Geländemodell, Geländemodifikator, Vermessungspunkt, Belag/Weg, Grenzlinie, Kataster-Baum).

Ein Landmark-Objekt ist ein Vectorworks-Plug-in-Objekt (eine Instanz eines Plug-ins, das vom Modul Landschaft / Vectorworks Landmark registriert wird; in der API auch parametrisches Objekt genannt). Jedes Landmark-Objekt wird durch seinen universellen (parametrischen) Namen identifiziert, z. B. "Plant", "Hardscape", "Existing Tree". Die nachfolgenden Klassen prüfen den universellen Namen in ihrer statischen Methode `Is()`, um die Plug-in-Arten zu unterscheiden.

Die Klasse erbt von PrimitiveObject, sodass alle allgemeinen Zugriffsmethoden verfügbar sind (Identität, Klasse, Attribute, Hierarchie, Begrenzungen, Verschieben/Drehen/Skalieren/Spiegeln, Löschen, ...). Zusätzlich bietet diese Klasse einen einheitlichen Zugriff über Zeichenfolgeschlüssel auf die Felder der Parameterdatenbank des Objekts. Die einzelnen Unterklassen ergänzen benannte Lese-/Schreibmethoden für die wichtigsten Felder jedes Plug-ins.

Von PrimitiveObject übernommene Konventionen:

- Lesemethoden geben bei einem ungültigen Objekt oder fehlenden Parameter `None` zurück.
- Schreibmethoden geben bei Erfolg `True` und bei einem ungültigen Objekt oder fehlenden Parameter `False` zurück.
- Längen werden in Welteinheiten angegeben, Winkel im Bogenmaß; Zeichenfolgen sind UTF-8-kodiert.

Grundlagen des Parameterzugriffs (Get/SetParam*):

- Jedes Landmark-Objekt speichert seine Daten in einer Datenbank mit benannten Feldern („Parametern“). Jede Unterklasse führt alle verfügbaren Parameternamen in ihrer „Vollständigen Parameterreferenz“ auf. Verwenden Sie diese Namen unverändert (Groß-/Kleinschreibung beachten, UTF-8) mit GetParamString / SetParamString / GetParamReal / ..., um Felder zu lesen oder zu schreiben, für die die Unterklasse keine eigene typisierte Zugriffsmethode anbietet.
- Für Parametertypen werden in den Tabellen folgende Kennzeichnungen verwendet:

- Zeichenfolge — Text (UTF-8) - GetParamString / SetParamString
- int — 32-Bit-Ganzzahl - GetParamInt / SetParamInt
- bool — boolescher Wert - GetParamBool / SetParamBool
- reell — Gleitkommawert (Weltkoordinate, Winkel in Grad, Fläche, Volumen, einfache Zahl, ...) - GetParamReal / SetParamReal
- Auswahlliste — Auswahl einer Zeichenkette aus N Möglichkeiten - GetParamString / SetParamString; gültige Werte stehen neben dem Parameter

- Wenn eine Lesemethode `None` oder eine Schreibmethode `False` zurückgibt, ist entweder das Objekt ungültig oder der Parametername existiert bei diesem Objekt nicht. Verwenden Sie `HasParam()`, um dies vorab zu prüfen.
- Parameternamen, die mit einem doppelten Unterstrich ("__") beginnen, gehören zum privaten Zustand des Plug-ins; sie sind lesbar, direkte Änderungen sind jedoch in der Regel nicht sinnvoll.
- Als „nur lesbar“ oder „berechnet“ gekennzeichnete Parameter werden vom Plug-in bei der Neuberechnung aktualisiert; das Schreiben dieser Werte hat normalerweise keine dauerhafte Wirkung.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `LandmarkObject(h: Handle)` | Verweist auf ein beliebiges Objekt `h` als generisches `LandmarkObject`; `IsValid()` prüft nur, ob das Handle nicht null ist. Prüfen Sie die Objektart mit `GetParametricName()` oder mit `Is(h)` einer konkreten Klasse. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `GetParametricName() -> str \| None` | Universeller (parametrischer) Name dieses Objekts, z. B. "Plant" oder "Hardscape". Leer, wenn das Objekt ungültig ist oder das zugrunde liegende Handle kein Plug-in-Objekt bezeichnet. |
| `HasParam(univParamName: str) -> bool` | Ob dieses Plug-in-Objekt ein Feld mit dem angegebenen universellen Namen hat. |
| `GetParamNames() -> list[str]` | Geordnete Liste aller vom Plug-in dieses Objekts definierten universellen Parameternamen. |
| `GetParamType(univParamName: str) -> RecordFieldType \| None` | Datentyp des Parameters; `None`, wenn der Parameter nicht existiert. |
| `GetParamString(univParamName: str) -> str \| None` | Allgemeine Feldzugriffsmethoden mit Zeichenfolgen als Schlüsseln. Bevorzugen Sie die typisierten, benannten Zugriffsmethoden der Unterklassen, sofern vorhanden; verwenden Sie diese Methoden für Parameter ohne eigene Zugriffsmethode. Die Abfragemethoden geben `None` zurück, wenn der Parameter nicht vorhanden ist; die Änderungsmethoden geben `False` zurück. |
| `SetParamString(univParamName: str, value: str) -> bool` | Legt den Parameterwert als Zeichenfolge fest. Allgemeine Feldzugriffsmethoden mit Zeichenfolgen als Schlüsseln. Bevorzugen Sie die typisierten, benannten Zugriffsmethoden der Unterklassen, sofern vorhanden; verwenden Sie diese Methoden für Parameter ohne eigene Zugriffsmethode. Die Abfragemethoden geben `None` zurück, wenn der Parameter nicht vorhanden ist; die Änderungsmethoden geben `False` zurück. |
| `GetParamReal(univParamName: str) -> float \| None` | Gibt den Parameterwert vom Typ real für `univParamName` zurück. |
| `SetParamReal(univParamName: str, value: float) -> bool` | Setzt den Parameterwert vom Typ real. |
| `GetParamBool(univParamName: str) -> bool \| None` | Ob *Boolescher Parameter* für `univParamName` aktiviert ist. |
| `SetParamBool(univParamName: str, value: bool) -> bool` | Setzt den booleschen Parameterwert. |
| `GetParamInt(univParamName: str) -> int \| None` | Gibt den ganzzahligen Parameterwert für `univParamName` zurück. |
| `SetParamInt(univParamName: str, value: int) -> bool` | Setzt den ganzzahligen Parameterwert. |
| `GetPathObject() -> Handle` | Pfadobjekt eines pfadbasierten Plug-in-Objekts (Belag/Weg, Flächenpflanzung, Geländemodifikator, Grenzlinie, ...). Gibt bei punktbasierten Plug-in-Objekten (einzelne Pflanze, Kataster-Baum, Vermessungspunkt) und bei einem ungültigen Objekt null zurück. |

Geerbt: alle Elemente von [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### PlantObject

> **Vollständiger Name:** `api.PlantObject` · **Erbt von:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Pflanze (universeller Name "Plant") aus dem Landmark-Plug-in.

Eine Pflanze ist entweder eine einzelne, an einer Position platzierte Instanz oder ein polygonbasierter Container, der mehrere Instanzen derselben Art verteilt (einzelne Pflanze, Pflanzen an Polygoneckpunkten, Pflanzen entlang von Polygonkanten, Pflanzen in einem Rechteck- oder Dreiecksraster). Die Konfiguration wird über den Parameter "config" gesteuert.

Häufig verwendete Parameter mit benannten Zugriffsmethoden:

- "plant ID" — Zubehörname des Pflanzensymbols / -stils
- "spread" — Durchmesser der Pflanzenkrone in Welteinheiten
- "height" — Höhe der Pflanze in Welteinheiten
- "latin name" — botanischer (lateinischer) Name
- "common name" — Trivialname
- "PlantDescription" — Kurzbeschreibung
- "comments" — frei formulierbare Kommentare
- "tag display" — None / Links / Rechts / Frei (Platzierung der Beschriftung relativ zur Pflanze)
- "config" — Einzelne Pflanze / Pflanzen an Polygoneckpunkten / Pflanzen entlang von Polygonkanten / ... (siehe PlantObject)
- "Show 3D Detail" — ob 3D-Geometrie dargestellt wird

Verwenden Sie für alle anderen Felder die allgemeinen Zugriffsmethoden von LandmarkObject (GetParamString / GetParamReal / ...).

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten) Typen: Zeichenfolge (Text/StaticText), reell (reelle Zahl/CoordDisp/CoordLocX/CoordLocY/Winkel/Fläche/Volumen), int (LongInt), bool (boolesch), Auswahlliste (Zeichenfolge, eine der aufgeführten Auswahlmöglichkeiten). Art / Identität

- "plant ID" — Zeichenfolge — Name des Symbols / Stils (identifiziert die Art)
- "PlantDescription" — Zeichenfolge — verständliche Beschreibung, die in der Infopalette angezeigt wird
- "latin name" — Zeichenfolge — botanischer Name
- "common name" — Zeichenfolge — Trivialname
- "comments" — Zeichenfolge — frei formulierbare Kommentare
- "custom ID" — Zeichenfolge
- "isCustom" — bool — `True` für benutzerdefinierte Pflanzen (nicht aus der Pflanzendatenbank)
- "onPlantList" — bool — in die Pflanzenliste aufnehmen
- "Category" — Auswahlliste — Kategorie (z. B. `None` / Bäume / Sträucher / ...)
- "Tag Schema" — Zeichenfolge — Schema für den Haupttext der Beschriftung
- "TagSchemaCenter" — Zeichenfolge — mittlerer Beschriftungstext
- "TagSchemaBottom" — Zeichenfolge — unterer Beschriftungstext
- "SKU" — Zeichenfolge
- "Price" — reell
- "HiddenName" — Zeichenfolge

Größe (Welteinheiten)

- "spread" — reell — Kronendurchmesser
- "height" — reell — Gesamthöhe
- "spacing" — reell — Abstand zwischen Instanzen (bei polygonbasierten Konfigurationen)
- "image size" — reell
- "Row spacing" — reell — Abstand zwischen den Reihen in Rastermodi
- "Rate" — reell — Pflanzen pro Einheit (siehe "Rate mode")
- "Percentage" — int — Prozentanteil für die Verteilungsmodi
- "Plants per row" — int
- "Plants per column" — int
- "Plant height scale" — Auswahlliste — Fixed / randAt5 / randAt10 / randAt15

Konfiguration und Darstellung

- "config" — Auswahlliste — Single plant / Plants at poly vertices / Plants along poly edges / Plants in rectangular array / Plants in triangular array
- "plant style" — Auswahlliste — No sketch / No sketch w/ shadows / Light sketch / Light sketch w/ shadows / Medium sketch / Medium sketch w/ shadows / Heavy sketch / Heavy sketch w/ shadows / Cloud / Cloud w/ shadows
- "tag display" — Auswahlliste — None / Left / Right / Floating
- "poly display" — Auswahlliste — None / Centers-Solid / Centers-Dashed / Boundary-Solid / Boundary-Dashed / Gapped-Solid / Gapped-Dashed
- "tickmark display" — Auswahlliste — None / Cross / Dot / XMark
- "tickmark size" — reell — Größe der Markierung in Welteinheiten
- "rotate mode" — Auswahlliste — FALSE / AlongLine / TRUE
- "quantity measure" — Auswahlliste — Count / Dripline area / Boundary area
- "Outline" — Auswahlliste — No Outline / Tight Outline / One Outline / Two Outlines / Three Outlines
- "TagBubble" — Auswahlliste — None / Circle / Circle (Quantity only) / Hexagon / Hexagon (Quantity only) / Rectangle / Round
- "TagApproachAngle" — reell — Grad
- "TagShoulderAngle" — reell — Grad
- "TagEnableShoulder" — bool
- "TagUseMarker" — bool
- "TagSnapCenters" — bool
- "display style" — bool
- "Show 3D Detail" — bool
- "ShowSettings" — bool
- "backGroundOnly" — bool
- "massPlants" — bool
- "Replace" — bool
- "drip cloud factor" — reell
- "drip sketch factor" — Auswahlliste — "1-Am wenigsten skizzenhaft" ... "9-Am stärksten skizzenhaft"
- "tagClass" — Auswahlliste — Klassenname für die Pflanzenbeschriftung
- "tickClass" — Auswahlliste — Klassenname für die Markierungen
- "PolylineDisplayClass" — Auswahlliste — Klasse für die Polyliniendarstellung
- "MassOutlineClass" — Auswahlliste — Klasse für den Umriss der Pflanzengruppe

Schatten und Erscheinungsbild

- "ShadowEnable" — bool
- "ShadowAngle" — reell — Grad
- "ShadowOffset" — reell — Welteinheiten
- "ShadowFillStyle" — Zeichenfolge
- "FillStyle" — Zeichenfolge
- "PenStyle" — Zeichenfolge
- "FillStyleParam", "FillSolidColor", "FillPattern", "FillHatch", "FillGrad", "FillImage"
- "FillForeColor", "FillBackColor" — int (Farbindizes)
- "PenStyleParam", "PenSolidColor", "PenForeColor", "PenBackColor" — int (Farbindizes)
- "PenWeight", "PenDash", "PenPattern" — int
- "SymbolFPat", "SymbolFFore", "SymbolFBack" — int
- "UseDocumentShadow" — bool

Hecken- / Verteilungsoptionen

- "Hedge" — bool — Heckenmodus aktivieren
- "Hedge rows" — int
- "HedgeMode" — Auswahlliste
- "HedgeModeNew" — Auswahlliste — Rectangular / StaggeredRow / TripleStaggeredRow
- "HedgeRowSpacingMode" — Auswahlliste — SameAsPlantSpacingOrRate / Fixed
- "HedgeRowSpacing" — reell — Welteinheiten
- "OffsetFromPath" — reell — Welteinheiten
- "OffsetRows" — bool
- "XOffset", "YOffset" — reell — Welteinheiten
- "Plant spacing mode" — Auswahlliste — Custom spacing / Distrib by Rate / Distrib by Coverage
- "Spacing mode" — Auswahlliste — Same as Plant Spread / Fixed / Best Fit / Count
- "Row spacing mode" — Auswahlliste — Same as spacing / ...
- "Rate mode" — Auswahlliste — Plants per unit / Unit on center / Plants per Linear Unit / Plants per Linear Unit Best Fit

3D-Geometrie (prozedural erzeugter Baum)

- "3DGeometryCanopyShape" — int
- "3DGeometryCanopyHgt" — reell — Welteinheiten
- "gen_generated" — bool
- "gen_canopyShape" — Zeichenfolge
- "gen_firstBranchHeight" — reell — Welteinheiten
- "gen_isFirstBranchHeightDefault" — bool
- "gen_trunkGirth" — reell — Welteinheiten
- "gen_canopyClass" — Auswahlliste — Klassenname
- "gen_trunkClass" — Auswahlliste — Klassenname
- "scraped_url" — Zeichenfolge

Wurzelbereiche (Welteinheiten, sofern nicht anders angegeben)

- "classRootZones" — Auswahlliste — Klassenname
- "classRootExcavation" — Auswahlliste — Klassenname
- "showRootBall" — Auswahlliste — None / 2D Only / 3D Only / 2D and 3D
- "shapeRootBall" — Auswahlliste — Sphere / B & B (Ball & Burlap; auf Deutsch: Ballentuch & Drahtkorb)
- "sizeRootBall1", "sizeRootBall2", "sizeRootBall3" — reell
- "attrByClassRootBall" — bool
- "lineWeightRootBall" — int
- "lineColorRootBall" — int — Farbindex
- "showPlantingExcav" — Auswahlliste — None / 2D Only / 3D Only / 2D and 3D
- "diamPlantingExcav" — Auswahlliste — 1.5x the root ball / 2x the root ball / 3x the root ball / Custom
- "depthPlantingExcav" — Auswahlliste — 1x the root ball / Custom
- "shapePlantingExcav" — Auswahlliste — Round / Rectangular
- "diamValueExcav", "depthValueExcav" — reell
- "attrByClassPlantingExcav" — bool
- "lineWeightPlantingExcav" — int
- "lineColorPlantingExcav" — int — Farbindex
- "rootBallArea", "rootBallVolume" — reell (nur lesbar, berechnet)
- "plantingExcArea", "plantingExcVolume" — reell (nur lesbar, berechnet)

Pflege / Wasser

- "MaintenanceNotes" — Zeichenfolge
- "PropagationNotes" — Zeichenfolge
- "FireResilience", "FireRisk" — Auswahlliste
- "IrrigationType" — Auswahlliste
- "PointEmitterValue" — Auswahlliste
- "PointEmitterQuantity" — int
- "PeakWaterRequirement" — reell
- "PeakWaterRequirementUnits" — Auswahlliste — InchesWeek / InchesMonth / LiterMinute / LiterHour / MillimeterWeek / MillimeterMonth
- "IrrigationFrequency" — int
- "IrrigationFrequencyUnits" — Auswahlliste — PerDay / PerWeek / PerTwoWeeks / PerMonth
- "ActiveRegion" — Auswahlliste

Zusammenwirken mit dem Geländemodell

- "siteModelLayer" — Auswahlliste — Ebenenname des Geländemodells
- "__notSingleAutoDTM" — bool

Laubwerk-3D-Geometrie (optional)

- "lw_Key", "lw_PlantFile", "lw_Variant" — Zeichenfolge
- "lw_GlobalSeason" — bool
- "lw_Season" — Zeichenfolge
- "lw_Global2D3DMat" — bool
- "lw_2DReprs", "lw_3DReprs" — Zeichenfolge
- "lw_MaterialStyle" — Zeichenfolge

Verschiedenes / nur lesbar

- "DripArea" — reell (nur lesbar, berechnet)
- "TotalCanopyArea" — reell (nur lesbar, berechnet)
- "Version" — int — Schemaversion des Plug-ins
- "sustainability" — Zeichenfolge — JSON-Datenblock mit Nachhaltigkeitsdaten
- "GroupAllocation" — Zeichenfolge
- "SourcePlantList" — Zeichenfolge
- "Factor" — reell
- "Message" — Zeichenfolge — Status-/Warnmeldung in der Infopalette
- "__ScheduledSize" — Zeichenfolge
- "__Status" — int
- "__fade enabled", "__fade percent" — bool / int
- "ControlPoint01X..ControlPoint04Y" — reell (Weltkoordinaten der Kontrollpunkte des Objekts)

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `PlantObject(h: Handle)` | Verweist auf die vorhandene Pflanze `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D, plantResourceName: str = '') -> PlantObject` *statisch* | Erzeugt eine einzelne Pflanzeninstanz an `position` auf der aktiven Ebene / im aktuellen Container. `plantResourceName` ist der Name des zu verwendenden Pflanzenstils (einer Symboldefinition mit einer Musterpflanze). Er wird aus den Vectorworks-Pflanzenbibliotheken importiert, wenn er noch nicht in der Zeichnung vorhanden ist. Wenn der Name leer ist oder der benannte Stil nirgends gefunden wird, wird der erste verfügbare Pflanzenstil verwendet. Gibt ein ungültiges Objekt zurück, wenn überhaupt kein Pflanzenstil verfügbar ist, da eine Pflanze ohne Stil keine darstellbare Grafik besitzt. |
| `CreateFromPath(hPath: Handle, plantResourceName: str = '') -> PlantObject` *statisch* | Erzeugt eine polygonbasierte Pflanze, die Instanzen entlang eines vorhandenen 2D-Pfadobjekts oder über dessen Fläche verteilt. Setzen Sie anschließend den Parameter "config", um den Verteilungsmodus auszuwählen. |
| `EnsurePlantStyle(styleName: str = '') -> str` *statisch* | Stellt sicher, dass ein Pflanzenstil in der aktuellen Zeichnung verfügbar ist, importiert ihn bei Bedarf aus den Vectorworks-Pflanzenbibliotheken und gibt seinen Namen zurück (leer, wenn kein Pflanzenstil bereitgestellt werden konnte). |
| `Duplicate() -> PlantObject` | Dupliziert die Pflanze in der Zeichnung und gibt die Kopie zurück. |

*Pflanzenstil*

| Methode | Beschreibung |
|---|---|
| `GetPlantStyle() -> str \| None` | Die Symboldefinition, aus der die Pflanze ihre Grafik und Standarddaten übernimmt. Dies ist derselbe Wert wie der Parameter "PlantDescription", über den die Pflanze mit ihrem Stil verknüpft ist. |
| `SetPlantStyle(styleName: str) -> bool` | Importiert `styleName` bei Bedarf, wendet alle Einstellungen dieses Stils auf diese Pflanze an und berechnet sie neu. |

*Identität / Art*

| Methode | Beschreibung |
|---|---|
| `GetPlantID() -> str \| None` | Gibt die Pflanzen-ID zurück (Zubehörname des Pflanzensymbols / -stils). |
| `SetPlantID(value: str) -> bool` | Setzt die Pflanzen-ID. |
| `GetLatinName() -> str \| None` | Gibt den lateinischen Namen zurück. |
| `SetLatinName(value: str) -> bool` | Setzt den lateinischen Namen. |
| `GetCommonName() -> str \| None` | Gibt den Trivialnamen zurück. |
| `SetCommonName(value: str) -> bool` | Setzt den Trivialnamen. |
| `GetPlantDescription() -> str \| None` | Name der Pflanzenstil-Symboldefinition; bevorzugen Sie SetPlantStyle, das den Stil auch importiert und seine Einstellungen übernimmt. Wird ein Name gesetzt, der nicht in der Zeichnung vorhanden ist, bleibt die Pflanze ohne Grafik. |
| `SetPlantDescription(value: str) -> bool` | Setzt die Pflanzenbeschreibung. Name der Pflanzenstil-Symboldefinition; bevorzugen Sie SetPlantStyle, das den Stil auch importiert und seine Einstellungen übernimmt. Wird ein Name gesetzt, der nicht in der Zeichnung vorhanden ist, bleibt die Pflanze ohne Grafik. |
| `GetComments() -> str \| None` | Gibt die Kommentare zurück. |
| `SetComments(value: str) -> bool` | Setzt die Kommentare. |
| `GetSpread() -> float \| None` | Größe (Welteinheiten) (Kronendurchmesser). |
| `SetSpread(value: float) -> bool` | Setzt den Kronendurchmesser (Größe in Welteinheiten). |
| `GetHeight() -> float \| None` | Gibt die Höhe zurück (Pflanzenhöhe). |
| `SetHeight(value: float) -> bool` | Setzt die Höhe. |
| `GetConfig() -> PlantObject.Config \| None` | Gibt die Konfiguration zurück. |
| `SetConfig(value: PlantObject.Config) -> bool` | Setzt die Konfiguration. |
| `GetTagDisplay() -> PlantObject.TagDisplay \| None` | Gibt die Beschriftungsdarstellung zurück. |
| `SetTagDisplay(value: PlantObject.TagDisplay) -> bool` | Setzt die Beschriftungsdarstellung. |
| `GetShow3DDetail() -> bool \| None` | Ob *3D-Details anzeigen* eingeschaltet ist. |
| `SetShow3DDetail(value: bool) -> bool` | Schaltet *3D-Details anzeigen* ein oder aus. |
| `GetSpacing() -> float \| None` | Abstand zwischen Pflanzen entlang einer Polygonkante oder in einer Rasteranordnung. |
| `SetSpacing(value: float) -> bool` | Setzt den Abstand. Abstand zwischen Pflanzen entlang einer Polygonkante oder in einer Rasteranordnung. |

Geerbt: alle Elemente von [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### PlantObject.Config

> **Vollständiger Name:** `api.PlantObject.Config` · **Art:** `IntEnum`

Konfiguration und Darstellung

| Element | Wert | Beschreibung |
|---|---|---|
| `SinglePlant` | `0` |  |
| `PlantsAtPolyVertices` | `1` |  |
| `PlantsAlongPolyEdges` | `2` |  |
| `PlantsInRectangularArray` | `3` |  |
| `PlantsInTriangularArray` | `4` |  |

#### PlantObject.TagDisplay

> **Vollständiger Name:** `api.PlantObject.TagDisplay` · **Art:** `IntEnum`

Wo die Pflanzenbeschriftung angezeigt wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` |  |
| `Left` | `1` |  |
| `Right` | `2` |  |
| `Floating` | `3` |  |

### LandscapeAreaObject

> **Vollständiger Name:** `api.LandscapeAreaObject` · **Erbt von:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Flächenpflanzung (universeller Name "Landscape Area") aus dem Plug-in Landmark.

Eine Flächenpflanzung ist ein pfadbasierter Container, der einen polygonalen 2D-Bereich mit einer oder mehreren, nach Prozentanteilen verteilten Pflanzenarten füllt. Sie berechnet die projizierte Fläche / Oberfläche und die insgesamt benötigte Pflanzenanzahl.

Die Pflanzenliste selbst (Art, Prozentanteil, Pflanzdichte) wird als indizierte Sammlung gespeichert, die das Plug-in verwaltet; verwenden Sie die allgemeinen Zugriffsmethoden von LandmarkObject, um einzelne Pflanzeneinträge zu lesen/schreiben.

Häufig verwendete Parameter mit benannten Zugriffsmethoden:

- "name" — für den Benutzer sichtbarer Name der Flächenpflanzung / Pflanzfläche
- "ID" — Kennzeichnung
- "Description" — Kurzbeschreibung
- "area" — berechnete Fläche (nur lesbar)
- "projectedArea" — projizierte Fläche auf dem Geländemodell (nur lesbar)
- "numPlants" — gesamte Pflanzenanzahl (nur lesbar)
- "Drawing Mode" — "Landscape Area" (Flächenpflanzung) oder "Hedgerow" (Hecke)
- "areaUnits" — Einheiten der Flächenanzeige (siehe `LandscapeAreaObject.AreaUnits`)
- "showPlants2D" — Auswahlliste für die 2D-Pflanzendarstellung

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten) Identität / Beschreibung

- "name" — Zeichenfolge — Name der Pflanzfläche / Flächenpflanzung
- "ID" — Zeichenfolge — Kennzeichnung
- "Description" — Zeichenfolge
- "Style Name Formula" — Zeichenfolge — Formel zum Erzeugen des Pflanzenstilnamens
- "Category" — Auswahlliste — z. B. „Stauden“
- "InstanceName" — Zeichenfolge — Instanzname (für Auswertungen)
- "CustomCombName", "CustomCombFormula" — Zeichenfolge
- "Drawing Mode" — Auswahlliste — "Landscape Area" / "Hedgerow"

Messwerte (nur lesbar, bei der Neuberechnung erneut ermittelt)

- "area" — reell
- "projectedArea" — reell
- "ProjectedAreaInLAUnits" — reell
- "SurfaceAreaInLAUnits" — reell
- "AreaLAUnits" — Zeichenfolge
- "areaUnits" — Auswahlliste — Square Feet / Square Meters / Acres / Hectares / Document Units
- "Hedgerow Length" — reell
- "numPlants" — int — Gesamtanzahl der verteilten Pflanzen
- "numAttachedPlants" — int
- "Area Vertex Count" — Zeichenfolge — nur lesbare, formatierte Anzahl
- "unitPrice" — reell
- "priceCode" — Zeichenfolge
- "AreaFactor" — reell — Multiplikator für die Flächenberechnung

2D-Grafik

- "borderStyle" — Auswahlliste — "Standard" / "None"
- "billowSize" — Auswahlliste — X Small / Small / Medium / Large / X Large
- "billowVar" — Auswahlliste — None / Low / Medium / High
- "billowHeight" — Auswahlliste — Small / Medium / Large
- "billowType" — Auswahlliste — Convex / Concave
- "segLength" — Auswahlliste — X Short / Short / Normal / Long / X Long
- "segThickness" — Auswahlliste — X Thin / Thin / Normal / Thick / X Thick
- "Smooth external corners" — bool
- "showPlants2D" — Auswahlliste — None / PlantCloud / PlantLine / PlantSymbols (oder FALSE)
- "showPlants3D" — Auswahlliste — None / Plant Block / Individual Plants
- "diameterScalePopup" — Auswahlliste — Fixed / Random 5% / Random 10% / Random 15%
- "diameterVisualScale" — reell — Prozent
- "heightScalePopup" — Auswahlliste — Fixed / Random 5% / Random 10% / Random 15%
- "heightVisualScale" — reell — Prozent
- "randomizePlantRotation" — bool
- "randomizePlantPosition" — bool
- "allPlantEdgesInsideArea" — bool
- "plantBlockHeight" — reell — Welteinheiten

3D / Geländemodell

- "3dDisplay" — Auswahlliste — None / Components / 3D Polygon / Texture Bed
- "displayAs3DPolygon" — bool
- "displayOnExisting" — bool
- "hasSiteModel" — bool
- "Cut into Site Model" — bool
- "siteModelLayer" — Auswahlliste — Ebenenname des Geländemodells
- "minTINElev", "maxTINElev" — reell (nur lesbar)
- "__RecalcTINSurfaces", "__RecalcTINDependent" — bool (interner Zustand)
- "__editComponents" — bool
- "Simplification Tolerance" — reell

Pflanzenliste / Verteilung nach Pflanzdichte

- "distRate" — Zeichenfolge — Modus der Verteilung nach Pflanzdichte (z. B. "CustomPerc")
- "percRate" — reell — Prozentanteil für die Verteilung
- "percType" — Zeichenfolge — Einheit der Pflanzdichte (pro Quadratfuß / pro Quadratmeter / ...)
- "hiddenSymbolName", "hiddenRate", "hiddenRateType", "hiddenPercentage" — Zeichenfolge (interner Zustand je Eintrag)
- "hiddenMinNumOfPlants", "hiddenTotalNumOfPlants" — Zeichenfolge
- "BestFit" — bool
- "HedgeSpacingEnum" — Auswahlliste — SameAsPlantSpacingOrRate / Fixed
- "HedgeSpacingValue" — reell

Heckenoptionen

- "Width" — reell
- "Row Structure" — Auswahlliste — Rectangular / Staggered / Triple Staggered / Area
- "Hedge Rows" — int
- "Offset rows" — bool
- "PathOffset" — reell

Beschriftung

- "tagDisplay" — Auswahlliste — None / Left / Right
- "displayMarker" — bool
- "tagClass" — Auswahlliste — Klassenname
- "tagLineAngle" — reell — Grad
- "tagTextAngle" — reell — Grad
- "tagHeader" — Auswahlliste / Zeichenfolge — Formel für den Kopftext der Beschriftung
- "tagBody" — Auswahlliste / Zeichenfolge — Formel für den Haupttext der Beschriftung
- "controlPoint1X..controlPoint3Y" — reell (Weltkoordinaten der Kontrollpunkte der Beschriftung)

Nachhaltigkeit (Skalarfelder älterer Versionen + JSON-Datenblock von 2026)

- "HasSustainability" — bool
- "HasPermeability", "IsPermeable" — bool
- "Permeability" — reell
- "Permeability Unit" — Auswahlliste — cm/hour / ...
- "RunoffCoef" — reell
- "SRI" — reell
- "Sustainability Metric" — Zeichenfolge
- "SusPoint1", "SusPoint2", "SusPoint3" — Zeichenfolge
- "sustainability" — Zeichenfolge — JSON-Datenblock ab 2026

Verschiedenes

- "version" — int
- "__IsNew" — bool
- "GroupAllocation" — Zeichenfolge

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `LandscapeAreaObject(h: Handle)` | Verweist auf die vorhandene Flächenpflanzung `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `CreateFromPath(hPath: Handle) -> LandscapeAreaObject` *statisch* | Erzeugt eine Flächenpflanzung aus einem vorhandenen 2D-Pfadobjekt (üblicherweise einem Polygon oder einer Polylinie). |
| `Duplicate() -> LandscapeAreaObject` | Dupliziert die Flächenpflanzung in der Zeichnung und gibt die Kopie zurück. |

*Identität*

| Methode | Beschreibung |
|---|---|
| `GetName() -> str \| None` | Gibt den Namen zurück ("name", den Namen der Pflanzfläche, nicht den Objektnamen). |
| `SetName(value: str) -> bool` | Setzt den Namen. |
| `GetID() -> str \| None` | Gibt die ID zurück. |
| `SetID(value: str) -> bool` | Setzt die ID. |
| `GetDescription() -> str \| None` | Gibt die Beschreibung zurück. |
| `SetDescription(value: str) -> bool` | Setzt die Beschreibung. |
| `GetArea() -> float \| None` | Messwerte (nur lesbar; vom Objekt bei der Neuberechnung ermittelt) (Fläche des Bereichs in den aktuellen Flächeneinheiten). |
| `GetProjectedArea() -> float \| None` | Gibt die projizierte Fläche zurück (auf das Geländemodell projiziert; 0, wenn keines vorhanden ist). |
| `GetNumPlants() -> int \| None` | Gibt die Pflanzenanzahl zurück (Gesamtanzahl der verteilten Pflanzeninstanzen). |
| `GetDrawingMode() -> LandscapeAreaObject.DrawingMode \| None` | Gibt den Zeichenmodus zurück. |
| `SetDrawingMode(value: LandscapeAreaObject.DrawingMode) -> bool` | Setzt den Zeichenmodus. |
| `GetAreaUnits() -> LandscapeAreaObject.AreaUnits \| None` | Gibt die Flächeneinheiten zurück. |
| `SetAreaUnits(value: LandscapeAreaObject.AreaUnits) -> bool` | Setzt die Flächeneinheiten. |
| `GetPlantDisplay2D() -> LandscapeAreaObject.PlantDisplay2D \| None` | Gibt die 2D-Pflanzendarstellung zurück. |
| `SetPlantDisplay2D(value: LandscapeAreaObject.PlantDisplay2D) -> bool` | Setzt die 2D-Pflanzendarstellung. |

*Zugriffsmethoden für die Kompatibilität*

| Methode | Beschreibung |
|---|---|
| `GetShowPlantsIn2D() -> bool \| None` | `True` für jede Darstellung außer `None`; das Setzen von `True` wählt PlantSymbols, das Setzen von `False` wählt `None`. Verwenden Sie die Zugriffsmethoden für die Auswahlliste, um Wolken-/Linienmodi beizubehalten. |
| `SetShowPlantsIn2D(show: bool) -> bool` | Schaltet *Pflanzen in 2D anzeigen* ein oder aus. `True` für jede Darstellung außer `None`; das Setzen von `True` wählt PlantSymbols, das Setzen von `False` wählt `None`. Verwenden Sie die Zugriffsmethoden für die Auswahlliste, um Wolken-/Linienmodi beizubehalten. |

Geerbt: alle Elemente von [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### LandscapeAreaObject.PlantDisplay2D

> **Vollständiger Name:** `api.LandscapeAreaObject.PlantDisplay2D` · **Art:** `IntEnum`

Wie die Pflanzen einer Flächenpflanzung in 2D dargestellt werden.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` |  |
| `PlantCloud` | `1` |  |
| `PlantLine` | `2` |  |
| `PlantSymbols` | `3` |  |

#### LandscapeAreaObject.DrawingMode

> **Vollständiger Name:** `api.LandscapeAreaObject.DrawingMode` · **Art:** `IntEnum`

Ob das Objekt als Flächenpflanzung oder als Hecke gezeichnet wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `LandscapeArea` | `0` |  |
| `Hedgerow` | `1` |  |

#### LandscapeAreaObject.AreaUnits

> **Vollständiger Name:** `api.LandscapeAreaObject.AreaUnits` · **Art:** `IntEnum`

Einheiten, in denen die Fläche einer Flächenpflanzung angezeigt wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `SqFeet` | `0` |  |
| `SqMeters` | `1` |  |
| `Acres` | `2` |  |
| `Hectares` | `3` |  |
| `DocumentUnits` | `4` |  |

### SiteModelObject

> **Vollständiger Name:** `api.SiteModelObject` · **Erbt von:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Geländemodell (universeller Name "DTM6") aus dem Plug-in Landmark.

Ein Geländemodell ist eine Oberfläche aus einem unregelmäßigen Dreiecksnetz (TIN), die aus Ausgangsdaten (Vermessungspunkten, Höhenlinien, Begrenzungspolygonen, ...) erzeugt wird. Es enthält gleichzeitig zwei Oberflächen: den Ist-Zustand und den Soll-Zustand des Geländes (der alle darauf angewendeten Geländemodifikatoren berücksichtigt).

Häufig verwendete Parameter mit benannten Zugriffsmethoden:

- "2D Display" — welche Oberfläche(n) in 2D gezeichnet werden (Ist-Zustand / Soll-Zustand / Beide)
- "2D Style" — 2D-Darstellungsart (Höhenlinien, Dreiecke, eingefärbte Neigungen, ...)
- "3D Display" — welche Oberfläche(n) in 3D gezeichnet werden (Keine / Ist-Zustand / Soll-Zustand / Abtrag und Auftrag)
- "3D Style" — 3D-Darstellungsart (Punktkörper, Raster, Höhenlinien, eingefärbte Höhen / Neigungen, ...)
- "Area Display Type" — Flächeneinheiten für den Infobereich
- "Volume Display Type" — Volumeneinheiten für den Infobereich
- "Geometry Zref" — Referenzhöhe
- "Show Errors" — TIN-Fehlermarkierungen anzeigen

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten) Darstellungsauswahl

- "2D Display" — Auswahlliste — `kTINDisplayExistingOnly` / `kTINDisplayProposedOnly` / `kTINDisplayExistingAndProposed`
- "2D Style" — Auswahlliste — k2DTINStyle2DContour / k2DTINStyle2DContourSmoothed / k2DTINStyle2DContourColoredElevations / k2DTINStyle2DTriangulatedContoursColoredSlopes / k2DTINStyle2DTriangles / k2DTINStyle2DTrianglesColoredSlopes
- "3D Display" — Auswahlliste — `kTINDisplayNothing` / `kTINDisplayExistingOnly` / `kTINDisplayProposedOnly` / `kTINDisplayCutNFill`
- "3D Style" — Auswahlliste — k3DTINStyleMesh / k3DTINStyleMeshColoredElev / k3DTINStyleMeshColoredSlopes / k3DTINStyleGrid / k3DTINStyleGridColoredElev / k3DTINStyleGridColoredSlope / k3DTINStyleVerticalGrid / k3DTINStyleContour / k3DTINStyleExtrudedContour / k3DTINStyleExtContColoredElev
- "2D C&F Map Overlay" — bool

Flächen- / Volumenanzeigen (alle nur lesbar, formatierte Zeichenfolgenwerte)

- "Area Display Type" — Auswahlliste — `kAreaDisplaySqM` / `kAreaDisplayDecar` / `kAreaDisplayHectars` / `kAreaDisplaySqFt` / `kAreaDisplayAcre` / `kAreaUseDocumentUnits`
- "Projected Area (Existing)" — Zeichenfolge
- "Surface Area (Existing)" — Zeichenfolge
- "Surface Area (Proposed)" — Zeichenfolge
- "Volume Display Type" — Auswahlliste — `kVolumeDisplayCuM` / `kVolumeDisplayCuFt` / `kVolumeDisplayCuYd` / `kVolumeUseDocumentUnits`
- "Volume (Existing)" — Zeichenfolge
- "Volume (Proposed)" — Zeichenfolge
- "Cut Volume" — Zeichenfolge
- "Fill Volume" — Zeichenfolge
- "Net C&F Volume" — Zeichenfolge
- "Total C&F Volume" — Zeichenfolge

Geometrie / Fehler

- "Geometry Zref" — reell — Welteinheiten – Referenzhöhe
- "Grid Size" — reell
- "Tolerance" — reell
- "Depth Intervals" — reell
- "Show Errors" — bool
- "dontShowErrors" — bool — (veraltet)
- "Error Count" — Zeichenfolge — nur lesbare, formatierte Anzahl
- "Site Model Name" — Zeichenfolge — nur lesbarer Anzeigename

Geobildüberlagerung

- "GeoImageEnabled" — bool
- "GeoServerURL" — Zeichenfolge
- "GeoServiceName" — Zeichenfolge
- "GeoServiceType" — Zeichenfolge
- "GeoServiceRenderFunc" — Auswahlliste
- "GeoLayers" — Zeichenfolge
- "GeoResolution" — int — Pixel pro Kachel
- "GeoTile" — int
- "StoreGeoimage" — bool

Interner Zustand

- "__version", "__messageID" — int
- "__UUID" — Zeichenfolge
- "__compsMinZ" — reell
- "__SavedGeoinfo" — Zeichenfolge

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `SiteModelObject(h: Handle)` | Verweist auf das vorhandene Geländemodell `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D) -> SiteModelObject` *statisch* | Geländemodelle werden üblicherweise interaktiv über die Landmark-Befehle erzeugt (Vermessungspunkte, Höhenlinien, ...); diese Erzeugungsmethode legt ein leeres Geländemodell an `position` an, das der Aufrufer anschließend mit den entsprechenden Menübefehlen oder durch Bearbeiten seiner Ausgangsdatengruppe füllt. |
| `Duplicate() -> SiteModelObject` | Dupliziert das Geländemodell in der Zeichnung und gibt die Kopie zurück. |
| `Get2DDisplay() -> SiteModelObject.Display2D \| None` | Gibt die 2D-Darstellung zurück. |
| `Set2DDisplay(value: SiteModelObject.Display2D) -> bool` | Setzt die 2D-Darstellung. |
| `Get3DDisplay() -> SiteModelObject.Display3D \| None` | Gibt die 3D-Darstellung zurück. |
| `Set3DDisplay(value: SiteModelObject.Display3D) -> bool` | Setzt die 3D-Darstellung. |
| `Get2DStyle() -> str \| None` | Unveränderte Werte der Darstellungsart (die vollständige Liste finden Sie in der Landmark-Dokumentation). Die Namen der Darstellungsarten sind ASCII-Bezeichner wie "k2DTINStyle2DTriangles" oder "k3DTINStyleMesh". |
| `Set2DStyle(value: str) -> bool` | Setzt die 2D-Darstellungsart. Unveränderte Werte der Darstellungsart (die vollständige Liste finden Sie in der Landmark-Dokumentation). Die Namen der Darstellungsarten sind ASCII-Bezeichner wie "k2DTINStyle2DTriangles" oder "k3DTINStyleMesh". |
| `Get3DStyle() -> str \| None` | Gibt die 3D-Darstellungsart zurück. |
| `Set3DStyle(value: str) -> bool` | Setzt die 3D-Darstellungsart. |
| `GetGeometryZReference() -> float \| None` | Referenzhöhe (Welteinheiten) für Berechnungen anhand von Höhenlinien. |
| `SetGeometryZReference(value: float) -> bool` | Setzt die Z-Referenz der Geometrie. Referenzhöhe (Welteinheiten) für Berechnungen anhand von Höhenlinien. |
| `GetShowErrors() -> bool \| None` | Ob *Fehler anzeigen* eingeschaltet ist. |
| `SetShowErrors(value: bool) -> bool` | Schaltet *Fehler anzeigen* ein oder aus. |
| `GetProjectedAreaExisting() -> str \| None` | Schreibgeschützte Flächen- und Volumenangaben (formatierte Zeichenfolge; leer, wenn nicht berechnet). |
| `GetSurfaceAreaExisting() -> str \| None` | Gibt den Flächeninhalt der Oberfläche im Ist-Zustand zurück. |
| `GetSurfaceAreaProposed() -> str \| None` | Gibt den Flächeninhalt der Oberfläche im Soll-Zustand zurück. |
| `GetVolumeExisting() -> str \| None` | Gibt das Volumen im Ist-Zustand zurück. |
| `GetVolumeProposed() -> str \| None` | Gibt das Volumen im Soll-Zustand zurück. |
| `GetCutVolume() -> str \| None` | Gibt das Abtragsvolumen zurück. |
| `GetFillVolume() -> str \| None` | Gibt das Auftragsvolumen zurück. |

Geerbt: alle Elemente von [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### SiteModelObject.Display2D

> **Vollständiger Name:** `api.SiteModelObject.Display2D` · **Art:** `IntEnum`

Auswahl der 2D- / 3D-Darstellung

| Element | Wert | Beschreibung |
|---|---|---|
| `ExistingOnly` | `0` |  |
| `ProposedOnly` | `1` |  |
| `ExistingAndProposed` | `2` |  |

#### SiteModelObject.Display3D

> **Vollständiger Name:** `api.SiteModelObject.Display3D` · **Art:** `IntEnum`

Was die 3D-Darstellung eines Geländemodells zeigt.

| Element | Wert | Beschreibung |
|---|---|---|
| `Nothing` | `0` |  |
| `ExistingOnly` | `1` |  |
| `ProposedOnly` | `2` |  |
| `CutAndFill` | `3` |  |

### SiteModifierObject

> **Vollständiger Name:** `api.SiteModifierObject` · **Erbt von:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Geländemodifikator (universeller Name "Site Modifiers") aus dem Plug-in Landmark.

Ein Geländemodifikator ist ein pfadbasiertes Objekt, das eine Geländemodell-Oberfläche umformt. Ein einzelner Geländemodifikator bietet mehrere mögliche Konfigurationen, die über den Parameter "Config" ausgewählt werden; jede Konfiguration wird gemäß dem Parameter "Apply To" auf den Ist-Zustand ("Existing") oder den Soll-Zustand ("Proposed") angewendet.

Häufig verwendete Parameter mit benannten Zugriffsmethoden:

- "Config" — zu verwendende Umformungsmethode (siehe `SiteModifierObject.Config` unten)
- "Apply To" — welche Geländemodell-Oberfläche geändert wird (Ist-Zustand / Soll-Zustand)
- "Show 3D" — Modifikator als 3D-Geometrie anzeigen
- "Retain Slope Inside" — Neigung innerhalb der Grundfläche des Modifikators beibehalten
- "Simplification Tolerance" — Toleranz für die Vereinfachung der Eckpunkte in Welteinheiten

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten). Der Geländemodifikator speichert die Parameter aller Konfigurationen gleichzeitig; das Plug-in verwendet tatsächlich nur die Parameter, die zum aktuellen Wert von "Config" gehören. Gemeinsam (alle Konfigurationen)

- "Config" — Auswahlliste — Fence (=Änderungsbereich) / Contour (=Bruchkante (Linie)) / Pad (=Bruchkante (Fläche)) / PadwEdge (=Senkrechte Bruchkante) / Aligned (=Angepasst) / Path (=Bruchkante mit Mittelachse) / Texture Bed (=Oberflächentextur) / Grader (=Auf-/Abtragsbereich)
- "Apply To" — Auswahlliste — Existing / Proposed
- "Show 3D" — bool
- "Retain Slope Inside" — bool
- "Simplification Tolerance" — reell — Welteinheiten
- "Modifier Vertex Count" — Zeichenfolge — nur lesbare, formatierte Anzahl
- "__version" — int
- "__IsNewObject" — bool
- "__WasGeometryChanged", "__WasSideDataChanged", "__IsInvalPath", "__ChangeAffectsSiteModel" — bool (intern)

Änderungsbereich (Config = "Fence")

- "Define by contours" — bool
- "Use as C&F Calc Zone" — bool
- "__AreContoursConnected" — bool (intern)

Bruchkante (Fläche) (Config = "Pad") und Senkrechte Bruchkante (Config = "PadwEdge")

- "Elevation" — reell — Welteinheiten
- "Slope Def" — Auswahlliste — None / Angle / DownPerc / UpPerc / DownRatio / UpRatio
- "Slope Ang" — reell — Grad (verwendet, wenn Slope Def = Angle)
- "Slope Percent" — Zeichenfolge — z. B. "5%" (verwendet, wenn Slope Def = DownPerc/UpPerc)
- "Slope Ratio" — Zeichenfolge — z. B. "1:4" (verwendet, wenn Slope Def = DownRatio/UpRatio)
- "ElevAtEnd" — reell — Welteinheiten
- "ContourAng" — reell — Grad
- "Slope A", "Slope B" — Zeichenfolge
- "Show Cross Slope" — bool
- "Show Slope A Arrow" — bool
- "Show Slope B Arrow" — bool
- "Constrain Slope Down" — bool
- "Show Slope Elevations" — bool
- "Show Modifier Elevation" — bool
- "Annotation Class" — Auswahlliste — Klassenname
- "__DoElevateRetEdge" — bool (nur für senkrechte Bruchkanten)
- "__UseSlopeToolAtCreate" — bool

Angepasst (Config = "Aligned")

- "Align with Objects on" — Auswahlliste — AllLayers / VisLayersOnly / SameLayerAsHScape / CustomSetOfLayers / SelectLayers
- "AlignWithObjectsOnOption" — int
- "Interpolate Surface" — bool
- "Interpolation Type" — Auswahlliste — Concave / Convex
- "Show Profile Lines" — bool
- "Show Profile Names" — bool
- "Show Slopes" — bool
- "Show Vertex Elevation" — bool
- "Show Profile Line Markers" — bool
- "Show Stake Objects" — bool
- "Show Grade Objects" — bool
- "Start Symbol Marker Name" — Zeichenfolge — Symbolname
- "End Symbol Marker Name" — Zeichenfolge — Symbolname
- "Smoothness Sampling" — int
- "Falloff" — Zeichenfolge — Prozent, z. B. "50,00%"
- "__RecreateAlignedTIN" — bool (intern)

Bruchkante mit Mittelachse (Config = "Path")

- "LongProf_StartElevValue" — reell — Welteinheiten
- "LongProf_EndElevValue" — reell — Welteinheiten
- "LongProf_MarkerType" — Auswahlliste — None / Triangle / TriangleFilled / Circle / Dot / Cross / Circle Cross / Tick Mark
- "LongProf_MarkerFactor" — reell
- "LongProf_SlopesDef" — Auswahlliste — GradePerc / Ratio / Angle
- "LongProf_ShowLine", "LongProf_ShowSlopes", "LongProf_ShowVertexElev", "LongProf_ShowLineMarkers" — bool
- "LongProf_StartSymMarkerName", "LongProf_EndSymMarkerName" — Zeichenfolge
- "TransProf_SlopesDef" — Auswahlliste — GradePerc / Ratio / Angle
- "TransProf_ShowLines", "TransProf_ShowNames", "TransProf_ShowSlopes", "TransProf_ShowVertexElev", "TransProf_ShowLineMarkers" — bool
- "TransProf_StartSymMarkerName", "TransProf_EndSymMarkerName" — Zeichenfolge
- "Prof_SlopeArrowDownward" — bool
- "__RecreatePathTIN", "__FitLongProfToSurf" — bool (intern)

An Objekte anpassen (Config = "Aligned", Untermodus)

- "Use Objects on" — Auswahlliste — AllLayers / VisLayersOnly / SameLayerAsObject / CustomSetOfLayers / SelectLayers
- "Fit to" — Auswahlliste — FitBottom / FitTop
- "__IsPathOK" — bool (intern)

Oberflächentextur (Config = "Texture Bed")

- "Texture Class" — Auswahlliste — Name der für die Oberflächentextur zu verwendenden Klasse

Flächen- / Volumenanzeigen (siehe Auswahlliste "Volume Display Type")

- "Area Display Type" — Auswahlliste — `kAreaDisplaySqM` / `kAreaDisplayDecar` / `kAreaDisplayHectars` / `kAreaDisplaySqFt` / `kAreaDisplayAcre` / `kAreaUseDocUnits`
- "Projected Area" — Zeichenfolge (nur lesbar)
- "Surface Area (Existing)" — Zeichenfolge (nur lesbar)
- "Surface Area (Proposed)" — Zeichenfolge (nur lesbar)
- "Volume Display Type" — Auswahlliste — `kVolumeDisplayCuM` / `kVolumeDisplayCuFt` / `kVolumeDisplayCuYd` / `kVolumeUseDocUnits`
- "Volume (Existing)" — Zeichenfolge (nur lesbar)
- "Volume (Proposed)" — Zeichenfolge (nur lesbar)
- "Cut Volume" — Zeichenfolge (nur lesbar)
- "Fill Volume" — Zeichenfolge (nur lesbar)
- "Net C&F Volume" — Zeichenfolge (nur lesbar)
- "Total C&F Volume" — Zeichenfolge (nur lesbar)

Veraltet (von Objekten verwendet, die in früheren Vectorworks-Versionen erzeugt wurden)

- "Zref" — reell
- "Slope" — reell
- "SlopeDef" — Auswahlliste — None / Angle / DownPerc / Percent / DownRatio / UpRatio
- "Prop" — Auswahlliste — Existing / Proposed
- "Class" — Auswahlliste — Klassenname
- "ControlPoint01X..ControlPoint14Y" — reell (Weltkoordinaten)
- "Show Slope Arrow" — bool

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `SiteModifierObject(h: Handle)` | Verweist auf den vorhandenen Geländemodifikator `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `CreateFromPath(hPath: Handle) -> SiteModifierObject` *statisch* | Erstellt einen Geländemodifikator aus einem vorhandenen 2D-Pfadobjekt (Polygon oder Polylinie). |
| `Duplicate() -> SiteModifierObject` | Dupliziert den Geländemodifikator in der Zeichnung und gibt die Kopie zurück. |
| `GetConfig() -> SiteModifierObject.Config \| None` | Gibt die Konfiguration zurück. |
| `SetConfig(value: SiteModifierObject.Config) -> bool` | Setzt die Konfiguration. |
| `GetApplyTo() -> SiteModifierObject.ApplyTo \| None` | Gibt zurück, auf welche Oberfläche die Änderung angewendet wird. |
| `SetApplyTo(value: SiteModifierObject.ApplyTo) -> bool` | Setzt, auf welche Oberfläche die Änderung angewendet wird. |
| `GetShow3D() -> bool \| None` | Ob *3D anzeigen* eingeschaltet ist. |
| `SetShow3D(value: bool) -> bool` | Schaltet *3D anzeigen* ein oder aus. |
| `GetRetainSlopeInside() -> bool \| None` | Ob *Neigung im Inneren beibehalten* eingeschaltet ist. |
| `SetRetainSlopeInside(value: bool) -> bool` | Schaltet *Neigung im Inneren beibehalten* ein oder aus. |
| `GetSimplificationTolerance() -> float \| None` | Gibt die Vereinfachungstoleranz zurück. |
| `SetSimplificationTolerance(value: float) -> bool` | Setzt die Vereinfachungstoleranz. |

Geerbt: alle Elemente von [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### SiteModifierObject.Config

> **Vollständiger Name:** `api.SiteModifierObject.Config` · **Art:** `IntEnum`

Umformungsmethode eines Geländemodifikators ("Config").

| Element | Wert | Beschreibung |
|---|---|---|
| `GradeLimits` | `0` | Geschlossene Umgrenzung, die den Einflussbereich der Änderung begrenzt. |
| `Contour` | `1` | Bruchkante (Linie): offene Höhenlinie auf einer festen Höhe. |
| `Pad` | `2` | Ebene Bruchkantenfläche auf einer Zielhöhe. |
| `RetainingPad` | `3` | Senkrechte Bruchkante. |
| `Aligned` | `4` | Angepasste Oberfläche mit Höhen und Neigungen pro Seite. |
| `Path` | `5` | Bruchkante mit Mittelachse (Pfad mit Längsprofil). |
| `FitToObjects` | `6` | Interpoliert anhand der Höhen der Objekte, die durch das Polygon verlaufen. |
| `TextureBed` | `7` | Oberflächentextur (keine Höhenänderung). |
| `SpoilPile` | `8` | Schüttet Material mit einer Neigung auf, bis ein Volumen / eine Höhe erreicht ist. |

#### SiteModifierObject.ApplyTo

> **Vollständiger Name:** `api.SiteModifierObject.ApplyTo` · **Art:** `IntEnum`

Auf welche Oberfläche des Geländemodells ein Geländemodifikator angewendet wird.

| Element | Wert | Beschreibung |
|---|---|---|
| `Existing` | `0` |  |
| `Proposed` | `1` |  |

### StakeObject

> **Vollständiger Name:** `api.StakeObject` · **Erbt von:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Vermessungspunkt (universeller Name "Stake Object") aus dem Plug-in Landmark.

Ein Vermessungspunkt ist ein beschrifteter 2D-Punkt an einer bestimmten Position und Höhe. Je nach "Mode" liefert der Vermessungspunkt seine Höhe als Ausgangsdaten für ein Geländemodell, übernimmt die Höhe der aktuellen Geländemodell-Oberfläche, dient nur als 2D-Grafik oder stellt einen Geländemodifikatorpunkt dar.

Häufig verwendete Parameter mit benannten Zugriffsmethoden:

- "Mode" — Funktion des Vermessungspunkts (siehe `StakeObject.Mode` unten)
- "Site Model" — auf welche Geländemodell-Oberfläche sich der Vermessungspunkt bezieht ("Existing" für Ist-Zustand oder "Proposed" für Soll-Zustand)
- "ID" — numerische Kennung
- "ID Prefix" — Präfix, das in Beschriftungen vor die ID gesetzt wird
- "ID Suffix" — Suffix, das in Beschriftungen an die ID angehängt wird
- "Z Value" — Höhenlage (Welteinheiten)
- "Data" — frei formulierbare Beschreibung
- "Label ReferenceN" — welche Daten in der Beschriftung des Vermessungspunkts erscheinen

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten) Funktion und Ziel-Geländemodell

- "Mode" — Auswahlliste — Include as site model data / Set elev to site model grade / Set elev to site model cut surface / Set elev to object spot / Use as 2D graphic only / Site modifier object
- "Previous Mode" — Zeichenfolge — zuletzt ausgewählter Wert von Mode (vom Plug-in verwendet)
- "Site Model" — Auswahlliste — Existing / Proposed

Identität / Beschriftung

- "ID" — int — numerische Kennung
- "ID Prefix" — Zeichenfolge
- "ID Suffix" — Zeichenfolge
- "Data" — Zeichenfolge — frei formulierbare Beschreibung
- "Label Reference" — Zeichenfolge — veralteter Beschriftungsbezug
- "Label ReferenceN" — Auswahlliste — ID / Elevation / Description / ID/Elevation / ID/Description / Description/Elevation / Stationing Data / Coordinate PointNE / Coordinate PointEN / Coordinate PointXY / Coordinate PointYX / Latitude/Longitude / Longitude/Latitude / Latitude/Longitude(WGS84) / Longitude/Latitude(WGS84) / No Label / Object Spot Height
- "Label Position" — Auswahlliste — Auto / Right / Left / Center
- "Style" — Auswahlliste — none / Triangle / TriangleFilled / Circle / Dot / Cross / Circle Cross / Tick Mark
- "AutoIDNumber" — bool
- "InitIDNumber" — int
- "Bubble Style" — Auswahlliste — None / Box / Round Rect / Cloud / Hexagonal / Circle
- "Radius Factor" — reell
- "Margin" — reell
- "UseAnnotation" — Auswahlliste — Data Tag / Built-in Tag
- "DataTagStyle" — Auswahlliste — Name des Datenstempelstils
- "LabelText", "LabelValues" — Zeichenfolge

Höhenlage und Koordinaten

- "Z Value" — reell — Welteinheiten (Höhenlage)
- "Station Point Data" — reell — Welteinheiten
- "Coordinate Units" — Auswahlliste — Document units / CRS units / Feet / Meters
- "ElevationUnits" — Auswahlliste — Document units / Feet/Inches / Inches / Feet / Yards / Miles / Microns / Millimeters / Centimeters / Meters / Kilometers / Decimal Degrees / Degrees/Minutes/Seconds
- "CoordinatePrecM" — Auswahlliste — 1 / .1 / .01 / .001 / .0001 / ... / .0000000001
- "CoordinatePrecA" — Auswahlliste — 0.0 / 0.00 / 0.000 / 0.0000 / ... / 0.00000000
- "ElevationPrecM", "ElevationPrecA" — Auswahlliste (dieselben Auswahlmöglichkeiten wie CoordinatePrecM/A)
- "ShowUnitMark" — bool
- "ShowElevationMark" — bool
- "Latitude", "Longitude", "Latitude WGS84", "Longitude WGS84" — reell
- "Easting", "Northing" — reell
- "Easting Display", "Northing Display" — Zeichenfolge (nur lesbare, formatierte Werte)

Darstellung

- "Display Leader Line" — bool
- "3D Display" — Auswahlliste — None / Locus / Extrude
- "ExtrudeWidth", "ExtrudeHeight" — reell (Welteinheiten)
- "Scale Factor" — reell
- "markOffsetX", "markOffsetY" — reell (Welteinheiten)
- "markRot" — reell (Grad)
- "ControlPoint01X", "ControlPoint01Y" — reell (Welteinheiten)

Intern / Versionierung

- "__version" — int
- "__new" — bool
- "__toolpref" — bool
- "__dtmElevCalculated" — bool
- "__DataTagStyleName" — Zeichenfolge

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `StakeObject(h: Handle)` | Verweist auf den vorhandenen Vermessungspunkt `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D, zValue: float = 0.0) -> StakeObject` *statisch* | Erzeugt einen Vermessungspunkt an `position` auf der aktiven Ebene / im aktuellen Container. |
| `Duplicate() -> StakeObject` | Dupliziert den Vermessungspunkt in der Zeichnung und gibt die Kopie zurück. |
| `GetMode() -> StakeObject.Mode \| None` | Gibt den Modus zurück. |
| `SetMode(value: StakeObject.Mode) -> bool` | Setzt den Modus. |
| `GetSiteModel() -> StakeObject.SiteModel \| None` | Gibt das Geländemodell zurück. |
| `SetSiteModel(value: StakeObject.SiteModel) -> bool` | Setzt das Geländemodell. |
| `GetID() -> int \| None` | Gibt die ID zurück. |
| `SetID(value: int) -> bool` | Setzt die ID. |
| `GetIDPrefix() -> str \| None` | Gibt das ID-Präfix zurück. |
| `SetIDPrefix(value: str) -> bool` | Setzt das ID-Präfix. |
| `GetIDSuffix() -> str \| None` | Gibt das ID-Suffix zurück. |
| `SetIDSuffix(value: str) -> bool` | Setzt das ID-Suffix. |
| `GetZValue() -> float \| None` | Gibt den Z-Wert zurück (Höhenlage in Welteinheiten). |
| `SetZValue(value: float) -> bool` | Setzt den Z-Wert. |
| `GetData() -> str \| None` | Gibt die Daten zurück (frei formulierbare Beschreibung in der Beschriftung). |
| `SetData(value: str) -> bool` | Setzt die Daten. |
| `GetLabelReference() -> str \| None` | Was die Beschriftung des Vermessungspunkts anzeigt (ID / Höhe / Beschreibung / Kombinationen / Koordinaten / ...) |
| `SetLabelReference(value: str) -> bool` | Setzt den Beschriftungsbezug. Was die Beschriftung des Vermessungspunkts anzeigt (ID / Höhe / Beschreibung / Kombinationen / Koordinaten / ...) |
| `GetDisplayLeaderLine() -> bool \| None` | Ob *Verweislinie anzeigen* eingeschaltet ist. |
| `SetDisplayLeaderLine(value: bool) -> bool` | Schaltet *Verweislinie anzeigen* ein oder aus. |
| `GetShowElevationMark() -> bool \| None` | Ob *Höhenmarke anzeigen* eingeschaltet ist. |
| `SetShowElevationMark(value: bool) -> bool` | Schaltet *Höhenmarke anzeigen* ein oder aus. |

Geerbt: alle Elemente von [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### StakeObject.Mode

> **Vollständiger Name:** `api.StakeObject.Mode` · **Art:** `IntEnum`

Funktion des Vermessungspunkts in Bezug auf das Geländemodell.

| Element | Wert | Beschreibung |
|---|---|---|
| `SiteModelSource` | `0` | „Für Ist-Modell verwenden“ – der Z-Wert des Vermessungspunkts wird als Punkt der Ausgangsdaten verwendet. |
| `SetToSiteModelGrade` | `1` | „z-Wert automatisch anpassen“. |
| `SetToCutSurface` | `2` | „z-Wert auf Schnittfläche Geländemodell setzen“. |
| `SetToObjectSpot` | `3` | „z-Wert auf Objektpunkt setzen“. |
| `Graphic2DOnly` | `4` | „Nur als Punkt verwenden“. |
| `SiteModifierObject` | `5` | „Als Modifikator verwenden“. |

#### StakeObject.SiteModel

> **Vollständiger Name:** `api.StakeObject.SiteModel` · **Art:** `IntEnum`

Auf welche Oberfläche des Geländemodells sich ein Vermessungspunkt bezieht.

| Element | Wert | Beschreibung |
|---|---|---|
| `Existing` | `0` |  |
| `Proposed` | `1` |  |

### HardscapeObject

> **Vollständiger Name:** `api.HardscapeObject` · **Erbt von:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Belag/Weg (universeller Name "Hardscape") aus dem Plug-in Landmark.

Ein Belag/Weg-Objekt ist ein pfadbasiertes Objekt, das eine befestigte Oberfläche darstellt (Gehweg, Terrasse, Zufahrt, ...). Es kann eine Fläche oder ein Weg sein (Streifen mit konstanter Breite entlang des Pfads). Es kann eine Einfassung enthalten, 3D-Geometrie erzeugen (Boden/Decke, Bruchkante an der Oberseite, Bruchkante an der Unterseite, Oberflächentextur) und Flächeninhalte sowie Umfänge von Hauptfläche und Einfassung ausgeben.

Häufig verwendete Parameter mit benannten Zugriffsmethoden:

- "ID" — für den Benutzer sichtbare Kennung / Name des Oberflächenmaterials
- "Sketch" — Skizzenstil (die vollständige Liste finden Sie im Plug-in)
- "Tag Display" — Beschriftungsplatzierung (None / Rechts / Links / Frei)
- "Tag Style" — in der Beschriftung angezeigte Informationen
- "Draw 3D" — 3D-Geometrie erzeugen
- "Site Mod" — als Geländemodifikator wirken
- "isPathway" — Wegmodus (Streifen mit fester Breite)
- "Use Border" — Einfassung hinzufügen
- "Slab Thick" — Boden/Decke-Dicke (Welteinheiten)
- "Border Thick" — Dicke der Einfassung (Welteinheiten)
- "Path Wid" — Wegbreite (Welteinheiten, nur im Wegmodus)
- "Path Offset" — Wegversatz (Welteinheiten, nur im Wegmodus)
- "Main Area", "Border Area", "Footprint Area", "Perimeter" — nur lesbare Messwerte

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten). Ein Belag/Weg-Objekt besitzt außerdem den gesamten Parametersatz eines Geländemodifikators (siehe SiteModifierObject); diese Parameter sind nur aktiv, wenn "Use Site Modifier" auf TRUE gesetzt ist und das Belag/Weg-Objekt einen Geländemodifikator steuert. Identität / Beschreibung

- "ID" — Zeichenfolge — für den Benutzer sichtbare Oberflächen- / Materialkennung
- "IDN" — Zeichenfolge — alternatives ID-Feld
- "Instance Name" — Zeichenfolge
- "Custom combination name" — Zeichenfolge
- "Custom combination formula" — Zeichenfolge
- "Description" — Zeichenfolge
- "Category" — Auswahlliste — z. B. Pflasterung (Kategoriesystem)
- "Style Name Formula" — Zeichenfolge
- "__NNA_Version" — int — Schemaversion des Plug-ins
- "__xver", "__modeOffset" — int / reell

Modusauswahl

- "Sketch" — Auswahlliste — Single sketch / weitere Optionen für die Skizzenqualität
- "isPathway" — bool
- "Draw 3D" — bool
- "Site Mod" — bool
- "Use Border" — bool
- "Configuration" — int
- "Mode 3D" — Auswahlliste (str) — "0" = `None` / "1" = Boden/Decke / "2" = Bruchkante an der Unterseite / "3" = Oberflächentextur / "4" = Bruchkante an der Oberseite
- "New Mode 3D" — Auswahlliste
- "Use Site Modifier" — bool
- "Site Model Interaction" — Auswahlliste — z. B. ActAsSiteModifier
- "TextBedClass" — Zeichenfolge
- "ConvertToBoundary" — bool

Weg- / Einfassungsmaße (Welteinheiten, sofern nicht anders angegeben)

- "Path Wid" — reell — Wegbreite
- "Path Offset" — reell — Versatz des Wegs gegenüber dem Pfad
- "Border Wid" — reell — Breite der Einfassung
- "Bord Spacing" — reell
- "Bord Path Opt" — int
- "Bord Back CIdx" — int — Farbindex der Hintergrundfarbe der Einfassung
- "Slab Thick" — reell
- "Border Thick" — reell

Fugen- / Schraffurmuster

- "Main Rsrc Name" — Zeichenfolge — Zubehörname des Fugenmusters der Hauptfläche
- "Bord Rsrc Name" — Zeichenfolge — Zubehörname des Fugenmusters der Einfassung
- "Main Joint Patt" — int
- "Bord Joint Patt" — int
- "Main Jt Patt Mod" — reell
- "Main Jt Patt Y Mod" — reell
- "Main Jt Patt Ang" — reell — Grad
- "Bord Jt Patt Ang" — reell — Grad
- "Main Jt I Scale", "Main Jt J Scale" — reell
- "Bord Jt I Scale", "Bord Jt J Scale" — reell
- "MainJointClass", "BorderJointClass" — Auswahlliste — Klassenname

Optionen für Kreis- / Wegpflaster (bei Kreis- oder Wegmustern)

- "Radial Course Spacing" — reell — Welteinheiten
- "Radial Center Paver Diam" — reell
- "Radial Offset Mode" — Zeichenfolge
- "Radial Offset Width" — reell
- "Radial Offset Angle" — reell — Grad
- "Radial Offset Shift" — reell
- "Radial Inside Paver Width" — reell
- "Radial Count Paver Width" — int
- "Path Paver Width" — reell
- "Path Paver Length" — reell
- "Path Paver Length Is Rand" — bool
- "Path Paver Rand Pct Length" — reell
- "Path Paver Offset Mode" — Zeichenfolge
- "Path Paver Offset Width" — reell
- "Path Paver Offset Shift" — reell

Beschriftung

- "Tag Display" — Auswahlliste — None / Right / Left / Floating
- "Tag Style" — Auswahlliste — ID only / ID-Area(s) / ID-Area(s)-Perim
- "TagAlignment" — Auswahlliste — Underline / Center
- "TagApproachAngle" — reell — Grad
- "TagShoulderAngle" — reell — Grad
- "TagUseMarker" — bool
- "TagSnapEdge" — bool
- "tagClass" — Auswahlliste — Klassenname
- "SlopeArrowClass" — Auswahlliste — Klassenname

Messwerte (schreibgeschützt, beim Zurücksetzen berechnet)

- "Main Area" — reell — (Fläche)
- "Border Area" — reell
- "Footprint Area" — reell
- "Perimeter" — reell — Welteinheiten
- "Main Perimeter" — reell
- "Border Perimeter" — reell
- "Main Area Fill Color" — int — Farbindex
- "Fill Type" — int

Preisangaben

- "Main Unit Price" — reell
- "Border Unit Price" — reell
- "Main Price Code" — Zeichenfolge
- "Border Price Code" — Zeichenfolge

Kontrollpunkte (Welteinheiten, durch die Umformen-Funktion gesteuert)

- "ControlPoint01X..ControlPoint21Y" — reell

Nachhaltigkeit (Skalarfelder älterer Versionen + JSON-Datenblock)

- "IsPermeable" — bool
- "RunoffCoef" — reell
- "Sustainability Metric" — Zeichenfolge
- "SusPoint1", "SusPoint2", "SusPoint3" — Zeichenfolge
- "SRI" — reell
- "HasSustainability", "HasPermeability" — bool
- "Permeability" — reell
- "Permeability Unit" — Auswahlliste — cm/hour / ...
- "sustainability" — Zeichenfolge — JSON-Datenblock (VW2026+)

Geländemodifikatorparameter des Belag/Weg-Objekts (vollständige Liste siehe SiteModifierObject): "Config", "Apply To", "Show 3D", "Retain Slope Inside", "Simplification Tolerance" sowie Parameter für Bruchkante (Fläche) / Angepasst / Bruchkante mit Mittelachse / An Objekte anpassen / Oberflächentextur und für die Flächen- / Volumenanzeigen.

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `HardscapeObject(h: Handle)` | Verweist auf das vorhandene Belag/Weg-Objekt `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `CreateFromPath(hPath: Handle) -> HardscapeObject` *statisch* | Erstellt ein Belag/Weg-Objekt aus einem vorhandenen 2D-Pfadobjekt (Polygon oder Polylinie). |
| `Duplicate() -> HardscapeObject` | Dupliziert das Belag/Weg-Objekt in der Zeichnung und gibt die Kopie zurück. |

*Identität*

| Methode | Beschreibung |
|---|---|
| `GetID() -> str \| None` | Gibt die ID zurück. |
| `SetID(value: str) -> bool` | Setzt die ID. |
| `Get3DMode() -> HardscapeObject.Mode3D \| None` | Gibt den 3D-Modus zurück. |
| `Set3DMode(value: HardscapeObject.Mode3D) -> bool` | Setzt den 3D-Modus. |
| `GetDraw3D() -> bool \| None` | Ob *3D zeichnen* eingeschaltet ist. |
| `SetDraw3D(value: bool) -> bool` | Schaltet *3D zeichnen* ein oder aus. |
| `GetIsSiteModifier() -> bool \| None` | Ob *Geländemodifikator* eingeschaltet ist. |
| `SetIsSiteModifier(value: bool) -> bool` | Schaltet *Geländemodifikator* ein oder aus. |
| `GetIsPathway() -> bool \| None` | Ob *Weg* eingeschaltet ist. |
| `SetIsPathway(value: bool) -> bool` | Schaltet *Weg* ein oder aus. |
| `GetUseBorder() -> bool \| None` | Ob *Einfassung verwenden* eingeschaltet ist. |
| `SetUseBorder(value: bool) -> bool` | Schaltet *Einfassung verwenden* ein oder aus. |
| `GetSlabThickness() -> float \| None` | Abmessungen (Welteinheiten). |
| `SetSlabThickness(value: float) -> bool` | Setzt die Boden/Decke-Dicke (Abmessungen in Welteinheiten). |
| `GetBorderThickness() -> float \| None` | Gibt die Dicke der Einfassung zurück. |
| `SetBorderThickness(value: float) -> bool` | Setzt die Dicke der Einfassung. |
| `GetBorderWidth() -> float \| None` | Gibt die Breite der Einfassung zurück. |
| `SetBorderWidth(value: float) -> bool` | Setzt die Breite der Einfassung. |
| `GetPathwayWidth() -> float \| None` | Gibt die Wegbreite zurück (isPathway = `True`). |
| `SetPathwayWidth(value: float) -> bool` | Setzt die Wegbreite. |
| `GetPathwayOffset() -> float \| None` | Gibt den Wegversatz zurück. |
| `SetPathwayOffset(value: float) -> bool` | Setzt den Wegversatz. |
| `GetMainArea() -> float \| None` | Messwerte (nur lesbar, bei der Neuberechnung ermittelt). |
| `GetBorderArea() -> float \| None` | Gibt die Fläche der Einfassung zurück. |
| `GetFootprintArea() -> float \| None` | Gibt die Grundfläche zurück. |
| `GetPerimeter() -> float \| None` | Gibt den Umfang zurück. |
| `GetMainPerimeter() -> float \| None` | Gibt den Umfang der Hauptfläche zurück. |
| `GetBorderPerimeter() -> float \| None` | Gibt den Umfang der Einfassung zurück. |

Geerbt: alle Elemente von [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### HardscapeObject.Mode3D

> **Vollständiger Name:** `api.HardscapeObject.Mode3D` · **Art:** `IntEnum`

3D-Modus des Belag/Weg-Objekts. Die vorhandenen Enumerationswerte sind API-Werte, keine nativen Auswahllistencodes. Die Schreibmethode synchronisiert bei aktuellen Objekten außerdem New Mode 3D / Use Site Modifier sowie bei Modifikatormodi Config, damit die Neuberechnung in Vectorworks den angeforderten Modus beibehält.

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` |  |
| `Slab` | `1` |  |
| `PadUnder` | `2` |  |
| `PadOver` | `3` |  |
| `TextureBed` | `4` |  |
| `SlabDrainage` | `5` |  |
| `AlignedSlab` | `6` |  |
| `AlignedModifOver` | `7` |  |
| `AlignedModifUnder` | `8` |  |

### PropertyLineObject

> **Vollständiger Name:** `api.PropertyLineObject` · **Erbt von:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Grenzlinie (universeller Name "Property Line") aus dem Plug-in Landmark.

Eine Grenzlinie stellt die rechtliche Grenze eines Flurstücks als geschlossenen 2D-Pfad dar. Sie beschriftet jedes Segment mit seiner Richtung/Länge und berechnet Fläche und Umfang des Flurstücks in einstellbaren Einheiten.

Häufig verwendete Parameter mit benannten Zugriffsmethoden:

- "Name" — für den Benutzer sichtbarer Name des Flurstücks
- "Number" — Flurstücksnummer
- "Area" — berechnete Fläche (nur lesbar, formatiert)
- "Perimeter" — berechneter Umfang (nur lesbar, formatiert)
- "Show Name" — Namen am Flurstück anzeigen
- "Show Number" — Nummer am Flurstück anzeigen
- "Show Area" — berechnete Fläche anzeigen
- "Area Units Imperial" — Flächeneinheiten bei einem Dokument mit imperialen Einheiten
- "Area Units Metric" — Flächeneinheiten bei einem Dokument mit metrischen Einheiten
- "Annotation Units" — Einheiten für die Längenbeschriftungen der Segmente (Get/SetDistanceUnits)

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten) Identität

- "Name" — Zeichenfolge
- "Number" — Zeichenfolge

Messwerte (nur lesbar, formatiert)

- "Area" — Zeichenfolge
- "Perimeter" — Zeichenfolge

Ein-/Ausschaltoptionen

- "Show Name" — bool
- "Show Number" — bool
- "Show Area" — bool
- "Reverse Direction" — bool
- "Fill Behind Text" — bool
- "FillBehindSegText" — bool
- "Tag Show Unit" — bool
- "Seg Show Unit" — bool
- "Annotate Segments" — bool
- "Draw 3D" — bool

Einheiten und Formatierung

- "Area Units Metric" — Auswahlliste — Document Units / Square Feet / Square Yards / Square Miles / Acres / Square Meters / Square Kilometers / Hectares
- "Area Units Imperial" — Auswahlliste — (dieselben Auswahlmöglichkeiten wie Area Units Metric)
- "Annotation Units" — Auswahlliste — Document Units / Feet & Inches / Inches / Feet / Yards / Miles / Microns / Millimeters / Centimeters / Meters / Kilometers
- "Decimals" — int
- "SegDecimals" — int
- "Text Rotation" — reell — Grad

Segment- / Eckpunktdarstellung

- "Annotation Style" — Auswahlliste — Angle, Distance, Curve / Angle, Distance / Distance Only
- "Angle Format" — Optionsfeld — Azimut / Quadrantenwinkel
- "Corner Indicator" — Auswahlliste — None / Triangle / Filled Triangle / Circle / Dot / Cross / Circle Cross / Tick Mark
- "Corner Indicator Size" — reell — Welteinheiten
- "Report Distance" — Auswahlliste — On Segment (Outside) / On Segment (Inside) / No
- "Report Angle" — Auswahlliste — On Segment (Outside) / On Segment (Inside) / Bearing at Corner (Outside) / Bearing at Corner (Inside) / Interior at Corner (Outside) / Interior at Corner (Inside) / No
- "Report Curve" — Auswahlliste — Yes as Table / Yes as Segment Label / No

Zusammenwirken mit Geländemodifikatoren

- "Site Modifier" — Auswahlliste — None / Grade Limits / Texture Bed
- "Texture Bed Class" — Auswahlliste — Klassenname

Abweichende Textstile (je Beschriftung)

- "Name Text Style" — Auswahlliste — Un-Styled / Class Text Style
- "Number Text Style" — Auswahlliste — Un-Styled / Class Text Style
- "Area Text Style" — Auswahlliste — Un-Styled / Class Text Style
- "Annot Text Style" — Auswahlliste — Un-Styled / Class Text Style

Interner Zustand

- "__IsNew" — bool
- "__Simple_Dialog" — bool
- "startCurveIDsAt", "numberOfCurves" — int
- "ControlPoint01X..ControlPoint02Y" — reell (Weltkoordinaten)
- "ResetCurveDataWS" — bool

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `PropertyLineObject(h: Handle)` | Verweist auf die vorhandene Grenzlinie `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `CreateFromPath(hPath: Handle) -> PropertyLineObject` *statisch* | Erstellt eine Grenzlinie aus einem vorhandenen 2D-Pfadobjekt (geschlossenes Polygon oder geschlossene Polylinie). |
| `Duplicate() -> PropertyLineObject` | Dupliziert die Grenzlinie in der Zeichnung und gibt die Kopie zurück. |
| `GetName() -> str \| None` | Gibt den Namen zurück. |
| `SetName(value: str) -> bool` | Setzt den Namen. |
| `GetNumber() -> str \| None` | Gibt die Nummer zurück. |
| `SetNumber(value: str) -> bool` | Setzt die Nummer. |
| `GetAreaText() -> str \| None` | Formatierte, nur lesbare Messwerte. Verwenden Sie `PrimitiveObject.GetArea` / GetPerimeter für die geometrischen Werte in Welteinheiten. |
| `GetPerimeterText() -> str \| None` | Gibt den Umfang als Text zurück. |
| `GetShowName() -> bool \| None` | Ob *Name anzeigen* eingeschaltet ist. |
| `SetShowName(value: bool) -> bool` | Schaltet *Name anzeigen* ein oder aus. |
| `GetShowNumber() -> bool \| None` | Ob *Nummer anzeigen* eingeschaltet ist. |
| `SetShowNumber(value: bool) -> bool` | Schaltet *Nummer anzeigen* ein oder aus. |
| `GetShowArea() -> bool \| None` | Ob *Fläche anzeigen* eingeschaltet ist. |
| `SetShowArea(value: bool) -> bool` | Schaltet *Fläche anzeigen* ein oder aus. |
| `GetAreaUnitsImperial() -> PropertyLineObject.AreaUnits \| None` | Gibt die imperialen Flächeneinheiten zurück. |
| `SetAreaUnitsImperial(value: PropertyLineObject.AreaUnits) -> bool` | Setzt die imperialen Flächeneinheiten. |
| `GetAreaUnitsMetric() -> PropertyLineObject.AreaUnits \| None` | Gibt die metrischen Flächeneinheiten zurück. |
| `SetAreaUnitsMetric(value: PropertyLineObject.AreaUnits) -> bool` | Setzt die metrischen Flächeneinheiten. |
| `GetDistanceUnits() -> str \| None` | Unveränderte Zeichenfolge der Längeneinheit (vollständige Liste siehe Plug-in, z. B. "Feet", "Meters", ...). |
| `SetDistanceUnits(value: str) -> bool` | Setzt die Längeneinheiten. Unveränderte Zeichenfolge der Längeneinheit (vollständige Liste siehe Plug-in, z. B. "Feet", "Meters", ...). |

Geerbt: alle Elemente von [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### PropertyLineObject.AreaUnits

> **Vollständiger Name:** `api.PropertyLineObject.AreaUnits` · **Art:** `IntEnum`

Flächeneinheiten, die sowohl von "Area Units Imperial" als auch von "Area Units Metric" unterstützt werden.

| Element | Wert | Beschreibung |
|---|---|---|
| `DocumentUnits` | `0` |  |
| `SquareFeet` | `1` |  |
| `SquareYards` | `2` |  |
| `SquareMiles` | `3` |  |
| `Acres` | `4` |  |
| `SquareMeters` | `5` |  |
| `SquareKilometers` | `6` |  |
| `Hectares` | `7` |  |

### ExistingTreeObject

> **Vollständiger Name:** `api.ExistingTreeObject` · **Erbt von:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plug-in-Objekt Baumkataster (universeller Name "Existing Tree") aus dem Plug-in Landmark.

Ein Kataster-Baum stellt einen einzelnen, bereits auf dem Gelände vorhandenen Baum dar. Er enthält Angaben zur Art, Größe (Höhe, Kronendurchmesser, Stammdurchmesser), Wurzeldaten (Wurzelballen, kritischer / primärer Wurzelbereich, Baumschutzbereich) sowie baumpflegerische Bewertungen von Zustand / Bedeutung / SULE / Maßnahmen.

Häufig verwendete Parameter mit benannten Zugriffsmethoden:

- "Genus Species" — botanischer (lateinischer) Name
- "Common Name" — Trivialname
- "Tree No" — Kennzeichnung / Instanzkennung
- "Origin" — Nicht festgelegt / Endemisch / Heimisch / Exotisch / Gebietsheimisch / Benutzerdefiniert
- "Height" — gesamte Baumhöhe (Welteinheiten)
- "Canopy" — Kronendurchmesser (Welteinheiten)
- "Calliper" — Stammdurchmesser in Brusthöhe (DBH), in Welteinheiten
- "RootBall" — Wurzelballendurchmesser (Welteinheiten)
- "CriticalRootZone" — Durchmesser des kritischen Wurzelbereichs (Welteinheiten)
- "PrimaryRootZone" — Durchmesser des primären Wurzelbereichs (Welteinheiten)
- "DisplayTPZ" — None / Kreisförmiger Bereich / Anhand von 12*DBH
- "Condition" — Nicht festgelegt / Ausgezeichnet / Gut / Durchschnittlich / Schlecht / Benutzerdefiniert
- "SULE" — Kategorie der voraussichtlichen sicheren Reststandzeit
- "Significance" — Bedeutungskategorie
- "ActionComment" — empfohlene Maßnahme (Erhalten / Entfernen / Verpflanzen / ...)
- "Location" — frei formulierbare Standortbeschreibung
- "Comments" — frei formulierbare Anmerkungen
- "Create3D" — 3D-Geometrie erzeugen

Vollständige Parameterreferenz für GetParam.../SetParam... (Parametername | Typ | Hinweise/Auswahlmöglichkeiten) Art / Identität

- "Genus Species" — Zeichenfolge — botanischer Name (Gattung + Art)
- "Common Name" — Zeichenfolge
- "Family" — Zeichenfolge
- "Tree No" — Zeichenfolge — Kennzeichnung / Instanzkennung
- "Origin" — Auswahlliste — Not Set / Endemic / Native / Exotic / Indigenous / Custom
- "CustomOrigin" — Zeichenfolge — frei formulierbarer Wert für Origin, wenn Origin = "Custom"
- "Invasive" — bool
- "InvasiveSpecies" — bool — (ersetzt "Invasive" ab 2026)
- "Elevation" — reell — Welteinheiten

Größe (Welteinheiten)

- "Height" — reell — gesamte Baumhöhe
- "Canopy" — reell — Kronendurchmesser (verwendet, wenn UseCanopyMin = `False`)
- "UseCanopyMin" — bool — CanopyMin für den Mindestradius verwenden
- "CanopyMin" — reell — kleinster Kronendurchmesser (unregelmäßige Kronen)
- "CanopyRotate" — reell — Grad – Drehung der Krone
- "CanopyArea" — reell (nur lesbar, berechnet)
- "Hgt First Branch" — reell — Welteinheiten
- "CrownClearance" — reell
- "FirstBranchDir" — Auswahlliste
- "AddIntercardinalDir" — bool — Kronenradien NO/SO/SW/NW einbeziehen
- "Calliper" — reell — DBH (Durchmesser in Brusthöhe)

Wurzelbereiche und Baumschutzbereich (TPZ), Welteinheiten

- "RootBall" — reell — Wurzelballendurchmesser
- "CriticalRootZone" — reell — Durchmesser des kritischen Wurzelbereichs (CRZ)
- "PrimaryRootZone" — reell — Durchmesser des primären Wurzelbereichs (PRZ)
- "RootZones" — Auswahlliste — None / Critical Zone / Primary Zone / Both Zones / Root Ball
- "EditTPZ" — bool
- "DisplayTPZ" — Auswahlliste — None / Display Circular Zone / Display Using 12 x DBH
- "TPZCornerRadius" — reell
- "TPZRadius" — reell
- "TPZArea", "AdjustedTPZArea" — reell (nur lesbar)
- "MinSRZRadius" — reell
- "DiamAtButtress" — reell
- "StructuralRootZone" — bool
- "CalculatedSRZ" — Zeichenfolge (nur lesbar, formatiert)

Baumpflegerische Beurteilung

- "Condition" — Auswahlliste — Not Set / Excellent / Good / Average / Poor / Custom
- "CustomCondition" — Zeichenfolge — frei formulierbarer Wert für Condition, wenn Condition = "Custom"
- "SULE" — Auswahlliste — Not Set / "Long (40+ yrs)" / "Medium (16-39 yrs)" / "Short (5-15 yrs)" / Removal / Custom
- "CustomSULE" — Zeichenfolge
- "Significance" — Auswahlliste — Not Set / Most Significant / Highly Significant / Less Significant / Least Significant / Hazardous / Custom
- "CustomSignificance" — Zeichenfolge
- "ActionComment" — Auswahlliste — Not Set / Retain / "Retain - Arborist Work Required" / "Transplant - Original Location" / "Transplant - Proposed Location" / Remove / "Remove - Within Building Footprint" / "Remove - Poor Health" / "Remove - Undesirable Species" / Custom
- "CustomAction" — Zeichenfolge
- "TreeProtectionOrder" — bool
- "VeteranTree" — bool
- "AncientTree" — bool
- "Form" — Auswahlliste — Not Set / Excellent / Good / Average / Poor
- "Structure" — Auswahlliste — Not Set / Excellent / Good / Average / Poor
- "Vigour" — Auswahlliste — Not Set / Excellent / Good / Average / Poor

Zusätzliche Daten

- "RL" — Zeichenfolge — Höhe über dem Bezugsniveau (Höhenreferenz)
- "Age" — Zeichenfolge
- "Year Planted" — Zeichenfolge
- "DateAssessed" — Zeichenfolge
- "Location" — Zeichenfolge
- "Comments" — Zeichenfolge — frei formulierbare Anmerkungen
- "Field1..Field10" — Zeichenfolge — benutzerdefinierte Zusatzfelder
- "sustainability" — Zeichenfolge — JSON-Datenblock (VW2026+)
- "VersionInfo" — Zeichenfolge (nur lesbar)

Mehrstämmige Bäume

- "__UseMultipleStems" — bool
- "__NumStems" — int
- "__Stem1..__Stem10" — reell — Durchmesser jedes Stamms in Welteinheiten
- "__TrunkPerim" — reell — Stammumfang

Unregelmäßige Krone (Radien je Richtung, Welteinheiten)

- "__CustomCanopy" — bool
- "__CanopyNorth", "__CanopySouth", "__CanopyEast", "__CanopyWest" — reell
- "__CanopyNorthEast", "__CanopySouthEast", "__CanopySouthWest", "__CanopyNorthWest" — reell

3D-Geometrie

- "Create 3D" — bool
- "UseGenerated3DGeometry" — bool
- "UseLaubwerk3DGeometry" — bool
- "UseImageProp3DGeometry" — bool
- "ImagePropSymbol" — Zeichenfolge — Symbolname für das Bildobjekt
- "__CanopySymbolName", "__TrunkSymbolName", "__RetainSymbolName", "__RemoveSymbolName", "__TransOldSymbolName", "__TransNewSymbolName", "__CustActionSymbolName", "__TransTrunkSymName" — Zeichenfolge (Namen der Symbole)
- "__UseSymComponents" — bool
- "__ApplyClassTextures" — bool
- "UseXForRemoveTrees" — bool — X-Markierung für Bäume zeichnen, die zur Entfernung vorgesehen sind
- "lw_Key", "lw_PlantFile", "lw_Variant" — Zeichenfolge — (Laubwerk-3D-Artenauswahl)
- "lw_GlobalSeason" — bool
- "lw_Season" — Zeichenfolge
- "lw_Global2D3DMat" — bool
- "lw_2DReprs", "lw_3DReprs" — Zeichenfolge
- "lw_MaterialStyle" — Zeichenfolge

Kennzeichnung / Beschriftung

- "UseTag" — bool
- "__SnapTagToTrunk" — bool
- "__DisplayTagMarker" — bool
- "__EnableTagShoulder" — bool
- "__TagShoulderAngle" — reell — Grad
- "__TagShoulderLength" — reell — Welteinheiten
- "__TagDisplayType" — int
- "__IDClass" — Auswahlliste — Klassenname
- "__FlagNumberDLog", "__FlagNumberDLogFEO" — bool
- "ControlPoint01X..ControlPoint08Y" — reell (Weltkoordinaten der verschiedenen Kontrollpunkte)

Abweichende Attribute (Farbe / Klasse / Liniendicke je Bereich) "__TPZClass", "__RootClass", "__TrunkClass", "__CanopyClass", "__SigClass" Auswahlliste (Klassenname) "__TPZLineWeight", "__TPZLineStyle", "__TPZLineCol" int "__PRZLineWeight", "__PRZLineStyle", "__PRZLineCol" int "__CRZLineWeight", "__CRZLineStyle", "__CRZLineCol" int

- "__UseSigColours" — bool
- "__Sig1FillCol..__Sig5FillCol" — int — Farbindizes
- "__SigColDisplay" — int
- "__TrunkType" — int

Automatische Nummerierung

- "__AutoNumberDefault" — bool
- "__AutoNumCurrent" — int
- "__AutoNumPrefix", "__AutoNumSuffix" — Zeichenfolge
- "__AutoNumZeroDefault" — int
- "__AutoNumberDups" — bool
- "__AutoNumSepLayers" — bool
- "__AutoNumThisTree" — bool
- "__IsAppliedAsTheDocDef" — bool
- "__IsNewDocument" — bool

Intern / Versionierung

- "__UniqueID" — Zeichenfolge
- "__LayerName" — Zeichenfolge
- "__LineTypes" — Zeichenfolge
- "__ETShape", "__ETShapeNum" — int
- "__CustomFieldNum" — int
- "__CustomLabels" — Zeichenfolge

**Konstruktoren**

| Konstruktor | Beschreibung |
|---|---|
| `ExistingTreeObject(h: Handle)` | Verweist auf den vorhandenen Kataster-Baum `h`; vor der Verwendung `IsValid()` prüfen. |

**Methoden**

*Allgemein*

| Methode | Beschreibung |
|---|---|
| `Is(h: Handle) -> bool` *statisch* | True, wenn `h` auf ein Objekt des von dieser Klasse dargestellten Typs verweist. |
| `Create(position: Math.Point2D) -> ExistingTreeObject` *statisch* | Erzeugt einen Kataster-Baum an `position` auf der aktiven Ebene / im aktuellen Container. |
| `Duplicate() -> ExistingTreeObject` | Dupliziert den Kataster-Baum in der Zeichnung und gibt die Kopie zurück. |

*Art / Identität*

| Methode | Beschreibung |
|---|---|
| `GetBotanicalName() -> str \| None` | Gibt den botanischen Namen zurück. |
| `SetBotanicalName(value: str) -> bool` | Setzt den botanischen Namen. |
| `GetCommonName() -> str \| None` | Gibt den Trivialnamen zurück. |
| `SetCommonName(value: str) -> bool` | Setzt den Trivialnamen. |
| `GetTreeNumber() -> str \| None` | Gibt die Baumnummer zurück (Kennzeichnung / Instanzkennung). |
| `SetTreeNumber(value: str) -> bool` | Setzt die Baumnummer. |
| `GetOrigin() -> ExistingTreeObject.Origin \| None` | Gibt den Ursprung zurück. |
| `SetOrigin(value: ExistingTreeObject.Origin) -> bool` | Legt den Ursprung fest. |
| `GetHeight() -> float \| None` | Größe (Welteinheiten) (Gesamthöhe). |
| `SetHeight(value: float) -> bool` | Setzt die Höhe (Größe in Welteinheiten). |
| `GetCanopyDiameter() -> float \| None` | Gibt den Kronendurchmesser zurück. |
| `SetCanopyDiameter(value: float) -> bool` | Setzt den Kronendurchmesser. |
| `GetCaliper() -> float \| None` | Gibt den Stammdurchmesser zurück (DBH: Durchmesser in Brusthöhe). |
| `SetCaliper(value: float) -> bool` | Setzt den Stammdurchmesser. |
| `GetRootBallDiameter() -> float \| None` | Wurzelbereiche (Welteinheiten). |
| `SetRootBallDiameter(value: float) -> bool` | Setzt den Wurzelballendurchmesser (Wurzelbereiche in Welteinheiten). |
| `GetCriticalRootZoneDiameter() -> float \| None` | Gibt den Durchmesser des kritischen Wurzelbereichs zurück. |
| `SetCriticalRootZoneDiameter(value: float) -> bool` | Setzt den Durchmesser des kritischen Wurzelbereichs. |
| `GetPrimaryRootZoneDiameter() -> float \| None` | Gibt den Durchmesser des primären Wurzelbereichs zurück. |
| `SetPrimaryRootZoneDiameter(value: float) -> bool` | Setzt den Durchmesser des primären Wurzelbereichs. |
| `GetTreeProtectionZone() -> ExistingTreeObject.TreeProtection \| None` | Gibt den Baumschutzbereich zurück. |
| `SetTreeProtectionZone(value: ExistingTreeObject.TreeProtection) -> bool` | Setzt den Baumschutzbereich. |
| `GetCondition() -> ExistingTreeObject.Condition \| None` | Gibt den Zustand zurück. |
| `SetCondition(value: ExistingTreeObject.Condition) -> bool` | Setzt den Zustand. |
| `GetSULE() -> ExistingTreeObject.SULE \| None` | Gibt die SULE-Kategorie zurück. |
| `SetSULE(value: ExistingTreeObject.SULE) -> bool` | Setzt die SULE-Kategorie. |
| `GetSignificance() -> ExistingTreeObject.Significance \| None` | Gibt die Bedeutung zurück. |
| `SetSignificance(value: ExistingTreeObject.Significance) -> bool` | Setzt die Bedeutung. |
| `GetActionComment() -> ExistingTreeObject.Action \| None` | Gibt den Maßnahmenkommentar zurück. |
| `SetActionComment(value: ExistingTreeObject.Action) -> bool` | Setzt den Maßnahmenkommentar. |
| `GetLocation() -> str \| None` | Gibt den Standort zurück (frei formulierbare Standortbeschreibung). |
| `SetLocation(value: str) -> bool` | Setzt den Standort. |
| `GetNotes() -> str \| None` | Gibt die Anmerkungen zurück. |
| `SetNotes(value: str) -> bool` | Setzt die Anmerkungen. |
| `GetCreate3D() -> bool \| None` | Ob *3D erzeugen* eingeschaltet ist. |
| `SetCreate3D(value: bool) -> bool` | Schaltet *3D erzeugen* ein oder aus. |

Geerbt: alle Elemente von [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### ExistingTreeObject.Origin

> **Vollständiger Name:** `api.ExistingTreeObject.Origin` · **Art:** `IntEnum`

Herkunft der Art eines Kataster-Baums.

| Element | Wert | Beschreibung |
|---|---|---|
| `NotSet` | `0` |  |
| `Endemic` | `1` |  |
| `Native` | `2` |  |
| `Exotic` | `3` |  |
| `Indigenous` | `4` |  |
| `Custom` | `5` |  |

#### ExistingTreeObject.TreeProtection

> **Vollständiger Name:** `api.ExistingTreeObject.TreeProtection` · **Art:** `IntEnum`

Darstellung des Baumschutzbereichs

| Element | Wert | Beschreibung |
|---|---|---|
| `None_` | `0` |  |
| `CircularZone` | `1` |  |
| `Using12DBH` | `2` |  |

#### ExistingTreeObject.Condition

> **Vollständiger Name:** `api.ExistingTreeObject.Condition` · **Art:** `IntEnum`

Baumpflegerische Beurteilung

| Element | Wert | Beschreibung |
|---|---|---|
| `NotSet` | `0` |  |
| `Excellent` | `1` |  |
| `Good` | `2` |  |
| `Average` | `3` |  |
| `Poor` | `4` |  |
| `Custom` | `5` |  |

#### ExistingTreeObject.SULE

> **Vollständiger Name:** `api.ExistingTreeObject.SULE` · **Art:** `IntEnum`

Voraussichtliche sichere Reststandzeit

| Element | Wert | Beschreibung |
|---|---|---|
| `NotSet` | `0` |  |
| `Long` | `1` |  |
| `Medium` | `2` |  |
| `Short` | `3` |  |
| `Removal` | `4` |  |
| `Custom` | `5` |  |

#### ExistingTreeObject.Significance

> **Vollständiger Name:** `api.ExistingTreeObject.Significance` · **Art:** `IntEnum`

Bewertung der Bedeutung eines Kataster-Baums.

| Element | Wert | Beschreibung |
|---|---|---|
| `NotSet` | `0` |  |
| `MostSignificant` | `1` |  |
| `HighlySignificant` | `2` |  |
| `LessSignificant` | `3` |  |
| `LeastSignificant` | `4` |  |
| `Hazardous` | `5` |  |
| `Custom` | `6` |  |

#### ExistingTreeObject.Action

> **Vollständiger Name:** `api.ExistingTreeObject.Action` · **Art:** `IntEnum`

Vorgeschlagene Maßnahme für einen Kataster-Baum.

| Element | Wert | Beschreibung |
|---|---|---|
| `NotSet` | `0` |  |
| `Retain` | `1` |  |
| `RetainArborist` | `2` |  |
| `TransplantOriginal` | `3` |  |
| `TransplantProposed` | `4` |  |
| `Remove` | `5` |  |
| `RemoveBuildingFootprint` | `6` |  |
| `RemovePoorHealth` | `7` |  |
| `RemoveSpecies` | `8` |  |
| `Custom` | `9` |  |

---

[Zurück zum Index](README.md) · [Nach oben](#objectslandmark--pflanzen-geländemodelle-belagweg-objekte-und-weitere-landschaftsobjekte)
