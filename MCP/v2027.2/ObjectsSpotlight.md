**English** • [Deutsch](../../MCP.de/v2027.2/ObjectsSpotlight.md) • [日本語](../../MCP.ja/v2027.2/ObjectsSpotlight.md)

# ObjectsSpotlight — lighting devices and GDTF fixture types

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools for Spotlight lighting devices and the GDTF fixture types (General Device Type Format) they use.

## Table of contents

- [Overview](#overview)
- [Spotlight](#spotlight)
  - [listGDTFs](#listgdtfs)
  - [importGDTF](#importgdtf)
  - [createLightingDevice](#createlightingdevice)
  - [getLightingDevice](#getlightingdevice)
  - [setLightingDevice](#setlightingdevice)

## Overview

This folder holds 1 tool group with 5 tools in total.

| Group | Group ID | Active by default | Safety level | Tools | Summary |
|---|---|---|---|---|---|
| [Spotlight](#spotlight) | `spotlight` | No | medium | 5 | Spotlight lighting devices and the GDTF fixture types they use. |

## Spotlight

> **Group:** `Spotlight` · **Group ID:** `spotlight` · **Active by default:** No · **Safety level:** medium · **Tools:** 5

**Spotlight lighting devices and the GDTF fixture types they use.**

Create, inspect and edit Spotlight lighting devices and the GDTF fixture types (General Device Type Format) they use: list the available GDTF fixture types and their DMX modes, import a .gdtf file into the drawing, create a lighting device with a GDTF fixture type, DMX mode and 3D model, and read or change it. A GDTF fixture type is addressed by its `gdtfName` as listGDTFs reports it; a lighting device can only use a fixture type that is in the drawing (isInDocument), so import a .gdtf file first.

Each change runs as its own named, undoable Vectorworks operation.

> **Note:** `gdtfName` and `mode` are matched exactly, including the case, and only against the fixture types in the drawing. For a fixture type in the drawing, `gdtfName` is built as `<Manufacturer>@<Name>.gdtf` from the data of the GDTF file. For a .gdtf file that is not imported yet, `listGDTFs` shows the file name on disk, which can differ. Use the `gdtfName` that `importGDTF` returns, or that `listGDTFs` reports with `documentOnly`.

| Tool | Effect | Safety | Summary |
|---|---|---|---|
| [`listGDTFs`](#listgdtfs) | Read-only | low | Lists the available GDTF fixture types and their DMX modes. |
| [`importGDTF`](#importgdtf) | Edit | medium | Imports a .gdtf file into the drawing as a GDTF fixture type. |
| [`createLightingDevice`](#createlightingdevice) | Edit | medium | Creates a lighting device, optionally with a GDTF fixture type. |
| [`getLightingDevice`](#getlightingdevice) | Read-only | low | Reads a lighting device. |
| [`setLightingDevice`](#setlightingdevice) | Edit | medium | Edits a lighting device. |

### listGDTFs

Lists the available GDTF fixture types and their DMX modes.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the GDTF fixture types available to Spotlight, one entry per DMX mode: `gdtfName` (pass it to createLightingDevice / setLightingDevice), `fixtureName` (with '@&lt;revision&gt;' when the file has one), `manufacturer`, `mode`, `footprint` (DMX channels) and `isInDocument` (imported into the drawing; then also `symbolDefinitionUuid`). Fixture types in the drawing come first, then the .gdtf files of the Spotlight GDTF folders, which Spotlight reads once per session; only the fixture types in the drawing can be assigned to a lighting device - import a file with importGDTF.

Optional filters: `manufacturer` and `search` (case-insensitive parts of the manufacturer / fixture or GDTF name) and `documentOnly`. Paged by `limit` (default 200) and `offset`; `countOnly` returns only the count.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `manufacturer` | string |  | Part of the manufacturer name. Case-insensitive for ASCII letters only. |
| `search` | string |  | Part of the `fixtureName` or of the `gdtfName`; the `manufacturer` value itself is not searched (use `manufacturer`). Case-insensitive for ASCII letters only. With `manufacturer`, both filters must match. |
| `documentOnly` | boolean |  | Only the fixture types that are imported into the drawing (`isInDocument` true). Default false. |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). Default 200. See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

**Result**

A paged result (see [Paging](Common.md#paging)) whose items key is `gdtfs`. Each entry has:

| Key | Description |
|---|---|
| `gdtfName` | The name to pass to `createLightingDevice` and `setLightingDevice`. |
| `fixtureName` | The fixture name, with `@&lt;revision&gt;` when the file has one. |
| `manufacturer` | The manufacturer. |
| `mode` | The DMX mode of this entry. |
| `footprint` | The number of DMX channels of the mode. |
| `isInDocument` | `true` when the fixture type is imported into the drawing. |
| `symbolDefinitionUuid` | The UUID of the fixture type's symbol definition. Only when `isInDocument` is `true`. |

A fixture type with several DMX modes has one entry per mode, with the same `gdtfName`. With `countOnly` the `gdtfs` list is left out.

Errors: `the GDTF support of Spotlight is not available`; the paging errors (see [Paging](Common.md#paging)).

### importGDTF

Imports a .gdtf file into the drawing as a GDTF fixture type.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: importGDTF" · **In runToolBatch:** yes

**Details**

Import the .gdtf file at `filePath` (full native path) into the drawing as a GDTF fixture type (a symbol definition in the GDTF resource folder). Returns its reference and `gdtfName`. Never asks the user: a fixture type with the same GDTF type ID that is already in the drawing is kept (isImported false); an unreadable file is an error.

> **Note:** The fixture type's own symbol definition is created at the root of the symbol library; only its helper symbol definitions (such as `<fixtureName>_Thumbnail`) are placed in the `GDTF` symbol folder. When the symbol name `<Manufacturer>@<Name>.gdtf` is already in use, the symbol definition is renamed `<Manufacturer>@<Name>(1).gdtf` (and so on), while `gdtfName` stays `<Manufacturer>@<Name>.gdtf`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `filePath` | string | Yes | Full native path of a .gdtf file. |

**Result**

On import: the object reference of the new fixture type's symbol definition (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `gdtfName` | The name to pass to `createLightingDevice` and `setLightingDevice`. |
| `isImported` | `true`. |

A fixture type with the same GDTF type ID that is already in the drawing is kept and never replaced. The result then has only `isImported` (`false`) and a `message`, with no object reference and no `gdtfName`. Find the kept fixture type with `listGDTFs` and `documentOnly`.

Errors: `'filePath' is required: the full path of a .gdtf file`; `the GDTF support of Spotlight is not available`; `the file could not be read as GDTF: <path>`.

### createLightingDevice

Creates a lighting device, optionally with a GDTF fixture type.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: createLightingDevice" · **In runToolBatch:** yes

**Details**

Create a Spotlight lighting device (without a lighting symbol) at `position`, rotated by `angle` (radians). Optional `gdtfName` (a fixture type in the drawing, from listGDTFs or importGDTF) with `mode` (DMX mode; the first mode when omitted) assigns a GDTF fixture type as dropping it on the device in the Resource Manager does, and then draws its 3D model unless `useGdtfGeometry` is false.

Optional `instrumentType` and raw `params`. `applied` reports per setting whether it was written; `gdtf` false means the drawing has no fixture type with that gdtfName and mode, and the device keeps its GDTF settings; `mode` false means a mode was given without `gdtfName`.

> **Note:** `gdtfName` and `mode` are matched exactly, including the case. A `mode` that is omitted, empty or not a string selects the first DMX mode. A `gdtf` of `false` does not fail the call: the lighting device is created without the fixture type.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `position` | [point](Common.md#points) | Yes | Insertion point in world units; only x and y are used. A missing or malformed point is not rejected: it reads as 0,0. |
| `angle` | number |  | Angle in radians, counter-clockwise. Default 0. |
| `gdtfName` | string |  | A fixture type in the drawing, from listGDTFs or importGDTF. Matched exactly, including the case. |
| `mode` | string |  | DMX mode of the fixture type, matched exactly, including the case. Only used with `gdtfName`. The first mode when omitted, empty or not a string. |
| `useGdtfGeometry` | boolean |  | Draw the 3D model of the GDTF fixture type. Default true after `gdtfName` was applied. Must be a JSON boolean: any other value is written as `true`. |
| `instrumentType` | string |  | Spotlight instrument type (the `Inst Type` parameter of the device). |
| `params` | object |  | Raw plug-in parameters { "ParamName": value } (see getObjectParameters). See [Plug-in parameters](Common.md#plug-in-parameters). |
| `class` | string |  | Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options). |
| `name` | string |  | Creation option: name of the new object. |
| `select` | boolean |  | Creation option: select the new object. |
| `useClassAttributes` | boolean |  | Creation option: with `class`, also set the attributes of the new object by class. |

**Result**

The object reference of the new lighting device (see [Object references](Common.md#object-references)) and, only when a setting was given, `applied` (see [Applied settings](Common.md#applied-settings)). Its keys are `gdtf` and `mode` (as described above), `useGdtfGeometry`, `instrumentType` and `params`. A key is present only for a setting that was given, except: with `gdtfName`, `gdtf` covers `mode` and there is no `mode` key (`mode` appears, always `false`, only without `gdtfName`); `useGdtfGeometry` is also present after `gdtfName` was applied; `params` only when it is an object. A `useGdtfGeometry` that is not a boolean counts as `true`, and an `instrumentType` that is not a string writes empty text; both report `true`. The `params` entry is an object with `true` or `false` for each parameter name.

Errors: `failed to create the lighting device (is Spotlight installed?)`. A failed call is rolled back (`rolledBack`).

### getLightingDevice

Reads a lighting device.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read a lighting device by uuid, name or index: `instrumentType`, `symbolName`, the GDTF fixture type `gdtfName` and DMX `mode`, `dmxFootprint`, `useGdtfGeometry` and `bounds`. Optional `params` lists plug-in parameter names (see getObjectParameters) to return as raw typed values.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `params` | array of string |  | Names of plug-in parameters to return with typed values. See [Plug-in parameters](Common.md#plug-in-parameters). |

**Result**

The object reference of the lighting device (see [Object references](Common.md#object-references)) and:

| Key | Description |
|---|---|
| `instrumentType` | The Spotlight instrument type (the `Inst Type` parameter). |
| `symbolName` | The name of the lighting symbol (the `Symbol Name` parameter). |
| `gdtfName` | The GDTF fixture type, as `listGDTFs` reports it. |
| `mode` | The DMX mode name, as `listGDTFs` reports it. |
| `dmxFootprint` | The number of DMX channels (the `Num Channels` parameter). |
| `useGdtfGeometry` | Whether the 3D model of the GDTF fixture type is drawn. |
| `bounds` | The bounds of the device, as a [rectangle](Common.md#rectangles) in world units. |
| `params` | Only when `params` was given: an object with the typed value of each requested parameter that the device has. Unknown names are left out. |

A key is left out when the device has no such parameter. A parameter that exists but is empty is returned as an empty string.

Errors: `object not found`; `not a lighting device`. The device is looked up by `uuid`, then `name`, then `index`.

### setLightingDevice

Edits a lighting device.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: setLightingDevice" · **In runToolBatch:** yes

**Details**

Edit a lighting device by uuid, name or index: `gdtfName` (a fixture type in the drawing) with `mode` assigns a GDTF fixture type (and, when that succeeded, turns its 3D model on unless `useGdtfGeometry` is false), `useGdtfGeometry`, `instrumentType` and raw `params`. The device is regenerated; `applied` reports per setting whether it was written.

> **Note:** `gdtfName` and `mode` are matched exactly, including the case. A `gdtf` of `false` means that the fixture type could not be assigned; normally the device is unchanged. A `mode` that is given without `gdtfName` is not written (`applied.mode` is `false`).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `gdtfName` | string |  | A fixture type in the drawing, as listGDTFs reports it. Matched exactly, including the case. |
| `mode` | string |  | DMX mode of the fixture type, matched exactly, including the case. Only written together with `gdtfName`. The first mode when omitted, empty or not a string. |
| `useGdtfGeometry` | boolean |  | Draw the 3D model of the GDTF fixture type. Default true after `gdtfName` was applied; also written without `gdtfName` when given. Must be a JSON boolean: any other value is written as `true`. |
| `instrumentType` | string |  | Spotlight instrument type (the `Inst Type` parameter of the device). |
| `params` | object |  | Raw plug-in parameters { "ParamName": value } (see getObjectParameters). See [Plug-in parameters](Common.md#plug-in-parameters). |

**Result**

Only `applied` (see [Applied settings](Common.md#applied-settings)); there is no object reference. `applied` is always present, even when it is empty. Its keys are the same as for `createLightingDevice`: `gdtf` and `mode`, `useGdtfGeometry`, `instrumentType` and `params`. A key is present only for a setting that was given, except: with `gdtfName`, `gdtf` covers `mode` and there is no `mode` key (`mode` appears, always `false`, only without `gdtfName`); `useGdtfGeometry` is also present after `gdtfName` was applied; `params` only when it is an object. A `useGdtfGeometry` that is not a boolean counts as `true`, and an `instrumentType` that is not a string writes empty text; both report `true`.

Errors: `object not found`; `not a lighting device`. The device is looked up by `uuid`, then `name`, then `index`. A failed call is rolled back (`rolledBack`).
