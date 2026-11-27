"""v233 (plan 3c): with All notes shown on YOUR LANDSCAPE (Pattern Analysis), a tap on the ground says what
gathers there. With the 3D loaded, taps a grid of spots on the relief and prints each reading; checks that a
question selected turns it off and that All notes turns it back on. Then runs the flat fallback (no WebGL).
Usage: python3 -I groundtap.py WORKBOOK.json [OUTPREFIX]"""
import json, sys
from playwright.sync_api import sync_playwright
SRC = open('../gsm-preview.js', 'rb').read(); REL = open('../gsm-relief.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(sys.argv[1]))['data']; OUT = sys.argv[2] if len(sys.argv) > 2 else None
ok = True
def check(c, m):
    global ok
    print(('PASS ' if c else 'FAIL ') + m); ok = ok and c
def run(p, gl):
    args = ['--no-sandbox'] + (['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] if gl else ['--disable-webgl', '--disable-3d-apis'])
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=args)
    pg = b.new_page(viewport={'width': 1200, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=25000)
    pg.evaluate("window.gsmTab(2)"); pg.wait_for_timeout(800)
    if not pg.query_selector('.gterr-host[data-an]'): print('no Analysis map in this workbook'); b.close(); return
    pg.evaluate("document.querySelector('.gterr-host[data-an]').scrollIntoView({block:'center'})"); pg.wait_for_timeout(4000 if gl else 1500)
    host = pg.query_selector('.gterr-host[data-an]')
    surf = host.query_selector('.grel canvas') if gl else None
    if gl and not surf: print('3D DID NOT LOAD'); b.close(); return
    if not gl: surf = host.query_selector('canvas')
    check(bool(surf), ('3D' if gl else 'flat') + ': map surface found')
    pg.evaluate("e=>e.scrollIntoView({block:'center'})", surf); pg.wait_for_timeout(600)
    bb = surf.bounding_box()
    tipsel = '.grel .tip' if gl else '#gsm-tip, .gterr .tip'
    def tap(fx, fy):
        x, y = bb['x'] + bb['width'] * fx, bb['y'] + bb['height'] * fy
        pg.mouse.move(x, y); pg.mouse.down(); pg.mouse.up(); pg.wait_for_timeout(350)
        return pg.evaluate("h=>{var t=[...h.querySelectorAll('.tip')].find(e=>e.style.display==='block');return t?t.innerText.replace(/\\n+/g,' | '):''}", host)
    seen = []
    for fy in (0.38, 0.5, 0.62):
        for fx in (0.25, 0.5, 0.75):
            t = tap(fx, fy)
            if t.startswith('WHAT GATHERS HERE'): seen.append(t)
            print(' (%.2f,%.2f) %s' % (fx, fy, t[:700] or '-'))
    check(len(seen) >= 3, '%s: %d of 9 taps read the ground' % ('3D' if gl else 'flat', len(seen)))
    check(all(('feeling' not in t.lower()) for t in seen), 'no "feeling" in the readings')
    if OUT and seen and gl:
        tap(0.5, 0.62); pg.screenshot(path=OUT + '_3d.png', clip={'x': bb['x'] - 20, 'y': bb['y'] - 120, 'width': bb['width'] + 40, 'height': bb['height'] + 160})
    qs = [x for x in host.query_selector_all('.gtrb button') if x.inner_text().startswith('Q.')]
    if qs:
        qs[0].click(); pg.wait_for_timeout(600)
        t = tap(0.5, 0.5)
        check(not t.startswith('WHAT GATHERS HERE'), 'with a question selected, a ground tap does not read the ground')
        host.query_selector('.gtrb button').click(); pg.wait_for_timeout(600)
        t2 = [tap(fx, fy) for fy in (0.38, 0.62) for fx in (0.25, 0.5, 0.75)]
        check(any(x.startswith('WHAT GATHERS HERE') for x in t2), 'All notes again: the ground reads')
    say = pg.evaluate("h=>(h.querySelector('.gtansay')||{}).innerText||''", host)
    check('tap the ground to read what gathers there' in say, 'the line under the map says so')
    check(not errs, 'no page errors %s' % errs[:3])
    b.close()
with sync_playwright() as p:
    run(p, True)
    run(p, False)
print('ALL PASS' if ok else 'SOME FAILED')
