**English** • [Deutsch](../../PythonAPI.de/v2027.2/ObjectsAnnotation.md) • [日本語](../../PythonAPI.ja/v2027.2/ObjectsAnnotation.md)

# ObjectsAnnotation — dimensions, data tags, title block borders and worksheets

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The annotation classes. Annotation objects do not describe the building, they describe the drawing: they read data out of objects and the document and print it on the sheet.

`AnnotationObject` is the base of the plug-in based annotations (`DataTagObject` labels an object with data read from it, `TitleBlockBorderObject` is the sheet border, zone grid and title block). Both take their graphics from an object **style**, so their `Create` functions resolve a style (importing one from the Vectorworks content when the drawing has none) and fail when none is available.

Dimensions are the other half of annotation: `DimensionObject` holds the settings every dimension shares, and `LinearDimensionObject`, `AngularDimensionObject`, `ArcLengthDimensionObject` and `RadialDimensionObject` measure distances, angles, arc lengths and radii/diameters. Unlike data tags and title block borders, dimensions are native objects without a plug-in record or style: their look comes from the dimension standard they reference. `CenterMarkObject` is the center cross of a circle or arc (a group of lines, not a dimension). `WorksheetObject` edits worksheet resources.

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [AnnotationObject](#annotationobject)
  - [DataTagObject](#datatagobject)
    - [DataTagObject.LeaderType](#datatagobjectleadertype)
    - [DataTagObject.HorizontalPosition](#datatagobjecthorizontalposition)
    - [DataTagObject.MoveBehaviour](#datatagobjectmovebehaviour)
  - [TitleBlockBorderObject](#titleblockborderobject)
    - [TitleBlockBorderObject.Revision](#titleblockborderobjectrevision)
  - [DimensionObject](#dimensionobject)
  - [LinearDimensionObject](#lineardimensionobject)
  - [AngularDimensionObject](#angulardimensionobject)
  - [ArcLengthDimensionObject](#arclengthdimensionobject)
  - [RadialDimensionObject](#radialdimensionobject)
  - [CenterMarkObject](#centermarkobject)
  - [WorksheetObject](#worksheetobject)
    - [WorksheetObject.Range](#worksheetobjectrange)
    - [WorksheetObject.NumberFormat](#worksheetobjectnumberformat)
    - [WorksheetObject.TextFormat](#worksheetobjecttextformat)
    - [WorksheetObject.Fill](#worksheetobjectfill)
    - [WorksheetObject.Borders](#worksheetobjectborders)
- [Enumerations](#enumerations)
  - [DimensionKind](#dimensionkind)
  - [DimensionTolerance](#dimensiontolerance)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`AnnotationObject`](#annotationobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Common base of the annotation plug-in object classes (data tag, title block border). |
| [`DataTagObject`](#datatagobject) | class | [`AnnotationObject`](#annotationobject) | Data tag plug-in object (universal name "Data Tag") from Plug-Ins/Shipping/DataTag. |
| [`DataTagObject.LeaderType`](#datatagobjectleadertype) | IntEnum (nested) |  | Shape of the leader of a data tag ("Leader Type"). |
| [`DataTagObject.HorizontalPosition`](#datatagobjecthorizontalposition) | IntEnum (nested) |  | Which side of the leader the tag text sits on ("Horizontal Position"). |
| [`DataTagObject.MoveBehaviour`](#datatagobjectmovebehaviour) | IntEnum (nested) |  | What dragging the tag in the drawing moves: the whole tag, or only the tip of its leader. |
| [`TitleBlockBorderObject`](#titleblockborderobject) | class | [`AnnotationObject`](#annotationobject) | Title block border plug-in object (universal name "Title Block Border") from Plug-Ins/Shipping/TitleBlockBorder. |
| [`TitleBlockBorderObject.Revision`](#titleblockborderobjectrevision) | class (nested) |  | One revision of a title block: number, date, note, publish date and recipients. |
| [`DimensionObject`](#dimensionobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Base class of every dimension object (`ObjectType.Dimension`). |
| [`LinearDimensionObject`](#lineardimensionobject) | class | [`DimensionObject`](#dimensionobject) | Linear dimension: measures the distance between two points. |
| [`AngularDimensionObject`](#angulardimensionobject) | class | [`DimensionObject`](#dimensionobject) | Angular dimension: measures the angle between two legs meeting at a vertex. |
| [`ArcLengthDimensionObject`](#arclengthdimensionobject) | class | [`DimensionObject`](#dimensionobject) | Arc length dimension: measures the length ALONG an arc rather than the straight distance between its endpoints, which is what a linear dimension would report. |
| [`RadialDimensionObject`](#radialdimensionobject) | class | [`DimensionObject`](#dimensionobject) | Radial and diametrical dimension: measures the radius or the diameter of a circle or arc. |
| [`CenterMarkObject`](#centermarkobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Center mark: the cross that marks the centre of a circle or an arc. |
| [`WorksheetObject`](#worksheetobject) | class | [`TypedResource`](Resources.md#typedresource) | Non-owning worksheet RESOURCE, not a placed worksheet image or an annotation plug-in object. |
| [`WorksheetObject.Range`](#worksheetobjectrange) | class (nested) |  | Inclusive 1-based worksheet range. |
| [`WorksheetObject.NumberFormat`](#worksheetobjectnumberformat) | class (nested) |  | Native worksheet number format, including format-dependent accuracy and UTF-8 leader/trailer. |
| [`WorksheetObject.TextFormat`](#worksheetobjecttextformat) | class (nested) |  | Worksheet text: point size, font/style, alignments, degree angle, ColorRef index and wrap. |
| [`WorksheetObject.Fill`](#worksheetobjectfill) | class (nested) |  | Native fill style, document ColorRef indices and pattern. |
| [`WorksheetObject.Borders`](#worksheetobjectborders) | class (nested) |  | Cell border flags plus outline and inside range application flags. |
| [`DimensionKind`](#dimensionkind) | IntEnum |  | Kind of dimension an object is. |
| [`DimensionTolerance`](#dimensiontolerance) | IntEnum |  | How much a dimension deviates from its nominal value, printed next to the measurement. |

## Classes

### AnnotationObject

> **Full name:** `api.AnnotationObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Common base of the annotation plug-in object classes (data tag, title block border).

An annotation object does not describe a piece of the building: it describes the drawing. It reads data from the objects and from the document and prints it on the sheet. Both annotation objects are Vectorworks plug-in objects (also called parametric objects in the API) identified by their universal (parametric) name - "Data Tag" and "Title Block Border".

What sets these two apart from the Architect / Landmark classes is that their graphics come almost entirely from an object STYLE (a "plug-in style"): a symbol definition that holds a master instance of the plug-in plus the text and geometry layout that is stamped onto every object using that style. An unstyled data tag has no text layout and an unstyled title block border has no title block graphics, so both classes resolve a style when they create the object - see `DataTagObject.Create` and `TitleBlockBorderObject.Create` - and expose the style through GetStyleName / SetStyle.

Conventions carried over from PrimitiveObject:

- Getters return `None` for an invalid object or a missing parameter.
- Setters return `True` on success and `False` for an invalid object or a missing parameter.
- Lengths are in world units, angles in radians, strings are UTF-8.

Parameter access primer (Get/SetParam*):

- Every annotation object stores its data as a record with named fields ("parameters"). Each subclass lists the useful parameter names in its "Full parameter reference". Use those names verbatim (case-sensitive, UTF-8) with GetParamString / SetParamString / GetParamReal / ... to read or write any field the subclass does not already expose through a dedicated typed accessor.
- Parameter types in the tables use these tags:

- string — text (UTF-8) - GetParamString / SetParamString
- int — 32-bit integer - GetParamInt / SetParamInt
- bool — boolean - GetParamBool / SetParamBool
- real — floating-point (world coordinate, angle in DEGREES, plain number, ...) - GetParamReal / SetParamReal
- popup — one-of-N string choice - GetParamString / SetParamString; valid values are listed next to the parameter

- Parameter names that start with a double underscore ("__") are the plug-in's private state; they are readable but not usually meaningful to change directly.
- A parameter that the object takes "by style" is read from the style symbol definition; writing it on the instance has no lasting effect until the parameter is switched to "by instance".

**Constructors**

| Constructor | Description |
|---|---|
| `AnnotationObject(h: Handle)` | Refers to any object `h` as a generic `AnnotationObject`; `IsValid()` only checks for a non-null handle. Use `GetParametricName()` or a concrete class's `Is(h)` to check the object kind. |

**Methods**

*General*

| Method | Description |
|---|---|
| `GetParametricName() -> str \| None` | Universal (parametric) name of this object, "Data Tag" or "Title Block Border". Empty when the object is invalid or the underlying handle is not a plug-in object. |
| `HasParam(univParamName: str) -> bool` | Whether this plug-in object has a field with the given universal name. |
| `GetParamNames() -> list[str]` | Ordered list of every parameter (universal) name defined by this object's plug-in. |
| `GetParamString(univParamName: str) -> str \| None` | Generic, string-keyed field accessors. Prefer the typed named accessors on the subclasses when available; use these for parameters that do not have a dedicated accessor. The getters return `None` when the parameter does not exist; the setters return `False`. |
| `SetParamString(univParamName: str, value: str) -> bool` | Sets the param string. Generic, string-keyed field accessors. Prefer the typed named accessors on the subclasses when available; use these for parameters that do not have a dedicated accessor. The getters return `None` when the parameter does not exist; the setters return `False`. |
| `GetParamReal(univParamName: str) -> float \| None` | Returns the param real for `univParamName`. |
| `SetParamReal(univParamName: str, value: float) -> bool` | Sets the param real. |
| `GetParamBool(univParamName: str) -> bool \| None` | Whether *Param Bool* is on for `univParamName`. |
| `SetParamBool(univParamName: str, value: bool) -> bool` | Sets the param bool. |
| `GetParamInt(univParamName: str) -> int \| None` | Returns the param int for `univParamName`. |
| `SetParamInt(univParamName: str, value: int) -> bool` | Sets the param int. |

*object style (plug-in style)*

| Method | Description |
|---|---|
| `GetStyleHandle() -> Handle` | Symbol definition of the style the object is attached to, null when the object is unstyled. |
| `GetStyleName() -> str \| None` | Name of that style resource; `None` when the object is unstyled or the object is invalid. |
| `IsStyled() -> bool` | True when the object uses an object style. |
| `SetStyle(styleName: str) -> bool` | Attaches the object to the style resource of the current drawing named `styleName` and takes over its by-style parameter values. Fails when no such resource exists or it is not a plug-in style. The subclasses add a Ensure*`Style()` static that imports the style from the Vectorworks content first. |
| `SetStyle(hStyleSymbolDefinition: Handle) -> bool` | Attaches the object to the style resource of the current drawing named `styleName` and takes over its by-style parameter values. Fails when no such resource exists or it is not a plug-in style. The subclasses add a Ensure*`Style()` static that imports the style from the Vectorworks content first. |
| `RemoveStyle() -> bool` | Detaches the object from its style; every parameter becomes "by instance" and keeps its current value. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### DataTagObject

> **Full name:** `api.DataTagObject` · **Inherits:** [`AnnotationObject`](#annotationobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Data tag plug-in object (universal name "Data Tag") from Plug-Ins/Shipping/DataTag.

A data tag labels another object with data read out of that object: its record fields, its plug-in parameters, its class, its attributes, worksheet formulas, ... The text layout of the tag - which fields it shows, in what arrangement, inside which bubble - lives entirely in the tag's STYLE, a plug-in style symbol definition. A data tag without a style therefore displays nothing at all, which is why `Create()` always resolves a style (importing one from the Vectorworks content when the drawing has none) and fails when no data tag style is available anywhere.

The second half of a usable tag is the association with the object it describes: the tag reads its data from the object it is attached to, and it follows that object when the object moves. `Create()` takes the object to tag; AttachTo / DetachFrom change it later.

Common parameters exposed as named accessors:

- "Use Leader" — whether the tag draws a leader line to the tagged object
- "Leader Type" — shape of that leader (see `DataTagObject.LeaderType` below)
- "Leader Length" — length of the leader, world units
- "Leader Angle" — angle of the leader (the accessors use radians, the raw parameter degrees)
- "Shoulder Length" — length of the horizontal shoulder between leader and text
- "Horizontal Position" — which side of the leader the text sits on (see `DataTagObject.HorizontalPosition`)
- "Move Behaviour" — what dragging the tag moves (see `DataTagObject.MoveBehaviour`)
- "X Offset"/"Y Offset" — offset of the tag from the tagged object, world units

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Leader and shoulder

- "Use Leader" — bool
- "Leader Type" — popup — Line / Arc / Bezier
- "Leader Length" — real — world units
- "Leader Angle" — real — degrees
- "Leader Radius" — real — world units (arc leader)
- "Shoulder Length" — real — world units
- "Use Marker" — bool — draw a marker at the leader end
- "Clip Leader" — bool
- "Leader/Shoulder Class" — string — class of the leader and shoulder geometry
- "__Marker", "__Marker Style", "__Marker Angle", "__Marker Size", "__Marker Width", "__Marker Thickness Basis", "__Marker Thickness" — marker definition (internal)
- "__Bezier Length Factor 1/2", "__Bezier Offset1/2" — bezier leader shape (internal)
- "__LeaderEndX", "__LeaderEndY" — real — local unassociated leader coordinates (use Get/SetLeaderEnd)

Placement

- "Horizontal Position" — popup — Left / Right / Auto
- "Move Behaviour" — popup — Entire Tag / Leader End
- "Offset Mode" — popup — Global / Local
- "X Offset", "Y Offset" — real — world units
- "Align to Walls" — bool
- "Wall Alignment" — popup — Unconstrained / Center Line / Left Edge / Right Edge
- "World-based" — bool — keep the tag oriented to the world, not to the view
- "MirrorElements" — bool
- "Allow Mult Att Points" — bool
- "__RefOffsetX/Y/Z", "__RefCenterX/Y/Z", "__MoveOffsetX/Y/Z" — real (internal placement state)
- "__RefWallOffset", "__IsRefWallLeftSide", "__RefOffsetFromWall", "__RefWallCenterOffse", "__IsRefWallCenterLeftSide", "__RefCenterOffsetFromWall" — (internal)

Scaling

- "Scaling" — popup — None / Symmetric / Asymmetric
- "Scale Text" — bool
- "X Scale", "Y Scale" — real

Eligibility (which objects this tag may be attached to)

- "UseCriteriaEligibility" — bool
- "__CriteriaEligibility" — string — Vectorworks criteria, e.g. "((ALL))"
- "SubpartMode" — bool — tag sub-parts of the object instead of the object
- "EnableOverlappingVerticalChains" — bool

Dialogs / internal state

- "Always Display ETD Dialog" — bool
- "__Edit Tag Layout" — string — (static text placeholder in the OIP)
- "__Was Moved", "__Is For Updating", "__Is For Moving", "__Was Rotated From OIP" — bool
- "__IsCompensateAngleUsed", "__IsBubbleFlipped" — bool
- "__Version" — int

**Constructors**

| Constructor | Description |
|---|---|
| `DataTagObject(h: Handle)` | Refers to the existing data tag `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D, styleName: str = '', hObjectToTag: Handle = None) -> DataTagObject` *static* | Creates a data tag at `position` that tags `hObjectToTag` (which may be null for a free-standing tag). `styleName` selects the data tag style: it is looked up in the drawing first and imported from the Vectorworks data tag content when it is not there yet. Leave it empty to use any available style. Returns an invalid object when no data tag style can be found at all - a tag without a style has no text layout and would be invisible. |
| `EnsureStyle(styleName: str = '') -> str` *static* | Makes sure a data tag style named `styleName` exists in the current drawing, importing it from the Vectorworks content when needed. Returns the name of the style that is now available (which may differ from the requested one when that one does not exist), or an empty string when there is none. |
| `Duplicate() -> DataTagObject` | Duplicates the data tag in the drawing and returns the copy. |

*association*

| Method | Description |
|---|---|
| `GetTaggedObject() -> Handle` | The object this tag reads its data from; null for a tag that is not attached to anything. |
| `AttachTo(hObject: Handle) -> bool` | Attaches the tag to `hObject` (replacing the current association) and refreshes the tag text. |
| `DetachFrom(hObject: Handle = None) -> bool` | Detaches the tag from `hObject`. Pass null to detach it from whatever it is tagging. |
| `CanBeTagged(hObject: Handle) -> bool` *static* | Whether `hObject` is a kind of object a data tag may be attached to. |
| `GetTagsOfObject(hObject: Handle) -> list[Handle]` *static* | Every data tag attached to `hObject`. |

*content*

| Method | Description |
|---|---|
| `GetExtractedData() -> list[tuple[str, str]]` | The data the tag currently displays, as (label, value) pairs. The label is the field label defined in the tag layout; the value is the text the tag actually prints for the tagged object. |
| `Update() -> bool` | Re-reads the data from the tagged object and redraws the tag. |

*leader*

| Method | Description |
|---|---|
| `GetUseLeader() -> bool \| None` | Whether *Use Leader* is on. |
| `SetUseLeader(value: bool) -> bool` | Turns *Use Leader* on or off. |
| `GetLeaderType() -> DataTagObject.LeaderType \| None` | Returns the leader type. |
| `SetLeaderType(value: DataTagObject.LeaderType) -> bool` | Sets the leader type. |
| `GetLeaderLength() -> float \| None` | Returns the leader length (world units). |
| `SetLeaderLength(value: float) -> bool` | Sets the leader length. |
| `GetLeaderAngle() -> float \| None` | Returns the leader angle (radians). |
| `SetLeaderAngle(radians: float) -> bool` | Sets the leader angle. |
| `GetShoulderLength() -> float \| None` | Returns the shoulder length (world units). |
| `SetShoulderLength(value: float) -> bool` | Sets the shoulder length. |
| `GetUseMarker() -> bool \| None` | Whether *Use Marker* is on. |
| `SetUseMarker(value: bool) -> bool` | Turns *Use Marker* on or off. |
| `GetLeaderEnd() -> Math.Point2D \| None` | Tip of the leader line, in world units. Setting it moves the leader end without moving the tag text. Global/model XY, for associated and unassociated tags. Getter requires an enabled leader and native leader provider; empty for tilted enclosing plug-in objects (provider is XY-only). |
| `SetLeaderEnd(position: Math.Point2D) -> bool` | Sets the leader end. Tip of the leader line, in world units. Setting it moves the leader end without moving the tag text. Global/model XY, for associated and unassociated tags. Getter requires an enabled leader and native leader provider; empty for tilted enclosing plug-in objects (provider is XY-only). |

*placement*

| Method | Description |
|---|---|
| `GetHorizontalPosition() -> DataTagObject.HorizontalPosition \| None` | Returns the horizontal position. |
| `SetHorizontalPosition(value: DataTagObject.HorizontalPosition) -> bool` | Sets the horizontal position. |
| `GetMoveBehaviour() -> DataTagObject.MoveBehaviour \| None` | Returns the move behaviour. |
| `SetMoveBehaviour(value: DataTagObject.MoveBehaviour) -> bool` | Sets the move behaviour. |
| `GetOffset() -> Math.Point2D \| None` | Offset of the tag from the object it tags, in world units. |
| `SetOffset(offset: Math.Point2D) -> bool` | Sets the offset. Offset of the tag from the object it tags, in world units. |
| `GetAlignToWalls() -> bool \| None` | Whether *Align To Walls* is on. |
| `SetAlignToWalls(value: bool) -> bool` | Turns *Align To Walls* on or off. |

*eligibility*

| Method | Description |
|---|---|
| `GetUseCriteriaEligibility() -> bool \| None` | Whether the tag restricts the objects it may be attached to by a criteria string. |
| `SetUseCriteriaEligibility(value: bool) -> bool` | Turns *Use Criteria Eligibility* on or off. Whether the tag restricts the objects it may be attached to by a criteria string. |
| `GetEligibilityCriteria() -> str \| None` | The Vectorworks criteria string used when the restriction is on, e.g. "((ALL))" or "((PON=`Door`))". |
| `SetEligibilityCriteria(criteria: str) -> bool` | Sets the eligibility criteria. The Vectorworks criteria string used when the restriction is on, e.g. "((ALL))" or "((PON=`Door`))". |

Inherited: everything from [`AnnotationObject`](#annotationobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### DataTagObject.LeaderType

> **Full name:** `api.DataTagObject.LeaderType` · **Kind:** `IntEnum`

Shape of the leader of a data tag ("Leader Type").

| Member | Value | Description |
|---|---|---|
| `Line` | `0` |  |
| `Arc` | `1` |  |
| `Bezier` | `2` |  |

#### DataTagObject.HorizontalPosition

> **Full name:** `api.DataTagObject.HorizontalPosition` · **Kind:** `IntEnum`

Which side of the leader the tag text sits on ("Horizontal Position").

| Member | Value | Description |
|---|---|---|
| `Left` | `0` |  |
| `Right` | `1` |  |
| `Auto` | `2` |  |

#### DataTagObject.MoveBehaviour

> **Full name:** `api.DataTagObject.MoveBehaviour` · **Kind:** `IntEnum`

What dragging the tag in the drawing moves: the whole tag, or only the tip of its leader.

| Member | Value | Description |
|---|---|---|
| `EntireTag` | `0` |  |
| `LeaderEnd` | `1` |  |

### TitleBlockBorderObject

> **Full name:** `api.TitleBlockBorderObject` · **Inherits:** [`AnnotationObject`](#annotationobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Title block border plug-in object (universal name "Title Block Border") from Plug-Ins/Shipping/TitleBlockBorder.

A title block border is the frame of a sheet: the sheet border with its margins and zone grid, plus the title block itself - the block of text in the corner that prints the project name, the client, the sheet number, the scale, the issue and revision history, and so on. It is normally placed on a sheet layer, one per sheet.

Like the data tag, its graphics live in a STYLE (a plug-in style symbol definition): the style decides what the title block looks like and which fields it prints. A title block border without a style draws only an empty border, so `Create()` resolves a style - importing one from the Vectorworks title block border content when the drawing has none - and fails when there is no style to be had.

The data a title block prints comes from three places:

- the object's own parameters (sheet size, margins, zones, north point, drawing stamp, ...), reachable through the typed accessors below and through Get/SetParam...;
- the SHEET DATA, a set of named fields stored per title block border object (sheet title, sheet number, drawn by, checked by, ...) - see GetSheetData / SetSheetData;
- the PROJECT DATA, a set of named fields stored once per document and shared by every title block border (project name, client, address, ...) - see the static GetProjectData / SetProjectData.

Revisions and issues are read with GetRevisions / GetIssueDates.

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Sheet

- "Sheet Size ID" — int — index of the predefined sheet size, -1 for a custom size
- "Sheet Size Name" — string — e.g. "ANSI D", "ISO A1"
- "Sheet Width", "Sheet Height" — real — world units (custom sizes)
- "Sheet Orientation" — popup — portrait / landscape
- "Sheet Fit Method" — popup — how the border is fitted to the page
- "Lock To Page Center" — bool
- "Sheet Margin Left/Right/Top/Bottom" — real — world units
- "Sheet Hide Border" — bool
- "Border Use Object Line Weight" — bool
- "Border Line Weight" — real
- "Sheet Fill Border" — bool
- "Display Format" — popup
- "Units" — popup — units the sheet size is expressed in
- "Show unit mark" — bool
- "Use custom name" — bool

Sheet zones (the A/B/C - 1/2/3 grid printed along the border) "Show Grids", "Show Grid Lines", "Show Grid Lines Extensions"	bool

- "Vertical Zones", "Horizontal Zones" — int
- "Grid Text Order", "Grid Number Order" — popup
- "Grid Label Size" — real
- "Grid Marker Line Length" — real
- "Draw Crop Marks" — bool
- "Crop Marks Line Weight" — real
- "Fold Mark" — popup
- "Fold Mark Class" — string
- "Margin Width", "Folded Width", "Folded Height" — real
- "Zoom In to Title Block" — bool
- "Graphics Scale" — real
- "__Version" — int

Title block

- "Use As Title Block" — bool — draw the title block, not just the border
- "Title Block Position" — popup — corner of the sheet the title block sits in
- "Title Block Margin" — real
- "Scale Factor" — real
- "Use Layout Text Attributes" — bool
- "Countersignature" — bool
- "This Title Block Is Active" — bool — the title block that feeds the document's sheet data
- "Use Auto Drawing Coordination" — bool

Sheet / revision / issue data

- "Plot Date Format" — popup
- "Scale" — string
- "Date" — string
- "Current Revision Number" — string
- "Show Revisions Count" — int — how many revision rows to print
- "Revision Line Spacing" — real
- "Revision Direction" — popup — up / down
- "Current Issue Number" — string
- "Show Issues Count" — int
- "Issue Line Spacing" — real
- "Issue Direction" — popup
- "Issue Increment", "Revision Increment" — int
- "Issue Mark", "Revision Mark" — string

North point

- "Display North Arrow" — bool
- "North Arrow Symbol" — string — symbol definition name
- "North Angle" — real — DEGREES (GetNorthAngle/SetNorthAngle use radians)
- "North Scale Factor" — real
- "Selected Heliodon City", "Selected Heliodon Country" — string
- "Use Heliodon Rotation Angle" — bool
- "Show MN Declination" — bool
- "Declination Degree Offset" — real — degrees
- "North Default Position X", "North Default Position Y" — real — world units

Drawing stamp (the "PRELIMINARY - NOT FOR CONSTRUCTION" overlay)

- "Display Drawing Stamp" — bool
- "Stamp Text" — popup — predefined stamp text
- "Custom Text" — string — used when "Stamp Text" selects the custom entry
- "Stamp Text Style" — string
- "Stamp Text Size" — real
- "Stamp Text Size Unit" — popup
- "Use ALL CAPS" — bool
- "Append Date" — bool
- "Stamp Date" — string
- "Stamp Angle" — real — degrees
- "Stamp Default Position X", "Stamp Default Position Y" — real — world units

**Constructors**

| Constructor | Description |
|---|---|
| `TitleBlockBorderObject(h: Handle)` | Refers to the existing title block border `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D, styleName: str = '') -> TitleBlockBorderObject` *static* | Creates a title block border with its lower left corner area at `position`. `styleName` selects the title block border style: it is looked up in the drawing first and imported from the Vectorworks title block border content when it is not there yet. Leave it empty to use any available style. Returns an invalid object when no title block border style can be found - a title block border without a style has no title block graphics. |
| `EnsureStyle(styleName: str = '') -> str` *static* | Makes sure a title block border style named `styleName` exists in the current drawing, importing it from the Vectorworks content when needed. Returns the name of the style that is now available (which may differ from the requested one when that one does not exist), empty when there is none. |
| `Duplicate() -> TitleBlockBorderObject` | Duplicates the title block border in the drawing and returns the copy. |

*sheet*

| Method | Description |
|---|---|
| `GetSheetSizeName() -> str \| None` | Name of the predefined sheet size, e.g. "ANSI D" or "ISO A1". |
| `SetSheetSizeName(name: str) -> bool` | Sets the sheet size name. Name of the predefined sheet size, e.g. "ANSI D" or "ISO A1". |
| `GetSheetWidth() -> float \| None` | Custom sheet size, world units. Only meaningful when the object uses a custom size. |
| `SetSheetWidth(value: float) -> bool` | Sets the sheet width. Custom sheet size, world units. Only meaningful when the object uses a custom size. |
| `GetSheetHeight() -> float \| None` | Returns the sheet height. |
| `SetSheetHeight(value: float) -> bool` | Sets the sheet height. |
| `GetMarginLeft() -> float \| None` | Sheet margins, world units. |
| `GetMarginRight() -> float \| None` | Returns the margin right. |
| `GetMarginTop() -> float \| None` | Returns the margin top. |
| `GetMarginBottom() -> float \| None` | Returns the margin bottom. |
| `SetMargins(left: float, right: float, top: float, bottom: float) -> bool` | Sets the margins. |

*zone grid*

| Method | Description |
|---|---|
| `GetShowGrids() -> bool \| None` | Whether *Show Grids* is on. |
| `SetShowGrids(value: bool) -> bool` | Turns *Show Grids* on or off. |
| `GetHorizontalZones() -> int \| None` | Returns the horizontal zones. |
| `SetHorizontalZones(count: int) -> bool` | Sets the horizontal zones. |
| `GetVerticalZones() -> int \| None` | Returns the vertical zones. |
| `SetVerticalZones(count: int) -> bool` | Sets the vertical zones. |
| `GetDrawCropMarks() -> bool \| None` | Whether *Draw Crop Marks* is on. |
| `SetDrawCropMarks(value: bool) -> bool` | Turns *Draw Crop Marks* on or off. |

*title block*

| Method | Description |
|---|---|
| `GetUseAsTitleBlock() -> bool \| None` | Whether the object draws the title block, or only the sheet border. |
| `SetUseAsTitleBlock(value: bool) -> bool` | Turns *Use As Title Block* on or off. Whether the object draws the title block, or only the sheet border. |
| `GetIsActiveTitleBlock() -> bool \| None` | Whether this is the title block whose sheet data the document reads (one per sheet). |
| `SetIsActiveTitleBlock(value: bool) -> bool` | Turns *Active Title Block* on or off. Whether this is the title block whose sheet data the document reads (one per sheet). |

*north point*

| Method | Description |
|---|---|
| `GetDisplayNorthArrow() -> bool \| None` | Whether *Display North Arrow* is on. |
| `SetDisplayNorthArrow(value: bool) -> bool` | Turns *Display North Arrow* on or off. |
| `GetNorthAngle() -> float \| None` | Returns the north angle (radians). |
| `SetNorthAngle(radians: float) -> bool` | Sets the north angle. |

*drawing stamp*

| Method | Description |
|---|---|
| `GetDisplayDrawingStamp() -> bool \| None` | Whether *Display Drawing Stamp* is on. |
| `SetDisplayDrawingStamp(value: bool) -> bool` | Turns *Display Drawing Stamp* on or off. |
| `GetDrawingStampText() -> str \| None` | Free text printed by the stamp, used when the stamp text is set to the custom entry. |
| `SetDrawingStampText(text: str) -> bool` | Sets the drawing stamp text. Free text printed by the stamp, used when the stamp text is set to the custom entry. |

*sheet data*

| Method | Description |
|---|---|
| `GetSheetDataFieldNames() -> list[str]` | Returns the sheet data field names. |
| `GetSheetData(fieldName: str) -> str \| None` | Returns the sheet data for `fieldName`. |
| `SetSheetData(fieldName: str, value: str) -> bool` | Sets the sheet data. |
| `GetAllSheetData() -> list[tuple[str, str]]` | Every sheet data field of this title block as (field name, value) pairs. |

*project data*

| Method | Description |
|---|---|
| `GetProjectDataFieldNames() -> list[str]` *static* | Returns the project data field names. |
| `GetProjectData(fieldName: str) -> str \| None` *static* | Returns the project data for `fieldName`. |
| `SetProjectData(fieldName: str, value: str) -> bool` *static* | Sets the project data. |
| `GetAllProjectData() -> list[tuple[str, str]]` *static* | Returns all project data. |

*revisions and issues*

| Method | Description |
|---|---|
| `GetRevisions() -> list[TitleBlockBorderObject.Revision]` | The revision history printed by this title block, oldest first. |
| `GetSheetID() -> str \| None` | Sheet identification as the title block currently prints it. |
| `GetSheetTitle() -> str \| None` | Returns the sheet title. |
| `GetSheetDate() -> str \| None` | Returns the sheet date. |
| `GetLatestIssueDate() -> str \| None` | Date of the most recent issue of this title block, empty when it was never issued. |
| `UpdateData(updateAutomaticData: bool = True) -> bool` *static* | Re-reads the document data into every title block border of the drawing and redraws them. `updateAutomaticData` also refreshes the values Vectorworks maintains itself (file name, page numbers, sheet counts, plot date, ...). |

Inherited: everything from [`AnnotationObject`](#annotationobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### TitleBlockBorderObject.Revision

> **Full name:** `api.TitleBlockBorderObject.Revision` · **Inherits:** `api.Object`

One revision of a title block: number, date, note, publish date and recipients.

**Constructors**

| Constructor | Description |
|---|---|
| `Revision()` | Default value (fields at their defaults). |
| `Revision(fNumber, fDate, fNote, fPublishDate, fRecipients)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fNumber` | `str` | Revision number. |
| `fDate` | `str` | Revision date. |
| `fNote` | `str` | Revision note. |
| `fPublishDate` | `str` | Publish date. |
| `fRecipients` | `str` | Recipients. |

### DimensionObject

> **Full name:** `api.DimensionObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Base class of every dimension object (`ObjectType.Dimension`).

A dimension is a NATIVE Vectorworks object, not a plug-in object: it has no parameter record and no object style. Everything about it - the measured points, what text it prints, whether it draws witness lines - is stored in object variables, which this class exposes as named accessors.

A dimension draws itself from three sources:

1. its own geometry (the measured points and the offset of the dimension line from them),
2. the DIMENSION STANDARD it references (GetStandardName): arrow style and size, witness line gap and overhang, text placement, ... all of which are page lengths and therefore scale-aware,
3. the UNIT SETTINGS: by default the document's primary/secondary units, or a named dimension unit setting when one is assigned (GetUnitSetting).

Changing the standard or the units of a dimension never changes what it measures, only how it looks.

The text a dimension prints is the measured value (GetShowValue) wrapped in optional leader and trailer text; switching the value off and setting leader text turns the dimension into a plain label. The "secondary" accessors are the same settings for the second (dual) unit display.

Dimensions may be ASSOCIATIVE: when `Associate()` succeeds, the dimension keeps measuring the object it was snapped to and updates itself when that object changes. Associativity is a property of the document ("Associate Dimensions" preference) as much as of the object.

All angles in this API are radians; all lengths are world units.

**Constructors**

| Constructor | Description |
|---|---|
| `DimensionObject(h: Handle)` | Refers to the existing dimension `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents (any dimension object). |
| `KindOf(h: Handle) -> DimensionKind` *static* | Kind of the dimension, or Unknown when `h` is not a dimension. |
| `Duplicate() -> DimensionObject` | Duplicates the dimension in the drawing and returns the copy. |

*identity*

| Method | Description |
|---|---|
| `GetKind() -> DimensionKind \| None` | Returns the kind. |
| `GetKindName() -> str \| None` | Returns the kind name. |
| `GetKindName(kind: DimensionKind) -> str` *static* | Returns the kind name for `kind`. |

*measured geometry*

| Method | Description |
|---|---|
| `GetStartPoint() -> Math.Point2D \| None` | The two points the dimension measures between. For angular dimensions these are the two leg points and the vertex is kept separately (see AngularDimensionObject); for radial and arc length dimensions they are points on the circle / arc. |
| `SetStartPoint(pt: Math.Point2D) -> bool` | Sets the start point. The two points the dimension measures between. For angular dimensions these are the two leg points and the vertex is kept separately (see AngularDimensionObject); for radial and arc length dimensions they are points on the circle / arc. |
| `GetEndPoint() -> Math.Point2D \| None` | Returns the end point. |
| `SetEndPoint(pt: Math.Point2D) -> bool` | Sets the end point. |
| `SetPoints(start: Math.Point2D, end: Math.Point2D) -> bool` | Sets the points. |
| `GetOffset() -> float \| None` | Distance between the measured points and the dimension line itself. Positive offsets put the dimension line on the left of the start -> end direction, negative ones on the right. |
| `SetOffset(offset: float) -> bool` | Sets the offset. Distance between the measured points and the dimension line itself. Positive offsets put the dimension line on the left of the start -> end direction, negative ones on the right. |
| `GetMeasuredLength() -> float \| None` | Straight distance between the two measured points, in world units. This is the length the dimension prints for an unconstrained linear dimension; constrained ones print the projection of this distance onto their fixed direction. |

*witness (extension) lines*

| Method | Description |
|---|---|
| `GetStartWitness() -> bool \| None` | Whether *Start Witness* is on. |
| `SetStartWitness(show: bool) -> bool` | Turns *Start Witness* on or off. |
| `GetEndWitness() -> bool \| None` | Whether *End Witness* is on. |
| `SetEndWitness(show: bool) -> bool` | Turns *End Witness* on or off. |
| `GetWitnessOverride() -> int \| None` | 0 = use the dimension standard, 1 = one custom length for both witness lines, 2 = a custom length per witness line, 3 = one custom offset for both, 4 = a custom offset per witness line. |
| `SetWitnessOverride(mode: int) -> bool` | Sets the witness override. 0 = use the dimension standard, 1 = one custom length for both witness lines, 2 = a custom length per witness line, 3 = one custom offset for both, 4 = a custom offset per witness line. |
| `GetStartWitnessLength() -> float \| None` | Returns the start witness length (world units, custom override). |
| `SetStartWitnessLength(length: float) -> bool` | Sets the start witness length. |
| `GetEndWitnessLength() -> float \| None` | Returns the end witness length. |
| `SetEndWitnessLength(length: float) -> bool` | Sets the end witness length. |
| `GetStartWitnessOffset() -> float \| None` | Returns the start witness offset (world units, custom override). |
| `SetStartWitnessOffset(offset: float) -> bool` | Sets the start witness offset. |
| `GetEndWitnessOffset() -> float \| None` | Returns the end witness offset. |
| `SetEndWitnessOffset(offset: float) -> bool` | Sets the end witness offset. |

*arrows and leader*

| Method | Description |
|---|---|
| `GetArrowsInside() -> bool \| None` | `True` when the arrowheads point inwards (between the witness lines) rather than outwards. |
| `SetArrowsInside(inside: bool) -> bool` | Turns *Arrows Inside* on or off. `True` when the arrowheads point inwards (between the witness lines) rather than outwards. |
| `GetLeaderLine() -> bool \| None` | A leader line connects the text to the dimension line when the text does not fit between the witness lines. Mostly used by radial and small linear dimensions. |
| `SetLeaderLine(use: bool) -> bool` | Turns *Leader Line* on or off. A leader line connects the text to the dimension line when the text does not fit between the witness lines. Mostly used by radial and small linear dimensions. |

*printed text*

| Method | Description |
|---|---|
| `GetShowValue() -> bool \| None` | Whether the measured value is printed at all. Off + leader text = a plain annotation label. |
| `SetShowValue(show: bool) -> bool` | Turns *Show Value* on or off. Whether the measured value is printed at all. Off + leader text = a plain annotation label. |
| `GetLeaderText() -> str \| None` | Returns the leader text (printed before the value). |
| `SetLeaderText(text: str) -> bool` | Sets the leader text. |
| `GetTrailerText() -> str \| None` | Returns the trailer text (printed after the value). |
| `SetTrailerText(text: str) -> bool` | Sets the trailer text. |
| `GetBoxText() -> bool \| None` | Whether *Box Text* is on (draw a box around the text). |
| `SetBoxText(box: bool) -> bool` | Turns *Box Text* on or off. |
| `GetPrecision() -> int \| None` | Digits after the decimal point for decimal units; a power of two (0 = 1/1 ... 6 = 1/64) for fractional units; for angular dimensions 1 = whole degrees, 2 = deg/min, 3 = deg/min/sec. |
| `SetPrecision(precision: int) -> bool` | Sets the precision. Digits after the decimal point for decimal units; a power of two (0 = 1/1 ... 6 = 1/64) for fractional units; for angular dimensions 1 = whole degrees, 2 = deg/min, 3 = deg/min/sec. |
| `GetShowSecondaryValue() -> bool \| None` | Secondary (dual) unit display - the same four settings for the second measurement. |
| `SetShowSecondaryValue(show: bool) -> bool` | Turns *Show Secondary Value* on or off. Secondary (dual) unit display - the same four settings for the second measurement. |
| `GetSecondaryLeaderText() -> str \| None` | Returns the secondary leader text. |
| `SetSecondaryLeaderText(text: str) -> bool` | Sets the secondary leader text. |
| `GetSecondaryTrailerText() -> str \| None` | Returns the secondary trailer text. |
| `SetSecondaryTrailerText(text: str) -> bool` | Sets the secondary trailer text. |
| `GetSecondaryBoxText() -> bool \| None` | Whether *Secondary Box Text* is on. |
| `SetSecondaryBoxText(box: bool) -> bool` | Turns *Secondary Box Text* on or off. |
| `GetSecondaryPrecision() -> int \| None` | Returns the secondary precision. |
| `SetSecondaryPrecision(precision: int) -> bool` | Sets the secondary precision. |
| `GetNoteText() -> str \| None` | Note text carried by the dimension, shown by some standards below the measurement. |
| `SetNoteText(text: str) -> bool` | Sets the note text. Note text carried by the dimension, shown by some standards below the measurement. |

*text placement*

| Method | Description |
|---|---|
| `GetTextPositionAutomatic() -> bool \| None` | `True` when Vectorworks positions the text itself; `False` when it was dragged to a fixed spot. |
| `SetTextPositionAutomatic(automatic: bool) -> bool` | Turns *Text Position Automatic* on or off. `True` when Vectorworks positions the text itself; `False` when it was dragged to a fixed spot. |
| `GetTextInside() -> bool \| None` | Whether *Text Inside* is on (text between the witness lines). |
| `SetTextInside(inside: bool) -> bool` | Turns *Text Inside* on or off. |
| `GetTextFlipped() -> bool \| None` | Whether *Text Flipped* is on. |
| `SetTextFlipped(flipped: bool) -> bool` | Turns *Text Flipped* on or off. |
| `GetTextRotation() -> int \| None` | 0 = aligned with the dimension line, 1 = horizontal only, 2 = horizontal / vertical. |
| `SetTextRotation(rotation: int) -> bool` | Sets the text rotation. 0 = aligned with the dimension line, 1 = horizontal only, 2 = horizontal / vertical. |
| `GetTextOffsetAlongLine() -> float \| None` | Distance of the text from the start point (negative) or the end point (positive), world units. |
| `SetTextOffsetAlongLine(offset: float) -> bool` | Sets the text offset along line. Distance of the text from the start point (negative) or the end point (positive), world units. |
| `GetTextOffsetAboveLine() -> float \| None` | Distance of the text above the dimension line, world units. |
| `SetTextOffsetAboveLine(offset: float) -> bool` | Sets the text offset above line. Distance of the text above the dimension line, world units. |

*text font*

| Method | Description |
|---|---|
| `GetFontSize() -> float \| None` | Returns the font size (points). |
| `SetFontSize(points: float) -> bool` | Sets the font size. |
| `GetFontStyle() -> int \| None` | Sum of 1 = bold, 2 = italic, 4 = underline. |
| `SetFontStyle(style: int) -> bool` | Sets the font style. Sum of 1 = bold, 2 = italic, 4 = underline. |
| `GetTextStyleName() -> str \| None` | Name of the text style resource applied to the dimension text; empty when the dimension uses its own font settings. |
| `SetTextStyleName(name: str) -> bool` | Sets the text style name. Name of the text style resource applied to the dimension text; empty when the dimension uses its own font settings. |

*tolerance*

| Method | Description |
|---|---|
| `GetToleranceType() -> DimensionTolerance \| None` | Returns the tolerance type. |
| `SetToleranceType(type: DimensionTolerance) -> bool` | Sets the tolerance type. |
| `GetTolerancePlus() -> float \| None` | Returns the tolerance plus (world units). |
| `SetTolerancePlus(value: float) -> bool` | Sets the tolerance plus. |
| `GetToleranceMinus() -> float \| None` | Returns the tolerance minus (world units). |
| `SetToleranceMinus(value: float) -> bool` | Sets the tolerance minus. |

*standard and units*

| Method | Description |
|---|---|
| `GetStandardName() -> str \| None` | Name of the dimension standard the object references ("ASME", "ISO", a custom standard, ...). The standard supplies every page-length detail of the drawn dimension. |
| `SetStandardName(name: str) -> bool` | Sets the standard name. Name of the dimension standard the object references ("ASME", "ISO", a custom standard, ...). The standard supplies every page-length detail of the drawn dimension. |
| `GetStandardIndex() -> int \| None` | Index of the standard: > 0 a built-in standard, < 0 a custom (document) standard. |
| `SetStandardIndex(index: int) -> bool` | Sets the standard index. Index of the standard: > 0 a built-in standard, < 0 a custom (document) standard. |
| `GetUnitSetting() -> int \| None` | 0 = use the document units; otherwise the index of a named dimension unit setting resource. |
| `SetUnitSetting(index: int) -> bool` | Sets the unit setting. 0 = use the document units; otherwise the index of a named dimension unit setting resource. |

*associativity*

| Method | Description |
|---|---|
| `Associate(selectedObjectsOnly: bool = False) -> bool` | Binds the dimension to the object(s) it measures so it follows them. `selectedObjectsOnly` limits the search for something to bind to to the current selection. Not every dimension can be bound; returns `False` when the binding was refused. |
| `GetDimensionsOf(hObject: Handle) -> list[Handle]` *static* | Objects a dimension may be bound to: the dimensions currently measuring `hObject`. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### LinearDimensionObject

> **Full name:** `api.LinearDimensionObject` · **Inherits:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Linear dimension: measures the distance between two points.

There are two flavours, and the difference is what happens when the two measured points are not aligned with the dimension line:

CONSTRAINED (fixed angle) - CreateConstrained / CreateHorizontal / CreateVertical The dimension line keeps the direction it was created with. The printed value is the PROJECTION of the distance between the two points onto that direction, so a horizontal dimension across a sloped wall reports the horizontal run, not the length of the wall. This is what the Constrained Linear Dimension tool draws and what plans are normally dimensioned with.

UNCONSTRAINED (sloped) - CreateUnconstrained The dimension line is parallel to the line between the two points, so the printed value is always their true distance. This is what the Unconstrained Linear Dimension tool draws.

Both take an OFFSET: how far the dimension line sits from the measured points, in world units. A positive offset places it to the left of the start -> end direction, a negative one to the right.

A third flavour, ORDINATE, measures every point against a common datum and prints only the offset from it; CreateOrdinate produces one.

Linear dimensions can be associative (see `DimensionObject.Associate`): bound to the object they were snapped to, they re-measure themselves whenever that object changes.

**Constructors**

| Constructor | Description |
|---|---|
| `LinearDimensionObject(h: Handle)` | Refers to the existing linear dimension `h`; check `IsValid()` before use. |

**Methods**

*Any linear dimension*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | Constrained, unconstrained or ordinate. |
| `CreateConstrained(start: Math.Point2D, end: Math.Point2D, direction: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *static* | Constrained dimension along an explicit direction. `direction` is the direction of the dimension line; a zero vector falls back to the direction from `start` to `end`. Fails when the two points coincide. |
| `CreateConstrained(start: Math.Point2D, end: Math.Point2D, angle: float, offset: float = 0.0) -> LinearDimensionObject` *static* | Constrained dimension whose dimension line is rotated by `angle` radians from the X axis. |
| `CreateHorizontal(start: Math.Point2D, end: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *static* | Constrained dimension measuring the horizontal / vertical distance between the two points. |
| `CreateVertical(start: Math.Point2D, end: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *static* | Creates a constrained dimension measuring the vertical distance between `start` and `end`, placed at `offset`. |
| `CreateUnconstrained(start: Math.Point2D, end: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *static* | Unconstrained ("sloped") dimension: the dimension line follows start -> end and the value is the true distance between the two points. Fails when the two points coincide. |

*Ordinate dimension*

| Method | Description |
|---|---|
| `CreateOrdinate(datum: Math.Point2D, point: Math.Point2D, direction: Math.Point2D, offset: float = 0.0) -> LinearDimensionObject` *static* | `start` is the datum, `end` the measured point. |
| `Duplicate() -> LinearDimensionObject` | Duplicates the linear dimension in the drawing and returns the copy. |
| `IsConstrained() -> bool \| None` | `True` for a constrained (fixed angle) dimension, `False` for an unconstrained one. |
| `GetDirectionAngle() -> float \| None` | Direction of the dimension line as an angle in radians from the X axis. For an unconstrained dimension this is the direction from the start to the end point. |
| `SetDirectionAngle(angle: float) -> bool` | Only meaningful for a constrained dimension; rotates the dimension line without moving the measured points, which changes the value the dimension prints. |
| `GetValue() -> float \| None` | Value the dimension prints: the distance between the measured points, projected onto the dimension line direction for a constrained dimension. |

Inherited: everything from [`DimensionObject`](#dimensionobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### AngularDimensionObject

> **Full name:** `api.AngularDimensionObject` · **Inherits:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Angular dimension: measures the angle between two legs meeting at a vertex.

The dimension is defined by three points - the VERTEX where the two legs meet and one point on each leg - plus an offset that decides the radius of the arc the dimension draws between the legs. The printed value is the angle swept counter-clockwise from the first leg to the second, so swapping the two leg points gives the explementary angle (360 degrees minus the first one).

An angular dimension can be a REFERENCE ANGLE: it then draws only one witness line and measures the angle of a single leg against the reference direction instead of the angle between two legs. Vectorworks creates reference angle dimensions by default, so `Create()` switches that off; `CreateReferenceAngle()` keeps it on.

The angle accessors of this class work in radians like the rest of the API, while the angular PRECISION follows the dimension conventions: 1 = whole degrees, 2 = degrees + minutes, 3 = degrees + minutes + seconds, 5..12 = that many decimal places.

**Constructors**

| Constructor | Description |
|---|---|
| `AngularDimensionObject(h: Handle)` | Refers to the existing angular dimension `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(vertex: Math.Point2D, firstLegPoint: Math.Point2D, secondLegPoint: Math.Point2D, offset: float = 0.0) -> AngularDimensionObject` *static* | Angle from `firstLegPoint` to `secondLegPoint` around `vertex`, drawn at `offset` world units from the vertex. Fails when any two of the three points coincide. |
| `Create(vertex: Math.Point2D, startAngle: float, endAngle: float, legLength: float, offset: float = 0.0) -> AngularDimensionObject` *static* | Same, but built from the vertex, the two leg directions (radians) and a leg length. |

*Reference angle variant*

| Method | Description |
|---|---|
| `CreateReferenceAngle(vertex: Math.Point2D, firstLegPoint: Math.Point2D, secondLegPoint: Math.Point2D, offset: float = 0.0) -> AngularDimensionObject` *static* | A single witness line measuring one leg against the reference direction. |
| `Duplicate() -> AngularDimensionObject` | Duplicates the angular dimension in the drawing and returns the copy. |
| `GetVertex() -> Math.Point2D \| None` | Vertex the two legs meet at. Vectorworks keeps it in the dimension box rather than in the start / end points, which hold the two leg points. |
| `SetVertex(vertex: Math.Point2D) -> bool` | Sets the vertex. Vertex the two legs meet at. Vectorworks keeps it in the dimension box rather than in the start / end points, which hold the two leg points. |
| `GetStartAngle() -> float \| None` | Directions of the two legs, radians from the X axis. |
| `GetEndAngle() -> float \| None` | Returns the end angle. |
| `GetValue() -> float \| None` | Measured angle in radians, counter-clockwise from the first leg to the second, in [0, 2*pi). |
| `GetReferenceAngle() -> bool \| None` | Whether the dimension measures against the reference direction with a single witness line. |
| `SetReferenceAngle(reference: bool) -> bool` | Turns *Reference Angle* on or off. Whether the dimension measures against the reference direction with a single witness line. |

Inherited: everything from [`DimensionObject`](#dimensionobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### ArcLengthDimensionObject

> **Full name:** `api.ArcLengthDimensionObject` · **Inherits:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Arc length dimension: measures the length ALONG an arc rather than the straight distance between its endpoints, which is what a linear dimension would report.

It is defined by the two endpoints of the measured span and the CENTRE of the arc they lie on; the centre is what tells the dimension how the two points are connected. Because two arcs run between any two points on a circle, `clockwise` selects which of them is measured.

Three switches decide how it is drawn, and Vectorworks fixes all three at creation time (they are read-only afterwards - recreate the dimension to change them):

- clockwise — which of the two arcs between the endpoints is measured
- witnessPerpChord — witness lines perpendicular to the chord instead of radial from the centre
- arcIndicator — draw the arc symbol that marks the value as an arc length

**Constructors**

| Constructor | Description |
|---|---|
| `ArcLengthDimensionObject(h: Handle)` | Refers to the existing arc length dimension `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(start: Math.Point2D, end: Math.Point2D, center: Math.Point2D, offset: float = 0.0, clockwise: bool = False, witnessPerpendicularToChord: bool = False, arcIndicator: bool = True) -> ArcLengthDimensionObject` *static* | Measures from `start` to `end` along the arc around `center`. Fails when the points coincide with each other or with the centre. |
| `Create(center: Math.Point2D, radius: float, startAngle: float, sweepAngle: float, offset: float = 0.0, witnessPerpendicularToChord: bool = False, arcIndicator: bool = True) -> ArcLengthDimensionObject` *static* | Same, expressed as an arc: centre, radius and the start / sweep angles in radians. A negative sweep measures the clockwise arc. |
| `Duplicate() -> ArcLengthDimensionObject` | Duplicates the arc length dimension in the drawing and returns the copy. |
| `GetCenter() -> Math.Point2D \| None` | Centre of the measured arc. Vectorworks keeps it in the dimension box; the start / end points hold the two endpoints of the measured span. |
| `GetRadius() -> float \| None` | Returns the radius. |
| `GetStartAngle() -> float \| None` | Start angle and signed sweep of the measured arc, radians. |
| `GetSweepAngle() -> float \| None` | Returns the sweep angle. |
| `GetValue() -> float \| None` | Value the dimension prints: the length along the arc, world units. |
| `IsClockwise() -> bool \| None` | Drawing options fixed at creation (read-only on the object). |
| `IsWitnessPerpendicularToChord() -> bool \| None` | True when the witness lines are perpendicular to the chord. |
| `HasArcIndicator() -> bool \| None` | True when the dimension shows the arc indicator. |

Inherited: everything from [`DimensionObject`](#dimensionobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### RadialDimensionObject

> **Full name:** `api.RadialDimensionObject` · **Inherits:** [`DimensionObject`](#dimensionobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Radial and diametrical dimension: measures the radius or the diameter of a circle or arc.

Both kinds are built from the CENTRE of the circle and a POINT ON IT, which fixes the direction the dimension is drawn in. The difference is only what is measured and printed:

- RADIAL — draws from the centre (or from outside, with a leader) to the circle and prints the radius, conventionally prefixed with "R". DIAMETRICAL draws right across the circle and prints the diameter, conventionally prefixed with the diameter sign.

Use SetLeaderText to change that prefix; the prefix is not implied by the dimension kind.

The offset moves the text (and the leader) away from the circle; on a radial dimension a positive offset pushes the measurement outside the circle.

COMPACT mode (Get/SetCompact) is the short radial notation: only a short stub with the arrowhead is drawn at the circle instead of a line reaching the centre - used when the circle is too small to hold the dimension.

**Constructors**

| Constructor | Description |
|---|---|
| `RadialDimensionObject(h: Handle)` | Refers to the existing radial dimension `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | Any radial or diametrical dimension. |
| `CreateRadial(center: Math.Point2D, radius: float, angle: float, offset: float = 0.0) -> RadialDimensionObject` *static* | Radius dimension of the circle `centre`/`radius`, drawn towards `angle` radians. |
| `CreateRadial(center: Math.Point2D, pointOnCircle: Math.Point2D, offset: float = 0.0) -> RadialDimensionObject` *static* | Radius dimension of the circle through `pointOnCircle` around `center`. |
| `CreateDiametrical(center: Math.Point2D, radius: float, angle: float, offset: float = 0.0) -> RadialDimensionObject` *static* | Diameter dimension, same arguments. |
| `CreateDiametrical(center: Math.Point2D, pointOnCircle: Math.Point2D, offset: float = 0.0) -> RadialDimensionObject` *static* | Diameter dimension, same arguments. |
| `Duplicate() -> RadialDimensionObject` | Duplicates the radial dimension in the drawing and returns the copy. |
| `IsDiametrical() -> bool \| None` | `True` when the dimension prints the diameter, `False` when it prints the radius. |
| `GetCenter() -> Math.Point2D \| None` | Circle the dimension measures. The centre is the start point, the point on the circle the end point. |
| `SetCenter(center: Math.Point2D) -> bool` | Sets the center. Circle the dimension measures. The centre is the start point, the point on the circle the end point. |
| `GetRadius() -> float \| None` | Returns the radius. |
| `SetRadius(radius: float) -> bool` | Sets the radius (keeps the centre and the direction). |
| `GetDiameter() -> float \| None` | Returns the diameter. |
| `SetDiameter(diameter: float) -> bool` | Sets the diameter. |
| `GetAngle() -> float \| None` | Direction the dimension is drawn in, radians from the X axis. |
| `SetAngle(angle: float) -> bool` | Sets the angle. Direction the dimension is drawn in, radians from the X axis. keeps the centre and the radius. |
| `GetValue() -> float \| None` | Value the dimension prints: the diameter for a diametrical dimension, the radius otherwise. |
| `GetCompact() -> bool \| None` | Short radial notation - a stub with the arrowhead instead of a line to the centre. |
| `SetCompact(compact: bool) -> bool` | Turns *Compact* on or off. Short radial notation - a stub with the arrowhead instead of a line to the centre. |

Inherited: everything from [`DimensionObject`](#dimensionobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### CenterMarkObject

> **Full name:** `api.CenterMarkObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Center mark: the cross that marks the centre of a circle or an arc.

Unlike every other object in this group a center mark is NOT a dimension object. Vectorworks builds it as a plain GROUP of line segments, exactly like the Center Mark tool does:

- a horizontal and a vertical segment forming the small cross at the centre, each one spoke long;
- optionally four extension segments reaching out to (and a little beyond) the circle, separated from the cross by a gap. They are only added when the circle is large enough to hold both the cross and the gaps, which is the same rule the tool applies.

Because it is ordinary geometry it carries no measurement and nothing to regenerate - moving or scaling it just moves or scales the lines.

The three page lengths that shape it (spoke length, gap, extension overshoot) come from the active DIMENSION STANDARD, so a center mark drawn on a 1:50 layer is the same size on paper as one drawn on a 1:100 layer. `Create()` reads them from the standard; `CreateWithSizes()` takes explicit world lengths instead for full control.

Like the tool, the group is placed in the dimension class when the "create dimensions in the dimension class" document preference is on, otherwise in the active class.

**Constructors**

| Constructor | Description |
|---|---|
| `CenterMarkObject(h: Handle)` | Refers to the existing center mark `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | Native center marks are unmarked groups: `Is()` conservatively returns `False`. Keep the object returned by `Create()`, or construct one from the handle of a known center-mark group. |
| `Create(center: Math.Point2D, radius: float = 0.0) -> CenterMarkObject` *static* | Center mark for the circle `center`/`radius`, sized from the active dimension standard. A zero or negative radius draws the bare cross without the extension segments. |
| `CreateFor(hObject: Handle) -> CenterMarkObject` *static* | Center mark for an existing circle, arc, oval or any other object - the mark is placed at the centre of its bounding box and sized to it. |
| `CreateWithSizes(center: Math.Point2D, radius: float, spokeLength: float, gap: float, extension: float) -> CenterMarkObject` *static* | Center mark with explicit world lengths: `spokeLength` is the length of one spoke of the cross, `gap` the space between the cross and the extension segments and `extension` how far the extension segments reach beyond the circle. Extensions are omitted when the circle is too small. |
| `Duplicate() -> CenterMarkObject` | Duplicates the center mark in the drawing and returns the copy. |
| `GetCenter() -> Math.Point2D \| None` | Centre of the cross. |
| `GetSegmentCount() -> int \| None` | Number of line segments the mark is made of: 2 for a bare cross, up to 6 with extensions. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### WorksheetObject

> **Full name:** `api.WorksheetObject` · **Inherits:** [`TypedResource`](Resources.md#typedresource) → [`Resource`](Resources.md#resource) → `api.Object`

Non-owning worksheet RESOURCE, not a placed worksheet image or an annotation plug-in object. All row, column and database subrow indices are native worksheet 1-based (column 1 = A), unlike the 0-based geometry APIs. Ranges are inclusive. Strings are UTF-8. Vectorworks uses signed 16-bit indices/sizes; Python rejects values outside that representation.

**Constructors**

| Constructor | Description |
|---|---|
| `WorksheetObject(h: Handle)` | Refers to the existing worksheet `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `FromName(name: str) -> WorksheetObject` *static* | The worksheet resource named `name`; an invalid object when there is none. |

*Creates only*

| Method | Description |
|---|---|
| `Create(name: str, rows: int = 20, columns: int = 10) -> WorksheetObject` *static* | An occupied name (even another worksheet) fails; use FromName for lookup. |
| `Duplicate() -> WorksheetObject` | Duplicates the worksheet in the drawing and returns the copy. |
| `GetRowCount() -> int \| None` | Number of row items. |
| `GetColumnCount() -> int \| None` | Number of column items. |
| `IsValidCell(row: int, column: int) -> bool` | True when the cell `row` / `column` exists in the worksheet. |
| `IsValidRange(range: WorksheetObject.Range) -> bool` | True when every cell of `range` exists in the worksheet. |
| `InsertRows(beforeRow: int, count: int = 1) -> bool` | Inserts `count` rows before the row `beforeRow`. |
| `InsertColumns(beforeColumn: int, count: int = 1) -> bool` | Inserts `count` columns before the column `beforeColumn`. |
| `DeleteRows(startRow: int, count: int = 1) -> bool` | Deletes `count` rows starting at the row `startRow`. |
| `DeleteColumns(startColumn: int, count: int = 1) -> bool` | Deletes `count` columns starting at the column `startColumn`. |
| `GetCellFormula(row: int, column: int) -> str \| None` | Definition string, including literals. Passed to Vectorworks unchanged; Vectorworks may normalize formulas. |
| `SetCellFormula(row: int, column: int, formula: str) -> bool` | Sets the cell formula. Definition string, including literals. Passed to Vectorworks unchanged; Vectorworks may normalize formulas. |
| `SetRangeFormula(range: WorksheetObject.Range, formula: str) -> bool` | Sets the range formula. |
| `GetCellText(row: int, column: int) -> str \| None` | Returns the cell text for `row`, `column`. |
| `GetCellValue(row: int, column: int) -> float \| None` | Empty for nonnumeric/error cells, not a misleading zero. Values reflect last recalculation. |
| `ClearCells(range: WorksheetObject.Range) -> bool` | Clears the contents of the cells in `range`. |
| `IsDatabaseRow(row: int) -> bool \| None` | True when `row` is a database row. |
| `GetDatabaseCriteria(row: int) -> str \| None` | Returns the database criteria for `row`. |
| `SetDatabaseCriteria(row: int, criteria: str) -> bool` | Opaque native definition, e.g. "=DATABASE(ALL)". Empty converts to a spreadsheet row. No criteria parsing here. `False` if Vectorworks cannot apply it (e.g. merged row). |
| `GetSubrowCount(row: int) -> int \| None` | Number of subrow items for `row`. |
| `GetSubrowCellText(row: int, column: int, subrow: int) -> str \| None` | Returns the subrow cell text for `row`, `column`, `subrow`. |
| `GetSubrowCellValue(row: int, column: int, subrow: int) -> float \| None` | Returns the subrow cell value for `row`, `column`, `subrow`. |
| `GetColumnWidth(column: int) -> int \| None` | Width/height are native worksheet pixels, NOT model/world units. |
| `SetColumnWidth(firstColumn: int, lastColumn: int, width: int) -> bool` | Sets the column width. Width/height are native worksheet pixels, NOT model/world units. |
| `GetRowHeight(row: int) -> int \| None` | Returns the row height for `row`. |
| `GetRowHeightLocked(row: int) -> bool \| None` | Whether *Row Height Locked* is on for `row`. |
| `SetRowHeight(firstRow: int, lastRow: int, height: int, lockHeight: bool = True, includeSubrows: bool = False) -> bool` | Sets the row height. |
| `AutoFitRowHeights(firstRow: int, lastRow: int) -> bool` | Fits the heights of the rows `firstRow` .. `lastRow` to their contents. |
| `GetSubrowHeight(row: int, subrow: int) -> int \| None` | Returns the subrow height for `row`, `subrow`. |
| `GetCellNumberFormat(row: int, column: int) -> WorksheetObject.NumberFormat \| None` | Returns the cell number format for `row`, `column`. |
| `SetNumberFormat(range: WorksheetObject.Range, format: WorksheetObject.NumberFormat) -> bool` | Sets the number format. |
| `GetCellTextFormat(row: int, column: int) -> WorksheetObject.TextFormat \| None` | Returns the cell text format for `row`, `column`. |
| `SetTextFormat(range: WorksheetObject.Range, format: WorksheetObject.TextFormat) -> bool` | Sets the text format. |
| `GetCellFill(row: int, column: int) -> WorksheetObject.Fill \| None` | Returns the cell fill for `row`, `column`. |
| `SetFill(range: WorksheetObject.Range, fill: WorksheetObject.Fill) -> bool` | Sets the fill. |
| `GetCellBorders(row: int, column: int) -> WorksheetObject.Borders \| None` | Returns the cell borders for `row`, `column`. |
| `SetBorders(range: WorksheetObject.Range, borders: WorksheetObject.Borders) -> bool` | Sets the borders. |
| `GetMergedCellRange(row: int, column: int) -> WorksheetObject.Range \| None` | Returns the merged cell range for `row`, `column`. |
| `MergeCells(range: WorksheetObject.Range) -> bool` | Merges the cells of `range` into one cell. |
| `UnmergeCells(range: WorksheetObject.Range) -> bool` | Splits the merged cells of `range`. |
| `Recalculate() -> bool` | Recalculates the worksheet. |
| `GetAutoRecalculate() -> bool \| None` | Whether *Auto Recalculate* is on. |
| `SetAutoRecalculate(enabled: bool) -> bool` | Turns *Auto Recalculate* on or off. |
| `CreateImage(topLeftCorner: Point2D) -> Handle` | Image handles are drawing objects: do not use them as WorksheetObject. It repositions the first existing image, or creates one on the active layer if absent. This is not an "always create another image" factory. |
| `GetImage() -> Handle` | Returns the image. First associated image, null if absent. |
| `FromImage(image: Handle) -> WorksheetObject` *static* | The worksheet resource shown by the worksheet image `image` (an object placed in the drawing). |

Inherited: everything from [`TypedResource`](Resources.md#typedresource), [`Resource`](Resources.md#resource).

#### WorksheetObject.Range

> **Full name:** `api.WorksheetObject.Range` · **Inherits:** `api.Object`

Inclusive 1-based worksheet range.

**Constructors**

| Constructor | Description |
|---|---|
| `Range()` | Default value (fields at their defaults). |
| `Range(firstRow, firstColumn, lastRow, lastColumn)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `firstRow` | `int` | First row (1-based). |
| `firstColumn` | `int` | First column (1-based). |
| `lastRow` | `int` | Last row (inclusive). |
| `lastColumn` | `int` | Last column (inclusive). |

#### WorksheetObject.NumberFormat

> **Full name:** `api.WorksheetObject.NumberFormat` · **Inherits:** `api.Object`

Native worksheet number format, including format-dependent accuracy and UTF-8 leader/trailer.

**Constructors**

| Constructor | Description |
|---|---|
| `NumberFormat()` | Default value (fields at their defaults). |
| `NumberFormat(style, accuracy, leader, trailer)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `style` | `int` | 0 general, 1 decimal, 2 decimal with commas, 3 scientific, 4 fractional, 5 dimension, 6 angle, 7 date, 8 conditional, 9 general fraction, 10 dimension with divider, 11 area, 12 volume, 13 text, 14 percentage. |
| `accuracy` | `int` | Native format-dependent accuracy, not always decimal places. |
| `leader` | `str` | 0 general, 1 decimal, 2 decimal with commas, 3 scientific, 4 fractional, 5 dimension, 6 angle, 7 date, 8 conditional, 9 general fraction, 10 dimension with divider, 11 area, 12 volume, 13 text, 14 percentage. |
| `trailer` | `str` | 0 general, 1 decimal, 2 decimal with commas, 3 scientific, 4 fractional, 5 dimension, 6 angle, 7 date, 8 conditional, 9 general fraction, 10 dimension with divider, 11 area, 12 volume, 13 text, 14 percentage. |

#### WorksheetObject.TextFormat

> **Full name:** `api.WorksheetObject.TextFormat` · **Inherits:** `api.Object`

Worksheet text: point size, font/style, alignments, degree angle, ColorRef index and wrap.

**Constructors**

| Constructor | Description |
|---|---|
| `TextFormat()` | Default value (fields at their defaults). |
| `TextFormat(fontIndex, size, style, alignment, verticalAlignment, angle, color, wrap)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fontIndex` | `int` | Document font table index. |
| `size` | `int` | Points. |
| `style` | `int` | Native text style bits (bold=1, italic=2, underline=4, ...). |
| `alignment` | `int` | 0 general, 1 left, 2 center, 3 right. |
| `verticalAlignment` | `int` | 0 general, 1 top, 3 center, 5 bottom. |
| `angle` | `int` | Native worksheet text angle in DEGREES, not radians. |
| `color` | `int` | Document ColorRef index, not RGB. |
| `wrap` | `bool` | Whether the text wraps in the cell. |

#### WorksheetObject.Fill

> **Full name:** `api.WorksheetObject.Fill` · **Inherits:** `api.Object`

Native fill style, document ColorRef indices and pattern.

**Constructors**

| Constructor | Description |
|---|---|
| `Fill()` | Default value (fields at their defaults). |
| `Fill(style, background, foreground, pattern)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `style` | `int` | 0 none, 1 solid, 2 pattern. |
| `background` | `int` | Background color (color index). |
| `foreground` | `int` | Document ColorRef indices. |
| `pattern` | `int` | Native fill pattern, used only for style 2. |

#### WorksheetObject.Borders

> **Full name:** `api.WorksheetObject.Borders` · **Inherits:** `api.Object`

Cell border flags plus outline and inside range application flags.

**Constructors**

| Constructor | Description |
|---|---|
| `Borders()` | Default value (fields at their defaults). |
| `Borders(top, left, bottom, right, outline, insideHorizontal, insideVertical)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `top` | `bool` | Top border. |
| `left` | `bool` | Left border. |
| `bottom` | `bool` | Bottom border. |
| `right` | `bool` | Right border. |
| `outline` | `bool` | Range application options; a single-cell getter leaves these `False`. |
| `insideHorizontal` | `bool` | Range application options; a single-cell getter leaves these `False`. |
| `insideVertical` | `bool` | Range application options; a single-cell getter leaves these `False`. |

## Enumerations

### DimensionKind

> **Full name:** `api.DimensionKind` · **Kind:** `IntEnum`

Kind of dimension an object is. Stored on the object; it decides how the dimension measures and draws and it cannot be changed after creation (create the right kind instead).

| Member | Value | Description |
|---|---|---|
| `Unknown` | `-1` |  |
| `ConstrainedLinear` | `0` | Linear, fixed direction: the dimension line keeps the direction given at creation (horizontal, vertical or any rotated angle) and measures the projection of the two points on it. fix_ang. |
| `UnconstrainedLinear` | `1` | Linear, free direction: the dimension line follows the line between the two measured points, so the dimension always reports the true distance between them. sloped. |
| `Ordinate` | `2` | Linear, measured from a common datum; the dimension prints only the offset from that datum. |
| `Radial` | `3` | Radius of a circle / arc. |
| `Diametrical` | `4` | Diameter of a circle / arc. |
| `Angular` | `5` | Angle between two legs around a vertex. |
| `ArcLength` | `6` | Length along an arc. |

### DimensionTolerance

> **Full name:** `api.DimensionTolerance` · **Kind:** `IntEnum`

How much a dimension deviates from its nominal value, printed next to the measurement.

| Member | Value | Description |
|---|---|---|
| `None_` | `0` |  |
| `Single` | `1` | One +/- value. |
| `Double` | `2` | Separate plus and minus values. |
| `Limit` | `3` | Upper and lower limit instead of the nominal value. |

---

[Back to the index](README.md) · [Back to top](#objectsannotation--dimensions-data-tags-title-block-borders-and-worksheets)
