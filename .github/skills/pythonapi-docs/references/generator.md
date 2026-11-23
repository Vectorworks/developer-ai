# Generator reference

How [build.py](../scripts/build.py) turns a Vectorworks source tree into the reference pages, and where to change
what the pages say.

## Pipeline

| Step | Module | What it does |
|---|---|---|
| 1 | [bindscan.py](../scripts/bindscan.py) | Reads the Python binding (`PythonAPI/**/*.cpp` of the source tree): classes, enumerations, constructors, methods, fields, constants, Python names, argument names and default values. It decides what is exposed. |
| 2 | [cppscan.py](../scripts/cppscan.py) | Reads the C++ API headers (`API/**/*.h`): declarations with their comments (leading, trailing, group comments and `-- Title --` section markers). |
| 3 | [model.py](../scripts/model.py) | Joins both: C++ names to Python names (`CDocument` → `Document`, `EDescend` → `Descend`, `CWallObject::THeights` → `WallObject.Heights`, `Math::CPoint2D` → `Math.Point2D`) and C++ types to Python types (`std::optional<T>` → `T \| None`, `std::vector<T>` → `list[T]`, ...). |
| 4 | [resolve.py](../scripts/resolve.py) | Matches every exposed member with its declaration: Python signature, static flag, comments, defaults as Python expressions. |
| 5 | [describe.py](../scripts/describe.py) | Chooses each description (order below). `Translator` rewrites C++ names to Python names and puts parameters, calls, dotted names and literals in backticks. |
| 6 | [scrub.py](../scripts/scrub.py) | Removes implementation vocabulary from text that comes from the source comments (see Wording rules). |
| 7 | [intros.py](../scripts/intros.py) | Hand-written text: group titles, short summaries and introductions (`FOLDERS`), and the whole version README (`readme()`: getting started, conventions, API tree, indexes). |
| 8 | [render.py](../scripts/render.py) | Page layout. `FOLDER_DOCS` maps each binding folder to its page and sets the page order. |
| 9 | [validate.py](../scripts/validate.py), [coverage.py](../scripts/coverage.py), [audit_terms.py](../scripts/audit_terms.py) | Checks run by build.py: links, anchors, tables and tables of contents; every exposed item documented; no implementation vocabulary (strict patterns plus the C++ names of the exposed types). |

## Language navigation

After rendering, `build.py` runs the shared [language-selector helper](../../../scripts/doc_languages.py).
It adds a first-line selector linking to the same page in the same version folder of every existing language folder
(`PythonAPI/v2027.2`, `PythonAPI.de/v2027.2`, `PythonAPI.ja/v2027.2`), with the current language bold. Missing
translations are not linked; English-only pages remain unchanged. `AI-CONTEXT.md` is English-only and never gets a
selector; the helper removes one if present. Staging uses the final `--out` location, and validation checks those
parent-relative links.

To refresh existing pages in every language without regenerating their bodies:

```text
python .github/scripts/doc_languages.py PythonAPI/v2027.2 PythonAPI.de/v2027.2 PythonAPI.ja/v2027.2
```

## Curated descriptions (overrides_data.py)

[overrides_data.py](../scripts/overrides_data.py) holds `OVERRIDES`, about 1,000 hand-written descriptions. Keys use
Python names, as printed on the pages:

| Key | Applies to |
|---|---|
| `Class.Method` | every overload of a method |
| `Class.Method(p: T, q: U)` | one overload; parameter names and types exactly as in its signature |
| `Class.__init__(p: T)` | one constructor |
| `Class.Field`, `Class.Constant` | a field or a class constant |
| `api.Fn`, `api.Math.Fn` | a module function |
| `class:Class`, `enum:Enum` | a class or enumeration description: a string, or a list of Markdown blocks (paragraphs, lists, Python code) |

Nested names use dots: `WallObject.Heights`, `Math.Point2D`, `enum:TextObject.Spacing`. In method entries, a value
starting with `+` is a sentence placed before the comment from the source. Write overrides in the plain style of the
pages and follow the wording rules of the instruction file; nothing scrubs them.

## Where a description comes from

1. A curated override.
2. The comment that documents the declaration (lists in it become `<br>• ` items).
3. The group comment of another overload with the same name.
4. Rules for accessors and protocols: `Get`/`Set` pairs, `Is(h)`, `IsValid`, `GetHandle`, `Duplicate`, operators.
5. Weaker sources: a group comment, a trailing comment, or the name alone. These members are listed in
   `review.json` (`weakly_described`); they are the best candidates for new overrides.

## Wording rules (scrub.py)

Applied to every translated comment, in this order:

- `DROP`: paragraphs that only make sense to C++ developers are removed.
- `PHRASES`: exact sentence rewrites (also matched with the first letter in the other case).
- `RAW`: regular expressions over the whole text (parenthesized SDK references, C++ operator notes, ...).
- `kXxxNode` constants become `ObjectType.Xxx`.
- `PROSE`: regular expressions outside code spans ("wrapper" → "object", "the core" → "Vectorworks", "enum" →
  "enumeration", ...).

Add a scrub rule when the same phrasing comes from several comments; add an override when a single member is
affected. When `audit_terms.py` flags wording that is legitimate public vocabulary, narrow its `STRICT` pattern
instead of rewriting the text.

## Changing the generator safely

Regenerating an unchanged source tree must reproduce the published pages byte for byte. Before changing the
scripts, build the current version with `--check-only` and compare the staged pages with the version folder; after
the change, the differences must be exactly the intended ones.
