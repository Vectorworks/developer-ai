**English** • [Deutsch](../../MCP.de/v2027.2/ToolAccess.md) • [日本語](../../MCP.ja/v2027.2/ToolAccess.md)

# ToolAccess — interactive tools

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools that operate the interactive Vectorworks tools of the tool palettes like a user: activate a tool, set its modes and click in the drawing.

## Table of contents

- [Overview](#overview)
- [InteractiveTools](#interactivetools)
  - [getTools](#gettools)
  - [getTool](#gettool)
  - [getActiveTool](#getactivetool)
  - [activateTool](#activatetool)
  - [getToolModes](#gettoolmodes)
  - [setToolMode](#settoolmode)
  - [setToolModes](#settoolmodes)
  - [sendToolPointer](#sendtoolpointer)
  - [sendToolAction](#sendtoolaction)
  - [convertToolCoordinates](#converttoolcoordinates)

## Overview

This folder holds 1 tool group with 10 tools in total.

| Group | Group ID | Active by default | Safety level | Tools | Summary |
|---|---|---|---|---|---|
| [InteractiveTools](#interactivetools) | `interactivetools` | No | high | 10 | Operate the interactive Vectorworks tools of the tool palettes like a user. |

## InteractiveTools

> **Group:** `InteractiveTools` · **Group ID:** `interactivetools` · **Active by default:** No · **Safety level:** high · **Tools:** 10

**Operate the interactive Vectorworks tools of the tool palettes like a user.**

Use the interactive Vectorworks TOOLS - the drawing and editing tools of the tool palettes (Rectangle, Polyline, Wall, Door, Selection, Reshape, Eyedropper, ...) - exactly as a user does: find a tool, activate it, set its modes on the mode bar, then click, double click or drag in the drawing and finish or cancel the action. Prefer the dedicated create/edit tools of the other groups when they cover the task; use this group for tools that have no direct API (plug-in tools, special editing tools) or when the user asks to operate a tool.

Workflow:

1. getTools with `search` (and filter `activatable`) finds a tool; tools are identified by `universalName` (built-in tools use a negative number such as `-207` and also accept their English `name`). getTool returns one tool with its declared mode buttons.
2. activateTool activates it (optionally setting modes) and returns the live mode bar, the instruction text (`helpMessage`) and the tool points.
3. Modes: the mode bar holds up to 8 mode groups (radio buttons, push buttons, toggles, pull-downs, edit fields, resource pop-ups, searchable pull-downs, combo boxes). Address a mode by its 0-based `modeIndex` or by `modeName` (its label or one of its choice names). setToolModes sets several modes by text value; setToolMode offers every typed operation. A tool may rebuild its mode bar after a change, so re-read the modes (getToolModes) instead of reusing old indexes. Pressing a preferences button opens a modal dialog.
4. sendToolPointer clicks points in the drawing. In `model` space points are world units and are applied EXACTLY (no snapping); { x, y } lies on the layer plane, { x, y, z } is a 3D point. In `view` space points are pixels in the active pane and behave like a real click including SmartCursor snapping. Tools that pick the object under the cursor (Selection, Reshape, Eyedropper, ...) need the point visible in the pane - check with convertToolCoordinates. Each click usually adds one tool point; two-point tools (rectangle, line) need two clicks in click-click drawing mode, multi-point tools (polyline, wall, polygon) are completed with `finish` or a doubleClick.
5. sendToolAction finishes (Return), cancels or removes the last point. Always finish or cancel a started action before switching tools.

Check the outcome with getActiveTool (`toolPointCount`, `helpMessage`) and with the Objects/Selection groups. Modifier keys (Shift, Alt) are not supported. Changes made by a tool are recorded by the tool itself in the Vectorworks undo history, not as 'MCP: &lt;tool&gt;'.

> **Note:** The group level `high` applies to the group as a whole. Each tool reports its own level: `low` for the five read-only tools and `medium` for the five tools that operate a tool like a user (see the table below).
>
> **Note:** A call returns `err` for invalid arguments, an unknown tool or mode, a tool that cannot be activated and, for `sendToolPointer` and `sendToolAction`, when there is no active drawing pane. When the active tool does not accept an input or a mode change, the call still succeeds and says so in the result (`ok: false`, `allApplied: false` or `modesApplied: false`). The five tools that operate a tool are not allowed in `runToolBatch`. The server opens no undo event for them and never rolls them back, so a failed call has no `rolledBack` key.

| Tool | Effect | Safety | Summary |
|---|---|---|---|
| [`getTools`](#gettools) | Read-only | low | Lists the Vectorworks tools. |
| [`getTool`](#gettool) | Read-only | low | Returns one tool with its declared mode buttons. |
| [`getActiveTool`](#getactivetool) | Read-only | low | Returns the state of the active tool. |
| [`activateTool`](#activatetool) | Interactive | medium | Activates a tool. |
| [`getToolModes`](#gettoolmodes) | Read-only | low | Reads the live mode bar of the active tool. |
| [`setToolMode`](#settoolmode) | Interactive | medium | Changes one mode of the active tool. |
| [`setToolModes`](#settoolmodes) | Interactive | medium | Sets several modes of the active tool. |
| [`sendToolPointer`](#sendtoolpointer) | Interactive | medium | Clicks, double-clicks, hovers or drags in the drawing with the active tool. |
| [`sendToolAction`](#sendtoolaction) | Interactive | medium | Finishes or cancels the action of the active tool, or removes its last point. |
| [`convertToolCoordinates`](#converttoolcoordinates) | Read-only | low | Converts points between model space and the view of the active pane. |

### getTools

Lists the Vectorworks tools.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the Vectorworks tools: built-in tools, VectorScript/Python plug-in tools and SDK plug-in tools. `filter`: all (default; every installed tool, also those not in the workspace), activatable (can be activated now) or inWorkspace (placed in the tool palettes). `search` matches the universal name, name, display name and category (case-insensitive); `kind` keeps one kind of tool.

Each tool reports universalName, name, displayName, category, helpText, shortcut, kind, creationType (point|line|box|path2D|path3D|custom|normal), inWorkspace, canActivate and active; `includeModeButtons` adds the mode buttons the tool declares. Results are paged (`count` is the total; `truncated` means more follow).

> **Note:** `kind` is compared exactly: any other value returns no tools and no error. `search` is case-insensitive for the letters A-Z only.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `filter` | string |  | One of: `all` (default), `activatable`, `inWorkspace`. Any other value is an error. An empty string counts as `all`. |
| `search` | string |  | Text filter: keeps the tools whose `universalName`, `name`, `displayName` or `category` contains this text (case-insensitive). |
| `kind` | string |  | One of: `internalClassic`, `internalExtension`, `scriptPlugin`, `extensionPlugin`, `unknown`. Compared exactly. |
| `includeModeButtons` | boolean |  | `true` lists the declared mode buttons of every tool (`modeButtons`) instead of their number (`modeButtonCount`). Default `false`. |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1, default 100). See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

**Result**

| Key | Description |
|---|---|
| `tools` | The tools of the page, sorted by `displayName` (case-insensitive). Left out with `countOnly`. |
| `count`, `returned`, `offset`, `limit`, `truncated`, `nextOffset` | The paging keys (see [Paging](Common.md#paging)). `nextOffset` appears only when `truncated` is true. |

Each tool has these keys:

| Key | Description |
|---|---|
| `universalName` | The id of the tool. Built-in tools use a negative number such as `-207`. |
| `name` | The English name of a built-in tool; for plug-in tools the same as `universalName`. |
| `displayName` | The localized name. |
| `category`, `helpText`, `shortcut` | The category, the help text and the keyboard shortcut of the tool. |
| `kind` | `internalClassic` (built into the core as a classic tool), `internalExtension` (built into the core as an extension tool), `scriptPlugin` (VectorScript or Python plug-in tool), `extensionPlugin` (SDK plug-in tool) or `unknown`. |
| `creationType` | `point`, `line`, `box`, `path2D`, `path3D`, `custom` or `normal`. |
| `inWorkspace` | `true` when the tool is placed in a tool palette of the current workspace. |
| `canActivate` | `true` when `activateTool` can activate the tool now: a document is open and the tool system lists the tool. It does not depend on `inWorkspace`. |
| `active` | `true` for the active tool. |
| `modeButtonCount` | The number of mode buttons the tool declares (0 for a tool that declares none). Replaced by `modeButtons` with `includeModeButtons`. |
| `modeButtons` | Only with `includeModeButtons`: a list of `{ name, helpText, kind }`. `kind` is `radio`, `button`, `preferences`, `check`, `editText` or `pullDown`. |

Errors: `'filter' must be all, activatable or inWorkspace`; the paging errors (see [Results and errors](Common.md#results-and-errors)).

### getTool

Returns one tool with its declared mode buttons.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Return one tool found by `name` (universal name, English name of a built-in tool, or localized display name), including the mode buttons it declares (name, helpText, kind). The declared buttons are static information; the live mode bar is read with getToolModes after activation.

> **Note:** `name` is matched in this order of preference: the exact `universalName` (case-sensitive), then a `universalName` or English `name` that differs only in case, then the localized name or `displayName` that differs only in case. When several tools match equally, a tool that can be activated wins.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Universal name, English name of a built-in tool, or localized display name. |

**Result**

One tool with its `modeButtons`, with the keys described under [`getTools`](#gettools).

Errors: `'name' is required`; `no Vectorworks tool matches '<name>' (use getTools with 'search' to find it)`.

### getActiveTool

Returns the state of the active tool.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Return the state of the active tool: the tool, its current instruction text (`helpMessage`), whether an action is in progress, the tool points entered so far (point2D, point3D, viewPoint), the current hover point, the size of the active pane in pixels and - unless `includeModes` is false - the live mode bar. `maxChoices` limits the listed choices per mode (default 50).

> **Note:** `activeTool` can be a helper tool that `getTools` does not list, for example while a script picks points. It is `null` when no tool is active.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `includeModes` | boolean |  | `false` leaves out the live mode bar (`modes`). Default `true`. |
| `maxChoices` | integer |  | Maximum number of choices listed per mode (0 or more, default 50). |

**Result**

| Key | Description |
|---|---|
| `activeTool` | The active tool with its `modeButtons`, with the keys described under [`getTools`](#gettools). `null` when no tool is active. |
| `helpMessage` | The current instruction text of the tool. |
| `inProgress` | Whether an action of the tool is in progress. |
| `toolPointCount` | The number of tool points entered so far. |
| `toolPoints` | The tool points, each `{ point2D: { x, y }, point3D: { x, y, z }, viewPoint: { x, y } }`. `point3D` is the model point, `point2D` the point on the screen plane (2D tools) or on the working plane (3D tools), `viewPoint` the position in pixels of the active pane. |
| `currentPoint` | The current hover point, in the form of a tool point. Only when available. |
| `viewSize` | `{ width, height }` of the active pane in pixels. Only when there is an active pane. |
| `modes` | The live mode bar: a list of modes, each as described under [`getToolModes`](#gettoolmodes). Left out with `includeModes` false. |

### activateTool

Activates a tool.

> **Effect:** Interactive · **Safety:** medium · **Undo:** recorded by Vectorworks as for user input · **In runToolBatch:** no

**Details**

Activate the tool given by `name` (universal name, English name of a built-in tool or display name), or the default Selection tool with `selectionTool`: true. Only tools in the current workspace can be activated (see getTools `canActivate`). Optionally set modes right after activation: `modes` is an array of { modeIndex | modeName, value } (same as setToolModes), or `modeIndex` / `modeName` with `choiceIndex` picks one choice.

Returns the new active tool state with its live mode bar and `modesApplied`.

> **Note:** The check is the `canActivate` of the tool, not `inWorkspace` (see [`getTools`](#gettools)). With `selectionTool` true, `name` is ignored; otherwise `name` is matched as in [`getTool`](#gettool). When the tool is activated but a mode cannot be set, the call still succeeds with `modesApplied: false`.
>
> **Note:** `modes` wins over `modeIndex` / `modeName` with `choiceIndex`. The latter works like `selectChoice` of [`setToolMode`](#settoolmode): it fails for edit fields and resource pop-ups (`modesApplied: false`), which need `modes` with a `value`. A missing `choiceIndex` counts as 0. `modeName` is used only when `modeIndex` is absent.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Universal name, English name of a built-in tool or display name. |
| `selectionTool` | boolean |  | `true` activates the default Selection tool and ignores `name`. Default `false`. |
| `modes` | array of object |  | Modes to set right after activation, in order, in the form of the `settings` of [`setToolModes`](#settoolmodes). Wins over `modeIndex` / `modeName`. |
| `modes[].modeIndex` | integer |  | 0-based index of the mode. Wins over `modeName`. |
| `modes[].modeName` | string |  | Label of the mode or one of its choice names. Used only when `modeIndex` is absent. |
| `modes[].value` | string or number or integer or boolean | Yes | The new value, as the `value` of [`setToolMode`](#settoolmode) with `setValue`. A setting without `value` is applied as an empty text. |
| `modeIndex` | integer |  | 0-based index of the one mode to change with `choiceIndex`. Wins over `modeName`. |
| `modeName` | string |  | Label of the mode or one of its choice names. Used only when `modeIndex` is absent. |
| `choiceIndex` | integer |  | The choice to pick in the mode `modeIndex` / `modeName`, as `selectChoice` of [`setToolMode`](#settoolmode). Default 0. A negative value, or one that is not a number, counts as 0. |
| `maxChoices` | integer |  | Maximum number of choices listed per mode (0 or more, default 50). |

**Result**

| Key | Description |
|---|---|
| `activated` | `true`. When the tool cannot be activated, the call fails with an error instead. |
| `modesApplied` | `true` when no mode was requested or every requested mode change worked, otherwise `false`. |
| `modeResults` | Only with `modes`: one entry per setting, in the form of the `results` of [`setToolModes`](#settoolmodes). |

The result also has the keys of [`getActiveTool`](#getactivetool), with the live mode bar (`modes`).

Errors: `'name' is required (or set 'selectionTool' to true)`; `no Vectorworks tool matches '<name>' (use getTools with 'search' to find it)`; `'<display name>' is not in the current workspace and cannot be activated` (the tool has `canActivate` false); `'<display name>' could not be activated`; `the Selection tool could not be activated`.

### getToolModes

Reads the live mode bar of the active tool.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the live mode bar of the active tool. Without `modeIndex` / `modeName` all modes are returned. Each mode reports index, type (radio|button|toggle|pullDown|editText|resourcePopup|searchablePullDown|comboBox), enabled, label, value (current value as text), choices (name, helpText, image, id) with choiceCount, selectedChoice and isOn for toggles. `maxChoices` limits the listed choices per mode (default 50).

> **Note:** `modeName` matches the label of a mode or one of its choice names (case-insensitive). `modeIndex` wins over `modeName`: an index outside the mode bar is an error and does not fall back to `modeName`. Modes are searched from index 0 upward and the first mode whose label or any of its choice names matches is used.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `maxChoices` | integer |  | Maximum number of choices listed per mode (0 or more, default 50). |
| `modeIndex` | integer |  | 0-based index of the mode to return. Wins over `modeName`. |
| `modeName` | string |  | Label of the mode or one of its choice names. Used only when `modeIndex` is absent. |

**Result**

Without `modeIndex` and `modeName`:

| Key | Description |
|---|---|
| `modeCount` | The number of modes on the mode bar. |
| `modes` | The list of all modes. |

With `modeIndex` or `modeName`, the result is the one mode itself, without `modeCount` and `modes`. Each mode has these keys:

| Key | Description |
|---|---|
| `index` | The 0-based index of the mode. |
| `type` | `radio`, `button`, `toggle`, `pullDown`, `editText`, `resourcePopup`, `searchablePullDown` or `comboBox`. |
| `enabled` | Whether the mode can be changed. |
| `label` | The label of the mode. |
| `value` | The current value as text. |
| `choiceCount` | The number of choices of the mode. |
| `choices` | The listed choices, each `{ index, name }` plus `helpText`, `image` and `id` when they are not empty. Up to `maxChoices` entries; always empty for edit fields and resource pop-ups. |
| `choicesTruncated` | `true` when `choices` has fewer entries than `choiceCount`. Present only then. |
| `selectedChoice` | The index of the selected choice. Present only when the mode has one. |
| `isOn` | Whether the toggle is on. Present only for toggles. |

Error: `no mode matches 'modeIndex' / 'modeName' (modeCount is N)`, where N is the number of modes.

### setToolMode

Changes one mode of the active tool.

> **Effect:** Interactive · **Safety:** medium · **Undo:** recorded by Vectorworks as for user input · **In runToolBatch:** no

**Details**

Change one mode of the active tool, addressed by `modeIndex` or `modeName`, exactly as a user does on the mode bar. `action` (default setValue): setValue - `value` interpreted by mode type (radio: button name or index; button: press; toggle: on/off/true/false/toggle; pullDown/searchablePullDown: item text, id or index; comboBox: item or free text; editText: text; resourcePopup: resource name); selectChoice - pick choice `choiceIndex` of any mode type; selectRadio - radio button `choiceIndex`; pressButton; setToggle - `isOn`; selectItem - list item by `item` (text or id) or `choiceIndex`; setText - `text` into an edit field or combo box; selectResource - `resourceName` in a resource pop-up.

Disabled modes cannot be changed. Returns `ok` and the mode after the change.

> **Note:** Only the items of a searchable pull-down have an id; the items of pull-downs and combo boxes are matched by their text (case-insensitive). The text or id of an item is tried before the number, so `"1"` first selects an item named `1`.
>
> **Note:** The checks run in this order: the mode, then `action`, then the argument that the action needs. `modeIndex` wins over `modeName`; an index outside the mode bar is an error and does not fall back to `modeName`. A disabled mode, or a value that the mode does not accept, is not an error: the call returns `ok: false`.
>
> **Note:** `selectChoice` works for radio buttons, buttons (`choiceIndex` is ignored), toggles (0 is off, any other number is on) and the lists of pull-downs, searchable pull-downs and combo boxes. It always fails for edit fields and resource pop-ups; use `setText` or `selectResource` for them.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `action` | string |  | One of: `setValue` (default), `selectChoice`, `selectRadio`, `pressButton`, `setToggle`, `selectItem`, `setText`, `selectResource`. |
| `value` | string or number or integer or boolean |  | The value for `setValue` (required for that action). How it is read depends on the mode type. A boolean counts as `on` or `off`, a number as its decimal text. |
| `choiceIndex` | integer |  | 0-based number of the choice. Required for `selectChoice` and `selectRadio`; for `selectItem` it is used when `item` is absent. A negative value, or one that is not a number, counts as 0. |
| `isOn` | boolean |  | Required for `setToggle`. A value that is not a boolean counts as `false`. |
| `item` | string |  | Text of the item (case-insensitive), or the id of a searchable pull-down item. For `selectItem`; wins over `choiceIndex`. |
| `text` | string |  | Required for `setText`. |
| `resourceName` | string |  | Required for `selectResource`. |
| `maxChoices` | integer |  | Maximum number of choices listed per mode in `mode` (0 or more, default 50). |
| `modeIndex` | integer |  | 0-based index of the mode. Wins over `modeName`. |
| `modeName` | string |  | Label of the mode or one of its choice names. Used only when `modeIndex` is absent. |

**Actions**

| Action | Needs | What it does |
|---|---|---|
| `setValue` | `value` | Sets the mode from `value`; see the table below. |
| `selectChoice` | `choiceIndex` | Picks a choice, see the second note above. |
| `selectRadio` | `choiceIndex` | Presses the radio button with this number. Fails when the number is past the last button. A negative value, or one that is not a number, counts as 0. |
| `pressButton` | none | Presses a button mode. |
| `setToggle` | `isOn` | Turns a toggle on or off. A toggle that already has the state is left alone and the call returns `ok: true`. |
| `selectItem` | `item` or `choiceIndex` | Picks an item of a pull-down, searchable pull-down or combo box list. `item` (text, or id for a searchable pull-down) wins over `choiceIndex`. |
| `setText` | `text` | Types text into an edit field or a combo box. |
| `selectResource` | `resourceName` | Selects a resource in a resource pop-up. `ok` is `true` only when the pop-up then shows that resource. |

`setValue` reads `value` by mode type:

| Mode type | `value` |
|---|---|
| `radio` | The name or the image of a choice (case-insensitive), or the number of the choice. |
| `button` | Ignored: the button is pressed. |
| `toggle` | `on`, `true`, `yes` or `1` for on; `off`, `false`, `no` or `0` for off; `toggle` flips the toggle. The words are case-insensitive. |
| `pullDown`, `searchablePullDown` | The text of an item (case-insensitive) or, for a searchable pull-down, its id; else the number of the item. The text or id is tried first. |
| `comboBox` | The text of an item (case-insensitive); any other text is typed into the field. |
| `editText` | The text to type. |
| `resourcePopup` | The name of the resource. |

**Result**

| Key | Description |
|---|---|
| `ok` | `true` when the change was applied. |
| `modeCount` | The number of modes on the mode bar. |
| `mode` | The mode after the change, with the keys described under [`getToolModes`](#gettoolmodes). `maxChoices` applies. |

Errors: `no mode matches 'modeIndex' / 'modeName' (modeCount is N)`; `unknown 'action'`; `'<argument>' is required for action '<action>'`; `'item' or 'choiceIndex' is required for action 'selectItem'`.

### setToolModes

Sets several modes of the active tool.

> **Effect:** Interactive · **Safety:** medium · **Undo:** recorded by Vectorworks as for user input · **In runToolBatch:** no

**Details**

Set several modes of the active tool in order: `settings` is an array of { modeIndex | modeName, value } where value is interpreted as in setToolMode setValue. Every setting is reported in `results` (ok, newValue, err); `allApplied` is false when any failed. Returns the refreshed modes.

> **Note:** Every setting is tried, also after a failure. A setting that fails does not make the call fail: it shows in `results` and sets `allApplied` to `false`. Each setting finds its mode as in [`setToolMode`](#settoolmode): `modeIndex` wins over `modeName`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `settings` | array of object | Yes | The mode changes, applied in order. A non-empty array of `{ modeIndex | modeName, value }`. |
| `settings[].modeIndex` | integer |  | 0-based index of the mode. Wins over `modeName`. |
| `settings[].modeName` | string |  | Label of the mode or one of its choice names. Used only when `modeIndex` is absent. |
| `settings[].value` | string or number or integer or boolean | Yes | The new value, read by mode type as the `value` of [`setToolMode`](#settoolmode) with `setValue`. The tool does not refuse a setting without `value`: it is applied as an empty text. |
| `maxChoices` | integer |  | Maximum number of choices listed per mode in `modes` (0 or more, default 50). |

**Result**

| Key | Description |
|---|---|
| `allApplied` | `true` when every setting was applied. |
| `results` | One entry per setting, in order. |
| `modes` | The refreshed mode bar: the list of all modes, each as described under [`getToolModes`](#gettoolmodes). `maxChoices` applies. |

Each entry of `results` repeats the setting (a setting that is not an object appears as `{ "setting": <the value> }`) and adds:

| Key | Description |
|---|---|
| `ok` | `true` when the mode was changed. |
| `modeIndex` | The 0-based index of the mode that was found. |
| `newValue` | The text value of the mode after the change. |
| `err` | `no mode matches 'modeIndex' / 'modeName'`. Only when no mode was found; then `ok` is `false` and `modeIndex` and `newValue` are absent. |

Error: `'settings' must be a non-empty array of { modeIndex | modeName, value }`, when `settings` is missing, is not an array or is empty.

### sendToolPointer

Clicks, double-clicks, hovers or drags in the drawing with the active tool.

> **Effect:** Interactive · **Safety:** medium · **Undo:** recorded by Vectorworks as for user input · **In runToolBatch:** no

**Details**

Operate the active tool with the pointer, as the user does in the drawing. `action`: click (default), doubleClick, move (hover only; updates the preview) or drag (mouse down at `from`, up at `to`). `space`: model (default; world units, exact, no snapping; { x, y } on the layer plane or { x, y, z }) or view (pixels in the active pane, with snapping). Give one `point` or several `points` (sent in order, stopping at the first failure); `finish`: true presses Return afterwards to complete multi-point tools.

Returns `sent` and the tool state after the input (`toolPointCount`, `toolPoints`, `helpMessage`).

> **Note:** `points` wins over `point`. For `drag` only `from` and `to` count: they must both be 2D (no `z`), both 3D (with `z`) or both view points. All points are read before anything is sent, so a point that cannot be read gives an error and nothing is sent. A view point is rounded to whole pixels and must fit into 16 bits (-32768 to 32767).
>
> **Note:** Sending stops early only when a point in `view` space lies outside the active pane. The answer of the tool to a point is not reported: `sent` counts the pointer inputs that were delivered, not the points that the tool accepted. Check `toolPointCount` and `helpMessage` to see what the tool did.
>
> **Note:** `finish` is applied after every action, also after `move` and `drag`, and presses Return even when `sent` is 0. A `model` point that is not visible in the active pane is delivered at the center of the pane. A tool that takes the point itself still gets the exact model point; a tool that picks what lies under the pointer (Selection, Reshape, Eyedropper) acts at the pane center, and no error is reported. Use [`convertToolCoordinates`](#converttoolcoordinates) with `modelToView` to check that a point is visible.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `action` | string |  | One of: `click` (default), `doubleClick`, `move` (hover only), `drag`. `drag` uses `from` and `to`; the other actions use `point` or `points`. |
| `space` | string |  | One of: `model` (default), `view`. `model`: world units, exact, with snapping suspended. `view`: pixels in the active pane, with SmartCursor snapping like a real click. |
| `point` | [3D point](Common.md#points) |  | Model space: { x, y } on the layer plane or { x, y, z } in 3D, in world units. View space: { x, y } in pixels from the top-left corner of the active drawing pane. Used by `click`, `doubleClick` and `move`; ignored when `points` is given. |
| `points` | array of [3D point](Common.md#points) |  | Each item: Model space: { x, y } on the layer plane or { x, y, z } in 3D, in world units. View space: { x, y } in pixels from the top-left corner of the active drawing pane. Sent in order. Wins over `point`. |
| `from` | [3D point](Common.md#points) |  | Model space: { x, y } on the layer plane or { x, y, z } in 3D, in world units. View space: { x, y } in pixels from the top-left corner of the active drawing pane. For `drag` only: where the mouse goes down. `from` and `to` must be of the same kind. |
| `to` | [3D point](Common.md#points) |  | Model space: { x, y } on the layer plane or { x, y, z } in 3D, in world units. View space: { x, y } in pixels from the top-left corner of the active drawing pane. For `drag` only: where the mouse goes up. |
| `finish` | boolean |  | `true` presses Return after the input, to complete multi-point tools. |

**Result**

The state of the active tool after the input, with the keys of [`getActiveTool`](#getactivetool) except `modes` (`activeTool`, `helpMessage`, `inProgress`, `toolPointCount`, `toolPoints`, `currentPoint`, `viewSize`), plus:

| Key | Description |
|---|---|
| `sent` | The number of pointer inputs that were delivered: one per point for `move`, `click` and `doubleClick`; 1 or 0 for `drag`. |
| `ok` | `true` when `sent` is greater than 0. |
| `finished` | `true` when `finish` was set and the Return key was handled. |

Errors, in the order in which they are checked: `there is no active drawing pane to send input to`; `'action' must be move, click, doubleClick or drag`; `'space' must be model or view`; for `drag`, `'drag' needs 'from' and 'to' of the same kind (both 2D, both 3D, or both view points)`; for the other actions, `'point' or a non-empty 'points' array is required`, or `point <N> must be { x, y } or { x, y, z } in world units` (model space) or `point <N> must be { x, y } in pixels (16 bit)` (view space), where `<N>` is the 0-based position in `points`.

### sendToolAction

Finishes or cancels the action of the active tool, or removes its last point.

> **Effect:** Interactive · **Safety:** medium · **Undo:** recorded by Vectorworks as for user input · **In runToolBatch:** no

**Details**

Control the action of the active tool: finish (Return - completes multi-point tools), cancel (removes all tool points without changing the selection), removeLastPoint, or pressKey with `key` return, escape or backspace (escape with no tool points also clears the selection, like the user key). Returns `ok` and the tool state.

> **Note:** `finish` presses Return. `cancel` clears all tool points without touching the selection, like Escape while tool points exist. `removeLastPoint` removes one tool point, like Backspace. `pressKey` sends the named key to the active drawing pane; `escape` with no tool points also clears the selection, as the user's key does.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `action` | string | Yes | One of: `finish`, `cancel`, `removeLastPoint`, `pressKey`. |
| `key` | string |  | One of: `return`, `escape`, `backspace`. Needed for `pressKey`; without a valid key that action fails with the `'action' must be ...` error. The other actions ignore it. |

**Result**

The state of the active tool after the action, with the keys of [`getActiveTool`](#getactivetool) except `modes`, plus `ok`. `ok` depends on the action:

| Action | `ok` is `true` when |
|---|---|
| `finish` | the Return key was handled. |
| `cancel` | no tool points remain. This is also the case when there were none to begin with. |
| `removeLastPoint` | a tool point was removed. `false` when there are no tool points. |
| `pressKey` | the key was handled. This does not show what the tool did with it. |

Errors: `there is no active drawing pane to send input to`; `'action' must be finish, cancel, removeLastPoint or pressKey (with 'key' return, escape or backspace)`.

### convertToolCoordinates

Converts points between model space and the view of the active pane.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Convert points between model space and the view of the active pane. `direction` modelToView: model { x, y } or { x, y, z } to pixels, null when the point is not visible in the pane. viewToModel: pixels to the 2D model point under them (layer plane in Top/Plan, screen plane otherwise), null outside the pane. Give `point` or `points`. Also returns the pane size (`viewSize`).

> **Note:** A point that cannot be converted gives `null` in its place; that is not an error. The call fails only for a wrong `direction` or when no point is given. With `points`, `point` is ignored. `modelToView` reads `{ x, y }` as a 2D point and `{ x, y, z }` as a 3D point. `viewToModel` always gives a 2D model point and never a `z`. Without an active drawing pane every entry is `null` and `viewSize` is absent.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `direction` | string | Yes | One of: `modelToView` (model points to pixels of the active pane), `viewToModel` (pixels to model points). |
| `point` | [3D point](Common.md#points) |  | One point to convert. For `modelToView`: a model point, { x, y } or { x, y, z }, in world units. For `viewToModel`: { x, y } in pixels from the top-left corner of the active drawing pane (rounded to whole pixels; must lie between -32768 and 32767). Ignored when `points` is given. |
| `points` | array of [3D point](Common.md#points) |  | The points to convert, each in the form of `point`. Wins over `point`. |

**Result**

| Key | Description |
|---|---|
| `points` | One entry per input point, in the same order. Each entry is `{ x, y }` or `null`. `modelToView` gives pixels, `viewToModel` gives a 2D model point in world units. |
| `viewSize` | `{ width, height }` of the active pane in pixels. Only when there is an active pane. |

An entry is `null` when the point cannot be read, when it cannot be converted (`modelToView`: the point is not visible in the pane; `viewToModel`: the pixel lies outside the pane), or when there is no active drawing pane.

Errors: `'direction' must be modelToView or viewToModel`; `'point' or a non-empty 'points' array is required`.
