import json, sys, time, traceback
from playwright.sync_api import sync_playwright
SRC=open('gsm-pretty.js','rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
TABS=[(5,'Start'),(0,'MapCtx'),(1,'MapChg'),(2,'Analysis'),(3,'Synthesis'),(6,'Parallel'),(4,'Action')]
files=sys.argv[1:]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    for f in files:
        wb=json.load(open(f))['data']
        pg=b.new_page(viewport={'width':1400,'height':900}); errs=[]
        pg.on('pageerror',lambda e:errs.append('PAGEERROR: '+str(e).split('\n')[0]))
        pg.on('console',lambda m:(errs.append('CONSOLE: '+m.text) if m.type=='error' and 'ERR_FAILED' not in m.text else None))
        def route(r):
            u=r.request.url
            if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
            elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
            else: r.abort()
        pg.route('**/*',route)
        pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');"%json.dumps(json.dumps(wb)))
        t0=time.time()
        try:
            pg.goto('http://t.local/'); pg.wait_for_selector('#gsm',timeout=25000)
        except Exception as e:
            print(f, 'BOOT FAILED', e); pg.close(); continue
        boot=time.time()-t0
        times={}
        for n,label in TABS:
            t1=time.time()
            try:
                pg.evaluate("window.gsmTab&&window.gsmTab(%d)"%n); pg.wait_for_timeout(120)
                pg.wait_for_function("()=>true")
                words=pg.evaluate("()=>document.querySelector('#gsm').innerText.split(/\\s+/).filter(Boolean).length")
            except Exception as e:
                errs.append('TAB %s THREW %s'%(label,str(e)[:90])); words=-1
            times[label]=(round((time.time()-t1)*1000), words)
        xss=pg.evaluate("()=>[!!window.XSS,!!window.XSS2]")
        print('%-18s boot=%4dms %s xss=%s' % (f.replace('wb_','').replace('.json',''), boot*1000, ' '.join('%s:%dms/%dw'%(k,v[0],v[1]) for k,v in times.items()), xss))
        for e in dict.fromkeys(errs): print('    !!', e[:170])
        pg.close()
    b.close()
