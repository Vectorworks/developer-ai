# Writes README.md: the index of the reference, with the tool tree, the contents by category and the A-Z index.
import json

import summaries
from pages import yes_no
from shared import CORE, CORE_SUMMARY, CORE_SUMMARY_GROUP, _fmt
from mdlib import EFFECTS, Page, code, inline, slug
from summaries import CATEGORIES, FOLDERS, GROUP_SUMMARY, TOOL_SUMMARY

SHARED = ["Attributes", "Common"]


def _folders(by_folder):
    """Every page in the order of the tool folders, the shared pages included."""
    return sorted(SHARED + list(by_folder), key=str.lower)


def _group_link(g):
    return "[%s](%s.md#%s)" % (g["fName"], g["folder"], slug(g["fName"]))


def _tool_link(folder, name):
    return "[%s](%s.md#%s)" % (code(name), folder, name.lower())


def readme(cat, by_folder):
    page = Page("Vectorworks MCP server — tool reference for %s" % summaries.VERSION, "", [])
    tools_total = sum(len(g["tools"]) for g in cat)
    page.head = [
        "# " + page.title, "",
        "This reference documents the tools of the Vectorworks MCP server: what each tool does, the arguments it takes "
        "and what it returns. The %d tools are organized in %d tool groups, plus the %d always available meta-tools "
        "of the Core group. There is one page per area, with a table of contents at the top of every page and the same "
        "layout for every group and tool." % (tools_total, len(cat), CORE["toolCount"]),
        "",
        "For what MCP is and how the server runs, see [Vectorworks MCP Server](../README.md).",
        "",
    ]

    _getting_started(page, cat)
    _conventions(page)
    _tree(page, by_folder)
    _contents(page, by_folder)
    _index(page, cat)
    _layout(page)
    _statistics(page, by_folder)
    return page.render()


def _getting_started(page, cat):
    page.h(2, "Getting started")
    active = [g for g in cat if g["fActiveByDefault"]]
    page.para([
        "1. Connect an MCP client to the Vectorworks MCP server and open a drawing in Vectorworks.",
        "2. The tool list (`tools/list`) shows the tools of the active groups only: the [Core](Common.md#core-group) "
        "meta-tools and the groups active by default, %s." % ", ".join(_group_link(g) for g in active),
        "3. Call [`listToolGroups`](Common.md#listtoolgroups) to see every group, and "
        "[`activateToolGroups`](Common.md#activatetoolgroups) to switch on the groups you need, such as "
        "[Architecture](ObjectsArchitect.md#architecture). Then refresh the tool list.",
        "4. Call the tools. Each call is undone with one Edit > Undo; use [`runToolBatch`](Common.md#runtoolbatch) to "
        "make several calls one undo step.",
        "",
        "For example, activate the Architecture group and draw a wall:",
    ])
    for call in ({"name": "activateToolGroups", "arguments": {"groups": ["architecture"]}},
                 {"name": "createWall", "arguments": {"start": {"x": 0, "y": 0}, "end": {"x": 5000, "y": 0},
                                                      "thickness": 200}}):
        page.add("```json", _fmt(call), "```", "")
    page.para(["`createWall` returns the [object reference](Common.md#object-references) of the new wall, whose "
               "`uuid` the next calls use. Lengths are in the units of the drawing (millimeters in this example)."])


