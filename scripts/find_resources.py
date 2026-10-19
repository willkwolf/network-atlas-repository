#!/usr/bin/env python3
"""Search Network Atlas resources by primary category, tags, status, or free text."""
from pathlib import Path
import argparse, json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'data' / 'resources.json'

def main():
    parser = argparse.ArgumentParser(description='Find graph/network resources in Network Atlas')
    parser.add_argument('--category', help='Exact primary category, e.g. web_visualization')
    parser.add_argument('--interface', help='Interface tag, e.g. python, desktop, webgl')
    parser.add_argument('--network-type', help='Network/model tag, e.g. temporal, hypergraph, biological')
    parser.add_argument('--status', help='Exact verification status, e.g. needs_link_resolution')
    parser.add_argument('--text', help='Substring across name, role, notes, URL and tags')
    parser.add_argument('--json', action='store_true', help='Print matching entries as JSON')
    args = parser.parse_args()
    data = json.loads(REGISTRY.read_text(encoding='utf-8'))
    q = (args.text or '').casefold()
    found = []
    for r in data:
        if args.category and r['primary_category'] != args.category: continue
        if args.interface and args.interface.casefold() not in [x.casefold() for x in r['interfaces']]: continue
        if args.network_type and args.network_type.casefold() not in [x.casefold() for x in r['network_types']]: continue
        if args.status and r['verification_status'] != args.status: continue
        if q:
            blob = ' '.join([r['name'],r['role'],r['notes'],r['url'],r['primary_category'],*r['interfaces'],*r['network_types']]).casefold()
            if q not in blob: continue
        found.append(r)
    if args.json:
        print(json.dumps(found, ensure_ascii=False, indent=2))
    else:
        for r in found:
            print(f"{r['name']} [{r['primary_category']}] — {r['url']}\n  Interfaces: {', '.join(r['interfaces'])}; models: {', '.join(r['network_types'])}; verification: {r['verification_status']}\n  {r['role']}\n")
    print(f'# {len(found)} recurso(s)', file=__import__('sys').stderr)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
