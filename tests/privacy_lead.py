"""The privacy screen on Lead a project (v318).\n(based on f8read.py) F8 step 6, the dashboard reading (v313): READING THEM TOGETHER and See everyone's ground together.
python3 -I f8read.py JS WORKBOOK.json WIDTH OUTPREFIX
(based on f8dash.py) F8 step 5, EVERY WORKBOOK (v312), against fake Firebase modules (no network).
python3 -I f8dash.py JS WORKBOOK.json WIDTH OUTPREFIX
(based on f8lead.py) F8 step 3, Lead a project (v309, v310), against fake Firebase modules (no network).
python3 -I f8lead.py JS WORKBOOK.json WIDTH OUTPREFIX
Signs in as a fake Google lead, creates a project, edits it, shows the QR code, deletes it,
and prints every write the page made, in order, so the delete order can be checked."""
import json, sys, os
from playwright.sync_api import sync_playwright
JS, WB, W, OUT = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
SRC = open(JS, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0"><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
APP = b'export function initializeApp(c,n){return {c,n}}'
AUTH = b'''let cur=null,subs=[];const fire=()=>subs.forEach(f=>f(cur));
export function getAuth(){return {get currentUser(){return cur},authStateReady:()=>Promise.resolve()}}
export function onAuthStateChanged(a,f){subs.push(f);setTimeout(()=>f(cur),0)}
export class GoogleAuthProvider{setCustomParameters(){}}
export function signInWithPopup(){cur={uid:'lead1',isAnonymous:false,displayName:'Test Lead',email:'lead@example.com'};fire();return Promise.resolve({user:cur})}
export function signInAnonymously(){cur={uid:'anon1',isAnonymous:true};fire();return Promise.resolve({user:cur})}
export function signOut(){cur=null;fire();return Promise.resolve()}'''
FS = b'''const D=window.__fsdb={},L=window.__fslog=[];let n=0;
const path=a=>a.join('/');
export function getFirestore(){return {}}
export function collection(db,...p){return {kind:'col',path:path(p)}}
export function doc(x,...p){if(x&&x.kind==='col'&&!p.length){n++;return {kind:'doc',path:x.path+'/AUTO'+n,id:'AUTO'+n}}const q=path(p);return {kind:'doc',path:q,id:q.split('/').pop()}}
export function serverTimestamp(){return {seconds:Math.floor(Date.now()/1000)}}
export function where(f,o,v){return {f,v}}
export function query(c,w){return {kind:'col',path:c.path,w}}
export function setDoc(r,d){L.push('set '+r.path);if(JSON.stringify(d).length>1e6)throw {code:'too-big'};D[r.path]=JSON.parse(JSON.stringify(d));return Promise.resolve()}
export function updateDoc(r,d){L.push('update '+r.path);if(!D[r.path])return Promise.reject({code:'not-found'});Object.assign(D[r.path],JSON.parse(JSON.stringify(d)));return Promise.resolve()}
export function getDoc(r){return Promise.resolve({exists:()=>!!D[r.path],data:()=>D[r.path]})}
export function deleteDoc(r){L.push('delete '+r.path);delete D[r.path];return Promise.resolve()}
export function getDocs(q){const pre=q.path+'/';const docs=Object.keys(D).filter(k=>k.startsWith(pre)&&!k.slice(pre.length).includes('/')).filter(k=>!q.w||D[k][q.w.f]===q.w.v).map(k=>({id:k.slice(pre.length),ref:{kind:'doc',path:k},data:()=>D[k]}));return Promise.resolve({docs})}'''

wb = json.load(open(WB))['data']
def mk(goal, a, notes):
    return json.dumps({'goal': goal, 'a': a, 'm': notes, 'p': {'m': []}, 'voices': [], 'links': [], 'others': [], 'who': ''})
G = 'Open a satellite clinic on Broad Street that residents trust and use.'
A1 = ['The hospital board fears losing referrals.', 'The hospital board opposes the satellite clinic.', 'The school nurse already refers families.', 'Past closures.', 'Hold open meetings.', 'Weekly hours.', 'A shared calendar.']
A2 = ['Residents remember the last closure.', 'The hospital board worries about referrals.', 'The school nurse and the pastor.', 'Bus routes.', 'Ask the pastor to host.', 'Evening hours.', 'A sign-up sheet.']
A3 = ['Funding is short.', '', 'Fire crews support it.', '', '', '', '']
N1 = [[2, 60, 60, 'The satellite clinic would bring care within walking distance.', None, 1, 0, None, 'a1'],
      [3, 80, 70, 'The school nurse refers families every week.', None, 1, 0, None, 'a2'],
      [2, 150, 170, 'Bus routes do not reach Broad Street on Sundays.', None, 3, 1, None, 'a3']]
N2 = [[2, 70, 180, 'Residents see the satellite clinic as another promise that will close.', None, 2, 1, None, 'b1'],
      [3, 90, 50, 'The school nurse is trusted by parents.', None, 1, 3, None, 'b2'],
      [1, 120, 190, 'The hospital board resists sharing referrals.', None, 4, 3, None, 'b3']]
N3 = [[2, 40, 40, 'Fire crews already run a health check at the station.', None, 1, 3, None, 'c1']]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    ctx = b.new_context(viewport={'width': W, 'height': 900}, is_mobile=W < 600, has_touch=W < 600)
    pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    pg.on('console', lambda m: m.type == 'error' and 'Failed to load resource' not in m.text and errs.append('console: ' + m.text[:150]))
    def route(r):
        u = r.request.url
        if u.startswith('http://t.local/?') or u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=open(os.path.join(os.path.dirname(os.path.abspath(JS)),'gsm-relief.js'),'rb').read())
        elif u.endswith('/firebase-app.js'): r.fulfill(status=200, content_type='application/javascript', body=APP, headers={'access-control-allow-origin': '*'})
        elif u.endswith('/firebase-auth.js'): r.fulfill(status=200, content_type='application/javascript', body=AUTH, headers={'access-control-allow-origin': '*'})
        elif u.endswith('/firebase-firestore.js'): r.fulfill(status=200, content_type='application/javascript', body=FS, headers={'access-control-allow-origin': '*'})
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("if(!localStorage.getItem('t-init')){localStorage.setItem('t-init','1');localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},x:0}));}" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/?f8test=1'); pg.wait_for_selector('#gsm-wlead', timeout=25000); pg.wait_for_timeout(500)
    def ok(n, c): print(('PASS ' if c else 'FAIL ') + n)
    ok('no screen for solo (already acknowledged)', not pg.is_visible('#gsm-priv'))
    pg.click('#gsm-wlead'); pg.wait_for_timeout(300)
    ok('Lead a project asks first', pg.is_visible('#gsm-priv') and 'shared project' in pg.inner_text('#gsm-priv'))
    ok('sign-in not opened yet', not pg.is_visible('[data-l=signin]'))
    pg.click('[data-pv=ok]'); pg.wait_for_timeout(600)
    ok('then carries on to sign-in', pg.is_visible('[data-l=signin]'))
    pg.click('[data-l=signin]'); pg.wait_for_timeout(500)
    pg.click('[data-l=new]'); pg.wait_for_timeout(300)
    pg.fill('#gsm-lpn', 'Privacy test'); pg.fill('#gsm-lpg', 'A goal.')
    pg.click('[data-l=save]'); pg.wait_for_timeout(700)
    db = pg.evaluate('()=>__fsdb'); pk = [k for k in db if k.count('/') == 1][0]; kk = [k for k in db if '/keys/' in k][0]
    ok('project record carries the acknowledgement', (db[pk].get('privacy') or {}).get('v') == '2026-11-26')
    ok('invite key does not', 'privacy' not in db[kk])
    pg.fill('#gsm-lpg', 'An edited goal.'); pg.click('[data-l=save]'); pg.wait_for_timeout(500)
    ok('kept after an edit', (pg.evaluate('()=>__fsdb')[pk].get('privacy') or {}).get('v') == '2026-11-26')
    pg.click('#gsm-wlead'); pg.wait_for_timeout(300)
    ok('not asked again', not pg.is_visible('#gsm-priv'))
    print('ERRORS', errs)
    b.close()
