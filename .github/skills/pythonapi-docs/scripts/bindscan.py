"""Parser for the PythonAPI binding sources (Py*.cpp).

Extracts, per binding file: BindClass / BindEnum / BindAlias / BindImplicitConversion calls and the members added
through CClassBuilder / CModuleBuilder (Init, Def, Field, Constant), plus the adapter functions defined in the file.
"""

import os
import re

OPERATOR_RE = re.compile(r'operator\s*(==|!=|<=|>=|<<|>>|\+=|-=|\*=|/=|->|\(\)|\[\]|<|>|\+|-|\*|/|!|=)')
OPERATOR_TOKENS = {
    '==': 'EQ', '!=': 'NE', '<=': 'LE', '>=': 'GE', '<<': 'SHL', '>>': 'SHR', '+=': 'IADD', '-=': 'ISUB',
    '*=': 'IMUL', '/=': 'IDIV', '->': 'ARROW', '()': 'CALL', '[]': 'INDEX', '<': 'LT', '>': 'GT', '+': 'ADD',
    '-': 'SUB', '*': 'MUL', '/': 'DIV', '!': 'NOT', '=': 'ASSIGN',
}
TOKEN_OPERATORS = {v: k for k, v in OPERATOR_TOKENS.items()}


def protect_operators(text):
    return OPERATOR_RE.sub(lambda m: 'operator__' + OPERATOR_TOKENS[m.group(1)], text)


def restore_operators(text):
    return re.sub(r'operator__([A-Z]+)', lambda m: 'operator' + TOKEN_OPERATORS[m.group(1)], text)


def strip_comments(text):
    """Removes // and /* */ comments, keeping string and char literals intact."""
    out = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == '"' or c == "'":
            j = i + 1
            while j < n and text[j] != c:
                j += 2 if text[j] == '\\' else 1
            out.append(text[i:j + 1])
            i = j + 1
        elif text.startswith('//', i):
            j = text.find('\n', i)
            i = n if j < 0 else j
        elif text.startswith('/*', i):
            j = text.find('*/', i + 2)
            i = n if j < 0 else j + 2
        else:
            out.append(c)
            i += 1
    return ''.join(out)


def find_matching(text, start, open_ch, close_ch):
    """Index of the bracket closing the one at 'start' (text[start] == open_ch); string aware."""
    depth = 0
    i = start
    n = len(text)
    while i < n:
        c = text[i]
        if c == '"' or c == "'":
            j = i + 1
            while j < n and text[j] != c:
                j += 2 if text[j] == '\\' else 1
            i = j + 1
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError('unbalanced %s at %d' % (open_ch, start))


def find_angle_close(text, start):
    """text[start] == '<'. Returns the index of the matching '>' (parentheses are skipped as a whole)."""
    depth = 0
    i = start
    n = len(text)
    while i < n:
        c = text[i]
        if c == '(':
            i = find_matching(text, i, '(', ')') + 1
            continue
        if c == '<':
            depth += 1
        elif c == '>':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError('unbalanced < at %d' % start)


def split_top(text, sep=','):
    """Splits at top level separators (outside (), {}, [], <> and literals)."""
    parts = []
    depth = 0
    angle = 0
    cur = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c == '"' or c == "'":
            j = i + 1
            while j < n and text[j] != c:
                j += 2 if text[j] == '\\' else 1
            cur.append(text[i:j + 1])
            i = j + 1
            continue
        if c in '({[':
            depth += 1
        elif c in ')}]':
            depth -= 1
        elif c == '<':
            # template bracket when preceded by an identifier character
            k = len(''.join(cur).rstrip())
            prev = ''.join(cur).rstrip()[-1:] if k else ''
            if prev and (prev.isalnum() or prev in '_:'):
                angle += 1
        elif c == '>' and angle > 0:
            angle -= 1
        if c == sep and depth == 0 and angle == 0:
            parts.append(''.join(cur).strip())
            cur = []
        else:
            cur.append(c)
        i += 1
    tail = ''.join(cur).strip()
    if tail or parts:
        parts.append(tail)
    return parts


def unescape_c(s):
    return (s.replace('\\\\', '\x00').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
            .replace('\\"', '"').replace("\\'", "'").replace('\x00', '\\'))


def concat_strings(expr):
    """Concatenates adjacent C string literals: '"a" "b"' -> 'ab'. Returns None when expr is not a literal."""
    parts = re.findall(r'"((?:[^"\\]|\\.)*)"', expr)
    rest = re.sub(r'"((?:[^"\\]|\\.)*)"', '', expr).strip()
    if not parts or rest:
        return None
    return unescape_c(''.join(parts))


