  cellCol=new Array(NX*NY);
  /* cast shadows: walk toward the sun from each point */
  var nV=VX*VY,shd=new Float32Array(nV),Lh=Math.hypot(L[0],L[2]),sx0=L[0]/Lh,sz0=L[2]/Lh,rise=L[1]/Lh;
  for(var sj=0;sj<VY;sj++)for(var si=0;si<VX;si++){var z0=zArr[sj*VX+si],x0=si*CX,y0=sj*CY,lit=1;
    for(var dd=2;dd<140;dd+=2){var xx=x0+sx0*dd,yy=y0+sz0*dd;if(xx<0||yy<0||xx>W||yy>HH)break;if(zAt(xx,yy)>z0+rise*dd+0.6){lit=0;break;}}shd[sj*VX+si]=lit;}
  _blur(shd,VX,VY,2);
  /* emotion field from the notes: the nearest strong emotion wins; a rock face where distant emotions meet */
  var EP=T.pts||[],R2=2*26*26,RANK=[3,0,2,1,4],VC=EMO.map(function(e){return _viv(e[1]);}),eC=new Float32Array(nV*3),eS=new Float32Array(nV),eG=new Float32Array(nV),ws=[0,0,0,0,0];
  for(var q=0;q<nV;q++){var qx=(q%VX)*CX,qy=((q/VX)|0)*CY;ws[0]=ws[1]=ws[2]=ws[3]=ws[4]=0;
    for(var pi=0;pi<EP.length;pi++){var ex=EP[pi].x-qx,ey=EP[pi].y-qy,e2=ex*ex+ey*ey;if(e2<10816)ws[EP[pi].e]+=Math.exp(-e2/R2);}
    if(T.bench)ws[3]+=T.bench[q];
    var tot=ws[0]+ws[1]+ws[2]+ws[3]+ws[4],pw=0,cr=0,cg=0,cb=0;
    for(var k=0;k<5;k++){var v=Math.pow(ws[k]*(k===4?1.6:1),2.2);pw+=v;cr+=VC[k][0]*v;cg+=VC[k][1]*v;cb+=VC[k][2]*v;}
    if(pw>0){eC[q*3]=cr/pw;eC[q*3+1]=cg/pw;eC[q*3+2]=cb/pw;}
    eS[q]=_ss(0.04,0.5,tot);
    var k1=0,k2=-1;for(var k3=1;k3<5;k3++)if(ws[k3]>ws[k1])k1=k3;for(var k4=0;k4<5;k4++)if(k4!==k1&&(k2<0||ws[k4]>ws[k2]))k2=k4;
    eG[q]=(Math.abs(RANK[k1]-RANK[k2])<2||RANK[k1]===1||RANK[k2]===1||ws[k2]<0.03)?0:_ss(0.22,0.42,ws[k2]/(ws[k1]+ws[k2]));}
  var GR=[98,108,62],GR2=[140,134,86],SO=[124,96,66],SO2=[86,68,50],RK=[122,118,112],RK2=[168,160,148];
  for(var j=0;j<NY;j++)for(var i=0;i<NX;i++){
    var a=j*VX+i,b=a+1,c=a+VX,d=c+1;
    var dzx=(zArr[b]+zArr[d]-zArr[a]-zArr[c])/(2*CX),dzz=(zArr[c]+zArr[d]-zArr[a]-zArr[b])/(2*CY);
    var lam=lamB[j*NX+i],hh=(T.hn[a]+T.hn[b]+T.hn[c]+T.hn[d])/4,sl=Math.hypot(dzx,dzz)*58/A,sd=(shd[a]+shd[b]+shd[c]+shd[d])/4;
    if(clay){var cv0=(250*(0.72+0.36*lam)*(0.8+0.2*sd))|0;cellCol[j*NX+i]="rgb("+Math.min(255,cv0)+","+Math.min(255,(cv0*0.985)|0)+","+Math.min(255,(cv0*0.96)|0)+")";continue;}
    var n1=vnoise(i*0.11+3.1,j*0.11+7.7),n2=vnoise(i*1.2,j*1.2),sp=hash2(i*7+3,j*13+5);
    var grass=_mx(GR,GR2,_ss(0.35,0.75,vnoise(i*0.07+9,j*0.07))),soil=_mx(SO,SO2,_ss(-0.2,-0.9,hh)*0.8),rock=_mx(RK,RK2,n2*0.7);
    var tR=_ss(0.55,1.15,sl+(n1-0.5)*0.5),tS=_ss(0.25,0.55,sl+(n1-0.5)*0.6)*(1-tR);
    var col=_mx(_mx(grass,soil,Math.min(1,tS+_ss(-0.4,-1.0,hh)*0.5*(1-tR))),rock,tR),kk=0.94+0.12*sp;col=[col[0]*kk,col[1]*kk,col[2]*kk];
    var gap=(eG[a]+eG[b]+eG[c]+eG[d])/4,st0=(eS[a]+eS[b]+eS[c]+eS[d])/4;
    if(gap>0.01)col=_mx(col,rock,gap*0.85);
    var em=[0,1,2].map(function(z){return (eC[a*3+z]+eC[b*3+z]+eC[c*3+z]+eC[d*3+z])/4;}),ls=_lum(col),le=_lum(em)||1;
    col=_mx(col,[Math.min(255,em[0]*ls/le*1.05),Math.min(255,em[1]*ls/le*1.05),Math.min(255,em[2]*ls/le*1.05)],0.6*st0*(1-gap));
    var sh=(0.58+0.62*lam)*(0.7+0.3*sd)*1.06;
    cellCol[j*NX+i]="rgb("+Math.min(255,col[0]*sh|0)+","+Math.min(255,col[1]*sh|0)+","+Math.min(255,col[2]*sh|0)+")";
  }
}
function _zmin(){var m=1e9;for(var q=0;q<zArr.length;q++)if(zArr[q]<m)m=zArr[q];return m;}
function _ss(a,b,x){var t=Math.min(1,Math.max(0,(x-a)/(b-a)));return t*t*(3-2*t);}
function _mx(a,b,t){return [a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t,a[2]+(b[2]-a[2])*t];}
function _lum(q){return 0.3*q[0]+0.59*q[1]+0.11*q[2];}
function _blur(arr,w,h,k){for(var p=0;p<k;p++){var c=new Float32Array(arr);for(var y=1;y<h-1;y++)for(var x=1;x<w-1;x++){var i=y*w+x;arr[i]=(c[i]*4+c[i-1]+c[i+1]+c[i-w]+c[i+w])/8;}}}
function _viv(c){var r=c[0]/255,g=c[1]/255,b=c[2]/255,mx=Math.max(r,g,b),mn=Math.min(r,g,b),l=(mx+mn)/2,sa=0,h=0,d=mx-mn;
  if(d>1e-6){sa=l>0.5?d/(2-mx-mn):d/(mx+mn);h=mx===r?(g-b)/d+(g<b?6:0):mx===g?(b-r)/d+2:(r-g)/d+4;h/=6;}
  sa=Math.min(1,sa*1.5+0.08);l=Math.min(0.62,Math.max(0.42,l));var q=l<0.5?l*(1+sa):l+sa-l*sa,p=2*l-q;
  function f(t){t=(t+1)%1;return t<1/6?p+(q-p)*6*t:t<0.5?q:t<2/3?p+(q-p)*(2/3-t)*6:p;}return [f(h+1/3)*255,f(h)*255,f(h-1/3)*255];}
