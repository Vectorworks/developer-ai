# Writes the shared pages: Common.md (conventions and the always available meta-tools) and Attributes.md (value formats).
import json
import os
import re

from pages import header, yes_no
from mdlib import EFFECTS, Page, block, code, inline, is_drop_shadow, is_marker, schema_rows, slug, tool_safety
from summaries import FOLDERS, GROUP_SUMMARY

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = json.load(open(os.path.join(HERE, "core.json"), encoding="utf-8"))

CORE_SUMMARY = {
    "listToolGroups": "List all tool groups, active and inactive, with their activation state and, optionally, their tools.",
    "activateToolGroups": "Activate tool groups for the rest of the session so that their tools appear in the tool list.",
    "runToolBatch": "Run several tool calls as one undo step, all or nothing.",
}

# (effect label, undo, in runToolBatch)
CORE_EFFECT = {
    "listToolGroups": ("Read-only", "none", "no"),
    "activateToolGroups": ("Session setting", "none (the drawing is not changed)", "no"),
    "runToolBatch": ("Edit (batch)", 'one step "MCP: <name>" for the whole batch', "no"),
}

CORE_SCHEMA = {
    "listToolGroups": {"type": "object", "properties": {
        "group": {"type": "string", "description": "Optional group display name or groupId to inspect."},
        "includeTools": {"type": "boolean", "default": False,
                         "description": "Include tool names and descriptions, even for inactive groups; no schemas."},
    }},
    "activateToolGroups": {"type": "object", "required": ["groups"], "properties": {
        "groups": {"type": "array", "items": {"type": "string"}, "description": "Group display names or groupIds to activate."},
    }},
    "runToolBatch": {"type": "object", "required": ["name", "calls"], "properties": {
        "name": {"type": "string", "minLength": 1, "maxLength": 63,
                 "description": "Name of the undo step 'MCP: <name>': not blank, without control characters; "
                                "for example 'Create walls and slab'."},
        "calls": {"type": "array", "minItems": 1, "maxItems": 50, "description": "The tool calls, run in this order.",
                  "items": {"type": "object", "required": ["tool"], "properties": {
                      "tool": {"type": "string", "description": "Name of a tool of an active group."},
                      "arguments": {"type": "object", "description": "Arguments of the tool, as in a direct call; default {}."},
                  }}},
    }},
}

CORE_EXAMPLE = {
    "listToolGroups": {"group": "architecture", "includeTools": True},
    "activateToolGroups": {"groups": ["architecture", "Dimensioning"]},
    "runToolBatch": {"name": "Create walls", "calls": [
        {"tool": "createWall", "arguments": {"start": {"x": 0, "y": 0}, "end": {"x": 5000, "y": 0}}},
        {"tool": "createWall", "arguments": {"start": {"x": 5000, "y": 0}, "end": {"x": 5000, "y": 4000}}},
    ]},
}

CORE_EXAMPLE_NOTE = {
    "runToolBatch": " (two walls in one undo step; the Architecture group must be active)",
}

# tool -> (items key, default limit); verified against the tool descriptions
PAGED = {
    "listIFCMappingObjects": ("objects", "200"),
    "findMenuCommands": ("commands", "50"),
    "getMenus": ("menus, entries or items", "100"),
    "findObjects": ("objects", "200"),
    "getObjectsAtPoint": ("objects", "50"),
    "get3DGeometry": ("items, in each list", "100"),
    "listConnectCADSignals": ("signals", "500"),
    "listConnectCADConnectors": ("connectors", "500"),
    "listGDTFs": ("gdtfs", "200"),
    "getOIPControls": ("controls", "100"),
    "getResources": ("resources", "200"),
    "getWorksheet": ("cells or subrows", "200 cells, 100 subrows"),
    "listScripts": ("scripts", "200"),
    "getTools": ("tools", "100"),
}

# (tool, list, limit and offset arguments, items key, default limit)
NESTED_PAGED = [
    ("getObjectInfo", "members", "memberLimit, memberOffset", "objects", "50"),
    ("getText", "lines", "lineLimit, lineOffset", "items", "100"),
    ("getText", "styleRuns", "runLimit, runOffset", "items", "100"),
]

