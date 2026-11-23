**English** • [Deutsch](../../PythonAPI.de/v2027.2/Objects3D.md) • [日本語](../../PythonAPI.ja/v2027.2/Objects3D.md)

# Objects3D — 3D objects

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The 3D object classes: extrudes, multiple extrudes and sweeps, solid objects (solid additions, subtractions and intersections, which keep their modeling history, and history-free generic solids), solid primitives (spheres, hemispheres, cones, ...), NURBS curves and surfaces, 3D polygons, meshes, shell solids and surface models. All of them derive from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject), so the shared object operations (name, class, layer, attributes, bounds, moving, deleting, ...) are documented there.

Coordinates are world units in the 3D model space; angles are radians.

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [ExtrudeObject](#extrudeobject)
    - [ExtrudeObject.Values](#extrudeobjectvalues)
    - [ExtrudeObject.Transform](#extrudeobjecttransform)
  - [SweepObject](#sweepobject)
    - [SweepObject.Values](#sweepobjectvalues)
  - [MultiExtrudeObject](#multiextrudeobject)
  - [SurfaceModelObject](#surfacemodelobject)
    - [SurfaceModelObject.PathOptions](#surfacemodelobjectpathoptions)
  - [GenericSolidObject](#genericsolidobject)
    - [GenericSolidObject.HistoryStep](#genericsolidobjecthistorystep)
    - [GenericSolidObject.Operation](#genericsolidobjectoperation)
  - [ShellObject](#shellobject)
  - [Polygon3DObject](#polygon3dobject)
    - [Polygon3DObject.Plane](#polygon3dobjectplane)
    - [Polygon3DObject.ClosestPoint](#polygon3dobjectclosestpoint)
  - [MeshObject](#meshobject)
    - [MeshObject.Face](#meshobjectface)
    - [MeshObject.Part](#meshobjectpart)
    - [MeshObject.Smoothing](#meshobjectsmoothing)
  - [SolidPrimitiveObject](#solidprimitiveobject)
    - [SolidPrimitiveObject.Kind](#solidprimitiveobjectkind)
  - [SphereObject](#sphereobject)
  - [HemisphereObject](#hemisphereobject)
  - [ConeObject](#coneobject)
    - [ConeObject.Radii](#coneobjectradii)
  - [NurbsCurveObject](#nurbscurveobject)
    - [NurbsCurveObject.Location](#nurbscurveobjectlocation)
  - [NurbsSurfaceObject](#nurbssurfaceobject)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`ExtrudeObject`](#extrudeobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Native extrude (not a plug-in object). |
| [`ExtrudeObject.Values`](#extrudeobjectvalues) | class (nested) |  | Local base elevation and signed thickness, in world units. |
| [`ExtrudeObject.Transform`](#extrudeobjecttransform) | class (nested) |  | Orthonormal local axes and origin in the parent coordinate system (identity by default). |
| [`SweepObject`](#sweepobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Native sweep. |
| [`SweepObject.Values`](#sweepobjectvalues) | class (nested) |  | Sweep angles in radians and pitch in world units per full turn. |
| [`MultiExtrudeObject`](#multiextrudeobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Native multiple extrude. |
| [`SurfaceModelObject`](#surfacemodelobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | A modeling result is a NURBS surface, a CSG solid, or a group of modeling results. |
| [`SurfaceModelObject.PathOptions`](#surfacemodelobjectpathoptions) | class (nested) |  | Extrude-along-path scale and profile-placement options. |
| [`GenericSolidObject`](#genericsolidobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Covers native solid objects, including solid additions, subtractions and intersections and history-free generic solids. |
| [`GenericSolidObject.HistoryStep`](#genericsolidobjecthistorystep) | class (nested) |  | One node in the native construction tree, in preorder. |
| [`GenericSolidObject.Operation`](#genericsolidobjectoperation) | IntEnum (nested) |  | Solid Boolean operation. |
| [`ShellObject`](#shellobject) | class | [`GenericSolidObject`](#genericsolidobject) | Shell solid: a CSG offset node (Shell Solid tool, VectorScript CreateShell). |
| [`Polygon3DObject`](#polygon3dobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Native 3D polygon (`ObjectType.Polygon3D`). |
| [`Polygon3DObject.Plane`](#polygon3dobjectplane) | class (nested) |  | Plane through the vertex centroid; normal is a unit vector following the vertex order (right-hand rule) and d satisfies normal . |
| [`Polygon3DObject.ClosestPoint`](#polygon3dobjectclosestpoint) | class (nested) |  | Closest point on the polygon path, its distance, edge index and path distance from the first vertex. |
| [`MeshObject`](#meshobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Native mesh (`ObjectType.Mesh`): a shared vertex list plus polygonal faces that index into it. |
| [`MeshObject.Face`](#meshobjectface) | class (nested) |  | part 0 means the overall (untextured) part, see `GetOverallPart()`. |
| [`MeshObject.Part`](#meshobjectpart) | class (nested) |  | Texture part: id, texture reference (0 = untextured) and number of faces using it. |
| [`MeshObject.Smoothing`](#meshobjectsmoothing) | IntEnum (nested) |  | How the mesh is smoothed when it is rendered. |
| [`SolidPrimitiveObject`](#solidprimitiveobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Common base of the native parametric solid primitives (`ObjectType.Solid`): spheres, hemispheres and cones. |
| [`SolidPrimitiveObject.Kind`](#solidprimitiveobjectkind) | IntEnum (nested) |  | Kind of a solid primitive. |
| [`SphereObject`](#sphereobject) | class | [`SolidPrimitiveObject`](#solidprimitiveobject) | Native sphere solid: center and I/J/K radii (unequal radii give an ellipsoid); lightweight view of the drawing object. |
| [`HemisphereObject`](#hemisphereobject) | class | [`SphereObject`](#sphereobject) | Native hemisphere solid: center, radii and a dome pointing along the local K axis; lightweight view of the drawing object. |
| [`ConeObject`](#coneobject) | class | [`SolidPrimitiveObject`](#solidprimitiveobject) | Native cone solid. |
| [`ConeObject.Radii`](#coneobjectradii) | class (nested) |  | Base radii along the local I and J axes. |
| [`NurbsCurveObject`](#nurbscurveobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Native piecewise NURBS curve. |
| [`NurbsCurveObject.Location`](#nurbscurveobjectlocation) | class (nested) |  | Curve point and native parameter on a zero-based piece; parameters are not arc lengths. |
| [`NurbsSurfaceObject`](#nurbssurfaceobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Native NURBS surface. |

## Classes

### ExtrudeObject

> **Full name:** `api.ExtrudeObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Native extrude (not a plug-in object). Dimensions and profile coordinates are local to the object matrix; lengths are world units. Wrapping an existing extrude never changes it.

**Constructors**

| Constructor | Description |
|---|---|
| `ExtrudeObject(h: Handle)` | Refers to the existing extrude `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(hProfile: Handle, baseElevation: float, thickness: float, keepOriginal: bool = False) -> ExtrudeObject` *static* | A handle profile must be a native 2D shape. On success it is moved into the extrude, unless keepOriginal is `True` (a copy is used). Failure leaves the original untouched. |
| `Create(profile: Math.Polygon2D, thickness: float) -> ExtrudeObject` *static* | A handle profile must be a native 2D shape. On success it is moved into the extrude, unless keepOriginal is `True` (a copy is used). Failure leaves the original untouched. |
| `Create(profile: Math.Polygon2D, baseElevation: float, thickness: float) -> ExtrudeObject` *static* | A handle profile must be a native 2D shape. On success it is moved into the extrude, unless keepOriginal is `True` (a copy is used). Failure leaves the original untouched. |
| `Create(points: list[Math.Point2D], baseElevation: float, thickness: float, closed: bool = True) -> ExtrudeObject` *static* | A handle profile must be a native 2D shape. On success it is moved into the extrude, unless keepOriginal is `True` (a copy is used). Failure leaves the original untouched. |
| `Create(rect: Math.Rect2D, baseElevation: float, thickness: float) -> ExtrudeObject` *static* | A handle profile must be a native 2D shape. On success it is moved into the extrude, unless keepOriginal is `True` (a copy is used). Failure leaves the original untouched. |
| `CreatePlanar(points: list[Point3D], thickness: float) -> ExtrudeObject` *static* | A closed planar 3D boundary; its plane determines placement. |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, keepOriginal: bool = False) -> ExtrudeObject` *static* | Local Z follows start -> end. The optional up vector defines local +Y (projected onto the profile plane); it must not be parallel to the extrusion direction. |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, up: Point3D, keepOriginal: bool = False) -> ExtrudeObject` *static* | Local Z follows start -> end. The optional up vector defines local +Y (projected onto the profile plane); it must not be parallel to the extrusion direction. |
| `Duplicate() -> ExtrudeObject` | Duplicates the extrude in the drawing and returns the copy. |
| `GetExtrudeValues() -> ExtrudeObject.Values \| None` | Returns the extrude values. |
| `SetExtrudeValues(baseElevation: float, thickness: float) -> bool` | Sets the extrude values. |
| `SetExtrudeValues(values: ExtrudeObject.Values) -> bool` | Sets the extrude values. |
| `GetBaseElevation() -> float \| None` | Returns the base elevation. |
| `SetBaseElevation(baseElevation: float) -> bool` | Sets the base elevation (preserves thickness). |
| `GetThickness() -> float \| None` | Returns the thickness. |
| `SetThickness(thickness: float) -> bool` | Sets the thickness (preserves base elevation). |
| `GetTopElevation() -> float \| None` | Returns the top elevation. |
| `SetTopElevation(topElevation: float) -> bool` | Sets the top elevation (preserves base elevation). |
| `GetBaseObject() -> Handle` | Non-owning profile/hole handles. Edits through these handles require `Reset()`. |
| `SetBaseObject(hProfile: Handle, keepOriginal: bool = False) -> bool` | Sets the base object. Non-owning profile/hole handles. Edits through these handles require `Reset()`. |
| `GetBasePolygon() -> Math.Polygon2D \| None` | Returns the base polygon. |
| `SetBasePolygon(profile: Math.Polygon2D) -> bool` | Sets the base polygon (replaces profile AND holes). |
| `GetHoleObjects() -> list[Handle]` | Returns the hole objects. |
| `GetHoleCount() -> int` | Number of hole items. |
| `GetHoleObject(index: int) -> Handle` | Returns the hole object at `index`. |
| `AddHoleObject(hProfile: Handle, keepOriginal: bool = False) -> bool` | Adds the 2D object `hProfile` as a hole of the profile (a copy of it when `keepOriginal`). Non-owning profile/hole handles. Edits through these handles require `Reset()`. |
| `AddHoleObject(profile: Math.Polygon2D) -> bool` | Adds a hole with the shape `profile`. Non-owning profile/hole handles. Edits through these handles require `Reset()`. |
| `RemoveHole(index: int) -> bool` | Removes the hole at `index`. Non-owning profile/hole handles. Edits through these handles require `Reset()`. |
| `RemoveAllHoles() -> bool` | Removes every hole. Non-owning profile/hole handles. Edits through these handles require `Reset()`. |
| `GetTransform() -> ExtrudeObject.Transform \| None` | Returns the transform. |
| `SetTransform(transform: ExtrudeObject.Transform) -> bool` | Sets the transform (rejects non-orthonormal axes). |
| `Move3D(offset: Point3D) -> bool` | Moves the extrude by `offset` in 3D. |
| `GetVolume() -> float \| None` | Returns the volume (world units cubed). |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### ExtrudeObject.Values

> **Full name:** `api.ExtrudeObject.Values` · **Inherits:** `api.Object`

Local base elevation and signed thickness, in world units.

**Constructors**

| Constructor | Description |
|---|---|
| `Values()` | Default value (fields at their defaults). |
| `Values(baseElevation, thickness)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `baseElevation` | `float` | Elevation of the bottom of the extrude. |
| `thickness` | `float` | Height of the extrude. |

#### ExtrudeObject.Transform

> **Full name:** `api.ExtrudeObject.Transform` · **Inherits:** `api.Object`

Orthonormal local axes and origin in the parent coordinate system (identity by default).

**Constructors**

| Constructor | Description |
|---|---|
| `Transform()` | Default value (fields at their defaults). |
| `Transform(origin, uAxis, vAxis, wAxis)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `origin` | `Point3D` | Origin of the local frame. |
| `uAxis` | `Point3D` | Local X axis. |
| `vAxis` | `Point3D` | Local Y axis. |
| `wAxis` | `Point3D` | Local Z axis (extrusion direction). |

### SweepObject

> **Full name:** `api.SweepObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Native sweep. Profile X is radial and profile Y is axial; the sweep axis is local Y. At angle zero the radial direction is local +Z; positive angles turn towards local +X. Angles are radians, pitch is world units per full turn. Inputs are always copied.

**Constructors**

| Constructor | Description |
|---|---|
| `SweepObject(h: Handle)` | Refers to the existing sweep `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(profile: Handle) -> SweepObject` *static* | Creates a sweep of the 2D object `profile` with the default sweep values. |
| `Create(profile: Handle, values: SweepObject.Values) -> SweepObject` *static* | Creates a sweep of the 2D object `profile` with the sweep values `values`. |
| `Create(profiles: list[Handle], values: SweepObject.Values) -> SweepObject` *static* | An optional 2D locus specifies the axis; otherwise Vectorworks uses the left edge of the profiles. |
| `AreValidValues(values: SweepObject.Values) -> bool` *static* | True when `values` are valid sweep values for `Create`. |
| `Duplicate() -> SweepObject` | Duplicates the sweep in the drawing and returns the copy. |
| `GetSweepValues() -> SweepObject.Values \| None` | Returns the sweep values. |
| `SetSweepValues(values: SweepObject.Values) -> bool` | Sets the sweep values. |
| `GetProfiles() -> list[Handle]` | Returns the profiles. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### SweepObject.Values

> **Full name:** `api.SweepObject.Values` · **Inherits:** `api.Object`

Sweep angles in radians and pitch in world units per full turn.

**Constructors**

| Constructor | Description |
|---|---|
| `Values()` | Default value (fields at their defaults). |
| `Values(startAngle, sweepAngle, incrementAngle, pitch)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `startAngle` | `float` | Start angle of the sweep (radians). |
| `sweepAngle` | `float` | Swept angle (radians, default a full turn; the sign gives the direction). |
| `incrementAngle` | `float` | Positive magnitude; the sign of sweepAngle determines direction. |
| `pitch` | `float` | Positive magnitude; the sign of sweepAngle determines direction. |

### MultiExtrudeObject

> **Full name:** `api.MultiExtrudeObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Native multiple extrude. Profiles are copied in section order, evenly spaced between baseElevation and baseElevation + thickness. At least two native 2D profiles are required.

**Constructors**

| Constructor | Description |
|---|---|
| `MultiExtrudeObject(h: Handle)` | Refers to the existing multiple extrude `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(profiles: list[Handle], baseElevation: float, thickness: float) -> MultiExtrudeObject` *static* | Creates a multiple extrude from the 2D `profiles` (list of handles) at `baseElevation` with the thickness `thickness`. |
| `Duplicate() -> MultiExtrudeObject` | Duplicates the multiple extrude in the drawing and returns the copy. |
| `GetExtrudeValues() -> ExtrudeObject.Values \| None` | Returns the extrude values. |
| `SetExtrudeValues(baseElevation: float, thickness: float) -> bool` | Sets the extrude values. |
| `GetProfiles() -> list[Handle]` | Returns the profiles. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### SurfaceModelObject

> **Full name:** `api.SurfaceModelObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

A modeling result is a NURBS surface, a CSG solid, or a group of modeling results. This is a result-shape check, not a persistent feature/provenance type. Factories preserve all input objects and place one result in the current container. Coordinates and lengths are world units; all angles are radians.

**Constructors**

| Constructor | Description |
|---|---|
| `SurfaceModelObject(h: Handle)` | Refers to the existing surface model `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `CreateLoft(sections: list[Handle], ruled: bool = False, closed: bool = False, solid: bool = False) -> SurfaceModelObject` *static* | Ordered NURBS curves or 3D loci. Closed lofts need at least three sections. solid requests end caps and sewing; failure to sew is reported, not returned as a group. |
| `CreateRailSweep(sections: list[Handle], rail: Handle, secondRail: Handle = None, solid: bool = False) -> SurfaceModelObject` *static* | One or two NURBS rails; sections are NURBS curves, in order along the rails. |
| `CreateRevolve(profile: Handle, values: SweepObject.Values = SweepObject.Values()) -> SurfaceModelObject` *static* | Uses the native sweep profile/axis convention, then converts the result to NURBS. |
| `CreateRevolveWithRail(profile: Handle, rail: Handle, axis: Handle) -> SurfaceModelObject` *static* | Axis must be a linear curve. Vectorworks validates intersections and profile/rail compatibility. |
| `CreateExtrudeAlongPath(path: Handle, profile: Handle) -> SurfaceModelObject` *static* | Path must be a NURBS curve. The result is a history-free CSG solid/sheet. |
| `CreateExtrudeAlongPath(path: Handle, profile: Handle, options: SurfaceModelObject.PathOptions) -> SurfaceModelObject` *static* | Path must be a NURBS curve. The result is a history-free CSG solid/sheet. |
| `CreateTaperedExtrude(profile: Handle, angle: float, height: float) -> SurfaceModelObject` *static* | Creates a tapered extrude of the 2D `profile` with the taper angle `angle` and the height `height`. |
| `CreateCylinder(baseCenter: Point3D, radius: float, height: float) -> ExtrudeObject` *static* | Creates a cylinder (an extrude of a circle) with the base center `baseCenter`, the radius `radius` and the height `height`. |
| `CreateBox(minimum: Point3D, maximum: Point3D) -> ExtrudeObject` *static* | Creates an axis-aligned box (an extrude of a rectangle) from the corner `minimum` to the corner `maximum`. |
| `CreateTorus(center: Point3D, majorRadius: float, minorRadius: float) -> SweepObject` *static* | Ring torus about world Z; majorRadius > minorRadius > 0. |
| `Duplicate() -> SurfaceModelObject` | Duplicates the surface model in the drawing and returns the copy. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### SurfaceModelObject.PathOptions

> **Full name:** `api.SurfaceModelObject.PathOptions` · **Inherits:** `api.Object`

Extrude-along-path scale and profile-placement options.

**Constructors**

| Constructor | Description |
|---|---|
| `PathOptions()` | Default value (fields at their defaults). |
| `PathOptions(isExponentialScale, scale, isProfilePlaneLocked, isProfileFixed)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `isExponentialScale` | `bool` | Scale the profile exponentially (instead of linearly) along the path. |
| `scale` | `float` | Scale of the profile at the end of the path. |
| `isProfilePlaneLocked` | `bool` | Keep the profile plane locked while it follows the path. |
| `isProfileFixed` | `bool` | Keep the profile fixed (not rotated along the path). |

### GenericSolidObject

> **Full name:** `api.GenericSolidObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Covers native solid objects, including solid additions, subtractions and intersections and history-free generic solids. No synthetic history is stored: the document's actual operand tree is used.

**Constructors**

| Constructor | Description |
|---|---|
| `GenericSolidObject(h: Handle)` | Refers to the existing generic solid `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `IsGenericSolid(h: Handle) -> bool` *static* | True when `h` is a generic solid (a CSG solid). |
| `Create(hSolid: Handle, keepOriginal: bool = True) -> GenericSolidObject` *static* | Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreateBoolean(operation: GenericSolidObject.Operation, hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *static* | Creates the solid Boolean `operation` of `hBlank` and `hTool`. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreateUnion(hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *static* | Creates the union of `hBlank` and `hTool`. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreateIntersection(hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *static* | Creates the intersection of `hBlank` and `hTool`. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreateDifference(hBlank: Handle, hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` *static* | Creates `hBlank` minus `hTool`. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreateFromExtrude(hProfile: Handle, baseElevation: float, thickness: float, keepOriginal: bool = True) -> GenericSolidObject` *static* | Creates a solid by extruding the 2D object `hProfile` from `baseElevation` by `thickness`. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreateFromExtrude(profile: Math.Polygon2D, baseElevation: float, thickness: float) -> GenericSolidObject` *static* | Creates a solid by extruding the polygon `profile` from `baseElevation` by `thickness`. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreateFromExtrude(rect: Math.Rect2D, baseElevation: float, thickness: float) -> GenericSolidObject` *static* | Creates a solid by extruding the rectangle `rect` from `baseElevation` by `thickness`. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreateFromExtrude(points: list[Math.Point2D], baseElevation: float, thickness: float, closed: bool = True) -> GenericSolidObject` *static* | Creates a solid by extruding the polygon through `points` from `baseElevation` by `thickness`. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreatePlanar(points: list[Point3D], thickness: float) -> GenericSolidObject` *static* | Creates a solid from the planar 3D polygon `points` with the thickness `thickness`. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, keepOriginal: bool = True) -> GenericSolidObject` *static* | Creates a solid by extruding the profile `hProfile` from `start` to `end`. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, up: Point3D, keepOriginal: bool = True) -> GenericSolidObject` *static* | Creates a solid by extruding the profile `hProfile` from `start` to `end`, with `up` orienting the profile. Existing CSG solids are used as they are or duplicated. Other solid primitives become a one-operand union, retaining the primitive. On success keepOriginal=`False` moves inputs into history; on failure inputs are unchanged. Creation results remain in the input's container, except two-input Boolean results, which are inserted into the active container. |
| `CanConvertToGenericSolid(h: Handle) -> bool` *static* | `True` for objects ConvertToGenericSolid accepts: CSG solids (including shells), extrudes, sweeps, meshes, solid primitives (sphere, hemisphere, cone, ...), closed 3D polygons with at least three vertices and other legal CSG primitives (walls, slabs, NURBS, symbols, ...). |

*Like VectorScript ConvertToGenericSolid*

| Method | Description |
|---|---|
| `ConvertToGenericSolid(hObject: Handle, keepOriginal: bool = True) -> GenericSolidObject` *static* | Builds a history-free generic solid. Kinds the native converter does not take directly are wrapped in a one-operand union first. The result is placed next to the source; keepOriginal=`False` deletes the source on success (do not use it for operands nested in another solid's history). Irreversible on the result. |
| `Duplicate() -> GenericSolidObject` | Duplicates the generic solid in the drawing and returns the copy. |
| `GetAction() -> int \| None` | Returns the action. |
| `GetOperation() -> GenericSolidObject.Operation \| None` | Returns the operation. |
| `HasHistory() -> bool \| None` | True when the solid keeps its modeling history. |
| `SetOperation(operation: GenericSolidObject.Operation) -> bool` | Sets the operation. |
| `GetOperands() -> list[Handle]` | Returns the operands. |
| `GetOperandCount() -> int` | Number of operand items. |
| `GetOperand(index: int) -> Handle` | Returns the operand at `index`. |
| `SetOperand(index: int, hSolid: Handle) -> bool` | Copies the supplied solid into this slot, in native operand coordinates. Only Boolean nodes can be edited. Replaced operand handles are invalidated only on success. |
| `GetHistory() -> list[GenericSolidObject.HistoryStep]` | Returns the history. |
| `Rebuild() -> bool` | Unlike inherited `Reset()`, rebuilds the native CSG caches after edits to history handles. Rebuild the outermost solid after batching edits. `False` leaves the edits in place. |

*Irreversible*

| Method | Description |
|---|---|
| `ClearHistory() -> bool` | Removes all operands and feature data, invalidating their handles. |
| `GetTransform() -> ExtrudeObject.Transform \| None` | Returns the transform. |
| `SetTransform(transform: ExtrudeObject.Transform) -> bool` | Sets the transform. |
| `GetScale() -> Point3D \| None` | Returns the scale. |
| `SetScale(scale: Point3D) -> bool` | Sets the scale. |
| `Move3D(offset: Point3D) -> bool` | Moves the solid by `offset` in 3D. |
| `GetVolume() -> float \| None` | Returns the volume. |
| `GetSurfaceArea() -> float \| None` | Returns the surface area. |
| `ConvertToMesh(keepOriginal: bool = True) -> MeshObject` | Tessellates the solid into a mesh placed right after it; the solid is deleted unless keepOriginal is `True`. Solids nested in another solid's history need keepOriginal = `True`. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### GenericSolidObject.HistoryStep

> **Full name:** `api.GenericSolidObject.HistoryStep` · **Inherits:** `api.Object`

One node in the native construction tree, in preorder.

**Constructors**

| Constructor | Description |
|---|---|
| `HistoryStep()` | Default value (fields at their defaults). |
| `HistoryStep(object, parent, operandIndex, depth, action, operation, hasHistory)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `object` | `Handle` | Handle of the object of this step. |
| `parent` | `Handle` | Handle of the parent step. |
| `operandIndex` | `int` | Index of the operand in its parent. |
| `depth` | `int` | Depth of the step in the history tree. |
| `action` | `int` | Raw action code of the step (-1 when there is none). |
| `operation` | `GenericSolidObject.Operation \| None` | Solid operation of the step; `None` when it is not a Boolean operation. |
| `hasHistory` | `bool` | Whether the step has a history of its own. |

#### GenericSolidObject.Operation

> **Full name:** `api.GenericSolidObject.Operation` · **Kind:** `IntEnum`

Solid Boolean operation.

| Member | Value | Description |
|---|---|---|
| `Union` | `0` |  |
| `Intersection` | `1` |  |
| `Difference` | `2` |  |

### ShellObject

> **Full name:** `api.ShellObject` · **Inherits:** [`GenericSolidObject`](#genericsolidobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Shell solid: a CSG offset node (Shell Solid tool, VectorScript CreateShell). It has exactly one operand (the source surface or solid) and remembers the thickness and the selected faces as history. A NURBS surface is thickened; a solid is hollowed with the selected faces removed (open faces). The stored thickness is signed: negative values offset to the opposite side ("Offset Side" in the OIP). Inherited Boolean editing (SetOperation / SetOperand) does not apply to shell nodes.

**Constructors**

| Constructor | Description |
|---|---|
| `ShellObject(h: Handle)` | Refers to the existing shell solid `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | CSG node with the offset action, including a node whose last rebuild failed. |
| `Create(hSurface: Handle, thickness: float, keepOriginal: bool = True) -> ShellObject` *static* | `thickness` must be finite and non-zero; a negative value thickens to the opposite side. The result is inserted in place of the source, which becomes the shell's operand; with keepOriginal a copy of the source is used instead. On failure the inputs are unchanged. Records the shell and any source copy for Undo; joins an existing event. Do not register the returned shell again. A newly created source must be registered before this call. |
| `CreateFromSolid(hSolid: Handle, openFaceIndices: list[int], thickness: float, keepOriginal: bool = True) -> ShellObject` *static* | Hollows a solid; `openFaceIndices` are 0-based face indices (see GetFaceCount) removed from the shell. |
| `GetFaceCount(h: Handle) -> int \| None` *static* | Number of faces addressable by CreateFromSolid. |
| `Duplicate() -> ShellObject` | Duplicates the shell solid in the drawing and returns the copy. |
| `IsFailed() -> bool \| None` | True when the shell could not be built. |
| `GetThickness() -> float \| None` | Thickness magnitude; the side is reported by IsReversed. |
| `SetThickness(thickness: float) -> bool` | Positive magnitude, keeping the side. A failed rebuild restores the previous value. |
| `IsReversed() -> bool \| None` | True when the shell is built on the reversed side of the surface. |
| `SetReversed(isReversed: bool) -> bool` | Turns *Reversed* on or off. |
| `GetSource() -> Handle` | The thickened surface or hollowed solid (the only operand). |
| `IsMonikerBased() -> bool \| None` | Faces are tracked by persistent monikers when the source supports them, otherwise by index. |
| `GetSelectedFaceIndices() -> list[int]` | Returns the selected face indices. |
| `GetSelectedFaceMonikers() -> list[str]` | Returns the selected face monikers. |
| `ResolveSelectedFaceIndices() -> list[int] \| None` | Sorted, unique current 0-based source face indices, including selections stored as monikers. Unavailable if the source cannot be read or any selected face no longer resolves. |

Inherited: everything from [`GenericSolidObject`](#genericsolidobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### Polygon3DObject

> **Full name:** `api.Polygon3DObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Native 3D polygon (`ObjectType.Polygon3D`). Vertices are corner points in parent coordinates (world units); a 3D polygon has no arc/bezier vertices and no per-edge visibility. Indices are 0-based. A 3D polygon always keeps at least two vertices. Wrapping an existing polygon never changes it.

**Constructors**

| Constructor | Description |
|---|---|
| `Polygon3DObject(h: Handle)` | Refers to the existing 3D polygon `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(points: list[Point3D], closed: bool = True) -> Polygon3DObject` *static* | Requires 2..32767 finite points; the new polygon is inserted in the active layer. |

*Corner points only*

| Method | Description |
|---|---|
| `Create(polygon: Math.Polygon2D, z: float = 0.0) -> Polygon3DObject` *static* | Arc/bezier vertex data of the 2D polygon is ignored. |
| `Create(rect: Math.Rect2D, z: float = 0.0) -> Polygon3DObject` *static* | Arc/bezier vertex data of the 2D polygon is ignored. |
| `ConvertToGroup(hObject: Handle, keepOriginal: bool = True) -> Handle` *static* | Converts any 2D/3D object to 3D polygons (ConvertTo3DPolygons). Returns the group that holds the polygons, or null. The original is deleted unless keepOriginal is `True`. |
| `GetPolygonsIn(hContainer: Handle) -> list[Handle]` *static* | 3D polygons inside a container (group, layer, symbol, ...), including those in nested groups. |
| `Duplicate() -> Polygon3DObject` | Duplicates the 3D polygon in the drawing and returns the copy. |

*Vertices*

| Method | Description |
|---|---|
| `GetVertexCount() -> int` | Number of vertex items. |
| `GetVertex(index: int) -> Point3D \| None` | Returns the vertex at `index`. |
| `SetVertex(index: int, point: Point3D) -> bool` | Sets the vertex at `index`. |
| `GetVertices() -> list[Point3D]` | Returns the vertices. |
| `SetVertices(points: list[Point3D]) -> bool` | Sets the vertices (2..32767 points). |
| `AddVertex(point: Point3D) -> bool` | Appends the vertex `point`. |
| `AddVertices(points: list[Point3D], reverse: bool = False) -> bool` | Appends the vertices `points` (in reverse order when `reverse` is `True`). |
| `InsertVertex(beforeIndex: int, point: Point3D) -> bool` | Inserts `point` before the vertex `beforeIndex` (0 .. vertex count). |
| `DeleteVertex(index: int) -> bool` | Deletes the vertex at `index`; fails when only two vertices remain. |
| `IsClosed() -> bool` | True when the polygon is closed. |
| `SetClosed(closed: bool) -> bool` | Turns *Closed* on or off. |

*Shape*

| Method | Description |
|---|---|
| `GetPolygon2D() -> Math.Polygon2D \| None` | Returns the polygon 2D (XY projection, keeps the closed flag). |
| `IsClockwise() -> bool \| None` | True when the XY projection runs clockwise (sign of the Newell normal z). |
| `Reverse() -> bool` | Reverses the vertex order (flips the polygon normal). |
| `IsPlanar(tolerance: float = 1e-09) -> bool \| None` | True when all vertices lie in one plane within `tolerance`. |
| `IsValidPolygon(tolerance: float = 1e-09) -> bool \| None` | True when the polygon has enough distinct vertices to be valid (within `tolerance`). |
| `GetNormal() -> Point3D \| None` | Returns the normal (Newell normal, unit length). |
| `GetPlane() -> Polygon3DObject.Plane \| None` | Returns the plane. |
| `GetPlaneTransform() -> ExtrudeObject.Transform \| None` | Returns the plane transform (local frame with W along the polygon normal). |
| `GetVertexCentroid() -> Point3D \| None` | Measurements (world units); 3D bounds, center (Get3DCntr) and size (Get3DInfo) come from PrimitiveObject (average of the vertices). |
| `GetLength() -> float \| None` | Returns the length (includes the closing edge when closed). |
| `GetSegmentLength(segmentIndex: int) -> float \| None` | Returns the segment length at `segmentIndex`. |
| `GetArea() -> float \| None` | Returns the area (planar area of a closed polygon (Newell)). |
| `GetPointAtDistance(distance: float) -> Point3D \| None` | Returns the point at distance for `distance` (distance along the path). |
| `GetClosestPoint(point: Point3D) -> Polygon3DObject.ClosestPoint \| None` | Returns the closest point for `point`. |
| `GetDistanceTo(point: Point3D) -> float \| None` | Returns the distance to for `point`. |
| `GetDistanceToPlane(point: Point3D) -> float \| None` | Returns the distance to plane for `point` (signed). |
| `IntersectLine(start: Point3D, direction: Point3D) -> Point3D \| None` | Intersection of the line through `start` along `direction` with the plane of the polygon. |

*Edits*

| Method | Description |
|---|---|
| `Cleanup(tolerance: float = 1e-09) -> bool` | Removes duplicate and collinear vertices (within `tolerance`). |
| `CleanupFeaturePreserving(collinearTolerance: float, closenessTolerance: float) -> bool` | Removes collinear (`collinearTolerance`) and nearly coincident (`closenessTolerance`) vertices while keeping the shape. |
| `Simplify(maxDeviation: float) -> bool` | Simplifies the polygon with the Douglas-Peucker algorithm, deviating at most `maxDeviation`. |
| `Segment(maxSegmentLength: float) -> bool` | Subdivides the edges longer than `maxSegmentLength`. |
| `Transform(transform: ExtrudeObject.Transform) -> bool` | Transforms the polygon by `transform` (maps local coordinates to the parent space). |
| `Move3D(offset: Point3D) -> bool` | Moves the polygon by `offset` in 3D. |
| `Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool` | Rotates the polygon by `angleDegrees` (degrees) around the axis `axis` through `center`. |
| `Scale3D(center: Point3D, factors: Point3D) -> bool` | Scales the polygon by `factors` (per axis) relative to `center`. |

*Generic solid integration*

| Method | Description |
|---|---|
| `IsValidSolidOperand() -> bool` | Only closed polygons with at least three vertices are valid operands. keepOriginal = `False` moves this polygon into the new solid's history. |
| `ToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | Converts the polygon into a generic solid. Only closed polygons with at least three vertices are valid operands. keepOriginal = `False` moves this polygon into the new solid's history. |
| `Union(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Union with the solid `hTool`, as a generic solid. Only closed polygons with at least three vertices are valid operands. keepOriginal = `False` moves this polygon into the new solid's history. |
| `Subtract(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Subtracts the solid `hTool`, giving a generic solid. Only closed polygons with at least three vertices are valid operands. keepOriginal = `False` moves this polygon into the new solid's history. |
| `Intersect(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Intersection with the solid `hTool`, as a generic solid. Only closed polygons with at least three vertices are valid operands. keepOriginal = `False` moves this polygon into the new solid's history. |
| `ConvertToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | History-free generic solid (as ConvertToGenericSolid); keepOriginal = `False` deletes this polygon. |
| `ToPlanarSolid(thickness: float) -> GenericSolidObject` | Planar solid with the polygon's vertices as its face, extruded by thickness along its normal. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### Polygon3DObject.Plane

> **Full name:** `api.Polygon3DObject.Plane` · **Inherits:** `api.Object`

Plane through the vertex centroid; normal is a unit vector following the vertex order (right-hand rule) and d satisfies normal . p + d = 0 for points p on the plane.

**Constructors**

| Constructor | Description |
|---|---|
| `Plane()` | Default value (fields at their defaults). |
| `Plane(point, normal, d)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `point` | `Point3D` | Vertex centroid (a point of the plane). |
| `normal` | `Point3D` | Unit normal following the vertex order (right-hand rule). |
| `d` | `float` | Plane constant: `normal . p + d = 0` for points `p` of the plane. |

#### Polygon3DObject.ClosestPoint

> **Full name:** `api.Polygon3DObject.ClosestPoint` · **Inherits:** `api.Object`

Closest point on the polygon path, its distance, edge index and path distance from the first vertex.

**Constructors**

| Constructor | Description |
|---|---|
| `ClosestPoint()` | Default value (fields at their defaults). |
| `ClosestPoint(point, distance, segmentIndex, distanceAlong)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `point` | `Point3D` | Closest point. |
| `distance` | `float` | Distance to the closest point. |
| `segmentIndex` | `int` | Edge from vertex segmentIndex to the next vertex. |
| `distanceAlong` | `float` | Path length from the first vertex to point. |

### MeshObject

> **Full name:** `api.MeshObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Native mesh (`ObjectType.Mesh`): a shared vertex list plus polygonal faces that index into it. Vertex and face indices are 0-based. Optional per-vertex normals and UV coordinates and texture parts (face groups with their own texture) are supported. Meshes are valid generic solid operands: ToGenericSolid/Union/Subtract/Intersect build solids from meshes, and `GenericSolidObject.ConvertToMesh` turns a solid back into a mesh. Rewriting the face list (SetFaces, SetGeometry, DeleteFace, FlipFaces) keeps face parts but resets per-face attributes (class, fill, pen) to the mesh defaults.

**Constructors**

| Constructor | Description |
|---|---|
| `MeshObject(h: Handle)` | Refers to the existing mesh `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `GetOverallPart() -> int` *static* | Returns the overall part. |
| `Create(vertices: list[Point3D], faces: list[list[int]]) -> MeshObject` *static* | Faces need at least three valid vertex indices. The mesh is inserted in the active layer. |
| `Create(vertices: list[Point3D], faces: list[MeshObject.Face]) -> MeshObject` *static* | Faces need at least three valid vertex indices. The mesh is inserted in the active layer. |
| `CreateFromPolygons(polygons: list[list[Point3D]]) -> MeshObject` *static* | Each polygon becomes a face; coincident points are welded into shared vertices. |
| `CreateFromGroup(hGroup: Handle) -> MeshObject` *static* | Converts a group of 3D polygons in place (nested groups are flattened first). The group handle becomes the mesh handle. Fails without changes when the group holds other objects. |
| `CreateFromObject(hObject: Handle, keepOriginal: bool = True) -> MeshObject` *static* | Meshes any 3D object (solids, extrudes, generic solids, ...) through 3D polygons. The mesh is placed right after the original, which is deleted unless keepOriginal is `True`. An operand inside a generic solid history can be converted only with keepOriginal = `True`. |
| `GetMeshesIn(hContainer: Handle) -> list[Handle]` *static* | Meshes that are direct members of a container (group, layer, symbol, ...). |
| `GetMeshOperands(hSolid: Handle) -> list[Handle]` *static* | Meshes used anywhere in the history of a generic solid. |
| `Duplicate() -> MeshObject` | Duplicates the mesh in the drawing and returns the copy. |

*Vertices*

| Method | Description |
|---|---|
| `GetVertexCount() -> int` | Number of vertex items. |
| `GetVertex(index: int) -> Point3D \| None` | Returns the vertex at `index`. |
| `SetVertex(index: int, point: Point3D) -> bool` | Sets the vertex at `index`. |
| `GetVertices() -> list[Point3D]` | Returns the vertices. |
| `SetVertices(points: list[Point3D]) -> bool` | Sets the vertices (same vertex count). |
| `HasNormals() -> bool` | Per-vertex normals and UV coordinates (one entry per vertex). |
| `GetNormals() -> list[Point3D]` | Returns the normals (Per-vertex normals and UV coordinates (one entry per vertex)). |
| `SetNormals(normals: list[Point3D]) -> bool` | Sets the normals (Per-vertex normals and UV coordinates (one entry per vertex) normalized on write). |
| `ClearNormals() -> bool` | Removes the per-vertex normals. |
| `HasUVs() -> bool` | True when the mesh has per-vertex UV coordinates. |
| `GetUVs() -> list[Math.Point2D]` | Returns the UVs. |
| `SetUVs(uvs: list[Math.Point2D]) -> bool` | Sets the UVs. |
| `ClearUVs() -> bool` | Removes the per-vertex UV coordinates (also resets all faces to the overall part). |

*Faces*

| Method | Description |
|---|---|
| `GetFaceCount() -> int` | Number of face items. |
| `GetFace(index: int) -> MeshObject.Face \| None` | Returns the face at `index`. |
| `GetFaces() -> list[MeshObject.Face]` | Returns the faces. |
| `SetFaces(faces: list[MeshObject.Face]) -> bool` | Sets the faces. |
| `AddFace(vertexIndices: list[int], part: int = 0) -> bool` | Adds a face through the vertices `vertexIndices` in the texture part `part` (keeps the face attributes). |
| `DeleteFace(index: int) -> bool` | Deletes the face at `index`. |
| `SetGeometry(vertices: list[Point3D], faces: list[MeshObject.Face]) -> bool` | Replaces vertices and faces at once (vertex count may change). Normals and UVs are cleared when the vertex count changes. |
| `SetFacePart(faceIndex: int, part: int) -> bool` | Sets the face part at `faceIndex`. |
| `GetFaceNormal(faceIndex: int) -> Point3D \| None` | Returns the face normal at `faceIndex` (Newell normal, unit length). |
| `GetFaceArea(faceIndex: int) -> float \| None` | Returns the face area at `faceIndex`. |
| `GetFaceCenter(faceIndex: int) -> Point3D \| None` | Returns the face center at `faceIndex` (average of the face vertices). |

*Texture parts*

| Method | Description |
|---|---|
| `GetParts() -> list[MeshObject.Part]` | Returns the parts. |
| `AddPart(texture: int = 0) -> int \| None` | Adds a texture part (with the texture index `texture`, 0 = none); returns the index of the new part. |
| `GetPartTexture(part: int) -> int \| None` | Returns the part texture for `part`. |
| `SetPartTexture(part: int, texture: int) -> bool` | Sets the part texture. |

*Smoothing*

| Method | Description |
|---|---|
| `GetSmoothing() -> MeshObject.Smoothing \| None` | Returns the smoothing. |
| `SetSmoothing(smoothing: MeshObject.Smoothing) -> bool` | Sets the smoothing. |
| `GetCreaseAngle() -> float \| None` | Returns the crease angle. |
| `SetCreaseAngle(degrees: float) -> bool` | Sets the crease angle (0..180, switches to CustomCrease). |

*Topology*

| Method | Description |
|---|---|
| `IsClosed() -> bool` | True when the mesh is closed (watertight: each edge is shared by two opposite faces). |
| `FlipFaces() -> bool` | Reverses the winding and the vertex normals. |

*Operations*

| Method | Description |
|---|---|
| `Simplify(qualityPercent: float) -> bool` | Simplifies the mesh in place to `qualityPercent` of its detail (0 < quality < 100). |
| `Repair() -> list[Handle]` | Repaired meshes are inserted after this mesh; this mesh is left unchanged. |
| `ConvertToGroup() -> Handle` | Converts this mesh in place to a group of 3D polygons; this object becomes invalid. |
| `ToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | Generic solid integration. keepOriginal = `False` moves this mesh into the new solid's history, so the object then refers to the history operand. |
| `Union(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Union with the solid `hTool`, as a generic solid. Generic solid integration. keepOriginal = `False` moves this mesh into the new solid's history, so the object then refers to the history operand. |
| `Subtract(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Subtracts the solid `hTool`, giving a generic solid. Generic solid integration. keepOriginal = `False` moves this mesh into the new solid's history, so the object then refers to the history operand. |
| `Intersect(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Intersection with the solid `hTool`, as a generic solid. Generic solid integration. keepOriginal = `False` moves this mesh into the new solid's history, so the object then refers to the history operand. |
| `ConvertToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | History-free generic solid (as ConvertToGenericSolid); keepOriginal = `False` deletes this mesh. |
| `Transform(transform: ExtrudeObject.Transform) -> bool` | Transforms (vertex normals follow; mirroring also reverses the face winding) (maps local coordinates to the parent space). |
| `Move3D(offset: Point3D) -> bool` | Moves the mesh by `offset`. Transforms (vertex normals follow; mirroring also reverses the face winding). |
| `Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool` | Rotates the mesh by `angleDegrees` (degrees) around the axis `axis` through `center`. Transforms (vertex normals follow; mirroring also reverses the face winding). |
| `Scale3D(center: Point3D, factors: Point3D) -> bool` | Scales the mesh by `factors` (per axis) relative to `center`. Transforms (vertex normals follow; mirroring also reverses the face winding). |
| `GetSurfaceArea() -> float \| None` | Measurements (world units); 3D bounds, center and size come from PrimitiveObject. |
| `GetVolume() -> float \| None` | Returns the volume (meaningful for closed meshes). |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### MeshObject.Face

> **Full name:** `api.MeshObject.Face` · **Inherits:** `api.Object`

Part 0 means the overall (untextured) part, see `GetOverallPart()`.

**Constructors**

| Constructor | Description |
|---|---|
| `Face()` | Default value (fields at their defaults). |
| `Face(vertexIndices, part)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `vertexIndices` | `list[int]` | Indices of the face vertices. |
| `part` | `int` | Index of the texture part of the face. |

#### MeshObject.Part

> **Full name:** `api.MeshObject.Part` · **Inherits:** `api.Object`

Texture part: id, texture reference (0 = untextured) and number of faces using it.

**Constructors**

| Constructor | Description |
|---|---|
| `Part()` | Default value (fields at their defaults). |
| `Part(id, texture, faceCount)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `id` | `int` | Part ID. |
| `texture` | `int` | Texture resource reference, 0 when untextured. |
| `faceCount` | `int` | Number of faces in the part. |

#### MeshObject.Smoothing

> **Full name:** `api.MeshObject.Smoothing` · **Kind:** `IntEnum`

How the mesh is smoothed when it is rendered.

| Member | Value | Description |
|---|---|---|
| `None_` | `0` |  |
| `DocumentPreference` | `1` |  |
| `CustomCrease` | `2` |  |
| `Imported` | `3` |  |

### SolidPrimitiveObject

> **Full name:** `api.SolidPrimitiveObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Common base of the native parametric solid primitives (`ObjectType.Solid`): spheres, hemispheres and cones. Each primitive is stored as a local frame (origin + orthonormal I/J/K axes) plus its parameters:

- sphere / hemisphere: origin = center, K = up axis (the hemisphere dome points along +K)
- cone: origin = base center, K = axis from the base towards the tip

Primitives are valid generic solid operands. After editing a primitive that sits in the history of a generic solid, call `GenericSolidObject.Rebuild()` on the outermost solid.

**Constructors**

| Constructor | Description |
|---|---|
| `SolidPrimitiveObject(h: Handle)` | Refers to the existing solid primitive `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `GetKindOf(h: Handle) -> SolidPrimitiveObject.Kind \| None` *static* | Returns the kind of for `h`. |
| `GetPrimitivesIn(hContainer: Handle) -> list[Handle]` *static* | Sphere, hemisphere and cone primitives that are direct members of a container (group, layer, ...) |
| `GetPrimitiveOperands(hSolid: Handle) -> list[Handle]` *static* | Primitives used anywhere in the history of a generic solid. |
| `GetKind() -> SolidPrimitiveObject.Kind \| None` | Returns the kind. |

*Local frame*

| Method | Description |
|---|---|
| `GetFrame() -> ExtrudeObject.Transform \| None` | Origin, uAxis = I, vAxis = J, wAxis = K (unit vectors). |
| `SetFrame(origin: Point3D, iAxis: Point3D, jAxis: Point3D) -> bool` | Moves the origin and re-orients the primitive. iAxis and jAxis are orthonormalized, K = I x J. |
| `GetAxis() -> Point3D \| None` | Returns the axis. |
| `SetAxis(axis: Point3D) -> bool` | Turns the primitive around its origin so that K points along `axis` (shortest rotation). |
| `Move3D(offset: Point3D) -> bool` | Rigid and uniform transforms (the primitive keeps its kind). |
| `Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool` | Rotates by `angleDegrees` (degrees) around the axis `axis` through `center`. Rigid and uniform transforms (the primitive keeps its kind). |
| `Scale3D(center: Point3D, factor: float) -> bool` | Scales uniformly by `factor` (> 0) relative to `center`. Rigid and uniform transforms (the primitive keeps its kind). |
| `GetVolume() -> float \| None` | Measurements (world units). |
| `GetSurfaceArea() -> float \| None` | Returns the surface area. |
| `ToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | Generic solid integration. keepOriginal = `False` moves this primitive into the new solid's history, so the object then refers to the history operand. |
| `Union(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Union with the solid `hTool`, as a generic solid. Generic solid integration. keepOriginal = `False` moves this primitive into the new solid's history, so the object then refers to the history operand. |
| `Subtract(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Subtracts the solid `hTool`, giving a generic solid. Generic solid integration. keepOriginal = `False` moves this primitive into the new solid's history, so the object then refers to the history operand. |
| `Intersect(hTool: Handle, keepOriginal: bool = True) -> GenericSolidObject` | Intersection with the solid `hTool`, as a generic solid. Generic solid integration. keepOriginal = `False` moves this primitive into the new solid's history, so the object then refers to the history operand. |
| `ConvertToGenericSolid(keepOriginal: bool = True) -> GenericSolidObject` | History-free generic solid (as ConvertToGenericSolid); keepOriginal = `False` deletes this primitive. |
| `ToMesh(keepOriginal: bool = True) -> MeshObject` | Tessellates the primitive into a mesh placed right after it. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### SolidPrimitiveObject.Kind

> **Full name:** `api.SolidPrimitiveObject.Kind` · **Kind:** `IntEnum`

Kind of a solid primitive.

| Member | Value | Description |
|---|---|---|
| `Sphere` | `0` |  |
| `Hemisphere` | `1` |  |
| `Cone` | `2` |  |

### SphereObject

> **Full name:** `api.SphereObject` · **Inherits:** [`SolidPrimitiveObject`](#solidprimitiveobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Native sphere solid. Radii are measured along the local I/J/K axes, so unequal radii give an ellipsoid.

**Constructors**

| Constructor | Description |
|---|---|
| `SphereObject(h: Handle)` | Refers to the existing sphere `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(center: Point3D, radius: float) -> SphereObject` *static* | Creates a sphere with the given `center` and `radius`. |
| `CreateEllipsoid(center: Point3D, radii: Point3D) -> SphereObject` *static* | Axis aligned ellipsoid; radii = (I radius, J radius, K radius). |
| `Duplicate() -> SphereObject` | Duplicates the sphere in the drawing and returns the copy. |
| `GetCenter() -> Point3D \| None` | Returns the center. |
| `SetCenter(center: Point3D) -> bool` | Sets the center. |
| `GetRadius() -> float \| None` | GetRadius returns the I radius; SetRadius sets all three radii. |
| `SetRadius(radius: float) -> bool` | Sets the radius. GetRadius returns the I radius; SetRadius sets all three radii. |
| `GetRadii() -> Point3D \| None` | Returns the radii. |
| `SetRadii(radii: Point3D) -> bool` | Sets the radii. |
| `IsEllipsoid() -> bool` | True when the sphere is scaled unevenly (an ellipsoid). |

Inherited: everything from [`SolidPrimitiveObject`](#solidprimitiveobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### HemisphereObject

> **Full name:** `api.HemisphereObject` · **Inherits:** [`SphereObject`](#sphereobject) → [`SolidPrimitiveObject`](#solidprimitiveobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Native hemisphere solid: the dome points from the center along the local K axis

**Constructors**

| Constructor | Description |
|---|---|
| `HemisphereObject(h: Handle)` | Refers to the existing hemisphere `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(center: Point3D, topPoint: Point3D) -> HemisphereObject` *static* | Creates a hemisphere around `center` whose top (pole) is at `topPoint`. |
| `Create(center: Point3D, radius: float) -> HemisphereObject` *static* | Creates an upright hemisphere with the given `center` and `radius`. |
| `Duplicate() -> HemisphereObject` | Duplicates the hemisphere in the drawing and returns the copy. |
| `GetTopPoint() -> Point3D \| None` | Center + K * K radius. |
| `SetTopPoint(topPoint: Point3D) -> bool` | Points the dome at topPoint and sets a uniform radius = \|topPoint - center\|. |

Inherited: everything from [`SphereObject`](#sphereobject), [`SolidPrimitiveObject`](#solidprimitiveobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### ConeObject

> **Full name:** `api.ConeObject` · **Inherits:** [`SolidPrimitiveObject`](#solidprimitiveobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Native cone solid. The base is an ellipse in the local I/J plane around the base center (frame origin); the tip is stored in object space, so moving the base center moves the whole cone. A right cone has its tip on the local K axis; an oblique cone has its tip anywhere above or below the base plane.

**Constructors**

| Constructor | Description |
|---|---|
| `ConeObject(h: Handle)` | Refers to the existing cone `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(baseCenter: Point3D, tipPoint: Point3D, radius: float) -> ConeObject` *static* | Creates a cone with the base circle of `radius` around `baseCenter` and the tip at `tipPoint`. |
| `Create(baseCenter: Point3D, radius: float, height: float) -> ConeObject` *static* | Creates a cone with the base circle of `radius` around `baseCenter` and the tip at `tipPoint`. |
| `Duplicate() -> ConeObject` | Duplicates the cone in the drawing and returns the copy. |
| `GetBaseCenter() -> Point3D \| None` | Returns the base center. |
| `SetBaseCenter(baseCenter: Point3D) -> bool` | Sets the base center. |
| `GetTipPoint() -> Point3D \| None` | Tip in world coordinates. keepRight = `True` re-orients the cone so that it stays a right cone; `False` keeps the base plane and makes the cone oblique if needed. |
| `SetTipPoint(tipPoint: Point3D, keepRight: bool = True) -> bool` | Sets the tip point. Tip in world coordinates. keepRight = `True` re-orients the cone so that it stays a right cone; `False` keeps the base plane and makes the cone oblique if needed. |
| `GetLocalTipPoint() -> Point3D \| None` | Tip in the local frame (I, J, K). |
| `SetLocalTipPoint(localTipPoint: Point3D) -> bool` | Sets the local tip point (Tip in the local frame (I, J, K)). |
| `IsRightCone() -> bool` | True when the tip lies on the axis through the base center. |
| `GetHeight() -> float \| None` | Distance from the base plane to the tip. SetHeight makes the cone a right cone; a negative height flips the cone to the other side of its base. |
| `SetHeight(height: float) -> bool` | Sets the height. Distance from the base plane to the tip. SetHeight makes the cone a right cone; a negative height flips the cone to the other side of its base. |
| `GetRadius() -> float \| None` | GetRadius returns the I radius; SetRadius sets both base radii. |
| `SetRadius(radius: float) -> bool` | Sets the radius. GetRadius returns the I radius; SetRadius sets both base radii. |
| `GetRadii() -> ConeObject.Radii \| None` | Returns the radii. |
| `SetRadii(radii: ConeObject.Radii) -> bool` | Sets the radii. |
| `IsElliptical() -> bool` | True when the base is an ellipse rather than a circle. |

Inherited: everything from [`SolidPrimitiveObject`](#solidprimitiveobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### ConeObject.Radii

> **Full name:** `api.ConeObject.Radii` · **Inherits:** `api.Object`

Base radii along the local I and J axes.

**Constructors**

| Constructor | Description |
|---|---|
| `Radii()` | Default value (fields at their defaults). |
| `Radii(i, j)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `i` | `float` | Base radius along the local I axis. |
| `j` | `float` | Base radius along the local J axis. |

### NurbsCurveObject

> **Full name:** `api.NurbsCurveObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Native piecewise NURBS curve. Piece, point and knot indices are 0-based; coordinates and distances use world units. An instance is a lightweight view of the drawing object.

**Constructors**

| Constructor | Description |
|---|---|
| `NurbsCurveObject(h: Handle)` | Refers to the existing NURBS curve `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(points: list[Point3D], degree: int, byControlPoints: bool = True) -> NurbsCurveObject` *static* | Creates a control-point or fit-point curve. The first point creates the native curve; remaining points are inserted using the native NURBS point operation. |
| `Duplicate() -> NurbsCurveObject` | Duplicates the NURBS curve in the drawing and returns the copy. |
| `GetPieceCount() -> int` | Number of piece items. |
| `GetPointCount(pieceIndex: int = 0) -> int` | Number of point items at `pieceIndex`. |
| `GetControlPointCount(pieceIndex: int = 0) -> int` | Number of control point items at `pieceIndex`. |
| `GetDegree(pieceIndex: int = 0) -> int \| None` | Returns the degree at `pieceIndex`. |
| `GetPoint(pieceIndex: int, pointIndex: int) -> Point3D \| None` | Returns the point for `pieceIndex`, `pointIndex`. |
| `SetPoint(pieceIndex: int, pointIndex: int, point: Point3D) -> bool` | Sets the point at `pieceIndex`. |
| `GetWeight(pieceIndex: int, controlPointIndex: int) -> float \| None` | Returns the weight for `pieceIndex`, `controlPointIndex`. |
| `SetWeight(pieceIndex: int, controlPointIndex: int, weight: float) -> bool` | Sets the weight at `pieceIndex`. |
| `GetKnotCount(pieceIndex: int = 0) -> int` | Number of knot items at `pieceIndex`. |
| `GetKnot(pieceIndex: int, knotIndex: int) -> float \| None` | Returns the knot for `pieceIndex`, `knotIndex`. |
| `SetKnot(pieceIndex: int, knotIndex: int, knot: float) -> bool` | Sets the knot at `pieceIndex`. |
| `Evaluate(pieceIndex: int, parameter: float) -> Point3D \| None` | Point of the piece `pieceIndex` at `parameter`. |
| `GetLength() -> float \| None` | Read-only analysis in world coordinates, not screen-projected distances. Parameters are native per-piece knot parameters, not normalized arc lengths. At a piece join, a distance lookup selects the preceding nonzero-length piece. |
| `GetLocationAtDistance(distance: float) -> NurbsCurveObject.Location \| None` | Returns the location at distance for `distance`. |
| `GetPointAtDistance(distance: float) -> Point3D \| None` | Returns the point at distance for `distance`. |
| `GetClosestPoint(point: Point3D) -> NurbsCurveObject.Location \| None` | Returns the closest point for `point`. |
| `GetDistanceTo(point: Point3D) -> float \| None` | Returns the distance to for `point`. |
| `GetTangent(pieceIndex: int, parameter: float) -> Point3D \| None` | Unit tangent and nonnegative curvature (inverse world units). At knots these use the right-hand derivative, except at the piece end where they use the left. A zero-speed point has no tangent or curvature and returns `None`. |
| `GetCurvature(pieceIndex: int, parameter: float) -> float \| None` | Returns the curvature for `pieceIndex`, `parameter`. |
| `DivideByCount(count: int, includeEnd: bool = True) -> list[Point3D] \| None` | Exactly count >= 2 equally arc-spaced points. includeEnd includes both endpoints, even on a closed curve; `False` omits the end/seam. No wrapping or clamping. Invalid/degenerate curves, nonfinite/out-of-range distances and failures return `None`. |
| `Extend(distance: float, atStart: bool, linear: bool) -> NurbsCurveObject` | Native operations insert their results into the active layer and leave this curve unchanged. |
| `Offset(distance: float) -> NurbsCurveObject` | Creates a curve offset by `distance`. Native operations insert their results into the active layer and leave this curve unchanged. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### NurbsCurveObject.Location

> **Full name:** `api.NurbsCurveObject.Location` · **Inherits:** `api.Object`

Curve point and native parameter on a zero-based piece; parameters are not arc lengths.

**Constructors**

| Constructor | Description |
|---|---|
| `Location()` | Default value (fields at their defaults). |
| `Location(point, pieceIndex, parameter)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `point` | `Point3D` | Point on the curve. |
| `pieceIndex` | `int` | Index of the curve piece. |
| `parameter` | `float` | Parameter on that piece. |

### NurbsSurfaceObject

> **Full name:** `api.NurbsSurfaceObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Native NURBS surface. Control-net coordinates and distances use world units; U/V point and knot indices are 0-based. An instance is a lightweight view of the drawing object.

**Constructors**

| Constructor | Description |
|---|---|
| `NurbsSurfaceObject(h: Handle)` | Refers to the existing NURBS surface `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(uPointCount: int, vPointCount: int, uDegree: int, vDegree: int) -> NurbsSurfaceObject` *static* | Creates a NURBS surface with `uPointCount` x `vPointCount` control points and the degrees `uDegree` / `vDegree`. |
| `CreateFromCurvesNetwork() -> bool` *static* | Uses the selected intersecting curves and consumes them; discard all source objects. Native failure cleanup can also delete inputs. Register undo before invoking. |
| `Duplicate() -> NurbsSurfaceObject` | Duplicates the NURBS surface in the drawing and returns the copy. |
| `GetUPointCount() -> int` | Number of U point items. |
| `GetVPointCount() -> int` | Number of V point items. |
| `GetUDegree() -> int \| None` | Returns the U degree. |
| `GetVDegree() -> int \| None` | Returns the V degree. |
| `GetPoint(uIndex: int, vIndex: int) -> Point3D \| None` | Returns the point for `uIndex`, `vIndex`. |
| `SetPoint(uIndex: int, vIndex: int, point: Point3D) -> bool` | Sets the point at `uIndex`. |
| `GetWeight(uIndex: int, vIndex: int) -> float \| None` | Returns the weight for `uIndex`, `vIndex`. |
| `SetWeight(uIndex: int, vIndex: int, weight: float) -> bool` | Sets the weight at `uIndex`. |
| `GetUKnotCount() -> int` | Number of U knot items. |
| `GetVKnotCount() -> int` | Number of V knot items. |
| `GetUKnot(knotIndex: int) -> float \| None` | Returns the U knot at `knotIndex`. |
| `GetVKnot(knotIndex: int) -> float \| None` | Returns the V knot at `knotIndex`. |
| `SetUKnot(knotIndex: int, knot: float) -> bool` | Sets the U knot at `knotIndex`. |
| `SetVKnot(knotIndex: int, knot: float) -> bool` | Sets the V knot at `knotIndex`. |
| `Evaluate(u: float, v: float) -> Point3D \| None` | Point of the surface at the parameters `u`, `v`. |
| `TrimByCurve(curve: NurbsCurveObject) -> bool` | TrimNurbsSurface attaches the curve to the surface as its trim boundary. |
| `Extend(distance: float, atStart: bool, linear: bool, uDirection: bool) -> NurbsSurfaceObject` | Native operations insert their results into the active layer and leave this surface unchanged. |
| `Offset(distance: float) -> NurbsSurfaceObject` | Creates a surface offset by `distance`. Native operations insert their results into the active layer and leave this surface unchanged. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

---

[Back to the index](README.md) · [Back to top](#objects3d--3d-objects)
