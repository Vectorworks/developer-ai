"""Extracts the catalog of the MCP tool groups from a Vectorworks source tree.

Evaluates every group definition (the DefineGroup bodies under MCP/) with a small interpreter of the C++ subset they
use, and writes a JSON list of groups: fName, fDesc, fActiveByDefault, fSafetyLevel, groupId, folder, class and tools
[{name, effect, description, inputSchema, file, handlerFile}]. 'class', 'file' and 'handlerFile' are for the checks
only and never appear on the pages.

Usage: python extract.py --source "<tree>/Interfaces/VectorWorks" --out catalog.json
"""
import os, sys, json, glob, re
sys.path.insert(0, os.path.dirname(__file__))
from cpptok import tokenize, strip_preprocessor, match_close, split_args, Tok

ROOT = None       # <source>/MCP, set by extract()


class EvalError(Exception):
    pass


class InitList:
    def __init__(self, items):
        self.items = items

    def __repr__(self):
        return f'InitList({self.items!r})'


class Lambda:
    def __init__(self, params, body, interp):
        self.params, self.body, self.interp = params, body, interp


class Ref:
    """Reference to a named value (for &x / *x / range-for over pointers)."""


class Unknown:
    def __init__(self, what):
        self.what = what

    def __repr__(self):
        return f'Unknown({self.what})'


def to_json(v):
    if isinstance(v, InitList):
        items = v.items
        if items and all(isinstance(e, InitList) and len(e.items) == 2 and isinstance(to_json_scalar(e.items[0]), str) for e in items):
            d = {}
            for e in items:
                d[to_json(e.items[0])] = to_json(e.items[1])
            return d
        if not items:
            return None
        return [to_json(e) for e in items]
    if isinstance(v, dict):
        return {k: to_json(x) for k, x in v.items()}
    if isinstance(v, list):
        return [to_json(x) for x in v]
    return v


def to_json_scalar(v):
    return v if not isinstance(v, InitList) else None


def deep_copy(v):
    return json.loads(json.dumps(v)) if not isinstance(v, (InitList, Lambda, Unknown)) else v


# ---------------------------------------------------------------- global symbol tables
ENUM_TABLES = {}      # name -> list of names
STR_ARRAYS = {}       # name -> list of strings
GLOBAL_DEFS = {}      # name -> (tokens of expression, file)
GLOBAL_NUMS = {}      # name -> number
API_ROOT = None       # <source>/API/Resources, set by extract()
API_TABLES = {}       # kResourceTypeNames / kContentFolderNames / kFieldTypeNames -> names
API_LISTS = {
    'GetAllTypes': 'kResourceTypeNames',
    'GetAllContentFolders': 'kContentFolderNames',
    'GetAllFieldTypes': 'kFieldTypeNames',
}
API_IDENTITY = {'GetTypeName', 'GetContentFolderName', 'GetFieldTypeName'}


class KV:
    def __init__(self, k, v):
        self.k, self.v = k, v
FUNCS = {}            # name -> (param tokens, body tokens, file)
FILE_TOKS = {}


def find_stmt_end(toks, i):
    depth = 0
    while i < len(toks):
        t = toks[i]
        if t.kind == 'op':
            if t.val in '({[':
                depth += 1
            elif t.val in ')}]':
                depth -= 1
            elif t.val == ';' and depth == 0:
                return i
        i += 1
    return i


def collect_api_tables():
    for f in glob.glob(os.path.join(API_ROOT, '*.cpp')):
        toks = tokenize(strip_preprocessor(open(f, encoding='utf-8-sig', errors='replace').read()))
        for i, t in enumerate(toks):
            if t.kind == 'ident' and t.val in API_LISTS.values() and toks[i + 1].val == '[' and toks[i + 2].val == ']':
                k = i + 3
                while toks[k].val != '{':
                    k += 1
                e = match_close(toks, k)
                names = []
                for a in split_args(toks, k + 1, e):
                    strs = [x.val for x in a if x.kind == 'str']
                    if strs:
                        names.append(strs[-1])
                API_TABLES[t.val] = names


