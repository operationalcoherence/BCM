import json, sys
from playwright.sync_api import sync_playwright
SRC=open('../gsm-preview.js','rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb=json.load(open(sys.argv[1]))['data']; nogl=sys.argv[2]=='nogl'
with sync_playwright() as p:
    args=['--no-sandbox']+(['--disable-webgl','--disable-3d-apis'] if nogl else ['--use-gl=swiftshader','--enable-unsafe-swiftshader'])
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=args)
    pg=b.new_page(viewport={'width':1400,'height':900}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)[:150]))
    def route(r):
        u=r.request.url
        if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
        elif 'gsm-preview.js' in u: r.fulfill(status=200,content_type='application/javascript',body=SRC)
        elif 'gsm-relief.js' in u: r.fulfill(status=200,content_type='application/javascript',body=open('../gsm-relief.js','rb').read())
        else: r.abort()
    pg.route('**/*',route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));"%json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm',timeout=25000)
    pg.evaluate("window.gsmTab(2)"); pg.wait_for_timeout(4000)
    hosts=pg.query_selector_all('.gtbare')
    print('bare hosts',len(hosts),'errors',errs)
    for i,h in enumerate(pg.query_selector_all('.gtbare canvas, .gtbare')[:1]):
        h.scroll_into_view_if_needed(); pg.wait_for_timeout(800)
        h.screenshot(path='/home/claude/bare_%s.png'%sys.argv[2])
    print(pg.evaluate("()=>{var h=document.querySelector('.gtbare');return h?[h.querySelectorAll('canvas').length, !!h._rel]:null}"))
    b.close()
