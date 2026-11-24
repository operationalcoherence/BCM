"""Taking Action card map, full screen, same camera: screenshot the card with the most numbered stops (or CARD=n).
Usage: python3 -I cardshot.py PREVIEW.js RELIEF.js WORKBOOK.json OUT.png"""
import json, sys, os
from playwright.sync_api import sync_playwright
JS, RJ, WB, OUT = sys.argv[1:5]
SRC = open(JS, 'rb').read(); REL = open(RJ, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(WB))['data']
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    pg = b.new_page(viewport={'width': 1600, 'height': 1000}, device_scale_factor=float(os.environ.get('DSF', '1'))); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm'); pg.wait_for_timeout(1500)
    pg.evaluate("window.gsmTab(4)"); pg.wait_for_timeout(1500)
    n = pg.evaluate("document.querySelectorAll('#gsm .coa').length"); best = (-1, -1)
    if os.environ.get('CARD'): best = (int(os.environ['CARD']), 0)
    else:
        for i in range(n):
            pg.evaluate("i=>{var c=document.querySelectorAll('#gsm .coa')[i];c.querySelectorAll('details').forEach(d=>d.open=true);c.scrollIntoView()}", i); pg.wait_for_timeout(1300)
            k = pg.evaluate("i=>document.querySelectorAll('#gsm .coa')[i].querySelectorAll('.grel .wn').length", i)
            if k > best[1]: best = (i, k)
    CI = best[0]; print('cards', n, 'card', best)
    if CI < 0: sys.exit(1)
    pg.evaluate("i=>{var c=document.querySelectorAll('#gsm .coa')[i];c.querySelectorAll('details').forEach(d=>d.open=true);c.scrollIntoView()}", CI); pg.wait_for_timeout(1500)
    c = pg.query_selector_all('#gsm .coa')[CI]
    fs = [x for x in c.query_selector_all('button') if x.is_visible() and (x.inner_text() or '') == 'Full screen']
    if fs: fs[0].click(); pg.wait_for_timeout(5000)
    pg.screenshot(path=OUT); print('ok', OUT, errs[:3])
    b.close()
