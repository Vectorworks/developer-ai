**English** • [Deutsch](../../MCP.de/v2027.2/DocumentAccess.md) • [日本語](../../MCP.ja/v2027.2/DocumentAccess.md)

# DocumentAccess — document and selection

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools for the active drawing as a whole and for the current selection: the document summary, layers, stories, classes, units, the view and the document preferences, and bulk edits of the selected objects.

## Table of contents

- [Overview](#overview)
- [Document](#document)
  - [getDocumentInfo](#getdocumentinfo)
  - [getLayers](#getlayers)
  - [createLayer](#createlayer)
  - [editLayer](#editlayer)
  - [getStories](#getstories)
  - [createStory](#createstory)
  - [editStory](#editstory)
  - [getClasses](#getclasses)
  - [createClass](#createclass)
  - [editClass](#editclass)
  - [setActiveContext](#setactivecontext)
  - [getUnits](#getunits)
  - [setUnits](#setunits)
  - [convertUnits](#convertunits)
  - [setView](#setview)
  - [getPreferences](#getpreferences)
  - [setPreferences](#setpreferences)
- [Selection](#selection)
  - [getSelection](#getselection)
  - [selectObjects](#selectobjects)
  - [editSelection](#editselection)

## Overview

This folder holds 2 tool groups with 20 tools in total.

| Group | Group ID | Active by default | Risk level | Tools | Summary |
|---|---|---|---|---|---|
| [Document](#document) | `document` | Yes | low | 17 | The active drawing: document summary, layers, stories, classes, units, view and document preferences. |
| [Selection](#selection) | `selection` | Yes | medium | 3 | List the current selection and move, rotate, scale, duplicate, group, delete or re-class it in bulk. |

## Document

> **Group:** `Document` · **Group ID:** `document` · **Active by default:** Yes · **Risk level:** low · **Tools:** 17

**The active drawing: document summary, layers, stories, classes, units, view and document preferences.**

Inspect and manage the active Vectorworks drawing itself: document summary, layers, stories, classes, units, view and document preferences. Read getDocumentInfo, getLayers and getClasses when the task depends on the drawing's layers, classes, units or active context. Their results are read live and stay valid until the drawing changes - through your edits or the user's; the selection and active layer change often.

How a Vectorworks drawing is composed:

- A document is one drawing file. Everything lives either on a layer (the drawing content) or in the resource list of the document (reusable definitions - see the Resources group).
- LAYERS are the containers of all geometry. A DESIGN LAYER holds real-world model content: its coordinates are world units and its scale (1:scale) only decides how large the page-based graphics, text and line weights print. A SHEET LAYER is a printable page; it holds viewports (cropped, scaled views of design layers), title blocks and page annotation. Exactly one layer is active at a time and new objects are created on it.
- STORIES are the floors of a building (BIM): each has an elevation and levels, named heights (level types such as `OK-FB`) at an offset from the story elevation. A level can have its own design layer, whose elevation then follows the level, and walls bind their top and bottom to levels. BIM workflow order: stories (getStories, createStory, editStory) → styles (Resources group) → building elements (Architecture group) on the story layers.
- CLASSES are named, saved attribute sets (pen, fill, line weight, opacity, markers, drop shadow, texture, text style) that cut across layers. Every object belongs to exactly one class. An attribute set 'by class' on an object follows its class, so re-styling a class re-styles every object that defers to it. Classes also drive visibility: an object is drawn only when both its layer and its class are visible. The class `None` always exists.
- OBJECTS are the geometry: 2D primitives, parametric plug-in objects (walls, doors, plants, data tags, ...), groups, symbol instances and viewports. Each has a stable uuid, a class, graphical attributes and - for plug-in objects - a parameter record. Containers (groups, symbol definitions, viewport annotations) nest objects; new objects go into the container currently being edited, which getDocumentInfo reports as `container`.
- RESOURCES are the reusable definitions stored in the document: symbol definitions, hatches, gradients, tiles, image fills, line types, textures, record formats, worksheets, text styles and object (plug-in) styles. Objects reference them; a plug-in object driven by an object style takes its parameters from that style.
- COORDINATES are world units (the internal length unit the API uses); the UI shows them converted to the document units (use convertUnits). The USER ORIGIN is the world point the user sees as (0,0). Angles are radians, counter-clockwise from the X axis.
- UNDO: each call that changes the drawing is ONE undo step 'MCP: &lt;tool&gt;' that the user can undo (Vectorworks shows the name in the status message after Edit &gt; Undo), and a call that fails changes nothing (`rolledBack` in its result). To make a user-level job one undo step, do it in one runPythonScript run (Scripting group).

| Tool | Effect | Risk | Summary |
|---|---|---|---|
| [`getDocumentInfo`](#getdocumentinfo) | Read-only | low | Returns a summary of the active document: file, counts, page bounds, view center and user origin. |
| [`getLayers`](#getlayers) | Read-only | low | Lists the layers with their kind, visibility, scale, elevation, object count and bounds. |
| [`createLayer`](#createlayer) | Edit | low | Creates a design layer or a sheet layer. |
| [`editLayer`](#editlayer) | Edit | low | Changes the properties of a layer: name, visibility, scale, elevation, thickness and more. |
| [`getStories`](#getstories) | Read-only | low | Lists the stories (building floors) with their levels, lowest first. |
| [`createStory`](#createstory) | Edit | low | Creates one or more stories with their levels. |
| [`editStory`](#editstory) | Edit | low | Changes a story, the level types of the document or its default story levels. |
| [`getClasses`](#getclasses) | Read-only | low | Lists the classes of the document and names the special classes. |
| [`createClass`](#createclass) | Edit | low | Creates a class, or returns the existing class of that name. |
| [`editClass`](#editclass) | Edit | low | Changes a class: description, visibility, pen, fill, markers, drop shadow and more. |
| [`setActiveContext`](#setactivecontext) | Edit | low | Sets the active layer and class and how the other layers and classes are shown. |
| [`getUnits`](#getunits) | Read-only | low | Returns the primary and secondary unit settings of the document. |
| [`setUnits`](#setunits) | Edit | low | Changes the primary or secondary unit settings of the document. |
| [`convertUnits`](#convertunits) | Read-only | low | Converts lengths between world units and document units. |
| [`setView`](#setview) | Edit | low | Moves the view, sets the zoom, moves the user origin or redraws the page. |
| [`getPreferences`](#getpreferences) | Read-only | low | Reads one category of document preferences. |
| [`setPreferences`](#setpreferences) | Edit | low | Writes document preferences of one category. |

> **Note:** Several calls of the tools of this group can also be one undo step with [`runToolBatch`](Common.md#runtoolbatch), all or nothing.

### getDocumentInfo

Returns a summary of the active document: file, counts, page bounds, view center and user origin.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Return a summary of the active document: fileName (including extension), filePath (full native path, or null for an unsaved drawing), selection/layer/class counts (selectionCount covers every layer, not only the active one), page bounds, view center, user origin, plan rotation, active layer (with its kind and scale), active class, primary units, the layer/class visibility options, IFC summary (`hasIFCEntities` and `ifcSchema` when IFC support is available), the `container` new objects are created in (active layer, or the group / symbol definition being edited).

Takes no arguments.

> **Note:** `container` is always in the result, and leaves out a member that does not apply. `default` is an [object reference](Common.md#object-references) to the container that new objects go into: the active layer, or the group or symbol definition being edited. `insideGroup` tells whether a group is being edited, and `editedGroup` references that group. `editedSymbolDefinition` references the current symbol of the document (the symbol definition that the Symbol Insertion tool places); Vectorworks keeps it also when no symbol definition is being edited, so read `default` to see where new objects go.

**Parameters**

This tool takes no parameters.

**Result**

| Key | Description |
|---|---|
| `isOpen` | Always `true`. |
| `fileName`, `filePath` | The file name with its extension and the full native path. For an unsaved drawing `fileName` is its name and `filePath` is `null`. |
| `selectionCount`, `layerCount`, `classCount` | The selected objects on all layers, the layers and the classes (the classes of referenced files included). |
| `pageBounds` | The page bounds, a [rectangle](Common.md#rectangles) in world units. |
| `viewCenter`, `userOrigin` | The view center and the user origin, [points](Common.md#points) in world units. |
| `activeLayer`, `activeLayerKind`, `activeLayerScale` | The name, the kind (as `kind` in [`getLayers`](#getlayers)) and the scale (1:scale) of the active layer. |
| `activeClass` | The name of the active class. |
| `primaryUnits`, `unitsPerInch` | The name of the primary units and their units per inch. |
| `planRotated`, `planRotationAngle` | Whether the plan is rotated, and the plan rotation angle. |
| `layerOptions`, `classOptions` | The visibility options of the layers and of the classes: `activeOnly`, `grayOthers`, `showOthers`, `showSnapOthers`, `showSnapModifyOthers` or `graySnapOthers`. |
| `hasIFCEntities`, `ifcSchema` | Only when IFC support is available. |
| `container` | See the note above. |

A value that Vectorworks cannot read is left out of the result.

### getLayers

Lists the layers with their kind, visibility, scale, elevation, object count and bounds.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the layers of the drawing with name, uuid, kind (design, sheet, or guestDesign for a design layer referenced from another file), visibility, scale (1:scale), elevation, thickness, sheet description, DPI, render mode, projection, object count, bounds and whether each is the active layer. The object tools (getObjectInfo, for example) address a layer by its `uuid`: their `name` finds objects only, and layer names are a separate namespace. A design layer in a story also reports `story` (the story name) and `levelType` (its level in the story; a layer can also have a level type without story).

Object count and bounds cover the top level drawing objects of each layer (not the internal entries Vectorworks keeps for deleted objects) and visit every one of them, which is slow on large drawings; narrow the call when you can. `activeOnly` returns only the active layer. `visibleOnly` leaves out invisible layers (grayed layers are kept). `traverse` "allObjects" (default) counts every object; "visibleObjects" counts only the objects Vectorworks currently draws (visible layer and visible class), so an invisible layer then reports objectCount 0 and no bounds.

The response echoes `traverse`, `visibleOnly` and `activeOnly`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `activeOnly` | boolean |  | Return only the active layer. |
| `visibleOnly` | boolean |  | Leave out invisible layers (grayed layers are kept). |
| `traverse` | string |  | One of: `allObjects`, `visibleObjects`. |

**Result**

| Key | Description |
|---|---|
| `layers` | The layers. Each has `name`, `uuid`, `kind`, `active`, `visibility` (`visible`, `grayed` or `invisible`), `scale`, `elevation`, `thickness`, `story` and `levelType` (for a design layer that has them), `description` (for a sheet layer, when it is not empty), `dpi` (for a sheet layer), `renderMode`, `projection`, `objectCount` and `bounds` (only when there is something to bound). |
| `traverse`, `visibleOnly`, `activeOnly` | The values that the call used. |

Errors: `'activeOnly' must be true or false` (likewise `visibleOnly`); `unknown 'traverse'; use allObjects | visibleObjects`.

### createLayer

Creates a design layer or a sheet layer.

> **Effect:** Edit · **Risk:** low · **Undo:** one step "MCP: createLayer" · **In runToolBatch:** yes

**Details**

Create a layer and return it as getLayers lists it. `type` "design" (default) creates a world-coordinate design layer with `scale` (1:scale, default 1), `elevation` and `thickness` (the wall height of the layer), both in world units; "sheet" creates a printable sheet layer, which refuses those arguments and `story`/`levelType`. `story` (a story name) with `levelType` makes the new design layer the layer of that level of the story: a level without layer takes it, a missing level is added at the offset of the first default story level of that type (or 0).

The elevation of a layer in a story follows its level, so `elevation` is refused with `story`; to add a level at a given offset with a new layer, use editStory `addLevels`. `levelType` without `story` gives the layer a level type outside stories. The active layer does not change unless `activate` is true (new objects are created on the active layer).

A refused argument fails the call, which then creates nothing.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | The name of the new layer. When a layer has that name already, Vectorworks gives the new layer the next free name (`<name>-2`, …): read it from `name` in the result. |
| `type` | string |  | One of: `design`, `sheet`. Default: `design`; any other value also creates a design layer. |
| `scale` | number |  | Design layers: 1:scale, default 1. A sheet layer ignores it, but it must still be a positive number. |
| `elevation` | number |  | Elevation, in world units. |
| `thickness` | number |  | The wall height of the layer. |
| `story` | string |  | A story name. |
| `levelType` | string |  | With `story`, the level of that story that the new layer takes. Without `story`, a level type outside stories. 1 to 63 characters. |
| `activate` | boolean |  | Default: `false`. |

**Result**

The new layer as getLayers lists it, with one more key:

| Key | Description |
|---|---|
| `created` | `true`. |

Errors: `'name' is required`; `'scale' must be a positive number (1:scale)`; `'elevation' and 'thickness' must be numbers in world units, 'thickness' not negative`; `'activate' must be true or false`; `'elevation', 'thickness', 'story' and 'levelType' apply to design layers only` (for a sheet layer); `'story' and 'levelType' must be strings`; `story not found: <name>`; `'levelType' must have 1 to 63 characters`; `a layer in a story needs a 'levelType'`; `level '<levelType>' of story '<story>' has the layer '<layer>' already`; `the elevation of a layer in a story follows its level: …` (`elevation` with `story`); `failed to create layer`; `Vectorworks refused the 'thickness' of the new layer` (likewise for `'elevation'` and `'story' / 'levelType'`). A refusal fails the call and the new layer is removed again (`rolledBack`).

### editLayer

Changes the properties of a layer: name, visibility, scale, elevation, thickness and more.

> **Effect:** Edit · **Risk:** low · **Undo:** one step "MCP: editLayer" · **In runToolBatch:** yes

**Details**

Change the properties of the layer named `name` (the active layer when omitted): rename with `newName`, set `visibility` (visible|grayed|invisible), `scale` (design layers, 1:scale), `elevation` and `thickness` in world units, `description` (the sheet title) and `dpi` for sheet layers, or make it active with `activate` (otherwise the active layer does not change).

**Design layers:** `story` (a story name) makes the layer the layer of the level `levelType` (default: its own level type) of that story, and it moves to the level's elevation; `story` "" takes it out of its story (it keeps its elevation and loses its level type unless `levelType` sets one); `levelType` alone moves a layer in a story to that level of its story ("" clears the level type). A level has one layer. The elevation of a layer in a story follows its level, so `elevation` is refused for it: change the level's offset with editStory `setLevels`. The story arguments are applied first; when they are refused the call fails and changes nothing. Returns the updated layer as getLayers lists it, with `applied`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | The active layer when omitted. |
| `newName` | string |  | The new name. |
| `visibility` | string |  | One of: `visible`, `grayed`, `invisible`. Also accepts `normal`, `gray`, `hidden`. |
| `scale` | number |  | Design layers, 1:scale. |
| `elevation` | number |  | Elevation, in world units. |
| `thickness` | number |  | Thickness, in world units. |
| `description` | string |  | The sheet title. |
| `dpi` | integer |  | The resolution of a sheet layer. |
| `story` | string |  | A story name. `""` takes the layer out of its story. |
| `levelType` | string |  | The level of the story that the layer takes (see Details). `""` clears the level type. Otherwise 1 to 63 characters. |
| `activate` | boolean |  | Otherwise the active layer does not change. |

**Result**

The updated layer as getLayers lists it, with one more key:

| Key | Description |
|---|---|
| `applied` | One entry for each property that the call was given: `name` (for `newName`), `visibility`, `scale`, `elevation`, `thickness`, `description`, `dpi`, `story`, `levelType`, and `activate` when it is `true` (`activate` false or omitted adds no entry). A value is `true` when Vectorworks accepted it and `false` when it refused it, for example an unknown `visibility`. |

Errors: `layer not found: <name>`; `'story' and 'levelType' must be strings`; `'story' and 'levelType' apply to design layers only`; `story not found: <name>`; `'levelType' must have 1 to 63 characters`; `a layer in a story needs a 'levelType'`; `level '<levelType>' of story '<story>' has the layer '<layer>' already`; `the elevation of a layer in a story follows its level`; `Vectorworks refused the 'story' / 'levelType' of layer '<name>'`. The story arguments are checked before anything changes, so these errors leave the layer as it was.

### getStories

Lists the stories (building floors) with their levels, lowest first.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the stories of the drawing (the floors of a building), sorted by elevation, lowest first. Each story reports name, uuid, index (its 1-based position in that order), affix (the prefix or suffix of the names of the layers that Vectorworks makes for the story from default story levels), isPrefix (Vectorworks infers it from the level layer names: true when no level has a layer), elevation, storyAbove / storyBelow (names; null at the top / bottom) and levels, sorted by offset: { levelType, offset (relative to the story elevation), elevation (story elevation + offset), layerName (the design layer of the level; null for a level without layer), layerUuid }.

`includeLevelTypes` adds the level types of the document (Organization dialog &gt; Stories &gt; Level Types); `includeDefaultLevels` adds the default story levels { index, levelType, offset, layerName (without the affix), scale, wallHeight }, the templates of story levels. Lengths are world units. Stories are addressed by name in createStory and editStory.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `includeLevelTypes` | boolean |  | Add `levelTypes`, the level types of the document. |
| `includeDefaultLevels` | boolean |  | Add `defaultStoryLevels`, the templates of story levels. |

**Result**

| Key | Description |
|---|---|
| `stories` | The stories, lowest first. Each has `name`, `uuid`, `index`, `affix`, `isPrefix`, `elevation`, `storyAbove`, `storyBelow` (names; `null` at the top and the bottom) and `levels`. |
| `count` | The number of stories. |
| `levelTypes` | Only with `includeLevelTypes`: the names of the level types of the document. |
| `defaultStoryLevels` | Only with `includeDefaultLevels`: the default story levels, each with `index`, `levelType`, `offset`, `layerName`, `scale` and `wallHeight`. |

Each level of a story has `levelType`, `offset`, `elevation` and `layerName`, which is `null` for a level without a layer. A level that has a layer also reports its `layerUuid`. When the story still names a layer that the document no longer has, the level reports that `layerName`, no `layerUuid` and `layerMissing` `true`.

Errors: `'includeLevelTypes' must be true or false` (likewise for `includeDefaultLevels`).

### createStory

Creates one or more stories with their levels.

> **Effect:** Edit · **Risk:** low · **Undo:** one step "MCP: createStory" · **In runToolBatch:** yes

**Details**

Create one story (top-level `name`, `elevation`, optional `affix`, `isPrefix`, `levels`) or several in one call (`stories`: an array of such objects). Elevations and offsets are world units. Each story needs its own elevation and its own affix (compared ignoring case; default: the story name). `levels` adds levels: { levelType, offset (relative to the story elevation), layerName, createLayer, scale }.

`layerName` is the design layer of the level: an existing design layer without level type moves into the story at the level elevation; a missing one is created (unless `createLayer` is false) with `scale` (1:scale; default: the scale of the active layer). Without `layerName` the level has no layer. A level type that the document does not have is added to its level types.

The active layer does not change. Every story and level is checked before anything is created, and a refusal fails the call, which then creates nothing (`rolledBack`). With `reuseExisting` (default false) a story that exists is kept as it is (elevation, affix, levels) and only the levels it lacks are added, so the same call can be repeated. Returns each story as getStories lists it, with `created`, `reused`, `levelsAdded` and `levelsKept`, plus `levelTypesAdded` and `layersCreated`.

The call is one undo step.

> **Note:** Give either the arguments of one story (`name`, `elevation`, `affix`, `isPrefix`, `levels`) or `stories`, not both. The layer of a level must be a design layer that has no level type yet, or a name that no other object uses (the layer is then created, unless `createLayer` is false). One layer cannot go to two levels of the call.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | The story name: 1 to 63 characters, not used by another object. |
| `elevation` | number |  | Elevation, in world units. |
| `affix` | string |  | Compared ignoring case; default: the story name. |
| `isPrefix` | boolean |  | `true` when `affix` is a prefix of the layer names of the story. Default: `false` (a suffix). |
| `levels` | array of object |  | The levels to add to the story. |
| `levels[].levelType` | string | Yes | 1 to 63 characters. A type that the document does not have is added to its level types. |
| `levels[].offset` | number | Yes | Relative to the story elevation, in world units. |
| `levels[].layerName` | string |  | The design layer of the level. Without it the level has no layer. |
| `levels[].createLayer` | boolean |  | Create the layer when the document has none of that name. Default: `true`. |
| `levels[].scale` | number |  | The scale of a created layer (1:scale). Default (or `0`): the scale of the active layer. |
| `stories` | array of object |  | Several stories, each with the arguments of one story. |
| `stories[].name` | string | Yes | The story name: 1 to 63 characters, not used by another object. |
| `stories[].elevation` | number | Yes | Elevation, in world units. |
| `stories[].affix` | string |  | Compared ignoring case; default: the story name. |
| `stories[].isPrefix` | boolean |  | `true` when `affix` is a prefix of the layer names of the story. Default: `false` (a suffix). |
| `stories[].levels` | array of object |  | The levels to add to the story. |
| `stories[].levels[].levelType` | string | Yes | 1 to 63 characters. A type that the document does not have is added to its level types. |
| `stories[].levels[].offset` | number | Yes | Relative to the story elevation, in world units. |
| `stories[].levels[].layerName` | string |  | The design layer of the level. Without it the level has no layer. |
| `stories[].levels[].createLayer` | boolean |  | Create the layer when the document has none of that name. Default: `true`. |
| `stories[].levels[].scale` | number |  | The scale of a created layer (1:scale). Default (or `0`): the scale of the active layer. |
| `reuseExisting` | boolean |  | Default: `false`. |

**Result**

| Key | Description |
|---|---|
| `stories` | One entry for each story of the call, as getStories lists it, with `created` and `reused` (booleans), `levelsAdded` (the level types that the call added to the story) and `levelsKept` (the level types of the call that a reused story had already). |
| `createdCount`, `reusedCount` | How many stories the call created and how many it kept with `reuseExisting`. |
| `levelTypesAdded` | The level types that the call added to the document. |
| `layersCreated` | The names of the layers that the call created. |

Errors: `give either one story ('name', 'elevation', ...) or a 'stories' array`; `'stories' must be a non-empty array of stories`; `'reuseExisting' must be true or false`; `each story needs a 'name' of 1 to 63 characters`; `story '<name>': 'elevation' must be a number (world units)`; `story '<name>': 'affix' must be a string and 'isPrefix' true or false`; `story '<name>' is given twice`; `story '<name>' exists already; set 'reuseExisting' to keep it and add the levels it lacks`; `story '<name>': the name is used by another object`; `story '<name>': the story '<other>' has that elevation already` and the same for the affix; for a level, `each level needs a 'levelType' of 1 to 63 characters`, `story '<name>' level '<type>': 'offset' must be a number (world units, relative to the story elevation)`, `...: 'layerName' must be a string and 'createLayer' true or false`, `...: 'scale' must be a positive number (1:scale)`, `story '<name>': 'levels' must be an array of levels`, `the level type '<type>' is given twice`, and the refusals of its layer (`is not a design layer`, `is the layer of the level '<type>' already`, `is the name of another object`, `does not exist and 'createLayer' is false`, `is given to another level, or deleted, in the same call`); `Vectorworks refused to create the story` or `Vectorworks refused the level '<type>'`. Every story and level is checked first, and a refusal fails the call, which creates nothing (`rolledBack`).

### editStory

Changes a story, the level types of the document or its default story levels.

> **Effect:** Edit · **Risk:** low · **Undo:** one step "MCP: editStory" · **In runToolBatch:** yes

**Details**

Change the story `name`, the level types of the document or its default story levels. All changes of a call are checked before anything changes and are one undo step; a refusal fails the whole call, which then changes nothing (`rolledBack`). Lengths are world units. Story changes, applied in this order: `affix`; `elevation` with `mode` single (default: only this story), currentAndAbove, currentAndBelow or all (the moved stories all move by the same distance, and two stories cannot share an elevation) - the design layers of the moved stories, and the objects bound to their levels, move with them; `removeLevels` [{ levelType, deleteLayer }] (the level's layer stays as a design layer without story and level type, unless `deleteLayer` deletes it, which is refused for a layer that holds objects); `setLevels` [{ levelType, offset }] moves levels with their layers; `addLevels` like the `levels` of createStory; and, after the other changes of the call, `newName` (also renamed in the IFC data).

`delete` true deletes the story, in a call of its own: its design layers stay, with their objects, as layers without story and level type, unless `deleteLayers` deletes them, which is refused unless all of them are empty. Without `name`: `levelTypes` { add: [names], rename: [{ from, to }], delete: [names] } - a level type of a story level cannot be deleted (layers and default story levels lose a deleted one), and Undo does not restore a renamed level type in the bounds of walls (rename it back instead); `defaultStoryLevels` { reset: replace|append (the Vectorworks defaults), delete: [index] (as getStories `includeDefaultLevels` reports them), add: [{ levelType, offset, layerName, scale, wallHeight }] (added at the start of the list, in the given order) }.

Returns the story as getStories lists it with `applied`, `levelTypesAdded`, `layersCreated`, and `levelTypes` / `defaultStoryLevels` when they were changed.

> **Note:** Without `name` the call changes only the level types and the default story levels. The changes are applied in this order: `levelTypes.add`; the story changes (or `delete`); `defaultStoryLevels`; `levelTypes.delete`; `newName`; last `levelTypes.rename`. `mode` needs `elevation`. `defaultStoryLevels` takes `reset` or `delete`, not both: `replace` deletes the existing default story levels before it restores the Vectorworks defaults, `append` keeps them. An item of `removeLevels` can also be a plain level type string. A deletion of layers (`deleteLayers`, `removeLevels[].deleteLayer`) is also refused when it would delete all design layers of the document.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | The story to change. Leave it out to change only `levelTypes` and `defaultStoryLevels`. |
| `newName` | string |  | Also renamed in the IFC data. 1 to 63 characters, not the name of another object. |
| `affix` | string |  | The new affix of the story. |
| `elevation` | number |  | Elevation, in world units. Two stories cannot share an elevation. |
| `mode` | string |  | One of: `single`, `currentAndAbove`, `currentAndBelow`, `all`. Default: `single`. Needs `elevation`. |
| `removeLevels` | array of object |  | The levels to remove from the story. |
| `removeLevels[].levelType` | string | Yes | The level type of a level of the story. |
| `removeLevels[].deleteLayer` | boolean |  | Delete the layer of the level too. Refused for a layer that holds objects. Default: the layer stays. |
| `setLevels` | array of object |  | The levels to move, with their layers. |
| `setLevels[].levelType` | string | Yes | The level type of a level of the story. |
| `setLevels[].offset` | number | Yes | The new offset, relative to the story elevation, in world units. |
| `addLevels` | array of object |  | The levels to add, as the `levels` of createStory. |
| `addLevels[].levelType` | string | Yes | 1 to 63 characters. The story must not have the level yet (move it with `setLevels`). |
| `addLevels[].offset` | number | Yes | Relative to the story elevation, in world units. |
| `addLevels[].layerName` | string |  | The design layer of the level. Without it the level has no layer. |
| `addLevels[].createLayer` | boolean |  | Create the layer when the document has none of that name. Default: `true`. |
| `addLevels[].scale` | number |  | The scale of a created layer (1:scale). Default (or `0`): the scale of the active layer. |
| `delete` | boolean |  | `true` deletes the story. |
| `deleteLayers` | boolean |  | With `delete`: delete the design layers of the story too. Refused unless all of them are empty. |
| `levelTypes` | object |  | Changes of the level types of the document: `add`, `rename`, `delete`. |
| `levelTypes.add` | array of string |  | The names of the level types to add: 1 to 63 characters each. |
| `levelTypes.rename` | array of object |  | The level types to rename. |
| `levelTypes.rename[].from` | string | Yes | The current name. |
| `levelTypes.rename[].to` | string | Yes | The new name: 1 to 63 characters. |
| `levelTypes.delete` | array of string |  | The names of the level types to delete. A level type of a story level cannot be deleted. |
| `defaultStoryLevels` | object |  | Changes of the default story levels: `reset` or `delete`, and `add`. |
| `defaultStoryLevels.reset` | string |  | One of: `replace`, `append`. |
| `defaultStoryLevels.delete` | array of integer |  | The indexes of the default story levels to delete, as getStories `includeDefaultLevels` reports them. |
| `defaultStoryLevels.add` | array of object |  | The default story levels to add, at the start of the list, in the given order. |
| `defaultStoryLevels.add[].levelType` | string | Yes | The level type. |
| `defaultStoryLevels.add[].offset` | number | Yes | Relative to the story elevation, in world units. |
| `defaultStoryLevels.add[].layerName` | string |  | The layer name of the level. |
| `defaultStoryLevels.add[].scale` | number |  | The scale of the layer (1:scale). Default: `0` (the scale of the active layer); not negative. |
| `defaultStoryLevels.add[].wallHeight` | number |  | The wall height of the level, in world units. Default: `0`; not negative. |

**Result**

| Key | Description |
|---|---|
| `story` | The story as getStories lists it, after the changes. Only when the call changed a story. |
| `applied` | Only with `story`. One entry for each change of the story that the call was given: `affix`, `elevation` and `newName` are `true`; `removeLevels`, `setLevels` and `addLevels` are the arrays of the level types that the call removed, moved or added. |
| `levelTypesAdded` | The names of the level types that the call added to the document (an empty array when none). |
| `layersCreated` | The names of the layers that the call created (an empty array when none). |
| `levelTypes` | Only when the call has `levelTypes`: the names of all level types of the document after the changes. |
| `defaultStoryLevels` | Only when the call has `defaultStoryLevels`: the default story levels after the changes, as getStories `includeDefaultLevels` lists them. |
| `deleted` | Only with `delete`: `true`. There is then no `story` and no `applied`. |
| `layersDeleted`, `layersKept` | Only with `delete`: the names of the design layers of the story, deleted with `deleteLayers` or kept (as layers without story and level type). |

Errors: `nothing to change: give changes of the story 'name', 'levelTypes' or 'defaultStoryLevels'`; `'delete' deletes the story in a call of its own: leave out the other changes`; `'name' (the story to change) is required for 'newName', 'affix', 'elevation', the level changes and 'delete'`; `story not found: <name>`; `story '<name>': 'elevation' must be a number (world units), and 'mode' (single, currentAndAbove, currentAndBelow or all) goes with it`; `story '<name>': 'delete' and 'deleteLayers' are true or false, and 'deleteLayers' goes with 'delete'`; `'defaultStoryLevels' takes 'reset' or 'delete', not both`; `each item of 'defaultStoryLevels.add' is { levelType, offset, layerName, scale, wallHeight }: lengths in world units, 'scale' and 'wallHeight' not negative`; `story '<name>': 'newName' must have 1 to 63 characters and must not be the name of another object`; `story '<name>': another story has the affix '<affix>' (affixes are compared ignoring case)`; `story '<name>': its layer '<layer>' holds <n> objects, and only empty layers are deleted; leave out 'deleteLayers' to keep the layers`; `story '<name>': its layers are all the design layers of the document, and Vectorworks keeps at least one`; `story '<name>': the 'elevation' would move a story onto the elevation of a story that does not move ('mode'); two stories cannot share an elevation`; `story '<name>' has no level '<type>' to remove, or it is removed twice`; `story '<name>' level '<type>': its layer '<layer>' holds <n> objects, and only an empty layer is deleted; leave out 'deleteLayer' to keep the layer`; `story '<name>' level '<type>': deleting its layer would delete the last design layer of the document`; `story '<name>' has no level '<type>' to move, or 'removeLevels' removes it, or it is moved twice`; `story '<name>' has the level '<type>' already (move it with 'setLevels')`; `the level type '<type>' exists already, or is given twice`; `the level type '<from>' cannot be renamed to '<to>': it must exist, the new name must not (a change of the letter case only is not possible), and each is changed once`; `the level type '<from>' is renamed in a call of its own: other changes of this call use it`; `the level type '<name>' cannot be deleted: it must exist and not be used by the other changes of the call`; `the level type '<name>' is a level of the story '<story>': remove the level first ('removeLevels')`; `'defaultStoryLevels.delete': there is no default story level <index>, or it is given twice`; and the refusals of Vectorworks, such as `Vectorworks refused to remove the level '<type>'`, `Vectorworks refused to delete the level type '<name>'`. Every change is checked first and a refusal fails the call, which changes nothing (`rolledBack`).

### getClasses

Lists the classes of the document and names the special classes.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the classes of the document (the named attribute sets objects inherit from) with name, index and visibility, plus `specialClasses`: the names of the `none` class, the built-in `dimension` class and the `default` class of the current container (normally the active class); createClass `guides` returns the Guides class. Set `detailed` to also return description, non-plot/use-at-creation flags, pen (RGB colors and color table indices, lineWeightMils, opacity, raw style, styleKind, lineType), fill (RGB colors and color table indices, type, raw style, resource, opacity), markers, drop shadow, textures (`texture`, `wallTextures` right/left/center, `roofTextures` top/edge/dormer) and text style of each class.

Set `includeGuestClasses` to include classes referenced from other documents.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `includeGuestClasses` | boolean |  | Include the guest classes: classes that are referenced from other documents. |
| `detailed` | boolean |  | Add the attributes of each class (see Result). |

**Result**

| Key | Description |
|---|---|
| `classes` | The classes of the document. Each has `name`, `index` and `visibility`, and with `detailed` the keys below. |
| `classOptions` | How the classes other than the active class are shown: one of the `classOptions` names of setActiveContext. Left out when it cannot be read. |
| `specialClasses` | The names of the special classes: `none`, `dimension` and `default`. |

With `detailed`, each class also has: `description` (only when it is not empty), `nonPlot`, `useAtCreation`, `pen` (`foreColor`, `backColor`, `foreColorIndex`, `backColorIndex`, `lineWeightMils`, `opacity`, `style`, `styleKind`, `lineType`), `fill` (`foreColor`, `backColor`, `foreColorIndex`, `backColorIndex`, `type`, `style`, `resource`, `opacity`), `beginningMarker`, `endMarker` (as [Attributes](Attributes.md#line-end-markers) describes them; the markers of a class always report `visible` `true`), `dropShadow` ([drop shadow](Attributes.md#drop-shadow)), `useTextures`, `texture`, `wallTextures` (`right`, `left`, `center`), `roofTextures` (`top`, `edge`, `dormer`), `useTextStyle` and `textStyle`. Texture values are render texture indices (0 = none). `textStyle` is the internal index of a text style resource (0 = none). A value that cannot be read is left out.

### createClass

Creates a class, or returns the existing class of that name.

> **Effect:** Edit · **Risk:** low · **Undo:** one step "MCP: createClass" · **In runToolBatch:** yes

**Details**

Create a class, returning the existing one when the name is taken. Set `guides` instead of `name` to get the Guides class (the class of guide objects, created when missing). Optional `description`; set `activate` to make it the active class so new objects are created in it. Returns the class name and index.

> **Note:** `name` is not used when `guides` is `true`. `description` and `activate` also apply to a class that exists already.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | The class name. Required unless `guides` is `true`. |
| `guides` | boolean |  | `true`: return the Guides class instead of the class `name`. |
| `description` | string |  | Description text. |
| `activate` | boolean |  | Make the class the active class. |

**Result**

| Key | Description |
|---|---|
| `created` | Always `true`, also when the class existed already. Use getClasses first to find out whether it exists. |
| `name` | The name of the class. |
| `index` | The internal index of the class. Left out when it cannot be read. |

Errors: `'name' is required (or set 'guides')`; `failed to create class`.

### editClass

Changes a class: description, visibility, pen, fill, markers, drop shadow and more.

> **Effect:** Edit · **Risk:** low · **Undo:** one step "MCP: editClass" · **In runToolBatch:** yes

**Details**

Change the class named `name` (the active class when omitted). Set `description`, `visibility` (visible|grayed|invisible), `nonPlot`, `useAtCreation`, the class `pen` (foreColor, backColor, foreColorIndex, backColorIndex, lineWeightMils, opacity, style, lineType), `fill` (foreColor, backColor, foreColorIndex, backColorIndex, opacity, style, resource), combined `opacity`, `beginningMarker`/`endMarker`, `dropShadow`, `useTextures`/`texture`, `wallTextures` (right, left, center), `roofTextures` (top, edge, dormer), `useTextStyle`/`textStyle`, or `activate` it.

Color indices are document color table indices; an index equal to the class's current one is ignored, so a class read with getClasses can be sent back with the RGB color edited, and when both forms change the index wins. Texture parts are render texture indices (0 = none); partial marker, drop shadow and texture part objects keep the members left out.

`action` "delete" removes the class and moves its objects to None. Objects whose attributes are set "by class" follow these values.

> **Note:** A class has no `visible` flag for its markers: it always reports them `visible` `true`, and a `visible` member of `beginningMarker` or `endMarker` is ignored. `textStyle` is the internal index of a text style resource (0 = none), not a name.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | The active class when omitted. |
| `action` | string |  | One of: `modify`, `delete`. |
| `description` | string |  | Description text. |
| `visibility` | string |  | One of: `visible`, `grayed`, `invisible`. |
| `nonPlot` | boolean |  | Do not plot the objects of the class. |
| `useAtCreation` | boolean |  | Objects that are created in the class take its attributes at creation. |
| `pen` | object |  | Pen attributes; only the members given are changed. |
| `pen.foreColor` | [color](Common.md#colors) |  | Foreground color (RGB). |
| `pen.backColor` | [color](Common.md#colors) |  | Background color (RGB). |
| `pen.foreColorIndex` | integer |  | Foreground color as an index into the document color table. |
| `pen.backColorIndex` | integer |  | Background color as an index into the document color table. |
| `pen.lineWeightMils` | integer |  | Line weight in mils. |
| `pen.opacity` | integer |  | Opacity, 0-100. |
| `pen.style` | integer |  | Raw pen style. |
| `pen.lineType` | integer |  | Internal index of a line type. |
| `fill` | object |  | Fill attributes; only the members given are changed. |
| `fill.foreColor` | [color](Common.md#colors) |  | Foreground color (RGB). |
| `fill.backColor` | [color](Common.md#colors) |  | Background color (RGB). |
| `fill.foreColorIndex` | integer |  | Foreground color as an index into the document color table. |
| `fill.backColorIndex` | integer |  | Background color as an index into the document color table. |
| `fill.opacity` | integer |  | Opacity, 0-100. |
| `fill.style` | integer |  | Raw fill style. |
| `fill.resource` | integer |  | Internal index of a hatch, tile, gradient or image. |
| `opacity` | integer |  | Opacity, 0-100. |
| `beginningMarker` | [marker](Attributes.md#line-end-markers) |  | The beginning marker of the class. The members left out keep their value. |
| `endMarker` | [marker](Attributes.md#line-end-markers) |  | The end marker of the class. The members left out keep their value. |
| `dropShadow` | [drop shadow](Attributes.md#drop-shadow) |  | The drop shadow of the class. The members left out keep their value. |
| `useTextures` | boolean |  | Use the textures of the class. |
| `texture` | integer |  | Render texture index; 0 = none. |
| `wallTextures` | object |  | Members: `right`, `left`, `center`. |
| `wallTextures.right` | integer |  | Render texture index of the right side of walls; 0 = none. |
| `wallTextures.left` | integer |  | Render texture index of the left side of walls; 0 = none. |
| `wallTextures.center` | integer |  | Render texture index of the center of walls; 0 = none. |
| `roofTextures` | object |  | Members: `top`, `edge`, `dormer`. |
| `roofTextures.top` | integer |  | Render texture index of the top of roofs; 0 = none. |
| `roofTextures.edge` | integer |  | Render texture index of the edge of roofs; 0 = none. |
| `roofTextures.dormer` | integer |  | Render texture index of the dormers of roofs; 0 = none. |
| `useTextStyle` | boolean |  | Use the text style of the class. |
| `textStyle` | integer |  | Internal index of a text style resource, as getClasses reports it with `detailed`; 0 for none. |
| `activate` | boolean |  | Make the class the active class. |

**Result**

With `action` `delete` the result is `deleted`: `true` when the class was deleted.

Otherwise it is the class as getClasses lists it with `detailed`, with one more key:

| Key | Description |
|---|---|
| `applied` | One entry for each setting that the call was given. A value is `true` when Vectorworks accepted the setting. The keys are `description`, `visibility`, `nonPlot`, `useAtCreation`, `opacity`, `useTextures`, `texture`, `wallTextures`, `roofTextures` (`false` when the value is not an object), `useTextStyle`, `textStyle`, `beginningMarker`, `endMarker`, `dropShadow`, `activate` (listed only when it is `true`), and, for the pen and the fill, `penForeColor`, `penBackColor`, `lineWeightMils`, `penOpacity`, `penStyle`, `penLineType`, `penColorIndices`, `fillForeColor`, `fillBackColor`, `fillOpacity`, `fillStyle`, `fillResource` and `fillColorIndices`. |

Errors: `class not found: <name>` (also when `name` is omitted and the active class is not valid).

### setActiveContext

Sets the active layer and class and how the other layers and classes are shown.

> **Effect:** Edit · **Risk:** low · **Undo:** one step "MCP: setActiveContext" · **In runToolBatch:** yes

**Details**

Set what new objects inherit and what the user can work on: the active `layer` and/or `class` by name, how non-active layers and classes are shown with `layerOptions`/`classOptions` (activeOnly, grayOthers, showOthers, showSnapOthers, showSnapModifyOthers, graySnapOthers), and the symbol definition to edit with `symbolDefinition`.

> **Note:** `symbolDefinition` sets the current symbol definition; it does not open the definition for editing. A name that is not a symbol definition does not fail the call: `symbolDefinitionActivated` is `false`. The arguments are checked in the order `layer`, `class`, `layerOptions`, `classOptions`, `symbolDefinition`; only strings count.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `layer` | string |  | The name of the layer to make active. |
| `class` | string |  | The name of the class to make active. |
| `layerOptions` | string |  | One of: `activeOnly`, `grayOthers`, `showOthers`, `showSnapOthers`, `showSnapModifyOthers`, `graySnapOthers`. |
| `classOptions` | string |  | One of: `activeOnly`, `grayOthers`, `showOthers`, `showSnapOthers`, `showSnapModifyOthers`, `graySnapOthers`. |
| `symbolDefinition` | string |  | The name of the symbol definition to make the current symbol definition. |

**Result**

One key for each argument that the call was given:

| Key | Description |
|---|---|
| `layerActivated` | `true` when the layer is now active. |
| `classActivated` | `true` when the class is now active. |
| `layerOptions` | `true` when Vectorworks accepted the option; `false` for an unknown option name. |
| `classOptions` | `true` when Vectorworks accepted the option; `false` for an unknown option name. |
| `symbolDefinitionActivated` | `true` when the symbol definition is now the current one; `false` when the name is not a symbol definition. |

Errors: `layer not found: <name>`; `class not found: <name>`; `symbol definition not found: <name>`; `provide 'layer', 'class', 'layerOptions', 'classOptions' and/or 'symbolDefinition'`. An error fails the call, and Vectorworks reverts the changes that the call made before it (`rolledBack`).

### getUnits

Returns the primary and secondary unit settings of the document.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Return the full primary and secondary unit settings of the document: name, mark, units per inch, metric flag, display/dimension precision, fraction and separator options, angular unit, and (primary only) the area and volume units and the document angular settings. Takes no arguments.

**Parameters**

This tool takes no parameters.

**Result**

| Key | Description |
|---|---|
| `primary` | The primary unit settings. |
| `secondary` | The secondary unit settings. |

Both have the keys `name`, `mark`, `unitsPerInch`, `style`, `metric`, `showUnitMark`, `leadingZero`, `trailingZeros`, `displayAsFraction`, `showThousandsSeparator`, `decimalDisplayPrecision`, `decimalDimensionPrecision`, `fractionalDisplayPrecision`, `fractionalDimensionPrecision` and `angularUnit` (`degrees`, `radians` or `gradians`). The primary units also have `worldUnitsPerUnit`, `squareUnitDivision`, `squareUnitMark`, `areaUnitName`, `areaUnitMark`, `areaUnitsPerSquareInch`, `areaDecimalPrecision`, `volumeUnitName`, `volumeUnitMark`, `volumeUnitsPerCubicInch`, `volumeDecimalPrecision`, `documentAngularUnit` and `documentAngularPrecision`. A value that cannot be read is left out.

### setUnits

Changes the primary or secondary unit settings of the document.

> **Effect:** Edit · **Risk:** low · **Undo:** one step "MCP: setUnits" · **In runToolBatch:** yes

**Details**

Change the document units. `which` selects "primary" (default) or "secondary". Set any of `name`, `mark`, `unitsPerInch`, `style`, `metric`, `showUnitMark`, `leadingZero`, `trailingZeros`, `displayAsFraction`, `showThousandsSeparator`, the decimal/fractional display and dimension precisions, `angularUnit` (degrees|radians|gradians) and - for the primary units - the square/area/volume unit names, marks, factors and precisions plus `documentAngularUnit` and `documentAngularPrecision`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `which` | string |  | One of: `primary`, `secondary`. Default: `primary`. |
| `name` | string |  | The name of the unit. |
| `mark` | string |  | The unit mark, shown after a value. |
| `unitsPerInch` | number |  | How many of the unit make one inch. |
| `style` | integer |  | The style code of the unit, as getUnits reports it. |
| `metric` | boolean |  | `true` for a metric unit. |
| `showUnitMark` | boolean |  | Show the unit mark after a value. |
| `leadingZero` | boolean |  | Show a leading zero for a value below 1. |
| `trailingZeros` | boolean |  | Show trailing zeros. |
| `displayAsFraction` | boolean |  | Show values as fractions. |
| `showThousandsSeparator` | boolean |  | Show the thousands separator. |
| `decimalDisplayPrecision` | integer |  | Decimal places of a displayed value. |
| `decimalDimensionPrecision` | integer |  | Decimal places of a dimension value. |
| `fractionalDisplayPrecision` | integer |  | Fraction precision of a displayed value. |
| `fractionalDimensionPrecision` | integer |  | Fraction precision of a dimension value. |
| `angularUnit` | string |  | One of: `degrees`, `radians`, `gradians`. |
| `squareUnitDivision` | integer |  | Primary units only. The square unit division. |
| `squareUnitMark` | string |  | Primary units only. The mark of the square unit. |
| `areaUnitName` | string |  | Primary units only. The name of the area unit. |
| `areaUnitMark` | string |  | Primary units only. The mark of the area unit. |
| `areaUnitsPerSquareInch` | number |  | Primary units only. How many area units make one square inch. |
| `areaDecimalPrecision` | integer |  | Primary units only. Decimal places of an area. |
| `volumeUnitName` | string |  | Primary units only. The name of the volume unit. |
| `volumeUnitMark` | string |  | Primary units only. The mark of the volume unit. |
| `volumeUnitsPerCubicInch` | number |  | Primary units only. How many volume units make one cubic inch. |
| `volumeDecimalPrecision` | integer |  | Primary units only. Decimal places of a volume. |
| `documentAngularUnit` | string |  | Primary units only. One of: `degrees`, `radians`, `gradians`. |
| `documentAngularPrecision` | integer |  | Primary units only. Decimal places of an angle. |

**Result**

| Key | Description |
|---|---|
| `applied` | One entry for each setting that the call was given. A value is `true` when Vectorworks accepted the setting; an unknown `angularUnit` or `documentAngularUnit` name gives `false`. |
| `units` | The unit settings after the changes, as getUnits lists them. |

Error: `provide at least one unit setting to change`.

### convertUnits

Converts lengths between world units and document units.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Convert lengths between the world units used by every tool of this API and the document units shown in the Vectorworks UI. `worldLength` is returned as `inDocumentUnits`, `unitsLength` as `inWorldUnits`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `worldLength` | number |  | A length in world units. |
| `unitsLength` | number |  | A length in document units. |

**Result**

| Key | Description |
|---|---|
| `inDocumentUnits` | Only with `worldLength`: that length in document units. |
| `inWorldUnits` | Only with `unitsLength`: that length in world units. |
| `documentUnits` | The name of the primary document unit. |

A conversion that fails leaves its key out. Error: `provide 'worldLength' and/or 'unitsLength'`.

### setView

Moves the view, sets the zoom, moves the user origin or redraws the page.

> **Effect:** Edit · **Risk:** low · **Undo:** one step "MCP: setView" · **In runToolBatch:** yes

**Details**

Change what is shown and where the drawing origin is: `center` moves the view to a world point, `zoom` sets the zoom factor (1.0 = 100%), `userOrigin` moves the world point the user sees as (0,0), and `redraw` forces a redraw of the page area.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `center` | [point](Common.md#points) |  | Center point. |
| `zoom` | number |  | The zoom factor; 1.0 = 100%. A value of 0 or less is refused (`zoomSet` is `false`). |
| `userOrigin` | [point](Common.md#points) |  | The world point that the user sees as (0,0). |
| `redraw` | boolean |  | `true` forces a redraw of the page area. |

**Result**

| Key | Description |
|---|---|
| `centerSet` | Only with `center`: `true` when the view was moved. |
| `zoomSet` | Only with `zoom`: `true` when the zoom was set. |
| `userOriginSet` | Only with `userOrigin`: always `true`. Vectorworks does not move the user origin while a container that disables it is being edited; read it back with getDocumentInfo. |
| `redrawn` | Only with `redraw` `true`: `true` when the page area was redrawn. |

A `center` or `userOrigin` that is not a point, and a `zoom` that is not a number, are skipped without an error and have no key in the result. Error: `provide 'center', 'zoom', 'userOrigin' and/or 'redraw'` when the call sets nothing.

### getPreferences

Reads one category of document preferences.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the document preferences of one `category`: display (rendering and on-screen display), editing (session, dimensions, undo, autosave), snapping (SmartCursor), grid, stackLayers, text (defaults for new text) or defaultAttributes (pen/fill colors as RGB and color table index, styles, line weight, fill resources, opacity, markers, the by-class flags, the document drop shadow and the classes used for new objects and dimensions).

Omit `category` to read them all. With category "variable" it reads a raw program variable given by `selector` and `type` (bool|uint8|int8|int16|int32|double|string).

> **Note:** Without `category` the result holds the seven named categories; `variable` is read only on request.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `category` | string |  | One of: `display`, `editing`, `snapping`, `grid`, `stackLayers`, `text`, `defaultAttributes`, `variable`. Omit it to read the seven named categories. |
| `selector` | integer |  | With `variable`: the selector of the program variable. |
| `type` | string |  | One of: `bool`, `uint8`, `int8`, `int16`, `int32`, `double`, `string`. With `variable`: the type of the program variable. Default: `bool`. |

**Result**

| Key | Description |
|---|---|
| `display`, `editing`, `snapping`, `grid`, `stackLayers`, `text`, `defaultAttributes` | One object for each category that was read: the category given, or all seven when `category` is omitted. |
| `selector`, `value` | With `category` `variable`, instead of the categories above: the selector and the value of the program variable. |

A setting that cannot be read is left out. Errors: `unknown 'category' (display, editing, snapping, grid, stackLayers, text, defaultAttributes, variable)`; `unknown variable 'type': <type>`; `program variable not available`.

**Settings of each category**

setPreferences writes the same settings under the same names.

| Category | Settings |
|---|---|
| `display` | Booleans: `blackAndWhiteOnly`, `useLayerColors`, `zoomLineThickness`, `blackBackground`, `showRulers`, `showScrollBars`, `showPageBoundary`, `showPageBreaks`, `showOthersInGroup`, `showOthersInGroupGrayed`, `eightSelectionHandles`, `fullScreenCursor`, `noFillBehindText`, `adjustFlippedText`, `xRayMode`, `displayHiddenObjectsGhosted`, `showInternalOriginMarker`, `allowDropShadows`, `perspectiveCropped`. Whole numbers: `conversionResolution2D`, `conversionResolution3D`, `displayLightObjects`, `rotatedTextDisplay`, `displayBitmaps`, `hiddenLineShade`, `display3DLoci`, `defaultRenderMode`, `defaultProjection`, `rotationResponse3D`. |
| `editing` | Booleans: `clickDrag`, `offsetDuplicates`, `associateDimensions`, `autoAssociateDimensions`, `createDimensionsInDimensionClass`, `wallAutoJoin`, `undoViewChanges`, `duplicateTagsWithObjects`, `occludedPickingAndSnapping`. Whole numbers: `maxUndos`, `autoSaveInterval`, `backupInterval`, `lineWeightUnit`, `dimensionStandard`. Number: `customMoveDistance`. |
| `snapping` | Booleans: `snapToGrid`, `snapToObjects`, `snapToLoci`, `snapToEdgePoints`, `snapToSelectionOnly`, `snapToAngle`, `snapToIntersection`, `smartPoints`, `snapToDistance`, `smartEdge`, `constrainTangent`, `snapToEndPoint`, `snapToMidPoint`, `snapToCenter`, `snapToQuadrant`, `snapToInsertionPoint`, `snapToVertex`, `snapToEdge`, `snapToMasterPoints`, `snapToRelativeAngles`, `snapToAlternateCoordinateSystem`, `snapToAnglesFromAxes` (read-only), `snapToCombinedPageArea`, `snapToIndividualPages`, `floatingDatum`, `showSnapBox`, `showSelectionBox`, `useEdgeOffset`, `useProportionalDivision`, `useMultipleDivisions`. Whole number: `snapRadiusPixels`. Numbers: `snapBoxRadius`, `selectionRadius`, `relativeAngle`, `alternateCoordinateSystemAngle`, `edgeOffsetDistance`, `proportionalPercent`, `divisionDistance`. String: `snapAngles`. |
| `grid` | Booleans: `showGrid`, `printGrid`, `snapToGrid`. Numbers: `snapGridX`, `snapGridY`, `referenceGridX`, `referenceGridY`, `sheetLayerSnapGridX`, `sheetLayerSnapGridY`, `angle`, `angleY`. |
| `stackLayers` | Booleans: `enabled`, `create2DObjects`, `ignoreOtherScales`, `restoreViews`, `centerView`, `showPageBoundary`, `onlyActiveLayer2DObjects`, `onlyStoryLayers`. |
| `text` | `fontName` (string), `size` (number, in world units), `leading` (number), `style` (object of the booleans `bold`, `italic`, `underline`, `outline`, `shadow`), `justification` (`left`, `center` or `right`), `verticalAlignment` (`topOfBox`, `topBaseline`, `centerOfBox`, `bottomBaseline` or `bottomOfBox`), `lineSpacing` (`single`, `oneAndHalf`, `double` or `custom`). |
| `defaultAttributes` | The colors as RGB (`penForeColor`, `penBackColor`, `fillForeColor`, `fillBackColor`) and as color table indices (`penForeColorIndex`, `penBackColorIndex`, `fillForeColorIndex`, `fillBackColorIndex`); `penStyle`, `lineWeightMils`, `fillStyle`, `fillType` (read-only), `hatch`, `gradient`, `imageFill`, `tile`, `penOpacity`, `fillOpacity`; the by-class flags `penColorsByClass`, `fillColorsByClass`, `penStyleByClass`, `lineWeightByClass`, `fillStyleByClass`, `penOpacityByClass`, `fillOpacityByClass`, `markersByClass`; `beginningMarker` and `endMarker` ([markers](Attributes.md#line-end-markers)); `documentDropShadow` (read-only, [drop shadow](Attributes.md#drop-shadow)); `class` and `dimensionClass` (class names). |

### setPreferences

Writes document preferences of one category.

> **Effect:** Edit · **Risk:** low · **Undo:** one step "MCP: setPreferences" · **In runToolBatch:** yes

**Details**

Write document preferences. `category` picks the group (display, editing, snapping, grid, stackLayers, text, defaultAttributes) and `values` is an object of the setting names returned by getPreferences; only the members present are written and the result reports which succeeded.

**Read-only:** snapToAnglesFromAxes, fillType and documentDropShadow. In defaultAttributes the colors take RGB (penForeColor, ...) or color table indices (penForeColorIndex, ...); an index equal to the current one is ignored, so the values read with getPreferences can be sent back with an RGB color edited, and when both forms change the index wins. beginningMarker/endMarker take partial marker objects, and the by-class flags other than penOpacityByClass/fillOpacityByClass can only be switched on (writing an explicit value switches one off). With category "variable" it writes the raw program variable `selector` of `type` to `value`.

> **Note:** The settings come from `values`. When `values` is not an object, the call reads them from its top-level arguments. A setting name that the category does not have is ignored without an error, and a value of the wrong JSON type is written as `false`, 0 or an empty string without an error. In `defaultAttributes`, a by-class flag (`penColorsByClass`, `fillColorsByClass`, `penStyleByClass`, `lineWeightByClass`, `fillStyleByClass`, `markersByClass`) is written, and reported in `applied`, only with the value `true`: an explicit `false` is ignored. `penOpacityByClass` and `fillOpacityByClass` take `true` or `false`. With `variable` and `type` `bool`, a `value` that is not a boolean is written as `false`. In `text`, an unknown `justification`, `verticalAlignment` or `lineSpacing` name is written as `left`, `topOfBox` or `custom`, and a `style` that is not an object is ignored.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | One of: `display`, `editing`, `snapping`, `grid`, `stackLayers`, `text`, `defaultAttributes`, `variable`. |
| `values` | object |  | The settings to write, by the names that getPreferences lists for the category. Only the members present are written. |
| `selector` | integer |  | With `variable`: the selector of the program variable. |
| `type` | string |  | One of: `bool`, `uint8`, `int8`, `int16`, `int32`, `double`, `string`. With `variable`: the type of the program variable. Default: `bool`. |
| `value` | string or number or integer or boolean |  | With `variable`: the value to write; its JSON type must fit `type`. |

**Result**

| Key | Description |
|---|---|
| `applied` | For a category: one entry for each setting that the call was given, `true` when Vectorworks accepted it. For `variable`: `true` when the variable was written. |
| `selector` | With `variable`: the selector that was written. |

In `defaultAttributes`, `applied` has these keys: `colors` (the RGB colors), `colorIndices` (the color table indices; `false` when an index is not a whole number within the color index range), the by-class flags, `penStyle`, `lineWeightMils`, `fillStyle`, `hatch`, `gradient`, `imageFill`, `tile`, `opacity` (`penOpacity` and `fillOpacity`; the one that is left out keeps its value), `opacityByClass` (`penOpacityByClass` and `fillOpacityByClass`; the one that is left out keeps its value), `beginningMarker`, `endMarker` (a partial marker keeps the members left out) and `class` and `dimensionClass` (`false` when the class does not exist). The `text` category has `applied.style` for its `style` object; only the members present change.

Errors: `unknown 'category' (display, editing, snapping, grid, stackLayers, text, defaultAttributes, variable)`; `unknown variable 'type': <type>`.

## Selection

> **Group:** `Selection` · **Group ID:** `selection` · **Active by default:** Yes · **Risk level:** medium · **Tools:** 3

**List the current selection and move, rotate, scale, duplicate, group, delete or re-class it in bulk.**

Query and operate on the current selection: list selected objects and move, rotate, scale, duplicate, group, delete or re-class them in bulk. Each edit runs as its own named, undoable Vectorworks operation.

| Tool | Effect | Risk | Summary |
|---|---|---|---|
| [`getSelection`](#getselection) | Read-only | low | Lists the selected objects on every layer and the bounds of the selection. |
| [`selectObjects`](#selectobjects) | Edit | medium | Selects or deselects objects by criteria or by UUID, or all or none. |
| [`editSelection`](#editselection) | Edit | medium | Moves, rotates, scales, duplicates, groups, deletes or re-classes the selection. |

### getSelection

Lists the selected objects on every layer and the bounds of the selection.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the currently selected objects (uuid, type, name) and the combined selection bounds. Covers the selected objects on every layer of the drawing, not only the active one. `descend` (none by default, groups, viewports or all) also lists selected objects inside those containers, e.g. while the user edits inside a group; `bounds` covers the selected top-level objects.

`workingLayers` gives the count and bounds of the selection editSelection acts on: the selected objects of the active layer, plus the other layers when the layer options allow editing them.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `descend` | string |  | One of: `none`, `groups`, `viewports`, `all`. Default: `none`. |

**Result**

| Key | Description |
|---|---|
| `count` | The number of objects in `objects`. |
| `objects` | The selected objects, each as an [object reference](Common.md#object-references). |
| `bounds` | The combined [bounds](Common.md#rectangles) of the selected top-level objects. Left out when nothing is selected. |
| `workingLayers` | The selection that editSelection acts on: `count` (the number of selected objects) and `bounds`. `bounds` is left out when there is no such selection. |

Error: `unknown 'descend'; use none | groups | viewports | all`.

### selectObjects

Selects or deselects objects by criteria or by UUID, or all or none.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: selectObjects" · **In runToolBatch:** yes

**Details**

Change the selection. Use `all` or `none` to select/deselect everything, or provide `criteria` (a Vectorworks criteria string, same syntax as findObjects) and/or `uuids`. Criteria that do not compile return an error. `mode` "replace" (default) or "add" selects the targets and returns `selectedCount`; "remove" deselects only the targets and returns `deselectedCount`.

> **Note:** `all` is checked first, then `none`; when one of them is `true`, the call ignores `criteria`, `uuids` and `mode`. Otherwise the targets are the objects that match `criteria` together with the objects that have one of the `uuids`. An unknown `mode` behaves as `replace`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `all` | boolean |  | `true` selects every object. |
| `none` | boolean |  | `true` deselects every object. |
| `criteria` | string |  | A Vectorworks criteria string, same syntax as findObjects. |
| `uuids` | array of string |  | UUIDs of the objects to act on. A UUID that matches no object is skipped without an error. |
| `mode` | string |  | One of: `replace`, `add`, `remove`. Default: `replace`. |

**Result**

| Key | Description |
|---|---|
| `selected` | With `all` or `none`: `"all"` or `"none"`. |
| `selectedCount` | With `mode` `replace` or `add`: the number of targets that are selected after the call (with `add`, also targets that were selected before). An object that matches `criteria` and is in `uuids`, or a UUID listed twice, is counted each time. |
| `deselectedCount` | With `mode` `remove`: the number of target objects that were deselected; objects that were not selected are not counted. |

Errors: `invalid criteria: <detail>`; `no target objects (provide 'criteria', 'uuids', or 'all' / 'none')` when no object matches.

### editSelection

Moves, rotates, scales, duplicates, groups, deletes or re-classes the selection.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: editSelection" · **In runToolBatch:** yes

**Details**

Operate on the whole selection of the working layers (see getSelection `workingLayers`). `action`: move (needs `offset`), rotate (`angle` radians, `center`), scale (`scaleX`,`scaleY`,`center`), duplicate (`offset`), group, delete, or setClass (`class`; `useClassAttributes` also sets every attribute of the objects by class). `group` moves the selected objects into a new group in the active layer (or in the group or symbol definition being edited), selects the group and returns it with `groupedCount`; selected objects that a group cannot take, such as doors and windows inserted in walls and members of a plug-in object or a roof, stay where they are (`ungroupedCount`), and the call fails, changing nothing, when no selected object can be grouped.

Edit &gt; Undo of the group puts the objects back where they were and removes the group.

> **Note:** The tool does not check that an action has the arguments the Details list. Without `offset`, `move` and `duplicate` use (0,0), so the objects do not move. Without `center`, `rotate` and `scale` turn or scale about the world origin (0,0). `angle` defaults to 0 and `scaleX` and `scaleY` to 1. The tool acts only on the selection of the working layers, which `getSelection` reports as `workingLayers`; selected objects that are not on a working layer are not changed.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `action` | string | Yes | One of: `move`, `rotate`, `scale`, `duplicate`, `group`, `delete`, `setClass`. |
| `offset` | [point](Common.md#points) |  | `move` and `duplicate`: the distance to move by, in world units. Default: (0,0). |
| `angle` | number |  | Angle in radians, counter-clockwise. `rotate` only. Default: 0. |
| `center` | [point](Common.md#points) |  | `rotate` and `scale`: the point to turn or scale about. Default: the world origin. |
| `scaleX` | number |  | `scale` only: the factor along x. Default: 1. A factor of 0 fails (`ok` is `false`). |
| `scaleY` | number |  | `scale` only: the factor along y. Default: 1. A factor of 0 fails (`ok` is `false`). |
| `class` | string |  | `setClass` only: the name of an existing class. |
| `useClassAttributes` | boolean |  | `setClass` only: `true` also sets every attribute of the objects by class. |

**Result**

| Key | Description |
|---|---|
| `ok` | `move`, `rotate`, `scale` and `duplicate`: `true` when Vectorworks applied the action, `false` (without an `err`) when nothing is selected on the working layers. `setClass`: `true` when every selected object took the class, also when nothing is selected. After `duplicate` the new copies are the selection. |
| `deletedCount` | `delete`: the number of objects deleted; 0 when nothing is selected. |
| object reference, `groupedCount`, `ungroupedCount` | `group`: the new group as an [object reference](Common.md#object-references), the number of objects that moved into it, and, only when some stayed where they were, `ungroupedCount`. The group is selected afterwards. |

Errors: `unknown 'action'; use move | rotate | scale | duplicate | group | delete | setClass`; `class not found` for `setClass` with an unknown or empty `class`. `group` fails with `failed to group the selection`, alone when Vectorworks cannot create the group, or followed by one of these reasons: `nothing is selected on the working layers`; `the active container is not a layer, a group or a symbol definition`; `none of the selected objects can be moved into a group (objects inserted in a wall, such as doors and windows, and members of a plug-in object or a roof stay where they are)`; `none of the selected objects could be moved into a group`. An error reverts the call (`rolledBack`).
