---
name: mcp-docs
description: 'Regenerate, update or check the Vectorworks MCP server tool reference (the pages in MCP/v<year>.<update>/) from a Vectorworks source tree, optionally verified against a running Vectorworks MCP server. Use when documenting a new Vectorworks version or update, when MCP tool groups, tools, descriptions or input schemas were added or changed, when fixing or adding summaries and parameter notes, or when validating the reference pages (links, coverage, external wording, live server).'
argument-hint: 'Version to document (for example "Vectorworks 2028 Update 1") and the source folder'
---

# MCP tool reference generator

Builds the reference of the Vectorworks MCP server tools (one page per tool folder, `Common.md`, `Attributes.md` and
`README.md` in `MCP/v<year>.<update>/`) from the Vectorworks source of the documented version, then checks it.
Standard library only (tested with Python 3.13). The rules for the pages themselves are in
[mcp-docs.instructions.md](../../instructions/mcp-docs.instructions.md).

## Inputs

| Option | Example | Notes |
|---|---|---|
| `--source` | `<source tree>/.../Interfaces/VectorWorks` | The folder of the documented version that contains `MCP/` (one subfolder per page, holding the tool group definitions) and `API/Resources/` (name lists that some schemas enumerate). It is the same folder the pythonapi-docs skill uses. It differs per version and per machine: ask the user when you don't know it, never hard-code it. |
| `--catalog` | `catalog.json` | Instead of `--source`: a catalog written by an earlier build (`catalog.json` in the work folder) or by `extract.py`. |
| `--version` | `Vectorworks 2028 Update 1` | Label shown on every page. |
| `--out` | `MCP/v2028.1` | One folder per version: `v<year>.<update>`. |
| `--live [URL]` | `--live` | Optional: also compare the catalog with a running Vectorworks MCP server (default `http://localhost:8765`). Read-only: it never activates groups or calls tools that change anything. Use it whenever Vectorworks of the documented version is running with its MCP server. |

Without access to the source tree you cannot regenerate: make small fixes by hand in the pages *and* in the
generator inputs (below), so the next build keeps them.

## Procedure

1. Build and check without touching the repository (run from the repository root):
   ```
   python .github/skills/mcp-docs/scripts/build.py --source "<Interfaces/VectorWorks folder>" --version "Vectorworks 2028 Update 1" --out MCP/v2028.1 --check-only --live
   ```
   The catalog is extracted (`catalog.json`), each folder, group and tool must have its hand-written text, the pages
   are rendered into a staging folder (`mcp-docs-build` in the temp folder; change it with `--work`), then the checks
   run: links, anchors, tables, tables of contents and code; coverage of every group, tool and parameter; external
   wording; with `--live`, the running server.
