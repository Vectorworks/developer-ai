"""Renders the Python API reference: one Markdown page per group plus README.md. Run it through build.py."""

import collections
import os
import re

import bindscan
from describe import Describer, Translator, sentence, phrase
from model import Model, norm_type
from resolve import resolve, py_default
import intros

# binding folder -> page (the document entry point first); every folder also needs an entry in intros.FOLDERS
FOLDER_DOCS = collections.OrderedDict([
    ('.', 'DocumentAccess.md'),
    ('Attributes', 'Attributes.md'),
    ('ObjectPrimitives', 'ObjectPrimitives.md'),
    ('Math', 'ObjectPrimitives.Math.md'),
    ('Objects3D', 'Objects3D.md'),
    ('ObjectsAnnotation', 'ObjectsAnnotation.md'),
    ('ObjectsArchitect', 'ObjectsArchitect.md'),
    ('ObjectsConnectCAD', 'ObjectsConnectCAD.md'),
    ('ObjectsLandmark', 'ObjectsLandmark.md'),
    ('ObjectsSpotlight', 'ObjectsSpotlight.md'),
    ('Resources', 'Resources.md'),
    ('Scripting', 'Scripting.md'),
    ('UIAutomation', 'UIAutomation.md'),
    ('UILayoutCreate', 'UILayoutCreate.md'),
])

OPERATOR_SYMBOL = {
    '__eq__': '==', '__ne__': '!=', '__lt__': '<', '__le__': '<=', '__gt__': '>', '__ge__': '>=', '__add__': '+',
    '__sub__': '-', '__mul__': '*', '__rmul__': '* (reflected)', '__truediv__': '/', '__neg__': '- (unary)',
    '__iadd__': '+=', '__isub__': '-=', '__imul__': '*=', '__itruediv__': '/=', '__bool__': 'bool()',
    '__len__': 'len()', '__getitem__': '[]', '__setitem__': '[] =', '__call__': '()', '__repr__': 'repr()',
}


def anchor(text):
    a = text.strip().lower()
    a = re.sub(r'[^\w\- ]', '', a)
    a = a.replace(' ', '-')
    return a


def esc(text):
    """Escapes text for a Markdown table cell."""
    if text is None:
        return ''
    text = text.replace('\r', ' ').replace('\n', ' ')
    return text.replace('|', '\\|')


def first_sentence(text, limit=160):
    if not text:
        return ''
    m = re.match(r'^(.+?[.!?])(\s|$)', text)
    s = m.group(1) if m else text
    if len(s) > limit:
        s = s[:limit].rsplit(' ', 1)[0] + '...'
    return s


CODE_RE = re.compile(r'(^\s*(if|for|while)\s*\(|^\s*[{}]\s*$|^\s*C[A-Z]\w+\s+\w+\s*(;|=)|->\w+\(|static_cast<|^\s*\.\.\.;\s*$)')
CALL_RE = re.compile(r'^\s*[\w.]+\(.*\);\s*(//.*)?$')
CODE_LINES = []


def split_columns(s):
    parts = [p.strip() for p in re.split(r'\t+|\s{3,}', s) if p.strip()]
    return parts


def param_row(s):
    cols = split_columns(s)
    return ' — '.join([cols[0]] + [re.sub(r'^-\s+', '', c) for c in cols[1:]]) if len(cols) > 1 else s


