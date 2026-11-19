"""v237: Way A on strategy cards follows the data. Opens every card's folds, mounts its map, and prints each
way's name and reading plus the stats of way A (the path the ground points). Usage: python3 -I waya.py WORKBOOK.json [GSMJS]"""
import json, sys
from playwright.sync_api import sync_playwright
SRC = open(sys.argv[2] if len(sys.argv) > 2 else '../gsm-preview.js', 'rb').read(); REL = open('../gsm-relief.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    wb = json.load(open(sys.argv[1]))['data']; pg = b.new_page(viewport={'width': 1400, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
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
    pg.evaluate("document.querySelectorAll('#gsm [data-pv=\"4\"] details, #gsm .coa details').forEach(d=>d.open=true)"); pg.wait_for_timeout(500)
    n = pg.evaluate("document.querySelectorAll('#gsm .coa').length")
    for i in range(n):
        pg.evaluate("i=>{var c=document.querySelectorAll('#gsm .coa')[i];c.querySelectorAll('details').forEach(d=>d.open=true);var t=c.querySelector('.tawhy');t&&t.click&&0;c.scrollIntoView()}", i); pg.wait_for_timeout(1300)
        r = pg.evaluate("""i=>{var c=document.querySelectorAll('#gsm .coa')[i];var t=(c.querySelector('.hd b')||{}).textContent||'';var m=(c.querySelector('.mode')||{}).textContent||'';
          var rd=[...c.querySelectorAll('.gtread div, .gtways div, .taways div, .cr')].map(e=>e.textContent).filter(x=>/^A[ :·]|^Way A|ground points|way through its notes/i.test(x)).slice(0,2);
          var all=c.innerText.match(/(The way the ground points[^\\n]{0,180}|Its way through its notes[^\\n]{0,120})/g)||[];return [t,m,all.slice(0,2)]}""", i)
        if r[2]: print('==', r[1], '|', r[0][:70]); [print('    ', x[:300]) for x in r[2]]
    print('errors:', list(dict.fromkeys(errs))[:3])
    b.close()
