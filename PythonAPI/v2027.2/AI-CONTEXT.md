# Vectorworks Python `api` - condensed context for AI

## Table of contents

- [1. Rules](#1-rules)
- [2. Where things are](#2-where-things-are)
- [3. Undo - required around every drawing change](#3-undo---required-around-every-drawing-change)
  - [Scripts run through MCP](#scripts-run-through-mcp)
- [4. Recipes](#4-recipes)
- [5. Tools, menus and the Object Info palette](#5-tools-menus-and-the-object-info-palette-tool-palette-tool-bar-mode-bar-simulated-input-menu-commands-oip)
- [6. Gotchas](#6-gotchas)
- [7. Reference](#7-reference)
- [API contract regression checks](#api-contract-regression-checks)

Use this file as AI context when writing Vectorworks Python scripts. It combines API usage rules, recipes, and a condensed reference; the [human documentation](README.md) provides feature-organized explanations.

**Use only `api` and `api.Math` for Vectorworks operations in scripts generated from this context.** The separate public `vs` module provides substantially overlapping functionality, but belongs to a different interface. Do not import `vs`, mix `vs.*` calls with `api.*`, or substitute a `vs` call when an `api` feature is missing. If a requested operation is not exposed here, explain the limitation rather than silently falling back to `vs` or inventing an `api` method. Standard-library imports are fine. Handle compatibility with `vs` is an implementation detail, not a recommendation to mix modules.

`import api` in any Python script run by Vectorworks. `api` is a thin binding of the C++ object API
`VWObjectAPI`: exposed classes, records, and enums omit the native C++ `C`, `S`, `T`, and `E` prefixes;
methods, fields, and constants keep their names and delegate to the C++ implementation. Templates, operators and protected constructors
have Python adapters; this is not complete coverage of the native SDK or every Vectorworks feature.
Script execution is intentionally not exposed: `api` can manage script resources and palettes, but cannot execute scripts.
Automation of already-running dialogs is also intentionally excluded: `CDialogAccess`, `CDialogInput`, their records/enums,
and incomplete deferred dialog helpers are not callable. Creating dialogs with `LayoutDialog`, alerts, and standard dialogs
is a separate supported feature.
Submodule `api.Math` (`import api.Math` or
`from api.Math import Point2D`) holds standalone 2D and 3D geometry. Sections 1-6: rules and recipes. Section 7: complete reference.

## 1. Rules
- Stay within `api` / `api.Math` for Vectorworks operations; do not use the overlapping `vs` interface or mix the two APIs.
- Script management only: create, find, rename, read/write text and language, organize palettes, or delete script resources.
  Creating a resource or changing its text does not run it. `api.CScriptRunner`, `api.SScriptResult`,
  `api.EScriptStatus`, and `ScriptResource.Execute` are not available. Do not generate calls to them or attempt
  nested script execution through `api`; the native C++ script-execution API is deliberately not bound.
- Scripts run by an MCP client: see [Scripts run through MCP](#scripts-run-through-mcp) at the end of section 3.
- Dialog automation exclusion: `api.CDialogAccess`, `api.CDialogInput`, `api.SDialogRect`, `api.SDialogControl`,
  `api.SDialog`, `api.EDialogControlType`, and `api.EDialogControlAction` are unavailable. Their dormant code is
  unbuilt/unregistered in the audited Windows configuration. Do not generate calls to them or to the incomplete
  deferred helpers `RunLater` / `RunOnEventLoop`; do not infer availability from native source definitions.
  `LayoutDialog`, alerts, and standard dialogs are not excluded. See the [dialog creation reference](UILayoutCreate.md).
- Names: remove native `C`/`S`/`T`/`E` type prefixes, including nested types: `VWObjectAPI::CDocument` -> `api.Document`,
  `VWObjectAPI::Math::CPoint3D` -> `api.Math.Point3D`, `CWallObject::SHeightBound` -> `api.WallObject.HeightBound`.
  `T`-prefixed records drop the `T` too (`CWallObject::THeights` -> `api.WallObject.Heights`). Fields keep their native
  names: `T` records use plain names (`startTop`), many `S` records use `f*` names (`HeightBound.fKind`).
  Collision names: records `DialogEvent` / `ListBrowserEvent`, enums `DialogEventType` / `ListBrowserEventType`;
  numeric-leading enums `HardscapeObject.Mode3D`, `SiteModelObject.Display2D` / `Display3D`.
  This breaks old imports/type references: prefixed names are not retained as aliases. The old `STextStyle` alias
  is removed; use `TextStyleData` for the record, `TextStyle` for the resource.
  Python keywords get a `_`: enumerator `None` -> `None_` (`api.Descend.None_`), parameter `from` -> `from_`.
- Keyword arguments use the parameter names of section 7: `doc.GetSelection(descend=api.Descend.Groups)`.
- Results: getters return the value or `None` when it cannot be obtained (invalid wrapper, wrong object kind, missing
  parameter); handle getters return a null handle, collection getters return an empty list, and count getters return zero.
  Factories return invalid wrappers on failure. Most setters and actions return `True`/`False`; check each signature.
  Operational failures use the documented return values - check results. Failed geometry operations (`Math.Polygon2D`
  `Union`/`Intersection`/`Difference`/`SymmetricDifference`/`Offset`, `PolyObject` `Boolean*`/`CombineShapes`) raise
  `RuntimeError`. Binding misuse raises `TypeError`
  (no overload accepts the arguments; the message lists every signature) or `IndexError`; callback exceptions propagate.
- Units: lengths and coordinates are WORLD UNITS = millimetres, whatever the document units ("2 m" -> 2000).
  `doc.UnitsToWorld(v)` / `doc.WorldToUnits(v)` convert from/to the document units (`doc.PrimaryUnits()`).
  Angles are radians, counter-clockwise from +X (`api.Math.DegToRad`). Exceptions (marked in section 7): `Marker.angle`,
  `DropShadow.angle` and roof `Edge.slope` in degrees; `Marker.length/width` in page inches; `*Mils` line weights in
  1/1000 inch (`*Millimeters` variants exist); raw plug-in parameters (`GetParamReal/SetParamReal`) use world units for
  lengths but DEGREES for angles. Indexes are 0-based except worksheet rows/columns (1-based).
- Colors: `ColorRGB` channels are 16 bit (0-65535): use `api.ColorRGB.FromRGB8(r, g, b)` and `.Red8()`. Ints named
  `*ColorIndex`, `ColorPair`, `ObjectColors` are palette indices (`api.AttributesBase.RGBToColorIndex(rgb)`,
  `ColorIndexToRGB(i)`). Opacity is 0-100 (`api.kMaxOpacity`). Strings are UTF-8 `str`; name lookups ignore case, but
  pass plug-in universal names exactly (`ParametricObject.GetPluginKind` requires it; a wrongly cased name to `Create`
  or `GetDefinitionFormat` can define a wrongly named plug-in format).
- Handles: `api.Handle` shares its underlying type with `vs.Handle`, but this compatibility does not authorize mixing APIs.
  A null handle is returned as a FALSY `api.Handle` (test `if h:`, not `is None`); pass `None` as a null handle.
  An api wrapper is accepted wherever a `Handle` is expected. Report unsupported operations rather than using `vs` as a fallback.
- Wrappers (`*Object`, `Layer`, `ClassAttributes`, `Resource` and subclasses, attribute views) are non-owning views
  of one drawing object: cheap, any number per object, hashable by handle (set/dict keys), `bool(w)` = `w.IsValid()`;
  objects, layers, classes and resources also compare `==` by handle. `obj.Delete()` invalidates that wrapper; never use
  other wrappers or handles of a deleted object.
- Typed wrapper from a handle: `api.ArcObject(h)` (falsy when h is not an arc), `api.ArcObject.Is(h)`,
  `api.Document.As(api.ArcObject, h)` (None when not an arc). `type` arguments (As, GetObjectsOf, GetSelectionOf) must
  be classes with a static `Is` (header marker `+Is` or an `Is(h)` line in section 7).
- ANY object: `api.PrimitiveObject(h)` gives name, class, attributes, bounds, hierarchy, move/rotate/scale/mirror,
  delete, reset. ANY plug-in (parametric) object: `api.ArchitectObject(h)`, `api.LandmarkObject(h)` or
  `api.AnnotationObject(h)` add `GetParametricName/GetParamNames/HasParam/GetParam*/SetParam*` (and styles on
  AnnotationObject). These four accept every non-null handle; the concrete classes check the object kind.
- Value types (records and all `api.Math` classes) are Python-owned copies. Changing a returned struct does not
  change the drawing: change it, then pass it to the setter (`hs = wall.GetHeights(); hs.startTop = 3000; wall.SetHeights(hs)`).
  A struct field that is itself a struct is a live view into its parent (`colors.pen.fore = 5` edits `colors`); list and
  optional fields return copies (assign the whole value back). `copy.copy(v)` duplicates; `repr(v)` shows the fields.
- Compatibility: native field names (including `f*` fields) and existing factory ownership defaults remain available;
  prefixed record names are not (see Names).
  `UnitSettings.IsMetric()` aliases `GetIsMetric()`. Do not infer ownership from
  another factory: handle-based extrude factories consume inputs by default, while generic-solid factories preserve them.
- Struct construction: by constructor (section 7 headers) or, when no constructor matches, from fields: positionally
  with ALL field values in order, or by keyword with any of them (`api.WorksheetCell(2, 1)`, `api.ViewPoint(x=10, y=20)`).
  Struct ARGUMENTS also accept a tuple/list (constructor or field values) or a dict of fields: `(100, 200)` /
  `{'x': 100, 'y': 200}` for `Point2D`, `[(0, 0), (1000, 0)]` for `[Point2D]`. `api.Point2D` and `api.Math.Point2D`
  (likewise `api.Point3D` and `api.Math.Point3D`) convert into each other.
- When overloads differ only by struct type (`ToolControl.Click(Point2D|Point3D|ViewPoint)`) a tuple selects the
  first one (Point2D): construct the type explicitly (`api.Point3D(x=0, y=0, z=0)`, `api.ViewPoint(x=5, y=5)`).
- Enums are `enum.IntEnum` (`api.Descend` is `IntFlag`: `api.Descend.Groups | api.Descend.Viewports`); plain ints are
  accepted; values outside the enum come back as plain ints.
- Callbacks (`fn(Handle)`, `fn(Layer)`, ...): any callable, run synchronously, result ignored, cannot stop early (use the
  list-returning twin). If a callback raises, the remaining calls are skipped and the exception propagates.
- `help(api.Document)` / `help(api.Document.Select)` print every signature; `dir(api)`, `dir(api.Math)` list names.
- Document access requires an open drawing: `api.Document.IsOpen()`. `api.Document()` and the other facades are
  stateless; construct them freely.

## 2. Where things are
| Need | Use |
|---|---|
| Selection, finding objects, layers, classes, view, units, undo, preferences | `doc = api.Document()` |
| Create/edit 2D shapes | `Locus2DObject Line2DObject RectangleObject RoundRectObject ArcObject CircleObject PolygonObject PolylineObject GroupObject TextObject` (static `Create*`); 2D Booleans: static `PolyObject.CombineShapes(op, first, second)` for any two 2D shapes (e.g. rectangle minus circle) and the inherited `PolyObject` Boolean methods return detached handles of 2D objects of any type; `PolyObject.AlignShapePlanes(first, second)` first moves shapes of different planes into one (no undo: register both) |
| Create/edit extrudes | `ExtrudeObject`: `Create`, `CreatePlanar`, `CreateBetween`; local dimensions, profile, holes, 3D transform and volume (reference at the end) |
| Sweeps, multiple extrudes and modeling factories | `SweepObject`, `MultiExtrudeObject`, `SurfaceModelObject`: always preserve inputs; loft, rail-sweep, revolve, rail-guided revolve, extrude-along-path, tapered-extrude, cylinder/torus/box (reference below) |
| Create/edit solid models | `GenericSolidObject`: native Boolean operations, extrude factories, operand/history access, placement, scale, volume and surface area; explicit `ClearHistory()` for a flattened generic solid; `ConvertToGenericSolid(h)` / `CanConvertToGenericSolid(h)` convert any 3D object (CSG, extrude, mesh, sphere/hemisphere/cone, closed 3D polygon, ...) to a history-free generic solid, like VectorScript `ConvertToGenericSolid` (reference at the end) |
| Create/edit 3D polygons | `Polygon3DObject`: `Create` from 3D points, a `Polygon2D` or a `Rect2D`; vertex editing, open/closed, plane/normal, length/area, closest point, cleanup/simplify and 3D move/rotate/scale/transform (reference at the end) |
| Create/edit NURBS curves and surfaces | `NurbsCurveObject` / `NurbsSurfaceObject`: control points, weights, knots, degree inspection, evaluation, curve/surface extension and offset, surface trimming, and selected-curve-network surface creation (reference at the end) |
| Create/edit meshes | `MeshObject`: `Create` from vertices and faces, `CreateFromPolygons`, `CreateFromObject` (mesh any 3D object); vertices, faces, normals, UVs, texture parts, smoothing, closedness, volume, 3D transforms; `ToGenericSolid`/`Union`/`Subtract`/`Intersect` build solids, `GenericSolidObject.ConvertToMesh` goes back (reference at the end) |
| Create/edit shell solids | `ShellObject` (a `GenericSolidObject`): `Create` thickens a NURBS surface (VectorScript `CreateShell`), `CreateFromSolid` hollows a solid with open faces; thickness, side (`IsReversed`), source operand and selected faces; inherited history/`Rebuild` (reference at the end) |
| Create/edit spheres, hemispheres, cones | `SphereObject`, `HemisphereObject`, `ConeObject` (base `SolidPrimitiveObject`): center/radii, top point, base/tip/height/radii; frame, axis, move/rotate/scale; `ToGenericSolid`/`Union`/`Subtract`/`Intersect`/`ToMesh`; `GetPrimitiveOperands` (reference at the end) |
| Any object | `PrimitiveObject(h)`; kind: `api.Document.GetObjectType(h)` (ObjectType), plug-in name: `api.ArchitectObject(h).GetParametricName()` |
| Any plug-in object WITHOUT a specific wrapper (fallback only) | `ParametricObject`: `GetParameterDefinitions(universalName)` lists parameters and types, `GetDefinitionChoices` the choices of a pop-up, `GetPluginKind` the placement (`Create` at a point, `CreateFromPath` on a path); `Get/SetParam*` by universal parameter name, then `Reset()` |
| Pen, fill, fill mapping, markers, drop shadow, opacity, class | `obj.Attributes()` or `api.Document.AttributesOf(h)` -> `ObjectAttributes`: `Pen() Fill() FillMapping() Markers() DropShadow()` |
| Classes / layers | `ClassAttributes` (FromName, Create, GetAll), `Layer` (`doc.GetLayers() FindLayer() CreateDesignLayer() CreateSheetLayer()`) |
| Stories, levels, level types | `doc.GetStories() FindStory() CreateStory()` -> `Story` (`AddLevel`, `GetLevels`, `GetLayerForLevelType`, `SetElevation(elevation, StoryElevationChangeMode)`); `doc.GetLevelTypes() AddLevelType()`, `doc.GetStoryLevelTemplates()`; `Layer.AssociateWithStory()`; story-bound walls: `WallObject.SetHeightBounds()` |
| Dimensions | `LinearDimensionObject.CreateHorizontal/Vertical/Constrained/Unconstrained/Ordinate`, `AngularDimensionObject`, `ArcLengthDimensionObject`, `RadialDimensionObject`, `CenterMarkObject` |
| Full worksheet editor | `WorksheetObject : TypedResource`: native 1-based cells/ranges/subrows, definition strings, opaque database criteria, sizing, formatting, merging, recalculation and drawing image linkage. See [worksheet editor](ObjectsAnnotation.md#worksheetobject). |
| Data tags, title block borders (style based) | `DataTagObject`, `TitleBlockBorderObject`: `EnsureStyle(name)` then `Create(...)` |
| Building elements | `WallObject SlabObject RoofObject` (native objects) and `WindowObject DoorObject ColumnObject StairObject` (plug-ins) |
| Landscape | `PlantObject LandscapeAreaObject SiteModelObject SiteModifierObject StakeObject HardscapeObject PropertyLineObject ExistingTreeObject` |
| Spotlight lighting devices, GDTF fixture types | `LightingDeviceObject` (`Create`, `SetGDTF`, `SetUseGDTFGeometry`), `GDTFLibrary` (`GetAvailable`, `Import`); generic parameters from `ParametricObject` |
| ConnectCAD devices, sockets, device types | `ConnectCADDeviceObject` (`CreateFromJSON`, `GetSockets`, `AddSocket`, `CreateDeviceType`), `ConnectCADSocketObject`, `ConnectCADLibrary` (`GetSignals`, `GetConnectors`, `ValidateDevice`) |
| Resources | `ResourceList` (list document or library content, import), `Resource` + typed: `SymbolDefinition Hatch Gradient Tile ImageFill LineType Texture RecordFormat Worksheet TextStyle WallStyle SlabStyle RoofStyle ViewportStyle BuildingMaterial DataVisualization RenderStyle RenderBackground ResourceFolder` |
| Manage script resources (no execution) | `api.ScriptResource` and `api.ScriptPalette` find, edit, and manage scripts in the current document; `api.ScriptLanguage` identifies the stored language |
| Tools: activate, Tool bar, simulated clicks/keys | `api.ToolAccess()` -> `ModeBar()`, `Control()` |
| Menus: installed commands, menu bar, chunk items, execute | `api.MenuAccess()` -> `GetMenuCommands()`, `GetMenuEntries()`, `GetChunkItems()`, `ExecuteMenu()`, `GetMenuStatus()` |
| Object Info palette: read and change its controls like the user | `api.OIPAccess()` -> `GetControls()`, `FindControl()`, `GetValue()`, `SetValue()` |
| Alerts, questions, value dialogs, custom dialogs | `api.Alerts` (Inform, Critical, Question, Confirm), `api.StandardDialogs` (EditText, EditInteger, EditDimension, ChooseFromList, ...), `api.LayoutDialog` (any layout manager dialog; end of section 5) |
| Geometry math | `api.Math` (`Point2D` = `Vector2D`, `Transform2D Rect2D RotatedRect2D Line2D Circle2D Arc2D Polygon2D`; `Point3D` = `Vector3D`, `Transform3D Line3D Plane3D`); `Polygon2D` holes, value-based Boolean operations, and miter/round offsets; 3D math is Python-owned and does not create drawing objects |
| Raw preferences by selector | `ProgramVariables` |

## 3. Undo - required around every drawing change
1. `doc.StartUndoEvent()` (method `UndoMethod.SwapObjects`) and `doc.NameUndoEvent("Label")` before any change.
2. `doc.AddAfterSwapObject(h)` AFTER creating an object; `doc.AddBothSwapObject(h)` BEFORE modifying one (`None`
   registers the whole selection); `Delete()` / `DeleteSelection()` record themselves. The story methods (`Story`,
   the level type and default story level methods of `Document`, `Layer.SetLevelType/AssociateWithStory/DetachFromStory`)
   also record themselves, including the layers they create: do not register those again. Moving an object into another
   layer, group or symbol definition (`MoveToContainer`) needs the move pair instead: `doc.AddBeforeMoveObject(h)` BEFORE
   and `doc.AddAfterMoveObject(h)` after the move, and no other registration of that object in the event.
3. `doc.EndUndoEvent()`. Read-only scripts must not open an undo event.
4. To take everything back when a step fails: open the event with `doc.StartUndoEvent(isRevertible=True)` and, on the
   failure path, call `doc.RevertUndoEvent()` INSTEAD of `EndUndoEvent()` (each of them ends the event: never both).
   It undoes what the event recorded (registered objects, `Delete()`, the story methods) and removes the event. Only an
   event opened with `isRevertible=True` can be reverted; for another event nothing is reverted. `doc.IsBuildingUndoEvent()`
   tells whether an undo event is being built (also one that Vectorworks opened for the running script);
   `RevertUndoEvent()` returns `False` and does nothing when none is. In an event that is already being built, the
   revertible event is nested: it reverts only what was recorded since its own `StartUndoEvent()`. When an application
   runs the script inside an undo event it owns, `StartUndoEvent`, `NameUndoEvent`, `EndUndoEvent` and `RevertUndoEvent`
   do nothing (`RevertUndoEvent()` returns `False`): do not treat that as an error.

```python
import api
from api.Math import Rect2D

doc = api.Document()
doc.StartUndoEvent(isRevertible=True); doc.NameUndoEvent("Create a rectangle")
is_done = False
try:
    r = api.RectangleObject.Create(Rect2D(0, 1000, 2000, 0))
    if not r:
        raise RuntimeError("Rectangle creation failed")
    doc.AddAfterSwapObject(r)
    is_done = True
finally:
    if is_done:
        doc.EndUndoEvent()
    else:
        doc.RevertUndoEvent()          # removes what was created before the failure
```

### Scripts run through MCP
An MCP client, such as an AI assistant connected to the Vectorworks MCP server, runs a script with `runPythonScript`
(code) or `runScript` (a saved Python script resource). Vectorworks runs the whole script as ONE undo step "MCP: script"
that it opens itself. Items 1-4 still apply to scripts run in other ways; in an MCP run:
- `doc.StartUndoEvent()`, `NameUndoEvent()`, `EndUndoEvent()` and `RevertUndoEvent()` do nothing (`RevertUndoEvent()`
  returns `False`, see item 4), so a script written as above runs unchanged.
- Registration is still required (item 2): `doc.AddAfterSwapObject(h)` after creating an object, `doc.AddBothSwapObject(h)`
  BEFORE changing one, and the move pair around `MoveToContainer`. Undo, and the revert of a failed run, take back only what was
  recorded (item 4): a change that nothing recorded stays.
- A run that ends with an exception, or does not compile, is reverted as a whole: what it recorded is undone, and the
  result reports `rolledBack`. To give up after a failure, let the exception propagate or re-raise it; a script that
  catches it and ends normally keeps its changes so far, because its own `RevertUndoEvent()` does nothing.
- Use only `api` (section 1): the undo calls of `vs` reach Vectorworks directly and can rename the step or clear the
  undo history.
- Print results as JSON (`import json`, then `print(json.dumps({"created": count}))`): the printed text comes back to
  the client as `output`, a traceback as `errors`.
- Never wait for user input: no `api.Alerts`, `api.StandardDialogs` or `api.LayoutDialog`, and no tool, menu command
  or Object Info palette button that opens a dialog (section 5); the run would wait until the user closes it. Prefer
  `api` object methods to the user-input automation of section 5.
- Scripts run on the main thread of Vectorworks: an endless loop freezes Vectorworks.
- Inside the script, `api` still cannot run other scripts.

## 4. Recipes
```python
import api
from api.Math import Point2D, DegToRad
doc = api.Document()

# Read script resources without executing them
for script in api.ScriptResource.GetAll():
    print(script.GetName(), script.GetLanguage(), script.GetText())

# Read: selection, typed views, search
for h in doc.GetSelection():                      # working layers; GetSelectionOnAllLayers() for every layer
    o = api.PrimitiveObject(h)
    print(api.Document.GetObjectType(h).name, o.GetName(), o.GetBounds(), o.GetClass().GetName())
lines = doc.GetSelectionOf(api.Line2DObject)     # [Line2DObject]
walls = doc.GetObjectsOf(api.WallObject, api.Traverse.Visible, api.Descend.Groups)
hs = doc.GetObjectsInCriteria("((T=RECT) & (C='A-Walls'))")   # criteria syntax of VectorScript, see GetCriteriaError
# (L='Layer-1')  (PON='Door')  (R IN ['MyRecord'])  ('MyRecord'.'Width' > 100)
near = doc.GetObjectsAtPoint((0, 0), 10.0)       # hit test, radius in mm

# Create (new objects go to the active layer / edited container: doc.GetDefaultContainer())
doc.StartUndoEvent(); doc.NameUndoEvent("Create shapes")
r = api.RectangleObject.Create(Point2D(0, 0), 2000, 1000)        # center, width, height
l = api.Line2DObject.Create((0, 0), (5000, 0))
p = api.PolygonObject.Create([(0, 0), (1000, 0), (500, 800)])     # closed
c = api.CircleObject.Create((3000, 0), 500)
for o in (r, l, p, c):
    if o:
        doc.AddAfterSwapObject(o)
doc.EndUndoEvent()

# Modify attributes, class, geometry
doc.StartUndoEvent(); doc.NameUndoEvent("Restyle")
cls = api.ClassAttributes.Create("A-Walls")      # existing class when the name is taken
cls.SetPenForeColor(api.ColorRGB.FromRGB8(0, 0, 255))
for h in doc.GetSelection():
    doc.AddBothSwapObject(h)                      # BEFORE the change
    o = api.PrimitiveObject(h)
    o.SetClass(cls, useClassAttributes=True)
    pen = o.Attributes().Pen()
    pen.SetForeColor(api.ColorRGB.FromRGB8(255, 0, 0)); pen.SetLineWeightMillimeters(0.35)
    fill = o.Attributes().Fill()
    fill.SetSolid(); fill.SetForeColor(api.ColorRGB.FromRGB8(220, 230, 255)); fill.SetOpacity(50)
    o.Rotate(DegToRad(15), o.GetBounds().Center())
doc.EndUndoEvent()

# Layers and classes
lay = doc.CreateDesignLayer("Site", 100.0)        # 1:100
lay.Activate()                                    # or doc.SetActiveLayer(lay)
doc.SetActiveClass(cls)
for L in doc.GetLayers():
    print(L.GetName(), L.GetType(), L.GetObjectCount(), L.GetVisibility())

# Plug-in objects: typed accessors + generic parameters, then Reset() to regenerate
w = api.WindowObject.Create((0, 0))
w.SetWidth(900); w.SetHeight(1200)                 # palette size, measured as w.GetSizeReference() says
w.SetSillHeight(800); w.SetParamBool("IncludeSill", True)   # sill after the height (keeps ElevationSetAt)
w.Reset()                                         # REQUIRED after parameter changes
print(w.GetParamNames())                          # discover parameter names (LandmarkObject.GetParamType gives types)
po = api.LandmarkObject(h)                       # any plug-in object, e.g. one without a typed wrapper
wall = api.WallObject.Create((0, 0), (6000, 0), 200)   # start, end, thickness

# Annotation
dim = api.LinearDimensionObject.CreateHorizontal((0, 0), (6000, 0), offset=500)
style = api.DataTagObject.EnsureStyle("")        # name of the style now available (imported if needed; "" = none)
tag = api.DataTagObject.Create((0, -1000), style, wall)   # tags 'wall'

# Resources: library content, import, use
lst = api.ResourceList.FromFolder(api.ResourceType.Hatch, api.ContentFolder.Hatches)
for e in lst.GetEntries():
    print(e.index, e.actualName, e.isInDocument)
res = lst.Import(0, api.ImportConflict.Rename)  # by index or name -> Resource (falsy on failure)
r.Attributes().Fill().SetResource(res.GetInternalIndex())   # hatch / tile / gradient / image fill by internal index
sym = api.SymbolDefinition.FromName("Chair")
if sym:
    hInst = sym.Insert((1000, 0), DegToRad(90))
ws = api.Worksheet.Create("Report", rows=10, columns=3)
ws.SetCellFormula(api.WorksheetCell(1, 1), "Count")             # row, column: 1-based
ws.SetCellFormula((2, 1), "=COUNT(ALL)"); ws.Recalculate(); print(ws.GetCellText((2, 1)))
ws.CreateImage((0, 0))                            # place the worksheet on the active layer

# Math
from api.Math import Transform2D, Polygon2D
t = Transform2D.Rotation(DegToRad(90), Point2D(0, 0)) * Transform2D.Translation(100, 0)  # translate, then rotate
poly = p.GetPolygon()                             # copy (Polygon2D); edit, then p.SetPolygon(poly)
pts = [v.point for v in poly]                     # PolyVertex: point, type, arcRadius, visible
poly[0] = Point2D(-100, 0); poly.Transform(t); p.SetPolygon(poly)
```

## 5. Tools, menus and the Object Info palette (tool palette, Tool bar (mode bar), simulated input, menu commands, OIP)
```python
tools = api.ToolAccess()
if tools.ActivateTool("Rectangle"):               # universal name or English name (Tool.fName)
    mb = tools.ModeBar()
    for m in mb.GetModes():
        print(m.fIndex, m.fType.name, m.fLabel, m.fValue, [ch.fName for ch in m.fChoices])
    mb.SetMode(0, "Rotated Rectangle Mode")        # generic text value, or SelectChoice(i, n) / typed setters
    ctl = tools.Control()
    ctl.Click(Point2D(0, 0)); ctl.Click(Point2D(2000, 1000))  # model points: exact, no snapping (click-click mode)
    ctl.Click(api.ViewPoint(x=300, y=200))        # pixel in the drawing pane: like a user click, with snapping
    ctl.PressKey(api.ToolKey.Return)              # Finish(), Cancel(), RemoveLastPoint() exist too
tools.ActivateSelectionTool()
```
- Only tools in the current workspace can be activated (`GetTools(api.ToolFilter.Activatable)`, `CanActivateTool`).
- Input behaves exactly like user input (previews, undo, dialogs the tool opens). Re-read the Tool bar after changes.
- Mode index = SDK mode group - 1. Pressing a "Preferences" mode button opens a dialog.

```python
menus = api.MenuAccess()
print(menus.GetMenuTitles())                      # ['File', 'Edit', 'View', ...]
for e in menus.GetMenuEntries("Modify"):          # one menu with its submenus; chunks expanded into their items
    if e.fType != api.MenuEntryType.Separator:
        print(" > ".join(e.fMenuPath + [e.fText]), e.fUniversalName, e.fChunkItemIndex, e.fIsEnabled)
if not menus.ExecuteMenu("Select All"):           # universal name ("-34"), English name or display title
    print(menus.GetMenuStatus("Select All").name) # why not: NotInWorkspace, Disabled, ...
for item in menus.GetChunkItems("Standard Views"):   # current items of a chunk
    print(item.fIndex, item.fText, item.fIsEnabled)
menus.ExecuteMenu("Standard Views", "Top/Plan")   # chunk item by text, or by index: ExecuteMenu(name, 0)
e = menus.FindMenuEntry(["View", "Standard Views", "Top/Plan"])
if e:
    menus.ExecuteMenuEntry(e)
for c in menus.GetMenuCommands(api.MenuFilter.InWorkspace):
    print(c.fUniversalName, c.fName, c.fDisplayName, c.fKind.name, c.fIsChunk, c.fShortcut)
```
- Commands are identified by universal name. Built-in commands use negative numbers ("-28") and also accept their English
  name (`MenuCommand.fName`, the name `vs.DoMenuTextByName` expects) and their display title (the trailing "..." is optional).
- A chunk (`MenuCommand.fIsChunk`) provides several items (recent files, standard views, render modes). Address an item
  by its text or its 0-based index (`vs.DoMenuTextByName` uses index + 1). Separators and empty placeholders are left out;
  `fIndex` keeps positions.
- Chunk items (count, texts, check marks) come from the menu bar, which Vectorworks updates when the user works with the
  menus, not while a script runs; `fIsEnabled` is always current. A chunk runs the item at the index in its current data:
  once the script changed that data (e.g. opened a document, which changes the recent files), the items may not match.
- Only commands placed in the current workspace (menu bar or context menus) run. Executing behaves like choosing the item:
  the command may open a dialog (the call returns when it is closed) and creates its own undo event, so do not wrap it in
  `doc.StartUndoEvent()` / `EndUndoEvent()`. A False result is explained by `GetMenuStatus(name)`.

```python
oip = api.OIPAccess()
doc.SetSelection([h])                             # the OIP shows the selection (one or several objects)
for c in oip.GetControls(api.OIPPane.Shape):     # visible controls in id order; includeHidden=True for all
    print(c.fId, c.fType.name, c.fLabel, c.fValue, c.fChoices, c.fIsEnabled)
cid = oip.FindControl(api.OIPPane.Shape, "Class")   # by label: case-insensitive, trailing ':' ignored
if cid is not None:
    oip.SetValue(api.OIPPane.Shape, cid, "Walls")    # generic: interpreted by control type
cid = oip.FindControl(api.OIPPane.Shape, "Width")   # look up again: the change above may have rebuilt the OIP
if cid is not None:
    oip.SetText(api.OIPPane.Shape, cid, "2000")      # typed setters: SetText, SetChecked, SelectChoice, PressButton
s = api.OIPSetting(); s.fPane = api.OIPPane.Shape; s.fControlId = oip.FindControl(api.OIPPane.Shape, "Class"); s.fValue = "None"
oip.SetValues([s])                                # several changes in order; stops at the first failure
```
- Control ids are valid until the OIP is rebuilt (selection change, or a change that shows/hides controls): look them up
  again (`FindControl`, `GetControls`) after each change.
- A change goes through the same core path as a user edit on Windows and macOS: the selection is changed, plug-in objects
  are reset immediately (also while the script runs) and an undo event is created, so do not wrap it in
  `doc.StartUndoEvent()` / `EndUndoEvent()`.
- `SetValue` text per type: EditText - typed text (units/math evaluated); CheckBox - on/off/true/false/1/0/toggle;
  RadioGroup/PullDown/ClassPullDown/LayerPullDown/SearchablePullDown - item text (case-insensitive) or 0-based index;
  Button - presses it (value ignored). Disabled, hidden and read-only controls are not changed (False).
- Buttons and some items ("New...", "Edit...") open dialogs; the call returns when they are closed.
- SearchablePullDown reports only `fChoiceCount`/`fSelectedChoice`/`fValue` (no `fChoices`); select by item text or index.
- `Other` controls (box position, 3D location, color, lists, ...) are listed but have no typed setter; `NotifyChanged`
  sends a raw switchboard change (expert use).

### Alerts and dialogs (`Alerts`, `StandardDialogs`, `LayoutDialog`; guide: [UILayoutCreate.md](UILayoutCreate.md))
```python
api.Alerts.Inform("Done.", "12 files written.")
if api.Alerts.Confirm("Delete the selection?", okText="Delete"): ...
name = api.StandardDialogs.EditText("Rename", "New name:", "Wall-1", isEmptyAllowed=False)   # None on cancel
if name is not None: ...
idx = api.StandardDialogs.ChooseFromList("Pick", "Style:", ["A", "B", "C"])                  # int? (0-based)

ID_LBL, ID_NAME, ID_KIND, ID_GROUP = 3, 4, 5, 6
dlg = api.LayoutDialog("Settings", okText="Create")
dlg.AddStaticText(ID_LBL, "Name:", 10); dlg.AddEditText(ID_NAME, "Copy", 25)
dlg.AddPullDownMenu(ID_KIND, 20); dlg.AddCheckBox(ID_GROUP, "Group copies")
dlg.SetFirstItem(ID_LBL); dlg.PlaceRight(ID_LBL, ID_NAME)
dlg.PlaceBelow(ID_LBL, ID_KIND); dlg.PlaceBelow(ID_KIND, ID_GROUP)
dlg.SetChoices(ID_KIND, ["Line", "Grid"]); dlg.SelectChoice(ID_KIND, 0)     # queued until the dialog is shown
def on_ok(ev):
    if not dlg.GetText(ID_NAME):
        api.Alerts.Critical("Enter a name."); dlg.CancelClose()           # keeps the dialog open
dlg.OnOk(on_ok)
dlg.OnControl(ID_KIND, lambda ev: dlg.Enable(ID_GROUP, dlg.GetSelectedChoice(ID_KIND) == 1))
if dlg.Run() == api.DialogResult.Ok:
    print(dlg.GetText(ID_NAME), dlg.GetSelectedChoiceText(ID_KIND), dlg.GetBool(ID_GROUP))
```
- Standard dialogs return `None` on cancel. Lengths/points are world units (mm, shown to the user in
  document units); angles are DEGREES (unlike the rest of `api`), also for `AddEditReal(..., EditRealType.Angle)`.
- `LayoutDialog` runs AT MOST ONCE and is not copyable: build a new instance for each showing. OK = controlID 1, Cancel = controlID 2;
  use control ids 3..9999, unique per dialog. Widths are in characters and heights in lines unless named `*InPixels`.
- Identifier roles: controlID/referenceControlID identify controls; groupControlID/paneControlID identify group-box controls;
  tabControlID/swapControlID identify containers. Tree itemID/parentID identify tree items, not dialog controls.
- AlignLeft|AlignRight|AlignBottom(controlID, alignmentGroupID, isResizing=False) assign ONE control to a shared edge-alignment
  group. Call the same method for each participating control with the same alignmentGroupID. This is NOT a second control
  or group-box ID; no matching control is required. Choose a positive signed-16-bit group ID (e.g. 20000).
  False shifts the control; True resizes it. Calls are allowed before Run only.
- Python keyword migration: id -> controlID; placement referenceID -> referenceControlID; groupID -> groupControlID;
  paneGroupID -> paneControlID. For Align* specifically: old referenceID -> controlID, old id -> alignmentGroupID.
  Positional order, types and defaults are unchanged.
- Placement: `SetFirstItem` for the first top-level control, then `PlaceBelow`/`PlaceRight(referenceControlID, controlID)`. Children of a
  group box / tab pane / swap pane: `SetFirstGroupItem(groupControlID, controlID)` then `PlaceBelow`/`PlaceRight` among siblings. Tabs:
  `AddTabControl(tab)`, one `AddGroupBox(pane, "Label")` per page, `AddTabPane(tab, pane)`.
- Setters called before `Run()` are queued and applied before `OnSetup`. EXCEPTION: `AddTreeItem` works only while running
  (fill trees in `OnSetup`). Getters return `None` before the dialog is shown, live values while it runs, and values
  captured at close after `Run()` (also on Cancel: check the `Run()` result).
- Handlers take one `DialogEvent` (`fControlID`, `fEvent`, `fData`, `fIsNegative`); return value ignored; a newer
  registration replaces the older. `CancelClose()` in `OnOk`/`OnCancel` keeps the dialog open; `Close(isOk)` from any
  handler closes it without calling `OnOk`/`OnCancel`. List browser detail: `GetListBrowserEvent(controlID)` inside its
  `OnControl` handler. If a handler raises, later handlers are skipped and the exception propagates when `Run()` returns.

## 6. Gotchas
- Check `if obj:` after `Create...`; failures give an invalid (falsy) wrapper, not an exception.
- Selection getters cover the working layers only; `*OnAllLayers` variants cover every layer. `Select([h...])` adds,
  `SetSelection([h...])` replaces, `DeselectAll()` clears.
- `Get*` returning structs/Math values and `GetPolygon()` give copies: write them back with the setter.
- `kNotFound` (2**64-1) is returned by `ResourceList.Find` / `Add` and `RecordFormat.FindField` when nothing matches.
- Native walls/slabs/roofs have no plug-in parameters (`GetParam*` -> None); windows/doors/columns/stairs and all
  landscape and annotation objects do. Parameters starting with `__` are private plug-in state. Parameters taken "by
  style" are read from the style; change the style or detach it (`RemoveStyle`) first.
- Raw indices (`GetInternalIndex`, `*Resource`, `*Style` ints) refer to resources of the current drawing only.
- Use `doc.Redraw(rect)` only after edits made outside the API (e.g. with `vs`).

## 7. Reference
Format: `### Class(ctor args) | (other ctor)  : Base` then description, fields, props, methods. `T?` = T or None, `[T]` = list,
`(A, B)` = tuple, `(T *4)` = 4-tuple, `{K: V}` = dict, `fn(A)` = callable taking A, `A|B` = either type, `[s]` = static (call on
the class), `name=default` = optional argument (type implied by the default), `max` = no limit. `Handle` = vs.Handle; `int` also
covers C++ index/size/color/opacity types. `props:` lists getter/setter pairs: `Name: T` means `GetName() -> T?` and
`SetName(v: T) -> bool`. A boolean property named `IsX` normally maps to `IsX()` / `SetX(v)`, except
`UnitSettings.IsMetric` (`IsMetric()` or `GetIsMetric()` / `SetIsMetric(v)`), `TitleBlockBorderObject.IsActiveTitleBlock` and
`HardscapeObject.IsSiteModifier` / `IsPathway` (`GetIsX()` / `SetIsX(v)`). `T: Name1, Name2` lists several props of type T. Classes inherit the members of `: Base`.
Header markers: `+Is` = `Is(h: Handle) -> bool [s]` (h is this kind of object), `+Duplicate` = `Duplicate() -> <same class>`
(copy of the object). `GetA|B(...) -> ta|tb` lines are families: GetA returns ta, GetB returns tb (same for argument types).
Math types (Point2D/Vector2D, Transform2D, Rect2D, RotatedRect2D, Line2D, Circle2D, Arc2D, Polygon2D, PolyVertex,
VertexType, OffsetJoin, Point3D/Vector3D, Transform3D, Line3D, Plane3D, kEpsilon) live in `api.Math`. Nested types are `Outer.Inner` (e.g. `api.Texture.Part`).
The 3D values use world millimetres. `Point3D` converts to/from legacy `api.Point3D`; zero normalization returns zero,
and `AngleBetween` is unsigned in `[0, pi]` (zero-vector angle is zero). `Transform3D` acts on column vectors, so `A * B`
applies `B` first; angles are right-handed radians. `Rotation(angle, axis, center)` and `Mirror(origin, normal)` return
`None` for zero/non-finite axes; `Inverse()` and `ApplyToNormal()` return `None` when the transform is singular.
`ApplyToNormal` and `Plane3D.Transformed` use the inverse transpose. `Plane3D()` is the XY plane with +Z normal;
plane equality ignores normal orientation. `Line3D.Intersect` does not return collinear overlap, while `Intersects` includes it.
See [3D geometry](ObjectPrimitives.Math.md#mathpoint3d) for constructors, fields, all methods/operators, and intersection details.
Module constants: api.kMaxOpacity=100.

### ==== Document, layers, preferences ====

### TextStyleData()
fields: bold: bool, italic: bool, underline: bool, outline: bool, shadow: bool
- ToBits() -> int
- FromBits(bits: int) -> TextStyleData [s]

### ProgramVariables()
Low-level, typed access to any Vectorworks program variable (application-wide or per-document preference) by numeric selector.
- GetBool|UInt8|Int8|Int16|Int32|Double|String(selector: int) -> bool?|int?|int?|int?|int?|float?|str? [s]
- SetBool|UInt8|Int8|Int16|Int32|Double|String(selector: int, value: bool|int|int|int|int|float|str) -> bool [s]

### DisplaySettings()
Display preferences.
props:
  bool: BlackAndWhiteOnly, UseLayerColors, ZoomLineThickness, BlackBackground, ShowRulers, ShowScrollBars, ShowPageBoundary, ShowPageBreaks, ShowOthersInGroup, ShowOthersInGroupGrayed, EightSelectionHandles, FullScreenCursor, NoFillBehindText, AdjustFlippedText, XRayMode, DisplayHiddenObjectsGhosted, ShowInternalOriginMarker, AllowDropShadows, PerspectiveCropped
  int: 3DConversionResolution, DisplayLightObjects, RotatedTextDisplay, DisplayBitmaps, HiddenLineShade, Display3DLoci, DefaultRenderMode, DefaultProjection
  2DConversionResolution: int  # Raw values of the corresponding preference popups.
  3DRotationResponse: int  # 1..5

### EditingSettings()
Editing and session preferences.
props:
  bool: ClickDrag, OffsetDuplicates, AssociateDimensions, AutoAssociateDimensions, CreateDimensionsInDimensionClass, WallAutoJoin, UndoViewChanges, DuplicateTagsWithObjects, OccludedPickingAndSnapping
  int: MaxUndos, AutoSaveInterval, BackupInterval, LineWeightUnit, DimensionStandard
  float: CustomMoveDistance

### SnapSettings()
Snapping (SmartCursor) preferences.
props:
  bool: SnapToGrid, SnapToObjects, SnapToLoci, SnapToEdgePoints, SnapToSelectionOnly, SnapToAngle, SnapToIntersection, SmartPoints, SnapToDistance, SmartEdge, ConstrainTangent, SnapToEndPoint, SnapToMidPoint, SnapToCenter, SnapToQuadrant, SnapToInsertionPoint, SnapToVertex, SnapToEdge, SnapToMasterPoints, SnapToRelativeAngles, SnapToAlternateCoordinateSystem, SnapToCombinedPageArea, SnapToIndividualPages, FloatingDatum, ShowSnapBox, ShowSelectionBox, UseEdgeOffset, UseProportionalDivision, UseMultipleDivisions
  int: SnapRadiusPixels
  float: SnapBoxRadius, SelectionRadius, EdgeOffsetDistance, ProportionalPercent, DivisionDistance
  SnapAngles: str  # comma separated list in degrees, e.g. "30,45,60"
  RelativeAngle: float  # radians
  AlternateCoordinateSystemAngle: float  # radians
- GetSnapToAnglesFromAxes() -> bool?  # read-only

### GridSettings()
Grid preferences.
props:
  bool: ShowGrid, PrintGrid, SnapToGrid
  float: SnapGridX, SnapGridY, ReferenceGridX, ReferenceGridY, SheetLayerSnapGridX, SheetLayerSnapGridY
  Angle: float  # radians
  AngleY: float  # radians

### StackLayersSettings()
Unified view (stack layers) preferences.
props:
  bool: Enabled, Create2DObjects, IgnoreOtherScales, RestoreViews, CenterView, ShowPageBoundary, OnlyActiveLayer2DObjects, OnlyStoryLayers

### UnitSettings(primary=True)
Primary or secondary dimension units of the active document.
props:
  str: Name, Mark, SquareUnitMark, AreaUnitName, AreaUnitMark, VolumeUnitName, VolumeUnitMark
  float: UnitsPerInch, AreaUnitsPerSquareInch, VolumeUnitsPerCubicInch
  bool: IsMetric, ShowUnitMark, LeadingZero, TrailingZeros, DisplayAsFraction, ShowThousandsSeparator
  int: DecimalDisplayPrecision, DecimalDimensionPrecision, FractionalDisplayPrecision, FractionalDimensionPrecision, SquareUnitDivision, AreaDecimalPrecision, VolumeDecimalPrecision, DocumentAngularPrecision
  AngularUnit: AngularUnit
  Style: int  # raw unit style
  DocumentAngularUnit: AngularUnit  # Document angular settings (shared by the primary and secondary...
- IsPrimary() -> bool
- IsMetric() -> bool?  # Same value as GetIsMetric(); both names remain supported.
- GetWorldUnitsPerUnit() -> float?  # Primary units only (None / False for the secondary units) read-only

### TextDefaults()
Default text settings for new text objects.
props:
  str: FontName
  TextStyleData: Style
  TextJustification: Justification
  TextVerticalAlignment: VerticalAlignment
  TextLineSpacing: LineSpacing
  Size: float  # world units
  Leading: float  # custom line spacing

### DefaultAttributes()
Default attributes for new objects (the Attributes palette with nothing selected). The SetXxxByClass() methods make the attribute follow the active class; setting an explicit value clears the corresponding by-class flag.
props:
  ObjectColors: Colors
  int: LineWeightMils, Hatch, Gradient, ImageFill, Tile
  Marker: BeginningMarker, EndMarker
  ClassAttributes: DimensionClass
  PenStyle: int  # Pen: raw pen style, same values as PenAttributes.GetStyle
  FillStyle: int  # Fill: raw fill style, same values as FillAttributes.GetStyle
  Class: ClassAttributes  # Class used for new objects and for new dimensions
- GetPenColorsByClass() -> bool?
- SetPenColorsByClass() -> bool
- GetFillColorsByClass() -> bool?
- SetFillColorsByClass() -> bool
- GetPenStyleByClass() -> bool?
- SetPenStyleByClass() -> bool
- GetLineWeightByClass() -> bool?
- SetLineWeightByClass() -> bool
- GetFillStyleByClass() -> bool?
- SetFillStyleByClass() -> bool
- GetFillTypeRaw() -> int?  # read-only
- GetPenOpacity() -> int?
- GetFillOpacity() -> int?
- SetOpacity(pen: int, fill: int) -> bool
- GetPenOpacityByClass() -> bool?
- GetFillOpacityByClass() -> bool?
- SetOpacityByClass(penByClass: bool, fillByClass: bool) -> bool
- GetMarkersByClass() -> bool?
- SetMarkersByClass() -> bool
- GetDocumentDropShadow() -> DropShadow?  # Drop shadow of the document (Document Preferences)

### LayerContents()
Object count and bounds of the top level objects of a layer.
fields: fObjectCount: int, fBounds: Rect2D?

### Layer(hLayer: Handle)  +Is
Wrapper of a layer (design or sheet layer). Constructing from a handle that is not a layer produces an invalid wrapper (IsValid() == False).
props:
  str: Name
  LayerVisibility: Visibility
  int: DPI
  Scale: float  # 1:scale
  Elevation: float  # world units
  Thickness: float  # world units
  Description: str  # sheet title
- GetHandle() -> Handle
- IsValid() -> bool
- GetType() -> LayerType?
- IsDesignLayer() -> bool
- IsSheetLayer() -> bool
- GetNext() -> Layer
- GetPrevious() -> Layer
- IsActive() -> bool
- Activate() -> bool
- GetRenderMode() -> int?  # raw render mode
- GetProjection() -> int?  # raw projection
- GetStory() -> Story  # story of the design layer; invalid when none
- GetLevelType() -> str?  # empty when none
- SetLevelType(levelType: str) -> bool  # in a story: moves the layer to that level (AssociateWithStory); "" clears it (story loses the level)
- AssociateWithStory(story: Story, levelType="") -> bool  # "" = current level type; layer moves to the level elevation; fails when another layer of the story has the type
- DetachFromStory() -> bool  # keeps its elevation; loses story and level type
- GetFirstObject() -> Handle  # Contents (top level objects)
- GetLastObject() -> Handle
- ForEachObject(callback: fn(Handle))
- GetObjects() -> [Handle]
- GetObjectCount() -> int
- GetBounds() -> Rect2D?  # bounds of the top level objects
- GetContents() -> LayerContents  # object count and bounds in one walk
- GetObjectsOf(type) -> [type]  # top level objects of the layer that are `type`

### StoryLevel()
One level of a story (a copy). fElevationOffset relative to the story; fElevation = story elevation + offset (world units).
fields: fLevelType: str, fElevationOffset: float, fElevation: float, fLayerName: str, fLayer: Layer  # fLayer invalid when the level has no layer

### StoryLevelTemplate()
A default story level (a copy); fIndex is 1-based. fLayerName is without the story affix.
fields: fIndex: int, fLevelType: str, fElevationOffset: float, fLayerName: str, fScaleFactor: float, fDefaultWallHeight: float

### Story(hStory: Handle)  +Is
A story: floor at an elevation with levels and their design layers; document data, not a drawing object (find with
doc.GetStories()/FindStory()). Changing methods record their own undo (story data, layers, bound objects); open an undo
event, but do not register stories or the layers they create. Level types and affixes compare ignoring case; names <= 63 chars.
- GetHandle() -> Handle
- IsValid() -> bool
- Create(name: str, elevation: float, affix="", isPrefix=False) -> Story [s]  # no levels; name, affix ("" counts) and elevation must be unique; invalid wrapper on failure
- GetName() -> str?
- SetName(name: str) -> bool
- GetAffix() -> str?
- SetAffix(affix: str) -> bool  # layer names do not change
- UsesPrefix() -> bool?  # inferred from layer names (not stored)
- GetElevation() -> float?
- SetElevation(elevation: float, mode=StoryElevationChangeMode.Single) -> bool  # moved stories take their layers along; fails without change on an elevation clash
- GetStoryAbove() -> Story
- GetStoryBelow() -> Story
- Delete(deleteLayers=False) -> bool  # layers stay without story unless deleteLayers
- GetLevels() -> [StoryLevel]  # sorted by elevation offset
- GetLevel(levelType: str) -> StoryLevel?
- AddLevel(levelType: str, elevationOffset: float, layerName="", createLayerIfMissing=True, scale=0.0) -> bool  # "" = no layer; existing free design layer is bound, missing one created (scale 0 = active layer scale)
- AddLevelFromTemplate(index: int) -> bool  # layer "<template layer>-<affix>"
- SetLevelElevationOffset(levelType: str, elevationOffset: float) -> bool  # moves the level layer and its objects
- RemoveLevel(levelType: str, deleteLayer=False) -> bool
- GetLayers() -> [Layer]
- GetLayerForLevelType(levelType: str) -> Layer

### Document()
Stateless facade over the active Vectorworks document. Exposes the selection, layers, stories, classes, objects, view, units, default attributes and preferences.
props:
  Layer: ActiveLayer
  VisibilityOptions: LayerOptions, ClassOptions
  ClassAttributes: ActiveClass
  ActiveSymbolDefinition: Handle  # The symbol definition currently being edited (null when not...
  UserOrigin: Point2D  # User origin: the world point that appears at (0, 0) in the user...
  ViewCenter: Point2D  # Point at the center of the current view, in world coordinates.
- IsOpen() -> bool [s]  # Whether there is currently an open, active document.
- Display() -> DisplaySettings
- Editing() -> EditingSettings
- Snapping() -> SnapSettings
- Grid() -> GridSettings
- StackLayers() -> StackLayersSettings
- PrimaryUnits() -> UnitSettings
- SecondaryUnits() -> UnitSettings
- TextDefaults() -> TextDefaults
- DefaultAttributes() -> DefaultAttributes
- GetSelectionCount() -> int  # These report the selection the way the Vectorworks editing commands see it: only the...
- HasSelection() -> bool
- GetFirstSelected() -> Handle
- GetSelection(descend=Descend.None_) -> [Handle]
- ForEachSelected(callback: fn(Handle), descend=Descend.None_)
- GetSelectionBounds() -> Rect2D?
- GetSelectionCountOnAllLayers() -> int  # Same, but over every layer of the drawing: an object stays selected when the user...
- GetSelectionOnAllLayers(descend=Descend.None_) -> [Handle]
- ForEachSelectedOnAllLayers(callback: fn(Handle), descend=Descend.None_)
- GetSelectionBoundsOnAllLayers() -> Rect2D?
- IsSelected(h: Handle) -> bool
- Select(h: Handle, select=True) -> bool
- Select(object: PrimitiveObject, select=True) -> bool
- Deselect(h: Handle) -> bool
- Select(objects: [Handle]) -> int  # adds to the selection; returns how many were selected
- SetSelection(objects: [Handle]) -> int  # replaces the selection
- SelectAll()
- DeselectAll()
- MoveSelection(offset: Vector2D) -> bool  # Operations on the selection
- RotateSelection(angle: float, center: Point2D) -> bool  # radians, counter-clockwise
- ScaleSelection(scaleX: float, scaleY: float, center: Point2D) -> bool
- DuplicateSelection(offset: Vector2D=(0,0)) -> bool
- GroupSelection() -> Handle
- DeleteSelection(useUndo=True) -> int
- SetSelectionClass(theClass: ClassAttributes, useClassAttributes=False) -> bool
- ForEachObject(what: Traverse, callback: fn(Handle), descend=Descend.None_)  # Visits every object matching 'what' (see Traverse).
- GetObjects(what: Traverse, descend=Descend.None_) -> [Handle]  # Collects every object matching 'what' (see ForEachObject).
- GetLayerContents(what: Traverse) -> {Handle: LayerContents}  # Object count and bounds of the top level objects 'what' visits, keyed by layer handle...
- GetObjectsAtPoint(pt: Point2D, radius: float, what=Traverse.Visible, descend=Descend.None_) -> [Handle]  # Collects objects whose geometry lies within 'radius' world units of 'pt' (like a click...
- GetObjectsInCriteria(criteria: str) -> [Handle]  # Collects objects matching a Vectorworks criteria string (the same syntax used by...
- GetCriteriaError(criteria: str) -> str?  # Why 'criteria' does not compile (GetObjectsInCriteria then finds nothing); None when it...
- GetObjectType(h: Handle) -> ObjectType [s]  # Object node type (kind of geometric / structural object).
- AttributesOf(h: Handle) -> ObjectAttributes [s]  # Graphical attributes (pen, fill, marker, drop shadow, class, ...) of any object.
- ClassOf(h: Handle) -> ClassAttributes [s]
- LayerOf(h: Handle) -> Layer [s]  # The layer that ultimately contains the object (walks up through groups, symbols, ......
- FindByName(name: str) -> Handle  # Object identity lookups. Return None when no object matches.
- FindByUuid(uuid: str) -> Handle
- FindByIndex(index: int) -> Handle
- GetUuid(h: Handle) -> str?  # Persistent UUID of the object, stable across save/load.
- FindLayer(name: str) -> Layer
- ForEachLayer(callback: fn(Layer))
- GetLayers() -> [Layer]
- GetLayers(type: LayerType) -> [Layer]
- CreateDesignLayer(name: str, scale=1.0) -> Layer
- CreateSheetLayer(name: str) -> Layer
- GetActiveLayerScale() -> float?
- GetStories() -> [Story]  # sorted by elevation
- FindStory(name: str) -> Story  # invalid when none
- CreateStory(name: str, elevation: float, affix="", isPrefix=False) -> Story  # = Story.Create
- GetLevelTypes() -> [str]
- AddLevelType(name: str) -> bool
- RenameLevelType(oldName: str, newName: str) -> bool  # also renames it in layers, story levels, default story levels, bound objects; Undo leaves story bounds and horizontal section viewports renamed (rename back instead)
- DeleteLevelType(name: str) -> bool  # layers and default story levels lose it; story levels keep it
- GetStoryLevelTemplates() -> [StoryLevelTemplate]  # default story levels, index order
- AddStoryLevelTemplate(levelType: str, elevationOffset: float, layerName="", scaleFactor=0.0, defaultWallHeight=0.0) -> int?  # inserted at index 1
- DeleteStoryLevelTemplate(index: int) -> bool  # 1-based
- ResetDefaultStoryLevels(deleteExisting: bool) -> bool  # adds the Vectorworks defaults; without deleteExisting they can duplicate
- FindClass(name: str) -> ClassAttributes
- CreateClass(name: str) -> ClassAttributes
- GetClasses(includeGuestClasses=False) -> [ClassAttributes]
- GetDrawingHeader() -> Handle  # Root object of the drawing. Rarely needed directly.
- GetDefaultContainer() -> Handle  # The container that receives newly created objects (the active layer, or the edited group...
- IsInsideGroup() -> bool?  # True when the user is currently editing the contents of a group (inside a "Enter Group"...
- GetEditedGroup() -> Handle  # The group currently being edited (null when not editing a group).
- GetPageBounds() -> Rect2D?  # Rectangle covering the printable pages of the drawing, in world coordinates.
- SetZoom(zoomFactor: float) -> bool  # Zoom factor: 1.0 = 100 %, 2.0 = 200 % (twice as large on screen), 0.5 = 50 %.
- IsPlanRotated() -> bool?
- GetPlanRotationAngle() -> float?  # radians, counter-clockwise
- Redraw(area: Rect2D) -> bool  # Marks the world rectangle 'area' as needing redraw.
- WorldToUnits(worldLength: float) -> float?  # Converts between the internal world units used by the API and the primary document units...
- UnitsToWorld(unitsLength: float) -> float?
- StartUndoEvent(method=UndoMethod.SwapObjects, isRevertible=False)  # Opens an undo event and selects its method (usually UndoMethod.SwapObjects); isRevertible=True lets RevertUndoEvent() take the event back (SwapObjects and ReplaceSelection only).
- NameUndoEvent(name: str)  # Names the current undo event so it appears as "Undo <name>" in the Edit menu.
- EndUndoEvent()  # Closes the current undo event now.
- RevertUndoEvent() -> bool  # Takes back the event that is being built (undoes what it recorded, removes it); use it instead of EndUndoEvent() for an event opened with isRevertible=True, otherwise nothing is reverted; False, without effect, when no event is being built.
- IsBuildingUndoEvent() -> bool  # Whether an undo event is being built (also one that Vectorworks opened for the running script).
- AddAfterSwapObject(object: Handle) -> bool  # Undo object registration - only meaningful inside an UndoMethod.SwapObjects (or...
- AddBothSwapObject(object: Handle) -> bool  # Register an object you are ABOUT TO MODIFY so Undo restores its previous state; a copy is...
- AddBeforeSwapObject(object: Handle) -> bool  # Register an object you are about to DELETE.
- AddBeforeMoveObject(object: Handle) -> bool  # BEFORE moving an object into another container (layer, group, symbol definition) with MoveToContainer
- AddAfterMoveObject(object: Handle) -> bool  # AFTER the move: Undo puts the object back; record only this pair for the moved object in the event
- As(type, h: Handle) -> type? [s]  # wrapper of class `type` (any api object class) for h; None when h is not that kind of object
- GetObjectsOf(type, what=Traverse.All, descend=Descend.None_) -> [type]  # objects that are `type` (uses type.Is)
- GetSelectionOf(type, descend=Descend.None_) -> [type]  # selected objects that are `type`

### ==== 2D objects (wrappers of drawing objects) ====

### PrimitiveObject(h: Handle)
Common base of the 2D primitive object wrappers (line, rectangle, arc, circle, polygon, polyline, locus, ...). A wrapper is a lightweight, non-owning view of a BlankHandle - copying it does not copy the object, and destroying it does not delete the object.
props:
  bool: IsLocked, IsSelected
  Name: str  # fails when the name is used by another object
  IsVisible: bool  # visible considering the class and layer visibility
- GetHandle() -> Handle
- IsValid() -> bool
- GetObjectType() -> ObjectType
- GetInternalIndex() -> int?
- GetParent() -> Handle  # layer, group, symbol definition, ...
- GetNext() -> Handle  # NextObj; null after the last object
- GetPrevious() -> Handle  # PrevObj; null before the first object
- MoveToContainer(container: Handle) -> bool  # Moves the object into a layer, group or symbol definition; records no undo (AddBeforeMoveObject / AddAfterMoveObject around it; a new object: AddAfterSwapObject); never into/out of a wall or plug-in object, nor into itself, nor a symbol instance into its own definition (also through nested symbols)
- GetFirstMember() -> Handle  # FInGroup; null for objects without members
- GetLastMember() -> Handle  # LInGroup; null for objects without members
- ForEachMember(callback: fn(Handle))  # direct members
- GetMembers() -> [Handle]  # direct members; empty for objects without members
- GetClass() -> ClassAttributes
- SetClass(theClass: ClassAttributes, useClassAttributes=False) -> bool  # Assigns the object to 'theClass'.
- Attributes() -> ObjectAttributes  # Graphical attributes (pen, fill, markers, drop shadow, ...)
- GetBounds() -> Rect2D?  # None when unavailable (including empty containers); valid point/line bounds may have zero width or height
- GetArea() -> float?  # square world units (mm squared), independent of document area/length units
- GetPerimeter() -> float?
- GetBounds3D(layerRelative=False) -> PrimitiveObject.Bounds3D?  # minimum, maximum (Point3D); any object; layerRelative=True subtracts legacy layer Z (Get3DCntr)
- GetCenter3D(layerRelative=False) -> Point3D?  # GetCenter3D(True) == VectorScript Get3DCntr
- GetSize3D() -> Point3D?  # x = width, y = height, z = depth (VectorScript Get3DInfo)
- Move(offset: Vector2D) -> bool  # Transformations (the object handle may change for some operations; the wrapper follows...
- Move(dx: float, dy: float) -> bool
- Rotate(angle: float, center: Point2D) -> bool
- Scale(scaleX: float, scaleY: float, center: Point2D) -> bool
- Mirror(axisStart: Point2D, axisEnd: Point2D) -> bool
- Reset()  # Notifies the drawing engine that the object was modified externally.
- Delete(useUndo=True) -> bool  # Deletes the object from the document; the wrapper becomes invalid.
- ConvertToPolygon(keepOriginal=False, resolution=0) -> PolygonObject  # Conversion to a new polygon / polyline object.
- ConvertToPolyline(keepOriginal=False) -> PolylineObject

Successful consuming conversions invalidate the source wrapper even when the native handle stays the same.
Failed conversions leave the source wrapper unchanged. With `keepOriginal=True`, the source remains available.
Do not keep using other wrappers referring to an object consumed by conversion.

### Locus2DObject(h: Handle)  : PrimitiveObject  +Is +Duplicate
2D locus (kLocusNode): a reference point.
props:
  Point2D: Position
  bool: ShowMasterSnapOutsideSnapBox
  MasterSnapPoint: bool  # Snap point behaviour when the locus is inside a symbol...
- Create(position: Point2D) -> Locus2DObject [s]  # Creates a locus in the active layer / current container
- DistanceTo(pt: Point2D) -> float?

### Line2DObject(h: Handle)  : PrimitiveObject  +Is +Duplicate
2D line (kLineNode): a straight segment between two points.
props:
  Point2D: StartPoint, EndPoint
  Length: float  # keeps the start point and the direction
  Angle: float  # rotates around the start point, keeps the length
- Create(start: Point2D, end: Point2D) -> Line2DObject [s]  # Creates a line in the active layer / current container
- Create(line: Line2D) -> Line2DObject [s]
- GetLine() -> Line2D?
- SetLine(line: Line2D) -> bool
- SetLine(start: Point2D, end: Point2D) -> bool
- GetMidPoint() -> Point2D?
- GetDirection() -> Vector2D?  # unit vector from start to end
- Reverse() -> bool  # swaps the start and end points
- Extend(atStart: float, atEnd: float) -> bool  # negative values trim
- OffsetParallel(distance: float) -> bool  # positive to the left of start->end
- ClosestPoint(pt: Point2D) -> Point2D?
- DistanceTo(pt: Point2D) -> float?
- Intersect(other: Line2DObject) -> Point2D?  # Intersection point with another line object (segments)

### RectangularObject  (not constructible)  : PrimitiveObject
Common base of the rectangle and the rounded rectangle wrappers. The geometry is a possibly rotated rectangle (RotatedRect2D): a corner (origin), the direction of the width side, the width and the height.
props:
  RotatedRect2D: Rect
  Width: float  # keeps the origin corner
  Height: float  # keeps the origin corner
  Center: Point2D  # moves the object
  Angle: float  # rotates around the center
- GetOrigin() -> Point2D?
- GetDirection() -> Vector2D?  # unit vector along the width side
- SetSize(width: float, height: float, keepCenter=True) -> bool
- IsAxisAligned() -> bool?
- GetCorners() -> (Point2D *4)?  # Corners, counter-clockwise starting at the origin (for positive width and height)
- SetBounds(bounds: Rect2D) -> bool  # Sets an unrotated rectangle
- Contains(pt: Point2D) -> bool
- GetPolygon() -> Polygon2D?  # the four corners (corner rounding is ignored)

### RectangleObject(h: Handle)  : RectangularObject  +Is +Duplicate
Rectangle (kBoxNode), possibly rotated.
- Create(rect: RotatedRect2D) -> RectangleObject [s]  # Creates a rectangle in the active layer / current container.
- Create(bounds: Rect2D) -> RectangleObject [s]
- Create(center: Point2D, width: float, height: float, angle=0.0) -> RectangleObject [s]
- IsSquare() -> bool?

### CornerDiameters()
Corner rounding of a rounded rectangle: the diameters of the corner ellipse along the width side (alongWidth) and along the height side (alongHeight).
fields: alongWidth: float, alongHeight: float

### RoundRectObject(h: Handle)  : RectangularObject  +Is +Duplicate
Rounded rectangle (`ObjectType.RoundedRectangle`), possibly rotated.
props:
  CornerDiameters: CornerDiameters
  CornerRadius: float  # Radius of circular corners (the average when the corners are...
- Create(rect: RotatedRect2D, corners: CornerDiameters, proportional=False) -> RoundRectObject [s]  # Creates a rounded rectangle in the active layer / current container.
- Create(bounds: Rect2D, corners: CornerDiameters, proportional=False) -> RoundRectObject [s]
- Create(center: Point2D, width: float, height: float, cornerRadius: float, angle=0.0) -> RoundRectObject [s]
- HasCircularCorners() -> bool?

### ArcObject(h: Handle)  : PrimitiveObject  +Duplicate
Circular arc (kArcNode). Angles are in radians, counter-clockwise from the X axis. The document always stores arcs counter-clockwise: a negative sweep passed to a setter is normalized, so GetSweepAngle() is always positive.
props:
  Arc2D: Arc
  Point2D: Center
  float: Radius
  StartAngle: float  # keeps the end angle
  SweepAngle: float  # keeps the start angle
  EndAngle: float  # keeps the start angle
- Is(h: Handle) -> bool [s]  # any kArcNode, including full circles
- Create(arc: Arc2D) -> ArcObject [s]  # Creates an arc in the active layer / current container. Radius and sweep must not be zero.
- Create(center: Point2D, radius: float, startAngle: float, sweepAngle: float) -> ArcObject [s]
- CreateThreePoints(start: Point2D, onArc: Point2D, end: Point2D) -> ArcObject [s]
- SetAngles(startAngle: float, sweepAngle: float) -> bool
- GetStartPoint() -> Point2D?
- GetEndPoint() -> Point2D?
- GetMidPoint() -> Point2D?
- GetChord() -> Line2D?
- GetLength() -> float?
- GetChordLength() -> float?
- GetSagitta() -> float?
- IsCircle() -> bool?
- ClosestPoint(pt: Point2D) -> Point2D?
- DistanceTo(pt: Point2D) -> float?
- Intersect(other: ArcObject) -> [Point2D]
- Intersect(line: Line2D) -> [Point2D]

### CircleObject(h: Handle)  : PrimitiveObject  +Duplicate
Circle. In the document a circle is an arc (kArcNode) with a full 360 degree sweep.
props:
  Circle2D: Circle
  Point2D: Center
  float: Radius, Diameter
- Is(h: Handle) -> bool [s]  # kArcNode with a full sweep
- Create(circle: Circle2D) -> CircleObject [s]  # Creates a circle in the active layer / current container. The radius must be positive.
- Create(center: Point2D, radius: float) -> CircleObject [s]
- CreateThreePoints(p1: Point2D, p2: Point2D, p3: Point2D) -> CircleObject [s]
- AsArc() -> ArcObject  # The same object seen as an arc
- GetCircumference() -> float?
- Contains(pt: Point2D) -> bool
- ClosestPoint(pt: Point2D) -> Point2D?
- DistanceTo(pt: Point2D) -> float?  # distance to the circumference
- PointAt(angle: float) -> Point2D?
- Intersect(other: CircleObject) -> [Point2D]
- Intersect(line: Line2D) -> [Point2D]
- GetTangentPoints(from_: Point2D) -> [Point2D]

### PolyObject  (not constructible)  : PrimitiveObject
Common base of the polygon and polyline wrappers. Vertex indices are 0-based. The visibility of a vertex is the visibility of the edge that starts at it.
Position, type, control-point and visibility queries use the same indices: 0 through GetVertexCount() - 1.
enums: BooleanOperation{Union=0,Intersection,Difference,SymmetricDifference}  # CombineShapes operation; Difference = first minus second, SymmetricDifference = both differences
props:
  bool: IsClosed, IsClockwise
- GetVertexCount() -> int
- GetVertex(index: int) -> PolyVertex?
- GetVertexPoint(index: int) -> Point2D?
- SetVertexPoint(index: int, pt: Point2D) -> bool  # keeps the vertex type
- GetVertexPoints() -> [Point2D]
- DeleteVertex(index: int) -> bool
- DeleteAllVertices() -> bool
- GetVertexVisible(index: int) -> bool?
- SetVertexVisible(index: int, visible: bool) -> bool
- SetAllVerticesVisible(visible: bool) -> bool
- GetPolygon() -> Polygon2D?
- Reverse() -> bool  # reverses the vertex order, keeps the edge visibility
- GetPolyArea() -> float?  # Measurement (the base GetArea / GetPerimeter give the same results through the generic...
- GetPolyPerimeter() -> float?
- GetCurveLength() -> float?
- GetCurveLocationAtDistance(distance: float) -> api.Math.Polygon2D.CurveLocation?
- GetCurvePointAtDistance(distance: float) -> Point2D?
- GetCurveTangentAtDistance(distance: float) -> Vector2D?
- GetCurveCurvatureAtDistance(distance: float) -> float?
- GetCurveClosestPoint(point: Point2D) -> api.Math.Polygon2D.CurveLocation?
- GetCurveDistanceTo(point: Point2D) -> float?
- DivideCurveByCount(count: int, includeEnd: bool=True) -> [Point2D]?
- Contains(pt: Point2D) -> bool  # Queries on the vertex polygon (curve vertices are treated as control points)
- ClosestPoint(pt: Point2D) -> Point2D?
- DistanceTo(pt: Point2D) -> float?
- GetCentroid() -> Point2D?
- IsConvex() -> bool?
- IsSelfIntersecting() -> bool?
- Intersect(line: Line2D) -> [Point2D]
- BooleanUnion(other: PolyObject) -> [Handle]  # CombineShapes with self as first, other as second
- BooleanIntersection(other: PolyObject) -> [Handle]
- BooleanDifference(other: PolyObject) -> [Handle]
- BooleanSymmetricDifference(other: PolyObject) -> [Handle]
- IsCombinableShape(h: Handle) -> bool [s]  # line, rectangle, rounded rectangle, oval, arc, circle, polygon, polyline; NOT freehand polygons, < 2 vertices, or a 2-vertex polyline that is not a straight segment
- AreShapesInOnePlane(first: Handle, second: Handle) -> bool [s]  # same planar ref ID, as CombineShapes requires; False for None
- AlignShapePlanes(first: Handle, second: Handle) -> bool [s]  # moves second into first's plane when coplanar (like Modify > Add/Clip/Intersect Surface); records NO undo: doc.AddBothSwapObject(both) first
- CombineShapes(operation: BooleanOperation, first: Handle, second: Handle) -> [Handle] [s]  # 2D Boolean of any two combinable shapes in one plane
2D Booleans (Core's Add/Clip/Intersect Surface engine): CombineShapes combines any two shapes that IsCombinableShape
accepts, e.g. a rectangle minus a circle; first/second take a Handle or any api wrapper (None = null, refused). The
inherited Boolean* methods do the same for polygons and polylines. CombineShapes and Boolean* never change their inputs. Results are NEW DETACHED
handles (in no container) of 2D objects of ANY type (polyline, polygon, or a copy of an input shape: a difference of
area shapes with disjoint bounding boxes returns a copy of first, a union of such shapes a copy of each, an intersection
where one shape lies inside the other that shape as polygon/polyline). Every result has first's attributes: class,
pen/fill, records, plane, selected/locked/visibility state. Wrap with PrimitiveObject(handle) (never assume
PolylineObject); insert with MoveToContainer(doc.GetDefaultContainer()) + doc.AddAfterSwapObject(handle) inside an
undo event, or delete an unwanted result with PrimitiveObject(handle).Delete(False). An empty list is SUCCESS without
a shape: intersection of non-overlapping shapes, difference whose second covers first or whose first is a line,
symmetric difference of equal shapes; a Parasolid failure looks the same. RuntimeError ONLY for invalid input: None or
a shape IsCombinableShape refuses (text, group, symbol, plug-in, 3D, freehand polygon), first is second, shapes in
different planes (a screen-plane and a layer-plane shape count as different), an unknown operation number; an invalid
wrapper counts as None. Planes: CombineShapes never changes planes; AlignShapePlanes(first, second) moves ONLY second
into first's plane like the Surface commands, keeping handles valid: if first's plane is parallel to the screen plane
(Top/Plan: screen plane, layer planes) second must be in a parallel plane and keeps its position seen along the
normal (Top/Plan: same 2D coordinates, screen plane <-> layer plane); otherwise second must lie in first's plane.
False (nothing changed) when not coplanar, e.g. a screen-plane and a layer-plane shape in a 3D view. It records NO
undo: in the undo event call doc.AddBothSwapObject(first) and (second) BEFORE it. Open shapes: Core closes an open
polygon/polyline of 3+ vertices with a straight segment and an arc with its chord (its radii when filled); a line or
2-vertex poly has no area: as second of a Difference it splits first where it crosses first completely (each piece is
a result); in other operations it gives no meaningful area.
GetCurve.../DivideCurveByCount are also inherited by PolygonObject and PolylineObject. They analyze the actual
curved outer path through temporary Core geometry, preserve inputs and insert no drawing objects. Requires an open
drawing context. Includes hidden edges and a closed path's closing edge; excludes holes. Coordinates use the
polygon's own XY plane independent of the view/working plane; lengths use world millimetres. Existing Contains,
ClosestPoint and DistanceTo keep their control-polygon behavior. See Polygon2D below for arc-distance, endpoint,
derivative and failure conventions.

### PolygonObject(h: Handle)  : PolyObject  +Is +Duplicate
Polygon (kPolygonNode, and freehand polygons kFreehandPolygonNode): corner vertices only. Use PolylineObject for curved vertices.
- Create(poly: Polygon2D) -> PolygonObject [s]  # Creates a polygon in the active layer / current container (at least two vertices).
- Create(points: [Point2D], closed=True) -> PolygonObject [s]
- Create(rect: Rect2D) -> PolygonObject [s]
- CreateRegular(center: Point2D, circumradius: float, sides: int, startAngle=0.0) -> PolygonObject [s]
- IsFreehand() -> bool?
- AddVertex(pt: Point2D, visible=True) -> bool
- InsertVertex(beforeIndex: int, pt: Point2D, visible=True) -> bool
- SetPolygon(poly: Polygon2D) -> bool  # Replaces all vertices and the closed flag (curve vertices are set as corners)
- SetVertexPoints(points: [Point2D]) -> bool  # keeps the closed flag

### PolylineObject(h: Handle)  : PolyObject  +Is +Duplicate
Polyline (kPolylineNode): a poly shape whose vertices can be corner, bezier, cubic, arc or radius vertices. Vertex points are control points; the curve passes through corner vertices only (and through arc vertices with a non-zero radius when it fits).
- Create(poly: Polygon2D) -> PolylineObject [s]  # Creates a polyline in the active layer / current container (at least two vertices).
- CreateCircle(center: Point2D, radius: float) -> PolylineObject [s]  # Closed polyline of four radius vertices that forms a circle
- CreateFilletedRect(rect: Rect2D, cornerRadius: float) -> PolylineObject [s]  # Closed polyline of a rectangle with filleted corners
- AddVertex(vertex: PolyVertex) -> bool
- AddVertex(pt: Point2D, type=VertexType.Corner, arcRadius=0.0) -> bool
- InsertVertex(beforeIndex: int, vertex: PolyVertex) -> bool
- SetVertex(index: int, vertex: PolyVertex) -> bool
- GetVertexType(index: int) -> VertexType?
- SetVertexType(index: int, type: VertexType) -> bool
- GetVertexArcRadius(index: int) -> float?  # 0 for vertices that are not arc vertices
- SetVertexArcRadius(index: int, radius: float) -> bool  # makes the vertex an arc vertex
- GetVertexMaxRadius(index: int) -> float?  # Largest radius that fits an arc vertex between its neighbours
- GetControlVertex(index: int) -> PolyVertex?  # Control vertex as stored in the document (for arc vertices the point that defines the...
- HasCurves() -> bool?
- SetPolygon(poly: Polygon2D) -> bool  # Replaces all vertices and the closed flag

### GroupObject(h: Handle)  : PrimitiveObject  +Is +Duplicate
Group (kGroupNode): a container of other objects. Members are walked with the PrimitiveObject member API.
- Create() -> GroupObject [s]  # empty group in the active layer / current container
- Create(members: [Handle]) -> GroupObject [s]  # moves members into a new group; null handles skipped
- CreateFromSelection() -> GroupObject [s]  # groups the selected objects (VectorScript Group)
- GetMemberCount() -> int?
- AddMember(h: Handle) -> bool  # moves h into the group as its last member
- Ungroup() -> bool  # members move to the group's container; the group is deleted and the wrapper becomes invalid

### ParametricObject(h: Handle)  : PrimitiveObject  +Is +Duplicate
Generic plug-in (parametric) object of any kind, script or SDK. USE ONLY WHEN NO SPECIFIC WRAPPER EXISTS (PlantObject, WindowObject, DataTagObject, ...); it reads/writes raw record fields by universal name. Call Reset() after changing parameters.
enums: PluginKind{Point=0,Linear,Rectangle,Path2D,Path3D,Custom}  # how the objects of a plug-in are placed: Path2D/Path3D with CreateFromPath, the others with Create
- IsNamed(h: Handle, universalName: str) -> bool [s]
- Create(universalName: str, location: Point2D, angle=0.0) -> ParametricObject [s]  # point-based plug-in; angle in radians; records its insertion itself: do NOT AddAfterSwapObject it
- CreateFromPath(universalName: str, hPath: Handle) -> ParametricObject [s]  # path-based plug-in; hPath itself becomes its path (no copy; for a 2D path plug-in Vectorworks converts it into a polyline); records the insertion and the change of a path in a layer itself: do NOT AddAfterSwapObject it
- GetDefinitionFormat(universalName: str) -> RecordFormat [s]  # plug-in's parametric format; invalid for unknown names; adds the format to the document if missing
- GetParameterDefinitions(universalName: str) -> [RecordField] [s]  # name, localizedName, type, defaultValue of every parameter; no instance needed
- GetDefinitionChoices(universalName: str, univParamName: str) -> [str] [s]  # universal choices of a PopUp parameter, as GetParamChoices gives them for an object; empty for unknown names and non-PopUp parameters; adds the format if missing, named as given: pass the exact universal name
- GetPluginKind(universalName: str) -> PluginKind? [s]  # EXACT universal name (case matters); None when no plug-in OBJECT has exactly that name (unknown, differently cased, menu command, tool); changes nothing
- GetParametricName() -> str?
- GetParameters() -> [RecordField]
- GetParamNames() -> [str]
- HasParam(univParamName: str) -> bool
- GetParamType(univParamName: str) -> RecordFieldType?
- GetParamChoices(univParamName: str) -> [str]  # universal choices of a PopUp parameter
- GetParamString(univParamName: str) -> str? / SetParamString(univParamName: str, value: str) -> bool  # any type, as text
- GetParamReal(univParamName: str) -> float? / SetParamReal(univParamName: str, value: float) -> bool  # Real, Dimension, CoordLocX/Y, Angle (degrees), Area, Volume
- GetParamBool(univParamName: str) -> bool? / SetParamBool(univParamName: str, value: bool) -> bool
- GetParamInt(univParamName: str) -> int? / SetParamInt(univParamName: str, value: int) -> bool  # Integer, DimStdPopUp
- GetPathObject() -> Handle  # null for point-based plug-ins

### TextObject(h: Handle)  : PrimitiveObject  +Is +Duplicate
Text block. UTF-8 text, line separator "\r" (GetNewLine()). Char indices are 0-based UTF-16 code units. Range setters take (value, first=0, count=kToEnd); count is clamped to the text end. Sizes in world units unless *Points; angles in radians.
consts: kStylePlain=0 kStyleBold=1 kStyleItalic=2 kStyleUnderline=4 kStyleOutline=8 kStyleShadow=16 (combine with |); kCustomStyleNone=0 kCustomDiagonalFraction=1 kCustomVerticalFraction=2 kCustomSuperscript=32 kCustomSubscript=64; kToEnd
enums: HorizontalAlignment{Left=1,Center,Right,Justify}  VerticalAlignment{TopBox=1,TopBaseline,CenterBox,BottomBaseline,BottomBox}  Spacing{Custom=0,Single=2,OneAndHalf=3,Double=4}  TabAlignment{Left=1,Right,Center,Decimal}
- Create(text: str, origin: Point2D, width=0.0) -> TextObject [s]  # width > 0 = fixed-width wrapping block
- CreateUnlinkedCopy() -> TextObject  # copy not linked to a record field
- GetText() -> str? / SetText(text: str, clearFormatting=False) -> bool
- GetLength() -> int?
- InsertText(text: str, beforeIndex: int) -> bool / AppendText(text: str) -> bool / DeleteText(first=0, count=kToEnd) -> bool
- GetNewLine() -> str [s]
- GetOrigin() -> Point2D? / SetOrigin(origin: Point2D) -> bool
- GetAngle() -> float? / IsFlipped() -> bool? / SetOrientation(angle: float, flipped=False) -> bool
- GetBoxCorners() -> (Point2D, Point2D, Point2D, Point2D)?  # TL, TR, BR, BL of the rotated box
- GetCharIndexAt(point: Point2D) -> int?
- Get/SetHorizontalAlignment(HorizontalAlignment) / Get/SetVerticalAlignment(VerticalAlignment)
- GetSpacing() -> Spacing? / GetLeading() -> float? / SetSpacing(spacing: Spacing, leading=0.0) -> bool  # leading > 0 required for Custom
- GetWidth() -> float? / SetWidth(width: float) -> bool / IsWrapped() -> bool? / SetWrapped(wrapped: bool) -> bool
- GetLineHeight(charIndex=0) -> float? / GetLineCount() -> int? / GetLineStarts() -> [int] / GetLines() -> [str]  # after wrapping
- GetCharWidths() -> [float]
- GetFont(charIndex=0) -> str? / GetFontIndex(charIndex=0) -> int? / GetSize(charIndex=0) -> float? / GetSizePoints(charIndex=0) -> float?
- GetStyle(charIndex=0) -> int? / GetCustomStyle(charIndex=0) -> int? / GetColor(charIndex=0) -> ColorRGB? / GetColorIndex(charIndex=0) -> int? / GetTracking(charIndex=0) -> float?
- GetStyleRuns() -> [TextObject.StyleRun]  # fields: start length font fontIndex size sizePoints style customStyle color textStyle tracking
- SetFont(fontName: str, first=0, count=kToEnd) -> bool / SetFontIndex(fontIndex: int, ...) / SetSize(size: float, ...) / SetSizePoints(points: float, ...)
- SetStyle(style: int, ...) -> bool  # replaces flags / SetCustomStyle(customStyle: int, ...) / SetColor(color: ColorRGB, ...) / SetColorIndex(color: int, ...) / SetTracking(tracking: float, ...)  # tracking 0.1..10, 1 = normal
- GetTextStyleRef() -> int? / GetTextStyleRefAt(charIndex: int) -> int? / SetTextStyleRef(textStyle: int, first=0, count=kToEnd) -> bool  # 0 = none
- IsTextStyleByClass() -> bool? / IsTextStyleByClassAt(charIndex: int) -> bool? / SetTextStyleByClass(first=0, count=kToEnd) -> bool
- UpdateTextStyleSize() -> bool  # rescales text style sizes to the layer scale
- GetTabStops() -> [TextObject.TabStop]  # fields: offset alignment / GetTabStopCount() -> int?
- AddTabStop(offset: float) -> bool / MoveTabStop(index: int, offset: float) -> bool / RemoveTabStop(index: int) -> bool  # index 0 cannot be removed
- GetRepeatingTabStop() -> float? / SetRepeatingTabStop(interval: float) -> bool  # 0 = none
- HasTightFill() -> bool? / SetTightFill(tightFill: bool) -> bool
- IsLinkedToRecord() -> bool? / UnlinkFromRecord() -> bool / IsNoteText() -> bool? / IsSIAElevationText() -> bool? / IsRightToLeft() -> bool?
- FormatAsSIA(centimeters: str, millimeters: str, superscriptPercent=100.0) -> bool / FormatValueAsSIA(value: float, alwaysMeters: bool, superscriptPercent=100.0) -> bool / FormatSegmentAsSIA(first: int, count: int, superscriptPercent=100.0) -> bool
- FontIndexFromName(fontName: str) -> int? [s] / FontNameFromIndex(fontIndex: int) -> str? [s]
- PointsToWorld(points: float) -> float [s] / WorldToPoints(length: float) -> float [s]

### ==== Attributes and classes ====

### Point2D()
fields: x: float, y: float

### ColorRGB()
RGB color with 16 bits per channel (0 .. 65535), lossless with the core color representation.
fields: red: int, green: int, blue: int
- FromRGB8(r: int, g: int, b: int) -> ColorRGB [s]
- Red8() -> int
- Green8() -> int
- Blue8() -> int

### ColorPair()
Foreground and background colors of a pen or a fill, as color indices.
fields: fore: int, back: int

### ObjectColors()
All four object colors (pen fore/back, fill fore/back), as color indices.
fields: pen: ColorPair, fill: ColorPair

### Marker()
fields:
  shape: MarkerShape
  fill: MarkerFill
  base: MarkerBase
  halfTick: MarkerHalfTick
  tail: bool
  angle: int  # degrees
  length: float  # page inches
  width: float  # page inches
  thicknessBasis: MarkerThicknessBasis
  thicknessUnits: MarkerThicknessUnits
  thickness: float  # used with MarkerThicknessBasis.Custom, in thicknessUnits
  visible: bool
- GetStyleValue() -> int  # Packed marker style value (shape | fill | base | half tick | tail).
- SetStyleValue(value: int)

### DropShadow()
fields:
  useDropShadow: bool
  units: DropShadowUnits
  offset: float
  blurRadius: float
  angle: float  # degrees
  color: int
  opacity: int

### WallTextures()
Wall textures of a class (internal indices of texture resources, 0 = none).
fields: right: int, left: int, center: int

### RoofTextures()
Roof textures of a class (internal indices of texture resources, 0 = none).
fields: top: int, edge: int, dormer: int

### AttributesBase(h: Handle)
Common base of the graphical attribute wrappers. A wrapper does not own the object; it only reads and writes attributes of the wrapped handle. Getters return an empty optional when the handle is null or the object does not support the attribute.
props:
  ObjectColors: ObjectColors  # All four colors at once (pen fore/back, fill fore/back).
- GetHandle() -> Handle
- IsValid() -> bool
- GetObjectType() -> ObjectType
- IsGroup() -> bool
- ColorIndexToRGB(index: int) -> ColorRGB [s]
- RGBToColorIndex(color: ColorRGB) -> int [s]

### PenAttributes(h: Handle)  : AttributesBase
Pen (stroke) attributes of an object: colors, style (pattern / line type), line weight, opacity, by-class flags and the line type mapping (pen space).
props:
  ColorRGB: ForeColor, BackColor
  int: ForeColorIndex, BackColorIndex, LineWeightMils, Opacity
  ColorPair: Colors
  float: LineWeightMillimeters, Scale
  bool: OpacityByClass, LocalMapping, FlipHorizontal, FlipVertical
  Style: int  # Style.
  LineType: int  # Line type internal index (positive), empty if the pen is not a...
- GetColorsByClass() -> bool?
- SetColorsByClass() -> bool
- GetStyleKind() -> PenStyleKind?
- GetNone() -> bool?
- SetNone() -> bool  # applied recursively to group members
- GetSolid() -> bool?
- SetSolid() -> bool  # applied recursively to group members
- GetStyleByClass() -> bool?
- SetStyleByClass() -> bool
- GetLineWeightByClass() -> bool?
- SetLineWeightByClass() -> bool
- IsMappingExisting() -> bool  # Line type mapping (pen space)

### FillAttributes(h: Handle)  : AttributesBase
Fill attributes of an object: colors, style (pattern / hatch / tile / gradient / image), opacity and by-class flags. The fill mapping (origin, scale, rotation ...) is in FillMappingAttributes.
props:
  ColorRGB: ForeColor, BackColor
  int: ForeColorIndex, BackColorIndex, Opacity
  ColorPair: Colors
  bool: OpacityByClass
  Style: int  # Style.
  Resource: int  # Internal index (positive) of the hatch, tile, gradient or image...
- GetColorsByClass() -> bool?
- SetColorsByClass() -> bool
- GetType() -> FillType?
- GetNone() -> bool?
- SetNone() -> bool  # applied recursively to group members
- GetSolid() -> bool?
- SetSolid() -> bool  # applied recursively to group members
- GetStyleByClass() -> bool?
- SetStyleByClass() -> bool

### FillMappingAttributes(h: Handle)  : AttributesBase
Mapping of hatch, tile, gradient and image fills (fill space): origin, axes, offsets, rotation, repeat, mirror and flip. Getters return empty when the object has no fill mapping; setters create the mapping if needed.
props:
  Point2D: IAxisEndPoint, JAxisEndPoint
  Frame: Frame
  float: YOffset, IAxisLength, JAxisLength, YOffsetInCurrentUnits, IAxisLengthInCurrentUnits, JAxisLengthInCurrentUnits
  bool: Repeat, Mirror, Flip, MaintainAspectRatio
  OriginPoint: Point2D  # Mapping frame, in world coordinates
  XOffset: float  # Offset and axis lengths, in internal units
  XOffsetInCurrentUnits: float  # Offset and axis lengths, in the document current units
  Angle: float  # Rotation of the mapping about its origin, in radians
  GeometryType: int  # Gradient geometry type (linear, radial, ...)
  LocalMapping: bool  # Local (object relative) vs. world mapping
- IsMappingExisting() -> bool

### FillMappingAttributes.Frame()
fields: origin: Point2D, iAxisEnd: Point2D, jAxisEnd: Point2D

### MarkerAttributes(h: Handle)  : AttributesBase
Beginning and end markers (arrow heads) of an object.
props:
  Marker: BeginningMarker, EndMarker
  bool: BeginningMarkerVisible, EndMarkerVisible
- GetByClass() -> bool?
- SetByClass() -> bool

### DropShadowAttributes(h: Handle)  : AttributesBase
Drop shadow of an object.
props:
  bool: Enabled, ByClass
  int: Opacity
  Data: DropShadow  # Object specific drop shadow data; empty if the object has none.
  Color: ColorRGB  # Convenience accessors on top of GetData / SetData
- DeleteData() -> bool

### ClassAttributes(hClassDefinition: Handle)  : AttributesBase
Wrapper of a class definition (kClassDefNode): a named, saved configuration of attributes.
props:
  str: Description
  bool: NonPlot, UseTextStyle
  ColorPair: PenColors, FillColors
  ColorRGB: PenForeColor, PenBackColor, FillForeColor, FillBackColor
  int: PenLineType, LineWeightMils, PenOpacity, FillResource, FillOpacity, GeneralTexture, TextStyle
  Marker: EndMarker
  WallTextures: WallTextures
  RoofTextures: RoofTextures
  Visibility: ClassVisibility  # does not redraw or reset the visibility of the objects
  UseAtCreation: bool  # Whether new objects created in this class get the class...
  ObjectColors: ObjectColors  # Colors (overrides AttributesBase to read/write the class...
  PenStyle: int  # Raw pen style, same values as PenAttributes.GetStyle.
  FillStyle: int  # Raw fill style, same values as FillAttributes.GetStyle.
  BeginningMarker: Marker  # Markers.
  DropShadow: DropShadow  # Drop shadow.
  UseTextures: bool  # Whether the class applies its textures at creation
- FromIndex(classIndex: int) -> ClassAttributes [s]
- FromName(name: str) -> ClassAttributes [s]
- OfObject(hObject: Handle) -> ClassAttributes [s]
- Create(name: str) -> ClassAttributes [s]  # returns the existing class if the name is taken
- GetNoneClass() -> ClassAttributes [s]
- GetDimensionClass() -> ClassAttributes [s]
- GetGuidesClass() -> ClassAttributes [s]  # creates it if missing
- GetDefaultClass() -> ClassAttributes [s]  # class of the current container (parametric class during a reset)
- GetActiveClass() -> ClassAttributes [s]  # active class of the document, outside the current container
- GetMaxIndex() -> int [s]
- ForEach(includeGuestClasses: bool, callback: fn(ClassAttributes)) [s]
- GetAll(includeGuestClasses: bool) -> [ClassAttributes] [s]
- GetIndex() -> int?
- GetName() -> str?
- MakeDefault() -> bool
- Delete() -> bool  # Deletes the class; its objects are moved to the None class. The wrapper becomes invalid.
- GetPenStyleKind() -> PenStyleKind?
- GetFillType() -> FillType?
- SetOpacity(opacity: int) -> bool  # Pen and fill opacity together
- AssignTo(hObject: Handle, useClassAttributes=False, descendIntoGroups=True) -> bool  # Assigns the object to this class.

### ObjectAttributes(h: Handle)  : AttributesBase
All graphical attributes of an object (the equivalent of VWFC VWObjectAttr). Geometry is intentionally not part of this API.
props:
  Opacity: int  # Combined opacity (the same for pen and fill)
- Pen() -> PenAttributes
- Fill() -> FillAttributes
- FillMapping() -> FillMappingAttributes
- Markers() -> MarkerAttributes
- DropShadow() -> DropShadowAttributes
- GetClass() -> ClassAttributes  # Class of the object
- SetClass(theClass: ClassAttributes, descendIntoGroups=True) -> bool
- SetAllByClass() -> bool  # Sets every attribute that supports it "by class": pen and fill colors and styles, line...
- GetOpacityByClass() -> bool?
- SetOpacityByClass() -> bool
- ApplyTo(target: Handle) -> bool  # Copies colors, pen and fill style, line weight, opacity, markers and drop shadow to the...

### ==== Annotation: dimensions, data tags, title block borders ====

### AnnotationObject(h: Handle)  : PrimitiveObject
Common base of the annotation plug-in object wrappers (data tag, title block border). An annotation object does not describe a piece of the building: it describes the drawing. It reads data from the objects and from the document and prints it on the sheet.
- GetParametricName() -> str?  # Universal (parametric) name of this object, "Data Tag" or "Title Block Border".
- HasParam(univParamName: str) -> bool  # Whether this plug-in object has a field with the given universal name.
- GetParamNames() -> [str]  # Ordered list of every parameter (universal) name defined by this object's plug-in.
- GetParamString|Real|Bool|Int(univParamName: str) -> str?|float?|bool?|int?  # Generic, string-keyed field accessors.
- SetParamString|Real|Bool|Int(univParamName: str, value: str|float|bool|int) -> bool
- GetStyleHandle() -> Handle  # Symbol definition of the style the object is attached to, null when the object is...
- GetStyleName() -> str?  # Name of that style resource; empty optional when the object is unstyled or the wrapper is...
- IsStyled() -> bool
- SetStyle(styleName: str) -> bool  # Attaches the object to the style resource of the current drawing named 'styleName' and...
- SetStyle(hStyleSymbolDefinition: Handle) -> bool
- RemoveStyle() -> bool  # Detaches the object from its style; every parameter becomes "by instance" and keeps its...

### DataTagObject(h: Handle)  : AnnotationObject  +Is +Duplicate
Data tag plug-in object (universal name "Data Tag").
props:
  bool: UseLeader, UseMarker, AlignToWalls
  LeaderType: LeaderType
  HorizontalPosition: HorizontalPosition
  MoveBehaviour: MoveBehaviour
  LeaderLength: float  # world units
  LeaderAngle: float  # radians
  ShoulderLength: float  # world units
  LeaderEnd: Point2D  # Tip of the leader line, in world units.
  Offset: Point2D  # Offset of the tag from the object it tags, in world units.
  UseCriteriaEligibility: bool  # Whether the tag restricts the objects it may be attached to by...
  EligibilityCriteria: str  # The Vectorworks criteria string used when the restriction is...
- Create(position: Point2D, styleName="", hObjectToTag: Handle=None) -> DataTagObject [s]  # Creates a data tag at 'position' that tags 'hObjectToTag' (which may be null for a...
- EnsureStyle(styleName="") -> str [s]  # Makes sure a data tag style named 'styleName' exists in the current drawing, importing it...
- GetTaggedObject() -> Handle  # The object this tag reads its data from; null for a tag that is not attached to anything.
- AttachTo(hObject: Handle) -> bool  # Attaches the tag to 'hObject' (replacing the current association) and refreshes the tag...
- DetachFrom(hObject: Handle=None) -> bool  # Detaches the tag from 'hObject'. Pass null to detach it from whatever it is tagging.
- CanBeTagged(hObject: Handle) -> bool [s]  # Whether 'hObject' is a kind of object a data tag may be attached to.
- GetTagsOfObject(hObject: Handle) -> [Handle] [s]  # Every data tag attached to 'hObject'.
- GetExtractedData() -> [(str, str)]  # The data the tag currently displays, as (label, value) pairs.
- Update() -> bool  # Re-reads the data from the tagged object and redraws the tag.

### TitleBlockBorderObject(h: Handle)  : AnnotationObject  +Is +Duplicate
Title block border plug-in object (universal name "Title Block Border").
props:
  float: SheetHeight
  bool: ShowGrids, DrawCropMarks, DisplayNorthArrow, DisplayDrawingStamp
  int: HorizontalZones, VerticalZones
  SheetSizeName: str  # Name of the predefined sheet size, e.g. "ANSI D" or "ISO A1".
  SheetWidth: float  # Custom sheet size, world units.
  UseAsTitleBlock: bool  # Whether the object draws the title block, or only the sheet...
  IsActiveTitleBlock: bool  # Whether this is the title block whose sheet data the document...
  NorthAngle: float  # radians
  DrawingStampText: str  # Free text printed by the stamp, used when the stamp text is set...
- Create(position: Point2D, styleName="") -> TitleBlockBorderObject [s]  # Creates a title block border with its lower left corner area at 'position'.
- EnsureStyle(styleName="") -> str [s]  # Makes sure a title block border style named 'styleName' exists in the current drawing...
- GetMarginLeft() -> float?  # Sheet margins, world units.
- GetMarginRight() -> float?
- GetMarginTop() -> float?
- GetMarginBottom() -> float?
- SetMargins(left: float, right: float, top: float, bottom: float) -> bool
- GetSheetDataFieldNames() -> [str]
- GetSheetData(fieldName: str) -> str?
- SetSheetData(fieldName: str, value: str) -> bool
- GetAllSheetData() -> [(str, str)]  # Every sheet data field of this title block as (field name, value) pairs.
- GetProjectDataFieldNames() -> [str] [s]
- GetProjectData(fieldName: str) -> str? [s]
- SetProjectData(fieldName: str, value: str) -> bool [s]
- GetAllProjectData() -> [(str, str)] [s]
- GetRevisions() -> [Revision]  # The revision history printed by this title block, oldest first.
- GetSheetID() -> str?  # Sheet identification as the title block currently prints it.
- GetSheetTitle() -> str?
- GetSheetDate() -> str?
- GetLatestIssueDate() -> str?  # Date of the most recent issue of this title block, empty when it was never issued.
- UpdateData(updateAutomaticData=True) -> bool [s]  # Re-reads the document data into every title block border of the drawing and redraws them.

### TitleBlockBorderObject.Revision()
fields: fNumber: str, fDate: str, fNote: str, fPublishDate: str, fRecipients: str

### DimensionObject(h: Handle)  : PrimitiveObject  +Duplicate
Base class of every dimension object (`ObjectType.Dimension`). A dimension is a NATIVE Vectorworks object, not a plug-in object: it has no parameter record and no object style.
props:
  Point2D: EndPoint
  bool: StartWitness, EndWitness, SecondaryBoxText, TextFlipped
  float: EndWitnessLength, EndWitnessOffset
  str: SecondaryLeaderText, SecondaryTrailerText
  int: SecondaryPrecision
  DimensionTolerance: ToleranceType
  StartPoint: Point2D  # The two points the dimension measures between.
  Offset: float  # Distance between the measured points and the dimension line...
  WitnessOverride: int  # 0 = use the dimension standard, 1 = one custom length for both...
  StartWitnessLength: float  # world units, custom override
  StartWitnessOffset: float  # world units, custom override
  ArrowsInside: bool  # True when the arrowheads point inwards (between the witness...
  LeaderLine: bool  # A leader line connects the text to the dimension line when the...
  ShowValue: bool  # Whether the measured value is printed at all.
  LeaderText: str  # printed before the value
  TrailerText: str  # printed after the value
  BoxText: bool  # draw a box around the text
  Precision: int  # Digits after the decimal point for decimal units; a power of...
  ShowSecondaryValue: bool  # Secondary (dual) unit display - the same four settings for the...
  NoteText: str  # Note text carried by the dimension, shown by some standards...
  TextPositionAutomatic: bool  # True when Vectorworks positions the text itself; False when it...
  TextInside: bool  # text between the witness lines
  TextRotation: int  # 0 = aligned with the dimension line, 1 = horizontal only, 2 =...
  TextOffsetAlongLine: float  # Distance of the text from the start point (negative) or the end...
  TextOffsetAboveLine: float  # Distance of the text above the dimension line, world units.
  FontSize: float  # points
  FontStyle: int  # Sum of 1 = bold, 2 = italic, 4 = underline.
  TextStyleName: str  # Name of the text style resource applied to the dimension text...
  TolerancePlus: float  # world units
  ToleranceMinus: float  # world units
  StandardName: str  # Name of the dimension standard the object references ("ASME"...
  StandardIndex: int  # Index of the standard: > 0 a built-in standard, < 0 a custom...
  UnitSetting: int  # 0 = use the document units; otherwise the index of a named...
- Is(h: Handle) -> bool [s]  # any dimension object
- KindOf(h: Handle) -> DimensionKind [s]  # Kind of the dimension, or Unknown when 'h' is not a dimension.
- GetKind() -> DimensionKind?
- GetKindName() -> str?
- GetKindName(kind: DimensionKind) -> str [s]
- SetPoints(start: Point2D, end: Point2D) -> bool
- GetMeasuredLength() -> float?  # Straight distance between the two measured points, in world units.
- Associate(selectedObjectsOnly=False) -> bool  # Binds the dimension to the object(s) it measures so it follows them.
- GetDimensionsOf(hObject: Handle) -> [Handle] [s]  # Objects a dimension may be bound to: the dimensions currently measuring 'hObject'.

### LinearDimensionObject(h: Handle)  : DimensionObject  +Duplicate
Linear dimension: measures the distance between two points.
props:
  DirectionAngle: float  # Only meaningful for a constrained dimension; rotates the...
- Is(h: Handle) -> bool [s]  # Any linear dimension: constrained, unconstrained or ordinate.
- CreateConstrained(start: Point2D, end: Point2D, direction: Vector2D, offset=0.0) -> LinearDimensionObject [s]  # Constrained dimension along an explicit direction.
- CreateConstrained(start: Point2D, end: Point2D, angle: float, offset=0.0) -> LinearDimensionObject [s]  # Constrained dimension whose dimension line is rotated by 'angle' radians from the X axis.
- CreateHorizontal(start: Point2D, end: Point2D, offset=0.0) -> LinearDimensionObject [s]  # Constrained dimension measuring the horizontal / vertical distance between the two points.
- CreateVertical(start: Point2D, end: Point2D, offset=0.0) -> LinearDimensionObject [s]
- CreateUnconstrained(start: Point2D, end: Point2D, offset=0.0) -> LinearDimensionObject [s]  # Unconstrained ("sloped") dimension: the dimension line follows start -> end and the value...
- CreateOrdinate(datum: Point2D, point: Point2D, direction: Vector2D, offset=0.0) -> LinearDimensionObject [s]  # Ordinate dimension: 'start' is the datum, 'end' the measured point.
- IsConstrained() -> bool?  # True for a constrained (fixed angle) dimension, False for an unconstrained one.
- GetValue() -> float?  # Value the dimension prints: the distance between the measured points, projected onto the...

### AngularDimensionObject(h: Handle)  : DimensionObject  +Is +Duplicate
Angular dimension: measures the angle between two legs meeting at a vertex.
props:
  Vertex: Point2D  # Vertex the two legs meet at.
  ReferenceAngle: bool  # Whether the dimension measures against the reference direction...
- Create(vertex: Point2D, firstLegPoint: Point2D, secondLegPoint: Point2D, offset=0.0) -> AngularDimensionObject [s]  # Angle from 'firstLegPoint' to 'secondLegPoint' around 'vertex', drawn at 'offset' world...
- Create(vertex: Point2D, startAngle: float, endAngle: float, legLength: float, offset=0.0) -> AngularDimensionObject [s]  # Same, but built from the vertex, the two leg directions (radians) and a leg length.
- CreateReferenceAngle(vertex: Point2D, firstLegPoint: Point2D, secondLegPoint: Point2D, offset=0.0) -> AngularDimensionObject [s]  # Reference angle variant: a single witness line measuring one leg against the reference...
- GetStartAngle() -> float?  # Directions of the two legs, radians from the X axis.
- GetEndAngle() -> float?
- GetValue() -> float?  # Measured angle in radians, counter-clockwise from the first leg to the second, in [0...

### ArcLengthDimensionObject(h: Handle)  : DimensionObject  +Is +Duplicate
Arc length dimension: measures the length ALONG an arc rather than the straight distance between its endpoints, which is what a linear dimension would report.
- Create(start: Point2D, end: Point2D, center: Point2D, offset=0.0, clockwise=False, witnessPerpendicularToChord=False, arcIndicator=True) -> ArcLengthDimensionObject [s]  # Measures from 'start' to 'end' along the arc around 'center'.
- Create(center: Point2D, radius: float, startAngle: float, sweepAngle: float, offset=0.0, witnessPerpendicularToChord=False, arcIndicator=True) -> ArcLengthDimensionObject [s]  # Same, expressed as an arc: centre, radius and the start / sweep angles in radians.
- GetCenter() -> Point2D?  # Centre of the measured arc.
- GetRadius() -> float?
- GetStartAngle() -> float?  # Start angle and signed sweep of the measured arc, radians.
- GetSweepAngle() -> float?
- GetValue() -> float?  # Value the dimension prints: the length along the arc, world units.
- IsClockwise() -> bool?  # Drawing options fixed at creation (read-only on the object).
- IsWitnessPerpendicularToChord() -> bool?
- HasArcIndicator() -> bool?

### RadialDimensionObject(h: Handle)  : DimensionObject  +Duplicate
Radial and diametrical dimension: measures the radius or the diameter of a circle or arc. Both kinds are built from the CENTRE of the circle and a POINT ON IT, which fixes the direction the dimension is drawn in.
props:
  float: Diameter
  Center: Point2D  # Circle the dimension measures.
  Radius: float  # keeps the centre and the direction
  Angle: float  # keeps the centre and the radius
  Compact: bool  # Short radial notation - a stub with the arrowhead instead of a...
- Is(h: Handle) -> bool [s]  # Any radial or diametrical dimension.
- CreateRadial(center: Point2D, radius: float, angle: float, offset=0.0) -> RadialDimensionObject [s]  # Radius dimension of the circle 'centre'/'radius', drawn towards 'angle' radians.
- CreateRadial(center: Point2D, pointOnCircle: Point2D, offset=0.0) -> RadialDimensionObject [s]  # Radius dimension of the circle through 'pointOnCircle' around 'center'.
- CreateDiametrical(center: Point2D, radius: float, angle: float, offset=0.0) -> RadialDimensionObject [s]  # Diameter dimension, same arguments.
- CreateDiametrical(center: Point2D, pointOnCircle: Point2D, offset=0.0) -> RadialDimensionObject [s]
- IsDiametrical() -> bool?  # True when the dimension prints the diameter, False when it prints the radius.
- GetValue() -> float?  # Value the dimension prints: the diameter for a diametrical dimension, the radius...

### CenterMarkObject(h: Handle)  : PrimitiveObject  +Duplicate
Center mark: the cross that marks the centre of a circle or an arc. Unlike every other object in this group a center mark is NOT a dimension object.
- Is(h: Handle) -> bool [s]  # Conservatively False: native marks have no verified persistent discriminator.
- Create(center: Point2D, radius=0.0) -> CenterMarkObject [s]  # Center mark for the circle 'center'/'radius', sized from the active dimension standard.
- CreateFor(hObject: Handle) -> CenterMarkObject [s]  # Center mark for an existing circle, arc, oval or any other object - the mark is placed at...
- CreateWithSizes(center: Point2D, radius: float, spokeLength: float, gap: float, extension: float) -> CenterMarkObject [s]  # Center mark with explicit world lengths: 'spokeLength' is the length of one spoke of the...
- GetCenter() -> Point2D?  # Centre of the cross.
- GetSegmentCount() -> int?  # Number of line segments the mark is made of: 2 for a bare cross, up to 6 with extensions.

### ==== Architecture: walls, slabs, roofs, windows, doors, columns, stairs ====

### ArchitectObject(h: Handle)  : PrimitiveObject
Common base of the Architect object wrappers (wall, slab, roof, window, door, column, stair).
- GetParametricName() -> str?  # Universal (parametric) name of the object, e.g. "Slab", "Window", "Door", "Column2", "Stairs CW".
- HasParam(univParamName: str) -> bool  # Whether this plug-in object has a field with the given universal name.
- GetParamNames() -> [str]  # Ordered list of every parameter (universal) name defined by this object's plug-in.
- GetParamString|Real|Bool|Int(univParamName: str) -> str?|float?|bool?|int?  # Generic, string-keyed field accessors.
- SetParamString|Real|Bool|Int(univParamName: str, value: str|float|bool|int) -> bool
- GetPluginStyleName() -> str?  # name of the plug-in style (door/window/column/stair style) of the object; None when unstyled
- IsParamSetByStyle(univParamName: str) -> bool  # the plug-in style sets the parameter (by style or catalog): a value written on the object does not last; Door/Window typed setters return False for it

### WallObject(h: Handle)  : ArchitectObject  +Is +Duplicate
Wall (kWallNode) - a straight or curved wall that can host windows, doors and other wall inserts.
props:
  Caps: Caps
- Create(start: Point2D, end: Point2D, thickness=0.0) -> WallObject [s]  # Creates a straight wall between 'start' and 'end' in the active layer / current container.
- CreateRound(start: Point2D, onArc: Point2D, end: Point2D, thickness=0.0) -> WallObject [s]  # Creates a curved wall through the three given points (start, a point on the arc, end).
- GetLine() -> Line2D?  # Line from the wall's start to its end. Empty for a curved wall.
- SetLine(start: Point2D, end: Point2D) -> bool
- GetStartPoint() -> Point2D?
- GetEndPoint() -> Point2D?
- GetLength() -> float?  # world units, straight-line length
- GetAngle() -> float?  # radians, direction from start to end
- SetThickness(thickness: float) -> bool  # Thickness (world units). Setting the thickness detaches the wall from its wall style.
- GetHeights() -> Heights?
- SetHeights(heights: Heights) -> bool
- SetHeights(startTop: float, startBottom: float, endTop: float, endBottom: float) -> bool
- GetHeightBound(isTop: bool) -> HeightBound
- SetHeightBounds(bottomBound: HeightBound, topBound: HeightBound) -> bool  # binds both ends and moves the heights; fails when a bound does not exist for the wall or top <= bottom; no own undo (AddBothSwapObject first)
- SetHeightBound(isTop: bool, bound: HeightBound) -> bool  # one end; the other keeps its bound
- GetAverageHeight() -> float?
- GetStyle() -> int?  # Wall style (kWallStyleNode resource). 0 = un-styled (freehand thickness / components).
- SetStyle(wallStyle: int, selectedOffset=0.0, replacingOffset=0.0) -> bool
- IsCurtainWall() -> bool?  # Curtain wall flag (a wall used as the framing of a curtain-wall system).
- SetIsCurtainWall(isCurtainWall: bool) -> bool

### WallObject.Heights()
Heights (world units) relative to the layer plane (0 = top of layer, negative = below). A wall can be tapered by using different start / end heights.
fields: startTop: float, startBottom: float, endTop: float, endBottom: float

### WallObject.HeightBound()
Bound of the wall bottom or top. Setters use fKind, fRelativeStory (Story: -1 below, 0 the wall layer's story, 1 above), fLevelType (Story) and fOffset (world units); fStatus and fElevation (world Z when Valid) are results.
fields: fStatus: BoundStatus, fKind: BoundKind, fRelativeStory: int, fLevelType: str, fOffset: float, fElevation: float?

### WallObject.Caps()
End caps.
fields:
  leftCap: bool  # close the start end
  rightCap: bool  # close the end end
  round: bool  # cap style is rounded

### SlabObject(h: Handle)  : ArchitectObject  +Is +Duplicate
Slab (kSlabNode) - a horizontal element (floor, roof deck, ceiling deck, ...) defined by a 2D boundary profile and vertically extruded by its thickness.
props:
  Height: float  # Height / elevation of the slab's bottom face, in world units.
  Style: int  # Slab style (kSlabStyle resource); 0 = un-styled.
- Create(hProfile: Handle) -> SlabObject [s]  # Creates a slab whose boundary is the given 2D profile (polygon or polyline).
- AddModifier(hProfile: Handle, isSubtract: bool, componentID=-1, clipToBoundary=True) -> bool  # Adds a modifier (a 2D profile) to the slab.

### RoofObject(h: Handle)  : ArchitectObject  +Is +Duplicate
Roof (kRoofContainerNode) - a polygonal roof defined by a list of edges. Each edge has an insertion point, a slope, a projection (eave overhang) and an eave height. Roof accessories (attic, soffit, fascia) can be inserted around the perimeter.
props:
  Attributes: Attributes
- Create(generateGableWalls: bool, bearingInset: float, roofThickness: float, miterType: MiterType, verticalMiter: float) -> RoofObject [s]  # Creates a new roof object, with no attic, soffit or fascia (SetAccessories adds them).
- SetAccessories(accessories: Accessories) -> bool
- GetEdgeCount() -> int?  # count of edges / vertices
- GetEdge(index: int) -> Edge?  # 0-based index
- SetEdge(index: int, edge: Edge) -> bool  # resets the roof: a slope outside 2..90 degrees opens a MODAL alert
- AppendEdge(edge: Edge) -> bool  # no reset: Reset() after the last edge
- RemoveEdge(index: int) -> bool

### RoofObject.Attributes()
Roof-wide attributes.
fields: generateGableWalls: bool, bearingInset: float, roofThickness: float, miterType: MiterType, verticalMiter: float

### RoofObject.Accessories()
Roof accessories along the perimeter.
fields:
  insertAttic: bool
  insertSoffit: bool
  insertFascia: bool
  fasciaWidth: float  # world units
  fasciaHeight: float
  atticHeight: float
  recess: float
  rakeThickness: float
  trimDepth: float

### RoofObject.Edge()
Roof edges (polygon vertex + per-edge slope and overhang).
fields:
  insertionPoint: Point2D
  slope: float  # degrees; Vectorworks builds a roof only when every edge slope is 2..90 (check before SetEdge / Reset)
  projection: float  # world units - eave overhang
  eaveHeight: float  # world units

### WindowObject(h: Handle)  : ArchitectObject  +Is +Duplicate
Window plug-in object (universal name "Window") from the Architectural Objects plug-in. A window inserts into a host wall (kWallNode) at a specific position along the wall and at an elevation.
Width/Height are the size the Object Info palette shows, measured as SizeReference ("Sash Opening" | "Unit Size" | "Rough Opening") says; Reset() computes the unit size OverallWidth/OverallHeight from them. Heights are above the layer plane (also in a wall: not above the wall bottom).
props:
  float: Width, Height  # setters: False without writing for a value <= 0 or a parameter the plug-in style sets (IsParamSetByStyle)
  SizeReference: str  # popup only: the stored size is measured in the new reference at the next reset; set Width/Height after it
  float: OverallWidth, OverallHeight  # unit size of the last reset; setters write the Width/Height that give it for Unit Size and Sash Opening (height: no transom), else False
  Elevation: float  # raw palette value: head or sill height, as GetElevationSetAt() says
  float: JambWidth, JambDepth
  str: TopShape, SillStyle, IDLabel, Description
  bool: IncludeSill, OnSchedule
  SashOperation: str  # Legacy: stored as "SashOperation"; superseded by...
- GetElevationSetAt() -> str?  # "Head of Window" | "Sill of Window": which height Elevation holds
- GetSillHeight() -> float?  # Elevation - Height (Head of Window) or Elevation (Sill of Window)
- SetSillHeight(value: float) -> bool  # writes Elevation for the current ElevationSetAt with the current Height: set the height first
- GetHeadHeight() -> float?  # Elevation (Head of Window) or Elevation + Height (Sill of Window)
- Create(position: Point2D) -> WindowObject [s]  # Creates a window at 'position'. Typically inserted into a wall via WallObject afterwards.
- GetConfiguration() -> str?
- GetCasementOperation() -> str?
- GetFixedGlassOperation() -> str?
- GetHungOperation() -> str?
- GetInteriorSide() -> str?
- GetFlipped() -> bool?
- GetHingeDirection() -> bool?
- GetShow3DOpen() -> bool?
- GetOpenAngle() -> float?
- GetAwningOpenDirection() -> str?  # Sash hinge and open-direction parameters (popups; see the sash operation table in...
- GetCasementHingeSide() -> str?
- GetCasementOpenDirection() -> str?
- GetHopperOpenDirection() -> str?
- GetTiltTurnHingeSide() -> str?
- GetTiltTurnOpenDirection() -> str?
- GetVerticalPivotOpensOutToward() -> str?

### DoorObject(h: Handle)  : ArchitectObject  +Is +Duplicate
Door plug-in object (universal name "Door") from the Architectural Objects plug-in. A door inserts into a host wall (kWallNode). It carries frame / leaf / jamb / lintel / threshold / trim / side-light / vision-panel / muntin parameters.
Width/Height are the size the Object Info palette shows, measured as SizeReference ("Leaf Size" | "Unit Size" | "Rough Opening") says (earlier builds read the leaf size there); Reset() computes the leaf size from them.
props:
  float: Width, Height  # setters: False without writing for a value <= 0 or a parameter the plug-in style sets (IsParamSetByStyle)
  SizeReference: str  # popup only: the stored size is measured in the new reference at the next reset; set Width/Height after it
  Thickness: float  # leaf thickness
  str: TopShape, LeafType, IDLabel
  bool: OnSchedule
  Config: str  # Legacy "Config" parameter; GetConfiguration() reads the...
- GetLeafWidth() -> float?  # leaf size ("DoorWidth") computed at the last reset
- GetLeafHeight() -> float?  # ("DoorHeight")
- Create(position: Point2D) -> DoorObject [s]  # Creates a door at 'position'. Typically inserted into a wall via WallObject afterwards.
- GetConfiguration() -> str?
- GetSwingDirection() -> str?  # Opening (leaf swing; SwingOperation, SwingDirection and SwingHingeSide apply to the...
- GetSwingHingeSide() -> str?
- GetInteriorSide() -> str?
- GetIsFlipped() -> bool?
- GetOpenAngle() -> float?
- GetSwingOperation() -> str?
- GetOperation() -> str?  # Legacy: stored as "Operation"; superseded by GetSwingOperation()
- Get3DOpen() -> bool?

### ColumnObject(h: Handle)  : ArchitectObject  +Is +Duplicate
Column plug-in object - the Vectorworks column, universal name "Column2" (Is() also accepts the legacy "Column" plug-in object). A column is a vertical structural element with a shaft (rectangular or round), an optional base and an optional cap.
props:
  float: ShaftDepth
  TotalHeight: float  # Overall height (world units); unavailable for composite columns.
  ShaftWidth: float  # Rectangular shaft (world units)
  ShaftDiameter: float  # Round shaft (world units)
  Shape: str  # Native ShaftType value; use the plug-in's supported universal choices.
- Create(position: Point2D) -> ColumnObject [s]  # Creates a Column at 'position' in the active layer / current container.

### StairObject(h: Handle)  : ArchitectObject  +Is +Duplicate
Stair plug-in object - the Vectorworks stair, universal name "Stairs CW". A stair carries the overall rise / run, tread and riser dimensions, a configuration (straight, L-shaped, U-shaped, spiral, ...), and optional handrails / stringers.
props:
  float: TotalRise, StairWidth, TreadDepth, RiserHeight
  int: NumTreads, NumRisers
  str: Configuration
  bool: HandrailLeft, HandrailRight
  TotalRun: float  # Overall geometry (world units)
- Create(position: Point2D) -> StairObject [s]  # Creates a Stair at 'position' in the active layer / current container.

### ==== Landscape (Landmark plug-in objects) ====

### LandmarkObject(h: Handle)  : PrimitiveObject
Common base of the Landmark plug-in object wrappers (plant, landscape area, site model, site modifier, stake, hardscape, property line, existing tree).
- GetParametricName() -> str?  # Universal (parametric) name of this object, e.g. "Plant" or "Hardscape".
- HasParam(univParamName: str) -> bool  # Whether this plug-in object has a field with the given universal name.
- GetParamNames() -> [str]  # Ordered list of every parameter (universal) name defined by this object's plug-in.
- GetParamType(univParamName: str) -> RecordFieldType?  # Data type of the parameter; None when the parameter does not exist.
- GetParamString|Real|Bool|Int(univParamName: str) -> str?|float?|bool?|int?  # Generic, string-keyed field accessors.
- SetParamString|Real|Bool|Int(univParamName: str, value: str|float|bool|int) -> bool
- GetPathObject() -> Handle  # Path object of a path-based plug-in object (hardscape, landscape area, site modifier...

### PlantObject(h: Handle)  : LandmarkObject  +Is +Duplicate
Plant plug-in object (universal name "Plant") from the Landmark plug-in.
props:
  str: LatinName, CommonName, Comments
  Config: Config
  TagDisplay: TagDisplay
  bool: Show3DDetail
  PlantStyle: str  # Imports 'styleName' if needed, applies all of its settings to...
  PlantID: str  # resource name of the plant symbol / style
  PlantDescription: str  # Name of the plant style symbol definition; prefer...
  Spread: float  # Size (world units) canopy diameter
  Height: float  # plant height
  Spacing: float  # Distance between plants along a poly edge or in an array...
- Create(position: Point2D, plantResourceName="") -> PlantObject [s]  # Creates a single-instance plant at 'position' in the active layer / current container.
- CreateFromPath(hPath: Handle, plantResourceName="") -> PlantObject [s]  # Creates a poly-based plant that distributes instances along/over an existing 2D path...
- EnsurePlantStyle(styleName="") -> str [s]  # Makes sure a plant style is available in the current drawing, importing it from the...

### LandscapeAreaObject(h: Handle)  : LandmarkObject  +Is +Duplicate
Landscape area plug-in object (universal name "Landscape Area") from the Landmark plug-in. A landscape area is a path-based container that fills a 2D polygonal region with one or more plant species distributed by percentage.
props:
  str: ID, Description
  DrawingMode: DrawingMode
  AreaUnits: AreaUnits
  Name: str  # "name" (softscape name), not the object name
  PlantDisplay2D: PlantDisplay2D
  ShowPlantsIn2D: bool  # Any non-None display; setting True selects PlantSymbols.
- CreateFromPath(hPath: Handle) -> LandscapeAreaObject [s]  # Creates a landscape area from an existing 2D path object (typically a polygon or...
- GetArea() -> float?  # Measurements (read-only; computed by the object during its reset) area of the region in...
- GetProjectedArea() -> float?  # projected onto the site model (0 when there is none)
- GetNumPlants() -> int?  # total number of plant instances distributed

### SiteModelObject(h: Handle)  : LandmarkObject  +Is +Duplicate
Site model plug-in object (universal name "DTM6") from the Landmark plug-in. A site model is a triangulated irregular network (TIN) surface built from source data (survey points, contour lines, boundary polygons, ...).
props:
  Display2D: 2DDisplay
  Display3D: 3DDisplay
  str: 3DStyle
  bool: ShowErrors
  2DStyle: str  # Raw display style values (see the Landmark documentation for...
  GeometryZReference: float  # Reference elevation (world units) used by contour-based...
- Create(position: Point2D) -> SiteModelObject [s]  # Site models are typically created interactively through the Landmark commands (survey...
- GetProjectedAreaExisting() -> str?  # Read-only area and volume readouts (formatted string; empty when not computed).
- GetSurfaceAreaExisting() -> str?
- GetSurfaceAreaProposed() -> str?
- GetVolumeExisting() -> str?
- GetVolumeProposed() -> str?
- GetCutVolume() -> str?
- GetFillVolume() -> str?

### SiteModifierObject(h: Handle)  : LandmarkObject  +Is +Duplicate
Site modifier plug-in object (universal name "Site Modifiers"), the modern SiteModifierEx2 implementation from the Landmark plug-in. A site modifier is a path-based object that reshapes a site model surface.
props:
  Config: Config
  ApplyTo: ApplyTo
  bool: Show3D, RetainSlopeInside
  float: SimplificationTolerance
- CreateFromPath(hPath: Handle) -> SiteModifierObject [s]  # Creates a site modifier from an existing 2D path object (polygon or polyline).

### StakeObject(h: Handle)  : LandmarkObject  +Is +Duplicate
Stake plug-in object (universal name "Stake Object") from the Landmark plug-in. A stake is a labeled 2D point placed at a specific location and elevation.
props:
  Mode: Mode
  SiteModel: SiteModel
  int: ID
  str: IDPrefix, IDSuffix
  bool: DisplayLeaderLine, ShowElevationMark
  ZValue: float  # elevation, in world units
  Data: str  # free-form description shown on the label
  LabelReference: str  # What the stake's label displays (ID / Elevation / Description /...
- Create(position: Point2D, zValue=0.0) -> StakeObject [s]  # Creates a stake at 'position' in the active layer / current container.

### HardscapeObject(h: Handle)  : LandmarkObject  +Is +Duplicate
Hardscape plug-in object (universal name "Hardscape") from the Landmark plug-in. A hardscape is a path-based object that represents a paved surface (walkway, patio, driveway, ...). It can be a boundary hardscape or a pathway hardscape (constant-width strip along the path).
props:
  str: ID
  Mode3D: 3DMode
  bool: Draw3D, IsSiteModifier, IsPathway, UseBorder
  float: BorderThickness, BorderWidth, PathwayOffset
  SlabThickness: float  # Sizes (world units)
  PathwayWidth: float  # isPathway = True
- CreateFromPath(hPath: Handle) -> HardscapeObject [s]  # Creates a hardscape from an existing 2D path object (polygon or polyline).
- GetMainArea() -> float?  # Measurements (read-only, computed at reset)
- GetBorderArea() -> float?
- GetFootprintArea() -> float?
- GetPerimeter() -> float?
- GetMainPerimeter() -> float?
- GetBorderPerimeter() -> float?

### PropertyLineObject(h: Handle)  : LandmarkObject  +Is +Duplicate
Property line plug-in object (universal name "Property Line") from the Landmark plug-in. A property line represents a legal parcel boundary as a closed 2D path.
props:
  str: Name, Number
  bool: ShowName, ShowNumber, ShowArea
  AreaUnits: AreaUnitsImperial, AreaUnitsMetric
  DistanceUnits: str  # Native Annotation Units popup (see the plug-in for supported values).
- CreateFromPath(hPath: Handle) -> PropertyLineObject [s]  # Creates a property line from an existing 2D path object (a closed polygon or polyline).
- GetAreaText() -> str?  # Formatted, read-only measurements.
- GetPerimeterText() -> str?

### ExistingTreeObject(h: Handle)  : LandmarkObject  +Is +Duplicate
Existing tree plug-in object (universal name "Existing Tree") from the Landmark plug-in. An existing tree represents a single tree already present on site.
props:
  str: BotanicalName, CommonName, Notes
  Origin: Origin
  float: CanopyDiameter, CriticalRootZoneDiameter, PrimaryRootZoneDiameter
  TreeProtection: TreeProtectionZone
  Condition: Condition
  SULE: SULE
  Significance: Significance
  Action: ActionComment
  bool: Create3D
  TreeNumber: str  # tag / instance identifier
  Height: float  # Size (world units) overall height
  Caliper: float  # DBH: diameter at breast height
  RootBallDiameter: float  # Root zones (world units)
  Location: str  # free-form location description
- Create(position: Point2D) -> ExistingTreeObject [s]  # Creates an existing tree at 'position' in the active layer / current container.

### ==== Spotlight (lighting devices and GDTF fixture types) ====

```python
doc = api.Document()
doc.StartUndoEvent(); doc.NameUndoEvent("Add Robin Spiider")
try:
    imported = api.GDTFLibrary.Import(r"C:\Fixtures\Robe_Lighting@Robin_Spiider.gdtf")   # never asks; keeps an existing type
    if not imported.isValidFile:
        raise RuntimeError("not a GDTF file")
    modes = [e for e in api.GDTFLibrary.GetAvailable()
             if e.isInDocument and e.fixtureName.startswith("Robin Spiider")]
    device = api.LightingDeviceObject.Create((0, 0))
    if device:
        doc.AddAfterSwapObject(device.GetHandle())              # right after creation, before any step can fail
        if modes and device.SetGDTF(modes[0].gdtfName, "Mode 2 - Basic"):   # mode "" = first mode
            device.SetUseGDTFGeometry(True)
            device.SetInstrumentType("Robin Spiider")
        device.Reset()                                          # REQUIRED after the changes
finally:
    doc.EndUndoEvent()
```
- Requires the Spotlight and GDTF plug-ins (`GDTFLibrary.IsAvailable()`).
- `GetAvailable()` lists one entry per DMX mode: fixture types imported into the drawing first (`isInDocument`), then the
  .gdtf files of the Spotlight GDTF folders, which Spotlight reads once per session.
- `SetGDTF` only accepts fixture types in the drawing (`isInDocument`, named "<Manufacturer>@<Fixture>.gdtf"); otherwise
  it returns False and leaves the device unchanged. Import a file first with `Import`.
- `Import` records its own undo for a new fixture type (do not call `AddAfterSwapObject` on it). `replaceExisting=True`
  changes an existing type in place without an undo record.
- `SetGDTF` applies the fixture type as dropping a GDTF on the device in the Resource Manager does (mode, footprint).

### LightingDeviceObject(h: Handle)  : ParametricObject  +Is +Duplicate
Lighting device plug-in object (universal name "Lighting Device") from the Spotlight plug-in. Graphics come from a
lighting device symbol ("Symbol Name") and/or a GDTF fixture type ("GDTF Fixture Name" with "UseGDTFGeometry").
Other parameters: "Device Type", "Purpose", "Position", "Unit Number", "Channel", "Universe", "DMX Address", "Color",
"Wattage", "Weight", "Field Angle", "Beam Angle", "Focus", "User Field 1".."User Field 6" (multi-cell devices: first cell).
props:
  InstrumentType: str  # "Inst Type"
  UseGDTFGeometry: bool  # draw the 3D model of the GDTF fixture type
- Create(position: Point2D, angle=0.0) -> LightingDeviceObject [s]  # A device without a lighting device symbol; angle in radians.
- GetSymbolName() -> str?  # Lighting device symbol; empty for a device without one (symbols are assigned in Spotlight).
- GetGDTFName() -> str?  # GDTF name of the fixture type, empty when the device has none.
- GetGDTFMode() -> str?  # DMX mode, without the GDTF name the plug-in appends ("<mode>.<gdtfName>").
- GetDMXFootprint() -> int?  # "Num Channels"
- SetGDTF(gdtfName: str, mode="") -> bool  # Fixture type in the drawing only; False (device unchanged) otherwise. Call Reset() afterwards.

### GDTFLibrary()
The GDTF fixture types available to Spotlight and the import of .gdtf files. Stateless; all methods are static.
- IsAvailable() -> bool [s]  # Whether the GDTF support of Spotlight is installed.
- GetAvailable() -> [GDTFLibrary.Entry] [s]  # One entry per DMX mode; imported fixture types first.
- Import(filePath: str, replaceExisting=False) -> GDTFLibrary.ImportResult [s]  # Never asks the user. A type with the same GDTF type ID in the drawing is replaced only with replaceExisting (in place, not undoable). A new type records its own undo.

### GDTFLibrary.Entry()
fields:
  gdtfName: str  # pass to LightingDeviceObject.SetGDTF (entries with isInDocument)
  fixtureName: str  # fixture type name, "@<revision>" appended when the file has one
  manufacturer: str
  mode: str  # DMX mode name
  footprint: int  # DMX channels of the mode
  symbolDefinition: Handle  # GDTF symbol definition; null for a file that is not imported
  isInDocument: bool

### GDTFLibrary.ImportResult()
fields: symbolDefinition: Handle, gdtfName: str, isImported: bool, isValidFile: bool
`isValidFile=False` when the file could not be read as GDTF. `isImported=False` with `isValidFile=True` when the fixture
type is already in the drawing and was kept (null handle; find it with `GetAvailable`).

### ==== ConnectCAD (devices, sockets and device types) ====

```python
description = json.dumps(device)          # ONE device object (see connectcad.md); never the array of devices
check = api.ConnectCADLibrary.ValidateDevice(description)       # errors: FUSE/BUS sockets, LOOP+X, unknown signal ...
doc = api.Document()
doc.StartUndoEvent(); doc.NameUndoEvent("Add device")
try:
    created = api.ConnectCADDeviceObject.CreateFromJSON(description, (0, 0))   # nothing created on errors; own undo
    if created.device:
        device = api.ConnectCADDeviceObject(created.device)
        deviceType = device.CreateDeviceType(description)        # symbol "<make> <model>" keeps pinout, extra_data
finally:
    doc.EndUndoEvent()
```
- Requires the ConnectCAD plug-in and licence (`ConnectCADLibrary.IsAvailable()`).
- Socket types IN, OUT, IO; LOOP = IN "<name>" + OUT "<name>_LP", IOloop = IO + IO "_LP"; FUSE / BUS are not sockets.
  Orientations L, R, X; loops only L / R. qty 1..50 -> "<name> 1".."<name> n". Signals / connectors from
  `GetSignals()` / `GetConnectors()`; a pinout lists the connector pins with pinIDs unique in the device.
- Required: name, tag, make, model, width_r, is_modular, n_slots. A rack device height is whole rack units
  (n x 44.45 mm); `n_slots` > 0 only when `is_modular`.
- Devices keep name, tag, make, model, sizes, power, weight; category, pinout, extra_data, uuid and source only live in
  the device type. `AddSocket` adds IN / OUT / IO on L / R only; register the device (`AddBothSwapObject`) first.

### ConnectCADDeviceObject(h: Handle)  : ParametricObject  +Is +Duplicate
ConnectCAD schematic device (universal name "Device") with socket objects in its profile group.
- CreateFromJSON(deviceJson: str, position: Point2D) -> ConnectCADDeviceObject.CreateResult [s]  # device, errors, warnings
- GetDeviceName|GetTag|GetDescription|GetMake|GetModel() -> str?
- GetRackWidth() -> str?  # non-rack | half-rack | full-rack
- GetRackUnits() -> str?  # "---" when not whole rack units
- IsModular() -> bool?; GetSlotCount() -> int?
- GetSockets() -> [ConnectCADSocketObject]
- AddSocket(name: str, type: str, signal: str, connector: str, orientation: str) -> ConnectCADDeviceObject.AddSocketResult  # socket, errors; type IN/OUT/IO, orientation L/R
- CreateDeviceType(deviceJson="") -> ConnectCADDeviceObject.DeviceTypeResult  # symbolDefinition, name, isCreated, isFullDataStored, errors, warnings

### ConnectCADSocketObject(h: Handle)  : ParametricObject  +Is +Duplicate
ConnectCAD socket (universal name "Socket"). Setters validate and regenerate the socket and its device.
- GetDevice() -> Handle
- GetSocketName() -> str?; SetSocketName(name: str) -> bool  # unique in the device, no '+', not ending in _LP; loop sockets cannot be renamed
- GetTag() -> str?
- GetSocketType() -> str?; SetSocketType(type: str) -> bool  # IN | OUT | IO
- GetSignal() -> str?; SetSignal(signal: str) -> bool
- GetConnector() -> str?; SetConnector(connector: str) -> bool
- GetOrientation() -> str?  # L | R | X, fixed at creation
- IsLoopOutput() -> bool

### ConnectCADLibrary()
ConnectCAD signal and connector types, validation, Device Definition record. Stateless; all methods are static.
- IsAvailable() -> bool [s]
- GetSignals() -> [ConnectCADLibrary.Signal] [s]  # name, category, description, defaultConnector, connectors
- GetConnectors() -> [ConnectCADLibrary.Connector] [s]  # name, localizedName, category, pins
- ValidateDevice(deviceJson: str) -> ConnectCADLibrary.Validation [s]  # errors, warnings, isValid
- GetDeviceDefinition(symbolDefinition: Handle) -> ConnectCADLibrary.DeviceDefinition [s]  # symbolDefinition, category, type, make, model, rackMounting, slotCount, socketGroups (JSON)

### ==== Resources (Resource Manager) ====

### Resource(hResource: Handle)
Wrapper of one resource, identified by its handle. Like every wrapper of this API it is a lightweight, non-owning view: copying it does not copy the resource and destroying it does not delete the resource.
props:
  str: Description
  Name: str  # Renames the resource; fails when another object already uses...
- Is(h: Handle) -> bool [s]  # True when the handle is a resource of one of the ResourceType kinds.
- TypeOf(h: Handle) -> ResourceType [s]
- GetTypeName(type: ResourceType) -> str [s]  # Stable, lowerCamelCase name of a resource type ("symbolDefinition", "hatch", "texture"...
- GetTypeFromName(typeName: str) -> ResourceType [s]  # Parses a type name produced by GetTypeName (case insensitive).
- GetAllTypes() -> [ResourceType] [s]  # Every resource type this API understands, in the order shown above.
- FromName(name: str) -> Resource [s]  # Resource of the current drawing with that name; invalid when there is none.
- FromIndex(index: int) -> Resource [s]  # Resource with that internal index (hatch / gradient / tile / image / line type / texture...
- GetHandle() -> Handle
- IsValid() -> bool
- GetResourceType() -> ResourceType
- GetObjectType() -> ObjectType
- GetResourceTypeName() -> str
- GetInternalIndex() -> int?
- GetUuid() -> str?  # Persistent UUID of the resource, stable across sessions.
- GetFolder() -> Handle  # Folder resource containing this resource, null when it sits at the top level of the...
- GetFolderName() -> str?
- MoveToFolder(hFolder: Handle) -> bool  # Moves the resource into 'hFolder' (a ResourceType.Folder resource).
- IsContainer() -> bool  # True for resources that contain other objects: symbol definitions and resource folders.
- GetContents() -> [Handle]  # Objects inside the resource (the geometry of a symbol definition, the resources of a...
- GetContentCount() -> int
- ForEachContent(callback: fn(Handle))
- Attributes() -> ObjectAttributes  # Graphical attributes, for the resource kinds that carry them.
- Duplicate() -> Resource  # Copy of the resource in the same document and folder; invalid on failure.
- Delete(useUndo=True) -> bool  # Deletes the resource from the document; the wrapper becomes invalid.

### ResourceList() | (type: ResourceType)
A list of resources of one kind, coming from the current drawing or from external content. Move-only: it owns the underlying Vectorworks resource list and disposes it on destruction.
constants: kNotFound=2**64-1
- BuildFromDocument(type: ResourceType, sort=True) -> bool  # Resources of 'type' defined in the current drawing.
- BuildFromFolder(type: ResourceType, folder: ContentFolder, subFolder="", includeDocument=False, sort=True) -> bool  # Resources of 'type' in a standard Vectorworks content folder (the external / default...
- BuildFromFolderIndex(type: ResourceType, folderIndex: int, subFolder="", sort=True) -> bool  # Same, for a folder specifier that ContentFolder does not name.
- BuildFromFile(type: ResourceType, filePath: str) -> bool  # Resources of 'type' inside one Vectorworks file, given by its full native path.
- BuildFromOpenDocument(type: ResourceType, openDocumentIndex: int, sort=True) -> bool  # Resources of 'type' of another currently open document (see the Vectorworks open files...
- FromDocument(type: ResourceType, sort=True) -> ResourceList [s]  # Factory equivalents of the Build... methods.
- FromFolder(type: ResourceType, folder: ContentFolder, subFolder="", includeDocument=False, sort=True) -> ResourceList [s]
- FromFolderIndex(type: ResourceType, folderIndex: int, subFolder="", sort=True) -> ResourceList [s]
- FromFile(type: ResourceType, filePath: str) -> ResourceList [s]
- FromOpenDocument(type: ResourceType, openDocumentIndex: int, sort=True) -> ResourceList [s]
- Dispose()  # Releases the underlying Vectorworks resource list. Called automatically by the destructor.
- IsValid() -> bool
- GetListID() -> int  # Raw Vectorworks resource list id, for the low level calls that still need it.
- GetResourceType() -> ResourceType
- GetContentFolderName(folder: ContentFolder) -> str [s]  # Stable, lowerCamelCase name of a content folder ("hatches", "textures", "objectStyles"...
- GetContentFolderFromName(folderName: str) -> ContentFolder [s]  # Parses a name produced by GetContentFolderName (case insensitive); ContentFolder.None_ when it does not...
- GetAllContentFolders() -> [ContentFolder] [s]
- GetCount() -> int
- IsEmpty() -> bool
- GetResource(index: int) -> Resource  # Resource at 'index'; invalid while the entry is external content that was not imported...
- GetName(index: int) -> str?  # Name as shown in the Resource Manager (for external content it can carry the source file...
- GetActualName(index: int) -> str?  # Real name of the resource, the one it gets when it is imported.
- GetFolderName(index: int) -> str?  # Name of the resource folder the entry belongs to, empty at the top level.
- IsInDocument(index: int) -> bool  # Whether the resource already exists in the current drawing.
- GetEntry(index: int) -> Entry?
- GetEntries() -> [Entry]
- ForEach(callback: fn(Entry))
- Find(name: str) -> int  # Index of the entry whose actual name - or, failing that, whose displayed name - is 'name'.
- Contains(name: str) -> bool
- Import(index: int, onConflict=ImportConflict.Rename) -> Resource  # Copies the resource into the current drawing and returns it.
- Import(name: str, onConflict=ImportConflict.Rename) -> Resource
- ImportWithResult(index: int, onConflict=ImportConflict.Rename) -> ResourceList.ImportResult
- SetClassRenamePrefix(prefix: str)  # Prefix added to the names of the classes that come with an imported resource.
- GetClassRenamePrefix() -> str
- Add(hResource: Handle) -> int  # Adds a resource of the current drawing to the list; returns its index or kNotFound.
- Remove(index: int) -> bool  # Removes the entry from the list. The resource itself is not deleted.

### ResourceList.Entry()
One entry of the list.
fields:
  index: int  # 0-based index in this list
  name: str  # name as shown in the Resource Manager
  actualName: str  # real resource name (without the disambiguating file name)
  folderName: str  # parent folder of the resource, empty at the top level
  handle: Handle  # null while the resource is not in the current drawing
  isInDocument: bool  # False for external content that still has to be imported

### ResourceList.ImportResult()
fields: handle: Handle, isImported: bool
`isImported=False` when an existing document resource is returned. A null handle indicates failure.
Native import registers its own undo: do not also call `AddAfterSwapObject` on the returned resource.

### TypedResource  (not constructible)  : Resource
Resource wrapper restricted to one ResourceType. Everything Resource offers - name, description, folder, duplicate, delete - is available on the typed wrappers as well.
- GetExpectedType() -> ResourceType  # Resource type this wrapper is restricted to.

### HatchLevel()
One line family of a hatch. Parallel lines start at `startPoint + n * offsetVector` and run along `repeatVector`.
fields:
  startPoint: Point2D  # origin of the line family
  repeatVector: Point2D  # line direction and dash repeat length
  dashFactor: float  # drawn fraction of each repeat (0..1; 1 = solid)
  offsetVector: Point2D  # step from one parallel line to the next
  color: ColorRGB  # pen color of the lines
  lineWeightMils: int  # pen weight in mils (1/1000 inch)

### Hatch(h: Handle)  : TypedResource  +Is
Vector hatch fill (kHatchDefNode): line families repeated over the filled area, without an artificial eight-family cap.
props:
  bool: RotateInSymbols
  UsePageUnits: bool  # True when the hatch is measured on the printed page instead of...
  Transparent: bool  # True when the area behind the hatch lines stays transparent...
  RotateInWalls: bool  # Whether the hatch follows the rotation of the wall / symbol it...
- FromName(name: str) -> Hatch [s]
- FromIndex(index: int) -> Hatch [s]
- Create(name: str, usePageUnits=False, transparent=True, backgroundColor: ColorRGB=ColorRGB()) -> Hatch [s]  # Creates an empty hatch. A number is appended to 'name' when it is already taken.
- GetLevelCount() -> int
- GetLevel(index: int) -> HatchLevel?
- GetLevels() -> [HatchLevel]
- SetLevel(index: int, level: HatchLevel) -> bool  # Replaces the level at 'index'; appending is allowed at index == GetLevelCount().
- AddLevel(level: HatchLevel) -> bool

### GradientSegment()
One color stop of a gradient. 'spotPosition' is where the color sits (0 .. 1 across the gradient) and 'midpointPosition' is where the blend with the next stop is half done (0 .. 1 between the two stops).
fields:
  spotPosition: float
  midpointPosition: float
  color: ColorRGB
  opacity: int  # 0 = fully transparent, 100 = opaque

### Gradient(h: Handle)  : TypedResource  +Is
Gradient fill (kGradientDefNode): a blend between two or more color stops.
- FromName(name: str) -> Gradient [s]
- FromIndex(index: int) -> Gradient [s]
- Create(name: str) -> Gradient [s]  # Creates a gradient with the default two stops.
- GetSegmentCount() -> int
- GetSegment(index: int) -> GradientSegment?
- GetSegments() -> [GradientSegment]
- SetSegment(index: int, segment: GradientSegment) -> bool  # Native sorting may change the stop's index.
- InsertSegment(segment: GradientSegment) -> int?  # Zero-based inserted index, including append; None on failure.
- RemoveSegment(index: int) -> bool

### Tile(h: Handle)  : TypedResource  +Is
Tile fill (kTileDefNode): a group of 2D objects repeated over the filled area on a grid.
props:
  Point2D: Repetition
  bool: TransparentBackground, RotateInWalls, RotateInSymbols
  ColorRGB: BackgroundColor
  Offset: Point2D  # Origin of the tile grid and the step from one repetition to the...
  UsePageUnits: bool  # True when the tile is measured on the printed page instead of...
- FromName(name: str) -> Tile [s]
- FromIndex(index: int) -> Tile [s]
- Create(name: str) -> Tile [s]  # Creates an empty tile. A number is appended to a name that is already taken.
- GetGeometryGroup() -> Handle  # Group holding the 2D objects the tile repeats; add geometry to it with AddGeometry.
- GetGeometry() -> [Handle]
- AddGeometry(hObject: Handle) -> bool  # Moves an existing 2D object into the tile.

### ImageFill(h: Handle)  : TypedResource  +Is
Image resource (kImageDefNode): a bitmap used as an image fill, as an image prop or as a texture image.
props:
  Compression: Compression
- FromName(name: str) -> ImageFill [s]
- FromIndex(index: int) -> ImageFill [s]
- GetWidthPixels() -> int?
- GetHeightPixels() -> int?
- CreateFromPngData(pngData: bytes) -> ImageFill [s]

### LineType(h: Handle)  : TypedResource  +Is
Line type resource. There are two kinds: simple - a dash pattern: alternating line and gap lengths (see GetDashPattern). complex - a group of 2D objects repeated along the line (see GetGeometry).
props:
  GapSize: float  # Gap between two repetitions of the geometry, in world units (or...
  UsePageUnits: bool  # True when the line type is measured on the printed page instead...
- FromName(name: str) -> LineType [s]
- FromIndex(index: int) -> LineType [s]
- CreateSimple(dashPattern: [float], scaleWithLineWeight=False) -> LineType [s]  # Finds or creates a simple line type with that dash pattern: alternating line and gap...
- CreateComplex(name: str) -> LineType [s]  # Creates an empty complex line type; add the repeated 2D objects with AddGeometry.
- IsSimple() -> bool?
- IsComplex() -> bool?
- GetDashPattern() -> [float]  # Alternating line and gap lengths; empty for a complex line type.
- GetScaleWithLineWeight() -> bool?
- GetGeometryGroup() -> Handle  # Group holding the 2D objects repeated along the line; null for a simple line type.
- GetGeometry() -> [Handle]
- AddGeometry(hObject: Handle) -> bool  # Moves an existing 2D object into the line type.

### RecordField()
One field of a record format.
fields:
  name: str  # universal (non-localized) name, the one APIs use
  localizedName: str  # name shown in the user interface
  type: RecordFieldType
  defaultValue: str  # value new records start with, as text

### RecordFormat(h: Handle)  : TypedResource  +Is
Record format. Attaching it to an object creates a record - a set of values for these fields - on that object; see Document for reading and writing the values of an attached record.
constants: kNotFound=2**64-1
props:
  str: LocalizedName
  Visible: bool  # Hidden formats do not show up in the data pane of the Object...
- FromName(name: str) -> RecordFormat [s]
- FromIndex(index: int) -> RecordFormat [s]
- Create(name: str) -> RecordFormat [s]  # Creates an empty record format; returns the existing one when the name is already taken.
- IsInternalName(name: str) -> bool [s]  # True for names reserved for internal record formats: "NNA_" or "__NNA" prefix...
- GetFieldTypeName(type: RecordFieldType) -> str [s]  # Stable, lowerCamelCase name of a field type ("integer", "text", "popUp", ...).
- GetFieldTypeFromName(typeName: str) -> RecordFieldType [s]
- GetAllFieldTypes() -> [RecordFieldType] [s]
- IsParametric() -> bool?  # A parametric format belongs to a plug-in object and must not be edited.
- GetFieldCount() -> int
- GetField(index: int) -> RecordField?
- GetFields() -> [RecordField]
- FindField(fieldName: str) -> int
- HasField(fieldName: str) -> bool
- AddField(name: str, type: RecordFieldType, defaultValue="", updateExistingRecords=True) -> int  # Final default is supplied before propagating to existing records.
- RemoveField(fieldName: str) -> bool
- RenameField(index: int, name: str) -> bool
- GetFieldDefaultValue(fieldName: str) -> str?  # Default value of a field, as text.
- SetFieldDefaultValue(fieldName: str, value: str) -> bool
- GetFieldChoices(fieldName: str) -> [str]  # Choices offered by a PopUp field, in order.
- SetFieldChoices(fieldName: str, choices: [str]) -> bool  # Replaces the choices of a PopUp field.

### Texture(h: Handle)  : TypedResource  +Is
Texture (kTextureNode): color, reflectivity, transparency and bump of a rendered surface.
props:
  Size: float  # Real world size the texture image covers, in world units.
- FromName(name: str) -> Texture [s]
- FromIndex(index: int) -> Texture [s]
- Create(name: str) -> Texture [s]  # Creates an empty texture. A number is appended to a name that is already taken.
- GetUVAspectRatio() -> float?  # Ratio between the U and the V extent of the texture image.
- ApplyToObject(hObject: Handle, part=Part.Overall) -> bool  # Assigns the texture to an object (or to one of its parts).
- UpdateThumbnail() -> bool  # Refreshes the Resource Manager preview after the texture changed.

### RenderStyle(h: Handle)  : TypedResource  +Is
Render style (kRenderStyleNode): a saved configuration of the rendering settings, applied to a viewport or to a layer.
- FromName(name: str) -> RenderStyle [s]
- FromIndex(index: int) -> RenderStyle [s]

### RenderBackground(h: Handle)  : TypedResource  +Is
Renderworks background (kRenderBackgroundNode): what a rendering shows behind the model.
- FromName(name: str) -> RenderBackground [s]
- FromIndex(index: int) -> RenderBackground [s]
- Create(name: str, kind: Kind) -> RenderBackground [s]  # Creates a background of that kind. A number is appended to a name that is already taken.

### TextStyle(h: Handle)  : TypedResource  +Is
Text style (kTextStyleNode): font, size and text attributes applied to text objects and dimensions.
- FromName(name: str) -> TextStyle [s]
- FromIndex(index: int) -> TextStyle [s]
- Create(name: str) -> TextStyle [s]  # Creates a text style; returns the existing one when the name is already taken.
- ApplyToObject(hObject: Handle) -> bool  # Applies the style to a text object (or to any object that carries text attributes).
- OfObject(hObject: Handle) -> TextStyle [s]  # Text style an object follows; invalid when the object uses its own text attributes.

### WallStyle(h: Handle)  : TypedResource  +Is
Wall style (kWallStyleNode): the components, thickness and attributes of a wall.
- FromName(name: str) -> WallStyle [s]
- FromIndex(index: int) -> WallStyle [s]
- Create(name: str) -> WallStyle [s]  # Creates a wall style; returns the existing one when the name is already taken.
- ApplyToObject(hWall: Handle, selectedOffset=0.0, replacingOffset=0.0) -> bool  # Applies the style to a wall.
- OfObject(hWall: Handle) -> WallStyle [s]

### SlabStyle(h: Handle)  : TypedResource  +Is
Slab style (kSlabStyleNode): the components and attributes of a slab.
- FromName(name: str) -> SlabStyle [s]
- FromIndex(index: int) -> SlabStyle [s]
- Create(name: str) -> SlabStyle [s]  # Creates a slab style; returns the existing one when the name is already taken.
- ApplyToObject(hSlab: Handle) -> bool
- OfObject(hSlab: Handle) -> SlabStyle [s]

### RoofStyle(h: Handle)  : TypedResource  +Is
Roof style (kRoofStyleNode): the components and attributes of a roof.
- FromName(name: str) -> RoofStyle [s]
- FromIndex(index: int) -> RoofStyle [s]
- Create(name: str) -> RoofStyle [s]  # Creates a roof style; returns the existing one when the name is already taken.
- ApplyToObject(hRoof: Handle) -> bool
- OfObject(hRoof: Handle) -> RoofStyle [s]

### ViewportStyle(h: Handle)  : TypedResource  +Is
Viewport style (kViewportStyleNode): the saved settings of a sheet layer viewport.
- FromName(name: str) -> ViewportStyle [s]
- FromIndex(index: int) -> ViewportStyle [s]
- ApplyToObject(hViewport: Handle) -> bool
- OfObject(hViewport: Handle) -> ViewportStyle [s]

### BuildingMaterial(h: Handle)  : TypedResource  +Is
Material (building material, kBuildingMaterialNode): the physical material of a wall, slab or roof component. It carries the attributes and the data (fire rating, thermal values, ...) of that material.
- FromName(name: str) -> BuildingMaterial [s]
- FromIndex(index: int) -> BuildingMaterial [s]

### DataVisualization(h: Handle)  : TypedResource  +Is
Data visualization (kDataVisualizationNode): a rule that overrides the graphic attributes of the objects matching a criteria, applied to a viewport or to the design layers. The core identifies data visualizations by name, so this wrapper works with names.
- FromName(name: str) -> DataVisualization [s]
- GetAllNames() -> [str] [s]  # Names of every data visualization of the current document.
- Rename(oldName: str, newName: str) -> bool [s]
- DeleteByName(name: str) -> bool [s]
- GetActiveOn(hObject: Handle) -> [str] [s]  # Names of the data visualizations active on an object (a viewport, a saved view or a...
- Activate(hObject: Handle, name: str, activate: bool) -> bool [s]  # Turns a data visualization on or off for that object.
- SetObjectExcluded(hObject: Handle, exclude: bool) -> bool [s]  # Keeps an object out of every data visualization.

### ResourceFolder(h: Handle)  : TypedResource  +Is
Resource folder (kFolderNode): groups resources of one kind in the Resource Manager.
- FromName(name: str) -> ResourceFolder [s]
- Create(name: str, forType: ResourceType) -> ResourceFolder [s]  # Creates a folder for resources of that kind.
- CreatePath(folderPath: str, forType: ResourceType) -> ResourceFolder [s]  # Creates a chain of nested folders from a path such as "Doors/Interior"; returns the...
- CreatePathFolders(folderPath: str, forType: ResourceType) -> ResourceFolderPath [s]
- GetContentType() -> ResourceType?  # Kind of resource the folder holds.
- GetResources() -> [Handle]  # Resources inside the folder.
- Add(hResource: Handle) -> bool  # Moves a resource into this folder.

### ResourceFolderPath()
fields: folders: [Handle], createdFolders: [Handle]
Both lists are outermost first. Path creation reuses matching folders of the same type under the same parent.
Name/type/parent conflicts fail with empty lists and remove newly created folders. Empty path components are skipped.
Creation registers no undo: within an undo event, register only `createdFolders[0]` when nonempty, never reused folders.
The outermost new folder's insertion registration includes its new descendants; registering descendants again is invalid.

### SymbolDefinition(h: Handle)  : TypedResource  +Is
Symbol definition. Its contents are the objects the symbol draws; every instance in the drawing shows the same contents, so editing them updates every instance at once.
props:
  InsertMode: InsertMode
  BreakMode: BreakMode
  PageBased: bool  # Page based symbols keep their size on the printed page instead...
  InsertAsGroup: bool  # True when inserting the symbol drops a copy of its contents...
- FromName(name: str) -> SymbolDefinition [s]
- FromIndex(index: int) -> SymbolDefinition [s]
- Create(name: str) -> SymbolDefinition [s]  # Creates an empty symbol definition.
- GetActive() -> SymbolDefinition [s]  # Symbol definition new symbol instances are created from.
- SetActive() -> bool
- GetGeometryType() -> GeometryType?
- CanInsertIntoWalls() -> bool?  # True when the symbol may be inserted into a wall (it has a wall insertion point).
- ContainsLight() -> bool?
- GetGeometry() -> [Handle]  # The objects the symbol draws (same as Resource.GetContents).
- AddGeometry(hObject: Handle) -> bool  # Moves an existing object into the symbol definition.
- ResetInstances() -> bool  # Redraws every instance after the contents changed.
- Insert(position: Point2D, rotationRadians=0.0) -> Handle  # Creates a symbol instance at 'position' in the active layer / current container; null on...

### WorksheetObject(h: Handle) : TypedResource

Non-owning worksheet RESOURCE, never its placed drawing image; not AnnotationObject/PrimitiveObject.
Shared identity/name/folder/metadata/delete come from Resource. Existing Worksheet remains unchanged and
can wrap the same handle. Create fails on ANY occupied name, unlike Worksheet.Create's reuse behavior.
Indices and inclusive Range endpoints are native 1-based, including database subrows (unlike 0-based geometry).
Signed 16-bit integers; Python overflow is rejected. Core size limits 4094 rows, 256 columns.
Getters -> None for invalid input; bool setters -> False; factories -> falsy wrapper; image absence -> null handle.
Definitions/formulas/criteria UTF-8, no wrapper parser/rewrite. GetCellFormula includes literals.
Core can normalize expressions; criteria read/write/read roundtrip uses full native definition, e.g.
"=DATABASE(ALL)"; "" converts to spreadsheet. Invalid criteria can convert the row to spreadsheet, not
transactional. Merged cells block conversion. Spreadsheet criteria/subrow count None; empty database count 0.
Numeric getters return None for nonnumeric/error/invalid cells; never silently zero. Text is formatted/displayed.
Recalculate after drawing changes or batched edits. Void Core setters report validated dispatch, NOT
successful formula evaluation. Native bool structure/merge errors propagate.

- Is(h: Handle) -> bool [s]
- FromName(name: str) -> WorksheetObject [s]
- Create(name: str, rows: int=20, columns: int=10) -> WorksheetObject [s]
- Duplicate() -> WorksheetObject
- GetRowCount() -> int?
- GetColumnCount() -> int?
- IsValidCell(row: int, column: int) -> bool
- IsValidRange(range: WorksheetObject.Range) -> bool
- InsertRows(beforeRow: int, count: int=1) -> bool
- InsertColumns(beforeColumn: int, count: int=1) -> bool
- DeleteRows(startRow: int, count: int=1) -> bool
- DeleteColumns(startColumn: int, count: int=1) -> bool
- GetCellFormula(row: int, column: int) -> str?
- SetCellFormula(row: int, column: int, formula: str) -> bool
- SetRangeFormula(range: WorksheetObject.Range, formula: str) -> bool
- GetCellText(row: int, column: int) -> str?
- GetCellValue(row: int, column: int) -> float?
- ClearCells(range: WorksheetObject.Range) -> bool
- IsDatabaseRow(row: int) -> bool?
- GetDatabaseCriteria(row: int) -> str?
- SetDatabaseCriteria(row: int, criteria: str) -> bool
- GetSubrowCount(row: int) -> int?
- GetSubrowCellText(row: int, column: int, subrow: int) -> str?
- GetSubrowCellValue(row: int, column: int, subrow: int) -> float?
- GetColumnWidth(column: int) -> int?
- SetColumnWidth(firstColumn: int, lastColumn: int, width: int) -> bool
- GetRowHeight(row: int) -> int?
- GetRowHeightLocked(row: int) -> bool?
- SetRowHeight(firstRow: int, lastRow: int, height: int, lockHeight: bool=True, includeSubrows: bool=False) -> bool
- AutoFitRowHeights(firstRow: int, lastRow: int) -> bool
- GetSubrowHeight(row: int, subrow: int) -> int?
- GetCellNumberFormat(row: int, column: int) -> WorksheetObject.NumberFormat?
- SetNumberFormat(range: WorksheetObject.Range, format: WorksheetObject.NumberFormat) -> bool
- GetCellTextFormat(row: int, column: int) -> WorksheetObject.TextFormat?
- SetTextFormat(range: WorksheetObject.Range, format: WorksheetObject.TextFormat) -> bool
- GetCellFill(row: int, column: int) -> WorksheetObject.Fill?
- SetFill(range: WorksheetObject.Range, fill: WorksheetObject.Fill) -> bool
- GetCellBorders(row: int, column: int) -> WorksheetObject.Borders?
- SetBorders(range: WorksheetObject.Range, borders: WorksheetObject.Borders) -> bool
- GetMergedCellRange(row: int, column: int) -> WorksheetObject.Range?
- MergeCells(range: WorksheetObject.Range) -> bool
- UnmergeCells(range: WorksheetObject.Range) -> bool
- Recalculate() -> bool
- GetAutoRecalculate() -> bool?
- SetAutoRecalculate(enabled: bool) -> bool
- CreateImage(topLeftCorner: Point2D) -> Handle
- GetImage() -> Handle
- FromImage(image: Handle) -> WorksheetObject [s]

Insertion at current size+1 appends; deletion leaves >=1 row/column. Width/height are positive worksheet
PIXELS, not world units; CreateImage placement is world XY. GetImage returns first associated image,
not all images. CreateImage repositions first existing image on its layer, or creates one on the active
layer if absent; it does NOT always create another image. FromImage rejects non-images; WorksheetObject(image) is invalid.

### WorksheetObject.Range()
Writable value fields: firstRow: int=1, firstColumn: int=1, lastRow: int=1, lastColumn: int=1.

### WorksheetObject.NumberFormat()
Writable fields: style: int=0, accuracy: int=2, leader: str="", trailer: str="".
Native number style codes: 0 general, 1 decimal, 2 decimal with commas, 3 scientific, 4 fractional,
5 dimension, 6 angle, 7 date, 8 conditional, 9 general fraction, 10 dimension with divider, 11 area,
12 volume, 13 text, 14 percentage. Accuracy native format-dependent 0..127, not always decimal places.

### WorksheetObject.TextFormat()
Writable fields: fontIndex: int=0, size: int=12, style: int=0, alignment: int=0,
verticalAlignment: int=0, angle: int=0, color: int=0, wrap: bool=False.
Document font index, point size, style bits (1 bold/2 italic/4 underline), horizontal 0 general/1 left/2 center/3 right,
vertical 0 general/1 top/3 center/5 bottom. Angle native DEGREES, not geometry radians.
Color unsigned 16-bit document ColorRef INDEX, not RGB. Read-modify-write to preserve font/other fields.

### WorksheetObject.Fill()
Writable fields: style: int=0, background: int=0, foreground: int=0, pattern: int=0.
Style 0 none/1 solid/2 pattern. Colors unsigned 16-bit document ColorRef indices; pattern only used for style 2.
Core can normalize unused fill fields/font indices.

### WorksheetObject.Borders()
Writable bool fields, all False: top, left, bottom, right, outline, insideHorizontal, insideVertical.
Getter fills four sides only; application flags stay False. No border weight/style/color API in this wrapper.
All five records are owned copies, default construct then set fields; range setters replace all record fields,
not partial patches. No automatic document mutation when editing a returned record.
See [worksheet reference and undo-safe example](ObjectsAnnotation.md#worksheetobject).
Verification: static signature/registration and Python syntax checks only; application and C++ builds unrun.

### WorksheetCell()
A worksheet cell. Rows and columns are 1 based, like the row numbers and the column letters shown to the user; column 1 is "A".
fields: row: int, column: int

### WorksheetCellContent()
One cell with its content.
fields:
  cell: WorksheetCell
  formula: str  # what the cell was given; empty for a cell that holds a literal
  text: str  # what the cell shows after the last recalculation

### Worksheet(h: Handle)  : TypedResource  +Is
Worksheet. A worksheet is a resource, and it may also be placed on a layer as a worksheet image.
- FromName(name: str) -> Worksheet [s]
- FromIndex(index: int) -> Worksheet [s]
- Create(name: str, rows=20, columns=10) -> Worksheet [s]  # Creates an empty worksheet; returns the existing one when the name is already taken.
- GetRowCount() -> int?
- GetColumnCount() -> int?
- IsValidCell(cell: WorksheetCell) -> bool
- GetCellFormula(cell: WorksheetCell) -> str?  # Formula of a cell; a cell holding a literal value returns an empty string.
- SetCellFormula(cell: WorksheetCell, formula: str) -> bool  # Assigns a formula (for example "=COUNT(ALL)") or a literal to one cell, or to every cell...
- SetRangeFormula(topLeft: WorksheetCell, bottomRight: WorksheetCell, formula: str) -> bool
- GetCellText(cell: WorksheetCell) -> str?  # Text the cell currently shows. Call Recalculate first when the drawing changed.
- GetCellValue(cell: WorksheetCell) -> float?  # Numeric value of a cell; empty when the cell does not hold a number.
- GetCells(topLeft: WorksheetCell, bottomRight: WorksheetCell) -> [WorksheetCellContent]  # Reads a rectangular block of cells, row by row.
- ClearCells(topLeft: WorksheetCell, bottomRight: WorksheetCell) -> bool
- InsertRows(beforeRow: int, count=1) -> bool
- InsertColumns(beforeColumn: int, count=1) -> bool
- DeleteRows(startRow: int, count=1) -> bool
- DeleteColumns(startColumn: int, count=1) -> bool
- Recalculate() -> bool  # Reevaluates every formula. Do this after the drawing changed and before reading cell text.
- CreateImage(topLeftCorner: Point2D) -> Handle  # Places the worksheet on the active layer so that it can be seen in the drawing; returns...

### ==== Tools (tool palette, Tool bar (mode bar), driving the active tool) ====

### Point3D()
3D point in world coordinates (the API counterpart of the core WorldPt3).
fields: x: float, y: float, z: float

### ViewPoint()
Point in view coordinates, in pixels (the API counterpart of the core ViewPt; ViewCoord is 16 bit).
fields: x: int, y: int

### ViewSize()
Size of the active view pane in pixels.
fields: fWidth: int, fHeight: int

### ToolPoint()
One point entered into the active tool, as the tool receives it (gSDK->GetToolPt2D / GetToolPt3D / GetToolPtViewPoint).
fields:
  fPoint2D: Point2D  # screen plane point for 2D tools (rotated with the plan), working plane point for 3D tools
  fPoint3D: Point3D  # model point
  fViewPoint: ViewPoint  # view position of the click

### ModeButtonDefinition()
A mode button as declared by a tool (static information, available without activating the tool). Only tools that declare their Tool bar buttons provide these.
fields: fName: str, fHelpText: str, fKind: ModeButtonKind

### Tool()
Description of one tool.
fields:
  fUniversalName: str  # unique identity; pass it to ActivateTool / FindTool
  fName: str  # user friendly English name (equals fUniversalName for plug-in tools)
  fDisplayName: str  # localized name shown in the tool palette
  fCategory: str  # plug-in category (empty for most built-in tools)
  fHelpText: str  # short description of the tool
  fShortcut: str  # keyboard shortcut in the current workspace (may be empty)
  fKind: ToolKind
  fCreationType: ToolCreationType
  fIsInWorkspace: bool  # placed in a tool palette of the current workspace
  fCanActivate: bool  # ActivateTool can activate it now
  fIsActive: bool  # currently the active tool
  fModeButtons: [ModeButtonDefinition]  # declared mode buttons (see ModeButtonDefinition)

### ModeChoice()
One choice of a mode group: a radio button, the single button of a Button/Toggle group, or an item of a PullDown / ComboBox / SearchablePullDown group.
fields:
  fName: str  # mode name or item text (may be empty for unnamed buttons of built-in tools)
  fHelpText: str  # tooltip text (buttons only)
  fImage: str  # image resource specifier (buttons only), e.g. "Vectorworks/ModeViewBar/Options.png"
  fId: str  # item id (SearchablePullDown only)

### ToolMode()
Live state of one mode group of the active tool.
fields:
  fIndex: int  # position on the Tool bar; SDK group number is fIndex + 1
  fType: ModeType
  fIsEnabled: bool
  fLabel: str  # label of the control, or the mode name for unlabelled buttons
  fChoices: [ModeChoice]  # see ModeChoice; empty for EditText and ResourcePopup
  fChoiceCount: int  # total number of choices (fChoices may be truncated)
  fSelectedChoice: int?  # Radio, PullDown, ComboBox, SearchablePullDown
  fIsOn: bool?  # Toggle
  fValue: str  # current value as text (see ModeBar.GetModeValue)

### ModeSetting()
A mode change request used by the generic, text based mode API (see ModeBar.SetMode).
fields: fModeIndex: int, fValue: str

### ModeBar()
Stateless view over the Tool bar (mode bar) of the active tool. Obtain it with ToolAccess.ModeBar(). Every method requires an open document (Document.IsOpen()).
- GetModeCount() -> int
- GetModes(maxChoices: int=max) -> [ToolMode]  # maxChoices limits fChoices of every mode (fChoiceCount always holds the full count).
- GetMode(modeIndex: int, maxChoices: int=max) -> ToolMode?
- GetModeType(modeIndex: int) -> ModeType?
- FindMode(name: str) -> int?  # Index of the first mode whose label or one of whose choices matches 'name'...
- GetModeValue(modeIndex: int) -> str?  # Current value as text: Radio - name of the selected button (or its index when unnamed), Toggle - "on"/"off", Button - empty,; PullDown/SearchablePullDown - selected item text, EditText/ComboBox - field text,; ResourcePopup - selected resource name.
- SelectRadio(modeIndex: int, choiceIndex: int) -> bool
- PressButton(modeIndex: int) -> bool
- SetToggle(modeIndex: int, isOn: bool) -> bool
- SelectItem(modeIndex: int, itemIndex: int) -> bool  # PullDown, ComboBox or SearchablePullDown
- SelectItem(modeIndex: int, itemNameOrId: str) -> bool  # PullDown, ComboBox or SearchablePullDown: matches the item text, or the item id for...
- SetText(modeIndex: int, text: str) -> bool  # EditText or ComboBox
- SelectResource(modeIndex: int, resourceName: str) -> bool  # ResourcePopup: selects the resource by name without showing the pop-up
- SelectChoice(modeIndex: int, choiceIndex: int) -> bool  # Picks the n-th choice: Radio - button n, Button - press (n ignored), Toggle - n != 0...
- SetMode(modeIndex: int, value: str) -> bool  # Interprets 'value' according to the mode type: Radio - button name, image specifier or 0-based index; Button - presses the button (value ignored); Toggle - "on"/"off", "true"/"false", "yes"/"no", "1"/"0" or "toggle"; PullDown - item text or 0-based index; SearchablePullDown - item text, item id or 0-based index; ComboBox - item text, otherwise the text is entered into the field; EditText - the text to enter; ResourcePopup - resource name
- SetModes(settings: [ModeSetting]) -> bool  # Applies the settings in order; stops at the first failure and returns False.

### ToolControl()
Stateless driver of the active tool. Obtain it with ToolAccess.Control() after activating a tool.
- IsAvailable() -> bool [s]  # Whether there is an active view pane that can receive input.
- GetToolPointCount() -> int  # Points entered into the active tool so far; empty when the tool is idle.
- GetToolPoints() -> [ToolPoint]
- GetCurrentPoint() -> ToolPoint?  # Current (hover) point of the active tool.
- IsToolInProgress() -> bool
- GetViewSize() -> ViewSize?
- ModelToView(modelPoint: Point2D|Point3D) -> ViewPoint?  # View position of a model point; None when it is outside the active pane.
- ViewToModel(viewPoint: ViewPoint) -> Point2D?  # 2D model point under a view position (on the layer plane in Top/Plan, on the screen plane...
- MoveTo(modelPoint: Point2D|Point3D) -> bool  # Moves the pointer without clicking; tools update their preview (rubber band) to the new...
- MoveTo(viewPoint: ViewPoint) -> bool
- Click(modelPoint: Point2D|Point3D) -> bool  # Left click (mouse down + mouse up) - usually adds one tool point.
- Click(viewPoint: ViewPoint) -> bool
- DoubleClick(modelPoint: Point2D|Point3D) -> bool  # Double click - completes multi point tools or edits the object under the pointer...
- DoubleClick(viewPoint: ViewPoint) -> bool
- Drag(from_: Point2D|Point3D|ViewPoint, to: Point2D|Point3D|ViewPoint) -> bool  # Mouse down at 'from', move, mouse up at 'to' (click-drag drawing mode, marquee selection...
- PressKey(key: ToolKey) -> bool  # Sends the key exactly like the user pressing it over the drawing.
- Finish() -> bool  # Completes the current tool action (Return key).
- Cancel() -> bool  # Removes all tool points and restarts the tool action; does not change the selection.
- RemoveLastPoint() -> bool  # Removes the most recent tool point.

### ToolAccess()
Stateless facade over the Vectorworks tool system.
- IsAvailable() -> bool [s]  # Whether tools can be activated and modes changed (requires an open document).
- GetTools(filter=ToolFilter.All) -> [Tool]
- FindTool(name: str) -> Tool?  # Looks a tool up by universal name, user friendly name or localized display name (in this...
- IsToolInWorkspace(name: str) -> bool
- CanActivateTool(name: str) -> bool
- GetActiveTool() -> Tool?
- GetActiveToolUniversalName() -> str?
- IsToolActive(name: str) -> bool
- GetActiveToolHelpMessage() -> str?  # Instruction text the active tool currently shows to the user (e.g. "Click to set the...
- ActivateTool(name: str) -> bool
- ActivateTool(name: str, modeSettings: [ModeSetting]) -> bool  # Activates the tool, then applies the mode settings (see ModeBar.SetModes).
- ActivateTool(name: str, modeIndex: int, choiceIndex: int) -> bool  # Activates the tool, then picks the n-th choice of a mode (see ModeBar.SelectChoice).
- ActivateSelectionTool() -> bool  # Returns to the default Selection tool.
- ModeBar() -> ModeBar
- Control() -> ToolControl

### ==== Menus (menu commands, menu bar, chunk items) ====
`MenuAccess` identifies commands by universal name (built-in: negative number, also accepts the English name `fName` or
the display title). Executing a command behaves like choosing it in the menu bar: it is checked for being enabled, may
open a dialog and creates its own undo event. Only commands placed in the current workspace run; `GetMenuStatus` tells why
a command does not. Chunk items are 0-based (`vs.DoMenuTextByName` uses index + 1) and are read from the menu bar, which
is not updated while a script runs (see section 5).

### MenuCommand()
Description of one installed menu command.
fields:
  fUniversalName: str  # unique identity; pass it to ExecuteMenu / FindMenuCommand
  fName: str  # user friendly English name (equals fUniversalName for plug-in commands)
  fDisplayName: str  # localized title shown in the menus
  fCategory: str  # category of the command in the Workspace Editor
  fHelpText: str  # short description of the command
  fShortcut: str  # keyboard shortcut in the current workspace (may be empty)
  fKind: MenuCommandKind
  fIsChunk: bool  # provides a group of items (see MenuAccess.GetChunkItems)
  fIsInWorkspace: bool  # placed in the menus of the current workspace
  fIsEnabled: bool  # ExecuteMenu can run it now (a chunk: at least one of its items)

### MenuChunkItem()
One current item of a chunk.
fields:
  fIndex: int  # position in the chunk; SDK chunk index is fIndex + 1
  fText: str  # item text as the menu shows it
  fIsEnabled: bool  # ExecuteMenu can run it now
  fIsChecked: bool  # the menu shows a check mark (always False on Mac: the shell does not report it)

### MenuEntry()
One entry of a menu of the menu bar, as the current workspace defines it.
fields:
  fType: MenuEntryType
  fMenuPath: [str]  # titles of the menus containing the entry, from the menu bar down (e.g. ["File", "Export"])
  fText: str  # title shown in the menu (empty for separators)
  fUniversalName: str  # Command, ChunkItem: universal name of the command or the chunk
  fChunkKind: MenuChunkKind  # ChunkItem: kind of the chunk
  fChunkItemIndex: int?  # ChunkItem: index of the item in the chunk
  fShortcut: str  # keyboard shortcut (may be empty)
  fIsEnabled: bool  # Command, ChunkItem: ExecuteMenuEntry can run it now
  fIsChecked: bool  # Command, ChunkItem: the menu shows a check mark (see MenuChunkItem.fIsChecked)

### MenuAccess()
Stateless facade over the Vectorworks menu system.
- IsAvailable() -> bool [s]  # Whether menu commands can be executed now: the menu bar is set up and no plug-in object is being regenerated.
- GetMenuCommands(filter=MenuFilter.All) -> [MenuCommand]
- FindMenuCommand(name: str) -> MenuCommand?  # By universal name, English name or display title (in this order); a command in the workspace wins.
- IsMenuCommandInWorkspace(name: str) -> bool
- GetMenuTitles() -> [str]  # Titles of the menus of the menu bar, from left to right.
- GetMenuEntries() -> [MenuEntry]  # Every entry of the menu bar, depth first: a Submenu entry is followed by its entries; chunks are expanded into their current items.
- GetMenuEntries(menuTitle: str) -> [MenuEntry]  # The entries of one menu of the menu bar, including its submenus.
- FindMenuEntry(path: [str]) -> MenuEntry?  # The entry whose menu path and text equal 'path', e.g. ["Modify", "Align", "Align Left"].
- GetChunkItems(name: str) -> [MenuChunkItem]  # Items of a chunk placed in the workspace, as the menu bar shows them (see section 5); empty when 'name' is not such a chunk.
- FindChunkItem(name: str, itemText: str) -> int?  # Index of the chunk item whose text matches 'itemText'.
- GetMenuStatus(name: str) -> MenuStatus  # Whether ExecuteMenu would run it now, and why not. Without an index a chunk with exactly one item is accepted.
- GetMenuStatus(name: str, chunkItemIndex: int) -> MenuStatus
- CanExecuteMenu(name: str) -> bool
- ExecuteMenu(name: str) -> bool  # Executes a normal command, or the only item of a chunk.
- ExecuteMenu(name: str, chunkItemIndex: int) -> bool  # Executes an item of a chunk.
- ExecuteMenu(name: str, chunkItemText: str) -> bool
- ExecuteMenuEntry(entry: MenuEntry) -> bool  # Executes a Command or ChunkItem entry of GetMenuEntries.

### ==== Object Info palette (controls of the Shape, Data and Render panes) ====
`OIPAccess` reads the controls the OIP shows for the current selection and changes them exactly as the user would (the
same core path on Windows and macOS: undo, plug-in object reset). Control ids come from `GetControls` / `FindControl` and
stay valid until the OIP is rebuilt (see section 5). Choice indices are 0-based.

### OIPControl()
Description and live state of one Object Info palette control.
fields:
  fId: int  # control id; valid until the OIP is rebuilt
  fPane: OIPPane
  fType: OIPControlType
  fCoreTypeId: int  # switchboard type id of the core widget (diagnostics)
  fParentId: int  # id of the parent control (0 when none)
  fLabel: str  # prompt / label shown next to the control
  fValue: str  # current value as text (see OIPAccess.GetValue)
  fChoices: [str]  # RadioGroup, PullDown, ClassPullDown, LayerPullDown (limited by maxChoices)
  fChoiceCount: int  # total number of choices
  fSelectedChoice: int?  # choice controls (incl. SearchablePullDown)
  fIsChecked: bool?  # CheckBox (None when indeterminate)
  fIsEnabled: bool
  fIsVisible: bool
  fIsReadOnly: bool  # EditText that only displays a value
  fIsIndeterminate: bool  # multiple selection with different values

### OIPSetting()
A control change request used by the generic, text based OIP API (see OIPAccess.SetValue).
fields:
  fPane: OIPPane
  fControlId: int
  fValue: str

### OIPAccess()
Stateless, direct access to the Object Info palette.
- IsAvailable() -> bool [s]  # Whether the OIP can be accessed (requires an open document).
- IsPaneAvailable(pane: OIPPane) -> bool  # Whether the pane currently shows controls.
- GetControls(pane=OIPPane.Shape, maxChoices=max, includeHidden=False) -> [OIPControl]  # Controls of the pane in id order.
- GetControl(pane: OIPPane, controlId: int, maxChoices=max) -> OIPControl?
- FindControl(pane: OIPPane, label: str) -> int?  # First visible control whose label matches (case-insensitive; a trailing ':' is ignored).
- GetValue(pane: OIPPane, controlId: int) -> str?  # EditText: text; StaticText: label; CheckBox: "on"/"off" ("" when indeterminate); choices: selected item text; Button/Other: "".
- SetText(pane: OIPPane, controlId: int, text: str) -> bool  # EditText, typed as the user would (units and math evaluated by the core).
- SetChecked(pane: OIPPane, controlId: int, isChecked: bool) -> bool  # CheckBox.
- SelectChoice(pane: OIPPane, controlId: int, choiceIndex: int) -> bool  # RadioGroup, PullDown, SearchablePullDown, ClassPullDown, LayerPullDown.
- SelectChoice(pane: OIPPane, controlId: int, choiceName: str) -> bool  # Item text, case-insensitive.
- PressButton(pane: OIPPane, controlId: int) -> bool  # Presses and releases the button (may open a dialog).
- SetValue(pane: OIPPane, controlId: int, value: str) -> bool  # Generic: interprets 'value' by control type (see section 5).
- SetValues(settings: [OIPSetting]) -> bool  # Applies the settings in order; stops at the first failure.
- NotifyChanged(pane: OIPPane, controlId: int, changeInfo: int) -> bool  # Raises the raw "widget changed" event (0 = plain value change); for Other controls, expert use.
- Refresh(pane: OIPPane) -> bool  # Rebuilds the pane from the selection.

### ==== Alerts and dialogs (full reference: [UILayoutCreate.md](UILayoutCreate.md)) ====
enums: DialogResult{None_=0,Ok,Cancel,ButtonA,ButtonB}  AlertButton{Cancel=0,Ok,ButtonA,ButtonB}  EditRealType{Real=1,Angle,Dimension,CoordinateX,CoordinateY}  StaticTextStyle{Regular=0,Caption,Bold,Reduced}  CheckState{Off=0,On,Mixed}  DialogEventType{Setup=0,Setdown,Ok,Cancel,Control,Resize,Timer,EditLostFocus,Other}  ListBrowserControlType{None_=1,Radio,MultiState,SingleInstance,NoClick,Number,MultipleImages,DiscTriangle}  ListBrowserDisplayType{ImageOnly=1,TextOnly,ImageAndText}  ListBrowserEventType{Unknown=0,DataChangeClick,DataChangeAllClick,SelectionChangeClick,DoubleClick,DeleteKeyPressed,UpKey,DownKey,AlphaNumericKey,SortOccurred,SelectionMultChangeClick,EnterKey,DataChangeRecursiveClick,DoubleAllClick,DoubleRecursiveClick,ReceivingDragAndDrop,DragAndDrop}

### DialogEvent()
fields: fDialogID: int, fControlID: int (1 = OK, 2 = Cancel), fEvent: DialogEventType, fData: int (slider position, color 0x00RRGGBB, raw code for Other), fIsNegative: bool (secondary action, e.g. list browser double-click)

### ListBrowserEvent()
fields: fEvent: ListBrowserEventType, fRow: int (-1 none), fColumn: int (-1 none)

### DialogSize()
fields: fWidth: int, fHeight: int  # pixels

### TextPair()
fields: fFirst: str, fSecond: str  # supports ==, !=

### Alerts (static only)
- Inform(text: str, advice="", isMinor=False, category="", item="", checkboxText="") -> None [s]  # category+item add "do not show again"
- Critical(text: str, advice="") -> None [s]
- Question(question: str, advice="", defaultButton=AlertButton.Ok, okText="", cancelText="", buttonAText="", buttonBText="", category="", item="", checkboxText="") -> DialogResult [s]
- Confirm(question: str, advice="", okText="", cancelText="", isOkDefault=True) -> bool [s]
- InformWithLink(text: str, adviceBeforeLink: str, linkTitle: str, linkURL: str, adviceAfterLink="", isMinor=False, category="", item="", checkboxText="") -> None [s]
- CriticalWithLink(text: str, adviceBeforeLink: str, linkTitle: str, linkURL: str, adviceAfterLink="") -> None [s]
- AreAlertsAllowed() -> bool [s]  # False in batch / automated test mode

### StandardDialogs (static only; every function returns None on cancel)
- EditText(title: str, label: str, value="", okText="", cancelText="", helpText="", isEmptyAllowed=True) -> str? [s]
- EditMultilineText(title: str, label: str, value="", width=40, height=10, okText="", cancelText="", helpText="", isEmptyAllowed=True) -> str? [s]
- EditTwoTexts(title: str, label1: str, label2: str, value1="", value2="", helpText1="", helpText2="", okText="", cancelText="") -> TextPair? [s]
- EditInteger|EditReal|EditDimension|EditAngle(title: str, label: str, value=0|0.0, okText="", cancelText="", helpText="") -> int?|float?|float?|float? [s]  # Dimension: world units; Angle: degrees
- EditPoint2D|EditPoint3D(title: str, label: str, value=Point2D()|Point3D(), okText="", cancelText="", helpText="") -> Point2D?|Point3D? [s]  # world units
- ChooseFromList(title: str, label: str, choices: [str], selectedIndex=0, okText="", cancelText="") -> int? [s]
- ChooseManyFromList(title: str, label: str, choices: [str], selectedIndices=[], okText="", cancelText="") -> [int]? [s]

### LayoutDialog(title: str, okText="", cancelText="", hasCancel=True, isWidthResizable=False, isHeightResizable=False)
Layout manager dialog; runs at most once; not copyable. Actions/setters return bool (False: unknown controlID, wrong control kind,
or not allowed now). Getters: None before showing, live while running, captured values after Run.
Identifiers: controlID/referenceControlID/tabControlID/swapControlID are controls; groupControlID/paneControlID are group-box
controls. alignmentGroupID is a shared edge-alignment label, NOT a control; tree itemID/parentID are tree items.
- IsValid() -> bool; GetDialogID() -> int; IsRunning() -> bool; WasRun() -> bool
- Run(helpID="") -> DialogResult  # Ok / Cancel; None_ when already run or invalid
- Close(isOk=True) -> bool  # from a handler; OnOk/OnCancel not called
- CancelClose() -> None  # from OnOk/OnCancel: keep the dialog open
- OnSetup|OnSetdown|OnOk|OnCancel|OnResize|OnEditLostFocus|OnAnyEvent(handler: fn(DialogEvent)) -> None
- OnControl(controlID: int, handler: fn(DialogEvent)) -> None
- GetListBrowserEvent(controlID: int) -> ListBrowserEvent  # inside that control's handler
- SetFirstItem(controlID); SetFirstGroupItem(groupControlID, controlID); PlaceBelow|PlaceRight(referenceControlID, controlID, indent=0, spacing=0)
- BindEdges|BindProportional(controlID, isLeft, isRight, isTop, isBottom); AlignLeft|AlignRight|AlignBottom(controlID, alignmentGroupID, isResizing=False)
  # Align* registers each control in a shared group for that edge. No control with alignmentGroupID needs to exist.
  # Call for every participating control with the same group ID. False shifts; True resizes; building phase only.
- SetControlSize(controlID, widthInPixels, heightInPixels); SetDialogSize(size: DialogSize); GetDialogSize() -> DialogSize?; SetDialogPosition(left, top)
- Controls (all -> bool): AddStaticText(controlID, text, width=-1, style=StaticTextStyle.Regular), AddCenteredStaticText(controlID, text, width=-1),
  AddRightStaticText(controlID, text, width=-1), AddEditText(controlID, text="", width=20, heightInLines=1), AddEditInteger(controlID, value=0, width=10),
  AddEditReal(controlID, value=0.0, type=EditRealType.Real, width=10), AddEditPassword(controlID, width=20), AddSearchBox(controlID, prompt="", width=20),
  AddPushButton(controlID, text), AddCheckBox(controlID, text), AddThreeStateCheckBox(controlID, text), AddRadioButton(controlID, text),
  AddGroupBox(controlID, text="", hasFrame=True), AddCheckBoxGroupBox(controlID, text, hasFrame=True), AddRadioButtonGroupBox(controlID, text, hasFrame=True),
  AddPullDownMenu(controlID, width=20), AddListBox(controlID, width=20, heightInLines=8, isMultiSelect=False), AddListBrowser(controlID, width=40, heightInLines=10),
  AddTreeControl(controlID, width=40, heightInLines=10), AddTabControl(controlID), AddTabPane(tabControlID, paneControlID), AddSwapControl(controlID),
  AddSwapPane(swapControlID, paneControlID), AddSeparator(controlID, widthInPixels=0), AddColorPopup(controlID, width=-1), AddPatternPopup(controlID),
  AddLineWeightPopup(controlID), AddClassPullDown(controlID, width=30, isShowingDefaultItems=True), AddLayerPullDown(controlID, width=30, isShowingDefaultItems=True),
  AddColorButton(controlID, color=ColorRGB()), AddSlider(controlID, maximum=100), AddImage(controlID, widthInPixels, heightInPixels, imageSpecifier); HasControl(controlID) -> bool
- Any control: Enable(controlID, isEnabled=True), Show(controlID, isVisible=True), IsEnabled(controlID) -> bool?, IsVisible(controlID) -> bool?, SetFocus(controlID),
  SetHelpText(controlID, helpText), SetToolTip(controlID, toolTip, subToolTip=""), SetIndeterminate(controlID, isIndeterminate=True)
- Text: SetText|GetText(controlID) -> str?, SetTextEditable(controlID, isEditable), SelectAllText(controlID), SetTextSelection(controlID, start, end),
  SetStaticTextStyle(controlID, style), SetStaticTextColor(controlID, color: ColorRGB)
- Values: SetBool|GetBool -> bool?, SetCheckState|GetCheckState -> CheckState?, SetInteger|GetInteger -> int?, SetReal|GetReal -> float?
- Choices (pull-down, list box, class/layer pull-down): AddChoice(controlID, text, index=-1), SetChoices(controlID, choices: [str]), RemoveChoice(controlID, index),
  RemoveAllChoices(controlID), GetChoiceCount(controlID) -> int?, GetChoiceText(controlID, index) -> str?, FindChoice(controlID, text) -> int?,
  SelectChoice(controlID, index, isSelected=True), SelectChoiceByText(controlID, text), GetSelectedChoice(controlID) -> int?, GetSelectedChoiceText(controlID) -> str?,
  GetSelectedChoices(controlID) -> [int]?
- Attributes: SetColorButton|GetColorButton -> ColorRGB?, SetColorIndex|GetColorIndex, SetPatternIndex|GetPatternIndex, SetLineWeight|GetLineWeight (mils)
- SetSliderValue|GetSliderValue, SetSliderLiveUpdate(controlID, isLive), SetSliderTickMarks(controlID, count), SetImage(controlID, imageSpecifier),
  ShowTabPane(tabControlID, paneControlID), ShowSwapPane(swapControlID, paneControlID), GetActivePane(controlID) -> int?  # visible pane's group-box control ID, not alignmentGroupID
- List browser (rows/columns 0-based; Add* return bool): AddListBrowserColumn(controlID, header, widthInPixels=100, column=-1), RemoveListBrowserColumn,
  GetListBrowserColumnCount, SetListBrowserColumnWidth, SetListBrowserColumnControl(controlID, column, controlType: ListBrowserControlType),
  SetListBrowserColumnDisplay(controlID, column, itemDisplay, editDisplay=TextOnly), AddListBrowserColumnChoice(controlID, column, text, imageOn=-1, imageOff=-1, data=0),
  SetListBrowserCellChoice(controlID, row, column, choiceIndex), AddListBrowserRow(controlID, text, row=-1), AddListBrowserRowCells(controlID, cells: [str]),
  RemoveListBrowserRow, RemoveAllListBrowserRows, GetListBrowserRowCount, SetListBrowserCell(controlID, row, column, text, imageIndex=-1),
  GetListBrowserCell -> str?, Set|GetListBrowserCellData (int), Set|GetListBrowserCellCheckState (CheckState), SetListBrowserCellTextColor,
  SetListBrowserCellReadOnly, SetListBrowserReadOnly, SelectListBrowserRows(controlID, firstRow, lastRow, isSelected=True), IsListBrowserRowSelected,
  GetListBrowserSelectedRows -> [int]?, EnableListBrowserSorting, SetListBrowserSortColumn(controlID, column, isAscending=True),
  EnableListBrowserSingleSelection, EnableListBrowserDragAndDrop, ShowListBrowserHeader, EnsureListBrowserRowVisible,
  EnableListBrowserUpdates(controlID, isEnabled), RefreshListBrowser(controlID)
- Tree (only while running, e.g. in OnSetup): AddTreeItem(controlID, text, parentID=-1) -> int?, RemoveTreeItem(controlID, itemID), RemoveAllTreeItems,
  GetTreeItemText, GetTreeItemParent, GetTreeItemChildren -> [int]?, Set|GetTreeItemData (int), SetTreeItemCheckState(controlID, itemID, state, isClickable=True),
  GetTreeItemCheckState, ExpandTreeItem(controlID, itemID, isExpanded=True), IsTreeItemExpanded, SelectTreeItem, GetSelectedTreeItem -> int?,
  GetSelectedTreeItems -> [int]?, EnableTreeMultiSelection

### ==== api.Math (standalone 2D math) ====

### Point2D() | (inX: float, inY: float) | (pt: Point2D)
2D point / vector (the equivalent of VWFC VWPoint2D).
fields: x: float, y: float
- FromPolar(length: float, angle: float) -> Point2D [s]
- UnitFromAngle(angle: float) -> Point2D [s]
- IsEqual(o: Point2D, tolerance: float=kEpsilon) -> bool
- IsZero(tolerance: float=kEpsilon) -> bool
- Dot(o: Point2D) -> float
- Cross(o: Point2D) -> float  # z of the 3D cross product
- LengthSquared() -> float
- Length() -> float
- Angle() -> float  # (-pi, pi]
- Normalized() -> Point2D
- Normalize() -> Point2D
- WithLength(length: float) -> Point2D
- Perpendicular() -> Point2D  # rotated 90 degrees counter-clockwise
- PerpendicularCW() -> Point2D  # rotated 90 degrees clockwise
- Rotated(angle: float) -> Point2D
- Rotated(angle: float, center: Point2D) -> Point2D
- Scaled(sx: float, sy: float, center: Point2D=(0,0)) -> Point2D
- DistanceSquaredTo(o: Point2D) -> float
- DistanceTo(o: Point2D) -> float
- AngleTo(o: Point2D) -> float  # direction from this point to 'o'
- MidPoint(o: Point2D) -> Point2D
- Lerp(o: Point2D, t: float) -> Point2D
- AngleBetween(o: Point2D) -> float  # Signed angle from this vector to 'o', in (-pi, pi], positive is counter-clockwise
- IsParallel(o: Point2D, angleTolerance: float=kAngleEpsilon) -> bool
- IsPerpendicular(o: Point2D, angleTolerance: float=kAngleEpsilon) -> bool
- Orientation(a: Point2D, b: Point2D, c: Point2D) -> float [s]  # Returns > 0 when 'c' is to the left of a->b, < 0 when to the right, 0 when collinear.
- operators: p+q, p-q, -p, p*f, f*p, p/f, +=, -=, *=, /=, ==, != (f: float)

### Transform2D() | (inA: float, inB: float, inC: float, inD: float, inTx: float, inTy: float)
2D affine transformation (the equivalent of VWFC VWTransformMatrix restricted to 2D). | a b tx | | x | | c d ty | * | y | | 0 0 1 | | 1 | Composition 'A * B' applies B first, then A.
fields: a: float, b: float, tx: float, c: float, d: float, ty: float
- Identity() -> Transform2D [s]
- Translation(dx: float, dy: float) -> Transform2D [s]
- Translation(v: Vector2D) -> Transform2D [s]
- Rotation(angle: float) -> Transform2D [s]
- Rotation(angle: float, center: Point2D) -> Transform2D [s]
- Scale(sx: float, sy: float) -> Transform2D [s]
- Scale(sx: float, sy: float, center: Point2D) -> Transform2D [s]
- Mirror(p1: Point2D, p2: Point2D) -> Transform2D [s]  # Mirror across the infinite line through p1 and p2
- FromAxes(origin: Point2D, xAxis: Vector2D, yAxis: Vector2D) -> Transform2D [s]  # Maps the unit X/Y axes to 'xAxis'/'yAxis' and the origin to 'origin'
- Then(next: Transform2D) -> Transform2D  # The transform that applies this one first and then 'next'
- Apply(p: Point2D) -> Point2D
- ApplyToVector(v: Vector2D) -> Vector2D
- Determinant() -> float
- IsInvertible(tolerance: float=kEpsilon) -> bool
- Inverse() -> Transform2D?
- GetTranslation() -> Vector2D
- SetTranslation(v: Vector2D)
- GetRotation() -> float  # rotation of the X axis
- GetScaleX() -> float
- GetScaleY() -> float  # negative when mirrored
- IsMirrored() -> bool
- IsOrthogonal(tolerance: float=kEpsilon) -> bool  # Rotation and uniform/non-uniform scale along the axes only (no shear)
- IsIdentity(tolerance: float=kEpsilon) -> bool
- IsEqual(o: Transform2D, tolerance: float=kEpsilon) -> bool
- operators: A*B (applies B first, then A), A*=B, t(p) == t.Apply(p)

### Rect2D() | (inLeft: float, inTop: float, inRight: float, inBottom: float) | (p1: Point2D, p2: Point2D)
Axis aligned rectangle (the equivalent of VWFC VWRectangle2D). Y grows upwards: top >= bottom. A default constructed rectangle is empty; adding points to it grows it.
fields: left: float, bottom: float, right: float, top: float
- FromCenter(center: Point2D, width: float, height: float) -> Rect2D [s]
- IsEmpty() -> bool
- IsDegenerate(tolerance: float=kEpsilon) -> bool  # Empty or with zero width or height
- Width() -> float
- Height() -> float
- Area() -> float
- Perimeter() -> float
- Diagonal() -> float
- Center() -> Point2D
- TopLeft() -> Point2D
- TopRight() -> Point2D
- BottomLeft() -> Point2D
- BottomRight() -> Point2D
- CenterLeft() -> Point2D
- CenterRight() -> Point2D
- CenterTop() -> Point2D
- CenterBottom() -> Point2D
- Corners() -> (Point2D *4)  # Counter-clockwise, starting at bottom-left
- Add(p: Point2D) -> Rect2D
- Add(r: Rect2D) -> Rect2D
- Union(r: Rect2D) -> Rect2D
- Intersection(r: Rect2D) -> Rect2D
- Inflated(dx: float, dy: float) -> Rect2D  # Grows by 'dx' on left and right, by 'dy' on top and bottom (negative values shrink)
- Offset(v: Vector2D) -> Rect2D
- Transformed(t: Transform2D) -> Rect2D  # Bounds of the transformed corners
- Contains(p: Point2D, tolerance: float=kEpsilon) -> bool
- Contains(r: Rect2D, tolerance: float=kEpsilon) -> bool
- Intersects(r: Rect2D, tolerance: float=kEpsilon) -> bool
- ClosestPoint(p: Point2D) -> Point2D
- DistanceTo(p: Point2D) -> float
- IsEqual(r: Rect2D, tolerance: float=kEpsilon) -> bool
- FromPoints(points: [Point2D]) -> Rect2D [s]  # bounds of the points

### RotatedRect2D() | (inOrigin: Point2D, inDirection: Vector2D, inWidth: float, inHeight: float) | (r: Rect2D)
Rectangle that may be rotated: a corner, the direction of the width side and the two side lengths. This is how Vectorworks stores rectangles and rounded rectangles.
fields:
  origin: Point2D
  direction: Vector2D  # unit vector along the width side
  width: float
  height: float
- FromCenter(center: Point2D, inWidth: float, inHeight: float, angle=0.0) -> RotatedRect2D [s]
- Angle() -> float
- WidthVector() -> Vector2D
- HeightVector() -> Vector2D
- Area() -> float
- Perimeter() -> float
- Center() -> Point2D
- IsAxisAligned(angleTolerance: float=kAngleEpsilon) -> bool
- Corners() -> (Point2D *4)
- Bounds() -> Rect2D
- LocalToWorld() -> Transform2D  # Local frame: X along the width side, Y along the height side, origin at 'origin'
- Contains(p: Point2D, tolerance: float=kEpsilon) -> bool
- Offset(v: Vector2D) -> RotatedRect2D
- Rotated(angle: float, center: Point2D) -> RotatedRect2D
- Normalized() -> RotatedRect2D  # Same rectangle, normalized to positive width and height
- Transformed(t: Transform2D, tolerance: float=kEpsilon) -> RotatedRect2D?  # Only similarity transforms (rotation, translation, uniform scale, mirror) keep a...
- IsEqual(r: RotatedRect2D, tolerance: float=kEpsilon) -> bool

### Line2D() | (inStart: Point2D, inEnd: Point2D) | (x1: float, y1: float, x2: float, y2: float)
Line segment from 'start' to 'end' (the equivalent of VWFC VWLine2D). Methods with "Infinite" in the name treat the segment as an infinite line through both points. A parameter 't' maps 0 to 'start' and 1 to 'end'.
fields: start: Point2D, end: Point2D
- FromPointAngleLength(inStart: Point2D, angle: float, length: float) -> Line2D [s]
- Vector() -> Vector2D
- Direction() -> Vector2D
- Normal() -> Vector2D  # unit normal to the left
- Length() -> float
- LengthSquared() -> float
- Angle() -> float
- MidPoint() -> Point2D
- PointAt(t: float) -> Point2D
- PointAtDistance(distanceFromStart: float) -> Point2D
- IsDegenerate(tolerance: float=kEpsilon) -> bool
- Bounds() -> Rect2D
- Reversed() -> Line2D
- Offset(v: Vector2D) -> Line2D
- OffsetParallel(distance: float) -> Line2D  # Parallel line at 'distance' to the left (negative: to the right)
- Transformed(t: Transform2D) -> Line2D
- Rotated(angle: float, center: Point2D) -> Line2D
- WithLength(length: float) -> Line2D  # Moves the end point along the line so the segment has the specified length
- Extended(atStart: float, atEnd: float) -> Line2D  # Extends (or trims when negative) both ends
- ProjectParameter(p: Point2D) -> float  # Parameter of the projection of 'p' on the infinite line
- ProjectInfinite(p: Point2D) -> Point2D
- ClosestPoint(p: Point2D) -> Point2D
- DistanceTo(p: Point2D) -> float
- DistanceToInfinite(p: Point2D) -> float
- SignedDistanceToInfinite(p: Point2D) -> float  # Positive when 'p' is to the left of the line
- SideOf(p: Point2D, tolerance: float=kEpsilon) -> int  # > 0 left, < 0 right, 0 on the infinite line
- IsPointOn(p: Point2D, tolerance: float=kEpsilon) -> bool
- IsPointOnInfinite(p: Point2D, tolerance: float=kEpsilon) -> bool
- Mirror(p: Point2D) -> Point2D
- IsParallel(o: Line2D, angleTolerance: float=kAngleEpsilon) -> bool
- IsPerpendicular(o: Line2D, angleTolerance: float=kAngleEpsilon) -> bool
- IsCollinear(o: Line2D, tolerance: float=kEpsilon) -> bool
- IntersectInfinite(o: Line2D) -> Intersection?
- Intersect(o: Line2D, tolerance: float=kEpsilon) -> Point2D?  # Intersection point of the two segments (parallel or collinear segments return no point)
- Intersects(o: Line2D, tolerance: float=kEpsilon) -> bool
- DistanceTo(o: Line2D) -> float  # Shortest distance between the two segments
- IsEqual(o: Line2D, tolerance: float=kEpsilon) -> bool
- IsEqualIgnoreDirection(o: Line2D, tolerance: float=kEpsilon) -> bool

### Line2D.Intersection()
Intersection of the infinite lines. Returns the point and the parameters on this line and on 'o'.
fields:
  point: Point2D
  t: float  # parameter on this line
  tOther: float  # parameter on the other line

### Circle2D() | (inCenter: Point2D, inRadius: float)
Circle (the equivalent of VWFC VWCircle2D).
fields: center: Point2D, radius: float
- FromDiameter(p1: Point2D, p2: Point2D) -> Circle2D [s]
- FromThreePoints(p1: Point2D, p2: Point2D, p3: Point2D) -> Circle2D? [s]  # Circle through three points; empty when the points are collinear
- Diameter() -> float
- Circumference() -> float
- Area() -> float
- Bounds() -> Rect2D
- IsDegenerate(tolerance: float=kEpsilon) -> bool
- PointAt(angle: float) -> Point2D
- AngleOf(p: Point2D) -> float
- TangentAt(angle: float) -> Vector2D  # counter-clockwise direction
- ClosestPoint(p: Point2D) -> Point2D
- DistanceTo(p: Point2D) -> float  # Distance to the circumference
- Contains(p: Point2D, tolerance: float=kEpsilon) -> bool
- IsPointOn(p: Point2D, tolerance: float=kEpsilon) -> bool
- Offset(v: Vector2D) -> Circle2D
- Rotated(angle: float, c: Point2D) -> Circle2D
- Scaled(factor: float, c: Point2D) -> Circle2D
- IntersectInfinite(line: Line2D, tolerance: float=kEpsilon) -> [Point2D]  # Intersection points with the infinite line (0, 1 or 2 points)
- Intersect(line: Line2D, tolerance: float=kEpsilon) -> [Point2D]  # Intersection points with the segment
- Intersect(o: Circle2D, tolerance: float=kEpsilon) -> [Point2D]  # Intersection points with another circle (coincident circles return no points)
- TangentPoints(p: Point2D, tolerance: float=kEpsilon) -> [Point2D]  # Tangent points on the circle for tangent lines through 'p' (none when 'p' is inside)
- IsEqual(o: Circle2D, tolerance: float=kEpsilon) -> bool

### Arc2D() | (inCenter: Point2D, inRadius: float, inStartAngle: float, inSweepAngle: float) | (circle: Circle2D)
Circular arc (the equivalent of VWFC VWArc2D). 'sweepAngle' is positive for counter-clockwise arcs and negative for clockwise arcs; |sweepAngle| >= 2*pi is a full circle.
fields: center: Point2D, radius: float, startAngle: float, sweepAngle: float
- FromCenterStartEnd(inCenter: Point2D, startPt: Point2D, endPt: Point2D, ccw=True) -> Arc2D [s]  # Counter-clockwise (ccw = True) or clockwise arc from 'startPt' to the ray through 'endPt'
- FromThreePoints(startPt: Point2D, midPt: Point2D, endPt: Point2D) -> Arc2D? [s]  # Arc starting at 'startPt', passing through 'midPt' and ending at 'endPt'; empty when the...
- FromTangent(startPt: Point2D, startTangent: Vector2D, endPt: Point2D) -> Arc2D? [s]  # Arc from 'startPt' with the given start tangent direction, ending at 'endPt'
- Circle() -> Circle2D
- IsFullCircle(tolerance: float=kAngleEpsilon) -> bool
- IsCounterClockwise() -> bool
- EndAngle() -> float
- MidAngle() -> float
- PointAtAngle(angle: float) -> Point2D
- PointAt(t: float) -> Point2D
- StartPoint() -> Point2D
- EndPoint() -> Point2D
- MidPoint() -> Point2D
- TangentAt(t: float) -> Vector2D  # Unit tangent in the direction of travel
- Length() -> float
- Chord() -> Line2D
- ChordLength() -> float
- Sagitta() -> float  # Distance from the chord midpoint to the arc midpoint
- SectorArea() -> float
- SegmentArea() -> float  # Area between the arc and its chord
- ContainsAngle(angle: float, tolerance: float=kAngleEpsilon) -> bool  # Whether the ray from the center at 'angle' passes through the arc
- IsPointOn(p: Point2D, tolerance: float=kEpsilon) -> bool
- ClosestPoint(p: Point2D) -> Point2D
- DistanceTo(p: Point2D) -> float
- Bounds() -> Rect2D  # Bounds of the arc curve (not including the center)
- Reversed() -> Arc2D
- Normalized() -> Arc2D  # Same arc with a non-negative sweep and a start angle in [0, 2*pi)
- Offset(v: Vector2D) -> Arc2D
- Rotated(angle: float, c: Point2D) -> Arc2D
- WithRadius(r: float) -> Arc2D  # Concentric arc with a different radius (same angles)
- Intersect(line: Line2D, tolerance: float=kEpsilon) -> [Point2D]  # Intersection points with a segment / another arc / a circle
- Intersect(circle: Circle2D, tolerance: float=kEpsilon) -> [Point2D]
- Intersect(o: Arc2D, tolerance: float=kEpsilon) -> [Point2D]
- Tessellate(maxDeviation: float) -> [Point2D]  # Points along the arc so that the chord deviation is at most 'maxDeviation' (includes both...
- IsEqual(o: Arc2D, tolerance: float=kEpsilon) -> bool

### PolyVertex() | (pt: Point2D, t=VertexType.Corner, radius=0.0, vis=True)
fields:
  point: Point2D
  type: VertexType
  arcRadius: float  # only for VertexType.Arc
  visible: bool  # visibility of the edge starting at this vertex

### Polygon2D() | (points: [Point2D], closed=True) | (vertices: [PolyVertex], closed=True)
Polygon or polyline vertex list (the equivalent of VWFC VWPolygon2D).
Area/perimeter/containment/ClosestPoint/DistanceTo use straight control-point edges; GetCurve... uses actual curves.
- FromRect(r: Rect2D) -> Polygon2D [s]
- FromRotatedRect(r: RotatedRect2D) -> Polygon2D [s]
- FromArc(arc: Arc2D, maxDeviation: float, closeThroughCenter=False) -> Polygon2D [s]
- RegularPolygon(center: Point2D, circumradius: float, sides: int, startAngle=0.0) -> Polygon2D [s]
- GetVertexCount() -> int
- IsEmpty() -> bool
- GetVertex(i: int) -> PolyVertex
- GetPoint(i: int) -> Point2D
- SetPoint(i: int, p: Point2D)
- GetVertices() -> [PolyVertex]
- GetPoints() -> [Point2D]
- AddVertex(v: PolyVertex)
- AddVertex(p: Point2D, type=VertexType.Corner, arcRadius=0.0)
- InsertVertex(beforeIndex: int, v: PolyVertex)
- RemoveVertex(i: int)
- Clear()
- IsClosed() -> bool
- SetClosed(closed: bool)
- HasCurves() -> bool
- HasHiddenEdges() -> bool
- GetHoleCount() -> int
- GetHole(i: int) -> Polygon2D
- AddHole(hole: Polygon2D)
- ClearHoles()
- GetEdgeCount() -> int  # Edges. A closed polygon has as many edges as vertices, an open one has one less.
- GetEdge(i: int) -> Line2D  # Vertex i to vertex i + 1, wrapping to vertex 0; i in 0..GetEdgeCount() - 1; IndexError when i >= GetVertexCount()
- SignedArea() -> float  # Positive for counter-clockwise polygons
- Area() -> float
- Perimeter() -> float
- Centroid() -> Point2D  # Area centroid for closed polygons with non-zero area, vertex average otherwise
- Bounds() -> Rect2D
- IsCounterClockwise() -> bool
- IsClockwise() -> bool
- Reverse() -> Polygon2D  # Reverses the vertex order. Edge visibility follows its edge.
- Reversed() -> Polygon2D
- Contains(p: Point2D, tolerance: float=kEpsilon) -> bool  # Even-odd containment test (the boundary counts as inside)
- IsPointOnBoundary(p: Point2D, tolerance: float=kEpsilon) -> bool
- ClosestPoint(p: Point2D) -> Point2D
- DistanceTo(p: Point2D) -> float
- GetCurveLength() -> float?
- GetCurveLocationAtDistance(distance: float) -> Polygon2D.CurveLocation?
- GetCurvePointAtDistance(distance: float) -> Point2D?
- GetCurveTangentAtDistance(distance: float) -> Vector2D?
- GetCurveCurvatureAtDistance(distance: float) -> float?
- GetCurveClosestPoint(point: Point2D) -> Polygon2D.CurveLocation?
- GetCurveDistanceTo(point: Point2D) -> float?
- DivideCurveByCount(count: int, includeEnd: bool=True) -> [Point2D]?
- IsConvex() -> bool
- IsSelfIntersecting(tolerance: float=kEpsilon) -> bool  # Whether any two non-adjacent edges intersect
- Intersect(line: Line2D, tolerance: float=kEpsilon) -> [Point2D]  # Intersection points of the edges with a segment
- Transform(t: Transform2D) -> Polygon2D
- Transformed(t: Transform2D) -> Polygon2D
- Offset(d: Vector2D) -> Polygon2D  # Translates the polygon and holes.
- Offset(distance: float, join: OffsetJoin=Miter) -> [Polygon2D]
- Rotate(angle: float, center: Point2D) -> Polygon2D
- RemoveDuplicateVertices(tolerance: float=kEpsilon) -> Polygon2D  # Removes consecutive coincident vertices (and the closing duplicate of a closed polygon)
- RemoveCollinearVertices(tolerance: float=kEpsilon) -> Polygon2D  # Removes vertices that lie on the straight line through their neighbours (corner vertices...
- IsEqual(o: Polygon2D, tolerance: float=kEpsilon) -> bool
- Union(other: Polygon2D) -> [Polygon2D]
- Intersection(other: Polygon2D) -> [Polygon2D]
- Difference(other: Polygon2D) -> [Polygon2D]
- SymmetricDifference(other: Polygon2D) -> [Polygon2D]
Value Boolean methods use Core's Parasolid-backed 2D operations, require an open drawing context, and return separate
contours in a list; each result retains nested holes. An empty list is a successful operation with no contours.
Conversion or Boolean failure raises RuntimeError.
The scalar Offset overload is a true Core polyline offset: positive distance expands closed contours; negative distance
insets. It can return multiple contours, retains nested holes, defaults to miter joins, and accepts OffsetJoin.Round
for round arcs at convex joins. A fully collapsed inset returns an empty list; conversion or offset failure raises
RuntimeError. It requires an open drawing context. The Vector2D overload remains translation only.
- len(poly); poly[i] -> PolyVertex (a copy); poly[i] = PolyVertex|Point2D; for v in poly; i < 0 counts from the end; IndexError when out of range

Curve analysis has the same drawing-context/outer-path/coordinate contract as PolyObject. Arc distances are absolute
world millimetres from the start, finite and within [0,length]; no wrapping/clamping. Tangents are unit vectors and
curvature is nonnegative in inverse millimetres. Derivatives are right-hand at knots except left-hand at piece ends;
an exact join distance selects the preceding nonzero-length piece. Corner derivatives are one-sided, not smooth.
DivideCurveByCount returns exactly count>=2 points, not segments: includeEnd=True includes both endpoints (duplicate
seam on closed paths); False omits the last endpoint/seam. Invalid arguments, missing drawing context and Core failure
return None; zero-speed tangent/curvature and zero-length point/division queries return None. Successful length may
be zero. A failed division never returns a partial list.

### api.Math.Polygon2D.CurveLocation()
Writable copied-value record shared by PolyObject and Polygon2D analysis, not a handle to temporary geometry.
fields: point: Point2D=(0,0), pieceIndex: int=0, parameter: float=0.0
pieceIndex identifies a temporary Core NURBS piece, not an original vertex/segment index. parameter is a native knot
parameter within that piece, not a length fraction or arc distance.

### Point3D() | (inX: float, inY: float, inZ: float) | (point: Point2D, inZ: float=0.0) | (point: api.Point3D)
api.Math.Point3D; alias Vector3D is the same type. Python-owned, no document or undo required.
fields: x: float, y: float, z: float
operators: +, binary/unary -, scalar * and /, +=, -=, *=, /=, ==, !=; scalar multiplication works on either side.
Equality operators are exact; use IsEqual for tolerance. Normalize and in-place operators mutate; other vector methods return values.
Implicit conversion to/from api.Point3D; api.Point3D(point) constructs the legacy record.
- IsEqual(other: Point3D, tolerance: float=kEpsilon) -> bool
- IsZero(tolerance: float=kEpsilon) -> bool
- IsFinite() -> bool
- Dot(other: Point3D) -> float
- Cross(other: Point3D) -> Vector3D
- LengthSquared() -> float
- Length() -> float
- Normalized() -> Vector3D
- Normalize() -> Point3D
- WithLength(length: float) -> Vector3D
- DistanceSquaredTo(other: Point3D) -> float
- DistanceTo(other: Point3D) -> float
- MidPoint(other: Point3D) -> Point3D
- Lerp(other: Point3D, parameter: float) -> Point3D
- AngleBetween(other: Point3D) -> float
- IsParallel(other: Point3D, angleTolerance: float=kAngleEpsilon) -> bool
- IsPerpendicular(other: Point3D, angleTolerance: float=kAngleEpsilon) -> bool
- XY() -> Point2D

### Transform3D() | (inA: float, inB: float, inC: float, inD: float, inE: float, inF: float, inG: float, inH: float, inI: float, inTx: float, inTy: float, inTz: float)
api.Math.Transform3D; Python-owned affine matrix, not a general projective matrix. Default is identity.
fields: a, b, c, d, e, f, g, h, i, tx, ty, tz: float
Matrix rows are (a,b,c,tx), (d,e,f,ty), (g,h,i,tz), (0,0,0,1).
Constructor order is nine linear coefficients by row, THEN translation, NOT interleaved rows of four.
operators: * and *= compose transforms; A*B applies B then A. transform(point) is Apply(point).
Only *=, field assignment and SetTranslation mutate. Apply includes translation; ApplyToVector does not.
- Identity() -> Transform3D [s]
- Translation(dx: float, dy: float, dz: float) -> Transform3D [s]
- Translation(offset: Vector3D) -> Transform3D [s]
- Scale(sx: float, sy: float, sz: float) -> Transform3D [s]
- Scale(sx: float, sy: float, sz: float, center: Point3D) -> Transform3D [s]
- RotationX(angle: float) -> Transform3D [s]
- RotationY(angle: float) -> Transform3D [s]
- RotationZ(angle: float) -> Transform3D [s]
- Rotation(angle: float, axis: Vector3D, center: Point3D=Point3D()) -> Transform3D? [s]
- Mirror(origin: Point3D, normal: Vector3D) -> Transform3D? [s]
- FromAxes(origin: Point3D, xAxis: Vector3D, yAxis: Vector3D, zAxis: Vector3D) -> Transform3D [s]
- Then(next: Transform3D) -> Transform3D
- Apply(point: Point3D) -> Point3D
- ApplyToVector(vector: Vector3D) -> Vector3D
- Determinant() -> float
- IsInvertible(tolerance: float=kEpsilon) -> bool
- Inverse() -> Transform3D?
- ApplyToNormal(normal: Vector3D) -> Vector3D?
- GetTranslation() -> Vector3D
- SetTranslation(offset: Vector3D) -> None
- GetXAxis() -> Vector3D
- GetYAxis() -> Vector3D
- GetZAxis() -> Vector3D
- IsMirrored() -> bool
- IsOrthogonal(tolerance: float=kEpsilon) -> bool
- IsIdentity(tolerance: float=kEpsilon) -> bool
- IsEqual(other: Transform3D, tolerance: float=kEpsilon) -> bool
- IsFinite() -> bool
FromAxes uses axes as columns without normalization/validation; scale and shear are allowed.
IsOrthogonal checks pairwise dot products, not unit length or invertibility.
IsInvertible compares abs(determinant) with tolerance; Inverse rejects exactly zero/non-finite determinant or non-finite output.
ApplyToNormal normalizes the inverse-transpose result; zero/non-finite normals or unusable output return None.
Rotation also rejects non-finite angle/center; Mirror rejects non-finite origin.

### Line3D() | (inStart: Point3D, inEnd: Point3D) | (x1: float, y1: float, z1: float, x2: float, y2: float, z2: float)
api.Math.Line3D; Python-owned segment. Default is a point at the origin.
fields: start: Point3D, end: Point3D
Parameter 0=start, 1=end. PointAt/PointAtDistance extrapolate; ClosestPoint clamps to segment.
Reversed, Offset, Transformed, WithLength and Extended return new values.
- Vector() -> Vector3D
- Direction() -> Vector3D
- Length() -> float
- LengthSquared() -> float
- MidPoint() -> Point3D
- PointAt(parameter: float) -> Point3D
- PointAtDistance(distance: float) -> Point3D
- IsDegenerate(tolerance: float=kEpsilon) -> bool
- Reversed() -> Line3D
- Offset(offset: Vector3D) -> Line3D
- Transformed(transform: Transform3D) -> Line3D
- WithLength(length: float) -> Line3D
- Extended(atStart: float, atEnd: float) -> Line3D
- ProjectParameter(point: Point3D) -> float
- ProjectInfinite(point: Point3D) -> Point3D
- ClosestPoint(point: Point3D) -> Point3D
- DistanceTo(point: Point3D) -> float
- DistanceTo(other: Line3D) -> float
- DistanceToInfinite(point: Point3D) -> float
- IsPointOn(point: Point3D, tolerance: float=kEpsilon) -> bool
- IsPointOnInfinite(point: Point3D, tolerance: float=kEpsilon) -> bool
- IsParallel(other: Line3D, angleTolerance: float=kAngleEpsilon) -> bool
- IsPerpendicular(other: Line3D, angleTolerance: float=kAngleEpsilon) -> bool
- IsCollinear(other: Line3D, tolerance: float=kEpsilon) -> bool
- IntersectInfinite(other: Line3D, tolerance: float=kEpsilon) -> Point3D?
- Intersect(other: Line3D, tolerance: float=kEpsilon) -> Point3D?
- Intersects(other: Line3D, tolerance: float=kEpsilon) -> bool
- IsEqual(other: Line3D, tolerance: float=kEpsilon) -> bool
- IsEqualIgnoreDirection(other: Line3D, tolerance: float=kEpsilon) -> bool
Infinite intersection returns None for parallel, collinear, skew or degenerate lines.
Intersect returns a unique segment intersection, not an overlapping interval; Intersects includes collinear overlap.
DistanceTo(other) measures segment-to-segment distance, not infinite-line distance.

### Plane3D()
api.Math.Plane3D; Python-owned oriented infinite plane, default XY/+Z. All methods return values without mutation.
- FromPointNormal(origin: Point3D, normal: Vector3D) -> Plane3D? [s]
- FromPoints(first: Point3D, second: Point3D, third: Point3D) -> Plane3D? [s]
- GetOrigin() -> Point3D
- GetNormal() -> Vector3D
- SignedDistanceTo(point: Point3D) -> float
- DistanceTo(point: Point3D) -> float
- Project(point: Point3D) -> Point3D
- Mirror(point: Point3D) -> Point3D
- Contains(point: Point3D, tolerance: float=kEpsilon) -> bool
- Reversed() -> Plane3D
- Offset(distance: float) -> Plane3D
- IsParallel(other: Plane3D, angleTolerance: float=kAngleEpsilon) -> bool
- IsPerpendicular(other: Plane3D, angleTolerance: float=kAngleEpsilon) -> bool
- IsEqual(other: Plane3D, tolerance: float=kEpsilon, angleTolerance: float=kAngleEpsilon) -> bool
- IntersectInfinite(line: Line3D, angleTolerance: float=kAngleEpsilon) -> Point3D?
- Intersect(line: Line3D, tolerance: float=kEpsilon) -> Point3D?
- Intersect(other: Plane3D, angleTolerance: float=kAngleEpsilon) -> Line3D?
- Transformed(transform: Transform3D) -> Plane3D?
Factories return None for invalid/degenerate input; getters return origin and unit normal.
Reversed flips the positive side; Offset moves along the normal. IsEqual ignores normal orientation.
Coplanar non-degenerate segments return None; a point-segment on the plane returns its point.
Infinite intersection returns None for parallel/coplanar/zero-length lines.
Plane intersection returns a unit-length-direction line or None for parallel/coincident planes.
Transformed uses the inverse transpose and returns None for singular transforms or invalid output.

### api.Math functions and constants
constants: kPi=3.14159265358979323846, kTwoPi=2.0 * kPi, kHalfPi=0.5 * kPi, kEpsilon=1e-9, kAngleEpsilon=1e-9
- DegToRad(deg: float) -> float
- RadToDeg(rad: float) -> float
- IsZero(value: float, tolerance: float=kEpsilon) -> bool
- AreEqual(a: float, b: float, tolerance: float=kEpsilon) -> bool
- IsLess(a: float, b: float, tolerance: float=kEpsilon) -> bool
- IsGreater(a: float, b: float, tolerance: float=kEpsilon) -> bool
- IsBetween(v: float, lo: float, hi: float, tolerance: float=kEpsilon) -> bool
- Sign(v: float) -> float
- Clamp(v: float, lo: float, hi: float) -> float
- Lerp(a: float, b: float, t: float) -> float
- NormalizeAngle(angle: float) -> float  # Angle in [0, 2*pi)
- NormalizeAngleSigned(angle: float) -> float  # Angle in (-pi, pi]
- AngleDelta(from_: float, to: float) -> float  # Counter-clockwise angle from 'from' to 'to', in [0, 2*pi)
- AnglesAreEqual(a: float, b: float, tolerance: float=kAngleEpsilon) -> bool
aliases: Vector2D = Point2D, Vector3D = Point3D

### OffsetJoin
api.Math.OffsetJoin is an IntEnum: Miter=0, Round=1.

### ==== Scripting (script resource and palette management only) ====
Script execution is not possible through `api`. It exposes stored script text, language, resource identity, and palettes,
not an execution engine. `CScriptRunner`, `SScriptResult`, `EScriptStatus`, and `ScriptResource.Execute` are intentionally
absent from the Python module, even though the native C++ API supports execution. Creating a script resource or calling
`SetText` only stores source code; it never executes it. Bracket resource changes with the undo workflow in section 3.
To check this management-only contract, run the following read-only assertions inside Vectorworks:

```python
import api

for name in ("CScriptRunner", "SScriptResult", "EScriptStatus"):
    assert not hasattr(api, name), name
assert not hasattr(api.ScriptResource, "Execute")
for name in ("ScriptResource", "ScriptPalette", "ScriptLanguage"):
    assert hasattr(api, name), name
assert hasattr(api.ScriptResource, "SetText")
```

### ScriptResource(hScript: Handle)
Non-owning wrapper of a VectorScript or Python script resource; saved views are not script resources.
- Is(h: Handle) -> bool [s]
- FromName(name: str) -> ScriptResource [s]
- GetAll() -> [ScriptResource] [s]  # Sorted by name
- Create(name: str, paletteName: str, text: str, language: ScriptLanguage) -> ScriptResource [s]
- GetHandle() -> Handle
- IsValid() -> bool
- GetName() -> str?
- SetName(name: str) -> bool
- GetLanguage() -> ScriptLanguage?
- GetText() -> str?
- SetText(text: str) -> bool  # Keeps the language
- SetText(text: str, language: ScriptLanguage) -> bool
- GetPalette() -> ScriptPalette
- Delete(useUndo=True) -> bool

### ScriptPalette(hPalette: Handle)
Non-owning wrapper of a script palette; the Saved Views palette is not a script palette.
- Is(h: Handle) -> bool [s]
- FromName(name: str) -> ScriptPalette [s]
- GetAll() -> [ScriptPalette] [s]  # Sorted by name
- GetHandle() -> Handle
- IsValid() -> bool
- GetName() -> str?
- SetName(name: str) -> bool
- GetScripts() -> [ScriptResource]  # In palette order
- GetScriptCount() -> int
- SetOpen(isOpen: bool) -> bool
- Delete(useUndo=True) -> bool

### ==== Enumerations ====
IntEnum classes (members are ints; plain ints are accepted). Nested ones are attributes of their class.
PenStyleKind: None_ Solid Pattern SimpleLineType ComplexLineType Unknown
FillType: Unknown=-1 None_=1 Solid=2 Pattern=3 Hatch=4 Tile=5 Gradient=6 Image=7 Class=8
MarkerShape: Arrow=0 ConcaveCurvedArrow=1 Circle=2 DimSlash=3 DimCross=4 Lasso=5 Hexagon=6 VShaped=7 Cone=8 TaperedVShaped=9 SShaped=10 Rectangle=11 DoubleLine=12
MarkerFill: LineColor=0 White=128 NoFill=256
MarkerBase: Flat=0 Open=1024 Angle=2048 Arc=3072
MarkerHalfTick: Full=0 Left=16384 Right=24576
MarkerThicknessBasis: LineThickness=0 DimThickness=1 Custom=2
MarkerThicknessUnits: Mils=0 Points=16 Millimeters=32
DropShadowUnits: Page=0 World=1
ClassVisibility: Invisible=-1 Visible=0 Grayed=2
ObjectType: Invalid=-1 Term=0 Line=2 Box=3 Oval=4 Polygon=5 Arc=6 DimUnitSettings=7 FreehandPolygon=8 Locus3D=9 Text=10 Group=11 QuarterArc=12 RoundedRectangle=13 Paint=14 Symbol=15 SymbolDefinition=16 Locus=17 Worksheet=18 BuildingMaterial=19 Polyline=21 Extrude=24 Polygon3D=25 SlabDrain=26 SlabDrainValley=27 SlabSlopeValley=28 LayerReference=29 DashPatterns=30 Layer=31 Header=32 RefList=33 Sweep=34 ClassList=35 ViewportStyle=36 DataVisualization=37 MultiExtrude=38 DimensionStandard=39 Mesh=40 SavedView=43 RenderSpec=44 Eps=45 Format=47 Record=48 ToolCommand=49 SymbolList=54 WorksheetImage=56 Data=57 RecordLink=58 WorksheetDatabase=60 LeaderList=62 Dimension=63 HatchContainer=65 HatchDefinition=66 Bsp=67 Wall=68 InnerLines=69 SlabDrainageSettings=70 Slab=71 PenSpace=73 FontTable=74 StyleRun=75 UserData=76 WorkingPlane=77 WPlaneList=78 PixelPatternList=79 ColorPalette=80 Light=81 RoofEdge=82 RoofContainer=83 CSGTree=84 BoundaryRep=85 Parametric=86 RoofAdorner=87 Subscribe=88 ObsoleteRoundWall=89 UndoPlaceholder=90 TextureSpace=91 Folder=92 TextureBitmap=93 ClassDefinition=94 Solid=95 LineTypeDefinition=96 Texture=97 ADSymbolDefinitionHandler=98 ADSymbolHandler=99 SlabEdge=100 DropShadow=101 RoofStyle=102 CurtainWallFrame=103 CurtainWallPanel=104 CurtainWallGrid=105 RenderStyle=106 SlabStyle=107 TileDefinition=108 TextStyle=109 Constraint=110 PieceWiseNurbsCurve=111 CorePrintInfo=112 NurbsSurface=113 CompositeSurface=114 RenderBackground=115 PolyBreak=116 BatchRenderJob=117 BatchRenderJobList=118 ImageDefinition=119 GradientDefinition=120 FillSpace=121 Viewport=122 ArtRWStyle=123 Association=124 AuxMarker=125 GeoReference=126 WallStyle=127
VertexType: Corner=0; Bezier=1 (quadratic bezier control point); Cubic=2 (cubic spline control point); Arc=3 (arc control point with radius (0 = maximum...); Radius=4 (radius (tangent) control point)
Traverse: Selected=0 (selected visible objects on working layers); Editable=1 (unlocked objects on editable layers); Visible=2 (visible layers/classes); Drawing=3 (drawing layers, excluding resources); SymbolDefinitions=4 (symbol definitions and their contents); SelectedAndEditable=5 (selected AND visible AND unlocked on editable layers); All=6 (all drawing objects plus symbol definitions and contents); AllAndResources=7 (all drawing objects and resource objects)
Descend (IntFlag, combine with |): None_=0 (top level only); Groups=32 (groups); All=64 (all container kinds); Viewports=128 (viewports); AuxiliaryLists=256 (auxiliary objects attached to visited objects)
LayerType: Unknown=0; Design=1 (a world coordinate design layer (regular...); Sheet=2 (a sheet layer (a printable page, holds...); GuestDesign=3 (a design layer imported/referenced from another...)
LayerVisibility: Invisible=-1 (hidden); Normal=0 (shown normally); Grayed=2 (shown, but drawn in gray to indicate it is not...)
VisibilityOptions: ActiveOnly=1 (show only the active layer/class); GrayOthers=2 (show others grayed out (not editable, not...); ShowOthers=3 (show others normally (visible, but not...); ShowSnapOthers=4 (show others normally and allow snapping to them...); ShowSnapModifyOthers=5 (show others normally, allow snapping and...); GraySnapOthers=6 (show others grayed but allow snapping to them)
StoryElevationChangeMode: Single=0 (only this story); CurrentAndAbove=1 (and every story above); CurrentAndBelow=2 (and every story below); All=3 (every story)
UndoMethod: None_=0 (disables undo and clears the undo table for the...); ReplaceSelection=17 (remembers the current selection; Undo restores...); SwapObjects=21 (object level undo: register the objects you...)
AngularUnit: Degrees=0 Radians=1 Gradians=2
TextJustification: Left=1 Center=2 Right=3
TextVerticalAlignment: TopOfBox=1 TopBaseline=2 CenterOfBox=3 BottomBaseline=4 BottomOfBox=5
TextLineSpacing: Custom=0 (see TextDefaults.GetLeading); Single=2; OneAndHalf=3; Double=4
ToolKind: Unknown=0; InternalClassic=1 (built into the core as a classic tool definition); InternalExtension=2 (built into the core as a VCOM IExtensionTool...); ScriptPlugin=3 (VectorScript / Python plug-in tool); ExtensionPlugin=4 (external VCOM IExtensionTool implementation...)
ToolCreationType: Normal=0 (a regular tool (custom click handling)); Point=1 (one click places a point object); Line=2 (two clicks define a line-like object); Box=3 (two clicks define a rectangle-like object); Path2D=4 (clicks define a 2D path object); Path3D=5 (clicks define a 3D path object); Custom=6 (custom object creation)
ToolFilter: All=0 (every tool installed in Vectorworks, including...); Activatable=1 (only tools that ActivateTool can activate now); InWorkspace=2 (only tools placed in the tool palettes of the...)
ModeType: Radio=0 (group of mutually exclusive buttons; exactly...); Button=1 (push button that performs an action (may show...); Toggle=2 (on/off button); PullDown=3 (pull-down menu with a fixed list of items); EditText=4 (labelled edit field); ResourcePopup=5 (resource pop-up (symbols, styles, textures...); SearchablePullDown=6 (pull-down with search, items identified by name...); ComboBox=7 (edit field with a list of suggested items)
ModeButtonKind: Radio=0; Button=1; Preferences=2 (opens the tool preferences dialog box); Check=3 (toggle button); EditText=4; PullDown=5
ToolKey: Return=0 (completes the action of tools that finish on...); Escape=1 (removes all tool points; with no tool points it...); Backspace=2 (removes the last tool point)
MenuCommandKind: Unknown=0; Internal=1 (built into the core; the universal name is a...); ScriptPlugin=2 (VectorScript / Python plug-in menu command...); ExtensionPlugin=3 (VCOM IExtensionMenu implementation from a...)
MenuChunkKind: None_=0 (not a chunk: a normal command); Regular=1 (a fixed list of items); Dynamic=2 (items built when the menu bar is built); Variable=3 (items that change while Vectorworks runs)
MenuFilter: All=0 (every menu command installed in Vectorworks...); Executable=1 (only commands whose fIsEnabled is set); InWorkspace=2 (only commands placed in the current workspace)
MenuEntryType: Command=0 (a normal command); ChunkItem=1 (one item of a chunk); Submenu=2 (opens a submenu; its entries follow it); Separator=3 (a separator line)
MenuStatus: Ready=0 (ExecuteMenu can run it now); Unavailable=1 (no menu bar, or plug-in objects regenerating); NotFound=2 (no installed menu command has this name); NotInWorkspace=3 (not placed in the menus of the current workspace); Disabled=4 (disabled in the current state); ChunkItemRequired=5 (a chunk with several items: pass an item); ChunkItemNotFound=6 (no such chunk item, or not a chunk)
OIPPane: Shape=0 (geometric and parametric properties); Data=1 (records and other attached data); Render=2 (textures)
OIPControlType: EditText=0 (edit field, possibly read only); StaticText=1 (label or separator); CheckBox=2 (on/off check box); RadioGroup=3 (radio or push buttons; exactly one is selected); PullDown=4 (pull-down with a fixed list of items); SearchablePullDown=5 (pull-down with search); Button=6 (push button that performs an action); ClassPullDown=7 (the class pull-down); LayerPullDown=8 (the layer pull-down); Other=9 (any other control; see OIPAccess.NotifyChanged)
ResourceType: Unknown=0 (the object is not a resource); SymbolDefinition=16 (reusable object template; instances of it are...); Worksheet=18 (spreadsheet / report); BuildingMaterial=19 (material of a wall, slab or roof component); ViewportStyle=36; DataVisualization=37 (rule based graphic override of a viewport /...); RecordFormat=47 (data record definition (the format attached to...); Hatch=66 (vector hatch fill); Folder=92 (resource folder grouping other resources in the...); Class=94 (class definition (see ClassAttributes for its...); LineType=96 (simple or complex line type (dashed / patterned...); Texture=97 (texture); RoofStyle=102; RenderStyle=106 (render style); SlabStyle=107; Tile=108 (tile fill); TextStyle=109; RenderBackground=115 (Renderworks background); ImageFill=119 (image definition used as an image fill / image...); Gradient=120 (gradient fill); WallStyle=127
ContentFolder: None_=0 (no library folder: the current drawing only); ObjectLibraries=11; Libraries=13; Defaults=14; Textures=100; Gradients=103; Hatches=105; ImageFills=106; PlantStyles=107; RenderBackgrounds=109; TitleBlocks=115; Reports=120; SketchStyles=134; Tiles=163; TextStyles=164; RenderStyles=171; LineTypes=174; RecordFormats=197; ObjectStyles=217; Materials=345; WallStyles=393; RoofStyles=394; SlabStyles=395; PlantLibraries=399
ImportConflict: DoNotImport=0 (keep the existing resource, import nothing); Replace=1 (overwrite the existing resource); Rename=2 (import under a new, unique name); AskWithUI=3 (show the standard Vectorworks conflict dialog...)
ImageFill.Compression: None_=0 Jpeg=1 Png=2 PngMonochrome=3
RecordFieldType: Unknown=0; Integer=1; Boolean=2; Real=3; Text=4; Dimension=7 (a length, shown in the document units); PopUp=8 (text with a list of predefined choices); Radio=9; CoordLocX=10 (plug-in parameter only); CoordLocY=11 (plug-in parameter only); StaticText=14 (label, not editable on the object); ControlPoint=15; DimStdPopUp=16 (plug-in parameter only); PrecisionPopUp=17 (plug-in parameter only); ClassPopUp=18; LayerPopUp=19; Angle=20; Area=21; Volume=22; Class=23 (internal index of a class); BuildingMaterial=24 (internal index of a material); Fill=25; PenStyle=26; PenWeight=27; Color=28; Texture=29 (internal index of a texture); SymbolDefinition=30 (internal index of a symbol definition)
Texture.Part: Overall (the whole object); ExtrudeTop (extrudes and sweeps); ExtrudeBottom (extrudes and sweeps); ExtrudeSides (extrudes and sweeps); WallLeft (walls); WallRight (walls); WallTop (walls); WallBottom (walls); SlabTop (slabs); SlabBottom (slabs); SlabSides (slabs); RoofTop (roofs); RoofBottom (roofs); RoofSides (roofs)
RenderBackground.Kind: Clouds OneColor TwoColor PhysicalSky
SymbolDefinition.GeometryType: Unknown=0 TwoD=1 ThreeD=2 Hybrid=3
SymbolDefinition.InsertMode: Edge Center LeftEdge RightEdge CoreComponentCenter CoreComponentLeftEdge CoreComponentRightEdge WallInsertLocation WallClosureInsertLocation
SymbolDefinition.BreakMode: FullWithCaps FullNoCaps Half None_
DataTagObject.LeaderType: Line Arc Bezier
DataTagObject.HorizontalPosition: Left Right Auto
DataTagObject.MoveBehaviour: EntireTag LeaderEnd
DimensionKind: Unknown=-1; ConstrainedLinear=0 (fix_ang); UnconstrainedLinear=1 (sloped); Ordinate=2; Radial=3 (radius of a circle / arc); Diametrical=4 (diameter of a circle / arc); Angular=5 (angle between two legs around a vertex); ArcLength=6 (length along an arc)
DimensionTolerance: None_=0; Single=1 (one +/- value); Double=2 (separate plus and minus values); Limit=3 (upper and lower limit instead of the nominal...)
WallObject.BoundStatus: Missing Unresolved Invalid Valid
WallObject.BoundKind: Unknown LayerElevation LayerWallHeight Story
RoofObject.MiterType: Vertical=1 (vertical intersection); Horizontal=2 (horizontal intersection); Double=3 (double miter (intersection has both a vertical...)
PlantObject.Config: SinglePlant PlantsAtPolyVertices PlantsAlongPolyEdges PlantsInRectangularArray PlantsInTriangularArray
PlantObject.TagDisplay: None_ Left Right Floating
LandscapeAreaObject.DrawingMode: LandscapeArea Hedgerow
LandscapeAreaObject.AreaUnits: SqFeet SqMeters Acres Hectares DocumentUnits
SiteModelObject.Display2D: ExistingOnly ProposedOnly ExistingAndProposed
SiteModelObject.Display3D: Nothing ExistingOnly ProposedOnly CutAndFill
SiteModifierObject.Config: GradeLimits (closed fence limiting how far the modification...); Contour (contour line at a fixed elevation); Pad (flat pad at a target elevation); RetainingPad (pad with a retaining edge); Aligned (aligned surface using per-side elevations and...); Path (path with a longitudinal profile); FitToObjects (interpolates from the elevation of the objects...); TextureBed (3D texture bed (no elevation change)); SpoilPile (piles material at a slope until it reaches a...)
SiteModifierObject.ApplyTo: Existing Proposed
StakeObject.Mode: SiteModelSource ("Include as site model data" - the stake's Z is...); SetToSiteModelGrade ("Set elev to site model grade"); SetToCutSurface ("Set elev to site model cut surface"); SetToObjectSpot ("Set elev to object spot"); Graphic2DOnly ("Use as 2D graphic only"); SiteModifierObject ("Site modifier object")
StakeObject.SiteModel: Existing Proposed
LandscapeAreaObject.PlantDisplay2D: None_ PlantCloud PlantLine PlantSymbols
HardscapeObject.Mode3D: None_=0 Slab=1 PadUnder=2 PadOver=3 TextureBed=4 SlabDrainage=5 AlignedSlab=6 AlignedModifOver=7 AlignedModifUnder=8
PropertyLineObject.AreaUnits: DocumentUnits SquareFeet SquareYards SquareMiles Acres SquareMeters SquareKilometers Hectares
ExistingTreeObject.Origin: NotSet Endemic Native Exotic Indigenous Custom
ExistingTreeObject.TreeProtection: None_ CircularZone Using12DBH
ExistingTreeObject.Condition: NotSet Excellent Good Average Poor Custom
ExistingTreeObject.SULE: NotSet Long Medium Short Removal Custom
ExistingTreeObject.Significance: NotSet MostSignificant HighlySignificant LessSignificant LeastSignificant Hazardous Custom
ExistingTreeObject.Action: NotSet Retain RetainArborist TransplantOriginal TransplantProposed Remove RemoveBuildingFootprint RemovePoorHealth RemoveSpecies Custom
ScriptLanguage: VectorScript=0 Python=1

### ==== Native 3D objects (Objects3D) ====

### SweepObject(h: Handle) : PrimitiveObject +Is +Duplicate

Native sweep; all factories COPY inputs. Profile X radial, Y axial; local Y axis. At angle 0 radial +Z,
positive towards +X. Optional single 2D axis locus in profiles, otherwise axis at left edge.
Angles radians; pitch mm/full turn. At least one native 2D profile.

- Create(profile: Handle) -> SweepObject [s]
- Create(profile: Handle, values: SweepObject.Values) -> SweepObject [s]
- Create(profiles: [Handle], values: SweepObject.Values) -> SweepObject [s]
- AreValidValues(values: SweepObject.Values) -> bool [s]
- GetSweepValues() -> SweepObject.Values?
- SetSweepValues(values: SweepObject.Values) -> bool
- GetProfiles() -> [Handle]

GetProfiles returns non-owning copied child handles; Reset after editing. Factories return falsy wrapper on failure.

### SweepObject.Values()
fields: startAngle: float=0, sweepAngle: float=2*pi, incrementAngle: float=pi/36, pitch: float=0.
Finite values; sweepAngle != 0, incrementAngle > 0; sign of sweepAngle determines direction.
Segment ratio abs(sweepAngle)/incrementAngle <= 3600, checked in degrees; conversions and total travel must stay finite.

### MultiExtrudeObject(h: Handle) : PrimitiveObject +Is +Duplicate

Native multiple extrude; copies >=2 native 2D profiles in order, evenly spaced between base and base+thickness.
Local dimensions mm; finite nonzero signed thickness, finite distinct top elevation.
- Create(profiles: [Handle], baseElevation: float, thickness: float) -> MultiExtrudeObject [s]
- GetExtrudeValues() -> ExtrudeObject.Values?
- SetExtrudeValues(baseElevation: float, thickness: float) -> bool
- GetProfiles() -> [Handle]
No separate MultiExtrudeObject.Values type. Child handles non-owning; Reset after editing.

### SurfaceModelObject(h: Handle) : PrimitiveObject +Is +Duplicate

Shared RESULT-SHAPE wrapper, not feature provenance: NURBS surface, CSG solid/sheet, or nonempty recursively
compatible group. No editable loft/revolve/path feature history. All factories copy inputs, leave originals
in place on success/failure, insert one result in current container; falsy wrapper on failure (logged).
Handle arguments and lists accept wrappers. Lengths mm; angles radians.

- CreateLoft(sections: [Handle], ruled=False, closed=False, solid=False) -> SurfaceModelObject [s]
- CreateRailSweep(sections: [Handle], rail: Handle, secondRail: Handle=None, solid=False) -> SurfaceModelObject [s]
- CreateRevolve(profile: Handle, values: SweepObject.Values=SweepObject.Values()) -> SurfaceModelObject [s]
- CreateRevolveWithRail(profile: Handle, rail: Handle, axis: Handle) -> SurfaceModelObject [s]
- CreateExtrudeAlongPath(path: Handle, profile: Handle) -> SurfaceModelObject [s]
- CreateExtrudeAlongPath(path: Handle, profile: Handle, options: SurfaceModelObject.PathOptions) -> SurfaceModelObject [s]
- CreateTaperedExtrude(profile: Handle, angle: float, height: float) -> SurfaceModelObject [s]
- CreateCylinder(baseCenter: Point3D, radius: float, height: float) -> ExtrudeObject [s]
- CreateBox(minimum: Point3D, maximum: Point3D) -> ExtrudeObject [s]
- CreateTorus(center: Point3D, majorRadius: float, minorRadius: float) -> SweepObject [s]

Loft: >=2 ordered NURBS curves/3D loci with >=1 curve; closed needs >=3, joins last to first; ruled uses ruled spans.
Rail sweep: >=1 NURBS section, one/two NURBS rails. solid=True requests caps/sewing, fails unless closed solid
(never silently returns surface group). Revolve uses SweepObject convention then converts to NURBS.
Rail-guided revolve requires linear axis; Core validates compatibility. Path must be NURBS;
default PathOptions below; path/taper results are history-free CSG solids/sheets.
Taper abs(angle)<pi/2, finite nonzero signed height. Cylinder radius>0, signed nonzero height, world Z axis.
Box maximum>minimum on every axis. Torus majorRadius>minorRadius>0, world Z axis. Dimensions finite.
Primitive helpers return ExtrudeObject/SweepObject, NOT SurfaceModelObject.

### SurfaceModelObject.PathOptions()
fields: isExponentialScale: bool=False, scale: float=1, isProfilePlaneLocked: bool=False, isProfileFixed: bool=False.
scale positive finite; switches select exponential scaling, locked profile plane and fixed supplied placement.
See [modeling factories](Objects3D.md#surfacemodelobject) for full contracts and an undo-safe example.

### ExtrudeObject(h: Handle) : PrimitiveObject +Is +Duplicate
Native extrude (`ObjectType.Extrude`), not a plug-in object. Inherits identity, class, graphical attributes,
hierarchy, selection, visibility, locking, 2D transformations, bounds, reset and deletion from `PrimitiveObject`.
`Document.As(ExtrudeObject, h)`, `GetObjectsOf` and `GetSelectionOf` work as for the other typed wrappers.
Constructing a wrapper never converts or modifies its existing profile.

Lengths are world units (millimetres), volume is world units cubed. `baseElevation`, `topElevation`, `thickness`
and profile XY coordinates are LOCAL to the extrude. `topElevation = baseElevation + thickness`; after a rotation
these are not world Z coordinates. Thickness may be negative, but must be finite, nonzero, and produce a finite,
distinct top elevation. Dimension setters reset the object; setting base elevation preserves thickness, while setting
thickness or top elevation preserves base elevation.

Creation returns a falsy wrapper on failure. `Create` accepts native 2D line, rectangle, oval, arc, rounded rectangle,
polygon/freehand polygon or polyline handles. Polygon values preserve curved vertices, edge visibility and closure;
open profiles can produce surfaces. `CreatePlanar` accepts at least three finite, non-collinear, coplanar 3D points
(planarity tolerance `api.Math.kEpsilon`); it derives the placement plane using the VWFC convention. `CreateBetween`
places the local origin at `start`, the base at local Z=0, and the top at `end`. Its local +Z axis follows `end-start`.
With an explicit `up`, local +Y is the projection of `up` into the profile plane; a zero/parallel vector or coincident
endpoints fails without consuming the input. Without `up`, world +Z is the reference, or world +Y for near-vertical
directions (including negative Z).

Handle ownership:
- `Create(hProfile, ...)` and `SetBaseObject` move the profile into the extrude on success. `keepOriginal=True` uses
  a duplicate instead. Failure leaves the caller's profile untouched.
- `GetBaseObject`, `GetHoleObject` and `GetHoleObjects` return non-owning handles, not copies. Wrap them with
  `PolygonObject`/`PolylineObject` (or the matching primitive wrapper) to edit vertices, then call the extrude's `Reset()`.
- `SetBaseObject`/`SetBasePolygon` replace the old profile AND its holes, invalidating handles to that geometry.
  `GetBasePolygon` returns only the outer boundary as a value; for non-poly profiles it converts a temporary copy,
  never the original. Read holes separately.
- `AddHoleObject` requires a closed profile. It converts a copy into a polyline hole and consumes/deletes the input
  on success unless `keepOriginal=True`. Adding a hole can convert the outer profile into a polyline; re-fetch the
  base handle afterwards. Hole coordinates are local XY, not world coordinates. Choose holes inside the boundary
  and avoid intersecting holes. Removal invalidates the removed hole handles.
- New value-based profiles and failed creation temporaries are cleaned up. Deleting an extrude deletes its profile
  and holes. A wrapper does not own or keep its drawing object alive.

`Transform` stores the origin and local X/Y/Z axes (`uAxis`, `vAxis`, `wAxis`) in the parent coordinate system.
`SetTransform` replaces placement, accepting finite orthonormal axes (unit-length and perpendicular within `1e-8`,
including mirrored bases); scaling/shearing matrices are rejected. Use dimensions or profile edits to resize.
`Move3D` translates in parent coordinates. All successful setters/actions reset the extrude.

- Create(hProfile: Handle, baseElevation: float, thickness: float, keepOriginal=False) -> ExtrudeObject [s]
- Create(profile: Polygon2D, thickness: float) -> ExtrudeObject [s]  # baseElevation=0
- Create(profile: Polygon2D, baseElevation: float, thickness: float) -> ExtrudeObject [s]
- Create(points: [Point2D], baseElevation: float, thickness: float, closed=True) -> ExtrudeObject [s]
- Create(rect: Rect2D, baseElevation: float, thickness: float) -> ExtrudeObject [s]
- CreatePlanar(points: [Point3D], thickness: float) -> ExtrudeObject [s]
- CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, keepOriginal=False) -> ExtrudeObject [s]
- CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, up: Point3D, keepOriginal=False) -> ExtrudeObject [s]
- GetExtrudeValues() -> ExtrudeObject.Values?
- SetExtrudeValues(baseElevation: float, thickness: float) -> bool
- SetExtrudeValues(values: ExtrudeObject.Values) -> bool
- GetBaseElevation() -> float?
- SetBaseElevation(baseElevation: float) -> bool
- GetThickness() -> float?
- SetThickness(thickness: float) -> bool
- GetTopElevation() -> float?
- SetTopElevation(topElevation: float) -> bool
- GetBaseObject() -> Handle
- SetBaseObject(hProfile: Handle, keepOriginal=False) -> bool
- GetBasePolygon() -> Polygon2D?
- SetBasePolygon(profile: Polygon2D) -> bool
- GetHoleObjects() -> [Handle]
- GetHoleCount() -> int
- GetHoleObject(index: int) -> Handle  # null handle when out of range
- AddHoleObject(hProfile: Handle, keepOriginal=False) -> bool
- AddHoleObject(profile: Polygon2D) -> bool
- RemoveHole(index: int) -> bool
- RemoveAllHoles() -> bool
- GetTransform() -> ExtrudeObject.Transform?
- SetTransform(transform: ExtrudeObject.Transform) -> bool
- Move3D(offset: Point3D) -> bool
- GetVolume() -> float?

### ExtrudeObject.Values()
fields: baseElevation: float=0, thickness: float=0

### ExtrudeObject.Transform()
fields: origin: Point3D=(0,0,0), uAxis: Point3D=(1,0,0), vAxis: Point3D=(0,1,0), wAxis: Point3D=(0,0,1)

### Extrude example / regression checks
Run inside Vectorworks with an open disposable drawing after building the updated application. This example
creates and deletes its geometry. It has not been executed as part of the no-C++-build implementation checks.

```python
import math
import api
from api.Math import Polygon2D, Rect2D

assert api.Document.IsOpen()
extrude = api.ExtrudeObject.Create(rect=Rect2D(0, 1000, 1000, 0),
                                  baseElevation=100, thickness=500)
assert extrude
try:
    assert api.ExtrudeObject.Is(extrude.GetHandle())
    assert api.Document.As(api.ExtrudeObject, extrude.GetHandle())
    assert extrude.GetBaseElevation() == 100
    assert extrude.GetTopElevation() == 600
    assert math.isclose(extrude.GetVolume(), 1000 * 1000 * 500, rel_tol=1e-8)
    assert extrude.SetBaseElevation(200)
    assert extrude.GetThickness() == 500 and extrude.GetTopElevation() == 700
    values = extrude.GetExtrudeValues()
    values.thickness = 600
    assert extrude.SetExtrudeValues(values)
    assert extrude.SetTopElevation(1000)
    assert extrude.GetThickness() == 800
    assert not extrude.SetThickness(0)
    assert not extrude.SetThickness(float("nan"))
    assert extrude.GetThickness() == 800

    hole = Polygon2D.FromRect(Rect2D(200, 400, 400, 200))
    assert extrude.AddHoleObject(profile=hole)
    assert extrude.GetHoleCount() == 1
    assert extrude.GetHoleObject(0) and not extrude.GetHoleObject(1)
    assert math.isclose(extrude.GetVolume(), (1000**2 - 200**2) * 800, rel_tol=1e-8)
    assert extrude.RemoveHole(0) and not extrude.RemoveHole(0)
    assert extrude.RemoveAllHoles()
    assert extrude.GetHoleCount() == 0

    placement = extrude.GetTransform()
    placement.origin = api.Point3D(x=10, y=20, z=30)
    assert extrude.SetTransform(placement)
    assert extrude.Move3D(api.Point3D(x=0, y=0, z=70))
    assert math.isclose(extrude.GetTransform().origin.z, 100, abs_tol=1e-8)
    placement.uAxis = api.Point3D(x=2, y=0, z=0)
    assert not extrude.SetTransform(placement)

    copy = extrude.Duplicate()
    assert copy and copy.GetHandle() != extrude.GetHandle()
    assert copy.Delete(useUndo=False)
finally:
    assert extrude.Delete(useUndo=False)

invalid = api.ExtrudeObject(None)
assert not invalid and invalid.GetExtrudeValues() is None
assert invalid.GetTransform() is None and invalid.GetVolume() is None
assert not invalid.SetThickness(10) and not invalid.RemoveHole(0)
assert invalid.GetHoleObjects() == []
```

Additional manual coverage: every creation overload (including curved/open profiles and negative thickness);
planar 3D boundaries in horizontal/vertical/oblique planes and rejection of non-planar/collinear inputs; directed
extrudes along +Z, -Z and oblique directions with/without `up`; zero/parallel/nonfinite directions; profile and hole
handle ownership with both `keepOriginal` settings; non-destructive wrapping/reading of rectangle/circle profiles;
hole insertion on a non-poly outer profile; profile replacement clearing holes; editing a returned profile/hole
followed by `Reset`; mirrored placements; selection/type filtering; document undo/redo and inherited attributes.

### GenericSolidObject(h: Handle) : PrimitiveObject +Is +Duplicate

Non-owning wrapper for native CSG nodes (`kCSGTreeNode`), including solid additions, solid subtractions,
solid intersections and flattened generic solids. Wrapping does not alter the document. Native solids have no
plug-in parameter record: dimensions are derived from the retained primitives, not independent width/height
fields on the solid. Inherited name, class, attributes, visibility, hierarchy and 2D transforms remain available.

**History is the document's native construction tree, not a Python-side log.** Boolean creation retains the blank
(operand 0) followed by the tool(s), recursively retaining earlier solids and their primitives. A solid created
from one primitive is a one-operand union, so the primitive remains editable. `Create` on an existing CSG node
duplicates its actual tree when `keepOriginal=True`; otherwise it wraps that same node.

In native terminology a flattened **generic solid has NO editable history** (action 26, also used for imported
solids). `Is(h)` accepts all CSG nodes; `IsGenericSolid(h)` identifies only this history-free case.
`ClearHistory()` explicitly invokes that destructive native conversion; no automatic flattening occurs during
creation or Boolean modeling. `HasHistory()` then returns `False`, `GetOperation()` returns `None`,
`GetOperands()` is empty, and `GetHistory()` contains only the root. History cannot be restored by this API.

**Ownership and failure conventions**
- Factories default to `keepOriginal=True`: copies are used and the input objects remain independent.
  With `False`, successful `Create`/Boolean creation moves the supplied primitives into the result's history.
  Such handles remain valid but are now owned by that solid; do not delete them independently. On failure the
  supplied inputs are preserved. The profile-based extrude factories always stage a profile copy, and delete
  the original profile only after success when `keepOriginal=False`.
- Native two-input Boolean results are inserted into the active container, as for the SDK Boolean commands;
  `Create` from a single primitive inserts next to that primitive. Inputs in different containers must already
  use compatible native coordinates; the wrapper does not convert between container coordinate systems.
- `SetOperand` always copies its argument. It and `SetOperation` edit only Boolean nodes, rebuild the result,
  and restore the old operand/operation on kernel failure (including an empty result). Root handles remain stable.
  A successful operand replacement deletes the previous operand and its descendants: reacquire history handles.
  A supplied argument that is itself in the replaced subtree is also invalidated when that old subtree is deleted.
- Identical/ancestor-related Boolean inputs, invalid handles, invalid operations and unsupported/locked source
  primitives are rejected. Kernel failures return a falsy wrapper or `False`; check results.
- `GetOperands` and `GetHistory` return non-owning handles, not detached geometry or a replay recipe. Primitive
  parameters can be edited using `ExtrudeObject(step.object)` (or the appropriate existing wrapper). Call
  **`Rebuild()` on the outermost solid** after batching edits: inherited `Reset()` refreshes CSG bounds but is
  not a solid-history regeneration. Failed `Rebuild()` leaves those external primitive edits in place for repair.
- Non-Boolean features (fillet, chamfer, shell, section, etc.) can be read in existing history and participate as
  solid operands. This wrapper does not add setters for their feature-specific parameters.
- `ClearHistory()` rejects failed solids and deletes all history handles below that node. Work on `Duplicate()`
  first if the construction history must be retained. Do not use other wrappers to deleted operands.

`GetTransform`/`SetTransform` reuse **`ExtrudeObject.Transform`**, already exported by the 3D API.
Placement uses orthonormal axes and an origin in parent coordinates (mirrored bases are allowed).
Scale is stored separately: `SetScale` sets absolute, nonzero X/Y/Z factors about the native scale center,
not an additional relative scale; negative factors mirror, and native kernel limits apply.
Surface area is in world units squared, volume in world units cubed. Bounds come from the inherited
`PrimitiveObject.GetBounds3D`/`GetCenter3D`/`GetSize3D` (axis-aligned, not local-space dimension setters).

- Is(h: Handle) -> bool [s]
- IsGenericSolid(h: Handle) -> bool [s]
- Create(hSolid: Handle, keepOriginal=True) -> GenericSolidObject [s]
- CreateBoolean(operation: Operation, hBlank: Handle, hTool: Handle, keepOriginal=True) -> GenericSolidObject [s]
- CreateUnion(hBlank: Handle, hTool: Handle, keepOriginal=True) -> GenericSolidObject [s]
- CreateIntersection(hBlank: Handle, hTool: Handle, keepOriginal=True) -> GenericSolidObject [s]
- CreateDifference(hBlank: Handle, hTool: Handle, keepOriginal=True) -> GenericSolidObject [s]  # blank minus tool
- CreateFromExtrude(hProfile: Handle, baseElevation: float, thickness: float, keepOriginal=True) -> GenericSolidObject [s]
- CreateFromExtrude(profile: Polygon2D, baseElevation: float, thickness: float) -> GenericSolidObject [s]
- CreateFromExtrude(rect: Rect2D, baseElevation: float, thickness: float) -> GenericSolidObject [s]
- CreateFromExtrude(points: [Point2D], baseElevation: float, thickness: float, closed=True) -> GenericSolidObject [s]
- CreatePlanar(points: [Point3D], thickness: float) -> GenericSolidObject [s]
- CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, keepOriginal=True) -> GenericSolidObject [s]
- CreateBetween(hProfile: Handle, start: Point3D, end: Point3D, up: Point3D, keepOriginal=True) -> GenericSolidObject [s]
- CanConvertToGenericSolid(h: Handle) -> bool [s]  # CSG, extrude, sweep, mesh, primitive, closed 3D polygon (>= 3 vertices), wall, ...
- ConvertToGenericSolid(hObject: Handle, keepOriginal=True) -> GenericSolidObject [s]  # history-free, next to the source (VectorScript ConvertToGenericSolid); works on a copy, False deletes the source on success
- GetAction() -> int?  # raw native action: 1 union, 2 intersection, 3 difference, 4/5/6 failed Boolean, 26 generic solid
- GetOperation() -> Operation?  # Boolean operation, including its failed native variant; None for other actions
- HasHistory() -> bool?
- SetOperation(operation: Operation) -> bool
- GetOperands() -> [Handle]  # ordered immediate children; excludes terminators/undo placeholders
- GetOperandCount() -> int
- GetOperand(index: int) -> Handle  # null for an out-of-range index
- SetOperand(index: int, hSolid: Handle) -> bool
- GetHistory() -> [HistoryStep]  # preorder: root, then each ordered operand subtree; invalid wrapper returns []
- Rebuild() -> bool  # False for invalid or history-free solids, or a failed native rebuild
- ClearHistory() -> bool
- GetTransform() -> ExtrudeObject.Transform?
- SetTransform(transform: ExtrudeObject.Transform) -> bool
- GetScale() -> Point3D?
- SetScale(scale: Point3D) -> bool
- Move3D(offset: Point3D) -> bool
- GetVolume() -> float?
- GetSurfaceArea() -> float?
- ConvertToMesh(keepOriginal=True) -> MeshObject  # tessellated, no history; False deletes the solid

### GenericSolidObject.Operation
`Union`, `Intersection`, `Difference`. Use the enum, not raw native action numbers, as operation arguments.

### GenericSolidObject.HistoryStep()
fields: object: Handle, parent: Handle, operandIndex: int, depth: int, action: int, operation: Operation?,
hasHistory: bool

Root: null `parent`, `depth=0`. Each child identifies its parent node and 0-based operand position.
Primitive leaves use `action=-1`, `operation=None`, `hasHistory=False`; a generic solid leaf uses `action=26`.
Extrudes are leaves here: use `ExtrudeObject` for their profile, holes, signed thickness and placement.
Other native CSG features preserve their raw action and ordered children; `operation` is `None` for those features.
Changing these returned value records does not edit the document.

### Solid example / regression checks
Run in Vectorworks with an open disposable drawing after building the updated application. This script
creates and deletes its own objects. Geometry checks have **not** been run as part of the no-C++-build checks.

```python
import math
import api
from api.Math import Rect2D

Solid = api.GenericSolidObject
Op = Solid.Operation
assert api.Document.IsOpen()
created = []

def track(obj):
    assert obj
    created.append(obj)
    return obj

def volume(obj, expected):
    assert math.isclose(obj.GetVolume(), expected, rel_tol=1e-8)

try:
    a = track(api.ExtrudeObject.Create(Rect2D(0, 1000, 1000, 0), 0, 1000))
    b = track(api.ExtrudeObject.Create(Rect2D(500, 1000, 1500, 0), 0, 1000))
    solid = track(Solid.CreateUnion(a, b))
    volume(solid, 1.5e9)
    volume(a, 1e9)  # default keepOriginal=True
    assert Solid.Is(solid) and not Solid.IsGenericSolid(solid)
    assert api.Document.As(Solid, solid.GetHandle())
    assert solid.GetOperation() == Op.Union and solid.HasHistory()
    history = solid.GetHistory()
    assert len(history) == 3 and history[0].depth == 0
    assert history[1].parent == solid.GetHandle() and history[1].operandIndex == 0
    assert history[2].operandIndex == 1 and history[2].action == -1
    assert api.ExtrudeObject.Is(history[1].object)
    assert not solid.GetOperand(2)
    assert not solid.SetOperation(999) and not solid.SetOperand(2, a)

    intersection = track(Solid.CreateIntersection(a, b))
    volume(intersection, 0.5e9)
    assert solid.SetOperation(Op.Difference)
    volume(solid, 0.5e9)
    cutter = track(api.ExtrudeObject.Create(Rect2D(750, 1000, 1250, 0), 0, 1000))
    assert solid.SetOperand(1, cutter)
    volume(solid, 0.75e9)

    old_tool = solid.GetOperand(1)
    covering = track(api.ExtrudeObject.Create(Rect2D(-1000, 2000, 3000, -1000), -1000, 5000))
    assert not solid.SetOperand(1, covering)  # empty subtraction must roll back
    assert solid.GetOperand(1) == old_tool
    volume(solid, 0.75e9)

    blank = api.ExtrudeObject(solid.GetOperand(0))
    assert blank.SetThickness(2000)
    assert solid.Rebuild()  # not merely Reset()
    volume(solid, 1.75e9)
    assert solid.SetScale((2, 1, 1))
    volume(solid, 3.5e9)
    assert solid.SetScale((1, 1, 1))
    volume(solid, 1.75e9)
    assert not solid.SetScale((0, 1, 1))
    assert not solid.Move3D((float("nan"), 0, 0))
    placement = solid.GetTransform()
    assert solid.SetTransform(placement)
    placement.uAxis = api.Point3D(x=2, y=0, z=0)
    assert not solid.SetTransform(placement)
    assert solid.Move3D((10, 20, 30))
    bounds = solid.GetBounds3D()
    assert math.isclose(bounds.minimum.z, 30, abs_tol=1e-8)
    assert solid.GetSurfaceArea() > 0

    nested = track(Solid.CreateUnion(solid, b))
    assert len(nested.GetHistory()) == 5
    frozen = track(nested.Duplicate())
    before = frozen.GetVolume()
    assert frozen.ClearHistory() and Solid.IsGenericSolid(frozen)
    volume(frozen, before)
    assert not frozen.HasHistory() and frozen.GetOperation() is None
    assert frozen.GetOperandCount() == 0 and len(frozen.GetHistory()) == 1
    assert not frozen.SetOperation(Op.Union) and not frozen.Rebuild()
    assert nested.HasHistory()  # flattening the copy did not touch the original
    single = track(Solid.CreateFromExtrude(rect=Rect2D(0, 100, 100, 0), baseElevation=0, thickness=200))
    assert single.HasHistory() and single.GetOperandCount() == 1
    assert api.ExtrudeObject.Is(single.GetOperand(0))
    volume(single, 2e6)

    far = track(api.ExtrudeObject.Create(Rect2D(10000, 1000, 11000, 0), 0, 1000))
    a_parent, far_parent = a.GetParent(), far.GetParent()
    assert not Solid.CreateIntersection(a, far, keepOriginal=False)
    assert a.GetParent() == a_parent and far.GetParent() == far_parent
    volume(a, 1e9)
    assert not Solid.CreateUnion(a, a, keepOriginal=False)
finally:
    for obj in reversed(created):
        assert obj.Delete(useUndo=False)

invalid = Solid(None)
assert not invalid and invalid.GetAction() is None and invalid.HasHistory() is None
assert invalid.GetTransform() is None and invalid.GetScale() is None
assert invalid.GetBounds3D() is None and invalid.GetVolume() is None
assert invalid.GetHistory() == [] and invalid.GetOperands() == []
assert not invalid.ClearHistory() and not invalid.Rebuild()
```

Additional manual coverage: all extrusion overloads (curves, holes, planar/oblique/negative extrusions and `up`);
existing imported/generic solids, meshes, sweeps and other native solid operands; both ownership modes on successful
creation (refresh wrapper ownership before cleanup); failed creation and replacement preserving object order and
handles; non-Boolean history inspection and rejected feature setters; nested edits followed by outermost rebuild;
save/reopen retaining the native tree; class/by-class attributes, texture and attached records on Boolean operations;
mirrored placements, native scale limits, rotated/scaled nested models and cross-container coordinate conventions;
selection/type filtering; script-level undo/redo. No modeling-engine, fillet/chamfer/shell UI or non-Boolean feature
implementations were changed.

### Polygon3DObject(h: Handle) : PrimitiveObject +Is +Duplicate
Native 3D polygon (`ObjectType.Polygon3D`). Vertices are plain corner points in parent coordinates (world units,
0-based indices); no arc/Bezier vertices, no per-edge visibility. New polygons go into the active layer.
At least two vertices are always kept (`DeleteVertex` fails at two; `SetVertices` needs 2..32767 points).
Lengths, closest point and point-at-distance follow the closed flag; `GetArea` needs a closed polygon with >= 3
vertices. `IsClockwise`/`GetPolygon2D` use the XY projection; normal/plane/planarity use the Newell normal
(collinear vertices -> None). Setters return False and leave the polygon unchanged for an invalid wrapper,
out-of-range index or non-finite value. `Transform`/`GetPlaneTransform` reuse **`ExtrudeObject.Transform`**;
`Transform` maps `p` to `origin + uAxis*p.x + vAxis*p.y + wAxis*p.z` and accepts any non-degenerate (not
necessarily orthonormal) frame.

- Is(h: Handle) -> bool [s]
- Create(points: [Point3D], closed=True) -> Polygon3DObject [s]
- Create(polygon: Polygon2D, z=0.0) -> Polygon3DObject [s]  # corner points only, keeps closed flag
- Create(rect: Rect2D, z=0.0) -> Polygon3DObject [s]  # closed, counter-clockwise
- ConvertToGroup(hObject: Handle, keepOriginal=True) -> Handle [s]  # group of 3D polygons, or null
- GetPolygonsIn(hContainer: Handle) -> [Handle] [s]  # 3D polygon members, including nested groups
- Duplicate() -> Polygon3DObject
- GetVertexCount() -> int
- GetVertex(index: int) -> Point3D?
- SetVertex(index: int, point: Point3D) -> bool
- GetVertices() -> [Point3D]
- SetVertices(points: [Point3D]) -> bool
- AddVertex(point: Point3D) -> bool
- AddVertices(points: [Point3D], reverse=False) -> bool
- InsertVertex(beforeIndex: int, point: Point3D) -> bool  # beforeIndex == count appends
- DeleteVertex(index: int) -> bool
- IsClosed() -> bool
- SetClosed(closed: bool) -> bool
- GetPolygon2D() -> Polygon2D?
- IsClockwise() -> bool?
- Reverse() -> bool
- IsPlanar(tolerance=1e-9) -> bool?
- IsValidPolygon(tolerance=1e-9) -> bool?
- GetNormal() -> Point3D?
- GetPlane() -> Plane?
- GetPlaneTransform() -> ExtrudeObject.Transform?  # W axis = polygon normal
- GetVertexCentroid() -> Point3D?  # vertex average; the cube center is the inherited GetCenter3D
- GetLength() -> float?
- GetSegmentLength(segmentIndex: int) -> float?
- GetArea() -> float?
- GetPointAtDistance(distance: float) -> Point3D?
- GetClosestPoint(point: Point3D) -> ClosestPoint?
- GetDistanceTo(point: Point3D) -> float?
- GetDistanceToPlane(point: Point3D) -> float?  # signed, positive on the normal side
- IntersectLine(start: Point3D, direction: Point3D) -> Point3D?  # None when parallel to the plane
- Cleanup(tolerance=1e-9) -> bool
- CleanupFeaturePreserving(collinearTolerance: float, closenessTolerance: float) -> bool
- Simplify(maxDeviation: float) -> bool
- Segment(maxSegmentLength: float) -> bool
- Transform(transform: ExtrudeObject.Transform) -> bool
- Move3D(offset: Point3D) -> bool
- Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool
- Scale3D(center: Point3D, factors: Point3D) -> bool  # non-zero factors
- IsValidSolidOperand() -> bool  # closed, >= 3 vertices
- ToGenericSolid(keepOriginal=True) -> GenericSolidObject  # one-operand solid, polygon kept in history
- Union(hTool: Handle, keepOriginal=True) -> GenericSolidObject
- Subtract(hTool: Handle, keepOriginal=True) -> GenericSolidObject
- Intersect(hTool: Handle, keepOriginal=True) -> GenericSolidObject
- ConvertToGenericSolid(keepOriginal=True) -> GenericSolidObject  # history-free
- ToPlanarSolid(thickness: float) -> GenericSolidObject  # GenericSolidObject.CreatePlanar(vertices, thickness)

### Polygon3DObject.Plane()
fields: point: Point3D (vertex centroid), normal: Point3D (unit), d: float (normal . p + d = 0)

### Polygon3DObject.ClosestPoint()
fields: point: Point3D, distance: float, segmentIndex: int, distanceAlong: float

### 3D polygon example / regression checks
Run in Vectorworks with an open disposable drawing after building the updated application. This script creates
and deletes its own objects. These checks have **not** been run as part of the no-C++-build checks.

```python
import math
import api
from api.Math import Rect2D

Poly = api.Polygon3DObject
P = lambda x, y, z: api.Point3D(x=x, y=y, z=z)
assert api.Document.IsOpen()
created = []

def track(obj):
    assert obj
    created.append(obj)
    return obj

try:
    square = track(Poly.Create(Rect2D(0, 1000, 1000, 0), 500))
    assert Poly.Is(square) and api.Document.As(Poly, square.GetHandle())
    assert square.GetVertexCount() == 4 and square.IsClosed()
    assert math.isclose(square.GetLength(), 4000) and math.isclose(square.GetArea(), 1e6)
    assert square.IsPlanar() and square.IsClockwise() is False
    plane = square.GetPlane()
    assert math.isclose(plane.normal.z, 1) and math.isclose(plane.point.z, 500)
    assert math.isclose(square.GetDistanceToPlane(P(0, 0, 600)), 100)

    assert square.SetClosed(False) and math.isclose(square.GetLength(), 3000)
    assert square.GetArea() is None
    assert square.SetClosed(True)
    assert square.InsertVertex(1, P(500, 0, 500)) and square.GetVertexCount() == 5
    assert square.Cleanup() and square.GetVertexCount() == 4  # collinear vertex removed
    assert not square.SetVertex(9, P(0, 0, 0)) and not square.SetVertex(0, P(float("nan"), 0, 0))

    closest = square.GetClosestPoint(P(500, -200, 500))
    assert math.isclose(closest.distance, 200) and math.isclose(closest.point.y, 0, abs_tol=1e-9)
    assert square.Move3D(P(0, 0, 100)) and math.isclose(square.GetBounds3D().minimum.z, 600)
    assert square.Rotate3D(P(0, 0, 600), P(1, 0, 0), 90)
    assert math.isclose(abs(square.GetNormal().y), 1, rel_tol=1e-9)
    assert square.Scale3D(P(0, 0, 0), P(2, 2, 2)) and math.isclose(square.GetArea(), 4e6)
    assert not square.Scale3D(P(0, 0, 0), P(0, 1, 1))

    line = track(Poly.Create([P(0, 0, 0), P(0, 0, 1000)], closed=False))
    assert not line.DeleteVertex(0)  # two vertices are always kept
    assert line.GetNormal() is None
    p = line.GetPointAtDistance(250)
    assert math.isclose(p.z, 250)
    assert line.Segment(100) and line.GetVertexCount() >= 10
    assert math.isclose(line.GetLength(), 1000)
    assert line.Simplify(1) and line.GetVertexCount() == 2
    copy = track(line.Duplicate())
    assert copy.Reverse() and math.isclose(copy.GetVertex(0).z, 1000)
    assert math.isclose(line.GetVertex(0).z, 0)  # original unchanged
finally:
    for obj in reversed(created):
        assert obj.Delete(useUndo=False)

invalid = Poly(None)
assert not invalid and invalid.GetVertexCount() == 0 and invalid.GetVertices() == []
assert invalid.GetVertex(0) is None and invalid.GetPlane() is None and invalid.GetLength() is None
assert not invalid.AddVertex(api.Point3D(x=0, y=0, z=0)) and not invalid.SetClosed(True)
assert not Poly.Create([api.Point3D(x=0, y=0, z=0)])  # fewer than two points
```

Additional manual coverage: `Create(Polygon2D)` with arc/Bezier vertices (corner points only); `ConvertToGroup`
on 2D shapes, extrudes and solids with both `keepOriginal` values, followed by `GetPolygonsIn` on the result;
`CleanupFeaturePreserving`, `IsValidPolygon`, `IntersectLine` and non-orthonormal `Transform`; class/attribute
retention after vertex edits; save/reopen; script-level undo/redo.

### MeshObject(h: Handle) : PrimitiveObject +Is +Duplicate
Native mesh (`ObjectType.Mesh`): shared vertices (parent coordinates, world units) plus polygonal faces of >= 3
vertex indices. All indices are 0-based. New meshes go into the active layer. Setters return False and leave the
mesh unchanged for an invalid wrapper, out-of-range index or non-finite value. Part 0 (`GetOverallPart()`) is the
overall, untextured part. Normals/UVs hold one entry per vertex. Face-list rewrites (`SetFaces`, `SetGeometry`,
`DeleteFace`, `FlipFaces`) keep parts but reset per-face class/fill/pen; `AddFace` keeps them. `SetVertices` needs
the same count; `SetGeometry` may change it and then clears normals/UVs. `ClearUVs` also resets every face to part 0.
Transforms carry normals along; mirroring also reverses winding. `Simplify` needs the mesh utility component.
**Solid integration:** a mesh is a valid generic solid operand. `ToGenericSolid`/`Union`/`Subtract`/`Intersect`
follow the `GenericSolidObject` factory conventions (`keepOriginal=True` default; `False` moves the mesh into the
history). `GenericSolidObject.ConvertToMesh`/`MeshObject.CreateFromObject` tessellate back (no history kept);
`GetMeshOperands(hSolid)` lists meshes inside a solid's history (edit them, then `Rebuild()` the outermost solid).

- Is(h: Handle) -> bool [s]
- GetOverallPart() -> int [s]
- Create(vertices: [Point3D], faces: [[int]]) -> MeshObject [s]
- Create(vertices: [Point3D], faces: [Face]) -> MeshObject [s]
- CreateFromPolygons(polygons: [[Point3D]]) -> MeshObject [s]  # welds coincident points
- CreateFromGroup(hGroup: Handle) -> MeshObject [s]  # group of 3D polygons, converted in place
- CreateFromObject(hObject: Handle, keepOriginal=True) -> MeshObject [s]  # any 3D object
- GetMeshesIn(hContainer: Handle) -> [Handle] [s]
- GetMeshOperands(hSolid: Handle) -> [Handle] [s]
- Duplicate() -> MeshObject
- GetVertexCount() -> int
- GetVertex(index: int) -> Point3D?
- SetVertex(index: int, point: Point3D) -> bool
- GetVertices() -> [Point3D]
- SetVertices(points: [Point3D]) -> bool  # same count
- HasNormals() -> bool
- GetNormals() -> [Point3D]
- SetNormals(normals: [Point3D]) -> bool  # normalized on write
- ClearNormals() -> bool
- HasUVs() -> bool
- GetUVs() -> [Point2D]
- SetUVs(uvs: [Point2D]) -> bool
- ClearUVs() -> bool
- GetFaceCount() -> int
- GetFace(index: int) -> Face?
- GetFaces() -> [Face]
- SetFaces(faces: [Face]) -> bool
- AddFace(vertexIndices: [int], part=0) -> bool
- DeleteFace(index: int) -> bool
- SetGeometry(vertices: [Point3D], faces: [Face]) -> bool
- SetFacePart(faceIndex: int, part: int) -> bool
- GetFaceNormal(faceIndex: int) -> Point3D?
- GetFaceArea(faceIndex: int) -> float?
- GetFaceCenter(faceIndex: int) -> Point3D?
- GetParts() -> [Part]
- AddPart(texture=0) -> int?
- GetPartTexture(part: int) -> int?
- SetPartTexture(part: int, texture: int) -> bool
- GetSmoothing() -> Smoothing?
- SetSmoothing(smoothing: Smoothing) -> bool
- GetCreaseAngle() -> float?
- SetCreaseAngle(degrees: float) -> bool  # 0..180, switches to CustomCrease
- IsClosed() -> bool  # watertight, consistently oriented
- FlipFaces() -> bool
- Simplify(qualityPercent: float) -> bool  # 0 < q < 100
- Repair() -> [Handle]  # new meshes after this one; this mesh unchanged
- ConvertToGroup() -> Handle  # in place; wrapper becomes invalid
- ToGenericSolid(keepOriginal=True) -> GenericSolidObject
- Union(hTool: Handle, keepOriginal=True) -> GenericSolidObject
- Subtract(hTool: Handle, keepOriginal=True) -> GenericSolidObject  # mesh minus tool
- Intersect(hTool: Handle, keepOriginal=True) -> GenericSolidObject
- ConvertToGenericSolid(keepOriginal=True) -> GenericSolidObject  # history-free
- Transform(transform: ExtrudeObject.Transform) -> bool
- Move3D(offset: Point3D) -> bool
- Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool
- Scale3D(center: Point3D, factors: Point3D) -> bool  # non-zero factors
- GetSurfaceArea() -> float?
- GetVolume() -> float?  # closed meshes

### MeshObject.Face()
fields: vertexIndices: [int], part: int (0 = overall part)

### MeshObject.Part()
fields: id: int, texture: int (texture reference, 0 = none), faceCount: int

### MeshObject.Smoothing
`None_`, `DocumentPreference`, `CustomCrease`, `Imported`.

### NurbsCurveObject(h: Handle) : PrimitiveObject +Is +Duplicate
Native piecewise NURBS curve; non-owning wrapper. Creation inserts a control-point curve in the active layer.
Piece, point and knot indices are 0-based. Points and distances use world millimetres; parameters/knots use the
native curve parameter domain. Degree is specified at creation and read-only afterward. Setters reject non-finite
values and return False on invalid wrappers/indices; optional getters return None and counts return 0 on invalid input.

- Is(h: Handle) -> bool [s]
- Create(points: [Point3D], degree: int, byControlPoints=True) -> NurbsCurveObject [s]
- Duplicate() -> NurbsCurveObject
- GetPieceCount() -> int
- GetPointCount(pieceIndex=0) -> int
- GetControlPointCount(pieceIndex=0) -> int
- GetDegree(pieceIndex=0) -> int?
- GetPoint(pieceIndex: int, pointIndex: int) -> Point3D?
- SetPoint(pieceIndex: int, pointIndex: int, point: Point3D) -> bool
- GetWeight(pieceIndex: int, controlPointIndex: int) -> float?
- SetWeight(pieceIndex: int, controlPointIndex: int, weight: float) -> bool
- GetKnotCount(pieceIndex=0) -> int
- GetKnot(pieceIndex: int, knotIndex: int) -> float?
- SetKnot(pieceIndex: int, knotIndex: int, knot: float) -> bool
- Evaluate(pieceIndex: int, parameter: float) -> Point3D?
- GetLength() -> float?
- GetLocationAtDistance(distance: float) -> NurbsCurveObject.Location?
- GetPointAtDistance(distance: float) -> Point3D?
- GetClosestPoint(point: Point3D) -> NurbsCurveObject.Location?
- GetDistanceTo(point: Point3D) -> float?
- GetTangent(pieceIndex: int, parameter: float) -> Point3D?
- GetCurvature(pieceIndex: int, parameter: float) -> float?
- DivideByCount(count: int, includeEnd: bool=True) -> [Point3D]?
- Extend(distance: float, atStart: bool, linear: bool) -> NurbsCurveObject # new object in active layer
- Offset(distance: float) -> NurbsCurveObject # signed offset; new object in active layer

GetPointCount/GetPoint/SetPoint address fit points on fitted pieces, control points otherwise.
GetControlPointCount counts the underlying control points for weights; their index domain can exceed the fit-point count.
SetWeight returns False for fitted pieces. Create(..., byControlPoints=False) creates a fit-point curve.
Analysis is read-only true 3D world-space, never screen-projected, and searches all pieces for the global closest
point. Arc distance is absolute world millimetres from the first piece's start, not a fraction; finite [0,length],
no wrapping/clamping. GetLocationAtDistance returns a native per-piece parameter reusable with Evaluate/GetTangent/
GetCurvature. At an exact piece join it selects the preceding nonzero-length piece. Tangents are unit vectors;
curvature is nonnegative inverse millimetres. Derivatives are right-hand at knots, left-hand at piece ends.
DivideByCount returns exactly count>=2 arc-spaced points, not segments. includeEnd=True includes endpoints/duplicate
closed seam; False omits the final endpoint/seam. Invalid/nonfinite/out-of-range input and Core failure return None.
Zero speed has no tangent/curvature; zero-length point/division queries return None, but successful length may be zero.
Analysis preserves the source and inserts no drawing objects; failed division never returns a partial list.

### NurbsCurveObject.Location()
Writable copied-value record, not a drawing-object owner.
fields: point: Point3D=(0,0,0), pieceIndex: int=0, parameter: float=0.0
pieceIndex is zero-based; parameter is a native knot parameter within that piece, not arc distance.

### NurbsSurfaceObject(h: Handle) : PrimitiveObject +Is +Duplicate
Native NURBS surface; non-owning wrapper. `Create` inserts a control net in the active layer. U/V point and knot
indices are 0-based. Coordinates/distances use world millimetres; evaluation parameters/knots use native U/V domains.
Degrees are specified at creation and read-only afterward.

- Is(h: Handle) -> bool [s]
- Create(uPointCount: int, vPointCount: int, uDegree: int, vDegree: int) -> NurbsSurfaceObject [s] # counts >= 2; 1 <= each degree < its count
- CreateFromCurvesNetwork() -> bool [s] # consumes selected intersecting curves; status only, no wrapper returned
- Duplicate() -> NurbsSurfaceObject
- GetUPointCount() -> int
- GetVPointCount() -> int
- GetUDegree() -> int?
- GetVDegree() -> int?
- GetPoint(uIndex: int, vIndex: int) -> Point3D?
- SetPoint(uIndex: int, vIndex: int, point: Point3D) -> bool
- GetWeight(uIndex: int, vIndex: int) -> float?
- SetWeight(uIndex: int, vIndex: int, weight: float) -> bool
- GetUKnotCount() -> int
- GetVKnotCount() -> int
- GetUKnot(knotIndex: int) -> float?
- GetVKnot(knotIndex: int) -> float?
- SetUKnot(knotIndex: int, knot: float) -> bool
- SetVKnot(knotIndex: int, knot: float) -> bool
- Evaluate(u: float, v: float) -> Point3D?
- TrimByCurve(curve: NurbsCurveObject) -> bool # success moves curve to the surface auxiliary trim list
- Extend(distance: float, atStart: bool, linear: bool, uDirection: bool) -> NurbsSurfaceObject # new object in active layer
- Offset(distance: float) -> NurbsSurfaceObject # signed offset; new object in active layer

Trim changes the surface and moves its curve into the auxiliary trim list; register both inputs with the undo event
before the call. `CreateFromCurvesNetwork` deletes selected input curves when creating a surface; native failure cleanup can
also delete inputs. Register undo before calling; duplicate/select only copies to preserve originals.
Discard source wrappers/handles after the call and reacquire results by traversing the drawing: IsValid only tests a non-null
handle and cannot detect deletion by the native command. Never query/delete stale handles.
Both operations follow native behavior and return False on failure. See [3D geometry](Objects3D.md#nurbssurfaceobject)
for the full reference and manual source-lifetime/undo regression.

### Mesh example / regression checks
Run in Vectorworks with an open disposable drawing after building the updated application. This script creates
and deletes its own objects. These checks have **not** been run as part of the no-C++-build checks.

```python
import math
import api
from api.Math import Rect2D

Mesh = api.MeshObject
Solid = api.GenericSolidObject
P = lambda x, y, z: api.Point3D(x=x, y=y, z=z)
assert api.Document.IsOpen()
created = []

def track(obj):
    assert obj
    created.append(obj)
    return obj

try:
    # Unit tetrahedron with outward-facing faces: volume = 1000^3 / 6
    verts = [P(0, 0, 0), P(1000, 0, 0), P(0, 1000, 0), P(0, 0, 1000)]
    tet = track(Mesh.Create(verts, [[0, 2, 1], [0, 1, 3], [1, 2, 3], [0, 3, 2]]))
    assert Mesh.Is(tet) and api.Document.As(Mesh, tet.GetHandle())
    assert tet.GetVertexCount() == 4 and tet.GetFaceCount() == 4 and tet.IsClosed()
    assert math.isclose(tet.GetVolume(), 1e9 / 6, rel_tol=1e-6)
    assert math.isclose(tet.GetFaceNormal(0).z, -1)
    assert all(f.part == 0 for f in tet.GetFaces())

    assert tet.Move3D(P(0, 0, 100)) and math.isclose(tet.GetBounds3D().minimum.z, 100)
    assert tet.Scale3D(P(0, 0, 100), P(-1, 1, 1)) and tet.IsClosed()  # mirror keeps faces outward
    assert math.isclose(tet.GetVolume(), 1e9 / 6, rel_tol=1e-6)
    assert not tet.SetVertex(9, P(0, 0, 0)) and not tet.SetVertices(verts[:3])
    assert not tet.AddFace([0, 1])  # fewer than three indices

    assert tet.SetNormals([P(0, 0, 2)] * 4) and tet.HasNormals()
    assert math.isclose(tet.GetNormals()[0].z, 1)
    assert tet.ClearNormals() and not tet.HasNormals()
    assert tet.SetCreaseAngle(30) and tet.GetSmoothing() == Mesh.Smoothing.CustomCrease

    part = tet.AddPart()
    assert part is not None and tet.SetFacePart(1, part)
    assert any(p.id == part and p.faceCount == 1 for p in tet.GetParts())

    open_mesh = track(Mesh.CreateFromPolygons([[P(0, 0, 0), P(10, 0, 0), P(10, 10, 0)],
                                               [P(0, 0, 0), P(10, 10, 0), P(0, 10, 0)]]))
    assert open_mesh.GetVertexCount() == 4 and not open_mesh.IsClosed()  # welded, open

    solid = track(tet.ToGenericSolid(keepOriginal=True))
    assert solid.HasHistory() and len(Mesh.GetMeshOperands(solid.GetHandle())) == 1
    back = track(solid.ConvertToMesh(keepOriginal=True))
    assert back.IsClosed() and math.isclose(back.GetVolume(), tet.GetVolume(), rel_tol=1e-6)

    box = track(Solid.CreateFromExtrude(rect=Rect2D(-500, 500, 500, -500),
                                        baseElevation=0, thickness=500))
    cut = track(tet.Subtract(box.GetHandle(), keepOriginal=True))
    assert cut.GetOperation() == Solid.Operation.Difference
    assert cut.GetVolume() < tet.GetVolume()
finally:
    for obj in reversed(created):
        if obj:
            obj.Delete(useUndo=False)

invalid = Mesh(None)
assert not invalid and invalid.GetVertexCount() == 0 and invalid.GetFaces() == []
assert invalid.GetVolume() is None and invalid.GetBounds3D() is None
assert not invalid.ToGenericSolid() and not invalid.FlipFaces()
assert not Mesh.Create([P(0, 0, 0)], [[0, 1, 2]])  # face index out of range
```

Additional manual coverage: `CreateFromGroup` with mixed content (must fail unchanged); `CreateFromObject` on
extrudes, sweeps and nested solids with both `keepOriginal` values, and on a history operand; UV/part workflows
with real textures; `Simplify` and `Repair` on dense or damaged imports; `ConvertToGroup`; editing a mesh operand
inside a solid followed by the outermost `Rebuild()`; per-face attribute behaviour after face rewrites;
save/reopen; script-level undo/redo.

### ShellObject(h: Handle) : GenericSolidObject +Is +Duplicate
Shell solid (Shell Solid tool, VectorScript `CreateShell`): a CSG offset node with exactly one operand (the source)
that stores a signed thickness and the selected faces as history. A NURBS surface is thickened; a solid is hollowed
with the selected faces removed. Negative stored thickness = opposite side ("Offset Side"). Factories default to
`keepOriginal=True`; with `keepOriginal=False` the result replaces the source in its container and the source becomes
the operand; with `keepOriginal=True` the source stays and a copy inserted right after it becomes the operand, so the
shell sits right after the source; failures leave inputs unchanged. Face indices are 0-based, global across all bodies of the source. When the source supports
monikers the faces are stored as monikers instead of indices. Inherited `SetOperation`/`SetOperand` return False.
`SetThickness`/`SetReversed` rebuild and restore the old value if the rebuild fails.
Factories record the shell and any source copy for Undo and join an existing event. Do not register the returned
shell again; register a newly created source before shelling it.
- Create(hSurface: Handle, thickness: float, keepOriginal=True) -> ShellObject [s]  # NURBS surface only
- CreateFromSolid(hSolid: Handle, openFaceIndices: [int], thickness: float, keepOriginal=True) -> ShellObject [s]
- GetFaceCount(h: Handle) -> int? [s]  # faces of a surface/solid across all bodies
- Duplicate() -> ShellObject
- IsFailed() -> bool?  # last rebuild failed
- GetThickness() -> float?  # magnitude
- SetThickness(thickness: float) -> bool  # > 0, keeps side
- IsReversed() -> bool?
- SetReversed(isReversed: bool) -> bool
- GetSource() -> Handle  # operand 0
- IsMonikerBased() -> bool?
- GetSelectedFaceIndices() -> [int]  # empty when moniker-based
- GetSelectedFaceMonikers() -> [str]  # empty when index-based
- ResolveSelectedFaceIndices() -> [int]?  # sorted, unique current source-face indices, resolving monikers; None if the source or any selected face is unavailable, never a partial selection

### Shell example / regression checks
Run in a disposable drawing where the script controls its undo event; reverting the event cleans up the test geometry.
```python
import api
from api.Math import Rect2D
Shell = api.ShellObject
doc = api.Document()
doc.StartUndoEvent(isRevertible=True)
doc.NameUndoEvent("Shell regression checks")
try:
    box = api.ExtrudeObject.Create(rect=Rect2D(0, 100, 100, 0), baseElevation=0, thickness=100)
    assert box
    wasRegistered = doc.AddAfterSwapObject(box.GetHandle())
    assert wasRegistered
    count = Shell.GetFaceCount(box.GetHandle())
    assert count == 6
    shell = Shell.CreateFromSolid(box.GetHandle(), [0], thickness=5, keepOriginal=True)
    assert shell and Shell.Is(shell.GetHandle()) and api.GenericSolidObject.Is(shell.GetHandle())
    assert abs(shell.GetThickness() - 5) < 1e-9 and shell.IsReversed() is False and not shell.IsFailed()
    assert len(shell.GetOperands()) == 1 and shell.GetSource()
    assert shell.ResolveSelectedFaceIndices() == [0]
    vol = shell.GetVolume()
    assert shell.SetThickness(10) and shell.GetVolume() > vol
    assert shell.SetReversed(True) and shell.IsReversed()
    assert not shell.SetThickness(0) and not shell.SetThickness(-1)
    assert not shell.SetOperation(api.GenericSolidObject.Operation.Union)
finally:
    wasReverted = doc.RevertUndoEvent()
    assert wasReverted
assert not Shell.CreateFromSolid(None, [0], 5) and not Shell(None).GetThickness()
```

Additional manual coverage: `Create` on NURBS surfaces with both sides and `keepOriginal` values; moniker-based faces
on extrudes/generic solids; out-of-range or empty face lists (must fail unchanged); a shell as an operand of
`GenericSolidObject.CreateBoolean`; editing the source in the history followed by `Rebuild()`; save/reopen; undo/redo.

### SolidPrimitiveObject(h: Handle) : PrimitiveObject +Is
Common base of native sphere/hemisphere/cone solids (one Core node type with a kind). Stored as a local frame
(origin + orthonormal I/J/K) plus parameters. Sphere/hemisphere: origin = center, K = up (dome along +K).
Cone: origin = base center, K = base->tip of a right cone, tip stored in object space. Valid generic solid operands;
after editing one inside a solid's history call `Rebuild()` on the outermost solid. Setters regenerate geometry.
`GetFrame` returns `ExtrudeObject.Transform`; `GetBounds3D` is inherited from `PrimitiveObject`.
- GetKindOf(h: Handle) -> Kind? [s]
- GetPrimitivesIn(hContainer: Handle) -> [Handle] [s]  # direct members
- GetPrimitiveOperands(hSolid: Handle) -> [Handle] [s]  # anywhere in a solid's history
- GetKind() -> Kind?
- GetFrame() -> ExtrudeObject.Transform?
- SetFrame(origin: Point3D, iAxis: Point3D, jAxis: Point3D) -> bool  # orthonormalized, K = I x J
- GetAxis() -> Point3D?  # K
- SetAxis(axis: Point3D) -> bool  # shortest rotation around origin
- Move3D(offset: Point3D) -> bool
- Rotate3D(center: Point3D, axis: Point3D, angleDegrees: float) -> bool
- Scale3D(center: Point3D, factor: float) -> bool  # uniform, > 0
- GetVolume() -> float?
- GetSurfaceArea() -> float?
- ToGenericSolid(keepOriginal=True) -> GenericSolidObject
- Union(hTool: Handle, keepOriginal=True) -> GenericSolidObject  # primitive is the blank
- Subtract(hTool: Handle, keepOriginal=True) -> GenericSolidObject
- Intersect(hTool: Handle, keepOriginal=True) -> GenericSolidObject
- ToMesh(keepOriginal=True) -> MeshObject
- ConvertToGenericSolid(keepOriginal=True) -> GenericSolidObject  # history-free

### SolidPrimitiveObject.Kind
Sphere=0, Hemisphere=1, Cone=2

### SphereObject(h: Handle) : SolidPrimitiveObject +Is +Duplicate
Radii along local I/J/K; unequal radii = ellipsoid.
- Create(center: Point3D, radius: float) -> SphereObject [s]
- CreateEllipsoid(center: Point3D, radii: Point3D) -> SphereObject [s]  # axis-aligned: I, J, K = world X, Y, Z, so radii = (x, y, z)
- GetCenter() -> Point3D? / SetCenter(center: Point3D) -> bool
- GetRadius() -> float?  # I radius
- SetRadius(radius: float) -> bool  # all three
- GetRadii() -> Point3D? / SetRadii(radii: Point3D) -> bool  # each > 0
- IsEllipsoid() -> bool  # True when radii differ
- Ellipsoid GetVolume() = 4/3*pi*I*J*K (halved for hemisphere); GetSurfaceArea() is inaccurate for ellipsoids (modeler reports a sphere of the I radius) - do not use

### HemisphereObject(h: Handle) : SphereObject +Is +Duplicate
Center of the flat face; dome along K.
- Create(center: Point3D, topPoint: Point3D) -> HemisphereObject [s]
- Create(center: Point3D, radius: float) -> HemisphereObject [s]  # dome +Z
- GetTopPoint() -> Point3D?  # center + K * K radius
- SetTopPoint(topPoint: Point3D) -> bool  # re-orients, uniform radius = distance

### ConeObject(h: Handle) : SolidPrimitiveObject +Is +Duplicate
Elliptical base in the local I/J plane; tip in object space (SetBaseCenter moves the whole cone).
Volume is pi * I * J * abs(perpendicular height) / 3, including elliptical/oblique cones. Their surface area uses
the existing polygonal boundary, including the base, so it depends on tessellation resolution. Queries do not
regenerate or convert geometry; unavailable area returns None (omitted by MCP), never a fabricated zero.
Right circular cones retain their historical analytic lateral area, excluding the base.
- Create(baseCenter: Point3D, tipPoint: Point3D, radius: float) -> ConeObject [s]
- Create(baseCenter: Point3D, radius: float, height: float) -> ConeObject [s]  # +Z; negative height = -Z
- GetBaseCenter() -> Point3D? / SetBaseCenter(baseCenter: Point3D) -> bool
- GetTipPoint() -> Point3D?  # world
- SetTipPoint(tipPoint: Point3D, keepRight=True) -> bool  # True re-orients; False keeps base plane (oblique); tip in base plane fails
- GetLocalTipPoint() -> Point3D? / SetLocalTipPoint(localTipPoint: Point3D) -> bool  # z != 0
- IsRightCone() -> bool
- GetHeight() -> float?
- SetHeight(height: float) -> bool  # makes a right cone; negative flips
- GetRadius() -> float?  # I radius
- SetRadius(radius: float) -> bool  # both base radii
- GetRadii() -> Radii? / SetRadii(radii: Radii) -> bool  # each > 0
- IsElliptical() -> bool

### ConeObject.Radii
Fields: i: float, j: float  # base radii along local I and J

### Solid primitive example / regression checks
```python
import api
P = api.Point3D
Prim, Cone, Sphere, Hemi = api.SolidPrimitiveObject, api.ConeObject, api.SphereObject, api.HemisphereObject
cone = Cone.Create(baseCenter=P(x=0, y=0, z=0), radius=50, height=100)
sphere = Sphere.Create(center=P(x=0, y=0, z=100), radius=30)
hemi = Hemi.Create(center=P(x=200, y=0, z=0), radius=40)
solid = None
try:
    assert cone and sphere and hemi
    assert Prim.GetKindOf(cone.GetHandle()) == Prim.Kind.Cone and Hemi.Is(hemi.GetHandle())
    assert Sphere.Is(sphere.GetHandle()) and not Hemi.Is(sphere.GetHandle()) and not Cone.Is(sphere.GetHandle())
    assert abs(cone.GetHeight() - 100) < 1e-6 and cone.IsRightCone() and not cone.IsElliptical()
    assert abs(cone.GetTipPoint().z - 100) < 1e-6
    assert cone.SetTipPoint(P(x=30, y=0, z=100), keepRight=False) and not cone.IsRightCone()
    assert cone.SetHeight(80) and cone.IsRightCone() and abs(cone.GetHeight() - 80) < 1e-6
    assert not cone.SetTipPoint(P(x=10, y=0, z=0), keepRight=False)  # in the base plane
    assert cone.SetRadii(Cone.Radii(i=50, j=40)) and cone.IsElliptical()
    assert sphere.SetRadii(P(x=30, y=20, z=10)) and sphere.IsEllipsoid() and abs(sphere.GetRadius() - 30) < 1e-6
    assert hemi.SetTopPoint(P(x=200, y=0, z=-60)) and abs(hemi.GetRadius() - 60) < 1e-6
    assert hemi.GetAxis().z < -0.999
    assert not sphere.SetRadius(0) and not sphere.Scale3D(P(x=0, y=0, z=0), 0)
    solid = cone.Subtract(sphere.GetHandle(), keepOriginal=True)
    assert solid and len(Prim.GetPrimitiveOperands(solid.GetHandle())) == 2
finally:
    for obj in (solid, cone, sphere, hemi):
        if obj:
            obj.Delete(useUndo=False)
assert not Cone(None).GetHeight() and not Sphere.Create(P(x=0, y=0, z=0), -1)
```

Additional manual coverage: Object Info palette agreement after each setter (radii, height, tip, axis);
`Rotate3D`/`SetFrame` on all three kinds; `keepOriginal=False` Booleans followed by editing the operand and
`Rebuild()` on the outermost solid; `ToMesh`; volume/area for ellipsoids and elliptical cones; save/reopen; undo/redo.

### Convert to Generic Solid example / regression checks
```python
import api
P = api.Point3D
GS = api.GenericSolidObject
sphere = api.SphereObject.Create(center=P(x=0, y=0, z=0), radius=30)
poly = api.Polygon3DObject.Create([P(x=0, y=0, z=0), P(x=100, y=0, z=0), P(x=100, y=100, z=0)], True)
openPoly = api.Polygon3DObject.Create([P(x=0, y=0, z=0), P(x=100, y=0, z=0)], False)
created = []
try:
    assert GS.CanConvertToGenericSolid(sphere.GetHandle()) and GS.CanConvertToGenericSolid(poly.GetHandle())
    assert not GS.CanConvertToGenericSolid(openPoly.GetHandle()) and not openPoly.IsValidSolidOperand()
    flat = sphere.ConvertToGenericSolid(keepOriginal=True)
    created.append(flat)
    assert flat and api.SphereObject.Is(sphere.GetHandle())  # source untouched
    assert GS.IsGenericSolid(flat.GetHandle()) and not flat.HasHistory() and flat.GetVolume() > 0
    slab = poly.ToPlanarSolid(10)
    created.append(slab)
    assert slab and slab.GetVolume() > 0
    hist = poly.ToGenericSolid(keepOriginal=True)
    created.append(hist)
    assert hist and hist.HasHistory()
    assert not openPoly.ConvertToGenericSolid() and not GS.ConvertToGenericSolid(None)
finally:
    for obj in created + [sphere, poly, openPoly]:
        if obj:
            obj.Delete(useUndo=False)
```

Additional manual coverage: `ConvertToGenericSolid` on an extrude, sweep, mesh, Shell, cone, hemisphere and a nested
CSG solid; `keepOriginal=False` deletes the source only on success; overall texture kept for extrude/mesh sources;
undo/redo of the conversion; the result has the source's class and layer.

## API contract regression checks

When validating an installed Vectorworks version, use a disposable drawing and check concrete results, not just successful calls:
open versus closed centroid, empty over-shrunk
rectangles, exact collapse, world-squared area under different document units, polygon/base measurement agreement,
consuming and preserving conversions, failed conversion preserving the source, and compatibility aliases.
Restore document unit settings and delete any geometry created by your checks. Plug-in/resource tests and native
undo/redo require application-level verification.

These are validation scenarios, not a claim of live application results. Syntax/static verification is not a
substitute for checking behavior inside Vectorworks.

Additional application checks:

1. Draw a closed freehand rectangle with known dimensions. Wrap its handle in `PolygonObject`; `GetArea()` and
   `GetPolyArea()` must agree in square millimetres, and `GetPerimeter()` and `GetPolyPerimeter()` must agree in
   millimetres, under metric and imperial document units.
2. Select one editable object and leave another editable object unselected. `SelectedAndEditable` must return
   only the selected editable object. Locking it must exclude it. `All` includes symbol definitions and contents;
   `Drawing` excludes resources. Combine `AuxiliaryLists` with the required container flags to inspect auxiliaries.
3. In a disposable drawing, test `Polygon2D` union, intersection, difference, and symmetric difference on two
   overlapping rectangles. Verify the result lists and that summed areas are respectively 1,500,000, 500,000,
   500,000, and 1,000,000 square millimetres. Add a contained contour with `AddHole`, then verify it is accessible
   through `GetHoleCount` and `GetHole`.
4. In a disposable drawing, offset a square by positive and negative distances with both `OffsetJoin.Miter` and
   `OffsetJoin.Round`. Verify positive values expand its area, negative values inset it, round joins contain arc
   vertices at convex corners, and an inset beyond collapse returns an empty list.
5. Select a rectangle and a circle that overlap in a disposable drawing and call `api.PolyObject.CombineShapes` with
   each `PolyObject.BooleanOperation`; call a `PolyObject` Boolean method on a polygon and a polyline. Verify that the
   inputs are unchanged, that the returned handles have no drawing container before insertion, that their types vary
   (`api.PrimitiveObject(h).GetObjectType()`) and they carry the first shape's class, and that they can be inserted
   with `MoveToContainer(doc.GetDefaultContainer())`. Verify undo and redo of the insertion. Verify an empty list for
   the intersection of two disjoint rectangles, and `RuntimeError` for a text object, the same shape twice, and a
   screen-plane shape with a layer-plane shape. For those two shapes in Top/Plan, inside an undo event after
   `doc.AddBothSwapObject` of both, verify that `AlignShapePlanes` returns `True`, keeps the 2D coordinates of the second
   shape, makes `AreShapesInOnePlane` `True` and lets `CombineShapes` succeed, and that undo restores the plane.
6. In a disposable drawing, create and update a Python script resource using the following round-trip checks.
   The native storage must copy UTF-8 **bytes**, not the number of Unicode characters. This does not execute the
   saved script. Close the disposable drawing without saving afterwards: script/palette deletion is deliberately
   blocked while a script is running.

```python
import uuid
import api

suffix = uuid.uuid4().hex[:12]
text = "# caf\u00e9 \u03a9 \u6f22\u5b57 \U0001f642"
script = api.ScriptResource.Create("UTF8_" + suffix, "UTF8Palette_" + suffix,
                                   text, api.ScriptLanguage.Python)
assert script and script.GetText() == text
updated = text + " updated \u0436"
assert script.SetText(updated) and script.GetText() == updated
assert script.GetLanguage() == api.ScriptLanguage.Python
```

### Domain corrections and compatibility

- Roof edge indices are zero-based for get, set and remove (including the first and last edge).
- Column dimension access uses native shaft/height fields. Composite columns do not have one unambiguous total height:
  `GetTotalHeight()` returns `None` and `SetTotalHeight()` returns `False` for them.
  Architectural shaft shapes map to native Oval/Rectangular. Previously mentioned `"Custom Column"` / `"Symbol Name"`
  fields do not exist in the verified native Column definition; `SetShape("Custom")` returns `False` without mutation.
  Structural steel-shape configuration is a separate workflow and is not exposed by that shaft-shape setter.
- Stake elevation updates both the parameter and insertion matrix. Modes that calculate height from other objects or
  the site model can intentionally replace it during reset; use `Mode.SiteModelSource` for isolated elevation tests.
- Data tag leader endpoints use global/model XY for both accessors. Enable the leader before reading/writing it.
  A disabled leader returns `None`/`False`. A tilted enclosing plug-in object can make global XY unavailable through the
  native XY-only provider; the getter returns `None` rather than inventing a coordinate.
- `LandscapeAreaObject.PlantDisplay2D` exposes `None_`, `PlantCloud`, `PlantLine`, and `PlantSymbols`.
  `GetPlantDisplay2D()` / `SetPlantDisplay2D(value)` preserve all native popup choices. Existing `GetShowPlantsIn2D()`
  returns true for any non-None display; `SetShowPlantsIn2D(True)` selects PlantSymbols and false selects None_.
  MCP accepts `plantDisplay2D` (`none`, `plantCloud`, `plantLine`, `plantSymbols`); do not also supply the boolean form.
- Site modifier `Config.FitToObjects` uses its own native configuration, not Aligned.
- Property line `GetDistanceUnits()` / `SetDistanceUnits(value)` access native `Annotation Units`.
- Hardscape `Mode3D` retains existing values and adds `SlabDrainage=5`, `AlignedSlab=6`, `AlignedModifOver=7`,
  `AlignedModifUnder=8`. Unknown native codes return `None`, not the valid `None_` mode.
- Native center marks are anonymous groups without a verified persistent discriminator. `CenterMarkObject.Is(h)`
  conservatively returns false; generic type discovery no longer labels every group as a center mark.
  Retain the wrapper returned by creation, or explicitly wrap a group already known to be a center mark.

Suggested domain regression checks include first/last roof edges and bounds, stake height after reset,
site modifier configuration, all landscape area display modes and boolean compatibility, property line units,
and decoding every hardscape mode. Additional manual cases: composite and story-bound columns, typed hardscape
changes followed by reset, translated/rotated data tags both associated and unassociated (including walls/trusses),
and MCP error reporting/failed-creation cleanup. Path factories consume their path on success: delete the resulting
plug-in object, not the original path handle separately.

### Resource correctness and undo

- Gradient get/set/remove/insert indices are zero-based, including the final stop. Insertion returns the inserted
  index or `None`; native sorting can change indices after an edit.
- Hatches expose the native level count, not an eight-level subset. `SetLevel(count, level)` appends; indices greater
  than count fail. Use `repeatVector` for line direction/repeat and `offsetVector` for parallel-line spacing.
- Record field defaults are parsed before the typed native field is added. With `updateExistingRecords=True`, existing
  attached records receive the requested default, not an intermediate zero/empty value. Fill and PenStyle defaults
  use resource names (hatch/tile/gradient/image for Fill, line type for PenStyle). Invalid defaults return `kNotFound`.
  Color defaults are comma-separated 16-bit RGB components; PenWeight is an integer. Empty defaults use the type's
  empty value. Plug-in-only/unsupported field types are not promised to be creatable in ordinary record formats.
- Folder paths use real create/reuse/move operations instead of the unimplemented native path helper. Use
  `CreatePathFolders` when you need to register undo only for newly created folders.
- MCP `createResource` reports `created` when creation can be determined; reusing an existing worksheet/style/resource never registers that resource
  as newly inserted. Description edits on reused resources are registered as modifications.
  Simple line types are shared by dash pattern and native code owns their undo; the response omits `created` and explains
  that an existing matching type may have been returned. Failed undo registration returns an explicit error; newly
  created untracked folders are removed, while a non-folder resource may remain and is identified in the error.
- MCP `importResource` reports `imported`; the native import owns undo registration. Returning a pre-existing resource
  must not make undo delete that resource.

Manual undo/redo checks must include creation versus reuse of a worksheet/style, nested folder reuse and partial
name conflicts, importing a new resource, and importing with a conflict policy that returns an existing resource.
Also attach a record before adding Integer/Text/Fill/PenStyle fields with defaults; verify the old record receives
each requested value and invalid defaults do not add a field. Perform these checks in a disposable drawing.
