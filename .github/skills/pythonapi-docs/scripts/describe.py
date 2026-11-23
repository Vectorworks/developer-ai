"""Descriptions of the Python-visible members: header comments translated to Python names, rule based fallbacks
for accessors and operators, and curated overrides (overrides.json)."""

import collections
import json
import os
import re

from scrub import Scrubber

ACRONYMS = {'2D', '3D', 'DPI', 'GDTF', 'XY', 'XYZ', 'ID', 'IDS', 'UI', 'OIP', 'RGB', 'DMX', 'URL', 'JSON', 'SIA', 'IFC',
            'PNG', 'UV', 'NURBS', 'CSG', 'HTML', 'UTF8', 'CAD', 'BIM', 'PDF', 'RGB8', 'TIN', 'DTM', 'CW', 'CCW', 'PIO',
            'ASCII', 'IP', 'GUID', 'UUID', 'LED', 'SVG', 'DWG', 'ID'}
SPECIAL_WORDS = {'XRay': 'X-ray', 'Nurbs': 'NURBS', 'Gdtf': 'GDTF', 'Dpi': 'DPI', 'Uv': 'UV', 'Csg': 'CSG', 'UVs': 'UVs'}

OVERRIDES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'overrides.json')


def load_overrides():
    try:
        import overrides_data
        return dict(overrides_data.OVERRIDES)
    except ImportError:
        return {}


def split_words(name):
    for k, v in SPECIAL_WORDS.items():
        name = name.replace(k, '_' + v + '_')
    parts = []
    for chunk in name.split('_'):
        if not chunk:
            continue
        if chunk in SPECIAL_WORDS.values():
            parts.append(chunk)
            continue
        parts.extend(re.findall(r'\d+D(?![a-z])|\d+|[A-Z]+(?=[A-Z][a-z]|\d|$)|[A-Z][a-z]+|[a-z]+|[A-Z]+', chunk))
    return parts


def phrase(name, title=False):
    words = split_words(name)
    out = []
    for w in words:
        if w.upper() in ACRONYMS or (len(w) > 1 and w.isupper()) or re.match(r'^\d+D$', w) or w == 'UVs':
            out.append(w)
        elif len(w) == 1 and w.isalpha():
            out.append(w.upper())
        elif title:
            out.append(w[0].upper() + w[1:])
        else:
            out.append(w.lower())
    return ' '.join(out)


def sentence(text):
    text = text.strip()
    if not text:
        return text
    text = text[0].upper() + text[1:]
    if not text.endswith(('.', '!', '?', ')', ':')) and not text.endswith('...'):
        text += '.'
    elif text.endswith(')') and not re.search(r'\.\)$', text):
        text += '.'
    return text


