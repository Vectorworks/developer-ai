**English** • [Deutsch](../../PythonAPI.de/v2027.2/ObjectsLandmark.md) • [日本語](../../PythonAPI.ja/v2027.2/ObjectsLandmark.md)

# ObjectsLandmark — plants, site models, hardscapes and other landscape objects

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The classes of the Landmark plug-in objects. `LandmarkObject` is their common base (generic parameter access). The specific classes are `PlantObject` ("Plant"), `LandscapeAreaObject` ("Landscape Area"), `SiteModelObject` ("DTM6", a terrain model with existing and proposed surfaces), `SiteModifierObject` ("Site Modifiers"), `StakeObject` ("Stake Object"), `HardscapeObject` ("Hardscape"), `PropertyLineObject` ("Property Line") and `ExistingTreeObject` ("Existing Tree").

All landmark objects are plug-in objects, told apart by the universal name of their record. `Is(h)` tests that name, `Create(...)` creates a new instance in the active layer / container, getters return `None` for an invalid object or a missing parameter and setters return `True` on success.

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [LandmarkObject](#landmarkobject)
  - [PlantObject](#plantobject)
    - [PlantObject.Config](#plantobjectconfig)
    - [PlantObject.TagDisplay](#plantobjecttagdisplay)
  - [LandscapeAreaObject](#landscapeareaobject)
    - [LandscapeAreaObject.PlantDisplay2D](#landscapeareaobjectplantdisplay2d)
    - [LandscapeAreaObject.DrawingMode](#landscapeareaobjectdrawingmode)
    - [LandscapeAreaObject.AreaUnits](#landscapeareaobjectareaunits)
  - [SiteModelObject](#sitemodelobject)
    - [SiteModelObject.Display2D](#sitemodelobjectdisplay2d)
    - [SiteModelObject.Display3D](#sitemodelobjectdisplay3d)
  - [SiteModifierObject](#sitemodifierobject)
    - [SiteModifierObject.Config](#sitemodifierobjectconfig)
    - [SiteModifierObject.ApplyTo](#sitemodifierobjectapplyto)
  - [StakeObject](#stakeobject)
    - [StakeObject.Mode](#stakeobjectmode)
    - [StakeObject.SiteModel](#stakeobjectsitemodel)
  - [HardscapeObject](#hardscapeobject)
    - [HardscapeObject.Mode3D](#hardscapeobjectmode3d)
  - [PropertyLineObject](#propertylineobject)
    - [PropertyLineObject.AreaUnits](#propertylineobjectareaunits)
  - [ExistingTreeObject](#existingtreeobject)
    - [ExistingTreeObject.Origin](#existingtreeobjectorigin)
    - [ExistingTreeObject.TreeProtection](#existingtreeobjecttreeprotection)
    - [ExistingTreeObject.Condition](#existingtreeobjectcondition)
    - [ExistingTreeObject.SULE](#existingtreeobjectsule)
    - [ExistingTreeObject.Significance](#existingtreeobjectsignificance)
    - [ExistingTreeObject.Action](#existingtreeobjectaction)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`LandmarkObject`](#landmarkobject) | class | [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) | Common base of the Landmark plug-in object classes (plant, landscape area, site model, site modifier, stake, hardscape, property line, existing tree). |
| [`PlantObject`](#plantobject) | class | [`LandmarkObject`](#landmarkobject) | Plant plug-in object (universal name "Plant") from the Landmark plug-in. |
| [`PlantObject.Config`](#plantobjectconfig) | IntEnum (nested) |  | Configuration and display |
| [`PlantObject.TagDisplay`](#plantobjecttagdisplay) | IntEnum (nested) |  | Where the plant tag is shown. |
| [`LandscapeAreaObject`](#landscapeareaobject) | class | [`LandmarkObject`](#landmarkobject) | Landscape area plug-in object (universal name "Landscape Area") from the Landmark plug-in. |
| [`LandscapeAreaObject.PlantDisplay2D`](#landscapeareaobjectplantdisplay2d) | IntEnum (nested) |  | How the plants of a landscape area are shown in 2D. |
| [`LandscapeAreaObject.DrawingMode`](#landscapeareaobjectdrawingmode) | IntEnum (nested) |  | Whether the object is drawn as a landscape area or as a hedgerow. |
| [`LandscapeAreaObject.AreaUnits`](#landscapeareaobjectareaunits) | IntEnum (nested) |  | Units in which the area of a landscape area is displayed. |
| [`SiteModelObject`](#sitemodelobject) | class | [`LandmarkObject`](#landmarkobject) | Site model plug-in object (universal name "DTM6") from the Landmark plug-in. |
| [`SiteModelObject.Display2D`](#sitemodelobjectdisplay2d) | IntEnum (nested) |  | 2D / 3D display selection |
| [`SiteModelObject.Display3D`](#sitemodelobjectdisplay3d) | IntEnum (nested) |  | What the 3D display of a site model shows. |
| [`SiteModifierObject`](#sitemodifierobject) | class | [`LandmarkObject`](#landmarkobject) | Site modifier plug-in object (universal name "Site Modifiers") of the Landmark plug-in. |
| [`SiteModifierObject.Config`](#sitemodifierobjectconfig) | IntEnum (nested) |  | Reshaping strategy of a site modifier ("Config"). |
| [`SiteModifierObject.ApplyTo`](#sitemodifierobjectapplyto) | IntEnum (nested) |  | Which site model surface a site modifier applies to. |
| [`StakeObject`](#stakeobject) | class | [`LandmarkObject`](#landmarkobject) | Stake plug-in object (universal name "Stake Object") from the Landmark plug-in. |
| [`StakeObject.Mode`](#stakeobjectmode) | IntEnum (nested) |  | Role of the stake with respect to the site model. |
| [`StakeObject.SiteModel`](#stakeobjectsitemodel) | IntEnum (nested) |  | Which site model surface a stake refers to. |
| [`HardscapeObject`](#hardscapeobject) | class | [`LandmarkObject`](#landmarkobject) | Hardscape plug-in object (universal name "Hardscape") from the Landmark plug-in. |
| [`HardscapeObject.Mode3D`](#hardscapeobjectmode3d) | IntEnum (nested) |  | 3D mode of the hardscape. |
| [`PropertyLineObject`](#propertylineobject) | class | [`LandmarkObject`](#landmarkobject) | Property line plug-in object (universal name "Property Line") from the Landmark plug-in. |
| [`PropertyLineObject.AreaUnits`](#propertylineobjectareaunits) | IntEnum (nested) |  | Area unit choices supported by both "Area Units Imperial" and "Area Units Metric" parameters. |
| [`ExistingTreeObject`](#existingtreeobject) | class | [`LandmarkObject`](#landmarkobject) | Existing tree plug-in object (universal name "Existing Tree") from the Landmark plug-in. |
| [`ExistingTreeObject.Origin`](#existingtreeobjectorigin) | IntEnum (nested) |  | Origin of an existing tree species. |
| [`ExistingTreeObject.TreeProtection`](#existingtreeobjecttreeprotection) | IntEnum (nested) |  | Tree Protection Zone display |
| [`ExistingTreeObject.Condition`](#existingtreeobjectcondition) | IntEnum (nested) |  | Arborist assessment |
| [`ExistingTreeObject.SULE`](#existingtreeobjectsule) | IntEnum (nested) |  | Safe Useful Life Expectancy |
| [`ExistingTreeObject.Significance`](#existingtreeobjectsignificance) | IntEnum (nested) |  | Significance rating of an existing tree. |
| [`ExistingTreeObject.Action`](#existingtreeobjectaction) | IntEnum (nested) |  | Proposed action for an existing tree. |

## Classes

### LandmarkObject

> **Full name:** `api.LandmarkObject` · **Inherits:** [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Common base of the Landmark plug-in object classes (plant, landscape area, site model, site modifier, stake, hardscape, property line, existing tree).

A Landmark object is a Vectorworks plug-in object (an instance of a plug-in registered by the Landscape / Vectorworks Landmark module; also called a parametric object in the API). Every landmark object is identified by its universal (parametric) name, e.g. "Plant", "Hardscape", "Existing Tree". The classes below check the universal name in their static `Is()` to distinguish among the plug-in kinds.

The class inherits from PrimitiveObject so every generic accessor (identity, class, attributes, hierarchy, bounds, move/rotate/scale/mirror, delete, ...) is available. In addition, this class exposes uniform, string-keyed access to the object's parametric record fields. The individual subclasses add named getters/setters for the most useful fields of each plug-in.

Conventions carried over from PrimitiveObject:

- Getters return `None` for an invalid object or a missing parameter.
- Setters return `True` on success and `False` for an invalid object or a missing parameter.
- Lengths are in world units, angles in radians, strings are UTF-8.

Parameter access primer (Get/SetParam*):

- Every landmark object stores its data as a record with named fields ("parameters"). Each subclass lists all available parameter names in its "Full parameter reference". Use those names verbatim (case-sensitive, UTF-8) with GetParamString / SetParamString / GetParamReal / ... to read or write any field the subclass does not already expose through a dedicated typed accessor.
- Parameter types in the tables use these tags:

- string — text (UTF-8) - GetParamString / SetParamString
- int — 32-bit integer - GetParamInt / SetParamInt
- bool — boolean - GetParamBool / SetParamBool
- real — floating-point (world coordinate, angle in degrees, area, volume, plain number, ...) - GetParamReal / SetParamReal
- popup — one-of-N string choice - GetParamString / SetParamString; valid values are listed next to the parameter

- When a getter returns `None` or a setter returns `False`, either the object is invalid or the parameter name does not exist on this object. Use `HasParam()` to test in advance.
- Parameter names that start with a double underscore ("__") are the plug-in's private state; they are readable but not usually meaningful to change directly.
- Parameters marked "read-only" or "computed" are updated by the plug-in during its reset; writing them typically has no lasting effect.

**Constructors**

| Constructor | Description |
|---|---|
| `LandmarkObject(h: Handle)` | Refers to any object `h` as a generic `LandmarkObject`; `IsValid()` only checks for a non-null handle. Use `GetParametricName()` or a concrete class's `Is(h)` to check the object kind. |

**Methods**

| Method | Description |
|---|---|
| `GetParametricName() -> str \| None` | Universal (parametric) name of this object, e.g. "Plant" or "Hardscape". Empty when the object is invalid or the underlying handle is not a plug-in object. |
| `HasParam(univParamName: str) -> bool` | Whether this plug-in object has a field with the given universal name. |
| `GetParamNames() -> list[str]` | Ordered list of every parameter (universal) name defined by this object's plug-in. |
| `GetParamType(univParamName: str) -> RecordFieldType \| None` | Data type of the parameter; `None` when the parameter does not exist. |
| `GetParamString(univParamName: str) -> str \| None` | Generic, string-keyed field accessors. Prefer the typed named accessors on the subclasses when available; use these for parameters that do not have a dedicated accessor. The getters return `None` when the parameter does not exist; the setters return `False`. |
| `SetParamString(univParamName: str, value: str) -> bool` | Sets the param string. Generic, string-keyed field accessors. Prefer the typed named accessors on the subclasses when available; use these for parameters that do not have a dedicated accessor. The getters return `None` when the parameter does not exist; the setters return `False`. |
| `GetParamReal(univParamName: str) -> float \| None` | Returns the param real for `univParamName`. |
| `SetParamReal(univParamName: str, value: float) -> bool` | Sets the param real. |
| `GetParamBool(univParamName: str) -> bool \| None` | Whether *Param Bool* is on for `univParamName`. |
| `SetParamBool(univParamName: str, value: bool) -> bool` | Sets the param bool. |
| `GetParamInt(univParamName: str) -> int \| None` | Returns the param int for `univParamName`. |
| `SetParamInt(univParamName: str, value: int) -> bool` | Sets the param int. |
| `GetPathObject() -> Handle` | Path object of a path-based plug-in object (hardscape, landscape area, site modifier, property line, ...). Returns null for point-based plug-in objects (single-instance plant, existing tree, stake) and when the object is invalid. |

Inherited: everything from [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

### PlantObject

> **Full name:** `api.PlantObject` · **Inherits:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Plant plug-in object (universal name "Plant") from the Landmark plug-in.

A plant is either a single instance placed at a location or a poly-based container that distributes many instances of the same species (single plant, plants at poly vertices, plants along poly edges, plants in a rectangular or triangular array). The configuration is controlled by the "config" parameter.

Common parameters exposed as named accessors:

- "plant ID" — the resource name of the plant symbol / style
- "spread" — diameter of the plant canopy, in world units
- "height" — height of the plant, in world units
- "latin name" — botanical (Latin) name
- "common name" — common name
- "PlantDescription" — short description
- "comments" — free-form comments
- "tag display" — None / Left / Right / Floating (tag placement relative to the plant)
- "config" — Single plant / Plants at poly vertices / Plants along poly edges / ... (see PlantObject)
- "Show 3D Detail" — whether to render 3D geometry

Use the generic LandmarkObject accessors (GetParamString / GetParamReal / ...) for any other field.

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Types: string (Text/StaticText), real (Real/CoordDisp/CoordLocX/CoordLocY/Angle/Area/Volume), int (LongInt), bool (Boolean), popup (string, one of the listed choices). Species / identity

- "plant ID" — string — symbol / style resource name (identifies the species)
- "PlantDescription" — string — human-readable description shown in the OIP
- "latin name" — string — botanical name
- "common name" — string — common name
- "comments" — string — free-form comments
- "custom ID" — string
- "isCustom" — bool — `True` for user-defined plants (not from the plant database)
- "onPlantList" — bool — include on the plant schedule
- "Category" — popup — category (e.g. None / Trees / Shrubs / ...)
- "Tag Schema" — string — schema for the tag body text
- "TagSchemaCenter" — string — tag center text
- "TagSchemaBottom" — string — tag bottom text
- "SKU" — string
- "Price" — real
- "HiddenName" — string

Size (world units)

- "spread" — real — canopy diameter
- "height" — real — overall height
- "spacing" — real — spacing between instances (for poly configurations)
- "image size" — real
- "Row spacing" — real — distance between rows in array modes
- "Rate" — real — plants per unit (see "Rate mode")
- "Percentage" — int — percent used for distribution modes
- "Plants per row" — int
- "Plants per column" — int
- "Plant height scale" — popup — Fixed / randAt5 / randAt10 / randAt15

Configuration and display

- "config" — popup — Single plant / Plants at poly vertices / Plants along poly edges / Plants in rectangular array / Plants in triangular array
- "plant style" — popup — No sketch / No sketch w/ shadows / Light sketch / Light sketch w/ shadows / Medium sketch / Medium sketch w/ shadows / Heavy sketch / Heavy sketch w/ shadows / Cloud / Cloud w/ shadows
- "tag display" — popup — None / Left / Right / Floating
- "poly display" — popup — None / Centers-Solid / Centers-Dashed / Boundary-Solid / Boundary-Dashed / Gapped-Solid / Gapped-Dashed
- "tickmark display" — popup — None / Cross / Dot / XMark
- "tickmark size" — real — size of the tickmark in world units
- "rotate mode" — popup — FALSE / AlongLine / TRUE
- "quantity measure" — popup — Count / Dripline area / Boundary area
- "Outline" — popup — No Outline / Tight Outline / One Outline / Two Outlines / Three Outlines
- "TagBubble" — popup — None / Circle / Circle (Quantity only) / Hexagon / Hexagon (Quantity only) / Rectangle / Round
- "TagApproachAngle" — real — degrees
- "TagShoulderAngle" — real — degrees
- "TagEnableShoulder" — bool
- "TagUseMarker" — bool
- "TagSnapCenters" — bool
- "display style" — bool
- "Show 3D Detail" — bool
- "ShowSettings" — bool
- "backGroundOnly" — bool
- "massPlants" — bool
- "Replace" — bool
- "drip cloud factor" — real
- "drip sketch factor" — popup — "1-Least sketchy" ... "9-Sketchiest"
- "tagClass" — popup — class name for the plant tag
- "tickClass" — popup — class name for the tickmarks
- "PolylineDisplayClass" — popup — class for the polyline display
- "MassOutlineClass" — popup — class for the mass outline

Shadows and appearance

- "ShadowEnable" — bool
- "ShadowAngle" — real — degrees
- "ShadowOffset" — real — world units
- "ShadowFillStyle" — string
- "FillStyle" — string
- "PenStyle" — string
- "FillStyleParam", "FillSolidColor", "FillPattern", "FillHatch", "FillGrad", "FillImage"
- "FillForeColor", "FillBackColor" — int (color indices)
- "PenStyleParam", "PenSolidColor", "PenForeColor", "PenBackColor" — int (color indices)
- "PenWeight", "PenDash", "PenPattern" — int
- "SymbolFPat", "SymbolFFore", "SymbolFBack" — int
- "UseDocumentShadow" — bool

Hedge / distribution options

- "Hedge" — bool — enable hedge mode
- "Hedge rows" — int
- "HedgeMode" — popup
- "HedgeModeNew" — popup — Rectangular / StaggeredRow / TripleStaggeredRow
- "HedgeRowSpacingMode" — popup — SameAsPlantSpacingOrRate / Fixed
- "HedgeRowSpacing" — real — world units
- "OffsetFromPath" — real — world units
- "OffsetRows" — bool
- "XOffset", "YOffset" — real — world units
- "Plant spacing mode" — popup — Custom spacing / Distrib by Rate / Distrib by Coverage
- "Spacing mode" — popup — Same as Plant Spread / Fixed / Best Fit / Count
- "Row spacing mode" — popup — Same as spacing / ...
- "Rate mode" — popup — Plants per unit / Unit on center / Plants per Linear Unit / Plants per Linear Unit Best Fit

3D geometry (procedurally generated tree)

- "3DGeometryCanopyShape" — int
- "3DGeometryCanopyHgt" — real — world units
- "gen_generated" — bool
- "gen_canopyShape" — string
- "gen_firstBranchHeight" — real — world units
- "gen_isFirstBranchHeightDefault" — bool
- "gen_trunkGirth" — real — world units
- "gen_canopyClass" — popup — class name
- "gen_trunkClass" — popup — class name
- "scraped_url" — string

Root zones (world units unless noted)

- "classRootZones" — popup — class name
- "classRootExcavation" — popup — class name
- "showRootBall" — popup — None / 2D Only / 3D Only / 2D and 3D
- "shapeRootBall" — popup — Sphere / B & B (Ball & Burlap)
- "sizeRootBall1", "sizeRootBall2", "sizeRootBall3" — real
- "attrByClassRootBall" — bool
- "lineWeightRootBall" — int
- "lineColorRootBall" — int — color index
- "showPlantingExcav" — popup — None / 2D Only / 3D Only / 2D and 3D
- "diamPlantingExcav" — popup — 1.5x the root ball / 2x the root ball / 3x the root ball / Custom
- "depthPlantingExcav" — popup — 1x the root ball / Custom
- "shapePlantingExcav" — popup — Round / Rectangular
- "diamValueExcav", "depthValueExcav" — real
- "attrByClassPlantingExcav" — bool
- "lineWeightPlantingExcav" — int
- "lineColorPlantingExcav" — int — color index
- "rootBallArea", "rootBallVolume" — real (read-only, computed)
- "plantingExcArea", "plantingExcVolume" — real (read-only, computed)

Maintenance / water

- "MaintenanceNotes" — string
- "PropagationNotes" — string
- "FireResilience", "FireRisk" — popup
- "IrrigationType" — popup
- "PointEmitterValue" — popup
- "PointEmitterQuantity" — int
- "PeakWaterRequirement" — real
- "PeakWaterRequirementUnits" — popup — InchesWeek / InchesMonth / LiterMinute / LiterHour / MillimeterWeek / MillimeterMonth
- "IrrigationFrequency" — int
- "IrrigationFrequencyUnits" — popup — PerDay / PerWeek / PerTwoWeeks / PerMonth
- "ActiveRegion" — popup

Site model interaction

- "siteModelLayer" — popup — layer name of the site model
- "__notSingleAutoDTM" — bool

Laubwerk 3D geometry (optional)

- "lw_Key", "lw_PlantFile", "lw_Variant" — string
- "lw_GlobalSeason" — bool
- "lw_Season" — string
- "lw_Global2D3DMat" — bool
- "lw_2DReprs", "lw_3DReprs" — string
- "lw_MaterialStyle" — string

Miscellaneous / read-only

- "DripArea" — real (read-only, computed)
- "TotalCanopyArea" — real (read-only, computed)
- "Version" — int — plug-in schema version
- "sustainability" — string — JSON blob of sustainability data
- "GroupAllocation" — string
- "SourcePlantList" — string
- "Factor" — real
- "Message" — string — OIP status/warning message
- "__ScheduledSize" — string
- "__Status" — int
- "__fade enabled", "__fade percent" — bool / int
- "ControlPoint01X..ControlPoint04Y" — real (world coordinates of the object's control points)

**Constructors**

| Constructor | Description |
|---|---|
| `PlantObject(h: Handle)` | Refers to the existing plant `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D, plantResourceName: str = '') -> PlantObject` *static* | Creates a single-instance plant at `position` in the active layer / current container. `plantResourceName` is the name of the plant style resource (a symbol definition holding a master plant) to use. It is imported from the Vectorworks plant content when it is not in the drawing yet. When empty - or when the named style cannot be found anywhere - the first available plant style is used. Returns an invalid object when no plant style is available at all, because a plant without a style has no graphics to draw. |
| `CreateFromPath(hPath: Handle, plantResourceName: str = '') -> PlantObject` *static* | Creates a poly-based plant that distributes instances along/over an existing 2D path object. Set the "config" parameter afterwards to choose the distribution mode. |
| `EnsurePlantStyle(styleName: str = '') -> str` *static* | Makes sure a plant style is available in the current drawing, importing it from the Vectorworks plant content when necessary, and returns its name (empty when no plant style could be made available). |
| `Duplicate() -> PlantObject` | Duplicates the plant in the drawing and returns the copy. |

*Plant style*

| Method | Description |
|---|---|
| `GetPlantStyle() -> str \| None` | The symbol definition the plant takes its graphics and default data from. This is the same value as the "PlantDescription" parameter, which is how the plant links to its style. |
| `SetPlantStyle(styleName: str) -> bool` | Imports `styleName` if needed, applies all of its settings to this plant and regenerates it. |

*Identity / species*

| Method | Description |
|---|---|
| `GetPlantID() -> str \| None` | Returns the plant ID (resource name of the plant symbol / style). |
| `SetPlantID(value: str) -> bool` | Sets the plant ID. |
| `GetLatinName() -> str \| None` | Returns the latin name. |
| `SetLatinName(value: str) -> bool` | Sets the latin name. |
| `GetCommonName() -> str \| None` | Returns the common name. |
| `SetCommonName(value: str) -> bool` | Sets the common name. |
| `GetPlantDescription() -> str \| None` | Name of the plant style symbol definition; prefer SetPlantStyle, which also imports the style and takes over its settings. Setting a name that is not in the drawing leaves the plant without graphics. |
| `SetPlantDescription(value: str) -> bool` | Sets the plant description. Name of the plant style symbol definition; prefer SetPlantStyle, which also imports the style and takes over its settings. Setting a name that is not in the drawing leaves the plant without graphics. |
| `GetComments() -> str \| None` | Returns the comments. |
| `SetComments(value: str) -> bool` | Sets the comments. |
| `GetSpread() -> float \| None` | Size (world units) (canopy diameter). |
| `SetSpread(value: float) -> bool` | Sets the spread (Size (world units)). |
| `GetHeight() -> float \| None` | Returns the height (plant height). |
| `SetHeight(value: float) -> bool` | Sets the height. |
| `GetConfig() -> PlantObject.Config \| None` | Returns the config. |
| `SetConfig(value: PlantObject.Config) -> bool` | Sets the config. |
| `GetTagDisplay() -> PlantObject.TagDisplay \| None` | Returns the tag display. |
| `SetTagDisplay(value: PlantObject.TagDisplay) -> bool` | Sets the tag display. |
| `GetShow3DDetail() -> bool \| None` | Whether *Show 3D Detail* is on. |
| `SetShow3DDetail(value: bool) -> bool` | Turns *Show 3D Detail* on or off. |
| `GetSpacing() -> float \| None` | Distance between plants along a poly edge or in an array configuration. |
| `SetSpacing(value: float) -> bool` | Sets the spacing. Distance between plants along a poly edge or in an array configuration. |

Inherited: everything from [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### PlantObject.Config

> **Full name:** `api.PlantObject.Config` · **Kind:** `IntEnum`

Configuration and display

| Member | Value | Description |
|---|---|---|
| `SinglePlant` | `0` |  |
| `PlantsAtPolyVertices` | `1` |  |
| `PlantsAlongPolyEdges` | `2` |  |
| `PlantsInRectangularArray` | `3` |  |
| `PlantsInTriangularArray` | `4` |  |

#### PlantObject.TagDisplay

> **Full name:** `api.PlantObject.TagDisplay` · **Kind:** `IntEnum`

Where the plant tag is shown.

| Member | Value | Description |
|---|---|---|
| `None_` | `0` |  |
| `Left` | `1` |  |
| `Right` | `2` |  |
| `Floating` | `3` |  |

### LandscapeAreaObject

> **Full name:** `api.LandscapeAreaObject` · **Inherits:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Landscape area plug-in object (universal name "Landscape Area") from the Landmark plug-in.

A landscape area is a path-based container that fills a 2D polygonal region with one or more plant species distributed by percentage. It computes projected / surface area and the total number of plants required.

The plant list itself (species, percentage, rate) is stored as an indexed collection managed by the plug-in; use the generic LandmarkObject accessors to read/write individual plant entries.

Common parameters exposed as named accessors:

- "name" — user-visible landscape area name / softscape name
- "ID" — identifier tag
- "Description" — short description
- "area" — computed area (read-only)
- "projectedArea" — projected area on the site model (read-only)
- "numPlants" — total plant count (read-only)
- "Drawing Mode" — "Landscape Area" or "Hedgerow"
- "areaUnits" — area display units (see `LandscapeAreaObject.AreaUnits`)
- "showPlants2D" — 2D plant display popup

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Identity / description

- "name" — string — softscape / landscape area name
- "ID" — string — identifier tag
- "Description" — string
- "Style Name Formula" — string — formula that generates the plant style name
- "Category" — popup — e.g. "Perennials"
- "InstanceName" — string — instance name (for reporting)
- "CustomCombName", "CustomCombFormula" — string
- "Drawing Mode" — popup — "Landscape Area" / "Hedgerow"

Measurements (read-only, recomputed on reset)

- "area" — real
- "projectedArea" — real
- "ProjectedAreaInLAUnits" — real
- "SurfaceAreaInLAUnits" — real
- "AreaLAUnits" — string
- "areaUnits" — popup — Square Feet / Square Meters / Acres / Hectares / Document Units
- "Hedgerow Length" — real
- "numPlants" — int — total number of distributed plants
- "numAttachedPlants" — int
- "Area Vertex Count" — string — read-only, formatted count
- "unitPrice" — real
- "priceCode" — string
- "AreaFactor" — real — multiplier used for area math

2D graphics

- "borderStyle" — popup — "Standard" / "None"
- "billowSize" — popup — X Small / Small / Medium / Large / X Large
- "billowVar" — popup — None / Low / Medium / High
- "billowHeight" — popup — Small / Medium / Large
- "billowType" — popup — Convex / Concave
- "segLength" — popup — X Short / Short / Normal / Long / X Long
- "segThickness" — popup — X Thin / Thin / Normal / Thick / X Thick
- "Smooth external corners" — bool
- "showPlants2D" — popup — None / PlantCloud / PlantLine / PlantSymbols (or FALSE)
- "showPlants3D" — popup — None / Plant Block / Individual Plants
- "diameterScalePopup" — popup — Fixed / Random 5% / Random 10% / Random 15%
- "diameterVisualScale" — real — percent
- "heightScalePopup" — popup — Fixed / Random 5% / Random 10% / Random 15%
- "heightVisualScale" — real — percent
- "randomizePlantRotation" — bool
- "randomizePlantPosition" — bool
- "allPlantEdgesInsideArea" — bool
- "plantBlockHeight" — real — world units

3D / site model

- "3dDisplay" — popup — None / Components / 3D Polygon / Texture Bed
- "displayAs3DPolygon" — bool
- "displayOnExisting" — bool
- "hasSiteModel" — bool
- "Cut into Site Model" — bool
- "siteModelLayer" — popup — layer name of the site model
- "minTINElev", "maxTINElev" — real (read-only)
- "__RecalcTINSurfaces", "__RecalcTINDependent" — bool (internal state)
- "__editComponents" — bool
- "Simplification Tolerance" — real

Plant list / rate distribution

- "distRate" — string — distribution rate mode (e.g. "CustomPerc")
- "percRate" — real — percent used for distribution
- "percType" — string — unit of the rate (per sqft / per sqm / ...)
- "hiddenSymbolName", "hiddenRate", "hiddenRateType", "hiddenPercentage" — string (internal state per entry)
- "hiddenMinNumOfPlants", "hiddenTotalNumOfPlants" — string
- "BestFit" — bool
- "HedgeSpacingEnum" — popup — SameAsPlantSpacingOrRate / Fixed
- "HedgeSpacingValue" — real

Hedgerow options

- "Width" — real
- "Row Structure" — popup — Rectangular / Staggered / Triple Staggered / Area
- "Hedge Rows" — int
- "Offset rows" — bool
- "PathOffset" — real

Tag

- "tagDisplay" — popup — None / Left / Right
- "displayMarker" — bool
- "tagClass" — popup — class name
- "tagLineAngle" — real — degrees
- "tagTextAngle" — real — degrees
- "tagHeader" — popup / string — formula for the tag header text
- "tagBody" — popup / string — formula for the tag body text
- "controlPoint1X..controlPoint3Y" — real (world coordinates for the tag control points)

Sustainability (legacy scalar fields + 2026 JSON blob)

- "HasSustainability" — bool
- "HasPermeability", "IsPermeable" — bool
- "Permeability" — real
- "Permeability Unit" — popup — cm/hour / ...
- "RunoffCoef" — real
- "SRI" — real
- "Sustainability Metric" — string
- "SusPoint1", "SusPoint2", "SusPoint3" — string
- "sustainability" — string — 2026+ JSON blob

Miscellaneous

- "version" — int
- "__IsNew" — bool
- "GroupAllocation" — string

**Constructors**

| Constructor | Description |
|---|---|
| `LandscapeAreaObject(h: Handle)` | Refers to the existing landscape area `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `CreateFromPath(hPath: Handle) -> LandscapeAreaObject` *static* | Creates a landscape area from an existing 2D path object (typically a polygon or polyline). |
| `Duplicate() -> LandscapeAreaObject` | Duplicates the landscape area in the drawing and returns the copy. |

*Identity*

| Method | Description |
|---|---|
| `GetName() -> str \| None` | Returns the name ("name" (softscape name), not the object name). |
| `SetName(value: str) -> bool` | Sets the name. |
| `GetID() -> str \| None` | Returns the ID. |
| `SetID(value: str) -> bool` | Sets the ID. |
| `GetDescription() -> str \| None` | Returns the description. |
| `SetDescription(value: str) -> bool` | Sets the description. |
| `GetArea() -> float \| None` | Measurements (read-only; computed by the object during its reset) (area of the region in the current area units). |
| `GetProjectedArea() -> float \| None` | Returns the projected area (projected onto the site model (0 when there is none)). |
| `GetNumPlants() -> int \| None` | Returns the num plants (total number of plant instances distributed). |
| `GetDrawingMode() -> LandscapeAreaObject.DrawingMode \| None` | Returns the drawing mode. |
| `SetDrawingMode(value: LandscapeAreaObject.DrawingMode) -> bool` | Sets the drawing mode. |
| `GetAreaUnits() -> LandscapeAreaObject.AreaUnits \| None` | Returns the area units. |
| `SetAreaUnits(value: LandscapeAreaObject.AreaUnits) -> bool` | Sets the area units. |
| `GetPlantDisplay2D() -> LandscapeAreaObject.PlantDisplay2D \| None` | Returns the plant display 2D. |
| `SetPlantDisplay2D(value: LandscapeAreaObject.PlantDisplay2D) -> bool` | Sets the plant display 2D. |

*Compatibility accessors*

| Method | Description |
|---|---|
| `GetShowPlantsIn2D() -> bool \| None` | `True` for any non-`None` display; setting `True` selects PlantSymbols, setting `False` selects `None`. Use the popup accessors to preserve cloud/line modes. |
| `SetShowPlantsIn2D(show: bool) -> bool` | Turns *Show Plants In 2D* on or off. `True` for any non-`None` display; setting `True` selects PlantSymbols, setting `False` selects `None`. Use the popup accessors to preserve cloud/line modes. |

Inherited: everything from [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### LandscapeAreaObject.PlantDisplay2D

> **Full name:** `api.LandscapeAreaObject.PlantDisplay2D` · **Kind:** `IntEnum`

How the plants of a landscape area are shown in 2D.

| Member | Value | Description |
|---|---|---|
| `None_` | `0` |  |
| `PlantCloud` | `1` |  |
| `PlantLine` | `2` |  |
| `PlantSymbols` | `3` |  |

#### LandscapeAreaObject.DrawingMode

> **Full name:** `api.LandscapeAreaObject.DrawingMode` · **Kind:** `IntEnum`

Whether the object is drawn as a landscape area or as a hedgerow.

| Member | Value | Description |
|---|---|---|
| `LandscapeArea` | `0` |  |
| `Hedgerow` | `1` |  |

#### LandscapeAreaObject.AreaUnits

> **Full name:** `api.LandscapeAreaObject.AreaUnits` · **Kind:** `IntEnum`

Units in which the area of a landscape area is displayed.

| Member | Value | Description |
|---|---|---|
| `SqFeet` | `0` |  |
| `SqMeters` | `1` |  |
| `Acres` | `2` |  |
| `Hectares` | `3` |  |
| `DocumentUnits` | `4` |  |

### SiteModelObject

> **Full name:** `api.SiteModelObject` · **Inherits:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Site model plug-in object (universal name "DTM6") from the Landmark plug-in.

A site model is a triangulated irregular network (TIN) surface built from source data (survey points, contour lines, boundary polygons, ...). It carries two surfaces at once: the existing terrain and the proposed terrain (which reflects any site modifiers applied to it).

Common parameters exposed as named accessors:

- "2D Display" — which surface(s) to draw in 2D (Existing / Proposed / Both)
- "2D Style" — 2D visual style (contours, triangles, colored slopes, ...)
- "3D Display" — which surface(s) to draw in 3D (Nothing / Existing / Proposed / Cut&Fill)
- "3D Style" — 3D visual style (mesh, grid, contours, colored elevation / slopes, ...)
- "Area Display Type" — area units for the info panel
- "Volume Display Type" — volume units for the info panel
- "Geometry Zref" — reference elevation
- "Show Errors" — display TIN error markers

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Display selection

- "2D Display" — popup — `kTINDisplayExistingOnly` / `kTINDisplayProposedOnly` / `kTINDisplayExistingAndProposed`
- "2D Style" — popup — k2DTINStyle2DContour / k2DTINStyle2DContourSmoothed / k2DTINStyle2DContourColoredElevations / k2DTINStyle2DTriangulatedContoursColoredSlopes / k2DTINStyle2DTriangles / k2DTINStyle2DTrianglesColoredSlopes
- "3D Display" — popup — `kTINDisplayNothing` / `kTINDisplayExistingOnly` / `kTINDisplayProposedOnly` / `kTINDisplayCutNFill`
- "3D Style" — popup — k3DTINStyleMesh / k3DTINStyleMeshColoredElev / k3DTINStyleMeshColoredSlopes / k3DTINStyleGrid / k3DTINStyleGridColoredElev / k3DTINStyleGridColoredSlope / k3DTINStyleVerticalGrid / k3DTINStyleContour / k3DTINStyleExtrudedContour / k3DTINStyleExtContColoredElev
- "2D C&F Map Overlay" — bool

Area / volume readouts (all are read-only, formatted string values)

- "Area Display Type" — popup — `kAreaDisplaySqM` / `kAreaDisplayDecar` / `kAreaDisplayHectars` / `kAreaDisplaySqFt` / `kAreaDisplayAcre` / `kAreaUseDocumentUnits`
- "Projected Area (Existing)" — string
- "Surface Area (Existing)" — string
- "Surface Area (Proposed)" — string
- "Volume Display Type" — popup — `kVolumeDisplayCuM` / `kVolumeDisplayCuFt` / `kVolumeDisplayCuYd` / `kVolumeUseDocumentUnits`
- "Volume (Existing)" — string
- "Volume (Proposed)" — string
- "Cut Volume" — string
- "Fill Volume" — string
- "Net C&F Volume" — string
- "Total C&F Volume" — string

Geometry / errors

- "Geometry Zref" — real — world units - reference elevation
- "Grid Size" — real
- "Tolerance" — real
- "Depth Intervals" — real
- "Show Errors" — bool
- "dontShowErrors" — bool — (legacy)
- "Error Count" — string — read-only formatted count
- "Site Model Name" — string — read-only display name

Geoimage overlay

- "GeoImageEnabled" — bool
- "GeoServerURL" — string
- "GeoServiceName" — string
- "GeoServiceType" — string
- "GeoServiceRenderFunc" — popup
- "GeoLayers" — string
- "GeoResolution" — int — pixels per tile
- "GeoTile" — int
- "StoreGeoimage" — bool

Internal state

- "__version", "__messageID" — int
- "__UUID" — string
- "__compsMinZ" — real
- "__SavedGeoinfo" — string

**Constructors**

| Constructor | Description |
|---|---|
| `SiteModelObject(h: Handle)` | Refers to the existing site model `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D) -> SiteModelObject` *static* | Site models are typically created interactively through the Landmark commands (survey points, contour lines, ...); this factory creates an empty site model at `position` that the caller then populates using the corresponding menu commands or by editing its source data group. |
| `Duplicate() -> SiteModelObject` | Duplicates the site model in the drawing and returns the copy. |
| `Get2DDisplay() -> SiteModelObject.Display2D \| None` | Returns the 2D display. |
| `Set2DDisplay(value: SiteModelObject.Display2D) -> bool` | Sets the 2D display. |
| `Get3DDisplay() -> SiteModelObject.Display3D \| None` | Returns the 3D display. |
| `Set3DDisplay(value: SiteModelObject.Display3D) -> bool` | Sets the 3D display. |
| `Get2DStyle() -> str \| None` | Raw display style values (see the Landmark documentation for the full list of styles). The style names are ASCII identifiers such as "k2DTINStyle2DTriangles" or "k3DTINStyleMesh". |
| `Set2DStyle(value: str) -> bool` | Sets the 2D style. Raw display style values (see the Landmark documentation for the full list of styles). The style names are ASCII identifiers such as "k2DTINStyle2DTriangles" or "k3DTINStyleMesh". |
| `Get3DStyle() -> str \| None` | Returns the 3D style. |
| `Set3DStyle(value: str) -> bool` | Sets the 3D style. |
| `GetGeometryZReference() -> float \| None` | Reference elevation (world units) used by contour-based calculations. |
| `SetGeometryZReference(value: float) -> bool` | Sets the geometry Z reference. Reference elevation (world units) used by contour-based calculations. |
| `GetShowErrors() -> bool \| None` | Whether *Show Errors* is on. |
| `SetShowErrors(value: bool) -> bool` | Turns *Show Errors* on or off. |
| `GetProjectedAreaExisting() -> str \| None` | Read-only area and volume readouts (formatted string; empty when not computed). |
| `GetSurfaceAreaExisting() -> str \| None` | Returns the surface area existing. |
| `GetSurfaceAreaProposed() -> str \| None` | Returns the surface area proposed. |
| `GetVolumeExisting() -> str \| None` | Returns the volume existing. |
| `GetVolumeProposed() -> str \| None` | Returns the volume proposed. |
| `GetCutVolume() -> str \| None` | Returns the cut volume. |
| `GetFillVolume() -> str \| None` | Returns the fill volume. |

Inherited: everything from [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### SiteModelObject.Display2D

> **Full name:** `api.SiteModelObject.Display2D` · **Kind:** `IntEnum`

2D / 3D display selection

| Member | Value | Description |
|---|---|---|
| `ExistingOnly` | `0` |  |
| `ProposedOnly` | `1` |  |
| `ExistingAndProposed` | `2` |  |

#### SiteModelObject.Display3D

> **Full name:** `api.SiteModelObject.Display3D` · **Kind:** `IntEnum`

What the 3D display of a site model shows.

| Member | Value | Description |
|---|---|---|
| `Nothing` | `0` |  |
| `ExistingOnly` | `1` |  |
| `ProposedOnly` | `2` |  |
| `CutAndFill` | `3` |  |

### SiteModifierObject

> **Full name:** `api.SiteModifierObject` · **Inherits:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Site modifier plug-in object (universal name "Site Modifiers") of the Landmark plug-in.

A site modifier is a path-based object that reshapes a site model surface. A single site modifier carries several possible configurations chosen through the "Config" parameter; every configuration applies to the "Existing" or the "Proposed" surface as chosen through the "Apply To" parameter.

Common parameters exposed as named accessors:

- "Config" — which reshaping strategy to use (see `SiteModifierObject.Config` below)
- "Apply To" — which site model surface receives the modification (Existing / Proposed)
- "Show 3D" — display the modifier as 3D geometry
- "Retain Slope Inside" — preserve the slope inside the modifier footprint
- "Simplification Tolerance" — vertex simplification tolerance, in world units

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices). The site modifier stores parameters from every configuration at once; only the parameters that belong to the current "Config" value are actually used by the plug-in. Common (all configurations)

- "Config" — popup — Fence (=Grade Limits) / Contour / Pad / PadwEdge (=Pad with Retaining Edge) / Aligned / Path / Texture Bed / Grader (=Spoil Pile)
- "Apply To" — popup — Existing / Proposed
- "Show 3D" — bool
- "Retain Slope Inside" — bool
- "Simplification Tolerance" — real — world units
- "Modifier Vertex Count" — string — read-only formatted count
- "__version" — int
- "__IsNewObject" — bool
- "__WasGeometryChanged", "__WasSideDataChanged", "__IsInvalPath", "__ChangeAffectsSiteModel" — bool (internal)

Grade Limits (Config = "Fence")

- "Define by contours" — bool
- "Use as C&F Calc Zone" — bool
- "__AreContoursConnected" — bool (internal)

Planar Pad (Config = "Pad") and Pad with Retaining Edge (Config = "PadwEdge")

- "Elevation" — real — world units
- "Slope Def" — popup — None / Angle / DownPerc / UpPerc / DownRatio / UpRatio
- "Slope Ang" — real — degrees (used when Slope Def = Angle)
- "Slope Percent" — string — e.g. "5%" (used when Slope Def = DownPerc/UpPerc)
- "Slope Ratio" — string — e.g. "1:4" (used when Slope Def = DownRatio/UpRatio)
- "ElevAtEnd" — real — world units
- "ContourAng" — real — degrees
- "Slope A", "Slope B" — string
- "Show Cross Slope" — bool
- "Show Slope A Arrow" — bool
- "Show Slope B Arrow" — bool
- "Constrain Slope Down" — bool
- "Show Slope Elevations" — bool
- "Show Modifier Elevation" — bool
- "Annotation Class" — popup — class name
- "__DoElevateRetEdge" — bool (pad with retaining edge only)
- "__UseSlopeToolAtCreate" — bool

Aligned (Config = "Aligned")

- "Align with Objects on" — popup — AllLayers / VisLayersOnly / SameLayerAsHScape / CustomSetOfLayers / SelectLayers
- "AlignWithObjectsOnOption" — int
- "Interpolate Surface" — bool
- "Interpolation Type" — popup — Concave / Convex
- "Show Profile Lines" — bool
- "Show Profile Names" — bool
- "Show Slopes" — bool
- "Show Vertex Elevation" — bool
- "Show Profile Line Markers" — bool
- "Show Stake Objects" — bool
- "Show Grade Objects" — bool
- "Start Symbol Marker Name" — string — symbol name
- "End Symbol Marker Name" — string — symbol name
- "Smoothness Sampling" — int
- "Falloff" — string — percent, e.g. "50,00%"
- "__RecreateAlignedTIN" — bool (internal)

Path (Config = "Path")

- "LongProf_StartElevValue" — real — world units
- "LongProf_EndElevValue" — real — world units
- "LongProf_MarkerType" — popup — None / Triangle / TriangleFilled / Circle / Dot / Cross / Circle Cross / Tick Mark
- "LongProf_MarkerFactor" — real
- "LongProf_SlopesDef" — popup — GradePerc / Ratio / Angle
- "LongProf_ShowLine", "LongProf_ShowSlopes", "LongProf_ShowVertexElev", "LongProf_ShowLineMarkers" — bool
- "LongProf_StartSymMarkerName", "LongProf_EndSymMarkerName" — string
- "TransProf_SlopesDef" — popup — GradePerc / Ratio / Angle
- "TransProf_ShowLines", "TransProf_ShowNames", "TransProf_ShowSlopes", "TransProf_ShowVertexElev", "TransProf_ShowLineMarkers" — bool
- "TransProf_StartSymMarkerName", "TransProf_EndSymMarkerName" — string
- "Prof_SlopeArrowDownward" — bool
- "__RecreatePathTIN", "__FitLongProfToSurf" — bool (internal)

Fit To Objects (Config = "Aligned", sub-mode)

- "Use Objects on" — popup — AllLayers / VisLayersOnly / SameLayerAsObject / CustomSetOfLayers / SelectLayers
- "Fit to" — popup — FitBottom / FitTop
- "__IsPathOK" — bool (internal)

Texture Bed (Config = "Texture Bed")

- "Texture Class" — popup — class name to use as the texture bed

Area / volume readouts (see the "Volume Display Type" popup)

- "Area Display Type" — popup — `kAreaDisplaySqM` / `kAreaDisplayDecar` / `kAreaDisplayHectars` / `kAreaDisplaySqFt` / `kAreaDisplayAcre` / `kAreaUseDocUnits`
- "Projected Area" — string (read-only)
- "Surface Area (Existing)" — string (read-only)
- "Surface Area (Proposed)" — string (read-only)
- "Volume Display Type" — popup — `kVolumeDisplayCuM` / `kVolumeDisplayCuFt` / `kVolumeDisplayCuYd` / `kVolumeUseDocUnits`
- "Volume (Existing)" — string (read-only)
- "Volume (Proposed)" — string (read-only)
- "Cut Volume" — string (read-only)
- "Fill Volume" — string (read-only)
- "Net C&F Volume" — string (read-only)
- "Total C&F Volume" — string (read-only)

Legacy (used by objects created in earlier Vectorworks versions)

- "Zref" — real
- "Slope" — real
- "SlopeDef" — popup — None / Angle / DownPerc / Percent / DownRatio / UpRatio
- "Prop" — popup — Existing / Proposed
- "Class" — popup — class name
- "ControlPoint01X..ControlPoint14Y" — real (world coordinates)
- "Show Slope Arrow" — bool

**Constructors**

| Constructor | Description |
|---|---|
| `SiteModifierObject(h: Handle)` | Refers to the existing site modifier `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `CreateFromPath(hPath: Handle) -> SiteModifierObject` *static* | Creates a site modifier from an existing 2D path object (polygon or polyline). |
| `Duplicate() -> SiteModifierObject` | Duplicates the site modifier in the drawing and returns the copy. |
| `GetConfig() -> SiteModifierObject.Config \| None` | Returns the config. |
| `SetConfig(value: SiteModifierObject.Config) -> bool` | Sets the config. |
| `GetApplyTo() -> SiteModifierObject.ApplyTo \| None` | Returns the apply to. |
| `SetApplyTo(value: SiteModifierObject.ApplyTo) -> bool` | Sets the apply to. |
| `GetShow3D() -> bool \| None` | Whether *Show 3D* is on. |
| `SetShow3D(value: bool) -> bool` | Turns *Show 3D* on or off. |
| `GetRetainSlopeInside() -> bool \| None` | Whether *Retain Slope Inside* is on. |
| `SetRetainSlopeInside(value: bool) -> bool` | Turns *Retain Slope Inside* on or off. |
| `GetSimplificationTolerance() -> float \| None` | Returns the simplification tolerance. |
| `SetSimplificationTolerance(value: float) -> bool` | Sets the simplification tolerance. |

Inherited: everything from [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### SiteModifierObject.Config

> **Full name:** `api.SiteModifierObject.Config` · **Kind:** `IntEnum`

Reshaping strategy of a site modifier ("Config").

| Member | Value | Description |
|---|---|---|
| `GradeLimits` | `0` | Closed fence limiting how far the modification can go. |
| `Contour` | `1` | Contour line at a fixed elevation. |
| `Pad` | `2` | Flat pad at a target elevation. |
| `RetainingPad` | `3` | Pad with a retaining edge. |
| `Aligned` | `4` | Aligned surface using per-side elevations and slopes. |
| `Path` | `5` | Path with a longitudinal profile. |
| `FitToObjects` | `6` | Interpolates from the elevation of the objects passing through the polygon. |
| `TextureBed` | `7` | 3D texture bed (no elevation change). |
| `SpoilPile` | `8` | Piles material at a slope until it reaches a volume / height. |

#### SiteModifierObject.ApplyTo

> **Full name:** `api.SiteModifierObject.ApplyTo` · **Kind:** `IntEnum`

Which site model surface a site modifier applies to.

| Member | Value | Description |
|---|---|---|
| `Existing` | `0` |  |
| `Proposed` | `1` |  |

### StakeObject

> **Full name:** `api.StakeObject` · **Inherits:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Stake plug-in object (universal name "Stake Object") from the Landmark plug-in.

A stake is a labeled 2D point placed at a specific location and elevation. Depending on its "Mode", the stake either contributes its elevation as source data for a site model, sets its elevation to the current site model surface, acts as a 2D graphic only, or represents a site modifier point.

Common parameters exposed as named accessors:

- "Mode" — role of the stake (see `StakeObject.Mode` below)
- "Site Model" — which site model surface the stake targets ("Existing" or "Proposed")
- "ID" — numeric identifier
- "ID Prefix" — prefix prepended to the ID in labels
- "ID Suffix" — suffix appended to the ID in labels
- "Z Value" — elevation (world units)
- "Data" — free-form description
- "Label ReferenceN" — which data appears on the stake's label

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Role and target site model

- "Mode" — popup — Include as site model data / Set elev to site model grade / Set elev to site model cut surface / Set elev to object spot / Use as 2D graphic only / Site modifier object
- "Previous Mode" — string — last selected Mode value (used by the plug-in)
- "Site Model" — popup — Existing / Proposed

Identity / label

- "ID" — int — numeric identifier
- "ID Prefix" — string
- "ID Suffix" — string
- "Data" — string — free-form description
- "Label Reference" — string — legacy label reference
- "Label ReferenceN" — popup — ID / Elevation / Description / ID/Elevation / ID/Description / Description/Elevation / Stationing Data / Coordinate PointNE / Coordinate PointEN / Coordinate PointXY / Coordinate PointYX / Latitude/Longitude / Longitude/Latitude / Latitude/Longitude(WGS84) / Longitude/Latitude(WGS84) / No Label / Object Spot Height
- "Label Position" — popup — Auto / Right / Left / Center
- "Style" — popup — none / Triangle / TriangleFilled / Circle / Dot / Cross / Circle Cross / Tick Mark
- "AutoIDNumber" — bool
- "InitIDNumber" — int
- "Bubble Style" — popup — None / Box / Round Rect / Cloud / Hexagonal / Circle
- "Radius Factor" — real
- "Margin" — real
- "UseAnnotation" — popup — Data Tag / Built-in Tag
- "DataTagStyle" — popup — data tag style resource name
- "LabelText", "LabelValues" — string

Elevation and coordinates

- "Z Value" — real — world units (elevation)
- "Station Point Data" — real — world units
- "Coordinate Units" — popup — Document units / CRS units / Feet / Meters
- "ElevationUnits" — popup — Document units / Feet/Inches / Inches / Feet / Yards / Miles / Microns / Millimeters / Centimeters / Meters / Kilometers / Decimal Degrees / Degrees/Minutes/Seconds
- "CoordinatePrecM" — popup — 1 / .1 / .01 / .001 / .0001 / ... / .0000000001
- "CoordinatePrecA" — popup — 0.0 / 0.00 / 0.000 / 0.0000 / ... / 0.00000000
- "ElevationPrecM", "ElevationPrecA" — popup (same choices as CoordinatePrecM/A)
- "ShowUnitMark" — bool
- "ShowElevationMark" — bool
- "Latitude", "Longitude", "Latitude WGS84", "Longitude WGS84" — real
- "Easting", "Northing" — real
- "Easting Display", "Northing Display" — string (read-only formatted values)

Display

- "Display Leader Line" — bool
- "3D Display" — popup — None / Locus / Extrude
- "ExtrudeWidth", "ExtrudeHeight" — real (world units)
- "Scale Factor" — real
- "markOffsetX", "markOffsetY" — real (world units)
- "markRot" — real (degrees)
- "ControlPoint01X", "ControlPoint01Y" — real (world units)

Internal / versioning

- "__version" — int
- "__new" — bool
- "__toolpref" — bool
- "__dtmElevCalculated" — bool
- "__DataTagStyleName" — string

**Constructors**

| Constructor | Description |
|---|---|
| `StakeObject(h: Handle)` | Refers to the existing stake `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D, zValue: float = 0.0) -> StakeObject` *static* | Creates a stake at `position` in the active layer / current container. |
| `Duplicate() -> StakeObject` | Duplicates the stake in the drawing and returns the copy. |
| `GetMode() -> StakeObject.Mode \| None` | Returns the mode. |
| `SetMode(value: StakeObject.Mode) -> bool` | Sets the mode. |
| `GetSiteModel() -> StakeObject.SiteModel \| None` | Returns the site model. |
| `SetSiteModel(value: StakeObject.SiteModel) -> bool` | Sets the site model. |
| `GetID() -> int \| None` | Returns the ID. |
| `SetID(value: int) -> bool` | Sets the ID. |
| `GetIDPrefix() -> str \| None` | Returns the ID prefix. |
| `SetIDPrefix(value: str) -> bool` | Sets the ID prefix. |
| `GetIDSuffix() -> str \| None` | Returns the ID suffix. |
| `SetIDSuffix(value: str) -> bool` | Sets the ID suffix. |
| `GetZValue() -> float \| None` | Returns the Z value (elevation, in world units). |
| `SetZValue(value: float) -> bool` | Sets the Z value. |
| `GetData() -> str \| None` | Returns the data (free-form description shown on the label). |
| `SetData(value: str) -> bool` | Sets the data. |
| `GetLabelReference() -> str \| None` | What the stake's label displays (ID / Elevation / Description / combinations / coordinates / ...) |
| `SetLabelReference(value: str) -> bool` | Sets the label reference. What the stake's label displays (ID / Elevation / Description / combinations / coordinates / ...) |
| `GetDisplayLeaderLine() -> bool \| None` | Whether *Display Leader Line* is on. |
| `SetDisplayLeaderLine(value: bool) -> bool` | Turns *Display Leader Line* on or off. |
| `GetShowElevationMark() -> bool \| None` | Whether *Show Elevation Mark* is on. |
| `SetShowElevationMark(value: bool) -> bool` | Turns *Show Elevation Mark* on or off. |

Inherited: everything from [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### StakeObject.Mode

> **Full name:** `api.StakeObject.Mode` · **Kind:** `IntEnum`

Role of the stake with respect to the site model.

| Member | Value | Description |
|---|---|---|
| `SiteModelSource` | `0` | "Include as site model data" - the stake's Z is a source point. |
| `SetToSiteModelGrade` | `1` | "Set elev to site model grade". |
| `SetToCutSurface` | `2` | "Set elev to site model cut surface". |
| `SetToObjectSpot` | `3` | "Set elev to object spot". |
| `Graphic2DOnly` | `4` | "Use as 2D graphic only". |
| `SiteModifierObject` | `5` | "Site modifier object". |

#### StakeObject.SiteModel

> **Full name:** `api.StakeObject.SiteModel` · **Kind:** `IntEnum`

Which site model surface a stake refers to.

| Member | Value | Description |
|---|---|---|
| `Existing` | `0` |  |
| `Proposed` | `1` |  |

### HardscapeObject

> **Full name:** `api.HardscapeObject` · **Inherits:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Hardscape plug-in object (universal name "Hardscape") from the Landmark plug-in.

A hardscape is a path-based object that represents a paved surface (walkway, patio, driveway, ...). It can be a boundary hardscape or a pathway hardscape (constant-width strip along the path). It may include a border, generate 3D geometry (slab, pad-over, pad-under, texture bed), and report main/border areas and perimeters.

Common parameters exposed as named accessors:

- "ID" — user-facing identifier / surface material name
- "Sketch" — sketch style (see the plug-in for the full list)
- "Tag Display" — tag placement (None / Right / Left / Floating)
- "Tag Style" — information shown on the tag
- "Draw 3D" — generate 3D geometry
- "Site Mod" — act as a site modifier
- "isPathway" — pathway (fixed-width strip) mode
- "Use Border" — include a border component
- "Slab Thick" — slab thickness (world units)
- "Border Thick" — border thickness (world units)
- "Path Wid" — pathway width (world units, pathway mode only)
- "Path Offset" — pathway offset (world units, pathway mode only)
- "Main Area", "Border Area", "Footprint Area", "Perimeter" — read-only measurements

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices). A hardscape also carries the entire site modifier parameter set (see SiteModifierObject); those parameters are active only when "Use Site Modifier" is TRUE and the hardscape drives a site modifier. Identity / description

- "ID" — string — user-facing surface / material identifier
- "IDN" — string — alternate ID field
- "Instance Name" — string
- "Custom combination name" — string
- "Custom combination formula" — string
- "Description" — string
- "Category" — popup — e.g. Paving (category taxonomy)
- "Style Name Formula" — string
- "__NNA_Version" — int — plug-in schema version
- "__xver", "__modeOffset" — int / real

Mode selectors

- "Sketch" — popup — Single sketch / other sketch-quality choices
- "isPathway" — bool
- "Draw 3D" — bool
- "Site Mod" — bool
- "Use Border" — bool
- "Configuration" — int
- "Mode 3D" — popup (str) — "0" = None / "1" = Slab / "2" = Pad Under / "3" = Texture Bed / "4" = Pad Over
- "New Mode 3D" — popup
- "Use Site Modifier" — bool
- "Site Model Interaction" — popup — e.g. ActAsSiteModifier
- "TextBedClass" — string
- "ConvertToBoundary" — bool

Path / border dimensions (world units unless noted)

- "Path Wid" — real — pathway width
- "Path Offset" — real — pathway offset from the path
- "Border Wid" — real — border width
- "Bord Spacing" — real
- "Bord Path Opt" — int
- "Bord Back CIdx" — int — color index of the border back color
- "Slab Thick" — real
- "Border Thick" — real

Joint / hatch patterns

- "Main Rsrc Name" — string — resource name of the main joint pattern
- "Bord Rsrc Name" — string — resource name of the border joint pattern
- "Main Joint Patt" — int
- "Bord Joint Patt" — int
- "Main Jt Patt Mod" — real
- "Main Jt Patt Y Mod" — real
- "Main Jt Patt Ang" — real — degrees
- "Bord Jt Patt Ang" — real — degrees
- "Main Jt I Scale", "Main Jt J Scale" — real
- "Bord Jt I Scale", "Bord Jt J Scale" — real
- "MainJointClass", "BorderJointClass" — popup — class name

Radial / path paver options (when used with radial or path patterns)

- "Radial Course Spacing" — real — world units
- "Radial Center Paver Diam" — real
- "Radial Offset Mode" — string
- "Radial Offset Width" — real
- "Radial Offset Angle" — real — degrees
- "Radial Offset Shift" — real
- "Radial Inside Paver Width" — real
- "Radial Count Paver Width" — int
- "Path Paver Width" — real
- "Path Paver Length" — real
- "Path Paver Length Is Rand" — bool
- "Path Paver Rand Pct Length" — real
- "Path Paver Offset Mode" — string
- "Path Paver Offset Width" — real
- "Path Paver Offset Shift" — real

Tag

- "Tag Display" — popup — None / Right / Left / Floating
- "Tag Style" — popup — ID only / ID-Area(s) / ID-Area(s)-Perim
- "TagAlignment" — popup — Underline / Center
- "TagApproachAngle" — real — degrees
- "TagShoulderAngle" — real — degrees
- "TagUseMarker" — bool
- "TagSnapEdge" — bool
- "tagClass" — popup — class name
- "SlopeArrowClass" — popup — class name

Measurements (read-only, computed at reset)

- "Main Area" — real — (area)
- "Border Area" — real
- "Footprint Area" — real
- "Perimeter" — real — world units
- "Main Perimeter" — real
- "Border Perimeter" — real
- "Main Area Fill Color" — int — color index
- "Fill Type" — int

Pricing

- "Main Unit Price" — real
- "Border Unit Price" — real
- "Main Price Code" — string
- "Border Price Code" — string

Control points (world units, driven by the reshape provider)

- "ControlPoint01X..ControlPoint21Y" — real

Sustainability (legacy scalar fields + JSON blob)

- "IsPermeable" — bool
- "RunoffCoef" — real
- "Sustainability Metric" — string
- "SusPoint1", "SusPoint2", "SusPoint3" — string
- "SRI" — real
- "HasSustainability", "HasPermeability" — bool
- "Permeability" — real
- "Permeability Unit" — popup — cm/hour / ...
- "sustainability" — string — JSON blob (VW2026+)

Site modifier parameters carried by the hardscape (see SiteModifierObject for the full list): "Config", "Apply To", "Show 3D", "Retain Slope Inside", "Simplification Tolerance", plus Pad / Aligned / Path / Fit-To-Objects / Texture Bed and Area / Volume readout parameters.

**Constructors**

| Constructor | Description |
|---|---|
| `HardscapeObject(h: Handle)` | Refers to the existing hardscape `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `CreateFromPath(hPath: Handle) -> HardscapeObject` *static* | Creates a hardscape from an existing 2D path object (polygon or polyline). |
| `Duplicate() -> HardscapeObject` | Duplicates the hardscape in the drawing and returns the copy. |

*Identity*

| Method | Description |
|---|---|
| `GetID() -> str \| None` | Returns the ID. |
| `SetID(value: str) -> bool` | Sets the ID. |
| `Get3DMode() -> HardscapeObject.Mode3D \| None` | Returns the 3D mode. |
| `Set3DMode(value: HardscapeObject.Mode3D) -> bool` | Sets the 3D mode. |
| `GetDraw3D() -> bool \| None` | Whether *Draw 3D* is on. |
| `SetDraw3D(value: bool) -> bool` | Turns *Draw 3D* on or off. |
| `GetIsSiteModifier() -> bool \| None` | Whether *Site Modifier* is on. |
| `SetIsSiteModifier(value: bool) -> bool` | Turns *Site Modifier* on or off. |
| `GetIsPathway() -> bool \| None` | Whether *Pathway* is on. |
| `SetIsPathway(value: bool) -> bool` | Turns *Pathway* on or off. |
| `GetUseBorder() -> bool \| None` | Whether *Use Border* is on. |
| `SetUseBorder(value: bool) -> bool` | Turns *Use Border* on or off. |
| `GetSlabThickness() -> float \| None` | Sizes (world units). |
| `SetSlabThickness(value: float) -> bool` | Sets the slab thickness (Sizes (world units)). |
| `GetBorderThickness() -> float \| None` | Returns the border thickness. |
| `SetBorderThickness(value: float) -> bool` | Sets the border thickness. |
| `GetBorderWidth() -> float \| None` | Returns the border width. |
| `SetBorderWidth(value: float) -> bool` | Sets the border width. |
| `GetPathwayWidth() -> float \| None` | Returns the pathway width (isPathway = `True`). |
| `SetPathwayWidth(value: float) -> bool` | Sets the pathway width. |
| `GetPathwayOffset() -> float \| None` | Returns the pathway offset. |
| `SetPathwayOffset(value: float) -> bool` | Sets the pathway offset. |
| `GetMainArea() -> float \| None` | Measurements (read-only, computed at reset). |
| `GetBorderArea() -> float \| None` | Returns the border area. |
| `GetFootprintArea() -> float \| None` | Returns the footprint area. |
| `GetPerimeter() -> float \| None` | Returns the perimeter. |
| `GetMainPerimeter() -> float \| None` | Returns the main perimeter. |
| `GetBorderPerimeter() -> float \| None` | Returns the border perimeter. |

Inherited: everything from [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### HardscapeObject.Mode3D

> **Full name:** `api.HardscapeObject.Mode3D` · **Kind:** `IntEnum`

3D mode of the hardscape. Existing enumeration values are API values, not native popup codes. Setter also synchronizes New Mode 3D / Use Site Modifier and, for modifier modes, Config on current objects so the native reset preserves the requested mode.

| Member | Value | Description |
|---|---|---|
| `None_` | `0` |  |
| `Slab` | `1` |  |
| `PadUnder` | `2` |  |
| `PadOver` | `3` |  |
| `TextureBed` | `4` |  |
| `SlabDrainage` | `5` |  |
| `AlignedSlab` | `6` |  |
| `AlignedModifOver` | `7` |  |
| `AlignedModifUnder` | `8` |  |

### PropertyLineObject

> **Full name:** `api.PropertyLineObject` · **Inherits:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Property line plug-in object (universal name "Property Line") from the Landmark plug-in.

A property line represents a legal parcel boundary as a closed 2D path. It labels each segment with its bearing/distance and computes the parcel area and perimeter in configurable units.

Common parameters exposed as named accessors:

- "Name" — user-facing name of the parcel
- "Number" — lot number
- "Area" — computed area (read-only, formatted)
- "Perimeter" — computed perimeter (read-only, formatted)
- "Show Name" — show the name on the parcel
- "Show Number" — show the number on the parcel
- "Show Area" — show the computed area
- "Area Units Imperial" — area units used when the document is in imperial units
- "Area Units Metric" — area units used when the document is in metric units
- "Annotation Units" — units for segment distance labels (Get/SetDistanceUnits)

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Identity

- "Name" — string
- "Number" — string

Measurements (read-only, formatted)

- "Area" — string
- "Perimeter" — string

Toggles

- "Show Name" — bool
- "Show Number" — bool
- "Show Area" — bool
- "Reverse Direction" — bool
- "Fill Behind Text" — bool
- "FillBehindSegText" — bool
- "Tag Show Unit" — bool
- "Seg Show Unit" — bool
- "Annotate Segments" — bool
- "Draw 3D" — bool

Units and formatting

- "Area Units Metric" — popup — Document Units / Square Feet / Square Yards / Square Miles / Acres / Square Meters / Square Kilometers / Hectares
- "Area Units Imperial" — popup — (same choices as Area Units Metric)
- "Annotation Units" — popup — Document Units / Feet & Inches / Inches / Feet / Yards / Miles / Microns / Millimeters / Centimeters / Meters / Kilometers
- "Decimals" — int
- "SegDecimals" — int
- "Text Rotation" — real — degrees

Segment / corner display

- "Annotation Style" — popup — Angle, Distance, Curve / Angle, Distance / Distance Only
- "Angle Format" — radio — Azimuth / Bearing
- "Corner Indicator" — popup — None / Triangle / Filled Triangle / Circle / Dot / Cross / Circle Cross / Tick Mark
- "Corner Indicator Size" — real — world units
- "Report Distance" — popup — On Segment (Outside) / On Segment (Inside) / No
- "Report Angle" — popup — On Segment (Outside) / On Segment (Inside) / Bearing at Corner (Outside) / Bearing at Corner (Inside) / Interior at Corner (Outside) / Interior at Corner (Inside) / No
- "Report Curve" — popup — Yes as Table / Yes as Segment Label / No

Site modifier interaction

- "Site Modifier" — popup — None / Grade Limits / Texture Bed
- "Texture Bed Class" — popup — class name

Text style overrides (per label)

- "Name Text Style" — popup — Un-Styled / Class Text Style
- "Number Text Style" — popup — Un-Styled / Class Text Style
- "Area Text Style" — popup — Un-Styled / Class Text Style
- "Annot Text Style" — popup — Un-Styled / Class Text Style

Internal state

- "__IsNew" — bool
- "__Simple_Dialog" — bool
- "startCurveIDsAt", "numberOfCurves" — int
- "ControlPoint01X..ControlPoint02Y" — real (world coordinates)
- "ResetCurveDataWS" — bool

**Constructors**

| Constructor | Description |
|---|---|
| `PropertyLineObject(h: Handle)` | Refers to the existing property line `h`; check `IsValid()` before use. |

**Methods**

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `CreateFromPath(hPath: Handle) -> PropertyLineObject` *static* | Creates a property line from an existing 2D path object (a closed polygon or polyline). |
| `Duplicate() -> PropertyLineObject` | Duplicates the property line in the drawing and returns the copy. |
| `GetName() -> str \| None` | Returns the name. |
| `SetName(value: str) -> bool` | Sets the name. |
| `GetNumber() -> str \| None` | Returns the number. |
| `SetNumber(value: str) -> bool` | Sets the number. |
| `GetAreaText() -> str \| None` | Formatted, read-only measurements. Use `PrimitiveObject.GetArea` / GetPerimeter for the geometric values in world units. |
| `GetPerimeterText() -> str \| None` | Returns the perimeter text. |
| `GetShowName() -> bool \| None` | Whether *Show Name* is on. |
| `SetShowName(value: bool) -> bool` | Turns *Show Name* on or off. |
| `GetShowNumber() -> bool \| None` | Whether *Show Number* is on. |
| `SetShowNumber(value: bool) -> bool` | Turns *Show Number* on or off. |
| `GetShowArea() -> bool \| None` | Whether *Show Area* is on. |
| `SetShowArea(value: bool) -> bool` | Turns *Show Area* on or off. |
| `GetAreaUnitsImperial() -> PropertyLineObject.AreaUnits \| None` | Returns the area units imperial. |
| `SetAreaUnitsImperial(value: PropertyLineObject.AreaUnits) -> bool` | Sets the area units imperial. |
| `GetAreaUnitsMetric() -> PropertyLineObject.AreaUnits \| None` | Returns the area units metric. |
| `SetAreaUnitsMetric(value: PropertyLineObject.AreaUnits) -> bool` | Sets the area units metric. |
| `GetDistanceUnits() -> str \| None` | Raw distance unit string (see the plug-in for the full list, e.g. "Feet", "Meters", ...). |
| `SetDistanceUnits(value: str) -> bool` | Sets the distance units. Raw distance unit string (see the plug-in for the full list, e.g. "Feet", "Meters", ...). |

Inherited: everything from [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### PropertyLineObject.AreaUnits

> **Full name:** `api.PropertyLineObject.AreaUnits` · **Kind:** `IntEnum`

Area unit choices supported by both "Area Units Imperial" and "Area Units Metric" parameters.

| Member | Value | Description |
|---|---|---|
| `DocumentUnits` | `0` |  |
| `SquareFeet` | `1` |  |
| `SquareYards` | `2` |  |
| `SquareMiles` | `3` |  |
| `Acres` | `4` |  |
| `SquareMeters` | `5` |  |
| `SquareKilometers` | `6` |  |
| `Hectares` | `7` |  |

### ExistingTreeObject

> **Full name:** `api.ExistingTreeObject` · **Inherits:** [`LandmarkObject`](#landmarkobject) → [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject) → `api.Object`

Existing tree plug-in object (universal name "Existing Tree") from the Landmark plug-in.

An existing tree represents a single tree already present on site. It carries species information, size (height, canopy diameter, caliper), root zone data (root ball, critical / primary root zones, tree protection zone), and arborist-style condition / significance / SULE / action assessment.

Common parameters exposed as named accessors:

- "Genus Species" — botanical (Latin) name
- "Common Name" — common name
- "Tree No" — tag / instance identifier
- "Origin" — Not Set / Endemic / Native / Exotic / Indigenous / Custom
- "Height" — overall tree height (world units)
- "Canopy" — canopy diameter (world units)
- "Calliper" — trunk diameter at breast height (DBH), in world units
- "RootBall" — root ball diameter (world units)
- "CriticalRootZone" — critical root zone diameter (world units)
- "PrimaryRootZone" — primary root zone diameter (world units)
- "DisplayTPZ" — None / Circular Zone / Using 12*DBH
- "Condition" — Not Set / Excellent / Good / Average / Poor / Custom
- "SULE" — Safe Useful Life Expectancy category
- "Significance" — importance category
- "ActionComment" — recommended action (Retain / Remove / Transplant / ...)
- "Location" — free-form location description
- "Comments" — free-form notes
- "Create3D" — generate 3D geometry

Full parameter reference for GetParam.../SetParam... (parameter name | type | notes/choices) Species / identity

- "Genus Species" — string — botanical name (genus + species)
- "Common Name" — string
- "Family" — string
- "Tree No" — string — tag / instance identifier
- "Origin" — popup — Not Set / Endemic / Native / Exotic / Indigenous / Custom
- "CustomOrigin" — string — free-form Origin value when Origin = "Custom"
- "Invasive" — bool
- "InvasiveSpecies" — bool — (2026+ replacement of "Invasive")
- "Elevation" — real — world units

Size (world units)

- "Height" — real — overall tree height
- "Canopy" — real — canopy diameter (used when UseCanopyMin = `False`)
- "UseCanopyMin" — bool — use CanopyMin for min radius
- "CanopyMin" — real — minimum canopy diameter (irregular canopies)
- "CanopyRotate" — real — degrees - rotation of the canopy
- "CanopyArea" — real (read-only, computed)
- "Hgt First Branch" — real — world units
- "CrownClearance" — real
- "FirstBranchDir" — popup
- "AddIntercardinalDir" — bool — include NE/SE/SW/NW canopy radii
- "Calliper" — real — DBH (diameter at breast height)

Root zones and Tree Protection Zone (TPZ), world units

- "RootBall" — real — root ball diameter
- "CriticalRootZone" — real — Critical Root Zone (CRZ) diameter
- "PrimaryRootZone" — real — Primary Root Zone (PRZ) diameter
- "RootZones" — popup — None / Critical Zone / Primary Zone / Both Zones / Root Ball
- "EditTPZ" — bool
- "DisplayTPZ" — popup — None / Display Circular Zone / Display Using 12 x DBH
- "TPZCornerRadius" — real
- "TPZRadius" — real
- "TPZArea", "AdjustedTPZArea" — real (read-only)
- "MinSRZRadius" — real
- "DiamAtButtress" — real
- "StructuralRootZone" — bool
- "CalculatedSRZ" — string (read-only, formatted)

Arborist assessment

- "Condition" — popup — Not Set / Excellent / Good / Average / Poor / Custom
- "CustomCondition" — string — free-form Condition value when Condition = "Custom"
- "SULE" — popup — Not Set / "Long (40+ yrs)" / "Medium (16-39 yrs)" / "Short (5-15 yrs)" / Removal / Custom
- "CustomSULE" — string
- "Significance" — popup — Not Set / Most Significant / Highly Significant / Less Significant / Least Significant / Hazardous / Custom
- "CustomSignificance" — string
- "ActionComment" — popup — Not Set / Retain / "Retain - Arborist Work Required" / "Transplant - Original Location" / "Transplant - Proposed Location" / Remove / "Remove - Within Building Footprint" / "Remove - Poor Health" / "Remove - Undesirable Species" / Custom
- "CustomAction" — string
- "TreeProtectionOrder" — bool
- "VeteranTree" — bool
- "AncientTree" — bool
- "Form" — popup — Not Set / Excellent / Good / Average / Poor
- "Structure" — popup — Not Set / Excellent / Good / Average / Poor
- "Vigour" — popup — Not Set / Excellent / Good / Average / Poor

Additional data

- "RL" — string — reduced level (elevation reference)
- "Age" — string
- "Year Planted" — string
- "DateAssessed" — string
- "Location" — string
- "Comments" — string — free-form notes
- "Field1..Field10" — string — user-defined additional fields
- "sustainability" — string — JSON blob (VW2026+)
- "VersionInfo" — string (read-only)

Multi-stem trees

- "__UseMultipleStems" — bool
- "__NumStems" — int
- "__Stem1..__Stem10" — real — diameter of each stem, in world units
- "__TrunkPerim" — real — trunk perimeter / circumference

Irregular canopy (per-direction radii, world units)

- "__CustomCanopy" — bool
- "__CanopyNorth", "__CanopySouth", "__CanopyEast", "__CanopyWest" — real
- "__CanopyNorthEast", "__CanopySouthEast", "__CanopySouthWest", "__CanopyNorthWest" — real

3D geometry

- "Create 3D" — bool
- "UseGenerated3DGeometry" — bool
- "UseLaubwerk3DGeometry" — bool
- "UseImageProp3DGeometry" — bool
- "ImagePropSymbol" — string — symbol name for the image prop
- "__CanopySymbolName", "__TrunkSymbolName", "__RetainSymbolName", "__RemoveSymbolName", "__TransOldSymbolName", "__TransNewSymbolName", "__CustActionSymbolName", "__TransTrunkSymName" — string (symbol resource names)
- "__UseSymComponents" — bool
- "__ApplyClassTextures" — bool
- "UseXForRemoveTrees" — bool — draw an X marker for trees marked for removal
- "lw_Key", "lw_PlantFile", "lw_Variant" — string — (Laubwerk 3D species selection)
- "lw_GlobalSeason" — bool
- "lw_Season" — string
- "lw_Global2D3DMat" — bool
- "lw_2DReprs", "lw_3DReprs" — string
- "lw_MaterialStyle" — string

Tag / label

- "UseTag" — bool
- "__SnapTagToTrunk" — bool
- "__DisplayTagMarker" — bool
- "__EnableTagShoulder" — bool
- "__TagShoulderAngle" — real — degrees
- "__TagShoulderLength" — real — world units
- "__TagDisplayType" — int
- "__IDClass" — popup — class name
- "__FlagNumberDLog", "__FlagNumberDLogFEO" — bool
- "ControlPoint01X..ControlPoint08Y" — real (world coordinates for the various control points)

Attribute overrides (colour / class / line-weight per zone) "__TPZClass", "__RootClass", "__TrunkClass", "__CanopyClass", "__SigClass"		popup (class name) "__TPZLineWeight", "__TPZLineStyle", "__TPZLineCol"		int "__PRZLineWeight", "__PRZLineStyle", "__PRZLineCol"		int "__CRZLineWeight", "__CRZLineStyle", "__CRZLineCol"		int

- "__UseSigColours" — bool
- "__Sig1FillCol..__Sig5FillCol" — int — colour indices
- "__SigColDisplay" — int
- "__TrunkType" — int

Auto-numbering

- "__AutoNumberDefault" — bool
- "__AutoNumCurrent" — int
- "__AutoNumPrefix", "__AutoNumSuffix" — string
- "__AutoNumZeroDefault" — int
- "__AutoNumberDups" — bool
- "__AutoNumSepLayers" — bool
- "__AutoNumThisTree" — bool
- "__IsAppliedAsTheDocDef" — bool
- "__IsNewDocument" — bool

Internal / versioning

- "__UniqueID" — string
- "__LayerName" — string
- "__LineTypes" — string
- "__ETShape", "__ETShapeNum" — int
- "__CustomFieldNum" — int
- "__CustomLabels" — string

**Constructors**

| Constructor | Description |
|---|---|
| `ExistingTreeObject(h: Handle)` | Refers to the existing tree `h`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `Create(position: Math.Point2D) -> ExistingTreeObject` *static* | Creates an existing tree at `position` in the active layer / current container. |
| `Duplicate() -> ExistingTreeObject` | Duplicates the existing tree in the drawing and returns the copy. |

*Species / identity*

| Method | Description |
|---|---|
| `GetBotanicalName() -> str \| None` | Returns the botanical name. |
| `SetBotanicalName(value: str) -> bool` | Sets the botanical name. |
| `GetCommonName() -> str \| None` | Returns the common name. |
| `SetCommonName(value: str) -> bool` | Sets the common name. |
| `GetTreeNumber() -> str \| None` | Returns the tree number (tag / instance identifier). |
| `SetTreeNumber(value: str) -> bool` | Sets the tree number. |
| `GetOrigin() -> ExistingTreeObject.Origin \| None` | Returns the origin. |
| `SetOrigin(value: ExistingTreeObject.Origin) -> bool` | Sets the origin. |
| `GetHeight() -> float \| None` | Size (world units) (overall height). |
| `SetHeight(value: float) -> bool` | Sets the height (Size (world units)). |
| `GetCanopyDiameter() -> float \| None` | Returns the canopy diameter. |
| `SetCanopyDiameter(value: float) -> bool` | Sets the canopy diameter. |
| `GetCaliper() -> float \| None` | Returns the caliper (DBH: diameter at breast height). |
| `SetCaliper(value: float) -> bool` | Sets the caliper. |
| `GetRootBallDiameter() -> float \| None` | Root zones (world units). |
| `SetRootBallDiameter(value: float) -> bool` | Sets the root ball diameter (Root zones (world units)). |
| `GetCriticalRootZoneDiameter() -> float \| None` | Returns the critical root zone diameter. |
| `SetCriticalRootZoneDiameter(value: float) -> bool` | Sets the critical root zone diameter. |
| `GetPrimaryRootZoneDiameter() -> float \| None` | Returns the primary root zone diameter. |
| `SetPrimaryRootZoneDiameter(value: float) -> bool` | Sets the primary root zone diameter. |
| `GetTreeProtectionZone() -> ExistingTreeObject.TreeProtection \| None` | Returns the tree protection zone. |
| `SetTreeProtectionZone(value: ExistingTreeObject.TreeProtection) -> bool` | Sets the tree protection zone. |
| `GetCondition() -> ExistingTreeObject.Condition \| None` | Returns the condition. |
| `SetCondition(value: ExistingTreeObject.Condition) -> bool` | Sets the condition. |
| `GetSULE() -> ExistingTreeObject.SULE \| None` | Returns the SULE. |
| `SetSULE(value: ExistingTreeObject.SULE) -> bool` | Sets the SULE. |
| `GetSignificance() -> ExistingTreeObject.Significance \| None` | Returns the significance. |
| `SetSignificance(value: ExistingTreeObject.Significance) -> bool` | Sets the significance. |
| `GetActionComment() -> ExistingTreeObject.Action \| None` | Returns the action comment. |
| `SetActionComment(value: ExistingTreeObject.Action) -> bool` | Sets the action comment. |
| `GetLocation() -> str \| None` | Returns the location (free-form location description). |
| `SetLocation(value: str) -> bool` | Sets the location. |
| `GetNotes() -> str \| None` | Returns the notes. |
| `SetNotes(value: str) -> bool` | Sets the notes. |
| `GetCreate3D() -> bool \| None` | Whether *Create 3D* is on. |
| `SetCreate3D(value: bool) -> bool` | Turns *Create 3D* on or off. |

Inherited: everything from [`LandmarkObject`](#landmarkobject), [`PrimitiveObject`](ObjectPrimitives.md#primitiveobject).

#### ExistingTreeObject.Origin

> **Full name:** `api.ExistingTreeObject.Origin` · **Kind:** `IntEnum`

Origin of an existing tree species.

| Member | Value | Description |
|---|---|---|
| `NotSet` | `0` |  |
| `Endemic` | `1` |  |
| `Native` | `2` |  |
| `Exotic` | `3` |  |
| `Indigenous` | `4` |  |
| `Custom` | `5` |  |

#### ExistingTreeObject.TreeProtection

> **Full name:** `api.ExistingTreeObject.TreeProtection` · **Kind:** `IntEnum`

Tree Protection Zone display

| Member | Value | Description |
|---|---|---|
| `None_` | `0` |  |
| `CircularZone` | `1` |  |
| `Using12DBH` | `2` |  |

#### ExistingTreeObject.Condition

> **Full name:** `api.ExistingTreeObject.Condition` · **Kind:** `IntEnum`

Arborist assessment

| Member | Value | Description |
|---|---|---|
| `NotSet` | `0` |  |
| `Excellent` | `1` |  |
| `Good` | `2` |  |
| `Average` | `3` |  |
| `Poor` | `4` |  |
| `Custom` | `5` |  |

#### ExistingTreeObject.SULE

> **Full name:** `api.ExistingTreeObject.SULE` · **Kind:** `IntEnum`

Safe Useful Life Expectancy

| Member | Value | Description |
|---|---|---|
| `NotSet` | `0` |  |
| `Long` | `1` |  |
| `Medium` | `2` |  |
| `Short` | `3` |  |
| `Removal` | `4` |  |
| `Custom` | `5` |  |

#### ExistingTreeObject.Significance

> **Full name:** `api.ExistingTreeObject.Significance` · **Kind:** `IntEnum`

Significance rating of an existing tree.

| Member | Value | Description |
|---|---|---|
| `NotSet` | `0` |  |
| `MostSignificant` | `1` |  |
| `HighlySignificant` | `2` |  |
| `LessSignificant` | `3` |  |
| `LeastSignificant` | `4` |  |
| `Hazardous` | `5` |  |
| `Custom` | `6` |  |

#### ExistingTreeObject.Action

> **Full name:** `api.ExistingTreeObject.Action` · **Kind:** `IntEnum`

Proposed action for an existing tree.

| Member | Value | Description |
|---|---|---|
| `NotSet` | `0` |  |
| `Retain` | `1` |  |
| `RetainArborist` | `2` |  |
| `TransplantOriginal` | `3` |  |
| `TransplantProposed` | `4` |  |
| `Remove` | `5` |  |
| `RemoveBuildingFootprint` | `6` |  |
| `RemovePoorHealth` | `7` |  |
| `RemoveSpecies` | `8` |  |
| `Custom` | `9` |  |

---

[Back to the index](README.md) · [Back to top](#objectslandmark--plants-site-models-hardscapes-and-other-landscape-objects)
