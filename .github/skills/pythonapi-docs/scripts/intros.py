"""Hand-written parts of the documentation: group titles and introductions, and README.md."""

import collections
import re

FOLDERS = {
    '.': {
        'title': 'DocumentAccess — document, layers, stories and preferences',
        'name': 'DocumentAccess',
        'short': 'The active document: selection, objects, layers, stories, classes, view, units, undo and preferences.',
        'intro': [
            '`api.Document` is the entry point of the API: a stateless facade over the active drawing. Construct it on demand '
            'with `api.Document()` and use it to reach the selection, layers, stories, classes, objects, the view, units, undo '
            'and the typed preference views (`DisplaySettings`, `EditingSettings`, `SnapSettings`, `GridSettings`, '
            '`StackLayersSettings`, `UnitSettings`, `TextDefaults`, `DefaultAttributes`, `ProgramVariables`).',
            'Vectorworks vocabulary used below: a **layer** is a design layer (a world coordinate plane at a given scale) or a '
            'sheet layer (a printable page); a **story** is a floor of the building at an elevation that groups the design layers '
            'of its levels; a **level type** is the name of a story level (for example "Slab"); a **class** is a named style '
            'container whose "by class" attributes objects inherit; a **container** is anything that holds objects (a layer, a '
            'group, a symbol definition, a viewport).',
            'Shared conventions: getters return `None` when a value cannot be obtained, setters and actions return `False` on '
            'failure; lengths and coordinates are world units, angles radians (counter-clockwise), strings UTF-8. Object handles '
            'are `api.Handle` (`vs.Handle`) objects; pass `None` for a null handle. Use `Document.As(type, h)` to get a typed '
            'object of a handle.',
        ],
    },
    'Attributes': {
        'title': 'Attributes — graphic attributes and classes',
        'name': 'Attributes',
        'short': 'Pen, fill, fill mapping, markers, drop shadow, object attributes, classes and the attribute value types.',
        'intro': [
            'The attribute classes describe how objects look. `ObjectAttributes` gathers all graphic attributes of one object '
            '(`Pen()`, `Fill()`, `FillMapping()`, `Markers()`, `DropShadow()`); `PenAttributes` covers the stroke (colors, '
            'style, line weight, opacity), `FillAttributes` the fill (colors, style, opacity), `FillMappingAttributes` the '
            'mapping of hatch, tile, gradient and image fills, `MarkerAttributes` the beginning and end markers and '
            '`DropShadowAttributes` the drop shadow. `ClassAttributes` represents a class definition: a named, saved set of '
            'attributes shared by many objects.',
            'The value types `ColorRGB`, `ColorPair`, `ObjectColors`, `Marker`, `DropShadow`, `WallTextures`, `RoofTextures` and '
            '`Point2D`, the attribute enumerations and the module constant `api.kMaxOpacity` belong to this group as well.',
            '**"By class":** an attribute set "by class" ignores the object\'s own value and uses the value of the class the '
            'object belongs to. Query and change it with the `Get...ByClass` / `Set...ByClass` methods of the attribute classes.',
        ],
    },
    'ObjectPrimitives': {
        'title': 'ObjectPrimitives — 2D primitive objects',
        'name': 'ObjectPrimitives',
        'short': 'The common object base (PrimitiveObject) and 2D objects: lines, rectangles, arcs, circles, polygons, polylines, groups, plug-in objects, text.',
        'intro': [
            'The 2D object classes. Every object class is a lightweight view of a drawing object: copying a Python object does '
            'not copy the drawing object, and deleting it does not delete the drawing object.',
            '`PrimitiveObject` is the common base of **every** object class of the API (including the 3D, annotation, '
            'architectural, landscape, Spotlight and ConnectCAD objects): identity, hierarchy, state, attributes and '
            'transforms are documented once there. `ParametricObject` represents any plug-in object (use it when no specific '
            'class exists); `PolyObject` is the shared base of `PolygonObject` and `PolylineObject`; `RectangularObject` is '
            'the shared base of the rectangle classes.',
            'Getters return `None` when a value is not available and setters return `False` on failure. Coordinates are '
            'world units, angles radians (counter-clockwise from the X axis).',
        ],
    },
    'Math': {
        'title': 'Math — standalone 2D and 3D math (`api.Math`)',
        'name': 'ObjectPrimitives.Math',
        'short': 'The api.Math submodule: points/vectors, transforms, rectangles, lines, planes, circles, arcs, polygons, utilities.',
        'intro': [
            '`api.Math` is a submodule of standalone math values that need no drawing (import it with '
            '`from api.Math import Point2D` or use `api.Math.Point2D`): points and vectors (`Point2D` = `Vector2D`, '
            '`Point3D` = `Vector3D`), transforms (`Transform2D`, `Transform3D`), rectangles (`Rect2D`, `RotatedRect2D`), lines '
            '(`Line2D`, `Line3D`), planes (`Plane3D`), circles (`Circle2D`), arcs (`Arc2D`) and polygons (`Polygon2D` made of '
            '`PolyVertex` values), plus utility functions and constants.',
            'All angles are radians, measured counter-clockwise from the positive X axis. Changing a returned value never '
            'changes a drawing object: pass the value back to the object\'s setter.',
        ],
    },
    'Objects3D': {
        'title': 'Objects3D — 3D objects',
        'name': 'Objects3D',
        'short': 'Extrudes, multiple extrudes, sweeps, solids, primitives (sphere, cone, ...), NURBS, 3D polygons, meshes, shells.',
        'intro': [
            'The 3D object classes: extrudes, multiple extrudes and sweeps, solid objects (solid additions, subtractions and '
            'intersections, which keep their modeling history, and history-free generic solids), solid primitives (spheres, '
            'hemispheres, cones, ...), NURBS curves and surfaces, '
            '3D polygons, meshes, shell solids and surface models. All of them derive from '
            '[`PrimitiveObject`](ObjectPrimitives.md#primitiveobject), so the shared object operations (name, class, layer, '
            'attributes, bounds, moving, deleting, ...) are documented there.',
            'Coordinates are world units in the 3D model space; angles are radians.',
        ],
    },
    'ObjectsAnnotation': {
        'title': 'ObjectsAnnotation — dimensions, data tags, title block borders and worksheets',
        'name': 'ObjectsAnnotation',
        'short': 'Dimensions (linear, angular, arc length, radial), center marks, data tags, title block borders, worksheets.',
        'intro': [
            'The annotation classes. Annotation objects do not describe the building, they describe the drawing: they read '
            'data out of objects and the document and print it on the sheet.',
            '`AnnotationObject` is the base of the plug-in based annotations (`DataTagObject` labels an object with data read '
            'from it, `TitleBlockBorderObject` is the sheet border, zone grid and title block). Both take their graphics from '
            'an object **style**, so their `Create` functions resolve a style (importing one from the Vectorworks content when '
            'the drawing has none) and fail when none is available.',
            'Dimensions are the other half of annotation: `DimensionObject` holds the settings every dimension shares, and '
            '`LinearDimensionObject`, `AngularDimensionObject`, `ArcLengthDimensionObject` and `RadialDimensionObject` measure '
            'distances, angles, arc lengths and radii/diameters. Unlike data tags and title block borders, dimensions are '
            'native objects without a plug-in record or style: their look comes from the dimension standard they reference. '
            '`CenterMarkObject` is the center cross of a circle or arc (a group of lines, not a dimension). '
            '`WorksheetObject` edits worksheet resources.',
        ],
    },
    'ObjectsArchitect': {
        'title': 'ObjectsArchitect — walls, roofs, slabs, windows, doors, columns, stairs',
        'name': 'ObjectsArchitect',
        'short': 'Architectural objects: walls, roofs, slabs, windows, doors, columns and stairs.',
        'intro': [
            'The classes of the main architectural objects. `ArchitectObject` is their common base (it extends '
            '`PrimitiveObject` with access to the parameters of plug-in objects; for walls and roofs those accessors return '
            'nothing).',
            'Walls (`WallObject`) and roofs (`RoofObject`) are native Vectorworks objects. Slabs, windows, doors, columns and '
            'stairs are plug-in objects recognized by their universal name ("Slab", "Window", "Door", "Column2", "Stairs CW"); '
            'the static `Is(h)` of each class checks it.',
            'Conventions: `Is(h)` tests the object kind, `Create(...)` creates a new instance in the active layer / current '
            'container, typed getters return `None` for an invalid object or a missing field, typed setters return `True` on '
            'success. `WindowObject.Create` and `DoorObject.Create` place a free-standing instance at a point.',
        ],
    },
    'ObjectsConnectCAD': {
        'title': 'ObjectsConnectCAD — ConnectCAD devices and sockets',
        'name': 'ObjectsConnectCAD',
        'short': 'ConnectCAD schematic devices (created from JSON descriptions), sockets, device types, signal and connector types.',
        'intro': [
            'The ConnectCAD classes (they require ConnectCAD). `ConnectCADDeviceObject` is a schematic device ("Device") with '
            'its sockets, created from a JSON device description; it can also create a device-type symbol that stores the full '
            'description. `ConnectCADSocketObject` is a connection point of a device ("Socket": IN, OUT or IO; loops are socket '
            'pairs). `ConnectCADLibrary` lists the signal and connector types, validates device descriptions and reads the '
            'Device Definition record of device types.',
            'Generic parameter access comes from [`ParametricObject`](ObjectPrimitives.md#parametricobject).',
        ],
    },
    'ObjectsLandmark': {
        'title': 'ObjectsLandmark — plants, site models, hardscapes and other landscape objects',
        'name': 'ObjectsLandmark',
        'short': 'Landmark objects: plants, landscape areas, site models and modifiers, stakes, hardscapes, property lines, existing trees.',
        'intro': [
            'The classes of the Landmark plug-in objects. `LandmarkObject` is their common base (generic parameter access). '
            'The specific classes are `PlantObject` ("Plant"), `LandscapeAreaObject` ("Landscape Area"), `SiteModelObject` '
            '("DTM6", a terrain model with existing and proposed surfaces), `SiteModifierObject` ("Site Modifiers"), '
            '`StakeObject` ("Stake Object"), `HardscapeObject` ("Hardscape"), `PropertyLineObject` ("Property Line") and '
            '`ExistingTreeObject` ("Existing Tree").',
            'All landmark objects are plug-in objects, told apart by the universal name of their record. `Is(h)` tests that '
            'name, `Create(...)` creates a new instance in the active layer / container, getters return `None` for an invalid '
            'object or a missing parameter and setters return `True` on success.',
        ],
    },
    'ObjectsSpotlight': {
        'title': 'ObjectsSpotlight — lighting devices and GDTF fixture types',
        'name': 'ObjectsSpotlight',
        'short': 'Spotlight lighting devices and the GDTF fixture-type library (import, available modes).',
        'intro': [
            'The Spotlight classes (they require Spotlight). `LightingDeviceObject` is a fixture of the lighting plot '
            '("Lighting Device"), drawn from a lighting device symbol, a GDTF fixture type or both. `GDTFLibrary` lists the '
            'GDTF fixture types available to Spotlight and imports `.gdtf` files into the drawing.',
            'Generic parameter access comes from [`ParametricObject`](ObjectPrimitives.md#parametricobject).',
        ],
    },
    'Resources': {
        'title': 'Resources — resources, resource lists and typed resources',
        'name': 'Resources',
        'short': 'The Resource Manager side: resources of any kind, resource lists and import, and typed resources (hatches, symbols, styles, ...).',
        'intro': [
            'The resource classes (the Resource Manager side of the API). `Resource` is one resource of any kind (name, '
            'description, folder, contents, lifetime). `ResourceList` lists the resources of one kind from the current drawing '
            'or from external content (the Vectorworks libraries, a file, another open document) and imports them into the '
            'drawing. `TypedResource` is the base of the typed resource classes; a typed resource object is invalid unless its '
            'handle really is a resource of its kind, so it can never act on the wrong resource.',
            'The typed classes add what only their kind has: hatches, gradients, tiles and image fills; line types; symbol '
            'definitions; textures, render styles and backgrounds; record formats; worksheets; text, wall, slab, roof and '
            'viewport styles; materials; data visualizations and resource folders. Classes are resources too, but '
            'they are covered by [`ClassAttributes`](Attributes.md#classattributes).',
        ],
    },
    'Scripting': {
        'title': 'Scripting — script resources and script palettes',
        'name': 'Scripting',
        'short': 'Script resources (VectorScript / Python) and script palettes stored in the document.',
        'intro': [
            'The scripting classes: `ScriptResource` is a VectorScript or Python script stored in the current document '
            '(create, find, read, change and delete it) and `ScriptPalette` is a script palette, the named group of script '
            'resources that Vectorworks shows as a floating palette and as a folder of scripts in the Resource Manager.',
            'Scripts can be created, read, changed and organized through this API; running them is not part of the API.',
        ],
    },
    'UIAutomation': {
        'title': 'UIAutomation — tools, the Tool bar, menus and the Object Info palette',
        'name': 'UIAutomation',
        'short': 'Drive the user interface: tools and their activation, Tool bar (mode bar), tool input, menu commands and chunks, Object Info palette controls.',
        'intro': [
            'The user interface automation classes. `ToolAccess` is the tool catalogue (activate tools), `ModeBar` reads and '
            'changes the modes of the active tool and `ToolControl` drives the active tool with clicks, drags, mouse moves and '
            'keys. `MenuAccess` lists and executes menu commands and chunk items. `OIPAccess` lists, reads and operates the '
            'controls the Object Info palette shows for the selection.',
            'Conventions: getters return `None` when a value cannot be obtained, setters/actions return `True` on success; '
            'name comparisons are case-insensitive; all indexes are 0-based, mode indexes and chunk item indexes included. '
            'Operating the user interface behaves exactly like user input: tools may rebuild their Tool bar (mode bar), '
            'commands show their dialogs and set up their own undo, Object Info palette changes rebuild the palette — re-read '
            'values after a change instead of caching them, and do not execute menu commands inside an undo event opened with '
            '`Document.StartUndoEvent`.',
            'Built-in tools and commands use a negative number as universal name (for example "-207"); for those the English '
            'name is accepted as well. Model coordinates are world units; view coordinates are pixels from the top-left corner '
            'of the view pane (y grows downwards).',
        ],
    },
    'UILayoutCreate': {
        'title': 'UILayoutCreate — alerts, standard dialogs and layout dialogs',
        'name': 'UILayoutCreate',
        'short': 'Alerts and questions, ready-made value dialogs, and modal dialogs built control by control.',
        'intro': [
            'The user interface classes: `Alerts` (message boxes, questions, warnings and errors), `StandardDialogs` '
            '(ready-made dialogs that edit one or two values or choose from a list) and `LayoutDialog` (any modal dialog, built '
            'control by control, with event handlers written in Python). The value types `DialogEvent` and `ListBrowserEvent` '
            'and the dialog enumerations belong to this group too.',
            'Dialogs are modal: `Run()` returns when the user closes the dialog. Control values stay readable after `Run()`.',
        ],
    },
}


