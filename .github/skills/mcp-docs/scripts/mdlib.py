# Markdown helpers for the external MCP tool reference.
import json
import re

from summaries import REPLACEMENTS

# ---- text ------------------------------------------------------------------------------------------------------------

def clean(text):
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text


_CODE_RE = re.compile(r"(?<![\w'`])'([-\w][\w.\[\]/-]*)'(?![\w'])")


def _esc(s, table):
    s = s.replace("->", "\u2192")
    s = re.sub(r"\\(?=[!-/:-@\[-`{-~])", r"\\\\", s)
    s = s.replace("<", "&lt;").replace(">", "&gt;").replace("*", "\\*")
    s = re.sub(r"(?<![\w\\])_|_(?!\w)", r"\\_", s)
    if table:
        s = s.replace("|", "\\|")
    return s


def code(value, table=False):
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    s = value if isinstance(value, str) else json.dumps(value)
    if table:
        s = s.replace("|", "\\|")
    return "`" + s + "`"


_SPAN_RE = re.compile(r"`[^`\n]+`")


def _inline_plain(text, table):
    out, pos = [], 0
    for m in _CODE_RE.finditer(text):
        out.append(_esc(text[pos:m.start()], table))
        out.append(code(m.group(1), table))
        pos = m.end()
    out.append(_esc(text[pos:], table))
    return "".join(out)


def inline(text, table=False):
    """One line of text as Markdown: quoted identifiers become code, Markdown syntax is escaped; code spans are kept."""
    out, pos = [], 0
    for m in _SPAN_RE.finditer(text):
        out.append(_inline_plain(text[pos:m.start()], table))
        out.append(m.group(0).replace("|", "\\|") if table else m.group(0))
        pos = m.end()
    out.append(_inline_plain(text[pos:], table))
    return "".join(out)


def sentence(text):
    text = text.strip()
    return text if not text or text[-1] in ".!?" else text + "."


