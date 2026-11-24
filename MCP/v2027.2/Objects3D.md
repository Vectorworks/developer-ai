**English** • [Deutsch](../../MCP.de/v2027.2/Objects3D.md) • [日本語](../../MCP.ja/v2027.2/Objects3D.md)

# Objects3D — 3D modeling

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools to create, read and edit 3D geometry: solids, 3D polygons, meshes, NURBS curves and surfaces, and surface models.

## Table of contents

- [Overview](#overview)
- [3D Modeling](#3d-modeling)
  - [createExtrude](#createextrude)
  - [createSolidPrimitive](#createsolidprimitive)
  - [createSweep](#createsweep)
  - [combineSolids](#combinesolids)
  - [createShell](#createshell)
  - [convertSolid](#convertsolid)
  - [getSolid](#getsolid)
  - [editSolid](#editsolid)
  - [create3DPolygon](#create3dpolygon)
  - [createMesh](#createmesh)
  - [createNurbsCurve](#createnurbscurve)
  - [createNurbsSurface](#createnurbssurface)
  - [createSurfaceModel](#createsurfacemodel)
  - [get3DGeometry](#get3dgeometry)
  - [edit3DGeometry](#edit3dgeometry)
  - [convertTo3D](#convertto3d)

## Overview

This folder holds 1 tool group with 16 tools in total.

| Group | Group ID | Active by default | Risk level | Tools | Summary |
|---|---|---|---|---|---|
| [3D Modeling](#3d-modeling) | `3d-modeling` | No | medium | 16 | Create, read and edit solids, 3D polygons, meshes, NURBS curves and surfaces, and surface models. |

## 3D Modeling

> **Group:** `3D Modeling` · **Group ID:** `3d-modeling` · **Active by default:** No · **Risk level:** medium · **Tools:** 16

**Create, read and edit solids, 3D polygons, meshes, NURBS curves and surfaces, and surface models.**

Create, read and edit 3D solids: extrudes (from points, a rectangle, a 2D shape or coplanar 3D points, or between two 3D points; with holes and a placement in 3D), multiple extrudes and tapered extrudes (createExtrude); spheres, ellipsoids, hemispheres, cones, boxes, cylinders and tori (createSolidPrimitive); sweeps, profiles revolved about an axis (createSweep); combine solids into a Generic Solid (combineSolids), create shells (createShell), and convert solids to Generic Solids or meshes (convertSolid); read the kind, 3D box, parameters and Generic Solid history (getSolid), and move, rotate, scale, re-orient and resize extrudes, multiple extrudes, sweeps, spheres, hemispheres and cones (editSolid). 3D polygons and meshes: create 3D polygons from 3D points, from 2D points or a rectangle at a Z (create3DPolygon) and meshes from vertices and faces, from polygons or from a group of 3D polygons (createMesh); read their vertices, faces, plane, area, volume, smoothing and parts, each list in pages (`limit`, `offset`, `countOnly`) (get3DGeometry); edit their vertices, faces, closure, smoothing and parts, simplify, segment, move, rotate and scale them, and make planar solids of 3D polygons and repaired copies of meshes (edit3DGeometry); convert any 2D or 3D object to a group of 3D polygons, a mesh or a Generic Solid (convertTo3D).

**NURBS curves and surfaces:** create curves from control points (with weights) or fit points of a degree (createNurbsCurve) and surfaces from a control net points[u][v] with degrees and weights (createNurbsSurface); read their pieces, points, weights and knots, and measure curves: points at distances, closest points, points with tangent and curvature at parameters, division into equal parts (get3DGeometry); set their points and weights, trim a surface by a curve and make extended and offset copies of both (edit3DGeometry; NURBS take no move3D, rotate3D, scale3D or knot edits). Surface models of NURBS surfaces: lofts through sections, rail sweeps of sections along one or two rails, revolves of a profile (about its left edge, or along a rail about an axis) and extrudes of a profile along a path; the result is a NURBS surface, a Generic Solid or a group of them (createSurfaceModel). Lengths are world units and angles are radians. All 3D coordinates, given and returned (points, centers, frames, baseElevation and bounds3D), are absolute world Z: the tools add no design layer elevation to them, so an object given at z 0 lies at world Z 0, not on the plane of an elevated layer. To put an object on the plane of a layer at elevation E, add E to its Z values; layerElevation reports E for the owning design layer (null without a design-layer owner). New objects usually go on the active layer; shells and conversions can retain the source's container. The optional `select` creation option controls whether a result is selected. Input shapes are never changed: the tools copy them (delete them afterwards with editObject action delete if they are no longer wanted). Every change runs as its own named, undoable Vectorworks operation; a refused call changes nothing.

> **Note:** `combineSolids`, `createShell`, `convertSolid` and `convertTo3D` set the selection of the result to `select`, like the other create tools: the result is selected only when `select` is true, even when its source is selected.

> **Note:** `createShell` and `convertSolid` (both `genericSolid` and `mesh`) always place the result right after the source, in the source's container (a layer, a symbol definition or a group). `combineSolids` places its result in the active layer, or in the group or symbol definition being edited, not next to its operands.

| Tool | Effect | Risk | Summary |
|---|---|---|---|
| [`createExtrude`](#createextrude) | Edit | medium | Creates an extrude, a multiple extrude or a tapered extrude. |
| [`createSolidPrimitive`](#createsolidprimitive) | Edit | medium | Creates a sphere, ellipsoid, hemisphere, cone, box, cylinder or torus. |
| [`createSweep`](#createsweep) | Edit | medium | Creates a sweep: 2D profiles revolved about an axis. |
| [`combineSolids`](#combinesolids) | Edit | medium | Combines two solids into a Generic Solid by union, intersection or difference. |
| [`createShell`](#createshell) | Edit | medium | Creates a shell by thickening a NURBS surface or hollowing a solid. |
| [`convertSolid`](#convertsolid) | Edit | medium | Creates a copy of a solid converted to a Generic Solid or a mesh. |
| [`getSolid`](#getsolid) | Read-only | low | Reads a solid: its kind, 3D bounds, parameters and Generic Solid history. |
| [`editSolid`](#editsolid) | Edit | medium | Moves, rotates, scales, re-orients or resizes a solid. |
| [`create3DPolygon`](#create3dpolygon) | Edit | medium | Creates a 3D polygon from 3D points, from 2D points at a height, or from a rectangle. |
| [`createMesh`](#createmesh) | Edit | medium | Creates a mesh from vertices and faces, from polygons or from a group of 3D polygons. |
| [`createNurbsCurve`](#createnurbscurve) | Edit | medium | Creates a NURBS curve from control points or fit points. |
| [`createNurbsSurface`](#createnurbssurface) | Edit | medium | Creates a NURBS surface from its control net. |
| [`createSurfaceModel`](#createsurfacemodel) | Edit | medium | Creates a loft, rail sweep, revolve or extrude-along-path surface model from existing objects. |
| [`get3DGeometry`](#get3dgeometry) | Read-only | low | Reads a 3D polygon, mesh, NURBS curve or NURBS surface. |
| [`edit3DGeometry`](#edit3dgeometry) | Edit | medium | Edits a 3D polygon, mesh, NURBS curve or NURBS surface. |
| [`convertTo3D`](#convertto3d) | Edit | medium | Converts a copy of an object to 3D polygons, a mesh or a Generic Solid. |

### createExtrude

Creates an extrude, a multiple extrude or a tapered extrude.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createExtrude" · **In runToolBatch:** yes

**Details**

Create an extrude from exactly one profile source: `points` (3 or more points { x, y }: a closed profile in the XY plane), `rect` { left, top, right, bottom } (the form getObjectInfo `bounds` reports), `profileUuid` (a 2D shape: line, rectangle, rounded rectangle, oval, arc, polygon, freehand polygon or polyline), `points3D` (3 or more coplanar 3D points { x, y, z } in world Z: the profile lies in their plane and is extruded along its normal) or `profileUuids` (2 or more 2D shapes in section order: a multiple extrude, its sections spread evenly from `baseElevation` to `baseElevation` + `thickness`).

`thickness` is required (not 0; a negative thickness extrudes the other way); `baseElevation` (default 0, world Z) applies to points, rect, profileUuid and profileUuids. `between` { start, end, up? } (3D points) with `profileUuid` or `points` extrudes the profile from start to end instead, its origin at start (the thickness is their distance; the profile's +Y follows `up`, by default world Z, or world Y for a vertical extrusion; `up` must not be parallel to end - start) and takes no thickness or baseElevation.

`taper` { angle, height } with `profileUuid` makes a tapered extrude whose sides slope by `angle` (radians, |angle| &lt; pi/2) over `height` (not 0): a NURBS surface, a CSG solid or a group of them (kind surfaceModel), without thickness or baseElevation. Single extrudes take `holes`: an array of { points } (3 or more points) or { uuid } (a closed 2D shape), in the coordinates of the profile; a hole that cannot be added refuses the call.

`transform` { origin, uAxis, vAxis, wAxis? } places a single extrude of points, rect or profileUuid in 3D: origin is in world Z; its local axes are orthonormal unit vectors (wAxis defaults to uAxis x vAxis). Shapes given by UUID are copied and stay unchanged. Every argument is checked before anything is created. Returns the object reference, `kind` (extrude, multipleExtrude or surfaceModel), `bounds3D` { min, max } in world Z, and `layerElevation` in world units; getSolid reads the extrude.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `points` | array of [point](Common.md#points) |  | 3 or more points { x, y }: a closed profile in the XY plane. |
| `rect` | [rectangle](Common.md#rectangles) |  |  |
| `profileUuid` | string |  | A 2D shape: line, rectangle, rounded rectangle, oval, arc, polygon, freehand polygon or polyline. |
| `points3D` | array of [3D point](Common.md#points) |  | Each item: A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `profileUuids` | array of string |  |  |
| `baseElevation` | number |  | World Z of the base (default 0). Applies to `points`, `rect`, `profileUuid` and `profileUuids`. |
| `thickness` | number |  | Thickness, in world units. |
| `between` | object |  |  |
| `between.start` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `between.end` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `between.up` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `taper` | object |  |  |
| `taper.angle` | number | Yes |  |
| `taper.height` | number | Yes |  |
| `holes` | array of object |  |  |
| `holes[].points` | array of [point](Common.md#points) |  |  |
| `holes[].uuid` | string |  |  |
| `transform` | object |  | 3D placement { origin, uAxis, vAxis, wAxis? } of a single extrude of `points`, `rect` or `profileUuid`; refused with `between`, `points3D`, `profileUuids` or `taper`. |
| `transform.origin` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `transform.uAxis` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `transform.vAxis` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `transform.wAxis` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createSolidPrimitive

Creates a sphere, ellipsoid, hemisphere, cone, box, cylinder or torus.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createSolidPrimitive" · **In runToolBatch:** yes

**Details**

Create a solid primitive of `kind`: sphere (`center` with `radius`, or with `radii` { x, y, z } for an ellipsoid with radii along the world axes), hemisphere (`center` with `radius` for a dome along +Z, or with `topPoint`, the top of the dome), cone (`baseCenter` and `radius` with `height` for a right cone along +Z, a negative height pointing it along -Z, or with `tipPoint`), box (`minimum` and `maximum`, the opposite corners: an extrude), cylinder (`baseCenter`, `radius` and `height` (not 0) along Z: an extrude of a circle) or torus (`center`, `majorRadius` &gt; `minorRadius` &gt; 0, about the world Z axis: a sweep).

Points are in world Z. Radii must be positive. Every argument is checked before anything is created. Returns the object reference, `kind` as getSolid reports it (sphere, hemisphere, cone; extrude for a box or a cylinder; sweep for a torus), `bounds3D` { min, max } in world Z and `layerElevation` in world units.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `kind` | string | Yes | One of: `sphere`, `hemisphere`, `cone`, `box`, `cylinder`, `torus`. |
| `center` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `radius` | number |  | Radius, in world units. |
| `radii` | [3D point](Common.md#points) |  | Sphere only, instead of `radius` (an ellipsoid): the positive semi-axis lengths { x, y, z } in world units along the world X, Y and Z axes. Not a point: add no layer elevation to `z`. |
| `topPoint` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `baseCenter` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `height` | number |  | Height, in world units. |
| `tipPoint` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `minimum` | [3D point](Common.md#points) |  | For `box`: the lower corner; each coordinate of `maximum` must be greater than that of `minimum`. A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `maximum` | [3D point](Common.md#points) |  | For `box`: the upper corner; each coordinate must be greater than that of `minimum`. A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `majorRadius` | number |  |  |
| `minorRadius` | number |  |  |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createSweep

Creates a sweep: 2D profiles revolved about an axis.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createSweep" · **In runToolBatch:** yes

**Details**

Create a sweep, a solid or surface of revolution, from copies of the 2D shapes `profileUuids` (1 or more: lines, rectangles, rounded rectangles, ovals, arcs, polygons, freehand polygons or polylines). The profile's X is the radius and its Y lies along the axis: the axis is parallel to Y, through the 2D locus `axisUuid` (copied), or along the left edge of the profiles without it; the new sweep revolves about a line parallel to world Y.

`startAngle` (default 0), `sweepAngle` (default 2\*pi, a full turn; negative turns the other way), `incrementAngle` (default pi/36, positive: the angle of each segment) and `pitch` (default 0: the rise along the axis per full turn, in world units, for a helix). The profiles and the axis locus are 2D shapes, read in X and Y; bounds3D reports where the sweep lies in world Z. Every argument is checked before anything is created.

Returns the object reference, `kind` sweep, `bounds3D` { min, max } in world Z and `layerElevation` in world units; editSolid changes the angles and the pitch.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `profileUuids` | array of string | Yes | 1 or more: lines, rectangles, rounded rectangles, ovals, arcs, polygons, freehand polygons or polylines. |
| `axisUuid` | string |  |  |
| `startAngle` | number |  | Start angle in radians, counter-clockwise. |
| `sweepAngle` | number |  | Sweep angle in radians, not 0; positive is counter-clockwise. |
| `incrementAngle` | number |  | Angle of each segment in radians: positive, and at most 3600 segments over `sweepAngle` (default pi/36). |
| `pitch` | number |  |  |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### combineSolids

Combines two solids into a Generic Solid by union, intersection or difference.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: combineSolids" · **In runToolBatch:** yes

**Details**

Combine two solid objects by `blankUuid` and `toolUuid` with `operation` union, intersection or difference. Both inputs are copied and remain unchanged; a locked solid, or a solid that is not in a layer, a symbol definition or a group of these, is refused. The result is a Generic Solid with its Boolean operation and history; the result includes `bounds3D` { min, max } in world Z and `layerElevation` in world units.

> **Note:** The result includes the getSolid values of the new solid.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `operation` | string | Yes | One of: `union`, `intersection`, `difference`. |
| `blankUuid` | string | Yes |  |
| `toolUuid` | string | Yes |  |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createShell

Creates a shell by thickening a NURBS surface or hollowing a solid.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createShell" · **In runToolBatch:** yes

**Details**

Create a shell from a NURBS surface (thicken it) or a solid (hollow it). `uuid` identifies the source and `thickness` is finite, non-zero and signed; for a solid, `openFaceIndices` is a non-empty array of 0-based faces to remove. The source is copied and stays unchanged; the shell can retain the source's container instead of going on the active layer.

A locked source, or a source that is not in a layer, a symbol definition or a group of these, is refused. The optional `select` creation option controls whether the shell is selected. Returns kind shell, its Generic Solid history, `openFaceIndices` resolved against the source's current faces when available, `bounds3D` { min, max } in world Z and `layerElevation` in world units.

> **Note:** The result includes the getSolid values of the new solid.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string | Yes | The UUID of the source NURBS surface or solid (only a UUID; `name` is the name of the new shell). |
| `thickness` | number | Yes | Thickness, in world units. |
| `openFaceIndices` | array of integer | For a solid | Required for a solid source: a non-empty array of 0-based faces to remove (each below the solid's face count). Refused for a NURBS surface. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### convertSolid

Creates a copy of a solid converted to a Generic Solid or a mesh.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: convertSolid" · **In runToolBatch:** yes

**Details**

Create a copy of the supported solid identified by `sourceUuid`, converted to `genericSolid` (history-free) or `mesh`; the source stays unchanged. A Generic Solid result can retain the source's container instead of going on the active layer; a solid that is not in a layer, a symbol definition or a group of these is refused; converting to `genericSolid` also refuses a locked solid.

The optional `select` creation option controls whether the result is selected. Returns the object reference, the resulting `kind`, `bounds3D` { min, max } in world Z and `layerElevation` in world units; Generic Solid results also include their history.

> **Note:** The result includes the getSolid values of the new solid (for `convertSolid`, only with `to` `genericSolid`).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `sourceUuid` | string | Yes |  |
| `to` | string | Yes | One of: `genericSolid`, `mesh`. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### getSolid

Reads a solid: its kind, 3D bounds, parameters and Generic Solid history.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read a solid by uuid, name or index: the object reference, its `kind` (extrude, multipleExtrude, sweep, sphere, hemisphere, cone, genericSolid or shell), `bounds3D` { min, max } in world Z, `layerElevation` in world units (null without a design-layer owner) and the values of its kind. Frames, centers, points and elevations are in world Z too, like the arguments of the create and edit tools; nothing is converted between coordinate systems. extrude: baseElevation, thickness, topElevation, transform { origin, uAxis, vAxis, wAxis }, volume, profileBounds (2D, in the coordinates of the profile), holeCount and holes [{ index, bounds }]. multipleExtrude: baseElevation, thickness, topElevation and profileCount. sweep: startAngle, sweepAngle, incrementAngle, pitch and profileCount (without the axis locus). sphere and hemisphere: center, radii { x, y, z } (along the local axes), isEllipsoid, frame { origin, uAxis, vAxis, wAxis }, axis (the local Z; a hemisphere's dome points along it), volume and surfaceArea; hemisphere also topPoint. cone: baseCenter, tipPoint, height, radii { i, j }, isRightCone, isElliptical, frame, axis (from the base towards the tip), analytic volume and surfaceArea; asymmetric cone area approximates the closed surface from the existing polygonal cache and is omitted if unavailable; right circular cones retain their analytic lateral area.

**Generic Solids and shells:** hasHistory, operation when known, volume, surfaceArea, and history entries with object references, nesting depth, operand index, parent UUID and nested operation; shells also report thickness, openFaceIndices (current source indices, resolving persistent face names) and sourceUuid when available. Volumes and areas are in world units; values that Vectorworks cannot report are left out.

> **Note:** For Generic Solids and shells, `history` lists the solid and its operands in pre-order, starting with the solid itself at `depth` 0. Each entry is an [object reference](Common.md#object-references) with `depth`, `hasHistory` (false for an operand that is not a Generic Solid), and, for operands (`depth` &gt; 0), `operandIndex` and `parentUuid` (when available); a Boolean Generic Solid entry adds `operation` (`union`, `intersection` or `difference`). A shell's `sourceUuid` is the copy of the source that the shell holds, not the `uuid` given to createShell.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |

### editSolid

Moves, rotates, scales, re-orients or resizes a solid.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: editSolid" · **In runToolBatch:** yes

**Details**

Edit a supported solid by uuid, name or index; the call is one undo step. Refused, with nothing changed: an object that getSolid does not take, a Generic Solid or shell (getSolid reads their history, but editSolid does not edit them), a locked solid (unlock it first with editObject `locked` false), a solid that is not in a layer, a symbol definition or a group of these (e.g. an operand of a Generic Solid, or in a wall, a plug-in object or a viewport), an operation that the kind does not take, a wrong value and a call without changes.

The operations, applied in this order: `transform` { origin, uAxis, vAxis, wAxis? } (orthonormal; spheres, hemispheres and cones take a right-handed frame), `move3D` { offset } and `rotate3D` { center, axis, angle } (radians, right-handed about the axis) for extrudes, spheres, hemispheres and cones; `scale3D` { center, factor &gt; 0 } and `axis` (turns the local Z to this direction) for spheres, hemispheres and cones; `baseElevation`, `thickness` and `topElevation` (sets the thickness; not with `thickness`) for extrudes and multiple extrudes; for extrudes `removeHoles` (indices of getSolid `holes`) or `removeAllHoles` true, then `addHoles` (as createExtrude `holes`); sphere and hemisphere: `center`, then `radius` or `radii` { x, y, z }; hemisphere: `topPoint` (turns the dome to it and sets the radius to its distance); cone: `baseCenter` (moves the cone), `tipPoint` with `keepRight` (default true: the cone turns to stay a right cone; false keeps the base plane and makes it oblique), `height` (makes a right cone; negative flips it), `radius` or `radii` { i, j }; sweep: `startAngle`, `sweepAngle`, `incrementAngle` and `pitch`.

Returns the object reference, `changed` (the arguments applied, in order) and the getSolid values after the change.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `transform` | object |  |  |
| `transform.origin` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `transform.uAxis` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `transform.vAxis` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `transform.wAxis` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `move3D` | object |  |  |
| `move3D.offset` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `rotate3D` | object |  |  |
| `rotate3D.center` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `rotate3D.axis` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `rotate3D.angle` | number | Yes |  |
| `scale3D` | object |  |  |
| `scale3D.center` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `scale3D.factor` | number | Yes |  |
| `axis` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `baseElevation` | number |  | World Z of the base, for an extrude or a multiple extrude. |
| `thickness` | number |  | Thickness, in world units. |
| `topElevation` | number |  | Sets the thickness; not with `thickness`. |
| `removeHoles` | array of integer |  | Indices of getSolid `holes`. |
| `removeAllHoles` | boolean |  |  |
| `addHoles` | array of object |  | As createExtrude `holes`. |
| `addHoles[].points` | array of [point](Common.md#points) |  |  |
| `addHoles[].uuid` | string |  |  |
| `center` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `radius` | number |  | Radius, in world units. |
| `radii` | object |  | Sphere and hemisphere: { x, y, z }; cone: { i, j }. |
| `radii.x` | number |  |  |
| `radii.y` | number |  |  |
| `radii.z` | number |  |  |
| `radii.i` | number |  |  |
| `radii.j` | number |  |  |
| `topPoint` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `baseCenter` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `tipPoint` | [3D point](Common.md#points) |  | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `keepRight` | boolean |  | Cone, with `tipPoint`: default true, the cone turns to stay a right cone; false keeps the base plane (oblique). Not an edit by itself. |
| `height` | number |  | Makes a right cone; negative flips it. |
| `startAngle` | number |  | Start angle in radians, counter-clockwise. |
| `sweepAngle` | number |  | Sweep angle in radians, not 0; positive is counter-clockwise. |
| `incrementAngle` | number |  | Angle of each segment in radians: positive, and at most 3600 segments over `sweepAngle`. |
| `pitch` | number |  |  |

### create3DPolygon

Creates a 3D polygon from 3D points, from 2D points at a height, or from a rectangle.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: create3DPolygon" · **In runToolBatch:** yes

**Details**

Create a 3D polygon from exactly one source: `points` (2 to 32767 3D points { x, y, z }, world Z), `points2D` (2 to 32767 points { x, y } in the plane at the world Z `z`, default 0) or `rect` { left, top, right, bottom } (the form getObjectInfo `bounds` reports) at `z`. `closed` (default true) applies to points and points2D; a rect is always closed, and `z` does not apply to `points`.

Every argument is checked before anything is created; the polygon goes on the active layer. Returns the object reference, `kind` polygon3D, `vertexCount`, `closed`, `bounds3D` { min, max } in world Z and `layerElevation` (the owning design layer's world-Z elevation, null without one); get3DGeometry reads the polygon and edit3DGeometry edits it.

> **Note:** A `z` together with `points` (each point has its own z), and `closed` false together with `rect`, are refused.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `points` | array of [3D point](Common.md#points) |  | Each item: A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `points2D` | array of [point](Common.md#points) |  | 2 to 32767 points { x, y } in the plane at the world Z `z`, default 0. |
| `rect` | [rectangle](Common.md#rectangles) |  |  |
| `z` | number |  | Z value (height), in world units. |
| `closed` | boolean |  | Whether the shape is closed. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createMesh

Creates a mesh from vertices and faces, from polygons or from a group of 3D polygons.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createMesh" · **In runToolBatch:** yes

**Details**

Create a mesh from exactly one source: `vertices` (3 or more 3D points { x, y, z }, world Z) with `faces` (an array of faces, each an array of 3 or more 0-based indices into `vertices`, counter-clockwise seen from outside), `polygons` (an array of polygons, each 3 or more 3D points in world Z; coincident points are welded into shared vertices) or `groupUuid` (a group that holds only 3D polygons and groups of them, e.g. the result of convertTo3D `polygons`: the mesh is made of a copy and placed right after the group, which stays).

A locked group, or a group that is not in a layer, a symbol definition or a group of these, is refused. Every argument is checked before anything is created; meshes of vertices or polygons go on the active layer. Returns the object reference, `kind` mesh, `vertexCount`, `faceCount`, `isClosed` (watertight), `bounds3D` { min, max } in world Z and `layerElevation` in world units.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `vertices` | array of [3D point](Common.md#points) |  | Each item: A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `faces` | array of array of integer |  | An array of faces, each an array of 3 or more 0-based indices into `vertices`, counter-clockwise seen from outside. A face can also be an object { vertexIndices, part? }; `part` is 0, the overall part, by default. |
| `polygons` | array of array of [3D point](Common.md#points) |  | An array of polygons, each 3 or more 3D points in world Z; coincident points are welded into shared vertices. |
| `groupUuid` | string |  |  |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createNurbsCurve

Creates a NURBS curve from control points or fit points.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createNurbsCurve" · **In runToolBatch:** yes

**Details**

Create a NURBS curve from `points` (3D points { x, y, z }, world Z: 2 to 1000, or to 998 for a fit-point curve of degree 2 or more, which Vectorworks gives 2 control points more than fit points): `pointKind` control (default: the points are the control points, which the curve follows without passing through all of them) or fit (the curve passes through every point); `degree` (a whole number from 1 to 28, default 3; a control-point curve of degree d needs at least d + 1 points); `weights` (control points only: one weight from 0.0001 to 100 for each point; a higher weight pulls the curve toward its point).

Every argument is checked before anything is created; the curve goes on the active layer. Returns the object reference, `kind` nurbsCurve, `pieceCount`, `degree`, `pointCount` and `controlPointCount` (of the first piece), `length` (null when unavailable), `bounds3D` { min, max } in world Z and `layerElevation` (the owning design layer's world-Z elevation, null without one); get3DGeometry reads and measures the curve and edit3DGeometry edits it.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `points` | array of [3D point](Common.md#points) | Yes | Each item: A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `pointKind` | string |  | One of: `control`, `fit`. |
| `degree` | integer |  | A whole number from 1 to 28, default 3; a control-point curve of degree d needs at least d + 1 points. |
| `weights` | array of number |  | Control points only: one weight from 0.0001 to 100 for each point; a higher weight pulls the curve toward its point. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createNurbsSurface

Creates a NURBS surface from its control net.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createNurbsSurface" · **In runToolBatch:** yes

**Details**

Create a NURBS surface from its control net `points`: an array of 2 or more rows, each an array of 2 or more 3D points { x, y, z } in world Z, every row of the same length; points[u][v] is the point v of the row u (at most 32767 rows and points per row). `uDegree` and `vDegree`: whole numbers from 1 to 28; a direction of n points takes a degree up to n - 1, and by default the lower of 3 and n - 1.

`weights` (optional, of the shape of `points`: a weight from 0.0001 to 100 for each control point). Every argument is checked before anything is created; the surface goes on the active layer. Returns the object reference, `kind` nurbsSurface, `uPointCount`, `vPointCount`, `uDegree`, `vDegree`, `bounds3D` { min, max } in world Z and `layerElevation` in world units; get3DGeometry reads the surface and edit3DGeometry edits it.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `points` | array of array of [3D point](Common.md#points) | Yes | The points, in order. |
| `uDegree` | integer |  |  |
| `vDegree` | integer |  |  |
| `weights` | array of array of number |  |  |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### createSurfaceModel

Creates a loft, rail sweep, revolve or extrude-along-path surface model from existing objects.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createSurfaceModel" · **In runToolBatch:** yes

**Details**

Create a surface model of `kind` from copies of existing objects, which stay unchanged: loft: NURBS surfaces skinned through `sectionUuids` (2 or more sections in order, each a NURBS curve or a 3D locus, at least one of them a curve), `ruled` (default false: smooth; true: straight between neighboring sections; two sections always make a ruled loft) and `closed` (default false; true returns the loft from the last section to the first, so its 3 or more sections must go around a loop, e.g. around an axis: sections in a row make the closing part cross the loft, and Vectorworks then makes no loft); railSweep: `sectionUuids` (1 or more NURBS curves) swept along the NURBS curve `railUuid` and, when given, the second rail `secondRailUuid`.

**Loft and railSweep:** `solid` (default false: surfaces open at their ends; true: end caps, except for a closed loft, and sewing into one Generic Solid; the sections must be closed curves and the result must close, or nothing is created). revolve: the 2D shape `profileUuid` (a line, rectangle, rounded rectangle, oval, arc, polygon, freehand polygon or polyline) revolved as createSweep revolves a profile without `axisUuid` (the profile's X is the radius and its Y lies along the axis, the left edge of the profile, parallel to world Y) with createSweep's `startAngle` (default 0), `sweepAngle` (default 2\*pi), `incrementAngle` (default pi/36) and `pitch` (default 0): the shape and place of createSweep's sweep, made of NURBS surfaces; or, with `railUuid` and the required `axisUuid` (the profile, the rail and the axis each a 2D shape, a NURBS curve or a 3D polygon; no angles or pitch), the profile revolved about the axis along the rail: the axis must be straight, the profile must lie in one plane with the axis without crossing it, and the rail must leave that plane (a planar rail lies in a plane perpendicular to it). extrudeAlongPath: `profileUuid` (a planar 2D shape, NURBS curve or 3D polygon that does not cross itself) swept along the NURBS curve `pathUuid`, with `scale` (greater than 0, default 1; with the default linear scaling, 1 keeps the size of the profile), `exponentialScale` (default false: the profile scales linearly along the path; true: exponentially), `lockProfilePlane` (default false; true sweeps with a lock direction, Z once Vectorworks has turned the path into the XY plane, to which the profile keeps its orientation), `fixProfile` (default false; true sweeps the profile where it is drawn instead of turning it to the start of the path, and then the path must not start parallel to the plane of the profile); along a closed path or a path with corners, only `scale` 1 without `exponentialScale` works. The arguments of another kind and an object given for two inputs are refused. Every argument is checked before anything is created; the result goes on the active layer. Returns the object reference, `kind` (nurbsSurface; genericSolid when Vectorworks makes a solid of a composite surface; group for several results, with `members` [{ reference, kind }]), `bounds3D` { min, max } in world Z (for NURBS surfaces, Vectorworks' box of all their control points, also where a trimmed surface is cut away, which can be larger than the surface) and `layerElevation` in world units; get3DGeometry reads NURBS surfaces and getSolid reads Generic Solids.

> **Note:** The `kind` of a result that is none of these is `surfaceModel`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `kind` | string | Yes | One of: `loft`, `railSweep`, `revolve`, `extrudeAlongPath`. |
| `sectionUuids` | array of string |  | `loft`: 2 or more sections in order (3 or more when `closed`), each a NURBS curve or a 3D locus, at least one of them a curve. `railSweep`: 1 or more NURBS curves. |
| `ruled` | boolean |  |  |
| `closed` | boolean |  | Whether the shape is closed. |
| `solid` | boolean |  |  |
| `railUuid` | string |  | `railSweep`: a NURBS curve; `revolve`: a 2D shape, a NURBS curve or a 3D polygon (with `axisUuid`). |
| `secondRailUuid` | string |  | `railSweep` only: a second NURBS curve rail. |
| `profileUuid` | string |  | `revolve` without `railUuid`: a line, rectangle, rounded rectangle, oval, arc, polygon, freehand polygon or polyline. `revolve` with `railUuid` and `extrudeAlongPath`: a 2D shape, a NURBS curve or a 3D polygon (for `extrudeAlongPath` planar and not crossing itself). |
| `axisUuid` | string |  |  |
| `startAngle` | number |  | Start angle in radians, counter-clockwise. |
| `sweepAngle` | number |  | Sweep angle in radians, not 0; positive is counter-clockwise. |
| `incrementAngle` | number |  | Angle of each segment in radians: positive, and at most 3600 segments over `sweepAngle` (default pi/36). |
| `pitch` | number |  |  |
| `pathUuid` | string |  | `extrudeAlongPath`: the UUID of a NURBS curve, the path. |
| `scale` | number |  | Greater than 0, default 1; with the default linear scaling, 1 keeps the size of the profile. |
| `exponentialScale` | boolean |  |  |
| `lockProfilePlane` | boolean |  |  |
| `fixProfile` | boolean |  |  |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

### get3DGeometry

Reads a 3D polygon, mesh, NURBS curve or NURBS surface.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read a 3D polygon, a mesh, a NURBS curve or a NURBS surface by uuid, name or index (getSolid reads solids). Vertices, points and `bounds3D` { min, max } use world Z; `layerElevation` is the owning design layer's world-Z elevation (null without one); angles are radians. `limit` (default 100), `offset` and `countOnly` apply to each list: a list is { count, returned, offset, limit, truncated, nextOffset (when truncated), items } (no items with countOnly). 3D polygon: kind polygon3D, vertexCount, closed, planar, normal (unit, right-handed to the vertex order; null when unavailable), plane { point, normal, d } (normal . p + d = 0; null when unavailable), area (null when open), length (with the closing edge when closed), bounds3D, layerElevation and `vertices` (items { x, y, z }).

**Mesh:** kind mesh, vertexCount, faceCount, isClosed (watertight), surfaceArea, volume (null unless closed), smoothing (none, documentPreference, customCrease or imported), creaseAngle (radians; null when unavailable), parts [{ id, texture, faceCount }] (part 0 is the overall part; texture 0 is none), bounds3D, layerElevation, `vertices` (items { x, y, z }) and `faces` (items { vertexIndices, part }).

**NURBS curve:** kind nurbsCurve, pieceCount, degree, pointCount and controlPointCount (of the first piece), length (null when unavailable), bounds3D, layerElevation, pieces [{ index, degree, pointCount, controlPointCount, knotCount }], and of the piece `piece` (default 0): `piece`, `points` (items { x, y, z, weight }: the points that define the piece, its fit points or its control points; `weight` is the weight of the control point of that index, when there is one) and `knots` (all of them). Measurements of a curve, each an array of 1 to 100 entries, with null values where Vectorworks has no result: `atDistance` [distances from 0 to the length] returns `pointsAtDistance` [{ distance, point, piece, parameter }]; `closestTo` [3D points] returns `closestPoints` [{ to, point, distance, piece, parameter }]; `evaluate` [{ piece? (default 0), parameter }] returns `evaluated` [{ piece, parameter, point, tangent (a unit vector), curvature (in 1 / world units) }]; `divide` { count (2 to 1000), includeEnd? (default true: both ends) } returns `divisionPoints`, count points equally spaced along the curve (an error when Vectorworks cannot divide it). Parameters are the native knot parameters of a piece (within its `knots`), not arc lengths.

**NURBS surface:** kind nurbsSurface, uPointCount, vPointCount, uDegree, vDegree, uKnots and vKnots (all of them), bounds3D, layerElevation and `points`, the control net in u-major order (item i is points[i / vPointCount][i % vPointCount]: { u, v, x, y, z, weight }); `evaluate` [{ u, v }] (1 to 100 parameters within uKnots and vKnots) returns `evaluated` [{ u, v, point }]. `piece`, `atDistance`, `closestTo` and `divide` apply to NURBS curves only, and `evaluate` to NURBS curves and surfaces.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |
| `piece` | integer |  | Used for NURBS curve. |
| `atDistance` | array of number |  |  |
| `closestTo` | array of [3D point](Common.md#points) |  | Each item: A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `evaluate` | array of object |  |  |
| `evaluate[].piece` | integer |  |  |
| `evaluate[].parameter` | number |  |  |
| `evaluate[].u` | number |  |  |
| `evaluate[].v` | number |  |  |
| `divide` | object |  |  |
| `divide.count` | integer | Yes |  |
| `divide.includeEnd` | boolean |  |  |

### edit3DGeometry

Edits a 3D polygon, mesh, NURBS curve or NURBS surface.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: edit3DGeometry" · **In runToolBatch:** yes

**Details**

Edit a 3D polygon, a mesh, a NURBS curve or a NURBS surface by uuid, name or index; the call is one undo step (editSolid edits solids). Points and bounds3D use world Z; angles are radians; indices are 0-based. Refused, with nothing changed: an object of another kind, a locked object (unlock it first with editObject `locked` false), an object that is not in a layer, a symbol definition or a group of these, an operation that the kind does not take, a call without operations, a creating operation with any other operation, and a wrong value.

The operations, applied in this order: `vertices` (replaces all; a polygon takes 2 to 32767 3D points; a mesh with `faces` may change its vertex count, which clears its normals and UVs, and without `faces` keeps it), `faces` (mesh: [{ vertexIndices, part? }], replaces the faces), `setVertex` { index, point }, `insertVertex` { index, point } (polygon: before index; index = vertexCount appends), `deleteVertex` { index } (polygon: keeps at least 2 vertices), `addFace` { vertexIndices, part? }, `deleteFace` { index } and `setFacePart` { index, part } (mesh), `closed` (polygon), `reverse` true (polygon) or `flipFaces` true (mesh), `cleanup` { tolerance? } (polygon: removes duplicate and collinear vertices), `simplify` (polygon { maxDeviation &gt; 0 }: Douglas-Peucker; mesh { quality }: the percent of detail to keep, 0 &lt; quality &lt; 100, lower removes more faces), `segment` { maxSegmentLength &gt; 0 } (polygon: subdivides longer edges), `smoothing` (mesh: none, documentPreference or customCrease), `creaseAngle` (mesh: from 0 to pi; switches the smoothing to customCrease), `addPart` { texture? } (mesh: a part with a texture resource reference, 0 for none; returns its id as `addedPart`), `setPartTexture` { part, texture } (mesh), then for both `move3D` { offset }, `rotate3D` { center, axis, angle } (right-handed about the axis) and `scale3D` { center, factor &gt; 0 }.

**NURBS curves and surfaces:** `setPoint` (curve { piece? (default 0), index, point }: a point of get3DGeometry `points` of the piece; surface { u, v, point }: a control point of the net), `setWeight` (curve { piece?, index, weight }, index of a control point; surface { u, v, weight }; weight from 0.0001 to 100; a curve piece defined by fit points takes no weights), then `trimByCurve` { curveUuid } (surface: a copy of the NURBS curve becomes its trim boundary; the curve stays). NURBS take no move3D, rotate3D or scale3D (there are no 3D transforms of NURBS), and knots are not edited (runPythonScript can). Creating operations, each the only operation of its call, leave the object unchanged: `toPlanarSolid` { thickness } (not 0; a closed, planar polygon of 3 or more vertices) makes a Generic Solid on the active layer, the polygon extruded along its normal; `repair` true (mesh) makes repaired meshes right after the mesh; `extend` { distance &gt; 0, atStart? (default false: the end), linear? (default false), direction (surface only, required: u or v) } and `offset` { distance } (not 0) make an extended or offset copy of a NURBS curve or surface on the active layer. Returns the object reference, `changed` (the operations applied, in order), `kind`, `vertexCount`, `closed` (polygon) or `faceCount` and `isClosed` (mesh), `pieceCount`, `degree`, `pointCount`, `controlPointCount` and `length` (curve) or `uPointCount`, `vPointCount`, `uDegree` and `vDegree` (surface), `bounds3D` and `layerElevation`; `toPlanarSolid` adds `created` (the reference and getSolid values of the new solid), `repair` adds `created`, an array of the new meshes (empty when Vectorworks made none), and `extend` and `offset` add `created` (the reference and these values of the new curve or surface).

> **Note:** The objects that `toPlanarSolid`, `repair`, `extend` and `offset` create take no creation options (`class`, `name`, `select`, `useClassAttributes`).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `vertices` | array of [3D point](Common.md#points) |  | Each item: A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `faces` | array of object |  | Mesh: [{ vertexIndices, part? }], replaces the faces. A face can also be a plain array of 3 or more vertex indices. |
| `faces[].vertexIndices` | array of integer | Yes |  |
| `faces[].part` | integer |  |  |
| `setVertex` | object |  |  |
| `setVertex.index` | integer | Yes |  |
| `setVertex.point` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `insertVertex` | object |  |  |
| `insertVertex.index` | integer | Yes |  |
| `insertVertex.point` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `deleteVertex` | object |  |  |
| `deleteVertex.index` | integer | Yes |  |
| `addFace` | object |  | Mesh: { vertexIndices, part? }, or a plain array of 3 or more vertex indices. |
| `addFace.vertexIndices` | array of integer | Yes |  |
| `addFace.part` | integer |  |  |
| `deleteFace` | object |  |  |
| `deleteFace.index` | integer | Yes |  |
| `setFacePart` | object |  |  |
| `setFacePart.index` | integer | Yes |  |
| `setFacePart.part` | integer | Yes |  |
| `closed` | boolean |  | Whether the shape is closed. |
| `reverse` | boolean |  | Polygon: true reverses the vertex order; false is refused. |
| `flipFaces` | boolean |  | Mesh: true flips the faces; false is refused. |
| `cleanup` | object |  |  |
| `cleanup.tolerance` | number |  |  |
| `simplify` | object |  |  |
| `simplify.maxDeviation` | number |  |  |
| `simplify.quality` | number |  |  |
| `segment` | object |  |  |
| `segment.maxSegmentLength` | number | Yes |  |
| `smoothing` | string |  | One of: `none`, `documentPreference`, `customCrease`. |
| `creaseAngle` | number |  | Mesh: from 0 to pi; switches the smoothing to customCrease, so a `smoothing` given with it must be customCrease. |
| `addPart` | object |  |  |
| `addPart.texture` | integer |  |  |
| `setPartTexture` | object |  |  |
| `setPartTexture.part` | integer | Yes |  |
| `setPartTexture.texture` | integer | Yes |  |
| `move3D` | object |  |  |
| `move3D.offset` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `rotate3D` | object |  |  |
| `rotate3D.center` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `rotate3D.axis` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `rotate3D.angle` | number | Yes |  |
| `scale3D` | object |  |  |
| `scale3D.center` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `scale3D.factor` | number | Yes |  |
| `setPoint` | object |  |  |
| `setPoint.piece` | integer |  |  |
| `setPoint.index` | integer |  |  |
| `setPoint.u` | integer |  |  |
| `setPoint.v` | integer |  |  |
| `setPoint.point` | [3D point](Common.md#points) | Yes | A 3D point or a vector in world units: { x, y, z }. Point Z is absolute world Z, like bounds3D: the tools add no design layer elevation to it; vectors are independent of layer elevation. |
| `setWeight` | object |  |  |
| `setWeight.piece` | integer |  |  |
| `setWeight.index` | integer |  |  |
| `setWeight.u` | integer |  |  |
| `setWeight.v` | integer |  |  |
| `setWeight.weight` | number | Yes |  |
| `trimByCurve` | object |  |  |
| `trimByCurve.curveUuid` | string | Yes |  |
| `toPlanarSolid` | object |  |  |
| `toPlanarSolid.thickness` | number | Yes |  |
| `repair` | boolean |  | Mesh: true repairs the mesh; false is refused. |
| `extend` | object |  |  |
| `extend.distance` | number | Yes |  |
| `extend.atStart` | boolean |  |  |
| `extend.linear` | boolean |  |  |
| `extend.direction` | string |  | One of: `u`, `v`. |
| `offset` | object |  |  |
| `offset.distance` | number | Yes |  |

### convertTo3D

Converts a copy of an object to 3D polygons, a mesh or a Generic Solid.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: convertTo3D" · **In runToolBatch:** yes

**Details**

Convert a copy of the 2D or 3D object `sourceUuid` to `to`: `polygons` (a group of 3D polygons), `mesh` or `genericSolid` (history-free; a 2D object is refused: convert it to `polygons` or `mesh`, or extrude it). convertSolid takes solids only; convertTo3D takes any 2D or 3D object. The source stays unchanged, and the result is placed right after it, in its container; a source that is not in a layer, a symbol definition or a group of these is refused, and so is a locked source for `genericSolid`.

The optional `select` creation option controls whether the result is selected. Returns the object reference, `kind` (group, mesh or genericSolid), `bounds3D` { min, max } in world Z and `layerElevation` in world units; a group adds `polygonCount`, a mesh `vertexCount`, `faceCount` and `isClosed`, a Generic Solid its getSolid values. createMesh `groupUuid` makes a mesh of such a group; get3DGeometry reads 3D polygons and meshes.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `sourceUuid` | string | Yes |  |
| `to` | string | Yes | One of: `polygons`, `mesh`, `genericSolid`. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |
