**English** • [Deutsch](../../MCP.de/v2027.2/ObjectPrimitives.md) • [日本語](../../MCP.ja/v2027.2/ObjectPrimitives.md)

# ObjectPrimitives — objects and 2D drawing

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools for any object of the drawing (finding, inspecting, styling, transforming, plug-in parameters and records) and for creating, editing, measuring and combining 2D primitives and text.

## Table of contents

- [Overview](#overview)
- [Draw2D](#draw2d)
  - [createLine](#createline)
  - [createRectangle](#createrectangle)
  - [createCircle](#createcircle)
  - [createArc](#createarc)
  - [createPolygon](#createpolygon)
  - [createPolyline](#createpolyline)
  - [createLocus](#createlocus)
  - [getGeometry](#getgeometry)
  - [setGeometry](#setgeometry)
  - [editVertices](#editvertices)
  - [queryGeometry](#querygeometry)
  - [combineShapes](#combineshapes)
  - [createText](#createtext)
  - [getText](#gettext)
  - [editText](#edittext)
- [Objects](#objects)
  - [findObjects](#findobjects)
  - [getObjectsAtPoint](#getobjectsatpoint)
  - [getObjectInfo](#getobjectinfo)
  - [getObjectAttributes](#getobjectattributes)
  - [setObjectAttributes](#setobjectattributes)
  - [copyAttributes](#copyattributes)
  - [editObject](#editobject)
  - [getObjectParameters](#getobjectparameters)
  - [getObjectRecords](#getobjectrecords)
  - [setObjectParameter](#setobjectparameter)
  - [getPluginDefinition](#getplugindefinition)
  - [createPluginObject](#createpluginobject)

## Overview

This folder holds 2 tool groups with 27 tools in total.

| Group | Group ID | Active by default | Safety level | Tools | Summary |
|---|---|---|---|---|---|
| [Draw2D](#draw2d) | `draw2d` | No | low | 15 | Create, edit, measure and combine 2D primitives, and create, read and edit text objects. |
| [Objects](#objects) | `objects` | Yes | medium | 12 | Find, inspect and edit any object: attributes, transforms, containers, plug-in parameters and records. |

## Draw2D

> **Group:** `Draw2D` · **Group ID:** `draw2d` · **Active by default:** No · **Safety level:** low · **Tools:** 15

**Create, edit, measure and combine 2D primitives, and create, read and edit text objects.**

Create, edit and measure 2D primitive geometry: lines, rectangles, rounded rectangles, circles, arcs, polygons, polylines and loci; combine two 2D shapes with Boolean operations (combineShapes: union, intersection, difference = the first shape minus the second, and symmetricDifference of lines, rectangles, rounded rectangles, ovals, arcs and circles, polygons (not freehand) and polylines; the results are new 2D objects of any type with the attributes of the first shape, in its container; the originals stay unchanged unless `deleteOriginals` says otherwise, apart from a second shape in another plane, which is first moved into the plane of the first; an empty result is a success without shapes); and create, read and edit text objects (createText, getText, editText): their content, the formatting of character ranges, text styles, alignment, line spacing, wrapping and tab stops.

Coordinates are in world units, angles in radians. New objects go on the active layer, the results of combineShapes into the container of the first shape; every change runs as its own named, undoable Vectorworks operation. queryGeometry answers closest point, distance, containment, intersection and tangent questions, and measures polygons and polylines along their true curve (length, the point, tangent and curvature at a distance, division into equal parts), without changing the drawing.

| Tool | Effect | Safety | Summary |
|---|---|---|---|
| [`createLine`](#createline) | Edit | low | Creates a straight line between two points. |
| [`createRectangle`](#createrectangle) | Edit | low | Creates a rectangle, optionally rotated and with rounded corners. |
| [`createCircle`](#createcircle) | Edit | low | Creates a circle from a center and radius, or through three points. |
| [`createArc`](#createarc) | Edit | low | Creates a circular arc from a center, radius and angles, or through three points. |
| [`createPolygon`](#createpolygon) | Edit | low | Creates a polygon from points, or a regular polygon. |
| [`createPolyline`](#createpolyline) | Edit | low | Creates a polyline from vertices of any vertex type, or a rounded shape. |
| [`createLocus`](#createlocus) | Edit | low | Creates a 2D locus (reference point). |
| [`getGeometry`](#getgeometry) | Read-only | low | Reads the type-specific geometry of a 2D primitive. |
| [`setGeometry`](#setgeometry) | Edit | low | Edits the geometry of a 2D primitive. |
| [`editVertices`](#editvertices) | Edit | low | Adds, inserts, changes, deletes, reverses or replaces the vertices of a polygon or polyline. |
| [`queryGeometry`](#querygeometry) | Read-only | low | Answers geometric questions about a 2D primitive: closest point, distance, containment, intersections, tangents and measurements along curves. |
| [`combineShapes`](#combineshapes) | Edit | low | Combines two 2D shapes with a Boolean operation: union, intersection, difference or symmetric difference. |
| [`createText`](#createtext) | Edit | low | Creates a text object. |
| [`getText`](#gettext) | Read-only | low | Reads a text object: its content, character formatting, style and layout. |
| [`editText`](#edittext) | Edit | low | Edits the content and formatting of a text object. |

### createLine

Creates a straight line between two points.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: createLine" · **In runToolBatch:** yes

**Details**

Create a straight line between two points `start` and `end`.

> **Note:** `start` and `end` are both required (`'start' and 'end' points are required`). A value that is given but is not a [point](Common.md#points) is read as (0, 0), without an error.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `start` | [point](Common.md#points) | Yes | Start point. |
| `end` | [point](Common.md#points) | Yes | End point. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createRectangle

Creates a rectangle, optionally rotated and with rounded corners.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: createRectangle" · **In runToolBatch:** yes

**Details**

Create a rectangle centered at `center` with `width` and `height`, optional `angle` (radians). A positive `cornerRadius`, or `cornerDiameters` { alongWidth, alongHeight } for elliptical corners (the corner diameters along the width and along the height side), creates a rounded rectangle; `proportional` makes its corners scale when it is resized interactively.

> **Note:** `width` and `height` must not be zero (`'width' and 'height' must be non-zero`). `center` is not checked: a missing or malformed `center` is read as (0, 0). `cornerDiameters` wins over `cornerRadius`; a `cornerRadius` of 0 or less is ignored, and a negative corner diameter is refused (`'cornerDiameters' must not be negative`). `proportional` has an effect only on a rounded rectangle.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `center` | [point](Common.md#points) | Yes | Center point. |
| `width` | number | Yes | Width, in world units. |
| `height` | number | Yes | Height, in world units. |
| `angle` | number |  | Angle in radians, counter-clockwise. |
| `cornerRadius` | number |  | Corner radius, in world units. Only a value above 0 makes a rounded rectangle; `cornerDiameters` wins when both are given. |
| `cornerDiameters` | object |  | Elliptical corners: the diameters of the corner ellipse. Wins over `cornerRadius`; neither value may be negative. Present in any form, it makes a rounded rectangle; a missing member is 0. |
| `cornerDiameters.alongWidth` | number |  | Corner diameter along the width side, in world units. Default 0. |
| `cornerDiameters.alongHeight` | number |  | Corner diameter along the height side, in world units. Default 0. |
| `proportional` | boolean |  | Rounded rectangle only: its corners scale when it is resized interactively. Default false. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createCircle

Creates a circle from a center and radius, or through three points.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: createCircle" · **In runToolBatch:** yes

**Details**

Create a circle at `center` with `radius`, or the circle through the three points `threePoints`.

> **Note:** `threePoints` wins when it is given. It needs exactly three points (entries that are not points are skipped), else `'threePoints' must hold exactly three points`, and they must not coincide or lie on one line (`failed to create the object: the three points coincide or are collinear`). Otherwise `radius` must be positive (`'radius' must be positive`); `center` is not checked: a missing or malformed `center` is read as (0, 0).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `center` | [point](Common.md#points) |  | Center point. |
| `radius` | number |  | Radius, in world units. |
| `threePoints` | array of [point](Common.md#points) |  | Three points on the circle; wins over `center` and `radius`. 3 items. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createArc

Creates a circular arc from a center, radius and angles, or through three points.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: createArc" · **In runToolBatch:** yes

**Details**

Create a circular arc at `center` with `radius`, `startAngle` and `sweepAngle` (radians, counter-clockwise), or the arc through `threePoints` [start, a point on the arc, end].

> **Note:** `threePoints` wins when it is given, with the same checks as in createCircle. Otherwise `radius` must be positive and `sweepAngle` must not be zero (`'radius' must be positive and 'sweepAngle' non-zero (radians)`); `startAngle` defaults to 0, and a missing or malformed `center` is read as (0, 0).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `center` | [point](Common.md#points) |  | Center point. |
| `radius` | number |  | Radius, in world units. |
| `startAngle` | number |  | Start angle in radians, counter-clockwise. |
| `sweepAngle` | number |  | Sweep angle in radians; positive is counter-clockwise. |
| `threePoints` | array of [point](Common.md#points) |  | Start, a point on the arc and end; wins over `center`, `radius` and the angles. 3 items. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createPolygon

Creates a polygon from points, or a regular polygon.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: createPolygon" · **In runToolBatch:** yes

**Details**

Create a polygon from a `points` array (with `closed`, default true), or a regular polygon from `center`/`radius`/`sides` (optional `startAngle`).

> **Note:** When `sides` is given, the regular polygon is created and `points` is not read: it needs `sides` of at least 3 and a positive `radius` (`a regular polygon needs 'sides' >= 3 and 'radius' > 0`), and a missing or malformed `center` is read as (0, 0). Without `sides`, `points` must hold at least two points (entries that are not points are skipped), else `provide 'points' (>= 2), or 'center'/'radius'/'sides' for a regular polygon`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `points` | array of [point](Common.md#points) |  | The points, in order (at least 2). Not read when `sides` is given. |
| `closed` | boolean |  | Whether the shape is closed. Default true; used only with `points`. |
| `center` | [point](Common.md#points) |  | Center point. |
| `radius` | number |  | Radius, in world units. |
| `sides` | integer |  | Number of sides of a regular polygon, at least 3. When it is given, `points` is not read. A value that is not a number is read as 3. |
| `startAngle` | number |  | Start angle in radians, counter-clockwise. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createPolyline

Creates a polyline from vertices of any vertex type, or a rounded shape.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: createPolyline" · **In runToolBatch:** yes

**Details**

Create a polyline from a `vertices` array. Each vertex is { x, y, type?, arcRadius?, visible? } where type is corner|bezier|cubic|arc|radius and visible false hides the edge to the next vertex. Optional `closed` (default false). Without `vertices`, `center` with `radius` creates a closed circle of four arc vertices, and `center` with `width` and `height` a closed rectangle whose corners are arc vertices with `cornerRadius` (default 0: sharp corners; at most half the shorter side).

> **Note:** `vertices` wins when it is given. It needs at least two vertices (entries without a point are skipped), else `provide 'vertices' (>= 2), each { x, y, type?, arcRadius?, visible? }, or 'center' with 'radius' (circle) or with 'width'/'height' (filleted rectangle)`. Without `vertices`, `radius` wins over `width` and `height`. The circle needs a positive `radius` (`'radius' must be positive`); the rectangle needs a non-zero `width` and `height` and a `cornerRadius` that is not negative (`'width' and 'height' must be non-zero and 'cornerRadius' must not be negative`). A missing or malformed `center` is read as (0, 0).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `vertices` | array of object |  | The vertices, in order (at least 2); each is an object, or a point `[x, y]`. Entries without a point are skipped. |
| `vertices[].x` | number |  | X coordinate, in world units. |
| `vertices[].y` | number |  | Y coordinate, in world units. |
| `vertices[].type` | string |  | One of: `corner`, `bezier`, `cubic`, `arc`, `radius`. Default `corner`. An unknown `type` is read as `corner`. |
| `vertices[].arcRadius` | number |  | Radius of an `arc` vertex, in world units; ignored for the other vertex types. Default 0. |
| `vertices[].visible` | boolean |  | false hides the edge to the next vertex. Default true. |
| `closed` | boolean |  | Whether the shape is closed. Default false; used only with `vertices`. |
| `center` | [point](Common.md#points) |  | Center point. |
| `radius` | number |  | Radius, in world units. |
| `width` | number |  | Width, in world units. |
| `height` | number |  | Height, in world units. |
| `cornerRadius` | number |  | Corner radius, in world units. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createLocus

Creates a 2D locus (reference point).

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: createLocus" · **In runToolBatch:** yes

**Details**

Create a 2D locus (reference/snap point) at `position`.

> **Note:** `position` is not checked: a missing or malformed `position` creates the locus at (0, 0), without an error.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### getGeometry

Reads the type-specific geometry of a 2D primitive.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the type-specific geometry of a 2D primitive (`kind`).

**Line:** start, end, length, angle, midPoint, direction (unit vector).

**Circle:** center, radius, diameter, circumference.

**Arc:** center, radius, startAngle, sweepAngle, endAngle, startPoint and endPoint (the chord ends), midPoint, length (along the arc), chordLength, sagitta.

**Rectangle and RoundedRectangle:** center, width, height, angle, origin (first corner), direction (unit vector along the width side), corners (counter-clockwise from origin), isAxisAligned, plus isSquare (rectangle) or cornerRadius, cornerDiameters { alongWidth, alongHeight } and hasCircularCorners (rounded rectangle).

**Locus:** position, masterSnapPoint, showMasterSnapOutsideSnapBox.

**Polygon:** closed, isFreehand, points (a point whose edge to the next point is hidden has visible false).

**Polyline:** closed, hasCurves, vertices { x, y, type, arcRadius, maxRadius (largest radius that fits an arc vertex), controlPoint (stored control point, when it differs from x/y), visible }. Polygons and polylines additionally return vertex count, area, perimeter, centroid and the clockwise/convex/self-intersecting flags.

> **Note:** The result starts with the [object reference](Common.md#object-references) keys, then `kind`: `Line`, `Circle`, `Arc`, `Rectangle`, `RoundedRectangle`, `Locus`, `Polyline` or `Polygon`. For any other object the call succeeds and returns only the object reference, without `kind`. A value that the object cannot report is left out. The vertex count is the key `vertexCount`; `area`, `perimeter`, `centroid`, `clockwise`, `convex` and `selfIntersecting` follow, each only when it could be computed. A polyline vertex reports `arcRadius` only when it is not 0.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |

### setGeometry

Edits the geometry of a 2D primitive.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: setGeometry" · **In runToolBatch:** yes

**Details**

Edit the geometry of a 2D primitive by uuid; provide the fields of its type.

**Line:** start, end, length, angle, extendStart/extendEnd (lengthen the ends, negative trims), offsetParallel (move sideways, positive to the left of start→end), reverse (swap the ends).

**Circle:** threePoints (3 points on the circle), center, radius, diameter; startAngle/sweepAngle/endAngle turn it into an arc.

**Arc:** threePoints [start, a point on the arc, end], center, radius, startAngle (keeps the end angle), sweepAngle and endAngle (keep the start angle); startAngle with sweepAngle sets both.

**Rectangle and rounded rectangle:** center, angle, width/height (keep the center), origin and direction (place the first corner and the width side, keep the size), bounds { left, top, right, bottom } (unrotated); rounded rectangle also cornerRadius and cornerDiameters { alongWidth, alongHeight }.

**Locus:** position, masterSnapPoint and showMasterSnapOutsideSnapBox (snap behaviour inside a symbol definition). Use editVertices for polygons and polylines.

> **Note:** Only the fields that the type of the object uses are written. The others are ignored, with no entry in `applied` and no error: `cornerRadius` and `cornerDiameters` on a plain rectangle, `angle` on an arc, `radius` on a line, and so on. On a circle, `startAngle`, `sweepAngle` and `endAngle` edit it as an arc, which turns it into an arc unless the sweep stays a full turn. `width` or `height` given alone keeps the other side. Values other than `threePoints` and `bounds` are not type-checked: a given point that is not a [point](Common.md#points) is read as (0, 0), a given number that is not a number as 0 (`radius`, `diameter` and `sweepAngle` then fail with `applied` `false`; the others write 0), and a locus boolean that is not a boolean as `false`. Only `origin`, `direction`, `width`, `height` and the members of `cornerDiameters` fall back to their current values.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `start` | [point](Common.md#points) |  | Used for line. Start point. |
| `end` | [point](Common.md#points) |  | Used for line. End point. |
| `length` | number |  | Used for line. Length, in world units; `start` stays, `end` moves along the line. `applied.length` is false for a line of zero length. |
| `angle` | number |  | Used for line, rectangle and rounded rectangle. Angle in radians, counter-clockwise; a line turns about `start` and keeps its length, a rectangle turns about its center. |
| `extendStart` | number |  | Used for line. Length to add at the start, in world units; negative trims. |
| `extendEnd` | number |  | Used for line. Length to add at the end, in world units; negative trims. |
| `offsetParallel` | number |  | Used for line. Move sideways, positive to the left of start→end. |
| `reverse` | boolean |  | Used for line. `true` swaps the ends; `false` is ignored, with no entry in `applied`. |
| `center` | [point](Common.md#points) |  | Used for circle, arc, rectangle and rounded rectangle. Center point. |
| `radius` | number |  | Used for circle, arc. Radius, in world units. |
| `diameter` | number |  | Used for circle. Diameter, in world units. |
| `threePoints` | array of [point](Common.md#points) |  | Used for circle and arc. Three points on the circle; for an arc: start, a point on the arc, end. `applied.threePoints` is false unless there are exactly three points that are not collinear. 3 items. |
| `startAngle` | number |  | Used for circle, arc. Start angle in radians, counter-clockwise. Alone it keeps the end angle; with `sweepAngle` it sets both. |
| `sweepAngle` | number |  | Used for circle, arc. Sweep angle in radians; positive is counter-clockwise. Alone it keeps the start angle. |
| `endAngle` | number |  | Used for circle and arc. End angle in radians; the start angle is kept. |
| `width` | number |  | Used for rectangle and rounded rectangle. Width, in world units. |
| `height` | number |  | Used for rectangle and rounded rectangle. Height, in world units. `width` and `height` keep the center; the one that is missing keeps its current value. |
| `origin` | [point](Common.md#points) |  | Used for rectangle and rounded rectangle. The first corner. With `direction` it places the rectangle and keeps the size; the one that is missing keeps its current value. |
| `direction` | [point](Common.md#points) |  | Used for rectangle and rounded rectangle. Direction of the width side, a unit vector as getGeometry reports it. See `origin`. |
| `bounds` | [rectangle](Common.md#rectangles) |  | Used for rectangle and rounded rectangle. Unrotated rectangle; all four of `left`, `top`, `right` and `bottom` must be numbers, else `applied.bounds` is false. |
| `cornerRadius` | number |  | Used for rounded rectangle only; a plain rectangle ignores it. Corner radius, in world units. |
| `cornerDiameters` | object |  | Used for rounded rectangle only; a plain rectangle ignores it. A missing member keeps its current value. |
| `cornerDiameters.alongWidth` | number |  | Corner diameter along the width side, in world units. |
| `cornerDiameters.alongHeight` | number |  | Corner diameter along the height side, in world units. |
| `position` | [point](Common.md#points) |  | Used for locus. Insertion point. |
| `masterSnapPoint` | boolean |  | Used for locus. Master snap point flag (snap behaviour inside a symbol definition). |
| `showMasterSnapOutsideSnapBox` | boolean |  | Used for locus. Snap behaviour inside a symbol definition. |

**Result**

| Key | Description |
|---|---|
| `applied` | One entry per value that was given and that the type of the object uses; `true` when it was written. |

The result has no object reference. The keys of `applied` are the parameter names, except `extend` (for `extendStart` and `extendEnd`), `size` (for `width` and `height`), `frame` (for `origin` and `direction`) and `angles` (for `startAngle` together with `sweepAngle`).

Errors: `object not found`; `this object's geometry cannot be edited with setGeometry; polygons and polylines are edited with editVertices` (any object that is not a line, circle, arc, rectangle, rounded rectangle or locus). The call then changes nothing (`rolledBack`).

### editVertices

Adds, inserts, changes, deletes, reverses or replaces the vertices of a polygon or polyline.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: editVertices" · **In runToolBatch:** yes

**Details**

Edit the vertices of a polygon or polyline. `action`: add (append `point`), insert (`point` before `index`), set (change the `point`, `type`, `arcRadius` or edge `visible` flag of the vertex at `index`), delete (`index`), deleteAll, reverse, or replace (every vertex: from `points`, with all edges visible, or from `vertices` { x, y, type?, arcRadius?, visible? } as in createPolyline; at least two; keeps the closed flag). add and insert also take `type`, `arcRadius` and `visible` for the new vertex.

Vertex `type` (corner|bezier|cubic|arc|radius) and `arcRadius` apply to polylines only. `closed`, `clockwise` and `allVerticesVisible` can be set with any action. Returns `applied` and the updated vertex count, area, perimeter, centroid and shape flags.

> **Note:** `action` is `set` when it is missing. `index` counts the vertices from 0 (below 0 counts as 0) and is used by `insert`, `set` and `delete`; `add` appends. A failed edit is not an error: its entry in `applied` is `false`. The key `index` also refers to an object by its internal index (see [Object references](Common.md#object-references)): when `uuid` and `name` do not find the object, the object with the internal index `index` is edited instead. Always send a valid `uuid`. Values are not checked: a `closed`, `clockwise` or `allVerticesVisible` that is not a boolean is read as false, an unknown `type` as `corner`, and an `arcRadius` that is not a number as 0, and they are written.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Vertex index, counting from 0, for `insert` (the new vertex goes before it), `set` and `delete`. Also the reference by internal index; see the Note. |
| `action` | string |  | One of: `add`, `insert`, `set`, `delete`, `deleteAll`, `reverse`, `replace`. Default `set`. |
| `point` | [point](Common.md#points) |  | The point of the vertex for `add` and `insert` (required there) and for `set`. |
| `type` | string |  | One of: `corner`, `bezier`, `cubic`, `arc`, `radius`. Polylines only. For `add` and `insert` the default is `corner`; for `set` it changes the vertex at `index`. |
| `arcRadius` | number |  | Polylines only. Arc radius of the vertex, in world units, at least 0. For `add` and `insert` it is used only when `type` is `arc` (default 0). For `set` it makes the vertex an `arc` vertex with that radius, also when `type` gives another type in the same call; a negative value gives `applied.arcRadius` false. |
| `visible` | boolean |  | Whether the edge from the vertex to the next one is visible. For `add` and `insert` the default is true; for `set` it changes the vertex at `index`. |
| `points` | array of [point](Common.md#points) |  | The points for `replace`, in order; all edges become visible. At least two. `vertices` wins when both are given. |
| `vertices` | array of object |  | The vertices for `replace`, as in createPolyline; at least two. An item without a point is skipped. A polygon takes them as corners. |
| `vertices[].x` | number |  | X coordinate, in world units. |
| `vertices[].y` | number |  | Y coordinate, in world units. |
| `vertices[].type` | string |  | One of: `corner`, `bezier`, `cubic`, `arc`, `radius`. Default `corner`. |
| `vertices[].arcRadius` | number |  | Arc radius, in world units; used only when `type` is `arc`. Default 0. |
| `vertices[].visible` | boolean |  | Whether the edge to the next vertex is visible. Default true. |
| `closed` | boolean |  | Whether the shape is closed. Can be given with any action; `replace` itself keeps the current flag. |
| `clockwise` | boolean |  | Vertex order: true clockwise, false counter-clockwise. Can be given with any action. |
| `allVerticesVisible` | boolean |  | true makes the edge of every vertex visible, false hides them all. Can be given with any action. |

**Result**

The object reference (see [Object references](Common.md#object-references)), `applied` and the measures of the edited shape.

| Key | Description |
|---|---|
| `applied` | One entry for the edit and one for each of `closed`, `clockwise` and `allVerticesVisible` that was given; `true` when it was written. The entry of the edit is named after the `action` (`add`, `insert`, `delete`, `deleteAll`, `reverse`, `replace`). For `set` there is one entry for each of `point`, `type`, `arcRadius` and `visible` that was given; on a polygon `type` and `arcRadius` get no entry, and neither does a `point` that is not a valid point. `replace` with fewer than two vertices gives `replace: false`. |
| `vertexCount` | Number of vertices. |
| `area`, `perimeter`, `centroid` | Measures of the shape, each only when Vectorworks can compute it. |
| `clockwise`, `convex`, `selfIntersecting` | Shape flags, each only when Vectorworks can compute it. |

Errors: `object not found`; `object is not a polygon or a polyline`; `'point' is required to add or insert a vertex`; `unknown 'action' (add, insert, set, delete, deleteAll, reverse, replace)`. After an error the call changes nothing (`rolledBack`).

### queryGeometry

Answers geometric questions about a 2D primitive: closest point, distance, containment, intersections, tangents and measurements along curves.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Answer a geometric question about a 2D primitive without changing it. `operation`: closestPoint (`point`; returns the nearest `point` on the object and its `distance`) and distanceTo (`point`; returns `distance`) for lines, arcs, circles (to the circumference), rectangles, polygons, polylines and loci; contains (`point`; true inside or on the boundary) for circles, rectangles and closed polygons/polylines; intersect (returns `points`) with the object `otherUuid` or the segment `lineStart`-`lineEnd`: lines, arcs, circles, rectangles, polygons and polylines intersect segments and line objects, arcs and circles also intersect each other; pointAt (`angle` in radians; returns `point`) and tangentPoints (`point`; returns the circle `points` whose tangents pass through it, none from inside) for circles.

For polygons and polylines also: curveLength (returns `length`); pointAtDistance (`distance` along the curve from its start, from 0 to its length; returns the `point`, the unit `tangent` (the direction of the curve there) and the `curvature` (1 / radius, 0 along straight edges); tangent and curvature are left out where the curve has no direction); divide (`count` points, 2 to 10000, equally spaced along the curve from its start; `includeEnd` true (default) puts the last point at the end, which is the start again on a closed curve, false spaces them by the length / count and leaves the end out; returns `points`).

Polygons and polylines are measured along their true curve, as drawn (arcs and splines, not their control points): the outer path with its hidden edges and its closing edge, without holes; this applies to closestPoint, distanceTo, curveLength, pointAtDistance and divide. contains and intersect use the vertex polygon instead (straight edges between the vertex points, curve vertices taken as corners): there is no true-curve containment test.

Rectangles are measured along their four corners (corner rounding ignored).

> **Note:** Rounded rectangles count as rectangles. `intersect` with `otherUuid` works when one of the two objects is a line (the other one can then be any object that `intersect` takes with a segment) or when both are arcs or circles; any other pair is refused. `otherUuid` wins over `lineStart` and `lineEnd`. `pointAt` and `tangentPoints` take circles only; an arc is refused. `contains` on an open polygon or polyline is not refused: it returns `false`, also for a point on its edges.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `operation` | string | Yes | One of: `closestPoint`, `distanceTo`, `contains`, `intersect`, `pointAt`, `tangentPoints`, `curveLength`, `pointAtDistance`, `divide`. |
| `point` | [point](Common.md#points) |  | The point of closestPoint, distanceTo, contains and tangentPoints (required for them). |
| `otherUuid` | string |  | For intersect: UUID of the other object. Looked up by UUID only. |
| `lineStart` | [point](Common.md#points) |  | For intersect: start of the segment. Used together with `lineEnd`; a malformed point reads as (0, 0). |
| `lineEnd` | [point](Common.md#points) |  | For intersect: end of the segment. Used together with `lineStart`. |
| `angle` | number |  | For pointAt (required there). Angle in radians, counter-clockwise. |
| `distance` | number |  | For pointAtDistance (required there). Distance along the curve from its start, from 0 to its length, in world units. |
| `count` | integer |  | For divide (required there). Number of points, 2 to 10000. |
| `includeEnd` | boolean |  | For divide. true (default) puts the last point at the end of the curve; false spaces the points by length / count and leaves the end out. |

**Result**

The result has no object reference. Its keys depend on the `operation`:

| Operation | Keys |
|---|---|
| `closestPoint` | `distance` and `point`, the nearest point on the object. |
| `distanceTo` | `distance`. |
| `contains` | `contains`, true or false. |
| `intersect` | `points`, the crossing points; an empty list when the objects do not cross. |
| `pointAt` | `point`. |
| `tangentPoints` | `points`, the points on the circle whose tangents pass through `point`; an empty list from inside. |
| `curveLength` | `length`, in world units. |
| `pointAtDistance` | `point`, the unit `tangent` and the `curvature`; the last two are left out where the curve has no direction. |
| `divide` | `points`. |

Errors: `object not found`; `unknown 'operation' (closestPoint, distanceTo, contains, intersect, pointAt, tangentPoints, curveLength, pointAtDistance, divide)` (also for a missing `operation`); `'<operation>' needs 'point'`; `the 'otherUuid' object was not found`; `'intersect' needs 'otherUuid', or 'lineStart' and 'lineEnd'`; `'intersect' does not support this combination of objects`; `'pointAt' needs the number 'angle' (radians)`; `'<operation>' supports circles only`; `'contains' supports circles, rectangles, polygons and polylines`; `'<operation>' supports lines, arcs, circles, rectangles, polygons, polylines and loci`; `'<operation>' supports polygons and polylines only`; `'pointAtDistance' needs 'distance', a number from 0 to the length of the curve, <length> (world units)`; `'divide' needs 'count', a whole number of points from 2 to 10000`; `'includeEnd' must be true or false`; `Vectorworks could not measure the curve of the polygon or polyline: it needs two vertices or more and a curve that is not degenerate`; `failed to read the circle` (pointAt); `Vectorworks could not find the point at 'distance' on the curve` (pointAtDistance).

### combineShapes

Combines two 2D shapes with a Boolean operation: union, intersection, difference or symmetric difference.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: combineShapes" · **In runToolBatch:** yes

**Details**

Combine two 2D shapes with a Boolean operation, as Modify &gt; Add Surface, Clip Surface and Intersect Surface do, but keeping the originals unless asked. `operation`: union (the area of either shape), intersection (the area of both), difference (the first shape minus the second: `firstUuid` minus `secondUuid`; a line as the second shape cuts the first into pieces where it crosses it completely) or symmetricDifference (the area of exactly one of them).

`firstUuid` and `secondUuid` are two different shapes: lines, rectangles, rounded rectangles, ovals, arcs and circles, polygons (not freehand) and polylines; not text, groups, symbols, plug-in objects or 3D objects. They must be coplanar: when they are in different planes (e.g. one in the screen plane and one in the layer plane, in Top/Plan), the second shape is first moved into the plane of the first, as Modify &gt; Add Surface does, which changes the plane of the second original and adds `planesAligned` true to the result; shapes that are not coplanar are refused.

An open polygon or polyline of three or more vertices counts as closed by a straight edge, an arc by its chord; a line encloses no area, so it is meaningful only as the second shape of a difference. The first shape must be in a layer, a symbol definition or a group of these (not in a wall, a plug-in object, a viewport or a group of one); the second shape too when the call changes it (`deleteOriginals` both, or a move into the plane of the first).

The results are new 2D objects of any type (usually polylines; a polygon, or a copy of a shape when no new outline is needed, e.g. a copy of the first shape for a difference without overlap) with the graphic attributes, records and visibility of the first shape and its class (`class` gives another; `useClassAttributes` makes the attributes follow the class).

They go into the container of the first shape, in front of its objects, unlocked, and selected only with `select`; the bounds of the groups around them follow. The originals stay unchanged, apart from a plane alignment, unless `deleteOriginals` is first or both (default none); nothing is deleted when no shape results. A locked first shape can be combined, but a locked shape that the call would delete or move into another plane is refused.

A combination without area (an intersection of shapes that do not overlap, a difference whose second shape covers the first or whose first shape is a line, a symmetric difference of equal shapes; Vectorworks reports a failure of its modeling the same way) is a success with no shapes and a `note`; an empty union is an error. `name` names the single result: refused when the shapes combine into several shapes or when another object has that name.

Every argument is checked before anything changes: a refused call changes nothing; a call is one undo step, which also restores the planes of aligned shapes. Returns `operation`, `count`, `shapes` (the references of the new objects), `deleted` (the UUIDs of the deleted originals), `planesAligned` (true when the planes of the shapes were moved into one) and, without results, `note`.

> **Note:** A polygon or polyline of fewer than two vertices, or a polyline of two vertices that coincide or are not both corner vertices, is not a shape that combineShapes takes, although the list above does not say so.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `operation` | string | Yes | One of: `union`, `intersection`, `difference`, `symmetricDifference`. |
| `firstUuid` | string | Yes | UUID of the first shape. The new shapes take its class, attributes and container. |
| `secondUuid` | string | Yes | UUID of the second shape. It must differ from `firstUuid`. |
| `deleteOriginals` | string |  | One of: `none`, `first`, `both`. Default `none`. `first` deletes the first shape, `both` deletes both; nothing is deleted when no shape results. |
| `class` | string |  | Creation option: class of the new shapes; created when missing. Without it they keep the class of the first shape. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new shape. Refused when the shapes combine into several shapes, or when another object has that name. |
| `select` | boolean |  | Creation option: select the new shapes. |
| `useClassAttributes` | boolean |  | Creation option: the attributes of the new shapes follow their class: `class`, or else the class of the first shape. It does not need `class`. |

**Result**

| Key | Description |
|---|---|
| `operation` | The operation that was run. |
| `count` | Number of new shapes. |
| `shapes` | The new shapes, as [object references](Common.md#object-references). |
| `deleted` | UUIDs of the originals that were deleted; empty when nothing was deleted. |
| `planesAligned` | `true` when the second shape was moved into the plane of the first; left out otherwise. |
| `note` | Only without results: the reason, and that nothing was created and the originals were kept, also with `deleteOriginals`. |

Errors: a missing `operation`; an unknown `operation` or `deleteOriginals`; `the 'firstUuid' object was not found` (or `'secondUuid'`); `'firstUuid' and 'secondUuid' are the same object: combineShapes combines two different shapes`; `the '<key>' object is not a shape that combineShapes takes: it takes …` with the list above; the first shape is not in a layer, a symbol definition or a group of these; the second shape is not in such a container and the call would delete it or move it into another plane; a locked shape that the call would delete or move into another plane (unlock it first with editObject `locked` false); `the shapes are not coplanar: …`; `'name' must be a text`; `the name '<name>' is used by another object, …`; `'name' names one object, but the shapes combine into <count> shapes: …`; `Vectorworks gave no union of the shapes: its modeling failed, or the shapes enclose no area (lines)`; `Vectorworks refused to combine the shapes`; `Vectorworks could not insert the combined shapes into the container of the first shape`. A call that fails is rolled back (`rolledBack`).

### createText

Creates a text object.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: createText" · **In runToolBatch:** yes

**Details**

Create a text object from `text` (UTF-8; "\n" and "\r\n" become "\r", the line separator of text objects; at most 16383 UTF-16 code units) at `origin`, the alignment point of the text (world units): the text is placed so that the point its alignment sets lies there. Optional `width` (world units, positive) makes a wrapped text that breaks its lines at that width.

The formatting of the whole text is written in this order, so that the explicit values override those of the text style: `textStyle` (the name or the resource UUID of a text style of the drawing, getResources lists them with resourceType `textStyle`; "" for none) or `textStyleByClass` true (the text follows the text style of its class); `font` (a font name); `size` (world units) or `sizePoints` (points); the style flags `bold`, `italic`, `underline`, `outline` and `shadow` (outline and shadow show on macOS only); `color`.

Then the layout: `horizontalAlignment` (left|center|right|justify), `verticalAlignment` (topBox|topBaseline|centerBox|bottomBaseline|bottomBox), `lineSpacing` (single|oneAndHalf|double, or custom with `leading`, the line distance in world units), `angle` (radians, counter-clockwise, about the origin) and `flipped` (mirrored vertically). What is not given comes from the text defaults of the document.

Every argument is checked before anything is created: a wrong type, an unknown name, font or text style, `size` together with `sizePoints`, or a width, size or leading that is not positive refuses the call, which then creates nothing. The creation options (class, name, select, useClassAttributes) are applied before the formatting. Returns the object reference and `applied` (true/false for each formatting and layout argument given, origin included; leading under lineSpacing); getText reads the text back.

> **Note:** `textStyle` and `textStyleByClass` are refused together. `textStyleByClass` takes only `true`; `textStyle` `""` removes the text style. `lineSpacing` `custom` needs `leading`, and `leading` needs `lineSpacing` `custom`. The creation options (`class`, `name`, `select`) are applied before the formatting, so `class` does not override a formatting argument. A refused call creates nothing.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `text` | string | Yes | The text (UTF-8); "\n" starts a new line. |
| `origin` | [point](Common.md#points) | Yes | Alignment point of the text, in world units. |
| `width` | number |  | Wrapping width in world units; makes a wrapped text. |
| `textStyle` | string |  | Name or resource UUID of a text style; an empty string for none. |
| `textStyleByClass` | boolean |  | Use the text style of the class. |
| `font` | string |  | Font name. |
| `size` | number |  | Text size in world units (not together with `sizePoints`). |
| `sizePoints` | number |  | Text size in points. |
| `color` | [color](Common.md#colors) |  | Text color. |
| `bold` | boolean |  | Bold style. |
| `italic` | boolean |  | Italic style. |
| `underline` | boolean |  | Underline style. |
| `outline` | boolean |  | Outline style (shown on macOS only). |
| `shadow` | boolean |  | Shadow style (shown on macOS only). |
| `horizontalAlignment` | string |  | One of: `left`, `center`, `right`, `justify`. |
| `verticalAlignment` | string |  | One of: `topBox`, `topBaseline`, `centerBox`, `bottomBaseline`, `bottomBox`. |
| `lineSpacing` | string |  | One of: `single`, `oneAndHalf`, `double`, `custom`. |
| `leading` | number |  | Line distance in world units, for custom line spacing. |
| `angle` | number |  | Rotation in radians, counter-clockwise, about the origin. |
| `flipped` | boolean |  | Mirror the text vertically. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The [object reference](Common.md#object-references) of the new text and:

| Key | Description |
|---|---|
| `applied` | `true` or `false` under the name of each argument that was written: `origin` (always), the formatting arguments (`textStyle`, `textStyleByClass`, `font`, `size`, `sizePoints`, each style flag given, `color`) and the layout arguments (`horizontalAlignment`, `verticalAlignment`, `lineSpacing` with `leading`, `angle`, `flipped`). `width` is not listed: it shapes the new text. |

Errors: `'text' must be a text that is not empty`; `'text' is too long: Vectorworks edits text objects of at most 16383 UTF-16 code units`; `'origin' must be a point { x, y } in world units`; `give either 'textStyle' or 'textStyleByClass'`; `'textStyleByClass' takes true, which makes the text follow the text style of its class; 'textStyle' "" removes the text style`; `'textStyle' "<name>" is neither the name nor the UUID of a text style of the drawing (getResources lists them with resourceType 'textStyle'); "" removes the text style`; `'font' "<name>" is no font that Vectorworks knows`; `'textStyle' must be the name or the UUID of a text style, or ""`; `'font' must be the name of a font`; `give either 'size' (world units) or 'sizePoints' (points)`; a size, width or leading that is not positive; `'lineSpacing' custom needs 'leading', the line distance in world units, and 'leading' needs 'lineSpacing' custom`; a wrong type or an unknown name of an alignment, line spacing, style flag, color, angle or flipped value. A refused call creates nothing.

### getText

Reads a text object: its content, character formatting, style and layout.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read a text object by uuid, name or index. Character indices are 0-based UTF-16 code units (a character outside the Basic Multilingual Plane counts two); lengths are in world units, angles in radians. Returns `text` (complete; lines separated by "\r"), `length`, `lineCount` and `lines`, the lines after wrapping as { start, text }, paged like findObjects with `lineLimit` (default 100) and `lineOffset` (count, returned, offset, limit, truncated, nextOffset, items); `origin` (the alignment point), `angle`, `flipped` (mirrored vertically) and `boxCorners` (top-left, top-right, bottom-right and bottom-left of the text box, rotated with the text); `horizontalAlignment`, `verticalAlignment`, `lineSpacing` (with `leading` for custom spacing), `width` and `wrapped`; the formatting of character 0: `font`, `size` (world units), `sizePoints`, `style` (the names of its flags: bold, italic, underline, outline, shadow), `customStyle` (diagonalFraction|verticalFraction|superscript|subscript, when it has one), `color` and `tracking` (character spacing, 1 = normal); `textStyle` of the whole text: { byClass, name, uuid }, { byClass: true } for a class without a text style, { mixed: true } when the characters follow different text styles, or null for none; `styleRuns`, the formatting runs in order as { start, length } with the same formatting keys and the `textStyle` of the run, paged with `runLimit` (default 100) and `runOffset`; `tabStops` ({ offset in world units from the left of the text, alignment left|right|center|decimal }, sorted by offset), `repeatingTabStop` (the spacing of evenly spaced tab stops, 0 otherwise), `tightFill` and `isLinkedToRecord`.

The names and keys are those that createText and editText take.

> **Note:** `lines` and `styleRuns` are paged lists, each an object with `count`, `returned`, `offset`, `limit`, `truncated`, `nextOffset` (only when `truncated` is true) and `items`. An item of `lines` is `{ start, text }`, where `start` is the character index of the first character of the line. The two lists are paged separately, and `getText` has no `countOnly`. A `lineLimit` or `runLimit` below 1, an offset below 0 or a value that is not a number is refused with `'lineLimit' must be a number of at least 1 and 'lineOffset' a number of at least 0` (`'runLimit'` and `'runOffset'` for the runs). An object that is not a text object is refused with `the object is not a text object: getText and editText take text objects only`. An object that is not found is refused with `object not found (provide 'uuid', 'name' or 'index')`. For an empty text (`length` 0) the formatting keys of character 0 (`font`, `size`, `sizePoints`, `style`, `customStyle`, `color`, `tracking`) are left out; `textStyle` and `styleRuns` are still returned.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `lineLimit` | integer |  | The maximum number of `lines` in the page; at least 1. Default 100. |
| `lineOffset` | integer |  | The number of lines to skip; not negative. Default 0. |
| `runLimit` | integer |  | The maximum number of `styleRuns` in the page; at least 1. Default 100. |
| `runOffset` | integer |  | The number of formatting runs to skip; not negative. Default 0. |

### editText

Edits the content and formatting of a text object.

> **Effect:** Edit · **Safety:** low · **Undo:** one step "MCP: editText" · **In runToolBatch:** yes

**Details**

Edit a text object by uuid, name or index; the call is one undo step. Character indices and counts are 0-based UTF-16 code units (a character outside the Basic Multilingual Plane counts two); lengths are in world units, angles in radians; in new text "\n" and "\r\n" become "\r", the line separator of text objects. Every argument is checked before anything changes: a wrong type, an unknown name, font or text style, a range outside the text, a size, width, leading, interval or offset that is not positive, an empty text, more than one content change, a call without a change, or an object that is no text refuses the call, which then changes nothing.

The changes run in this order.

1. Content, at most one of: `setText` (replaces the whole text, which takes the formatting of the last character; the old and the new text together must stay within 16383 code units), `insertText` { text, at } (inserts before character `at`, where the length of the text appends; the new text takes the formatting of the character before it, at 0 that of the first character), `appendText`, `deleteText` { first, count } (count defaults to the rest of the text; the whole text cannot be deleted).

2. Character formatting of the range `first` (default 0) and `count` (default: the rest) of the text after the content change, in this order: `textStyle` (the name or the resource UUID of a text style of the drawing; "" detaches the range from its text style and keeps its formatting) or `textStyleByClass` true (the range follows the text style of the class of the text); `font`; `size` (world units) or `sizePoints` (points); the style flags `bold`, `italic`, `underline`, `outline` and `shadow` (only the flags given change: each character keeps its other flags and its superscript, subscript or fraction style); `color`.

3. **Layout:** `horizontalAlignment` and `verticalAlignment` (a new alignment keeps the text where it is and moves its origin, the alignment point, as Vectorworks does), `lineSpacing` (custom needs `leading`), `width` (the wrapping width; the text wraps at it), `wrapped` (true wraps at the current width, false breaks the lines only at line separators; not false together with `width`), `origin` (moves the text so that its alignment point lies there), `angle` and `flipped`. The layout comes after the formatting because a text style applied to the whole text also sets its alignment and spacing.

4. **Tab stops:** `repeatingTabStop` (re-spaces every tab stop at multiples of the interval, left aligned), `removeTabStops` (indices into getText `tabStops`; tab stop 0 cannot be removed), `moveTabStop` { index, offset } (the index after the removals; the tab stops stay sorted by offset), `addTabStops` (the offsets of new left tab stops).

5. `unlinkFromRecord` true unlinks a text that is linked to a record field (refused for another text).

Returns the object reference, `applied` (true/false for each argument given; leading under lineSpacing), `length` and `lineCount`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `setText` | string |  | Replaces the whole text. Not empty; the old and the new text together at most 16383 UTF-16 code units. |
| `insertText` | object |  | Inserts a text before a character. Give `text` and `at`. |
| `insertText.text` | string | Yes | The text to insert; not empty; "\n" starts a new line. With the old text at most 16383 UTF-16 code units. |
| `insertText.at` | integer | Yes | Character index before which the text goes: 0 is the start, the length of the text is the end. |
| `appendText` | string |  | Text to add at the end. Not empty; with the old text at most 16383 UTF-16 code units. |
| `deleteText` | object |  | Deletes a range of characters. The whole text cannot be deleted. |
| `deleteText.first` | integer |  | Index of the first character to delete, below the length of the text. Default 0. |
| `deleteText.count` | integer |  | Number of characters to delete, from 1 to the rest of the text. Default: the rest of the text. |
| `first` | integer |  | First character of the range that the character formatting is written to, counted in the text after the content change. Default 0. Read only when a formatting argument is given (`textStyle`, `textStyleByClass`, `font`, `size`, `sizePoints`, a style flag or `color`). |
| `count` | integer |  | Number of characters of that range, from 1 to the rest of the text. Default: the rest of the text. |
| `width` | number |  | Wrapping width in world units; makes a wrapped text. |
| `wrapped` | boolean |  | True wraps at the current width, false breaks the lines only at line separators; not false together with `width`. |
| `repeatingTabStop` | number |  | Re-spaces every tab stop at multiples of the interval, left aligned. |
| `removeTabStops` | array of integer |  | Indices into getText `tabStops`; tab stop 0 cannot be removed. |
| `moveTabStop` | object |  | Moves one tab stop. Give `index` and `offset`. |
| `moveTabStop.index` | integer | Yes | Index of the tab stop among those left after `removeTabStops`; 0 is the first. |
| `moveTabStop.offset` | number | Yes | New offset in world units from the left of the text. Positive. |
| `addTabStops` | array of number |  | The offsets of new left tab stops. |
| `unlinkFromRecord` | boolean |  | True unlinks a text that is linked to a record field (`isLinkedToRecord` of getText); refused for a text that is not linked. `false` changes nothing and adds no entry to `applied`. |
| `textStyle` | string |  | Name or resource UUID of a text style; an empty string for none. |
| `textStyleByClass` | boolean |  | Use the text style of the class. Takes only `true`; refused together with `textStyle`. |
| `font` | string |  | Font name. |
| `size` | number |  | Text size in world units (not together with `sizePoints`). |
| `sizePoints` | number |  | Text size in points. |
| `color` | [color](Common.md#colors) |  | Text color. |
| `bold` | boolean |  | Bold style. |
| `italic` | boolean |  | Italic style. |
| `underline` | boolean |  | Underline style. |
| `outline` | boolean |  | Outline style (shown on macOS only). |
| `shadow` | boolean |  | Shadow style (shown on macOS only). |
| `horizontalAlignment` | string |  | One of: `left`, `center`, `right`, `justify`. |
| `verticalAlignment` | string |  | One of: `topBox`, `topBaseline`, `centerBox`, `bottomBaseline`, `bottomBox`. |
| `lineSpacing` | string |  | One of: `single`, `oneAndHalf`, `double`, `custom`. |
| `leading` | number |  | Line distance in world units, positive. Required with `lineSpacing` `custom` and refused without it. |
| `origin` | [point](Common.md#points) |  | Alignment point of the text, in world units. |
| `angle` | number |  | Rotation in radians, counter-clockwise, about the origin. |
| `flipped` | boolean |  | Mirror the text vertically. |

**Result**

The [object reference](Common.md#object-references) and:

| Key | Description |
|---|---|
| `applied` | `true` or `false` under the name of each argument that was given: `setText`, `insertText`, `appendText` or `deleteText`; the formatting arguments (`textStyle`, `textStyleByClass`, `font`, `size`, `sizePoints`, each style flag given, `color`); the layout arguments (`horizontalAlignment`, `verticalAlignment`, `lineSpacing` with `leading`, `width`, `wrapped`, `origin`, `angle`, `flipped`); `repeatingTabStop`, `removeTabStops`, `moveTabStop`, `addTabStops` and `unlinkFromRecord`. `removeTabStops` and `addTabStops` are reported only when the list is not empty, `unlinkFromRecord` only when it is `true`. |
| `length` | Length of the text after the call, in UTF-16 code units. |
| `lineCount` | Number of lines after wrapping. |

Errors: `object not found (provide 'uuid', 'name' or 'index')`; `the object is not a text object: getText and editText take text objects only`; `give at most one of 'setText', 'insertText', 'appendText' and 'deleteText' per call`; `'<key>' must be a text that is not empty`; `'<key>' is too long …: Vectorworks edits text objects of at most 16383 UTF-16 code units`; `'insertText' must be { text, at }` and `'insertText' needs 'at', a character index from 0 (the start) to <length> (the end of the text)`; `'deleteText' must be { first, count }`, `'deleteText' is outside the text: …` and `'deleteText' cannot delete the whole text: …`; `the formatting range is outside the text: …`; `'width' wraps the text at that width; it cannot be combined with 'wrapped' false`; `tab stop 0 cannot be removed: …`; `'removeTabStops' must be an array of indices of the <n> tab stops of the text (getText 'tabStops')`; `'moveTabStop' must be { index, offset }: …`; `'addTabStops' must be an array of offsets (world units, positive)`; `'unlinkFromRecord': the text is not linked to a record field`; the formatting and layout refusals of createText; `nothing to change: give a content, formatting, layout, tab stop or 'unlinkFromRecord' argument`. A refused call changes nothing (`rolledBack`).

## Objects

> **Group:** `Objects` · **Group ID:** `objects` · **Active by default:** Yes · **Safety level:** medium · **Tools:** 12

**Find, inspect and edit any object: attributes, transforms, containers, plug-in parameters and records.**

Inspect and edit any existing object by its stable uuid: find by criteria or by picking a point, read info (also the 3D bounding box and the members of groups, layers and other containers) and graphical attributes, set pen/fill/opacity/markers/drop shadow, copy attributes between objects, transform, rename, re-class, move between containers (also into a group), ungroup groups, convert to polygons/polylines, read or write plug-in (PIO) parameters (with their types and pop-up choices), and read the user data records attached to any object.

Read the definition of any installed plug-in object by its universal name (getPluginDefinition: kind, parameters, pop-up choices) and create plug-in objects that no group has a create tool for (createPluginObject; doors, windows, plants, data tags, ... are made with their own tools, which it names). Identify a plug-in object by its `parametricName` - never infer its kind from the type code alone, from attached records or from its IFC entity.

IFC data (IFC entity, standard and custom property sets, IFC property types) is read with the IFC group tools getObjectIFCData, getIFCPsetDefinition and listIFCPsets, not with getObjectRecords or getResourceDetails. Search results report `count` as the total number of matches and `truncated` when the list is cut off; a truncated list is only a sample, so never state totals, absence or what every object has from it.

Each edit runs as its own named, undoable Vectorworks operation.

| Tool | Effect | Safety | Summary |
|---|---|---|---|
| [`findObjects`](#findobjects) | Read-only | low | Finds the objects that match a criteria string. |
| [`getObjectsAtPoint`](#getobjectsatpoint) | Read-only | low | Finds the objects at a point. |
| [`getObjectInfo`](#getobjectinfo) | Read-only | low | Returns the identity, class, layer, bounds, state and container of an object. |
| [`getObjectAttributes`](#getobjectattributes) | Read-only | low | Returns the graphical attributes of an object. |
| [`setObjectAttributes`](#setobjectattributes) | Edit | medium | Sets graphical attributes of an object: pen, fill, opacity, markers, drop shadow and more. |
| [`copyAttributes`](#copyattributes) | Edit | medium | Copies the graphical attributes of one object onto other objects. |
| [`editObject`](#editobject) | Edit | medium | Moves, rotates, scales, mirrors, duplicates, regroups, converts, resets or deletes an object, or changes its name and class. |
| [`getObjectParameters`](#getobjectparameters) | Read-only | low | Reads the parameters of a plug-in object. |
| [`getObjectRecords`](#getobjectrecords) | Read-only | low | Reads the data records attached to an object. |
| [`setObjectParameter`](#setobjectparameter) | Edit | medium | Writes one or more parameters of a plug-in object. |
| [`getPluginDefinition`](#getplugindefinition) | Read-only | low | Describes an installed plug-in object: its kind, parameters and pop-up choices. |
| [`createPluginObject`](#createpluginobject) | Edit | medium | Creates a plug-in object that has no dedicated create tool. |

### findObjects

Finds the objects that match a criteria string.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Find objects matching a Vectorworks criteria string (e.g. "(T=RECT)", "(C='My Class')", "ALL"). Returns uuid/type/typeName/name for up to `limit` matches (default 200) starting at `offset` (default 0). `count` is the total number of matches, `returned` the number listed in `objects`, and `truncated` is true when more matches follow; fetch them with `offset` set to `nextOffset`, or pass `countOnly` to get just `count`.

Offsets stay valid only while the drawing is unchanged. To count or check existence, prefer a targeted criteria with `countOnly` over listing "ALL". The search covers objects on design and sheet layers, inside groups and in design layer viewports. `notSearched` lists the scope keywords missing from the criteria: INSYMBOL (inside symbol definitions), INOBJECT (inside plug-in objects), INVIEWPORT (viewport annotations and crop groups), INOBJPATH and INOBJPROFILE (plug-in object paths and profile groups); prefix them to search there ("INSYMBOL & INOBJECT & (T=RECT)").

A count of 0 only means no match within that scope. Parametric plug-in objects (type 86) also report `parametricName` and `localizedParametricName`, which say what the object is (e.g. "Window", "Door", "Plant"). Find plug-in objects by their `parametricName` with criteria such as "(PON='Window')". Criteria that do not compile return an error naming the problem; a valid criteria with no match returns count 0.

Names in the criteria (record, field, class, plug-in) are not validated: a misspelled or nonexistent name compiles and also returns count 0 (internal `NNA_` record names are refused with an error). "(N='...')" matches the Vectorworks object name only, case-insensitively: without wildcards it is an exact name, '\*' matches any run of characters and '?' one character ("(N='\*door\*')"); these wildcards cannot be escaped.

Quote strings with single quotes and double a quote inside a name ("(N='O''Brien')"). An exact name finds the object wherever it is; a wildcard pattern searches the objects on design and sheet layers including groups. N does not match IFC names, IFC property-set values or record field values; read IFC data with the IFC group tools.

> **Note:** With `countOnly` the result has the paging keys `count`, `returned`, `offset`, `limit` and `truncated` but no `objects`, so it is more than "just `count`". `notSearched` is given in every case.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `criteria` | string | Yes | A Vectorworks criteria string, for example `(T=RECT)` or `(C='My Class')`. It must compile and must not refer to an internal IFC record format. |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

**Result**

| Key | Description |
|---|---|
| `count` | The total number of matches. |
| `returned` | The number of objects in `objects` (0 with `countOnly`). |
| `offset` | The `offset` that was used. |
| `limit` | The `limit` that was used. |
| `truncated` | `true` when more matches follow this page. |
| `nextOffset` | The `offset` of the next page; only when `truncated` is `true`. |
| `objects` | The matches as [object references](Common.md#object-references); left out with `countOnly`. |
| `notSearched` | The list of scope keywords that the criteria does not contain (see Details); always present, also with `countOnly`. |

Errors: `'criteria' is required (a Vectorworks criteria string, e.g. "(T=RECT)" or "(C='My Class')")` when `criteria` is missing, empty or not a string; `criteria cannot reference internal IFC record formats; use the IFC tools instead`; `invalid criteria: <the compile error>`; and for the paging arguments `'limit' must be at least 1`, `'offset' must not be negative`, `'limit' must be a number` (likewise for `offset`) and `'countOnly' must be true or false`.

### getObjectsAtPoint

Finds the objects at a point.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Find the objects located at a world `point`, optionally within a `radius`. `traverse` selects which objects are tested (visibleObjects by default, allObjects, selectedObjects, editableObjects) and `descend` which containers are entered (none by default, groups, viewports, all); unknown values return an error and the applied values are echoed back. Returns up to `limit` object references (default 50) starting at `offset`, front-most first, with `count`, `returned`, `truncated` and `nextOffset` as in findObjects; `countOnly` returns just `count`.

> **Note:** With `countOnly` the result has the paging keys (`count`, `returned` 0, `offset`, `limit`, `truncated`) but no `objects`. A missing `point` is refused; a `point` that is not a valid point is read as (0, 0), so the search runs at the origin.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `point` | [point](Common.md#points) | Yes | The world point to test. A value that is not a point is read as (0, 0). |
| `radius` | number |  | Pick radius around `point`, in world units. Default 0. |
| `traverse` | string |  | Which objects are tested. One of: `allObjects`, `visibleObjects`, `selectedObjects`, `editableObjects`. Default `visibleObjects`. |
| `descend` | string |  | Which containers are entered. One of: `none`, `groups`, `viewports`, `all`. Default `none`. |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

**Result**

| Key | Description |
|---|---|
| `count`, `returned`, `offset`, `limit`, `truncated`, `nextOffset`, `objects` | The page of objects found, as for [`findObjects`](#findobjects) (there is no `notSearched`). |
| `traverse` | The `traverse` that was used. |
| `descend` | The `descend` that was used. |

Errors: `'point' is required`; `unknown 'traverse'; use allObjects | visibleObjects | selectedObjects | editableObjects` (also for a `traverse` that is not a string); `unknown 'descend'; use none | groups | viewports | all`; and the paging errors listed for [`findObjects`](#findobjects).

### getObjectInfo

Returns the identity, class, layer, bounds, state and container of an object.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Return identity, class, layer, bounds, area, perimeter and visible/locked/selected state for one object, its internal `index`, and as object references its `parent` container (layer, group, symbol definition, ...) and its `next` / `previous` neighbours in the parent's stacking order (`next` is drawn in front). Plug-in objects also report `parametricName` and `localizedParametricName`.

`bounds3D` { min: {x,y,z}, max: {x,y,z} }, `center3D` {x,y,z} and `size3D` {x,y,z} (the extents along X, Y and Z; z is the height) give the 3D bounding box in world units with world Z (the elevation of a design layer included; inside a symbol definition, in the coordinates of the definition). They are left out when the box is flat at z = 0, as it is for a 2D object in the layer plane or the screen plane, which has no elevation in it (use `bounds`), and for a group or layer of such objects only.

`memberCount` is the number of direct members of an object that holds members: a layer, a group or a symbol definition (also 0), and any other object with members, such as the inserts of a wall, the profile of an extrude or the geometry of a plug-in object or a roof (generated: Vectorworks rebuilds that geometry when the object is reset, so changes to it do not last).

With `includeMembers` true, `members` lists them as object references in stacking order (back to front), paged like findObjects: up to `memberLimit` (default 50) starting at `memberOffset` (default 0), with `count`, `returned`, `truncated`, `nextOffset` and `objects`. `name` is the exact Vectorworks object name; not finding it does not mean no object holds that value in a record field, IFC data or plug-in parameter - search those with findObjects criteria.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `includeMembers` | boolean |  | Add `members`, a page of the direct members of a container. Must be `true` or `false`. Default: `false`. |
| `memberLimit` | integer |  | With `includeMembers`: the maximum number of members in the page (at least 1). Default 50. |
| `memberOffset` | integer |  | With `includeMembers`: the number of members to skip (at least 0). Default 0. |

**Result**

Keys other than the object reference are left out when Vectorworks gives no value for them.

| Key | Description |
|---|---|
| `uuid`, `type`, `typeName`, `name` | The [object reference](Common.md#object-references); a plug-in object also has `parametricName` and `localizedParametricName`. |
| `bounds` | The 2D bounding [rectangle](Common.md#rectangles), in world units. |
| `bounds3D`, `center3D`, `size3D` | The 3D bounding box, its center and its size (see Details); left out when the box is flat at z = 0. |
| `area`, `perimeter` | The area and the perimeter, for an object that has them. |
| `visible`, `locked`, `selected` | The state of the object. |
| `class`, `layer` | The names of the class and of the layer of the object. |
| `index` | The internal index of the object. |
| `memberCount` | The number of direct members, for an object that holds members. |
| `members` | With `includeMembers` on an object that reports `memberCount` (a layer, group, symbol definition, or any object with at least one member): the page of members, `{ count, returned, offset, limit, truncated, nextOffset, objects }`, with `objects` as object references in stacking order. |
| `parent`, `next`, `previous` | The container and the neighbours in its stacking order, as object references; each is left out when there is none, and the drawing header is never given as `parent`. |

Errors: `object not found (provide 'uuid', 'name' or 'index')`; `'includeMembers' must be true or false`; `'memberLimit' must be a number of at least 1 and 'memberOffset' a number of at least 0` (for a wrong type or range of either).

### getObjectAttributes

Returns the graphical attributes of an object.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Return the graphical attributes of an object: pen (foreColor/backColor as RGB and foreColorIndex/backColorIndex in the document color table, line weight in mils/mm, raw style, line type, style kind, opacity, the by-class flags and the line type mapping), fill (colors and color indexes, type, style, fill resource, opacity, by-class flags), fill mapping (origin, axis end points, offsets, axis lengths, angle, repeat/mirror/flip, ...) for hatch/tile/gradient/image fills, the beginning and end markers with beginningVisible/endVisible, the drop shadow, the object opacity with opacityByClass, and the class it inherits from.

The keys are the ones setObjectAttributes accepts, except the read-only pen styleKind and fill type.

> **Note:** A key is left out when Vectorworks gives no value for it. `pen.styleKind` and `fill.type` are whole numbers. `styleKind`: 0 none, 1 solid, 2 pattern, 3 simple line type, 4 complex line type, 5 unknown. `type`: -1 unknown, 1 none, 2 solid, 3 pattern, 4 hatch, 5 tile, 6 gradient, 7 image, 8 class. `pen.lineTypeMapping` and `fillMapping` are given only when the object has such a mapping. `markers` is always given; see [Line end markers](Attributes.md#line-end-markers). `dropShadow` has all its members when the object has drop shadow data of its own and otherwise only `enabled`, and `byClass` is added in both cases; see [Drop shadow](Attributes.md#drop-shadow). The top level has `opacity`, `opacityByClass` and `class` (the name of the class).
>
> The keys match those of [`setObjectAttributes`](#setobjectattributes) with three differences: `colorsByClass` has no `byClass` alias, there is no `allByClass`, and `dropShadow` has no `delete`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |

Errors: `object not found`.

### setObjectAttributes

Sets graphical attributes of an object: pen, fill, opacity, markers, drop shadow and more.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: setObjectAttributes" · **In runToolBatch:** yes

**Details**

Set graphical attributes of an object; only the members you provide are changed. `pen` and `fill` accept foreColor/backColor (RGB) or foreColorIndex/backColorIndex (document color table index), opacity 0-100, none/solid, true for colorsByClass (alias byClass) and styleByClass to use the class values, and opacityByClass true/false. Pen also takes `lineWeightMm` or `lineWeightMils`, `lineType` (internal index of a line type), `style` (raw pen style), lineWeightByClass and `lineTypeMapping` { localMapping, flipHorizontal, flipVertical, scale }; fill also takes `resource` (internal index of a hatch/tile/gradient/image) and `style` (raw fill style).

`fillMapping` positions a hatch/tile/gradient/image fill: origin, iAxisEnd, jAxisEnd (world points), xOffset, yOffset, iAxisLength, jAxisLength (world units), angle (radians), repeat, mirror, flip, maintainAspectRatio, geometryType, localMapping. `markers` sets the beginning/end line markers, their visibility (beginningVisible/endVisible) or byClass.

`dropShadow` is a boolean or an object. Top-level `opacity`, `opacityByClass`, `allByClass` and `class` are also supported.

> **Note:** Only the members given are written, and most types are not checked: a number or boolean of the wrong JSON type is read as 0 or `false`, a `foreColor` or `backColor` that is not a [color](Common.md#colors) is written as black, and a `pen`, `pen.lineTypeMapping`, `fill`, `fillMapping`, `markers` or `class` of the wrong JSON type (or a `dropShadow` that is neither a boolean nor an object) is ignored. Send the types shown in the table.
>
> **Note:** These flags act only as `true`; `false` does nothing: `none`, `solid`, `byClass`, `colorsByClass`, `styleByClass` and `lineWeightByClass` of `pen`; `none`, `solid`, `byClass`, `colorsByClass` and `styleByClass` of `fill`; `markers.byClass`; the top-level `opacityByClass` and `allByClass`. These take `true` and `false`: `pen.opacityByClass`, `fill.opacityByClass`, `markers.beginningVisible`, `markers.endVisible` and the `byClass` of a `dropShadow` object. The other booleans are written as given.
>
> **Note:** A given `foreColorIndex` or `backColorIndex` is applied after the RGB value and always wins (see [Colors](Common.md#colors)). `foreColorIndex` and `backColorIndex` take a whole number from 0 to 65535 (a numeric string of one is also accepted); any other value is not written and sets its `applied` entry to `false`. `class` must be the name of an existing class: no class is created, and `applied.class` is `false` for an unknown name. A top-level `opacity` that is not a JSON number is ignored. A `fillMapping` point that is not a valid point is skipped without an entry in `applied`. A `dropShadow` object without `delete` always writes drop shadow data (the existing data, or a default, with the members given), even when it holds only `byClass`; see [Drop shadow](Attributes.md#drop-shadow).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `pen` | object |  | Pen attributes; only the members given are changed. |
| `pen.foreColor` | [color](Common.md#colors) |  | Foreground color (RGB). |
| `pen.backColor` | [color](Common.md#colors) |  | Background color (RGB). |
| `pen.foreColorIndex` | integer |  | Foreground color as an index into the document color table. |
| `pen.backColorIndex` | integer |  | Background color as an index into the document color table. |
| `pen.lineWeightMm` | number |  | Line weight in millimeters. |
| `pen.lineWeightMils` | integer |  | Line weight in mils. |
| `pen.lineType` | integer |  | Internal index of a line type. |
| `pen.style` | integer |  | Raw pen style. |
| `pen.opacity` | integer |  | Opacity, 0-100. |
| `pen.none` | boolean |  | `true` sets the pen to none (no line). `false` does nothing. |
| `pen.solid` | boolean |  | `true` sets the pen to solid. `false` does nothing. |
| `pen.byClass` | boolean |  | The same as `pen.colorsByClass`. |
| `pen.colorsByClass` | boolean |  | `true` takes the pen colors from the class. `false` does nothing. |
| `pen.styleByClass` | boolean |  | `true` takes the pen style from the class. `false` does nothing. |
| `pen.lineWeightByClass` | boolean |  | `true` takes the line weight from the class. `false` does nothing. |
| `pen.opacityByClass` | boolean |  | `true` takes the pen opacity from the class, `false` stops doing so. |
| `pen.lineTypeMapping` | object |  | How the line type is mapped on the pen; only the members given are changed. |
| `pen.lineTypeMapping.localMapping` | boolean |  | The local mapping flag of the line type mapping. |
| `pen.lineTypeMapping.flipHorizontal` | boolean |  | Flip the line type horizontally. |
| `pen.lineTypeMapping.flipVertical` | boolean |  | Flip the line type vertically. |
| `pen.lineTypeMapping.scale` | number |  | Scale of the line type mapping. |
| `fill` | object |  | Fill attributes; only the members given are changed. |
| `fill.foreColor` | [color](Common.md#colors) |  | Foreground color (RGB). |
| `fill.backColor` | [color](Common.md#colors) |  | Background color (RGB). |
| `fill.foreColorIndex` | integer |  | Foreground color as an index into the document color table. |
| `fill.backColorIndex` | integer |  | Background color as an index into the document color table. |
| `fill.opacity` | integer |  | Opacity, 0-100. |
| `fill.style` | integer |  | Raw fill style. |
| `fill.resource` | integer |  | Internal index of a hatch, tile, gradient or image. |
| `fill.none` | boolean |  | `true` sets the fill to none. `false` does nothing. |
| `fill.solid` | boolean |  | `true` sets the fill to solid. `false` does nothing. |
| `fill.byClass` | boolean |  | The same as `fill.colorsByClass`. |
| `fill.colorsByClass` | boolean |  | `true` takes the fill colors from the class. `false` does nothing. |
| `fill.styleByClass` | boolean |  | `true` takes the fill style from the class. `false` does nothing. |
| `fill.opacityByClass` | boolean |  | `true` takes the fill opacity from the class, `false` stops doing so. |
| `fillMapping` | object |  | How a hatch, tile, gradient or image fill is positioned; only the members given are changed. |
| `fillMapping.origin` | [point](Common.md#points) |  | Origin of the mapping (a world point). |
| `fillMapping.iAxisEnd` | [point](Common.md#points) |  | End point of the I axis (a world point). |
| `fillMapping.jAxisEnd` | [point](Common.md#points) |  | End point of the J axis (a world point). |
| `fillMapping.xOffset` | number |  | Offset in X, in world units. |
| `fillMapping.yOffset` | number |  | Offset in Y, in world units. |
| `fillMapping.iAxisLength` | number |  | Length of the I axis, in world units. |
| `fillMapping.jAxisLength` | number |  | Length of the J axis, in world units. |
| `fillMapping.angle` | number |  | Angle, in radians. |
| `fillMapping.repeat` | boolean |  | Whether the fill repeats. |
| `fillMapping.mirror` | boolean |  | Whether the fill is mirrored. |
| `fillMapping.flip` | boolean |  | Whether the fill is flipped. |
| `fillMapping.maintainAspectRatio` | boolean |  | Whether the fill keeps its aspect ratio. |
| `fillMapping.geometryType` | integer |  | The gradient geometry type (linear, radial, ...), as a whole number. |
| `fillMapping.localMapping` | boolean |  | `true` maps the fill relative to the object (local mapping), `false` relative to the world. |
| `markers` | object |  | The line end markers; only the members given are changed. See [Line end markers](Attributes.md#line-end-markers). |
| `markers.beginning` | [marker](Attributes.md#line-end-markers) |  | The marker at the beginning of the line. Writing it switches `byClass` off for the object. |
| `markers.end` | [marker](Attributes.md#line-end-markers) |  | The marker at the end of the line. Writing it switches `byClass` off for the object. |
| `markers.beginningVisible` | boolean |  | Show (`true`) or hide (`false`) the beginning marker. |
| `markers.endVisible` | boolean |  | Show (`true`) or hide (`false`) the end marker. |
| `markers.byClass` | boolean |  | `true` uses the markers of the class. `false` does nothing. |
| `opacity` | integer |  | Opacity, 0-100. |
| `opacityByClass` | boolean |  | `true` takes the opacity of the object from the class. `false` does nothing. |
| `dropShadow` | [drop shadow](Attributes.md#drop-shadow) |  | A boolean (the drop shadow on or off) or an object with the drop shadow members, `byClass` and `delete`. |
| `allByClass` | boolean |  | `true` sets every attribute that supports it to "by class": pen and fill colors and styles, line weight, opacity, markers and drop shadow. `false` does nothing. |
| `class` | string |  | Name of the class. |

**Result**

`{ applied }`, with one entry for each member that was written. An entry is `true` when Vectorworks took the value and `false` when it refused it. The object itself is not returned. The keys are not always the names of the arguments:

| Argument | Key in `applied` |
|---|---|
| `pen.foreColor`, `pen.backColor` | `penForeColor`, `penBackColor` |
| `pen.foreColorIndex`, `pen.backColorIndex` | `penForeColorIndex`, `penBackColorIndex` |
| `pen.lineWeightMm`, `pen.lineWeightMils` | `lineWeightMm`, `lineWeightMils` |
| `pen.opacity` | `penOpacity` |
| `pen.style`, `pen.lineType` | `penStyle`, `penLineType` |
| `pen.none`, `pen.solid` | `penNone`, `penSolid` |
| `pen.byClass` or `pen.colorsByClass` | `penByClass` |
| `pen.styleByClass`, `pen.lineWeightByClass`, `pen.opacityByClass` | `penStyleByClass`, `lineWeightByClass`, `penOpacityByClass` |
| `pen.lineTypeMapping.localMapping`, `flipHorizontal`, `flipVertical`, `scale` | `penLocalMapping`, `penFlipHorizontal`, `penFlipVertical`, `penScale` |
| `fill.foreColor`, `fill.backColor` | `fillForeColor`, `fillBackColor` |
| `fill.foreColorIndex`, `fill.backColorIndex` | `fillForeColorIndex`, `fillBackColorIndex` |
| `fill.opacity`, `fill.style`, `fill.resource` | `fillOpacity`, `fillStyle`, `fillResource` |
| `fill.none`, `fill.solid` | `fillNone`, `fillSolid` |
| `fill.byClass` or `fill.colorsByClass` | `fillByClass` |
| `fill.styleByClass`, `fill.opacityByClass` | `fillStyleByClass`, `fillOpacityByClass` |
| `fillMapping.origin`, `iAxisEnd`, `jAxisEnd` | `mapOrigin`, `mapIAxisEnd`, `mapJAxisEnd` |
| `fillMapping.xOffset`, `yOffset`, `iAxisLength`, `jAxisLength`, `angle` | `mapXOffset`, `mapYOffset`, `mapIAxisLength`, `mapJAxisLength`, `mapAngle` |
| `fillMapping.repeat`, `mirror`, `flip`, `maintainAspectRatio`, `geometryType`, `localMapping` | `mapRepeat`, `mapMirror`, `mapFlip`, `mapAspect`, `mapGeometryType`, `mapLocalMapping` |
| `markers.beginning`, `markers.end` | `beginningMarker`, `endMarker` |
| `markers.beginningVisible`, `markers.endVisible` | `beginningMarkerVisible`, `endMarkerVisible` |
| `markers.byClass` | `markersByClass` |
| `opacity`, `opacityByClass` | `opacity`, `opacityByClass` |
| `dropShadow` (a boolean, or an object with the members) | `dropShadow` |
| `dropShadow.byClass`, `dropShadow.delete` | `dropShadowByClass`, `dropShadowDeleted` |
| `class`, `allByClass` | `class`, `allByClass` |

A flag that acts only as `true` has an entry only when `true` is given.

Errors: `object not found`. It is the only error text: a value that Vectorworks refuses is `false` in `applied`, and the call still succeeds and keeps the other changes.

### copyAttributes

Copies the graphical attributes of one object onto other objects.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: copyAttributes" · **In runToolBatch:** yes

**Details**

Copy every graphical attribute of the source object (pen, fill, markers, drop shadow, opacity) onto one `targetUuid` or many `targetUuids`. Set `includeClass` to also put the targets into the class of the source.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `targetUuid` | string |  | UUID of the object to copy the attributes onto. |
| `targetUuids` | array of string |  | UUIDs of several objects to copy the attributes onto. They are added to `targetUuid` when both are given. |
| `includeClass` | boolean |  | `true` also puts each target into the class of the source object. |

**Result**

`{ results }`, with one entry for each target, in the order given (`targetUuid` first):

| Key | Description |
|---|---|
| `uuid` | The UUID of the target, as given. |
| `applied` | `true` when the attributes were copied, `false` when Vectorworks refused. Here it is one boolean, not an object. |
| `class` | Only with `includeClass`: `true` when the class was set. |
| `err` | `object not found`, when no object has that UUID. The entry then has no `applied`. |

Entries of `targetUuids` that are not text are skipped, so an empty list gives an empty `results`.

Errors: `source object not found (provide 'uuid', 'name' or 'index')` and `provide 'targetUuid' or 'targetUuids'` (neither key was given). A target that is not found is reported only in its own entry: the call still succeeds, the other targets keep their changes and nothing is rolled back.

### editObject

Moves, rotates, scales, mirrors, duplicates, regroups, converts, resets or deletes an object, or changes its name and class.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: editObject" · **In runToolBatch:** yes

**Details**

Transform or update one object. `action`: move (`offset`), rotate (`angle` radians, `center`), scale (`scaleX`,`scaleY`,`center`), mirror (`axisStart`,`axisEnd`), duplicate (`offset`), moveToContainer (into the group or symbol definition `containerUuid` or onto the layer `layer`), addToGroup (into the group `groupUuid`), ungroup (a group), convertToPolygon / convertToPolyline (optional `keepOriginal`, `resolution`; returns the new object), reset (regenerate a plug-in object) or delete.

Without an action it just applies any of `name`, `class`, `visible`, `locked`, `selected`. moveToContainer only moves objects between layers, groups and symbol definitions: the target must be a layer, a symbol definition or a group in one of them, and so must the container the object is in. It refuses a layer as the object, a target inside the object itself, and objects in or into a wall, a plug-in object or a roof: moving a door or a window into a wall, or out of the wall it is inserted in, would corrupt the wall and is not supported (insert doors and windows into walls in Vectorworks).

Into a symbol definition, or a group in one, it refuses an object that is or holds (at any depth) an instance of that symbol, or of a symbol that holds an instance of it at any depth: a symbol nested inside itself creates an infinite loop. It cannot be combined with a new `name` (the object's own name, which identifies it, is fine), `class`, `visible`, `locked` or `selected` (change them in another call); a refused or failed move changes nothing.

It updates the bounds of the groups that the object leaves and enters, and of the groups around them, and Edit &gt; Undo of a move puts the object back where it was and the bounds of those groups as they were. addToGroup is moveToContainer into the group `groupUuid`, with the same checks, refusals and undo; a `groupUuid` that is no group (a layer, a symbol definition, ...) is refused: use moveToContainer for those. ungroup is Vectorworks' Ungroup of one group: it moves the members into the container of the group where the group was in the stacking order, in their order, deletes the group and returns the former members as object references in stacking order (`members`) with their container (`parent`).

The members end up selected (other selected objects stay selected). Records attached to the group itself are not guaranteed to pass to the members. It refuses an object that is no group, a locked group (unlock it first), a group inside a wall, a plug-in object or a roof, the group being edited (or one that holds it), and a new name, class, visible, locked or selected; members hidden at the current level of detail (possible in symbol definitions) are deleted with the group, as Ungroup does, and counted in `deletedMemberCount`.

Edit &gt; Undo of an ungroup brings the group back with its members.

> **Note:** `name` has two uses. It finds the object when no `uuid` is given (the order is `uuid`, `name`, `index`; see [Object references](Common.md#object-references)), and it is the new name of the object. An object found by its `name` is therefore "renamed" to the name it already has. To rename an object, find it by `uuid` and give the new `name`. With `index` instead, an object that already has the new name is found first, because `name` is tried before `index`.
>
> **Note:** Defaults when a member is missing: `offset` is (0, 0), `center` is the world origin (0, 0), `angle` is 0, and `scaleX` and `scaleY` are 1. For `mirror`, `axisStart` and `axisEnd` must be two different points. Points are in world units. `duplicate` moves the copy only when `offset` is given.
>
> **Note:** An `action` that is not in the list does nothing and is not reported: the call succeeds, and only the members `name`, `class`, `visible`, `locked` and `selected` that were given are applied. For `duplicate`, `convertToPolygon` and `convertToPolyline` these five members are ignored. `convertToPolyline` ignores `resolution`.
>
> **Note:** `class` must be the name of an existing class: no class is created, and `applied.class` is `false` for an unknown name. With `useClassAttributes` set to `true` the object also takes the attributes of the class, as `allByClass` does in [`setObjectAttributes`](#setobjectattributes).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `action` | string |  | One of: `move`, `rotate`, `scale`, `mirror`, `duplicate`, `moveToContainer`, `addToGroup`, `ungroup`, `convertToPolygon`, `convertToPolyline`, `reset`, `delete`. |
| `offset` | [point](Common.md#points) |  | Shift for `move` and `duplicate`, in world units. Default (0, 0). |
| `angle` | number |  | Angle in radians, counter-clockwise. |
| `center` | [point](Common.md#points) |  | Center point of the rotation or scale, for `rotate` and `scale`. Default: the world origin (0, 0). |
| `scaleX` | number |  | Scale factor in X, for `scale`. Default 1. |
| `scaleY` | number |  | Scale factor in Y, for `scale`. Default 1. |
| `axisStart` | [point](Common.md#points) |  | First point of the mirror axis, for `mirror`. |
| `axisEnd` | [point](Common.md#points) |  | Second point of the mirror axis, for `mirror`. It must differ from `axisStart`. |
| `containerUuid` | string |  | UUID of the group or symbol definition to move the object into, for `moveToContainer`. It wins over `layer`. |
| `layer` | string |  | Name of the layer to move the object onto, for `moveToContainer`. |
| `groupUuid` | string |  | UUID of the group to add the object to, for `addToGroup`. |
| `keepOriginal` | boolean |  | For `convertToPolygon` and `convertToPolyline`: `true` keeps the original object. Default `false`. |
| `resolution` | integer |  | For `convertToPolygon`: the resolution of the conversion, a whole number (0 when not given). Not used by `convertToPolyline`. |
| `class` | string |  | Name of an existing class to put the object into. See the Note above. |
| `useClassAttributes` | boolean |  | With `class`: `true` also sets the attributes of the object to follow the class. |
| `visible` | boolean |  | Show (`true`) or hide (`false`) the object. |
| `locked` | boolean |  | Lock (`true`) or unlock (`false`) the object. |
| `selected` | boolean |  | Select (`true`) or deselect (`false`) the object. |

**Result**

The result depends on the action:

| Action | Result |
|---|---|
| `delete` | `{ deleted }`: `true` when the object was deleted. |
| `duplicate`, `convertToPolygon`, `convertToPolyline` | The [object reference](Common.md#object-references) of the new object. |
| `moveToContainer`, `addToGroup` | The object reference of the moved object, with `applied` set to `{ "moveToContainer": true }` or `{ "addToGroup": true }`. |
| `ungroup` | `{ ungrouped, parent, members, deletedMemberCount }`: `ungrouped` is `true`, `parent` is the container that now holds the members, `members` are the former members as object references in stacking order, and `deletedMemberCount` is given only when hidden members were deleted with the group. |
| `move`, `rotate`, `scale`, `mirror`, `reset`, no action, or an unknown action | The object reference of the object, with `applied`. It has an entry for the action (`move`, `rotate`, `scale`, `mirror` or `reset`) and an entry for each of `name`, `visible`, `locked`, `selected` and `class` that was given. An entry is `true` when Vectorworks took the value and `false` when it refused it. |

Errors: `object not found`, `failed to duplicate`, `failed to convert to a polygon`, `failed to convert to a polyline`, `container not found (provide 'containerUuid' or 'layer')`, `group not found (provide 'groupUuid')`, `Vectorworks could not move the object into the container`, and for a `groupUuid` that is no group `addToGroup adds objects to a group only, and 'groupUuid' is no group: move objects into a layer or a symbol definition with editObject 'moveToContainer' ('containerUuid' or 'layer')`. A refused `moveToContainer`, `addToGroup` or `ungroup` returns an `err` that says why. An `err` rolls the call back (`rolledBack`), so nothing is changed.

### getObjectParameters

Reads the parameters of a plug-in object.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the parameter record of a parametric plug-in object (PIO) ONLY - e.g. doors, windows, plants, hardscapes, data tags; check that findObjects/getObjectInfo reports a `parametricName` first. Returns the parametric name, the list of parameter names, and their values as strings. Optionally restrict to specific `names`. Optional `includeDefinitions` (default false) adds `definitions`: for each parameter read, by name, its `type` (integer, boolean, real, text, dimension, popUp, angle, coordLocX, ...), `localizedName` and, for a popUp, the universal `choices` it accepts; `parameters` and `values` are unchanged.

Optional `curated` (default false) adds a `curated` array of { param, label, value, display } for door and window opening parameters: label is the localized parameter name, display the localized popup choice for the opening popups (null otherwise or when not available); the `values` output is unchanged. Other plug-in objects return an empty `curated` array.

It returns an error for every other object (lines, rectangles, arcs, polygons, groups, symbols, walls, ...) and never reads user data records (record formats attached to objects) - use getObjectRecords for those.

> **Note:** With `names` the result has no `parameters` list, and a name that the object does not have is left out of `values` and `definitions` without an error. Entries of `names` that are not text are skipped. `curated` ignores `names`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `names` | array of string |  | Names of the parameters to read. Default: all parameters. See the Note above. |
| `includeDefinitions` | boolean |  | Default: `false`. Adds `definitions` to the result. |
| `curated` | boolean |  | Default: `false`. Adds `curated` to the result. |

**Result**

| Key | Description |
|---|---|
| `parametricName` | The universal name of the plug-in object. |
| `parameters` | The names of all parameters, in declaration order. Left out when `names` is given. |
| `values` | The values as text: `{ "<parameter>": "<value>" }`. |
| `definitions` | Only with `includeDefinitions`: `{ "<parameter>": { localizedName, type, choices } }` for each parameter that was read. `type` is the type name from the Details. `choices` (the universal choices) is given for a `popUp` only. |
| `curated` | Only with `curated`: an array of `{ param, label, value, display }`. It is empty for a plug-in object that is not a door or window. |

Errors: `object not found`, `object is not a parametric plug-in object (no parameter record)`.

### getObjectRecords

Reads the data records attached to an object.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the user data records attached to any object (plug-in or not): for each attached non-internal record format, its name, localized name and the field values as strings. Optionally restrict to specific record format names with `records` (universal or localized name, case-insensitive). Internal IFC records are omitted: read an object's IFC data (entity, standard and custom property sets, IFC property types) with getObjectIFCData, and property-set definitions with listIFCPsets and getIFCPsetDefinition.

The parameter record of a plug-in object is not included - use getObjectParameters for it. To find objects by a record value use findObjects with criteria such as "`('MyRecord'.'MyField' > 1)`"; the field definitions of a record format are read with getResourceDetails.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `records` | array of string |  | Universal or localized name, case-insensitive. |

**Result**

`{ object, records }`: `object` is the [object reference](Common.md#object-references) and `records` is an array with one entry for each record that was read:

| Key | Description |
|---|---|
| `name` | The universal name of the record format. |
| `localizedName` | The localized name. Left out when the format has none. |
| `values` | The field values as text: `{ "<field>": "<value>" }`. |

Names in `records` that no attached record has are ignored. An object without records gives an empty `records`.

Errors: `object not found`.

### setObjectParameter

Writes one or more parameters of a plug-in object.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: setObjectParameter" · **In runToolBatch:** yes

**Details**

Write parameter(s) of a parametric plug-in object. Either set one `name`/`value` (type taken from the parameter definition, or forced via `type`), or pass a `params` object of name/value pairs. Numeric parameters also accept numeric strings (e.g. "5", "5.0"); a value that cannot be converted to the parameter type is not written and reports false (`ok`, or its entry in `applied`). The object is regenerated afterwards.

> **Note:** `name` has two uses. In the single-parameter form it is the name of the parameter to write, and as in every object tool it also finds the object: `uuid` first, then `name`, then `index`, each used when the one before finds nothing. Give the object by `uuid` (preferred) so that a parameter name is never taken for an object name. With `params`, `name` only finds the object.
>
> **Note:** `params` wins when it is an object: `name`, `value` and `type` are then not used for a parameter. The `name` form fails with `parameter not found: <name>` when the object has no such parameter. In `params` an unknown name is not an error: its entry in `applied` is `false`. A `false` is no failure of the call: the other values are written, the object is regenerated, and the call is not rolled back. A value is converted by the type of its parameter, see [Plug-in parameters](Common.md#plug-in-parameters).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | In the single-parameter form: the name of the parameter to write, as `getObjectParameters` reports it. It also finds the object, see the Note above. |
| `index` | integer |  | Reference by internal index. |
| `value` | string or number or integer or boolean |  | The value for `name`. Its type is taken from the parameter definition, or forced via `type`. Without a value nothing is written and `ok` is `false`. |
| `type` | string |  | One of: `string`, `real`, `int`, `bool`. `number`, `integer` and `boolean` are also accepted, and any other text writes the value as text. Used only with `name`. |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. See [Plug-in parameters](Common.md#plug-in-parameters). It wins over `name` and `value`; a `params` that is not an object is ignored. |

**Result**

| Form | Result |
|---|---|
| `params` | `{ applied }`: `{ "<parameter>": true or false }` for each name in `params`. |
| `name` and `value` | `{ ok }`: `true` when the value was written. |

Errors: `object not found`, `object is not a parametric plug-in object`, `'name' (parameter name) is required, or provide a 'params' object` and, in the `name` form, `parameter not found: <name>`.

### getPluginDefinition

Describes an installed plug-in object: its kind, parameters and pop-up choices.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Describe an installed plug-in object (PIO) without an instance, by its exact universal name `universalName` (case-sensitive: the `parametricName` that findObjects and getObjectInfo report, e.g. "Drawing Label2" or "Revision Cloud"). Returns `universalName`, `localizedName`, `kind` - how createPluginObject places it: point, linear, rectangle and custom take a `position`, path2D and path3D a `pathUuid` -, `dedicatedTool` { tool, group } when a group has a create tool of its own for it (createPluginObject refuses it, use that tool), and `parameters` in declaration order: [{ name (the universal name that createPluginObject `params` and setObjectParameter take), localizedName, type (integer, boolean, real, text, dimension, popUp, angle, coordLocX, ...), defaultValue (as text), choices (the universal choices of a popUp parameter) }].

Returns an error for an unknown or differently cased name, a plug-in that is not installed, and a menu command or tool. It changes nothing: when the plug-in's parameter record format is missing from the document, it defines the format only to read it, inside a private undo event that it takes back, so neither the format nor an undo step remains.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `universalName` | string | Yes | The exact universal name of the plug-in object, case-sensitive: the `parametricName` that `findObjects` and `getObjectInfo` report. |

**Result**

| Key | Description |
|---|---|
| `universalName` | The universal name. |
| `localizedName` | The localized name. Left out when there is none. |
| `kind` | How `createPluginObject` places the plug-in object, as named in the Details. |
| `dedicatedTool` | `{ tool, group }`. Only when a group has a create tool of its own for this plug-in object. |
| `parameters` | The parameters in declaration order: `{ name, localizedName, type, defaultValue, choices }`. `defaultValue` is text. `choices` (the universal choices) is given for a `popUp` only. |

Errors: `'universalName' is required: the universal name of a plug-in object, e.g. the 'parametricName' that findObjects and getObjectInfo report for an existing one` and `no plug-in object '<universalName>' is installed: …`, which also covers a menu command or a tool. When the name is that of a plug-in object with a create tool of its own, in another letter case or not installed here, the error also gives its exact universal name and the tool to use.

### createPluginObject

Creates a plug-in object that has no dedicated create tool.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createPluginObject" · **In runToolBatch:** yes

**Details**

Create a plug-in object (PIO) by its exact universal name `universalName` (case-sensitive; getPluginDefinition reports its kind and parameters). Only for plug-ins without a create tool of their own: doors, windows, slabs, columns, stairs, plants, hardscapes, landscape areas, site modifiers, property lines, site models, stakes, existing trees, lighting devices, ConnectCAD devices and sockets, data tags and title block borders are refused, and the error names the tool to use (getPluginDefinition `dedicatedTool`).

The kind decides the placement: a point, linear, rectangle or custom plug-in object is created at `position` (a world point), turned by the optional `angle` (radians). A path2D or path3D one takes `pathUuid` and no `position` or `angle`: an existing object that is a direct member of the active layer (or of the group being edited on a layer), which the new object takes over as its path, as the plug-in tools do with a shape they pick - the object itself, not a copy: it leaves the layer, and Vectorworks converts a 2D shape into a polyline.

A path in a symbol definition being edited, or in a group in one, is refused: Vectorworks records the change of a path only when it is in a layer, so Undo would delete the path with the new object; create the object from a path on a layer and move it into the symbol definition with editObject `moveToContainer`. A path2D plug-in object takes a rectangle, rounded rectangle, oval, arc, polygon, freehand polygon or polyline; a path3D one also a 3D polygon, NURBS curve or NURBS surface.

Edit &gt; Undo removes the new object and brings the path back. Optional `params` { "ParamName": value } set parameters by universal name as setObjectParameter `params` does, and the object is regenerated after them; `applied` reports each one. The creation options class, useClassAttributes, name and select apply. Everything is checked before anything changes: an unknown or differently cased name, a missing or extra `pathUuid` or `position`, a path object outside the active container, in a symbol definition or of another shape, an unknown parameter name or a value that does not fit its parameter refuses the call, which then creates nothing.

A plug-in that does not allow the object there, or a parameter that the new object does not take, fails the call, which is rolled back. Returns the reference of the new object with `kind` and, for a path plug-in object, its `pathObject`. Like using the plug-in, it adds the plug-in's parameter record format to the document when it is missing (a refused or failed call is rolled back with it).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `universalName` | string | Yes | Case-sensitive; getPluginDefinition reports its kind and parameters. |
| `position` | [point](Common.md#points) |  | A world point `{ x, y }`. Required for a point, linear, rectangle or custom plug-in object; not allowed for a path one. |
| `angle` | number |  | Angle in radians, counter-clockwise. Default 0. Not allowed for a path plug-in object. |
| `pathUuid` | string |  | UUID of the object that supplies the path. Required for a `path2D` or `path3D` plug-in object; not allowed for the other kinds. |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`, by universal name. See [Plug-in parameters](Common.md#plug-in-parameters). Every name and value is checked before anything is created. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The [object reference](Common.md#object-references) of the new object, with these keys added:

| Key | Description |
|---|---|
| `kind` | The kind of the plug-in object: `point`, `linear`, `rectangle`, `custom`, `path2D` or `path3D`. |
| `applied` | Only when `params` was given and is not empty: `{ "<parameter>": true }` for each parameter. A parameter that is not written fails the call, so every entry is `true`. |
| `pathObject` | Only for a `path2D` or `path3D` plug-in object: the object reference of its path object, the object that `pathUuid` named. |

Errors that refuse the call before anything is created:

- `'universalName' is required: …` and `no plug-in object '<universalName>' is installed: …`, as in `getPluginDefinition`.
- `'<universalName>' has a create tool of its own, which knows the object and keeps it consistent: use <tool> of the <group> …`.
- For a `path2D` or `path3D` plug-in object: `'<universalName>' is a plug-in object of kind '<kind>': give 'pathUuid', the uuid of the object of the active layer that becomes its path …`, and `…, which its path places: give 'pathUuid' without 'position' or 'angle'`.
- For the other kinds: `'<universalName>' is a plug-in object of kind '<kind>': give 'position', a point { x, y } in world units`, `…, which is placed at 'position' (turned by 'angle'): it takes no 'pathUuid'`, and `'angle' must be a number (radians)`.
- A path that does not fit: `path object not found ('pathUuid' is the uuid of an object of the active layer)`, `the path object is not a direct member of the active layer (or of the group being edited) …`, `the path object is not in a layer …`, and `the path object is <type>, which a plug-in object of kind '<kind>' does not take as its path: give …`.
- `'params' must be an object of universal parameter names and values: { "ParamName": value }`, `the plug-in object '<universalName>' has no parameter <names>: 'params' takes universal parameter names (getPluginDefinition lists them)`, and `these 'params' values do not fit the type of their parameter: <names> (real and integer parameters take a number or a numeric string, boolean ones true or false, the others text)`.

Errors after the checks passed. Both roll the call back (`rolledBack`), so nothing is left:

- `Vectorworks did not create the plug-in object '<universalName>', for example because the active layer, group or symbol definition does not allow this plug-in object`.
- `the new plug-in object '<universalName>' did not take the parameter(s) <names>, for example a parameter that its plug-in style sets`. This `err` also has `applied`, with `false` for each parameter that was not taken.