class Translator:
    """Replaces C++ names of bound types in comments with their Python names."""

    def __init__(self, model):
        self.names = {}
        for q, c in model.classes.items():
            self.names[q] = model.py_class_name(q)
        for q, e in model.enums.items():
            self.names[q] = model.py_enum_name(q)
        # unqualified spellings of nested and Math names
        extra = {}
        for q, py in self.names.items():
            short = q.split('::')[-1]
            if '::' in q and q.startswith('Math::'):
                extra.setdefault(short, py)
        for k, v in extra.items():
            self.names.setdefault(k, v)
        self.enum_values = {}
        for q, e in model.enums.items():
            for v in e['values']:
                self.enum_values[norm_enum(v['cpp'])] = '%s.%s' % (model.py_enum_name(q), v['name'])
        # unqualified spellings of nested C++ types (ESpacing, THeights, ...) when they are unique
        shorts = collections.defaultdict(set)
        for q, py in self.names.items():
            if '::' in q:
                short = q.split('::')[-1]
                if re.match(r'^[CET][A-Z]', short):
                    shorts[short].add(py)
        for short, pys in shorts.items():
            if len(pys) == 1:
                self.names.setdefault(short, next(iter(pys)))
        short_values = collections.defaultdict(set)
        for cpp, py in self.enum_values.items():
            parts = cpp.split('::')
            if len(parts) > 2:
                short_values['::'.join(parts[-2:])].add(py)
        for short, pys in short_values.items():
            if len(pys) == 1:
                self.enum_values.setdefault(short, next(iter(pys)))
        object_types = []
        for q, e in model.enums.items():
            if model.py_enum_name(q) == 'ObjectType':
                object_types = [v['name'] for v in e['values']]
        self.scrub = Scrubber(object_types)
        self.pattern = re.compile(r'\b(?:VWObjectAPI::)?((?:Math::)?[A-Z]\w*(?:::[A-Za-z_]\w*)*)(<[^<>()]*>)?(\(\))?')

    def translate(self, text):
        if not text:
            return text

        def repl(m):
            full = m.group(1)
            tmpl = m.group(2) or ''
            call = m.group(3) or ''
            if full in self.enum_values:
                return self.enum_values[full]
            parts = full.split('::')
            # longest prefix that is a bound type
            for k in range(len(parts), 0, -1):
                head = '::'.join(parts[:k])
                if head in self.names:
                    rest = parts[k:]
                    py = self.names[head]
                    if rest:
                        py += '.' + '.'.join(rest)
                    if tmpl and rest:
                        tmpl = ''
                    return py + tmpl + call
            return m.group(0)

        text = self.pattern.sub(repl, text)
        text = re.sub(r'\bstd::nullopt\b', 'None', text)
        text = re.sub(r'\bnullopt\b', 'None', text)
        text = re.sub(r'\bnullptr\b', 'null', text)
        text = re.sub(r'\b(an )?empty optional\b', 'None', text, flags=re.I)
        text = re.sub(r'\bstd::optional\b', 'optional', text)
        text = re.sub(r'\bstd::vector\b', 'list', text)
        text = re.sub(r'\bstd::string\b', 'str', text)
        adjective_use = r'(?!\s+(world|north|size|length|colou?r|scale|distance|area|shape|height|width|angle|position|origin|type|name|value|elevation|direction)\b)'
        text = re.sub(r'\btrue\b' + adjective_use, 'True', text)
        text = re.sub(r'\bfalse\b' + adjective_use, 'False', text)
        text = re.sub(r'\bBlankHandle\b', 'Handle', text)
        return self.scrub(self.codeify(text))

    CODE_TOKEN = re.compile(
        r"'([A-Za-z_]\w*)'"                                         # 'param'
        r"|((?:Math\.)?[A-Z]\w*(?:\.[A-Za-z_]\w*)*\(\))"            # Name() / Class.Method()
        r"|((?:Math\.)?[A-Z]\w*(?:\.[A-Za-z_]\w*)+)"                 # Class.Member
        r"|\b(True|False|None|k[A-Z]\w+)\b")                        # literals and k-constants

    def codeify(self, text):
        known = set(v for v in self.names.values())
        # Markdown-like '[title](target)' in C++ comments is not a link
        text = re.sub(r'(?<!`)\[(\w+)\]\((\w+)\)', r'`[\1](\2)`', text)
        parts = re.split(r'(`[^`]*`)', text)
        for k in range(0, len(parts), 2):
            seg = parts[k]

            def repl(m, seg=seg):
                if m.group(1):
                    return '`%s`' % m.group(1)
                if m.group(2):
                    return '`%s`' % m.group(2)
                if m.group(3):
                    head = m.group(3).split('.')
                    first = '.'.join(head[:2]) if head[0] == 'Math' else head[0]
                    if first in known or head[0] in known:
                        return '`%s`' % m.group(3)
                    return m.group(0)
                # 'None / Circular Zone': a choice label, not the Python literal
                before = seg[max(0, m.start() - 3):m.start()]
                after = seg[m.end():m.end() + 3]
                if m.group(4) in ('None', 'True', 'False') and ('/' in before or '/' in after):
                    return m.group(0)
                return '`%s`' % m.group(4)
            parts[k] = self.CODE_TOKEN.sub(repl, seg)
        return ''.join(parts)


def norm_enum(cpp):
    return cpp.replace('VWObjectAPI::', '').strip()


