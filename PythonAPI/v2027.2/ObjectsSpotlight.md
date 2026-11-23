**English** • [Deutsch](../../PythonAPI.de/v2027.2/ObjectsSpotlight.md) • [日本語](../../PythonAPI.ja/v2027.2/ObjectsSpotlight.md)

# ObjectsSpotlight — lighting devices and GDTF fixture types

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The Spotlight classes (they require Spotlight). `LightingDeviceObject` is a fixture of the lighting plot ("Lighting Device"), drawn from a lighting device symbol, a GDTF fixture type or both. `GDTFLibrary` lists the GDTF fixture types available to Spotlight and imports `.gdtf` files into the drawing.

Generic parameter access comes from [`ParametricObject`](ObjectPrimitives.md#parametricobject).

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [LightingDeviceObject](#lightingdeviceobject)
  - [GDTFLibrary](#gdtflibrary)
    - [GDTFLibrary.Entry](#gdtflibraryentry)
    - [GDTFLibrary.ImportResult](#gdtflibraryimportresult)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`LightingDeviceObject`](#lightingdeviceobject) | class | [`ParametricObject`](ObjectPrimitives.md#parametricobject) | Lighting device plug-in object (universal name "Lighting Device") from the Spotlight plug-in. |
| [`GDTFLibrary`](#gdtflibrary) | class |  | GDTF fixture types (General Device Type Format, DIN SPEC 15800) known to Spotlight. |
| [`GDTFLibrary.Entry`](#gdtflibraryentry) | class (nested) |  | One DMX mode of an available fixture type. |
| [`GDTFLibrary.ImportResult`](#gdtflibraryimportresult) | class (nested) |  | Outcome of Import: the GDTF symbol definition, its GDTF name, whether this call imported it and whether the file was read as GDTF. |

## Classes

### LightingDeviceObject

> **Full name:** `api.LightingDeviceObject` · **Inherits:** [`ParametricObject`](ObjectPrimitives.md#parametricobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Lighting device plug-in object (universal name "Lighting Device") from the Spotlight plug-in.

The generic parameter access (GetParamString / SetParamString / ..., GetParameters, GetParamChoices) comes from ParametricObject.

A lighting device represents one fixture (or a multi-cell lighting device) of a lighting plot. Its graphics come from a lighting device symbol ("Symbol Name") and/or from a GDTF fixture type ("GDTF Fixture Name" with "UseGDTFGeometry"). The GDTF fixture type also supplies the DMX mode and footprint.

Typical GDTF workflow (see GDTFLibrary for the available fixture types):

1. `GDTFLibrary.Import`(path) — - bring the .gdtf file into the drawing (a lighting device can only use a fixture type that is in the drawing)
2. `LightingDeviceObject.Create`(position) — - a device without a lighting device symbol
3. device.SetGDTF(gdtfName, mode) — - fixture type, DMX mode and footprint
4. device.SetUseGDTFGeometry(`True`) — - draw the GDTF 3D model
5. device.`Reset()` — - regenerate the device

Common parameters exposed as named accessors:

- "Inst Type" — instrument type shown in the Object Info palette and in reports
- "Symbol Name" — lighting device symbol of the device (read-only here: assign symbols in Spotlight)
- "GDTF Fixture Name" — GDTF name of the fixture type (`GDTFLibrary.Entry.gdtfName`)
- "GDTF Fixture Mode" — "<DMX mode>.<GDTF name>"; GetGDTFMode returns the DMX mode only
- "Num Channels" — DMX footprint
- "UseGDTFGeometry" — draw the 3D model of the GDTF fixture type

Further parameters for GetParam.../SetParam... (parameter name | type | notes) Multi-cell devices store several of these per cell; the record holds the values of the first cell.

- "Device Type" — popup — Light / ...
- "Purpose", "Position", "Unit Number", "Color", "Dimmer", "Channel" — string
- "Universe", "DMX Address", "Absolute Address", "UniverseAddress" — string / int
- "Circuit Number", "Circuit Name", "System", "Breaker ID" — string
- "Wattage", "Voltage", "Weight", "Cost", "Time", "Mark" — string
- "Frame Size", "Template", "Template2", "TemplateRot1", "TemplateRot2" — string / real (degrees)
- "Field Angle", "Field Angle 2", "Beam Angle", "Beam Angle 2" — real (degrees)
- "Lamp Rotation Angle", "Fall off distance", "Throw Distance" — real
- "Draw Beam", "Draw Beam as Solid", "Use Vertical Beam", "Light On" — bool
- "Focus", "Pan", "Tilt" — string / real (degrees)
- "User Field 1" .. "User Field 6" — string
- "Fixture Mode", "Vision Fixture Name" — string (Vision fixture library)
- "GDTF Fixture Type ID", "GDTF Fixture Custom ID" — string
- "Lightwright ID", "UID" — string

**Constructors**

| Constructor | Description |
|---|---|
| `LightingDeviceObject(h: Handle)` | Refers to the existing lighting device `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D, angle: float = 0.0) -> LightingDeviceObject` *static* | Creates a lighting device without a lighting device symbol at `position`, rotated by `angle` (radians), in the active layer / current container, and regenerates it once. Assign a GDTF fixture type with SetGDTF, then call `Reset()`. |
| `Duplicate() -> LightingDeviceObject` | Duplicates the lighting device in the drawing and returns the copy. |
| `GetInstrumentType() -> str \| None` | Returns the instrument type. |
| `SetInstrumentType(value: str) -> bool` | Sets the instrument type. |
| `GetSymbolName() -> str \| None` | Name of the lighting device symbol of the device; empty for a device without a symbol. |

*GDTF fixture type*

| Method | Description |
|---|---|
| `GetGDTFName() -> str \| None` | Its GDTF name (`GDTFLibrary.Entry.gdtfName`), empty when the device has none. |
| `GetGDTFMode() -> str \| None` | DMX mode of the GDTF fixture type, without the GDTF name the plug-in appends to it. |
| `GetDMXFootprint() -> int \| None` | DMX footprint (number of channels) of the device. |
| `SetGDTF(gdtfName: str, mode: str = '') -> bool` | Assigns the GDTF fixture type `gdtfName` (an imported entry of `GDTFLibrary.GetAvailable`) in the DMX mode `mode` - the first mode of the fixture type when `mode` is empty - and applies its data (mode, footprint, ...) as dropping the GDTF on the device in the Resource Manager does. Call `Reset()` afterwards. Returns `False`, without changing the device, when the drawing has no fixture type with this name and mode. |
| `GetUseGDTFGeometry() -> bool \| None` | Whether the device draws the 3D model of its GDTF fixture type. Call `Reset()` after changing it. |
| `SetUseGDTFGeometry(value: bool) -> bool` | Turns *Use GDTF Geometry* on or off. Whether the device draws the 3D model of its GDTF fixture type. Call `Reset()` after changing it. |

Inherited: everything from [`ParametricObject`](ObjectPrimitives.md#parametricobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### GDTFLibrary

> **Full name:** `api.GDTFLibrary` · **Inherits:** `api.Object`

GDTF fixture types (General Device Type Format, DIN SPEC 15800) known to Spotlight.

The available fixture types are the ones imported into the drawing (stored as GDTF symbol definitions) and the .gdtf files in the GDTF folder of the Spotlight data in the user and application folders. Spotlight reads the folders once per session, so a file copied there later is only listed after a restart. A fixture type must be imported into the drawing (Import) before a lighting device can use it. Requires the Spotlight and GDTF plug-ins; without them the list is empty and Import fails.

**Constructors**

| Constructor | Description |
|---|---|
| `GDTFLibrary()` | Stateless object; every method is static and can be called on the class itself. |

**Methods**

| Method | Description |
|---|---|
| `IsAvailable() -> bool` *static* | Whether the GDTF support of Spotlight is installed. |
| `GetAvailable() -> list[GDTFLibrary.Entry]` *static* | Every DMX mode of every available fixture type: the imported ones first, then the files on disk. `LightingDeviceObject.SetGDTF` only accepts imported fixture types (isInDocument). |
| `Import(filePath: str, replaceExisting: bool = False) -> GDTFLibrary.ImportResult` *static* | Imports the .gdtf file at `filePath` (full native path) into the drawing as a GDTF symbol definition. A fixture type with the same GDTF type ID that is already in the drawing is replaced when `replaceExisting` is `True` and left unchanged otherwise (then isImported is `False`; use GetAvailable to find it). Never asks the user. A new fixture type records its own undo when an undo event is open; replacing an existing one changes it in place and its previous state is not recorded for undo. |

#### GDTFLibrary.Entry

> **Full name:** `api.GDTFLibrary.Entry` · **Inherits:** `api.Object`

One DMX mode of an available fixture type.

**Constructors**

| Constructor | Description |
|---|---|
| `Entry()` | Default value (fields at their defaults). |
| `Entry(gdtfName, fixtureName, manufacturer, mode, footprint, symbolDefinition, isInDocument)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `gdtfName` | `str` | Name to pass to `LightingDeviceObject.SetGDTF`. |
| `fixtureName` | `str` | Fixture type name, followed by "@<revision>" when it has one. |
| `manufacturer` | `str` | Manufacturer of the fixture type. |
| `mode` | `str` | DMX mode name. |
| `footprint` | `int` | DMX channels of the mode. |
| `symbolDefinition` | `Handle` | GDTF symbol definition; null for a file that is not imported. |
| `isInDocument` | `bool` | Imported into the drawing. |

#### GDTFLibrary.ImportResult

> **Full name:** `api.GDTFLibrary.ImportResult` · **Inherits:** `api.Object`

Outcome of Import.

**Constructors**

| Constructor | Description |
|---|---|
| `ImportResult()` | Default value (fields at their defaults). |
| `ImportResult(symbolDefinition, gdtfName, isImported, isValidFile)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `symbolDefinition` | `Handle` | GDTF symbol definition created or replaced by the import. |
| `gdtfName` | `str` | GDTF name of the imported fixture type, for `LightingDeviceObject.SetGDTF`. |
| `isImported` | `bool` | `False` when the file was not read or the fixture type was already in the drawing and kept. |
| `isValidFile` | `bool` | The file was read as GDTF; `False` for a missing or invalid file. |

---

[Back to the index](README.md) · [Back to top](#objectsspotlight--lighting-devices-and-gdtf-fixture-types)
