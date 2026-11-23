"""Joins the binding model (bindscan) with the API headers (cppscan): Python names, Python types and C++ comments."""

import os
import re

import bindscan
import cppscan

INT_TYPES = {
    'char', 'signed char', 'unsigned char', 'short', 'unsigned short', 'int', 'unsigned', 'unsigned int', 'long',
    'unsigned long', 'long long', 'unsigned long long', 'size_t', 'std::size_t', 'ptrdiff_t', 'std::ptrdiff_t',
    'int8_t', 'int16_t', 'int32_t', 'int64_t', 'uint8_t', 'uint16_t', 'uint32_t', 'uint64_t',
    'std::int8_t', 'std::int16_t', 'std::int32_t', 'std::int64_t', 'std::uint8_t', 'std::uint16_t', 'std::uint32_t',
    'std::uint64_t', 'Sint8', 'Sint16', 'Sint32', 'Sint64', 'Uint8', 'Uint16', 'Uint32', 'Uint64', 'short int',
    'InternalIndex', 'RefNumber', 'ColorRef', 'OpacityRef', 'TSint32', 'TUint32', 'Byte', 'Uchar',
    'ObjectColorType', 'ViewCoord', 'SintptrT', 'UintptrT', 'GSHandle', 'MacTypes::Size', 'OSType', 'TVWObjectType',
    'short_t', 'Sint', 'Uint',
}
FLOAT_TYPES = {'double', 'float', 'long double', 'WorldCoord', 'double_param', 'double_gs', 'Real64', 'Real32',
               'WorldCoord_param', 'WorldArea', 'WorldVolume'}
HANDLE_TYPES = {'BlankHandle', 'MCObjectHandle', 'Handle', 'MCObjectHandleID'}
STRING_TYPES = {'std::string', 'string', 'std::basic_string<char>'}

BINDING_ROOT = None
API_ROOT = None


def norm_type(t):
    t = t.replace('VWObjectAPI::', '').strip()
    t = re.sub(r'^::', '', t)
    t = re.sub(r'\bconst\b', '', t)
    t = re.sub(r'\bvolatile\b', '', t)
    t = re.sub(r'\btypename\b', '', t)
    t = t.replace('&&', '').replace('&', '')
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'\s*([<>,:*])\s*', r'\1', t)
    t = t.replace(',', ', ')
    t = t.replace('>>', '> >').replace('> >', '>>')
    return t


def split_template(t):
    """'std::vector<A, B>' -> ('std::vector', ['A', 'B']); None when t is not a template id."""
    m = re.match(r'^([\w:]+)\s*<(.*)>$', t, re.S)
    if not m:
        return None
    return m.group(1), [x.strip() for x in bindscan.split_top(m.group(2))]