EFFECT_INFO = {
    # label: (meaning, annotations)
    "Read-only": ("Reads the drawing or the application state and changes nothing.", "`readOnlyHint`: true"),
    "Edit": ("Changes the drawing. Undo reverts the change.", "`readOnlyHint`: false"),
    "Destructive edit": ("Changes the drawing in a far-reaching way.", "`readOnlyHint`: false, `destructiveHint`: true"),
    "Interactive": ("Operates the user interface like a user: tool palettes or the Object Info palette.",
                    "`readOnlyHint`: false"),
    "Interactive, destructive": ("Runs a menu command as if the user chose it.",
                                 "`readOnlyHint`: false, `destructiveHint`: true"),
    "Script run": ("Runs a Python script, which can do anything a script can do.",
                   "`readOnlyHint`: false, `destructiveHint`: true"),
}


def _tool_index(cat):
    """tool name -> (folder, group, tool)."""
    return {t["name"]: (g["folder"], g, t) for g in cat for t in g["tools"]}


def _link(index, name):
    if name not in index:
        raise KeyError("shared.py names the tool %r, which is not in the catalog any more; update the text" % name)
    folder = index[name][0]
    return "[%s](%s.md#%s)" % (code(name), folder, name.lower())


def _links(index, names):
    return ", ".join(_link(index, n) for n in names)


def _fmt(value, indent=0):
    """JSON with small objects and arrays kept on one line."""
    one = json.dumps(value, ensure_ascii=False)
    if not isinstance(value, (dict, list)) or not value or (indent and len(one) <= 72):
        return one
    pad = " " * (indent + 2)
    if isinstance(value, dict):
        parts = ["%s%s: %s" % (pad, json.dumps(k, ensure_ascii=False), _fmt(v, indent + 2)) for k, v in value.items()]
        return "{\n" + ",\n".join(parts) + "\n" + " " * indent + "}"
    parts = [pad + _fmt(v, indent + 2) for v in value]
    return "[\n" + ",\n".join(parts) + "\n" + " " * indent + "]"


def _json(value):
    return ["```json", _fmt(value), "```", ""]


# ---- Common.md -------------------------------------------------------------------------------------------------------

def common_page(cat):
    index = _tool_index(cat)
    tagline, intro = FOLDERS["Common"]
    page = Page("Common — %s" % tagline, header(), [inline(intro), ""])

    topics = [
        ("Tool groups and activation", "Which tools are available and how to switch groups on."),
        ("Core group", "The three meta-tools that are always available: `listToolGroups`, `activateToolGroups`, `runToolBatch`."),
        ("Calling a tool", "The shape of a call and of its result, with an example."),
        ("Results and errors", "Result objects, error messages and rolled back calls."),
        ("Object references", "How tools identify objects in their arguments and in their results."),
        ("Points, rectangles and colors", "The shared value formats for geometry and color."),
        ("Units and angles", "World units, radians and the few exceptions."),
        ("Creation options", "The options that every create tool accepts: class, name and selection."),
        ("Applied settings", "How tools report, setting by setting, what they wrote."),
        ("Plug-in parameters", "Reading and writing the parameters of plug-in objects."),
        ("Paging", "How long lists are returned page by page."),
        ("Effects and risk levels", "What a tool may change, and how clients should treat it."),
        ("Undo", "How the changes of a tool call are recorded for Edit > Undo."),
    ]
    page.h(2, "Overview")
    page.table(["Topic", "What it covers"], [["[%s](#%s)" % (t, slug(t)), inline(d, True)] for t, d in topics])

    _groups_section(page, cat)
    _core_section(page)
    _calling_section(page)
    _results_section(page)
    _references_section(page)
    _geometry_section(page)
    _units_section(page)
    _creation_section(page, cat, index)
    _applied_section(page, cat, index)
    _params_section(page, cat, index)
    _paging_section(page, index)
    _effects_section(page, cat, index)
    _undo_section(page, cat, index)
    return page.render()


