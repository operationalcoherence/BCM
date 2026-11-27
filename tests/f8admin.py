"""F8 step 5b, the admin page (v314), at #bcmadmin.
python3 -I f8admin.py JS WORKBOOK.json WIDTH OUTPREFIX EMAIL
(based on f8dash.py) F8 step 5, EVERY WORKBOOK (v312), against fake Firebase modules (no network).
python3 -I f8dash.py JS WORKBOOK.json WIDTH OUTPREFIX
(based on f8lead.py) F8 step 3, Lead a project (v309, v310), against fake Firebase modules (no network).
python3 -I f8lead.py JS WORKBOOK.json WIDTH OUTPREFIX
Signs in as a fake Google lead, creates a project, edits it, shows the QR code, deletes it,
and prints every write the page made, in order, so the delete order can be checked."""
import json, sys
from playwright.sync_api import sync_playwright
JS, WB, W, OUT = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
EMAIL = sys.argv[5] if len(sys.argv) > 5 else 'operationalcoherence@gmail.com'
SRC = open(JS, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0"><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
APP = b'export function initializeApp(c,n){return {c,n}}'
AUTH = b'''let cur=null,subs=[];const fire=()=>subs.forEach(f=>f(cur));
export function getAuth(){return {get currentUser(){return cur},authStateReady:()=>Promise.resolve()}}
export function onAuthStateChanged(a,f){subs.push(f);setTimeout(()=>f(cur),0)}
export class GoogleAuthProvider{setCustomParameters(){}}
export function signInWithPopup(){cur={uid:'lead1',isAnonymous:false,displayName:'Test Lead',email:'__EMAIL__'};fire();return Promise.resolve({user:cur})}
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
export function collectionGroup(db,id){return {kind:'grp',id}}\nexport function increment(n){return {__inc:n}}\nexport function getDocs(q){const pre=q.path+'/';const docs=Object.keys(D).filter(k=>k.startsWith(pre)&&!k.slice(pre.length).includes('/')).filter(k=>!q.w||D[k][q.w.f]===q.w.v).map(k=>({id:k.slice(pre.length),ref:{kind:'doc',path:k},data:()=>D[k]}));return Promise.resolve({docs})}'''

AUTH = AUTH.replace(b'__EMAIL__', EMAIL.encode())
FS = FS.replace(b"export function getDocs(q){", b"export function getDocs(q){if(q.kind==='grp'){const docs=Object.keys(D).filter(k=>{const s=k.split('/');return s.length>=2&&s[s.length-2]===q.id}).map(k=>{const s=k.split('/');return {id:s[s.length-1],ref:{path:k,parent:{id:s[s.length-2],parent:{id:s[s.length-3]}}},data:()=>D[k]}});return Promise.resolve({docs})}")
wb = json.load(open(WB))['data']
import os; T = os.path.dirname(os.path.abspath(WB)) + '/'
def wbj(f): return json.dumps(json.load(open(T+f))['data'])
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
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/#bcmadmin'); pg.wait_for_selector('#gsm-admin', timeout=25000); pg.wait_for_timeout(800)
    print('--- before sign-in\n' + pg.inner_text('#gsm-admin'))
    now = int(__import__('time').time())
    pg.evaluate("window.gsmF8.fs()"); pg.wait_for_timeout(300)
    pg.evaluate("""(a)=>{const [now,j1,j2,j3]=a;
      __fsdb['projects/P1']={lead:'L1',leadName:'Gregory',name:'Broad Street',created:{seconds:now-86400*3},updated:{seconds:now-3600},exports:2};
      __fsdb['projects/P2']={lead:'L2',leadName:'Sam <b>x</b>',name:'Old project',created:{seconds:now-86400*30},updated:{seconds:now-86400*20}};
      __fsdb['projects/P1/keys/kkkkkkkkkkkkkkkkkkkkkkkk']={open:true};
      __fsdb['projects/P1/workbooks/u1']={uid:'u1',name:'Ana',voice:'Residents',data:{json:j1},saved:{seconds:now-60}};
      __fsdb['projects/P1/workbooks/u2']={uid:'u2',name:'Ben',voice:'Fire',data:{json:j2},saved:{seconds:now-7200}};
      __fsdb['projects/P2/workbooks/u3']={uid:'u3',name:'Cy',voice:'',data:{json:j3},saved:{seconds:now-86400*21}};
      __fsdb['projects/P2/workbooks/u4']={uid:'u4',name:'Dee',voice:'',data:{json:'{bad'},saved:{seconds:now-86400*21}};}""", [now, wbj('wb_clinic.json'), wbj('wb_big.json'), wbj('wb_empty.json')])
    pg.click('[data-a=in]'); pg.wait_for_timeout(800)
    print('--- after sign-in as', EMAIL, '\n' + pg.inner_text('#gsm-admin'))
    print('shows names of people answering:', any(n in pg.inner_text('#gsm-admin') for n in ['Ana', 'Ben', 'Dee']), '| html escaped:', '<b>x</b>' not in pg.inner_html('#gsm-admin'))
    print('reads:', pg.evaluate('__fslog'))
    pg.locator('#gsm-admin').screenshot(path=OUT + '_admin.png')
    print('ERRORS', errs)
    b.close()
