#!/usr/bin/env python3
"""Validate minimal invariants of Network Atlas's JSON registry (stdlib only)."""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'data' / 'resources.json'
ALLOWED_PRIMARY = {
    'desktop_exploration','web_hosted','python_analysis','web_visualization','r_analysis',
    'scale_distributed','higher_order_temporal','research_layout_algorithms','datasets_benchmarks',
    'graph_database_query','infrastructure_topology','domain_data_sources','domain_solutions','existing_repositories','learning_research','needs_triage'
}
REQUIRED = {'id','name','url','primary_category','role','interfaces','network_types','scale_profile','maturity','cost_model','verification_status','source_origin','notes'}

def main():
    try:
        data = json.loads(REGISTRY.read_text(encoding='utf-8'))
    except Exception as e:
        print(f'ERROR: cannot parse {REGISTRY}: {e}', file=sys.stderr)
        return 2
    if not isinstance(data, list):
        print('ERROR: registry root must be a JSON array', file=sys.stderr)
        return 2
    ids = set()
    errors = []
    for i, item in enumerate(data):
        where = f'entry[{i}]'
        if not isinstance(item, dict):
            errors.append(f'{where}: expected object')
            continue
        missing = REQUIRED - set(item)
        if missing: errors.append(f'{where}: missing fields {sorted(missing)}')
        rid = item.get('id','')
        if not isinstance(rid, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', rid):
            errors.append(f'{where}: invalid id {rid!r}')
        if rid in ids: errors.append(f'{where}: duplicate id {rid}')
        ids.add(rid)
        url = item.get('url','')
        if not isinstance(url, str) or not url.startswith(('https://','http://')):
            errors.append(f'{where}: URL must start with http:// or https://')
        cat = item.get('primary_category')
        if cat not in ALLOWED_PRIMARY: errors.append(f'{where}: unknown primary_category {cat!r}')
        for field in REQUIRED - {'id'}:
            if field not in item: continue
            if field in {'interfaces','network_types'}:
                if not isinstance(item[field], list) or not item[field] or any(not isinstance(x,str) or not x.strip() for x in item[field]):
                    errors.append(f'{where}: {field} must be a non-empty array of strings')
            elif not isinstance(item[field], str) or not item[field].strip():
                errors.append(f'{where}: {field} must be non-empty string')
    if errors:
        print('Registry validation FAILED:')
        for err in errors: print(f'- {err}')
        return 1
    print(f'OK: {len(data)} resources; {len(ids)} unique IDs; required fields and primary categories valid.')
    unresolved = [r['name'] for r in data if r.get('verification_status') == 'needs_link_resolution']
    if unresolved:
        print('Manual link resolution still required for: ' + ', '.join(unresolved))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
