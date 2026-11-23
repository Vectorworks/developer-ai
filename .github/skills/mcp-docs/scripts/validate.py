"""Validates the generated Markdown of the MCP tool reference.

Checks: internal links and anchors resolve; tables are well formed; every page has a table of contents near the top
that lists every level 2 and 3 heading (except the letter headings of the README index); JSON code blocks parse;
code spans are closed and hold no Markdown escapes; files are UTF-8 without BOM, with LF line endings.
Translated pages are checked the same way: their table of contents and index headings may use the titles below, and
HTML anchors (<a id="...">) are link targets too, so a translated heading can keep its English anchor.

Usage: python validate.py <pages folder>
"""

import glob
import json
import os
import re
import sys

TOC_TITLES = ('Table of contents', 'Inhaltsverzeichnis', '\u76ee\u6b21')
INDEX_PREFIXES = ('Index ', '\u7d22\u5f15 ')
HTML_ANCHOR = re.compile(r'<a\s+(?:id|name)="([^"]+)"')


def gh_anchor(text):
    # GitHub: strip markdown/code formatting, lowercase, remove punctuation except '-' and spaces, spaces -> '-'
    text = re.sub(r'`([^`]*)`', r'\1', text)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = text.strip().lower()
    text = re.sub(r'[^\w\- ]', '', text, flags=re.UNICODE)
    return text.replace(' ', '-')


def headings_of(lines):
    """(level, text, anchors) of every heading outside code blocks. anchors: the GitHub anchor, with GitHub's -1, -2
    suffixes for repeats, then the ids of the HTML anchor lines directly above the heading."""
    result, counts, in_code, above = [], {}, False, []
    for line in lines:
        if line.startswith('```'):
            in_code, above = not in_code, []
            continue
        if in_code:
            continue
        m = re.match(r'^(#{1,6})\s+(.*?)\s*$', line)
        if m:
            a = gh_anchor(m.group(2))
            n = counts.get(a, 0)
            result.append((len(m.group(1)), m.group(2), [a if n == 0 else '%s-%d' % (a, n)] + above))
            counts[a] = n + 1
            above = []
        elif re.fullmatch(r'\s*(?:<a\s[^>]*>\s*</a>\s*)+', line):
            above += HTML_ANCHOR.findall(line)
        elif line.strip():
            above = []
    return result


def anchors_of(lines):
    """Every link target of a page: the heading anchors and the ids of all HTML anchors outside code."""
    result, in_code = {a for _, _, anchors in headings_of(lines) for a in anchors}, False
    for line in lines:
        if line.startswith('```'):
            in_code = not in_code
        elif not in_code:
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


def _toc(lines):
    """Anchors listed in the table of contents."""
    out, inside = set(), False
    for line in lines:
        if line.startswith('## ') and line[3:] in TOC_TITLES:
            inside = True
            continue
        if inside and line.startswith('#'):
            break
        if inside:
            m = re.match(r'^\s*- \[.*\]\(#([^)]+)\)$', line)
            if m:
                out.add(m.group(1))
    return out


def check_page(name, raw, anchors, folder=None):
    problems = []
    if raw.startswith(b'\xef\xbb\xbf'):
        problems.append('%s: starts with a byte order mark' % name)
    if b'\r' in raw:
        problems.append('%s: CR line endings (use LF)' % name)
    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError as ex:
        return ['%s: not UTF-8 (%s)' % (name, ex)]
    lines = text.split('\n')
    if not any('## ' + title in text[:6000] for title in TOC_TITLES):
        problems.append('%s: no table of contents near the top' % name)
    toc = _toc(lines)
    for level, heading, targets in headings_of(lines):
        if level in (2, 3) and heading not in TOC_TITLES and not heading.startswith(INDEX_PREFIXES) \
                and not toc.intersection(targets):
            problems.append('%s: heading "%s" is not in the table of contents' % (name, heading))
    in_code, code_lang, code_lines, code_start, header_cols = False, '', [], 0, None
    for no, line in enumerate(lines, 1):
        if line.startswith('```'):
            if not in_code:
                in_code, code_lang, code_lines, code_start = True, line[3:].strip(), [], no
            else:
                in_code = False
                if code_lang == 'json':
                    try:
                        json.loads('\n'.join(code_lines))
                    except ValueError as ex:
                        problems.append('%s:%d: JSON block does not parse (%s)' % (name, code_start, ex))
            continue
        if in_code:
            code_lines.append(line)
            continue
        # code spans: closed, and without Markdown escapes (a code span shows them literally)
        if line.replace('\\`', '').count('`') % 2:
            problems.append('%s:%d: unbalanced backticks' % (name, no))
        for span in re.findall(r'`[^`]*`', line):
            if re.search(r'&lt;|&gt;|&amp;|\\[*_]', span):
                problems.append('%s:%d: Markdown escape inside the code span %s' % (name, no, span))
        # links (code spans are not links)
        plain = re.sub(r'`[^`]*`', '', line)
        for m in re.finditer(r'(?<!\!)\[[^\]]*\]\(([^)\s]+)\)', plain):
            target = m.group(1)
            if re.match(r'^[a-z]+://', target):
                continue
            doc, _, anc = target.partition('#')
            doc = doc or name
            if doc.startswith('../') and doc not in anchors:
                if folder is None:
                    continue
                external = os.path.join(folder, doc)
                if os.path.isfile(external):
                    with open(external, encoding='utf-8') as f:
                        anchors[doc] = anchors_of(f.read().split('\n'))
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
    if in_code:
        problems.append('%s:%d: code block is not closed' % (name, code_start))
    return problems


def main(folder, published=None):
    """Checks every .md file of `folder`; returns 1 when there is a problem."""
    files = sorted(glob.glob(os.path.join(folder, '*.md')))
    raws = {os.path.basename(f): open(f, 'rb').read() for f in files}
    anchors = {n: anchors_of(r.decode('utf-8', 'replace').split('\n')) for n, r in raws.items()}
    problems = []
    links = 0
    for name, raw in raws.items():
        problems += check_page(name, raw, anchors, published or folder)
        links += len(re.findall(r'(?<!\!)\[[^\]]*\]\((?![a-z]+://)[^)\s]+\)', raw.decode('utf-8', 'replace')))
    for p in problems:
        print(p)
    print('%d files, %d links, %d problems' % (len(files), links, len(problems)))
    return 1 if problems else 0


if __name__ == '__main__':
    import argparse
    sys.dont_write_bytecode = True
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('folder', help='version folder or staging folder with the pages')
    p.add_argument('--published', help='final version folder for parent-relative links in staged pages')
    args = p.parse_args()
    sys.exit(main(args.folder, published=args.published))