class Model:
    def __init__(self, binding_root, api_root):
        self.binding_root = binding_root
        self.api_root = api_root
        self.bfiles = bindscan.scan(binding_root)
        self.headers = cppscan.scan_api(api_root)
        self.hclasses = {}
        self.henums = {}
        self.haliases = {}
        self.hfunctions = {}
        self.hconstants = {}
        for h in self.headers.values():
            for q, c in h.classes.items():
                if q not in self.hclasses or not self.hclasses[q]['members']:
                    self.hclasses[q] = c
            self.henums.update(h.enums)
            self.haliases.update(h.aliases)
            for f in h.functions:
                q = (f['scope'] + '::' + f['name']) if f.get('scope') else f['name']
                self.hfunctions.setdefault(q, []).append(f)
            self.hconstants.update(h.constants)
        self.classes = {}    # normalized cpp -> binding class record
        self.enums = {}
        for bf in self.bfiles:
            for c in bf.classes:
                c['cppn'] = norm_type(c['cpp'])
                c['folder'] = bf.folder
                self.classes[c['cppn']] = c
            for e in bf.enums:
                e['cppn'] = norm_type(e['cpp'])
                e['folder'] = bf.folder
                self.enums[e['cppn']] = e
        self.problems = []

    # ------------------------------------------------------------------------------------------------------------
    @staticmethod
    def scope_chain(scope):
        parts = scope.split('::') if scope else []
        chain = []
        for k in range(len(parts), -1, -1):
            chain.append('::'.join(parts[:k]))
        return chain

    def resolve_name(self, name, scope):
        """Canonical qualified C++ name of a class / enum / alias, or None."""
        name = name.replace('VWObjectAPI::', '').lstrip(':')
        for prefix in self.scope_chain(scope):
            q = (prefix + '::' + name) if prefix else name
            if q in self.hclasses or q in self.henums or q in self.haliases or q in self.classes or q in self.enums:
                return q
            # name resolved through a base class (nested types of bases)
        # nested name of a base class: Base::Nested
        return None

    def class_scope_of(self, qual):
        return qual

    def py_class_name(self, cppq):
        c = self.classes.get(cppq)
        if c is None:
            return None
        return ('Math.' + c['qualname']) if c['module'] == 'api.Math' else c['qualname']

    def py_enum_name(self, cppq):
        e = self.enums.get(cppq)
        if e is None:
            return None
        return ('Math.' + e['qualname']) if e['module'] == 'api.Math' else e['qualname']

    def py_type(self, t, scope='', depth=0):
        """Python type name of a C++ type, as the binding prints it (TConv<T>::Name)."""
        if depth > 20:
            return '?'
        t = norm_type(t)
        if t in ('void', ''):
            return 'None'
        if t == 'bool':
            return 'bool'
        if t in INT_TYPES:
            return 'int'
        if t in FLOAT_TYPES:
            return 'float'
        if t in STRING_TYPES:
            return 'str'
        if t in HANDLE_TYPES:
            return 'Handle'
        if t == 'SBytes':
            return 'bytes'
        if t == 'SClassArg':
            return 'type'
        if t == 'CPyRef':
            return 'object'
        if t.endswith('*'):
            return 'object'
        st = split_template(t)
        if st:
            tmpl, args = st
            tmpl = tmpl.replace('std::', '')
            if tmpl == 'optional':
                return self.py_type(args[0], scope, depth + 1) + ' | None'
            if tmpl == 'vector':
                return 'list[%s]' % self.py_type(args[0], scope, depth + 1)
            if tmpl == 'array':
                return 'tuple[%s * %s]' % (self.py_type(args[0], scope, depth + 1), args[1])
            if tmpl == 'pair':
                return 'tuple[%s, %s]' % (self.py_type(args[0], scope, depth + 1), self.py_type(args[1], scope, depth + 1))
            if tmpl in ('unordered_map', 'map'):
                return 'dict[%s, %s]' % (self.py_type(args[0], scope, depth + 1), self.py_type(args[1], scope, depth + 1))
            if tmpl == 'function':
                m = re.match(r'^(.*?)\((.*)\)$', args[0])
                inner = [self.py_type(a, scope, depth + 1) for a in bindscan.split_top(m.group(2)) if a.strip()]
                return 'callable(%s)' % ', '.join(inner)
            if tmpl == 'IsTrue':
                return 'bool'
        q = self.resolve_name(t, scope)
        if q is not None:
            if q in self.classes:
                return self.py_class_name(q)
            if q in self.enums:
                return self.py_enum_name(q)
            if q in self.henums:
                return 'int'   # enumeration without Python binding: EnumName(nullptr) == "int"
            if q in self.haliases:
                a = self.haliases[q]
                return self.py_type(a['target'], a['scope'], depth + 1)
            if q in self.hclasses:
                self.problems.append('unbound class type %s (scope %s)' % (t, scope))
                return '<unbound %s>' % t
        self.problems.append('unknown type %s (scope %s)' % (t, scope))
        return '<%s>' % t

    def canonical(self, t, scope):
        """C++ type with names resolved and aliases expanded, for overload matching."""
        t = norm_type(t)
        st = split_template(t)
        if st:
            return '%s<%s>' % (st[0].replace('std::', ''), ','.join(self.canonical(a, scope) for a in st[1]))
        if t in INT_TYPES or t in FLOAT_TYPES or t in HANDLE_TYPES or t in STRING_TYPES or t == 'bool':
            return t.replace('std::', '')
        q = self.resolve_name(t, scope)
        if q is not None and q in self.haliases:
            a = self.haliases[q]
            return self.canonical(a['target'], a['scope'])
        return q or t

    # ------------------------------------------------------------------------------------------------------------
    def header_class(self, cpp):
        q = self.resolve_name(norm_type(cpp), '')
        if q in self.haliases:
            a = self.haliases[q]
            q = self.resolve_name(norm_type(a['target']), a['scope'])
        return self.hclasses.get(q) if q else None

    def base_classes(self, hc):
        result = []
        scope = hc['qual'].rpartition('::')[0]
        for b in hc.get('bases', []):
            q = self.resolve_name(norm_type(b), scope)
            if q in self.hclasses:
                result.append(self.hclasses[q])
        return result

    def find_members(self, hc, name, kind='function', seen=None):
        if hc is None:
            return []
        found = [m for m in hc['members'] if m.get('type') == kind and m.get('name') == name]
        found += [m for m in hc.get('friends', []) if m.get('name') == name] if kind == 'function' else []
        if found:
            return [(hc, m) for m in found]
        for b in self.base_classes(hc):
            r = self.find_members(b, name, kind)
            if r:
                return r
        return []

    def match_overload(self, candidates, sig, nargs, owner_scope):
        if len(candidates) == 1:
            return candidates[0]
        if sig:
            want = [self.canonical(p, owner_scope) for p in sig['params']]
            for hc, m in candidates:
                got = [self.canonical(p['type'], hc['qual']) for p in m['params']]
                if got == want:
                    return hc, m
            # looser: same count, same text
            for hc, m in candidates:
                if len(m['params']) == len(want) and all(norm_type(a['type']).split('::')[-1] == norm_type(b).split('::')[-1]
                                                        for a, b in zip(m['params'], sig['params'])):
                    return hc, m
        same = [(hc, m) for hc, m in candidates if len(m['params']) == nargs]
        if len(same) == 1:
            return same[0]
        return None


def build(binding_root, api_root):
    return Model(binding_root, api_root)
