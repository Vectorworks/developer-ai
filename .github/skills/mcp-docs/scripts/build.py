"""Builds the MCP tool reference of one Vectorworks version and checks it.

1. extracts the catalog of the tool groups from the source tree (extract.py), or reads it from --catalog,
2. checks that every folder, group and tool has its hand-written text (summaries.py),
3. renders every page into a staging folder (never into the repository directly),
4. checks links, anchors, tables, tables of contents and code (validate.py), coverage of every group, tool and
   parameter (coverage.py), the external wording (audit_terms.py) and, with --live, the running server (live.py),
5. unless --check-only: copies the pages into --out; other files there are left alone.

Example:
  python build.py --source "<tree>/Interfaces/VectorWorks" --version "Vectorworks 2027 Update 2" --out MCP/v2027.2
"""

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import filecmp  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import tempfile  # noqa: E402

import audit_terms  # noqa: E402
import coverage  # noqa: E402
import extract  # noqa: E402
import render  # noqa: E402
import validate  # noqa: E402


def main(argv=None):
    p = argparse.ArgumentParser(description='Build and check the MCP tool reference of one Vectorworks version.')
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument('--source',
                     help='Interfaces/VectorWorks folder of the Vectorworks source tree of the documented version '
                          '(contains MCP/ and API/)')
    src.add_argument('--catalog', help='a catalog.json written by extract.py, instead of --source')
    p.add_argument('--version', required=True, dest='version_label',
                   help='version label shown on every page, for example "Vectorworks 2027 Update 2"')
    p.add_argument('--out', required=True, help='version folder of the reference, for example MCP/v2027.2')
    p.add_argument('--work', default=os.path.join(tempfile.gettempdir(), 'mcp-docs-build'),
                   help='staging folder, recreated on every run (default: %(default)s)')
    p.add_argument('--check-only', action='store_true', help='build and check, but do not copy into --out')
    p.add_argument('--live', nargs='?', const=None, default=False, metavar='URL',
                   help='also compare the catalog with a running Vectorworks MCP server (read-only; default URL %s)'
                        % 'http://localhost:8765')
    args = p.parse_args(argv)

    work = os.path.abspath(args.work)
    if os.path.isdir(work):
        shutil.rmtree(work)
    os.makedirs(work)
    catalog_path = os.path.join(work, 'catalog.json')

    if args.source:
        source = os.path.abspath(args.source)
        for need in ('MCP', os.path.join('API', 'Resources')):
            if not os.path.isdir(os.path.join(source, need)):
                p.error('%s not found in %s: --source must be the Interfaces/VectorWorks folder' % (need, source))
        cat, errors = extract.extract(source)
        if errors:
            print('\n'.join('Cannot evaluate %s' % e for e in errors))
            print('\nFAILED: extraction. Nothing copied. Extend extract.py for the new construct.')
            return 1
    else:
        with open(args.catalog, encoding='utf-8') as f:
            cat = json.load(f)
    with open(catalog_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(cat, f, indent=1, ensure_ascii=False)
    print('Catalog: %d groups, %d tools (%s)' % (len(cat), sum(len(g['tools']) for g in cat), catalog_path))

    missing = render.precheck(cat)
    if missing:
        print('\n'.join(missing))
        print('\nFAILED: hand-written texts missing (summaries.py). Nothing copied.')
        return 1

    pages = os.path.join(work, 'pages')
    written = render.write_all(cat, pages, args.version_label)
    print('Rendered %d pages into %s' % (len(written), pages))
    language_script = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts', 'doc_languages.py')
    subprocess.run([sys.executable, language_script, pages, '--published', args.out], check=True)

    failures = []
    print('\n== Links, anchors, tables, tables of contents, code')
    if validate.main(pages, published=args.out):
        failures.append('validate')
    print('\n== Coverage of groups, tools and parameters')
    if coverage.check(cat, pages):
        failures.append('coverage')
    print('\n== External wording')
    if audit_terms.audit(pages, audit_terms.internal_names(cat)):
        failures.append('wording')
    if args.live is not False:
        import live
        print('\n== Running server')
        if live.check(cat, args.live or live.DEFAULT_URL):
            failures.append('live')

    notes = render.review(cat)
    broad = os.path.join(work, 'broad.txt')
    print('\n== Review (not failures)')
    for note in notes:
        print('  ' + note)
    print('  %d hand-written texts to review' % len(notes))
    audit_terms.broad_report(pages, broad)

    if failures:
        print('\nFAILED: %s. Nothing copied.' % ', '.join(failures))
        return 1
    if args.check_only:
        print('\nAll checks passed. Nothing copied (--check-only).')
        return 0
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    changed = 0
    for name in written:
        source_page, target = os.path.join(pages, name), os.path.join(out, name)
        if not os.path.exists(target) or not filecmp.cmp(source_page, target, shallow=False):
            changed += 1
        shutil.copyfile(source_page, target)
    print('\nAll checks passed. Copied %d pages into %s (%d changed)' % (len(written), out, changed))
    others = sorted(set(os.listdir(out)) - set(written))
    if others:
        print('Left untouched there: %s' % ', '.join(others))
    return 0


if __name__ == '__main__':
    sys.exit(main())
