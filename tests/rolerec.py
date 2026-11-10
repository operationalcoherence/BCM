import sys
src=open('../gsm-preview.js').read()
old='function lo(t){return t.slice().sort(function(t,e){return(g[e]||0)-(g[t]||0)||t.localeCompare(e)})}'
assert src.count(old)==1
new='''function lo(t){var old=t.slice().sort(function(t,e){return(g[e]||0)-(g[t]||0)||t.localeCompare(e)});
try{if(lo._g!==g){lo._g=g;lo._H={};lo._X={};a.forEach(function(n){if(n.line){var s=n.line[2]<118?lo._H:lo._X;for(var q in n.t.k)s[q]=1}})}
var R={},G={},ik=function(w,n){return!!(i[n-1]&&i[n-1].k[w])},rng=function(w,a1,b1){for(var n=a1;n<=b1;n++)if(ik(w,n))return 1;return 0};
old.forEach(function(w){var f=[],m=!!k[w],any=rng(w,1,7),q2=ik(w,2),q3=ik(w,3),q4=ik(w,4),gl=!!r.k[w];
if(q2&&!rng(w,4,7)&&!m)f.push("oppNE");if(gl&&!any&&!m)f.push("goalNR");if(q4&&!rng(w,5,7)&&!m)f.push("condNot");
if(q3&&!ik(w,7))f.push("suppNR");if(any&&!m)f.push("saidNM");if(m&&!any)f.push("mapNA");if(q2&&q3)f.push("forAg");
if(lo._H[w]&&lo._X[w])f.push("cross");if(rng(w,1,4)&&rng(w,5,7))f.push("carry");R[w]=f;G[w]=g[w]||0});
(window.__lo=window.__lo||[]).push({old:old,roles:R,g:G})}catch(e){window.__loerr=String(e)}
return old}'''
open('../rec_tmp.js','w').write(src.replace(old,new))
print('ok')
