---
description: "Use when creating, editing, translating, moving or regenerating any README. Keep English, German and Japanese README files synchronized (root README.de.md/README.ja.md siblings; elsewhere mirrored <Folder>.de/ and <Folder>.ja/ language folders), with first-line language selectors and correct localized links."
applyTo: "**/README*.md"
---
# README localization

## Keep language versions synchronized

- These rules apply to README files throughout the repository, not just the root, `PythonAPI/` and `MCP/`.
- Repository root only: use `README.md` for English, `README.de.md` for German and `README.ja.md` for Japanese,
  side by side.
- Everywhere else, translations live in sibling language folders that mirror the top-level English folder with the
  same relative path: `PythonAPI/README.md` is translated in `PythonAPI.de/README.md` and `PythonAPI.ja/README.md`,
  `MCP/README.md` in `MCP.de/README.md` and `MCP.ja/README.md`, and `<Folder>/<path>/README.md` in
  `<Folder>.de/<path>/README.md` and `<Folder>.ja/<path>/README.md`. Never add `README.de.md` or `README.ja.md`
  outside the root. When adding a new hand-maintained README, create all three language versions.
- Update every localized sibling in the same task whenever content, sections, version tables, examples or links
  change. If a substantive correction starts in a translation, apply it to English and the other translations too.
  Language-specific spelling or grammar fixes do not require unrelated changes to other languages.
- Translate the meaning faithfully while preserving technical names, code, filenames and version labels. Keep the
  same information and structure in every language; do not leave translations stale or omit new content.
- When moving or renaming a README, handle its localized counterparts and update affected links together.
- For generated READMEs, follow the [MCP](mcp-docs.instructions.md) or
  [Python API](pythonapi-docs.instructions.md) generation rules: change the generator, rebuild, then synchronize
  any existing translations. English-only generated reference READMEs do not need selectors or new translations
  unless localization is requested; never hand-edit generated output to add a selector.

## First-line language selector

For every localized README set, put a single inline selector on the very first line, followed by a blank line and
the main heading. Use ` • ` between languages, not pipes. Bold the current language without linking it, and link
the other languages using relative paths. Use the labels and order shown below.

At the repository root, link the sibling files:

- `README.md`:
  ```markdown
  **English** • [Deutsch](README.de.md) • [日本語](README.ja.md)
  ```
- `README.de.md`:
  ```markdown
  [English](README.md) • **Deutsch** • [日本語](README.ja.md)
  ```
- `README.ja.md`:
  ```markdown
  [English](README.md) • [Deutsch](README.de.md) • **日本語**
  ```

In language folders, link the same README in the other language folders (shown for `PythonAPI`; add one `../` per
level for deeper READMEs):

- `PythonAPI/README.md`:
  ```markdown
  **English** • [Deutsch](../PythonAPI.de/README.md) • [日本語](../PythonAPI.ja/README.md)
  ```
- `PythonAPI.de/README.md`:
  ```markdown
  [English](../PythonAPI/README.md) • **Deutsch** • [日本語](../PythonAPI.ja/README.md)
  ```
- `PythonAPI.ja/README.md`:
  ```markdown
  [English](../PythonAPI/README.md) • [Deutsch](../PythonAPI.de/README.md) • **日本語**
  ```

Only include languages whose files exist. When adding or removing a language, update every selector in that set.

## Links and checks

- In translated prose, link to the corresponding localized README when it exists (`PythonAPI.de/README.md` from the
  root `README.de.md`, `../PythonAPI.de/README.md` from `MCP.de/README.md`). Otherwise keep the English target,
  including links to untranslated version references; from a language folder that target lies outside it
  (`../PythonAPI/v2028.1/README.md` from `PythonAPI.de/README.md`), because the English relative path would point
  into the language folder. `AI-CONTEXT.md` is never translated: localized READMEs always link the English file
  (`../PythonAPI/v2028.1/AI-CONTEXT.md` from `PythonAPI.de/README.md`). Keep paths relative and update heading
  anchors when their translated text changes.
- Preserve UTF-8 without BOM, Markdown formatting and LF line endings.
- Before finishing, compare all language versions for equivalent coverage, confirm each selector is the first
  line, and verify every selector and changed relative link resolves. Include newly created, untracked files in
  these checks; do not rely on `git diff --check` alone to validate them.
