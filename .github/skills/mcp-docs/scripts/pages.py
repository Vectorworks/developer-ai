# Writes one page per tool folder.
import summaries
from mdlib import EFFECTS, Page, block, clean, code, implicit_notes, inline, schema_rows, tool_safety
from paramnotes import param_notes, tool_overrides
from summaries import FOLDERS, GROUP_SUMMARY, TOOL_SUMMARY


def header():
    return "> **Server:** Vectorworks MCP · **Version:** %s" % summaries.VERSION


def yes_no(b):
    return "Yes" if b else "No"


def folder_page(folder, groups):
    tagline, intro = FOLDERS[folder]
    page = Page("%s — %s" % (folder, tagline), header(), [inline(intro), ""])

    total = sum(len(g["tools"]) for g in groups)
    page.h(2, "Overview")
    page.para(["This folder holds %d tool group%s with %d tools in total." % (len(groups), "" if len(groups) == 1 else "s", total)])
    rows = []
    for g in groups:
        rows.append(["[%s](#%s)" % (g["fName"], _peek(page, g["fName"])), code(g["groupId"], True), yes_no(g["fActiveByDefault"]),
                     g["fSafetyLevel"], str(len(g["tools"])), inline(GROUP_SUMMARY[g["fName"]], True)])
    page.table(["Group", "Group ID", "Active by default", "Safety level", "Tools", "Summary"], rows)

    for g in groups:
        group_section(page, g)
    return page.render()


def _peek(page, text):
    """The anchor the next heading 'text' will get."""
    from mdlib import slug
    base = slug(text)
    n = page.used.get(base, 0)
    return base if n == 0 else "%s-%d" % (base, n)


def group_section(page, g):
    page.h(2, g["fName"])
    page.para(["> **Group:** %s · **Group ID:** %s · **Active by default:** %s · **Safety level:** %s · **Tools:** %d"
               % (code(g["fName"]), code(g["groupId"]), yes_no(g["fActiveByDefault"]), g["fSafetyLevel"], len(g["tools"]))])
    page.para(["**" + inline(GROUP_SUMMARY[g["fName"]]) + "**"])
    page.para(block(g["fDesc"]))

    rows = []
    for t in g["tools"]:
        label = EFFECTS[t["effect"]][0]
        rows.append(["[%s](#%s)" % (code(t["name"]), t["name"].lower()), label,
                     tool_safety(t["effect"], g["fSafetyLevel"]), inline(TOOL_SUMMARY[t["name"]], True)])
    page.table(["Tool", "Effect", "Safety", "Summary"], rows)

    for t in g["tools"]:
        tool_section(page, g, t)


def tool_section(page, g, t):
    anchor = page.h(3, t["name"])
    assert anchor == t["name"].lower(), (anchor, t["name"])
    label, undo, batch = EFFECTS[t["effect"]]
    page.para([inline(TOOL_SUMMARY[t["name"]])])
    page.para(["> **Effect:** %s · **Safety:** %s · **Undo:** %s · **In runToolBatch:** %s"
               % (label, tool_safety(t["effect"], g["fSafetyLevel"]), inline(undo.format(tool=t["name"])), batch)])
    page.para(["**Details**"])
    page.para(block(t["description"]))
    page.para(["**Parameters**"])
    schema = t["inputSchema"]
    notes = param_notes(g["fName"], t)
    implicit = implicit_notes(schema)
    for p in tool_overrides(t["name"]):
        implicit.pop(p, None)
    notes.update(implicit)
    rows = list(schema_rows(schema, notes))
    if rows:
        page.table(["Parameter", "Type", "Required", "Description"], rows)
    else:
        page.para(["This tool takes no parameters."])
