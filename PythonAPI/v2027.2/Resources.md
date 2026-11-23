**English** • [Deutsch](../../PythonAPI.de/v2027.2/Resources.md) • [日本語](../../PythonAPI.ja/v2027.2/Resources.md)

# Resources — resources, resource lists and typed resources

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The resource classes (the Resource Manager side of the API). `Resource` is one resource of any kind (name, description, folder, contents, lifetime). `ResourceList` lists the resources of one kind from the current drawing or from external content (the Vectorworks libraries, a file, another open document) and imports them into the drawing. `TypedResource` is the base of the typed resource classes; a typed resource object is invalid unless its handle really is a resource of its kind, so it can never act on the wrong resource.

The typed classes add what only their kind has: hatches, gradients, tiles and image fills; line types; symbol definitions; textures, render styles and backgrounds; record formats; worksheets; text, wall, slab, roof and viewport styles; materials; data visualizations and resource folders. Classes are resources too, but they are covered by [`ClassAttributes`](Attributes.md#classattributes).

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [Resource](#resource)
  - [ResourceList](#resourcelist)
    - [ResourceList.Entry](#resourcelistentry)
    - [ResourceList.ImportResult](#resourcelistimportresult)
  - [TypedResource](#typedresource)
  - [HatchLevel](#hatchlevel)
  - [Hatch](#hatch)
  - [GradientSegment](#gradientsegment)
  - [Gradient](#gradient)
  - [Tile](#tile)
  - [ImageFill](#imagefill)
    - [ImageFill.Compression](#imagefillcompression)
  - [LineType](#linetype)
  - [RecordField](#recordfield)
  - [RecordFormat](#recordformat)
  - [Texture](#texture)
    - [Texture.Part](#texturepart)
  - [RenderStyle](#renderstyle)
  - [RenderBackground](#renderbackground)
    - [RenderBackground.Kind](#renderbackgroundkind)
  - [TextStyle](#textstyle)
  - [WallStyle](#wallstyle)
  - [SlabStyle](#slabstyle)
  - [RoofStyle](#roofstyle)
  - [ViewportStyle](#viewportstyle)
  - [BuildingMaterial](#buildingmaterial)
  - [DataVisualization](#datavisualization)
  - [ResourceFolderPath](#resourcefolderpath)
  - [ResourceFolder](#resourcefolder)
  - [SymbolDefinition](#symboldefinition)
    - [SymbolDefinition.GeometryType](#symboldefinitiongeometrytype)
    - [SymbolDefinition.InsertMode](#symboldefinitioninsertmode)
    - [SymbolDefinition.BreakMode](#symboldefinitionbreakmode)
  - [WorksheetCell](#worksheetcell)
  - [WorksheetCellContent](#worksheetcellcontent)
  - [Worksheet](#worksheet)
- [Enumerations](#enumerations)
  - [ResourceType](#resourcetype)
  - [ContentFolder](#contentfolder)
  - [ImportConflict](#importconflict)
  - [RecordFieldType](#recordfieldtype)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`Resource`](#resource) | class |  | One resource, identified by its handle. |
| [`ResourceList`](#resourcelist) | class |  | A list of resources of one kind, coming from the current drawing or from external content. |
| [`ResourceList.Entry`](#resourcelistentry) | class (nested) |  | One entry of the list. |
| [`ResourceList.ImportResult`](#resourcelistimportresult) | class (nested) |  | Outcome of ImportWithResult: the resource in the drawing and whether this call copied it in (`False` when the resource already in the drawing is returned). |
| [`TypedResource`](#typedresource) | class | [`Resource`](#resource) | Resource restricted to one ResourceType. |
| [`HatchLevel`](#hatchlevel) | class |  | One line family of a hatch. |
| [`Hatch`](#hatch) | class | [`TypedResource`](#typedresource) | Vector hatch fill (`ObjectType.HatchDefinition`): a set of line families repeated over the filled area. |
| [`GradientSegment`](#gradientsegment) | class |  | One color stop of a gradient. |
| [`Gradient`](#gradient) | class | [`TypedResource`](#typedresource) | Gradient fill (`ObjectType.GradientDefinition`): a blend between two or more color stops. |
| [`Tile`](#tile) | class | [`TypedResource`](#typedresource) | Tile fill (`ObjectType.TileDefinition`): a group of 2D objects repeated over the filled area on a grid. |
| [`ImageFill`](#imagefill) | class | [`TypedResource`](#typedresource) | Image resource (`ObjectType.ImageDefinition`): a bitmap used as an image fill, as an image prop or as a texture image. |
| [`ImageFill.Compression`](#imagefillcompression) | IntEnum (nested) |  | Compression the image is stored with. |
| [`LineType`](#linetype) | class | [`TypedResource`](#typedresource) | Line type resource. |
| [`RecordField`](#recordfield) | class |  | One field of a record format. |
| [`RecordFormat`](#recordformat) | class | [`TypedResource`](#typedresource) | Record format. |
| [`Texture`](#texture) | class | [`TypedResource`](#typedresource) | Texture (`ObjectType.Texture`): color, reflectivity, transparency and bump of a rendered surface. |
| [`Texture.Part`](#texturepart) | IntEnum (nested) |  | Part of an object a texture is applied to. |
| [`RenderStyle`](#renderstyle) | class | [`TypedResource`](#typedresource) | Render style (`ObjectType.RenderStyle`): a saved configuration of the rendering settings, applied to a viewport or to a layer. |
| [`RenderBackground`](#renderbackground) | class | [`TypedResource`](#typedresource) | Renderworks background (`ObjectType.RenderBackground`): what a rendering shows behind the model. |
| [`RenderBackground.Kind`](#renderbackgroundkind) | IntEnum (nested) |  | Kind of background a new resource is created with. |
| [`TextStyle`](#textstyle) | class | [`TypedResource`](#typedresource) | Text style (`ObjectType.TextStyle`): font, size and text attributes applied to text objects and dimensions. |
| [`WallStyle`](#wallstyle) | class | [`TypedResource`](#typedresource) | Wall style (`ObjectType.WallStyle`): the components, thickness and attributes of a wall. |
| [`SlabStyle`](#slabstyle) | class | [`TypedResource`](#typedresource) | Slab style (`ObjectType.SlabStyle`): the components and attributes of a slab. |
| [`RoofStyle`](#roofstyle) | class | [`TypedResource`](#typedresource) | Roof style (`ObjectType.RoofStyle`): the components and attributes of a roof. |
| [`ViewportStyle`](#viewportstyle) | class | [`TypedResource`](#typedresource) | Viewport style (`ObjectType.ViewportStyle`): the saved settings of a sheet layer viewport. |
| [`BuildingMaterial`](#buildingmaterial) | class | [`TypedResource`](#typedresource) | Material (building material, `ObjectType.BuildingMaterial`): the physical material of a wall, slab or roof component. |
| [`DataVisualization`](#datavisualization) | class | [`TypedResource`](#typedresource) | Data visualization (`ObjectType.DataVisualization`): a rule that overrides the graphic attributes of the objects matching a criteria, applied to a viewport or... |
| [`ResourceFolderPath`](#resourcefolderpath) | class |  | Folders of a path made by `ResourceFolder.CreatePathFolders`: every folder of the path and the ones the call created, outermost first. |
| [`ResourceFolder`](#resourcefolder) | class | [`TypedResource`](#typedresource) | Resource folder (`ObjectType.Folder`): groups resources of one kind in the Resource Manager. |
| [`SymbolDefinition`](#symboldefinition) | class | [`TypedResource`](#typedresource) | Symbol definition. |
| [`SymbolDefinition.GeometryType`](#symboldefinitiongeometrytype) | IntEnum (nested) |  | What the symbol can draw: 2D only, 3D only, or both (a hybrid symbol shows its 2D part in top/plan). |
| [`SymbolDefinition.InsertMode`](#symboldefinitioninsertmode) | IntEnum (nested) |  | Where the symbol sits relative to the wall it is inserted into. |
| [`SymbolDefinition.BreakMode`](#symboldefinitionbreakmode) | IntEnum (nested) |  | How the wall is cut where the symbol is inserted. |
| [`WorksheetCell`](#worksheetcell) | class |  | A worksheet cell. |
| [`WorksheetCellContent`](#worksheetcellcontent) | class |  | One cell with its content. |
| [`Worksheet`](#worksheet) | class | [`TypedResource`](#typedresource) | Worksheet. |
| [`ResourceType`](#resourcetype) | IntEnum |  | Kind of a resource. |
| [`ContentFolder`](#contentfolder) | IntEnum |  | Standard Vectorworks content folder holding external (library / default) resources. |
| [`ImportConflict`](#importconflict) | IntEnum |  | How a name conflict is resolved when a resource is imported into the current drawing and a resource of the same name already exists there. |
| [`RecordFieldType`](#recordfieldtype) | IntEnum |  | Data type of a record field. |

## Classes

### Resource

> **Full name:** `api.Resource` · **Inherits:** `api.Object`

One resource, identified by its handle. Like every object class of this API it is a lightweight view: copying it does not copy the resource and destroying it does not delete the resource. Constructing it from a handle that is not a resource produces an invalid object (`IsValid()` == `False`); getters then return `None` and setters / operations return `False`. Strings are UTF-8.

**Constructors**

| Constructor | Description |
|---|---|
| `Resource(hResource: Handle)` | Refers to the existing resource `hResource`; check `IsValid()` before use. |

**Methods**

*Type*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | `True` when the handle is a resource of one of the ResourceType kinds. |
| `TypeOf(h: Handle) -> ResourceType` *static* | Resource type of the handle `h`. |
| `GetTypeName(type: ResourceType) -> str` *static* | Stable, lowerCamelCase name of a resource type ("symbolDefinition", "hatch", "texture", ...). Returns an empty string for `ResourceType.Unknown`. |
| `GetTypeFromName(typeName: str) -> ResourceType` *static* | Parses a type name produced by GetTypeName (case insensitive). Returns Unknown when it does not match. |
| `GetAllTypes() -> list[ResourceType]` *static* | Every resource type this API understands, in the order shown above. |

*Lookup*

| Method | Description |
|---|---|
| `FromName(name: str) -> Resource` *static* | Resource of the current drawing with that name; invalid when there is none. |
| `FromIndex(index: int) -> Resource` *static* | Resource with that internal index (hatch / gradient / tile / image / line type / texture indices). |

*Identity*

| Method | Description |
|---|---|
| `GetHandle() -> Handle` | Handle of the resource. |
| `IsValid() -> bool` | True when this object refers to an existing resource. |
| `GetResourceType() -> ResourceType` | Returns the resource type. |
| `GetObjectType() -> ObjectType` | Returns the object type. |
| `GetResourceTypeName() -> str` | Returns the resource type name. |
| `GetName() -> str \| None` | Returns the name. |
| `SetName(name: str) -> bool` | Renames the resource; fails when another object already uses the name. |
| `GetDescription() -> str \| None` | Returns the description. |
| `SetDescription(description: str) -> bool` | Sets the description. |
| `GetInternalIndex() -> int \| None` | Returns the internal index. |
| `GetUuid() -> str \| None` | Persistent UUID of the resource, stable across sessions. |

*Resource folder*

| Method | Description |
|---|---|
| `GetFolder() -> Handle` | Folder resource containing this resource, null when it sits at the top level of the Resource Manager. |
| `GetFolderName() -> str \| None` | Returns the folder name. |
| `MoveToFolder(hFolder: Handle) -> bool` | Moves the resource into `hFolder` (a `ResourceType.Folder` resource). |

*Contents*

| Method | Description |
|---|---|
| `IsContainer() -> bool` | `True` for resources that contain other objects: symbol definitions and resource folders. |
| `GetContents() -> list[Handle]` | Objects inside the resource (the geometry of a symbol definition, the resources of a folder). |
| `GetContentCount() -> int` | Number of content items. |
| `ForEachContent(callback: callable(Handle)) -> None` | Calls `callback` with every object inside the resource. Objects inside the resource (the geometry of a symbol definition, the resources of a folder). |

*Attributes*

| Method | Description |
|---|---|
| `Attributes() -> ObjectAttributes` | Graphical attributes, for the resource kinds that carry them. |

*Lifetime*

| Method | Description |
|---|---|
| `Duplicate() -> Resource` | Copy of the resource in the same document and folder; invalid on failure. |
| `Delete(useUndo: bool = True) -> bool` | Deletes the resource from the document; the object becomes invalid. Objects using it lose the resource. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True when the object is valid (same as `IsValid()`). |
| `==` | `__eq__(o: Resource) -> bool` | `a == b`: True when both objects refer to the same resource. |
| `!=` | `__ne__(o: Resource) -> bool` | `a != b`: True when the objects refer to different resources. |

### ResourceList

> **Full name:** `api.ResourceList` · **Inherits:** `api.Object`

A list of resources of one kind, coming from the current drawing or from external content. It cannot be copied: it holds a Vectorworks resource list and releases it when the Python object is deleted.

**Constructors**

| Constructor | Description |
|---|---|
| `ResourceList()` | Empty, invalid list; fill it with one of the `Build...` methods. |
| `ResourceList(type: ResourceType)` | Empty list of that type. |

**Methods**

*Building*

| Method | Description |
|---|---|
| `BuildFromDocument(type: ResourceType, sort: bool = True) -> bool` | Resources of `type` defined in the current drawing. |
| `BuildFromFolder(type: ResourceType, folder: ContentFolder, subFolder: str = '', includeDocument: bool = False, sort: bool = True) -> bool` | Resources of `type` in a standard Vectorworks content folder (the external / default content). `subFolder` restricts the search to a subfolder (or partial path) of it, empty means the whole folder. With `includeDocument` the resources of the current drawing are listed as well. |
| `BuildFromFolderIndex(type: ResourceType, folderIndex: int, subFolder: str = '', sort: bool = True) -> bool` | Same, for a folder specifier that ContentFolder does not name. A positive `folderIndex` also lists the resources of the current drawing, a negative one lists the folder only, 0 lists the drawing only. |
| `BuildFromFile(type: ResourceType, filePath: str) -> bool` | Resources of `type` inside one Vectorworks file, given by its full native path. |
| `BuildFromOpenDocument(type: ResourceType, openDocumentIndex: int, sort: bool = True) -> bool` | Resources of `type` of another currently open document (see the Vectorworks open files list). |
| `FromDocument(type: ResourceType, sort: bool = True) -> ResourceList` *static* | Factory equivalents of the Build... methods. |
| `FromFolder(type: ResourceType, folder: ContentFolder, subFolder: str = '', includeDocument: bool = False, sort: bool = True) -> ResourceList` *static* | New list of the resources of `type` in the content folder `folder`. Factory equivalents of the Build... methods. |
| `FromFolderIndex(type: ResourceType, folderIndex: int, subFolder: str = '', sort: bool = True) -> ResourceList` *static* | New list of the resources of `type` in the content folder with the index `folderIndex`. Factory equivalents of the Build... methods. |
| `FromFile(type: ResourceType, filePath: str) -> ResourceList` *static* | New list of the resources of `type` in the Vectorworks file `filePath`. Factory equivalents of the Build... methods. |
| `FromOpenDocument(type: ResourceType, openDocumentIndex: int, sort: bool = True) -> ResourceList` *static* | New list of the resources of `type` in another open document. Factory equivalents of the Build... methods. |
| `Dispose() -> None` | Releases the Vectorworks resource list. Called automatically when the Python object is deleted. |

*Identity*

| Method | Description |
|---|---|
| `IsValid() -> bool` | True when this object refers to an existing resource list. |
| `GetListID() -> int` | Raw Vectorworks resource list id, for the low level calls that still need it. |
| `GetResourceType() -> ResourceType` | Returns the resource type. |

*Content folders*

| Method | Description |
|---|---|
| `GetContentFolderName(folder: ContentFolder) -> str` *static* | Stable, lowerCamelCase name of a content folder ("hatches", "textures", "objectStyles", ...). |
| `GetContentFolderFromName(folderName: str) -> ContentFolder` *static* | Parses a name produced by GetContentFolderName (case insensitive); `None` when it does not match. |
| `GetAllContentFolders() -> list[ContentFolder]` *static* | Returns all content folders. |

*Entries*

| Method | Description |
|---|---|
| `GetCount() -> int` | Returns the count. |
| `IsEmpty() -> bool` | True when the list has no entries. |
| `GetResource(index: int) -> Resource` | Resource at `index`; invalid while the entry is external content that was not imported yet. |
| `GetName(index: int) -> str \| None` | Name as shown in the Resource Manager (for external content it can carry the source file name). |
| `GetActualName(index: int) -> str \| None` | Real name of the resource, the one it gets when it is imported. |
| `GetFolderName(index: int) -> str \| None` | Name of the resource folder the entry belongs to, empty at the top level. |
| `IsInDocument(index: int) -> bool` | Whether the resource already exists in the current drawing. |
| `GetEntry(index: int) -> ResourceList.Entry \| None` | Returns the entry at `index`. |
| `GetEntries() -> list[ResourceList.Entry]` | Returns the entries. |
| `ForEach(callback: callable(ResourceList.Entry)) -> None` | Calls `callback` with every entry of the list. |
| `Find(name: str) -> int` | Index of the entry whose actual name - or, failing that, whose displayed name - is `name`. Returns `kNotFound` when there is no match. |
| `Contains(name: str) -> bool` | True when an entry has the actual or displayed name `name`. |

*Importing*

| Method | Description |
|---|---|
| `Import(index: int, onConflict: ImportConflict = ImportConflict.Rename) -> Resource` | Copies the resource into the current drawing and returns it. Already imported resources are returned as they are. The call changes the document, so it must run inside an undo event. Vectorworks registers the resources it imports with Undo itself: do not register them again with `Document.AddAfterSwapObject`. |
| `Import(name: str, onConflict: ImportConflict = ImportConflict.Rename) -> Resource` | Copies the resource into the current drawing and returns it. Already imported resources are returned as they are. The call changes the document, so it must run inside an undo event. Vectorworks registers the resources it imports with Undo itself: do not register them again with `Document.AddAfterSwapObject`. |
| `ImportWithResult(index: int, onConflict: ImportConflict = ImportConflict.Rename) -> ResourceList.ImportResult` | Import that also tells whether the resource was copied into the drawing or the one already there was returned. The same rules as Import apply. |
| `SetClassRenamePrefix(prefix: str) -> None` | Prefix added to the names of the classes that come with an imported resource. Empty by default. |
| `GetClassRenamePrefix() -> str` | Returns the class rename prefix. Prefix added to the names of the classes that come with an imported resource. Empty by default. |

*Editing the list*

| Method | Description |
|---|---|
| `Add(hResource: Handle) -> int` | Adds a resource of the current drawing to the list; returns its index or `kNotFound`. |
| `Remove(index: int) -> bool` | Removes the entry from the list. The resource itself is not deleted. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True when the object is valid (same as `IsValid()`). |

**Constants**

| Constant | Type | Value | Description |
|---|---|---|---|
| `ResourceList.kNotFound` | `int` | `2**64 - 1` | Value returned by Find when no entry matches. |

#### ResourceList.Entry

> **Full name:** `api.ResourceList.Entry` · **Inherits:** `api.Object`

One entry of the list.

**Constructors**

| Constructor | Description |
|---|---|
| `Entry()` | Default value (fields at their defaults). |
| `Entry(index, name, actualName, folderName, handle, isInDocument)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `index` | `int` | 0-based index in this list. |
| `name` | `str` | Name as shown in the Resource Manager. |
| `actualName` | `str` | Real resource name (without the disambiguating file name). |
| `folderName` | `str` | Parent folder of the resource, empty at the top level. |
| `handle` | `Handle` | Null while the resource is not in the current drawing. |
| `isInDocument` | `bool` | `False` for external content that still has to be imported. |

#### ResourceList.ImportResult

> **Full name:** `api.ResourceList.ImportResult` · **Inherits:** `api.Object`

Outcome of ImportWithResult.

**Constructors**

| Constructor | Description |
|---|---|
| `ImportResult()` | Default value (fields at their defaults). |
| `ImportResult(handle, isImported)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `handle` | `Handle` | The resource in the current drawing; null when the import failed. |
| `isImported` | `bool` | `True` when this call copied the resource into the drawing (renamed. |

### TypedResource

> **Full name:** `api.TypedResource` · **Inherits:** [`Resource`](#resource) → `api.Object`

Resource restricted to one ResourceType. Everything Resource offers - name, description, folder, duplicate, delete - is available on the typed classes as well.

**Constructors**

Not instantiable from Python: instances are returned by other API functions.

**Methods**

| Method | Description |
|---|---|
| `GetExpectedType() -> ResourceType` | Resource type this class is restricted to. |

Inherited: everything from [`Resource`](#resource).

### HatchLevel

> **Full name:** `api.HatchLevel` · **Inherits:** `api.Object`

One line family of a hatch. `startPoint` and `repeatVector` define the first line of the family: the line runs along `repeatVector`, whose length is the repeat length of the dash pattern. The family is repeated as parallel lines at `startPoint` + n * `offsetVector`. `dashFactor` is the fraction of each repeat that is drawn (0 .. 1, 1 = solid line). Distances are in world units when the hatch works in world space, in page units (mm on the drawing) when it uses page units - see `Hatch.GetUsePageUnits`.

**Constructors**

| Constructor | Description |
|---|---|
| `HatchLevel()` | Default value (fields at their defaults). |
| `HatchLevel(startPoint, repeatVector, dashFactor, offsetVector, color, lineWeightMils)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `startPoint` | `Point2D` | Origin of the line family. |
| `repeatVector` | `Point2D` | Direction of the lines and repeat length of the dash pattern along them. |
| `dashFactor` | `float` | Drawn fraction of each repeat, 1 = solid line (Vectorworks expects > 0). |
| `offsetVector` | `Point2D` | Spacing from one parallel line of the family to the next. |
| `color` | `ColorRGB` | Pen color of the lines. |
| `lineWeightMils` | `int` | Pen weight in mils (1/1000 inch). |

### Hatch

> **Full name:** `api.Hatch` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Vector hatch fill (`ObjectType.HatchDefinition`): a set of line families repeated over the filled area.

**Constructors**

| Constructor | Description |
|---|---|
| `Hatch(h: Handle)` | Refers to the existing hatch `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> Hatch` *static* | The hatch resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> Hatch` *static* | The hatch resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str, usePageUnits: bool = False, transparent: bool = True, backgroundColor: ColorRGB = ColorRGB()) -> Hatch` *static* | Creates an empty hatch. A number is appended to `name` when it is already taken. |

*Settings*

| Method | Description |
|---|---|
| `GetUsePageUnits() -> bool \| None` | `True` when the hatch is measured on the printed page instead of in world units. |
| `SetUsePageUnits(value: bool) -> bool` | Turns *Use Page Units* on or off. `True` when the hatch is measured on the printed page instead of in world units. |
| `GetTransparent() -> bool \| None` | `True` when the area behind the hatch lines stays transparent instead of being filled with the background. |
| `SetTransparent(value: bool) -> bool` | Turns *Transparent* on or off. `True` when the area behind the hatch lines stays transparent instead of being filled with the background. |
| `GetRotateInWalls() -> bool \| None` | Whether the hatch follows the rotation of the wall / symbol it is drawn in. |
| `SetRotateInWalls(value: bool) -> bool` | Turns *Rotate In Walls* on or off. Whether the hatch follows the rotation of the wall / symbol it is drawn in. |
| `GetRotateInSymbols() -> bool \| None` | Whether *Rotate In Symbols* is on. |
| `SetRotateInSymbols(value: bool) -> bool` | Turns *Rotate In Symbols* on or off. |

*Levels*

| Method | Description |
|---|---|
| `GetLevelCount() -> int` | Levels (line families) are 0 based. There is no fixed limit on how many a hatch holds. |
| `GetLevel(index: int) -> HatchLevel \| None` | Returns the level at `index`. |
| `GetLevels() -> list[HatchLevel]` | Returns the levels. |
| `SetLevel(index: int, level: HatchLevel) -> bool` | Replaces the level at `index`; appending is allowed at index == `GetLevelCount()`. |
| `AddLevel(level: HatchLevel) -> bool` | Appends the level `level`. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### GradientSegment

> **Full name:** `api.GradientSegment` · **Inherits:** `api.Object`

One color stop of a gradient. `spotPosition` is where the color sits (0 .. 1 across the gradient) and `midpointPosition` is where the blend with the next stop is half done (0 .. 1 between the two stops).

**Constructors**

| Constructor | Description |
|---|---|
| `GradientSegment()` | Default value (fields at their defaults). |
| `GradientSegment(spotPosition, midpointPosition, color, opacity)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `spotPosition` | `float` | Position of the color stop along the gradient (0 .. 1). |
| `midpointPosition` | `float` | Position of the midpoint to the next stop (0 .. 1). |
| `color` | `ColorRGB` | Color of the stop. |
| `opacity` | `int` | 0 = fully transparent, 100 = opaque. |

### Gradient

> **Full name:** `api.Gradient` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Gradient fill (`ObjectType.GradientDefinition`): a blend between two or more color stops.

**Constructors**

| Constructor | Description |
|---|---|
| `Gradient(h: Handle)` | Refers to the existing gradient `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> Gradient` *static* | The gradient resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> Gradient` *static* | The gradient resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str) -> Gradient` *static* | Creates a gradient with the default two stops. A number is appended to a name that is already taken. |
| `GetSegmentCount() -> int` | Stops are 0 based, ordered by spot position, from 0 to `GetSegmentCount()` - 1. |
| `GetSegment(index: int) -> GradientSegment \| None` | Returns the segment at `index`. |
| `GetSegments() -> list[GradientSegment]` | Returns the segments. |
| `SetSegment(index: int, segment: GradientSegment) -> bool` | Changing the spot position may re-sort the stops, so the stop can end up at another index. |
| `InsertSegment(segment: GradientSegment) -> int \| None` | Adds a stop; the gradient keeps its stops sorted, so the 0 based index of the new stop is returned. Returns `None` when the stop was not added. |
| `RemoveSegment(index: int) -> bool` | Removes the color stop at `index`. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### Tile

> **Full name:** `api.Tile` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Tile fill (`ObjectType.TileDefinition`): a group of 2D objects repeated over the filled area on a grid.

**Constructors**

| Constructor | Description |
|---|---|
| `Tile(h: Handle)` | Refers to the existing tile `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> Tile` *static* | The tile resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> Tile` *static* | The tile resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str) -> Tile` *static* | Creates an empty tile. A number is appended to a name that is already taken. |

*Geometry*

| Method | Description |
|---|---|
| `GetGeometryGroup() -> Handle` | Group holding the 2D objects the tile repeats; add geometry to it with AddGeometry. |
| `GetGeometry() -> list[Handle]` | Returns the geometry. |
| `AddGeometry(hObject: Handle) -> bool` | Moves an existing 2D object into the tile. |

*Settings*

| Method | Description |
|---|---|
| `GetOffset() -> Point2D \| None` | Origin of the tile grid and the step from one repetition to the next. |
| `SetOffset(value: Point2D) -> bool` | Sets the offset. Origin of the tile grid and the step from one repetition to the next. |
| `GetRepetition() -> Point2D \| None` | Returns the repetition. |
| `SetRepetition(value: Point2D) -> bool` | Sets the repetition. |
| `GetUsePageUnits() -> bool \| None` | `True` when the tile is measured on the printed page instead of in world units. |
| `SetUsePageUnits(value: bool) -> bool` | Turns *Use Page Units* on or off. `True` when the tile is measured on the printed page instead of in world units. |
| `GetTransparentBackground() -> bool \| None` | Whether *Transparent Background* is on. |
| `SetTransparentBackground(value: bool) -> bool` | Turns *Transparent Background* on or off. |
| `GetBackgroundColor() -> ColorRGB \| None` | Returns the background color. |
| `SetBackgroundColor(color: ColorRGB) -> bool` | Sets the background color. |
| `GetRotateInWalls() -> bool \| None` | Whether *Rotate In Walls* is on. |
| `SetRotateInWalls(value: bool) -> bool` | Turns *Rotate In Walls* on or off. |
| `GetRotateInSymbols() -> bool \| None` | Whether *Rotate In Symbols* is on. |
| `SetRotateInSymbols(value: bool) -> bool` | Turns *Rotate In Symbols* on or off. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### ImageFill

> **Full name:** `api.ImageFill` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Image resource (`ObjectType.ImageDefinition`): a bitmap used as an image fill, as an image prop or as a texture image.

**Constructors**

| Constructor | Description |
|---|---|
| `ImageFill(h: Handle)` | Refers to the existing image fill `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> ImageFill` *static* | The image fill resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> ImageFill` *static* | The image fill resource with the internal index `index`; an invalid object when there is none. |
| `GetWidthPixels() -> int \| None` | Returns the width pixels. |
| `GetHeightPixels() -> int \| None` | Returns the height pixels. |
| `GetCompression() -> ImageFill.Compression \| None` | Returns the compression. |
| `SetCompression(value: ImageFill.Compression) -> bool` | Sets the compression. |
| `CreateFromPngData(pngData: bytes) -> ImageFill` *static* | Creates an image fill resource from PNG file contents (`bytes`). |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

#### ImageFill.Compression

> **Full name:** `api.ImageFill.Compression` · **Kind:** `IntEnum`

Compression the image is stored with.

| Member | Value | Description |
|---|---|---|
| `None_` | `0` |  |
| `Jpeg` | `1` |  |
| `Png` | `2` |  |
| `PngMonochrome` | `3` |  |

### LineType

> **Full name:** `api.LineType` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Line type resource. There are two kinds:

- simple — a dash pattern: alternating line and gap lengths (see GetDashPattern). complex - a group of 2D objects repeated along the line (see GetGeometry).

Objects reference a line type through their pen style; see `PenAttributes.SetLineType`.

**Constructors**

| Constructor | Description |
|---|---|
| `LineType(h: Handle)` | Refers to the existing line type `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> LineType` *static* | The line type resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> LineType` *static* | The line type resource with the internal index `index`; an invalid object when there is none. |
| `CreateSimple(dashPattern: list[float], scaleWithLineWeight: bool = False) -> LineType` *static* | Finds or creates a simple line type with that dash pattern: alternating line and gap lengths, at most 16 entries. `scaleWithLineWeight` makes the pattern scale with the pen weight of the object. Vectorworks reuses an existing matching line type - including one from the default content - instead of creating a duplicate, so the returned resource may carry a different name. |
| `CreateComplex(name: str) -> LineType` *static* | Creates an empty complex line type; add the repeated 2D objects with AddGeometry. |

*Kind*

| Method | Description |
|---|---|
| `IsSimple() -> bool \| None` | True for a simple (dashed) line type. |
| `IsComplex() -> bool \| None` | True for a complex line type (repeated geometry). |

*Simple line type*

| Method | Description |
|---|---|
| `GetDashPattern() -> list[float]` | Alternating line and gap lengths; empty for a complex line type. |
| `GetScaleWithLineWeight() -> bool \| None` | Whether *Scale With Line Weight* is on. |

*Complex line type*

| Method | Description |
|---|---|
| `GetGeometryGroup() -> Handle` | Group holding the 2D objects repeated along the line; null for a simple line type. |
| `GetGeometry() -> list[Handle]` | Returns the geometry. |
| `AddGeometry(hObject: Handle) -> bool` | Moves an existing 2D object into the line type. |
| `GetGapSize() -> float \| None` | Gap between two repetitions of the geometry, in world units (or page units when in page space). |
| `SetGapSize(value: float) -> bool` | Sets the gap size. Gap between two repetitions of the geometry, in world units (or page units when in page space). |
| `GetUsePageUnits() -> bool \| None` | `True` when the line type is measured on the printed page instead of in world units. |
| `SetUsePageUnits(value: bool) -> bool` | Turns *Use Page Units* on or off. `True` when the line type is measured on the printed page instead of in world units. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### RecordField

> **Full name:** `api.RecordField` · **Inherits:** `api.Object`

One field of a record format.

**Constructors**

| Constructor | Description |
|---|---|
| `RecordField()` | Default value (fields at their defaults). |
| `RecordField(name, localizedName, type, defaultValue)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `name` | `str` | Universal (non-localized) name, the one APIs use. |
| `localizedName` | `str` | Name shown in the user interface. |
| `type` | `RecordFieldType` | Field type. |
| `defaultValue` | `str` | Value new records start with, as text. |

### RecordFormat

> **Full name:** `api.RecordFormat` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Record format. Attaching it to an object creates a record - a set of values for these fields - on that object; see Document for reading and writing the values of an attached record.

**Constructors**

| Constructor | Description |
|---|---|
| `RecordFormat(h: Handle)` | Refers to the existing record format `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> RecordFormat` *static* | The record format resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> RecordFormat` *static* | The record format resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str) -> RecordFormat` *static* | Creates an empty record format; returns the existing one when the name is already taken. |
| `IsInternalName(name: str) -> bool` *static* | `True` for names reserved for internal record formats: "NNA_" or "__NNA" prefix, case-insensitive. |
| `GetFieldTypeName(type: RecordFieldType) -> str` *static* | Stable, lowerCamelCase name of a field type ("integer", "text", "popUp", ...). |
| `GetFieldTypeFromName(typeName: str) -> RecordFieldType` *static* | Returns the field type from name for `typeName`. |
| `GetAllFieldTypes() -> list[RecordFieldType]` *static* | Returns all field types. |

*Format settings*

| Method | Description |
|---|---|
| `GetLocalizedName() -> str \| None` | Returns the localized name. |
| `SetLocalizedName(name: str) -> bool` | Sets the localized name. |
| `IsParametric() -> bool \| None` | A parametric format belongs to a plug-in object and must not be edited. |
| `GetVisible() -> bool \| None` | Hidden formats do not show up in the data pane of the Object Info palette. |
| `SetVisible(value: bool) -> bool` | Turns *Visible* on or off. Hidden formats do not show up in the data pane of the Object Info palette. |

*Fields*

| Method | Description |
|---|---|
| `GetFieldCount() -> int` | Number of field items. |
| `GetField(index: int) -> RecordField \| None` | Returns the field at `index`. |
| `GetFields() -> list[RecordField]` | Returns the fields. |
| `FindField(fieldName: str) -> int` | Index of the field named `fieldName`; `kNotFound` when there is none. |
| `HasField(fieldName: str) -> bool` | True when the record format has a field named `fieldName`. |
| `AddField(name: str, type: RecordFieldType, defaultValue: str = '', updateExistingRecords: bool = True) -> int` | Adds a field. `defaultValue` is parsed according to `type` the way a value typed by the user is; an empty string uses the empty value of the type. Text types keep the string; `RecordFieldType.Boolean` takes the string "True" or "False"; `RecordFieldType.Color` takes "red,green,blue" (0 .. 65535 each); `RecordFieldType.Class`, `BuildingMaterial`, `Texture` and `SymbolDefinition` take the name of an existing resource of that kind; `Fill` and `PenStyle` take the name of a hatch, tile, gradient, image or line type resource. `updateExistingRecords` adds the field to the records already attached to objects, with `defaultValue` as their value. Returns the index of the new field, or `kNotFound` when `defaultValue` is not valid for `type`, the type cannot be added (`Radio`, `ControlPoint`, `LayerPopUp` and the plug-in only types) or the field is not created. |
| `RemoveField(fieldName: str) -> bool` | Removes the field named `fieldName`. |
| `RenameField(index: int, name: str) -> bool` | Renames the field at `index` to `name`. |
| `GetFieldDefaultValue(fieldName: str) -> str \| None` | Default value of a field, as text. |
| `SetFieldDefaultValue(fieldName: str, value: str) -> bool` | Sets the field default value. Default value of a field, as text. |

*Pop-up choices*

| Method | Description |
|---|---|
| `GetFieldChoices(fieldName: str) -> list[str]` | Choices offered by a PopUp field, in order. |
| `SetFieldChoices(fieldName: str, choices: list[str]) -> bool` | Replaces the choices of a PopUp field. |

**Constants**

| Constant | Type | Value | Description |
|---|---|---|---|
| `RecordFormat.kNotFound` | `int` | `2**64 - 1` | Index of the field with that universal name; `kNotFound` when there is none. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### Texture

> **Full name:** `api.Texture` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Texture (`ObjectType.Texture`): color, reflectivity, transparency and bump of a rendered surface.

**Constructors**

| Constructor | Description |
|---|---|
| `Texture(h: Handle)` | Refers to the existing texture `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> Texture` *static* | The texture resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> Texture` *static* | The texture resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str) -> Texture` *static* | Creates an empty texture. A number is appended to a name that is already taken. |
| `GetSize() -> float \| None` | Real world size the texture image covers, in world units. |
| `SetSize(value: float) -> bool` | Sets the size. Real world size the texture image covers, in world units. |
| `GetUVAspectRatio() -> float \| None` | Ratio between the U and the V extent of the texture image. |
| `ApplyToObject(hObject: Handle, part: Texture.Part = Texture.Part.Overall) -> bool` | Assigns the texture to an object (or to one of its parts). |
| `UpdateThumbnail() -> bool` | Refreshes the Resource Manager preview after the texture changed. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

#### Texture.Part

> **Full name:** `api.Texture.Part` · **Kind:** `IntEnum`

Part of an object a texture is applied to. Objects that have no parts use Overall.

| Member | Value | Description |
|---|---|---|
| `Overall` | `0` | The whole object. |
| `ExtrudeTop` | `1` |  |
| `ExtrudeBottom` | `2` |  |
| `ExtrudeSides` | `3` | Extrudes and sweeps. |
| `WallLeft` | `4` |  |
| `WallRight` | `5` |  |
| `WallTop` | `6` |  |
| `WallBottom` | `7` | Walls. |
| `SlabTop` | `8` |  |
| `SlabBottom` | `9` |  |
| `SlabSides` | `10` | Slabs. |
| `RoofTop` | `11` |  |
| `RoofBottom` | `12` |  |
| `RoofSides` | `13` | Roofs. |

### RenderStyle

> **Full name:** `api.RenderStyle` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Render style (`ObjectType.RenderStyle`): a saved configuration of the rendering settings, applied to a viewport or to a layer.

**Constructors**

| Constructor | Description |
|---|---|
| `RenderStyle(h: Handle)` | Refers to the existing render style `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> RenderStyle` *static* | The render style resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> RenderStyle` *static* | The render style resource with the internal index `index`; an invalid object when there is none. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### RenderBackground

> **Full name:** `api.RenderBackground` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Renderworks background (`ObjectType.RenderBackground`): what a rendering shows behind the model.

**Constructors**

| Constructor | Description |
|---|---|
| `RenderBackground(h: Handle)` | Refers to the existing Renderworks background `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> RenderBackground` *static* | The Renderworks background resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> RenderBackground` *static* | The Renderworks background resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str, kind: RenderBackground.Kind) -> RenderBackground` *static* | Creates a background of that kind. A number is appended to a name that is already taken. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

#### RenderBackground.Kind

> **Full name:** `api.RenderBackground.Kind` · **Kind:** `IntEnum`

Kind of background a new resource is created with.

| Member | Value | Description |
|---|---|---|
| `Clouds` | `0` |  |
| `OneColor` | `1` |  |
| `TwoColor` | `2` |  |
| `PhysicalSky` | `3` |  |

### TextStyle

> **Full name:** `api.TextStyle` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Text style (`ObjectType.TextStyle`): font, size and text attributes applied to text objects and dimensions.

**Constructors**

| Constructor | Description |
|---|---|
| `TextStyle(h: Handle)` | Refers to the existing text style `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> TextStyle` *static* | The text style resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> TextStyle` *static* | The text style resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str) -> TextStyle` *static* | Creates a text style; returns the existing one when the name is already taken. |
| `ApplyToObject(hObject: Handle) -> bool` | Applies the style to a text object (or to any object that carries text attributes). |
| `OfObject(hObject: Handle) -> TextStyle` *static* | Text style an object follows; invalid when the object uses its own text attributes. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### WallStyle

> **Full name:** `api.WallStyle` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Wall style (`ObjectType.WallStyle`): the components, thickness and attributes of a wall.

**Constructors**

| Constructor | Description |
|---|---|
| `WallStyle(h: Handle)` | Refers to the existing wall style `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> WallStyle` *static* | The wall style resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> WallStyle` *static* | The wall style resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str) -> WallStyle` *static* | Creates a wall style; returns the existing one when the name is already taken. |
| `ApplyToObject(hWall: Handle, selectedOffset: float = 0.0, replacingOffset: float = 0.0) -> bool` | Applies the style to a wall. The two offsets say which line of the old wall and which line of the new style stay in place, measured from the wall centre in world units; 0 keeps the centre line. |
| `OfObject(hWall: Handle) -> WallStyle` *static* | The wall style the wall `hWall` follows (invalid when it has none). |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### SlabStyle

> **Full name:** `api.SlabStyle` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Slab style (`ObjectType.SlabStyle`): the components and attributes of a slab.

**Constructors**

| Constructor | Description |
|---|---|
| `SlabStyle(h: Handle)` | Refers to the existing slab style `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> SlabStyle` *static* | The slab style resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> SlabStyle` *static* | The slab style resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str) -> SlabStyle` *static* | Creates a slab style; returns the existing one when the name is already taken. |
| `ApplyToObject(hSlab: Handle) -> bool` | Applies this slab style to the slab `hSlab`. |
| `OfObject(hSlab: Handle) -> SlabStyle` *static* | The slab style the slab `hSlab` follows (invalid when it has none). |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### RoofStyle

> **Full name:** `api.RoofStyle` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Roof style (`ObjectType.RoofStyle`): the components and attributes of a roof.

**Constructors**

| Constructor | Description |
|---|---|
| `RoofStyle(h: Handle)` | Refers to the existing roof style `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> RoofStyle` *static* | The roof style resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> RoofStyle` *static* | The roof style resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str) -> RoofStyle` *static* | Creates a roof style; returns the existing one when the name is already taken. |
| `ApplyToObject(hRoof: Handle) -> bool` | Applies this roof style to the roof `hRoof`. |
| `OfObject(hRoof: Handle) -> RoofStyle` *static* | The roof style the roof `hRoof` follows (invalid when it has none). |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### ViewportStyle

> **Full name:** `api.ViewportStyle` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Viewport style (`ObjectType.ViewportStyle`): the saved settings of a sheet layer viewport.

**Constructors**

| Constructor | Description |
|---|---|
| `ViewportStyle(h: Handle)` | Refers to the existing viewport style `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> ViewportStyle` *static* | The viewport style resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> ViewportStyle` *static* | The viewport style resource with the internal index `index`; an invalid object when there is none. |
| `ApplyToObject(hViewport: Handle) -> bool` | Applies this viewport style to the viewport `hViewport`. |
| `OfObject(hViewport: Handle) -> ViewportStyle` *static* | The viewport style the viewport `hViewport` follows (invalid when it has none). |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### BuildingMaterial

> **Full name:** `api.BuildingMaterial` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Material (building material, `ObjectType.BuildingMaterial`): the physical material of a wall, slab or roof component. It carries the attributes and the data (fire rating, thermal values, ...) of that material.

**Constructors**

| Constructor | Description |
|---|---|
| `BuildingMaterial(h: Handle)` | Refers to the existing material `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> BuildingMaterial` *static* | The material resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> BuildingMaterial` *static* | The material resource with the internal index `index`; an invalid object when there is none. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### DataVisualization

> **Full name:** `api.DataVisualization` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Data visualization (`ObjectType.DataVisualization`): a rule that overrides the graphic attributes of the objects matching a criteria, applied to a viewport or to the design layers. Vectorworks identifies data visualizations by name, so this class works with names.

**Constructors**

| Constructor | Description |
|---|---|
| `DataVisualization(h: Handle)` | Refers to the existing data visualization `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> DataVisualization` *static* | The data visualization resource named `name`; an invalid object when there is none. |
| `GetAllNames() -> list[str]` *static* | Names of every data visualization of the current document. |
| `Rename(oldName: str, newName: str) -> bool` *static* | Renames the data visualization `oldName` to `newName`. |
| `DeleteByName(name: str) -> bool` *static* | Deletes the data visualization named `name`. |
| `GetActiveOn(hObject: Handle) -> list[str]` *static* | Names of the data visualizations active on an object (a viewport, a saved view or a layer). |
| `Activate(hObject: Handle, name: str, activate: bool) -> bool` *static* | Turns a data visualization on or off for that object. |
| `SetObjectExcluded(hObject: Handle, exclude: bool) -> bool` *static* | Keeps an object out of every data visualization. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### ResourceFolderPath

> **Full name:** `api.ResourceFolderPath` · **Inherits:** `api.Object`

Folders of a path made by `ResourceFolder.CreatePathFolders`.

**Constructors**

| Constructor | Description |
|---|---|
| `ResourceFolderPath()` | Default value (fields at their defaults). |
| `ResourceFolderPath(folders, createdFolders)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `folders` | `list[Handle]` | Every folder of the path, outermost first; empty on failure. |
| `createdFolders` | `list[Handle]` | The folders this call created, outermost first. |

### ResourceFolder

> **Full name:** `api.ResourceFolder` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Resource folder (`ObjectType.Folder`): groups resources of one kind in the Resource Manager.

**Constructors**

| Constructor | Description |
|---|---|
| `ResourceFolder(h: Handle)` | Refers to the existing resource folder `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> ResourceFolder` *static* | The resource folder resource named `name`; an invalid object when there is none. |
| `Create(name: str, forType: ResourceType) -> ResourceFolder` *static* | Creates a top level folder for resources of that kind. Fails (invalid folder) when the name is already taken; resource names are unique in a document. Undo is not registered: register the new folder with `Document.AddAfterSwapObject`. |
| `CreatePath(folderPath: str, forType: ResourceType) -> ResourceFolder` *static* | Creates a chain of nested folders from a path such as "Doors/Interior"; returns the innermost folder. See CreatePathFolders for the rules. |
| `CreatePathFolders(folderPath: str, forType: ResourceType) -> ResourceFolderPath` *static* | Creates a chain of nested folders from a path such as "Doors/Interior" and returns all of them. A folder of the path that already exists for `forType` at exactly that place is reused. Fails (empty result) when a name of the path is taken by anything else, including a folder elsewhere or for another kind; the folders created so far are removed again then. Empty names ("A//B", a leading or a trailing '/') are skipped. Undo is not registered: register only the first of `createdFolders` (the outermost new folder) with `Document.AddAfterSwapObject`. It holds the other new folders, and registering a folder marks its contents as inserted too, so registering a deeper new folder as well would insert it twice. Never register the reused ones. |
| `GetContentType() -> ResourceType \| None` | Kind of resource the folder holds. |
| `GetResources() -> list[Handle]` | Resources inside the folder. |
| `Add(hResource: Handle) -> bool` | Moves a resource into this folder. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

### SymbolDefinition

> **Full name:** `api.SymbolDefinition` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Symbol definition. Its contents are the objects the symbol draws; every instance in the drawing shows the same contents, so editing them updates every instance at once. A plant style, a title block border style and other plug-in styles are symbol definitions as well - they hold one plug-in object as their only content (see `PlantObject.EnsurePlantStyle`).

**Constructors**

| Constructor | Description |
|---|---|
| `SymbolDefinition(h: Handle)` | Refers to the existing symbol definition `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> SymbolDefinition` *static* | The symbol definition resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> SymbolDefinition` *static* | The symbol definition resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str) -> SymbolDefinition` *static* | Creates an empty symbol definition. A number is appended to a name that is already taken, so read the name back with `GetName()`. |
| `GetActive() -> SymbolDefinition` *static* | Symbol definition new symbol instances are created from. |
| `SetActive() -> bool` | Sets the active. Symbol definition new symbol instances are created from. |

*Kind*

| Method | Description |
|---|---|
| `GetGeometryType() -> SymbolDefinition.GeometryType \| None` | Returns the geometry type. |
| `CanInsertIntoWalls() -> bool \| None` | `True` when the symbol may be inserted into a wall (it has a wall insertion point). |
| `ContainsLight() -> bool \| None` | True when the symbol definition contains a light. |

*Insertion behaviour*

| Method | Description |
|---|---|
| `GetInsertMode() -> SymbolDefinition.InsertMode \| None` | Returns the insert mode. |
| `SetInsertMode(value: SymbolDefinition.InsertMode) -> bool` | Sets the insert mode. |
| `GetBreakMode() -> SymbolDefinition.BreakMode \| None` | Returns the break mode. |
| `SetBreakMode(value: SymbolDefinition.BreakMode) -> bool` | Sets the break mode. |
| `GetPageBased() -> bool \| None` | Page based symbols keep their size on the printed page instead of in world units. |
| `SetPageBased(value: bool) -> bool` | Turns *Page Based* on or off. Page based symbols keep their size on the printed page instead of in world units. |
| `GetInsertAsGroup() -> bool \| None` | `True` when inserting the symbol drops a copy of its contents instead of a symbol instance. |
| `SetInsertAsGroup(value: bool) -> bool` | Turns *Insert As Group* on or off. `True` when inserting the symbol drops a copy of its contents instead of a symbol instance. |

*Contents*

| Method | Description |
|---|---|
| `GetGeometry() -> list[Handle]` | The objects the symbol draws (same as `Resource.GetContents`). |
| `AddGeometry(hObject: Handle) -> bool` | Moves an existing object into the symbol definition. |
| `ResetInstances() -> bool` | Redraws every instance after the contents changed. |

*Instances*

| Method | Description |
|---|---|
| `Insert(position: Point2D, rotationRadians: float = 0.0) -> Handle` | Creates a symbol instance at `position` in the active layer / current container; null on failure. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

#### SymbolDefinition.GeometryType

> **Full name:** `api.SymbolDefinition.GeometryType` · **Kind:** `IntEnum`

What the symbol can draw: 2D only, 3D only, or both (a hybrid symbol shows its 2D part in top/plan).

| Member | Value | Description |
|---|---|---|
| `Unknown` | `0` |  |
| `TwoD` | `1` |  |
| `ThreeD` | `2` |  |
| `Hybrid` | `3` |  |

#### SymbolDefinition.InsertMode

> **Full name:** `api.SymbolDefinition.InsertMode` · **Kind:** `IntEnum`

Where the symbol sits relative to the wall it is inserted into.

| Member | Value | Description |
|---|---|---|
| `Edge` | `0` |  |
| `Center` | `1` |  |
| `LeftEdge` | `2` |  |
| `RightEdge` | `3` |  |
| `CoreComponentCenter` | `4` |  |
| `CoreComponentLeftEdge` | `5` |  |
| `CoreComponentRightEdge` | `6` |  |
| `WallInsertLocation` | `7` |  |
| `WallClosureInsertLocation` | `8` |  |

#### SymbolDefinition.BreakMode

> **Full name:** `api.SymbolDefinition.BreakMode` · **Kind:** `IntEnum`

How the wall is cut where the symbol is inserted.

| Member | Value | Description |
|---|---|---|
| `FullWithCaps` | `0` |  |
| `FullNoCaps` | `1` |  |
| `Half` | `2` |  |
| `None_` | `3` |  |

### WorksheetCell

> **Full name:** `api.WorksheetCell` · **Inherits:** `api.Object`

A worksheet cell. Rows and columns are 1 based, like the row numbers and the column letters shown to the user; column 1 is "A".

**Constructors**

| Constructor | Description |
|---|---|
| `WorksheetCell()` | Default value (fields at their defaults). |
| `WorksheetCell(row, column)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `row` | `int` | Row (1-based). |
| `column` | `int` | Column (1-based). |

### WorksheetCellContent

> **Full name:** `api.WorksheetCellContent` · **Inherits:** `api.Object`

One cell with its content.

**Constructors**

| Constructor | Description |
|---|---|
| `WorksheetCellContent()` | Default value (fields at their defaults). |
| `WorksheetCellContent(cell, formula, text)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `cell` | `WorksheetCell` | The cell. |
| `formula` | `str` | What the cell was given; empty for a cell that holds a literal. |
| `text` | `str` | What the cell shows after the last recalculation. |

### Worksheet

> **Full name:** `api.Worksheet` · **Inherits:** [`TypedResource`](#typedresource) → [`Resource`](#resource) → `api.Object`

Worksheet. A worksheet is a resource, and it may also be placed on a layer as a worksheet image.

**Constructors**

| Constructor | Description |
|---|---|
| `Worksheet(h: Handle)` | Refers to the existing worksheet `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> Worksheet` *static* | The worksheet resource named `name`; an invalid object when there is none. |
| `FromIndex(index: int) -> Worksheet` *static* | The worksheet resource with the internal index `index`; an invalid object when there is none. |
| `Create(name: str, rows: int = 20, columns: int = 10) -> Worksheet` *static* | Creates an empty worksheet; returns the existing one when the name is already taken. |

*Size*

| Method | Description |
|---|---|
| `GetRowCount() -> int \| None` | Number of row items. |
| `GetColumnCount() -> int \| None` | Number of column items. |
| `IsValidCell(cell: WorksheetCell) -> bool` | True when the cell `cell` exists in the worksheet. |

*Cells*

| Method | Description |
|---|---|
| `GetCellFormula(cell: WorksheetCell) -> str \| None` | Formula of a cell; a cell holding a literal value returns an empty string. |
| `SetCellFormula(cell: WorksheetCell, formula: str) -> bool` | Assigns a formula (for example "=COUNT(ALL)") or a literal to one cell, or to every cell of a range. |
| `SetRangeFormula(topLeft: WorksheetCell, bottomRight: WorksheetCell, formula: str) -> bool` | Sets the range formula. |
| `GetCellText(cell: WorksheetCell) -> str \| None` | Text the cell currently shows. Call Recalculate first when the drawing changed. |
| `GetCellValue(cell: WorksheetCell) -> float \| None` | Numeric value of a cell; empty when the cell does not hold a number. |
| `GetCells(topLeft: WorksheetCell, bottomRight: WorksheetCell) -> list[WorksheetCellContent]` | Reads a rectangular block of cells, row by row. Cells with neither a formula nor text are skipped. |
| `ClearCells(topLeft: WorksheetCell, bottomRight: WorksheetCell) -> bool` | Clears the cells of the block from `topLeft` to `bottomRight`. |

*Structure*

| Method | Description |
|---|---|
| `InsertRows(beforeRow: int, count: int = 1) -> bool` | Inserts `count` rows before the row `beforeRow`. |
| `InsertColumns(beforeColumn: int, count: int = 1) -> bool` | Inserts `count` columns before the column `beforeColumn`. |
| `DeleteRows(startRow: int, count: int = 1) -> bool` | Deletes `count` rows starting at the row `startRow`. |
| `DeleteColumns(startColumn: int, count: int = 1) -> bool` | Deletes `count` columns starting at the column `startColumn`. |
| `Recalculate() -> bool` | Reevaluates every formula. Do this after the drawing changed and before reading cell text. |
| `CreateImage(topLeftCorner: Point2D) -> Handle` | Places the worksheet on the active layer so that it can be seen in the drawing; returns the image object. |

Inherited: everything from [`TypedResource`](#typedresource), [`Resource`](#resource).

## Enumerations

### ResourceType

> **Full name:** `api.ResourceType` · **Kind:** `IntEnum`

Kind of a resource. The values are the object types (the same values as the matching ObjectType constants), so a resource type can be passed to any API that expects an object type.

| Member | Value | Description |
|---|---|---|
| `Unknown` | `0` | The object is not a resource. |
| `SymbolDefinition` | `16` | Reusable object template; placed in the drawing as symbol instances. |
| `Worksheet` | `18` | Spreadsheet / report. |
| `BuildingMaterial` | `19` | Material of a wall, slab or roof component. |
| `ViewportStyle` | `36` |  |
| `DataVisualization` | `37` | Rule based graphic override of a viewport / layer. |
| `RecordFormat` | `47` | Data record definition (the format attached to objects). |
| `Hatch` | `66` | Vector hatch fill. |
| `Folder` | `92` | Resource folder grouping other resources in the Resource Manager. |
| `Class` | `94` | Class definition (see ClassAttributes for its attributes). |
| `LineType` | `96` | Simple or complex line type (dashed / patterned pen). |
| `Texture` | `97` | Texture. |
| `RoofStyle` | `102` |  |
| `RenderStyle` | `106` | Render style. |
| `SlabStyle` | `107` |  |
| `Tile` | `108` | Tile fill. |
| `TextStyle` | `109` |  |
| `RenderBackground` | `115` | Renderworks background. |
| `ImageFill` | `119` | Image definition used as an image fill / image prop. |
| `Gradient` | `120` | Gradient fill. |
| `WallStyle` | `127` |  |

### ContentFolder

> **Full name:** `api.ContentFolder` · **Kind:** `IntEnum`

Standard Vectorworks content folder holding external (library / default) resources. The values are the Vectorworks folder specifiers; pass any other one through BuildFromFolderIndex.

| Member | Value | Description |
|---|---|---|
| `None_` | `0` | No library folder: the current drawing only. |
| `ObjectLibraries` | `11` |  |
| `Libraries` | `13` |  |
| `Defaults` | `14` |  |
| `Textures` | `100` |  |
| `Gradients` | `103` |  |
| `Hatches` | `105` |  |
| `ImageFills` | `106` |  |
| `PlantStyles` | `107` |  |
| `RenderBackgrounds` | `109` |  |
| `TitleBlocks` | `115` |  |
| `Reports` | `120` |  |
| `SketchStyles` | `134` |  |
| `Tiles` | `163` |  |
| `TextStyles` | `164` |  |
| `RenderStyles` | `171` |  |
| `LineTypes` | `174` |  |
| `RecordFormats` | `197` |  |
| `ObjectStyles` | `217` |  |
| `Materials` | `345` |  |
| `WallStyles` | `393` |  |
| `RoofStyles` | `394` |  |
| `SlabStyles` | `395` |  |
| `PlantLibraries` | `399` |  |

### ImportConflict

> **Full name:** `api.ImportConflict` · **Kind:** `IntEnum`

How a name conflict is resolved when a resource is imported into the current drawing and a resource of the same name already exists there.

| Member | Value | Description |
|---|---|---|
| `DoNotImport` | `0` | Keep the existing resource, import nothing. |
| `Replace` | `1` | Overwrite the existing resource. |
| `Rename` | `2` | Import under a new, unique name. |
| `AskWithUI` | `3` | Show the standard Vectorworks conflict dialog (interactive sessions only). |

### RecordFieldType

> **Full name:** `api.RecordFieldType` · **Kind:** `IntEnum`

Data type of a record field.

| Member | Value | Description |
|---|---|---|
| `Unknown` | `0` |  |
| `Integer` | `1` |  |
| `Boolean` | `2` |  |
| `Real` | `3` |  |
| `Text` | `4` |  |
| `Dimension` | `7` | A length, shown in the document units. |
| `PopUp` | `8` | Text with a list of predefined choices. |
| `Radio` | `9` |  |
| `CoordLocX` | `10` | Plug-in parameter only. |
| `CoordLocY` | `11` | Plug-in parameter only. |
| `StaticText` | `14` | Label, not editable on the object. |
| `ControlPoint` | `15` |  |
| `DimStdPopUp` | `16` | Plug-in parameter only. |
| `PrecisionPopUp` | `17` | Plug-in parameter only. |
| `ClassPopUp` | `18` |  |
| `LayerPopUp` | `19` |  |
| `Angle` | `20` |  |
| `Area` | `21` |  |
| `Volume` | `22` |  |
| `Class` | `23` | Internal index of a class. |
| `BuildingMaterial` | `24` | Internal index of a material. |
| `Fill` | `25` |  |
| `PenStyle` | `26` |  |
| `PenWeight` | `27` |  |
| `Color` | `28` |  |
| `Texture` | `29` | Internal index of a texture. |
| `SymbolDefinition` | `30` | Internal index of a symbol definition. |

---

[Back to the index](README.md) · [Back to top](#resources--resources-resource-lists-and-typed-resources)
