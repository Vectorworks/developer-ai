# Generator reference

How [build.py](../scripts/build.py) turns a Vectorworks source tree into the MCP tool reference, and where to change
what the pages say.

## Pipeline

| Step | Module | What it does |
|---|---|---|
| 1 | [cpptok.py](../scripts/cpptok.py) | Tokenizes the C++ sources under `MCP/` (preprocessor lines removed, string literals joined). |
| 2 | [extract.py](../scripts/extract.py) | Collects enumeration name tables, string arrays, constants and functions, then evaluates every `DefineGroup` body with a small interpreter of the C++ subset the groups use (schema builders, string concatenation, loops over name tables, the name lists of `API/Resources/`). The result is the catalog. |
| 3 | [render.py](../scripts/render.py) | `precheck()`: every folder, group and tool has its hand-written text and a known effect. `write_all()`: renders the pages in catalog order. `review()`: hand-written texts that match nothing any more. |
| 4 | [pages.py](../scripts/pages.py) | One page per tool folder: overview table, then per group its section and per tool its section. |
| 5 | [shared.py](../scripts/shared.py) | `Common.md` (calling conventions, results, references, formats, units, creation options, applied settings, plug-in parameters, paging, effects, undo, and the Core group) and `Attributes.md` (line end markers, drop shadows). |
| 6 | [readme.py](../scripts/readme.py) | The version `README.md`: getting started, conventions, tool tree, contents by category, A–Z index, page layout, statistics. |
| 7 | [mdlib.py](../scripts/mdlib.py) | Markdown helpers: `Page` (headings, GitHub anchors, table of contents), `inline` / `block` (quoted names become code spans, Markdown escaped outside code spans, labelled lists and paragraphs), `schema_rows` (the Parameters table), `EFFECTS` and `tool_safety`. |
| 8 | [validate.py](../scripts/validate.py), [coverage.py](../scripts/coverage.py), [audit_terms.py](../scripts/audit_terms.py), [live.py](../scripts/live.py) | The checks build.py runs. |

## Language navigation

After rendering, `build.py` runs the shared [language-selector helper](../../../scripts/doc_languages.py).
It adds a first-line selector linking to the same page in the same version folder of every existing language folder
(`MCP/v2027.2`, `MCP.de/v2027.2`, `MCP.ja/v2027.2`), with the current language bold. Missing translations are not
linked; English-only pages remain unchanged. Staging uses the final `--out` location, and validation checks those
parent-relative links.

To refresh existing pages in every language after adding translations, without regenerating their bodies:

```text
python .github/scripts/doc_languages.py MCP/v2027.2 MCP.de/v2027.2 MCP.ja/v2027.2
```

## Catalog

`catalog.json` is a list of groups in definition order (folder by folder):

| Key | Meaning | Published |
|---|---|---|
| `fName`, `fDesc` | Group display name and description (the server reports `fDesc` as `shortDescription`). | Yes |
| `fActiveByDefault`, `fSafetyLevel` | Activation at session start; `low`, `medium` or `high`. | Yes |
| `groupId` | Derived from the display name as the server does: lowercase, every run of other characters than `a-z0-9` becomes one `-`, ends trimmed (`3D Modeling` → `3d-modeling`). | Yes |
| `folder` | Subfolder of `MCP/`: the page the group is on. | As the page name |
| `class` | C++ class of the group. | Never; the wording audit flags it |
| `tools[]` | `name`, `effect`, `description`, `inputSchema` (JSON schema, as the server sends it), `file` and `handlerFile` (source files; never published, flagged by the audit). | Except `file`, `handlerFile` |

The Core group (`listToolGroups`, `activateToolGroups`, `runToolBatch`) is defined by the server itself, not under
`MCP/`. Its group entry is a snapshot from a running server in [core.json](../scripts/core.json) (refresh with
`live.py --update-core`); its schemas, summaries, effects and examples are hand-written in `shared.py` (`CORE_*`).

## Where each part of a page comes from

