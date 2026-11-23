"""Short notes for parameters that the input schemas leave undescribed (used only where a schema has no description)."""
import re

GENERIC = {
    "position": "Insertion point.",
    "center": "Center point.",
    "angle": "Angle in radians, counter-clockwise.",
    "startAngle": "Start angle in radians, counter-clockwise.",
    "endAngle": "End angle in radians, counter-clockwise.",
    "sweepAngle": "Sweep angle in radians; positive is counter-clockwise.",
    "radius": "Radius, in world units.",
    "diameter": "Diameter, in world units.",
    "width": "Width, in world units.",
    "height": "Height, in world units.",
    "depth": "Depth, in world units.",
    "thickness": "Thickness, in world units.",
    "elevation": "Elevation, in world units.",
    "cornerRadius": "Corner radius, in world units.",
    "start": "Start point.",
    "end": "End point.",
    "point": "A point.",
    "points": "The points, in order.",
    "closed": "Whether the shape is closed.",
    "z": "Z value (height), in world units.",
    "pathUuid": "UUID of the object that supplies the path.",
    "profileUuid": "UUID of the object that supplies the profile.",
    "objectUuid": "UUID of the target object.",
    "newName": "The new name.",
    "description": "Description text.",
    "search": "Text filter: keeps the entries that contain this text (case-insensitive).",
    "filePath": "Full path of the file.",
    "textStyle": "Name or resource UUID of a text style; an empty string for none.",
    "maxChoices": "Maximum number of choices listed per control or mode (0 or more).",
}

TOOL = {
    ("createSlab", "height"): "Elevation of the slab datum (the top or bottom of its core component, as the style sets it), in world units.",
    ("setLandmarkObject", "name"): "Used for landscape area (the area name, not the object name), property line.",
    ("createExistingTree", "caliper"): "Trunk diameter (DBH).",
    ("setLandmarkObject", "caliper"): "Used for existing tree. Trunk diameter (DBH).",
    ("setResourceDetails", "recalculate"): "Recalculate the worksheet after the change; on by default.",
    ("setArchitectureObject", "height"): "Used for slabs (the elevation of the slab datum), doors, windows, columns. In world units.",
    ("setArchitectureObject", "numTreads"): "Stairs: cannot be set (reported as not applied).",
    ("setArchitectureObject", "configuration"): "Stairs: cannot be set (reported as not applied).",
    ("setArchitectureObject", "handrailLeft"): "Stairs: cannot be set (reported as not applied).",
    ("setArchitectureObject", "handrailRight"): "Stairs: cannot be set (reported as not applied).",
}

TEXT = {
    "text": 'The text (UTF-8); "\\n" starts a new line.',
    "origin": "Alignment point of the text, in world units.",
    "width": "Wrapping width in world units; makes a wrapped text.",
    "angle": "Rotation in radians, counter-clockwise, about the origin.",
    "textStyleByClass": "Use the text style of the class.",
    "font": "Font name.",
    "size": "Text size in world units (not together with `sizePoints`).",
    "sizePoints": "Text size in points.",
    "color": "Text color.",
    "bold": "Bold style.",
    "italic": "Italic style.",
    "underline": "Underline style.",
    "outline": "Outline style (shown on macOS only).",
    "shadow": "Shadow style (shown on macOS only).",
    "leading": "Line distance in world units, for custom line spacing.",
    "flipped": "Mirror the text vertically.",
}

ATTRIBUTES = {
    "pen": "Pen attributes; only the members given are changed.",
    "fill": "Fill attributes; only the members given are changed.",
    "opacity": "Opacity, 0-100.",
    "class": "Name of the class.",
}
for _part in ("pen", "fill"):
    ATTRIBUTES.update({
        _part + ".foreColor": "Foreground color (RGB).",
        _part + ".backColor": "Background color (RGB).",
        _part + ".foreColorIndex": "Foreground color as an index into the document color table.",
        _part + ".backColorIndex": "Background color as an index into the document color table.",
        _part + ".opacity": "Opacity, 0-100.",
        _part + ".style": "Raw %s style." % _part,
    })
ATTRIBUTES.update({
    "pen.lineWeightMils": "Line weight in mils.",
    "pen.lineType": "Internal index of a line type.",
    "fill.resource": "Internal index of a hatch, tile, gradient or image.",
})

