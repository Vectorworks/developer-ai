**English** • [Deutsch](../../MCP.de/v2027.2/IFC.md) • [日本語](../../MCP.ja/v2027.2/IFC.md)

# IFC — IFC data and Data Manager mappings

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Read-only access to the IFC (Industry Foundation Classes) data of the drawing: the IFC entity and property sets of objects, property-set definitions, and the IFC Data Manager mappings of the document.

## Table of contents

- [Overview](#overview)
- [IFC](#ifc)
  - [getObjectIFCData](#getobjectifcdata)
  - [getIFCPsetDefinition](#getifcpsetdefinition)
  - [listIFCPsets](#listifcpsets)
  - [listIFCCustomPsets](#listifccustompsets)
- [IFC Data Mapping](#ifc-data-mapping)
  - [listIFCMappingObjects](#listifcmappingobjects)
  - [getIFCMapping](#getifcmapping)

## Overview

This folder holds 2 tool groups with 6 tools in total.

| Group | Group ID | Active by default | Risk level | Tools | Summary |
|---|---|---|---|---|---|
| [IFC](#ifc) | `ifc` | Yes | low | 4 | Read-only IFC data: the IFC entity and property sets of objects, the IFC property-set definitions (standard and custom) and the custom property sets of the document. |
| [IFC Data Mapping](#ifc-data-mapping) | `ifc-data-mapping` | No | low | 2 | Read the IFC Data Manager mapping definitions of the active document. |

## IFC

> **Group:** `IFC` · **Group ID:** `ifc` · **Active by default:** Yes · **Risk level:** low · **Tools:** 4

**Read-only IFC data: the IFC entity and property sets of objects, the IFC property-set definitions (standard and custom) and the custom property sets of the document.**

Read-only access to IFC data through the IFC support library only: object entity assignment, property sets, entity and property values, and custom property-set definitions. IFC values come from the Data Manager; this group cannot change them. These tools never expose or edit the raw internal IFC records directly; use them instead of the generic object/resource record tools for IFC work.

When IFC support is unavailable they return an explicit error. getObjectIFCData reports an object's IFC data as IFC export computes it. listIFCCustomPsets lists the custom property sets of the active document and is the only complete check for whether a custom set exists; getIFCPsetDefinition checks one loaded definition and listIFCPsets covers one entity type.

Data Manager mapping definitions are in the inactive 'IFC Data Mapping' group; use it only when the user asks about data mapping. A failed read is an `err` result and never means the data is absent.

| Tool | Effect | Risk | Summary |
|---|---|---|---|
| [`getObjectIFCData`](#getobjectifcdata) | Read-only | low | Reads the IFC data of an object as IFC export computes it. |
| [`getIFCPsetDefinition`](#getifcpsetdefinition) | Read-only | low | Reads one IFC property-set definition by name. |
| [`listIFCPsets`](#listifcpsets) | Read-only | low | Lists the IFC property sets applicable to an IFC entity type. |
| [`listIFCCustomPsets`](#listifccustompsets) | Read-only | low | Lists the custom IFC property-set definitions of the document. |

### getObjectIFCData

Reads the IFC data of an object as IFC export computes it.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the IFC data of the object identified by `uuid` as IFC export computes it from the attached IFC records and the Data Manager mapping (values from plug-in parameters, records, styles and formulas included): `hasIFC`, `entity`, `schema`, IFC `guid`, entity `attributes` and the exported property sets (`psets`) with `custom` and their properties (name, value type, IFC type and value when set).

Export settings, MVD filtering and layer/story mapping are not applied, and the extra parts that IFC export writes for door/window parts, symbol types, stairs and wall components are not reproduced. A property set is listed only if export would write it. Use the reported `type`/`ifcType`; never derive types from the entity name (for example IfcSlab).

The result is the current state only, so it cannot show that a value or type changed.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string | Yes | The UUID of the object. This tool does not accept `name` or `index`. |

**Result**

| Key | Description |
|---|---|
| `object` | The object reference (see [Object references](Common.md#object-references)). |
| `hasIFC` | `true` when the object has an IFC entity as export computes it. |
| `scope` | A fixed text that says what the data covers. |
| `attributes` | The attributes of the entity, as a list of properties (see below); attributes that reference other IFC instances are left out. Empty when `hasIFC` is `false`. |
| `psets` | The exported property sets, as a list of `{ "name", "custom", "properties" }`. `properties` is a list of properties (see below). Empty when `hasIFC` is `false`. |
| `readErrors` | Always an empty list at present. A failed read is an `err` result. |
| `entity` | The IFC entity name. Only when `hasIFC` is `true`. |
| `schema` | The active IFC schema: `IFC2x2`, `IFC2x3`, `IFC4` or `IFC4x3`. Only when `hasIFC` is `true`. `getDocumentInfo` reports the IFC4 schema as `IFC2x4`. |
| `guid` | The IFC GUID. Only when the object has one. |

Each property has `name`, `type` and, when known, `ifcType` and `value`. `type` is a symbolic value type, for example `kIfcType_STRING` or `kIfcType_DOUBLE`, or `unknown`. `ifcType` is the IFC data type name from the definition, for example `IfcLabel`. `value` is always a string; it is left out when it is empty and for references to other IFC instances. Entity attributes that reference other IFC instances are left out of `attributes` entirely; in `psets` such properties are listed without `value`.

Errors: `'uuid' is required`, `object not found`, `IFC support is unavailable in this Vectorworks session` and `failed to read the object's IFC data` (for example when no IFC document or scheme is active).

### getIFCPsetDefinition

Reads one IFC property-set definition by name.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read one IFC property-set definition by `name`. Returns whether it is defined, whether it is custom, and its property names. A missing definition is reported explicitly instead of as an empty result. `scope` says what was searched: `defined` false means the IFC support library has no standard or custom definition by that name; it is not a search of record formats or object data.

A similarly named property set or record format is a different one. To check whether the document has a custom property set, use listIFCCustomPsets.

> **Note:** The name is looked up in the IFC2x3, IFC4 and IFC4x3 definitions, but `custom` and `propertyNames` are read from the active IFC schema only. A standard property set that exists only in another schema returns the error `failed to read IFC property set definition: <name>` instead of `defined: false`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | The name of the property set, for example `Pset_WallCommon`. |

**Result**

| Key | Description |
|---|---|
| `name` | The name that was asked for. |
| `scope` | A fixed text that says what was searched. |
| `defined` | `true` when the IFC support library has a definition by that name. |
| `custom` | Only when `defined` is `true`: `true` for a custom property set. |
| `propertyNames` | Only when `defined` is `true`: the names of the properties, as a list of strings. |

Errors: `'name' is required`, `IFC support is unavailable in this Vectorworks session`, `failed to determine whether IFC property set is defined: <name>`, `failed to determine whether IFC property set is custom: <name>` and `failed to read IFC property set definition: <name>`.

### listIFCPsets

Lists the IFC property sets applicable to an IFC entity type.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the IFC property sets applicable to one entity type. `entity` defaults to `IfcBuildingElementProxy`. Set `customOnly` to keep only custom property sets. Only the sets applicable to `entity` are returned, from the IFC schema and the Data Manager mapping of that entity; this is not a list of the document's property sets. Use listIFCCustomPsets for the document's custom sets.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `customOnly` | boolean |  | Keep only the custom property sets. Default: `false`. |
| `entity` | string |  | The IFC entity type, for example `IfcWall`. Default: `IfcBuildingElementProxy`. |

**Result**

| Key | Description |
|---|---|
| `entity` | The entity that was used: the `entity` argument, or `IfcBuildingElementProxy` when it is missing or not a string. |
| `customOnly` | The value that was used. |
| `psets` | The applicable property sets, as a list of `{ "name", "custom" }`. |

Errors: `IFC support is unavailable in this Vectorworks session`, `failed to list IFC property sets for entity: <entity>` (the entity is not known in the active IFC schema, or `entity` is an empty string) and `failed to determine whether IFC property set is custom: <name>`.

### listIFCCustomPsets

Lists the custom IFC property-set definitions of the document.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the custom IFC property-set definitions of the active document with each property's IFC type and whether the set is enabled. A set missing from a successful result is not defined in the document; an `err` result means presence cannot be determined. Takes no arguments.

**Parameters**

This tool takes no parameters.

**Result**

| Key | Description |
|---|---|
| `scope` | A fixed text: `custom property-set definitions of the active document`. |
| `customPsets` | The custom property sets, as a list of `{ "name", "enabled", "properties" }`. `properties` is a list of `{ "name", "ifcType", "unit" }`. `unit` is only present when the property has a unit: `Length`, `Area`, `SolidAngle`, `Mass`, `Time`, `Temperature`, `Luminosity`, `Power`, `ThermalTransmittance`, `Dimension`, `Volume` or `Angle`. |

Errors: `IFC support is unavailable in this Vectorworks session` and `the custom property sets of the active document could not be read; presence cannot be determined` (for example when the IFC data is not bound to the active document).

## IFC Data Mapping

> **Group:** `IFC Data Mapping` · **Group ID:** `ifc-data-mapping` · **Active by default:** No · **Risk level:** low · **Tools:** 2

**Read the IFC Data Manager mapping definitions of the active document.**

Read the IFC Data Manager mapping definitions of the active document: which objects are mapped, their conditions, IFC entries, property sets and the formula that supplies each field. Use these tools only when the user asks about data mapping or the Data Manager; for an object's IFC values use getObjectIFCData in the IFC group.

| Tool | Effect | Risk | Summary |
|---|---|---|---|
| [`listIFCMappingObjects`](#listifcmappingobjects) | Read-only | low | Lists the mapping objects of the active Data Manager mapping. |
| [`getIFCMapping`](#getifcmapping) | Read-only | low | Reads the Data Manager mapping of one mapping object. |

### listIFCMappingObjects

Lists the mapping objects of the active Data Manager mapping.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the mapping objects of the active Data Manager mapping with their `name`, `enabled`, `condition` and `category`, paged by `limit` (default 200) and `offset`; `count` is the total and `truncated` says whether more follow. Pass a name to getIFCMapping for its entries.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). Default: 200. See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

**Result**

The paging keys (see [Paging](Common.md#paging)) and `objects`, the mapping objects of this page. Each object has:

| Key | Description |
|---|---|
| `index` | The position of the object in the mapping. |
| `name` | The name of the object. Pass it as `objectName` to `getIFCMapping`. |
| `enabled` | `true` when the object is enabled. |
| `condition` | The condition of the object. Only when it has one. |
| `category` | Only when the object has a stored category: `classBasedLegacy`, `symbolDefinition`, `plugInThirdPartyLegacy`, `plugInBuiltInLegacy`, `ifcEntity`, `criteriaBased`, `parametricObjects`, `modelHierarchy`, `zones`, `systems`, `groups` or `unknown`. |

An object that cannot be read has only `index` and `readFailed: true`. A mapping without objects gives an empty list, not an error. Errors: `IFC support is unavailable in this Vectorworks session` and the paging errors (see [Paging](Common.md#paging)).

### getIFCMapping

Reads the Data Manager mapping of one mapping object.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the Data Manager mapping of one mapping object `objectName` (as returned by listIFCMappingObjects): its condition and IFC entries, each with its `type` (primary, secondary or unknown), enabled state, fields (value type, mapping formula, enabled, optional, empty) and property sets with their condition and fields. An unknown name returns an error.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `objectName` | string | Yes | The name of the mapping object, as returned by listIFCMappingObjects. |

**Result**

| Key | Description |
|---|---|
| `objectName` | The name that was asked for. |
| `enabled` | `true` when the mapping object is enabled. |
| `condition` | The condition of the mapping object. Only when it has one. |
| `entries` | The IFC entries of the object. Each entry has the keys below. |

| Entry key | Description |
|---|---|
| `name` | The name of the entry. |
| `type` | `primary`, `secondary` or `unknown`. |
| `enabled` | `true` when the entry is enabled. |
| `fields` | The fields of the entry. |
| `psets` | The property sets of the entry, as a list of `{ "name", "enabled", "fields", "condition" }`. `condition` is only present when the property set has one. |

Each field has `name`, `enabled`, `optional` and `empty` (the flags of the field in the Data Manager) and, when they are known, `type` (a symbolic value type, as in `getObjectIFCData`) and `mapping` (the formula; left out when empty).

Errors: `IFC support is unavailable in this Vectorworks session`, `'objectName' is required` and `no Data Manager mapping for object: <name>`.
