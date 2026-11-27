"""F8 project clusters (v323): the lead's combined copy, Pattern Analysis, the note map in clusters.
python3 -I clustershot.py PREVIEW.js RELIEF.js COMBINED.json OUTPREFIX [width] [solo]
Opens the combined copy the way the dashboard does (#bcmread=), or with 'solo' as a plain workbook (no clusters)."""
import json, sys, os
from playwright.sync_api import sync_playwright
JS, RJ, WB, OUT = sys.argv[1:5]; W = int(sys.argv[5]) if len(sys.argv) > 5 else 1400; SOLO = len(sys.argv) > 6
SRC = open(JS, 'rb').read(); REL = open(RJ, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.dumps(json.load(open(WB))['data'])
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    pg = b.new_page(viewport={'width': W, 'height': 1000}, device_scale_factor=float(os.environ.get('DSF','1'))); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    pg.on('console', lambda m: m.type in ('error', 'warning') and 'Failed to load' not in m.text and errs.append('console: ' + m.text[:160]))
    def route(r):
        u = r.request.url
        if u.split('#')[0] == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
        else: r.abort()
    pg.route('**/*', route)
    priv = "localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));"
    if SOLO: pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);" % json.dumps(wb) + priv)
    else: pg.add_init_script("if(!sessionStorage.getItem('t')){sessionStorage.setItem('t','1');localStorage.setItem('groundsmith-web-f8read',%s);localStorage.setItem('groundsmith-web-f8readmeta',JSON.stringify({name:'Upper canyon fuel break',n:20,at:Date.now()}));}" % json.dumps(wb) + priv)
    pg.goto('http://t.local/' if SOLO else 'http://t.local/#bcmread=test'); pg.wait_for_selector('#gsm', timeout=25000); pg.wait_for_timeout(800)
    print('read mode', pg.evaluate('!!window.gsmRead'), 'ver', pg.evaluate("(document.getElementById('gsm-ver')||{}).textContent"))
    tab = pg.evaluate("[...document.querySelectorAll('#gsm-jsub button,#gsm-jump button')].map(b=>b.textContent)")
    print('tabs', tab)
    for t in range(2, 6):
        pg.evaluate("window.gsmTab(%d)" % t); pg.wait_for_timeout(600)
        if pg.query_selector('.gterr-host[data-an]:not([data-bare])'): break
    h = pg.query_selector('.gterr-host[data-an]:not([data-bare])')
    if not h: print('NO NOTE MAP', errs); sys.exit(1)
    h.scroll_into_view_if_needed()
    for _ in range(40):
        if h.query_selector('.grel canvas'): break
        pg.wait_for_timeout(400)
    pg.wait_for_timeout(5000)
    h.screenshot(path=OUT + '_map.png')
    P = pg.query_selector('.gtcl')
    print('panel', bool(P), 'tags', len(h.query_selector_all('.clt')), 'note labels', len(h.query_selector_all('.lb.nl')))
    if P:
        P.screenshot(path=OUT + '_panel.png')
        bs = P.query_selector_all('.cli')
        if len(bs) > 1:
            pg.evaluate("document.querySelectorAll('.gtcl .cli')[1].click()"); pg.wait_for_timeout(1500); None; h.screenshot(path=OUT + '_sel.png'); P.screenshot(path=OUT + '_panelsel.png')
    pg.evaluate("document.querySelectorAll('.gtcl .cli.on').forEach(b=>b.click())"); pg.wait_for_timeout(500)
    fs = [x for x in h.query_selector_all('.grel .bt') if x.inner_text() == 'Full screen' and x.is_visible()]
    if fs:
        fs[0].click(); pg.wait_for_timeout(800)
        hl = [x for x in pg.query_selector_all('.grel.fs .fslb') if x.is_visible()]
        if hl: hl[0].click(); pg.wait_for_timeout(800)
        pg.wait_for_timeout(3000); pg.screenshot(path=OUT + '_fs.png')
    print('errors', [e for e in errs if 'GL Driver' not in e and 'PCFSoft' not in e][:6])
    b.close()
