"""Builds the Python API reference pages of one Vectorworks version and checks them.

1. renders every page into a staging folder (never into the repository directly),
2. checks links, anchors, tables and tables of contents (validate.py), coverage of every exposed class and member
   (coverage.py) and the external wording (audit_terms.py),
3. unless --check-only: copies the pages into --out; other files there (AI-CONTEXT.md, ...) are left alone.

Example:
  python build.py --source "<tree>/Interfaces/VectorWorks" --version "Vectorworks 2027 Update 2" --out PythonAPI/v2027.2
"""

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import collections  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import tempfile  # noqa: E402

import audit_terms  # noqa: E402
import coverage  # noqa: E402
import render  # noqa: E402
import validate  # noqa: E402

REVIEW_KINDS = {
    'missing': 'methods without any description',
    'field': 'fields described from their name only',
    'constant': 'constants without a description',
    'ctor': 'constructors described from their parameters only',
    'auto-weak': 'methods described from their name only',
    'auto-is': 'Is/Has/Can methods described from their name',
    'auto+trail': 'methods described from their name and a trailing comment',
    'trail-only': 'methods described by a trailing comment only',
    'group-other': 'methods described by the comment of their group',
}


def main(argv=None):
    p = argparse.ArgumentParser(description='Build and check the Python API reference of one Vectorworks version.')
    p.add_argument('--source', required=True,
                   help='Interfaces/VectorWorks folder of the Vectorworks source tree of the documented version '
                        '(contains PythonProvider.cpp, API/ and PythonAPI/)')
    p.add_argument('--version', required=True, dest='version_label',
                   help='version label shown on every page, for example "Vectorworks 2027 Update 2"')
    p.add_argument('--out', required=True, help='version folder of the reference, for example PythonAPI/v2027.2')
    p.add_argument('--work', default=os.path.join(tempfile.gettempdir(), 'pythonapi-docs-build'),
                   help='staging folder, recreated on every run (default: %(default)s)')
    p.add_argument('--check-only', action='store_true', help='build and check, but do not copy into --out')
    args = p.parse_args(argv)

    source = os.path.abspath(args.source)
    for need in ('PythonProvider.cpp', 'API', 'PythonAPI'):
        if not os.path.exists(os.path.join(source, need)):
            p.error('%s not found in %s: --source must be the Interfaces/VectorWorks folder' % (need, source))
    work = os.path.abspath(args.work)
    if os.path.isdir(work):
        shutil.rmtree(work)
    pages = os.path.join(work, 'pages')

    docs = render.Docs(source, pages, args.version_label)
    written = docs.write_all()
    print('Rendered %d pages into %s' % (len(written), pages))
    language_script = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts', 'doc_languages.py')
    subprocess.run([sys.executable, language_script, pages, '--published', args.out], check=True)

    failures = []
    print('\n== Links, anchors, tables, tables of contents')
    if validate.main(pages, published=args.out):
        failures.append('validate')
    print('\n== Coverage of classes, enumerations and members')
    if coverage.check(docs, pages):
        failures.append('coverage')
    print('\n== External wording')
    if audit_terms.audit(pages, audit_terms.cpp_type_names(docs.model)):
        failures.append('wording')

    # review items: not failures, but candidates for curated descriptions in overrides_data.py
    unused = sorted(set(docs.desc.overrides) - docs.desc.used_overrides)
    kinds = collections.Counter(k for _, _, k in docs.desc.review)
    review = {
        'weakly_described': [{'key': k, 'text': t, 'kind': kind} for k, t, kind in docs.desc.review],
        'unused_overrides': unused,
        'resolve_notes': list(docs.problems) + sorted(set(docs.model.problems)),
        'dropped_code_lines': ['%s: %s' % x for x in render.CODE_LINES],
        'notes': docs.notes,
    }
    review_path = os.path.join(work, 'review.json')
    with open(review_path, 'w', encoding='utf-8') as f:
        json.dump(review, f, indent=1, ensure_ascii=False)
    print('\n== Review (not failures; details in %s)' % review_path)
    for kind, n in sorted(kinds.items()):
        print('  %4d %s' % (n, REVIEW_KINDS.get(kind, kind)))
    print('  %4d unused overrides%s' % (len(unused), (': ' + ', '.join(unused[:10])) if unused else ''))
    for note in review['resolve_notes'] + docs.notes:
        print('  note: %s' % note)

    if failures:
        print('\nFAILED: %s. Nothing copied.' % ', '.join(failures))
        return 1
    if args.check_only:
        print('\nAll checks passed. Nothing copied (--check-only).')
        return 0
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    for name in written:
        shutil.copyfile(os.path.join(pages, name), os.path.join(out, name))
    print('\nAll checks passed. Copied %d pages into %s' % (len(written), out))
    others = sorted(set(os.listdir(out)) - set(written))
    if others:
        print('Left untouched there: %s' % ', '.join(others))
    return 0


if __name__ == '__main__':
    sys.exit(main())
