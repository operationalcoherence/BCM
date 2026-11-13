# v167: relief look approved 12 Nov 2026 (substrate + 60% emotion hue + rock face), deeper defiance,
# bigger markers, HELP off the land, solid block sides. Exec'd by make_module.py with j and TPL in scope.
rep('var bad=1.5*sw[0]+sw[2]+2*sw[4]','var bad=1.5*sw[0]+sw[2]+3.4*sw[4]')
a=j.index('  cellCol=new Array(NX*NY);\n  for(var j=0;j<NY;j++)for(var i=0;i<NX;i++){')
b=j.index('\nfunction boost(',a)
j=j[:a]+open(os.path.join(R,'tools/terrain/prepare_v167.js')).read().rstrip('\n')+j[b:]
rep('var L=[-0.6,0.5,-0.6],ln=','var L=[-0.6,0.62,-0.6],ln=')
rep('  var bx=HALF_X+16,bz=HALF_Z+16,YT=0;',
 '  var bx=HALF_X+16,bz=HALF_Z+16,YT=0;\n'
 '  var ZB=_zmin()-12;\n'
 '  function side(edge){var top=[],bot=[];edge.forEach(function(e){top.push(pr(wx(e[0]),zAt(e[0],e[1]),wz(e[1]),[0,0]));bot.push(pr(wx(e[0]),ZB,wz(e[1]),[0,0]));});\n'
 '    ctx.beginPath();top.forEach(function(p,k){k?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]);});for(var k=bot.length-1;k>=0;k--)ctx.lineTo(bot[k][0],bot[k][1]);ctx.closePath();ctx.fillStyle="#1d1c1a";ctx.fill();ctx.strokeStyle="#1d1c1a";ctx.lineWidth=1;ctx.stroke();}\n'
 '  var SE={s:[],n:[],w:[],e:[]};for(var se=0;se<=80;se++){var tt=se/80;SE.s.push([tt*W,HH]);SE.n.push([tt*W,0]);SE.w.push([0,tt*HH]);SE.e.push([W,tt*HH]);}\n'
 '  ["n","w","e","s"].forEach(function(k){side(SE[k]);});\n'
 '  (function(){var p=pr(wx(W/2),(zAt(W/2,HH)+ZB)/2-2,wz(HH),[0,0]);ctx.font="bold "+Math.round(16*TS)+"px Questrial,sans-serif";ctx.textAlign="center";ctx.fillStyle="rgba(255,255,255,.88)";ctx.fillText("\\u2193  HINDER",p[0],p[1]+5);})();')
rep('[0.5].forEach(function(f){var x=W*f;badge("↑ HELP",wx(x),zAt(x,4)+10,wz(-6),"#1f6f66");badge("↓ HINDER",wx(x),zAt(x,HH-4)+10,wz(HH+8),"#8a2a22");});',
    '(function(){var p=pr(wx(-6),zAt(0,2)+6,wz(2),[0,0]);ctx.font="bold "+Math.round(15*TS)+"px Questrial,sans-serif";ctx.textAlign="right";ctx.lineWidth=3.4;ctx.strokeStyle="rgba(255,255,255,.95)";ctx.strokeText("\\u2191 HELP",p[0],p[1]);ctx.fillStyle="#1f6f66";ctx.fillText("\\u2191 HELP",p[0],p[1]);})();')
rep('view.zoom=z0;FIT={k:fk,','var zb9=_zmin()-12;[[0,0],[W,0],[0,HH],[W,HH]].forEach(function(cr){pr(wx(cr[0]),zb9,wz(cr[1]),o9);if(o9[0]<x0)x0=o9[0];if(o9[0]>x1)x1=o9[0];if(o9[1]<y0)y0=o9[1];if(o9[1]>y1)y1=o9[1];});\n      view.zoom=z0;FIT={k:fk,')
rep('pr(wx(nt.x),z+9,wz(nt.y),[0,0]);','pr(wx(nt.x),z+13,wz(nt.y),[0,0]);')
rep('ctx.arc(p1[0],p1[1],3.8,0,6.283);ctx.fillStyle=','ctx.arc(p1[0],p1[1],6*TS,0,6.283);ctx.fillStyle=')
rep('ctx.arc(p1[0],p1[1],3.8,0,6.283);ctx.strokeStyle="#111"','ctx.arc(p1[0],p1[1],6*TS,0,6.283);ctx.strokeStyle="#111"')
rep('ctx.font=(9*TS)+"px Questrial,sans-serif";ctx.textAlign="left";','ctx.font="bold "+(13*TS)+"px Questrial,sans-serif";ctx.textAlign="left";')
rep('ctx.strokeText("N"+p.n.k,p.x+5*TS,p.y+3*TS);','ctx.strokeText("N"+p.n.k,p.x+8*TS,p.y+4*TS);')
rep('ctx.fillText("N"+p.n.k,p.x+5*TS,p.y+3*TS);','ctx.fillText("N"+p.n.k,p.x+8*TS,p.y+4*TS);')
rep('ctx.fillRect(b1[0]-11*TS,b1[1]-8*TS,22*TS,12*TS);ctx.font="bold "+(9*TS)+"px','ctx.fillRect(b1[0]-16*TS,b1[1]-12*TS,32*TS,17*TS);ctx.font="bold "+(13*TS)+"px')
rep('ctx.fillRect(b1[0]-10*TS,b1[1]-8*TS,20*TS,12*TS);ctx.font="bold "+(9*TS)+"px','ctx.fillRect(b1[0]-16*TS,b1[1]-12*TS,32*TS,17*TS);ctx.font="bold "+(13*TS)+"px')
rep('var zq=zAt(Q.x,Q.y),b0=pr(wx(Q.x),zq,wz(Q.y),[0,0]),b1=pr(wx(Q.x),zq+14,wz(Q.y),[0,0]);','var zq=zAt(Q.x,Q.y),b0=pr(wx(Q.x),zq,wz(Q.y),[0,0]),b1=pr(wx(Q.x),zq+20,wz(Q.y),[0,0]);')
rep('rr=k%2?3.4:8;','rr=k%2?5:12;')
rep('text("PRESENT",wx(START.x),zAt(START.x,START.y)+23,wz(START.y),{size:10});','text("PRESENT",wx(START.x),zAt(START.x,START.y)+23,wz(START.y),{size:14});')
rep('text("GOAL",wx(GOAL.x),zAt(GOAL.x,GOAL.y)+16,wz(GOAL.y),{size:10});','text("GOAL",wx(GOAL.x),zAt(GOAL.x,GOAL.y)+18,wz(GOAL.y),{size:14});')
rep('ctx.arc(b1[0],b1[1],on?11:9,0,6.283);','ctx.arc(b1[0],b1[1],(on?16:14)*TS,0,6.283);')
rep('ctx.font="bold "+(on?12:11)+"px Questrial,sans-serif";ctx.textAlign="center";ctx.fillStyle="#fff";ctx.fillText(String(i+1),b1[0],b1[1]+4);',
    'ctx.font="bold "+((on?17:16)*TS)+"px Questrial,sans-serif";ctx.textAlign="center";ctx.fillStyle="#fff";ctx.fillText(String(i+1),b1[0],b1[1]+6*TS);')
