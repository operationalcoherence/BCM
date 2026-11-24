"""v248: screenshot of YOUR STORY SO FAR on Pattern Analysis."""
import json, sys
from playwright.sync_api import sync_playwright
SRC=open('../gsm-preview.js','rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    for f in sys.argv[1:]:
        wb=json.load(open(f))['data']
        pg=b.new_page(viewport={'width':1200,'height':900})
        def route(r):
            u=r.request.url
            if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
            elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
            else: r.abort()
        pg.route('**/*',route)
        pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');"%json.dumps(json.dumps(wb)))
        pg.goto('http://t.local/'); pg.wait_for_selector('#gsm'); pg.wait_for_timeout(1000)
        pg.evaluate("window.gsmTab(2)"); pg.wait_for_timeout(3500)
        el=pg.query_selector('.storylead')
        print(f, pg.evaluate("()=>{var d=document.querySelector('details.onel');return d?d.innerText.slice(0,300):'no fold'}"))
        el.screenshot(path='out/story_'+f.replace('.json','')+'.png')
        pg.close()
    b.close()
