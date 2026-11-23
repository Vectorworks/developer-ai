"""Resolves every binding member against the headers: Python signature parts, static flag, C++ comments."""

import re

import bindscan
from model import Model, norm_type, split_template


def py_default(model, bf, expr, py_t):
    """Python text of an SArg default value (like ReprText of the converted default)."""
    if expr is None:
        return None
    e = expr.strip()
    # unwrap static_cast<T>(x) and T(x) / T{x}
    m = re.match(r'^static_cast<(.+)>\((.*)\)$', e, re.S)
    if m:
        inner_t, e = m.group(1).strip(), m.group(2).strip()
    m = re.match(r'^(?:std::)?u?int(?:8|16|32|64)_t\((.*)\)$', e)
    if m:
        e = m.group(1).strip()
    if e in bf.local_consts:
        lc = bf.local_consts[e]
        if lc['value']:
            if lc['value'].startswith('CTextObject::k') or re.match(r'^C\w+::k\w+$', lc['value']):
                return lc['value'].split('::')[-1]
            e = lc['value']
        elif 'string' in lc['type']:
            return "''"
    if e in ('true', 'false'):
        return 'True' if e == 'true' else 'False'
    if e in ('nullptr', 'BlankHandle(nullptr)', 'NULL'):
        return 'None'
    if e in ('std::string{}', 'std::string()', '""', 'kEmpty'):
        return "''"
    if e == 'SIZE_MAX':
        return '2**64 - 1'
    if re.match(r'^-?\d+$', e):
        return e
    if re.match(r'^-?\d*\.\d*(e-?\d+)?$', e):
        v = float(e)
        return repr(v)
    if e.startswith('Math::k') or e.startswith('k'):
        name = e.split('::')[-1]
        consts = {'kEpsilon': '1e-09', 'kAngleEpsilon': '1e-09'}
        return consts.get(name, name)
    m = re.match(r'^std::vector<.*>\(\)$', e)
    if m:
        return '[]'
    # enumerator
    m = re.match(r'^([\w:]+)::(\w+)$', e)
    if m:
        enum_q = model.resolve_name(m.group(1), '')
        if enum_q in model.enums:
            en = model.enums[enum_q]
            for v in en['values']:
                if v['cpp'].split('::')[-1] == m.group(2):
                    return '%s.%s' % (model.py_enum_name(enum_q), v['name'])
    # value of a bound class: T(), T{}, T(args)
    m = re.match(r'^([\w:]+)\s*[({](.*)[)}]$', e, re.S)
    if m:
        q = model.resolve_name(m.group(1), '')
        if q in model.haliases and q not in model.classes:
            a = model.haliases[q]
            q = model.resolve_name(norm_type(a['target']), a['scope'])
        if q in model.classes:
            args = ', '.join(a.strip() for a in bindscan.split_top(m.group(2)) if a.strip())
            return '%s(%s)' % (model.py_class_name(q), args)
    return e


class Member:
    """One overload of a Python-visible callable, a field or a constant."""

    def __init__(self, **kw):
        self.__dict__.update(kw)


def describe_params(model, cpp_params, scope, sargs):
    out = []
    for k, t in enumerate(cpp_params):
        a = sargs[k] if k < len(sargs) else {'name': 'arg%d' % k, 'default': None}
        out.append({'name': a['name'], 'type': model.py_type(t, scope), 'cpp': t, 'default_expr': a['default']})
    return out


def resolve(model):
    problems = []
    resolved = []
    for bf in model.bfiles:
        for mem in bf.members:
            r = resolve_member(model, bf, mem, problems)
            if r is not None:
                resolved.append(r)
    return resolved, problems


