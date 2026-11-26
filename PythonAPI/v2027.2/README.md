**English** • [Deutsch](../../PythonAPI.de/v2027.2/README.md) • [日本語](../../PythonAPI.ja/v2027.2/README.md)

# Vectorworks Python API (`api`) — reference for Vectorworks 2027 Update 2

This reference documents the object-oriented Python module `api` that Vectorworks provides for scripts and AI workflows. It is organized by feature group: one page per group, with a table of contents at the top of every page and the same layout for every class.

## Table of contents

- [Getting started](#getting-started)
- [Conventions](#conventions)
  - [Modules](#modules)
  - [Reading the signatures](#reading-the-signatures)
  - [Calling functions](#calling-functions)
  - [Records](#records)
  - [Enumerations](#enumerations)
  - [Handles and objects](#handles-and-objects)
  - [Copying, printing and hashing](#copying-printing-and-hashing)
  - [Callbacks](#callbacks)
  - [Errors](#errors)
- [API tree](#api-tree)
- [Contents by group](#contents-by-group)
- [Index A–Z](#index-az)
- [Page layout](#page-layout)
- [Statistics](#statistics)

## Getting started

```python
import api
from api.Math import Point2D

doc = api.Document()
if doc.IsOpen():
    for h in doc.GetSelection():
        obj = api.PrimitiveObject(h)
        print(obj.GetName(), obj.GetBounds())
```

- Start with [`api.Document`](DocumentAccess.md#document): the active drawing, its selection, layers, stories, classes and preferences.
- Shared drawing-object operations are documented on [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject). Follow each class's inheritance information: for example, [`WorksheetObject`](ObjectsAnnotation.md#worksheetobject) derives from `TypedResource`, not `PrimitiveObject`.
- Pure math values live directly in the submodule [`api.Math`](ObjectPrimitives.Math.md); they do not create drawing objects.
- `help(api.Document)` in Vectorworks prints the signatures of a class.

Use only `api` and `api.Math` for the Vectorworks operations described here. Do not mix calls to the separate `vs` interface or use it as a fallback for missing features. Standard-library imports are fine; report unsupported operations rather than inventing API calls.

[Script resources and palettes](Scripting.md) can be managed but scripts cannot be executed through `api`. Automation of already-open dialogs and the deferred helpers `RunLater` / `RunOnEventLoop` are unavailable; [dialog creation, alerts and standard dialogs](UILayoutCreate.md) remain supported. See [AI-CONTEXT.md](AI-CONTEXT.md) for the complete usage rules and recipes.

## Conventions

| Topic | Convention |
|---|---|
| Results | Getters return `None` when a value cannot be obtained, except that handle getters return a null handle, collection getters an empty list and count getters zero. Drawing-object factories return invalid objects on failure. Most setters and actions return `True` / `False`; check each signature and its result. |
| Units | World lengths and coordinates are millimetres, regardless of document units. Use `Document.UnitsToWorld` / `Document.WorldToUnits` to convert document units. Angles are radians, counter-clockwise from +X, unless specified otherwise. |
| Unit exceptions | `Marker.angle`, `DropShadow.angle` and `RoofObject.Edge.slope` use degrees; `Marker.length` / `Marker.width` use page inches. `*Mils` line weights use 1/1000 inch. Raw plug-in angle parameters read/written with `GetParamReal` / `SetParamReal` use degrees; length parameters use world units. |
| Indexes | Zero-based, except worksheet rows and columns, which are one-based. |
| Colors | `ColorRGB` channels are 0–65535; use `ColorRGB.FromRGB8` / `Red8()` for 8-bit values. Color indices are palette indices, not RGB values. Opacity is 0–100 (`api.kMaxOpacity`). |
| Strings | Python `str`, exchanged as UTF-8. Name lookups ignore case, but pass plug-in universal names exactly. |
| Handles | Pass `None` for a null handle argument. A returned null `api.Handle` is falsy: test `if h:`, not `h is None`. Object classes are lightweight views of a handle; `bool(obj)` is equivalent to `IsValid()`. |
| Undo | Drawing changes require an undo event and the appropriate object registrations; read-only scripts must not start an event. See the [undo workflow](AI-CONTEXT.md#3-undo---required-around-every-drawing-change) for `StartUndoEvent(isRevertible=True)`, rollback and application-managed events. |
| Names | Members whose names are Python keywords end with an underscore (`None_`), and so do keyword-like argument names (`from_`). |
| Records | Value types are Python-owned copies: change them, then pass them back to the setter. They can be constructed from field values (`api.ColorRGB(red=65535)`). |
| Enumerations | `IntEnum` (`api.Descend` is an `IntFlag`); plain integers are accepted. |
| Arguments | Every parameter has a keyword name; parameters with defaults can be omitted; tuples, lists and dicts are accepted for record arguments. |
| Signatures | `Name(param: type = default) -> result`; *static* marks static methods; `T \| None` is an optional result. |

### Modules

| Name | What it is |
|---|---|
| `api` | The module. Start with `api.Document()`. |
| `api.Math` | Direct submodule of `api` with standalone 2D/3D math ([Math](ObjectPrimitives.Math.md)); `import api.Math` and `from api.Math import Point2D` work. It is not nested under `ObjectPrimitives`. |
| `api.Object` | Base class of every `api` class (see [Copying, printing and hashing](#copying-printing-and-hashing)). |
| `api.Handle` | A Vectorworks object handle. Test returned handles for truth rather than comparing them with `None`. |

### Reading the signatures

The signatures use these types:

| Type | Meaning |
|---|---|
| `bool`, `int`, `float`, `str` | Python built-in values. An `int` is accepted where a `float` is expected. |
| `Handle` | A Vectorworks object handle (`api.Handle`). Pass `None` for a null handle argument; returned null handles are falsy. Any object with `GetHandle()` is accepted as well. |
| `T \| None` | An optional value: `None` means "no value". |
| `list[T]` | A list (a list or a tuple is accepted as argument). |
| `tuple[T * N]` | A tuple of exactly N values. |
| `tuple[A, B]` | A pair of values. |
| `dict[K, V]` | A dictionary. |
| `callable(A, ...)` | Any Python callable that takes the listed arguments (see [Callbacks](#callbacks)). |
| `bytes` | `bytes`, `bytearray` or any other buffer (not `str`). |
| `type` | An `api` class, for example `api.ArcObject` in `api.Document.As(api.ArcObject, h)`; only classes with a static `Is(h)` and a constructor from a handle qualify. |
| `object` | Any Python object; the method description tells what is returned. |
| enumeration names | `IntEnum` / `IntFlag` classes; plain integers are accepted. |
| class names | `api` classes; record arguments also accept tuples, lists and dicts (see [Records](#records)). |

Default values are shown as Python expressions (`2**64 - 1` means "no limit"). Methods with several rows of the same name accept several argument lists (overloads).

### Calling functions

- **Overloads:** when a method accepts several argument lists, the first one that fits the arguments is used, first with exact types, then with the conversions described here. When record types distinguish overloads, construct the type explicitly: a tuple passed to `ToolControl.Click` selects `Point2D`, so use `api.Point3D(...)` or `api.ViewPoint(...)` for the other coordinate types.
- **Keywords and defaults:** every parameter can be passed by keyword (using the names in the signatures); parameters with a default value can be omitted.
- **Static methods:** methods marked *static* can be called on the class (`api.ArcObject.Create(...)`) or through an instance. When a name has both static and instance rows, call it through an instance.
- **Conversions:** a record argument can be given as a tuple or list (the values of a constructor), as a dict (field values) or as a compatible record (`api.Math.Point2D` and `api.Point2D`, as well as `api.Math.Point3D` and `api.Point3D`, convert into each other); an `int` is accepted for a `bool` or a `float`; any object with a `GetHandle()` method is accepted where a `Handle` is expected.
- **Results:** results are new Python values, except for methods that change a value in place and return it (for example `Math.Point2D.Normalize()`): they return the same Python object, so calls can be chained.
- **Operators:** comparison and arithmetic operators return `NotImplemented` for unsupported operands, so Python can try the reflected operation.

### Records

Records (value types such as `api.ColorRGB`, `api.WallObject.Heights`, `api.Math.Point2D`) are Python-owned values. Changing a record never changes the drawing: pass it back to the setter it came from.

When no constructor accepts the arguments, a record can also be constructed from field values: all fields positionally (in the order of the Fields tables, fields of the base class first) or any fields as keywords, for example `api.ColorRGB(red=65535)`. Classes with neither constructors nor fields cannot be constructed from Python.

A field whose type is itself a record reads as a live view into its owner (`rect.origin.x = 1` changes `rect`); fields of other types (numbers, strings, lists, optional values) read as copies. Fields cannot be deleted.

### Enumerations

Enumerations are `enum.IntEnum` classes (`api.Descend` is an `enum.IntFlag`: combine its members with `|`). Nested enumerations live in their class (`api.TextObject.HorizontalAlignment`). Members whose names are Python keywords end with `_` (`api.Descend.None_`). Plain integers are accepted as arguments, and values without a member come back as integers.

### Handles and objects

Object handles are `api.Handle` values. Pass `None` for a null handle argument, but test returned handles with `if h:`: a null handle is not `None`. Handle compatibility does not justify mixing `api` and `vs`. The object classes are lightweight views of a handle: they do not own the drawing object. Most have a static `Is(h)` and a constructor from a handle; constructing one from a handle of the wrong kind gives an invalid object (`IsValid()` / `bool(obj)` is `False`). `api.Document.As(type, h)` returns a typed object or `None`.

The base views `PrimitiveObject(h)`, `ArchitectObject(h)`, `LandmarkObject(h)` and `AnnotationObject(h)` accept any non-null handle; concrete classes check the object kind. `Delete()` invalidates the view on which it is called. Never use other views or handles of the deleted object.

### Copying, printing and hashing

Every `api` class derives from `api.Object`, which provides:

| Member | Description |
|---|---|
| `copy.copy(x)` / `copy.deepcopy(x)` | A copy of the value. For an object class this copies the view (the handle), **not** the drawing object; use `Duplicate()` to duplicate drawing objects. Raises `TypeError` for classes that cannot be copied (for example `ResourceList`). |
| `repr(x)` | Records print their fields (`api.ColorRGB(red=0, green=0, blue=0)`), object classes their handle (`<api.ArcObject handle=0x...>`), instances whose `__init__` was not called `<... (not initialized)>`. |
| `hash(x)` | Object classes hash by their handle, so they can be dictionary keys or set members; records are not hashable. Drawing objects, layers, classes and resources compare by handle with `==`. Value-type equality is documented in the Operators tables; other Python objects compare by identity. |

### Callbacks

Parameters of type `callable(...)` take any Python callable (for example the traversal `Document.ForEachObject`). The callable is called synchronously and its return value is ignored; it cannot stop traversal early. Use the list-returning counterpart when you need to stop early. When a call raises, the remaining calls are skipped and the exception propagates once the method returns.

### Errors

Operational failures use the documented return values; always check results. Python usage and conversion errors and the failed geometry operations listed below raise exceptions as described below, and callback exceptions propagate to the caller.

| Situation | Python exception |
|---|---|
| No argument list of the method fits the arguments | `TypeError`, listing every signature of the method. |
| Constructing a class that cannot be constructed from Python, or using an instance whose `__init__` was not called (for example in a subclass) | `TypeError`. |
| Setting a field to a value of the wrong type, deleting a field | `TypeError`. |
| Copying a class that cannot be copied | `TypeError`. |
| An index out of range of a math value (for example `Polygon2D`) | `IndexError`. |
| A failed geometry operation: `Math.Polygon2D` `Union`, `Intersection`, `Difference`, `SymmetricDifference`, `Offset`; `PolyObject` `BooleanUnion`, `BooleanIntersection`, `BooleanDifference`, `BooleanSymmetricDifference`, `CombineShapes` | `RuntimeError` with a message. |
| A result that cannot be converted | `RuntimeError`. |
| The module could not be initialized | `ImportError` on `import api`. |

## API tree

`Math` is a direct submodule of `api`. The other entries below are documentation groups for names exposed directly on `api` (for example `api.Document` and `api.PrimitiveObject`), not Python submodules. Reference filenames do not define Python namespaces: `ObjectPrimitives.Math.md` documents `api.Math`.

```text
api
├── Math  (api.Math)               → ObjectPrimitives.Math.md
├── DocumentAccess                 → DocumentAccess.md
├── Attributes                     → Attributes.md
├── ObjectPrimitives               → ObjectPrimitives.md
├── Objects3D                      → Objects3D.md
├── ObjectsAnnotation              → ObjectsAnnotation.md
├── ObjectsArchitect               → ObjectsArchitect.md
├── ObjectsConnectCAD              → ObjectsConnectCAD.md
├── ObjectsLandmark                → ObjectsLandmark.md
├── ObjectsSpotlight               → ObjectsSpotlight.md
├── Resources                      → Resources.md
├── Scripting                      → Scripting.md
├── UIAutomation                   → UIAutomation.md
└── UILayoutCreate                 → UILayoutCreate.md
```

## Contents by group

- **[DocumentAccess](DocumentAccess.md)** — The active document: selection, objects, layers, stories, classes, view, units, undo and preferences.
  - Classes:
    - [`TextStyleData`](DocumentAccess.md#textstyledata)
    - [`ProgramVariables`](DocumentAccess.md#programvariables)
    - [`DisplaySettings`](DocumentAccess.md#displaysettings)
    - [`EditingSettings`](DocumentAccess.md#editingsettings)
    - [`SnapSettings`](DocumentAccess.md#snapsettings)
    - [`GridSettings`](DocumentAccess.md#gridsettings)
    - [`StackLayersSettings`](DocumentAccess.md#stacklayerssettings)
    - [`UnitSettings`](DocumentAccess.md#unitsettings)
    - [`TextDefaults`](DocumentAccess.md#textdefaults)
    - [`DefaultAttributes`](DocumentAccess.md#defaultattributes)
    - [`LayerContents`](DocumentAccess.md#layercontents)
    - [`Layer`](DocumentAccess.md#layer)
    - [`StoryLevel`](DocumentAccess.md#storylevel)
    - [`StoryLevelTemplate`](DocumentAccess.md#storyleveltemplate)
    - [`Story`](DocumentAccess.md#story)
    - [`Document`](DocumentAccess.md#document)
  - Enumerations: [`Traverse`](DocumentAccess.md#traverse) · [`Descend`](DocumentAccess.md#descend) · [`LayerType`](DocumentAccess.md#layertype) · [`LayerVisibility`](DocumentAccess.md#layervisibility) · [`VisibilityOptions`](DocumentAccess.md#visibilityoptions) · [`StoryElevationChangeMode`](DocumentAccess.md#storyelevationchangemode) · [`UndoMethod`](DocumentAccess.md#undomethod) · [`AngularUnit`](DocumentAccess.md#angularunit) · [`TextJustification`](DocumentAccess.md#textjustification) · [`TextVerticalAlignment`](DocumentAccess.md#textverticalalignment) · [`TextLineSpacing`](DocumentAccess.md#textlinespacing)
- **[Attributes](Attributes.md)** — Pen, fill, fill mapping, markers, drop shadow, object attributes, classes and the attribute value types.
  - Classes:
    - [`Point2D`](Attributes.md#point2d)
    - [`ColorRGB`](Attributes.md#colorrgb)
    - [`ColorPair`](Attributes.md#colorpair)
    - [`ObjectColors`](Attributes.md#objectcolors)
    - [`Marker`](Attributes.md#marker)
    - [`DropShadow`](Attributes.md#dropshadow)
    - [`WallTextures`](Attributes.md#walltextures)
    - [`RoofTextures`](Attributes.md#rooftextures)
    - [`AttributesBase`](Attributes.md#attributesbase)
    - [`PenAttributes`](Attributes.md#penattributes)
    - [`FillAttributes`](Attributes.md#fillattributes)
    - [`FillMappingAttributes`](Attributes.md#fillmappingattributes) — [`Frame`](Attributes.md#fillmappingattributesframe)
    - [`MarkerAttributes`](Attributes.md#markerattributes)
    - [`DropShadowAttributes`](Attributes.md#dropshadowattributes)
    - [`ClassAttributes`](Attributes.md#classattributes)
    - [`ObjectAttributes`](Attributes.md#objectattributes)
  - Enumerations: [`PenStyleKind`](Attributes.md#penstylekind) · [`FillType`](Attributes.md#filltype) · [`MarkerShape`](Attributes.md#markershape) · [`MarkerFill`](Attributes.md#markerfill) · [`MarkerBase`](Attributes.md#markerbase) · [`MarkerHalfTick`](Attributes.md#markerhalftick) · [`MarkerThicknessBasis`](Attributes.md#markerthicknessbasis) · [`MarkerThicknessUnits`](Attributes.md#markerthicknessunits) · [`DropShadowUnits`](Attributes.md#dropshadowunits) · [`ClassVisibility`](Attributes.md#classvisibility) · [`ObjectType`](Attributes.md#objecttype)
  - [Module constants](Attributes.md#module-constants): `kMaxOpacity`
- **[ObjectPrimitives](ObjectPrimitives.md)** — The common object base (PrimitiveObject) and 2D objects: lines, rectangles, arcs, circles, polygons, polylines, groups, plug-in objects, text.
  - Classes:
    - [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) — [`Bounds3D`](ObjectPrimitives.md#primitiveobjectbounds3d)
    - [`Locus2DObject`](ObjectPrimitives.md#locus2dobject)
    - [`Line2DObject`](ObjectPrimitives.md#line2dobject)
    - [`RectangularObject`](ObjectPrimitives.md#rectangularobject)
    - [`RectangleObject`](ObjectPrimitives.md#rectangleobject)
    - [`CornerDiameters`](ObjectPrimitives.md#cornerdiameters)
    - [`RoundRectObject`](ObjectPrimitives.md#roundrectobject)
    - [`ArcObject`](ObjectPrimitives.md#arcobject)
    - [`CircleObject`](ObjectPrimitives.md#circleobject)
    - [`PolyObject`](ObjectPrimitives.md#polyobject) — [`BooleanOperation`](ObjectPrimitives.md#polyobjectbooleanoperation)
    - [`PolygonObject`](ObjectPrimitives.md#polygonobject)
    - [`PolylineObject`](ObjectPrimitives.md#polylineobject)
    - [`GroupObject`](ObjectPrimitives.md#groupobject)
    - [`ParametricObject`](ObjectPrimitives.md#parametricobject) — [`PluginKind`](ObjectPrimitives.md#parametricobjectpluginkind)
    - [`TextObject`](ObjectPrimitives.md#textobject) — [`StyleRun`](ObjectPrimitives.md#textobjectstylerun) · [`TabStop`](ObjectPrimitives.md#textobjecttabstop) · [`HorizontalAlignment`](ObjectPrimitives.md#textobjecthorizontalalignment) · [`VerticalAlignment`](ObjectPrimitives.md#textobjectverticalalignment) · [`Spacing`](ObjectPrimitives.md#textobjectspacing) · [`TabAlignment`](ObjectPrimitives.md#textobjecttabalignment)
- **[Math (`api.Math`)](ObjectPrimitives.Math.md)** — The api.Math submodule: points/vectors, transforms, rectangles, lines, planes, circles, arcs, polygons, utilities.
  - Classes:
    - [`Math.Point2D`](ObjectPrimitives.Math.md#mathpoint2d)
    - [`Math.Transform2D`](ObjectPrimitives.Math.md#mathtransform2d)
    - [`Math.Rect2D`](ObjectPrimitives.Math.md#mathrect2d)
    - [`Math.RotatedRect2D`](ObjectPrimitives.Math.md#mathrotatedrect2d)
    - [`Math.Line2D`](ObjectPrimitives.Math.md#mathline2d) — [`Intersection`](ObjectPrimitives.Math.md#mathline2dintersection)
    - [`Math.Circle2D`](ObjectPrimitives.Math.md#mathcircle2d)
    - [`Math.Arc2D`](ObjectPrimitives.Math.md#matharc2d)
    - [`Math.PolyVertex`](ObjectPrimitives.Math.md#mathpolyvertex)
    - [`Math.Polygon2D`](ObjectPrimitives.Math.md#mathpolygon2d) — [`CurveLocation`](ObjectPrimitives.Math.md#mathpolygon2dcurvelocation)
    - [`Math.Point3D`](ObjectPrimitives.Math.md#mathpoint3d)
    - [`Math.Transform3D`](ObjectPrimitives.Math.md#mathtransform3d)
    - [`Math.Line3D`](ObjectPrimitives.Math.md#mathline3d)
    - [`Math.Plane3D`](ObjectPrimitives.Math.md#mathplane3d)
  - Enumerations: [`Math.VertexType`](ObjectPrimitives.Math.md#mathvertextype) · [`Math.OffsetJoin`](ObjectPrimitives.Math.md#mathoffsetjoin)
  - [Module functions](ObjectPrimitives.Math.md#module-functions): `AngleDelta`, `AnglesAreEqual`, `AreEqual`, `Clamp`, `DegToRad`, `IsBetween`, `IsGreater`, `IsLess`, `IsZero`, `Lerp`, `NormalizeAngle`, `NormalizeAngleSigned`, `RadToDeg`, `Sign`
  - [Module constants](ObjectPrimitives.Math.md#module-constants): `kPi`, `kTwoPi`, `kHalfPi`, `kEpsilon`, `kAngleEpsilon`
- **[Objects3D](Objects3D.md)** — Extrudes, multiple extrudes, sweeps, solids, primitives (sphere, cone, ...), NURBS, 3D polygons, meshes, shells.
  - Classes:
    - [`ExtrudeObject`](Objects3D.md#extrudeobject) — [`Values`](Objects3D.md#extrudeobjectvalues) · [`Transform`](Objects3D.md#extrudeobjecttransform)
    - [`SweepObject`](Objects3D.md#sweepobject) — [`Values`](Objects3D.md#sweepobjectvalues)
    - [`MultiExtrudeObject`](Objects3D.md#multiextrudeobject)
    - [`SurfaceModelObject`](Objects3D.md#surfacemodelobject) — [`PathOptions`](Objects3D.md#surfacemodelobjectpathoptions)
    - [`GenericSolidObject`](Objects3D.md#genericsolidobject) — [`HistoryStep`](Objects3D.md#genericsolidobjecthistorystep) · [`Operation`](Objects3D.md#genericsolidobjectoperation)
    - [`ShellObject`](Objects3D.md#shellobject)
    - [`Polygon3DObject`](Objects3D.md#polygon3dobject) — [`Plane`](Objects3D.md#polygon3dobjectplane) · [`ClosestPoint`](Objects3D.md#polygon3dobjectclosestpoint)
    - [`MeshObject`](Objects3D.md#meshobject) — [`Face`](Objects3D.md#meshobjectface) · [`Part`](Objects3D.md#meshobjectpart) · [`Smoothing`](Objects3D.md#meshobjectsmoothing)
    - [`SolidPrimitiveObject`](Objects3D.md#solidprimitiveobject) — [`Kind`](Objects3D.md#solidprimitiveobjectkind)
    - [`SphereObject`](Objects3D.md#sphereobject)
    - [`HemisphereObject`](Objects3D.md#hemisphereobject)
    - [`ConeObject`](Objects3D.md#coneobject) — [`Radii`](Objects3D.md#coneobjectradii)
    - [`NurbsCurveObject`](Objects3D.md#nurbscurveobject) — [`Location`](Objects3D.md#nurbscurveobjectlocation)
    - [`NurbsSurfaceObject`](Objects3D.md#nurbssurfaceobject)
- **[ObjectsAnnotation](ObjectsAnnotation.md)** — Dimensions (linear, angular, arc length, radial), center marks, data tags, title block borders, worksheets.
  - Classes:
    - [`AnnotationObject`](ObjectsAnnotation.md#annotationobject)
    - [`DataTagObject`](ObjectsAnnotation.md#datatagobject) — [`LeaderType`](ObjectsAnnotation.md#datatagobjectleadertype) · [`HorizontalPosition`](ObjectsAnnotation.md#datatagobjecthorizontalposition) · [`MoveBehaviour`](ObjectsAnnotation.md#datatagobjectmovebehaviour)
    - [`TitleBlockBorderObject`](ObjectsAnnotation.md#titleblockborderobject) — [`Revision`](ObjectsAnnotation.md#titleblockborderobjectrevision)
    - [`DimensionObject`](ObjectsAnnotation.md#dimensionobject)
    - [`LinearDimensionObject`](ObjectsAnnotation.md#lineardimensionobject)
    - [`AngularDimensionObject`](ObjectsAnnotation.md#angulardimensionobject)
    - [`ArcLengthDimensionObject`](ObjectsAnnotation.md#arclengthdimensionobject)
    - [`RadialDimensionObject`](ObjectsAnnotation.md#radialdimensionobject)
    - [`CenterMarkObject`](ObjectsAnnotation.md#centermarkobject)
    - [`WorksheetObject`](ObjectsAnnotation.md#worksheetobject) — [`Range`](ObjectsAnnotation.md#worksheetobjectrange) · [`NumberFormat`](ObjectsAnnotation.md#worksheetobjectnumberformat) · [`TextFormat`](ObjectsAnnotation.md#worksheetobjecttextformat) · [`Fill`](ObjectsAnnotation.md#worksheetobjectfill) · [`Borders`](ObjectsAnnotation.md#worksheetobjectborders)
  - Enumerations: [`DimensionKind`](ObjectsAnnotation.md#dimensionkind) · [`DimensionTolerance`](ObjectsAnnotation.md#dimensiontolerance)
- **[ObjectsArchitect](ObjectsArchitect.md)** — Architectural objects: walls, roofs, slabs, windows, doors, columns and stairs.
  - Classes:
    - [`ArchitectObject`](ObjectsArchitect.md#architectobject)
    - [`WallObject`](ObjectsArchitect.md#wallobject) — [`Heights`](ObjectsArchitect.md#wallobjectheights) · [`HeightBound`](ObjectsArchitect.md#wallobjectheightbound) · [`Caps`](ObjectsArchitect.md#wallobjectcaps) · [`BoundStatus`](ObjectsArchitect.md#wallobjectboundstatus) · [`BoundKind`](ObjectsArchitect.md#wallobjectboundkind)
    - [`SlabObject`](ObjectsArchitect.md#slabobject)
    - [`RoofObject`](ObjectsArchitect.md#roofobject) — [`Attributes`](ObjectsArchitect.md#roofobjectattributes) · [`Accessories`](ObjectsArchitect.md#roofobjectaccessories) · [`Edge`](ObjectsArchitect.md#roofobjectedge) · [`MiterType`](ObjectsArchitect.md#roofobjectmitertype)
    - [`WindowObject`](ObjectsArchitect.md#windowobject)
    - [`DoorObject`](ObjectsArchitect.md#doorobject)
    - [`ColumnObject`](ObjectsArchitect.md#columnobject)
    - [`StairObject`](ObjectsArchitect.md#stairobject)
- **[ObjectsConnectCAD](ObjectsConnectCAD.md)** — ConnectCAD schematic devices (created from JSON descriptions), sockets, device types, signal and connector types.
  - Classes:
    - [`ConnectCADLibrary`](ObjectsConnectCAD.md#connectcadlibrary) — [`Signal`](ObjectsConnectCAD.md#connectcadlibrarysignal) · [`Connector`](ObjectsConnectCAD.md#connectcadlibraryconnector) · [`Validation`](ObjectsConnectCAD.md#connectcadlibraryvalidation) · [`DeviceDefinition`](ObjectsConnectCAD.md#connectcadlibrarydevicedefinition)
    - [`ConnectCADSocketObject`](ObjectsConnectCAD.md#connectcadsocketobject)
    - [`ConnectCADDeviceObject`](ObjectsConnectCAD.md#connectcaddeviceobject) — [`CreateResult`](ObjectsConnectCAD.md#connectcaddeviceobjectcreateresult) · [`AddSocketResult`](ObjectsConnectCAD.md#connectcaddeviceobjectaddsocketresult) · [`DeviceTypeResult`](ObjectsConnectCAD.md#connectcaddeviceobjectdevicetyperesult)
- **[ObjectsLandmark](ObjectsLandmark.md)** — Landmark objects: plants, landscape areas, site models and modifiers, stakes, hardscapes, property lines, existing trees.
  - Classes:
    - [`LandmarkObject`](ObjectsLandmark.md#landmarkobject)
    - [`PlantObject`](ObjectsLandmark.md#plantobject) — [`Config`](ObjectsLandmark.md#plantobjectconfig) · [`TagDisplay`](ObjectsLandmark.md#plantobjecttagdisplay)
    - [`LandscapeAreaObject`](ObjectsLandmark.md#landscapeareaobject) — [`PlantDisplay2D`](ObjectsLandmark.md#landscapeareaobjectplantdisplay2d) · [`DrawingMode`](ObjectsLandmark.md#landscapeareaobjectdrawingmode) · [`AreaUnits`](ObjectsLandmark.md#landscapeareaobjectareaunits)
    - [`SiteModelObject`](ObjectsLandmark.md#sitemodelobject) — [`Display2D`](ObjectsLandmark.md#sitemodelobjectdisplay2d) · [`Display3D`](ObjectsLandmark.md#sitemodelobjectdisplay3d)
    - [`SiteModifierObject`](ObjectsLandmark.md#sitemodifierobject) — [`Config`](ObjectsLandmark.md#sitemodifierobjectconfig) · [`ApplyTo`](ObjectsLandmark.md#sitemodifierobjectapplyto)
    - [`StakeObject`](ObjectsLandmark.md#stakeobject) — [`Mode`](ObjectsLandmark.md#stakeobjectmode) · [`SiteModel`](ObjectsLandmark.md#stakeobjectsitemodel)
    - [`HardscapeObject`](ObjectsLandmark.md#hardscapeobject) — [`Mode3D`](ObjectsLandmark.md#hardscapeobjectmode3d)
    - [`PropertyLineObject`](ObjectsLandmark.md#propertylineobject) — [`AreaUnits`](ObjectsLandmark.md#propertylineobjectareaunits)
    - [`ExistingTreeObject`](ObjectsLandmark.md#existingtreeobject) — [`Origin`](ObjectsLandmark.md#existingtreeobjectorigin) · [`TreeProtection`](ObjectsLandmark.md#existingtreeobjecttreeprotection) · [`Condition`](ObjectsLandmark.md#existingtreeobjectcondition) · [`SULE`](ObjectsLandmark.md#existingtreeobjectsule) · [`Significance`](ObjectsLandmark.md#existingtreeobjectsignificance) · [`Action`](ObjectsLandmark.md#existingtreeobjectaction)
- **[ObjectsSpotlight](ObjectsSpotlight.md)** — Spotlight lighting devices and the GDTF fixture-type library (import, available modes).
  - Classes:
    - [`LightingDeviceObject`](ObjectsSpotlight.md#lightingdeviceobject)
    - [`GDTFLibrary`](ObjectsSpotlight.md#gdtflibrary) — [`Entry`](ObjectsSpotlight.md#gdtflibraryentry) · [`ImportResult`](ObjectsSpotlight.md#gdtflibraryimportresult)
- **[Resources](Resources.md)** — The Resource Manager side: resources of any kind, resource lists and import, and typed resources (hatches, symbols, styles, ...).
  - Classes:
    - [`Resource`](Resources.md#resource)
    - [`ResourceList`](Resources.md#resourcelist) — [`Entry`](Resources.md#resourcelistentry) · [`ImportResult`](Resources.md#resourcelistimportresult)
    - [`TypedResource`](Resources.md#typedresource)
    - [`HatchLevel`](Resources.md#hatchlevel)
    - [`Hatch`](Resources.md#hatch)
    - [`GradientSegment`](Resources.md#gradientsegment)
    - [`Gradient`](Resources.md#gradient)
    - [`Tile`](Resources.md#tile)
    - [`ImageFill`](Resources.md#imagefill) — [`Compression`](Resources.md#imagefillcompression)
    - [`LineType`](Resources.md#linetype)
    - [`RecordField`](Resources.md#recordfield)
    - [`RecordFormat`](Resources.md#recordformat)
    - [`Texture`](Resources.md#texture) — [`Part`](Resources.md#texturepart)
    - [`RenderStyle`](Resources.md#renderstyle)
    - [`RenderBackground`](Resources.md#renderbackground) — [`Kind`](Resources.md#renderbackgroundkind)
    - [`TextStyle`](Resources.md#textstyle)
    - [`WallStyle`](Resources.md#wallstyle)
    - [`SlabStyle`](Resources.md#slabstyle)
    - [`RoofStyle`](Resources.md#roofstyle)
    - [`ViewportStyle`](Resources.md#viewportstyle)
    - [`BuildingMaterial`](Resources.md#buildingmaterial)
    - [`DataVisualization`](Resources.md#datavisualization)
    - [`ResourceFolderPath`](Resources.md#resourcefolderpath)
    - [`ResourceFolder`](Resources.md#resourcefolder)
    - [`SymbolDefinition`](Resources.md#symboldefinition) — [`GeometryType`](Resources.md#symboldefinitiongeometrytype) · [`InsertMode`](Resources.md#symboldefinitioninsertmode) · [`BreakMode`](Resources.md#symboldefinitionbreakmode)
    - [`WorksheetCell`](Resources.md#worksheetcell)
    - [`WorksheetCellContent`](Resources.md#worksheetcellcontent)
    - [`Worksheet`](Resources.md#worksheet)
  - Enumerations: [`ResourceType`](Resources.md#resourcetype) · [`ContentFolder`](Resources.md#contentfolder) · [`ImportConflict`](Resources.md#importconflict) · [`RecordFieldType`](Resources.md#recordfieldtype)
- **[Scripting](Scripting.md)** — Script resources (VectorScript / Python) and script palettes stored in the document.
  - Classes:
    - [`ScriptResource`](Scripting.md#scriptresource)
    - [`ScriptPalette`](Scripting.md#scriptpalette)
  - Enumerations: [`ScriptLanguage`](Scripting.md#scriptlanguage)
- **[UIAutomation](UIAutomation.md)** — Drive the user interface: tools and their activation, Tool bar (mode bar), tool input, menu commands and chunks, Object Info palette controls.
  - Classes:
    - [`Point3D`](UIAutomation.md#point3d)
    - [`ViewPoint`](UIAutomation.md#viewpoint)
    - [`ViewSize`](UIAutomation.md#viewsize)
    - [`ToolPoint`](UIAutomation.md#toolpoint)
    - [`ModeButtonDefinition`](UIAutomation.md#modebuttondefinition)
    - [`Tool`](UIAutomation.md#tool)
    - [`ModeChoice`](UIAutomation.md#modechoice)
    - [`ToolMode`](UIAutomation.md#toolmode)
    - [`ModeSetting`](UIAutomation.md#modesetting)
    - [`ModeBar`](UIAutomation.md#modebar)
    - [`ToolControl`](UIAutomation.md#toolcontrol)
    - [`ToolAccess`](UIAutomation.md#toolaccess)
    - [`MenuCommand`](UIAutomation.md#menucommand)
    - [`MenuChunkItem`](UIAutomation.md#menuchunkitem)
    - [`MenuEntry`](UIAutomation.md#menuentry)
    - [`MenuAccess`](UIAutomation.md#menuaccess)
    - [`OIPControl`](UIAutomation.md#oipcontrol)
    - [`OIPSetting`](UIAutomation.md#oipsetting)
    - [`OIPAccess`](UIAutomation.md#oipaccess)
  - Enumerations: [`ToolKind`](UIAutomation.md#toolkind) · [`ToolCreationType`](UIAutomation.md#toolcreationtype) · [`ToolFilter`](UIAutomation.md#toolfilter) · [`ModeType`](UIAutomation.md#modetype) · [`ModeButtonKind`](UIAutomation.md#modebuttonkind) · [`ToolKey`](UIAutomation.md#toolkey) · [`MenuCommandKind`](UIAutomation.md#menucommandkind) · [`MenuChunkKind`](UIAutomation.md#menuchunkkind) · [`MenuFilter`](UIAutomation.md#menufilter) · [`MenuEntryType`](UIAutomation.md#menuentrytype) · [`MenuStatus`](UIAutomation.md#menustatus) · [`OIPPane`](UIAutomation.md#oippane) · [`OIPControlType`](UIAutomation.md#oipcontroltype)
- **[UILayoutCreate](UILayoutCreate.md)** — Alerts and questions, ready-made value dialogs, and modal dialogs built control by control.
  - Classes:
    - [`DialogEvent`](UILayoutCreate.md#dialogevent)
    - [`ListBrowserEvent`](UILayoutCreate.md#listbrowserevent)
    - [`DialogSize`](UILayoutCreate.md#dialogsize)
    - [`Alerts`](UILayoutCreate.md#alerts)
    - [`TextPair`](UILayoutCreate.md#textpair)
    - [`StandardDialogs`](UILayoutCreate.md#standarddialogs)
    - [`LayoutDialog`](UILayoutCreate.md#layoutdialog)
  - Enumerations: [`DialogResult`](UILayoutCreate.md#dialogresult) · [`AlertButton`](UILayoutCreate.md#alertbutton) · [`EditRealType`](UILayoutCreate.md#editrealtype) · [`StaticTextStyle`](UILayoutCreate.md#statictextstyle) · [`CheckState`](UILayoutCreate.md#checkstate) · [`DialogEventType`](UILayoutCreate.md#dialogeventtype) · [`ListBrowserControlType`](UILayoutCreate.md#listbrowsercontroltype) · [`ListBrowserDisplayType`](UILayoutCreate.md#listbrowserdisplaytype) · [`ListBrowserEventType`](UILayoutCreate.md#listbrowsereventtype)

## Index A–Z

[A](#index-a) · [B](#index-b) · [C](#index-c) · [D](#index-d) · [E](#index-e) · [F](#index-f) · [G](#index-g) · [H](#index-h) · [I](#index-i) · [L](#index-l) · [M](#index-m) · [N](#index-n) · [O](#index-o) · [P](#index-p) · [R](#index-r) · [S](#index-s) · [T](#index-t) · [U](#index-u) · [V](#index-v) · [W](#index-w)

### Index A

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`AlertButton`](UILayoutCreate.md#alertbutton) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Default button of a question alert. |
| [`Alerts`](UILayoutCreate.md#alerts) | class | [UILayoutCreate](UILayoutCreate.md) | Standard Vectorworks alerts: information, error and question alerts (static functions only). |
| [`AngularDimensionObject`](ObjectsAnnotation.md#angulardimensionobject) | class | [ObjectsAnnotation](ObjectsAnnotation.md) | Angular dimension: measures the angle between two legs meeting at a vertex. |
| [`AngularUnit`](DocumentAccess.md#angularunit) | IntEnum | [DocumentAccess](DocumentAccess.md) | Unit in which angles are displayed (`UnitSettings.GetAngularUnit`). |
| [`AnnotationObject`](ObjectsAnnotation.md#annotationobject) | class | [ObjectsAnnotation](ObjectsAnnotation.md) | Common base of the annotation plug-in object classes (data tag, title block border). |
| [`Math.Arc2D`](ObjectPrimitives.Math.md#matharc2d) | class | [Math](ObjectPrimitives.Math.md) | Circular arc. |
| [`ArchitectObject`](ObjectsArchitect.md#architectobject) | class | [ObjectsArchitect](ObjectsArchitect.md) | Common base of the Architect object classes (wall, slab, roof, window, door, column, stair). |
| [`ArcLengthDimensionObject`](ObjectsAnnotation.md#arclengthdimensionobject) | class | [ObjectsAnnotation](ObjectsAnnotation.md) | Arc length dimension: measures the length ALONG an arc rather than the straight distance between its... |
| [`ArcObject`](ObjectPrimitives.md#arcobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Circular arc (`ObjectType.Arc`). |
| [`AttributesBase`](Attributes.md#attributesbase) | class | [Attributes](Attributes.md) | Common base of the graphical attribute classes. |

### Index B

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`BuildingMaterial`](Resources.md#buildingmaterial) | class | [Resources](Resources.md) | Material (building material, `ObjectType.BuildingMaterial`): the physical material of a wall, slab or roof... |

### Index C

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`CenterMarkObject`](ObjectsAnnotation.md#centermarkobject) | class | [ObjectsAnnotation](ObjectsAnnotation.md) | Center mark: the cross that marks the centre of a circle or an arc. |
| [`CheckState`](UILayoutCreate.md#checkstate) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | State of a three-state check box, a list browser cell or a tree item check box. |
| [`Math.Circle2D`](ObjectPrimitives.Math.md#mathcircle2d) | class | [Math](ObjectPrimitives.Math.md) | Circle. |
| [`CircleObject`](ObjectPrimitives.md#circleobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Circle. |
| [`ClassAttributes`](Attributes.md#classattributes) | class | [Attributes](Attributes.md) | A class definition (`ObjectType.ClassDefinition`): a named, saved configuration of attributes. |
| [`ClassVisibility`](Attributes.md#classvisibility) | IntEnum | [Attributes](Attributes.md) | Classes |
| [`ColorPair`](Attributes.md#colorpair) | class | [Attributes](Attributes.md) | Foreground and background colors of a pen or a fill, as color indices. |
| [`ColorRGB`](Attributes.md#colorrgb) | class | [Attributes](Attributes.md) | RGB color with 16 bits per channel (0 .. |
| [`ColumnObject`](ObjectsArchitect.md#columnobject) | class | [ObjectsArchitect](ObjectsArchitect.md) | Column plug-in object - the Vectorworks column, universal name "Column2". |
| [`ConeObject`](Objects3D.md#coneobject) | class | [Objects3D](Objects3D.md) | Native cone solid. |
| [`ConeObject.Radii`](Objects3D.md#coneobjectradii) | class (nested) | [Objects3D](Objects3D.md) | Base radii along the local I and J axes. |
| [`ConnectCADDeviceObject`](ObjectsConnectCAD.md#connectcaddeviceobject) | class | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCAD schematic device (universal name "Device"): a named box with socket objects in its profile group. |
| [`ConnectCADDeviceObject.AddSocketResult`](ObjectsConnectCAD.md#connectcaddeviceobjectaddsocketresult) | class (nested) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Outcome of AddSocket: the socket (null when not added) and errors. |
| [`ConnectCADDeviceObject.CreateResult`](ObjectsConnectCAD.md#connectcaddeviceobjectcreateresult) | class (nested) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Outcome of CreateFromJSON: the device (null when not created), errors and warnings. |
| [`ConnectCADDeviceObject.DeviceTypeResult`](ObjectsConnectCAD.md#connectcaddeviceobjectdevicetyperesult) | class (nested) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Outcome of CreateDeviceType: the device-type symbol definition, whether it is new and whether the full... |
| [`ConnectCADLibrary`](ObjectsConnectCAD.md#connectcadlibrary) | class | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCAD data shared by its devices: the signal and connector types, the validation of device descriptions... |
| [`ConnectCADLibrary.Connector`](ObjectsConnectCAD.md#connectcadlibraryconnector) | class (nested) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | A ConnectCAD connector type. |
| [`ConnectCADLibrary.DeviceDefinition`](ObjectsConnectCAD.md#connectcadlibrarydevicedefinition) | class (nested) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Device Definition record of a device-type symbol definition. |
| [`ConnectCADLibrary.Signal`](ObjectsConnectCAD.md#connectcadlibrarysignal) | class (nested) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | A ConnectCAD signal type with its category and preferred connectors. |
| [`ConnectCADLibrary.Validation`](ObjectsConnectCAD.md#connectcadlibraryvalidation) | class (nested) | [ObjectsConnectCAD](ObjectsConnectCAD.md) | Outcome of ValidateDevice: errors (the device would be wrong) and warnings (data kept only in a device type). |
| [`ConnectCADSocketObject`](ObjectsConnectCAD.md#connectcadsocketobject) | class | [ObjectsConnectCAD](ObjectsConnectCAD.md) | ConnectCAD socket (universal name "Socket"): a connection point of a schematic device, inside the device's... |
| [`ContentFolder`](Resources.md#contentfolder) | IntEnum | [Resources](Resources.md) | Standard Vectorworks content folder holding external (library / default) resources. |
| [`CornerDiameters`](ObjectPrimitives.md#cornerdiameters) | class | [ObjectPrimitives](ObjectPrimitives.md) | Corner rounding of a rounded rectangle: the diameters of the corner ellipse along the width side (alongWidth)... |

### Index D

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`DataTagObject`](ObjectsAnnotation.md#datatagobject) | class | [ObjectsAnnotation](ObjectsAnnotation.md) | Data tag plug-in object (universal name "Data Tag"). |
| [`DataTagObject.HorizontalPosition`](ObjectsAnnotation.md#datatagobjecthorizontalposition) | IntEnum (nested) | [ObjectsAnnotation](ObjectsAnnotation.md) | Which side of the leader the tag text sits on ("Horizontal Position"). |
| [`DataTagObject.LeaderType`](ObjectsAnnotation.md#datatagobjectleadertype) | IntEnum (nested) | [ObjectsAnnotation](ObjectsAnnotation.md) | Shape of the leader of a data tag ("Leader Type"). |
| [`DataTagObject.MoveBehaviour`](ObjectsAnnotation.md#datatagobjectmovebehaviour) | IntEnum (nested) | [ObjectsAnnotation](ObjectsAnnotation.md) | What dragging the tag in the drawing moves: the whole tag, or only the tip of its leader. |
| [`DataVisualization`](Resources.md#datavisualization) | class | [Resources](Resources.md) | Data visualization (`ObjectType.DataVisualization`): a rule that overrides the graphic attributes of the... |
| [`DefaultAttributes`](DocumentAccess.md#defaultattributes) | class | [DocumentAccess](DocumentAccess.md) | Default attributes for new objects (the Attributes palette with nothing selected). |
| [`Descend`](DocumentAccess.md#descend) | IntFlag | [DocumentAccess](DocumentAccess.md) | How deep a traversal descends into container objects (groups, symbols, viewports, ...). |
| [`DialogEvent`](UILayoutCreate.md#dialogevent) | class | [UILayoutCreate](UILayoutCreate.md) | One event delivered to a layout dialog handler. |
| [`DialogEventType`](UILayoutCreate.md#dialogeventtype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Kind of a dialog event (see DialogEvent). |
| [`DialogResult`](UILayoutCreate.md#dialogresult) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | How a dialog or an alert was closed. |
| [`DialogSize`](UILayoutCreate.md#dialogsize) | class | [UILayoutCreate](UILayoutCreate.md) | Size of a dialog, in pixels. |
| [`DimensionKind`](ObjectsAnnotation.md#dimensionkind) | IntEnum | [ObjectsAnnotation](ObjectsAnnotation.md) | Kind of dimension an object is. |
| [`DimensionObject`](ObjectsAnnotation.md#dimensionobject) | class | [ObjectsAnnotation](ObjectsAnnotation.md) | Base class of every dimension object (`ObjectType.Dimension`). |
| [`DimensionTolerance`](ObjectsAnnotation.md#dimensiontolerance) | IntEnum | [ObjectsAnnotation](ObjectsAnnotation.md) | How much a dimension deviates from its nominal value, printed next to the measurement. |
| [`DisplaySettings`](DocumentAccess.md#displaysettings) | class | [DocumentAccess](DocumentAccess.md) | Display preferences. |
| [`Document`](DocumentAccess.md#document) | class | [DocumentAccess](DocumentAccess.md) | Stateless facade over the active Vectorworks document. |
| [`DoorObject`](ObjectsArchitect.md#doorobject) | class | [ObjectsArchitect](ObjectsArchitect.md) | Door plug-in object (universal name "Door") from the Architectural Objects plug-in. |
| [`DropShadow`](Attributes.md#dropshadow) | class | [Attributes](Attributes.md) | Drop shadow settings of an object, a class or the document: on/off, units, offset, blur radius, angle, color... |
| [`DropShadowAttributes`](Attributes.md#dropshadowattributes) | class | [Attributes](Attributes.md) | Drop shadow of an object. |
| [`DropShadowUnits`](Attributes.md#dropshadowunits) | IntEnum | [Attributes](Attributes.md) | Drop shadow |

### Index E

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`EditingSettings`](DocumentAccess.md#editingsettings) | class | [DocumentAccess](DocumentAccess.md) | Editing and session preferences. |
| [`EditRealType`](UILayoutCreate.md#editrealtype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Kind of value shown by a real number edit field. |
| [`ExistingTreeObject`](ObjectsLandmark.md#existingtreeobject) | class | [ObjectsLandmark](ObjectsLandmark.md) | Existing tree plug-in object (universal name "Existing Tree") from the Landmark plug-in. |
| [`ExistingTreeObject.Action`](ObjectsLandmark.md#existingtreeobjectaction) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Proposed action for an existing tree. |
| [`ExistingTreeObject.Condition`](ObjectsLandmark.md#existingtreeobjectcondition) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Arborist assessment |
| [`ExistingTreeObject.Origin`](ObjectsLandmark.md#existingtreeobjectorigin) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Origin of an existing tree species. |
| [`ExistingTreeObject.Significance`](ObjectsLandmark.md#existingtreeobjectsignificance) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Significance rating of an existing tree. |
| [`ExistingTreeObject.SULE`](ObjectsLandmark.md#existingtreeobjectsule) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Safe Useful Life Expectancy |
| [`ExistingTreeObject.TreeProtection`](ObjectsLandmark.md#existingtreeobjecttreeprotection) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Tree Protection Zone display |
| [`ExtrudeObject`](Objects3D.md#extrudeobject) | class | [Objects3D](Objects3D.md) | Native extrude (not a plug-in object). |
| [`ExtrudeObject.Transform`](Objects3D.md#extrudeobjecttransform) | class (nested) | [Objects3D](Objects3D.md) | Orthonormal local axes and origin in the parent coordinate system (identity by default). |
| [`ExtrudeObject.Values`](Objects3D.md#extrudeobjectvalues) | class (nested) | [Objects3D](Objects3D.md) | Local base elevation and signed thickness, in world units. |

### Index F

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`FillAttributes`](Attributes.md#fillattributes) | class | [Attributes](Attributes.md) | Fill attributes of an object: colors, style (pattern / hatch / tile / gradient / image), opacity and by-class... |
| [`FillMappingAttributes`](Attributes.md#fillmappingattributes) | class | [Attributes](Attributes.md) | Mapping of hatch, tile, gradient and image fills (fill space): origin, axes, offsets, rotation, repeat,... |
| [`FillMappingAttributes.Frame`](Attributes.md#fillmappingattributesframe) | class (nested) | [Attributes](Attributes.md) | Mapping frame of a hatch, tile, gradient or image fill: the origin and the end points of the I and J axes. |
| [`FillType`](Attributes.md#filltype) | IntEnum | [Attributes](Attributes.md) | Kind of the fill of an object. |

### Index G

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`GDTFLibrary`](ObjectsSpotlight.md#gdtflibrary) | class | [ObjectsSpotlight](ObjectsSpotlight.md) | GDTF fixture types (General Device Type Format, DIN SPEC 15800) known to Spotlight. |
| [`GDTFLibrary.Entry`](ObjectsSpotlight.md#gdtflibraryentry) | class (nested) | [ObjectsSpotlight](ObjectsSpotlight.md) | One DMX mode of an available fixture type. |
| [`GDTFLibrary.ImportResult`](ObjectsSpotlight.md#gdtflibraryimportresult) | class (nested) | [ObjectsSpotlight](ObjectsSpotlight.md) | Outcome of Import: the GDTF symbol definition, its GDTF name, whether this call imported it and whether the... |
| [`GenericSolidObject`](Objects3D.md#genericsolidobject) | class | [Objects3D](Objects3D.md) | Covers native solid objects, including solid additions, subtractions and intersections and history-free... |
| [`GenericSolidObject.HistoryStep`](Objects3D.md#genericsolidobjecthistorystep) | class (nested) | [Objects3D](Objects3D.md) | One node in the native construction tree, in preorder. |
| [`GenericSolidObject.Operation`](Objects3D.md#genericsolidobjectoperation) | IntEnum (nested) | [Objects3D](Objects3D.md) | Solid Boolean operation. |
| [`Gradient`](Resources.md#gradient) | class | [Resources](Resources.md) | Gradient fill (`ObjectType.GradientDefinition`): a blend between two or more color stops. |
| [`GradientSegment`](Resources.md#gradientsegment) | class | [Resources](Resources.md) | One color stop of a gradient. |
| [`GridSettings`](DocumentAccess.md#gridsettings) | class | [DocumentAccess](DocumentAccess.md) | Grid preferences. |
| [`GroupObject`](ObjectPrimitives.md#groupobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Group (`ObjectType.Group`): a container of other objects. |

### Index H

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`HardscapeObject`](ObjectsLandmark.md#hardscapeobject) | class | [ObjectsLandmark](ObjectsLandmark.md) | Hardscape plug-in object (universal name "Hardscape") from the Landmark plug-in. |
| [`HardscapeObject.Mode3D`](ObjectsLandmark.md#hardscapeobjectmode3d) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | 3D mode of the hardscape. |
| [`Hatch`](Resources.md#hatch) | class | [Resources](Resources.md) | Vector hatch fill (`ObjectType.HatchDefinition`): a set of line families repeated over the filled area. |
| [`HatchLevel`](Resources.md#hatchlevel) | class | [Resources](Resources.md) | One line family of a hatch. |
| [`HemisphereObject`](Objects3D.md#hemisphereobject) | class | [Objects3D](Objects3D.md) | Native hemisphere solid: center, radii and a dome pointing along the local K axis; lightweight view of the... |

### Index I

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`ImageFill`](Resources.md#imagefill) | class | [Resources](Resources.md) | Image resource (`ObjectType.ImageDefinition`): a bitmap used as an image fill, as an image prop or as a... |
| [`ImageFill.Compression`](Resources.md#imagefillcompression) | IntEnum (nested) | [Resources](Resources.md) | Compression the image is stored with. |
| [`ImportConflict`](Resources.md#importconflict) | IntEnum | [Resources](Resources.md) | How a name conflict is resolved when a resource is imported into the current drawing and a resource of the... |

### Index L

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`LandmarkObject`](ObjectsLandmark.md#landmarkobject) | class | [ObjectsLandmark](ObjectsLandmark.md) | Common base of the Landmark plug-in object classes (plant, landscape area, site model, site modifier, stake,... |
| [`LandscapeAreaObject`](ObjectsLandmark.md#landscapeareaobject) | class | [ObjectsLandmark](ObjectsLandmark.md) | Landscape area plug-in object (universal name "Landscape Area") from the Landmark plug-in. |
| [`LandscapeAreaObject.AreaUnits`](ObjectsLandmark.md#landscapeareaobjectareaunits) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Units in which the area of a landscape area is displayed. |
| [`LandscapeAreaObject.DrawingMode`](ObjectsLandmark.md#landscapeareaobjectdrawingmode) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Whether the object is drawn as a landscape area or as a hedgerow. |
| [`LandscapeAreaObject.PlantDisplay2D`](ObjectsLandmark.md#landscapeareaobjectplantdisplay2d) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | How the plants of a landscape area are shown in 2D. |
| [`Layer`](DocumentAccess.md#layer) | class | [DocumentAccess](DocumentAccess.md) | A layer (design or sheet layer). |
| [`LayerContents`](DocumentAccess.md#layercontents) | class | [DocumentAccess](DocumentAccess.md) | Object count and bounds of the top level objects of a layer. |
| [`LayerType`](DocumentAccess.md#layertype) | IntEnum | [DocumentAccess](DocumentAccess.md) | Kind of a layer. |
| [`LayerVisibility`](DocumentAccess.md#layervisibility) | IntEnum | [DocumentAccess](DocumentAccess.md) | Visibility of a layer (as shown in the Navigation palette). |
| [`LayoutDialog`](UILayoutCreate.md#layoutdialog) | class | [UILayoutCreate](UILayoutCreate.md) | Modal layout manager dialog, built control by control in code. |
| [`LightingDeviceObject`](ObjectsSpotlight.md#lightingdeviceobject) | class | [ObjectsSpotlight](ObjectsSpotlight.md) | Lighting device plug-in object (universal name "Lighting Device") from the Spotlight plug-in. |
| [`Math.Line2D`](ObjectPrimitives.Math.md#mathline2d) | class | [Math](ObjectPrimitives.Math.md) | Line segment from `start` to `end`. |
| [`Math.Line2D.Intersection`](ObjectPrimitives.Math.md#mathline2dintersection) | class (nested) | [Math](ObjectPrimitives.Math.md) | Intersection of the infinite lines. |
| [`Line2DObject`](ObjectPrimitives.md#line2dobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | 2D line (`ObjectType.Line`): a straight segment between two points. |
| [`Math.Line3D`](ObjectPrimitives.Math.md#mathline3d) | class | [Math](ObjectPrimitives.Math.md) | Python-owned 3D segment from start to end in world millimetres. |
| [`LinearDimensionObject`](ObjectsAnnotation.md#lineardimensionobject) | class | [ObjectsAnnotation](ObjectsAnnotation.md) | Linear dimension: measures the distance between two points. |
| [`LineType`](Resources.md#linetype) | class | [Resources](Resources.md) | Line type resource. |
| [`ListBrowserControlType`](UILayoutCreate.md#listbrowsercontroltype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Behavior of a list browser column. |
| [`ListBrowserDisplayType`](UILayoutCreate.md#listbrowserdisplaytype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | What a list browser column shows. |
| [`ListBrowserEvent`](UILayoutCreate.md#listbrowserevent) | class | [UILayoutCreate](UILayoutCreate.md) | Detail of the last list browser event. |
| [`ListBrowserEventType`](UILayoutCreate.md#listbrowsereventtype) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | What happened in a list browser (see `LayoutDialog.GetListBrowserEvent`). |
| [`Locus2DObject`](ObjectPrimitives.md#locus2dobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | 2D locus (`ObjectType.Locus`): a reference point. |

### Index M

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`Marker`](Attributes.md#marker) | class | [Attributes](Attributes.md) | Marker (arrow head) at the beginning or end of a line: shape, fill, base, half tick, tail, angle (degrees),... |
| [`MarkerAttributes`](Attributes.md#markerattributes) | class | [Attributes](Attributes.md) | Beginning and end markers (arrow heads) of an object. |
| [`MarkerBase`](Attributes.md#markerbase) | IntEnum | [Attributes](Attributes.md) | Shape of the base of a marker (pre-shifted bit values, see `Marker.GetStyleValue`). |
| [`MarkerFill`](Attributes.md#markerfill) | IntEnum | [Attributes](Attributes.md) | The marker style enumerations below (MarkerFill, MarkerBase, MarkerHalfTick) use pre-shifted values so they... |
| [`MarkerHalfTick`](Attributes.md#markerhalftick) | IntEnum | [Attributes](Attributes.md) | Whole marker, or only its left or right half (pre-shifted bit values, see `Marker.GetStyleValue`). |
| [`MarkerShape`](Attributes.md#markershape) | IntEnum | [Attributes](Attributes.md) | Markers (arrow heads) |
| [`MarkerThicknessBasis`](Attributes.md#markerthicknessbasis) | IntEnum | [Attributes](Attributes.md) | What the line thickness of a marker follows. |
| [`MarkerThicknessUnits`](Attributes.md#markerthicknessunits) | IntEnum | [Attributes](Attributes.md) | Units of a custom marker line thickness. |
| [`MenuAccess`](UIAutomation.md#menuaccess) | class | [UIAutomation](UIAutomation.md) | Stateless facade over the Vectorworks menu system. |
| [`MenuChunkItem`](UIAutomation.md#menuchunkitem) | class | [UIAutomation](UIAutomation.md) | One current item of a chunk. |
| [`MenuChunkKind`](UIAutomation.md#menuchunkkind) | IntEnum | [UIAutomation](UIAutomation.md) | Kind of a chunk (see "Chunk" above). |
| [`MenuCommand`](UIAutomation.md#menucommand) | class | [UIAutomation](UIAutomation.md) | Description of one installed menu command. |
| [`MenuCommandKind`](UIAutomation.md#menucommandkind) | IntEnum | [UIAutomation](UIAutomation.md) | How a menu command is provided. |
| [`MenuEntry`](UIAutomation.md#menuentry) | class | [UIAutomation](UIAutomation.md) | One entry of a menu of the menu bar, as the current workspace defines it. |
| [`MenuEntryType`](UIAutomation.md#menuentrytype) | IntEnum | [UIAutomation](UIAutomation.md) | Kind of an entry of a menu of the menu bar. |
| [`MenuFilter`](UIAutomation.md#menufilter) | IntEnum | [UIAutomation](UIAutomation.md) | Which menu commands `MenuAccess.GetMenuCommands` returns. |
| [`MenuStatus`](UIAutomation.md#menustatus) | IntEnum | [UIAutomation](UIAutomation.md) | Whether a menu command (or chunk item) can be executed now, and why not (see `MenuAccess.GetMenuStatus`). |
| [`MeshObject`](Objects3D.md#meshobject) | class | [Objects3D](Objects3D.md) | Native mesh (`ObjectType.Mesh`): a shared vertex list plus polygonal faces that index into it. |
| [`MeshObject.Face`](Objects3D.md#meshobjectface) | class (nested) | [Objects3D](Objects3D.md) | part 0 means the overall (untextured) part, see `GetOverallPart()`. |
| [`MeshObject.Part`](Objects3D.md#meshobjectpart) | class (nested) | [Objects3D](Objects3D.md) | Texture part: id, texture reference (0 = untextured) and number of faces using it. |
| [`MeshObject.Smoothing`](Objects3D.md#meshobjectsmoothing) | IntEnum (nested) | [Objects3D](Objects3D.md) | How the mesh is smoothed when it is rendered. |
| [`ModeBar`](UIAutomation.md#modebar) | class | [UIAutomation](UIAutomation.md) | Stateless view over the Tool bar (mode bar) of the active tool. |
| [`ModeButtonDefinition`](UIAutomation.md#modebuttondefinition) | class | [UIAutomation](UIAutomation.md) | A mode button as declared by a tool (static information, available without activating the tool). |
| [`ModeButtonKind`](UIAutomation.md#modebuttonkind) | IntEnum | [UIAutomation](UIAutomation.md) | Kind of a mode button as declared by a tool when it is registered (may differ from the live ModeType). |
| [`ModeChoice`](UIAutomation.md#modechoice) | class | [UIAutomation](UIAutomation.md) | One choice of a mode group: a radio button, the single button of a Button/Toggle group, or an item of a... |
| [`ModeSetting`](UIAutomation.md#modesetting) | class | [UIAutomation](UIAutomation.md) | A mode change request used by the generic, text based mode API (see `ModeBar.SetMode`). |
| [`ModeType`](UIAutomation.md#modetype) | IntEnum | [UIAutomation](UIAutomation.md) | Kind of a mode group on the Tool bar of the active tool. |
| [`MultiExtrudeObject`](Objects3D.md#multiextrudeobject) | class | [Objects3D](Objects3D.md) | Native multiple extrude. |

### Index N

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`NurbsCurveObject`](Objects3D.md#nurbscurveobject) | class | [Objects3D](Objects3D.md) | Native piecewise NURBS curve. |
| [`NurbsCurveObject.Location`](Objects3D.md#nurbscurveobjectlocation) | class (nested) | [Objects3D](Objects3D.md) | Curve point and native parameter on a zero-based piece; parameters are not arc lengths. |
| [`NurbsSurfaceObject`](Objects3D.md#nurbssurfaceobject) | class | [Objects3D](Objects3D.md) | Native NURBS surface. |

### Index O

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`ObjectAttributes`](Attributes.md#objectattributes) | class | [Attributes](Attributes.md) | All graphical attributes of an object. |
| [`ObjectColors`](Attributes.md#objectcolors) | class | [Attributes](Attributes.md) | All four object colors (pen fore/back, fill fore/back), as color indices. |
| [`ObjectType`](Attributes.md#objecttype) | IntEnum | [Attributes](Attributes.md) | Type of an object. |
| [`Math.OffsetJoin`](ObjectPrimitives.Math.md#mathoffsetjoin) | IntEnum | [Math](ObjectPrimitives.Math.md) | Corner style of polygon offsets (`Polygon2D.Offset`). |
| [`OIPAccess`](UIAutomation.md#oipaccess) | class | [UIAutomation](UIAutomation.md) | Stateless facade over the Object Info palette. |
| [`OIPControl`](UIAutomation.md#oipcontrol) | class | [UIAutomation](UIAutomation.md) | Description and live state of one OIP control. |
| [`OIPControlType`](UIAutomation.md#oipcontroltype) | IntEnum | [UIAutomation](UIAutomation.md) | Kind of an OIP control. |
| [`OIPPane`](UIAutomation.md#oippane) | IntEnum | [UIAutomation](UIAutomation.md) | Pane (tab) of the Object Info palette. |
| [`OIPSetting`](UIAutomation.md#oipsetting) | class | [UIAutomation](UIAutomation.md) | A control change request used by the generic, text based API (see `OIPAccess.SetValue`). |

### Index P

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`ParametricObject`](ObjectPrimitives.md#parametricobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Generic plug-in (parametric) object (`ObjectType.Parametric`) of any kind, defined by a script or by a... |
| [`ParametricObject.PluginKind`](ObjectPrimitives.md#parametricobjectpluginkind) | IntEnum (nested) | [ObjectPrimitives](ObjectPrimitives.md) | How the objects of a plug-in are placed: the object subtype that the plug-in declares. |
| [`PenAttributes`](Attributes.md#penattributes) | class | [Attributes](Attributes.md) | Pen (stroke) attributes of an object: colors, style (pattern / line type), line weight, opacity, by-class... |
| [`PenStyleKind`](Attributes.md#penstylekind) | IntEnum | [Attributes](Attributes.md) | Classification of a raw pen style value. |
| [`Math.Plane3D`](ObjectPrimitives.Math.md#mathplane3d) | class | [Math](ObjectPrimitives.Math.md) | Python-owned oriented infinite plane with a unit normal. |
| [`PlantObject`](ObjectsLandmark.md#plantobject) | class | [ObjectsLandmark](ObjectsLandmark.md) | Plant plug-in object (universal name "Plant") from the Landmark plug-in. |
| [`PlantObject.Config`](ObjectsLandmark.md#plantobjectconfig) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Configuration and display |
| [`PlantObject.TagDisplay`](ObjectsLandmark.md#plantobjecttagdisplay) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Where the plant tag is shown. |
| [`Math.Point2D`](ObjectPrimitives.Math.md#mathpoint2d) | class | [Math](ObjectPrimitives.Math.md) | 2D point / vector. |
| [`Point2D`](Attributes.md#point2d) | class | [Attributes](Attributes.md) | Plain 2D point record (`x`, `y` in world units) used by the dialog and attribute APIs. |
| [`Math.Point3D`](ObjectPrimitives.Math.md#mathpoint3d) | class | [Math](ObjectPrimitives.Math.md) | Python-owned 3D point / vector in world millimetres. |
| [`Point3D`](UIAutomation.md#point3d) | class | [UIAutomation](UIAutomation.md) | 3D point in world coordinates. |
| [`Math.Polygon2D`](ObjectPrimitives.Math.md#mathpolygon2d) | class | [Math](ObjectPrimitives.Math.md) | Polygon or polyline vertex list. |
| [`Math.Polygon2D.CurveLocation`](ObjectPrimitives.Math.md#mathpolygon2dcurvelocation) | class (nested) | [Math](ObjectPrimitives.Math.md) | Point and native piece parameter on the temporary NURBS representation of the polygon's curved outer path. |
| [`Polygon3DObject`](Objects3D.md#polygon3dobject) | class | [Objects3D](Objects3D.md) | Native 3D polygon (`ObjectType.Polygon3D`). |
| [`Polygon3DObject.ClosestPoint`](Objects3D.md#polygon3dobjectclosestpoint) | class (nested) | [Objects3D](Objects3D.md) | Closest point on the polygon path, its distance, edge index and path distance from the first vertex. |
| [`Polygon3DObject.Plane`](Objects3D.md#polygon3dobjectplane) | class (nested) | [Objects3D](Objects3D.md) | Plane through the vertex centroid; normal is a unit vector following the vertex order (right-hand rule) and d... |
| [`PolygonObject`](ObjectPrimitives.md#polygonobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Polygon (`ObjectType.Polygon`, and freehand polygons `ObjectType.FreehandPolygon`): corner vertices only. |
| [`PolylineObject`](ObjectPrimitives.md#polylineobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Polyline (`ObjectType.Polyline`): a poly shape whose vertices can be corner, bezier, cubic, arc or radius... |
| [`PolyObject`](ObjectPrimitives.md#polyobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Common base of the polygon and polyline classes. |
| [`PolyObject.BooleanOperation`](ObjectPrimitives.md#polyobjectbooleanoperation) | IntEnum (nested) | [ObjectPrimitives](ObjectPrimitives.md) | Operation of the 2D Boolean functions |
| [`Math.PolyVertex`](ObjectPrimitives.Math.md#mathpolyvertex) | class | [Math](ObjectPrimitives.Math.md) | One vertex of a `Polygon2D`: its point, vertex type, arc radius (radius vertices) and the visibility of the... |
| [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Common base of every object class of the API (2D primitives and, through their subclasses, 3D, annotation,... |
| [`PrimitiveObject.Bounds3D`](ObjectPrimitives.md#primitiveobjectbounds3d) | class (nested) | [ObjectPrimitives](ObjectPrimitives.md) | Axis-aligned 3D bounding box, in world units |
| [`ProgramVariables`](DocumentAccess.md#programvariables) | class | [DocumentAccess](DocumentAccess.md) | Low-level, typed access to any Vectorworks program variable (application-wide or per-document preference) by... |
| [`PropertyLineObject`](ObjectsLandmark.md#propertylineobject) | class | [ObjectsLandmark](ObjectsLandmark.md) | Property line plug-in object (universal name "Property Line") from the Landmark plug-in. |
| [`PropertyLineObject.AreaUnits`](ObjectsLandmark.md#propertylineobjectareaunits) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Area unit choices supported by both "Area Units Imperial" and "Area Units Metric" parameters. |

### Index R

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`RadialDimensionObject`](ObjectsAnnotation.md#radialdimensionobject) | class | [ObjectsAnnotation](ObjectsAnnotation.md) | Radial and diametrical dimension: measures the radius or the diameter of a circle or arc. |
| [`RecordField`](Resources.md#recordfield) | class | [Resources](Resources.md) | One field of a record format. |
| [`RecordFieldType`](Resources.md#recordfieldtype) | IntEnum | [Resources](Resources.md) | Data type of a record field. |
| [`RecordFormat`](Resources.md#recordformat) | class | [Resources](Resources.md) | Record format. |
| [`Math.Rect2D`](ObjectPrimitives.Math.md#mathrect2d) | class | [Math](ObjectPrimitives.Math.md) | Axis aligned rectangle. |
| [`RectangleObject`](ObjectPrimitives.md#rectangleobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Rectangle (`ObjectType.Box`), possibly rotated. |
| [`RectangularObject`](ObjectPrimitives.md#rectangularobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Common base of the rectangle and the rounded rectangle classes. |
| [`RenderBackground`](Resources.md#renderbackground) | class | [Resources](Resources.md) | Renderworks background (`ObjectType.RenderBackground`): what a rendering shows behind the model. |
| [`RenderBackground.Kind`](Resources.md#renderbackgroundkind) | IntEnum (nested) | [Resources](Resources.md) | Kind of background a new resource is created with. |
| [`RenderStyle`](Resources.md#renderstyle) | class | [Resources](Resources.md) | Render style (`ObjectType.RenderStyle`): a saved configuration of the rendering settings, applied to a... |
| [`Resource`](Resources.md#resource) | class | [Resources](Resources.md) | One resource, identified by its handle. |
| [`ResourceFolder`](Resources.md#resourcefolder) | class | [Resources](Resources.md) | Resource folder (`ObjectType.Folder`): groups resources of one kind in the Resource Manager. |
| [`ResourceFolderPath`](Resources.md#resourcefolderpath) | class | [Resources](Resources.md) | Folders of a path made by `ResourceFolder.CreatePathFolders`: every folder of the path and the ones the call... |
| [`ResourceList`](Resources.md#resourcelist) | class | [Resources](Resources.md) | A list of resources of one kind, coming from the current drawing or from external content. |
| [`ResourceList.Entry`](Resources.md#resourcelistentry) | class (nested) | [Resources](Resources.md) | One entry of the list. |
| [`ResourceList.ImportResult`](Resources.md#resourcelistimportresult) | class (nested) | [Resources](Resources.md) | Outcome of ImportWithResult: the resource in the drawing and whether this call copied it in (`False` when the... |
| [`ResourceType`](Resources.md#resourcetype) | IntEnum | [Resources](Resources.md) | Kind of a resource. |
| [`RoofObject`](ObjectsArchitect.md#roofobject) | class | [ObjectsArchitect](ObjectsArchitect.md) | Roof (`ObjectType.RoofContainer`) - a polygonal roof defined by a list of edges. |
| [`RoofObject.Accessories`](ObjectsArchitect.md#roofobjectaccessories) | class (nested) | [ObjectsArchitect](ObjectsArchitect.md) | Roof accessories along the perimeter. |
| [`RoofObject.Attributes`](ObjectsArchitect.md#roofobjectattributes) | class (nested) | [ObjectsArchitect](ObjectsArchitect.md) | Roof-wide attributes. |
| [`RoofObject.Edge`](ObjectsArchitect.md#roofobjectedge) | class (nested) | [ObjectsArchitect](ObjectsArchitect.md) | Roof edges (polygon vertex + per-edge slope and overhang), in the order of the roof outline. |
| [`RoofObject.MiterType`](ObjectsArchitect.md#roofobjectmitertype) | IntEnum (nested) | [ObjectsArchitect](ObjectsArchitect.md) | Miter types for the roof edges (how two adjacent slope faces are joined). |
| [`RoofStyle`](Resources.md#roofstyle) | class | [Resources](Resources.md) | Roof style (`ObjectType.RoofStyle`): the components and attributes of a roof. |
| [`RoofTextures`](Attributes.md#rooftextures) | class | [Attributes](Attributes.md) | Roof textures of a class (internal indices of texture resources, 0 = none). |
| [`Math.RotatedRect2D`](ObjectPrimitives.Math.md#mathrotatedrect2d) | class | [Math](ObjectPrimitives.Math.md) | Rectangle that may be rotated: a corner, the direction of the width side and the two side lengths. |
| [`RoundRectObject`](ObjectPrimitives.md#roundrectobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Rounded rectangle (`ObjectType.RoundedRectangle`), possibly rotated. |

### Index S

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`ScriptLanguage`](Scripting.md#scriptlanguage) | IntEnum | [Scripting](Scripting.md) | Language of a script. |
| [`ScriptPalette`](Scripting.md#scriptpalette) | class | [Scripting](Scripting.md) | One script palette, identified by its handle. |
| [`ScriptResource`](Scripting.md#scriptresource) | class | [Scripting](Scripting.md) | One script resource, identified by its handle. |
| [`ShellObject`](Objects3D.md#shellobject) | class | [Objects3D](Objects3D.md) | Shell solid: a CSG offset node (Shell Solid tool, VectorScript CreateShell). |
| [`SiteModelObject`](ObjectsLandmark.md#sitemodelobject) | class | [ObjectsLandmark](ObjectsLandmark.md) | Site model plug-in object (universal name "DTM6") from the Landmark plug-in. |
| [`SiteModelObject.Display2D`](ObjectsLandmark.md#sitemodelobjectdisplay2d) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | 2D / 3D display selection |
| [`SiteModelObject.Display3D`](ObjectsLandmark.md#sitemodelobjectdisplay3d) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | What the 3D display of a site model shows. |
| [`SiteModifierObject`](ObjectsLandmark.md#sitemodifierobject) | class | [ObjectsLandmark](ObjectsLandmark.md) | Site modifier plug-in object (universal name "Site Modifiers") of the Landmark plug-in. |
| [`SiteModifierObject.ApplyTo`](ObjectsLandmark.md#sitemodifierobjectapplyto) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Which site model surface a site modifier applies to. |
| [`SiteModifierObject.Config`](ObjectsLandmark.md#sitemodifierobjectconfig) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Reshaping strategy of a site modifier ("Config"). |
| [`SlabObject`](ObjectsArchitect.md#slabobject) | class | [ObjectsArchitect](ObjectsArchitect.md) | Slab - a horizontal element (floor, roof deck, ceiling deck, ...) defined by a 2D boundary profile and... |
| [`SlabStyle`](Resources.md#slabstyle) | class | [Resources](Resources.md) | Slab style (`ObjectType.SlabStyle`): the components and attributes of a slab. |
| [`SnapSettings`](DocumentAccess.md#snapsettings) | class | [DocumentAccess](DocumentAccess.md) | Snapping (SmartCursor) preferences. |
| [`SolidPrimitiveObject`](Objects3D.md#solidprimitiveobject) | class | [Objects3D](Objects3D.md) | Common base of the native parametric solid primitives (`ObjectType.Solid`): spheres, hemispheres and cones. |
| [`SolidPrimitiveObject.Kind`](Objects3D.md#solidprimitiveobjectkind) | IntEnum (nested) | [Objects3D](Objects3D.md) | Kind of a solid primitive. |
| [`SphereObject`](Objects3D.md#sphereobject) | class | [Objects3D](Objects3D.md) | Native sphere solid: center and I/J/K radii (unequal radii give an ellipsoid); lightweight view of the... |
| [`StackLayersSettings`](DocumentAccess.md#stacklayerssettings) | class | [DocumentAccess](DocumentAccess.md) | Unified view (stack layers) preferences. |
| [`StairObject`](ObjectsArchitect.md#stairobject) | class | [ObjectsArchitect](ObjectsArchitect.md) | Stair plug-in object - the Vectorworks stair, universal name "Stairs CW". |
| [`StakeObject`](ObjectsLandmark.md#stakeobject) | class | [ObjectsLandmark](ObjectsLandmark.md) | Stake plug-in object (universal name "Stake Object") from the Landmark plug-in. |
| [`StakeObject.Mode`](ObjectsLandmark.md#stakeobjectmode) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Role of the stake with respect to the site model. |
| [`StakeObject.SiteModel`](ObjectsLandmark.md#stakeobjectsitemodel) | IntEnum (nested) | [ObjectsLandmark](ObjectsLandmark.md) | Which site model surface a stake refers to. |
| [`StandardDialogs`](UILayoutCreate.md#standarddialogs) | class | [UILayoutCreate](UILayoutCreate.md) | Ready-made dialogs that edit one or two values or choose from a list (static functions only). |
| [`StaticTextStyle`](UILayoutCreate.md#statictextstyle) | IntEnum | [UILayoutCreate](UILayoutCreate.md) | Font style of a static text. |
| [`Story`](DocumentAccess.md#story) | class | [DocumentAccess](DocumentAccess.md) | A story: a floor of the building at an elevation. |
| [`StoryElevationChangeMode`](DocumentAccess.md#storyelevationchangemode) | IntEnum | [DocumentAccess](DocumentAccess.md) | Which stories `Story.SetElevation` moves (the choices of the Change Story Elevation dialog box). |
| [`StoryLevel`](DocumentAccess.md#storylevel) | class | [DocumentAccess](DocumentAccess.md) | One level of a story: a named height (its level type) relative to the story elevation, optionally with the... |
| [`StoryLevelTemplate`](DocumentAccess.md#storyleveltemplate) | class | [DocumentAccess](DocumentAccess.md) | A default story level (Organization dialog box > Stories tab > Default Story Levels): a template for story... |
| [`SurfaceModelObject`](Objects3D.md#surfacemodelobject) | class | [Objects3D](Objects3D.md) | A modeling result is a NURBS surface, a CSG solid, or a group of modeling results. |
| [`SurfaceModelObject.PathOptions`](Objects3D.md#surfacemodelobjectpathoptions) | class (nested) | [Objects3D](Objects3D.md) | Extrude-along-path scale and profile-placement options. |
| [`SweepObject`](Objects3D.md#sweepobject) | class | [Objects3D](Objects3D.md) | Native sweep. |
| [`SweepObject.Values`](Objects3D.md#sweepobjectvalues) | class (nested) | [Objects3D](Objects3D.md) | Sweep angles in radians and pitch in world units per full turn. |
| [`SymbolDefinition`](Resources.md#symboldefinition) | class | [Resources](Resources.md) | Symbol definition. |
| [`SymbolDefinition.BreakMode`](Resources.md#symboldefinitionbreakmode) | IntEnum (nested) | [Resources](Resources.md) | How the wall is cut where the symbol is inserted. |
| [`SymbolDefinition.GeometryType`](Resources.md#symboldefinitiongeometrytype) | IntEnum (nested) | [Resources](Resources.md) | What the symbol can draw: 2D only, 3D only, or both (a hybrid symbol shows its 2D part in top/plan). |
| [`SymbolDefinition.InsertMode`](Resources.md#symboldefinitioninsertmode) | IntEnum (nested) | [Resources](Resources.md) | Where the symbol sits relative to the wall it is inserted into. |

### Index T

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`TextDefaults`](DocumentAccess.md#textdefaults) | class | [DocumentAccess](DocumentAccess.md) | Default text settings for new text objects. |
| [`TextJustification`](DocumentAccess.md#textjustification) | IntEnum | [DocumentAccess](DocumentAccess.md) | Horizontal justification of new text (`TextDefaults`). |
| [`TextLineSpacing`](DocumentAccess.md#textlinespacing) | IntEnum | [DocumentAccess](DocumentAccess.md) | Line spacing of new text (`TextDefaults`); `Custom` uses the leading of `TextDefaults.GetLeading`. |
| [`TextObject`](ObjectPrimitives.md#textobject) | class | [ObjectPrimitives](ObjectPrimitives.md) | Text block (`ObjectType.Text`): formatted text placed at an origin point. |
| [`TextObject.HorizontalAlignment`](ObjectPrimitives.md#textobjecthorizontalalignment) | IntEnum (nested) | [ObjectPrimitives](ObjectPrimitives.md) | Horizontal alignment of a text block. |
| [`TextObject.Spacing`](ObjectPrimitives.md#textobjectspacing) | IntEnum (nested) | [ObjectPrimitives](ObjectPrimitives.md) | Line spacing of a text block; `Custom` uses the leading passed to `SetSpacing`. |
| [`TextObject.StyleRun`](ObjectPrimitives.md#textobjectstylerun) | class (nested) | [ObjectPrimitives](ObjectPrimitives.md) | Run of characters sharing the same formatting: start, length, font, size (world units and points), style... |
| [`TextObject.TabAlignment`](ObjectPrimitives.md#textobjecttabalignment) | IntEnum (nested) | [ObjectPrimitives](ObjectPrimitives.md) | Alignment of the text at a tab stop. |
| [`TextObject.TabStop`](ObjectPrimitives.md#textobjecttabstop) | class (nested) | [ObjectPrimitives](ObjectPrimitives.md) | Tab stop: offset in world units from the left of the text and alignment. |
| [`TextObject.VerticalAlignment`](ObjectPrimitives.md#textobjectverticalalignment) | IntEnum (nested) | [ObjectPrimitives](ObjectPrimitives.md) | Vertical alignment of a text block relative to its origin. |
| [`TextPair`](UILayoutCreate.md#textpair) | class | [UILayoutCreate](UILayoutCreate.md) | Values entered in the two-text dialog. |
| [`TextStyle`](Resources.md#textstyle) | class | [Resources](Resources.md) | Text style (`ObjectType.TextStyle`): font, size and text attributes applied to text objects and dimensions. |
| [`TextStyleData`](DocumentAccess.md#textstyledata) | class | [DocumentAccess](DocumentAccess.md) | Text style flags of a text (bold, italic, underline, outline, shadow), as used by `TextDefaults.GetStyle` /... |
| [`Texture`](Resources.md#texture) | class | [Resources](Resources.md) | Texture (`ObjectType.Texture`): color, reflectivity, transparency and bump of a rendered surface. |
| [`Texture.Part`](Resources.md#texturepart) | IntEnum (nested) | [Resources](Resources.md) | Part of an object a texture is applied to. |
| [`TextVerticalAlignment`](DocumentAccess.md#textverticalalignment) | IntEnum | [DocumentAccess](DocumentAccess.md) | Vertical alignment of new text (`TextDefaults`). |
| [`Tile`](Resources.md#tile) | class | [Resources](Resources.md) | Tile fill (`ObjectType.TileDefinition`): a group of 2D objects repeated over the filled area on a grid. |
| [`TitleBlockBorderObject`](ObjectsAnnotation.md#titleblockborderobject) | class | [ObjectsAnnotation](ObjectsAnnotation.md) | Title block border plug-in object (universal name "Title Block Border"). |
| [`TitleBlockBorderObject.Revision`](ObjectsAnnotation.md#titleblockborderobjectrevision) | class (nested) | [ObjectsAnnotation](ObjectsAnnotation.md) | One revision of a title block: number, date, note, publish date and recipients. |
| [`Tool`](UIAutomation.md#tool) | class | [UIAutomation](UIAutomation.md) | Description of one tool. |
| [`ToolAccess`](UIAutomation.md#toolaccess) | class | [UIAutomation](UIAutomation.md) | Stateless facade over the Vectorworks tool system. |
| [`ToolControl`](UIAutomation.md#toolcontrol) | class | [UIAutomation](UIAutomation.md) | Stateless driver of the active tool. |
| [`ToolCreationType`](UIAutomation.md#toolcreationtype) | IntEnum | [UIAutomation](UIAutomation.md) | What kind of interaction the tool uses to create objects. |
| [`ToolFilter`](UIAutomation.md#toolfilter) | IntEnum | [UIAutomation](UIAutomation.md) | Which tools `ToolAccess.GetTools` returns. |
| [`ToolKey`](UIAutomation.md#toolkey) | IntEnum | [UIAutomation](UIAutomation.md) | Keys that tools react to while points are being entered (see `ToolControl.PressKey`). |
| [`ToolKind`](UIAutomation.md#toolkind) | IntEnum | [UIAutomation](UIAutomation.md) | How a tool is provided. |
| [`ToolMode`](UIAutomation.md#toolmode) | class | [UIAutomation](UIAutomation.md) | Live state of one mode group of the active tool. |
| [`ToolPoint`](UIAutomation.md#toolpoint) | class | [UIAutomation](UIAutomation.md) | One point entered into the active tool, as the tool receives it. |
| [`Math.Transform2D`](ObjectPrimitives.Math.md#mathtransform2d) | class | [Math](ObjectPrimitives.Math.md) | 2D affine transformation. |
| [`Math.Transform3D`](ObjectPrimitives.Math.md#mathtransform3d) | class | [Math](ObjectPrimitives.Math.md) | Python-owned 3D affine matrix acting on column vectors; A * B applies B first. |
| [`Traverse`](DocumentAccess.md#traverse) | IntEnum | [DocumentAccess](DocumentAccess.md) | Which set of objects a document traversal visits. |
| [`TypedResource`](Resources.md#typedresource) | class | [Resources](Resources.md) | Resource restricted to one ResourceType. |

### Index U

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`UndoMethod`](DocumentAccess.md#undomethod) | IntEnum | [DocumentAccess](DocumentAccess.md) | Undo method passed to `Document.StartUndoEvent`. |
| [`UnitSettings`](DocumentAccess.md#unitsettings) | class | [DocumentAccess](DocumentAccess.md) | Primary or secondary dimension units of the active document. |

### Index V

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`Math.VertexType`](ObjectPrimitives.Math.md#mathvertextype) | IntEnum | [Math](ObjectPrimitives.Math.md) | Type of a poly vertex. |
| [`ViewPoint`](UIAutomation.md#viewpoint) | class | [UIAutomation](UIAutomation.md) | Point in view coordinates, in pixels (16-bit coordinates). |
| [`ViewportStyle`](Resources.md#viewportstyle) | class | [Resources](Resources.md) | Viewport style (`ObjectType.ViewportStyle`): the saved settings of a sheet layer viewport. |
| [`ViewSize`](UIAutomation.md#viewsize) | class | [UIAutomation](UIAutomation.md) | Size of the active view pane in pixels. |
| [`VisibilityOptions`](DocumentAccess.md#visibilityoptions) | IntEnum | [DocumentAccess](DocumentAccess.md) | How layers or classes other than the active one are shown. |

### Index W

| Name | Kind | Page | Summary |
|---|---|---|---|
| [`WallObject`](ObjectsArchitect.md#wallobject) | class | [ObjectsArchitect](ObjectsArchitect.md) | Wall (`ObjectType.Wall`) - a straight or curved wall that can host windows, doors and other wall inserts. |
| [`WallObject.BoundKind`](ObjectsArchitect.md#wallobjectboundkind) | IntEnum (nested) | [ObjectsArchitect](ObjectsArchitect.md) | What a wall height bound follows: the layer elevation, the layer wall height or a story level. |
| [`WallObject.BoundStatus`](ObjectsArchitect.md#wallobjectboundstatus) | IntEnum (nested) | [ObjectsArchitect](ObjectsArchitect.md) | Status of a wall height bound (`WallObject.HeightBound.fStatus`). |
| [`WallObject.Caps`](ObjectsArchitect.md#wallobjectcaps) | class (nested) | [ObjectsArchitect](ObjectsArchitect.md) | End caps. |
| [`WallObject.HeightBound`](ObjectsArchitect.md#wallobjectheightbound) | class (nested) | [ObjectsArchitect](ObjectsArchitect.md) | Bound of the bottom or top of the wall: what its height follows. |
| [`WallObject.Heights`](ObjectsArchitect.md#wallobjectheights) | class (nested) | [ObjectsArchitect](ObjectsArchitect.md) | Heights (world units) relative to the layer plane (0 = top of layer, negative = below). |
| [`WallStyle`](Resources.md#wallstyle) | class | [Resources](Resources.md) | Wall style (`ObjectType.WallStyle`): the components, thickness and attributes of a wall. |
| [`WallTextures`](Attributes.md#walltextures) | class | [Attributes](Attributes.md) | Wall textures of a class (internal indices of texture resources, 0 = none). |
| [`WindowObject`](ObjectsArchitect.md#windowobject) | class | [ObjectsArchitect](ObjectsArchitect.md) | Window plug-in object (universal name "Window") from the Architectural Objects plug-in. |
| [`Worksheet`](Resources.md#worksheet) | class | [Resources](Resources.md) | Worksheet. |
| [`WorksheetCell`](Resources.md#worksheetcell) | class | [Resources](Resources.md) | A worksheet cell. |
| [`WorksheetCellContent`](Resources.md#worksheetcellcontent) | class | [Resources](Resources.md) | One cell with its content. |
| [`WorksheetObject`](ObjectsAnnotation.md#worksheetobject) | class | [ObjectsAnnotation](ObjectsAnnotation.md) | Non-owning worksheet RESOURCE, not a placed worksheet image or an annotation plug-in object. |
| [`WorksheetObject.Borders`](ObjectsAnnotation.md#worksheetobjectborders) | class (nested) | [ObjectsAnnotation](ObjectsAnnotation.md) | Cell border flags plus outline and inside range application flags. |
| [`WorksheetObject.Fill`](ObjectsAnnotation.md#worksheetobjectfill) | class (nested) | [ObjectsAnnotation](ObjectsAnnotation.md) | Native fill style, document ColorRef indices and pattern. |
| [`WorksheetObject.NumberFormat`](ObjectsAnnotation.md#worksheetobjectnumberformat) | class (nested) | [ObjectsAnnotation](ObjectsAnnotation.md) | Native worksheet number format, including format-dependent accuracy and UTF-8 leader/trailer. |
| [`WorksheetObject.Range`](ObjectsAnnotation.md#worksheetobjectrange) | class (nested) | [ObjectsAnnotation](ObjectsAnnotation.md) | Inclusive 1-based worksheet range. |
| [`WorksheetObject.TextFormat`](ObjectsAnnotation.md#worksheetobjecttextformat) | class (nested) | [ObjectsAnnotation](ObjectsAnnotation.md) | Worksheet text: point size, font/style, alignments, degree angle, ColorRef index and wrap. |

## Page layout

Every group page follows the same layout:

1. **Title** — the group, the Python module and the Vectorworks version.
2. **Table of contents** — every class, nested type and enumeration of the page.
3. **Overview** — one row per type with its base class and a one-line summary.
4. **Classes** — for each class: its full name, what it inherits from, a description, then tables of constructors, methods (grouped by topic), operators, fields and constants. Nested classes and enumerations follow their owner. Inherited methods are documented once, on the base class.
5. **Enumerations** — members with their numeric values and descriptions.

In Vectorworks, `dir(api)` and `help(...)` show what is available in the running version.

## Statistics

| Page | Classes | Enumerations | Methods | Constructors | Fields | Constants |
|---|---|---|---|---|---|---|
| [DocumentAccess](DocumentAccess.md) | 16 | 11 | 508 | 16 | 18 | 0 |
| [Attributes](Attributes.md) | 17 | 11 | 249 | 17 | 37 | 1 |
| [ObjectPrimitives](ObjectPrimitives.md) | 18 | 6 | 329 | 16 | 17 | 12 |
| [Math](ObjectPrimitives.Math.md) | 15 | 2 | 383 | 36 | 51 | 5 |
| [Objects3D](Objects3D.md) | 25 | 3 | 303 | 25 | 38 | 0 |
| [ObjectsAnnotation](ObjectsAnnotation.md) | 16 | 5 | 291 | 16 | 32 | 0 |
| [ObjectsArchitect](ObjectsArchitect.md) | 14 | 3 | 176 | 14 | 31 | 0 |
| [ObjectsConnectCAD](ObjectsConnectCAD.md) | 10 | 0 | 34 | 10 | 31 | 0 |
| [ObjectsLandmark](ObjectsLandmark.md) | 9 | 19 | 211 | 9 | 0 | 0 |
| [ObjectsSpotlight](ObjectsSpotlight.md) | 4 | 0 | 15 | 4 | 11 | 0 |
| [Resources](Resources.md) | 30 | 10 | 270 | 30 | 29 | 2 |
| [Scripting](Scripting.md) | 2 | 1 | 30 | 2 | 0 | 0 |
| [UIAutomation](UIAutomation.md) | 19 | 13 | 75 | 19 | 81 | 0 |
| [UILayoutCreate](UILayoutCreate.md) | 7 | 9 | 182 | 5 | 12 | 0 |
| **Total** | **202** | **93** | **3056** | **219** | **388** | **20** |

Methods count names (several argument lists of one name count once).
