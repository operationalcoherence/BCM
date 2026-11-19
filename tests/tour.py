"""v208/v210: the guided tour on Pattern Synthesis. With the 3D loaded, presses Play the tour, records each caption
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
    pg.evaluate("e=>{window.__caps=[];var c=e.querySelector('.tourcap');new MutationObserver(function(){var t=c.querySelector('.tt');t&&window.__caps[window.__caps.length-1]!==t.textContent&&window.__caps.push(t.textContent)}).observe(c,{childList:true,subtree:true})}", stage)
    btn.click(); t0 = time.time(); caps = []; shots = 0
    fs_on = None
    while time.time() - t0 < (600 if SLOW else 150):
        if fs_on is None and time.time() - t0 > 1: fs_on = pg.evaluate("e=>e.classList.contains('fs')", stage)
        c = pg.evaluate("e=>{var c=e.querySelector('.tourcap');return c&&c.style.display!=='none'?c.innerText.replace(/\\n+/g,' | '):''}", stage)
        if c and (not caps or caps[-1][1] != c): caps.append((round(time.time() - t0, 1), c))
        if shots < 3 and time.time() - t0 > ([12, 90, 300] if SLOW else [3, 14, 40])[shots]:
            stage.as_element().screenshot(path='%s%d.png' % (OUT, shots)); shots += 1
        if pg.evaluate("e=>[...e.querySelectorAll('.bt')].some(x=>x.textContent==='Play the tour')", stage) and time.time() - t0 > 2: break
        pg.wait_for_timeout(150)
    print('tour ended after %.1fs' % (time.time() - t0)); print('Play opened full screen:', fs_on, '| full screen closed at the end:', not pg.evaluate("e=>e.classList.contains('fs')", stage))
    print('play button box:', pg.evaluate("e=>{var r=e.querySelector('.tpb').getBoundingClientRect();return [Math.round(r.width),Math.round(r.height),Math.round(r.left+r.width/2-e.getBoundingClientRect().left),Math.round(e.getBoundingClientRect().bottom-r.bottom)]}", stage), '(w, h, center x, from bottom)')
    allc = pg.evaluate('()=>window.__caps'); print('stops visited (%d):' % len(allc), ' / '.join(allc))
    print('readings on the page:', pg.evaluate("e=>e.querySelectorAll('.rdm').length", stage))
    for t, c in caps: print(t, c[:260])
    bt = lambda: pg.evaluate("e=>e.querySelector('.tpb').textContent", stage)
    btn.click(); pg.wait_for_timeout(1500)
    stage.as_element().query_selector('canvas').click(force=True); pg.wait_for_timeout(400)
    c1 = pg.evaluate("e=>e.querySelector('.tourcap .tt').textContent", stage)
    pg.wait_for_timeout(3000)
    c2 = pg.evaluate("e=>e.querySelector('.tourcap .tt').textContent", stage)
    print('click pauses:', bt() == 'Play', '| caption held while paused:', c1 == c2, c1)
    btn.click(); pg.wait_for_timeout(300); print('play resumes:', bt() == 'Pause')
    pg.keyboard.press('Escape'); pg.wait_for_timeout(300); print('Escape ends:', bt() == 'Play the tour')
    # v246: Back and Next, the ring, and the glowing note badges
    btn.click(); pg.wait_for_timeout(2500)
    tt = lambda: pg.evaluate("e=>e.querySelector('.tourcap .tt').textContent", stage)
    nx = lambda: pg.evaluate("e=>e.querySelector('.tourbar .tpn:last-of-type, .tourbar .tpn + .tpb + .tpn').click()", stage)
    a0 = tt(); pg.evaluate("e=>[...e.querySelectorAll('.tourbar .tpn')][1].click()", stage); pg.wait_for_timeout(2200); a1 = tt()
    pg.evaluate("e=>[...e.querySelectorAll('.tourbar .tpn')][1].click()", stage); pg.wait_for_timeout(2200); a2 = tt()
    pg.evaluate("e=>[...e.querySelectorAll('.tourbar .tpn')][0].click()", stage); pg.wait_for_timeout(2200); a3 = tt()
    print('Next moves on:', a0 != a1 != a2, '| Back goes back:', a3 == a1, '|', a0, '>', a1, '>', a2, '<', a3)
    print('glowing note badges now:', pg.evaluate("e=>[...e.querySelectorAll('.lb.tfoc')].map(x=>x.textContent)", stage))
    pg.screenshot(path=OUT + 'spot.png')
    pg.keyboard.press('Escape'); pg.wait_for_timeout(300); print('Escape clears the glow:', pg.evaluate("e=>e.querySelectorAll('.lb.tfoc').length", stage) == 0)
    print('buttons now:', [x.inner_text() for x in stage.as_element().query_selector_all('.bt')], pg.evaluate("e=>[e.isConnected,e.classList.contains('fs')]", stage))
    fsb = [x for x in stage.as_element().query_selector_all('.bt') if x.inner_text() == 'Full screen'][0]
    fsb.click(); pg.wait_for_timeout(1500); btn.click(); pg.wait_for_timeout(2500)
    r = pg.evaluate("e=>{var c=e.querySelector('.tourcap').getBoundingClientRect(),l=e.querySelector('.grfs:not(.shut):not(.brand)'),lr=l&&l.offsetWidth?l.getBoundingClientRect().right:0;return [Math.round(c.left),Math.round(lr)]}", stage)
    print('full screen: caption left %d, legend right %d, clear: %s' % (r[0], r[1], r[0] >= r[1]))
    pg.screenshot(path=OUT + 'fs.png')
    print('errors:', errs)
    b.close()