def _groups_section(page, cat):
    page.h(2, "Tool groups and activation")
    active = [g for g in cat if g["fActiveByDefault"]]
    page.para([
        "The tools are organized in tool groups. The tool list of the server (`tools/list`) shows only the tools of the "
        "**active** groups, so a tool that is missing from the list is not necessarily unsupported.",
        "",
        "- %d groups are active by default: %s. The **Core** group is always active." % (
            len(active), ", ".join(g["fName"] for g in active)),
        "- The other groups are activated with [`activateToolGroups`](#activatetoolgroups) and stay active for the rest "
        "of the session. Refresh the tool list afterwards (clients that handle the `list_changed` notification do this "
        "automatically).",
        "- [`listToolGroups`](#listtoolgroups) lists every group, active or not, and with `includeTools` the names and "
        "descriptions of its tools.",
        "- Groups are named by their display name or by their group ID; both are accepted.",
    ])
    rows = [["[Core](#core-group)", code(CORE["groupId"], True), "[Common](#core-group)", "Always", CORE["safetyLevel"],
             str(CORE["toolCount"]), inline(CORE_SUMMARY_GROUP, True)]]
    for g in cat:
        rows.append(["[%s](%s.md#%s)" % (g["fName"], g["folder"], slug(g["fName"])), code(g["groupId"], True),
                     "[%s](%s.md)" % (g["folder"], g["folder"]), yes_no(g["fActiveByDefault"]), g["fSafetyLevel"],
                     str(len(g["tools"])), inline(GROUP_SUMMARY[g["fName"]], True)])
    page.table(["Group", "Group ID", "Page", "Active by default", "Risk level", "Tools", "Summary"], rows)


CORE_SUMMARY_GROUP = "Discover and activate tool groups, and run several tool calls as one undo step."


def _core_section(page):
    page.h(2, "Core group")
    page.para(["> **Group:** `Core` · **Group ID:** `%s` · **Active:** always · **Risk level:** %s · **Tools:** %d"
               % (CORE["groupId"], CORE["safetyLevel"], CORE["toolCount"])])
    page.para(["**" + CORE_SUMMARY_GROUP + "**"])
    page.para(["The meta-tools of the Core group are always available. They manage the tool list and group tool calls; "
               "they cannot be called inside [`runToolBatch`](#runtoolbatch)."])
    rows = []
    for t in CORE["tools"]:
        label = CORE_EFFECT[t["name"]][0]
        rows.append(["[%s](#%s)" % (code(t["name"]), t["name"].lower()), label, t["safetyLevel"],
                     inline(CORE_SUMMARY[t["name"]], True)])
    page.table(["Tool", "Effect", "Risk", "Summary"], rows)

    for t in CORE["tools"]:
        name = t["name"]
        page.h(3, name)
        label, undo, batch = CORE_EFFECT[name]
        page.para([inline(CORE_SUMMARY[name])])
        page.para(["> **Effect:** %s · **Risk:** %s · **Undo:** %s · **In runToolBatch:** %s"
                   % (label, t["safetyLevel"], inline(undo), batch)])
        page.para(["**Details**"])
        page.para(block(t["description"]))
        page.para(["**Parameters**"])
        page.table(["Parameter", "Type", "Required", "Description"], list(schema_rows(CORE_SCHEMA[name])))
        page.para(["**Example arguments**" + CORE_EXAMPLE_NOTE.get(name, "")])
        page.add(*_json(CORE_EXAMPLE[name]))


def _calling_section(page):
    page.h(2, "Calling a tool")
    page.para([
        "A tool is called with the MCP `tools/call` request: the tool `name` and an `arguments` object. Arguments that "
        "are not needed are left out. Every tool returns one JSON object.",
        "",
        "For example, list the rectangles of the drawing, two at a time:",
    ])
    page.add(*_json({"name": "findObjects", "arguments": {"criteria": "(T=RECT)", "limit": 2}}))
    page.para(["The result, with placeholders for the UUIDs:"])
    page.add(*_json({
        "count": 3, "limit": 2, "nextOffset": 2,
        "notSearched": ["INSYMBOL", "INOBJECT", "INVIEWPORT", "INOBJPATH", "INOBJPROFILE"],
        "objects": [
            {"type": 3, "typeName": "Rectangle", "uuid": "<uuid 1>"},
            {"name": "Plot outline", "type": 3, "typeName": "Rectangle", "uuid": "<uuid 2>"},
        ],
        "offset": 0, "returned": 2, "truncated": True,
    }))
    page.para([
        "`count` is the number of all matches, `objects` holds this page of [object references](#object-references) and "
        "`nextOffset` is the `offset` of the next page (see [Paging](#paging)). `notSearched` lists the places that the "
        "criteria did not include, such as the inside of symbol definitions.",
    ])


