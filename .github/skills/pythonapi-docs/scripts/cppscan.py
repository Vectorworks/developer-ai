"""Token based scanner for the VWObjectAPI headers.

Collects classes / structs (with bases and members), enums (with enumerators), functions (with parameters and
qualifiers), fields, constants and type aliases, and keeps the comments that document them:
  lead     own-line comment block directly above a declaration
  trail    comment on the same line (and aligned continuation lines)
  group    lead comment of an earlier declaration of the same paragraph (no blank line in between)
  section  last short title comment ('// Geometry') of the scope
"""

import os
import re

OPERATOR_SYMBOLS = ['()', '[]', '->*', '->', '<<=', '>>=', '<=>', '==', '!=', '<=', '>=', '<<', '>>', '+=', '-=', '*=',
                    '/=', '%=', '&=', '|=', '^=', '&&', '||', '++', '--', '<', '>', '+', '-', '*', '/', '%', '&', '|',
                    '^', '!', '~', '=', ',']


class Tok:
    __slots__ = ('kind', 'text', 'line', 'col', 'nl', 'own_line')

    def __init__(self, kind, text, line, col, nl, own_line):
        self.kind = kind          # ident, number, string, punct, comment
        self.text = text
        self.line = line
        self.col = col
        self.nl = nl              # newlines between the previous token and this one
        self.own_line = own_line  # first token of its line

    def __repr__(self):
        return '%s(%r@%d)' % (self.kind, self.text, self.line)


def tokenize(text):
    toks = []
    i = 0
    n = len(text)
    line = 1
    col = 0
    nl = 0
    line_has_token = False
    line_start = 0

    def add(kind, s, start):
        nonlocal nl, line_has_token
        toks.append(Tok(kind, s, line, start - line_start, nl, not line_has_token))
        nl = 0
        line_has_token = True

    while i < n:
        c = text[i]
        if c == '\n':
            line += 1
            nl += 1
            i += 1
            line_start = i
            line_has_token = False
            continue
        if c in ' \t\r\f\v':
            i += 1
            continue
        if c == '#' and not line_has_token:
            # preprocessor directive (with line continuations)
            while i < n and text[i] != '\n':
                if text[i] == '\\' and i + 1 < n and text[i + 1] == '\n':
                    i += 2
                    line += 1
                    line_start = i
                    continue
                i += 1
            continue
        if text.startswith('//', i):
            j = text.find('\n', i)
            j = n if j < 0 else j
            add('comment', text[i:j], i)
            i = j
            continue
        if text.startswith('/*', i):
            j = text.find('*/', i + 2)
            j = n if j < 0 else j + 2
            add('comment', text[i:j], i)
            line += text.count('\n', i, j)
            if '\n' in text[i:j]:
                line_start = text.rfind('\n', i, j) + 1
            i = j
            continue
        if c == '"' or c == "'":
            j = i + 1
            while j < n and text[j] != c:
                j += 2 if text[j] == '\\' else 1
            add('string', text[i:j + 1], i)
            i = j + 1
            continue
        if c == 'R' and text.startswith('R"', i):
            m = re.match(r'R"([^(]*)\(', text[i:])
            if m:
                end = text.find(')' + m.group(1) + '"', i)
                add('string', text[i:end + len(m.group(1)) + 2], i)
                line += text.count('\n', i, end)
                i = end + len(m.group(1)) + 2
                continue
        if c.isalpha() or c == '_':
            j = i + 1
            while j < n and (text[j].isalnum() or text[j] == '_'):
                j += 1
            word = text[i:j]
            if word == 'operator':
                k = j
                while k < n and text[k] in ' \t':
                    k += 1
                sym = next((s for s in OPERATOR_SYMBOLS if text.startswith(s, k)), None)
                if sym:
                    add('ident', 'operator' + sym, i)
                    i = k + len(sym)
                    continue
                m = re.match(r'\s*([A-Za-z_][\w:]*)', text[j:])
                if m:  # conversion operator: operator bool
                    add('ident', 'operator ' + m.group(1), i)
                    i = j + m.end()
                    continue
            add('ident', word, i)
            i = j
            continue
        if c.isdigit() or (c == '.' and i + 1 < n and text[i + 1].isdigit()):
            m = re.match(r"(0[xX][0-9a-fA-F']+|[0-9][0-9']*\.?[0-9']*(?:[eE][+-]?[0-9]+)?|\.[0-9]+(?:[eE][+-]?[0-9]+)?)[uUlLfF]*", text[i:])
            add('number', m.group(0), i)
            i += m.end()
            continue
        if text.startswith('::', i):
            add('punct', '::', i)
            i += 2
            continue
        if text.startswith('...', i):
            add('punct', '...', i)
            i += 3
            continue
        add('punct', c, i)
        i += 1
    return toks