def resolve_member(model, bf, mem, problems):
    kind = mem['kind']
    if mem['builder'] == 'module':
        module = 'api.Math' if mem['owner'] == 'mathModule' else 'api'
        owner_cls = None
        owner_hc = None
        owner_q = None
    else:
        owner_q = model.resolve_name(norm_type(mem['owner']), '')
        if owner_q in model.haliases:
            a = model.haliases[owner_q]
            owner_q = model.resolve_name(norm_type(a['target']), a['scope'])
        owner_cls = model.classes.get(owner_q)
        owner_hc = model.hclasses.get(owner_q)
        module = owner_cls['module'] if owner_cls else None
        if owner_cls is None:
            problems.append('%s: builder of unbound class %s' % (bf.rel, mem['owner']))
    r = Member(kind=kind, file=bf.rel, folder=bf.folder, module=module, owner=owner_q, name=mem.get('name'),
               define_fn=mem.get('define_fn'), pos=mem['pos'], decl=None, decl_class=None, adapter=None)
    scope = owner_q or ''

    if kind == 'Init':
        ctor_q = model.resolve_name(norm_type(mem['ctor_class']), '')
        params = mem['params']
        r.name = '__init__'
        r.static = False
        r.params = describe_params(model, params, '', mem['args'])
        r.ret = None
        cands = [(owner_hc, m) for m in (owner_hc['members'] if owner_hc else []) if m.get('type') == 'function' and m.get('ctor')]
        if mem.get('adapter_store'):
            r.adapter = 'ctor'
            cands = cands
        want = [model.canonical(p, '') for p in params]
        hit = None
        for hc, m in cands:
            if [model.canonical(p['type'], hc['qual']) for p in m['params']] == want:
                hit = (hc, m)
        if hit is None and not params:
            hit = None  # implicit default constructor
        elif hit is None and cands:
            same = [(hc, m) for hc, m in cands if len(m['params']) == len(params)]
            hit = same[0] if len(same) == 1 else None
            if hit is None:
                problems.append('%s: ctor %s(%s) not found' % (bf.rel, owner_q, ', '.join(params)))
        if hit:
            r.decl_class, r.decl = hit
        return r

    if kind == 'Field':
        target = mem['target']
        own, _, fname = target.rpartition('::')
        fq = model.resolve_name(norm_type(own), '')
        hc = model.hclasses.get(fq)
        found = model.find_members(hc, fname, 'field')
        if not found:
            problems.append('%s: field %s not found' % (bf.rel, target))
            r.type = '?'
        else:
            r.decl_class, r.decl = found[0]
            r.type = model.py_type(r.decl['ftype'], r.decl_class['qual'])
        r.static = False
        return r

    if kind == 'Constant':
        expr = mem['value']
        e = expr
        if e in bf.local_consts and bf.local_consts[e]['value']:
            e = bf.local_consts[e]['value']
        cq = None
        decl = None
        own, _, cname = e.replace('VWObjectAPI::', '').rpartition('::')
        if own:
            oq = model.resolve_name(own, '')
            if oq in model.hclasses:
                found = model.find_members(model.hclasses[oq], cname, 'field')
                if found:
                    r.decl_class, decl = found[0]
            if decl is None and (own + '::' + cname) in model.hconstants:
                decl = model.hconstants[own + '::' + cname]
        else:
            decl = model.hconstants.get(cname)
        if decl is None:
            problems.append('%s: constant %s not found' % (bf.rel, expr))
            r.type = '?'
            r.value = expr
        else:
            r.decl = decl
            r.type = model.py_type(decl['ftype'], r.decl_class['qual'] if r.decl_class else decl.get('scope', ''))
            r.value = decl.get('init')
        r.static = True
        return r

    # Def
    target = mem['target']
    sig = bindscan.parse_signature(mem['sig']) if mem.get('sig') else None
    sargs = mem['args']
    r.self_first = mem['self_first']
    if '::' not in target:
        # adapter in the binding file, or IsTrue<T>
        if target.startswith('IsTrue<'):
            r.adapter = 'IsTrue'
            r.static = False
            r.params = []
            r.ret = 'bool'
            return r
        ad = bf.adapters.get(target)
        if ad is None:
            problems.append('%s: adapter %s not found' % (bf.rel, target))
            return None
        r.adapter = target
        r.adapter_comment = ad['comment']
        params = ad['params']
        if mem['self_first']:
            params = params[1:]
        ptypes = []
        for p in params:
            m = re.match(r'^(.*?)([A-Za-z_]\w*)$', p.strip())
            ptypes.append(m.group(1).strip() if m and m.group(1).strip() else p)
        r.params = describe_params(model, ptypes, '', sargs)
        r.ret = model.py_type(ad['ret'], '')
        r.ret_cpp = ad['ret']
        r.static = not mem['self_first']
        # documentation of the wrapped API function: 'CDocument::As<T>(h): ...' in the adapter comment
        m = re.search(r'\b(C\w+|Math::C\w+)::(\w+)', ad['comment'] or '')
        if m:
            hq = model.resolve_name(m.group(1), '')
            found = model.find_members(model.hclasses.get(hq), m.group(2), 'function')
            if found:
                r.decl_class, r.decl = found[0]
        if r.decl is None and owner_hc is not None:
            found = model.find_members(owner_hc, r.name, 'function')
            if found:
                r.decl_class, r.decl = found[0]
        return r

    own, _, fname = target.rpartition('::')
    oq = model.resolve_name(own, '')
    if oq in model.haliases:
        a = model.haliases[oq]
        oq = model.resolve_name(norm_type(a['target']), a['scope'])
    if oq in model.hclasses:
        cands = model.find_members(model.hclasses[oq], fname, 'function')
        hit = model.match_overload(cands, sig, len(sargs), oq) if cands else None
        if hit is None:
            problems.append('%s: %s%s not resolved (%d candidates)' % (bf.rel, target, '' if not sig else str(sig['params']), len(cands)))
            if sig is None:
                return r
        else:
            r.decl_class, r.decl = hit
        decl_scope = r.decl_class['qual'] if r.decl_class else oq
        if sig:
            ptypes = sig['params']
            ret = sig['ret']
            static = sig['owner'] is None
            pscope = oq
        else:
            ptypes = [p['type'] for p in r.decl['params']]
            ret = r.decl['ret']
            static = r.decl['static']
            pscope = decl_scope
        if r.decl is not None and r.decl.get('friend'):
            static = False
        r.params = describe_params(model, ptypes, pscope, sargs)
        r.ret = model.py_type(ret, pscope if sig else decl_scope)
        r.ret_cpp = ret
        r.static = static
        if len(ptypes) != len(sargs):
            problems.append('%s: %s has %d params but %d SArgs' % (bf.rel, target, len(ptypes), len(sargs)))
        return r

    # free function in a namespace (module functions)
    fq = own.replace('VWObjectAPI::', '') + '::' + fname
    cands = [(None, f) for f in model.hfunctions.get(fq, [])]
    if not cands:
        problems.append('%s: free function %s not found' % (bf.rel, target))
        return r
    if len(cands) > 1 and sig:
        want = [model.canonical(p, own) for p in sig['params']]
        cands = [(h, f) for h, f in cands if [model.canonical(p['type'], own) for p in f['params']] == want] or cands
    r.decl = cands[0][1]
    ptypes = sig['params'] if sig else [p['type'] for p in r.decl['params']]
    ret = sig['ret'] if sig else r.decl['ret']
    r.params = describe_params(model, ptypes, own, sargs)
    r.ret = model.py_type(ret, own)
    r.ret_cpp = ret
    r.static = True
    return r


if __name__ == '__main__':
    import sys
    import collections
    m = Model(sys.argv[1], sys.argv[2])
    res, problems = resolve(m)
    print('resolved', len(res))
    for p in problems:
        print('PROBLEM', p)
    for p in sorted(set(m.problems)):
        print('TYPE', p)
    stats = collections.Counter()
    for r in res:
        if r.kind != 'Def':
            continue
        d = r.decl or {}
        if d.get('lead'):
            stats['lead'] += 1
        elif d.get('trail'):
            stats['trail-only'] += 1
        elif d.get('group'):
            stats['group-only'] += 1
        elif r.adapter:
            stats['adapter'] += 1
        else:
            stats['none'] += 1
    print(stats)
