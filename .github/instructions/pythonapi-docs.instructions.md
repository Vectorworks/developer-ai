---
description: "Use when editing, reviewing, regenerating, translating or adding a version of the Vectorworks Python API reference in PythonAPI/ or its localized PythonAPI.de/ and PythonAPI.ja/ folders (api module pages, version folders such as v2027.2, the version index) or the pythonapi-docs generator. Covers the external-audience wording rules, the page standard, the localized folder layout and the required checks."
applyTo: "PythonAPI/**,PythonAPI.*/**,.github/skills/pythonapi-docs/**"
---
# Vectorworks Python API reference

`PythonAPI/` is the published reference of the Vectorworks Python module `api`: one folder per Vectorworks version
(`v<year>.<update>`; `v2027.2` is Vectorworks 2027 Update 2) and the version index `PythonAPI/README.md`, which the
repository README links to. Translations live in sibling language folders that mirror it with the same file and
folder names: `PythonAPI.de/` (German) and `PythonAPI.ja/` (Japanese), for example `PythonAPI.de/README.md` and
`PythonAPI.de/v2027.2/Resources.md`. The exception is `AI-CONTEXT.md`: it is never localized and exists exactly once
per version, in English, in `PythonAPI/v<year>.<update>/`.

## Audience: external script authors

The pages are presented outside Vectorworks. Describe only what a Python user sees and does:

- Never mention the binding, the C++ implementation, the SDK, source files or folders, internal tools, or how the
  pages were produced.
- Use Python names only: `api.Document` (not `CDocument`), `api.Descend` (not `EDescend`), `api.WallObject.Heights`,
  `Math.Point2D`, `ObjectType.Arc` (not `kArcNode`), `None` / `True` / `False`, and `bool`, `int`, `float`, `str`
  instead of C++ types.
- Say "object" or "class", not "wrapper"; "Vectorworks", not "the core"; for null handles, "pass `None`".
- Names that clash with Python keywords end with `_`: `Descend.None_`, `from_`.

## Page standard

- A version folder holds `README.md` (getting started, conventions, API tree, contents by group, A–Z index, page
  layout, statistics) and one page per group: `DocumentAccess`, `Attributes`, `ObjectPrimitives`,
  `ObjectPrimitives.Math` (`api.Math`), `Objects3D`, `ObjectsAnnotation`, `ObjectsArchitect`, `ObjectsConnectCAD`,
  `ObjectsLandmark`, `ObjectsSpotlight`, `Resources`, `Scripting`, `UIAutomation`, `UILayoutCreate`. Every English
  version folder `PythonAPI/v<year>.<update>/` also holds the hand-maintained `AI-CONTEXT.md`.
- Every page: title; `> **Python module:** ... · **Version:** ...`; link back to the index; introduction;
  `## Table of contents` near the top; `## Overview` table; classes; enumerations; module functions and constants.
- Every class: `> **Full name:** ... · **Inherits:** ...`, a description, then the tables Constructors, Methods
  (grouped by topic), Operators and Python protocols, Fields, Constants. Nested types follow their owner. Inherited
  members are documented once, on the base class. Enumerations list Member, Value and Description.
- Signatures: `Name(param: type = default) -> result`, `*static*` after static methods, optional results `T \| None`
  (escape `|` in table cells), defaults as Python expressions (`1e-09`, `2**64 - 1`).
- Descriptions: short, plain sentences. Getters return `None` when a value cannot be obtained, setters and actions
  return `False` on failure; lengths are world units, angles radians counter-clockwise.
- UTF-8 without BOM, LF line endings, relative links, GitHub anchors (`Math.Point2D` → `#mathpoint2d`).

## German localization and language navigation

- When German localization is requested, create the version folder `PythonAPI.de/v<year>.<update>/` with the same
  Markdown page set as `PythonAPI/v<year>.<update>/` except `AI-CONTEXT.md`. Translate every page, including the
  version `README.md`. Never put translations inside `PythonAPI/` (no `v<year>.<update>.de` folders or `.de.md`
  files).
