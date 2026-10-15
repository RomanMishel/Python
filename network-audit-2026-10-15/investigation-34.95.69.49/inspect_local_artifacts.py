import datetime as dt
import hashlib
import json
import re
import sqlite3
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

OUT = Path(__file__).resolve().parent
HOME = Path(r'C:\Users\seala')
LOCAL = HOME / 'AppData' / 'Local'
ROAMING = HOME / 'AppData' / 'Roaming'
TARGET = re.compile(r'34\.95\.69\.49|(?:[a-z0-9-]+\.)?clean\.gg', re.I)


def clean_url(value):
    try:
        u = urlsplit(value)
        return urlunsplit((u.scheme, u.hostname or '', u.path, '', ''))
    except ValueError:
        return '[malformed URL]'


def chrome_time(value):
    if not value:
        return None
    return (dt.datetime(1601, 1, 1, tzinfo=dt.timezone.utc) + dt.timedelta(microseconds=value)).isoformat()


roots = [LOCAL/'BraveSoftware'/'Brave-Browser'/'User Data', LOCAL/'Google'/'Chrome'/'User Data', LOCAL/'Microsoft'/'Edge'/'User Data']
profiles = []
for root in roots:
    if root.exists():
        profiles.extend(p for p in root.iterdir() if p.is_dir() and (p.name in {'Default', 'Guest Profile', 'System Profile'} or p.name.startswith('Profile ')))

history_results = []
state_results = []
for profile in profiles:
    history = profile/'History'
    if history.exists():
        item = {'Source': str(history), 'Size': history.stat().st_size, 'Status': 'OK'}
        try:
            con = sqlite3.connect(history.as_uri()+'?mode=ro', uri=True, timeout=2)
            con.execute('PRAGMA query_only=ON')
            rows = con.execute("SELECT id,url,visit_count,last_visit_time FROM urls WHERE url LIKE ? OR url LIKE ?", ('%34.95.69.49%', '%clean.gg%')).fetchall()
            item['Matches'] = [{'ID': r[0], 'URLWithoutQuery': clean_url(r[1]), 'VisitCount': r[2], 'LastVisitUTC': chrome_time(r[3])} for r in rows]
            tables = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            if 'downloads_url_chains' in tables:
                item['DownloadMatches'] = [{'ID': r[0], 'URLWithoutQuery': clean_url(r[1])} for r in con.execute("SELECT id,url FROM downloads_url_chains WHERE url LIKE ? OR url LIKE ?", ('%34.95.69.49%', '%clean.gg%'))]
            con.close()
        except (sqlite3.Error, OSError, OverflowError) as e:
            item['Status'] = 'ERROR'
            item['Error'] = str(e)
        history_results.append(item)
    state = profile/'Network'/'Network Persistent State'
    if state.exists():
        text = state.read_text(encoding='utf-8', errors='replace')
        hits = sorted(set(TARGET.findall(text)))
        state_results.append({'Source': str(state), 'MatchingHostsOrIPs': hits, 'Bytes': state.stat().st_size})

state = ROAMING/'Blitz'/'Network'/'Network Persistent State'
data = json.loads((OUT/'blitz-network-persistent-state.json').read_text(encoding='utf-8-sig'))
blitz_entries = []
def walk(value, path='$'):
    if isinstance(value, dict):
        if any(TARGET.search(str(v)) for v in value.values() if isinstance(v, (str, int, float))):
            blitz_entries.append({'JSONPath': path, 'Entry': value})
        for k, v in value.items():
            walk(v, path+'.'+k)
    elif isinstance(value, list):
        for i, v in enumerate(value):
            walk(v, f'{path}[{i}]')
walk(data)

logs = []
window_events = []
for file in [ROAMING/'Blitz'/'app.log', ROAMING/'Blitz'/'app.log.0', ROAMING/'Blitz'/'flutter-game-shim-ex.log', ROAMING/'Blitz'/'injector.log']:
    if not file.exists():
        continue
    raw = file.read_bytes()
    text = raw.decode('utf-8', errors='replace')
    hits = []
    for number, line in enumerate(text.splitlines(), 1):
        if TARGET.search(line):
            hits.append({'Line': number, 'Text': re.sub(r'STEAM_\d:\d:\d+', '[Steam ID redacted]', line)[:1500]})
        if file.name == 'app.log' and '2026-10-15' in line and ('Recreating window view' in line or 'Requesting CSGO_READ_LIVE_GAME' in line):
            window_events.append({'Line': number, 'Text': re.sub(r'STEAM_\d:\d:\d+', '[Steam ID redacted]', line)})
    logs.append({'Source': str(file), 'Bytes': len(raw), 'SHA256': hashlib.sha256(raw).hexdigest(), 'TargetMatches': hits})

result = {'CheckedAtUTC': dt.datetime.now(dt.timezone.utc).isoformat(), 'History': history_results, 'BrowserNetworkState': state_results, 'BlitzNetworkEntries': blitz_entries, 'BlitzLogs': logs, 'BlitzWindowEventsToday': window_events}
(OUT/'local-artifact-findings.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
(OUT/'blitz-window-events-redacted.txt').write_text('\n'.join(f'{e["Line"]}: {e["Text"]}' for e in window_events), encoding='utf-8')
print(json.dumps({'HistoryDatabases': len(history_results), 'HistoryMatches': sum(len(r.get('Matches', [])) for r in history_results), 'DownloadMatches': sum(len(r.get('DownloadMatches', [])) for r in history_results), 'HistoryErrors': [r for r in history_results if r['Status']!='OK'], 'BrowserStateMatches': [r for r in state_results if r['MatchingHostsOrIPs']], 'BlitzNetworkEntries': blitz_entries, 'BlitzLogTargetMatchCounts': [{'Source':r['Source'],'Count':len(r['TargetMatches'])} for r in logs], 'BlitzWindowEventsToday': len(window_events)}, ensure_ascii=True, indent=2))