def _results_section(page):
    page.h(2, "Results and errors")
    page.para([
        "- Every tool returns one JSON object. The keys of the object are described with each tool.",
        "- A call that fails returns an object with `err`, a message that says what went wrong. For example:",
    ])
    page.add(*_json({"err": "object not found (provide 'uuid', 'name' or 'index')"}))
    page.para([
        "- Arguments are checked before anything changes. Messages name the argument, for example "
        "`'limit' must be a number`, `'countOnly' must be true or false`, `'limit' must be at least 1` or "
        "`'offset' must not be negative`.",
        "- When a call that edits the drawing fails, its changes are reverted and the result reports `rolledBack`. "
        "See [Undo](#undo).",
        "- Tools that write several settings report, setting by setting, what they wrote in `applied`. "
        "See [Applied settings](#applied-settings).",
    ])


def _references_section(page):
    page.h(2, "Object references")
    page.para(["Tools that work on one existing object take the object in one of three arguments:"])
    page.table(["Argument", "Type", "Meaning"], [
        [code("uuid", True), "string", "The UUID of the object, as reported by the tools. The preferred way."],
        [code("name", True), "string", "The exact Vectorworks name of the object (Object Info palette, Name field)."],
        [code("index", True), "integer", "The internal index of the object."],
    ])
    page.para([
        "The server tries `uuid` first, then `name`, then `index`, and uses the first that finds an object. When none "
        "finds one, the call fails with `object not found (provide 'uuid', 'name' or 'index')`. Some tools name the "
        "argument after its role, such as `targetUuid`, `pathUuid` or `profileUuid`; these take a UUID.",
        "",
        "Tools that return objects (search results, created objects, group members) report them as **object "
        "references**:",
    ])
    page.table(["Key", "Type", "Meaning"], [
        [code("uuid", True), "string", "The UUID of the object."],
        [code("type", True), "integer", "The numeric Vectorworks object type, for example 2 for a line, 3 for a rectangle "
                                         "and 86 for a plug-in object."],
        [code("typeName", True), "string", "The type name, for the common types only: Line, Rectangle, Oval, Polygon, Arc, "
                                            "FreehandPolygon, Text, Group, RoundedRectangle, Symbol, SymbolDefinition, Locus, "
                                            "Polyline, Extrude, Mesh and Layer."],
        [code("parametricName", True), "string", "Plug-in objects only: the universal name of the plug-in, for example "
                                                  "`Door`."],
        [code("localizedParametricName", True), "string", "Plug-in objects only: the plug-in name in the language of "
                                                           "Vectorworks, when the plug-in is installed."],
        [code("name", True), "string", "The object name, when the object has one."],
    ])
    page.para(["Use the `uuid` of a reference in the next call."])


def _geometry_section(page):
    page.h(2, "Points, rectangles and colors")
    page.h(3, "Points")
    page.para([
        "A 2D point is an object `{ \"x\": 0, \"y\": 0 }` in world units; the array form `[x, y]` is also accepted. "
        "A 3D point adds `z`: `{ \"x\": 0, \"y\": 0, \"z\": 0 }`.",
        "",
        "3D tools use layer coordinates: `z` is relative to the elevation of the design layer. Where a tool reports "
        "`bounds3D`, its Z values are absolute world heights.",
    ])
    page.h(3, "Rectangles")
    page.para([
        "A rectangle is `{ \"left\": 0, \"top\": 1000, \"right\": 2000, \"bottom\": 0 }` in world units, with `top` above "
        "`bottom`. Bounds that the tools report add `width`, `height` and `center` (a point):",
    ])
    page.add(*_json({"left": 0, "top": 1000, "right": 2000, "bottom": 0, "width": 2000, "height": 1000,
                     "center": {"x": 1000, "y": 500}}))
    page.h(3, "Colors")
    page.para([
        "A color is `{ \"r\": 255, \"g\": 128, \"b\": 0 }` with channels from 0 to 255; the array form `[r, g, b]` is also "
        "accepted. Values outside 0 to 255 are clamped. Attributes that can also use the document color table have a "
        "separate index key next to the RGB value, such as `foreColorIndex` next to `foreColor`; when both are given "
        "and both change, the index wins.",
    ])


