**English** • [Deutsch](../../MCP.de/v2027.2/MenuAccess.md) • [日本語](../../MCP.ja/v2027.2/MenuAccess.md)

# MenuAccess — menu commands

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools that read the Vectorworks menus, check whether a command can run, and run menu commands as if the user chose them.

## Table of contents

- [Overview](#overview)
- [Menus](#menus)
  - [findMenuCommands](#findmenucommands)
  - [getMenus](#getmenus)
  - [getMenuStatus](#getmenustatus)
  - [runMenuCommand](#runmenucommand)

## Overview

This folder holds 1 tool group with 4 tools in total.

| Group | Group ID | Active by default | Safety level | Tools | Summary |
|---|---|---|---|---|---|
| [Menus](#menus) | `menus` | No | high | 4 | Find menu commands, read the menu bar, check whether a command can run now, and run it. |

## Menus

> **Group:** `Menus` · **Group ID:** `menus` · **Active by default:** No · **Safety level:** high · **Tools:** 4

**Find menu commands, read the menu bar, check whether a command can run now, and run it.**

Read the Vectorworks menus and run their commands: the installed menu commands, the menus of the menu bar of the current workspace with their submenus, commands and chunk items, whether a command or a chunk item is enabled or checked now, and runMenuCommand, which runs a command or chunk item as if the user chose it. Use this group to find out whether and where Vectorworks offers a command for a task (to guide the user to it), what a command does, whether it can run in the current state (an open document, a selection, ...) or is checked (e.g. a view option), and the current items of chunks such as the recent files, the standard views or the open documents. findMenuCommands, getMenus and getMenuStatus only read: nothing in the drawing changes (no undo step). runMenuCommand is high risk: a menu command can change or remove data and open dialogs, and it records its own undo step; ask the user before each call.

Prefer the dedicated tools of the other groups for the changes they cover.

Names: a command has a `universalName` (its stable identity; built-in commands use a negative number such as "-28"), a `name` (the English name; equals universalName for plug-in commands) and a `displayName` (the localized title that the menus show). The tools take any of them, case-insensitive, with or without a trailing "..."; prefer universalName. Menu titles and entry texts are localized, as the user sees them.

Installed and in the workspace: findMenuCommands lists every installed command; `inWorkspace` tells whether the menus of the current workspace contain it. Only commands in the workspace can be enabled, and only chunks in the workspace have items.

**Chunks:** a chunk is a command that provides a group of menu items (the recent files, the standard views, ...). An item is named by the universalName of its chunk and its 0-based index or its text. A chunk is regular (fixed items), dynamic (items built with the menu bar) or variable (items that change while Vectorworks runs). Item texts and check marks are as Vectorworks last updated the menus, which it does when the user opens them, so they can be out of date; `enabled` is always current. On Mac, chunk items have no `checked`.

Workflow:

1. findMenuCommands `search` finds candidate commands.
2. getMenus `search` or `menu` shows where they are in the menus; getMenus `chunk` lists the items of a chunk.
3. getMenuStatus tells whether a command or chunk item could run now, and why not.
4. runMenuCommand runs it, after the user agreed.

| Tool | Effect | Safety | Summary |
|---|---|---|---|
| [`findMenuCommands`](#findmenucommands) | Read-only | low | Finds installed menu commands by text and by workspace. |
| [`getMenus`](#getmenus) | Read-only | low | Reads the menu bar of the current workspace, one menu, or the items of a chunk. |
| [`getMenuStatus`](#getmenustatus) | Read-only | low | Tells whether a menu command or chunk item can run now, and why not. |
| [`runMenuCommand`](#runmenucommand) | Interactive, destructive | high | Runs a menu command or chunk item as if the user chose it. |

### findMenuCommands

Finds installed menu commands by text and by workspace.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Find installed menu commands. `search` keeps the commands whose universalName, name, displayName, category or helpText contains the text (case-insensitive). `filter`: all (default: every installed command), inWorkspace (in the menus of the current workspace) or enabled (Vectorworks could run it now; a chunk: at least one of its items). Or `name` looks up one command by universalName, name or displayName (case-insensitive, a trailing "..." optional; on a tie a command in the workspace wins), not together with `search` or `filter`.

`limit` (default 50) and `offset` page the list; `countOnly` (default false) returns the paging keys without `commands`. Returns `commands` (this page), `count` (all matches), `returned`, `offset`, `limit`, `truncated` and `nextOffset` when more follow, and `filter` - or `name` when `name` is given. A `name` that no command has is not an error: `count` 0 and a `hint`.

Each command has `universalName`, `name`, `displayName`, `category` (its category in the Workspace Editor), `helpText`, `kind` (internal, scriptPlugin, extensionPlugin or unknown), `isChunk`, `inWorkspace`, `enabled` and `shortcut` when the workspace assigns one.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Looks up one command by universalName, name or displayName (case-insensitive). A trailing "..." may be left out of, or added to, the displayName only; universalName and name must match apart from case. Not together with `search` or `filter`. |
| `search` | string |  | Text filter: keeps the commands whose universalName, name, displayName, category or helpText contains this text (case-insensitive for the ASCII letters). |
| `filter` | string |  | One of: `all`, `inWorkspace`, `enabled`. Default: `all`. |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). Default: 50. See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

Errors: `'filter' must be all, inWorkspace or enabled`; `'name' cannot be used with 'search' or 'filter'`; `'name' must be a non-empty string` or `'search' must be a non-empty string` for an empty or non-string value.

### getMenus

Reads the menu bar of the current workspace, one menu, or the items of a chunk.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the menu bar of the current workspace; nothing is run.

**Without arguments:** `menus`, the titles of its menus from left to right. `menu` (a title from `menus`, case-insensitive) lists the entries of that menu depth first: a submenu entry is followed by the entries of its submenu, and a chunk by its current items; separators are left out. `search` keeps the entries whose text or universalName contains it (case-insensitive), in all menus or only in `menu`. `chunk` (the universalName, name or displayName of a chunk in the workspace; not together with `menu` or `search`) lists the current items of that chunk. `limit` (default 100) and `offset` page the list; `countOnly` (default false) returns the paging keys only. Returns `menus`, `entries` or `items` (this page) with `count`, `returned`, `offset`, `limit`, `truncated` and `nextOffset` when more follow; also `menu` when `menu` is given, and `chunk` (the command, as in findMenuCommands) for a chunk. An entry has `type` (command, chunkItem or submenu), `menuPath` (the titles of the menus that contain it, from the menu bar down, e.g. ["File", "Export"]) and `text`; a command or chunk item also `universalName`, `enabled` and `checked`, a chunk item `chunkKind` (regular, dynamic or variable) and `chunkItemIndex`, and any entry `shortcut` when it has one. An item of a `chunk` has `index` (its 0-based position in the chunk; positions of separators are skipped), `text`, `enabled` and `checked`. On Mac, chunk items have no `checked`.

**Errors:** a `menu` that the menu bar does not have; a `chunk` that no command is named, that is not a chunk or that is not in the workspace.

> **Note:** A `menu` that exists but has no entries at all fails too, and the error lists the titles of the menus: `no menu titled '<menu>' in the menu bar, or the menu is empty; its menus: <titles>` (a menu that has only separators returns an empty `entries` list, `count` 0, instead). A `menu` title matches with or without a trailing "...". `universalName` is left out of an entry that has none.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `menu` | string |  | A title from `menus`, case-insensitive; a trailing "..." may be left out. |
| `search` | string |  | Text filter: keeps the entries whose text or universalName contains this text (case-insensitive for the ASCII letters), in all menus or only in `menu`. |
| `chunk` | string |  | The universalName, name or displayName of a chunk in the workspace; not together with `menu` or `search`. |
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). Default: 100. See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

Errors: `'chunk' cannot be used with 'menu' or 'search'`; `'<key>' must be a non-empty string` for an empty or non-string `menu`, `search` or `chunk`; `'<chunk>' is the menu command '<universalName>', not a chunk: getMenuStatus tells whether it can run`; `the chunk '<universalName>' is not placed in the menus of the current workspace, so it shows no items`; `no installed menu command is named '<chunk>': search for it with findMenuCommands 'search'`.

### getMenuStatus

Tells whether a menu command or chunk item can run now, and why not.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Whether Vectorworks could run a menu command or a chunk item now, and why not; nothing is run. `name`: the universalName (preferred), name or displayName of the command or chunk. For a chunk, `chunkItemIndex` (an `index` or `chunkItemIndex` from getMenus) or `chunkItemText` (case-insensitive) names the item; a chunk with one item needs neither. Returns `name`, `status`, `enabled` (true for ready), `reason`, `command` (as in findMenuCommands) when a command has the name, and for ready or disabled `checked` (whether the menu shows a check mark; not for chunk items on Mac) and, for a chunk item, `chunkItemIndex` and `chunkItemText`.

`status`: ready; disabled (it needs another state: an open document, a selection, ...); notInWorkspace (installed, but not in the menus of the current workspace); notFound; chunkItemRequired (a chunk with several items: name one); chunkItemNotFound (no such item, or the command is not a chunk); unavailable (no command can run now: the menu bar is not set up or a plug-in object is being regenerated).

> **Note:** `chunkItemNotFound` is also the status of a chunk that has no items at the moment (when no item is named) and of a `chunkItemIndex` given for a command that is not a chunk. `checked` is read from the first menu-bar entry that runs the command and is left out when there is none, e.g. for a command placed only in a context menu. Like every Core tool, the call fails with `no active Vectorworks document` when no document is open (see [Results and errors](Common.md#results-and-errors)), so no command is reported as `disabled` for want of an open document.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | The universalName (preferred), name or displayName of the command or chunk. |
| `chunkItemIndex` | integer |  | An `index` or `chunkItemIndex` from getMenus (0 or more). Not together with `chunkItemText`. |
| `chunkItemText` | string |  | The text of the item, case-insensitive; a trailing "..." may be left out. Not together with `chunkItemIndex`. |

Errors: `'name' must be a non-empty string`; `'chunkItemText' must be a non-empty string`; `'chunkItemIndex' must be a whole number of 0 or more`; `'chunkItemIndex' and 'chunkItemText' cannot be used together`.

### runMenuCommand

Runs a menu command or chunk item as if the user chose it.

> **Effect:** Interactive, destructive · **Safety:** high · **Undo:** recorded by the menu command · **In runToolBatch:** no

**Details**

Run a Vectorworks menu command or chunk item as if the user chose it in the menu bar.

**High risk:** tell the user which command you will run and what it does, and run it only after they agreed. `name`: the universalName (preferred), name or displayName of the command or chunk, as in getMenuStatus; for a chunk, `chunkItemIndex` or `chunkItemText` names the item (a chunk with one item needs neither). It runs only when getMenuStatus would report ready; otherwise nothing runs, and the result has `err`, `ran` false and the keys of getMenuStatus (`status`, `reason`, `command`, ...).

**Dialogs:** the call returns only after the user closed the dialogs and alerts that the command opens, and no other call is answered meanwhile. A command or chunk item whose title ends with "..." opens a dialog, and SDK plug-in commands (kind extensionPlugin) may open one without "...": these are refused unless `allowDialog` is true, which you pass after telling the user that a dialog will open and that they must close it in Vectorworks. Any command can still show an alert (e.g. one that the license does not include).

**Refused before anything runs:** commands that open, save, print, close or switch documents or quit Vectorworks (New, Open, the recent files, the Home Screen, Close, Save, Save All, Revert, Export Previous Version, Print, Quit, the open documents of the Window menu, ...), refreshing a Project Sharing file, Undo and Redo, Cut and Copy (they replace the user's clipboard), repeating recent commands, Run Script, the Plug-in Manager, switching workspaces, and VectorScript or Python plug-in commands (kind scriptPlugin); and a ready command while a tool action is in progress or an undo event is open.

**Undo:** the command records its own undo step as in Vectorworks, not "MCP: runMenuCommand"; a failed call is not rolled back, and the tool cannot run in runToolBatch. Returns `ran` true, `command`, `chunkItemIndex` and `chunkItemText` for a chunk item, `undoSteps` (the names of the undo steps that the command added, newest first; empty when it added none), `documentBefore` and `documentAfter` (the file names of the active document; `documentAfter` is null when none is open) with `documentChanged`, `activeTool` (the universalName of the active tool afterwards) with `activeToolChanged`, `waitingForInput` (true when the command left an undo step open or changed the active tool: it may wait for input in Vectorworks, e.g. clicks of a temporary tool; tell the user to finish or cancel it there, and make no other changes until then), and a `hint` for a changed document or waiting input. When the document changed, `undoSteps` is left out and later calls act on the new active document. Read the menus, the selection and the objects again afterwards.

> **Note:** The refusals and the dialog rule are checked first, and each returns only `err`: no `ran`, and none of the getMenuStatus keys that the paragraph above names. The texts are `'<title>' (<universalName>) is not run by runMenuCommand: it <reason>; ask the user to choose it in Vectorworks`, `'<dialogTitle>' opens a dialog in Vectorworks: tell the user that it will open and that they must close it there, then call again with 'allowDialog': true` and `'<title>' is an SDK plug-in command, which can open a dialog in Vectorworks: ...`. Because of this order, a disabled command whose title ends with "..." asks for `allowDialog` before its status is reported, so call getMenuStatus first. A title ends with "..." when its text, without trailing spaces, tabs and line breaks, ends with three dots or with the ellipsis character "…"; the rule is applied to the chunk item text and to the name and displayName of the command. Besides running scripts, the refused commands include encrypting scripts.
>
> Only a command that passed these checks and is not ready or not found returns the keys of getMenuStatus, plus `ran` false and `err` (`<reason>; nothing was run`). Two more refusals return only `err`: `a tool action is in progress in Vectorworks: the user must finish or cancel it first; nothing was run` and `an undo event is open in Vectorworks (another operation is in progress): a menu command records its own undo step and cannot run inside it; nothing was run`. A run that Vectorworks refuses or stops returns `err` (`'<title>' did not run: Vectorworks refused or stopped it, for example a command that the license does not include (an alert tells the user)`) and `ran` false, without the status keys.
>
> A temporary tool that waits for its first click is not noticed by the check for a tool action in progress, so a later call is not refused while it waits. After `waitingForInput` is true, make no further call until the user has finished or cancelled the tool in Vectorworks. Like every Core tool, the call fails with `no active Vectorworks document` when no document is open (see [Results and errors](Common.md#results-and-errors)).
>
> `undoSteps` compares the undo steps before and after the run by the id of their undo event, not by name: it names every step that the command added and that is still in the undo history (which keeps at most the "Maximum number of undos" of the Vectorworks preferences), also when its name repeats an earlier step.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | The universalName (preferred), name or displayName of the command or chunk, as in getMenuStatus. |
| `chunkItemIndex` | integer |  | An `index` or `chunkItemIndex` from getMenus (0 or more). Not together with `chunkItemText`. |
| `chunkItemText` | string |  | The text of the item, case-insensitive; a trailing "..." may be left out. Not together with `chunkItemIndex`. |
| `allowDialog` | boolean |  | Default: false. Must be true to run a command that opens or may open a dialog: its title ends with "..." or "…", or its kind is extensionPlugin. |

**Result**

A run that happened:

| Key | Description |
|---|---|
| `name` | The `name` as passed. |
| `ran` | `true`. |
| `command` | The command, as in findMenuCommands. |
| `chunkItemIndex`, `chunkItemText` | Only for a chunk item: the item that ran. |
| `documentBefore` | The file name of the active document (for an unsaved document, its untitled name) before the run. |
| `documentAfter` | The file name of the active document (for an unsaved document, its untitled name) afterwards; `null` when no document is open. |
| `documentChanged` | `true` when the active document is not the one from before: another document, none (`documentAfter` is `null`), the same file reopened, or the same document under another file path (e.g. it was saved under a new name). |
| `undoSteps` | The names of the undo steps that the command added, newest first (empty when it added none). Left out when the document changed, and when the undo steps cannot be read. |
| `activeTool` | The universalName of the active tool afterwards; `null` when there is none. |
| `activeToolChanged` | `true` when the run changed the active tool. |
| `waitingForInput` | `true` when the command left an undo event open or changed the active tool. |
| `hint` | Only when there is something to tell: a changed document or waiting input. |

Errors: `'allowDialog' must be true or false`, and the argument errors of getMenuStatus; the refusals, the not ready result and the failed run that the Note above describes.