# ----------------------------------------------------------------------------------------------------------------
def readme(docs):
    from render import FOLDER_DOCS, anchor, esc, first_sentence
    lines = []
    w = lines.append
    w('# Vectorworks Python API (`api`) — reference for %s' % docs.version_label)
    w('')
    w('This reference documents the object-oriented Python module `api` that Vectorworks provides for scripts and AI '
      'workflows. It is organized by feature group: one page per group, with a table of contents at the top of every page '
      'and the same layout for every class.')
    w('')
    w('## Table of contents')
    w('')
    toc = [
        ('Getting started', 0), ('Conventions', 0), ('Modules', 1), ('Reading the signatures', 1), ('Calling functions', 1),
        ('Records', 1), ('Enumerations', 1), ('Handles and objects', 1), ('Copying, printing and hashing', 1),
        ('Callbacks', 1), ('Errors', 1), ('API tree', 0), ('Contents by group', 0), ('Index A–Z', 0), ('Page layout', 0),
        ('Statistics', 0),
    ]
    for title, level in toc:
        w('%s- [%s](#%s)' % ('  ' * level, title, anchor(title)))
    w('')

    w('## Getting started')
    w('')
    w('```python')
    w('import api')
    w('from api.Math import Point2D')
    w('')
    w('doc = api.Document()')
    w('if doc.IsOpen():')
    w('    for h in doc.GetSelection():')
    w('        obj = api.PrimitiveObject(h)')
    w('        print(obj.GetName(), obj.GetBounds())')
    w('```')
    w('')
    w('- Start with [`api.Document`](DocumentAccess.md#document): the active drawing, its selection, layers, stories, '
      'classes and preferences.')
    w('- Shared drawing-object operations are documented on [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject). '
      'Follow each class\'s inheritance information: for example, [`WorksheetObject`](ObjectsAnnotation.md#worksheetobject) '
      'derives from `TypedResource`, not `PrimitiveObject`.')
    w('- Pure math values live directly in the submodule [`api.Math`](ObjectPrimitives.Math.md); they do not create drawing objects.')
    w('- `help(api.Document)` in Vectorworks prints the signatures of a class.')
    w('')
    w('Use only `api` and `api.Math` for the Vectorworks operations described here. Do not mix calls to the separate `vs` '
      'interface or use it as a fallback for missing features. Standard-library imports are fine; report unsupported '
      'operations rather than inventing API calls.')
    w('')
    w('[Script resources and palettes](Scripting.md) can be managed but scripts cannot be executed through `api`. '
      'Automation of already-open dialogs and the deferred helpers `RunLater` / `RunOnEventLoop` are unavailable; '
      '[dialog creation, alerts and standard dialogs](UILayoutCreate.md) remain supported. See '
      '[AI-CONTEXT.md](AI-CONTEXT.md) for the complete usage rules and recipes.')
    w('')

    # -- conventions ---------------------------------------------------------------------------------------------
    w('## Conventions')
    w('')
    w('| Topic | Convention |')
    w('|---|---|')
    w('| Results | Getters return `None` when a value cannot be obtained, except that handle getters return a null handle, '
      'collection getters an empty list and count getters zero. Drawing-object factories return invalid objects on failure. Most setters '
      'and actions return `True` / `False`; check each signature and its result. |')
    w('| Units | World lengths and coordinates are millimetres, regardless of document units. Use `Document.UnitsToWorld` / '
      '`Document.WorldToUnits` to convert document units. Angles are radians, counter-clockwise from +X, unless specified otherwise. |')
    w('| Unit exceptions | `Marker.angle`, `DropShadow.angle` and `RoofObject.Edge.slope` use degrees; `Marker.length` / '
      '`Marker.width` use page inches. `*Mils` line weights use 1/1000 inch. Raw plug-in angle parameters read/written with '
      '`GetParamReal` / `SetParamReal` use degrees; length parameters use world units. |')
    w('| Indexes | Zero-based, except worksheet rows and columns, which are one-based. |')
    w('| Colors | `ColorRGB` channels are 0–65535; use `ColorRGB.FromRGB8` / `Red8()` for 8-bit values. Color indices are '
      'palette indices, not RGB values. Opacity is 0–100 (`api.kMaxOpacity`). |')
    w('| Strings | Python `str`, exchanged as UTF-8. Name lookups ignore case, but pass plug-in universal names exactly. |')
    w('| Handles | Pass `None` for a null handle argument. A returned null `api.Handle` is falsy: test `if h:`, not '
      '`h is None`. Object classes are lightweight views of a handle; `bool(obj)` is equivalent to `IsValid()`. |')
    w('| Undo | Drawing changes require an undo event and the appropriate object registrations; read-only scripts must not '
      'start an event. See the [undo workflow](AI-CONTEXT.md#3-undo---required-around-every-drawing-change) for '
      '`StartUndoEvent(isRevertible=True)`, rollback and application-managed events. |')
    w('| Names | Members whose names are Python keywords end with an underscore (`None_`), and so do keyword-like argument names (`from_`). |')
    w('| Records | Value types are Python-owned copies: change them, then pass them back to the setter. They can be constructed from field values (`api.ColorRGB(red=65535)`). |')
    w('| Enumerations | `IntEnum` (`api.Descend` is an `IntFlag`); plain integers are accepted. |')
    w('| Arguments | Every parameter has a keyword name; parameters with defaults can be omitted; tuples, lists and dicts are accepted for record arguments. |')
    w('| Signatures | `Name(param: type = default) -> result`; *static* marks static methods; `T \\| None` is an optional result. |')
    w('')

    w('### Modules')
    w('')
    w('| Name | What it is |')
    w('|---|---|')
    w('| `api` | The module. Start with `api.Document()`. |')
    w('| `api.Math` | Direct submodule of `api` with standalone 2D/3D math ([Math](ObjectPrimitives.Math.md)); '
      '`import api.Math` and `from api.Math import Point2D` work. It is not nested under `ObjectPrimitives`. |')
    w('| `api.Object` | Base class of every `api` class (see [Copying, printing and hashing](#copying-printing-and-hashing)). |')
    w('| `api.Handle` | A Vectorworks object handle. Test returned handles for truth rather than comparing them with `None`. |')
    w('')

    w('### Reading the signatures')
    w('')
    w('The signatures use these types:')
    w('')
    w('| Type | Meaning |')
    w('|---|---|')
    w('| `bool`, `int`, `float`, `str` | Python built-in values. An `int` is accepted where a `float` is expected. |')
    w('| `Handle` | A Vectorworks object handle (`api.Handle`). Pass `None` for a null handle argument; returned null handles '
      'are falsy. Any object with `GetHandle()` is accepted as well. |')
    w('| `T \\| None` | An optional value: `None` means "no value". |')
    w('| `list[T]` | A list (a list or a tuple is accepted as argument). |')
    w('| `tuple[T * N]` | A tuple of exactly N values. |')
    w('| `tuple[A, B]` | A pair of values. |')
    w('| `dict[K, V]` | A dictionary. |')
    w('| `callable(A, ...)` | Any Python callable that takes the listed arguments (see [Callbacks](#callbacks)). |')
    w('| `bytes` | `bytes`, `bytearray` or any other buffer (not `str`). |')
    w('| `type` | An `api` class, for example `api.ArcObject` in `api.Document.As(api.ArcObject, h)`; only classes with a static `Is(h)` and a constructor from a handle qualify. |')
    w('| `object` | Any Python object; the method description tells what is returned. |')
    w('| enumeration names | `IntEnum` / `IntFlag` classes; plain integers are accepted. |')
    w('| class names | `api` classes; record arguments also accept tuples, lists and dicts (see [Records](#records)). |')
    w('')
    w('Default values are shown as Python expressions (`2**64 - 1` means "no limit"). Methods with several rows of the '
      'same name accept several argument lists (overloads).')
    w('')

    w('### Calling functions')
    w('')
    w('- **Overloads:** when a method accepts several argument lists, the first one that fits the arguments is used, first '
      'with exact types, then with the conversions described here. When record types distinguish overloads, construct the '
      'type explicitly: a tuple passed to `ToolControl.Click` selects `Point2D`, so use `api.Point3D(...)` or '
      '`api.ViewPoint(...)` for the other coordinate types.')
    w('- **Keywords and defaults:** every parameter can be passed by keyword (using the names in the signatures); '
      'parameters with a default value can be omitted.')
    w('- **Static methods:** methods marked *static* can be called on the class (`api.ArcObject.Create(...)`) or through '
      'an instance. When a name has both static and instance rows, call it through an instance.')
    w('- **Conversions:** a record argument can be given as a tuple or list (the values of a constructor), as a dict '
      '(field values) or as a compatible record (`api.Math.Point2D` and `api.Point2D`, as well as `api.Math.Point3D` and '
      '`api.Point3D`, convert into each other); an `int` is '
      'accepted for a `bool` or a `float`; any object with a `GetHandle()` method is accepted where a `Handle` is expected.')
    w('- **Results:** results are new Python values, except for methods that change a value in place and return it (for '
      'example `Math.Point2D.Normalize()`): they return the same Python object, so calls can be chained.')
    w('- **Operators:** comparison and arithmetic operators return `NotImplemented` for unsupported operands, so Python can '
      'try the reflected operation.')
    w('')

    w('### Records')
    w('')
    w('Records (value types such as `api.ColorRGB`, `api.WallObject.Heights`, `api.Math.Point2D`) are Python-owned values. '
      'Changing a record never changes the drawing: pass it back to the setter it came from.')
    w('')
    w('When no constructor accepts the arguments, a record can also be constructed from field values: all fields '
      'positionally (in the order of the Fields tables, fields of the base class first) or any fields as keywords, for '
      'example `api.ColorRGB(red=65535)`. Classes with neither constructors nor fields cannot be constructed from Python.')
    w('')
    w('A field whose type is itself a record reads as a live view into its owner (`rect.origin.x = 1` changes `rect`); '
      'fields of other types (numbers, strings, lists, optional values) read as copies. Fields cannot be deleted.')
    w('')
    w('### Enumerations')
    w('')
    w('Enumerations are `enum.IntEnum` classes (`api.Descend` is an `enum.IntFlag`: combine its members with `|`). '
      'Nested enumerations live in their class (`api.TextObject.HorizontalAlignment`). Members whose names are Python '
      'keywords end with `_` (`api.Descend.None_`). Plain integers are accepted as arguments, and values without a member '
      'come back as integers.')
    w('')
    w('### Handles and objects')
    w('')
    w('Object handles are `api.Handle` values. Pass `None` for a null handle argument, but test returned handles with '
      '`if h:`: a null handle is not `None`. Handle compatibility does not justify mixing `api` and `vs`. The '
      'object classes are lightweight views of a handle: they do not own the drawing object. Most have a static `Is(h)` '
      'and a constructor from a handle; constructing one from a handle of the wrong kind gives an invalid object '
      '(`IsValid()` / `bool(obj)` is `False`). `api.Document.As(type, h)` returns a typed object or `None`.')
    w('')
    w('The base views `PrimitiveObject(h)`, `ArchitectObject(h)`, `LandmarkObject(h)` and `AnnotationObject(h)` accept '
      'any non-null handle; concrete classes check the object kind. `Delete()` invalidates the view on which it is called. '
      'Never use other views or handles of the deleted object.')
    w('')
    w('### Copying, printing and hashing')
    w('')
    w('Every `api` class derives from `api.Object`, which provides:')
    w('')
    w('| Member | Description |')
    w('|---|---|')
    w('| `copy.copy(x)` / `copy.deepcopy(x)` | A copy of the value. For an object class this copies the view (the handle), **not** the drawing object; use `Duplicate()` to duplicate drawing objects. Raises `TypeError` for classes that cannot be copied (for example `ResourceList`). |')
    w('| `repr(x)` | Records print their fields (`api.ColorRGB(red=0, green=0, blue=0)`), object classes their handle (`<api.ArcObject handle=0x...>`), instances whose `__init__` was not called `<... (not initialized)>`. |')
    w('| `hash(x)` | Object classes hash by their handle, so they can be dictionary keys or set members; records are not '
      'hashable. Drawing objects, layers, classes and resources compare by handle with `==`. Value-type equality is '
      'documented in the Operators tables; other Python objects compare by identity. |')
    w('')
    w('### Callbacks')
    w('')
    w('Parameters of type `callable(...)` take any Python callable (for example the traversal `Document.ForEachObject`). The '
      'callable is called synchronously and its return value is ignored; it cannot stop traversal early. Use the '
      'list-returning counterpart when you need to stop early. When a call raises, the remaining calls are skipped '
      'and the exception propagates once the method returns.')
    w('')
    w('### Errors')
    w('')
    w('Operational failures use the documented return values; always check results. Python usage and conversion errors '
      'and the failed geometry operations listed below raise exceptions as described below, and callback exceptions propagate to the caller.')
    w('')
    w('| Situation | Python exception |')
    w('|---|---|')
    w('| No argument list of the method fits the arguments | `TypeError`, listing every signature of the method. |')
    w('| Constructing a class that cannot be constructed from Python, or using an instance whose `__init__` was not called (for example in a subclass) | `TypeError`. |')
    w('| Setting a field to a value of the wrong type, deleting a field | `TypeError`. |')
    w('| Copying a class that cannot be copied | `TypeError`. |')
    w('| An index out of range of a math value (for example `Polygon2D`) | `IndexError`. |')
    w('| A failed geometry operation: `Math.Polygon2D` `Union`, `Intersection`, `Difference`, `SymmetricDifference`, `Offset`; `PolyObject` `BooleanUnion`, `BooleanIntersection`, `BooleanDifference`, `BooleanSymmetricDifference`, `CombineShapes` | `RuntimeError` with a message. |')
    w('| A result that cannot be converted | `RuntimeError`. |')
    w('| The module could not be initialized | `ImportError` on `import api`. |')
    w('')

    # -- tree ------------------------------------------------------------------------------------------------
    w('## API tree')
    w('')
    w('`Math` is a direct submodule of `api`. The other entries below are documentation groups for names exposed '
      'directly on `api` (for example `api.Document` and `api.PrimitiveObject`), not Python submodules. Reference '
      'filenames do not define Python namespaces: `ObjectPrimitives.Math.md` documents `api.Math`.')
    w('')
    w('```text')
    tree = [
        ('api', None, 0),
        ('Math  (api.Math)', 'ObjectPrimitives.Math.md', 1),
        ('DocumentAccess', 'DocumentAccess.md', 1),
        ('Attributes', 'Attributes.md', 1),
        ('ObjectPrimitives', 'ObjectPrimitives.md', 1),
        ('Objects3D', 'Objects3D.md', 1),
        ('ObjectsAnnotation', 'ObjectsAnnotation.md', 1),
        ('ObjectsArchitect', 'ObjectsArchitect.md', 1),
        ('ObjectsConnectCAD', 'ObjectsConnectCAD.md', 1),
        ('ObjectsLandmark', 'ObjectsLandmark.md', 1),
        ('ObjectsSpotlight', 'ObjectsSpotlight.md', 1),
        ('Resources', 'Resources.md', 1),
        ('Scripting', 'Scripting.md', 1),
        ('UIAutomation', 'UIAutomation.md', 1),
        ('UILayoutCreate', 'UILayoutCreate.md', 1),
    ]
    level1 = [t for t in tree if t[2] == 1]
    for name, doc, level in tree:
        if level == 0:
            w(name)
            continue
        if level == 1:
            prefix = '└── ' if (name, doc, level) == level1[-1] else '├── '
        else:
            prefix = '│   └── '
        w('%-34s → %s' % (prefix + name, doc))
    w('```')
    w('')

    # -- contents by group --------------------------------------------------------------------------------------
    w('## Contents by group')
    w('')
    for folder, doc in FOLDER_DOCS.items():
        info = FOLDERS[folder]
        display = 'Math (`api.Math`)' if folder == 'Math' else info['name']
        w('- **[%s](%s)** — %s' % (display, doc, info['short']))
        classes = [c for c in docs.cls_info.values() if c['folder'] == folder]
        enums = [e for e in docs.enum_info.values() if e['folder'] == folder]
        classes.sort(key=lambda c: (docs.file_rank(c['file']), c['pos']))
        enums.sort(key=lambda e: (docs.file_rank(e['file']), e['pos']))
        top = [c for c in classes if not c['nested_in']]
        if top:
            w('  - Classes:')
            for c in top:
                nested = [n for n in classes if n['nested_in'] and n['qualname'].startswith(c['qualname'] + '.')]
                nested += [e for e in enums if e['nested_in'] and e['qualname'].startswith(c['qualname'] + '.')]
                line = '    - [`%s`](%s#%s)' % (c['py'], doc, anchor(c['py']))
                if nested:
                    line += ' — ' + ' · '.join('[`%s`](%s#%s)' % (n['py'].split('.', 1)[1] if not n['py'].startswith('Math.') else n['py'].split('.', 2)[2], doc, anchor(n['py'])) for n in nested)
                w(line)
        top_enums = [e for e in enums if not e['nested_in']]
        if top_enums:
            w('  - Enumerations: ' + ' · '.join('[`%s`](%s#%s)' % (e['py'], doc, anchor(e['py'])) for e in top_enums))
        mods = docs.module_members.get(folder, [])
        if mods:
            funcs = [r for r in mods if r.kind == 'Def']
            consts = [r for r in mods if r.kind == 'Constant']
            if funcs:
                w('  - [Module functions](%s#module-functions): %s' % (doc, ', '.join('`%s`' % n for n in sorted(set(r.name for r in funcs)))))
            if consts:
                w('  - [Module constants](%s#module-constants): %s' % (doc, ', '.join('`%s`' % r.name for r in consts)))
    w('')

    # -- A-Z index ------------------------------------------------------------------------------------------------
    w('## Index A–Z')
    w('')
    entries = []
    for c in docs.cls_info.values():
        kind = 'class (nested)' if c['nested_in'] else 'class'
        entries.append((c['py'], kind, c['folder'], first_sentence(docs.class_description(c), 110)))
    for e in docs.enum_info.values():
        kind = ('IntFlag' if e['flag'] else 'IntEnum') + (' (nested)' if e['nested_in'] else '')
        entries.append((e['py'], kind, e['folder'], first_sentence(docs.enum_description(e), 110)))
    entries.sort(key=lambda x: (x[0].replace('Math.', '').lower(), x[0]))
    letters = sorted(set(x[0].replace('Math.', '')[0].upper() for x in entries))
    w(' · '.join('[%s](#%s)' % (L, anchor('index-' + L)) for L in letters))
    w('')
    current = None
    for name, kind, folder, summary in entries:
        L = name.replace('Math.', '')[0].upper()
        if L != current:
            if current is not None:
                w('')
            current = L
            w('### Index %s' % L)
            w('')
            w('| Name | Kind | Page | Summary |')
            w('|---|---|---|---|')
        doc = FOLDER_DOCS[folder]
        page = 'Math' if folder == 'Math' else FOLDERS[folder]['name']
        w('| [`%s`](%s#%s) | %s | [%s](%s) | %s |' % (name, doc, anchor(name), kind, page, doc, esc(summary)))
    w('')

    w('## Page layout')
    w('')
    w('Every group page follows the same layout:')
    w('')
    w('1. **Title** — the group, the Python module and the Vectorworks version.')
    w('2. **Table of contents** — every class, nested type and enumeration of the page.')
    w('3. **Overview** — one row per type with its base class and a one-line summary.')
    w('4. **Classes** — for each class: its full name, what it inherits from, a description, then tables of constructors, '
      'methods (grouped by topic), operators, fields and constants. Nested classes and enumerations follow their owner. '
      'Inherited methods are documented once, on the base class.')
    w('5. **Enumerations** — members with their numeric values and descriptions.')
    w('')
    w('In Vectorworks, `dir(api)` and `help(...)` show what is available in the running version.')
    w('')

    w('## Statistics')
    w('')
    w('| Page | Classes | Enumerations | Methods | Constructors | Fields | Constants |')
    w('|---|---|---|---|---|---|---|')
    tot = collections.Counter()
    for folder, doc in FOLDER_DOCS.items():
        ncls = sum(1 for c in docs.cls_info.values() if c['folder'] == folder)
        nen = sum(1 for e in docs.enum_info.values() if e['folder'] == folder)
        mem = [r for r in docs.members if r.folder == folder]
        nm = len(set((r.owner, r.name) for r in mem if r.kind == 'Def'))
        nc = sum(1 for r in mem if r.kind == 'Init')
        nf = sum(1 for r in mem if r.kind == 'Field')
        nk = sum(1 for r in mem if r.kind == 'Constant')
        tot.update({'c': ncls, 'e': nen, 'm': nm, 'i': nc, 'f': nf, 'k': nk})
        page = 'Math' if folder == 'Math' else FOLDERS[folder]['name']
        w('| [%s](%s) | %d | %d | %d | %d | %d | %d |' % (page, doc, ncls, nen, nm, nc, nf, nk))
    w('| **Total** | **%d** | **%d** | **%d** | **%d** | **%d** | **%d** |' % (tot['c'], tot['e'], tot['m'], tot['i'], tot['f'], tot['k']))
    w('')
    w('Methods count names (several argument lists of one name count once).')
    w('')
    return '\n'.join(lines)
