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
rules.append("#gsm .gtfsb{float:right;background:#fff;color:#222;border:1px solid #222;font:11.5px 'Questrial',sans-serif;padding:3px 9px;cursor:pointer;margin:-3px 0 0 8px;letter-spacing:.03em}#gsm .coa.gtfs-on{position:fixed;top:0;left:0;right:0;bottom:0;z-index:2147483000;background:#fff;overflow:auto;margin:0;border:0;padding:0 2vw 48px;-webkit-overflow-scrolling:touch}#gsm .coa.gtfs-on .selbox,#gsm .coa.gtfs-on .csn,#gsm .coa.gtfs-on .coacall,#gsm .coa.gtfs-on .cq{max-width:960px}.gtrb{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:0 0 6px;font:12px 'Questrial',sans-serif}.gtrb span{letter-spacing:.1em;color:#555;margin-right:2px}.gtrb button{background:#fff;color:#111;border:2px solid #111;border-radius:14px;padding:4px 11px;font:12.5px 'Questrial',sans-serif;cursor:pointer}.gtrb button.on{background:#111;color:#fff}#gsm .coa.gtfs-on .hd{padding-top:56px}#gsm .coa.gtfs-on .gtfsb{position:fixed;top:10px;right:12px;z-index:2147483001;background:#222;color:#fff;padding:9px 15px;font-size:14px;margin:0}")
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
# on a card the numbered readings are not shown, so name stuck places plainly
_o='if(st.pits.length)o.push("It passes through "+list(st.pits.map(pitName))+".");'
assert j.count(_o)==1
j=j.replace(_o,'if(st.pits.length)o.push(CARDH?"It passes through "+(st.pits.length===1?"a place":st.pits.length+" places")+" where it is easy to get stuck.":"It passes through "+list(st.pits.map(pitName))+".");')
# one terrain per workbook, shared by Pattern Synthesis and every Taking Action card
assert j.count('terr=buildTerrain(prep(curRaw));')==1
j=j.replace('terr=buildTerrain(prep(curRaw));','var tk=ver+"|"+growK+"|"+JSON.stringify(curRaw);terr=TC[tk]||(TC[tk]=buildTerrain(prep(curRaw)));')
assert j.count('terr=buildTerrain(notes);')==1
j=j.replace('terr=buildTerrain(notes);','var tk0=ver+"|"+growK+"|"+JSON.stringify(raw);terr=TC[tk0]||(TC[tk0]=buildTerrain(notes));')
assert j.count('buildTerrain(')==3
assert j.count('Math.round(Math.max(380,Math.min(620,w*0.62)))')==1
j=j.replace('Math.round(Math.max(380,Math.min(620,w*0.62)))','Math.round(CARDH?(host.closest(".gtfs-on")?Math.max(420,window.innerHeight*0.8):Math.max(300,Math.min(520,w*0.62))):Math.max(380,Math.min(620,w*0.62)))')


# ---- v166: card map fills its frame, readable labels, colored routes with a one-at-a-time selector
def rep(a,b,n=1):
    global j
    assert j.count(a)==n,(j.count(a),a[:70])
    j=j.replace(a,b)
rep('var P={}; /* projection */','var P={},FIT=null,TS=1,TL=1,ROUTESEL=null,RCOL={A:"#111111",B:"#0a4fff",C:"#e0007a"}; /* projection */')
rep('P.cy=cssH*0.5;P.D=900;\n}',
 'P.cy=cssH*0.5;P.D=900;\n'
 '  TS=CARDH?Math.max(1,Math.min(1.9,cssW/620)):1;TL=1+(TS-1)*0.6;\n'
 '  if(CARDH&&terr&&zArr){var fk=cssW+"|"+cssH+"|"+view.az+"|"+view.tilt+"|"+VX+"|"+VY+"|"+exag;\n'
 '    if(!FIT||FIT.k!==fk){var z0=view.zoom;view.zoom=1;P.base=Math.min(cssW/(W*1.3),cssH/(HH*1.6));P.cx=0;P.cy=0;var o9=[0,0],x0=1e9,x1=-1e9,y0=1e9,y1=-1e9,i9,j9,sp9=Math.max(1,Math.floor(VX/70));\n'
 '      for(j9=0;j9<VY;j9+=sp9)for(i9=0;i9<VX;i9+=sp9){pr(wx(i9*CX),zArr[j9*VX+i9],wz(j9*CY),o9);if(o9[0]<x0)x0=o9[0];if(o9[0]>x1)x1=o9[0];if(o9[1]<y0)y0=o9[1];if(o9[1]>y1)y1=o9[1];}\n'
 '      view.zoom=z0;FIT={k:fk,z:Math.min(0.9*cssW/(x1-x0||1),0.84*cssH/(y1-y0||1)),dx:-(x0+x1)/2,dy:-(y0+y1)/2};}\n'
 '    var zz=view.zoom*FIT.z;P.base=Math.min(cssW/(W*1.3),cssH/(HH*1.6))*zz;P.cx=cssW/2+FIT.dx*zz;P.cy=cssH*0.53+FIT.dy*zz;}\n}')
