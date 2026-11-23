**English** • [Deutsch](../../MCP.de/v2027.2/ObjectsArchitect.md) • [日本語](../../MCP.ja/v2027.2/ObjectsArchitect.md)

# ObjectsArchitect — architecture (BIM)

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools for BIM building elements: walls, slabs, roofs, doors, windows, columns and stairs.

## Table of contents

- [Overview](#overview)
- [Architecture](#architecture)
  - [createWall](#createwall)
  - [createSlab](#createslab)
  - [createRoof](#createroof)
  - [createDoor](#createdoor)
  - [createWindow](#createwindow)
  - [createColumn](#createcolumn)
  - [createStair](#createstair)
  - [getArchitectureObject](#getarchitectureobject)
  - [setArchitectureObject](#setarchitectureobject)

## Overview

This folder holds 1 tool group with 9 tools in total.

| Group | Group ID | Active by default | Safety level | Tools | Summary |
|---|---|---|---|---|---|
| [Architecture](#architecture) | `architecture` | No | medium | 9 | BIM building elements: walls, slabs, roofs, doors, windows, columns and stairs. |

## Architecture

> **Group:** `Architecture` · **Group ID:** `architecture` · **Active by default:** No · **Safety level:** medium · **Tools:** 9

**BIM building elements: walls, slabs, roofs, doors, windows, columns and stairs.**

Inspect, create and edit BIM building objects: straight and round (curved) walls, slabs, roofs, doors, windows, columns and stairs.

**BIM workflow order:** stories and their levels first (Document group: getStories, createStory), then styles (Resources group), then the building elements on the story layers; walls bind their top and bottom to story levels with topBound / bottomBound. Read getArchitectureObject for wall endpoint heights and style; request includeHeightDetails for average height and top/bottom bound metadata, offsets and validated elevations. Lengths are in world units, angles in radians, except roof edge slopes, which are in degrees (2 to 90). Doors and windows are created free-standing; insert them into a wall in Vectorworks. Each change runs as its own named, undoable Vectorworks operation.

> **Note:** Angles are in radians, except two cases that are in degrees: the roof edge `slope`, and the angle parameters of plug-in objects (an angle parameter written through `params`, and `openAngleParameter`, which `getArchitectureObject` reports with `includeOpening`). The wall `angle` that `getArchitectureObject` reports is in radians. Where a tool returns `applied`, it reports the values that were given, one entry per value or per group of values (see the Result of each tool): `true` when the value was written, `false` when it was not (for example a value of the wrong type); a value that is not written at all is not listed. `createRoof` and `createColumn` return no `applied`. A failed call returns `err` and is rolled back (`rolledBack`); see [Results and errors](Common.md#results-and-errors).

| Tool | Effect | Safety | Summary |
|---|---|---|---|
| [`createWall`](#createwall) | Edit | medium | Creates a straight or round wall. |
| [`createSlab`](#createslab) | Edit | medium | Creates a slab from a 2D boundary object. |
| [`createRoof`](#createroof) | Edit | medium | Creates a polygonal roof. |
| [`createDoor`](#createdoor) | Edit | medium | Creates a free-standing door. |
| [`createWindow`](#createwindow) | Edit | medium | Creates a free-standing window. |
| [`createColumn`](#createcolumn) | Edit | medium | Creates a column. |
| [`createStair`](#createstair) | Edit | medium | Creates a stair. |
| [`getArchitectureObject`](#getarchitectureobject) | Read-only | low | Reads the properties of a wall, slab, roof, door, window, column or stair. |
| [`setArchitectureObject`](#setarchitectureobject) | Edit | medium | Edits a wall, slab, roof, door, window, column or stair. |

### createWall

Creates a straight or round wall.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createWall" · **In runToolBatch:** yes

**Details**

Create a wall from `start` to `end`: straight, or round (curved) through `pointOnArc`, a point on the arc between start and end that is not on their line. `thickness` 0 uses the active wall preference. Optional `topHeight`/`bottomHeight` set the wall heights relative to the layer plane. Optional `topBound` / `bottomBound` bind the top / bottom of the wall like the Object Info palette: { kind: story|layerElevation|layerWallHeight, levelType (story bounds: the level type), relativeStory (story bounds: -1 the story below, 0 the story of the wall's layer, the default, 1 the story above), offset (world units, default 0) }; getArchitectureObject `includeHeightDetails` reads them back.

They are applied after the other values and move the wall ends to the bound heights, so they replace topHeight/bottomHeight: a call with both is refused. A bound that the wall cannot take (its layer in no story, no story above/below, a story without that level, a top not above the bottom) fails the call, which then creates nothing; `applied` reports topBound/bottomBound.

> **Note:** When only one of `topHeight` and `bottomHeight` is given, the other one is `0`, so give both. A bound of `kind` `story` needs a `levelType` that is not empty; the layer kinds ignore the values of `levelType` and `relativeStory`, but still refuse a `levelType` that is not a string or a `relativeStory` other than -1, 0 or 1.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `start` | [point](Common.md#points) | Yes | Start point. |
| `end` | [point](Common.md#points) | Yes | End point. |
| `pointOnArc` | [point](Common.md#points) |  | Makes the wall round (curved): a point on the arc between `start` and `end`. A point that is not off the line from `start` to `end` makes the call fail. |
| `thickness` | number |  | Thickness, in world units. `0` uses the active wall preference. |
| `topHeight` | number |  | Height of the top of the wall at both ends, in world units, relative to the layer plane. When only one of `topHeight` and `bottomHeight` is given, the other one is `0`. Refused together with `topBound` or `bottomBound`. |
| `bottomHeight` | number |  | Height of the bottom of the wall at both ends, in world units, relative to the layer plane. When only one of `topHeight` and `bottomHeight` is given, the other one is `0`. Refused together with `topBound` or `bottomBound`. |
| `topBound` | object |  | Binds the top of the wall like the Object Info palette; replaces `topHeight` and `bottomHeight`. |
| `topBound.kind` | string | Yes | One of: `story`, `layerElevation`, `layerWallHeight`. |
| `topBound.levelType` | string |  | The level type of the story. Required, and not empty, for `kind` `story`; its value is ignored for the layer kinds, but a value that is not a string refuses the call for every kind. |
| `topBound.relativeStory` | integer |  | One of: `-1`, `0`, `1`. Default: `0`. The story below (`-1`), the story of the wall's layer (`0`) or the story above (`1`). Used for `kind` `story`; its value is ignored for the layer kinds, but a value other than `-1`, `0` or `1` refuses the call for every kind. |
| `topBound.offset` | number |  | Default: `0`. Offset, in world units. |
| `bottomBound` | object |  | Binds the bottom of the wall like the Object Info palette; replaces `topHeight` and `bottomHeight`. |
| `bottomBound.kind` | string | Yes | One of: `story`, `layerElevation`, `layerWallHeight`. |
| `bottomBound.levelType` | string |  | The level type of the story. Required, and not empty, for `kind` `story`; its value is ignored for the layer kinds, but a value that is not a string refuses the call for every kind. |
| `bottomBound.relativeStory` | integer |  | One of: `-1`, `0`, `1`. Default: `0`. The story below (`-1`), the story of the wall's layer (`0`) or the story above (`1`). Used for `kind` `story`; its value is ignored for the layer kinds, but a value other than `-1`, `0` or `1` refuses the call for every kind. |
| `bottomBound.offset` | number |  | Default: `0`. Offset, in world units. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new wall (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | Only `topBound` and `bottomBound`, `true` for each bound that was given and written. Omitted when no bound was given: `thickness`, `pointOnArc` and the heights are not reported. |

Errors: `'start' and 'end' points are required`; `failed to create round wall ('pointOnArc' must be a point { x, y } off the line from 'start' to 'end')`; `failed to create wall`; `give the heights of a wall either as 'topBound' / 'bottomBound' or as heights (topHeight, bottomHeight, startTop, ...), not both in one call`; a bound that is not well formed (`'<key>' needs 'kind': story, layerElevation or layerWallHeight`; `'<key>': 'relativeStory' is -1, 0 or 1, 'offset' a number (world units) and 'levelType' a string`; `'<key>': a story bound needs 'levelType', the level of the story`); a bound that the wall cannot take (`Vectorworks refused the wall bounds: the top must stay above the bottom, and the wall must be on a design layer`, or a text that names the problem with the story). A failed call is rolled back (`rolledBack`), so no wall remains.

### createSlab

Creates a slab from a 2D boundary object.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createSlab" · **In runToolBatch:** yes

**Details**

Create a slab (floor/deck/ceiling; the Vectorworks `Slab` plug-in object) from an existing 2D boundary object given by `profileUuid`: a polygon, polyline, oval/circle or arc, which the slab consumes. Optional `style` and `height` (elevation of the slab's datum, the top or bottom of its core component as the style sets it), written in that order. `style` is a slab style of the drawing: its name or the UUID of its resource (getResources with resourceType `slabStyle` lists them), checked before anything is created: a name or UUID that is no slab style of the drawing refuses the call, which then creates nothing; or its internal index, where 0 makes the slab unstyled, keeping its components, and an index that is not a slab style is reported false and not written.

`applied` reports true/false for each one given; getArchitectureObject reports style (the index) and styleName.

> **Note:** The schema requires `profileUuid`. When it is missing, the boundary object is looked up with the `uuid`, `name` or `index` of the same arguments, so a `name` meant as the creation option would pick the boundary: always give `profileUuid`. A string `style` is always read as a name or a resource UUID, also a numeric one; use an integer for the internal index.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `profileUuid` | string | Yes | UUID of the object that supplies the profile: a polygon, polyline, oval/circle or arc. The slab consumes it. |
| `height` | number |  | Elevation of the slab datum (the top or bottom of its core component, as the style sets it), in world units. |
| `style` | integer or string |  | A slab style of the drawing: its name or the UUID of its resource (`getResources` with `resourceType` `slabStyle` lists them), or an integer, its internal index (`0`: unstyled, keeping its components). A name or UUID that is no slab style refuses the call; an index that is no slab style is reported `false` and not written. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new slab (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | `style` and `height`, for each one that was given: `true` when written, `false` when not (a value of the wrong type, or a `style` index that is no slab style). Omitted when neither was given. |

Errors: `profile object not found (provide 'profileUuid' of a polygon/polyline boundary)`; `failed to create slab (the profile must be a polygon, polyline, oval/circle or arc)`; `'style' "<text>" is neither the name nor the UUID of a slab style of the drawing (getResources lists them with resourceType 'slabStyle')`. A failed call is rolled back (`rolledBack`).

### createRoof

Creates a polygonal roof.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createRoof" · **In runToolBatch:** yes

**Details**

Create a polygonal roof. Optional `generateGableWalls`, `bearingInset`, `roofThickness`, `miterType` (vertical|horizontal|double), `verticalMiter`, and `edges`, the roof outline in order: at least 3 items { point, slope, projection, eaveHeight }, with the slope in degrees from 2 to 90 (Vectorworks builds a roof only with edge slopes from 2 to 90 degrees), and projection (eave overhang) and eaveHeight (relative to the layer elevation) in world units, default 0.

Every edge is checked before the roof is created: a missing point or slope, a value that is not a finite number or a slope outside 2 to 90 refuses the call, which then creates nothing. The new roof has no attic, soffit or fascia. getArchitectureObject reports the edges in the same form.

> **Note:** A `generateGableWalls`, `bearingInset`, `roofThickness` or `verticalMiter` of the wrong type is read as `false` or `0`, and a `miterType` other than `horizontal` or `double` as `vertical`, without an error.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `generateGableWalls` | boolean |  | Default `false`. |
| `bearingInset` | number |  | Default `0`. |
| `roofThickness` | number |  | Default `0`. |
| `miterType` | string |  | One of: `vertical`, `horizontal`, `double`. Default: `vertical`. |
| `verticalMiter` | number |  | Default `0`. |
| `edges` | array of object |  | From 3 to 32767 items. |
| `edges[].point` | [point](Common.md#points) | Yes | A point of the roof outline; the edges are taken in order. |
| `edges[].slope` | number | Yes | Degrees, 2 to 90. Minimum: `2`. Maximum: `90`. |
| `edges[].projection` | number |  | Eave overhang, in world units. Default `0`. |
| `edges[].eaveHeight` | number |  | Eave height, relative to the layer elevation, in world units. Default `0`. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new roof (see [Object references](Common.md#object-references)). There is no `applied`.

Errors: `'edges' must be an array of 3 to 32767 edges`; a problem with an edge, always prefixed with `'edges'[<i>]: ` and found before the roof is created (`an edge is an object { point, slope, projection, eaveHeight } whose slope, projection and eaveHeight are numbers`; `the edge needs a 'point' { x, y }`; `the edge needs a 'slope' (degrees, 2 to 90)`; `the point, slope, projection and eaveHeight must be finite numbers`; `the slope <n> is not 2 to 90 degrees: Vectorworks builds a roof only with edge slopes from 2 to 90 degrees`); `failed to create roof`; `Vectorworks refused the roof edge 'edges'[<i>]`. A failed call is rolled back (`rolledBack`), so no roof remains.

### createDoor

Creates a free-standing door.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createDoor" · **In runToolBatch:** yes

**Details**

Create a Door parametric object at `position`, free-standing (insert it into a wall in Vectorworks). Optional `width` and `height` (positive, world units) are the size of the door as the Object Info palette shows it, measured as its Size Reference says; Vectorworks computes the leaf size from them (getArchitectureObject leafWidth / leafHeight). Optional `sizeReference` (leaf: the leaf, unit: the unit with its frame, roughOpening: the rough opening) is written first; the door settings of the drawing give the default.

A `sizeReference` that changes the reference needs both `width` and `height`, since the door would measure its stored size in the new reference. Optional `config` (legacy Config popup) and `idLabel`. A value that the plug-in style of the door sets cannot be changed: the call is refused and creates nothing. `applied` reports true/false for each value given; getArchitectureObject reads width and height back as given.

> **Note:** The plug-in style check covers only `sizeReference`, `width` and `height`, and only a value that would change: it is refused with `'<key>' cannot be changed: the plug-in style '<name>' of the door sets its parameter '<param>' (edit the style instead); the call changes nothing`. `config` and `idLabel` are written without that check. The values are written in the order `sizeReference`, `width`, `height`, `config`, `idLabel`; a `config` or `idLabel` that is not a string is written as empty text.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point. |
| `width` | number |  | In world units. Greater than `0`: another value is refused. |
| `height` | number |  | In world units. Greater than `0`: another value is refused. |
| `sizeReference` | string |  | One of: `leaf`, `unit`, `roughOpening` (Leaf Size, Unit Size, Rough Opening). A value that changes the reference needs `width` and `height` with it. |
| `config` | string |  | Legacy Config popup. |
| `idLabel` | string |  | The ID label of the door. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new door (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | One entry for each of `sizeReference`, `width`, `height`, `config` and `idLabel` that was given: `true` when written, `false` when the door refused the value. Omitted when none was given. |

Errors: `failed to create door`; `'width' must be a positive number (world units)` (and the same for `'height'`); `'sizeReference' is one of leaf|unit|roughOpening`; `'sizeReference' changes what the size of the door measures: give both 'width' and 'height' with it; the call changes nothing`; `'<key>' cannot be changed: the plug-in style '<name>' of the door sets its parameter '<param>' (edit the style instead); the call changes nothing`. A refused call is rolled back (`rolledBack`), so no door remains.

### createWindow

Creates a free-standing window.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createWindow" · **In runToolBatch:** yes

**Details**

Create a Window parametric object at `position`, free-standing (insert it into a wall in Vectorworks). Optional `width` and `height` (positive, world units) are the size of the window as the Object Info palette shows it, measured as its Size Reference says; Vectorworks computes the unit size from them (getArchitectureObject unitWidth / unitHeight). Optional `sizeReference` (sash: the sash opening, unit: the unit, roughOpening: the rough opening) is written first; the window settings of the drawing give the default; one that changes the reference needs both `width` and `height`.

Optional `elevation` is the sill height, the bottom of the window, in world units above the layer plane (also for a window in a wall: not above the bottom of the wall), written after the size. The window keeps its Elevation Set At setting: with Head of Window (the default) Vectorworks stores the head height, elevation + height (getArchitectureObject reports headHeight and elevationSetAt).

Optional `idLabel`. A value that the plug-in style of the window sets cannot be changed: the call is refused and creates nothing. `applied` reports true/false for each value given; getArchitectureObject reads width, height and elevation back as given.

> **Note:** The plug-in style check covers only `sizeReference`, `width`, `height` and `elevation`, and only a value that would change: it is refused with `'<key>' cannot be changed: the plug-in style '<name>' of the window sets its parameter '<param>' (edit the style instead); the call changes nothing`. `idLabel` is written without that check; a value that is not a string is written as empty text. The values are written in the order `sizeReference`, `width`, `height`, `elevation`, `idLabel`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point. |
| `width` | number |  | In world units. Greater than `0`: another value is refused. |
| `height` | number |  | In world units. Greater than `0`: another value is refused. |
| `sizeReference` | string |  | One of: `sash`, `unit`, `roughOpening`. A value that changes the reference needs `width` and `height` with it. |
| `elevation` | number |  | The sill height, in world units above the layer plane. Must be a number. Refused when the window has no valid Elevation Set At (Head of Window or Sill of Window) and Height. |
| `idLabel` | string |  | The ID label of the window. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new window (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | One entry for each of `sizeReference`, `width`, `height`, `elevation` and `idLabel` that was given: `true` when written, `false` when the window refused the value. Omitted when none was given. |

Errors: `failed to create window`; `'width' must be a positive number (world units)` (and the same for `'height'`); `'elevation' (the sill height) must be a number (world units)`; `'sizeReference' is one of sash|unit|roughOpening`; `'sizeReference' changes what the size of the window measures: give both 'width' and 'height' with it; the call changes nothing`; `'elevation' cannot be written: the window has no valid ElevationSetAt (Head of Window or Sill of Window) and Height`; `'<key>' cannot be changed: the plug-in style '<name>' of the window sets its parameter '<param>' (edit the style instead); the call changes nothing`. A refused call is rolled back (`rolledBack`), so no window remains.

### createColumn

Creates a column.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createColumn" · **In runToolBatch:** yes

**Details**

Create a column (the Vectorworks `Column2` plug-in object) at `position`. Optional `shape` (Rectangular|Oval; Round is Oval), `height` (of the single active component; fails when the column uses both architectural and structural components), `width` and `depth` (shaft), `diameter` (round shaft). When a value cannot be set the column is removed and the tool fails.

> **Note:** `height`, `width`, `depth` and `diameter` must be finite numbers greater than `0`. The values are written in the order `shape`, `height`, `width`, `depth`, `diameter`, so a `diameter` overrides `width` and `depth`: it makes the shaft `Oval` with width and depth equal to the diameter. `shape` accepts `Rectangular`, `Oval` or `Round` (read as `Oval`); any other text fails the call. The column is the `Column2` plug-in object, or the legacy `Column` object when `Column2` is not installed.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point. |
| `shape` | string |  | `Rectangular`, `Oval` or `Round` (read as `Oval`). The schema does not restrict the text, but any other value fails the call. |
| `height` | number |  | Greater than `0`. Of the single active component; fails when the column uses both architectural and structural components. |
| `width` | number |  | Width of the shaft, in world units. Greater than `0`. |
| `depth` | number |  | Depth of the shaft, in world units. Greater than `0`. |
| `diameter` | number |  | Diameter of the round shaft, in world units. Greater than `0`. Makes the shaft `Oval` with `width` and `depth` equal to the diameter, overriding both. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new column (see [Object references](Common.md#object-references)). There is no `applied`.

Errors: `failed to create column (requires the 'Column2' plug-in object)`; `failed to set column shape`; `failed to set column height (requires a single bound component)`; `failed to set column shaft width`; `failed to set column shaft depth`; `failed to set column shaft diameter`. The column is deleted when a value fails, and a failed call is rolled back (`rolledBack`), so no column remains.

### createStair

Creates a stair.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createStair" · **In runToolBatch:** yes

**Details**

Create a stair (the Vectorworks 'Stairs CW' plug-in object, in its default configuration) at `position`. Optional positive `totalRise`, `totalRun` (walking line length), `treadDepth` and `riserHeight` are written before the stair is reset; the stair recalculates the dependent values, so read them back with getArchitectureObject. `width` cannot be set on a Stairs CW stair. `applied` reports true/false for each value given.

> **Note:** `width` is always reported `false`: Stairs CW writes the first of its stair widths and does not read it back. `totalRise`, `totalRun`, `treadDepth` and `riserHeight` must be finite numbers greater than `0`; another value is reported `false` and the stair keeps its default.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point. |
| `width` | number |  | Width, in world units. Always reported `false` in `applied`: the value cannot be set on a Stairs CW stair. |
| `totalRise` | number |  | Total rise, in world units. Greater than `0`. |
| `totalRun` | number |  | Walking line length. Greater than `0`. |
| `treadDepth` | number |  | Tread depth, in world units. Greater than `0`. |
| `riserHeight` | number |  | Riser height, in world units. Greater than `0`. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new stair (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `applied` | One entry for each of `width`, `totalRise`, `totalRun`, `treadDepth` and `riserHeight` that was given: `true` when written, `false` when not. `width` is always `false`. Omitted when none was given. |

Error: `failed to create stair (requires the 'Stairs CW' plug-in object)`. A failed call is rolled back (`rolledBack`).

### getArchitectureObject

Reads the properties of a wall, slab, roof, door, window, column or stair.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the typed properties of a wall, slab, roof, door, window, column or stair (dimensions, heights, style, schedule id, ...). Walls report native endpoint Z values startTop/startBottom/endTop/endBottom in world units, not stored constraint offsets, plus caps { leftCap (start end), rightCap (end end), round } and isCurtainWall. Slabs (the `Slab` plug-in object, or a legacy floor slab node of older files, which has no height and no parameters) report height, style (the internal index of the slab style; 0 is unstyled) and styleName (the name of that style).

Roofs report edgeCount and edges, the roof outline in order: one { point, slope (degrees), projection, eaveHeight (relative to the layer elevation) } per edge, null for an edge that cannot be read, in the form createRoof and setArchitectureObject take; and generateGableWalls, bearingInset, roofThickness, miterType (vertical|horizontal|double) and verticalMiter.

Doors report width and height (the size of the door as the Object Info palette shows it, in world units, measured as sizeReference says: leaf|unit|roughOpening), leafWidth / leafHeight (the leaf size Vectorworks computed from them at the last reset), config, idLabel, thickness (leaf), topShape, leafType and onSchedule; windows width, height and sizeReference (sash|unit|roughOpening) in the same way, unitWidth / unitHeight (the unit size Vectorworks computed from them), elevation (the sill height: the bottom of the window above the layer plane, also for a window in a wall), headHeight, elevationSetAt (head|sill: which of the two the window stores as its Elevation parameter), idLabel, sashOperation (legacy SashOperation popup), topShape, jambWidth, jambDepth, includeSill, sillStyle, onSchedule and description; columns (the `Column2` plug-in object, or a legacy `Column`) shape, height, width, depth and diameter; stairs (the 'Stairs CW' plug-in object) width (its first stair width), totalRise, totalRun (walking line length), numRisers, treadDepth and riserHeight.

Popup values are reported raw, as the plug-in stores them. Optional `params` (array of plug-in parameter names; slabs, doors, windows, columns and stairs) adds `params` { name: value } with typed values: reals as numbers in world units (angle parameters in degrees), integers, booleans and other types as strings; names the object does not have are omitted.

Unlike the display strings of getObjectParameters these are exact values, in the form setArchitectureObject `params` writes them. Optional includeHeightDetails (default false) adds a wall-only heightDetails object: startHeight/endHeight (endpoint differences), averageHeight (existing geometric average calculation, normalized to world units), measurement availability statuses, and topBound/bottomBound with status (valid|missing|unresolved|invalid), kind (layerElevation|layerWallHeight|story|unknown), levelType, offset, and relativeStory for story bounds (-1 below, 0 current, 1 above).

Only valid bounds have resolvedElevation, using the parent-container semantics of Vectorworks; missing references never report a fallback elevation. Missing bounds do not imply missing geometric heights. These bound levels are not a story catalog or absolute story identifiers (getStories of the Document group lists the stories and their levels). All heightDetails lengths are world units; use convertUnits for UI units.

Optional includeOpening (default false) adds an `opening` object to doors and windows: capability (operable|fixed|notApplicable|unknown); config (window Configuration popup, raw) or configuration (door Configuration popup, raw); operation (door SwingOperation for the Swing configuration; window CasementOperation, FixedGlassOperation or HungOperation for its configuration); hingeSide as viewed from the exterior (door Swing; window Casement and Tilt/Turn); openDirection (door Swing; window Awning, Casement, Hopper and Tilt/Turn; Vertical Pivot reports outwardSide instead); hingeDirection (windows), interiorSide, flipped, show3DOpen and openAngleParameter as raw values, and legacyOperation (doors: the legacy Operation popup, superseded by operation).

Direction parameters are emitted only when they apply to the configuration. opensToward is interior or exterior from the In/Out value (In is the interior side, Out the exterior side) for a single-leaf door Swing and for verified window openings (Awning, Hopper, Tilt/Turn, single-leaf Casement); Vertical Pivot is both; Opening, Cased Opening and Fixed Glass are notApplicable; other openings are unknown.

The drawn open angle is reported separately from the capability. The door `config` property now reads the Configuration popup.

> **Note:** The last sentence of the description above is wrong for doors: `config` reports the legacy `Config` popup, the one that `createDoor` writes. The Configuration popup is reported only as `opening.configuration`, with `includeOpening`. `openAngleParameter` is the raw value of the plug-in parameter, in degrees, not radians. `capability` is `operable` for a door Swing and for the window configurations Awning, Casement, Hopper, Tilt/Turn and Vertical Pivot; `fixed` for a Fixed Glass window; `notApplicable` for Opening and Cased Opening; `unknown` otherwise (for example Hung, Sliding, Folding, or a door other than Swing). `hingeDirection`, `flipped` and `show3DOpen` are booleans; `interiorSide` and `legacyOperation` are strings.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `includeHeightDetails` | boolean |  | Default: `false`. Adds `heightDetails` to a wall. |
| `includeOpening` | boolean |  | Default: `false`. Adds `opening` to a door or window. |
| `params` | array of string |  | Names of plug-in parameters to return with typed values. See [Plug-in parameters](Common.md#plug-in-parameters). Slabs, doors, windows, columns and stairs only: walls and roofs report no `params`. |

**Result**

The object reference (see [Object references](Common.md#object-references)) and `kind` (`Wall`, `Slab`, `Roof`, `Door`, `Window`, `Column` or `Stair`), then the keys of that kind. A value that cannot be read from the object is left out.

| Kind | Keys |
|---|---|
| `Wall` | `start`, `end` ([points](Common.md#points)), `length`, `angle` (radians), `startTop`, `startBottom`, `endTop`, `endBottom` (world units), `style` (the internal index of the wall style), `caps` (`{ leftCap, rightCap, round }`), `isCurtainWall`, and `heightDetails` with `includeHeightDetails`. |
| `Slab` | `height`, `style` (the internal index; `0` is unstyled), `styleName` (only when `style` is not `0`), and `params` when requested. |
| `Roof` | `edgeCount`, `edges`, `roofThickness`, `bearingInset`, `generateGableWalls`, `verticalMiter`, `miterType`. |
| `Door` | `opening` (with `includeOpening`), `width`, `height`, `sizeReference`, `leafWidth`, `leafHeight`, `config`, `idLabel`, `thickness`, `topShape`, `leafType`, `onSchedule`, and `params` when requested. |
| `Window` | `opening` (with `includeOpening`), `width`, `height`, `sizeReference`, `unitWidth`, `unitHeight`, `elevation`, `headHeight`, `elevationSetAt`, `idLabel`, `sashOperation`, `topShape`, `jambWidth`, `jambDepth`, `includeSill`, `sillStyle`, `onSchedule`, `description`, and `params` when requested. |
| `Column` | `shape`, `height`, `width`, `depth`, `diameter` (only for an `Oval` shaft whose width equals its depth), and `params` when requested. |
| `Stair` | `width` (the first of the stair widths), `totalRise`, `totalRun`, `numRisers`, `treadDepth`, `riserHeight`, and `params` when requested. `numTreads`, `configuration`, `handrailLeft` and `handrailRight` are never reported. |

`heightDetails` (walls, with `includeHeightDetails`) holds `units` (`world`), `startHeight` and `endHeight` (`null` unless both endpoint heights are finite), `endpointHeightStatus` (`available` or `unavailable`), `averageHeight` (`null` when it cannot be computed), `averageHeightStatus` (`available` or `unavailable`), `topBound` and `bottomBound`. A bound always has `status` (`valid`, `missing`, `unresolved` or `invalid`). Unless the status is `missing`, it also has `kind` (`layerElevation`, `layerWallHeight`, `story` or `unknown`), `levelType`, `offset` (`null` when it is not a finite number) and, for a story bound, `relativeStory`. `resolvedElevation` is present only when the status is `valid` and the bound has an elevation.

Errors: `object not found`; `not an architectural object (wall, slab, roof, door, window, column or stair)`.

### setArchitectureObject

Edits a wall, slab, roof, door, window, column or stair.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: setArchitectureObject" · **In runToolBatch:** yes

**Details**

Edit a wall, slab, roof, door, window, column or stair by uuid. Provide the fields relevant to the type, with the keys and values that getArchitectureObject reports; `applied` reports true/false per change.

**Walls:** thickness, start/end, topHeight/bottomHeight (both ends), startTop/startBottom/endTop/endBottom (single endpoint heights, e.g. for a tapered wall; applied as `endHeights`), style (the internal index of a wall style; another value is false and not written), caps { leftCap, rightCap } (round caps are no longer supported), isCurtainWall, and topBound / bottomBound as createWall takes them, applied after the other values: each moves its wall end by the change of its bound height (like the Object Info palette), so they cannot be combined with the heights in one call, and a bound that the wall cannot take fails the call, which then changes nothing.

**Slabs:** style as createSlab takes it (a slab style name or the UUID of its resource: one that is no slab style of the drawing refuses the call, which then changes nothing; or the internal index: 0 unstyles the slab, keeping its components, and an index that is not a slab style of the drawing is false and not written) and height (the `Slab` plug-in object only; false for a legacy floor slab node), written in that order.

**Roofs:** generateGableWalls, bearingInset, roofThickness (ignored when the roof has components), miterType (vertical|horizontal|double) and verticalMiter, applied together as `attributes`; `accessories` { insertAttic, insertSoffit, insertFascia, fasciaWidth, fasciaHeight, atticHeight, recess, rakeThickness, trimDepth (lengths in world units) } cannot be read and is written as a whole: missing members become false/0. Roof `edges` replaces the roof outline with at least 3 items in the form getArchitectureObject reports, in order: the members an item omits keep the values of the current edge at its position (an item beyond the current edges needs a `point` and a `slope`); every slope must be 2 to 90 degrees (Vectorworks builds a roof only with edge slopes from 2 to 90 degrees), and an invalid item refuses the call, which then changes nothing. Unchanged edges are not rewritten, further edges are appended and surplus edges are removed from the end together with the dormers and skylights on them. Nothing is written when a point coincides with the next one or lies on one line with its two neighbours (Vectorworks removes such points). Applied as `edges`, true when the roof ends with exactly these points, slopes and projections (Vectorworks can raise the eave height of a gable edge to the height its neighbours bear).

**Doors:** width, height and sizeReference (leaf|unit|roughOpening) as createDoor takes them, written first in the order sizeReference, width, height, then thickness (leaf), config, topShape, leafType (Solid|Glass|Panel|Custom), onSchedule, idLabel.

**Windows:** width, height, sizeReference (sash|unit|roughOpening) and elevation (the sill height) as createWindow takes them, written first in the order sizeReference, width, height, elevation (without `elevation` the window keeps its stored Elevation, so with Head of Window a new height moves the sill), then topShape, sashOperation (legacy), jambWidth, jambDepth, includeSill, sillStyle (Timber|Masonry|Brick|Open Profile Beside Frame|Open Profile Below Frame|Closed Profile), onSchedule, idLabel, description. A door or window value that the plug-in style of the object sets refuses the call, which then changes nothing; a value equal to the current one is not written again. topShape is Square|Round|Segment|Sloped from Left|Sloped from Right|Gable|Ellipse|Gothic; windows also accept Half Round, Half Segment, Half Ellipse and Half Gothic, each followed by ' from Left' or ' from Right'.

**Columns:** shape, height, width, depth, diameter.

**Stairs (Stairs CW):** positive totalRise, totalRun (walking line length), treadDepth, riserHeight and numRisers (1-32767), which the stair applies when it is reset after the edit, recalculating the dependent values (read them back); width, numTreads, configuration, handrailLeft and handrailRight cannot be set on it (applied false). A `params` object sets raw plug-in parameters (reals in world units, as getArchitectureObject `params` reads them).

> **Note:** Everything that can refuse the call is checked before anything is changed, so a refused call changes nothing: wall bounds (also bounds given together with heights), a slab `style` that is no slab style of the drawing, the roof `edges`, and the size and plug-in style checks of a door or window (see [createDoor](#createdoor) and [createWindow](#createwindow)). A door takes the `sizeReference` values `leaf`, `unit` and `roughOpening`, a window `sash`, `unit` and `roughOpening`. The plug-in style check covers only `sizeReference`, `width`, `height` and the window `elevation`, and only a value that would change; an unchanged value is not written again but is reported `true`. All other door and window values are written without that check.
>
> `topHeight` and `bottomHeight` are written together: when only one is given, the other one is `0`. `start` and `end` are written together: a single one is ignored and not reported. A `config` or `idLabel` that is not a string is written as empty text, and a wall `thickness` that is not a number is read as `0`, in both cases without an error.
>
> A door's `config` and `idLabel` are written right after the size values, before `thickness`, `topShape`, `leafType` and `onSchedule`. A window's `elevation` and `idLabel` are written right after the size values, before the other window values, and `sashOperation` is written before `topShape`. The order in the description above differs. `params` is accepted for every kind of object; its result is `applied.params`. It applies to slabs, doors, windows, columns and stairs; for walls and roofs, which have no plug-in parameters, every entry is `false`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `thickness` | number |  | Used for walls, doors. Thickness, in world units (of the leaf, for a door). A wall `thickness` that is not a number is read as `0`. |
| `start` | [point](Common.md#points) |  | Used for walls. Start point. Written only together with `end`; a single one is ignored and not reported. |
| `end` | [point](Common.md#points) |  | Used for walls. End point. Written only together with `start`; a single one is ignored and not reported. |
| `topHeight` | number |  | Used for walls. Height of the top at both ends, in world units. When only one of `topHeight` and `bottomHeight` is given, the other one is `0`. Reported as `heights`. Refused together with `topBound` or `bottomBound`. |
| `bottomHeight` | number |  | Used for walls. Height of the bottom at both ends, in world units. When only one of `topHeight` and `bottomHeight` is given, the other one is `0`. Reported as `heights`. Refused together with `topBound` or `bottomBound`. |
| `style` | integer or string |  | Used for walls, slabs. A wall takes the internal index of a wall style (another value is `false` and not written). A slab takes the name or the resource UUID of a slab style, or its internal index, as in createSlab. |
| `height` | number |  | Used for slabs (the elevation of the slab datum), doors, windows, columns. In world units. For a column: greater than `0` and only when one component is active; otherwise `false` (also when the column uses both architectural and structural components). |
| `width` | number |  | Used for doors, windows, columns. Width, in world units. For a column: greater than `0`, otherwise `false`. |
| `sizeReference` | string |  | Used for doors, windows. A door takes `leaf`, `unit` or `roughOpening`, a window `sash`, `unit` or `roughOpening`; the value of the other kind refuses the call. A value that changes the reference needs `width` and `height` with it. |
| `config` | string |  | Used for doors. The legacy Config popup. A value that is not a string is written as empty text. |
| `idLabel` | string |  | Used for doors, windows. A value that is not a string is written as empty text. |
| `elevation` | number |  | Used for windows. The sill height, in world units. Must be a number. |
| `shape` | string |  | Used for columns. `Rectangular`, `Oval` or `Round` (read as `Oval`); another text is reported `false`. |
| `depth` | number |  | Used for columns. Depth, in world units. Greater than `0`, otherwise `false`. |
| `diameter` | number |  | Used for columns. Diameter, in world units. Makes the shaft `Oval` with `width` and `depth` equal to the diameter. Greater than `0`, otherwise `false`. It is written after `shape`, `width` and `depth` and sets the shape to Oval and both sizes, so it overrides them. |
| `totalRise` | number |  | Used for stairs (Stairs CW). Greater than `0`. |
| `totalRun` | number |  | Used for stairs (Stairs CW). Walking line length. Greater than `0`. |
| `treadDepth` | number |  | Used for stairs (Stairs CW). Greater than `0`. |
| `riserHeight` | number |  | Used for stairs (Stairs CW). Greater than `0`. |
| `startTop` | number |  | Used for walls. Top height at the start point, in world units. Applied as `endHeights`. |
| `startBottom` | number |  | Used for walls. Bottom height at the start point, in world units. Applied as `endHeights`. |
| `endTop` | number |  | Used for walls. Top height at the end point, in world units. Applied as `endHeights`. |
| `endBottom` | number |  | Used for walls. Bottom height at the end point, in world units. Single endpoint heights, e.g. for a tapered wall; applied as `endHeights`. The heights that are not given keep their values; `false` when the wall has no readable heights or a value is not a number. Refused together with `topBound` or `bottomBound`. |
| `caps` | object |  | Used for walls. `{ leftCap, rightCap }`; the round cap is not written. `false` when it is not an object or a cap is not a boolean. |
| `caps.leftCap` | boolean |  | Whether the start end of the wall is closed. |
| `caps.rightCap` | boolean |  | Whether the end end of the wall is closed. |
| `isCurtainWall` | boolean |  | Used for walls. |
| `topBound` | object |  | Used for walls. Binds the top of the wall as createWall takes it; applied after the other values. Refused together with the heights. |
| `topBound.kind` | string | Yes | One of: `story`, `layerElevation`, `layerWallHeight`. |
| `topBound.levelType` | string |  | The level type of the story. Required, and not empty, for `kind` `story`; its value is ignored for the layer kinds, but a value that is not a string refuses the call for every kind. |
| `topBound.relativeStory` | integer |  | One of: `-1`, `0`, `1`. Default: `0`. The story below (`-1`), the story of the wall's layer (`0`) or the story above (`1`). Used for `kind` `story`; its value is ignored for the layer kinds, but a value other than `-1`, `0` or `1` refuses the call for every kind. |
| `topBound.offset` | number |  | Default: `0`. Offset, in world units. |
| `bottomBound` | object |  | Used for walls. Binds the bottom of the wall as createWall takes it; applied after the other values. Refused together with the heights. |
| `bottomBound.kind` | string | Yes | One of: `story`, `layerElevation`, `layerWallHeight`. |
| `bottomBound.levelType` | string |  | The level type of the story. Required, and not empty, for `kind` `story`; its value is ignored for the layer kinds, but a value that is not a string refuses the call for every kind. |
| `bottomBound.relativeStory` | integer |  | One of: `-1`, `0`, `1`. Default: `0`. The story below (`-1`), the story of the wall's layer (`0`) or the story above (`1`). Used for `kind` `story`; its value is ignored for the layer kinds, but a value other than `-1`, `0` or `1` refuses the call for every kind. |
| `bottomBound.offset` | number |  | Default: `0`. Offset, in world units. |
| `generateGableWalls` | boolean |  | Used for roofs. Written together with the other roof attributes (`applied.attributes`); an attribute that is not given keeps its value. |
| `bearingInset` | number |  | Used for roofs. In world units. |
| `roofThickness` | number |  | Used for roofs. Ignored when the roof has components. |
| `miterType` | string |  | Used for roofs. One of: `vertical`, `horizontal`, `double`. |
| `verticalMiter` | number |  | Used for roofs. |
| `accessories` | object |  | Used for roofs. Written as a whole: a member that is not given becomes `false` or `0`. |
| `accessories.insertAttic` | boolean |  | Whether to insert an attic. |
| `accessories.insertSoffit` | boolean |  | Whether to insert a soffit. |
| `accessories.insertFascia` | boolean |  | Whether to insert a fascia. |
| `accessories.fasciaWidth` | number |  | Width of the fascia, in world units. |
| `accessories.fasciaHeight` | number |  | Height of the fascia, in world units. |
| `accessories.atticHeight` | number |  | Height of the attic, in world units. |
| `accessories.recess` | number |  | Recess, in world units. |
| `accessories.rakeThickness` | number |  | Rake thickness, in world units. |
| `accessories.trimDepth` | number |  | Trim depth, in world units. |
| `edges` | array of object |  | Used for roofs. From 3 to 32767 items. Replaces the roof outline. |
| `edges[].point` | [point](Common.md#points) |  | A point of the roof outline. An item that omits it keeps the point of the current edge at its position; an item beyond the current edges needs a `point` and a `slope`. |
| `edges[].slope` | number |  | Degrees, 2 to 90. Minimum: `2`. Maximum: `90`. |
| `edges[].projection` | number |  | Eave overhang, in world units. An item that omits it keeps the current value. |
| `edges[].eaveHeight` | number |  | Eave height, relative to the layer elevation, in world units. An item that omits it keeps the current value. |
| `topShape` | string |  | Used for doors, windows. The values are listed in the description above. |
| `leafType` | string |  | Used for doors. `Solid`, `Glass`, `Panel` or `Custom`; the schema does not restrict the text. |
| `onSchedule` | boolean |  | Used for doors, windows. |
| `sashOperation` | string |  | Used for windows. Legacy. |
| `jambWidth` | number |  | Used for windows. |
| `jambDepth` | number |  | Used for windows. |
| `includeSill` | boolean |  | Used for windows. |
| `sillStyle` | string |  | Used for windows. `Timber`, `Masonry`, `Brick`, `Open Profile Beside Frame`, `Open Profile Below Frame` or `Closed Profile`; the schema does not restrict the text. |
| `description` | string |  | Used for windows. Description text. |
| `numTreads` | integer |  | Stairs: cannot be set (reported as not applied). |
| `numRisers` | integer |  | Used for stairs (Stairs CW). 1-32767. |
| `configuration` | string |  | Stairs: cannot be set (reported as not applied). |
| `handrailLeft` | boolean |  | Stairs: cannot be set (reported as not applied). |
| `handrailRight` | boolean |  | Stairs: cannot be set (reported as not applied). |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. See [Plug-in parameters](Common.md#plug-in-parameters). Applies to slabs, doors, windows, columns and stairs; for walls and roofs, which have no plug-in parameters, every entry is `false`. Reported in `applied.params`. Angle parameters are written in degrees. |

**Result**

An object `{ "applied": { ... } }`; there is no object reference. `applied` has one entry for each value that was given: `true` when it was written, `false` when it was not. The keys are the parameter names, except where the table says otherwise.

| Kind | Keys of `applied` |
|---|---|
| Wall | `thickness`; `line` (`start` and `end`, only when both are given); `heights` (`topHeight` and `bottomHeight`); `style`; `endHeights` (`startTop`, `startBottom`, `endTop` and `endBottom`); `caps`; `isCurtainWall`; `topBound`; `bottomBound` |
| Slab | `style`; `height` |
| Roof | `attributes` (`generateGableWalls`, `bearingInset`, `roofThickness`, `miterType` and `verticalMiter` together); `accessories`; `edges` |
| Door | `sizeReference`; `width`; `height`; `config`; `idLabel`; `thickness`; `topShape`; `leafType`; `onSchedule` |
| Window | `sizeReference`; `width`; `height`; `elevation`; `idLabel`; `topShape`; `sashOperation`; `jambWidth`; `jambDepth`; `includeSill`; `sillStyle`; `onSchedule`; `description` |
| Column | `shape`; `height`; `width`; `depth`; `diameter` |
| Stair | `totalRise`; `totalRun`; `treadDepth`; `riserHeight`; `numRisers`; and, always `false`, `width`, `numTreads`, `configuration`, `handrailLeft`, `handrailRight` |

`applied.params` is an object `{ "<name>": true|false }` with one entry for each name in `params`. Applies to slabs, doors, windows, columns and stairs; for walls and roofs, which have no plug-in parameters, every entry is `false`. `endHeights` is `false` when the wall has no readable heights or a value is not a number; the heights that are not given keep their values. `attributes` is `false` when the roof has no attributes, a value has the wrong type or the `miterType` is unknown; the attributes that are not given keep their values.

Errors: `object not found`; `not an architectural object (wall, slab, roof, door, window, column or stair)`; and the refusals that the Note lists, with the texts of the create tools: [createWall](#createwall) (the wall bounds), [createSlab](#createslab) (the slab style), [createRoof](#createroof) (`'edges' must be an array of 3 to 32767 edges` and the per-edge texts), [createDoor](#createdoor) and [createWindow](#createwindow) (the size and plug-in style checks). A wall bound that Vectorworks refuses fails the call with `Vectorworks refused the wall bounds: the top must stay above the bottom, and the wall must be on a design layer`, or a text that names the problem with the story. A failed call is rolled back (`rolledBack`).
