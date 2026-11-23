**English** • [Deutsch](../../PythonAPI.de/v2027.2/ObjectsArchitect.md) • [日本語](../../PythonAPI.ja/v2027.2/ObjectsArchitect.md)

# ObjectsArchitect — walls, roofs, slabs, windows, doors, columns, stairs

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The classes of the main architectural objects. `ArchitectObject` is their common base (it extends `PrimitiveObject` with access to the parameters of plug-in objects; for walls and roofs those accessors return nothing).

Walls (`WallObject`) and roofs (`RoofObject`) are native Vectorworks objects. Slabs, windows, doors, columns and stairs are plug-in objects recognized by their universal name ("Slab", "Window", "Door", "Column2", "Stairs CW"); the static `Is(h)` of each class checks it.

Conventions: `Is(h)` tests the object kind, `Create(...)` creates a new instance in the active layer / current container, typed getters return `None` for an invalid object or a missing field, typed setters return `True` on success. `WindowObject.Create` and `DoorObject.Create` place a free-standing instance at a point.

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [ArchitectObject](#architectobject)
  - [WallObject](#wallobject)
    - [WallObject.Heights](#wallobjectheights)
    - [WallObject.HeightBound](#wallobjectheightbound)
    - [WallObject.Caps](#wallobjectcaps)
    - [WallObject.BoundStatus](#wallobjectboundstatus)
    - [WallObject.BoundKind](#wallobjectboundkind)
  - [SlabObject](#slabobject)
  - [RoofObject](#roofobject)
    - [RoofObject.Attributes](#roofobjectattributes)
    - [RoofObject.Accessories](#roofobjectaccessories)
    - [RoofObject.Edge](#roofobjectedge)
    - [RoofObject.MiterType](#roofobjectmitertype)
  - [WindowObject](#windowobject)
  - [DoorObject](#doorobject)
  - [ColumnObject](#columnobject)
  - [StairObject](#stairobject)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`ArchitectObject`](#architectobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Common base of the Architect object classes (wall, slab, roof, window, door, column, stair). |
| [`WallObject`](#wallobject) | class | [`ArchitectObject`](#architectobject) | Wall (`ObjectType.Wall`) - a straight or curved wall that can host windows, doors and other wall inserts. |
| [`WallObject.Heights`](#wallobjectheights) | class (nested) |  | Heights (world units) relative to the layer plane (0 = top of layer, negative = below). |
| [`WallObject.HeightBound`](#wallobjectheightbound) | class (nested) |  | Bound of the bottom or top of the wall: what its height follows. |
| [`WallObject.Caps`](#wallobjectcaps) | class (nested) |  | End caps. |
| [`WallObject.BoundStatus`](#wallobjectboundstatus) | IntEnum (nested) |  | Status of a wall height bound (`WallObject.HeightBound.fStatus`). |
| [`WallObject.BoundKind`](#wallobjectboundkind) | IntEnum (nested) |  | What a wall height bound follows: the layer elevation, the layer wall height or a story level. |
| [`SlabObject`](#slabobject) | class | [`ArchitectObject`](#architectobject) | Slab - a horizontal element (floor, roof deck, ceiling deck, ...) defined by a 2D boundary profile and vertically extruded by its thickness. |
| [`RoofObject`](#roofobject) | class | [`ArchitectObject`](#architectobject) | Roof (`ObjectType.RoofContainer`) - a polygonal roof defined by a list of edges. |
| [`RoofObject.Attributes`](#roofobjectattributes) | class (nested) |  | Roof-wide attributes. |
| [`RoofObject.Accessories`](#roofobjectaccessories) | class (nested) |  | Roof accessories along the perimeter. |
| [`RoofObject.Edge`](#roofobjectedge) | class (nested) |  | Roof edges (polygon vertex + per-edge slope and overhang), in the order of the roof outline. |
| [`RoofObject.MiterType`](#roofobjectmitertype) | IntEnum (nested) |  | Miter types for the roof edges (how two adjacent slope faces are joined). |
| [`WindowObject`](#windowobject) | class | [`ArchitectObject`](#architectobject) | Window plug-in object (universal name "Window") from the Architectural Objects plug-in. |
| [`DoorObject`](#doorobject) | class | [`ArchitectObject`](#architectobject) | Door plug-in object (universal name "Door") from the Architectural Objects plug-in. |
| [`ColumnObject`](#columnobject) | class | [`ArchitectObject`](#architectobject) | Column plug-in object - the Vectorworks column, universal name "Column2". |
| [`StairObject`](#stairobject) | class | [`ArchitectObject`](#architectobject) | Stair plug-in object - the Vectorworks stair, universal name "Stairs CW". |

## Classes

### ArchitectObject

> **Full name:** `api.ArchitectObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Common base of the Architect object classes (wall, slab, roof, window, door, column, stair).

The architectural objects fall into two families:

- Native container objects with their own object types (Wall = `ObjectType.Wall`, Roof = `ObjectType.RoofContainer`). Each of them exposes typed accessors (heights, thickness, style, ...). They are NOT plug-in objects, so the parametric-record accessors below return empty / False on them.
- Plug-in objects (Slab "Slab", Window "Window", Door "Door", Column "Column2", Stair "Stairs CW"). These store their configuration in a record; the parametric accessors below are the primary way to read / write those fields. The slab also has typed accessors, and a floor object (`ObjectType.Slab` of the floor kind) is a native slab without a record.

Every subclass inherits the generic PrimitiveObject API (identity, class, attributes, hierarchy, bounds, move/rotate/scale/mirror, delete, ...). Conventions:

- Getters return `None` for an invalid object or a missing parameter.
- Setters return `True` on success and `False` for an invalid object or a missing parameter.
- Lengths are in world units, angles in radians (unless a specific parameter is documented as degrees), strings are UTF-8.

Parameter access primer (Get/SetParam*):

- Applies to plug-in objects only (slabs, windows, doors, columns, stairs). For a wall, a roof or a floor object the parametric accessors return None / False because the underlying object does not carry a parametric record.
- The Window, Door, Column and Stair classes list the available parameter names in their "Full parameter reference"; `GetParamNames()` lists the parameters of any of them, including the slab. Use those names verbatim (case-sensitive, UTF-8) with GetParamString / SetParamString / GetParamReal / ... to read or write any field the subclass does not already expose through a dedicated typed accessor.
- Parameter types in the tables use these tags:

- string — text (UTF-8) - GetParamString / SetParamString
- int — 32-bit integer - GetParamInt / SetParamInt
- bool — boolean (may be stored as "True"/"False" strings) - GetParamBool / SetParamBool
- real — floating-point value (world coordinate, angle in degrees, plain number, area, ...) - GetParamReal / SetParamReal
- popup — one-of-N string choice - GetParamString / SetParamString; valid values are listed next to the parameter

- Names starting with "__" are internal plug-in state; readable but not usually meaningful to write directly.

**Constructors**

| Constructor | Description |
|---|---|
| `ArchitectObject(h: Handle)` | Refers to any object `h` as a generic `ArchitectObject`; `IsValid()` only checks for a non-null handle. Use `GetParametricName()` or a concrete class's `Is(h)` to check the object kind. |

**Methods**

*General*

| Method | Description |
|---|---|
| `GetParametricName() -> str \| None` | Universal (parametric) name of the object, e.g. "Slab", "Window", "Door", "Column2", "Stairs CW". Empty for the native wall and roof objects, a floor object and handles that are not plug-in objects. |
| `HasParam(univParamName: str) -> bool` | Whether this plug-in object has a field with the given universal name. Always returns `False` for the native wall and roof objects and a floor object. |
| `GetParamNames() -> list[str]` | Ordered list of every parameter (universal) name defined by this object's plug-in. Empty for the native wall and roof objects and a floor object. |
| `GetParamString(univParamName: str) -> str \| None` | Generic, string-keyed field accessors. Prefer the typed named accessors on the subclasses when available. Use these for parameters that do not have a dedicated accessor. |
| `SetParamString(univParamName: str, value: str) -> bool` | Sets the param string. Generic, string-keyed field accessors. Prefer the typed named accessors on the subclasses when available. Use these for parameters that do not have a dedicated accessor. |
| `GetParamReal(univParamName: str) -> float \| None` | Returns the param real for `univParamName`. |
| `SetParamReal(univParamName: str, value: float) -> bool` | Sets the param real. |
| `GetParamBool(univParamName: str) -> bool \| None` | Whether *Param Bool* is on for `univParamName`. |
| `SetParamBool(univParamName: str, value: bool) -> bool` | Sets the param bool. |
| `GetParamInt(univParamName: str) -> int \| None` | Returns the param int for `univParamName`. |
| `SetParamInt(univParamName: str, value: int) -> bool` | Sets the param int. |

*plug-in style*

| Method | Description |
|---|---|
| `GetPluginStyleName() -> str \| None` | Name of the plug-in style resource of the object; empty when the object is unstyled or not a plug-in object (the native wall and roof objects, a floor object), or the object is invalid. |
| `IsParamSetByStyle(univParamName: str) -> bool` | Whether the plug-in style of the object sets the parameter `univParamName`: the style takes it "by style", "by catalog" (also a parameter of the catalog the style uses), or "mixed" (a state of the style dialogs that is treated as set by the style). `False` for a parameter that the object takes "by instance", for an unstyled object and for an object that is not a plug-in object. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### WallObject

> **Full name:** `api.WallObject` · **Inherits:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Wall (`ObjectType.Wall`) - a straight or curved wall that can host windows, doors and other wall inserts.

A wall carries per-end heights (top and bottom, relative to the layer plane), a thickness, an optional wall style (which controls its layered components), left / right / round caps, and a number of read-only computed areas / lengths / heights. Openings and inserts are stored as child objects of the wall.

A wall is NOT a plug-in object; the generic Get/SetParam* accessors inherited from ArchitectObject return empty / False. Use the typed accessors below and the wall's inherited ObjectAttributes for the graphical attributes.

**Constructors**

| Constructor | Description |
|---|---|
| `WallObject(h: Handle)` | Refers to the existing wall `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(start: Math.Point2D, end: Math.Point2D, thickness: float = 0.0) -> WallObject` *static* | Creates a straight wall between `start` and `end` in the active layer / current container. Passing `thickness` = 0 uses the active wall preferences thickness. |
| `CreateRound(start: Math.Point2D, onArc: Math.Point2D, end: Math.Point2D, thickness: float = 0.0) -> WallObject` *static* | Creates a curved wall through the three given points (start, a point on the arc, end). |
| `Duplicate() -> WallObject` | Duplicates the wall in the drawing and returns the copy. |

*Geometry*

| Method | Description |
|---|---|
| `GetLine() -> Math.Line2D \| None` | Line from the wall's start to its end. Empty for a curved wall. |
| `SetLine(start: Math.Point2D, end: Math.Point2D) -> bool` | Sets the line. Line from the wall's start to its end. Empty for a curved wall. |
| `GetStartPoint() -> Math.Point2D \| None` | Returns the start point. |
| `GetEndPoint() -> Math.Point2D \| None` | Returns the end point. |
| `GetLength() -> float \| None` | Returns the length (world units, straight-line length). |
| `GetAngle() -> float \| None` | Returns the angle (radians, direction from start to end). |
| `SetThickness(thickness: float) -> bool` | Thickness (world units). Setting the thickness detaches the wall from its wall style. |
| `GetHeights() -> WallObject.Heights \| None` | Returns the heights. |
| `SetHeights(heights: WallObject.Heights) -> bool` | Sets the heights. |
| `SetHeights(startTop: float, startBottom: float, endTop: float, endBottom: float) -> bool` | Sets the heights. |
| `GetHeightBound(isTop: bool) -> WallObject.HeightBound` | Returns the height bound for `isTop`. |
| `SetHeightBounds(bottomBound: WallObject.HeightBound, topBound: WallObject.HeightBound) -> bool` | Binds the bottom and the top of the wall and moves its heights to them (the wall's Top / Bottom Bound in the Object Info palette). For layer bounds fRelativeStory and fLevelType are ignored and stored as 0 and empty. Fails when a bound does not exist for the wall (e.g. its layer is in no story, or the story has no such level), or when the top would not be above the bottom. A stored bound that is missing (older files) or no longer exists is first replaced by the layer elevation bound at the wall's current height, from which the move is measured. Like the other setters it does not register undo: call `Document.AddBothSwapObject` first. |
| `SetHeightBound(isTop: bool, bound: WallObject.HeightBound) -> bool` | Binds the top (isTop) or the bottom of the wall like SetHeightBounds; the other end keeps its bound. |
| `GetAverageHeight() -> float \| None` | Returns the average height. |
| `GetCaps() -> WallObject.Caps \| None` | Returns the caps. |
| `SetCaps(caps: WallObject.Caps) -> bool` | Sets the caps. |
| `GetStyle() -> int \| None` | Wall style (`ObjectType.WallStyle` resource). 0 = un-styled (freehand thickness / components). |
| `SetStyle(wallStyle: int, selectedOffset: float = 0.0, replacingOffset: float = 0.0) -> bool` | Sets the style. Wall style (`ObjectType.WallStyle` resource). 0 = un-styled (freehand thickness / components). |
| `IsCurtainWall() -> bool \| None` | Curtain wall flag (a wall used as the framing of a curtain-wall system). |
| `SetIsCurtainWall(isCurtainWall: bool) -> bool` | Turns *Curtain Wall* on or off. |

Inherited: everything from [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### WallObject.Heights

> **Full name:** `api.WallObject.Heights` · **Inherits:** `api.Object`

Heights (world units) relative to the layer plane (0 = top of layer, negative = below). A wall can be tapered by using different start / end heights.

**Constructors**

| Constructor | Description |
|---|---|
| `Heights()` | Default value (fields at their defaults). |
| `Heights(startTop, startBottom, endTop, endBottom)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `startTop` | `float` | Top height at the wall start. |
| `startBottom` | `float` | Bottom height at the wall start. |
| `endTop` | `float` | Top height at the wall end. |
| `endBottom` | `float` | Bottom height at the wall end. |

#### WallObject.HeightBound

> **Full name:** `api.WallObject.HeightBound` · **Inherits:** `api.Object`

Bound of the bottom or top of the wall: what its height follows. GetHeightBound returns it; SetHeightBound(s) take it, using fKind, fRelativeStory, fLevelType and fOffset (fStatus and fElevation are read-only results).

**Constructors**

| Constructor | Description |
|---|---|
| `HeightBound()` | Default value (fields at their defaults). |
| `HeightBound(fStatus, fKind, fRelativeStory, fLevelType, fOffset, fElevation)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fStatus` | `WallObject.BoundStatus` | Whether the bound is missing, unresolved, invalid or valid. |
| `fKind` | `WallObject.BoundKind` | Layer elevation, layer wall height, or a story level. |
| `fRelativeStory` | `int` | Story: -1 the story below, 0 the story of the wall's layer, 1 the story above. |
| `fLevelType` | `str` | Story: the level type of the level in that story. |
| `fOffset` | `float` | World units, added to the bound height. |
| `fElevation` | `float \| None` | Resolved bound height (world Z, offset included) when fStatus is Valid. |

#### WallObject.Caps

> **Full name:** `api.WallObject.Caps` · **Inherits:** `api.Object`

End caps.

**Constructors**

| Constructor | Description |
|---|---|
| `Caps()` | Default value (fields at their defaults). |
| `Caps(leftCap, rightCap, round)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `leftCap` | `bool` | Close the start end. |
| `rightCap` | `bool` | Close the end end. |
| `round` | `bool` | Cap style is rounded. |

#### WallObject.BoundStatus

> **Full name:** `api.WallObject.BoundStatus` · **Kind:** `IntEnum`

Status of a wall height bound (`WallObject.HeightBound.fStatus`).

| Member | Value | Description |
|---|---|---|
| `Missing` | `0` |  |
| `Unresolved` | `1` |  |
| `Invalid` | `2` |  |
| `Valid` | `3` |  |

#### WallObject.BoundKind

> **Full name:** `api.WallObject.BoundKind` · **Kind:** `IntEnum`

What a wall height bound follows: the layer elevation, the layer wall height or a story level.

| Member | Value | Description |
|---|---|---|
| `Unknown` | `0` |  |
| `LayerElevation` | `1` |  |
| `LayerWallHeight` | `2` |  |
| `Story` | `3` |  |

### SlabObject

> **Full name:** `api.SlabObject` · **Inherits:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Slab - a horizontal element (floor, roof deck, ceiling deck, ...) defined by a 2D boundary profile and vertically extruded by its thickness. Two objects are slabs:

- the slab plug-in object (`ObjectType.Parametric`, universal name "Slab") that Vectorworks creates;
- a floor object (`ObjectType.Slab` of the floor kind, created with the Floor command). Roof faces and legacy columns are `ObjectType.Slab` objects too, but they are not slabs.

A slab carries an elevation and a style (a slab style resource) that controls its component layers. Holes can be added to the boundary through slab modifiers.

The slab plug-in object has a parametric record: the generic Get/SetParam* accessors inherited from ArchitectObject read and write its parameters (`GetParamNames()` lists them). On a floor object they return empty / False.

**Constructors**

| Constructor | Description |
|---|---|
| `SlabObject(h: Handle)` | Refers to the existing slab `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(hProfile: Handle) -> SlabObject` *static* | Creates a slab plug-in object whose boundary is the given 2D profile: a polygon, polyline, oval (circle) or arc. The profile handle is consumed by the slab. Returns an invalid object for another kind of profile or on failure. |
| `Duplicate() -> SlabObject` | Duplicates the slab in the drawing and returns the copy. |
| `GetHeight() -> float \| None` | Height of the slab's datum, the top or bottom of its core component as the slab style sets it, in world units; SetHeight moves the slab vertically. Slab plug-in object only: the getter is empty and the setter returns `False` for a floor object. |
| `SetHeight(height: float) -> bool` | Sets the height. Height of the slab's datum, the top or bottom of its core component as the slab style sets it, in world units; SetHeight moves the slab vertically. Slab plug-in object only: the getter is empty and the setter returns `False` for a floor object. |
| `GetStyle() -> int \| None` | Slab style (a slab style resource); 0 = un-styled. SetStyle(0) unstyles the slab and keeps its current components; setting a style replaces the component configuration with the style's components. The setter returns `False`, and does not change the slab, for an index that is not a slab style of the drawing; it also returns `False` when the slab does not have the style afterwards. |
| `SetStyle(slabStyle: int) -> bool` | Sets the style. Slab style (a slab style resource); 0 = un-styled. SetStyle(0) unstyles the slab and keeps its current components; setting a style replaces the component configuration with the style's components. The setter returns `False`, and does not change the slab, for an index that is not a slab style of the drawing; it also returns `False` when the slab does not have the style afterwards. |
| `AddModifier(hProfile: Handle, isSubtract: bool, componentID: int = -1, clipToBoundary: bool = True) -> bool` | Adds a modifier (a 2D profile) to the slab.<br>• When `isSubtract` is `True` the profile is a hole cut through the slab.<br>• `componentID` targets a specific component (< 0 for the whole slab).<br>• `clipToBoundary` clips the profile to the slab boundary. |

Inherited: everything from [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### RoofObject

> **Full name:** `api.RoofObject` · **Inherits:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Roof (`ObjectType.RoofContainer`) - a polygonal roof defined by a list of edges. Each edge has an insertion point, a slope, a projection (eave overhang) and an eave height. Roof accessories (attic, soffit, fascia) can be inserted around the perimeter.

A roof is NOT a plug-in object; the generic Get/SetParam* accessors inherited from ArchitectObject return empty / False.

**Constructors**

| Constructor | Description |
|---|---|
| `RoofObject(h: Handle)` | Refers to the existing roof `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(generateGableWalls: bool, bearingInset: float, roofThickness: float, miterType: RoofObject.MiterType, verticalMiter: float) -> RoofObject` *static* | Creates a new roof object.<br>• `generateGableWalls` automatically extends host walls up to the roof underside.<br>• `bearingInset` distance from the wall to the roof bearing point, in world units.<br>• `roofThickness` thickness of the roof deck, in world units.<br>• `miterType` see `RoofObject.MiterType`.<br>• `verticalMiter` vertical component of a double miter, in world units.<br>The new roof has no attic, soffit or fascia; SetAccessories adds them. |
| `Duplicate() -> RoofObject` | Duplicates the roof in the drawing and returns the copy. |
| `GetAttributes() -> RoofObject.Attributes \| None` | Returns the attributes. |
| `SetAttributes(attributes: RoofObject.Attributes) -> bool` | Sets the attributes. |
| `SetAccessories(accessories: RoofObject.Accessories) -> bool` | Sets the accessories. |
| `GetEdgeCount() -> int \| None` | Number of edge items (count of edges (roof outline vertices)). |
| `GetEdge(index: int) -> RoofObject.Edge \| None` | Returns the edge at `index` (0-based index). |
| `SetEdge(index: int, edge: RoofObject.Edge) -> bool` | Sets the edge at `index`. |
| `AppendEdge(edge: RoofObject.Edge) -> bool` | Appends the edge `edge` (insertion point, slope, projection, eave height) to the roof. |
| `RemoveEdge(index: int) -> bool` | Removes the edge at `index`. |

Inherited: everything from [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### RoofObject.Attributes

> **Full name:** `api.RoofObject.Attributes` · **Inherits:** `api.Object`

Roof-wide attributes.

**Constructors**

| Constructor | Description |
|---|---|
| `Attributes()` | Default value (fields at their defaults). |
| `Attributes(generateGableWalls, bearingInset, roofThickness, miterType, verticalMiter)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `generateGableWalls` | `bool` | Whether gable walls are generated. |
| `bearingInset` | `float` | Bearing inset. |
| `roofThickness` | `float` | Roof thickness. |
| `miterType` | `RoofObject.MiterType` | Miter type of the roof edges. |
| `verticalMiter` | `float` | Vertical miter value. |

#### RoofObject.Accessories

> **Full name:** `api.RoofObject.Accessories` · **Inherits:** `api.Object`

Roof accessories along the perimeter.

**Constructors**

| Constructor | Description |
|---|---|
| `Accessories()` | Default value (fields at their defaults). |
| `Accessories(insertAttic, insertSoffit, insertFascia, fasciaWidth, fasciaHeight, atticHeight, recess, rakeThickness, trimDepth)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `insertAttic` | `bool` | Whether an attic is inserted. |
| `insertSoffit` | `bool` | Whether a soffit is inserted. |
| `insertFascia` | `bool` | Whether a fascia is inserted. |
| `fasciaWidth` | `float` | World units. |
| `fasciaHeight` | `float` | Fascia height. |
| `atticHeight` | `float` | Attic height. |
| `recess` | `float` | Recess. |
| `rakeThickness` | `float` | Rake thickness. |
| `trimDepth` | `float` | Trim depth. |

#### RoofObject.Edge

> **Full name:** `api.RoofObject.Edge` · **Inherits:** `api.Object`

Roof edges (polygon vertex + per-edge slope and overhang), in the order of the roof outline. The eave height is relative to the elevation of the roof's design layer; SetEdge and AppendEdge take it in the same way.

**Constructors**

| Constructor | Description |
|---|---|
| `Edge()` | Default value (fields at their defaults). |
| `Edge(insertionPoint, slope, projection, eaveHeight)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `insertionPoint` | `Math.Point2D` | Insertion point of the edge. |
| `slope` | `float` | Degrees. |
| `projection` | `float` | World units - eave overhang. |
| `eaveHeight` | `float` | World units, relative to the layer elevation. |

#### RoofObject.MiterType

> **Full name:** `api.RoofObject.MiterType` · **Kind:** `IntEnum`

Miter types for the roof edges (how two adjacent slope faces are joined).

| Member | Value | Description |
|---|---|---|
| `Vertical` | `1` | Vertical intersection. |
| `Horizontal` | `2` | Horizontal intersection. |
| `Double` | `3` | Double miter (intersection has both a vertical and a horizontal part). |

### WindowObject

> **Full name:** `api.WindowObject` · **Inherits:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Window plug-in object (universal name "Window") from the Architectural Objects plug-in.

A window inserts into a host wall (`ObjectType.Wall`) at a specific position along the wall and at an elevation. It carries frame / sash / muntin / glazing / sill / trim / lintel / shutter parameters.

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Overall size and placement

- "Width" — real — size of the window as the Object Info palette shows it, measured as "SizeReference" says (GetWidth / SetWidth)
- "Height" — real — (GetHeight / SetHeight)
- "SizeReference" — popup — Sash Opening / Unit Size / Rough Opening: what "Width" / "Height" measure
- "OverallWidth" — real — unit size, which the window computes from "Width" / "Height" when it is reset (GetOverallWidth); a value written here is replaced at the reset
- "OverallHeight" — real — (GetOverallHeight)
- "Elevation" — real — height of the head or the sill of the window, as "ElevationSetAt" says, above the layer plane (GetElevation; GetSillHeight / GetHeadHeight)
- "ElevationSetAt" — popup — Head of Window / Sill of Window
- "OffsetInWall" — real — horizontal offset from the wall insertion point
- "UseWallDepth" — bool — match the wall thickness for the frame depth
- "TopShape" — popup — Square / Round / Segment / Sloped from Left / Sloped from Right / Gable / Ellipse / Gothic / Half Round from Left / Half Round from Right / Half Segment from Left / Half Segment from Right / Half Ellipse from Left / Half Ellipse from Right / Half Gothic from Left / Half Gothic from Right
- "Rise", "Spring" — real — parameters of curved / gabled tops
- "WindowShape" — popup — Rectangle / Circle / Oval / Half Circle / Half Oval / Diamond / Hexagon - Top Flat / Hexagon - Side Flat / Octagon
- "RoundWallOffset" — real — offset from a round host wall
- "SpanWall" — bool — window spans the entire host wall
- "CornerWindow" — bool — use a corner-window configuration
- "CornerWindowOp" — popup — Opening / Cased Opening / Flush Glass / Flush Glass - No Sash / Mitered Sash / Corner Post
- "CornerPostSize", "CornerPostOffset" — real

Configuration

- "Configuration" — popup — Opening / Cased Opening / Awning / Casement / Fixed Glass / Folding / Hopper / Hung / Sliding / Tilt/Turn / Vertical Pivot / Custom
- "CasementOperation" — popup — Single / Bi-Part (Casement configuration)
- "FixedGlassOperation" — popup — Sash / No Sash (Fixed Glass configuration)
- "HungOperation" — popup — Single / Double (Hung configuration)
- "SashOperation" — popup — legacy; superseded by "Configuration" and the per-type operations
- "CustSashOpPopup" — popup — custom sash operation
- "CustSashOp", "CustSashLock" — string
- "CustSashWdth", "CustSashHght" — string — custom sash width / height layout
- "CustomSash" — bool
- "CustSashSel" — string
- "CustSashWidth", "CustSashHeight" — real
- "Rows", "Cols" — int — custom sash grid dimensions
- "UnequalSash" — bool
- "SashScaleFactor" — real
- "HingeDirection" — bool — reverse the hinge side
- "HingePref" — int
- "Show3DOpen" — bool
- "OpenAngle" — real — degrees

Transom

- "Transom" — bool
- "TransWidth", "TransDepth" — real — transom mullion width / depth
- "TransomGlazingClass" — popup — class name
- "NumVTranMuntins", "NumHTranMuntins" — int
- "TranMuntinWidth", "TranMuntinOffset", "TranMuntinDepth" — real
- "TranMuntinPattern" — popup — Colonial / Prairie / Prairie w/sunburst / Colonial w/sunburst / Renaissance
- "TranNumOfRays" — int
- "TransomMuntins" — bool
- "MullionWidth", "MullionDepth" — real

Curtain wall configuration

- "CurtainWallWindow" — bool
- "CWSashOperation" — popup — Fixed Glass / Fixed Glass - No Sash / Casement / Bi-parting Casement / Horizontal Slider / Awning / Hopper / Tilt/Turn / Vertical Pivot

Jamb / sash frame

- "JambWidth" — real — jamb face width
- "JambDepth" — real — jamb depth (into the wall)
- "SashWidth", "SashDepth" — real
- "ShimGap" — real
- "MasonMod" — real — masonry module offset
- "UseJambExtension" — bool
- "JambExtenWidth" — real

Muntins

- "MuntinPattern" — popup — Colonial / Prairie / Prairie w/sunburst / Colonial w/sunburst / Renaissance
- "MuntinApplication" — popup — None / All / Top / Bottom / Transom / Top\Bottom / Top\Transom / Bot\Transom
- "NumVMuntins", "NumHMuntins" — int
- "MuntinWidth", "MuntinOffset", "MuntinDepth" — real
- "NumOfRays" — int
- "TopSashMuntins", "BottomSashMuntins", "TransomMuntins" — bool
- "CustomTopMuntins" — bool
- "TopSashHorizBars" — int
- "CustMuntins" — string
- "CustMullDepth", "CustMullWidth" — real

Sill / stool

- "SillStyle" — popup — Timber / Masonry / Brick / Open Profile Beside Frame / Open Profile Below Frame / Closed Profile
- "IncludeSill" — bool
- "SillDepth", "SillHeight", "SillLip", "SillRise", "SillKeep", "SillExt" — real
- "StoolLip", "StoolNose" — real

Trim

- "IntTrim", "ExtTrim" — bool
- "IntTrimWidth", "IntTrimDepth", "ExtTrimWidth", "ExtTrimDepth" — real
- "TrimUnderStool", "TrimUnderSill" — bool

Splays (interior / exterior wall opening angle)

- "IntSplay", "ExtSplay" — bool
- "UseIntSplayAngle", "UseExtSplayAngle" — bool
- "IntSplayAngle", "ExtSplayAngle" — real (degrees)
- "IntSplayDiag", "ExtSplayDiag" — real
- "UseIntSplayWidth", "UseExtSplayWidth" — bool
- "IntSplayWidth", "ExtSplayWidth" — real
- "IntSplayDepth", "ExtSplayDepth" — real

Lintel

- "Lintels" — bool
- "LintelThick" — real
- "IntLintelProt", "ExtLintelProt" — real
- "UseLintelAngle" — bool
- "LintelAngle" — real (degrees)
- "UseLintelDrop" — bool
- "LintelDrop" — real
- "LintelClass" — popup — class name

Shutters

- "IntShutters", "ExtShutters" — bool
- "IntShtThick", "ExtShtThick" — real
- "IntShtMllWidth", "ExtShtMllWidth" — real
- "IntShtDivWSash", "ExtShtDivWSash" — bool
- "IntShtEqualDiv", "ExtShtEqualDiv" — bool
- "IntShtNumPanels", "ExtShtNumPanels" — int
- "IntShtIsPanel", "ExtShtIsPanel" — bool
- "IntShtIsCustom", "ExtShtIsCustom" — bool
- "IntShtCustomIndex", "ExtShtCustomIndex" — int
- "UseCustIntShutterWidth", "UseCustExtShutterWidth" — bool
- "CustIntShutterWidth", "CustExtShutterWidth" — real

ID / scheduling / tag

- "OnSchedule" — bool
- "IDPrefix", "IDLabel", "IDSuffix" — string
- "IDLabelSize" — real
- "IDLabelShape" — popup — None / Rectangle / Round / Hexagon
- "IDLabelClass" — popup — class name
- "KeepIDHoriz" — bool
- "ShowIDLeader" — bool
- "IDLeaderLW" — int — pen weight
- "UseMarker" — bool
- "MarkerIDx" — int
- "MarkerStyle" — int
- "MarkerAngle" — int (degrees)
- "MarkerSize" — real
- "MarkerWidth" — real
- "MarkerThick", "MarkerThickB" — real / int
- "TagInElevation" — bool
- "Tag3DHorzOffset", "Tag3DVertOffset" — real

Cavities (frame) counts

- "NumOfIntCavities", "NumOfExtCavities" — int

Classes (per component)

- "IntSashClass", "ExtSashClass" — popup — class name
- "IntJTClass", "ExtJTClass" — popup — class name (jamb + trim)
- "IntShutterClass", "ExtShutterClass" — popup — class name
- "SillClass", "StoolClass" — popup — class name
- "GlazingClass", "TransomGlazingClass" — popup — class name
- "IntTransomClass", "ExtTransomClass" — popup — class name
- "HingeClass" — popup — class name
- "Sills2DClass", "CeilingMainClass", "NonPlotClass" — popup — class name

Metadata (for schedules)

- "WindowDesc" — string — short description
- "Model", "ManufSupplier", "StockNo", "GlassDesc" — string
- "HeadDetail", "JambDetail", "SillDetail" — string
- "Accessories" — string
- "Egress" — string / bool
- "WindowMaterial", "WindowFinish", "FrameType", "FrameMaterial", "FrameFinish", "WindowSill" — string
- "Location" — string
- "LintelType" — string
- "UserFld1..UserFld10" — string — user-defined fields for schedules

Display flags

- "PlanDetail" — bool — draw plan-view detail
- "DrawWallLines" — bool
- "Clerestory" — bool
- "LW_LS_OverRide" — bool
- "IsDoor" — bool — internal flag (window used as a door)
- "Flipped" — bool
- "WrapPointsSwapped" — bool
- "ShowShimGap" — bool
- "ShowInteriorHinge" — bool
- "Set2DAttribsBy" — popup — Object / Line Style / Class
- "PenStyle", "FillStyle" — popup — None / Solid / Line Type / By Object / By Class (pen), plus Hatch / Tile / Gradient / By Material (fill)
- "LastRenderMode", "Last3DView" — int
- "NGA2" — real (area, read-only)
- "ControlPoint01X..ControlPoint03Y" — real (world coordinates)

**Constructors**

| Constructor | Description |
|---|---|
| `WindowObject(h: Handle)` | Refers to the existing window `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D) -> WindowObject` *static* | Creates a window at `position`. Typically inserted into a wall via WallObject afterwards. |
| `Duplicate() -> WindowObject` | Duplicates the window in the drawing and returns the copy. |

*size (world units)*

| Method | Description |
|---|---|
| `GetWidth() -> float \| None` | "Width" / "Height" are the size of the window as the Object Info palette shows it, measured as the Size Reference says: the sash opening ("Sash Opening"), the unit ("Unit Size") or the rough opening ("Rough Opening"). When the window is reset, it computes its unit size (GetOverallWidth / GetOverallHeight) from them: call `Reset()` after the setters. The setters return `False`, and write nothing, for an invalid object, a value that is not a positive finite number, or a parameter that the plug-in style of the window sets (IsParamSetByStyle). Vectorworks measures a window of the Opening configuration as a rough opening, and sizes a window in a curtain wall to its panel, whatever these values say. |
| `SetWidth(value: float) -> bool` | Sets the width. "Width" / "Height" are the size of the window as the Object Info palette shows it, measured as the Size Reference says: the sash opening ("Sash Opening"), the unit ("Unit Size") or the rough opening ("Rough Opening"). When the window is reset, it computes its unit size (GetOverallWidth / GetOverallHeight) from them: call `Reset()` after the setters. The setters return `False`, and write nothing, for an invalid object, a value that is not a positive finite number, or a parameter that the plug-in style of the window sets (IsParamSetByStyle). Vectorworks measures a window of the Opening configuration as a rough opening, and sizes a window in a curtain wall to its panel, whatever these values say. |
| `GetHeight() -> float \| None` | Returns the height. |
| `SetHeight(value: float) -> bool` | Sets the height. |
| `GetSizeReference() -> str \| None` | What GetWidth / GetHeight measure: "Sash Opening", "Unit Size" or "Rough Opening" (parameter "SizeReference"). SetSizeReference writes the popup only: "Width", "Height" and "Elevation" keep their values, which the window measures in the new reference at its next reset, so the window changes its size (the Object Info palette converts the size instead). Set the size after it. It returns `False`, and writes nothing, for another value or when the style sets the parameter. |
| `SetSizeReference(value: str) -> bool` | Sets the size reference. What GetWidth / GetHeight measure: "Sash Opening", "Unit Size" or "Rough Opening" (parameter "SizeReference"). SetSizeReference writes the popup only: "Width", "Height" and "Elevation" keep their values, which the window measures in the new reference at its next reset, so the window changes its size (the Object Info palette converts the size instead). Set the size after it. It returns `False`, and writes nothing, for another value or when the style sets the parameter. |
| `GetOverallWidth() -> float \| None` | The unit size, as the window computed it at its last reset (parameters "OverallWidth" / "OverallHeight"). SetOverallWidth / SetOverallHeight write the width / height of the current Size Reference that gives the unit size `value` at the next reset: `value` itself for "Unit Size", `value` minus twice the jamb width ("JambWidth") for "Sash Opening". They return `False`, and write nothing, where this is not exact: for "Rough Opening" (the window can take its shim gaps from the wall or from each other), for the height of a "Sash Opening" window with a transom (the transom height depends on the top shape), for a window of the Opening configuration, a corner window, a window in a curtain wall or in a door and window assembly (Vectorworks sizes them itself), for a value that gives no positive size, and where SetWidth / SetHeight return `False`. |
| `SetOverallWidth(value: float) -> bool` | Sets the overall width. The unit size, as the window computed it at its last reset (parameters "OverallWidth" / "OverallHeight"). SetOverallWidth / SetOverallHeight write the width / height of the current Size Reference that gives the unit size `value` at the next reset: `value` itself for "Unit Size", `value` minus twice the jamb width ("JambWidth") for "Sash Opening". They return `False`, and write nothing, where this is not exact: for "Rough Opening" (the window can take its shim gaps from the wall or from each other), for the height of a "Sash Opening" window with a transom (the transom height depends on the top shape), for a window of the Opening configuration, a corner window, a window in a curtain wall or in a door and window assembly (Vectorworks sizes them itself), for a value that gives no positive size, and where SetWidth / SetHeight return `False`. |
| `GetOverallHeight() -> float \| None` | Returns the overall height. |
| `SetOverallHeight(value: float) -> bool` | Sets the overall height. |

*elevation (world units)*

| Method | Description |
|---|---|
| `GetElevation() -> float \| None` | Heights above the layer plane; for a window in a wall, above the layer plane raised by the height of its wall break (normally 0), not above the bottom of the wall. "Elevation" is the raw value of the Object Info palette: the height of the head or of the sill of the window, as "ElevationSetAt" ("Head of Window" or "Sill of Window") says; GetElevation / SetElevation read and write it. GetSillHeight / GetHeadHeight read the sill / the head whatever "ElevationSetAt" says, as the palette converts "Elevation" when the user switches between them: head = sill + Height. SetSillHeight writes "Elevation" for the current "ElevationSetAt" (sill + Height for "Head of Window") with the "Height" of the window at the time of the call: set the height first; it keeps "ElevationSetAt". SetElevation and SetSillHeight return `False`, and write nothing, for a value that is not finite or when the plug-in style sets "Elevation"; SetSillHeight also when "Height" or "ElevationSetAt" cannot be read. |
| `SetElevation(value: float) -> bool` | Sets the elevation. Heights above the layer plane; for a window in a wall, above the layer plane raised by the height of its wall break (normally 0), not above the bottom of the wall. "Elevation" is the raw value of the Object Info palette: the height of the head or of the sill of the window, as "ElevationSetAt" ("Head of Window" or "Sill of Window") says; GetElevation / SetElevation read and write it. GetSillHeight / GetHeadHeight read the sill / the head whatever "ElevationSetAt" says, as the palette converts "Elevation" when the user switches between them: head = sill + Height. SetSillHeight writes "Elevation" for the current "ElevationSetAt" (sill + Height for "Head of Window") with the "Height" of the window at the time of the call: set the height first; it keeps "ElevationSetAt". SetElevation and SetSillHeight return `False`, and write nothing, for a value that is not finite or when the plug-in style sets "Elevation"; SetSillHeight also when "Height" or "ElevationSetAt" cannot be read. |
| `GetElevationSetAt() -> str \| None` | Returns the elevation set at. |
| `GetSillHeight() -> float \| None` | Returns the sill height. |
| `SetSillHeight(value: float) -> bool` | Sets the sill height. |
| `GetHeadHeight() -> float \| None` | Returns the head height. |

*Configuration*

| Method | Description |
|---|---|
| `GetConfiguration() -> str \| None` | Returns the configuration. |
| `GetCasementOperation() -> str \| None` | Returns the casement operation. |
| `GetFixedGlassOperation() -> str \| None` | Returns the fixed glass operation. |
| `GetHungOperation() -> str \| None` | Returns the hung operation. |

*Legacy*

| Method | Description |
|---|---|
| `GetSashOperation() -> str \| None` | Stored as "SashOperation"; superseded by `GetConfiguration()` and the per-type operation getters. |
| `SetSashOperation(value: str) -> bool` | Sets the sash operation. Stored as "SashOperation"; superseded by `GetConfiguration()` and the per-type operation getters. |
| `GetTopShape() -> str \| None` | Returns the top shape. |
| `SetTopShape(value: str) -> bool` | Sets the top shape. |

*Frame / sash*

| Method | Description |
|---|---|
| `GetJambWidth() -> float \| None` | Returns the jamb width. |
| `SetJambWidth(value: float) -> bool` | Sets the jamb width. |
| `GetJambDepth() -> float \| None` | Returns the jamb depth. |
| `SetJambDepth(value: float) -> bool` | Sets the jamb depth. |

*Sill*

| Method | Description |
|---|---|
| `GetIncludeSill() -> bool \| None` | Whether *Include Sill* is on. |
| `SetIncludeSill(value: bool) -> bool` | Turns *Include Sill* on or off. |
| `GetSillStyle() -> str \| None` | Returns the sill style. |
| `SetSillStyle(value: str) -> bool` | Sets the sill style. |

*Scheduling*

| Method | Description |
|---|---|
| `GetOnSchedule() -> bool \| None` | Whether *On Schedule* is on. |
| `SetOnSchedule(value: bool) -> bool` | Turns *On Schedule* on or off. |
| `GetIDLabel() -> str \| None` | Returns the ID label. |
| `SetIDLabel(value: str) -> bool` | Sets the ID label. |
| `GetDescription() -> str \| None` | Returns the description. |
| `SetDescription(value: str) -> bool` | Sets the description. |

*Opening*

| Method | Description |
|---|---|
| `GetInteriorSide() -> str \| None` | Returns the interior side. |
| `GetFlipped() -> bool \| None` | Whether *Flipped* is on. |
| `GetHingeDirection() -> bool \| None` | Whether *Hinge Direction* is on. |
| `GetShow3DOpen() -> bool \| None` | Whether *Show 3D Open* is on. |
| `GetOpenAngle() -> float \| None` | Returns the open angle. |
| `GetAwningOpenDirection() -> str \| None` | Sash hinge and open-direction parameters (popups). |
| `GetCasementHingeSide() -> str \| None` | Returns the casement hinge side. |
| `GetCasementOpenDirection() -> str \| None` | Returns the casement open direction. |
| `GetHopperOpenDirection() -> str \| None` | Returns the hopper open direction. |
| `GetTiltTurnHingeSide() -> str \| None` | Returns the tilt turn hinge side. |
| `GetTiltTurnOpenDirection() -> str \| None` | Returns the tilt turn open direction. |
| `GetVerticalPivotOpensOutToward() -> str \| None` | Returns the vertical pivot opens out toward. |

Inherited: everything from [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### DoorObject

> **Full name:** `api.DoorObject` · **Inherits:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Door plug-in object (universal name "Door") from the Architectural Objects plug-in.

A door inserts into a host wall (`ObjectType.Wall`). It carries frame / leaf / jamb / lintel / threshold / trim / side-light / vision-panel / muntin parameters.

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Overall size and placement

- "Width" — real — size of the door as the Object Info palette shows it, measured as "SizeReference" says (GetWidth / SetWidth)
- "Height" — real — (GetHeight / SetHeight)
- "SizeReference" — popup — Leaf Size / Unit Size / Rough Opening: what "Width" / "Height" measure
- "DoorWidth" — real — leaf size, which the door computes from "Width" / "Height" when it is reset (GetLeafWidth); a value written here is replaced at the reset
- "DoorHeight" — real — (GetLeafHeight)
- "OffsetInWall" — real — horizontal offset from the wall insertion point
- "UseWallDepth" — bool — match the wall thickness for the frame depth
- "TopShape" — popup — Square / Round / Segment / Sloped from Left / Sloped from Right / Gable / Ellipse / Gothic
- "Rise", "Spring" — real — parameters of curved / gabled tops

Configuration

- "Configuration" — popup — Opening / Cased Opening / Barn / Double Acting / Double Egress / Folding / Overhead / Pocket / Sliding / Swing
- "SwingOperation" — popup — Single / Bi-part / Pivot Single / Pivot Double Bi-part (Swing configuration)
- "Operation" — popup — legacy; superseded by "SwingOperation"
- "PlanDetail" — bool
- "DetailLevel" — popup — Low / Medium / High
- "Show3DHinge" — bool
- "DrawWallLines" — bool
- "LW_LS_OverRide" — bool
- "3DOpen" — bool
- "OpenAngle" — real — degrees

Transom

- "Transom" — bool
- "TranMullDepth", "TranMullWidth" — real — transom mullion size
- "TranSashWidth", "TranSashDepth" — real

Jamb

- "JambWidth", "JambDepth" — real
- "AstragalWidth", "AstragalDepth" — real
- "ShimGap" — real
- "MasonMod" — real

Trim

- "IntTrim", "ExtTrim" — bool
- "IntTrimWidth", "IntTrimDepth", "ExtTrimWidth", "ExtTrimDepth" — real

Cavities (frame) counts

- "NumIntComps", "NumExtComps" — int

Scheduling / ID

- "OnSched" — bool
- "IDPrefix", "IDLabel", "IDSuffix" — string
- "IDLabelSize" — real
- "IDLabelShape" — popup — None / Rectangle / Round / Hexagon
- "KeepIDHoriz" — bool
- "ShowIDLeader" — bool
- "UseMarker" — bool

Leaf

- "LeafType" — popup — Solid / Glass / Panel / Custom
- "DoorThickness" — real
- "TopStileWidth", "LRStileWidth", "MidStileWidth", "BottomStileWidth" — real
- "NumPanelsV", "NumPanelsH" — int
- "SetTopPanel" — bool
- "TopPanelHeight" — real

Muntins (on leaf glazing)

- "MuntinStyle" — popup — Colonial / Prairie
- "DoorMuntinWidth" — real
- "DoorVMuntins", "DoorHMuntins" — int
- "Muntins" — bool
- "GlassMuntin" — popup — Colonial / Prairie / Colonial w/Sunburst / Prairie w/ Sunburst / Renaissance
- "NumVMuntins", "NumHMuntins" — int
- "MuntinWidth" — real

Side lights

- "SideLights" — bool
- "LeftLiteWidth", "RightLiteWidth" — real
- "SashWidth", "SashDepth" — real
- "SLMullWidth", "SLMullDepth" — real

Lintel

- "Lintel" — bool
- "IntLintelProt", "ExtLintelProt" — real
- "LintelThick" — real
- "UseLintelAngle" — bool
- "LintelAngle" — real (degrees)
- "UseLintelDrop" — bool
- "LintelDrop" — real
- "LintelClass" — popup — class name

Threshold

- "Threshold" — bool
- "IntTHDepth", "ExtTHDepth", "OverallTHDepth" — real
- "OffJambCenter" — real
- "ThreshThick", "ThreshNose" — real
- "ThresholdClass" — popup — class name

Splays

- "IntSplay", "ExtSplay" — bool
- "UseIntSplayAngle", "UseExtSplayAngle" — bool
- "IntSplayAngle", "ExtSplayAngle" — real (degrees)
- "IntSplayDiag", "ExtSplayDiag" — real
- "UseIntSplayWidth", "UseExtSplayWidth" — bool
- "IntSplayWidth", "ExtSplayWidth" — real
- "IntSplayDepth", "ExtSplayDepth" — real

Symbol substitution (use a symbol as the leaf)

- "UseSymDef" — bool
- "SymbolName" — string — symbol resource name

Line weights / styles (per component)

- "Part", "LWPart" — string — which part is being edited by the OIP
- "JambLW", "JambLS", "TrimLW", "TrimLS", "LeafLW", "LeafLS" — int
- "SwingLW", "SwingLS", "SashLW", "SashLS", "GlassLW", "GlassLS", "AstragalLW", "AstragalLS" — int
- "DetailLW" — int

Classes (per component)

- "PartClass" — popup — class name for the currently selected part
- "IntPanelClass", "ExtPanelClass" — popup — class name
- "IntSRClass", "ExtSRClass" — popup — class name (interior / exterior stiles & rails)
- "IntJambClass", "ExtJambClass" — popup — class name
- "IntTrimClass", "ExtTrimClass" — popup — class name
- "IntSashClass", "ExtSashClass" — popup — class name
- "SwingTrajectory" — popup — class name of the swing arc
- "GlazingClass" — popup — class name
- "SideLGlazingClass" — popup — class name (side-light glazing)

Sizing

- "ROWidth", "ROHeight" — real — rough opening size
- "MOWidth", "MOHeight" — real — masonry opening size
- "NGA" — real — net glass area (read-only)

Metadata (for schedules)

- "Manuf", "Model", "SKU" — string
- "Accessories" — string
- "HeadDetail", "JambDetail", "ThreshDetail" — string
- "FrameFR", "DoorFR" — string — fire ratings
- "Notes" — string
- "UserFld1..UserFld10" — string — user-defined fields

Barn door variant (Configuration = "Barn")

- "BarnShowRail" — popup — None / 2D / 3D / 2D and 3D
- "BarnRailType" — popup — Box / Flat / Round
- "BarnShowRailMounts" — popup — None / 3D
- "BarnBracketType" — popup — None / U / Z
- "BarnShowLeafHangers" — popup — None / 3D
- "BarnHangerMounting" — popup — Leaf Front / Leaf Top

**Constructors**

| Constructor | Description |
|---|---|
| `DoorObject(h: Handle)` | Refers to the existing door `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D) -> DoorObject` *static* | Creates a door at `position`. Typically inserted into a wall via WallObject afterwards. |
| `Duplicate() -> DoorObject` | Duplicates the door in the drawing and returns the copy. |

*size (world units)*

| Method | Description |
|---|---|
| `GetWidth() -> float \| None` | "Width" / "Height" are the size of the door as the Object Info palette shows it, measured as the Size Reference says: the leaf ("Leaf Size"), the unit with its frame ("Unit Size") or the rough opening ("Rough Opening"). When the door is reset, it computes its leaf size (GetLeafWidth / GetLeafHeight) from them: call `Reset()` after the setters. GetWidth / GetHeight read the values the setters write; in earlier builds of this API they read the leaf size, which GetLeafWidth / GetLeafHeight read now. The setters return `False`, and write nothing, for an invalid object, a value that is not a positive finite number, or a parameter that the plug-in style of the door sets (IsParamSetByStyle). Vectorworks measures a door of the Opening configuration as a rough opening, and sizes a door in a curtain wall to its panel, whatever these values say. |
| `SetWidth(value: float) -> bool` | Sets the width. "Width" / "Height" are the size of the door as the Object Info palette shows it, measured as the Size Reference says: the leaf ("Leaf Size"), the unit with its frame ("Unit Size") or the rough opening ("Rough Opening"). When the door is reset, it computes its leaf size (GetLeafWidth / GetLeafHeight) from them: call `Reset()` after the setters. GetWidth / GetHeight read the values the setters write; in earlier builds of this API they read the leaf size, which GetLeafWidth / GetLeafHeight read now. The setters return `False`, and write nothing, for an invalid object, a value that is not a positive finite number, or a parameter that the plug-in style of the door sets (IsParamSetByStyle). Vectorworks measures a door of the Opening configuration as a rough opening, and sizes a door in a curtain wall to its panel, whatever these values say. |
| `GetHeight() -> float \| None` | Returns the height. |
| `SetHeight(value: float) -> bool` | Sets the height. |
| `GetLeafWidth() -> float \| None` | The leaf size, as the door computed it at its last reset (parameters "DoorWidth" / "DoorHeight"). |
| `GetLeafHeight() -> float \| None` | Returns the leaf height. |
| `GetSizeReference() -> str \| None` | What GetWidth / GetHeight measure: "Leaf Size", "Unit Size" or "Rough Opening" (parameter "SizeReference"). SetSizeReference writes the popup only: "Width" and "Height" keep their values, which the door measures in the new reference at its next reset, so the door changes its size (the Object Info palette converts the size instead). Set the size after it. It returns `False`, and writes nothing, for another value or when the style sets the parameter. |
| `SetSizeReference(value: str) -> bool` | Sets the size reference. What GetWidth / GetHeight measure: "Leaf Size", "Unit Size" or "Rough Opening" (parameter "SizeReference"). SetSizeReference writes the popup only: "Width" and "Height" keep their values, which the door measures in the new reference at its next reset, so the door changes its size (the Object Info palette converts the size instead). Set the size after it. It returns `False`, and writes nothing, for another value or when the style sets the parameter. |
| `GetThickness() -> float \| None` | Leaf thickness (world units, parameter "DoorThickness"). |
| `SetThickness(value: float) -> bool` | Sets the thickness. Leaf thickness (world units, parameter "DoorThickness"). |
| `GetConfig() -> str \| None` | Legacy "Config" parameter; `GetConfiguration()` reads the "Configuration" popup. |
| `SetConfig(value: str) -> bool` | Sets the config. Legacy "Config" parameter; `GetConfiguration()` reads the "Configuration" popup. |
| `GetConfiguration() -> str \| None` | Returns the configuration. |
| `GetTopShape() -> str \| None` | Returns the top shape. |
| `SetTopShape(value: str) -> bool` | Sets the top shape. |
| `GetLeafType() -> str \| None` | Returns the leaf type. |
| `SetLeafType(value: str) -> bool` | Sets the leaf type. |

*Scheduling*

| Method | Description |
|---|---|
| `GetOnSchedule() -> bool \| None` | Whether *On Schedule* is on. |
| `SetOnSchedule(value: bool) -> bool` | Turns *On Schedule* on or off. |
| `GetIDLabel() -> str \| None` | Returns the ID label. |
| `SetIDLabel(value: str) -> bool` | Sets the ID label. |
| `GetSwingDirection() -> str \| None` | Opening (leaf swing; SwingOperation, SwingDirection and SwingHingeSide apply to the "Swing" configuration). |
| `GetSwingHingeSide() -> str \| None` | Returns the swing hinge side. |
| `GetInteriorSide() -> str \| None` | Returns the interior side. |
| `GetIsFlipped() -> bool \| None` | Whether *Flipped* is on. |
| `GetOpenAngle() -> float \| None` | Returns the open angle. |
| `GetSwingOperation() -> str \| None` | Returns the swing operation. |

*Legacy*

| Method | Description |
|---|---|
| `GetOperation() -> str \| None` | Stored as "Operation"; superseded by `GetSwingOperation()`. |
| `Get3DOpen() -> bool \| None` | Whether *3D Open* is on. |

Inherited: everything from [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### ColumnObject

> **Full name:** `api.ColumnObject` · **Inherits:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Column plug-in object - the Vectorworks column, universal name "Column2". `Is()` also accepts the legacy "Column" plug-in object of older files, whose parameters may differ. `Create()` creates a Column2, or a legacy Column when only that plug-in is installed.

A column is a vertical structural element with an architectural shaft (rectangular or oval), an optional base and capital, and in Vectorworks Architect an optional structural member (see "Use Component").

Column2 is a scripted plug-in shipped with Vectorworks (Column2.vso; its script is shared with Pilaster2). The parameter names listed below are universal parameter names that the plug-in defines and that the Vectorworks IFC export reads; use the generic GetParam.../SetParam... accessors from ArchitectObject to read / write any of them, and `HasParam()` / `GetParamNames()` to probe an object.

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Components (Vectorworks Architect)

- "Use Component" — popup — Architectural Only / Structural Only / Architectural and Structural

Overall size (world units)

- "OA Height" — real — architectural component height
- "Struct Height" — real — structural component height
- "NewHeight" — real — single-component height input

Architectural shaft (world units)

- "ShaftType" — popup — Rectangular / Oval; there is no Custom shaft type
- "Shaft Width" — real
- "Shaft Depth" — real
- "Shaft Radius" — real — corner radius of a rectangular shaft Round shafts use equal "Shaft Width" and "Shaft Depth" with "ShaftType" = "Oval".
- "Taper" — popup — `None`, or the kind of taper
- "Taper Width", "Taper Depth" — real
- "Arch Offset X", "Arch Offset Y", "Arch Offset Z" — real

Base

- "Use Base" — bool
- "BaseType" — popup
- "Base Height", "Base Width", "Base Depth", "Base Radius" — real
- "Base Divisions" — int

Capital

- "Use Capital" — bool
- "CapitalType" — popup — e.g. Oval Mushroom / Rectangular Mushroom
- "Capital Height", "Capital Width", "Capital Depth", "Capital Radius" — real

Structural member (the steel shape is configured here, not by ShaftType)

- "Struct Type" — popup — e.g. Steel
- "Struct Shape", "Steel Shape" — popup
- "Struct Width", "Struct Depth", "Struct Radius" — real
- "Struct Rotation", "Struct Clearance" — real
- "Use Base Plate", "Use Top Plate" — bool
- "BP Width", "BP Depth", "BP Thickness", "BP Radius" — real — base plate
- "TP Width", "TP Depth", "TP Thickness", "TP Radius" — real — top plate
- "BP Shape", "TP Shape" — popup

Class and identification

- "Arch Class" — popup — class name
- "Column ID" — string

**Constructors**

| Constructor | Description |
|---|---|
| `ColumnObject(h: Handle)` | Refers to the existing column `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D) -> ColumnObject` *static* | Creates a column at `position` in the active layer / current container: a Column2, or a legacy Column when only that plug-in is installed. Returns an invalid object when neither is installed. |
| `Duplicate() -> ColumnObject` | Duplicates the column in the drawing and returns the copy. |
| `GetTotalHeight() -> float \| None` | Height of the active single component (world units): OA Height or Struct Height ("Use Component"). Composite columns (Architectural and Structural) have independently bound components: getter is empty and setter fails. Setter also updates NewHeight and the existing top-bound offset, preserving its reference. |
| `SetTotalHeight(value: float) -> bool` | Sets the total height. Height of the active single component (world units): OA Height or Struct Height ("Use Component"). Composite columns (Architectural and Structural) have independently bound components: getter is empty and setter fails. Setter also updates NewHeight and the existing top-bound offset, preserving its reference. |
| `GetShaftWidth() -> float \| None` | Rectangular shaft (world units). |
| `SetShaftWidth(value: float) -> bool` | Sets the shaft width (Rectangular shaft (world units)). |
| `GetShaftDepth() -> float \| None` | Returns the shaft depth. |
| `SetShaftDepth(value: float) -> bool` | Sets the shaft depth. |
| `GetShaftDiameter() -> float \| None` | Round shaft (world units). Getter is empty for non-circular shafts; setter selects Oval and sets both width and depth to the diameter. |
| `SetShaftDiameter(value: float) -> bool` | Sets the shaft diameter. Round shaft (world units). Getter is empty for non-circular shafts; setter selects Oval and sets both width and depth to the diameter. |
| `GetShape() -> str \| None` | Native shaft shape ("Rectangular" / "Oval"); setter also accepts "Round" as an Oval alias. "Custom" returns `False` without mutation: the native architectural shaft has no Custom mode. |
| `SetShape(value: str) -> bool` | Sets the shape. Native shaft shape ("Rectangular" / "Oval"); setter also accepts "Round" as an Oval alias. "Custom" returns `False` without mutation: the native architectural shaft has no Custom mode. |

Inherited: everything from [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### StairObject

> **Full name:** `api.StairObject` · **Inherits:** [`ArchitectObject`](#architectobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Stair plug-in object - the Vectorworks stair, universal name "Stairs CW".

Stairs CW keeps its configuration (shape, flights, landings, widths, railings) in its own settings and mirrors its main values in the parameters below. On each reset it reads TotalRise, Orientation, UpperLayer and the plan display parameters back, as well as WalkLineLength, TreadLength, RiserHeight and NumberOfRisers when they are positive, recalculates the stair and writes the values it calculated. So set the values, call `Reset()` and read the recalculated values back. It does not read StairWidth back.

Older stair objects are not supported: Vectorworks translates the pre-2010 "Stair" object to "Simple Stair" or "Custom Stair" when it opens a file, and installs no "Stair2" plug-in. Use ParametricObject for them.

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Main values (world units)

- "TotalRise" — real — height of the stair (top minus bottom elevation)
- "WalkLineLength" — real — length of the walking line (the total run)
- "StairWidth" — real — the first stair width; calculated, not read back
- "TreadLength" — real — tread depth (going)
- "RiserHeight" — real
- "NumberOfRisers" — int
- "Orientation" — popup — RightHand / LeftHand
- "UpperLayer" — popup — layer name of the upper floor

Calculated quantities (written on each reset)

- "StairArea" — real — area
- "NosingLength", "TreadLengthAtOffset" — real
- "Flight1Length" ... "Flight4Length" — real — walking line length of each flight
- "Flight1WalkingLineOffset" ... "Flight4WalkingLineOffset" — real
- "Flight1NumberOfRiser" ... "Flight4NumberOfRiser" — int
- "Flight1NumberOfTreads" ... "Flight4NumberOfTreads" — int

Plan display: each name exists for both detail levels, ending in Detailed or Schematic

- "BreakModeLowerFloorDetailed" — popup — NoBreak / SolidSolid / SolidNone / NoneSolid / SolidDashed / DashedSolid / NoneDashed / DashedNone
- "BreakElevationDetailed" — real
- "BreakLineAngleDetailed" — real — degrees
- "BreakLinesSeparationMMDetailed" — real — millimeters
- "ShowGuardrailOfInsideRailingDetailed" — bool
- "ShowGuardrailOfOutsideRailingDetailed" — bool

Internal

- "ControlPoint01X" ... "ControlPoint14Y" — real — positions of the text labels
- "InternalVersionNumberOfRecordFormat" — int

**Constructors**

| Constructor | Description |
|---|---|
| `StairObject(h: Handle)` | Refers to the existing stair `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D) -> StairObject` *static* | Creates a Stairs CW stair, in its default configuration, at `position` in the active layer / current container. Returns an invalid object when the plug-in is not installed. |
| `Duplicate() -> StairObject` | Duplicates the stair in the drawing and returns the copy. |
| `GetTotalRun() -> float \| None` | Overall geometry (world units): TotalRun is "WalkLineLength", TotalRise "TotalRise", StairWidth "StairWidth", TreadDepth "TreadLength" and RiserHeight "RiserHeight". The setters take positive values and the stair applies them on `Reset()`. StairWidth is the first stair width, which Stairs CW does not read back: SetStairWidth returns `False`. |
| `SetTotalRun(value: float) -> bool` | Sets the total run. Overall geometry (world units): TotalRun is "WalkLineLength", TotalRise "TotalRise", StairWidth "StairWidth", TreadDepth "TreadLength" and RiserHeight "RiserHeight". The setters take positive values and the stair applies them on `Reset()`. StairWidth is the first stair width, which Stairs CW does not read back: SetStairWidth returns `False`. |
| `GetTotalRise() -> float \| None` | Returns the total rise. |
| `SetTotalRise(value: float) -> bool` | Sets the total rise. |
| `GetStairWidth() -> float \| None` | Returns the stair width. |
| `SetStairWidth(value: float) -> bool` | Sets the stair width. |
| `GetTreadDepth() -> float \| None` | Returns the tread depth. |
| `SetTreadDepth(value: float) -> bool` | Sets the tread depth. |
| `GetRiserHeight() -> float \| None` | Returns the riser height. |
| `SetRiserHeight(value: float) -> bool` | Sets the riser height. |
| `GetNumTreads() -> int \| None` | Counts. NumRisers is "NumberOfRisers" (1 to 32767). Stairs CW has no overall tread count: GetNumTreads is empty and SetNumTreads returns `False`. |
| `SetNumTreads(value: int) -> bool` | Sets the num treads. Counts. NumRisers is "NumberOfRisers" (1 to 32767). Stairs CW has no overall tread count: GetNumTreads is empty and SetNumTreads returns `False`. |
| `GetNumRisers() -> int \| None` | Returns the num risers. |
| `SetNumRisers(value: int) -> bool` | Sets the num risers. |

*Configuration and handrails*

| Method | Description |
|---|---|
| `GetConfiguration() -> str \| None` | Stairs CW keeps them in its settings, not in parameters. The getters are empty and the setters return `False`. |
| `SetConfiguration(value: str) -> bool` | Sets the configuration. Stairs CW keeps them in its settings, not in parameters. The getters are empty and the setters return `False`. |
| `GetHandrailLeft() -> bool \| None` | Handrails (see above). |
| `SetHandrailLeft(value: bool) -> bool` | Turns *Handrail Left* on or off (Handrails (see above)). |
| `GetHandrailRight() -> bool \| None` | Whether *Handrail Right* is on. |
| `SetHandrailRight(value: bool) -> bool` | Turns *Handrail Right* on or off. |

Inherited: everything from [`ArchitectObject`](#architectobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

---

[Back to the index](README.md) · [Back to top](#objectsarchitect--walls-roofs-slabs-windows-doors-columns-stairs)
