"""v210: the short tour on Pattern Analysis (how to read this map). With the 3D loaded, presses Play the tour on
the Analysis map, prints each caption, screenshots one stop, and checks that End tour closes full screen.
Usage: python3 -I tour_an.py WORKBOOK.json [OUTPREFIX]"""
import json, sys, time
from playwright.sync_api import sync_playwright
SRC = open('../gsm-preview.js', 'rb').read(); REL = open('../gsm-relief.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(sys.argv[1]))['data']; OUT = sys.argv[2] if len(sys.argv) > 2 else '/tmp/touran'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    pg = b.new_page(viewport={'width': 1200, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},live:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=25000)
    pg.evaluate("window.gsmTab(2)"); pg.wait_for_timeout(1500)
    btn = None
    for _ in range(40):
        bs = [x for x in pg.query_selector_all('.grel .tpb') if x.is_visible()]
        if bs: btn = bs[0]; break
        pg.mouse.wheel(0, 500); pg.wait_for_timeout(450)
    if not btn: print('NO PLAY BUTTON ON ANALYSIS', errs); sys.exit()
    stage = pg.evaluate_handle("e=>e.closest('.grel')", btn)
    btn.click(); t0 = time.time(); caps = []; shot = False
    while time.time() - t0 < 90:
        c = pg.evaluate("e=>{var c=e.querySelector('.tourcap');return c&&c.style.display!=='none'?c.innerText.replace(/\\n+/g,' | '):''}", stage)
        if c and (not caps or caps[-1] != c): caps.append(c)
        if not shot and len(caps) >= 4: pg.wait_for_timeout(1600); pg.screenshot(path=OUT + '.png'); shot = True
        if pg.evaluate("e=>e.querySelector('.tpb').textContent==='Play the tour'", stage) and time.time() - t0 > 2: break
        pg.wait_for_timeout(200)
    print('tour ended after %.1fs, full screen closed: %s' % (time.time() - t0, not pg.evaluate("e=>e.classList.contains('fs')", stage)))
    for c in caps: print(' -', c)
    btn.click(); pg.wait_for_timeout(1500); pg.evaluate("e=>e.querySelector('.tpe').click()", stage); pg.wait_for_timeout(400)
    print('End tour ends and closes full screen:', pg.evaluate("e=>e.querySelector('.tpb').textContent==='Play the tour'&&!e.classList.contains('fs')", stage))
    print('errors:', errs); b.close()
