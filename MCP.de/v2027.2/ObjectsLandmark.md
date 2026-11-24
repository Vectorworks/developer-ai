[English](../../MCP/v2027.2/ObjectsLandmark.md) • **Deutsch** • [日本語](../../MCP.ja/v2027.2/ObjectsLandmark.md)

# ObjectsLandmark — Grundstück und Landschaft

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Zurück zum Inhaltsverzeichnis](README.md)

Werkzeuge für Grundstücks- und Landschaftsobjekte: Pflanzen, Beläge, Landschaftsflächen, Geländemodelle, Geländemodifikationen, Höhenpunkte, Grundstücksgrenzen und vorhandene Bäume.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Landmark](#landmark)
  - [createPlant](#createplant)
  - [createHardscape](#createhardscape)
  - [createLandscapeArea](#createlandscapearea)
  - [createSiteModifier](#createsitemodifier)
  - [createPropertyLine](#createpropertyline)
  - [createSiteModel](#createsitemodel)
  - [createStake](#createstake)
  - [createExistingTree](#createexistingtree)
  - [getLandmarkObject](#getlandmarkobject)
  - [setLandmarkObject](#setlandmarkobject)

## Überblick

Dieser Ordner enthält 1 Werkzeuggruppe mit insgesamt 10 Werkzeugen.

| Gruppe | Gruppen-ID | Standardmäßig aktiv | Risikostufe | Werkzeuge | Zusammenfassung |
|---|---|---|---|---|---|
| [Landmark](#landmark) | `landmark` | Nein | mittel | 10 | Pflanzen, Beläge, Landschaftsflächen, Geländemodelle, Geländemodifikationen, Höhenpunkte, Grundstücksgrenzen und vorhandene Bäume. |

## Landmark

> **Gruppe:** `Landmark` · **Gruppen-ID:** `landmark` · **Standardmäßig aktiv:** Nein · **Risikostufe:** mittel · **Werkzeuge:** 10

**Pflanzen, Beläge, Landschaftsflächen, Geländemodelle, Geländemodifikationen, Höhenpunkte, Grundstücksgrenzen und vorhandene Bäume.**

Grundstücks- und Landschaftsobjekte erstellen, anzeigen und bearbeiten: Pflanzen, Beläge, Landschaftsflächen, Geländemodelle, Geländemodifikationen, Höhenpunkte, Grundstücksgrenzen und vorhandene Bäume, einschließlich ihrer typisierten Einstellungen sowie Flächen- und Volumenangaben. Pfadbasierte Objekte werden anhand eines vorhandenen Polygons oder einer Polylinie erstellt. Jede Änderung wird als eigener benannter, rückgängig machbarer Vectorworks-Vorgang ausgeführt.

| Werkzeug | Auswirkung | Risiko | Zusammenfassung |
|---|---|---|---|
| [`createPlant`](#createplant) | Bearbeitung | mittel | Erstellt eine Pflanze an einem Punkt oder entlang eines Pfads. |
| [`createHardscape`](#createhardscape) | Bearbeitung | mittel | Erstellt einen Belag aus einem 2D-Pfadobjekt. |
| [`createLandscapeArea`](#createlandscapearea) | Bearbeitung | mittel | Erstellt eine Landschaftsfläche aus einem 2D-Pfadobjekt. |
| [`createSiteModifier`](#createsitemodifier) | Bearbeitung | mittel | Erstellt eine Geländemodifikation aus einem 2D-Pfadobjekt. |
| [`createPropertyLine`](#createpropertyline) | Bearbeitung | mittel | Erstellt eine Grundstücksgrenze aus einem geschlossenen 2D-Pfadobjekt. |
| [`createSiteModel`](#createsitemodel) | Bearbeitung | mittel | Erstellt ein leeres Geländemodell. |
| [`createStake`](#createstake) | Bearbeitung | mittel | Erstellt einen Höhenpunkt. |
| [`createExistingTree`](#createexistingtree) | Bearbeitung | mittel | Erstellt einen vorhandenen Baum. |
| [`getLandmarkObject`](#getlandmarkobject) | Nur lesend | niedrig | Liest die Eigenschaften eines Grundstücks- oder Landschaftsobjekts aus. |
| [`setLandmarkObject`](#setlandmarkobject) | Bearbeitung | mittel | Bearbeitet ein Grundstücks- oder Landschaftsobjekt. |

### createPlant

Erstellt eine Pflanze an einem Punkt oder entlang eines Pfads.

> **Auswirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: createPlant“ · **In runToolBatch:** ja

**Details**

Erstellt eine Pflanze an `position` (oder verteilt Pflanzen entlang von `pathUuid`). Der optionale Wert `plantResource` gibt den Pflanzenstil (eine Symboldefinition) an, der verwendet werden soll; befindet er sich noch nicht in der Zeichnung, wird er aus dem Vectorworks-Pflanzeninhalt importiert. Wird er ausgelassen oder nicht gefunden, wird der erste verfügbare Pflanzenstil verwendet. Der tatsächlich angewendete Stil wird als `plantStyle` zurückgegeben. Optional sind `latinName`, `commonName`, `spread` und `height`.

Die optionalen Werte `config` (mit `pathUuid`: plantsAtPolyVertices, plantsAlongPolyEdges, plantsInRectangularArray oder plantsInTriangularArray), `spacing` (Abstand zwischen den Pflanzen), `plantID`, `comments`, `tagDisplay` und `show3DDetail` werden wie bei `setLandmarkObject` festgelegt und in `applied` gemeldet.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) |  | Einfügepunkt. |
| `pathUuid` | string |  | UUID des Objekts, das den Pfad bereitstellt. |
| `plantResource` | string |  | Name des zu verwendenden Pflanzenstils (einer Symboldefinition); wird bei Bedarf aus dem Pflanzeninhalt importiert. |
| `latinName` | string |  | Botanischer Name. |
| `commonName` | string |  | Gebräuchlicher Name. |
| `spread` | number |  | Kronendurchmesser (Ausdehnung). |
| `height` | number |  | Höhe in Welteinheiten. |
| `plantID` | string |  | Identifiziert die Pflanzenart. |
| `comments` | string |  |  |
| `config` | string |  | Einer von: `singlePlant`, `plantsAtPolyVertices`, `plantsAlongPolyEdges`, `plantsInRectangularArray`, `plantsInTriangularArray`. |
| `tagDisplay` | string |  | Einer von: `none`, `left`, `right`, `floating`. |
| `show3DDetail` | boolean |  |  |
| `spacing` | number |  | Abstand zwischen den Pflanzen. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `plantStyle` | Name des verwendeten Pflanzenstils. Kann von `plantResource` abweichen. |
| `applied` | Für jedes angegebene und geschriebene Feld aus `config`, `spacing`, `plantID`, `comments`, `tagDisplay` und `show3DDetail` `true`, andernfalls `false`. Wird ausgelassen, wenn keines angegeben wurde. |


### createHardscape

Erstellt einen Belag aus einem 2D-Pfadobjekt.

> **Auswirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: createHardscape“ · **In runToolBatch:** ja

**Details**

Erstellt einen Belag (befestigte Fläche) aus einem vorhandenen 2D-Pfadobjekt, angegeben durch `pathUuid`. Die optionalen Werte `mode3D`, `draw3D`, `isSiteModifier`, `isPathway` mit `pathwayWidth` / `pathwayOffset` (ein Streifen fester Breite entlang des Pfads), `useBorder`, `borderWidth`, `borderThickness` und `slabThickness` werden wie bei `setLandmarkObject` festgelegt und in `applied` gemeldet.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `pathUuid` | string | Ja | UUID des Objekts, das den Pfad bereitstellt. |
| `mode3D` | string |  | Einer von: `none`, `slab`, `padUnder`, `padOver`, `textureBed`, `slabDrainage`, `alignedSlab`, `alignedModifOver`, `alignedModifUnder`. |
| `draw3D` | boolean |  |  |
| `isSiteModifier` | boolean |  |  |
| `isPathway` | boolean |  | Durchgehender Streifen mit fester Breite entlang des Pfads. |
| `useBorder` | boolean |  |  |
| `slabThickness` | number |  |  |
| `borderThickness` | number |  |  |
| `borderWidth` | number |  |  |
| `pathwayWidth` | number |  |  |
| `pathwayOffset` | number |  |  |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene und geschriebene Feld aus `mode3D`, `draw3D`, `isSiteModifier`, `isPathway`, `useBorder`, `slabThickness`, `borderThickness`, `borderWidth`, `pathwayWidth` und `pathwayOffset` `true`, andernfalls `false`. Wird ausgelassen, wenn keines angegeben wurde. |


### createLandscapeArea

Erstellt eine Landschaftsfläche aus einem 2D-Pfadobjekt.

> **Auswirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: createLandscapeArea“ · **In runToolBatch:** ja

**Details**

Erstellt eine Landschaftsfläche (bepflanzter Bereich) aus einem vorhandenen 2D-Pfadobjekt, angegeben durch `pathUuid`. Die optionalen Werte `id`, `description`, `drawingMode`, `areaUnits` und `plantDisplay2D` (oder die Kompatibilitätsoption `showPlantsIn2D`) werden wie bei `setLandmarkObject` festgelegt und in `applied` gemeldet.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `pathUuid` | string | Ja | UUID des Objekts, das den Pfad bereitstellt. |
| `id` | string |  | ID der Landschaftsfläche (Text). |
| `description` | string |  | Beschreibungstext. |
| `drawingMode` | string |  | Einer von: `landscapeArea`, `hedgerow`. |
| `areaUnits` | string |  | Einer von: `sqFeet`, `sqMeters`, `acres`, `hectares`, `documentUnits`. |
| `showPlantsIn2D` | boolean |  | Kompatibilitätsform von `plantDisplay2D`: `true` wählt `plantSymbols`, `false` wählt `none`. Nicht beide Werte angeben. |
| `plantDisplay2D` | string |  | Einer von: `none`, `plantCloud`, `plantLine`, `plantSymbols`. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene und geschriebene Feld aus `id`, `description`, `drawingMode`, `areaUnits`, `plantDisplay2D` und `showPlantsIn2D` `true`, andernfalls `false` (bei gemeinsamer Angabe melden beide Anzeigeeigenschaften `false`). Wird ausgelassen, wenn keines angegeben wurde. |


### createSiteModifier

Erstellt eine Geländemodifikation aus einem 2D-Pfadobjekt.

> **Auswirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: createSiteModifier“ · **In runToolBatch:** ja

**Details**

Erstellt eine Geländemodifikation aus einem vorhandenen 2D-Pfadobjekt, angegeben durch `pathUuid`. Die optionalen Werte `config` (z. B. pad, gradeLimits), `applyTo`, `show3D`, `retainSlopeInside` und `simplificationTolerance` werden wie bei `setLandmarkObject` festgelegt und in `applied` gemeldet.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `pathUuid` | string | Ja | UUID des Objekts, das den Pfad bereitstellt. |
| `config` | string |  | Einer von: `gradeLimits`, `contour`, `pad`, `retainingPad`, `aligned`, `path`, `fitToObjects`, `textureBed`, `spoilPile`. |
| `applyTo` | string |  | Einer von: `existing`, `proposed`. |
| `show3D` | boolean |  |  |
| `retainSlopeInside` | boolean |  |  |
| `simplificationTolerance` | number |  |  |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene und geschriebene Feld aus `config`, `applyTo`, `show3D`, `retainSlopeInside` und `simplificationTolerance` `true`, andernfalls `false`. Wird ausgelassen, wenn keines angegeben wurde. |


### createPropertyLine

Erstellt eine Grundstücksgrenze aus einem geschlossenen 2D-Pfadobjekt.

> **Auswirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: createPropertyLine“ · **In runToolBatch:** ja

**Details**

Erstellt eine Grundstücksgrenze (Parzellengrenze) aus einem vorhandenen geschlossenen 2D-Pfadobjekt, angegeben durch `pathUuid`. Die optionalen Werte `showName`, `showNumber`, `showArea`, `areaUnitsImperial`, `areaUnitsMetric` und `distanceUnits` werden wie bei `setLandmarkObject` festgelegt und in `applied` gemeldet.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `pathUuid` | string | Ja | UUID des Objekts, das den Pfad bereitstellt. |
| `showName` | boolean |  |  |
| `showNumber` | boolean |  |  |
| `showArea` | boolean |  |  |
| `areaUnitsImperial` | string |  | Einer von: `documentUnits`, `squareFeet`, `squareYards`, `squareMiles`, `acres`, `squareMeters`, `squareKilometers`, `hectares`. |
| `areaUnitsMetric` | string |  | Einer von: `documentUnits`, `squareFeet`, `squareYards`, `squareMiles`, `acres`, `squareMeters`, `squareKilometers`, `hectares`. |
| `distanceUnits` | string |  | Einer von: `Document Units`, `Feet & Inches`, `Inches`, `Feet`, `Yards`, `Miles`, `Microns`, `Millimeters`, `Centimeters`, `Meters`, `Kilometers`. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene und geschriebene Feld aus `showName`, `showNumber`, `showArea`, `areaUnitsImperial`, `areaUnitsMetric` und `distanceUnits` `true`, andernfalls `false`. Wird ausgelassen, wenn keines angegeben wurde. |


### createSiteModel

Erstellt ein leeres Geländemodell.

> **Auswirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: createSiteModel“ · **In runToolBatch:** ja

**Details**

Erstellt ein (leeres) Geländemodell-/Geländeobjekt an `position`; füge anschließend Vermessungsdaten oder Landmark-Befehle hinzu. Die optionalen Werte `display2D`, `display3D`, `style2D`, `style3D`, `geometryZReference` und `showErrors` werden wie bei `setLandmarkObject` festgelegt und in `applied` gemeldet.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `display2D` | string |  | Einer von: `existingOnly`, `proposedOnly`, `existingAndProposed`. |
| `display3D` | string |  | Einer von: `nothing`, `existingOnly`, `proposedOnly`, `cutAndFill`. |
| `style2D` | string |  | Einer von: `k2DTINStyle2DContour`, `k2DTINStyle2DContourSmoothed`, `k2DTINStyle2DContourColoredElevations`, `k2DTINStyle2DTriangulatedContoursColoredSlopes`, `k2DTINStyle2DTriangles`, `k2DTINStyle2DTrianglesColoredSlopes`. |
| `style3D` | string |  | Einer von: `k3DTINStyleMesh`, `k3DTINStyleMeshColoredElev`, `k3DTINStyleMeshColoredSlopes`, `k3DTINStyleGrid`, `k3DTINStyleGridColoredElev`, `k3DTINStyleGridColoredSlope`, `k3DTINStyleVerticalGrid`, `k3DTINStyleContour`, `k3DTINStyleExtrudedContour`, `k3DTINStyleExtContColoredElev`. |
| `geometryZReference` | number |  | Bezugshöhe für Höhenlinien. |
| `showErrors` | boolean |  |  |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene und geschriebene Feld aus `display2D`, `display3D`, `style2D`, `style3D`, `geometryZReference` und `showErrors` `true`, andernfalls `false`. Wird ausgelassen, wenn keines angegeben wurde. |


### createStake

Erstellt einen Höhenpunkt.

> **Auswirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: createStake“ · **In runToolBatch:** ja

**Details**

Erstellt an `position` einen Höhenpunkt mit optionaler Höhe `z` und Beschriftung `data`. Die optionalen Werte `mode`, `siteModel`, `id`, `idPrefix`, `idSuffix`, `labelReference`, `displayLeaderLine` und `showElevationMark` werden wie bei `setLandmarkObject` festgelegt und in `applied` gemeldet.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `z` | number |  | Z-Wert (Höhe) in Welteinheiten. |
| `data` | string |  | Beschriftungstext des Absteckpunkts (seine Beschreibung). |
| `mode` | string |  | Einer von: `siteModelSource`, `setToSiteModelGrade`, `setToCutSurface`, `setToObjectSpot`, `graphic2DOnly`, `siteModifierObject`. |
| `siteModel` | string |  | Einer von: `existing`, `proposed`. |
| `id` | integer |  | Ganzzahlige ID des Absteckpunkts. Eine ganze Zahl oder eine numerische Zeichenfolge wie `"12"` wird geschrieben; andere Werte nicht (`false` in `applied`). |
| `idPrefix` | string |  |  |
| `idSuffix` | string |  |  |
| `labelReference` | string |  | Einer von: `ID`, `Elevation`, `Description`, `ID/Elevation`, `ID/Description`, `Description/Elevation`, `Stationing Data`, `Coordinate PointNE`, `Coordinate PointEN`, `Coordinate PointXY`, `Coordinate PointYX`, `Latitude/Longitude`, `Longitude/Latitude`, `Latitude/Longitude(WGS84)`, `Longitude/Latitude(WGS84)`, `No Label`, `Object Spot Height`. |
| `displayLeaderLine` | boolean |  |  |
| `showElevationMark` | boolean |  |  |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene und geschriebene Feld aus `mode`, `siteModel`, `id`, `idPrefix`, `idSuffix`, `labelReference`, `displayLeaderLine` und `showElevationMark` `true`, andernfalls `false`. Wird ausgelassen, wenn keines angegeben wurde. |


### createExistingTree

Erstellt einen vorhandenen Baum.

> **Auswirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: createExistingTree“ · **In runToolBatch:** ja

**Details**

Erstellt an `position` ein Objekt für einen vorhandenen Baum. Optional sind `botanicalName`, `commonName`, `height`, `canopyDiameter` und `caliper` (BHD). Die übrigen Eigenschaften des vorhandenen Baums aus `setLandmarkObject` (treeNumber, origin, Wurzelschutzzonendurchmesser, treeProtectionZone, condition, sule, significance, actionComment, location, notes, create3D) werden auf dieselbe Weise festgelegt und in `applied` gemeldet.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `position` | [Punkt](Common.md#punkte) | Ja | Einfügepunkt. |
| `botanicalName` | string |  |  |
| `commonName` | string |  |  |
| `height` | number |  | Höhe in Welteinheiten. |
| `canopyDiameter` | number |  |  |
| `caliper` | number |  | Stammdurchmesser (BHD). |
| `treeNumber` | string |  |  |
| `origin` | string |  | Einer von: `notSet`, `endemic`, `native`, `exotic`, `indigenous`, `custom`. |
| `rootBallDiameter` | number |  |  |
| `criticalRootZoneDiameter` | number |  |  |
| `primaryRootZoneDiameter` | number |  |  |
| `treeProtectionZone` | string |  | Einer von: `none`, `circularZone`, `using12DBH`. |
| `condition` | string |  | Einer von: `notSet`, `excellent`, `good`, `average`, `poor`, `custom`. |
| `sule` | string |  | Einer von: `notSet`, `long`, `medium`, `short`, `removal`, `custom`. |
| `significance` | string |  | Einer von: `notSet`, `mostSignificant`, `highlySignificant`, `lessSignificant`, `leastSignificant`, `hazardous`, `custom`. |
| `actionComment` | string |  | Einer von: `notSet`, `retain`, `retainArborist`, `transplantOriginal`, `transplantProposed`, `remove`, `removeBuildingFootprint`, `removePoorHealth`, `removeSpecies`, `custom`. |
| `location` | string |  |  |
| `notes` | string |  |  |
| `create3D` | boolean |  | Derzeit nicht geschrieben: `applied.create3D` ist immer `false`. |
| `class` | string |  | Erstellungsoption: Klasse des neuen Objekts; wird bei Bedarf erstellt. Siehe [Erstellungsoptionen](Common.md#optionen-zur-erstellung). |
| `name` | string |  | Erstellungsoption: Name des neuen Objekts. |
| `select` | boolean |  | Erstellungsoption: Neues Objekt auswählen. |
| `useClassAttributes` | boolean |  | Erstellungsoption: Mit `class` auch die Attribute des neuen Objekts anhand der Klasse festlegen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene und geschriebene Feld aus `treeNumber`, `origin`, `rootBallDiameter`, `criticalRootZoneDiameter`, `primaryRootZoneDiameter`, `treeProtectionZone`, `condition`, `sule`, `significance`, `actionComment`, `location` und `notes` `true`, andernfalls `false`; `create3D` ist immer `false`. Wird ausgelassen, wenn keines angegeben wurde. |


### getLandmarkObject

Liest die Eigenschaften eines Grundstücks- oder Landschaftsobjekts aus.

> **Auswirkung:** Nur lesend · **Risiko:** niedrig · **Rückgängig:** keiner · **In runToolBatch:** zulässig

**Details**

Liest die typisierten Eigenschaften einer Pflanze, eines Belags, einer Landschaftsfläche, eines vorhandenen Baums, Höhenpunkts, einer Grundstücksgrenze, eines Geländemodells oder einer Geländemodifikation aus: `kind`, die Felder, die `setLandmarkObject` schreibt (bei einer Pflanze wird ihr Stil als `plantStyle` ausgegeben), sowie schreibgeschützte Werte – beim Belag `mainArea`, `borderArea`, `footprintArea` (m² im metrischen Maßsystem, ft² bei imperialen Dokumenten) und `perimeter`, `mainPerimeter`, `borderPerimeter` (Welteinheiten); bei einer Landschaftsfläche `area` (in `areaUnits`), `projectedArea` (auf das Geländemodell projiziert, ohne Geländemodell 0) und `numPlants`; bei einer Grundstücksgrenze `areaText` und `perimeterText`; beim Geländemodell `projectedAreaExisting`, `surfaceAreaExisting`, `surfaceAreaProposed`, `volumeExisting`, `volumeProposed`, `cutVolume` und `fillVolume` (formatierte Texte, bis zur Berechnung leer).

Pfadbasierte Objekte geben außerdem `pathObject` zurück, die Referenz auf ihren 2D-Pfad. Der optionale Parameter `params` listet Plug-in-Parameternamen auf (siehe `getObjectParameters`), deren typisierte Rohwerte ausgegeben werden sollen: Zahlen (Längen in Welteinheiten, Winkel in Grad), boolesche Werte oder Text.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Referenz über Namen. |
| `index` | integer |  | Referenz über internen Index. |
| `params` | array of string |  | Namen der Plug-in-Parameter, die mit typisierten Werten ausgegeben werden sollen. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `kind` | `Plant`, `Hardscape`, `LandscapeArea`, `ExistingTree`, `Stake`, `PropertyLine`, `SiteModel` oder `SiteModifier`. |
| Fields of the kind | The fields that `setLandmarkObject` writes for the kind, and the read-only values named in the Details. A value that cannot be read is left out. |
| `pathObject` | Objektreferenz des 2D-Pfads eines pfadbasierten Objekts. Wird für ein Objekt ohne Pfad ausgelassen. |
| `params` | Nur wenn `params` als Array angegeben wurde: Objekt, das jeden angefragten Namen seinem rohen typisierten Wert zuordnet. Nicht-textuelle Namen und Namen unbekannter Parameter werden ohne Fehler übersprungen. |


### setLandmarkObject

Bearbeitet ein Grundstücks- oder Landschaftsobjekt.

> **Auswirkung:** Bearbeitung · **Risiko:** mittel · **Rückgängig:** ein Schritt „MCP: setLandmarkObject“ · **In runToolBatch:** ja

**Details**

Bearbeitet ein Landmark-Objekt anhand der UUID. Gib die unten für den jeweiligen Typ aufgeführten Felder an (`getLandmarkObject` liest sie unter denselben Schlüsseln aus); `applied` meldet für jedes Feld, ob es geschrieben wurde (unbekannte Auswahlwerte werden abgelehnt).

**Pflanze:** `plantResource` (wechselt zu einem anderen Pflanzenstil und importiert ihn bei Bedarf; wird als `plantStyle` zurückgegeben), `latinName`, `commonName`, `plantID` (identifiziert die Art), `comments`, `spread` (Kronendurchmesser), `height`, `spacing` (Abstand zwischen Pflanzen entlang von Polylinienkanten oder in Arrays), `config`, `tagDisplay`, `show3DDetail`.

**Belag:** `id` (Text), `mode3D`, `draw3D`, `isSiteModifier`, `isPathway` (Streifen fester Breite entlang des Pfads) mit `pathwayWidth` / `pathwayOffset`, `useBorder`, `borderWidth`, `borderThickness`, `slabThickness`.

**Landschaftsfläche:** `name` (Flächenname, nicht Objektname), `id` (Text), `description`, `drawingMode`, `areaUnits`, `plantDisplay2D` (none, plantCloud, plantLine, plantSymbols). Die Kompatibilitätsoption `showPlantsIn2D` wird für jeden sichtbaren Modus als true ausgegeben; beim Schreiben wählt true `plantSymbols` und false `none`. Gib nicht beide Anzeigeeigenschaften an; werden beide angegeben, schlagen sie fehl.

**Vorhandener Baum:** `botanicalName`, `commonName`, `treeNumber`, `origin`, `height`, `canopyDiameter`, `caliper` (BHD), `rootBallDiameter`, `criticalRootZoneDiameter`, `primaryRootZoneDiameter`, `treeProtectionZone`, `condition`, `sule` (sichere Lebenserwartung), `significance`, `actionComment`, `location`, `notes`, `create3D`; bei einer Auswahl `custom` wird der Freitext des Parameters CustomOrigin / CustomCondition / CustomSULE / CustomSignificance / CustomAction verwendet (lege ihn mit `params` fest).

**Höhenpunkt:** `z` (Höhe), `data` (Beschreibung), `mode` (Funktion im Geländemodell), `siteModel` (Zieloberfläche), `id` (Ganzzahl), `idPrefix`, `idSuffix`, `labelReference` (Beschriftungsinhalt), `displayLeaderLine`, `showElevationMark`.

**Grundstücksgrenze:** `name`, `number`, `showName`, `showNumber`, `showArea`, `areaUnitsImperial` / `areaUnitsMetric` (Flächeneinheiten bei imperialen / metrischen Dokumenten), `distanceUnits` (Beschriftungen der Liniensegmente).

**Geländemodell:** `display2D` / `display3D` (angezeigte Oberflächen), `style2D`, `style3D`, `geometryZReference` (Bezugshöhe für Höhenlinien), `showErrors`.

**Geländemodifikation:** `config` (fitToObjects wird als aligned gespeichert), `applyTo` (beeinflusste Oberfläche), `show3D`, `retainSlopeInside`, `simplificationTolerance`. Längen werden in Welteinheiten angegeben; mögliche Werte sind im Schema aufgeführt. Ein Objekt `params` legt unveränderte Plug-in-Parameter fest.

**Parameter**

| Parameter | Typ | Erforderlich | Beschreibung |
|---|---|---|---|
| `uuid` | string |  | Referenz über UUID (bevorzugt). Siehe [Objektreferenzen](Common.md#objektreferenzen). |
| `name` | string |  | Verwendet für Landschaftsfläche (Flächenname, nicht Objektname) und Grundstücksgrenze. |
| `index` | integer |  | Referenz über internen Index. |
| `plantResource` | string |  | Für Pflanzen. Wechselt zu einem anderen Pflanzenstil und importiert ihn bei Bedarf; wird als `plantStyle` zurückgegeben. |
| `latinName` | string |  | Für Pflanzen. |
| `commonName` | string |  | Für Pflanzen und vorhandene Bäume. |
| `spread` | number |  | Für Pflanzen. Kronendurchmesser. |
| `height` | number |  | Für Pflanzen und vorhandene Bäume. Höhe in Welteinheiten. |
| `number` | string |  | Für Grundstücksgrenzen. |
| `botanicalName` | string |  | Für vorhandene Bäume. |
| `canopyDiameter` | number |  | Für vorhandene Bäume. |
| `caliper` | number |  | Für vorhandene Bäume. Stammdurchmesser (BHD). |
| `z` | number |  | Für Höhenpunkte. Z-Wert (Höhe) in Welteinheiten. |
| `data` | string |  | Für Höhenpunkte. Beschreibung. |
| `params` | object |  | Unveränderte Plug-in-Parameter `{ "ParamName": value }`. Siehe [Plug-in-Parameter](Common.md#plug-in-parameter). |
| `plantID` | string |  | Für Pflanzen. Identifiziert die Art. |
| `comments` | string |  | Für Pflanzen. |
| `config` | string |  | Für Pflanzen und Geländemodifikationen. Einer von: `singlePlant`, `plantsAtPolyVertices`, `plantsAlongPolyEdges`, `plantsInRectangularArray`, `plantsInTriangularArray`, `gradeLimits`, `contour`, `pad`, `retainingPad`, `aligned`, `path`, `fitToObjects`, `textureBed`, `spoilPile`. |
| `tagDisplay` | string |  | Für Pflanzen. Einer von: `none`, `left`, `right`, `floating`. |
| `show3DDetail` | boolean |  | Für Pflanzen. |
| `spacing` | number |  | Für Pflanzen. Abstand zwischen Pflanzen entlang von Polylinienkanten oder in Arrays. |
| `mode3D` | string |  | Für Beläge. Einer von: `none`, `slab`, `padUnder`, `padOver`, `textureBed`, `slabDrainage`, `alignedSlab`, `alignedModifOver`, `alignedModifUnder`. |
| `draw3D` | boolean |  | Für Beläge. |
| `isSiteModifier` | boolean |  | Für Beläge. |
| `isPathway` | boolean |  | Für Beläge. Streifen fester Breite entlang des Pfads. |
| `useBorder` | boolean |  | Für Beläge. |
| `slabThickness` | number |  | Für Beläge. |
| `borderThickness` | number |  | Für Beläge. |
| `borderWidth` | number |  | Für Beläge. |
| `pathwayWidth` | number |  | Für Beläge. |
| `pathwayOffset` | number |  | Für Beläge. |
| `id` | string or integer |  | Für Beläge, Landschaftsflächen und Höhenpunkte. |
| `description` | string |  | Für Landschaftsflächen und Höhenpunkte. Beschreibungstext. |
| `drawingMode` | string |  | Für Landschaftsflächen. Einer von: `landscapeArea`, `hedgerow`. |
| `areaUnits` | string |  | Für Landschaftsflächen. Einer von: `sqFeet`, `sqMeters`, `acres`, `hectares`, `documentUnits`. |
| `showPlantsIn2D` | boolean |  | Für Landschaftsflächen verwendet. Kompatibilitätsform von `plantDisplay2D`: `true` wählt `plantSymbols`, `false` wählt `none`. Nicht beide angeben: Beide werden mit `false` gemeldet und keiner wird geschrieben. |
| `plantDisplay2D` | string |  | Für Landschaftsflächen. Einer von: `none`, `plantCloud`, `plantLine`, `plantSymbols`. |
| `treeNumber` | string |  | Für vorhandene Bäume. |
| `origin` | string |  | Für vorhandene Bäume. Einer von: `notSet`, `endemic`, `native`, `exotic`, `indigenous`, `custom`. |
| `rootBallDiameter` | number |  | Für vorhandene Bäume. |
| `criticalRootZoneDiameter` | number |  | Für vorhandene Bäume. |
| `primaryRootZoneDiameter` | number |  | Für vorhandene Bäume. |
| `treeProtectionZone` | string |  | Für vorhandene Bäume. Einer von: `none`, `circularZone`, `using12DBH`. |
| `condition` | string |  | Für vorhandene Bäume. Einer von: `notSet`, `excellent`, `good`, `average`, `poor`, `custom`. |
| `sule` | string |  | Für vorhandene Bäume. Einer von: `notSet`, `long`, `medium`, `short`, `removal`, `custom`. |
| `significance` | string |  | Für vorhandene Bäume. Einer von: `notSet`, `mostSignificant`, `highlySignificant`, `lessSignificant`, `leastSignificant`, `hazardous`, `custom`. |
| `actionComment` | string |  | Für vorhandene Bäume. Einer von: `notSet`, `retain`, `retainArborist`, `transplantOriginal`, `transplantProposed`, `remove`, `removeBuildingFootprint`, `removePoorHealth`, `removeSpecies`, `custom`. |
| `location` | string |  | Für vorhandene Bäume. |
| `notes` | string |  | Für vorhandene Bäume. |
| `create3D` | boolean |  | Für vorhandene Bäume. |
| `mode` | string |  | Für Höhenpunkte. Einer von: `siteModelSource`, `setToSiteModelGrade`, `setToCutSurface`, `setToObjectSpot`, `graphic2DOnly`, `siteModifierObject`. |
| `siteModel` | string |  | Für Höhenpunkte. Einer von: `existing`, `proposed`. |
| `idPrefix` | string |  | Für Höhenpunkte. |
| `idSuffix` | string |  | Für Höhenpunkte. |
| `labelReference` | string |  | Für Höhenpunkte. Einer von: `ID`, `Elevation`, `Description`, `ID/Elevation`, `ID/Description`, `Description/Elevation`, `Stationing Data`, `Coordinate PointNE`, `Coordinate PointEN`, `Coordinate PointXY`, `Coordinate PointYX`, `Latitude/Longitude`, `Longitude/Latitude`, `Latitude/Longitude(WGS84)`, `Longitude/Latitude(WGS84)`, `No Label`, `Object Spot Height`. |
| `displayLeaderLine` | boolean |  | Für Höhenpunkte. |
| `showElevationMark` | boolean |  | Für Höhenpunkte. |
| `showName` | boolean |  | Für Grundstücksgrenzen. |
| `showNumber` | boolean |  | Für Grundstücksgrenzen. |
| `showArea` | boolean |  | Für Grundstücksgrenzen. |
| `areaUnitsImperial` | string |  | Für Grundstücksgrenzen. Einer von: `documentUnits`, `squareFeet`, `squareYards`, `squareMiles`, `acres`, `squareMeters`, `squareKilometers`, `hectares`. |
| `areaUnitsMetric` | string |  | Für Grundstücksgrenzen. Einer von: `documentUnits`, `squareFeet`, `squareYards`, `squareMiles`, `acres`, `squareMeters`, `squareKilometers`, `hectares`. |
| `distanceUnits` | string |  | Für Grundstücksgrenzen. Einer von: `Document Units`, `Feet & Inches`, `Inches`, `Feet`, `Yards`, `Miles`, `Microns`, `Millimeters`, `Centimeters`, `Meters`, `Kilometers`. |
| `display2D` | string |  | Für Geländemodelle. Einer von: `existingOnly`, `proposedOnly`, `existingAndProposed`. |
| `display3D` | string |  | Für Geländemodelle. Einer von: `nothing`, `existingOnly`, `proposedOnly`, `cutAndFill`. |
| `style2D` | string |  | Für Geländemodelle. Einer von: `k2DTINStyle2DContour`, `k2DTINStyle2DContourSmoothed`, `k2DTINStyle2DContourColoredElevations`, `k2DTINStyle2DTriangulatedContoursColoredSlopes`, `k2DTINStyle2DTriangles`, `k2DTINStyle2DTrianglesColoredSlopes`. |
| `style3D` | string |  | Für Geländemodelle. Einer von: `k3DTINStyleMesh`, `k3DTINStyleMeshColoredElev`, `k3DTINStyleMeshColoredSlopes`, `k3DTINStyleGrid`, `k3DTINStyleGridColoredElev`, `k3DTINStyleGridColoredSlope`, `k3DTINStyleVerticalGrid`, `k3DTINStyleContour`, `k3DTINStyleExtrudedContour`, `k3DTINStyleExtContColoredElev`. |
| `geometryZReference` | number |  | Für Geländemodelle. Bezugshöhe für Höhenlinien. |
| `showErrors` | boolean |  | Für Geländemodelle. |
| `applyTo` | string |  | Für Geländemodifikationen. Einer von: `existing`, `proposed`. |
| `show3D` | boolean |  | Für Geländemodifikationen. |
| `retainSlopeInside` | boolean |  | Für Geländemodifikationen. |
| `simplificationTolerance` | number |  | Für Geländemodifikationen. |

**Ergebnis**

| Schlüssel | Beschreibung |
|---|---|
| `applied` | Für jedes angegebene Feld: `true`, wenn das Feld geschrieben wurde, andernfalls `false`. |
| `applied.params` | Nur wenn `params` als Objekt angegeben wurde: für jeden Parameternamen `true`, wenn der Wert geschrieben wurde, andernfalls `false`. |