# Object names as the Vectorworks help writes them, where the class name does not give them.
OWNER_NOUNS = {
    'PrimitiveObject': 'drawing object',
    'ParametricObject': 'plug-in object',
    'RoundRectObject': 'rounded rectangle',
    'Locus2DObject': '2D locus',
    'MultiExtrudeObject': 'multiple extrude',
    'Polygon3DObject': '3D polygon',
    'ShellObject': 'shell solid',
    'ConnectCADSocketObject': 'ConnectCAD socket',
    'ConnectCADDeviceObject': 'ConnectCAD device',
    'RenderBackground': 'Renderworks background',
    'BuildingMaterial': 'material',
}


def owner_noun(py_class):
    if not py_class:
        return 'object'
    base = py_class.split('.')[-1]
    if base in OWNER_NOUNS:
        return OWNER_NOUNS[base]
    base = re.sub(r'(Object|Resource|Attributes|Settings)$', '', base) or base
    base = re.sub(r'2D$|3D$', '', base) or base
    return phrase(base)


def plural(noun):
    if re.search(r'[^aeiou]y$', noun):
        return noun[:-1] + 'ies'
    return noun + 's'


def fmt_trail(trail):
    if not trail:
        return ''
    t = ' '.join(x.strip() for x in trail if x.strip())
    return t


def join_desc(main, extra):
    """main sentence + extra comment fragment."""
    if not extra:
        return sentence(main) if main else ''
    if not main:
        return sentence(extra)
    main = sentence(main)
    words = len(extra.split())
    if words <= 12 and not re.search(r'[.;]\s', extra) and not extra.endswith('.'):
        return main[:-1] + ' (' + extra.rstrip('.') + ').' if main.endswith('.') else main + ' (' + extra + ')'
    return main + ' ' + sentence(extra)


BOOL_TYPES = ('bool', 'bool | None')

ADJECTIVES = {
    'valid', 'open', 'empty', 'visible', 'hidden', 'active', 'closed', 'locked', 'selected', 'flipped', 'modular',
    'available', 'enabled', 'running', 'wrapped', 'metric', 'primary', 'clockwise', 'counterclockwise', 'convex',
    'finite', 'zero', 'equal', 'parallel', 'perpendicular', 'degenerate', 'planar', 'solid', 'editable', 'relative',
    'linked', 'default', 'deleted', 'mirrored', 'rotated', 'right', 'left', 'top', 'bottom', 'in', 'on', 'inside',
    'outside', 'full', 'same', 'imported', 'reversed', 'square', 'axis', 'round', 'straight', 'horizontal', 'vertical',
    'read', 'unique', 'ready', 'checked', 'expanded', 'multi', 'single', 'tapered', 'symmetric', 'curved', 'free',
    'stacked', 'grouped', 'nested', 'locked', 'transparent', 'opaque', 'unfolded', 'hybrid', 'empty', 'new', 'up',
    'within', 'inverse', 'normalized', 'identity', 'set',
}

OPERATOR_TEXT = {
    '__add__': '`a + b`: sum of the two values.',
    '__sub__': '`a - b`: difference of the two values.',
    '__neg__': '`-a`: the negated value.',
    '__mul__': None,
    '__rmul__': '`s * a`: the value scaled by a scalar.',
    '__truediv__': '`a / s`: the value divided by a scalar.',
    '__iadd__': '`a += b`: adds the other value in place.',
    '__isub__': '`a -= b`: subtracts the other value in place.',
    '__imul__': None,
    '__itruediv__': '`a /= s`: divides in place by a scalar.',
    '__len__': '`len(a)`: number of vertices.',
    '__repr__': '`repr(a)`: short text description.',
}


