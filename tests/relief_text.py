"""Load workbooks with the 3D relief served, visit Pattern Analysis and Taking Action, scroll every card into view,
and report page errors plus whether given strings appear anywhere in the page (open or folded).
Usage: python3 -I relief_text.py "string1|string2" wb1.json wb2.json"""
import json, sys
from playwright.sync_api import sync_playwright

SRC = open(__import__('os').environ.get('GSMJS', '../gsm-preview.js'), 'rb').read()
REL = open('../gsm-relief.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
WANT = sys.argv[1].split('|')
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',
                          args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    for f in sys.argv[2:]:
        wb = json.load(open(f))['data']
        pg = b.new_page(viewport={'width': 1400, 'height': 900}); errs = []
        pg.on('pageerror', lambda e: errs.append('PAGEERROR: ' + str(e).split('\n')[0]))
        pg.on('console', lambda m: (errs.append('CONSOLE: ' + m.text) if m.type == 'error' and 'ERR_FAILED' not in m.text else None))
        def route(r):
            u = r.request.url
            if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
            elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
            elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
            else: r.abort()
        pg.route('**/*', route)
        pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');" % json.dumps(json.dumps(wb)))
        pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=25000)
        seen = set()
        for tab in (2, 3, 4):
            pg.evaluate("window.gsmTab&&window.gsmTab(%d)" % tab); pg.wait_for_timeout(1500)
            h = pg.evaluate("()=>document.body.scrollHeight")
            for y in range(0, h + 900, 600):
                pg.evaluate("y=>window.scrollTo(0,y)", y); pg.wait_for_timeout(250)
            pg.wait_for_timeout(1500)
            html = pg.evaluate("()=>document.body.innerHTML")
            for w in WANT:
                if w in html: seen.add(w)
        canv = pg.evaluate("()=>document.querySelectorAll('canvas').length")
        print(f, 'canvases=%d' % canv, 'found:', sorted(seen), 'missing:', [w for w in WANT if w not in seen])
        for e in dict.fromkeys(errs): print('   !!', e[:170])
        pg.close()
    b.close()
