"""The privacy screen (v318): solo, full page, Lead a project, an invite link, and what is recorded.
(based on f8join.py) F8 step 4, the invited person (v311), against fake Firebase modules (no network).
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
    pg.add_init_script("if(!sessionStorage.getItem('seeded')){sessionStorage.setItem('seeded','1');sessionStorage.setItem('fsdb',%s);localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');}" % (json.dumps(json.dumps(SEED)), json.dumps(solo)))

    LS = lambda k: pg.evaluate('k=>localStorage.getItem(k)', k)
    DB = lambda: pg.evaluate("()=>JSON.parse(sessionStorage.getItem('fsdb'))")
    def ok(name, cond): print(('PASS ' if cond else 'FAIL ') + name)
    G = lambda: pg.is_visible('#gsm-priv')
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm-priv', timeout=25000); pg.wait_for_timeout(300)
    print('--- solo screen\n' + pg.inner_text('#gsm-priv'))
    pg.screenshot(path=OUT + '_solo.png')
    ok('solo screen shown on first open', G() and 'WORKING ON YOUR OWN' in pg.inner_text('#gsm-priv'))
    ok('workbook is inert behind it', pg.evaluate("()=>document.getElementById('gsm').inert===true"))
    blocked = False
    try: pg.click('#gsm-nbgo', timeout=1500)
    except Exception: blocked = True
    ok('cannot click into the workbook', blocked)
    pg.keyboard.press('Escape'); pg.wait_for_timeout(100)
    ok('Escape does not close it', G())
    pg.mouse.click(5, 5); pg.wait_for_timeout(100)
    ok('clicking outside does not close it', G())
    for _ in range(5): pg.keyboard.press('Tab')
    ok('Tab stays inside', pg.evaluate("()=>document.getElementById('gsm-priv').contains(document.activeElement)"))
    pg.click('[data-pv=full]'); pg.wait_for_timeout(100)
    t = pg.inner_text('#gsm-priv'); print('--- full page from the screen\n' + t)
    ok('full page reachable before acknowledging', 'ANSWERING AN INVITE' in t and 'LEADING A PROJECT' in t and 'BCM administrator' in t and G())
    pg.screenshot(path=OUT + '_full.png')
    pg.click('[data-pv=ok]'); pg.wait_for_timeout(200)
    r = json.loads(LS('groundsmith-web-privacy') or '{}')
    ok('I understand closes it and records solo', not G() and r.get('solo', {}).get('v') == '2026-11-26.2' and 'join' not in r and 'lead' not in r)
    ok('workbook usable after', pg.evaluate("()=>document.getElementById('gsm').inert===false"))
    pg.fill('#gsm-nb', 'Pat'); ok('can type after', pg.input_value('#gsm-nb') == 'Pat')
    pg.reload(); pg.wait_for_selector('#gsm-ways', state='attached', timeout=25000); pg.wait_for_timeout(1200)
    ok('not asked again', not G())
    pg.click('#gsm-privlink'); pg.wait_for_timeout(150)
    ok('footer Privacy link opens the full page', G() and 'QUESTIONS' in pg.inner_text('#gsm-priv') and pg.is_visible('[data-pv=close]'))
    pg.keyboard.press('Escape'); pg.wait_for_timeout(100)
    pg.click('[data-pv=close]'); pg.wait_for_timeout(100)
    ok('Close closes the full page', not G())
    # an old version is asked again
    pg.evaluate("()=>localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'2026-01-01'}}))")
    pg.reload(); pg.wait_for_timeout(2500)
    ok('asked again when the text changes', G())
    pg.click('[data-pv=ok]'); pg.wait_for_timeout(100)
    # an invite link: the live screen
    LINK = 'http://t.local/#bcmjoin=PID1.' + KEY
    pg.goto(LINK); pg.wait_for_selector('#gsm-priv [data-pv=ok]', timeout=25000); pg.wait_for_timeout(300)
    t = pg.inner_text('#gsm-priv'); print('--- live screen\n' + t)
    pg.screenshot(path=OUT + '_live.png')
    ok('invite screen names the project and lead, even after solo', '“CANYON TEST”' in t and 'Test Lead sees everything you write here' in t and 'wouldn’t want Test Lead to read' in t and 'Delete my workbook' in t)
    ok('it is not the lead screen', 'BEFORE YOU LEAD' not in t)
    blocked = False
    try: pg.click('[data-j=go]', timeout=1500)
    except Exception: blocked = True
    ok('cannot Begin before acknowledging', blocked)
    pg.click('[data-pv=ok]'); pg.wait_for_timeout(200)
    pg.fill('#gsm-jn', 'Pat Tester'); pg.click('[data-j=v][data-v=Residents]'); pg.click('[data-j=go]')
    pg.wait_for_selector('#gsm-jline', timeout=25000); pg.wait_for_timeout(1500)
    ok('no screen after reload', not G())
    rec = DB().get('projects/PID1/workbooks/anon1') or {}
    pv = (rec.get('data') or {}).get('privacy') or {}
    ok('workbook record carries the acknowledgement', pv.get('v') == '2026-11-26.2' and bool(pv.get('at')))
    pg.evaluate("()=>{const r=JSON.parse(localStorage.getItem('groundsmith-web-privacy'));delete r.join;localStorage.setItem('groundsmith-web-privacy',JSON.stringify(r))}")
    pg.goto('http://t.local/#bcmjoin=PID9.' + KEY); pg.wait_for_timeout(3000)
    ok('a bad link leaves no screen', not G() and 'doesn' in pg.inner_text('#gsm-join'))
    print('ERRORS', errs)
    b.close()
