**English** • [Deutsch](../../MCP.de/v2027.2/Scripting.md) • [日本語](../../MCP.ja/v2027.2/Scripting.md)

# Scripting — Python scripting

> **Server:** Vectorworks MCP · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

Tools to run Python scripts in Vectorworks, read and save Python script resources, and look up the Python `api` module that scripts use.

## Table of contents

- [Overview](#overview)
- [Scripting](#scripting)
  - [listScripts](#listscripts)
  - [getScript](#getscript)
  - [saveScript](#savescript)
  - [describePythonApi](#describepythonapi)
  - [getPythonApiGuide](#getpythonapiguide)
  - [runPythonScript](#runpythonscript)
  - [runScript](#runscript)

## Overview

This folder holds 1 tool group with 7 tools in total.

| Group | Group ID | Active by default | Safety level | Tools | Summary |
|---|---|---|---|---|---|
| [Scripting](#scripting) | `scripting` | No | high | 7 | Run Python scripts, read and save Python script resources, and look up the Python `api` module. |

## Scripting

> **Group:** `Scripting` · **Group ID:** `scripting` · **Active by default:** No · **Safety level:** high · **Tools:** 7

**Run Python scripts, read and save Python script resources, and look up the Python `api` module.**

Run Python scripts in Vectorworks, read and save the Python script resources of the active document, and look up the Python `api` module that scripts use. runPythonScript runs Python code and runScript a saved Python script resource; listScripts and getScript read the script resources (name, language, palette, text); saveScript creates or updates a Python script resource without running it; describePythonApi returns the help text of an `api` class, enum, function or member and, without a name, lists the names of `api` and `api.Math`. getPythonApiGuide returns the guide for writing these scripts, one section per call: read it before writing one.

Write scripts for the Python `api` module only (import api, then api.Document() and the other classes), not for the `vs` module. Its names have no C++ prefix (api.Document, not api.CDocument), so look every class up with describePythonApi before using it. Print results as JSON (json.dumps) to get them back in `output`. Each run is ONE undo step 'MCP: script' (a run that registers no change leaves none): the script's own undo event calls are ignored, so it must register what it creates (doc.AddAfterSwapObject(obj.GetHandle())) and what it changes (doc.AddBothSwapObject(handle), before the change), otherwise Undo cannot revert it.

A run that fails is reverted (`rolledBack`), so nothing that it registered stays: fix the script and run it again; changes that the script did not register cannot be reverted. A script must never wait for user input (GetPt, dialogs), and an endless loop freezes Vectorworks. A run is refused while another script runs or an undo event is open, and a script of more than 250 lines that deletes something or changes a record format runs only after the user confirms it in Vectorworks.

Scripts run with the rights of the user, now or later from their palette: ask the user before each run and say what the script will do, and tell the user what you saved and where. This is why the group has safety `high` and is off by default. Use it only when the user asks to run, read, write or document a script. Each saveScript is its own named, undoable Vectorworks operation.

> **Note:** The tools mode of the server decides whether this group is offered. In "Enable scripting tools only" it is the only group besides Core and it is active from the start; in "Enable all without scripting tools" it is not offered at all. See [Tool groups and activation](Common.md#tool-groups-and-activation).

| Tool | Effect | Safety | Summary |
|---|---|---|---|
| [`listScripts`](#listscripts) | Read-only | low | Lists the script resources of the document. |
| [`getScript`](#getscript) | Read-only | low | Reads a script resource without running it. |
| [`saveScript`](#savescript) | Edit | medium | Creates or updates a Python script resource without running it. |
| [`describePythonApi`](#describepythonapi) | Read-only | low | Returns the help text of the Python `api` module or one of its names. |
| [`getPythonApiGuide`](#getpythonapiguide) | Read-only | low | Returns one section of the guide for writing Python scripts. |
| [`runPythonScript`](#runpythonscript) | Script run | high | Runs Python code in Vectorworks. |
| [`runScript`](#runscript) | Script run | high | Runs a saved Python script resource. |

### listScripts

Lists the script resources of the document.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

List the script resources of the active document, sorted by name: `name`, `language` (`python` or `vectorscript`) and `palette` (the name of the script palette that holds the script). Paged by `limit` (default 200) and `offset`; `count` is the total and `truncated` says whether more follow; `countOnly` returns only the count. Nothing is run or changed.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `limit` | integer |  | Paging: the maximum number of items to return (at least 1). The default is 200. See [Paging](Common.md#paging). |
| `offset` | integer |  | Paging: the number of items to skip (default 0). |
| `countOnly` | boolean |  | Paging: return only the counts, without the items. |

**Result**

| Key | Description |
|---|---|
| `scripts` | This page of the script resources, sorted by name, as a list of `{ "name", "language", "palette" }`. `language` is `unknown` when it cannot be read. Left out with `countOnly`. |
| `count`, `returned`, `offset`, `limit`, `truncated`, `nextOffset` | The paging keys (see [Paging](Common.md#paging)). |

### getScript

Reads a script resource without running it.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Read the script resource `name` (1 to 63 characters): `name`, `language` (`python` or `vectorscript`), `palette` and the `text` with LF line breaks. The script is not run. Errors: `name` missing, empty, not a string or longer than 63 characters; no script resource has that name (a saved view or another object of that name is not a script); the script text is larger than 256 KB.

> **Note:** A `name` that has only spaces or contains control characters is refused like an empty one. The read errors are `script not found: <name>`, `the text of the script cannot be read: <name>` and `the script is larger than 256 KB (<n> bytes) and cannot be returned: <name>`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | 1 to 63 characters. |

### saveScript

Creates or updates a Python script resource without running it.

> **Effect:** Edit · **Safety:** medium · **Undo:** one step "MCP: saveScript" · **In runToolBatch:** yes

**Details**

Create or update the Python script resource `name` (1 to 63 characters) with `code` (at most 256 KB of UTF-8, no NUL characters) WITHOUT running it; write the code for the Python `api` module only. A new script is created in the script palette `palette` (1 to 63 characters, default 'MCP Scripts'); a missing palette is created and opened (`paletteCreated`: true).

When a script with that name exists, only its text is replaced: it keeps its palette and language, and a given `palette` is ignored (`paletteIgnored`: true). An existing VectorScript script is never changed. Returns `name`, `language`, `palette`, `created` and `codeLength` (the UTF-8 bytes of `code`). A script palette can keep running a compiled copy of a script it ran before until the script is edited in Vectorworks or the document is reopened.

**Errors:** `name`, `code` or `palette` missing, not a string or beyond its limit; `name` used by another object (a script palette included); `palette` equal to `name` or the name of an object that is not a script palette; the existing script is a VectorScript script.

> **Note:** `palette` is optional (default 'MCP Scripts'), although the Errors sentence lists it as missing: its format errors apply only when `palette` is given. When a new script is created, a `name` equal to its palette (the given one or 'MCP Scripts'), in any letter case, is refused, and so is a palette name that an object other than a script palette has; for an existing script these two checks are skipped. A `name` or `palette` that has only spaces or contains control characters is refused. When the script exists and `palette` is given (even when it names the palette that holds the script), the result has `created`: false, `paletteIgnored`: true and a `note`. `paletteCreated` (true) is returned only when a new script made its palette. An empty `code` is accepted. The errors of the change are `a script cannot have the name of its palette ('<palette>'); change 'name' or 'palette'`, `the name is the name of a script palette: <name>`, `the name is already used by another object of the document: <name>`, `the palette name is used by an object that is not a script palette: <palette>`, `failed to create the script '<name>' in the palette '<palette>'`, `the language of the script cannot be read: <name>`, `the script is a VectorScript script and is not changed (saveScript only changes Python scripts): <name>` and `failed to replace the text of the script: <name>`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | 1 to 63 characters. |
| `code` | string | Yes | At most 256 KB of UTF-8, no NUL characters. |
| `palette` | string |  | 1 to 63 characters, default 'MCP Scripts'. |

### describePythonApi

Returns the help text of the Python `api` module or one of its names.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Look up the Python `api` module that scripts use, with a fixed read-only Python script: nothing in the arguments is run as code. `name` (optional) is a dotted name that is resolved from the `api` module, with an optional leading `api.`: 1 to 8 parts of letters, digits and `_` that do not start with a digit, at most 128 characters. Python names have no C++ prefixes: `Document`, `Document.StartUndoEvent`, `WallObject.HeightBound` or `Math.Point2D`, not `CDocument`.

Returns `text`: the help of that class, enum, function or member as pydoc prints it in plain text (a constant shows its value; the sub-module `Math` lists its names), cut at 256 KB (`truncated`: true). Without `name`, `text` lists the names of the `api` and `api.Math` modules by kind (modules, classes, enums, functions, constants): use it to find class names.

**Errors:** `name` not a string or not a valid dotted name (refused before any script runs); 'unknown api name'; the Python engine cannot run now (no document, another script is running, engine unavailable) or the lookup failed.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | A dotted name that is resolved from the `api` module, with an optional leading `api.`: 1 to 8 parts of letters, digits and `_` that do not start with a digit, at most 128 characters. Without it, `text` lists the names of the module. An empty string or `null` counts as no `name`. The 128 characters include a leading `api.`. |

**Result**

| Key | Description |
|---|---|
| `name` | The name that was looked up, without a leading `api.`. Only when `name` was given. |
| `text` | The help text. |
| `truncated` | `true` when `text` was cut at 256 KB. |

### getPythonApiGuide

Returns one section of the guide for writing Python scripts.

> **Effect:** Read-only · **Safety:** low · **Undo:** none · **In runToolBatch:** allowed

**Details**

Return the guide for writing Vectorworks Python scripts that use the `api` module, one section per call, as Markdown text with LF line breaks. Nothing is run or changed. Call it first without `section`: `text` is then the start of the guide (its title, table of contents and introduction), `sections` lists sections 1 to 6 (`section`, `title`, and `bytes`: the size of its text) and `reference` tells where to look up section 7.

The sections: 1 Rules; 2 Where things are; 3 Undo, which ends with the rules for scripts run through MCP (read sections 1 and 3 before the first runPythonScript); 4 Recipes; 5 Tools, menus and the Object Info Palette; 6 Gotchas. With `section` (an integer from 1 to 6) it returns that section: `section`, `title` and `text` (from its heading '## n. ' to the next section).

`truncated` is true when a `text` was cut at 256 KB. Section 7 (Reference) is not returned: where the guide refers to section 7 or links to another .md page, look the class, function or member up with describePythonApi.

**Errors:** `section` not an integer from 1 to 6; section 7; the guide is not available (missing from the Vectorworks application resources, not valid UTF-8, or without one of its numbered sections): use describePythonApi then.

> **Note:** A `section` of `null` counts as omitted. The errors are `'section' must be an integer from 1 to 6` (also for a string such as `"3"` or a number such as 2.5), `Section 7 (Reference) is not returned: look classes, functions and members up with describePythonApi` and `the Python api guide is not available: <reason>`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `section` | integer |  | An integer from 1 to 6. |

### runPythonScript

Runs Python code in Vectorworks.

> **Effect:** Script run · **Safety:** high · **Undo:** one step "MCP: script" (none when the script registered no change) · **In runToolBatch:** no

**Details**

Run `code` as a Python script in Vectorworks: at most 256 KB of UTF-8, no NUL characters.

**HIGH RISK:** before each run, tell the user what the script will do and ask for permission. Write the code for the Python `api` module only (import api; not `vs`) and look its names up with describePythonApi (no C++ prefixes: api.Document, not api.CDocument). Print results as JSON (print(json.dumps(...))) to get them back in `output`. Before the first run, read sections 1 and 3 of the guide with getPythonApiGuide: section 3 ends with the rules for scripts run through MCP.

**Undo:** the whole run is ONE undo step 'MCP: script' (none when the script registered no change: Vectorworks keeps no empty step), and the script's own StartUndoEvent, NameUndoEvent, EndUndoEvent and RevertUndoEvent calls are ignored. The script must register what it creates (doc.AddAfterSwapObject(obj.GetHandle()), after creating it) and what it changes (doc.AddBothSwapObject(handle), BEFORE the change), otherwise Undo cannot revert it; Delete() needs no registration. A run that fails is reverted (`rolledBack`: true, no undo step), so nothing that it registered stays: fix the script and run it again; changes that the script did not register cannot be reverted. Never wait for user input (GetPt, dialogs): the run then ends as `Waiting` and no script can run until the user has finished. An endless loop freezes Vectorworks: scripts run on its main thread. The script does not run (`NotStarted`, no undo step) while another script runs or an undo event is open (another Vectorworks operation is in progress: try again later). A script of more than 250 lines that deletes something or changes a record format runs only after the user chooses Run in a Vectorworks alert; Cancel, or an alert that cannot be shown now, returns `NotStarted` with the reason. Never work around this check. Returns `status` (Succeeded, Failed, NotStarted or Waiting), `output` (the printed text) and `errors` (the tracebacks), each cut at 256 KB (`outputTruncated`, `errorsTruncated`), `undoStep` (true when the run left the undo step `undoName`; false when it registered no change, failed or did not start), `rolledBack` for a run that failed or did not start (true when what it registered was reverted), `err` when the script failed or did not run, `note` for Waiting and `warning` when an undo event is still open after the run.

**Errors:** `code` missing, empty, not a string, larger than 256 KB or with NUL characters.

> **Note:** `rolledBack` is returned only for a run that had started. A run that was refused before it started (another script runs, an undo event is open, the user cancelled the confirmation, or alerts are suppressed) has `status` `NotStarted` and an `err`, but no `rolledBack`: nothing was opened, so nothing was reverted.

> **Note:** Only the undo methods of `api.Document` are ignored. The undo calls of the `vs` module reach Vectorworks directly: a script that uses them can rename or end the undo step of the run. `warning` reports an undo event that is still open after the run.

> **Note:** The `err` of a run starts with `the script failed: `, `the script does not compile: ` or `the script did not run: `, followed by the reason, cut at 300 bytes.

> **Note:** The confirmation is a plain, case-sensitive text search of the script, comments and strings included. It applies only to a script of more than 250 lines (CRLF, CR and LF each end a line) that contains one of `.Delete(`, `DeleteSelection(`, `vs.DelObject`, `vs.DelRecord`, `RecordFormat.Create(`, `AddField(`, `RemoveField(`, `RenameField(`, `SetFieldDefaultValue(` or `SetFieldChoices(`.

> **Note:** The tool compares the undo history before and after the run by undo event id: `undoName` is the newest undo step that the run added, normally `MCP: script` (a script that renames the step with the undo calls of the `vs` module reports the new name). When the undo history cannot be read, the step is taken to be there and `undoStep` is true. With `undoStep` false after a run that succeeded, Edit &gt; Undo reverts the step before the run. A run that ends as `Waiting` also ends its undo step; changes that the script makes after the input are not part of it.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | Not empty, at most 256 KB of UTF-8, no NUL characters. |

### runScript

Runs a saved Python script resource.

> **Effect:** Script run · **Safety:** high · **Undo:** one step "MCP: script" (none when the script registered no change) · **In runToolBatch:** no

**Details**

Run the current text of the saved Python script resource `name` (1 to 63 characters), for example one saved with saveScript, the way runPythonScript runs `code`: ONE undo step 'MCP: script' when it registers a change, and a run that fails is reverted (`rolledBack`), so nothing that it registered stays: fix the script (saveScript) and run it again; changes that the script did not register cannot be reverted.

The same rules for the script, the same refusals and confirmation (they check the text of the script) and the same result, with `name`.

**HIGH RISK:** before each run, tell the user which script runs and what it does, and ask for permission.

**Errors:** `name` missing, empty, not a string or longer than 63 characters; no script resource has that name (a saved view or another object of that name is not a script); the script is a VectorScript script (only Python scripts run).

> **Note:** A `name` that has only spaces or contains control characters is refused like an empty one. The error texts are `script not found: <name>`, `the script cannot be read: <name>` and `the script is a VectorScript script and is not run (runScript runs only Python scripts): <name>`. When the script is deleted or renamed while the confirmation alert is open, the result is `NotStarted` with `The script '<name>' was deleted or renamed before it could run.`. The result also has `name`. The notes of [runPythonScript](#runpythonscript) on `rolledBack`, the undo calls of the `vs` module, the confirmation search and `undoStep` apply here too. An empty saved script (`The script is empty.`), or one that was deleted or renamed during the confirmation, ends `NotStarted` after the undo step was opened, so its result has `rolledBack`.

**Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | 1 to 63 characters. |