def collect_globals():
    collect_api_tables()
    files = glob.glob(os.path.join(ROOT, '**', '*.h'), recursive=True) + glob.glob(os.path.join(ROOT, '**', '*.cpp'), recursive=True)
    for p in files:
        text = strip_preprocessor(open(p, encoding='utf-8-sig', errors='replace').read())
        toks = tokenize(text)
        FILE_TOKS[p] = toks
        n = len(toks)
        for i in range(n):
            t = toks[i]
            # constexpr double NAME = NUM;
            if t.kind == 'ident' and t.val == 'constexpr' and i + 4 < n and toks[i + 1].val in ('double', 'int', 'float', 'size_t', 'short', 'long') \
                    and toks[i + 2].kind == 'ident' and toks[i + 3].val == '=' and toks[i + 4].kind == 'num':
                s = toks[i + 4].val.rstrip('fFuUlL')
                GLOBAL_NUMS[toks[i + 2].val] = float(s) if ('.' in s or 'e' in s.lower()) else int(s)
            # SPopupName NAME[] = { { "Label", "name" }, ... };
            if t.kind == 'ident' and t.val == 'SPopupName' and i + 2 < n and toks[i + 1].kind == 'ident' and toks[i + 2].val == '[':
                k = i + 2
                while toks[k].val != '{':
                    k += 1
                e = match_close(toks, k)
                names = []
                for a in split_args(toks, k + 1, e):
                    strs = [x.val for x in a if x.kind == 'str']
                    if strs:
                        names.append(strs[-1])
                ENUM_TABLES[toks[i + 1].val] = names
            # SEnumName<...> NAME[] = { ... };
            if t.kind == 'ident' and t.val == 'SEnumName' and i + 1 < n and toks[i + 1].val == '<':
                j = i + 2
                depth = 1
                while depth:
                    if toks[j].val == '<': depth += 1
                    elif toks[j].val == '>': depth -= 1
                    elif toks[j].val == '>>': depth -= 2
                    j += 1
                if toks[j].kind == 'ident' and toks[j + 1].val == '[':
                    name = toks[j].val
                    k = j + 1
                    while toks[k].val != '{':
                        k += 1
                    e = match_close(toks, k)
                    names = []
                    for a in split_args(toks, k + 1, e):
                        strs = [x.val for x in a if x.kind == 'str']
                        if strs:
                            names.append(strs[-1])
                    ENUM_TABLES[name] = names
            # const char* NAME[] = { "a", ... };
            if t.kind == 'ident' and t.val == 'char' and i + 3 < n and toks[i + 1].val == '*':
                k = i + 2
                if toks[k].kind == 'ident' and toks[k].val == 'const':
                    k += 1
                if toks[k].kind == 'ident' and toks[k + 1].val == '[':
                    name = toks[k].val
                    m = k + 1
                    while m < n and toks[m].val not in ('{', ';'):
                        m += 1
                    if toks[m].val == '{':
                        e = match_close(toks, m)
                        STR_ARRAYS[name] = [x.val for x in toks[m + 1:e] if x.kind == 'str']
        # function definitions (any 'IDENT ( ... ) {' at brace depth of a namespace)
        i = 0
        while i < n:
            t = toks[i]
            if t.kind == 'ident' and i + 1 < n and toks[i + 1].val == '(':
                try:
                    c = match_close(toks, i + 1)
                except SyntaxError:
                    i += 1
                    continue
                k = c + 1
                while k < n and toks[k].kind == 'ident' and toks[k].val in ('const', 'noexcept', 'override'):
                    k += 1
                if k < n and toks[k].val == '{' and (i == 0 or toks[i - 1].kind in ('ident', 'op') and toks[i - 1].val not in ('=', ',', '(', 'return', 'new')):
                    prev = toks[i - 1].val if i else ''
                    if prev in ('if', 'while', 'for', 'switch') or toks[i].val in ('if', 'while', 'for', 'switch', 'catch'):
                        i += 1
                        continue
                    e = match_close(toks, k)
                    name = t.val
                    if i >= 2 and toks[i - 1].val == '::':
                        name = toks[i - 2].val + '::' + t.val
                    FUNCS.setdefault(name, []).append((toks[i + 2:c], toks[k + 1:e], p))
                    i = e + 1
                    continue
            i += 1
        # file/namespace-scope json constants: 'json NAME = ...;' outside function bodies
        depth_fn = 0
        i = 0
        while i < n:
            t = toks[i]
            if t.kind == 'ident' and t.val == 'json' and i + 2 < n and toks[i + 1].kind == 'ident' and toks[i + 2].val in ('=', '{'):
                name = toks[i + 1].val
                if toks[i + 2].val == '=':
                    e = find_stmt_end(toks, i + 3)
                    GLOBAL_DEFS.setdefault(name, []).append((toks[i + 3:e], p))
                else:
                    e = match_close(toks, i + 2)
                    GLOBAL_DEFS.setdefault(name, []).append((toks[i + 2:e + 1], p))
            i += 1


