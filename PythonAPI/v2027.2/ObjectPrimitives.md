**English** • [Deutsch](../../PythonAPI.de/v2027.2/ObjectPrimitives.md) • [日本語](../../PythonAPI.ja/v2027.2/ObjectPrimitives.md)

# ObjectPrimitives — 2D primitive objects

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The 2D object classes. Every object class is a lightweight view of a drawing object: copying a Python object does not copy the drawing object, and deleting it does not delete the drawing object.

`PrimitiveObject` is the common base of **every** object class of the API (including the 3D, annotation, architectural, landscape, Spotlight and ConnectCAD objects): identity, hierarchy, state, attributes and transforms are documented once there. `ParametricObject` represents any plug-in object (use it when no specific class exists); `PolyObject` is the shared base of `PolygonObject` and `PolylineObject`; `RectangularObject` is the shared base of the rectangle classes.

Getters return `None` when a value is not available and setters return `False` on failure. Coordinates are world units, angles radians (counter-clockwise from the X axis).

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [PrimitiveObject](#primitiveobject)
    - [PrimitiveObject.Bounds3D](#primitiveobjectbounds3d)
  - [Locus2DObject](#locus2dobject)
  - [Line2DObject](#line2dobject)
  - [RectangularObject](#rectangularobject)
  - [RectangleObject](#rectangleobject)
  - [CornerDiameters](#cornerdiameters)
  - [RoundRectObject](#roundrectobject)
  - [ArcObject](#arcobject)
  - [CircleObject](#circleobject)
  - [PolyObject](#polyobject)
    - [PolyObject.BooleanOperation](#polyobjectbooleanoperation)
  - [PolygonObject](#polygonobject)
  - [PolylineObject](#polylineobject)
  - [GroupObject](#groupobject)
  - [ParametricObject](#parametricobject)
    - [ParametricObject.PluginKind](#parametricobjectpluginkind)
  - [TextObject](#textobject)
    - [TextObject.StyleRun](#textobjectstylerun)
    - [TextObject.TabStop](#textobjecttabstop)
    - [TextObject.HorizontalAlignment](#textobjecthorizontalalignment)
    - [TextObject.VerticalAlignment](#textobjectverticalalignment)
    - [TextObject.Spacing](#textobjectspacing)
    - [TextObject.TabAlignment](#textobjecttabalignment)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`PrimitiveObject`](#primitiveobject) | class |  | Common base of every object class of the API (2D primitives and, through their subclasses, 3D, annotation, architectural, landscape, Spotlight and ConnectCAD... |
| [`PrimitiveObject.Bounds3D`](#primitiveobjectbounds3d) | class (nested) |  | Axis-aligned 3D bounding box, in world units |
| [`Locus2DObject`](#locus2dobject) | class | [`PrimitiveObject`](#primitiveobject) | 2D locus (`ObjectType.Locus`): a reference point. |
| [`Line2DObject`](#line2dobject) | class | [`PrimitiveObject`](#primitiveobject) | 2D line (`ObjectType.Line`): a straight segment between two points. |
| [`RectangularObject`](#rectangularobject) | class | [`PrimitiveObject`](#primitiveobject) | Common base of the rectangle and the rounded rectangle classes. |
| [`RectangleObject`](#rectangleobject) | class | [`RectangularObject`](#rectangularobject) | Rectangle (`ObjectType.Box`), possibly rotated. |
| [`CornerDiameters`](#cornerdiameters) | class |  | Corner rounding of a rounded rectangle: the diameters of the corner ellipse along the width side (alongWidth) and along the height side (alongHeight). |
| [`RoundRectObject`](#roundrectobject) | class | [`RectangularObject`](#rectangularobject) | Rounded rectangle (`ObjectType.RoundedRectangle`), possibly rotated. |
| [`ArcObject`](#arcobject) | class | [`PrimitiveObject`](#primitiveobject) | Circular arc (`ObjectType.Arc`). |
| [`CircleObject`](#circleobject) | class | [`PrimitiveObject`](#primitiveobject) | Circle. |
| [`PolyObject`](#polyobject) | class | [`PrimitiveObject`](#primitiveobject) | Common base of the polygon and polyline classes. |
| [`PolyObject.BooleanOperation`](#polyobjectbooleanoperation) | IntEnum (nested) |  | Operation of the 2D Boolean functions |
| [`PolygonObject`](#polygonobject) | class | [`PolyObject`](#polyobject) | Polygon (`ObjectType.Polygon`, and freehand polygons `ObjectType.FreehandPolygon`): corner vertices only. |
| [`PolylineObject`](#polylineobject) | class | [`PolyObject`](#polyobject) | Polyline (`ObjectType.Polyline`): a poly shape whose vertices can be corner, bezier, cubic, arc or radius vertices. |
| [`GroupObject`](#groupobject) | class | [`PrimitiveObject`](#primitiveobject) | Group (`ObjectType.Group`): a container of other objects. |
| [`ParametricObject`](#parametricobject) | class | [`PrimitiveObject`](#primitiveobject) | Generic plug-in (parametric) object (`ObjectType.Parametric`) of any kind, defined by a script or by a compiled plug-in. |
| [`ParametricObject.PluginKind`](#parametricobjectpluginkind) | IntEnum (nested) |  | How the objects of a plug-in are placed: the object subtype that the plug-in declares. |
| [`TextObject`](#textobject) | class | [`PrimitiveObject`](#primitiveobject) | Text block (`ObjectType.Text`): formatted text placed at an origin point. |
| [`TextObject.StyleRun`](#textobjectstylerun) | class (nested) |  | Run of characters sharing the same formatting: start, length, font, size (world units and points), style flags, color, text style and tracking. |
| [`TextObject.TabStop`](#textobjecttabstop) | class (nested) |  | Tab stop: offset in world units from the left of the text and alignment. |
| [`TextObject.HorizontalAlignment`](#textobjecthorizontalalignment) | IntEnum (nested) |  | Horizontal alignment of a text block. |
| [`TextObject.VerticalAlignment`](#textobjectverticalalignment) | IntEnum (nested) |  | Vertical alignment of a text block relative to its origin. |
| [`TextObject.Spacing`](#textobjectspacing) | IntEnum (nested) |  | Line spacing of a text block; `Custom` uses the leading passed to `SetSpacing`. |
| [`TextObject.TabAlignment`](#textobjecttabalignment) | IntEnum (nested) |  | Alignment of the text at a tab stop. |

## Classes

### PrimitiveObject

> **Full name:** `api.PrimitiveObject` · **Inherits:** `api.Object`

Common base of every object class of the API (2D primitives and, through their subclasses, 3D, annotation, architectural, landscape, Spotlight and ConnectCAD objects). An instance is a lightweight view of a drawing object through its handle: copying it does not copy the drawing object, and destroying it does not delete the drawing object. To act on a raw handle:

- Test the type first: `if api.Line2DObject.Is(h): ...`
- Or use `api.Document.As(api.Line2DObject, h)`, which returns the typed object or `None`.
- `api.PrimitiveObject(h)` accepts any object handle.

Constructing a typed object from a handle of another type produces an invalid object (`IsValid()` is `False`); getters then return `None` and setters/operations return `False`. Conventions across the API:

- Coordinates are in world (model) units, angles in radians counter-clockwise from the X axis, strings are UTF-8.
- Value getters return `None` when a value is not available; setters and operations return a `bool`. Handle getters return a null handle and factories return invalid objects on failure.
- Transform operations (Move, Rotate, Scale, Mirror) may cause Vectorworks to replace the handle of the drawing object; the Python object transparently follows the new handle. Copies of it made before the transformation must be refreshed.

**Constructors**

| Constructor | Description |
|---|---|
| `PrimitiveObject(h: Handle)` | Refers to any drawing object `h` as a generic `PrimitiveObject`. |

**Methods**

*General*

| Method | Description |
|---|---|
| `GetHandle() -> Handle` | Handle of the drawing object. |
| `IsValid() -> bool` | True when this object refers to an existing drawing object. |
| `GetObjectType() -> ObjectType` | Returns the object type. |

*Identity*

| Method | Description |
|---|---|
| `GetName() -> str \| None` | Returns the name. |
| `SetName(name: str) -> bool` | Sets the name (fails when the name is used by another object). |
| `GetInternalIndex() -> int \| None` | Returns the internal index. |

*Hierarchy*

| Method | Description |
|---|---|
| `GetParent() -> Handle` | Returns the parent. Layer, group, symbol definition, ... |
| `GetNext() -> Handle` | Neighbours in the same list (VectorScript NextObj / PrevObj); null after the last / before the first object. |
| `GetPrevious() -> Handle` | Returns the previous. |
| `MoveToContainer(container: Handle) -> bool` | Moves the object into a container (layer, group, ...). Like the other operations it records no undo: to undo the move of an object that is in the drawing, call `Document.AddBeforeMoveObject` before it and `Document.AddAfterMoveObject` after it; register a new object that it inserts with `Document.AddAfterSwapObject`. It only relinks the object: it does not insert a door or window into a wall or take it out of one, and moving an object into a wall, a plug-in object, itself or one of its members, or out of one of these, can corrupt the document. Move only between layers, groups and symbol definitions. It does not check symbols either: moving into a symbol definition (or a group in one) an instance of that symbol, or of a symbol that holds an instance of it at any depth, nests the symbol inside itself, an infinite loop. |
| `GetFirstMember() -> Handle` | Members (VectorScript FInGroup / LInGroup walk). Every object type can be walked; objects that do not hold members (lines, rectangles, ...) return null / an empty list. |
| `GetLastMember() -> Handle` | Returns the last member. |
| `ForEachMember(callback: callable(Handle)) -> None` | Direct members only. The next member is fetched before `callback` runs, so the callback may delete or move the current one. |
| `GetMembers() -> list[Handle]` | Returns the members. |

*State*

| Method | Description |
|---|---|
| `IsVisible() -> bool \| None` | True when the object is visible, considering the visibility of its class and layer. |
| `SetVisible(visible: bool) -> bool` | Turns *Visible* on or off. |
| `IsLocked() -> bool \| None` | True when the object is locked. |
| `SetLocked(locked: bool) -> bool` | Turns *Locked* on or off. |
| `IsSelected() -> bool \| None` | True when the object is selected. |
| `SetSelected(selected: bool) -> bool` | Turns *Selected* on or off. |

*Class*

| Method | Description |
|---|---|
| `GetClass() -> ClassAttributes` | Returns the class. |
| `SetClass(theClass: ClassAttributes, useClassAttributes: bool = False) -> bool` | Assigns the object to `theClass`. When `useClassAttributes` is `True` every attribute of the object is set "by class". |
| `Attributes() -> ObjectAttributes` | Graphical attributes (pen, fill, markers, drop shadow, ...) |

*Measurement*

| Method | Description |
|---|---|
| `GetBounds() -> Math.Rect2D \| None` | Returns the bounds. |
| `GetArea() -> float \| None` | Returns the area. |
| `GetPerimeter() -> float \| None` | Returns the perimeter. |
| `GetBounds3D(layerRelative: bool = False) -> PrimitiveObject.Bounds3D \| None` | Returns 3D bounds with `minimum` and `maximum` corners (`Point3D`), available for every object (2D objects report a flat box at z = 0). `layerRelative` `False` returns true world Z; `True` subtracts the legacy layer elevation, matching the VectorScript Get3DCntr. `None` for an invalid object or an object without extents. |
| `GetCenter3D(layerRelative: bool = False) -> Point3D \| None` | Center of the 3D bounding box (VectorScript Get3DCntr with layerRelative = `True`). |
| `GetSize3D() -> Point3D \| None` | Extents of the 3D bounding box: x = width, y = height, z = depth (VectorScript Get3DInfo). |
| `Move(offset: Math.Point2D) -> bool` | Transformations (the object handle may change for some operations; the object follows the change). |
| `Move(dx: float, dy: float) -> bool` | Transformations (the object handle may change for some operations; the object follows the change). |
| `Rotate(angle: float, center: Math.Point2D) -> bool` | Rotates the object by `angle` radians around `center`. Transformations (the object handle may change for some operations; the object follows the change). |
| `Scale(scaleX: float, scaleY: float, center: Math.Point2D) -> bool` | Scales the object by `scaleX` / `scaleY` relative to `center`. Transformations (the object handle may change for some operations; the object follows the change). |
| `Mirror(axisStart: Math.Point2D, axisEnd: Math.Point2D) -> bool` | Mirrors the object across the axis from `axisStart` to `axisEnd`. Transformations (the object handle may change for some operations; the object follows the change). |

*Lifetime*

| Method | Description |
|---|---|
| `Reset() -> None` | Notifies the drawing engine that the object was modified externally. Call after batching multiple low-level edits or when the object is a plug-in object that needs to be regenerated. |
| `Delete(useUndo: bool = True) -> bool` | Deletes the object from the document; the object becomes invalid. |
| `ConvertToPolygon(keepOriginal: bool = False, resolution: int = 0) -> PolygonObject` | Conversion to a new polygon / polyline object. Without `keepOriginal` this object is replaced by the result and the object becomes invalid, even for in-place conversion. A failed conversion leaves the source object unchanged. `resolution` 0 uses the document conversion resolution. |
| `ConvertToPolyline(keepOriginal: bool = False) -> PolylineObject` | Converts the object to a polyline. Conversion to a new polygon / polyline object. Without `keepOriginal` this object is replaced by the result and the object becomes invalid, even for in-place conversion. A failed conversion leaves the source object unchanged. `resolution` 0 uses the document conversion resolution. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True when the object is valid (same as `IsValid()`). |
| `==` | `__eq__(o: PrimitiveObject) -> bool` | `a == b`: True when both objects refer to the same drawing object. |
| `!=` | `__ne__(o: PrimitiveObject) -> bool` | `a != b`: True when the objects refer to different drawing objects. |

#### PrimitiveObject.Bounds3D

> **Full name:** `api.PrimitiveObject.Bounds3D` · **Inherits:** `api.Object`

Axis-aligned 3D bounding box, in world units

**Constructors**

| Constructor | Description |
|---|---|
| `Bounds3D()` | Default value (fields at their defaults). |
| `Bounds3D(minimum, maximum)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `minimum` | `Point3D` | Corner with the smallest coordinates. |
| `maximum` | `Point3D` | Corner with the largest coordinates. |

### Locus2DObject

> **Full name:** `api.Locus2DObject` · **Inherits:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

2D locus (`ObjectType.Locus`): a reference point.

**Constructors**

| Constructor | Description |
|---|---|
| `Locus2DObject(h: Handle)` | Refers to the existing 2D locus `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D) -> Locus2DObject` *static* | Creates a locus in the active layer / current container. |
| `Duplicate() -> Locus2DObject` | Duplicates the 2D locus in the drawing and returns the copy. |
| `GetPosition() -> Math.Point2D \| None` | Returns the position. |
| `SetPosition(position: Math.Point2D) -> bool` | Sets the position. |
| `GetMasterSnapPoint() -> bool \| None` | Snap point behaviour when the locus is inside a symbol definition. |
| `SetMasterSnapPoint(isMasterSnap: bool) -> bool` | Turns *Master Snap Point* on or off (Snap point behaviour when the locus is inside a symbol definition). |
| `GetShowMasterSnapOutsideSnapBox() -> bool \| None` | Whether *Show Master Snap Outside Snap Box* is on. |
| `SetShowMasterSnapOutsideSnapBox(show: bool) -> bool` | Turns *Show Master Snap Outside Snap Box* on or off. |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | Distance from the locus to `pt`. |

Inherited: everything from [`PrimitiveObject`](#primitiveobject).

### Line2DObject

> **Full name:** `api.Line2DObject` · **Inherits:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

2D line (`ObjectType.Line`): a straight segment between two points.

**Constructors**

| Constructor | Description |
|---|---|
| `Line2DObject(h: Handle)` | Refers to the existing line `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(start: Math.Point2D, end: Math.Point2D) -> Line2DObject` *static* | Creates a line in the active layer / current container. |
| `Create(line: Math.Line2D) -> Line2DObject` *static* | Creates a line in the active layer / current container. |
| `Duplicate() -> Line2DObject` | Duplicates the line in the drawing and returns the copy. |

*Geometry*

| Method | Description |
|---|---|
| `GetLine() -> Math.Line2D \| None` | Returns the line. |
| `SetLine(line: Math.Line2D) -> bool` | Sets the line. |
| `SetLine(start: Math.Point2D, end: Math.Point2D) -> bool` | Sets the line. |
| `GetStartPoint() -> Math.Point2D \| None` | Returns the start point. |
| `SetStartPoint(pt: Math.Point2D) -> bool` | Sets the start point. |
| `GetEndPoint() -> Math.Point2D \| None` | Returns the end point. |
| `SetEndPoint(pt: Math.Point2D) -> bool` | Sets the end point. |

*Derived values*

| Method | Description |
|---|---|
| `GetLength() -> float \| None` | Returns the length. |
| `SetLength(length: float) -> bool` | Sets the length (keeps the start point and the direction). |
| `GetAngle() -> float \| None` | Returns the angle (direction from start to end). |
| `SetAngle(angle: float) -> bool` | Sets the angle (rotates around the start point, keeps the length). |
| `GetMidPoint() -> Math.Point2D \| None` | Returns the mid point. |
| `GetDirection() -> Math.Point2D \| None` | Returns the direction (unit vector from start to end). |

*Operations*

| Method | Description |
|---|---|
| `Reverse() -> bool` | Swaps the start and end points. |
| `Extend(atStart: float, atEnd: float) -> bool` | Extends the line by `atStart` before the start and `atEnd` after the end (negative values trim). |
| `OffsetParallel(distance: float) -> bool` | Moves the line parallel by `distance` (positive to the left of start -> end). |

*Queries*

| Method | Description |
|---|---|
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | Point of the line segment closest to `pt`. |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | Shortest distance from `pt` to the line segment. |
| `Intersect(other: Line2DObject) -> Math.Point2D \| None` | Intersection point with another line object (segments). |

Inherited: everything from [`PrimitiveObject`](#primitiveobject).

### RectangularObject

> **Full name:** `api.RectangularObject` · **Inherits:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Common base of the rectangle and the rounded rectangle classes. The geometry is a possibly rotated rectangle (`Math.RotatedRect2D`): a corner (origin), the direction of the width side, the width and the height.

**Constructors**

Not instantiable from Python: instances are returned by other API functions.

**Methods**

*General*

| Method | Description |
|---|---|
| `GetRect() -> Math.RotatedRect2D \| None` | Geometry. |
| `SetRect(rect: Math.RotatedRect2D) -> bool` | Sets the rect. |
| `GetOrigin() -> Math.Point2D \| None` | Returns the origin. |
| `GetDirection() -> Math.Point2D \| None` | Returns the direction (unit vector along the width side). |
| `GetWidth() -> float \| None` | Returns the width. |
| `SetWidth(width: float) -> bool` | Sets the width (keeps the origin corner). |
| `GetHeight() -> float \| None` | Returns the height. |
| `SetHeight(height: float) -> bool` | Sets the height (keeps the origin corner). |
| `SetSize(width: float, height: float, keepCenter: bool = True) -> bool` | Sets the size. |
| `GetCenter() -> Math.Point2D \| None` | Returns the center. |
| `SetCenter(center: Math.Point2D) -> bool` | Sets the center (moves the object). |
| `GetAngle() -> float \| None` | Returns the angle (angle of the width side). |
| `SetAngle(angle: float) -> bool` | Sets the angle (rotates around the center). |
| `IsAxisAligned() -> bool \| None` | True when the rectangle is not rotated (its sides are parallel to the axes). |
| `GetCorners() -> tuple[Math.Point2D * 4] \| None` | Corners, counter-clockwise starting at the origin (for positive width and height). |
| `SetBounds(bounds: Math.Rect2D) -> bool` | Sets an unrotated rectangle. |

*Queries*

| Method | Description |
|---|---|
| `Contains(pt: Math.Point2D) -> bool` | True when `pt` lies inside the rectangle (or on its border). |
| `GetPolygon() -> Math.Polygon2D \| None` | Returns the polygon (the four corners (corner rounding is ignored)). |

Inherited: everything from [`PrimitiveObject`](#primitiveobject).

### RectangleObject

> **Full name:** `api.RectangleObject` · **Inherits:** [`RectangularObject`](#rectangularobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

Rectangle (`ObjectType.Box`), possibly rotated.

**Constructors**

| Constructor | Description |
|---|---|
| `RectangleObject(h: Handle)` | Refers to the existing rectangle `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(rect: Math.RotatedRect2D) -> RectangleObject` *static* | Creates a rectangle in the active layer / current container. Width and height must not be zero. |
| `Create(bounds: Math.Rect2D) -> RectangleObject` *static* | Creates a rectangle in the active layer / current container. Width and height must not be zero. |
| `Create(center: Math.Point2D, width: float, height: float, angle: float = 0.0) -> RectangleObject` *static* | Creates a rectangle in the active layer / current container. Width and height must not be zero. |
| `Duplicate() -> RectangleObject` | Duplicates the rectangle in the drawing and returns the copy. |
| `IsSquare() -> bool \| None` | True when width and height are equal. |

Inherited: everything from [`RectangularObject`](#rectangularobject), [`PrimitiveObject`](#primitiveobject).

### CornerDiameters

> **Full name:** `api.CornerDiameters` · **Inherits:** `api.Object`

Corner rounding of a rounded rectangle: the diameters of the corner ellipse along the width side (alongWidth) and along the height side (alongHeight).

**Constructors**

| Constructor | Description |
|---|---|
| `CornerDiameters()` | Default value (fields at their defaults). |
| `CornerDiameters(alongWidth, alongHeight)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: CornerDiameters) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: CornerDiameters) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `alongWidth` | `float` | Corner diameter along the width side. |
| `alongHeight` | `float` | Corner diameter along the height side. |

### RoundRectObject

> **Full name:** `api.RoundRectObject` · **Inherits:** [`RectangularObject`](#rectangularobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

Rounded rectangle (`ObjectType.RoundedRectangle`), possibly rotated.

**Constructors**

| Constructor | Description |
|---|---|
| `RoundRectObject(h: Handle)` | Refers to the existing rounded rectangle `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(rect: Math.RotatedRect2D, corners: CornerDiameters, proportional: bool = False) -> RoundRectObject` *static* | Creates a rounded rectangle in the active layer / current container. Width and height must not be zero. `proportional` makes the corner diameters scale with the rectangle when it is resized interactively. |
| `Create(bounds: Math.Rect2D, corners: CornerDiameters, proportional: bool = False) -> RoundRectObject` *static* | Creates a rounded rectangle in the active layer / current container. Width and height must not be zero. `proportional` makes the corner diameters scale with the rectangle when it is resized interactively. |
| `Create(center: Math.Point2D, width: float, height: float, cornerRadius: float, angle: float = 0.0) -> RoundRectObject` *static* | Creates a rounded rectangle in the active layer / current container. Width and height must not be zero. `proportional` makes the corner diameters scale with the rectangle when it is resized interactively. |
| `Duplicate() -> RoundRectObject` | Duplicates the rounded rectangle in the drawing and returns the copy. |

*Corner rounding*

| Method | Description |
|---|---|
| `GetCornerDiameters() -> CornerDiameters \| None` | Returns the corner diameters. |
| `SetCornerDiameters(corners: CornerDiameters) -> bool` | Sets the corner diameters. |
| `GetCornerRadius() -> float \| None` | Radius of circular corners (the average when the corners are elliptical). |
| `SetCornerRadius(radius: float) -> bool` | Sets the corner radius (Radius of circular corners (the average when the corners are elliptical)). |
| `HasCircularCorners() -> bool \| None` | True when the corners are circular (equal corner width and height). |

Inherited: everything from [`RectangularObject`](#rectangularobject), [`PrimitiveObject`](#primitiveobject).

### ArcObject

> **Full name:** `api.ArcObject` · **Inherits:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Circular arc (`ObjectType.Arc`). Angles are in radians, counter-clockwise from the X axis. The document always stores arcs counter-clockwise: a negative sweep passed to a setter is normalized, so `GetSweepAngle()` is always positive. Full circles are arcs too; see also CircleObject.

**Constructors**

| Constructor | Description |
|---|---|
| `ArcObject(h: Handle)` | Refers to the existing arc `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents (any `ObjectType.Arc`, including full circles). |
| `Create(arc: Math.Arc2D) -> ArcObject` *static* | Creates an arc in the active layer / current container. Radius and sweep must not be zero. |
| `Create(center: Math.Point2D, radius: float, startAngle: float, sweepAngle: float) -> ArcObject` *static* | Creates an arc in the active layer / current container. Radius and sweep must not be zero. |
| `CreateThreePoints(start: Math.Point2D, onArc: Math.Point2D, end: Math.Point2D) -> ArcObject` *static* | Creates an arc through the three points `start`, `onArc` and `end` in the active layer / current container. |
| `Duplicate() -> ArcObject` | Duplicates the arc in the drawing and returns the copy. |

*Geometry*

| Method | Description |
|---|---|
| `GetArc() -> Math.Arc2D \| None` | Returns the arc. |
| `SetArc(arc: Math.Arc2D) -> bool` | Sets the arc. |
| `GetCenter() -> Math.Point2D \| None` | Returns the center. |
| `SetCenter(center: Math.Point2D) -> bool` | Sets the center. |
| `GetRadius() -> float \| None` | Returns the radius. |
| `SetRadius(radius: float) -> bool` | Sets the radius. |
| `GetStartAngle() -> float \| None` | Returns the start angle. |
| `SetStartAngle(angle: float) -> bool` | Sets the start angle (keeps the end angle). |
| `GetSweepAngle() -> float \| None` | Returns the sweep angle. |
| `SetSweepAngle(sweep: float) -> bool` | Sets the sweep angle (keeps the start angle). |
| `GetEndAngle() -> float \| None` | Returns the end angle. |
| `SetEndAngle(angle: float) -> bool` | Sets the end angle (keeps the start angle). |
| `SetAngles(startAngle: float, sweepAngle: float) -> bool` | Sets the angles. |
| `GetStartPoint() -> Math.Point2D \| None` | Returns the start point. |
| `GetEndPoint() -> Math.Point2D \| None` | Returns the end point. |
| `GetMidPoint() -> Math.Point2D \| None` | Returns the mid point. |
| `GetChord() -> Math.Line2D \| None` | Returns the chord. |

*Measures*

| Method | Description |
|---|---|
| `GetLength() -> float \| None` | Returns the length. |
| `GetChordLength() -> float \| None` | Returns the chord length. |
| `GetSagitta() -> float \| None` | Returns the sagitta. |
| `IsCircle() -> bool \| None` | True when the arc is a full circle. |

*Queries*

| Method | Description |
|---|---|
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | Point of the arc closest to `pt`. |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | Shortest distance from `pt` to the arc. |
| `Intersect(other: ArcObject) -> list[Math.Point2D]` | Intersection points with the arc `other`. |
| `Intersect(line: Math.Line2D) -> list[Math.Point2D]` | Intersection points with the line segment `line`. |

Inherited: everything from [`PrimitiveObject`](#primitiveobject).

### CircleObject

> **Full name:** `api.CircleObject` · **Inherits:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Circle. In the document a circle is an arc (`ObjectType.Arc`) with a full 360 degree sweep.

**Constructors**

| Constructor | Description |
|---|---|
| `CircleObject(h: Handle)` | Refers to the existing circle `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents (`ObjectType.Arc` with a full sweep). |
| `Create(circle: Math.Circle2D) -> CircleObject` *static* | Creates a circle in the active layer / current container. The radius must be positive. |
| `Create(center: Math.Point2D, radius: float) -> CircleObject` *static* | Creates a circle in the active layer / current container. The radius must be positive. |
| `CreateThreePoints(p1: Math.Point2D, p2: Math.Point2D, p3: Math.Point2D) -> CircleObject` *static* | Creates a circle through the three points `p1`, `p2` and `p3` in the active layer / current container. |
| `Duplicate() -> CircleObject` | Duplicates the circle in the drawing and returns the copy. |
| `AsArc() -> ArcObject` | The same object viewed as an `ArcObject` (a circle is an arc with a full sweep). |

*Geometry*

| Method | Description |
|---|---|
| `GetCircle() -> Math.Circle2D \| None` | Returns the circle. |
| `SetCircle(circle: Math.Circle2D) -> bool` | Sets the circle. |
| `GetCenter() -> Math.Point2D \| None` | Returns the center. |
| `SetCenter(center: Math.Point2D) -> bool` | Sets the center. |
| `GetRadius() -> float \| None` | Returns the radius. |
| `SetRadius(radius: float) -> bool` | Sets the radius. |
| `GetDiameter() -> float \| None` | Returns the diameter. |
| `SetDiameter(diameter: float) -> bool` | Sets the diameter. |

*Measures*

| Method | Description |
|---|---|
| `GetCircumference() -> float \| None` | Returns the circumference. |

*Queries*

| Method | Description |
|---|---|
| `Contains(pt: Math.Point2D) -> bool` | True when `pt` lies inside the circle (or on it). |
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | Point of the circle closest to `pt`. |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | Distance from `pt` to the circumference. |
| `PointAt(angle: float) -> Math.Point2D \| None` | Point of the circle at `angle` (radians, counter-clockwise from the X axis). |
| `Intersect(other: CircleObject) -> list[Math.Point2D]` | Intersection points with the circle `other`. |
| `Intersect(line: Math.Line2D) -> list[Math.Point2D]` | Intersection points with the line segment `line`. |
| `GetTangentPoints(from_: Math.Point2D) -> list[Math.Point2D]` | Returns the tangent points for `from_`. |

Inherited: everything from [`PrimitiveObject`](#primitiveobject).

### PolyObject

> **Full name:** `api.PolyObject` · **Inherits:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Common base of the polygon and polyline classes. Vertex indices are 0-based. The visibility of a vertex is the visibility of the edge that starts at it.

**Constructors**

Not instantiable from Python: instances are returned by other API functions.

**Methods**

*Vertices*

| Method | Description |
|---|---|
| `GetVertexCount() -> int` | Number of vertex items. |
| `GetVertex(index: int) -> Math.PolyVertex \| None` | Returns the vertex at `index`. |
| `GetVertexPoint(index: int) -> Math.Point2D \| None` | Returns the vertex point at `index`. |
| `SetVertexPoint(index: int, pt: Math.Point2D) -> bool` | Sets the vertex point at `index` (keeps the vertex type). |
| `GetVertexPoints() -> list[Math.Point2D]` | Returns the vertex points. |
| `DeleteVertex(index: int) -> bool` | Deletes the vertex at `index`. |
| `DeleteAllVertices() -> bool` | Deletes every vertex. |

*Edge visibility*

| Method | Description |
|---|---|
| `GetVertexVisible(index: int) -> bool \| None` | Whether *Vertex Visible* is on at `index`. |
| `SetVertexVisible(index: int, visible: bool) -> bool` | Sets the vertex visible at `index`. |
| `SetAllVerticesVisible(visible: bool) -> bool` | Turns *All Vertices Visible* on or off. |

*Closed / open*

| Method | Description |
|---|---|
| `IsClosed() -> bool \| None` | True when the shape is closed. |
| `SetClosed(closed: bool) -> bool` | Turns *Closed* on or off. |

*Whole geometry*

| Method | Description |
|---|---|
| `GetPolygon() -> Math.Polygon2D \| None` | Returns the polygon. |

*Orientation*

| Method | Description |
|---|---|
| `IsClockwise() -> bool \| None` | True when the vertices run clockwise. |
| `Reverse() -> bool` | Reverses the vertex order, keeps the edge visibility. |
| `SetClockwise(clockwise: bool) -> bool` | Turns *Clockwise* on or off. |
| `GetPolyArea() -> float \| None` | Measurement (the base GetArea / GetPerimeter give the same results through the generic object calls). |
| `GetPolyPerimeter() -> float \| None` | Returns the poly perimeter. |
| `GetCurveLength() -> float \| None` | Actual curved outer path in the object's local XY plane. These preserve the drawing, include invisible/closing edges, exclude holes, and do not use control-polygon lengths. See `Math.Polygon2D` for distance bounds, temporary NURBS parameters and endpoint policy. |
| `GetCurveLocationAtDistance(distance: float) -> Math.Polygon2D.CurveLocation \| None` | Returns the curve location at distance for `distance`. |
| `GetCurvePointAtDistance(distance: float) -> Math.Point2D \| None` | Returns the curve point at distance for `distance`. |
| `GetCurveTangentAtDistance(distance: float) -> Math.Point2D \| None` | Returns the curve tangent at distance for `distance`. |
| `GetCurveCurvatureAtDistance(distance: float) -> float \| None` | Returns the curve curvature at distance for `distance`. |
| `GetCurveClosestPoint(point: Math.Point2D) -> Math.Polygon2D.CurveLocation \| None` | Returns the curve closest point for `point`. |
| `GetCurveDistanceTo(point: Math.Point2D) -> float \| None` | Returns the curve distance to for `point`. |
| `DivideCurveByCount(count: int, includeEnd: bool = True) -> list[Math.Point2D] \| None` | Exactly `count` (>= 2) points evenly spaced along the actual curved path (`includeEnd=False` omits the final endpoint / seam); `None` on failure. Actual curved outer path in the object's local XY plane. These preserve the drawing, include invisible/closing edges, exclude holes, and do not use control-polygon lengths. See `Math.Polygon2D` for distance bounds, temporary NURBS parameters and endpoint policy. |
| `Contains(pt: Math.Point2D) -> bool` | Queries on the vertex polygon (curve vertices are treated as control points). |
| `ClosestPoint(pt: Math.Point2D) -> Math.Point2D \| None` | Point of the vertex polygon closest to `pt`. Queries on the vertex polygon (curve vertices are treated as control points). |
| `DistanceTo(pt: Math.Point2D) -> float \| None` | Distance from `pt` to the vertex polygon. Queries on the vertex polygon (curve vertices are treated as control points). |
| `GetCentroid() -> Math.Point2D \| None` | Returns the centroid. |
| `IsConvex() -> bool \| None` | True when the shape is convex. |
| `IsSelfIntersecting() -> bool \| None` | True when two non-adjacent edges intersect. |
| `Intersect(line: Math.Line2D) -> list[Math.Point2D]` | Intersection points of the vertex polygon with the segment `line`. Queries on the vertex polygon (curve vertices are treated as control points). |
| `BooleanUnion(other: PolyObject) -> list[Handle]` | Union with `other`: a list (possibly empty) of detached result handles with the attributes of this shape; both inputs stay unchanged. Insert the results with `PrimitiveObject(h).MoveToContainer(...)` or delete them. Raises `RuntimeError` for invalid input. |
| `BooleanIntersection(other: PolyObject) -> list[Handle]` | Intersection with `other`: a list (possibly empty) of detached result handles; both inputs stay unchanged. Raises `RuntimeError` for invalid input. |
| `BooleanDifference(other: PolyObject) -> list[Handle]` | This shape minus `other`: a list (possibly empty) of detached result handles; both inputs stay unchanged. Raises `RuntimeError` for invalid input. |
| `BooleanSymmetricDifference(other: PolyObject) -> list[Handle]` | Parts covered by exactly one of the two shapes: a list (possibly empty) of detached result handles; both inputs stay unchanged. Raises `RuntimeError` for invalid input. |
| `IsCombinableShape(h: Handle) -> bool` *static* | Whether CombineShapes accepts `h` as an operand (a 2D shape that the 2D Boolean operations handle). |
| `AreShapesInOnePlane(first: Handle, second: Handle) -> bool` *static* | Whether `first` and `second` are in one plane (the same planar ref ID), as CombineShapes requires. |
| `AlignShapePlanes(first: Handle, second: Handle) -> bool` *static* | Moves two coplanar shapes into one plane, the way Modify > Add / Clip / Intersect Surface do before they combine shapes. `True` when both shapes are in one plane afterwards (also when they already were); `False` when they are not coplanar, or a shape is null, not combinable or the same object. It changes the plane of the shapes it moves and records no undo: register both shapes (`Document.AddBothSwapObject`) before calling it. |
| `CombineShapes(operation: PolyObject.BooleanOperation, first: Handle, second: Handle) -> list[Handle]` *static* | Combines the 2D shapes `first` and `second` with `operation`: a list (possibly empty) of detached result handles with the attributes of `first`; the inputs stay unchanged. Raises `RuntimeError` for invalid input (a null or not combinable shape, the same object twice, shapes in different planes, an unknown operation). |

Inherited: everything from [`PrimitiveObject`](#primitiveobject).

#### PolyObject.BooleanOperation

> **Full name:** `api.PolyObject.BooleanOperation` · **Kind:** `IntEnum`

Operation of the 2D Boolean functions

| Member | Value | Description |
|---|---|---|
| `Union` | `0` |  |
| `Intersection` | `1` |  |
| `Difference` | `2` | `first` minus `second`. |
| `SymmetricDifference` | `3` | The parts covered by exactly one of the two shapes. |

### PolygonObject

> **Full name:** `api.PolygonObject` · **Inherits:** [`PolyObject`](#polyobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

Polygon (`ObjectType.Polygon`, and freehand polygons `ObjectType.FreehandPolygon`): corner vertices only. Use PolylineObject for curved vertices.

**Constructors**

| Constructor | Description |
|---|---|
| `PolygonObject(h: Handle)` | Refers to the existing polygon `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(poly: Math.Polygon2D) -> PolygonObject` *static* | Creates a polygon in the active layer / current container (at least two vertices). Curve vertices of `poly` are added as corners. |
| `Create(points: list[Math.Point2D], closed: bool = True) -> PolygonObject` *static* | Creates a polygon in the active layer / current container (at least two vertices). Curve vertices of `poly` are added as corners. |
| `Create(rect: Math.Rect2D) -> PolygonObject` *static* | Creates a polygon in the active layer / current container (at least two vertices). Curve vertices of `poly` are added as corners. |
| `CreateRegular(center: Math.Point2D, circumradius: float, sides: int, startAngle: float = 0.0) -> PolygonObject` *static* | Creates a regular polygon with `sides` corners on a circle of radius `circumradius` around `center` (first corner at `startAngle`) in the active layer / current container. |
| `Duplicate() -> PolygonObject` | Duplicates the polygon in the drawing and returns the copy. |
| `IsFreehand() -> bool \| None` | True when the polygon is a freehand polygon (`ObjectType.FreehandPolygon`). |

*Vertices*

| Method | Description |
|---|---|
| `AddVertex(pt: Math.Point2D, visible: bool = True) -> bool` | Appends a vertex at `pt`; `visible` controls whether the edge to the next vertex is drawn. |
| `InsertVertex(beforeIndex: int, pt: Math.Point2D, visible: bool = True) -> bool` | Inserts a vertex at `pt` before the vertex `beforeIndex`; `visible` controls the edge visibility. |
| `SetPolygon(poly: Math.Polygon2D) -> bool` | Replaces all vertices and the closed flag (curve vertices are set as corners). |
| `SetVertexPoints(points: list[Math.Point2D]) -> bool` | Sets the vertex points (keeps the closed flag). |

Inherited: everything from [`PolyObject`](#polyobject), [`PrimitiveObject`](#primitiveobject).

### PolylineObject

> **Full name:** `api.PolylineObject` · **Inherits:** [`PolyObject`](#polyobject) → [`PrimitiveObject`](#primitiveobject) → `api.Object`

Polyline (`ObjectType.Polyline`): a poly shape whose vertices can be corner, bezier, cubic, arc or radius vertices. Vertex points are control points; the curve passes through corner vertices only (and through arc vertices with a non-zero radius when it fits).

**Constructors**

| Constructor | Description |
|---|---|
| `PolylineObject(h: Handle)` | Refers to the existing polyline `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(poly: Math.Polygon2D) -> PolylineObject` *static* | Creates a polyline in the active layer / current container (at least two vertices). The result is always a polyline, even when all vertices are corners. |
| `CreateCircle(center: Math.Point2D, radius: float) -> PolylineObject` *static* | Closed polyline of four radius vertices that forms a circle. |
| `CreateFilletedRect(rect: Math.Rect2D, cornerRadius: float) -> PolylineObject` *static* | Closed polyline of a rectangle with filleted corners. |
| `Duplicate() -> PolylineObject` | Duplicates the polyline in the drawing and returns the copy. |

*Typed vertices*

| Method | Description |
|---|---|
| `AddVertex(vertex: Math.PolyVertex) -> bool` | Appends the vertex `vertex` (point, vertex type, arc radius and edge visibility). |
| `AddVertex(pt: Math.Point2D, type: Math.VertexType = Math.VertexType.Corner, arcRadius: float = 0.0) -> bool` | Appends a vertex at `pt` of the vertex type `type` (`arcRadius` for radius vertices). |
| `InsertVertex(beforeIndex: int, vertex: Math.PolyVertex) -> bool` | Inserts the vertex `vertex` before the vertex `beforeIndex`. |
| `SetVertex(index: int, vertex: Math.PolyVertex) -> bool` | Sets the vertex at `index`. |
| `GetVertexType(index: int) -> Math.VertexType \| None` | Returns the vertex type at `index`. |
| `SetVertexType(index: int, type: Math.VertexType) -> bool` | Sets the vertex type at `index`. |
| `GetVertexArcRadius(index: int) -> float \| None` | Returns the vertex arc radius at `index` (0 for vertices that are not arc vertices). |
| `SetVertexArcRadius(index: int, radius: float) -> bool` | Sets the vertex arc radius at `index` (makes the vertex an arc vertex). |
| `GetVertexMaxRadius(index: int) -> float \| None` | Largest radius that fits an arc vertex between its neighbours. |
| `GetControlVertex(index: int) -> Math.PolyVertex \| None` | Control vertex as stored in the document (for arc vertices the point that defines the fillet). |
| `HasCurves() -> bool \| None` | True when the polyline has curve vertices (Bezier, cubic, arc or radius). |

*Replaces all vertices and the closed flag*

| Method | Description |
|---|---|
| `SetPolygon(poly: Math.Polygon2D) -> bool` | Sets the polygon. |

Inherited: everything from [`PolyObject`](#polyobject), [`PrimitiveObject`](#primitiveobject).

### GroupObject

> **Full name:** `api.GroupObject` · **Inherits:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Group (`ObjectType.Group`): a container of other objects. Members are walked with the PrimitiveObject member API (GetFirstMember, ForEachMember, GetMembers, ...).

**Constructors**

| Constructor | Description |
|---|---|
| `GroupObject(h: Handle)` | Refers to the existing group `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create() -> GroupObject` *static* | Creates an empty group in the active layer / current container. |
| `Create(members: list[Handle]) -> GroupObject` *static* | Creates a group in the active layer / current container and moves `members` into it. Null handles are skipped. |
| `CreateFromSelection() -> GroupObject` *static* | Groups the selected objects of the active layer (VectorScript Group). |
| `Duplicate() -> GroupObject` | Duplicates the group in the drawing and returns the copy. |
| `GetMemberCount() -> int \| None` | Number of member items. |
| `AddMember(h: Handle) -> bool` | Moves `h` into the group as its last member and updates the group bounds. |
| `Ungroup() -> bool` | Moves the members to the group's container and deletes the group; the object becomes invalid. |

Inherited: everything from [`PrimitiveObject`](#primitiveobject).

### ParametricObject

> **Full name:** `api.ParametricObject` · **Inherits:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Generic plug-in (parametric) object (`ObjectType.Parametric`) of any kind, defined by a script or by a compiled plug-in.

Use this class ONLY when no specific class exists for the plug-in. The specific classes (PlantObject, WindowObject, DataTagObject, ...) know the meaning of the parameters, validate them and keep the object consistent; this class only reads and writes the raw parametric record fields by universal name.

Discover the parameters of a plug-in with GetParameterDefinitions(universalName) (no instance needed) or `GetParameters()` on an instance, and how its objects are placed with GetPluginKind(universalName), then use the typed Get/SetParam* accessors:

- string — any field type, as text — GetParamString / SetParamString
- real — Real, Dimension, CoordLocX/Y, Angle, Area, Volume — GetParamReal / SetParamReal
- bool — Boolean — GetParamBool / SetParamBool
- int — Integer, DimStdPopUp — GetParamInt / SetParamInt
- popUp — one-of-N text; choices from GetParamChoices (GetDefinitionChoices without an instance) GetParamString / SetParamString

The typed getters return `None` and the setters `False` when the object is invalid, the parameter does not exist or its type does not match the accessor. Lengths are in world units; Angle fields are in degrees as stored. Call `Reset()` after changing parameters so the plug-in regenerates its geometry.

**Constructors**

| Constructor | Description |
|---|---|
| `ParametricObject(h: Handle)` | Refers to the existing plug-in object `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | `True` for any plug-in object. |
| `IsNamed(h: Handle, universalName: str) -> bool` *static* | `True` for a plug-in object of the plug-in with that universal name, e.g. "Door". |
| `Create(universalName: str, location: Math.Point2D, angle: float = 0.0) -> ParametricObject` *static* | Creates a point-based plug-in object in the active layer / current container. `angle` in radians. |
| `CreateFromPath(universalName: str, hPath: Handle) -> ParametricObject` *static* | Creates a path-based plug-in object that takes `hPath` (a 2D poly) as its path. |
| `Duplicate() -> ParametricObject` | Duplicates the plug-in object in the drawing and returns the copy. |

*Plug-in definitions (by universal name, no instance needed)*

| Method | Description |
|---|---|
| `GetDefinitionFormat(universalName: str) -> RecordFormat` *static* | Parametric record format of the plug-in; invalid when no plug-in with that universal name is installed. Adds the format to the active document when it is not there yet. |
| `GetParameterDefinitions(universalName: str) -> list[RecordField]` *static* | Parameters of the plug-in with their universal and localized names, types and default values, in declaration order. Empty when no plug-in with that universal name is installed. |
| `GetDefinitionChoices(universalName: str, univParamName: str) -> list[str]` *static* | Universal choices of the PopUp parameter `univParamName` of the plug-in, in order, as GetParamChoices returns them for an object of the plug-in. Empty for an unknown plug-in or parameter and for a parameter that is not a PopUp. Like GetDefinitionFormat, adds the plug-in format to the active document when it is not there yet, named after `universalName` as given: pass the exact universal name (see GetPluginKind). |
| `GetPluginKind(universalName: str) -> ParametricObject.PluginKind \| None` *static* | Kind of the plug-in object with exactly that universal name, from Vectorworks' table of the installed plug-ins. Case matters: Vectorworks finds a plug-in without case, but names a format that it defines after the name it is given, so only the exact universal name is accepted. Empty when no plug-in object with exactly that name is installed (an unknown or differently cased name, or a menu command or a tool). Changes nothing in the document. |

*Universal name of the plug-in, e.g. "Door"*

| Method | Description |
|---|---|
| `GetParametricName() -> str \| None` | Returns the parametric name. |
| `GetParameters() -> list[RecordField]` | Parameters of this object's plug-in, see GetParameterDefinitions. |
| `GetParamNames() -> list[str]` | Returns the param names. |
| `HasParam(univParamName: str) -> bool` | True when the object has the parameter with the universal name `univParamName`. |
| `GetParamType(univParamName: str) -> RecordFieldType \| None` | Returns the param type for `univParamName`. |
| `GetParamChoices(univParamName: str) -> list[str]` | Universal choices of a PopUp parameter, in order; empty for other parameters. |
| `GetParamString(univParamName: str) -> str \| None` | Returns the param string for `univParamName`. |
| `SetParamString(univParamName: str, value: str) -> bool` | Sets the param string. |
| `GetParamReal(univParamName: str) -> float \| None` | Returns the param real for `univParamName`. |
| `SetParamReal(univParamName: str, value: float) -> bool` | Sets the param real. |
| `GetParamBool(univParamName: str) -> bool \| None` | Whether *Param Bool* is on for `univParamName`. |
| `SetParamBool(univParamName: str, value: bool) -> bool` | Sets the param bool. |
| `GetParamInt(univParamName: str) -> int \| None` | Returns the param int for `univParamName`. |
| `SetParamInt(univParamName: str, value: int) -> bool` | Sets the param int. |
| `GetPathObject() -> Handle` | Path object of a path-based plug-in object; null for point-based ones. |

Inherited: everything from [`PrimitiveObject`](#primitiveobject).

#### ParametricObject.PluginKind

> **Full name:** `api.ParametricObject.PluginKind` · **Kind:** `IntEnum`

How the objects of a plug-in are placed: the object subtype that the plug-in declares.

| Member | Value | Description |
|---|---|---|
| `Point` | `0` | Inserted at a point with a rotation, e.g. a door or a plant (hybrid symbol-like plug-ins). |
| `Linear` | `1` | Drawn as a line from a start point to an end point. |
| `Rectangle` | `2` | Drawn as a rectangle. |
| `Path2D` | `3` | Built on a 2D path that it takes over: CreateFromPath (Vectorworks makes the path a polyline). |
| `Path3D` | `4` | Built on a 3D path that it takes over: CreateFromPath (a NURBS curve, a 3D polygon, ...) |
| `Custom` | `5` | The plug-in handles its insertion itself. |

### TextObject

> **Full name:** `api.TextObject` · **Inherits:** [`PrimitiveObject`](#primitiveobject) → `api.Object`

Text block (`ObjectType.Text`): formatted text placed at an origin point. Character indices are 0-based and count UTF-16 code units (a character outside the Basic Multilingual Plane takes two). Text is exchanged as UTF-8; lines are separated by "\r" (see GetNewLine). Formatting setters work on the range [first, first + count); `count` is clamped to the end of the text, so the defaults (0, `kToEnd`) format the whole text. Sizes are in world units unless the name says "Points".

**Constructors**

| Constructor | Description |
|---|---|
| `TextObject(h: Handle)` | Refers to the existing text `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(text: str, origin: Math.Point2D, width: float = 0.0) -> TextObject` *static* | Creates a text block in the active layer / current container with the document default text attributes. `width` > 0 creates a fixed width (wrapping) text block. |
| `Duplicate() -> TextObject` | Duplicates the text in the drawing and returns the copy. |
| `CreateUnlinkedCopy() -> TextObject` | Copy of the text that keeps the formatting but is not linked to a record field. |

*Content*

| Method | Description |
|---|---|
| `GetText() -> str \| None` | Returns the text. |
| `SetText(text: str, clearFormatting: bool = False) -> bool` | Replaces the text. `clearFormatting` resets every character to the formatting of the first one. |
| `GetLength() -> int \| None` | Returns the length. |
| `InsertText(text: str, beforeIndex: int) -> bool` | Inserts before character `beforeIndex` (`GetLength()` appends); the new text takes the neighbouring formatting. |
| `AppendText(text: str) -> bool` | Appends `text` at the end of the text; the new text takes the formatting of the last character. |
| `DeleteText(first: int = 0, count: int = kToEnd) -> bool` | Deletes `count` characters starting at `first` (default: the whole text). |
| `GetNewLine() -> str` *static* | Line separator used by text objects: "\r". |

*Placement*

| Method | Description |
|---|---|
| `GetOrigin() -> Math.Point2D \| None` | Returns the origin. |
| `SetOrigin(origin: Math.Point2D) -> bool` | Sets the origin. |
| `GetAngle() -> float \| None` | Rotation in radians (counter-clockwise). |
| `IsFlipped() -> bool \| None` | True when the text is flipped (mirrored vertically). |
| `SetOrientation(angle: float, flipped: bool = False) -> bool` | Sets the orientation. |
| `GetBoxCorners() -> tuple[Math.Point2D * 4] \| None` | Corners of the (possibly rotated) text box: top-left, top-right, bottom-right, bottom-left. |
| `GetCharIndexAt(point: Math.Point2D) -> int \| None` | Index of the character nearest to `point`. |

*Layout*

| Method | Description |
|---|---|
| `GetHorizontalAlignment() -> TextObject.HorizontalAlignment \| None` | Returns the horizontal alignment. |
| `SetHorizontalAlignment(alignment: TextObject.HorizontalAlignment) -> bool` | Sets the horizontal alignment. |
| `GetVerticalAlignment() -> TextObject.VerticalAlignment \| None` | Returns the vertical alignment. |
| `SetVerticalAlignment(alignment: TextObject.VerticalAlignment) -> bool` | Sets the vertical alignment. |
| `GetSpacing() -> TextObject.Spacing \| None` | Returns the spacing. |
| `GetLeading() -> float \| None` | Custom line distance in world units; meaningful when `GetSpacing()` is `TextObject.Spacing.Custom`. |
| `SetSpacing(spacing: TextObject.Spacing, leading: float = 0.0) -> bool` | `leading` is used only with `TextObject.Spacing.Custom`. |
| `GetWidth() -> float \| None` | Width of the text box in world units. |
| `SetWidth(width: float) -> bool` | Sets the wrapping width; it applies when `IsWrapped()` is `True`. |
| `IsWrapped() -> bool \| None` | Fixed width text that wraps lines at `GetWidth()`. |
| `SetWrapped(wrapped: bool) -> bool` | Turns *Wrapped* on or off (Fixed width text that wraps lines at `GetWidth()`). |
| `GetLineHeight(charIndex: int = 0) -> float \| None` | Height of the line containing character `charIndex`, in world units. |
| `GetLineCount() -> int \| None` | Lines (after wrapping). |
| `GetLineStarts() -> list[int]` | Returns the line starts (first character index of each line). |
| `GetLines() -> list[str]` | Returns the lines (line texts without the separators). |
| `GetCharWidths() -> list[float]` | Advance width of each character in world units. |

*Character formatting at `charIndex`*

| Method | Description |
|---|---|
| `GetFont(charIndex: int = 0) -> str \| None` | Returns the font at `charIndex`. |
| `GetFontIndex(charIndex: int = 0) -> int \| None` | Returns the font index at `charIndex`. |
| `GetSize(charIndex: int = 0) -> float \| None` | Returns the size at `charIndex`. |
| `GetSizePoints(charIndex: int = 0) -> float \| None` | Returns the size points at `charIndex`. |
| `GetStyle(charIndex: int = 0) -> int \| None` | Returns the style at `charIndex`. |
| `GetCustomStyle(charIndex: int = 0) -> int \| None` | Returns the custom style at `charIndex`. |
| `GetColor(charIndex: int = 0) -> ColorRGB \| None` | Returns the color at `charIndex`. |
| `GetColorIndex(charIndex: int = 0) -> int \| None` | Returns the color index at `charIndex`. |

*Character spacing factor*

| Method | Description |
|---|---|
| `GetTracking(charIndex: int = 0) -> float \| None` | 1 = normal, 0.1 .. 10. |
| `GetStyleRuns() -> list[TextObject.StyleRun]` | The formatting runs of the whole text, in order. |
| `SetFont(fontName: str, first: int = 0, count: int = kToEnd) -> bool` | Character formatting of a range (fails for an empty range or an unknown font). |
| `SetFontIndex(fontIndex: int, first: int = 0, count: int = kToEnd) -> bool` | Sets the font index at `fontIndex`. |
| `SetSize(size: float, first: int = 0, count: int = kToEnd) -> bool` | Sets the size. |
| `SetSizePoints(points: float, first: int = 0, count: int = kToEnd) -> bool` | Sets the size points. |
| `SetStyle(style: int, first: int = 0, count: int = kToEnd) -> bool` | Replaces the style flags of the range (`kStylePlain` clears them). |
| `SetCustomStyle(customStyle: int, first: int = 0, count: int = kToEnd) -> bool` | Sets the custom style. |
| `SetColor(color: ColorRGB, first: int = 0, count: int = kToEnd) -> bool` | Sets the color. |
| `SetColorIndex(color: int, first: int = 0, count: int = kToEnd) -> bool` | Sets the color index. |
| `SetTracking(tracking: float, first: int = 0, count: int = kToEnd) -> bool` | `tracking` must be in 0.1 .. 10. |
| `GetTextStyleRef() -> int \| None` | Text style resources (see TextStyle). 0 = no text style. |
| `GetTextStyleRefAt(charIndex: int) -> int \| None` | Returns the text style ref at at `charIndex`. |
| `SetTextStyleRef(textStyle: int, first: int = 0, count: int = kToEnd) -> bool` | Sets the text style ref. Text style resources (see TextStyle). 0 = no text style. |
| `IsTextStyleByClass() -> bool \| None` | True when the text takes its text style from its class. |
| `IsTextStyleByClassAt(charIndex: int) -> bool \| None` | True when the character `charIndex` takes its text style from the class. |
| `SetTextStyleByClass(first: int = 0, count: int = kToEnd) -> bool` | Makes the range follow the text style of the object class. |
| `UpdateTextStyleSize() -> bool` | Rescales text style sizes after the object moved to a layer with another scale. |
| `GetTabStops() -> list[TextObject.TabStop]` | Tab stops (0-based, sorted by offset). |
| `GetTabStopCount() -> int \| None` | Number of tab stop items. |
| `AddTabStop(offset: float) -> bool` | Adds a left tab stop at `offset`. |
| `MoveTabStop(index: int, offset: float) -> bool` | Moves the tab stop `index` to `offset` (world units from the left of the text). |
| `RemoveTabStop(index: int) -> bool` | Vectorworks keeps the first tab stop: index 0 cannot be removed. |
| `GetRepeatingTabStop() -> float \| None` | Interval of the repeating tab stops in world units (0 = none). |
| `SetRepeatingTabStop(interval: float) -> bool` | Sets the repeating tab stop (Interval of the repeating tab stops in world units (0 = none)). |

*Flags*

| Method | Description |
|---|---|
| `HasTightFill() -> bool \| None` | Fill covers the text bounds only instead of the whole text box. |
| `SetTightFill(tightFill: bool) -> bool` | Turns *Tight Fill* on or off (Fill covers the text bounds only instead of the whole text box). |
| `IsLinkedToRecord() -> bool \| None` | Text linked to a record field of a symbol. |
| `UnlinkFromRecord() -> bool` | Unlinks the text from the record field of its symbol; it becomes plain text. |
| `IsNoteText() -> bool \| None` | True when the text is the note of a dimension. |
| `IsSIAElevationText() -> bool \| None` | True when the text is an SIA elevation text. |
| `IsRightToLeft() -> bool \| None` | True when the text runs right to left. |
| `FormatAsSIA(centimeters: str, millimeters: str, superscriptPercent: float = 100.0) -> bool` | SIA formatting (Swiss notation: centimeters with superscript millimeters). |
| `FormatValueAsSIA(value: float, alwaysMeters: bool, superscriptPercent: float = 100.0) -> bool` | Formats `value` (world units) as SIA text; `alwaysMeters` forces meters. |
| `FormatSegmentAsSIA(first: int, count: int, superscriptPercent: float = 100.0) -> bool` | Formats the `count` characters starting at `first` in SIA notation (centimeters with superscript millimeters). |

*Fonts*

| Method | Description |
|---|---|
| `FontIndexFromName(fontName: str) -> int \| None` *static* | Font index of the font named `fontName`. |
| `FontNameFromIndex(fontIndex: int) -> str \| None` *static* | Name of the font with the index `fontIndex`. |
| `PointsToWorld(points: float) -> float` *static* | Converts a size in page points to a length in world units. |
| `WorldToPoints(length: float) -> float` *static* | Converts a length in world units to a size in page points. |

**Constants**

| Constant | Type | Value | Description |
|---|---|---|---|
| `TextObject.kStylePlain` | `int` | `0` | Character style flags (GetStyle / SetStyle), combinable with '\|'. Outline and shadow display only on macOS. |
| `TextObject.kStyleBold` | `int` | `1` | Character style flags (GetStyle / SetStyle), combinable with '\|'. Outline and shadow display only on macOS. |
| `TextObject.kStyleItalic` | `int` | `2` | Character style flags (GetStyle / SetStyle), combinable with '\|'. Outline and shadow display only on macOS. |
| `TextObject.kStyleUnderline` | `int` | `4` | Character style flags (GetStyle / SetStyle), combinable with '\|'. Outline and shadow display only on macOS. |
| `TextObject.kStyleOutline` | `int` | `8` | Character style flags (GetStyle / SetStyle), combinable with '\|'. Outline and shadow display only on macOS. |
| `TextObject.kStyleShadow` | `int` | `16` | Character style flags (GetStyle / SetStyle), combinable with '\|'. Outline and shadow display only on macOS. |
| `TextObject.kCustomStyleNone` | `int` | `0` | Custom style flags (GetCustomStyle / SetCustomStyle). |
| `TextObject.kCustomDiagonalFraction` | `int` | `1` | Custom style flags (GetCustomStyle / SetCustomStyle). |
| `TextObject.kCustomVerticalFraction` | `int` | `2` | Custom style flags (GetCustomStyle / SetCustomStyle). |
| `TextObject.kCustomSuperscript` | `int` | `32` | Custom style flags (GetCustomStyle / SetCustomStyle). |
| `TextObject.kCustomSubscript` | `int` | `64` | Custom style flags (GetCustomStyle / SetCustomStyle). |
| `TextObject.kToEnd` | `int` | `2**64 - 1` | Range count meaning "up to the end of the text". |

Inherited: everything from [`PrimitiveObject`](#primitiveobject).

#### TextObject.StyleRun

> **Full name:** `api.TextObject.StyleRun` · **Inherits:** `api.Object`

A run of characters sharing the same formatting

**Constructors**

| Constructor | Description |
|---|---|
| `StyleRun()` | Default value (fields at their defaults). |
| `StyleRun(start, length, font, fontIndex, size, sizePoints, style, customStyle, color, textStyle, tracking)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `start` | `int` | Index of the first character of the run. |
| `length` | `int` | Number of characters of the run. |
| `font` | `str` | Font name. |
| `fontIndex` | `int` | Font index. |
| `size` | `float` | World units. |
| `sizePoints` | `float` | Page points. |
| `style` | `int` | `TextObject.kStyle...` flags. |
| `customStyle` | `int` | `TextObject.kCustom...` flags. |
| `color` | `ColorRGB` | Text color (color index). |
| `textStyle` | `int` | Text style resource; 0 = none. |
| `tracking` | `float` | Character spacing factor, 1 = normal. |

#### TextObject.TabStop

> **Full name:** `api.TextObject.TabStop` · **Inherits:** `api.Object`

Tab stop: offset in world units from the left of the text and alignment.

**Constructors**

| Constructor | Description |
|---|---|
| `TabStop()` | Default value (fields at their defaults). |
| `TabStop(offset, alignment)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `offset` | `float` | World units from the left of the text. |
| `alignment` | `TextObject.TabAlignment` | Alignment of the text at the tab stop. |

#### TextObject.HorizontalAlignment

> **Full name:** `api.TextObject.HorizontalAlignment` · **Kind:** `IntEnum`

Horizontal alignment of a text block.

| Member | Value | Description |
|---|---|---|
| `Left` | `1` |  |
| `Center` | `2` |  |
| `Right` | `3` |  |
| `Justify` | `4` |  |

#### TextObject.VerticalAlignment

> **Full name:** `api.TextObject.VerticalAlignment` · **Kind:** `IntEnum`

Vertical alignment of a text block relative to its origin.

| Member | Value | Description |
|---|---|---|
| `TopBox` | `1` | Top of the text box. |
| `TopBaseline` | `2` | Baseline of the first line. |
| `CenterBox` | `3` |  |
| `BottomBaseline` | `4` | Baseline of the last line. |
| `BottomBox` | `5` |  |

#### TextObject.Spacing

> **Full name:** `api.TextObject.Spacing` · **Kind:** `IntEnum`

Line spacing of a text block; `Custom` uses the leading passed to `SetSpacing`.

| Member | Value | Description |
|---|---|---|
| `Custom` | `0` | Custom leading, see GetLeading. |
| `Single` | `2` |  |
| `OneAndHalf` | `3` |  |
| `Double` | `4` |  |

#### TextObject.TabAlignment

> **Full name:** `api.TextObject.TabAlignment` · **Kind:** `IntEnum`

Alignment of the text at a tab stop.

| Member | Value | Description |
|---|---|---|
| `Left` | `1` |  |
| `Right` | `2` |  |
| `Center` | `3` |  |
| `Decimal` | `4` |  |

---

[Back to the index](README.md) · [Back to top](#objectprimitives--2d-primitive-objects)