DIMENSION = {
    "start": "First measured point, in world units.",
    "end": "Second measured point, in world units.",
    "offset": "Distance of the dimension line from the measured geometry, in world units.",
    "direction": "Linear dimensions: measuring direction in radians.",
    "vertex": "Angular dimensions: the vertex of the angle.",
    "referenceAngle": "Angular dimensions: measure a single leg against the reference direction.",
    "compact": "Radial dimensions: the shortened form that stops at the circle.",
    "clockwise": "Measure the clockwise arc between the points.",
    "startWitness": "Show the witness line at the start.",
    "endWitness": "Show the witness line at the end.",
    "witnessOverride": "Witness lines: 0 by standard, 1 one custom length, 2 a length per witness line, 3 one custom offset, 4 an offset per witness line.",
    "startWitnessLength": "Custom length of the start witness line.",
    "endWitnessLength": "Custom length of the end witness line.",
    "startWitnessOffset": "Custom offset of the start witness line.",
    "endWitnessOffset": "Custom offset of the end witness line.",
    "arrowsInside": "Place the arrows inside the witness lines.",
    "leaderLine": "Show the leader line.",
    "showValue": "Print the measured value.",
    "leaderText": "Text printed before the value.",
    "trailerText": "Text printed after the value.",
    "boxText": "Draw a box around the value.",
    "precision": "Decimal digits; fractional units: 0-6 = 1/1 to 1/64; angles: 1 degrees, 2 deg/min, 3 deg/min/sec.",
    "showSecondaryValue": "Also print the value in the secondary unit.",
    "secondaryLeaderText": "Text printed before the secondary value.",
    "secondaryTrailerText": "Text printed after the secondary value.",
    "secondaryBoxText": "Draw a box around the secondary value.",
    "secondaryPrecision": "Precision of the secondary value (as `precision`).",
    "noteText": "Note text added to the dimension.",
    "textPositionAutomatic": "Place the text automatically.",
    "textInside": "Place the text inside the witness lines.",
    "textFlipped": "Flip the text.",
    "textRotation": "Text rotation: 0 aligned, 1 horizontal, 2 horizontal/vertical.",
    "textOffsetAlongLine": "Offset of the text along the dimension line.",
    "textOffsetAboveLine": "Offset of the text above the dimension line.",
    "fontSize": "Font size in points.",
    "fontStyle": "Sum of 1 bold, 2 italic, 4 underline.",
    "toleranceType": "Tolerance: 0 none, 1 single, 2 double, 3 limit.",
    "tolerancePlus": "Upper tolerance value.",
    "toleranceMinus": "Lower tolerance value.",
    "standard": "Name of the dimension standard.",
    "standardIndex": "Dimension standard by index: above 0 built-in, below 0 custom.",
    "unit": "0 for document units, otherwise the index of a dimension unit setting.",
    "associate": "Bind the dimension to the geometry under its end points.",
    "associateSelectedOnly": "With `associate`: bind only to selected objects.",
}

_TEXT_TOOLS = {"createText", "editText"}
_ATTRIBUTE_TOOLS = {"editClass", "setObjectAttributes"}

_LIST_BEFORE = r"(?:^|[\s,/({]|\band\b\s)"
_LIST_AFTER = r"(?=$|[\s,/;.){:])"


def _listed(name, text):
    """Whether 'name' appears in 'text' as an item of a field list (not merely as an English word)."""
    pat = _LIST_BEFORE + r"'?" + re.escape(name) + r"'?" + _LIST_AFTER
    for m in re.finditer(pat, text):
        after = text[m.end():m.end() + 6]
        if re.match(r"^(\s*$|\s*[,/;.){:]|\s\(|\s(and|or|as|with|is|are|cannot|in)\b)", after):
            return True
    return False


_SECTION = re.compile(r"(?:^|(?<=[.;]\s))([A-Z][\w/()' -]{0,40}?):\s")
_SKIP_LABELS = {"Returns", "Return", "Note", "Notes", "Example", "Examples", "Kind-specific fields", "Errors", "Error",
                "Both kinds", "Result", "Results", "Paging", "Workflow", "Tip", "Important", "Output", "Integer codes",
                "Layout"}
_SKIP_LABEL_START = ("Optional", "Each ", "With ", "Without ", "A ", "An ", "The ")

# Remarks in parentheses that describe something else than the parameter they follow.
DROP = {
    ("createLayer", "type"), ("createPolygon", "sides"), ("getText", "lineOffset"), ("combineShapes", "class"),
    ("findObjects", "criteria"), ("editObject", "name"), ("editObject", "selected"), ("get3DGeometry", "index"),
    ("get3DGeometry", "piece"), ("edit3DGeometry", "scale3D"), ("edit3DGeometry", "closed"), ("createSweep", "axisUuid"),
    ("createSurfaceModel", "axisUuid"), ("createHardscape", "pathwayOffset"), ("createRadialDimension", "radius"),
    ("createLandscapeArea", "plantDisplay2D"), ("setOIPValues", "pane"), ("createSlab", "style"),
}