def _conventions(page):
    page.h(2, "Conventions")
    page.para(["The [Common](Common.md) page describes the conventions that every tool follows; "
               "[Attributes](Attributes.md) describes the line end marker and drop shadow formats."])
    rows = [
        ("Tool groups and activation", "Common.md#tool-groups-and-activation",
         "Only the tools of active groups are listed. `activateToolGroups` switches groups on for the session."),
        ("Results and errors", "Common.md#results-and-errors",
         "Every tool returns one JSON object; a failure returns `{ \"err\": \"...\" }`."),
        ("Object references", "Common.md#object-references",
         "Objects are passed as `uuid` (preferred), `name` or `index`, and returned with `uuid`, `type`, `typeName` and "
         "`name`."),
        ("Points, rectangles and colors", "Common.md#points-rectangles-and-colors",
         "`{ x, y }`, `{ left, top, right, bottom }` and `{ r, g, b }` with channels 0 to 255."),
        ("Units and angles", "Common.md#units-and-angles",
         "Lengths in world units (the units of the drawing), angles in radians, unless a tool says otherwise."),
        ("Creation options", "Common.md#creation-options",
         "Create tools accept `class`, `useClassAttributes`, `name` and `select`."),
        ("Applied settings", "Common.md#applied-settings",
         "Tools that write several settings report each one in `applied`."),
        ("Plug-in parameters", "Common.md#plug-in-parameters",
         "Parameters of plug-in objects are read and written by universal name, with `params`."),
        ("Paging", "Common.md#paging",
         "Long lists take `limit`, `offset` and `countOnly` and report `count`, `truncated` and `nextOffset`."),
        ("Effects and safety levels", "Common.md#effects-and-safety-levels",
         "Each tool is read-only, an edit, interactive or a script run, with a safety level low, medium or high."),
        ("Undo", "Common.md#undo",
         "Each edit call is one undo step `MCP: <tool>`; a failed call is reverted."),
        ("Line end markers and drop shadows", "Attributes.md",
         "Partial objects: only the members given are changed."),
    ]
    page.table(["Topic", "Convention"], [["[%s](%s)" % (t, l), inline(d, True)] for t, l, d in rows])


def _tree(page, by_folder):
    page.h(2, "Tool tree")
    page.para(["The pages of this reference and the tool groups they document, in the order of the tool folders. "
               "Groups marked *active* are active by default."])
    entries = []   # (depth, text, target, note)
    for folder in _folders(by_folder):
        if folder == "Common":
            entries.append((0, folder, folder + ".md", "conventions"))
            entries.append((1, "Core", "", "%d tools, always active" % CORE["toolCount"]))
        elif folder == "Attributes":
            entries.append((0, folder, folder + ".md", "line end markers, drop shadows"))
        else:
            entries.append((0, folder, folder + ".md", ""))
            for g in by_folder[folder]:
                entries.append((1, g["fName"], "", "%d tools%s" % (len(g["tools"]), ", active" if g["fActiveByDefault"] else "")))
    lines = ["Vectorworks MCP server"]
    width = 34
    for i, (depth, text, target, note) in enumerate(entries):
        last_top = all(e[0] != 0 for e in entries[i + 1:])
        if depth == 0:
            prefix = "└── " if last_top else "├── "
        else:
            nxt = entries[i + 1][0] if i + 1 < len(entries) else 0
            prefix = ("    " if _parent_is_last(entries, i) else "│   ") + ("├── " if nxt == 1 else "└── ")
        label = prefix + text
        if target:
            label = label.ljust(width) + "→ " + target
            if note:
                label = label.ljust(width + 22) + note
        elif note:
            label = label.ljust(width) + "(" + note + ")"
        lines.append(label.rstrip())
    page.add("```text", *lines, "```", "")


def _parent_is_last(entries, i):
    j = i
    while entries[j][0] != 0:
        j -= 1
    return all(e[0] != 0 for e in entries[j + 1:])


def _contents(page, by_folder):
    page.h(2, "Contents by category")
    page.para(["Every page, group and tool, by subject. Each tool links to its description."])
    for title, desc, folders in CATEGORIES:
        page.h(3, title)
        page.para([desc])
        lines = []
        for folder in folders:
            tagline, intro = FOLDERS[folder]
            lines.append("- **[%s](%s.md)** — %s" % (folder, folder, inline(intro)))
            if folder == "Common":
                lines.append("  - **[Core](Common.md#core-group)** (`core`, %d tools, always active) — %s"
                             % (CORE["toolCount"], CORE_SUMMARY_GROUP))
                for t in CORE["tools"]:
                    lines.append("    - [%s](Common.md#%s) — %s" % (code(t["name"]), t["name"].lower(),
                                                                   inline(CORE_SUMMARY[t["name"]])))
                lines.append("  - Conventions: [Calling a tool](Common.md#calling-a-tool) · "
                             "[Results and errors](Common.md#results-and-errors) · "
                             "[Object references](Common.md#object-references) · "
                             "[Points, rectangles and colors](Common.md#points-rectangles-and-colors) · "
                             "[Units and angles](Common.md#units-and-angles) · "
                             "[Creation options](Common.md#creation-options) · "
                             "[Applied settings](Common.md#applied-settings) · "
                             "[Plug-in parameters](Common.md#plug-in-parameters) · [Paging](Common.md#paging) · "
                             "[Effects and safety levels](Common.md#effects-and-safety-levels) · [Undo](Common.md#undo)")
                continue
            if folder == "Attributes":
                lines.append("  - Formats: [Line end markers](Attributes.md#line-end-markers) · "
                             "[Drop shadow](Attributes.md#drop-shadow)")
                continue
            for g in by_folder[folder]:
                lines.append("  - **%s** (%s, %d tools, %s) — %s" % (
                    _group_link(g), code(g["groupId"]), len(g["tools"]),
                    "active by default" if g["fActiveByDefault"] else "inactive by default",
                    inline(GROUP_SUMMARY[g["fName"]])))
                for t in g["tools"]:
                    lines.append("    - %s — %s" % (_tool_link(folder, t["name"]), inline(TOOL_SUMMARY[t["name"]])))
        page.para(lines)


