"""v208: the guided tour on Pattern Synthesis. With the 3D loaded, presses Play the tour, records each caption
as it changes, screenshots three moments, then checks that a click stops it and the view returns.
Usage: python3 -I tour.py WORKBOOK.json [OUTPREFIX] [slow]  (slow: the tour runs 8x slower, for settled screenshots)"""
import json, sys, time
from playwright.sync_api import sync_playwright
SRC = open('../gsm-preview.js', 'rb').read(); REL = open('../gsm-relief.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(sys.argv[1]))['data']; OUT = sys.argv[2] if len(sys.argv) > 2 else '/tmp/tour'
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
    SLOW = len(sys.argv) > 3
    SLOW and pg.add_init_script("window.gsmTourSlow=8")
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=25000)
    pg.evaluate("window.gsmTab(3)"); pg.wait_for_timeout(1500)
    btn = None
    for _ in range(30):
        bs = [x for x in pg.query_selector_all('.grel .bt') if x.inner_text() == 'Play the tour' and x.is_visible()]
        if bs: btn = bs[0]; break
        pg.mouse.wheel(0, 500); pg.wait_for_timeout(500)
    if not btn: print('NO PLAY BUTTON', errs); sys.exit()
    btn.scroll_into_view_if_needed(); pg.wait_for_timeout(800)
    stage = pg.evaluate_handle("()=>[...document.querySelectorAll('.grel .bt')].find(x=>x.textContent==='Play the tour').closest('.grel')")
    btn.click(); t0 = time.time(); caps = []; shots = 0
    while time.time() - t0 < (260 if SLOW else 40):
        c = pg.evaluate("e=>{var c=e.querySelector('.tourcap');return c&&c.style.display!=='none'?c.innerText.replace(/\\n+/g,' | '):''}", stage)
        if c and (not caps or caps[-1][1] != c): caps.append((round(time.time() - t0, 1), c))
        if shots < 3 and time.time() - t0 > ([12, 60, 130] if SLOW else [1.6, 9, 20])[shots]:
            stage.as_element().screenshot(path='%s%d.png' % (OUT, shots)); shots += 1
        if pg.evaluate("e=>[...e.querySelectorAll('.bt')].some(x=>x.textContent==='Play the tour')", stage) and time.time() - t0 > 2: break
        pg.wait_for_timeout(150)
    print('tour ended after %.1fs' % (time.time() - t0))
    for t, c in caps: print(t, c[:260])
    btn.click(); pg.wait_for_timeout(1500)
    stage.as_element().query_selector('canvas').click(); pg.wait_for_timeout(400)
    print('click stops it:', pg.evaluate("e=>[...e.querySelectorAll('.bt')].some(x=>x.textContent==='Play the tour')", stage))
    print('errors:', errs)
    b.close()
