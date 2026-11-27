"""v326 sample project in the lead dashboard. python3 -I samplepj.py JS ignored WIDTH OUTPREFIX"""
import json, sys, os
from playwright.sync_api import sync_playwright
JS, WB, W, OUT = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
SRC = open(JS, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0"><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
APP = b'export function initializeApp(c,n){return {c,n}}'
AUTH = b'''let cur=JSON.parse(sessionStorage.getItem('au')||'null'),subs=[];const fire=()=>subs.forEach(f=>f(cur));
export function getAuth(){return {get currentUser(){return cur},authStateReady:()=>Promise.resolve()}}
export function onAuthStateChanged(a,f){subs.push(f);setTimeout(()=>f(cur),0)}
export class GoogleAuthProvider{setCustomParameters(){}}
export function signInWithPopup(){cur={uid:'lead1',isAnonymous:false,displayName:'Test Lead',email:'lead@example.com'};sessionStorage.setItem('au',JSON.stringify(cur));fire();return Promise.resolve({user:cur})}
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


SAMPLE = open(os.path.join(os.path.dirname(os.path.abspath(JS)), 'tests', 'sample_project_fuel_break.json'), 'rb').read()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    pg = b.new_page(viewport={'width': W, 'height': 1000}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    def route(r):
        u = r.request.url
        if u.startswith('http://t.local/?') or u.split('#')[0] == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=open(os.path.join(os.path.dirname(os.path.abspath(JS)),'gsm-relief.js'),'rb').read())
        elif u.startswith('http://t.local/tests/sample_project_fuel_break.json'): r.fulfill(status=200, content_type='application/json', body=SAMPLE)
        elif u.endswith('/firebase-app.js'): r.fulfill(status=200, content_type='application/javascript', body=APP, headers={'access-control-allow-origin': '*'})
        elif u.endswith('/firebase-auth.js'): r.fulfill(status=200, content_type='application/javascript', body=AUTH, headers={'access-control-allow-origin': '*'})
        elif u.endswith('/firebase-firestore.js'): r.fulfill(status=200, content_type='application/javascript', body=FS, headers={'access-control-allow-origin': '*'})
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("if(!sessionStorage.getItem('i')){sessionStorage.setItem('i','1');localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));}")
    pg.goto('http://t.local/?f8test=1'); pg.wait_for_selector('#gsm-wlead', timeout=25000)
    pg.click('#gsm-wlead'); pg.wait_for_timeout(500); pg.click('[data-l=signin]'); pg.wait_for_timeout(1500)
    print(pg.inner_text('#gsm-ldash')[:300] if pg.query_selector('#gsm-ldash') else 'no ldash')
    pg.click('[data-l=open]'); pg.wait_for_timeout(2500)
    nav = lambda: pg.evaluate("(()=>{var n=document.getElementById('gsm-lnav');return n?[...n.querySelectorAll('button,select')].map(b=>(b.classList.contains('on')?'*':'')+(b.tagName=='SELECT'?'[select '+b.options.length+']':b.textContent)).join(' | '):'NO NAV'})()")
    print('1 dash:', nav())
    pg.screenshot(path=OUT + '_1.png')
    pg.click('#gsm-lnav [data-n=people]'); pg.wait_for_timeout(800); print('2 people:', nav(), '| cards', len(pg.query_selector_all('.ecard')))
    pg.select_option('#gsm-lnav select', 'sample05'); pg.wait_for_timeout(800); print('3 person:', nav(), '| eper', bool(pg.query_selector('.eper')))
    pg.screenshot(path=OUT + '_3.png')
    pg.click('#gsm-lnav [data-n=clusters]'); pg.wait_for_timeout(12000)
    print('dbg', pg.evaluate("[window.gsmRead&&window.gsmRead.pid, (localStorage.getItem('groundsmith-web-leadnav')||'none').slice(0,80), localStorage.getItem('groundsmith-web-leadgo-read'), window.scrollY]"))
    print('4 reading:', pg.evaluate('location.hash'), nav(), '| panel', bool(pg.query_selector('.gtcl')))
    pg.screenshot(path=OUT + '_4.png')
    pg.select_option('#gsm-lnav select', 'sample12'); pg.wait_for_timeout(8000)
    print('5 back to person:', pg.evaluate('location.hash'), nav(), '| eper', pg.inner_text('.eper')[:60] if pg.query_selector('.eper') else None)
    pg.screenshot(path=OUT + '_5.png'); print('lead box:', pg.evaluate("(document.getElementById('gsm-lead')||{}).innerText||'none'")[:300], pg.evaluate("localStorage.getItem('groundsmith-web-leadgo')"), pg.evaluate('location.href'))
    print('errors', errs[:5]); b.close()