# ---------------------------------------------------------------- interpreter
BUILTIN_SCHEMA = {
    'kString': {'type': 'string'},
    'kNumber': {'type': 'number'},
    'kBoolean': {'type': 'boolean'},
    'kInteger': {'type': 'integer'},
}


class Interp:
    def __init__(self, file, registry):
        self.file = file
        self.scopes = [{}]
        self.registry = registry

    # scope -----------------------------------------------------------
    def lookup(self, name):
        for s in reversed(self.scopes):
            if name in s:
                return s[name]
        if name in ENUM_TABLES:
            return ('enumtable', ENUM_TABLES[name])
        if name in GLOBAL_NUMS:
            return GLOBAL_NUMS[name]
        if name in STR_ARRAYS:
            return list(STR_ARRAYS[name])
        if name in GLOBAL_DEFS:
            defs = GLOBAL_DEFS[name]
            same = [d for d in defs if os.path.dirname(d[1]) == os.path.dirname(self.file)] or [d for d in defs if 'Common' in d[1]] or defs
            toks, f = same[0]
            sub = Interp(f, self.registry)
            v = sub.eval_tokens(toks)
            return to_json(v)
        raise EvalError(f'unknown name {name}')

    def set(self, name, v):
        for s in reversed(self.scopes):
            if name in s:
                s[name] = v
                return
        self.scopes[-1][name] = v

    # expressions -----------------------------------------------------
    def eval_tokens(self, toks):
        self.toks = toks
        self.i = 0
        v = self.expr()
        if self.i != len(toks):
            raise EvalError(f'trailing tokens: {toks[self.i:self.i+8]}')
        return v

    def peek(self, off=0):
        k = self.i + off
        return self.toks[k] if k < len(self.toks) else Tok('eof', None, -1)

    def take(self, val=None):
        t = self.peek()
        if val is not None and t.val != val:
            raise EvalError(f'expected {val} got {t}')
        self.i += 1
        return t

    def expr(self):
        v = self.unary()
        while self.peek().kind == 'op' and self.peek().val == '+':
            self.take()
            r = self.unary()
            v = v + r
        if self.peek().kind == 'op' and self.peek().val in ('==', '!='):
            op = self.take().val
            r = self.unary()
            if isinstance(v, tuple) and v[0] == 'find' and isinstance(r, tuple) and r[0] == 'iter':
                eq = not v[1]
            else:
                eq = to_json(v) == to_json(r)
            v = eq if op == '==' else not eq
        if self.peek().kind == 'op' and self.peek().val == '?':
            raise EvalError('ternary not supported')
        return v

    def unary(self):
        t = self.peek()
        if t.kind == 'op' and t.val in ('&', '*'):
            self.take()
            return self.unary()
        if t.kind == 'op' and t.val == '-':
            self.take()
            return -self.unary()
        return self.postfix(self.primary())

    def args(self):
        self.take('(')
        start = self.i
        depth = 1
        j = self.i
        while depth:
            v = self.toks[j].val if self.toks[j].kind == 'op' else None
            if v in ('(', '{', '['):
                depth += 1
            elif v in (')', '}', ']'):
                depth -= 1
            j += 1
        end = j - 1
        parts = split_args(self.toks, start, end)
        vals = []
        for p in parts:
            sub = Interp(self.file, self.registry)
            sub.scopes = self.scopes
            vals.append(sub.eval_tokens(p))
        self.i = end + 1
        return vals

    def initlist(self):
        self.take('{')
        start = self.i
        save_i = self.i
        # find match
        depth = 1
        j = self.i
        while depth:
            v = self.toks[j].val if self.toks[j].kind == 'op' else None
            if v in ('(', '{', '['):
                depth += 1
            elif v in (')', '}', ']'):
                depth -= 1
            j += 1
        end = j - 1
        parts = split_args(self.toks, start, end)
        vals = []
        for p in parts:
            sub = Interp(self.file, self.registry)
            sub.scopes = self.scopes
            vals.append(sub.eval_tokens(p))
        self.i = end + 1
        return InitList(vals)

    def qualified_name(self):
        parts = [self.take().val]
        while self.peek().val == '::' and self.peek(1).kind == 'ident':
            self.take()
            parts.append(self.take().val)
        # template args like std::vector<std::string>
        if self.peek().val == '<' and parts[-1] in ('vector', 'array', 'string'):
            depth = 0
            while True:
                t = self.take()
                if t.val == '<': depth += 1
                elif t.val == '>': depth -= 1
                elif t.val == '>>': depth -= 2
                if depth <= 0:
                    break
        return '::'.join(parts)

    def primary(self):
        t = self.peek()
        if t.kind == 'str':
            self.take()
            return t.val
        if t.kind == 'num':
            self.take()
            s = t.val.rstrip('fFuUlL')
            return float(s) if ('.' in s or 'e' in s.lower()) else int(s)
        if t.kind == 'op' and t.val == '{':
            return self.initlist()
        if t.kind == 'op' and t.val == '(':
            self.take()
            v = self.expr()
            self.take(')')
            return v
        if t.kind == 'op' and t.val == '[':
            # lambda
            e = match_close(self.toks, self.i)
            self.i = e + 1
            params = []
            if self.peek().val == '(':
                c = match_close(self.toks, self.i)
                for a in split_args(self.toks, self.i + 1, c):
                    # last identifier before '=' is the param name; default after '='
                    names = [x for x in a]
                    eq = next((k for k, x in enumerate(names) if x.val == '='), None)
                    decl = names[:eq] if eq is not None else names
                    pname = [x.val for x in decl if x.kind == 'ident'][-1]
                    default = names[eq + 1:] if eq is not None else None
                    params.append((pname, default))
                self.i = c + 1
            while self.peek().val != '{':
                self.take()
            c = match_close(self.toks, self.i)
            body = self.toks[self.i + 1:c]
            self.i = c + 1
            return Lambda(params, body, self)
        if t.kind == 'ident':
            if t.val in ('true', 'false'):
                self.take()
                return t.val == 'true'
            if t.val == 'nullptr':
                self.take()
                return None
            name = self.qualified_name()
            if self.peek().val == '(':
                return self.call(name)
            if self.peek().val == '{' and name in ('json', 'nlohmann::json'):
                v = self.initlist()
                return v
            if name in BUILTIN_SCHEMA:
                return dict(BUILTIN_SCHEMA[name])
            if name.startswith('Schema::'):
                name = name[len('Schema::'):]
                if name in BUILTIN_SCHEMA:
                    return dict(BUILTIN_SCHEMA[name])
            return self.lookup(name)
        raise EvalError(f'unexpected token {t}')

    def postfix(self, v):
        while True:
            t = self.peek()
            if t.kind == 'op' and t.val == '[':
                self.take()
                k = self.expr()
                self.take(']')
                v = to_json(v)[k]
            elif t.kind == 'op' and t.val == '.' and self.peek(1).kind == 'ident':
                self.take()
                m = self.take().val
                a = self.args() if self.peek().val == '(' else []
                v = self.method(v, m, a)
            else:
                return v

    def method(self, v, m, a):
        if m == 'end' or m == 'begin':
            return ('iter', m, v)
        if isinstance(v, KV) and m == 'key':
            return v.k
        if isinstance(v, KV) and m == 'value':
            return v.v
        if m == 'fName' and isinstance(v, str):
            return v
        if m == 'empty':
            v = to_json(v)
            return not v
        raise EvalError(f'method {m} in expression')

    def call(self, name):
        if name in ('std::move', 'move'):
            a = self.args()
            return a[0]
        a = self.args()
        return self.call_func(name, a)

    def call_func(self, name, a):
        short = name.split('::')[-1]
        if short in API_LISTS:
            return list(API_TABLES[API_LISTS[short]])
        if short in API_IDENTITY:
            return a[0]
        if short == 'ObjectSchema':
            s = {'type': 'object', 'properties': to_json(a[0]) or {}}
            if len(a) > 1:
                r = to_json(a[1])
                if r:
                    s['required'] = r
            return s
        if short == 'EnumSchema':
            return {'type': 'string', 'enum': list(to_json(a[0]))}
        if short == 'EnumNamesSchema':
            tbl = a[0]
            assert tbl[0] == 'enumtable'
            return {'type': 'string', 'enum': list(tbl[1])}
        if short in ('EnumNames', 'PopupNames'):
            return list(a[0][1])
        if name in ('std::find', 'find'):
            return ('find', to_json(a[2]) in to_json(a[0][2]))
        if short == 'ChoicesSchema':
            return {'type': 'string', 'enum': list(to_json(a[0]))}
        if short == 'WithCreateOptions':
            s = deep_copy(to_json(a[0]))
            s.setdefault('properties', {})
            s['properties']['class'] = {'type': 'string'}
            s['properties']['name'] = {'type': 'string'}
            s['properties']['select'] = {'type': 'boolean'}
            s['properties']['useClassAttributes'] = {'type': 'boolean'}
            return s
        if short == 'WithProperties':
            d = deep_copy(to_json(a[0])) or {}
            for k, x in (to_json(a[1]) or {}).items():
                d[k] = x
            return d
        if name in ('json::array', 'nlohmann::json::array'):
            if not a:
                return []
            v = to_json(a[0])
            return v if isinstance(v, list) else ([] if v is None else [v])
        if name in ('json::object', 'nlohmann::json::object'):
            if not a:
                return {}
            return to_json(a[0]) or {}
        if name in ('json', 'nlohmann::json'):
            return to_json(a[0]) if a else None
        if name.endswith('vector') or name in ('std::string', 'string'):
            return to_json(a[0]) if a else []
        v = None
        try:
            v = self.lookup(name)
        except EvalError:
            pass
        if isinstance(v, Lambda):
            return self.invoke_lambda(v, a)
        if short in FUNCS:
            return self.invoke_func(short, a)
        raise EvalError(f'unknown function {name}')

    def invoke_lambda(self, lam, a):
        scope = {}
        for idx, (pname, default) in enumerate(lam.params):
            if idx < len(a):
                scope[pname] = a[idx]
            elif default is not None:
                sub = Interp(self.file, self.registry)
                sub.scopes = lam.interp.scopes
                scope[pname] = sub.eval_tokens(default)
            else:
                scope[pname] = None
        sub = Interp(lam.interp.file, self.registry)
        sub.scopes = lam.interp.scopes + [scope]
        return sub.exec_block(lam.body)

    def invoke_func(self, name, a):
        cands = FUNCS[name]
        same = [c for c in cands if c[2] == self.file] or [c for c in cands if os.path.dirname(c[2]) == os.path.dirname(self.file)] or cands
        params, body, f = same[0]
        scope = {}
        for idx, p in enumerate(split_args(params, 0, len(params))):
            eq = next((k for k, x in enumerate(p) if x.val == '='), None)
            decl = p[:eq] if eq is not None else p
            ids = [x.val for x in decl if x.kind == 'ident']
            if not ids:
                continue
            pname = ids[-1]
            if idx < len(a):
                scope[pname] = a[idx]
            elif eq is not None:
                sub = Interp(f, self.registry)
                scope[pname] = sub.eval_tokens(p[eq + 1:])
        sub = Interp(f, self.registry)
        sub.scopes = [scope]
        return sub.exec_block(body)

    # statements ------------------------------------------------------
    def exec_block(self, toks):
        i = 0
        n = len(toks)
        while i < n:
            t = toks[i]
            if t.kind == 'ident' and t.val == 'for':
                c = match_close(toks, i + 1)
                header = toks[i + 2:c]
                if toks[c + 1].val == '{':
                    e = match_close(toks, c + 1)
                    body = toks[c + 2:e]
                    nxt = e + 1
                else:
                    e = find_stmt_end(toks, c + 1)
                    body = toks[c + 1:e + 1]
                    nxt = e + 1
                if any(x.val == ';' for x in header):
                    # for (auto it = SRC.begin(); it != SRC.end(); ++it)
                    var = header[1].val
                    src = header[3].val
                    if header[0].val != 'auto' or header[4].val != '.' or header[5].val != 'begin':
                        raise EvalError('unsupported classic for loop')
                    srcv = to_json(self.lookup(src))
                    for k2, v2 in list(srcv.items()):
                        self.scopes.append({var: KV(k2, v2)})
                        self.exec_block(body)
                        self.scopes.pop()
                    i = nxt
                    continue
                colon = next(k for k, x in enumerate(header) if x.val == ':' )
                var = [x.val for x in header[:colon] if x.kind == 'ident'][-1]
                coll_toks = header[colon + 1:]
                sub = Interp(self.file, self.registry)
                sub.scopes = self.scopes
                coll = sub.eval_tokens(coll_toks)
                if isinstance(coll, tuple) and coll and coll[0] == 'enumtable':
                    coll = coll[1]
                items = coll.items if isinstance(coll, InitList) else coll
                for it in items:
                    self.scopes.append({var: it})
                    r = self.exec_block(body)
                    self.scopes.pop()
                i = nxt
                continue
            if t.kind == 'ident' and t.val == 'if':
                c = match_close(toks, i + 1)
                cond = toks[i + 2:c]
                neg = False
                if cond and cond[0].val == '!':
                    neg = True
                    cond = cond[1:]
                sub = Interp(self.file, self.registry)
                sub.scopes = self.scopes
                cv = bool(sub.eval_tokens(cond))
                if neg:
                    cv = not cv
                if toks[c + 1].val == '{':
                    e = match_close(toks, c + 1)
                    body = toks[c + 2:e]
                else:
                    e = find_stmt_end(toks, c + 1)
                    body = toks[c + 1:e + 1]
                if e + 1 < n and toks[e + 1].val == 'else':
                    raise EvalError('else not supported')
                if cv:
                    r = self.exec_block(body)
                    if r is not None:
                        return r
                i = e + 1
                continue
            if t.kind == 'ident' and t.val in ('while', 'switch'):
                raise EvalError(f'control flow {t.val} not supported in {self.file}')
            if t.kind == 'op' and t.val == '{':
                e = match_close(toks, i)
                self.scopes.append({})
                r = self.exec_block(toks[i + 1:e])
                self.scopes.pop()
                if r is not None:
                    return r
                i = e + 1
                continue
            e = find_stmt_end(toks, i)
            stmt = toks[i:e]
            i = e + 1
            if not stmt:
                continue
            r = self.exec_stmt(stmt)
            if r is not None:
                return r
        return None

    def exec_stmt(self, s):
        if s[0].val == 'return':
            sub = Interp(self.file, self.registry)
            sub.scopes = self.scopes
            return ('return', sub.eval_tokens(s[1:]))[1]
        if s[0].val in ('using', 'SDefinitionGroup', 'static_assert'):
            return None
        # find top-level '='
        depth = 0
        eq = None
        for k, x in enumerate(s):
            if x.kind == 'op':
                if x.val in '({[':
                    depth += 1
                elif x.val in ')}]':
                    depth -= 1
                elif x.val == '=' and depth == 0:
                    eq = k
                    break
        sub = Interp(self.file, self.registry)
        sub.scopes = self.scopes
        if eq is not None:
            lhs = s[:eq]
            rhs = s[eq + 1:]
            # group.fXxx = ...
            if lhs[0].val == 'group' and len(lhs) == 3 and lhs[1].val == '.':
                self.registry.set_group_field(lhs[2].val, to_json(sub.eval_tokens(rhs)))
                return None
            if any(x.val == '[' for x in lhs) and lhs[0].kind == 'ident' and lhs[1].val == '[':
                # NAME["k"]["k2"] = v
                target = to_json(self.lookup(lhs[0].val))
                keys = []
                k = 1
                while k < len(lhs):
                    c = match_close(lhs, k)
                    ksub = Interp(self.file, self.registry)
                    ksub.scopes = self.scopes
                    keys.append(ksub.eval_tokens(lhs[k + 1:c]))
                    k = c + 1
                cur = target
                for key in keys[:-1]:
                    cur = cur.setdefault(key, {})
                cur[keys[-1]] = to_json(sub.eval_tokens(rhs))
                self.set(lhs[0].val, target)
                return None
            name = [x.val for x in lhs if x.kind == 'ident'][-1]
            v = sub.eval_tokens(rhs)
            if not isinstance(v, (Lambda,)) and not (isinstance(v, tuple)):
                v = to_json(v) if isinstance(v, InitList) and 'json' in [x.val for x in lhs] else v
            self.scopes[-1][name] = v
            return None
        # declaration with brace init: TYPE NAME{...}
        if len(s) >= 3 and s[-1].val == '}' and s[0].kind == 'ident':
            ob = next((k for k, x in enumerate(s) if x.val == '{'), None)
            if ob and s[ob - 1].kind == 'ident' and ob >= 2:
                name = s[ob - 1].val
                v = sub.eval_tokens(s[ob:])
                self.scopes[-1][name] = to_json(v) if 'json' in [x.val for x in s[:ob]] else v
                return None
        # registry.AddTool(...)
        if s[0].val == 'registry' and s[1].val == '.':
            m = s[2].val
            c = match_close(s, 3)
            args = split_args(s, 4, c)
            if m == 'AddTool':
                name = Interp(self.file, self.registry).eval_tokens(args[1]) if args[1][0].kind == 'str' else sub.eval_tokens(args[1])
                effect = args[2][-1].val
                desc = sub.eval_tokens(args[4])
                schema = to_json(sub.eval_tokens(args[5]))
                handler = args[3][-1].val
                hfile = next((os.path.basename(c[2]) for c in FUNCS.get(handler, [])), '')
                self.registry.add_tool(name, effect, desc, schema, self.file)
                self.registry.cur['tools'][-1]['handlerFile'] = hfile
            elif m == 'AddGroup':
                self.registry.add_group()
            return None
        # method statement: NAME.method(args)
        if s[0].kind == 'ident' and len(s) > 2 and s[1].val == '.' and s[3].val == '(':
            name = s[0].val
            m = s[2].val
            c = match_close(s, 3)
            args = []
            for p in split_args(s, 4, c):
                sub2 = Interp(self.file, self.registry)
                sub2.scopes = self.scopes
                args.append(sub2.eval_tokens(p))
            target = self.lookup(name)
            if m == 'update':
                target = to_json(target)
                target.update(to_json(args[0]))
                self.set(name, target)
            elif m == 'insert':
                # insert(end, begin, end)
                src = args[1][2]
                target = list(to_json(target)) + list(to_json(src))
                self.set(name, target)
            elif m == 'push_back' or m == 'emplace_back':
                target = list(to_json(target) or [])
                target.append(to_json(args[0]))
                self.set(name, target)
            elif m == 'erase':
                target = to_json(target)
                target.pop(to_json(args[0]), None)
                self.set(name, target)
            elif m in ('reserve',):
                pass
            else:
                raise EvalError(f'unsupported method stmt {m}')
            return None
        # free function call statement: Func(registry, group, ...)
        if s[0].kind == 'ident' and s[1].val in ('(', '::'):
            k = 0
            while s[k + 1].val == '::':
                k += 2
            fname = s[k].val
            if fname in FUNCS:
                c = match_close(s, k + 1)
                # pass through (registry/group are global in this interpreter)
                cands = FUNCS[fname]
                params, body, f = cands[0]
                sub3 = Interp(f, self.registry)
                sub3.scopes = [{}]
                sub3.exec_block(body)
                return None
        # plain declaration without init: 'json x;' etc.
        if all(x.kind == 'ident' or x.val in ('::', '<', '>', '*', '&') for x in s):
            name = s[-1].val
            self.scopes[-1][name] = {}
            return None
        raise EvalError('unsupported statement: ' + ' '.join(str(x.val) for x in s[:20]))


