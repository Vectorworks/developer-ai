"""External wording audit: the published pages must not reveal how the module is implemented.

Default (gate): lists every hit of the STRICT patterns and of C++ type names; exit code 1 when there is any.
--broad: writes every sentence that contains a weaker signal (wrapper, node, internal, header, ...) to a report for
manual review; most of those hits are legitimate Vectorworks wording.

Usage: python audit_terms.py <pages folder> [--broad <report file>] [--all]
"""

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import collections  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402

STRICT = collections.OrderedDict([
    ('C++', r'C\+\+'),
    ('source file', r'\b[\w./-]+\.(?:h|hpp|cpp|inl|mm)\b'),
    ('source folder', r'\bPythonAPI/|\bAPI/|Source folder'),
    ('binding', r'\b[Bb]inding (?:source|framework|file|class)|Binding\.md'),
    ('SDK', r'\bg?SDK\b|\bVWFC\b|\bVCOM\b|\bIExtension\w*'),
    ('node constant', r'\bk[A-Z]\w*Node\b'),
    ('wrapper', r'\b[Ww]rap(?:per|pers|s the|ped (?:handle|object))\b'),
    ('core', r'\bCore\b'),
    ('C++ syntax', r'::|\bstd\b|\bnullptr\b|\bnullopt\b|static_cast|\w->\w+\(|\bconst\s+[`\w.]+&'),
    ('C++ types', r'\b(?:TXString|WorldCoord|WorldPt3?|ViewPt|ViewCoord|MCObjectHandle|BlankHandle|GSHandle|Sint\d+|'
                  r'Uint\d+|RefNumber|InternalIndex|VW[A-Z]\w+|CB_\w+)\b'),
    ('framework', r'\b(?:TConv|SArg|kFn|kSelfFn|kCtor|BindClass|BindEnum|DefineMembers|PublishAll|PythonProvider|'
                  r'VWObjectAPI|CScriptRunner|EScriptUndo|Switchboard)\b'),
    ('authoring', r'\bstatic analysis\b|\bheader (?:file|comment)s?\b|block-comment|\bgenerated from\b|\bnon-owning\b|'
                  r'\bdestructor\b|\bMCP\b'),
])

BROAD = collections.OrderedDict([
    ('binding', r'(?i)\bbind(?:ing|s|ed)?\b'),
    ('header', r'(?i)\bheaders?\b'),
    ('node', r'(?i)\bnodes?\b'),
    ('core', r'\bcore\b'),
    ('C/E/T prefix', r'\b[CET][A-Z][a-z]\w+'),
    ('C++ words', r'(?i)\b(?:struct|namespace|typedef|template|macro|enum|virtual|pointer|member function|throws?|'
                  r'thrown|implementation|implemented|internal|adapter|wrap\w*|dispatch\w*|underlying|double|short|'
                  r'Boolean)\b'),
])


def _pages(folder, names=None):
    for fn in sorted(os.listdir(folder)):
        if fn.endswith('.md') and (names is None or fn in names):
            with open(os.path.join(folder, fn), encoding='utf-8') as f:
                yield fn, f.read().split('\n')


def generated_pages():
    from render import FOLDER_DOCS
    return set(FOLDER_DOCS.values()) | {'README.md'}


def cpp_type_names(model):
    """C++ names of the exposed classes and enumerations whose Python name differs (CDocument, EDescend, ...)."""
    names = set()
    for q in model.classes:
        if model.py_class_name(q).split('.')[-1] != q.split('::')[-1]:
            names.add(q.split('::')[-1])
    for q in model.enums:
        if model.py_enum_name(q).split('.')[-1] != q.split('::')[-1]:
            names.add(q.split('::')[-1])
    return names


def audit(folder, cpp_names=(), names=None):
    """Prints every strict hit in the pages `names` (default: every .md file); returns their number."""
    patterns = [(k, re.compile(p)) for k, p in STRICT.items()]
    if cpp_names:
        patterns.append(('C++ type name', re.compile(r'\b(?:%s)\b' % '|'.join(sorted(map(re.escape, cpp_names))))))
    hits = 0
    for fn, lines in _pages(folder, names):
        for no, line in enumerate(lines, 1):
            for key, rx in patterns:
                for m in rx.finditer(line):
                    hits += 1
                    s = max(0, m.start() - 60)
                    print('%s:%d [%s] ...%s...' % (fn, no, key, line[s:m.end() + 60]))
    print('%d wording hits' % hits)
    return hits


def broad_report(folder, path, names=None):
    """Writes each distinct sentence with a weaker signal, grouped by category; returns the number of sentences."""
    found = collections.OrderedDict()
    for fn, lines in _pages(folder, names):
        for no, line in enumerate(lines, 1):
            cells = [c.strip() for c in line.split(' | ')] if line.startswith('|') else [line.strip()]
            for cell in cells:
                for sent in re.split(r'(?<=[.;:])\s+(?=[A-Z`"(])', cell):
                    for key, pat in BROAD.items():
                        if re.search(pat, sent):
                            found.setdefault((key, sent[:400]), []).append('%s:%d' % (fn, no))
    with open(path, 'w', encoding='utf-8') as f:
        for (key, sent), locs in sorted(found.items(), key=lambda kv: kv[0][0]):
            more = ' +%d' % (len(locs) - 1) if len(locs) > 1 else ''
            f.write('[%s] (%s%s) %s\n' % (key, locs[0], more, sent))
    print('%d sentences for manual review in %s' % (len(found), path))
    return len(found)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('pages', help='version folder or staging folder with the pages')
    p.add_argument('--broad', metavar='REPORT', help='also write the broad review report to this file')
    p.add_argument('--all', action='store_true', help='check every .md file, not only the generated pages '
                                                      '(hand-maintained files such as AI-CONTEXT.md included)')
    a = p.parse_args()
    only = None if a.all else generated_pages()
    if a.broad:
        broad_report(a.pages, a.broad, only)
    sys.exit(1 if audit(a.pages, names=only) else 0)