def _units_section(page):
    page.h(2, "Units and angles")
    page.para(["Unless a tool says otherwise:"])
    page.table(["Value", "Unit"], [
        ["Coordinates, lengths, distances, offsets", "World units: the units of the drawing. Read them with "
                                                     "`getUnits`; convert with `convertUnits`."],
        ["Angles, rotations", "Radians, counter-clockwise positive."],
        ["Text", "UTF-8 strings."],
        ["Colors", "RGB, 0 to 255 per channel (see [Colors](#colors))."],
    ])
    page.para(["The exceptions are named in the tool descriptions. The main ones:"])
    page.table(["Value", "Unit"], [
        ["Font sizes", "Points."],
        ["Line end marker angle", "Whole degrees (see [Line end markers](Attributes.md#line-end-markers))."],
        ["Line end marker length and width", "Page inches."],
        ["Drop shadow angle", "Degrees (see [Drop shadow](Attributes.md#drop-shadow))."],
        ["Drop shadow offset and blur radius", "Page inches or world units, as `units` says."],
        ["Roof slopes", "Degrees."],
        ["Plug-in parameters read as typed values", "Lengths in world units, angles in degrees "
                                                    "(see [Plug-in parameters](#plug-in-parameters))."],
        ["Object Info palette values", "Typed as a user types them, in the units the palette shows."],
    ])


def _creation_section(page, cat, index):
    page.h(2, "Creation options")
    tools = [t["name"] for g in cat for t in g["tools"]
             if all(k in (t["inputSchema"].get("properties") or {}) for k in ("class", "name", "select", "useClassAttributes"))]
    page.para(["The tools that create objects accept four optional creation options. They are applied to the new "
               "object after it is created, and the tool then returns its [object reference](#object-references)."])
    page.table(["Option", "Type", "Meaning"], [
        [code("class", True), "string", "The class of the new object. A class that does not exist yet is created."],
        [code("useClassAttributes", True), "boolean", "With `class`: also set the graphical attributes of the object to "
                                                      "\"by class\"."],
        [code("name", True), "string", "The name of the new object."],
        [code("select", True), "boolean", "Select the new object."],
    ])
    page.para(["Tools with these options (%d): %s." % (len(tools), _links(index, tools))])


def _applied_section(page, cat, index):
    page.h(2, "Applied settings")
    tools = [t["name"] for g in cat for t in g["tools"] if "'applied'" in t["description"]]
    page.para([
        "Tools that write several settings in one call report the outcome of each in `applied`: an object with one entry "
        "per setting given, `true` when it was written and `false` when it was not (for example because the value does "
        "not fit or the object does not support the setting). A call can therefore succeed while single settings are "
        "rejected; check `applied` when it matters.",
        "",
        "For example, %s with these arguments:" % _link(index, "editLayer"),
    ])
    page.add(*_json({"name": "Design Layer-1", "elevation": 3000, "scale": 50}))
    page.para(["returns the updated layer with:"])
    page.add(*_json({"applied": {"elevation": True, "scale": True}}))
    page.para(["Tools that report `applied` (%d): %s." % (len(tools), _links(index, tools))])


def _params_section(page, cat, index):
    page.h(2, "Plug-in parameters")
    writers, readers = [], []
    for g in cat:
        for t in g["tools"]:
            p = (t["inputSchema"].get("properties") or {}).get("params")
            if p is None:
                continue
            (readers if p.get("type") == "array" else writers).append(t["name"])
    page.para([
        "Plug-in objects (doors, windows, plants, lighting devices, data tags and many more) keep their settings in "
        "parameters, named by their universal (not localized) names. Use %s to see which plug-in an object is "
        "(`parametricName`) and %s to see the parameters a plug-in has." % (
            _link(index, "getObjectInfo"), _link(index, "getPluginDefinition")),
    ])
    page.h(3, "Reading parameters")
    page.para([
        "- %s returns every parameter, or the ones in `names`, as display strings, and with `includeDefinitions` the "
        "type, localized name and pop-up choices of each." % _link(index, "getObjectParameters"),
        "- The `params` argument of %s takes an array of parameter names and returns their exact, typed values:" % _links(index, readers),
    ])
    page.table(["Parameter type", "JSON value"], [
        ["Real, dimension, coordinate, angle, area, volume", "number: lengths in world units, angles in degrees"],
        ["Integer, dimension standard pop-up", "integer"],
        ["Boolean", "`true` or `false`"],
        ["Any other type (text, pop-up, ...)", "string"],
    ])
    page.h(3, "Writing parameters")
    page.para([
        "- %s writes one parameter (`name` and `value`; the type comes from the parameter definition, or from `type`: "
        "`real`/`number`, `int`/`integer`, `bool`/`boolean`, otherwise text) or several at once with `params`."
        % _link(index, "setObjectParameter"),
        "- A `params` object `{ \"ParamName\": value }` writes parameters by universal name in %s."
        % _links(index, [w for w in writers if w != "setObjectParameter"]),
        "- %s and %s write values the same way: numeric parameters also accept numeric strings such as `\"5\"`, a "
        "value that cannot be converted to the parameter type is not written and is reported `false`, and the object "
        "is regenerated afterwards." % (_link(index, "setObjectParameter"), _link(index, "createPluginObject")),
        "- %s takes reals in world units, the form in which %s reads them with `params`, so a value that was read "
        "can be written back unchanged." % (_link(index, "setArchitectureObject"), _link(index, "getArchitectureObject")),
    ])


