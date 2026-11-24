**English** • [Deutsch](../../MCP.de/v2027.2/ObjectsConnectCAD.md) • [日本語](../../MCP.ja/v2027.2/ObjectsConnectCAD.md)

# ObjectsConnectCAD — ConnectCAD devices

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools for ConnectCAD schematic devices, their sockets and their device types, and the signal and connector types they use.

## Table of contents

- [Overview](#overview)
- [ConnectCAD](#connectcad)
  - [listConnectCADSignals](#listconnectcadsignals)
  - [listConnectCADConnectors](#listconnectcadconnectors)
  - [validateConnectCADDevice](#validateconnectcaddevice)
  - [createConnectCADDevice](#createconnectcaddevice)
  - [createConnectCADDevices](#createconnectcaddevices)
  - [getConnectCADDevice](#getconnectcaddevice)
  - [addConnectCADSocket](#addconnectcadsocket)
  - [setConnectCADSocket](#setconnectcadsocket)
  - [createConnectCADDeviceType](#createconnectcaddevicetype)
  - [getConnectCADDeviceType](#getconnectcaddevicetype)

## Overview

This folder holds 1 tool group with 10 tools in total.

| Group | Group ID | Active by default | Risk level | Tools | Summary |
|---|---|---|---|---|---|
| [ConnectCAD](#connectcad) | `connectcad` | No | medium | 10 | ConnectCAD schematic devices, sockets and device types, built from JSON device descriptions. |

## ConnectCAD

> **Group:** `ConnectCAD` · **Group ID:** `connectcad` · **Active by default:** No · **Risk level:** medium · **Tools:** 10

**ConnectCAD schematic devices, sockets and device types, built from JSON device descriptions.**

Create and inspect ConnectCAD schematic devices without scripts: a device with all its sockets from a JSON device description, sockets added to or edited on a device, device-type symbols (Device Definition record), and the signal and connector types to use. Device description (one JSON object): name, tag, description, make, model, category, width_r (`non-rack` | `half-rack` | `full-rack`), width, height, depth (mm; a rack device height is whole rack units of 44.45 mm), power (W), weight (kg), is_modular (bool), n_slots (int, &gt; 0 only when modular); name, tag, make, model, width_r, is_modular and n_slots are required; 'socket groups': [ { qty (1-50), type, name, signal, connector, orientation, pinout: [ { pinID, name, sourceID } ], extra_data } ].

**Socket types:** IN, OUT, IO (one socket each) and LOOP / IOloop (a pair '&lt;name&gt;' + '&lt;name&gt;\_LP'); orientations L, R, X (feed-through); LOOP and IOloop only L or R; FUSE and BUS are not sockets. qty &gt; 1 makes '&lt;name&gt; 1'..'&lt;name&gt; n' (default ConnectCAD numbering); socket names must be unique in the device, without '+' and not ending in `_LP`. Signals and connectors must come from listConnectCADSignals / listConnectCADConnectors; a pinout lists the pins of its connector with pinIDs unique in the device. Descriptions are validated first; an invalid one creates nothing. Each change runs as its own named, undoable Vectorworks operation.

> **Note:** The ConnectCAD tools need the ConnectCAD plug-in. Without it, `listConnectCADSignals`, `listConnectCADConnectors`, `validateConnectCADDevice`, `createConnectCADDevice` and `createConnectCADDevices` fail with the `err` text `ConnectCAD is not available (the ConnectCAD plug-in is not installed)`; for the two list tools a paging error is reported first. `addConnectCADSocket` lists the same text in `errors`. `getConnectCADDevice`, `setConnectCADSocket`, `createConnectCADDeviceType` and `getConnectCADDeviceType` do not check for the plug-in. Without it, `setConnectCADSocket` refuses every `signal` and `connector` (`false` in `applied`), and `createConnectCADDeviceType` reports `ConnectCAD returned no device type '<make> <model>': ...` in `errors` for a device with a make and model.
>
> **Note:** `createConnectCADDevice`, `createConnectCADDevices` and `createConnectCADDeviceType` take none of the [creation options](Common.md#creation-options): the handler does not apply a `class`, `name`, `useClassAttributes` or `select`, and the ConnectCAD plug-in creates the object in the active layer.
>
> **Note:** A device description needs more than the text above says: every socket group needs all six keys `qty`, `type`, `name`, `signal`, `connector` and `orientation`, and `label_symbol` is accepted. The full rules are listed under [validateConnectCADDevice](#validateconnectcaddevice).
>
> **Note:** Arguments of the wrong type fall back silently: a `position` or `origin` that is not a point is (0, 0), a `gap` that is not a number is 0, a `createDeviceType` or `createDeviceTypes` that is not a boolean is false, and a text filter or socket value that is not a string is empty. Only `limit`, `offset` and `countOnly` report a wrong type.

| Tool | Effect | Risk | Summary |
|---|---|---|---|
| [`listConnectCADSignals`](#listconnectcadsignals) | Read-only | low | Lists the ConnectCAD signal types. |
| [`listConnectCADConnectors`](#listconnectcadconnectors) | Read-only | low | Lists the ConnectCAD connector types and their pins. |
| [`validateConnectCADDevice`](#validateconnectcaddevice) | Read-only | low | Checks a device description without creating anything. |
| [`createConnectCADDevice`](#createconnectcaddevice) | Edit | medium | Creates a schematic device with all its sockets from a device description. |
| [`createConnectCADDevices`](#createconnectcaddevices) | Edit | medium | Creates several schematic devices in a row in one operation. |
| [`getConnectCADDevice`](#getconnectcaddevice) | Read-only | low | Reads a ConnectCAD device and its sockets. |
| [`addConnectCADSocket`](#addconnectcadsocket) | Edit | medium | Adds a socket to a device. |
| [`setConnectCADSocket`](#setconnectcadsocket) | Edit | medium | Edits a socket. |
| [`createConnectCADDeviceType`](#createconnectcaddevicetype) | Edit | medium | Creates the device-type symbol of a device. |
| [`getConnectCADDeviceType`](#getconnectcaddevicetype) | Read-only | low | Reads the Device Definition record of a device-type symbol. |

### listConnectCADSignals

Lists the ConnectCAD signal types.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the ConnectCAD signal types: `name` (use it as a socket `signal`), `category`, `description`, `defaultConnector` and the preferred `connectors`. Optional filters `category` and `search` (case-insensitive parts). Paged by `limit` (default 500) and `offset`; `countOnly` returns only the count.

> **Note:** `countOnly` returns the paging keys (`count`, `returned`, `offset`, `limit`, `truncated`) without the `signals` array. `category` is a part of the signal category; `search` is a part of the signal `name` or `description`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `category` | string |  | Filter: keeps the signals whose category contains this text (case-insensitive). |
| `search` | string |  | Text filter: keeps the signals whose name or description contains this text (case-insensitive). |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

**Result**

The paging keys (`count`, `returned`, `offset`, `limit`, `truncated`, and `nextOffset` when the list is truncated; see [Paging](Common.md#paging)) and:

| Key | Description |
|---|---|
| `signals` | Array of signal types (left out with `countOnly`): `name`, `category`, `description`, `defaultConnector` and `connectors` (the preferred connector names). |

Errors: the paging errors (see [Paging](Common.md#paging)); `ConnectCAD is not available (the ConnectCAD plug-in is not installed)`.

### listConnectCADConnectors

Lists the ConnectCAD connector types and their pins.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the ConnectCAD connector types: `name` (use it as a socket `connector`), `localizedName`, `category` and `pins` (the pin names, in order, for a socket group `pinout`). Optional `search`. Paged by `limit` (default 500) and `offset`; `countOnly` returns only the count.

> **Note:** `countOnly` returns the paging keys (`count`, `returned`, `offset`, `limit`, `truncated`) without the `connectors` array. `search` is a part of the connector `name`, `localizedName` or `category`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `search` | string |  | Text filter: keeps the connectors whose name, localized name or category contains this text (case-insensitive). |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

**Result**

The paging keys (see [Paging](Common.md#paging)) and:

| Key | Description |
|---|---|
| `connectors` | Array of connector types (left out with `countOnly`): `name`, `localizedName`, `category` and `pins` (the pin names, in order). |

Errors: as for `listConnectCADSignals`.

### validateConnectCADDevice

Checks a device description without creating anything.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Check a device description without creating anything: `isValid`, `errors` (what would make the device wrong or the plug-in fail) and `warnings` (data kept only in a device type: category, pinout, extra_data, uuid, source).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `device` | object or string | Yes | Device description (see the group description) as a JSON object or as JSON text. |

**Result**

| Key | Description |
|---|---|
| `isValid` | `true` when `errors` is empty. |
| `errors` | Array of texts (always present): what would make the device wrong or the plug-in fail. |
| `warnings` | Array of texts (always present): data that is kept only in the device type. |

An invalid description is a normal result, not an `err`. Errors: `ConnectCAD is not available (the ConnectCAD plug-in is not installed)`.

**Validation rules**

The create tools use the same rules. A message about a socket group starts with `socket group <n> (<name>)` (n counts from 1).

- The description is one JSON object, given as an object or as JSON text. An array of devices is refused (`the device must be one JSON object (an array of devices is not accepted)`).
- Strings: `name`, `tag`, `description`, `make`, `model`, `category`, `width_r` and `label_symbol` (`'<key>' must be a string`). Numbers: `width`, `height`, `depth`, `power` and `weight` (`'<key>' must be a number (mm, W or kg)`). `is_modular` is a boolean (`'is_modular' must be a boolean`) and `n_slots` an integer (`'n_slots' must be an integer`). Other keys are ignored.
- `name`, `tag`, `make` and `model` must not be blank (`'<key>' is required`). `width_r` is `non-rack`, `half-rack` or `full-rack`. A rack device with a `height` needs whole rack units, n × 44.45 mm within 0.1 mm (`a rack device needs a height of whole rack units (n x 44.45 mm)`); a missing `height` is not an error. `n_slots` is an integer, greater than 0 for a modular device and 0 or less otherwise (`'n_slots' must be greater than 0 for a modular device and 0 otherwise`).
- `socket groups` is optional and must be an array of objects. Each group needs all of `qty`, `type`, `name`, `signal`, `connector` and `orientation` (`<where>: missing '<key>' (the plug-in would throw)`). `qty` is an integer from 1 to 50. `uuid` and `source` are optional strings.
- `type` is `IN`, `OUT`, `IO` (one socket each), `LOOP` or `IOloop` (a pair `<name>` + `<name>_LP`). `FUSE` and `BUS` are refused (`type FUSE is an internal-wiring component, not a socket (a Socket is IN, OUT or IO)`). `orientation` is `L`, `R` or `X`; `LOOP` and `IOloop` cannot have `X`.
- A socket name is not blank, has no `+` (a numbering offset in ConnectCAD) and does not end in `_LP`. The generated names (`<name>`, or `<name> 1`..`<name> n`, and `<name>_LP` for a loop) are unique in the device (`socket name '<n>' is used <count> times in the device`).
- `signal` and `connector` must be known to ConnectCAD (`signal '<x>' is not a ConnectCAD signal type`, `connector '<x>' is not a ConnectCAD connector type`); `???` is never accepted. Take the names from `listConnectCADSignals` and `listConnectCADConnectors`.
- `pinout` (optional) is an array of objects with a string `name` and the optional integers `pinID` and `sourceID` (0 to 65535). The pin names must equal the pins of the connector, in order (`the pinout does not match the pins of connector <name>`). A `pinID` is used once in the device (`pinID <n> is used twice in the device`), and every `sourceID` must be a `pinID` of the device (`sourceID <n> is not a pinID of the device`).
- `extra_data` (optional) is an object. Strings: `power_factor`, `rating`. Boolean: `link_through`. Numbers: `avg_consumption`, `max_consumption`, `max_voltage`, `min_voltage`, `ampere`, `maximum_power`, `voltage`, `x`, `y`, `z`, `x_scale`, `y_scale`, `z_scale`, `x_offset`, `y_offset` and `z_rotation`. Another key is an error (`extra_data '<key>' is not a ConnectCAD key`).
- Warnings, not errors: `'category' is only kept in the device type (Device Definition record), not on the device`, and for each group `<where>: <keys> are only kept in the device type (Device Definition record), not on the device sockets` with the given keys of `uuid`, `source`, `pinout` and `extra_data`.

### createConnectCADDevice

Creates a schematic device with all its sockets from a device description.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createConnectCADDevice" · **In runToolBatch:** yes

**Details**

Create a ConnectCAD schematic device with all its sockets from a device description, in the active layer with its insertion point at `position`. With `createDeviceType` true it also creates the device-type symbol '&lt;make&gt; &lt;model&gt;' whose Device Definition record keeps the full description. Returns the device (uuid, deviceName, tag, make, model, rackWidth, rackUnits, bounds, sockets with uuid, name, type, signal, connector, orientation), `warnings` and `deviceType`.

An invalid description creates nothing and returns `errors`.

> **Note:** The ConnectCAD plug-in creates the device at the origin of the active layer, and the tool then moves it to `position`. `deviceName` is the ConnectCAD device name that the description gives as `name`; `name` of the object reference is the Vectorworks object name, which can differ.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `device` | object or string | Yes | Device description (see the group description) as a JSON object or as JSON text. |
| `position` | [point](Common.md#points) |  | Insertion point (default 0, 0). |
| `createDeviceType` | boolean |  | `true`: also create the device-type symbol '&lt;make&gt; &lt;model&gt;' (default `false`). |

**Result**

The new device (see the result of [getConnectCADDevice](#getconnectcaddevice)) and:

| Key | Description |
|---|---|
| `warnings` | Array of texts, only when there are warnings (those of `validateConnectCADDevice`). |
| `deviceType` | Only with `createDeviceType` true: the result of [createConnectCADDeviceType](#createconnectcaddevicetype) (`deviceTypeName`, `isCreated`, `isFullDataStored`, `warnings`, `errors`). |

Errors: `ConnectCAD is not available (the ConnectCAD plug-in is not installed)`. When the description has errors, or the plug-in does not create the device, the `err` is `the device was not created` and `errors` holds the messages of `validateConnectCADDevice` or `ConnectCAD did not create the device (is the ConnectCAD plug-in installed and licensed?)`. A failed call is rolled back (`rolledBack`).

### createConnectCADDevices

Creates several schematic devices in a row in one operation.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createConnectCADDevices" · **In runToolBatch:** yes

**Details**

Create several ConnectCAD devices from an array of device descriptions in one operation, in a row from left to right with their top edges at `origin` and `gap` (drawing units) between them; `createDeviceTypes` also creates their device types. All descriptions are validated first: if any has errors, nothing is created and `invalid` lists them by index.

> **Note:** Each device is created at the origin of the active layer and then moved so that its left edge is at `x` (the first `x` is `origin.x`) and its top edge at `origin.y`. After each device `x` grows by the width of that device plus `gap`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `devices` | array of object or string | Yes | Each item: Device description (see the group description) as a JSON object or as JSON text. The array must not be empty. |
| `origin` | [point](Common.md#points) |  | Left edge of the first device and top edge of all devices (default 0, 0). |
| `gap` | number |  | Space between two devices in drawing units (default 0). |
| `createDeviceTypes` | boolean |  | `true`: also create the device-type symbols (default `false`). |

**Result**

| Key | Description |
|---|---|
| `devices` | Array with one entry per description, in the given order. Each entry is like the result of [createConnectCADDevice](#createconnectcaddevice) (the device with its `bounds` after the move, `warnings`, `deviceType`), or holds the `err` and `errors` of that device when it was not created. |
| `partial` | `true`, only when a device was not created. The result then also has an `err`, and the call is rolled back: the devices that were created are removed again, so the `uuid`s in `devices` no longer exist (check `rolledBack`). Nothing stays in the drawing. |

Errors: `ConnectCAD is not available (the ConnectCAD plug-in is not installed)`; `'devices' must be a non-empty array of device descriptions`; `no device was created: some descriptions have errors`, with `invalid`: an array of objects with `index` (counted from 0) and `errors`; `not every device was created; see the 'err' / 'errors' of each entry`. A failed call is rolled back (`rolledBack`).

### getConnectCADDevice

Reads a ConnectCAD device and its sockets.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read a ConnectCAD device by uuid, name or index: deviceName, tag, description, make, model, rackWidth, rackUnits, isModular, slotCount, bounds and its sockets (uuid, name, type, signal, connector, orientation).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |

**Result**

The [object reference](Common.md#object-references) of the device and:

| Key | Description |
|---|---|
| `deviceName` | The ConnectCAD device name (the `name` of the description). `name` of the reference is the Vectorworks object name. |
| `tag`, `description`, `make`, `model` | Text of the device. |
| `rackWidth` | Text: `non-rack`, `half-rack` or `full-rack`. |
| `rackUnits` | Text: the height in rack units, or `---` when the height is not whole rack units or the device is not a rack device. |
| `isModular`, `slotCount` | Whether the device is modular, and its number of slots. |
| `bounds` | The [rectangle](Common.md#rectangles) of the device. |
| `sockets` | Array of sockets: `uuid`, `name`, `type`, `signal`, `connector`, `orientation`. |

A key is left out when its value cannot be read. Errors: `object not found`; `not a ConnectCAD device`.

### addConnectCADSocket

Adds a socket to a device.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: addConnectCADSocket" · **In runToolBatch:** yes

**Details**

Add a socket to a ConnectCAD device (uuid, name or index): `socketName`, `type` IN | OUT | IO, `signal`, `connector` and `orientation` L | R. It is placed below the sockets of that side and the device grows. Loops and X sockets can only be created with the device (createConnectCADDevice).

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name. |
| `index` | integer |  | Reference by internal index. |
| `socketName` | string | Yes | Name of the new socket: not blank, without `+`, not ending in `_LP`, and not used by another socket of the device. |
| `type` | string | Yes | One of: `IN`, `OUT`, `IO`. |
| `signal` | string | Yes | A ConnectCAD signal type (see `listConnectCADSignals`). |
| `connector` | string | Yes | A ConnectCAD connector type (see `listConnectCADConnectors`). |
| `orientation` | string | Yes | `L` or `R`. |

**Result**

The new socket:

| Key | Description |
|---|---|
| `uuid` | The UUID of the new socket. |
| `name`, `type`, `signal`, `connector`, `orientation` | The values of the socket, as `getConnectCADDevice` lists them. |

A value that is missing or not a string counts as empty and fails the check. Errors: `object not found`; `not a ConnectCAD device`; `the socket was not added`, with `errors`: an array of texts, each starting with `socket '<name>': ` (except the last three), such as `type must be IN, OUT or IO (loops and X sockets only when the device is created)`, `orientation must be L or R (CC_AddSocket)`, `empty socket name`, `'+' in a socket name is a numbering offset in ConnectCAD`, `names ending in _LP are read back as loops`, `signal '<x>' is not a ConnectCAD signal type`, `connector '<x>' is not a ConnectCAD connector type`, `the device already has a socket '<name>'`, `ConnectCAD did not add the socket (is the ConnectCAD plug-in installed and licensed?)` and `ConnectCAD is not available (the ConnectCAD plug-in is not installed)`. A failed call is rolled back (`rolledBack`).

### setConnectCADSocket

Edits a socket.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: setConnectCADSocket" · **In runToolBatch:** yes

**Details**

Edit a ConnectCAD socket by uuid: `socketName`, `type` (IN | OUT | IO), `signal` and `connector` (from the ConnectCAD lists). Invalid values are not written; `applied` reports per setting whether it was written. The socket and its device are regenerated.

> **Note:** `orientation` cannot be changed. A name is refused for a socket of a loop pair (`<name>` and `<name>_LP`), and for a name that is blank, contains `+`, ends in `_LP` or is used by another socket of the device. A refused value is not written and gives `false` in `applied`, without a reason.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string | Yes | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `socketName` | string |  | New name of the socket (see the note above). |
| `type` | string |  | One of: `IN`, `OUT`, `IO`. |
| `signal` | string |  | A ConnectCAD signal type (see `listConnectCADSignals`). |
| `connector` | string |  | From the ConnectCAD lists. |

**Result**

The socket (`uuid`, `name`, `type`, `signal`, `connector`, `orientation`, as `addConnectCADSocket` returns it) and:

| Key | Description |
|---|---|
| `applied` | An entry for each of `socketName`, `type`, `signal` and `connector` that was given: `true` when the value was written, `false` when it was refused or is not a string. |

The call succeeds even when every value was refused. The socket and its device are regenerated only when a value was written. Errors: `object not found`; `not a ConnectCAD socket`.

### createConnectCADDeviceType

Creates the device-type symbol of a device.

> **Effect:** Edit · **Risk:** medium · **Undo:** one step "MCP: createConnectCADDeviceType" · **In runToolBatch:** yes

**Details**

Create the device-type symbol '&lt;make&gt; &lt;model&gt;' with its ConnectCAD Device Definition record from a device (uuid, name or index). With `device` (the description the device was created from) the record keeps the full description (pinout, extra_data, uuid, source, category). A device type with that make and model already in the drawing is kept; one from the ConnectCAD libraries is imported instead (then the description is not written).

> **Note:** `uuid`, `name` and `index` find the device that the type is made from. `name` is not a name for the new symbol, which is always called '&lt;make&gt; &lt;model&gt;'.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name: the name of the device, not of the new symbol. |
| `index` | integer |  | Reference by internal index. |
| `device` | object or string |  | Device description (see the group description) as a JSON object or as JSON text. Not validated: only its make, model, `width_r`, `n_slots`, height, depth, power and weight are compared with the device type; validate it with `validateConnectCADDevice` first. |

**Result**

The [object reference](Common.md#object-references) of the device-type symbol definition (`{}` when there is no symbol) and:

| Key | Description |
|---|---|
| `deviceTypeName` | The name '&lt;make&gt; &lt;model&gt;' (empty when the make or model is missing). |
| `isCreated` | `true` when the symbol was created now, `false` when a symbol of that name was already in the drawing. |
| `isFullDataStored` | `true` only when the description was written to the Device Definition record. |
| `warnings` | Array of texts, only when there are warnings. |
| `errors` | Array of texts, only when there are errors. |

A device type that could not be made is reported in `errors` and is a normal result: it has no `err` and is not rolled back, so check `errors`. Errors of the call itself: `object not found`; `not a ConnectCAD device`.

In `errors`: `a device type needs the make and model of the device`; `ConnectCAD returned no device type '<make> <model>': only Generic and DA devices are supported, another object may have this name, or a library device type with another name was imported (see the Resource Manager)`.

In `warnings`: `a device type '<name>' was already in the drawing; it is kept and the description was not written`; `the device description was not written to the device type: <reason>`, where the reason is `the device description is not one JSON object`, `the make and model of the description differ from the device type` or `the device type has other data than the description (it comes from a ConnectCAD library)`; `the socket groups are too long for the Device Definition record and were not written` (over 32000 characters); `the device type has no ConnectCAD Device Definition record`.

### getConnectCADDeviceType

Reads the Device Definition record of a device-type symbol.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the ConnectCAD Device Definition record of a device-type symbol definition (uuid or name): category, type, make, model, rackMounting, slotCount and the parsed `socketGroups`.

> **Note:** The result has the `type` of the record (a text) in place of the numeric object `type` of the object reference. `rackMounting` and `slotCount` are texts, as the record stores them.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  | Reference by UUID (preferred). See [Object references](Common.md#object-references). |
| `name` | string |  | Reference by name: the name of the device-type symbol definition. |

**Result**

The [object reference](Common.md#object-references) of the symbol definition, then:

| Key | Description |
|---|---|
| `category`, `make`, `model` | Text of the Device Definition record. |
| `type` | The `Type` text of the record. It replaces the numeric `type` of the object reference. |
| `rackMounting` | Text: `non-rack`, `half-rack` or `full-rack`. |
| `slotCount` | The number of slots, as text. |
| `socketGroups` | Array: the parsed `socket groups` of the record, `[]` when it has none. |

Errors: `object not found`; `not a ConnectCAD device type (no ConnectCAD Device Definition record)`.
