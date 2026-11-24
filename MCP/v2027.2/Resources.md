**English** • [Deutsch](../../MCP.de/v2027.2/Resources.md) • [日本語](../../MCP.ja/v2027.2/Resources.md)

# Resources — resources and worksheets

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools for the resources of the drawing and of external content (libraries, files, other documents), and for worksheets.

## Table of contents

- [Overview](#overview)
- [Resources](#resources)
  - [getResourceTypes](#getresourcetypes)
  - [getResources](#getresources)
  - [getResource](#getresource)
  - [importResource](#importresource)
  - [editResource](#editresource)
  - [createResource](#createresource)
  - [getResourceDetails](#getresourcedetails)
  - [setResourceDetails](#setresourcedetails)
  - [applyResource](#applyresource)
  - [getWorksheet](#getworksheet)
  - [editWorksheet](#editworksheet)

## Overview

This folder holds 1 tool group with 11 tools in total.

| Group | Group ID | Active by default | Risk level | Tools | Summary |
|---|---|---|---|---|---|
| [Resources](#resources) | `resources` | No | medium | 11 | List, import, create, inspect, edit and apply resources; read and edit worksheets. |

## Resources

> **Group:** `Resources` · **Group ID:** `resources` · **Active by default:** No · **Risk level:** medium · **Tools:** 11

**List, import, create, inspect, edit and apply resources; read and edit worksheets.**

List, inspect, import and edit Vectorworks resources: symbol definitions, hatches, gradients, image fills, tiles, line types, textures, render styles and backgrounds, record formats, worksheets, text styles, wall/slab/roof/viewport styles, data visualizations, building materials, classes and resource folders. Resources are listed from the current drawing or from external content (the Vectorworks libraries, a file on disk, another open document) and imported into the drawing.

Note that plant styles, title block border styles and data tag styles are not resource types of their own: each is a `symbolDefinition` kept in a content folder (plantStyles / plantLibraries, titleBlocks, objectStyles), so list and import them with resourceType `symbolDefinition` plus the matching `folder`. The getResources schema already lists every `resourceType` and `folder` name; call getResourceTypes only to see the node type of each resource type.

IFC property sets, standard or custom, are handled by the IFC group (listIFCPsets, getIFCPsetDefinition), not through record formats. IFC Data Manager mappings and IFC export settings are not exposed by the Resources or IFC tools; getObjectIFCData only reports an object's mapped IFC entity and which of its IFC values come from a mapping. Worksheets are read and edited in full with getWorksheet and editWorksheet: cell formats, borders, merged cells, column widths, row heights, database rows and their subrows, recalculation.

Each change runs as its own named, undoable Vectorworks operation.

> **Note:** The `resourceType` of getResources, importResource and createResource is matched without regard to case, against the names that getResourceTypes lists and these aliases: `plantStyle`, `plant`, `titleBlockStyle`, `titleBlock`, `dataTagStyle`, `dataTag`, `symbol` and `objectStyle` (all mean `symbolDefinition`), `record` and `format` (`recordFormat`), `material` (`buildingMaterial`), `image` (`imageFill`), `font` (`textStyle`) and `background` (`renderBackground`). One trailing `s` is ignored (`textures` is `texture`); `hatches` is not accepted, use `hatch`. An unknown name fails, and the message lists the valid names.

| Tool | Effect | Risk | Summary |
|---|---|---|---|
| [`getResourceTypes`](#getresourcetypes) | Read-only | low | Lists the resource types and the standard content folders. |
| [`getResources`](#getresources) | Read-only | low | Lists the resources of one type from the drawing, a library, a file or another document. |
| [`getResource`](#getresource) | Read-only | low | Reads one resource of the drawing. |
| [`importResource`](#importresource) | Edit | medium | Imports an external resource into the drawing. |
| [`editResource`](#editresource) | Edit | medium | Renames, describes, moves, duplicates or deletes a resource. |
| [`createResource`](#createresource) | Edit | medium | Creates an empty resource. |
| [`getResourceDetails`](#getresourcedetails) | Read-only | low | Reads what a resource holds: hatch levels, gradient stops, line type dashes and more. |
| [`setResourceDetails`](#setresourcedetails) | Edit | medium | Changes what a resource holds. |
| [`applyResource`](#applyresource) | Edit | medium | Applies a texture, style or data visualization to an object. |
| [`getWorksheet`](#getworksheet) | Read-only | low | Reads a worksheet: its size, cells, formats and database rows. |
| [`editWorksheet`](#editworksheet) | Edit | medium | Changes a worksheet with a list of actions. |

### getResourceTypes

Lists the resource types and the standard content folders.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the resource types this API understands (`resourceType` values with their node type) and the names of the standard Vectorworks content folders (`folder` values). Takes no arguments.

**Parameters**

This tool takes no parameters.

**Result**

| Key | Description |
|---|---|
| `resourceTypes` | The resource types, each as `{ name, type }`: `name` is the value for a `resourceType` argument and `type` the node type number. |
| `contentFolders` | The names of the standard content folders: the values for the `folder` argument of [getResources](#getresources). |

### getResources

Lists the resources of one type from the drawing, a library, a file or another document.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the resources of one `resourceType`. `source` selects where they come from: "document" (the current drawing, default), "library" (a standard content folder given by `folder`, optionally narrowed by `subFolder` and extended with `includeDocument`), "file" (one Vectorworks file given by its full native `filePath`) or "openDocument" (`openDocumentIndex`).

Each entry reports its list `index`, `name`, `actualName`, `folder` and whether it `isInDocument`. `limit` (default 200) and `offset` page the list: `count` is the total number of resources, `returned` the number listed and `truncated` is true when more follow (`nextOffset`); `countOnly` returns just `count`. Internal IFC record formats are filtered out before counts and limits are applied.

> **Note:** `countOnly` leaves out only the `resources` list: the result still has `count`, `returned` (0), `offset`, `limit`, `truncated` and `resourceType`. `nextOffset` is there only when `truncated` is true.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `resourceType` | string | Yes | The kind of resource. Plant styles, title block styles and data tag styles are not types of their own: they are "symbolDefinition" resources kept in the plantStyles / plantLibraries, titleBlocks and objectStyles content folders. One of: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`. |
| `source` | string |  | One of: `document`, `library`, `file`, `openDocument`. |
| `folder` | string |  | The standard Vectorworks content folder to list from when source is "library". One of: `objectLibraries`, `libraries`, `defaults`, `textures`, `gradients`, `hatches`, `imageFills`, `plantStyles`, `renderBackgrounds`, `titleBlocks`, `reports`, `sketchStyles`, `tiles`, `textStyles`, `renderStyles`, `lineTypes`, `recordFormats`, `objectStyles`, `materials`, `wallStyles`, `roofStyles`, `slabStyles`, `plantLibraries`. |
| `subFolder` | string |  | A subfolder of the content folder `folder`; narrows the list when `source` is `library`. |
| `filePath` | string |  | Full path of the file. |
| `openDocumentIndex` | integer |  | Which open document to list when `source` is `openDocument`. |
| `includeDocument` | boolean |  | Also lists the resources of the current drawing when `source` is `library`. |
| `sort` | boolean |  | Sorts the list (default true). Not used when `source` is `file`. |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

**Result**

| Key | Description |
|---|---|
| `resources` | The page of entries; left out with `countOnly`. Each entry has `index` (its place in the list), `name`, `actualName`, `folder` (only when not empty) and `isInDocument`; `uuid` is there only when `isInDocument` is true. |
| `resourceType` | The name of the resource type that was listed. |
| `count`, `returned`, `offset`, `limit`, `truncated`, `nextOffset` | The page, as described under [Paging](Common.md#paging). |

Errors: `unknown resourceType '<x>'` and `unknown content folder '<x>'; expected one of: <names>`; `unknown source: <x>`; `'folder' is required when source is 'library'; expected one of: <names>`; `filePath is required when source is 'file'`; `failed to build the resource list` (with the hint that the content may not be installed or the file could not be opened).

### getResource

Reads one resource of the drawing.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read one resource of the current drawing by uuid, name or internal index: type, name, description, resource folder (`folder` name and `parentFolder` reference) and, for symbol definitions and resource folders, the objects it contains. With `objectUuid` instead, it reports the resources that object uses: `styles` - the text, wall, slab, roof or viewport style it follows (empty when it uses its own settings) - and `activeDataVisualizations` - the data visualizations active on a viewport, saved view or design layer (only when there are any).

Internal IFC record formats are refused; use the IFC tools instead.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `objectUuid` | string |  | UUID of the target object. |

**Result**

With `objectUuid` (it wins over `uuid`, `name` and `index`):

| Key | Description |
|---|---|
| `object` | The object (see [Object references](Common.md#object-references)). |
| `styles` | The resources the object follows, as resource references, in this order: text style, wall style, slab style, roof style, viewport style. Empty when it follows none. |
| `activeDataVisualizations` | The names of the data visualizations active on it. Omitted when there are none. |

Otherwise the resource reference and:

| Key | Description |
|---|---|
| `parentFolder` | The resource folder that holds the resource, as a resource reference. Omitted at the top level. |
| `contents` | For a symbol definition or a resource folder: the objects it contains, as object references. |

A resource reference is an object reference (see [Object references](Common.md#object-references)) plus `resourceType`, `description` (when not empty), `folder` (the name of the resource folder, when not empty), `internalIndex` (when the resource has one) and `contentCount` (symbol definitions and resource folders). The other tools of this page return the same reference.

Errors: `resource not found`; `not a resource`; `object not found: <uuid>`; the refusal for an internal IFC record format.

### importResource

Imports an external resource into the drawing.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: importResource" · **In runToolBatch:** yes

**Details**

Import an external resource into the current drawing and return it. Build the list the same way as getResources, then pick the resource by `name` or by its list `index`. `onConflict` decides what happens when the drawing already has a resource of that name: rename (default), replace, doNotImport or askWithUI. The result has `imported`: false when the resource already in the drawing was returned (it was in the drawing already, or doNotImport on a name conflict).

`classRenamePrefix` prefixes the classes that come with the resource. Internal IFC record formats are refused; use the IFC tools instead.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `resourceType` | string | Yes | The kind of resource. Plant styles, title block styles and data tag styles are not types of their own: they are "symbolDefinition" resources kept in the plantStyles / plantLibraries, titleBlocks and objectStyles content folders. One of: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`. |
| `source` | string |  | One of: `document`, `library`, `file`, `openDocument`. |
| `folder` | string |  | The standard Vectorworks content folder to list from when source is "library". One of: `objectLibraries`, `libraries`, `defaults`, `textures`, `gradients`, `hatches`, `imageFills`, `plantStyles`, `renderBackgrounds`, `titleBlocks`, `reports`, `sketchStyles`, `tiles`, `textStyles`, `renderStyles`, `lineTypes`, `recordFormats`, `objectStyles`, `materials`, `wallStyles`, `roofStyles`, `slabStyles`, `plantLibraries`. |
| `subFolder` | string |  | A subfolder of the content folder `folder`; narrows the list when `source` is `library`. |
| `filePath` | string |  | Full path of the file. |
| `openDocumentIndex` | integer |  | Which open document to list when `source` is `openDocument`. |
| `includeDocument` | boolean |  | Also lists the resources of the current drawing when `source` is `library`. |
| `sort` | boolean |  | Sorts the list (default true). Not used when `source` is `file`. |
| `name` | string |  | The name of the resource to import; it wins over `index`. |
| `index` | integer |  | The list `index` of the resource (see [getResources](#getresources)); used when there is no `name`. |
| `onConflict` | string |  | One of: `rename`, `replace`, `doNotImport`, `askWithUI`. |
| `classRenamePrefix` | string |  | A prefix for the names of the classes that come with the resource. |

**Result**

The resource reference of the imported resource (see [getResource](#getresource)) and:

| Key | Description |
|---|---|
| `imported` | False when the resource already in the drawing was returned instead (it was there already, or `doNotImport` met a name conflict). |
| `note` | Only when `imported` is false: `the resource was already in the drawing; it was returned instead of being imported`. |

Errors: those of getResources for the list arguments; `name or index is required`; `resource not found` (the list has no entry of that `name` or `index`); `failed to import the resource`; the refusal for an internal IFC record format. A failed call is rolled back (`rolledBack`).

### editResource

Renames, describes, moves, duplicates or deletes a resource.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: editResource" · **In runToolBatch:** yes

**Details**

Edit one resource of the current drawing, identified by uuid, name or internal index. `action`: modify (default - rename with `newName`, set `description`, move into the resource folder named by `folder`), duplicate (optionally named by `newName`) or delete. Internal IFC record formats are refused; use the IFC tools instead.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `action` | string |  | One of: `modify`, `duplicate`, `delete`. |
| `newName` | string |  | The new name. |
| `description` | string |  | Description text. |
| `folder` | string |  | The name of an existing resource folder to move the resource into (`modify`). An empty name, or a name no object has, fails (`resource folder not found: <folder>`), so this cannot move a resource to the top level; the name of an object that is not a resource folder gives `applied.folder`: false. |

**Result**

| Action | Result |
|---|---|
| `modify` (default) | `resource` (the resource reference, see [getResource](#getresource)) and `applied`: for each of `newName`, `description` and `folder` that was given, whether it was written. |
| `duplicate` | The resource reference of the copy. With `newName` the copy gets that name; when the name cannot be set (for example it is taken), the copy keeps the name it was given on duplication, and this is not reported. |
| `delete` | `deleted`: false when nothing was deleted. This is not an error. |

Errors: `resource not found`; `not a resource`; `unknown action: <action>`; `resource folder not found: <folder>`; `failed to duplicate the resource`; the refusal for an internal IFC record format. A failed call is rolled back (`rolledBack`).

### createResource

Creates an empty resource.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createResource" · **In runToolBatch:** yes

**Details**

Create an empty resource of `resourceType` in the current drawing, named `name`. When the name is taken, Vectorworks appends a number for most types, so read the returned name back; text, wall, slab and roof styles and record formats return the existing resource of that type instead, with `created`: false in the result, and a single folder name that is taken fails.

**Extra arguments per type:** hatch - `usePageUnits`, `transparent`, `backgroundColor`; lineType - `dashPattern` (alternating line and gap lengths; creates a simple line type) with `scaleWithLineWeight`, or no pattern for a complex one; renderBackground - `kind`; worksheet - `rows`, `columns`; folder - `contentType` (the resource type it holds; a name containing '/' creates nested folders, reusing the folders of the path that already exist for that type at that place, and fails when a name of the path is taken by anything else); imageFill - `pngBase64` (the bytes of a PNG file, base64 encoded) and the required `folder` (the resource folder for image fills that receives the image, created when missing); its `name` must not be in use. Types not listed here (texture, symbolDefinition, recordFormat, gradient, tile, textStyle, wallStyle, slabStyle, roofStyle) need only the name; the rest must be imported with importResource. Internal IFC record formats are refused; use the IFC tools instead.

> **Note:** Worksheets also return the existing worksheet when the `name` is taken by one (with `created`: false); `rows` and `columns` must still be at least 1 but are otherwise ignored. A new worksheet has 20 rows and 10 columns unless `rows` and `columns` say otherwise; both must be at least 1.
>
> **Note:** A simple line type (`dashPattern` given) has no name: `name` is ignored, although the schema still requires it. Simple line types are shared by their dash pattern, so the result may be an existing line type with the same pattern. Whether it is new is not reported: the result has no `created` key, only a `note`. Entries of `dashPattern` that are not numbers are skipped; a pattern with no numbers or with more than 10 numbers fails.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `resourceType` | string | Yes | The kind of resource. Plant styles, title block styles and data tag styles are not types of their own: they are "symbolDefinition" resources kept in the plantStyles / plantLibraries, titleBlocks and objectStyles content folders. One of: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`. |
| `name` | string | Yes | The name of the new resource. For a folder, a name with '/' is a path of nested folders. Ignored for a simple line type. imageFill: must not be used by any other object, nor equal `folder`. |
| `description` | string |  | Description text. |
| `usePageUnits` | boolean |  | Hatch: whether the hatch is sized in page units (default false). |
| `transparent` | boolean |  | Hatch: the `transparent` setting of the hatch (default true). |
| `backgroundColor` | [color](Common.md#colors) |  | Hatch: the background color. |
| `dashPattern` | array of number |  | Alternating line and gap lengths (1 to 10 numbers); creates a simple line type. |
| `scaleWithLineWeight` | boolean |  | Line type with `dashPattern`: whether the dashes scale with the line weight. |
| `kind` | string |  | One of: `clouds`, `oneColor`, `twoColor`, `physicalSky`. Default `oneColor`. |
| `rows` | integer |  | Worksheet: the number of rows (default 20, at least 1). |
| `columns` | integer |  | Worksheet: the number of columns (default 10, at least 1). |
| `contentType` | string |  | Folder (required when `resourceType` is `folder`): the resource type the folder holds; a missing or unknown value fails with `unknown contentType '<x>'; expected one of: ...`. One of: `symbolDefinition`, `worksheet`, `buildingMaterial`, `viewportStyle`, `dataVisualization`, `recordFormat`, `hatch`, `folder`, `class`, `lineType`, `texture`, `roofStyle`, `renderStyle`, `slabStyle`, `tile`, `textStyle`, `renderBackground`, `imageFill`, `gradient`, `wallStyle`. |
| `pngBase64` | string |  | The bytes of a PNG file, base64 encoded. A data URL prefix (`data:image/png;base64,`) is accepted. |
| `folder` | string |  | The resource folder for image fills that receives the image, created when missing. |

**Result**

The resource reference of the resource (see [getResource](#getresource)) and:

| Key | Description |
|---|---|
| `created` | False when the existing resource of that name was returned (styles, record formats, worksheets). Not there for a simple line type. |
| `note` | Only when the existing resource was returned: `a <type> resource named '<name>' already exists; it was returned instead of a new one`. For a simple line type: that the result may be an existing line type with the same pattern. |
| `details` | What [getResourceDetails](#getresourcedetails) reports for the resource: its typed settings. |

Errors: `unknown resourceType '<x>'` and `unknown contentType '<x>'` (the message lists the valid names); `unknown render background kind: <x>`; `creating a <type> resource is not supported; import one instead`; `failed to create the <type> resource`; `an imageFill needs 'folder': the name of a resource folder for image fills (created when missing)` (also when `folder` names an object that is not an image-fill resource folder); `'pngBase64' must hold a PNG file encoded as base64`; `an imageFill needs a 'name' that no other object uses`; `failed to create an image fill from the PNG data`; `failed to register the new folders of '<name>' with Undo; they were removed again`; `failed to register the new folder '<name>' with Undo; it was removed again`; the refusal for an internal IFC record format; a `description` that cannot be set. A failed call is rolled back (`rolledBack`).

If the new resource cannot be registered with Undo, the call fails. A new folder (or the new folders of a path) is removed again. Any other new resource stays in the drawing, although the call returns `err` and `rolledBack`: the message says `was created but could not be registered with Undo, so it stays in the document`.

### getResourceDetails

Reads what a resource holds: hatch levels, gradient stops, line type dashes and more.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read what one resource holds beyond its name: the levels and settings of a hatch, the color stops of a gradient, the spacing, geometry count and `geometryGroup` of a tile, the pixel size of an image fill, the dash pattern of a simple line type or the geometry count and `geometryGroup` of a complex one, the kind and insertion settings of a symbol definition and whether it is the `active` symbol, the size of a texture, the fields of a record format (a field's `type` is a Vectorworks record field type such as text, integer or popUp, not an IFC type), the size and cells of a worksheet, the contents of a resource folder, or the `activeDataVisualizations` of a viewport style.

`geometryGroup` references the group holding the repeated 2D objects. For a worksheet, pass `topLeft` and/or `bottomRight` to read the cells of that range (formula, shown text and, for a number, its unformatted `value`); without them only the size is returned; getWorksheet also reads formats, sizes, merged cells and database subrows. For a dataVisualization it returns only the names of all data visualizations in the document (no criteria or mapping); buildingMaterial, class, renderBackground, renderStyle, roofStyle, slabStyle, textStyle and wallStyle resources return an empty `details`.

The graphic attributes (pen, fill, ...) of a resource that carries them are read and set with getObjectAttributes / setObjectAttributes of the Objects group, given the resource uuid. Internal IFC record formats are refused; use the IFC tools instead.

> **Note:** For a worksheet, the `formula` and `text` of all cells in the range are read first, then the `value` of each number cell. Reading the `value` of a cell that waits for a recalculation makes Vectorworks recalculate the whole worksheet first, which also runs the scripts of RUNSCRIPT formulas. The `value` is then current, but the `text` of the cells can still be the shown text from before that recalculation. getWorksheet does not recalculate: it reports `needsRecalculation` for such a cell instead of a `value`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `topLeft` | object |  | Worksheet: the first cell of the range to read, as `{ row, column }`. Defaults to row 1, column 1 when only `bottomRight` is given. |
| `topLeft.row` | integer |  | Row of the cell (1 is the first row). |
| `topLeft.column` | integer |  | Column of the cell (1 is the first column). |
| `bottomRight` | object |  | Worksheet: the last cell of the range to read, as `{ row, column }`. Defaults to the last row and column when only `topLeft` is given. |
| `bottomRight.row` | integer |  | Row of the cell (1 is the first row). |
| `bottomRight.column` | integer |  | Column of the cell (1 is the first column). |

**Result**

The resource reference of the resource (see [getResource](#getresource)) and `details`. The keys of `details` depend on the type of the resource; a key is there only when its value could be read.

| Kind | Keys of `details` |
|---|---|
| `hatch` | `usePageUnits`, `transparent`, `rotateInWalls`, `rotateInSymbols`, `levels`: one entry per level with `startPoint`, `repeatVector`, `offsetVector`, `dashFactor`, `color` and `lineWeightMils` |
| `gradient` | `segments`: one entry per color stop with `spotPosition`, `midpointPosition`, `color` and `opacity` |
| `tile` | `offset`, `repetition`, `usePageUnits`, `transparentBackground`, `backgroundColor`, `rotateInWalls`, `rotateInSymbols`, `geometryCount` and `geometryGroup` (an object reference, when the tile has one) |
| `imageFill` | `widthPixels`, `heightPixels`, `compression` |
| `lineType` | `simple`; a simple line type adds `dashPattern` and `scaleWithLineWeight`, a complex one `gapSize`, `usePageUnits`, `geometryCount` and `geometryGroup` |
| `symbolDefinition` | `geometryType`, `canInsertIntoWalls`, `containsLight`, `pageBased`, `insertAsGroup`, `insertMode`, `breakMode`, `active` |
| `texture` | `size`, `uvAspectRatio` |
| `recordFormat` | `localizedName`, `parametric`, `visible`, `fields`: one entry per field with `name`, `localizedName`, `type`, `defaultValue` and, for a popUp field, `choices` |
| `worksheet` | `rows`, `columns`; with `topLeft` or `bottomRight` also `cells`: the cells of the range that have a formula or a text (empty cells and cells past `rows` or `columns` are left out; `cells` is empty when `topLeft` or `bottomRight` has a row or column below 1 or `bottomRight` is above or left of `topLeft`), each with `row`, `column`, `formula`, `text` and, for a number, `value` |
| `folder` | `contentType` (the resource type it holds) and `resources` (the resources it holds, as resource references; internal IFC record formats are left out) |
| `viewportStyle` | `activeDataVisualizations` |
| `dataVisualization` | `allNames` |
| any other type | `{}` (empty) |

Errors: `resource not found`; `not a resource`; the refusal for an internal IFC record format.

### setResourceDetails

Changes what a resource holds.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: setResourceDetails" · **In runToolBatch:** yes

**Details**

Change what a resource holds, identified by uuid, name or internal index.

**Per type:** hatch - `usePageUnits`, `transparent`, `rotateInWalls`, `rotateInSymbols`, `levels` (each with startPoint, repeatVector (direction of the lines and repeat length of the dash pattern), offsetVector (spacing to the next parallel line), dashFactor (drawn fraction of each repeat, 1 = solid), color, lineWeightMils; a level past the last one is appended), `addLevels` (levels with the same fields, appended after the last one); gradient - `removeSegments` (0-based indices of the stops to remove, applied before `segments`), `segments` (spotPosition, midpointPosition, color, opacity); tile - `offset`, `repetition`, `usePageUnits`, `transparentBackground`, `backgroundColor`, `rotateInWalls`, `rotateInSymbols`, `addGeometryUuid`; lineType - `gapSize`, `usePageUnits`, `addGeometryUuid`; symbolDefinition - `pageBased`, `insertAsGroup`, `insertMode`, `breakMode`, `addGeometryUuid`, `resetInstances`, `active` (true makes it the active symbol, the one new symbol instances are created from); texture - `size`, `updateThumbnail`; imageFill - `compression`; recordFormat - `localizedName`, `visible`, `addFields` (name, type, defaultValue, choices), `removeFields`, `renameFields` (name, newName), or `fieldName` with `defaultValue` and/or `choices` (replaces the choices of a popUp field); worksheet - `clearCells` ({ topLeft, bottomRight } range whose contents and formatting are cleared before `cells` are set), `cells` (row, column, formula; with `bottomRight` the formula is given to every cell from row/column to there), `insertRows`/`insertColumns`/`deleteRows`/`deleteColumns` with `count`, and `recalculate` (on by default; editWorksheet also sets formats, borders, merged cells, sizes and database rows); folder - `addResourceUuid`. Use editResource to rename, describe, duplicate or delete a resource instead. Internal IFC record formats are refused; use the IFC tools instead.

> **Note:** In `levels`, item `i` is applied to the level with the 0-based index `i`; members that are not given keep the current values. An index directly after the last level appends a level, whose members that are not given are 0, as with `addLevels`, and a larger index is not set (`false` in `applied.levels`). `addLevels` always appends, and every member that is not given is 0, so give `dashFactor` (1 = solid; the core expects a value above 0).
>
> **Note:** In `segments`, item `i` is applied to the stop with the 0-based index `i`; members that are not given keep the current values, and an index past the last stop inserts a new stop, whose members that are not given default to `spotPosition` 0, `midpointPosition` 0.5, `color` black (`{ "r": 0, "g": 0, "b": 0 }`) and `opacity` 100 (give all four). `removeSegments` runs first, so the indices of `segments` refer to the stops that remain. Vectorworks keeps the stops sorted by `spotPosition`: a stop whose new `spotPosition` passes a neighbor, and a new stop, move to their sorted place before the next item is applied, so later items address the re-sorted stops. Give `segments` in increasing `spotPosition` order.
>
> **Note:** `addFields[].type` lists `radio`, `controlPoint` and `layerPopUp`, but a field of one of these types is never added (`added: false`). An unknown type name is an error.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `usePageUnits` | boolean |  | Hatch, tile and line type: `true` measures the pattern on the printed page instead of in world units. |
| `transparent` | boolean |  | Hatch: `true` leaves the area behind the hatch lines transparent instead of filling it with the background. |
| `rotateInWalls` | boolean |  | Hatch and tile: whether the pattern follows the rotation of the wall it is drawn in. |
| `rotateInSymbols` | boolean |  | Hatch and tile: whether the pattern follows the rotation of the symbol it is drawn in. |
| `levels` | array of object |  | Hatch: item `i` sets the level `i` (see the first Note). Item members: `startPoint`, `repeatVector`, `offsetVector` ([points](Common.md#points)), `dashFactor` (number), `color` ([color](Common.md#colors)), `lineWeightMils` (integer, in mils = 1/1000 inch). |
| `addLevels` | array of object |  | Levels with the same fields, appended after the last one; members that are not given are 0 (give `dashFactor`). |
| `segments` | array of object |  | Gradient: item `i` sets the stop `i` (see the second Note). Item members: `spotPosition`, `midpointPosition` (numbers), `color` ([color](Common.md#colors)), `opacity` (integer). |
| `removeSegments` | array of integer |  | 0-based indices of the stops to remove, applied before `segments`. Duplicates and entries that are negative or not integers are ignored. |
| `offset` | [point](Common.md#points) |  | Tile: the origin of the tile grid. |
| `repetition` | [point](Common.md#points) |  | Tile: the step from one repetition to the next. |
| `transparentBackground` | boolean |  | Tile: whether the background of the tile is transparent. |
| `backgroundColor` | [color](Common.md#colors) |  | Tile: the background color. |
| `gapSize` | number |  | Line type: the gap between two repetitions of the geometry, in world units (in page units when the line type uses page units). |
| `addGeometryUuid` | string |  | Tile, line type and symbol definition: UUID of an existing object that is moved into the resource's geometry. `applied.addGeometry` is false when the object is not found or cannot be added. |
| `pageBased` | boolean |  | Symbol definition: `true` keeps the symbol at its size on the printed page instead of in world units. |
| `insertAsGroup` | boolean |  | Symbol definition: `true` inserts a copy of the symbol's contents instead of a symbol instance. |
| `resetInstances` | boolean |  | Symbol definition: `true` resets the instances of the definition; `false` does nothing. |
| `active` | boolean |  | True makes it the active symbol, the one new symbol instances are created from. |
| `insertMode` | string |  | One of: `edge`, `center`, `leftEdge`, `rightEdge`, `coreComponentCenter`, `coreComponentLeftEdge`, `coreComponentRightEdge`, `wallInsertLocation`, `wallClosureInsertLocation`. |
| `breakMode` | string |  | One of: `fullWithCaps`, `fullNoCaps`, `half`, `none`. |
| `size` | number |  | Texture: the real-world size that the texture image covers, in world units. |
| `updateThumbnail` | boolean |  | Texture: `true` refreshes the Resource Manager preview of the texture; `false` does nothing. |
| `compression` | string |  | One of: `none`, `jpeg`, `png`, `pngMonochrome`. |
| `localizedName` | string |  | Record format: the localized name of the format. |
| `visible` | boolean |  | Record format: `false` hides the format from the data pane of the Object Info palette. |
| `addFields` | array of object |  | Item members: `name`, `type` (`text` when omitted), `defaultValue`, `choices`. |
| `addFields[].name` | string |  | Name of the new field. The field is not added (`added: false`) when the name is empty or the format already has a field of that name. |
| `addFields[].type` | string |  | One of: `integer`, `boolean`, `real`, `text`, `dimension`, `popUp`, `radio`, `staticText`, `controlPoint`, `classPopUp`, `layerPopUp`, `angle`, `area`, `volume`, `class`, `buildingMaterial`, `fill`, `penStyle`, `penWeight`, `color`, `texture`, `symbolDefinition`. `radio`, `controlPoint` and `layerPopUp` are listed but never added. |
| `addFields[].defaultValue` | string |  | Default value as text. `text`, `popUp`, `staticText` and `classPopUp` fields keep it as it is; for every other type it is read the way Vectorworks reads a value typed by the user (a number, a flag, the name of an existing resource, a color). A value that is not valid for the type makes the add fail (`added: false`); an empty string is always accepted. |
| `addFields[].choices` | array of string |  | Choices of a popUp field, set once the field was added. |
| `removeFields` | array of string |  | Names of the fields to remove; entries that are not strings are skipped. |
| `renameFields` | array of object |  | Item members: `name`, `newName`. |
| `renameFields[].name` | string |  | Current name of the field. |
| `renameFields[].newName` | string |  | New name. `renamed` is false when the field does not exist, when `newName` is already a field, or when the rename fails. |
| `fieldName` | string |  | Existing field whose `defaultValue` and/or `choices` is replaced. |
| `defaultValue` | string |  | New default value of `fieldName`, as text, converted by the field type through the record format API (not the stricter parsing of `addFields[].defaultValue`). `applied.defaultValue` is true whenever the field exists, even when the text cannot be converted and the default stays unchanged. |
| `choices` | array of string |  | Replaces the choices of the popUp field `fieldName`; the field type is not checked, so `applied.choices` is true for any existing field. |
| `clearCells` | object |  | { topLeft, bottomRight } range whose contents and formatting are cleared before `cells` are set. |
| `clearCells.topLeft` | object |  | First cell of the range; row 1, column 1 when omitted. |
| `clearCells.topLeft.row` | integer |  | Row, 1-based (1 when omitted). |
| `clearCells.topLeft.column` | integer |  | Column, 1-based (1 when omitted). |
| `clearCells.bottomRight` | object |  | Last cell of the range; the first cell when omitted. |
| `clearCells.bottomRight.row` | integer |  | Row, 1-based (the row of `topLeft` when omitted). |
| `clearCells.bottomRight.column` | integer |  | Column, 1-based (the column of `topLeft` when omitted). |
| `cells` | array of object |  | Row, column, formula; with `bottomRight` the formula is given to every cell from row/column to there. |
| `cells[].row` | integer |  | Row, 1-based (1 when omitted). |
| `cells[].column` | integer |  | Column, 1-based (1 when omitted). |
| `cells[].formula` | string |  | The formula set in the cell, or in every cell of the range when `bottomRight` is given. |
| `cells[].bottomRight` | object |  | Last cell of the range; the cell itself when omitted. |
| `cells[].bottomRight.row` | integer |  | Row, 1-based (the row of the cell when omitted). |
| `cells[].bottomRight.column` | integer |  | Column, 1-based (the column of the cell when omitted). |
| `insertRows` | integer |  | Worksheet: the row before which `count` rows are inserted. |
| `insertColumns` | integer |  | Worksheet: the column before which `count` columns are inserted. |
| `deleteRows` | integer |  | Worksheet: the first of the `count` rows to delete. |
| `deleteColumns` | integer |  | Worksheet: the first of the `count` columns to delete. |
| `count` | integer |  | Number of rows or columns for `insertRows`, `insertColumns`, `deleteRows` and `deleteColumns` (default 1). Each of them is false in `applied` when its row or column, or `count`, is not above 0. |
| `recalculate` | boolean |  | Recalculate the worksheet after the change; on by default. |
| `addResourceUuid` | string |  | Folder: UUID of an existing resource that is moved into the folder (`applied.addResource`). |

**Result**

The resource reference of the changed resource (see [getResource](#getresource)) and:

| Key | Description |
|---|---|
| `applied` | What was written, per argument that was given (see the table below). |
| `details` | The details of the resource after the change, with the keys that [getResourceDetails](#getresourcedetails) reports for its kind. |

The entries of `applied` are named after the arguments, except `addGeometryUuid` (entry `addGeometry`) and `addResourceUuid` (entry `addResource`):

| Argument | Entry in applied |
|---|---|
| `usePageUnits`, `transparent`, `rotateInWalls`, `rotateInSymbols`, `offset`, `repetition`, `transparentBackground`, `backgroundColor`, `gapSize`, `pageBased`, `insertAsGroup`, `insertMode`, `breakMode`, `size`, `compression`, `localizedName`, `visible` | A boolean: true when the value was written. `insertMode` and `breakMode` are false for a name that is not in the list. |
| `levels`, `addLevels`, `segments` | An array with a boolean per item, in order. |
| `removeSegments` | An array of `{ index, removed }`. The indices are processed from the highest to the lowest. |
| `addGeometryUuid`, `addResourceUuid` | A boolean. |
| `resetInstances`, `active`, `updateThumbnail` | A boolean, present only when the argument is `true`. |
| `addFields` | An array of `{ name, added }`. |
| `removeFields` | An array of `{ name, removed }`. |
| `renameFields` | An array of `{ name, newName, renamed }`. |
| `defaultValue`, `choices` | A boolean, for the field `fieldName`. |
| `insertRows`, `insertColumns`, `deleteRows`, `deleteColumns`, `clearCells` | A boolean. |
| `cells` | An array of `{ row, column, set }`, one entry per item. |
| `recalculate` | A boolean; present unless `recalculate` is false. |

A worksheet is changed in this order: `insertRows`, `insertColumns`, `deleteRows`, `deleteColumns`, `clearCells`, `cells`, then the recalculation. So `clearCells` and `cells` refer to the rows and columns after the inserts and deletes.

Errors: `resource not found`; `not a resource`; `unknown compression: <x>`; `unknown record field type: <x>`; `the <type> resource has no typed settings; use editResource` (the resource type has no settings in this tool); the refusal for an internal IFC record format. A failed call is rolled back (`rolledBack`).

### applyResource

Applies a texture, style or data visualization to an object.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: applyResource" · **In runToolBatch:** yes

**Details**

Apply a resource of the current drawing (given by `resourceUuid` or `resourceName`) to the object given by `objectUuid`: a texture (optionally to one `part` of the object), a text style, a wall style (with `selectedOffset` and `replacingOffset` deciding which line stays in place), a slab, roof or viewport style, or a data visualization (`activate` turns it off when false; `excludeObject` instead keeps the object out of every data visualization when true, or lets it back in when false).

A symbol definition is instanced instead: it is inserted into the drawing at `position` with `rotation` in radians. A worksheet is placed on the active layer as a worksheet image with its top left corner at `position`; a worksheet that is already placed has its image moved there instead (`moved` is true). Neither needs an `objectUuid`. Internal IFC record formats are refused; use the IFC tools instead.

> **Note:** `resourceUuid` takes precedence over `resourceName`. Every resource except a symbol definition and a worksheet needs `objectUuid`. `excludeObject` still needs the data visualization as `resourceUuid` or `resourceName`, but it acts on the object for every data visualization.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `resourceUuid` | string |  | UUID of the resource to apply. Takes precedence over `resourceName`. |
| `resourceName` | string |  | Name of the resource. Used only when `resourceUuid` is absent; an empty or unknown `resourceUuid` gives `resource not found`. |
| `objectUuid` | string |  | UUID of the target object. Not used for a symbol definition or a worksheet. |
| `part` | string |  | Texture: the part of the object that gets the texture (default `overall`). One of: `overall`, `extrudeTop`, `extrudeBottom`, `extrudeSides`, `wallLeft`, `wallRight`, `wallTop`, `wallBottom`, `slabTop`, `slabBottom`, `slabSides`, `roofTop`, `roofBottom`, `roofSides`. |
| `selectedOffset` | number |  | Wall style: with `replacingOffset`, decides which line of the wall stays in place (default 0). |
| `replacingOffset` | number |  | Wall style: with `selectedOffset`, decides which line of the wall stays in place (default 0). |
| `activate` | boolean |  | Data visualization: `false` turns the data visualization off for the object (default `true`). Ignored when `excludeObject` is given. |
| `excludeObject` | boolean |  | Data visualization: `true` keeps the object out of every data visualization, `false` lets it back in. |
| `position` | [point](Common.md#points) |  | Symbol definition: the insertion point of the instance. Worksheet: the top left corner of the worksheet image. Default (0, 0). |
| `rotation` | number |  | Symbol definition: the rotation of the instance, in radians (default 0). |

**Result**

`resource` is the resource reference (see [getResource](#getresource)) and `object` is the object reference of the object that was created or changed (see [Object references](Common.md#object-references)). The other keys depend on the resource:

| Resource | `object` and the other keys |
|---|---|
| Symbol definition | `object` is the new symbol instance. There are no other keys. |
| Worksheet | `object` is the worksheet image. `moved` is `true` when the worksheet was already placed and its image was moved, and `false` when a new image was created. |
| Any other resource | `object` is the target object. `applied` is `true`. |

Errors: `resource not found`; `not a resource`; the refusal for an internal IFC record format; `failed to insert the symbol`; `failed to place the worksheet in the drawing`; `object not found` (`objectUuid` is missing or names no object); `unknown texture part: <x>`; `a <type> resource cannot be applied to an object` (the resource type has no apply action); `failed to apply the resource to the object`. A failed call is rolled back (`rolledBack`).

### getWorksheet

Reads a worksheet: its size, cells, formats and database rows.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read a worksheet resource in detail: its size (`rows`, `columns`), `autoRecalculate`, the worksheet `image` placed on a layer (when there is one) and the cells of a range. Cells are { row, column }, 1-based (column 1 is A); the range is `topLeft` to `bottomRight` (default: the whole worksheet). Each cell has its `formula` (the definition: a literal, or a formula starting with '='), the shown `text` and, for a number, its `value`; texts and values are those of the last recalculation (editWorksheet recalculates).

A cell whose formula waits for a recalculation has `needsRecalculation`: true instead of a `value`, because reading its value would make Vectorworks recalculate the worksheet. Cells without a formula or text are left out unless `includeEmpty` is true. `include` adds "formats" (per cell `numberFormat`, `textFormat`, `fill`, `borders` and, for a merged cell, `merged` with its range; the keys are those that editWorksheet takes, with `fontIndex` instead of `font` for a font without a name), "sizes" (`columnWidths` and `rowHeights` of the range, in worksheet pixels) and "database" (`databaseRows`: the database rows of the range with their `criteria` and `subrowCount`).

`subrowsOf` (the row of a database row) lists that row's `subrows` instead of the cells: one per object that the criteria found, each with the `text` and `value` of the columns of the range. `limit` (default 200 cells or 100 subrows), `offset` and `countOnly` page the cells or subrows. Pass the worksheet's `uuid`, `name` or `index`, or the `uuid` of a worksheet placed on a layer. createResource creates a worksheet, applyResource places it on a layer, and getResourceDetails / setResourceDetails read and set plain cells too.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `topLeft` | object |  | First cell of the range, `{ row, column }`; both are needed. Row 1, column 1 when omitted. |
| `topLeft.row` | integer |  | Row, 1-based. |
| `topLeft.column` | integer |  | Column, 1-based (column 1 is A). |
| `bottomRight` | object |  | Last cell of the range, `{ row, column }`; both are needed. The last cell of the worksheet when omitted. It must not be above or left of `topLeft`. |
| `bottomRight.row` | integer |  | Row, 1-based. |
| `bottomRight.column` | integer |  | Column, 1-based. |
| `include` | array of string |  | Each item one of: `formats`, `sizes`, `database`. Not allowed with `subrowsOf`. |
| `includeEmpty` | boolean |  | `true` also lists the cells that have neither a formula nor a text. Not allowed with `subrowsOf`. |
| `subrowsOf` | integer |  | The row of a database row (1 to the number of rows). The subrows of that row are listed instead of the cells. |
| `limit` | integer |  | Paging: the maximum number of cells (default 200) or subrows (default 100) to return (at least 1). See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

**Result**

The worksheet and the range that was read:

| Key | Description |
|---|---|
| `worksheet` | The resource reference of the worksheet (see [getResource](#getresource)). |
| `rows`, `columns` | The size of the worksheet. |
| `autoRecalculate` | Whether the worksheet recalculates itself automatically. |
| `image` | The object reference of the worksheet image. Only when the worksheet is placed on a layer. |
| `topLeft`, `bottomRight` | The range, each `{ row, column }`. |

Without `subrowsOf`, the result is the page of the cells (see [Paging](Common.md#paging)): `count` is the number of listed cells, and the cells are in `cells`; with `countOnly` they are left out. With `include`, the result also has:

| Key | Description |
|---|---|
| `columnWidths` | With `sizes`: `{ column, width }` for each column of the range that has a width, in worksheet pixels. |
| `rowHeights` | With `sizes`: `{ row, height, locked }` for each row of the range that has a height, in worksheet pixels. |
| `databaseRows` | With `database`: `{ row, criteria, subrowCount }` for each database row of the range. |

`columnWidths`, `rowHeights` and `databaseRows` are left out with `countOnly`.

Each item of `cells` has `row`, `column`, `formula` and `text`, and, for a number, `value`. A cell that waits for a recalculation has `needsRecalculation: true` and no `value`. With `formats`, an item also has `numberFormat`, `textFormat`, `fill`, `borders` and `merged` (`{ topLeft, bottomRight }`), each only when the cell has it.

With `subrowsOf`, the result has `subrowsOf` (the row) and the page of the subrows of that row in `subrows`; `count` is the number of subrows. Each item has `subrow` (1-based; item 0 is subrow 1) and `cells`: `{ column, text }` and, for a number, `value`, for each column of the range that the subrow has.

Errors: `no worksheet found: pass the 'uuid', 'name' or 'index' of a worksheet resource, or the 'uuid' of a worksheet placed on a layer`; `the object found is not a worksheet resource or a worksheet placed on a layer`; `'include' must be an array of: formats, sizes, database`; `'includeEmpty' must be true or false`; `'subrowsOf' cannot be used with 'include' or 'includeEmpty'`; `'topLeft' must be a cell { "row", "column" } of whole numbers` (also for `bottomRight`); `'topLeft' is outside the worksheet: row <n>, column <n>; the worksheet has <n> rows and <n> columns` (also for `bottomRight`); `'bottomRight' must not be above or left of 'topLeft'`; `'subrowsOf' must be a whole number from 1 to <rows>`; `row <n> is not a database row`. Errors of the paging arguments, such as `'limit' must be at least 1`, are described in [Results and errors](Common.md#results-and-errors).

### editWorksheet

Changes a worksheet with a list of actions.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: editWorksheet" · **In runToolBatch:** yes

**Details**

Change a worksheet resource with a list of `actions` (1 to 100), applied in order as one undoable step: when one fails, the call fails and the worksheet is left unchanged. Cells are { row, column }, 1-based (column 1 is A); a range is `topLeft` with an optional `bottomRight` (default: `topLeft`). Each action is an object with `action` and its arguments: setFormula (range, `formula`: a literal, or a formula starting with '=' such as =SUM(A1..A3), given to every cell of the range); clear (range: contents and formats); insertRows / insertColumns (`before`, `count`, default 1); deleteRows / deleteColumns (`start`, `count`, default 1; a worksheet keeps at least one row and one column); setNumberFormat (range, `numberStyle`, `accuracy`, `leader`, `trailer`); setTextFormat (range, `font` (a font name), `size` (points), `bold`, `italic`, `underline`, `outline`, `shadow`, `alignment`, `verticalAlignment`, `angle` (whole degrees), `color`, `wrap`); setFill (range, `fillStyle`, `background`, `foreground`, `pattern`; "solid" needs `background`, "pattern" needs `pattern`, `foreground` and `background`); these three change only the fields given, cell by cell, at most 10000 cells per action (setTextFormat leaves out cells hidden by a merge that have no font of their own, and needs `font` for other cells without one, such as cells split again after a merge); setBorders (range, `top`, `left`, `bottom`, `right`, `outline`, `insideHorizontal`, `insideVertical`: draws these borders; it cannot remove borders, since a false flag leaves a border as it is); merge (a range of two or more cells) / unmerge (range); setColumnWidth (`column`, `lastColumn`, `width`) and setRowHeight (`row`, `lastRow`, `height`, `lockHeight` (default true), `includeSubrows`), in worksheet pixels; autoFitRowHeights (`row`, `lastRow`); setDatabaseCriteria (`row`, `criteria` such as =DATABASE((T=RECT)), which makes the row a database row with one subrow per object found; an empty `criteria` makes it a plain row again); recalculate; setAutoRecalculate (`enabled`).

`recalculate` (default true) recalculates the worksheet after the actions; a recalculation also runs the scripts of RUNSCRIPT formulas. The result has the new `rows` and `columns` and an `applied` entry per action; read the cells back with getWorksheet.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `actions` | array of object | Yes | 1 to 100 items. |
| `actions[].action` | string | Yes | One of: `setFormula`, `clear`, `insertRows`, `insertColumns`, `deleteRows`, `deleteColumns`, `setNumberFormat`, `setTextFormat`, `setFill`, `setBorders`, `merge`, `unmerge`, `setColumnWidth`, `setRowHeight`, `autoFitRowHeights`, `setDatabaseCriteria`, `recalculate`, `setAutoRecalculate`. |
| `actions[].topLeft` | object |  | The first cell of the range, `{ row, column }`; both are needed. Needed by `setFormula`, `clear`, `setNumberFormat`, `setTextFormat`, `setFill`, `setBorders`, `merge` and `unmerge`. |
| `actions[].topLeft.row` | integer |  | Row, 1-based. |
| `actions[].topLeft.column` | integer |  | Column, 1-based (column 1 is A). |
| `actions[].bottomRight` | object |  | The last cell of the range, `{ row, column }`. The range is the single cell `topLeft` when omitted. It must not be above or left of `topLeft`. |
| `actions[].bottomRight.row` | integer |  | Row, 1-based. |
| `actions[].bottomRight.column` | integer |  | Column, 1-based. |
| `actions[].formula` | string |  | `setFormula`: required. A literal, or a formula that starts with `=`, such as `=SUM(A1..A3)`; every cell of the range gets it. |
| `actions[].before` | integer |  | `insertRows` and `insertColumns`: required. The new rows or columns are inserted before this row or column, 1 to the number of rows or columns plus 1. |
| `actions[].start` | integer |  | `deleteRows` and `deleteColumns`: required. The first row or column to delete, 1 to the number of rows or columns. |
| `actions[].count` | integer |  | `insertRows` and `insertColumns`: how many to insert, 1 to 32767 (default 1). `deleteRows` and `deleteColumns`: how many to delete from `start` on (default 1); the worksheet keeps at least one row and one column. |
| `actions[].numberStyle` | string |  | `setNumberFormat`: the number style, one of `general`, `decimal`, `decimalWithCommas`, `scientific`, `fractional`, `dimension`, `angle`, `date`, `conditional`, `generalFraction`, `dimensionWithDivider`, `area`, `volume`, `text`, `percentage`. |
| `actions[].accuracy` | integer |  | `setNumberFormat`: the accuracy of the number format, 0 to 127. What it means depends on the number style; it is not always the number of decimal places. |
| `actions[].leader` | string |  | `setNumberFormat`: the leader of the number format. |
| `actions[].trailer` | string |  | `setNumberFormat`: the trailer of the number format. |
| `actions[].font` | string |  | `setTextFormat`: the name of a font that Vectorworks knows. Needed for a cell that has no font of its own, such as a cell that was split again after a merge. |
| `actions[].size` | integer |  | `setTextFormat`: the font size in points, 1 to 32767. |
| `actions[].bold` | boolean |  | `setTextFormat`: `true` sets bold, `false` clears it. Unchanged when omitted. |
| `actions[].italic` | boolean |  | `setTextFormat`: `true` sets italic, `false` clears it. Unchanged when omitted. |
| `actions[].underline` | boolean |  | `setTextFormat`: `true` sets underline, `false` clears it. Unchanged when omitted. |
| `actions[].outline` | boolean |  | `setTextFormat`: `true` sets the outline text style, `false` clears it; unchanged when omitted. `setBorders`: `true` draws the outline border of the range (default `false`). |
| `actions[].shadow` | boolean |  | `setTextFormat`: `true` sets the shadow text style, `false` clears it. Unchanged when omitted. |
| `actions[].alignment` | string |  | `setTextFormat`: the horizontal alignment, one of `general`, `left`, `center`, `right`. |
| `actions[].verticalAlignment` | string |  | `setTextFormat`: the vertical alignment, one of `general`, `top`, `center`, `bottom`. |
| `actions[].angle` | integer |  | `setTextFormat`: the text angle in whole degrees, -360 to 360. |
| `actions[].color` | [color](Common.md#colors) |  | `setTextFormat`: the text color. Converted to the nearest color of the document palette; `getWorksheet` reports that color. |
| `actions[].wrap` | boolean |  | `setTextFormat`: whether the text wraps in the cell. |
| `actions[].fillStyle` | string |  | `setFill`: the kind of fill, one of `none`, `solid`, `pattern`. |
| `actions[].background` | [color](Common.md#colors) |  | `setFill`: the background color. Needed for `fillStyle` `solid` and `pattern`. Converted to the nearest color of the document palette. |
| `actions[].foreground` | [color](Common.md#colors) |  | `setFill`: the foreground color of the pattern. Needed for `fillStyle` `pattern`. Converted to the nearest color of the document palette. |
| `actions[].pattern` | integer |  | `setFill`: the fill pattern, 0 to 32767. Needed for `fillStyle` `pattern`. |
| `actions[].top` | boolean |  | `setBorders`: `true` draws the top edge of the range (default `false`). |
| `actions[].left` | boolean |  | `setBorders`: `true` draws the left edge of the range (default `false`). |
| `actions[].bottom` | boolean |  | `setBorders`: `true` draws the bottom edge of the range (default `false`). |
| `actions[].right` | boolean |  | `setBorders`: `true` draws the right edge of the range (default `false`). |
| `actions[].insideHorizontal` | boolean |  | `setBorders`: `true` draws the horizontal lines between the rows of the range (default `false`). |
| `actions[].insideVertical` | boolean |  | `setBorders`: `true` draws the vertical lines between the columns of the range (default `false`). |
| `actions[].column` | integer |  | `setColumnWidth`: required. The first column to size, 1 to the number of columns. |
| `actions[].lastColumn` | integer |  | `setColumnWidth`: the last column to size, from `column` to the number of columns (default `column`). |
| `actions[].width` | integer |  | `setColumnWidth`: required. The width in worksheet pixels, 1 to 32767. |
| `actions[].row` | integer |  | `setRowHeight` and `autoFitRowHeights`: required. The first row to change, 1 to the number of rows. `setDatabaseCriteria`: required. The row that gets the criteria, 1 to the number of rows. |
| `actions[].lastRow` | integer |  | `setRowHeight` and `autoFitRowHeights`: the last row to change, from `row` to the number of rows (default `row`). |
| `actions[].height` | integer |  | `setRowHeight`: required. The height in worksheet pixels, 1 to 32767. |
| `actions[].lockHeight` | boolean |  | `setRowHeight`: whether the new height is locked (default `true`). `getWorksheet` reports it as `locked`. |
| `actions[].includeSubrows` | boolean |  | `setRowHeight`: `true` sizes the subrows of database rows in the range too (default `false`). |
| `actions[].criteria` | string |  | `setDatabaseCriteria`: required. A database definition such as `=DATABASE((T=RECT))`. An empty string makes the row a plain row. |
| `actions[].enabled` | boolean |  | `setAutoRecalculate`: required. `true` turns the automatic recalculation of the worksheet on, `false` turns it off. |
| `recalculate` | boolean |  | `true` (default) recalculates the worksheet after the actions; `false` skips that. The `recalculate` action recalculates it in the middle of the list. |

**Result**

The worksheet after the actions:

| Key | Description |
|---|---|
| `worksheet` | The resource reference of the worksheet (see [getResource](#getresource)). |
| `rows`, `columns` | The size of the worksheet after the actions. |
| `applied` | One entry for each action, in the order of `actions`. Each entry has `action` (the name of the action) and the keys that the next table lists. |
| `recalculated` | `true` when the worksheet was recalculated after the actions; `false` when `recalculate` is `false` or the recalculation failed. |

The keys of an `applied` entry, besides `action`:

| Action | Keys |
|---|---|
| `setFormula`, `clear`, `setBorders`, `merge`, `unmerge` | `topLeft` and `bottomRight`: the range, each `{ row, column }`. |
| `setNumberFormat`, `setTextFormat`, `setFill` | `cells`: the number of cells in the range; `topLeft` and `bottomRight`. |
| `insertRows`, `deleteRows` | `rows`: the number of rows after the action. |
| `insertColumns`, `deleteColumns` | `columns`: the number of columns after the action. |
| `setDatabaseCriteria` | `row`, and `isDatabaseRow`: whether the row is a database row now. |
| `setAutoRecalculate` | `enabled`. |
| `setColumnWidth`, `setRowHeight`, `autoFitRowHeights`, `recalculate` | None. |

Before anything changes, the call checks the worksheet, `recalculate` and the list of actions. Errors: `no worksheet found: pass the 'uuid', 'name' or 'index' of a worksheet resource, or the 'uuid' of a worksheet placed on a layer`; `the object found is not a worksheet resource or a worksheet placed on a layer`; `'recalculate' must be true or false`; `'actions' must be an array of 1 to 100 actions`; `actions[<i>]: 'action' must be one of: <names>`.

An action that fails ends the call at once. The call is rolled back (`rolledBack`, see [Results and errors](Common.md#results-and-errors)), so the worksheet keeps the state it had before the call. The error starts with `actions[<i>] (<action>): `, where `<i>` is the position of the action in `actions`, counted from 0. Errors of the arguments: `'topLeft' must be a cell { "row", "column" } of whole numbers` (also for `bottomRight`); `'topLeft' is outside the worksheet: row <n>, column <n>; the worksheet has <n> rows and <n> columns` (also for `bottomRight`); `'bottomRight' must not be above or left of 'topLeft'`; `'topLeft' and 'bottomRight' must span at least two cells` (`merge`); `'<key>' must be a whole number from <min> to <max>`; `'<key>' must be true or false`; `'<key>' must be a string`; `'<key>' must be one of: <names>` (`numberStyle`, `alignment`, `verticalAlignment`, `fillStyle`); `'<key>' must be a color { "r", "g", "b" } with values from 0 to 255`; `'font' must be the name of a font that Vectorworks knows`; `give at least one of: numberStyle, accuracy, leader, trailer` (`setTextFormat` and `setFill` name their own arguments in the same way); `'fillStyle' "solid" needs 'background'`; `'fillStyle' "pattern" needs 'pattern', 'foreground' and 'background'`; `the range has <n> cells; at most 10000 cells are formatted in one action`; `row <r>, column <c> uses the default font of the worksheet (as cells that were merged away do): give 'font' too`; `a worksheet keeps at least one row` (also `column`).

When Vectorworks refuses a change, the error starts with `Vectorworks did not` and names the change, for example `Vectorworks did not insert the rows (a worksheet has a maximum number of rows)`; `Vectorworks did not merge the cells: the range must not cut through merged cells or hold a database row`; `Vectorworks did not set the database criteria: a row with merged cells cannot become a database row, and the criteria must be a database definition such as =DATABASE((T=RECT))`; `Vectorworks did not recalculate the worksheet`.

Limits: 100 actions in a call; 10000 cells in one format action; `count`, `width` and `height` at most 32767.
