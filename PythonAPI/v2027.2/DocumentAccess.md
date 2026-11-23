**English** • [Deutsch](../../PythonAPI.de/v2027.2/DocumentAccess.md) • [日本語](../../PythonAPI.ja/v2027.2/DocumentAccess.md)

# DocumentAccess — document, layers, stories and preferences

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

`api.Document` is the entry point of the API: a stateless facade over the active drawing. Construct it on demand with `api.Document()` and use it to reach the selection, layers, stories, classes, objects, the view, units, undo and the typed preference views (`DisplaySettings`, `EditingSettings`, `SnapSettings`, `GridSettings`, `StackLayersSettings`, `UnitSettings`, `TextDefaults`, `DefaultAttributes`, `ProgramVariables`).

Vectorworks vocabulary used below: a **layer** is a design layer (a world coordinate plane at a given scale) or a sheet layer (a printable page); a **story** is a floor of the building at an elevation that groups the design layers of its levels; a **level type** is the name of a story level (for example "Slab"); a **class** is a named style container whose "by class" attributes objects inherit; a **container** is anything that holds objects (a layer, a group, a symbol definition, a viewport).

Shared conventions: getters return `None` when a value cannot be obtained, setters and actions return `False` on failure; lengths and coordinates are world units, angles radians (counter-clockwise), strings UTF-8. Object handles are `api.Handle` (`vs.Handle`) objects; pass `None` for a null handle. Use `Document.As(type, h)` to get a typed object of a handle.

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [TextStyleData](#textstyledata)
  - [ProgramVariables](#programvariables)
  - [DisplaySettings](#displaysettings)
  - [EditingSettings](#editingsettings)
  - [SnapSettings](#snapsettings)
  - [GridSettings](#gridsettings)
  - [StackLayersSettings](#stacklayerssettings)
  - [UnitSettings](#unitsettings)
  - [TextDefaults](#textdefaults)
  - [DefaultAttributes](#defaultattributes)
  - [LayerContents](#layercontents)
  - [Layer](#layer)
  - [StoryLevel](#storylevel)
  - [StoryLevelTemplate](#storyleveltemplate)
  - [Story](#story)
  - [Document](#document)
- [Enumerations](#enumerations)
  - [Traverse](#traverse)
  - [Descend](#descend)
  - [LayerType](#layertype)
  - [LayerVisibility](#layervisibility)
  - [VisibilityOptions](#visibilityoptions)
  - [StoryElevationChangeMode](#storyelevationchangemode)
  - [UndoMethod](#undomethod)
  - [AngularUnit](#angularunit)
  - [TextJustification](#textjustification)
  - [TextVerticalAlignment](#textverticalalignment)
  - [TextLineSpacing](#textlinespacing)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`TextStyleData`](#textstyledata) | class |  | Text style flags of a text (bold, italic, underline, outline, shadow), as used by `TextDefaults.GetStyle` / `SetStyle`. |
| [`ProgramVariables`](#programvariables) | class |  | Low-level, typed access to any Vectorworks program variable (application-wide or per-document preference) by numeric selector. |
| [`DisplaySettings`](#displaysettings) | class |  | Display preferences. |
| [`EditingSettings`](#editingsettings) | class |  | Editing and session preferences. |
| [`SnapSettings`](#snapsettings) | class |  | Snapping (SmartCursor) preferences. |
| [`GridSettings`](#gridsettings) | class |  | Grid preferences. |
| [`StackLayersSettings`](#stacklayerssettings) | class |  | Unified view (stack layers) preferences. |
| [`UnitSettings`](#unitsettings) | class |  | Primary or secondary dimension units of the active document. |
| [`TextDefaults`](#textdefaults) | class |  | Default text settings for new text objects. |
| [`DefaultAttributes`](#defaultattributes) | class |  | Default attributes for new objects (the Attributes palette with nothing selected). |
| [`LayerContents`](#layercontents) | class |  | Object count and bounds of the top level objects of a layer. |
| [`Layer`](#layer) | class |  | A layer (design or sheet layer). |
| [`StoryLevel`](#storylevel) | class |  | One level of a story: a named height (its level type) relative to the story elevation, optionally with the design layer of that level. |
| [`StoryLevelTemplate`](#storyleveltemplate) | class |  | A default story level (Organization dialog box > Stories tab > Default Story Levels): a template for story levels. |
| [`Story`](#story) | class |  | A story: a floor of the building at an elevation. |
| [`Document`](#document) | class |  | Stateless facade over the active Vectorworks document. |
| [`Traverse`](#traverse) | IntEnum |  | Which set of objects a document traversal visits. |
| [`Descend`](#descend) | IntFlag |  | How deep a traversal descends into container objects (groups, symbols, viewports, ...). |
| [`LayerType`](#layertype) | IntEnum |  | Kind of a layer. |
| [`LayerVisibility`](#layervisibility) | IntEnum |  | Visibility of a layer (as shown in the Navigation palette). |
| [`VisibilityOptions`](#visibilityoptions) | IntEnum |  | How layers or classes other than the active one are shown. |
| [`StoryElevationChangeMode`](#storyelevationchangemode) | IntEnum |  | Which stories `Story.SetElevation` moves (the choices of the Change Story Elevation dialog box). |
| [`UndoMethod`](#undomethod) | IntEnum |  | Undo method passed to `Document.StartUndoEvent`. |
| [`AngularUnit`](#angularunit) | IntEnum |  | Unit in which angles are displayed (`UnitSettings.GetAngularUnit`). |
| [`TextJustification`](#textjustification) | IntEnum |  | Horizontal justification of new text (`TextDefaults`). |
| [`TextVerticalAlignment`](#textverticalalignment) | IntEnum |  | Vertical alignment of new text (`TextDefaults`). |
| [`TextLineSpacing`](#textlinespacing) | IntEnum |  | Line spacing of new text (`TextDefaults`); `Custom` uses the leading of `TextDefaults.GetLeading`. |

## Classes

### TextStyleData

> **Full name:** `api.TextStyleData` · **Inherits:** `api.Object`

Text style flags of a text (bold, italic, underline, outline, shadow), as used by `TextDefaults.GetStyle` / `SetStyle`. Convert to and from the Vectorworks style bit set with `ToBits` / `FromBits`.

**Constructors**

| Constructor | Description |
|---|---|
| `TextStyleData()` | Default value (fields at their defaults). |
| `TextStyleData(bold, italic, underline, outline, shadow)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Methods**

| Method | Description |
|---|---|
| `ToBits() -> int` | Packs the five style flags into the Vectorworks style bit set (bold 1, italic 2, underline 4, outline 8, shadow 16). |
| `FromBits(bits: int) -> TextStyleData` *static* | Creates a TextStyleData from a Vectorworks style bit set (bold 1, italic 2, underline 4, outline 8, shadow 16). |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: TextStyleData) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: TextStyleData) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `bold` | `bool` | Bold. |
| `italic` | `bool` | Italic. |
| `underline` | `bool` | Underline. |
| `outline` | `bool` | Outline. |
| `shadow` | `bool` | Shadow. |

### ProgramVariables

> **Full name:** `api.ProgramVariables` · **Inherits:** `api.Object`

Low-level, typed access to any Vectorworks program variable (application-wide or per-document preference) by numeric selector. Most preferences are more conveniently accessed through the typed settings classes (`DisplaySettings`, `EditingSettings`, `SnapSettings`, `GridSettings`, `StackLayersSettings`, `UnitSettings` and `TextDefaults`); use this class only for preferences that do not have a named accessor. Every selector has a value type; use the accessor that matches it:

| Accessor | Value type of the selector |
|---|---|
| `GetBool` / `SetBool` | Boolean (`bool`) |
| `GetUInt8` / `SetUInt8` | Unsigned 8-bit integer (0 to 255) |
| `GetInt8` / `SetInt8` | Signed 8-bit integer (-128 to 127) |
| `GetInt16` / `SetInt16` | 16-bit integer |
| `GetInt32` / `SetInt32` | 32-bit integer |
| `GetDouble` / `SetDouble` | Real number (`float`): lengths, angles and other real values |
| `GetString` / `SetString` | Text (`str`) |

**Constructors**

| Constructor | Description |
|---|---|
| `ProgramVariables()` | Stateless object; every method is static and can be called on the class itself. |

**Methods**

| Method | Description |
|---|---|
| `GetBool(selector: int) -> bool \| None` *static* | Value of the Boolean program variable `selector`. |
| `SetBool(selector: int, value: bool) -> bool` *static* | Sets the Boolean program variable `selector`. |
| `GetUInt8(selector: int) -> int \| None` *static* | Value of the unsigned 8-bit program variable `selector`. |
| `SetUInt8(selector: int, value: int) -> bool` *static* | Sets the unsigned 8-bit program variable `selector`. |
| `GetInt8(selector: int) -> int \| None` *static* | Value of the signed 8-bit program variable `selector`. |
| `SetInt8(selector: int, value: int) -> bool` *static* | Sets the signed 8-bit program variable `selector`. |
| `GetInt16(selector: int) -> int \| None` *static* | Value of the 16-bit program variable `selector`. |
| `SetInt16(selector: int, value: int) -> bool` *static* | Sets the 16-bit program variable `selector`. |
| `GetInt32(selector: int) -> int \| None` *static* | Value of the 32-bit program variable `selector`. |
| `SetInt32(selector: int, value: int) -> bool` *static* | Sets the 32-bit program variable `selector`. |
| `GetDouble(selector: int) -> float \| None` *static* | Value of the real number program variable `selector`. |
| `SetDouble(selector: int, value: float) -> bool` *static* | Sets the real number program variable `selector`. |
| `GetString(selector: int) -> str \| None` *static* | Value of the text program variable `selector`. |
| `SetString(selector: int, value: str) -> bool` *static* | Sets the text program variable `selector`. |

### DisplaySettings

> **Full name:** `api.DisplaySettings` · **Inherits:** `api.Object`

Display preferences.

**Constructors**

| Constructor | Description |
|---|---|
| `DisplaySettings()` | Stateless view of the display preferences of the active document. |

**Methods**

| Method | Description |
|---|---|
| `GetBlackAndWhiteOnly() -> bool \| None` | Whether *Black And White Only* is on. |
| `SetBlackAndWhiteOnly(value: bool) -> bool` | Turns *Black And White Only* on or off. |
| `GetUseLayerColors() -> bool \| None` | Whether *Use Layer Colors* is on. |
| `SetUseLayerColors(value: bool) -> bool` | Turns *Use Layer Colors* on or off. |
| `GetZoomLineThickness() -> bool \| None` | Whether *Zoom Line Thickness* is on. |
| `SetZoomLineThickness(value: bool) -> bool` | Turns *Zoom Line Thickness* on or off. |
| `GetBlackBackground() -> bool \| None` | Whether *Black Background* is on. |
| `SetBlackBackground(value: bool) -> bool` | Turns *Black Background* on or off. |
| `GetShowRulers() -> bool \| None` | Whether *Show Rulers* is on. |
| `SetShowRulers(value: bool) -> bool` | Turns *Show Rulers* on or off. |
| `GetShowScrollBars() -> bool \| None` | Whether *Show Scroll Bars* is on. |
| `SetShowScrollBars(value: bool) -> bool` | Turns *Show Scroll Bars* on or off. |
| `GetShowPageBoundary() -> bool \| None` | Whether *Show Page Boundary* is on. |
| `SetShowPageBoundary(value: bool) -> bool` | Turns *Show Page Boundary* on or off. |
| `GetShowPageBreaks() -> bool \| None` | Whether *Show Page Breaks* is on. |
| `SetShowPageBreaks(value: bool) -> bool` | Turns *Show Page Breaks* on or off. |
| `GetShowOthersInGroup() -> bool \| None` | Whether *Show Others In Group* is on. |
| `SetShowOthersInGroup(value: bool) -> bool` | Turns *Show Others In Group* on or off. |
| `GetShowOthersInGroupGrayed() -> bool \| None` | Whether *Show Others In Group Grayed* is on. |
| `SetShowOthersInGroupGrayed(value: bool) -> bool` | Turns *Show Others In Group Grayed* on or off. |
| `GetEightSelectionHandles() -> bool \| None` | Whether *Eight Selection Handles* is on. |
| `SetEightSelectionHandles(value: bool) -> bool` | Turns *Eight Selection Handles* on or off. |
| `GetFullScreenCursor() -> bool \| None` | Whether *Full Screen Cursor* is on. |
| `SetFullScreenCursor(value: bool) -> bool` | Turns *Full Screen Cursor* on or off. |
| `GetNoFillBehindText() -> bool \| None` | Whether *No Fill Behind Text* is on. |
| `SetNoFillBehindText(value: bool) -> bool` | Turns *No Fill Behind Text* on or off. |
| `GetAdjustFlippedText() -> bool \| None` | Whether *Adjust Flipped Text* is on. |
| `SetAdjustFlippedText(value: bool) -> bool` | Turns *Adjust Flipped Text* on or off. |
| `GetXRayMode() -> bool \| None` | Whether *X-ray Mode* is on. |
| `SetXRayMode(value: bool) -> bool` | Turns *X-ray Mode* on or off. |
| `GetDisplayHiddenObjectsGhosted() -> bool \| None` | Whether *Display Hidden Objects Ghosted* is on. |
| `SetDisplayHiddenObjectsGhosted(value: bool) -> bool` | Turns *Display Hidden Objects Ghosted* on or off. |
| `GetShowInternalOriginMarker() -> bool \| None` | Whether *Show Internal Origin Marker* is on. |
| `SetShowInternalOriginMarker(value: bool) -> bool` | Turns *Show Internal Origin Marker* on or off. |
| `GetAllowDropShadows() -> bool \| None` | Whether *Allow Drop Shadows* is on. |
| `SetAllowDropShadows(value: bool) -> bool` | Turns *Allow Drop Shadows* on or off. |
| `GetPerspectiveCropped() -> bool \| None` | Whether *Perspective Cropped* is on. |
| `SetPerspectiveCropped(value: bool) -> bool` | Turns *Perspective Cropped* on or off. |
| `Get2DConversionResolution() -> int \| None` | Raw values of the corresponding preference popups. |
| `Set2DConversionResolution(value: int) -> bool` | Sets the 2D conversion resolution. Raw values of the corresponding preference popups. |
| `Get3DConversionResolution() -> int \| None` | Returns the 3D conversion resolution. |
| `Set3DConversionResolution(value: int) -> bool` | Sets the 3D conversion resolution. |
| `GetDisplayLightObjects() -> int \| None` | Returns the display light objects. |
| `SetDisplayLightObjects(value: int) -> bool` | Sets the display light objects. |
| `GetRotatedTextDisplay() -> int \| None` | Returns the rotated text display. |
| `SetRotatedTextDisplay(value: int) -> bool` | Sets the rotated text display. |
| `GetDisplayBitmaps() -> int \| None` | Returns the display bitmaps. |
| `SetDisplayBitmaps(value: int) -> bool` | Sets the display bitmaps. |
| `GetHiddenLineShade() -> int \| None` | Returns the hidden line shade. |
| `SetHiddenLineShade(value: int) -> bool` | Sets the hidden line shade. |
| `GetDisplay3DLoci() -> int \| None` | Returns the display 3D loci. |
| `SetDisplay3DLoci(value: int) -> bool` | Sets the display 3D loci. |
| `GetDefaultRenderMode() -> int \| None` | Returns the default render mode. |
| `SetDefaultRenderMode(value: int) -> bool` | Sets the default render mode. |
| `GetDefaultProjection() -> int \| None` | Returns the default projection. |
| `SetDefaultProjection(value: int) -> bool` | Sets the default projection. |
| `Get3DRotationResponse() -> int \| None` | Returns the 3D rotation response (1..5). |
| `Set3DRotationResponse(value: int) -> bool` | Sets the 3D rotation response. |

### EditingSettings

> **Full name:** `api.EditingSettings` · **Inherits:** `api.Object`

Editing and session preferences.

**Constructors**

| Constructor | Description |
|---|---|
| `EditingSettings()` | Stateless view of the editing and session preferences. |

**Methods**

| Method | Description |
|---|---|
| `GetClickDrag() -> bool \| None` | Whether *Click Drag* is on. |
| `SetClickDrag(value: bool) -> bool` | Turns *Click Drag* on or off. |
| `GetOffsetDuplicates() -> bool \| None` | Whether *Offset Duplicates* is on. |
| `SetOffsetDuplicates(value: bool) -> bool` | Turns *Offset Duplicates* on or off. |
| `GetAssociateDimensions() -> bool \| None` | Whether *Associate Dimensions* is on. |
| `SetAssociateDimensions(value: bool) -> bool` | Turns *Associate Dimensions* on or off. |
| `GetAutoAssociateDimensions() -> bool \| None` | Whether *Auto Associate Dimensions* is on. |
| `SetAutoAssociateDimensions(value: bool) -> bool` | Turns *Auto Associate Dimensions* on or off. |
| `GetCreateDimensionsInDimensionClass() -> bool \| None` | Whether *Create Dimensions In Dimension Class* is on. |
| `SetCreateDimensionsInDimensionClass(value: bool) -> bool` | Turns *Create Dimensions In Dimension Class* on or off. |
| `GetWallAutoJoin() -> bool \| None` | Whether *Wall Auto Join* is on. |
| `SetWallAutoJoin(value: bool) -> bool` | Turns *Wall Auto Join* on or off. |
| `GetUndoViewChanges() -> bool \| None` | Whether *Undo View Changes* is on. |
| `SetUndoViewChanges(value: bool) -> bool` | Turns *Undo View Changes* on or off. |
| `GetDuplicateTagsWithObjects() -> bool \| None` | Whether *Duplicate Tags With Objects* is on. |
| `SetDuplicateTagsWithObjects(value: bool) -> bool` | Turns *Duplicate Tags With Objects* on or off. |
| `GetOccludedPickingAndSnapping() -> bool \| None` | Whether *Occluded Picking And Snapping* is on. |
| `SetOccludedPickingAndSnapping(value: bool) -> bool` | Turns *Occluded Picking And Snapping* on or off. |
| `GetMaxUndos() -> int \| None` | Returns the max undos. |
| `SetMaxUndos(value: int) -> bool` | Sets the max undos. |
| `GetAutoSaveInterval() -> int \| None` | Returns the auto save interval. |
| `SetAutoSaveInterval(value: int) -> bool` | Sets the auto save interval. |
| `GetBackupInterval() -> int \| None` | Returns the backup interval. |
| `SetBackupInterval(value: int) -> bool` | Sets the backup interval. |
| `GetLineWeightUnit() -> int \| None` | Returns the line weight unit. |
| `SetLineWeightUnit(value: int) -> bool` | Sets the line weight unit. |
| `GetDimensionStandard() -> int \| None` | Returns the dimension standard. |
| `SetDimensionStandard(value: int) -> bool` | Sets the dimension standard. |
| `GetCustomMoveDistance() -> float \| None` | Returns the custom move distance. |
| `SetCustomMoveDistance(value: float) -> bool` | Sets the custom move distance. |

### SnapSettings

> **Full name:** `api.SnapSettings` · **Inherits:** `api.Object`

Snapping (SmartCursor) preferences.

**Constructors**

| Constructor | Description |
|---|---|
| `SnapSettings()` | Stateless view of the snapping preferences. |

**Methods**

*General*

| Method | Description |
|---|---|
| `GetSnapToGrid() -> bool \| None` | Whether *Snap To Grid* is on. |
| `SetSnapToGrid(value: bool) -> bool` | Turns *Snap To Grid* on or off. |
| `GetSnapToObjects() -> bool \| None` | Whether *Snap To Objects* is on. |
| `SetSnapToObjects(value: bool) -> bool` | Turns *Snap To Objects* on or off. |
| `GetSnapToLoci() -> bool \| None` | Whether *Snap To Loci* is on. |
| `SetSnapToLoci(value: bool) -> bool` | Turns *Snap To Loci* on or off. |
| `GetSnapToEdgePoints() -> bool \| None` | Whether *Snap To Edge Points* is on. |
| `SetSnapToEdgePoints(value: bool) -> bool` | Turns *Snap To Edge Points* on or off. |
| `GetSnapToSelectionOnly() -> bool \| None` | Whether *Snap To Selection Only* is on. |
| `SetSnapToSelectionOnly(value: bool) -> bool` | Turns *Snap To Selection Only* on or off. |
| `GetSnapToAngle() -> bool \| None` | Whether *Snap To Angle* is on. |
| `SetSnapToAngle(value: bool) -> bool` | Turns *Snap To Angle* on or off. |
| `GetSnapToIntersection() -> bool \| None` | Whether *Snap To Intersection* is on. |
| `SetSnapToIntersection(value: bool) -> bool` | Turns *Snap To Intersection* on or off. |
| `GetSmartPoints() -> bool \| None` | Whether *Smart Points* is on. |
| `SetSmartPoints(value: bool) -> bool` | Turns *Smart Points* on or off. |
| `GetSnapToDistance() -> bool \| None` | Whether *Snap To Distance* is on. |
| `SetSnapToDistance(value: bool) -> bool` | Turns *Snap To Distance* on or off. |
| `GetSmartEdge() -> bool \| None` | Whether *Smart Edge* is on. |
| `SetSmartEdge(value: bool) -> bool` | Turns *Smart Edge* on or off. |
| `GetConstrainTangent() -> bool \| None` | Whether *Constrain Tangent* is on. |
| `SetConstrainTangent(value: bool) -> bool` | Turns *Constrain Tangent* on or off. |
| `GetSnapToEndPoint() -> bool \| None` | Whether *Snap To End Point* is on. |
| `SetSnapToEndPoint(value: bool) -> bool` | Turns *Snap To End Point* on or off. |
| `GetSnapToMidPoint() -> bool \| None` | Whether *Snap To Mid Point* is on. |
| `SetSnapToMidPoint(value: bool) -> bool` | Turns *Snap To Mid Point* on or off. |
| `GetSnapToCenter() -> bool \| None` | Whether *Snap To Center* is on. |
| `SetSnapToCenter(value: bool) -> bool` | Turns *Snap To Center* on or off. |
| `GetSnapToQuadrant() -> bool \| None` | Whether *Snap To Quadrant* is on. |
| `SetSnapToQuadrant(value: bool) -> bool` | Turns *Snap To Quadrant* on or off. |
| `GetSnapToInsertionPoint() -> bool \| None` | Whether *Snap To Insertion Point* is on. |
| `SetSnapToInsertionPoint(value: bool) -> bool` | Turns *Snap To Insertion Point* on or off. |
| `GetSnapToVertex() -> bool \| None` | Whether *Snap To Vertex* is on. |
| `SetSnapToVertex(value: bool) -> bool` | Turns *Snap To Vertex* on or off. |
| `GetSnapToEdge() -> bool \| None` | Whether *Snap To Edge* is on. |
| `SetSnapToEdge(value: bool) -> bool` | Turns *Snap To Edge* on or off. |
| `GetSnapToMasterPoints() -> bool \| None` | Whether *Snap To Master Points* is on. |
| `SetSnapToMasterPoints(value: bool) -> bool` | Turns *Snap To Master Points* on or off. |
| `GetSnapToRelativeAngles() -> bool \| None` | Whether *Snap To Relative Angles* is on. |
| `SetSnapToRelativeAngles(value: bool) -> bool` | Turns *Snap To Relative Angles* on or off. |
| `GetSnapToAlternateCoordinateSystem() -> bool \| None` | Whether *Snap To Alternate Coordinate System* is on. |
| `SetSnapToAlternateCoordinateSystem(value: bool) -> bool` | Turns *Snap To Alternate Coordinate System* on or off. |
| `GetSnapToAnglesFromAxes() -> bool \| None` | Whether *Snap To Angles From Axes* is on (read-only). |
| `GetSnapToCombinedPageArea() -> bool \| None` | Whether *Snap To Combined Page Area* is on. |
| `SetSnapToCombinedPageArea(value: bool) -> bool` | Turns *Snap To Combined Page Area* on or off. |
| `GetSnapToIndividualPages() -> bool \| None` | Whether *Snap To Individual Pages* is on. |
| `SetSnapToIndividualPages(value: bool) -> bool` | Turns *Snap To Individual Pages* on or off. |
| `GetFloatingDatum() -> bool \| None` | Whether *Floating Datum* is on. |
| `SetFloatingDatum(value: bool) -> bool` | Turns *Floating Datum* on or off. |
| `GetShowSnapBox() -> bool \| None` | Whether *Show Snap Box* is on. |
| `SetShowSnapBox(value: bool) -> bool` | Turns *Show Snap Box* on or off. |
| `GetShowSelectionBox() -> bool \| None` | Whether *Show Selection Box* is on. |
| `SetShowSelectionBox(value: bool) -> bool` | Turns *Show Selection Box* on or off. |
| `GetSnapRadiusPixels() -> int \| None` | Returns the snap radius pixels. |
| `SetSnapRadiusPixels(value: int) -> bool` | Sets the snap radius pixels. |
| `GetSnapBoxRadius() -> float \| None` | Returns the snap box radius. |
| `SetSnapBoxRadius(value: float) -> bool` | Sets the snap box radius. |
| `GetSelectionRadius() -> float \| None` | Returns the selection radius. |
| `SetSelectionRadius(value: float) -> bool` | Sets the selection radius. |

*Angles*

| Method | Description |
|---|---|
| `GetSnapAngles() -> str \| None` | Returns the snap angles. Comma separated list in degrees, e.g. "30,45,60". |
| `SetSnapAngles(degreesList: str) -> bool` | Sets the snap angles. |
| `GetRelativeAngle() -> float \| None` | Returns the relative angle (radians). |
| `SetRelativeAngle(radians: float) -> bool` | Sets the relative angle. |
| `GetAlternateCoordinateSystemAngle() -> float \| None` | Returns the alternate coordinate system angle (radians). |
| `SetAlternateCoordinateSystemAngle(radians: float) -> bool` | Sets the alternate coordinate system angle. |

*Edge snapping options*

| Method | Description |
|---|---|
| `GetUseEdgeOffset() -> bool \| None` | Whether *Use Edge Offset* is on. |
| `SetUseEdgeOffset(value: bool) -> bool` | Turns *Use Edge Offset* on or off. |
| `GetEdgeOffsetDistance() -> float \| None` | Returns the edge offset distance. |
| `SetEdgeOffsetDistance(value: float) -> bool` | Sets the edge offset distance. |
| `GetUseProportionalDivision() -> bool \| None` | Whether *Use Proportional Division* is on. |
| `SetUseProportionalDivision(value: bool) -> bool` | Turns *Use Proportional Division* on or off. |
| `GetProportionalPercent() -> float \| None` | Returns the proportional percent. |
| `SetProportionalPercent(value: float) -> bool` | Sets the proportional percent. |
| `GetUseMultipleDivisions() -> bool \| None` | Whether *Use Multiple Divisions* is on. |
| `SetUseMultipleDivisions(value: bool) -> bool` | Turns *Use Multiple Divisions* on or off. |
| `GetDivisionDistance() -> float \| None` | Returns the division distance. |
| `SetDivisionDistance(value: float) -> bool` | Sets the division distance. |

### GridSettings

> **Full name:** `api.GridSettings` · **Inherits:** `api.Object`

Grid preferences.

**Constructors**

| Constructor | Description |
|---|---|
| `GridSettings()` | Stateless view of the grid preferences. |

**Methods**

| Method | Description |
|---|---|
| `GetShowGrid() -> bool \| None` | Whether *Show Grid* is on. |
| `SetShowGrid(value: bool) -> bool` | Turns *Show Grid* on or off. |
| `GetPrintGrid() -> bool \| None` | Whether *Print Grid* is on. |
| `SetPrintGrid(value: bool) -> bool` | Turns *Print Grid* on or off. |
| `GetSnapToGrid() -> bool \| None` | Whether *Snap To Grid* is on. |
| `SetSnapToGrid(value: bool) -> bool` | Turns *Snap To Grid* on or off. |
| `GetSnapGridX() -> float \| None` | Returns the snap grid X. |
| `SetSnapGridX(value: float) -> bool` | Sets the snap grid X. |
| `GetSnapGridY() -> float \| None` | Returns the snap grid Y. |
| `SetSnapGridY(value: float) -> bool` | Sets the snap grid Y. |
| `GetReferenceGridX() -> float \| None` | Returns the reference grid X. |
| `SetReferenceGridX(value: float) -> bool` | Sets the reference grid X. |
| `GetReferenceGridY() -> float \| None` | Returns the reference grid Y. |
| `SetReferenceGridY(value: float) -> bool` | Sets the reference grid Y. |
| `GetSheetLayerSnapGridX() -> float \| None` | Returns the sheet layer snap grid X. |
| `SetSheetLayerSnapGridX(value: float) -> bool` | Sets the sheet layer snap grid X. |
| `GetSheetLayerSnapGridY() -> float \| None` | Returns the sheet layer snap grid Y. |
| `SetSheetLayerSnapGridY(value: float) -> bool` | Sets the sheet layer snap grid Y. |
| `GetAngle() -> float \| None` | Returns the angle (radians). |
| `SetAngle(radians: float) -> bool` | Sets the angle. |
| `GetAngleY() -> float \| None` | Returns the angle Y (radians). |
| `SetAngleY(radians: float) -> bool` | Sets the angle Y. |

### StackLayersSettings

> **Full name:** `api.StackLayersSettings` · **Inherits:** `api.Object`

Unified view (stack layers) preferences.

**Constructors**

| Constructor | Description |
|---|---|
| `StackLayersSettings()` | Stateless view of the unified view (stack layers) preferences. |

**Methods**

| Method | Description |
|---|---|
| `GetEnabled() -> bool \| None` | Whether *Enabled* is on. |
| `SetEnabled(value: bool) -> bool` | Turns *Enabled* on or off. |
| `GetCreate2DObjects() -> bool \| None` | Whether *Create 2D Objects* is on. |
| `SetCreate2DObjects(value: bool) -> bool` | Turns *Create 2D Objects* on or off. |
| `GetIgnoreOtherScales() -> bool \| None` | Whether *Ignore Other Scales* is on. |
| `SetIgnoreOtherScales(value: bool) -> bool` | Turns *Ignore Other Scales* on or off. |
| `GetRestoreViews() -> bool \| None` | Whether *Restore Views* is on. |
| `SetRestoreViews(value: bool) -> bool` | Turns *Restore Views* on or off. |
| `GetCenterView() -> bool \| None` | Whether *Center View* is on. |
| `SetCenterView(value: bool) -> bool` | Turns *Center View* on or off. |
| `GetShowPageBoundary() -> bool \| None` | Whether *Show Page Boundary* is on. |
| `SetShowPageBoundary(value: bool) -> bool` | Turns *Show Page Boundary* on or off. |
| `GetOnlyActiveLayer2DObjects() -> bool \| None` | Whether *Only Active Layer 2D Objects* is on. |
| `SetOnlyActiveLayer2DObjects(value: bool) -> bool` | Turns *Only Active Layer 2D Objects* on or off. |
| `GetOnlyStoryLayers() -> bool \| None` | Whether *Only Story Layers* is on. |
| `SetOnlyStoryLayers(value: bool) -> bool` | Turns *Only Story Layers* on or off. |

### UnitSettings

> **Full name:** `api.UnitSettings` · **Inherits:** `api.Object`

Primary or secondary dimension units of the active document.

**Constructors**

| Constructor | Description |
|---|---|
| `UnitSettings(primary: bool = True)` | View of the primary units (`primary=True`) or of the secondary units. |

**Methods**

| Method | Description |
|---|---|
| `IsPrimary() -> bool` | True for the primary units, False for the secondary units. |
| `GetName() -> str \| None` | Returns the name. |
| `SetName(value: str) -> bool` | Sets the name. |
| `GetMark() -> str \| None` | Returns the mark. |
| `SetMark(value: str) -> bool` | Sets the mark. |
| `GetUnitsPerInch() -> float \| None` | Returns the units per inch. |
| `SetUnitsPerInch(value: float) -> bool` | Sets the units per inch. |
| `GetStyle() -> int \| None` | Returns the style (raw unit style). |
| `SetStyle(value: int) -> bool` | Sets the style. |
| `GetIsMetric() -> bool \| None` | Whether *Metric* is on. |
| `IsMetric() -> bool \| None` | True when the units are metric (same as `GetIsMetric`). |
| `SetIsMetric(value: bool) -> bool` | Turns *Metric* on or off. |
| `GetShowUnitMark() -> bool \| None` | Whether *Show Unit Mark* is on. |
| `SetShowUnitMark(value: bool) -> bool` | Turns *Show Unit Mark* on or off. |
| `GetLeadingZero() -> bool \| None` | Whether *Leading Zero* is on. |
| `SetLeadingZero(value: bool) -> bool` | Turns *Leading Zero* on or off. |
| `GetTrailingZeros() -> bool \| None` | Whether *Trailing Zeros* is on. |
| `SetTrailingZeros(value: bool) -> bool` | Turns *Trailing Zeros* on or off. |
| `GetDisplayAsFraction() -> bool \| None` | Whether *Display As Fraction* is on. |
| `SetDisplayAsFraction(value: bool) -> bool` | Turns *Display As Fraction* on or off. |
| `GetShowThousandsSeparator() -> bool \| None` | Whether *Show Thousands Separator* is on. |
| `SetShowThousandsSeparator(value: bool) -> bool` | Turns *Show Thousands Separator* on or off. |
| `GetDecimalDisplayPrecision() -> int \| None` | Returns the decimal display precision. |
| `SetDecimalDisplayPrecision(value: int) -> bool` | Sets the decimal display precision. |
| `GetDecimalDimensionPrecision() -> int \| None` | Returns the decimal dimension precision. |
| `SetDecimalDimensionPrecision(value: int) -> bool` | Sets the decimal dimension precision. |
| `GetFractionalDisplayPrecision() -> int \| None` | Returns the fractional display precision. |
| `SetFractionalDisplayPrecision(value: int) -> bool` | Sets the fractional display precision. |
| `GetFractionalDimensionPrecision() -> int \| None` | Returns the fractional dimension precision. |
| `SetFractionalDimensionPrecision(value: int) -> bool` | Sets the fractional dimension precision. |
| `GetAngularUnit() -> AngularUnit \| None` | Returns the angular unit. |
| `SetAngularUnit(value: AngularUnit) -> bool` | Sets the angular unit. |
| `GetWorldUnitsPerUnit() -> float \| None` | Primary units only (None / False for the secondary units) (read-only). |
| `GetSquareUnitDivision() -> int \| None` | Returns the square unit division. |
| `SetSquareUnitDivision(value: int) -> bool` | Sets the square unit division. |
| `GetSquareUnitMark() -> str \| None` | Returns the square unit mark. |
| `SetSquareUnitMark(value: str) -> bool` | Sets the square unit mark. |
| `GetAreaUnitName() -> str \| None` | Returns the area unit name. |
| `SetAreaUnitName(value: str) -> bool` | Sets the area unit name. |
| `GetAreaUnitMark() -> str \| None` | Returns the area unit mark. |
| `SetAreaUnitMark(value: str) -> bool` | Sets the area unit mark. |
| `GetAreaUnitsPerSquareInch() -> float \| None` | Returns the area units per square inch. |
| `SetAreaUnitsPerSquareInch(value: float) -> bool` | Sets the area units per square inch. |
| `GetAreaDecimalPrecision() -> int \| None` | Returns the area decimal precision. |
| `SetAreaDecimalPrecision(value: int) -> bool` | Sets the area decimal precision. |
| `GetVolumeUnitName() -> str \| None` | Returns the volume unit name. |
| `SetVolumeUnitName(value: str) -> bool` | Sets the volume unit name. |
| `GetVolumeUnitMark() -> str \| None` | Returns the volume unit mark. |
| `SetVolumeUnitMark(value: str) -> bool` | Sets the volume unit mark. |
| `GetVolumeUnitsPerCubicInch() -> float \| None` | Returns the volume units per cubic inch. |
| `SetVolumeUnitsPerCubicInch(value: float) -> bool` | Sets the volume units per cubic inch. |
| `GetVolumeDecimalPrecision() -> int \| None` | Returns the volume decimal precision. |
| `SetVolumeDecimalPrecision(value: int) -> bool` | Sets the volume decimal precision. |
| `GetDocumentAngularUnit() -> AngularUnit \| None` | Document angular settings (shared by the primary and secondary units). |
| `SetDocumentAngularUnit(value: AngularUnit) -> bool` | Sets the document angular unit (Document angular settings (shared by the primary and secondary units)). |
| `GetDocumentAngularPrecision() -> int \| None` | Returns the document angular precision. |
| `SetDocumentAngularPrecision(value: int) -> bool` | Sets the document angular precision. |

### TextDefaults

> **Full name:** `api.TextDefaults` · **Inherits:** `api.Object`

Default text settings for new text objects.

**Constructors**

| Constructor | Description |
|---|---|
| `TextDefaults()` | Stateless view of the default text settings. |

**Methods**

| Method | Description |
|---|---|
| `GetFontName() -> str \| None` | Returns the font name. |
| `SetFontName(value: str) -> bool` | Sets the font name. |
| `GetSize() -> float \| None` | Returns the size (world units). |
| `SetSize(value: float) -> bool` | Sets the size. |
| `GetStyle() -> TextStyleData \| None` | Returns the style. |
| `SetStyle(value: TextStyleData) -> bool` | Sets the style. |
| `GetJustification() -> TextJustification \| None` | Returns the justification. |
| `SetJustification(value: TextJustification) -> bool` | Sets the justification. |
| `GetVerticalAlignment() -> TextVerticalAlignment \| None` | Returns the vertical alignment. |
| `SetVerticalAlignment(value: TextVerticalAlignment) -> bool` | Sets the vertical alignment. |
| `GetLineSpacing() -> TextLineSpacing \| None` | Returns the line spacing. |
| `SetLineSpacing(value: TextLineSpacing) -> bool` | Sets the line spacing. |
| `GetLeading() -> float \| None` | Returns the leading (custom line spacing). |
| `SetLeading(value: float) -> bool` | Sets the leading. |

### DefaultAttributes

> **Full name:** `api.DefaultAttributes` · **Inherits:** `api.Object`

Default attributes for new objects (the Attributes palette with nothing selected). The `SetXxxByClass()` methods make the attribute follow the active class; setting an explicit value clears the corresponding by-class flag.

**Constructors**

| Constructor | Description |
|---|---|
| `DefaultAttributes()` | Stateless view of the default attributes for new objects. |

**Methods**

*General*

| Method | Description |
|---|---|
| `GetColors() -> ObjectColors \| None` | Colors. |
| `SetColors(colors: ObjectColors) -> bool` | Sets the colors. |
| `GetPenColorsByClass() -> bool \| None` | Whether *Pen Colors By Class* is on. |
| `SetPenColorsByClass() -> bool` | Sets the pen colors by class. |
| `GetFillColorsByClass() -> bool \| None` | Whether *Fill Colors By Class* is on. |
| `SetFillColorsByClass() -> bool` | Sets the fill colors by class. |

*Pen*

| Method | Description |
|---|---|
| `GetPenStyle() -> int \| None` | Raw pen style, same values as `PenAttributes.GetStyle`. |
| `SetPenStyle(style: int) -> bool` | Sets the pen style (raw pen style, same values as `PenAttributes.GetStyle`). |
| `GetPenStyleByClass() -> bool \| None` | Whether *Pen Style By Class* is on. |
| `SetPenStyleByClass() -> bool` | Sets the pen style by class. |
| `GetLineWeightMils() -> int \| None` | Returns the line weight mils. |
| `SetLineWeightMils(mils: int) -> bool` | Sets the line weight mils. |
| `GetLineWeightByClass() -> bool \| None` | Whether *Line Weight By Class* is on. |
| `SetLineWeightByClass() -> bool` | Sets the line weight by class. |

*Fill*

| Method | Description |
|---|---|
| `GetFillStyle() -> int \| None` | Raw fill style, same values as `FillAttributes.GetStyle`. |
| `SetFillStyle(style: int) -> bool` | Sets the fill style (raw fill style, same values as `FillAttributes.GetStyle`). |
| `GetFillStyleByClass() -> bool \| None` | Whether *Fill Style By Class* is on. |
| `SetFillStyleByClass() -> bool` | Sets the fill style by class. |
| `GetFillTypeRaw() -> int \| None` | Returns the fill type raw (read-only). |
| `GetHatch() -> int \| None` | Returns the hatch. |
| `SetHatch(hatch: int) -> bool` | Sets the hatch. |
| `GetGradient() -> int \| None` | Returns the gradient. |
| `SetGradient(gradient: int) -> bool` | Sets the gradient. |
| `GetImageFill() -> int \| None` | Returns the image fill. |
| `SetImageFill(image: int) -> bool` | Sets the image fill. |
| `GetTile() -> int \| None` | Returns the tile. |
| `SetTile(tile: int) -> bool` | Sets the tile. |

*Opacity*

| Method | Description |
|---|---|
| `GetPenOpacity() -> int \| None` | Returns the pen opacity. |
| `GetFillOpacity() -> int \| None` | Returns the fill opacity. |
| `SetOpacity(pen: int, fill: int) -> bool` | Sets the opacity. |
| `GetPenOpacityByClass() -> bool \| None` | Whether *Pen Opacity By Class* is on. |
| `GetFillOpacityByClass() -> bool \| None` | Whether *Fill Opacity By Class* is on. |
| `SetOpacityByClass(penByClass: bool, fillByClass: bool) -> bool` | Sets the opacity by class. |

*Markers*

| Method | Description |
|---|---|
| `GetBeginningMarker() -> Marker \| None` | Returns the beginning marker. |
| `SetBeginningMarker(marker: Marker) -> bool` | Sets the beginning marker. |
| `GetEndMarker() -> Marker \| None` | Returns the end marker. |
| `SetEndMarker(marker: Marker) -> bool` | Sets the end marker. |
| `GetMarkersByClass() -> bool \| None` | Whether *Markers By Class* is on. |
| `SetMarkersByClass() -> bool` | Sets the markers by class. |
| `GetDocumentDropShadow() -> DropShadow \| None` | Drop shadow of the document (Document Preferences). |
| `GetClass() -> ClassAttributes` | Class used for new objects and for new dimensions. |
| `SetClass(theClass: ClassAttributes) -> bool` | Sets the class (Class used for new objects and for new dimensions). |
| `GetDimensionClass() -> ClassAttributes` | Returns the dimension class. |
| `SetDimensionClass(theClass: ClassAttributes) -> bool` | Sets the dimension class. |

### LayerContents

> **Full name:** `api.LayerContents` · **Inherits:** `api.Object`

Object count and bounds of the top level objects of a layer.

**Constructors**

| Constructor | Description |
|---|---|
| `LayerContents()` | Default value (fields at their defaults). |
| `LayerContents(fObjectCount, fBounds)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fObjectCount` | `int` | Number of top level objects. |
| `fBounds` | `Math.Rect2D \| None` | Bounds of the top level objects; `None` for an empty layer. |

### Layer

> **Full name:** `api.Layer` · **Inherits:** `api.Object`

A layer (design or sheet layer). Constructing from a handle that is not a layer produces an invalid object (`IsValid()` == `False`).

**Constructors**

| Constructor | Description |
|---|---|
| `Layer(hLayer: Handle)` | Refers to the existing layer `hLayer`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `GetHandle() -> Handle` | Handle of the layer. |
| `IsValid() -> bool` | True when this object refers to an existing layer. |

*Identity*

| Method | Description |
|---|---|
| `GetName() -> str \| None` | Returns the name. |
| `SetName(name: str) -> bool` | Sets the name. |
| `GetType() -> LayerType \| None` | Returns the type. |
| `IsDesignLayer() -> bool` | True for a design layer. |
| `IsSheetLayer() -> bool` | True for a sheet layer. |
| `GetNext() -> Layer` | Returns the next. |
| `GetPrevious() -> Layer` | Returns the previous. |

*State*

| Method | Description |
|---|---|
| `IsActive() -> bool` | True when this is the active layer. |
| `Activate() -> bool` | Makes this layer the active layer. |
| `GetVisibility() -> LayerVisibility \| None` | Returns the visibility. |
| `SetVisibility(visibility: LayerVisibility) -> bool` | Sets the visibility. |

*Design layer properties*

| Method | Description |
|---|---|
| `GetScale() -> float \| None` | Returns the scale (1:scale). |
| `SetScale(scale: float) -> bool` | Sets the scale. |
| `GetElevation() -> float \| None` | Returns the elevation (world units). |
| `SetElevation(elevation: float) -> bool` | Sets the elevation. |
| `GetThickness() -> float \| None` | Returns the thickness (world units). |
| `SetThickness(thickness: float) -> bool` | Sets the thickness. |
| `GetRenderMode() -> int \| None` | Returns the render mode (raw render mode). |
| `GetProjection() -> int \| None` | Returns the projection (raw projection). |
| `GetStory() -> Story` | Story of a design layer. A design layer belongs to at most one story and has at most one level type: the name of its level in the story (see Story). Changing them updates the story levels, records the layer and the story data for undo, and updates the objects bound to the stories (e.g. walls). The story of the layer; invalid when the layer is not in a story. |
| `GetLevelType() -> str \| None` | Level type of the layer; empty when it has none, `None` for an invalid object. |
| `SetLevelType(levelType: str) -> bool` | In a story the layer moves to the level of that type, like AssociateWithStory(`GetStory()`, levelType); empty clears the level type (the layer keeps its story and elevation, the story loses the level). A level type the document does not have yet is added to it. Design layers only. |
| `AssociateWithStory(story: Story, levelType: str = '') -> bool` | Puts the design layer into `story` at `levelType` (empty: the layer's current level type); a previous story of the layer loses the layer's level. The layer moves to the level elevation: the offset of the story's level of that type, or of the first default story level of that type, or 0. Fails when another layer of the story has that level type, or without a level type. A level type the document does not have yet is added to it. |
| `DetachFromStory() -> bool` | Removes the design layer from its story: it keeps its elevation and loses its story and level type; the story loses the level. `True` when the layer is not in a story. |

*Sheet layer properties*

| Method | Description |
|---|---|
| `GetDescription() -> str \| None` | Returns the description (sheet title). |
| `SetDescription(description: str) -> bool` | Sets the description. |
| `GetDPI() -> int \| None` | Returns the DPI. |
| `SetDPI(dpi: int) -> bool` | Sets the DPI. |
| `GetFirstObject() -> Handle` | Contents (top level objects). Like VectorScript FInLayer / NextObj these see the drawing objects only: the undo placeholders of deleted objects and the terminator that ends the object list are skipped. The first / last object is null for an empty layer. ForEachObject fetches the next object before the callback runs, so the callback may delete or move the current one. |
| `GetLastObject() -> Handle` | Returns the last object. |
| `ForEachObject(callback: callable(Handle)) -> None` | Calls `callback` with every top level object of the layer. Contents (top level objects). Like VectorScript FInLayer / NextObj these see the drawing objects only: the undo placeholders of deleted objects and the terminator that ends the object list are skipped. The first / last object is null for an empty layer. ForEachObject fetches the next object before the callback runs, so the callback may delete or move the current one. |
| `GetObjects() -> list[Handle]` | Returns the objects. |
| `GetObjectCount() -> int` | Number of object items. |
| `GetBounds() -> Math.Rect2D \| None` | Returns the bounds (bounds of the top level objects). |
| `GetContents() -> LayerContents` | Returns the contents (object count and bounds in one walk). |
| `GetObjectsOf(type: type) -> object` | Top level objects of the layer that are instances of the class `type`, as a list of `type` objects, e.g. `layer.GetObjectsOf(api.RectangleObject)`. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True when the object is valid (same as `IsValid()`). |
| `==` | `__eq__(o: Layer) -> bool` | `a == b`: True when both objects refer to the same layer. |
| `!=` | `__ne__(o: Layer) -> bool` | `a != b`: True when the objects refer to different layers. |

### StoryLevel

> **Full name:** `api.StoryLevel` · **Inherits:** `api.Object`

One level of a story: a named height (its level type) relative to the story elevation, optionally with the design layer of that level.

**Constructors**

| Constructor | Description |
|---|---|
| `StoryLevel()` | Default value (fields at their defaults). |
| `StoryLevel(fLevelType, fElevationOffset, fElevation, fLayerName, fLayer)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fLevelType` | `str` | Level type, unique in the story, e.g. "Slab" or "OK-FB". |
| `fElevationOffset` | `float` | World units, relative to the story elevation. |
| `fElevation` | `float` | World units: story elevation + fElevationOffset. |
| `fLayerName` | `str` | Name of the level's layer; empty for a level without layer. |
| `fLayer` | `Layer` | The design layer of the story with this level type; invalid when there is none. |

### StoryLevelTemplate

> **Full name:** `api.StoryLevelTemplate` · **Inherits:** `api.Object`

A default story level (Organization dialog box > Stories tab > Default Story Levels): a template for story levels.

**Constructors**

| Constructor | Description |
|---|---|
| `StoryLevelTemplate()` | Default value (fields at their defaults). |
| `StoryLevelTemplate(fIndex, fLevelType, fElevationOffset, fLayerName, fScaleFactor, fDefaultWallHeight)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fIndex` | `int` | 1-based position in the default story levels. |
| `fLevelType` | `str` | Level type of the levels made from it. |
| `fElevationOffset` | `float` | World units, relative to the story elevation. |
| `fLayerName` | `str` | Layer name without the story affix; empty: the levels have no layer. |
| `fScaleFactor` | `float` | Scale of the layer (1:fScaleFactor). |
| `fDefaultWallHeight` | `float` | World units; wall height of the layer. |

### Story

> **Full name:** `api.Story` · **Inherits:** `api.Object`

A story: a floor of the building at an elevation. Its levels (StoryLevel) are heights relative to the story elevation, each with a level type and, optionally, a design layer. When the story elevation changes, its layers and the objects bound to its levels follow. Stories are document data, not drawing objects. Constructing from a handle that is not a story produces an invalid object (`IsValid()` == `False`).

Undo: like the story dialog boxes of the Organization dialog box, the changing methods record what they change in the current undo event (open one with `Document.StartUndoEvent`): the story data, the layers they change, create or delete, and the objects bound to the changed stories, levels and layers, which they update. Do not register stories, or layers these methods create, again with `Document.AddAfterSwapObject` / AddBothSwapObject.

**Constructors**

| Constructor | Description |
|---|---|
| `Story(hStory: Handle)` | Refers to the existing story `hStory`; check `IsValid()` before use. |

**Methods**

*General*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | True when `h` refers to an object of the kind this class represents. |
| `GetHandle() -> Handle` | Handle of the story. |
| `IsValid() -> bool` | True when this object refers to an existing story. |
| `Create(name: str, elevation: float, affix: str = '', isPrefix: bool = False) -> Story` *static* | Creates a story without levels at `elevation` (world units); add levels with AddLevel / AddLevelFromTemplate. `affix` is the prefix or suffix of the names of the layers made for the story from default story levels. Each story needs its own affix (compared ignoring case); an empty affix counts as one. `isPrefix` is passed on like the New Story dialog box does, but Vectorworks does not store it (see UsesPrefix). Fails (invalid object) when `name` is empty, longer than 63 characters or names another object, when `affix` is used by another story, or when another story has that elevation. |

*Identity*

| Method | Description |
|---|---|
| `GetName() -> str \| None` | Returns the name. |
| `SetName(name: str) -> bool` | Fails for an empty name, a name longer than 63 characters or the name of another object. Like the Edit Story dialog box, it also renames the story in the IFC data and updates the objects that show the name. |
| `GetAffix() -> str \| None` | Prefix or suffix of the names of the layers made for the story from default story levels. |
| `SetAffix(affix: str) -> bool` | Fails when another story uses `affix` (ignoring case, so also for a change of the letter case only). The names of existing layers do not change. |
| `UsesPrefix() -> bool \| None` | Whether the story's layer names start with the affix. Vectorworks does not store it but infers it from the layer names of the levels: `True` when no level has a layer. |
| `GetElevation() -> float \| None` | Elevation (world units). |
| `SetElevation(elevation: float, mode: StoryElevationChangeMode = StoryElevationChangeMode.Single) -> bool` | Moves the story, and depending on `mode` the stories above / below it, by elevation - `GetElevation()`; the design layers of the moved stories move with them. Fails without change when a moved story would get the elevation of a story that does not move: two stories cannot share an elevation. |
| `GetStoryAbove() -> Story` | The next story above / below by elevation; invalid when there is none. |
| `GetStoryBelow() -> Story` | Returns the story below. |
| `Delete(deleteLayers: bool = False) -> bool` | Deletes the story; the object becomes invalid. Its design layers stay, without story and level type, unless `deleteLayers` deletes them; that fails when they are all the design layers of the document. |
| `GetLevels() -> list[StoryLevel]` | Levels, sorted by elevation offset. |
| `GetLevel(levelType: str) -> StoryLevel \| None` | The level with this level type (compared ignoring case, like Vectorworks does); `None` when there is none. |
| `AddLevel(levelType: str, elevationOffset: float, layerName: str = '', createLayerIfMissing: bool = True, scale: float = 0.0) -> bool` | Adds the level `levelType` at `elevationOffset` (world units, relative to the story elevation). Without `layerName` the level has no layer. Otherwise its layer is the design layer `layerName`: an existing one without level type is put into the story at the level elevation; a missing one is created when `createLayerIfMissing`, with `scale` (0: the scale of the active layer; the active layer stays active). Fails when the story already has the level type, or when `layerName` names a sheet layer, a layer with a level type or another object. A level type the document does not have yet is added to it. |
| `AddLevelFromTemplate(index: int) -> bool` | Adds the level of the default story level `index` (1-based, see `Document.GetStoryLevelTemplates`) like Vectorworks does: its layer, if the template has a layer name, is created as <layer name>-<affix> with the template scale and wall height, and the active layer stays active. Fails when the story already has that level type. |
| `SetLevelElevationOffset(levelType: str, elevationOffset: float) -> bool` | Moves the level and its layer, with its objects, to `elevationOffset` (world units, relative to the story). |
| `RemoveLevel(levelType: str, deleteLayer: bool = False) -> bool` | Removes the level. Its layer stays, without story and level type, unless `deleteLayer` deletes it; that fails when it is the only design layer of the document. |
| `GetLayers() -> list[Layer]` | Design layers in the story, in the order of the document's layer list. |
| `GetLayerForLevelType(levelType: str) -> Layer` | The design layer of the story with this level type; invalid when there is none. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True when the object is valid (same as `IsValid()`). |
| `==` | `__eq__(o: Story) -> bool` | `a == b`: True when both objects refer to the same story. |
| `!=` | `__ne__(o: Story) -> bool` | `a != b`: True when the objects refer to different stories. |

### Document

> **Full name:** `api.Document` · **Inherits:** `api.Object`

Stateless facade over the active Vectorworks document. Exposes the selection, layers, stories, classes, objects, view, units, default attributes and preferences. Construct it on demand (no state is kept between calls):

```python
import api

doc = api.Document()
if api.Document.IsOpen():                   # there is an active document
    for h in doc.GetSelection():               # iterate the current selection
        rect = api.Document.As(api.RectangleObject, h)
        if rect:
            rect.SetSize(1.0, 2.0)
```

**Constructors**

| Constructor | Description |
|---|---|
| `Document()` | Stateless facade over the active document (no state is kept between calls). |

**Methods**

*General*

| Method | Description |
|---|---|
| `IsOpen() -> bool` *static* | Whether there is currently an open, active document. Every other method requires this to be `True`. |

*Preferences*

| Method | Description |
|---|---|
| `Display() -> DisplaySettings` | The display preferences (`DisplaySettings`). |
| `Editing() -> EditingSettings` | The editing and session preferences (`EditingSettings`). |
| `Snapping() -> SnapSettings` | The snapping (SmartCursor) preferences (`SnapSettings`). |
| `Grid() -> GridSettings` | The grid preferences (`GridSettings`). |
| `StackLayers() -> StackLayersSettings` | The unified view (stack layers) preferences (`StackLayersSettings`). |
| `PrimaryUnits() -> UnitSettings` | The primary dimension units of the document (`UnitSettings`). |
| `SecondaryUnits() -> UnitSettings` | The secondary dimension units of the document (`UnitSettings`). |
| `TextDefaults() -> TextDefaults` | The default text settings for new text objects (`TextDefaults`). |
| `DefaultAttributes() -> DefaultAttributes` | The default attributes for new objects (`DefaultAttributes`). |

*Selection*

| Method | Description |
|---|---|
| `GetSelectionCount() -> int` | These report the selection the way the Vectorworks editing commands see it: only the working layers (the active layer, plus the other layers when the layer options allow modifying them). Use them for anything that edits the selection. |
| `HasSelection() -> bool` | True when at least one object is selected. |
| `GetFirstSelected() -> Handle` | Returns the first selected. |
| `GetSelection(descend: Descend = Descend.None_) -> list[Handle]` | Returns the selection for `descend`. |
| `ForEachSelected(callback: callable(Handle), descend: Descend = Descend.None_) -> None` | Calls `callback` with every selected object. These report the selection the way the Vectorworks editing commands see it: only the working layers (the active layer, plus the other layers when the layer options allow modifying them). Use them for anything that edits the selection. |
| `GetSelectionBounds() -> Math.Rect2D \| None` | Returns the selection bounds. |
| `GetSelectionCountOnAllLayers() -> int` | Same, but over every layer of the drawing: an object stays selected when the user switches layers, so these report the full selection. Reading only - the editing operations below still act on working layers. |
| `GetSelectionOnAllLayers(descend: Descend = Descend.None_) -> list[Handle]` | Returns the selection on all layers for `descend`. |
| `ForEachSelectedOnAllLayers(callback: callable(Handle), descend: Descend = Descend.None_) -> None` | Calls `callback` with every selected object of every layer. Same, but over every layer of the drawing: an object stays selected when the user switches layers, so these report the full selection. Reading only - the editing operations below still act on working layers. |
| `GetSelectionBoundsOnAllLayers() -> Math.Rect2D \| None` | Returns the selection bounds on all layers. |
| `IsSelected(h: Handle) -> bool` | True when the object `h` is selected. |
| `Select(h: Handle, select: bool = True) -> bool` | Selects (or, with `select=False`, deselects) the object `h`. |
| `Select(object: PrimitiveObject, select: bool = True) -> bool` | Selects (or, with `select=False`, deselects) `object`. |
| `Deselect(h: Handle) -> bool` | Deselects the object `h`. |
| `Select(objects: list[Handle]) -> int` | Adds the objects `objects` to the selection; returns how many were selected. |
| `SetSelection(objects: list[Handle]) -> int` | Sets the selection (replaces the selection). |
| `SelectAll() -> None` | Selects all objects (like Edit > Select All). |
| `DeselectAll() -> None` | Clears the selection. |
| `GetSelectionOf(type: type, descend: Descend = Descend.None_) -> object` | Selected objects that are instances of the class `type`, as a list of `type` objects, e.g. `doc.GetSelectionOf(api.Line2DObject)`. |

*Operations on the selection*

| Method | Description |
|---|---|
| `MoveSelection(offset: Math.Point2D) -> bool` | Moves the selected objects by `offset` (world units). |
| `RotateSelection(angle: float, center: Math.Point2D) -> bool` | Rotates the selected objects by `angle` (radians, counter-clockwise) around `center`. |
| `ScaleSelection(scaleX: float, scaleY: float, center: Math.Point2D) -> bool` | Scales the selected objects by `scaleX` / `scaleY` around `center`. |
| `DuplicateSelection(offset: Math.Point2D = Math.Point2D()) -> bool` | Duplicates the selected objects, offsetting the copies by `offset`. |
| `GroupSelection() -> Handle` | Groups the selected objects; returns the handle of the new group (null when nothing is selected). |
| `DeleteSelection(useUndo: bool = True) -> int` | Deletes the selected objects (recorded for undo unless `useUndo` is `False`); returns how many were deleted. |
| `SetSelectionClass(theClass: ClassAttributes, useClassAttributes: bool = False) -> bool` | Sets the selection class. |

*Objects*

| Method | Description |
|---|---|
| `ForEachObject(what: Traverse, callback: callable(Handle), descend: Descend = Descend.None_) -> None` | Visits every object matching `what` (see Traverse). `descend` controls whether the traversal enters containers such as groups, symbols and viewports (see Descend). The callback runs synchronously. |
| `GetObjects(what: Traverse, descend: Descend = Descend.None_) -> list[Handle]` | Collects every object matching `what` (see ForEachObject). |
| `GetLayerContents(what: Traverse) -> dict[Handle, LayerContents]` | Object count and bounds of the top level objects `what` visits, keyed by layer handle; layers without such objects are absent. |
| `GetObjectsAtPoint(pt: Math.Point2D, radius: float, what: Traverse = Traverse.Visible, descend: Descend = Descend.None_) -> list[Handle]` | Collects objects whose geometry lies within `radius` world units of `pt` (like a click hit test). |
| `GetObjectsInCriteria(criteria: str) -> list[Handle]` | Collects objects matching a Vectorworks criteria string (the same syntax used by Vectorscript / criteria dialogs), e.g. "(T=RECT)" for every rectangle or "(C='My Class')" for every object in the class 'My Class'. |
| `GetCriteriaError(criteria: str) -> str \| None` | Why `criteria` does not compile (GetObjectsInCriteria then finds nothing); `None` when it compiles. |
| `GetObjectType(h: Handle) -> ObjectType` *static* | Object type (kind of geometric / structural object). Only a subset of ObjectType has typed classes. |
| `AttributesOf(h: Handle) -> ObjectAttributes` *static* | Graphical attributes (pen, fill, marker, drop shadow, class, ...) of any object. |
| `ClassOf(h: Handle) -> ClassAttributes` *static* | Class of the object `h`. |
| `LayerOf(h: Handle) -> Layer` *static* | The layer that ultimately contains the object (walks up through groups, symbols, ... until it finds a layer). |
| `FindByName(name: str) -> Handle` | Object identity lookups. Return null when no object matches. |
| `FindByUuid(uuid: str) -> Handle` | The object with the persistent UUID `uuid`; a null handle when none matches. |
| `FindByIndex(index: int) -> Handle` | The object with the internal index `index`; a null handle when none matches. |
| `GetUuid(h: Handle) -> str \| None` | Persistent UUID of the object, stable across save/load. |
| `As(type: type, h: Handle) -> object` *static* | The handle `h` as a typed object: an instance of the class `type` (for example `api.ArcObject`) when `type.Is(h)`, otherwise `None`. Example: `arc = api.Document.As(api.ArcObject, h)`. |
| `GetObjectsOf(type: type, what: Traverse = Traverse.All, descend: Descend = Descend.None_) -> object` | Every object matching `what` that is an instance of the class `type`, as a list of `type` objects, e.g. `doc.GetObjectsOf(api.RectangleObject)`. |

*Layers*

| Method | Description |
|---|---|
| `GetActiveLayer() -> Layer` | Returns the active layer. |
| `SetActiveLayer(layer: Layer) -> bool` | Sets the active layer. |
| `FindLayer(name: str) -> Layer` | The layer named `name`; an invalid `Layer` when there is none. |
| `ForEachLayer(callback: callable(Layer)) -> None` | Calls `callback` with every layer of the document. |
| `GetLayers() -> list[Layer]` | Returns the layers. |
| `GetLayers(type: LayerType) -> list[Layer]` | Returns the layers for `type`. |
| `CreateDesignLayer(name: str, scale: float = 1.0) -> Layer` | Creates a design layer named `name` with the scale 1:`scale`. |
| `CreateSheetLayer(name: str) -> Layer` | Creates a sheet layer named `name`. |
| `GetLayerOptions() -> VisibilityOptions \| None` | Returns the layer options. |
| `SetLayerOptions(options: VisibilityOptions) -> bool` | Sets the layer options. |
| `GetActiveLayerScale() -> float \| None` | Returns the active layer scale. |

*Stories*

| Method | Description |
|---|---|
| `GetStories() -> list[Story]` | Stories of the document, sorted by elevation (lowest first). See Story, also for the undo behavior. |
| `FindStory(name: str) -> Story` | The story named `name`; invalid when there is none. |
| `CreateStory(name: str, elevation: float, affix: str = '', isPrefix: bool = False) -> Story` | Creates a story named `name` at `elevation` (same as `Story.Create`); `affix` is added to the names of its level layers. Fails (invalid object) for an empty, too long or used name, a used affix or a used elevation. |
| `GetLevelTypes() -> list[str]` | Level types (Organization dialog box > Stories tab > Level Types): the names of story levels, in document order. Names have at most 63 characters. Vectorworks compares them ignoring case; the story methods keep the spelling that the document or the story already uses. Changes are undoable. |
| `AddLevelType(name: str) -> bool` | Fails when the name exists already (ignoring case). |
| `RenameLevelType(oldName: str, newName: str) -> bool` | Also renames the level type of layers, story levels, default story levels and story bound objects. Fails when `newName` exists already (ignoring case), so also for a change of the letter case only. Undo does not restore the level type in the story bounds of objects and in horizontal section viewports: Vectorworks renames it there without recording them, as in the Level Types dialog box. Rename it back instead. |
| `DeleteLevelType(name: str) -> bool` | Like the Level Types dialog box: layers and default story levels with this level type lose it; story levels keep it. |
| `GetStoryLevelTemplates() -> list[StoryLevelTemplate]` | Default story levels (Organization dialog box > Stories tab > Default Story Levels), the templates of story levels. Indices are 1-based; GetStoryLevelTemplates returns them in index order. Changes are undoable. |
| `AddStoryLevelTemplate(levelType: str, elevationOffset: float, layerName: str = '', scaleFactor: float = 0.0, defaultWallHeight: float = 0.0) -> int \| None` | Adds a default story level and returns its index: Vectorworks inserts it first (index 1). `scaleFactor` 0 uses the scale of the active layer. Fails when a default story level has the same level type and elevation offset. A level type the document does not have yet is added to it. |
| `DeleteStoryLevelTemplate(index: int) -> bool` | Deletes the default story level at `index`. |
| `ResetDefaultStoryLevels(deleteExisting: bool) -> bool` | Adds the default story levels and level types of the Vectorworks defaults again (level types the document has are kept). `deleteExisting` deletes the current default story levels first; otherwise the defaults are added to them, which can duplicate default story levels. |

*Classes*

| Method | Description |
|---|---|
| `GetActiveClass() -> ClassAttributes` | Returns the active class. |
| `SetActiveClass(theClass: ClassAttributes) -> bool` | Sets the active class. |
| `FindClass(name: str) -> ClassAttributes` | The class named `name`; an invalid `ClassAttributes` when there is none. |
| `CreateClass(name: str) -> ClassAttributes` | Creates a class named `name` (or returns the existing one). |
| `GetClasses(includeGuestClasses: bool = False) -> list[ClassAttributes]` | Returns the classes for `includeGuestClasses`. |
| `GetClassOptions() -> VisibilityOptions \| None` | Returns the class options. |
| `SetClassOptions(options: VisibilityOptions) -> bool` | Sets the class options. |

*Containers*

| Method | Description |
|---|---|
| `GetDrawingHeader() -> Handle` | Root object of the drawing. Rarely needed directly. |
| `GetDefaultContainer() -> Handle` | The container that receives newly created objects (the active layer, or the edited group / symbol definition). |
| `IsInsideGroup() -> bool \| None` | `True` when the user is currently editing the contents of a group (inside a "Enter Group" edit session). |
| `GetEditedGroup() -> Handle` | The group currently being edited (null when not editing a group). |
| `GetActiveSymbolDefinition() -> Handle` | The symbol definition currently being edited (null when not editing one). |
| `SetActiveSymbolDefinition(hSymbolDefinition: Handle) -> bool` | Sets the active symbol definition. The symbol definition currently being edited (null when not editing one). |

*View and page*

| Method | Description |
|---|---|
| `GetPageBounds() -> Math.Rect2D \| None` | Rectangle covering the printable pages of the drawing, in world coordinates. |

*User origin*

| Method | Description |
|---|---|
| `GetUserOrigin() -> Math.Point2D \| None` | The world point that appears at (0, 0) in the user coordinate system. |
| `SetUserOrigin(origin: Math.Point2D) -> bool` | Sets the user origin. The world point that appears at (0, 0) in the user coordinate system. |
| `GetViewCenter() -> Math.Point2D \| None` | Point at the center of the current view, in world coordinates. |
| `SetViewCenter(center: Math.Point2D) -> bool` | Sets the view center. Point at the center of the current view, in world coordinates. |

*Zoom factor*

| Method | Description |
|---|---|
| `SetZoom(zoomFactor: float) -> bool` | 1.0 = 100 %, 2.0 = 200 % (twice as large on screen), 0.5 = 50 %. |
| `IsPlanRotated() -> bool \| None` | True when the plan rotation of the view is not zero. |
| `GetPlanRotationAngle() -> float \| None` | Returns the plan rotation angle (radians, counter-clockwise). |
| `Redraw(area: Math.Rect2D) -> bool` | Marks the world rectangle `area` as needing redraw. Call after edits that the API did not perform itself. |

*Units*

| Method | Description |
|---|---|
| `WorldToUnits(worldLength: float) -> float \| None` | Converts between the internal world units used by the API and the primary document units shown in the UI. |
| `UnitsToWorld(unitsLength: float) -> float \| None` | Converts `unitsLength` from document units to world units. Converts between the internal world units used by the API and the primary document units shown in the UI. |

*Undo*

| Method | Description |
|---|---|
| `StartUndoEvent(method: UndoMethod = UndoMethod.SwapObjects, isRevertible: bool = False) -> None` | Opens an undo event and selects its method (usually `UndoMethod.SwapObjects`). Call before making any change. `isRevertible` lets `RevertUndoEvent()` take the event back (see above). Vectorworks then builds the event even if undo is off (zero undo levels); it drops such an event when it ends. It applies to SwapObjects and ReplaceSelection: `UndoMethod.None_` begins no event. |
| `NameUndoEvent(name: str) -> None` | Names the current undo event so it appears as "Undo <name>" in the Edit menu. Call inside the event, before the change. |
| `EndUndoEvent() -> None` | Closes the current undo event now. Vectorworks also ends it automatically when the operation completes. |
| `RevertUndoEvent() -> bool` | Takes back the event that is being built: undoes what it recorded and removes it from the undo list (see above). Call it instead of `EndUndoEvent()`, for an event started with `isRevertible=True`. Returns `False` when no event is being built. Otherwise it returns `True`, also when the event could not be reverted (it cannot if it was not started with `isRevertible=True`). Does nothing and returns `False` while the undo of the running script is managed by the application that runs it. |
| `IsBuildingUndoEvent() -> bool` | Whether an undo event is being built: begun and not ended yet. That is `True` for the event you opened with StartUndoEvent, but also for an event that Vectorworks opened for the command or script that runs, and for a hidden event that an API call that records undo began because no event was open. |
| `AddAfterSwapObject(object: Handle) -> bool` | Undo object registration - only meaningful inside an `UndoMethod.SwapObjects` (or ReplaceSelection) event. Register an object you just CREATED and added to the drawing so Undo removes it again. Pass null to register every currently selected object (e.g. right after DuplicateSelection). |
| `AddBothSwapObject(object: Handle) -> bool` | Register an object you are ABOUT TO MODIFY so Undo restores its previous state; a copy is stored in the undo record. Call BEFORE the change. Pass null for every currently selected object. |
| `AddBeforeSwapObject(object: Handle) -> bool` | Register an object you are about to DELETE. Deprecated: `Delete()` already records the deletion for undo, so this is rarely needed. Pass null for every selected object. |
| `AddBeforeMoveObject(object: Handle) -> bool` | Register an object that you MOVE from its container (layer, group, symbol definition) into another one with `PrimitiveObject.MoveToContainer`, so that Undo puts it back where it was: AddBeforeMoveObject BEFORE the move, AddAfterMoveObject after it, both with the object. They record where the object is in the drawing, not its state. Record only this pair for the moved object in the event (the combination with AddBothSwapObject on the same object in one event is not a verified sequence): make other changes of the object in an undo event of their own. A new object that is not in the drawing yet (for example the result of a Boolean operation) is inserted with MoveToContainer and registered with AddAfterSwapObject instead. Pass null for every currently selected object. |
| `AddAfterMoveObject(object: Handle) -> bool` | Registers `object` for undo right after it was moved to another container. Register an object that you MOVE from its container (layer, group, symbol definition) into another one with `PrimitiveObject.MoveToContainer`, so that Undo puts it back where it was: AddBeforeMoveObject BEFORE the move, AddAfterMoveObject after it, both with the object. They record where the object is in the drawing, not its state. Record only this pair for the moved object in the event (the combination with AddBothSwapObject on the same object in one event is not a verified sequence): make other changes of the object in an undo event of their own. A new object that is not in the drawing yet (for example the result of a Boolean operation) is inserted with MoveToContainer and registered with AddAfterSwapObject instead. Pass null for every currently selected object. |

## Enumerations

### Traverse

> **Full name:** `api.Traverse` · **Kind:** `IntEnum`

Which set of objects a document traversal visits. Passed to `Document.ForEachObject` / GetObjects / GetObjectsAtPoint.

| Member | Value | Description |
|---|---|---|
| `Selected` | `0` | Only currently selected top-level objects. |
| `Editable` | `1` | Unlocked objects on visible, editable layers and classes. |
| `Visible` | `2` | Objects that are currently drawn on screen (visible layer + visible class). |
| `Drawing` | `3` | Every object in the drawing (all layers), excluding resources. |
| `SymbolDefinitions` | `4` | Only symbol definitions (the reusable templates in the Resource Manager). |
| `SelectedAndEditable` | `5` | Selected, visible and unlocked objects on editable layers. |
| `All` | `6` | Every drawing object plus symbol definitions and their contents. |
| `AllAndResources` | `7` | Like All, plus resource objects (hatches, gradients, symbol definitions, ...) |

### Descend

> **Full name:** `api.Descend` · **Kind:** `IntFlag` (members combine with `|`)

How deep a traversal descends into container objects (groups, symbols, viewports, ...). The values are bit flags: combine members with `|` to descend into more than one kind of container, for example `api.Descend.Groups | api.Descend.Viewports`.

| Member | Value | Description |
|---|---|---|
| `None_` | `0` | Visit top level objects only, do not enter any container. |
| `Groups` | `32` | Descend into groups. |
| `All` | `64` | Descend into every container kind (groups, symbols, plug-in objects, ...) |
| `Viewports` | `128` | Descend into viewports (sheet layer viewports). |
| `AuxiliaryLists` | `256` | Include auxiliary objects attached to visited objects. |

### LayerType

> **Full name:** `api.LayerType` · **Kind:** `IntEnum`

Kind of a layer.

| Member | Value | Description |
|---|---|---|
| `Unknown` | `0` |  |
| `Design` | `1` | A world coordinate design layer (regular drawing surface). |
| `Sheet` | `2` | A sheet layer (a printable page, holds viewports). |
| `GuestDesign` | `3` | A design layer imported/referenced from another document. |

### LayerVisibility

> **Full name:** `api.LayerVisibility` · **Kind:** `IntEnum`

Visibility of a layer (as shown in the Navigation palette).

| Member | Value | Description |
|---|---|---|
| `Invisible` | `-1` | Hidden. |
| `Normal` | `0` | Shown normally. |
| `Grayed` | `2` | Shown, but drawn in gray to indicate it is not the active layer. |

### VisibilityOptions

> **Full name:** `api.VisibilityOptions` · **Kind:** `IntEnum`

How layers or classes other than the active one are shown. Used by `Document.SetLayerOptions` and `Document.SetClassOptions`.

| Member | Value | Description |
|---|---|---|
| `ActiveOnly` | `1` | Show only the active layer/class. |
| `GrayOthers` | `2` | Show others grayed out (not editable, not snappable). |
| `ShowOthers` | `3` | Show others normally (visible, but not editable, not snappable). |
| `ShowSnapOthers` | `4` | Show others normally and allow snapping to them (still not editable). |
| `ShowSnapModifyOthers` | `5` | Show others normally, allow snapping and editing them. |
| `GraySnapOthers` | `6` | Show others grayed but allow snapping to them. |

### StoryElevationChangeMode

> **Full name:** `api.StoryElevationChangeMode` · **Kind:** `IntEnum`

Which stories `Story.SetElevation` moves (the choices of the Change Story Elevation dialog box). Every moved story moves by the same distance, and its design layers move with it.

| Member | Value | Description |
|---|---|---|
| `Single` | `0` | Only this story. |
| `CurrentAndAbove` | `1` | This story and every story above it. |
| `CurrentAndBelow` | `2` | This story and every story below it. |
| `All` | `3` | Every story of the document. |

### UndoMethod

> **Full name:** `api.UndoMethod` · **Kind:** `IntEnum`

Undo method passed to `Document.StartUndoEvent`.

| Member | Value | Description |
|---|---|---|
| `None_` | `0` | Disables undo and clears the undo table for the operation (use sparingly). |
| `ReplaceSelection` | `17` | Remembers the current selection; Undo restores it. |
| `SwapObjects` | `21` | Object level undo: register the objects you create / modify / delete - the usual choice. |

### AngularUnit

> **Full name:** `api.AngularUnit` · **Kind:** `IntEnum`

Unit in which angles are displayed (`UnitSettings.GetAngularUnit`).

| Member | Value | Description |
|---|---|---|
| `Degrees` | `0` |  |
| `Radians` | `1` |  |
| `Gradians` | `2` |  |

### TextJustification

> **Full name:** `api.TextJustification` · **Kind:** `IntEnum`

Horizontal justification of new text (`TextDefaults`).

| Member | Value | Description |
|---|---|---|
| `Left` | `1` |  |
| `Center` | `2` |  |
| `Right` | `3` |  |

### TextVerticalAlignment

> **Full name:** `api.TextVerticalAlignment` · **Kind:** `IntEnum`

Vertical alignment of new text (`TextDefaults`).

| Member | Value | Description |
|---|---|---|
| `TopOfBox` | `1` |  |
| `TopBaseline` | `2` |  |
| `CenterOfBox` | `3` |  |
| `BottomBaseline` | `4` |  |
| `BottomOfBox` | `5` |  |

### TextLineSpacing

> **Full name:** `api.TextLineSpacing` · **Kind:** `IntEnum`

Line spacing of new text (`TextDefaults`); `Custom` uses the leading of `TextDefaults.GetLeading`.

| Member | Value | Description |
|---|---|---|
| `Custom` | `0` | See `TextDefaults.GetLeading`. |
| `Single` | `2` |  |
| `OneAndHalf` | `3` |  |
| `Double` | `4` |  |

---

[Back to the index](README.md) · [Back to top](#documentaccess--document-layers-stories-and-preferences)
