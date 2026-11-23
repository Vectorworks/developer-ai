"""External wording audit: the published MCP pages must not reveal how the server is implemented.

Default (gate): lists every hit of the STRICT patterns and of the internal names from the catalog (group classes and
source file names); exit code 1 when there is any.
--broad: writes every sentence that contains a weaker signal (core, SDK, internal, ...) to a report for manual review;
most of those hits are legitimate wording ("Core" is the name of the meta-tool group, "SDK plug-in" is a kind of
Vectorworks tool, "core component" is a slab component).

Usage: python audit_terms.py <pages folder> [--catalog <catalog.json>] [--broad <report file>]
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
    ('source folder', r'AppSource|CoreVectorScript|DSTOP|Interfaces/VectorWorks|\bsource (?:code|files?|tree)\b'),
    ('binding', r'\b[Bb]inding'),
    ('class name', r'\bC?MCP[A-Z0-9]\w*|\bMCPTools\b'),
    ('effect name', r'\bE?ToolEffect\b|\bOwnUndo\w*|\bRunsScript\b|\bMediumRisk\b|\bHighRisk\b|\bReadOnly\b'),
    ('SDK', r'\bgSDK\b|\bVCOM\b|\bIExtension\w*|\bVWObjectAPI\b'),
    ('C++ syntax', r'::|\bstd\b|\bnullptr\b|static_cast|\bnlohmann\b'),
    ('C++ types', r'\b(?:TXString|MCObjectHandle|WorldCoord|WorldPt3?|Sint\d+|Uint\d+|InternalIndex)\b'),
    ('authoring', r'(?i)\bhandlers?\b|\bimplementation\b|\bcore tools?\b|\bDefineGroup\b|\bAddTool\b'),
])

BROAD = collections.OrderedDict([
    ('core', r'(?i)\bcore\b'),
    ('SDK', r'\bSDK\b'),
    ('internal', r'(?i)\binternal(?:ly)?\b'),
    ('C++ words', r'(?i)\b(?:struct|namespace|typedef|template|macro|enum|virtual|pointer|callback|lambda|'
                  r'implemented|dispatch\w*|underlying|registry|register(?:ed|s)?)\b'),
])


def _pages(folder):
    for fn in sorted(os.listdir(folder)):
        if fn.endswith('.md'):
            with open(os.path.join(folder, fn), encoding='utf-8') as f:
                yield fn, f.read().split('\n')


def internal_names(cat):
    """Names that exist only in the source: the group classes and the source file names."""
    names = set()
    for g in cat:
        names.add(g['class'])
        for t in g['tools']:
            for f in (t.get('file'), t.get('handlerFile')):
                if f:
                    base = os.path.basename(f)
                    names.update((base, os.path.splitext(base)[0]))
    return names


def audit(folder, names=()):
    """Prints every strict hit in the pages of `folder`; returns their number."""
    patterns = [(k, re.compile(p)) for k, p in STRICT.items()]
    if names:
        patterns.append(('internal name', re.compile(r'\b(?:%s)\b' % '|'.join(sorted(map(re.escape, names))))))
    hits = 0
    for fn, lines in _pages(folder):
        for no, line in enumerate(lines, 1):
            for key, rx in patterns:
                for m in rx.finditer(line):
                    hits += 1
                    s = max(0, m.start() - 60)
                    print('%s:%d [%s] ...%s...' % (fn, no, key, line[s:m.end() + 60]))
    print('%d wording hits' % hits)
    return hits


def broad_report(folder, path):
    """Writes each distinct sentence with a weaker signal, grouped by category; returns the number of sentences."""
    found = collections.OrderedDict()
    for fn, lines in _pages(folder):
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
    import json
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('pages', help='version folder or staging folder with the pages')
    p.add_argument('--catalog', help='catalog.json of the version: also flags its class and source file names')
    p.add_argument('--broad', metavar='REPORT', help='also write the broad review report to this file')
    a = p.parse_args()
    extra = internal_names(json.load(open(a.catalog, encoding='utf-8'))) if a.catalog else ()
    if a.broad:
        broad_report(a.pages, a.broad)
    sys.exit(1 if audit(a.pages, extra) else 0)