# fonts and sizes scale with the map
rep('ctx.font="9px Questrial,sans-serif";ctx.textAlign="left";ctx.lineWidth=2.6;','ctx.font=(9*TS)+"px Questrial,sans-serif";ctx.textAlign="left";ctx.lineWidth=2.6;')
rep('ctx.strokeText("N"+p.n.k,p.x+5,p.y+3);','ctx.strokeText("N"+p.n.k,p.x+5*TS,p.y+3*TS);')
rep('ctx.fillText("N"+p.n.k,p.x+5,p.y+3);','ctx.fillText("N"+p.n.k,p.x+5*TS,p.y+3*TS);')
rep('ctx.fillRect(b1[0]-11,b1[1]-8,22,12);ctx.font="bold 9px','ctx.fillRect(b1[0]-11*TS,b1[1]-8*TS,22*TS,12*TS);ctx.font="bold "+(9*TS)+"px')
rep('ctx.fillRect(b1[0]-10,b1[1]-8,20,12);ctx.font="bold 9px','ctx.fillRect(b1[0]-10*TS,b1[1]-8*TS,20*TS,12*TS);ctx.font="bold "+(9*TS)+"px')
rep('ctx.font=(opt.size||11)+"px Questrial,sans-serif"','ctx.font=((opt.size||11)*TS)+"px Questrial,sans-serif"')
rep('ctx.font="bold 15px Questrial,sans-serif";ctx.textAlign="center";var w=ctx.measureText(str).width+22;','ctx.font="bold "+(15*TS)+"px Questrial,sans-serif";ctx.textAlign="center";var w=ctx.measureText(str).width+22*TS;')
rep('var labelPins=terr.notes.length<=45,','var labelPins=terr.notes.length<=(CARDH&&host.closest(".gtfs-on")?100:45),')
# routes: own colors, one at a time
rep('stroke(o,"rgba(255,255,255,.95)",5.2);stroke(o,"#111",2.6,R.dash);});',
    'var dm=ROUTESEL&&R.key!==ROUTESEL;ctx.globalAlpha=dm?0.16:1;stroke(o,"rgba(255,255,255,.95)",5.6*TL);stroke(o,RCOL[R.key]||"#111",3.2*TL,R.dash);ctx.globalAlpha=1;});')
rep('ctx.arc(c0[0],c0[1],8,0,6.283);ctx.strokeStyle="#111";ctx.lineWidth=2;ctx.stroke();});}','ctx.arc(c0[0],c0[1],8*TL,0,6.283);ctx.strokeStyle="#111";ctx.lineWidth=2;ctx.stroke();});}')
a=j.index('markScr=[];if(COURSE!=null)ROUTES.forEach(function(R){var q=R.pts[Math.floor(R.pts.length*(R.key==="A"?0.3')
E='ctx.fillText(R.key,b1[0],b1[1]+4);});'
b=j.index(E,a)+len(E)
j=j[:a]+('markScr=[];if(COURSE!=null)ROUTES.forEach(function(R){if(ROUTESEL&&R.key!==ROUTESEL)return;var off=R.key==="B"?0.05:R.key==="C"?0.1:0;[0.2,0.5,0.8].forEach(function(f){var q=R.pts[Math.min(R.pts.length-1,Math.floor(R.pts.length*(f+off)))],z=zAt(q[0],q[1]),b1=pr(wx(q[0]),z+4,wz(q[1]),[0,0]);'
 'ctx.beginPath();ctx.arc(b1[0],b1[1],10*TS,0,6.283);ctx.fillStyle=RCOL[R.key]||"#111";ctx.fill();ctx.strokeStyle="#fff";ctx.lineWidth=2.4;ctx.stroke();ctx.font="bold "+(12*TS)+"px Questrial,sans-serif";ctx.textAlign="center";ctx.fillStyle="#fff";ctx.fillText(R.key,b1[0],b1[1]+4*TS);});});')+j[b:]
