"""Compares a catalog with a running Vectorworks MCP server.

Read-only: it calls initialize, listToolGroups (includeTools) and tools/list, and never activates groups or calls any
other tool, so nothing changes in Vectorworks or in the session.

Checked for every group: present on the server, groupId, risk level, short description (= fDesc), tool count, tool
names (the server lists them in no particular order), tool descriptions and risk levels. For the tools in tools/list (those of the active groups): input
schema, description and the readOnly and destructive hints against the effect. The Core group against core.json and
its schemas against shared.CORE_SCHEMA (structure only; the published parameter descriptions are curated).
Warnings only: groups whose current activation differs from their default (that depends on the session).

Usage: python live.py <catalog.json> [--url http://localhost:8765] [--update-core]
"""

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import urllib.request  # noqa: E402

from mdlib import tool_safety  # noqa: E402

DEFAULT_URL = 'http://localhost:8765'
DESTRUCTIVE = {'HighRisk', 'RunsScript', 'OwnUndoHighRisk'}
HERE = os.path.dirname(os.path.abspath(__file__))


class Server:
    def __init__(self, url):
        self.url, self.session, self.next_id = url, None, 1

    def post(self, method, params=None, notify=False):
        body = {'jsonrpc': '2.0', 'method': method}
        if params is not None:
            body['params'] = params
        if not notify:
            body['id'] = self.next_id
            self.next_id += 1
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream'}
        if self.session:
            headers['Mcp-Session-Id'] = self.session
        req = urllib.request.Request(self.url, json.dumps(body).encode('utf-8'), headers)
        with urllib.request.urlopen(req, timeout=60) as r:
            self.session = r.headers.get('Mcp-Session-Id') or self.session
            raw = r.read().decode('utf-8')
        if notify:
            return None
        if raw.lstrip().startswith(('event:', 'data:')):     # an SSE stream: the last data line holds the reply
            raw = [l[5:].strip() for l in raw.splitlines() if l.startswith('data:')][-1]
        reply = json.loads(raw)
        if 'error' in reply:
            raise RuntimeError('%s: %s' % (method, reply['error']))
        return reply['result']

    def call(self, tool, arguments):
        result = self.post('tools/call', {'name': tool, 'arguments': arguments})
        if result.get('isError'):
            raise RuntimeError('%s: %s' % (tool, result['content'][0]['text']))
        return json.loads(result['content'][0]['text'])


def fetch(url):
    """(listToolGroups groups, tools/list tools) of the server at `url`."""
    s = Server(url)
    s.post('initialize', {'protocolVersion': '2025-03-26', 'capabilities': {},
                          'clientInfo': {'name': 'mcp-docs-check', 'version': '1'}})
    s.post('notifications/initialized', notify=True)
    groups = s.call('listToolGroups', {'includeTools': True})['groups']
    tools, cursor = [], None
    while True:
        result = s.post('tools/list', {'cursor': cursor} if cursor else {})
        tools += result['tools']
        cursor = result.get('nextCursor')
        if not cursor:
            return groups, tools


def _strip_descriptions(value):
    if isinstance(value, dict):
        return {k: _strip_descriptions(v) for k, v in value.items() if k != 'description'}
    if isinstance(value, list):
        return [_strip_descriptions(v) for v in value]
    return value


