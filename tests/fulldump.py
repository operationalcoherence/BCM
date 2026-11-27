"""Pattern Analysis (tab 2) as plain text with every fold and <details> open and the 3D loaded (v275).
Usage: python3 -I fulldump.py WORKBOOK.json [JS expression to print instead of the page text]"""
import json, sys
from playwright.sync_api import sync_playwright
import os
R=os.environ.get('BCMR', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/')
SRC=open(R+'gsm-preview.js','rb').read(); REL=open(R+'gsm-relief.js','rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb=json.load(open(sys.argv[1]))['data']
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
    pg=b.new_page(viewport={'width':1300,'height':900}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e).split('\n')[0]))
    def route(r):
        u=r.request.url
        if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200,content_type='application/javascript',body=REL)
        else: r.abort()
    pg.route('**/*',route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},live:{v:'9999'}}));"%json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm',timeout=25000)
    pg.evaluate("window.gsmTab(2)"); pg.wait_for_timeout(1500)
    for _ in range(30): pg.mouse.wheel(0,600); pg.wait_for_timeout(300)
    pg.wait_for_timeout(4000)
    for _ in range(5):
        pg.evaluate("document.querySelectorAll('.closed').forEach(e=>e.classList.remove('closed'));document.querySelectorAll('details').forEach(d=>d.open=true)"); pg.wait_for_timeout(300)
    print(pg.evaluate(sys.argv[2] if len(sys.argv)>2 else "()=>document.querySelector('#gsm').innerText"))
    print("######## ERRORS", errs)
    b.close()
