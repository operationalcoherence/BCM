import json, sys
from playwright.sync_api import sync_playwright
JS, WB = sys.argv[1], sys.argv[2]
SRC=open(JS,'rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb=json.load(open(WB))['data']
# make it a combined-style workbook: pad to 10, give two notes another author
for i,n in enumerate(wb['m']):
    while len(n)<10: n.append(None)
wb['m'][1][9]='Sam'; wb['m'][3][9]='Sam'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1400,'height':1000}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    def route(r):
        u=r.request.url
        if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
        else: r.abort()
    pg.route('**/*',route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');"%json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm',timeout=20000); pg.wait_for_timeout(1200)
    pg.evaluate("window.gsmTab(1)"); pg.wait_for_timeout(800)
    pg.evaluate("document.querySelector('#gsm-view [data-v=line]')&&document.querySelector('#gsm-view [data-v=line]').click()"); pg.wait_for_timeout(500)
    print('version', pg.evaluate("document.getElementById('gsm-ver').textContent"))
    for j in [0,1,3,5]:
        el=pg.locator('#gsm-marks > g[data-j="%d"]'%j)
        el.scroll_into_view_if_needed(); bb=el.bounding_box()
        pg.mouse.move(bb['x']+bb['width']/2+1,bb['y']+bb['height']/2+1); pg.mouse.move(bb['x']+bb['width']/2,bb['y']+bb['height']/2); pg.wait_for_timeout(200)
        print(j, pg.evaluate("(()=>{var t=document.querySelector('.gsm-tt');return t&&t.style.display!=='none'?t.innerText.split('\\n')[0]:'(none)'})()"))
    print('ERRORS',errs); b.close()
