"""v205: hovering a question chip above YOUR LANDSCAPE shows the question and its notes.
Usage: python3 -I qhover.py WORKBOOK.json"""
import json, sys
from playwright.sync_api import sync_playwright
SRC=open('../gsm-preview.js','rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb=json.load(open(sys.argv[1]))['data']
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1400,'height':900}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    def route(r):
        u=r.request.url
        if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
        else: r.abort()
    pg.route('**/*',route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');"%json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm',timeout=25000)
    pg.evaluate("window.gsmTab(2)")
    pg.evaluate("document.querySelector('.gterr-host').scrollIntoView()"); pg.wait_for_timeout(2500)
    bs=pg.query_selector_all('.gterr-host .gtrb button')
    print('chips:',[x.inner_text() for x in bs])
    for x in bs[1:3]:
        x.hover(); pg.wait_for_timeout(150)
        print(pg.evaluate("()=>{var e=document.querySelector('.gtqpop');return e&&getComputedStyle(e).display+' | '+e.innerText}")[:500]); print('--')
    pg.mouse.move(5,5); pg.wait_for_timeout(100)
    print('after leave:',pg.evaluate("()=>getComputedStyle(document.querySelector('.gtqpop')).display"))
    print('errors:',errs)