def _index(page, cat):
    page.h(2, "Index A–Z")
    entries = [(t["name"], "Core", "[Core](Common.md#core-group)", "Common", CORE_SUMMARY[t["name"]]) for t in CORE["tools"]]
    for g in cat:
        for t in g["tools"]:
            entries.append((t["name"], g["fName"], _group_link(g), g["folder"], TOOL_SUMMARY[t["name"]]))
    entries.sort(key=lambda e: e[0].lower())
    letters = []
    for e in entries:
        letter = e[0][0].upper()
        if letter not in letters:
            letters.append(letter)
    page.para([" · ".join("[%s](#index-%s)" % (l, l.lower()) for l in letters)])
    for letter in letters:
        page.h(3, "Index " + letter, toc=False)
        rows = [[_tool_link(folder, name), glink, "[%s](%s.md)" % (folder, folder), inline(summary, True)]
                for name, gname, glink, folder, summary in entries if name[0].upper() == letter]
        page.table(["Tool", "Group", "Page", "Summary"], rows)


def _layout(page):
    page.h(2, "Page layout")
    page.para([
        "Every page of a tool folder follows the same layout:",
        "",
        "1. **Title** — the folder and its subject, the server and the Vectorworks version, and a link back to this index.",
        "2. **Table of contents** — every group and every tool of the page.",
        "3. **Overview** — one row per group: group ID, whether it is active by default, safety level, number of tools "
        "and a one-line summary.",
        "4. **Groups** — for each group: its group ID, activation and safety level, a summary, the description that the "
        "server reports, and a table of its tools with effect, safety level and summary.",
        "5. **Tools** — for each tool: a one-line summary; its effect, safety level, undo behavior and whether it can run "
        "inside `runToolBatch`; the **Details** that the server reports; and the **Parameters** table (name, type, "
        "required, description). Members of object parameters are listed as `parameter.member`, members of array items "
        "as `parameter[].member`.",
        "",
        "Shared formats link to [Common](Common.md) and [Attributes](Attributes.md), for example "
        "[point](Common.md#points), [color](Common.md#colors) or [marker](Attributes.md#line-end-markers).",
    ])


def _statistics(page, by_folder):
    page.h(2, "Statistics")
    labels = ["Read-only", "Edit", "Interactive", "Script run"]

    def kind(t):
        label = EFFECTS[t["effect"]][0]
        return "Interactive" if label.startswith("Interactive") else label

    rows, totals = [], [0] * (3 + len(labels))
    for folder, groups in by_folder.items():
        tools = [t for g in groups for t in g["tools"]]
        params = sum(len(t["inputSchema"].get("properties") or {}) for t in tools)
        counts = [len(groups), len(tools), params] + [sum(1 for t in tools if kind(t) == l) for l in labels]
        totals = [a + b for a, b in zip(totals, counts)]
        rows.append(["[%s](%s.md)" % (folder, folder)] + [str(c) for c in counts])
    rows.append(["**Total**"] + ["**%d**" % c for c in totals])
    page.table(["Page", "Groups", "Tools", "Parameters", "Read-only", "Edit", "Interactive", "Script run"], rows)
    page.para(["Parameters counts the top-level parameters of the tools. Interactive includes the menu command tool. "
               "The [Core](Common.md#core-group) group adds %d always available meta-tools." % CORE["toolCount"]])
