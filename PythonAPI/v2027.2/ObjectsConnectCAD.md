**English** • [Deutsch](../../PythonAPI.de/v2027.2/ObjectsConnectCAD.md) • [日本語](../../PythonAPI.ja/v2027.2/ObjectsConnectCAD.md)

# ObjectsConnectCAD — ConnectCAD devices and sockets

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The ConnectCAD classes (they require ConnectCAD). `ConnectCADDeviceObject` is a schematic device ("Device") with its sockets, created from a JSON device description; it can also create a device-type symbol that stores the full description. `ConnectCADSocketObject` is a connection point of a device ("Socket": IN, OUT or IO; loops are socket pairs). `ConnectCADLibrary` lists the signal and connector types, validates device descriptions and reads the Device Definition record of device types.

Generic parameter access comes from [`ParametricObject`](ObjectPrimitives.md#parametricobject).

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [ConnectCADLibrary](#connectcadlibrary)
    - [ConnectCADLibrary.Signal](#connectcadlibrarysignal)
    - [ConnectCADLibrary.Connector](#connectcadlibraryconnector)
    - [ConnectCADLibrary.Validation](#connectcadlibraryvalidation)
    - [ConnectCADLibrary.DeviceDefinition](#connectcadlibrarydevicedefinition)
  - [ConnectCADSocketObject](#connectcadsocketobject)
  - [ConnectCADDeviceObject](#connectcaddeviceobject)
    - [ConnectCADDeviceObject.CreateResult](#connectcaddeviceobjectcreateresult)
    - [ConnectCADDeviceObject.AddSocketResult](#connectcaddeviceobjectaddsocketresult)
    - [ConnectCADDeviceObject.DeviceTypeResult](#connectcaddeviceobjectdevicetyperesult)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`ConnectCADLibrary`](#connectcadlibrary) | class |  | ConnectCAD data shared by its devices: the signal and connector types, the validation of device descriptions (JSON) and the Device Definition record of... |
| [`ConnectCADLibrary.Signal`](#connectcadlibrarysignal) | class (nested) |  | A ConnectCAD signal type with its category and preferred connectors. |
| [`ConnectCADLibrary.Connector`](#connectcadlibraryconnector) | class (nested) |  | A ConnectCAD connector type. |
| [`ConnectCADLibrary.Validation`](#connectcadlibraryvalidation) | class (nested) |  | Outcome of ValidateDevice: errors (the device would be wrong) and warnings (data kept only in a device type). |
| [`ConnectCADLibrary.DeviceDefinition`](#connectcadlibrarydevicedefinition) | class (nested) |  | Device Definition record of a device-type symbol definition. |
| [`ConnectCADSocketObject`](#connectcadsocketobject) | class | [`ParametricObject`](ObjectPrimitives.md#parametricobject) | ConnectCAD socket (universal name "Socket"): a connection point of a schematic device, inside the device's profile group. |
| [`ConnectCADDeviceObject`](#connectcaddeviceobject) | class | [`ParametricObject`](ObjectPrimitives.md#parametricobject) | ConnectCAD schematic device (universal name "Device"): a named box with socket objects in its profile group. |
| [`ConnectCADDeviceObject.CreateResult`](#connectcaddeviceobjectcreateresult) | class (nested) |  | Outcome of CreateFromJSON: the device (null when not created), errors and warnings. |
| [`ConnectCADDeviceObject.AddSocketResult`](#connectcaddeviceobjectaddsocketresult) | class (nested) |  | Outcome of AddSocket: the socket (null when not added) and errors. |
| [`ConnectCADDeviceObject.DeviceTypeResult`](#connectcaddeviceobjectdevicetyperesult) | class (nested) |  | Outcome of CreateDeviceType: the device-type symbol definition, whether it is new and whether the full description is in its record. |

## Classes

### ConnectCADLibrary

> **Full name:** `api.ConnectCADLibrary` · **Inherits:** `api.Object`

ConnectCAD data shared by its devices: the signal and connector types, the validation of device descriptions (JSON) and the Device Definition record of device-type symbols.

A device description is one JSON object as ConnectCAD's CC_DeviceFromJSON reads it: { "name", "tag", "description", "make", "model", "category", "width_r": "non-rack" | "half-rack" | "full-rack", "width", "height", "depth" (mm), "power" (W), "weight" (kg), "is_modular" (bool), "n_slots" (int), "socket groups": [ { "qty", "type", "name", "signal", "connector", "orientation", "pinout": [ { "pinID", "name", "sourceID" } ], "extra_data": { ... }, "uuid", "source" } ] } Required: name, tag, make, model, width_r, is_modular, n_slots (> 0 only when modular); a rack device's height is whole rack units (n x 44.45 mm). Socket group types: IN, OUT, IO (one Socket each) and LOOP / IOloop (a pair "<name>" + "<name>_LP": IN + OUT / IO + IO). Orientations: L, R, X (feed-through); loops only L or R. FUSE and BUS are internal-wiring components of a device type, not sockets. qty 1..50 makes "<name> 1".."<name> n". Signals and connectors come from GetSignals and GetConnectors; a pinout lists the pins of its connector with pinIDs unique in the device. Requires the ConnectCAD plug-in and licence; without them IsAvailable is `False` and the lists are empty.

**Constructors**

| Constructor | Description |
|---|---|
| `ConnectCADLibrary()` | Stateless object; every method is static and can be called on the class itself. |

**Methods**

*General*

| Method | Description |
|---|---|
| `IsAvailable() -> bool` *static* | Whether the ConnectCAD plug-in is installed (creating devices also needs the licence). |

*Signal types*

| Method | Description |
|---|---|
| `GetSignals() -> list[ConnectCADLibrary.Signal]` *static* | The ConnectCAD signal files of the application, workgroup and user folders, as ConnectCAD merges them; only the signals ConnectCAD knows in this session are listed. |
| `GetConnectors() -> list[ConnectCADLibrary.Connector]` *static* | Connector types with their pins. |
| `ValidateDevice(deviceJson: str) -> ConnectCADLibrary.Validation` *static* | Checks a device description (one JSON object) as CC_DeviceFromJSON and the Socket object require it. |
| `GetDeviceDefinition(symbolDefinition: Handle) -> ConnectCADLibrary.DeviceDefinition` *static* | The Device Definition record of a device-type symbol definition, including `symbolDefinition`, category, type, make, model, rackMounting, slotCount and socketGroups; `symbolDefinition` is `None` when it has no record. |

#### ConnectCADLibrary.Signal

> **Full name:** `api.ConnectCADLibrary.Signal` · **Inherits:** `api.Object`

A ConnectCAD signal type.

**Constructors**

| Constructor | Description |
|---|---|
| `Signal()` | Default value (fields at their defaults). |
| `Signal(name, category, description, defaultConnector, connectors)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `name` | `str` | Universal name, e.g. "HDMI". |
| `category` | `str` | E.g. "Video". |
| `description` | `str` | Description of the signal type. |
| `defaultConnector` | `str` | Default connector type of the signal. |
| `connectors` | `list[str]` | Preferred connectors (all of them in GetConnectors). |

#### ConnectCADLibrary.Connector

> **Full name:** `api.ConnectCADLibrary.Connector` · **Inherits:** `api.Object`

A ConnectCAD connector type.

**Constructors**

| Constructor | Description |
|---|---|
| `Connector()` | Default value (fields at their defaults). |
| `Connector(name, localizedName, category, pins)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `name` | `str` | Universal name, e.g. "XLR3F". |
| `localizedName` | `str` | Localized display name. |
| `category` | `str` | Localized folder. |
| `pins` | `list[str]` | Pin names in order, for a socket group "pinout". |

#### ConnectCADLibrary.Validation

> **Full name:** `api.ConnectCADLibrary.Validation` · **Inherits:** `api.Object`

Outcome of ValidateDevice.

**Constructors**

| Constructor | Description |
|---|---|
| `Validation()` | Default value (fields at their defaults). |
| `Validation(errors, warnings, isValid)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `errors` | `list[str]` | The device would be wrong or the plug-in would fail. |
| `warnings` | `list[str]` | Data that is only kept in a device type. |
| `isValid` | `bool` | Whether the description is valid. |

#### ConnectCADLibrary.DeviceDefinition

> **Full name:** `api.ConnectCADLibrary.DeviceDefinition` · **Inherits:** `api.Object`

Device Definition record of a device-type symbol definition.

**Constructors**

| Constructor | Description |
|---|---|
| `DeviceDefinition()` | Default value (fields at their defaults). |
| `DeviceDefinition(symbolDefinition, category, type, make, model, rackMounting, slotCount, socketGroups)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `symbolDefinition` | `Handle` | Device-type symbol definition. |
| `category` | `str` | Device category. |
| `type` | `str` | Device type. |
| `make` | `str` | Manufacturer. |
| `model` | `str` | Model. |
| `rackMounting` | `str` | Non-rack, half-rack, full-rack. |
| `slotCount` | `str` | Number of slots (modular devices). |
| `socketGroups` | `str` | JSON: { "socket groups": [ ... ] }. |

### ConnectCADSocketObject

> **Full name:** `api.ConnectCADSocketObject` · **Inherits:** [`ParametricObject`](ObjectPrimitives.md#parametricobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

ConnectCAD socket (universal name "Socket"): a connection point of a schematic device, inside the device's profile group. Its type is IN, OUT or IO; a loop is a pair of sockets "<name>" and "<name>_LP". The graphics follow the type and orientation (connector symbol "skt_con_<type>" or, for X, "skt_con_classic_<type>"). The setters validate the value (type IN/OUT/IO, ConnectCAD signal and connector types) and regenerate the socket and its device. Register the device for undo before changing a socket (`Document.AddBothSwapObject`).

**Constructors**

| Constructor | Description |
|---|---|
| `ConnectCADSocketObject(h: Handle)` | Refers to the existing ConnectCAD socket `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Duplicate() -> ConnectCADSocketObject` | Duplicates the ConnectCAD socket in the drawing and returns the copy. |
| `GetDevice() -> Handle` | The device that owns the socket; null when the socket is not in a device. |
| `GetSocketName() -> str \| None` | Returns the socket name. |
| `SetSocketName(name: str) -> bool` | Must not be empty, contain '+' (numbering offset), end in "_LP" (loop output) or be used by another socket of the device. The sockets of a loop cannot be renamed. |
| `GetTag() -> str \| None` | Returns the tag. |
| `GetSocketType() -> str \| None` | IN, OUT or IO. |
| `SetSocketType(type: str) -> bool` | Sets the socket type. IN, OUT or IO. |
| `GetSignal() -> str \| None` | Returns the signal. |
| `SetSignal(signal: str) -> bool` | A signal type of `ConnectCADLibrary.GetSignals`. |
| `GetConnector() -> str \| None` | Returns the connector. |
| `SetConnector(connector: str) -> bool` | A connector type of `ConnectCADLibrary.GetConnectors`. |
| `GetOrientation() -> str \| None` | L, R or X; set when the device is created (the socket symbol depends on it). |
| `IsLoopOutput() -> bool` | Whether this socket is the output "<name>_LP" of a loop. |

Inherited: everything from [`ParametricObject`](ObjectPrimitives.md#parametricobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### ConnectCADDeviceObject

> **Full name:** `api.ConnectCADDeviceObject` · **Inherits:** [`ParametricObject`](ObjectPrimitives.md#parametricobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

ConnectCAD schematic device (universal name "Device"): a named box with socket objects in its profile group.

CreateFromJSON builds a device and its sockets from a device description (see ConnectCADLibrary for the JSON) after checking it with `ConnectCADLibrary.ValidateDevice`; an invalid description creates nothing. Devices carry name, tag, description, make, model, rack width / units, modular / slots, power and weight; category, pinout, extra_data, uuid and source live only in the device type (CreateDeviceType).

Undo: CreateFromJSON records the new device itself. Before AddSocket or socket edits, register the device for undo (`Document.AddBothSwapObject`). Requires the ConnectCAD plug-in and licence.

**Constructors**

| Constructor | Description |
|---|---|
| `ConnectCADDeviceObject(h: Handle)` | Refers to the existing ConnectCAD device `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `CreateFromJSON(deviceJson: str, position: Math.Point2D) -> ConnectCADDeviceObject.CreateResult` *static* | Creates a device with its sockets from a device description (one JSON object) in the active layer, with its insertion point at `position`. Nothing is created when the description has errors. |
| `Duplicate() -> ConnectCADDeviceObject` | Duplicates the ConnectCAD device in the drawing and returns the copy. |
| `GetDeviceName() -> str \| None` | Returns the device name. |
| `GetTag() -> str \| None` | Returns the tag. |
| `GetDescription() -> str \| None` | Returns the description. |
| `GetMake() -> str \| None` | Returns the make. |
| `GetModel() -> str \| None` | Returns the model. |
| `GetRackWidth() -> str \| None` | Non-rack, half-rack or full-rack. |
| `GetRackUnits() -> str \| None` | Rack units derived from the height ("---" when not whole units or not a rack device). |
| `IsModular() -> bool \| None` | True when the device is modular (has slots for cards). |
| `GetSlotCount() -> int \| None` | Number of slot items. |
| `GetSockets() -> list[ConnectCADSocketObject]` | The sockets of the device in drawing order; a loop is two sockets ("<name>" and "<name>_LP"). |
| `AddSocket(name: str, type: str, signal: str, connector: str, orientation: str) -> ConnectCADDeviceObject.AddSocketResult` | Adds an IN, OUT or IO socket on side L or R below the existing sockets of that side and grows the device. Returns a result with the new `socket` and `errors`; `socket` is `None` when the socket was not added. Loops and X sockets can only be created with the device (`CreateFromJSON`). |
| `CreateDeviceType(deviceJson: str = '') -> ConnectCADDeviceObject.DeviceTypeResult` | Creates the device-type symbol definition "<make> <model>" with a "ConnectCAD Device Definition" record from this device (ConnectCAD CC_DeviceType). With `deviceJson` (the description the device was created from) the record keeps the full description: pinout, extra_data, uuid, source and category. A device type with this make and model that is already in the drawing is kept unchanged; one from the ConnectCAD libraries is imported instead of creating a new one. |

Inherited: everything from [`ParametricObject`](ObjectPrimitives.md#parametricobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### ConnectCADDeviceObject.CreateResult

> **Full name:** `api.ConnectCADDeviceObject.CreateResult` · **Inherits:** `api.Object`

Outcome of CreateFromJSON.

**Constructors**

| Constructor | Description |
|---|---|
| `CreateResult()` | Default value (fields at their defaults). |
| `CreateResult(device, errors, warnings)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `device` | `Handle` | Null when nothing was created. |
| `errors` | `list[str]` | Why the device was not created. |
| `warnings` | `list[str]` | Data that is only kept in a device type. |

#### ConnectCADDeviceObject.AddSocketResult

> **Full name:** `api.ConnectCADDeviceObject.AddSocketResult` · **Inherits:** `api.Object`

Outcome of AddSocket.

**Constructors**

| Constructor | Description |
|---|---|
| `AddSocketResult()` | Default value (fields at their defaults). |
| `AddSocketResult(socket, errors)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `socket` | `Handle` | Null when no socket was added. |
| `errors` | `list[str]` | Error messages. |

#### ConnectCADDeviceObject.DeviceTypeResult

> **Full name:** `api.ConnectCADDeviceObject.DeviceTypeResult` · **Inherits:** `api.Object`

Outcome of CreateDeviceType.

**Constructors**

| Constructor | Description |
|---|---|
| `DeviceTypeResult()` | Default value (fields at their defaults). |
| `DeviceTypeResult(symbolDefinition, name, isCreated, isFullDataStored, errors, warnings)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `symbolDefinition` | `Handle` | The device-type symbol definition; null on failure. |
| `name` | `str` | "<make> <model>". |
| `isCreated` | `bool` | `False`: a device type with this make and model was already in the drawing and is kept. |
| `isFullDataStored` | `bool` | The device description (pinout, extra_data, category, ...) is in its record. |
| `errors` | `list[str]` | Error messages. |
| `warnings` | `list[str]` | Warning messages. |

---

[Back to the index](README.md) · [Back to top](#objectsconnectcad--connectcad-devices-and-sockets)