def parse_sargs(text):
    """'{ SArg("a"), SArg("b", 1.0) }' -> [{'name': 'a', 'default': None}, {'name': 'b', 'default': '1.0'}]"""
    text = text.strip()
    if text.startswith('{'):
        text = text[1:text.rfind('}')]
    args = []
    for part in split_top(text):
        if not part:
            continue
        m = re.match(r'(SArg|ArgText|ArgI16|ArgI32)\s*\((.*)\)\s*$', part, re.S)
        if not m:
            raise ValueError('not an SArg: ' + part)
        inner = split_top(m.group(2))
        name = concat_strings(inner[0])
        default = ','.join(inner[1:]).strip() if len(inner) > 1 else None
        if m.group(1) == 'ArgText':
            default = 'std::string{}'
        elif m.group(1) == 'ArgI16':
            default = 'std::int16_t(%s)' % default
        elif m.group(1) == 'ArgI32':
            default = 'std::int32_t(%s)' % default
        args.append({'name': name, 'default': default})
    return args


def parse_fn_ref(expr):
    """Parses the template argument of kFn / kSelfFn.

    Returns dict(target=<qualified name>, sig=<static_cast signature or None>).
    """
    expr = expr.strip()
    sig = None
    if expr.startswith('static_cast<'):
        close = find_angle_close(expr, len('static_cast'))
        sig = expr[len('static_cast<'):close].strip()
        rest = expr[close + 1:].strip()
        if rest.startswith('('):
            rest = rest[1:find_matching(rest, 0, '(', ')')]
        expr = rest.strip()
    target = expr.lstrip('&').strip()
    return {'target': restore_operators(target), 'sig': restore_operators(sig) if sig else None}


def parse_signature(sig):
    """'R (C::*)(P1, P2) const' or 'R (*)(P1)' -> dict(ret, owner, params, const)."""
    m = re.search(r'\(\s*(?:([\w:]+)::)?\*\s*\)', sig)
    if not m:
        raise ValueError('bad signature: ' + sig)
    ret = sig[:m.start()].strip()
    rest = sig[m.end():].strip()
    close = find_matching(rest, 0, '(', ')')
    params = [p for p in split_top(rest[1:close]) if p]
    suffix = rest[close + 1:].strip()
    return {'ret': ret, 'owner': m.group(1), 'params': params, 'const': 'const' in suffix.split()}


