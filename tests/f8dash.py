"""F8 step 5, EVERY WORKBOOK (v312), against fake Firebase modules (no network).
python3 -I f8dash.py JS WORKBOOK.json WIDTH OUTPREFIX
(based on f8lead.py) F8 step 3, Lead a project (v309, v310), against fake Firebase modules (no network).
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
export function getDoc(r){return Promise.resolve({exists:()=>!!D[r.path],data:()=>D[r.path]})}
export function deleteDoc(r){L.push('delete '+r.path);delete D[r.path];return Promise.resolve()}
export function getDocs(q){const pre=q.path+'/';const docs=Object.keys(D).filter(k=>k.startsWith(pre)&&!k.slice(pre.length).includes('/')).filter(k=>!q.w||D[k][q.w.f]===q.w.v).map(k=>({id:k.slice(pre.length),ref:{kind:'doc',path:k},data:()=>D[k]}));return Promise.resolve({docs})}'''
wb = json.load(open(WB))['data']
import os; T = os.path.dirname(os.path.abspath(WB)) + '/'
def wbj(f): return json.dumps(json.load(open(T+f))['data'])
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': W, 'height': 900}, is_mobile=W < 600, has_touch=W < 600, accept_downloads=True)
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
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/?f8test=1'); pg.wait_for_selector('#gsm-wlead', timeout=25000)
    D = lambda: pg.inner_text('#gsm-ldash')
    pg.click('#gsm-wlead'); pg.wait_for_timeout(500)
    pg.click('[data-l=signin]'); pg.wait_for_timeout(500)
    pg.click('[data-l=new]'); pg.wait_for_timeout(300)
    pg.fill('#gsm-lpn', 'Broad Street test'); pg.fill('#gsm-lpd', '2026-12-15')
    pg.click('[data-l=save]'); pg.wait_for_timeout(700)
    print('--- new project, empty table\n' + D())
    now = int(__import__('time').time())
    seed = {'p1': ('Ana', 'Residents', wbj('wb_clinic.json'), now - 60),
            'p2': ('Ben', 'Fire crews', wbj('wb_big.json'), now - 7200),
            'p3': ('Cy', 'Other: school board', wbj('wb_empty.json'), now - 3 * 86400),
            'p4': ('', '', '{not json', now - 30),
            'p5': ('Dee', 'Residents', wbj('wb_places_names.json'), now - 600)}
    pg.evaluate("""(seed)=>{const k=Object.keys(__fsdb).find(k=>k.includes('/keys/'));const pid=k.split('/')[1];
      for(const u in seed){const [n,v,j,t]=seed[u];__fsdb['projects/'+pid+'/workbooks/'+u]={uid:u,key:'x',name:n,voice:v,data:{fmt:'bcm-workbook',sv:2,json:j},saved:{seconds:t}}}}""", seed)
    pg.click('[data-l=dref]'); pg.wait_for_timeout(500)
    print('--- after seeding 5 workbooks\n' + D())
    pg.locator('#gsm-ldash').screenshot(path=OUT + '_table.png')
    href = pg.get_attribute('#gsm-ldash tbody tr:first-child a.lnk', 'href')
    import urllib.parse as up; print('remind (first row):', up.unquote(href)[:400])
    # open Ana
    pg.click('[data-l=dopen][data-u=p1]'); pg.wait_for_timeout(200)
    print('--- Ana opened\n' + pg.inner_text('#gsm-ldash .ewv')[:900])
    pg.locator('#gsm-ldash').screenshot(path=OUT + '_open.png')
    with pg.expect_download() as dl: pg.click('[data-l=dfile]')
    f = dl.value; path = f.path(); j = json.load(open(path))
    print('file:', f.suggested_filename, '| app', j['app'], '| who', j['data'].get('who'), '| answers', sum(1 for a in j['data']['a'] if a.strip()), '| notes', len(j['data']['m']))
    pg.click('[data-l=dopen][data-u=p4]'); pg.wait_for_timeout(200); print('broken open:', pg.inner_text('#gsm-ldash .ewv'))
    # delete Cy
    pg.click('[data-l=ddel][data-u=p3]'); pg.wait_for_timeout(200); print('delete ask:', pg.inner_text('#gsm-ldash .warn'))
    pg.click('[data-l=ddelyes]'); pg.wait_for_timeout(400); print('--- after delete\n' + D()[:300])
    # stop / start taking answers
    pg.click('[data-l=dtake]'); pg.wait_for_timeout(300)
    k = pg.evaluate("()=>{const k=Object.keys(__fsdb).find(k=>k.includes('/keys/'));return __fsdb[k].open}")
    print('after stop: key open =', k, '|', D()[D().find('Not taking'):][:120] if 'Not taking' in D() else 'MISSING')
    pg.click('[data-l=dtake]'); pg.wait_for_timeout(300)
    print('after start: key open =', pg.evaluate("()=>{const k=Object.keys(__fsdb).find(k=>k.includes('/keys/'));return __fsdb[k].open}"))
    # the form below still works, and typing is not lost on a table refresh
    pg.fill('#gsm-lpn', 'Broad Street test 2'); pg.click('[data-l=dref]'); pg.wait_for_timeout(400)
    print('name kept after refresh:', pg.input_value('#gsm-lpn'))
    # back to list, reopen: table loads again
    pg.click('[data-l=back]'); pg.wait_for_timeout(400); pg.click('[data-l=open]'); pg.wait_for_timeout(500)
    print('reopen rows:', pg.locator('#gsm-ldash tbody tr').count())
    pg.screenshot(path=OUT + '_page.png', full_page=False)
    print('reads/writes:', pg.evaluate('()=>__fslog'))
    print('ERRORS', errs)
    b.close()