- Never translate `AI-CONTEXT.md` or create one in a language folder. Localized pages and READMEs link to the
  English file: `../PythonAPI/v2027.2/AI-CONTEXT.md` from `PythonAPI.de/README.md`,
  `../../PythonAPI/v2027.2/AI-CONTEXT.md` from a page in `PythonAPI.de/v2027.2/`.
- Translate prose faithfully, but preserve Python API names, signatures, types, defaults, code, filenames, and
  external URLs. Point relative links to the corresponding localized page when it exists, updating translated
  anchors; retain the English target when no localized page exists. Links within the same language folder keep the
  English relative paths (`Resources.md`, `../README.md`); links to an English-only page must leave the language
  folder (`../../PythonAPI/v2027.2/Resources.md` from a version page). Use the English Vectorworks help and its
  corresponding German help as terminology references. For Vectorworks 2027, use the
  [English 2027 help](https://app-help.vectorworks.net/2027/eng/index.htm) and the
  [German Vectorworks help](https://vectorworks-hilfe.computerworks.eu/2025/index.htm); use the corresponding
  release references for other versions when available.
- Put a language selector as the first line of every page in each localized language set, followed by a blank line
  and the page title. `AI-CONTEXT.md` is the exception: it is English-only and has no selector. Follow the README
  selector style and language order (English, Deutsch, 日本語): bold the current language, link each other available
  language to the matching page using relative paths (for example `[English](../../PythonAPI/v2027.2/Resources.md)`
  from `PythonAPI.de/v2027.2/Resources.md`), and omit languages without a matching page.
- Keep selectors across regeneration: update the generator pipeline to run
  [the shared language-selector helper](../scripts/doc_languages.py) on rendered pages, and validate parent-relative
  selector links against the final published folder when pages are staged.
- Verify that the English and translated folders contain matching page sets (apart from the English-only
  `AI-CONTEXT.md`), every selector is first and resolves, and translated links and anchors resolve: run the skill's
  `validate.py` on every translated version folder too. It accepts the translated table of contents titles
  (`Inhaltsverzeichnis`, `目次`); add the title of a new language to `TOC_TITLES` in `validate.py`. To keep the
  English anchor of a translated heading, put `<a id="english-anchor"></a>` and a blank line directly above it.
  Avoid changing English page content as part of translation beyond its selector line.

## Generated and hand-maintained files

- Every page of a version folder except `AI-CONTEXT.md` is generated by the
  [pythonapi-docs skill](../skills/pythonapi-docs/SKILL.md). Change text where it comes from: curated descriptions
  (`overrides_data.py`), wording rules (`scrub.py`), group introductions and the version README (`intros.py`); then
  rebuild. A change made only in a page is lost at the next build.
- `AI-CONTEXT.md` (context for AI code generation) is maintained by hand, in English only: don't regenerate or
  rewrite it unless asked, and never translate it. Every version folder `PythonAPI/v<year>.<update>/` must have one,
  and every row of the version index links it in all languages. A new version is not complete without it: when it
  is missing, ask the user for it instead of omitting it or copying another version's file unchanged.
- `PythonAPI/README.md` and its localized counterparts `PythonAPI.de/README.md` and `PythonAPI.ja/README.md` are
  maintained by hand: do not regenerate them or make unrelated rewrites. Follow the
  [README localization instructions](readme-localization.instructions.md) whenever any of them changes, keeping
  content, links and language selectors synchronized. Add a version-index row in every language for each new
  version.
- The source tree and the version label change with every Vectorworks version: get them from the user and never
  hard-code them.

## Before finishing

Build with `--check-only` as the skill describes: links, anchors, tables and tables of contents, coverage of every
exposed item, and the external wording audit must all pass. Without the source tree, run the skill's `validate.py`
and `audit_terms.py` on the version folder instead. Run `validate.py` on the translated version folders as well.
Confirm that every `PythonAPI/v<year>.<update>/` has an `AI-CONTEXT.md` and that no `PythonAPI.<language>/` folder
has one.