def _paging_section(page, index):
    page.h(2, "Paging")
    page.para(["Tools that can return long lists return them page by page. They take the same paging arguments:"])
    page.table(["Argument", "Type", "Meaning"], [
        [code("limit", True), "integer", "The maximum number of items in this page; at least 1. The default depends on "
                                         "the tool (see below)."],
        [code("offset", True), "integer", "The number of items to skip; not negative. Default 0."],
        [code("countOnly", True), "boolean", "Return only the count and the paging keys, without the items. Default false."],
    ])
    page.para(["and report the same paging keys next to the items:"])
    page.table(["Key", "Meaning"], [
        [code("count", True), "The total number of items (or matches)."],
        [code("returned", True), "The number of items in this page."],
        [code("offset", True), "The offset of this page."],
        [code("limit", True), "The limit used."],
        [code("truncated", True), "`true` when more items follow."],
        [code("nextOffset", True), "The `offset` of the next page; only present when `truncated` is true."],
    ])
    page.para(["To read a whole list, call the tool again with `offset` set to `nextOffset` until `truncated` is false. "
               "To count or to check existence, use `countOnly`."])
    page.para(["**Paged tools**"])
    page.table(["Tool", "Items key", "Default limit"],
               [[_link(index, n), code_list(k), d] for n, (k, d) in PAGED.items()])
    page.para(["**Paged lists inside a result**",
               "",
               "Some results contain a list that is paged with arguments of its own. Each such list is an object with "
               "the paging keys and the items:"])
    page.table(["Tool", "List", "Arguments", "Items key", "Default limit"],
               [[_link(index, n), code(lst, True), ", ".join(code(a.strip(), True) for a in args.split(",")),
                 code(key, True), d] for n, lst, args, key, d in NESTED_PAGED])


def code_list(text):
    """'menus, entries or items' -> `menus`, `entries` or `items`; trailing words after a comma are kept as text."""
    words = re.split(r"(, | or )", text)
    out = []
    for w in words:
        if w in (", ", " or ") or " " in w:
            out.append(w)
        else:
            out.append(code(w, True))
    return "".join(out)


def _effects_section(page, cat, index):
    page.h(2, "Effects and risk levels")
    by_label = {}
    for g in cat:
        for t in g["tools"]:
            by_label.setdefault(EFFECTS[t["effect"]][0], []).append((g, t))
    page.para([
        "Every tool has an **effect**, which says what it may change, and a **risk level**, which says how carefully a "
        "client should treat it. Both are shown with each tool. The tool list reports the effect to MCP clients through "
        "the standard tool annotations `readOnlyHint` and `destructiveHint`. A higher risk level means a call can change "
        "more or is harder to undo; the server reports it in the `safetyLevel` field.",
    ])
    rows = []
    for label, (meaning, annotations) in EFFECT_INFO.items():
        tools = by_label.get(label, [])
        if not tools:
            continue
        levels = sorted({tool_safety(t["effect"], g["fSafetyLevel"]) for g, t in tools}, key=["low", "medium", "high"].index)
        effect = next(t["effect"] for g, t in tools)
        undo = EFFECTS[effect][1].format(tool="<tool>")
        rows.append([label, meaning, " or ".join(levels), annotations, inline(undo, True), EFFECTS[effect][2], str(len(tools))])
    page.table(["Effect", "Meaning", "Risk level", "Annotations", "Undo", "In runToolBatch", "Tools"], rows)
    page.para([
        "**Risk levels**",
        "",
        "- **low**: reads, session changes (such as which tool groups are active), and the plain edits of the document "
        "settings and of 2D primitives and text (%s). Edit > Undo reverts the edits." % _level_groups(cat, "low"),
        "- **medium**: edits of objects, 3D geometry, annotation and industry objects, resources and worksheets, and the "
        "interactive tools that operate the tool palettes and the Object Info palette. Edit > Undo reverts them.",
        "- **high**: menu commands and scripts, which may make far-reaching changes that are hard to predict. Clients "
        "should ask the user before each call. These tools cannot run inside [`runToolBatch`](#runtoolbatch).",
        "",
        "Each group has a risk level, shown on its page. A tool reports its own level: read-only tools are always low, "
        "interactive tools medium, menu commands and scripts high, and the other edit tools take the level of their "
        "group unless the tool sets its own.",
    ])
    lists = [(label, [t["name"] for g, t in by_label[label]]) for label in EFFECT_INFO if label != "Read-only" and label != "Edit"
             and label in by_label]
    if lists:
        page.para(["**Tools with a special effect**", ""] +
                  ["- %s: %s." % (label, _links(index, names)) for label, names in lists])


