**English** • [Deutsch](../../MCP.de/v2027.2/ObjectsAnnotation.md) • [日本語](../../MCP.ja/v2027.2/ObjectsAnnotation.md)

# ObjectsAnnotation — annotation and dimensions

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools for annotations: data tags, title block borders and the title block project data, and dimensions with center marks.

## Table of contents

- [Overview](#overview)
- [Annotation](#annotation)
  - [createDataTag](#createdatatag)
  - [createTitleBlock](#createtitleblock)
  - [getAnnotationObject](#getannotationobject)
  - [setAnnotationObject](#setannotationobject)
  - [tagObject](#tagobject)
  - [getObjectTags](#getobjecttags)
  - [getProjectData](#getprojectdata)
  - [setProjectData](#setprojectdata)
- [Dimensioning](#dimensioning)
  - [createLinearDimension](#createlineardimension)
  - [createAngularDimension](#createangulardimension)
  - [createArcLengthDimension](#createarclengthdimension)
  - [createRadialDimension](#createradialdimension)
  - [createCenterMark](#createcentermark)
  - [getDimension](#getdimension)
  - [setDimension](#setdimension)
  - [getObjectDimensions](#getobjectdimensions)

## Overview

This folder holds 2 tool groups with 16 tools in total.

| Group | Group ID | Active by default | Safety level | Tools | Summary |
|---|---|---|---|---|---|
| [Annotation](#annotation) | `annotation` | No | medium | 8 | Data tags, title block borders and the title block project data of the document. |
| [Dimensioning](#dimensioning) | `dimensioning` | No | medium | 8 | Linear, angular, arc length and radial dimensions, and center marks. |

## Annotation

> **Group:** `Annotation` · **Group ID:** `annotation` · **Active by default:** No · **Safety level:** medium · **Tools:** 8

**Data tags, title block borders and the title block project data of the document.**

Annotate the drawing with data tags and title block borders. A data tag labels an object with data read out of that object (record fields, plug-in parameters, class, ...); a title block border draws the sheet border, the zone grid and the title block that prints the project, sheet, revision and issue data. Both objects take their graphics from an object style, which these tools resolve and import from the Vectorworks content when the drawing does not have one yet.

Each change runs as its own named, undoable Vectorworks operation.

| Tool | Effect | Safety | Summary |
|---|---|---|---|
| [`createDataTag`](#createdatatag) | Edit | medium | Creates a data tag, optionally attached to an object. |
| [`createTitleBlock`](#createtitleblock) | Edit | medium | Creates a title block border. |
| [`getAnnotationObject`](#getannotationobject) | Read-only | low | Reads a data tag or a title block border. |
| [`setAnnotationObject`](#setannotationobject) | Edit | medium | Edits a data tag or a title block border. |
| [`tagObject`](#tagobject) | Edit | medium | Attaches a data tag to an object, or detaches it. |
| [`getObjectTags`](#getobjecttags) | Read-only | low | Lists the data tags attached to an object. |
| [`getProjectData`](#getprojectdata) | Read-only | low | Reads the title block project data of the document. |
| [`setProjectData`](#setprojectdata) | Edit | medium | Writes the title block project data of the document. |

### createDataTag

Creates a data tag, optionally attached to an object.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createDataTag" · **In runToolBatch:** yes

**Details**

Create a data tag at `position`. `taggedObjectUuid` is the object the tag reads its data from (it starts empty without one; use tagObject later). Optional `style` names the data tag style (a symbol definition) that supplies the tag's text layout; it is imported from the Vectorworks content when it is not in the drawing yet, and any available style is used when it is omitted or not found - the style actually applied is returned as `style`.

Optional `useLeader`, `leaderLength`, `leaderAngle` (radians), `leaderEnd` (the point the leader points at) and raw plug-in `params`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point. |
| `taggedObjectUuid` | string |  | UUID of the object the tag reads its data from. Only a UUID is accepted. |
| `style` | string |  | Name of the data tag style (a symbol definition). Imported when needed. When it is omitted or not found, any available style is used. |
| `useLeader` | boolean |  | Whether the tag has a leader. |
| `leaderLength` | number |  | Length of the leader, in world units. |
| `leaderAngle` | number |  | Radians. |
| `leaderEnd` | [point](Common.md#points) |  | The point the leader points at. |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. See [Plug-in parameters](Common.md#plug-in-parameters). The result of each write is not reported: a name or value that is refused is ignored without an error. A `params` that is not an object is ignored. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new data tag (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `style` | Name of the style that is applied. It differs from the requested `style` when that one was not found. Left out when the name cannot be read. |
| `taggedObject` | Reference of the object that the tag is attached to. Only when the tag is attached. |

There is no `applied`. Errors: `object to tag not found` (no object has the `taggedObjectUuid`); `failed to create data tag: a usable data tag style is required in the drawing or Vectorworks content, and any requested tagged object must support association` (this also covers an object that cannot be tagged; see `canBeTagged` of [`getObjectTags`](#getobjecttags)); `failed to set data tag leader properties` (Vectorworks refused `useLeader`, `leaderLength`, `leaderAngle` or `leaderEnd`; the new tag is deleted). A failed call is rolled back (`rolledBack`).

### createTitleBlock

Creates a title block border.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createTitleBlock" · **In runToolBatch:** yes

**Details**

Create a title block border at `position`, normally on a sheet layer. Optional `style` names the title block border style that supplies the title block graphics; it is imported from the Vectorworks title block content when it is not in the drawing yet, and any available style is used when it is omitted or not found - the style actually applied is returned as `style`.

Optional `sheetSize` (e.g. "ANSI D", "ISO A1"), `sheetWidth`/`sheetHeight` for a custom size, `showGrids`, a `sheetData` object of field name / value pairs (sheet title, sheet number, drawn by, ...) and raw plug-in `params`.

> **Note:** The call does not check whether Vectorworks took a value. One that is refused, such as a `sheetData` field that is not in the sheet data format, is ignored without an error. A `sheetData` or `params` that is not an object is ignored too.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point. |
| `style` | string |  | Name of the title block border style (a symbol definition). Imported from the Vectorworks title block content when needed. When it is omitted or not found, any available style is used. |
| `sheetSize` | string |  | Name of a predefined sheet size, for example `ANSI D` or `ISO A1`. |
| `sheetWidth` | number |  | Width of a custom sheet size, in world units. Only meaningful when the object uses a custom size. |
| `sheetHeight` | number |  | Height of a custom sheet size, in world units. Only meaningful when the object uses a custom size. |
| `showGrids` | boolean |  | Whether the zone grids are shown. |
| `sheetData` | object |  | Sheet data `{ "<field name>": value }`. Only the fields of the document's sheet data format are written; [`getAnnotationObject`](#getannotationobject) lists them as `sheetDataFieldNames`. A value that is not a string is stored as its JSON text. |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. See [Plug-in parameters](Common.md#plug-in-parameters). The result of each write is not reported: a name or value that is refused is ignored without an error. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new title block border (see [Object references](Common.md#object-references)) and `style`, the name of the style that is applied. It differs from the requested `style` when that one was not found, and is left out when the name cannot be read. There is no `applied`. Errors: `failed to create title block border: no title block border style is available in the drawing or in the Vectorworks content (a title block needs a style to get its graphics from)`. A failed call is rolled back (`rolledBack`).

### getAnnotationObject

Reads a data tag or a title block border.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read a data tag or a title block border by uuid, name or index. Both report the `style` name, `isStyled` and the style resource (a symbol definition) as `styleResource`. A data tag reports its leader (`useLeader`, `leaderType`, `leaderLength`, `leaderAngle`, `shoulderLength`, `useMarker`, `leaderEnd`), its placement (`offset`, `horizontalPosition`, `moveBehaviour`, `alignToWalls`), eligibility criteria, the object it tags and the `data` it currently prints.

A title block border reports its sheet size and `margins`, zone grid (`showGrids`, `horizontalZones`, `verticalZones`, `drawCropMarks`), `useAsTitleBlock`, `isActiveTitleBlock`, north arrow (`displayNorthArrow`, `northAngle`), drawing stamp (`displayDrawingStamp`, `drawingStampText`), sheet id/title/date, its `sheetData` with the `sheetDataFieldNames` of the sheet data format, and the document's `projectData` and `revisions`.

Settings use the same keys, units and enum values as setAnnotationObject.

> **Note:** The keys `kind`, `isStyled`, `styleResource`, `taggedObject`, `data`, `sheetID`, `sheetTitle`, `sheetDate`, `latestIssueDate`, `revisions` and `sheetDataFieldNames` only describe the object. [`setAnnotationObject`](#setannotationobject) ignores them; use [`tagObject`](#tagobject) to change `taggedObject`. The eligibility criteria are reported as `useCriteria` and `criteria`, and the sheet size as `sheetSize`, `sheetWidth` and `sheetHeight`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |

**Result**

The object reference (see [Object references](Common.md#object-references)) and the keys below. A value that Vectorworks cannot read is left out, for example `leaderEnd` when the tag has no leader.

| Key | Description |
|---|---|
| `kind` | `DataTag` or `TitleBlockBorder`. |
| `style`, `isStyled`, `styleResource` | The style name, whether the object is styled, and the style resource (a symbol definition). |
| `taggedObject` | Data tag only, and only when it is attached: the reference of the tagged object. |
| `data` | Data tag only: `{ "<label>": "<printed text>" }`, the data that the tag currently prints. |
| `sheetID`, `sheetTitle`, `sheetDate` | Title block border only. |
| `latestIssueDate` | Title block border only, and only when an issue was made. |
| `sheetData` | Title block border only: `{ "<field>": "<value>" }` of the sheet data format. `sheetDataFieldNames` lists the field names. |
| `projectData` | Title block border only: the document-wide project data, the same `projectData` that [`getProjectData`](#getprojectdata) returns. |
| `revisions` | Title block border only: an array of `{ number, date, note, publishDate, recipients }`. |

The other keys are named in the Details above; lengths are in world units and angles in radians. Errors: `object not found`; `not an annotation object (expected a Data Tag or a Title Block Border)`.

### setAnnotationObject

Edits a data tag or a title block border.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: setAnnotationObject" · **In runToolBatch:** yes

**Details**

Edit a data tag or a title block border by uuid.

**Both kinds:** `style` (imported when needed), or `removeStyle`: true to detach the object from its style - applied first; every parameter then keeps its current value and becomes editable per instance.

**Data tag:** `useLeader`, `leaderType`, `leaderLength`, `leaderAngle` (radians), `shoulderLength`, `useMarker` (marker at the leader end), `leaderEnd`, `offset`, `horizontalPosition` (side of the leader the text sits on), `moveBehaviour` (what dragging the tag moves), `alignToWalls`, `useCriteria`, `criteria`.

**Title block border:** `sheetSize`, `sheetWidth`, `sheetHeight`, `margins` (an omitted side keeps its value), `showGrids`, `horizontalZones`, `verticalZones`, `drawCropMarks`, `useAsTitleBlock`, `isActiveTitleBlock` (the title block whose sheet data the document reads, one per sheet), `displayNorthArrow`, `northAngle` (radians), `displayDrawingStamp`, `drawingStampText` (printed when the 'Stamp Text' parameter selects the custom entry), `sheetData` and `projectData` objects of field name / value pairs. A `params` object sets raw plug-in parameters. `applied` reports for each setting whether it was written.

> **Note:** The object is found by `uuid`, then `name`, then `index`; the Details name only `uuid`. A setting that the kind of the object does not have is ignored: a data tag ignores `sheetSize` and the other title block border keys, and a title block border ignores the data tag keys.

> **Note:** A value of the wrong type is handled by the key. `leaderType`, `useMarker`, `horizontalPosition`, `moveBehaviour`, `alignToWalls`, `drawCropMarks`, `isActiveTitleBlock`, `displayNorthArrow` and `displayDrawingStamp` write nothing and report `false` when the value has the wrong type (an unknown enum name counts as one). All other keys except `removeStyle`, `margins`, `sheetData`, `projectData` and `params` (see their rows) convert the value without a check: a missing or wrong-typed number becomes 0, a boolean `false`, a string empty text and a point the origin. That value is written, and `applied` reports whether Vectorworks took it (usually `true`). A `removeStyle` that is not a boolean counts as `false`: nothing is detached and `applied` has no `removeStyle` entry. Send every key with its documented type.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `style` | string |  | Name of a style (a symbol definition). The style in the drawing is used first, then the Vectorworks content (imported when needed). A name that is found nowhere does not fail: another style of the object kind is applied instead and `applied.style` stays `true`. It is `false` only when no style is available at all. |
| `useLeader` | boolean |  | Used for data tag. |
| `leaderLength` | number |  | Used for data tag. World units. |
| `leaderAngle` | number |  | Used for data tag. Radians. |
| `shoulderLength` | number |  | Used for data tag. World units. |
| `leaderEnd` | [point](Common.md#points) |  | Used for data tag. |
| `offset` | [point](Common.md#points) |  | Used for data tag. |
| `useCriteria` | boolean |  | Used for data tag. |
| `criteria` | string |  | Used for data tag. |
| `removeStyle` | boolean |  | For both kinds. `true` detaches the object from its style before the other settings are written: every parameter keeps its value and can then be edited per instance. `false` does nothing. A `style` in the same call applies a style again. |
| `leaderType` | string |  | Used for data tag. One of: `line`, `arc`, `bezier`. |
| `useMarker` | boolean |  | Used for data tag. Marker at the leader end. |
| `horizontalPosition` | string |  | Used for data tag. One of: `left`, `right`, `auto`. |
| `moveBehaviour` | string |  | Used for data tag. One of: `entireTag`, `leaderEnd`. |
| `alignToWalls` | boolean |  | Used for data tag. |
| `sheetSize` | string |  | Used for title block border. Name of a predefined sheet size, for example `ANSI D` or `ISO A1`. |
| `sheetWidth` | number |  | Used for title block border. World units. Only meaningful when the object uses a custom sheet size. |
| `sheetHeight` | number |  | Used for title block border. World units. Only meaningful when the object uses a custom sheet size. |
| `showGrids` | boolean |  | Used for title block border. |
| `horizontalZones` | integer |  | Used for title block border. |
| `verticalZones` | integer |  | Used for title block border. |
| `useAsTitleBlock` | boolean |  | Used for title block border. |
| `northAngle` | number |  | Used for title block border. Radians. |
| `margins` | object |  | Used for title block border. The four margin widths `{ "left": n, "right": n, "top": n, "bottom": n }`, in world units. It is not a [rectangle](Common.md#rectangles): `top` and `bottom` are widths, not positions. An omitted side keeps its value. When `margins` is not an object or a side is not a number, nothing is written and `applied.margins` is `false`. |
| `drawCropMarks` | boolean |  | Used for title block border. |
| `isActiveTitleBlock` | boolean |  | Used for title block border. The title block whose sheet data the document reads, one per sheet. |
| `displayNorthArrow` | boolean |  | Used for title block border. |
| `displayDrawingStamp` | boolean |  | Used for title block border. |
| `drawingStampText` | string |  | Used for title block border. Printed when the 'Stamp Text' parameter selects the custom entry. |
| `sheetData` | object |  | Used for title block border. Sheet data `{ "<field name>": value }`. A field that is not in the sheet data format is not written (`applied.sheetData` has `false` for it); [`getAnnotationObject`](#getannotationobject) lists the fields as `sheetDataFieldNames`. A value that is not a string is stored as its JSON text. |
| `projectData` | object |  | Used for title block border. Field name / value pairs of the document-wide project data that every title block shares. It writes the same data as [`setProjectData`](#setprojectdata): only fields of the project data format are written, and a value that is not a string is stored as its JSON text. |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. See [Plug-in parameters](Common.md#plug-in-parameters). |

**Result**

`{ "applied": { … } }`. `applied` has an entry for each setting that was given:

| Entry | Description |
|---|---|
| `<setting>` | `true` when Vectorworks took the value; `false` when it refused it or the value could not be converted to the type of the setting. |
| `removeStyle` | Only when `removeStyle` was `true`: whether the object was detached from its style. |
| `sheetData` | Title block border only: `{ "<field name>": true or false }`, one entry for each field that was given. |
| `projectData` | Title block border only: the same for the project data. |
| `params` | `{ "<name>": true or false }` for the raw plug-in parameters. |

A setting that the kind of the object does not have has no entry. A `sheetData`, `projectData` or `params` that is not an object is ignored. The call succeeds even when every entry is `false`. Errors: `object not found`; `not an annotation object (expected a Data Tag or a Title Block Border)`. A failed call is rolled back (`rolledBack`).

### tagObject

Attaches a data tag to an object, or detaches it.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: tagObject" · **In runToolBatch:** yes

**Details**

Attach the data tag given by uuid/name/index to the object given by `objectUuid` so the tag reads its data from it, or detach it again with `action` set to "detach".

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `objectUuid` | string |  | UUID of the target object. Required to attach, and only a UUID is accepted. Not used to detach. |
| `action` | string |  | One of: `attach`, `detach`. The default is `attach`; any other value attaches too. |

**Result**

| Action | Result |
|---|---|
| attach | `{ "attached": true, "taggedObject": <object reference> }`. The tag now reads its data from the object; its former association is replaced. |
| detach | `{ "detached": <boolean> }`: `true` when the tag had a tagged object to detach (Vectorworks does not report whether it detached it); `false` when it had none. |

Errors: `data tag not found` (the reference gives no object, or the object is not a data tag); `object to tag not found (provide 'objectUuid')`; `this kind of object cannot be tagged by a data tag` (see `canBeTagged` of [`getObjectTags`](#getobjecttags)); `failed to attach the data tag to the object`. A failed call is rolled back (`rolledBack`).

### getObjectTags

Lists the data tags attached to an object.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the data tags attached to the object given by uuid, name or index, and report whether that kind of object can be tagged at all.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |

**Result**

| Key | Description |
|---|---|
| `object` | Reference of the object (see [Object references](Common.md#object-references)). |
| `canBeTagged` | Whether a data tag can be attached to this kind of object. |
| `tags` | Array of the references of the data tags that are attached to the object; empty when there are none. |

Errors: `object not found`.

### getProjectData

Reads the title block project data of the document.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the title block project data of the document: the named fields shared by every title block, such as project name, client and address. Returns `projectData` (field name / value pairs) and `projectDataFieldNames` (the fields of the document's project data format, in format order). Takes no arguments.

**Parameters**

This tool takes no parameters.

**Result**

| Key | Description |
|---|---|
| `projectData` | Field name / value pairs of the project data. |
| `projectDataFieldNames` | Array of the field names of the project data format, in format order. |

Errors: `this document has no title block project data (it is created with the first title block border)`. This also covers project data without fields.

### setProjectData

Writes the title block project data of the document.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: setProjectData" · **In runToolBatch:** yes

**Details**

Write the title block project data of the document. `projectData` is an object of field name / value pairs; only fields that already exist in the project data format (see getProjectData) are written. Every title block in the drawing is refreshed afterwards.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `projectData` | object | Yes | Field name / value pairs `{ "<field name>": value }`. Only fields of the project data format (see [`getProjectData`](#getprojectdata)) are written. A value that is not a string is stored as its JSON text. |

**Result**

`{ "applied": { "<field name>": true or false } }`, one entry for each field that was given. A field that is not in the project data format is `false` and is not created. Errors: `provide 'projectData' as an object of field name / value pairs` (the argument is missing or not an object). A failed call is rolled back (`rolledBack`).

## Dimensioning

> **Group:** `Dimensioning` · **Group ID:** `dimensioning` · **Active by default:** No · **Safety level:** medium · **Tools:** 8

**Linear, angular, arc length and radial dimensions, and center marks.**

Measure and annotate the drawing with dimensions: linear (constrained, horizontal, vertical, unconstrained/sloped and ordinate), angular, arc length and radial/diametrical dimensions, plus center marks. A dimension is a native Vectorworks object, not a plug-in object: it measures two world points (a vertex and two legs for an angular one, a centre and a circle for a radial one) and prints the measured value using a dimension standard.

The kind of a dimension is fixed when it is created - a linear dimension can never become an angular one - so pick the right create tool up front. The dimension standard (an ISO/ANSI/architectural/custom preset stored in the document) supplies the arrowheads, witness line lengths, text size and the way the value is formatted; those lengths are page lengths, so a dimension keeps the same printed size on any layer scale, while `offset`, the point coordinates and the measured value are always world units.

`unit` picks which of the document's dimension unit settings formats the value. Text can be replaced or extended with `leaderText`/`trailerText`/`noteText` and a second value in a secondary unit can be printed next to the first one. A dimension can be associative: with `associate` it is bound to the geometry under its end points (`associateSelectedOnly` limits that to the selected objects) and follows it when that geometry moves.

All angles in this group are radians. A center mark is not a dimension object but a group of line segments placed in the dimension class, so it is read and edited with the generic object tools. Each change runs as its own named, undoable Vectorworks operation. The create tools also return `applied` (true/false per setting written, including `associate`) when settings were given.

> **Note:** The create tools return the object reference (see [Object references](Common.md#object-references)), the common dimension keys as [`getDimension`](#getdimension) returns them (`kind`, `start`, `end`, `offset`, `measuredLength` and every setting) and a few keys of the kind, which each tool lists. `applied` is present only when a setting was written. It reports `start` and `end` given together as `points` (a single one as `start` or `end`), `offset`, and each other setting by name. It reports `associate` only when `associate` was `true`, and it never reports `params`, the radial `compact` or the angular `referenceAngle`. `createCenterMark` returns no `applied`.

> **Note:** `applied.associate` is `true` whenever `associate` was requested, even when nothing could be bound: the call that binds the dimension returns no result. To check the binding, call [`getObjectDimensions`](#getobjectdimensions) on the measured object. [`setDimension`](#setdimension) reports `false` for `associate: false`; no tool removes an association.

> **Note:** The arguments are not type-checked. A value of the wrong type is read as an empty string, 0, `false` or the point (0, 0), and that fallback value is passed to the setter, so the setting is reported as applied unless the fallback value itself is refused (`fontSize`, `standard`, `standardIndex`, and in `setDimension` also `associate` and radial `radius` / `diameter`): `"leaderText": 5` clears the text, `"boxText": "yes"` writes `false`, and `"start": "1,2"` moves the point to (0, 0). Send the types that the Parameters tables show.

> **Note:** Units: `startWitnessLength`, `endWitnessLength`, `startWitnessOffset`, `endWitnessOffset`, `textOffsetAlongLine`, `textOffsetAboveLine`, `tolerancePlus` and `toleranceMinus` are world units, like `offset`. Only the values that the dimension standard supplies are page lengths. `fontSize` is in points.

> **Note:** These values are refused: nothing is written and `applied` reports `false` for the setting. A `witnessOverride` outside 0 to 4, a negative `precision` or `secondaryPrecision`, `fontSize` of 0 or less, a negative `fontStyle`, a `textRotation` outside 0 to 2, an empty `standard`, a `standardIndex` of 0, a negative `unit`, a radial `radius` or `diameter` of 0 or less in `setDimension`, and a `textStyle` name that no named object has (`textStyle` takes a name, never a UUID, and the object found is not checked to be a text style). A `toleranceType` outside 0 to 3 is written and reported as applied, but the dimension then reports no `toleranceType`; send 0 to 3. Setting `textOffsetAlongLine` also switches `textPositionAutomatic` off.

| Tool | Effect | Safety | Summary |
|---|---|---|---|
| [`createLinearDimension`](#createlineardimension) | Edit | medium | Creates a constrained, horizontal, vertical, unconstrained or ordinate linear dimension. |
| [`createAngularDimension`](#createangulardimension) | Edit | medium | Creates an angular dimension. |
| [`createArcLengthDimension`](#createarclengthdimension) | Edit | medium | Creates an arc length dimension. |
| [`createRadialDimension`](#createradialdimension) | Edit | medium | Creates a radial or diametrical dimension. |
| [`createCenterMark`](#createcentermark) | Edit | medium | Creates a center mark for a circular feature. |
| [`getDimension`](#getdimension) | Read-only | low | Reads a dimension: its kind, measured points, value and text settings. |
| [`setDimension`](#setdimension) | Edit | medium | Edits a dimension. |
| [`getObjectDimensions`](#getobjectdimensions) | Read-only | low | Lists the dimensions associated with an object. |

### createLinearDimension

Creates a constrained, horizontal, vertical, unconstrained or ordinate linear dimension.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createLinearDimension" · **In runToolBatch:** yes

**Details**

Create a linear dimension measuring the distance between `start` and `end`, its dimension line placed `offset` world units away from them. `mode` picks the kind: "constrained" (default) measures the distance projected onto a fixed direction - `angle` (radians) gives that direction, otherwise it follows start → end; "horizontal" and "vertical" are the axis-aligned shortcuts; "unconstrained" (sloped) measures the true distance along start → end; "ordinate" measures `end` from the datum `start` along `angle`.

The two points must not coincide.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `start` | [point](Common.md#points) | Yes | First measured point, in world units. |
| `end` | [point](Common.md#points) | Yes | Second measured point, in world units. |
| `offset` | number |  | Distance of the dimension line from the measured geometry, in world units. Positive: the dimension line is on the left of the start → end direction; negative: on the right. |
| `angle` | number |  | Angle in radians, counter-clockwise. `constrained`: the fixed direction of the measurement (without it: start → end). `ordinate`: the direction of the measurement axis (without it: 0, the +X axis, not start → end). Ignored by the other modes. |
| `mode` | string |  | One of: `constrained` (default), `horizontal`, `vertical`, `unconstrained` (`sloped` is accepted as an alias), `ordinate`. Any other value fails. |
| `startWitness` | boolean |  | Show the witness line at the start. |
| `endWitness` | boolean |  | Show the witness line at the end. |
| `witnessOverride` | integer |  | Witness lines: 0 by standard, 1 one custom length, 2 a length per witness line, 3 one custom offset, 4 an offset per witness line. |
| `startWitnessLength` | number |  | Custom length of the start witness line. |
| `endWitnessLength` | number |  | Custom length of the end witness line. |
| `startWitnessOffset` | number |  | Custom offset of the start witness line. |
| `endWitnessOffset` | number |  | Custom offset of the end witness line. |
| `arrowsInside` | boolean |  | Place the arrows inside the witness lines. |
| `leaderLine` | boolean |  | Show the leader line. |
| `showValue` | boolean |  | Print the measured value. |
| `leaderText` | string |  | Text printed before the value. |
| `trailerText` | string |  | Text printed after the value. |
| `boxText` | boolean |  | Draw a box around the value. |
| `precision` | integer |  | Decimal digits; fractional units: 0-6 = 1/1 to 1/64; angles: 1 degrees, 2 deg/min, 3 deg/min/sec. |
| `showSecondaryValue` | boolean |  | Also print the value in the secondary unit. |
| `secondaryLeaderText` | string |  | Text printed before the secondary value. |
| `secondaryTrailerText` | string |  | Text printed after the secondary value. |
| `secondaryBoxText` | boolean |  | Draw a box around the secondary value. |
| `secondaryPrecision` | integer |  | Precision of the secondary value (as `precision`). |
| `noteText` | string |  | Note text added to the dimension. |
| `textPositionAutomatic` | boolean |  | Place the text automatically. |
| `textInside` | boolean |  | Place the text inside the witness lines. |
| `textFlipped` | boolean |  | Flip the text. |
| `textRotation` | integer |  | Text rotation: 0 aligned, 1 horizontal, 2 horizontal/vertical. |
| `textOffsetAlongLine` | number |  | Offset of the text along the dimension line. |
| `textOffsetAboveLine` | number |  | Offset of the text above the dimension line. |
| `fontSize` | number |  | Font size in points. |
| `fontStyle` | integer |  | Sum of 1 bold, 2 italic, 4 underline. |
| `textStyle` | string |  | Name of a text style resource; an empty string for none. A UUID is not accepted. `applied.textStyle` is `false` when no named object has that name. |
| `toleranceType` | integer |  | Tolerance: 0 none, 1 single, 2 double, 3 limit. |
| `tolerancePlus` | number |  | Upper tolerance value. |
| `toleranceMinus` | number |  | Lower tolerance value. |
| `standard` | string |  | Name of the dimension standard. |
| `standardIndex` | integer |  | Dimension standard by index: above 0 built-in, below 0 custom. |
| `unit` | integer |  | 0 for document units, otherwise the index of a dimension unit setting. |
| `associate` | boolean |  | Bind the dimension to the geometry under its end points. The result always reports it as applied (see the notes of the [Dimensioning](#dimensioning) group). |
| `associateSelectedOnly` | boolean |  | With `associate`: bind only to selected objects. |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. A dimension is a native object without plug-in parameters, so this has no known use here, and the create tools do not report the outcome. See [Plug-in parameters](Common.md#plug-in-parameters). |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new dimension (see [Object references](Common.md#object-references)), the common dimension keys (see the notes of the [Dimensioning](#dimensioning) group) and:

| Key | Description |
|---|---|
| `value` | The printed value: the distance between the points, projected onto the direction of the dimension line for a constrained dimension. |
| `direction` | Direction of the dimension line, in radians from the X axis (start → end for an unconstrained dimension). |
| `applied` | Per setting written; `start` and `end` are reported together as `points`. |

Errors: `unknown mode: <mode> (expected constrained, horizontal, vertical, unconstrained or ordinate)`; `failed to create the linear dimension (the two points must not coincide)`; `failed to create the dimension`. A failed call is rolled back (`rolledBack`).

### createAngularDimension

Creates an angular dimension.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createAngularDimension" · **In runToolBatch:** yes

**Details**

Create an angular dimension at `vertex` measuring the counter-clockwise angle between the two legs, its arc placed `offset` world units from the vertex. Give the legs either as `firstLegPoint`/`secondLegPoint` (any point on each leg) or as `startAngle`/`endAngle` in radians together with a `legLength`. With `referenceAngle` true the dimension measures a single leg against the reference direction and draws only one witness line. The measured value is returned in radians as `value`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `vertex` | [point](Common.md#points) | Yes | Angular dimensions: the vertex of the angle. |
| `firstLegPoint` | [point](Common.md#points) |  | Any point on the first leg. |
| `secondLegPoint` | [point](Common.md#points) |  | Any point on the second leg. |
| `startAngle` | number |  | Start angle in radians, counter-clockwise. |
| `endAngle` | number |  | End angle in radians, counter-clockwise. |
| `legLength` | number |  | With `startAngle` and `endAngle`: length of the legs, in world units. Default 1; must be greater than 0. |
| `offset` | number |  | Distance of the dimension line from the measured geometry, in world units. |
| `referenceAngle` | boolean |  | Angular dimensions: measure a single leg against the reference direction. |
| `startWitness` | boolean |  | Show the witness line at the start. |
| `endWitness` | boolean |  | Show the witness line at the end. |
| `witnessOverride` | integer |  | Witness lines: 0 by standard, 1 one custom length, 2 a length per witness line, 3 one custom offset, 4 an offset per witness line. |
| `startWitnessLength` | number |  | Custom length of the start witness line. |
| `endWitnessLength` | number |  | Custom length of the end witness line. |
| `startWitnessOffset` | number |  | Custom offset of the start witness line. |
| `endWitnessOffset` | number |  | Custom offset of the end witness line. |
| `arrowsInside` | boolean |  | Place the arrows inside the witness lines. |
| `leaderLine` | boolean |  | Show the leader line. |
| `showValue` | boolean |  | Print the measured value. |
| `leaderText` | string |  | Text printed before the value. |
| `trailerText` | string |  | Text printed after the value. |
| `boxText` | boolean |  | Draw a box around the value. |
| `precision` | integer |  | Decimal digits; fractional units: 0-6 = 1/1 to 1/64; angles: 1 degrees, 2 deg/min, 3 deg/min/sec. |
| `showSecondaryValue` | boolean |  | Also print the value in the secondary unit. |
| `secondaryLeaderText` | string |  | Text printed before the secondary value. |
| `secondaryTrailerText` | string |  | Text printed after the secondary value. |
| `secondaryBoxText` | boolean |  | Draw a box around the secondary value. |
| `secondaryPrecision` | integer |  | Precision of the secondary value (as `precision`). |
| `noteText` | string |  | Note text added to the dimension. |
| `textPositionAutomatic` | boolean |  | Place the text automatically. |
| `textInside` | boolean |  | Place the text inside the witness lines. |
| `textFlipped` | boolean |  | Flip the text. |
| `textRotation` | integer |  | Text rotation: 0 aligned, 1 horizontal, 2 horizontal/vertical. |
| `textOffsetAlongLine` | number |  | Offset of the text along the dimension line. |
| `textOffsetAboveLine` | number |  | Offset of the text above the dimension line. |
| `fontSize` | number |  | Font size in points. |
| `fontStyle` | integer |  | Sum of 1 bold, 2 italic, 4 underline. |
| `textStyle` | string |  | Name of a text style resource; an empty string for none. A UUID is not accepted. `applied.textStyle` is `false` when no named object has that name. |
| `toleranceType` | integer |  | Tolerance: 0 none, 1 single, 2 double, 3 limit. |
| `tolerancePlus` | number |  | Upper tolerance value. |
| `toleranceMinus` | number |  | Lower tolerance value. |
| `standard` | string |  | Name of the dimension standard. |
| `standardIndex` | integer |  | Dimension standard by index: above 0 built-in, below 0 custom. |
| `unit` | integer |  | 0 for document units, otherwise the index of a dimension unit setting. |
| `associate` | boolean |  | Bind the dimension to the geometry under its end points. The result always reports it as applied (see the notes of the [Dimensioning](#dimensioning) group). |
| `associateSelectedOnly` | boolean |  | With `associate`: bind only to selected objects. |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. A dimension is a native object without plug-in parameters, so this has no known use here, and the create tools do not report the outcome. See [Plug-in parameters](Common.md#plug-in-parameters). |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

Give the legs as `startAngle` and `endAngle` together, or as `firstLegPoint` and `secondLegPoint`. The angles are used when both are present; with only one of them, or with neither, the leg points are used.

**Result**

The object reference of the new dimension (see [Object references](Common.md#object-references)), the common dimension keys (see the notes of the [Dimensioning](#dimensioning) group; `start` and `end` are the two leg points) and:

| Key | Description |
|---|---|
| `vertex` | The vertex, in world units. |
| `startAngle` | Start angle of the measured angle, in radians. |
| `endAngle` | End angle of the measured angle, in radians. |
| `value` | The measured angle in radians, counter-clockwise from the first leg to the second, in [0, 2π). |
| `referenceAngle` | Whether the dimension measures against the reference direction. |
| `applied` | Per setting written. |

Errors: `failed to create the angular dimension (the vertex and the two leg points must be distinct)` (also when `legLength` is 0 or less); `failed to create the dimension`. A failed call is rolled back (`rolledBack`).

### createArcLengthDimension

Creates an arc length dimension.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createArcLengthDimension" · **In runToolBatch:** yes

**Details**

Create an arc length dimension measuring the length along an arc, its dimension arc placed `offset` world units outside it. Give the arc either as `start`, `end` and `center` (with `clockwise` choosing which of the two arcs between the points is measured) or as `center`, `radius`, `startAngle` and `sweepAngle` in radians (a negative sweep goes clockwise).

`witnessPerpendicularToChord` draws the witness lines perpendicular to the chord instead of radially; `arcIndicator` (default true) prints the arc symbol in front of the value.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `start` | [point](Common.md#points) |  | First measured point, in world units. Used with `end` and `center`. |
| `end` | [point](Common.md#points) |  | Second measured point, in world units. Used with `start` and `center`. |
| `center` | [point](Common.md#points) | Yes | Center of the arc, in world units. |
| `radius` | number |  | Radius, in world units; must be greater than 0. Used with `startAngle` and `sweepAngle`. |
| `startAngle` | number |  | Start angle in radians, counter-clockwise. |
| `sweepAngle` | number |  | Sweep angle in radians; positive is counter-clockwise, negative is clockwise. Must not be 0. |
| `offset` | number |  | Distance of the dimension line from the measured geometry, in world units. |
| `clockwise` | boolean |  | With `start`, `end` and `center`: measure the clockwise arc between the points. |
| `witnessPerpendicularToChord` | boolean |  | Draw the witness lines perpendicular to the chord instead of radially. Default false. |
| `arcIndicator` | boolean |  | Print the arc symbol in front of the value. Default true. |
| `startWitness` | boolean |  | Show the witness line at the start. |
| `endWitness` | boolean |  | Show the witness line at the end. |
| `witnessOverride` | integer |  | Witness lines: 0 by standard, 1 one custom length, 2 a length per witness line, 3 one custom offset, 4 an offset per witness line. |
| `startWitnessLength` | number |  | Custom length of the start witness line. |
| `endWitnessLength` | number |  | Custom length of the end witness line. |
| `startWitnessOffset` | number |  | Custom offset of the start witness line. |
| `endWitnessOffset` | number |  | Custom offset of the end witness line. |
| `arrowsInside` | boolean |  | Place the arrows inside the witness lines. |
| `leaderLine` | boolean |  | Show the leader line. |
| `showValue` | boolean |  | Print the measured value. |
| `leaderText` | string |  | Text printed before the value. |
| `trailerText` | string |  | Text printed after the value. |
| `boxText` | boolean |  | Draw a box around the value. |
| `precision` | integer |  | Decimal digits; fractional units: 0-6 = 1/1 to 1/64; angles: 1 degrees, 2 deg/min, 3 deg/min/sec. |
| `showSecondaryValue` | boolean |  | Also print the value in the secondary unit. |
| `secondaryLeaderText` | string |  | Text printed before the secondary value. |
| `secondaryTrailerText` | string |  | Text printed after the secondary value. |
| `secondaryBoxText` | boolean |  | Draw a box around the secondary value. |
| `secondaryPrecision` | integer |  | Precision of the secondary value (as `precision`). |
| `noteText` | string |  | Note text added to the dimension. |
| `textPositionAutomatic` | boolean |  | Place the text automatically. |
| `textInside` | boolean |  | Place the text inside the witness lines. |
| `textFlipped` | boolean |  | Flip the text. |
| `textRotation` | integer |  | Text rotation: 0 aligned, 1 horizontal, 2 horizontal/vertical. |
| `textOffsetAlongLine` | number |  | Offset of the text along the dimension line. |
| `textOffsetAboveLine` | number |  | Offset of the text above the dimension line. |
| `fontSize` | number |  | Font size in points. |
| `fontStyle` | integer |  | Sum of 1 bold, 2 italic, 4 underline. |
| `textStyle` | string |  | Name of a text style resource; an empty string for none. A UUID is not accepted. `applied.textStyle` is `false` when no named object has that name. |
| `toleranceType` | integer |  | Tolerance: 0 none, 1 single, 2 double, 3 limit. |
| `tolerancePlus` | number |  | Upper tolerance value. |
| `toleranceMinus` | number |  | Lower tolerance value. |
| `standard` | string |  | Name of the dimension standard. |
| `standardIndex` | integer |  | Dimension standard by index: above 0 built-in, below 0 custom. |
| `unit` | integer |  | 0 for document units, otherwise the index of a dimension unit setting. |
| `associate` | boolean |  | Bind the dimension to the geometry under its end points. The result always reports it as applied (see the notes of the [Dimensioning](#dimensioning) group). |
| `associateSelectedOnly` | boolean |  | With `associate`: bind only to selected objects. |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. A dimension is a native object without plug-in parameters, so this has no known use here, and the create tools do not report the outcome. See [Plug-in parameters](Common.md#plug-in-parameters). |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

The second form of the arc (`center`, `radius`, `startAngle` and `sweepAngle`) is used when `radius`, `startAngle` and `sweepAngle` are all present; otherwise the first form (`start`, `end` and `center`) is used and a missing point counts as (0, 0).

**Result**

The object reference of the new dimension (see [Object references](Common.md#object-references)), the common dimension keys (see the notes of the [Dimensioning](#dimensioning) group) and:

| Key | Description |
|---|---|
| `center` | Center of the arc, in world units. |
| `radius` | Radius of the arc, in world units. |
| `startAngle` | Start angle of the measured arc, in radians. |
| `sweepAngle` | Signed sweep of the measured arc, in radians (negative is clockwise). |
| `value` | The printed value: the length along the arc, in world units. |
| `applied` | Per setting written. |

Errors: `failed to create the arc length dimension (provide either 'start', 'end' and 'center', or 'center', 'radius', 'startAngle' and 'sweepAngle')` (also when `radius` is 0 or less or `sweepAngle` is 0); `failed to create the dimension`. A failed call is rolled back (`rolledBack`).

### createRadialDimension

Creates a radial or diametrical dimension.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createRadialDimension" · **In runToolBatch:** yes

**Details**

Create a radial dimension for a circle centred at `center`, its leader placed `offset` world units outside the circle. `mode` "radial" (default) prints the radius, "diametrical" prints the diameter across the circle. Give the circle either as `radius` (or `diameter`) plus the `angle` in radians at which the leader leaves the centre, or as a `pointOnCircle` the leader points at. `compact` draws the shortened radial form that stops at the circle instead of running to the centre.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `center` | [point](Common.md#points) | Yes | Center of the circle, in world units. |
| `radius` | number |  | Radius, in world units; must be greater than 0. Ignored when `diameter` or `pointOnCircle` is given. |
| `diameter` | number |  | Diameter, in world units; half of it is the radius. Wins over `radius`; ignored when `pointOnCircle` is given. |
| `angle` | number |  | Angle in radians, counter-clockwise, at which the leader leaves the center. Default 0. Ignored when `pointOnCircle` is given. |
| `pointOnCircle` | [point](Common.md#points) |  | A point on the circle that the leader points at, in world units. Wins over `radius`, `diameter` and `angle`. |
| `offset` | number |  | Distance of the dimension line from the measured geometry, in world units. |
| `compact` | boolean |  | Radial dimensions: the shortened form that stops at the circle. It is set after the dimension is created and is not reported in the result. |
| `mode` | string |  | One of: `radial` (default), `diametrical`. `radius` and `diameter` are accepted as aliases of `radial` and `diametrical`; any other value fails. |
| `startWitness` | boolean |  | Show the witness line at the start. |
| `endWitness` | boolean |  | Show the witness line at the end. |
| `witnessOverride` | integer |  | Witness lines: 0 by standard, 1 one custom length, 2 a length per witness line, 3 one custom offset, 4 an offset per witness line. |
| `startWitnessLength` | number |  | Custom length of the start witness line. |
| `endWitnessLength` | number |  | Custom length of the end witness line. |
| `startWitnessOffset` | number |  | Custom offset of the start witness line. |
| `endWitnessOffset` | number |  | Custom offset of the end witness line. |
| `arrowsInside` | boolean |  | Place the arrows inside the witness lines. |
| `leaderLine` | boolean |  | Show the leader line. |
| `showValue` | boolean |  | Print the measured value. |
| `leaderText` | string |  | Text printed before the value. |
| `trailerText` | string |  | Text printed after the value. |
| `boxText` | boolean |  | Draw a box around the value. |
| `precision` | integer |  | Decimal digits; fractional units: 0-6 = 1/1 to 1/64; angles: 1 degrees, 2 deg/min, 3 deg/min/sec. |
| `showSecondaryValue` | boolean |  | Also print the value in the secondary unit. |
| `secondaryLeaderText` | string |  | Text printed before the secondary value. |
| `secondaryTrailerText` | string |  | Text printed after the secondary value. |
| `secondaryBoxText` | boolean |  | Draw a box around the secondary value. |
| `secondaryPrecision` | integer |  | Precision of the secondary value (as `precision`). |
| `noteText` | string |  | Note text added to the dimension. |
| `textPositionAutomatic` | boolean |  | Place the text automatically. |
| `textInside` | boolean |  | Place the text inside the witness lines. |
| `textFlipped` | boolean |  | Flip the text. |
| `textRotation` | integer |  | Text rotation: 0 aligned, 1 horizontal, 2 horizontal/vertical. |
| `textOffsetAlongLine` | number |  | Offset of the text along the dimension line. |
| `textOffsetAboveLine` | number |  | Offset of the text above the dimension line. |
| `fontSize` | number |  | Font size in points. |
| `fontStyle` | integer |  | Sum of 1 bold, 2 italic, 4 underline. |
| `textStyle` | string |  | Name of a text style resource; an empty string for none. A UUID is not accepted. `applied.textStyle` is `false` when no named object has that name. |
| `toleranceType` | integer |  | Tolerance: 0 none, 1 single, 2 double, 3 limit. |
| `tolerancePlus` | number |  | Upper tolerance value. |
| `toleranceMinus` | number |  | Lower tolerance value. |
| `standard` | string |  | Name of the dimension standard. |
| `standardIndex` | integer |  | Dimension standard by index: above 0 built-in, below 0 custom. |
| `unit` | integer |  | 0 for document units, otherwise the index of a dimension unit setting. |
| `associate` | boolean |  | Bind the dimension to the geometry under its end points. The result always reports it as applied (see the notes of the [Dimensioning](#dimensioning) group). |
| `associateSelectedOnly` | boolean |  | With `associate`: bind only to selected objects. |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. A dimension is a native object without plug-in parameters, so this has no known use here, and the create tools do not report the outcome. See [Plug-in parameters](Common.md#plug-in-parameters). |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

Give the circle as `pointOnCircle`, or as `radius` or `diameter` with an `angle`. `pointOnCircle` wins when present; otherwise `diameter` wins over `radius`, and `angle` defaults to 0.

**Result**

The object reference of the new dimension (see [Object references](Common.md#object-references)), the common dimension keys (see the notes of the [Dimensioning](#dimensioning) group) and:

| Key | Description |
|---|---|
| `diametrical` | `true` for a diametrical dimension. |
| `center` | Center of the circle, in world units. |
| `radius` | Radius, in world units. |
| `diameter` | Diameter, in world units. |
| `angle` | Direction in which the dimension is drawn, in radians from the X axis. |
| `value` | The printed value: the diameter for a diametrical dimension, the radius otherwise. |
| `applied` | Per setting written. |

Errors: `unknown mode: <mode> (expected radial or diametrical)`; `failed to create the radial dimension (provide 'center' plus 'radius' / 'diameter' and 'angle', or 'center' plus 'pointOnCircle'; the radius must not be zero)`; `failed to create the dimension`. A failed call is rolled back (`rolledBack`).

### createCenterMark

Creates a center mark for a circular feature.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createCenterMark" · **In runToolBatch:** yes

**Details**

Create a center mark: a cross, optionally with four extension segments, marking the centre of a circular feature. It is a group of lines placed in the dimension class, not a dimension object. Give either `objectUuid` to mark the centre of an existing object's bounding box, or `center` plus the `radius` of the feature. Without explicit sizes the cross, gap and extension lengths come from the active dimension standard and are scaled to the layer.

`spokeLength`, `gap` and `extension` override them with world lengths; the extension segments are omitted when the circle is too small for them.

> **Note:** The group goes to the dimension class only when the document preference "create dimensions in the dimension class" is on; otherwise it stays in the active class. A `class` creation option overrides both. Without `spokeLength` the sizes come from the dimension standard. The extension segments are drawn only when `radius` is greater than 0 and `spokeLength` plus `gap` is less than `radius`. A center mark is not a dimension object: [`getDimension`](#getdimension) and [`setDimension`](#setdimension) refuse it; edit it with [`editObject`](ObjectPrimitives.md#editobject).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `center` | [point](Common.md#points) |  | Center of the feature, in world units; default (0, 0). Ignored with `objectUuid`. |
| `radius` | number |  | Radius of the feature, in world units; default 0, which gives the cross alone. Ignored with `objectUuid`: the radius is then half of the smaller side of the object's bounding box. |
| `objectUuid` | string |  | UUID of the object to mark; the mark is centered on its bounding box. `center`, `radius`, `spokeLength`, `gap` and `extension` are then ignored. An unknown UUID fails. |
| `spokeLength` | number |  | Length of each spoke of the cross, measured from the center, in world units (the whole cross is twice as long); must be greater than 0. Without it, `gap` and `extension` are ignored. |
| `gap` | number |  | Gap between the end of a spoke and the start of an extension segment, in world units. Used only with `spokeLength`; a missing value counts as 0. |
| `extension` | number |  | How far the extension segments run past the circle, in world units. Used only with `spokeLength`; a missing value counts as 0. |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new group (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `center` | Center of the mark, in world units. |
| `segmentCount` | Number of line segments in the group: 2 for the cross alone, 6 with the four extension segments. |

There is no `applied`. Errors: `object to mark not found` (unknown `objectUuid`); `failed to create the center mark` (for example `spokeLength` of 0 or less). A failed call is rolled back (`rolledBack`).

### getDimension

Reads a dimension: its kind, measured points, value and text settings.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read a dimension by uuid, name or index: its `kind` (constrainedLinear, unconstrainedLinear, ordinate, radial, diametrical, angular or arcLength), measured points, `offset` and `measuredLength`, the witness line and arrow settings, the printed text and precision for both the primary and the secondary value, the text placement and font, the tolerance, the dimension standard and unit setting (integer codes as in setDimension), plus the fields specific to its kind - `value` and `direction` for a linear one, `vertex`/`startAngle`/`endAngle` for an angular one, `center`/`radius`/`sweepAngle` for an arc length one and `center`/`radius`/`diameter`/`angle` for a radial one.

All angles are radians. Center marks are unmarked groups and cannot be identified by this query.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |

**Result**

The object reference of the dimension (see [Object references](Common.md#object-references)) and the keys below. A key whose value cannot be read is left out.

| Key | Description |
|---|---|
| `kind` | `constrainedLinear`, `unconstrainedLinear`, `ordinate`, `radial`, `diametrical`, `angular`, `arcLength` or `unknown`. |
| `start`, `end` | The measured points, in world units. For an angular dimension they are the two leg points; for a radial or diametrical dimension, `start` is the center and `end` the point on the circle; for an arc length dimension, the two points on the arc. |
| `offset` | Distance between the measured points and the dimension line, in world units. Positive: the dimension line is on the left of the start → end direction; negative: on the right. |
| `measuredLength` | Straight distance between `start` and `end`, in world units. A constrained linear dimension prints the projection of this distance onto its direction (see `value`). |
| the settings | Every setting that [`setDimension`](#setdimension) writes, under the name of its parameter: `startWitness`, `endWitness`, `witnessOverride`, `startWitnessLength`, `endWitnessLength`, `startWitnessOffset`, `endWitnessOffset`, `arrowsInside`, `leaderLine`, `showValue`, `leaderText`, `trailerText`, `boxText`, `precision`, `showSecondaryValue`, `secondaryLeaderText`, `secondaryTrailerText`, `secondaryBoxText`, `secondaryPrecision`, `noteText`, `textPositionAutomatic`, `textInside`, `textFlipped`, `textRotation`, `textOffsetAlongLine`, `textOffsetAboveLine`, `fontSize`, `fontStyle`, `textStyle`, `toleranceType`, `tolerancePlus`, `toleranceMinus`, `standard`, `standardIndex`, `unit`. `textStyle` is the name of the text style (an empty string for none, or when the style cannot be found). `witnessOverride`, `precision`, `secondaryPrecision`, `textRotation`, `fontStyle`, `toleranceType`, `standardIndex` and `unit` are integer codes, as in [`setDimension`](#setdimension). |
| linear dimensions | `constrained` (boolean), `direction` (radians) and `value` (the measured distance projected on the direction of the dimension line, in world units). |
| angular dimensions | `vertex`, `startAngle` and `endAngle` (radians), `value` (radians, counter-clockwise from the first leg to the second, from 0 up to 2π) and `referenceAngle`. |
| arc length dimensions | `center`, `radius`, `startAngle`, `sweepAngle` (radians; negative: clockwise), `value` (the length along the arc, in world units), `clockwise`, `witnessPerpendicularToChord` and `arcIndicator`. |
| radial dimensions | `diametrical`, `center`, `radius`, `diameter`, `angle` (radians, from the X axis), `value` (the diameter for a diametrical dimension, the radius otherwise) and `compact`. |

Errors: `object not found`; `not a dimension object` (a center mark is a group of lines and is not recognized).

### setDimension

Edits a dimension.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: setDimension" · **In runToolBatch:** yes

**Details**

Edit a dimension by uuid, name or index. Any of the shared settings can be written: the measured `start`/`end` points, `offset`, the witness lines, `arrowsInside`/`leaderLine`, the printed text (`showValue`, `leaderText`, `trailerText`, `boxText`, `precision` and their 'secondary\*' counterparts, `noteText`), the text placement and font, the tolerance, `standard` and `unit`.

**Integer codes:** `witnessOverride` 0 by standard, 1 one custom length, 2 a length per witness line, 3 one custom offset, 4 an offset per witness line; `precision` decimal digits (fractional units: 0-6 = 1/1-1/64; angular: 1 degrees, 2 deg/min, 3 deg/min/sec); `textRotation` 0 aligned, 1 horizontal, 2 horizontal/vertical; `fontStyle` sum of 1 bold, 2 italic, 4 underline (`fontSize` is in points); `toleranceType` 0 none, 1 single, 2 double, 3 limit; `standardIndex` &gt; 0 built-in, &lt; 0 custom standard; `unit` 0 document units, otherwise the index of a dimension unit setting.

**Kind-specific fields:** `direction` (radians) for a linear dimension, `vertex` and `referenceAngle` for an angular one, `center`/`radius`/`diameter`/`angle`/`compact` for a radial one. `associate`: true binds the dimension to the geometry under its end points (`associateSelectedOnly` limits that to the selected objects; an association cannot be removed). The kind of a dimension cannot be changed. A `params` object sets raw plug-in parameters.

> **Note:** A kind-specific field that does not belong to the kind of the dimension (for example `vertex` on a linear dimension) is ignored and is not listed in `applied`. An arc length dimension has no kind-specific field.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `start` | [point](Common.md#points) |  | First measured point, in world units (for an angular dimension a leg point; for a radial or diametrical dimension the center, and `end` the point on the circle; for an arc length dimension a point on the arc). Given together with `end`, both are set at once and reported as `points`. |
| `end` | [point](Common.md#points) |  | Second measured point, in world units. See `start`. |
| `offset` | number |  | Distance between the measured points and the dimension line, in world units. Positive: the dimension line is on the left of the start → end direction; negative: on the right. |
| `startWitness` | boolean |  | Show the witness line at the start. |
| `endWitness` | boolean |  | Show the witness line at the end. |
| `witnessOverride` | integer |  | Witness lines: 0 by standard, 1 one custom length, 2 a length per witness line, 3 one custom offset, 4 an offset per witness line. |
| `startWitnessLength` | number |  | Custom length of the start witness line. |
| `endWitnessLength` | number |  | Custom length of the end witness line. |
| `startWitnessOffset` | number |  | Custom offset of the start witness line. |
| `endWitnessOffset` | number |  | Custom offset of the end witness line. |
| `arrowsInside` | boolean |  | Place the arrows inside the witness lines. |
| `leaderLine` | boolean |  | Show the leader line. |
| `showValue` | boolean |  | Print the measured value. |
| `leaderText` | string |  | Text printed before the value. |
| `trailerText` | string |  | Text printed after the value. |
| `boxText` | boolean |  | Draw a box around the value. |
| `precision` | integer |  | Decimal digits; fractional units: 0-6 = 1/1 to 1/64; angles: 1 degrees, 2 deg/min, 3 deg/min/sec. |
| `showSecondaryValue` | boolean |  | Also print the value in the secondary unit. |
| `secondaryLeaderText` | string |  | Text printed before the secondary value. |
| `secondaryTrailerText` | string |  | Text printed after the secondary value. |
| `secondaryBoxText` | boolean |  | Draw a box around the secondary value. |
| `secondaryPrecision` | integer |  | Precision of the secondary value (as `precision`). |
| `noteText` | string |  | Note text added to the dimension. |
| `textPositionAutomatic` | boolean |  | Place the text automatically. |
| `textInside` | boolean |  | Place the text inside the witness lines. |
| `textFlipped` | boolean |  | Flip the text. |
| `textRotation` | integer |  | Text rotation: 0 aligned, 1 horizontal, 2 horizontal/vertical. |
| `textOffsetAlongLine` | number |  | Offset of the text along the dimension line. |
| `textOffsetAboveLine` | number |  | Offset of the text above the dimension line. |
| `fontSize` | number |  | Font size in points. |
| `fontStyle` | integer |  | Sum of 1 bold, 2 italic, 4 underline. |
| `textStyle` | string |  | Name of a text style resource; an empty string for none. A UUID is not accepted. `applied.textStyle` is `false` when no named object has that name. |
| `toleranceType` | integer |  | Tolerance: 0 none, 1 single, 2 double, 3 limit. |
| `tolerancePlus` | number |  | Upper tolerance value. |
| `toleranceMinus` | number |  | Lower tolerance value. |
| `standard` | string |  | Name of the dimension standard. |
| `standardIndex` | integer |  | Dimension standard by index: above 0 built-in, below 0 custom. |
| `unit` | integer |  | 0 for document units, otherwise the index of a dimension unit setting. |
| `associate` | boolean |  | `true` binds the dimension to the geometry under its end points. `false` does nothing and is reported as `false`: no tool removes an association. A `true` is reported whenever the binding was requested (see the group notes). |
| `associateSelectedOnly` | boolean |  | With `associate`: bind only to selected objects. |
| `direction` | number |  | Linear dimensions: measuring direction in radians. |
| `vertex` | [point](Common.md#points) |  | Angular dimensions: the vertex of the angle. |
| `referenceAngle` | boolean |  | Angular dimensions: measure a single leg against the reference direction. |
| `center` | [point](Common.md#points) |  | Radial dimensions: the center of the circle (the `start` point), in world units. Moves only the center: the point on the circle stays, so the radius and angle change; give `radius` or `diameter` and `angle` with it. Written after `start` and `end`. |
| `radius` | number |  | Radial dimensions: the radius, in world units. Greater than 0 (otherwise `false`). |
| `diameter` | number |  | Radial dimensions: the diameter, in world units. It is applied after `radius`, so with both the diameter is the last value written. Greater than 0 (otherwise `false`). |
| `angle` | number |  | Radial dimensions: the direction in which the dimension is drawn, in radians from the X axis. |
| `compact` | boolean |  | Radial dimensions: the shortened form that stops at the circle. |
| `params` | object |  | Raw plug-in parameters `{ "ParamName": value }`. A dimension is a native object without plug-in parameters, so there is no known parameter to set here; the outcome is reported per name in `applied.params`. See [Plug-in parameters](Common.md#plug-in-parameters). |

**Result**

| Key | Description |
|---|---|
| `applied` | Always present, and empty when no setting was given. One entry per setting that was given: `true` when it was written, `false` when it was refused (see the group notes). `start` and `end` given together are reported as `points`; a single one as `start` or `end`. `params` is a nested object with `true` or `false` per parameter name. |

The result holds no object reference. Errors: `object not found`; `not a dimension object (a center mark is a group of lines - edit it with editObject)`. A failed call is rolled back (`rolledBack`).

### getObjectDimensions

Lists the dimensions associated with an object.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the dimensions that are associated with the object given by uuid, name or index, i.e. the dimensions that follow that object when it moves or changes size. Each listed dimension carries its `kind` (as in getDimension).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |

**Result**

| Key | Description |
|---|---|
| `object` | The object reference of the object (see [Object references](Common.md#object-references)). |
| `dimensions` | One entry per associated dimension: its object reference and its `kind` (as in [`getDimension`](#getdimension)). Empty when no dimension is associated. There is no paging. |

The tool lists the dimensions that are bound to the object by an association (see `associate`); for a plug-in object inserted into a wall, it also lists the dimensions bound to the wall break that the object causes. Errors: `object not found`.
