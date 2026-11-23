"""Add language selectors to versioned reference pages without changing their bodies.

Translations mirror the English section folder in a sibling language folder with the same version folder names:
MCP/v2027.2/Common.md, MCP.de/v2027.2/Common.md and MCP.ja/v2027.2/Common.md are one page in three languages.
"""

import argparse
import os
import re
from pathlib import Path
from typing import Optional

LANGUAGES = (('', 'English'), ('.de', 'Deutsch'), ('.ja', '\u65e5\u672c\u8a9e'))
PAGES_WITHOUT_SELECTOR = frozenset({'AI-CONTEXT.md'})
SEPARATOR = ' \u2022 '
LABEL = '(?:' + '|'.join(re.escape(label) for _, label in LANGUAGES) + ')'
ENTRY = r'(?:\*\*' + LABEL + r'\*\*|\[' + LABEL + r'\]\([^)\r\n]+\))'
SELECTOR = re.compile(ENTRY + '(?:' + re.escape(SEPARATOR) + ENTRY + ')*')


def without_selector(text: str) -> str:
    first, _, rest = text.partition('\n')
    if not SELECTOR.fullmatch(first.rstrip('\r')):
        return text
    if rest.startswith('\r\n'):
        return rest[2:]
    return rest[1:] if rest.startswith('\n') else rest


def language_selector(folder: Path, name: str) -> str:
    section = folder.parent
    base, current = section.name, ''
    for suffix, _ in LANGUAGES[1:]:
        if base.endswith(suffix):
            base, current = base[:-len(suffix)], suffix
            break
    entries = []
    for suffix, label in LANGUAGES:
        target = section.parent / (base + suffix) / folder.name / name
        if suffix == current:
            entries.append('**' + label + '**')
        elif target.is_file():
            href = os.path.relpath(target, folder).replace(os.sep, '/')
            entries.append('[' + label + '](' + href + ')')
    return SEPARATOR.join(entries) if len(entries) > 1 else ''


def update_pages(folder: Path, published: Optional[Path] = None) -> int:
    if not folder.is_dir():
        raise NotADirectoryError(folder)
    published = (published or folder).resolve()
    changed = 0
    for page in sorted(folder.glob('*.md')):
        raw = page.read_bytes()
        if raw.startswith(b'\xef\xbb\xbf'):
            raise ValueError(str(page) + ': UTF-8 without BOM is required')
        text = raw.decode('utf-8')
        body = without_selector(text)
        selector = '' if page.name in PAGES_WITHOUT_SELECTOR else language_selector(published, page.name)
        updated = ((selector + '\n\n') if selector else '') + body
        if updated != text:
            page.write_bytes(updated.encode('utf-8'))
            changed += 1
    return changed


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folders', type=Path, nargs='+', help='version folders to update')
    parser.add_argument('--published', type=Path,
                        help='final version folder when updating one staging folder')
    args = parser.parse_args(argv)
    if args.published is not None and len(args.folders) != 1:
        parser.error('--published requires exactly one staging folder')
    for folder in args.folders:
        changed = update_pages(folder, args.published)
        print('%s: %d language selectors updated' % (folder, changed))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