def _level_groups(cat, level):
    return ", ".join("[%s](%s.md#%s)" % (g["fName"], g["folder"], slug(g["fName"])) for g in cat if g["fSafetyLevel"] == level)


def _undo_section(page, cat, index):
    page.h(2, "Undo")
    interactive = [t["name"] for g in cat for t in g["tools"] if t["effect"] in ("OwnUndo", "OwnUndoHighRisk")]
    scripts = [t["name"] for g in cat for t in g["tools"] if t["effect"] == "RunsScript"]
    page.para([
        "- **Edit tools**: each successful call is one undo step named `MCP: <tool>`, for example `MCP: createWall`. "
        "Edit > Undo reverts it, and Vectorworks shows the name in its status message.",
        "- **Failed calls**: when an edit call fails, everything it changed is reverted and the result reports "
        "`rolledBack`. Nothing is left half done.",
        "- **Read-only tools** add no undo step.",
        "- **Batches**: [`runToolBatch`](#runtoolbatch) runs several calls as one undo step `MCP: <name>`, all or nothing. "
        "Inside a batch each call joins that step; when one fails, the batch stops and everything it did is reverted.",
        "- **Interactive tools** (%s) are recorded by Vectorworks the same way as the user's own actions, so Edit > Undo "
        "reverts them as it would for the user." % _links(index, interactive),
        "- **Scripts** (%s) run in one undo step `MCP: script`. The step is kept after a successful run, or one that waits "
        "for user input, and reverted after a failed run (`rolledBack`)." % _links(index, scripts),
    ])


# ---- Attributes.md ---------------------------------------------------------------------------------------------------

MARKER_NOTES = {
    "shape": "The shape of the marker.",
    "fill": "`lineColor` fills the marker with the line color, `white` with white, `none` leaves it open.",
    "base": "The shape of the marker base.",
    "halfTick": "Draw the whole marker, or only its left or right half.",
    "tail": "Add the marker tail.",
    "angle": "The opening angle, in whole degrees.",
    "length": "The length, in page inches.",
    "width": "The width, in page inches.",
    "thickness": "The line thickness of the marker, in `thicknessUnits`. A changed thickness sets `thicknessBasis` to "
                 "`custom`.",
    "thicknessBasis": "Where the thickness comes from: the line thickness of the object, the dimension line thickness, "
                      "or the custom `thickness`.",
    "thicknessUnits": "The units of `thickness`.",
    "visible": "Show the marker. Classes do not store it; for objects, `markers.beginningVisible` and "
               "`markers.endVisible` do the same.",
}

SHADOW_NOTES = {
    "enabled": "Draw the drop shadow.",
    "units": "The units of `offset` and `blurRadius`: page inches (`page`) or world units (`world`).",
    "offset": "The distance of the shadow from the object, in `units`.",
    "blurRadius": "The blur radius, in `units`.",
    "angle": "The direction of the shadow, in degrees.",
    "colorIndex": "The shadow color as an index into the document color table.",
    "color": "The shadow color as RGB (see [Colors](Common.md#colors)). When both `color` and `colorIndex` change, "
             "`colorIndex` wins.",
    "opacity": "The opacity, 0 to 100.",
    "byClass": "Objects only: use the drop shadow of the class of the object.",
    "delete": "Objects only: remove the drop shadow of the object itself.",
}


