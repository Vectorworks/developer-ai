**English** • [Deutsch](../../MCP.de/v2027.2/OIPAccess.md) • [日本語](../../MCP.ja/v2027.2/OIPAccess.md)

# OIPAccess — Object Info palette

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools that read and operate the Object Info palette for the current selection, like a user.

## Table of contents

- [Overview](#overview)
- [Object Info](#object-info)
  - [getOIPControls](#getoipcontrols)
  - [setOIPValues](#setoipvalues)
  - [pressOIPButton](#pressoipbutton)

## Overview

This folder holds 1 tool group with 3 tools in total.

| Group | Group ID | Active by default | Risk level | Tools | Summary |
|---|---|---|---|---|---|
| [Object Info](#object-info) | `object-info` | No | medium | 3 | Read and operate the Object Info palette for the current selection, like a user. |

## Object Info

> **Group:** `Object Info` · **Group ID:** `object-info` · **Active by default:** No · **Risk level:** medium · **Tools:** 3

**Read and operate the Object Info palette for the current selection, like a user.**

Read and operate the Object Info palette like a user: for the current selection it shows the Shape pane (class, layer, size, the parameters of plug-in objects, ...), the Data pane (records and other attached data) and the Render pane (textures) as controls - edit fields, check boxes, pull-downs, radio buttons and buttons. The palette does not have to be visible.

Use this group for properties that the palette shows and no dedicated tool covers, for the parameters of plug-in objects as the palette shows them (including the controls and buttons that a plug-in adds there), for record fields in the Data pane and textures in the Render pane, or when the user asks to use the Object Info palette. Prefer the dedicated tools of the other groups when they cover the change - e.g. setObjectParameter (or createPluginObject `params` when creating) for plug-in parameters, editObject for the name, class and transforms, setObjectAttributes for pen and fill, applyResource for textures: each of their calls is one undo step "MCP: &lt;tool&gt;", is rolled back when it fails and can run in runToolBatch.

Workflow:

1. Select the objects with selectObjects (Selection group); a change applies to the whole selection.
2. getOIPControls lists the controls of a `pane`: shape (default), data or render.
3. setOIPValues sets values and pressOIPButton presses a button. Name a control by `label` (the first visible control with that label, case-insensitive; a trailing ':' and blanks are ignored) or by `controlId` from getOIPControls - exactly one of them. Every change may rebuild the palette and change the control ids, so prefer labels.
4. Read the controls again with getOIPControls after changes.

Values are entered as a user types them: a plain number is in the document's units (getUnits), not in the world units and radians that the other groups use, so add a unit to be explicit (e.g. "200mm"). Text that Vectorworks cannot read may make it show an alert, which waits for the user like a dialog. Plug-in objects regenerate at once.

Undo: each palette change is its own Vectorworks undo step, named by Vectorworks as for a user edit, not "MCP: &lt;tool&gt;". setOIPValues and pressOIPButton cannot run in runToolBatch, and a failed setting does not take back the earlier ones.

Dialogs: a button or a choice can open a modal dialog or an alert. The call then waits until the user closes it, Vectorworks answers no other MCP call meanwhile and the MCP client may time out. A button label or choice name that ends in "..." opens a dialog (`opensDialog` in getOIPControls) and needs `allowDialog`: true (default false); pass it only after telling the user that the dialog will open and that they must close it there.

| Tool | Effect | Risk | Summary |
|---|---|---|---|
| [`getOIPControls`](#getoipcontrols) | Read-only | low | Lists the controls of one pane of the Object Info palette. |
| [`setOIPValues`](#setoipvalues) | Interactive | medium | Sets controls of the Object Info palette, as a user does. |
| [`pressOIPButton`](#pressoipbutton) | Interactive | medium | Presses a button of the Object Info palette. |

### getOIPControls

Lists the controls of one pane of the Object Info palette.

> **Effect:** Read-only · **Risk:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the controls that one pane of the Object Info palette shows for the current selection; the pane is refreshed first, so the list matches the selection also right after selectObjects. `pane`: shape (default), data or render. `search` keeps the controls whose label contains it (case-insensitive); `includeHidden` (default false) also lists hidden controls; `maxChoices` (0 or more, default 50) limits the listed `choices` of a control (`choiceCount` stays the full count); `limit` (default 100) and `offset` page the list; `countOnly` (default false) returns `count` and the other paging keys but no `controls`.

Returns `pane`, `available` (true), `selectionCount`, `count` (the controls that match `search`), `controls` (this page) and the paging keys (`truncated` is true when more follow). A pane without controls, e.g. with nothing selected, is not an error: `available` false, `count` 0, `controls` empty and a `hint`. Each control has `controlId`, `type` (editText, staticText, checkBox, radioGroup, pullDown, searchablePullDown, button, classPullDown, layerPullDown or other), `label`, `value` (as text), `enabled`, `readOnly` and `indeterminate` (the selected objects differ); `visible` with includeHidden, `parentId` when it has a parent control, `checked` for a check box that is not indeterminate, `choices`, `choiceCount` and `selectedChoice` (0-based) for radioGroup and the four pull-down types, `opensDialog`: true for a button whose label opens a dialog, and `coreTypeId` for type other.

> **Note:** The controls are listed in ascending `controlId` order. `value` is the text that the control shows: the text of an edit field, the label of a staticText, `on`, `off` or empty (indeterminate) for a check box, and the selected item for a radioGroup or any of the four pull-down types; it is empty for the other types. `readOnly` can be true only for an edit field.
>
> `choices` is always empty for a searchablePullDown: the palette does not list its items. `choiceCount` and `selectedChoice` are still set; `selectedChoice` is left out when no item is selected.
>
> Case is ignored for the letters A-Z only in `search` and in the choice names of setOIPValues: type other letters as the palette shows them. The `label` of setOIPValues and pressOIPButton is compared with Vectorworks' case-insensitive text comparison.
>
> A pane without controls returns only `pane`, `available` false, `selectionCount`, `count` 0, `controls` (always an empty list, also with `countOnly`) and `hint`, with no `returned`, `offset`, `limit` or `truncated`. The `hint` is `The <pane> pane of the Object Info palette shows no controls: select objects first (Selection group, selectObjects)`. This is also the result when every control of the pane is hidden and `includeHidden` is false.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pane` | string |  | One of: `shape`, `data`, `render`. Default: `shape`. |
| `search` | string |  | Text filter: keeps the controls whose label contains this text (case-insensitive for the letters A-Z only). |
| `includeHidden` | boolean |  | Also list hidden controls; each then has `visible`. Default false. |
| `maxChoices` | integer |  | 0 or more, default 50. The most `choices` listed for a control; `choiceCount` stays the full count. |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). Default: 100. See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

Errors: `'pane' must be shape, data or render`, `'search' must be a string`, `'maxChoices' must be a whole number of 0 or more`, `'includeHidden' must be true or false` and the paging errors (see [Paging](Common.md#paging)).

### setOIPValues

Sets controls of the Object Info palette, as a user does.

> **Effect:** Interactive · **Risk:** medium · **Undo:** recorded by Vectorworks as for user input · **In runToolBatch:** no

**Details**

Set controls of the Object Info palette in order, as a user does. `settings`: 1 to 50 entries { `label` or `controlId`, `value`, `pane` (optional; default the call's `pane`, which defaults to shape) }; `allowDialog` (default false). `value` by control type: editText - the text to type, or a number (typed as written); checkBox - a boolean, or on/off, yes/no, 1/0 or toggle; radioGroup and the four pull-down types - a choice name or a 0-based index; a searchablePullDown does not list its items, so an index into it needs `allowDialog`: true (the item may open a dialog).

Every setting is checked before anything changes: the call is refused, with nothing changed, for an unknown, hidden, disabled or read-only control, a staticText or other control, a button (use pressOIPButton), a value that does not fit the control, and a choice that opens a dialog without `allowDialog`: true. A control that an earlier setting would first show or enable is therefore refused too: set it in a later call.

The settings are then applied in order: each control is found again right before it is set (an earlier setting may rebuild the palette), its new value is read back, and the call stops at the first failure. Returns `pane`, `results` [{ index, label, controlId, ok, value (as read back) or err }], `appliedCount`, `allApplied` and `notAttemptedCount`. A failure of the first setting adds a top-level `err`; a later failure leaves the earlier settings applied (`allApplied` false, no top-level `err`).

There is no "MCP: setOIPValues" undo step and no rollback: each applied setting is its own Vectorworks undo step.

> **Note:** How `value` is read, by control type:
>
> - editText: a string (typed as written) or a number (written as the shortest text that reads back, for example `200` or `0.5`). Any other JSON type is refused.
> - checkBox: a JSON boolean, or one of the strings `on`, `off`, `true`, `false`, `yes`, `no`, `1`, `0` or `toggle` (case-insensitive). A JSON number such as `1` is refused. `toggle` checks an indeterminate check box.
> - radioGroup, pullDown, classPullDown and layerPullDown: a listed choice name (case-insensitive for the letters A-Z) is tried first. Otherwise a whole number below `choiceCount`, given as a JSON number or as a string of digits, is the 0-based index.
> - searchablePullDown: a non-empty string is always the text of an item (also `"3"`), which Vectorworks looks up when the setting is applied. An index must be a JSON number below `choiceCount`.
> - A choice whose text ends in `...` and an index into a searchablePullDown need `allowDialog`: true.
>
> **Note:** The check before the first change covers the control and the form of the value. It cannot know whether Vectorworks accepts the text of an edit field or the item text of a searchablePullDown, so such a value can fail when it is applied, after the earlier settings were applied (its entry has `ok` false and `allApplied` is false). A refusal in the check returns only `err`, which ends with `; nothing was changed`.
>
> **Note:** `results` has one entry for each setting that was tried; the settings after a failure are not tried (`notAttemptedCount`). `label` and `controlId` are those of the control found in the check before the first change; for a setting named by `label`, an earlier setting that rebuilt the palette can give the control another id, so read the controls again with getOIPControls before using a `controlId` from `results`. `value` is read back from the rebuilt palette and is left out when the control is no longer shown. The top-level `pane` is the `pane` of the call; the `pane` of a setting is not repeated in its entry. When the first setting fails, `err` is the reason followed by `; nothing was changed`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pane` | string |  | One of: `shape`, `data`, `render`. Default: `shape`. |
| `settings` | array of object | Yes | 1 to 50 items, applied in order. |
| `settings[].label` | string |  | Label of the control: the first visible control with that label (case-insensitive; leading and trailing blanks and a trailing `:` are ignored, blanks inside the label count). Exactly one of `label` and `controlId` is required. |
| `settings[].controlId` | integer |  | `controlId` from getOIPControls; also finds a hidden control, which is then refused. Exactly one of `label` and `controlId` is required. |
| `settings[].value` | string or number or boolean | Yes | The new value; how it is read depends on the type of the control (see the Note above). |
| `settings[].pane` | string |  | One of: `shape`, `data`, `render`. Default: the `pane` of the call. |
| `allowDialog` | boolean |  | Default false. Needed for a choice that opens a dialog (its text ends in `...` or `…`) and for an item picked by index in a searchablePullDown. |

Errors: `'pane' must be shape, data or render` and `'allowDialog' must be true or false`. In the check, `err` ends with `; nothing was changed`. It is, for example, `'settings' is missing: give an array of 1 to 50 objects with 'label' or 'controlId' and 'value'`; or it names the setting as `settings[<index>]` and says what is wrong: no `value`; `give 'label' or 'controlId'` (or `..., not both`); `no control labeled '<label>' in the <pane> pane` (or `no control with controlId <id> in the <pane> pane`); a control that is hidden, disabled, read-only, a button, a staticText or of type other; a value that does not fit the control; a choice that opens a dialog without `allowDialog`: true. While applying (in `results[].err`, without the `settings[<index>]` prefix): `Vectorworks did not accept <value> for '<label>'` (`<value>` is the JSON text of `value`, a string in double quotes; also returned when an earlier setting disabled the control, made an edit field read-only, or hid a control named by `controlId`); `no control labeled '<label>' in the <pane> pane` (when an earlier setting removed or hid the control) or `no control with controlId <id> in the <pane> pane` (when an earlier setting removed it); and `the Object Info palette changed after an earlier setting; read the controls again with getOIPControls` when a control now has another type or, named by `controlId`, another label.

### pressOIPButton

Presses a button of the Object Info palette.

> **Effect:** Interactive · **Risk:** medium · **Undo:** recorded by Vectorworks as for user input · **In runToolBatch:** no

**Details**

Press a button of the Object Info palette, as a user clicks it: `label` or `controlId` names it in `pane` (default shape). Refused, with nothing pressed, when the pane has no controls, the control is unknown, hidden, disabled or not a button, or the button opens a dialog (its label ends in "...": `opensDialog` in getOIPControls) and `allowDialog` is not true - then tell the user that the dialog will open and that they must close it there, and call again with `allowDialog`: true.

Returns `pane`, `label`, `controlId` and `pressed`: true. Pressing may rebuild the palette: read the controls again afterwards.

> **Note:** `label` and `controlId` are used as in setOIPValues: exactly one is required; a `label` finds the first visible control with that label; a `controlId` also finds a hidden control, which is then refused.
>
> A refusal returns only `err`, ending with `; nothing was pressed`: `<control> is hidden`, `<control> is disabled`, `<control> is not a button (type <type>)`, `<control> opens a dialog in Vectorworks: tell the user that it will open and that they must close it there, then call again with 'allowDialog': true`, a pane that shows no controls, and a control that is named wrongly or not found (`give 'label' or 'controlId'` or `..., not both`, `'label' must be a non-empty string`, `'controlId' must be an integer`, `no control labeled '<label>' in the <pane> pane`, `no control with controlId <id> in the <pane> pane`). `<control>` is `'<label>'`, or `controlId <id>` when the label is empty. When Vectorworks does not accept the press, `err` is `<control> could not be pressed`, without that ending.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `pane` | string |  | One of: `shape`, `data`, `render`. Default: `shape`. |
| `label` | string |  | Label of the button: the first visible control with that label (case-insensitive; leading and trailing blanks and a trailing `:` are ignored, blanks inside the label count). Exactly one of `label` and `controlId` is required. |
| `controlId` | integer |  | `controlId` from getOIPControls; also finds a hidden control, which is then refused. Exactly one of `label` and `controlId` is required. |
| `allowDialog` | boolean |  | Default false. Needed when the label of the button ends in `...` or `…`. |

Errors: `'pane' must be shape, data or render` and `'allowDialog' must be true or false`, before anything is looked up.
