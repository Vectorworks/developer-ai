---
description: "Use when editing, reviewing, regenerating, translating or adding a version of the Vectorworks MCP server tool reference in MCP/ or its localized MCP.de/ and MCP.ja/ folders (tool folder pages, Common.md, Attributes.md, version folders such as v2027.2, the version index) or the mcp-docs generator. Covers the external-audience wording rules, the page standard, the localized folder layout and the required checks."
applyTo: "MCP/**,MCP.*/**,.github/skills/mcp-docs/**"
---
# Vectorworks MCP tool reference

`MCP/` is the published reference of the tools of the Vectorworks MCP server: `MCP/README.md` (what MCP is, the
local HTTP server, the version table) and one folder per Vectorworks version (`v<year>.<update>`; `v2027.2` is
Vectorworks 2027 Update 2). Translations live in sibling language folders that mirror it with the same file and
folder names: `MCP.de/` (German) and `MCP.ja/` (Japanese), for example `MCP.de/README.md` and
`MCP.de/v2027.2/Common.md`.

## Audience: external MCP client and agent authors

The pages are presented outside Vectorworks, detached from its source. Describe only what an MCP client sees and
does:

- Never mention the C++ implementation, the binding, source files or folders, class names, handlers, the internal
  effect names (`ReadOnly`, `Modify`, `OwnUndo`, `RunsScript`, ...) or how the pages were produced.
- Use the names a client sees: tool names, group display names and group IDs, parameter names and JSON values,
  exactly as the server sends them.
- Say "Vectorworks", not "the core"; "built-in tool", not "core tool". "Core" is only the name of the always
  available meta-tool group (`listToolGroups`, `activateToolGroups`, `runToolBatch`). "SDK plug-in" is fine as a
  kind of Vectorworks tool or command.
- Effects are published as labels: Read-only, Edit, Destructive edit, Interactive, Interactive, destructive, Script
  run.

## Page standard

- A version folder holds `README.md` (getting started, conventions, tool tree, contents by category, A–Z index, page
  layout, statistics), `Common.md` (shared conventions and the Core group), `Attributes.md` (line end markers, drop
  shadows) and one page per tool folder of the server: `DocumentAccess`, `IFC`, `MenuAccess`, `ObjectPrimitives`,
  `Objects3D`, `ObjectsAnnotation`, `ObjectsArchitect`, `ObjectsConnectCAD`, `ObjectsLandmark`, `ObjectsSpotlight`,
  `OIPAccess`, `Resources`, `Scripting`, `ToolAccess`.
- Every page: `# <Folder> — <subject>`; `> **Server:** Vectorworks MCP · **Version:** ...`; a link back to the
  index; an introduction; `## Table of contents` near the top, listing every level 2 and 3 heading; an `## Overview`
  table (Group, Group ID, Active by default, Safety level, Tools, Summary).
- Every group: `## <display name>`; a quote line with Group, Group ID, Active by default, Safety level and Tools; a
  bold one-line summary; the description the server reports; a table Tool, Effect, Safety, Summary.
- Every tool: `### <toolName>` (anchor: the name in lowercase); a one-line summary;
  `> **Effect:** ... · **Safety:** ... · **Undo:** ... · **In runToolBatch:** ...`; **Details** (the description
  the server reports); **Parameters** (Parameter, Type, Required, Description; members as `parameter.member` and
  `parameter[].member`), or "This tool takes no parameters."
- Tools are listed in definition order. Shared formats are linked, not repeated: point, 3D point, color and
  rectangle to `Common.md`, marker and drop shadow to `Attributes.md`.
- Summaries: one short, plain sentence; tool summaries start with a verb ("Creates ...", "Returns ...",
  "Lists ..."). Lengths are world units and angles radians counter-clockwise, except where `Common.md` (Units and
  angles) lists an exception.
- UTF-8 without BOM, LF line endings, relative links, GitHub anchors. JSON examples must parse; no Markdown escapes
  inside code spans.

## German localization and language navigation

- When German localization is requested, create the version folder `MCP.de/v<year>.<update>/` with the same
  Markdown page set as `MCP/v<year>.<update>/`. Translate every page, including the version `README.md` and shared
  reference pages. Never put translations inside `MCP/` (no `v<year>.<update>.de` folders or `.de.md` files).
- Translate prose faithfully, but preserve tool and parameter names, IDs, JSON values, code, filenames, and external
  URLs. Point relative links to the corresponding localized page when it exists, updating translated anchors; retain
  the English target when no localized page exists. Links within the same language folder keep the English relative
  paths (`Common.md`, `../README.md`); links to an English-only page must leave the language folder
  (`../../MCP/v2027.2/Common.md` from a version page). Use the English Vectorworks help and its corresponding German
  help as terminology references. For Vectorworks 2027, use the
  [English 2027 help](https://app-help.vectorworks.net/2027/eng/index.htm) and the
  [German Vectorworks help](https://vectorworks-hilfe.computerworks.eu/2025/index.htm); use the corresponding
  release references for other versions when available.
- Put a language selector as the first line of every page in each localized language set, followed by a blank line
  and the page title. Follow the README selector style and language order (English, Deutsch, 日本語): bold the
  current language, link each other available language to the matching page using relative paths (for example
  `[English](../../MCP/v2027.2/Common.md)` from `MCP.de/v2027.2/Common.md`), and omit languages without a matching
  page.
- Keep selectors across regeneration: update the generator pipeline to run
  [the shared language-selector helper](../scripts/doc_languages.py) on rendered pages, and validate parent-relative
  selector links against the final published folder when pages are staged.
- Verify that the English and translated folders contain matching page sets, every selector is first and resolves,
  and translated links and anchors resolve: run the skill's `validate.py` on every translated version folder too.
  It accepts the translated table of contents titles (`Inhaltsverzeichnis`, `目次`) and index headings (`索引 A`);
  add those of a new language to `TOC_TITLES` and `INDEX_PREFIXES` in `validate.py`. To keep the English anchor of
  a translated heading, put `<a id="english-anchor"></a>` and a blank line directly above it. Avoid changing English
  page content as part of translation beyond its selector line.

## Generated and hand-maintained files

- Every page of a version folder is generated by the [mcp-docs skill](../skills/mcp-docs/SKILL.md). Change text
  where it comes from: page introductions, categories, group and tool summaries and the `REPLACEMENTS` for server
  texts (`summaries.py`), parameter notes (`paramnotes.py`), `Common.md`, `Attributes.md` and the Core group
  (`shared.py`); then rebuild. A change made only in a page is lost at the next build.
- Group and tool descriptions and input schemas come from the server. Don't reword them in the pages: fix
  implementation vocabulary with a `REPLACEMENTS` entry, and tell the user when the server text itself should change.
- `MCP/README.md` and its localized counterparts `MCP.de/README.md` and `MCP.ja/README.md` are maintained by hand:
  do not regenerate them or make unrelated rewrites. Follow the
  [README localization instructions](readme-localization.instructions.md) whenever any of them changes, keeping
  content, links and language selectors synchronized. Add a version-table row in every language for each new
  version.
- The source tree, the server URL and the version label change with every Vectorworks version and machine: get them
  from the user and never hard-code them.

## Before finishing

Build with `--check-only` as the skill describes, with `--live` when Vectorworks of the documented version runs its
MCP server: links, anchors, tables, tables of contents and code; coverage of every group, tool and parameter; the
external wording audit; and the live comparison must all pass. Without the source tree, run the skill's
`validate.py` and `audit_terms.py` on the version folder instead (and `coverage.py` when a `catalog.json` is at
hand). Run `validate.py` on the translated version folders as well.