def join_tokens(toks):
    out = ''
    prev = None
    for t in toks:
        s = t.text
        if prev is not None:
            p = prev.text
            need = (prev.kind in ('ident', 'number') and t.kind in ('ident', 'number')) or \
                   (p in (',',) ) or (p == '=' or s == '=') or (prev.kind == 'ident' and s in ('&', '*') and False)
            if p in ('::', '<', '(', '[', '~', '!') or s in ('::', '>', ')', ']', ',', ';', '<', '(', '['):
                need = need and p == ',' 
            if need:
                out += ' '
            elif prev.kind != 'punct' and t.kind == 'punct' and s in ('&', '*', '&&'):
                out += ''
            elif p in ('&', '*', '&&') and t.kind == 'ident':
                out += ' '
            elif prev.kind == 'punct' and p == '>' and t.kind == 'ident':
                out += ' '
        out += s
        prev = t
    return out


def comment_text(tok):
    s = tok.text
    if s.startswith('//'):
        s = s[2:]
        s = s.lstrip('/!<')
    elif s.startswith('/*'):
        s = s[2:-2]
        s = '\n'.join(l.strip().lstrip('*').strip() for l in s.split('\n'))
    return s.strip()


def is_separator(text):
    return bool(re.match(r'^[-=*_~#/ ]{3,}$', text)) or text == ''


def section_marker(text):
    """'-- Selection -----' or 'Any control -------' -> the title; None for other lines."""
    m = re.match(r'^[-=]{2,}\s*([^-=].*?)\s*[-=]{2,}\s*$', text) or re.match(r'^([A-Za-z].*?)\s*[-=]{4,}\s*$', text)
    return m.group(1).strip() if m else None


def clean_block(toks):
    """Comment tokens -> list of text lines (separator lines removed, '-- Title --' lines as '§Title')."""
    lines = []
    for t in toks:
        s = comment_text(t)
        title = section_marker(s)
        if title:
            lines.append('\u00a7' + title)
        elif not is_separator(s):
            lines.append(s)
    return lines


def raw_block(toks):
    """Comment tokens -> raw lines (indentation after '//' kept, '' for empty comment lines, no separators)."""
    lines = []
    for t in toks:
        s = t.text
        if s.startswith('//'):
            s = s[2:]
            if s.startswith(('/', '!', '<')):
                s = s[1:]
            s = s.rstrip()
            if s.startswith(' '):
                s = s[1:]
        elif s.startswith('/*'):
            s = s[2:-2].strip()
        if section_marker(s.strip()) or (s.strip() and is_separator(s.strip())):
            continue
        lines.append(s)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def looks_like_title(lines):
    if len(lines) != 1:
        return False
    s = lines[0].strip()
    if s.startswith('\u00a7'):
        return True
    if not s or len(s) > 60 or s.endswith(('.', ':', ';', ',', ')')) and not s.endswith('...)'):
        return False
    if s.lower().startswith(('todo', 'note', 'see ', 'e.g', 'i.e', 'returns', 'return ', 'true', 'false')):
        return False
    words = s.split()
    if len(words) > 7:
        return False
    if re.search(r'[=;{}]|\w\(|->', s):
        return False
    return s[0].isupper() or s[0].isdigit()


class Scope:
    def __init__(self, kind, name, qual, entity=None):
        self.kind = kind
        self.name = name
        self.qual = qual
        self.entity = entity
        self.section = None
        self.note = None


