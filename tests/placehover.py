"""Hover every place-map marker and print the tooltip heading.

    npm install leaflet@1.9.4
    python3 placehover.py ../gsm-preview.js bear-canyon-workbook-2026-11-05.json [NAME]

NAME, if given, is written into the workbook's `who` field, which is what the
heading falls back to for a note with no author. Leaflet is served from a local
copy because the page loads it from a CDN and the harness blocks outside
requests. Map tiles stay blocked; markers do not need them.
"""
import json, sys
from playwright.sync_api import sync_playwright
JS, WB = sys.argv[1], sys.argv[2]
NAME = sys.argv[3] if len(sys.argv)>3 else None
SRC=open(JS,'rb').read()
import os
def _leaf(f):
    here=os.path.dirname(os.path.abspath(__file__))
    for d in (os.path.join(here,'node_modules','leaflet','dist'),
              os.path.join(here,'..','node_modules','leaflet','dist'),
              os.path.join(os.getcwd(),'node_modules','leaflet','dist')):
        q=os.path.join(d,f)
        if os.path.exists(q): return open(q,'rb').read()
    raise SystemExit("Leaflet not found. Run:  npm install leaflet@1.9.4\n"
                     "(the page loads Leaflet from a CDN, which the harness blocks, so it is served locally)")
LJS=_leaf('leaflet.js')
LCSS=_leaf('leaflet.css')
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb=json.load(open(WB))['data']
if NAME is not None: wb['who']=NAME
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1400,'height':1000}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    def route(r):
        u=r.request.url
        if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
        elif 'leaflet' in u and u.endswith('.js'): r.fulfill(status=200,content_type='application/javascript',body=LJS)
        elif 'leaflet' in u and u.endswith('.css'): r.fulfill(status=200,content_type='text/css',body=LCSS)
        else: r.abort()
    pg.route('**/*',route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');"%json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm',timeout=20000); pg.wait_for_timeout(1500)
    pg.evaluate("window.gsmTab(1)"); pg.wait_for_timeout(2500)
    print('leaflet loaded:', pg.evaluate("typeof window.L!=='undefined'"))
    print('map container:', pg.evaluate("!!document.querySelector('#gsm .leaflet-container')"))
    print('pz class:', pg.evaluate("(()=>{var e=document.getElementById('gsm-pz');return e?e.className+' | rect='+JSON.stringify(e.getBoundingClientRect()):'(no #gsm-pz)'})()"))
    print('first marker rect:', pg.evaluate("(()=>{var m=document.querySelector('#gsm .leaflet-marker-icon');return m?JSON.stringify(m.getBoundingClientRect()):'none'})()"))
    pg.evaluate(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'placehover_probe.js')).read())
    mk=pg.locator('#gsm .leaflet-marker-icon')
    n=mk.count(); print('markers:', n)
    for i in range(min(n,5)):
        el=mk.nth(i); bb=el.bounding_box()
        if not bb: continue
        try: el.hover(force=True, timeout=4000)
        except Exception as ex: print('  hover failed', type(ex).__name__)
        pg.wait_for_timeout(200)
        if pg.evaluate("(()=>{var t=document.querySelector('.gsm-tt');return !(t&&t.style.display!=='none')})()"):
            el.evaluate("n=>n.dispatchEvent(new MouseEvent('mouseover',{bubbles:true,clientX:50,clientY:50}))")
            pg.wait_for_timeout(200)
        print(' marker',i, pg.evaluate("(()=>{var t=document.querySelector('.gsm-tt');return t&&t.style.display!=='none'?JSON.stringify(t.innerText.split('\\n')[0]):'(none)'})()"))
    print('tooltip mutations:', pg.evaluate("window.__zlog ? window.__zlog.slice(0,12) : 'none'"))
    print('ERRORS',errs); b.close()