rep('ctx.arc(b1[0],b1[1],10*TS,0,6.283);ctx.fillStyle=RCOL[R.key]||"#111";ctx.fill();ctx.strokeStyle="#fff";ctx.lineWidth=2.4;ctx.stroke();ctx.font="bold "+(12*TS)+"px Questrial,sans-serif";ctx.textAlign="center";ctx.fillStyle="#fff";',
    'ctx.arc(b1[0],b1[1],13*TS,0,6.283);ctx.fillStyle=RCOL[R.key]||"#111";ctx.fill();ctx.strokeStyle=R.key==="B"?"#111":"#fff";ctx.lineWidth=2.4;ctx.stroke();ctx.font="bold "+(15*TS)+"px Questrial,sans-serif";ctx.textAlign="center";ctx.fillStyle=R.key==="B"?"#111":"#fff";')
rep('RCOL={A:"#111111",B:"#0a4fff",C:"#e0007a"}','RCOL={A:"#111111",B:"#ffffff",C:"#e0007a"}')
rep('stroke(o,"rgba(255,255,255,.95)",5.6*TL);','stroke(o,R.key==="B"?"#111":"rgba(255,255,255,.95)",(R.key==="B"?6.4:5.6)*TL);')
rep('n.style.background=r.k?(RCOL[r.k]||"#111"):"#7a1d12";n.style.color="#fff";n.style.border="2px solid #fff";n.style.boxShadow="0 0 0 1px "+(r.k?(RCOL[r.k]||"#111"):"#7a1d12");',
    'n.style.background=r.k?(RCOL[r.k]||"#111"):"#7a1d12";n.style.color=r.k==="B"?"#111":"#fff";n.style.border="2px solid "+(r.k==="B"?"#111":"#fff");n.style.boxShadow="0 0 0 1px "+(r.k?(r.k==="B"?"#111":RCOL[r.k]||"#111"):"#7a1d12");')
rep("background:rgb('+boost(e[1][0],e[1][1],e[1][2]).map(function(v){return v|0;}).join(\",\")+')","background:rgb('+_viv(e[1]).map(function(v){return v|0;}).join(\",\")+')")
rep('"Broken ground (talus): emotions meet");','"Bare rock face: two distant emotions meet with no ridge of indifference between them, so getting across is a climb. A big move takes energy either way; most moves go through indifference.");')
rep('<rect x="1" y="2" width="28" height="10" rx="2" fill="rgb(238,235,227)" stroke="#bbb"/></svg>\',"Pale, level ground: no notes nearby");',
    '<rect x="1" y="2" width="28" height="10" rx="2" fill="rgb(116,122,74)" stroke="#bbb"/></svg>\',"Plain grass, soil or rock, no color: no notes nearby, so no information here");')
rep('<path d="M1 11 L4 6 L6 9 L9 3 L12 8 L14 5 L17 10 L20 4 L23 9 L26 6 L29 10" fill="none" stroke="#333" stroke-width="1.3"/>','<rect x="1" y="2" width="28" height="10" rx="2" fill="rgb(140,135,127)" stroke="#bbb"/>')
rep('stroke="#111" stroke-width="2.6" stroke-dasharray="\'+R.dash.join(" ")+\'"/></svg>\'',
    'stroke="#111" stroke-width="4.4"/><line x1="1" y1="7" x2="29" y2="7" stroke="\'+(RCOL[R.key]||"#111")+\'" stroke-width="2.6" stroke-dasharray="\'+R.dash.join(" ")+\'"/></svg>\'')
_T=json.loads(TPL)
_o='Colors blend where emotions meet, more so near the line between present and goal. Broken ground (talus) marks where emotions meet.'
assert _T.count(_o)==1
_T=_T.replace(_o,'Colors soften toward each other where emotions meet. Where two distant emotions meet with no ridge of indifference between them, the ground breaks to a bare rock face: getting across is a climb, and most moves go through indifference instead. Plain grass, soil or rock with no color means no notes nearby, so no information there.')
TPL=json.dumps(_T)