class HeaderScanner:
    def __init__(self, path, rel):
        self.path = path
        self.rel = rel
        with open(path, encoding='utf-8-sig', errors='replace') as f:
            self.text = f.read()
        self.toks = tokenize(self.text)
        self.i = 0
        self.classes = {}
        self.enums = {}
        self.functions = []      # namespace scope functions
        self.aliases = {}        # qual -> target text (scope::name)
        self.constants = {}      # qual -> {type, value}
        self.file_doc = self._file_doc()

    def _file_doc(self):
        lines = []
        for t in self.toks:
            if t.kind != 'comment':
                break
            lines.append(comment_text(t))
        # drop the copyright block
        text = [l for l in lines if not re.search(r'Copyright|Use of this file|developer\.vectorworks\.net', l)]
        while text and not text[0].strip():
            text.pop(0)
        return text

    # ---------------------------------------------------------------------------------------------------------------
    def peek(self, k=0):
        j = self.i + k
        return self.toks[j] if j < len(self.toks) else None

    def skip_balanced(self, open_ch, close_ch):
        """self.toks[self.i] is open_ch; moves past the matching close_ch. Returns the inner tokens."""
        depth = 0
        start = self.i
        while self.i < len(self.toks):
            t = self.toks[self.i]
            if t.kind == 'punct' and t.text == open_ch:
                depth += 1
            elif t.kind == 'punct' and t.text == close_ch:
                depth -= 1
                if depth == 0:
                    self.i += 1
                    return self.toks[start + 1:self.i - 1]
            self.i += 1
        return self.toks[start + 1:]

    def parse(self):
        root = Scope('namespace', '', '')
        self.parse_scope([root])
        return self

    # ---------------------------------------------------------------------------------------------------------------
    def qual_of(self, stack, name):
        parts = []
        for s in stack:
            if s.name:
                parts.extend(p for p in s.name.split('::') if p and p != 'VWObjectAPI')
        tail = [p for p in (name or '').split('::') if p and p != 'VWObjectAPI']
        return '::'.join(parts + tail)

    def parse_scope(self, stack):
        scope = stack[-1]
        pending = []          # own-line comments waiting for a declaration
        para_lead = None      # lead of the current paragraph
        last = None           # last finished declaration (trailing comments)
        last_line = -1
        last_trail_col = None
        stmt = []
        stmt_lead = []
        stmt_lead_mid = False
        pending_mid = False
        stmt_comments = []
        stmt_para_break = False
        access = 'private' if scope.kind == 'class' and scope.entity.get('kind') == 'class' else 'public'

        def flush_detached():
            nonlocal pending
            block = clean_block(pending)
            marks = [l for l in block if l.startswith('\u00a7')]
            if marks:
                scope.section = marks[-1][1:]
                scope.note = None
                block = [l for l in block if not l.startswith('\u00a7')]
            if block:
                if looks_like_title(block):
                    scope.section = block[0]
                    scope.note = None
                else:
                    scope.note = ' '.join(block)
            pending = []

        while self.i < len(self.toks):
            t = self.toks[self.i]
            if t.kind == 'comment':
                if not stmt:
                    if last is not None and t.line == last_line:
                        last.setdefault('trail', []).append(comment_text(t))
                        last_trail_col = t.col
                        self.i += 1
                        continue
                    if (last is not None and last_trail_col is not None and t.nl == 1 and not pending
                            and abs(t.col - last_trail_col) <= 3 and t.col > 8):
                        last.setdefault('trail', []).append(comment_text(t))
                        self.i += 1
                        continue
                    if pending and t.nl >= 2:
                        flush_detached()
                        para_lead = None
                    if t.nl >= 2:
                        para_lead = None
                    if not pending:
                        prev = self.toks[self.i - 1] if self.i > 0 else None
                        # a comment directly below a declaration (no blank line) documents the next declaration,
                        # even when it is short: it is not a section title
                        pending_mid = t.nl == 1 and prev is not None and prev.text != '{'
                    pending.append(t)
                    last = None
                    last_trail_col = None
                else:
                    stmt_comments.append(t)
                self.i += 1
                continue

            if not stmt:
                if pending and t.nl >= 2:
                    flush_detached()
                    para_lead = None
                stmt_para_break = t.nl >= 2
                if stmt_para_break:
                    para_lead = None
                stmt_lead = pending
                stmt_lead_mid = bool(pending) and pending_mid
                pending = []
                last = None
                last_trail_col = None

            if t.kind == 'punct' and t.text == '}' :
                # end of this scope
                self.i += 1
                return
            if t.kind == 'punct' and t.text == ';':
                self.i += 1
                if stmt:
                    ent = self.finish_statement(stack, stmt, None)
                    if ent is not None:
                        self.attach(ent, scope, stmt_lead, stmt_comments, para_lead, stmt_lead_mid)
                        if clean_block(stmt_lead) and not looks_like_title(clean_block(stmt_lead)):
                            para_lead = (ent.get('lead'), ent.get('name'))
                        last = ent
                        last_line = t.line
                        last_trail_col = None
                stmt = []
                stmt_comments = []
                stmt_lead = []
                continue
            if t.kind == 'ident' and t.text in ('public', 'private', 'protected') and not stmt:
                nxt = self.peek(1)
                if nxt is not None and nxt.text == ':':
                    access = t.text
                    self.i += 2
                    continue
            if t.kind == 'punct' and t.text == '{' and sum(1 if x.text == '(' else -1 if x.text == ')' else 0 for x in stmt) > 0:
                # brace initializer inside a parameter list (default argument '= {}')
                inner = self.skip_balanced('{', '}')
                stmt.append(Tok('punct', '{' + join_tokens(inner) + '}', t.line, t.col, 0, False))
                continue
            if t.kind == 'punct' and t.text == '{':
                head = join_tokens(stmt)
                kind = self.classify_block(stmt)
                if kind == 'namespace':
                    name = ''.join(x.text for x in stmt[1:] if x.kind == 'ident' or x.text == '::')
                    self.i += 1
                    sub = Scope('namespace', name, self.qual_of(stack, name))
                    self.parse_scope(stack + [sub])
                elif kind == 'extern':
                    self.i += 1
                    self.parse_scope(stack + [Scope('namespace', '', scope.qual)])
                elif kind == 'class':
                    ent = self.class_entity(stack, stmt)
                    self.attach(ent, scope, stmt_lead, stmt_comments, None)
                    self.i += 1
                    sub = Scope('class', ent['name'], ent['qual'], ent)
                    self.parse_scope(stack + [sub])
                    # optional declarators up to ';'
                    while self.i < len(self.toks) and self.toks[self.i].text != ';':
                        self.i += 1
                    self.i += 1
                    end_line = self.toks[self.i - 1].line
                    if scope.kind == 'class':
                        scope.entity['members'].append(ent)
                    last = ent
                    last_line = end_line
                elif kind == 'enum':
                    ent = self.enum_entity(stack, stmt)
                    self.attach(ent, scope, stmt_lead, stmt_comments, None)
                    self.i += 1
                    self.parse_enum_body(ent)
                    while self.i < len(self.toks) and self.toks[self.i].text != ';':
                        self.i += 1
                    self.i += 1
                    if scope.kind == 'class':
                        scope.entity['members'].append(ent)
                    last = ent
                    last_line = self.toks[self.i - 1].line
                elif kind == 'function':
                    if self.in_ctor_init(stmt) and stmt and stmt[-1].kind == 'ident':
                        inner = self.skip_balanced('{', '}')
                        stmt.append(Tok('punct', '{}', t.line, t.col, 0, False))
                        continue
                    body = self.skip_balanced('{', '}')
                    end_line = self.toks[self.i - 1].line
                    ent = self.finish_statement(stack, stmt, body)
                    if ent is not None:
                        self.attach(ent, scope, stmt_lead, stmt_comments, para_lead, stmt_lead_mid)
                        if clean_block(stmt_lead) and not looks_like_title(clean_block(stmt_lead)):
                            para_lead = (ent.get('lead'), ent.get('name'))
                        last = ent
                        last_line = end_line
                        last_trail_col = None
                    if self.peek() is not None and self.peek().text == ';':
                        self.i += 1
                    stmt = []
                    stmt_comments = []
                    stmt_lead = []
                    continue
                else:
                    # brace initializer: keep a placeholder and continue to ';'
                    inner = self.skip_balanced('{', '}')
                    stmt.append(Tok('punct', '{' + join_tokens(inner) + '}', t.line, t.col, 0, False))
                    continue
                stmt = []
                stmt_comments = []
                stmt_lead = []
                continue
            stmt.append(t)
            self.i += 1

    # ---------------------------------------------------------------------------------------------------------------
    @staticmethod
    def top_level_paren(stmt):
        """Index of the first '(' outside template brackets; None when there is none."""
        angle = 0
        for k, t in enumerate(stmt):
            if t.kind == 'punct':
                if t.text == '<' and k > 0 and stmt[k - 1].kind == 'ident':
                    angle += 1
                elif t.text == '>' and angle > 0:
                    angle -= 1
                elif t.text == '(' and angle == 0:
                    return k
                elif t.text == '=' and angle == 0:
                    return None
        return None

    def classify_block(self, stmt):
        words = [t.text for t in stmt if t.kind == 'ident']
        if not stmt:
            return 'brace'
        if stmt[0].text == 'namespace':
            return 'namespace'
        if stmt[0].text == 'extern' and len(stmt) > 1 and stmt[1].kind == 'string':
            return 'extern'
        k = 0
        if stmt[0].text == 'template':
            # skip template<...>
            depth = 0
            for k, t in enumerate(stmt):
                if t.text == '<':
                    depth += 1
                elif t.text == '>':
                    depth -= 1
                    if depth == 0:
                        k += 1
                        break
        head = stmt[k:] if k < len(stmt) else []
        if head and head[0].text in ('class', 'struct', 'union'):
            if self.top_level_paren(head) is None:
                return 'class'
        if head and head[0].text == 'enum':
            return 'enum'
        if self.top_level_paren(stmt) is not None:
            return 'function'
        return 'brace'

    @staticmethod
    def in_ctor_init(stmt):
        depth = 0
        seen_params = False
        for t in stmt:
            if t.text == '(':
                depth += 1
            elif t.text == ')':
                depth -= 1
                if depth == 0:
                    seen_params = True
            elif t.text == ':' and depth == 0 and seen_params:
                return True
        return False

    def class_entity(self, stack, stmt):
        toks = stmt
        is_template = toks[0].text == 'template'
        if is_template:
            depth = 0
            for k, t in enumerate(toks):
                if t.text == '<':
                    depth += 1
                elif t.text == '>':
                    depth -= 1
                    if depth == 0:
                        toks = toks[k + 1:]
                        break
        kind = toks[0].text
        name = None
        bases = []
        k = 1
        while k < len(toks):
            t = toks[k]
            if t.kind == 'ident' and t.text not in ('final', 'alignas') and name is None:
                name = t.text
            elif t.text == ':' :
                base_text = join_tokens(toks[k + 1:])
                for b in self.split_commas(base_text):
                    b = re.sub(r'^(public|protected|private|virtual)\s+', '', b.strip())
                    b = re.sub(r'^(public|protected|private|virtual)\s+', '', b.strip())
                    bases.append(b.strip())
                break
            k += 1
        qual = self.qual_of(stack, name)
        ent = {'type': 'class', 'kind': kind, 'name': name, 'qual': qual, 'bases': bases, 'members': [],
               'file': self.rel, 'line': stmt[0].line, 'template': is_template}
        if qual not in self.classes or not self.classes[qual].get('members'):
            self.classes[qual] = ent
        return ent

    def enum_entity(self, stack, stmt):
        words = [t.text for t in stmt]
        k = 1
        if k < len(words) and words[k] in ('class', 'struct'):
            k += 1
        name = words[k] if k < len(words) else ''
        underlying = join_tokens(stmt[k + 2:]) if k + 1 < len(words) and words[k + 1] == ':' else None
        qual = self.qual_of(stack, name)
        ent = {'type': 'enum', 'name': name, 'qual': qual, 'values': [], 'underlying': underlying,
               'file': self.rel, 'line': stmt[0].line}
        self.enums[qual] = ent
        return ent

    def parse_enum_body(self, ent):
        pending = []
        cur = []
        cur_lead = []
        last = None
        last_line = -1
        while self.i < len(self.toks):
            t = self.toks[self.i]
            if t.kind == 'comment':
                if last is not None and t.line == last_line and not cur:
                    last.setdefault('trail', []).append(comment_text(t))
                elif cur and t.line == cur[-1].line:
                    pending_trail = comment_text(t)
                    cur.append(Tok('comment', pending_trail, t.line, t.col, 0, False))
                else:
                    pending.append(t)
                self.i += 1
                continue
            if t.text in (',', '}'):
                if cur:
                    code = [x for x in cur if x.kind != 'comment']
                    trail = [x.text for x in cur if x.kind == 'comment']
                    name = code[0].text
                    value = join_tokens(code[2:]) if len(code) > 2 and code[1].text == '=' else None
                    val = {'name': name, 'value': value, 'lead': clean_block(cur_lead), 'trail': trail}
                    ent['values'].append(val)
                    last = val
                    last_line = t.line
                    cur = []
                if t.text == '}':
                    self.i += 1
                    return
                self.i += 1
                continue
            if not cur:
                cur_lead = pending
                pending = []
            cur.append(t)
            self.i += 1

    @staticmethod
    def split_commas(text):
        parts, depth, cur = [], 0, ''
        for ch in text:
            if ch in '<([{':
                depth += 1
            elif ch in '>)]}':
                depth -= 1
            if ch == ',' and depth == 0:
                parts.append(cur)
                cur = ''
            else:
                cur += ch
        if cur.strip():
            parts.append(cur)
        return parts

    # ---------------------------------------------------------------------------------------------------------------
    def attach(self, ent, scope, lead_toks, inner_comments, para_lead, mid=False):
        lead = clean_block(lead_toks)
        # '-- Title ---' markers start a section
        marks = [l for l in lead if l.startswith('\u00a7')]
        if marks:
            scope.section = marks[-1][1:]
            scope.note = None
            lead = [l for l in lead if not l.startswith('\u00a7')]
        if ent.get('type') in ('class', 'enum', 'function', 'field'):
            ent['lead_raw'] = raw_block(lead_toks)
        if lead and looks_like_title(lead) and ent.get('type') not in ('class', 'enum') and not mid:
            scope.section = lead[0]
            scope.note = None
            lead = []
        elif len(lead) > 1 and looks_like_title(lead[:1]) and not lead[0].endswith('.') and ent.get('type') not in ('class', 'enum') and not mid:
            # '// Title' followed by a description
            scope.section = lead[0]
            scope.note = None
            lead = lead[1:]
        if lead:
            m = re.match(r'^([A-Z][A-Za-z0-9]*(?: [A-Za-z0-9]+){0,2}):\s+(\S.*)$', lead[0])
            if m and ent.get('type') in ('function', 'field') and m.group(1).lower() not in (
                    'note', 'example', 'returns', 'warning', 'important', 'units', 'todo', 'e.g', 'i.e', 'see', 'usage',
                    'caution', 'remark', 'remarks'):
                # 'Pen: raw pen style ...' - a sub-section title followed by the description
                scope.section = m.group(1)
                scope.note = None
                lead = [m.group(2)] + lead[1:]
            ent['lead'] = ' '.join(lead)
        elif para_lead and ent.get('type') in ('function', 'field'):
            ent['group'] = para_lead[0]
            ent['group_owner'] = para_lead[1]
        if inner_comments:
            ent.setdefault('trail', []).extend(comment_text(c) for c in inner_comments)
        if scope.section:
            ent['section'] = scope.section
        if scope.note and ent.get('type') in ('function', 'field'):
            ent['note'] = scope.note
        for s in ent.get('siblings', []):
            for key in ('lead', 'group', 'trail', 'section', 'note'):
                if key in ent:
                    s[key] = ent[key]

    def finish_statement(self, stack, stmt, body):
        scope = stack[-1]
        words = [t.text for t in stmt]
        if not words:
            return None
        if words[0] in ('friend', 'static_assert'):
            if words[0] == 'friend' and self.top_level_paren(stmt) is not None:
                ent = self.function_entity(stack, stmt[1:], body)
                if ent:
                    ent['friend'] = True
                    self.functions.append(ent) if scope.kind != 'class' else scope.entity.setdefault('friends', []).append(ent)
                return None
            return None
        if words[0] == 'using':
            if len(words) > 2 and words[2] == '=':
                name = words[1]
                target = join_tokens(stmt[3:])
                self.aliases[self.qual_of(stack, name)] = {'target': target, 'scope': scope.qual}
                ent = {'type': 'alias', 'name': name, 'target': target}
                if scope.kind == 'class':
                    scope.entity['members'].append(ent)
                return ent
            return None
        if words[0] == 'typedef':
            name = words[-1]
            target = join_tokens(stmt[1:-1])
            self.aliases[self.qual_of(stack, name)] = {'target': target, 'scope': scope.qual}
            return None
        if words[0] in ('class', 'struct', 'enum', 'union') and self.top_level_paren(stmt) is None and '=' not in words:
            return None  # forward declaration
        if words[0] == 'template':
            depth = 0
            for k, t in enumerate(stmt):
                if t.text == '<':
                    depth += 1
                elif t.text == '>':
                    depth -= 1
                    if depth == 0:
                        rest = stmt[k + 1:]
                        ent = self.finish_statement(stack, rest, body)
                        if ent is not None:
                            ent['template'] = True
                        return ent
            return None
        if self.top_level_paren(stmt) is not None:
            ent = self.function_entity(stack, stmt, body)
        else:
            ent = self.field_entity(stack, stmt)
        if ent is None:
            return None
        if scope.kind == 'class':
            scope.entity['members'].append(ent)
            scope.entity['members'].extend(ent.get('siblings', []))
        else:
            if ent['type'] == 'function':
                ent['scope'] = scope.qual
                self.functions.append(ent)
            else:
                for e in [ent] + ent.get('siblings', []):
                    e['scope'] = scope.qual
                    self.constants[self.qual_of(stack, e['name'])] = e
        return ent

    SPECIFIERS = ('static', 'virtual', 'inline', 'constexpr', 'explicit', 'extern', 'consteval', 'constinit',
                  'mutable', 'thread_local')

    def function_entity(self, stack, stmt, body):
        p = self.top_level_paren(stmt)
        name_tok = stmt[p - 1] if p > 0 else None
        if name_tok is None:
            return None
        name_start = p - 1
        name = name_tok.text
        if p >= 2 and stmt[p - 2].text == '~':
            name = '~' + name
            name_start = p - 2
        # qualified names (out of class definitions) are not expected in these headers
        prefix = stmt[:name_start]
        while prefix and prefix[-1].text == '::':
            prefix = prefix[:-2]
        spec = set()
        ret_toks = []
        k = 0
        while k < len(prefix):
            t = prefix[k]
            if t.kind == 'ident' and t.text in self.SPECIFIERS:
                spec.add(t.text)
            elif t.text == '[' and k + 1 < len(prefix) and prefix[k + 1].text == '[':
                # attribute [[...]]
                depth = 0
                while k < len(prefix):
                    if prefix[k].text == '[':
                        depth += 1
                    elif prefix[k].text == ']':
                        depth -= 1
                        if depth == 0:
                            break
                    k += 1
            else:
                ret_toks.append(t)
            k += 1
        # parameters
        depth = 0
        q = p
        while q < len(stmt):
            if stmt[q].text == '(':
                depth += 1
            elif stmt[q].text == ')':
                depth -= 1
                if depth == 0:
                    break
            q += 1
        params_toks = stmt[p + 1:q]
        suffix = [t.text for t in stmt[q + 1:]]
        params = self.parse_params(params_toks)
        scope = stack[-1]
        ret = join_tokens(ret_toks)
        is_ctor = scope.kind == 'class' and name == scope.name and not ret
        ent = {'type': 'function', 'name': name, 'ret': ret, 'params': params, 'static': 'static' in spec,
               'const': 'const' in suffix, 'ctor': is_ctor, 'explicit': 'explicit' in spec,
               'deleted': suffix[-2:] == ['=', 'delete'], 'line': stmt[0].line, 'file': self.rel,
               'inline_body': body is not None}
        return ent

    def parse_params(self, toks):
        text = join_tokens(toks).strip()
        if not text or text == 'void':
            return []
        params = []
        for part in self.split_commas(text):
            part = part.strip()
            default = None
            m = re.search(r'(?<![=!<>])=(?!=)', part)
            # split at a top-level '=' (not inside template brackets / parens)
            depth = 0
            eq = None
            for idx, ch in enumerate(part):
                if ch in '<([{':
                    depth += 1
                elif ch in '>)]}':
                    depth -= 1
                elif ch == '=' and depth == 0 and part[idx - 1:idx] not in ('=', '!', '<', '>') and part[idx + 1:idx + 2] != '=':
                    eq = idx
                    break
            if eq is not None:
                default = part[eq + 1:].strip()
                part = part[:eq].strip()
            m = re.match(r'^(.*?)([A-Za-z_]\w*)$', part)
            ptype, pname = part, None
            if m:
                before = m.group(1).rstrip()
                word = m.group(2)
                if before and not before.endswith('::') and word not in ('int', 'double', 'float', 'bool', 'char', 'long',
                                                                         'short', 'unsigned', 'signed', 'const', 'size_t',
                                                                         'void', 'auto'):
                    if re.search(r'[\w>&*\]]$', before):
                        ptype, pname = before, word
            params.append({'type': ptype.strip(), 'name': pname, 'default': default})
        return params

    def field_entity(self, stack, stmt):
        spec = set()
        toks = list(stmt)
        while toks and toks[0].kind == 'ident' and toks[0].text in self.SPECIFIERS:
            spec.add(toks[0].text)
            toks = toks[1:]
        # declarators: 'double a = 1.0, b = 0.0;'
        parts = []
        cur = []
        depth = 0
        for k, t in enumerate(toks):
            if t.text in ('(', '[') or (t.text == '<' and k > 0 and toks[k - 1].kind == 'ident'):
                depth += 1
            elif t.text in (')', ']', '>') and depth > 0:
                depth -= 1
            if t.text == ',' and depth == 0:
                parts.append(cur)
                cur = []
            else:
                cur.append(t)
        parts.append(cur)

        def split_init(part):
            depth = 0
            for k, t in enumerate(part):
                if t.text in ('<', '(', '['):
                    depth += 1 if (t.text != '<' or (k > 0 and part[k - 1].kind == 'ident')) else 0
                elif t.text in ('>', ')', ']'):
                    depth = max(0, depth - 1)
                if depth == 0 and (t.text == '=' or (t.kind == 'punct' and t.text.startswith('{') and len(t.text) > 1)):
                    return part[:k], (join_tokens(part[k + 1:]) if t.text == '=' else t.text[1:-1].strip())
            return part, None

        decl, init = split_init(parts[0])
        if not decl:
            return None
        extra = []
        for p in parts[1:]:
            d, i = split_init(p)
            if d and d[-1].kind == 'ident':
                extra.append((d[-1].text, i))
        array = None
        if decl[-1].text == ']':
            # name[N]
            k = len(decl) - 1
            while k >= 0 and decl[k].text != '[':
                k -= 1
            array = join_tokens(decl[k + 1:-1])
            decl = decl[:k]
        if not decl or decl[-1].kind != 'ident':
            return None
        name = decl[-1].text
        ftype = join_tokens(decl[:-1])
        if not ftype:
            return None
        ent = {'type': 'field', 'name': name, 'ftype': ftype, 'init': init, 'static': 'static' in spec,
               'constexpr': 'constexpr' in spec, 'array': array, 'line': stmt[0].line, 'file': self.rel}
        if extra:
            ent['siblings'] = [dict(ent, name=n, init=i) for n, i in extra]
        return ent


