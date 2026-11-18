"""v213: THE TWO PICTURES, SIDE BY SIDE at the end of Pattern Synthesis. With the 3D loaded: lists each word, its
verdict, and the notes its hoses reach; taps the first word with two or more notes and checks its hoses are drawn on
the 3D relief above; screenshots the figure and the relief. Usage: python3 -I agree.py WORKBOOK.json [OUTPREFIX]"""
import json, sys
from playwright.sync_api import sync_playwright
SRC = open('../gsm-preview.js', 'rb').read(); REL = open('../gsm-relief.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(sys.argv[1]))['data']; OUT = sys.argv[2] if len(sys.argv) > 2 else '/tmp/agree'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    pg = b.new_page(viewport={'width': 1100, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=25000)
    pg.evaluate("window.gsmTab(3)"); pg.wait_for_timeout(1500)
    fig = pg.query_selector('.agfig')
    if not fig or not fig.is_visible(): print('NO FIGURE ON SYNTHESIS (visible: %s)' % (fig and fig.is_visible()), errs); sys.exit()
    # mount the Synthesis 3D first (it mounts when scrolled into view)
    for _ in range(30):
        if pg.evaluate("()=>!!window.gsmSynRel"): break
        pg.mouse.wheel(0, 500); pg.wait_for_timeout(500)
    print('Synthesis 3D mounted:', pg.evaluate("()=>!!window.gsmSynRel"))
    words = pg.evaluate("()=>[...document.querySelectorAll('.agfig svg g[role=button]')].map(g=>[...g.querySelectorAll('text')].map(t=>t.textContent).join(' '))")
    for w in words: print(' -', w)
    fig.scroll_into_view_if_needed(); pg.wait_for_timeout(600)
    fig.screenshot(path=OUT + '_fig.png')
    gs = pg.query_selector_all('.agfig svg g[role=button]')
    for i, g in enumerate(gs):
        g.click(); pg.wait_for_timeout(500)
        txt = pg.evaluate("()=>document.querySelector('.agfig .agread').innerText")
        n = pg.evaluate("()=>window.gsmSynRel&&window.gsmSynRel.hoseCount()")
        print('tap %d: hoses on the 3D = %s | %s' % (i, n, txt[:300]))
        if n and n > 0:
            fig.screenshot(path=OUT + '_sel.png')
            pg.evaluate("()=>window.gsmSynHost.scrollIntoView({block:'center'})"); pg.wait_for_timeout(2500)
            pg.screenshot(path=OUT + '_3d.png'); break
        g.click(); pg.wait_for_timeout(300)
    print('In Parallel old 3D folded:', pg.evaluate("()=>{var d=document.querySelector('details.parold');return d?!d.open:'none'}"))
    print('errors:', errs); b.close()