class Registry:
    def __init__(self):
        self.groups = []
        self.cur = None

    def set_group_field(self, field, v):
        if self.cur is None:
            self.cur = {'tools': []}
        self.cur[field] = v

    def add_tool(self, name, effect, desc, schema, file):
        if self.cur is None:
            self.cur = {'tools': []}
        self.cur['tools'].append({'name': name, 'effect': effect, 'description': desc, 'inputSchema': schema, 'file': file})

    def add_group(self):
        self.groups.append(self.cur)
        self.cur = None


def group_id(display_name):
    """The groupId the server derives from a group display name ("3D Modeling" -> "3d-modeling")."""
    s = re.sub(r'[^a-z0-9]+', '-', (display_name or 'Ungrouped').lower()).strip('-')
    return s or 'ungrouped'


def extract(source):
    """Catalog of the groups defined under <source>/MCP; returns (groups, errors)."""
    global ROOT, API_ROOT
    ROOT = os.path.join(os.path.abspath(source), 'MCP')
    API_ROOT = os.path.join(os.path.abspath(source), 'API', 'Resources')
    for table in (ENUM_TABLES, STR_ARRAYS, GLOBAL_DEFS, GLOBAL_NUMS, API_TABLES, FUNCS, FILE_TOKS):
        table.clear()
    collect_globals()
    reg = Registry()
    results, errors = [], []
    for name, defs in FUNCS.items():
        if not name.endswith('::DefineGroup'):
            continue
        for params, body, f in defs:
            interp = Interp(f, reg)
            try:
                interp.exec_block(body)
            except Exception as ex:
                errors.append('%s: %s %s' % (os.path.relpath(f, ROOT), type(ex).__name__, ex))
                reg.cur = None
                continue
            for g in reg.groups:
                g['folder'] = os.path.basename(os.path.dirname(f))
                g['class'] = name.split('::')[0]
                g['groupId'] = group_id(g.get('fName'))
                for t in g['tools']:
                    t['file'] = os.path.relpath(t['file'], ROOT).replace('\\', '/')
                results.append(g)
            reg.groups = []
    return results, errors


def main():
    import argparse
    p = argparse.ArgumentParser(description='Extract the MCP tool catalog from a Vectorworks source tree.')
    p.add_argument('--source', required=True, help='Interfaces/VectorWorks folder (contains MCP/ and API/)')
    p.add_argument('--out', required=True, help='catalog file to write')
    a = p.parse_args()
    results, errors = extract(a.source)
    for e in errors:
        print('ERROR in', e)
    with open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(results, f, indent=1, ensure_ascii=False)
    print('groups', len(results), 'tools', sum(len(g['tools']) for g in results))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