def scan_api(api_root):
    headers = {}
    for dirpath, dirnames, filenames in os.walk(api_root):
        dirnames.sort()
        for fn in sorted(filenames):
            if fn.endswith('.h'):
                path = os.path.join(dirpath, fn)
                rel = os.path.relpath(path, api_root).replace('\\', '/')
                headers[rel] = HeaderScanner(path, rel).parse()
    return headers


if __name__ == '__main__':
    import json
    import sys
    api_root = sys.argv[1]
    which = sys.argv[2] if len(sys.argv) > 2 else None
    hs = scan_api(api_root)
    if which:
        h = hs[which]
        print('FILE DOC:', h.file_doc[:5])
        for q, c in h.classes.items():
            print('CLASS', q, c['bases'], '|', c.get('lead', '')[:100])
            for m in c['members']:
                if m['type'] == 'function':
                    print('   F', m['name'], '(', ', '.join('%s %s' % (p['type'], p['name']) for p in m['params']), ')', '->', m['ret'],
                          'static' if m['static'] else '', '| L:', m.get('lead', '')[:60], '| G:', (m.get('group') or '')[:40],
                          '| T:', m.get('trail'), '| S:', m.get('section'))
                elif m['type'] == 'field':
                    print('   V', m['ftype'], m['name'], '=', m['init'], '| L:', m.get('lead', '')[:60], '| T:', m.get('trail'), '| S:', m.get('section'))
                elif m['type'] == 'alias':
                    print('   A', m['name'], '=', m['target'])
                else:
                    print('   ', m['type'], m.get('name'))
        for q, e in h.enums.items():
            print('ENUM', q, e['underlying'], '|', e.get('lead', '')[:80])
            for v in e['values']:
                print('     ', v['name'], '=', v['value'], v['lead'], v.get('trail'))
        for f in h.functions:
            print('FN', f['scope'], f['name'], [p['type'] for p in f['params']], '->', f['ret'], '|', f.get('lead', '')[:60], f.get('trail'))
        for q, a in h.aliases.items():
            print('ALIAS', q, '=', a['target'])
        for q, c in h.constants.items():
            print('CONST', q, c['ftype'], c['init'])
    else:
        nc = sum(len(h.classes) for h in hs.values())
        ne = sum(len(h.enums) for h in hs.values())
        print(len(hs), 'headers', nc, 'classes', ne, 'enums')