def compare(cat, live_groups, live_tools, core):
    """(problems, warnings): differences between the catalog (and core.json) and the server."""
    from shared import CORE_SCHEMA
    problems, warnings = [], []
    by_id = {g['groupId']: g for g in live_groups}
    listed = {t['name']: t for t in live_tools}
    for g in cat:
        live = by_id.pop(g['groupId'], None)
        where = 'group %s (%s)' % (g['fName'], g['groupId'])
        if live is None:
            problems.append('%s: not on the server' % where)
            continue
        for key, mine, theirs in (('display name', g['fName'], live.get('displayName')),
                                  ('risk level', g['fSafetyLevel'], live.get('safetyLevel')),
                                  ('short description', g['fDesc'], live.get('shortDescription')),
                                  ('tool count', len(g['tools']), live.get('toolCount'))):
            if mine != theirs:
                problems.append('%s: %s differs: catalog %r, server %r' % (where, key, mine, theirs))
        if live.get('currentlyActive') != g['fActiveByDefault']:
            warnings.append('%s: currently %s, %s by default' % (
                where, 'active' if live.get('currentlyActive') else 'inactive',
                'active' if g['fActiveByDefault'] else 'inactive'))
        # the server lists the tools of a group in no particular order; the pages keep the definition order
        names = [t['name'] for t in g['tools']]
        theirs = [t['name'] for t in live.get('tools') or []]
        if sorted(names) != sorted(theirs):
            problems.append('%s: tools differ: only in catalog %s, only on server %s' % (
                where, sorted(set(names) - set(theirs)), sorted(set(theirs) - set(names))))
        live_tool = {t['name']: t for t in live.get('tools') or []}
        for t in g['tools']:
            lt = live_tool.get(t['name'])
            if lt is None:
                continue
            if lt.get('description') != t['description']:
                problems.append('tool %s: description differs' % t['name'])
            if lt.get('safetyLevel') != tool_safety(t['effect'], g['fSafetyLevel']):
                problems.append('tool %s: risk level %r on the server, %r from effect %s' % (
                    t['name'], lt.get('safetyLevel'), tool_safety(t['effect'], g['fSafetyLevel']), t['effect']))
            lt = listed.pop(t['name'], None)
            if lt is None:
                continue
            if lt.get('inputSchema') != t['inputSchema']:
                problems.append('tool %s: input schema differs' % t['name'])
            if lt.get('description') != t['description']:
                problems.append('tool %s: description in tools/list differs' % t['name'])
            hints = lt.get('annotations') or {}
            if bool(hints.get('readOnlyHint')) != (t['effect'] == 'ReadOnly'):
                problems.append('tool %s: readOnlyHint %r, effect %s' % (t['name'], hints.get('readOnlyHint'), t['effect']))
            if bool(hints.get('destructiveHint')) != (t['effect'] in DESTRUCTIVE):
                problems.append('tool %s: destructiveHint %r, effect %s' % (
                    t['name'], hints.get('destructiveHint'), t['effect']))

    live_core = by_id.pop(core['groupId'], None)
    if live_core is None:
        problems.append('group Core (%s): not on the server' % core['groupId'])
    else:
        for key in ('displayName', 'safetyLevel', 'shortDescription', 'toolCount', 'tools'):
            mine, theirs = core.get(key), live_core.get(key)
            if key == 'tools':
                mine, theirs = (sorted(x or [], key=lambda t: t.get('name')) for x in (mine, theirs))
            if mine != theirs:
                problems.append('group Core: %s differs from core.json (run live.py with --update-core, then review '
                                'the Core texts in shared.py)' % key)
    for name, schema in CORE_SCHEMA.items():
        lt = listed.pop(name, None)
        if lt is None:
            problems.append('Core tool %s: not in tools/list' % name)
        elif _strip_descriptions(lt.get('inputSchema')) != _strip_descriptions(schema):
            problems.append('Core tool %s: input schema differs from shared.CORE_SCHEMA' % name)
    for g in by_id.values():
        problems.append('group %s (%s): on the server, not in the catalog' % (g.get('displayName'), g.get('groupId')))
    for name in listed:
        problems.append('tool %s: in tools/list, not in the catalog' % name)
    return problems, warnings


def check(cat, url=DEFAULT_URL, update_core=False):
    """Prints the differences; returns the number of problems (warnings do not count)."""
    core_path = os.path.join(HERE, 'core.json')
    with open(core_path, encoding='utf-8') as f:
        core = json.load(f)
    try:
        live_groups, live_tools = fetch(url)
    except OSError as ex:
        print('Cannot reach the Vectorworks MCP server at %s: %s' % (url, ex))
        print('Start Vectorworks with the MCP server, or leave out the live check.')
        return 1
    if update_core:
        live_core = next(g for g in live_groups if g.get('groupId') == core['groupId'])
        with open(core_path, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(live_core, f, indent=1, ensure_ascii=False)
        print('core.json updated from the server')
        core = live_core
    problems, warnings = compare(cat, live_groups, live_tools, core)
    for w in warnings:
        print('warning: %s' % w)
    for p in problems:
        print(p)
    print('%d groups and %d listed tools on the server, %d problems, %d warnings'
          % (len(live_groups), len(live_tools), len(problems), len(warnings)))
    return len(problems)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('catalog', help='catalog.json (from extract.py or the build work folder)')
    p.add_argument('--url', default=DEFAULT_URL, help='server URL (default: %(default)s)')
    p.add_argument('--update-core', action='store_true', help='rewrite core.json from the server first')
    a = p.parse_args()
    with open(a.catalog, encoding='utf-8') as f:
        sys.exit(1 if check(json.load(f), a.url, a.update_core) else 0)