def format_doc(lines, tr, owner=''):
    """Raw comment lines of a class or enum -> Markdown blocks (paragraphs, lists, rows)."""
    blocks = []
    para = []
    item_indent = None

    def flush_para():
        if para:
            blocks.append(('p', ' '.join(para)))
            para.clear()

    for raw in lines:
        if not raw.strip():
            flush_para()
            blocks.append(('break', None))
            continue
        indent = len(raw) - len(raw.lstrip())
        s = raw.strip()
        last = blocks[-1] if blocks else None
        if (last and last[0] in ('ul', 'ol', 'rows') and not para and item_indent is not None
                and indent >= item_indent + 2):
            # deeper indented line: continuation of the last item (the columns of a bare parameter-name row)
            bare = last[0] == 'rows' and last[1][-1].startswith('"') and ' — ' not in last[1][-1]
            last[1][-1] += (' — ' if bare else ' ') + s
            continue
        if CODE_RE.search(s) or (indent > 0 and CALL_RE.search(s)):
            CODE_LINES.append((owner, s))
            continue
        if s.startswith('|') and s.endswith('|') or (s.startswith('|') and '|' in s[1:]):
            flush_para()
            if last and last[0] == 'pre':
                last[1].append(s)
            else:
                blocks.append(('pre', [s]))
            continue
        m = re.match(r'^(?:[-*\u2022]|\d+[.)])\s+(.*)$', s)
        if m:
            flush_para()
            kind = 'ol' if re.match(r'^\d', s) else 'ul'
            item = m.group(1)
            cols = split_columns(item)
            if len(cols) > 1:
                item = ' — '.join(cols)
            if last and last[0] == kind:
                last[1].append(item)
            else:
                blocks.append((kind, [item]))
            item_indent = indent
            continue
        arrow = re.match(r'^(.+?)\s*->\s*(\S.*)$', s)
        if arrow and indent > 0:
            flush_para()
            item = '%s → %s' % (arrow.group(1).strip(), arrow.group(2).strip())
            if last and last[0] == 'rows':
                last[1].append(item)
            else:
                blocks.append(('rows', [item]))
            item_indent = indent
            continue
        if s.startswith('"') and last and last[0] == 'rows' and not para:
            # a quoted parameter name starts a new row; a row ending with ',' continues its name list
            if last[1][-1].endswith(',') and ' — ' not in last[1][-1]:
                last[1][-1] = param_row(last[1][-1] + ' ' + s)
            else:
                last[1].append(param_row(s))
            item_indent = indent
            continue
        cols = split_columns(s)
        if len(cols) > 1 and len(cols[0]) <= 48 and re.search(r'\t|\s{3,}', s):
            flush_para()
            cols = [cols[0]] + [re.sub(r'^-\s+', '', c) for c in cols[1:]]
            item = ' — '.join(cols)
            if last and last[0] == 'rows':
                last[1].append(item)
            else:
                blocks.append(('rows', [item]))
            item_indent = indent
            continue
        if indent > 0 and last and last[0] in ('ul', 'ol', 'rows') and not para:
            last[1][-1] += ' ' + s
            continue
        para.append(s)
    flush_para()

    out = []
    for kind, data in blocks:
        if kind == 'break':
            continue
        if kind == 'p':
            out.append(sentence_fix(tr.translate(data)))
        elif kind in ('ul', 'rows'):
            out.append('\n'.join('- ' + tr.translate(x) for x in data))
        elif kind == 'ol':
            out.append('\n'.join('%d. %s' % (k + 1, tr.translate(x)) for k, x in enumerate(data)))
        elif kind == 'pre':
            out.append('```text\n' + '\n'.join(tr.scrub(l) for l in data) + '\n```')
        elif kind == 'code':
            code = [l.replace('\t', '    ') for l in data]
            pad = min(len(l) - len(l.lstrip()) for l in code if l.strip())
            out.append('```cpp\n' + '\n'.join(l[pad:] for l in code) + '\n```')
    return [b for b in out if b.strip() and b.strip() not in ('-', '1.')]


def sentence_fix(text):
    text = text.strip()
    if text and text[0].islower():
        text = text[0].upper() + text[1:]
    return text


