"""3D ground screenshot, same camera every time: Pattern Synthesis (tab 3) relief, full screen at 1600x1000.
Usage: python3 -I reliefshot.py PREVIEW.js RELIEF.js WORKBOOK.json OUT.png [tab]"""
import json, sys
from playwright.sync_api import sync_playwright
JS, RJ, WB, OUT = sys.argv[1:5]; TAB = int(sys.argv[5]) if len(sys.argv) > 5 else 3
SRC = open(JS, 'rb').read(); REL = open(RJ, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(WB))['data']
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    import os; pg = b.new_page(viewport={'width': 1600, 'height': 1000}, device_scale_factor=float(os.environ.get('DSF','1'))); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("var __r;Object.defineProperty(window,'gsmRelief',{configurable:true,get:function(){return __r},set:function(v){var m=v.mount;v.mount=function(a,b){var t=performance.now();var o=m(a,b);(window.__mt=window.__mt||[]).push(Math.round(performance.now()-t));return o};__r=v}})")
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=25000)
    pg.evaluate("window.gsmTab(%d)" % TAB); pg.wait_for_timeout(1500)
    for _ in range(40):
        if pg.query_selector('.grel canvas'): break
        pg.mouse.wheel(0, 600); pg.wait_for_timeout(400)
    el = pg.query_selector('.grel')
    if not el: print('NO 3D', errs); sys.exit(1)
    el.scroll_into_view_if_needed(); pg.wait_for_timeout(1500)
    fs = [x for x in pg.query_selector_all('.grel .bt') if x.inner_text() == 'Full screen' and x.is_visible()]
    if fs: fs[0].click(); pg.wait_for_timeout(800)
    hl = [x for x in pg.query_selector_all('.grel.fs .fslb') if x.is_visible()]
    if hl: hl[0].click(); pg.wait_for_timeout(800)
    pg.wait_for_timeout(4000)
    t = pg.query_selector('.grel.fs') or el
    t.screenshot(path=OUT); print('ok', OUT, 'mount ms', pg.evaluate('window.__mt'), errs[:3])
    b.close()
