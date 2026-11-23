"""Coverage check: every class, enumeration and member exposed to Python is documented on its page.

Usage: python coverage.py --source <Interfaces/VectorWorks folder> --pages <folder with the generated pages>
"""

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import collections  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402

from render import Docs, FOLDER_DOCS, esc  # noqa: E402


def _section(text, py):
    m = re.search(r'^#{3,4} %s$' % re.escape(py), text, re.M)
    if not m:
        return None
    nxt = re.search(r'^#{2,4} ', text[m.end():], re.M)
    return text[m.end(): m.end() + (nxt.start() if nxt else len(text) - m.end())]


def check(docs, pages_dir):
    """Prints the counts and every undocumented item; returns the number of missing items."""
    pages = {}
    for doc in FOLDER_DOCS.values():
        with open(os.path.join(pages_dir, doc), encoding='utf-8') as f:
            pages[doc] = f.read()
    cnt = collections.Counter()
    missing = []
    for info in docs.cls_info.values():
        sec = _section(pages[FOLDER_DOCS[info['folder']]], info['py'])
        if sec is None:
            missing.append(('class', info['py']))
            continue
        cnt['classes'] += 1
        short = info['qualname'].split('.')[-1]
        for r in info['members']:
            if r.kind == 'Def':
                cnt['method signatures'] += 1
                ok = ('`%s`' % esc(docs.signature(r.name, r.params, r.ret, r.file))) in sec
            elif r.kind == 'Init':
                cnt['constructors'] += 1
                ok = ('`%s(' % short) in sec
            elif r.kind == 'Field':
                cnt['fields'] += 1
                ok = ('| `%s` |' % r.name) in sec
            elif r.kind == 'Constant':
                cnt['class constants'] += 1
                ok = ('.%s` |' % r.name) in sec
            else:
                ok = True
            if not ok:
                missing.append((r.kind, info['py'], r.name))
    for info in docs.enum_info.values():
        sec = _section(pages[FOLDER_DOCS[info['folder']]], info['py'])
        if sec is None:
            missing.append(('enum', info['py']))
            continue
        cnt['enumerations'] += 1
        for v in info['values']:
            cnt['enum members'] += 1
            if ('| `%s` |' % v['name']) not in sec:
                missing.append(('enum member', info['py'], v['name']))
    for folder, rs in docs.module_members.items():
        text = pages[FOLDER_DOCS[folder]]
        for r in rs:
            if r.kind == 'Def':
                cnt['module functions'] += 1
                if ('`%s`' % esc(docs.signature(r.name, r.params, r.ret, r.file))) not in text:
                    missing.append(('module function', folder, r.name))
            elif r.kind == 'Constant':
                cnt['module constants'] += 1
                if ('`%s`' % r.name) not in text:
                    missing.append(('module constant', folder, r.name))
    print(', '.join('%s %d' % kv for kv in cnt.items()))
    for item in missing:
        print('MISSING', ' '.join(item))
    print('%d missing' % len(missing))
    return len(missing)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('--source', required=True, help='Interfaces/VectorWorks folder of the Vectorworks source tree')
    p.add_argument('--pages', required=True, help='folder with the generated pages')
    a = p.parse_args()
    sys.exit(1 if check(Docs(a.source, a.pages, ''), a.pages) else 0)
