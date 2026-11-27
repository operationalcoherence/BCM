"""F8 step 4, the invited person (v311), against fake Firebase modules (no network).
python3 -I f8join.py JS SOLO_WORKBOOK.json WIDTH OUTPREFIX
The fake database and the anonymous user live in sessionStorage so they survive page reloads.
Walks: open the invite link (own workbook parked), name and voice, Begin, live save, an edit sent when the page is
hidden, Pause and Resume, the daily limit, back to own workbook and back again, the lead closing the project,
Delete my workbook, a bad link, and a place-map project."""
import json, sys
from playwright.sync_api import sync_playwright
JS, WB, W, OUT = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
SRC = open(JS, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0"><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
APP = b'export function initializeApp(c,n){return {c,n}}'
AUTH = b'''let cur=JSON.parse(sessionStorage.getItem('fauth')||'null'),subs=[];const fire=()=>{sessionStorage.setItem('fauth',JSON.stringify(cur));subs.forEach(f=>f(cur))};
export function getAuth(){return {get currentUser(){return cur},authStateReady:()=>Promise.resolve()}}
export function onAuthStateChanged(a,f){subs.push(f);setTimeout(()=>f(cur),0)}
export class GoogleAuthProvider{setCustomParameters(){}}
export function signInWithPopup(){cur={uid:'lead1',isAnonymous:false,displayName:'Test Lead',email:'lead@example.com'};fire();return Promise.resolve({user:cur})}
export function signInAnonymously(){window.__anon=(window.__anon||0)+1;cur={uid:'anon1',isAnonymous:true};fire();return Promise.resolve({user:cur})}
export function signOut(){cur=null;fire();return Promise.resolve()}'''
FS = b'''const D=JSON.parse(sessionStorage.getItem('fsdb')||'{}'),L=JSON.parse(sessionStorage.getItem('fslog')||'[]');window.__fsdb=D;window.__fslog=L;
const keep=()=>{sessionStorage.setItem('fsdb',JSON.stringify(D));sessionStorage.setItem('fslog',JSON.stringify(L))};
const path=a=>a.join('/');
export function getFirestore(){return {}}
export function collection(db,...p){return {kind:'col',path:path(p)}}
export function doc(x,...p){const q=path(p);return {kind:'doc',path:q,id:q.split('/').pop()}}
export function serverTimestamp(){return {seconds:Math.floor(Date.now()/1000)}}
export function getDoc(r){L.push('get '+r.path);keep();const d=D[r.path];return Promise.resolve({exists:()=>!!d,data:()=>d})}
export function setDoc(r,d){if(sessionStorage.getItem('fcap'))return Promise.reject({code:'resource-exhausted'});
 const m=/^projects\\/([^/]+)\\/workbooks\\//.exec(r.path);if(m){const k=D['projects/'+m[1]+'/keys/'+d.key];if(!k||k.open!==true)return Promise.reject({code:'permission-denied'});
 const ks=Object.keys(d).sort().join(',');if(ks!=='data,key,name,saved,uid,voice'||typeof d.data!=='object')return Promise.reject({code:'permission-denied',message:'shape '+ks})}
 L.push('set '+r.path);D[r.path]=JSON.parse(JSON.stringify(d));keep();return Promise.resolve()}
export function deleteDoc(r){L.push('delete '+r.path);delete D[r.path];keep();return Promise.resolve()}'''
KEY = 'K' * 8 + 'abcdefghjkmnpqrstuvwxyz2'  # 32 characters
INV = {'open': True, 'pid': 'PID1', 'name': 'Canyon test', 'goal': 'Keep the trail open for everyone.', 'voices': ['Residents', 'Fire crews'], 'due': '2026-12-15', 'map': {'kind': 'line'}, 'leadName': 'Test Lead'}
PL = {'c': [[40.0, -105.3]], 'loc': {'name': 'Bear Canyon', 'lat': 40.0, 'lon': -105.3}, 'name': 'Bear Canyon'}
INV2 = dict(INV, pid='PID2', name='Place test', map={'kind': 'place', 'name': 'Bear Canyon', 'p': json.dumps(PL)})
SEED = {'projects/PID1': {'lead': 'lead1'}, 'projects/PID1/keys/' + KEY: INV, 'projects/PID2/keys/' + KEY: INV2}
solo = json.dumps(json.load(open(WB))['data'])
def same(x):
    # the workbook tidies its own record when it opens (ids, history), so compare what the person wrote
    try:
        a, b = json.loads(x), json.loads(solo)
    except Exception:
        return False
    return all(a.get(k) == b.get(k) for k in ('goal', 'a', 'voices')) and [r[:4] for r in a.get('m', [])] == [r[:4] for r in b.get('m', [])] and a.get('p', {}).get('m') == b.get('p', {}).get('m')
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': W, 'height': 900}, is_mobile=W < 600, has_touch=W < 600)
    pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    pg.on('console', lambda m: m.type == 'error' and 'Failed to load resource' not in m.text and errs.append('console: ' + m.text[:150]))
    def route(r):
        u = r.request.url
        if u.startswith('http://t.local/?') or u.startswith('http://t.local/#') or u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.endswith('/firebase-app.js'): r.fulfill(status=200, content_type='application/javascript', body=APP, headers={'access-control-allow-origin': '*'})
        elif u.endswith('/firebase-auth.js'): r.fulfill(status=200, content_type='application/javascript', body=AUTH, headers={'access-control-allow-origin': '*'})
        elif u.endswith('/firebase-firestore.js'): r.fulfill(status=200, content_type='application/javascript', body=FS, headers={'access-control-allow-origin': '*'})
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("if(!sessionStorage.getItem('seeded')){sessionStorage.setItem('seeded','1');sessionStorage.setItem('fsdb',%s);localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},live:{v:'9999'}}));}" % (json.dumps(json.dumps(SEED)), json.dumps(solo)))
    LS = lambda k: pg.evaluate('k=>localStorage.getItem(k)', k)
    DB = lambda: pg.evaluate("()=>JSON.parse(sessionStorage.getItem('fsdb'))")
    T = lambda: pg.inner_text('#gsm-join')
    hide = lambda: pg.evaluate("()=>{Object.defineProperty(document,'visibilityState',{value:'hidden',configurable:true});document.dispatchEvent(new Event('visibilitychange'));Object.defineProperty(document,'visibilityState',{value:'visible',configurable:true})}")
    def ok(name, cond): print(('PASS ' if cond else 'FAIL ') + name)
    LINK = 'http://t.local/#bcmjoin=PID1.' + KEY
    pg.goto(LINK); pg.wait_for_selector('#gsm-join [data-j=go]', timeout=25000)
    print('--- ask view\n' + T())
    ok('own workbook parked', same(LS('groundsmith-web-v1-solo')) and LS('groundsmith-web-v1') is None)
    pg.fill('#gsm-jn', ''); pg.click('[data-j=go]'); pg.wait_for_timeout(150); print('no name:', pg.inner_text('#gsm-join .jmsg'))
    pg.fill('#gsm-jn', 'Pat Tester'); pg.click('[data-j=go]'); pg.wait_for_timeout(150); print('no voice:', pg.inner_text('#gsm-join .jmsg'))
    pg.click('[data-j=oth]'); pg.wait_for_timeout(100)
    ok('name kept after choosing Other', pg.input_value('#gsm-jn') == 'Pat Tester')
    pg.fill('#gsm-jo', 'Trail runners')
    pg.screenshot(path=OUT + '_ask.png', full_page=False)
    pg.click('[data-j=go]'); pg.wait_for_selector('#gsm-jline', timeout=25000); pg.wait_for_timeout(1200)
    print('--- bar\n' + T())
    rec = DB().get('projects/PID1/workbooks/anon1')
    ok('first save written', bool(rec) and rec['name'] == 'Pat Tester' and rec['voice'] == 'Trail runners' and rec['key'] == KEY)
    w = json.loads(rec['data']['json']) if rec else {}
    ok('workbook has the lead goal, name and voices', w.get('goal') == INV['goal'] and w.get('who') == 'Pat Tester' and 'Trail runners' in w.get('voices', []) and 'Residents' in w.get('voices', []))
    ok('goal is read-only', pg.evaluate("()=>document.querySelector('#gsm textarea.goal').readOnly") and pg.input_value('#gsm textarea.goal') == INV['goal'])
    ok('saved line', 'saved just now' in T())
    pg.screenshot(path=OUT + '_bar.png', full_page=False)
    n0 = len([l for l in pg.evaluate('()=>__fslog') if l.startswith('set')])
    hide(); pg.wait_for_timeout(500)
    ok('no write when nothing changed', len([l for l in pg.evaluate('()=>__fslog') if l.startswith('set')]) == n0)
    pg.evaluate("()=>{const w=JSON.parse(localStorage.getItem('groundsmith-web-v1'));w.a[0]='Because the lease ran out.';localStorage.setItem('groundsmith-web-v1',JSON.stringify(w))}")
    hide(); pg.wait_for_timeout(500)
    ok('edit sent when page hidden', 'lease ran out' in DB()['projects/PID1/workbooks/anon1']['data']['json'])
    pg.click('[data-j=pause]'); pg.wait_for_timeout(200); print('paused:', pg.inner_text('#gsm-jline'))
    pg.evaluate("()=>{const w=JSON.parse(localStorage.getItem('groundsmith-web-v1'));w.a[1]='PAUSED EDIT';localStorage.setItem('groundsmith-web-v1',JSON.stringify(w))}")
    hide(); pg.wait_for_timeout(400)
    ok('nothing sent while paused', 'PAUSED EDIT' not in DB()['projects/PID1/workbooks/anon1']['data']['json'])
    pg.click('[data-j=pause]'); pg.wait_for_timeout(500)
    ok('resume sends', 'PAUSED EDIT' in DB()['projects/PID1/workbooks/anon1']['data']['json'])
    pg.evaluate("()=>sessionStorage.setItem('fcap','1')")
    pg.evaluate("()=>{const w=JSON.parse(localStorage.getItem('groundsmith-web-v1'));w.a[2]='CAP EDIT';localStorage.setItem('groundsmith-web-v1',JSON.stringify(w))}")
    hide(); pg.wait_for_timeout(400); print('limit:', pg.inner_text('#gsm-jline'))
    pg.evaluate("()=>sessionStorage.removeItem('fcap')")
    for tab in (0, 1, 2, 4):
        pg.evaluate('t=>window.gsmTab(t)', tab); pg.wait_for_timeout(200)
        ok('bar visible on tab %d' % tab, pg.is_visible('#gsm-join'))
    # back to own workbook, then back to the project
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm-ways', state='attached', timeout=25000); pg.wait_for_timeout(500)
    ok('own workbook back', same(LS('groundsmith-web-v1')) and LS('groundsmith-web-v1-solo') is None and not pg.is_visible('#gsm-join'))
    ok('project copy kept', 'CAP EDIT' in (LS('groundsmith-web-f8wb-PID1') or ''))
    pg.goto(LINK); pg.wait_for_selector('#gsm-jline', timeout=25000); pg.wait_for_timeout(1200)
    ok('project workbook back, limit edit sent on return', 'CAP EDIT' in (LS('groundsmith-web-v1') or '') and 'CAP EDIT' in DB()['projects/PID1/workbooks/anon1']['data']['json'])
    # the lead changes the goal
    pg.evaluate("k=>{const d=JSON.parse(sessionStorage.getItem('fsdb'));d['projects/PID1/keys/'+k].goal='A changed goal.';sessionStorage.setItem('fsdb',JSON.stringify(d))}", KEY)
    pg.reload(); pg.wait_for_selector('#gsm-jline', timeout=25000); pg.wait_for_timeout(2500)
    ok('lead goal change taken', pg.input_value('#gsm textarea.goal') == 'A changed goal.')
    # the lead closes the project
    pg.evaluate("k=>{const d=JSON.parse(sessionStorage.getItem('fsdb'));d['projects/PID1/keys/'+k].open=false;sessionStorage.setItem('fsdb',JSON.stringify(d))}", KEY)
    pg.reload(); pg.wait_for_selector('#gsm-jline', timeout=25000); pg.wait_for_timeout(1200)
    print('closed:', pg.inner_text('#gsm-jline'))
    pg.evaluate("k=>{const d=JSON.parse(sessionStorage.getItem('fsdb'));d['projects/PID1/keys/'+k].open=true;sessionStorage.setItem('fsdb',JSON.stringify(d))}", KEY)
    # delete my workbook
    pg.click('[data-j=del]'); pg.wait_for_timeout(150); print('delete ask:', pg.inner_text('#gsm-join .warn'))
    pg.click('[data-j=delyes]'); pg.wait_for_url('http://t.local/', timeout=10000); pg.wait_for_selector('#gsm-ways', state='attached', timeout=25000); pg.wait_for_timeout(500)
    ok('deleted in project', 'projects/PID1/workbooks/anon1' not in DB())
    ok('deleted on device, own workbook back', same(LS('groundsmith-web-v1')) and LS('groundsmith-web-f8wb-PID1') is None and LS('groundsmith-web-f8me-PID1') is None and LS('groundsmith-web-f8cur') is None)
    # a bad link
    pg.goto('http://t.local/#bcmjoin=PID9.' + KEY); pg.wait_for_timeout(2500); print('bad link:', T())
    # a place-map project
    pg.goto('http://t.local/#bcmjoin=PID2.' + KEY); pg.wait_for_selector('#gsm-join [data-j=go]', timeout=25000)
    ok('switching projects keeps own workbook parked', same(LS('groundsmith-web-v1-solo')))
    pg.fill('#gsm-jn', 'Pat Tester'); pg.click('[data-j=v][data-v=Residents]'); pg.click('[data-j=go]'); pg.wait_for_selector('#gsm-jline', timeout=25000); pg.wait_for_timeout(1200)
    w2 = json.loads(LS('groundsmith-web-v1'))
    ok('place map carried', w2['p'].get('c') == PL['c'] and w2['p'].get('name') == 'Bear Canyon')
    ok('voice chip saved', DB()['projects/PID2/workbooks/anon1']['voice'] == 'Residents')
    print('anonymous sign-ins this page:', pg.evaluate('()=>window.__anon||0'))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm-ways', state='attached', timeout=25000)
    ok('own workbook back at the end', same(LS('groundsmith-web-v1')))
    print('ERRORS', errs)
    b.close()
