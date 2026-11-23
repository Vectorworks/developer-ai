"""Validates the generated Markdown: internal links/anchors resolve, tables are well formed, every page has a TOC.

Translated pages are checked the same way: their table of contents may use the titles below, and HTML anchors
(<a id="...">) are link targets too, so a translated heading can keep its English anchor.
"""

import glob
import os
import re
import sys

TOC_TITLES = ('Table of contents', 'Inhaltsverzeichnis', '\u76ee\u6b21')
HTML_ANCHOR = re.compile(r'<a\s+(?:id|name)="([^"]+)"')


def gh_anchor(text):
    # GitHub: strip markdown/code formatting, lowercase, remove punctuation except '-' and spaces, spaces -> '-'
    text = re.sub(r'`([^`]*)`', r'\1', text)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = text.strip().lower()
    text = re.sub(r'[^\w\- ]', '', text, flags=re.UNICODE)
    return text.replace(' ', '-')


def anchors_of(path):
    result = set()
    counts = {}
    in_code = False
    for line in open(path, encoding='utf-8'):
        if line.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r'^(#{1,6})\s+(.*?)\s*$', line)
        if m:
            a = gh_anchor(m.group(2))
            n = counts.get(a, 0)
            result.add(a if n == 0 else '%s-%d' % (a, n))
            counts[a] = n + 1
        else:
            result.update(HTML_ANCHOR.findall(re.sub(r'`[^`]*`', '', line)))
    return result


def split_cells(line):
    # split a table row on unescaped pipes outside code spans
    cells, cur, in_code, i = [], '', False, 0
    s = line.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|') and not s.endswith('\\|'):
        s = s[:-1]
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s) and s[i + 1] == '|':
            cur += '\\|'
            i += 2
            continue
        if c == '`':
            in_code = not in_code
        if c == '|' and not in_code:
            cells.append(cur)
            cur = ''
        else:
            cur += c
        i += 1
    cells.append(cur)
    return cells


def main(folder, names=None, published=None):
    """Checks the pages `names` of `folder` (default: every .md file); links may point to any .md file there."""
    files = sorted(glob.glob(os.path.join(folder, '*.md')))
    anchors = {os.path.basename(f): anchors_of(f) for f in files}
    if names is not None:
        files = [f for f in files if os.path.basename(f) in names]
    problems = []
    for f in files:
        name = os.path.basename(f)
        text = open(f, encoding='utf-8').read()
        if not any('## ' + title in text[:6000] for title in TOC_TITLES):
            problems.append('%s: no table of contents near the top' % name)
        in_code = False
        header_cols = None
        for no, line in enumerate(text.split('\n'), 1):
            if line.startswith('```'):
                in_code = not in_code
                continue
            if in_code:
                continue
            # links (code spans are not links)
            plain = re.sub(r'`[^`]*`', '', line)
            for m in re.finditer(r'(?<!\!)\[[^\]]*\]\(([^)\s]+)\)', plain):
                target = m.group(1)
                if re.match(r'^[a-z]+://', target):
                    continue
                doc, _, anc = target.partition('#')
                doc = doc or name
                if (doc.startswith('../') or doc == 'AI-CONTEXT.md') and doc not in anchors:
                    external = os.path.join(published or folder, doc)
                    if os.path.isfile(external):
                        anchors[doc] = anchors_of(external)
                if doc not in anchors:
                    problems.append('%s:%d: missing file %s' % (name, no, doc))
                elif anc and anc not in anchors[doc]:
                    problems.append('%s:%d: missing anchor %s#%s' % (name, no, doc, anc))
            # tables
            if line.startswith('|'):
                cells = split_cells(line)
                if re.match(r'^\|(\s*:?-+:?\s*\|)+\s*$', line):
                    continue
                if header_cols is None:
                    header_cols = len(cells)
                elif len(cells) != header_cols:
                    problems.append('%s:%d: %d cells, header has %d' % (name, no, len(cells), header_cols))
            else:
                header_cols = None
    for p in problems:
        print(p)
    print('%d files, %d problems' % (len(files), len(problems)))
    return 1 if problems else 0


if __name__ == '__main__':
    import argparse
    sys.dont_write_bytecode = True
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('folder', help='version folder or staging folder with the pages')
    p.add_argument('--published', help='final version folder for parent-relative links in staged pages')
    p.add_argument('--all', action='store_true', help='check every .md file, not only the generated pages '
                                                      '(hand-maintained files such as AI-CONTEXT.md included)')
    a = p.parse_args()
    if a.all:
        sys.exit(main(a.folder, published=a.published))
    from render import FOLDER_DOCS
    sys.exit(main(a.folder, set(FOLDER_DOCS.values()) | {'README.md'}, published=a.published))
