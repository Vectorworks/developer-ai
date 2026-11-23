**English** • [Deutsch](../../PythonAPI.de/v2027.2/ObjectPrimitives.Math.md) • [日本語](../../PythonAPI.ja/v2027.2/ObjectPrimitives.Math.md)

# Math — standalone 2D and 3D math (`api.Math`)

> **Python module:** `api.Math` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

`api.Math` is a submodule of standalone math values that need no drawing (import it with `from api.Math import Point2D` or use `api.Math.Point2D`): points and vectors (`Point2D` = `Vector2D`, `Point3D` = `Vector3D`), transforms (`Transform2D`, `Transform3D`), rectangles (`Rect2D`, `RotatedRect2D`), lines (`Line2D`, `Line3D`), planes (`Plane3D`), circles (`Circle2D`), arcs (`Arc2D`) and polygons (`Polygon2D` made of `PolyVertex` values), plus utility functions and constants.

All angles are radians, measured counter-clockwise from the positive X axis. Changing a returned value never changes a drawing object: pass the value back to the object's setter.

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [Math.Point2D](#mathpoint2d)
  - [Math.Transform2D](#mathtransform2d)
  - [Math.Rect2D](#mathrect2d)
  - [Math.RotatedRect2D](#mathrotatedrect2d)
  - [Math.Line2D](#mathline2d)
    - [Math.Line2D.Intersection](#mathline2dintersection)
  - [Math.Circle2D](#mathcircle2d)
  - [Math.Arc2D](#matharc2d)
  - [Math.PolyVertex](#mathpolyvertex)
  - [Math.Polygon2D](#mathpolygon2d)
    - [Math.Polygon2D.CurveLocation](#mathpolygon2dcurvelocation)
  - [Math.Point3D](#mathpoint3d)
  - [Math.Transform3D](#mathtransform3d)
  - [Math.Line3D](#mathline3d)
  - [Math.Plane3D](#mathplane3d)
- [Enumerations](#enumerations)
  - [Math.VertexType](#mathvertextype)
  - [Math.OffsetJoin](#mathoffsetjoin)
- [Module functions](#module-functions)
- [Module constants](#module-constants)
- [Aliases and implicit conversions](#aliases-and-implicit-conversions)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`Math.Point2D`](#mathpoint2d) | class |  | 2D point / vector. |
| [`Math.Transform2D`](#mathtransform2d) | class |  | 2D affine transformation. |
| [`Math.Rect2D`](#mathrect2d) | class |  | Axis aligned rectangle. |
| [`Math.RotatedRect2D`](#mathrotatedrect2d) | class |  | Rectangle that may be rotated: a corner, the direction of the width side and the two side lengths. |
| [`Math.Line2D`](#mathline2d) | class |  | Line segment from `start` to `end`. |
| [`Math.Line2D.Intersection`](#mathline2dintersection) | class (nested) |  | Intersection of the infinite lines. |
| [`Math.Circle2D`](#mathcircle2d) | class |  | Circle. |
| [`Math.Arc2D`](#matharc2d) | class |  | Circular arc. |
| [`Math.PolyVertex`](#mathpolyvertex) | class |  | One vertex of a `Polygon2D`: its point, vertex type, arc radius (radius vertices) and the visibility of the edge that starts at it. |
| [`Math.Polygon2D`](#mathpolygon2d) | class |  | Polygon or polyline vertex list. |
| [`Math.Polygon2D.CurveLocation`](#mathpolygon2dcurvelocation) | class (nested) |  | Point and native piece parameter on the temporary NURBS representation of the polygon's curved outer path. |
| [`Math.Point3D`](#mathpoint3d) | class |  | Python-owned 3D point / vector in world millimetres. |
| [`Math.Transform3D`](#mathtransform3d) | class |  | Python-owned 3D affine matrix acting on column vectors; A * B applies B first. |
| [`Math.Line3D`](#mathline3d) | class |  | Python-owned 3D segment from start to end in world millimetres. |
| [`Math.Plane3D`](#mathplane3d) | class |  | Python-owned oriented infinite plane with a unit normal. |
| [`Math.VertexType`](#mathvertextype) | IntEnum |  | Type of a poly vertex. |
| [`Math.OffsetJoin`](#mathoffsetjoin) | IntEnum |  | Corner style of polygon offsets (`Polygon2D.Offset`). |
| [Module functions](#module-functions) | functions | | `AngleDelta`, `AnglesAreEqual`, `AreEqual`, `Clamp`, `DegToRad`, `IsBetween`, `IsGreater`, `IsLess`, `IsZero`, `Lerp`, `NormalizeAngle`, `NormalizeAngleSigned`, `RadToDeg`, `Sign` |
| [Module constants](#module-constants) | constants | | `kPi`, `kTwoPi`, `kHalfPi`, `kEpsilon`, `kAngleEpsilon` |

## Classes

### Math.Point2D

> **Full name:** `api.Math.Point2D` · **Inherits:** `api.Object`

2D point / vector.

**Constructors**

| Constructor | Description |
|---|---|
| `Point2D()` | Default value (fields at their defaults). |
| `Point2D(inX: float, inY: float)` | Point / vector with the coordinates `inX`, `inY`. |
| `Point2D(pt: Point2D)` | Converts an `api.Point2D` record. |
| `Point2D(x=..., y=...)` | Field values as keywords (any subset), e.g. `Point2D(x=...)`. |

**Methods**

*General*

| Method | Description |
|---|---|
| `FromPolar(length: float, angle: float) -> Math.Point2D` *static* | Vector of length `length` in the direction `angle` (radians). |
| `UnitFromAngle(angle: float) -> Math.Point2D` *static* | Unit vector in the direction `angle` (radians). |

*Arithmetic*

| Method | Description |
|---|---|
| `IsEqual(o: Math.Point2D, tolerance: float = 1e-09) -> bool` | True when both coordinates match `o` within `tolerance`. |
| `IsZero(tolerance: float = 1e-09) -> bool` | True when the vector length is within `tolerance` of zero. |

*Vector operations*

| Method | Description |
|---|---|
| `Dot(o: Math.Point2D) -> float` | Dot product with `o`. |
| `Cross(o: Math.Point2D) -> float` | Cross product with `o` (the Z of the 3D cross product). |
| `LengthSquared() -> float` | Squared length of the vector (cheaper than `Length()`). |
| `Length() -> float` | Length of the vector (distance from the origin). |
| `Angle() -> float` | Direction angle of the vector, in (-pi, pi]. |
| `Normalized() -> Math.Point2D` | Unit vector in the same direction (a new value; a zero vector stays zero). |
| `Normalize() -> Math.Point2D` | Scales this vector to unit length in place and returns it. |
| `WithLength(length: float) -> Math.Point2D` | Vector in the same direction with the length `length`. |
| `Perpendicular() -> Math.Point2D` | The vector rotated 90 degrees counter-clockwise. |
| `PerpendicularCW() -> Math.Point2D` | The vector rotated 90 degrees clockwise. |
| `Rotated(angle: float) -> Math.Point2D` | The vector rotated by `angle` radians around the origin. |
| `Rotated(angle: float, center: Math.Point2D) -> Math.Point2D` | The point rotated by `angle` radians around `center`. |
| `Scaled(sx: float, sy: float, center: Math.Point2D = Math.Point2D(0.0, 0.0)) -> Math.Point2D` | The point scaled by `sx` / `sy` relative to `center`. |

*Point operations*

| Method | Description |
|---|---|
| `DistanceSquaredTo(o: Math.Point2D) -> float` | Squared distance to `o`. |
| `DistanceTo(o: Math.Point2D) -> float` | Distance to `o`. |
| `AngleTo(o: Math.Point2D) -> float` | Angle (radians) of the direction from this point to `o`. |
| `MidPoint(o: Math.Point2D) -> Math.Point2D` | Point halfway between this point and `o`. |
| `Lerp(o: Math.Point2D, t: float) -> Math.Point2D` | Linear interpolation towards `o`: `t` = 0 gives this point, 1 gives `o`. |
| `AngleBetween(o: Math.Point2D) -> float` | Signed angle from this vector to `o`, in (-pi, pi], positive is counter-clockwise. |
| `IsParallel(o: Math.Point2D, angleTolerance: float = 1e-09) -> bool` | True when the vectors are parallel (same or opposite direction) within `angleTolerance`. |
| `IsPerpendicular(o: Math.Point2D, angleTolerance: float = 1e-09) -> bool` | True when the vectors are perpendicular within `angleTolerance`. |
| `Orientation(a: Math.Point2D, b: Math.Point2D, c: Math.Point2D) -> float` *static* | Returns > 0 when `c` is to the left of the line from `a` to `b`, < 0 when to the right, 0 when collinear. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `+` | `__add__(o: Math.Point2D) -> Math.Point2D` | `a + b`: sum of the two values. |
| `-` | `__sub__(o: Math.Point2D) -> Math.Point2D` | `a - b`: difference of the two values. |
| `- (unary)` | `__neg__() -> Math.Point2D` | `-a`: the negated value. |
| `*` | `__mul__(s: float) -> Math.Point2D` | `a * s`: the value scaled by a scalar. |
| `/` | `__truediv__(s: float) -> Math.Point2D` | `a / s`: the value divided by a scalar. |
| `+=` | `__iadd__(o: Math.Point2D) -> Math.Point2D` | `a += b`: adds the other value in place. |
| `-=` | `__isub__(o: Math.Point2D) -> Math.Point2D` | `a -= b`: subtracts the other value in place. |
| `*=` | `__imul__(s: float) -> Math.Point2D` | `a *= s`: scales in place by a scalar. |
| `/=` | `__itruediv__(s: float) -> Math.Point2D` | `a /= s`: divides in place by a scalar. |
| `==` | `__eq__(o: Math.Point2D) -> bool` | `a == b`: True when the two values are equal. Exact comparison; use IsEqual for tolerance based comparison. |
| `!=` | `__ne__(o: Math.Point2D) -> bool` | `a != b`: True when the two values differ. |
| `* (reflected)` | `__rmul__(s: float) -> Math.Point2D` | `s * a`: the value scaled by a scalar. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `x` | `float` | X coordinate. |
| `y` | `float` | Y coordinate. |

### Math.Transform2D

> **Full name:** `api.Math.Transform2D` · **Inherits:** `api.Object`

2D affine transformation.

```text
| a  b  tx |   | x |
| c  d  ty | * | y |
| 0  0  1  |   | 1 |
```

Composition 'A * B' applies B first, then A.

**Constructors**

| Constructor | Description |
|---|---|
| `Transform2D()` | Default value (fields at their defaults). |
| `Transform2D(inA: float, inB: float, inC: float, inD: float, inTx: float, inTy: float)` | Transform mapping (x, y) to (`inA`*x + `inB`*y + `inTx`, `inC`*x + `inD`*y + `inTy`). |
| `Transform2D(a=..., b=..., tx=..., c=..., d=..., ty=...)` | Field values as keywords (any subset), e.g. `Transform2D(a=...)`. |

**Methods**

| Method | Description |
|---|---|
| `Identity() -> Math.Transform2D` *static* | The identity transform. |
| `Translation(dx: float, dy: float) -> Math.Transform2D` *static* | Translation by `dx`, `dy`. |
| `Translation(v: Math.Point2D) -> Math.Transform2D` *static* | Translation by the vector `v`. |
| `Rotation(angle: float) -> Math.Transform2D` *static* | Rotation by `angle` radians around the origin. |
| `Rotation(angle: float, center: Math.Point2D) -> Math.Transform2D` *static* | Rotation by `angle` radians around `center`. |
| `Scale(sx: float, sy: float) -> Math.Transform2D` *static* | Scaling by `sx` / `sy` around the origin. |
| `Scale(sx: float, sy: float, center: Math.Point2D) -> Math.Transform2D` *static* | Scaling by `sx` / `sy` around `center`. |
| `Mirror(p1: Math.Point2D, p2: Math.Point2D) -> Math.Transform2D` *static* | Mirror across the infinite line through p1 and p2. |
| `FromAxes(origin: Math.Point2D, xAxis: Math.Point2D, yAxis: Math.Point2D) -> Math.Transform2D` *static* | Maps the unit X/Y axes to `xAxis`/`yAxis` and the origin to `origin`. |
| `Then(next: Math.Transform2D) -> Math.Transform2D` | The transform that applies this one first and then `next`. |
| `Apply(p: Math.Point2D) -> Math.Point2D` | Transforms the point `p` (translation included). |
| `ApplyToVector(v: Math.Point2D) -> Math.Point2D` | Transforms the vector `v` (translation ignored). |
| `Determinant() -> float` | Determinant of the linear part (negative for mirroring transforms). |
| `IsInvertible(tolerance: float = 1e-09) -> bool` | True when the determinant is not zero (within `tolerance`). |
| `Inverse() -> Math.Transform2D \| None` | The inverse transform; `None` when the transform cannot be inverted. |
| `GetTranslation() -> Math.Point2D` | Returns the translation. |
| `SetTranslation(v: Math.Point2D) -> None` | Sets the translation. |
| `GetRotation() -> float` | Returns the rotation (rotation of the X axis). |
| `GetScaleX() -> float` | Returns the scale X. |
| `GetScaleY() -> float` | Returns the scale Y (negative when mirrored). |
| `IsMirrored() -> bool` | True when the transform mirrors (negative determinant). |
| `IsOrthogonal(tolerance: float = 1e-09) -> bool` | Rotation and uniform/non-uniform scale along the axes only (no shear). |
| `IsIdentity(tolerance: float = 1e-09) -> bool` | True when the transform is the identity within `tolerance`. |
| `IsEqual(o: Math.Transform2D, tolerance: float = 1e-09) -> bool` | True when all coefficients match `o` within `tolerance`. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `*` | `__mul__(o: Math.Transform2D) -> Math.Transform2D` | `A * B`: the composed transform (B is applied first, then A). |
| `*=` | `__imul__(o: Math.Transform2D) -> Math.Transform2D` | `A *= B`: composes the other transform in place. |
| `()` | `__call__(p: Math.Point2D) -> Math.Point2D` | `T(p)`: applies the transform to the point (same as `Apply`). |

**Fields**

| Field | Type | Description |
|---|---|---|
| `a` | `float` | Row 1, column 1 of the matrix. |
| `b` | `float` | Row 1, column 2 of the matrix. |
| `tx` | `float` | X translation. |
| `c` | `float` | Row 2, column 1 of the matrix. |
| `d` | `float` | Row 2, column 2 of the matrix. |
| `ty` | `float` | Y translation. |

### Math.Rect2D

> **Full name:** `api.Math.Rect2D` · **Inherits:** `api.Object`

Axis aligned rectangle. Y grows upwards: top >= bottom. A default constructed rectangle is empty; adding points to it grows it.

**Constructors**

| Constructor | Description |
|---|---|
| `Rect2D()` | Default value (fields at their defaults). |
| `Rect2D(inLeft: float, inTop: float, inRight: float, inBottom: float)` | Rectangle with the given sides (Y grows upwards: top >= bottom). |
| `Rect2D(p1: Math.Point2D, p2: Math.Point2D)` | Smallest rectangle containing the two corner points `p1` and `p2`. |
| `Rect2D(left=..., bottom=..., right=..., top=...)` | Field values as keywords (any subset), e.g. `Rect2D(left=...)`. |

**Methods**

*General*

| Method | Description |
|---|---|
| `FromCenter(center: Math.Point2D, width: float, height: float) -> Math.Rect2D` *static* | Rectangle of size `width` x `height` centered on `center`. |
| `IsEmpty() -> bool` | True for an empty rectangle (no point added yet). |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | Empty or with zero width or height. |
| `Width() -> float` | Width (0 for an empty rectangle). |
| `Height() -> float` | Height (0 for an empty rectangle). |
| `Area() -> float` | Area. |
| `Perimeter() -> float` | Perimeter. |
| `Diagonal() -> float` | Length of the diagonal. |
| `Center() -> Math.Point2D` | Center point. |
| `TopLeft() -> Math.Point2D` | Top left corner. |
| `TopRight() -> Math.Point2D` | Top right corner. |
| `BottomLeft() -> Math.Point2D` | Bottom left corner. |
| `BottomRight() -> Math.Point2D` | Bottom right corner. |
| `CenterLeft() -> Math.Point2D` | Middle of the left side. |
| `CenterRight() -> Math.Point2D` | Middle of the right side. |
| `CenterTop() -> Math.Point2D` | Middle of the top side. |
| `CenterBottom() -> Math.Point2D` | Middle of the bottom side. |
| `Corners() -> tuple[Math.Point2D * 4]` | The four corners, counter-clockwise starting at the bottom left corner. |
| `FromPoints(points: list[Math.Point2D]) -> Math.Rect2D` *static* | Smallest rectangle containing all `points` (empty for an empty list). |

*Growing*

| Method | Description |
|---|---|
| `Add(p: Math.Point2D) -> Math.Rect2D` | Grows the rectangle in place to include the point `p`; returns it. |
| `Add(r: Math.Rect2D) -> Math.Rect2D` | Grows the rectangle in place to include the rectangle `r`; returns it. |
| `Union(r: Math.Rect2D) -> Math.Rect2D` | Smallest rectangle containing this rectangle and `r` (a new value). |
| `Intersection(r: Math.Rect2D) -> Math.Rect2D` | Overlap of this rectangle and `r` (empty when they do not overlap). |
| `Inflated(dx: float, dy: float) -> Math.Rect2D` | Grows by `dx` on left and right, by `dy` on top and bottom (negative values shrink). |
| `Offset(v: Math.Point2D) -> Math.Rect2D` | The rectangle moved by the vector `v`. |
| `Transformed(t: Math.Transform2D) -> Math.Rect2D` | Bounds of the transformed corners. |

*Queries*

| Method | Description |
|---|---|
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True when the point `p` lies inside the rectangle or on its border. |
| `Contains(r: Math.Rect2D, tolerance: float = 1e-09) -> bool` | True when the rectangle `r` lies completely inside this rectangle. |
| `Intersects(r: Math.Rect2D, tolerance: float = 1e-09) -> bool` | True when the rectangles overlap or touch. |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | Point of the rectangle closest to `p` (`p` itself when it is inside). |
| `DistanceTo(p: Math.Point2D) -> float` | Distance from `p` to the rectangle (0 inside). |
| `IsEqual(r: Math.Rect2D, tolerance: float = 1e-09) -> bool` | True when all four sides match `r` within `tolerance`. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `left` | `float` | Left side (smallest X). |
| `bottom` | `float` | Bottom side (smallest Y). |
| `right` | `float` | Right side (largest X). |
| `top` | `float` | Top side (largest Y). |

### Math.RotatedRect2D

> **Full name:** `api.Math.RotatedRect2D` · **Inherits:** `api.Object`

Rectangle that may be rotated: a corner, the direction of the width side and the two side lengths. This is how Vectorworks stores rectangles and rounded rectangles. Corners (counter-clockwise when width and height are positive): origin, origin + dir*width, origin + dir*width + perp*height, origin + perp*height where perp is `direction` rotated 90 degrees counter-clockwise. Negative width or height extend the other way.

**Constructors**

| Constructor | Description |
|---|---|
| `RotatedRect2D()` | Default value (fields at their defaults). |
| `RotatedRect2D(inOrigin: Math.Point2D, inDirection: Math.Point2D, inWidth: float, inHeight: float)` | Rectangle with the corner `inOrigin`, the direction of the width side `inDirection` and the side lengths `inWidth`, `inHeight`. |
| `RotatedRect2D(r: Math.Rect2D)` | Unrotated rectangle equal to `r`. |
| `RotatedRect2D(origin=..., direction=..., width=..., height=...)` | Field values as keywords (any subset), e.g. `RotatedRect2D(origin=...)`. |

**Methods**

*General*

| Method | Description |
|---|---|
| `FromCenter(center: Math.Point2D, inWidth: float, inHeight: float, angle: float = 0.0) -> Math.RotatedRect2D` *static* | Rectangle of size `inWidth` x `inHeight` centered on `center`, rotated by `angle` radians. |
| `Angle() -> float` | Rotation angle of the width side (radians). |
| `WidthVector() -> Math.Point2D` | Vector along the width side (`direction * width`). |
| `HeightVector() -> Math.Point2D` | Vector along the height side (perpendicular to the width side, length `height`). |
| `Area() -> float` | Area. |
| `Perimeter() -> float` | Perimeter. |
| `Center() -> Math.Point2D` | Center point. |
| `IsAxisAligned(angleTolerance: float = 1e-09) -> bool` | True when the rectangle is not rotated (within `angleTolerance`). |
| `Corners() -> tuple[Math.Point2D * 4]` | The four corners: origin, origin + width vector, the opposite corner, origin + height vector. |
| `Bounds() -> Math.Rect2D` | Axis-aligned bounding rectangle. |

*Local frame*

| Method | Description |
|---|---|
| `LocalToWorld() -> Math.Transform2D` | X along the width side, Y along the height side, origin at `origin`. |
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True when `p` lies inside the rectangle or on its border. |
| `Offset(v: Math.Point2D) -> Math.RotatedRect2D` | The rectangle moved by the vector `v`. |
| `Rotated(angle: float, center: Math.Point2D) -> Math.RotatedRect2D` | The rectangle rotated by `angle` radians around `center`. |
| `Normalized() -> Math.RotatedRect2D` | Same rectangle, normalized to positive width and height. |
| `Transformed(t: Math.Transform2D, tolerance: float = 1e-09) -> Math.RotatedRect2D \| None` | Only similarity transforms (rotation, translation, uniform scale, mirror) keep a rectangle a rectangle. |
| `IsEqual(r: Math.RotatedRect2D, tolerance: float = 1e-09) -> bool` | True when the rectangles match within `tolerance`. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `origin` | `Math.Point2D` | Corner the width and height sides start from. |
| `direction` | `Math.Point2D` | Unit vector along the width side. |
| `width` | `float` | Length of the width side (negative extends the other way). |
| `height` | `float` | Length of the height side (negative extends the other way). |

### Math.Line2D

> **Full name:** `api.Math.Line2D` · **Inherits:** `api.Object`

Line segment from `start` to `end`. Methods with "Infinite" in the name treat the segment as an infinite line through both points. A parameter `t` maps 0 to `start` and 1 to `end`.

**Constructors**

| Constructor | Description |
|---|---|
| `Line2D()` | Default value (fields at their defaults). |
| `Line2D(inStart: Math.Point2D, inEnd: Math.Point2D)` | Segment from `inStart` to `inEnd`. |
| `Line2D(x1: float, y1: float, x2: float, y2: float)` | Segment from (`x1`, `y1`) to (`x2`, `y2`). |
| `Line2D(start=..., end=...)` | Field values as keywords (any subset), e.g. `Line2D(start=...)`. |

**Methods**

| Method | Description |
|---|---|
| `FromPointAngleLength(inStart: Math.Point2D, angle: float, length: float) -> Math.Line2D` *static* | Segment starting at `inStart` in the direction `angle` (radians) with the length `length`. |
| `Vector() -> Math.Point2D` | Vector from `start` to `end`. |
| `Direction() -> Math.Point2D` | Unit vector from `start` towards `end`. |
| `Normal() -> Math.Point2D` | Unit normal pointing to the left of the segment. |
| `Length() -> float` | Length of the segment. |
| `LengthSquared() -> float` | Squared length of the segment. |
| `Angle() -> float` | Angle of the segment direction (radians from the X axis). |
| `MidPoint() -> Math.Point2D` | Middle of the segment. |
| `PointAt(t: float) -> Math.Point2D` | Point at the parameter `t` (0 = `start`, 1 = `end`; other values extrapolate). |
| `PointAtDistance(distanceFromStart: float) -> Math.Point2D` | Point at the distance `distanceFromStart` from `start` along the line. |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | True when start and end coincide within `tolerance`. |
| `Bounds() -> Math.Rect2D` | Bounding rectangle of the segment. |
| `Reversed() -> Math.Line2D` | The segment with `start` and `end` swapped. |
| `Offset(v: Math.Point2D) -> Math.Line2D` | The segment moved by the vector `v`. |
| `OffsetParallel(distance: float) -> Math.Line2D` | Parallel line at `distance` to the left (negative: to the right). |
| `Transformed(t: Math.Transform2D) -> Math.Line2D` | The segment transformed by `t`. |
| `Rotated(angle: float, center: Math.Point2D) -> Math.Line2D` | The segment rotated by `angle` radians around `center`. |
| `WithLength(length: float) -> Math.Line2D` | Moves the end point along the line so the segment has the specified length. |
| `Extended(atStart: float, atEnd: float) -> Math.Line2D` | Extends (or trims when negative) both ends. |
| `ProjectParameter(p: Math.Point2D) -> float` | Parameter of the projection of `p` on the infinite line. |
| `ProjectInfinite(p: Math.Point2D) -> Math.Point2D` | Projection of `p` on the infinite line. |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | Point of the segment closest to `p`. |
| `DistanceTo(p: Math.Point2D) -> float` | Distance from `p` to the segment. |
| `DistanceToInfinite(p: Math.Point2D) -> float` | Distance from `p` to the infinite line. |
| `SignedDistanceToInfinite(p: Math.Point2D) -> float` | Positive when `p` is to the left of the line. |
| `SideOf(p: Math.Point2D, tolerance: float = 1e-09) -> int` | > 0 left, < 0 right, 0 on the infinite line. |
| `IsPointOn(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True when `p` lies on the segment within `tolerance`. |
| `IsPointOnInfinite(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True when `p` lies on the infinite line within `tolerance`. |
| `Mirror(p: Math.Point2D) -> Math.Point2D` | Mirror image of `p` across the infinite line. |
| `IsParallel(o: Math.Line2D, angleTolerance: float = 1e-09) -> bool` | True when the lines are parallel within `angleTolerance`. |
| `IsPerpendicular(o: Math.Line2D, angleTolerance: float = 1e-09) -> bool` | True when the lines are perpendicular within `angleTolerance`. |
| `IsCollinear(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | True when both segments lie on the same infinite line (within `tolerance`). |
| `IntersectInfinite(o: Math.Line2D) -> Math.Line2D.Intersection \| None` | Intersection of the infinite lines through both segments: the point and the parameters on both lines; `None` for parallel lines. |
| `Intersect(o: Math.Line2D, tolerance: float = 1e-09) -> Math.Point2D \| None` | Intersection point of the two segments (parallel or collinear segments return no point). |
| `Intersects(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | True when the two segments intersect or touch. |
| `DistanceTo(o: Math.Line2D) -> float` | Shortest distance between the two segments. |
| `IsEqual(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | True when start and end match `o` within `tolerance`. |
| `IsEqualIgnoreDirection(o: Math.Line2D, tolerance: float = 1e-09) -> bool` | True when the segments match `o` in either direction within `tolerance`. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `start` | `Math.Point2D` | Start point. |
| `end` | `Math.Point2D` | End point. |

#### Math.Line2D.Intersection

> **Full name:** `api.Math.Line2D.Intersection` · **Inherits:** `api.Object`

Intersection of the infinite lines. Returns the point and the parameters on this line and on `o`.

**Constructors**

| Constructor | Description |
|---|---|
| `Intersection()` | Default value (fields at their defaults). |
| `Intersection(point, t, tOther)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `point` | `Math.Point2D` | Intersection point. |
| `t` | `float` | Parameter on this line. |
| `tOther` | `float` | Parameter on the other line. |

### Math.Circle2D

> **Full name:** `api.Math.Circle2D` · **Inherits:** `api.Object`

Circle.

**Constructors**

| Constructor | Description |
|---|---|
| `Circle2D()` | Default value (fields at their defaults). |
| `Circle2D(inCenter: Math.Point2D, inRadius: float)` | Circle with the center `inCenter` and the radius `inRadius`. |
| `Circle2D(center=..., radius=...)` | Field values as keywords (any subset), e.g. `Circle2D(center=...)`. |

**Methods**

| Method | Description |
|---|---|
| `FromDiameter(p1: Math.Point2D, p2: Math.Point2D) -> Math.Circle2D` *static* | Circle whose diameter is the segment from `p1` to `p2`. |
| `FromThreePoints(p1: Math.Point2D, p2: Math.Point2D, p3: Math.Point2D) -> Math.Circle2D \| None` *static* | Circle through three points; empty when the points are collinear. |
| `Diameter() -> float` | Diameter. |
| `Circumference() -> float` | Circumference. |
| `Area() -> float` | Area. |
| `Bounds() -> Math.Rect2D` | Bounding rectangle. |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | True when the radius is zero (within `tolerance`). |
| `PointAt(angle: float) -> Math.Point2D` | Point of the circle at `angle` (radians). |
| `AngleOf(p: Math.Point2D) -> float` | Angle (radians) of the direction from the center to `p`. |
| `TangentAt(angle: float) -> Math.Point2D` | Unit tangent at `angle`, in the counter-clockwise direction. |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | Point of the circle closest to `p`. |
| `DistanceTo(p: Math.Point2D) -> float` | Distance from `p` to the circumference. |
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True when `p` lies inside the circle or on it. |
| `IsPointOn(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True when `p` lies on the circumference within `tolerance`. |
| `Offset(v: Math.Point2D) -> Math.Circle2D` | The circle moved by the vector `v`. |
| `Rotated(angle: float, c: Math.Point2D) -> Math.Circle2D` | The circle rotated by `angle` radians around `c`. |
| `Scaled(factor: float, c: Math.Point2D) -> Math.Circle2D` | The circle scaled by `factor` relative to `c`. |
| `IntersectInfinite(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Intersection points with the infinite line (0, 1 or 2 points). |
| `Intersect(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Intersection points with the segment. |
| `Intersect(o: Math.Circle2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Intersection points with another circle (coincident circles return no points). |
| `TangentPoints(p: Math.Point2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Tangent points on the circle for tangent lines through `p` (none when `p` is inside). |
| `IsEqual(o: Math.Circle2D, tolerance: float = 1e-09) -> bool` | True when center and radius match `o` within `tolerance`. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `center` | `Math.Point2D` | Center. |
| `radius` | `float` | Radius. |

### Math.Arc2D

> **Full name:** `api.Math.Arc2D` · **Inherits:** `api.Object`

Circular arc. `sweepAngle` is positive for counter-clockwise arcs and negative for clockwise arcs; |sweepAngle| >= 2*pi is a full circle.

**Constructors**

| Constructor | Description |
|---|---|
| `Arc2D()` | Default value (fields at their defaults). |
| `Arc2D(inCenter: Math.Point2D, inRadius: float, inStartAngle: float, inSweepAngle: float)` | Arc with the given center, radius, start angle and signed sweep angle (radians; a positive sweep runs counter-clockwise). |
| `Arc2D(circle: Math.Circle2D)` | Full-circle arc on `circle`. |
| `Arc2D(center=..., radius=..., startAngle=..., sweepAngle=...)` | Field values as keywords (any subset), e.g. `Arc2D(center=...)`. |

**Methods**

| Method | Description |
|---|---|
| `FromCenterStartEnd(inCenter: Math.Point2D, startPt: Math.Point2D, endPt: Math.Point2D, ccw: bool = True) -> Math.Arc2D` *static* | Counter-clockwise (ccw = `True`) or clockwise arc from `startPt` to the ray through `endPt`. |
| `FromThreePoints(startPt: Math.Point2D, midPt: Math.Point2D, endPt: Math.Point2D) -> Math.Arc2D \| None` *static* | Arc starting at `startPt`, passing through `midPt` and ending at `endPt`; empty when the points are collinear. |
| `FromTangent(startPt: Math.Point2D, startTangent: Math.Point2D, endPt: Math.Point2D) -> Math.Arc2D \| None` *static* | Arc from `startPt` with the given start tangent direction, ending at `endPt`. |
| `Circle() -> Math.Circle2D` | The full circle the arc lies on. |
| `IsFullCircle(tolerance: float = 1e-09) -> bool` | True when the sweep is a full turn (within `tolerance`). |
| `IsCounterClockwise() -> bool` | True when the sweep angle is positive. |
| `EndAngle() -> float` | Angle of the end point (start angle + sweep). |
| `MidAngle() -> float` | Angle of the middle of the arc. |
| `PointAtAngle(angle: float) -> Math.Point2D` | Point on the arc circle at `angle` (radians). |
| `PointAt(t: float) -> Math.Point2D` | Point at the parameter `t` along the sweep (0 = start, 1 = end). |
| `StartPoint() -> Math.Point2D` | Start point. |
| `EndPoint() -> Math.Point2D` | End point. |
| `MidPoint() -> Math.Point2D` | Middle point of the arc. |
| `TangentAt(t: float) -> Math.Point2D` | Unit tangent at the parameter `t`, in the sweep direction. |
| `Length() -> float` | Arc length. |
| `Chord() -> Math.Line2D` | Segment from the start point to the end point. |
| `ChordLength() -> float` | Length of the chord. |
| `Sagitta() -> float` | Distance from the chord midpoint to the arc midpoint. |
| `SectorArea() -> float` | Area of the circular sector between the center and the arc. |
| `SegmentArea() -> float` | Area between the arc and its chord. |
| `ContainsAngle(angle: float, tolerance: float = 1e-09) -> bool` | Whether the ray from the center at `angle` passes through the arc. |
| `IsPointOn(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True when `p` lies on the arc within `tolerance`. |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | Point of the arc closest to `p`. |
| `DistanceTo(p: Math.Point2D) -> float` | Distance from `p` to the arc. |
| `Bounds() -> Math.Rect2D` | Bounds of the arc curve (not including the center). |
| `Reversed() -> Math.Arc2D` | The same arc traversed in the opposite direction. |
| `Normalized() -> Math.Arc2D` | Same arc with a non-negative sweep and a start angle in [0, 2*pi). |
| `Offset(v: Math.Point2D) -> Math.Arc2D` | The arc moved by the vector `v`. |
| `Rotated(angle: float, c: Math.Point2D) -> Math.Arc2D` | The arc rotated by `angle` radians around `c`. |
| `WithRadius(r: float) -> Math.Arc2D` | Concentric arc with a different radius (same angles). |
| `Intersect(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Intersection points with a segment / another arc / a circle. |
| `Intersect(circle: Math.Circle2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Intersection points with a segment / another arc / a circle. |
| `Intersect(o: Math.Arc2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Intersection points with a segment / another arc / a circle. |
| `Tessellate(maxDeviation: float) -> list[Math.Point2D]` | Points along the arc so that the chord deviation is at most `maxDeviation` (includes both ends). |
| `IsEqual(o: Math.Arc2D, tolerance: float = 1e-09) -> bool` | True when the arcs match within `tolerance`. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `center` | `Math.Point2D` | Center. |
| `radius` | `float` | Radius. |
| `startAngle` | `float` | Start angle (radians). |
| `sweepAngle` | `float` | Signed sweep angle (radians; positive runs counter-clockwise). |

### Math.PolyVertex

> **Full name:** `api.Math.PolyVertex` · **Inherits:** `api.Object`

One vertex of a `Polygon2D`: its point, vertex type, arc radius (radius vertices) and the visibility of the edge that starts at it.

**Constructors**

| Constructor | Description |
|---|---|
| `PolyVertex()` | Default value (fields at their defaults). |
| `PolyVertex(pt: Math.Point2D, t: Math.VertexType = Math.VertexType.Corner, radius: float = 0.0, vis: bool = True)` | Vertex at `pt` of the type `t` (`radius` for radius vertices; `vis` is the visibility of the edge that starts at it). |
| `PolyVertex(point=..., type=..., arcRadius=..., visible=...)` | Field values as keywords (any subset), e.g. `PolyVertex(point=...)`. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: Math.PolyVertex) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: Math.PolyVertex) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `point` | `Math.Point2D` | Vertex position. |
| `type` | `Math.VertexType` | Vertex type (corner, Bezier, cubic, arc, radius). |
| `arcRadius` | `float` | Only for `Math.VertexType.Arc`. |
| `visible` | `bool` | Visibility of the edge starting at this vertex. |

### Math.Polygon2D

> **Full name:** `api.Math.Polygon2D` · **Inherits:** `api.Object`

Polygon or polyline vertex list. Except for GetCurve.../DivideCurveByCount, computations use the vertex points as straight edges; curve vertices (bezier, cubic, arc, radius) are treated as their control points.

**Constructors**

| Constructor | Description |
|---|---|
| `Polygon2D()` | Empty polygon. |
| `Polygon2D(points: list[Math.Point2D], closed: bool = True)` | Polygon with corner vertices at `points`. |
| `Polygon2D(vertices: list[Math.PolyVertex], closed: bool = True)` | Polygon with the vertices `vertices`. |

**Methods**

*General*

| Method | Description |
|---|---|
| `FromRect(r: Math.Rect2D) -> Math.Polygon2D` *static* | Closed polygon with the four corners of `r`. |
| `FromRotatedRect(r: Math.RotatedRect2D) -> Math.Polygon2D` *static* | Closed polygon with the four corners of the rotated rectangle `r`. |
| `FromArc(arc: Math.Arc2D, maxDeviation: float, closeThroughCenter: bool = False) -> Math.Polygon2D` *static* | Polygon approximating `arc` with at most `maxDeviation` between chords and arc; with `closeThroughCenter` the polygon is a closed sector. |
| `RegularPolygon(center: Math.Point2D, circumradius: float, sides: int, startAngle: float = 0.0) -> Math.Polygon2D` *static* | Regular polygon with `sides` corners on a circle of radius `circumradius` around `center`, the first corner at `startAngle`. |

*Vertices*

| Method | Description |
|---|---|
| `GetVertexCount() -> int` | Number of vertex items. |
| `IsEmpty() -> bool` | True when the polygon has no vertices. |
| `GetVertex(i: int) -> Math.PolyVertex` | Returns the vertex at `i`. |
| `GetPoint(i: int) -> Math.Point2D` | Returns the point at `i`. |
| `SetPoint(i: int, p: Math.Point2D) -> None` | Sets the point at `i`. |
| `GetVertices() -> list[Math.PolyVertex]` | Returns the vertices. |
| `GetPoints() -> list[Math.Point2D]` | Returns the points. |
| `AddVertex(v: Math.PolyVertex) -> None` | Appends the vertex `v`. |
| `AddVertex(p: Math.Point2D, type: Math.VertexType = Math.VertexType.Corner, arcRadius: float = 0.0) -> None` | Appends a vertex at `p` of the type `type` (`arcRadius` for radius vertices). |
| `InsertVertex(beforeIndex: int, v: Math.PolyVertex) -> None` | Inserts `v` before the vertex `beforeIndex` (appends when the index is past the end). |
| `RemoveVertex(i: int) -> None` | Removes the vertex `i` (ignored when out of range). |
| `Clear() -> None` | Removes every vertex and every hole. |
| `IsClosed() -> bool` | True when the polygon is closed. |
| `SetClosed(closed: bool) -> None` | Turns *Closed* on or off. |
| `HasCurves() -> bool` | True when a vertex is not a corner vertex. |
| `HasHiddenEdges() -> bool` | True when an edge is invisible. |
| `GetHoleCount() -> int` | Number of hole items. |
| `GetHole(i: int) -> Math.Polygon2D` | Returns the hole at `i`. |
| `AddHole(hole: Math.Polygon2D) -> None` | Adds `hole` as a hole of this polygon. |
| `ClearHoles() -> None` | Removes every hole. |
| `GetEdgeCount() -> int` | Edges. A closed polygon has as many edges as vertices, an open one has one less. |
| `GetEdge(i: int) -> Math.Line2D` | Returns the segment from vertex `i` to the next vertex; the last vertex connects back to vertex 0. Raises `IndexError` when `i >= GetVertexCount()`. For an open polygon, `i == GetEdgeCount()` returns the closing segment, although it is not included in the edge count. |

*Measurement*

| Method | Description |
|---|---|
| `SignedArea() -> float` | Positive for counter-clockwise polygons. |
| `Area() -> float` | Area of the polygon (not negative; see `SignedArea` for the orientation). |
| `Perimeter() -> float` | Total length of the straight vertex edges. |
| `Centroid() -> Math.Point2D` | Area centroid for closed polygons with non-zero area, vertex average otherwise. |
| `Bounds() -> Math.Rect2D` | Bounding rectangle of the vertices. |

*Orientation*

| Method | Description |
|---|---|
| `IsCounterClockwise() -> bool` | True when the vertices run counter-clockwise (positive signed area). |
| `IsClockwise() -> bool` | True when the vertices run clockwise (negative signed area). |
| `Reverse() -> Math.Polygon2D` | Reverses the vertex order. Edge visibility follows its edge. |
| `Reversed() -> Math.Polygon2D` | Copy of the polygon with the vertex order reversed. |

*Queries*

| Method | Description |
|---|---|
| `Contains(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | Even-odd containment test (the boundary counts as inside). |
| `IsPointOnBoundary(p: Math.Point2D, tolerance: float = 1e-09) -> bool` | True when `p` lies on an edge within `tolerance`. |
| `ClosestPoint(p: Math.Point2D) -> Math.Point2D` | Point of the polygon outline closest to `p` (straight vertex edges). |
| `DistanceTo(p: Math.Point2D) -> float` | Distance from `p` to the polygon outline (straight vertex edges). |
| `GetCurveLength() -> float \| None` | Actual curved OUTER path, unlike the control-polygon queries above. Vectorworks uses a temporary NURBS curve; no drawing objects are inserted or inputs modified. Requires an active drawing context, as do the Boolean operations. Includes hidden edges and the closing edge, excludes holes. Units are world units in the polygon's own XY plane. Parameters identify pieces of the temporary NURBS. |
| `GetCurveLocationAtDistance(distance: float) -> Math.Polygon2D.CurveLocation \| None` | Returns the curve location at distance for `distance`. |
| `GetCurvePointAtDistance(distance: float) -> Math.Point2D \| None` | Returns the curve point at distance for `distance`. |
| `GetCurveTangentAtDistance(distance: float) -> Math.Point2D \| None` | Returns the curve tangent at distance for `distance`. |
| `GetCurveCurvatureAtDistance(distance: float) -> float \| None` | Returns the curve curvature at distance for `distance`. |
| `GetCurveClosestPoint(point: Math.Point2D) -> Math.Polygon2D.CurveLocation \| None` | Returns the curve closest point for `point`. |
| `GetCurveDistanceTo(point: Math.Point2D) -> float \| None` | Returns the curve distance to for `point`. |
| `DivideCurveByCount(count: int, includeEnd: bool = True) -> list[Math.Point2D] \| None` | Exactly count >= 2 arc-spaced points; includeEnd=`False` omits the final endpoint/seam. Curvature is nonnegative, one-sided at corners; zero speed and invalid arguments fail. Failures return `None`, never a partial list. Distances must lie in [0, curve length]. |
| `IsConvex() -> bool` | True when the polygon is convex. |
| `IsSelfIntersecting(tolerance: float = 1e-09) -> bool` | Whether any two non-adjacent edges intersect. |
| `Intersect(line: Math.Line2D, tolerance: float = 1e-09) -> list[Math.Point2D]` | Intersection points of the edges with a segment. |

*Modification*

| Method | Description |
|---|---|
| `Transform(t: Math.Transform2D) -> Math.Polygon2D` | Transforms the polygon in place by `t` and returns it. |
| `Transformed(t: Math.Transform2D) -> Math.Polygon2D` | Copy of the polygon transformed by `t`. |
| `Offset(d: Math.Point2D) -> Math.Polygon2D` | Moves the polygon in place by the vector `d` and returns it. |
| `Offset(distance: float, join: Math.OffsetJoin = Math.OffsetJoin.Miter) -> list[Math.Polygon2D]` | Offset contours of the polygon at `distance` with the corner style `join`, as a list of polygons. Raises `RuntimeError` when the offset fails. |
| `Rotate(angle: float, center: Math.Point2D) -> Math.Polygon2D` | Rotates the polygon in place by `angle` radians around `center` and returns it. |
| `RemoveDuplicateVertices(tolerance: float = 1e-09) -> Math.Polygon2D` | Removes consecutive coincident vertices (and the closing duplicate of a closed polygon). |
| `RemoveCollinearVertices(tolerance: float = 1e-09) -> Math.Polygon2D` | Removes vertices that lie on the straight line through their neighbours (corner vertices only). |
| `IsEqual(o: Math.Polygon2D, tolerance: float = 1e-09) -> bool` | True when the vertices match `o` within `tolerance`. |
| `Union(other: Math.Polygon2D) -> list[Math.Polygon2D]` | Union with `other`, as a list of polygons. Needs an active drawing; raises `RuntimeError` when the operation fails. |
| `Intersection(other: Math.Polygon2D) -> list[Math.Polygon2D]` | Intersection with `other`, as a list of polygons. Needs an active drawing; raises `RuntimeError` when the operation fails. |
| `Difference(other: Math.Polygon2D) -> list[Math.Polygon2D]` | This polygon minus `other`, as a list of polygons. Needs an active drawing; raises `RuntimeError` when the operation fails. |
| `SymmetricDifference(other: Math.Polygon2D) -> list[Math.Polygon2D]` | Parts covered by exactly one of the two polygons, as a list of polygons. Needs an active drawing; raises `RuntimeError` when the operation fails. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `len()` | `__len__() -> int` | `len(a)`: number of vertices. |
| `[]` | `__getitem__(i: int) -> Math.PolyVertex` | `poly[i]`: the vertex at `i` (negative indices count from the end; `IndexError` when out of range). |
| `[] =` | `__setitem__(i: int, vertex: Math.PolyVertex) -> None` | `poly[i] = vertex`: replaces the vertex at `i`. |
| `[] =` | `__setitem__(i: int, point: Math.Point2D) -> None` | `poly[i] = point`: moves the vertex at `i` to `point` (keeps its type). |
| `repr()` | `__repr__() -> str` | `repr(poly)`: `<api.Math.Polygon2D vertices=N closed=True\|False>`. |

#### Math.Polygon2D.CurveLocation

> **Full name:** `api.Math.Polygon2D.CurveLocation` · **Inherits:** `api.Object`

Point and native piece parameter on the temporary NURBS representation of the polygon's curved outer path.

**Constructors**

| Constructor | Description |
|---|---|
| `CurveLocation()` | Default value (fields at their defaults). |
| `CurveLocation(point, pieceIndex, parameter)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `point` | `Math.Point2D` | Point on the curve. |
| `pieceIndex` | `int` | Index of the curve piece. |
| `parameter` | `float` | Parameter on that piece. |

### Math.Point3D

> **Full name:** `api.Math.Point3D` · **Inherits:** `api.Object`

Python-owned 3D point / vector in world millimetres. Vector3D is the same type. Construct from x, y, z, a Point2D with optional Z, or api.Point3D. `Normalized()` returns a value; `Normalize()` changes this value. Zero normalization returns zero. No drawing is required.

**Constructors**

| Constructor | Description |
|---|---|
| `Point3D()` | Default value (fields at their defaults). |
| `Point3D(inX: float, inY: float, inZ: float)` | Point / vector with the coordinates `inX`, `inY`, `inZ`. |
| `Point3D(point: Math.Point2D, inZ: float = 0.0)` | Point with the X and Y of `point` and the Z `inZ`. |
| `Point3D(point: Point3D)` | Converts an `api.Point3D` record. |
| `Point3D(x=..., y=..., z=...)` | Field values as keywords (any subset), e.g. `Point3D(x=...)`. |

**Methods**

| Method | Description |
|---|---|
| `IsEqual(other: Math.Point3D, tolerance: float = 1e-09) -> bool` | True when all coordinates match `other` within `tolerance`. |
| `IsZero(tolerance: float = 1e-09) -> bool` | True when the vector length is within `tolerance` of zero. |
| `IsFinite() -> bool` | True when no coordinate is infinite or NaN. |
| `Dot(other: Math.Point3D) -> float` | Dot product with `other`. |
| `Cross(other: Math.Point3D) -> Math.Point3D` | Cross product with `other`. |
| `LengthSquared() -> float` | Squared length of the vector. |
| `Length() -> float` | Length of the vector. |
| `Normalized() -> Math.Point3D` | Unit vector in the same direction (a new value; a zero vector stays zero). |
| `Normalize() -> Math.Point3D` | Scales this vector to unit length in place and returns it. |
| `WithLength(length: float) -> Math.Point3D` | Vector in the same direction with the length `length`. |
| `DistanceSquaredTo(other: Math.Point3D) -> float` | Squared distance to `other`. |
| `DistanceTo(other: Math.Point3D) -> float` | Distance to `other`. |
| `MidPoint(other: Math.Point3D) -> Math.Point3D` | Point halfway between this point and `other`. |
| `Lerp(other: Math.Point3D, parameter: float) -> Math.Point3D` | Linear interpolation towards `other`: `parameter` = 0 gives this point, 1 gives `other`. |
| `AngleBetween(other: Math.Point3D) -> float` | Angle between this vector and `other` (radians, 0 .. pi). |
| `IsParallel(other: Math.Point3D, angleTolerance: float = 1e-09) -> bool` | True when the vectors are parallel (same or opposite direction) within `angleTolerance`. |
| `IsPerpendicular(other: Math.Point3D, angleTolerance: float = 1e-09) -> bool` | True when the vectors are perpendicular within `angleTolerance`. |
| `XY() -> Math.Point2D` | The X and Y coordinates as a `Math.Point2D`. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `+` | `__add__(other: Math.Point3D) -> Math.Point3D` | `a + b`: sum of the two values. |
| `-` | `__sub__(other: Math.Point3D) -> Math.Point3D` | `a - b`: difference of the two values. |
| `- (unary)` | `__neg__() -> Math.Point3D` | `-a`: the negated value. |
| `*` | `__mul__(scalar: float) -> Math.Point3D` | `a * s`: the value scaled by a scalar. |
| `/` | `__truediv__(scalar: float) -> Math.Point3D` | `a / s`: the value divided by a scalar. |
| `+=` | `__iadd__(other: Math.Point3D) -> Math.Point3D` | `a += b`: adds the other value in place. |
| `-=` | `__isub__(other: Math.Point3D) -> Math.Point3D` | `a -= b`: subtracts the other value in place. |
| `*=` | `__imul__(scalar: float) -> Math.Point3D` | `a *= s`: scales in place by a scalar. |
| `/=` | `__itruediv__(scalar: float) -> Math.Point3D` | `a /= s`: divides in place by a scalar. |
| `==` | `__eq__(other: Math.Point3D) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(other: Math.Point3D) -> bool` | `a != b`: True when the two values differ. |
| `* (reflected)` | `__rmul__(scalar: float) -> Math.Point3D` | `s * a`: the value scaled by a scalar. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `x` | `float` | X coordinate. |
| `y` | `float` | Y coordinate. |
| `z` | `float` | Z coordinate. |

### Math.Transform3D

> **Full name:** `api.Math.Transform3D` · **Inherits:** `api.Object`

Affine matrix acting on column vectors; A * B applies B first, then A. The implicit last row is (0, 0, 0, 1). Angles are right-handed radians.

**Constructors**

| Constructor | Description |
|---|---|
| `Transform3D()` | Default value (fields at their defaults). |
| `Transform3D(inA: float, inB: float, inC: float, inD: float, inE: float, inF: float, inG: float, inH: float, inI: float, inTx: float, inTy: float, inTz: float)` | Transform with the nine linear coefficients by row (`inA` .. `inI`) and the translation `inTx`, `inTy`, `inTz`. |
| `Transform3D(a=..., b=..., c=..., tx=..., d=..., e=..., f=..., ty=..., g=..., h=..., i=..., tz=...)` | Field values as keywords (any subset), e.g. `Transform3D(a=...)`. |

**Methods**

| Method | Description |
|---|---|
| `Identity() -> Math.Transform3D` *static* | The identity transform. |
| `Translation(dx: float, dy: float, dz: float) -> Math.Transform3D` *static* | Translation by `dx`, `dy`, `dz`. |
| `Translation(offset: Math.Point3D) -> Math.Transform3D` *static* | Translation by the vector `offset`. |
| `Scale(sx: float, sy: float, sz: float) -> Math.Transform3D` *static* | Scaling by `sx`, `sy`, `sz` around the origin. |
| `Scale(sx: float, sy: float, sz: float, center: Math.Point3D) -> Math.Transform3D` *static* | Scaling by `sx`, `sy`, `sz` around `center`. |
| `RotationX(angle: float) -> Math.Transform3D` *static* | Rotation by `angle` radians around the X axis. |
| `RotationY(angle: float) -> Math.Transform3D` *static* | Rotation by `angle` radians around the Y axis. |
| `RotationZ(angle: float) -> Math.Transform3D` *static* | Rotation by `angle` radians around the Z axis. |
| `Rotation(angle: float, axis: Math.Point3D, center: Math.Point3D = Math.Point3D()) -> Math.Transform3D \| None` *static* | Rotation by `angle` radians around the axis `axis` through `center` (right-handed); `None` for a zero axis. |
| `Mirror(origin: Math.Point3D, normal: Math.Point3D) -> Math.Transform3D \| None` *static* | Mirroring across the plane through `origin` with the normal `normal`; `None` for a zero normal. |
| `FromAxes(origin: Math.Point3D, xAxis: Math.Point3D, yAxis: Math.Point3D, zAxis: Math.Point3D) -> Math.Transform3D` *static* | Transform that maps the unit axes to `xAxis`, `yAxis`, `zAxis` and the origin to `origin`. |
| `Then(next: Math.Transform3D) -> Math.Transform3D` | This transform followed by `next` (the same as `next * self`). |
| `Apply(point: Math.Point3D) -> Math.Point3D` | Transforms the point `point` (translation included). |
| `ApplyToVector(vector: Math.Point3D) -> Math.Point3D` | Transforms the vector `vector` (translation ignored). |
| `Determinant() -> float` | Determinant of the linear part (negative for mirroring transforms). |
| `IsInvertible(tolerance: float = 1e-09) -> bool` | True when the determinant is not zero (within `tolerance`). |
| `Inverse() -> Math.Transform3D \| None` | The inverse transform; `None` when the transform cannot be inverted. |
| `ApplyToNormal(normal: Math.Point3D) -> Math.Point3D \| None` | Transforms the surface normal `normal` (inverse transpose, normalized); `None` when the transform cannot be inverted. |
| `GetTranslation() -> Math.Point3D` | Returns the translation. |
| `SetTranslation(offset: Math.Point3D) -> None` | Sets the translation. |
| `GetXAxis() -> Math.Point3D` | Returns the X axis. |
| `GetYAxis() -> Math.Point3D` | Returns the Y axis. |
| `GetZAxis() -> Math.Point3D` | Returns the Z axis. |
| `IsMirrored() -> bool` | True when the transform mirrors (negative determinant). |
| `IsOrthogonal(tolerance: float = 1e-09) -> bool` | True when the linear part is a rotation or mirroring without scaling (within `tolerance`). |
| `IsIdentity(tolerance: float = 1e-09) -> bool` | True when the transform is the identity within `tolerance`. |
| `IsEqual(other: Math.Transform3D, tolerance: float = 1e-09) -> bool` | True when all coefficients match `other` within `tolerance`. |
| `IsFinite() -> bool` | True when no coefficient is infinite or NaN. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `*` | `__mul__(other: Math.Transform3D) -> Math.Transform3D` | `A * B`: the composed transform (B is applied first, then A). |
| `*=` | `__imul__(other: Math.Transform3D) -> Math.Transform3D` | `A *= B`: composes the other transform in place. |
| `()` | `__call__(point: Math.Point3D) -> Math.Point3D` | `T(p)`: applies the transform to the point (same as `Apply`). |

**Fields**

| Field | Type | Description |
|---|---|---|
| `a` | `float` | Row 1, column 1 of the linear part. |
| `b` | `float` | Row 1, column 2 of the linear part. |
| `c` | `float` | Row 1, column 3 of the linear part. |
| `tx` | `float` | X translation. |
| `d` | `float` | Row 2, column 1 of the linear part. |
| `e` | `float` | Row 2, column 2 of the linear part. |
| `f` | `float` | Row 2, column 3 of the linear part. |
| `ty` | `float` | Y translation. |
| `g` | `float` | Row 3, column 1 of the linear part. |
| `h` | `float` | Row 3, column 2 of the linear part. |
| `i` | `float` | Row 3, column 3 of the linear part. |
| `tz` | `float` | Z translation. |

### Math.Line3D

> **Full name:** `api.Math.Line3D` · **Inherits:** `api.Object`

Segment parameter 0 is start and 1 is end; Infinite methods do not clamp it.

**Constructors**

| Constructor | Description |
|---|---|
| `Line3D()` | Default value (fields at their defaults). |
| `Line3D(inStart: Math.Point3D, inEnd: Math.Point3D)` | Segment from `inStart` to `inEnd`. |
| `Line3D(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float)` | Segment from (`x1`, `y1`, `z1`) to (`x2`, `y2`, `z2`). |
| `Line3D(start=..., end=...)` | Field values as keywords (any subset), e.g. `Line3D(start=...)`. |

**Methods**

| Method | Description |
|---|---|
| `Vector() -> Math.Point3D` | Vector from `start` to `end`. |
| `Direction() -> Math.Point3D` | Unit vector from `start` towards `end`. |
| `Length() -> float` | Length of the segment. |
| `LengthSquared() -> float` | Squared length of the segment. |
| `MidPoint() -> Math.Point3D` | Middle of the segment. |
| `PointAt(parameter: float) -> Math.Point3D` | Point at `parameter` (0 = `start`, 1 = `end`; other values extrapolate). |
| `PointAtDistance(distance: float) -> Math.Point3D` | Point at `distance` from `start` along the line. |
| `IsDegenerate(tolerance: float = 1e-09) -> bool` | True when start and end coincide within `tolerance`. |
| `Reversed() -> Math.Line3D` | The segment with `start` and `end` swapped. |
| `Offset(offset: Math.Point3D) -> Math.Line3D` | The segment moved by the vector `offset`. |
| `Transformed(transform: Math.Transform3D) -> Math.Line3D` | The segment transformed by `transform`. |
| `WithLength(length: float) -> Math.Line3D` | Segment with the same start and direction and the length `length`. |
| `Extended(atStart: float, atEnd: float) -> Math.Line3D` | The segment extended by `atStart` before the start and `atEnd` after the end (negative values trim). |
| `ProjectParameter(point: Math.Point3D) -> float` | Parameter of the projection of `point` on the infinite line. |
| `ProjectInfinite(point: Math.Point3D) -> Math.Point3D` | Projection of `point` on the infinite line. |
| `ClosestPoint(point: Math.Point3D) -> Math.Point3D` | Point of the segment closest to `point`. |
| `DistanceTo(point: Math.Point3D) -> float` | Distance from `point` to the segment. |
| `DistanceToInfinite(point: Math.Point3D) -> float` | Distance from `point` to the infinite line. |
| `IsPointOn(point: Math.Point3D, tolerance: float = 1e-09) -> bool` | True when `point` lies on the segment within `tolerance`. |
| `IsPointOnInfinite(point: Math.Point3D, tolerance: float = 1e-09) -> bool` | True when `point` lies on the infinite line within `tolerance`. |
| `IsParallel(other: Math.Line3D, angleTolerance: float = 1e-09) -> bool` | True when the lines are parallel within `angleTolerance`. |
| `IsPerpendicular(other: Math.Line3D, angleTolerance: float = 1e-09) -> bool` | True when the lines are perpendicular within `angleTolerance`. |
| `IsCollinear(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | True when both segments lie on the same infinite line (within `tolerance`). |
| `IntersectInfinite(other: Math.Line3D, tolerance: float = 1e-09) -> Math.Point3D \| None` | Intersection point of the two infinite lines; `None` when they do not meet (parallel or skew). |
| `Intersect(other: Math.Line3D, tolerance: float = 1e-09) -> Math.Point3D \| None` | Intersection point of the two segments; `None` when they do not meet in a single point. |
| `Intersects(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | True when the two segments touch or overlap (collinear overlap included). |
| `DistanceTo(other: Math.Line3D) -> float` | Shortest distance between the two segments. |
| `IsEqual(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | True when start and end match `other` within `tolerance`. |
| `IsEqualIgnoreDirection(other: Math.Line3D, tolerance: float = 1e-09) -> bool` | True when the segments match `other` in either direction within `tolerance`. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `start` | `Math.Point3D` | Start point. |
| `end` | `Math.Point3D` | End point. |

### Math.Plane3D

> **Full name:** `api.Math.Plane3D` · **Inherits:** `api.Object`

Oriented infinite plane with a unit normal. The default plane is XY, normal +Z.

**Constructors**

| Constructor | Description |
|---|---|
| `Plane3D()` | The XY plane with the normal +Z. |

**Methods**

| Method | Description |
|---|---|
| `FromPointNormal(origin: Math.Point3D, normal: Math.Point3D) -> Math.Plane3D \| None` *static* | Plane through `origin` with the normal `normal`; `None` for a zero normal. |
| `FromPoints(first: Math.Point3D, second: Math.Point3D, third: Math.Point3D) -> Math.Plane3D \| None` *static* | Plane through three points (normal by the right-hand rule); `None` for collinear points. |
| `GetOrigin() -> Math.Point3D` | Returns the origin. |
| `GetNormal() -> Math.Point3D` | Returns the normal. |
| `SignedDistanceTo(point: Math.Point3D) -> float` | Signed distance of `point` (positive on the side the normal points to). |
| `DistanceTo(point: Math.Point3D) -> float` | Distance of `point` to the plane. |
| `Project(point: Math.Point3D) -> Math.Point3D` | Projection of `point` onto the plane. |
| `Mirror(point: Math.Point3D) -> Math.Point3D` | Mirror image of `point` across the plane. |
| `Contains(point: Math.Point3D, tolerance: float = 1e-09) -> bool` | True when `point` lies on the plane (within `tolerance`). |
| `Reversed() -> Math.Plane3D` | The same plane with the opposite normal. |
| `Offset(distance: float) -> Math.Plane3D` | The plane moved by `distance` along its normal. |
| `IsParallel(other: Math.Plane3D, angleTolerance: float = 1e-09) -> bool` | True when the planes are parallel within `angleTolerance`. |
| `IsPerpendicular(other: Math.Plane3D, angleTolerance: float = 1e-09) -> bool` | True when the planes are perpendicular within `angleTolerance`. |
| `IsEqual(other: Math.Plane3D, tolerance: float = 1e-09, angleTolerance: float = 1e-09) -> bool` | True when the planes coincide (the normal orientation is ignored) within the tolerances. |
| `IntersectInfinite(line: Math.Line3D, angleTolerance: float = 1e-09) -> Math.Point3D \| None` | Intersection of the infinite line through `line` with the plane; `None` when parallel. |
| `Intersect(line: Math.Line3D, tolerance: float = 1e-09) -> Math.Point3D \| None` | Intersection of the segment `line` with the plane; `None` when the segment does not cross it. |
| `Intersect(other: Math.Plane3D, angleTolerance: float = 1e-09) -> Math.Line3D \| None` | Intersection line of the two planes; `None` when they are parallel. |
| `Transformed(transform: Math.Transform3D) -> Math.Plane3D \| None` | The plane transformed by `transform`; `None` when the transform cannot be inverted. |

## Enumerations

### Math.VertexType

> **Full name:** `api.Math.VertexType` · **Kind:** `IntEnum`

Type of a poly vertex. Values match the Vectorworks VertexType constants.

| Member | Value | Description |
|---|---|---|
| `Corner` | `0` |  |
| `Bezier` | `1` | Quadratic bezier control point. |
| `Cubic` | `2` | Cubic spline control point. |
| `Arc` | `3` | Arc control point with radius (0 = maximum radius). |
| `Radius` | `4` | Radius (tangent) control point. |

### Math.OffsetJoin

> **Full name:** `api.Math.OffsetJoin` · **Kind:** `IntEnum`

Corner style of polygon offsets (`Polygon2D.Offset`).

| Member | Value | Description |
|---|---|---|
| `Miter` | `0` |  |
| `Round` | `1` |  |

## Module functions

Functions of the `api.Math` module (call them as `api.Math.Name(...)`).

| Function | Description |
|---|---|
| `DegToRad(deg: float) -> float` | Converts degrees to radians. |
| `RadToDeg(rad: float) -> float` | Converts radians to degrees. |
| `IsZero(value: float, tolerance: float = 1e-09) -> bool` | True when `abs(value) <= tolerance`. |
| `AreEqual(a: float, b: float, tolerance: float = 1e-09) -> bool` | True when `a` and `b` differ by at most `tolerance`. |
| `IsLess(a: float, b: float, tolerance: float = 1e-09) -> bool` | True when `a < b - tolerance`. |
| `IsGreater(a: float, b: float, tolerance: float = 1e-09) -> bool` | True when `a > b + tolerance`. |
| `IsBetween(v: float, lo: float, hi: float, tolerance: float = 1e-09) -> bool` | True when `v` lies between `lo` and `hi` (in either order), with the tolerance `tolerance`. |
| `Sign(v: float) -> float` | Sign of `v`: -1, 0 or 1. |
| `Clamp(v: float, lo: float, hi: float) -> float` | `v` limited to the range `[lo, hi]`. |
| `Lerp(a: float, b: float, t: float) -> float` | Linear interpolation: `a + (b - a) * t`. |
| `NormalizeAngle(angle: float) -> float` | Angle in [0, 2*pi). |
| `NormalizeAngleSigned(angle: float) -> float` | The angle normalized to `(-pi, pi]`. |
| `AngleDelta(from_: float, to: float) -> float` | Counter-clockwise angle from `from` to `to`, in [0, 2*pi). |
| `AnglesAreEqual(a: float, b: float, tolerance: float = 1e-09) -> bool` | True when the angles `a` and `b` are equal (modulo 2*pi) within `tolerance`. |

## Module constants

| Constant | Type | Value | Description |
|---|---|---|---|
| `api.Math.kPi` | `float` | `3.14159265358979323846` | The constant pi. |
| `api.Math.kTwoPi` | `float` | `2.0* `kPi`` | 2 * pi (a full turn in radians). |
| `api.Math.kHalfPi` | `float` | `0.5* `kPi`` | pi / 2 (a quarter turn in radians). |
| `api.Math.kEpsilon` | `float` | `1e-9` | Default distance tolerance. |
| `api.Math.kAngleEpsilon` | `float` | `1e-9` | Default angle tolerance (radians). |

## Aliases and implicit conversions

- `api.Math.Vector2D` is another name of [`Math.Point2D`](#mathpoint2d) (the same class object).
- `api.Math.Vector3D` is another name of [`Math.Point3D`](#mathpoint3d) (the same class object).
- A [`Math.Point2D`](#mathpoint2d) is accepted wherever a [`Point2D`](Attributes.md#point2d) argument is expected (implicit conversion).
- A [`Point2D`](Attributes.md#point2d) is accepted wherever a [`Math.Point2D`](#mathpoint2d) argument is expected (implicit conversion).
- A [`Math.Point3D`](#mathpoint3d) is accepted wherever a [`Point3D`](UIAutomation.md#point3d) argument is expected (implicit conversion).
- A [`Point3D`](UIAutomation.md#point3d) is accepted wherever a [`Math.Point3D`](#mathpoint3d) argument is expected (implicit conversion).

---

[Back to the index](README.md) · [Back to top](#math--standalone-2d-and-3d-math-apimath)
