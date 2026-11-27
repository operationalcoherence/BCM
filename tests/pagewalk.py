"""Walk Start Here, every Mapping Context step, and both Mapping Landscape
steps (v290). Prints each step's visible text with folds open and saves a
full-page screenshot per step.

    python3 pagewalk.py ../gsm-preview.js WORKBOOK.json OUTDIR [width]
"""
import json, os, sys
from playwright.sync_api import sync_playwright
JS, WB, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
W = int(sys.argv[4]) if len(sys.argv) > 4 else 420
os.makedirs(OUT, exist_ok=True)
SRC = open(JS, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(WB))['data']
OPEN = "document.querySelectorAll('#gsm details').forEach(d=>d.open=true)"
TXT = "()=>document.querySelector('#gsm').innerText"
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': W, 'height': 900})
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},live:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=20000); pg.wait_for_timeout(800)
    steps = [('start', "window.gsmTab(5)")]
    steps += [('ctx%d' % i, "window.gsmTab(0);window.gsmCStep(%d)" % i) for i in range(8)]
    steps += [('land1', "window.gsmTab(1);window.gsmMStep(1)"), ('land2', "window.gsmTab(1);window.gsmMStep(2)")]
    for name, js in steps:
        pg.evaluate(js); pg.wait_for_timeout(400); pg.evaluate(OPEN); pg.wait_for_timeout(150)
        print('########', name)
        print(pg.evaluate(TXT))
        pg.screenshot(path=os.path.join(OUT, name + '.png'), full_page=True)
    print('######## ERRORS', errs)
    b.close()
