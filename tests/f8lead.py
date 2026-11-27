"""F8 step 3, Lead a project (v309, v310), against fake Firebase modules (no network).
python3 -I f8lead.py JS WORKBOOK.json WIDTH OUTPREFIX
Signs in as a fake Google lead, creates a project, edits it, shows the QR code, deletes it,
and prints every write the page made, in order, so the delete order can be checked."""
import json, sys
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
export function deleteDoc(r){L.push('delete '+r.path);delete D[r.path];return Promise.resolve()}
export function getDocs(q){const pre=q.path+'/';const docs=Object.keys(D).filter(k=>k.startsWith(pre)&&!k.slice(pre.length).includes('/')).filter(k=>!q.w||D[k][q.w.f]===q.w.v).map(k=>({id:k.slice(pre.length),ref:{kind:'doc',path:k},data:()=>D[k]}));return Promise.resolve({docs})}'''
wb = json.load(open(WB))['data']
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': W, 'height': 900}, is_mobile=W < 600, has_touch=W < 600)
    pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    pg.on('console', lambda m: m.type == 'error' and 'Failed to load resource' not in m.text and errs.append('console: ' + m.text[:150]))
    def route(r):
        u = r.request.url
        if u.startswith('http://t.local/?') or u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.endswith('/firebase-app.js'): r.fulfill(status=200, content_type='application/javascript', body=APP, headers={'access-control-allow-origin': '*'})
        elif u.endswith('/firebase-auth.js'): r.fulfill(status=200, content_type='application/javascript', body=AUTH, headers={'access-control-allow-origin': '*'})
        elif u.endswith('/firebase-firestore.js'): r.fulfill(status=200, content_type='application/javascript', body=FS, headers={'access-control-allow-origin': '*'})
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},live:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/?f8test=1'); pg.wait_for_selector('#gsm-wlead', timeout=25000)
    T = lambda: pg.inner_text('#gsm-lead')
    pg.click('#gsm-wlead'); pg.wait_for_timeout(600); print('--- sign-in view\n' + T())
    pg.click('[data-l=signin]'); pg.wait_for_timeout(600); print('--- list view\n' + T())
    pg.click('[data-l=new]'); pg.wait_for_timeout(300)
    pg.click('[data-l=save]'); pg.wait_for_timeout(200); print('--- empty name:', pg.inner_text('#gsm-lead .lmsg'))
    pg.fill('#gsm-lpn', 'Test project')
    for v in ('Residents', 'Fire crews', 'residents'):
        pg.fill('#gsm-lpv', v); pg.press('#gsm-lpv', 'Enter'); pg.wait_for_timeout(100)
    pg.fill('#gsm-lpd', '2026-12-15')
    pg.screenshot(path=OUT + '_form.png', full_page=False)
    pg.click('[data-l=save]'); pg.wait_for_timeout(600); print('--- after create\n' + T())
    pg.click('[data-l=qr]'); pg.wait_for_timeout(200)
    print('qr svg:', pg.evaluate("()=>{const s=document.querySelector('#gsm-lqr svg');return s?s.getAttribute('viewBox')+' rects/paths:'+s.innerHTML.length:'none'}"))
    pg.locator('#gsm-lead .inv').screenshot(path=OUT + '_invite.png')
    pg.fill('#gsm-lpg', 'An edited shared goal.'); pg.click('[data-l=save]'); pg.wait_for_timeout(500)
    # a person's workbook in the project, to check the delete order
    pg.evaluate("()=>{const k=Object.keys(__fsdb).find(k=>k.includes('/keys/'));const pid=k.split('/')[1];__fsdb['projects/'+pid+'/workbooks/p1']={uid:'p1'}}")
    print('db before delete:', json.dumps(pg.evaluate('()=>__fsdb'), indent=1)[:1500])
    pg.click('[data-l=back]'); pg.wait_for_timeout(500); print('--- list again\n' + T())
    pg.click('[data-l=open]'); pg.wait_for_timeout(300)
    pg.click('[data-l=del]'); pg.wait_for_timeout(200); print('--- delete ask:', pg.inner_text('#gsm-lead .warn'))
    pg.click('[data-l=delyes]'); pg.wait_for_timeout(800); print('--- after delete\n' + T())
    print('writes:', pg.evaluate('()=>__fslog'))
    print('db left:', pg.evaluate('()=>Object.keys(__fsdb)'))
    # v310: the place-map link on the form opens Mapping Landscape at the place search
    pg.click('[data-l=new]'); pg.wait_for_timeout(300)
    print('map help:', pg.inner_text('#gsm-lead .lf:has([name=gsm-lpm]) .lh'))
    pg.click('[data-l=findplace]'); pg.wait_for_timeout(700)
    print('after findplace: focus =', pg.evaluate('()=>document.activeElement&&document.activeElement.id'), '| search visible =', pg.is_visible('#gsm-q'))
    print('ERRORS', errs)
    b.close()