class Docs:
    def __init__(self, vw_root, out_dir, version_label):
        self.vw_root = vw_root
        self.out_dir = out_dir
        self.version_label = version_label
        self.notes = []
        self.binding_root = os.path.join(vw_root, 'PythonAPI')
        self.api_root = os.path.join(vw_root, 'API')
        self.model = Model(self.binding_root, self.api_root)
        self.members, self.problems = resolve(self.model)
        self.tr = Translator(self.model)
        self.desc = Describer(self.model, self.tr)
        self.provider_order = self._provider_order()
        self._organize()

    # ------------------------------------------------------------------------------------------------------------
    def _provider_order(self):
        path = os.path.join(self.vw_root, 'PythonProvider.cpp')
        with open(path, encoding='utf-8-sig', errors='replace') as f:
            text = f.read()
        body = text[text.find('bool BindTypes('):]
        body = body[:body.find('}')]
        return re.findall(r'CPy(\w+)::BindTypes', body)

    def _file_order(self, folder, files):
        """Order of the binding files of a folder: the order the umbrella binding (or PythonProvider) binds them."""
        order = []
        for bf in self.model.bfiles:
            if bf.folder != folder:
                continue
            for m in re.finditer(r'CPy(\w+)::BindTypes\s*\(', bf.code):
                name = 'Py%s.cpp' % m.group(1)
                if name != os.path.basename(bf.rel) and name not in order:
                    order.append(name)
        for name in self.provider_order:
            fn = 'Py%s.cpp' % name
            if fn not in order:
                order.append(fn)
        rank = {n: k for k, n in enumerate(order)}
        return sorted(files, key=lambda bf: (rank.get(os.path.basename(bf.rel), 1000), bf.rel))

    def _organize(self):
        m = self.model
        self.cls_info = {}       # cpp qual -> info dict
        self.enum_info = {}
        by_owner = collections.defaultdict(list)
        module_members = collections.defaultdict(list)
        for r in self.members:
            if r.owner:
                by_owner[r.owner].append(r)
            else:
                module_members[r.folder].append(r)
        self.by_owner = by_owner
        self.module_members = module_members

        used = {bf.folder for bf in m.bfiles if bf.classes or bf.enums} | {r.folder for r in self.members}
        unknown = sorted(f for f in used if f not in FOLDER_DOCS)
        if unknown:
            raise SystemExit('No page for binding folder(s) %s: add each one to FOLDER_DOCS in render.py and to FOLDERS '
                             'in intros.py (title, name, short, intro).' % ', '.join(unknown))
        no_intro = [f for f in FOLDER_DOCS if f not in intros.FOLDERS]
        if no_intro:
            raise SystemExit('No entry in intros.FOLDERS for %s.' % ', '.join(no_intro))
        for folder in FOLDER_DOCS:
            if folder not in used:
                self.notes.append('group %s has no classes, enumerations or functions in this source; remove it from '
                                  'FOLDER_DOCS and intros.FOLDERS if the group was dropped' % folder)
        self.folder_files = collections.OrderedDict()
        for folder in FOLDER_DOCS:
            files = [bf for bf in m.bfiles if bf.folder == folder]
            self.folder_files[folder] = self._file_order(folder, files)

        # classes
        for bf in m.bfiles:
            for c in bf.classes:
                q = norm_type(c['cpp'])
                q = m.resolve_name(q, '') or q
                hc = m.hclasses.get(q)
                py = m.py_class_name(q)
                info = {
                    'cpp': q, 'py': py, 'qualname': c['qualname'], 'module': c['module'], 'folder': bf.folder,
                    'file': bf.rel, 'doc': c['doc'], 'hc': hc, 'base': None, 'nested_in': None,
                    'members': by_owner.get(q, []), 'pos': c['pos'],
                }
                if c['base']:
                    bq = m.resolve_name(norm_type(c['base']), '')
                    info['base'] = bq
                if '.' in c['qualname']:
                    outer = c['qualname'].rsplit('.', 1)[0]
                    info['nested_in'] = outer
                fields = [x for x in info['members'] if x.kind == 'Field']
                info['has_fields'] = bool(fields)
                methods = [x for x in info['members'] if x.kind == 'Def' and not x.name.startswith('__')]
                info['static_only'] = bool(methods) and all(x.static for x in methods)
                info['has_handle'] = any(x.kind == 'Def' and x.name == 'GetHandle' for x in self.all_members(q, info))
                info['is_settings'] = bool(re.search(r'Settings$|Defaults$|DefaultAttributes$', py or ''))
                self.cls_info[q] = info
        # handle-based wrappers inherit has_handle
        for q, info in self.cls_info.items():
            b = info['base']
            while b and not info['has_handle']:
                bi = self.cls_info.get(b)
                if not bi:
                    break
                if any(x.kind == 'Def' and x.name == 'GetHandle' for x in bi['members']):
                    info['has_handle'] = True
                b = bi['base']
        for bf in m.bfiles:
            for e in bf.enums:
                q = norm_type(e['cpp'])
                q = m.resolve_name(q, '') or q
                he = m.henums.get(q)
                self.enum_info[q] = {
                    'cpp': q, 'py': m.py_enum_name(q), 'qualname': e['qualname'], 'module': e['module'],
                    'folder': bf.folder, 'file': bf.rel, 'flag': e['flag'], 'values': e['values'], 'he': he,
                    'nested_in': e['qualname'].rsplit('.', 1)[0] if '.' in e['qualname'] else None, 'pos': e['pos'],
                }
        # Python name -> (doc file, anchor)
        self.locations = {}
        for q, info in self.cls_info.items():
            self.locations[info['py']] = (FOLDER_DOCS[info['folder']], anchor(info['py']))
        for q, info in self.enum_info.items():
            self.locations[info['py']] = (FOLDER_DOCS[info['folder']], anchor(info['py']))

    def all_members(self, q, info):
        return info['members'] if info else self.by_owner.get(q, [])

    def file_rank(self, rel):
        folder = rel.rsplit('/', 1)[0] if '/' in rel else '.'
        files = self.folder_files.get(folder, [])
        for k, bf in enumerate(files):
            if bf.rel == rel:
                return k
        return 1000

    # ------------------------------------------------------------------------------------------------------------
    def link(self, py, current_doc, code=True):
        loc = self.locations.get(py)
        text = '`%s`' % py if code else py
        if not loc:
            return text
        doc, anc = loc
        target = ('#' + anc) if doc == current_doc else '%s#%s' % (doc, anc)
        return '[%s](%s)' % (text, target)

    def link_type(self, type_text, current_doc):
        """Links the bound type names inside a Python type expression; returns Markdown (not inside code)."""
        parts = re.split(r'([\w.]+)', type_text)
        out = []
        for p in parts:
            if p in self.locations:
                doc, anc = self.locations[p]
                target = ('#' + anc) if doc == current_doc else '%s#%s' % (doc, anc)
                out.append('[%s](%s)' % (p, target))
            else:
                out.append(p)
        return ''.join(out)

    def signature(self, name, params, ret, bf_file):
        bf = next((b for b in self.model.bfiles if b.rel == bf_file), None)
        items = []
        for p in params:
            s = '%s: %s' % (p['name'], p['type'])
            if p['default_expr'] is not None:
                s += ' = %s' % py_default(self.model, bf, p['default_expr'], p['type'])
            items.append(s)
        sig = '%s(%s)' % (name, ', '.join(items))
        if ret is not None:
            sig += ' -> %s' % ret
        return sig

    # ------------------------------------------------------------------------------------------------------------
    def base_chain(self, q):
        chain = []
        b = self.cls_info[q]['base']
        while b:
            bi = self.cls_info.get(b)
            if not bi:
                break
            chain.append(bi['py'])
            b = bi['base']
        return chain

    def class_description(self, info):
        key = 'class:' + info['py']
        if key in self.desc.overrides:
            self.desc.used_overrides.add(key)
            ov = self.desc.overrides[key]
            return ov if isinstance(ov, str) else ' '.join(ov)
        hc = info['hc']
        text = ''
        if hc is not None and hc.get('lead'):
            text = hc['lead']
        if not text or (info['doc'] and len(info['doc']) > len(text) + 20):
            text = info['doc'] or text
        return self.tr.translate(text)

    def class_doc_blocks(self, info):
        key = 'class:' + info['py']
        if key in self.desc.overrides:
            self.desc.used_overrides.add(key)
            ov = self.desc.overrides[key]
            return [ov] if isinstance(ov, str) else list(ov)
        hc = info['hc']
        if hc is not None and hc.get('lead_raw'):
            blocks = format_doc(hc['lead_raw'], self.tr, info['py'])
            if blocks:
                return blocks
        d = self.class_description(info)
        return [sentence(d)] if d else []

    def enum_description(self, info):
        key = 'enum:' + info['py']
        if key in self.desc.overrides:
            ov = self.desc.overrides[key]
            return ov if isinstance(ov, str) else ' '.join(ov)
        he = info['he']
        text = (he or {}).get('lead') or ''
        trail = ' '.join((he or {}).get('trail') or [])
        if trail:
            text = (text + ' ' + trail).strip()
        return self.tr.translate(text)

    def enum_values(self, info):
        he = info['he'] or {'values': []}
        hv = {v['name']: v for v in he['values']}
        # numeric values: explicit literal or previous + 1
        numeric = {}
        prev = -1
        for v in he['values']:
            val = None
            if v['value'] is None:
                val = prev + 1
            else:
                expr = v['value'].strip()
                try:
                    if re.match(r'^-?(0x[0-9a-fA-F]+|\d+)[uUlL]*$', expr):
                        val = int(expr.rstrip('uUlL'), 0)
                    else:
                        e2 = re.sub(r'\b([A-Za-z_]\w*)\b', lambda mm: str(numeric[mm.group(1)]) if mm.group(1) in numeric else mm.group(1), expr)
                        e2 = re.sub(r'static_cast<[^>]+>', '', e2)
                        if re.match(r'^[\d\s|&+\-*()<>~x]+$', e2):
                            val = int(eval(e2, {'__builtins__': {}}, {}))
                except Exception:
                    val = None
            numeric[v['name']] = val if val is not None else v['value']
            if isinstance(val, int):
                prev = val
        rows = []
        for v in info['values']:
            cpp_name = v['cpp'].split('::')[-1]
            h = hv.get(cpp_name, {})
            value = numeric.get(cpp_name, '')
            comment = ' '.join([x for x in [' '.join(h.get('lead') or []), ' '.join(h.get('trail') or [])] if x])
            rows.append((v['name'], value, self.tr.translate(comment)))
        return rows

    # ------------------------------------------------------------------------------------------------------------
    def render_folder(self, folder):
        doc = FOLDER_DOCS[folder]
        files = self.folder_files[folder]
        classes = []
        enums = []
        for bf in files:
            for c in sorted(bf.classes, key=lambda x: x['pos']):
                q = self.model.resolve_name(norm_type(c['cpp']), '') or norm_type(c['cpp'])
                classes.append(self.cls_info[q])
            for e in sorted(bf.enums, key=lambda x: x['pos']):
                q = self.model.resolve_name(norm_type(e['cpp']), '') or norm_type(e['cpp'])
                enums.append(self.enum_info[q])
        top_classes = [c for c in classes if not c['nested_in']]
        nested_classes = collections.defaultdict(list)
        for c in classes:
            if c['nested_in']:
                nested_classes[c['nested_in']].append(c)
        nested_enums = collections.defaultdict(list)
        top_enums = []
        for e in enums:
            if e['nested_in']:
                nested_enums[e['nested_in']].append(e)
            else:
                top_enums.append(e)
        mod_members = self.module_members.get(folder, [])
        mod_funcs = [r for r in mod_members if r.kind == 'Def']
        mod_consts = [r for r in mod_members if r.kind == 'Constant']
        aliases = [a for bf in files for a in bf.aliases]
        implicit = [a for bf in files for a in bf.implicit]
        module_name = 'api.Math' if folder == 'Math' else 'api'

        intro = intros.FOLDERS[folder]
        lines = []
        w = lines.append
        w('# %s' % intro['title'])
        w('')
        w('> **Python module:** `%s` · **Version:** %s' % (module_name, self.version_label))
        w('')
        w('[Back to the index](README.md)')
        w('')
        for para in intro['intro']:
            w(para)
            w('')

        # table of contents
        w('## Table of contents')
        w('')
        w('- [Overview](#overview)')
        if top_classes:
            w('- [Classes](#classes)')
            for c in top_classes:
                w('  - [%s](#%s)' % (c['py'], anchor(c['py'])))
                for n in self._nested_of(c, nested_classes, nested_enums):
                    w('    - [%s](#%s)' % (n['py'], anchor(n['py'])))
        if top_enums:
            w('- [Enumerations](#enumerations)')
            for e in top_enums:
                w('  - [%s](#%s)' % (e['py'], anchor(e['py'])))
        if mod_funcs:
            w('- [Module functions](#module-functions)')
        if mod_consts:
            w('- [Module constants](#module-constants)')
        if aliases or implicit:
            w('- [Aliases and implicit conversions](#aliases-and-implicit-conversions)')
        w('')

        # overview
        w('## Overview')
        w('')
        w('| Name | Kind | Inherits from | Summary |')
        w('|---|---|---|---|')
        for c in top_classes:
            self._overview_row(w, c, 'class', doc)
            for n in self._nested_of(c, nested_classes, nested_enums):
                if 'values' in n:
                    self._overview_row(w, n, ('IntFlag' if n['flag'] else 'IntEnum') + ' (nested)', doc)
                else:
                    self._overview_row(w, n, 'class (nested)', doc)
        for e in top_enums:
            self._overview_row(w, e, 'IntFlag' if e['flag'] else 'IntEnum', doc)
        if mod_funcs:
            names = sorted(set(r.name for r in mod_funcs))
            w('| [Module functions](#module-functions) | functions | | %s |' % esc(', '.join('`%s`' % n for n in names)))
        if mod_consts:
            w('| [Module constants](#module-constants) | constants | | %s |' % esc(', '.join('`%s`' % r.name for r in mod_consts)))
        w('')

        if top_classes:
            w('## Classes')
            w('')
            for c in top_classes:
                self.render_class(w, c, doc, level=3)
                for n in self._nested_of(c, nested_classes, nested_enums):
                    if 'values' in n:
                        self.render_enum(w, n, doc, level=4)
                    else:
                        self.render_class(w, n, doc, level=4)
        if top_enums:
            w('## Enumerations')
            w('')
            for e in top_enums:
                self.render_enum(w, e, doc, level=3)
        if mod_funcs:
            w('## Module functions')
            w('')
            w('Functions of the `%s` module (call them as `%s.Name(...)`).' % (module_name, module_name))
            w('')
            w('| Function | Description |')
            w('|---|---|')
            for r in sorted(mod_funcs, key=lambda x: x.pos):
                sig = self.signature(r.name, r.params, r.ret, r.file)
                w('| `%s` | %s |' % (esc(sig), esc(self.desc.method(module_name, r, {}))))
            w('')
        if mod_consts:
            w('## Module constants')
            w('')
            w('| Constant | Type | Value | Description |')
            w('|---|---|---|---|')
            for r in sorted(mod_consts, key=lambda x: x.pos):
                w('| `%s.%s` | `%s` | `%s` | %s |' % (module_name, r.name, r.type, esc(self.const_value(r)), esc(self.desc.constant(module_name, r))))
            w('')
        if aliases or implicit:
            w('## Aliases and implicit conversions')
            w('')
            for a in aliases:
                q = self.model.resolve_name(norm_type(a['cpp']), '')
                py = self.model.py_class_name(q)
                w('- `%s.%s` is another name of %s (the same class object).' % (module_name, a['name'], self.link(py, doc)))
            for a in implicit:
                fq = self.model.resolve_name(norm_type(a['from']), '')
                tq = self.model.resolve_name(norm_type(a['to']), '')
                w('- A %s is accepted wherever a %s argument is expected (implicit conversion).' % (
                    self.link(self.model.py_class_name(fq), doc), self.link(self.model.py_class_name(tq), doc)))
            w('')
        w('---')
        w('')
        w('[Back to the index](README.md) · [Back to top](#%s)' % anchor(intro['title']))
        w('')
        return '\n'.join(lines)

    def _nested_of(self, c, nested_classes, nested_enums):
        out = []
        for n in nested_classes.get(c['qualname'], []):
            out.append(n)
            out.extend(self._nested_of(n, nested_classes, nested_enums))
        out.extend(nested_enums.get(c['qualname'], []))
        return out

    def _overview_row(self, w, info, kind, doc):
        if 'values' in info:
            summary = first_sentence(self.enum_description(info)) or ''
            base = ''
        else:
            summary = first_sentence(self.class_description(info)) or ''
            chain = self.base_chain(info['cpp'])
            base = self.link(chain[0], doc) if chain else ''
        w('| [`%s`](#%s) | %s | %s | %s |' % (info['py'], anchor(info['py']), kind, base, esc(summary)))

    def const_value(self, r):
        v = getattr(r, 'value', None)
        if v is None:
            return ''
        v = v.strip()
        v = re.sub(r'^static_cast<[^>]+>\((.*)\)$', r'\1', v)
        if v in ('true', 'false'):
            return 'True' if v == 'true' else 'False'
        if v == 'static_cast<size_t>(-1)' or v == '-1' and getattr(r, 'type', '') == 'int' and 'size_t' in str((r.decl or {}).get('ftype', '')):
            return '2**64 - 1'
        if (r.decl or {}).get('ftype', '').endswith('size_t') and v.strip() == '-1':
            return '2**64 - 1'
        return self.tr.translate(v)

    # ------------------------------------------------------------------------------------------------------------
    def render_class(self, w, info, doc, level):
        h = '#' * level
        w('%s %s' % (h, info['py']))
        w('')
        chain = self.base_chain(info['cpp'])
        inherits = ' → '.join([self.link(b, doc) for b in chain] + ['`api.Object`'])
        module = info['module']
        hc = info['hc']
        w('> **Full name:** `%s.%s` · **Inherits:** %s' % (module, info['qualname'], inherits))
        w('')
        for block in self.class_doc_blocks(info):
            w(block)
            w('')
        members = info['members']
        inits = [r for r in members if r.kind == 'Init']
        defs = [r for r in members if r.kind == 'Def']
        fields = [r for r in members if r.kind == 'Field']
        consts = [r for r in members if r.kind == 'Constant']
        ops = [r for r in defs if r.name.startswith('__')]
        methods = [r for r in defs if not r.name.startswith('__')]
        cls_info = info

        # constructors
        w('**Constructors**')
        w('')
        if inits:
            w('| Constructor | Description |')
            w('|---|---|')
            for r in inits:
                sig = self.signature(info['qualname'].split('.')[-1] if False else info['py'].split('.')[-1], r.params, None, r.file)
                w('| `%s` | %s |' % (esc(sig), esc(self.desc.ctor(info['py'], r, cls_info))))
            if fields and any(not r.params for r in inits):
                names = ', '.join(f.name for f in fields)
                short = info['py'].split('.')[-1]
                if any(len(r.params) == len(fields) for r in inits):
                    # positional values would select the explicit constructor of the same arity
                    w('| `%s(%s)` | Field values as keywords (any subset), e.g. `%s(%s=...)`. |' % (
                        short, esc(', '.join('%s=...' % f.name for f in fields)), short, fields[0].name))
                else:
                    w('| `%s(%s)` | Field values: all fields positionally (in this order) or any of them as keywords. |' % (short, esc(names)))
            w('')
        elif fields:
            w('Construct it with field values: `%s(%s)` (all fields positionally) or keywords.' % (info['py'].split('.')[-1], ', '.join(f.name for f in fields)))
            w('')
        else:
            static_only = methods and all(r.static for r in methods)
            if static_only:
                w('Not instantiable from Python: use the static methods on the class (`%s.%s.Method(...)`).' % (module, info['qualname']))
            else:
                w('Not instantiable from Python: instances are returned by other API functions.')
            w('')

        # methods grouped by header section
        if methods:
            w('**Methods**')
            w('')
            groups = collections.OrderedDict()
            for r in methods:
                sec = (r.decl or {}).get('section') if r.decl is not None else None
                if r.decl_class is not None and r.decl_class is not hc and hc is not None:
                    sec = sec
                groups.setdefault(sec or '', []).append(r)
            # avoid a single unnamed group plus named groups out of order: keep binding order of groups
            multi = len(groups) > 1
            for sec, items in groups.items():
                if multi:
                    w('*%s*' % (self.tr.translate(sec) if sec else 'General'))
                    w('')
                w('| Method | Description |')
                w('|---|---|')
                for r in items:
                    sig = self.signature(r.name, r.params, r.ret, r.file)
                    tag = ' *static*' if r.static else ''
                    w('| `%s`%s | %s |' % (esc(sig), tag, esc(self.desc.method(info['py'], r, cls_info))))
                w('')
        if ops:
            w('**Operators and Python protocols**')
            w('')
            w('| Operator | Method | Description |')
            w('|---|---|---|')
            for r in ops:
                sig = self.signature(r.name, r.params, r.ret, r.file)
                w('| `%s` | `%s` | %s |' % (esc(OPERATOR_SYMBOL.get(r.name, r.name)), esc(sig), esc(self.desc.method(info['py'], r, cls_info))))
            w('')
        if fields:
            w('**Fields**')
            w('')
            w('| Field | Type | Description |')
            w('|---|---|---|')
            for f in fields:
                w('| `%s` | `%s` | %s |' % (f.name, esc(f.type), esc(self.desc.field(info['py'], f))))
            w('')
        if consts:
            w('**Constants**')
            w('')
            w('| Constant | Type | Value | Description |')
            w('|---|---|---|---|')
            for c in consts:
                w('| `%s.%s` | `%s` | `%s` | %s |' % (info['py'].split('.')[-1], c.name, c.type, esc(self.const_value(c)), esc(self.desc.constant(info['py'], c))))
            w('')
        if not (inits or methods or ops or fields or consts):
            w('No members of its own.')
            w('')
        if chain:
            w('Inherited: everything from %s.' % ', '.join(self.link(b, doc) for b in chain))
            w('')

    def render_enum(self, w, info, doc, level):
        h = '#' * level
        w('%s %s' % (h, info['py']))
        w('')
        kind = '`IntFlag` (members combine with `|`)' if info['flag'] else '`IntEnum`'
        w('> **Full name:** `%s.%s` · **Kind:** %s' % (info['module'], info['qualname'], kind))
        w('')
        he_raw = (info['he'] or {}).get('lead_raw')
        ekey = 'enum:' + info['py']
        if ekey in self.desc.overrides:
            self.desc.used_overrides.add(ekey)
            ov = self.desc.overrides[ekey]
            for block in ([ov] if isinstance(ov, str) else ov):
                w(block)
                w('')
        elif he_raw:
            for block in format_doc(he_raw, self.tr, info['py']):
                w(block)
                w('')
        else:
            d = self.enum_description(info)
            if d:
                w(sentence(d))
                w('')
        w('| Member | Value | Description |')
        w('|---|---|---|')
        for name, value, comment in self.enum_values(info):
            w('| `%s` | `%s` | %s |' % (name, value, esc(sentence(comment) if comment else '')))
        w('')

    # ------------------------------------------------------------------------------------------------------------
    def write_all(self):
        os.makedirs(self.out_dir, exist_ok=True)
        written = []
        for folder, doc in FOLDER_DOCS.items():
            text = self.render_folder(folder)
            with open(os.path.join(self.out_dir, doc), 'w', encoding='utf-8', newline='\n') as f:
                f.write(text)
            written.append(doc)
        readme = intros.readme(self)
        with open(os.path.join(self.out_dir, 'README.md'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(readme)
        written.append('README.md')
        return written