| Part | Source |
|---|---|
| Page title tagline and introduction | `FOLDERS` in [summaries.py](../scripts/summaries.py) |
| README categories | `CATEGORIES` in summaries.py; every folder and both shared pages must be in one |
| Group summary (bold line, overview and README) | `GROUP_SUMMARY` in summaries.py |
| Group description | `fDesc`, through `REPLACEMENTS` and `block()` |
| Tool summary (tables, index, first line of the tool) | `TOOL_SUMMARY` in summaries.py |
| Effect, safety, undo, runToolBatch line | `effect` and the group safety level, through `EFFECTS` and `tool_safety` in mdlib.py |
| **Details** | The tool `description`, through `REPLACEMENTS` and `block()` |
| **Parameters** | `inputSchema`: type, required, then the notes below |
| Version label | `--version` (`summaries.VERSION` at render time) |

Parameter notes, in this order: the schema description, `enum` values, `default`, limits (`minimum`, `maxItems`,
...). Only where the schema has no description, a note is chosen (first match wins):

1. `TOOL[(tool, path)]` in [paramnotes.py](../scripts/paramnotes.py): a curated note for one parameter of one tool.
2. `implicit_notes()` in mdlib.py: object references (`uuid`, `name`, `index`), creation options (`class`, `name`,
   `select`, `useClassAttributes`), paging (`limit`, `offset`, `countOnly`) and plug-in parameters (`params`),
   linked to Common.md.
3. `TEXT`, `ATTRIBUTES`, `DIMENSION` in paramnotes.py: curated notes shared by the text tools, the attribute tools
   and the Dimensioning group.
4. Derived from the tool description: a short remark in parentheses right after the parameter name. `DROP`
   suppresses a remark that describes something else.
5. `GENERIC[name]` in paramnotes.py: notes for common names (`position`, `angle`, `width`, ...).

Steps 3 to 5 are prefixed with the labelled sections of the description that list the parameter ("Used for walls,
slabs.").

Value formats shared by many tools are linked, not repeated: `{x, y}` objects link to `Common.md#points`, `{r, g, b}`
to `Common.md#colors`, and the marker and drop shadow objects to `Attributes.md`.

## Effects

| Effect (catalog) | Published label | Safety | Undo | In runToolBatch |
|---|---|---|---|---|
| `ReadOnly` | Read-only | low | none | allowed |
| `Modify` | Edit | the group's | one step `MCP: <tool>` | yes |
| `MediumRisk` | Edit | medium | one step | yes |
| `HighRisk` | Destructive edit | high | one step | no |
| `OwnUndo` | Interactive | medium | recorded as for user input | no |
| `OwnUndoHighRisk` | Interactive, destructive | high | recorded by the menu command | no |
| `RunsScript` | Script run | high | one step `MCP: script` | no |

The catalog names never appear on the pages (the audit flags them); only the labels do. The server marks
`ReadOnly` tools with `readOnlyHint` and `HighRisk`, `OwnUndoHighRisk` and `RunsScript` tools with `destructiveHint`;
live.py checks both.

## Wording rules

- `REPLACEMENTS` in summaries.py: exact text rewrites applied to every group and tool description before rendering.
  Use them when a server text contains implementation vocabulary (C++, SDK, "core tool", "implementation", ...).
  The review list reports replacements that no longer match any text.
- Hand-written texts (summaries, notes, shared pages) are not rewritten: write them in the style of the pages.
- [audit_terms.py](../scripts/audit_terms.py) `STRICT` patterns are the gate; the catalog's class and source file
  names are added per build. `BROAD` patterns only feed `broad.txt`. When a strict hit is legitimate public wording,
  narrow the pattern instead of rewriting the text.

## Changing the generator safely

Regenerating an unchanged source tree must reproduce the published pages byte for byte: before changing the scripts,
build the current version (without `--check-only` it reports `0 changed`; with `--check-only`, compare the staged
pages with the version folder). After the change, the differences must be exactly the intended ones. The catalog of
the last build (`catalog.json` in the work folder) can be rebuilt with `--catalog` to iterate on the text without the
source tree.
