import sys
from playwright.sync_api import sync_playwright
f, out, q = sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv)>3 else ''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
    pg=b.new_page(viewport={'width':1600,'height':1000})
    errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
    pg.goto('file://'+f+q); pg.wait_for_function('window.__ready',timeout=120000); pg.wait_for_timeout(2500)
    pg.screenshot(path=out,timeout=120000); print('errs',errs[:3])
    b.close()
