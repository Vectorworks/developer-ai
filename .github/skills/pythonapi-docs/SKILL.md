---
name: pythonapi-docs
description: 'Regenerate, update or check the Vectorworks Python API reference (the api module pages in PythonAPI/v<year>.<update>/) from a Vectorworks source tree. Use when documenting a new Vectorworks version or update, when the api module gained or changed classes, methods, enumerations or groups, when fixing or adding member descriptions, or when validating the reference pages (links, coverage, external wording).'
argument-hint: 'Version to document (for example "Vectorworks 2028 Update 1") and the source folder'
---

# Python API reference generator

Builds the reference of the Python module `api` (one page per group plus `README.md` in `PythonAPI/v<year>.<update>/`)
from the Vectorworks source of the documented version, then checks it. Standard library only (tested with Python
3.13). The rules for the pages themselves are in
[pythonapi-docs.instructions.md](../../instructions/pythonapi-docs.instructions.md).

## Inputs

| Option | Example | Notes |
|---|---|---|
| `--source` | `<source tree>/.../Interfaces/VectorWorks` | The folder of the documented version that contains `PythonProvider.cpp`, `API/` (C++ API headers; their comments become the descriptions) and `PythonAPI/` (the Python binding; it decides what is exposed). It differs per version and per machine: ask the user when you don't know it, never hard-code it. |
| `--version` | `Vectorworks 2028 Update 1` | Label shown on every page. |
| `--out` | `PythonAPI/v2028.1` | One folder per version: `v<year>.<update>`. |

Without access to the source tree you cannot regenerate: make small fixes by hand in the pages *and* in the
generator inputs (below), so the next build keeps them.

## Procedure

1. Build and check without touching the repository (run from the repository root):
   ```
   python .github/skills/pythonapi-docs/scripts/build.py --source "<Interfaces/VectorWorks folder>" --version "Vectorworks 2028 Update 1" --out PythonAPI/v2028.1 --check-only
   ```
   The pages are rendered into a staging folder (`pythonapi-docs-build` in the temp folder; change it with `--work`),
   then three checks run: links, anchors, tables and tables of contents; coverage of every exposed class, enumeration
   and member; external wording.
2. Fix every failure (see [Fixing problems](#fixing-problems)) and repeat until it prints "All checks passed".
3. Go through the review list it prints (not failures): members described only from their name, unused overrides.
   Details are in `review.json` next to the staged pages.
4. Run the same command without `--check-only`: the pages are copied into `--out`. Other files there, such as
   `AI-CONTEXT.md`, are left alone. Delete a page yourself only when its group was removed.
5. New version: add a row to the version index `PythonAPI/README.md`, for example
   `| Vectorworks 2028 Update 1 | [v2028.1](v2028.1/README.md) | [AI-CONTEXT.md](v2028.1/AI-CONTEXT.md) |`. Every
   version needs its English `AI-CONTEXT.md` in `PythonAPI/v2028.1/`; it is maintained by hand, so ask the user for it
   when it is missing. Add the row to `PythonAPI.de/README.md` and `PythonAPI.ja/README.md` too, linking a
   translated version folder there when it exists and the English one otherwise
   (`[v2028.1](../PythonAPI/v2028.1/README.md)`), and always the English AI context
   (`[AI-CONTEXT.md](../PythonAPI/v2028.1/AI-CONTEXT.md)`); `AI-CONTEXT.md` is never translated.
6. Read the diff (`git diff -- PythonAPI`) and spot-check changed pages against the
   [instruction file](../../instructions/pythonapi-docs.instructions.md).

## Fixing problems

| Symptom | Fix |
|---|---|
| `No page for binding folder(s) X` | A new group: add it to `FOLDER_DOCS` in [render.py](./scripts/render.py), write `title`, `name`, `short` and `intro` for it in `FOLDERS` of [intros.py](./scripts/intros.py), and add it to the API tree in `intros.readme()`. |
| note `group X has no classes, ...` | The group was removed: drop it from `FOLDER_DOCS`, `FOLDERS` and the API tree, then delete its page from the version folder. |
| validate: `missing file`, `missing anchor`, cell count | Usually a link in an override or intro, or an unescaped `\|` in a table cell. |
| coverage: `MISSING ...` | An exposed item was not rendered: a generator bug (signature resolution or rendering); check the notes in `review.json`. |
| wording hits | Implementation vocabulary reached a page: add a rewrite to [scrub.py](./scripts/scrub.py) when the phrasing comes from several source comments, or a curated description to [overrides_data.py](./scripts/overrides_data.py) for one member. |
| review: members described from their name only, or without description | Add curated descriptions to [overrides_data.py](./scripts/overrides_data.py). |
| review: unused overrides | The member was renamed or removed, or its signature changed: update the key or delete the entry. |
| note `ctor ...(BlankHandle) not found` for `PrimitiveObject`, `AnnotationObject`, `ArchitectObject`, `LandmarkObject` | Expected: abstract base classes; their constructors are still documented. |

## Scripts

| Script | Use |
|---|---|
| [build.py](./scripts/build.py) | The entry point: render, check, copy. |
| [validate.py](./scripts/validate.py) `<folder> [--all]` | Links, anchors, tables, tables of contents of a version folder, English or translated; `--all` includes hand-maintained files. |
| [audit_terms.py](./scripts/audit_terms.py) `<folder> [--broad report.txt] [--all]` | External wording gate; `--broad` lists weaker signals for a manual read; `--all` includes hand-maintained files. |
| [coverage.py](./scripts/coverage.py) `--source ... --pages ...` | Coverage of every exposed item. |
| [overrides_data.py](./scripts/overrides_data.py), [scrub.py](./scripts/scrub.py), [intros.py](./scripts/intros.py) | The text you are most likely to edit: curated descriptions, wording rules, group introductions and the version README. |

The pipeline, the override key formats and the description rules are in
[references/generator.md](./references/generator.md). Changing a script: first confirm that building the current
version reproduces the published pages byte for byte, so the diff shows only your change.