2. Fix every failure (see [Fixing problems](#fixing-problems)) and repeat until it prints "All checks passed".
3. Go through the review list it prints (not failures): hand-written texts that no longer match any group, tool,
   parameter or text. Read `broad.txt` next to the staged pages: sentences with weaker wording signals (core, SDK,
   internal, ...) for a manual check.
4. Run the same command without `--check-only`: the pages are copied into `--out` and the number of changed pages is
   printed. Other files there are left alone. Delete a page yourself only when its tool folder was removed.
5. New version: add a row to the version table of the hand-maintained `MCP/README.md`, for example
   `| Vectorworks 2028 Update 1 | [v2028.1](v2028.1/README.md) |`. Add the row to `MCP.de/README.md` and
   `MCP.ja/README.md` too, linking a translated version folder there when it exists and the English one otherwise
   (`[v2028.1](../MCP/v2028.1/README.md)`).
6. Read the diff (`git diff -- MCP`) and spot-check changed pages against the
   [instruction file](../../instructions/mcp-docs.instructions.md).

## Fixing problems

| Symptom | Fix |
|---|---|
| `Cannot evaluate <file>: ...` | A group definition uses a construct the extractor does not know yet: extend the interpreter (`Interp`) in [extract.py](./scripts/extract.py), or the tokenizer [cpptok.py](./scripts/cpptok.py). |
| `summaries.FOLDERS` / `CATEGORIES`: no entry, in no category | A new tool folder (a new page): add its tagline and introduction to `FOLDERS` and put it in one of the `CATEGORIES` of [summaries.py](./scripts/summaries.py). A removed folder: drop it from both and delete its page. |
| `summaries.GROUP_SUMMARY` / `TOOL_SUMMARY`: no entry | A new group or tool: write a one-line summary in [summaries.py](./scripts/summaries.py), in the style of the others (tools start with a verb: "Creates ...", "Returns ..."). |
| `mdlib.EFFECTS: unknown effect` | A new tool effect: add its label, undo text and batch rule to `EFFECTS` and its risk level to `tool_safety` in [mdlib.py](./scripts/mdlib.py), describe it in `EFFECT_INFO` in [shared.py](./scripts/shared.py), and add its name to the `effect name` pattern of [audit_terms.py](./scripts/audit_terms.py). |
| `shared.py names the tool X, which is not in the catalog` | `Common.md` or `Attributes.md` refers to a removed or renamed tool: update the lists in [shared.py](./scripts/shared.py) (`PAGED`, `NESTED_PAGED`, the section texts). |
| validate: `missing file`, `missing anchor`, cell count, code span, JSON block | Usually a link or a value in hand-written text, an unescaped `\|` in a table cell, or an example in `shared.py` (`CORE_EXAMPLE`, ...). |
| coverage: `no section`, `parameter ... is not in the table` | A rendering bug in [pages.py](./scripts/pages.py) or `schema_rows` in [mdlib.py](./scripts/mdlib.py). |
| wording hits | Implementation vocabulary reached a page. In a tool or group description from the server: add an exact rewrite to `REPLACEMENTS` in [summaries.py](./scripts/summaries.py) (and tell the user, since the server text says it too). In hand-written text: rewrite it. When the hit is legitimate public wording, narrow the `STRICT` pattern instead. |
| live: `description differs`, `input schema differs`, tools differ | The running Vectorworks is not built from the same source as `--source`. Use the matching build or source; never edit the catalog by hand. |
| live: `group Core: ... differs from core.json` | The always-available Core group (defined by the server, not under `MCP/`) changed: run `live.py <catalog> --update-core`, then review the Core texts in [shared.py](./scripts/shared.py) (`CORE_SUMMARY`, `CORE_EFFECT`, `CORE_SCHEMA`, `CORE_EXAMPLE`). |
| live: `Core tool X: input schema differs from shared.CORE_SCHEMA` | Update `CORE_SCHEMA` in [shared.py](./scripts/shared.py) to the new structure (its descriptions are curated, only the structure is compared). |
| live warning: `currently active, inactive by default` | Not a failure: someone activated groups in this server session. |
| A parameter note is wrong or missing | Notes come from the schema; where the schema has none, from [paramnotes.py](./scripts/paramnotes.py): add a curated note to `TOOL`, suppress a misleading remark with `DROP`, or extend `GENERIC`. |
| review: unused entries | The group, tool or parameter was renamed or removed, or the server text changed: update the key or delete the entry. |

## Scripts

| Script | Use |
|---|---|
| [build.py](./scripts/build.py) | The entry point: extract, render, check, copy. |
| [extract.py](./scripts/extract.py) `--source ... --out catalog.json` | Only the catalog of groups, tools and schemas. |
| [validate.py](./scripts/validate.py) `<folder>` | Links, anchors, tables, tables of contents, code spans, JSON blocks, encoding of a version folder, English or translated. |
| [coverage.py](./scripts/coverage.py) `<catalog.json> <folder>` | Every group, tool and parameter documented. |
| [audit_terms.py](./scripts/audit_terms.py) `<folder> [--catalog catalog.json] [--broad report.txt]` | External wording gate; `--catalog` adds the internal names of that version; `--broad` lists weaker signals for a manual read. |
| [live.py](./scripts/live.py) `<catalog.json> [--url URL] [--update-core]` | Compare with a running server; `--update-core` refreshes [core.json](./scripts/core.json). |
| [summaries.py](./scripts/summaries.py), [paramnotes.py](./scripts/paramnotes.py), [shared.py](./scripts/shared.py) | The text you are most likely to edit: page introductions, categories, group and tool summaries, text replacements, parameter notes, the shared pages and the Core group. |

The pipeline, the catalog format and where each part of a page comes from are in
[references/generator.md](./references/generator.md). Changing a script: first confirm that building the current
version reproduces the published pages byte for byte (the build prints `0 changed`), so the diff shows only your
change.
