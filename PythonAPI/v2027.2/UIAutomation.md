**English** • [Deutsch](../../PythonAPI.de/v2027.2/UIAutomation.md) • [日本語](../../PythonAPI.ja/v2027.2/UIAutomation.md)

# UIAutomation — tools, the Tool bar, menus and the Object Info palette

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The user interface automation classes. `ToolAccess` is the tool catalogue (activate tools), `ModeBar` reads and changes the modes of the active tool and `ToolControl` drives the active tool with clicks, drags, mouse moves and keys. `MenuAccess` lists and executes menu commands and chunk items. `OIPAccess` lists, reads and operates the controls the Object Info palette shows for the selection.

Conventions: getters return `None` when a value cannot be obtained, setters/actions return `True` on success; name comparisons are case-insensitive; all indexes are 0-based, mode indexes and chunk item indexes included. Operating the user interface behaves exactly like user input: tools may rebuild their Tool bar (mode bar), commands show their dialogs and set up their own undo, Object Info palette changes rebuild the palette — re-read values after a change instead of caching them, and do not execute menu commands inside an undo event opened with `Document.StartUndoEvent`.

Built-in tools and commands use a negative number as universal name (for example "-207"); for those the English name is accepted as well. Model coordinates are world units; view coordinates are pixels from the top-left corner of the view pane (y grows downwards).

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [Point3D](#point3d)
  - [ViewPoint](#viewpoint)
  - [ViewSize](#viewsize)
  - [ToolPoint](#toolpoint)
  - [ModeButtonDefinition](#modebuttondefinition)
  - [Tool](#tool)
  - [ModeChoice](#modechoice)
  - [ToolMode](#toolmode)
  - [ModeSetting](#modesetting)
  - [ModeBar](#modebar)
  - [ToolControl](#toolcontrol)
  - [ToolAccess](#toolaccess)
  - [MenuCommand](#menucommand)
  - [MenuChunkItem](#menuchunkitem)
  - [MenuEntry](#menuentry)
  - [MenuAccess](#menuaccess)
  - [OIPControl](#oipcontrol)
  - [OIPSetting](#oipsetting)
  - [OIPAccess](#oipaccess)
- [Enumerations](#enumerations)
  - [ToolKind](#toolkind)
  - [ToolCreationType](#toolcreationtype)
  - [ToolFilter](#toolfilter)
  - [ModeType](#modetype)
  - [ModeButtonKind](#modebuttonkind)
  - [ToolKey](#toolkey)
  - [MenuCommandKind](#menucommandkind)
  - [MenuChunkKind](#menuchunkkind)
  - [MenuFilter](#menufilter)
  - [MenuEntryType](#menuentrytype)
  - [MenuStatus](#menustatus)
  - [OIPPane](#oippane)
  - [OIPControlType](#oipcontroltype)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`Point3D`](#point3d) | class |  | 3D point in world coordinates. |
| [`ViewPoint`](#viewpoint) | class |  | Point in view coordinates, in pixels (16-bit coordinates). |
| [`ViewSize`](#viewsize) | class |  | Size of the active view pane in pixels. |
| [`ToolPoint`](#toolpoint) | class |  | One point entered into the active tool, as the tool receives it. |
| [`ModeButtonDefinition`](#modebuttondefinition) | class |  | A mode button as declared by a tool (static information, available without activating the tool). |
| [`Tool`](#tool) | class |  | Description of one tool. |
| [`ModeChoice`](#modechoice) | class |  | One choice of a mode group: a radio button, the single button of a Button/Toggle group, or an item of a PullDown / ComboBox / SearchablePullDown group. |
| [`ToolMode`](#toolmode) | class |  | Live state of one mode group of the active tool. |
| [`ModeSetting`](#modesetting) | class |  | A mode change request used by the generic, text based mode API (see `ModeBar.SetMode`). |
| [`ModeBar`](#modebar) | class |  | Stateless view over the Tool bar (mode bar) of the active tool. |
| [`ToolControl`](#toolcontrol) | class |  | Stateless driver of the active tool. |
| [`ToolAccess`](#toolaccess) | class |  | Stateless facade over the Vectorworks tool system. |
| [`MenuCommand`](#menucommand) | class |  | Description of one installed menu command. |
| [`MenuChunkItem`](#menuchunkitem) | class |  | One current item of a chunk. |
| [`MenuEntry`](#menuentry) | class |  | One entry of a menu of the menu bar, as the current workspace defines it. |
| [`MenuAccess`](#menuaccess) | class |  | Stateless facade over the Vectorworks menu system. |
| [`OIPControl`](#oipcontrol) | class |  | Description and live state of one OIP control. |
| [`OIPSetting`](#oipsetting) | class |  | A control change request used by the generic, text based API (see `OIPAccess.SetValue`). |
| [`OIPAccess`](#oipaccess) | class |  | Stateless facade over the Object Info palette. |
| [`ToolKind`](#toolkind) | IntEnum |  | How a tool is provided. |
| [`ToolCreationType`](#toolcreationtype) | IntEnum |  | What kind of interaction the tool uses to create objects. |
| [`ToolFilter`](#toolfilter) | IntEnum |  | Which tools `ToolAccess.GetTools` returns. |
| [`ModeType`](#modetype) | IntEnum |  | Kind of a mode group on the Tool bar of the active tool. |
| [`ModeButtonKind`](#modebuttonkind) | IntEnum |  | Kind of a mode button as declared by a tool when it is registered (may differ from the live ModeType). |
| [`ToolKey`](#toolkey) | IntEnum |  | Keys that tools react to while points are being entered (see `ToolControl.PressKey`). |
| [`MenuCommandKind`](#menucommandkind) | IntEnum |  | How a menu command is provided. |
| [`MenuChunkKind`](#menuchunkkind) | IntEnum |  | Kind of a chunk (see "Chunk" above). |
| [`MenuFilter`](#menufilter) | IntEnum |  | Which menu commands `MenuAccess.GetMenuCommands` returns. |
| [`MenuEntryType`](#menuentrytype) | IntEnum |  | Kind of an entry of a menu of the menu bar. |
| [`MenuStatus`](#menustatus) | IntEnum |  | Whether a menu command (or chunk item) can be executed now, and why not (see `MenuAccess.GetMenuStatus`). |
| [`OIPPane`](#oippane) | IntEnum |  | Pane (tab) of the Object Info palette. |
| [`OIPControlType`](#oipcontroltype) | IntEnum |  | Kind of an OIP control. |

## Classes

### Point3D

> **Full name:** `api.Point3D` · **Inherits:** `api.Object`

3D point in world coordinates.

**Constructors**

| Constructor | Description |
|---|---|
| `Point3D()` | Default value (fields at their defaults). |
| `Point3D(x, y, z)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: Point3D) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: Point3D) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `x` | `float` | X coordinate (world units). |
| `y` | `float` | Y coordinate (world units). |
| `z` | `float` | Z coordinate (world units). |

### ViewPoint

> **Full name:** `api.ViewPoint` · **Inherits:** `api.Object`

Point in view coordinates, in pixels (16-bit coordinates).

**Constructors**

| Constructor | Description |
|---|---|
| `ViewPoint()` | Default value (fields at their defaults). |
| `ViewPoint(x, y)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `==` | `__eq__(o: ViewPoint) -> bool` | `a == b`: True when the two values are equal. |
| `!=` | `__ne__(o: ViewPoint) -> bool` | `a != b`: True when the two values differ. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `x` | `int` | Horizontal pixel position from the left of the active view pane. |
| `y` | `int` | Vertical pixel position from the top of the active view pane (grows downwards). |

### ViewSize

> **Full name:** `api.ViewSize` · **Inherits:** `api.Object`

Size of the active view pane in pixels.

**Constructors**

| Constructor | Description |
|---|---|
| `ViewSize()` | Default value (fields at their defaults). |
| `ViewSize(fWidth, fHeight)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fWidth` | `int` | Width of the active view pane in pixels. |
| `fHeight` | `int` | Height of the active view pane in pixels. |

### ToolPoint

> **Full name:** `api.ToolPoint` · **Inherits:** `api.Object`

One point entered into the active tool, as the tool receives it.

**Constructors**

| Constructor | Description |
|---|---|
| `ToolPoint()` | Default value (fields at their defaults). |
| `ToolPoint(fPoint2D, fPoint3D, fViewPoint)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fPoint2D` | `Math.Point2D` | Screen plane point for 2D tools (rotated with the plan), working plane point for 3D tools. |
| `fPoint3D` | `Point3D` | Model point. |
| `fViewPoint` | `ViewPoint` | View position of the click. |

### ModeButtonDefinition

> **Full name:** `api.ModeButtonDefinition` · **Inherits:** `api.Object`

A mode button as declared by a tool (static information, available without activating the tool). Only tools that declare their Tool bar buttons provide these.

**Constructors**

| Constructor | Description |
|---|---|
| `ModeButtonDefinition()` | Default value (fields at their defaults). |
| `ModeButtonDefinition(fName, fHelpText, fKind)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fName` | `str` | Name of the button. |
| `fHelpText` | `str` | Help text of the button. |
| `fKind` | `ModeButtonKind` | Kind of button. |

### Tool

> **Full name:** `api.Tool` · **Inherits:** `api.Object`

Description of one tool.

**Constructors**

| Constructor | Description |
|---|---|
| `Tool()` | Default value (fields at their defaults). |
| `Tool(fUniversalName, fName, fDisplayName, fCategory, fHelpText, fShortcut, fKind, fCreationType, fIsInWorkspace, fCanActivate, fIsActive, fModeButtons)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fUniversalName` | `str` | Unique identity; pass it to ActivateTool / FindTool. |
| `fName` | `str` | User friendly English name (equals fUniversalName for plug-in tools). |
| `fDisplayName` | `str` | Localized name shown in the tool palette. |
| `fCategory` | `str` | Plug-in category (empty for most built-in tools). |
| `fHelpText` | `str` | Short description of the tool. |
| `fShortcut` | `str` | Keyboard shortcut in the current workspace (may be empty). |
| `fKind` | `ToolKind` | Kind of tool. |
| `fCreationType` | `ToolCreationType` | How the tool creates objects. |
| `fIsInWorkspace` | `bool` | Placed in a tool palette of the current workspace. |
| `fCanActivate` | `bool` | ActivateTool can activate it now. |
| `fIsActive` | `bool` | Currently the active tool. |
| `fModeButtons` | `list[ModeButtonDefinition]` | Declared mode buttons (see ModeButtonDefinition). |

### ModeChoice

> **Full name:** `api.ModeChoice` · **Inherits:** `api.Object`

One choice of a mode group: a radio button, the single button of a Button/Toggle group, or an item of a PullDown / ComboBox / SearchablePullDown group.

**Constructors**

| Constructor | Description |
|---|---|
| `ModeChoice()` | Default value (fields at their defaults). |
| `ModeChoice(fName, fHelpText, fImage, fId)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fName` | `str` | Mode name or item text (may be empty for unnamed buttons of built-in tools). |
| `fHelpText` | `str` | Tooltip text (buttons only). |
| `fImage` | `str` | Image resource specifier (buttons only), e.g. "Vectorworks/ModeViewBar/Options.png". |
| `fId` | `str` | Item id (SearchablePullDown only). |

### ToolMode

> **Full name:** `api.ToolMode` · **Inherits:** `api.Object`

Live state of one mode group of the active tool.

**Constructors**

| Constructor | Description |
|---|---|
| `ToolMode()` | Default value (fields at their defaults). |
| `ToolMode(fIndex, fType, fIsEnabled, fLabel, fChoices, fChoiceCount, fSelectedChoice, fIsOn, fValue)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fIndex` | `int` | Position on the Tool bar (0-based). |
| `fType` | `ModeType` | Type of the mode group (radio, button, toggle, pull-down, ...). |
| `fIsEnabled` | `bool` | Whether the mode group is enabled. |
| `fLabel` | `str` | Label of the control, or the mode name for unlabelled buttons. |
| `fChoices` | `list[ModeChoice]` | See ModeChoice; empty for EditText and ResourcePopup. |
| `fChoiceCount` | `int` | Total number of choices (fChoices may be truncated). |
| `fSelectedChoice` | `int \| None` | Radio, PullDown, ComboBox, SearchablePullDown. |
| `fIsOn` | `bool \| None` | Toggle. |
| `fValue` | `str` | Current value as text (see `ModeBar.GetModeValue`). |

### ModeSetting

> **Full name:** `api.ModeSetting` · **Inherits:** `api.Object`

A mode change request used by the generic, text based mode API (see `ModeBar.SetMode`).

**Constructors**

| Constructor | Description |
|---|---|
| `ModeSetting()` | Default value (fields at their defaults). |
| `ModeSetting(fModeIndex, fValue)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fModeIndex` | `int` | Index of the mode group (0-based). |
| `fValue` | `str` | Value, interpreted like `ModeBar.SetMode`. |

### ModeBar

> **Full name:** `api.ModeBar` · **Inherits:** `api.Object`

Stateless view over the Tool bar (mode bar) of the active tool. Obtain it with `ToolAccess.ModeBar()`. Every method requires an open document (`Document.IsOpen()`).

Two ways of changing modes:

- typed: — SelectRadio, PressButton, SetToggle, SelectItem, SetText, SelectResource
- generic: SetMode(index, "text") interprets the text according to the mode type, and SelectChoice(index, n) picks the n-th choice of any mode type.

Disabled modes cannot be changed. Changes are applied exactly as user interaction on the Tool bar.

**Constructors**

| Constructor | Description |
|---|---|
| `ModeBar()` | Stateless view of the Tool bar of the active tool (same as `ToolAccess().ModeBar()`). |

**Methods**

*Reading*

| Method | Description |
|---|---|
| `GetModeCount() -> int` | Number of mode items. |
| `GetModes(maxChoices: int = 2**64 - 1) -> list[ToolMode]` | MaxChoices limits fChoices of every mode (fChoiceCount always holds the full count). |
| `GetMode(modeIndex: int, maxChoices: int = 2**64 - 1) -> ToolMode \| None` | Returns the mode for `modeIndex`, `maxChoices`. |
| `GetModeType(modeIndex: int) -> ModeType \| None` | Returns the mode type at `modeIndex`. |
| `FindMode(name: str) -> int \| None` | Index of the first mode whose label or one of whose choices matches `name` (case-insensitive). |
| `GetModeValue(modeIndex: int) -> str \| None` | Current value as text:<br>• Radio — name of the selected button (or its index when unnamed), Toggle - "on"/"off", Button - empty,<br>• PullDown/SearchablePullDown — selected item text, EditText/ComboBox - field text,<br>• ResourcePopup — selected resource name. |

*Typed changes*

| Method | Description |
|---|---|
| `SelectRadio(modeIndex: int, choiceIndex: int) -> bool` | Selects the button `choiceIndex` of the radio group mode `modeIndex`. |
| `PressButton(modeIndex: int) -> bool` | Presses the push button mode `modeIndex`. |
| `SetToggle(modeIndex: int, isOn: bool) -> bool` | Sets the toggle at `modeIndex`. |
| `SelectItem(modeIndex: int, itemIndex: int) -> bool` | Selects the item `itemIndex` of the pull-down, combo box or searchable pull-down mode `modeIndex`. |
| `SelectItem(modeIndex: int, itemNameOrId: str) -> bool` | PullDown, ComboBox or SearchablePullDown: matches the item text, or the item id for SearchablePullDown. |
| `SetText(modeIndex: int, text: str) -> bool` | EditText or ComboBox. |

*ResourcePopup*

| Method | Description |
|---|---|
| `SelectResource(modeIndex: int, resourceName: str) -> bool` | Selects the resource by name without showing the pop-up. |

*Generic changes*

| Method | Description |
|---|---|
| `SelectChoice(modeIndex: int, choiceIndex: int) -> bool` | Picks the n-th choice: Radio - button n, Button - press (n ignored), Toggle - n != 0 means on, PullDown/ComboBox/SearchablePullDown - item n. Not supported for EditText and ResourcePopup. |
| `SetMode(modeIndex: int, value: str) -> bool` | Interprets `value` according to the mode type:<br>• Radio — button name, image specifier or 0-based index<br>• Button — presses the button (value ignored)<br>• Toggle — "on"/"off", "True"/"False", "yes"/"no", "1"/"0" or "toggle"<br>• PullDown — item text or 0-based index<br>• SearchablePullDown — item text, item id or 0-based index<br>• ComboBox — item text, otherwise the text is entered into the field<br>• EditText — the text to enter<br>• ResourcePopup — resource name. |
| `SetModes(settings: list[ModeSetting]) -> bool` | Applies the settings in order; stops at the first failure and returns `False`. |

### ToolControl

> **Full name:** `api.ToolControl` · **Inherits:** `api.Object`

Stateless driver of the active tool. Obtain it with `ToolAccess.Control()` after activating a tool. Every input is processed exactly like real mouse and keyboard input, so the active tool behaves as if the user had operated it (previews, undo, dialogs the tool shows on completion, ...).

Coordinates:

- Model coordinates (`Math.Point2D`, `Point3D`) are applied exactly: SmartCursor snapping is suspended and the tool receives the given point, also when it is not visible. 2D points lie on the layer plane (z = 0). Tools that pick objects under the cursor (selection, reshape, ...) additionally need the point to be visible in the active pane (see `ModelToView`); otherwise the pointer is placed at the pane center.
- View coordinates (`ViewPoint`) behave like a real click at that pixel, including SmartCursor snapping. They must lie inside the active pane (see `GetViewSize`).

Typical use (two clicks draw a rectangle in click-click mode):

```python
import api
from api.Math import Point2D

tools = api.ToolAccess()
if tools.ActivateTool("Rectangle"):
    control = tools.Control()
    control.Click(Point2D(0.0, 0.0))
    control.Click(Point2D(1000.0, 500.0))
```

Multi-point tools (such as the Polyline and Wall tools) are completed with `Finish()` or a `DoubleClick` on the last point.

**Constructors**

| Constructor | Description |
|---|---|
| `ToolControl()` | Stateless driver of the active tool (same as `ToolAccess().Control()`). |

**Methods**

*General*

| Method | Description |
|---|---|
| `IsAvailable() -> bool` *static* | Whether there is an active view pane that can receive input. |

*Tool points*

| Method | Description |
|---|---|
| `GetToolPointCount() -> int` | Points entered into the active tool so far; empty when the tool is idle. |
| `GetToolPoints() -> list[ToolPoint]` | Returns the tool points. |
| `GetCurrentPoint() -> ToolPoint \| None` | Current (hover) point of the active tool. |
| `IsToolInProgress() -> bool` | True when the active tool has points entered (a tool action is in progress). |

*Coordinates*

| Method | Description |
|---|---|
| `GetViewSize() -> ViewSize \| None` | Returns the view size. |
| `ModelToView(modelPoint: Math.Point2D) -> ViewPoint \| None` | View position of a model point; `None` when it is outside the active pane. |
| `ModelToView(modelPoint: Point3D) -> ViewPoint \| None` | View position of a model point; `None` when it is outside the active pane. |
| `ViewToModel(viewPoint: ViewPoint) -> Math.Point2D \| None` | 2D model point under a view position (on the layer plane in Top/Plan, on the screen plane otherwise). |

*Pointer input*

| Method | Description |
|---|---|
| `MoveTo(modelPoint: Math.Point2D) -> bool` | Moves the pointer without clicking; tools update their preview (rubber band) to the new position. |
| `MoveTo(modelPoint: Point3D) -> bool` | Moves the pointer without clicking; tools update their preview (rubber band) to the new position. |
| `MoveTo(viewPoint: ViewPoint) -> bool` | Moves the pointer without clicking; tools update their preview (rubber band) to the new position. |
| `Click(modelPoint: Math.Point2D) -> bool` | Left click (mouse down + mouse up) - usually adds one tool point. |
| `Click(modelPoint: Point3D) -> bool` | Left click (mouse down + mouse up) - usually adds one tool point. |
| `Click(viewPoint: ViewPoint) -> bool` | Left click (mouse down + mouse up) - usually adds one tool point. |
| `DoubleClick(modelPoint: Math.Point2D) -> bool` | Double click - completes multi point tools or edits the object under the pointer (Selection tool). |
| `DoubleClick(modelPoint: Point3D) -> bool` | Double click - completes multi point tools or edits the object under the pointer (Selection tool). |
| `DoubleClick(viewPoint: ViewPoint) -> bool` | Double click - completes multi point tools or edits the object under the pointer (Selection tool). |
| `Drag(from_: Math.Point2D, to: Math.Point2D) -> bool` | Mouse down at `from`, move, mouse up at `to` (click-drag drawing mode, marquee selection, dragging objects). |
| `Drag(from_: Point3D, to: Point3D) -> bool` | Mouse down at `from`, move, mouse up at `to` (click-drag drawing mode, marquee selection, dragging objects). |
| `Drag(from_: ViewPoint, to: ViewPoint) -> bool` | Mouse down at `from`, move, mouse up at `to` (click-drag drawing mode, marquee selection, dragging objects). |

*Keyboard and tool actions*

| Method | Description |
|---|---|
| `PressKey(key: ToolKey) -> bool` | Sends the key exactly like the user pressing it over the drawing. |
| `Finish() -> bool` | Completes the current tool action (Return key). |
| `Cancel() -> bool` | Removes all tool points and restarts the tool action; does not change the selection. |
| `RemoveLastPoint() -> bool` | Removes the most recent tool point. |

### ToolAccess

> **Full name:** `api.ToolAccess` · **Inherits:** `api.Object`

Stateless facade over the Vectorworks tool system. Construct it on demand:

```python
import api

tools = api.ToolAccess()
for tool in tools.GetTools(api.ToolFilter.Activatable):   # what can be used now
    print(tool.fUniversalName, tool.fName)
if tools.ActivateTool("Rectangle"):                     # universal or friendly name
    for mode in tools.ModeBar().GetModes():            # inspect the mode bar
        print(mode)
    tools.ModeBar().SetMode(0, "Rotated Rectangle Mode")   # change a mode generically
```

**Constructors**

| Constructor | Description |
|---|---|
| `ToolAccess()` | Stateless facade over the tool system. |

**Methods**

*General*

| Method | Description |
|---|---|
| `IsAvailable() -> bool` *static* | Whether tools can be activated and modes changed (requires an open document). |

*Catalogue*

| Method | Description |
|---|---|
| `GetTools(filter: ToolFilter = ToolFilter.All) -> list[Tool]` | Returns the tools for `filter`. |
| `FindTool(name: str) -> Tool \| None` | Looks a tool up by universal name, user friendly name or localized display name (in this order of preference). |
| `IsToolInWorkspace(name: str) -> bool` | True when the tool `name` is placed in a tool palette of the current workspace. |
| `CanActivateTool(name: str) -> bool` | True when `ActivateTool(name)` can activate the tool now. |

*Active tool*

| Method | Description |
|---|---|
| `GetActiveTool() -> Tool \| None` | Returns the active tool. |
| `GetActiveToolUniversalName() -> str \| None` | Returns the active tool universal name. |
| `IsToolActive(name: str) -> bool` | True when the tool `name` is the active tool. |
| `GetActiveToolHelpMessage() -> str \| None` | Instruction text the active tool currently shows to the user (e.g. "Click to set the start point"). |

*Activation*

| Method | Description |
|---|---|
| `ActivateTool(name: str) -> bool` | Activates the tool `name` (universal, friendly or display name). |
| `ActivateTool(name: str, modeSettings: list[ModeSetting]) -> bool` | Activates the tool, then applies the mode settings (see `ModeBar.SetModes`). |
| `ActivateTool(name: str, modeIndex: int, choiceIndex: int) -> bool` | Activates the tool, then picks the n-th choice of a mode (see `ModeBar.SelectChoice`). |
| `ActivateSelectionTool() -> bool` | Returns to the default Selection tool. |

*Modes*

| Method | Description |
|---|---|
| `ModeBar() -> ModeBar` | The Tool bar of the active tool. |

*Input*

| Method | Description |
|---|---|
| `Control() -> ToolControl` | The driver of the active tool (clicks, drags, keys). |

### MenuCommand

> **Full name:** `api.MenuCommand` · **Inherits:** `api.Object`

Description of one installed menu command.

**Constructors**

| Constructor | Description |
|---|---|
| `MenuCommand()` | Default value (fields at their defaults). |
| `MenuCommand(fUniversalName, fName, fDisplayName, fCategory, fHelpText, fShortcut, fKind, fIsChunk, fIsInWorkspace, fIsEnabled)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fUniversalName` | `str` | Unique identity; pass it to ExecuteMenu / FindMenuCommand. |
| `fName` | `str` | User friendly English name (equals fUniversalName for plug-in commands). |
| `fDisplayName` | `str` | Localized title shown in the menus. |
| `fCategory` | `str` | Category of the command in the Workspace Editor. |
| `fHelpText` | `str` | Short description of the command. |
| `fShortcut` | `str` | Keyboard shortcut in the current workspace (may be empty). |
| `fKind` | `MenuCommandKind` | Kind of command (normal command or chunk). |
| `fIsChunk` | `bool` | Provides a group of items (see `MenuAccess.GetChunkItems`). |
| `fIsInWorkspace` | `bool` | Placed in the menus of the current workspace. |
| `fIsEnabled` | `bool` | ExecuteMenu can run it now (a chunk: at least one of its items). |

### MenuChunkItem

> **Full name:** `api.MenuChunkItem` · **Inherits:** `api.Object`

One current item of a chunk.

**Constructors**

| Constructor | Description |
|---|---|
| `MenuChunkItem()` | Default value (fields at their defaults). |
| `MenuChunkItem(fIndex, fText, fIsEnabled, fIsChecked)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fIndex` | `int` | Position in the chunk (0-based). |
| `fText` | `str` | Item text as the menu shows it. |
| `fIsEnabled` | `bool` | ExecuteMenu can run it now. |
| `fIsChecked` | `bool` | The menu shows a check mark (always `False` on Mac: the shell does not report it). |

### MenuEntry

> **Full name:** `api.MenuEntry` · **Inherits:** `api.Object`

One entry of a menu of the menu bar, as the current workspace defines it.

**Constructors**

| Constructor | Description |
|---|---|
| `MenuEntry()` | Default value (fields at their defaults). |
| `MenuEntry(fType, fMenuPath, fText, fUniversalName, fChunkKind, fChunkItemIndex, fShortcut, fIsEnabled, fIsChecked)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fType` | `MenuEntryType` | Kind of entry (command, chunk item, submenu or separator). |
| `fMenuPath` | `list[str]` | Titles of the menus containing the entry, from the menu bar down (e.g. {"File", "Export"}). |
| `fText` | `str` | Title shown in the menu (empty for separators). |
| `fUniversalName` | `str` | Command, ChunkItem: universal name of the command or the chunk. |
| `fChunkKind` | `MenuChunkKind` | ChunkItem: kind of the chunk. |
| `fChunkItemIndex` | `int \| None` | ChunkItem: index of the item in the chunk. |
| `fShortcut` | `str` | Keyboard shortcut (may be empty). |
| `fIsEnabled` | `bool` | Command, ChunkItem: ExecuteMenuEntry can run it now. |
| `fIsChecked` | `bool` | Command, ChunkItem: the menu shows a check mark (see `MenuChunkItem.fIsChecked`). |

### MenuAccess

> **Full name:** `api.MenuAccess` · **Inherits:** `api.Object`

Stateless facade over the Vectorworks menu system. Construct it on demand:

```python
import api

menus = api.MenuAccess()
for entry in menus.GetMenuEntries("Modify"):          # what the Modify menu offers
    print(entry)
if menus.GetMenuStatus("Select All") == api.MenuStatus.Ready:   # universal, friendly or display name
    menus.ExecuteMenu("Select All")
for item in menus.GetChunkItems("Recent Docs"):      # current items of a chunk
    print(item)
menus.ExecuteMenu("Standard Views", "Top/Plan")           # a chunk item by its text
```

**Constructors**

| Constructor | Description |
|---|---|
| `MenuAccess()` | Stateless facade over the menu system. |

**Methods**

*General*

| Method | Description |
|---|---|
| `IsAvailable() -> bool` *static* | Whether menu commands can be executed now: the menu bar is set up and no plug-in object is being regenerated. |

*Catalogue*

| Method | Description |
|---|---|
| `GetMenuCommands(filter: MenuFilter = MenuFilter.All) -> list[MenuCommand]` | Returns the menu commands for `filter`. |
| `FindMenuCommand(name: str) -> MenuCommand \| None` | Looks a command up by universal name, user friendly name or localized display name (in this order of preference). On equal preference a command placed in the workspace wins. |
| `IsMenuCommandInWorkspace(name: str) -> bool` | True when the command `name` is placed in the menus of the current workspace. |

*Menu bar of the current workspace*

| Method | Description |
|---|---|
| `GetMenuTitles() -> list[str]` | Titles of the menus of the menu bar, from left to right. |
| `GetMenuEntries() -> list[MenuEntry]` | Every entry of the menu bar, depth first in menu order: a Submenu entry is followed by the entries of its submenu, and chunks are expanded into their current items. |
| `GetMenuEntries(menuTitle: str) -> list[MenuEntry]` | The entries of one menu of the menu bar (see GetMenuTitles), including its submenus. |
| `FindMenuEntry(path: list[str]) -> MenuEntry \| None` | The entry whose menu path and text equal `path`, e.g. {"Modify", "Align", "Align Left"}. |

*Chunks*

| Method | Description |
|---|---|
| `GetChunkItems(name: str) -> list[MenuChunkItem]` | Current items of a chunk placed in the workspace, as the menu bar shows them (see "Chunk" above). Separators and placeholders without text are left out (fIndex keeps the position of the items). Empty when `name` is not a chunk placed in the workspace. |
| `FindChunkItem(name: str, itemText: str) -> int \| None` | Index of the chunk item whose text matches `itemText`. |

*Execution*

| Method | Description |
|---|---|
| `GetMenuStatus(name: str) -> MenuStatus` | Whether ExecuteMenu would run the command (or the chunk item) now, and why not. Without an index a chunk is accepted when it has exactly one item. |
| `GetMenuStatus(name: str, chunkItemIndex: int) -> MenuStatus` | Whether ExecuteMenu would run the command (or the chunk item) now, and why not. Without an index a chunk is accepted when it has exactly one item. |
| `CanExecuteMenu(name: str) -> bool` | True when `ExecuteMenu(name)` can run the command now. |
| `ExecuteMenu(name: str) -> bool` | Executes a normal command, or the only item of a chunk. Use GetMenuStatus to learn why it did not run. |
| `ExecuteMenu(name: str, chunkItemIndex: int) -> bool` | Executes an item of a chunk, given by index or by text. |
| `ExecuteMenu(name: str, chunkItemText: str) -> bool` | Executes an item of a chunk, given by index or by text. |
| `ExecuteMenuEntry(entry: MenuEntry) -> bool` | Executes a Command or ChunkItem entry of GetMenuEntries. |

### OIPControl

> **Full name:** `api.OIPControl` · **Inherits:** `api.Object`

Description and live state of one OIP control.

**Constructors**

| Constructor | Description |
|---|---|
| `OIPControl()` | Default value (fields at their defaults). |
| `OIPControl(fId, fPane, fType, fCoreTypeId, fParentId, fLabel, fValue, fChoices, fChoiceCount, fSelectedChoice, fIsChecked, fIsEnabled, fIsVisible, fIsReadOnly, fIsIndeterminate)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fId` | `int` | Control id; valid until the OIP is rebuilt. |
| `fPane` | `OIPPane` | Pane of the control. |
| `fType` | `OIPControlType` | Type of the control. |
| `fCoreTypeId` | `int` | Internal type id of the control (for diagnostics). |
| `fParentId` | `int` | Id of the parent control (0 when none). |
| `fLabel` | `str` | Prompt / label shown next to the control. |
| `fValue` | `str` | Current value as text (see `OIPAccess.GetValue`). |
| `fChoices` | `list[str]` | RadioGroup, PullDown, ClassPullDown, LayerPullDown. |
| `fChoiceCount` | `int` | Total number of choices (fChoices may be truncated). |
| `fSelectedChoice` | `int \| None` | RadioGroup, PullDown, SearchablePullDown, ClassPullDown, LayerPullDown. |
| `fIsChecked` | `bool \| None` | CheckBox (empty when indeterminate). |
| `fIsEnabled` | `bool` | Whether the control is enabled. |
| `fIsVisible` | `bool` | Whether the control is visible. |
| `fIsReadOnly` | `bool` | EditText that only displays a value. |
| `fIsIndeterminate` | `bool` | Multiple selection with different values. |

### OIPSetting

> **Full name:** `api.OIPSetting` · **Inherits:** `api.Object`

A control change request used by the generic, text based API (see `OIPAccess.SetValue`).

**Constructors**

| Constructor | Description |
|---|---|
| `OIPSetting()` | Default value (fields at their defaults). |
| `OIPSetting(fPane, fControlId, fValue)` | Field values: all fields positionally (in this order) or any of them as keywords. |

**Fields**

| Field | Type | Description |
|---|---|---|
| `fPane` | `OIPPane` | Pane of the control. |
| `fControlId` | `int` | ID of the control. |
| `fValue` | `str` | Value, interpreted like `OIPAccess.SetValue`. |

### OIPAccess

> **Full name:** `api.OIPAccess` · **Inherits:** `api.Object`

Stateless facade over the Object Info palette. Construct it on demand:

```python
import api

oip = api.OIPAccess()
for control in oip.GetControls(api.OIPPane.Shape):     # what the OIP shows now
    print(control)
control_id = oip.FindControl(api.OIPPane.Shape, "Width")   # find a control by its label
if control_id is not None:
    oip.SetValue(api.OIPPane.Shape, control_id, "200")     # change it as the user would
```

Two ways of changing controls:

- typed: `SetText`, `SetChecked`, `SelectChoice`, `PressButton`
- generic: `SetValue(pane, id, "text")` interprets the text according to the control type.

Disabled, hidden and read only controls cannot be changed.

**Constructors**

| Constructor | Description |
|---|---|
| `OIPAccess()` | Stateless facade over the Object Info palette. |

**Methods**

*General*

| Method | Description |
|---|---|
| `IsAvailable() -> bool` *static* | Whether the OIP can be accessed (requires an open document). |
| `IsPaneAvailable(pane: OIPPane) -> bool` | Whether the pane currently shows controls (requires a selection, or document defaults for some panes). |

*Reading*

| Method | Description |
|---|---|
| `GetControls(pane: OIPPane = OIPPane.Shape, maxChoices: int = 2**64 - 1, includeHidden: bool = False) -> list[OIPControl]` | Controls of the pane in id order. maxChoices limits fChoices of every control (fChoiceCount always holds the full count). Hidden controls are skipped unless includeHidden is `True`. |
| `GetControl(pane: OIPPane, controlId: int, maxChoices: int = 2**64 - 1) -> OIPControl \| None` | Returns the control for `pane`, `controlId`, `maxChoices`. |
| `FindControl(pane: OIPPane, label: str) -> int \| None` | Id of the first visible control whose label matches `label` (case-insensitive; a trailing ':' is ignored). |
| `GetValue(pane: OIPPane, controlId: int) -> str \| None` | Current value as text:<br>• EditText — field text, StaticText - label, CheckBox - "on"/"off" (empty when indeterminate), Button - empty,<br>• RadioGroup/PullDown/SearchablePullDown/ClassPullDown/LayerPullDown — selected item text, Other - empty. |

*EditText*

| Method | Description |
|---|---|
| `SetText(pane: OIPPane, controlId: int, text: str) -> bool` | The text is entered as the user would type it (units and math are evaluated by Vectorworks). |
| `SetChecked(pane: OIPPane, controlId: int, isChecked: bool) -> bool` | Sets the checked. |
| `SelectChoice(pane: OIPPane, controlId: int, choiceIndex: int) -> bool` | RadioGroup, PullDown, SearchablePullDown, ClassPullDown, LayerPullDown. |
| `SelectChoice(pane: OIPPane, controlId: int, choiceName: str) -> bool` | RadioGroup, PullDown, SearchablePullDown, ClassPullDown, LayerPullDown. |

*Button*

| Method | Description |
|---|---|
| `PressButton(pane: OIPPane, controlId: int) -> bool` | Presses and releases the button (may show UI). |

*Generic changes*

| Method | Description |
|---|---|
| `SetValue(pane: OIPPane, controlId: int, value: str) -> bool` | Interprets `value` according to the control type:<br>• EditText — the text to enter<br>• CheckBox — "on"/"off", "True"/"False", "yes"/"no", "1"/"0" or "toggle"<br>• RadioGroup/PullDown/SearchablePullDown/ClassPullDown/LayerPullDown — item text, otherwise 0-based index<br>• Button — presses the button (value ignored)<br>• StaticText/Other — not supported. |
| `SetValues(settings: list[OIPSetting]) -> bool` | Applies the settings in order; stops at the first failure and returns `False`. The control ids must be read right before, as every change may rebuild the OIP. |

*Raw access*

| Method | Description |
|---|---|
| `NotifyChanged(pane: OIPPane, controlId: int, changeInfo: int) -> bool` | Raises the "widget changed" event for any control, with a raw change info (0 for a plain value change; composite controls use their own change codes). The value must already be set in the Object Info palette. Use it for `OIPControlType.Other` controls. |
| `Refresh(pane: OIPPane) -> bool` | Rebuilds the pane from the current selection. |

## Enumerations

### ToolKind

> **Full name:** `api.ToolKind` · **Kind:** `IntEnum`

How a tool is provided.

| Member | Value | Description |
|---|---|---|
| `Unknown` | `0` |  |
| `InternalClassic` | `1` | Built into Vectorworks (classic tool). |
| `InternalExtension` | `2` | Built into Vectorworks (extension tool). |
| `ScriptPlugin` | `3` | VectorScript / Python plug-in tool. |
| `ExtensionPlugin` | `4` | Tool of an external plug-in module. |

### ToolCreationType

> **Full name:** `api.ToolCreationType` · **Kind:** `IntEnum`

What kind of interaction the tool uses to create objects.

| Member | Value | Description |
|---|---|---|
| `Normal` | `0` | A regular tool (custom click handling). |
| `Point` | `1` | One click places a point object. |
| `Line` | `2` | Two clicks define a line-like object. |
| `Box` | `3` | Two clicks define a rectangle-like object. |
| `Path2D` | `4` | Clicks define a 2D path object. |
| `Path3D` | `5` | Clicks define a 3D path object. |
| `Custom` | `6` | Custom object creation. |

### ToolFilter

> **Full name:** `api.ToolFilter` · **Kind:** `IntEnum`

Which tools `ToolAccess.GetTools` returns.

| Member | Value | Description |
|---|---|---|
| `All` | `0` | Every tool installed in Vectorworks, including tools that are not in the workspace. |
| `Activatable` | `1` | Only tools that ActivateTool can activate now. |
| `InWorkspace` | `2` | Only tools placed in the tool palettes of the current workspace. |

### ModeType

> **Full name:** `api.ModeType` · **Kind:** `IntEnum`

Kind of a mode group on the Tool bar of the active tool.

| Member | Value | Description |
|---|---|---|
| `Radio` | `0` | Group of mutually exclusive buttons; exactly one is selected. |
| `Button` | `1` | Push button that performs an action (may show UI, e.g. the tool preferences dialog box). |
| `Toggle` | `2` | On/off button. |
| `PullDown` | `3` | Pull-down menu with a fixed list of items. |
| `EditText` | `4` | Labelled edit field. |
| `ResourcePopup` | `5` | Resource pop-up (symbols, styles, textures, ...) selected by resource name. |
| `SearchablePullDown` | `6` | Pull-down with search, items identified by name or id. |
| `ComboBox` | `7` | Edit field with a list of suggested items. |

### ModeButtonKind

> **Full name:** `api.ModeButtonKind` · **Kind:** `IntEnum`

Kind of a mode button as declared by a tool when it is registered (may differ from the live ModeType).

| Member | Value | Description |
|---|---|---|
| `Radio` | `0` |  |
| `Button` | `1` |  |
| `Preferences` | `2` | Opens the tool preferences dialog box. |
| `Check` | `3` | Toggle button. |
| `EditText` | `4` |  |
| `PullDown` | `5` |  |

### ToolKey

> **Full name:** `api.ToolKey` · **Kind:** `IntEnum`

Keys that tools react to while points are being entered (see `ToolControl.PressKey`).

| Member | Value | Description |
|---|---|---|
| `Return` | `0` | Completes the action of tools that finish on Return/Enter (e.g. multi point tools). |
| `Escape` | `1` | Removes all tool points; with no tool points it also clears the selection, like the user key. |
| `Backspace` | `2` | Removes the last tool point. |

### MenuCommandKind

> **Full name:** `api.MenuCommandKind` · **Kind:** `IntEnum`

How a menu command is provided.

| Member | Value | Description |
|---|---|---|
| `Unknown` | `0` |  |
| `Internal` | `1` | Built into Vectorworks; the universal name is a negative number (e.g. "-28"). |
| `ScriptPlugin` | `2` | VectorScript / Python plug-in menu command (.vsm file). |
| `ExtensionPlugin` | `3` | Menu command of an external plug-in module. |

### MenuChunkKind

> **Full name:** `api.MenuChunkKind` · **Kind:** `IntEnum`

Kind of a chunk (see "Chunk" above).

| Member | Value | Description |
|---|---|---|
| `None_` | `0` | Not a chunk: a normal command. |
| `Regular` | `1` | A fixed list of items. |
| `Dynamic` | `2` | Items built when the menu bar is built (e.g. the installed workspaces). |
| `Variable` | `3` | Items that change while Vectorworks runs (e.g. the recent files, the open documents). |

### MenuFilter

> **Full name:** `api.MenuFilter` · **Kind:** `IntEnum`

Which menu commands `MenuAccess.GetMenuCommands` returns.

| Member | Value | Description |
|---|---|---|
| `All` | `0` | Every menu command installed in Vectorworks, including commands that are not in the workspace. |
| `Executable` | `1` | Only commands whose fIsEnabled is set (ExecuteMenu can run them now; a chunk: at least one of its items). |
| `InWorkspace` | `2` | Only commands placed in the menus of the current workspace. |

### MenuEntryType

> **Full name:** `api.MenuEntryType` · **Kind:** `IntEnum`

Kind of an entry of a menu of the menu bar.

| Member | Value | Description |
|---|---|---|
| `Command` | `0` | A normal command. |
| `ChunkItem` | `1` | One item of a chunk. |
| `Submenu` | `2` | Opens a submenu; the entries of the submenu follow it. |
| `Separator` | `3` | A separator line. |

### MenuStatus

> **Full name:** `api.MenuStatus` · **Kind:** `IntEnum`

Whether a menu command (or chunk item) can be executed now, and why not (see `MenuAccess.GetMenuStatus`).

| Member | Value | Description |
|---|---|---|
| `Ready` | `0` | ExecuteMenu can run it now. |
| `Unavailable` | `1` | No command can run now: the menu bar is not set up or a plug-in object is being regenerated. |
| `NotFound` | `2` | No installed menu command has this name. |
| `NotInWorkspace` | `3` | Installed, but not placed in the menus of the current workspace. |
| `Disabled` | `4` | Disabled in the current state (it needs an open document, a selection, ...) |
| `ChunkItemRequired` | `5` | A chunk with several items: pass the index or the text of the item. |
| `ChunkItemNotFound` | `6` | The chunk has no item with this index or text, or the command is not a chunk. |

### OIPPane

> **Full name:** `api.OIPPane` · **Kind:** `IntEnum`

Pane (tab) of the Object Info palette.

| Member | Value | Description |
|---|---|---|
| `Shape` | `0` | Geometric and parametric properties. |
| `Data` | `1` | Records and other attached data. |
| `Render` | `2` | Textures. |

### OIPControlType

> **Full name:** `api.OIPControlType` · **Kind:** `IntEnum`

Kind of an OIP control.

| Member | Value | Description |
|---|---|---|
| `EditText` | `0` | Edit field (numbers, dimensions, angles and text), possibly read only. |
| `StaticText` | `1` | Label or separator. |
| `CheckBox` | `2` | On/off check box. |
| `RadioGroup` | `3` | Radio buttons or push buttons; exactly one is selected. |
| `PullDown` | `4` | Pull-down menu (popup, combo box or menu button) with a fixed list of items. |
| `SearchablePullDown` | `5` | Pull-down with search. |
| `Button` | `6` | Push button that performs an action (may show UI). |
| `ClassPullDown` | `7` | The class pull-down. |
| `LayerPullDown` | `8` | The layer pull-down. |
| `Other` | `9` | Any other control (box position, 3D location, color, list, ...); see `OIPAccess.NotifyChanged`. |

---

[Back to the index](README.md) · [Back to top](#uiautomation--tools-the-tool-bar-menus-and-the-object-info-palette)
