"""Coverage of the MCP tool reference: every group, tool and parameter of the catalog is documented.

Checks that each group has its section on the page of its folder, each tool its section (### name, anchor
name.lower()) and its Parameters table with every parameter path (name, name.member, name[].member), and that the
README lists every group and tool.

Usage: python coverage.py <catalog.json> <pages folder>
"""

import sys

sys.dont_write_bytecode = True

import os  # noqa: E402
import re  # noqa: E402

import render  # noqa: E402
from mdlib import slug  # noqa: E402


def _sections(lines):
    """### heading -> its lines up to the next level 2 or 3 heading."""
    out, cur = {}, None
    for line in lines:
        m = re.match(r'^(#{2,3}) (.*)$', line)
        if m:
            cur = m.group(2) if len(m.group(1)) == 3 else None
            if cur is not None:
                out.setdefault(cur, [])
            continue
        if cur is not None:
            out[cur].append(line)
    return out


def check(cat, folder):
    """Prints every gap; returns their number."""
    problems = []
    readme = open(os.path.join(folder, 'README.md'), encoding='utf-8').read()
    tools = params = 0
    for name, groups in render.by_folder(cat).items():
        path = os.path.join(folder, name + '.md')
        if not os.path.exists(path):
            problems.append('%s.md: missing page' % name)
            continue
        lines = open(path, encoding='utf-8').read().split('\n')
        headings2 = {l[3:] for l in lines if l.startswith('## ')}
        sections = _sections(lines)
        for g in groups:
            if g['fName'] not in headings2:
                problems.append('%s.md: no section for the group %s' % (name, g['fName']))
            if '(%s.md#%s)' % (name, slug(g['fName'])) not in readme:
                problems.append('README.md: no link to the group %s' % g['fName'])
            for t in g['tools']:
                tools += 1
                body = sections.get(t['name'])
                if body is None:
                    problems.append('%s.md: no section for the tool %s' % (name, t['name']))
                    continue
                if '(%s.md#%s)' % (name, t['name'].lower()) not in readme:
                    problems.append('README.md: no link to the tool %s' % t['name'])
                table = {re.match(r'^\| `([^`]+)` \|', l).group(1) for l in body if re.match(r'^\| `[^`]+` \|', l)}
                for p in render.schema_paths(t['inputSchema']):
                    params += 1
                    if p not in table:
                        problems.append('%s.md: %s: parameter %s is not in the table' % (name, t['name'], p))
    for p in problems:
        print(p)
    print('%d groups, %d tools, %d parameter rows checked, %d gaps' % (len(cat), tools, params, len(problems)))
    return len(problems)


if __name__ == '__main__':
    import json
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(1 if check(json.load(open(sys.argv[1], encoding='utf-8')), sys.argv[2]) else 0)