_ABBREVIATIONS = ("e.g.", "i.e.", "etc.", "vs.", "approx.", "No.", "cf.")
_SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=['\"(A-Z])")
_LABEL = re.compile(r"^([A-Z][A-Za-z0-9 /()'-]{0,40}?):\s+(.*)$")


def _sentences(line):
    parts, start = [], 0
    for m in _SENTENCE_END.finditer(line):
        before = line[start:m.start()]
        if before.endswith(_ABBREVIATIONS):
            continue
        parts.append(before)
        start = m.end()
    parts.append(line[start:])
    return [p for p in parts if p]


_LABEL_STOP = {"It", "They", "Then", "Returns", "Create", "List", "The", "This", "These", "Optional", "Single"}


def _labelled(s):
    m = _LABEL.match(s)
    if not m:
        return None
    label = m.group(1)
    if len(label.split()) > 4 or "'" in label or label.count("(") != label.count(")") or label.split()[0] in _LABEL_STOP:
        return None
    return label, m.group(2)


def _paragraphs(line, limit=500):
    """A long line as several paragraphs: a new one at each 'Label: ...' sentence, or after about 'limit' characters."""
    if len(line) <= limit:
        return [inline(line)]
    chunks, cur, cur_len, cur_labelled = [], [], 0, False
    for s in _sentences(line):
        lab = _labelled(s)
        if cur and (lab or (not cur_labelled and cur_len >= limit * 0.7)):
            chunks.append(" ".join(cur))
            cur, cur_len, cur_labelled = [], 0, False
        if lab:
            cur.append("**" + _esc(lab[0], False) + ":** " + inline(lab[1]))
            cur_labelled = True
        else:
            cur.append(inline(s))
        cur_len += len(s)
    if cur:
        chunks.append(" ".join(cur))
    return chunks


def block(text):
    """Multi-line tool text as Markdown lines: paragraphs, numbered steps and bullet items."""
    out, prev = [], None
    for raw in clean(text).split("\n"):
        line = raw.strip()
        if not line:
            prev = None
            continue
        m = re.match(r"^(\d+)[.)]\s+(.*)$", line)
        if m:
            kind, contents = "ol", [m.group(1) + ". " + inline(m.group(2))]
        elif line.startswith("- "):
            kind, contents = "ul", ["- " + inline(line[2:])]
        else:
            kind, contents = "p", _paragraphs(line)
        for content in contents:
            if out and (kind != prev or kind == "p"):
                out.append("")
            out.append(content)
            prev = kind
    return out


# ---- anchors and pages -----------------------------------------------------------------------------------------------

def slug(text):
    a = text.strip().lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


class Page:
    """A Markdown page whose table of contents is built from its level 2 and 3 headings."""

    def __init__(self, title, tagline_md, intro_lines):
        self.title = title
        self.head = ["# " + title, "", tagline_md, "", "[Back to the index](README.md)", ""] + intro_lines
        self.body = []
        self.headings = []
        self.used = {}
        self._anchor(title)
        self._anchor("Table of contents")

    def _anchor(self, text):
        base = slug(text)
        n = self.used.get(base, 0)
        self.used[base] = n + 1
        return base if n == 0 else "%s-%d" % (base, n)

    def h(self, level, text, toc=True):
        anchor = self._anchor(text)
        if toc and level in (2, 3):
            self.headings.append((level, text, anchor))
        self.body += ["#" * level + " " + text, ""]
        return anchor

    def add(self, *lines):
        self.body += list(lines)

    def para(self, lines):
        self.body += list(lines) + [""]

    def table(self, header, rows):
        self.body.append("| " + " | ".join(header) + " |")
        self.body.append("|" + "---|" * len(header))
        for r in rows:
            self.body.append("| " + " | ".join(str(c) for c in r) + " |")
        self.body.append("")

    def render(self):
        toc = ["## Table of contents", ""]
        for level, text, anchor in self.headings:
            toc.append(("  " if level == 3 else "") + "- [%s](#%s)" % (text, anchor))
        lines = self.head + [""] + toc + [""] + self.body
        text = "\n".join(lines)
        text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
        return text


# ---- schemas ---------------------------------------------------------------------------------------------------------

_DROP_DESCRIPTIONS = {"A point in world units: { x, y }", "RGB color, channels 0-255"}


def is_marker(s):
    p = s.get("properties") or {}
    return "shape" in p and "thicknessBasis" in p


def is_drop_shadow(s):
    p = s.get("properties") or {}
    return "blurRadius" in p and "colorIndex" in p


def _plain(props):
    return all(not (v.get("description") or v.get("enum")) for v in props.values())


def type_of(s):
    """(Markdown type label, whether the value is shown as one row without its members)."""
    t = s.get("type")
    if isinstance(t, list):
        return " or ".join(t), True
    if t == "object":
        props = s.get("properties")
        if not props:
            return "object", True
        keys = set(props)
        if keys == {"x", "y"} and _plain(props):
            return "[point](Common.md#points)", True
        if keys == {"x", "y", "z"} and _plain(props):
            return "[3D point](Common.md#points)", True
        if keys == {"r", "g", "b"} and _plain(props):
            return "[color](Common.md#colors)", True
        if keys == {"left", "top", "right", "bottom"} and _plain(props):
            return "[rectangle](Common.md#rectangles)", True
        if is_marker(s):
            return "[marker](Attributes.md#line-end-markers)", True
        if is_drop_shadow(s):
            return "[drop shadow](Attributes.md#drop-shadow)", True
        return "object", False
    if t == "array":
        items = s.get("items")
        if not items:
            return "array", True
        label, collapsed = type_of(items)
        return "array of " + label, collapsed
    return t or "any", True


def _limits(s):
    n = []
    if "minimum" in s:
        n.append("Minimum: %s." % code(s["minimum"], True))
    if "exclusiveMinimum" in s:
        n.append("Greater than %s." % code(s["exclusiveMinimum"], True))
    if "maximum" in s:
        n.append("Maximum: %s." % code(s["maximum"], True))
    lo, hi = s.get("minItems"), s.get("maxItems")
    if lo is not None and hi is not None:
        n.append("%d item%s." % (lo, "" if lo == 1 else "s") if lo == hi else "%d to %d items." % (lo, hi))
    elif lo is not None:
        n.append("At least %d item%s." % (lo, "" if lo == 1 else "s"))
    elif hi is not None:
        n.append("At most %d items." % hi)
    lo, hi = s.get("minLength"), s.get("maxLength")
    if lo is not None and hi is not None:
        n.append("%d to %d characters." % (lo, hi))
    elif lo is not None:
        n.append("At least %d character%s." % (lo, "" if lo == 1 else "s"))
    elif hi is not None:
        n.append("At most %d characters." % hi)
    return n


def notes_for(s, implicit=""):
    n = []
    d = s.get("description")
    described = bool(d and d not in _DROP_DESCRIPTIONS and not is_marker(s) and not is_drop_shadow(s))
    if described:
        d = sentence(clean(d))
        n.append(inline(d[:1].upper() + d[1:], True))
    if "enum" in s:
        n.append("One of: " + ", ".join(code(v, True) for v in s["enum"]) + ".")
    items = s.get("items") if isinstance(s.get("items"), dict) else {}
    if items.get("description") and items["description"] not in _DROP_DESCRIPTIONS and not is_marker(items) and not is_drop_shadow(items):
        n.append("Each item: " + inline(sentence(clean(items["description"])), True))
    if "enum" in items:
        n.append("Each item one of: " + ", ".join(code(v, True) for v in items["enum"]) + ".")
    if "default" in s:
        n.append("Default: %s." % code(s["default"], True))
    n += _limits(s)
    if implicit and not n:
        n.append(implicit)
    elif implicit and not described:
        used = re.match(r"Used for [^.]*\.", implicit)
        if used:
            n.insert(0, used.group(0))
    return " ".join(n)


def schema_rows(schema, implicit=None, prefix=""):
    """Rows (parameter, type, required, notes) of an input schema, members of nested objects as dotted paths."""
    implicit = implicit or {}
    required = set(schema.get("required") or [])
    for name, s in (schema.get("properties") or {}).items():
        path = prefix + name
        label, collapsed = type_of(s)
        yield (code(path, True), label, "Yes" if name in required else "", notes_for(s, implicit.get(path, "")))
        if collapsed:
            continue
        if s.get("type") == "object":
            yield from schema_rows(s, implicit, path + ".")
        elif s.get("type") == "array":
            items, p = s["items"], path + "[]"
            while items.get("type") == "array":
                items, p = items.get("items") or {}, p + "[]"
            if items.get("type") == "object":
                yield from schema_rows(items, implicit, p + ".")


# ---- tool effects ----------------------------------------------------------------------------------------------------

# effect -> (label, undo, may run in runToolBatch)
EFFECTS = {
    "ReadOnly":        ("Read-only", "none", "allowed"),
    "Modify":          ("Edit", 'one step "MCP: {tool}"', "yes"),
    "MediumRisk":      ("Edit", 'one step "MCP: {tool}"', "yes"),
    "HighRisk":        ("Destructive edit", 'one step "MCP: {tool}"', "no"),
    "OwnUndo":         ("Interactive", "recorded by Vectorworks as for user input", "no"),
    "OwnUndoHighRisk": ("Interactive, destructive", "recorded by the menu command", "no"),
    "RunsScript":      ("Script run", 'one step "MCP: script"', "no"),
}


def tool_safety(effect, group_safety):
    return {"ReadOnly": "low", "MediumRisk": "medium", "HighRisk": "high", "OwnUndo": "medium",
            "OwnUndoHighRisk": "high", "RunsScript": "high"}.get(effect, group_safety)


def implicit_notes(schema):
    """Notes for well-known top-level parameters that the schema does not describe."""
    p = schema.get("properties") or {}
    n = {}
    create = all(k in p for k in ("class", "name", "select", "useClassAttributes"))
    if create:
        n.update({
            "class": "Creation option: class of the new object; created when missing. See [Creation options](Common.md#creation-options).",
            "name": "Creation option: name of the new object.",
            "select": "Creation option: select the new object.",
            "useClassAttributes": "Creation option: with `class`, also set the attributes of the new object by class.",
        })
    if "uuid" in p:
        n["uuid"] = "Reference by UUID (preferred). See [Object references](Common.md#object-references)."
    if not create and "uuid" in p and "index" in p and "name" in p:
        n["name"] = "Reference by name."
        n["index"] = "Reference by internal index."
    if "limit" in p and "offset" in p:
        n["limit"] = "Paging: the maximum number of items to return (at least 1). See [Paging](Common.md#paging)."
        n["offset"] = "Paging: the number of items to skip (default 0)."
    if "countOnly" in p:
        n["countOnly"] = "Paging: return only the counts, without the items."
    if "params" in p:
        if p["params"].get("type") == "array":
            n["params"] = "Names of plug-in parameters to return with typed values. See [Plug-in parameters](Common.md#plug-in-parameters)."
        else:
            n["params"] = 'Raw plug-in parameters `{ "ParamName": value }`. See [Plug-in parameters](Common.md#plug-in-parameters).'
    return n
