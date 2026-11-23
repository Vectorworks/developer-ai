**English** • [Deutsch](../../PythonAPI.de/v2027.2/Scripting.md) • [日本語](../../PythonAPI.ja/v2027.2/Scripting.md)

# Scripting — script resources and script palettes

> **Python module:** `api` · **Version:** Vectorworks 2027 Update 2

[Back to the index](README.md)

The scripting classes: `ScriptResource` is a VectorScript or Python script stored in the current document (create, find, read, change and delete it) and `ScriptPalette` is a script palette, the named group of script resources that Vectorworks shows as a floating palette and as a folder of scripts in the Resource Manager.

Scripts can be created, read, changed and organized through this API; running them is not part of the API.

## Table of contents

- [Overview](#overview)
- [Classes](#classes)
  - [ScriptResource](#scriptresource)
  - [ScriptPalette](#scriptpalette)
- [Enumerations](#enumerations)
  - [ScriptLanguage](#scriptlanguage)

## Overview

| Name | Kind | Inherits from | Summary |
|---|---|---|---|
| [`ScriptResource`](#scriptresource) | class |  | One script resource, identified by its handle. |
| [`ScriptPalette`](#scriptpalette) | class |  | One script palette, identified by its handle. |
| [`ScriptLanguage`](#scriptlanguage) | IntEnum |  | Language of a script. |

## Classes

### ScriptResource

> **Full name:** `api.ScriptResource` · **Inherits:** `api.Object`

One script resource, identified by its handle. Like every object class of this API it is a lightweight view: copying it does not copy the script and destroying it does not delete the script. Constructing it from a handle that is not a script resource produces an invalid object (`IsValid()` == `False`); getters then return `None` and setters / operations return `False`. Strings are UTF-8; script texts use "\n" line breaks.

**Constructors**

| Constructor | Description |
|---|---|
| `ScriptResource(hScript: Handle)` | Refers to the existing script `hScript`; check `IsValid()` before use. |

**Methods**

*Type*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | `True` when the handle is a script resource (saved views are not). |

*Lookup*

| Method | Description |
|---|---|
| `FromName(name: str) -> ScriptResource` *static* | Script resource of the current document with that name; invalid when there is none. |
| `GetAll() -> list[ScriptResource]` *static* | Every script resource of the current document, sorted by name. |

*Creation*

| Method | Description |
|---|---|
| `Create(name: str, paletteName: str, text: str, language: ScriptLanguage) -> ScriptResource` *static* | Creates a script resource in the script palette `paletteName`; a missing palette is created, and opened, first. Fails (invalid object) when `name` or `paletteName` is empty or longer than 63 characters, when both are the same, when an object of the document already uses `name`, or when `paletteName` names an object that is not a script palette. Undo: Vectorworks registers a new palette, but not the new script. Inside an undo event, register the script with `Document.AddAfterSwapObject`; do not register the palette again. |

*Identity*

| Method | Description |
|---|---|
| `GetHandle() -> Handle` | Handle of the script. |
| `IsValid() -> bool` | True when this object refers to an existing script. |
| `GetName() -> str \| None` | Returns the name. |
| `SetName(name: str) -> bool` | Renames the script; fails when the name is longer than 63 characters or another object already uses it. |

*Script*

| Method | Description |
|---|---|
| `GetLanguage() -> ScriptLanguage \| None` | Returns the language. |
| `GetText() -> str \| None` | Returns the text. |
| `SetText(text: str) -> bool` | Replaces the text and keeps the language. A script palette keeps a compiled copy of a script it ran, and runs that copy when the user runs the script from the palette again, until the script is edited in Vectorworks or the document is reopened. Execute always runs the current text. |
| `SetText(text: str, language: ScriptLanguage) -> bool` | Replaces the text and the language (see SetText above). |

*Script palette*

| Method | Description |
|---|---|
| `GetPalette() -> ScriptPalette` | Palette that contains the script. |

*Lifetime*

| Method | Description |
|---|---|
| `Delete(useUndo: bool = True) -> bool` | Deletes the script from the document; the object becomes invalid. Fails while a script is running, since the running script could be the deleted one. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True when the object is valid (same as `IsValid()`). |
| `==` | `__eq__(o: ScriptResource) -> bool` | `a == b`: True when both objects refer to the same script. |
| `!=` | `__ne__(o: ScriptResource) -> bool` | `a != b`: True when the objects refer to different scripts. |

### ScriptPalette

> **Full name:** `api.ScriptPalette` · **Inherits:** `api.Object`

One script palette, identified by its handle. Lightweight, like ScriptResource. Constructing it from a handle that is not a script palette produces an invalid object (`IsValid()` == `False`); getters then return `None` and setters / operations return `False`.

**Constructors**

| Constructor | Description |
|---|---|
| `ScriptPalette(hPalette: Handle)` | Refers to the existing script palette `hPalette`; check `IsValid()` before use. |

**Methods**

*Type*

| Method | Description |
|---|---|
| `Is(h: Handle) -> bool` *static* | `True` when the handle is a script palette (the Saved Views palette is not). |

*Lookup*

| Method | Description |
|---|---|
| `FromName(name: str) -> ScriptPalette` *static* | Script palette of the current document with that name; invalid when there is none. |
| `GetAll() -> list[ScriptPalette]` *static* | Every script palette of the current document, sorted by name. |

*Identity*

| Method | Description |
|---|---|
| `GetHandle() -> Handle` | Handle of the script palette. |
| `IsValid() -> bool` | True when this object refers to an existing script palette. |
| `GetName() -> str \| None` | Returns the name. |
| `SetName(name: str) -> bool` | Renames the palette; fails when the name is longer than 63 characters or another object already uses it. |

*Scripts*

| Method | Description |
|---|---|
| `GetScripts() -> list[ScriptResource]` | Script resources of the palette, in palette order. |
| `GetScriptCount() -> int` | Number of script items. |

*Display*

| Method | Description |
|---|---|
| `SetOpen(isOpen: bool) -> bool` | Shows (`True`) or closes (`False`) the floating palette. |

*Lifetime*

| Method | Description |
|---|---|
| `Delete(useUndo: bool = True) -> bool` | Deletes the palette with all its scripts; the object becomes invalid. Fails while a script is running, since the running script could be one of the deleted ones. |

**Operators and Python protocols**

| Operator | Method | Description |
|---|---|---|
| `bool()` | `__bool__() -> bool` | `bool(a)`: True when the object is valid (same as `IsValid()`). |
| `==` | `__eq__(o: ScriptPalette) -> bool` | `a == b`: True when both objects refer to the same script palette. |
| `!=` | `__ne__(o: ScriptPalette) -> bool` | `a != b`: True when the objects refer to different script palettes. |

## Enumerations

### ScriptLanguage

> **Full name:** `api.ScriptLanguage` · **Kind:** `IntEnum`

Language of a script.

| Member | Value | Description |
|---|---|---|
| `VectorScript` | `0` | The Pascal like Vectorworks scripting language. |
| `Python` | `1` | Python, with the Vectorworks "vs" and "api" modules. |

---

[Back to the index](README.md) · [Back to top](#scripting--script-resources-and-script-palettes)
