**English** • [Deutsch](../../PythonAPI.de/v2027.2/Attributes.md) • [日本語](../../PythonAPI.ja/v2027.2/Attributes.md)

# Attributes — graphic attributes and classes

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The attribute classes describe how objects look. `ObjectAttributes` gathers all graphic attributes of one object (`Pen()`, `Fill()`, `FillMapping()`, `Markers()`, `DropShadow()`); `PenAttributes` covers the stroke (colors, style, line weight, opacity), `FillAttributes` the fill (colors, style, opacity), `FillMappingAttributes` the mapping of hatch, tile, gradient and image fills, `MarkerAttributes` the beginning and end markers and `DropShadowAttributes` the drop shadow. `ClassAttributes` represents a class definition: a named, saved set of attributes shared by many objects.

The value types `ColorRGB`, `ColorPair`, `ObjectColors`, `Marker`, `DropShadow`, `WallTextures`, `RoofTextures` and `Point2D`, the attribute enumerations and the module constant `api.kMaxOpacity` belong to this group as well.

**"By class":** an attribute set "by class" ignores the object's own value and uses the value of the class the object belongs to. Query and change it with the `Get...ByClass` / `Set...ByClass` methods of the attribute classes.

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [Point2D](#point2d)
  - [ColorRGB](#colorrgb)
  - [ColorPair](#colorpair)
  - [ObjectColors](#objectcolors)
  - [Marker](#marker)
  - [DropShadow](#dropshadow)
  - [WallTextures](#walltextures)
  - [RoofTextures](#rooftextures)
  - [AttributesBase](#attributesbase)
  - [PenAttributes](#penattributes)
  - [FillAttributes](#fillattributes)
  - [FillMappingAttributes](#fillmappingattributes)
    - [FillMappingAttributes.Frame](#fillmappingattributesframe)
  - [MarkerAttributes](#markerattributes)
  - [DropShadowAttributes](#dropshadowattributes)
  - [ClassAttributes](#classattributes)
  - [ObjectAttributes](#objectattributes)
- [Enumerations](#enumerations)
  - [PenStyleKind](#penstylekind)
  - [FillType](#filltype)
  - [MarkerShape](#markershape)
  - [MarkerFill](#markerfill)
  - [MarkerBase](#markerbase)
  - [MarkerHalfTick](#markerhalftick)
  - [MarkerThicknessBasis](#markerthicknessbasis)
  - [MarkerThicknessUnits](#markerthicknessunits)
  - [DropShadowUnits](#dropshadowunits)
  - [ClassVisibility](#classvisibility)
  - [ObjectType](#objecttype)
- [Module constants](#module-constants)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`Point2D`](#point2d) | class |  | Plain 2D point record (`x`, `y` in world units) used by the dialog and attribute APIs. |
| [`ColorRGB`](#colorrgb) | class |  | RGB color with 16 bits per channel (0 .. |
| [`ColorPair`](#colorpair) | class |  | Foreground and background colors of a pen or a fill, as color indices. |
| [`ObjectColors`](#objectcolors) | class |  | All four object colors (pen fore/back, fill fore/back), as color indices. |
| [`Marker`](#marker) | class |  | Marker (arrow head) at the beginning or end of a line: shape, fill, base, half tick, tail, angle (degrees), length and width (page inches) and line thickness... |
| [`DropShadow`](#dropshadow) | class |  | Drop shadow settings of an object, a class or the document: on/off, units, offset, blur radius, angle, color and opacity. |
| [`WallTextures`](#walltextures) | class |  | Wall textures of a class (internal indices of texture resources, 0 = none). |
| [`RoofTextures`](#rooftextures) | class |  | Roof textures of a class (internal indices of texture resources, 0 = none). |
| [`AttributesBase`](#attributesbase) | class |  | Common base of the graphical attribute classes. |
| [`PenAttributes`](#penattributes) | class | [`AttributesBase`](#attributesbase) | Pen (stroke) attributes of an object: colors, style (pattern / line type), line weight, opacity, by-class flags and the line type mapping (pen space). |
| [`FillAttributes`](#fillattributes) | class | [`AttributesBase`](#attributesbase) | Fill attributes of an object: colors, style (pattern / hatch / tile / gradient / image), opacity and by-class flags. |
| [`FillMappingAttributes`](#fillmappingattributes) | class | [`AttributesBase`](#attributesbase) | Mapping of hatch, tile, gradient and image fills (fill space): origin, axes, offsets, rotation, repeat, mirror and flip. |
| [`FillMappingAttributes.Frame`](#fillmappingattributesframe) | class (nested) |  | Mapping frame of a hatch, tile, gradient or image fill: the origin and the end points of the I and J axes. |
| [`MarkerAttributes`](#markerattributes) | class | [`AttributesBase`](#attributesbase) | Beginning and end markers (arrow heads) of an object. |
| [`DropShadowAttributes`](#dropshadowattributes) | class | [`AttributesBase`](#attributesbase) | Drop shadow of an object. |
| [`ClassAttributes`](#classattributes) | class | [`AttributesBase`](#attributesbase) | A class definition (`ObjectType.ClassDefinition`): a named, saved configuration of attributes. |
| [`ObjectAttributes`](#objectattributes) | class | [`AttributesBase`](#attributesbase) | All graphical attributes of an object. |
| [`PenStyleKind`](#penstylekind) | IntEnum |  | Classification of a raw pen style value. |
| [`FillType`](#filltype) | IntEnum |  | Kind of the fill of an object. |
| [`MarkerShape`](#markershape) | IntEnum |  | Markers (arrow heads) |
| [`MarkerFill`](#markerfill) | IntEnum |  | The marker style enumerations below (MarkerFill, MarkerBase, MarkerHalfTick) use pre-shifted values so they can be bitwise-OR'd into a single 16-bit style... |
| [`MarkerBase`](#markerbase) | IntEnum |  | Shape of the base of a marker (pre-shifted bit values, see `Marker.GetStyleValue`). |
| [`MarkerHalfTick`](#markerhalftick) | IntEnum |  | Whole marker, or only its left or right half (pre-shifted bit values, see `Marker.GetStyleValue`). |
| [`MarkerThicknessBasis`](#markerthicknessbasis) | IntEnum |  | What the line thickness of a marker follows. |
| [`MarkerThicknessUnits`](#markerthicknessunits) | IntEnum |  | Units of a custom marker line thickness. |
| [`DropShadowUnits`](#dropshadowunits) | IntEnum |  | Drop shadow |
| [`ClassVisibility`](#classvisibility) | IntEnum |  | Classes |
| [`ObjectType`](#objecttype) | IntEnum |  | Type of an object. |
| [Module constants](#module-constants) | constants | | `kMaxOpacity` |

## Classes

### Point2D

> **Full name:** `api.Point2D` · **Inherits:** `api.Object`

Plain 2D point record (`x`, `y` in world units) used by the dialog and attribute APIs. It converts implicitly to and from `api.Math.Point2D`, which has the full vector math.

**Constructors**

| Constructor | Description |
|---|---|
| `Point2D()` | Default value (fields at their defaults). |
| `Point2D(x, y)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: Point2D) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: Point2D) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `x` | `float` | X coordinate (world units). |
| `y` | `float` | Y coordinate (world units). |

### ColorRGB

> **Full name:** `api.ColorRGB` · **Inherits:** `api.Object`

RGB color with 16 bits per channel (0 .. 65535), lossless with the Vectorworks color representation.

**Constructors**

| Constructor | Description |
|---|---|
| `ColorRGB()` | Default value (fields at their defaults). |
| `ColorRGB(red, green, blue)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Methods**

| Method | Description |
|---|---|
| `FromRGB8(r: int, g: int, b: int) -> ColorRGB` *static* | Creates a color from 8-bit channels (0 .. 255 each). |
| `Red8() -> int` | Red channel scaled to 8 bits (0 .. 255). |
| `Green8() -> int` | Green channel scaled to 8 bits (0 .. 255). |
| `Blue8() -> int` | Blue channel scaled to 8 bits (0 .. 255). |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: ColorRGB) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: ColorRGB) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `red` | `int` | Red channel (0 .. 65535). |
| `green` | `int` | Green channel (0 .. 65535). |
| `blue` | `int` | Blue channel (0 .. 65535). |

### ColorPair

> **Full name:** `api.ColorPair` · **Inherits:** `api.Object`

Foreground and background colors of a pen or a fill, as color indices.

**Constructors**

| Constructor | Description |
|---|---|
| `ColorPair()` | Default value (fields at their defaults). |
| `ColorPair(fore, back)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: ColorPair) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: ColorPair) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fore` | `int` | Foreground color (color index). |
| `back` | `int` | Background color (color index). |

### ObjectColors

> **Full name:** `api.ObjectColors` · **Inherits:** `api.Object`

All four object colors (pen fore/back, fill fore/back), as color indices.

**Constructors**

| Constructor | Description |
|---|---|
| `ObjectColors()` | Default value (fields at their defaults). |
| `ObjectColors(pen, fill)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: ObjectColors) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: ObjectColors) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `pen` | `ColorPair` | Pen foreground / background colors. |
| `fill` | `ColorPair` | Fill foreground / background colors. |

### Marker

> **Full name:** `api.Marker` · **Inherits:** `api.Object`

Marker (arrow head) at the beginning or end of a line: shape, fill, base, half tick, tail, angle (degrees), length and width (page inches) and line thickness settings.

**Constructors**

| Constructor | Description |
|---|---|
| `Marker()` | Default value (fields at their defaults). |
| `Marker(shape, fill, base, halfTick, tail, angle, length, width, thicknessBasis, thicknessUnits, thickness, visible)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Methods**

| Method | Description |
|---|---|
| `GetStyleValue() -> int` | Packed marker style value (shape \| fill \| base \| half tick \| tail). |
| `SetStyleValue(value: int) -> None` | Sets the style value. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: Marker) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: Marker) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `shape` | `MarkerShape` | Shape of the marker. |
| `fill` | `MarkerFill` | Fill of the marker. |
| `base` | `MarkerBase` | Shape of the marker base. |
| `halfTick` | `MarkerHalfTick` | Whole marker, or only its left or right half. |
| `tail` | `bool` | Whether the marker has a tail. |
| `angle` | `int` | Degrees. |
| `length` | `float` | Page inches. |
| `width` | `float` | Page inches. |
| `thicknessBasis` | `MarkerThicknessBasis` | What the marker line thickness follows: the line, the dimension standard or `thickness`. |
| `thicknessUnits` | `MarkerThicknessUnits` | Units of `thickness`. |
| `thickness` | `float` | Used with `MarkerThicknessBasis.Custom`, in thicknessUnits. |
| `visible` | `bool` | Whether the marker is shown. |

### DropShadow

> **Full name:** `api.DropShadow` · **Inherits:** `api.Object`

Drop shadow settings of an object, a class or the document: on/off, units, offset, blur radius, angle, color and opacity.

**Constructors**

| Constructor | Description |
|---|---|
| `DropShadow()` | Default value (fields at their defaults). |
| `DropShadow(useDropShadow, units, offset, blurRadius, angle, color, opacity)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: DropShadow) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: DropShadow) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `useDropShadow` | `bool` | Whether the drop shadow is on. |
| `units` | `DropShadowUnits` | Whether `offset` and `blurRadius` are page or world lengths. |
| `offset` | `float` | Distance of the shadow from the object. |
| `blurRadius` | `float` | Blur radius of the shadow. |
| `angle` | `float` | Degrees. |
| `color` | `int` | Shadow color (color index). |
| `opacity` | `int` | Shadow opacity (0 .. 100). |

### WallTextures

> **Full name:** `api.WallTextures` · **Inherits:** `api.Object`

Wall textures of a class (internal indices of texture resources, 0 = none).

**Constructors**

| Constructor | Description |
|---|---|
| `WallTextures()` | Default value (fields at their defaults). |
| `WallTextures(right, left, center)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: WallTextures) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: WallTextures) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `right` | `int` | Texture of the right side (texture index, 0 = none). |
| `left` | `int` | Texture of the left side (texture index, 0 = none). |
| `center` | `int` | Texture of the wall center (texture index, 0 = none). |

### RoofTextures

> **Full name:** `api.RoofTextures` · **Inherits:** `api.Object`

Roof textures of a class (internal indices of texture resources, 0 = none).

**Constructors**

| Constructor | Description |
|---|---|
| `RoofTextures()` | Default value (fields at their defaults). |
| `RoofTextures(top, edge, dormer)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: RoofTextures) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: RoofTextures) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `top` | `int` | Texture of the roof top (texture index, 0 = none). |
| `edge` | `int` | Texture of the roof edges (texture index, 0 = none). |
| `dormer` | `int` | Texture of the dormers (texture index, 0 = none). |

### AttributesBase

> **Full name:** `api.AttributesBase` · **Inherits:** `api.Object`

Common base of the graphical attribute classes. An instance does not own the object; it only reads and writes the attributes of the object. Getters return `None` when the handle is null or the object does not support the attribute. Setters return `False` when the handle is null or the object does not support the attribute.

**Constructors**

| Constructor | Description |
|---|---|
| `AttributesBase(h: Handle)` | Refers to the existing attributes base `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `GetHandle() -> Handle` | Handle of the attributes base. |
| `IsValid() -> bool` | True when this object refers to an existing attributes base. |
| `GetObjectType() -> ObjectType` | Returns the object type. |
| `IsGroup() -> bool` | True when the object is a group (its attributes apply to the objects inside). |
| `GetObjectColors() -> ObjectColors \| None` | All four colors at once (pen fore/back, fill fore/back). |
| `SetObjectColors(colors: ObjectColors) -> bool` | Sets the object colors. All four colors at once (pen fore/back, fill fore/back). |
| `ColorIndexToRGB(index: int) -> ColorRGB` *static* | RGB color of the color index `index` of the document color table. |
| `RGBToColorIndex(color: ColorRGB) -> int` *static* | Index of the document color table entry closest to `color`. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True when the object is valid (same as `IsValid()`). |

### PenAttributes

> **Full name:** `api.PenAttributes` · **Inherits:** [`AttributesBase`](#attributesbase) → `api.Object`

Pen (stroke) attributes of an object: colors, style (pattern / line type), line weight, opacity, by-class flags and the line type mapping (pen space).

**Constructors**

| Constructor | Description |
|---|---|
| `PenAttributes(h: Handle)` | Refers to the existing pen `h`; check `IsValid()` before use. |

**Methods**

*Colors*

| Method | Description |
|---|---|
| `GetForeColor() -> ColorRGB \| None` | Returns the fore color. |
| `SetForeColor(color: ColorRGB) -> bool` | Sets the fore color. |
| `GetBackColor() -> ColorRGB \| None` | Returns the back color. |
| `SetBackColor(color: ColorRGB) -> bool` | Sets the back color. |
| `GetForeColorIndex() -> int \| None` | Returns the fore color index. |
| `SetForeColorIndex(index: int) -> bool` | Sets the fore color index. |
| `GetBackColorIndex() -> int \| None` | Returns the back color index. |
| `SetBackColorIndex(index: int) -> bool` | Sets the back color index. |
| `GetColors() -> ColorPair \| None` | Returns the colors. |
| `SetColors(colors: ColorPair) -> bool` | Sets the colors. |
| `GetColorsByClass() -> bool \| None` | Whether *Colors By Class* is on. |
| `SetColorsByClass() -> bool` | Sets the colors by class. |
| `GetStyle() -> int \| None` | Style. Raw value: 0 none, 1-2 solid, > 2 legacy pattern, < 0 -(internal index of a line type). |
| `SetStyle(style: int) -> bool` | Sets the style. Style. Raw value: 0 none, 1-2 solid, > 2 legacy pattern, < 0 -(internal index of a line type). |
| `GetStyleKind() -> PenStyleKind \| None` | Returns the style kind. |
| `GetNone() -> bool \| None` | Whether *None* is on. |
| `SetNone() -> bool` | Sets the none (applied recursively to group members). |
| `GetSolid() -> bool \| None` | Whether *Solid* is on. |
| `SetSolid() -> bool` | Sets the solid (applied recursively to group members). |
| `GetLineType() -> int \| None` | Line type internal index (positive), empty if the pen is not a line type. |
| `SetLineType(lineTypeIndex: int) -> bool` | Sets the line type. Line type internal index (positive), empty if the pen is not a line type. |
| `GetStyleByClass() -> bool \| None` | Whether *Style By Class* is on. |
| `SetStyleByClass() -> bool` | Sets the style by class. |

*Line weight*

| Method | Description |
|---|---|
| `GetLineWeightMils() -> int \| None` | Returns the line weight mils. |
| `SetLineWeightMils(mils: int) -> bool` | Sets the line weight mils. |
| `GetLineWeightMillimeters() -> float \| None` | Returns the line weight millimeters. |
| `SetLineWeightMillimeters(mm: float) -> bool` | Sets the line weight millimeters. |
| `GetLineWeightByClass() -> bool \| None` | Whether *Line Weight By Class* is on. |
| `SetLineWeightByClass() -> bool` | Sets the line weight by class. |

*Opacity*

| Method | Description |
|---|---|
| `GetOpacity() -> int \| None` | Returns the opacity. |
| `SetOpacity(opacity: int) -> bool` | Sets the opacity. |
| `GetOpacityByClass() -> bool \| None` | Whether *Opacity By Class* is on. |
| `SetOpacityByClass(byClass: bool) -> bool` | Turns *Opacity By Class* on or off. |
| `IsMappingExisting() -> bool` | Line type mapping (pen space). |
| `GetLocalMapping() -> bool \| None` | Whether *Local Mapping* is on. |
| `SetLocalMapping(local: bool) -> bool` | Turns *Local Mapping* on or off. |
| `GetFlipHorizontal() -> bool \| None` | Whether *Flip Horizontal* is on. |
| `SetFlipHorizontal(flip: bool) -> bool` | Turns *Flip Horizontal* on or off. |
| `GetFlipVertical() -> bool \| None` | Whether *Flip Vertical* is on. |
| `SetFlipVertical(flip: bool) -> bool` | Turns *Flip Vertical* on or off. |
| `GetScale() -> float \| None` | Returns the scale. |
| `SetScale(scale: float) -> bool` | Sets the scale. |

Inherited: everything from [`AttributesBase`](#attributesbase).

### FillAttributes

> **Full name:** `api.FillAttributes` · **Inherits:** [`AttributesBase`](#attributesbase) → `api.Object`

Fill attributes of an object: colors, style (pattern / hatch / tile / gradient / image), opacity and by-class flags. The fill mapping (origin, scale, rotation ...) is in FillMappingAttributes.

**Constructors**

| Constructor | Description |
|---|---|
| `FillAttributes(h: Handle)` | Refers to the existing fill `h`; check `IsValid()` before use. |

**Methods**

*Colors*

| Method | Description |
|---|---|
| `GetForeColor() -> ColorRGB \| None` | Returns the fore color. |
| `SetForeColor(color: ColorRGB) -> bool` | Sets the fore color. |
| `GetBackColor() -> ColorRGB \| None` | Returns the back color. |
| `SetBackColor(color: ColorRGB) -> bool` | Sets the back color. |
| `GetForeColorIndex() -> int \| None` | Returns the fore color index. |
| `SetForeColorIndex(index: int) -> bool` | Sets the fore color index. |
| `GetBackColorIndex() -> int \| None` | Returns the back color index. |
| `SetBackColorIndex(index: int) -> bool` | Sets the back color index. |
| `GetColors() -> ColorPair \| None` | Returns the colors. |
| `SetColors(colors: ColorPair) -> bool` | Sets the colors. |
| `GetColorsByClass() -> bool \| None` | Whether *Colors By Class* is on. |
| `SetColorsByClass() -> bool` | Sets the colors by class. |
| `GetStyle() -> int \| None` | Style. Raw value: 0 none, 1 solid, > 1 legacy pattern, < 0 -(internal index of a hatch, tile, gradient or image resource). |
| `SetStyle(style: int) -> bool` | Sets the style. Style. Raw value: 0 none, 1 solid, > 1 legacy pattern, < 0 -(internal index of a hatch, tile, gradient or image resource). |
| `GetType() -> FillType \| None` | Returns the type. |
| `GetNone() -> bool \| None` | Whether *None* is on. |
| `SetNone() -> bool` | Sets the none (applied recursively to group members). |
| `GetSolid() -> bool \| None` | Whether *Solid* is on. |
| `SetSolid() -> bool` | Sets the solid (applied recursively to group members). |
| `GetResource() -> int \| None` | Internal index (positive) of the hatch, tile, gradient or image resource; empty if the fill does not use a resource. |
| `SetResource(resourceIndex: int) -> bool` | Sets the resource. Internal index (positive) of the hatch, tile, gradient or image resource; empty if the fill does not use a resource. |
| `GetStyleByClass() -> bool \| None` | Whether *Style By Class* is on. |
| `SetStyleByClass() -> bool` | Sets the style by class. |

*Opacity*

| Method | Description |
|---|---|
| `GetOpacity() -> int \| None` | Returns the opacity. |
| `SetOpacity(opacity: int) -> bool` | Sets the opacity. |
| `GetOpacityByClass() -> bool \| None` | Whether *Opacity By Class* is on. |
| `SetOpacityByClass(byClass: bool) -> bool` | Turns *Opacity By Class* on or off. |

Inherited: everything from [`AttributesBase`](#attributesbase).

### FillMappingAttributes

> **Full name:** `api.FillMappingAttributes` · **Inherits:** [`AttributesBase`](#attributesbase) → `api.Object`

Mapping of hatch, tile, gradient and image fills (fill space): origin, axes, offsets, rotation, repeat, mirror and flip. Getters return empty when the object has no fill mapping; setters create the mapping if needed.

**Constructors**

| Constructor | Description |
|---|---|
| `FillMappingAttributes(h: Handle)` | Refers to the existing fill mapping `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `IsMappingExisting() -> bool` | True when the object has its own fill mapping data. |

*Mapping frame, in world coordinates*

| Method | Description |
|---|---|
| `GetOriginPoint() -> Point2D \| None` | Returns the origin point. |
| `SetOriginPoint(pt: Point2D) -> bool` | Sets the origin point. |
| `GetIAxisEndPoint() -> Point2D \| None` | Returns the I axis end point. |
| `SetIAxisEndPoint(pt: Point2D) -> bool` | Sets the I axis end point. |
| `GetJAxisEndPoint() -> Point2D \| None` | Returns the J axis end point. |
| `SetJAxisEndPoint(pt: Point2D) -> bool` | Sets the J axis end point. |
| `GetFrame() -> FillMappingAttributes.Frame \| None` | Returns the frame. |
| `SetFrame(frame: FillMappingAttributes.Frame) -> bool` | Sets the frame. |

*Offset and axis lengths, in internal units*

| Method | Description |
|---|---|
| `GetXOffset() -> float \| None` | Returns the X offset. |
| `SetXOffset(value: float) -> bool` | Sets the X offset. |
| `GetYOffset() -> float \| None` | Returns the Y offset. |
| `SetYOffset(value: float) -> bool` | Sets the Y offset. |
| `GetIAxisLength() -> float \| None` | Returns the I axis length. |
| `SetIAxisLength(value: float) -> bool` | Sets the I axis length. |
| `GetJAxisLength() -> float \| None` | Returns the J axis length. |
| `SetJAxisLength(value: float) -> bool` | Sets the J axis length. |
| `GetXOffsetInCurrentUnits() -> float \| None` | Offset and axis lengths, in the document current units. |
| `SetXOffsetInCurrentUnits(value: float) -> bool` | Sets the X offset in current units (Offset and axis lengths, in the document current units). |
| `GetYOffsetInCurrentUnits() -> float \| None` | Returns the Y offset in current units. |
| `SetYOffsetInCurrentUnits(value: float) -> bool` | Sets the Y offset in current units. |
| `GetIAxisLengthInCurrentUnits() -> float \| None` | Returns the I axis length in current units. |
| `SetIAxisLengthInCurrentUnits(value: float) -> bool` | Sets the I axis length in current units. |
| `GetJAxisLengthInCurrentUnits() -> float \| None` | Returns the J axis length in current units. |
| `SetJAxisLengthInCurrentUnits(value: float) -> bool` | Sets the J axis length in current units. |
| `GetAngle() -> float \| None` | Rotation of the mapping about its origin, in radians. |
| `SetAngle(radians: float) -> bool` | Sets the angle (Rotation of the mapping about its origin, in radians). |
| `GetRepeat() -> bool \| None` | Whether *Repeat* is on. |
| `SetRepeat(repeat: bool) -> bool` | Turns *Repeat* on or off. |
| `GetMirror() -> bool \| None` | Whether *Mirror* is on. |
| `SetMirror(mirror: bool) -> bool` | Turns *Mirror* on or off. |
| `GetFlip() -> bool \| None` | Whether *Flip* is on. |
| `SetFlip(flip: bool) -> bool` | Turns *Flip* on or off. |
| `GetMaintainAspectRatio() -> bool \| None` | Whether *Maintain Aspect Ratio* is on. |
| `SetMaintainAspectRatio(maintain: bool) -> bool` | Turns *Maintain Aspect Ratio* on or off. |

*Gradient geometry type (linear, radial, ...)*

| Method | Description |
|---|---|
| `GetGeometryType() -> int \| None` | Returns the geometry type. |
| `SetGeometryType(type: int) -> bool` | Sets the geometry type. |

*Local (object relative) vs. world mapping*

| Method | Description |
|---|---|
| `GetLocalMapping() -> bool \| None` | Whether *Local Mapping* is on. |
| `SetLocalMapping(local: bool) -> bool` | Turns *Local Mapping* on or off. |

Inherited: everything from [`AttributesBase`](#attributesbase).

#### FillMappingAttributes.Frame

> **Full name:** `api.FillMappingAttributes.Frame` · **Inherits:** `api.Object`

Mapping frame of a hatch, tile, gradient or image fill: the origin and the end points of the I and J axes.

**Constructors**

| Constructor | Description |
|---|---|
| `Frame()` | Default value (fields at their defaults). |
| `Frame(origin, iAxisEnd, jAxisEnd)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `origin` | `Point2D` | Origin of the mapping. |
| `iAxisEnd` | `Point2D` | End point of the I axis (from the origin). |
| `jAxisEnd` | `Point2D` | End point of the J axis (from the origin). |

### MarkerAttributes

> **Full name:** `api.MarkerAttributes` · **Inherits:** [`AttributesBase`](#attributesbase) → `api.Object`

Beginning and end markers (arrow heads) of an object.

**Constructors**

| Constructor | Description |
|---|---|
| `MarkerAttributes(h: Handle)` | Refers to the existing marker `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `GetBeginningMarker() -> Marker \| None` | Returns the beginning marker. |
| `SetBeginningMarker(marker: Marker) -> bool` | Sets the beginning marker. |
| `GetEndMarker() -> Marker \| None` | Returns the end marker. |
| `SetEndMarker(marker: Marker) -> bool` | Sets the end marker. |
| `GetBeginningMarkerVisible() -> bool \| None` | Whether *Beginning Marker Visible* is on. |
| `SetBeginningMarkerVisible(visible: bool) -> bool` | Turns *Beginning Marker Visible* on or off. |
| `GetEndMarkerVisible() -> bool \| None` | Whether *End Marker Visible* is on. |
| `SetEndMarkerVisible(visible: bool) -> bool` | Turns *End Marker Visible* on or off. |
| `GetByClass() -> bool \| None` | Whether *By Class* is on. |
| `SetByClass() -> bool` | Sets the by class. |

Inherited: everything from [`AttributesBase`](#attributesbase).

### DropShadowAttributes

> **Full name:** `api.DropShadowAttributes` · **Inherits:** [`AttributesBase`](#attributesbase) → `api.Object`

Drop shadow of an object.

**Constructors**

| Constructor | Description |
|---|---|
| `DropShadowAttributes(h: Handle)` | Refers to the existing drop shadow `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `GetEnabled() -> bool \| None` | Whether *Enabled* is on. |
| `SetEnabled(enable: bool) -> bool` | Turns *Enabled* on or off. |
| `GetData() -> DropShadow \| None` | Object specific drop shadow data; empty if the object has none. |
| `SetData(data: DropShadow) -> bool` | Sets the data. Object specific drop shadow data; empty if the object has none. |
| `DeleteData() -> bool` | Removes the object specific drop shadow data (the object then has no own drop shadow). |
| `GetByClass() -> bool \| None` | Whether *By Class* is on. |
| `SetByClass(byClass: bool) -> bool` | Turns *By Class* on or off. |
| `GetColor() -> ColorRGB \| None` | Convenience accessors on top of GetData / SetData. |
| `SetColor(color: ColorRGB) -> bool` | Sets the color (Convenience accessors on top of GetData / SetData). |
| `GetOpacity() -> int \| None` | Returns the opacity. |
| `SetOpacity(opacity: int) -> bool` | Sets the opacity. |

Inherited: everything from [`AttributesBase`](#attributesbase).

### ClassAttributes

> **Full name:** `api.ClassAttributes` · **Inherits:** [`AttributesBase`](#attributesbase) → `api.Object`

A class definition (`ObjectType.ClassDefinition`): a named, saved configuration of attributes. Objects assigned to a class use its attributes for every attribute set "by class" (see the SetXxxByClass methods of PenAttributes, FillAttributes, MarkerAttributes, DropShadowAttributes and `ObjectAttributes.SetAllByClass`). Constructing from a handle that is not a class definition produces an invalid object (`IsValid()` == `False`). Strings are UTF-8.

**Constructors**

| Constructor | Description |
|---|---|
| `ClassAttributes(hClassDefinition: Handle)` | Refers to the existing class `hClassDefinition`; check `IsValid()` before use. |

**Methods**

*Lookup and creation*

| Method | Description |
|---|---|
| `FromIndex(classIndex: int) -> ClassAttributes` *static* | The class with the internal index `classIndex`. |
| `FromName(name: str) -> ClassAttributes` *static* | The class named `name`; an invalid object when there is none. |
| `OfObject(hObject: Handle) -> ClassAttributes` *static* | The class of the object `hObject`. |
| `Create(name: str) -> ClassAttributes` *static* | Creates a class named `name`; returns the existing class if the name is taken. |
| `GetNoneClass() -> ClassAttributes` *static* | Returns the none class. |
| `GetDimensionClass() -> ClassAttributes` *static* | Returns the dimension class. |
| `GetGuidesClass() -> ClassAttributes` *static* | Returns the guides class (creates it if missing). |
| `GetDefaultClass() -> ClassAttributes` *static* | Returns the default class (class of the current container (parametric class during a reset)). |
| `GetActiveClass() -> ClassAttributes` *static* | Returns the active class (active class of the document, outside the current container). |
| `GetMaxIndex() -> int` *static* | Returns the max index. |
| `ForEach(includeGuestClasses: bool, callback: callable(ClassAttributes)) -> None` *static* | Calls `callback` with every class of the document (guest classes of referenced files only when `includeGuestClasses` is `True`). |
| `GetAll(includeGuestClasses: bool) -> list[ClassAttributes]` *static* | Every class of the document (with the guest classes of referenced files when `includeGuestClasses` is `True`). |

*Identity*

| Method | Description |
|---|---|
| `GetIndex() -> int \| None` | Returns the index. |
| `GetName() -> str \| None` | Returns the name. |
| `GetDescription() -> str \| None` | Returns the description. |
| `SetDescription(description: str) -> bool` | Sets the description. |
| `MakeDefault() -> bool` | Makes this class the active class (the class of new objects). |
| `Delete() -> bool` | Deletes the class; its objects are moved to the `None` class. The object becomes invalid. |

*Options*

| Method | Description |
|---|---|
| `GetVisibility() -> ClassVisibility \| None` | Returns the visibility. |
| `SetVisibility(visibility: ClassVisibility) -> bool` | Sets the visibility (does not redraw or reset the visibility of the objects). |
| `GetNonPlot() -> bool \| None` | Whether *Non Plot* is on. |
| `SetNonPlot(nonPlot: bool) -> bool` | Turns *Non Plot* on or off. |
| `GetUseAtCreation() -> bool \| None` | Whether new objects created in this class get the class attributes automatically. |
| `SetUseAtCreation(use: bool) -> bool` | Turns *Use At Creation* on or off. Whether new objects created in this class get the class attributes automatically. |
| `GetObjectColors() -> ObjectColors \| None` | Colors (overrides AttributesBase to read/write the class colors). |
| `SetObjectColors(colors: ObjectColors) -> bool` | Sets the object colors (Colors (overrides AttributesBase to read/write the class colors)). |

*Pen*

| Method | Description |
|---|---|
| `GetPenColors() -> ColorPair \| None` | Returns the pen colors. |
| `SetPenColors(colors: ColorPair) -> bool` | Sets the pen colors. |
| `GetPenForeColor() -> ColorRGB \| None` | Returns the pen fore color. |
| `SetPenForeColor(color: ColorRGB) -> bool` | Sets the pen fore color. |
| `GetPenBackColor() -> ColorRGB \| None` | Returns the pen back color. |
| `SetPenBackColor(color: ColorRGB) -> bool` | Sets the pen back color. |
| `GetPenStyle() -> int \| None` | Raw pen style, same values as `PenAttributes.GetStyle`. |
| `SetPenStyle(style: int) -> bool` | Sets the pen style. Raw pen style, same values as `PenAttributes.GetStyle`. |
| `GetPenStyleKind() -> PenStyleKind \| None` | Returns the pen style kind. |
| `GetPenLineType() -> int \| None` | Returns the pen line type. |
| `SetPenLineType(lineTypeIndex: int) -> bool` | Sets the pen line type. |
| `GetLineWeightMils() -> int \| None` | Returns the line weight mils. |
| `SetLineWeightMils(mils: int) -> bool` | Sets the line weight mils. |
| `GetPenOpacity() -> int \| None` | Returns the pen opacity. |
| `SetPenOpacity(opacity: int) -> bool` | Sets the pen opacity. |

*Fill*

| Method | Description |
|---|---|
| `GetFillColors() -> ColorPair \| None` | Returns the fill colors. |
| `SetFillColors(colors: ColorPair) -> bool` | Sets the fill colors. |
| `GetFillForeColor() -> ColorRGB \| None` | Returns the fill fore color. |
| `SetFillForeColor(color: ColorRGB) -> bool` | Sets the fill fore color. |
| `GetFillBackColor() -> ColorRGB \| None` | Returns the fill back color. |
| `SetFillBackColor(color: ColorRGB) -> bool` | Sets the fill back color. |
| `GetFillStyle() -> int \| None` | Raw fill style, same values as `FillAttributes.GetStyle`. |
| `SetFillStyle(style: int) -> bool` | Sets the fill style. Raw fill style, same values as `FillAttributes.GetStyle`. |
| `GetFillType() -> FillType \| None` | Returns the fill type. |
| `GetFillResource() -> int \| None` | Returns the fill resource. |
| `SetFillResource(resourceIndex: int) -> bool` | Sets the fill resource. |
| `GetFillOpacity() -> int \| None` | Returns the fill opacity. |
| `SetFillOpacity(opacity: int) -> bool` | Sets the fill opacity. |

*Pen and fill opacity together*

| Method | Description |
|---|---|
| `SetOpacity(opacity: int) -> bool` | Sets the opacity. |
| `GetBeginningMarker() -> Marker \| None` | Markers. The class stores the marker style only; `Marker.visible` is not used. |
| `SetBeginningMarker(marker: Marker) -> bool` | Sets the beginning marker. Markers. The class stores the marker style only; `Marker.visible` is not used. |
| `GetEndMarker() -> Marker \| None` | Returns the end marker. |
| `SetEndMarker(marker: Marker) -> bool` | Sets the end marker. |
| `GetDropShadow() -> DropShadow \| None` | Drop shadow. `DropShadow.useDropShadow` enables the class drop shadow. |
| `SetDropShadow(data: DropShadow) -> bool` | Sets the drop shadow. Drop shadow. `DropShadow.useDropShadow` enables the class drop shadow. |
| `GetUseTextures() -> bool \| None` | Whether the class applies its textures at creation. |
| `SetUseTextures(use: bool) -> bool` | Turns *Use Textures* on or off. |
| `GetGeneralTexture() -> int \| None` | Returns the general texture. |
| `SetGeneralTexture(texture: int) -> bool` | Sets the general texture. |
| `GetWallTextures() -> WallTextures \| None` | Returns the wall textures. |
| `SetWallTextures(textures: WallTextures) -> bool` | Sets the wall textures. |
| `GetRoofTextures() -> RoofTextures \| None` | Returns the roof textures. |
| `SetRoofTextures(textures: RoofTextures) -> bool` | Sets the roof textures. |

*Text style*

| Method | Description |
|---|---|
| `GetUseTextStyle() -> bool \| None` | Whether *Use Text Style* is on. |
| `SetUseTextStyle(use: bool) -> bool` | Turns *Use Text Style* on or off. |
| `GetTextStyle() -> int \| None` | Returns the text style. |
| `SetTextStyle(textStyle: int) -> bool` | Sets the text style. |

*Objects*

| Method | Description |
|---|---|
| `AssignTo(hObject: Handle, useClassAttributes: bool = False, descendIntoGroups: bool = True) -> bool` | Assigns the object to this class. When `useClassAttributes` is `True` every attribute of the object is set "by class". |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: ClassAttributes) -> bool` | `a == b`: True when both objects refer to the same class. |
| `!=` | `__ne__(o: ClassAttributes) -> bool` | `a != b`: True when the objects refer to different drawing objects. |

Inherited: everything from [`AttributesBase`](#attributesbase).

### ObjectAttributes

> **Full name:** `api.ObjectAttributes` · **Inherits:** [`AttributesBase`](#attributesbase) → `api.Object`

All graphical attributes of an object. Geometry is intentionally not part of this API.

**Constructors**

| Constructor | Description |
|---|---|
| `ObjectAttributes(h: Handle)` | Refers to the existing object `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Pen() -> PenAttributes` | Pen attributes (stroke) of the object. |
| `Fill() -> FillAttributes` | Fill attributes of the object. |
| `FillMapping() -> FillMappingAttributes` | Fill mapping (hatch, tile, gradient and image fill placement) of the object. |
| `Markers() -> MarkerAttributes` | Beginning and end markers of the object. |
| `DropShadow() -> DropShadowAttributes` | Drop shadow of the object. |

*Class of the object*

| Method | Description |
|---|---|
| `GetClass() -> ClassAttributes` | Returns the class. |
| `SetClass(theClass: ClassAttributes, descendIntoGroups: bool = True) -> bool` | Sets the class. |
| `SetAllByClass() -> bool` | Sets every attribute that supports it "by class": pen and fill colors and styles, line weight, opacity, markers and drop shadow. The object then shows the attributes of its class. |
| `GetOpacity() -> int \| None` | Combined opacity (the same for pen and fill). |
| `SetOpacity(opacity: int) -> bool` | Sets the opacity (Combined opacity (the same for pen and fill)). |
| `GetOpacityByClass() -> bool \| None` | Whether *Opacity By Class* is on. |
| `SetOpacityByClass() -> bool` | Sets the opacity by class. |
| `ApplyTo(target: Handle) -> bool` | Copies colors, pen and fill style, line weight, opacity, markers and drop shadow to the target object, then applies the by-class flags (setting a value may reset the corresponding by-class flag). |

Inherited: everything from [`AttributesBase`](#attributesbase).

## Enumerations

### PenStyleKind

> **Full name:** `api.PenStyleKind` · **Kind:** `IntEnum`

Classification of a raw pen style value.

- 0 — none
- 1, 2 — solid
- > 2 — legacy pixel pattern
- < 0 — line type resource, value is -(internal index of the line type)

| Member | Value | Description |
|---|---|---|
| `None_` | `0` |  |
| `Solid` | `1` |  |
| `Pattern` | `2` |  |
| `SimpleLineType` | `3` |  |
| `ComplexLineType` | `4` |  |
| `Unknown` | `5` |  |

### FillType

> **Full name:** `api.FillType` · **Kind:** `IntEnum`

Kind of the fill of an object.

| Member | Value | Description |
|---|---|---|
| `Unknown` | `-1` |  |
| `None_` | `1` |  |
| `Solid` | `2` |  |
| `Pattern` | `3` |  |
| `Hatch` | `4` |  |
| `Tile` | `5` |  |
| `Gradient` | `6` |  |
| `Image` | `7` |  |
| `Class` | `8` |  |

### MarkerShape

> **Full name:** `api.MarkerShape` · **Kind:** `IntEnum`

Markers (arrow heads)

| Member | Value | Description |
|---|---|---|
| `Arrow` | `0` |  |
| `ConcaveCurvedArrow` | `1` |  |
| `Circle` | `2` |  |
| `DimSlash` | `3` |  |
| `DimCross` | `4` |  |
| `Lasso` | `5` |  |
| `Hexagon` | `6` |  |
| `VShaped` | `7` |  |
| `Cone` | `8` |  |
| `TaperedVShaped` | `9` |  |
| `SShaped` | `10` |  |
| `Rectangle` | `11` |  |
| `DoubleLine` | `12` |  |

### MarkerFill

> **Full name:** `api.MarkerFill` · **Kind:** `IntEnum`

The marker style enumerations below (MarkerFill, MarkerBase, MarkerHalfTick) use pre-shifted values so they can be bitwise-OR'd into a single 16-bit style value (see `Marker.GetStyleValue`). Use the enumeration names, not the integers.

| Member | Value | Description |
|---|---|---|
| `LineColor` | `0` |  |
| `White` | `128` |  |
| `NoFill` | `256` |  |

### MarkerBase

> **Full name:** `api.MarkerBase` · **Kind:** `IntEnum`

Shape of the base of a marker (pre-shifted bit values, see `Marker.GetStyleValue`).

| Member | Value | Description |
|---|---|---|
| `Flat` | `0` |  |
| `Open` | `1024` |  |
| `Angle` | `2048` |  |
| `Arc` | `3072` |  |

### MarkerHalfTick

> **Full name:** `api.MarkerHalfTick` · **Kind:** `IntEnum`

Whole marker, or only its left or right half (pre-shifted bit values, see `Marker.GetStyleValue`).

| Member | Value | Description |
|---|---|---|
| `Full` | `0` |  |
| `Left` | `16384` |  |
| `Right` | `24576` |  |

### MarkerThicknessBasis

> **Full name:** `api.MarkerThicknessBasis` · **Kind:** `IntEnum`

What the line thickness of a marker follows.

| Member | Value | Description |
|---|---|---|
| `LineThickness` | `0` |  |
| `DimThickness` | `1` |  |
| `Custom` | `2` |  |

### MarkerThicknessUnits

> **Full name:** `api.MarkerThicknessUnits` · **Kind:** `IntEnum`

Units of a custom marker line thickness.

| Member | Value | Description |
|---|---|---|
| `Mils` | `0` |  |
| `Points` | `16` |  |
| `Millimeters` | `32` |  |

### DropShadowUnits

> **Full name:** `api.DropShadowUnits` · **Kind:** `IntEnum`

Drop shadow

| Member | Value | Description |
|---|---|---|
| `Page` | `0` |  |
| `World` | `1` |  |

### ClassVisibility

> **Full name:** `api.ClassVisibility` · **Kind:** `IntEnum`

Classes

| Member | Value | Description |
|---|---|---|
| `Invisible` | `-1` |  |
| `Visible` | `0` |  |
| `Grayed` | `2` |  |

### ObjectType

> **Full name:** `api.ObjectType` · **Kind:** `IntEnum`

Type of an object. Returned by `Document.GetObjectType` and `AttributesBase.GetObjectType`. The list mirrors the Vectorworks object type codes and is intentionally exhaustive; only a small subset has typed classes today (see the map below). Every other value is opaque - identify the object by its type, then work with it as a raw Handle.

- Line → Line2DObject
- Box → RectangleObject
- RoundedRectangle → RoundRectObject
- Arc / QuarterArc → ArcObject (a full-circle arc is also CircleObject via `ArcObject.Is`)
- Polygon / FreehandPolygon → PolygonObject
- Polyline → PolylineObject
- Locus → Locus2DObject
- Layer → Layer
- ClassDefinition → ClassAttributes

| Member | Value | Description |
|---|---|---|
| `Invalid` | `-1` |  |
| `Term` | `0` |  |
| `Line` | `2` |  |
| `Box` | `3` |  |
| `Oval` | `4` |  |
| `Polygon` | `5` |  |
| `Arc` | `6` |  |
| `DimUnitSettings` | `7` |  |
| `FreehandPolygon` | `8` |  |
| `Locus3D` | `9` |  |
| `Text` | `10` |  |
| `Group` | `11` |  |
| `QuarterArc` | `12` |  |
| `RoundedRectangle` | `13` |  |
| `Paint` | `14` |  |
| `Symbol` | `15` |  |
| `SymbolDefinition` | `16` |  |
| `Locus` | `17` |  |
| `Worksheet` | `18` |  |
| `BuildingMaterial` | `19` |  |
| `Polyline` | `21` |  |
| `Extrude` | `24` |  |
| `Polygon3D` | `25` |  |
| `SlabDrain` | `26` |  |
| `SlabDrainValley` | `27` |  |
| `SlabSlopeValley` | `28` |  |
| `LayerReference` | `29` |  |
| `DashPatterns` | `30` |  |
| `Layer` | `31` |  |
| `Header` | `32` |  |
| `RefList` | `33` |  |
| `Sweep` | `34` |  |
| `ClassList` | `35` |  |
| `ViewportStyle` | `36` |  |
| `DataVisualization` | `37` |  |
| `MultiExtrude` | `38` |  |
| `DimensionStandard` | `39` |  |
| `Mesh` | `40` |  |
| `SavedView` | `43` |  |
| `RenderSpec` | `44` |  |
| `Eps` | `45` |  |
| `Format` | `47` |  |
| `Record` | `48` |  |
| `ToolCommand` | `49` |  |
| `SymbolList` | `54` |  |
| `WorksheetImage` | `56` |  |
| `Data` | `57` |  |
| `RecordLink` | `58` |  |
| `WorksheetDatabase` | `60` |  |
| `LeaderList` | `62` |  |
| `Dimension` | `63` |  |
| `HatchContainer` | `65` |  |
| `HatchDefinition` | `66` |  |
| `Bsp` | `67` |  |
| `Wall` | `68` |  |
| `InnerLines` | `69` |  |
| `SlabDrainageSettings` | `70` |  |
| `Slab` | `71` |  |
| `PenSpace` | `73` |  |
| `FontTable` | `74` |  |
| `StyleRun` | `75` |  |
| `UserData` | `76` |  |
| `WorkingPlane` | `77` |  |
| `WPlaneList` | `78` |  |
| `PixelPatternList` | `79` |  |
| `ColorPalette` | `80` |  |
| `Light` | `81` |  |
| `RoofEdge` | `82` |  |
| `RoofContainer` | `83` |  |
| `CSGTree` | `84` |  |
| `BoundaryRep` | `85` |  |
| `Parametric` | `86` |  |
| `RoofAdorner` | `87` |  |
| `Subscribe` | `88` |  |
| `ObsoleteRoundWall` | `89` |  |
| `UndoPlaceholder` | `90` |  |
| `TextureSpace` | `91` |  |
| `Folder` | `92` |  |
| `TextureBitmap` | `93` |  |
| `ClassDefinition` | `94` |  |
| `Solid` | `95` |  |
| `LineTypeDefinition` | `96` |  |
| `Texture` | `97` |  |
| `ADSymbolDefinitionHandler` | `98` |  |
| `ADSymbolHandler` | `99` |  |
| `SlabEdge` | `100` |  |
| `DropShadow` | `101` |  |
| `RoofStyle` | `102` |  |
| `CurtainWallFrame` | `103` |  |
| `CurtainWallPanel` | `104` |  |
| `CurtainWallGrid` | `105` |  |
| `RenderStyle` | `106` |  |
| `SlabStyle` | `107` |  |
| `TileDefinition` | `108` |  |
| `TextStyle` | `109` |  |
| `Constraint` | `110` |  |
| `PieceWiseNurbsCurve` | `111` |  |
| `CorePrintInfo` | `112` |  |
| `NurbsSurface` | `113` |  |
| `CompositeSurface` | `114` |  |
| `RenderBackground` | `115` |  |
| `PolyBreak` | `116` |  |
| `BatchRenderJob` | `117` |  |
| `BatchRenderJobList` | `118` |  |
| `ImageDefinition` | `119` |  |
| `GradientDefinition` | `120` |  |
| `FillSpace` | `121` |  |
| `Viewport` | `122` |  |
| `ArtRWStyle` | `123` |  |
| `Association` | `124` |  |
| `AuxMarker` | `125` |  |
| `GeoReference` | `126` |  |
| `WallStyle` | `127` |  |

## Module constants

| Constant | Type | Value | Description |
|---|---|---|---|
| `api.kMaxOpacity` | `int` | `100` | Maximum opacity (opacities range from 0 to 100). |

---

[Back to the index](README.md) · [Back to top](#attributes--graphic-attributes-and-classes)