def auto_describe(m, py_class, cls_info):
    """Rule based description of a method. Returns (text, confident)."""
    name = m.name
    params = m.params or []
    ret = m.ret or 'None'
    pnames = [p['name'] for p in params]
    noun = owner_noun(py_class)
    has_handle = cls_info.get('has_handle')

    if name == '__eq__':
        if has_handle:
            return '`a == b`: True when both objects refer to the same %s.' % noun, True
        return '`a == b`: True when the two values are equal.', True
    if name == '__ne__':
        if has_handle:
            return '`a != b`: True when the objects refer to different %s.' % plural(noun) if not noun.endswith('s') else '`a != b`: True when the objects refer to different drawing objects.', True
        return '`a != b`: True when the two values differ.', True
    if name == '__bool__':
        return '`bool(a)`: True when the object is valid (same as `IsValid()`).', True
    if name == '__mul__':
        if 'Transform' in (py_class or ''):
            return '`A * B`: the composed transform (B is applied first, then A).', True
        return '`a * s`: the value scaled by a scalar.', True
    if name == '__imul__':
        if 'Transform' in (py_class or ''):
            return '`A *= B`: composes the other transform in place.', True
        return '`a *= s`: scales in place by a scalar.', True
    if name == '__call__':
        return '`T(p)`: applies the transform to the point (same as `Apply`).', True
    if name in OPERATOR_TEXT and OPERATOR_TEXT[name]:
        return OPERATOR_TEXT[name], True

    if name == 'Is' and pnames == ['h'] and m.static:
        return 'True when `h` refers to an object of the kind this class represents.', True
    if name == 'IsValid' and not params:
        return 'True when this object refers to an existing %s.' % noun, True
    if name == 'GetHandle' and not params:
        return 'Handle of the %s.' % noun, True
    if name == 'Duplicate' and not params:
        return 'Duplicates the %s in the drawing and returns the copy.' % noun, True

    mm = re.match(r'^(Get|Set|Is|Has|Can|Uses|Count)([A-Z0-9].*)$', name)
    if not mm:
        return None, False
    verb, subject = mm.group(1), mm.group(2)
    sub_plain = phrase(subject)
    sub_title = phrase(subject, title=True)
    settings = cls_info.get('is_settings')

    def where():
        rest = [p for p in pnames]
        if not rest:
            return ''
        if len(rest) == 1:
            p = rest[0]
            if p in ('index', 'i') or p.endswith('Index'):
                return ' at `%s`' % p
            if p in ('controlID',):
                return ' of control `controlID`'
            if p in ('charIndex',):
                return ' at character `charIndex`'
            return ' for `%s`' % p
        return ' for ' + ', '.join('`%s`' % p for p in rest)

    if verb == 'Get':
        if subject.startswith('All') and len(subject) > 3 and subject[3].isupper():
            return 'Returns all %s%s.' % (phrase(subject[3:]), where()), True
        if subject == 'All':
            return 'Returns all items%s.' % where(), True
        if subject.endswith('Count') and len(subject) > 5:
            return 'Number of %s%s.' % (phrase(subject[:-5]) + ('' if subject[:-5].endswith('s') else ' items'), where()), True
        if ret in BOOL_TYPES:
            shown = subject[2:] if re.match(r'^Is[A-Z]', subject) else subject
            return 'Whether *%s* is on%s.' % (phrase(shown, title=True), where()), True
        return 'Returns the %s%s.' % (sub_plain, where()), True
    if verb == 'Set':
        vparams = [p for p in params]
        if len(vparams) == 1 and vparams[0]['type'] == 'bool':
            shown = subject[2:] if re.match(r'^Is[A-Z]', subject) else subject
            return 'Turns *%s* on or off.' % phrase(shown, title=True), True
        target = ''
        names = [p['name'] for p in vparams]
        if 'controlID' in names:
            target = ' of control `controlID`'
        elif names and (names[0] in ('index', 'i') or names[0].endswith('Index')) and len(names) > 1:
            target = ' at `%s`' % names[0]
        return 'Sets the %s%s.' % (sub_plain, target), True
    if verb == 'Is' and subject:
        words = phrase(subject)
        first = words.split()[0].lower() if words else ''
        if first in ADJECTIVES or re.search(r'(ed|able|ible|ive|ous|ful|less|ent|ant|ary|ory|ic|al)$', first):
            return 'True when the %s is %s%s.' % (noun, words, where()), False
        article = 'an' if first[:1] in 'aeiou' else 'a'
        return 'True when the %s is %s %s%s.' % (noun, article, words, where()), False
    if verb == 'Has':
        return 'True when the %s has %s%s.' % (noun, sub_plain, where()), False
    if verb == 'Can':
        return 'True when the %s can %s%s.' % (noun, sub_plain, where()), False
    if verb == 'Uses':
        return 'True when the %s uses %s.' % (noun, sub_plain), False
    return None, False