def _label_md(label):
    return label if len(label) > 1 and label[1].isupper() else label[0].lower() + label[1:]


def _sections(description):
    from mdlib import _sentences, clean
    out = []
    for line in clean(description).split("\n"):
        matches = list(_SECTION.finditer(line))
        for i, m in enumerate(matches):
            label = m.group(1).strip()
            if label in _SKIP_LABELS or label.startswith(_SKIP_LABEL_START) or len(label.split()) > 4:
                continue
            body = line[m.end():matches[i + 1].start() if i + 1 < len(matches) else len(line)]
            first = (_sentences(body.strip()) or [""])[0]
            first = "; ".join(p for p in first.split("; ") if "cannot be set" not in p)
            out.append((label, first))
    return out


def _render_paren(paren, s):
    """A remark in parentheses as a Markdown note; value lists become code lists."""
    from mdlib import code, inline
    p = paren.strip().rstrip(" ;,.")
    if re.fullmatch(r"\w[\w ]*(?:\s*\|\s*\w[\w ]*)+", p):
        return "One of: " + ", ".join(code(v.strip(), True) for v in p.split("|")) + "."
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9]*(?:, [A-Za-z][A-Za-z0-9]*)+", p):
        t, items = s.get("type"), s.get("items") if isinstance(s.get("items"), dict) else {}
        lead = {"object": "Members: ", "string": "One of: "}.get(t)
        if t == "array" and items.get("type") == "object":
            lead = "Item members: "
        return lead + ", ".join(code(v, True) for v in p.split(", ")) + "." if lead else ""
    out, pos = [], 0
    for m in re.finditer(r"\b\w+(?:\|\w+)+\b", p):
        vals = m.group(0).split("|")
        out.append(inline(p[pos:m.start()], True))
        out.append(", ".join(code(v, True) for v in vals[:-1]) + " or " + code(vals[-1], True))
        pos = m.end()
    out.append(inline(p[pos:], True))
    md = "".join(out)
    return (md[0].upper() + md[1:] if md[:1].islower() else md) + "."


def derived_notes(tool):
    """Notes derived from the tool text: the labelled sections ('Walls: ...') that list a parameter, and a short
    remark in parentheses directly after its name. Path -> (labels Markdown, remark Markdown, remark word count)."""
    from mdlib import clean, inline
    description = clean(tool["description"])
    props = tool["inputSchema"].get("properties") or {}
    sections = _sections(description)
    notes = {}
    for name, s in props.items():
        paren, words, labels = "", 0, ""
        found = list(dict.fromkeys(lab for lab, body in sections if _listed(name, body)))
        if found and len(found) < len(sections):
            labels = inline("Used for " + ", ".join(_label_md(l) for l in found) + ".", True)
        m = re.search(r"(?<![\w.])'?" + re.escape(name) + r"'?\s\(([^()]{2,120})\)", description)
        if m and (tool["name"], name) not in DROP and len(found) < 2 \
                and not re.match(r"^(e\.g\.|see |default|optional|or )", m.group(1), re.I):
            paren, words = _render_paren(m.group(1), s), len(m.group(1).split())
        notes[name] = (labels, paren, words)
    return notes


def tool_overrides(tool_name):
    return {p for (t, p) in TOOL if t == tool_name}


def param_notes(group_name, tool):
    """Path -> Markdown note for this tool; the caller uses it only where the schema gives no description."""
    from mdlib import inline
    tool_name = tool["name"]
    curated = {}
    if tool_name in _TEXT_TOOLS:
        curated.update(TEXT)
    if tool_name in _ATTRIBUTE_TOOLS:
        curated.update(ATTRIBUTES)
    if group_name == "Dimensioning" and tool_name != "createCenterMark":
        curated.update(DIMENSION)

    derived = derived_notes(tool)
    notes = {}
    for path in set(derived) | set(curated) | set(GENERIC):
        labels, paren, words = derived.get(path, ("", "", 0))
        if path in curated:
            main = inline(curated[path], True)
        elif paren and (words >= 3 or path not in GENERIC):
            main = paren
        else:
            main = inline(GENERIC[path], True) if path in GENERIC else ""
        text = " ".join(p for p in (labels, main) if p)
        if text:
            notes[path] = text
    for (t, p), n in TOOL.items():
        if t == tool_name:
            notes[p] = inline(n, True)
    return notes