def _find(cat, pred):
    """(tool name, folder, path) of every schema value that matches pred, and the first such schema."""
    hits, first = [], None

    def walk(s, path, t, folder):
        nonlocal first
        if not isinstance(s, dict):
            return
        if pred(s):
            hits.append((t["name"], folder, path))
            first = first or s
        for k, v in (s.get("properties") or {}).items():
            walk(v, path + "." + k if path else k, t, folder)
        if isinstance(s.get("items"), dict):
            walk(s["items"], path + "[]", t, folder)

    for g in cat:
        for t in g["tools"]:
            walk(t["inputSchema"], "", t, g["folder"])
    return hits, first


def _member_rows(schema, notes):
    rows = []
    for name, s in schema["properties"].items():
        from mdlib import type_of
        label = type_of(s)[0]
        n = notes.get(name, "")
        if "enum" in s:
            n += " One of: " + ", ".join(code(v, True) for v in s["enum"]) + "."
        rows.append([code(name, True), label, inline(n.strip(), True) if "`" not in n else n.strip()])
    return rows


def attributes_page(cat):
    index = _tool_index(cat)
    tagline, intro = FOLDERS["Attributes"]
    page = Page("Attributes — %s" % tagline, header(), [inline(intro), ""])
    markers, marker_schema = _find(cat, is_marker)
    shadows, shadow_schema = _find(cat, is_drop_shadow)

    page.h(2, "Overview")
    page.table(["Format", "Used in", "Summary"], [
        ["[Line end markers](#line-end-markers)", _links(index, sorted({h[0] for h in markers})),
         "The arrowheads, ticks and other markers at the start and end of lines, arcs, polylines and walls."],
        ["[Drop shadow](#drop-shadow)", _links(index, sorted({h[0] for h in shadows})),
         "The drop shadow drawn behind an object."],
    ])
    page.para([
        "Both formats are **partial**: only the members given are changed, the others keep their values. A value equal "
        "to the current one is ignored, so a marker or drop shadow that was read can be sent back with one member edited.",
    ])

    page.h(2, "Line end markers")
    page.para(["A line end marker is an object with these members, all optional:"])
    page.table(["Member", "Type", "Description"], _member_rows(marker_schema, MARKER_NOTES))
    page.para(["**Example**: an open arrow at the end of a line, made a little longer.", ""])
    page.add(*_json({"uuid": "<uuid>", "markers": {"end": {"shape": "arrow", "fill": "none", "length": 0.2, "angle": 20},
                                                   "endVisible": True}}))
    page.para(["**Where this format is used**"])
    rows = [[_link(index, n), code(p, True)] for n, folder, p in markers]
    page.table(["Tool", "Argument"], rows)
    page.para([
        "With %s, `markers` also takes `beginningVisible` and `endVisible` (show or hide each marker) and `byClass` "
        "(use the markers of the class). %s and %s (`detailed`) read markers in the same format; %s and %s read and write "
        "the default markers of the document." % (
            _link(index, "setObjectAttributes"), _link(index, "getObjectAttributes"), _link(index, "getClasses"),
            _link(index, "getPreferences"), _link(index, "setPreferences")),
    ])

    page.h(2, "Drop shadow")
    page.para(["A drop shadow is an object with these members, all optional:"])
    page.table(["Member", "Type", "Description"], _member_rows(shadow_schema, SHADOW_NOTES))
    page.para(["**Example**: a soft black shadow at half opacity, 0.05 page inches from the object.", ""])
    page.add(*_json({"uuid": "<uuid>", "dropShadow": {"enabled": True, "units": "page", "offset": 0.05, "angle": -45,
                                                      "blurRadius": 0.03, "opacity": 50,
                                                      "color": {"r": 0, "g": 0, "b": 0}}}))
    page.para(["**Where this format is used**"])
    rows = [[_link(index, n), code(p, True)] for n, folder, p in shadows]
    page.table(["Tool", "Argument"], rows)
    page.para([
        "%s also accepts `true` or `false` for `dropShadow` to switch the drop shadow of an object on or off. %s and %s "
        "(`detailed`) read drop shadows in the same format." % (
            _link(index, "setObjectAttributes"), _link(index, "getObjectAttributes"), _link(index, "getClasses")),
    ])
    return page.render()
