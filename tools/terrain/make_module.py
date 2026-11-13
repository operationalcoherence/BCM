import os
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import re, json, sys
src=open(os.path.join(R,'mockups/terrain.html')).read()
src=src.replace('sel.value="clinic";setModel(SAMPLES.clinic.notes,SAMPLES.clinic.goal,SAMPLES.clinic.a,SAMPLES.clinic.cards);','setModel(SAMPLES.nov7.notes,SAMPLES.nov7.goal,SAMPLES.nov7.a,SAMPLES.nov7.cards);')
css=re.search(r'<style>(.*?)</style>',src,re.S).group(1)
body=re.search(r'<div class="wrap">(.*?)</div>\s*<script>',src,re.S).group(1)
js=re.search(r'<script>\s*"use strict";(.*)</script>',src,re.S).group(1)

# ---- CSS: scope under .gterr
rules=[]
for m in re.finditer(r'([^{}]+)\{([^}]*)\}',css):
    sel_,decl=m.group(1).strip(),m.group(2)
    if sel_ in (':root','*','body','.wrap','.kick','h1'): continue
    decl=decl.replace('var(--ink)','#222').replace('var(--mute)','#777').replace('var(--line)','#ddd')
    sels=','.join('.gterr '+x.strip() for x in sel_.split(','))
    rules.append(sels+'{'+decl+'}')
rules.append('.gterr{color:#222;line-height:1.45;margin:6px 0 18px}.gterr *{box-sizing:border-box}')
rules.append('.gtold{margin:10px 0 18px}')
CSS=''.join(rules)

# ---- template
t=body
t=re.sub(r'\s*<div class="kick">.*?</div>','',t,flags=re.S)
t=re.sub(r'\s*<h1>.*?</h1>','',t,flags=re.S)
import re as _re2
t=_re2.sub(r'<div class="sub">.*?</div>','<div class="plab">THE LAY OF THE LAND</div><div class="sub">The ground your notes describe, read before Taking Action leads you across it. The numbers on the ground are explained below the map. Drag to turn it; scroll or pinch to zoom.</div>',t,count=1,flags=_re2.S)
t=re.sub(r'\s*<label>Workbook\s*<select id="sel"></select>\s*</label>','',t)
t=re.sub(r'\s*<button id="load" type="button">Load your saved workbook…</button>','',t)
t=re.sub(r'\s*<input id="file"[^>]*>','',t)
t=t.replace(' The wording on this page is a placeholder.','')
t=re.sub(r' id="([A-Za-z0-9_-]+)"',r' data-gt="\1"',t)
assert ' id=' not in t
t=re.sub(r'\s+\n','\n',t).strip()
TPL=json.dumps(t)

# ---- JS
j=js
a=j.index('var SAMPLES={};'); b=j.index('/* ---------- state ---------- */')
j=j[:a]+j[b:]
a=j.index('var sel=document.getElementById("sel");'); E='rd.readAsText(f);};'; b=j.index(E,a)+len(E)
j=j[:a]+j[b:]
j=j.replace('el.textContent=sel.value==="user"?"Courses of action come from Taking Action. In this mock-up they are built in only for the sample workbooks; once this is part of the workbook, every card will be here.":"This workbook has no courses of action yet. Taking Action opens once all seven questions are answered.";return;}',
            'el.textContent="";el.style.display="none";var sh=el.previousElementSibling;if(sh)sh.style.display="none";return;}')
j=re.sub(r'view=\{az:0\.05,tilt:0\.6,zoom:1\.1\};setModel\(SAMPLES[^\n]*','view={az:0.05,tilt:0.6,zoom:1.1};setModel(data.m||[],data.goal||"",data.a||[],data.cards||null);',j)
import re as _r
for _w in ['sel.value','SAMPLES','userOpt']:
    for _m in _r.finditer(_r.escape(_w),j): print(_w,repr(j[_m.start()-60:_m.start()+40]))
assert 'sel.value' not in j and 'SAMPLES' not in j and 'userOpt' not in j
j=j.replace('document.getElementById(','$(')
j=j.replace('document.querySelectorAll(".rd")','host.querySelectorAll(".rd")')
j=j.replace('window.addEventListener("resize",resize);','function onR(){if(!host.isConnected){window.removeEventListener("resize",onR);return;}resize();}window.addEventListener("resize",onR);')
assert 'setModel(data.m' in j
assert 'document.getElementById' not in j
# size from the stage itself: it may be hidden (another tab) when mounted
j=j.replace('function resize(){var w=$("stage").clientWidth;','function resize(){var w=$("stage").clientWidth;if(!w)return;')
j=j.replace('function onR(){if(!host.isConnected){window.removeEventListener("resize",onR);return;}resize();}window.addEventListener("resize",onR);',
 'function onR(){if(!host.isConnected){window.removeEventListener("resize",onR);if(ro)ro.disconnect();return;}resize();}window.addEventListener("resize",onR);var ro=window.ResizeObserver?new ResizeObserver(function(){onR();}):null;if(ro)ro.observe($("stage"));')
# legend sits under the model when the column is narrow
j=j.replace('function fillLegendBox(){var el=$("legbox");el.innerHTML="";el.classList.toggle("hide",!LEGON);',
 'function fillLegendBox(){var el=$("legbox");el.innerHTML="";el.classList.toggle("hide",!LEGON);var nar=$("stage").clientWidth<760&&!isFull();el.style.position=nar?"static":"";el.style.width=nar?"auto":"";el.style.margin=nar?"6px 0 0":"";el.style.columnCount=nar?"2":"";if(nar&&el.parentNode===$("stage"))$("stage").parentNode.insertBefore(el,$("stage").nextSibling);if(!nar&&el.parentNode!==$("stage"))$("stage").appendChild(el);')
j=j.replace('document.addEventListener("fullscreenchange",function(){setTimeout(resize,50);});','document.addEventListener("fullscreenchange",function(){setTimeout(function(){resize();fillLegendBox();render();},50);});')
j=j.replace('$S().classList.add("full");resize();','$S().classList.add("full");resize();fillLegendBox();render();')
j=j.replace('$S().classList.remove("full");resize();','$S().classList.remove("full");resize();fillLegendBox();render();')
assert 'if(!w)return;' in j and 'ResizeObserver' in j and 'var nar=' in j

MOD='''
/* ---- Pattern Synthesis terrain (layer: the ground ahead) ---- */
!function(){var CSS=%s,TPL=%s;
function mount(host,data){"use strict";host.className+=" gterr";host.innerHTML=TPL;function $(id){return host.querySelector('[data-gt="'+id+'"]');}
%s
}
window.gsmTerrainMount=mount;
function scan(){document.querySelectorAll(".gterr-host:not([data-on])").forEach(function(h){h.setAttribute("data-on","1");try{mount(h,window.gsmTD||{})}catch(e){h.textContent="";h.style.display="none";if(window.console)console.warn("terrain",e)}})}
function start(){if(!document.getElementById("gsm-tcss")){var s=document.createElement("style");s.id="gsm-tcss";s.textContent=CSS;document.head.appendChild(s)}new MutationObserver(scan).observe(document.body,{childList:true,subtree:true});scan()}
document.body?start():document.addEventListener("DOMContentLoaded",start)}();
'''%(json.dumps(CSS),TPL,j)
open(os.path.join(R,'tools/terrain/module.js'),'w').write(MOD)
print(len(MOD))
