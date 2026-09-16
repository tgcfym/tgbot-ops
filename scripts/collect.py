import json, os, urllib.request, datetime
B = 'https://tgcfym.us.ci'
def j(u, h=None):
    try:
        r = urllib.request.Request(u, headers=h or {'User-Agent': 'tgcf-stats'})
        with urllib.request.urlopen(r, timeout=25) as f:
            return f.status, json.load(f)
    except Exception as e:
        return getattr(e, 'code', 0), None
row = {'t': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}
s, h = j(B + '/health')
row['health'] = s
if isinstance(h, dict):
    row['bindings'] = sum(1 for v in (h.get('bindings') or {}).values() if v)
    row['service'] = h.get('service')
s, d = j(B + '/api/stats')
row['stats'] = s
if isinstance(d, dict):
    for k in ('users', 'active_24h', 'ai_messages', 'files', 'storage_bytes'):
        row[k] = d.get(k)
f = 'data/history.json'
old = json.load(open(f)) if os.path.exists(f) else []
old.append(row)
old = old[-2000:]
os.makedirs('data', exist_ok=True)
json.dump(old, open(f, 'w'), ensure_ascii=False, separators=(',', ':'))
print('appended ->', json.dumps(row, ensure_ascii=False))