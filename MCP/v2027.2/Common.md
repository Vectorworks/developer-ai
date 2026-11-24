**English** • [Deutsch](../../MCP.de/v2027.2/Common.md) • [日本語](../../MCP.ja/v2027.2/Common.md)

# Common — shared conventions

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The conventions that every tool of the Vectorworks MCP server follows: calls and results, object references, points and colors, units, creation options, applied settings, plug-in parameters, paging, effects, risk levels and undo.

## Table of contents

- [Overview](#overview)
- [Tool groups and activation](#tool-groups-and-activation)
- [Core group](#core-group)
  - [listToolGroups](#listtoolgroups)
  - [activateToolGroups](#activatetoolgroups)
  - [runToolBatch](#runtoolbatch)
- [Calling a tool](#calling-a-tool)
- [Results and errors](#results-and-errors)
- [Object references](#object-references)
- [Points, rectangles and colors](#points-rectangles-and-colors)
  - [Points](#points)
  - [Rectangles](#rectangles)
  - [Colors](#colors)
- [Units and angles](#units-and-angles)
- [Creation options](#creation-options)
- [Applied settings](#applied-settings)
- [Plug-in parameters](#plug-in-parameters)
  - [Reading parameters](#reading-parameters)
  - [Writing parameters](#writing-parameters)
- [Paging](#paging)
- [Effects and risk levels](#effects-and-risk-levels)
- [Undo](#undo)

## Overview

| Topic | What it covers |
|---|---|
| [Tool groups and activation](#tool-groups-and-activation) | Which tools are available and how to switch groups on. |
| [Core group](#core-group) | The three meta-tools that are always available: `listToolGroups`, `activateToolGroups`, `runToolBatch`. |
| [Calling a tool](#calling-a-tool) | The shape of a call and of its result, with an example. |
| [Results and errors](#results-and-errors) | Result objects, error messages and rolled back calls. |
| [Object references](#object-references) | How tools identify objects in their arguments and in their results. |
| [Points, rectangles and colors](#points-rectangles-and-colors) | The shared value formats for geometry and color. |
| [Units and angles](#units-and-angles) | World units, radians and the few exceptions. |
| [Creation options](#creation-options) | The options that most create tools accept: class, name and selection. |
| [Applied settings](#applied-settings) | How tools report, setting by setting, what they wrote. |
| [Plug-in parameters](#plug-in-parameters) | Reading and writing the parameters of plug-in objects. |
| [Paging](#paging) | How long lists are returned page by page. |
| [Effects and risk levels](#effects-and-risk-levels) | What a tool may change, and how clients should treat it. |
| [Undo](#undo) | How the changes of a tool call are recorded for Edit &gt; Undo. |

## Tool groups and activation

The tools are organized in tool groups. The tool list of the server (`tools/list`) shows only the tools of the **active** groups, so a tool that is missing from the list is not necessarily unsupported.

- 4 groups are active by default: Document, Selection, IFC, Objects. The **Core** group is always active.
- The other groups are activated with [`activateToolGroups`](#activatetoolgroups). An activated group stays active until the server is stopped or restarted. The server keeps the activation, not the connection, so it applies to every client. Refresh the tool list afterwards (clients that handle the `list_changed` notification do this automatically).
- [`listToolGroups`](#listtoolgroups) lists every group, active or not, and with `includeTools` the names and descriptions of its tools.
- Groups are named by their display name or by their group ID; both are accepted.
- The **tools mode** that is chosen in the Start MCP Server dialog decides which groups the server offers at all:
  - **Enable all tools** (the default): every group is offered.
  - **Enable all without scripting tools**: the [Scripting](Scripting.md#scripting) group, with its 7 tools, is not registered. It does not appear in `listToolGroups`, and `activateToolGroups` reports it in `not_found`.
  - **Enable scripting tools only**: only the Scripting group is offered (besides the Core group), and it is active at once.

| Group | Group ID | Page | Active by default | Risk level | Tools | Summary |
|---|---|---|---|---|---|---|
| [Core](#core-group) | `core` | [Common](#core-group) | Always | low | 3 | Discover and activate tool groups, and run several tool calls as one undo step. |
| [Document](DocumentAccess.md#document) | `document` | [DocumentAccess](DocumentAccess.md) | Yes | low | 17 | The active drawing: document summary, layers, stories, classes, units, view and document preferences. |
| [Selection](DocumentAccess.md#selection) | `selection` | [DocumentAccess](DocumentAccess.md) | Yes | medium | 3 | List the current selection and move, rotate, scale, duplicate, group, delete or re-class it in bulk. |
| [IFC](IFC.md#ifc) | `ifc` | [IFC](IFC.md) | Yes | low | 4 | Read-only IFC data: the IFC entity and property sets of objects, the IFC property-set definitions (standard and custom) and the custom property sets of the document. |
| [IFC Data Mapping](IFC.md#ifc-data-mapping) | `ifc-data-mapping` | [IFC](IFC.md) | No | low | 2 | Read the IFC Data Manager mapping definitions of the active document. |
| [Menus](MenuAccess.md#menus) | `menus` | [MenuAccess](MenuAccess.md) | No | high | 4 | Find menu commands, read the menu bar, check whether a command can run now, and run it. |
| [Draw2D](ObjectPrimitives.md#draw2d) | `draw2d` | [ObjectPrimitives](ObjectPrimitives.md) | No | low | 15 | Create, edit, measure and combine 2D primitives, and create, read and edit text objects. |
| [Objects](ObjectPrimitives.md#objects) | `objects` | [ObjectPrimitives](ObjectPrimitives.md) | Yes | medium | 12 | Find, inspect and edit any object: attributes, transforms, containers, plug-in parameters and records. |
| [3D Modeling](Objects3D.md#3d-modeling) | `3d-modeling` | [Objects3D](Objects3D.md) | No | medium | 16 | Create, read and edit solids, 3D polygons, meshes, NURBS curves and surfaces, and surface models. |
| [Annotation](ObjectsAnnotation.md#annotation) | `annotation` | [ObjectsAnnotation](ObjectsAnnotation.md) | No | medium | 8 | Data tags, title block borders and the title block project data of the document. |
| [Dimensioning](ObjectsAnnotation.md#dimensioning) | `dimensioning` | [ObjectsAnnotation](ObjectsAnnotation.md) | No | medium | 8 | Linear, angular, arc length and radial dimensions, and center marks. |
| [Architecture](ObjectsArchitect.md#architecture) | `architecture` | [ObjectsArchitect](ObjectsArchitect.md) | No | medium | 9 | BIM building elements: walls, slabs, roofs, doors, windows, columns and stairs. |
| [ConnectCAD](ObjectsConnectCAD.md#connectcad) | `connectcad` | [ObjectsConnectCAD](ObjectsConnectCAD.md) | No | medium | 10 | ConnectCAD schematic devices, sockets and device types, built from JSON device descriptions. |
| [Landmark](ObjectsLandmark.md#landmark) | `landmark` | [ObjectsLandmark](ObjectsLandmark.md) | No | medium | 10 | Plants, hardscapes, landscape areas, site models, site modifiers, stakes, property lines and existing trees. |
| [Spotlight](ObjectsSpotlight.md#spotlight) | `spotlight` | [ObjectsSpotlight](ObjectsSpotlight.md) | No | medium | 5 | Spotlight lighting devices and the GDTF fixture types they use. |
| [Object Info](OIPAccess.md#object-info) | `object-info` | [OIPAccess](OIPAccess.md) | No | medium | 3 | Read and operate the Object Info palette for the current selection, like a user. |
| [Resources](Resources.md#resources) | `resources` | [Resources](Resources.md) | No | medium | 11 | List, import, create, inspect, edit and apply resources; read and edit worksheets. |
| [Scripting](Scripting.md#scripting) | `scripting` | [Scripting](Scripting.md) | No | high | 7 | Run Python scripts, read and save Python script resources, and look up the Python `api` module. |
| [InteractiveTools](ToolAccess.md#interactivetools) | `interactivetools` | [ToolAccess](ToolAccess.md) | No | high | 10 | Operate the interactive Vectorworks tools of the tool palettes like a user. |

## Core group

> **Group:** `Core` · **Group ID:** `core` · **Active:** always · **Risk level:** low · **Tools:** 3

**Discover and activate tool groups, and run several tool calls as one undo step.**

The meta-tools of the Core group are always available. They manage the tool list and group tool calls; they cannot be called inside [`runToolBatch`](#runtoolbatch).

| Tool | Effect | Risk | Summary |
|---|---|---|---|
| [`listToolGroups`](#listtoolgroups) | Read-only | low | List all tool groups, active and inactive, with their activation state and, optionally, their tools. |
| [`activateToolGroups`](#activatetoolgroups) | Session setting | low | Activate tool groups so that their tools appear in the tool list, until the server is stopped. |
| [`runToolBatch`](#runtoolbatch) | Edit (batch) | medium | Run several tool calls as one undo step, all or nothing. |

### listToolGroups

List all tool groups, active and inactive, with their activation state and, optionally, their tools.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** no

**Details**

List active AND inactive tool groups with their metadata and activation state. Before declaring a capability unsupported, inspect relevant groups with `group` (display name or groupId) and `includeTools` true to read their tool names and descriptions without activation or schemas. Activate the required group, then refresh tools/list before using its tools; absence from the active tool list does not mean unsupported.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `group` | string |  | Optional group display name or groupId to inspect. |
| `includeTools` | boolean |  | Include tool names and descriptions, even for inactive groups; no schemas. Default: `false`. |

**Result**

`{ "groups": [...] }`, one entry per group. The Core group is first; the order of the other groups is not defined. Without `group` every group is returned; with `group` only that one.

| Key | Description |
|---|---|
| `groupId` | The group ID, for example `3d-modeling`. |
| `displayName` | The group name, for example `3D Modeling`. |
| `shortDescription` | When to activate the group. |
| `safetyLevel` | `low`, `medium` or `high`. |
| `currentlyActive` | `true` when the tools of the group are in the tool list. |
| `toolCount` | The number of tools of the group. |
| `tools` | Only with `includeTools`: a list of `{ "name", "description", "safetyLevel" }`. A tool that has no risk level of its own gets the risk level of its group. |

Errors: `listToolGroups requires an arguments object`, `includeTools must be a boolean`, `group must be a display name or groupId string` and `Unknown tool group: <value>`.

**Example arguments**

```json
{
  "group": "architecture",
  "includeTools": true
}
```

### activateToolGroups

Activate tool groups so that their tools appear in the tool list, until the server is stopped.

> **Effect:** Session setting · **Risk:** low · **Undo:** none (the drawing is not changed) · **In runToolBatch:** no

**Details**

Enable one or more tool groups for the rest of the session, exposing their tools to subsequent tools/list requests. Each entry may be either the group's display name or its groupId as reported by listToolGroups. Refresh tools/list after activation (or allow your client's list_changed handling to refresh it) before calling newly exposed tools. Activation changes tool availability, not drawing content, and does not authorize editing tools.

> **Note:** "The rest of the session" means until the server is stopped or restarted. The activation belongs to the server, not to the client connection, so it applies to every client. A group cannot be deactivated again.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `groups` | array of string | Yes | Group display names or groupIds to activate. |

**Result**

`{ "activated": [...], "already_active": [...], "not_found": [...] }`.

- `activated` and `already_active` list the display names of the groups.
- `not_found` repeats the entries that name no group, for example the Scripting group in the tools mode "Enable all without scripting tools".
- Entries that are not strings are skipped, and a group that is named twice is reported once.
- Without a `groups` array the result is `{ "err": "activateToolGroups requires a 'groups' array" }`.
- When the client accepts `text/event-stream`, the server answers as an event stream: a `notifications/tools/list_changed` message first, then the result. Otherwise it sends the plain JSON-RPC response, and the client has to refresh the tool list itself. The server does this for every `activateToolGroups` call, also when no group changed or the result has `err`.

**Example arguments**

```json
{
  "groups": ["architecture", "Dimensioning"]
}
```

### runToolBatch

Run several tool calls as one undo step, all or nothing.

> **Effect:** Edit (batch) · **Risk:** medium · **Undo:** one step "MCP: &lt;name&gt;" for the whole batch · **In runToolBatch:** no

**Details**

Run several tool calls as ONE Vectorworks undo step 'MCP: &lt;name&gt;', all or nothing. Use it for one user-level job made of independent calls, for example 'create these 4 walls and the slab', so that one Undo reverts the whole job. `calls` run in this order, each { tool, arguments } as in a direct call of the tool (arguments default {}); at most 50. A call cannot use results of earlier calls in the same batch, such as the UUID of an object created in it: for that, write one runPythonScript.

Returns `undoStep` true, `undoName` and `results` ({ tool, result } per call). When a call fails (`err` in its result, or an exception), the batch stops and everything it did is reverted: `err` names the call, `failedCall` is its 1-based number, `rolledBack` says whether the revert ran, `undoStep` is false and `results` ends with the failed call. `warning` is added when an undo event is still open afterwards.

Only tools of active groups.

**Refused before anything runs:** high-risk tools (safetyLevel=high or destructiveHint=true: ask the user, then call them one by one), the interactive tools (they record their own undo) and the meta-tools, runToolBatch included; any batch while no document is open or another Vectorworks operation is in progress. Vectorworks is busy until the batch ends. Read-only tools are allowed but not needed.

> **Note:** The advice "write one runPythonScript" applies only when the [Scripting](Scripting.md#scripting) group is available. That group is not active by default, `runPythonScript` is a high-risk tool (ask the user first), and the tools mode "Enable all without scripting tools" does not offer the group at all. Without scripting, call the tools one after another. Each call that changes the drawing is then its own undo step.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Name of the undo step 'MCP: &lt;name&gt;': not blank, without control characters; for example 'Create walls and slab'. 1 to 63 characters. |
| `calls` | array of object | Yes | The tool calls, run in this order. 1 to 50 items. |
| `calls[].tool` | string | Yes | Name of a tool of an active group. |
| `calls[].arguments` | object |  | Arguments of the tool, as in a direct call; default {}. |

**Result**

| Outcome | Result |
|---|---|
| Every call succeeded | `{ "undoStep": true, "undoName": "MCP: <name>", "results": [ { "tool", "result" }, ... ] }` |
| A call failed | `{ "err": "call <n> (<tool>) failed: <err of the call>", "failedCall": <n>, "rolledBack": <true or false>, "undoStep": false, "results": [ ... ] }`. The batch stops at that call, and `results` ends with it. |
| The batch was refused | `{ "err": "<reason>", "undoStep": false }`. Nothing ran, and the result has no `results`, `failedCall` or `rolledBack`. |

- A call fails when its result has a top-level `err`, or when it throws. A thrown exception is reported as `exception: <message>`, or as `unhandled exception`.
- `rolledBack` is `true` when the undo event of the batch was reverted. It is `false` when no undo event was open any more, so there was nothing to revert.
- `warning` ("An undo event is still open after the batch: changes made until Vectorworks ends it can join it.") is added to a successful or a failed result when an undo event is still open after the batch.
- The whole batch is checked before anything runs, in this order: `name`, `calls` (the first call that cannot run is named), and the state of Vectorworks. The reasons for a refusal:

| `err` of a refused batch | Cause |
|---|---|
| `'name' must be a string` | `name` is missing or is not a string. |
| `'name' must not be empty or blank` | `name` is empty or has only spaces. |
| `'name' must not contain control characters` | `name` contains a control character. |
| `'name' must have at most 63 characters` | `name` is longer than 63 characters. |
| `'calls' must be an array of 1 to 50 calls { tool, arguments }` | `calls` is missing, is not an array, is empty or has more than 50 items. |
| `call <n> (<tool>): must be an object with a string 'tool'` | The call is not an object with a string `tool`. |
| `call <n> (<tool>): 'arguments' must be an object` | `arguments` is not an object. |
| `call <n> (<tool>): unknown tool` | No tool has this name. |
| `call <n> (<tool>): the tool is in an inactive group; activate it via activateToolGroups` | The group of the tool is not active. |
| `call <n> (<tool>): only provider tools can run in a batch, not the meta-tools (listToolGroups, activateToolGroups, runToolBatch)` | The tool is a meta-tool of the Core group. |
| `call <n> (<tool>): high-risk tools cannot run in a batch: ask the user, then call the tool on its own` | The tool has `destructiveHint`, or the risk level `high` (its own or, without one, that of its group): `runPythonScript`, `runScript` and `runMenuCommand`. |
| `call <n> (<tool>): interactive tools record their own undo steps and cannot run in a batch: call the tool on its own` | The tool records its own undo steps: `activateTool`, `setToolMode`, `setToolModes`, `sendToolPointer`, `sendToolAction`, `setOIPValues` and `pressOIPButton`. |
| `no document is open` | No drawing is open. |
| `an undo event is already open: another Vectorworks operation is in progress; try again when it has finished` | Another undo event is being built. |

`<n>` is the 1-based number of the call. `(<tool>)` is left out when the call has no tool name.

**Example arguments** (two walls in one undo step; the Architecture group must be active)

```json
{
  "name": "Create walls",
  "calls": [
    {
      "tool": "createWall",
      "arguments": {"start": {"x": 0, "y": 0}, "end": {"x": 5000, "y": 0}}
    },
    {
      "tool": "createWall",
      "arguments": {"start": {"x": 5000, "y": 0}, "end": {"x": 5000, "y": 4000}}
    }
  ]
}
```

## Calling a tool

A tool is called with the MCP `tools/call` request: the tool `name` and an `arguments` object. Arguments that are not needed are left out. Every tool returns one JSON object.

For example, list the rectangles of the drawing, two at a time:

```json
{
  "name": "findObjects",
  "arguments": {"criteria": "(T=RECT)", "limit": 2}
}
```

The result, with placeholders for the UUIDs:

```json
{
  "count": 3,
  "limit": 2,
  "nextOffset": 2,
  "notSearched": ["INSYMBOL", "INOBJECT", "INVIEWPORT", "INOBJPATH", "INOBJPROFILE"],
  "objects": [
    {"type": 3, "typeName": "Rectangle", "uuid": "<uuid 1>"},
    {
      "name": "Plot outline",
      "type": 3,
      "typeName": "Rectangle",
      "uuid": "<uuid 2>"
    }
  ],
  "offset": 0,
  "returned": 2,
  "truncated": true
}
```

`count` is the number of all matches, `objects` holds this page of [object references](#object-references) and `nextOffset` is the `offset` of the next page (see [Paging](#paging)). `notSearched` lists the places that the criteria did not include, such as the inside of symbol definitions.

## Results and errors

- Every tool returns one JSON object. The keys of the object are described with each tool.
- A call that fails returns an object with `err`, a message that says what went wrong. For example:

```json
{
  "err": "object not found"
}
```

- The server sends the object as the text of the first `content` item of the MCP result: `result.content[0].text` holds the JSON text. When the object has a top-level `err`, the result also has `isError: true`.
- `arguments` must be a JSON object. Anything else counts as `{}`; a string that holds a JSON object is parsed. This holds for the tools of the 18 groups. The Core tools `listToolGroups`, `activateToolGroups` and `runToolBatch` get `arguments` as sent: a string is not parsed, and a value that is not an object gives their error (for example `listToolGroups requires an arguments object`).
- Paged tools and some other tools check the type and the range of their arguments before anything changes. The message names the argument, for example `'limit' must be a number`, `'countOnly' must be true or false`, `'limit' must be at least 1` or `'offset' must not be negative`. Not every tool checks the types: an argument of the wrong JSON type is often read as if it was missing, and the default applies. Check the types in your call.
- When a call that edits the drawing fails, the server reverts what the tool registered for undo and adds `rolledBack` to the result: `true` when the revert worked, `false` when it did not. Tools that record their own undo step are never rolled back. See [Undo](#undo).
- Tools that write several settings report, setting by setting, what they wrote in `applied`. See [Applied settings](#applied-settings).

These `err` texts can come from any tool:

| `err` | Cause |
|---|---|
| `no active Vectorworks document` | No document is open. Every tool outside the [Core](#core-group) group needs an open document, `convertUnits` included. The meta-tools [`listToolGroups`](#listtoolgroups) and [`activateToolGroups`](#activatetoolgroups) do not. |
| `exception: &lt;text&gt;` or `unhandled exception` | The tool threw an exception. The call counts as failed (see `rolledBack`). |

A request that the server cannot handle at all is answered with a JSON-RPC error, not with a tool result:

| Code | Meaning |
|---|---|
| `-32700` | The body is not valid JSON. |
| `-32601` | `Method not found: &lt;method&gt;`. |
| `-32602` | Invalid parameters: `tools/call requires a 'name' parameter`, `Tool '&lt;name&gt;' is in an inactive group; activate it via activateToolGroups.` or `Unknown tool: &lt;name&gt;`. |
| `-32603` | Internal error, also when `params` of `tools/call` is not an object or `name` is not a string. |

## Object references

Tools that work on one existing object take the object in one of three arguments:

| Argument | Type | Meaning |
|---|---|---|
| `uuid` | string | The UUID of the object, as reported by the tools. The preferred way. |
| `name` | string | The exact Vectorworks name of the object (Object Info palette, Name field). |
| `index` | integer | The internal index of the object. |

The server tries `uuid` first, then `name`, then `index`, and uses the first that finds an object. When none finds one, the call fails with `object not found`. Some tools add a hint, as in `object not found (provide 'uuid', 'name' or 'index')`, or name the role of the object, as in `source object not found`, `path object not found` or `profile object not found`. Some tools name the argument after its role, such as `targetUuid`, `pathUuid` or `profileUuid`; these take a UUID. In two tools `name` has a second use: in [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) it is also the parameter to write, and in [`editObject`](ObjectPrimitives.md#editobject) it is also the new name of the object. Give the object by `uuid` there, because `name` is tried before `index`.

Tools that return objects (search results, created objects, group members) report them as **object references**:

| Key | Type | Meaning |
|---|---|---|
| `uuid` | string | The UUID of the object. |
| `type` | integer | The numeric Vectorworks object type, for example 2 for a line, 3 for a rectangle and 86 for a plug-in object. |
| `typeName` | string | The type name, for the common types only: Line, Rectangle, Oval, Polygon, Arc, FreehandPolygon, Text, Group, RoundedRectangle, Symbol, SymbolDefinition, Locus, Polyline, Extrude, Mesh and Layer. |
| `parametricName` | string | Plug-in objects only: the universal name of the plug-in, for example `Door`. |
| `localizedParametricName` | string | Plug-in objects only: the plug-in name in the language of Vectorworks, when the plug-in is installed. |
| `name` | string | The object name, when the object has one. |

Use the `uuid` of a reference in the next call.

## Points, rectangles and colors

### Points

A 2D point is an object `{ "x": 0, "y": 0 }` in world units. The array form `[x, y]` is also accepted, but the input schemas declare only the object form, so prefer it. A 3D point adds `z`: `{ "x": 0, "y": 0, "z": 0 }`.

The 3D Modeling tools use absolute world Z for every 3D point, center, frame and `baseElevation` that they take or return: they add no design layer elevation, so `z` 0 is world Z 0, not the plane of an elevated layer. To put an object on a layer at elevation E, add E to its Z values; these tools report E as `layerElevation`. `bounds3D` Z values are absolute world heights too.

### Rectangles

A rectangle is `{ "left": 0, "top": 1000, "right": 2000, "bottom": 0 }` in world units, with `top` above `bottom`. Bounds that the tools report add `width`, `height` and `center` (a point):

```json
{
  "left": 0,
  "top": 1000,
  "right": 2000,
  "bottom": 0,
  "width": 2000,
  "height": 1000,
  "center": {"x": 1000, "y": 500}
}
```

### Colors

A color is `{ "r": 255, "g": 128, "b": 0 }` with channels from 0 to 255; the array form `[r, g, b]` is also accepted, but the input schemas declare only the object form, so prefer it. Values outside 0 to 255 are clamped. Attributes that can also use the document color table have a separate index key next to the RGB value, such as `foreColorIndex` next to `foreColor`. When both are given and both differ from the current value, the index wins. The exception is `setObjectAttributes`: there a given `foreColorIndex` or `backColorIndex` is applied after the RGB value and always wins, even when it equals the current index.

## Units and angles

Unless a tool says otherwise:

| Value | Unit |
|---|---|
| Coordinates, lengths, distances, offsets | World units: the units of the drawing. Read them with `getUnits`; convert with `convertUnits`. |
| Angles, rotations | Radians, counter-clockwise positive. |
| Text | UTF-8 strings. |
| Colors | RGB, 0 to 255 per channel (see [Colors](#colors)). |

The exceptions are named in the tool descriptions. The main ones:

| Value | Unit |
|---|---|
| Font sizes of dimensions (`fontSize`), of worksheet text formats (`size`) and `sizePoints` of text | Points. The `size` of text objects and of the text preferences is in world units. |
| Line end marker angle | Whole degrees (see [Line end markers](Attributes.md#line-end-markers)). |
| Line end marker length and width | Page inches. |
| Drop shadow angle | Degrees (see [Drop shadow](Attributes.md#drop-shadow)). |
| Drop shadow offset and blur radius | Page inches or world units, as `units` says. |
| Roof slopes | Degrees. |
| Plug-in parameters read as typed values | Lengths in world units, angles in degrees (see [Plug-in parameters](#plug-in-parameters)). |
| Object Info palette values | Typed as a user types them, in the units the palette shows. |

## Creation options

Most tools that create objects accept four optional creation options. They are applied to the new object after it is created, and the tool then returns its [object reference](#object-references). A value of the wrong type (a `class` or `name` that is not a string, for example) is ignored without an error. Without `class`, the tool sets no class. The exception is [`combineShapes`](ObjectPrimitives.md#combineshapes): its results get the class of the first shape, and `useClassAttributes` then makes their attributes follow that class, with or without `class`.

| Option | Type | Meaning |
|---|---|---|
| `class` | string | The class of the new object. A class that does not exist yet is created. |
| `useClassAttributes` | boolean | With `class`: also set the graphical attributes of the object to "by class". |
| `name` | string | The name of the new object. |
| `select` | boolean | Select the new object. |

Tools with these options (45): [`createLine`](ObjectPrimitives.md#createline), [`createRectangle`](ObjectPrimitives.md#createrectangle), [`createCircle`](ObjectPrimitives.md#createcircle), [`createArc`](ObjectPrimitives.md#createarc), [`createPolygon`](ObjectPrimitives.md#createpolygon), [`createPolyline`](ObjectPrimitives.md#createpolyline), [`createLocus`](ObjectPrimitives.md#createlocus), [`combineShapes`](ObjectPrimitives.md#combineshapes), [`createText`](ObjectPrimitives.md#createtext), [`createPluginObject`](ObjectPrimitives.md#createpluginobject), [`createExtrude`](Objects3D.md#createextrude), [`createSolidPrimitive`](Objects3D.md#createsolidprimitive), [`createSweep`](Objects3D.md#createsweep), [`combineSolids`](Objects3D.md#combinesolids), [`createShell`](Objects3D.md#createshell), [`convertSolid`](Objects3D.md#convertsolid), [`create3DPolygon`](Objects3D.md#create3dpolygon), [`createMesh`](Objects3D.md#createmesh), [`createNurbsCurve`](Objects3D.md#createnurbscurve), [`createNurbsSurface`](Objects3D.md#createnurbssurface), [`createSurfaceModel`](Objects3D.md#createsurfacemodel), [`convertTo3D`](Objects3D.md#convertto3d), [`createDataTag`](ObjectsAnnotation.md#createdatatag), [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock), [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension), [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension), [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension), [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension), [`createCenterMark`](ObjectsAnnotation.md#createcentermark), [`createWall`](ObjectsArchitect.md#createwall), [`createSlab`](ObjectsArchitect.md#createslab), [`createRoof`](ObjectsArchitect.md#createroof), [`createDoor`](ObjectsArchitect.md#createdoor), [`createWindow`](ObjectsArchitect.md#createwindow), [`createColumn`](ObjectsArchitect.md#createcolumn), [`createStair`](ObjectsArchitect.md#createstair), [`createPlant`](ObjectsLandmark.md#createplant), [`createHardscape`](ObjectsLandmark.md#createhardscape), [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea), [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier), [`createPropertyLine`](ObjectsLandmark.md#createpropertyline), [`createSiteModel`](ObjectsLandmark.md#createsitemodel), [`createStake`](ObjectsLandmark.md#createstake), [`createExistingTree`](ObjectsLandmark.md#createexistingtree), [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice).

These create tools take no creation options: `createLayer`, `createClass`, `createStory`, `createResource`, `createConnectCADDevice`, `createConnectCADDevices` and `createConnectCADDeviceType`. The objects that `edit3DGeometry` creates (a planar solid, repaired meshes, extended and offset copies) take none either.

## Applied settings

Tools that write several settings in one call report the outcome of each in `applied`: an object with one entry per setting given, `true` when it was written and `false` when it was not (for example because the value does not fit or the object does not support the setting). A call can therefore succeed while single settings are rejected; check `applied` when it matters.

For example, [`editLayer`](DocumentAccess.md#editlayer) with these arguments:

```json
{
  "name": "Design Layer-1",
  "elevation": 3000,
  "scale": 50
}
```

returns the updated layer with:

```json
{
  "applied": {"elevation": true, "scale": true}
}
```

Tools that report `applied` (43): [`editLayer`](DocumentAccess.md#editlayer), [`editStory`](DocumentAccess.md#editstory), [`editClass`](DocumentAccess.md#editclass), [`setUnits`](DocumentAccess.md#setunits), [`setPreferences`](DocumentAccess.md#setpreferences), [`setGeometry`](ObjectPrimitives.md#setgeometry), [`editVertices`](ObjectPrimitives.md#editvertices), [`createText`](ObjectPrimitives.md#createtext), [`editText`](ObjectPrimitives.md#edittext), [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes), [`copyAttributes`](ObjectPrimitives.md#copyattributes), [`editObject`](ObjectPrimitives.md#editobject), [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter), [`createPluginObject`](ObjectPrimitives.md#createpluginobject), [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject), [`setProjectData`](ObjectsAnnotation.md#setprojectdata), [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension), [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension), [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension), [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension), [`setDimension`](ObjectsAnnotation.md#setdimension), [`createWall`](ObjectsArchitect.md#createwall), [`createSlab`](ObjectsArchitect.md#createslab), [`createDoor`](ObjectsArchitect.md#createdoor), [`createWindow`](ObjectsArchitect.md#createwindow), [`createStair`](ObjectsArchitect.md#createstair), [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject), [`setConnectCADSocket`](ObjectsConnectCAD.md#setconnectcadsocket), [`createPlant`](ObjectsLandmark.md#createplant), [`createHardscape`](ObjectsLandmark.md#createhardscape), [`createLandscapeArea`](ObjectsLandmark.md#createlandscapearea), [`createSiteModifier`](ObjectsLandmark.md#createsitemodifier), [`createPropertyLine`](ObjectsLandmark.md#createpropertyline), [`createSiteModel`](ObjectsLandmark.md#createsitemodel), [`createStake`](ObjectsLandmark.md#createstake), [`createExistingTree`](ObjectsLandmark.md#createexistingtree), [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject), [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice), [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice), [`editResource`](Resources.md#editresource), [`setResourceDetails`](Resources.md#setresourcedetails), [`applyResource`](Resources.md#applyresource), [`editWorksheet`](Resources.md#editworksheet).

The shape of `applied` differs in these tools:

- A create tool reports `applied` only when the call gave at least one of the settings it reports. This holds for [`createText`](ObjectPrimitives.md#createtext), [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice), the four `create…Dimension` tools and the create tools of the Architecture and Landmark groups. [`createPluginObject`](ObjectPrimitives.md#createpluginobject) reports it only with `params`. The create tools that are not listed (`createColumn`, `createRoof`, `createDataTag`, `createTitleBlock` and `createCenterMark`) report no `applied`.
- [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) reports `applied` only with `params`; with `name` and `value` it returns `ok`. [`editStory`](DocumentAccess.md#editstory) reports it (with `story`) only when it edits the story that `name` gives: a call that changes only `levelTypes` or `defaultStoryLevels`, and a call with `delete`, have none. [`editResource`](Resources.md#editresource) reports it only for `action` `modify`.
- The key is not always the name of the argument. A nested argument is flattened: [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) and [`editClass`](DocumentAccess.md#editclass) report `pen.foreColor` as `penForeColor`. The Result of [`setObjectAttributes`](ObjectPrimitives.md#setobjectattributes) lists all its keys; a flag there that acts only as `true` has no entry when it is `false`.
- [`copyAttributes`](ObjectPrimitives.md#copyattributes) reports `applied` inside each entry of `results`. For the category `variable`, [`setPreferences`](DocumentAccess.md#setpreferences) reports `applied` as one boolean, next to `selector`. [`applyResource`](Resources.md#applyresource) reports the single value `true` (a failure is an `err`). [`editWorksheet`](Resources.md#editworksheet) reports a list with one entry per action.

## Plug-in parameters

Plug-in objects (doors, windows, plants, lighting devices, data tags and many more) keep their settings in parameters, named by their universal (not localized) names. Use [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo) to see which plug-in an object is (`parametricName`) and [`getPluginDefinition`](ObjectPrimitives.md#getplugindefinition) to see the parameters a plug-in has.

### Reading parameters

- [`getObjectParameters`](ObjectPrimitives.md#getobjectparameters) returns every parameter, or the ones in `names`, as display strings, and with `includeDefinitions` the type, localized name and pop-up choices of each.
- The `params` argument of [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject), [`getLandmarkObject`](ObjectsLandmark.md#getlandmarkobject), [`getLightingDevice`](ObjectsSpotlight.md#getlightingdevice) takes an array of parameter names and returns their exact, typed values:

| Parameter type | JSON value |
|---|---|
| Real, dimension, coordinate, angle, area, volume | number: lengths in world units, angles in degrees |
| Integer, dimension standard pop-up | integer |
| Boolean | `true` or `false` |
| Any other type (text, pop-up, ...) | string |

### Writing parameters

- [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) writes one parameter (`name` and `value`; the type comes from the parameter definition, or from `type`: `real`/`number`, `int`/`integer`, `bool`/`boolean`, otherwise text) or several at once with `params`.
- A `params` object `{ "ParamName": value }` writes parameters by universal name in [`createPluginObject`](ObjectPrimitives.md#createpluginobject), [`createDataTag`](ObjectsAnnotation.md#createdatatag), [`createTitleBlock`](ObjectsAnnotation.md#createtitleblock), [`setAnnotationObject`](ObjectsAnnotation.md#setannotationobject), [`createLinearDimension`](ObjectsAnnotation.md#createlineardimension), [`createAngularDimension`](ObjectsAnnotation.md#createangulardimension), [`createArcLengthDimension`](ObjectsAnnotation.md#createarclengthdimension), [`createRadialDimension`](ObjectsAnnotation.md#createradialdimension), [`setDimension`](ObjectsAnnotation.md#setdimension), [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject), [`setLandmarkObject`](ObjectsLandmark.md#setlandmarkobject), [`createLightingDevice`](ObjectsSpotlight.md#createlightingdevice), [`setLightingDevice`](ObjectsSpotlight.md#setlightingdevice).
- [`setObjectParameter`](ObjectPrimitives.md#setobjectparameter) and [`createPluginObject`](ObjectPrimitives.md#createpluginobject) write values the same way: a real parameter takes a number or a numeric string such as `"5"`, an integer parameter a whole number or a whole numeric string (`2.5` does not fit), a boolean parameter only `true` or `false`, and any other parameter text; a number or a boolean given for such a parameter is written as its text (`5` becomes `"5"`), and the object is regenerated afterwards. The two tools handle a value that does not fit the type of its parameter, or an unknown parameter name, differently. `setObjectParameter` does not write it and reports `false` for it (in `applied`, or as `ok`); the call still succeeds and its other values are written. `createPluginObject` checks every name and value before it creates anything: one that does not fit refuses the whole call (`these 'params' values do not fit the type of their parameter: …`), so nothing is created and no `applied` is reported. Only a parameter that the new object does not take after its creation (for example one that its plug-in style sets) fails the call later: its `err` names the parameters, the result still carries `applied` with `false` for them, and the call is rolled back (`rolledBack`).
- [`setArchitectureObject`](ObjectsArchitect.md#setarchitectureobject) takes reals in world units, the form in which [`getArchitectureObject`](ObjectsArchitect.md#getarchitectureobject) reads them with `params`, so a value that was read can be written back unchanged.

## Paging

Tools that can return long lists return them page by page. They take the same paging arguments:

| Argument | Type | Meaning |
|---|---|---|
| `limit` | integer | The maximum number of items in this page; at least 1. The default depends on the tool (see below). |
| `offset` | integer | The number of items to skip; not negative. Default 0. |
| `countOnly` | boolean | Return only the count and the paging keys, without the items. Default false. |

and report the same paging keys next to the items:

| Key | Meaning |
|---|---|
| `count` | The total number of items (or matches). |
| `returned` | The number of items in this page. |
| `offset` | The offset of this page. |
| `limit` | The limit used. |
| `truncated` | `true` when more items follow. |
| `nextOffset` | The `offset` of the next page; only present when `truncated` is true. |

To read a whole list, call the tool again with `offset` set to `nextOffset` until `truncated` is false. To count or to check existence, use `countOnly`.

A wrong paging argument is refused before anything is read; these are the paging errors: `'limit' must be a number`, `'offset' must be a number`, `'countOnly' must be true or false`, `'limit' must be at least 1` and `'offset' must not be negative`.

**Paged tools**

| Tool | Items key | Default limit |
|---|---|---|
| [`listIFCMappingObjects`](IFC.md#listifcmappingobjects) | `objects` | 200 |
| [`findMenuCommands`](MenuAccess.md#findmenucommands) | `commands` | 50 |
| [`getMenus`](MenuAccess.md#getmenus) | `menus`, `entries` or `items` | 100 |
| [`findObjects`](ObjectPrimitives.md#findobjects) | `objects` | 200 |
| [`getObjectsAtPoint`](ObjectPrimitives.md#getobjectsatpoint) | `objects` | 50 |
| [`get3DGeometry`](Objects3D.md#get3dgeometry) | `items`, in each list | 100 |
| [`listConnectCADSignals`](ObjectsConnectCAD.md#listconnectcadsignals) | `signals` | 500 |
| [`listConnectCADConnectors`](ObjectsConnectCAD.md#listconnectcadconnectors) | `connectors` | 500 |
| [`listGDTFs`](ObjectsSpotlight.md#listgdtfs) | `gdtfs` | 200 |
| [`getOIPControls`](OIPAccess.md#getoipcontrols) | `controls` | 100 |
| [`getResources`](Resources.md#getresources) | `resources` | 200 |
| [`getWorksheet`](Resources.md#getworksheet) | `cells` or `subrows` | 200 cells, 100 subrows |
| [`listScripts`](Scripting.md#listscripts) | `scripts` | 200 |
| [`getTools`](ToolAccess.md#gettools) | `tools` | 100 |

**Paged lists inside a result**

Some results contain a list that is paged with arguments of its own. Each such list is an object with the paging keys and the items:

| Tool | List | Arguments | Items key | Default limit |
|---|---|---|---|---|
| [`getObjectInfo`](ObjectPrimitives.md#getobjectinfo) | `members` | `memberLimit`, `memberOffset` | `objects` | 50 |
| [`getText`](ObjectPrimitives.md#gettext) | `lines` | `lineLimit`, `lineOffset` | `items` | 100 |
| [`getText`](ObjectPrimitives.md#gettext) | `styleRuns` | `runLimit`, `runOffset` | `items` | 100 |

## Effects and risk levels

Every tool has an **effect**, which says what it may change, and a **risk level**, which says how carefully a client should treat it. Both are shown with each tool. The tool list reports the effect to MCP clients through the standard tool annotations `readOnlyHint` and `destructiveHint`. A higher risk level means a call can change more or is harder to undo; the server reports it in the `safetyLevel` field.

| Effect | Meaning | Risk level | Annotations | Undo | In runToolBatch | Tools |
|---|---|---|---|---|---|---|
| Read-only | Reads the drawing or the application state and changes nothing. | low | `readOnlyHint`: true | none | allowed | 58 |
| Edit | Changes the drawing. Undo reverts the change. | low or medium | `readOnlyHint`: false | one step "MCP: &lt;tool&gt;" | yes | 86 |
| Interactive | Operates the user interface like a user: tool palettes or the Object Info palette. | medium | `readOnlyHint`: false | recorded by Vectorworks as for user input | no | 7 |
| Interactive, destructive | Runs a menu command as if the user chose it. | high | `readOnlyHint`: false, `destructiveHint`: true | recorded by the menu command | no | 1 |
| Script run | Runs a Python script, which can do anything a script can do. | high | `readOnlyHint`: false, `destructiveHint`: true | one step "MCP: script" (none when the script registered no change) | no | 2 |

The three meta-tools of the [Core group](#core-group) are not counted in this table. [`listToolGroups`](#listtoolgroups) is read-only. [`activateToolGroups`](#activatetoolgroups) is a **session setting**: it changes which tool groups the server offers, not the drawing (annotations `readOnlyHint`: true, `destructiveHint`: false). [`runToolBatch`](#runtoolbatch) is an **edit (batch)**: it runs other tools in one undo step (annotations `readOnlyHint`: false, `destructiveHint`: false; risk level medium).

**Risk levels**

- **low**: reads, session changes (such as which tool groups are active), and the plain edits of the document settings and of 2D primitives and text ([Document](DocumentAccess.md#document), [IFC](IFC.md#ifc), [IFC Data Mapping](IFC.md#ifc-data-mapping), [Draw2D](ObjectPrimitives.md#draw2d)). Edit > Undo reverts the edits.
- **medium**: edits of objects, 3D geometry, annotation and industry objects, resources and worksheets, and the interactive tools that operate the tool palettes and the Object Info palette. Edit > Undo reverts them.
- **high**: menu commands and scripts, which may make far-reaching changes that are hard to predict. Clients should ask the user before each call. These tools cannot run inside [`runToolBatch`](#runtoolbatch).

Each group has a risk level, shown on its page. A tool reports its own level: read-only tools are always low, interactive tools medium, menu commands and scripts high, and the other edit tools take the level of their group unless the tool sets its own. The level that the [InteractiveTools](ToolAccess.md#interactivetools) group shows (high) is therefore the level of none of its tools: its read-only tools are low and its interactive tools medium.

**Tools with a special effect**

- Interactive: [`setOIPValues`](OIPAccess.md#setoipvalues), [`pressOIPButton`](OIPAccess.md#pressoipbutton), [`activateTool`](ToolAccess.md#activatetool), [`setToolMode`](ToolAccess.md#settoolmode), [`setToolModes`](ToolAccess.md#settoolmodes), [`sendToolPointer`](ToolAccess.md#sendtoolpointer), [`sendToolAction`](ToolAccess.md#sendtoolaction).
- Interactive, destructive: [`runMenuCommand`](MenuAccess.md#runmenucommand).
- Script run: [`runPythonScript`](Scripting.md#runpythonscript), [`runScript`](Scripting.md#runscript).

## Undo

- **Edit tools**: each successful call is one undo step named `MCP: <tool>`, for example `MCP: createWall`. Edit > Undo reverts it, and Vectorworks shows the name in its status message.
- **Failed calls**: when an edit call fails, the changes that it registered for undo are reverted and the result reports `rolledBack` (`true` when the revert worked, `false` when it did not). A change that a tool did not register cannot be reverted. Tools that record their own undo step (the interactive tools and `runMenuCommand`) are never rolled back.
- **Read-only tools** add no undo step.
- **Batches**: [`runToolBatch`](#runtoolbatch) runs several calls as one undo step `MCP: <name>`, all or nothing. Inside a batch each call joins that step; when one fails, the batch stops and everything it did is reverted.
- **Interactive tools** ([`runMenuCommand`](MenuAccess.md#runmenucommand), [`setOIPValues`](OIPAccess.md#setoipvalues), [`pressOIPButton`](OIPAccess.md#pressoipbutton), [`activateTool`](ToolAccess.md#activatetool), [`setToolMode`](ToolAccess.md#settoolmode), [`setToolModes`](ToolAccess.md#settoolmodes), [`sendToolPointer`](ToolAccess.md#sendtoolpointer), [`sendToolAction`](ToolAccess.md#sendtoolaction)) are recorded by Vectorworks the same way as the user's own actions, so Edit > Undo reverts them as it would for the user.
- **Scripts** ([`runPythonScript`](Scripting.md#runpythonscript), [`runScript`](Scripting.md#runscript)) run in one undo step `MCP: script`. The step is kept after a successful run, or one that waits for user input, and reverted after a failed run (`rolledBack`). Vectorworks keeps no empty step, so a run that registered no change leaves none (`undoStep` false). The script itself must register what it creates and changes, otherwise Undo cannot revert it.