class Describer:
    def __init__(self, model, translator):
        self.model = model
        self.tr = translator
        self.overrides = load_overrides()
        self.used_overrides = set()
        self.review = []   # (key, text, source) for members described by weak rules

    def key(self, py_class, m):
        sig = ', '.join('%s: %s' % (p['name'], p['type']) for p in (m.params or []))
        return '%s.%s(%s)' % (py_class or m.module, m.name, sig)

    def method(self, py_class, m, cls_info):
        k = self.key(py_class, m)
        short = '%s.%s' % (py_class or m.module, m.name)
        for cand in (k, short):
            if cand in self.overrides:
                self.used_overrides.add(cand)
                text = self.overrides[cand]
                if text.startswith('+'):
                    d = m.decl or {}
                    ctx = self.tr.translate(d.get('lead') or d.get('group') or '')
                    return (sentence(text[1:]) + ' ' + sentence(ctx)).strip()
                return text
        d = m.decl or {}
        lead = self.tr.translate(d.get('lead') or '')
        trail = self.tr.translate(fmt_trail(d.get('trail')))
        group = self.tr.translate(d.get('group') or '')
        if m.adapter == 'IsTrue':
            return '`bool(a)`: True when the object is valid (same as `IsValid()`).'
        if m.adapter and m.adapter not in ('IsTrue', 'ctor') and not lead:
            ac = self.tr.translate(getattr(m, 'adapter_comment', '') or '')
            if ac:
                lead = re.sub(r'^[\w.]+(?:<[^>]*>)?\([^)]*\)\s*:?\s*', '', ac).strip() or ac
        auto, confident = auto_describe(m, py_class, cls_info)
        if lead:
            lead = self.structured(d, lead)
            if m.name.startswith('__') and auto:
                return join_desc(auto, lead)
            return join_desc(lead, trail)
        if group and d.get('group_owner') == m.name:
            # another overload of the documented function
            return join_desc(group, trail)
        if auto and confident:
            if group and self.same_subject(m, d):
                return join_desc(auto, group if not trail else group + ' ' + trail)
            return join_desc(auto, trail)
        if auto and group and self.same_subject(m, d):
            return join_desc(auto, group)
        if auto and m.name.startswith(('Is', 'Has', 'Can')):
            self.review.append((k, join_desc(auto, trail), 'auto-is'))
            return join_desc(auto, trail)
        if group:
            self.review.append((k, join_desc(group, trail), 'group-other'))
            return join_desc(group, trail)
        if trail:
            if auto:
                self.review.append((k, join_desc(auto, trail), 'auto+trail'))
                return join_desc(auto, trail)
            self.review.append((k, sentence(trail), 'trail-only'))
            return sentence(trail)
        if auto:
            self.review.append((k, auto, 'auto-weak'))
            return sentence(auto)
        self.review.append((k, '', 'missing'))
        return ''

    @staticmethod
    def same_subject(m, d):
        owner = d.get('group_owner')
        if not owner:
            return False
        strip = lambda n: re.sub(r'^(Get|Set|Is|Has)', '', n or '')
        return strip(owner) == strip(m.name) and owner != m.name

    def structured(self, d, lead):
        """A lead comment with list items or aligned rows keeps its lines (joined with <br>)."""
        raw = d.get('lead_raw') or []
        lines = [l for l in raw if l.strip()]
        if len(lines) < 2:
            return lead
        section = d.get('section')
        if section and lines and lines[0].strip() == section:
            lines = lines[1:]

        def row_split(s):
            m = re.match(r'^(.+?)(?:\t+|\s{3,})(?:-\s+)?(\S.*)$', s)
            if m:
                return m.group(1).strip(), m.group(2).strip()
            m = re.match(r'^(\S+(?:\s\S+)?)\s+-\s+(\S.*)$', s)
            if m:
                return m.group(1).strip(), m.group(2).strip()
            return None

        prose, items, tail = [], [], []
        pending_key = None
        for l in lines:
            s = l.strip()
            indented = l[:1] in ('\t', ' ')
            bullet = re.match(r'^(?:[-*\u2022]|\d+[.)])\s+(.*)$', s)
            if not indented and not bullet:
                (tail if items else prose).append(s)
                continue
            if pending_key is not None:
                pending_key += s
                rs = row_split(pending_key) or (pending_key.split(' - ', 1) if ' - ' in pending_key else None)
                if rs:
                    items.append('%s — %s' % (rs[0].strip(), rs[1].strip()))
                    pending_key = None
                continue
            if bullet:
                items.append(bullet.group(1) if not re.match(r'^\d', s) else s)
                continue
            rs = row_split(s)
            if rs:
                items.append('%s — %s' % rs)
            elif s.endswith('/'):
                pending_key = s
            elif items:
                items[-1] += ' ' + s
            else:
                prose.append(s)
        if pending_key:
            items.append(pending_key)
        if not items:
            return lead
        text = ' '.join(prose) + ''.join('<br>• ' + i for i in items)
        if tail:
            text += '<br>' + ' '.join(tail)
        return self.tr.translate(text.strip())

    def ctor(self, py_class, m, cls_info):
        k = '%s.__init__(%s)' % (py_class, ', '.join('%s: %s' % (p['name'], p['type']) for p in m.params))
        if k in self.overrides:
            self.used_overrides.add(k)
            return self.overrides[k]
        d = m.decl or {}
        lead = self.tr.translate(d.get('lead') or '')
        trail = self.tr.translate(fmt_trail(d.get('trail')))
        if lead:
            return join_desc(lead, trail)
        types = [p['type'] for p in m.params]
        if not m.params:
            if cls_info.get('has_fields'):
                return 'Default value (fields at their defaults).'
            if cls_info.get('static_only'):
                return 'Stateless object; every method is static and can be called on the class itself.'
            if cls_info.get('has_handle'):
                return join_desc('Creates an empty (invalid) object', trail)
            return join_desc('Creates the object', trail)
        if types == ['Handle']:
            # 'the existing existing tree' reads as 'the existing tree'
            existing = re.sub(r'^existing ', '', owner_noun(py_class))
            return join_desc('Refers to the existing %s `%s`; check `IsValid()` before use' % (existing, m.params[0]['name']), trail)
        if trail:
            return sentence(trail)
        self.review.append((k, '', 'ctor'))
        return 'Creates the value from ' + ', '.join('`%s`' % p['name'] for p in m.params) + '.'

    def field(self, py_class, f):
        k = '%s.%s' % (py_class, f.name)
        if k in self.overrides:
            self.used_overrides.add(k)
            return self.overrides[k]
        d = f.decl or {}
        lead = self.tr.translate(d.get('lead') or '')
        trail = self.tr.translate(fmt_trail(d.get('trail')))
        group = self.tr.translate(d.get('group') or '')
        if lead and trail:
            return join_desc(lead, trail)
        if lead:
            return sentence(lead)
        if trail:
            return sentence(trail)
        if group:
            return sentence(group)
        self.review.append((k, '', 'field'))
        return sentence(phrase(f.name[1:] if re.match(r'^f[A-Z]', f.name) else f.name))

    def constant(self, owner, c):
        k = '%s.%s' % (owner, c.name)
        if k in self.overrides:
            self.used_overrides.add(k)
            return self.overrides[k]
        d = c.decl or {}
        text = ' '.join(x for x in [d.get('lead') or '', fmt_trail(d.get('trail'))] if x)
        if not text and d.get('group'):
            text = d['group']
        if not text:
            self.review.append((k, '', 'constant'))
        return sentence(self.tr.translate(text)) if text else ''
