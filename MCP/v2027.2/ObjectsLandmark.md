**English** • [Deutsch](../../MCP.de/v2027.2/ObjectsLandmark.md) • [日本語](../../MCP.ja/v2027.2/ObjectsLandmark.md)

# ObjectsLandmark — site and landscape

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools for site and landscape objects: plants, hardscapes, landscape areas, site models, site modifiers, stakes, property lines and existing trees.

## Table of contents

- [Overview](#overview)
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

## Overview

This folder holds 1 tool group with 10 tools in total.

| Group | Group ID | Active by default | Risk level | Tools | Summary |
|---|---|---|---|---|---|
| [Landmark](#landmark) | `landmark` | No | medium | 10 | Plants, hardscapes, landscape areas, site models, site modifiers, stakes, property lines and existing trees. |

## Landmark

> **Group:** `Landmark` · **Group ID:** `landmark` · **Active by default:** No · **Risk level:** medium · **Tools:** 10

**Plants, hardscapes, landscape areas, site models, site modifiers, stakes, property lines and existing trees.**

Create, inspect and edit site and landscape objects: plants, hardscapes, landscape areas, site models, site modifiers, stakes, property lines and existing trees, including their typed settings and area / volume readouts. Path-based objects are built from an existing polygon/polyline. Each change runs as its own named, undoable Vectorworks operation.

> **Note:** Lengths, heights and elevations are in world units. Points are in world units too (see [Points](Common.md#points)).
>
> **Note:** A successful `createPlant` with `pathUuid`, `createHardscape`, `createLandscapeArea`, `createSiteModifier` and `createPropertyLine` use up the source polygon or polyline: the new object takes it over, and `getLandmarkObject` reports it as `pathObject`. A call that fails early leaves the path as it was. To build several objects from one outline, duplicate the path first (see [`editObject`](ObjectPrimitives.md#editobject), action `duplicate`). Always give `pathUuid` to these tools: when it is missing, the four path-based tools look for the path with `uuid`, `name` or `index`, so the creation option `name` would pick the path object.
>
> **Note:** In the result of a create tool, `applied` holds only the typed properties that the tool describes as "set as by `setLandmarkObject`". The main arguments (`position`, `pathUuid`, `plantResource`, `latinName`, `commonName`, `spread`, `height`, `z`, `data`, `botanicalName`, `canopyDiameter`, `caliper`) and the creation options are written without an `applied` entry. `applied` is left out when no typed property was given. A main argument of the wrong JSON type (for example a numeric string for a number) is written as `0` or as an empty string, without an error; `setLandmarkObject` reports `true` for it.

| Tool | Effect | Risk | Summary |
|---|---|---|---|
| [`createPlant`](#createplant) | Edit | medium | Creates a plant at a point or along a path. |
| [`createHardscape`](#createhardscape) | Edit | medium | Creates a hardscape from a 2D path object. |
| [`createLandscapeArea`](#createlandscapearea) | Edit | medium | Creates a landscape area from a 2D path object. |
| [`createSiteModifier`](#createsitemodifier) | Edit | medium | Creates a site modifier from a 2D path object. |
| [`createPropertyLine`](#createpropertyline) | Edit | medium | Creates a property line from a closed 2D path object. |
| [`createSiteModel`](#createsitemodel) | Edit | medium | Creates an empty site model. |
| [`createStake`](#createstake) | Edit | medium | Creates a stake (elevation point). |
| [`createExistingTree`](#createexistingtree) | Edit | medium | Creates an existing tree. |
| [`getLandmarkObject`](#getlandmarkobject) | Read-only | low | Reads the properties of a site or landscape object. |
| [`setLandmarkObject`](#setlandmarkobject) | Edit | medium | Edits a site or landscape object. |

### createPlant

Creates a plant at a point or along a path.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createPlant" · **In runToolBatch:** yes

**Details**

Create a plant at `position` (or distributed along `pathUuid`). Optional `plantResource` names the Plant style (a symbol definition) to use; it is imported from the Vectorworks plant content when it is not in the drawing yet. When omitted or not found, the first available Plant style is used. The style actually applied is returned as `plantStyle`. Optional `latinName`, `commonName`, `spread`, `height`.

Optional `config` (with `pathUuid`: plantsAtPolyVertices, plantsAlongPolyEdges, plantsInRectangularArray or plantsInTriangularArray), `spacing` (distance between the plants), `plantID`, `comments`, `tagDisplay` and `show3DDetail` are set as by setLandmarkObject and reported in `applied`.

> **Note:** Without `position` and without `pathUuid` the plant is placed at the origin (0, 0). `pathUuid` wins when both are given. A successful call with `pathUuid` uses up the path object (see the note of the group), so duplicate it first to keep the outline.
>
> **Note:** An unknown `plantResource` is not rejected. The tool looks for a Plant style of that name in the drawing, then imports one of that name from the plant content (`plantStyles`, then `plantLibraries`). When nothing is found, it imports and uses the first Plant style of the content; the drawing's own Plant styles are not consulted in this fallback. With `plantResource` omitted, the first Plant style of the drawing is used, or else the first of the content. Read `plantStyle` in the result to see which style was used.
>
> **Note:** An unknown `pathUuid` is not reported as `path object not found`: the call fails with the "no plant style is available" error (see the result), which is misleading in this case.
>
> **Note:** `plantResource`, `latinName`, `commonName`, `spread` and `height` are written without an `applied` entry.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) |  | Insertion point, in world units. Ignored when `pathUuid` is given; defaults to the origin (0, 0) when neither is given. |
| `pathUuid` | string |  | UUID of the object that supplies the path. The path object is used up by the new plant. |
| `plantResource` | string |  | Name of the Plant style (a symbol definition) to use; imported from the plant content when needed. |
| `latinName` | string |  | Latin (botanical) name. |
| `commonName` | string |  | Common name. |
| `spread` | number |  | Canopy diameter (spread). |
| `height` | number |  | Height, in world units. |
| `plantID` | string |  | Identifies the species. |
| `comments` | string |  |  |
| `config` | string |  | One of: `singlePlant`, `plantsAtPolyVertices`, `plantsAlongPolyEdges`, `plantsInRectangularArray`, `plantsInTriangularArray`. |
| `tagDisplay` | string |  | One of: `none`, `left`, `right`, `floating`. |
| `show3DDetail` | boolean |  |  |
| `spacing` | number |  | Distance between the plants. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new plant (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `plantStyle` | Name of the Plant style that was used. It can differ from `plantResource`. |
| `applied` | `true` for each of `config`, `spacing`, `plantID`, `comments`, `tagDisplay` and `show3DDetail` that was given and written, `false` for one that was not written. Omitted when none was given. |

Errors: `failed to create plant: no plant style is available. …`, with `requestedStyle` (only when `plantResource` was given) and `symbolDefinitionsFound` (the numbers of symbol definitions in the drawing and in the content folders `plantStyles` and `plantLibraries`). A failed call is rolled back (`rolledBack`), so no plant remains.

### createHardscape

Creates a hardscape from a 2D path object.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createHardscape" · **In runToolBatch:** yes

**Details**

Create a hardscape (paved surface) from an existing 2D path object given by `pathUuid`. Optional `mode3D`, `draw3D`, `isSiteModifier`, `isPathway` with `pathwayWidth` / `pathwayOffset` (a fixed-width strip along the path), `useBorder`, `borderWidth`, `borderThickness` and `slabThickness` are set as by setLandmarkObject and reported in `applied`.

> **Note:** A successful call uses up the path object (see the note of the group). The hardscape `id` is not set at creation: use `setLandmarkObject` for it. The creation option `name` sets only the Vectorworks object name.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pathUuid` | string | Yes | UUID of the object that supplies the path. The path object is used up by the new hardscape. |
| `mode3D` | string |  | One of: `none`, `slab`, `padUnder`, `padOver`, `textureBed`, `slabDrainage`, `alignedSlab`, `alignedModifOver`, `alignedModifUnder`. |
| `draw3D` | boolean |  |  |
| `isSiteModifier` | boolean |  |  |
| `isPathway` | boolean |  | Fixed-width strip along the path. |
| `useBorder` | boolean |  |  |
| `slabThickness` | number |  |  |
| `borderThickness` | number |  |  |
| `borderWidth` | number |  |  |
| `pathwayWidth` | number |  |  |
| `pathwayOffset` | number |  |  |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new hardscape (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | `true` for each of `mode3D`, `draw3D`, `isSiteModifier`, `isPathway`, `useBorder`, `slabThickness`, `borderThickness`, `borderWidth`, `pathwayWidth` and `pathwayOffset` that was given and written, `false` for one that was not written. Omitted when none was given. |

Errors: `path object not found (provide 'pathUuid' of a polygon/polyline)`; `failed to create object`. A failed call is rolled back (`rolledBack`), so no hardscape remains.

### createLandscapeArea

Creates a landscape area from a 2D path object.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createLandscapeArea" · **In runToolBatch:** yes

**Details**

Create a landscape area (planted region) from an existing 2D path object given by `pathUuid`. Optional `id`, `description`, `drawingMode`, `areaUnits` and `plantDisplay2D` (or compatibility `showPlantsIn2D`) are set as by setLandmarkObject and reported in `applied`.

> **Note:** A successful call uses up the path object (see the note of the group). The area name is not set at creation: the creation option `name` sets only the Vectorworks object name, so use `setLandmarkObject` with the `uuid` of the new object and `name` to set the area name.
>
> **Note:** Do not give `showPlantsIn2D` together with `plantDisplay2D`: both report `false` in `applied` and neither is written.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pathUuid` | string | Yes | UUID of the object that supplies the path. The path object is used up by the new landscape area. |
| `id` | string |  | ID of the landscape area (text). |
| `description` | string |  | Description text. |
| `drawingMode` | string |  | One of: `landscapeArea`, `hedgerow`. |
| `areaUnits` | string |  | One of: `sqFeet`, `sqMeters`, `acres`, `hectares`, `documentUnits`. |
| `showPlantsIn2D` | boolean |  | Compatibility form of `plantDisplay2D`: `true` selects `plantSymbols`, `false` selects `none`. Do not give both. |
| `plantDisplay2D` | string |  | One of: `none`, `plantCloud`, `plantLine`, `plantSymbols`. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new landscape area (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | `true` for each of `id`, `description`, `drawingMode`, `areaUnits`, `plantDisplay2D` and `showPlantsIn2D` that was given and written, `false` for one that was not written (both display properties report `false` when they are given together). Omitted when none was given. |

Errors: `path object not found (provide 'pathUuid' of a polygon/polyline)`; `failed to create object`. A failed call is rolled back (`rolledBack`), so no landscape area remains.

### createSiteModifier

Creates a site modifier from a 2D path object.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createSiteModifier" · **In runToolBatch:** yes

**Details**

Create a site modifier from an existing 2D path object given by `pathUuid`. Optional `config` (e.g. pad, gradeLimits), `applyTo`, `show3D`, `retainSlopeInside` and `simplificationTolerance` are set as by setLandmarkObject and reported in `applied`.

> **Note:** A successful call uses up the path object (see the note of the group).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pathUuid` | string | Yes | UUID of the object that supplies the path. The path object is used up by the new site modifier. |
| `config` | string |  | One of: `gradeLimits`, `contour`, `pad`, `retainingPad`, `aligned`, `path`, `fitToObjects`, `textureBed`, `spoilPile`. |
| `applyTo` | string |  | One of: `existing`, `proposed`. |
| `show3D` | boolean |  |  |
| `retainSlopeInside` | boolean |  |  |
| `simplificationTolerance` | number |  |  |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new site modifier (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | `true` for each of `config`, `applyTo`, `show3D`, `retainSlopeInside` and `simplificationTolerance` that was given and written, `false` for one that was not written. Omitted when none was given. |

Errors: `path object not found (provide 'pathUuid' of a polygon/polyline)`; `failed to create object`. A failed call is rolled back (`rolledBack`), so no site modifier remains.

### createPropertyLine

Creates a property line from a closed 2D path object.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createPropertyLine" · **In runToolBatch:** yes

**Details**

Create a property line (parcel boundary) from an existing closed 2D path object given by `pathUuid`. Optional `showName`, `showNumber`, `showArea`, `areaUnitsImperial`, `areaUnitsMetric` and `distanceUnits` are set as by setLandmarkObject and reported in `applied`.

> **Note:** A successful call uses up the path object (see the note of the group). The tool does not check that the path is closed. The parcel name and number are not set at creation: the creation option `name` sets only the Vectorworks object name, so use `setLandmarkObject` with the `uuid` of the new object and `name` and `number`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pathUuid` | string | Yes | UUID of the object that supplies the path. The path object is used up by the new property line. |
| `showName` | boolean |  |  |
| `showNumber` | boolean |  |  |
| `showArea` | boolean |  |  |
| `areaUnitsImperial` | string |  | One of: `documentUnits`, `squareFeet`, `squareYards`, `squareMiles`, `acres`, `squareMeters`, `squareKilometers`, `hectares`. |
| `areaUnitsMetric` | string |  | One of: `documentUnits`, `squareFeet`, `squareYards`, `squareMiles`, `acres`, `squareMeters`, `squareKilometers`, `hectares`. |
| `distanceUnits` | string |  | One of: `Document Units`, `Feet & Inches`, `Inches`, `Feet`, `Yards`, `Miles`, `Microns`, `Millimeters`, `Centimeters`, `Meters`, `Kilometers`. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new property line (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | `true` for each of `showName`, `showNumber`, `showArea`, `areaUnitsImperial`, `areaUnitsMetric` and `distanceUnits` that was given and written, `false` for one that was not written. Omitted when none was given. |

Errors: `path object not found (provide 'pathUuid' of a polygon/polyline)`; `failed to create object`. A failed call is rolled back (`rolledBack`), so no property line remains.

### createSiteModel

Creates an empty site model.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createSiteModel" · **In runToolBatch:** yes

**Details**

Create an (empty) site model / terrain object at `position`; populate it afterwards with survey data or the Landmark commands. Optional `display2D`, `display3D`, `style2D`, `style3D`, `geometryZReference` and `showErrors` are set as by setLandmarkObject and reported in `applied`.

> **Note:** `position` is marked required, but the tool does not enforce it: when it is missing or is not a point, the site model is placed at the origin (0, 0).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point, in world units. |
| `display2D` | string |  | One of: `existingOnly`, `proposedOnly`, `existingAndProposed`. |
| `display3D` | string |  | One of: `nothing`, `existingOnly`, `proposedOnly`, `cutAndFill`. |
| `style2D` | string |  | One of: `k2DTINStyle2DContour`, `k2DTINStyle2DContourSmoothed`, `k2DTINStyle2DContourColoredElevations`, `k2DTINStyle2DTriangulatedContoursColoredSlopes`, `k2DTINStyle2DTriangles`, `k2DTINStyle2DTrianglesColoredSlopes`. |
| `style3D` | string |  | One of: `k3DTINStyleMesh`, `k3DTINStyleMeshColoredElev`, `k3DTINStyleMeshColoredSlopes`, `k3DTINStyleGrid`, `k3DTINStyleGridColoredElev`, `k3DTINStyleGridColoredSlope`, `k3DTINStyleVerticalGrid`, `k3DTINStyleContour`, `k3DTINStyleExtrudedContour`, `k3DTINStyleExtContColoredElev`. |
| `geometryZReference` | number |  | Reference elevation for contours. |
| `showErrors` | boolean |  |  |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new site model (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | `true` for each of `display2D`, `display3D`, `style2D`, `style3D`, `geometryZReference` and `showErrors` that was given and written, `false` for one that was not written. Omitted when none was given. |

Errors: `failed to create object`. A failed call is rolled back (`rolledBack`), so no site model remains.

### createStake

Creates a stake (elevation point).

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createStake" · **In runToolBatch:** yes

**Details**

Create a stake (elevation point) at `position` with optional elevation `z` and label `data`. Optional `mode`, `siteModel`, `id`, `idPrefix`, `idSuffix`, `labelReference`, `displayLeaderLine` and `showElevationMark` are set as by setLandmarkObject and reported in `applied`.

> **Note:** `position` is marked required, but the tool does not enforce it: when it is missing or is not a point, the stake is placed at (0, 0). `z` defaults to 0. `z` and `data` are written without an `applied` entry.
>
> **Note:** `data` is the description (label text) of the stake. The argument `description` is read only for landscape areas.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point, in world units. |
| `z` | number |  | Z value (height), in world units. Defaults to 0. |
| `data` | string |  | Label text of the stake (its description). |
| `mode` | string |  | One of: `siteModelSource`, `setToSiteModelGrade`, `setToCutSurface`, `setToObjectSpot`, `graphic2DOnly`, `siteModifierObject`. |
| `siteModel` | string |  | One of: `existing`, `proposed`. |
| `id` | integer |  | Integer ID of the stake. A whole number or a numeric string such as `"12"` is written; another value is not (`false` in `applied`). |
| `idPrefix` | string |  |  |
| `idSuffix` | string |  |  |
| `labelReference` | string |  | One of: `ID`, `Elevation`, `Description`, `ID/Elevation`, `ID/Description`, `Description/Elevation`, `Stationing Data`, `Coordinate PointNE`, `Coordinate PointEN`, `Coordinate PointXY`, `Coordinate PointYX`, `Latitude/Longitude`, `Longitude/Latitude`, `Latitude/Longitude(WGS84)`, `Longitude/Latitude(WGS84)`, `No Label`, `Object Spot Height`. |
| `displayLeaderLine` | boolean |  |  |
| `showElevationMark` | boolean |  |  |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new stake (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | `true` for each of `mode`, `siteModel`, `id`, `idPrefix`, `idSuffix`, `labelReference`, `displayLeaderLine` and `showElevationMark` that was given and written, `false` for one that was not written. Omitted when none was given. |

Errors: `failed to create stake`. A failed call is rolled back (`rolledBack`), so no stake remains.

### createExistingTree

Creates an existing tree.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createExistingTree" · **In runToolBatch:** yes

**Details**

Create an existing-tree object at `position`. Optional `botanicalName`, `commonName`, `height`, `canopyDiameter`, `caliper` (DBH). The other existing-tree properties of setLandmarkObject (treeNumber, origin, the root zone diameters, treeProtectionZone, condition, sule, significance, actionComment, location, notes, create3D) are set the same way and reported in `applied`.

> **Note:** `position` is marked required, but the tool does not enforce it: when it is missing or is not a point, the tree is placed at (0, 0). `botanicalName`, `commonName`, `height`, `canopyDiameter` and `caliper` are written without an `applied` entry.
>
> **Note:** At present `create3D` is not written: `applied.create3D` is always `false`, and `getLandmarkObject` does not return `create3D`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point, in world units. |
| `botanicalName` | string |  |  |
| `commonName` | string |  |  |
| `height` | number |  | Height, in world units. |
| `canopyDiameter` | number |  |  |
| `caliper` | number |  | Trunk diameter (DBH). |
| `treeNumber` | string |  |  |
| `origin` | string |  | One of: `notSet`, `endemic`, `native`, `exotic`, `indigenous`, `custom`. |
| `rootBallDiameter` | number |  |  |
| `criticalRootZoneDiameter` | number |  |  |
| `primaryRootZoneDiameter` | number |  |  |
| `treeProtectionZone` | string |  | One of: `none`, `circularZone`, `using12DBH`. |
| `condition` | string |  | One of: `notSet`, `excellent`, `good`, `average`, `poor`, `custom`. |
| `sule` | string |  | One of: `notSet`, `long`, `medium`, `short`, `removal`, `custom`. |
| `significance` | string |  | One of: `notSet`, `mostSignificant`, `highlySignificant`, `lessSignificant`, `leastSignificant`, `hazardous`, `custom`. |
| `actionComment` | string |  | One of: `notSet`, `retain`, `retainArborist`, `transplantOriginal`, `transplantProposed`, `remove`, `removeBuildingFootprint`, `removePoorHealth`, `removeSpecies`, `custom`. |
| `location` | string |  |  |
| `notes` | string |  |  |
| `create3D` | boolean |  | Not written at present: `applied.create3D` is always `false`. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new existing tree (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | `true` for each of `treeNumber`, `origin`, `rootBallDiameter`, `criticalRootZoneDiameter`, `primaryRootZoneDiameter`, `treeProtectionZone`, `condition`, `sule`, `significance`, `actionComment`, `location` and `notes` that was given and written, `false` for one that was not written; `create3D` is always `false`. Omitted when none was given. |

Errors: `failed to create existing tree`. A failed call is rolled back (`rolledBack`), so no existing tree remains.

### getLandmarkObject

Reads the properties of a site or landscape object.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the typed properties of a plant, hardscape, landscape area, existing tree, stake, property line, site model or site modifier: `kind`, the fields setLandmarkObject writes (a plant reports its style as `plantStyle`) and read-only values - hardscape mainArea, borderArea, footprintArea (sq m in metric, sq ft in imperial documents) and perimeter, mainPerimeter, borderPerimeter (world units); landscape area `area` (in its areaUnits), projectedArea (onto the site model, 0 without one) and numPlants; property line areaText and perimeterText; site model projectedAreaExisting, surfaceAreaExisting, surfaceAreaProposed, volumeExisting, volumeProposed, cutVolume and fillVolume (formatted texts, empty until computed).

Path-based objects also return `pathObject`, the reference of their 2D path. Optional `params` lists plug-in parameter names (see getObjectParameters) to return as raw typed values: numbers (lengths in world units, angles in degrees), booleans or text.

> **Note:** For a landscape area and a property line, `name` is the area name or the parcel name, not the Vectorworks object name: it replaces the `name` of the object reference, also when it is empty. For an existing tree, `create3D` is never returned.
>
> **Note:** The description above says that `area` is in `areaUnits` and that `projectedArea` is 0 without a site model. The plug-in stores both values in square millimeters, and without a site model `projectedArea` is the plan area of the path. For a value in the area units, ask for the plug-in parameters `SurfaceAreaInLAUnits` and `ProjectedAreaInLAUnits` with `params`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `params` | array of string |  | Names of plug-in parameters to return with typed values. See [Plug-in parameters](Common.md#plug-in-parameters). |

**Result**

The object reference of the object (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `kind` | `Plant`, `Hardscape`, `LandscapeArea`, `ExistingTree`, `Stake`, `PropertyLine`, `SiteModel` or `SiteModifier`. |
| Fields of the kind | The fields that `setLandmarkObject` writes for the kind, and the read-only values named in the Details. A value that cannot be read is left out. |
| `pathObject` | Object reference of the 2D path of a path-based object. Left out for an object without a path. |
| `params` | Only when `params` was given as an array: an object that maps each requested name to its raw typed value. A name that is not text and the name of an unknown parameter are skipped without an error. |

Errors: `object not found`; `not a landmark object`.

### setLandmarkObject

Edits a site or landscape object.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: setLandmarkObject" · **In runToolBatch:** yes

**Details**

Edit a landmark object by uuid. Provide the fields of its kind listed below (getLandmarkObject reads them under the same keys); `applied` reports per field whether it was written (unknown choices are rejected).

**Plant:** plantResource (switches to another Plant style, importing it if needed; read back as `plantStyle`), latinName, commonName, plantID (identifies the species), comments, spread (canopy diameter), height, spacing (distance between plants along poly edges or in arrays), config, tagDisplay, show3DDetail.

**Hardscape:** id (text), mode3D, draw3D, isSiteModifier, isPathway (fixed-width strip along the path) with pathwayWidth / pathwayOffset, useBorder, borderWidth, borderThickness, slabThickness.

**Landscape area:** name (area name, not the object name), id (text), description, drawingMode, areaUnits, plantDisplay2D (none, plantCloud, plantLine, plantSymbols). Compatibility showPlantsIn2D reads true for any visible mode; writing true selects plantSymbols, false selects none. Do not supply both display properties; both fail when supplied together.

**Existing tree:** botanicalName, commonName, treeNumber, origin, height, canopyDiameter, caliper (DBH), rootBallDiameter, criticalRootZoneDiameter, primaryRootZoneDiameter, treeProtectionZone, condition, sule (safe useful life expectancy), significance, actionComment, location, notes, create3D; a `custom` choice uses the free text of the CustomOrigin / CustomCondition / CustomSULE / CustomSignificance / CustomAction parameter (set it with `params`).

**Stake:** z (elevation), data (description), mode (its role for the site model), siteModel (surface it targets), id (integer), idPrefix, idSuffix, labelReference (label content), displayLeaderLine, showElevationMark.

**Property line:** name, number, showName, showNumber, showArea, areaUnitsImperial / areaUnitsMetric (area units in imperial / metric documents), distanceUnits (segment labels).

**Site model:** display2D / display3D (surfaces drawn), style2D, style3D, geometryZReference (reference elevation for contours), showErrors.

**Site modifier:** config (fitToObjects is stored as aligned), applyTo (surface it modifies), show3D, retainSlopeInside, simplificationTolerance. Lengths are in world units; the schema lists the choices. A `params` object sets raw plug-in parameters.

> **Note:** The object is found by `uuid`, then by `name`, then by `index`. `name` is also written as the area name of a landscape area and as the parcel name of a property line (see its row).
>
> **Note:** Fields that do not belong to the kind of the object are ignored without an `applied` entry. Besides the eight landmark kinds, the tool accepts any other plug-in object; then only `params` has an effect. An object that is not a plug-in object gives `not a landmark object`.
>
> **Note:** "Unknown choices are rejected" holds for the choice fields only. An unknown `plantResource` is not rejected: `applied.plantResource` is `true` when a fallback Plant style is found (see `createPlant`), so read `plantStyle` with `getLandmarkObject` to see which Plant style is in use. A main field whose value has the wrong JSON type is written as `0` or as empty text and reported as `true` (see the note of the group).
>
> **Note:** The Details say that `fitToObjects` is stored as `aligned`. The code does not do this: `fitToObjects` is stored, and read back, as `fitToObjects`. `create3D` is not written at present: `applied.create3D` is always `false`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name when `uuid` is missing. Also used for landscape area (the area name, not the object name) and property line (the parcel name): the same value is written, so give `uuid` to change only that name. |
| `index` | integer |  | Reference by internal index. |
| `plantResource` | string |  | Used for plant. Switches to another Plant style, importing it if needed; read back as `plantStyle`. An unknown name is not rejected. Switching the style takes over all of the style's settings (names, plant ID, spread, height, config, …) and overwrites the current ones; give the fields to keep in the same call. Resolved like `plantResource` in `createPlant` (`false` when no fallback Plant style can be found or imported). |
| `latinName` | string |  | Used for plant. |
| `commonName` | string |  | Used for plant, existing tree. |
| `spread` | number |  | Used for plant. Canopy diameter (spread), in world units. |
| `height` | number |  | Used for plant, existing tree. Height, in world units. |
| `number` | string |  | Used for property line. |
| `botanicalName` | string |  | Used for existing tree. |
| `canopyDiameter` | number |  | Used for existing tree. |
| `caliper` | number |  | Used for existing tree. Trunk diameter (DBH). |
| `z` | number |  | Used for stake. Z value (height), in world units. |
| `data` | string |  | Used for stake. Description (label text). |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. See [Plug-in parameters](Common.md#plug-in-parameters). |
| `plantID` | string |  | Used for plant. Identifies the species. |
| `comments` | string |  | Used for plant. |
| `config` | string |  | Used for plant, site modifier. For a plant, one of: `singlePlant`, `plantsAtPolyVertices`, `plantsAlongPolyEdges`, `plantsInRectangularArray`, `plantsInTriangularArray`. For a site modifier, one of: `gradeLimits`, `contour`, `pad`, `retainingPad`, `aligned`, `path`, `fitToObjects`, `textureBed`, `spoilPile`. |
| `tagDisplay` | string |  | Used for plant. One of: `none`, `left`, `right`, `floating`. |
| `show3DDetail` | boolean |  | Used for plant. |
| `spacing` | number |  | Used for plant. Distance between plants along poly edges or in arrays. |
| `mode3D` | string |  | Used for hardscape. One of: `none`, `slab`, `padUnder`, `padOver`, `textureBed`, `slabDrainage`, `alignedSlab`, `alignedModifOver`, `alignedModifUnder`. |
| `draw3D` | boolean |  | Used for hardscape. |
| `isSiteModifier` | boolean |  | Used for hardscape. |
| `isPathway` | boolean |  | Used for hardscape. Fixed-width strip along the path. |
| `useBorder` | boolean |  | Used for hardscape. |
| `slabThickness` | number |  | Used for hardscape. |
| `borderThickness` | number |  | Used for hardscape. |
| `borderWidth` | number |  | Used for hardscape. |
| `pathwayWidth` | number |  | Used for hardscape. |
| `pathwayOffset` | number |  | Used for hardscape. |
| `id` | string or integer |  | Used for hardscape and landscape area (text) and for stake (an integer; a numeric string such as `"12"` is accepted). For hardscape and landscape area a value that is not text is not written (`false` in `applied`); for a stake, a value that is not a whole number. |
| `description` | string |  | Used for landscape area. Description text. A stake has no `description`: its description is `data`. |
| `drawingMode` | string |  | Used for landscape area. One of: `landscapeArea`, `hedgerow`. |
| `areaUnits` | string |  | Used for landscape area. One of: `sqFeet`, `sqMeters`, `acres`, `hectares`, `documentUnits`. |
| `showPlantsIn2D` | boolean |  | Used for landscape area. Compatibility form of `plantDisplay2D`: `true` selects `plantSymbols`, `false` selects `none`. Do not give both: both report `false` and neither is written. |
| `plantDisplay2D` | string |  | Used for landscape area. One of: `none`, `plantCloud`, `plantLine`, `plantSymbols`. |
| `treeNumber` | string |  | Used for existing tree. |
| `origin` | string |  | Used for existing tree. One of: `notSet`, `endemic`, `native`, `exotic`, `indigenous`, `custom`. |
| `rootBallDiameter` | number |  | Used for existing tree. |
| `criticalRootZoneDiameter` | number |  | Used for existing tree. |
| `primaryRootZoneDiameter` | number |  | Used for existing tree. |
| `treeProtectionZone` | string |  | Used for existing tree. One of: `none`, `circularZone`, `using12DBH`. |
| `condition` | string |  | Used for existing tree. One of: `notSet`, `excellent`, `good`, `average`, `poor`, `custom`. |
| `sule` | string |  | Used for existing tree. One of: `notSet`, `long`, `medium`, `short`, `removal`, `custom`. |
| `significance` | string |  | Used for existing tree. One of: `notSet`, `mostSignificant`, `highlySignificant`, `lessSignificant`, `leastSignificant`, `hazardous`, `custom`. |
| `actionComment` | string |  | Used for existing tree. One of: `notSet`, `retain`, `retainArborist`, `transplantOriginal`, `transplantProposed`, `remove`, `removeBuildingFootprint`, `removePoorHealth`, `removeSpecies`, `custom`. |
| `location` | string |  | Used for existing tree. |
| `notes` | string |  | Used for existing tree. |
| `create3D` | boolean |  | Used for existing tree. Not written at present: `applied.create3D` is always `false`. |
| `mode` | string |  | Used for stake. One of: `siteModelSource`, `setToSiteModelGrade`, `setToCutSurface`, `setToObjectSpot`, `graphic2DOnly`, `siteModifierObject`. |
| `siteModel` | string |  | Used for stake. One of: `existing`, `proposed`. |
| `idPrefix` | string |  | Used for stake. |
| `idSuffix` | string |  | Used for stake. |
| `labelReference` | string |  | Used for stake. One of: `ID`, `Elevation`, `Description`, `ID/Elevation`, `ID/Description`, `Description/Elevation`, `Stationing Data`, `Coordinate PointNE`, `Coordinate PointEN`, `Coordinate PointXY`, `Coordinate PointYX`, `Latitude/Longitude`, `Longitude/Latitude`, `Latitude/Longitude(WGS84)`, `Longitude/Latitude(WGS84)`, `No Label`, `Object Spot Height`. |
| `displayLeaderLine` | boolean |  | Used for stake. |
| `showElevationMark` | boolean |  | Used for stake. |
| `showName` | boolean |  | Used for property line. |
| `showNumber` | boolean |  | Used for property line. |
| `showArea` | boolean |  | Used for property line. |
| `areaUnitsImperial` | string |  | Used for property line. One of: `documentUnits`, `squareFeet`, `squareYards`, `squareMiles`, `acres`, `squareMeters`, `squareKilometers`, `hectares`. |
| `areaUnitsMetric` | string |  | Used for property line. One of: `documentUnits`, `squareFeet`, `squareYards`, `squareMiles`, `acres`, `squareMeters`, `squareKilometers`, `hectares`. |
| `distanceUnits` | string |  | Used for property line. One of: `Document Units`, `Feet & Inches`, `Inches`, `Feet`, `Yards`, `Miles`, `Microns`, `Millimeters`, `Centimeters`, `Meters`, `Kilometers`. |
| `display2D` | string |  | Used for site model. One of: `existingOnly`, `proposedOnly`, `existingAndProposed`. |
| `display3D` | string |  | Used for site model. One of: `nothing`, `existingOnly`, `proposedOnly`, `cutAndFill`. |
| `style2D` | string |  | Used for site model. One of: `k2DTINStyle2DContour`, `k2DTINStyle2DContourSmoothed`, `k2DTINStyle2DContourColoredElevations`, `k2DTINStyle2DTriangulatedContoursColoredSlopes`, `k2DTINStyle2DTriangles`, `k2DTINStyle2DTrianglesColoredSlopes`. |
| `style3D` | string |  | Used for site model. One of: `k3DTINStyleMesh`, `k3DTINStyleMeshColoredElev`, `k3DTINStyleMeshColoredSlopes`, `k3DTINStyleGrid`, `k3DTINStyleGridColoredElev`, `k3DTINStyleGridColoredSlope`, `k3DTINStyleVerticalGrid`, `k3DTINStyleContour`, `k3DTINStyleExtrudedContour`, `k3DTINStyleExtContColoredElev`. |
| `geometryZReference` | number |  | Used for site model. Reference elevation for contours. |
| `showErrors` | boolean |  | Used for site model. |
| `applyTo` | string |  | Used for site modifier. One of: `existing`, `proposed`. |
| `show3D` | boolean |  | Used for site modifier. |
| `retainSlopeInside` | boolean |  | Used for site modifier. |
| `simplificationTolerance` | number |  | Used for site modifier. |

**Result**

Only `applied`; the call returns no object reference.

| Key | Description |
|---|---|
| `applied` | Per field that was given: `true` when the field was written, `false` when it was not. |
| `applied.params` | Only when `params` was given as an object: for each parameter name, `true` when the value was written, `false` when it was not. |

Errors: `object not found`; `not a landmark object`. A failed call is rolled back (`rolledBack`), so nothing is changed.
