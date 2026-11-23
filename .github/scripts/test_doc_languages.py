import contextlib
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from doc_languages import update_pages, without_selector

GITHUB = Path(__file__).resolve().parents[1]
BODY = '# Page\n\n## Table of contents\n\n- [Topic](#topic)\n\n## Topic\n\nText.\n'


def load_validator(skill):
    path = GITHUB / 'skills' / skill / 'scripts' / 'validate.py'
    spec = importlib.util.spec_from_file_location(skill.replace('-', '_') + '_validate', path)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load validator: ' + str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LanguageSelectorTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='doc-languages-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def page(self, folder, name='Page.md', body=BODY):
        path = self.root / folder / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body.encode('utf-8'))
        return path

    def test_matching_pages_in_all_languages_and_idempotence(self):
        en = self.page('MCP/v2027.2')
        de = self.page('MCP.de/v2027.2')
        ja = self.page('MCP.ja/v2027.2')
        expected = {
            en: '**English** \u2022 [Deutsch](../../MCP.de/v2027.2/Page.md) \u2022 '
                '[\u65e5\u672c\u8a9e](../../MCP.ja/v2027.2/Page.md)',
            de: '[English](../../MCP/v2027.2/Page.md) \u2022 **Deutsch** \u2022 '
                '[\u65e5\u672c\u8a9e](../../MCP.ja/v2027.2/Page.md)',
            ja: '[English](../../MCP/v2027.2/Page.md) \u2022 [Deutsch](../../MCP.de/v2027.2/Page.md) \u2022 '
                '**\u65e5\u672c\u8a9e**',
        }
        for path, selector in expected.items():
            with self.subTest(language=path.parent.parent.name):
                self.assertEqual(update_pages(path.parent), 1)
                self.assertEqual(path.read_bytes(), (selector + '\n\n' + BODY).encode('utf-8'))
                self.assertEqual(update_pages(path.parent), 0)

    def test_only_existing_same_name_counterparts_are_linked(self):
        en = self.page('MCP/v2027.2')
        self.page('MCP.de/v2027.2', name='Other.md')
        self.page('MCP.ja/v2027.1')
        self.page('PythonAPI.ja/v2027.2')
        self.assertEqual(update_pages(en.parent), 0)
        self.assertEqual(en.read_bytes(), BODY.encode('utf-8'))
        self.page('MCP.de/v2027.2')
        self.assertEqual(update_pages(en.parent), 1)
        self.assertEqual(en.read_text(encoding='utf-8').splitlines()[0],
                         '**English** \u2022 [Deutsch](../../MCP.de/v2027.2/Page.md)')

    def test_obsolete_selector_is_removed_without_changing_body(self):
        selector = '**English** \u2022 [Deutsch](../../MCP.de/v2027.2/Page.md)'
        en = self.page('MCP/v2027.2', body=selector + '\n\n' + BODY)
        self.assertEqual(update_pages(en.parent), 1)
        self.assertEqual(en.read_bytes(), BODY.encode('utf-8'))
        self.assertEqual(without_selector('[English](guide.md) is a topic.\n'),
                         '[English](guide.md) is a topic.\n')

    def test_ai_context_never_gets_a_selector(self):
        selector = '**English** \u2022 [Deutsch](../../PythonAPI.de/v2027.2/AI-CONTEXT.md)'
        en = self.page('PythonAPI/v2027.2', 'AI-CONTEXT.md', body=selector + '\n\n' + BODY)
        self.page('PythonAPI.de/v2027.2', 'AI-CONTEXT.md')
        self.assertEqual(update_pages(en.parent), 1)
        self.assertEqual(en.read_bytes(), BODY.encode('utf-8'))
        self.assertEqual(update_pages(en.parent), 0)

    def test_staging_uses_the_published_folder_not_the_temporary_name(self):
        staged = self.page('work/pages')
        self.page('MCP.de/v2027.2')
        public = self.root / 'MCP' / 'v2027.2'
        self.assertFalse(public.exists())
        self.assertEqual(update_pages(staged.parent, public), 1)
        self.assertEqual(staged.read_text(encoding='utf-8').splitlines()[0],
                         '**English** \u2022 [Deutsch](../../MCP.de/v2027.2/Page.md)')
        self.assertFalse(public.exists())

    def test_cli_updates_multiple_folders(self):
        en, de = self.page('MCP/v2027.2'), self.page('MCP.de/v2027.2')
        result = subprocess.run(
            [sys.executable, str(GITHUB / 'scripts' / 'doc_languages.py'), str(en.parent), str(de.parent)],
            capture_output=True, text=True, check=True,
        )
        self.assertEqual(result.stdout.count('1 language selectors updated'), 2)
        self.assertTrue(en.read_bytes().startswith(b'**English**'))
        self.assertTrue(de.read_bytes().startswith(b'[English]'))

    def test_invalid_staging_arguments_do_not_modify_pages(self):
        en, de = self.page('MCP/v2027.2'), self.page('MCP.de/v2027.2')
        result = subprocess.run(
            [sys.executable, str(GITHUB / 'scripts' / 'doc_languages.py'),
             str(en.parent), str(de.parent), '--published', str(en.parent)],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn('exactly one staging folder', result.stderr)
        self.assertEqual(en.read_bytes(), BODY.encode('utf-8'))
        self.assertEqual(de.read_bytes(), BODY.encode('utf-8'))

    def test_validators_resolve_and_check_parent_links(self):
        staged = self.page('work/pages')
        translated = self.page('MCP.de/v2027.2')
        public = self.root / 'MCP' / 'v2027.2'
        update_pages(staged.parent, public)
        header = staged.read_text(encoding='utf-8').splitlines()[0]
        for skill in ('mcp-docs', 'pythonapi-docs'):
            validator = load_validator(skill)
            for fragment, expected in (('', 0), ('#topic', 0), ('#missing', 1)):
                with self.subTest(skill=skill, fragment=fragment):
                    text = header.replace('/Page.md)', '/Page.md' + fragment + ')') + '\n\n' + BODY
                    staged.write_bytes(text.encode('utf-8'))
                    with contextlib.redirect_stdout(io.StringIO()) as output:
                        self.assertEqual(validator.main(str(staged.parent), published=str(public)), expected)
                    if expected:
                        self.assertIn('missing anchor', output.getvalue())
        translated.unlink()
        for skill in ('mcp-docs', 'pythonapi-docs'):
            with self.subTest(skill=skill, missing_file=True):
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(load_validator(skill).main(str(staged.parent), published=str(public)), 1)
                self.assertIn('missing file', output.getvalue())

    def test_pythonapi_validator_resolves_published_ai_context(self):
        staged = self.page('work/pages', body=BODY + '\n[AI context](AI-CONTEXT.md#topic)\n')
        public = self.root / 'PythonAPI' / 'v2027.2'
        self.page('PythonAPI/v2027.2', 'AI-CONTEXT.md')
        validator = load_validator('pythonapi-docs')
        for fragment, expected in (('#topic', 0), ('#missing', 1)):
            with self.subTest(fragment=fragment):
                text = BODY + '\n[AI context](AI-CONTEXT.md' + fragment + ')\n'
                staged.write_bytes(text.encode('utf-8'))
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(validator.main(str(staged.parent), published=str(public)), expected,
                                     output.getvalue())
                if expected:
                    self.assertIn('missing anchor', output.getvalue())

    def test_validators_do_not_use_old_published_pages_for_local_links(self):
        staged = self.page('work/pages', body=BODY + '\n[Old page](Old.md)\n')
        self.page('MCP/v2027.2', 'Old.md')
        for skill in ('mcp-docs', 'pythonapi-docs'):
            with self.subTest(skill=skill):
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    result = load_validator(skill).main(str(staged.parent),
                                                        published=str(self.root / 'MCP' / 'v2027.2'))
                self.assertEqual(result, 1)
                self.assertIn('missing file Old.md', output.getvalue())

    def test_validators_accept_translated_tables_of_contents_and_html_anchors(self):
        body = ('# \u30da\u30fc\u30b8\n\n## {toc}\n\n- [\u30c8\u30d4\u30c3\u30af](#topic)\n\n'
                '<a id="topic"></a>\n\n## \u30c8\u30d4\u30c3\u30af\n\n[\u30c8\u30d4\u30c3\u30af](#topic)\n\n'
                '### {index} A\n\nText.\n')
        for toc, index in (('Inhaltsverzeichnis', 'Index'), ('\u76ee\u6b21', '\u7d22\u5f15')):
            page = self.page('Translated', body=body.format(toc=toc, index=index))
            for skill in ('mcp-docs', 'pythonapi-docs'):
                with self.subTest(skill=skill, toc=toc):
                    with contextlib.redirect_stdout(io.StringIO()) as output:
                        self.assertEqual(load_validator(skill).main(str(page.parent)), 0, output.getvalue())
        page.write_bytes(page.read_bytes().replace(b'</a>\n\n', b'</a>\n\nText.\n\n') + b'\n[Gone](#gone)\n')
        for skill, expected in (('mcp-docs', ('not in the table of contents', 'missing anchor')),
                                ('pythonapi-docs', ('missing anchor',))):
            with self.subTest(skill=skill, broken=True):
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(load_validator(skill).main(str(page.parent)), 1)
                for problem in expected:
                    self.assertIn(problem, output.getvalue())


if __name__ == '__main__':
    unittest.main()