rep('n.style.background=r.k?"#fff":"#7a1d12";n.style.color=r.k?"#111":"#fff";n.style.border="2px solid #111";','n.style.background=r.k?(RCOL[r.k]||"#111"):"#7a1d12";n.style.color="#fff";n.style.border="2px solid #fff";n.style.boxShadow="0 0 0 1px "+(r.k?(RCOL[r.k]||"#111"):"#7a1d12");')

exec(open(os.path.join(R,'tools/terrain/patch_v167.py')).read())
exec(open(os.path.join(R,'tools/terrain/patch_relief.py')).read())
MOD='''
/* ---- Pattern Synthesis terrain (layer: the ground ahead) ---- */
!function(){var CSS=%s,TPL=%s,TC={},QU=[],QB=0;function pump(){var f=QU.shift();if(!f){QB=0;return;}f();setTimeout(pump,16);}
function mount(host,data){"use strict";host.className+=" gterr";host.innerHTML=TPL;function $(id){return host.querySelector('[data-gt="'+id+'"]');}var CARDH=!!data.card;
%s
if(CARDH){host.classList.add("gtcard");
  host.querySelectorAll(".plab,.sub,.bar,.gfold").forEach(function(e){e.style.display="none";});
  ["crshead","courses","rdhead","readings","selnote","msg"].forEach(function(id){var e=$(id);if(e)e.style.display="none";});
  host._gtRe=function(){resize();render();};LEGON=false;showCause=false;var cw0=host.clientWidth||600;view={az:0.05,tilt:0.72,zoom:1};setCourse(0);
  if(ROUTES.length>1){var rb=document.createElement("div");rb.className="gtrb";rb.innerHTML="<span>Show</span>";function rbtn(key,label,col){var b=document.createElement("button");b.type="button";b.textContent=label;if(col)b.style.borderColor=col;b.onclick=function(){ROUTESEL=key;[].slice.call(rb.querySelectorAll("button")).forEach(function(x){x.classList.toggle("on",x===b)});render();};if(!key)b.classList.add("on");rb.appendChild(b);}
    rbtn(null,"All ways","#111");ROUTES.forEach(function(R){rbtn(R.key,R.key+": "+(/firm ground/.test(R.name)?"firm ground only":/support/.test(R.name)?"from the support":"through its notes"),(R.key==="B"?"#111":RCOL[R.key]));});$("stage").parentNode.insertBefore(rb,$("stage"));}
  var bx=$("coursebox").querySelector(".selbox");if(bx){var kids=[].slice.call(bx.children);kids.slice(0,3).forEach(function(e){e.remove();});var last=bx.lastElementChild;if(last&&last.classList.contains("small"))last.remove();}
}
if(!CARDH)(function(){var stg=$("stage"),box=document.createElement("div");stg.parentNode.insertBefore(box,stg);
  function go(){(window.__gsmRelP||(window.__gsmRelP=new Promise(function(ok,no){if(window.gsmRelief)return ok();var sc=document.querySelector('script[src*="gsm-preview.js"]'),src=sc?sc.src.replace(/gsm-preview\\.js/,"gsm-relief.js"):"gsm-relief.js",s=document.createElement("script");s.src=src;s.onload=function(){window.gsmRelief?ok():no();};s.onerror=no;document.head.appendChild(s);}))).then(function(){
    if(!host.isConnected||host._rel)return;var c=document.createElement("canvas");if(!(c.getContext("webgl2")||c.getContext("webgl")))return;
    var D={VX:VX,VY:VY,CX:CX,CY:CY,hn:terr.hn,START:START,GOAL:GOAL,emo:EMO,qpos:terr.qpos.map(function(Q){return Q?{q:Q.q,x:Q.x,y:Q.y,n:Q.n,title:QT[Q.q-1]||"",ans:String(ANSWERS[Q.q-1]||"").trim()}:null;}),notes:terr.notes.map(function(n){return {k:n.k,x:n.x,y:n.y,e:n.e,q:n.q,t:n.t};}),read:READ.map(function(r){return {at:r.at,title:r.title,text:r.short+(r.more?" "+r.more:"")};}),goalText:GOALTEXT,onHL:function(i){if(!HLSTICK){HL=i;markList();}}};
    try{host._rel=window.gsmRelief.mount(box,D);}catch(e){box.innerHTML="";host._rel=null;if(window.console)console.warn("relief",e);return;}
    stg.style.display="none";var lb=$("legbox");if(lb)lb.style.display="none";host.querySelectorAll(".bar").forEach(function(e){e.style.display="none";});
  }).catch(function(){});}
  if(window.IntersectionObserver){var io=new IntersectionObserver(function(es){if(es.some(function(x){return x.isIntersecting;})){io.disconnect();go();}},{rootMargin:"300px"});io.observe(box.parentNode);}else go();
})();
}
window.gsmTerrainMount=mount;
function addFS(h){var coa=h.closest(".coa"),lab=h.previousElementSibling;if(!coa||!lab||lab.querySelector(".gtfsb"))return;
  var b=document.createElement("button");b.type="button";b.className="gtfsb";b.textContent="Full screen";lab.insertBefore(b,lab.firstChild);
  function set(on){coa.classList.toggle("gtfs-on",on);b.textContent=on?"Close full screen":"Full screen";document.documentElement.style.overflow=on?"hidden":"";
    if(on)coa.scrollTop=0;if(h._gtRe)h._gtRe(on);setTimeout(function(){if(h._gtRe)h._gtRe()},300)}
  b.addEventListener("click",function(){set(!coa.classList.contains("gtfs-on"))});
  document.addEventListener("keydown",function(e){if(e.key==="Escape"&&coa.classList.contains("gtfs-on"))set(false)})}
function scan(){document.querySelectorAll(".gterr-host:not([data-on])").forEach(function(h){h.setAttribute("data-on","1");try{mount(h,window.gsmData?window.gsmData():(window.gsmTD||{}))}catch(e){h.textContent="";h.style.display="none";if(window.console)console.warn("terrain",e)}});
document.querySelectorAll(".gterr-card:not([data-on])").forEach(function(h){h.setAttribute("data-on","1");
  function go(){QU.push(go1);if(!QB){QB=1;setTimeout(pump,0);}}
  function go1(){if(h.getAttribute("data-m")||!h.isConnected)return;h.setAttribute("data-m","1");var fb=h.innerHTML,cls=h.className;
    try{var d=window.gsmData?window.gsmData():(window.gsmTD||{}),st=[];try{st=JSON.parse(h.getAttribute("data-steps")||"[]")}catch(e){}
      mount(h,{m:d.m||[],a:d.a||[],goal:d.goal||"",card:1,cards:[{w:"",why:"",mode:h.getAttribute("data-mode")==="PROGRAM"?"PROGRAM":"STRATEGY",ids:(h.getAttribute("data-ids")||"").split(",").map(function(x){x=x.trim();var m=/^(?:note\\s*|N)(\\d+)$/i.exec(x);return m?"N"+m[1]:x;}).filter(Boolean),steps:st}]});addFS(h)}
    catch(e){h.innerHTML=fb;h.className=cls;if(window.console)console.warn("terrain card",e)}}
  if(window.IntersectionObserver){var io=new IntersectionObserver(function(es){if(es.some(function(x){return x.isIntersecting})){io.disconnect();go();}},{rootMargin:"400px"});io.observe(h);}else go();});}
function start(){if(!document.getElementById("gsm-tcss")){var s=document.createElement("style");s.id="gsm-tcss";s.textContent=CSS;document.head.appendChild(s)}new MutationObserver(scan).observe(document.body,{childList:true,subtree:true});scan()}
document.body?start():document.addEventListener("DOMContentLoaded",start)}();
'''%(json.dumps(CSS),TPL,j)
open(os.path.join(R,'tools/terrain/module.js'),'w').write(MOD)
print(len(MOD))
