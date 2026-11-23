import re

TOKEN_RE = re.compile(r'''
    (?P<ws>\s+)
  | (?P<lcomment>//[^\n]*)
  | (?P<bcomment>/\*.*?\*/)
  | (?P<raw>u8?R"(?P<delim>[^(\s]*)\((?P<rawbody>.*?)\)(?P=delim)")
  | (?P<str>(?:u8)?"(?:\\.|[^"\\\n])*")
  | (?P<chr>'(?:\\.|[^'\\\n])*')
  | (?P<num>\d+(?:\.\d*)?(?:[eE][+-]?\d+)?[fFuUlL]*|\.\d+(?:[eE][+-]?\d+)?[fF]?)
  | (?P<ident>[A-Za-z_]\w*)
  | (?P<op>::|->|<<|>>|<=|>=|==|!=|&&|\|\||[{}()\[\];,<>=+\-*/&|!?:.%^~#])
''', re.S | re.X)


def unescape(s):
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s):
            n = s[i + 1]
            m = {'n': '\n', 't': '\t', '"': '"', "'": "'", '\\': '\\', 'r': '\r', '0': '\0'}
            if n in m:
                out.append(m[n]); i += 2; continue
            if n == 'x':
                j = i + 2
                h = ''
                while j < len(s) and s[j] in '0123456789abcdefABCDEF':
                    h += s[j]; j += 1
                out.append(chr(int(h, 16))); i = j; continue
            out.append(n); i += 2; continue
        out.append(c); i += 1
    return ''.join(out)


class Tok:
    __slots__ = ('kind', 'val', 'pos')

    def __init__(self, kind, val, pos):
        self.kind, self.val, self.pos = kind, val, pos

    def __repr__(self):
        return f'{self.kind}:{self.val!r}'


def tokenize(text):
    toks = []
    pos = 0
    n = len(text)
    while pos < n:
        m = TOKEN_RE.match(text, pos)
        if not m:
            raise SyntaxError(f'cannot tokenize at {pos}: {text[pos:pos+40]!r}')
        k = m.lastgroup
        if k in ('ws', 'lcomment', 'bcomment'):
            pass
        elif k == 'raw':
            toks.append(Tok('str', m.group('rawbody'), pos))
        elif k == 'delim' or k == 'rawbody':
            toks.append(Tok('str', m.group('rawbody'), pos))
        elif k == 'str':
            v = m.group('str')
            if v.startswith('u8'):
                v = v[2:]
            toks.append(Tok('str', unescape(v[1:-1]), pos))
        elif k == 'chr':
            toks.append(Tok('chr', m.group('chr'), pos))
        elif k == 'num':
            toks.append(Tok('num', m.group('num'), pos))
        elif k == 'ident':
            toks.append(Tok('ident', m.group('ident'), pos))
        else:
            toks.append(Tok('op', m.group('op'), pos))
        pos = m.end()
    # merge adjacent string literals
    merged = []
    for t in toks:
        if t.kind == 'str' and merged and merged[-1].kind == 'str':
            merged[-1] = Tok('str', merged[-1].val + t.val, merged[-1].pos)
        else:
            merged.append(t)
    return merged


def strip_preprocessor(text):
    # remove preprocessor lines (#include, #pragma, ...) incl. continuation lines
    out = []
    cont = False
    for line in text.split('\n'):
        s = line.lstrip()
        if cont or s.startswith('#'):
            cont = line.rstrip().endswith('\\')
            out.append('')
            continue
        out.append(line)
    return '\n'.join(out)


def match_close(toks, i):
    """toks[i] is an opening bracket; return index of the matching close."""
    pairs = {'(': ')', '{': '}', '[': ']'}
    stack = [pairs[toks[i].val]]
    j = i + 1
    while j < len(toks):
        v = toks[j].val if toks[j].kind == 'op' else None
        if v in pairs:
            stack.append(pairs[v])
        elif v in (')', '}', ']'):
            if v != stack[-1]:
                raise SyntaxError(f'mismatched {v} at token {j}')
            stack.pop()
            if not stack:
                return j
        j += 1
    raise SyntaxError('unclosed')


def split_args(toks, i, j):
    """Split toks[i:j] at top-level commas."""
    args = []
    cur = []
    depth = 0
    k = i
    while k < j:
        t = toks[k]
        if t.kind == 'op' and t.val in '({[':
            depth += 1
        elif t.kind == 'op' and t.val in ')}]':
            depth -= 1
        if depth == 0 and t.kind == 'op' and t.val == ',':
            args.append(cur); cur = []
        else:
            cur.append(t)
        k += 1
    if cur:
        args.append(cur)
    return args