class BindingFile:
    def __init__(self, path, root):
        self.path = path
        self.rel = os.path.relpath(path, root).replace('\\', '/')
        self.folder = os.path.dirname(self.rel) or '.'
        with open(path, encoding='utf-8-sig', errors='replace') as f:
            self.raw = f.read()
        self.code = protect_operators(strip_comments(self.raw))
        self.includes = re.findall(r'#include\s+"([^"]+)"', self.raw)
        self.classes = []        # BindClass calls
        self.enums = []          # BindEnum calls
        self.aliases = []
        self.implicit = []
        self.members = []        # (builder cpp type or module, kind, data) in order
        self.adapters = {}       # adapter functions defined in this file
        self.local_consts = {}   # 'kFirst' -> '0'
        self.call_order = []     # Define*/BindTypes call order within the file (informational)

    # ------------------------------------------------------------------------------------------------------------
    def parse(self):
        self.using_list = [(m.start(), m.group(1), m.group(2).strip()) for m in re.finditer(r'\busing\s+(\w+)\s*=\s*([^;]+);', self.code)]
        self.local_usings = {name: target for _, name, target in self.using_list}
        self.define_fns = [(m.start(), m.group(1)) for m in re.finditer(r'void\s+CPy\w+::(Define\w*)\s*\(', self.code)]
        self._parse_local_consts()
        self._parse_adapters()
        self._parse_bind_class()
        self._parse_bind_enum()
        self._parse_aliases()
        self._parse_builders()
        return self

    def _parse_local_consts(self):
        for m in re.finditer(r'const\s+([\w:<>]+)\s+(k\w+)\s*(?:=\s*([^;]+))?;', self.code):
            self.local_consts[m.group(2)] = {'type': m.group(1), 'value': (m.group(3) or '').strip()}

    def _parse_adapters(self):
        """Free functions in the anonymous namespace (used as kFn / kSelfFn targets)."""
        raw = protect_operators(self.raw)
        m = re.search(r'namespace\s*\n?\s*\{', raw)
        if not m:
            return
        start = raw.find('{', m.start())
        end = find_matching(raw, start, '{', '}')
        body = raw[start + 1:end]
        lines = body.split('\n')
        # Walk top level definitions of the anonymous namespace.
        code = strip_comments(body)
        pos = 0
        while True:
            fm = re.compile(r'(?m)^\t(?!\t)([^\n;{}]*?)\b(\w+)\s*\(').search(code, pos)
            if not fm:
                break
            ret = fm.group(1).strip()
            name = fm.group(2)
            if ret.startswith('class') or ret.startswith('struct') or name in ('if', 'for', 'while', 'switch', 'return'):
                # skip a class definition body
                brace = code.find('{', fm.end())
                pos = (find_matching(code, brace, '{', '}') + 1) if brace >= 0 else fm.end()
                continue
            open_paren = fm.end() - 1
            close_paren = find_matching(code, open_paren, '(', ')')
            params = [p.strip() for p in split_top(code[open_paren + 1:close_paren]) if p.strip()]
            after = code[close_paren + 1:]
            brace_rel = after.find('{')
            semi_rel = after.find(';')
            if brace_rel < 0 or (0 <= semi_rel < brace_rel):
                pos = close_paren + 1
                continue
            brace = close_paren + 1 + brace_rel
            end_body = find_matching(code, brace, '{', '}')
            # leading comment: find in the raw lines
            comment = self._leading_comment(body, name)
            if ret and name not in self.adapters:
                self.adapters[name] = {'ret': restore_operators(ret), 'params': [restore_operators(p) for p in params],
                                       'comment': comment, 'body': code[brace:end_body + 1]}
            pos = end_body + 1

    @staticmethod
    def _leading_comment(body, name):
        lines = body.split('\n')
        for i, line in enumerate(lines):
            if re.match(r'^\t(?!\t)[^/\n]*\b' + re.escape(name) + r'\s*\(', line):
                j = i - 1
                block = []
                while j >= 0 and lines[j].strip().startswith('//'):
                    block.insert(0, lines[j].strip()[2:].strip())
                    j -= 1
                return ' '.join(block)
        return ''

    def _calls(self, keyword):
        """Yields (template_args, args_text, start) for every 'keyword<...>(...)'."""
        for m in re.finditer(r'\b' + keyword + r'\s*<', self.code):
            lt = self.code.index('<', m.start())
            gt = find_angle_close(self.code, lt)
            tmpl = self.code[lt + 1:gt]
            p = gt + 1
            while self.code[p].isspace():
                p += 1
            if self.code[p] != '(':
                continue
            close = find_matching(self.code, p, '(', ')')
            yield tmpl, self.code[p + 1:close], m.start()

    def _parse_bind_class(self):
        for tmpl, args, pos in self._calls('BindClass'):
            targs = split_top(tmpl)
            a = split_top(args)
            if len(a) < 4:
                continue
            self.classes.append({
                'cpp': self.resolve_local(targs[0].strip(), pos),
                'base': self.resolve_local(targs[1].strip(), pos) if len(targs) > 1 else None,
                'parent': a[0].strip(),
                'module': concat_strings(a[1]),
                'qualname': concat_strings(a[2]),
                'doc': concat_strings(','.join(a[3:])) or '',
                'pos': pos,
                'file': self.rel,
            })

    def _parse_bind_enum(self):
        for tmpl, args, pos in self._calls('BindEnum'):
            a = split_top(args)
            values = []
            init = a[4].strip()
            init = init[1:init.rfind('}')]
            for entry in split_top(init):
                if not entry:
                    continue
                inner = entry.strip()
                inner = inner[1:inner.rfind('}')]
                name, val = split_top(inner)
                values.append({'name': concat_strings(name), 'cpp': val.strip()})
            self.enums.append({
                'cpp': self.resolve_local(tmpl.strip(), pos),
                'parent': a[0].strip(),
                'module': concat_strings(a[1]),
                'qualname': concat_strings(a[2]),
                'flag': a[3].strip() == 'true',
                'values': values,
                'pos': pos,
                'file': self.rel,
            })

    def _parse_aliases(self):
        for m in re.finditer(r'BindAlias\s*\(\s*(\w+)\s*,\s*"([^"]+)"\s*,\s*ClassObject<([^>]+)>\(\)\s*\)', self.code):
            self.aliases.append({'parent': m.group(1), 'name': m.group(2), 'cpp': m.group(3).strip()})
        for tmpl, args, pos in self._calls('BindImplicitConversion'):
            f, t = split_top(tmpl)
            self.implicit.append({'from': f.strip(), 'to': t.strip()})

    def _parse_builders(self):
        builders = {}
        events = []
        for m in re.finditer(r'CClassBuilder\s+(\w+)\s*=\s*Builder\s*<', self.code):
            lt = self.code.index('<', m.end() - 1)
            gt = find_angle_close(self.code, lt)
            events.append((m.start(), 'class', m.group(1), self.code[lt + 1:gt].strip()))
        for m in re.finditer(r'CModuleBuilder\s+(\w+)\s*\(\s*(\w+)\s*\)', self.code):
            events.append((m.start(), 'module', m.group(1), m.group(2)))
        for m in re.finditer(r'\b(\w+)\s*\.\s*(Init|Def|Field|Constant)\s*\(', self.code):
            p = m.end() - 1
            close = find_matching(self.code, p, '(', ')')
            events.append((m.start(), 'member', m.group(1), (m.group(2), self.code[p + 1:close])))
        events.sort(key=lambda e: e[0])
        for pos, kind, var, data in events:
            if kind in ('class', 'module'):
                builders[var] = (kind, self.resolve_local(data, pos) if kind == 'class' else data)
                continue
            if var not in builders:
                raise ValueError('%s: unknown builder %s' % (self.rel, var))
            bkind, owner = builders[var]
            what, args = data
            self.members.append(self._parse_member(bkind, owner, what, args, pos))

    def resolve_local(self, name, pos=None):
        """Applies the binding file's local 'using' aliases to a C++ name (TDlg::Run -> CLayoutDialog::Run)."""
        head, sep, tail = name.partition('::')
        target = None
        for upos, uname, utarget in self.using_list:
            if uname == head and (pos is None or upos <= pos):
                target = utarget
        if target is not None:
            return target + sep + tail
        return name

    def _define_fn_at(self, pos):
        current = None
        for start, name in self.define_fns:
            if start <= pos:
                current = name
        return current

    def _parse_member(self, bkind, owner, what, args, pos):
        a = split_top(args)
        rec = {'builder': bkind, 'owner': owner, 'kind': what, 'pos': pos, 'file': self.rel,
               'define_fn': self._define_fn_at(pos)}
        if what == 'Init':
            first = a[0]
            m = re.match(r'(kCtor|kAdapterCtor)\s*<(.*)>\s*$', first, re.S)
            targs = [t.strip() for t in split_top(m.group(2))]
            if m.group(1) == 'kCtor':
                rec['ctor_class'] = self.resolve_local(targs[0], pos)
                rec['params'] = targs[1:]
            else:
                rec['ctor_class'] = self.resolve_local(targs[0], pos)
                rec['adapter_store'] = targs[1]
                rec['params'] = targs[2:]
            rec['args'] = parse_sargs(','.join(a[1:])) if len(a) > 1 else []
        elif what == 'Def':
            first = a[0]
            m = re.match(r'(kFn|kSelfFn)\s*<(.*)>\s*$', first, re.S)
            if not m:
                raise ValueError('bad Def: ' + first)
            rec['self_first'] = m.group(1) == 'kSelfFn'
            rec.update(parse_fn_ref(m.group(2)))
            rec['target'] = self.resolve_local(rec['target'], pos)
            rec['name'] = concat_strings(a[1])
            rec['args'] = parse_sargs(','.join(a[2:])) if len(a) > 2 else []
        elif what == 'Field':
            m = re.match(r'kField\s*<\s*&(.*)>\s*$', a[0], re.S)
            rec['target'] = self.resolve_local(m.group(1).strip(), pos)
            rec['name'] = concat_strings(a[1])
        elif what == 'Constant':
            rec['name'] = concat_strings(a[0])
            rec['value'] = ','.join(a[1:]).strip()
        return rec


def scan(root):
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        if os.path.basename(dirpath) == 'Binding':
            continue
        for fn in sorted(filenames):
            if fn.endswith('.cpp'):
                files.append(BindingFile(os.path.join(dirpath, fn), root).parse())
    return files


if __name__ == '__main__':
    import json
    import sys
    root = sys.argv[1]
    result = scan(root)
    total = {'classes': 0, 'enums': 0, 'members': 0, 'adapters': 0}
    for bf in result:
        total['classes'] += len(bf.classes)
        total['enums'] += len(bf.enums)
        total['members'] += len(bf.members)
        total['adapters'] += len(bf.adapters)
    print(json.dumps(total))
    kinds = {}
    for bf in result:
        for mem in bf.members:
            kinds[mem['kind']] = kinds.get(mem['kind'], 0) + 1
    print(kinds)
    for bf in result:
        if bf.adapters:
            print(bf.rel, sorted(bf.adapters))
