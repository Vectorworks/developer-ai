"""Renders the Markdown pages of the MCP tool reference from a catalog (see extract.py).

One page per tool folder (pages.py), the shared pages Common.md and Attributes.md (shared.py) and the index README.md
(readme.py). The hand-written texts are in summaries.py, paramnotes.py and shared.py.
"""

import collections
import os

import mdlib
import paramnotes
import summaries

SHARED_PAGES = ['Common', 'Attributes']


def by_folder(cat):
    """folder -> its groups, in catalog order."""
    folders = collections.OrderedDict()
    for g in cat:
        folders.setdefault(g['folder'], []).append(g)
    return folders


def page_names(cat):
    return [f + '.md' for f in by_folder(cat)] + [p + '.md' for p in SHARED_PAGES] + ['README.md']


def schema_paths(schema):
    """Every parameter path of a schema as the Parameters table shows it (name, name.member, name[].member)."""
    return [row[0][1:-1] for row in mdlib.schema_rows(schema)]


def precheck(cat):
    """Errors that would stop the rendering or leave a page incomplete: catalog entries without a hand-written text."""
    errors = []
    folders = by_folder(cat)
    categorized = [f for _, _, fs in summaries.CATEGORIES for f in fs]
    for folder in folders:
        if folder in SHARED_PAGES or folder == 'README':
            errors.append('tool folder %r has the name of a shared page' % folder)
        if folder not in summaries.FOLDERS:
            errors.append('summaries.FOLDERS: no entry for the folder %r' % folder)
        if folder not in categorized:
            errors.append('summaries.CATEGORIES: the folder %r is in no category' % folder)
    for folder in SHARED_PAGES:
        if folder not in categorized:
            errors.append('summaries.CATEGORIES: the shared page %r is in no category' % folder)
    for folder in categorized:
        if folder not in folders and folder not in SHARED_PAGES:
            errors.append('summaries.CATEGORIES: %r is no tool folder any more' % folder)
    names = collections.Counter()
    for g in cat:
        if g['fName'] not in summaries.GROUP_SUMMARY:
            errors.append('summaries.GROUP_SUMMARY: no entry for the group %r' % g['fName'])
        for t in g['tools']:
            names[t['name']] += 1
            if t['name'] not in summaries.TOOL_SUMMARY:
                errors.append('summaries.TOOL_SUMMARY: no entry for the tool %r (group %s)' % (t['name'], g['fName']))
            if t['effect'] not in mdlib.EFFECTS:
                errors.append('mdlib.EFFECTS: unknown effect %r of the tool %r' % (t['effect'], t['name']))
    for name, n in names.items():
        if n > 1:
            errors.append('the tool name %r is defined %d times' % (name, n))
    return errors


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from _strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from _strings(v)


def review(cat):
    """Hand-written texts that no longer match the catalog: not failures, but candidates for clean-up."""
    from shared import CORE
    notes = []
    groups = {g['fName'] for g in cat}
    tools = {t['name']: t for g in cat for t in g['tools']}
    folders = set(by_folder(cat)) | set(SHARED_PAGES)
    for key in sorted(set(summaries.FOLDERS) - folders):
        notes.append('summaries.FOLDERS: unused entry %r' % key)
    for key in sorted(set(summaries.GROUP_SUMMARY) - groups):
        notes.append('summaries.GROUP_SUMMARY: unused entry %r' % key)
    for key in sorted(set(summaries.TOOL_SUMMARY) - set(tools)):
        notes.append('summaries.TOOL_SUMMARY: unused entry %r' % key)
    for table in ('TOOL', 'DROP'):
        for tool, path in sorted(getattr(paramnotes, table)):
            if tool not in tools:
                notes.append('paramnotes.%s: unknown tool %r' % (table, tool))
            elif path not in schema_paths(tools[tool]['inputSchema']):
                notes.append('paramnotes.%s: %r has no parameter %r' % (table, tool, path))
    for table in ('_TEXT_TOOLS', '_ATTRIBUTE_TOOLS'):
        for tool in sorted(getattr(paramnotes, table) - set(tools)):
            notes.append('paramnotes.%s: unknown tool %r' % (table, tool))
    texts = list(_strings(cat)) + list(_strings(CORE))
    for old, _ in summaries.REPLACEMENTS:
        if not any(old in s for s in texts):
            notes.append('summaries.REPLACEMENTS: %r occurs in no text any more' % old)
    return notes


def write_all(cat, out, version):
    """Writes every page into the folder `out`; returns the page names."""
    from pages import folder_page
    from readme import readme
    from shared import attributes_page, common_page
    if not version:
        raise ValueError('a version label is required, for example "Vectorworks 2027 Update 2"')
    summaries.VERSION = version
    os.makedirs(out, exist_ok=True)
    folders = by_folder(cat)
    pages = collections.OrderedDict()
    for folder, groups in folders.items():
        pages[folder + '.md'] = folder_page(folder, groups)
    pages['Common.md'] = common_page(cat)
    pages['Attributes.md'] = attributes_page(cat)
    pages['README.md'] = readme(cat, folders)
    for name, text in pages.items():
        with open(os.path.join(out, name), 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
    return list(pages)
