(()=>{var Xo="187",ms={LEFT:0,MIDDLE:1,RIGHT:2,ROTATE:0,DOLLY:1,PAN:2},gs={ROTATE:0,PAN:1,DOLLY_PAN:2,DOLLY_ROTATE:3},Ru=0,Uc=1,Cu=2;var Cs=1,qo=2,gr=3,_s=0,vn=1,zn=2,Ps=0,_r=1,Fc=2,Oc=3,Bc=4,Pu=5;var Is=100,Iu=101,Lu=102,Nu=103,Du=104,Uu=200,Fu=201,Ou=202,Bu=203,kc=204,zc=205,ku=206,zu=207,Hu=208,Gu=209,Vu=210,Wu=211,Xu=212,qu=213,Yu=214,ro=0,ao=1,oo=2,ir=3,lo=4,co=5,ho=6,uo=7,Hc=0,Zu=1,Ju=2,Ci=0,Gc=1,Vc=2,Wc=3,ca=4,Xc=5,qc=6,Yc=7;var Zc=300,Ls=301,xr=302,Yo=303,Zo=304,fo=1e3,Ei=1001,po=1002,cn=1003,Ku=1004;var ha=1005;var Ln=1006,Jo=1007;var qi=1008;var Hn=1009,Jc=1010,Kc=1011,yr=1012,Ko=1013,gi=1014,_i=1015,xi=1016,$o=1017,jo=1018,Ns=1020,$c=35902,jc=35899,Qc=1021,th=1022,yi=1023,zi=1026,Yi=1027,eh=1028,Qo=1029,xs=1030,tl=1031;var el=1033,ua=33776,da=33777,fa=33778,pa=33779,nl=35840,il=35841,sl=35842,rl=35843,al=36196,ol=37492,ll=37496,cl=37488,hl=37489,ma=37490,ul=37491,dl=37808,fl=37809,pl=37810,ml=37811,gl=37812,_l=37813,xl=37814,yl=37815,vl=37816,Ml=37817,Sl=37818,bl=37819,El=37820,Tl=37821,wl=36492,Al=36494,Rl=36495,Cl=36283,Pl=36284,ga=36285,Il=36286;var Wr=2300,mo=2301,io=2302,Ac=2303,Rc=2400,Cc=2401,Pc=2402;var $u=3200;var Ll=0,ju=1,Zi="",fn="srgb",Xr="srgb-linear",qr="linear",De="srgb";var so=7680;var Qu=519,td=512,ed=513,nd=514,nh=515,id=516,sd=517,ih=518,sh=519,rd=35044;var rh="300 es",ni=2e3,sr=2001;function Sf(i){for(let t=i.length-1;t>=0;--t)if(i[t]>=65535)return!0;return!1}function bf(i){return ArrayBuffer.isView(i)&&!(i instanceof DataView)}function Yr(i){return document.createElementNS("http://www.w3.org/1999/xhtml",i)}function ad(){let i=Yr("canvas");return i.style.display="block",i}var $h={},rr=null;function ah(...i){let t="THREE."+i.shift();rr?rr("log",t,...i):console.log(t,...i)}function od(i){let t=i[0];if(typeof t=="string"&&t.startsWith("TSL:")){let e=i[1];e&&e.isStackTrace?i[0]+=" "+e.getLocation():i[1]='Stack trace not available. Enable "THREE.Node.captureStackTrace" to capture stack traces.'}return i}function Kt(...i){i=od(i);let t="THREE."+i.shift();if(rr)rr("warn",t,...i);else{let e=i[0];e&&e.isStackTrace?console.warn(e.getError(t)):console.warn(t,...i)}}function ie(...i){i=od(i);let t="THREE."+i.shift();if(rr)rr("error",t,...i);else{let e=i[0];e&&e.isStackTrace?console.error(e.getError(t)):console.error(t,...i)}}function kr(...i){let t=i.join(" ");t in $h||($h[t]=!0,Kt(...i))}function ld(i,t,e){return new Promise(function(n,s){function r(){switch(i.clientWaitSync(t,i.SYNC_FLUSH_COMMANDS_BIT,0)){case i.WAIT_FAILED:s();break;case i.TIMEOUT_EXPIRED:setTimeout(r,e);break;default:n()}}setTimeout(r,e)})}var cd={[ro]:ro,[oo]:ho,[lo]:lo,[ir]:co,[ao]:ao,[ho]:oo,[uo]:uo,[co]:ir},pi=class{addEventListener(t,e){this._listeners===void 0&&(this._listeners={});let n=this._listeners;n[t]===void 0&&(n[t]=[]),n[t].indexOf(e)===-1&&n[t].push(e)}hasEventListener(t,e){let n=this._listeners;return n===void 0?!1:n[t]!==void 0&&n[t].indexOf(e)!==-1}removeEventListener(t,e){let n=this._listeners;if(n===void 0)return;let s=n[t];if(s!==void 0){let r=s.indexOf(e);r!==-1&&s.splice(r,1)}}dispatchEvent(t){let e=this._listeners;if(e===void 0)return;let n=e[t.type];if(n!==void 0){t.target=this;let s=n.slice(0);for(let r=0,a=s.length;r<a;r++)s[r].call(this,t);t.target=null}}},An=["00","01","02","03","04","05","06","07","08","09","0a","0b","0c","0d","0e","0f","10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","40","41","42","43","44","45","46","47","48","49","4a","4b","4c","4d","4e","4f","50","51","52","53","54","55","56","57","58","59","5a","5b","5c","5d","5e","5f","60","61","62","63","64","65","66","67","68","69","6a","6b","6c","6d","6e","6f","70","71","72","73","74","75","76","77","78","79","7a","7b","7c","7d","7e","7f","80","81","82","83","84","85","86","87","88","89","8a","8b","8c","8d","8e","8f","90","91","92","93","94","95","96","97","98","99","9a","9b","9c","9d","9e","9f","a0","a1","a2","a3","a4","a5","a6","a7","a8","a9","aa","ab","ac","ad","ae","af","b0","b1","b2","b3","b4","b5","b6","b7","b8","b9","ba","bb","bc","bd","be","bf","c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","ca","cb","cc","cd","ce","cf","d0","d1","d2","d3","d4","d5","d6","d7","d8","d9","da","db","dc","dd","de","df","e0","e1","e2","e3","e4","e5","e6","e7","e8","e9","ea","eb","ec","ed","ee","ef","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","fa","fb","fc","fd","fe","ff"],jh=1234567,zr=Math.PI/180,ar=180/Math.PI;function vr(){let i=Math.random()*4294967295|0,t=Math.random()*4294967295|0,e=Math.random()*4294967295|0,n=Math.random()*4294967295|0;return(An[i&255]+An[i>>8&255]+An[i>>16&255]+An[i>>24&255]+"-"+An[t&255]+An[t>>8&255]+"-"+An[t>>16&15|64]+An[t>>24&255]+"-"+An[e&63|128]+An[e>>8&255]+"-"+An[e>>16&255]+An[e>>24&255]+An[n&255]+An[n>>8&255]+An[n>>16&255]+An[n>>24&255]).toLowerCase()}function ge(i,t,e){return Math.max(t,Math.min(e,i))}function oh(i,t){return(i%t+t)%t}function Ef(i,t,e,n,s){return n+(i-t)*(s-n)/(e-t)}function Tf(i,t,e){return i!==t?(e-i)/(t-i):0}function Hr(i,t,e){return(1-e)*i+e*t}function wf(i,t,e,n){return Hr(i,t,1-Math.exp(-e*n))}function Af(i,t=1){return t-Math.abs(oh(i,t*2)-t)}function Rf(i,t,e){return i<=t?0:i>=e?1:(i=(i-t)/(e-t),i*i*(3-2*i))}function Cf(i,t,e){return i<=t?0:i>=e?1:(i=(i-t)/(e-t),i*i*i*(i*(i*6-15)+10))}function Pf(i,t){return i+Math.floor(Math.random()*(t-i+1))}function If(i,t){return i+Math.random()*(t-i)}function Lf(i){return i*(.5-Math.random())}function Nf(i){i!==void 0&&(jh=i);let t=jh+=1831565813;return t=Math.imul(t^t>>>15,t|1),t^=t+Math.imul(t^t>>>7,t|61),((t^t>>>14)>>>0)/4294967296}function Df(i){return i*zr}function Uf(i){return i*ar}function Ff(i){return i>0&&Number.isInteger(i)&&2**Math.round(Math.log2(i))===i}function Of(i){return Math.pow(2,Math.ceil(Math.log(i)/Math.LN2))}function lh(i){return Math.pow(2,Math.floor(Math.log(i)/Math.LN2))}function Bf(i,t,e,n,s){let r=Math.cos,a=Math.sin,o=r(e/2),l=a(e/2),c=r((t+n)/2),h=a((t+n)/2),f=r((t-n)/2),d=a((t-n)/2),p=r((n-t)/2),x=a((n-t)/2);switch(s){case"XYX":i.set(o*h,l*f,l*d,o*c);break;case"YZY":i.set(l*d,o*h,l*f,o*c);break;case"ZXZ":i.set(l*f,l*d,o*h,o*c);break;case"XZX":i.set(o*h,l*x,l*p,o*c);break;case"YXY":i.set(l*p,o*h,l*x,o*c);break;case"ZYZ":i.set(l*x,l*p,o*h,o*c);break;default:Kt("MathUtils: .setQuaternionFromProperEuler() encountered an unknown order: "+s)}}function ch(i){switch(i.constructor){case Uint32Array:return 4294967295;case Uint16Array:return 65535;case Uint8Array:case Uint8ClampedArray:return 255;case Int32Array:return 2147483647;case Int16Array:return 32767;case Int8Array:return 127;default:return}}function hd(i,t){if(t.constructor===Float32Array)return i;let e=ch(t);if(e===void 0)throw new Error("THREE.MathUtils: Invalid component type.");return Math.max(i/e,-1)}function ud(i,t){if(t.constructor===Float32Array)return i;let e=ch(t);if(e===void 0)throw new Error("THREE.MathUtils: Invalid component type.");return Math.round(i*e)}var hh={DEG2RAD:zr,RAD2DEG:ar,generateUUID:vr,clamp:ge,euclideanModulo:oh,mapLinear:Ef,inverseLerp:Tf,lerp:Hr,damp:wf,pingpong:Af,smoothstep:Rf,smootherstep:Cf,randInt:Pf,randFloat:If,randFloatSpread:Lf,seededRandom:Nf,degToRad:Df,radToDeg:Uf,isPowerOfTwo:Ff,ceilPowerOfTwo:Of,floorPowerOfTwo:lh,setQuaternionFromProperEuler:Bf,normalize:ud,denormalize:hd},kt=class{static{this.prototype.isVector2=!0}constructor(t=0,e=0){this.x=t,this.y=e}get width(){return this.x}set width(t){this.x=t}get height(){return this.y}set height(t){this.y=t}set(t,e){return this.x=t,this.y=e,this}setScalar(t){return this.x=t,this.y=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;default:throw new Error("THREE.Vector2: index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;default:throw new Error("THREE.Vector2: index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y)}copy(t){return this.x=t.x,this.y=t.y,this}add(t){return this.x+=t.x,this.y+=t.y,this}addScalar(t){return this.x+=t,this.y+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this}subScalar(t){return this.x-=t,this.y-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this}multiply(t){return this.x*=t.x,this.y*=t.y,this}multiplyScalar(t){return this.x*=t,this.y*=t,this}divide(t){return this.x/=t.x,this.y/=t.y,this}divideScalar(t){return this.multiplyScalar(1/t)}applyMatrix3(t){let e=this.x,n=this.y,s=t.elements;return this.x=s[0]*e+s[3]*n+s[6],this.y=s[1]*e+s[4]*n+s[7],this}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this}clamp(t,e){return this.x=ge(this.x,t.x,e.x),this.y=ge(this.y,t.y,e.y),this}clampScalar(t,e){return this.x=ge(this.x,t,e),this.y=ge(this.y,t,e),this}clampLength(t,e){let n=this.length();return this.divideScalar(n||1).multiplyScalar(ge(n,t,e))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this}negate(){return this.x=-this.x,this.y=-this.y,this}dot(t){return this.x*t.x+this.y*t.y}cross(t){return this.x*t.y-this.y*t.x}lengthSq(){return this.x*this.x+this.y*this.y}length(){return Math.sqrt(this.x*this.x+this.y*this.y)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)}normalize(){return this.divideScalar(this.length()||1)}angle(){return Math.atan2(-this.y,-this.x)+Math.PI}angleTo(t){let e=Math.sqrt(this.lengthSq()*t.lengthSq());if(e===0)return Math.PI/2;let n=this.dot(t)/e;return Math.acos(ge(n,-1,1))}distanceTo(t){return Math.sqrt(this.distanceToSquared(t))}distanceToSquared(t){let e=this.x-t.x,n=this.y-t.y;return e*e+n*n}manhattanDistanceTo(t){return Math.abs(this.x-t.x)+Math.abs(this.y-t.y)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this}lerpVectors(t,e,n){return this.x=t.x+(e.x-t.x)*n,this.y=t.y+(e.y-t.y)*n,this}equals(t){return t.x===this.x&&t.y===this.y}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this}rotateAround(t,e){let n=Math.cos(e),s=Math.sin(e),r=this.x-t.x,a=this.y-t.y;return this.x=r*n-a*s+t.x,this.y=r*s+a*n+t.y,this}random(){return this.x=Math.random(),this.y=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y}},Nn=class{constructor(t=0,e=0,n=0,s=1){this.isQuaternion=!0,this._x=t,this._y=e,this._z=n,this._w=s}static slerpFlat(t,e,n,s,r,a,o){let l=n[s+0],c=n[s+1],h=n[s+2],f=n[s+3],d=r[a+0],p=r[a+1],x=r[a+2],S=r[a+3];if(f!==S||l!==d||c!==p||h!==x){let m=l*d+c*p+h*x+f*S;m<0&&(d=-d,p=-p,x=-x,S=-S,m=-m);let g=1-o;if(m<.9995){let E=Math.acos(m),P=Math.sin(E);g=Math.sin(g*E)/P,o=Math.sin(o*E)/P,l=l*g+d*o,c=c*g+p*o,h=h*g+x*o,f=f*g+S*o}else{l=l*g+d*o,c=c*g+p*o,h=h*g+x*o,f=f*g+S*o;let E=1/Math.sqrt(l*l+c*c+h*h+f*f);l*=E,c*=E,h*=E,f*=E}}t[e]=l,t[e+1]=c,t[e+2]=h,t[e+3]=f}static multiplyQuaternionsFlat(t,e,n,s,r,a){let o=n[s],l=n[s+1],c=n[s+2],h=n[s+3],f=r[a],d=r[a+1],p=r[a+2],x=r[a+3];return t[e]=o*x+h*f+l*p-c*d,t[e+1]=l*x+h*d+c*f-o*p,t[e+2]=c*x+h*p+o*d-l*f,t[e+3]=h*x-o*f-l*d-c*p,t}get x(){return this._x}set x(t){this._x=t,this._onChangeCallback()}get y(){return this._y}set y(t){this._y=t,this._onChangeCallback()}get z(){return this._z}set z(t){this._z=t,this._onChangeCallback()}get w(){return this._w}set w(t){this._w=t,this._onChangeCallback()}set(t,e,n,s){return this._x=t,this._y=e,this._z=n,this._w=s,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._w)}copy(t){return this._x=t.x,this._y=t.y,this._z=t.z,this._w=t.w,this._onChangeCallback(),this}setFromEuler(t,e=!0){let n=t._x,s=t._y,r=t._z,a=t._order,o=Math.cos,l=Math.sin,c=o(n/2),h=o(s/2),f=o(r/2),d=l(n/2),p=l(s/2),x=l(r/2);switch(a){case"XYZ":this._x=d*h*f+c*p*x,this._y=c*p*f-d*h*x,this._z=c*h*x+d*p*f,this._w=c*h*f-d*p*x;break;case"YXZ":this._x=d*h*f+c*p*x,this._y=c*p*f-d*h*x,this._z=c*h*x-d*p*f,this._w=c*h*f+d*p*x;break;case"ZXY":this._x=d*h*f-c*p*x,this._y=c*p*f+d*h*x,this._z=c*h*x+d*p*f,this._w=c*h*f-d*p*x;break;case"ZYX":this._x=d*h*f-c*p*x,this._y=c*p*f+d*h*x,this._z=c*h*x-d*p*f,this._w=c*h*f+d*p*x;break;case"YZX":this._x=d*h*f+c*p*x,this._y=c*p*f+d*h*x,this._z=c*h*x-d*p*f,this._w=c*h*f-d*p*x;break;case"XZY":this._x=d*h*f-c*p*x,this._y=c*p*f-d*h*x,this._z=c*h*x+d*p*f,this._w=c*h*f+d*p*x;break;default:Kt("Quaternion: .setFromEuler() encountered an unknown order: "+a)}return e===!0&&this._onChangeCallback(),this}setFromAxisAngle(t,e){let n=e/2,s=Math.sin(n);return this._x=t.x*s,this._y=t.y*s,this._z=t.z*s,this._w=Math.cos(n),this._onChangeCallback(),this}setFromRotationMatrix(t){let e=t.elements,n=e[0],s=e[4],r=e[8],a=e[1],o=e[5],l=e[9],c=e[2],h=e[6],f=e[10],d=n+o+f;if(d>0){let p=.5/Math.sqrt(d+1);this._w=.25/p,this._x=(h-l)*p,this._y=(r-c)*p,this._z=(a-s)*p}else if(n>o&&n>f){let p=2*Math.sqrt(1+n-o-f);this._w=(h-l)/p,this._x=.25*p,this._y=(s+a)/p,this._z=(r+c)/p}else if(o>f){let p=2*Math.sqrt(1+o-n-f);this._w=(r-c)/p,this._x=(s+a)/p,this._y=.25*p,this._z=(l+h)/p}else{let p=2*Math.sqrt(1+f-n-o);this._w=(a-s)/p,this._x=(r+c)/p,this._y=(l+h)/p,this._z=.25*p}return this._onChangeCallback(),this}setFromUnitVectors(t,e){let n=t.dot(e)+1;return n<1e-8?(n=0,Math.abs(t.x)>Math.abs(t.z)?(this._x=-t.y,this._y=t.x,this._z=0,this._w=n):(this._x=0,this._y=-t.z,this._z=t.y,this._w=n)):(this._x=t.y*e.z-t.z*e.y,this._y=t.z*e.x-t.x*e.z,this._z=t.x*e.y-t.y*e.x,this._w=n),this.normalize()}angleTo(t){return 2*Math.acos(Math.abs(ge(this.dot(t),-1,1)))}rotateTowards(t,e){let n=this.angleTo(t);if(n===0)return this;let s=Math.min(1,e/n);return this.slerp(t,s),this}identity(){return this.set(0,0,0,1)}invert(){return this.conjugate()}conjugate(){return this._x*=-1,this._y*=-1,this._z*=-1,this._onChangeCallback(),this}dot(t){return this._x*t._x+this._y*t._y+this._z*t._z+this._w*t._w}lengthSq(){return this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w}length(){return Math.sqrt(this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w)}normalize(){let t=this.length();return t===0?(this._x=0,this._y=0,this._z=0,this._w=1):(t=1/t,this._x=this._x*t,this._y=this._y*t,this._z=this._z*t,this._w=this._w*t),this._onChangeCallback(),this}multiply(t){return this.multiplyQuaternions(this,t)}premultiply(t){return this.multiplyQuaternions(t,this)}multiplyQuaternions(t,e){let n=t._x,s=t._y,r=t._z,a=t._w,o=e._x,l=e._y,c=e._z,h=e._w;return this._x=n*h+a*o+s*c-r*l,this._y=s*h+a*l+r*o-n*c,this._z=r*h+a*c+n*l-s*o,this._w=a*h-n*o-s*l-r*c,this._onChangeCallback(),this}slerp(t,e){let n=t._x,s=t._y,r=t._z,a=t._w,o=this.dot(t);o<0&&(n=-n,s=-s,r=-r,a=-a,o=-o);let l=1-e;if(o<.9995){let c=Math.acos(o),h=Math.sin(c);l=Math.sin(l*c)/h,e=Math.sin(e*c)/h,this._x=this._x*l+n*e,this._y=this._y*l+s*e,this._z=this._z*l+r*e,this._w=this._w*l+a*e,this._onChangeCallback()}else this._x=this._x*l+n*e,this._y=this._y*l+s*e,this._z=this._z*l+r*e,this._w=this._w*l+a*e,this.normalize();return this}slerpQuaternions(t,e,n){return this.copy(t).slerp(e,n)}random(){let t=2*Math.PI*Math.random(),e=2*Math.PI*Math.random(),n=Math.random(),s=Math.sqrt(1-n),r=Math.sqrt(n);return this.set(s*Math.sin(t),s*Math.cos(t),r*Math.sin(e),r*Math.cos(e))}equals(t){return t._x===this._x&&t._y===this._y&&t._z===this._z&&t._w===this._w}fromArray(t,e=0){return this._x=t[e],this._y=t[e+1],this._z=t[e+2],this._w=t[e+3],this._onChangeCallback(),this}toArray(t=[],e=0){return t[e]=this._x,t[e+1]=this._y,t[e+2]=this._z,t[e+3]=this._w,t}fromBufferAttribute(t,e){return this._x=t.getX(e),this._y=t.getY(e),this._z=t.getZ(e),this._w=t.getW(e),this._onChangeCallback(),this}toJSON(){return this.toArray()}_onChange(t){return this._onChangeCallback=t,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._w}},D=class{static{this.prototype.isVector3=!0}constructor(t=0,e=0,n=0){this.x=t,this.y=e,this.z=n}set(t,e,n){return n===void 0&&(n=this.z),this.x=t,this.y=e,this.z=n,this}setScalar(t){return this.x=t,this.y=t,this.z=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setZ(t){return this.z=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;case 2:this.z=e;break;default:throw new Error("THREE.Vector3: index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;case 2:return this.z;default:throw new Error("THREE.Vector3: index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y,this.z)}copy(t){return this.x=t.x,this.y=t.y,this.z=t.z,this}add(t){return this.x+=t.x,this.y+=t.y,this.z+=t.z,this}addScalar(t){return this.x+=t,this.y+=t,this.z+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this.z=t.z+e.z,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this.z+=t.z*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this.z-=t.z,this}subScalar(t){return this.x-=t,this.y-=t,this.z-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this.z=t.z-e.z,this}multiply(t){return this.x*=t.x,this.y*=t.y,this.z*=t.z,this}multiplyScalar(t){return this.x*=t,this.y*=t,this.z*=t,this}multiplyVectors(t,e){return this.x=t.x*e.x,this.y=t.y*e.y,this.z=t.z*e.z,this}applyEuler(t){return this.applyQuaternion(Qh.setFromEuler(t))}applyAxisAngle(t,e){return this.applyQuaternion(Qh.setFromAxisAngle(t,e))}applyMatrix3(t){let e=this.x,n=this.y,s=this.z,r=t.elements;return this.x=r[0]*e+r[3]*n+r[6]*s,this.y=r[1]*e+r[4]*n+r[7]*s,this.z=r[2]*e+r[5]*n+r[8]*s,this}applyNormalMatrix(t){return this.applyMatrix3(t).normalize()}applyMatrix4(t){let e=this.x,n=this.y,s=this.z,r=t.elements,a=1/(r[3]*e+r[7]*n+r[11]*s+r[15]);return this.x=(r[0]*e+r[4]*n+r[8]*s+r[12])*a,this.y=(r[1]*e+r[5]*n+r[9]*s+r[13])*a,this.z=(r[2]*e+r[6]*n+r[10]*s+r[14])*a,this}applyQuaternion(t){let e=this.x,n=this.y,s=this.z,r=t.x,a=t.y,o=t.z,l=t.w,c=2*(a*s-o*n),h=2*(o*e-r*s),f=2*(r*n-a*e);return this.x=e+l*c+a*f-o*h,this.y=n+l*h+o*c-r*f,this.z=s+l*f+r*h-a*c,this}project(t){return this.applyMatrix4(t.matrixWorldInverse).applyMatrix4(t.projectionMatrix)}unproject(t){return this.applyMatrix4(t.projectionMatrixInverse).applyMatrix4(t.matrixWorld)}transformDirection(t){let e=this.x,n=this.y,s=this.z,r=t.elements;return this.x=r[0]*e+r[4]*n+r[8]*s,this.y=r[1]*e+r[5]*n+r[9]*s,this.z=r[2]*e+r[6]*n+r[10]*s,this.normalize()}divide(t){return this.x/=t.x,this.y/=t.y,this.z/=t.z,this}divideScalar(t){return this.multiplyScalar(1/t)}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this.z=Math.min(this.z,t.z),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this.z=Math.max(this.z,t.z),this}clamp(t,e){return this.x=ge(this.x,t.x,e.x),this.y=ge(this.y,t.y,e.y),this.z=ge(this.z,t.z,e.z),this}clampScalar(t,e){return this.x=ge(this.x,t,e),this.y=ge(this.y,t,e),this.z=ge(this.z,t,e),this}clampLength(t,e){let n=this.length();return this.divideScalar(n||1).multiplyScalar(ge(n,t,e))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this}dot(t){return this.x*t.x+this.y*t.y+this.z*t.z}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)}normalize(){return this.divideScalar(this.length()||1)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this.z+=(t.z-this.z)*e,this}lerpVectors(t,e,n){return this.x=t.x+(e.x-t.x)*n,this.y=t.y+(e.y-t.y)*n,this.z=t.z+(e.z-t.z)*n,this}cross(t){return this.crossVectors(this,t)}crossVectors(t,e){let n=t.x,s=t.y,r=t.z,a=e.x,o=e.y,l=e.z;return this.x=s*l-r*o,this.y=r*a-n*l,this.z=n*o-s*a,this}projectOnVector(t){let e=t.lengthSq();if(e===0)return this.set(0,0,0);let n=t.dot(this)/e;return this.copy(t).multiplyScalar(n)}projectOnPlane(t){return ic.copy(this).projectOnVector(t),this.sub(ic)}reflect(t){return this.sub(ic.copy(t).multiplyScalar(2*this.dot(t)))}angleTo(t){let e=Math.sqrt(this.lengthSq()*t.lengthSq());if(e===0)return Math.PI/2;let n=this.dot(t)/e;return Math.acos(ge(n,-1,1))}distanceTo(t){return Math.sqrt(this.distanceToSquared(t))}distanceToSquared(t){let e=this.x-t.x,n=this.y-t.y,s=this.z-t.z;return e*e+n*n+s*s}manhattanDistanceTo(t){return Math.abs(this.x-t.x)+Math.abs(this.y-t.y)+Math.abs(this.z-t.z)}setFromSpherical(t){return this.setFromSphericalCoords(t.radius,t.phi,t.theta)}setFromSphericalCoords(t,e,n){let s=Math.sin(e)*t;return this.x=s*Math.sin(n),this.y=Math.cos(e)*t,this.z=s*Math.cos(n),this}setFromCylindrical(t){return this.setFromCylindricalCoords(t.radius,t.theta,t.y)}setFromCylindricalCoords(t,e,n){return this.x=t*Math.sin(e),this.y=n,this.z=t*Math.cos(e),this}setFromMatrixPosition(t){let e=t.elements;return this.x=e[12],this.y=e[13],this.z=e[14],this}setFromMatrixScale(t){let e=this.setFromMatrixColumn(t,0).length(),n=this.setFromMatrixColumn(t,1).length(),s=this.setFromMatrixColumn(t,2).length();return this.x=e,this.y=n,this.z=s,this}setFromMatrixColumn(t,e){return this.fromArray(t.elements,e*4)}setFromMatrix3Column(t,e){return this.fromArray(t.elements,e*3)}setFromEuler(t){return this.x=t._x,this.y=t._y,this.z=t._z,this}setFromColor(t){return this.x=t.r,this.y=t.g,this.z=t.b,this}equals(t){return t.x===this.x&&t.y===this.y&&t.z===this.z}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this.z=t[e+2],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t[e+2]=this.z,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this.z=t.getZ(e),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this}randomDirection(){let t=Math.random()*Math.PI*2,e=Math.random()*2-1,n=Math.sqrt(1-e*e);return this.x=n*Math.cos(t),this.y=e,this.z=n*Math.sin(t),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z}},ic=new D,Qh=new Nn,ae=class{static{this.prototype.isMatrix3=!0}constructor(t,e,n,s,r,a,o,l,c){this.elements=[1,0,0,0,1,0,0,0,1],t!==void 0&&this.set(t,e,n,s,r,a,o,l,c)}set(t,e,n,s,r,a,o,l,c){let h=this.elements;return h[0]=t,h[1]=s,h[2]=o,h[3]=e,h[4]=r,h[5]=l,h[6]=n,h[7]=a,h[8]=c,this}identity(){return this.set(1,0,0,0,1,0,0,0,1),this}copy(t){let e=this.elements,n=t.elements;return e[0]=n[0],e[1]=n[1],e[2]=n[2],e[3]=n[3],e[4]=n[4],e[5]=n[5],e[6]=n[6],e[7]=n[7],e[8]=n[8],this}extractBasis(t,e,n){return t.setFromMatrix3Column(this,0),e.setFromMatrix3Column(this,1),n.setFromMatrix3Column(this,2),this}setFromMatrix4(t){let e=t.elements;return this.set(e[0],e[4],e[8],e[1],e[5],e[9],e[2],e[6],e[10]),this}multiply(t){return this.multiplyMatrices(this,t)}premultiply(t){return this.multiplyMatrices(t,this)}multiplyMatrices(t,e){let n=t.elements,s=e.elements,r=this.elements,a=n[0],o=n[3],l=n[6],c=n[1],h=n[4],f=n[7],d=n[2],p=n[5],x=n[8],S=s[0],m=s[3],g=s[6],E=s[1],P=s[4],T=s[7],C=s[2],A=s[5],_=s[8];return r[0]=a*S+o*E+l*C,r[3]=a*m+o*P+l*A,r[6]=a*g+o*T+l*_,r[1]=c*S+h*E+f*C,r[4]=c*m+h*P+f*A,r[7]=c*g+h*T+f*_,r[2]=d*S+p*E+x*C,r[5]=d*m+p*P+x*A,r[8]=d*g+p*T+x*_,this}multiplyScalar(t){let e=this.elements;return e[0]*=t,e[3]*=t,e[6]*=t,e[1]*=t,e[4]*=t,e[7]*=t,e[2]*=t,e[5]*=t,e[8]*=t,this}determinant(){let t=this.elements,e=t[0],n=t[1],s=t[2],r=t[3],a=t[4],o=t[5],l=t[6],c=t[7],h=t[8];return e*a*h-e*o*c-n*r*h+n*o*l+s*r*c-s*a*l}invert(){let t=this.elements,e=t[0],n=t[1],s=t[2],r=t[3],a=t[4],o=t[5],l=t[6],c=t[7],h=t[8],f=h*a-o*c,d=o*l-h*r,p=c*r-a*l,x=e*f+n*d+s*p;if(x===0)return this.set(0,0,0,0,0,0,0,0,0);let S=1/x;return t[0]=f*S,t[1]=(s*c-h*n)*S,t[2]=(o*n-s*a)*S,t[3]=d*S,t[4]=(h*e-s*l)*S,t[5]=(s*r-o*e)*S,t[6]=p*S,t[7]=(n*l-c*e)*S,t[8]=(a*e-n*r)*S,this}transpose(){let t,e=this.elements;return t=e[1],e[1]=e[3],e[3]=t,t=e[2],e[2]=e[6],e[6]=t,t=e[5],e[5]=e[7],e[7]=t,this}getNormalMatrix(t){return this.setFromMatrix4(t).invert().transpose()}transposeIntoArray(t){let e=this.elements;return t[0]=e[0],t[1]=e[3],t[2]=e[6],t[3]=e[1],t[4]=e[4],t[5]=e[7],t[6]=e[2],t[7]=e[5],t[8]=e[8],this}setUvTransform(t,e,n,s,r,a,o){let l=Math.cos(r),c=Math.sin(r);return this.set(n*l,n*c,-n*(l*a+c*o)+a+t,-s*c,s*l,-s*(-c*a+l*o)+o+e,0,0,1),this}scale(t,e){return kr("Matrix3: .scale() is deprecated. Use .makeScale() instead."),this.premultiply(sc.makeScale(t,e)),this}rotate(t){return kr("Matrix3: .rotate() is deprecated. Use .makeRotation() instead."),this.premultiply(sc.makeRotation(-t)),this}translate(t,e){return kr("Matrix3: .translate() is deprecated. Use .makeTranslation() instead."),this.premultiply(sc.makeTranslation(t,e)),this}makeTranslation(t,e){return t.isVector2?this.set(1,0,t.x,0,1,t.y,0,0,1):this.set(1,0,t,0,1,e,0,0,1),this}makeRotation(t){let e=Math.cos(t),n=Math.sin(t);return this.set(e,-n,0,n,e,0,0,0,1),this}makeScale(t,e){return this.set(t,0,0,0,e,0,0,0,1),this}equals(t){let e=this.elements,n=t.elements;for(let s=0;s<9;s++)if(e[s]!==n[s])return!1;return!0}fromArray(t,e=0){for(let n=0;n<9;n++)this.elements[n]=t[n+e];return this}toArray(t=[],e=0){let n=this.elements;return t[e]=n[0],t[e+1]=n[1],t[e+2]=n[2],t[e+3]=n[3],t[e+4]=n[4],t[e+5]=n[5],t[e+6]=n[6],t[e+7]=n[7],t[e+8]=n[8],t}clone(){return new this.constructor().fromArray(this.elements)}},sc=new ae,tu=new ae().set(.4123908,.3575843,.1804808,.212639,.7151687,.0721923,.0193308,.1191948,.9505322),eu=new ae().set(3.2409699,-1.5373832,-.4986108,-.9692436,1.8759675,.0415551,.0556301,-.203977,1.0569715);function kf(){let i={enabled:!0,workingColorSpace:Xr,spaces:{},convert:function(s,r,a){return this.enabled===!1||r===a||!r||!a||(this.spaces[r].transfer===De&&(s.r=ki(s.r),s.g=ki(s.g),s.b=ki(s.b)),this.spaces[r].primaries!==this.spaces[a].primaries&&(s.applyMatrix3(this.spaces[r].toXYZ),s.applyMatrix3(this.spaces[a].fromXYZ)),this.spaces[a].transfer===De&&(s.r=nr(s.r),s.g=nr(s.g),s.b=nr(s.b))),s},workingToColorSpace:function(s,r){return this.convert(s,this.workingColorSpace,r)},colorSpaceToWorking:function(s,r){return this.convert(s,r,this.workingColorSpace)},getPrimaries:function(s){return this.spaces[s].primaries},getTransfer:function(s){return s===Zi?qr:this.spaces[s].transfer},getToneMappingMode:function(s){return this.spaces[s].outputColorSpaceConfig.toneMappingMode||"standard"},getLuminanceCoefficients:function(s,r=this.workingColorSpace){return s.fromArray(this.spaces[r].luminanceCoefficients)},define:function(s){Object.assign(this.spaces,s)},_getMatrix:function(s,r,a){return s.copy(this.spaces[a].fromXYZ).multiply(this.spaces[r].toXYZ)},_getDrawingBufferColorSpace:function(s){return this.spaces[s].outputColorSpaceConfig.drawingBufferColorSpace},_getUnpackColorSpace:function(s=this.workingColorSpace){return this.spaces[s].workingColorSpaceConfig.unpackColorSpace}},t=[.64,.33,.3,.6,.15,.06],e=[.2126,.7152,.0722],n=[.3127,.329];return i.define({[Xr]:{primaries:t,whitePoint:n,transfer:qr,toXYZ:tu,fromXYZ:eu,luminanceCoefficients:e,workingColorSpaceConfig:{unpackColorSpace:fn},outputColorSpaceConfig:{drawingBufferColorSpace:fn}},[fn]:{primaries:t,whitePoint:n,transfer:De,toXYZ:tu,fromXYZ:eu,luminanceCoefficients:e,outputColorSpaceConfig:{drawingBufferColorSpace:fn}}}),i}var be=kf();function ki(i){return i<.04045?i*.0773993808:Math.pow(i*.9478672986+.0521327014,2.4)}function nr(i){return i<.0031308?i*12.92:1.055*Math.pow(i,.41666)-.055}var Vs,go=class{static getDataURL(t,e="image/png"){if(/^data:/i.test(t.src)||typeof HTMLCanvasElement>"u")return t.src;let n;if(t instanceof HTMLCanvasElement)n=t;else{Vs===void 0&&(Vs=Yr("canvas")),Vs.width=t.width,Vs.height=t.height;let s=Vs.getContext("2d");t instanceof ImageData?s.putImageData(t,0,0):s.drawImage(t,0,0,t.width,t.height),n=Vs}return n.toDataURL(e)}static sRGBToLinear(t){if(typeof HTMLImageElement<"u"&&t instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&t instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&t instanceof ImageBitmap){let e=Yr("canvas");e.width=t.width,e.height=t.height;let n=e.getContext("2d");n.drawImage(t,0,0,t.width,t.height);let s=n.getImageData(0,0,t.width,t.height),r=s.data;for(let a=0;a<r.length;a++)r[a]=ki(r[a]/255)*255;return n.putImageData(s,0,0),e}else if(t.data){let e=t.data.slice(0);for(let n=0;n<e.length;n++)e instanceof Uint8Array||e instanceof Uint8ClampedArray?e[n]=Math.floor(ki(e[n]/255)*255):e[n]=ki(e[n]);return{data:e,width:t.width,height:t.height}}else return Kt("ImageUtils.sRGBToLinear(): Unsupported image type. No color space conversion applied."),t}},zf=0,or=class{constructor(t=null){this.isTextureSource=!0,Object.defineProperty(this,"id",{value:zf++}),this.uuid=vr(),this.data=t,this.dataReady=!0,this.version=0}getSize(t){let e=this.data;return typeof HTMLVideoElement<"u"&&e instanceof HTMLVideoElement?t.set(e.videoWidth,e.videoHeight,0):typeof VideoFrame<"u"&&e instanceof VideoFrame?t.set(e.displayWidth,e.displayHeight,0):e!==null?t.set(e.width||0,e.height||0,e.depth||0):t.set(0,0,0),t}set needsUpdate(t){t===!0&&this.version++}toJSON(t){let e=t===void 0||typeof t=="string";if(!e&&t.images[this.uuid]!==void 0)return t.images[this.uuid];let n={uuid:this.uuid,url:""},s=this.data;if(s!==null){let r;if(Array.isArray(s)){r=[];for(let a=0,o=s.length;a<o;a++)s[a].isDataTexture?r.push(rc(s[a].image)):r.push(rc(s[a]))}else r=rc(s);n.url=r}return e||(t.images[this.uuid]=n),n}};function rc(i){return typeof HTMLImageElement<"u"&&i instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&i instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&i instanceof ImageBitmap?go.getDataURL(i):i.data?{data:Array.from(i.data),width:i.width,height:i.height,type:i.data.constructor.name}:(Kt("Texture: Unable to serialize Texture."),{})}var Hf=0,ac=new D,Dn=class i extends pi{constructor(t=i.DEFAULT_IMAGE,e=i.DEFAULT_MAPPING,n=Ei,s=Ei,r=Ln,a=qi,o=yi,l=Hn,c=i.DEFAULT_ANISOTROPY,h=Zi){super(),this.isTexture=!0,Object.defineProperty(this,"id",{value:Hf++}),this.uuid=vr(),this.name="",this.source=new or(t),this.mipmaps=[],this.mapping=e,this.channel=0,this.wrapS=n,this.wrapT=s,this.magFilter=r,this.minFilter=a,this.anisotropy=c,this.format=o,this.internalFormat=null,this.type=l,this.offset=new kt(0,0),this.repeat=new kt(1,1),this.center=new kt(0,0),this.rotation=0,this.matrixAutoUpdate=!0,this.matrix=new ae,this.generateMipmaps=!0,this.mipmapsAutoUpdate=!0,this.premultiplyAlpha=!1,this.flipY=!0,this.unpackAlignment=4,this.colorSpace=h,this.userData={},this.updateRanges=[],this.version=0,this.onUpdate=null,this.renderTarget=null,this.isRenderTargetTexture=!1,this.isArrayTexture=!!(t&&t.depth&&t.depth>1),this.pmremVersion=0,this.isPMREMTexture=!1,this.normalized=!1}get width(){return this.source.getSize(ac).x}get height(){return this.source.getSize(ac).y}get depth(){return this.source.getSize(ac).z}get image(){return this.source.data}set image(t){this.source.data=t}updateMatrix(){this.matrix.setUvTransform(this.offset.x,this.offset.y,this.repeat.x,this.repeat.y,this.rotation,this.center.x,this.center.y)}addUpdateRange(t,e){this.updateRanges.push({start:t,count:e})}clearUpdateRanges(){this.updateRanges.length=0}clone(){return new this.constructor().copy(this)}copy(t){return this.name=t.name,this.source=t.source,this.mipmaps=t.mipmaps.slice(0),this.mapping=t.mapping,this.channel=t.channel,this.wrapS=t.wrapS,this.wrapT=t.wrapT,this.magFilter=t.magFilter,this.minFilter=t.minFilter,this.anisotropy=t.anisotropy,this.format=t.format,this.internalFormat=t.internalFormat,this.type=t.type,this.normalized=t.normalized,this.offset.copy(t.offset),this.repeat.copy(t.repeat),this.center.copy(t.center),this.rotation=t.rotation,this.matrixAutoUpdate=t.matrixAutoUpdate,this.matrix.copy(t.matrix),this.generateMipmaps=t.generateMipmaps,this.mipmapsAutoUpdate=t.mipmapsAutoUpdate,this.premultiplyAlpha=t.premultiplyAlpha,this.flipY=t.flipY,this.unpackAlignment=t.unpackAlignment,this.colorSpace=t.colorSpace,this.renderTarget=t.renderTarget,this.isRenderTargetTexture=t.isRenderTargetTexture,this.isPMREMTexture=t.isPMREMTexture,this.isArrayTexture=t.isArrayTexture,this.userData=JSON.parse(JSON.stringify(t.userData)),this.needsUpdate=!0,this}setValues(t){for(let e in t){let n=t[e];if(n===void 0){Kt(`Texture.setValues(): parameter '${e}' has value of undefined.`);continue}let s=this[e];if(s===void 0){Kt(`Texture.setValues(): property '${e}' does not exist.`);continue}s&&n&&s.isVector2&&n.isVector2||s&&n&&s.isVector3&&n.isVector3||s&&n&&s.isMatrix3&&n.isMatrix3?s.copy(n):this[e]=n}}toJSON(t){let e=t===void 0||typeof t=="string";if(!e&&t.textures[this.uuid]!==void 0)return t.textures[this.uuid];let n={metadata:{version:4.7,type:"Texture",generator:"Texture.toJSON"},uuid:this.uuid,name:this.name,image:this.source.toJSON(t).uuid,mapping:this.mapping,channel:this.channel,repeat:[this.repeat.x,this.repeat.y],offset:[this.offset.x,this.offset.y],center:[this.center.x,this.center.y],rotation:this.rotation,wrap:[this.wrapS,this.wrapT],format:this.format,internalFormat:this.internalFormat,type:this.type,normalized:this.normalized,colorSpace:this.colorSpace,minFilter:this.minFilter,magFilter:this.magFilter,anisotropy:this.anisotropy,flipY:this.flipY,generateMipmaps:this.generateMipmaps,mipmapsAutoUpdate:this.mipmapsAutoUpdate,premultiplyAlpha:this.premultiplyAlpha,unpackAlignment:this.unpackAlignment};return Object.keys(this.userData).length>0&&(n.userData=this.userData),e||(t.textures[this.uuid]=n),n}dispose(){this.dispatchEvent({type:"dispose"})}transformUv(t){if(this.mapping!==Zc)return t;if(t.applyMatrix3(this.matrix),t.x<0||t.x>1)switch(this.wrapS){case fo:t.x=t.x-Math.floor(t.x);break;case Ei:t.x=t.x<0?0:1;break;case po:Math.abs(Math.floor(t.x)%2)===1?t.x=Math.ceil(t.x)-t.x:t.x=t.x-Math.floor(t.x);break}if(t.y<0||t.y>1)switch(this.wrapT){case fo:t.y=t.y-Math.floor(t.y);break;case Ei:t.y=t.y<0?0:1;break;case po:Math.abs(Math.floor(t.y)%2)===1?t.y=Math.ceil(t.y)-t.y:t.y=t.y-Math.floor(t.y);break}return this.flipY&&(t.y=1-t.y),t}set needsUpdate(t){t===!0&&(this.version++,this.source.needsUpdate=!0)}set needsPMREMUpdate(t){t===!0&&this.pmremVersion++}};Dn.DEFAULT_IMAGE=null;Dn.DEFAULT_MAPPING=Zc;Dn.DEFAULT_ANISOTROPY=1;var je=class{static{this.prototype.isVector4=!0}constructor(t=0,e=0,n=0,s=1){this.x=t,this.y=e,this.z=n,this.w=s}get width(){return this.z}set width(t){this.z=t}get height(){return this.w}set height(t){this.w=t}set(t,e,n,s){return this.x=t,this.y=e,this.z=n,this.w=s,this}setScalar(t){return this.x=t,this.y=t,this.z=t,this.w=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setZ(t){return this.z=t,this}setW(t){return this.w=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;case 2:this.z=e;break;case 3:this.w=e;break;default:throw new Error("THREE.Vector4: index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;case 2:return this.z;case 3:return this.w;default:throw new Error("THREE.Vector4: index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y,this.z,this.w)}copy(t){return this.x=t.x,this.y=t.y,this.z=t.z,this.w=t.w!==void 0?t.w:1,this}add(t){return this.x+=t.x,this.y+=t.y,this.z+=t.z,this.w+=t.w,this}addScalar(t){return this.x+=t,this.y+=t,this.z+=t,this.w+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this.z=t.z+e.z,this.w=t.w+e.w,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this.z+=t.z*e,this.w+=t.w*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this.z-=t.z,this.w-=t.w,this}subScalar(t){return this.x-=t,this.y-=t,this.z-=t,this.w-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this.z=t.z-e.z,this.w=t.w-e.w,this}multiply(t){return this.x*=t.x,this.y*=t.y,this.z*=t.z,this.w*=t.w,this}multiplyScalar(t){return this.x*=t,this.y*=t,this.z*=t,this.w*=t,this}applyMatrix4(t){let e=this.x,n=this.y,s=this.z,r=this.w,a=t.elements;return this.x=a[0]*e+a[4]*n+a[8]*s+a[12]*r,this.y=a[1]*e+a[5]*n+a[9]*s+a[13]*r,this.z=a[2]*e+a[6]*n+a[10]*s+a[14]*r,this.w=a[3]*e+a[7]*n+a[11]*s+a[15]*r,this}divide(t){return this.x/=t.x,this.y/=t.y,this.z/=t.z,this.w/=t.w,this}divideScalar(t){return this.multiplyScalar(1/t)}setAxisAngleFromQuaternion(t){this.w=2*Math.acos(t.w);let e=Math.sqrt(1-t.w*t.w);return e<1e-4?(this.x=1,this.y=0,this.z=0):(this.x=t.x/e,this.y=t.y/e,this.z=t.z/e),this}setAxisAngleFromRotationMatrix(t){let e,n,s,r,l=t.elements,c=l[0],h=l[4],f=l[8],d=l[1],p=l[5],x=l[9],S=l[2],m=l[6],g=l[10];if(Math.abs(h-d)<.01&&Math.abs(f-S)<.01&&Math.abs(x-m)<.01){if(Math.abs(h+d)<.1&&Math.abs(f+S)<.1&&Math.abs(x+m)<.1&&Math.abs(c+p+g-3)<.1)return this.set(1,0,0,0),this;e=Math.PI;let P=(c+1)/2,T=(p+1)/2,C=(g+1)/2,A=(h+d)/4,_=(f+S)/4,b=(x+m)/4;return P>T&&P>C?P<.01?(n=0,s=.707106781,r=.707106781):(n=Math.sqrt(P),s=A/n,r=_/n):T>C?T<.01?(n=.707106781,s=0,r=.707106781):(s=Math.sqrt(T),n=A/s,r=b/s):C<.01?(n=.707106781,s=.707106781,r=0):(r=Math.sqrt(C),n=_/r,s=b/r),this.set(n,s,r,e),this}let E=Math.sqrt((m-x)*(m-x)+(f-S)*(f-S)+(d-h)*(d-h));return Math.abs(E)<.001&&(E=1),this.x=(m-x)/E,this.y=(f-S)/E,this.z=(d-h)/E,this.w=Math.acos((c+p+g-1)/2),this}setFromMatrixPosition(t){let e=t.elements;return this.x=e[12],this.y=e[13],this.z=e[14],this.w=e[15],this}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this.z=Math.min(this.z,t.z),this.w=Math.min(this.w,t.w),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this.z=Math.max(this.z,t.z),this.w=Math.max(this.w,t.w),this}clamp(t,e){return this.x=ge(this.x,t.x,e.x),this.y=ge(this.y,t.y,e.y),this.z=ge(this.z,t.z,e.z),this.w=ge(this.w,t.w,e.w),this}clampScalar(t,e){return this.x=ge(this.x,t,e),this.y=ge(this.y,t,e),this.z=ge(this.z,t,e),this.w=ge(this.w,t,e),this}clampLength(t,e){let n=this.length();return this.divideScalar(n||1).multiplyScalar(ge(n,t,e))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this.w=Math.floor(this.w),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this.w=Math.ceil(this.w),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this.w=Math.round(this.w),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this.w=Math.trunc(this.w),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this.w=-this.w,this}dot(t){return this.x*t.x+this.y*t.y+this.z*t.z+this.w*t.w}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)+Math.abs(this.w)}normalize(){return this.divideScalar(this.length()||1)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this.z+=(t.z-this.z)*e,this.w+=(t.w-this.w)*e,this}lerpVectors(t,e,n){return this.x=t.x+(e.x-t.x)*n,this.y=t.y+(e.y-t.y)*n,this.z=t.z+(e.z-t.z)*n,this.w=t.w+(e.w-t.w)*n,this}equals(t){return t.x===this.x&&t.y===this.y&&t.z===this.z&&t.w===this.w}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this.z=t[e+2],this.w=t[e+3],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t[e+2]=this.z,t[e+3]=this.w,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this.z=t.getZ(e),this.w=t.getW(e),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this.w=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z,yield this.w}},_o=class extends pi{constructor(t=1,e=1,n={}){super(),n=Object.assign({generateMipmaps:!1,internalFormat:null,minFilter:Ln,depthBuffer:!0,stencilBuffer:!1,resolveColorBuffer:!0,resolveDepthBuffer:!0,resolveStencilBuffer:!0,storeMultisampledColorBuffer:!0,storeMultisampledDepthBuffer:!0,storeMultisampledStencilBuffer:!0,depthTexture:null,samples:0,count:1,depth:1,multiview:!1,useArrayDepthTexture:!1},n),this.isRenderTarget=!0,this.width=t,this.height=e,this.depth=n.depth,this.scissor=new je(0,0,t,e),this.scissorTest=!1,this.viewport=new je(0,0,t,e),this.textures=[];let s=n.count;for(let r=0;r<s;r++)this.textures[r]=new Dn({width:t,height:e,depth:n.depth}),this.textures[r].isRenderTargetTexture=!0,this.textures[r].renderTarget=this;this._setTextureOptions(n),this.depthBuffer=n.depthBuffer,this.stencilBuffer=n.stencilBuffer,this.resolveColorBuffer=n.resolveColorBuffer,this.resolveDepthBuffer=n.resolveDepthBuffer,this.resolveStencilBuffer=n.resolveStencilBuffer,this.storeMultisampledColorBuffer=n.storeMultisampledColorBuffer,this.storeMultisampledDepthBuffer=n.storeMultisampledDepthBuffer,this.storeMultisampledStencilBuffer=n.storeMultisampledStencilBuffer,this._depthTexture=null,this.depthTexture=n.depthTexture,this.samples=n.samples,this.multiview=n.multiview,this.useArrayDepthTexture=n.useArrayDepthTexture}_setTextureOptions(t={}){let e={minFilter:Ln,generateMipmaps:!1,flipY:!1,internalFormat:null};t.mapping!==void 0&&(e.mapping=t.mapping),t.wrapS!==void 0&&(e.wrapS=t.wrapS),t.wrapT!==void 0&&(e.wrapT=t.wrapT),t.wrapR!==void 0&&(e.wrapR=t.wrapR),t.magFilter!==void 0&&(e.magFilter=t.magFilter),t.minFilter!==void 0&&(e.minFilter=t.minFilter),t.format!==void 0&&(e.format=t.format),t.type!==void 0&&(e.type=t.type),t.anisotropy!==void 0&&(e.anisotropy=t.anisotropy),t.colorSpace!==void 0&&(e.colorSpace=t.colorSpace),t.flipY!==void 0&&(e.flipY=t.flipY),t.generateMipmaps!==void 0&&(e.generateMipmaps=t.generateMipmaps),t.mipmapsAutoUpdate!==void 0&&(e.mipmapsAutoUpdate=t.mipmapsAutoUpdate),t.internalFormat!==void 0&&(e.internalFormat=t.internalFormat);for(let n=0;n<this.textures.length;n++)this.textures[n].setValues(e)}get texture(){return this.textures[0]}set texture(t){this.textures[0]=t}set depthTexture(t){this._depthTexture!==null&&this._depthTexture.renderTarget===this&&(this._depthTexture.renderTarget=null),t!==null&&t.renderTarget===null&&(t.renderTarget=this),this._depthTexture=t}get depthTexture(){return this._depthTexture}setSize(t,e,n=1){if(this.width!==t||this.height!==e||this.depth!==n){this.width=t,this.height=e,this.depth=n;for(let s=0,r=this.textures.length;s<r;s++)this.textures[s].image.width=t,this.textures[s].image.height=e,this.textures[s].image.depth=n,this.textures[s].isData3DTexture!==!0&&(this.textures[s].isArrayTexture=this.textures[s].image.depth>1);this.dispose()}this.viewport.set(0,0,t,e),this.scissor.set(0,0,t,e)}clone(){return new this.constructor().copy(this)}copy(t){this.width=t.width,this.height=t.height,this.depth=t.depth,this.scissor.copy(t.scissor),this.scissorTest=t.scissorTest,this.viewport.copy(t.viewport),this.textures.length=0;for(let e=0,n=t.textures.length;e<n;e++){this.textures[e]=t.textures[e].clone(),this.textures[e].isRenderTargetTexture=!0,this.textures[e].renderTarget=this;let s=Object.assign({},t.textures[e].image);this.textures[e].source=new or(s)}if(this.depthBuffer=t.depthBuffer,this.stencilBuffer=t.stencilBuffer,this.resolveColorBuffer=t.resolveColorBuffer,this.resolveDepthBuffer=t.resolveDepthBuffer,this.resolveStencilBuffer=t.resolveStencilBuffer,this.storeMultisampledColorBuffer=t.storeMultisampledColorBuffer,this.storeMultisampledDepthBuffer=t.storeMultisampledDepthBuffer,this.storeMultisampledStencilBuffer=t.storeMultisampledStencilBuffer,t.depthTexture!==null)if(t.depthTexture.renderTarget===t){let e=t.depthTexture.clone();e.renderTarget=null,this.depthTexture=e}else this.depthTexture=t.depthTexture;else this.depthTexture=null;return this.samples=t.samples,this.multiview=t.multiview,this.useArrayDepthTexture=t.useArrayDepthTexture,this}dispose(){this.dispatchEvent({type:"dispose"})}},Zn=class extends _o{constructor(t=1,e=1,n={}){super(t,e,n),this.isWebGLRenderTarget=!0}},Zr=class extends Dn{constructor(t=null,e=1,n=1,s=1){super(null),this.isDataArrayTexture=!0,this.image={data:t,width:e,height:n,depth:s},this.magFilter=cn,this.minFilter=cn,this.wrapR=Ei,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1,this.layerUpdates=new Set}copy(t){return super.copy(t),this.wrapR=t.wrapR,this}addLayerUpdate(t){this.layerUpdates.add(t)}clearLayerUpdates(){this.layerUpdates.clear()}};var xo=class extends Dn{constructor(t=null,e=1,n=1,s=1){super(null),this.isData3DTexture=!0,this.image={data:t,width:e,height:n,depth:s},this.magFilter=cn,this.minFilter=cn,this.wrapR=Ei,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}copy(t){return super.copy(t),this.wrapR=t.wrapR,this}};var Ge=class i{static{this.prototype.isMatrix4=!0}constructor(t,e,n,s,r,a,o,l,c,h,f,d,p,x,S,m){this.elements=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],t!==void 0&&this.set(t,e,n,s,r,a,o,l,c,h,f,d,p,x,S,m)}set(t,e,n,s,r,a,o,l,c,h,f,d,p,x,S,m){let g=this.elements;return g[0]=t,g[4]=e,g[8]=n,g[12]=s,g[1]=r,g[5]=a,g[9]=o,g[13]=l,g[2]=c,g[6]=h,g[10]=f,g[14]=d,g[3]=p,g[7]=x,g[11]=S,g[15]=m,this}identity(){return this.set(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),this}clone(){return new i().fromArray(this.elements)}copy(t){let e=this.elements,n=t.elements;return e[0]=n[0],e[1]=n[1],e[2]=n[2],e[3]=n[3],e[4]=n[4],e[5]=n[5],e[6]=n[6],e[7]=n[7],e[8]=n[8],e[9]=n[9],e[10]=n[10],e[11]=n[11],e[12]=n[12],e[13]=n[13],e[14]=n[14],e[15]=n[15],this}copyPosition(t){let e=this.elements,n=t.elements;return e[12]=n[12],e[13]=n[13],e[14]=n[14],this}setFromMatrix3(t){let e=t.elements;return this.set(e[0],e[3],e[6],0,e[1],e[4],e[7],0,e[2],e[5],e[8],0,0,0,0,1),this}extractBasis(t,e,n){return this.determinantAffine()===0?(t.set(1,0,0),e.set(0,1,0),n.set(0,0,1),this):(t.setFromMatrixColumn(this,0),e.setFromMatrixColumn(this,1),n.setFromMatrixColumn(this,2),this)}makeBasis(t,e,n){return this.set(t.x,e.x,n.x,0,t.y,e.y,n.y,0,t.z,e.z,n.z,0,0,0,0,1),this}extractRotation(t){if(t.determinantAffine()===0)return this.identity();let e=this.elements,n=t.elements,s=1/Ws.setFromMatrixColumn(t,0).length(),r=1/Ws.setFromMatrixColumn(t,1).length(),a=1/Ws.setFromMatrixColumn(t,2).length();return e[0]=n[0]*s,e[1]=n[1]*s,e[2]=n[2]*s,e[3]=0,e[4]=n[4]*r,e[5]=n[5]*r,e[6]=n[6]*r,e[7]=0,e[8]=n[8]*a,e[9]=n[9]*a,e[10]=n[10]*a,e[11]=0,e[12]=0,e[13]=0,e[14]=0,e[15]=1,this}makeRotationFromEuler(t){let e=this.elements,n=t.x,s=t.y,r=t.z,a=Math.cos(n),o=Math.sin(n),l=Math.cos(s),c=Math.sin(s),h=Math.cos(r),f=Math.sin(r);if(t.order==="XYZ"){let d=a*h,p=a*f,x=o*h,S=o*f;e[0]=l*h,e[4]=-l*f,e[8]=c,e[1]=p+x*c,e[5]=d-S*c,e[9]=-o*l,e[2]=S-d*c,e[6]=x+p*c,e[10]=a*l}else if(t.order==="YXZ"){let d=l*h,p=l*f,x=c*h,S=c*f;e[0]=d+S*o,e[4]=x*o-p,e[8]=a*c,e[1]=a*f,e[5]=a*h,e[9]=-o,e[2]=p*o-x,e[6]=S+d*o,e[10]=a*l}else if(t.order==="ZXY"){let d=l*h,p=l*f,x=c*h,S=c*f;e[0]=d-S*o,e[4]=-a*f,e[8]=x+p*o,e[1]=p+x*o,e[5]=a*h,e[9]=S-d*o,e[2]=-a*c,e[6]=o,e[10]=a*l}else if(t.order==="ZYX"){let d=a*h,p=a*f,x=o*h,S=o*f;e[0]=l*h,e[4]=x*c-p,e[8]=d*c+S,e[1]=l*f,e[5]=S*c+d,e[9]=p*c-x,e[2]=-c,e[6]=o*l,e[10]=a*l}else if(t.order==="YZX"){let d=a*l,p=a*c,x=o*l,S=o*c;e[0]=l*h,e[4]=S-d*f,e[8]=x*f+p,e[1]=f,e[5]=a*h,e[9]=-o*h,e[2]=-c*h,e[6]=p*f+x,e[10]=d-S*f}else if(t.order==="XZY"){let d=a*l,p=a*c,x=o*l,S=o*c;e[0]=l*h,e[4]=-f,e[8]=c*h,e[1]=d*f+S,e[5]=a*h,e[9]=p*f-x,e[2]=x*f-p,e[6]=o*h,e[10]=S*f+d}return e[3]=0,e[7]=0,e[11]=0,e[12]=0,e[13]=0,e[14]=0,e[15]=1,this}makeRotationFromQuaternion(t){return this.compose(Gf,t,Vf)}lookAt(t,e,n){let s=this.elements;return Xn.subVectors(t,e),Xn.lengthSq()===0&&(Xn.z=1),Xn.normalize(),is.crossVectors(n,Xn),is.lengthSq()===0&&(Math.abs(n.z)===1?Xn.x+=1e-4:Xn.z+=1e-4,Xn.normalize(),is.crossVectors(n,Xn)),is.normalize(),Ua.crossVectors(Xn,is),s[0]=is.x,s[4]=Ua.x,s[8]=Xn.x,s[1]=is.y,s[5]=Ua.y,s[9]=Xn.y,s[2]=is.z,s[6]=Ua.z,s[10]=Xn.z,this}multiply(t){return this.multiplyMatrices(this,t)}premultiply(t){return this.multiplyMatrices(t,this)}multiplyMatrices(t,e){let n=t.elements,s=e.elements,r=this.elements,a=n[0],o=n[4],l=n[8],c=n[12],h=n[1],f=n[5],d=n[9],p=n[13],x=n[2],S=n[6],m=n[10],g=n[14],E=n[3],P=n[7],T=n[11],C=n[15],A=s[0],_=s[4],b=s[8],G=s[12],B=s[1],k=s[5],H=s[9],K=s[13],U=s[2],Y=s[6],tt=s[10],j=s[14],dt=s[3],V=s[7],it=s[11],ft=s[15];return r[0]=a*A+o*B+l*U+c*dt,r[4]=a*_+o*k+l*Y+c*V,r[8]=a*b+o*H+l*tt+c*it,r[12]=a*G+o*K+l*j+c*ft,r[1]=h*A+f*B+d*U+p*dt,r[5]=h*_+f*k+d*Y+p*V,r[9]=h*b+f*H+d*tt+p*it,r[13]=h*G+f*K+d*j+p*ft,r[2]=x*A+S*B+m*U+g*dt,r[6]=x*_+S*k+m*Y+g*V,r[10]=x*b+S*H+m*tt+g*it,r[14]=x*G+S*K+m*j+g*ft,r[3]=E*A+P*B+T*U+C*dt,r[7]=E*_+P*k+T*Y+C*V,r[11]=E*b+P*H+T*tt+C*it,r[15]=E*G+P*K+T*j+C*ft,this}multiplyScalar(t){let e=this.elements;return e[0]*=t,e[4]*=t,e[8]*=t,e[12]*=t,e[1]*=t,e[5]*=t,e[9]*=t,e[13]*=t,e[2]*=t,e[6]*=t,e[10]*=t,e[14]*=t,e[3]*=t,e[7]*=t,e[11]*=t,e[15]*=t,this}determinant(){let t=this.elements,e=t[0],n=t[4],s=t[8],r=t[12],a=t[1],o=t[5],l=t[9],c=t[13],h=t[2],f=t[6],d=t[10],p=t[14],x=t[3],S=t[7],m=t[11],g=t[15],E=l*p-c*d,P=o*p-c*f,T=o*d-l*f,C=a*p-c*h,A=a*d-l*h,_=a*f-o*h;return e*(S*E-m*P+g*T)-n*(x*E-m*C+g*A)+s*(x*P-S*C+g*_)-r*(x*T-S*A+m*_)}determinantAffine(){let t=this.elements,e=t[0],n=t[4],s=t[8],r=t[1],a=t[5],o=t[9],l=t[2],c=t[6],h=t[10];return e*(a*h-o*c)-n*(r*h-o*l)+s*(r*c-a*l)}transpose(){let t=this.elements,e;return e=t[1],t[1]=t[4],t[4]=e,e=t[2],t[2]=t[8],t[8]=e,e=t[6],t[6]=t[9],t[9]=e,e=t[3],t[3]=t[12],t[12]=e,e=t[7],t[7]=t[13],t[13]=e,e=t[11],t[11]=t[14],t[14]=e,this}setPosition(t,e,n){let s=this.elements;return t.isVector3?(s[12]=t.x,s[13]=t.y,s[14]=t.z):(s[12]=t,s[13]=e,s[14]=n),this}invert(){let t=this.elements,e=t[0],n=t[1],s=t[2],r=t[3],a=t[4],o=t[5],l=t[6],c=t[7],h=t[8],f=t[9],d=t[10],p=t[11],x=t[12],S=t[13],m=t[14],g=t[15],E=e*o-n*a,P=e*l-s*a,T=e*c-r*a,C=n*l-s*o,A=n*c-r*o,_=s*c-r*l,b=h*S-f*x,G=h*m-d*x,B=h*g-p*x,k=f*m-d*S,H=f*g-p*S,K=d*g-p*m,U=E*K-P*H+T*k+C*B-A*G+_*b;if(U===0)return this.set(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);let Y=1/U;return t[0]=(o*K-l*H+c*k)*Y,t[1]=(s*H-n*K-r*k)*Y,t[2]=(S*_-m*A+g*C)*Y,t[3]=(d*A-f*_-p*C)*Y,t[4]=(l*B-a*K-c*G)*Y,t[5]=(e*K-s*B+r*G)*Y,t[6]=(m*T-x*_-g*P)*Y,t[7]=(h*_-d*T+p*P)*Y,t[8]=(a*H-o*B+c*b)*Y,t[9]=(n*B-e*H-r*b)*Y,t[10]=(x*A-S*T+g*E)*Y,t[11]=(f*T-h*A-p*E)*Y,t[12]=(o*G-a*k-l*b)*Y,t[13]=(e*k-n*G+s*b)*Y,t[14]=(S*P-x*C-m*E)*Y,t[15]=(h*C-f*P+d*E)*Y,this}scale(t){let e=this.elements,n=t.x,s=t.y,r=t.z;return e[0]*=n,e[4]*=s,e[8]*=r,e[1]*=n,e[5]*=s,e[9]*=r,e[2]*=n,e[6]*=s,e[10]*=r,e[3]*=n,e[7]*=s,e[11]*=r,this}getMaxScaleOnAxis(){let t=this.elements,e=t[0]*t[0]+t[1]*t[1]+t[2]*t[2],n=t[4]*t[4]+t[5]*t[5]+t[6]*t[6],s=t[8]*t[8]+t[9]*t[9]+t[10]*t[10];return Math.sqrt(Math.max(e,n,s))}makeTranslation(t,e,n){return t.isVector3?this.set(1,0,0,t.x,0,1,0,t.y,0,0,1,t.z,0,0,0,1):this.set(1,0,0,t,0,1,0,e,0,0,1,n,0,0,0,1),this}makeRotationX(t){let e=Math.cos(t),n=Math.sin(t);return this.set(1,0,0,0,0,e,-n,0,0,n,e,0,0,0,0,1),this}makeRotationY(t){let e=Math.cos(t),n=Math.sin(t);return this.set(e,0,n,0,0,1,0,0,-n,0,e,0,0,0,0,1),this}makeRotationZ(t){let e=Math.cos(t),n=Math.sin(t);return this.set(e,-n,0,0,n,e,0,0,0,0,1,0,0,0,0,1),this}makeRotationAxis(t,e){let n=Math.cos(e),s=Math.sin(e),r=1-n,a=t.x,o=t.y,l=t.z,c=r*a,h=r*o;return this.set(c*a+n,c*o-s*l,c*l+s*o,0,c*o+s*l,h*o+n,h*l-s*a,0,c*l-s*o,h*l+s*a,r*l*l+n,0,0,0,0,1),this}makeScale(t,e,n){return this.set(t,0,0,0,0,e,0,0,0,0,n,0,0,0,0,1),this}makeShear(t,e,n,s,r,a){return this.set(1,n,r,0,t,1,a,0,e,s,1,0,0,0,0,1),this}compose(t,e,n){let s=this.elements,r=e._x,a=e._y,o=e._z,l=e._w,c=r+r,h=a+a,f=o+o,d=r*c,p=r*h,x=r*f,S=a*h,m=a*f,g=o*f,E=l*c,P=l*h,T=l*f,C=n.x,A=n.y,_=n.z;return s[0]=(1-(S+g))*C,s[1]=(p+T)*C,s[2]=(x-P)*C,s[3]=0,s[4]=(p-T)*A,s[5]=(1-(d+g))*A,s[6]=(m+E)*A,s[7]=0,s[8]=(x+P)*_,s[9]=(m-E)*_,s[10]=(1-(d+S))*_,s[11]=0,s[12]=t.x,s[13]=t.y,s[14]=t.z,s[15]=1,this}decompose(t,e,n){let s=this.elements;t.x=s[12],t.y=s[13],t.z=s[14];let r=this.determinantAffine();if(r===0)return n.set(1,1,1),e.identity(),this;let a=Ws.set(s[0],s[1],s[2]).length(),o=Ws.set(s[4],s[5],s[6]).length(),l=Ws.set(s[8],s[9],s[10]).length();r<0&&(a=-a),ui.copy(this);let c=1/a,h=1/o,f=1/l;return ui.elements[0]*=c,ui.elements[1]*=c,ui.elements[2]*=c,ui.elements[4]*=h,ui.elements[5]*=h,ui.elements[6]*=h,ui.elements[8]*=f,ui.elements[9]*=f,ui.elements[10]*=f,e.setFromRotationMatrix(ui),n.x=a,n.y=o,n.z=l,this}makePerspective(t,e,n,s,r,a,o=ni,l=!1){let c=this.elements,h=2*r/(e-t),f=2*r/(n-s),d=(e+t)/(e-t),p=(n+s)/(n-s),x,S;if(l)x=r/(a-r),S=a*r/(a-r);else if(o===ni)x=-(a+r)/(a-r),S=-2*a*r/(a-r);else if(o===sr)x=-a/(a-r),S=-a*r/(a-r);else throw new Error("THREE.Matrix4.makePerspective(): Invalid coordinate system: "+o);return c[0]=h,c[4]=0,c[8]=d,c[12]=0,c[1]=0,c[5]=f,c[9]=p,c[13]=0,c[2]=0,c[6]=0,c[10]=x,c[14]=S,c[3]=0,c[7]=0,c[11]=-1,c[15]=0,this}makeOrthographic(t,e,n,s,r,a,o=ni,l=!1){let c=this.elements,h=2/(e-t),f=2/(n-s),d=-(e+t)/(e-t),p=-(n+s)/(n-s),x,S;if(l)x=1/(a-r),S=a/(a-r);else if(o===ni)x=-2/(a-r),S=-(a+r)/(a-r);else if(o===sr)x=-1/(a-r),S=-r/(a-r);else throw new Error("THREE.Matrix4.makeOrthographic(): Invalid coordinate system: "+o);return c[0]=h,c[4]=0,c[8]=0,c[12]=d,c[1]=0,c[5]=f,c[9]=0,c[13]=p,c[2]=0,c[6]=0,c[10]=x,c[14]=S,c[3]=0,c[7]=0,c[11]=0,c[15]=1,this}equals(t){let e=this.elements,n=t.elements;for(let s=0;s<16;s++)if(e[s]!==n[s])return!1;return!0}fromArray(t,e=0){for(let n=0;n<16;n++)this.elements[n]=t[n+e];return this}toArray(t=[],e=0){let n=this.elements;return t[e]=n[0],t[e+1]=n[1],t[e+2]=n[2],t[e+3]=n[3],t[e+4]=n[4],t[e+5]=n[5],t[e+6]=n[6],t[e+7]=n[7],t[e+8]=n[8],t[e+9]=n[9],t[e+10]=n[10],t[e+11]=n[11],t[e+12]=n[12],t[e+13]=n[13],t[e+14]=n[14],t[e+15]=n[15],t}},Ws=new D,ui=new Ge,Gf=new D(0,0,0),Vf=new D(1,1,1),is=new D,Ua=new D,Xn=new D,nu=new Ge,iu=new Nn,Hi=class i{constructor(t=0,e=0,n=0,s=i.DEFAULT_ORDER){this.isEuler=!0,this._x=t,this._y=e,this._z=n,this._order=s}get x(){return this._x}set x(t){this._x=t,this._onChangeCallback()}get y(){return this._y}set y(t){this._y=t,this._onChangeCallback()}get z(){return this._z}set z(t){this._z=t,this._onChangeCallback()}get order(){return this._order}set order(t){this._order=t,this._onChangeCallback()}set(t,e,n,s=this._order){return this._x=t,this._y=e,this._z=n,this._order=s,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._order)}copy(t){return this._x=t._x,this._y=t._y,this._z=t._z,this._order=t._order,this._onChangeCallback(),this}setFromRotationMatrix(t,e=this._order,n=!0){let s=t.elements,r=s[0],a=s[4],o=s[8],l=s[1],c=s[5],h=s[9],f=s[2],d=s[6],p=s[10];switch(e){case"XYZ":this._y=Math.asin(ge(o,-1,1)),Math.abs(o)<.9999999?(this._x=Math.atan2(-h,p),this._z=Math.atan2(-a,r)):(this._x=Math.atan2(d,c),this._z=0);break;case"YXZ":this._x=Math.asin(-ge(h,-1,1)),Math.abs(h)<.9999999?(this._y=Math.atan2(o,p),this._z=Math.atan2(l,c)):(this._y=Math.atan2(-f,r),this._z=0);break;case"ZXY":this._x=Math.asin(ge(d,-1,1)),Math.abs(d)<.9999999?(this._y=Math.atan2(-f,p),this._z=Math.atan2(-a,c)):(this._y=0,this._z=Math.atan2(l,r));break;case"ZYX":this._y=Math.asin(-ge(f,-1,1)),Math.abs(f)<.9999999?(this._x=Math.atan2(d,p),this._z=Math.atan2(l,r)):(this._x=0,this._z=Math.atan2(-a,c));break;case"YZX":this._z=Math.asin(ge(l,-1,1)),Math.abs(l)<.9999999?(this._x=Math.atan2(-h,c),this._y=Math.atan2(-f,r)):(this._x=0,this._y=Math.atan2(o,p));break;case"XZY":this._z=Math.asin(-ge(a,-1,1)),Math.abs(a)<.9999999?(this._x=Math.atan2(d,c),this._y=Math.atan2(o,r)):(this._x=Math.atan2(-h,p),this._y=0);break;default:Kt("Euler: .setFromRotationMatrix() encountered an unknown order: "+e)}return this._order=e,n===!0&&this._onChangeCallback(),this}setFromQuaternion(t,e,n){return nu.makeRotationFromQuaternion(t),this.setFromRotationMatrix(nu,e,n)}setFromVector3(t,e=this._order){return this.set(t.x,t.y,t.z,e)}reorder(t){return iu.setFromEuler(this),this.setFromQuaternion(iu,t)}equals(t){return t._x===this._x&&t._y===this._y&&t._z===this._z&&t._order===this._order}fromArray(t){return this._x=t[0],this._y=t[1],this._z=t[2],t[3]!==void 0&&(this._order=t[3]),this._onChangeCallback(),this}toArray(t=[],e=0){return t[e]=this._x,t[e+1]=this._y,t[e+2]=this._z,t[e+3]=this._order,t}_onChange(t){return this._onChangeCallback=t,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._order}};Hi.DEFAULT_ORDER="XYZ";var lr=class{constructor(){this.mask=1}set(t){this.mask=(1<<t|0)>>>0}enable(t){this.mask|=1<<t|0}enableAll(){this.mask=-1}toggle(t){this.mask^=1<<t|0}disable(t){this.mask&=~(1<<t|0)}disableAll(){this.mask=0}test(t){return(this.mask&t.mask)!==0}isEnabled(t){return(this.mask&(1<<t|0))!==0}},Wf=0,su=new D,Xs=new Nn,Di=new Ge,Fa=new D,Dr=new D,Xf=new D,qf=new Nn,ru=new D(1,0,0),au=new D(0,1,0),ou=new D(0,0,1),lu={type:"added"},Yf={type:"removed"},qs={type:"childadded",child:null},oc={type:"childremoved",child:null},Mn=class i extends pi{constructor(){super(),this.isObject3D=!0,Object.defineProperty(this,"id",{value:Wf++}),this.uuid=vr(),this.name="",this.type="Object3D",this.parent=null,this.children=[],this.up=i.DEFAULT_UP.clone();let t=new D,e=new Hi,n=new Nn,s=new D(1,1,1);function r(){n.setFromEuler(e,!1)}function a(){e.setFromQuaternion(n,void 0,!1)}e._onChange(r),n._onChange(a),Object.defineProperties(this,{position:{configurable:!0,enumerable:!0,value:t},rotation:{configurable:!0,enumerable:!0,value:e},quaternion:{configurable:!0,enumerable:!0,value:n},scale:{configurable:!0,enumerable:!0,value:s},modelViewMatrix:{value:new Ge},normalMatrix:{value:new ae}}),this.matrix=new Ge,this.matrixWorld=new Ge,this.matrixAutoUpdate=i.DEFAULT_MATRIX_AUTO_UPDATE,this.matrixWorldAutoUpdate=i.DEFAULT_MATRIX_WORLD_AUTO_UPDATE,this.matrixWorldNeedsUpdate=!1,this.layers=new lr,this.visible=!0,this.castShadow=!1,this.receiveShadow=!1,this.frustumCulled=!0,this.renderOrder=0,this.animations=[],this.customDepthMaterial=void 0,this.customDistanceMaterial=void 0,this.static=!1,this.userData={},this.pivot=null}onBeforeShadow(){}onAfterShadow(){}onBeforeRender(){}onAfterRender(){}applyMatrix4(t){this.matrixAutoUpdate&&this.updateMatrix(),this.matrix.premultiply(t),this.matrix.decompose(this.position,this.quaternion,this.scale),this.pivot!==null&&this.position.copy(this.pivot).applyMatrix4(this.matrix).sub(this.pivot)}applyQuaternion(t){return this.quaternion.premultiply(t),this}setRotationFromAxisAngle(t,e){this.quaternion.setFromAxisAngle(t,e)}setRotationFromEuler(t){this.quaternion.setFromEuler(t,!0)}setRotationFromMatrix(t){this.quaternion.setFromRotationMatrix(t)}setRotationFromQuaternion(t){this.quaternion.copy(t)}rotateOnAxis(t,e){return Xs.setFromAxisAngle(t,e),this.quaternion.multiply(Xs),this}rotateOnWorldAxis(t,e){return Xs.setFromAxisAngle(t,e),this.quaternion.premultiply(Xs),this}rotateX(t){return this.rotateOnAxis(ru,t)}rotateY(t){return this.rotateOnAxis(au,t)}rotateZ(t){return this.rotateOnAxis(ou,t)}translateOnAxis(t,e){return su.copy(t).applyQuaternion(this.quaternion),this.position.add(su.multiplyScalar(e)),this}translateX(t){return this.translateOnAxis(ru,t)}translateY(t){return this.translateOnAxis(au,t)}translateZ(t){return this.translateOnAxis(ou,t)}localToWorld(t){return this.updateWorldMatrix(!0,!1),t.applyMatrix4(this.matrixWorld)}worldToLocal(t){return this.updateWorldMatrix(!0,!1),t.applyMatrix4(Di.copy(this.matrixWorld).invert())}lookAt(t,e,n){t.isVector3?Fa.copy(t):Fa.set(t,e,n);let s=this.parent;this.updateWorldMatrix(!0,!1),Dr.setFromMatrixPosition(this.matrixWorld),this.isCamera||this.isLight?Di.lookAt(Dr,Fa,this.up):Di.lookAt(Fa,Dr,this.up),this.quaternion.setFromRotationMatrix(Di),s&&(Di.extractRotation(s.matrixWorld),Xs.setFromRotationMatrix(Di),this.quaternion.premultiply(Xs.invert()))}add(t){if(arguments.length>1){for(let e=0;e<arguments.length;e++)this.add(arguments[e]);return this}return t===this?(ie("Object3D.add: object can't be added as a child of itself.",t),this):(t&&t.isObject3D?(t.removeFromParent(),t.parent=this,this.children.push(t),t.dispatchEvent(lu),qs.child=t,this.dispatchEvent(qs),qs.child=null):ie("Object3D.add: object not an instance of THREE.Object3D.",t),this)}remove(t){if(arguments.length>1){for(let n=0;n<arguments.length;n++)this.remove(arguments[n]);return this}let e=this.children.indexOf(t);return e!==-1&&(t.parent=null,this.children.splice(e,1),t.dispatchEvent(Yf),oc.child=t,this.dispatchEvent(oc),oc.child=null),this}removeFromParent(){let t=this.parent;return t!==null&&t.remove(this),this}clear(){return this.remove(...this.children)}attach(t){return this.updateWorldMatrix(!0,!1),Di.copy(this.matrixWorld).invert(),t.parent!==null&&(t.parent.updateWorldMatrix(!0,!1),Di.multiply(t.parent.matrixWorld)),t.applyMatrix4(Di),t.removeFromParent(),t.parent=this,this.children.push(t),t.updateWorldMatrix(!1,!0),t.dispatchEvent(lu),qs.child=t,this.dispatchEvent(qs),qs.child=null,this}getObjectById(t){return this.getObjectByProperty("id",t)}getObjectByName(t){return this.getObjectByProperty("name",t)}getObjectByProperty(t,e){if(this[t]===e)return this;for(let n=0,s=this.children.length;n<s;n++){let a=this.children[n].getObjectByProperty(t,e);if(a!==void 0)return a}}getObjectsByProperty(t,e,n=[]){this[t]===e&&n.push(this);let s=this.children;for(let r=0,a=s.length;r<a;r++)s[r].getObjectsByProperty(t,e,n);return n}getWorldPosition(t){return this.updateWorldMatrix(!0,!1),t.setFromMatrixPosition(this.matrixWorld)}getWorldQuaternion(t){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(Dr,t,Xf),t}getWorldScale(t){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(Dr,qf,t),t}getWorldDirection(t){this.updateWorldMatrix(!0,!1);let e=this.matrixWorld.elements;return t.set(e[8],e[9],e[10]).normalize()}raycast(){}intersectsFrustum(){return!0}traverse(t){t(this);let e=this.children;for(let n=0,s=e.length;n<s;n++)e[n].traverse(t)}traverseVisible(t){if(this.visible===!1)return;t(this);let e=this.children;for(let n=0,s=e.length;n<s;n++)e[n].traverseVisible(t)}traverseAncestors(t){let e=this.parent;e!==null&&(t(e),e.traverseAncestors(t))}updateMatrix(){this.matrix.compose(this.position,this.quaternion,this.scale);let t=this.pivot;if(t!==null){let e=t.x,n=t.y,s=t.z,r=this.matrix.elements;r[12]+=e-r[0]*e-r[4]*n-r[8]*s,r[13]+=n-r[1]*e-r[5]*n-r[9]*s,r[14]+=s-r[2]*e-r[6]*n-r[10]*s}this.matrixWorldNeedsUpdate=!0}updateMatrixWorld(t){this.matrixAutoUpdate&&this.updateMatrix(),(this.matrixWorldNeedsUpdate||t)&&(this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),this.matrixWorldNeedsUpdate=!1,t=!0);let e=this.children;for(let n=0,s=e.length;n<s;n++)e[n].updateMatrixWorld(t)}updateWorldMatrix(t,e,n=!1){let s=this.parent;if(t===!0&&s!==null&&s.updateWorldMatrix(!0,!1),this.matrixAutoUpdate&&this.updateMatrix(),(this.matrixWorldNeedsUpdate||n)&&(this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),this.matrixWorldNeedsUpdate=!1,n=!0),e===!0){let r=this.children;for(let a=0,o=r.length;a<o;a++)r[a].updateWorldMatrix(!1,!0,n)}}toJSON(t){let e=t===void 0||typeof t=="string",n={};e&&(t={geometries:{},materials:{},textures:{},images:{},shapes:{},skeletons:{},animations:{},nodes:{}},n.metadata={version:4.7,type:"Object",generator:"Object3D.toJSON"});let s={};s.uuid=this.uuid,s.type=this.type,s.name=this.name,s.castShadow=this.castShadow,s.receiveShadow=this.receiveShadow,s.visible=this.visible,s.frustumCulled=this.frustumCulled,s.renderOrder=this.renderOrder,s.static=this.static,s.matrixAutoUpdate=this.matrixAutoUpdate,Object.keys(this.userData).length>0&&(s.userData=this.userData),s.layers=this.layers.mask,s.matrix=this.matrix.toArray(),s.up=this.up.toArray(),this.pivot!==null&&(s.pivot=this.pivot.toArray()),this.morphTargetDictionary!==void 0&&(s.morphTargetDictionary=Object.assign({},this.morphTargetDictionary)),this.morphTargetInfluences!==void 0&&(s.morphTargetInfluences=this.morphTargetInfluences.slice()),this.isInstancedMesh&&(s.type="InstancedMesh",s.count=this.count,s.instanceMatrix=this.instanceMatrix.toJSON(),this.instanceColor!==null&&(s.instanceColor=this.instanceColor.toJSON())),this.isBatchedMesh&&(s.type="BatchedMesh",s.perObjectFrustumCulled=this.perObjectFrustumCulled,s.sortObjects=this.sortObjects,s.drawRanges=this._drawRanges,s.reservedRanges=this._reservedRanges,s.geometryInfo=this._geometryInfo.map(o=>({...o,boundingBox:o.boundingBox?o.boundingBox.toJSON():void 0,boundingSphere:o.boundingSphere?o.boundingSphere.toJSON():void 0})),s.instanceInfo=this._instanceInfo.map(o=>({...o})),s.availableInstanceIds=this._availableInstanceIds.slice(),s.availableGeometryIds=this._availableGeometryIds.slice(),s.nextIndexStart=this._nextIndexStart,s.nextVertexStart=this._nextVertexStart,s.geometryCount=this._geometryCount,s.maxInstanceCount=this._maxInstanceCount,s.maxVertexCount=this._maxVertexCount,s.maxIndexCount=this._maxIndexCount,s.geometryInitialized=this._geometryInitialized,s.matricesTexture=this._matricesTexture.toJSON(t),s.indirectTexture=this._indirectTexture.toJSON(t),this._colorsTexture!==null&&(s.colorsTexture=this._colorsTexture.toJSON(t)),this.boundingSphere!==null&&(s.boundingSphere=this.boundingSphere.toJSON()),this.boundingBox!==null&&(s.boundingBox=this.boundingBox.toJSON()));function r(o,l){return o[l.uuid]===void 0&&(o[l.uuid]=l.toJSON(t)),l.uuid}if(this.isScene)this.background&&(this.background.isColor?s.background=this.background.toJSON():this.background.isTexture&&(s.background=this.background.toJSON(t).uuid)),this.environment&&this.environment.isTexture&&this.environment.isRenderTargetTexture!==!0&&(s.environment=this.environment.toJSON(t).uuid);else if(this.isMesh||this.isLine||this.isPoints){s.geometry=r(t.geometries,this.geometry);let o=this.geometry.parameters;if(o!==void 0&&o.shapes!==void 0){let l=o.shapes;if(Array.isArray(l))for(let c=0,h=l.length;c<h;c++){let f=l[c];r(t.shapes,f)}else r(t.shapes,l)}}if(this.isSkinnedMesh&&(s.bindMode=this.bindMode,s.bindMatrix=this.bindMatrix.toArray(),this.skeleton!==void 0&&(r(t.skeletons,this.skeleton),s.skeleton=this.skeleton.uuid)),this.material!==void 0)if(Array.isArray(this.material)){let o=[];for(let l=0,c=this.material.length;l<c;l++)o.push(r(t.materials,this.material[l]));s.material=o}else s.material=r(t.materials,this.material);if(this.children.length>0){s.children=[];for(let o=0;o<this.children.length;o++)s.children.push(this.children[o].toJSON(t).object)}if(this.animations.length>0){s.animations=[];for(let o=0;o<this.animations.length;o++){let l=this.animations[o];s.animations.push(r(t.animations,l))}}if(e){let o=a(t.geometries),l=a(t.materials),c=a(t.textures),h=a(t.images),f=a(t.shapes),d=a(t.skeletons),p=a(t.animations),x=a(t.nodes);o.length>0&&(n.geometries=o),l.length>0&&(n.materials=l),c.length>0&&(n.textures=c),h.length>0&&(n.images=h),f.length>0&&(n.shapes=f),d.length>0&&(n.skeletons=d),p.length>0&&(n.animations=p),x.length>0&&(n.nodes=x)}return n.object=s,n;function a(o){let l=[];for(let c in o){let h=o[c];delete h.metadata,l.push(h)}return l}}clone(t){return new this.constructor().copy(this,t)}copy(t,e=!0){if(this.name=t.name,this.up.copy(t.up),this.position.copy(t.position),this.rotation.order=t.rotation.order,this.quaternion.copy(t.quaternion),this.scale.copy(t.scale),this.pivot=t.pivot!==null?t.pivot.clone():null,this.matrix.copy(t.matrix),this.matrixWorld.copy(t.matrixWorld),this.matrixAutoUpdate=t.matrixAutoUpdate,this.matrixWorldAutoUpdate=t.matrixWorldAutoUpdate,this.matrixWorldNeedsUpdate=t.matrixWorldNeedsUpdate,this.layers.mask=t.layers.mask,this.visible=t.visible,this.castShadow=t.castShadow,this.receiveShadow=t.receiveShadow,this.frustumCulled=t.frustumCulled,this.renderOrder=t.renderOrder,this.static=t.static,this.animations=t.animations.slice(),this.userData=JSON.parse(JSON.stringify(t.userData)),e===!0)for(let n=0;n<t.children.length;n++){let s=t.children[n];this.add(s.clone())}return this}dispose(){this.dispatchEvent({type:"dispose"})}};Mn.DEFAULT_UP=new D(0,1,0);Mn.DEFAULT_MATRIX_AUTO_UPDATE=!0;Mn.DEFAULT_MATRIX_WORLD_AUTO_UPDATE=!0;var ii=class extends Mn{constructor(){super(),this.isGroup=!0,this.type="Group"}},Zf={type:"move"},cr=class{constructor(){this._targetRay=null,this._grip=null,this._hand=null}getHandSpace(){return this._hand===null&&(this._hand=new ii,this._hand.matrixAutoUpdate=!1,this._hand.visible=!1,this._hand.joints={},this._hand.inputState={pinching:!1}),this._hand}getTargetRaySpace(){return this._targetRay===null&&(this._targetRay=new ii,this._targetRay.matrixAutoUpdate=!1,this._targetRay.visible=!1,this._targetRay.hasLinearVelocity=!1,this._targetRay.linearVelocity=new D,this._targetRay.hasAngularVelocity=!1,this._targetRay.angularVelocity=new D),this._targetRay}getGripSpace(){return this._grip===null&&(this._grip=new ii,this._grip.matrixAutoUpdate=!1,this._grip.visible=!1,this._grip.hasLinearVelocity=!1,this._grip.linearVelocity=new D,this._grip.hasAngularVelocity=!1,this._grip.angularVelocity=new D,this._grip.eventsEnabled=!1),this._grip}dispatchEvent(t){return this._targetRay!==null&&this._targetRay.dispatchEvent(t),this._grip!==null&&this._grip.dispatchEvent(t),this._hand!==null&&this._hand.dispatchEvent(t),this}connect(t){if(t&&t.hand){let e=this._hand;if(e)for(let n of t.hand.values())this._getHandJoint(e,n)}return this.dispatchEvent({type:"connected",data:t}),this}disconnect(t){return this.dispatchEvent({type:"disconnected",data:t}),this._targetRay!==null&&(this._targetRay.visible=!1),this._grip!==null&&(this._grip.visible=!1),this._hand!==null&&(this._hand.visible=!1),this}update(t,e,n){let s=null,r=null,a=null,o=this._targetRay,l=this._grip,c=this._hand;if(t&&e.session.visibilityState!=="visible-blurred"){if(c&&t.hand){a=!0;for(let S of t.hand.values()){let m=e.getJointPose(S,n),g=this._getHandJoint(c,S);m!==null&&(g.matrix.fromArray(m.transform.matrix),g.matrix.decompose(g.position,g.quaternion,g.scale),g.matrixWorldNeedsUpdate=!0,g.jointRadius=m.radius),g.visible=m!==null}let h=c.joints["index-finger-tip"],f=c.joints["thumb-tip"],d=h.position.distanceTo(f.position),p=.02,x=.005;c.inputState.pinching&&d>p+x?(c.inputState.pinching=!1,this.dispatchEvent({type:"pinchend",handedness:t.handedness,target:this})):!c.inputState.pinching&&d<=p-x&&(c.inputState.pinching=!0,this.dispatchEvent({type:"pinchstart",handedness:t.handedness,target:this}))}else l!==null&&t.gripSpace&&(r=e.getPose(t.gripSpace,n),r!==null&&(l.matrix.fromArray(r.transform.matrix),l.matrix.decompose(l.position,l.quaternion,l.scale),l.matrixWorldNeedsUpdate=!0,r.linearVelocity?(l.hasLinearVelocity=!0,l.linearVelocity.copy(r.linearVelocity)):l.hasLinearVelocity=!1,r.angularVelocity?(l.hasAngularVelocity=!0,l.angularVelocity.copy(r.angularVelocity)):l.hasAngularVelocity=!1,l.eventsEnabled&&l.dispatchEvent({type:"gripUpdated",data:t,target:this})));o!==null&&(s=e.getPose(t.targetRaySpace,n),s===null&&r!==null&&(s=r),s!==null&&(o.matrix.fromArray(s.transform.matrix),o.matrix.decompose(o.position,o.quaternion,o.scale),o.matrixWorldNeedsUpdate=!0,s.linearVelocity?(o.hasLinearVelocity=!0,o.linearVelocity.copy(s.linearVelocity)):o.hasLinearVelocity=!1,s.angularVelocity?(o.hasAngularVelocity=!0,o.angularVelocity.copy(s.angularVelocity)):o.hasAngularVelocity=!1,this.dispatchEvent(Zf)))}return o!==null&&(o.visible=s!==null),l!==null&&(l.visible=r!==null),c!==null&&(c.visible=a!==null),this}_getHandJoint(t,e){if(t.joints[e.jointName]===void 0){let n=new ii;n.matrixAutoUpdate=!1,n.visible=!1,t.joints[e.jointName]=n,t.add(n)}return t.joints[e.jointName]}},dd={aliceblue:15792383,antiquewhite:16444375,aqua:65535,aquamarine:8388564,azure:15794175,beige:16119260,bisque:16770244,black:0,blanchedalmond:16772045,blue:255,blueviolet:9055202,brown:10824234,burlywood:14596231,cadetblue:6266528,chartreuse:8388352,chocolate:13789470,coral:16744272,cornflowerblue:6591981,cornsilk:16775388,crimson:14423100,cyan:65535,darkblue:139,darkcyan:35723,darkgoldenrod:12092939,darkgray:11119017,darkgreen:25600,darkgrey:11119017,darkkhaki:12433259,darkmagenta:9109643,darkolivegreen:5597999,darkorange:16747520,darkorchid:10040012,darkred:9109504,darksalmon:15308410,darkseagreen:9419919,darkslateblue:4734347,darkslategray:3100495,darkslategrey:3100495,darkturquoise:52945,darkviolet:9699539,deeppink:16716947,deepskyblue:49151,dimgray:6908265,dimgrey:6908265,dodgerblue:2003199,firebrick:11674146,floralwhite:16775920,forestgreen:2263842,fuchsia:16711935,gainsboro:14474460,ghostwhite:16316671,gold:16766720,goldenrod:14329120,gray:8421504,green:32768,greenyellow:11403055,grey:8421504,honeydew:15794160,hotpink:16738740,indianred:13458524,indigo:4915330,ivory:16777200,khaki:15787660,lavender:15132410,lavenderblush:16773365,lawngreen:8190976,lemonchiffon:16775885,lightblue:11393254,lightcoral:15761536,lightcyan:14745599,lightgoldenrodyellow:16448210,lightgray:13882323,lightgreen:9498256,lightgrey:13882323,lightpink:16758465,lightsalmon:16752762,lightseagreen:2142890,lightskyblue:8900346,lightslategray:7833753,lightslategrey:7833753,lightsteelblue:11584734,lightyellow:16777184,lime:65280,limegreen:3329330,linen:16445670,magenta:16711935,maroon:8388608,mediumaquamarine:6737322,mediumblue:205,mediumorchid:12211667,mediumpurple:9662683,mediumseagreen:3978097,mediumslateblue:8087790,mediumspringgreen:64154,mediumturquoise:4772300,mediumvioletred:13047173,midnightblue:1644912,mintcream:16121850,mistyrose:16770273,moccasin:16770229,navajowhite:16768685,navy:128,oldlace:16643558,olive:8421376,olivedrab:7048739,orange:16753920,orangered:16729344,orchid:14315734,palegoldenrod:15657130,palegreen:10025880,paleturquoise:11529966,palevioletred:14381203,papayawhip:16773077,peachpuff:16767673,peru:13468991,pink:16761035,plum:14524637,powderblue:11591910,purple:8388736,rebeccapurple:6697881,red:16711680,rosybrown:12357519,royalblue:4286945,saddlebrown:9127187,salmon:16416882,sandybrown:16032864,seagreen:3050327,seashell:16774638,sienna:10506797,silver:12632256,skyblue:8900331,slateblue:6970061,slategray:7372944,slategrey:7372944,snow:16775930,springgreen:65407,steelblue:4620980,tan:13808780,teal:32896,thistle:14204888,tomato:16737095,turquoise:4251856,violet:15631086,wheat:16113331,white:16777215,whitesmoke:16119285,yellow:16776960,yellowgreen:10145074},ss={h:0,s:0,l:0},Oa={h:0,s:0,l:0};function lc(i,t,e){return e<0&&(e+=1),e>1&&(e-=1),e<1/6?i+(t-i)*6*e:e<1/2?t:e<2/3?i+(t-i)*6*(2/3-e):i}var fe=class{constructor(t,e,n){return this.isColor=!0,this.r=1,this.g=1,this.b=1,this.set(t,e,n)}set(t,e,n){if(e===void 0&&n===void 0){let s=t;s&&s.isColor?this.copy(s):typeof s=="number"?this.setHex(s):typeof s=="string"&&this.setStyle(s)}else this.setRGB(t,e,n);return this}setScalar(t){return this.r=t,this.g=t,this.b=t,this}setHex(t,e=fn){return t=Math.floor(t),this.r=(t>>16&255)/255,this.g=(t>>8&255)/255,this.b=(t&255)/255,be.colorSpaceToWorking(this,e),this}setRGB(t,e,n,s=be.workingColorSpace){return this.r=t,this.g=e,this.b=n,be.colorSpaceToWorking(this,s),this}setHSL(t,e,n,s=be.workingColorSpace){if(t=oh(t,1),e=ge(e,0,1),n=ge(n,0,1),e===0)this.r=this.g=this.b=n;else{let r=n<=.5?n*(1+e):n+e-n*e,a=2*n-r;this.r=lc(a,r,t+1/3),this.g=lc(a,r,t),this.b=lc(a,r,t-1/3)}return be.colorSpaceToWorking(this,s),this}setStyle(t,e=fn){function n(r){r!==void 0&&parseFloat(r)<1&&Kt("Color: Alpha component of "+t+" will be ignored.")}let s;if(s=/^(\w+)\(([^\)]*)\)/.exec(t)){let r,a=s[1],o=s[2];switch(a){case"rgb":case"rgba":if(r=/^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d+(?:\.\d+)?|\.\d+)\s*)?$/.exec(o))return n(r[4]),this.setRGB(Math.min(255,parseInt(r[1],10))/255,Math.min(255,parseInt(r[2],10))/255,Math.min(255,parseInt(r[3],10))/255,e);if(r=/^\s*(\d+(?:\.\d+)?|\.\d+)\%\s*,\s*(\d+(?:\.\d+)?|\.\d+)\%\s*,\s*(\d+(?:\.\d+)?|\.\d+)\%\s*(?:,\s*(\d+(?:\.\d+)?|\.\d+)\s*)?$/.exec(o))return n(r[4]),this.setRGB(Math.min(100,parseFloat(r[1]))/100,Math.min(100,parseFloat(r[2]))/100,Math.min(100,parseFloat(r[3]))/100,e);break;case"hsl":case"hsla":if(r=/^\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+))\s*,\s*(\d+(?:\.\d+)?|\.\d+)\%\s*,\s*(\d+(?:\.\d+)?|\.\d+)\%\s*(?:,\s*(\d+(?:\.\d+)?|\.\d+)\s*)?$/.exec(o))return n(r[4]),this.setHSL(parseFloat(r[1])/360,parseFloat(r[2])/100,parseFloat(r[3])/100,e);break;default:Kt("Color: Unknown color model "+t)}}else if(s=/^\#([A-Fa-f\d]+)$/.exec(t)){let r=s[1],a=r.length;if(a===3)return this.setRGB(parseInt(r.charAt(0),16)/15,parseInt(r.charAt(1),16)/15,parseInt(r.charAt(2),16)/15,e);if(a===6)return this.setHex(parseInt(r,16),e);Kt("Color: Invalid hex color "+t)}else if(t&&t.length>0)return this.setColorName(t,e);return this}setColorName(t,e=fn){let n=dd[t.toLowerCase()];return n!==void 0?this.setHex(n,e):Kt("Color: Unknown color "+t),this}clone(){return new this.constructor(this.r,this.g,this.b)}copy(t){return this.r=t.r,this.g=t.g,this.b=t.b,this}copySRGBToLinear(t){return this.r=ki(t.r),this.g=ki(t.g),this.b=ki(t.b),this}copyLinearToSRGB(t){return this.r=nr(t.r),this.g=nr(t.g),this.b=nr(t.b),this}convertSRGBToLinear(){return this.copySRGBToLinear(this),this}convertLinearToSRGB(){return this.copyLinearToSRGB(this),this}getHex(t=fn){return be.workingToColorSpace(Rn.copy(this),t),Math.round(ge(Rn.r*255,0,255))*65536+Math.round(ge(Rn.g*255,0,255))*256+Math.round(ge(Rn.b*255,0,255))}getHexString(t=fn){return("000000"+this.getHex(t).toString(16)).slice(-6)}getHSL(t,e=be.workingColorSpace){be.workingToColorSpace(Rn.copy(this),e);let n=Rn.r,s=Rn.g,r=Rn.b,a=Math.max(n,s,r),o=Math.min(n,s,r),l,c,h=(o+a)/2;if(o===a)l=0,c=0;else{let f=a-o;switch(c=h<=.5?f/(a+o):f/(2-a-o),a){case n:l=(s-r)/f+(s<r?6:0);break;case s:l=(r-n)/f+2;break;case r:l=(n-s)/f+4;break}l/=6}return t.h=l,t.s=c,t.l=h,t}getRGB(t,e=be.workingColorSpace){return be.workingToColorSpace(Rn.copy(this),e),t.r=Rn.r,t.g=Rn.g,t.b=Rn.b,t}getStyle(t=fn){be.workingToColorSpace(Rn.copy(this),t);let e=Rn.r,n=Rn.g,s=Rn.b;return t!==fn?`color(${t} ${e.toFixed(3)} ${n.toFixed(3)} ${s.toFixed(3)})`:`rgb(${Math.round(e*255)},${Math.round(n*255)},${Math.round(s*255)})`}offsetHSL(t,e,n){return this.getHSL(ss),this.setHSL(ss.h+t,ss.s+e,ss.l+n)}add(t){return this.r+=t.r,this.g+=t.g,this.b+=t.b,this}addColors(t,e){return this.r=t.r+e.r,this.g=t.g+e.g,this.b=t.b+e.b,this}addScalar(t){return this.r+=t,this.g+=t,this.b+=t,this}sub(t){return this.r=Math.max(0,this.r-t.r),this.g=Math.max(0,this.g-t.g),this.b=Math.max(0,this.b-t.b),this}multiply(t){return this.r*=t.r,this.g*=t.g,this.b*=t.b,this}multiplyScalar(t){return this.r*=t,this.g*=t,this.b*=t,this}lerp(t,e){return this.r+=(t.r-this.r)*e,this.g+=(t.g-this.g)*e,this.b+=(t.b-this.b)*e,this}lerpColors(t,e,n){return this.r=t.r+(e.r-t.r)*n,this.g=t.g+(e.g-t.g)*n,this.b=t.b+(e.b-t.b)*n,this}lerpHSL(t,e){this.getHSL(ss),t.getHSL(Oa);let n=Hr(ss.h,Oa.h,e),s=Hr(ss.s,Oa.s,e),r=Hr(ss.l,Oa.l,e);return this.setHSL(n,s,r),this}setFromVector3(t){return this.r=t.x,this.g=t.y,this.b=t.z,this}applyMatrix3(t){let e=this.r,n=this.g,s=this.b,r=t.elements;return this.r=r[0]*e+r[3]*n+r[6]*s,this.g=r[1]*e+r[4]*n+r[7]*s,this.b=r[2]*e+r[5]*n+r[8]*s,this}equals(t){return t.r===this.r&&t.g===this.g&&t.b===this.b}fromArray(t,e=0){return this.r=t[e],this.g=t[e+1],this.b=t[e+2],this}toArray(t=[],e=0){return t[e]=this.r,t[e+1]=this.g,t[e+2]=this.b,t}fromBufferAttribute(t,e){return this.r=t.getX(e),this.g=t.getY(e),this.b=t.getZ(e),this}toJSON(){return this.getHex()}*[Symbol.iterator](){yield this.r,yield this.g,yield this.b}},Rn=new fe;fe.NAMES=dd;var hr=class extends Mn{constructor(){super(),this.isScene=!0,this.type="Scene",this.background=null,this.environment=null,this.fog=null,this.backgroundBlurriness=0,this.backgroundIntensity=1,this.backgroundRotation=new Hi,this.environmentIntensity=1,this.environmentRotation=new Hi,this.overrideMaterial=null,typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}copy(t,e){return super.copy(t,e),this.background=t.background!==null?t.background.clone():null,this.environment=t.environment!==null?t.environment.clone():null,this.fog=t.fog!==null?t.fog.clone():null,this.backgroundBlurriness=t.backgroundBlurriness,this.backgroundIntensity=t.backgroundIntensity,this.backgroundRotation.copy(t.backgroundRotation),this.environmentIntensity=t.environmentIntensity,this.environmentRotation.copy(t.environmentRotation),this.overrideMaterial=t.overrideMaterial!==null?t.overrideMaterial.clone():null,this.matrixAutoUpdate=t.matrixAutoUpdate,this}toJSON(t){let e=super.toJSON(t);return this.fog!==null&&(e.object.fog=this.fog.toJSON()),e.object.backgroundBlurriness=this.backgroundBlurriness,e.object.backgroundIntensity=this.backgroundIntensity,e.object.backgroundRotation=this.backgroundRotation.toArray(),e.object.environmentIntensity=this.environmentIntensity,e.object.environmentRotation=this.environmentRotation.toArray(),e}},di=new D,Ui=new D,cc=new D,Fi=new D,Ys=new D,Zs=new D,cu=new D,hc=new D,uc=new D,dc=new D,fc=new je,pc=new je,mc=new je,ls=class i{constructor(t=new D,e=new D,n=new D){this.a=t,this.b=e,this.c=n}static getNormal(t,e,n,s){s.subVectors(n,e),di.subVectors(t,e),s.cross(di);let r=s.lengthSq();return r>0?s.multiplyScalar(1/Math.sqrt(r)):s.set(0,0,0)}static getBarycoord(t,e,n,s,r){di.subVectors(s,e),Ui.subVectors(n,e),cc.subVectors(t,e);let a=di.dot(di),o=di.dot(Ui),l=di.dot(cc),c=Ui.dot(Ui),h=Ui.dot(cc),f=a*c-o*o;if(f===0)return r.set(0,0,0),null;let d=1/f,p=(c*l-o*h)*d,x=(a*h-o*l)*d;return r.set(1-p-x,x,p)}static containsPoint(t,e,n,s){return this.getBarycoord(t,e,n,s,Fi)===null?!1:Fi.x>=0&&Fi.y>=0&&Fi.x+Fi.y<=1}static getInterpolation(t,e,n,s,r,a,o,l){return this.getBarycoord(t,e,n,s,Fi)===null?(l.x=0,l.y=0,"z"in l&&(l.z=0),"w"in l&&(l.w=0),null):(l.setScalar(0),l.addScaledVector(r,Fi.x),l.addScaledVector(a,Fi.y),l.addScaledVector(o,Fi.z),l)}static getInterpolatedAttribute(t,e,n,s,r,a){return fc.setScalar(0),pc.setScalar(0),mc.setScalar(0),fc.fromBufferAttribute(t,e),pc.fromBufferAttribute(t,n),mc.fromBufferAttribute(t,s),a.setScalar(0),a.addScaledVector(fc,r.x),a.addScaledVector(pc,r.y),a.addScaledVector(mc,r.z),a}static isFrontFacing(t,e,n,s){return di.subVectors(n,e),Ui.subVectors(t,e),di.cross(Ui).dot(s)<0}set(t,e,n){return this.a.copy(t),this.b.copy(e),this.c.copy(n),this}setFromPointsAndIndices(t,e,n,s){return this.a.copy(t[e]),this.b.copy(t[n]),this.c.copy(t[s]),this}setFromAttributeAndIndices(t,e,n,s){return this.a.fromBufferAttribute(t,e),this.b.fromBufferAttribute(t,n),this.c.fromBufferAttribute(t,s),this}clone(){return new this.constructor().copy(this)}copy(t){return this.a.copy(t.a),this.b.copy(t.b),this.c.copy(t.c),this}getArea(){return di.subVectors(this.c,this.b),Ui.subVectors(this.a,this.b),di.cross(Ui).length()*.5}getMidpoint(t){return t.addVectors(this.a,this.b).add(this.c).multiplyScalar(1/3)}getNormal(t){return i.getNormal(this.a,this.b,this.c,t)}getPlane(t){return t.setFromCoplanarPoints(this.a,this.b,this.c)}getBarycoord(t,e){return i.getBarycoord(t,this.a,this.b,this.c,e)}getInterpolation(t,e,n,s,r){return i.getInterpolation(t,this.a,this.b,this.c,e,n,s,r)}containsPoint(t){return i.containsPoint(t,this.a,this.b,this.c)}isFrontFacing(t){return i.isFrontFacing(this.a,this.b,this.c,t)}intersectsBox(t){return t.intersectsTriangle(this)}closestPointToPoint(t,e){let n=this.a,s=this.b,r=this.c,a,o;Ys.subVectors(s,n),Zs.subVectors(r,n),hc.subVectors(t,n);let l=Ys.dot(hc),c=Zs.dot(hc);if(l<=0&&c<=0)return e.copy(n);uc.subVectors(t,s);let h=Ys.dot(uc),f=Zs.dot(uc);if(h>=0&&f<=h)return e.copy(s);let d=l*f-h*c;if(d<=0&&l>=0&&h<=0&&l-h>0)return a=l/(l-h),e.copy(n).addScaledVector(Ys,a);dc.subVectors(t,r);let p=Ys.dot(dc),x=Zs.dot(dc);if(x>=0&&p<=x)return e.copy(r);let S=p*c-l*x;if(S<=0&&c>=0&&x<=0)return o=c/(c-x),e.copy(n).addScaledVector(Zs,o);let m=h*x-p*f;if(m<=0&&f-h>=0&&p-x>=0)return cu.subVectors(r,s),o=(f-h)/(f-h+(p-x)),e.copy(s).addScaledVector(cu,o);let g=1/(m+S+d);return a=S*g,o=d*g,e.copy(n).addScaledVector(Ys,a).addScaledVector(Zs,o)}equals(t){return t.a.equals(this.a)&&t.b.equals(this.b)&&t.c.equals(this.c)}},cs=class{constructor(t=new D(1/0,1/0,1/0),e=new D(-1/0,-1/0,-1/0)){this.isBox3=!0,this.min=t,this.max=e}set(t,e){return this.min.copy(t),this.max.copy(e),this}setFromArray(t){this.makeEmpty();for(let e=0,n=t.length;e<n;e+=3)this.expandByPoint(fi.fromArray(t,e));return this}setFromBufferAttribute(t){this.makeEmpty();for(let e=0,n=t.count;e<n;e++)this.expandByPoint(fi.fromBufferAttribute(t,e));return this}setFromPoints(t){this.makeEmpty();for(let e=0,n=t.length;e<n;e++)this.expandByPoint(t[e]);return this}setFromCenterAndSize(t,e){let n=fi.copy(e).multiplyScalar(.5);return this.min.copy(t).sub(n),this.max.copy(t).add(n),this}setFromObject(t,e=!1){return this.makeEmpty(),this.expandByObject(t,e)}clone(){return new this.constructor().copy(this)}copy(t){return this.min.copy(t.min),this.max.copy(t.max),this}makeEmpty(){return this.min.x=this.min.y=this.min.z=1/0,this.max.x=this.max.y=this.max.z=-1/0,this}isEmpty(){return this.max.x<this.min.x||this.max.y<this.min.y||this.max.z<this.min.z}getCenter(t){return this.isEmpty()?t.set(0,0,0):t.addVectors(this.min,this.max).multiplyScalar(.5)}getSize(t){return this.isEmpty()?t.set(0,0,0):t.subVectors(this.max,this.min)}expandByPoint(t){return this.min.min(t),this.max.max(t),this}expandByVector(t){return this.min.sub(t),this.max.add(t),this}expandByScalar(t){return this.min.addScalar(-t),this.max.addScalar(t),this}expandByObject(t,e=!1){t.updateWorldMatrix(!1,!1);let n=t.geometry;if(n!==void 0){let r=n.getAttribute("position");if(e===!0&&r!==void 0&&t.isInstancedMesh!==!0&&t.isBatchedMesh!==!0)for(let a=0,o=r.count;a<o;a++)t.isMesh===!0?t.getVertexPosition(a,fi):fi.fromBufferAttribute(r,a),fi.applyMatrix4(t.matrixWorld),this.expandByPoint(fi);else t.boundingBox!==void 0?(t.boundingBox===null&&t.computeBoundingBox(),Ba.copy(t.boundingBox)):(n.boundingBox===null&&n.computeBoundingBox(),Ba.copy(n.boundingBox)),Ba.applyMatrix4(t.matrixWorld),this.union(Ba)}let s=t.children;for(let r=0,a=s.length;r<a;r++)this.expandByObject(s[r],e);return this}containsPoint(t){return t.x>=this.min.x&&t.x<=this.max.x&&t.y>=this.min.y&&t.y<=this.max.y&&t.z>=this.min.z&&t.z<=this.max.z}containsBox(t){return this.min.x<=t.min.x&&t.max.x<=this.max.x&&this.min.y<=t.min.y&&t.max.y<=this.max.y&&this.min.z<=t.min.z&&t.max.z<=this.max.z}getParameter(t,e){return e.set((t.x-this.min.x)/(this.max.x-this.min.x),(t.y-this.min.y)/(this.max.y-this.min.y),(t.z-this.min.z)/(this.max.z-this.min.z))}intersectsBox(t){return t.max.x>=this.min.x&&t.min.x<=this.max.x&&t.max.y>=this.min.y&&t.min.y<=this.max.y&&t.max.z>=this.min.z&&t.min.z<=this.max.z}intersectsSphere(t){return this.clampPoint(t.center,fi),fi.distanceToSquared(t.center)<=t.radius*t.radius}intersectsPlane(t){let e,n;return t.normal.x>0?(e=t.normal.x*this.min.x,n=t.normal.x*this.max.x):(e=t.normal.x*this.max.x,n=t.normal.x*this.min.x),t.normal.y>0?(e+=t.normal.y*this.min.y,n+=t.normal.y*this.max.y):(e+=t.normal.y*this.max.y,n+=t.normal.y*this.min.y),t.normal.z>0?(e+=t.normal.z*this.min.z,n+=t.normal.z*this.max.z):(e+=t.normal.z*this.max.z,n+=t.normal.z*this.min.z),e<=-t.constant&&n>=-t.constant}intersectsTriangle(t){if(this.isEmpty())return!1;this.getCenter(Ur),ka.subVectors(this.max,Ur),Js.subVectors(t.a,Ur),Ks.subVectors(t.b,Ur),$s.subVectors(t.c,Ur),rs.subVectors(Ks,Js),as.subVectors($s,Ks),bs.subVectors(Js,$s);let e=[0,-rs.z,rs.y,0,-as.z,as.y,0,-bs.z,bs.y,rs.z,0,-rs.x,as.z,0,-as.x,bs.z,0,-bs.x,-rs.y,rs.x,0,-as.y,as.x,0,-bs.y,bs.x,0];return!gc(e,Js,Ks,$s,ka)||(e=[1,0,0,0,1,0,0,0,1],!gc(e,Js,Ks,$s,ka))?!1:(za.crossVectors(rs,as),e=[za.x,za.y,za.z],gc(e,Js,Ks,$s,ka))}clampPoint(t,e){return e.copy(t).clamp(this.min,this.max)}distanceToPoint(t){return this.clampPoint(t,fi).distanceTo(t)}getBoundingSphere(t){return this.isEmpty()?t.makeEmpty():(this.getCenter(t.center),t.radius=this.getSize(fi).length()*.5),t}intersect(t){return this.min.max(t.min),this.max.min(t.max),this.isEmpty()&&this.makeEmpty(),this}union(t){return this.min.min(t.min),this.max.max(t.max),this}applyMatrix4(t){return this.isEmpty()?this:(Oi[0].set(this.min.x,this.min.y,this.min.z).applyMatrix4(t),Oi[1].set(this.min.x,this.min.y,this.max.z).applyMatrix4(t),Oi[2].set(this.min.x,this.max.y,this.min.z).applyMatrix4(t),Oi[3].set(this.min.x,this.max.y,this.max.z).applyMatrix4(t),Oi[4].set(this.max.x,this.min.y,this.min.z).applyMatrix4(t),Oi[5].set(this.max.x,this.min.y,this.max.z).applyMatrix4(t),Oi[6].set(this.max.x,this.max.y,this.min.z).applyMatrix4(t),Oi[7].set(this.max.x,this.max.y,this.max.z).applyMatrix4(t),this.setFromPoints(Oi),this)}translate(t){return this.min.add(t),this.max.add(t),this}equals(t){return t.min.equals(this.min)&&t.max.equals(this.max)}toJSON(){return{min:this.min.toArray(),max:this.max.toArray()}}fromJSON(t){return this.min.fromArray(t.min),this.max.fromArray(t.max),this}},Oi=[new D,new D,new D,new D,new D,new D,new D,new D],fi=new D,Ba=new cs,Js=new D,Ks=new D,$s=new D,rs=new D,as=new D,bs=new D,Ur=new D,ka=new D,za=new D,Es=new D;function gc(i,t,e,n,s){for(let r=0,a=i.length-3;r<=a;r+=3){Es.fromArray(i,r);let o=s.x*Math.abs(Es.x)+s.y*Math.abs(Es.y)+s.z*Math.abs(Es.z),l=t.dot(Es),c=e.dot(Es),h=n.dot(Es);if(Math.max(-Math.max(l,c,h),Math.min(l,c,h))>o)return!1}return!0}var ln=new D,Ha=new kt,Jf=0,Ti=class extends pi{constructor(t,e,n=!1){if(super(),Array.isArray(t))throw new TypeError("THREE.BufferAttribute: array should be a Typed Array.");this.isBufferAttribute=!0,Object.defineProperty(this,"id",{value:Jf++}),this.name="",this.array=t,this.itemSize=e,this.count=t!==void 0?t.length/e:0,this.normalized=n,this.usage=rd,this.updateRanges=[],this.gpuType=_i,this.version=0,this._normalizationScale=t!==void 0?ch(t):void 0}onUploadCallback(){}set needsUpdate(t){t===!0&&this.version++}setUsage(t){return this.usage=t,this}addUpdateRange(t,e){this.updateRanges.push({start:t,count:e})}clearUpdateRanges(){this.updateRanges.length=0}copy(t){return this.name=t.name,this.array=new t.array.constructor(t.array),this.itemSize=t.itemSize,this.count=t.count,this.normalized=t.normalized,this.usage=t.usage,this.gpuType=t.gpuType,this._normalizationScale=t._normalizationScale,this}copyAt(t,e,n){t*=this.itemSize,n*=e.itemSize;for(let s=0,r=this.itemSize;s<r;s++)this.array[t+s]=e.array[n+s];return this}copyArray(t){return this.array.set(t),this}applyMatrix3(t){if(this.itemSize===2)for(let e=0,n=this.count;e<n;e++)Ha.fromBufferAttribute(this,e),Ha.applyMatrix3(t),this.setXY(e,Ha.x,Ha.y);else if(this.itemSize===3)for(let e=0,n=this.count;e<n;e++)ln.fromBufferAttribute(this,e),ln.applyMatrix3(t),this.setXYZ(e,ln.x,ln.y,ln.z);return this}applyMatrix4(t){for(let e=0,n=this.count;e<n;e++)ln.fromBufferAttribute(this,e),ln.applyMatrix4(t),this.setXYZ(e,ln.x,ln.y,ln.z);return this}applyNormalMatrix(t){for(let e=0,n=this.count;e<n;e++)ln.fromBufferAttribute(this,e),ln.applyNormalMatrix(t),this.setXYZ(e,ln.x,ln.y,ln.z);return this}transformDirection(t){for(let e=0,n=this.count;e<n;e++)ln.fromBufferAttribute(this,e),ln.transformDirection(t),this.setXYZ(e,ln.x,ln.y,ln.z);return this}set(t,e=0){return this.array.set(t,e),this}getComponent(t,e){let n=this.array[t*this.itemSize+e];return this.normalized&&(n=this._denormalize(n)),n}setComponent(t,e,n){return this.normalized&&(n=this._normalize(n)),this.array[t*this.itemSize+e]=n,this}getX(t){let e=this.array[t*this.itemSize];return this.normalized&&(e=this._denormalize(e)),e}setX(t,e){return this.normalized&&(e=this._normalize(e)),this.array[t*this.itemSize]=e,this}getY(t){let e=this.array[t*this.itemSize+1];return this.normalized&&(e=this._denormalize(e)),e}setY(t,e){return this.normalized&&(e=this._normalize(e)),this.array[t*this.itemSize+1]=e,this}getZ(t){let e=this.array[t*this.itemSize+2];return this.normalized&&(e=this._denormalize(e)),e}setZ(t,e){return this.normalized&&(e=this._normalize(e)),this.array[t*this.itemSize+2]=e,this}getW(t){let e=this.array[t*this.itemSize+3];return this.normalized&&(e=this._denormalize(e)),e}setW(t,e){return this.normalized&&(e=this._normalize(e)),this.array[t*this.itemSize+3]=e,this}setXY(t,e,n){return t*=this.itemSize,this.normalized&&(e=this._normalize(e),n=this._normalize(n)),this.array[t+0]=e,this.array[t+1]=n,this}setXYZ(t,e,n,s){return t*=this.itemSize,this.normalized&&(e=this._normalize(e),n=this._normalize(n),s=this._normalize(s)),this.array[t+0]=e,this.array[t+1]=n,this.array[t+2]=s,this}setXYZW(t,e,n,s,r){return t*=this.itemSize,this.normalized&&(e=this._normalize(e),n=this._normalize(n),s=this._normalize(s),r=this._normalize(r)),this.array[t+0]=e,this.array[t+1]=n,this.array[t+2]=s,this.array[t+3]=r,this}onUpload(t){return this.onUploadCallback=t,this}clone(){return new this.constructor(this.array,this.itemSize).copy(this)}toJSON(){let t={itemSize:this.itemSize,type:this.array.constructor.name,array:Array.from(this.array),normalized:this.normalized};return t.name=this.name,t.usage=this.usage,t.gpuType=this.gpuType,t}dispose(){this.dispatchEvent({type:"dispose"})}_denormalize(t){let e=this._normalizationScale;return e!==void 0?Math.max(t/e,-1):hd(t,this.array)}_normalize(t){let e=this._normalizationScale;return e!==void 0?Math.round(t*e):ud(t,this.array)}};var Jr=class extends Ti{constructor(t,e,n){super(new Uint16Array(t),e,n)}};var Kr=class extends Ti{constructor(t,e,n){super(new Uint32Array(t),e,n)}};var Be=class extends Ti{constructor(t,e,n){super(new Float32Array(t),e,n)}},Kf=new cs,Fr=new D,_c=new D,As=class{constructor(t=new D,e=-1){this.isSphere=!0,this.center=t,this.radius=e}set(t,e){return this.center.copy(t),this.radius=e,this}setFromPoints(t,e){let n=this.center;e!==void 0?n.copy(e):Kf.setFromPoints(t).getCenter(n);let s=0;for(let r=0,a=t.length;r<a;r++)s=Math.max(s,n.distanceToSquared(t[r]));return this.radius=Math.sqrt(s),this}copy(t){return this.center.copy(t.center),this.radius=t.radius,this}isEmpty(){return this.radius<0}makeEmpty(){return this.center.set(0,0,0),this.radius=-1,this}containsPoint(t){return t.distanceToSquared(this.center)<=this.radius*this.radius}distanceToPoint(t){return t.distanceTo(this.center)-this.radius}intersectsSphere(t){let e=this.radius+t.radius;return t.center.distanceToSquared(this.center)<=e*e}intersectsBox(t){return t.intersectsSphere(this)}intersectsPlane(t){return Math.abs(t.distanceToPoint(this.center))<=this.radius}clampPoint(t,e){let n=this.center.distanceToSquared(t);return e.copy(t),n>this.radius*this.radius&&(e.sub(this.center).normalize(),e.multiplyScalar(this.radius).add(this.center)),e}getBoundingBox(t){return this.isEmpty()?(t.makeEmpty(),t):(t.set(this.center,this.center),t.expandByScalar(this.radius),t)}applyMatrix4(t){return this.center.applyMatrix4(t),this.radius=this.radius*t.getMaxScaleOnAxis(),this}translate(t){return this.center.add(t),this}expandByPoint(t){if(this.isEmpty())return this.center.copy(t),this.radius=0,this;Fr.subVectors(t,this.center);let e=Fr.lengthSq();if(e>this.radius*this.radius){let n=Math.sqrt(e),s=(n-this.radius)*.5;this.center.addScaledVector(Fr,s/n),this.radius+=s}return this}union(t){return t.isEmpty()?this:this.isEmpty()?(this.copy(t),this):(this.center.equals(t.center)===!0?this.radius=Math.max(this.radius,t.radius):(_c.subVectors(t.center,this.center).setLength(t.radius),this.expandByPoint(Fr.copy(t.center).add(_c)),this.expandByPoint(Fr.copy(t.center).sub(_c))),this)}equals(t){return t.center.equals(this.center)&&t.radius===this.radius}clone(){return new this.constructor().copy(this)}toJSON(){return{radius:this.radius,center:this.center.toArray()}}fromJSON(t){return this.radius=t.radius,this.center.fromArray(t.center),this}},$f=0,ei=new Ge,xc=new Mn,js=new D,qn=new cs,Or=new cs,yn=new D,Sn=class i extends pi{constructor(){super(),this.isBufferGeometry=!0,Object.defineProperty(this,"id",{value:$f++}),this.uuid=vr(),this.name="",this.type="BufferGeometry",this.index=null,this.indirect=null,this.indirectOffset=0,this.attributes={},this.morphAttributes={},this.morphTargetsRelative=!1,this.groups=[],this.boundingBox=null,this.boundingSphere=null,this.drawRange={start:0,count:1/0},this.userData={},this._transformed=!1}getIndex(){return this.index}setIndex(t){return Array.isArray(t)?this.index=new(Sf(t)?Kr:Jr)(t,1):this.index=t,this}setIndirect(t,e=0){return this.indirect=t,this.indirectOffset=e,this}getIndirect(){return this.indirect}getAttribute(t){return this.attributes[t]}setAttribute(t,e){return this.attributes[t]=e,this}deleteAttribute(t){return delete this.attributes[t],this}hasAttribute(t){return this.attributes[t]!==void 0}addGroup(t,e,n=0){this.groups.push({start:t,count:e,materialIndex:n})}clearGroups(){this.groups=[]}setDrawRange(t,e){this.drawRange.start=t,this.drawRange.count=e}applyMatrix4(t){let e=this.attributes.position;e!==void 0&&(e.applyMatrix4(t),e.needsUpdate=!0);let n=this.attributes.normal;if(n!==void 0){let r=new ae().getNormalMatrix(t);n.applyNormalMatrix(r),n.needsUpdate=!0}let s=this.attributes.tangent;return s!==void 0&&(s.transformDirection(t),s.needsUpdate=!0),this.boundingBox!==null&&this.computeBoundingBox(),this.boundingSphere!==null&&this.computeBoundingSphere(),this._transformed=!0,this}applyQuaternion(t){return ei.makeRotationFromQuaternion(t),this.applyMatrix4(ei),this}rotateX(t){return ei.makeRotationX(t),this.applyMatrix4(ei),this}rotateY(t){return ei.makeRotationY(t),this.applyMatrix4(ei),this}rotateZ(t){return ei.makeRotationZ(t),this.applyMatrix4(ei),this}translate(t,e,n){return ei.makeTranslation(t,e,n),this.applyMatrix4(ei),this}scale(t,e,n){return ei.makeScale(t,e,n),this.applyMatrix4(ei),this}lookAt(t){return xc.lookAt(t),xc.updateMatrix(),this.applyMatrix4(xc.matrix),this}center(){return this.computeBoundingBox(),this.boundingBox.getCenter(js).negate(),this.translate(js.x,js.y,js.z),this}setFromPoints(t){let e=this.getAttribute("position");if(e===void 0){let n=[];for(let s=0,r=t.length;s<r;s++){let a=t[s];n.push(a.x,a.y,a.z||0)}this.setAttribute("position",new Be(n,3))}else{let n=Math.min(t.length,e.count);for(let s=0;s<n;s++){let r=t[s];e.setXYZ(s,r.x,r.y,r.z||0)}t.length>e.count&&Kt("BufferGeometry: Buffer size too small for points data. Use .dispose() and create a new geometry."),e.needsUpdate=!0}return this}computeBoundingBox(){this.boundingBox===null&&(this.boundingBox=new cs);let t=this.attributes.position,e=this.morphAttributes.position;if(t&&t.isGLBufferAttribute){ie("BufferGeometry.computeBoundingBox(): GLBufferAttribute requires a manual bounding box.",this),this.boundingBox.set(new D(-1/0,-1/0,-1/0),new D(1/0,1/0,1/0));return}if(t!==void 0){if(this.boundingBox.setFromBufferAttribute(t),e)for(let n=0,s=e.length;n<s;n++){let r=e[n];qn.setFromBufferAttribute(r),this.morphTargetsRelative?(yn.addVectors(this.boundingBox.min,qn.min),this.boundingBox.expandByPoint(yn),yn.addVectors(this.boundingBox.max,qn.max),this.boundingBox.expandByPoint(yn)):(this.boundingBox.expandByPoint(qn.min),this.boundingBox.expandByPoint(qn.max))}}else this.boundingBox.makeEmpty();(isNaN(this.boundingBox.min.x)||isNaN(this.boundingBox.min.y)||isNaN(this.boundingBox.min.z))&&ie('BufferGeometry.computeBoundingBox(): Computed min/max have NaN values. The "position" attribute is likely to have NaN values.',this)}computeBoundingSphere(){this.boundingSphere===null&&(this.boundingSphere=new As);let t=this.attributes.position,e=this.morphAttributes.position;if(t&&t.isGLBufferAttribute){ie("BufferGeometry.computeBoundingSphere(): GLBufferAttribute requires a manual bounding sphere.",this),this.boundingSphere.set(new D,1/0);return}if(t){let n=this.boundingSphere.center;if(qn.setFromBufferAttribute(t),e)for(let r=0,a=e.length;r<a;r++){let o=e[r];Or.setFromBufferAttribute(o),this.morphTargetsRelative?(yn.addVectors(qn.min,Or.min),qn.expandByPoint(yn),yn.addVectors(qn.max,Or.max),qn.expandByPoint(yn)):(qn.expandByPoint(Or.min),qn.expandByPoint(Or.max))}qn.getCenter(n);let s=0;for(let r=0,a=t.count;r<a;r++)yn.fromBufferAttribute(t,r),s=Math.max(s,n.distanceToSquared(yn));if(e)for(let r=0,a=e.length;r<a;r++){let o=e[r],l=this.morphTargetsRelative;for(let c=0,h=o.count;c<h;c++)yn.fromBufferAttribute(o,c),l&&(js.fromBufferAttribute(t,c),yn.add(js)),s=Math.max(s,n.distanceToSquared(yn))}this.boundingSphere.radius=Math.sqrt(s),isNaN(this.boundingSphere.radius)&&ie('BufferGeometry.computeBoundingSphere(): Computed radius is NaN. The "position" attribute is likely to have NaN values.',this)}}computeTangents(){let t=this.index,e=this.attributes;if(t===null||e.position===void 0||e.normal===void 0||e.uv===void 0){ie("BufferGeometry: .computeTangents() failed. Missing required attributes (index, position, normal or uv)");return}let n=e.position,s=e.normal,r=e.uv,a=this.getAttribute("tangent");(a===void 0||a.count!==n.count)&&(a=new Ti(new Float32Array(4*n.count),4),this.setAttribute("tangent",a));let o=[],l=[],c=new Uint8Array(n.count);for(let G=0;G<n.count;G++)o[G]=new D,l[G]=new D;let h=new D,f=new D,d=new D,p=new kt,x=new kt,S=new kt,m=new D,g=new D;function E(G,B,k){c[G]=c[B]=c[k]=1,h.fromBufferAttribute(n,G),f.fromBufferAttribute(n,B),d.fromBufferAttribute(n,k),p.fromBufferAttribute(r,G),x.fromBufferAttribute(r,B),S.fromBufferAttribute(r,k),f.sub(h),d.sub(h),x.sub(p),S.sub(p);let H=1/(x.x*S.y-S.x*x.y);isFinite(H)&&(m.copy(f).multiplyScalar(S.y).addScaledVector(d,-x.y).multiplyScalar(H),g.copy(d).multiplyScalar(x.x).addScaledVector(f,-S.x).multiplyScalar(H),o[G].add(m),o[B].add(m),o[k].add(m),l[G].add(g),l[B].add(g),l[k].add(g))}let P=this.groups;P.length===0&&(P=[{start:0,count:t.count}]);for(let G=0,B=P.length;G<B;++G){let k=P[G],H=k.start,K=k.count;for(let U=H,Y=H+K;U<Y;U+=3)E(t.getX(U+0),t.getX(U+1),t.getX(U+2))}let T=new D,C=new D,A=new D,_=new D;function b(G){A.fromBufferAttribute(s,G),_.copy(A);let B=o[G];T.copy(B),T.sub(A.multiplyScalar(A.dot(B))).normalize(),C.crossVectors(_,B);let H=C.dot(l[G])<0?-1:1;a.setXYZW(G,T.x,T.y,T.z,H)}for(let G=0,B=n.count;G<B;++G)c[G]&&b(G);this._transformed=!0}computeVertexNormals(){let t=this.index,e=this.getAttribute("position");if(e!==void 0){let n=this.getAttribute("normal");if(n===void 0||n.count!==e.count)n=new Ti(new Float32Array(e.count*3),3),this.setAttribute("normal",n);else for(let d=0,p=n.count;d<p;d++)n.setXYZ(d,0,0,0);let s=new D,r=new D,a=new D,o=new D,l=new D,c=new D,h=new D,f=new D;if(t)for(let d=0,p=t.count;d<p;d+=3){let x=t.getX(d+0),S=t.getX(d+1),m=t.getX(d+2);s.fromBufferAttribute(e,x),r.fromBufferAttribute(e,S),a.fromBufferAttribute(e,m),h.subVectors(a,r),f.subVectors(s,r),h.cross(f),o.fromBufferAttribute(n,x),l.fromBufferAttribute(n,S),c.fromBufferAttribute(n,m),o.add(h),l.add(h),c.add(h),n.setXYZ(x,o.x,o.y,o.z),n.setXYZ(S,l.x,l.y,l.z),n.setXYZ(m,c.x,c.y,c.z)}else for(let d=0,p=e.count;d<p;d+=3)s.fromBufferAttribute(e,d+0),r.fromBufferAttribute(e,d+1),a.fromBufferAttribute(e,d+2),h.subVectors(a,r),f.subVectors(s,r),h.cross(f),n.setXYZ(d+0,h.x,h.y,h.z),n.setXYZ(d+1,h.x,h.y,h.z),n.setXYZ(d+2,h.x,h.y,h.z);this.normalizeNormals(),n.needsUpdate=!0}}normalizeNormals(){let t=this.attributes.normal;for(let e=0,n=t.count;e<n;e++)yn.fromBufferAttribute(t,e),yn.normalize(),t.setXYZ(e,yn.x,yn.y,yn.z)}toNonIndexed(){function t(o,l){let c=o.array,h=o.itemSize,f=o.normalized,d=new c.constructor(l.length*h),p=0,x=0;for(let S=0,m=l.length;S<m;S++){o.isInterleavedBufferAttribute?p=l[S]*o.data.stride+o.offset:p=l[S]*h;for(let g=0;g<h;g++)d[x++]=c[p++]}return new Ti(d,h,f)}if(this.index===null)return Kt("BufferGeometry.toNonIndexed(): BufferGeometry is already non-indexed."),this;let e=new i,n=this.index.array,s=this.attributes;for(let o in s){let l=s[o],c=t(l,n);e.setAttribute(o,c)}let r=this.morphAttributes;for(let o in r){let l=[],c=r[o];for(let h=0,f=c.length;h<f;h++){let d=c[h],p=t(d,n);l.push(p)}e.morphAttributes[o]=l}e.morphTargetsRelative=this.morphTargetsRelative;let a=this.groups;for(let o=0,l=a.length;o<l;o++){let c=a[o];e.addGroup(c.start,c.count,c.materialIndex)}return e}toJSON(){let t={metadata:{version:4.7,type:"BufferGeometry",generator:"BufferGeometry.toJSON"}};if(t.uuid=this.uuid,t.type=this.parameters!==void 0&&this._transformed===!0?"BufferGeometry":this.type,t.name=this.name,Object.keys(this.userData).length>0&&(t.userData=this.userData),this.parameters!==void 0&&this._transformed!==!0){let l=this.parameters;for(let c in l)l[c]!==void 0&&(t[c]=l[c]);return t}t.data={attributes:{}};let e=this.index;e!==null&&(t.data.index={type:e.array.constructor.name,array:Array.prototype.slice.call(e.array)});let n=this.attributes;for(let l in n){let c=n[l];t.data.attributes[l]=c.toJSON(t.data)}let s={},r=!1;for(let l in this.morphAttributes){let c=this.morphAttributes[l],h=[];for(let f=0,d=c.length;f<d;f++){let p=c[f];h.push(p.toJSON(t.data))}h.length>0&&(s[l]=h,r=!0)}r&&(t.data.morphAttributes=s,t.data.morphTargetsRelative=this.morphTargetsRelative);let a=this.groups;a.length>0&&(t.data.groups=JSON.parse(JSON.stringify(a)));let o=this.boundingSphere;return o!==null&&(t.data.boundingSphere=o.toJSON()),t}clone(){return new this.constructor().copy(this)}copy(t){this.index=null,this.attributes={},this.morphAttributes={},this.groups=[],this.boundingBox=null,this.boundingSphere=null;let e={};this.name=t.name;let n=t.index;n!==null&&this.setIndex(n.clone());let s=t.attributes;for(let c in s){let h=s[c];this.setAttribute(c,h.clone(e))}let r=t.morphAttributes;for(let c in r){let h=[],f=r[c];for(let d=0,p=f.length;d<p;d++)h.push(f[d].clone(e));this.morphAttributes[c]=h}this.morphTargetsRelative=t.morphTargetsRelative;let a=t.groups;for(let c=0,h=a.length;c<h;c++){let f=a[c];this.addGroup(f.start,f.count,f.materialIndex)}let o=t.boundingBox;o!==null&&(this.boundingBox=o.clone());let l=t.boundingSphere;return l!==null&&(this.boundingSphere=l.clone()),this.drawRange.start=t.drawRange.start,this.drawRange.count=t.drawRange.count,this.userData=t.userData,this._transformed=t._transformed,this}dispose(){this.dispatchEvent({type:"dispose"})}};var yc=new D,jf=new D,Qf=new ae,Yn=class{constructor(t=new D(1,0,0),e=0){this.isPlane=!0,this.normal=t,this.constant=e}set(t,e){return this.normal.copy(t),this.constant=e,this}setComponents(t,e,n,s){return this.normal.set(t,e,n),this.constant=s,this}setFromNormalAndCoplanarPoint(t,e){return this.normal.copy(t),this.constant=-e.dot(this.normal),this}setFromCoplanarPoints(t,e,n){let s=yc.subVectors(n,e).cross(jf.subVectors(t,e)).normalize();return this.setFromNormalAndCoplanarPoint(s,t),this}copy(t){return this.normal.copy(t.normal),this.constant=t.constant,this}normalize(){let t=1/this.normal.length();return this.normal.multiplyScalar(t),this.constant*=t,this}negate(){return this.constant*=-1,this.normal.negate(),this}distanceToPoint(t){return this.normal.dot(t)+this.constant}distanceToSphere(t){return this.distanceToPoint(t.center)-t.radius}projectPoint(t,e){return e.copy(t).addScaledVector(this.normal,-this.distanceToPoint(t))}intersectLine(t,e,n=!0){let s=t.delta(yc),r=this.normal.dot(s);if(r===0)return this.distanceToPoint(t.start)===0?e.copy(t.start):null;let a=-(t.start.dot(this.normal)+this.constant)/r;return n===!0&&(a<0||a>1)?null:e.copy(t.start).addScaledVector(s,a)}intersectsLine(t){let e=this.distanceToPoint(t.start),n=this.distanceToPoint(t.end);return e<0&&n>0||n<0&&e>0}intersectsBox(t){return t.intersectsPlane(this)}intersectsSphere(t){return t.intersectsPlane(this)}coplanarPoint(t){return t.copy(this.normal).multiplyScalar(-this.constant)}applyMatrix4(t,e){let n=e||Qf.getNormalMatrix(t),s=this.coplanarPoint(yc).applyMatrix4(t),r=this.normal.applyMatrix3(n).normalize();return this.constant=-s.dot(r),this}translate(t){return this.constant-=t.dot(this.normal),this}equals(t){return t.normal.equals(this.normal)&&t.constant===this.constant}clone(){return new this.constructor().copy(this)}toJSON(){return{normal:this.normal.toArray(),constant:this.constant}}fromJSON(t){return this.normal.fromArray(t.normal),this.constant=t.constant,this}},tp=0,Gi=class extends pi{constructor(){super(),this.isMaterial=!0,Object.defineProperty(this,"id",{value:tp++}),this.uuid=vr(),this.name="",this.type="Material",this.blending=_r,this.side=_s,this.vertexColors=!1,this.opacity=1,this.transparent=!1,this.alphaHash=!1,this.blendSrc=kc,this.blendDst=zc,this.blendEquation=Is,this.blendSrcAlpha=null,this.blendDstAlpha=null,this.blendEquationAlpha=null,this.blendColor=new fe(0,0,0),this.blendAlpha=0,this.depthFunc=ir,this.depthTest=!0,this.depthWrite=!0,this.stencilWriteMask=255,this.stencilFunc=Qu,this.stencilRef=0,this.stencilFuncMask=255,this.stencilFail=so,this.stencilZFail=so,this.stencilZPass=so,this.stencilWrite=!1,this.clippingPlanes=null,this.clipIntersection=!1,this.clipShadows=!1,this.shadowSide=null,this.colorWrite=!0,this.precision=null,this.polygonOffset=!1,this.polygonOffsetFactor=0,this.polygonOffsetUnits=0,this.dithering=!1,this.alphaToCoverage=!1,this.premultipliedAlpha=!1,this.forceSinglePass=!1,this.allowOverride=!0,this.visible=!0,this.toneMapped=!0,this.userData={},this.version=0,this._alphaTest=0}get alphaTest(){return this._alphaTest}set alphaTest(t){this._alphaTest>0!=t>0&&this.version++,this._alphaTest=t}onBeforeRender(){}onBeforeCompile(){}customProgramCacheKey(){return this.onBeforeCompile.toString()}setValues(t){if(t!==void 0)for(let e in t){let n=t[e];if(n===void 0){Kt(`Material: parameter '${e}' has value of undefined.`);continue}let s=this[e];if(s===void 0){Kt(`Material: '${e}' is not a property of THREE.${this.type}.`);continue}s&&s.isColor?s.set(n):s&&s.isVector2&&n&&n.isVector2||s&&s.isEuler&&n&&n.isEuler||s&&s.isVector3&&n&&n.isVector3?s.copy(n):this[e]=n}}toJSON(t){let e=t===void 0||typeof t=="string";e&&(t={textures:{},images:{}});let n={metadata:{version:4.7,type:"Material",generator:"Material.toJSON"}};n.uuid=this.uuid,n.type=this.type,n.blending=this.blending,n.side=this.side,n.shadowSide=this.shadowSide,n.vertexColors=this.vertexColors,n.opacity=this.opacity,n.transparent=this.transparent,n.blendSrc=this.blendSrc,n.blendDst=this.blendDst,n.blendEquation=this.blendEquation,n.blendSrcAlpha=this.blendSrcAlpha,n.blendDstAlpha=this.blendDstAlpha,n.blendEquationAlpha=this.blendEquationAlpha,n.blendColor=this.blendColor.getHex(),n.blendAlpha=this.blendAlpha,n.depthFunc=this.depthFunc,n.depthTest=this.depthTest,n.depthWrite=this.depthWrite,n.colorWrite=this.colorWrite,n.clipIntersection=this.clipIntersection,n.clipShadows=this.clipShadows,n.stencilWriteMask=this.stencilWriteMask,n.stencilFunc=this.stencilFunc,n.stencilRef=this.stencilRef,n.stencilFuncMask=this.stencilFuncMask,n.stencilFail=this.stencilFail,n.stencilZFail=this.stencilZFail,n.stencilZPass=this.stencilZPass,n.stencilWrite=this.stencilWrite,n.polygonOffset=this.polygonOffset,n.polygonOffsetFactor=this.polygonOffsetFactor,n.polygonOffsetUnits=this.polygonOffsetUnits,n.dithering=this.dithering,n.alphaTest=this.alphaTest,n.alphaHash=this.alphaHash,n.alphaToCoverage=this.alphaToCoverage,n.premultipliedAlpha=this.premultipliedAlpha,n.forceSinglePass=this.forceSinglePass,n.allowOverride=this.allowOverride,n.visible=this.visible,n.toneMapped=this.toneMapped,n.name=this.name,this.color&&this.color.isColor&&(n.color=this.color.getHex()),this.roughness!==void 0&&(n.roughness=this.roughness),this.metalness!==void 0&&(n.metalness=this.metalness),this.sheen!==void 0&&(n.sheen=this.sheen),this.sheenColor&&this.sheenColor.isColor&&(n.sheenColor=this.sheenColor.getHex()),this.sheenRoughness!==void 0&&(n.sheenRoughness=this.sheenRoughness),this.emissive&&this.emissive.isColor&&(n.emissive=this.emissive.getHex()),this.emissiveIntensity!==void 0&&(n.emissiveIntensity=this.emissiveIntensity),this.specular&&this.specular.isColor&&(n.specular=this.specular.getHex()),this.specularIntensity!==void 0&&(n.specularIntensity=this.specularIntensity),this.specularColor&&this.specularColor.isColor&&(n.specularColor=this.specularColor.getHex()),this.shininess!==void 0&&(n.shininess=this.shininess),this.clearcoat!==void 0&&(n.clearcoat=this.clearcoat),this.clearcoatRoughness!==void 0&&(n.clearcoatRoughness=this.clearcoatRoughness),this.diffuseRoughness!==void 0&&(n.diffuseRoughness=this.diffuseRoughness),this.diffuseRoughnessMap&&this.diffuseRoughnessMap.isTexture&&(n.diffuseRoughnessMap=this.diffuseRoughnessMap.toJSON(t).uuid),this.clearcoatMap&&this.clearcoatMap.isTexture&&(n.clearcoatMap=this.clearcoatMap.toJSON(t).uuid),this.clearcoatRoughnessMap&&this.clearcoatRoughnessMap.isTexture&&(n.clearcoatRoughnessMap=this.clearcoatRoughnessMap.toJSON(t).uuid),this.clearcoatNormalMap&&this.clearcoatNormalMap.isTexture&&(n.clearcoatNormalMap=this.clearcoatNormalMap.toJSON(t).uuid,n.clearcoatNormalScale=this.clearcoatNormalScale.toArray()),this.sheenColorMap&&this.sheenColorMap.isTexture&&(n.sheenColorMap=this.sheenColorMap.toJSON(t).uuid),this.sheenRoughnessMap&&this.sheenRoughnessMap.isTexture&&(n.sheenRoughnessMap=this.sheenRoughnessMap.toJSON(t).uuid),this.dispersion!==void 0&&(n.dispersion=this.dispersion),this.retroreflectivity!==void 0&&(n.retroreflectivity=this.retroreflectivity),this.iridescence!==void 0&&(n.iridescence=this.iridescence),this.iridescenceIOR!==void 0&&(n.iridescenceIOR=this.iridescenceIOR),this.iridescenceThicknessMinimum!==void 0&&(n.iridescenceThicknessMinimum=this.iridescenceThicknessMinimum),this.iridescenceThicknessMaximum!==void 0&&(n.iridescenceThicknessMaximum=this.iridescenceThicknessMaximum),this.iridescenceMap&&this.iridescenceMap.isTexture&&(n.iridescenceMap=this.iridescenceMap.toJSON(t).uuid),this.iridescenceThicknessMap&&this.iridescenceThicknessMap.isTexture&&(n.iridescenceThicknessMap=this.iridescenceThicknessMap.toJSON(t).uuid),this.anisotropy!==void 0&&(n.anisotropy=this.anisotropy),this.anisotropyRotation!==void 0&&(n.anisotropyRotation=this.anisotropyRotation),this.anisotropyMap&&this.anisotropyMap.isTexture&&(n.anisotropyMap=this.anisotropyMap.toJSON(t).uuid),this.map&&this.map.isTexture&&(n.map=this.map.toJSON(t).uuid),this.matcap&&this.matcap.isTexture&&(n.matcap=this.matcap.toJSON(t).uuid),this.alphaMap&&this.alphaMap.isTexture&&(n.alphaMap=this.alphaMap.toJSON(t).uuid),this.lightMap&&this.lightMap.isTexture&&(n.lightMap=this.lightMap.toJSON(t).uuid,n.lightMapIntensity=this.lightMapIntensity),this.aoMap&&this.aoMap.isTexture&&(n.aoMap=this.aoMap.toJSON(t).uuid,n.aoMapIntensity=this.aoMapIntensity),this.bumpMap&&this.bumpMap.isTexture&&(n.bumpMap=this.bumpMap.toJSON(t).uuid,n.bumpScale=this.bumpScale),this.normalMap&&this.normalMap.isTexture&&(n.normalMap=this.normalMap.toJSON(t).uuid,n.normalMapType=this.normalMapType,n.normalScale=this.normalScale.toArray()),this.displacementMap&&this.displacementMap.isTexture&&(n.displacementMap=this.displacementMap.toJSON(t).uuid,n.displacementScale=this.displacementScale,n.displacementBias=this.displacementBias),this.roughnessMap&&this.roughnessMap.isTexture&&(n.roughnessMap=this.roughnessMap.toJSON(t).uuid),this.metalnessMap&&this.metalnessMap.isTexture&&(n.metalnessMap=this.metalnessMap.toJSON(t).uuid),this.emissiveMap&&this.emissiveMap.isTexture&&(n.emissiveMap=this.emissiveMap.toJSON(t).uuid),this.specularMap&&this.specularMap.isTexture&&(n.specularMap=this.specularMap.toJSON(t).uuid),this.specularIntensityMap&&this.specularIntensityMap.isTexture&&(n.specularIntensityMap=this.specularIntensityMap.toJSON(t).uuid),this.specularColorMap&&this.specularColorMap.isTexture&&(n.specularColorMap=this.specularColorMap.toJSON(t).uuid),this.envMap&&this.envMap.isTexture&&(n.envMap=this.envMap.toJSON(t).uuid,this.combine!==void 0&&(n.combine=this.combine)),this.envMapRotation!==void 0&&(n.envMapRotation=this.envMapRotation.toArray()),this.envMapIntensity!==void 0&&(n.envMapIntensity=this.envMapIntensity),this.reflectivity!==void 0&&(n.reflectivity=this.reflectivity),this.refractionRatio!==void 0&&(n.refractionRatio=this.refractionRatio),this.gradientMap&&this.gradientMap.isTexture&&(n.gradientMap=this.gradientMap.toJSON(t).uuid),this.transmission!==void 0&&(n.transmission=this.transmission),this.transmissionMap&&this.transmissionMap.isTexture&&(n.transmissionMap=this.transmissionMap.toJSON(t).uuid),this.thickness!==void 0&&(n.thickness=this.thickness),this.thicknessMap&&this.thicknessMap.isTexture&&(n.thicknessMap=this.thicknessMap.toJSON(t).uuid),this.attenuationDistance!==void 0&&(n.attenuationDistance=this.attenuationDistance),this.attenuationColor!==void 0&&(n.attenuationColor=this.attenuationColor.getHex()),this.size!==void 0&&(n.size=this.size),this.sizeAttenuation!==void 0&&(n.sizeAttenuation=this.sizeAttenuation),Array.isArray(this.clippingPlanes)&&this.clippingPlanes.length>0&&(n.clippingPlanes=this.clippingPlanes.map(r=>r.toJSON())),this.rotation!==void 0&&(n.rotation=this.rotation),this.depthPacking!==void 0&&(n.depthPacking=this.depthPacking),this.linewidth!==void 0&&(n.linewidth=this.linewidth),this.linecap!==void 0&&(n.linecap=this.linecap),this.linejoin!==void 0&&(n.linejoin=this.linejoin),this.dashSize!==void 0&&(n.dashSize=this.dashSize),this.gapSize!==void 0&&(n.gapSize=this.gapSize),this.scale!==void 0&&(n.scale=this.scale),this.wireframe!==void 0&&(n.wireframe=this.wireframe),this.wireframeLinewidth!==void 0&&(n.wireframeLinewidth=this.wireframeLinewidth),this.wireframeLinecap!==void 0&&(n.wireframeLinecap=this.wireframeLinecap),this.wireframeLinejoin!==void 0&&(n.wireframeLinejoin=this.wireframeLinejoin),this.flatShading!==void 0&&(n.flatShading=this.flatShading),this.fog!==void 0&&(n.fog=this.fog),Object.keys(this.userData).length>0&&(n.userData=this.userData);function s(r){let a=[];for(let o in r){let l=r[o];delete l.metadata,a.push(l)}return a}if(e){let r=s(t.textures),a=s(t.images);r.length>0&&(n.textures=r),a.length>0&&(n.images=a)}return n}fromJSON(t,e){if(t.uuid!==void 0&&(this.uuid=t.uuid),t.name!==void 0&&(this.name=t.name),t.color!==void 0&&this.color!==void 0&&this.color.setHex(t.color),t.roughness!==void 0&&(this.roughness=t.roughness),t.metalness!==void 0&&(this.metalness=t.metalness),t.sheen!==void 0&&(this.sheen=t.sheen),t.sheenColor!==void 0&&(this.sheenColor=new fe().setHex(t.sheenColor)),t.sheenRoughness!==void 0&&(this.sheenRoughness=t.sheenRoughness),t.emissive!==void 0&&this.emissive!==void 0&&this.emissive.setHex(t.emissive),t.specular!==void 0&&this.specular!==void 0&&this.specular.setHex(t.specular),t.specularIntensity!==void 0&&(this.specularIntensity=t.specularIntensity),t.specularColor!==void 0&&this.specularColor!==void 0&&this.specularColor.setHex(t.specularColor),t.shininess!==void 0&&(this.shininess=t.shininess),t.clearcoat!==void 0&&(this.clearcoat=t.clearcoat),t.clearcoatRoughness!==void 0&&(this.clearcoatRoughness=t.clearcoatRoughness),t.diffuseRoughness!==void 0&&(this.diffuseRoughness=t.diffuseRoughness),t.dispersion!==void 0&&(this.dispersion=t.dispersion),t.retroreflectivity!==void 0&&(this.retroreflectivity=t.retroreflectivity),t.iridescence!==void 0&&(this.iridescence=t.iridescence),t.iridescenceIOR!==void 0&&(this.iridescenceIOR=t.iridescenceIOR),t.iridescenceThicknessMinimum!==void 0&&(this.iridescenceThicknessMinimum=t.iridescenceThicknessMinimum),t.iridescenceThicknessMaximum!==void 0&&(this.iridescenceThicknessMaximum=t.iridescenceThicknessMaximum),t.iridescenceThicknessRange!==void 0&&(this.iridescenceThicknessMinimum=t.iridescenceThicknessRange[0],this.iridescenceThicknessMaximum=t.iridescenceThicknessRange[1]),t.transmission!==void 0&&(this.transmission=t.transmission),t.thickness!==void 0&&(this.thickness=t.thickness),t.attenuationDistance!==void 0&&(this.attenuationDistance=t.attenuationDistance),t.attenuationColor!==void 0&&this.attenuationColor!==void 0&&this.attenuationColor.setHex(t.attenuationColor),t.anisotropy!==void 0&&(this.anisotropy=t.anisotropy),t.anisotropyRotation!==void 0&&(this.anisotropyRotation=t.anisotropyRotation),t.fog!==void 0&&(this.fog=t.fog),t.flatShading!==void 0&&(this.flatShading=t.flatShading),t.blending!==void 0&&(this.blending=t.blending),t.combine!==void 0&&(this.combine=t.combine),t.side!==void 0&&(this.side=t.side),t.shadowSide!==void 0&&(this.shadowSide=t.shadowSide),t.opacity!==void 0&&(this.opacity=t.opacity),t.transparent!==void 0&&(this.transparent=t.transparent),t.alphaTest!==void 0&&(this.alphaTest=t.alphaTest),t.alphaHash!==void 0&&(this.alphaHash=t.alphaHash),t.depthFunc!==void 0&&(this.depthFunc=t.depthFunc),t.depthTest!==void 0&&(this.depthTest=t.depthTest),t.depthWrite!==void 0&&(this.depthWrite=t.depthWrite),t.colorWrite!==void 0&&(this.colorWrite=t.colorWrite),t.clippingPlanes!==void 0&&(this.clippingPlanes=t.clippingPlanes.map(n=>new Yn().fromJSON(n))),t.clipIntersection!==void 0&&(this.clipIntersection=t.clipIntersection),t.clipShadows!==void 0&&(this.clipShadows=t.clipShadows),t.depthPacking!==void 0&&(this.depthPacking=t.depthPacking),t.blendSrc!==void 0&&(this.blendSrc=t.blendSrc),t.blendDst!==void 0&&(this.blendDst=t.blendDst),t.blendEquation!==void 0&&(this.blendEquation=t.blendEquation),t.blendSrcAlpha!==void 0&&(this.blendSrcAlpha=t.blendSrcAlpha),t.blendDstAlpha!==void 0&&(this.blendDstAlpha=t.blendDstAlpha),t.blendEquationAlpha!==void 0&&(this.blendEquationAlpha=t.blendEquationAlpha),t.blendColor!==void 0&&this.blendColor!==void 0&&this.blendColor.setHex(t.blendColor),t.blendAlpha!==void 0&&(this.blendAlpha=t.blendAlpha),t.stencilWriteMask!==void 0&&(this.stencilWriteMask=t.stencilWriteMask),t.stencilFunc!==void 0&&(this.stencilFunc=t.stencilFunc),t.stencilRef!==void 0&&(this.stencilRef=t.stencilRef),t.stencilFuncMask!==void 0&&(this.stencilFuncMask=t.stencilFuncMask),t.stencilFail!==void 0&&(this.stencilFail=t.stencilFail),t.stencilZFail!==void 0&&(this.stencilZFail=t.stencilZFail),t.stencilZPass!==void 0&&(this.stencilZPass=t.stencilZPass),t.stencilWrite!==void 0&&(this.stencilWrite=t.stencilWrite),t.wireframe!==void 0&&(this.wireframe=t.wireframe),t.wireframeLinewidth!==void 0&&(this.wireframeLinewidth=t.wireframeLinewidth),t.wireframeLinecap!==void 0&&(this.wireframeLinecap=t.wireframeLinecap),t.wireframeLinejoin!==void 0&&(this.wireframeLinejoin=t.wireframeLinejoin),t.rotation!==void 0&&(this.rotation=t.rotation),t.linewidth!==void 0&&(this.linewidth=t.linewidth),t.linecap!==void 0&&(this.linecap=t.linecap),t.linejoin!==void 0&&(this.linejoin=t.linejoin),t.dashSize!==void 0&&(this.dashSize=t.dashSize),t.gapSize!==void 0&&(this.gapSize=t.gapSize),t.scale!==void 0&&(this.scale=t.scale),t.polygonOffset!==void 0&&(this.polygonOffset=t.polygonOffset),t.polygonOffsetFactor!==void 0&&(this.polygonOffsetFactor=t.polygonOffsetFactor),t.polygonOffsetUnits!==void 0&&(this.polygonOffsetUnits=t.polygonOffsetUnits),t.dithering!==void 0&&(this.dithering=t.dithering),t.alphaToCoverage!==void 0&&(this.alphaToCoverage=t.alphaToCoverage),t.premultipliedAlpha!==void 0&&(this.premultipliedAlpha=t.premultipliedAlpha),t.forceSinglePass!==void 0&&(this.forceSinglePass=t.forceSinglePass),t.allowOverride!==void 0&&(this.allowOverride=t.allowOverride),t.visible!==void 0&&(this.visible=t.visible),t.toneMapped!==void 0&&(this.toneMapped=t.toneMapped),t.userData!==void 0&&(this.userData=t.userData),t.vertexColors!==void 0&&(typeof t.vertexColors=="number"?this.vertexColors=t.vertexColors>0:this.vertexColors=t.vertexColors),t.size!==void 0&&(this.size=t.size),t.sizeAttenuation!==void 0&&(this.sizeAttenuation=t.sizeAttenuation),t.map!==void 0&&(this.map=e[t.map]||null),t.matcap!==void 0&&(this.matcap=e[t.matcap]||null),t.alphaMap!==void 0&&(this.alphaMap=e[t.alphaMap]||null),t.bumpMap!==void 0&&(this.bumpMap=e[t.bumpMap]||null),t.bumpScale!==void 0&&(this.bumpScale=t.bumpScale),t.normalMap!==void 0&&(this.normalMap=e[t.normalMap]||null),t.normalMapType!==void 0&&(this.normalMapType=t.normalMapType),t.normalScale!==void 0){let n=t.normalScale;Array.isArray(n)===!1&&(n=[n,n]),this.normalScale=new kt().fromArray(n)}return t.displacementMap!==void 0&&(this.displacementMap=e[t.displacementMap]||null),t.displacementScale!==void 0&&(this.displacementScale=t.displacementScale),t.displacementBias!==void 0&&(this.displacementBias=t.displacementBias),t.roughnessMap!==void 0&&(this.roughnessMap=e[t.roughnessMap]||null),t.metalnessMap!==void 0&&(this.metalnessMap=e[t.metalnessMap]||null),t.emissiveMap!==void 0&&(this.emissiveMap=e[t.emissiveMap]||null),t.emissiveIntensity!==void 0&&(this.emissiveIntensity=t.emissiveIntensity),t.specularMap!==void 0&&(this.specularMap=e[t.specularMap]||null),t.specularIntensityMap!==void 0&&(this.specularIntensityMap=e[t.specularIntensityMap]||null),t.specularColorMap!==void 0&&(this.specularColorMap=e[t.specularColorMap]||null),t.envMap!==void 0&&(this.envMap=e[t.envMap]||null),t.envMapRotation!==void 0&&this.envMapRotation.fromArray(t.envMapRotation),t.envMapIntensity!==void 0&&(this.envMapIntensity=t.envMapIntensity),t.reflectivity!==void 0&&(this.reflectivity=t.reflectivity),t.refractionRatio!==void 0&&(this.refractionRatio=t.refractionRatio),t.lightMap!==void 0&&(this.lightMap=e[t.lightMap]||null),t.lightMapIntensity!==void 0&&(this.lightMapIntensity=t.lightMapIntensity),t.aoMap!==void 0&&(this.aoMap=e[t.aoMap]||null),t.aoMapIntensity!==void 0&&(this.aoMapIntensity=t.aoMapIntensity),t.gradientMap!==void 0&&(this.gradientMap=e[t.gradientMap]||null),t.clearcoatMap!==void 0&&(this.clearcoatMap=e[t.clearcoatMap]||null),t.clearcoatRoughnessMap!==void 0&&(this.clearcoatRoughnessMap=e[t.clearcoatRoughnessMap]||null),t.clearcoatNormalMap!==void 0&&(this.clearcoatNormalMap=e[t.clearcoatNormalMap]||null),t.clearcoatNormalScale!==void 0&&(this.clearcoatNormalScale=new kt().fromArray(t.clearcoatNormalScale)),t.diffuseRoughnessMap!==void 0&&(this.diffuseRoughnessMap=e[t.diffuseRoughnessMap]||null),t.iridescenceMap!==void 0&&(this.iridescenceMap=e[t.iridescenceMap]||null),t.iridescenceThicknessMap!==void 0&&(this.iridescenceThicknessMap=e[t.iridescenceThicknessMap]||null),t.transmissionMap!==void 0&&(this.transmissionMap=e[t.transmissionMap]||null),t.thicknessMap!==void 0&&(this.thicknessMap=e[t.thicknessMap]||null),t.anisotropyMap!==void 0&&(this.anisotropyMap=e[t.anisotropyMap]||null),t.sheenColorMap!==void 0&&(this.sheenColorMap=e[t.sheenColorMap]||null),t.sheenRoughnessMap!==void 0&&(this.sheenRoughnessMap=e[t.sheenRoughnessMap]||null),this}clone(){return new this.constructor().copy(this)}copy(t){this.name=t.name,this.blending=t.blending,this.side=t.side,this.vertexColors=t.vertexColors,this.opacity=t.opacity,this.transparent=t.transparent,this.blendSrc=t.blendSrc,this.blendDst=t.blendDst,this.blendEquation=t.blendEquation,this.blendSrcAlpha=t.blendSrcAlpha,this.blendDstAlpha=t.blendDstAlpha,this.blendEquationAlpha=t.blendEquationAlpha,this.blendColor.copy(t.blendColor),this.blendAlpha=t.blendAlpha,this.depthFunc=t.depthFunc,this.depthTest=t.depthTest,this.depthWrite=t.depthWrite,this.stencilWriteMask=t.stencilWriteMask,this.stencilFunc=t.stencilFunc,this.stencilRef=t.stencilRef,this.stencilFuncMask=t.stencilFuncMask,this.stencilFail=t.stencilFail,this.stencilZFail=t.stencilZFail,this.stencilZPass=t.stencilZPass,this.stencilWrite=t.stencilWrite;let e=t.clippingPlanes,n=null;if(e!==null){let s=e.length;n=new Array(s);for(let r=0;r!==s;++r)n[r]=e[r].clone()}return this.clippingPlanes=n,this.clipIntersection=t.clipIntersection,this.clipShadows=t.clipShadows,this.shadowSide=t.shadowSide,this.colorWrite=t.colorWrite,this.precision=t.precision,this.polygonOffset=t.polygonOffset,this.polygonOffsetFactor=t.polygonOffsetFactor,this.polygonOffsetUnits=t.polygonOffsetUnits,this.dithering=t.dithering,this.alphaTest=t.alphaTest,this.alphaHash=t.alphaHash,this.alphaToCoverage=t.alphaToCoverage,this.premultipliedAlpha=t.premultipliedAlpha,this.forceSinglePass=t.forceSinglePass,this.allowOverride=t.allowOverride,this.visible=t.visible,this.toneMapped=t.toneMapped,this.userData=JSON.parse(JSON.stringify(t.userData)),this}dispose(){this.dispatchEvent({type:"dispose"})}set needsUpdate(t){t===!0&&this.version++}};var Bi=new D,vc=new D,Ga=new D,Va=new D,hs=class{constructor(t=new D,e=new D(0,0,-1)){this.origin=t,this.direction=e}set(t,e){return this.origin.copy(t),this.direction.copy(e),this}copy(t){return this.origin.copy(t.origin),this.direction.copy(t.direction),this}at(t,e){return e.copy(this.origin).addScaledVector(this.direction,t)}lookAt(t){return this.direction.copy(t).sub(this.origin).normalize(),this}recast(t){return this.origin.copy(this.at(t,Bi)),this}closestPointToPoint(t,e){e.subVectors(t,this.origin);let n=e.dot(this.direction);return n<0?e.copy(this.origin):e.copy(this.origin).addScaledVector(this.direction,n)}distanceToPoint(t){return Math.sqrt(this.distanceSqToPoint(t))}distanceSqToPoint(t){let e=Bi.subVectors(t,this.origin).dot(this.direction);return e<0?this.origin.distanceToSquared(t):(Bi.copy(this.origin).addScaledVector(this.direction,e),Bi.distanceToSquared(t))}distanceSqToSegment(t,e,n,s){vc.copy(t).add(e).multiplyScalar(.5),Ga.copy(e).sub(t).normalize(),Va.copy(this.origin).sub(vc);let r=t.distanceTo(e)*.5,a=-this.direction.dot(Ga),o=Va.dot(this.direction),l=-Va.dot(Ga),c=Va.lengthSq(),h=Math.abs(1-a*a),f,d,p,x;if(h>0)if(f=a*l-o,d=a*o-l,x=r*h,f>=0)if(d>=-x)if(d<=x){let S=1/h;f*=S,d*=S,p=f*(f+a*d+2*o)+d*(a*f+d+2*l)+c}else d=r,f=Math.max(0,-(a*d+o)),p=-f*f+d*(d+2*l)+c;else d=-r,f=Math.max(0,-(a*d+o)),p=-f*f+d*(d+2*l)+c;else d<=-x?(f=Math.max(0,-(-a*r+o)),d=f>0?-r:Math.min(Math.max(-r,-l),r),p=-f*f+d*(d+2*l)+c):d<=x?(f=0,d=Math.min(Math.max(-r,-l),r),p=d*(d+2*l)+c):(f=Math.max(0,-(a*r+o)),d=f>0?r:Math.min(Math.max(-r,-l),r),p=-f*f+d*(d+2*l)+c);else d=a>0?-r:r,f=Math.max(0,-(a*d+o)),p=-f*f+d*(d+2*l)+c;return n&&n.copy(this.origin).addScaledVector(this.direction,f),s&&s.copy(vc).addScaledVector(Ga,d),p}intersectSphere(t,e){if(t.radius<0)return null;Bi.subVectors(t.center,this.origin);let n=Bi.dot(this.direction),s=Bi.dot(Bi)-n*n,r=t.radius*t.radius;if(s>r)return null;let a=Math.sqrt(r-s),o=n-a,l=n+a;return l<0?null:o<0?this.at(l,e):this.at(o,e)}intersectsSphere(t){return t.radius<0?!1:this.distanceSqToPoint(t.center)<=t.radius*t.radius}distanceToPlane(t){let e=t.normal.dot(this.direction);if(e===0)return t.distanceToPoint(this.origin)===0?0:null;let n=-(this.origin.dot(t.normal)+t.constant)/e;return n>=0?n:null}intersectPlane(t,e){let n=this.distanceToPlane(t);return n===null?null:this.at(n,e)}intersectsPlane(t){let e=t.distanceToPoint(this.origin);return e===0||t.normal.dot(this.direction)*e<0}intersectBox(t,e){let n,s,r,a,o,l,c=1/this.direction.x,h=1/this.direction.y,f=1/this.direction.z,d=this.origin;return c>=0?(n=(t.min.x-d.x)*c,s=(t.max.x-d.x)*c):(n=(t.max.x-d.x)*c,s=(t.min.x-d.x)*c),h>=0?(r=(t.min.y-d.y)*h,a=(t.max.y-d.y)*h):(r=(t.max.y-d.y)*h,a=(t.min.y-d.y)*h),n>a||r>s||((r>n||isNaN(n))&&(n=r),(a<s||isNaN(s))&&(s=a),f>=0?(o=(t.min.z-d.z)*f,l=(t.max.z-d.z)*f):(o=(t.max.z-d.z)*f,l=(t.min.z-d.z)*f),n>l||o>s)||((o>n||n!==n)&&(n=o),(l<s||s!==s)&&(s=l),s<0)?null:this.at(n>=0?n:s,e)}intersectsBox(t){return this.intersectBox(t,Bi)!==null}intersectTriangle(t,e,n,s,r){let a=this.origin,o=this.direction,l=o.x,c=o.y,h=o.z,f=t.x-a.x,d=t.y-a.y,p=t.z-a.z,x=e.x-a.x,S=e.y-a.y,m=e.z-a.z,g=n.x-a.x,E=n.y-a.y,P=n.z-a.z,T=Math.abs(l),C=Math.abs(c),A=Math.abs(h),_,b,G,B,k,H,K,U,Y,tt,j,dt;if(T>=C&&T>=A?(G=l,H=f,Y=x,dt=g,l>=0?(_=c,b=h,B=d,k=p,K=S,U=m,tt=E,j=P):(_=h,b=c,B=p,k=d,K=m,U=S,tt=P,j=E)):C>=A?(G=c,H=d,Y=S,dt=E,c>=0?(_=h,b=l,B=p,k=f,K=m,U=x,tt=P,j=g):(_=l,b=h,B=f,k=p,K=x,U=m,tt=g,j=P)):(G=h,H=p,Y=m,dt=P,h>=0?(_=l,b=c,B=f,k=d,K=x,U=S,tt=g,j=E):(_=c,b=l,B=d,k=f,K=S,U=x,tt=E,j=g)),G===0)return null;let V=_/G,it=b/G,ft=1/G,Gt=B-V*H,ee=k-it*H,at=K-V*Y,It=U-it*Y,Ft=tt-V*dt,qt=j-it*dt,pt=Ft*It-qt*at,oe=Gt*qt-ee*Ft,$t=at*ee-It*Gt;if(s){if(pt<0||oe<0||$t<0)return null}else if((pt<0||oe<0||$t<0)&&(pt>0||oe>0||$t>0))return null;let zt=pt+oe+$t;if(zt===0)return null;let Se=ft*(pt*H+oe*Y+$t*dt);return(zt>0?Se<0:Se>0)?null:this.at(Se/zt,r)}applyMatrix4(t){return this.origin.applyMatrix4(t),this.direction.transformDirection(t),this}equals(t){return t.origin.equals(this.origin)&&t.direction.equals(this.direction)}clone(){return new this.constructor().copy(this)}},kn=class extends Gi{constructor(t){super(),this.isMeshBasicMaterial=!0,this.type="MeshBasicMaterial",this.color=new fe(16777215),this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.specularMap=null,this.alphaMap=null,this.envMap=null,this.envMapRotation=new Hi,this.combine=Hc,this.reflectivity=1,this.refractionRatio=.98,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.color.copy(t.color),this.map=t.map,this.lightMap=t.lightMap,this.lightMapIntensity=t.lightMapIntensity,this.aoMap=t.aoMap,this.aoMapIntensity=t.aoMapIntensity,this.specularMap=t.specularMap,this.alphaMap=t.alphaMap,this.envMap=t.envMap,this.envMapRotation.copy(t.envMapRotation),this.combine=t.combine,this.reflectivity=t.reflectivity,this.refractionRatio=t.refractionRatio,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.wireframeLinecap=t.wireframeLinecap,this.wireframeLinejoin=t.wireframeLinejoin,this.fog=t.fog,this}},hu=new Ge,Ts=new hs,Wa=new As,uu=new D,Xa=new D,qa=new D,Ya=new D,Mc=new D,Za=new D,du=new D,Ja=new D,Qt=class extends Mn{constructor(t=new Sn,e=new kn){super(),this.isMesh=!0,this.type="Mesh",this.geometry=t,this.material=e,this.morphTargetDictionary=void 0,this.morphTargetInfluences=void 0,this.count=1,this.updateMorphTargets()}copy(t,e){return super.copy(t,e),t.morphTargetInfluences!==void 0?this.morphTargetInfluences=t.morphTargetInfluences.slice():this.morphTargetInfluences=void 0,t.morphTargetDictionary!==void 0?this.morphTargetDictionary=Object.assign({},t.morphTargetDictionary):this.morphTargetDictionary=void 0,this.material=Array.isArray(t.material)?t.material.slice():t.material,this.geometry=t.geometry,this}updateMorphTargets(){let e=this.geometry.morphAttributes,n=Object.keys(e);if(n.length>0){let s=e[n[0]];if(s!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,a=s.length;r<a;r++){let o=s[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=r}}}}getVertexPosition(t,e){let n=this.geometry,s=n.attributes.position,r=n.morphAttributes.position,a=n.morphTargetsRelative;e.fromBufferAttribute(s,t);let o=this.morphTargetInfluences;if(r&&o){Za.set(0,0,0);for(let l=0,c=r.length;l<c;l++){let h=o[l],f=r[l];h!==0&&(Mc.fromBufferAttribute(f,t),a?Za.addScaledVector(Mc,h):Za.addScaledVector(Mc.sub(e),h))}e.add(Za)}return e}intersectsFrustum(t){return t.intersectsObject(this)}raycast(t,e){let n=this.geometry,s=this.material,r=this.matrixWorld;s!==void 0&&(n.boundingSphere===null&&n.computeBoundingSphere(),Wa.copy(n.boundingSphere),Wa.applyMatrix4(r),Ts.copy(t.ray).recast(t.near),!(Wa.containsPoint(Ts.origin)===!1&&(Ts.intersectSphere(Wa,uu)===null||Ts.origin.distanceToSquared(uu)>(t.far-t.near)**2))&&(hu.copy(r).invert(),Ts.copy(t.ray).applyMatrix4(hu),!(n.boundingBox!==null&&Ts.intersectsBox(n.boundingBox)===!1)&&this._computeIntersections(t,e,Ts)))}_computeIntersections(t,e,n){let s,r=this.geometry,a=this.material,o=r.index,l=r.attributes.position,c=r.attributes.uv,h=r.attributes.uv1,f=r.attributes.normal,d=r.groups,p=r.drawRange;if(o!==null)if(Array.isArray(a))for(let x=0,S=d.length;x<S;x++){let m=d[x],g=a[m.materialIndex],E=Math.max(m.start,p.start),P=Math.min(o.count,Math.min(m.start+m.count,p.start+p.count));for(let T=E,C=P;T<C;T+=3){let A=o.getX(T),_=o.getX(T+1),b=o.getX(T+2);s=Ka(this,g,t,n,c,h,f,A,_,b),s&&(s.faceIndex=Math.floor(T/3),s.face.materialIndex=m.materialIndex,e.push(s))}}else{let x=Math.max(0,p.start),S=Math.min(o.count,p.start+p.count);for(let m=x,g=S;m<g;m+=3){let E=o.getX(m),P=o.getX(m+1),T=o.getX(m+2);s=Ka(this,a,t,n,c,h,f,E,P,T),s&&(s.faceIndex=Math.floor(m/3),e.push(s))}}else if(l!==void 0)if(Array.isArray(a))for(let x=0,S=d.length;x<S;x++){let m=d[x],g=a[m.materialIndex],E=Math.max(m.start,p.start),P=Math.min(l.count,Math.min(m.start+m.count,p.start+p.count));for(let T=E,C=P;T<C;T+=3){let A=T,_=T+1,b=T+2;s=Ka(this,g,t,n,c,h,f,A,_,b),s&&(s.faceIndex=Math.floor(T/3),s.face.materialIndex=m.materialIndex,e.push(s))}}else{let x=Math.max(0,p.start),S=Math.min(l.count,p.start+p.count);for(let m=x,g=S;m<g;m+=3){let E=m,P=m+1,T=m+2;s=Ka(this,a,t,n,c,h,f,E,P,T),s&&(s.faceIndex=Math.floor(m/3),e.push(s))}}}};function ep(i,t,e,n,s,r,a,o){let l;if(t.side===vn?l=n.intersectTriangle(a,r,s,!0,o):l=n.intersectTriangle(s,r,a,t.side===_s,o),l===null)return null;Ja.copy(o),Ja.applyMatrix4(i.matrixWorld);let c=e.ray.origin.distanceTo(Ja);return c<e.near||c>e.far?null:{distance:c,point:Ja.clone(),object:i}}function Ka(i,t,e,n,s,r,a,o,l,c){i.getVertexPosition(o,Xa),i.getVertexPosition(l,qa),i.getVertexPosition(c,Ya);let h=ep(i,t,e,n,Xa,qa,Ya,du);if(h){let f=new D;ls.getBarycoord(du,Xa,qa,Ya,f),s&&(h.uv=ls.getInterpolatedAttribute(s,o,l,c,f,new kt)),r&&(h.uv1=ls.getInterpolatedAttribute(r,o,l,c,f,new kt)),a&&(h.normal=ls.getInterpolatedAttribute(a,o,l,c,f,new D),h.normal.dot(n.direction)>0&&h.normal.multiplyScalar(-1));let d={a:o,b:l,c,normal:new D,materialIndex:0};ls.getNormal(Xa,qa,Ya,d.normal),h.face=d,h.barycoord=f}return h}var yo=class extends Dn{constructor(t=null,e=1,n=1,s,r,a,o,l,c=cn,h=cn,f,d){super(null,a,o,l,c,h,s,r,f,d),this.isDataTexture=!0,this.image={data:t,width:e,height:n},this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}};var ws=new As,np=new kt(.5,.5),$a=new D,us=class{constructor(t=new Yn,e=new Yn,n=new Yn,s=new Yn,r=new Yn,a=new Yn){this.planes=[t,e,n,s,r,a]}set(t,e,n,s,r,a){let o=this.planes;return o[0].copy(t),o[1].copy(e),o[2].copy(n),o[3].copy(s),o[4].copy(r),o[5].copy(a),this}copy(t){let e=this.planes;for(let n=0;n<6;n++)e[n].copy(t.planes[n]);return this}setFromProjectionMatrix(t,e=ni,n=!1){let s=this.planes,r=t.elements,a=r[0],o=r[1],l=r[2],c=r[3],h=r[4],f=r[5],d=r[6],p=r[7],x=r[8],S=r[9],m=r[10],g=r[11],E=r[12],P=r[13],T=r[14],C=r[15];if(s[0].setComponents(c-a,p-h,g-x,C-E).normalize(),s[1].setComponents(c+a,p+h,g+x,C+E).normalize(),s[2].setComponents(c+o,p+f,g+S,C+P).normalize(),s[3].setComponents(c-o,p-f,g-S,C-P).normalize(),n)s[4].setComponents(l,d,m,T).normalize(),s[5].setComponents(c-l,p-d,g-m,C-T).normalize();else if(s[4].setComponents(c-l,p-d,g-m,C-T).normalize(),e===ni)s[5].setComponents(c+l,p+d,g+m,C+T).normalize();else if(e===sr)s[5].setComponents(l,d,m,T).normalize();else throw new Error("THREE.Frustum.setFromProjectionMatrix(): Invalid coordinate system: "+e);return this}intersectsObject(t){if(t.boundingSphere!==void 0)t.boundingSphere===null&&t.computeBoundingSphere(),ws.copy(t.boundingSphere).applyMatrix4(t.matrixWorld);else{let e=t.geometry;e.boundingSphere===null&&e.computeBoundingSphere(),ws.copy(e.boundingSphere).applyMatrix4(t.matrixWorld)}return this.intersectsSphere(ws)}intersectsSprite(t){ws.center.set(0,0,0);let e=np.distanceTo(t.center);return ws.radius=.7071067811865476+e,ws.applyMatrix4(t.matrixWorld),this.intersectsSphere(ws)}intersectsSphere(t){let e=this.planes,n=t.center,s=-t.radius;for(let r=0;r<6;r++)if(e[r].distanceToPoint(n)<s)return!1;return!0}intersectsBox(t){let e=this.planes;for(let n=0;n<6;n++){let s=e[n];if($a.x=s.normal.x>0?t.max.x:t.min.x,$a.y=s.normal.y>0?t.max.y:t.min.y,$a.z=s.normal.z>0?t.max.z:t.min.z,s.distanceToPoint($a)<0)return!1}return!0}containsPoint(t){let e=this.planes;for(let n=0;n<6;n++)if(e[n].distanceToPoint(t)<0)return!1;return!0}clone(){return new this.constructor().copy(this)}},fu=new Ge,vo=class i{constructor(){this.coordinateSystem=ni,this._frustums=[],this._count=0}setFromArrayCamera(t){let e=t.cameras,n=this._frustums;for(let s=0;s<e.length;s++){let r=e[s];fu.multiplyMatrices(r.projectionMatrix,r.matrixWorldInverse),n[s]===void 0&&(n[s]=new us),n[s].setFromProjectionMatrix(fu,r.coordinateSystem,r.reversedDepth)}return this._count=e.length,this}getFrustum(t){return this._frustums[t]}intersectsObject(t){let e=this._frustums;for(let n=0;n<this._count;n++)if(e[n].intersectsObject(t))return!0;return!1}intersectsSprite(t){let e=this._frustums;for(let n=0;n<this._count;n++)if(e[n].intersectsSprite(t))return!0;return!1}intersectsSphere(t){let e=this._frustums;for(let n=0;n<this._count;n++)if(e[n].intersectsSphere(t))return!0;return!1}intersectsBox(t){let e=this._frustums;for(let n=0;n<this._count;n++)if(e[n].intersectsBox(t))return!0;return!1}containsPoint(t){let e=this._frustums;for(let n=0;n<this._count;n++)if(e[n].containsPoint(t))return!0;return!1}copy(t){this.coordinateSystem=t.coordinateSystem;let e=this._frustums,n=t._frustums;for(let s=0;s<t._count;s++)e[s]===void 0&&(e[s]=new us),e[s].copy(n[s]);return this._count=t._count,this}clone(){return new i().copy(this)}};var ur=class extends Gi{constructor(t){super(),this.isLineBasicMaterial=!0,this.type="LineBasicMaterial",this.color=new fe(16777215),this.map=null,this.linewidth=1,this.linecap="round",this.linejoin="round",this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.color.copy(t.color),this.map=t.map,this.linewidth=t.linewidth,this.linecap=t.linecap,this.linejoin=t.linejoin,this.fog=t.fog,this}},Mo=new D,So=new D,pu=new Ge,Br=new hs,ja=new As,Sc=new D,mu=new D,$r=class extends Mn{constructor(t=new Sn,e=new ur){super(),this.isLine=!0,this.type="Line",this.geometry=t,this.material=e,this.morphTargetDictionary=void 0,this.morphTargetInfluences=void 0,this.updateMorphTargets()}copy(t,e){return super.copy(t,e),t.morphTargetInfluences!==void 0?this.morphTargetInfluences=t.morphTargetInfluences.slice():this.morphTargetInfluences=void 0,t.morphTargetDictionary!==void 0?this.morphTargetDictionary=Object.assign({},t.morphTargetDictionary):this.morphTargetDictionary=void 0,this.material=Array.isArray(t.material)?t.material.slice():t.material,this.geometry=t.geometry,this}computeLineDistances(){let t=this.geometry;if(t.index===null){let e=t.attributes.position,n=[0];for(let s=1,r=e.count;s<r;s++)Mo.fromBufferAttribute(e,s-1),So.fromBufferAttribute(e,s),n[s]=n[s-1],n[s]+=Mo.distanceTo(So);t.setAttribute("lineDistance",new Be(n,1))}else Kt("Line.computeLineDistances(): Computation only possible with non-indexed BufferGeometry.");return this}intersectsFrustum(t){return t.intersectsObject(this)}raycast(t,e){let n=this.geometry,s=this.matrixWorld,r=t.params.Line.threshold,a=n.drawRange;if(n.boundingSphere===null&&n.computeBoundingSphere(),ja.copy(n.boundingSphere),ja.applyMatrix4(s),ja.radius+=r,t.ray.intersectsSphere(ja)===!1)return;pu.copy(s).invert(),Br.copy(t.ray).applyMatrix4(pu);let o=r/((this.scale.x+this.scale.y+this.scale.z)/3),l=o*o,c=this.isLineSegments?2:1,h=n.index,d=n.attributes.position;if(h!==null){let p=Math.max(0,a.start),x=Math.min(h.count,a.start+a.count);for(let S=p,m=x-1;S<m;S+=c){let g=h.getX(S),E=h.getX(S+1),P=Qa(this,t,Br,l,g,E,S);P&&e.push(P)}if(this.isLineLoop){let S=h.getX(x-1),m=h.getX(p),g=Qa(this,t,Br,l,S,m,x-1);g&&e.push(g)}}else{let p=Math.max(0,a.start),x=Math.min(d.count,a.start+a.count);for(let S=p,m=x-1;S<m;S+=c){let g=Qa(this,t,Br,l,S,S+1,S);g&&e.push(g)}if(this.isLineLoop){let S=Qa(this,t,Br,l,x-1,p,x-1);S&&e.push(S)}}}updateMorphTargets(){let e=this.geometry.morphAttributes,n=Object.keys(e);if(n.length>0){let s=e[n[0]];if(s!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,a=s.length;r<a;r++){let o=s[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=r}}}}};function Qa(i,t,e,n,s,r,a){let o=i.geometry.attributes.position;if(Mo.fromBufferAttribute(o,s),So.fromBufferAttribute(o,r),e.distanceSqToSegment(Mo,So,Sc,mu)>n)return;Sc.applyMatrix4(i.matrixWorld);let c=t.ray.origin.distanceTo(Sc);if(!(c<t.near||c>t.far))return{distance:c,point:mu.clone().applyMatrix4(i.matrixWorld),index:a,face:null,faceIndex:null,barycoord:null,object:i}}var jr=class extends Dn{constructor(t=[],e=Ls,n,s,r,a,o,l,c,h){super(t,e,n,s,r,a,o,l,c,h),this.isCubeTexture=!0,this.flipY=!1}get images(){return this.image}set images(t){this.image=t}},wi=class extends Dn{constructor(t,e,n,s,r,a,o,l,c){super(t,e,n,s,r,a,o,l,c),this.isCanvasTexture=!0,this.needsUpdate=!0}};var Vi=class extends Dn{constructor(t,e,n=gi,s,r,a,o=cn,l=cn,c,h=zi,f=1){if(h!==zi&&h!==Yi)throw new Error("THREE.DepthTexture: format must be either THREE.DepthFormat or THREE.DepthStencilFormat");let d={width:t,height:e,depth:f};super(d,s,r,a,o,l,h,n,c),this.isDepthTexture=!0,this.flipY=!1,this.generateMipmaps=!1,this.compareFunction=null}copy(t){return super.copy(t),this.source=new or(Object.assign({},t.image)),this.compareFunction=t.compareFunction,this}toJSON(t){let e=super.toJSON(t);return e.compareFunction=this.compareFunction,e}},Qr=class extends Vi{constructor(t,e=gi,n=Ls,s,r,a=cn,o=cn,l,c=zi){let h={width:t,height:t,depth:1},f=[h,h,h,h,h,h];super(t,t,e,n,s,r,a,o,l,c),this.image=f,this.isCubeDepthTexture=!0,this.isCubeTexture=!0}get images(){return this.image}set images(t){this.image=t}},ta=class extends Dn{constructor(t=null){super(),this.sourceTexture=t,this.isExternalTexture=!0}copy(t){return super.copy(t),this.sourceTexture=t.sourceTexture,this}},mi=class i extends Sn{constructor(t=1,e=1,n=1,s=1,r=1,a=1){super(),this.type="BoxGeometry",this.parameters={width:t,height:e,depth:n,widthSegments:s,heightSegments:r,depthSegments:a};let o=this;s=Math.floor(s),r=Math.floor(r),a=Math.floor(a);let l=[],c=[],h=[],f=[],d=0,p=0;x("z","y","x",-1,-1,n,e,t,a,r,0),x("z","y","x",1,-1,n,e,-t,a,r,1),x("x","z","y",1,1,t,n,e,s,a,2),x("x","z","y",1,-1,t,n,-e,s,a,3),x("x","y","z",1,-1,t,e,n,s,r,4),x("x","y","z",-1,-1,t,e,-n,s,r,5),this.setIndex(l),this.setAttribute("position",new Be(c,3)),this.setAttribute("normal",new Be(h,3)),this.setAttribute("uv",new Be(f,2));function x(S,m,g,E,P,T,C,A,_,b,G){let B=T/_,k=C/b,H=T/2,K=C/2,U=A/2,Y=_+1,tt=b+1,j=0,dt=0,V=new D;for(let it=0;it<tt;it++){let ft=it*k-K;for(let Gt=0;Gt<Y;Gt++){let ee=Gt*B-H;V[S]=ee*E,V[m]=ft*P,V[g]=U,c.push(V.x,V.y,V.z),V[S]=0,V[m]=0,V[g]=A>0?1:-1,h.push(V.x,V.y,V.z),f.push(Gt/_),f.push(1-it/b),j+=1}}for(let it=0;it<b;it++)for(let ft=0;ft<_;ft++){let Gt=d+ft+Y*it,ee=d+ft+Y*(it+1),at=d+(ft+1)+Y*(it+1),It=d+(ft+1)+Y*it;l.push(Gt,ee,It),l.push(ee,at,It),dt+=6}o.addGroup(p,dt,G),p+=dt,d+=j}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.width,t.height,t.depth,t.widthSegments,t.heightSegments,t.depthSegments)}};var Ai=class i extends Sn{constructor(t=1,e=1,n=1,s=32,r=1,a=!1,o=0,l=Math.PI*2){super(),this.type="CylinderGeometry",this.parameters={radiusTop:t,radiusBottom:e,height:n,radialSegments:s,heightSegments:r,openEnded:a,thetaStart:o,thetaLength:l};let c=this;s=Math.floor(s),r=Math.floor(r);let h=[],f=[],d=[],p=[],x=0,S=[],m=n/2,g=0;E(),a===!1&&(t>0&&P(!0),e>0&&P(!1)),this.setIndex(h),this.setAttribute("position",new Be(f,3)),this.setAttribute("normal",new Be(d,3)),this.setAttribute("uv",new Be(p,2));function E(){let T=new D,C=new D,A=0,_=(e-t)/n;for(let b=0;b<=r;b++){let G=[],B=b/r,k=B*(e-t)+t;for(let H=0;H<=s;H++){let K=H/s,U=K*l+o,Y=Math.sin(U),tt=Math.cos(U);C.x=k*Y,C.y=-B*n+m,C.z=k*tt,f.push(C.x,C.y,C.z),T.set(Y,_,tt).normalize(),d.push(T.x,T.y,T.z),p.push(K,1-B),G.push(x++)}S.push(G)}for(let b=0;b<s;b++)for(let G=0;G<r;G++){let B=S[G][b],k=S[G+1][b],H=S[G+1][b+1],K=S[G][b+1];(t>0||G!==0)&&(h.push(B,k,K),A+=3),(e>0||G!==r-1)&&(h.push(k,H,K),A+=3)}c.addGroup(g,A,0),g+=A}function P(T){let C=x,A=new kt,_=new D,b=0,G=T===!0?t:e,B=T===!0?1:-1;for(let H=1;H<=s;H++)f.push(0,m*B,0),d.push(0,B,0),p.push(.5,.5),x++;let k=x;for(let H=0;H<=s;H++){let U=H/s*l+o,Y=Math.cos(U),tt=Math.sin(U);_.x=G*tt,_.y=m*B,_.z=G*Y,f.push(_.x,_.y,_.z),d.push(0,B,0),A.x=Y*.5+.5,A.y=tt*.5*B+.5,p.push(A.x,A.y),x++}for(let H=0;H<s;H++){let K=C+H,U=k+H;T===!0?h.push(U,U+1,K):h.push(U+1,U,K),b+=3}c.addGroup(g,b,T===!0?1:2),g+=b}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radiusTop,t.radiusBottom,t.height,t.radialSegments,t.heightSegments,t.openEnded,t.thetaStart,t.thetaLength)}};var si=class{constructor(){this.type="Curve",this.arcLengthDivisions=200,this.needsUpdate=!1,this.cacheArcLengths=null}getPoint(){Kt("Curve: .getPoint() not implemented.")}getPointAt(t,e){let n=this.getUtoTmapping(t);return this.getPoint(n,e)}getPoints(t=5){let e=[];for(let n=0;n<=t;n++)e.push(this.getPoint(n/t));return e}getSpacedPoints(t=5){let e=[];for(let n=0;n<=t;n++)e.push(this.getPointAt(n/t));return e}getLength(){let t=this.getLengths();return t[t.length-1]}getLengths(t=this.arcLengthDivisions){if(this.cacheArcLengths&&this.cacheArcLengths.length===t+1&&!this.needsUpdate)return this.cacheArcLengths;this.needsUpdate=!1;let e=[],n,s=this.getPoint(0),r=0;e.push(0);for(let a=1;a<=t;a++)n=this.getPoint(a/t),r+=n.distanceTo(s),e.push(r),s=n;return this.cacheArcLengths=e,e}updateArcLengths(){this.needsUpdate=!0,this.getLengths()}getUtoTmapping(t,e=null){let n=this.getLengths(),s=0,r=n.length,a;e?a=e:a=t*n[r-1];let o=0,l=r-1,c;for(;o<=l;)if(s=Math.floor(o+(l-o)/2),c=n[s]-a,c<0)o=s+1;else if(c>0)l=s-1;else{l=s;break}if(s=l,n[s]===a)return s/(r-1);let h=n[s],d=n[s+1]-h,p=(a-h)/d;return(s+p)/(r-1)}getTangent(t,e){let s=t-1e-4,r=t+1e-4;s<0&&(s=0),r>1&&(r=1);let a=this.getPoint(s),o=this.getPoint(r),l=e||(a.isVector2?new kt:new D);return l.copy(o).sub(a).normalize(),l}getTangentAt(t,e){let n=this.getUtoTmapping(t);return this.getTangent(n,e)}computeFrenetFrames(t,e=!1){let n=new D,s=[],r=[],a=[],o=new D,l=new Ge;for(let p=0;p<=t;p++){let x=p/t;s[p]=this.getTangentAt(x,new D)}r[0]=new D,a[0]=new D;let c=Number.MAX_VALUE,h=Math.abs(s[0].x),f=Math.abs(s[0].y),d=Math.abs(s[0].z);h<=c&&(c=h,n.set(1,0,0)),f<=c&&(c=f,n.set(0,1,0)),d<=c&&n.set(0,0,1),o.crossVectors(s[0],n).normalize(),r[0].crossVectors(s[0],o),a[0].crossVectors(s[0],r[0]);for(let p=1;p<=t;p++){if(r[p]=r[p-1].clone(),a[p]=a[p-1].clone(),o.crossVectors(s[p-1],s[p]),o.length()>Number.EPSILON){o.normalize();let x=Math.acos(ge(s[p-1].dot(s[p]),-1,1));r[p].applyMatrix4(l.makeRotationAxis(o,x))}a[p].crossVectors(s[p],r[p])}if(e===!0){let p=Math.acos(ge(r[0].dot(r[t]),-1,1));p/=t,s[0].dot(o.crossVectors(r[0],r[t]))>0&&(p=-p);for(let x=1;x<=t;x++)r[x].applyMatrix4(l.makeRotationAxis(s[x],p*x)),a[x].crossVectors(s[x],r[x])}return{tangents:s,normals:r,binormals:a}}clone(){return new this.constructor().copy(this)}copy(t){return this.arcLengthDivisions=t.arcLengthDivisions,this.cacheArcLengths=null,this}toJSON(){let t={metadata:{version:4.7,type:"Curve",generator:"Curve.toJSON"}};return t.arcLengthDivisions=this.arcLengthDivisions,t.type=this.type,t}fromJSON(t){return this.arcLengthDivisions=t.arcLengthDivisions,this.cacheArcLengths=null,this}},ea=class extends si{constructor(t=0,e=0,n=1,s=1,r=0,a=Math.PI*2,o=!1,l=0){super(),this.isEllipseCurve=!0,this.type="EllipseCurve",this.aX=t,this.aY=e,this.xRadius=n,this.yRadius=s,this.aStartAngle=r,this.aEndAngle=a,this.aClockwise=o,this.aRotation=l}getPoint(t,e=new kt){let n=e,s=Math.PI*2,r=this.aEndAngle-this.aStartAngle,a=Math.abs(r)<Number.EPSILON;for(;r<0;)r+=s;for(;r>s;)r-=s;r<Number.EPSILON&&(a?r=0:r=s),this.aClockwise===!0&&!a&&(r===s?r=-s:r=r-s);let o=this.aStartAngle+t*r,l=this.aX+this.xRadius*Math.cos(o),c=this.aY+this.yRadius*Math.sin(o);if(this.aRotation!==0){let h=Math.cos(this.aRotation),f=Math.sin(this.aRotation),d=l-this.aX,p=c-this.aY;l=d*h-p*f+this.aX,c=d*f+p*h+this.aY}return n.set(l,c)}copy(t){return super.copy(t),this.aX=t.aX,this.aY=t.aY,this.xRadius=t.xRadius,this.yRadius=t.yRadius,this.aStartAngle=t.aStartAngle,this.aEndAngle=t.aEndAngle,this.aClockwise=t.aClockwise,this.aRotation=t.aRotation,this}toJSON(){let t=super.toJSON();return t.aX=this.aX,t.aY=this.aY,t.xRadius=this.xRadius,t.yRadius=this.yRadius,t.aStartAngle=this.aStartAngle,t.aEndAngle=this.aEndAngle,t.aClockwise=this.aClockwise,t.aRotation=this.aRotation,t}fromJSON(t){return super.fromJSON(t),this.aX=t.aX,this.aY=t.aY,this.xRadius=t.xRadius,this.yRadius=t.yRadius,this.aStartAngle=t.aStartAngle,this.aEndAngle=t.aEndAngle,this.aClockwise=t.aClockwise,this.aRotation=t.aRotation,this}},bo=class extends ea{constructor(t,e,n,s,r,a){super(t,e,n,n,s,r,a),this.isArcCurve=!0,this.type="ArcCurve"}};function uh(){let i=0,t=0,e=0,n=0;function s(r,a,o,l){i=r,t=o,e=-3*r+3*a-2*o-l,n=2*r-2*a+o+l}return{initCatmullRom:function(r,a,o,l,c){s(a,o,c*(o-r),c*(l-a))},initNonuniformCatmullRom:function(r,a,o,l,c,h,f){let d=(a-r)/c-(o-r)/(c+h)+(o-a)/h,p=(o-a)/h-(l-a)/(h+f)+(l-o)/f;d*=h,p*=h,s(a,o,d,p)},calc:function(r){let a=r*r,o=a*r;return i+t*r+e*a+n*o}}}var gu=new D,_u=new D,bc=new uh,Ec=new uh,Tc=new uh,ri=class extends si{constructor(t=[],e=!1,n="centripetal",s=.5){super(),this.isCatmullRomCurve3=!0,this.type="CatmullRomCurve3",this.points=t,this.closed=e,this.curveType=n,this.tension=s}getPoint(t,e=new D){let n=e,s=this.points,r=s.length,a=(r-(this.closed?0:1))*t,o=Math.floor(a),l=a-o;this.closed?o+=o>0?0:(Math.floor(Math.abs(o)/r)+1)*r:l===0&&o===r-1&&(o=r-2,l=1);let c,h;this.closed||o>0?c=s[(o-1)%r]:(_u.subVectors(s[0],s[1]).add(s[0]),c=_u);let f=s[o%r],d=s[(o+1)%r];if(this.closed||o+2<r?h=s[(o+2)%r]:(gu.subVectors(s[r-1],s[r-2]).add(s[r-1]),h=gu),this.curveType==="centripetal"||this.curveType==="chordal"){let p=this.curveType==="chordal"?.5:.25,x=Math.pow(c.distanceToSquared(f),p),S=Math.pow(f.distanceToSquared(d),p),m=Math.pow(d.distanceToSquared(h),p);S<1e-4&&(S=1),x<1e-4&&(x=S),m<1e-4&&(m=S),bc.initNonuniformCatmullRom(c.x,f.x,d.x,h.x,x,S,m),Ec.initNonuniformCatmullRom(c.y,f.y,d.y,h.y,x,S,m),Tc.initNonuniformCatmullRom(c.z,f.z,d.z,h.z,x,S,m)}else this.curveType==="catmullrom"&&(bc.initCatmullRom(c.x,f.x,d.x,h.x,this.tension),Ec.initCatmullRom(c.y,f.y,d.y,h.y,this.tension),Tc.initCatmullRom(c.z,f.z,d.z,h.z,this.tension));return n.set(bc.calc(l),Ec.calc(l),Tc.calc(l)),n}copy(t){super.copy(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(s.clone())}return this.closed=t.closed,this.curveType=t.curveType,this.tension=t.tension,this}toJSON(){let t=super.toJSON();t.points=[];for(let e=0,n=this.points.length;e<n;e++){let s=this.points[e];t.points.push(s.toArray())}return t.closed=this.closed,t.curveType=this.curveType,t.tension=this.tension,t}fromJSON(t){super.fromJSON(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(new D().fromArray(s))}return this.closed=t.closed,this.curveType=t.curveType,this.tension=t.tension,this}};function xu(i,t,e,n,s){let r=(n-t)*.5,a=(s-e)*.5,o=i*i,l=i*o;return(2*e-2*n+r+a)*l+(-3*e+3*n-2*r-a)*o+r*i+e}function ip(i,t){let e=1-i;return e*e*t}function sp(i,t){return 2*(1-i)*i*t}function rp(i,t){return i*i*t}function Gr(i,t,e,n){return ip(i,t)+sp(i,e)+rp(i,n)}function ap(i,t){let e=1-i;return e*e*e*t}function op(i,t){let e=1-i;return 3*e*e*i*t}function lp(i,t){return 3*(1-i)*i*i*t}function cp(i,t){return i*i*i*t}function Vr(i,t,e,n,s){return ap(i,t)+op(i,e)+lp(i,n)+cp(i,s)}var Eo=class extends si{constructor(t=new kt,e=new kt,n=new kt,s=new kt){super(),this.isCubicBezierCurve=!0,this.type="CubicBezierCurve",this.v0=t,this.v1=e,this.v2=n,this.v3=s}getPoint(t,e=new kt){let n=e,s=this.v0,r=this.v1,a=this.v2,o=this.v3;return n.set(Vr(t,s.x,r.x,a.x,o.x),Vr(t,s.y,r.y,a.y,o.y)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this.v3.copy(t.v3),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t.v3=this.v3.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this.v3.fromArray(t.v3),this}},To=class extends si{constructor(t=new D,e=new D,n=new D,s=new D){super(),this.isCubicBezierCurve3=!0,this.type="CubicBezierCurve3",this.v0=t,this.v1=e,this.v2=n,this.v3=s}getPoint(t,e=new D){let n=e,s=this.v0,r=this.v1,a=this.v2,o=this.v3;return n.set(Vr(t,s.x,r.x,a.x,o.x),Vr(t,s.y,r.y,a.y,o.y),Vr(t,s.z,r.z,a.z,o.z)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this.v3.copy(t.v3),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t.v3=this.v3.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this.v3.fromArray(t.v3),this}},wo=class extends si{constructor(t=new kt,e=new kt){super(),this.isLineCurve=!0,this.type="LineCurve",this.v1=t,this.v2=e}getPoint(t,e=new kt){let n=e;return t===1?n.copy(this.v2):(n.copy(this.v2).sub(this.v1),n.multiplyScalar(t).add(this.v1)),n}getPointAt(t,e){return this.getPoint(t,e)}getTangent(t,e=new kt){return e.subVectors(this.v2,this.v1).normalize()}getTangentAt(t,e){return this.getTangent(t,e)}copy(t){return super.copy(t),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},Ao=class extends si{constructor(t=new D,e=new D){super(),this.isLineCurve3=!0,this.type="LineCurve3",this.v1=t,this.v2=e}getPoint(t,e=new D){let n=e;return t===1?n.copy(this.v2):(n.copy(this.v2).sub(this.v1),n.multiplyScalar(t).add(this.v1)),n}getPointAt(t,e){return this.getPoint(t,e)}getTangent(t,e=new D){return e.subVectors(this.v2,this.v1).normalize()}getTangentAt(t,e){return this.getTangent(t,e)}copy(t){return super.copy(t),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},Ro=class extends si{constructor(t=new kt,e=new kt,n=new kt){super(),this.isQuadraticBezierCurve=!0,this.type="QuadraticBezierCurve",this.v0=t,this.v1=e,this.v2=n}getPoint(t,e=new kt){let n=e,s=this.v0,r=this.v1,a=this.v2;return n.set(Gr(t,s.x,r.x,a.x),Gr(t,s.y,r.y,a.y)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},na=class extends si{constructor(t=new D,e=new D,n=new D){super(),this.isQuadraticBezierCurve3=!0,this.type="QuadraticBezierCurve3",this.v0=t,this.v1=e,this.v2=n}getPoint(t,e=new D){let n=e,s=this.v0,r=this.v1,a=this.v2;return n.set(Gr(t,s.x,r.x,a.x),Gr(t,s.y,r.y,a.y),Gr(t,s.z,r.z,a.z)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},Co=class extends si{constructor(t=[]){super(),this.isSplineCurve=!0,this.type="SplineCurve",this.points=t}getPoint(t,e=new kt){let n=e,s=this.points,r=(s.length-1)*t,a=Math.floor(r),o=r-a,l=s[a===0?a:a-1],c=s[a],h=s[a>s.length-2?s.length-1:a+1],f=s[a>s.length-3?s.length-1:a+2];return n.set(xu(o,l.x,c.x,h.x,f.x),xu(o,l.y,c.y,h.y,f.y)),n}copy(t){super.copy(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(s.clone())}return this}toJSON(){let t=super.toJSON();t.points=[];for(let e=0,n=this.points.length;e<n;e++){let s=this.points[e];t.points.push(s.toArray())}return t}fromJSON(t){super.fromJSON(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(new kt().fromArray(s))}return this}},hp=Object.freeze({__proto__:null,ArcCurve:bo,CatmullRomCurve3:ri,CubicBezierCurve:Eo,CubicBezierCurve3:To,EllipseCurve:ea,LineCurve:wo,LineCurve3:Ao,QuadraticBezierCurve:Ro,QuadraticBezierCurve3:na,SplineCurve:Co});var Wi=class i extends Sn{constructor(t=1,e=1,n=1,s=1){super(),this.type="PlaneGeometry",this.parameters={width:t,height:e,widthSegments:n,heightSegments:s};let r=t/2,a=e/2,o=Math.floor(n),l=Math.floor(s),c=o+1,h=l+1,f=t/o,d=e/l,p=[],x=[],S=[],m=[];for(let g=0;g<h;g++){let E=g*d-a;for(let P=0;P<c;P++){let T=P*f-r;x.push(T,-E,0),S.push(0,0,1),m.push(P/o),m.push(1-g/l)}}for(let g=0;g<l;g++)for(let E=0;E<o;E++){let P=E+c*g,T=E+c*(g+1),C=E+1+c*(g+1),A=E+1+c*g;p.push(P,T,A),p.push(T,C,A)}this.setIndex(p),this.setAttribute("position",new Be(x,3)),this.setAttribute("normal",new Be(S,3)),this.setAttribute("uv",new Be(m,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.width,t.height,t.widthSegments,t.heightSegments)}};var Xi=class i extends Sn{constructor(t=1,e=32,n=16,s=0,r=Math.PI*2,a=0,o=Math.PI){super(),this.type="SphereGeometry",this.parameters={radius:t,widthSegments:e,heightSegments:n,phiStart:s,phiLength:r,thetaStart:a,thetaLength:o},e=Math.max(3,Math.floor(e)),n=Math.max(2,Math.floor(n));let l=Math.min(a+o,Math.PI),c=0,h=[],f=new D,d=new D,p=[],x=[],S=[],m=[];for(let g=0;g<=n;g++){let E=[],P=g/n,T=a+P*o,C=t*Math.cos(T),A=Math.sqrt(t*t-C*C),_=0;g===0&&a===0?_=.5/e:g===n&&l===Math.PI&&(_=-.5/e);for(let b=0;b<=e;b++){let G=b/e,B=s+G*r;f.x=-A*Math.cos(B),f.y=C,f.z=A*Math.sin(B),x.push(f.x,f.y,f.z),d.copy(f).normalize(),S.push(d.x,d.y,d.z),m.push(G+_,1-P),E.push(c++)}h.push(E)}for(let g=0;g<n;g++)for(let E=0;E<e;E++){let P=h[g][E+1],T=h[g][E],C=h[g+1][E],A=h[g+1][E+1];(g!==0||a>0)&&p.push(P,T,A),(g!==n-1||l<Math.PI)&&p.push(T,C,A)}this.setIndex(p),this.setAttribute("position",new Be(x,3)),this.setAttribute("normal",new Be(S,3)),this.setAttribute("uv",new Be(m,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radius,t.widthSegments,t.heightSegments,t.phiStart,t.phiLength,t.thetaStart,t.thetaLength)}};var Rs=class i extends Sn{constructor(t=1,e=.4,n=12,s=48,r=Math.PI*2,a=0,o=Math.PI*2){super(),this.type="TorusGeometry",this.parameters={radius:t,tube:e,radialSegments:n,tubularSegments:s,arc:r,thetaStart:a,thetaLength:o},n=Math.floor(n),s=Math.floor(s);let l=[],c=[],h=[],f=[],d=new D,p=new D,x=new D;for(let S=0;S<=n;S++){let m=a+S/n*o;for(let g=0;g<=s;g++){let E=g/s*r;p.x=(t+e*Math.cos(m))*Math.cos(E),p.y=(t+e*Math.cos(m))*Math.sin(E),p.z=e*Math.sin(m),c.push(p.x,p.y,p.z),d.x=t*Math.cos(E),d.y=t*Math.sin(E),x.subVectors(p,d).normalize(),h.push(x.x,x.y,x.z),f.push(g/s),f.push(S/n)}}for(let S=1;S<=n;S++)for(let m=1;m<=s;m++){let g=(s+1)*S+m-1,E=(s+1)*(S-1)+m-1,P=(s+1)*(S-1)+m,T=(s+1)*S+m;l.push(g,E,T),l.push(E,P,T)}this.setIndex(l),this.setAttribute("position",new Be(c,3)),this.setAttribute("normal",new Be(h,3)),this.setAttribute("uv",new Be(f,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radius,t.tube,t.radialSegments,t.tubularSegments,t.arc,t.thetaStart,t.thetaLength)}};var Ri=class i extends Sn{constructor(t=new na(new D(-1,-1,0),new D(-1,1,0),new D(1,1,0)),e=64,n=1,s=8,r=!1){super(),this.type="TubeGeometry",this.parameters={path:t,tubularSegments:e,radius:n,radialSegments:s,closed:r};let a=t.computeFrenetFrames(e,r);this.tangents=a.tangents,this.normals=a.normals,this.binormals=a.binormals;let o=new D,l=new D,c=new kt,h=new D,f=[],d=[],p=[],x=[];S(),this.setIndex(x),this.setAttribute("position",new Be(f,3)),this.setAttribute("normal",new Be(d,3)),this.setAttribute("uv",new Be(p,2));function S(){for(let P=0;P<e;P++)m(P);m(r===!1?e:0),E(),g()}function m(P){h=t.getPointAt(P/e,h);let T=a.normals[P],C=a.binormals[P];for(let A=0;A<=s;A++){let _=A/s*Math.PI*2,b=Math.sin(_),G=-Math.cos(_);l.x=G*T.x+b*C.x,l.y=G*T.y+b*C.y,l.z=G*T.z+b*C.z,l.normalize(),d.push(l.x,l.y,l.z),o.x=h.x+n*l.x,o.y=h.y+n*l.y,o.z=h.z+n*l.z,f.push(o.x,o.y,o.z)}}function g(){for(let P=1;P<=e;P++)for(let T=1;T<=s;T++){let C=(s+1)*(P-1)+(T-1),A=(s+1)*P+(T-1),_=(s+1)*P+T,b=(s+1)*(P-1)+T;x.push(C,A,b),x.push(A,_,b)}}function E(){for(let P=0;P<=e;P++)for(let T=0;T<=s;T++)c.x=P/e,c.y=T/s,p.push(c.x,c.y)}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}toJSON(){let t=super.toJSON();return t.path=this.parameters.path.toJSON(),t}static fromJSON(t){return new i(new hp[t.path.type]().fromJSON(t.path),t.tubularSegments,t.radius,t.radialSegments,t.closed)}};function Ds(i){let t={};for(let e in i){t[e]={};for(let n in i[e]){let s=i[e][n];if(yu(s))s.isRenderTargetTexture?(Kt("UniformsUtils: Textures of render targets cannot be cloned via cloneUniforms() or mergeUniforms()."),t[e][n]=null):t[e][n]=s.clone();else if(Array.isArray(s))if(yu(s[0])){let r=[];for(let a=0,o=s.length;a<o;a++)r[a]=s[a].clone();t[e][n]=r}else t[e][n]=s.slice();else t[e][n]=s}}return t}function Cn(i){let t={};for(let e=0;e<i.length;e++){let n=Ds(i[e]);for(let s in n)t[s]=n[s]}return t}function yu(i){return i&&(i.isColor||i.isMatrix3||i.isMatrix4||i.isVector2||i.isVector3||i.isVector4||i.isTexture||i.isQuaternion)}function up(i){let t=[];for(let e=0;e<i.length;e++)t.push(i[e].clone());return t}function dh(i){let t=i.getRenderTarget();return t===null?i.outputColorSpace:t.isXRRenderTarget===!0?t.texture.colorSpace:be.workingColorSpace}var fd={clone:Ds,merge:Cn},dp=`void main() {
	gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}`,fp=`void main() {
	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0 );
}`,ai=class extends Gi{constructor(t){super(),this.isShaderMaterial=!0,this.type="ShaderMaterial",this.defines={},this.uniforms={},this.uniformsGroups=[],this.vertexShader=dp,this.fragmentShader=fp,this.linewidth=1,this.wireframe=!1,this.wireframeLinewidth=1,this.fog=!1,this.lights=!1,this.clipping=!1,this.forceSinglePass=!0,this.extensions={clipCullDistance:!1,multiDraw:!1},this.defaultAttributeValues={color:[1,1,1],uv:[0,0],uv1:[0,0]},this.index0AttributeName=void 0,this.uniformsNeedUpdate=!1,this.glslVersion=null,t!==void 0&&this.setValues(t)}copy(t){return super.copy(t),this.fragmentShader=t.fragmentShader,this.vertexShader=t.vertexShader,this.uniforms=Ds(t.uniforms),this.uniformsGroups=up(t.uniformsGroups),this.defines=Object.assign({},t.defines),this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.fog=t.fog,this.lights=t.lights,this.clipping=t.clipping,this.extensions=Object.assign({},t.extensions),this.glslVersion=t.glslVersion,this.defaultAttributeValues=Object.assign({},t.defaultAttributeValues),this.index0AttributeName=t.index0AttributeName,this.uniformsNeedUpdate=t.uniformsNeedUpdate,this}toJSON(t){let e=super.toJSON(t);e.glslVersion=this.glslVersion,e.uniforms={};for(let s in this.uniforms){let a=this.uniforms[s].value;a&&a.isTexture?e.uniforms[s]={type:"t",value:a.toJSON(t).uuid}:a&&a.isColor?e.uniforms[s]={type:"c",value:a.getHex()}:a&&a.isVector2?e.uniforms[s]={type:"v2",value:a.toArray()}:a&&a.isVector3?e.uniforms[s]={type:"v3",value:a.toArray()}:a&&a.isVector4?e.uniforms[s]={type:"v4",value:a.toArray()}:a&&a.isMatrix3?e.uniforms[s]={type:"m3",value:a.toArray()}:a&&a.isMatrix4?e.uniforms[s]={type:"m4",value:a.toArray()}:e.uniforms[s]={value:a}}Object.keys(this.defines).length>0&&(e.defines=this.defines),e.vertexShader=this.vertexShader,e.fragmentShader=this.fragmentShader,e.lights=this.lights,e.clipping=this.clipping;let n={};for(let s in this.extensions)this.extensions[s]===!0&&(n[s]=!0);return Object.keys(n).length>0&&(e.extensions=n),e}fromJSON(t,e){if(super.fromJSON(t,e),t.uniforms!==void 0)for(let n in t.uniforms){let s=t.uniforms[n];switch(this.uniforms[n]={},s.type){case"t":this.uniforms[n].value=e[s.value]||null;break;case"c":this.uniforms[n].value=new fe().setHex(s.value);break;case"v2":this.uniforms[n].value=new kt().fromArray(s.value);break;case"v3":this.uniforms[n].value=new D().fromArray(s.value);break;case"v4":this.uniforms[n].value=new je().fromArray(s.value);break;case"m3":this.uniforms[n].value=new ae().fromArray(s.value);break;case"m4":this.uniforms[n].value=new Ge().fromArray(s.value);break;default:this.uniforms[n].value=s.value}}if(t.defines!==void 0&&(this.defines=t.defines),t.vertexShader!==void 0&&(this.vertexShader=t.vertexShader),t.fragmentShader!==void 0&&(this.fragmentShader=t.fragmentShader),t.glslVersion!==void 0&&(this.glslVersion=t.glslVersion),t.extensions!==void 0)for(let n in t.extensions)this.extensions[n]=t.extensions[n];return t.lights!==void 0&&(this.lights=t.lights),t.clipping!==void 0&&(this.clipping=t.clipping),this}},Po=class extends ai{constructor(t){super(t),this.isRawShaderMaterial=!0,this.type="RawShaderMaterial"}},tn=class extends Gi{constructor(t){super(),this.isMeshStandardMaterial=!0,this.type="MeshStandardMaterial",this.defines={STANDARD:""},this.color=new fe(16777215),this.roughness=1,this.metalness=0,this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.emissive=new fe(0),this.emissiveIntensity=1,this.emissiveMap=null,this.bumpMap=null,this.bumpScale=1,this.normalMap=null,this.normalMapType=Ll,this.normalScale=new kt(1,1),this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.roughnessMap=null,this.metalnessMap=null,this.alphaMap=null,this.envMap=null,this.envMapRotation=new Hi,this.envMapIntensity=1,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.flatShading=!1,this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.defines={STANDARD:""},this.color.copy(t.color),this.roughness=t.roughness,this.metalness=t.metalness,this.map=t.map,this.lightMap=t.lightMap,this.lightMapIntensity=t.lightMapIntensity,this.aoMap=t.aoMap,this.aoMapIntensity=t.aoMapIntensity,this.emissive.copy(t.emissive),this.emissiveMap=t.emissiveMap,this.emissiveIntensity=t.emissiveIntensity,this.bumpMap=t.bumpMap,this.bumpScale=t.bumpScale,this.normalMap=t.normalMap,this.normalMapType=t.normalMapType,this.normalScale.copy(t.normalScale),this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this.roughnessMap=t.roughnessMap,this.metalnessMap=t.metalnessMap,this.alphaMap=t.alphaMap,this.envMap=t.envMap,this.envMapRotation.copy(t.envMapRotation),this.envMapIntensity=t.envMapIntensity,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.wireframeLinecap=t.wireframeLinecap,this.wireframeLinejoin=t.wireframeLinejoin,this.flatShading=t.flatShading,this.fog=t.fog,this}};var Io=class extends Gi{constructor(t){super(),this.isMeshDepthMaterial=!0,this.type="MeshDepthMaterial",this.depthPacking=$u,this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.wireframe=!1,this.wireframeLinewidth=1,this.setValues(t)}copy(t){return super.copy(t),this.depthPacking=t.depthPacking,this.map=t.map,this.alphaMap=t.alphaMap,this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this}},Lo=class extends Gi{constructor(t){super(),this.isMeshDistanceMaterial=!0,this.type="MeshDistanceMaterial",this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.setValues(t)}copy(t){return super.copy(t),this.map=t.map,this.alphaMap=t.alphaMap,this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this}};function Qs(i,t){return!i||i.constructor===t?i:typeof t.BYTES_PER_ELEMENT=="number"?new t(i):Array.prototype.slice.call(i)}function to(i){return i!==void 0&&i.inTangents!==void 0&&i.outTangents!==void 0}var ds=class{constructor(t,e,n,s){this.parameterPositions=t,this._cachedIndex=0,this.resultBuffer=s!==void 0?s:new e.constructor(n),this.sampleValues=e,this.valueSize=n,this.settings=null,this.DefaultSettings_={}}evaluate(t){let e=this.parameterPositions,n=this._cachedIndex,s=e[n],r=e[n-1];n:{t:{let a;e:{i:if(!(t<s)){for(let o=n+2;;){if(s===void 0){if(t<r)break i;return n=e.length,this._cachedIndex=n,this.copySampleValue_(n-1)}if(n===o)break;if(r=s,s=e[++n],t<s)break t}a=e.length;break e}if(!(t>=r)){let o=e[1];t<o&&(n=2,r=o);for(let l=n-2;;){if(r===void 0)return this._cachedIndex=0,this.copySampleValue_(0);if(n===l)break;if(s=r,r=e[--n-1],t>=r)break t}a=n,n=0;break e}break n}for(;n<a;){let o=n+a>>>1;t<e[o]?a=o:n=o+1}if(s=e[n],r=e[n-1],r===void 0)return this._cachedIndex=0,this.copySampleValue_(0);if(s===void 0)return n=e.length,this._cachedIndex=n,this.copySampleValue_(n-1)}this._cachedIndex=n,this.intervalChanged_(n,r,s)}return this.interpolate_(n,r,t,s)}getSettings_(){return this.settings||this.DefaultSettings_}copySampleValue_(t){let e=this.resultBuffer,n=this.sampleValues,s=this.valueSize,r=t*s;for(let a=0;a!==s;++a)e[a]=n[r+a];return e}interpolate_(){throw new Error("THREE.Interpolant: Call to abstract method.")}intervalChanged_(){}},No=class extends ds{constructor(t,e,n,s){super(t,e,n,s),this._weightPrev=-0,this._offsetPrev=-0,this._weightNext=-0,this._offsetNext=-0,this.DefaultSettings_={endingStart:Rc,endingEnd:Rc}}intervalChanged_(t,e,n){let s=this.parameterPositions,r=t-2,a=t+1,o=s[r],l=s[a];if(o===void 0)switch(this.getSettings_().endingStart){case Cc:r=t,o=2*e-n;break;case Pc:r=s.length-2,o=e+s[r]-s[r+1];break;default:r=t,o=n}if(l===void 0)switch(this.getSettings_().endingEnd){case Cc:a=t,l=2*n-e;break;case Pc:a=1,l=n+s[1]-s[0];break;default:a=t-1,l=e}let c=(n-e)*.5,h=this.valueSize;this._weightPrev=c/(e-o),this._weightNext=c/(l-n),this._offsetPrev=r*h,this._offsetNext=a*h}interpolate_(t,e,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=t*o,c=l-o,h=this._offsetPrev,f=this._offsetNext,d=this._weightPrev,p=this._weightNext,x=(n-e)/(s-e),S=x*x,m=S*x,g=-d*m+2*d*S-d*x,E=(1+d)*m+(-1.5-2*d)*S+(-.5+d)*x+1,P=(-1-p)*m+(1.5+p)*S+.5*x,T=p*m-p*S;for(let C=0;C!==o;++C)r[C]=g*a[h+C]+E*a[c+C]+P*a[l+C]+T*a[f+C];return r}},Do=class extends ds{constructor(t,e,n,s){super(t,e,n,s)}interpolate_(t,e,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=t*o,c=l-o,h=(n-e)/(s-e),f=1-h;for(let d=0;d!==o;++d)r[d]=a[c+d]*f+a[l+d]*h;return r}},Uo=class extends ds{constructor(t,e,n,s){super(t,e,n,s)}interpolate_(t){return this.copySampleValue_(t-1)}},Fo=class extends ds{interpolate_(t,e,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=t*o,c=l-o,h=this.inTangents,f=this.outTangents;if(!h||!f){let x=(n-e)/(s-e),S=1-x;for(let m=0;m!==o;++m)r[m]=a[c+m]*S+a[l+m]*x;return r}let d=o*2,p=t-1;for(let x=0;x!==o;++x){let S=a[c+x],m=a[l+x],g=p*d+x*2,E=f[g],P=f[g+1],T=t*d+x*2,C=h[T],A=h[T+1],_=mp(n,e,E,C,s);r[x]=pd(_,S,P,A,m)}return r}};function pd(i,t,e,n,s){let r=1-i;return r*r*r*t+3*r*r*i*e+3*r*i*i*n+i*i*i*s}function pp(i,t,e,n,s){let r=1-i;return 3*r*r*(e-t)+6*r*i*(n-e)+3*i*i*(s-n)}function mp(i,t,e,n,s){let r=(i-t)/(s-t);for(let a=0;a<8;a++){let o=pd(r,t,e,n,s)-i;if(Math.abs(o)<1e-10)break;let l=pp(r,t,e,n,s);if(Math.abs(l)<1e-10)break;r=Math.max(0,Math.min(1,r-o/l))}return r}var Jn=class{constructor(t,e,n,s){if(t===void 0)throw new Error("THREE.KeyframeTrack: track name is undefined");if(e===void 0||e.length===0)throw new Error("THREE.KeyframeTrack: no keyframes in track named "+t);this.name=t,this.times=Qs(e,this.TimeBufferType),this.values=Qs(n,this.ValueBufferType),this.setInterpolation(s||this.DefaultInterpolation)}static toJSON(t){let e=t.constructor,n;if(e.toJSON!==this.toJSON)n=e.toJSON(t);else{n={name:t.name,times:Qs(t.times,Array),values:Qs(t.values,Array)};let s=t.getInterpolation();s!==t.DefaultInterpolation&&(n.interpolation=s),to(t.settings)&&(n.settings={inTangents:Qs(t.settings.inTangents,Array),outTangents:Qs(t.settings.outTangents,Array)})}return n.type=t.ValueTypeName,n}InterpolantFactoryMethodDiscrete(t){return new Uo(this.times,this.values,this.getValueSize(),t)}InterpolantFactoryMethodLinear(t){return new Do(this.times,this.values,this.getValueSize(),t)}InterpolantFactoryMethodSmooth(t){return new No(this.times,this.values,this.getValueSize(),t)}InterpolantFactoryMethodBezier(t){let e=new Fo(this.times,this.values,this.getValueSize(),t);return this.settings&&(e.inTangents=this.settings.inTangents,e.outTangents=this.settings.outTangents),e}setInterpolation(t){let e;switch(t){case Wr:e=this.InterpolantFactoryMethodDiscrete;break;case mo:e=this.InterpolantFactoryMethodLinear;break;case io:e=this.InterpolantFactoryMethodSmooth;break;case Ac:e=this.InterpolantFactoryMethodBezier;break}if(e===void 0){let n="unsupported interpolation for "+this.ValueTypeName+" keyframe track named "+this.name;if(this.createInterpolant===void 0)if(t!==this.DefaultInterpolation)this.setInterpolation(this.DefaultInterpolation);else throw new Error(n);return Kt("KeyframeTrack:",n),this}return this.createInterpolant=e,this}getInterpolation(){switch(this.createInterpolant){case this.InterpolantFactoryMethodDiscrete:return Wr;case this.InterpolantFactoryMethodLinear:return mo;case this.InterpolantFactoryMethodSmooth:return io;case this.InterpolantFactoryMethodBezier:return Ac}}getValueSize(){return this.values.length/this.times.length}shift(t){if(t!==0){let e=this.times;for(let n=0,s=e.length;n!==s;++n)e[n]+=t;to(this.settings)&&(vu(this.settings.inTangents,t),vu(this.settings.outTangents,t))}return this}scale(t){if(t!==1){let e=this.times;for(let n=0,s=e.length;n!==s;++n)e[n]*=t;to(this.settings)&&(Mu(this.settings.inTangents,t),Mu(this.settings.outTangents,t))}return this}trim(t,e){let n=this.times,s=n.length,r=0,a=s-1;for(;r!==s&&n[r]<t;)++r;for(;a!==-1&&n[a]>e;)--a;if(++a,r!==0||a!==s){r>=a&&(a=Math.max(a,1),r=a-1);let o=this.getValueSize();this.times=n.slice(r,a),this.values=this.values.slice(r*o,a*o)}return this}validate(){let t=!0,e=this.getValueSize();e-Math.floor(e)!==0&&(ie("KeyframeTrack: Invalid value size in track.",this),t=!1);let n=this.times,s=this.values,r=n.length;r===0&&(ie("KeyframeTrack: Track is empty.",this),t=!1);let a=null;for(let o=0;o!==r;o++){let l=n[o];if(typeof l=="number"&&isNaN(l)){ie("KeyframeTrack: Time is not a valid number.",this,o,l),t=!1;break}if(a!==null&&a>l){ie("KeyframeTrack: Out of order keys.",this,o,l,a),t=!1;break}a=l}if(s!==void 0&&bf(s))for(let o=0,l=s.length;o!==l;++o){let c=s[o];if(isNaN(c)){ie("KeyframeTrack: Value is not a valid number.",this,o,c),t=!1;break}}return t}optimize(){let t=this.times.slice(),e=this.values.slice(),n=this.getValueSize(),s=this.getInterpolation()===io,r=t.length-1,a=1;for(let o=1;o<r;++o){let l=!1,c=t[o],h=t[o+1];if(c!==h&&(o!==1||c!==t[0]))if(s)l=!0;else{let f=o*n,d=f-n,p=f+n;for(let x=0;x!==n;++x){let S=e[f+x];if(S!==e[d+x]||S!==e[p+x]){l=!0;break}}}if(l){if(o!==a){t[a]=t[o];let f=o*n,d=a*n;for(let p=0;p!==n;++p)e[d+p]=e[f+p]}++a}}if(r>0){t[a]=t[r];for(let o=r*n,l=a*n,c=0;c!==n;++c)e[l+c]=e[o+c];++a}return a!==t.length?(this.times=t.slice(0,a),this.values=e.slice(0,a*n)):(this.times=t,this.values=e),this}clone(){let t=this.times.slice(),e=this.values.slice(),n=this.constructor,s=new n(this.name,t,e);return s.createInterpolant=this.createInterpolant,to(this.settings)&&(s.settings={inTangents:this.settings.inTangents.slice(),outTangents:this.settings.outTangents.slice()}),s}};function vu(i,t){for(let e=0,n=i.length;e!==n;e+=2)i[e]+=t}function Mu(i,t){for(let e=0,n=i.length;e!==n;e+=2)i[e]*=t}Jn.prototype.ValueTypeName="";Jn.prototype.TimeBufferType=Float32Array;Jn.prototype.ValueBufferType=Float32Array;Jn.prototype.DefaultInterpolation=mo;var fs=class extends Jn{constructor(t,e,n){super(t,e,n)}};fs.prototype.ValueTypeName="bool";fs.prototype.ValueBufferType=Array;fs.prototype.DefaultInterpolation=Wr;fs.prototype.InterpolantFactoryMethodLinear=void 0;fs.prototype.InterpolantFactoryMethodSmooth=void 0;var Oo=class extends Jn{constructor(t,e,n,s){super(t,e,n,s)}};Oo.prototype.ValueTypeName="color";var Bo=class extends Jn{constructor(t,e,n,s){super(t,e,n,s)}};Bo.prototype.ValueTypeName="number";var ko=class extends ds{constructor(t,e,n,s){super(t,e,n,s)}interpolate_(t,e,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=(n-e)/(s-e),c=t*o;for(let h=c+o;c!==h;c+=4)Nn.slerpFlat(r,0,a,c-o,a,c,l);return r}},ia=class extends Jn{constructor(t,e,n,s){super(t,e,n,s)}InterpolantFactoryMethodLinear(t){return new ko(this.times,this.values,this.getValueSize(),t)}};ia.prototype.ValueTypeName="quaternion";ia.prototype.InterpolantFactoryMethodSmooth=void 0;var ps=class extends Jn{constructor(t,e,n){super(t,e,n)}};ps.prototype.ValueTypeName="string";ps.prototype.ValueBufferType=Array;ps.prototype.DefaultInterpolation=Wr;ps.prototype.InterpolantFactoryMethodLinear=void 0;ps.prototype.InterpolantFactoryMethodSmooth=void 0;var zo=class extends Jn{constructor(t,e,n,s){super(t,e,n,s)}};zo.prototype.ValueTypeName="vector";var Ho=class{constructor(t,e,n){let s=this,r=!1,a=0,o=0,l,c=[];this.onStart=void 0,this.onLoad=t,this.onProgress=e,this.onError=n,this._abortController=null,this.itemStart=function(h){o++,r===!1&&s.onStart!==void 0&&s.onStart(h,a,o),r=!0},this.itemEnd=function(h){a++,s.onProgress!==void 0&&s.onProgress(h,a,o),a===o&&(r=!1,s.onLoad!==void 0&&s.onLoad())},this.itemError=function(h){s.onError!==void 0&&s.onError(h)},this.resolveURL=function(h){return h=h.normalize("NFC"),l?l(h):h},this.setURLModifier=function(h){return l=h,this},this.addHandler=function(h,f){return c.push(h,f),this},this.removeHandler=function(h){let f=c.indexOf(h);return f!==-1&&c.splice(f,2),this},this.getHandler=function(h){for(let f=0,d=c.length;f<d;f+=2){let p=c[f],x=c[f+1];if(p.global&&(p.lastIndex=0),p.test(h))return x}return null},this.abort=function(){return this.abortController.abort(),this._abortController=null,this}}get abortController(){return this._abortController||(this._abortController=new AbortController),this._abortController}},md=new Ho,Go=class{constructor(t){this.manager=t!==void 0?t:md,this.crossOrigin="anonymous",this.withCredentials=!1,this.path="",this.resourcePath="",this.requestHeader={},this.priority="auto",this.cache="default",typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}load(){}loadAsync(t,e){let n=this;return new Promise(function(s,r){n.load(t,s,e,r)})}parse(){}setCrossOrigin(t){return this.crossOrigin=t,this}setWithCredentials(t){return this.withCredentials=t,this}setPath(t){return this.path=t,this}setResourcePath(t){return this.resourcePath=t,this}setRequestHeader(t){return this.requestHeader=t,this}setPriority(t){return this.priority=t,this}setCache(t){return this.cache=t,this}abort(){return this}};Go.DEFAULT_MATERIAL_NAME="__DEFAULT";var sa=class extends Mn{static registerNode(t){this.prototype._lightNode=t}constructor(t,e=1){super(),this.isLight=!0,this.type="Light",this.color=new fe(t),this.intensity=e}copy(t,e){return super.copy(t,e),this.color.copy(t.color),this.intensity=t.intensity,this}toJSON(t){let e=super.toJSON(t);return e.object.color=this.color.getHex(),e.object.intensity=this.intensity,e}},dr=class extends sa{constructor(t,e,n){super(t,n),this.isHemisphereLight=!0,this.type="HemisphereLight",this.position.copy(Mn.DEFAULT_UP),this.updateMatrix(),this.groundColor=new fe(e)}copy(t,e){return super.copy(t,e),this.groundColor.copy(t.groundColor),this}toJSON(t){let e=super.toJSON(t);return e.object.groundColor=this.groundColor.getHex(),e}},wc=new Ge,Su=new D,bu=new D,Vo=class{constructor(t){this.camera=t,this.intensity=1,this.bias=0,this.biasNode=null,this.normalBias=0,this.radius=1,this.blurSamples=8,this.mapSize=new kt(512,512),this.mapType=Hn,this.map=null,this.mapPass=null,this.matrix=new Ge,this.autoUpdate=!0,this.needsUpdate=!1,this._frustum=new us,this._frameExtents=new kt(1,1),this._viewportCount=1,this._viewports=[new je(0,0,1,1)]}getViewportCount(){return this._viewportCount}getCamera(){return this.camera}getFrustum(){return this._frustum}updateMatrices(t){let e=this.camera;Su.setFromMatrixPosition(t.matrixWorld),e.position.copy(Su),bu.setFromMatrixPosition(t.target.matrixWorld),e.lookAt(bu),e.updateMatrixWorld(),this._updateMatrix(e,this.matrix,this._frustum)}_updateMatrix(t,e,n,s){wc.multiplyMatrices(t.projectionMatrix,t.matrixWorldInverse),n.setFromProjectionMatrix(wc,t.coordinateSystem,t.reversedDepth);let r=this._frameExtents,a=s?s.z/r.x:1,o=s?s.w/r.y:1,l=s?s.x/r.x:0,c=s?s.y/r.y:0;t.coordinateSystem===sr||t.reversedDepth?e.set(.5*a,0,0,.5*a+l,0,.5*o,0,.5*o+c,0,0,1,0,0,0,0,1):e.set(.5*a,0,0,.5*a+l,0,.5*o,0,.5*o+c,0,0,.5,.5,0,0,0,1),e.multiply(wc)}getViewport(t){return this._viewports[t]}getFrameExtents(){return this._frameExtents}dispose(){this.map&&this.map.dispose(),this.mapPass&&this.mapPass.dispose()}copy(t){return this.camera=t.camera.clone(),this.intensity=t.intensity,this.bias=t.bias,this.radius=t.radius,this.autoUpdate=t.autoUpdate,this.needsUpdate=t.needsUpdate,this.normalBias=t.normalBias,this.blurSamples=t.blurSamples,this.mapSize.copy(t.mapSize),this.mapType=t.mapType,this.biasNode=t.biasNode,this}clone(){return new this.constructor().copy(this)}toJSON(){let t={};return t.intensity=this.intensity,t.bias=this.bias,t.normalBias=this.normalBias,t.radius=this.radius,t.blurSamples=this.blurSamples,t.mapSize=this.mapSize.toArray(),t.mapType=this.mapType,t.camera=this.camera.toJSON(!1).object,delete t.camera.matrix,t}},eo=new D,no=new Nn,bi=new D,ra=class extends Mn{constructor(){super(),this.isCamera=!0,this.type="Camera",this.matrixWorldInverse=new Ge,this.projectionMatrix=new Ge,this.projectionMatrixInverse=new Ge,this.coordinateSystem=ni,this._reversedDepth=!1}get reversedDepth(){return this._reversedDepth}copy(t,e){return super.copy(t,e),this.matrixWorldInverse.copy(t.matrixWorldInverse),this.projectionMatrix.copy(t.projectionMatrix),this.projectionMatrixInverse.copy(t.projectionMatrixInverse),this.coordinateSystem=t.coordinateSystem,this}getWorldDirection(t){return super.getWorldDirection(t).negate()}updateMatrixWorld(t){super.updateMatrixWorld(t),this.matrixWorld.decompose(eo,no,bi),bi.x===1&&bi.y===1&&bi.z===1?this.matrixWorldInverse.copy(this.matrixWorld).invert():this.matrixWorldInverse.compose(eo,no,bi.set(1,1,1)).invert()}updateWorldMatrix(t,e,n=!1){super.updateWorldMatrix(t,e,n),this.matrixWorld.decompose(eo,no,bi),bi.x===1&&bi.y===1&&bi.z===1?this.matrixWorldInverse.copy(this.matrixWorld).invert():this.matrixWorldInverse.compose(eo,no,bi.set(1,1,1)).invert()}clone(){return new this.constructor().copy(this)}},os=new D,Eu=new kt,Tu=new kt,In=class extends ra{constructor(t=50,e=1,n=.1,s=2e3){super(),this.isPerspectiveCamera=!0,this.type="PerspectiveCamera",this.fov=t,this.zoom=1,this.near=n,this.far=s,this.focus=10,this.aspect=e,this.view=null,this.filmGauge=35,this.filmOffset=0,this.updateProjectionMatrix()}copy(t,e){return super.copy(t,e),this.fov=t.fov,this.zoom=t.zoom,this.near=t.near,this.far=t.far,this.focus=t.focus,this.aspect=t.aspect,this.view=t.view===null?null:Object.assign({},t.view),this.filmGauge=t.filmGauge,this.filmOffset=t.filmOffset,this}setFocalLength(t){let e=.5*this.getFilmHeight()/t;this.fov=ar*2*Math.atan(e),this.updateProjectionMatrix()}getFocalLength(){let t=Math.tan(zr*.5*this.fov);return .5*this.getFilmHeight()/t}getEffectiveFOV(){return ar*2*Math.atan(Math.tan(zr*.5*this.fov)/this.zoom)}getFilmWidth(){return this.filmGauge*Math.min(this.aspect,1)}getFilmHeight(){return this.filmGauge/Math.max(this.aspect,1)}getViewBounds(t,e,n){os.set(-1,-1,.5).applyMatrix4(this.projectionMatrixInverse),e.set(os.x,os.y).multiplyScalar(-t/os.z),os.set(1,1,.5).applyMatrix4(this.projectionMatrixInverse),n.set(os.x,os.y).multiplyScalar(-t/os.z)}getViewSize(t,e){return this.getViewBounds(t,Eu,Tu),e.subVectors(Tu,Eu)}setViewOffset(t,e,n,s,r,a){this.aspect=t/e,this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=t,this.view.fullHeight=e,this.view.offsetX=n,this.view.offsetY=s,this.view.width=r,this.view.height=a,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){let t=this.near,e=t*Math.tan(zr*.5*this.fov)/this.zoom,n=2*e,s=this.aspect*n,r=-.5*s,a=this.view;if(this.view!==null&&this.view.enabled){let l=a.fullWidth,c=a.fullHeight;r+=a.offsetX*s/l,e-=a.offsetY*n/c,s*=a.width/l,n*=a.height/c}let o=this.filmOffset;o!==0&&(r+=t*o/this.getFilmWidth()),this.projectionMatrix.makePerspective(r,r+s,e,e-n,t,this.far,this.coordinateSystem,this.reversedDepth),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(t){let e=super.toJSON(t);return e.object.fov=this.fov,e.object.zoom=this.zoom,e.object.near=this.near,e.object.far=this.far,e.object.focus=this.focus,e.object.aspect=this.aspect,this.view!==null&&(e.object.view=Object.assign({},this.view)),e.object.filmGauge=this.filmGauge,e.object.filmOffset=this.filmOffset,e}};var aa=class extends ra{constructor(t=-1,e=1,n=1,s=-1,r=.1,a=2e3){super(),this.isOrthographicCamera=!0,this.type="OrthographicCamera",this.zoom=1,this.view=null,this.left=t,this.right=e,this.top=n,this.bottom=s,this.near=r,this.far=a,this.updateProjectionMatrix()}copy(t,e){return super.copy(t,e),this.left=t.left,this.right=t.right,this.top=t.top,this.bottom=t.bottom,this.near=t.near,this.far=t.far,this.zoom=t.zoom,this.view=t.view===null?null:Object.assign({},t.view),this}setViewOffset(t,e,n,s,r,a){this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=t,this.view.fullHeight=e,this.view.offsetX=n,this.view.offsetY=s,this.view.width=r,this.view.height=a,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){let t=(this.right-this.left)/(2*this.zoom),e=(this.top-this.bottom)/(2*this.zoom),n=(this.right+this.left)/2,s=(this.top+this.bottom)/2,r=n-t,a=n+t,o=s+e,l=s-e;if(this.view!==null&&this.view.enabled){let c=(this.right-this.left)/this.view.fullWidth/this.zoom,h=(this.top-this.bottom)/this.view.fullHeight/this.zoom;r+=c*this.view.offsetX,a=r+c*this.view.width,o-=h*this.view.offsetY,l=o-h*this.view.height}this.projectionMatrix.makeOrthographic(r,a,o,l,this.near,this.far,this.coordinateSystem,this.reversedDepth),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(t){let e=super.toJSON(t);return e.object.zoom=this.zoom,e.object.left=this.left,e.object.right=this.right,e.object.top=this.top,e.object.bottom=this.bottom,e.object.near=this.near,e.object.far=this.far,this.view!==null&&(e.object.view=Object.assign({},this.view)),e}},Ic=class extends Vo{constructor(){super(new aa(-5,5,5,-5,.5,500)),this.isDirectionalLightShadow=!0}},fr=class extends sa{constructor(t,e){super(t,e),this.isDirectionalLight=!0,this.type="DirectionalLight",this.position.copy(Mn.DEFAULT_UP),this.updateMatrix(),this.target=new Mn,this.shadow=new Ic}dispose(){super.dispose(),this.shadow.dispose()}copy(t){return super.copy(t),this.target=t.target.clone(),this.shadow=t.shadow.clone(),this}toJSON(t){let e=super.toJSON(t);return e.object.shadow=this.shadow.toJSON(),e.object.target=this.target.uuid,e}};var tr=-90,er=1,pr=class extends Mn{constructor(t,e,n){super(),this.type="CubeCamera",this.renderTarget=n,this.coordinateSystem=null,this.activeMipmapLevel=0;let s=new In(tr,er,t,e);s.layers=this.layers,this.add(s);let r=new In(tr,er,t,e);r.layers=this.layers,this.add(r);let a=new In(tr,er,t,e);a.layers=this.layers,this.add(a);let o=new In(tr,er,t,e);o.layers=this.layers,this.add(o);let l=new In(tr,er,t,e);l.layers=this.layers,this.add(l);let c=new In(tr,er,t,e);c.layers=this.layers,this.add(c)}updateCoordinateSystem(){let t=this.coordinateSystem,e=this.children.concat(),[n,s,r,a,o,l]=e;for(let c of e)this.remove(c);if(t===ni)n.up.set(0,1,0),n.lookAt(1,0,0),s.up.set(0,1,0),s.lookAt(-1,0,0),r.up.set(0,0,-1),r.lookAt(0,1,0),a.up.set(0,0,1),a.lookAt(0,-1,0),o.up.set(0,1,0),o.lookAt(0,0,1),l.up.set(0,1,0),l.lookAt(0,0,-1);else if(t===sr)n.up.set(0,-1,0),n.lookAt(-1,0,0),s.up.set(0,-1,0),s.lookAt(1,0,0),r.up.set(0,0,1),r.lookAt(0,1,0),a.up.set(0,0,-1),a.lookAt(0,-1,0),o.up.set(0,-1,0),o.lookAt(0,0,1),l.up.set(0,-1,0),l.lookAt(0,0,-1);else throw new Error("THREE.CubeCamera.updateCoordinateSystem(): Invalid coordinate system: "+t);for(let c of e)this.add(c),c.updateMatrixWorld()}update(t,e){this.parent===null&&this.updateMatrixWorld();let{renderTarget:n,activeMipmapLevel:s}=this;this.coordinateSystem!==t.coordinateSystem&&(this.coordinateSystem=t.coordinateSystem,this.updateCoordinateSystem());let[r,a,o,l,c,h]=this.children,f=t.getRenderTarget(),d=t.getActiveCubeFace(),p=t.getActiveMipmapLevel(),x=t.xr.enabled;t.xr.enabled=!1;let S=n.texture.mipmapsAutoUpdate;n.texture.mipmapsAutoUpdate=!1;let m=!1;t.isWebGLRenderer===!0?m=t.state.buffers.depth.getReversed():m=t.reversedDepthBuffer,t.setRenderTarget(n,0,s),m&&t.autoClear===!1&&t.clearDepth(),t.render(e,r),t.setRenderTarget(n,1,s),m&&t.autoClear===!1&&t.clearDepth(),t.render(e,a),t.setRenderTarget(n,2,s),m&&t.autoClear===!1&&t.clearDepth(),t.render(e,o),t.setRenderTarget(n,3,s),m&&t.autoClear===!1&&t.clearDepth(),t.render(e,l),t.setRenderTarget(n,4,s),m&&t.autoClear===!1&&t.clearDepth(),t.render(e,c),n.texture.mipmapsAutoUpdate=S,t.setRenderTarget(n,5,s),m&&t.autoClear===!1&&t.clearDepth(),t.render(e,h),t.setRenderTarget(f,d,p),t.xr.enabled=x,n.texture.needsPMREMUpdate=!0}},Wo=class extends In{constructor(t=[]){super(),this.isArrayCamera=!0,this.isMultiViewCamera=!1,this.cameras=t,this.perCameraFrustumCulled=!1}};var fh="\\[\\]\\.:\\/",gp=new RegExp("["+fh+"]","g"),ph="[^"+fh+"]",_p="[^"+fh.replace("\\.","")+"]",xp=/((?:WC+[\/:])*)/.source.replace("WC",ph),yp=/(WCOD+)?/.source.replace("WCOD",_p),vp=/(?:\.(WC+)(?:\[(.+)\])?)?/.source.replace("WC",ph),Mp=/\.(WC+)(?:\[(.+)\])?/.source.replace("WC",ph),Sp=new RegExp("^"+xp+yp+vp+Mp+"$"),bp=["material","materials","bones","map"],Lc=class{constructor(t,e,n){let s=n||Ze.parseTrackName(e);this._targetGroup=t,this._bindings=t.subscribe_(e,s)}getValue(t,e){this.bind();let n=this._targetGroup.nCachedObjects_,s=this._bindings[n];s!==void 0&&s.getValue(t,e)}setValue(t,e){let n=this._bindings;for(let s=this._targetGroup.nCachedObjects_,r=n.length;s!==r;++s)n[s].setValue(t,e)}bind(){let t=this._bindings;for(let e=this._targetGroup.nCachedObjects_,n=t.length;e!==n;++e)t[e].bind()}unbind(){let t=this._bindings;for(let e=this._targetGroup.nCachedObjects_,n=t.length;e!==n;++e)t[e].unbind()}},Ze=class i{constructor(t,e,n){this.path=e,this.parsedPath=n||i.parseTrackName(e),this.node=i.findNode(t,this.parsedPath.nodeName),this.rootNode=t,this.getValue=this._getValue_unbound,this.setValue=this._setValue_unbound}static create(t,e,n){return t&&t.isAnimationObjectGroup?new i.Composite(t,e,n):new i(t,e,n)}static sanitizeNodeName(t){return t.replace(/\s/g,"_").replace(gp,"")}static parseTrackName(t){let e=Sp.exec(t);if(e===null)throw new Error("THREE.PropertyBinding: Cannot parse trackName: "+t);let n={nodeName:e[2],objectName:e[3],objectIndex:e[4],propertyName:e[5],propertyIndex:e[6]},s=n.nodeName&&n.nodeName.lastIndexOf(".");if(s!==void 0&&s!==-1){let r=n.nodeName.substring(s+1);bp.indexOf(r)!==-1&&(n.nodeName=n.nodeName.substring(0,s),n.objectName=r)}if(n.propertyName===null||n.propertyName.length===0)throw new Error("THREE.PropertyBinding: can not parse propertyName from trackName: "+t);return n}static findNode(t,e){if(e===void 0||e===""||e==="."||e===-1||e===t.name||e===t.uuid)return t;if(t.skeleton){let n=t.skeleton.getBoneByName(e);if(n!==void 0)return n}if(t.children){let n=function(r){for(let a=0;a<r.length;a++){let o=r[a];if(o.name===e||o.uuid===e)return o;let l=n(o.children);if(l)return l}return null},s=n(t.children);if(s)return s}return null}_getValue_unavailable(){}_setValue_unavailable(){}_getValue_direct(t,e){t[e]=this.targetObject[this.propertyName]}_getValue_array(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)t[e++]=n[s]}_getValue_arrayElement(t,e){t[e]=this.resolvedProperty[this.propertyIndex]}_getValue_toArray(t,e){this.resolvedProperty.toArray(t,e)}_setValue_direct(t,e){this.targetObject[this.propertyName]=t[e]}_setValue_direct_setNeedsUpdate(t,e){this.targetObject[this.propertyName]=t[e],this.targetObject.needsUpdate=!0}_setValue_direct_setMatrixWorldNeedsUpdate(t,e){this.targetObject[this.propertyName]=t[e],this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_array(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=t[e++]}_setValue_array_setNeedsUpdate(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=t[e++];this.targetObject.needsUpdate=!0}_setValue_array_setMatrixWorldNeedsUpdate(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=t[e++];this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_arrayElement(t,e){this.resolvedProperty[this.propertyIndex]=t[e]}_setValue_arrayElement_setNeedsUpdate(t,e){this.resolvedProperty[this.propertyIndex]=t[e],this.targetObject.needsUpdate=!0}_setValue_arrayElement_setMatrixWorldNeedsUpdate(t,e){this.resolvedProperty[this.propertyIndex]=t[e],this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_fromArray(t,e){this.resolvedProperty.fromArray(t,e)}_setValue_fromArray_setNeedsUpdate(t,e){this.resolvedProperty.fromArray(t,e),this.targetObject.needsUpdate=!0}_setValue_fromArray_setMatrixWorldNeedsUpdate(t,e){this.resolvedProperty.fromArray(t,e),this.targetObject.matrixWorldNeedsUpdate=!0}_getValue_unbound(t,e){this.bind(),this.getValue(t,e)}_setValue_unbound(t,e){this.bind(),this.setValue(t,e)}bind(){let t=this.node,e=this.parsedPath,n=e.objectName,s=e.propertyName,r=e.propertyIndex;if(t||(t=i.findNode(this.rootNode,e.nodeName),this.node=t),this.getValue=this._getValue_unavailable,this.setValue=this._setValue_unavailable,!t){Kt("PropertyBinding: No target node found for track: "+this.path+".");return}if(n){let c=e.objectIndex;switch(n){case"materials":if(!t.material){ie("PropertyBinding: Can not bind to material as node does not have a material.",this);return}if(!t.material.materials){ie("PropertyBinding: Can not bind to material.materials as node.material does not have a materials array.",this);return}t=t.material.materials;break;case"bones":if(!t.skeleton){ie("PropertyBinding: Can not bind to bones as node does not have a skeleton.",this);return}t=t.skeleton.bones;for(let h=0;h<t.length;h++)if(t[h].name===c){c=h;break}break;case"map":if("map"in t){t=t.map;break}if(!t.material){ie("PropertyBinding: Can not bind to material as node does not have a material.",this);return}if(!t.material.map){ie("PropertyBinding: Can not bind to material.map as node.material does not have a map.",this);return}t=t.material.map;break;default:if(t[n]===void 0){ie("PropertyBinding: Can not bind to objectName of node undefined.",this);return}t=t[n]}if(c!==void 0){if(t[c]===void 0){ie("PropertyBinding: Trying to bind to objectIndex of objectName, but is undefined.",this,t);return}t=t[c]}}let a=t[s];if(a===void 0){let c=e.nodeName;ie("PropertyBinding: Trying to update property for track: "+c+"."+s+" but it wasn't found.",t);return}let o=this.Versioning.None;this.targetObject=t,t.isMaterial===!0?o=this.Versioning.NeedsUpdate:t.isObject3D===!0&&(o=this.Versioning.MatrixWorldNeedsUpdate);let l=this.BindingType.Direct;if(r!==void 0){if(s==="morphTargetInfluences"){if(!t.geometry){ie("PropertyBinding: Can not bind to morphTargetInfluences because node does not have a geometry.",this);return}if(!t.geometry.morphAttributes){ie("PropertyBinding: Can not bind to morphTargetInfluences because node does not have a geometry.morphAttributes.",this);return}t.morphTargetDictionary[r]!==void 0&&(r=t.morphTargetDictionary[r])}l=this.BindingType.ArrayElement,this.resolvedProperty=a,this.propertyIndex=r}else a.fromArray!==void 0&&a.toArray!==void 0?(l=this.BindingType.HasFromToArray,this.resolvedProperty=a):Array.isArray(a)?(l=this.BindingType.EntireArray,this.resolvedProperty=a):this.propertyName=s;this.getValue=this.GetterByBindingType[l],this.setValue=this.SetterByBindingTypeAndVersioning[l][o]}unbind(){this.node=null,this.getValue=this._getValue_unbound,this.setValue=this._setValue_unbound}};Ze.Composite=Lc;Ze.prototype.BindingType={Direct:0,EntireArray:1,ArrayElement:2,HasFromToArray:3};Ze.prototype.Versioning={None:0,NeedsUpdate:1,MatrixWorldNeedsUpdate:2};Ze.prototype.GetterByBindingType=[Ze.prototype._getValue_direct,Ze.prototype._getValue_array,Ze.prototype._getValue_arrayElement,Ze.prototype._getValue_toArray];Ze.prototype.SetterByBindingTypeAndVersioning=[[Ze.prototype._setValue_direct,Ze.prototype._setValue_direct_setNeedsUpdate,Ze.prototype._setValue_direct_setMatrixWorldNeedsUpdate],[Ze.prototype._setValue_array,Ze.prototype._setValue_array_setNeedsUpdate,Ze.prototype._setValue_array_setMatrixWorldNeedsUpdate],[Ze.prototype._setValue_arrayElement,Ze.prototype._setValue_arrayElement_setNeedsUpdate,Ze.prototype._setValue_arrayElement_setMatrixWorldNeedsUpdate],[Ze.prototype._setValue_fromArray,Ze.prototype._setValue_fromArray_setNeedsUpdate,Ze.prototype._setValue_fromArray_setMatrixWorldNeedsUpdate]];var Ix=new Float32Array(1);var wu=new Ge,oa=class{constructor(t,e,n=0,s=1/0){this.ray=new hs(t,e),this.near=n,this.far=s,this.camera=null,this.layers=new lr,this.params={Mesh:{},Line:{threshold:1},LOD:{},Points:{threshold:1},Sprite:{}}}set(t,e){this.ray.set(t,e)}setFromCamera(t,e){e.isPerspectiveCamera?(this.ray.origin.setFromMatrixPosition(e.matrixWorld),this.ray.direction.set(t.x,t.y,.5).unproject(e).sub(this.ray.origin).normalize(),this.camera=e):e.isOrthographicCamera?(this.ray.origin.set(t.x,t.y,e.projectionMatrix.elements[14]).unproject(e),this.ray.direction.set(0,0,-1).transformDirection(e.matrixWorld),this.camera=e):ie("Raycaster: Unsupported camera type: "+e.type)}setFromXRController(t){return wu.identity().extractRotation(t.matrixWorld),this.ray.origin.setFromMatrixPosition(t.matrixWorld),this.ray.direction.set(0,0,-1).applyMatrix4(wu),this}intersectObject(t,e=!0,n=[]){return Nc(t,this,n,e),n.sort(Au),n}intersectObjects(t,e=!0,n=[]){for(let s=0,r=t.length;s<r;s++)Nc(t[s],this,n,e);return n.sort(Au),n}};function Au(i,t){return i.distance-t.distance}function Nc(i,t,e,n){let s=!0;if(i.layers.test(t.layers)&&i.raycast(t,e)===!1&&(s=!1),s===!0&&n===!0){let r=i.children;for(let a=0,o=r.length;a<o;a++)Nc(r[a],t,e,!0)}}var mr=class{constructor(t=1,e=0,n=0){this.radius=t,this.phi=e,this.theta=n}set(t,e,n){return this.radius=t,this.phi=e,this.theta=n,this}copy(t){return this.radius=t.radius,this.phi=t.phi,this.theta=t.theta,this}makeSafe(){return this.phi=ge(this.phi,1e-6,Math.PI-1e-6),this}setFromVector3(t){return this.setFromCartesianCoords(t.x,t.y,t.z)}setFromCartesianCoords(t,e,n){return this.radius=Math.sqrt(t*t+e*e+n*n),this.radius===0?(this.theta=0,this.phi=0):(this.theta=Math.atan2(t,n),this.phi=Math.acos(ge(e/this.radius,-1,1))),this}clone(){return new this.constructor().copy(this)}};var Dc=class{static{this.prototype.isMatrix2=!0}constructor(t,e,n,s){this.elements=[1,0,0,1],t!==void 0&&this.set(t,e,n,s)}identity(){return this.set(1,0,0,1),this}fromArray(t,e=0){for(let n=0;n<4;n++)this.elements[n]=t[n+e];return this}set(t,e,n,s){let r=this.elements;return r[0]=t,r[2]=e,r[1]=n,r[3]=s,this}};var la=class extends pi{constructor(t,e=null){super(),this.object=t,this.domElement=e,this.enabled=!0,this.state=-1,this.keys={},this.mouseButtons={LEFT:null,MIDDLE:null,RIGHT:null},this.touches={ONE:null,TWO:null}}connect(t){this.domElement!==null&&this.disconnect(),this.domElement=t}disconnect(){}dispose(){}update(){}};function mh(i,t,e,n){let s=Ep(n);switch(e){case Qc:return i*t;case eh:return i*t/s.components*s.byteLength;case Qo:return i*t/s.components*s.byteLength;case xs:return i*t*2/s.components*s.byteLength;case tl:return i*t*2/s.components*s.byteLength;case th:return i*t*3/s.components*s.byteLength;case yi:return i*t*4/s.components*s.byteLength;case el:return i*t*4/s.components*s.byteLength;case ua:case da:return Math.floor((i+3)/4)*Math.floor((t+3)/4)*8;case fa:case pa:return Math.floor((i+3)/4)*Math.floor((t+3)/4)*16;case il:case rl:return Math.max(i,16)*Math.max(t,8)/4;case nl:case sl:return Math.max(i,8)*Math.max(t,8)/2;case al:case ol:case cl:case hl:return Math.floor((i+3)/4)*Math.floor((t+3)/4)*8;case ll:case ma:case ul:return Math.floor((i+3)/4)*Math.floor((t+3)/4)*16;case dl:return Math.floor((i+3)/4)*Math.floor((t+3)/4)*16;case fl:return Math.floor((i+4)/5)*Math.floor((t+3)/4)*16;case pl:return Math.floor((i+4)/5)*Math.floor((t+4)/5)*16;case ml:return Math.floor((i+5)/6)*Math.floor((t+4)/5)*16;case gl:return Math.floor((i+5)/6)*Math.floor((t+5)/6)*16;case _l:return Math.floor((i+7)/8)*Math.floor((t+4)/5)*16;case xl:return Math.floor((i+7)/8)*Math.floor((t+5)/6)*16;case yl:return Math.floor((i+7)/8)*Math.floor((t+7)/8)*16;case vl:return Math.floor((i+9)/10)*Math.floor((t+4)/5)*16;case Ml:return Math.floor((i+9)/10)*Math.floor((t+5)/6)*16;case Sl:return Math.floor((i+9)/10)*Math.floor((t+7)/8)*16;case bl:return Math.floor((i+9)/10)*Math.floor((t+9)/10)*16;case El:return Math.floor((i+11)/12)*Math.floor((t+9)/10)*16;case Tl:return Math.floor((i+11)/12)*Math.floor((t+11)/12)*16;case wl:case Al:case Rl:return Math.ceil(i/4)*Math.ceil(t/4)*16;case Cl:case Pl:return Math.ceil(i/4)*Math.ceil(t/4)*8;case ga:case Il:return Math.ceil(i/4)*Math.ceil(t/4)*16}throw new Error(`Unable to determine texture byte length for ${e} format.`)}function Ep(i){switch(i){case Hn:case Jc:return{byteLength:1,components:1};case yr:case Kc:case xi:return{byteLength:2,components:1};case $o:case jo:return{byteLength:2,components:4};case gi:case Ko:case _i:return{byteLength:4,components:1};case $c:case jc:return{byteLength:4,components:3}}throw new Error(`THREE.TextureUtils: Unknown texture type ${i}.`)}typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("register",{detail:{revision:Xo}}));typeof window<"u"&&(window.__THREE__?Kt("WARNING: Multiple instances of Three.js being imported."):window.__THREE__=Xo);function Od(){let i=null,t=!1,e=null,n=null;function s(r,a){n=i.requestAnimationFrame(s),e(r,a)}return{start:function(){t!==!0&&e!==null&&i!==null&&(n=i.requestAnimationFrame(s),t=!0)},stop:function(){i!==null&&i.cancelAnimationFrame(n),t=!1},setAnimationLoop:function(r){e=r},setContext:function(r){i=r}}}function Tp(i){let t=new WeakMap;function e(o,l){let c=o.array,h=o.usage,f=c.byteLength,d=i.createBuffer();i.bindBuffer(l,d),i.bufferData(l,c,h),o.onUploadCallback();let p;if(c instanceof Float32Array)p=i.FLOAT;else if(typeof Float16Array<"u"&&c instanceof Float16Array)p=i.HALF_FLOAT;else if(c instanceof Uint16Array)o.isFloat16BufferAttribute?p=i.HALF_FLOAT:p=i.UNSIGNED_SHORT;else if(c instanceof Int16Array)p=i.SHORT;else if(c instanceof Uint32Array)p=i.UNSIGNED_INT;else if(c instanceof Int32Array)p=i.INT;else if(c instanceof Int8Array)p=i.BYTE;else if(c instanceof Uint8Array)p=i.UNSIGNED_BYTE;else if(c instanceof Uint8ClampedArray)p=i.UNSIGNED_BYTE;else throw new Error("THREE.WebGLAttributes: Unsupported buffer data format: "+c);return{buffer:d,type:p,bytesPerElement:c.BYTES_PER_ELEMENT,version:o.version,size:f}}function n(o,l,c){let h=l.array,f=l.updateRanges;if(i.bindBuffer(c,o),f.length===0)i.bufferSubData(c,0,h);else{f.sort((p,x)=>p.start-x.start);let d=0;for(let p=1;p<f.length;p++){let x=f[d],S=f[p];S.start<=x.start+x.count+1?x.count=Math.max(x.count,S.start+S.count-x.start):(++d,f[d]=S)}f.length=d+1;for(let p=0,x=f.length;p<x;p++){let S=f[p];i.bufferSubData(c,S.start*h.BYTES_PER_ELEMENT,h,S.start,S.count)}l.clearUpdateRanges()}l.onUploadCallback()}function s(o){return o.isInterleavedBufferAttribute&&(o=o.data),t.get(o)}function r(o){o.isInterleavedBufferAttribute&&(o=o.data);let l=t.get(o);l&&(i.deleteBuffer(l.buffer),t.delete(o))}function a(o,l){if(o.isInterleavedBufferAttribute&&(o=o.data),o.isGLBufferAttribute){let h=t.get(o);(!h||h.version<o.version)&&t.set(o,{buffer:o.buffer,type:o.type,bytesPerElement:o.elementSize,version:o.version});return}let c=t.get(o);if(c===void 0)t.set(o,e(o,l));else if(c.version<o.version){if(c.size!==o.array.byteLength)throw new Error("THREE.WebGLAttributes: The size of the buffer attribute's array buffer does not match the original size. Resizing buffer attributes is not supported.");n(c.buffer,o,l),c.version=o.version}}return{get:s,remove:r,update:a}}var wp=`#ifdef USE_ALPHAHASH
	if ( diffuseColor.a < getAlphaHashThreshold( vPosition ) ) discard;
#endif`,Ap=`#ifdef USE_ALPHAHASH
	const float ALPHA_HASH_SCALE = 0.05;
	float hash2D( vec2 value ) {
		return fract( 1.0e4 * sin( 17.0 * value.x + 0.1 * value.y ) * ( 0.1 + abs( sin( 13.0 * value.y + value.x ) ) ) );
	}
	float hash3D( vec3 value ) {
		return hash2D( vec2( hash2D( value.xy ), value.z ) );
	}
	float getAlphaHashThreshold( vec3 position ) {
		float maxDeriv = max(
			length( dFdx( position.xyz ) ),
			length( dFdy( position.xyz ) )
		);
		float pixScale = 1.0 / ( ALPHA_HASH_SCALE * maxDeriv );
		vec2 pixScales = vec2(
			exp2( floor( log2( pixScale ) ) ),
			exp2( ceil( log2( pixScale ) ) )
		);
		vec2 alpha = vec2(
			hash3D( floor( pixScales.x * position.xyz ) ),
			hash3D( floor( pixScales.y * position.xyz ) )
		);
		float lerpFactor = fract( log2( pixScale ) );
		float x = ( 1.0 - lerpFactor ) * alpha.x + lerpFactor * alpha.y;
		float a = min( lerpFactor, 1.0 - lerpFactor );
		vec3 cases = vec3(
			x * x / ( 2.0 * a * ( 1.0 - a ) ),
			( x - 0.5 * a ) / ( 1.0 - a ),
			1.0 - ( ( 1.0 - x ) * ( 1.0 - x ) / ( 2.0 * a * ( 1.0 - a ) ) )
		);
		float threshold = ( x < ( 1.0 - a ) )
			? ( ( x < a ) ? cases.x : cases.y )
			: cases.z;
		return clamp( threshold , 1.0e-6, 1.0 );
	}
#endif`,Rp=`#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, vAlphaMapUv ).g;
#endif`,Cp=`#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,Pp=`#ifdef USE_ALPHATEST
	#ifdef ALPHA_TO_COVERAGE
	diffuseColor.a = smoothstep( alphaTest, alphaTest + fwidth( diffuseColor.a ), diffuseColor.a );
	if ( diffuseColor.a == 0.0 ) discard;
	#else
	if ( diffuseColor.a < alphaTest ) discard;
	#endif
#endif`,Ip=`#ifdef USE_ALPHATEST
	uniform float alphaTest;
#endif`,Lp=`#ifdef USE_AOMAP
	float ambientOcclusion = ( texture2D( aoMap, vAoMapUv ).r - 1.0 ) * aoMapIntensity + 1.0;
	reflectedLight.indirectDiffuse *= ambientOcclusion;
	#if defined( USE_CLEARCOAT ) 
		clearcoatSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_SHEEN ) 
		sheenSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD )
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		reflectedLight.indirectSpecular *= computeSpecularOcclusion( dotNV, ambientOcclusion, material.roughness );
	#endif
#endif`,Np=`#ifdef USE_AOMAP
	uniform sampler2D aoMap;
	uniform float aoMapIntensity;
#endif`,Dp=`#ifdef USE_BATCHING
	#if ! defined( GL_ANGLE_multi_draw )
	#define gl_DrawID _gl_DrawID
	uniform int _gl_DrawID;
	#endif
	uniform highp sampler2D batchingTexture;
	uniform highp usampler2D batchingIdTexture;
	mat4 getBatchingMatrix( const in float i ) {
		int size = textureSize( batchingTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( batchingTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( batchingTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( batchingTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( batchingTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
	float getIndirectIndex( const in int i ) {
		int size = textureSize( batchingIdTexture, 0 ).x;
		int x = i % size;
		int y = i / size;
		return float( texelFetch( batchingIdTexture, ivec2( x, y ), 0 ).r );
	}
#endif
#ifdef USE_BATCHING_COLOR
	uniform sampler2D batchingColorTexture;
	vec4 getBatchingColor( const in float i ) {
		int size = textureSize( batchingColorTexture, 0 ).x;
		int j = int( i );
		int x = j % size;
		int y = j / size;
		return texelFetch( batchingColorTexture, ivec2( x, y ), 0 );
	}
#endif`,Up=`#ifdef USE_BATCHING
	mat4 batchingMatrix = getBatchingMatrix( getIndirectIndex( gl_DrawID ) );
#endif`,Fp=`vec3 transformed = vec3( position );
#ifdef USE_ALPHAHASH
	vPosition = vec3( position );
#endif`,Op=`vec3 objectNormal = vec3( normal );
#ifdef USE_TANGENT
	vec3 objectTangent = vec3( tangent.xyz );
#endif`,Bp=`float G_BlinnPhong_Implicit( ) {
	return 0.25;
}
float D_BlinnPhong( const in float shininess, const in float dotNH ) {
	return RECIPROCAL_PI * ( shininess * 0.5 + 1.0 ) * pow( dotNH, shininess );
}
vec3 BRDF_BlinnPhong( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in vec3 specularColor, const in float shininess ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( specularColor, 1.0, dotVH );
	float G = G_BlinnPhong_Implicit( );
	float D = D_BlinnPhong( shininess, dotNH );
	return F * ( G * D );
} // validated`,kp=`#ifdef USE_IRIDESCENCE
	const mat3 XYZ_TO_REC709 = mat3(
		 3.2404542, -0.9692660,  0.0556434,
		-1.5371385,  1.8760108, -0.2040259,
		-0.4985314,  0.0415560,  1.0572252
	);
	vec3 Fresnel0ToIor( vec3 fresnel0 ) {
		vec3 sqrtF0 = sqrt( fresnel0 );
		return ( vec3( 1.0 ) + sqrtF0 ) / ( vec3( 1.0 ) - sqrtF0 );
	}
	vec3 IorToFresnel0( vec3 transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - vec3( incidentIor ) ) / ( transmittedIor + vec3( incidentIor ) ) );
	}
	float IorToFresnel0( float transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - incidentIor ) / ( transmittedIor + incidentIor ));
	}
	vec3 evalSensitivity( float OPD, vec3 shift ) {
		float phase = 2.0 * PI * OPD * 1.0e-9;
		vec3 val = vec3( 5.4856e-13, 4.4201e-13, 5.2481e-13 );
		vec3 pos = vec3( 1.6810e+06, 1.7953e+06, 2.2084e+06 );
		vec3 var = vec3( 4.3278e+09, 9.3046e+09, 6.6121e+09 );
		vec3 xyz = val * sqrt( 2.0 * PI * var ) * cos( pos * phase + shift ) * exp( - pow2( phase ) * var );
		xyz.x += 9.7470e-14 * sqrt( 2.0 * PI * 4.5282e+09 ) * cos( 2.2399e+06 * phase + shift[ 0 ] ) * exp( - 4.5282e+09 * pow2( phase ) );
		xyz /= 1.0685e-7;
		vec3 rgb = XYZ_TO_REC709 * xyz;
		return rgb;
	}
	vec3 evalIridescence( float outsideIOR, float eta2, float cosTheta1, float thinFilmThickness, vec3 baseF0 ) {
		vec3 I;
		float iridescenceIOR = mix( outsideIOR, eta2, smoothstep( 0.0, 0.03, thinFilmThickness ) );
		float sinTheta2Sq = pow2( outsideIOR / iridescenceIOR ) * ( 1.0 - pow2( cosTheta1 ) );
		float cosTheta2Sq = 1.0 - sinTheta2Sq;
		if ( cosTheta2Sq < 0.0 ) {
			return vec3( 1.0 );
		}
		float cosTheta2 = sqrt( cosTheta2Sq );
		float R0 = IorToFresnel0( iridescenceIOR, outsideIOR );
		float R12 = F_Schlick( R0, 1.0, cosTheta1 );
		float T121 = 1.0 - R12;
		float phi12 = 0.0;
		if ( iridescenceIOR < outsideIOR ) phi12 = PI;
		float phi21 = PI - phi12;
		vec3 baseIOR = Fresnel0ToIor( clamp( baseF0, 0.0, 0.9999 ) );		vec3 R1 = IorToFresnel0( baseIOR, iridescenceIOR );
		vec3 R23 = F_Schlick( R1, 1.0, cosTheta2 );
		vec3 phi23 = vec3( 0.0 );
		if ( baseIOR[ 0 ] < iridescenceIOR ) phi23[ 0 ] = PI;
		if ( baseIOR[ 1 ] < iridescenceIOR ) phi23[ 1 ] = PI;
		if ( baseIOR[ 2 ] < iridescenceIOR ) phi23[ 2 ] = PI;
		float OPD = 2.0 * iridescenceIOR * thinFilmThickness * cosTheta2;
		vec3 phi = vec3( phi21 ) + phi23;
		vec3 R123 = clamp( R12 * R23, 1e-5, 0.9999 );
		vec3 r123 = sqrt( R123 );
		vec3 Rs = pow2( T121 ) * R23 / ( vec3( 1.0 ) - R123 );
		vec3 C0 = R12 + Rs;
		I = C0;
		vec3 Cm = Rs - T121;
		for ( int m = 1; m <= 2; ++ m ) {
			Cm *= r123;
			vec3 Sm = 2.0 * evalSensitivity( float( m ) * OPD, float( m ) * phi );
			I += Cm * Sm;
		}
		return max( I, vec3( 0.0 ) );
	}
#endif`,zp=`#ifdef USE_BUMPMAP
	uniform sampler2D bumpMap;
	uniform float bumpScale;
	vec2 dHdxy_fwd() {
		vec2 dSTdx = dFdx( vBumpMapUv );
		vec2 dSTdy = dFdy( vBumpMapUv );
		float Hll = bumpScale * texture2D( bumpMap, vBumpMapUv ).x;
		float dBx = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdx ).x - Hll;
		float dBy = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdy ).x - Hll;
		return vec2( dBx, dBy );
	}
	vec3 perturbNormalArb( vec3 surf_pos, vec3 surf_norm, vec2 dHdxy, float faceDirection ) {
		vec3 vSigmaX = normalize( dFdx( surf_pos.xyz ) );
		vec3 vSigmaY = normalize( dFdy( surf_pos.xyz ) );
		vec3 vN = surf_norm;
		vec3 R1 = cross( vSigmaY, vN );
		vec3 R2 = cross( vN, vSigmaX );
		float fDet = dot( vSigmaX, R1 ) * faceDirection;
		vec3 vGrad = sign( fDet ) * ( dHdxy.x * R1 + dHdxy.y * R2 );
		return normalize( abs( fDet ) * surf_norm - vGrad );
	}
#endif`,Hp=`#if NUM_CLIPPING_PLANES > 0
	vec4 plane;
	#ifdef ALPHA_TO_COVERAGE
		float distanceToPlane, distanceGradient;
		float clipOpacity = 1.0;
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
			distanceGradient = fwidth( distanceToPlane ) / 2.0;
			clipOpacity *= smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			if ( clipOpacity == 0.0 ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			float unionClipOpacity = 1.0;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
				distanceGradient = fwidth( distanceToPlane ) / 2.0;
				unionClipOpacity *= 1.0 - smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			}
			#pragma unroll_loop_end
			clipOpacity *= 1.0 - unionClipOpacity;
		#endif
		diffuseColor.a *= clipOpacity;
		if ( diffuseColor.a == 0.0 ) discard;
	#else
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			if ( dot( vClipPosition, plane.xyz ) > plane.w ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			bool clipped = true;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				clipped = ( dot( vClipPosition, plane.xyz ) > plane.w ) && clipped;
			}
			#pragma unroll_loop_end
			if ( clipped ) discard;
		#endif
	#endif
#endif`,Gp=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
	uniform vec4 clippingPlanes[ NUM_CLIPPING_PLANES ];
#endif`,Vp=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
#endif`,Wp=`#if NUM_CLIPPING_PLANES > 0
	vClipPosition = - mvPosition.xyz;
#endif`,Xp=`#if defined( USE_COLOR ) || defined( USE_COLOR_ALPHA )
	diffuseColor *= vColor;
#endif`,qp=`#if defined( USE_COLOR ) || defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#endif`,Yp=`#if defined( USE_COLOR ) || defined( USE_COLOR_ALPHA ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	varying vec4 vColor;
#endif`,Zp=`#if defined( USE_COLOR ) || defined( USE_COLOR_ALPHA ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	vColor = vec4( 1.0 );
#endif
#ifdef USE_COLOR_ALPHA
	vColor *= color;
#elif defined( USE_COLOR )
	vColor.rgb *= color;
#endif
#ifdef USE_INSTANCING_COLOR
	vColor.rgb *= instanceColor.rgb;
#endif
#ifdef USE_BATCHING_COLOR
	vColor *= getBatchingColor( getIndirectIndex( gl_DrawID ) );
#endif`,Jp=`#define PI 3.141592653589793
#define PI2 6.283185307179586
#define PI_HALF 1.5707963267948966
#define RECIPROCAL_PI 0.3183098861837907
#define RECIPROCAL_PI2 0.15915494309189535
#define EPSILON 1e-6
#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
#define whiteComplement( a ) ( 1.0 - saturate( a ) )
float pow2( const in float x ) { return x*x; }
vec3 pow2( const in vec3 x ) { return x*x; }
float pow3( const in float x ) { return x*x*x; }
float pow4( const in float x ) { float x2 = x*x; return x2*x2; }
float max3( const in vec3 v ) { return max( max( v.x, v.y ), v.z ); }
float average( const in vec3 v ) { return dot( v, vec3( 0.3333333 ) ); }
highp float rand( const in vec2 uv ) {
	const highp float a = 12.9898, b = 78.233, c = 43758.5453;
	highp float dt = dot( uv.xy, vec2( a,b ) ), sn = mod( dt, PI );
	return fract( sin( sn ) * c );
}
#ifdef HIGH_PRECISION
	float precisionSafeLength( vec3 v ) { return length( v ); }
#else
	float precisionSafeLength( vec3 v ) {
		float maxComponent = max3( abs( v ) );
		return length( v / maxComponent ) * maxComponent;
	}
#endif
struct IncidentLight {
	vec3 color;
	vec3 direction;
	bool visible;
};
struct ReflectedLight {
	vec3 directDiffuse;
	vec3 directSpecular;
	vec3 indirectDiffuse;
	vec3 indirectSpecular;
};
#ifdef USE_ALPHAHASH
	varying vec3 vPosition;
#endif
vec3 transformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );
}
#define inverseTransformDirection transformDirectionByInverseViewMatrix
vec3 transformNormalByInverseViewMatrix( in vec3 normal, in mat4 viewMatrix ) {
	return normalize( ( vec4( normal, 0.0 ) * viewMatrix ).xyz );
}
vec3 transformDirectionByInverseViewMatrix( in vec3 dir, in mat4 viewMatrix ) {
	return normalize( ( vec4( dir, 0.0 ) * viewMatrix ).xyz );
}
bool isPerspectiveMatrix( mat4 m ) {
	return m[ 2 ][ 3 ] == - 1.0;
}
vec2 equirectUv( in vec3 dir ) {
	float u = atan( dir.z, dir.x ) * RECIPROCAL_PI2 + 0.5;
	float v = asin( clamp( dir.y, - 1.0, 1.0 ) ) * RECIPROCAL_PI + 0.5;
	return vec2( u, v );
}
vec3 BRDF_Lambert( const in vec3 diffuseColor ) {
	return RECIPROCAL_PI * diffuseColor;
}
vec3 F_Schlick( const in vec3 f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
}
float F_Schlick( const in float f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
} // validated`,Kp=`vec3 transformedNormal = objectNormal;
#ifdef USE_TANGENT
	vec3 transformedTangent = objectTangent;
#endif
#ifdef USE_BATCHING
	mat3 bm = mat3( batchingMatrix );
	transformedNormal /= vec3( dot( bm[ 0 ], bm[ 0 ] ), dot( bm[ 1 ], bm[ 1 ] ), dot( bm[ 2 ], bm[ 2 ] ) );
	transformedNormal = bm * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = bm * transformedTangent;
	#endif
#endif
#ifdef USE_INSTANCING
	mat3 im = mat3( instanceMatrix );
	transformedNormal /= vec3( dot( im[ 0 ], im[ 0 ] ), dot( im[ 1 ], im[ 1 ] ), dot( im[ 2 ], im[ 2 ] ) );
	transformedNormal = im * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = im * transformedTangent;
	#endif
#endif
transformedNormal = normalMatrix * transformedNormal;
#ifdef FLIP_SIDED
	transformedNormal = - transformedNormal;
#endif
#ifdef USE_TANGENT
	transformedTangent = ( modelViewMatrix * vec4( transformedTangent, 0.0 ) ).xyz;
#endif`,$p=`#ifdef USE_DISPLACEMENTMAP
	uniform sampler2D displacementMap;
	uniform float displacementScale;
	uniform float displacementBias;
#endif`,jp=`#ifdef USE_DISPLACEMENTMAP
	transformed += normalize( objectNormal ) * ( texture2D( displacementMap, vDisplacementMapUv ).x * displacementScale + displacementBias );
#endif`,Qp=`#ifdef USE_EMISSIVEMAP
	vec4 emissiveColor = texture2D( emissiveMap, vEmissiveMapUv );
	#ifdef DECODE_VIDEO_TEXTURE_EMISSIVE
		emissiveColor = sRGBTransferEOTF( emissiveColor );
	#endif
	totalEmissiveRadiance *= emissiveColor.rgb;
#endif`,tm=`#ifdef USE_EMISSIVEMAP
	uniform sampler2D emissiveMap;
#endif`,em="gl_FragColor = linearToOutputTexel( gl_FragColor );",nm=`vec4 LinearTransferOETF( in vec4 value ) {
	return value;
}
vec4 sRGBTransferEOTF( in vec4 value ) {
	return vec4( mix( pow( value.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), value.rgb * 0.0773993808, vec3( lessThanEqual( value.rgb, vec3( 0.04045 ) ) ) ), value.a );
}
vec4 sRGBTransferOETF( in vec4 value ) {
	return vec4( mix( pow( value.rgb, vec3( 0.41666 ) ) * 1.055 - vec3( 0.055 ), value.rgb * 12.92, vec3( lessThanEqual( value.rgb, vec3( 0.0031308 ) ) ) ), value.a );
}`,im=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vec3 cameraToFrag;
		if ( isOrthographic ) {
			cameraToFrag = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToFrag = normalize( vWorldPosition - cameraPosition );
		}
		vec3 worldNormal = transformNormalByInverseViewMatrix( normal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vec3 reflectVec = reflect( cameraToFrag, worldNormal );
		#else
			vec3 reflectVec = refract( cameraToFrag, worldNormal, refractionRatio );
		#endif
	#else
		vec3 reflectVec = vReflect;
	#endif
	#ifdef ENVMAP_TYPE_CUBE
		vec4 envColor = textureCube( envMap, envMapRotation * reflectVec );
		#ifdef ENVMAP_BLENDING_MULTIPLY
			outgoingLight = mix( outgoingLight, outgoingLight * envColor.xyz, specularStrength * reflectivity );
		#elif defined( ENVMAP_BLENDING_MIX )
			outgoingLight = mix( outgoingLight, envColor.xyz, specularStrength * reflectivity );
		#elif defined( ENVMAP_BLENDING_ADD )
			outgoingLight += envColor.xyz * specularStrength * reflectivity;
		#endif
	#endif
#endif`,sm=`#ifdef USE_ENVMAP
	uniform float envMapIntensity;
	uniform mat3 envMapRotation;
	uniform samplerCube envMap;
	#ifdef ENVMAP_TYPE_PMREM
		float roughnessToMip( const in float roughness ) {
			float r = clamp( roughness, 0.0, 1.0 );
			return ENVMAP_MAX_LOD * r * ( 2.0 - r );
		}
	#endif
#endif`,rm=`#ifdef USE_ENVMAP
	uniform float reflectivity;
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		varying vec3 vWorldPosition;
		uniform float refractionRatio;
	#else
		varying vec3 vReflect;
	#endif
#endif`,am=`#ifdef USE_ENVMAP
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		
		varying vec3 vWorldPosition;
	#else
		varying vec3 vReflect;
		uniform float refractionRatio;
	#endif
#endif`,om=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vWorldPosition = worldPosition.xyz;
	#else
		vec3 cameraToVertex;
		if ( isOrthographic ) {
			cameraToVertex = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToVertex = normalize( worldPosition.xyz - cameraPosition );
		}
		vec3 worldNormal = transformNormalByInverseViewMatrix( transformedNormal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vReflect = reflect( cameraToVertex, worldNormal );
		#else
			vReflect = refract( cameraToVertex, worldNormal, refractionRatio );
		#endif
	#endif
#endif`,lm=`#ifdef USE_FOG
	vFogDepth = - mvPosition.z;
#endif`,cm=`#ifdef USE_FOG
	varying float vFogDepth;
#endif`,hm=`#ifdef USE_FOG
	#ifdef FOG_EXP2
		float fogFactor = 1.0 - exp( - fogDensity * fogDensity * vFogDepth * vFogDepth );
	#else
		float fogFactor = smoothstep( fogNear, fogFar, vFogDepth );
	#endif
	gl_FragColor.rgb = mix( gl_FragColor.rgb, fogColor, fogFactor );
#endif`,um=`#ifdef USE_FOG
	uniform vec3 fogColor;
	varying float vFogDepth;
	#ifdef FOG_EXP2
		uniform float fogDensity;
	#else
		uniform float fogNear;
		uniform float fogFar;
	#endif
#endif`,dm=`#ifdef USE_GRADIENTMAP
	uniform sampler2D gradientMap;
#endif
vec3 getGradientIrradiance( vec3 normal, vec3 lightDirection ) {
	float dotNL = dot( normal, lightDirection );
	vec2 coord = vec2( dotNL * 0.5 + 0.5, 0.0 );
	#ifdef USE_GRADIENTMAP
		return vec3( texture2D( gradientMap, coord ).r );
	#else
		vec2 fw = fwidth( coord ) * 0.5;
		return mix( vec3( 0.7 ), vec3( 1.0 ), smoothstep( 0.7 - fw.x, 0.7 + fw.x, coord.x ) );
	#endif
}`,fm=`#ifdef USE_LIGHTMAP
	uniform sampler2D lightMap;
	uniform float lightMapIntensity;
#endif`,pm=`LambertMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularStrength = specularStrength;`,mm=`varying vec3 vViewPosition;
struct LambertMaterial {
	vec3 diffuseColor;
	float specularStrength;
};
void RE_Direct_Lambert( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Lambert( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Lambert
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Lambert`,gm=`uniform bool receiveShadow;
uniform vec3 ambientLightColor;
#if defined( USE_LIGHT_PROBES )
	uniform vec3 lightProbe[ 9 ];
#endif
vec3 shGetIrradianceAt( in vec3 normal, in vec3 shCoefficients[ 9 ] ) {
	float x = normal.x, y = normal.y, z = normal.z;
	vec3 result = shCoefficients[ 0 ] * 0.886227;
	result += shCoefficients[ 1 ] * 2.0 * 0.511664 * y;
	result += shCoefficients[ 2 ] * 2.0 * 0.511664 * z;
	result += shCoefficients[ 3 ] * 2.0 * 0.511664 * x;
	result += shCoefficients[ 4 ] * 2.0 * 0.429043 * x * y;
	result += shCoefficients[ 5 ] * 2.0 * 0.429043 * y * z;
	result += shCoefficients[ 6 ] * ( 0.743125 * z * z - 0.247708 );
	result += shCoefficients[ 7 ] * 2.0 * 0.429043 * x * z;
	result += shCoefficients[ 8 ] * 0.429043 * ( x * x - y * y );
	return result;
}
vec3 getLightProbeIrradiance( const in vec3 lightProbe[ 9 ], const in vec3 normal ) {
	vec3 worldNormal = transformNormalByInverseViewMatrix( normal, viewMatrix );
	vec3 irradiance = shGetIrradianceAt( worldNormal, lightProbe );
	return irradiance;
}
vec3 getAmbientLightIrradiance( const in vec3 ambientLightColor ) {
	vec3 irradiance = ambientLightColor;
	return irradiance;
}
float getDistanceAttenuation( const in float lightDistance, const in float cutoffDistance, const in float decayExponent ) {
	float distanceFalloff = 1.0 / max( pow( lightDistance, decayExponent ), 0.01 );
	if ( cutoffDistance > 0.0 ) {
		distanceFalloff *= pow2( saturate( 1.0 - pow4( lightDistance / cutoffDistance ) ) );
	}
	return distanceFalloff;
}
float getSpotAttenuation( const in float coneCosine, const in float penumbraCosine, const in float angleCosine ) {
	return smoothstep( coneCosine, penumbraCosine, angleCosine );
}
#if NUM_SUN_LIGHTS > 0
	struct SunLight {
		vec3 direction;
		vec3 color;
	};
	uniform SunLight sunLights[ NUM_SUN_LIGHTS ];
	void getSunLightInfo( const in SunLight sunLight, out IncidentLight light ) {
		light.color = sunLight.color;
		light.direction = sunLight.direction;
		light.visible = true;
	}
#endif
#if NUM_DIR_LIGHTS > 0
	struct DirectionalLight {
		vec3 direction;
		vec3 color;
	};
	uniform DirectionalLight directionalLights[ NUM_DIR_LIGHTS ];
	void getDirectionalLightInfo( const in DirectionalLight directionalLight, out IncidentLight light ) {
		light.color = directionalLight.color;
		light.direction = directionalLight.direction;
		light.visible = true;
	}
#endif
#if NUM_POINT_LIGHTS > 0
	struct PointLight {
		vec3 position;
		vec3 color;
		float distance;
		float decay;
	};
	uniform PointLight pointLights[ NUM_POINT_LIGHTS ];
	void getPointLightInfo( const in PointLight pointLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = pointLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float lightDistance = length( lVector );
		light.color = pointLight.color;
		light.color *= getDistanceAttenuation( lightDistance, pointLight.distance, pointLight.decay );
		light.visible = ( light.color != vec3( 0.0 ) );
	}
#endif
#if NUM_SPOT_LIGHTS > 0
	struct SpotLight {
		vec3 position;
		vec3 direction;
		vec3 color;
		float distance;
		float decay;
		float coneCos;
		float penumbraCos;
	};
	uniform SpotLight spotLights[ NUM_SPOT_LIGHTS ];
	void getSpotLightInfo( const in SpotLight spotLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = spotLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float angleCos = dot( light.direction, spotLight.direction );
		float spotAttenuation = getSpotAttenuation( spotLight.coneCos, spotLight.penumbraCos, angleCos );
		if ( spotAttenuation > 0.0 ) {
			float lightDistance = length( lVector );
			light.color = spotLight.color * spotAttenuation;
			light.color *= getDistanceAttenuation( lightDistance, spotLight.distance, spotLight.decay );
			light.visible = ( light.color != vec3( 0.0 ) );
		} else {
			light.color = vec3( 0.0 );
			light.visible = false;
		}
	}
#endif
#if NUM_RECT_AREA_LIGHTS > 0
	struct RectAreaLight {
		vec3 color;
		vec3 position;
		vec3 halfWidth;
		vec3 halfHeight;
	};
	uniform sampler2D ltc_1;	uniform sampler2D ltc_2;
	uniform RectAreaLight rectAreaLights[ NUM_RECT_AREA_LIGHTS ];
#endif
#if NUM_HEMI_LIGHTS > 0
	struct HemisphereLight {
		vec3 direction;
		vec3 skyColor;
		vec3 groundColor;
	};
	uniform HemisphereLight hemisphereLights[ NUM_HEMI_LIGHTS ];
	vec3 getHemisphereLightIrradiance( const in HemisphereLight hemiLight, const in vec3 normal ) {
		float dotNL = dot( normal, hemiLight.direction );
		float hemiDiffuseWeight = 0.5 * dotNL + 0.5;
		vec3 irradiance = mix( hemiLight.groundColor, hemiLight.skyColor, hemiDiffuseWeight );
		return irradiance;
	}
#endif
#include <lightprobes_pars_fragment>`,_m=`#ifdef USE_ENVMAP
	vec3 getIBLIrradiance( const in vec3 normal ) {
		#ifdef ENVMAP_TYPE_PMREM
			vec3 worldNormal = transformNormalByInverseViewMatrix( normal, viewMatrix );
			vec4 envMapColor = textureLod( envMap, envMapRotation * worldNormal, ENVMAP_MAX_LOD );
			return PI * envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	vec3 getIBLRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness ) {
		#ifdef ENVMAP_TYPE_PMREM
			vec3 reflectVec = reflect( - viewDir, normal );
			reflectVec = normalize( mix( reflectVec, normal, pow4( roughness ) ) );
			reflectVec = transformDirectionByInverseViewMatrix( reflectVec, viewMatrix );
			vec4 envMapColor = textureLod( envMap, envMapRotation * reflectVec, roughnessToMip( roughness ) );
			return envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	#ifdef USE_RETROREFLECTION
		vec3 getIBLRetroRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness ) {
			#ifdef ENVMAP_TYPE_PMREM
				vec3 retroVec = normalize( mix( viewDir, normal, pow4( roughness ) ) );
				retroVec = transformDirectionByInverseViewMatrix( retroVec, viewMatrix );
				vec4 envMapColor = textureLod( envMap, envMapRotation * retroVec, roughnessToMip( roughness ) );
				return envMapColor.rgb * envMapIntensity;
			#else
				return vec3( 0.0 );
			#endif
		}
	#endif
	#ifdef USE_ANISOTROPY
		vec3 getIBLAnisotropyRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness, const in vec3 bitangent, const in float anisotropy ) {
			#ifdef ENVMAP_TYPE_PMREM
				vec3 bentNormal = cross( bitangent, viewDir );
				bentNormal = normalize( cross( bentNormal, bitangent ) );
				bentNormal = normalize( mix( bentNormal, normal, pow2( pow2( 1.0 - anisotropy * ( 1.0 - roughness ) ) ) ) );
				return getIBLRadiance( viewDir, bentNormal, roughness );
			#else
				return vec3( 0.0 );
			#endif
		}
		#ifdef USE_RETROREFLECTION
			vec3 getIBLAnisotropyRetroRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness, const in vec3 bitangent, const in float anisotropy ) {
				#ifdef ENVMAP_TYPE_PMREM
					vec3 bentNormal = cross( bitangent, viewDir );
					bentNormal = normalize( cross( bentNormal, bitangent ) );
					bentNormal = normalize( mix( bentNormal, normal, pow2( pow2( 1.0 - anisotropy * ( 1.0 - roughness ) ) ) ) );
					return getIBLRetroRadiance( viewDir, bentNormal, roughness );
				#else
					return vec3( 0.0 );
				#endif
			}
		#endif
	#endif
#endif`,xm=`ToonMaterial material;
material.diffuseColor = diffuseColor.rgb;`,ym=`varying vec3 vViewPosition;
struct ToonMaterial {
	vec3 diffuseColor;
};
void RE_Direct_Toon( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	vec3 irradiance = getGradientIrradiance( geometryNormal, directLight.direction ) * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Toon( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Toon
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Toon`,vm=`BlinnPhongMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularColor = specular;
material.specularShininess = shininess;
material.specularStrength = specularStrength;`,Mm=`varying vec3 vViewPosition;
struct BlinnPhongMaterial {
	vec3 diffuseColor;
	vec3 specularColor;
	float specularShininess;
	float specularStrength;
};
void RE_Direct_BlinnPhong( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
	reflectedLight.directSpecular += irradiance * BRDF_BlinnPhong( directLight.direction, geometryViewDir, geometryNormal, material.specularColor, material.specularShininess ) * material.specularStrength;
}
void RE_IndirectDiffuse_BlinnPhong( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_BlinnPhong
#define RE_IndirectDiffuse		RE_IndirectDiffuse_BlinnPhong`,Sm=`PhysicalMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.diffuseContribution = diffuseColor.rgb * ( 1.0 - metalnessFactor );
material.metalness = metalnessFactor;
vec3 dxy = max( abs( dFdx( nonPerturbedNormal ) ), abs( dFdy( nonPerturbedNormal ) ) );
float geometryRoughness = max( max( dxy.x, dxy.y ), dxy.z );
material.roughness = max( roughnessFactor, 0.045 );
material.roughness += geometryRoughness;
material.roughness = min( material.roughness, 1.0 );
#ifdef USE_DIFFUSE_ROUGHNESS
	float diffuseRoughnessFactor = diffuseRoughness;
	#ifdef USE_DIFFUSE_ROUGHNESSMAP
		diffuseRoughnessFactor *= texture2D( diffuseRoughnessMap, vDiffuseRoughnessMapUv ).r;
	#endif
	material.diffuseRoughness = saturate( diffuseRoughnessFactor );
#endif
#ifdef IOR
	material.ior = ior;
	#ifdef USE_SPECULAR
		float specularIntensityFactor = specularIntensity;
		vec3 specularColorFactor = specularColor;
		#ifdef USE_SPECULAR_COLORMAP
			specularColorFactor *= texture2D( specularColorMap, vSpecularColorMapUv ).rgb;
		#endif
		#ifdef USE_SPECULAR_INTENSITYMAP
			specularIntensityFactor *= texture2D( specularIntensityMap, vSpecularIntensityMapUv ).a;
		#endif
		material.specularF90 = mix( specularIntensityFactor, 1.0, metalnessFactor );
	#else
		float specularIntensityFactor = 1.0;
		vec3 specularColorFactor = vec3( 1.0 );
		material.specularF90 = 1.0;
	#endif
	material.specularColor = min( pow2( ( material.ior - 1.0 ) / ( material.ior + 1.0 ) ) * specularColorFactor, vec3( 1.0 ) ) * specularIntensityFactor;
	material.specularColorBlended = mix( material.specularColor, diffuseColor.rgb, metalnessFactor );
#else
	material.specularColor = vec3( 0.04 );
	material.specularColorBlended = mix( material.specularColor, diffuseColor.rgb, metalnessFactor );
	material.specularF90 = 1.0;
#endif
#ifdef USE_CLEARCOAT
	material.clearcoat = clearcoat;
	material.clearcoatRoughness = clearcoatRoughness;
	material.clearcoatF0 = vec3( 0.04 );
	material.clearcoatF90 = 1.0;
	#ifdef USE_CLEARCOATMAP
		material.clearcoat *= texture2D( clearcoatMap, vClearcoatMapUv ).x;
	#endif
	#ifdef USE_CLEARCOAT_ROUGHNESSMAP
		material.clearcoatRoughness *= texture2D( clearcoatRoughnessMap, vClearcoatRoughnessMapUv ).y;
	#endif
	material.clearcoat = saturate( material.clearcoat );	material.clearcoatRoughness = max( material.clearcoatRoughness, 0.045 );
	material.clearcoatRoughness += geometryRoughness;
	material.clearcoatRoughness = min( material.clearcoatRoughness, 1.0 );
#endif
#ifdef USE_DISPERSION
	material.dispersion = dispersion;
#endif
#ifdef USE_RETROREFLECTION
	material.retroreflectivity = retroreflectivity;
#endif
#ifdef USE_IRIDESCENCE
	material.iridescence = iridescence;
	material.iridescenceIOR = iridescenceIOR;
	#ifdef USE_IRIDESCENCEMAP
		material.iridescence *= texture2D( iridescenceMap, vIridescenceMapUv ).r;
	#endif
	#ifdef USE_IRIDESCENCE_THICKNESSMAP
		material.iridescenceThickness = (iridescenceThicknessMaximum - iridescenceThicknessMinimum) * texture2D( iridescenceThicknessMap, vIridescenceThicknessMapUv ).g + iridescenceThicknessMinimum;
	#else
		material.iridescenceThickness = iridescenceThicknessMaximum;
	#endif
#endif
#ifdef USE_SHEEN
	material.sheenColor = sheenColor;
	#ifdef USE_SHEEN_COLORMAP
		material.sheenColor *= texture2D( sheenColorMap, vSheenColorMapUv ).rgb;
	#endif
	material.sheenRoughness = clamp( sheenRoughness, 0.0001, 1.0 );
	#ifdef USE_SHEEN_ROUGHNESSMAP
		material.sheenRoughness *= texture2D( sheenRoughnessMap, vSheenRoughnessMapUv ).a;
	#endif
#endif
#ifdef USE_ANISOTROPY
	#ifdef USE_ANISOTROPYMAP
		mat2 anisotropyMat = mat2( anisotropyVector.x, anisotropyVector.y, - anisotropyVector.y, anisotropyVector.x );
		vec3 anisotropyPolar = texture2D( anisotropyMap, vAnisotropyMapUv ).rgb;
		vec2 anisotropyV = anisotropyMat * normalize( 2.0 * anisotropyPolar.rg - vec2( 1.0 ) ) * anisotropyPolar.b;
	#else
		vec2 anisotropyV = anisotropyVector;
	#endif
	material.anisotropy = length( anisotropyV );
	if( material.anisotropy == 0.0 ) {
		anisotropyV = vec2( 1.0, 0.0 );
	} else {
		anisotropyV /= material.anisotropy;
		material.anisotropy = saturate( material.anisotropy );
	}
	material.alphaT = mix( pow2( material.roughness ), 1.0, pow2( material.anisotropy ) );
	material.anisotropyT = tbn[ 0 ] * anisotropyV.x + tbn[ 1 ] * anisotropyV.y;
	material.anisotropyB = tbn[ 1 ] * anisotropyV.x - tbn[ 0 ] * anisotropyV.y;
#endif`,bm=`uniform sampler2D dfgLUT;
struct PhysicalMaterial {
	vec3 diffuseColor;
	vec3 diffuseContribution;
	vec3 specularColor;
	vec3 specularColorBlended;
	float roughness;
	float metalness;
	float specularF90;
	float dispersion;
	vec2 dfg;
	vec3 multiScatteringCompensation;
	#ifdef USE_DIFFUSE_ROUGHNESS
		float diffuseRoughness;
	#endif
	#ifdef USE_RETROREFLECTION
		float retroreflectivity;
	#endif
	#ifdef USE_CLEARCOAT
		float clearcoat;
		float clearcoatRoughness;
		vec3 clearcoatF0;
		float clearcoatF90;
	#endif
	#ifdef USE_IRIDESCENCE
		float iridescence;
		float iridescenceIOR;
		float iridescenceThickness;
		vec3 iridescenceFresnel;
		vec3 iridescenceF0Dielectric;
		vec3 iridescenceF0Metallic;
	#endif
	#ifdef USE_SHEEN
		vec3 sheenColor;
		float sheenRoughness;
	#endif
	#ifdef IOR
		float ior;
	#endif
	#ifdef USE_TRANSMISSION
		float transmission;
		float transmissionAlpha;
		float thickness;
		float attenuationDistance;
		vec3 attenuationColor;
	#endif
	#ifdef USE_ANISOTROPY
		float anisotropy;
		float alphaT;
		vec3 anisotropyT;
		vec3 anisotropyB;
	#endif
};
vec3 clearcoatSpecularDirect = vec3( 0.0 );
vec3 clearcoatSpecularIndirect = vec3( 0.0 );
vec3 sheenSpecularDirect = vec3( 0.0 );
vec3 sheenSpecularIndirect = vec3(0.0 );
vec3 Schlick_to_F0( const in vec3 f, const in float f90, const in float dotVH ) {
    float x = clamp( 1.0 - dotVH, 0.0, 1.0 );
    float x2 = x * x;
    float x5 = clamp( x * x2 * x2, 0.0, 0.9999 );
    return ( f - vec3( f90 ) * x5 ) / ( 1.0 - x5 );
}
#ifdef USE_DIFFUSE_ROUGHNESS
	const float EON_EPSILON = 1e-7;
	float FON_DirectionalAlbedo( const in float mu, const in float roughness, const in float A ) {
		float muComp = 1.0 - mu;
		float gOverPi = muComp * ( 0.0571085289 + muComp * ( 0.491881867 + muComp * ( - 0.332181442 + muComp * 0.0714429953 ) ) );
		return A * ( 1.0 + roughness * gOverPi );
	}
	vec3 BRDF_EON( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in vec3 diffuseColor, const in float roughness ) {
		vec3 rho = saturate( diffuseColor );
		if ( roughness <= EON_EPSILON ) return BRDF_Lambert( rho );
		float dotNL = saturate( dot( normal, lightDir ) );
		float dotNV = saturate( dot( normal, viewDir ) );
		float s = dot( lightDir, viewDir ) - dotNL * dotNV;
		float sOverT = ( s > 0.0 ) ? s / max( max( dotNL, dotNV ), EON_EPSILON ) : s;
		float A = 1.0 / ( 1.0 + ( 0.5 - 2.0 / ( 3.0 * PI ) ) * roughness );
		vec3 singleScatter = rho * RECIPROCAL_PI * A * ( 1.0 + roughness * sOverT );
		float averageAlbedo = A * ( 1.0 + ( 2.0 / 3.0 - 28.0 / ( 15.0 * PI ) ) * roughness );
		float albedoV = FON_DirectionalAlbedo( dotNV, roughness, A );
		float albedoL = FON_DirectionalAlbedo( dotNL, roughness, A );
		vec3 rhoMultiScatter = rho * rho * averageAlbedo / max( vec3( EON_EPSILON ), vec3( 1.0 ) - rho * ( 1.0 - averageAlbedo ) );
		vec3 multiScatter = rhoMultiScatter * RECIPROCAL_PI
			* max( EON_EPSILON, 1.0 - albedoV )
			* max( EON_EPSILON, 1.0 - albedoL )
			/ max( EON_EPSILON, 1.0 - averageAlbedo );
		return singleScatter + multiScatter;
	}
	vec3 EON_DirectionalAlbedo( const in vec3 diffuseColor, const in float roughness, const in float dotNV ) {
		vec3 rho = saturate( diffuseColor );
		if ( roughness <= EON_EPSILON ) return rho;
		float A = 1.0 / ( 1.0 + ( 0.5 - 2.0 / ( 3.0 * PI ) ) * roughness );
		float directionalAlbedo = FON_DirectionalAlbedo( dotNV, roughness, A );
		float averageAlbedo = A * ( 1.0 + ( 2.0 / 3.0 - 28.0 / ( 15.0 * PI ) ) * roughness );
		vec3 rhoMultiScatter = rho * rho * averageAlbedo / max( vec3( EON_EPSILON ), vec3( 1.0 ) - rho * ( 1.0 - averageAlbedo ) );
		return rho * directionalAlbedo + rhoMultiScatter * ( 1.0 - directionalAlbedo );
	}
#endif
float V_GGX_SmithCorrelated( const in float alpha, const in float dotNL, const in float dotNV ) {
	float a2 = pow2( alpha );
	float gv = dotNL * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNV ) );
	float gl = dotNV * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNL ) );
	return 0.5 / max( gv + gl, EPSILON );
}
float D_GGX( const in float alpha, const in float dotNH ) {
	float a2 = pow2( alpha );
	float denom = pow2( dotNH ) * ( a2 - 1.0 ) + 1.0;
	return RECIPROCAL_PI * a2 / pow2( denom );
}
#ifdef USE_ANISOTROPY
	float V_GGX_SmithCorrelated_Anisotropic( const in float alphaT, const in float alphaB, const in float dotTV, const in float dotBV, const in float dotTL, const in float dotBL, const in float dotNV, const in float dotNL ) {
		float gv = dotNL * length( vec3( alphaT * dotTV, alphaB * dotBV, dotNV ) );
		float gl = dotNV * length( vec3( alphaT * dotTL, alphaB * dotBL, dotNL ) );
		return 0.5 / max( gv + gl, EPSILON );
	}
	float D_GGX_Anisotropic( const in float alphaT, const in float alphaB, const in float dotNH, const in float dotTH, const in float dotBH ) {
		float a2 = alphaT * alphaB;
		highp vec3 v = vec3( alphaB * dotTH, alphaT * dotBH, a2 * dotNH );
		highp float v2 = dot( v, v );
		float w2 = a2 / v2;
		return RECIPROCAL_PI * a2 * pow2 ( w2 );
	}
#endif
#ifdef USE_CLEARCOAT
	vec3 BRDF_GGX_Clearcoat( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material) {
		vec3 f0 = material.clearcoatF0;
		float f90 = material.clearcoatF90;
		float roughness = max( material.clearcoatRoughness, 0.045 );
		float alpha = pow2( roughness );
		vec3 halfDir = normalize( lightDir + viewDir );
		float dotNL = saturate( dot( normal, lightDir ) );
		float dotNV = saturate( dot( normal, viewDir ) );
		float dotNH = saturate( dot( normal, halfDir ) );
		float dotVH = saturate( dot( viewDir, halfDir ) );
		vec3 F = F_Schlick( f0, f90, dotVH );
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
		return F * ( V * D );
	}
#endif
vec3 BRDF_GGX( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material ) {
	vec3 f0 = material.specularColorBlended;
	float f90 = material.specularF90;
	float roughness = max( material.roughness, 0.045 );
	float alpha = pow2( roughness );
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( f0, f90, dotVH );
	#ifdef USE_IRIDESCENCE
		F = mix( F, material.iridescenceFresnel, material.iridescence );
	#endif
	#ifdef USE_ANISOTROPY
		float dotTL = dot( material.anisotropyT, lightDir );
		float dotTV = dot( material.anisotropyT, viewDir );
		float dotTH = dot( material.anisotropyT, halfDir );
		float dotBL = dot( material.anisotropyB, lightDir );
		float dotBV = dot( material.anisotropyB, viewDir );
		float dotBH = dot( material.anisotropyB, halfDir );
		float alphaT = max( material.alphaT, alpha );
		float V = V_GGX_SmithCorrelated_Anisotropic( alphaT, alpha, dotTV, dotBV, dotTL, dotBL, dotNV, dotNL );
		float D = D_GGX_Anisotropic( alphaT, alpha, dotNH, dotTH, dotBH );
	#else
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
	#endif
	return F * ( V * D );
}
vec2 LTC_Uv( const in vec3 N, const in vec3 V, const in float roughness ) {
	const float LUT_SIZE = 64.0;
	const float LUT_SCALE = ( LUT_SIZE - 1.0 ) / LUT_SIZE;
	const float LUT_BIAS = 0.5 / LUT_SIZE;
	float dotNV = saturate( dot( N, V ) );
	vec2 uv = vec2( roughness, sqrt( 1.0 - dotNV ) );
	uv = uv * LUT_SCALE + LUT_BIAS;
	return uv;
}
float LTC_ClippedSphereFormFactor( const in vec3 f ) {
	float l = length( f );
	return max( ( l * l + f.z ) / ( l + 1.0 ), 0.0 );
}
vec3 LTC_EdgeVectorFormFactor( const in vec3 v1, const in vec3 v2 ) {
	float x = dot( v1, v2 );
	float y = abs( x );
	float a = 0.8543985 + ( 0.4965155 + 0.0145206 * y ) * y;
	float b = 3.4175940 + ( 4.1616724 + y ) * y;
	float v = a / b;
	float theta_sintheta = ( x > 0.0 ) ? v : 0.5 * inversesqrt( max( 1.0 - x * x, 1e-7 ) ) - v;
	return cross( v1, v2 ) * theta_sintheta;
}
vec3 LTC_Evaluate( const in vec3 N, const in vec3 V, const in vec3 P, const in mat3 mInv, const in vec3 rectCoords[ 4 ] ) {
	vec3 v1 = rectCoords[ 1 ] - rectCoords[ 0 ];
	vec3 v2 = rectCoords[ 3 ] - rectCoords[ 0 ];
	vec3 lightNormal = cross( v1, v2 );
	if( dot( lightNormal, P - rectCoords[ 0 ] ) < 0.0 ) return vec3( 0.0 );
	vec3 T1, T2;
	T1 = normalize( V - N * dot( V, N ) );
	T2 = - cross( N, T1 );
	mat3 mat = mInv * transpose( mat3( T1, T2, N ) );
	vec3 coords[ 4 ];
	coords[ 0 ] = mat * ( rectCoords[ 0 ] - P );
	coords[ 1 ] = mat * ( rectCoords[ 1 ] - P );
	coords[ 2 ] = mat * ( rectCoords[ 2 ] - P );
	coords[ 3 ] = mat * ( rectCoords[ 3 ] - P );
	coords[ 0 ] = normalize( coords[ 0 ] );
	coords[ 1 ] = normalize( coords[ 1 ] );
	coords[ 2 ] = normalize( coords[ 2 ] );
	coords[ 3 ] = normalize( coords[ 3 ] );
	vec3 vectorFormFactor = vec3( 0.0 );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 0 ], coords[ 1 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 1 ], coords[ 2 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 2 ], coords[ 3 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 3 ], coords[ 0 ] );
	float result = LTC_ClippedSphereFormFactor( vectorFormFactor );
	return vec3( result );
}
#if defined( USE_SHEEN )
float D_Charlie( float roughness, float dotNH ) {
	float alpha = pow2( roughness );
	float invAlpha = 1.0 / alpha;
	float cos2h = dotNH * dotNH;
	float sin2h = max( 1.0 - cos2h, 0.0078125 );
	return ( 2.0 + invAlpha ) * pow( sin2h, invAlpha * 0.5 ) / ( 2.0 * PI );
}
float V_Neubelt( float dotNV, float dotNL ) {
	return saturate( 1.0 / ( 4.0 * ( dotNL + dotNV - dotNL * dotNV ) ) );
}
vec3 BRDF_Sheen( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, vec3 sheenColor, const in float sheenRoughness ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float D = D_Charlie( sheenRoughness, dotNH );
	float V = V_Neubelt( dotNV, dotNL );
	return sheenColor * ( D * V );
}
#endif
float IBLSheenBRDF( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	float r2 = roughness * roughness;
	float rInv = 1.0 / ( roughness + 0.1 );
	float a = -1.9362 + 1.0678 * roughness + 0.4573 * r2 - 0.8469 * rInv;
	float b = -0.6014 + 0.5538 * roughness - 0.4670 * r2 - 0.1255 * rInv;
	float DG = exp( a * dotNV + b );
	return saturate( DG );
}
vec3 EnvironmentBRDF( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	vec2 fab = texture2D( dfgLUT, vec2( roughness, dotNV ) ).rg;
	return specularColor * fab.x + specularF90 * fab.y;
}
#ifdef USE_IRIDESCENCE
void computeMultiscatteringIridescence( const in vec2 fab, const in vec3 specularColor, const in float specularF90, const in float iridescence, const in vec3 iridescenceF0, inout vec3 singleScatter, inout vec3 multiScatter ) {
#else
void computeMultiscattering( const in vec2 fab, const in vec3 specularColor, const in float specularF90, inout vec3 singleScatter, inout vec3 multiScatter ) {
#endif
	#ifdef USE_IRIDESCENCE
		vec3 Fr = mix( specularColor, iridescenceF0, iridescence );
	#else
		vec3 Fr = specularColor;
	#endif
	vec3 FssEss = Fr * fab.x + specularF90 * fab.y;
	float Ess = fab.x + fab.y;
	float Ems = 1.0 - Ess;
	vec3 Favg = Fr + ( 1.0 - Fr ) * 0.047619;	vec3 Fms = FssEss * Favg / ( 1.0 - Ems * Favg );
	singleScatter += FssEss;
	multiScatter += Fms * Ems;
}
#if NUM_RECT_AREA_LIGHTS > 0
	void RE_Direct_RectArea_Physical( const in RectAreaLight rectAreaLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
		vec3 normal = geometryNormal;
		vec3 viewDir = geometryViewDir;
		vec3 position = geometryPosition;
		vec3 lightPos = rectAreaLight.position;
		vec3 halfWidth = rectAreaLight.halfWidth;
		vec3 halfHeight = rectAreaLight.halfHeight;
		vec3 lightColor = rectAreaLight.color;
		float roughness = material.roughness;
		vec3 rectCoords[ 4 ];
		rectCoords[ 0 ] = lightPos + halfWidth - halfHeight;		rectCoords[ 1 ] = lightPos - halfWidth - halfHeight;
		rectCoords[ 2 ] = lightPos - halfWidth + halfHeight;
		rectCoords[ 3 ] = lightPos + halfWidth + halfHeight;
		vec2 uv = LTC_Uv( normal, viewDir, roughness );
		vec4 t1 = texture2D( ltc_1, uv );
		vec4 t2 = texture2D( ltc_2, uv );
		mat3 mInv = mat3(
			vec3( t1.x, 0, t1.y ),
			vec3(    0, 1,    0 ),
			vec3( t1.z, 0, t1.w )
		);
		vec3 fresnel = ( material.specularColorBlended * t2.x + ( material.specularF90 - material.specularColorBlended ) * t2.y );
		reflectedLight.directSpecular += lightColor * fresnel * LTC_Evaluate( normal, viewDir, position, mInv, rectCoords );
		reflectedLight.directDiffuse += lightColor * material.diffuseContribution * LTC_Evaluate( normal, viewDir, position, mat3( 1.0 ), rectCoords );
		#ifdef USE_CLEARCOAT
			vec3 Ncc = geometryClearcoatNormal;
			vec2 uvClearcoat = LTC_Uv( Ncc, viewDir, material.clearcoatRoughness );
			vec4 t1Clearcoat = texture2D( ltc_1, uvClearcoat );
			vec4 t2Clearcoat = texture2D( ltc_2, uvClearcoat );
			mat3 mInvClearcoat = mat3(
				vec3( t1Clearcoat.x, 0, t1Clearcoat.y ),
				vec3(             0, 1,             0 ),
				vec3( t1Clearcoat.z, 0, t1Clearcoat.w )
			);
			vec3 fresnelClearcoat = material.clearcoatF0 * t2Clearcoat.x + ( material.clearcoatF90 - material.clearcoatF0 ) * t2Clearcoat.y;
			clearcoatSpecularDirect += lightColor * fresnelClearcoat * LTC_Evaluate( Ncc, viewDir, position, mInvClearcoat, rectCoords );
		#endif
	}
#endif
void RE_Direct_Physical( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	#ifdef USE_CLEARCOAT
		float dotNLcc = saturate( dot( geometryClearcoatNormal, directLight.direction ) );
		vec3 ccIrradiance = dotNLcc * directLight.color;
		clearcoatSpecularDirect += ccIrradiance * BRDF_GGX_Clearcoat( directLight.direction, geometryViewDir, geometryClearcoatNormal, material );
	#endif
	#ifdef USE_SHEEN
 
 		sheenSpecularDirect += irradiance * BRDF_Sheen( directLight.direction, geometryViewDir, geometryNormal, material.sheenColor, material.sheenRoughness );
 
 		float sheenAlbedoV = IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
 		float sheenAlbedoL = IBLSheenBRDF( geometryNormal, directLight.direction, material.sheenRoughness );
 
 		float sheenEnergyComp = 1.0 - max3( material.sheenColor ) * max( sheenAlbedoV, sheenAlbedoL );
 
 		irradiance *= sheenEnergyComp;
 
 	#endif
	vec3 specularBRDF = BRDF_GGX( directLight.direction, geometryViewDir, geometryNormal, material );
	#ifdef USE_RETROREFLECTION
		vec3 retroViewDir = reflect( - geometryViewDir, geometryNormal );
		vec3 retroSpecularBRDF = BRDF_GGX( directLight.direction, retroViewDir, geometryNormal, material );
		specularBRDF = mix( specularBRDF, retroSpecularBRDF, saturate( material.retroreflectivity ) );
	#endif
	reflectedLight.directSpecular += irradiance * specularBRDF * material.multiScatteringCompensation;
	vec3 halfDir = normalize( directLight.direction + geometryViewDir );
	float dotVH = saturate( dot( geometryViewDir, halfDir ) );
	vec3 F = F_Schlick( material.specularColor, material.specularF90, dotVH );
	#ifdef USE_RETROREFLECTION
		vec3 retroHalfDir = normalize( directLight.direction + retroViewDir );
		float dotRetroVH = saturate( dot( retroViewDir, retroHalfDir ) );
		vec3 retroF = F_Schlick( material.specularColor, material.specularF90, dotRetroVH );
		F = mix( F, retroF, saturate( material.retroreflectivity ) );
	#endif
	#ifdef USE_DIFFUSE_ROUGHNESS
		vec3 diffuseBRDF = BRDF_EON( directLight.direction, geometryViewDir, geometryNormal, material.diffuseColor, material.diffuseRoughness ) * ( 1.0 - material.metalness );
	#else
		vec3 diffuseBRDF = BRDF_Lambert( material.diffuseContribution );
	#endif
	reflectedLight.directDiffuse += irradiance * diffuseBRDF * ( 1.0 - F );
}
void RE_IndirectDiffuse_Physical( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	vec3 singleScattering = vec3( 0.0 );
	vec3 multiScattering = vec3( 0.0 );
	#ifdef USE_IRIDESCENCE
		computeMultiscatteringIridescence( material.dfg, material.specularColor, material.specularF90, material.iridescence, material.iridescenceF0Dielectric, singleScattering, multiScattering );
	#else
		computeMultiscattering( material.dfg, material.specularColor, material.specularF90, singleScattering, multiScattering );
	#endif
	#ifdef USE_DIFFUSE_ROUGHNESS
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		vec3 diffuseAlbedo = EON_DirectionalAlbedo( material.diffuseColor, material.diffuseRoughness, dotNV ) * ( 1.0 - material.metalness );
		vec3 diffuse = irradiance * RECIPROCAL_PI * diffuseAlbedo * ( 1.0 - singleScattering - multiScattering );
	#else
		vec3 diffuse = irradiance * BRDF_Lambert( material.diffuseContribution ) * ( 1.0 - singleScattering - multiScattering );
	#endif
	#ifdef USE_SHEEN
		float sheenAlbedo = IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
		sheenSpecularIndirect += irradiance * material.sheenColor * sheenAlbedo * RECIPROCAL_PI;
		float sheenEnergyComp = 1.0 - max3( material.sheenColor ) * sheenAlbedo;
		diffuse *= sheenEnergyComp;
	#endif
	reflectedLight.indirectDiffuse += diffuse;
}
void RE_IndirectSpecular_Physical( const in vec3 radiance, const in vec3 irradiance, const in vec3 clearcoatRadiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight) {
	#ifdef USE_CLEARCOAT
		clearcoatSpecularIndirect += clearcoatRadiance * EnvironmentBRDF( geometryClearcoatNormal, geometryViewDir, material.clearcoatF0, material.clearcoatF90, material.clearcoatRoughness );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularIndirect += irradiance * material.sheenColor * IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness ) * RECIPROCAL_PI;
 	#endif
	vec3 singleScatteringDielectric = vec3( 0.0 );
	vec3 multiScatteringDielectric = vec3( 0.0 );
	vec3 singleScatteringMetallic = vec3( 0.0 );
	vec3 multiScatteringMetallic = vec3( 0.0 );
	#ifdef USE_IRIDESCENCE
		computeMultiscatteringIridescence( material.dfg, material.specularColor, material.specularF90, material.iridescence, material.iridescenceF0Dielectric, singleScatteringDielectric, multiScatteringDielectric );
		computeMultiscatteringIridescence( material.dfg, material.diffuseColor, material.specularF90, material.iridescence, material.iridescenceF0Metallic, singleScatteringMetallic, multiScatteringMetallic );
	#else
		computeMultiscattering( material.dfg, material.specularColor, material.specularF90, singleScatteringDielectric, multiScatteringDielectric );
		computeMultiscattering( material.dfg, material.diffuseColor, material.specularF90, singleScatteringMetallic, multiScatteringMetallic );
	#endif
	vec3 singleScattering = mix( singleScatteringDielectric, singleScatteringMetallic, material.metalness );
	vec3 multiScattering = mix( multiScatteringDielectric, multiScatteringMetallic, material.metalness );
	vec3 totalScatteringDielectric = singleScatteringDielectric + multiScatteringDielectric;
	#ifdef USE_DIFFUSE_ROUGHNESS
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		vec3 diffuse = EON_DirectionalAlbedo( material.diffuseColor, material.diffuseRoughness, dotNV ) * ( 1.0 - material.metalness ) * ( 1.0 - totalScatteringDielectric );
	#else
		vec3 diffuse = material.diffuseContribution * ( 1.0 - totalScatteringDielectric );
	#endif
	vec3 cosineWeightedIrradiance = irradiance * RECIPROCAL_PI;
	vec3 indirectSpecular = radiance * singleScattering;
	indirectSpecular += multiScattering * cosineWeightedIrradiance;
	vec3 indirectDiffuse = diffuse * cosineWeightedIrradiance;
	#ifdef USE_SHEEN
		float sheenAlbedo = IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
		float sheenEnergyComp = 1.0 - max3( material.sheenColor ) * sheenAlbedo;
		indirectSpecular *= sheenEnergyComp;
		indirectDiffuse *= sheenEnergyComp;
	#endif
	reflectedLight.indirectSpecular += indirectSpecular;
	reflectedLight.indirectDiffuse += indirectDiffuse;
}
#define RE_Direct				RE_Direct_Physical
#define RE_Direct_RectArea		RE_Direct_RectArea_Physical
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Physical
#define RE_IndirectSpecular		RE_IndirectSpecular_Physical
float computeSpecularOcclusion( const in float dotNV, const in float ambientOcclusion, const in float roughness ) {
	return saturate( pow( dotNV + ambientOcclusion, exp2( - 16.0 * roughness - 1.0 ) ) - 1.0 + ambientOcclusion );
}`,Em=`
vec3 geometryPosition = - vViewPosition;
vec3 geometryNormal = normal;
vec3 geometryViewDir = ( isOrthographic ) ? vec3( 0, 0, 1 ) : normalize( vViewPosition );
vec3 geometryClearcoatNormal = vec3( 0.0 );
#ifdef USE_CLEARCOAT
	geometryClearcoatNormal = clearcoatNormal;
#endif
#ifdef USE_IRIDESCENCE
	float dotNVi = saturate( dot( normal, geometryViewDir ) );
	if ( material.iridescenceThickness == 0.0 ) {
		material.iridescence = 0.0;
	} else {
		material.iridescence = saturate( material.iridescence );
	}
	if ( material.iridescence > 0.0 ) {
		vec3 iridescenceFresnelDielectric = evalIridescence( 1.0, material.iridescenceIOR, dotNVi, material.iridescenceThickness, material.specularColor );
		vec3 iridescenceFresnelMetallic = evalIridescence( 1.0, material.iridescenceIOR, dotNVi, material.iridescenceThickness, material.diffuseColor );
		material.iridescenceFresnel = mix( iridescenceFresnelDielectric, iridescenceFresnelMetallic, material.metalness );
		material.iridescenceF0Dielectric = Schlick_to_F0( iridescenceFresnelDielectric, 1.0, dotNVi );
		material.iridescenceF0Metallic = Schlick_to_F0( iridescenceFresnelMetallic, 1.0, dotNVi );
	}
#endif
#ifdef STANDARD
	float dotNVms = saturate( dot( geometryNormal, geometryViewDir ) );
	material.dfg = texture2D( dfgLUT, vec2( material.roughness, dotNVms ) ).rg;
	#if ( NUM_SUN_LIGHTS > 0 || NUM_DIR_LIGHTS > 0 || NUM_POINT_LIGHTS > 0 || NUM_SPOT_LIGHTS > 0 )
		float EssMs = material.dfg.x + material.dfg.y;
		material.multiScatteringCompensation = 1.0 + material.specularColorBlended * ( 1.0 / EssMs - 1.0 );
	#endif
#endif
IncidentLight directLight;
#if ( NUM_POINT_LIGHTS > 0 ) && defined( RE_Direct )
	PointLight pointLight;
	#if defined( USE_SHADOWMAP ) && NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHTS; i ++ ) {
		pointLight = pointLights[ i ];
		getPointLightInfo( pointLight, geometryPosition, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_POINT_LIGHT_SHADOWS ) && ( defined( SHADOWMAP_TYPE_PCF ) || defined( SHADOWMAP_TYPE_BASIC ) )
		pointLightShadow = pointLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getPointShadow( pointShadowMap[ i ], pointLightShadow.shadowMapSize, pointLightShadow.shadowIntensity, pointLightShadow.shadowBias, pointLightShadow.shadowRadius, vPointShadowCoord[ i ], pointLightShadow.shadowCameraNear, pointLightShadow.shadowCameraFar ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_SPOT_LIGHTS > 0 ) && defined( RE_Direct )
	SpotLight spotLight;
	vec4 spotColor;
	vec3 spotLightCoord;
	bool inSpotLightMap;
	#if defined( USE_SHADOWMAP ) && NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHTS; i ++ ) {
		spotLight = spotLights[ i ];
		getSpotLightInfo( spotLight, geometryPosition, directLight );
		#if ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#define SPOT_LIGHT_MAP_INDEX UNROLLED_LOOP_INDEX
		#elif ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		#define SPOT_LIGHT_MAP_INDEX NUM_SPOT_LIGHT_MAPS
		#else
		#define SPOT_LIGHT_MAP_INDEX ( UNROLLED_LOOP_INDEX - NUM_SPOT_LIGHT_SHADOWS + NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#endif
		#if ( SPOT_LIGHT_MAP_INDEX < NUM_SPOT_LIGHT_MAPS )
			spotLightCoord = vSpotLightCoord[ i ].xyz / vSpotLightCoord[ i ].w;
			inSpotLightMap = all( lessThan( abs( spotLightCoord * 2. - 1. ), vec3( 1.0 ) ) );
			spotColor = texture2D( spotLightMap[ SPOT_LIGHT_MAP_INDEX ], spotLightCoord.xy );
			directLight.color = inSpotLightMap ? directLight.color * spotColor.rgb : directLight.color;
		#endif
		#undef SPOT_LIGHT_MAP_INDEX
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		spotLightShadow = spotLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( spotShadowMap[ i ], spotLightShadow.shadowMapSize, spotLightShadow.shadowIntensity, spotLightShadow.shadowBias, spotLightShadow.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_SUN_LIGHTS > 0 ) && defined( RE_Direct )
	SunLight sunLight;
	#if defined( USE_SHADOWMAP ) && NUM_SUN_LIGHT_SHADOWS > 0
	SunLightShadow sunLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SUN_LIGHTS; i ++ ) {
		sunLight = sunLights[ i ];
		getSunLightInfo( sunLight, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_SUN_LIGHT_SHADOWS )
		sunLightShadow = sunLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getSunShadow( sunShadowMap[ i ], sunLightShadow, UNROLLED_LOOP_INDEX ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_DIR_LIGHTS > 0 ) && defined( RE_Direct )
	DirectionalLight directionalLight;
	#if defined( USE_SHADOWMAP ) && NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHTS; i ++ ) {
		directionalLight = directionalLights[ i ];
		getDirectionalLightInfo( directionalLight, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_DIR_LIGHT_SHADOWS )
		directionalLightShadow = directionalLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( directionalShadowMap[ i ], directionalLightShadow.shadowMapSize, directionalLightShadow.shadowIntensity, directionalLightShadow.shadowBias, directionalLightShadow.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_RECT_AREA_LIGHTS > 0 ) && defined( RE_Direct_RectArea )
	RectAreaLight rectAreaLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_RECT_AREA_LIGHTS; i ++ ) {
		rectAreaLight = rectAreaLights[ i ];
		RE_Direct_RectArea( rectAreaLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if defined( RE_IndirectDiffuse )
	vec3 iblIrradiance = vec3( 0.0 );
	vec3 irradiance = getAmbientLightIrradiance( ambientLightColor );
	#if defined( USE_LIGHT_PROBES )
		irradiance += getLightProbeIrradiance( lightProbe, geometryNormal );
	#endif
	#if ( NUM_HEMI_LIGHTS > 0 )
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_HEMI_LIGHTS; i ++ ) {
			irradiance += getHemisphereLightIrradiance( hemisphereLights[ i ], geometryNormal );
		}
		#pragma unroll_loop_end
	#endif
	#if NUM_LIGHT_PROBE_GRIDS > 0
		vec3 probeWorldPos = ( ( vec4( geometryPosition, 1.0 ) - viewMatrix[ 3 ] ) * viewMatrix ).xyz;
		vec3 probeWorldNormal = transformNormalByInverseViewMatrix( geometryNormal, viewMatrix );
		int probeGrid = - 1;
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_LIGHT_PROBE_GRIDS; i ++ ) {
			if ( isInsideLightProbeGrid( probeWorldPos, probeWorldNormal, probesMin[ i ], probesMax[ i ], probesResolution[ i ] ) ) probeGrid = UNROLLED_LOOP_INDEX;
		}
		#pragma unroll_loop_end
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_LIGHT_PROBE_GRIDS; i ++ ) {
			if ( probeGrid == UNROLLED_LOOP_INDEX ) irradiance += getLightProbeGridIrradiance( probesSH[ i ], probesMin[ i ], probesMax[ i ], probesResolution[ i ], probeWorldPos, probeWorldNormal );
		}
		#pragma unroll_loop_end
	#endif
#endif
#if defined( RE_IndirectSpecular )
	vec3 radiance = vec3( 0.0 );
	vec3 clearcoatRadiance = vec3( 0.0 );
#endif`,Tm=`#if defined( RE_IndirectDiffuse )
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		vec3 lightMapIrradiance = lightMapTexel.rgb * lightMapIntensity;
		irradiance += lightMapIrradiance;
	#endif
	#if defined( USE_ENVMAP ) && defined( ENVMAP_TYPE_PMREM )
		#if defined( STANDARD ) || defined( LAMBERT ) || defined( PHONG )
			iblIrradiance += getIBLIrradiance( geometryNormal );
		#endif
	#endif
#endif
#if defined( USE_ENVMAP ) && defined( RE_IndirectSpecular )
	#ifdef USE_ANISOTROPY
		vec3 iblRadiance = getIBLAnisotropyRadiance( geometryViewDir, geometryNormal, material.roughness, material.anisotropyB, material.anisotropy );
	#else
		vec3 iblRadiance = getIBLRadiance( geometryViewDir, geometryNormal, material.roughness );
	#endif
	#ifdef USE_RETROREFLECTION
		#ifdef USE_ANISOTROPY
			vec3 retroIBLRadiance = getIBLAnisotropyRetroRadiance( geometryViewDir, geometryNormal, material.roughness, material.anisotropyB, material.anisotropy );
		#else
			vec3 retroIBLRadiance = getIBLRetroRadiance( geometryViewDir, geometryNormal, material.roughness );
		#endif
		iblRadiance = mix( iblRadiance, retroIBLRadiance, saturate( material.retroreflectivity ) );
	#endif
	radiance += iblRadiance;
	#ifdef USE_CLEARCOAT
		clearcoatRadiance += getIBLRadiance( geometryViewDir, geometryClearcoatNormal, material.clearcoatRoughness );
	#endif
#endif`,wm=`#if defined( RE_IndirectDiffuse )
	#if defined( LAMBERT ) || defined( PHONG )
		irradiance += iblIrradiance;
	#endif
	RE_IndirectDiffuse( irradiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif
#if defined( RE_IndirectSpecular )
	RE_IndirectSpecular( radiance, iblIrradiance, clearcoatRadiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif`,Am=`#if NUM_LIGHT_PROBE_GRIDS > 0
uniform highp sampler3D probesSH[ NUM_LIGHT_PROBE_GRIDS ];
uniform vec3 probesMin[ NUM_LIGHT_PROBE_GRIDS ];
uniform vec3 probesMax[ NUM_LIGHT_PROBE_GRIDS ];
uniform vec3 probesResolution[ NUM_LIGHT_PROBE_GRIDS ];
bool isInsideLightProbeGrid( vec3 worldPos, vec3 worldNormal, vec3 probesMin, vec3 probesMax, vec3 probesResolution ) {
	vec3 spacing = ( probesMax - probesMin ) / probesResolution;
	vec3 samplePos = worldPos + worldNormal * spacing * 0.5;
	vec3 margin = spacing * 0.01;
	return all( greaterThanEqual( samplePos, probesMin - margin ) ) && all( lessThanEqual( samplePos, probesMax + margin ) );
}
vec3 getLightProbeGridIrradiance( highp sampler3D probesSH, vec3 probesMin, vec3 probesMax, vec3 probesResolution, vec3 worldPos, vec3 worldNormal ) {
	vec3 res = probesResolution;
	vec3 gridRange = probesMax - probesMin;
	vec3 probeSpacing = gridRange / res;
	vec3 samplePos = worldPos + worldNormal * probeSpacing * 0.5;
	vec3 uvw = clamp( ( samplePos - probesMin ) / gridRange, 0.5 / res, 1.0 - 0.5 / res );
	float nz          = res.z;
	float paddedSlices = nz + 2.0;
	float atlasDepth  = 7.0 * paddedSlices;
	float uvZBase     = uvw.z * nz + 1.0;
	vec4 s0 = texture( probesSH, vec3( uvw.xy, ( uvZBase                       ) / atlasDepth ) );
	vec4 s1 = texture( probesSH, vec3( uvw.xy, ( uvZBase +       paddedSlices   ) / atlasDepth ) );
	vec4 s2 = texture( probesSH, vec3( uvw.xy, ( uvZBase + 2.0 * paddedSlices   ) / atlasDepth ) );
	vec4 s3 = texture( probesSH, vec3( uvw.xy, ( uvZBase + 3.0 * paddedSlices   ) / atlasDepth ) );
	vec4 s4 = texture( probesSH, vec3( uvw.xy, ( uvZBase + 4.0 * paddedSlices   ) / atlasDepth ) );
	vec4 s5 = texture( probesSH, vec3( uvw.xy, ( uvZBase + 5.0 * paddedSlices   ) / atlasDepth ) );
	vec4 s6 = texture( probesSH, vec3( uvw.xy, ( uvZBase + 6.0 * paddedSlices   ) / atlasDepth ) );
	vec3 c0 = s0.xyz;
	vec3 c1 = vec3( s0.w, s1.xy );
	vec3 c2 = vec3( s1.zw, s2.x );
	vec3 c3 = s2.yzw;
	vec3 c4 = s3.xyz;
	vec3 c5 = vec3( s3.w, s4.xy );
	vec3 c6 = vec3( s4.zw, s5.x );
	vec3 c7 = s5.yzw;
	vec3 c8 = s6.xyz;
	float x = worldNormal.x, y = worldNormal.y, z = worldNormal.z;
	vec3 result = c0 * 0.886227;
	result += c1 * 2.0 * 0.511664 * y;
	result += c2 * 2.0 * 0.511664 * z;
	result += c3 * 2.0 * 0.511664 * x;
	result += c4 * 2.0 * 0.429043 * x * y;
	result += c5 * 2.0 * 0.429043 * y * z;
	result += c6 * ( 0.743125 * z * z - 0.247708 );
	result += c7 * 2.0 * 0.429043 * x * z;
	result += c8 * 0.429043 * ( x * x - y * y );
	return max( result, vec3( 0.0 ) );
}
#endif`,Rm=`#if defined( USE_LOGARITHMIC_DEPTH_BUFFER )
	gl_FragDepth = vIsPerspective == 0.0 ? gl_FragCoord.z : log2( vFragDepth ) * logDepthBufFC * 0.5;
#endif`,Cm=`#if defined( USE_LOGARITHMIC_DEPTH_BUFFER )
	uniform float logDepthBufFC;
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,Pm=`#ifdef USE_LOGARITHMIC_DEPTH_BUFFER
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,Im=`#ifdef USE_LOGARITHMIC_DEPTH_BUFFER
	vFragDepth = 1.0 + gl_Position.w;
	vIsPerspective = float( isPerspectiveMatrix( projectionMatrix ) );
#endif`,Lm=`#ifdef USE_MAP
	vec4 sampledDiffuseColor = texture2D( map, vMapUv );
	#ifdef DECODE_VIDEO_TEXTURE
		sampledDiffuseColor = sRGBTransferEOTF( sampledDiffuseColor );
	#endif
	diffuseColor *= sampledDiffuseColor;
#endif`,Nm=`#ifdef USE_MAP
	uniform sampler2D map;
#endif`,Dm=`#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
	#if defined( USE_POINTS_UV )
		vec2 uv = vUv;
	#else
		vec2 uv = ( uvTransform * vec3( gl_PointCoord.x, 1.0 - gl_PointCoord.y, 1 ) ).xy;
	#endif
#endif
#ifdef USE_MAP
	diffuseColor *= texture2D( map, uv );
#endif
#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, uv ).g;
#endif`,Um=`#if defined( USE_POINTS_UV )
	varying vec2 vUv;
#else
	#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
		uniform mat3 uvTransform;
	#endif
#endif
#ifdef USE_MAP
	uniform sampler2D map;
#endif
#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,Fm=`float metalnessFactor = metalness;
#ifdef USE_METALNESSMAP
	vec4 texelMetalness = texture2D( metalnessMap, vMetalnessMapUv );
	metalnessFactor *= texelMetalness.b;
#endif`,Om=`#ifdef USE_METALNESSMAP
	uniform sampler2D metalnessMap;
#endif`,Bm=`#ifdef USE_INSTANCING_MORPH
	float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	float morphTargetBaseInfluence = texelFetch( morphTexture, ivec2( 0, gl_InstanceID ), 0 ).r;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		morphTargetInfluences[i] =  texelFetch( morphTexture, ivec2( i + 1, gl_InstanceID ), 0 ).r;
	}
#endif`,km=`#if defined( USE_MORPHCOLORS )
	#if defined( USE_COLOR_ALPHA )
		vColor *= morphTargetBaseInfluence;
	#elif defined( USE_COLOR )
		vColor.rgb *= morphTargetBaseInfluence;
	#endif
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		#if defined( USE_COLOR_ALPHA )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ) * morphTargetInfluences[ i ];
		#elif defined( USE_COLOR )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor.rgb += getMorph( gl_VertexID, i, 2 ).rgb * morphTargetInfluences[ i ];
		#endif
	}
#endif`,zm=`#ifdef USE_MORPHNORMALS
	objectNormal *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) objectNormal += getMorph( gl_VertexID, i, 1 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,Hm=`#ifdef USE_MORPHTARGETS
	#ifndef USE_INSTANCING_MORPH
		uniform float morphTargetBaseInfluence;
		uniform float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	#endif
	uniform sampler2DArray morphTargetsTexture;
	uniform ivec2 morphTargetsTextureSize;
	vec4 getMorph( const in int vertexIndex, const in int morphTargetIndex, const in int offset ) {
		int texelIndex = vertexIndex * MORPHTARGETS_TEXTURE_STRIDE + offset;
		int y = texelIndex / morphTargetsTextureSize.x;
		int x = texelIndex - y * morphTargetsTextureSize.x;
		ivec3 morphUV = ivec3( x, y, morphTargetIndex );
		return texelFetch( morphTargetsTexture, morphUV, 0 );
	}
#endif`,Gm=`#ifdef USE_MORPHTARGETS
	transformed *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) transformed += getMorph( gl_VertexID, i, 0 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,Vm=`float faceDirection = gl_FrontFacing ? 1.0 : - 1.0;
#ifdef FLAT_SHADED
	vec3 fdx = dFdx( vViewPosition );
	vec3 fdy = dFdy( vViewPosition );
	vec3 normal = normalize( cross( fdx, fdy ) );
#else
	vec3 normal = normalize( vNormal );
	#ifdef DOUBLE_SIDED
		normal *= faceDirection;
	#endif
#endif
#if defined( USE_NORMALMAP_TANGENTSPACE ) || defined( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY )
	#ifdef USE_TANGENT
		mat3 tbn = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn = getTangentFrame( - vViewPosition, normal,
		#if defined( USE_NORMALMAP )
			vNormalMapUv
		#elif defined( USE_CLEARCOAT_NORMALMAP )
			vClearcoatNormalMapUv
		#else
			vUv
		#endif
		);
	#endif
	#ifdef DOUBLE_SIDED
		tbn[0] *= faceDirection;
		tbn[1] *= faceDirection;
	#endif
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	#ifdef USE_TANGENT
		mat3 tbn2 = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn2 = getTangentFrame( - vViewPosition, normal, vClearcoatNormalMapUv );
	#endif
	#ifdef DOUBLE_SIDED
		tbn2[0] *= faceDirection;
		tbn2[1] *= faceDirection;
	#endif
#endif
vec3 nonPerturbedNormal = normal;`,Wm=`#ifdef USE_NORMALMAP_OBJECTSPACE
	normal = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	#ifdef FLIP_SIDED
		normal = - normal;
	#endif
	#ifdef DOUBLE_SIDED
		normal = normal * faceDirection;
	#endif
	normal = normalize( normalMatrix * normal );
#elif defined( USE_NORMALMAP_TANGENTSPACE )
	vec3 mapN = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	#if defined( USE_PACKED_NORMALMAP )
		mapN = vec3( mapN.xy, sqrt( saturate( 1.0 - dot( mapN.xy, mapN.xy ) ) ) );
	#endif
	mapN.xy *= normalScale;
	normal = normalize( tbn * mapN );
#elif defined( USE_BUMPMAP )
	normal = perturbNormalArb( - vViewPosition, normal, dHdxy_fwd(), faceDirection );
#endif`,Xm=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,qm=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,Ym=`#ifndef FLAT_SHADED
	vNormal = normalize( transformedNormal );
	#ifdef USE_TANGENT
		vTangent = normalize( transformedTangent );
		vBitangent = normalize( cross( vNormal, vTangent ) * tangent.w );
		#ifdef FLIP_SIDED
			vBitangent = - vBitangent;
		#endif
	#endif
#endif`,Zm=`#ifdef USE_NORMALMAP
	uniform sampler2D normalMap;
	uniform vec2 normalScale;
#endif
#ifdef USE_NORMALMAP_OBJECTSPACE
	uniform mat3 normalMatrix;
#endif
#if ! defined ( USE_TANGENT ) && ( defined ( USE_NORMALMAP_TANGENTSPACE ) || defined ( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY ) )
	mat3 getTangentFrame( vec3 eye_pos, vec3 surf_norm, vec2 uv ) {
		vec3 q0 = dFdx( eye_pos.xyz );
		vec3 q1 = dFdy( eye_pos.xyz );
		vec2 st0 = dFdx( uv.st );
		vec2 st1 = dFdy( uv.st );
		vec3 N = surf_norm;
		vec3 q1perp = cross( q1, N );
		vec3 q0perp = cross( N, q0 );
		vec3 T = q1perp * st0.x + q0perp * st1.x;
		vec3 B = q1perp * st0.y + q0perp * st1.y;
		float det = max( dot( T, T ), dot( B, B ) );
		float scale = ( det == 0.0 ) ? 0.0 : inversesqrt( det );
		return mat3( T * scale, B * scale, N );
	}
#endif`,Jm=`#ifdef USE_CLEARCOAT
	vec3 clearcoatNormal = nonPerturbedNormal;
#endif`,Km=`#ifdef USE_CLEARCOAT_NORMALMAP
	vec3 clearcoatMapN = texture2D( clearcoatNormalMap, vClearcoatNormalMapUv ).xyz * 2.0 - 1.0;
	clearcoatMapN.xy *= clearcoatNormalScale;
	clearcoatNormal = normalize( tbn2 * clearcoatMapN );
#endif`,$m=`#ifdef USE_CLEARCOATMAP
	uniform sampler2D clearcoatMap;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform sampler2D clearcoatNormalMap;
	uniform vec2 clearcoatNormalScale;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform sampler2D clearcoatRoughnessMap;
#endif`,jm=`#ifdef USE_IRIDESCENCEMAP
	uniform sampler2D iridescenceMap;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform sampler2D iridescenceThicknessMap;
#endif`,Qm=`#ifdef OPAQUE
diffuseColor.a = 1.0;
#endif
#ifdef USE_TRANSMISSION
diffuseColor.a *= material.transmissionAlpha;
#endif
gl_FragColor = vec4( outgoingLight, diffuseColor.a );`,tg=`vec3 packNormalToRGB( const in vec3 normal ) {
	return normalize( normal ) * 0.5 + 0.5;
}
vec3 unpackRGBToNormal( const in vec3 rgb ) {
	return 2.0 * rgb.xyz - 1.0;
}
const float PackUpscale = 256. / 255.;const float UnpackDownscale = 255. / 256.;const float ShiftRight8 = 1. / 256.;
const float Inv255 = 1. / 255.;
const vec4 PackFactors = vec4( 1.0, 256.0, 256.0 * 256.0, 256.0 * 256.0 * 256.0 );
const vec2 UnpackFactors2 = vec2( UnpackDownscale, 1.0 / PackFactors.g );
const vec3 UnpackFactors3 = vec3( UnpackDownscale / PackFactors.rg, 1.0 / PackFactors.b );
const vec4 UnpackFactors4 = vec4( UnpackDownscale / PackFactors.rgb, 1.0 / PackFactors.a );
vec4 packDepthToRGBA( const in float v ) {
	if( v <= 0.0 )
		return vec4( 0., 0., 0., 0. );
	if( v >= 1.0 )
		return vec4( 1., 1., 1., 1. );
	float vuf;
	float af = modf( v * PackFactors.a, vuf );
	float bf = modf( vuf * ShiftRight8, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec4( vuf * Inv255, gf * PackUpscale, bf * PackUpscale, af );
}
vec3 packDepthToRGB( const in float v ) {
	if( v <= 0.0 )
		return vec3( 0., 0., 0. );
	if( v >= 1.0 )
		return vec3( 1., 1., 1. );
	float vuf;
	float bf = modf( v * PackFactors.b, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec3( vuf * Inv255, gf * PackUpscale, bf );
}
vec2 packDepthToRG( const in float v ) {
	if( v <= 0.0 )
		return vec2( 0., 0. );
	if( v >= 1.0 )
		return vec2( 1., 1. );
	float vuf;
	float gf = modf( v * 256., vuf );
	return vec2( vuf * Inv255, gf );
}
float unpackRGBAToDepth( const in vec4 v ) {
	return dot( v, UnpackFactors4 );
}
float unpackRGBToDepth( const in vec3 v ) {
	return dot( v, UnpackFactors3 );
}
float unpackRGToDepth( const in vec2 v ) {
	return v.r * UnpackFactors2.r + v.g * UnpackFactors2.g;
}
vec4 pack2HalfToRGBA( const in vec2 v ) {
	vec4 r = vec4( v.x, fract( v.x * 255.0 ), v.y, fract( v.y * 255.0 ) );
	return vec4( r.x - r.y / 255.0, r.y, r.z - r.w / 255.0, r.w );
}
vec2 unpackRGBATo2Half( const in vec4 v ) {
	return vec2( v.x + ( v.y / 255.0 ), v.z + ( v.w / 255.0 ) );
}
float viewZToOrthographicDepth( const in float viewZ, const in float near, const in float far ) {
	return ( viewZ + near ) / ( near - far );
}
float orthographicDepthToViewZ( const in float depth, const in float near, const in float far ) {
	#ifdef USE_REVERSED_DEPTH_BUFFER
	
		return depth * ( far - near ) - far;
	#else
		return depth * ( near - far ) - near;
	#endif
}
float viewZToPerspectiveDepth( const in float viewZ, const in float near, const in float far ) {
	return ( ( near + viewZ ) * far ) / ( ( far - near ) * viewZ );
}
float perspectiveDepthToViewZ( const in float depth, const in float near, const in float far ) {
	
	#ifdef USE_REVERSED_DEPTH_BUFFER
		return ( near * far ) / ( ( near - far ) * depth - near );
	#else
		return ( near * far ) / ( ( far - near ) * depth - far );
	#endif
}`,eg=`#ifdef PREMULTIPLIED_ALPHA
	gl_FragColor.rgb *= gl_FragColor.a;
#endif`,ng=`vec4 mvPosition = vec4( transformed, 1.0 );
#ifdef USE_BATCHING
	mvPosition = batchingMatrix * mvPosition;
#endif
#ifdef USE_INSTANCING
	mvPosition = instanceMatrix * mvPosition;
#endif
mvPosition = modelViewMatrix * mvPosition;
gl_Position = projectionMatrix * mvPosition;`,ig=`#ifdef DITHERING
	gl_FragColor.rgb = dithering( gl_FragColor.rgb );
#endif`,sg=`#ifdef DITHERING
	vec3 dithering( vec3 color ) {
		float grid_position = rand( gl_FragCoord.xy );
		vec3 dither_shift_RGB = vec3( 0.25 / 255.0, -0.25 / 255.0, 0.25 / 255.0 );
		dither_shift_RGB = mix( 2.0 * dither_shift_RGB, -2.0 * dither_shift_RGB, grid_position );
		return color + dither_shift_RGB;
	}
#endif`,rg=`float roughnessFactor = roughness;
#ifdef USE_ROUGHNESSMAP
	vec4 texelRoughness = texture2D( roughnessMap, vRoughnessMapUv );
	roughnessFactor *= texelRoughness.g;
#endif`,ag=`#ifdef USE_ROUGHNESSMAP
	uniform sampler2D roughnessMap;
#endif`,og=`#if NUM_SPOT_LIGHT_COORDS > 0
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#if NUM_SPOT_LIGHT_MAPS > 0
	uniform sampler2D spotLightMap[ NUM_SPOT_LIGHT_MAPS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_SUN_LIGHT_SHADOWS > 0
		#define SUN_LIGHT_CASCADES 2
		#if defined( SHADOWMAP_TYPE_PCF )
			uniform sampler2DShadow sunShadowMap[ NUM_SUN_LIGHT_SHADOWS ];
		#else
			uniform sampler2D sunShadowMap[ NUM_SUN_LIGHT_SHADOWS ];
		#endif
		uniform mat4 sunShadowMatrix[ NUM_SUN_LIGHT_SHADOWS * SUN_LIGHT_CASCADES ];
		uniform vec4 sunShadowCascade[ NUM_SUN_LIGHT_SHADOWS * SUN_LIGHT_CASCADES ];
		varying vec4 vSunShadowWorldPosition;
		varying vec3 vSunShadowWorldNormal;
		struct SunLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SunLightShadow sunLightShadows[ NUM_SUN_LIGHT_SHADOWS ];
	#endif
	#if NUM_DIR_LIGHT_SHADOWS > 0
		#if defined( SHADOWMAP_TYPE_PCF )
			uniform sampler2DShadow directionalShadowMap[ NUM_DIR_LIGHT_SHADOWS ];
		#else
			uniform sampler2D directionalShadowMap[ NUM_DIR_LIGHT_SHADOWS ];
		#endif
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		#if defined( SHADOWMAP_TYPE_PCF )
			uniform sampler2DShadow spotShadowMap[ NUM_SPOT_LIGHT_SHADOWS ];
		#else
			uniform sampler2D spotShadowMap[ NUM_SPOT_LIGHT_SHADOWS ];
		#endif
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		#if defined( SHADOWMAP_TYPE_PCF )
			uniform samplerCubeShadow pointShadowMap[ NUM_POINT_LIGHT_SHADOWS ];
		#elif defined( SHADOWMAP_TYPE_BASIC )
			uniform samplerCube pointShadowMap[ NUM_POINT_LIGHT_SHADOWS ];
		#endif
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
	#if defined( SHADOWMAP_TYPE_PCF )
		float interleavedGradientNoise( vec2 position ) {
			return fract( 52.9829189 * fract( dot( position, vec2( 0.06711056, 0.00583715 ) ) ) );
		}
		vec2 vogelDiskSample( int sampleIndex, int samplesCount, float phi ) {
			const float goldenAngle = 2.399963229728653;
			float r = sqrt( ( float( sampleIndex ) + 0.5 ) / float( samplesCount ) );
			float theta = float( sampleIndex ) * goldenAngle + phi;
			return vec2( cos( theta ), sin( theta ) ) * r;
		}
	#endif
	#if defined( SHADOWMAP_TYPE_PCF )
		float getShadow( sampler2DShadow shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
			float shadow = 1.0;
			shadowCoord.xyz /= shadowCoord.w;
			#ifdef USE_REVERSED_DEPTH_BUFFER
				shadowCoord.z -= shadowBias;
			#else
				shadowCoord.z += shadowBias;
			#endif
			bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
			bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
			if ( frustumTest ) {
				vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
				vec2 radius = shadowRadius * texelSize;
				float phi = interleavedGradientNoise( gl_FragCoord.xy ) * PI2;
				shadow = (
					texture( shadowMap, vec3( shadowCoord.xy + vogelDiskSample( 0, 5, phi ) * radius, shadowCoord.z ) ) +
					texture( shadowMap, vec3( shadowCoord.xy + vogelDiskSample( 1, 5, phi ) * radius, shadowCoord.z ) ) +
					texture( shadowMap, vec3( shadowCoord.xy + vogelDiskSample( 2, 5, phi ) * radius, shadowCoord.z ) ) +
					texture( shadowMap, vec3( shadowCoord.xy + vogelDiskSample( 3, 5, phi ) * radius, shadowCoord.z ) ) +
					texture( shadowMap, vec3( shadowCoord.xy + vogelDiskSample( 4, 5, phi ) * radius, shadowCoord.z ) )
				) * 0.2;
			}
			return mix( 1.0, shadow, shadowIntensity );
		}
	#elif defined( SHADOWMAP_TYPE_VSM )
		float getShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
			float shadow = 1.0;
			shadowCoord.xyz /= shadowCoord.w;
			#ifdef USE_REVERSED_DEPTH_BUFFER
				shadowCoord.z -= shadowBias;
			#else
				shadowCoord.z += shadowBias;
			#endif
			bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
			bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
			if ( frustumTest ) {
				vec2 distribution = texture2D( shadowMap, shadowCoord.xy ).rg;
				float mean = distribution.x;
				float variance = distribution.y * distribution.y;
				#ifdef USE_REVERSED_DEPTH_BUFFER
					float hard_shadow = step( mean, shadowCoord.z );
				#else
					float hard_shadow = step( shadowCoord.z, mean );
				#endif
				
				if ( hard_shadow == 1.0 ) {
					shadow = 1.0;
				} else {
					variance = max( variance, 0.0000001 );
					float d = shadowCoord.z - mean;
					float p_max = variance / ( variance + d * d );
					p_max = clamp( ( p_max - 0.3 ) / 0.65, 0.0, 1.0 );
					shadow = max( hard_shadow, p_max );
				}
			}
			return mix( 1.0, shadow, shadowIntensity );
		}
	#else
		float getShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
			float shadow = 1.0;
			shadowCoord.xyz /= shadowCoord.w;
			#ifdef USE_REVERSED_DEPTH_BUFFER
				shadowCoord.z -= shadowBias;
			#else
				shadowCoord.z += shadowBias;
			#endif
			bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
			bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
			if ( frustumTest ) {
				float depth = texture2D( shadowMap, shadowCoord.xy ).r;
				#ifdef USE_REVERSED_DEPTH_BUFFER
					shadow = step( depth, shadowCoord.z );
				#else
					shadow = step( shadowCoord.z, depth );
				#endif
			}
			return mix( 1.0, shadow, shadowIntensity );
		}
	#endif
	#if NUM_SUN_LIGHT_SHADOWS > 0
		float getSunShadow(
			#if defined( SHADOWMAP_TYPE_PCF )
				sampler2DShadow shadowMap,
			#else
				sampler2D shadowMap,
			#endif
			SunLightShadow sunLightShadow,
			int shadowIndex
		) {
			vec4 shadowWorldPosition = vec4( vSunShadowWorldPosition.xyz + vSunShadowWorldNormal * sunLightShadow.shadowNormalBias, 1.0 );
			float viewDepth = vSunShadowWorldPosition.w;
			int cascadeOffset = shadowIndex * SUN_LIGHT_CASCADES;
			float shadow = 1.0;
			for ( int i = SUN_LIGHT_CASCADES - 1; i >= 0; i -- ) {
				vec4 cascade = sunShadowCascade[ cascadeOffset + i ];
				if ( viewDepth >= cascade.x && viewDepth < cascade.y ) {
					float cascadeShadow = getShadow(
						shadowMap,
						sunLightShadow.shadowMapSize,
						sunLightShadow.shadowIntensity,
						sunLightShadow.shadowBias,
						sunLightShadow.shadowRadius,
						sunShadowMatrix[ cascadeOffset + i ] * shadowWorldPosition
					);
					shadow = mix( cascadeShadow, shadow, smoothstep( cascade.z, cascade.y, viewDepth ) );
				}
			}
			return shadow;
		}
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
	#if defined( SHADOWMAP_TYPE_PCF )
	float getPointShadow( samplerCubeShadow shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord, float shadowCameraNear, float shadowCameraFar ) {
		float shadow = 1.0;
		vec3 lightToPosition = shadowCoord.xyz;
		vec3 bd3D = normalize( lightToPosition );
		vec3 absVec = abs( lightToPosition );
		float viewSpaceZ = max( max( absVec.x, absVec.y ), absVec.z );
		if ( viewSpaceZ - shadowCameraFar <= 0.0 && viewSpaceZ - shadowCameraNear >= 0.0 ) {
			float lightDistance = length( lightToPosition );
			float depthRange = shadowCameraFar - shadowCameraNear;
			#ifdef USE_REVERSED_DEPTH_BUFFER
				float depthA = - shadowCameraNear / depthRange - shadowBias;
				float depthB = shadowCameraNear * shadowCameraFar / ( depthRange * lightDistance );
			#else
				float depthA = shadowCameraFar / depthRange + shadowBias;
				float depthB = - shadowCameraNear * shadowCameraFar / ( depthRange * lightDistance );
			#endif
			float texelSize = shadowRadius / shadowMapSize.x;
			vec3 absDir = abs( bd3D );
			vec3 tangent = absDir.x > absDir.z ? vec3( 0.0, 1.0, 0.0 ) : vec3( 1.0, 0.0, 0.0 );
			tangent = normalize( cross( bd3D, tangent ) );
			vec3 bitangent = cross( bd3D, tangent );
			float phi = interleavedGradientNoise( gl_FragCoord.xy ) * PI2;
			shadow = 0.0;
			for ( int i = 0; i < 5; i ++ ) {
				vec2 offset = vogelDiskSample( i, 5, phi );
				vec3 direction = bd3D + ( tangent * offset.x + bitangent * offset.y ) * texelSize;
				vec3 absDirection = abs( direction );
				float dp = depthA + depthB / max( max( absDirection.x, absDirection.y ), absDirection.z );
				shadow += texture( shadowMap, vec4( direction, dp ) );
			}
			shadow *= 0.2;
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
	#elif defined( SHADOWMAP_TYPE_BASIC )
	float getPointShadow( samplerCube shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord, float shadowCameraNear, float shadowCameraFar ) {
		float shadow = 1.0;
		vec3 lightToPosition = shadowCoord.xyz;
		vec3 absVec = abs( lightToPosition );
		float viewSpaceZ = max( max( absVec.x, absVec.y ), absVec.z );
		if ( viewSpaceZ - shadowCameraFar <= 0.0 && viewSpaceZ - shadowCameraNear >= 0.0 ) {
			float dp = ( shadowCameraFar * ( viewSpaceZ - shadowCameraNear ) ) / ( viewSpaceZ * ( shadowCameraFar - shadowCameraNear ) );
			dp += shadowBias;
			vec3 bd3D = normalize( lightToPosition );
			float depth = textureCube( shadowMap, bd3D ).r;
			#ifdef USE_REVERSED_DEPTH_BUFFER
				depth = 1.0 - depth;
			#endif
			shadow = step( dp, depth );
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
	#endif
	#endif
#endif`,lg=`#if NUM_SPOT_LIGHT_COORDS > 0
	uniform mat4 spotLightMatrix[ NUM_SPOT_LIGHT_COORDS ];
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_SUN_LIGHT_SHADOWS > 0
		varying vec4 vSunShadowWorldPosition;
		varying vec3 vSunShadowWorldNormal;
	#endif
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform mat4 directionalShadowMatrix[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform mat4 pointShadowMatrix[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
#endif`,cg=`#if ( defined( USE_SHADOWMAP ) && ( NUM_DIR_LIGHT_SHADOWS > 0 || NUM_SUN_LIGHT_SHADOWS > 0 || NUM_POINT_LIGHT_SHADOWS > 0 ) ) || ( NUM_SPOT_LIGHT_COORDS > 0 )
	#ifdef HAS_NORMAL
		vec3 shadowWorldNormal = transformNormalByInverseViewMatrix( transformedNormal, viewMatrix );
	#else
		vec3 shadowWorldNormal = vec3( 0.0 );
	#endif
	vec4 shadowWorldPosition;
#endif
#if defined( USE_SHADOWMAP )
	#if NUM_SUN_LIGHT_SHADOWS > 0
		vSunShadowWorldPosition = vec4( worldPosition.xyz, - mvPosition.z );
		vSunShadowWorldNormal = shadowWorldNormal;
	#endif
	#if NUM_DIR_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * directionalLightShadows[ i ].shadowNormalBias, 0 );
			vDirectionalShadowCoord[ i ] = directionalShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * pointLightShadows[ i ].shadowNormalBias, 0 );
			vPointShadowCoord[ i ] = pointShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
#endif
#if NUM_SPOT_LIGHT_COORDS > 0
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_COORDS; i ++ ) {
		shadowWorldPosition = worldPosition;
		#if ( defined( USE_SHADOWMAP ) && UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
			shadowWorldPosition.xyz += shadowWorldNormal * spotLightShadows[ i ].shadowNormalBias;
		#endif
		vSpotLightCoord[ i ] = spotLightMatrix[ i ] * shadowWorldPosition;
	}
	#pragma unroll_loop_end
#endif`,hg=`float getShadowMask() {
	float shadow = 1.0;
	#ifdef USE_SHADOWMAP
	#if NUM_SUN_LIGHT_SHADOWS > 0
	SunLightShadow sunLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SUN_LIGHT_SHADOWS; i ++ ) {
		sunLight = sunLightShadows[ i ];
		shadow *= receiveShadow ? getSunShadow( sunShadowMap[ i ], sunLight, UNROLLED_LOOP_INDEX ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
		directionalLight = directionalLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( directionalShadowMap[ i ], directionalLight.shadowMapSize, directionalLight.shadowIntensity, directionalLight.shadowBias, directionalLight.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_SHADOWS; i ++ ) {
		spotLight = spotLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( spotShadowMap[ i ], spotLight.shadowMapSize, spotLight.shadowIntensity, spotLight.shadowBias, spotLight.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0 && ( defined( SHADOWMAP_TYPE_PCF ) || defined( SHADOWMAP_TYPE_BASIC ) )
	PointLightShadow pointLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
		pointLight = pointLightShadows[ i ];
		shadow *= receiveShadow ? getPointShadow( pointShadowMap[ i ], pointLight.shadowMapSize, pointLight.shadowIntensity, pointLight.shadowBias, pointLight.shadowRadius, vPointShadowCoord[ i ], pointLight.shadowCameraNear, pointLight.shadowCameraFar ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#endif
	return shadow;
}`,ug=`#ifdef USE_SKINNING
	mat4 boneMatX = getBoneMatrix( skinIndex.x );
	mat4 boneMatY = getBoneMatrix( skinIndex.y );
	mat4 boneMatZ = getBoneMatrix( skinIndex.z );
	mat4 boneMatW = getBoneMatrix( skinIndex.w );
#endif`,dg=`#ifdef USE_SKINNING
	uniform mat4 bindMatrix;
	uniform mat4 bindMatrixInverse;
	uniform highp sampler2D boneTexture;
	mat4 getBoneMatrix( const in float i ) {
		int size = textureSize( boneTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( boneTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( boneTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( boneTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( boneTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
#endif`,fg=`#ifdef USE_SKINNING
	vec4 skinVertex = bindMatrix * vec4( transformed, 1.0 );
	vec4 skinned = vec4( 0.0 );
	skinned += boneMatX * skinVertex * skinWeight.x;
	skinned += boneMatY * skinVertex * skinWeight.y;
	skinned += boneMatZ * skinVertex * skinWeight.z;
	skinned += boneMatW * skinVertex * skinWeight.w;
	transformed = ( bindMatrixInverse * skinned ).xyz;
#endif`,pg=`#ifdef USE_SKINNING
	mat4 skinMatrix = mat4( 0.0 );
	skinMatrix += skinWeight.x * boneMatX;
	skinMatrix += skinWeight.y * boneMatY;
	skinMatrix += skinWeight.z * boneMatZ;
	skinMatrix += skinWeight.w * boneMatW;
	skinMatrix = bindMatrixInverse * skinMatrix * bindMatrix;
	objectNormal = vec4( skinMatrix * vec4( objectNormal, 0.0 ) ).xyz;
	#ifdef USE_TANGENT
		objectTangent = vec4( skinMatrix * vec4( objectTangent, 0.0 ) ).xyz;
	#endif
#endif`,mg=`float specularStrength;
#ifdef USE_SPECULARMAP
	vec4 texelSpecular = texture2D( specularMap, vSpecularMapUv );
	specularStrength = texelSpecular.r;
#else
	specularStrength = 1.0;
#endif`,gg=`#ifdef USE_SPECULARMAP
	uniform sampler2D specularMap;
#endif`,_g=`#if defined( TONE_MAPPING )
	gl_FragColor.rgb = toneMapping( gl_FragColor.rgb );
#endif`,xg=`#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
uniform float toneMappingExposure;
vec3 LinearToneMapping( vec3 color ) {
	return saturate( toneMappingExposure * color );
}
vec3 ReinhardToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	return saturate( color / ( vec3( 1.0 ) + color ) );
}
vec3 CineonToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	color = max( vec3( 0.0 ), color - 0.004 );
	return pow( ( color * ( 6.2 * color + 0.5 ) ) / ( color * ( 6.2 * color + 1.7 ) + 0.06 ), vec3( 2.2 ) );
}
vec3 RRTAndODTFit( vec3 v ) {
	vec3 a = v * ( v + 0.0245786 ) - 0.000090537;
	vec3 b = v * ( 0.983729 * v + 0.4329510 ) + 0.238081;
	return a / b;
}
vec3 ACESFilmicToneMapping( vec3 color ) {
	const mat3 ACESInputMat = mat3(
		vec3( 0.59719, 0.07600, 0.02840 ),		vec3( 0.35458, 0.90834, 0.13383 ),
		vec3( 0.04823, 0.01566, 0.83777 )
	);
	const mat3 ACESOutputMat = mat3(
		vec3(  1.60475, -0.10208, -0.00327 ),		vec3( -0.53108,  1.10813, -0.07276 ),
		vec3( -0.07367, -0.00605,  1.07602 )
	);
	color *= toneMappingExposure / 0.6;
	color = ACESInputMat * color;
	color = RRTAndODTFit( color );
	color = ACESOutputMat * color;
	return saturate( color );
}
const mat3 LINEAR_REC2020_TO_LINEAR_SRGB = mat3(
	vec3( 1.6605, - 0.1246, - 0.0182 ),
	vec3( - 0.5876, 1.1329, - 0.1006 ),
	vec3( - 0.0728, - 0.0083, 1.1187 )
);
const mat3 LINEAR_SRGB_TO_LINEAR_REC2020 = mat3(
	vec3( 0.6274, 0.0691, 0.0164 ),
	vec3( 0.3293, 0.9195, 0.0880 ),
	vec3( 0.0433, 0.0113, 0.8956 )
);
vec3 agxDefaultContrastApprox( vec3 x ) {
	vec3 x2 = x * x;
	vec3 x4 = x2 * x2;
	return + 15.5 * x4 * x2
		- 40.14 * x4 * x
		+ 31.96 * x4
		- 6.868 * x2 * x
		+ 0.4298 * x2
		+ 0.1191 * x
		- 0.00232;
}
vec3 AgXToneMapping( vec3 color ) {
	const mat3 AgXInsetMatrix = mat3(
		vec3( 0.856627153315983, 0.137318972929847, 0.11189821299995 ),
		vec3( 0.0951212405381588, 0.761241990602591, 0.0767994186031903 ),
		vec3( 0.0482516061458583, 0.101439036467562, 0.811302368396859 )
	);
	const mat3 AgXOutsetMatrix = mat3(
		vec3( 1.1271005818144368, - 0.1413297634984383, - 0.14132976349843826 ),
		vec3( - 0.11060664309660323, 1.157823702216272, - 0.11060664309660294 ),
		vec3( - 0.016493938717834573, - 0.016493938717834257, 1.2519364065950405 )
	);
	const float AgxMinEv = - 12.47393;	const float AgxMaxEv = 4.026069;
	color *= toneMappingExposure;
	color = LINEAR_SRGB_TO_LINEAR_REC2020 * color;
	color = AgXInsetMatrix * color;
	color = max( color, 1e-10 );	color = log2( color );
	color = ( color - AgxMinEv ) / ( AgxMaxEv - AgxMinEv );
	color = clamp( color, 0.0, 1.0 );
	color = agxDefaultContrastApprox( color );
	color = AgXOutsetMatrix * color;
	color = pow( max( vec3( 0.0 ), color ), vec3( 2.2 ) );
	color = LINEAR_REC2020_TO_LINEAR_SRGB * color;
	color = clamp( color, 0.0, 1.0 );
	return color;
}
vec3 NeutralToneMapping( vec3 color ) {
	const float StartCompression = 0.8 - 0.04;
	const float Desaturation = 0.15;
	color *= toneMappingExposure;
	float x = min( color.r, min( color.g, color.b ) );
	float offset = x < 0.08 ? x - 6.25 * x * x : 0.04;
	color -= offset;
	float peak = max( color.r, max( color.g, color.b ) );
	if ( peak < StartCompression ) return color;
	float d = 1. - StartCompression;
	float newPeak = 1. - d * d / ( peak + d - StartCompression );
	color *= newPeak / peak;
	float g = 1. - 1. / ( Desaturation * ( peak - newPeak ) + 1. );
	return mix( color, vec3( newPeak ), g );
}
vec3 CustomToneMapping( vec3 color ) { return color; }`,yg=`#ifdef USE_TRANSMISSION
	material.transmission = transmission;
	material.transmissionAlpha = 1.0;
	material.thickness = thickness;
	material.attenuationDistance = attenuationDistance;
	material.attenuationColor = attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		material.transmission *= texture2D( transmissionMap, vTransmissionMapUv ).r;
	#endif
	#ifdef USE_THICKNESSMAP
		material.thickness *= texture2D( thicknessMap, vThicknessMapUv ).g;
	#endif
	vec3 pos = vWorldPosition;
	vec3 v = normalize( cameraPosition - pos );
	vec3 n = transformNormalByInverseViewMatrix( normal, viewMatrix );
	vec4 transmitted = getIBLVolumeRefraction(
		n, v, material.roughness, material.diffuseContribution, material.specularColorBlended, material.specularF90,
		pos, modelMatrix, viewMatrix, projectionMatrix, material.dispersion, material.ior, material.thickness,
		material.attenuationColor, material.attenuationDistance );
	material.transmissionAlpha = mix( material.transmissionAlpha, transmitted.a, material.transmission );
	totalDiffuse = mix( totalDiffuse, transmitted.rgb, material.transmission );
#endif`,vg=`#ifdef USE_TRANSMISSION
	uniform float transmission;
	uniform float thickness;
	uniform float attenuationDistance;
	uniform vec3 attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		uniform sampler2D transmissionMap;
	#endif
	#ifdef USE_THICKNESSMAP
		uniform sampler2D thicknessMap;
	#endif
	uniform vec2 transmissionSamplerSize;
	uniform sampler2D transmissionSamplerMap;
	uniform mat4 modelMatrix;
	uniform mat4 projectionMatrix;
	varying vec3 vWorldPosition;
	float w0( float a ) {
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - a + 3.0 ) - 3.0 ) + 1.0 );
	}
	float w1( float a ) {
		return ( 1.0 / 6.0 ) * ( a *  a * ( 3.0 * a - 6.0 ) + 4.0 );
	}
	float w2( float a ){
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - 3.0 * a + 3.0 ) + 3.0 ) + 1.0 );
	}
	float w3( float a ) {
		return ( 1.0 / 6.0 ) * ( a * a * a );
	}
	float g0( float a ) {
		return w0( a ) + w1( a );
	}
	float g1( float a ) {
		return w2( a ) + w3( a );
	}
	float h0( float a ) {
		return - 1.0 + w1( a ) / ( w0( a ) + w1( a ) );
	}
	float h1( float a ) {
		return 1.0 + w3( a ) / ( w2( a ) + w3( a ) );
	}
	vec4 bicubic( sampler2D tex, vec2 uv, vec4 texelSize, float lod ) {
		uv = uv * texelSize.zw + 0.5;
		vec2 iuv = floor( uv );
		vec2 fuv = fract( uv );
		float g0x = g0( fuv.x );
		float g1x = g1( fuv.x );
		float h0x = h0( fuv.x );
		float h1x = h1( fuv.x );
		float h0y = h0( fuv.y );
		float h1y = h1( fuv.y );
		vec2 p0 = ( vec2( iuv.x + h0x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p1 = ( vec2( iuv.x + h1x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p2 = ( vec2( iuv.x + h0x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		vec2 p3 = ( vec2( iuv.x + h1x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		return g0( fuv.y ) * ( g0x * textureLod( tex, p0, lod ) + g1x * textureLod( tex, p1, lod ) ) +
			g1( fuv.y ) * ( g0x * textureLod( tex, p2, lod ) + g1x * textureLod( tex, p3, lod ) );
	}
	vec4 textureBicubic( sampler2D sampler, vec2 uv, float lod ) {
		vec2 fLodSize = vec2( textureSize( sampler, int( lod ) ) );
		vec2 cLodSize = vec2( textureSize( sampler, int( lod + 1.0 ) ) );
		vec2 fLodSizeInv = 1.0 / fLodSize;
		vec2 cLodSizeInv = 1.0 / cLodSize;
		vec4 fSample = bicubic( sampler, uv, vec4( fLodSizeInv, fLodSize ), floor( lod ) );
		vec4 cSample = bicubic( sampler, uv, vec4( cLodSizeInv, cLodSize ), ceil( lod ) );
		return mix( fSample, cSample, fract( lod ) );
	}
	vec3 getVolumeTransmissionRay( const in vec3 n, const in vec3 v, const in float thickness, const in float ior, const in mat4 modelMatrix ) {
		vec3 refractionVector = refract( - v, normalize( n ), 1.0 / ior );
		vec3 modelScale;
		modelScale.x = length( vec3( modelMatrix[ 0 ].xyz ) );
		modelScale.y = length( vec3( modelMatrix[ 1 ].xyz ) );
		modelScale.z = length( vec3( modelMatrix[ 2 ].xyz ) );
		return normalize( refractionVector ) * thickness * modelScale;
	}
	float applyIorToRoughness( const in float roughness, const in float ior ) {
		return roughness * clamp( ior * 2.0 - 2.0, 0.0, 1.0 );
	}
	vec4 getTransmissionSample( const in vec2 fragCoord, const in float roughness, const in float ior ) {
		float lod = log2( transmissionSamplerSize.x ) * applyIorToRoughness( roughness, ior );
		return textureBicubic( transmissionSamplerMap, fragCoord.xy, lod );
	}
	vec3 volumeAttenuation( const in float transmissionDistance, const in vec3 attenuationColor, const in float attenuationDistance ) {
		if ( isinf( attenuationDistance ) ) {
			return vec3( 1.0 );
		} else {
			vec3 attenuationCoefficient = -log( attenuationColor ) / attenuationDistance;
			vec3 transmittance = exp( - attenuationCoefficient * transmissionDistance );			return transmittance;
		}
	}
	vec4 getIBLVolumeRefraction( const in vec3 n, const in vec3 v, const in float roughness, const in vec3 diffuseColor,
		const in vec3 specularColor, const in float specularF90, const in vec3 position, const in mat4 modelMatrix,
		const in mat4 viewMatrix, const in mat4 projMatrix, const in float dispersion, const in float ior, const in float thickness,
		const in vec3 attenuationColor, const in float attenuationDistance ) {
		vec4 transmittedLight;
		vec3 transmittance;
		#ifdef USE_DISPERSION
			float halfSpread = ( ior - 1.0 ) * 0.025 * dispersion;
			vec3 iors = vec3( ior - halfSpread, ior, ior + halfSpread );
			for ( int i = 0; i < 3; i ++ ) {
				vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, iors[ i ], modelMatrix );
				vec3 refractedRayExit = position + transmissionRay;
				vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
				vec2 refractionCoords = ndcPos.xy / ndcPos.w;
				refractionCoords += 1.0;
				refractionCoords /= 2.0;
				vec4 transmissionSample = getTransmissionSample( refractionCoords, roughness, iors[ i ] );
				transmittedLight[ i ] = transmissionSample[ i ];
				transmittedLight.a += transmissionSample.a;
				transmittance[ i ] = diffuseColor[ i ] * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance )[ i ];
			}
			transmittedLight.a /= 3.0;
		#else
			vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, ior, modelMatrix );
			vec3 refractedRayExit = position + transmissionRay;
			vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
			vec2 refractionCoords = ndcPos.xy / ndcPos.w;
			refractionCoords += 1.0;
			refractionCoords /= 2.0;
			transmittedLight = getTransmissionSample( refractionCoords, roughness, ior );
			transmittance = diffuseColor * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance );
		#endif
		vec3 attenuatedColor = transmittance * transmittedLight.rgb;
		vec3 F = EnvironmentBRDF( n, v, specularColor, specularF90, roughness );
		float transmittanceFactor = ( transmittance.r + transmittance.g + transmittance.b ) / 3.0;
		return vec4( ( 1.0 - F ) * attenuatedColor, 1.0 - ( 1.0 - transmittedLight.a ) * transmittanceFactor );
	}
#endif`,Mg=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_DIFFUSE_ROUGHNESSMAP
	varying vec2 vDiffuseRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_SPECULARMAP
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,Sg=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	uniform mat3 mapTransform;
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	uniform mat3 alphaMapTransform;
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	uniform mat3 lightMapTransform;
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	uniform mat3 aoMapTransform;
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	uniform mat3 bumpMapTransform;
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	uniform mat3 normalMapTransform;
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_DISPLACEMENTMAP
	uniform mat3 displacementMapTransform;
	varying vec2 vDisplacementMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	uniform mat3 emissiveMapTransform;
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	uniform mat3 metalnessMapTransform;
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	uniform mat3 roughnessMapTransform;
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_DIFFUSE_ROUGHNESSMAP
	uniform mat3 diffuseRoughnessMapTransform;
	varying vec2 vDiffuseRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	uniform mat3 anisotropyMapTransform;
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	uniform mat3 clearcoatMapTransform;
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform mat3 clearcoatNormalMapTransform;
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform mat3 clearcoatRoughnessMapTransform;
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	uniform mat3 sheenColorMapTransform;
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	uniform mat3 sheenRoughnessMapTransform;
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	uniform mat3 iridescenceMapTransform;
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform mat3 iridescenceThicknessMapTransform;
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SPECULARMAP
	uniform mat3 specularMapTransform;
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	uniform mat3 specularColorMapTransform;
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	uniform mat3 specularIntensityMapTransform;
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,bg=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	vUv = vec3( uv, 1 ).xy;
#endif
#ifdef USE_MAP
	vMapUv = ( mapTransform * vec3( MAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ALPHAMAP
	vAlphaMapUv = ( alphaMapTransform * vec3( ALPHAMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_LIGHTMAP
	vLightMapUv = ( lightMapTransform * vec3( LIGHTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_AOMAP
	vAoMapUv = ( aoMapTransform * vec3( AOMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_BUMPMAP
	vBumpMapUv = ( bumpMapTransform * vec3( BUMPMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_NORMALMAP
	vNormalMapUv = ( normalMapTransform * vec3( NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_DISPLACEMENTMAP
	vDisplacementMapUv = ( displacementMapTransform * vec3( DISPLACEMENTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_EMISSIVEMAP
	vEmissiveMapUv = ( emissiveMapTransform * vec3( EMISSIVEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_METALNESSMAP
	vMetalnessMapUv = ( metalnessMapTransform * vec3( METALNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ROUGHNESSMAP
	vRoughnessMapUv = ( roughnessMapTransform * vec3( ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_DIFFUSE_ROUGHNESSMAP
	vDiffuseRoughnessMapUv = ( diffuseRoughnessMapTransform * vec3( DIFFUSE_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ANISOTROPYMAP
	vAnisotropyMapUv = ( anisotropyMapTransform * vec3( ANISOTROPYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOATMAP
	vClearcoatMapUv = ( clearcoatMapTransform * vec3( CLEARCOATMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	vClearcoatNormalMapUv = ( clearcoatNormalMapTransform * vec3( CLEARCOAT_NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	vClearcoatRoughnessMapUv = ( clearcoatRoughnessMapTransform * vec3( CLEARCOAT_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCEMAP
	vIridescenceMapUv = ( iridescenceMapTransform * vec3( IRIDESCENCEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	vIridescenceThicknessMapUv = ( iridescenceThicknessMapTransform * vec3( IRIDESCENCE_THICKNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_COLORMAP
	vSheenColorMapUv = ( sheenColorMapTransform * vec3( SHEEN_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	vSheenRoughnessMapUv = ( sheenRoughnessMapTransform * vec3( SHEEN_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULARMAP
	vSpecularMapUv = ( specularMapTransform * vec3( SPECULARMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_COLORMAP
	vSpecularColorMapUv = ( specularColorMapTransform * vec3( SPECULAR_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	vSpecularIntensityMapUv = ( specularIntensityMapTransform * vec3( SPECULAR_INTENSITYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_TRANSMISSIONMAP
	vTransmissionMapUv = ( transmissionMapTransform * vec3( TRANSMISSIONMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_THICKNESSMAP
	vThicknessMapUv = ( thicknessMapTransform * vec3( THICKNESSMAP_UV, 1 ) ).xy;
#endif`,Eg=`#if defined( USE_ENVMAP ) || defined( DISTANCE ) || defined ( USE_SHADOWMAP ) || defined ( USE_TRANSMISSION ) || NUM_SPOT_LIGHT_COORDS > 0
	vec4 worldPosition = vec4( transformed, 1.0 );
	#ifdef USE_BATCHING
		worldPosition = batchingMatrix * worldPosition;
	#endif
	#ifdef USE_INSTANCING
		worldPosition = instanceMatrix * worldPosition;
	#endif
	worldPosition = modelMatrix * worldPosition;
#endif`,Tg=`varying vec2 vUv;
uniform mat3 uvTransform;
void main() {
	vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	gl_Position = vec4( position.xy, 1.0, 1.0 );
}`,wg=`uniform sampler2D t2D;
uniform float backgroundIntensity;
varying vec2 vUv;
void main() {
	vec4 texColor = texture2D( t2D, vUv );
	#ifdef DECODE_VIDEO_TEXTURE
		texColor = vec4( mix( pow( texColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), texColor.rgb * 0.0773993808, vec3( lessThanEqual( texColor.rgb, vec3( 0.04045 ) ) ) ), texColor.w );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,Ag=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,Rg=`uniform float backgroundBlurriness;
uniform float backgroundIntensity;
uniform mat3 backgroundRotation;
varying vec3 vWorldDirection;
#include <envmap_common_pars_fragment>
void main() {
	#ifdef ENVMAP_TYPE_PMREM
		vec4 texColor = textureLod( envMap, backgroundRotation * vWorldDirection, roughnessToMip( backgroundBlurriness ) );
	#else
		vec4 texColor = textureCube( envMap, backgroundRotation * vWorldDirection );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,Cg=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,Pg=`uniform samplerCube tCube;
uniform float tFlip;
uniform float opacity;
varying vec3 vWorldDirection;
void main() {
	vec4 texColor = textureCube( tCube, vec3( tFlip * vWorldDirection.x, vWorldDirection.yz ) );
	gl_FragColor = texColor;
	gl_FragColor.a *= opacity;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,Ig=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
varying vec2 vHighPrecisionZW;
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vHighPrecisionZW = gl_Position.zw;
}`,Lg=`#if DEPTH_PACKING == 3200
	uniform float opacity;
#endif
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
varying vec2 vHighPrecisionZW;
void main() {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#if DEPTH_PACKING == 3200
		diffuseColor.a = opacity;
	#endif
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <logdepthbuf_fragment>
	#ifdef USE_REVERSED_DEPTH_BUFFER
		float fragCoordZ = vHighPrecisionZW[ 0 ] / vHighPrecisionZW[ 1 ];
	#else
		float fragCoordZ = 0.5 * vHighPrecisionZW[ 0 ] / vHighPrecisionZW[ 1 ] + 0.5;
	#endif
	#if DEPTH_PACKING == 3200
		gl_FragColor = vec4( vec3( 1.0 - fragCoordZ ), opacity );
	#elif DEPTH_PACKING == 3201
		gl_FragColor = packDepthToRGBA( fragCoordZ );
	#elif DEPTH_PACKING == 3202
		gl_FragColor = vec4( packDepthToRGB( fragCoordZ ), 1.0 );
	#elif DEPTH_PACKING == 3203
		gl_FragColor = vec4( packDepthToRG( fragCoordZ ), 0.0, 1.0 );
	#endif
}`,Ng=`#define DISTANCE
varying vec3 vWorldPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <worldpos_vertex>
	#include <clipping_planes_vertex>
	vWorldPosition = worldPosition.xyz;
}`,Dg=`#define DISTANCE
uniform vec3 referencePosition;
uniform float nearDistance;
uniform float farDistance;
varying vec3 vWorldPosition;
#include <common>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	float dist = length( vWorldPosition - referencePosition );
	dist = ( dist - nearDistance ) / ( farDistance - nearDistance );
	dist = saturate( dist );
	gl_FragColor = vec4( dist, 0.0, 0.0, 1.0 );
}`,Ug=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
}`,Fg=`uniform sampler2D tEquirect;
varying vec3 vWorldDirection;
#include <common>
void main() {
	vec3 direction = normalize( vWorldDirection );
	vec2 sampleUV = equirectUv( direction );
	gl_FragColor = texture2D( tEquirect, sampleUV );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,Og=`uniform float scale;
attribute float lineDistance;
varying float vLineDistance;
#include <common>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	vLineDistance = scale * lineDistance;
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,Bg=`uniform vec3 diffuse;
uniform float opacity;
uniform float dashSize;
uniform float totalSize;
varying float vLineDistance;
#include <common>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	if ( mod( vLineDistance, totalSize ) > dashSize ) {
		discard;
	}
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,kg=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#if defined ( USE_ENVMAP ) || defined ( USE_SKINNING )
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinbase_vertex>
		#include <skinnormal_vertex>
		#include <defaultnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <fog_vertex>
}`,zg=`uniform vec3 diffuse;
uniform float opacity;
#ifndef FLAT_SHADED
	varying vec3 vNormal;
#endif
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		reflectedLight.indirectDiffuse += lightMapTexel.rgb * lightMapIntensity * RECIPROCAL_PI;
	#else
		reflectedLight.indirectDiffuse += vec3( 1.0 );
	#endif
	#include <aomap_fragment>
	reflectedLight.indirectDiffuse *= diffuseColor.rgb;
	vec3 outgoingLight = reflectedLight.indirectDiffuse;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Hg=`#define LAMBERT
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,Gg=`#define LAMBERT
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_lambert_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_lambert_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Vg=`#define MATCAP
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <displacementmap_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
	vViewPosition = - mvPosition.xyz;
}`,Wg=`#define MATCAP
uniform vec3 diffuse;
uniform float opacity;
uniform sampler2D matcap;
varying vec3 vViewPosition;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	vec3 viewDir = normalize( vViewPosition );
	vec3 x = normalize( vec3( viewDir.z, 0.0, - viewDir.x ) );
	vec3 y = cross( viewDir, x );
	vec2 uv = vec2( dot( x, normal ), dot( y, normal ) ) * 0.495 + 0.5;
	#ifdef USE_MATCAP
		vec4 matcapColor = texture2D( matcap, uv );
	#else
		vec4 matcapColor = vec4( vec3( mix( 0.2, 0.8, uv.y ) ), 1.0 );
	#endif
	vec3 outgoingLight = diffuseColor.rgb * matcapColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Xg=`#define NORMAL
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	vViewPosition = - mvPosition.xyz;
#endif
}`,qg=`#define NORMAL
uniform float opacity;
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <uv_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( 0.0, 0.0, 0.0, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	gl_FragColor = vec4( normalize( normal ) * 0.5 + 0.5, diffuseColor.a );
	#ifdef OPAQUE
		gl_FragColor.a = 1.0;
	#endif
}`,Yg=`#define PHONG
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,Zg=`#define PHONG
uniform vec3 diffuse;
uniform vec3 emissive;
uniform vec3 specular;
uniform float shininess;
uniform float opacity;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_phong_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_phong_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + reflectedLight.directSpecular + reflectedLight.indirectSpecular + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Jg=`#define STANDARD
varying vec3 vViewPosition;
#ifdef USE_TRANSMISSION
	varying vec3 vWorldPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
#ifdef USE_TRANSMISSION
	vWorldPosition = worldPosition.xyz;
#endif
}`,Kg=`#define STANDARD
#ifdef PHYSICAL
	#define IOR
	#define USE_SPECULAR
#endif
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float roughness;
uniform float metalness;
uniform float opacity;
#ifdef IOR
	uniform float ior;
#endif
#ifdef USE_SPECULAR
	uniform float specularIntensity;
	uniform vec3 specularColor;
	#ifdef USE_SPECULAR_COLORMAP
		uniform sampler2D specularColorMap;
	#endif
	#ifdef USE_SPECULAR_INTENSITYMAP
		uniform sampler2D specularIntensityMap;
	#endif
#endif
#ifdef USE_CLEARCOAT
	uniform float clearcoat;
	uniform float clearcoatRoughness;
#endif
#ifdef USE_DIFFUSE_ROUGHNESS
	uniform float diffuseRoughness;
	#ifdef USE_DIFFUSE_ROUGHNESSMAP
		uniform sampler2D diffuseRoughnessMap;
	#endif
#endif
#ifdef USE_DISPERSION
	uniform float dispersion;
#endif
#ifdef USE_RETROREFLECTION
	uniform float retroreflectivity;
#endif
#ifdef USE_IRIDESCENCE
	uniform float iridescence;
	uniform float iridescenceIOR;
	uniform float iridescenceThicknessMinimum;
	uniform float iridescenceThicknessMaximum;
#endif
#ifdef USE_SHEEN
	uniform vec3 sheenColor;
	uniform float sheenRoughness;
	#ifdef USE_SHEEN_COLORMAP
		uniform sampler2D sheenColorMap;
	#endif
	#ifdef USE_SHEEN_ROUGHNESSMAP
		uniform sampler2D sheenRoughnessMap;
	#endif
#endif
#ifdef USE_ANISOTROPY
	uniform vec2 anisotropyVector;
	#ifdef USE_ANISOTROPYMAP
		uniform sampler2D anisotropyMap;
	#endif
#endif
varying vec3 vViewPosition;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <iridescence_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_physical_pars_fragment>
#include <transmission_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <clearcoat_pars_fragment>
#include <iridescence_pars_fragment>
#include <roughnessmap_pars_fragment>
#include <metalnessmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <roughnessmap_fragment>
	#include <metalnessmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <clearcoat_normal_fragment_begin>
	#include <clearcoat_normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_physical_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 totalDiffuse = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse;
	vec3 totalSpecular = reflectedLight.directSpecular + reflectedLight.indirectSpecular;
	#include <transmission_fragment>
	vec3 outgoingLight = totalDiffuse + totalSpecular + totalEmissiveRadiance;
	#ifdef USE_SHEEN
 
		outgoingLight = outgoingLight + sheenSpecularDirect + sheenSpecularIndirect;
 
 	#endif
	#ifdef USE_CLEARCOAT
		float dotNVcc = saturate( dot( geometryClearcoatNormal, geometryViewDir ) );
		vec3 Fcc = F_Schlick( material.clearcoatF0, material.clearcoatF90, dotNVcc );
		outgoingLight = outgoingLight * ( 1.0 - material.clearcoat * Fcc ) + ( clearcoatSpecularDirect + clearcoatSpecularIndirect ) * material.clearcoat;
	#endif
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,$g=`#define TOON
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,jg=`#define TOON
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <gradientmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_toon_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_toon_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Qg=`uniform float size;
uniform float scale;
#include <common>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
#ifdef USE_POINTS_UV
	varying vec2 vUv;
	uniform mat3 uvTransform;
#endif
void main() {
	#ifdef USE_POINTS_UV
		vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	#endif
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	gl_PointSize = size;
	#ifdef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) gl_PointSize *= ( scale / - mvPosition.z );
	#endif
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <fog_vertex>
}`,t0=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <color_pars_fragment>
#include <map_particle_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_particle_fragment>
	#include <color_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,e0=`#include <common>
#include <batching_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <shadowmap_pars_vertex>
void main() {
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,n0=`uniform vec3 color;
uniform float opacity;
#include <common>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <logdepthbuf_pars_fragment>
#include <shadowmap_pars_fragment>
#include <shadowmask_pars_fragment>
void main() {
	#include <logdepthbuf_fragment>
	gl_FragColor = vec4( color, opacity * ( 1.0 - getShadowMask() ) );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,i0=`uniform float rotation;
uniform vec2 center;
#include <common>
#include <uv_pars_vertex>
#include <fog_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	vec4 mvPosition = modelViewMatrix[ 3 ];
	vec2 scale = vec2( length( modelMatrix[ 0 ].xyz ), length( modelMatrix[ 1 ].xyz ) );
	#ifndef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) scale *= - mvPosition.z;
	#endif
	vec2 alignedPosition = ( position.xy - ( center - vec2( 0.5 ) ) ) * scale;
	vec2 rotatedPosition;
	rotatedPosition.x = cos( rotation ) * alignedPosition.x - sin( rotation ) * alignedPosition.y;
	rotatedPosition.y = sin( rotation ) * alignedPosition.x + cos( rotation ) * alignedPosition.y;
	mvPosition.xy += rotatedPosition;
	gl_Position = projectionMatrix * mvPosition;
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,s0=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,_e={alphahash_fragment:wp,alphahash_pars_fragment:Ap,alphamap_fragment:Rp,alphamap_pars_fragment:Cp,alphatest_fragment:Pp,alphatest_pars_fragment:Ip,aomap_fragment:Lp,aomap_pars_fragment:Np,batching_pars_vertex:Dp,batching_vertex:Up,begin_vertex:Fp,beginnormal_vertex:Op,bsdfs:Bp,iridescence_fragment:kp,bumpmap_pars_fragment:zp,clipping_planes_fragment:Hp,clipping_planes_pars_fragment:Gp,clipping_planes_pars_vertex:Vp,clipping_planes_vertex:Wp,color_fragment:Xp,color_pars_fragment:qp,color_pars_vertex:Yp,color_vertex:Zp,common:Jp,defaultnormal_vertex:Kp,displacementmap_pars_vertex:$p,displacementmap_vertex:jp,emissivemap_fragment:Qp,emissivemap_pars_fragment:tm,colorspace_fragment:em,colorspace_pars_fragment:nm,envmap_fragment:im,envmap_common_pars_fragment:sm,envmap_pars_fragment:rm,envmap_pars_vertex:am,envmap_physical_pars_fragment:_m,envmap_vertex:om,fog_vertex:lm,fog_pars_vertex:cm,fog_fragment:hm,fog_pars_fragment:um,gradientmap_pars_fragment:dm,lightmap_pars_fragment:fm,lights_lambert_fragment:pm,lights_lambert_pars_fragment:mm,lights_pars_begin:gm,lights_toon_fragment:xm,lights_toon_pars_fragment:ym,lights_phong_fragment:vm,lights_phong_pars_fragment:Mm,lights_physical_fragment:Sm,lights_physical_pars_fragment:bm,lights_fragment_begin:Em,lights_fragment_maps:Tm,lights_fragment_end:wm,lightprobes_pars_fragment:Am,logdepthbuf_fragment:Rm,logdepthbuf_pars_fragment:Cm,logdepthbuf_pars_vertex:Pm,logdepthbuf_vertex:Im,map_fragment:Lm,map_pars_fragment:Nm,map_particle_fragment:Dm,map_particle_pars_fragment:Um,metalnessmap_fragment:Fm,metalnessmap_pars_fragment:Om,morphinstance_vertex:Bm,morphcolor_vertex:km,morphnormal_vertex:zm,morphtarget_pars_vertex:Hm,morphtarget_vertex:Gm,normal_fragment_begin:Vm,normal_fragment_maps:Wm,normal_pars_fragment:Xm,normal_pars_vertex:qm,normal_vertex:Ym,normalmap_pars_fragment:Zm,clearcoat_normal_fragment_begin:Jm,clearcoat_normal_fragment_maps:Km,clearcoat_pars_fragment:$m,iridescence_pars_fragment:jm,opaque_fragment:Qm,packing:tg,premultiplied_alpha_fragment:eg,project_vertex:ng,dithering_fragment:ig,dithering_pars_fragment:sg,roughnessmap_fragment:rg,roughnessmap_pars_fragment:ag,shadowmap_pars_fragment:og,shadowmap_pars_vertex:lg,shadowmap_vertex:cg,shadowmask_pars_fragment:hg,skinbase_vertex:ug,skinning_pars_vertex:dg,skinning_vertex:fg,skinnormal_vertex:pg,specularmap_fragment:mg,specularmap_pars_fragment:gg,tonemapping_fragment:_g,tonemapping_pars_fragment:xg,transmission_fragment:yg,transmission_pars_fragment:vg,uv_pars_fragment:Mg,uv_pars_vertex:Sg,uv_vertex:bg,worldpos_vertex:Eg,background_vert:Tg,background_frag:wg,backgroundCube_vert:Ag,backgroundCube_frag:Rg,cube_vert:Cg,cube_frag:Pg,depth_vert:Ig,depth_frag:Lg,distance_vert:Ng,distance_frag:Dg,equirect_vert:Ug,equirect_frag:Fg,linedashed_vert:Og,linedashed_frag:Bg,meshbasic_vert:kg,meshbasic_frag:zg,meshlambert_vert:Hg,meshlambert_frag:Gg,meshmatcap_vert:Vg,meshmatcap_frag:Wg,meshnormal_vert:Xg,meshnormal_frag:qg,meshphong_vert:Yg,meshphong_frag:Zg,meshphysical_vert:Jg,meshphysical_frag:Kg,meshtoon_vert:$g,meshtoon_frag:jg,points_vert:Qg,points_frag:t0,shadow_vert:e0,shadow_frag:n0,sprite_vert:i0,sprite_frag:s0},Ut={common:{diffuse:{value:new fe(16777215)},opacity:{value:1},map:{value:null},mapTransform:{value:new ae},alphaMap:{value:null},alphaMapTransform:{value:new ae},alphaTest:{value:0}},specularmap:{specularMap:{value:null},specularMapTransform:{value:new ae}},envmap:{envMap:{value:null},envMapRotation:{value:new ae},reflectivity:{value:1},ior:{value:1.5},refractionRatio:{value:.98},dfgLUT:{value:null}},aomap:{aoMap:{value:null},aoMapIntensity:{value:1},aoMapTransform:{value:new ae}},lightmap:{lightMap:{value:null},lightMapIntensity:{value:1},lightMapTransform:{value:new ae}},bumpmap:{bumpMap:{value:null},bumpMapTransform:{value:new ae},bumpScale:{value:1}},normalmap:{normalMap:{value:null},normalMapTransform:{value:new ae},normalScale:{value:new kt(1,1)}},displacementmap:{displacementMap:{value:null},displacementMapTransform:{value:new ae},displacementScale:{value:1},displacementBias:{value:0}},emissivemap:{emissiveMap:{value:null},emissiveMapTransform:{value:new ae}},metalnessmap:{metalnessMap:{value:null},metalnessMapTransform:{value:new ae}},roughnessmap:{roughnessMap:{value:null},roughnessMapTransform:{value:new ae}},gradientmap:{gradientMap:{value:null}},fog:{fogDensity:{value:25e-5},fogNear:{value:1},fogFar:{value:2e3},fogColor:{value:new fe(16777215)}},lights:{ambientLightColor:{value:[]},lightProbe:{value:[]},sunLights:{value:[],properties:{direction:{},color:{}}},sunLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},sunShadowMatrix:{value:[]},sunShadowCascade:{value:[]},directionalLights:{value:[],properties:{direction:{},color:{}}},directionalLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},directionalShadowMatrix:{value:[]},spotLights:{value:[],properties:{color:{},position:{},direction:{},distance:{},coneCos:{},penumbraCos:{},decay:{}}},spotLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},spotLightMap:{value:[]},spotLightMatrix:{value:[]},pointLights:{value:[],properties:{color:{},position:{},decay:{},distance:{}}},pointLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{},shadowCameraNear:{},shadowCameraFar:{}}},pointShadowMatrix:{value:[]},hemisphereLights:{value:[],properties:{direction:{},skyColor:{},groundColor:{}}},rectAreaLights:{value:[],properties:{color:{},position:{},width:{},height:{}}},ltc_1:{value:null},ltc_2:{value:null},probesSH:{value:[]},probesMin:{value:[]},probesMax:{value:[]},probesResolution:{value:[]}},points:{diffuse:{value:new fe(16777215)},opacity:{value:1},size:{value:1},scale:{value:1},map:{value:null},alphaMap:{value:null},alphaMapTransform:{value:new ae},alphaTest:{value:0},uvTransform:{value:new ae}},sprite:{diffuse:{value:new fe(16777215)},opacity:{value:1},center:{value:new kt(.5,.5)},rotation:{value:0},map:{value:null},mapTransform:{value:new ae},alphaMap:{value:null},alphaMapTransform:{value:new ae},alphaTest:{value:0}}},Ii={basic:{uniforms:Cn([Ut.common,Ut.specularmap,Ut.envmap,Ut.aomap,Ut.lightmap,Ut.fog]),vertexShader:_e.meshbasic_vert,fragmentShader:_e.meshbasic_frag},lambert:{uniforms:Cn([Ut.common,Ut.specularmap,Ut.envmap,Ut.aomap,Ut.lightmap,Ut.emissivemap,Ut.bumpmap,Ut.normalmap,Ut.displacementmap,Ut.fog,Ut.lights,{emissive:{value:new fe(0)},envMapIntensity:{value:1}}]),vertexShader:_e.meshlambert_vert,fragmentShader:_e.meshlambert_frag},phong:{uniforms:Cn([Ut.common,Ut.specularmap,Ut.envmap,Ut.aomap,Ut.lightmap,Ut.emissivemap,Ut.bumpmap,Ut.normalmap,Ut.displacementmap,Ut.fog,Ut.lights,{emissive:{value:new fe(0)},specular:{value:new fe(1118481)},shininess:{value:30},envMapIntensity:{value:1}}]),vertexShader:_e.meshphong_vert,fragmentShader:_e.meshphong_frag},standard:{uniforms:Cn([Ut.common,Ut.envmap,Ut.aomap,Ut.lightmap,Ut.emissivemap,Ut.bumpmap,Ut.normalmap,Ut.displacementmap,Ut.roughnessmap,Ut.metalnessmap,Ut.fog,Ut.lights,{emissive:{value:new fe(0)},roughness:{value:1},metalness:{value:0},envMapIntensity:{value:1}}]),vertexShader:_e.meshphysical_vert,fragmentShader:_e.meshphysical_frag},toon:{uniforms:Cn([Ut.common,Ut.aomap,Ut.lightmap,Ut.emissivemap,Ut.bumpmap,Ut.normalmap,Ut.displacementmap,Ut.gradientmap,Ut.fog,Ut.lights,{emissive:{value:new fe(0)}}]),vertexShader:_e.meshtoon_vert,fragmentShader:_e.meshtoon_frag},matcap:{uniforms:Cn([Ut.common,Ut.bumpmap,Ut.normalmap,Ut.displacementmap,Ut.fog,{matcap:{value:null}}]),vertexShader:_e.meshmatcap_vert,fragmentShader:_e.meshmatcap_frag},points:{uniforms:Cn([Ut.points,Ut.fog]),vertexShader:_e.points_vert,fragmentShader:_e.points_frag},dashed:{uniforms:Cn([Ut.common,Ut.fog,{scale:{value:1},dashSize:{value:1},totalSize:{value:2}}]),vertexShader:_e.linedashed_vert,fragmentShader:_e.linedashed_frag},depth:{uniforms:Cn([Ut.common,Ut.displacementmap]),vertexShader:_e.depth_vert,fragmentShader:_e.depth_frag},normal:{uniforms:Cn([Ut.common,Ut.bumpmap,Ut.normalmap,Ut.displacementmap,{opacity:{value:1}}]),vertexShader:_e.meshnormal_vert,fragmentShader:_e.meshnormal_frag},sprite:{uniforms:Cn([Ut.sprite,Ut.fog]),vertexShader:_e.sprite_vert,fragmentShader:_e.sprite_frag},background:{uniforms:{uvTransform:{value:new ae},t2D:{value:null},backgroundIntensity:{value:1}},vertexShader:_e.background_vert,fragmentShader:_e.background_frag},backgroundCube:{uniforms:{envMap:{value:null},backgroundBlurriness:{value:0},backgroundIntensity:{value:1},backgroundRotation:{value:new ae}},vertexShader:_e.backgroundCube_vert,fragmentShader:_e.backgroundCube_frag},cube:{uniforms:{tCube:{value:null},tFlip:{value:-1},opacity:{value:1}},vertexShader:_e.cube_vert,fragmentShader:_e.cube_frag},equirect:{uniforms:{tEquirect:{value:null}},vertexShader:_e.equirect_vert,fragmentShader:_e.equirect_frag},distance:{uniforms:Cn([Ut.common,Ut.displacementmap,{referencePosition:{value:new D},nearDistance:{value:1},farDistance:{value:1e3}}]),vertexShader:_e.distance_vert,fragmentShader:_e.distance_frag},shadow:{uniforms:Cn([Ut.lights,Ut.fog,{color:{value:new fe(0)},opacity:{value:1}}]),vertexShader:_e.shadow_vert,fragmentShader:_e.shadow_frag}};Ii.physical={uniforms:Cn([Ii.standard.uniforms,{clearcoat:{value:0},clearcoatMap:{value:null},clearcoatMapTransform:{value:new ae},clearcoatNormalMap:{value:null},clearcoatNormalMapTransform:{value:new ae},clearcoatNormalScale:{value:new kt(1,1)},clearcoatRoughness:{value:0},clearcoatRoughnessMap:{value:null},clearcoatRoughnessMapTransform:{value:new ae},diffuseRoughness:{value:0},diffuseRoughnessMap:{value:null},diffuseRoughnessMapTransform:{value:new ae},dispersion:{value:0},retroreflectivity:{value:0},iridescence:{value:0},iridescenceMap:{value:null},iridescenceMapTransform:{value:new ae},iridescenceIOR:{value:1.3},iridescenceThicknessMinimum:{value:100},iridescenceThicknessMaximum:{value:400},iridescenceThicknessMap:{value:null},iridescenceThicknessMapTransform:{value:new ae},sheen:{value:0},sheenColor:{value:new fe(0)},sheenColorMap:{value:null},sheenColorMapTransform:{value:new ae},sheenRoughness:{value:1},sheenRoughnessMap:{value:null},sheenRoughnessMapTransform:{value:new ae},transmission:{value:0},transmissionMap:{value:null},transmissionMapTransform:{value:new ae},transmissionSamplerSize:{value:new kt},transmissionSamplerMap:{value:null},thickness:{value:0},thicknessMap:{value:null},thicknessMapTransform:{value:new ae},attenuationDistance:{value:0},attenuationColor:{value:new fe(0)},specularColor:{value:new fe(1,1,1)},specularColorMap:{value:null},specularColorMapTransform:{value:new ae},specularIntensity:{value:1},specularIntensityMap:{value:null},specularIntensityMapTransform:{value:new ae},anisotropyVector:{value:new kt},anisotropyMap:{value:null},anisotropyMapTransform:{value:new ae}}]),vertexShader:_e.meshphysical_vert,fragmentShader:_e.meshphysical_frag};var Nl={r:0,b:0,g:0},r0=new Ge,Bd=new ae;Bd.set(-1,0,0,0,1,0,0,0,1);function a0(i,t,e,n,s,r){let a=new fe(0),o=s===!0?0:1,l,c,h=null,f=0,d=null;function p(E){let P=E.isScene===!0?E.background:null;if(P&&P.isTexture){let T=E.backgroundBlurriness>0;P=t.get(P,T)}return P}function x(E){let P=!1,T=p(E);T===null?m(a,o):T&&T.isColor&&(m(T,1),P=!0);let C=i.xr.getEnvironmentBlendMode();C==="additive"?e.buffers.color.setClear(0,0,0,1,r):C==="alpha-blend"&&e.buffers.color.setClear(0,0,0,0,r),(i.autoClear||P)&&(e.buffers.depth.setTest(!0),e.buffers.depth.setMask(!0),e.buffers.color.setMask(!0),i.clear(i.autoClearColor,i.autoClearDepth,i.autoClearStencil))}function S(E,P){let T=p(P);T&&T.isCubeTexture?(c===void 0&&(c=new Qt(new mi(1,1,1),new ai({name:"BackgroundCubeMaterial",uniforms:Ds(Ii.backgroundCube.uniforms),vertexShader:Ii.backgroundCube.vertexShader,fragmentShader:Ii.backgroundCube.fragmentShader,side:vn,depthTest:!1,depthWrite:!1,fog:!1,allowOverride:!1})),c.geometry.deleteAttribute("normal"),c.geometry.deleteAttribute("uv"),c.onBeforeRender=function(C,A,_){this.matrixWorld.copyPosition(_.matrixWorld)},Object.defineProperty(c.material,"envMap",{get:function(){return this.uniforms.envMap.value}}),n.update(c)),c.material.uniforms.envMap.value=T,c.material.uniforms.backgroundBlurriness.value=P.backgroundBlurriness,c.material.uniforms.backgroundIntensity.value=P.backgroundIntensity,c.material.uniforms.backgroundRotation.value.setFromMatrix4(r0.makeRotationFromEuler(P.backgroundRotation)).transpose(),T.isRenderTargetTexture===!1&&c.material.uniforms.backgroundRotation.value.premultiply(Bd),c.material.toneMapped=be.getTransfer(T.colorSpace)!==De,(h!==T||f!==T.version||d!==i.toneMapping)&&(c.material.needsUpdate=!0,h=T,f=T.version,d=i.toneMapping),c.layers.enableAll(),E.unshift(c,c.geometry,c.material,0,0,null)):T&&T.isTexture&&(l===void 0&&(l=new Qt(new Wi(2,2),new ai({name:"BackgroundMaterial",uniforms:Ds(Ii.background.uniforms),vertexShader:Ii.background.vertexShader,fragmentShader:Ii.background.fragmentShader,side:_s,depthTest:!1,depthWrite:!1,fog:!1,allowOverride:!1})),l.geometry.deleteAttribute("normal"),Object.defineProperty(l.material,"map",{get:function(){return this.uniforms.t2D.value}}),n.update(l)),l.material.uniforms.t2D.value=T,l.material.uniforms.backgroundIntensity.value=P.backgroundIntensity,l.material.toneMapped=be.getTransfer(T.colorSpace)!==De,T.matrixAutoUpdate===!0&&T.updateMatrix(),l.material.uniforms.uvTransform.value.copy(T.matrix),(h!==T||f!==T.version||d!==i.toneMapping)&&(l.material.needsUpdate=!0,h=T,f=T.version,d=i.toneMapping),l.layers.enableAll(),E.unshift(l,l.geometry,l.material,0,0,null))}function m(E,P){E.getRGB(Nl,dh(i)),e.buffers.color.setClear(Nl.r,Nl.g,Nl.b,P,r)}function g(){c!==void 0&&(c.geometry.dispose(),c.material.dispose(),c=void 0),l!==void 0&&(l.geometry.dispose(),l.material.dispose(),l=void 0)}return{getClearColor:function(){return a},setClearColor:function(E,P=1){a.set(E),o=P,m(a,o)},getClearAlpha:function(){return o},setClearAlpha:function(E){o=E,m(a,o)},render:x,addToRenderList:S,dispose:g}}function o0(i,t){let e=i.getParameter(i.MAX_VERTEX_ATTRIBS),n={},s=d(null),r=s,a=!1;function o(k,H,K,U,Y){let tt=!1,j=f(k,U,K,H);r!==j&&(r=j,c(r.object)),tt=p(k,U,K,Y),tt&&x(k,U,K,Y),Y!==null&&t.update(Y,i.ELEMENT_ARRAY_BUFFER),(tt||a)&&(a=!1,T(k,H,K,U),Y!==null&&i.bindBuffer(i.ELEMENT_ARRAY_BUFFER,t.get(Y).buffer))}function l(){return i.createVertexArray()}function c(k){return i.bindVertexArray(k)}function h(k){return i.deleteVertexArray(k)}function f(k,H,K,U){let Y=U.wireframe===!0,tt=n[H.id];tt===void 0&&(tt={},n[H.id]=tt);let j=k.isInstancedMesh===!0?k.id:0,dt=tt[j];dt===void 0&&(dt={},tt[j]=dt);let V=dt[K.id];V===void 0&&(V={},dt[K.id]=V);let it=V[Y];return it===void 0&&(it=d(l()),V[Y]=it),it}function d(k){let H=[],K=[],U=[];for(let Y=0;Y<e;Y++)H[Y]=0,K[Y]=0,U[Y]=0;return{geometry:null,program:null,wireframe:!1,newAttributes:H,enabledAttributes:K,attributeDivisors:U,object:k,attributes:{},index:null}}function p(k,H,K,U){let Y=r.attributes,tt=H.attributes,j=0,dt=K.getAttributes();for(let V in dt)if(dt[V].location>=0){let ft=Y[V],Gt=tt[V];if(Gt===void 0&&(V==="instanceMatrix"&&k.instanceMatrix&&(Gt=k.instanceMatrix),V==="instanceColor"&&k.instanceColor&&(Gt=k.instanceColor)),ft===void 0||ft.attribute!==Gt||Gt&&ft.data!==Gt.data)return!0;j++}return r.attributesNum!==j||r.index!==U}function x(k,H,K,U){let Y={},tt=H.attributes,j=0,dt=K.getAttributes();for(let V in dt)if(dt[V].location>=0){let ft=tt[V];ft===void 0&&(V==="instanceMatrix"&&k.instanceMatrix&&(ft=k.instanceMatrix),V==="instanceColor"&&k.instanceColor&&(ft=k.instanceColor));let Gt={};Gt.attribute=ft,ft&&ft.data&&(Gt.data=ft.data),Y[V]=Gt,j++}r.attributes=Y,r.attributesNum=j,r.index=U}function S(){let k=r.newAttributes;for(let H=0,K=k.length;H<K;H++)k[H]=0}function m(k){g(k,0)}function g(k,H){let K=r.newAttributes,U=r.enabledAttributes,Y=r.attributeDivisors;K[k]=1,U[k]===0&&(i.enableVertexAttribArray(k),U[k]=1),Y[k]!==H&&(i.vertexAttribDivisor(k,H),Y[k]=H)}function E(){let k=r.newAttributes,H=r.enabledAttributes;for(let K=0,U=H.length;K<U;K++)H[K]!==k[K]&&(i.disableVertexAttribArray(K),H[K]=0)}function P(k,H,K,U,Y,tt,j){j===!0?i.vertexAttribIPointer(k,H,K,Y,tt):i.vertexAttribPointer(k,H,K,U,Y,tt)}function T(k,H,K,U){S();let Y=U.attributes,tt=K.getAttributes(),j=H.defaultAttributeValues;for(let dt in tt){let V=tt[dt];if(V.location>=0){let it=Y[dt];if(it===void 0&&(dt==="instanceMatrix"&&k.instanceMatrix&&(it=k.instanceMatrix),dt==="instanceColor"&&k.instanceColor&&(it=k.instanceColor)),it!==void 0){let ft=it.normalized,Gt=it.itemSize,ee=t.get(it);if(ee===void 0)continue;let at=ee.buffer,It=ee.type,Ft=ee.bytesPerElement,qt=It===i.INT||It===i.UNSIGNED_INT||it.gpuType===Ko;if(it.isInterleavedBufferAttribute){let pt=it.data,oe=pt.isInterleavedBuffer===!0?pt.stride:pt.itemSize,$t=it.offset;if(pt.isInstancedInterleavedBuffer||pt.isInstancedBufferAttribute){for(let zt=0;zt<V.locationSize;zt++)g(V.location+zt,pt.meshPerAttribute);k.isInstancedMesh!==!0&&U._maxInstanceCount===void 0&&(U._maxInstanceCount=pt.meshPerAttribute*pt.count)}else for(let zt=0;zt<V.locationSize;zt++)m(V.location+zt);i.bindBuffer(i.ARRAY_BUFFER,at);for(let zt=0;zt<V.locationSize;zt++)P(V.location+zt,Gt/V.locationSize,It,ft,oe*Ft,($t+Gt/V.locationSize*zt)*Ft,qt)}else{if(it.isInstancedBufferAttribute){for(let pt=0;pt<V.locationSize;pt++)g(V.location+pt,it.meshPerAttribute);k.isInstancedMesh!==!0&&U._maxInstanceCount===void 0&&(U._maxInstanceCount=it.meshPerAttribute*it.count)}else for(let pt=0;pt<V.locationSize;pt++)m(V.location+pt);i.bindBuffer(i.ARRAY_BUFFER,at);for(let pt=0;pt<V.locationSize;pt++)P(V.location+pt,Gt/V.locationSize,It,ft,Gt*Ft,Gt/V.locationSize*pt*Ft,qt)}}else if(j!==void 0){let ft=j[dt];if(ft!==void 0)switch(ft.length){case 2:i.vertexAttrib2fv(V.location,ft);break;case 3:i.vertexAttrib3fv(V.location,ft);break;case 4:i.vertexAttrib4fv(V.location,ft);break;default:i.vertexAttrib1fv(V.location,ft)}}}}E()}function C(){G();for(let k in n){let H=n[k];for(let K in H){let U=H[K];for(let Y in U){let tt=U[Y];for(let j in tt)h(tt[j].object),delete tt[j];delete U[Y]}}delete n[k]}}function A(k){if(n[k.id]===void 0)return;let H=n[k.id];for(let K in H){let U=H[K];for(let Y in U){let tt=U[Y];for(let j in tt)h(tt[j].object),delete tt[j];delete U[Y]}}delete n[k.id]}function _(k){for(let H in n){let K=n[H];for(let U in K){let Y=K[U];if(Y[k.id]===void 0)continue;let tt=Y[k.id];for(let j in tt)h(tt[j].object),delete tt[j];delete Y[k.id]}}}function b(k){for(let H in n){let K=n[H],U=k.isInstancedMesh===!0?k.id:0,Y=K[U];if(Y!==void 0){for(let tt in Y){let j=Y[tt];for(let dt in j)h(j[dt].object),delete j[dt];delete Y[tt]}delete K[U],Object.keys(K).length===0&&delete n[H]}}}function G(){B(),a=!0,r!==s&&(r=s,c(r.object))}function B(){s.geometry=null,s.program=null,s.wireframe=!1}return{setup:o,reset:G,resetDefaultState:B,dispose:C,releaseStatesOfGeometry:A,releaseStatesOfObject:b,releaseStatesOfProgram:_,initAttributes:S,enableAttribute:m,disableUnusedAttributes:E}}function l0(i,t,e){let n;function s(l){n=l}function r(l,c){i.drawArrays(n,l,c),e.update(c,n,1)}function a(l,c,h){h!==0&&(i.drawArraysInstanced(n,l,c,h),e.update(c,n,h))}function o(l,c,h){if(h===0)return;t.get("WEBGL_multi_draw").multiDrawArraysWEBGL(n,l,0,c,0,h);let d=0;for(let p=0;p<h;p++)d+=c[p];e.update(d,n,1)}this.setMode=s,this.render=r,this.renderInstances=a,this.renderMultiDraw=o}function c0(i,t,e,n){let s;function r(){if(s!==void 0)return s;if(t.has("EXT_texture_filter_anisotropic")===!0){let _=t.get("EXT_texture_filter_anisotropic");s=i.getParameter(_.MAX_TEXTURE_MAX_ANISOTROPY_EXT)}else s=0;return s}function a(_){return!(_!==yi&&n.convert(_)!==i.getParameter(i.IMPLEMENTATION_COLOR_READ_FORMAT))}function o(_){let b=_===xi&&(t.has("EXT_color_buffer_half_float")||t.has("EXT_color_buffer_float"));return!(_!==Hn&&_!==_i&&!b&&n.convert(_)!==i.getParameter(i.IMPLEMENTATION_COLOR_READ_TYPE))}function l(_){if(_==="highp"){if(i.getShaderPrecisionFormat(i.VERTEX_SHADER,i.HIGH_FLOAT).precision>0&&i.getShaderPrecisionFormat(i.FRAGMENT_SHADER,i.HIGH_FLOAT).precision>0)return"highp";_="mediump"}return _==="mediump"&&i.getShaderPrecisionFormat(i.VERTEX_SHADER,i.MEDIUM_FLOAT).precision>0&&i.getShaderPrecisionFormat(i.FRAGMENT_SHADER,i.MEDIUM_FLOAT).precision>0?"mediump":"lowp"}let c=e.precision!==void 0?e.precision:"highp",h=l(c);h!==c&&(Kt("WebGLRenderer:",c,"not supported, using",h,"instead."),c=h);let f=e.reversedDepthBuffer===!0&&t.has("EXT_clip_control"),d=e.logarithmicDepthBuffer===!0&&f===!1;e.reversedDepthBuffer===!0&&f===!1&&Kt("WebGLRenderer: Unable to use reversed depth buffer due to missing EXT_clip_control extension. Fallback to default depth buffer."),e.logarithmicDepthBuffer===!0&&f===!0&&Kt("WebGLRenderer: Logarithmic depth buffer is ignored when reversed depth buffer is enabled.");let p=i.getParameter(i.MAX_TEXTURE_IMAGE_UNITS),x=i.getParameter(i.MAX_VERTEX_TEXTURE_IMAGE_UNITS),S=i.getParameter(i.MAX_TEXTURE_SIZE),m=i.getParameter(i.MAX_CUBE_MAP_TEXTURE_SIZE),g=i.getParameter(i.MAX_VERTEX_ATTRIBS),E=i.getParameter(i.MAX_VERTEX_UNIFORM_VECTORS),P=i.getParameter(i.MAX_VARYING_VECTORS),T=i.getParameter(i.MAX_FRAGMENT_UNIFORM_VECTORS),C=i.getParameter(i.MAX_SAMPLES),A=i.getParameter(i.SAMPLES);return{isWebGL2:!0,getMaxAnisotropy:r,getMaxPrecision:l,textureFormatReadable:a,textureTypeReadable:o,precision:c,logarithmicDepthBuffer:d,reversedDepthBuffer:f,maxTextures:p,maxVertexTextures:x,maxTextureSize:S,maxCubemapSize:m,maxAttributes:g,maxVertexUniforms:E,maxVaryings:P,maxFragmentUniforms:T,maxSamples:C,samples:A}}function h0(i){let t=this,e=null,n=0,s=!1,r=!1,a=new Yn,o=new ae,l={value:null,needsUpdate:!1};this.uniform=l,this.numPlanes=0,this.numIntersection=0,this.init=function(f,d){let p=f.length!==0||d||n!==0||s;return s=d,n=f.length,p},this.beginShadows=function(){r=!0,h(null)},this.endShadows=function(){r=!1},this.setGlobalState=function(f,d){e=h(f,d,0)},this.setState=function(f,d,p){let x=f.clippingPlanes,S=f.clipIntersection,m=f.clipShadows,g=i.get(f);if(!s||x===null||x.length===0||r&&!m)r?h(null):c();else{let E=r?0:n,P=E*4,T=g.clippingState||null;l.value=T,T=h(x,d,P,p);for(let C=0;C!==P;++C)T[C]=e[C];g.clippingState=T,this.numIntersection=S?this.numPlanes:0,this.numPlanes+=E}};function c(){l.value!==e&&(l.value=e,l.needsUpdate=n>0),t.numPlanes=n,t.numIntersection=0}function h(f,d,p,x){let S=f!==null?f.length:0,m=null;if(S!==0){if(m=l.value,x!==!0||m===null){let g=p+S*4,E=d.matrixWorldInverse;o.getNormalMatrix(E),(m===null||m.length<g)&&(m=new Float32Array(g));for(let P=0,T=p;P!==S;++P,T+=4)a.copy(f[P]).applyMatrix4(E,o),a.normal.toArray(m,T),m[T+3]=a.constant}l.value=m,l.needsUpdate=!0}return t.numPlanes=S,t.numIntersection=0,m}}var ya=class extends Zn{constructor(t=1,e={}){super(t,t,e),this.isWebGLCubeRenderTarget=!0;let n={width:t,height:t,depth:1},s=[n,n,n,n,n,n];this.texture=new jr(s),this._setTextureOptions(e),this.texture.isRenderTargetTexture=!0}fromEquirectangularTexture(t,e){this.texture.type=e.type,this.texture.colorSpace=e.colorSpace,this.texture.generateMipmaps=e.generateMipmaps,this.texture.minFilter=e.minFilter,this.texture.magFilter=e.magFilter;let n={uniforms:{tEquirect:{value:null}},vertexShader:`

				varying vec3 vWorldDirection;

				vec3 transformDirection( in vec3 dir, in mat4 matrix ) {

					return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );

				}

				void main() {

					vWorldDirection = transformDirection( position, modelMatrix );

					#include <begin_vertex>
					#include <project_vertex>

				}
			`,fragmentShader:`

				uniform sampler2D tEquirect;

				varying vec3 vWorldDirection;

				#include <common>

				void main() {

					vec3 direction = normalize( vWorldDirection );

					vec2 sampleUV = equirectUv( direction );

					gl_FragColor = texture2D( tEquirect, sampleUV );

				}
			`},s=new mi(5,5,5),r=new ai({name:"CubemapFromEquirect",uniforms:Ds(n.uniforms),vertexShader:n.vertexShader,fragmentShader:n.fragmentShader,side:vn,blending:Ps});r.uniforms.tEquirect.value=e;let a=new Qt(s,r),o=e.minFilter;return e.minFilter===qi&&(e.minFilter=Ln),new pr(1,10,this).update(t,a),e.minFilter=o,a.geometry.dispose(),a.material.dispose(),this}clear(t,e=!0,n=!0,s=!0){let r=t.getRenderTarget();for(let a=0;a<6;a++)t.setRenderTarget(this,a),t.clear(e,n,s);t.setRenderTarget(r)}},gd=256,u0=3,d0=20,kd=256,zd=16,f0=3,p0=new D,m0=new fe,Sr=class i{constructor(t){this._renderer=t,this._cubeSize=0,this._sourceTarget=null,this._cubeCamera=new pr(1,10,null),this._boxMesh=new Qt(new mi(5,5,5),null),this._cubemapMaterial=null,this._equirectMaterial=null,this._blurMaterial=null,this._ggxMaterial=null,this._integrationMaterial=null}fromScene(t,e=0,n=.1,s=100,r={}){let{size:a=256,position:o=p0}=r,l=this._renderer;this._setSize(a);let c=this._allocateTarget(),h=this._getSourceTarget(!0);e>0&&(h.texture.mipmapsAutoUpdate=!1);let f=l.autoClear,d=l.autoClearColor,p=l.autoClearDepth,x=l.autoClearStencil,S=t.background;l.autoClear=!0,l.autoClearColor=!0,l.autoClearDepth=!0,l.autoClearStencil=!0,S===null&&(t.background=l.getClearColor(m0));let m=new pr(n,s,h);return m.position.copy(o),m.update(l,t),l.autoClear=f,l.autoClearColor=d,l.autoClearDepth=p,l.autoClearStencil=x,t.background=S,e>0&&(h.texture.mipmapsAutoUpdate=!0,this._blur(c,e)),this._applyPMREM(c),c}fromEquirectangular(t,e=null){return this._fromTexture(t,e)}fromCubemap(t,e=null){return this._fromTexture(t,e)}compileCubemapShader(){this._cubemapMaterial===null&&(this._cubemapMaterial=yd(),this._compileMaterial(this._cubemapMaterial))}compileEquirectangularShader(){this._equirectMaterial===null&&(this._equirectMaterial=xd(),this._compileMaterial(this._equirectMaterial))}dispose(){this._sourceTarget!==null&&this._sourceTarget.dispose(),this._cubemapMaterial!==null&&this._cubemapMaterial.dispose(),this._equirectMaterial!==null&&this._equirectMaterial.dispose(),this._blurMaterial!==null&&this._blurMaterial.dispose(),this._ggxMaterial!==null&&this._ggxMaterial.dispose(),this._integrationMaterial!==null&&this._integrationMaterial.dispose(),this._boxMesh.geometry.dispose()}static lodToRoughness(t,e){return e>0?1-Math.sqrt(1-t/e):0}_setSize(t){this._cubeSize=Math.max(gd,lh(t))}_fromTexture(t,e){t.mapping===Ls||t.mapping===xr?this._setSize(t.image.length===0?gd:t.image[0].width||t.image[0].image.width):this._setSize(t.image.width/4);let n=e||this._allocateTarget();return this._textureToCubemap(t),this._applyPMREM(n),n}_allocateTarget(){let t=this._cubeSize,e=_d(t,!1,!1),n=Math.log2(t)-u0;for(let s=0;s<=n;s++)e.texture.mipmaps.push({width:t>>s,height:t>>s});return e.texture.name="PMREM",e.texture.isPMREMTexture=!0,e}_getSourceTarget(t=!1){let e=this._cubeSize,n=this._sourceTarget;return(n===null||n.width!==e||t&&n.depthBuffer===!1)&&(n!==null&&n.dispose(),this._sourceTarget=_d(e,!0,t)),this._sourceTarget}_compileMaterial(t){this._boxMesh.material=t,this._renderer.compile(this._boxMesh,this._cubeCamera.children[0])}_renderCube(t,e,n){let s=this._boxMesh,r=this._cubeCamera;s.material=n,r.renderTarget=t,r.activeMipmapLevel=e;let a=t.width>>e;t.viewport.set(0,0,a,a),r.update(this._renderer,s),t.viewport.set(0,0,t.width,t.height)}_textureToCubemap(t){let e;t.mapping===Ls||t.mapping===xr?(this._cubemapMaterial===null&&(this._cubemapMaterial=yd()),e=this._cubemapMaterial,e.uniforms.flipEnvMap.value=t.isRenderTargetTexture===!1?-1:1):(this._equirectMaterial===null&&(this._equirectMaterial=xd()),e=this._equirectMaterial),e.uniforms.envMap.value=t,this._renderCube(this._getSourceTarget(),0,e)}_applyPMREM(t){this._ggxMaterial===null&&(this._ggxMaterial=g0(),this._integrationMaterial=_0());let e=this._cubeSize,n=t.texture.mipmaps.length-1,s=this._ggxMaterial.uniforms;s.envMap.value=this._sourceTarget.texture;let r=this._integrationMaterial.uniforms;r.envMap.value=this._sourceTarget.texture,r.sourceLod.value=Math.log2(e/zd);for(let a=0;a<=n;a++){let o=i.lodToRoughness(a,n);if(a>n-f0)r.roughness.value=o,this._renderCube(t,a,this._integrationMaterial);else{let l=o>0?Math.log2(e)+.5*Math.log2(6/(kd*Math.pow(o,4)))+.5:0;s.roughness.value=o,s.lodBias.value=l,this._renderCube(t,a,this._ggxMaterial)}}}_blur(t,e){this._blurMaterial===null&&(this._blurMaterial=x0());let n=this._blurMaterial,s=n.uniforms,r=this._sourceTarget;s.sigma.value=Math.min(e,Math.PI)/Math.SQRT2,s.envMap.value=r.texture,this._renderCube(t,0,n),s.envMap.value=t.texture,this._renderCube(r,0,n)}};function _d(i,t,e){return new ya(i,{minFilter:qi,generateMipmaps:t,type:xi,colorSpace:Xr,depthBuffer:e})}function va(i,t,e){return new ai({name:i,uniforms:t,vertexShader:_e.cube_vert,fragmentShader:e,side:vn,blending:Ps,depthTest:!1,depthWrite:!1})}function g0(){return va("PMREMGGXConvolution",{envMap:{value:null},roughness:{value:0},lodBias:{value:0}},`

		#define GGX_SAMPLES ${kd}u

		varying vec3 vWorldDirection;

		uniform samplerCube envMap;
		uniform float roughness;
		uniform float lodBias;

		#include <common>

		// Van der Corput radical inverse
		float radicalInverse_VdC( uint bits ) {

			bits = ( bits << 16u ) | ( bits >> 16u );
			bits = ( ( bits & 0x55555555u ) << 1u ) | ( ( bits & 0xAAAAAAAAu ) >> 1u );
			bits = ( ( bits & 0x33333333u ) << 2u ) | ( ( bits & 0xCCCCCCCCu ) >> 2u );
			bits = ( ( bits & 0x0F0F0F0Fu ) << 4u ) | ( ( bits & 0xF0F0F0F0u ) >> 4u );
			bits = ( ( bits & 0x00FF00FFu ) << 8u ) | ( ( bits & 0xFF00FF00u ) >> 8u );
			return float( bits ) * 2.3283064365386963e-10; // / 0x100000000

		}

		// Hammersley sequence
		vec2 hammersley( uint i, uint N ) {

			return vec2( float( i ) / float( N ), radicalInverse_VdC( i ) );

		}

		void main() {

			vec3 N = normalize( vWorldDirection );

			// For very low roughness, just sample the environment directly
			if ( roughness < 0.001 ) {

				gl_FragColor = vec4( textureLod( envMap, N, 0.0 ).rgb, 1.0 );
				return;

			}

			float alpha = roughness * roughness;
			float alpha2 = alpha * alpha;

			// Tangent space basis for VNDF sampling
			vec3 up = abs( N.z ) < 0.999 ? vec3( 0.0, 0.0, 1.0 ) : vec3( 1.0, 0.0, 0.0 );
			vec3 tangent = normalize( cross( up, N ) );
			vec3 bitangent = cross( N, tangent );

			vec3 prefilteredColor = vec3( 0.0 );
			float totalWeight = 0.0;

			for ( uint i = 0u; i < GGX_SAMPLES; i ++ ) {

				vec2 Xi = hammersley( i, GGX_SAMPLES );

				// With V = N, sample the reflected direction directly.
				float invQ = 1.0 / ( 1.0 - Xi.x + alpha2 * Xi.x );
				float NdotL = ( 1.0 - Xi.x - alpha2 * Xi.x ) * invQ;

				if ( NdotL > 0.0 ) {

					float phi = 2.0 * PI * Xi.y;
					float sinTheta = 2.0 * alpha * sqrt( Xi.x * ( 1.0 - Xi.x ) ) * invQ;
					vec3 L = N * NdotL + ( tangent * cos( phi ) + bitangent * sin( phi ) ) * sinTheta;

					// Match the source mip to the sample's solid angle. The terms
					// independent of the sample are precomputed in lodBias.
					float d = alpha2 * invQ;
					float lod = max( log2( d ) + lodBias, 0.0 );

					// Weight by NdotL for the split-sum approximation
					prefilteredColor += textureLod( envMap, L, lod ).rgb * NdotL;
					totalWeight += NdotL;

				}

			}

			gl_FragColor = vec4( prefilteredColor / totalWeight, 1.0 );

		}
	`)}function _0(){return va("PMREMGGXIntegration",{envMap:{value:null},roughness:{value:0},sourceLod:{value:0},sourceSize:{value:zd}},`

		varying vec3 vWorldDirection;

		uniform samplerCube envMap;
		uniform float roughness;
		uniform float sourceLod;
		uniform int sourceSize;

		void main() {

			vec3 N = normalize( vWorldDirection );

			float alpha = roughness * roughness;
			float alpha2 = alpha * alpha;

			float texelSize = 2.0 / float( sourceSize );

			vec3 prefilteredColor = vec3( 0.0 );
			float totalWeight = 0.0;

			// Pair opposite texels: only the one in N's hemisphere contributes.
			for ( int face = 0; face < 3; face ++ ) {

				for ( int y = 0; y < sourceSize; y ++ ) {

					for ( int x = 0; x < sourceSize; x ++ ) {

						vec2 uv = ( vec2( x, y ) + 0.5 ) * texelSize - 1.0;
						vec3 texelDirection = face == 0 ? vec3( 1.0, uv ) : ( face == 1 ? vec3( uv.x, 1.0, uv.y ) : vec3( uv, 1.0 ) );

						float invDistance = inversesqrt( 1.0 + dot( uv, uv ) );
						float NdotL = dot( N, texelDirection );
						texelDirection *= NdotL < 0.0 ? - 1.0 : 1.0;
						NdotL = abs( NdotL ) * invDistance;

						// With V = N, NdotH squared is ( 1 + NdotL ) / 2. Common factors
						// in the GGX distribution and texel solid angle cancel when normalized.
						float d = 1.0 + alpha2 + ( alpha2 - 1.0 ) * NdotL;
						float weight = NdotL * invDistance * invDistance * invDistance / ( d * d );

						prefilteredColor += textureLod( envMap, texelDirection, sourceLod ).rgb * weight;
						totalWeight += weight;

					}

				}

			}

			gl_FragColor = vec4( prefilteredColor / totalWeight, 1.0 );

		}
	`)}function x0(){return va("PMREMSphericalGaussianBlur",{envMap:{value:null},sigma:{value:0}},`

		#define SAMPLES ${d0}
		#define GOLDEN_ANGLE 2.39996322973

		varying vec3 vWorldDirection;

		uniform samplerCube envMap;
		uniform float sigma;

		#include <common>

		void main() {

			vec3 outputDirection = normalize( vWorldDirection );

			vec3 up = abs( outputDirection.z ) < 0.999 ? vec3( 0.0, 0.0, 1.0 ) : vec3( 1.0, 0.0, 0.0 );
			vec3 tangent = normalize( cross( up, outputDirection ) );
			vec3 bitangent = cross( outputDirection, tangent );

			// Truncate the kernel at three standard deviations or at the antipode.
			float thetaMax = min( 3.0 * sigma, PI );
			float truncation = 1.0 - exp( - 0.5 * thetaMax * thetaMax / ( sigma * sigma ) );

			vec3 accumColor = vec3( 0.0 );
			float accumWeight = 0.0;

			for ( int i = 0; i < SAMPLES; i ++ ) {

				// Stratified inverse-CDF sampling of the Gaussian, placed on a golden-angle spiral.
				float stratum = ( float( i ) + 0.5 ) / float( SAMPLES );
				float theta = sigma * sqrt( - 2.0 * log( 1.0 - stratum * truncation ) );
				float phi = float( i ) * GOLDEN_ANGLE;

				vec3 offset = cos( phi ) * tangent + sin( phi ) * bitangent;
				vec3 sampleDirection = cos( theta ) * outputDirection + sin( theta ) * offset;

				// Correct the planar sample density to solid angle.
				float weight = sin( theta ) / theta;

				accumColor += weight * textureLod( envMap, sampleDirection, 0.0 ).rgb;
				accumWeight += weight;

			}

			gl_FragColor = vec4( accumColor / accumWeight, 1.0 );

		}
	`)}function xd(){return va("PMREMEquirectangularToCubemap",{envMap:{value:null}},`

		varying vec3 vWorldDirection;

		uniform sampler2D envMap;

		#include <common>

		void main() {

			// Average four subpixel samples to preserve small, bright features.
			vec3 direction = normalize( vWorldDirection );
			vec3 dx = dFdx( direction ) * 0.25;
			vec3 dy = dFdy( direction ) * 0.25;

			vec3 color = textureLod( envMap, equirectUv( normalize( direction - dx - dy ) ), 0.0 ).rgb;
			color += textureLod( envMap, equirectUv( normalize( direction + dx - dy ) ), 0.0 ).rgb;
			color += textureLod( envMap, equirectUv( normalize( direction - dx + dy ) ), 0.0 ).rgb;
			color += textureLod( envMap, equirectUv( normalize( direction + dx + dy ) ), 0.0 ).rgb;
			gl_FragColor = vec4( color * 0.25, 1.0 );

		}
	`)}function yd(){return va("PMREMCubemapToCubemap",{envMap:{value:null},flipEnvMap:{value:-1}},`

		varying vec3 vWorldDirection;

		uniform samplerCube envMap;
		uniform float flipEnvMap;

		void main() {

			gl_FragColor = vec4( textureCube( envMap, vec3( flipEnvMap * vWorldDirection.x, vWorldDirection.yz ) ).rgb, 1.0 );

		}
	`)}function y0(i){let t=new WeakMap,e=new WeakMap,n=null;function s(d,p=!1){return d==null?null:p?a(d):r(d)}function r(d){if(d&&d.isTexture){let p=d.mapping;if(p===Yo||p===Zo)if(t.has(d)){let x=t.get(d).texture;return o(x,d.mapping)}else{let x=d.image;if(x&&x.height>0){let S=new ya(x.height);return S.fromEquirectangularTexture(i,d),t.set(d,S),d.addEventListener("dispose",c),o(S.texture,d.mapping)}else return null}}return d}function a(d){if(d&&d.isTexture&&d.isPMREMTexture!==!0){let p=d.mapping,x=p===Yo||p===Zo,S=p===Ls||p===xr;if(x||S){let m=e.get(d),g=m!==void 0?m.texture.pmremVersion:0;if(d.isRenderTargetTexture&&d.pmremVersion!==g)return n===null&&(n=new Sr(i)),m=x?n.fromEquirectangular(d,m):n.fromCubemap(d,m),m.texture.pmremVersion=d.pmremVersion,e.set(d,m),m.texture;if(m!==void 0)return m.texture;{let E=d.image;return x&&E&&E.height>0||S&&E&&l(E)?(n===null&&(n=new Sr(i)),m=x?n.fromEquirectangular(d):n.fromCubemap(d),m.texture.pmremVersion=d.pmremVersion,e.set(d,m),d.addEventListener("dispose",h),m.texture):null}}}return d}function o(d,p){return p===Yo?d.mapping=Ls:p===Zo&&(d.mapping=xr),d}function l(d){let p=0,x=6;for(let S=0;S<x;S++)d[S]!==void 0&&p++;return p===x}function c(d){let p=d.target;p.removeEventListener("dispose",c);let x=t.get(p);x!==void 0&&(t.delete(p),x.dispose())}function h(d){let p=d.target;p.removeEventListener("dispose",h);let x=e.get(p);x!==void 0&&(e.delete(p),x.dispose())}function f(){t=new WeakMap,e=new WeakMap,n!==null&&(n.dispose(),n=null)}return{get:s,dispose:f}}function v0(i){let t={};function e(n){if(t[n]!==void 0)return t[n];let s=i.getExtension(n);return t[n]=s,s}return{has:function(n){return e(n)!==null},init:function(){e("EXT_color_buffer_float"),e("WEBGL_clip_cull_distance"),e("OES_texture_float_linear"),e("EXT_color_buffer_half_float"),e("WEBGL_multisampled_render_to_texture"),e("WEBGL_render_shared_exponent")},get:function(n){let s=e(n);return s===null&&kr("WebGLRenderer: "+n+" extension not supported."),s}}}function M0(i,t,e,n){let s={},r=new WeakMap,a=new FinalizationRegistry(x=>delete s[x]);function o(x){l(x.target)}function l(x){x.index!==null&&t.remove(x.index);for(let m in x.attributes)t.remove(x.attributes[m]);x.removeEventListener("dispose",o),delete s[x.id],a.unregister(x);let S=r.get(x);S&&(t.remove(S),r.delete(x)),n.releaseStatesOfGeometry(x),x.isInstancedBufferGeometry===!0&&delete x._maxInstanceCount,e.memory.geometries--}function c(x,S){return s[S.id]!==void 0||(S.addEventListener("dispose",o),s[S.id]=new WeakRef(S),a.register(S,S.id,S),e.memory.geometries++),S}function h(x){let S=x.attributes;for(let m in S)t.update(S[m],i.ARRAY_BUFFER)}function f(x){let S=x.index,m=x.attributes.position,g=0;if(m===void 0)return;let E=S!==null?S.array.length:m.array.length/3-1,P=m.count>=65535?Kr:Jr,T=new P(Math.ceil(E/3)*6,1),C=T.array;if(S!==null){let _=S.array;g=S.version;for(let b=0,G=0;b<E;b+=3){let B=_[b+0],k=_[b+1],H=_[b+2];C[G++]=B,C[G++]=k,C[G++]=k,C[G++]=H,C[G++]=H,C[G++]=B}}else{g=m.version;for(let _=0,b=0;_<E;_+=3){let G=_+0,B=_+1,k=_+2;C[b++]=G,C[b++]=B,C[b++]=B,C[b++]=k,C[b++]=k,C[b++]=G}}T.version=g;let A=r.get(x);A&&t.remove(A),r.set(x,T)}function d(x){let S=r.get(x);if(S){let m=x.index;m!==null&&S.version<m.version&&f(x)}else f(x);return r.get(x)}function p(){for(let x in s){let S=s[x].deref();S!==void 0&&l(S)}}return{get:c,update:h,getWireframeAttribute:d,dispose:p}}function S0(i,t,e){let n;function s(f){n=f}let r,a;function o(f){r=f.type,a=f.bytesPerElement}function l(f,d){i.drawElements(n,d,r,f*a),e.update(d,n,1)}function c(f,d,p){p!==0&&(i.drawElementsInstanced(n,d,r,f*a,p),e.update(d,n,p))}function h(f,d,p){if(p===0)return;t.get("WEBGL_multi_draw").multiDrawElementsWEBGL(n,d,0,r,f,0,p);let S=0;for(let m=0;m<p;m++)S+=d[m];e.update(S,n,1)}this.setMode=s,this.setIndex=o,this.render=l,this.renderInstances=c,this.renderMultiDraw=h}function b0(i){let t={geometries:0,textures:0},e={frame:0,calls:0,triangles:0,points:0,lines:0};function n(r,a,o){switch(e.calls++,a){case i.TRIANGLES:e.triangles+=o*(r/3);break;case i.LINES:e.lines+=o*(r/2);break;case i.LINE_STRIP:e.lines+=o*(r-1);break;case i.LINE_LOOP:e.lines+=o*r;break;case i.POINTS:e.points+=o*r;break;default:ie("WebGLInfo: Unknown draw mode:",a);break}}function s(){e.calls=0,e.triangles=0,e.points=0,e.lines=0}return{memory:t,render:e,programs:null,autoReset:!0,reset:s,update:n}}function E0(i,t,e){let n=new WeakMap,s=new je;function r(a,o,l){let c=a.morphTargetInfluences,h=o.morphAttributes.position||o.morphAttributes.normal||o.morphAttributes.color,f=h!==void 0?h.length:0,d=n.get(o);if(d===void 0||d.count!==f){let G=function(){_.dispose(),n.delete(o),o.removeEventListener("dispose",G)};d!==void 0&&d.texture.dispose();let p=o.morphAttributes.position!==void 0,x=o.morphAttributes.normal!==void 0,S=o.morphAttributes.color!==void 0,m=o.morphAttributes.position||[],g=o.morphAttributes.normal||[],E=o.morphAttributes.color||[],P=0;p===!0&&(P=1),x===!0&&(P=2),S===!0&&(P=3);let T=o.attributes.position.count*P,C=1;T>t.maxTextureSize&&(C=Math.ceil(T/t.maxTextureSize),T=t.maxTextureSize);let A=new Float32Array(T*C*4*f),_=new Zr(A,T,C,f);_.type=_i,_.needsUpdate=!0;let b=P*4;for(let B=0;B<f;B++){let k=m[B],H=g[B],K=E[B],U=T*C*4*B;for(let Y=0;Y<k.count;Y++){let tt=Y*b;p===!0&&(s.fromBufferAttribute(k,Y),A[U+tt+0]=s.x,A[U+tt+1]=s.y,A[U+tt+2]=s.z,A[U+tt+3]=0),x===!0&&(s.fromBufferAttribute(H,Y),A[U+tt+4]=s.x,A[U+tt+5]=s.y,A[U+tt+6]=s.z,A[U+tt+7]=0),S===!0&&(s.fromBufferAttribute(K,Y),A[U+tt+8]=s.x,A[U+tt+9]=s.y,A[U+tt+10]=s.z,A[U+tt+11]=K.itemSize===4?s.w:1)}}d={count:f,texture:_,size:new kt(T,C)},n.set(o,d),o.addEventListener("dispose",G)}if(a.isInstancedMesh===!0&&a.morphTexture!==null)l.getUniforms().setValue(i,"morphTexture",a.morphTexture,e);else{let p=0;for(let S=0;S<c.length;S++)p+=c[S];let x=o.morphTargetsRelative?1:1-p;l.getUniforms().setValue(i,"morphTargetBaseInfluence",x),l.getUniforms().setValue(i,"morphTargetInfluences",c)}l.getUniforms().setValue(i,"morphTargetsTexture",d.texture,e),l.getUniforms().setValue(i,"morphTargetsTextureSize",d.size)}return{update:r}}function T0(i,t,e,n,s){let r=new WeakMap;function a(c){let h=s.render.frame,f=c.geometry,d=t.get(c,f);if(r.get(d)!==h&&(t.update(d),r.set(d,h)),c.isInstancedMesh&&(c.hasEventListener("dispose",l)===!1&&c.addEventListener("dispose",l),r.get(c)!==h&&(e.update(c.instanceMatrix,i.ARRAY_BUFFER),c.instanceColor!==null&&e.update(c.instanceColor,i.ARRAY_BUFFER),r.set(c,h))),c.isSkinnedMesh){let p=c.skeleton;r.get(p)!==h&&(p.update(),r.set(p,h))}return d}function o(){r=new WeakMap}function l(c){let h=c.target;h.removeEventListener("dispose",l),n.releaseStatesOfObject(h),e.remove(h.instanceMatrix),h.instanceColor!==null&&e.remove(h.instanceColor)}return{update:a,dispose:o}}var w0={[Gc]:"LINEAR_TONE_MAPPING",[Vc]:"REINHARD_TONE_MAPPING",[Wc]:"CINEON_TONE_MAPPING",[ca]:"ACES_FILMIC_TONE_MAPPING",[qc]:"AGX_TONE_MAPPING",[Yc]:"NEUTRAL_TONE_MAPPING",[Xc]:"CUSTOM_TONE_MAPPING"};function A0(i,t,e,n,s,r){let a=new Zn(t,e,{type:i,depthBuffer:s,stencilBuffer:r,samples:n?4:0,storeMultisampledDepthBuffer:!1,storeMultisampledStencilBuffer:!1,resolveDepthBuffer:!1,resolveStencilBuffer:!1}),o=null,l=null,c=null,h=new Sn;h.setAttribute("position",new Be([-1,3,0,-1,-1,0,3,-1,0],3)),h.setAttribute("uv",new Be([0,2,0,0,2,0],2));let f=new Po({uniforms:{tDiffuse:{value:null}},vertexShader:`
			precision highp float;

			uniform mat4 modelViewMatrix;
			uniform mat4 projectionMatrix;

			attribute vec3 position;
			attribute vec2 uv;

			varying vec2 vUv;

			void main() {
				vUv = uv;
				gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
			}`,fragmentShader:`
			precision highp float;

			uniform sampler2D tDiffuse;

			varying vec2 vUv;

			#include <tonemapping_pars_fragment>
			#include <colorspace_pars_fragment>

			void main() {
				gl_FragColor = texture2D( tDiffuse, vUv );

				#ifdef LINEAR_TONE_MAPPING
					gl_FragColor.rgb = LinearToneMapping( gl_FragColor.rgb );
				#elif defined( REINHARD_TONE_MAPPING )
					gl_FragColor.rgb = ReinhardToneMapping( gl_FragColor.rgb );
				#elif defined( CINEON_TONE_MAPPING )
					gl_FragColor.rgb = CineonToneMapping( gl_FragColor.rgb );
				#elif defined( ACES_FILMIC_TONE_MAPPING )
					gl_FragColor.rgb = ACESFilmicToneMapping( gl_FragColor.rgb );
				#elif defined( AGX_TONE_MAPPING )
					gl_FragColor.rgb = AgXToneMapping( gl_FragColor.rgb );
				#elif defined( NEUTRAL_TONE_MAPPING )
					gl_FragColor.rgb = NeutralToneMapping( gl_FragColor.rgb );
				#elif defined( CUSTOM_TONE_MAPPING )
					gl_FragColor.rgb = CustomToneMapping( gl_FragColor.rgb );
				#endif

				#ifdef SRGB_TRANSFER
					gl_FragColor = sRGBTransferOETF( gl_FragColor );
				#endif
			}`,depthTest:!1,depthWrite:!1}),d=new Qt(h,f),p=new aa(-1,1,1,-1,0,1),x=null,S=null,m=!1,g,E=null,P=[],T=!1;this.setSize=function(C,A){a.setSize(C,A),o!==null&&o.setSize(C,A),l!==null&&l.setSize(C,A);for(let _=0;_<P.length;_++){let b=P[_];b.setSize&&b.setSize(C,A)}},this.setEffects=function(C){P=C,T=P.length>0&&P[0].isRenderPass===!0;let A=a.width,_=a.height;P.length>0&&o===null&&(o=new Zn(A,_,{type:xi,depthBuffer:!1,stencilBuffer:!1}),l=new Zn(A,_,{type:xi,depthBuffer:!1,stencilBuffer:!1}));let b=s===!0&&P.some(G=>G.needsDepthTexture===!0);b!==(a.depthTexture!==null)&&(b===!0&&c===null&&(c=new Vi(A,_),r===!0&&(c.format=Yi,c.type=Ns)),a.dispose(),a.depthTexture=b?c:null,a.resolveDepthBuffer=b,a.storeMultisampledDepthBuffer=b);for(let G=0;G<P.length;G++){let B=P[G];B.setSize&&B.setSize(A,_),b&&B.needsDepthTexture===!0&&B.setDepthTexture&&B.setDepthTexture(c)}},this.begin=function(C,A){if(m||C.toneMapping===Ci&&P.length===0)return!1;if(E=A,A!==null){let _=A.width,b=A.height;(a.width!==_||a.height!==b)&&this.setSize(_,b)}return T===!1&&C.setRenderTarget(a),g=C.toneMapping,C.toneMapping=Ci,!0},this.hasRenderPass=function(){return T},this.end=function(C,A){C.toneMapping=g,m=!0;let _=a,b=o;for(let G=0;G<P.length;G++){let B=P[G];B.enabled!==!1&&(B.render(C,b,_,A),B.needsSwap!==!1&&(_=b,b=b===o?l:o))}if(x!==C.outputColorSpace||S!==C.toneMapping){x=C.outputColorSpace,S=C.toneMapping,f.defines={},be.getTransfer(x)===De&&(f.defines.SRGB_TRANSFER="");let G=w0[S];G&&(f.defines[G]=""),f.needsUpdate=!0}f.uniforms.tDiffuse.value=_.texture,C.setRenderTarget(E),C.render(d,p),E=null,m=!1},this.isCompositing=function(){return m},this.dispose=function(){a.dispose(),o!==null&&o.dispose(),l!==null&&l.dispose(),h.dispose(),f.dispose()}}var Hd=new Dn,Gd=new Vi(1,1),Vd=new Qr(1),Wd=new Zr,Xd=new xo,qd=new jr,vd=[],Md=[],Sd=new Float32Array(16),bd=new Float32Array(9),Ed=new Float32Array(4);function br(i,t,e){let n=i[0];if(n<=0||n>0)return i;let s=t*e,r=vd[s];if(r===void 0&&(r=new Float32Array(s),vd[s]=r),t!==0){n.toArray(r,0);for(let a=1,o=0;a!==t;++a)o+=e,i[a].toArray(r,o)}return r}function pn(i,t){if(i.length!==t.length)return!1;for(let e=0,n=i.length;e<n;e++)if(i[e]!==t[e])return!1;return!0}function mn(i,t){for(let e=0,n=t.length;e<n;e++)i[e]=t[e]}function Fl(i,t){let e=Md[t];e===void 0&&(e=new Int32Array(t),Md[t]=e);for(let n=0;n!==t;++n)e[n]=i.allocateTextureUnit();return e}function R0(i,t){let e=this.cache;e[0]!==t&&(i.uniform1f(this.addr,t),e[0]=t)}function C0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(i.uniform2f(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(pn(e,t))return;i.uniform2fv(this.addr,t),mn(e,t)}}function P0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(i.uniform3f(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else if(t.r!==void 0)(e[0]!==t.r||e[1]!==t.g||e[2]!==t.b)&&(i.uniform3f(this.addr,t.r,t.g,t.b),e[0]=t.r,e[1]=t.g,e[2]=t.b);else{if(pn(e,t))return;i.uniform3fv(this.addr,t),mn(e,t)}}function I0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(i.uniform4f(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(pn(e,t))return;i.uniform4fv(this.addr,t),mn(e,t)}}function L0(i,t){let e=this.cache,n=t.elements;if(n===void 0){if(pn(e,t))return;i.uniformMatrix2fv(this.addr,!1,t),mn(e,t)}else{if(pn(e,n))return;Ed.set(n),i.uniformMatrix2fv(this.addr,!1,Ed),mn(e,n)}}function N0(i,t){let e=this.cache,n=t.elements;if(n===void 0){if(pn(e,t))return;i.uniformMatrix3fv(this.addr,!1,t),mn(e,t)}else{if(pn(e,n))return;bd.set(n),i.uniformMatrix3fv(this.addr,!1,bd),mn(e,n)}}function D0(i,t){let e=this.cache,n=t.elements;if(n===void 0){if(pn(e,t))return;i.uniformMatrix4fv(this.addr,!1,t),mn(e,t)}else{if(pn(e,n))return;Sd.set(n),i.uniformMatrix4fv(this.addr,!1,Sd),mn(e,n)}}function U0(i,t){let e=this.cache;e[0]!==t&&(i.uniform1i(this.addr,t),e[0]=t)}function F0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(i.uniform2i(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(pn(e,t))return;i.uniform2iv(this.addr,t),mn(e,t)}}function O0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(i.uniform3i(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else{if(pn(e,t))return;i.uniform3iv(this.addr,t),mn(e,t)}}function B0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(i.uniform4i(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(pn(e,t))return;i.uniform4iv(this.addr,t),mn(e,t)}}function k0(i,t){let e=this.cache;e[0]!==t&&(i.uniform1ui(this.addr,t),e[0]=t)}function z0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(i.uniform2ui(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(pn(e,t))return;i.uniform2uiv(this.addr,t),mn(e,t)}}function H0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(i.uniform3ui(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else{if(pn(e,t))return;i.uniform3uiv(this.addr,t),mn(e,t)}}function G0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(i.uniform4ui(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(pn(e,t))return;i.uniform4uiv(this.addr,t),mn(e,t)}}function Ol(i){return i.version===0&&(i.compareFunction=sh,i.needsUpdate=!0),i}function V0(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s);let r;this.type===i.SAMPLER_2D_SHADOW?r=Ol(Gd):r=Hd,e.setTexture2D(t||r,s)}function W0(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s),e.setTexture3D(t||Xd,s)}function X0(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s);let r;this.type===i.SAMPLER_CUBE_SHADOW?r=Ol(Vd):r=qd,e.setTextureCube(t||r,s)}function q0(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s),e.setTexture2DArray(t||Wd,s)}function Y0(i){switch(i){case 5126:return R0;case 35664:return C0;case 35665:return P0;case 35666:return I0;case 35674:return L0;case 35675:return N0;case 35676:return D0;case 5124:case 35670:return U0;case 35667:case 35671:return F0;case 35668:case 35672:return O0;case 35669:case 35673:return B0;case 5125:return k0;case 36294:return z0;case 36295:return H0;case 36296:return G0;case 35678:case 36198:case 36298:case 36306:case 35682:return V0;case 35679:case 36299:case 36307:return W0;case 35680:case 36300:case 36308:case 36293:return X0;case 36289:case 36303:case 36311:case 36292:return q0}}function Z0(i,t){i.uniform1fv(this.addr,t)}function J0(i,t){let e=br(t,this.size,2);i.uniform2fv(this.addr,e)}function K0(i,t){let e=br(t,this.size,3);i.uniform3fv(this.addr,e)}function $0(i,t){let e=br(t,this.size,4);i.uniform4fv(this.addr,e)}function j0(i,t){let e=br(t,this.size,4);i.uniformMatrix2fv(this.addr,!1,e)}function Q0(i,t){let e=br(t,this.size,9);i.uniformMatrix3fv(this.addr,!1,e)}function t_(i,t){let e=br(t,this.size,16);i.uniformMatrix4fv(this.addr,!1,e)}function e_(i,t){i.uniform1iv(this.addr,t)}function n_(i,t){i.uniform2iv(this.addr,t)}function i_(i,t){i.uniform3iv(this.addr,t)}function s_(i,t){i.uniform4iv(this.addr,t)}function r_(i,t){i.uniform1uiv(this.addr,t)}function a_(i,t){i.uniform2uiv(this.addr,t)}function o_(i,t){i.uniform3uiv(this.addr,t)}function l_(i,t){i.uniform4uiv(this.addr,t)}function c_(i,t,e){let n=this.cache,s=t.length,r=Fl(e,s);pn(n,r)||(i.uniform1iv(this.addr,r),mn(n,r));let a;this.type===i.SAMPLER_2D_SHADOW?a=Ol(Gd):a=Hd;for(let o=0;o!==s;++o)e.setTexture2D(t[o]||a,r[o])}function h_(i,t,e){let n=this.cache,s=t.length,r=Fl(e,s);pn(n,r)||(i.uniform1iv(this.addr,r),mn(n,r));for(let a=0;a!==s;++a)e.setTexture3D(t[a]||Xd,r[a])}function u_(i,t,e){let n=this.cache,s=t.length,r=Fl(e,s);pn(n,r)||(i.uniform1iv(this.addr,r),mn(n,r));let a;this.type===i.SAMPLER_CUBE_SHADOW?a=Ol(Vd):a=qd;for(let o=0;o!==s;++o)e.setTextureCube(t[o]||a,r[o])}function d_(i,t,e){let n=this.cache,s=t.length,r=Fl(e,s);pn(n,r)||(i.uniform1iv(this.addr,r),mn(n,r));for(let a=0;a!==s;++a)e.setTexture2DArray(t[a]||Wd,r[a])}function f_(i){switch(i){case 5126:return Z0;case 35664:return J0;case 35665:return K0;case 35666:return $0;case 35674:return j0;case 35675:return Q0;case 35676:return t_;case 5124:case 35670:return e_;case 35667:case 35671:return n_;case 35668:case 35672:return i_;case 35669:case 35673:return s_;case 5125:return r_;case 36294:return a_;case 36295:return o_;case 36296:return l_;case 35678:case 36198:case 36298:case 36306:case 35682:return c_;case 35679:case 36299:case 36307:return h_;case 35680:case 36300:case 36308:case 36293:return u_;case 36289:case 36303:case 36311:case 36292:return d_}}var xh=class{constructor(t,e,n){this.id=t,this.addr=n,this.cache=[],this.type=e.type,this.setValue=Y0(e.type)}},yh=class{constructor(t,e,n){this.id=t,this.addr=n,this.cache=[],this.type=e.type,this.size=e.size,this.setValue=f_(e.type)}},vh=class{constructor(t){this.id=t,this.seq=[],this.map={}}setValue(t,e,n){let s=this.seq;for(let r=0,a=s.length;r!==a;++r){let o=s[r];o.setValue(t,e[o.id],n)}}},gh=/(\w+)(\])?(\[|\.)?/g;function Td(i,t){i.seq.push(t),i.map[t.id]=t}function p_(i,t,e){let n=i.name,s=n.length;for(gh.lastIndex=0;;){let r=gh.exec(n),a=gh.lastIndex,o=r[1],l=r[2]==="]",c=r[3];if(l&&(o=o|0),c===void 0||c==="["&&a+2===s){Td(e,c===void 0?new xh(o,i,t):new yh(o,i,t));break}else{let f=e.map[o];f===void 0&&(f=new vh(o),Td(e,f)),e=f}}}var Mr=class{constructor(t,e){this.seq=[],this.map={};let n=t.getProgramParameter(e,t.ACTIVE_UNIFORMS);for(let a=0;a<n;++a){let o=t.getActiveUniform(e,a),l=t.getUniformLocation(e,o.name);p_(o,l,this)}let s=[],r=[];for(let a of this.seq)a.type===t.SAMPLER_2D_SHADOW||a.type===t.SAMPLER_CUBE_SHADOW||a.type===t.SAMPLER_2D_ARRAY_SHADOW?s.push(a):r.push(a);s.length>0&&(this.seq=s.concat(r))}setValue(t,e,n,s){let r=this.map[e];r!==void 0&&r.setValue(t,n,s)}setOptional(t,e,n){let s=e[n];s!==void 0&&this.setValue(t,n,s)}static upload(t,e,n,s){for(let r=0,a=e.length;r!==a;++r){let o=e[r],l=n[o.id];l.needsUpdate!==!1&&o.setValue(t,l.value,s)}}static seqWithValue(t,e){let n=[];for(let s=0,r=t.length;s!==r;++s){let a=t[s];a.id in e&&n.push(a)}return n}};function wd(i,t,e){let n=i.createShader(t);return i.shaderSource(n,e),i.compileShader(n),n}var m_=37297,g_=0;function __(i,t){let e=i.split(`
`),n=[],s=Math.max(t-6,0),r=Math.min(t+6,e.length);for(let a=s;a<r;a++){let o=a+1;n.push(`${o===t?">":" "} ${o}: ${e[a]}`)}return n.join(`
`)}var Ad=new ae;function x_(i){be._getMatrix(Ad,be.workingColorSpace,i);let t=`mat3( ${Ad.elements.map(e=>e.toFixed(4))} )`;switch(be.getTransfer(i)){case qr:return[t,"LinearTransferOETF"];case De:return[t,"sRGBTransferOETF"];default:return Kt("WebGLProgram: Unsupported color space: ",i),[t,"LinearTransferOETF"]}}function Rd(i,t,e){let n=i.getShaderParameter(t,i.COMPILE_STATUS),r=(i.getShaderInfoLog(t)||"").trim();if(n&&r==="")return"";let a=/ERROR: 0:(\d+)/.exec(r);if(a){let o=parseInt(a[1]);return e.toUpperCase()+`

`+r+`

`+__(i.getShaderSource(t),o)}else return r}function y_(i,t){let e=x_(t);return[`vec4 ${i}( vec4 value ) {`,`	return ${e[1]}( vec4( ${e[0]} * value.rgb, value.a ) );`,"}"].join(`
`)}var v_={[Gc]:"Linear",[Vc]:"Reinhard",[Wc]:"Cineon",[ca]:"ACESFilmic",[qc]:"AgX",[Yc]:"Neutral",[Xc]:"Custom"};function M_(i,t){let e=v_[t];return e===void 0?(Kt("WebGLProgram: Unsupported toneMapping:",t),"vec3 "+i+"( vec3 color ) { return LinearToneMapping( color ); }"):"vec3 "+i+"( vec3 color ) { return "+e+"ToneMapping( color ); }"}var Dl=new D;function S_(){be.getLuminanceCoefficients(Dl);let i=Dl.x.toFixed(4),t=Dl.y.toFixed(4),e=Dl.z.toFixed(4);return["float luminance( const in vec3 rgb ) {",`	const vec3 weights = vec3( ${i}, ${t}, ${e} );`,"	return dot( weights, rgb );","}"].join(`
`)}function b_(i){return[i.extensionClipCullDistance?"#extension GL_ANGLE_clip_cull_distance : require":"",i.extensionMultiDraw?"#extension GL_ANGLE_multi_draw : require":""].filter(xa).join(`
`)}function E_(i){let t=[];for(let e in i){let n=i[e];n!==!1&&t.push("#define "+e+" "+n)}return t.join(`
`)}function T_(i,t){let e={},n=i.getProgramParameter(t,i.ACTIVE_ATTRIBUTES);for(let s=0;s<n;s++){let r=i.getActiveAttrib(t,s),a=r.name,o=1;r.type===i.FLOAT_MAT2&&(o=2),r.type===i.FLOAT_MAT3&&(o=3),r.type===i.FLOAT_MAT4&&(o=4),e[a]={type:r.type,location:i.getAttribLocation(t,a),locationSize:o}}return e}function xa(i){return i!==""}function Cd(i,t){let e=t.numSpotLightShadows+t.numSpotLightMaps-t.numSpotLightShadowsWithMaps;return i.replace(/NUM_SUN_LIGHTS/g,t.numSunLights).replace(/NUM_DIR_LIGHTS/g,t.numDirLights).replace(/NUM_SPOT_LIGHTS/g,t.numSpotLights).replace(/NUM_SPOT_LIGHT_MAPS/g,t.numSpotLightMaps).replace(/NUM_SPOT_LIGHT_COORDS/g,e).replace(/NUM_RECT_AREA_LIGHTS/g,t.numRectAreaLights).replace(/NUM_POINT_LIGHTS/g,t.numPointLights).replace(/NUM_HEMI_LIGHTS/g,t.numHemiLights).replace(/NUM_SUN_LIGHT_SHADOWS/g,t.numSunLightShadows).replace(/NUM_DIR_LIGHT_SHADOWS/g,t.numDirLightShadows).replace(/NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS/g,t.numSpotLightShadowsWithMaps).replace(/NUM_SPOT_LIGHT_SHADOWS/g,t.numSpotLightShadows).replace(/NUM_POINT_LIGHT_SHADOWS/g,t.numPointLightShadows).replace(/NUM_LIGHT_PROBE_GRIDS/g,t.numLightProbeGrids)}function Pd(i,t){return i.replace(/NUM_CLIPPING_PLANES/g,t.numClippingPlanes).replace(/UNION_CLIPPING_PLANES/g,t.numClippingPlanes-t.numClipIntersection)}var w_=/^[ \t]*#include +<([\w\d./]+)>/gm;function Mh(i){return i.replace(w_,A_)}function A_(i,t){let e=_e[t];if(e===void 0)throw new Error("THREE.WebGLProgram: Can not resolve #include <"+t+">");return Mh(e)}var R_=/#pragma unroll_loop_start\s+for\s*\(\s*int\s+i\s*=\s*(\d+)\s*;\s*i\s*<\s*(\d+)\s*;\s*i\s*\+\+\s*\)\s*{([\s\S]+?)}\s+#pragma unroll_loop_end/g;function Id(i){return i.replace(R_,C_)}function C_(i,t,e,n){let s="";for(let r=parseInt(t);r<parseInt(e);r++)s+=n.replace(/\[\s*i\s*\]/g,"[ "+r+" ]").replace(/UNROLLED_LOOP_INDEX/g,r);return s}function Ld(i){let t=`precision ${i.precision} float;
	precision ${i.precision} int;
	precision ${i.precision} sampler2D;
	precision ${i.precision} samplerCube;
	precision ${i.precision} sampler3D;
	precision ${i.precision} sampler2DArray;
	precision ${i.precision} sampler2DShadow;
	precision ${i.precision} samplerCubeShadow;
	precision ${i.precision} sampler2DArrayShadow;
	precision ${i.precision} isampler2D;
	precision ${i.precision} isampler3D;
	precision ${i.precision} isamplerCube;
	precision ${i.precision} isampler2DArray;
	precision ${i.precision} usampler2D;
	precision ${i.precision} usampler3D;
	precision ${i.precision} usamplerCube;
	precision ${i.precision} usampler2DArray;
	`;return i.precision==="highp"?t+=`
#define HIGH_PRECISION`:i.precision==="mediump"?t+=`
#define MEDIUM_PRECISION`:i.precision==="lowp"&&(t+=`
#define LOW_PRECISION`),t}var P_={[Cs]:"SHADOWMAP_TYPE_PCF",[gr]:"SHADOWMAP_TYPE_VSM"};function I_(i){return P_[i.shadowMapType]||"SHADOWMAP_TYPE_BASIC"}var L_={[xr]:"ENVMAP_MODE_REFRACTION"};function N_(i){return i.envMap===!1?"ENVMAP_MODE_REFLECTION":L_[i.envMapMode]||"ENVMAP_MODE_REFLECTION"}var D_={[Hc]:"ENVMAP_BLENDING_MULTIPLY",[Zu]:"ENVMAP_BLENDING_MIX",[Ju]:"ENVMAP_BLENDING_ADD"};function U_(i){return i.envMap===!1?"ENVMAP_BLENDING_NONE":D_[i.combine]||"ENVMAP_BLENDING_NONE"}function F_(i,t,e,n){let s=i.getContext(),r=e.defines,a=e.vertexShader,o=e.fragmentShader,l=I_(e),c=e.envMapPMREM===!0?"ENVMAP_TYPE_PMREM":"ENVMAP_TYPE_CUBE",h=N_(e),f=U_(e),d=b_(e),p=E_(r),x=s.createProgram(),S,m,g=e.glslVersion?"#version "+e.glslVersion+`
`:"";e.isRawShaderMaterial?(S=["#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,p].filter(xa).join(`
`),S.length>0&&(S+=`
`),m=["#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,p].filter(xa).join(`
`),m.length>0&&(m+=`
`)):(S=[Ld(e),"#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,p,e.extensionClipCullDistance?"#define USE_CLIP_DISTANCE":"",e.batching?"#define USE_BATCHING":"",e.batchingColor?"#define USE_BATCHING_COLOR":"",e.instancing?"#define USE_INSTANCING":"",e.instancingColor?"#define USE_INSTANCING_COLOR":"",e.instancingMorph?"#define USE_INSTANCING_MORPH":"",e.useFog&&e.fog?"#define USE_FOG":"",e.useFog&&e.fogExp2?"#define FOG_EXP2":"",e.map?"#define USE_MAP":"",e.envMap?"#define USE_ENVMAP":"",e.envMap?"#define "+h:"",e.lightMap?"#define USE_LIGHTMAP":"",e.aoMap?"#define USE_AOMAP":"",e.bumpMap?"#define USE_BUMPMAP":"",e.normalMap?"#define USE_NORMALMAP":"",e.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",e.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",e.displacementMap?"#define USE_DISPLACEMENTMAP":"",e.emissiveMap?"#define USE_EMISSIVEMAP":"",e.anisotropy?"#define USE_ANISOTROPY":"",e.anisotropyMap?"#define USE_ANISOTROPYMAP":"",e.clearcoatMap?"#define USE_CLEARCOATMAP":"",e.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",e.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",e.diffuseRoughnessMap?"#define USE_DIFFUSE_ROUGHNESSMAP":"",e.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",e.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",e.specularMap?"#define USE_SPECULARMAP":"",e.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",e.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",e.roughnessMap?"#define USE_ROUGHNESSMAP":"",e.metalnessMap?"#define USE_METALNESSMAP":"",e.alphaMap?"#define USE_ALPHAMAP":"",e.alphaHash?"#define USE_ALPHAHASH":"",e.transmission?"#define USE_TRANSMISSION":"",e.transmissionMap?"#define USE_TRANSMISSIONMAP":"",e.thicknessMap?"#define USE_THICKNESSMAP":"",e.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",e.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",e.mapUv?"#define MAP_UV "+e.mapUv:"",e.alphaMapUv?"#define ALPHAMAP_UV "+e.alphaMapUv:"",e.lightMapUv?"#define LIGHTMAP_UV "+e.lightMapUv:"",e.aoMapUv?"#define AOMAP_UV "+e.aoMapUv:"",e.emissiveMapUv?"#define EMISSIVEMAP_UV "+e.emissiveMapUv:"",e.bumpMapUv?"#define BUMPMAP_UV "+e.bumpMapUv:"",e.normalMapUv?"#define NORMALMAP_UV "+e.normalMapUv:"",e.displacementMapUv?"#define DISPLACEMENTMAP_UV "+e.displacementMapUv:"",e.metalnessMapUv?"#define METALNESSMAP_UV "+e.metalnessMapUv:"",e.roughnessMapUv?"#define ROUGHNESSMAP_UV "+e.roughnessMapUv:"",e.anisotropyMapUv?"#define ANISOTROPYMAP_UV "+e.anisotropyMapUv:"",e.clearcoatMapUv?"#define CLEARCOATMAP_UV "+e.clearcoatMapUv:"",e.clearcoatNormalMapUv?"#define CLEARCOAT_NORMALMAP_UV "+e.clearcoatNormalMapUv:"",e.clearcoatRoughnessMapUv?"#define CLEARCOAT_ROUGHNESSMAP_UV "+e.clearcoatRoughnessMapUv:"",e.diffuseRoughnessMapUv?"#define DIFFUSE_ROUGHNESSMAP_UV "+e.diffuseRoughnessMapUv:"",e.iridescenceMapUv?"#define IRIDESCENCEMAP_UV "+e.iridescenceMapUv:"",e.iridescenceThicknessMapUv?"#define IRIDESCENCE_THICKNESSMAP_UV "+e.iridescenceThicknessMapUv:"",e.sheenColorMapUv?"#define SHEEN_COLORMAP_UV "+e.sheenColorMapUv:"",e.sheenRoughnessMapUv?"#define SHEEN_ROUGHNESSMAP_UV "+e.sheenRoughnessMapUv:"",e.specularMapUv?"#define SPECULARMAP_UV "+e.specularMapUv:"",e.specularColorMapUv?"#define SPECULAR_COLORMAP_UV "+e.specularColorMapUv:"",e.specularIntensityMapUv?"#define SPECULAR_INTENSITYMAP_UV "+e.specularIntensityMapUv:"",e.transmissionMapUv?"#define TRANSMISSIONMAP_UV "+e.transmissionMapUv:"",e.thicknessMapUv?"#define THICKNESSMAP_UV "+e.thicknessMapUv:"",e.vertexTangents&&e.flatShading===!1?"#define USE_TANGENT":"",e.vertexNormals?"#define HAS_NORMAL":"",e.vertexColors?"#define USE_COLOR":"",e.vertexAlphas?"#define USE_COLOR_ALPHA":"",e.vertexUv1s?"#define USE_UV1":"",e.vertexUv2s?"#define USE_UV2":"",e.vertexUv3s?"#define USE_UV3":"",e.pointsUvs?"#define USE_POINTS_UV":"",e.flatShading?"#define FLAT_SHADED":"",e.skinning?"#define USE_SKINNING":"",e.morphTargets?"#define USE_MORPHTARGETS":"",e.morphNormals&&e.flatShading===!1?"#define USE_MORPHNORMALS":"",e.morphColors?"#define USE_MORPHCOLORS":"",e.morphTargetsCount>0?"#define MORPHTARGETS_TEXTURE_STRIDE "+e.morphTextureStride:"",e.morphTargetsCount>0?"#define MORPHTARGETS_COUNT "+e.morphTargetsCount:"",e.doubleSided?"#define DOUBLE_SIDED":"",e.flipSided?"#define FLIP_SIDED":"",e.shadowMapEnabled?"#define USE_SHADOWMAP":"",e.shadowMapEnabled?"#define "+l:"",e.sizeAttenuation?"#define USE_SIZEATTENUATION":"",e.numLightProbes>0?"#define USE_LIGHT_PROBES":"",e.logarithmicDepthBuffer?"#define USE_LOGARITHMIC_DEPTH_BUFFER":"",e.reversedDepthBuffer?"#define USE_REVERSED_DEPTH_BUFFER":"","uniform mat4 modelMatrix;","uniform mat4 modelViewMatrix;","uniform mat4 projectionMatrix;","uniform mat4 viewMatrix;","uniform mat3 normalMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;","#ifdef USE_INSTANCING","	attribute mat4 instanceMatrix;","#endif","#ifdef USE_INSTANCING_COLOR","	attribute vec3 instanceColor;","#endif","#ifdef USE_INSTANCING_MORPH","	uniform sampler2D morphTexture;","#endif","attribute vec3 position;","attribute vec3 normal;","attribute vec2 uv;","#ifdef USE_UV1","	attribute vec2 uv1;","#endif","#ifdef USE_UV2","	attribute vec2 uv2;","#endif","#ifdef USE_UV3","	attribute vec2 uv3;","#endif","#ifdef USE_TANGENT","	attribute vec4 tangent;","#endif","#if defined( USE_COLOR_ALPHA )","	attribute vec4 color;","#elif defined( USE_COLOR )","	attribute vec3 color;","#endif","#ifdef USE_SKINNING","	attribute vec4 skinIndex;","	attribute vec4 skinWeight;","#endif",`
`].filter(xa).join(`
`),m=[Ld(e),"#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,p,e.useFog&&e.fog?"#define USE_FOG":"",e.useFog&&e.fogExp2?"#define FOG_EXP2":"",e.alphaToCoverage?"#define ALPHA_TO_COVERAGE":"",e.map?"#define USE_MAP":"",e.matcap?"#define USE_MATCAP":"",e.envMap?"#define USE_ENVMAP":"",e.envMap?"#define "+c:"",e.envMap?"#define "+h:"",e.envMap?"#define "+f:"",e.envMapPMREM?"#define ENVMAP_MAX_LOD "+e.envMapMaxLod+".0":"",e.envMapPMREM?"#define ENVMAP_SIZE "+e.envMapSize+".0":"",e.lightMap?"#define USE_LIGHTMAP":"",e.aoMap?"#define USE_AOMAP":"",e.bumpMap?"#define USE_BUMPMAP":"",e.normalMap?"#define USE_NORMALMAP":"",e.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",e.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",e.packedNormalMap?"#define USE_PACKED_NORMALMAP":"",e.emissiveMap?"#define USE_EMISSIVEMAP":"",e.anisotropy?"#define USE_ANISOTROPY":"",e.anisotropyMap?"#define USE_ANISOTROPYMAP":"",e.clearcoat?"#define USE_CLEARCOAT":"",e.clearcoatMap?"#define USE_CLEARCOATMAP":"",e.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",e.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",e.diffuseRoughness?"#define USE_DIFFUSE_ROUGHNESS":"",e.diffuseRoughnessMap?"#define USE_DIFFUSE_ROUGHNESSMAP":"",e.dispersion?"#define USE_DISPERSION":"",e.retroreflection?"#define USE_RETROREFLECTION":"",e.iridescence?"#define USE_IRIDESCENCE":"",e.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",e.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",e.specularMap?"#define USE_SPECULARMAP":"",e.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",e.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",e.roughnessMap?"#define USE_ROUGHNESSMAP":"",e.metalnessMap?"#define USE_METALNESSMAP":"",e.alphaMap?"#define USE_ALPHAMAP":"",e.alphaTest?"#define USE_ALPHATEST":"",e.alphaHash?"#define USE_ALPHAHASH":"",e.sheen?"#define USE_SHEEN":"",e.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",e.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",e.transmission?"#define USE_TRANSMISSION":"",e.transmissionMap?"#define USE_TRANSMISSIONMAP":"",e.thicknessMap?"#define USE_THICKNESSMAP":"",e.vertexTangents&&e.flatShading===!1?"#define USE_TANGENT":"",e.vertexColors||e.instancingColor?"#define USE_COLOR":"",e.vertexAlphas||e.batchingColor?"#define USE_COLOR_ALPHA":"",e.vertexUv1s?"#define USE_UV1":"",e.vertexUv2s?"#define USE_UV2":"",e.vertexUv3s?"#define USE_UV3":"",e.pointsUvs?"#define USE_POINTS_UV":"",e.gradientMap?"#define USE_GRADIENTMAP":"",e.flatShading?"#define FLAT_SHADED":"",e.doubleSided?"#define DOUBLE_SIDED":"",e.flipSided?"#define FLIP_SIDED":"",e.shadowMapEnabled?"#define USE_SHADOWMAP":"",e.shadowMapEnabled?"#define "+l:"",e.premultipliedAlpha?"#define PREMULTIPLIED_ALPHA":"",e.numLightProbes>0?"#define USE_LIGHT_PROBES":"",e.decodeVideoTexture?"#define DECODE_VIDEO_TEXTURE":"",e.decodeVideoTextureEmissive?"#define DECODE_VIDEO_TEXTURE_EMISSIVE":"",e.logarithmicDepthBuffer?"#define USE_LOGARITHMIC_DEPTH_BUFFER":"",e.reversedDepthBuffer?"#define USE_REVERSED_DEPTH_BUFFER":"","uniform mat4 viewMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;",e.toneMapping!==Ci?"#define TONE_MAPPING":"",e.toneMapping!==Ci?_e.tonemapping_pars_fragment:"",e.toneMapping!==Ci?M_("toneMapping",e.toneMapping):"",e.dithering?"#define DITHERING":"",e.opaque?"#define OPAQUE":"",_e.colorspace_pars_fragment,y_("linearToOutputTexel",e.outputColorSpace),S_(),e.useDepthPacking?"#define DEPTH_PACKING "+e.depthPacking:"",`
`].filter(xa).join(`
`)),a=Mh(a),a=Cd(a,e),a=Pd(a,e),o=Mh(o),o=Cd(o,e),o=Pd(o,e),a=Id(a),o=Id(o),e.isRawShaderMaterial!==!0&&(g=`#version 300 es
`,S=[d,"#define attribute in","#define varying out","#define texture2D texture"].join(`
`)+`
`+S,m=["#define varying in",e.glslVersion===rh?"":"layout(location = 0) out highp vec4 pc_fragColor;",e.glslVersion===rh?"":"#define gl_FragColor pc_fragColor","#define gl_FragDepthEXT gl_FragDepth","#define texture2D texture","#define textureCube texture","#define texture2DProj textureProj","#define texture2DLodEXT textureLod","#define texture2DProjLodEXT textureProjLod","#define textureCubeLodEXT textureLod","#define texture2DGradEXT textureGrad","#define texture2DProjGradEXT textureProjGrad","#define textureCubeGradEXT textureGrad"].join(`
`)+`
`+m);let E=g+S+a,P=g+m+o,T=wd(s,s.VERTEX_SHADER,E),C=wd(s,s.FRAGMENT_SHADER,P);s.attachShader(x,T),s.attachShader(x,C),e.index0AttributeName!==void 0?s.bindAttribLocation(x,0,e.index0AttributeName):e.hasPositionAttribute===!0&&s.bindAttribLocation(x,0,"position"),s.linkProgram(x);function A(B){if(i.debug.checkShaderErrors){let k=s.getProgramInfoLog(x)||"",H=s.getShaderInfoLog(T)||"",K=s.getShaderInfoLog(C)||"",U=k.trim(),Y=H.trim(),tt=K.trim(),j=!0,dt=!0;if(s.getProgramParameter(x,s.LINK_STATUS)===!1)if(j=!1,typeof i.debug.onShaderError=="function")i.debug.onShaderError(s,x,T,C);else{let V=Rd(s,T,"vertex"),it=Rd(s,C,"fragment");ie("WebGLProgram: Shader Error "+s.getError()+" - VALIDATE_STATUS "+s.getProgramParameter(x,s.VALIDATE_STATUS)+`

Material Name: `+B.name+`
Material Type: `+B.type+`

Program Info Log: `+U+`
`+V+`
`+it)}else U!==""?Kt("WebGLProgram: Program Info Log:",U):(Y===""||tt==="")&&(dt=!1);dt&&(B.diagnostics={runnable:j,programLog:U,vertexShader:{log:Y,prefix:S},fragmentShader:{log:tt,prefix:m}})}s.deleteShader(T),s.deleteShader(C),_=new Mr(s,x),b=T_(s,x)}let _;this.getUniforms=function(){return _===void 0&&A(this),_};let b;this.getAttributes=function(){return b===void 0&&A(this),b};let G=e.rendererExtensionParallelShaderCompile===!1;return this.isReady=function(){return G===!1&&(G=s.getProgramParameter(x,m_)),G},this.destroy=function(){n.releaseStatesOfProgram(this),s.deleteProgram(x),this.program=void 0},this.type=e.shaderType,this.name=e.shaderName,this.id=g_++,this.cacheKey=t,this.usedTimes=1,this.program=x,this.vertexShader=T,this.fragmentShader=C,this}var O_=0,Sh=class{constructor(){this.shaderCache=new Map,this.materialCache=new Map}update(t,e,n){let s=this._getShaderCacheForMaterial(t);return s.has(e)===!1&&(s.add(e),e.usedTimes++),s.has(n)===!1&&(s.add(n),n.usedTimes++),this}remove(t){let e=this.materialCache.get(t);for(let n of e)n.usedTimes--,n.usedTimes===0&&this.shaderCache.delete(n.code);return this.materialCache.delete(t),this}getVertexShaderStage(t){return this._getShaderStage(t.vertexShader)}getFragmentShaderStage(t){return this._getShaderStage(t.fragmentShader)}dispose(){this.shaderCache.clear(),this.materialCache.clear()}_getShaderCacheForMaterial(t){let e=this.materialCache,n=e.get(t);return n===void 0&&(n=new Set,e.set(t,n)),n}_getShaderStage(t){let e=this.shaderCache,n=e.get(t);return n===void 0&&(n=new bh(t),e.set(t,n)),n}},bh=class{constructor(t){this.id=O_++,this.code=t,this.usedTimes=0}};function B_(i){return i===xs||i===ma||i===ga}function k_(i,t,e,n,s,r){let a=new lr,o=new Sh,l=new Set,c=[],h=new Map,f=n.logarithmicDepthBuffer,d={MeshDepthMaterial:"depth",MeshDistanceMaterial:"distance",MeshNormalMaterial:"normal",MeshBasicMaterial:"basic",MeshLambertMaterial:"lambert",MeshPhongMaterial:"phong",MeshToonMaterial:"toon",MeshStandardMaterial:"physical",MeshPhysicalMaterial:"physical",MeshMatcapMaterial:"matcap",LineBasicMaterial:"basic",LineDashedMaterial:"dashed",PointsMaterial:"points",ShadowMaterial:"shadow",SpriteMaterial:"sprite"};function p(_){return l.add(_),_===0?"uv":`uv${_}`}function x(_,b,G,B,k,H){let K=B.fog,U=k.geometry,Y=_.isMeshStandardMaterial||_.isMeshLambertMaterial||_.isMeshPhongMaterial?B.environment:null,tt=_.isMeshStandardMaterial||_.isMeshLambertMaterial&&!_.envMap||_.isMeshPhongMaterial&&!_.envMap,j=t.get(_.envMap||Y,tt),dt=d[_.type],V=n.precision;_.precision!==null&&(V=n.getMaxPrecision(_.precision),V!==_.precision&&Kt("WebGLProgram.getParameters:",_.precision,"not supported, using",V,"instead."));let it=U.morphAttributes.position||U.morphAttributes.normal||U.morphAttributes.color,ft=it!==void 0?it.length:0,Gt=0;U.morphAttributes.position!==void 0&&(Gt=1),U.morphAttributes.normal!==void 0&&(Gt=2),U.morphAttributes.color!==void 0&&(Gt=3);let ee,at,It,Ft;if(dt){let Lt=Ii[dt];ee=Lt.vertexShader,at=Lt.fragmentShader}else{ee=_.vertexShader,at=_.fragmentShader;let Lt=o.getVertexShaderStage(_),Ce=o.getFragmentShaderStage(_);o.update(_,Lt,Ce),It=Lt.id,Ft=Ce.id}let qt=i.getRenderTarget(),pt=i.state.buffers.depth.getReversed(),oe=k.isInstancedMesh===!0,$t=k.isBatchedMesh===!0,zt=!!_.map,Se=!!_.matcap,ye=!!j,he=ye&&j.isPMREMTexture===!0,Je=!!_.aoMap,Xe=!!_.lightMap,_n=!!_.bumpMap&&_.wireframe===!1,ke=!!_.normalMap,Kn=!!_.displacementMap,on=!!_.emissiveMap,Un=!!_.metalnessMap,pe=!!_.roughnessMap,Zt=_.anisotropy>0,N=_.clearcoat>0,me=_.diffuseRoughness>0,we=_.dispersion>0,ze=_.retroreflectivity>0,Rt=_.iridescence>0,en=_.sheen>0,Pt=_.transmission>0,Dt=Zt&&!!_.anisotropyMap,w=N&&!!_.clearcoatMap,y=N&&!!_.clearcoatNormalMap,W=N&&!!_.clearcoatRoughnessMap,mt=me&&!!_.diffuseRoughnessMap,ct=Rt&&!!_.iridescenceMap,wt=Rt&&!!_.iridescenceThicknessMap,Ct=en&&!!_.sheenColorMap,rt=en&&!!_.sheenRoughnessMap,st=!!_.specularMap,bt=!!_.specularColorMap,L=!!_.specularIntensityMap,nt=Pt&&!!_.transmissionMap,Q=Pt&&!!_.thicknessMap,St=!!_.gradientMap,vt=!!_.alphaMap,_t=_.alphaTest>0,Wt=!!_.alphaHash,de=!!_.extensions,gt=Ci;_.toneMapped&&(qt===null||qt.isXRRenderTarget===!0)&&(gt=i.toneMapping);let Xt=he?j.isCompressedCubeTexture?j.image[0].mipmaps:j.mipmaps:null,le={shaderID:dt,shaderType:_.type,shaderName:_.name,vertexShader:ee,fragmentShader:at,defines:_.defines,customVertexShaderID:It,customFragmentShaderID:Ft,isRawShaderMaterial:_.isRawShaderMaterial===!0,glslVersion:_.glslVersion,precision:V,batching:$t,batchingColor:$t&&k._colorsTexture!==null,instancing:oe,instancingColor:oe&&k.instanceColor!==null,instancingMorph:oe&&k.morphTexture!==null,outputColorSpace:qt===null?i.outputColorSpace:qt.isXRRenderTarget===!0?qt.texture.colorSpace:be.workingColorSpace,alphaToCoverage:!!_.alphaToCoverage,map:zt,matcap:Se,envMap:ye,envMapMode:ye&&j.mapping,envMapPMREM:he,envMapMaxLod:he?Xt.length-1:null,envMapSize:he?Xt[0].width:null,aoMap:Je,lightMap:Xe,bumpMap:_n,normalMap:ke,displacementMap:Kn,emissiveMap:on,normalMapObjectSpace:ke&&_.normalMapType===ju,normalMapTangentSpace:ke&&_.normalMapType===Ll,packedNormalMap:ke&&_.normalMapType===Ll&&B_(_.normalMap.format),metalnessMap:Un,roughnessMap:pe,anisotropy:Zt,anisotropyMap:Dt,clearcoat:N,clearcoatMap:w,clearcoatNormalMap:y,clearcoatRoughnessMap:W,diffuseRoughness:me,diffuseRoughnessMap:mt,dispersion:we,retroreflection:ze,iridescence:Rt,iridescenceMap:ct,iridescenceThicknessMap:wt,sheen:en,sheenColorMap:Ct,sheenRoughnessMap:rt,specularMap:st,specularColorMap:bt,specularIntensityMap:L,transmission:Pt,transmissionMap:nt,thicknessMap:Q,gradientMap:St,opaque:_.transparent===!1&&_.blending===_r&&_.alphaToCoverage===!1,alphaMap:vt,alphaTest:_t,alphaHash:Wt,combine:_.combine,mapUv:zt&&p(_.map.channel),aoMapUv:Je&&p(_.aoMap.channel),lightMapUv:Xe&&p(_.lightMap.channel),bumpMapUv:_n&&p(_.bumpMap.channel),normalMapUv:ke&&p(_.normalMap.channel),displacementMapUv:Kn&&p(_.displacementMap.channel),emissiveMapUv:on&&p(_.emissiveMap.channel),metalnessMapUv:Un&&p(_.metalnessMap.channel),roughnessMapUv:pe&&p(_.roughnessMap.channel),anisotropyMapUv:Dt&&p(_.anisotropyMap.channel),clearcoatMapUv:w&&p(_.clearcoatMap.channel),clearcoatNormalMapUv:y&&p(_.clearcoatNormalMap.channel),clearcoatRoughnessMapUv:W&&p(_.clearcoatRoughnessMap.channel),diffuseRoughnessMapUv:mt&&p(_.diffuseRoughnessMap.channel),iridescenceMapUv:ct&&p(_.iridescenceMap.channel),iridescenceThicknessMapUv:wt&&p(_.iridescenceThicknessMap.channel),sheenColorMapUv:Ct&&p(_.sheenColorMap.channel),sheenRoughnessMapUv:rt&&p(_.sheenRoughnessMap.channel),specularMapUv:st&&p(_.specularMap.channel),specularColorMapUv:bt&&p(_.specularColorMap.channel),specularIntensityMapUv:L&&p(_.specularIntensityMap.channel),transmissionMapUv:nt&&p(_.transmissionMap.channel),thicknessMapUv:Q&&p(_.thicknessMap.channel),alphaMapUv:vt&&p(_.alphaMap.channel),vertexTangents:!!U.attributes.tangent&&(ke||Zt),vertexNormals:!!U.attributes.normal,vertexColors:_.vertexColors,vertexAlphas:_.vertexColors===!0&&!!U.attributes.color&&U.attributes.color.itemSize===4,pointsUvs:k.isPoints===!0&&!!U.attributes.uv&&(zt||vt),fog:!!K,useFog:_.fog===!0,fogExp2:!!K&&K.isFogExp2,flatShading:_.wireframe===!1&&(_.flatShading===!0||U.attributes.normal===void 0&&ke===!1&&(_.isMeshLambertMaterial||_.isMeshPhongMaterial||_.isMeshStandardMaterial||_.isMeshPhysicalMaterial)),sizeAttenuation:_.sizeAttenuation===!0,logarithmicDepthBuffer:f,reversedDepthBuffer:pt,skinning:k.isSkinnedMesh===!0,hasPositionAttribute:U.attributes.position!==void 0,morphTargets:U.morphAttributes.position!==void 0,morphNormals:U.morphAttributes.normal!==void 0,morphColors:U.morphAttributes.color!==void 0,morphTargetsCount:ft,morphTextureStride:Gt,numSunLights:b.sun.length,numDirLights:b.directional.length,numPointLights:b.point.length,numSpotLights:b.spot.length,numSpotLightMaps:b.spotLightMap.length,numRectAreaLights:b.rectArea.length,numHemiLights:b.hemi.length,numSunLightShadows:b.sunShadowMap.length,numDirLightShadows:b.directionalShadowMap.length,numPointLightShadows:b.pointShadowMap.length,numSpotLightShadows:b.spotShadowMap.length,numSpotLightShadowsWithMaps:b.numSpotLightShadowsWithMaps,numLightProbes:b.numLightProbes,numLightProbeGrids:H.filter(Lt=>Lt.texture!==null).length,numClippingPlanes:r.numPlanes,numClipIntersection:r.numIntersection,dithering:_.dithering,shadowMapEnabled:i.shadowMap.enabled&&G.length>0,shadowMapType:i.shadowMap.type,toneMapping:gt,decodeVideoTexture:zt&&_.map.isVideoTexture===!0&&be.getTransfer(_.map.colorSpace)===De,decodeVideoTextureEmissive:on&&_.emissiveMap.isVideoTexture===!0&&be.getTransfer(_.emissiveMap.colorSpace)===De,premultipliedAlpha:_.premultipliedAlpha,doubleSided:_.side===zn,flipSided:_.side===vn,useDepthPacking:_.depthPacking>=0,depthPacking:_.depthPacking||0,index0AttributeName:_.index0AttributeName,extensionClipCullDistance:de&&_.extensions.clipCullDistance===!0&&e.has("WEBGL_clip_cull_distance"),extensionMultiDraw:(de&&_.extensions.multiDraw===!0||$t)&&e.has("WEBGL_multi_draw"),rendererExtensionParallelShaderCompile:e.has("KHR_parallel_shader_compile"),customProgramCacheKey:_.customProgramCacheKey()};return le.vertexUv1s=l.has(1),le.vertexUv2s=l.has(2),le.vertexUv3s=l.has(3),l.clear(),le}function S(_){let b=[];if(_.shaderID?b.push(_.shaderID):(b.push(_.customVertexShaderID),b.push(_.customFragmentShaderID)),_.defines!==void 0)for(let G in _.defines)b.push(G),b.push(_.defines[G]);return _.isRawShaderMaterial===!1&&(m(b,_),g(b,_),b.push(i.outputColorSpace)),b.push(_.customProgramCacheKey),b.join()}function m(_,b){_.push(b.precision),_.push(b.outputColorSpace),_.push(b.envMapMode),_.push(b.envMapPMREM),_.push(b.envMapMaxLod),_.push(b.envMapSize),_.push(b.mapUv),_.push(b.alphaMapUv),_.push(b.lightMapUv),_.push(b.aoMapUv),_.push(b.bumpMapUv),_.push(b.normalMapUv),_.push(b.displacementMapUv),_.push(b.emissiveMapUv),_.push(b.metalnessMapUv),_.push(b.roughnessMapUv),_.push(b.anisotropyMapUv),_.push(b.clearcoatMapUv),_.push(b.clearcoatNormalMapUv),_.push(b.clearcoatRoughnessMapUv),_.push(b.diffuseRoughnessMapUv),_.push(b.iridescenceMapUv),_.push(b.iridescenceThicknessMapUv),_.push(b.sheenColorMapUv),_.push(b.sheenRoughnessMapUv),_.push(b.specularMapUv),_.push(b.specularColorMapUv),_.push(b.specularIntensityMapUv),_.push(b.transmissionMapUv),_.push(b.thicknessMapUv),_.push(b.combine),_.push(b.fogExp2),_.push(b.sizeAttenuation),_.push(b.morphTargetsCount),_.push(b.numSunLights),_.push(b.numDirLights),_.push(b.numPointLights),_.push(b.numSpotLights),_.push(b.numSpotLightMaps),_.push(b.numHemiLights),_.push(b.numRectAreaLights),_.push(b.numSunLightShadows),_.push(b.numDirLightShadows),_.push(b.numPointLightShadows),_.push(b.numSpotLightShadows),_.push(b.numSpotLightShadowsWithMaps),_.push(b.numLightProbes),_.push(b.numLightProbeGrids),_.push(b.shadowMapType),_.push(b.toneMapping),_.push(b.numClippingPlanes),_.push(b.numClipIntersection),_.push(b.depthPacking)}function g(_,b){a.disableAll(),b.instancing&&a.enable(0),b.instancingColor&&a.enable(1),b.instancingMorph&&a.enable(2),b.matcap&&a.enable(3),b.envMap&&a.enable(4),b.normalMapObjectSpace&&a.enable(5),b.normalMapTangentSpace&&a.enable(6),b.clearcoat&&a.enable(7),b.iridescence&&a.enable(8),b.alphaTest&&a.enable(9),b.vertexColors&&a.enable(10),b.vertexAlphas&&a.enable(11),b.vertexUv1s&&a.enable(12),b.vertexUv2s&&a.enable(13),b.vertexUv3s&&a.enable(14),b.vertexTangents&&a.enable(15),b.anisotropy&&a.enable(16),b.alphaHash&&a.enable(17),b.batching&&a.enable(18),b.dispersion&&a.enable(19),b.retroreflection&&a.enable(24),b.diffuseRoughness&&a.enable(25),b.batchingColor&&a.enable(20),b.gradientMap&&a.enable(21),b.packedNormalMap&&a.enable(22),b.vertexNormals&&a.enable(23),_.push(a.mask),a.disableAll(),b.fog&&a.enable(0),b.useFog&&a.enable(1),b.flatShading&&a.enable(2),b.logarithmicDepthBuffer&&a.enable(3),b.reversedDepthBuffer&&a.enable(4),b.skinning&&a.enable(5),b.morphTargets&&a.enable(6),b.morphNormals&&a.enable(7),b.morphColors&&a.enable(8),b.premultipliedAlpha&&a.enable(9),b.shadowMapEnabled&&a.enable(10),b.doubleSided&&a.enable(11),b.flipSided&&a.enable(12),b.useDepthPacking&&a.enable(13),b.dithering&&a.enable(14),b.transmission&&a.enable(15),b.sheen&&a.enable(16),b.opaque&&a.enable(17),b.pointsUvs&&a.enable(18),b.decodeVideoTexture&&a.enable(19),b.decodeVideoTextureEmissive&&a.enable(20),b.alphaToCoverage&&a.enable(21),b.numLightProbeGrids>0&&a.enable(22),b.hasPositionAttribute&&a.enable(23),_.push(a.mask)}function E(_){let b=d[_.type],G;if(b){let B=Ii[b];G=fd.clone(B.uniforms)}else G=_.uniforms;return G}function P(_,b){let G=h.get(b);return G!==void 0?++G.usedTimes:(G=new F_(i,b,_,s),c.push(G),h.set(b,G)),G}function T(_){if(--_.usedTimes===0){let b=c.indexOf(_);c[b]=c[c.length-1],c.pop(),h.delete(_.cacheKey),_.destroy()}}function C(_){o.remove(_)}function A(){o.dispose()}return{getParameters:x,getProgramCacheKey:S,getUniforms:E,acquireProgram:P,releaseProgram:T,releaseShaderCache:C,programs:c,dispose:A}}function z_(){let i=new WeakMap;function t(a){return i.has(a)}function e(a){let o=i.get(a);return o===void 0&&(o={},i.set(a,o)),o}function n(a){i.delete(a)}function s(a,o,l){i.get(a)[o]=l}function r(){i=new WeakMap}return{has:t,get:e,remove:n,update:s,dispose:r}}function H_(i,t){return i.groupOrder!==t.groupOrder?i.groupOrder-t.groupOrder:i.renderOrder!==t.renderOrder?i.renderOrder-t.renderOrder:i.material.id!==t.material.id?i.material.id-t.material.id:i.materialVariant!==t.materialVariant?i.materialVariant-t.materialVariant:i.z!==t.z?i.z-t.z:i.id-t.id}function Nd(i,t){return i.groupOrder!==t.groupOrder?i.groupOrder-t.groupOrder:i.renderOrder!==t.renderOrder?i.renderOrder-t.renderOrder:i.z!==t.z?t.z-i.z:i.id-t.id}function Dd(){let i=[],t=0,e=[],n=[],s=[];function r(){t=0,e.length=0,n.length=0,s.length=0}function a(d){let p=0;return d.isInstancedMesh&&(p+=2),d.isSkinnedMesh&&(p+=1),p}function o(d,p,x,S,m,g){let E=i[t];return E===void 0?(E={id:d.id,object:d,geometry:p,material:x,materialVariant:a(d),groupOrder:S,renderOrder:d.renderOrder,z:m,group:g},i[t]=E):(E.id=d.id,E.object=d,E.geometry=p,E.material=x,E.materialVariant=a(d),E.groupOrder=S,E.renderOrder=d.renderOrder,E.z=m,E.group=g),t++,E}function l(d,p,x,S,m,g,E){E.reversedDepth===!0&&(m=-m);let P=o(d,p,x,S,m,g);x.transmission>0?n.push(P):x.transparent===!0?s.push(P):e.push(P)}function c(d,p,x,S,m,g){let E=o(d,p,x,S,m,g);x.transmission>0?n.unshift(E):x.transparent===!0?s.unshift(E):e.unshift(E)}function h(d,p){e.length>1&&e.sort(d||H_),n.length>1&&n.sort(p||Nd),s.length>1&&s.sort(p||Nd)}function f(){for(let d=t,p=i.length;d<p;d++){let x=i[d];if(x.id===null)break;x.id=null,x.object=null,x.geometry=null,x.material=null,x.group=null}}return{opaque:e,transmissive:n,transparent:s,init:r,push:l,unshift:c,finish:f,sort:h}}function G_(){let i=new WeakMap;function t(n,s){let r=i.get(n),a;return r===void 0?(a=new Dd,i.set(n,[a])):s>=r.length?(a=new Dd,r.push(a)):a=r[s],a}function e(){i=new WeakMap}return{get:t,dispose:e}}function V_(){let i={};return{get:function(t){if(i[t.id]!==void 0)return i[t.id];let e;switch(t.type){case"SunLight":case"DirectionalLight":e={direction:new D,color:new fe};break;case"SpotLight":e={position:new D,direction:new D,color:new fe,distance:0,coneCos:0,penumbraCos:0,decay:0};break;case"PointLight":e={position:new D,color:new fe,distance:0,decay:0};break;case"HemisphereLight":e={direction:new D,skyColor:new fe,groundColor:new fe};break;case"RectAreaLight":e={color:new fe,position:new D,halfWidth:new D,halfHeight:new D};break}return i[t.id]=e,e}}}function W_(){let i={};return{get:function(t){if(i[t.id]!==void 0)return i[t.id];let e;switch(t.type){case"SunLight":case"DirectionalLight":e={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new kt};break;case"SpotLight":e={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new kt};break;case"PointLight":e={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new kt,shadowCameraNear:1,shadowCameraFar:1e3};break}return i[t.id]=e,e}}}var X_=0;function q_(i,t){return(t.castShadow?2:0)-(i.castShadow?2:0)+(t.map?1:0)-(i.map?1:0)}function Y_(i){let t=new V_,e=W_(),n={version:0,hash:{sunLength:-1,directionalLength:-1,pointLength:-1,spotLength:-1,rectAreaLength:-1,hemiLength:-1,numSunShadows:-1,numDirectionalShadows:-1,numPointShadows:-1,numSpotShadows:-1,numSpotMaps:-1,numLightProbes:-1},ambient:[0,0,0],probe:[],sun:[],sunShadow:[],sunShadowMap:[],sunShadowMatrix:[],sunShadowCascade:[],directional:[],directionalShadow:[],directionalShadowMap:[],directionalShadowMatrix:[],spot:[],spotLightMap:[],spotShadow:[],spotShadowMap:[],spotLightMatrix:[],rectArea:[],rectAreaLTC1:null,rectAreaLTC2:null,point:[],pointShadow:[],pointShadowMap:[],pointShadowMatrix:[],hemi:[],numSpotLightShadowsWithMaps:0,numLightProbes:0};for(let c=0;c<9;c++)n.probe.push(new D);let s=new D,r=new Ge,a=new Ge;function o(c){let h=0,f=0,d=0;for(let H=0;H<9;H++)n.probe[H].set(0,0,0);let p=0,x=0,S=0,m=0,g=0,E=0,P=0,T=0,C=0,A=0,_=0,b=0,G=0,B=0;c.sort(q_);for(let H=0,K=c.length;H<K;H++){let U=c[H],Y=U.color,tt=U.intensity,j=U.distance,dt=null;if(U.shadow&&U.shadow.map&&(U.shadow.map.texture.format===xs?dt=U.shadow.map.texture:dt=U.shadow.map.depthTexture||U.shadow.map.texture),U.isAmbientLight)h+=Y.r*tt,f+=Y.g*tt,d+=Y.b*tt;else if(U.isLightProbe){for(let V=0;V<9;V++)n.probe[V].addScaledVector(U.sh.coefficients[V],tt);B++}else if(U.isSunLight){let V=t.get(U);if(V.color.copy(U.color).multiplyScalar(U.intensity),U.castShadow){let it=U.shadow,ft=e.get(U);ft.shadowIntensity=it.intensity,ft.shadowBias=it.bias,ft.shadowNormalBias=it.normalBias,ft.shadowRadius=it.radius,ft.shadowMapSize.copy(it.mapSize).multiply(it.getFrameExtents()),n.sunShadow[x]=ft,n.sunShadowMap[x]=dt;let Gt=it.getViewportCount();for(let ee=0;ee<Gt;ee++)n.sunShadowMatrix[S+ee]=it.getMatrix(ee),n.sunShadowCascade[S+ee]=it._cascadeData[ee];S+=Gt,x++}n.sun[p]=V,p++}else if(U.isDirectionalLight){let V=t.get(U);if(V.color.copy(U.color).multiplyScalar(U.intensity),U.castShadow){let it=U.shadow,ft=e.get(U);ft.shadowIntensity=it.intensity,ft.shadowBias=it.bias,ft.shadowNormalBias=it.normalBias,ft.shadowRadius=it.radius,ft.shadowMapSize=it.mapSize,n.directionalShadow[m]=ft,n.directionalShadowMap[m]=dt,n.directionalShadowMatrix[m]=U.shadow.matrix,C++}n.directional[m]=V,m++}else if(U.isSpotLight){let V=t.get(U);V.position.setFromMatrixPosition(U.matrixWorld),V.color.copy(Y).multiplyScalar(tt),V.distance=j,V.coneCos=Math.cos(U.angle),V.penumbraCos=Math.cos(U.angle*(1-U.penumbra)),V.decay=U.decay,n.spot[E]=V;let it=U.shadow;if(U.map&&(n.spotLightMap[b]=U.map,b++,it.updateMatrices(U),U.castShadow&&G++),n.spotLightMatrix[E]=it.matrix,U.castShadow){let ft=e.get(U);ft.shadowIntensity=it.intensity,ft.shadowBias=it.bias,ft.shadowNormalBias=it.normalBias,ft.shadowRadius=it.radius,ft.shadowMapSize=it.mapSize,n.spotShadow[E]=ft,n.spotShadowMap[E]=dt,_++}E++}else if(U.isRectAreaLight){let V=t.get(U);V.color.copy(Y).multiplyScalar(tt),V.halfWidth.set(U.width*.5,0,0),V.halfHeight.set(0,U.height*.5,0),n.rectArea[P]=V,P++}else if(U.isPointLight){let V=t.get(U);if(V.color.copy(U.color).multiplyScalar(U.intensity),V.distance=U.distance,V.decay=U.decay,U.castShadow){let it=U.shadow,ft=e.get(U);ft.shadowIntensity=it.intensity,ft.shadowBias=it.bias,ft.shadowNormalBias=it.normalBias,ft.shadowRadius=it.radius,ft.shadowMapSize=it.mapSize,ft.shadowCameraNear=it.camera.near,ft.shadowCameraFar=it.camera.far,n.pointShadow[g]=ft,n.pointShadowMap[g]=dt,n.pointShadowMatrix[g]=U.shadow.matrix,A++}n.point[g]=V,g++}else if(U.isHemisphereLight){let V=t.get(U);V.skyColor.copy(U.color).multiplyScalar(tt),V.groundColor.copy(U.groundColor).multiplyScalar(tt),n.hemi[T]=V,T++}}P>0&&(i.has("OES_texture_float_linear")===!0?(n.rectAreaLTC1=Ut.LTC_FLOAT_1,n.rectAreaLTC2=Ut.LTC_FLOAT_2):(n.rectAreaLTC1=Ut.LTC_HALF_1,n.rectAreaLTC2=Ut.LTC_HALF_2)),n.ambient[0]=h,n.ambient[1]=f,n.ambient[2]=d;let k=n.hash;(k.sunLength!==p||k.directionalLength!==m||k.pointLength!==g||k.spotLength!==E||k.rectAreaLength!==P||k.hemiLength!==T||k.numSunShadows!==x||k.numDirectionalShadows!==C||k.numPointShadows!==A||k.numSpotShadows!==_||k.numSpotMaps!==b||k.numLightProbes!==B)&&(n.sun.length=p,n.directional.length=m,n.spot.length=E,n.rectArea.length=P,n.point.length=g,n.hemi.length=T,n.sunShadow.length=x,n.sunShadowMap.length=x,n.sunShadowMatrix.length=S,n.sunShadowCascade.length=S,n.directionalShadow.length=C,n.directionalShadowMap.length=C,n.directionalShadowMatrix.length=C,n.pointShadow.length=A,n.pointShadowMap.length=A,n.pointShadowMatrix.length=A,n.spotShadow.length=_,n.spotShadowMap.length=_,n.spotLightMatrix.length=_+b-G,n.spotLightMap.length=b,n.numSpotLightShadowsWithMaps=G,n.numLightProbes=B,k.sunLength=p,k.directionalLength=m,k.pointLength=g,k.spotLength=E,k.rectAreaLength=P,k.hemiLength=T,k.numSunShadows=x,k.numDirectionalShadows=C,k.numPointShadows=A,k.numSpotShadows=_,k.numSpotMaps=b,k.numLightProbes=B,n.version=X_++)}function l(c,h){let f=0,d=0,p=0,x=0,S=0,m=0,g=h.matrixWorldInverse;for(let E=0,P=c.length;E<P;E++){let T=c[E];if(T.isSunLight){let C=n.sun[f];C.direction.setFromMatrixPosition(T.matrixWorld),C.direction.transformDirection(g),f++}else if(T.isDirectionalLight){let C=n.directional[d];C.direction.setFromMatrixPosition(T.matrixWorld),s.setFromMatrixPosition(T.target.matrixWorld),C.direction.sub(s),C.direction.transformDirection(g),d++}else if(T.isSpotLight){let C=n.spot[x];C.position.setFromMatrixPosition(T.matrixWorld),C.position.applyMatrix4(g),C.direction.setFromMatrixPosition(T.matrixWorld),s.setFromMatrixPosition(T.target.matrixWorld),C.direction.sub(s),C.direction.transformDirection(g),x++}else if(T.isRectAreaLight){let C=n.rectArea[S];C.position.setFromMatrixPosition(T.matrixWorld),C.position.applyMatrix4(g),a.identity(),r.copy(T.matrixWorld),r.premultiply(g),a.extractRotation(r),C.halfWidth.set(T.width*.5,0,0),C.halfHeight.set(0,T.height*.5,0),C.halfWidth.applyMatrix4(a),C.halfHeight.applyMatrix4(a),S++}else if(T.isPointLight){let C=n.point[p];C.position.setFromMatrixPosition(T.matrixWorld),C.position.applyMatrix4(g),p++}else if(T.isHemisphereLight){let C=n.hemi[m];C.direction.setFromMatrixPosition(T.matrixWorld),C.direction.transformDirection(g),m++}}}return{setup:o,setupView:l,state:n}}function Ud(i){let t=new Y_(i),e=[],n=[],s=[];function r(f){h.camera=f,e.length=0,n.length=0,s.length=0}function a(f){f.isLightProbeGrid?s.push(f):e.push(f)}function o(f){n.push(f)}function l(){t.setup(e),s.sort((f,d)=>f.priority-d.priority||f.id-d.id)}function c(f){t.setupView(e,f)}let h={lightsArray:e,shadowsArray:n,lightProbeGridArray:s,camera:null,lights:t,transmissionRenderTarget:{},textureUnits:0};return{init:r,state:h,setupLights:l,setupLightsView:c,pushLight:a,pushShadow:o}}function Z_(i){let t=new WeakMap;function e(s,r=0){let a=t.get(s),o;return a===void 0?(o=new Ud(i),t.set(s,[o])):r>=a.length?(o=new Ud(i),a.push(o)):o=a[r],o}function n(){t=new WeakMap}return{get:e,dispose:n}}var J_=`void main() {
	gl_Position = vec4( position, 1.0 );
}`,K_=`uniform sampler2D shadow_pass;
uniform vec2 resolution;
uniform float radius;
void main() {
	const float samples = float( VSM_SAMPLES );
	float mean = 0.0;
	float squared_mean = 0.0;
	float uvStride = samples <= 1.0 ? 0.0 : 2.0 / ( samples - 1.0 );
	float uvStart = samples <= 1.0 ? 0.0 : - 1.0;
	for ( float i = 0.0; i < samples; i ++ ) {
		float uvOffset = uvStart + i * uvStride;
		#ifdef HORIZONTAL_PASS
			vec2 distribution = texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( uvOffset, 0.0 ) * radius ) / resolution ).rg;
			mean += distribution.x;
			squared_mean += distribution.y * distribution.y + distribution.x * distribution.x;
		#else
			float depth = texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( 0.0, uvOffset ) * radius ) / resolution ).r;
			mean += depth;
			squared_mean += depth * depth;
		#endif
	}
	mean = mean / samples;
	squared_mean = squared_mean / samples;
	float std_dev = sqrt( max( 0.0, squared_mean - mean * mean ) );
	gl_FragColor = vec4( mean, std_dev, 0.0, 1.0 );
}`,$_=[new D(1,0,0),new D(-1,0,0),new D(0,1,0),new D(0,-1,0),new D(0,0,1),new D(0,0,-1)],j_=[new D(0,-1,0),new D(0,-1,0),new D(0,0,1),new D(0,0,-1),new D(0,-1,0),new D(0,-1,0)],Fd=new Ge,_a=new D,_h=new D;function Q_(i,t,e){let n=new us,s=new kt,r=new kt,a=new je,o=new Io,l=new Lo,c={},h=e.maxTextureSize,f={[_s]:vn,[vn]:_s,[zn]:zn},d=new ai({defines:{VSM_SAMPLES:8},uniforms:{shadow_pass:{value:null},resolution:{value:new kt},radius:{value:4}},vertexShader:J_,fragmentShader:K_}),p=d.clone();p.defines.HORIZONTAL_PASS=1;let x=new Sn;x.setAttribute("position",new Ti(new Float32Array([-1,-1,.5,3,-1,.5,-1,3,.5]),3));let S=new Qt(x,d),m=this;this.enabled=!1,this.autoUpdate=!0,this.needsUpdate=!1,this.type=Cs;let g=this.type;this.render=function(A,_,b){if(m.enabled===!1||m.autoUpdate===!1&&m.needsUpdate===!1||A.length===0)return;this.type===qo&&(Kt("WebGLShadowMap: PCFSoftShadowMap has been removed. Using PCFShadowMap instead."),this.type=Cs);let G=i.getRenderTarget(),B=i.getActiveCubeFace(),k=i.getActiveMipmapLevel(),H=i.state;H.setBlending(Ps),H.buffers.depth.getReversed()===!0?H.buffers.color.setClear(0,0,0,0):H.buffers.color.setClear(1,1,1,1),H.buffers.depth.setTest(!0),H.setScissorTest(!1);let K=g!==this.type;K&&_.traverse(function(U){U.material&&(Array.isArray(U.material)?U.material.forEach(Y=>Y.needsUpdate=!0):U.material.needsUpdate=!0)});for(let U=0,Y=A.length;U<Y;U++){let tt=A[U],j=tt.shadow;if(j===void 0){Kt("WebGLShadowMap:",tt,"has no shadow.");continue}if(j.autoUpdate===!1&&j.needsUpdate===!1)continue;s.copy(j.mapSize);let dt=j.getFrameExtents();s.multiply(dt),r.copy(j.mapSize),(s.x>h||s.y>h)&&(s.x>h&&(r.x=Math.floor(h/dt.x),s.x=r.x*dt.x,j.mapSize.x=r.x),s.y>h&&(r.y=Math.floor(h/dt.y),s.y=r.y*dt.y,j.mapSize.y=r.y));let V=i.state.buffers.depth.getReversed();if(j.camera._reversedDepth=V,j.map===null||K===!0){if(j.map!==null&&(j.map.depthTexture!==null&&(j.map.depthTexture.dispose(),j.map.depthTexture=null),j.map.dispose()),this.type===gr){if(tt.isPointLight){Kt("WebGLShadowMap: VSM shadow maps are not supported for PointLights. Use PCF or BasicShadowMap instead.");continue}j.map=new Zn(s.x,s.y,{format:xs,type:xi,minFilter:Ln,magFilter:Ln,generateMipmaps:!1}),j.map.texture.name=tt.name+".shadowMap",j.map.depthTexture=new Vi(s.x,s.y,_i),j.map.depthTexture.name=tt.name+".shadowMapDepth",j.map.depthTexture.format=zi,j.map.depthTexture.compareFunction=null,j.map.depthTexture.minFilter=cn,j.map.depthTexture.magFilter=cn}else tt.isPointLight?(j.map=new ya(s.x),j.map.depthTexture=new Qr(s.x,gi)):(j.map=new Zn(s.x,s.y),j.map.depthTexture=new Vi(s.x,s.y,gi)),j.map.depthTexture.name=tt.name+".shadowMap",j.map.depthTexture.format=zi,this.type===Cs?(j.map.depthTexture.compareFunction=V?ih:nh,j.map.depthTexture.minFilter=Ln,j.map.depthTexture.magFilter=Ln):(j.map.depthTexture.compareFunction=null,j.map.depthTexture.minFilter=cn,j.map.depthTexture.magFilter=cn);j.camera.updateProjectionMatrix()}j.map.isWebGLCubeRenderTarget!==!0&&(j.map.width!==s.x||j.map.height!==s.y)&&j.map.setSize(s.x,s.y);let it=j.map.isWebGLCubeRenderTarget?6:j.getViewportCount();tt.isPointLight!==!0&&j.updateMatrices(tt,b);let ft=j.camera.layers.mask&4294967294?j.camera.layers:b.layers;for(let Gt=0;Gt<it;Gt++){let ee=j.getCamera(Gt);if(tt.isPointLight){let at=j.camera,It=j.matrix,Ft=tt.distance||at.far;Ft!==at.far&&(at.far=Ft,at.updateProjectionMatrix()),_a.setFromMatrixPosition(tt.matrixWorld),at.position.copy(_a),_h.copy(at.position),_h.add($_[Gt]),at.up.copy(j_[Gt]),at.lookAt(_h),at.updateMatrixWorld(),It.makeTranslation(-_a.x,-_a.y,-_a.z),Fd.multiplyMatrices(at.projectionMatrix,at.matrixWorldInverse),j._frustum.setFromProjectionMatrix(Fd,at.coordinateSystem,at.reversedDepth)}if(j.map.isWebGLCubeRenderTarget)i.setRenderTarget(j.map,Gt),i.clear();else{Gt===0&&(i.setRenderTarget(j.map),i.clear());let at=j.getViewport(Gt);a.set(r.x*at.x,r.y*at.y,r.x*at.z,r.y*at.w),H.viewport(a)}n=j.getFrustum(Gt),T(_,b,ee,tt,ft,this.type)}j.isPointLightShadow!==!0&&this.type===gr&&E(j,b),j.needsUpdate=!1}g=this.type,m.needsUpdate=!1,i.setRenderTarget(G,B,k)};function E(A,_){let b=t.update(S);d.defines.VSM_SAMPLES!==A.blurSamples&&(d.defines.VSM_SAMPLES=A.blurSamples,p.defines.VSM_SAMPLES=A.blurSamples,d.needsUpdate=!0,p.needsUpdate=!0),A.mapPass===null?A.mapPass=new Zn(s.x,s.y,{format:xs,type:xi}):(A.mapPass.width!==A.map.width||A.mapPass.height!==A.map.height)&&A.mapPass.setSize(A.map.width,A.map.height),d.uniforms.shadow_pass.value=A.map.depthTexture,d.uniforms.resolution.value.set(A.map.width,A.map.height),d.uniforms.radius.value=A.radius,i.setRenderTarget(A.mapPass),i.clear(),i.renderBufferDirect(_,null,b,d,S,null),p.uniforms.shadow_pass.value=A.mapPass.texture,p.uniforms.resolution.value.set(A.map.width,A.map.height),p.uniforms.radius.value=A.radius,i.setRenderTarget(A.map),i.clear(),i.renderBufferDirect(_,null,b,p,S,null)}function P(A,_,b,G){let B=null,k=b.isPointLight===!0?A.customDistanceMaterial:A.customDepthMaterial;if(k!==void 0)B=k;else if(B=b.isPointLight===!0?l:o,i.localClippingEnabled&&_.clipShadows===!0&&Array.isArray(_.clippingPlanes)&&_.clippingPlanes.length!==0||_.displacementMap&&_.displacementScale!==0||_.alphaMap&&_.alphaTest>0||_.map&&_.alphaTest>0||_.alphaToCoverage===!0){let H=B.uuid,K=_.uuid,U=c[H];U===void 0&&(U={},c[H]=U);let Y=U[K];Y===void 0&&(Y=B.clone(),U[K]=Y,_.addEventListener("dispose",C)),B=Y}if(B.visible=_.visible,B.wireframe=_.wireframe,G===gr?B.side=_.shadowSide!==null?_.shadowSide:_.side:B.side=_.shadowSide!==null?_.shadowSide:f[_.side],B.alphaMap=_.alphaMap,B.alphaTest=_.alphaToCoverage===!0?.5:_.alphaTest,B.map=_.map,B.clipShadows=_.clipShadows,B.clippingPlanes=_.clippingPlanes,B.clipIntersection=_.clipIntersection,B.displacementMap=_.displacementMap,B.displacementScale=_.displacementScale,B.displacementBias=_.displacementBias,B.wireframeLinewidth=_.wireframeLinewidth,B.linewidth=_.linewidth,b.isPointLight===!0&&B.isMeshDistanceMaterial===!0){let H=i.properties.get(B);H.light=b}return B}function T(A,_,b,G,B,k){if(A.visible===!1)return;if(A.layers.test(B)&&(A.isMesh||A.isLine||A.isPoints)&&(A.castShadow||A.receiveShadow&&k===gr)&&(!A.frustumCulled||A.intersectsFrustum(n))){A.modelViewMatrix.multiplyMatrices(b.matrixWorldInverse,A.matrixWorld);let U=t.update(A),Y=A.material;if(Array.isArray(Y)){let tt=U.groups;for(let j=0,dt=tt.length;j<dt;j++){let V=tt[j],it=Y[V.materialIndex];if(it&&it.visible){let ft=P(A,it,G,k);A.onBeforeShadow(i,A,_,b,U,ft,V),i.renderBufferDirect(b,null,U,ft,A,V),A.onAfterShadow(i,A,_,b,U,ft,V)}}}else if(Y.visible){let tt=P(A,Y,G,k);A.onBeforeShadow(i,A,_,b,U,tt,null),i.renderBufferDirect(b,null,U,tt,A,null),A.onAfterShadow(i,A,_,b,U,tt,null)}}let K=A.children;for(let U=0,Y=K.length;U<Y;U++)T(K[U],_,b,G,B,k)}function C(A){A.target.removeEventListener("dispose",C);for(let b in c){let G=c[b],B=A.target.uuid;B in G&&(G[B].dispose(),delete G[B])}}}function tx(i,t){function e(){let L=!1,nt=new je,Q=null,St=new je(0,0,0,0);return{setMask:function(vt){Q!==vt&&!L&&(i.colorMask(vt,vt,vt,vt),Q=vt)},setLocked:function(vt){L=vt},setClear:function(vt,_t,Wt,de,gt){gt===!0&&(vt*=de,_t*=de,Wt*=de),nt.set(vt,_t,Wt,de),St.equals(nt)===!1&&(i.clearColor(vt,_t,Wt,de),St.copy(nt))},reset:function(){L=!1,Q=null,St.set(-1,0,0,0)}}}function n(){let L=!1,nt=!1,Q=null,St=null,vt=null;return{setReversed:function(_t){if(nt!==_t){let Wt=t.get("EXT_clip_control");_t?Wt.clipControlEXT(Wt.LOWER_LEFT_EXT,Wt.ZERO_TO_ONE_EXT):Wt.clipControlEXT(Wt.LOWER_LEFT_EXT,Wt.NEGATIVE_ONE_TO_ONE_EXT),nt=_t;let de=vt;vt=null,this.setClear(de)}},getReversed:function(){return nt},setTest:function(_t){_t?pt(i.DEPTH_TEST):oe(i.DEPTH_TEST)},setMask:function(_t){Q!==_t&&!L&&(i.depthMask(_t),Q=_t)},setFunc:function(_t){if(nt&&(_t=cd[_t]),St!==_t){switch(_t){case ro:i.depthFunc(i.NEVER);break;case ao:i.depthFunc(i.ALWAYS);break;case oo:i.depthFunc(i.LESS);break;case ir:i.depthFunc(i.LEQUAL);break;case lo:i.depthFunc(i.EQUAL);break;case co:i.depthFunc(i.GEQUAL);break;case ho:i.depthFunc(i.GREATER);break;case uo:i.depthFunc(i.NOTEQUAL);break;default:i.depthFunc(i.LEQUAL)}St=_t}},setLocked:function(_t){L=_t},setClear:function(_t){vt!==_t&&(vt=_t,nt&&(_t=1-_t),i.clearDepth(_t))},reset:function(){L=!1,Q=null,St=null,vt=null,nt=!1}}}function s(){let L=!1,nt=null,Q=null,St=null,vt=null,_t=null,Wt=null,de=null,gt=null;return{setTest:function(Xt){L||(Xt?pt(i.STENCIL_TEST):oe(i.STENCIL_TEST))},setMask:function(Xt){nt!==Xt&&!L&&(i.stencilMask(Xt),nt=Xt)},setFunc:function(Xt,le,Lt){(Q!==Xt||St!==le||vt!==Lt)&&(i.stencilFunc(Xt,le,Lt),Q=Xt,St=le,vt=Lt)},setOp:function(Xt,le,Lt){(_t!==Xt||Wt!==le||de!==Lt)&&(i.stencilOp(Xt,le,Lt),_t=Xt,Wt=le,de=Lt)},setLocked:function(Xt){L=Xt},setClear:function(Xt){gt!==Xt&&(i.clearStencil(Xt),gt=Xt)},reset:function(){L=!1,nt=null,Q=null,St=null,vt=null,_t=null,Wt=null,de=null,gt=null}}}let r=new e,a=new n,o=new s,l={},c=new WeakMap,h={},f={},d={},p=new WeakMap,x=[],S=null,m=!1,g=null,E=null,P=null,T=null,C=null,A=null,_=null,b=new fe(0,0,0),G=0,B=!1,k=null,H=null,K=null,U=null,Y=null,tt=i.getParameter(i.MAX_COMBINED_TEXTURE_IMAGE_UNITS),j=!1,dt=0,V=i.getParameter(i.VERSION);V.indexOf("WebGL")!==-1?(dt=parseFloat(/^WebGL (\d)/.exec(V)[1]),j=dt>=1):V.indexOf("OpenGL ES")!==-1&&(dt=parseFloat(/^OpenGL ES (\d)/.exec(V)[1]),j=dt>=2);let it=null,ft={},Gt=i.getParameter(i.SCISSOR_BOX),ee=i.getParameter(i.VIEWPORT),at=new je().fromArray(Gt),It=new je().fromArray(ee);function Ft(L,nt,Q,St){let vt=new Uint8Array(4),_t=i.createTexture();i.bindTexture(L,_t),i.texParameteri(L,i.TEXTURE_MIN_FILTER,i.NEAREST),i.texParameteri(L,i.TEXTURE_MAG_FILTER,i.NEAREST);for(let Wt=0;Wt<Q;Wt++)L===i.TEXTURE_3D||L===i.TEXTURE_2D_ARRAY?i.texImage3D(nt,0,i.RGBA,1,1,St,0,i.RGBA,i.UNSIGNED_BYTE,vt):i.texImage2D(nt+Wt,0,i.RGBA,1,1,0,i.RGBA,i.UNSIGNED_BYTE,vt);return _t}let qt={};qt[i.TEXTURE_2D]=Ft(i.TEXTURE_2D,i.TEXTURE_2D,1),qt[i.TEXTURE_CUBE_MAP]=Ft(i.TEXTURE_CUBE_MAP,i.TEXTURE_CUBE_MAP_POSITIVE_X,6),qt[i.TEXTURE_2D_ARRAY]=Ft(i.TEXTURE_2D_ARRAY,i.TEXTURE_2D_ARRAY,1,1),qt[i.TEXTURE_3D]=Ft(i.TEXTURE_3D,i.TEXTURE_3D,1,1),r.setClear(0,0,0,1),a.setClear(1),o.setClear(0),pt(i.DEPTH_TEST),a.setFunc(ir),_n(!1),ke(Uc),pt(i.CULL_FACE),Je(Ps);function pt(L){h[L]!==!0&&(i.enable(L),h[L]=!0)}function oe(L){h[L]!==!1&&(i.disable(L),h[L]=!1)}function $t(L,nt){return d[L]!==nt?(i.bindFramebuffer(L,nt),d[L]=nt,L===i.DRAW_FRAMEBUFFER&&(d[i.FRAMEBUFFER]=nt),L===i.FRAMEBUFFER&&(d[i.DRAW_FRAMEBUFFER]=nt),!0):!1}function zt(L,nt){let Q=x,St=!1;if(L){Q=p.get(nt),Q===void 0&&(Q=[],p.set(nt,Q));let vt=L.textures;if(Q.length!==vt.length||Q[0]!==i.COLOR_ATTACHMENT0){for(let _t=0,Wt=vt.length;_t<Wt;_t++)Q[_t]=i.COLOR_ATTACHMENT0+_t;Q.length=vt.length,St=!0}}else Q[0]!==i.BACK&&(Q[0]=i.BACK,St=!0);St&&i.drawBuffers(Q)}function Se(L){return S!==L?(i.useProgram(L),S=L,!0):!1}let ye={[Is]:i.FUNC_ADD,[Iu]:i.FUNC_SUBTRACT,[Lu]:i.FUNC_REVERSE_SUBTRACT};ye[Nu]=i.MIN,ye[Du]=i.MAX;let he={[Uu]:i.ZERO,[Fu]:i.ONE,[Ou]:i.SRC_COLOR,[kc]:i.SRC_ALPHA,[Vu]:i.SRC_ALPHA_SATURATE,[Hu]:i.DST_COLOR,[ku]:i.DST_ALPHA,[Bu]:i.ONE_MINUS_SRC_COLOR,[zc]:i.ONE_MINUS_SRC_ALPHA,[Gu]:i.ONE_MINUS_DST_COLOR,[zu]:i.ONE_MINUS_DST_ALPHA,[Wu]:i.CONSTANT_COLOR,[Xu]:i.ONE_MINUS_CONSTANT_COLOR,[qu]:i.CONSTANT_ALPHA,[Yu]:i.ONE_MINUS_CONSTANT_ALPHA};function Je(L,nt,Q,St,vt,_t,Wt,de,gt,Xt){if(L===Ps){m===!0&&(oe(i.BLEND),m=!1);return}if(m===!1&&(pt(i.BLEND),m=!0),L!==Pu){if(L!==g||Xt!==B){if((E!==Is||C!==Is)&&(i.blendEquation(i.FUNC_ADD),E=Is,C=Is),Xt)switch(L){case _r:i.blendFuncSeparate(i.ONE,i.ONE_MINUS_SRC_ALPHA,i.ONE,i.ONE_MINUS_SRC_ALPHA);break;case Fc:i.blendFunc(i.ONE,i.ONE);break;case Oc:i.blendFuncSeparate(i.ZERO,i.ONE_MINUS_SRC_COLOR,i.ZERO,i.ONE);break;case Bc:i.blendFuncSeparate(i.DST_COLOR,i.ONE_MINUS_SRC_ALPHA,i.ZERO,i.ONE);break;default:ie("WebGLState: Invalid blending: ",L);break}else switch(L){case _r:i.blendFuncSeparate(i.SRC_ALPHA,i.ONE_MINUS_SRC_ALPHA,i.ONE,i.ONE_MINUS_SRC_ALPHA);break;case Fc:i.blendFuncSeparate(i.SRC_ALPHA,i.ONE,i.ONE,i.ONE);break;case Oc:ie("WebGLState: SubtractiveBlending requires material.premultipliedAlpha = true");break;case Bc:ie("WebGLState: MultiplyBlending requires material.premultipliedAlpha = true");break;default:ie("WebGLState: Invalid blending: ",L);break}P=null,T=null,A=null,_=null,b.set(0,0,0),G=0,g=L,B=Xt}return}vt=vt||nt,_t=_t||Q,Wt=Wt||St,(nt!==E||vt!==C)&&(i.blendEquationSeparate(ye[nt],ye[vt]),E=nt,C=vt),(Q!==P||St!==T||_t!==A||Wt!==_)&&(i.blendFuncSeparate(he[Q],he[St],he[_t],he[Wt]),P=Q,T=St,A=_t,_=Wt),(de.equals(b)===!1||gt!==G)&&(i.blendColor(de.r,de.g,de.b,gt),b.copy(de),G=gt),g=L,B=!1}function Xe(L,nt){L.side===zn?oe(i.CULL_FACE):pt(i.CULL_FACE);let Q=L.side===vn;nt&&(Q=!Q),_n(Q),L.blending===_r&&L.transparent===!1?Je(Ps):Je(L.blending,L.blendEquation,L.blendSrc,L.blendDst,L.blendEquationAlpha,L.blendSrcAlpha,L.blendDstAlpha,L.blendColor,L.blendAlpha,L.premultipliedAlpha),a.setFunc(L.depthFunc),a.setTest(L.depthTest),a.setMask(L.depthWrite),r.setMask(L.colorWrite);let St=L.stencilWrite;o.setTest(St),St&&(o.setMask(L.stencilWriteMask),o.setFunc(L.stencilFunc,L.stencilRef,L.stencilFuncMask),o.setOp(L.stencilFail,L.stencilZFail,L.stencilZPass)),on(L.polygonOffset,L.polygonOffsetFactor,L.polygonOffsetUnits),L.alphaToCoverage===!0?pt(i.SAMPLE_ALPHA_TO_COVERAGE):oe(i.SAMPLE_ALPHA_TO_COVERAGE)}function _n(L){k!==L&&(L?i.frontFace(i.CW):i.frontFace(i.CCW),k=L)}function ke(L){L!==Ru?(pt(i.CULL_FACE),L!==H&&(L===Uc?i.cullFace(i.BACK):L===Cu?i.cullFace(i.FRONT):i.cullFace(i.FRONT_AND_BACK))):oe(i.CULL_FACE),H=L}function Kn(L){L!==K&&(j&&i.lineWidth(L),K=L)}function on(L,nt,Q){L?(pt(i.POLYGON_OFFSET_FILL),(U!==nt||Y!==Q)&&(U=nt,Y=Q,a.getReversed()&&(nt=-nt,Q=-Q),i.polygonOffset(nt,Q))):oe(i.POLYGON_OFFSET_FILL)}function Un(L){L?pt(i.SCISSOR_TEST):oe(i.SCISSOR_TEST)}function pe(L){L===void 0&&(L=i.TEXTURE0+tt-1),it!==L&&(i.activeTexture(L),it=L)}function Zt(L,nt,Q){Q===void 0&&(it===null?Q=i.TEXTURE0+tt-1:Q=it);let St=ft[Q];St===void 0&&(St={type:void 0,texture:void 0},ft[Q]=St),(St.type!==L||St.texture!==nt)&&(it!==Q&&(i.activeTexture(Q),it=Q),i.bindTexture(L,nt||qt[L]),St.type=L,St.texture=nt)}function N(){let L=ft[it];L!==void 0&&L.type!==void 0&&(i.bindTexture(L.type,null),L.type=void 0,L.texture=void 0)}function me(){try{i.compressedTexImage2D(...arguments)}catch(L){ie("WebGLState:",L)}}function we(){try{i.compressedTexImage3D(...arguments)}catch(L){ie("WebGLState:",L)}}function ze(){try{i.texSubImage2D(...arguments)}catch(L){ie("WebGLState:",L)}}function Rt(){try{i.texSubImage3D(...arguments)}catch(L){ie("WebGLState:",L)}}function en(){try{i.compressedTexSubImage2D(...arguments)}catch(L){ie("WebGLState:",L)}}function Pt(){try{i.compressedTexSubImage3D(...arguments)}catch(L){ie("WebGLState:",L)}}function Dt(){try{i.texStorage2D(...arguments)}catch(L){ie("WebGLState:",L)}}function w(){try{i.texStorage3D(...arguments)}catch(L){ie("WebGLState:",L)}}function y(){try{i.texImage2D(...arguments)}catch(L){ie("WebGLState:",L)}}function W(){try{i.texImage3D(...arguments)}catch(L){ie("WebGLState:",L)}}function mt(L){return f[L]!==void 0?f[L]:i.getParameter(L)}function ct(L,nt){f[L]!==nt&&(i.pixelStorei(L,nt),f[L]=nt)}function wt(L){at.equals(L)===!1&&(i.scissor(L.x,L.y,L.z,L.w),at.copy(L))}function Ct(L){It.equals(L)===!1&&(i.viewport(L.x,L.y,L.z,L.w),It.copy(L))}function rt(L,nt){let Q=c.get(nt);Q===void 0&&(Q=new WeakMap,c.set(nt,Q));let St=Q.get(L);St===void 0&&(St=i.getUniformBlockIndex(nt,L.name),i.uniformBlockBinding(nt,St,St),Q.set(L,St))}function st(L,nt,Q){let vt=c.get(nt).get(L);l[vt]!==Q&&(i.bindBufferBase(i.UNIFORM_BUFFER,vt,Q),l[vt]=Q)}function bt(){i.disable(i.BLEND),i.disable(i.CULL_FACE),i.disable(i.DEPTH_TEST),i.disable(i.POLYGON_OFFSET_FILL),i.disable(i.SCISSOR_TEST),i.disable(i.STENCIL_TEST),i.disable(i.SAMPLE_ALPHA_TO_COVERAGE),i.blendEquation(i.FUNC_ADD),i.blendFunc(i.ONE,i.ZERO),i.blendFuncSeparate(i.ONE,i.ZERO,i.ONE,i.ZERO),i.blendColor(0,0,0,0),i.colorMask(!0,!0,!0,!0),i.clearColor(0,0,0,0),i.depthMask(!0),i.depthFunc(i.LESS),a.setReversed(!1),i.clearDepth(1),i.stencilMask(4294967295),i.stencilFunc(i.ALWAYS,0,4294967295),i.stencilOp(i.KEEP,i.KEEP,i.KEEP),i.clearStencil(0),i.cullFace(i.BACK),i.frontFace(i.CCW),i.polygonOffset(0,0),i.activeTexture(i.TEXTURE0),i.bindFramebuffer(i.FRAMEBUFFER,null),i.bindFramebuffer(i.DRAW_FRAMEBUFFER,null),i.bindFramebuffer(i.READ_FRAMEBUFFER,null),i.useProgram(null),i.lineWidth(1),i.scissor(0,0,i.canvas.width,i.canvas.height),i.viewport(0,0,i.canvas.width,i.canvas.height),i.pixelStorei(i.PACK_ALIGNMENT,4),i.pixelStorei(i.UNPACK_ALIGNMENT,4),i.pixelStorei(i.UNPACK_FLIP_Y_WEBGL,!1),i.pixelStorei(i.UNPACK_PREMULTIPLY_ALPHA_WEBGL,!1),i.pixelStorei(i.UNPACK_COLORSPACE_CONVERSION_WEBGL,i.BROWSER_DEFAULT_WEBGL),i.pixelStorei(i.PACK_ROW_LENGTH,0),i.pixelStorei(i.PACK_SKIP_PIXELS,0),i.pixelStorei(i.PACK_SKIP_ROWS,0),i.pixelStorei(i.UNPACK_ROW_LENGTH,0),i.pixelStorei(i.UNPACK_IMAGE_HEIGHT,0),i.pixelStorei(i.UNPACK_SKIP_PIXELS,0),i.pixelStorei(i.UNPACK_SKIP_ROWS,0),i.pixelStorei(i.UNPACK_SKIP_IMAGES,0),h={},f={},it=null,ft={},d={},l={},p=new WeakMap,x=[],S=null,m=!1,g=null,E=null,P=null,T=null,C=null,A=null,_=null,b=new fe(0,0,0),G=0,B=!1,k=null,H=null,K=null,U=null,Y=null,at.set(0,0,i.canvas.width,i.canvas.height),It.set(0,0,i.canvas.width,i.canvas.height),r.reset(),a.reset(),o.reset()}return{buffers:{color:r,depth:a,stencil:o},enable:pt,disable:oe,bindFramebuffer:$t,drawBuffers:zt,useProgram:Se,setBlending:Je,setMaterial:Xe,setFlipSided:_n,setCullFace:ke,setLineWidth:Kn,setPolygonOffset:on,setScissorTest:Un,activeTexture:pe,bindTexture:Zt,unbindTexture:N,compressedTexImage2D:me,compressedTexImage3D:we,texImage2D:y,texImage3D:W,pixelStorei:ct,getParameter:mt,updateUBOMapping:rt,uniformBlockBinding:st,texStorage2D:Dt,texStorage3D:w,texSubImage2D:ze,texSubImage3D:Rt,compressedTexSubImage2D:en,compressedTexSubImage3D:Pt,scissor:wt,viewport:Ct,reset:bt}}function ex(i,t,e,n,s,r,a){let o=t.has("WEBGL_multisampled_render_to_texture")?t.get("WEBGL_multisampled_render_to_texture"):null,l=typeof navigator>"u"?!1:/OculusBrowser/g.test(navigator.userAgent),c=new kt,h=new WeakMap,f=new Set,d,p=new WeakMap,x=new Set,S=new FinalizationRegistry(w=>x.delete(w)),m=!1;try{m=typeof OffscreenCanvas<"u"&&new OffscreenCanvas(1,1).getContext("2d")!==null}catch{}function g(w,y){return m?new OffscreenCanvas(w,y):Yr("canvas")}function E(w,y,W){let mt=1,ct=Dt(w);if((ct.width>W||ct.height>W)&&(mt=W/Math.max(ct.width,ct.height)),mt<1)if(typeof HTMLImageElement<"u"&&w instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&w instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&w instanceof ImageBitmap||typeof VideoFrame<"u"&&w instanceof VideoFrame){let wt=Math.floor(mt*ct.width),Ct=Math.floor(mt*ct.height);d===void 0&&(d=g(wt,Ct));let rt=y?g(wt,Ct):d;return rt.width=wt,rt.height=Ct,rt.getContext("2d").drawImage(w,0,0,wt,Ct),Kt("WebGLRenderer: Texture has been resized from ("+ct.width+"x"+ct.height+") to ("+wt+"x"+Ct+")."),rt}else return"data"in w&&Kt("WebGLRenderer: Image in DataTexture is too big ("+ct.width+"x"+ct.height+")."),w;return w}function P(w){return w.generateMipmaps}function T(w){i.generateMipmap(w)}function C(w){return w.isWebGLCubeRenderTarget?i.TEXTURE_CUBE_MAP:w.isWebGL3DRenderTarget?i.TEXTURE_3D:w.isWebGLArrayRenderTarget||w.isCompressedArrayTexture?i.TEXTURE_2D_ARRAY:i.TEXTURE_2D}function A(w,y,W,mt,ct,wt=!1){if(w!==null){if(i[w]!==void 0)return i[w];Kt("WebGLRenderer: Attempt to use non-existing WebGL internal format '"+w+"'")}let Ct;mt&&(Ct=t.get("EXT_texture_norm16"),Ct||Kt("WebGLRenderer: Unable to use normalized textures without EXT_texture_norm16 extension"));let rt=y;if(y===i.RED&&(W===i.FLOAT&&(rt=i.R32F),W===i.HALF_FLOAT&&(rt=i.R16F),W===i.UNSIGNED_BYTE&&(rt=i.R8),W===i.UNSIGNED_SHORT&&Ct&&(rt=Ct.R16_EXT),W===i.SHORT&&Ct&&(rt=Ct.R16_SNORM_EXT)),y===i.RED_INTEGER&&(W===i.UNSIGNED_BYTE&&(rt=i.R8UI),W===i.UNSIGNED_SHORT&&(rt=i.R16UI),W===i.UNSIGNED_INT&&(rt=i.R32UI),W===i.BYTE&&(rt=i.R8I),W===i.SHORT&&(rt=i.R16I),W===i.INT&&(rt=i.R32I)),y===i.RG&&(W===i.FLOAT&&(rt=i.RG32F),W===i.HALF_FLOAT&&(rt=i.RG16F),W===i.UNSIGNED_BYTE&&(rt=i.RG8),W===i.UNSIGNED_SHORT&&Ct&&(rt=Ct.RG16_EXT),W===i.SHORT&&Ct&&(rt=Ct.RG16_SNORM_EXT)),y===i.RG_INTEGER&&(W===i.UNSIGNED_BYTE&&(rt=i.RG8UI),W===i.UNSIGNED_SHORT&&(rt=i.RG16UI),W===i.UNSIGNED_INT&&(rt=i.RG32UI),W===i.BYTE&&(rt=i.RG8I),W===i.SHORT&&(rt=i.RG16I),W===i.INT&&(rt=i.RG32I)),y===i.RGB_INTEGER&&(W===i.UNSIGNED_BYTE&&(rt=i.RGB8UI),W===i.UNSIGNED_SHORT&&(rt=i.RGB16UI),W===i.UNSIGNED_INT&&(rt=i.RGB32UI),W===i.BYTE&&(rt=i.RGB8I),W===i.SHORT&&(rt=i.RGB16I),W===i.INT&&(rt=i.RGB32I)),y===i.RGBA_INTEGER&&(W===i.UNSIGNED_BYTE&&(rt=i.RGBA8UI),W===i.UNSIGNED_SHORT&&(rt=i.RGBA16UI),W===i.UNSIGNED_INT&&(rt=i.RGBA32UI),W===i.BYTE&&(rt=i.RGBA8I),W===i.SHORT&&(rt=i.RGBA16I),W===i.INT&&(rt=i.RGBA32I)),y===i.RGB&&(W===i.UNSIGNED_SHORT&&Ct&&(rt=Ct.RGB16_EXT),W===i.SHORT&&Ct&&(rt=Ct.RGB16_SNORM_EXT),W===i.UNSIGNED_INT_5_9_9_9_REV&&(rt=i.RGB9_E5),W===i.UNSIGNED_INT_10F_11F_11F_REV&&(rt=i.R11F_G11F_B10F)),y===i.RGBA){let st=wt?qr:be.getTransfer(ct);W===i.FLOAT&&(rt=i.RGBA32F),W===i.HALF_FLOAT&&(rt=i.RGBA16F),W===i.UNSIGNED_BYTE&&(rt=st===De?i.SRGB8_ALPHA8:i.RGBA8),W===i.UNSIGNED_SHORT&&Ct&&(rt=Ct.RGBA16_EXT),W===i.SHORT&&Ct&&(rt=Ct.RGBA16_SNORM_EXT),W===i.UNSIGNED_SHORT_4_4_4_4&&(rt=i.RGBA4),W===i.UNSIGNED_SHORT_5_5_5_1&&(rt=i.RGB5_A1)}return(rt===i.R16F||rt===i.R32F||rt===i.RG16F||rt===i.RG32F||rt===i.RGBA16F||rt===i.RGBA32F)&&t.get("EXT_color_buffer_float"),rt}function _(w,y){let W;return w?y===null||y===gi||y===Ns?W=i.DEPTH24_STENCIL8:y===_i?W=i.DEPTH32F_STENCIL8:y===yr&&(W=i.DEPTH24_STENCIL8,Kt("DepthTexture: 16 bit depth attachment is not supported with stencil. Using 24-bit attachment.")):y===null||y===gi||y===Ns?W=i.DEPTH_COMPONENT24:y===_i?W=i.DEPTH_COMPONENT32F:y===yr&&(W=i.DEPTH_COMPONENT16),W}function b(w,y){return P(w)===!0||w.isFramebufferTexture&&w.minFilter!==cn&&w.minFilter!==Ln?Math.log2(Math.max(y.width,y.height))+1:w.mipmaps.length>0?w.mipmaps.length:w.isCompressedTexture&&Array.isArray(w.image)?y.mipmaps.length:1}function G(w){let y=new WeakRef(w);n.get(w).__ref=y,x.add(y),S.register(w,y,y)}function B(w){let y=n.get(w).__ref;y!==void 0&&(x.delete(y),S.unregister(y))}function k(w){K(w.target)}function H(w){U(w.target)}function K(w){w.removeEventListener("dispose",k),B(w),tt(w),w.isVideoTexture&&h.delete(w),w.isHTMLTexture&&f.delete(w)}function U(w){w.removeEventListener("dispose",H),B(w),dt(w)}function Y(){for(let w of x){let y=w.deref();y!==void 0&&(y.isRenderTarget===!0?U(y):K(y))}x.clear(),f.clear()}function tt(w){let y=n.get(w);if(y.__webglInit===void 0)return;let W=w.source,mt=p.get(W);if(mt){let ct=mt[y.__cacheKey];ct.usedTimes--,ct.usedTimes===0&&j(w),Object.keys(mt).length===0&&p.delete(W)}n.remove(w)}function j(w){let y=n.get(w);i.deleteTexture(y.__webglTexture);let W=w.source,mt=p.get(W);delete mt[y.__cacheKey],a.memory.textures--}function dt(w){let y=n.get(w);y.__depthDisposeCallback&&y.__depthDisposeCallback();let W=w.depthTexture;if(W&&W.renderTarget===w&&K(W),w.isWebGLCubeRenderTarget)for(let ct=0;ct<6;ct++){if(Array.isArray(y.__webglFramebuffer[ct]))for(let wt=0;wt<y.__webglFramebuffer[ct].length;wt++)i.deleteFramebuffer(y.__webglFramebuffer[ct][wt]);else i.deleteFramebuffer(y.__webglFramebuffer[ct]);y.__webglDepthbuffer&&i.deleteRenderbuffer(y.__webglDepthbuffer[ct])}else{if(Array.isArray(y.__webglFramebuffer))for(let ct=0;ct<y.__webglFramebuffer.length;ct++)i.deleteFramebuffer(y.__webglFramebuffer[ct]);else i.deleteFramebuffer(y.__webglFramebuffer);if(y.__webglDepthbuffer&&i.deleteRenderbuffer(y.__webglDepthbuffer),y.__webglMultisampledFramebuffer&&i.deleteFramebuffer(y.__webglMultisampledFramebuffer),y.__webglColorRenderbuffer)for(let ct=0;ct<y.__webglColorRenderbuffer.length;ct++)y.__webglColorRenderbuffer[ct]&&i.deleteRenderbuffer(y.__webglColorRenderbuffer[ct]);y.__webglDepthRenderbuffer&&i.deleteRenderbuffer(y.__webglDepthRenderbuffer)}let mt=w.textures;for(let ct=0,wt=mt.length;ct<wt;ct++){let Ct=n.get(mt[ct]);Ct.__webglTexture&&(i.deleteTexture(Ct.__webglTexture),a.memory.textures--),n.remove(mt[ct])}n.remove(w)}let V=0;function it(){V=0}function ft(){return V}function Gt(w){V=w}function ee(){let w=V;return w>=s.maxTextures&&Kt("WebGLTextures: Trying to use "+(w+1)+" texture units while this GPU supports only "+s.maxTextures),V+=1,w}function at(w){let y=[];return y.push(w.wrapS),y.push(w.wrapT),y.push(w.wrapR||0),y.push(w.magFilter),y.push(w.minFilter),y.push(w.anisotropy),y.push(w.internalFormat),y.push(w.format),y.push(w.type),y.push(w.generateMipmaps),y.push(w.mipmapsAutoUpdate),y.push(w.premultiplyAlpha),y.push(w.flipY),y.push(w.unpackAlignment),y.push(w.colorSpace),y.join()}function It(w,y){let W=n.get(w);if(w.isVideoTexture&&en(w),w.isRenderTargetTexture===!1&&w.isExternalTexture!==!0&&w.version>0&&W.__version!==w.version){let mt=w.image;if(mt===null)Kt("WebGLRenderer: Texture marked for update but no image data found.");else if(mt.complete===!1)Kt("WebGLRenderer: Texture marked for update but image is incomplete");else{Xe(W,w,y);return}}else w.isExternalTexture&&(W.__webglTexture=w.sourceTexture?w.sourceTexture:null);e.bindTexture(i.TEXTURE_2D,W.__webglTexture,i.TEXTURE0+y)}function Ft(w,y){let W=n.get(w);if(w.isRenderTargetTexture===!1&&w.version>0&&W.__version!==w.version){Xe(W,w,y);return}else w.isExternalTexture&&(W.__webglTexture=w.sourceTexture?w.sourceTexture:null);e.bindTexture(i.TEXTURE_2D_ARRAY,W.__webglTexture,i.TEXTURE0+y)}function qt(w,y){let W=n.get(w);if(w.isRenderTargetTexture===!1&&w.version>0&&W.__version!==w.version){Xe(W,w,y);return}e.bindTexture(i.TEXTURE_3D,W.__webglTexture,i.TEXTURE0+y)}function pt(w,y){let W=n.get(w);if(w.version>0&&W.__version!==w.version){_n(W,w,y);return}e.bindTexture(i.TEXTURE_CUBE_MAP,W.__webglTexture,i.TEXTURE0+y)}let oe={[fo]:i.REPEAT,[Ei]:i.CLAMP_TO_EDGE,[po]:i.MIRRORED_REPEAT},$t={[cn]:i.NEAREST,[Ku]:i.NEAREST_MIPMAP_NEAREST,[ha]:i.NEAREST_MIPMAP_LINEAR,[Ln]:i.LINEAR,[Jo]:i.LINEAR_MIPMAP_NEAREST,[qi]:i.LINEAR_MIPMAP_LINEAR},zt={[td]:i.NEVER,[sh]:i.ALWAYS,[ed]:i.LESS,[nh]:i.LEQUAL,[nd]:i.EQUAL,[ih]:i.GEQUAL,[id]:i.GREATER,[sd]:i.NOTEQUAL};function Se(w,y){if(y.type===_i&&t.has("OES_texture_float_linear")===!1&&(y.magFilter===Ln||y.magFilter===Jo||y.magFilter===ha||y.magFilter===qi||y.minFilter===Ln||y.minFilter===Jo||y.minFilter===ha||y.minFilter===qi)&&Kt("WebGLRenderer: Unable to use linear filtering with floating point textures. OES_texture_float_linear not supported on this device."),i.texParameteri(w,i.TEXTURE_WRAP_S,oe[y.wrapS]),i.texParameteri(w,i.TEXTURE_WRAP_T,oe[y.wrapT]),(w===i.TEXTURE_3D||w===i.TEXTURE_2D_ARRAY)&&i.texParameteri(w,i.TEXTURE_WRAP_R,oe[y.wrapR]),i.texParameteri(w,i.TEXTURE_MAG_FILTER,$t[y.magFilter]),i.texParameteri(w,i.TEXTURE_MIN_FILTER,$t[y.minFilter]),y.compareFunction&&(i.texParameteri(w,i.TEXTURE_COMPARE_MODE,i.COMPARE_REF_TO_TEXTURE),i.texParameteri(w,i.TEXTURE_COMPARE_FUNC,zt[y.compareFunction])),t.has("EXT_texture_filter_anisotropic")===!0){if(y.magFilter===cn||y.minFilter!==ha&&y.minFilter!==qi||y.type===_i&&t.has("OES_texture_float_linear")===!1)return;if(y.anisotropy>1||n.get(y).__currentAnisotropy){let W=t.get("EXT_texture_filter_anisotropic");i.texParameterf(w,W.TEXTURE_MAX_ANISOTROPY_EXT,Math.min(y.anisotropy,s.getMaxAnisotropy())),n.get(y).__currentAnisotropy=y.anisotropy}}}function ye(w,y){let W=!1;w.__webglInit===void 0&&(w.__webglInit=!0,y.addEventListener("dispose",k),G(y));let mt=y.source,ct=p.get(mt);ct===void 0&&(ct={},p.set(mt,ct));let wt=at(y);if(wt!==w.__cacheKey){ct[wt]===void 0&&(ct[wt]={texture:i.createTexture(),usedTimes:0},a.memory.textures++,W=!0),ct[wt].usedTimes++;let Ct=ct[w.__cacheKey];Ct!==void 0&&(ct[w.__cacheKey].usedTimes--,Ct.usedTimes===0&&j(y)),w.__cacheKey=wt,w.__webglTexture=ct[wt].texture}return W}function he(w,y,W){return Math.floor(Math.floor(w/W)/y)}function Je(w,y,W,mt){let wt=w.updateRanges;if(wt.length===0)e.texSubImage2D(i.TEXTURE_2D,0,0,0,y.width,y.height,W,mt,y.data);else{wt.sort((L,nt)=>L.start-nt.start);let Ct=0;for(let L=1;L<wt.length;L++){let nt=wt[Ct],Q=wt[L],St=nt.start+nt.count,vt=he(Q.start,y.width,4),_t=he(nt.start,y.width,4);Q.start<=St+1&&vt===_t&&he(Q.start+Q.count-1,y.width,4)===vt?nt.count=Math.max(nt.count,Q.start+Q.count-nt.start):(++Ct,wt[Ct]=Q)}wt.length=Ct+1;let rt=e.getParameter(i.UNPACK_ROW_LENGTH),st=e.getParameter(i.UNPACK_SKIP_PIXELS),bt=e.getParameter(i.UNPACK_SKIP_ROWS);e.pixelStorei(i.UNPACK_ROW_LENGTH,y.width);for(let L=0,nt=wt.length;L<nt;L++){let Q=wt[L],St=Math.floor(Q.start/4),vt=Math.ceil(Q.count/4),_t=St%y.width,Wt=Math.floor(St/y.width),de=vt,gt=1;e.pixelStorei(i.UNPACK_SKIP_PIXELS,_t),e.pixelStorei(i.UNPACK_SKIP_ROWS,Wt),e.texSubImage2D(i.TEXTURE_2D,0,_t,Wt,de,gt,W,mt,y.data)}w.clearUpdateRanges(),e.pixelStorei(i.UNPACK_ROW_LENGTH,rt),e.pixelStorei(i.UNPACK_SKIP_PIXELS,st),e.pixelStorei(i.UNPACK_SKIP_ROWS,bt)}}function Xe(w,y,W){let mt=i.TEXTURE_2D;(y.isDataArrayTexture||y.isCompressedArrayTexture)&&(mt=i.TEXTURE_2D_ARRAY),y.isData3DTexture&&(mt=i.TEXTURE_3D);let ct=ye(w,y),wt=y.source;e.bindTexture(mt,w.__webglTexture,i.TEXTURE0+W);let Ct=n.get(wt);if(wt.version!==Ct.__version||ct===!0){if(e.activeTexture(i.TEXTURE0+W),(typeof ImageBitmap<"u"&&y.image instanceof ImageBitmap)===!1){let gt=be.getPrimaries(be.workingColorSpace),Xt=y.colorSpace===Zi?null:be.getPrimaries(y.colorSpace),le=y.colorSpace===Zi||gt===Xt?i.NONE:i.BROWSER_DEFAULT_WEBGL;e.pixelStorei(i.UNPACK_FLIP_Y_WEBGL,y.flipY),e.pixelStorei(i.UNPACK_PREMULTIPLY_ALPHA_WEBGL,y.premultiplyAlpha),e.pixelStorei(i.UNPACK_COLORSPACE_CONVERSION_WEBGL,le)}e.pixelStorei(i.UNPACK_ALIGNMENT,y.unpackAlignment);let st=E(y.image,!1,s.maxTextureSize);st=Pt(y,st);let bt=r.convert(y.format,y.colorSpace),L=r.convert(y.type),nt=A(y.internalFormat,bt,L,y.normalized,y.colorSpace,y.isVideoTexture);Se(mt,y);let Q,St=y.mipmaps,vt=y.isVideoTexture!==!0,_t=Ct.__version===void 0||ct===!0,Wt=wt.dataReady,de=b(y,st);if(y.isDepthTexture)nt=_(y.format===Yi,y.type),_t&&(vt?e.texStorage2D(i.TEXTURE_2D,1,nt,st.width,st.height):e.texImage2D(i.TEXTURE_2D,0,nt,st.width,st.height,0,bt,L,null));else if(y.isDataTexture)if(St.length>0){vt&&_t&&e.texStorage2D(i.TEXTURE_2D,de,nt,St[0].width,St[0].height);for(let gt=0,Xt=St.length;gt<Xt;gt++)Q=St[gt],vt?Wt&&e.texSubImage2D(i.TEXTURE_2D,gt,0,0,Q.width,Q.height,bt,L,Q.data):e.texImage2D(i.TEXTURE_2D,gt,nt,Q.width,Q.height,0,bt,L,Q.data);y.generateMipmaps=!1}else vt?(_t&&e.texStorage2D(i.TEXTURE_2D,de,nt,st.width,st.height),Wt&&Je(y,st,bt,L)):e.texImage2D(i.TEXTURE_2D,0,nt,st.width,st.height,0,bt,L,st.data);else if(y.isCompressedTexture)if(y.isCompressedArrayTexture){vt&&_t&&e.texStorage3D(i.TEXTURE_2D_ARRAY,de,nt,St[0].width,St[0].height,st.depth);for(let gt=0,Xt=St.length;gt<Xt;gt++)if(Q=St[gt],y.format!==yi)if(bt!==null)if(vt){if(Wt)if(y.layerUpdates.size>0){let le=mh(Q.width,Q.height,y.format,y.type);for(let Lt of y.layerUpdates){let Ce=Q.data.subarray(Lt*le/Q.data.BYTES_PER_ELEMENT,(Lt+1)*le/Q.data.BYTES_PER_ELEMENT);e.compressedTexSubImage3D(i.TEXTURE_2D_ARRAY,gt,0,0,Lt,Q.width,Q.height,1,bt,Ce)}}else e.compressedTexSubImage3D(i.TEXTURE_2D_ARRAY,gt,0,0,0,Q.width,Q.height,st.depth,bt,Q.data)}else e.compressedTexImage3D(i.TEXTURE_2D_ARRAY,gt,nt,Q.width,Q.height,st.depth,0,Q.data,0,0);else Kt("WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()");else vt?Wt&&e.texSubImage3D(i.TEXTURE_2D_ARRAY,gt,0,0,0,Q.width,Q.height,st.depth,bt,L,Q.data):e.texImage3D(i.TEXTURE_2D_ARRAY,gt,nt,Q.width,Q.height,st.depth,0,bt,L,Q.data);y.layerUpdates.size>0&&y.clearLayerUpdates()}else{vt&&_t&&e.texStorage2D(i.TEXTURE_2D,de,nt,St[0].width,St[0].height);for(let gt=0,Xt=St.length;gt<Xt;gt++)Q=St[gt],y.format!==yi?bt!==null?vt?Wt&&e.compressedTexSubImage2D(i.TEXTURE_2D,gt,0,0,Q.width,Q.height,bt,Q.data):e.compressedTexImage2D(i.TEXTURE_2D,gt,nt,Q.width,Q.height,0,Q.data):Kt("WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()"):vt?Wt&&e.texSubImage2D(i.TEXTURE_2D,gt,0,0,Q.width,Q.height,bt,L,Q.data):e.texImage2D(i.TEXTURE_2D,gt,nt,Q.width,Q.height,0,bt,L,Q.data)}else if(y.isDataArrayTexture)if(vt){if(_t&&e.texStorage3D(i.TEXTURE_2D_ARRAY,de,nt,st.width,st.height,st.depth),Wt)if(y.layerUpdates.size>0){let gt=mh(st.width,st.height,y.format,y.type);for(let Xt of y.layerUpdates){let le=st.data.subarray(Xt*gt/st.data.BYTES_PER_ELEMENT,(Xt+1)*gt/st.data.BYTES_PER_ELEMENT);e.texSubImage3D(i.TEXTURE_2D_ARRAY,0,0,0,Xt,st.width,st.height,1,bt,L,le)}y.clearLayerUpdates()}else e.texSubImage3D(i.TEXTURE_2D_ARRAY,0,0,0,0,st.width,st.height,st.depth,bt,L,st.data)}else e.texImage3D(i.TEXTURE_2D_ARRAY,0,nt,st.width,st.height,st.depth,0,bt,L,st.data);else if(y.isData3DTexture)vt?(_t&&e.texStorage3D(i.TEXTURE_3D,de,nt,st.width,st.height,st.depth),Wt&&e.texSubImage3D(i.TEXTURE_3D,0,0,0,0,st.width,st.height,st.depth,bt,L,st.data)):e.texImage3D(i.TEXTURE_3D,0,nt,st.width,st.height,st.depth,0,bt,L,st.data);else if(y.isFramebufferTexture){if(_t)if(vt)e.texStorage2D(i.TEXTURE_2D,de,nt,st.width,st.height);else{let gt=st.width,Xt=st.height;for(let le=0;le<de;le++)e.texImage2D(i.TEXTURE_2D,le,nt,gt,Xt,0,bt,L,null),gt>>=1,Xt>>=1}}else if(y.isHTMLTexture){if("texElementImage2D"in i){let gt=i.canvas;if(gt.hasAttribute("layoutsubtree")||gt.setAttribute("layoutsubtree","true"),st.parentNode!==gt){gt.appendChild(st),f.add(y),gt.onpaint=Xt=>{let le=Xt.changedElements;for(let Lt of f)le.includes(Lt.image)&&(Lt.needsUpdate=!0)},gt.requestPaint();return}if(i.texElementImage2D.length===3)i.texElementImage2D(i.TEXTURE_2D,i.RGBA8,st);else{let le=i.RGBA,Lt=i.RGBA,Ce=i.UNSIGNED_BYTE;i.texElementImage2D(i.TEXTURE_2D,0,le,Lt,Ce,st)}i.texParameteri(i.TEXTURE_2D,i.TEXTURE_MIN_FILTER,i.LINEAR),i.texParameteri(i.TEXTURE_2D,i.TEXTURE_WRAP_S,i.CLAMP_TO_EDGE),i.texParameteri(i.TEXTURE_2D,i.TEXTURE_WRAP_T,i.CLAMP_TO_EDGE)}}else if(St.length>0){if(vt&&_t){let gt=Dt(St[0]);e.texStorage2D(i.TEXTURE_2D,de,nt,gt.width,gt.height)}for(let gt=0,Xt=St.length;gt<Xt;gt++)Q=St[gt],vt?Wt&&e.texSubImage2D(i.TEXTURE_2D,gt,0,0,bt,L,Q):e.texImage2D(i.TEXTURE_2D,gt,nt,bt,L,Q);y.generateMipmaps=!1}else if(vt){if(_t){let gt=Dt(st);e.texStorage2D(i.TEXTURE_2D,de,nt,gt.width,gt.height)}Wt&&e.texSubImage2D(i.TEXTURE_2D,0,0,0,bt,L,st)}else e.texImage2D(i.TEXTURE_2D,0,nt,bt,L,st);P(y)&&y.mipmapsAutoUpdate===!0&&T(mt),Ct.__version=wt.version,y.onUpdate&&y.onUpdate(y)}w.__version=y.version}function _n(w,y,W){if(y.image.length!==6)return;let mt=ye(w,y),ct=y.source;e.bindTexture(i.TEXTURE_CUBE_MAP,w.__webglTexture,i.TEXTURE0+W);let wt=n.get(ct);if(ct.version!==wt.__version||mt===!0){e.activeTexture(i.TEXTURE0+W);let Ct=be.getPrimaries(be.workingColorSpace),rt=y.colorSpace===Zi?null:be.getPrimaries(y.colorSpace),st=y.colorSpace===Zi||Ct===rt?i.NONE:i.BROWSER_DEFAULT_WEBGL;e.pixelStorei(i.UNPACK_FLIP_Y_WEBGL,y.flipY),e.pixelStorei(i.UNPACK_PREMULTIPLY_ALPHA_WEBGL,y.premultiplyAlpha),e.pixelStorei(i.UNPACK_ALIGNMENT,y.unpackAlignment),e.pixelStorei(i.UNPACK_COLORSPACE_CONVERSION_WEBGL,st);let bt=y.isCompressedTexture||y.image[0].isCompressedTexture,L=y.image[0]&&y.image[0].isDataTexture,nt=[];for(let Lt=0;Lt<6;Lt++)!bt&&!L?nt[Lt]=E(y.image[Lt],!0,s.maxCubemapSize):nt[Lt]=L?y.image[Lt].image:y.image[Lt],nt[Lt]=Pt(y,nt[Lt]);let Q=nt[0],St=r.convert(y.format,y.colorSpace),vt=r.convert(y.type),_t=A(y.internalFormat,St,vt,y.normalized,y.colorSpace),Wt=y.isVideoTexture!==!0,de=wt.__version===void 0||mt===!0,gt=ct.dataReady,Xt=b(y,Q);Se(i.TEXTURE_CUBE_MAP,y);let le;if(y.isDepthTexture){if(_t=_(y.format===Yi,y.type),de)if(Wt)e.texStorage2D(i.TEXTURE_CUBE_MAP,1,_t,Q.width,Q.height);else for(let Lt=0;Lt<6;Lt++)e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,0,_t,Q.width,Q.height,0,St,vt,null)}else if(bt){Wt&&de&&e.texStorage2D(i.TEXTURE_CUBE_MAP,Xt,_t,Q.width,Q.height);for(let Lt=0;Lt<6;Lt++){le=nt[Lt].mipmaps;for(let Ce=0;Ce<le.length;Ce++){let Ve=le[Ce];y.format!==yi?St!==null?Wt?gt&&e.compressedTexSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,Ce,0,0,Ve.width,Ve.height,St,Ve.data):e.compressedTexImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,Ce,_t,Ve.width,Ve.height,0,Ve.data):Kt("WebGLRenderer: Attempt to load unsupported compressed texture format in .setTextureCube()"):Wt?gt&&e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,Ce,0,0,Ve.width,Ve.height,St,vt,Ve.data):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,Ce,_t,Ve.width,Ve.height,0,St,vt,Ve.data)}}}else{if(le=y.mipmaps,Wt&&de){le.length>0&&Xt++;let Lt=Dt(nt[0]);e.texStorage2D(i.TEXTURE_CUBE_MAP,Xt,_t,Lt.width,Lt.height)}for(let Lt=0;Lt<6;Lt++)if(L){Wt?gt&&e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,0,0,0,nt[Lt].width,nt[Lt].height,St,vt,nt[Lt].data):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,0,_t,nt[Lt].width,nt[Lt].height,0,St,vt,nt[Lt].data);for(let Ce=0;Ce<le.length;Ce++){let Ke=le[Ce].image[Lt].image;Wt?gt&&e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,Ce+1,0,0,Ke.width,Ke.height,St,vt,Ke.data):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,Ce+1,_t,Ke.width,Ke.height,0,St,vt,Ke.data)}}else{Wt?gt&&e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,0,0,0,St,vt,nt[Lt]):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,0,_t,St,vt,nt[Lt]);for(let Ce=0;Ce<le.length;Ce++){let Ve=le[Ce];Wt?gt&&e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,Ce+1,0,0,St,vt,Ve.image[Lt]):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,Ce+1,_t,St,vt,Ve.image[Lt])}}}P(y)&&y.mipmapsAutoUpdate===!0&&T(i.TEXTURE_CUBE_MAP),wt.__version=ct.version,y.onUpdate&&y.onUpdate(y)}w.__version=y.version}function ke(w,y,W,mt,ct,wt){let Ct=r.convert(W.format,W.colorSpace),rt=r.convert(W.type),st=A(W.internalFormat,Ct,rt,W.normalized,W.colorSpace),bt=n.get(y),L=n.get(W);if(L.__renderTarget=y,!bt.__hasExternalTextures){let nt=Math.max(1,y.width>>wt),Q=Math.max(1,y.height>>wt);ct===i.TEXTURE_3D||ct===i.TEXTURE_2D_ARRAY?e.texImage3D(ct,wt,st,nt,Q,y.depth,0,Ct,rt,null):e.texImage2D(ct,wt,st,nt,Q,0,Ct,rt,null)}e.bindFramebuffer(i.FRAMEBUFFER,w),Rt(y)?o.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,mt,ct,L.__webglTexture,0,ze(y)):(ct===i.TEXTURE_2D||ct>=i.TEXTURE_CUBE_MAP_POSITIVE_X&&ct<=i.TEXTURE_CUBE_MAP_NEGATIVE_Z)&&i.framebufferTexture2D(i.FRAMEBUFFER,mt,ct,L.__webglTexture,wt),e.bindFramebuffer(i.FRAMEBUFFER,null)}function Kn(w,y,W){if(i.bindRenderbuffer(i.RENDERBUFFER,w),y.depthBuffer){let mt=y.depthTexture,ct=mt&&mt.isDepthTexture?mt.type:null,wt=_(y.stencilBuffer,ct),Ct=y.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT;Rt(y)?o.renderbufferStorageMultisampleEXT(i.RENDERBUFFER,ze(y),wt,y.width,y.height):W?i.renderbufferStorageMultisample(i.RENDERBUFFER,ze(y),wt,y.width,y.height):i.renderbufferStorage(i.RENDERBUFFER,wt,y.width,y.height),i.framebufferRenderbuffer(i.FRAMEBUFFER,Ct,i.RENDERBUFFER,w)}else{let mt=y.textures;for(let ct=0;ct<mt.length;ct++){let wt=mt[ct],Ct=r.convert(wt.format,wt.colorSpace),rt=r.convert(wt.type),st=A(wt.internalFormat,Ct,rt,wt.normalized,wt.colorSpace);Rt(y)?o.renderbufferStorageMultisampleEXT(i.RENDERBUFFER,ze(y),st,y.width,y.height):W?i.renderbufferStorageMultisample(i.RENDERBUFFER,ze(y),st,y.width,y.height):i.renderbufferStorage(i.RENDERBUFFER,st,y.width,y.height)}}i.bindRenderbuffer(i.RENDERBUFFER,null)}function on(w,y,W){let mt=y.isWebGLCubeRenderTarget===!0;if(e.bindFramebuffer(i.FRAMEBUFFER,w),!(y.depthTexture&&y.depthTexture.isDepthTexture))throw new Error("THREE.WebGLTextures: renderTarget.depthTexture must be an instance of THREE.DepthTexture.");let ct=n.get(y.depthTexture);ct.__renderTarget=y;let wt=mt?y.depthTexture.image[0]:y.depthTexture.image;(!ct.__webglTexture||wt.width!==y.width||wt.height!==y.height)&&(wt.width=y.width,wt.height=y.height,y.depthTexture.needsUpdate=!0),mt?pt(y.depthTexture,0):It(y.depthTexture,0);let Ct=ct.__webglTexture,rt=ze(y),st=mt?i.TEXTURE_CUBE_MAP_POSITIVE_X+W:i.TEXTURE_2D,bt=y.depthTexture.format===Yi?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT;if(y.depthTexture.format===zi)Rt(y)?o.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,bt,st,Ct,0,rt):i.framebufferTexture2D(i.FRAMEBUFFER,bt,st,Ct,0);else if(y.depthTexture.format===Yi)Rt(y)?o.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,bt,st,Ct,0,rt):i.framebufferTexture2D(i.FRAMEBUFFER,bt,st,Ct,0);else throw new Error("THREE.WebGLTextures: Unknown depthTexture format.")}function Un(w){let y=n.get(w),W=w.isWebGLCubeRenderTarget===!0;if(y.__boundDepthTexture!==w.depthTexture){let mt=w.depthTexture;if(y.__depthDisposeCallback&&y.__depthDisposeCallback(),mt){let ct=()=>{delete y.__boundDepthTexture,delete y.__depthDisposeCallback,mt.removeEventListener("dispose",ct)};mt.addEventListener("dispose",ct),y.__depthDisposeCallback=ct}y.__boundDepthTexture=mt}if(w.depthTexture&&!y.__autoAllocateDepthBuffer)if(W)for(let mt=0;mt<6;mt++)on(y.__webglFramebuffer[mt],w,mt);else w.texture.mipmaps.length>0?on(y.__webglFramebuffer[0],w,0):on(y.__webglFramebuffer,w,0);else if(W){y.__webglDepthbuffer=[];for(let mt=0;mt<6;mt++)if(e.bindFramebuffer(i.FRAMEBUFFER,y.__webglFramebuffer[mt]),y.__webglDepthbuffer[mt]===void 0)y.__webglDepthbuffer[mt]=i.createRenderbuffer(),Kn(y.__webglDepthbuffer[mt],w,!1);else{let ct=w.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT,wt=y.__webglDepthbuffer[mt];i.bindRenderbuffer(i.RENDERBUFFER,wt),i.framebufferRenderbuffer(i.FRAMEBUFFER,ct,i.RENDERBUFFER,wt)}}else if(w.texture.mipmaps.length>0?e.bindFramebuffer(i.FRAMEBUFFER,y.__webglFramebuffer[0]):e.bindFramebuffer(i.FRAMEBUFFER,y.__webglFramebuffer),y.__webglDepthbuffer===void 0)y.__webglDepthbuffer=i.createRenderbuffer(),Kn(y.__webglDepthbuffer,w,!1);else{let ct=w.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT,wt=y.__webglDepthbuffer;i.bindRenderbuffer(i.RENDERBUFFER,wt),i.framebufferRenderbuffer(i.FRAMEBUFFER,ct,i.RENDERBUFFER,wt)}e.bindFramebuffer(i.FRAMEBUFFER,null)}function pe(w,y,W){let mt=n.get(w);y!==void 0&&ke(mt.__webglFramebuffer,w,w.texture,i.COLOR_ATTACHMENT0,i.TEXTURE_2D,0),W!==void 0&&Un(w)}function Zt(w){let y=w.texture,W=n.get(w),mt=n.get(y);w.addEventListener("dispose",H),G(w);let ct=w.textures,wt=w.isWebGLCubeRenderTarget===!0,Ct=ct.length>1;if(Ct||(mt.__webglTexture===void 0&&(mt.__webglTexture=i.createTexture()),mt.__version=y.version,a.memory.textures++),wt){W.__webglFramebuffer=[];for(let rt=0;rt<6;rt++)if(y.mipmaps.length>0){W.__webglFramebuffer[rt]=[];for(let st=0;st<y.mipmaps.length;st++)W.__webglFramebuffer[rt][st]=i.createFramebuffer()}else W.__webglFramebuffer[rt]=i.createFramebuffer()}else{if(y.mipmaps.length>0){W.__webglFramebuffer=[];for(let rt=0;rt<y.mipmaps.length;rt++)W.__webglFramebuffer[rt]=i.createFramebuffer()}else W.__webglFramebuffer=i.createFramebuffer();if(Ct)for(let rt=0,st=ct.length;rt<st;rt++){let bt=n.get(ct[rt]);bt.__webglTexture===void 0&&(bt.__webglTexture=i.createTexture(),a.memory.textures++)}if(w.samples>0&&Rt(w)===!1){W.__webglMultisampledFramebuffer=i.createFramebuffer(),W.__webglColorRenderbuffer=[],e.bindFramebuffer(i.FRAMEBUFFER,W.__webglMultisampledFramebuffer);for(let rt=0;rt<ct.length;rt++){let st=ct[rt];W.__webglColorRenderbuffer[rt]=i.createRenderbuffer(),i.bindRenderbuffer(i.RENDERBUFFER,W.__webglColorRenderbuffer[rt]);let bt=r.convert(st.format,st.colorSpace),L=r.convert(st.type),nt=A(st.internalFormat,bt,L,st.normalized,st.colorSpace,w.isXRRenderTarget===!0),Q=ze(w);i.renderbufferStorageMultisample(i.RENDERBUFFER,Q,nt,w.width,w.height),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+rt,i.RENDERBUFFER,W.__webglColorRenderbuffer[rt])}i.bindRenderbuffer(i.RENDERBUFFER,null),w.depthBuffer&&(W.__webglDepthRenderbuffer=i.createRenderbuffer(),Kn(W.__webglDepthRenderbuffer,w,!0)),e.bindFramebuffer(i.FRAMEBUFFER,null)}}if(wt){e.bindTexture(i.TEXTURE_CUBE_MAP,mt.__webglTexture),Se(i.TEXTURE_CUBE_MAP,y);for(let rt=0;rt<6;rt++)if(y.mipmaps.length>0)for(let st=0;st<y.mipmaps.length;st++)ke(W.__webglFramebuffer[rt][st],w,y,i.COLOR_ATTACHMENT0,i.TEXTURE_CUBE_MAP_POSITIVE_X+rt,st);else ke(W.__webglFramebuffer[rt],w,y,i.COLOR_ATTACHMENT0,i.TEXTURE_CUBE_MAP_POSITIVE_X+rt,0);P(y)?T(i.TEXTURE_CUBE_MAP):y.mipmaps.length>0&&i.texParameteri(i.TEXTURE_CUBE_MAP,i.TEXTURE_MAX_LEVEL,y.mipmaps.length-1),e.unbindTexture()}else if(Ct){for(let rt=0,st=ct.length;rt<st;rt++){let bt=ct[rt],L=n.get(bt),nt=i.TEXTURE_2D;(w.isWebGL3DRenderTarget||w.isWebGLArrayRenderTarget)&&(nt=w.isWebGL3DRenderTarget?i.TEXTURE_3D:i.TEXTURE_2D_ARRAY),e.bindTexture(nt,L.__webglTexture),Se(nt,bt),ke(W.__webglFramebuffer,w,bt,i.COLOR_ATTACHMENT0+rt,nt,0),P(bt)&&T(nt)}e.unbindTexture()}else{let rt=i.TEXTURE_2D;if((w.isWebGL3DRenderTarget||w.isWebGLArrayRenderTarget)&&(rt=w.isWebGL3DRenderTarget?i.TEXTURE_3D:i.TEXTURE_2D_ARRAY),e.bindTexture(rt,mt.__webglTexture),Se(rt,y),y.mipmaps.length>0)for(let st=0;st<y.mipmaps.length;st++)ke(W.__webglFramebuffer[st],w,y,i.COLOR_ATTACHMENT0,rt,st);else ke(W.__webglFramebuffer,w,y,i.COLOR_ATTACHMENT0,rt,0);P(y)?T(rt):y.mipmaps.length>0&&i.texParameteri(rt,i.TEXTURE_MAX_LEVEL,y.mipmaps.length-1),e.unbindTexture()}w.depthBuffer&&Un(w)}function N(w){let y=w.textures;for(let W=0,mt=y.length;W<mt;W++){let ct=y[W];if(P(ct)&&ct.mipmapsAutoUpdate===!0){let wt=C(w),Ct=n.get(ct).__webglTexture;e.bindTexture(wt,Ct),T(wt),e.unbindTexture()}}}let me=[];function we(w){if(w.samples>0){if(Rt(w)===!1){let y=w.textures,W=w.width,mt=w.height,ct=i.COLOR_BUFFER_BIT,wt=w.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT,Ct=n.get(w),rt=y.length>1;if(rt)for(let bt=0;bt<y.length;bt++)e.bindFramebuffer(i.FRAMEBUFFER,Ct.__webglMultisampledFramebuffer),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+bt,i.RENDERBUFFER,null),e.bindFramebuffer(i.FRAMEBUFFER,Ct.__webglFramebuffer),i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0+bt,i.TEXTURE_2D,null,0);e.bindFramebuffer(i.READ_FRAMEBUFFER,Ct.__webglMultisampledFramebuffer),w.texture.mipmaps.length>0?e.bindFramebuffer(i.DRAW_FRAMEBUFFER,Ct.__webglFramebuffer[0]):e.bindFramebuffer(i.DRAW_FRAMEBUFFER,Ct.__webglFramebuffer);for(let bt=0;bt<y.length;bt++){if(w.resolveDepthBuffer&&(w.depthBuffer&&(ct|=i.DEPTH_BUFFER_BIT),w.stencilBuffer&&w.resolveStencilBuffer&&(ct|=i.STENCIL_BUFFER_BIT)),rt){i.framebufferRenderbuffer(i.READ_FRAMEBUFFER,i.COLOR_ATTACHMENT0,i.RENDERBUFFER,Ct.__webglColorRenderbuffer[bt]);let L=n.get(y[bt]).__webglTexture;i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0,i.TEXTURE_2D,L,0)}i.blitFramebuffer(0,0,W,mt,0,0,W,mt,ct,i.NEAREST),l===!0&&(me.length=0,me.push(i.COLOR_ATTACHMENT0+bt),w.depthBuffer&&w.storeMultisampledDepthBuffer===!1&&me.push(wt),i.invalidateFramebuffer(i.READ_FRAMEBUFFER,me))}if(e.bindFramebuffer(i.READ_FRAMEBUFFER,null),e.bindFramebuffer(i.DRAW_FRAMEBUFFER,null),rt)for(let bt=0;bt<y.length;bt++){e.bindFramebuffer(i.FRAMEBUFFER,Ct.__webglMultisampledFramebuffer),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+bt,i.RENDERBUFFER,Ct.__webglColorRenderbuffer[bt]);let L=n.get(y[bt]).__webglTexture;e.bindFramebuffer(i.FRAMEBUFFER,Ct.__webglFramebuffer),i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0+bt,i.TEXTURE_2D,L,0)}e.bindFramebuffer(i.DRAW_FRAMEBUFFER,Ct.__webglMultisampledFramebuffer)}else if(w.depthBuffer&&w.storeMultisampledDepthBuffer===!1&&l){let y=w.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT;i.invalidateFramebuffer(i.DRAW_FRAMEBUFFER,[y])}}}function ze(w){return Math.min(s.maxSamples,w.samples)}function Rt(w){let y=n.get(w);return w.samples>0&&t.has("WEBGL_multisampled_render_to_texture")===!0&&y.__useRenderToTexture!==!1}function en(w){let y=a.render.frame;h.get(w)!==y&&(h.set(w,y),w.update())}function Pt(w,y){let W=w.colorSpace,mt=w.format,ct=w.type;return w.isCompressedTexture===!0||w.isVideoTexture===!0||W!==Xr&&W!==Zi&&(be.getTransfer(W)===De?(mt!==yi||ct!==Hn)&&Kt("WebGLTextures: sRGB encoded textures have to use RGBAFormat and UnsignedByteType."):ie("WebGLTextures: Unsupported texture color space:",W)),y}function Dt(w){return typeof HTMLImageElement<"u"&&w instanceof HTMLImageElement?(c.width=w.naturalWidth||w.width,c.height=w.naturalHeight||w.height):typeof VideoFrame<"u"&&w instanceof VideoFrame?(c.width=w.displayWidth,c.height=w.displayHeight):(c.width=w.width,c.height=w.height),c}this.allocateTextureUnit=ee,this.resetTextureUnits=it,this.getTextureUnits=ft,this.setTextureUnits=Gt,this.setTexture2D=It,this.setTexture2DArray=Ft,this.setTexture3D=qt,this.setTextureCube=pt,this.rebindTextures=pe,this.setupRenderTarget=Zt,this.updateRenderTargetMipmap=N,this.updateMultisampleRenderTarget=we,this.setupDepthRenderbuffer=Un,this.setupFrameBufferTexture=ke,this.useMultisampledRTT=Rt,this.dispose=Y}function nx(i,t){function e(n,s=Zi){let r,a=be.getTransfer(s);if(n===Hn)return i.UNSIGNED_BYTE;if(n===$o)return i.UNSIGNED_SHORT_4_4_4_4;if(n===jo)return i.UNSIGNED_SHORT_5_5_5_1;if(n===$c)return i.UNSIGNED_INT_5_9_9_9_REV;if(n===jc)return i.UNSIGNED_INT_10F_11F_11F_REV;if(n===Jc)return i.BYTE;if(n===Kc)return i.SHORT;if(n===yr)return i.UNSIGNED_SHORT;if(n===Ko)return i.INT;if(n===gi)return i.UNSIGNED_INT;if(n===_i)return i.FLOAT;if(n===xi)return i.HALF_FLOAT;if(n===Qc)return i.ALPHA;if(n===th)return i.RGB;if(n===yi)return i.RGBA;if(n===zi)return i.DEPTH_COMPONENT;if(n===Yi)return i.DEPTH_STENCIL;if(n===eh)return i.RED;if(n===Qo)return i.RED_INTEGER;if(n===xs)return i.RG;if(n===tl)return i.RG_INTEGER;if(n===el)return i.RGBA_INTEGER;if(n===ua||n===da||n===fa||n===pa)if(a===De)if(r=t.get("WEBGL_compressed_texture_s3tc_srgb"),r!==null){if(n===ua)return r.COMPRESSED_SRGB_S3TC_DXT1_EXT;if(n===da)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT;if(n===fa)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT;if(n===pa)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT}else return null;else if(r=t.get("WEBGL_compressed_texture_s3tc"),r!==null){if(n===ua)return r.COMPRESSED_RGB_S3TC_DXT1_EXT;if(n===da)return r.COMPRESSED_RGBA_S3TC_DXT1_EXT;if(n===fa)return r.COMPRESSED_RGBA_S3TC_DXT3_EXT;if(n===pa)return r.COMPRESSED_RGBA_S3TC_DXT5_EXT}else return null;if(n===nl||n===il||n===sl||n===rl)if(r=t.get("WEBGL_compressed_texture_pvrtc"),r!==null){if(n===nl)return r.COMPRESSED_RGB_PVRTC_4BPPV1_IMG;if(n===il)return r.COMPRESSED_RGB_PVRTC_2BPPV1_IMG;if(n===sl)return r.COMPRESSED_RGBA_PVRTC_4BPPV1_IMG;if(n===rl)return r.COMPRESSED_RGBA_PVRTC_2BPPV1_IMG}else return null;if(n===al||n===ol||n===ll||n===cl||n===hl||n===ma||n===ul)if(r=t.get("WEBGL_compressed_texture_etc"),r!==null){if(n===al||n===ol)return a===De?r.COMPRESSED_SRGB8_ETC2:r.COMPRESSED_RGB8_ETC2;if(n===ll)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ETC2_EAC:r.COMPRESSED_RGBA8_ETC2_EAC;if(n===cl)return r.COMPRESSED_R11_EAC;if(n===hl)return r.COMPRESSED_SIGNED_R11_EAC;if(n===ma)return r.COMPRESSED_RG11_EAC;if(n===ul)return r.COMPRESSED_SIGNED_RG11_EAC}else return null;if(n===dl||n===fl||n===pl||n===ml||n===gl||n===_l||n===xl||n===yl||n===vl||n===Ml||n===Sl||n===bl||n===El||n===Tl)if(r=t.get("WEBGL_compressed_texture_astc"),r!==null){if(n===dl)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR:r.COMPRESSED_RGBA_ASTC_4x4_KHR;if(n===fl)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR:r.COMPRESSED_RGBA_ASTC_5x4_KHR;if(n===pl)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR:r.COMPRESSED_RGBA_ASTC_5x5_KHR;if(n===ml)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR:r.COMPRESSED_RGBA_ASTC_6x5_KHR;if(n===gl)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR:r.COMPRESSED_RGBA_ASTC_6x6_KHR;if(n===_l)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR:r.COMPRESSED_RGBA_ASTC_8x5_KHR;if(n===xl)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR:r.COMPRESSED_RGBA_ASTC_8x6_KHR;if(n===yl)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR:r.COMPRESSED_RGBA_ASTC_8x8_KHR;if(n===vl)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR:r.COMPRESSED_RGBA_ASTC_10x5_KHR;if(n===Ml)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR:r.COMPRESSED_RGBA_ASTC_10x6_KHR;if(n===Sl)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR:r.COMPRESSED_RGBA_ASTC_10x8_KHR;if(n===bl)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR:r.COMPRESSED_RGBA_ASTC_10x10_KHR;if(n===El)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR:r.COMPRESSED_RGBA_ASTC_12x10_KHR;if(n===Tl)return a===De?r.COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR:r.COMPRESSED_RGBA_ASTC_12x12_KHR}else return null;if(n===wl||n===Al||n===Rl)if(r=t.get("EXT_texture_compression_bptc"),r!==null){if(n===wl)return a===De?r.COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT:r.COMPRESSED_RGBA_BPTC_UNORM_EXT;if(n===Al)return r.COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT;if(n===Rl)return r.COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT}else return null;if(n===Cl||n===Pl||n===ga||n===Il)if(r=t.get("EXT_texture_compression_rgtc"),r!==null){if(n===Cl)return r.COMPRESSED_RED_RGTC1_EXT;if(n===Pl)return r.COMPRESSED_SIGNED_RED_RGTC1_EXT;if(n===ga)return r.COMPRESSED_RED_GREEN_RGTC2_EXT;if(n===Il)return r.COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT}else return null;return n===Ns?i.UNSIGNED_INT_24_8:i[n]!==void 0?i[n]:null}return{convert:e}}var ix=`
void main() {

	gl_Position = vec4( position, 1.0 );

}`,sx=`
uniform sampler2DArray depthColor;
uniform float depthWidth;
uniform float depthHeight;

void main() {

	vec2 coord = vec2( gl_FragCoord.x / depthWidth, gl_FragCoord.y / depthHeight );

	if ( coord.x >= 1.0 ) {

		gl_FragDepth = texture( depthColor, vec3( coord.x - 1.0, coord.y, 1 ) ).r;

	} else {

		gl_FragDepth = texture( depthColor, vec3( coord.x, coord.y, 0 ) ).r;

	}

}`,Eh=class{constructor(){this.texture=null,this.mesh=null,this.depthNear=0,this.depthFar=0}init(t,e){if(this.texture===null){let n=new ta(t.texture);(t.depthNear!==e.depthNear||t.depthFar!==e.depthFar)&&(this.depthNear=t.depthNear,this.depthFar=t.depthFar),this.texture=n}}getMesh(t){if(this.texture!==null&&this.mesh===null){let e=t.cameras[0].viewport,n=new ai({vertexShader:ix,fragmentShader:sx,uniforms:{depthColor:{value:this.texture},depthWidth:{value:e.z},depthHeight:{value:e.w}}});this.mesh=new Qt(new Wi(20,20),n)}return this.mesh}reset(){this.texture=null,this.mesh=null}getDepthTexture(){return this.texture}},Th=class extends pi{constructor(t,e){super();let n=this,s=null,r=1,a=null,o="local-floor",l=1,c=null,h=null,f=null,d=null,p=null,x=null,S=typeof XRWebGLBinding<"u",m=new Eh,g={},E=e.getContextAttributes(),P=null,T=null,C=[],A=[],_=new kt,b=null,G=null,B=new In;B.viewport=new je;let k=new In;k.viewport=new je;let H=[B,k],K=new Wo,U=null,Y=null;this.cameraAutoUpdate=!0,this.enabled=!1,this.isPresenting=!1,this.getController=function(at){let It=C[at];return It===void 0&&(It=new cr,C[at]=It),It.getTargetRaySpace()},this.getControllerGrip=function(at){let It=C[at];return It===void 0&&(It=new cr,C[at]=It),It.getGripSpace()},this.getHand=function(at){let It=C[at];return It===void 0&&(It=new cr,C[at]=It),It.getHandSpace()};function tt(at){let It=A.indexOf(at.inputSource);if(It===-1)return;let Ft=C[It];Ft!==void 0&&(Ft.update(at.inputSource,at.frame,c||a),Ft.dispatchEvent({type:at.type,data:at.inputSource}))}function j(){s.removeEventListener("select",tt),s.removeEventListener("selectstart",tt),s.removeEventListener("selectend",tt),s.removeEventListener("squeeze",tt),s.removeEventListener("squeezestart",tt),s.removeEventListener("squeezeend",tt),s.removeEventListener("end",j),s.removeEventListener("inputsourceschange",dt);for(let at=0;at<C.length;at++){let It=A[at];It!==null&&(A[at]=null,C[at].disconnect(It))}U=null,Y=null,m.reset();for(let at in g)delete g[at];if(t.setRenderTarget(P),p=null,d=null,f=null,s=null,T=null,ee.stop(),n.isPresenting=!1,t.setPixelRatio(b),t.setSize(_.width,_.height,!1),G!==null){let at=G.camera;at.fov=G.fov,at.zoom=G.zoom,at.updateProjectionMatrix(),G=null}n.dispatchEvent({type:"sessionend"})}this.setFramebufferScaleFactor=function(at){r=at,n.isPresenting===!0&&Kt("WebXRManager: Cannot change framebuffer scale while presenting.")},this.setReferenceSpaceType=function(at){o=at,n.isPresenting===!0&&Kt("WebXRManager: Cannot change reference space type while presenting.")},this.getReferenceSpace=function(){return c||a},this.setReferenceSpace=function(at){c=at},this.getBaseLayer=function(){return d!==null?d:p},this.getBinding=function(){return f===null&&S&&(f=new XRWebGLBinding(s,e)),f},this.getFrame=function(){return x},this.getSession=function(){return s},this.setSession=async function(at){if(s=at,s!==null){if(P=t.getRenderTarget(),s.addEventListener("select",tt),s.addEventListener("selectstart",tt),s.addEventListener("selectend",tt),s.addEventListener("squeeze",tt),s.addEventListener("squeezestart",tt),s.addEventListener("squeezeend",tt),s.addEventListener("end",j),s.addEventListener("inputsourceschange",dt),E.xrCompatible!==!0&&await e.makeXRCompatible(),b=t.getPixelRatio(),t.getSize(_),S&&"createProjectionLayer"in XRWebGLBinding.prototype){let Ft=null,qt=null,pt=null;E.depth&&(pt=E.stencil?e.DEPTH24_STENCIL8:e.DEPTH_COMPONENT24,Ft=E.stencil?Yi:zi,qt=E.stencil?Ns:gi);let oe={colorFormat:e.RGBA8,depthFormat:pt,scaleFactor:r};f=this.getBinding(),d=f.createProjectionLayer(oe),s.updateRenderState({layers:[d]}),t.setPixelRatio(1),t.setSize(d.textureWidth,d.textureHeight,!1),T=new Zn(d.textureWidth,d.textureHeight,{format:yi,type:Hn,depthTexture:new Vi(d.textureWidth,d.textureHeight,qt,void 0,void 0,void 0,void 0,void 0,void 0,Ft),stencilBuffer:E.stencil,colorSpace:t.outputColorSpace,samples:E.antialias?4:0,resolveDepthBuffer:d.ignoreDepthValues===!1,resolveStencilBuffer:d.ignoreDepthValues===!1,storeMultisampledDepthBuffer:d.ignoreDepthValues===!1,storeMultisampledStencilBuffer:d.ignoreDepthValues===!1})}else{let Ft={antialias:E.antialias,alpha:!0,depth:E.depth,stencil:E.stencil,framebufferScaleFactor:r};p=new XRWebGLLayer(s,e,Ft),s.updateRenderState({baseLayer:p}),t.setPixelRatio(1),t.setSize(p.framebufferWidth,p.framebufferHeight,!1),T=new Zn(p.framebufferWidth,p.framebufferHeight,{format:yi,type:Hn,colorSpace:t.outputColorSpace,stencilBuffer:E.stencil,resolveDepthBuffer:p.ignoreDepthValues===!1,resolveStencilBuffer:p.ignoreDepthValues===!1,storeMultisampledDepthBuffer:p.ignoreDepthValues===!1,storeMultisampledStencilBuffer:p.ignoreDepthValues===!1})}T.isXRRenderTarget=!0,this.setFoveation(l),c=null,a=await s.requestReferenceSpace(o),ee.setContext(s),ee.start(),n.isPresenting=!0,n.dispatchEvent({type:"sessionstart"})}},this.getEnvironmentBlendMode=function(){if(s!==null)return s.environmentBlendMode},this.getDepthTexture=function(){return m.getDepthTexture()};function dt(at){for(let It=0;It<at.removed.length;It++){let Ft=at.removed[It],qt=A.indexOf(Ft);qt>=0&&(A[qt]=null,C[qt].disconnect(Ft))}for(let It=0;It<at.added.length;It++){let Ft=at.added[It],qt=A.indexOf(Ft);if(qt===-1){for(let oe=0;oe<C.length;oe++)if(oe>=A.length){A.push(Ft),qt=oe;break}else if(A[oe]===null){A[oe]=Ft,qt=oe;break}if(qt===-1)break}let pt=C[qt];pt&&pt.connect(Ft)}}function V(at,It){It===null?at.matrixWorld.copy(at.matrix):at.matrixWorld.multiplyMatrices(It.matrixWorld,at.matrix),at.matrixWorldInverse.copy(at.matrixWorld).invert()}this.updateCamera=function(at){if(s===null)return;let It=at.near,Ft=at.far;m.texture!==null&&(m.depthNear>0&&(It=m.depthNear),m.depthFar>0&&(Ft=m.depthFar)),K.near=k.near=B.near=It,K.far=k.far=B.far=Ft,(U!==K.near||Y!==K.far)&&(s.updateRenderState({depthNear:K.near,depthFar:K.far}),U=K.near,Y=K.far),K.layers.mask=at.layers.mask|6,B.layers.mask=K.layers.mask&-5,k.layers.mask=K.layers.mask&-3;let qt=at.parent,pt=K.cameras;V(K,qt);for(let oe=0;oe<pt.length;oe++)V(pt[oe],qt);K.projectionMatrix.copy(B.projectionMatrix),K.projectionMatrixInverse.copy(B.projectionMatrixInverse),G===null&&at.isPerspectiveCamera&&(G={camera:at,fov:at.fov,zoom:at.zoom}),it(at,K,qt)};function it(at,It,Ft){Ft===null?at.matrix.copy(It.matrixWorld):(at.matrix.copy(Ft.matrixWorld),at.matrix.invert(),at.matrix.multiply(It.matrixWorld)),at.matrix.decompose(at.position,at.quaternion,at.scale),at.updateMatrixWorld(!0),at.projectionMatrix.copy(It.projectionMatrix),at.projectionMatrixInverse.copy(It.projectionMatrixInverse),at.isPerspectiveCamera&&(at.fov=ar*2*Math.atan(1/at.projectionMatrix.elements[5]),at.zoom=1)}this.getCamera=function(){return K},this.getFoveation=function(){if(!(d===null&&p===null))return l},this.setFoveation=function(at){l=at,d!==null&&(d.fixedFoveation=at),p!==null&&p.fixedFoveation!==void 0&&(p.fixedFoveation=at)},this.hasDepthSensing=function(){return m.texture!==null},this.getDepthSensingMesh=function(){return m.getMesh(K)},this.getCameraTexture=function(at){return g[at]};let ft=null;function Gt(at,It){if(h=It.getViewerPose(c||a),x=It,h!==null){let Ft=h.views;p!==null&&(t.setRenderTargetFramebuffer(T,p.framebuffer),t.setRenderTarget(T));let qt=!1;Ft.length!==K.cameras.length&&(K.cameras.length=0,qt=!0);for(let zt=0;zt<Ft.length;zt++){let Se=Ft[zt],ye=null;if(p!==null)ye=p.getViewport(Se);else{let Je=f.getViewSubImage(d,Se);ye=Je.viewport,zt===0&&(t.setRenderTargetTextures(T,Je.colorTexture,Je.depthStencilTexture),t.setRenderTarget(T))}let he=H[zt];he===void 0&&(he=new In,he.layers.enable(zt),he.viewport=new je,H[zt]=he),he.matrix.fromArray(Se.transform.matrix),he.matrix.decompose(he.position,he.quaternion,he.scale),he.projectionMatrix.fromArray(Se.projectionMatrix),he.projectionMatrixInverse.copy(he.projectionMatrix).invert(),he.viewport.set(ye.x,ye.y,ye.width,ye.height),zt===0&&(K.matrix.copy(he.matrix),K.matrix.decompose(K.position,K.quaternion,K.scale)),qt===!0&&K.cameras.push(he)}let pt=s.enabledFeatures;if(pt&&pt.includes("depth-sensing")&&s.depthUsage=="gpu-optimized"&&S){f=n.getBinding();let zt=f.getDepthInformation(Ft[0]);zt&&zt.isValid&&zt.texture&&m.init(zt,s.renderState)}if(pt&&pt.includes("camera-access")&&S){t.state.unbindTexture(),f=n.getBinding();for(let zt=0;zt<Ft.length;zt++){let Se=Ft[zt].camera;if(Se){let ye=g[Se];ye||(ye=new ta,g[Se]=ye);let he=f.getCameraImage(Se);ye.sourceTexture=he}}}}for(let Ft=0;Ft<C.length;Ft++){let qt=A[Ft],pt=C[Ft];qt!==null&&pt!==void 0&&pt.update(qt,It,c||a)}ft&&ft(at,It),It.detectedPlanes&&n.dispatchEvent({type:"planesdetected",data:It}),x=null}let ee=new Od;ee.setAnimationLoop(Gt),this.setAnimationLoop=function(at){ft=at},this.dispose=function(){}}},rx=new Ge,Yd=new ae;Yd.set(-1,0,0,0,1,0,0,0,1);function ax(i,t){function e(m,g){m.matrixAutoUpdate===!0&&m.updateMatrix(),g.value.copy(m.matrix)}function n(m,g){g.color.getRGB(m.fogColor.value,dh(i)),g.isFog?(m.fogNear.value=g.near,m.fogFar.value=g.far):g.isFogExp2&&(m.fogDensity.value=g.density)}function s(m,g,E,P,T){g.isNodeMaterial?g.uniformsNeedUpdate=!1:g.isMeshBasicMaterial?r(m,g):g.isMeshLambertMaterial?(r(m,g),g.envMap&&(m.envMapIntensity.value=g.envMapIntensity)):g.isMeshToonMaterial?(r(m,g),f(m,g)):g.isMeshPhongMaterial?(r(m,g),h(m,g),g.envMap&&(m.envMapIntensity.value=g.envMapIntensity)):g.isMeshStandardMaterial?(r(m,g),d(m,g),g.isMeshPhysicalMaterial&&p(m,g,T)):g.isMeshMatcapMaterial?(r(m,g),x(m,g)):g.isMeshDepthMaterial?r(m,g):g.isMeshDistanceMaterial?(r(m,g),S(m,g)):g.isMeshNormalMaterial?r(m,g):g.isLineBasicMaterial?(a(m,g),g.isLineDashedMaterial&&o(m,g)):g.isPointsMaterial?l(m,g,E,P):g.isSpriteMaterial?c(m,g):g.isShadowMaterial?(m.color.value.copy(g.color),m.opacity.value=g.opacity):g.isShaderMaterial&&(g.uniformsNeedUpdate=!1)}function r(m,g){m.opacity.value=g.opacity,g.color&&m.diffuse.value.copy(g.color),g.emissive&&m.emissive.value.copy(g.emissive).multiplyScalar(g.emissiveIntensity),g.map&&(m.map.value=g.map,e(g.map,m.mapTransform)),g.alphaMap&&(m.alphaMap.value=g.alphaMap,e(g.alphaMap,m.alphaMapTransform)),g.bumpMap&&(m.bumpMap.value=g.bumpMap,e(g.bumpMap,m.bumpMapTransform),m.bumpScale.value=g.bumpScale,g.side===vn&&(m.bumpScale.value*=-1)),g.normalMap&&(m.normalMap.value=g.normalMap,e(g.normalMap,m.normalMapTransform),m.normalScale.value.copy(g.normalScale),g.side===vn&&m.normalScale.value.negate()),g.displacementMap&&(m.displacementMap.value=g.displacementMap,e(g.displacementMap,m.displacementMapTransform),m.displacementScale.value=g.displacementScale,m.displacementBias.value=g.displacementBias),g.emissiveMap&&(m.emissiveMap.value=g.emissiveMap,e(g.emissiveMap,m.emissiveMapTransform)),g.specularMap&&(m.specularMap.value=g.specularMap,e(g.specularMap,m.specularMapTransform)),g.alphaTest>0&&(m.alphaTest.value=g.alphaTest);let E=t.get(g),P=E.envMap,T=E.envMapRotation;P&&(m.envMap.value=P,m.envMapRotation.value.setFromMatrix4(rx.makeRotationFromEuler(T)).transpose(),P.isCubeTexture&&P.isRenderTargetTexture===!1&&m.envMapRotation.value.premultiply(Yd),m.reflectivity.value=g.reflectivity,m.ior.value=g.ior,m.refractionRatio.value=g.refractionRatio),g.lightMap&&(m.lightMap.value=g.lightMap,m.lightMapIntensity.value=g.lightMapIntensity,e(g.lightMap,m.lightMapTransform)),g.aoMap&&(m.aoMap.value=g.aoMap,m.aoMapIntensity.value=g.aoMapIntensity,e(g.aoMap,m.aoMapTransform))}function a(m,g){m.diffuse.value.copy(g.color),m.opacity.value=g.opacity,g.map&&(m.map.value=g.map,e(g.map,m.mapTransform))}function o(m,g){m.dashSize.value=g.dashSize,m.totalSize.value=g.dashSize+g.gapSize,m.scale.value=g.scale}function l(m,g,E,P){m.diffuse.value.copy(g.color),m.opacity.value=g.opacity,m.size.value=g.size*E,m.scale.value=P*.5,g.map&&(m.map.value=g.map,e(g.map,m.uvTransform)),g.alphaMap&&(m.alphaMap.value=g.alphaMap,e(g.alphaMap,m.alphaMapTransform)),g.alphaTest>0&&(m.alphaTest.value=g.alphaTest)}function c(m,g){m.diffuse.value.copy(g.color),m.opacity.value=g.opacity,m.rotation.value=g.rotation,g.map&&(m.map.value=g.map,e(g.map,m.mapTransform)),g.alphaMap&&(m.alphaMap.value=g.alphaMap,e(g.alphaMap,m.alphaMapTransform)),g.alphaTest>0&&(m.alphaTest.value=g.alphaTest)}function h(m,g){m.specular.value.copy(g.specular),m.shininess.value=Math.max(g.shininess,1e-4)}function f(m,g){g.gradientMap&&(m.gradientMap.value=g.gradientMap)}function d(m,g){m.metalness.value=g.metalness,g.metalnessMap&&(m.metalnessMap.value=g.metalnessMap,e(g.metalnessMap,m.metalnessMapTransform)),m.roughness.value=g.roughness,g.roughnessMap&&(m.roughnessMap.value=g.roughnessMap,e(g.roughnessMap,m.roughnessMapTransform)),g.envMap&&(m.envMapIntensity.value=g.envMapIntensity)}function p(m,g,E){m.ior.value=g.ior,g.diffuseRoughness>0&&(m.diffuseRoughness.value=g.diffuseRoughness,g.diffuseRoughnessMap&&(m.diffuseRoughnessMap.value=g.diffuseRoughnessMap,e(g.diffuseRoughnessMap,m.diffuseRoughnessMapTransform))),g.sheen>0&&(m.sheenColor.value.copy(g.sheenColor).multiplyScalar(g.sheen),m.sheenRoughness.value=g.sheenRoughness,g.sheenColorMap&&(m.sheenColorMap.value=g.sheenColorMap,e(g.sheenColorMap,m.sheenColorMapTransform)),g.sheenRoughnessMap&&(m.sheenRoughnessMap.value=g.sheenRoughnessMap,e(g.sheenRoughnessMap,m.sheenRoughnessMapTransform))),g.clearcoat>0&&(m.clearcoat.value=g.clearcoat,m.clearcoatRoughness.value=g.clearcoatRoughness,g.clearcoatMap&&(m.clearcoatMap.value=g.clearcoatMap,e(g.clearcoatMap,m.clearcoatMapTransform)),g.clearcoatRoughnessMap&&(m.clearcoatRoughnessMap.value=g.clearcoatRoughnessMap,e(g.clearcoatRoughnessMap,m.clearcoatRoughnessMapTransform)),g.clearcoatNormalMap&&(m.clearcoatNormalMap.value=g.clearcoatNormalMap,e(g.clearcoatNormalMap,m.clearcoatNormalMapTransform),m.clearcoatNormalScale.value.copy(g.clearcoatNormalScale),g.side===vn&&m.clearcoatNormalScale.value.negate())),g.dispersion>0&&(m.dispersion.value=g.dispersion),g.retroreflectivity>0&&(m.retroreflectivity.value=g.retroreflectivity),g.iridescence>0&&(m.iridescence.value=g.iridescence,m.iridescenceIOR.value=g.iridescenceIOR,m.iridescenceThicknessMinimum.value=g.iridescenceThicknessMinimum,m.iridescenceThicknessMaximum.value=g.iridescenceThicknessMaximum,g.iridescenceMap&&(m.iridescenceMap.value=g.iridescenceMap,e(g.iridescenceMap,m.iridescenceMapTransform)),g.iridescenceThicknessMap&&(m.iridescenceThicknessMap.value=g.iridescenceThicknessMap,e(g.iridescenceThicknessMap,m.iridescenceThicknessMapTransform))),g.transmission>0&&(m.transmission.value=g.transmission,m.transmissionSamplerMap.value=E.texture,m.transmissionSamplerSize.value.set(E.width,E.height),g.transmissionMap&&(m.transmissionMap.value=g.transmissionMap,e(g.transmissionMap,m.transmissionMapTransform)),m.thickness.value=g.thickness,g.thicknessMap&&(m.thicknessMap.value=g.thicknessMap,e(g.thicknessMap,m.thicknessMapTransform)),m.attenuationDistance.value=g.attenuationDistance,m.attenuationColor.value.copy(g.attenuationColor)),g.anisotropy>0&&(m.anisotropyVector.value.set(g.anisotropy*Math.cos(g.anisotropyRotation),g.anisotropy*Math.sin(g.anisotropyRotation)),g.anisotropyMap&&(m.anisotropyMap.value=g.anisotropyMap,e(g.anisotropyMap,m.anisotropyMapTransform))),m.specularIntensity.value=g.specularIntensity,m.specularColor.value.copy(g.specularColor),g.specularColorMap&&(m.specularColorMap.value=g.specularColorMap,e(g.specularColorMap,m.specularColorMapTransform)),g.specularIntensityMap&&(m.specularIntensityMap.value=g.specularIntensityMap,e(g.specularIntensityMap,m.specularIntensityMapTransform))}function x(m,g){g.matcap&&(m.matcap.value=g.matcap)}function S(m,g){let E=t.get(g).light;m.referencePosition.value.setFromMatrixPosition(E.matrixWorld),m.nearDistance.value=E.shadow.camera.near,m.farDistance.value=E.shadow.camera.far}return{refreshFogUniforms:n,refreshMaterialUniforms:s}}function ox(i,t,e,n){let s={},r={};function a(E,P){let T=P.program;n.uniformBlockBinding(E,T,s[E.id])}function o(E,P){let T=s[E.id];T===void 0&&(x(E),T=l(E),s[E.id]=T,E.addEventListener("dispose",m));let C=P.program;n.updateUBOMapping(E,C);let A=t.render.frame;r[E.id]!==A&&(c(E),r[E.id]=A)}function l(E){let P=i.createBuffer(),T=E.__size,C=E.usage;return i.bindBuffer(i.UNIFORM_BUFFER,P),i.bufferData(i.UNIFORM_BUFFER,T,C),i.bindBuffer(i.UNIFORM_BUFFER,null),P}function c(E){let P=s[E.id],T=E.uniforms,C=E.__cache;i.bindBuffer(i.UNIFORM_BUFFER,P);for(let A=0,_=T.length;A<_;A++){let b=T[A];if(Array.isArray(b))for(let G=0,B=b.length;G<B;G++)h(b[G],A,G,C);else h(b,A,0,C)}i.bindBuffer(i.UNIFORM_BUFFER,null)}function h(E,P,T,C){if(d(E,P,T,C)===!0){let A=E.__offset,_=E.value;if(Array.isArray(_)){let b=0;for(let G=0;G<_.length;G++){let B=_[G],k=S(B,!0);f(B,E.__data,b),b+=k.storage/Float32Array.BYTES_PER_ELEMENT}}else f(_,E.__data,0);i.bufferSubData(i.UNIFORM_BUFFER,A,E.__data)}}function f(E,P,T){typeof E=="number"||typeof E=="boolean"?P[T]=E:E.isMatrix3?(P[T]=E.elements[0],P[T+1]=E.elements[1],P[T+2]=E.elements[2],P[T+3]=0,P[T+4]=E.elements[3],P[T+5]=E.elements[4],P[T+6]=E.elements[5],P[T+7]=0,P[T+8]=E.elements[6],P[T+9]=E.elements[7],P[T+10]=E.elements[8],P[T+11]=0):ArrayBuffer.isView(E)?P.set(E.subarray(0,P.length-T),T):E.toArray(P,T)}function d(E,P,T,C){let A=E.value,_=P+"_"+T;if(Array.isArray(A)){C[_]===void 0&&(C[_]=[]);let b=C[_],G=!1;for(let B=0;B<A.length;B++)p(A[B],b,B)===!0&&(G=!0);return G}return p(A,C,_)}function p(E,P,T){if(P[T]===void 0)return typeof E=="number"||typeof E=="boolean"?P[T]=E:ArrayBuffer.isView(E)?P[T]=E.slice():P[T]=E.clone(),!0;{let C=P[T];if(typeof E=="number"||typeof E=="boolean"){if(C!==E)return P[T]=E,!0}else{if(ArrayBuffer.isView(E))return!0;if(C.equals(E)===!1)return C.copy(E),!0}}return!1}function x(E){let P=E.uniforms,T=0,C=16;for(let _=0,b=P.length;_<b;_++){let G=Array.isArray(P[_])?P[_]:[P[_]];for(let B=0,k=G.length;B<k;B++){let H=G[B],K=Array.isArray(H.value)?H.value:[H.value],U=Array.isArray(P[_])||Array.isArray(H.value),Y=T;for(let j=0,dt=K.length;j<dt;j++){let V=K[j],it=S(V,U),ft=T%C,Gt=ft%it.boundary,ee=ft+Gt;T+=Gt,ee!==0&&C-ee<it.storage&&(T+=C-ee),j===0&&(Y=T),T+=it.storage}let tt=H.type==="int"?Int32Array:H.type==="uint"?Uint32Array:Float32Array;H.__data=new tt((T-Y)/Float32Array.BYTES_PER_ELEMENT),H.__offset=Y}}let A=T%C;return A>0&&(T+=C-A),E.__size=T,E.__cache={},this}function S(E,P){let T={boundary:0,storage:0};return typeof E=="number"||typeof E=="boolean"?(T.boundary=4,T.storage=4):E.isVector2?(T.boundary=8,T.storage=8):E.isVector3||E.isColor?(T.boundary=16,T.storage=12):E.isVector4?(T.boundary=16,T.storage=16):E.isMatrix3?(T.boundary=16,T.storage=48):E.isMatrix4?(T.boundary=16,T.storage=64):E.isTexture?Kt("WebGLRenderer: Texture samplers can not be part of an uniforms group."):ArrayBuffer.isView(E)?(T.boundary=16,T.storage=E.byteLength):Kt("WebGLRenderer: Unsupported uniform value type.",E),P===!0&&(T.boundary=16,T.storage=Math.ceil(T.storage/16)*16),T}function m(E){let P=E.target;P.removeEventListener("dispose",m),i.deleteBuffer(s[P.id]),delete s[P.id],delete r[P.id]}function g(){for(let E in s)i.deleteBuffer(s[E]);s={},r={}}return{bind:a,update:o,dispose:g}}var lx=new Uint16Array([12469,15057,12620,14925,13266,14620,13807,14376,14323,13990,14545,13625,14713,13328,14840,12882,14931,12528,14996,12233,15039,11829,15066,11525,15080,11295,15085,10976,15082,10705,15073,10495,13880,14564,13898,14542,13977,14430,14158,14124,14393,13732,14556,13410,14702,12996,14814,12596,14891,12291,14937,11834,14957,11489,14958,11194,14943,10803,14921,10506,14893,10278,14858,9960,14484,14039,14487,14025,14499,13941,14524,13740,14574,13468,14654,13106,14743,12678,14818,12344,14867,11893,14889,11509,14893,11180,14881,10751,14852,10428,14812,10128,14765,9754,14712,9466,14764,13480,14764,13475,14766,13440,14766,13347,14769,13070,14786,12713,14816,12387,14844,11957,14860,11549,14868,11215,14855,10751,14825,10403,14782,10044,14729,9651,14666,9352,14599,9029,14967,12835,14966,12831,14963,12804,14954,12723,14936,12564,14917,12347,14900,11958,14886,11569,14878,11247,14859,10765,14828,10401,14784,10011,14727,9600,14660,9289,14586,8893,14508,8533,15111,12234,15110,12234,15104,12216,15092,12156,15067,12010,15028,11776,14981,11500,14942,11205,14902,10752,14861,10393,14812,9991,14752,9570,14682,9252,14603,8808,14519,8445,14431,8145,15209,11449,15208,11451,15202,11451,15190,11438,15163,11384,15117,11274,15055,10979,14994,10648,14932,10343,14871,9936,14803,9532,14729,9218,14645,8742,14556,8381,14461,8020,14365,7603,15273,10603,15272,10607,15267,10619,15256,10631,15231,10614,15182,10535,15118,10389,15042,10167,14963,9787,14883,9447,14800,9115,14710,8665,14615,8318,14514,7911,14411,7507,14279,7198,15314,9675,15313,9683,15309,9712,15298,9759,15277,9797,15229,9773,15166,9668,15084,9487,14995,9274,14898,8910,14800,8539,14697,8234,14590,7790,14479,7409,14367,7067,14178,6621,15337,8619,15337,8631,15333,8677,15325,8769,15305,8871,15264,8940,15202,8909,15119,8775,15022,8565,14916,8328,14804,8009,14688,7614,14569,7287,14448,6888,14321,6483,14088,6171,15350,7402,15350,7419,15347,7480,15340,7613,15322,7804,15287,7973,15229,8057,15148,8012,15046,7846,14933,7611,14810,7357,14682,7069,14552,6656,14421,6316,14251,5948,14007,5528,15356,5942,15356,5977,15353,6119,15348,6294,15332,6551,15302,6824,15249,7044,15171,7122,15070,7050,14949,6861,14818,6611,14679,6349,14538,6067,14398,5651,14189,5311,13935,4958,15359,4123,15359,4153,15356,4296,15353,4646,15338,5160,15311,5508,15263,5829,15188,6042,15088,6094,14966,6001,14826,5796,14678,5543,14527,5287,14377,4985,14133,4586,13869,4257,15360,1563,15360,1642,15358,2076,15354,2636,15341,3350,15317,4019,15273,4429,15203,4732,15105,4911,14981,4932,14836,4818,14679,4621,14517,4386,14359,4156,14083,3795,13808,3437,15360,122,15360,137,15358,285,15355,636,15344,1274,15322,2177,15281,2765,15215,3223,15120,3451,14995,3569,14846,3567,14681,3466,14511,3305,14344,3121,14037,2800,13753,2467,15360,0,15360,1,15359,21,15355,89,15346,253,15325,479,15287,796,15225,1148,15133,1492,15008,1749,14856,1882,14685,1886,14506,1783,14324,1608,13996,1398,13702,1183]),Pi=null;function cx(){return Pi===null&&(Pi=new yo(lx,16,16,xs,xi),Pi.name="DFG_LUT",Pi.minFilter=Ln,Pi.magFilter=Ln,Pi.wrapS=Ei,Pi.wrapT=Ei,Pi.generateMipmaps=!1,Pi.needsUpdate=!0),Pi}var Ul=class{constructor(t={}){let{canvas:e=ad(),context:n=null,depth:s=!0,stencil:r=!1,alpha:a=!1,antialias:o=!1,premultipliedAlpha:l=!0,preserveDrawingBuffer:c=!1,powerPreference:h="default",failIfMajorPerformanceCaveat:f=!1,reversedDepthBuffer:d=!1,outputBufferType:p=Hn}=t;this.isWebGLRenderer=!0;let x;if(n!==null){if(typeof WebGLRenderingContext<"u"&&n instanceof WebGLRenderingContext)throw new Error("THREE.WebGLRenderer: WebGL 1 is not supported since r163.");x=n.getContextAttributes().alpha}else x=a;let S=p,m=new Set([el,tl,Qo]),g=new Set([Hn,gi,yr,Ns,$o,jo]),E=new Uint32Array(4),P=new Int32Array(4),T={textures:[],min:[],max:[],resolution:[]},C=null,A=null,_=[],b=[],G=null;this.domElement=e,this.debug={checkShaderErrors:!0,diagnostics:{keywords:!1},onShaderError:null},this.autoClear=!0,this.autoClearColor=!0,this.autoClearDepth=!0,this.autoClearStencil=!0,this.sortObjects=!0,this.clippingPlanes=[],this.localClippingEnabled=!1,this.toneMapping=Ci,this.toneMappingExposure=1,this.transmissionResolutionScale=1;let B=this,k=!1,H=null,K=null,U=null,Y=null;this._outputColorSpace=fn;let tt=0,j=0,dt=null,V=-1,it=null,ft=new je,Gt=new je,ee=null,at=new fe(0),It=0,Ft=e.width,qt=e.height,pt=1,oe=null,$t=null,zt=new je(0,0,Ft,qt),Se=new je(0,0,Ft,qt),ye=!1,he=new us,Je=new vo,Xe=!1,_n=!1,ke=new Ge,Kn=new D,on=new je,Un={background:null,fog:null,environment:null,overrideMaterial:null,isScene:!0},pe=!1;function Zt(){return dt===null?pt:1}let N=n;function me(v,O){return e.getContext(v,O)}let we,ze,Rt,en,Pt,Dt,w,y,W,mt,ct,wt,Ct,rt,st,bt,L,nt,Q,St,vt,_t,Wt;try{let v={alpha:!0,depth:s,stencil:r,antialias:o,premultipliedAlpha:l,preserveDrawingBuffer:c,powerPreference:h,failIfMajorPerformanceCaveat:f};if("setAttribute"in e&&e.setAttribute("data-engine",`three.js r${Xo}`),e.addEventListener("webglcontextlost",Xt,!1),e.addEventListener("webglcontextrestored",le,!1),e.addEventListener("webglcontextcreationerror",Lt,!1),N===null){let O="webgl2";if(N=me(O,v),N===null)throw me(O)?new Error("THREE.WebGLRenderer: Error creating WebGL context with your selected attributes."):new Error("THREE.WebGLRenderer: Error creating WebGL context.")}de()}catch(v){throw e.removeEventListener("webglcontextlost",Xt,!1),e.removeEventListener("webglcontextrestored",le,!1),e.removeEventListener("webglcontextcreationerror",Lt,!1),ie("WebGLRenderer: "+v.message),v}function de(){we=new v0(N),we.init(),vt=new nx(N,we),ze=new c0(N,we,t,vt),Rt=new tx(N,we),ze.reversedDepthBuffer&&d&&Rt.buffers.depth.setReversed(!0),K=N.createFramebuffer(),U=N.createFramebuffer(),Y=N.createFramebuffer(),en=new b0(N),Pt=new z_,Dt=new ex(N,we,Rt,Pt,ze,vt,en),w=new y0(B),y=new Tp(N),_t=new o0(N,y),W=new M0(N,y,en,_t),mt=new T0(N,W,y,_t,en),nt=new E0(N,ze,Dt),st=new h0(Pt),ct=new k_(B,w,we,ze,_t,st),wt=new ax(B,Pt),Ct=new G_,rt=new Z_(we),L=new a0(B,w,Rt,mt,x,l),bt=new Q_(B,mt,ze),Wt=new ox(N,en,ze,Rt),Q=new l0(N,we,en),St=new S0(N,we,en),en.programs=ct.programs,B.capabilities=ze,B.extensions=we,B.properties=Pt,B.renderLists=Ct,B.shadowMap=bt,B.state=Rt,B.info=en}S!==Hn&&(G=new A0(S,e.width,e.height,o,s,r));let gt=new Th(B,N);this.xr=gt,this.getContext=function(){return N},this.getContextAttributes=function(){return N.getContextAttributes()},this.forceContextLoss=function(){let v=we.get("WEBGL_lose_context");v&&v.loseContext()},this.forceContextRestore=function(){let v=we.get("WEBGL_lose_context");v&&v.restoreContext()},this.getPixelRatio=function(){return pt},this.setPixelRatio=function(v){v!==void 0&&(pt=v,this.setSize(Ft,qt,!1))},this.getSize=function(v){return v.set(Ft,qt)},this.setSize=function(v,O,$=!0){if(gt.isPresenting){Kt("WebGLRenderer: Can't change size while VR device is presenting.");return}Ft=v,qt=O,e.width=Math.floor(v*pt),e.height=Math.floor(O*pt),$===!0&&(e.style.width=v+"px",e.style.height=O+"px"),G!==null&&G.setSize(e.width,e.height),this.setViewport(0,0,v,O)},this.getDrawingBufferSize=function(v){return v.set(Ft*pt,qt*pt).floor()},this.setDrawingBufferSize=function(v,O,$){Ft=v,qt=O,pt=$,e.width=Math.floor(v*$),e.height=Math.floor(O*$),this.setViewport(0,0,v,O)},this.setEffects=function(v){if(S===Hn){ie("WebGLRenderer: setEffects() requires outputBufferType set to HalfFloatType or FloatType.");return}if(v){for(let O=0;O<v.length;O++)if(v[O].isOutputPass===!0){Kt("WebGLRenderer: OutputPass is not needed in setEffects(). Tone mapping and color space conversion are applied automatically.");break}}G.setEffects(v||[])},this.getCurrentViewport=function(v){return v.copy(ft)},this.getViewport=function(v){return v.copy(zt)},this.setViewport=function(v,O,$,X){v.isVector4?zt.set(v.x,v.y,v.z,v.w):zt.set(v,O,$,X),Rt.viewport(ft.copy(zt).multiplyScalar(Zt()).round())},this.getScissor=function(v){return v.copy(Se)},this.setScissor=function(v,O,$,X){v.isVector4?Se.set(v.x,v.y,v.z,v.w):Se.set(v,O,$,X),Rt.scissor(Gt.copy(Se).multiplyScalar(Zt()).round())},this.getScissorTest=function(){return ye},this.setScissorTest=function(v){Rt.setScissorTest(ye=v)},this.setOpaqueSort=function(v){oe=v},this.setTransparentSort=function(v){$t=v},this.getClearColor=function(v){return v.copy(L.getClearColor())},this.setClearColor=function(){L.setClearColor(...arguments)},this.getClearAlpha=function(){return L.getClearAlpha()},this.setClearAlpha=function(){L.setClearAlpha(...arguments)},this.clear=function(v=!0,O=!0,$=!0){let X=0;if(v){let q=!1;if(dt!==null){let At=dt.texture.format;q=m.has(At)}if(q){let At=dt.texture.type,Ot=g.has(At),Et=L.getClearColor(),Nt=L.getClearAlpha(),Vt=Et.r,se=Et.g,re=Et.b;Ot?(E[0]=Vt,E[1]=se,E[2]=re,E[3]=Nt,N.clearBufferuiv(N.COLOR,0,E)):(P[0]=Vt,P[1]=se,P[2]=re,P[3]=Nt,N.clearBufferiv(N.COLOR,0,P))}else X|=N.COLOR_BUFFER_BIT}O&&(X|=N.DEPTH_BUFFER_BIT,this.state.buffers.depth.setMask(!0)),$&&(X|=N.STENCIL_BUFFER_BIT,this.state.buffers.stencil.setMask(4294967295)),X!==0&&N.clear(X)},this.clearColor=function(){this.clear(!0,!1,!1)},this.clearDepth=function(){this.clear(!1,!0,!1)},this.clearStencil=function(){this.clear(!1,!1,!0)},this.setNodesHandler=function(v){v.setRenderer(this),H=v},this.dispose=function(){e.removeEventListener("webglcontextlost",Xt,!1),e.removeEventListener("webglcontextrestored",le,!1),e.removeEventListener("webglcontextcreationerror",Lt,!1),L.dispose(),Ct.dispose(),rt.dispose(),Dt.dispose(),Pt.dispose(),w.dispose(),mt.dispose(),W.dispose(),_t.dispose(),Wt.dispose(),ct.dispose(),gt.dispose(),gt.removeEventListener("sessionstart",Er),gt.removeEventListener("sessionend",Tr),jn.stop()};function Xt(v){v.preventDefault(),ah("WebGLRenderer: Context Lost."),k=!0}function le(){ah("WebGLRenderer: Context Restored."),k=!1;let v=en.autoReset,O=bt.enabled,$=bt.autoUpdate,X=bt.needsUpdate,q=bt.type;de(),en.autoReset=v,bt.enabled=O,bt.autoUpdate=$,bt.needsUpdate=X,bt.type=q}function Lt(v){ie("WebGLRenderer: A WebGL context could not be created. Reason: ",v.statusMessage)}function Ce(v){let O=v.target;O.removeEventListener("dispose",Ce),Ve(O)}function Ve(v){Ke(v),Pt.remove(v)}function Ke(v){let O=Pt.get(v).programs;O!==void 0&&(O.forEach(function($){ct.releaseProgram($)}),v.isShaderMaterial&&ct.releaseShaderCache(v))}this.renderBufferDirect=function(v,O,$,X,q,At){O===null&&(O=Un);let Ot=q.isMesh&&q.matrixWorld.determinantAffine()<0,Et=vs(v,O,$,X,q);Rt.setMaterial(X,Ot);let Nt=$.index,Vt=1;if(X.wireframe===!0){if(Nt=W.getWireframeAttribute($),Nt===void 0)return;Vt=2}let se=$.drawRange,re=$.attributes.position,Ht=se.start*Vt,ve=(se.start+se.count)*Vt;At!==null&&(Ht=Math.max(Ht,At.start*Vt),ve=Math.min(ve,(At.start+At.count)*Vt)),Nt!==null?(Ht=Math.max(Ht,0),ve=Math.min(ve,Nt.count)):re!=null&&(Ht=Math.max(Ht,0),ve=Math.min(ve,re.count));let Fe=ve-Ht;if(Fe<0||Fe===1/0)return;_t.setup(q,X,Et,$,Nt);let Ae,Ie=Q;if(Nt!==null&&(Ae=y.get(Nt),Ie=St,Ie.setIndex(Ae)),q.isMesh)X.wireframe===!0?(Rt.setLineWidth(X.wireframeLinewidth*Zt()),Ie.setMode(N.LINES)):Ie.setMode(N.TRIANGLES);else if(q.isLine){let hn=X.linewidth;hn===void 0&&(hn=1),Rt.setLineWidth(hn*Zt()),q.isLineSegments?Ie.setMode(N.LINES):q.isLineLoop?Ie.setMode(N.LINE_LOOP):Ie.setMode(N.LINE_STRIP)}else q.isPoints?Ie.setMode(N.POINTS):q.isSprite&&Ie.setMode(N.TRIANGLES);if(q.isBatchedMesh)if(we.get("WEBGL_multi_draw"))Ie.renderMultiDraw(q._multiDrawStarts,q._multiDrawCounts,q._multiDrawCount);else{let hn=q._multiDrawStarts,Bt=q._multiDrawCounts,He=q._multiDrawCount,te=Nt?y.get(Nt).bytesPerElement:1,On=Pt.get(X).currentProgram.getUniforms();for(let $e=0;$e<He;$e++)On.setValue(N,"_gl_DrawID",$e),Ie.render(hn[$e]/te,Bt[$e])}else if(q.isInstancedMesh)Ie.renderInstances(Ht,Fe,q.count);else if($.isInstancedBufferGeometry){let hn=$._maxInstanceCount!==void 0?$._maxInstanceCount:1/0,Bt=Math.min($.instanceCount,hn);Ie.renderInstances(Ht,Fe,Bt)}else Ie.render(Ht,Fe)};function qe(v,O,$,X){H!==null&&v.isNodeMaterial&&H.setObject(X,v),Xe===!0&&st.setState(v,$,!1),v.transparent===!0&&v.side===zn&&v.forceSinglePass===!1?(v.side=vn,v.needsUpdate=!0,ys(v,O,X),v.side=_s,v.needsUpdate=!0,ys(v,O,X),v.side=zn):ys(v,O,X)}this.compile=function(v,O,$=null){$===null&&($=v),H!==null&&H.renderStart(v,O,$),A=rt.get($),A.init(O),b.push(A),$.traverseVisible(function(q){q.isLight&&q.layers.test(O.layers)&&(A.pushLight(q),q.castShadow&&A.pushShadow(q))}),v!==$&&v.traverseVisible(function(q){q.isLight&&q.layers.test(O.layers)&&(A.pushLight(q),q.castShadow&&A.pushShadow(q))}),A.setupLights(),H!==null&&H.updateLights(A.state.lightsArray),_n=this.localClippingEnabled,Xe=st.init(this.clippingPlanes,_n),Xe===!0&&st.setGlobalState(this.clippingPlanes,O),H!==null&&bt.render(A.state.shadowsArray,$,O);let X=new Set;return v.traverse(function(q){if(!(q.isMesh||q.isPoints||q.isLine||q.isSprite))return;let At=q.material;if(At)if(Array.isArray(At))for(let Ot=0;Ot<At.length;Ot++){let Et=At[Ot];qe(Et,$,O,q),X.add(Et)}else qe(At,$,O,q),X.add(At)}),A=b.pop(),H!==null&&H.renderEnd(),X},this.compileAsync=function(v,O,$=null){let X=this.compile(v,O,$);return new Promise(q=>{function At(){if(X.forEach(function(Ot){let Nt=Pt.get(Ot).currentProgram;(Nt===void 0||Nt.isReady())&&X.delete(Ot)}),X.size===0){q(v);return}setTimeout(At,10)}we.get("KHR_parallel_shader_compile")!==null?At():setTimeout(At,10)})};let oi=null;function $n(v){oi&&oi(v)}function Er(){jn.stop()}function Tr(){jn.start()}let jn=new Od;jn.setAnimationLoop($n),typeof self<"u"&&jn.setContext(self),this.setAnimationLoop=function(v){oi=v,gt.setAnimationLoop(v),v===null?jn.stop():jn.start()},gt.addEventListener("sessionstart",Er),gt.addEventListener("sessionend",Tr),this.render=function(v,O){if(O!==void 0&&O.isCamera!==!0){ie("WebGLRenderer.render: camera is not an instance of THREE.Camera.");return}if(k===!0)return;H!==null&&H.renderStart(v,O);let $=gt.enabled===!0&&gt.isPresenting===!0,X=G!==null&&(dt===null||$)&&G.begin(B,dt);if(v.matrixWorldAutoUpdate===!0&&v.updateMatrixWorld(),O.parent===null&&O.matrixWorldAutoUpdate===!0&&O.updateMatrixWorld(),gt.enabled===!0&&gt.isPresenting===!0&&(G===null||G.isCompositing()===!1)&&(gt.cameraAutoUpdate===!0&&gt.updateCamera(O),O=gt.getCamera()),v.isScene===!0&&v.onBeforeRender(B,v,O,dt),A=rt.get(v,b.length),A.init(O),A.state.textureUnits=Dt.getTextureUnits(),b.push(A),ke.multiplyMatrices(O.projectionMatrix,O.matrixWorldInverse),O.isArrayCamera?Je.setFromArrayCamera(O):he.setFromProjectionMatrix(ke,ni,O.reversedDepth),_n=this.localClippingEnabled,Xe=st.init(this.clippingPlanes,_n),C=Ct.get(v,_.length),C.init(),_.push(C),this.info.render.frame++,gt.enabled===!0&&gt.isPresenting===!0){let Ot=B.xr.getDepthSensingMesh();Ot!==null&&Li(Ot,O,-1/0,B.sortObjects)}Li(v,O,0,B.sortObjects),C.finish(),H!==null&&H.updateLights(A.state.lightsArray),B.sortObjects===!0&&C.sort(oe,$t),pe=gt.enabled===!1||gt.isPresenting===!1||gt.hasDepthSensing()===!1,pe&&L.addToRenderList(C,v),this.info.autoReset===!0&&this.info.reset(),Xe===!0&&st.beginShadows();let q=A.state.shadowsArray;if(bt.render(q,v,O),Xe===!0&&st.endShadows(),(X&&G.hasRenderPass())===!1){let Ot=C.opaque,Et=C.transmissive;if(A.setupLights(),O.isArrayCamera){let Nt=O.cameras;if(Et.length>0)for(let Vt=0,se=Nt.length;Vt<se;Vt++){let re=Nt[Vt];Us(Ot,Et,v,re)}pe&&L.render(v);for(let Vt=0,se=Nt.length;Vt<se;Vt++){let re=Nt[Vt];Qn(C,v,re,re.viewport)}}else Et.length>0&&Us(Ot,Et,v,O),pe&&L.render(v),Qn(C,v,O)}dt!==null&&j===0&&(Dt.updateMultisampleRenderTarget(dt),Dt.updateRenderTargetMipmap(dt)),X&&G.end(B),v.isScene===!0&&v.onAfterRender(B,v,O),_t.resetDefaultState(),V=-1,it=null,b.pop(),b.length>0?(A=b[b.length-1],Dt.setTextureUnits(A.state.textureUnits),Xe===!0&&st.setGlobalState(B.clippingPlanes,A.state.camera)):A=null,_.pop(),_.length>0?C=_[_.length-1]:C=null,H!==null&&H.renderEnd()};function Li(v,O,$,X){if(v.visible===!1)return;if(v.layers.test(O.layers)){if(v.isGroup)$=v.renderOrder;else if(v.isLOD)v.autoUpdate===!0&&v.update(O);else if(v.isLight)A.pushLight(v),v.castShadow&&A.pushShadow(v);else if(v.isSprite){let Ot=O.isArrayCamera?Je:he;if(!v.frustumCulled||v.intersectsFrustum(Ot)){X&&on.setFromMatrixPosition(v.matrixWorld).applyMatrix4(ke);let Et=mt.update(v),Nt=v.material;Nt.visible&&C.push(v,Et,Nt,$,on.z,null,O)}}else if(v.isMesh||v.isLine||v.isPoints){let Ot=O.isArrayCamera?Je:he;if(!v.frustumCulled||v.intersectsFrustum(Ot)){let Et=mt.update(v),Nt=v.material;if(X&&(v.boundingSphere!==void 0?(v.boundingSphere===null&&v.computeBoundingSphere(),on.copy(v.boundingSphere.center)):(Et.boundingSphere===null&&Et.computeBoundingSphere(),on.copy(Et.boundingSphere.center)),on.applyMatrix4(v.matrixWorld).applyMatrix4(ke)),Array.isArray(Nt)){let Vt=Et.groups;for(let se=0,re=Vt.length;se<re;se++){let Ht=Vt[se],ve=Nt[Ht.materialIndex];ve&&ve.visible&&C.push(v,Et,ve,$,on.z,Ht,O)}}else Nt.visible&&C.push(v,Et,Nt,$,on.z,null,O)}}}let At=v.children;for(let Ot=0,Et=At.length;Ot<Et;Ot++)Li(At[Ot],O,$,X)}function Qn(v,O,$,X){let{opaque:q,transmissive:At,transparent:Ot}=v;A.setupLightsView($),Xe===!0&&st.setGlobalState(B.clippingPlanes,$),X&&Rt.viewport(ft.copy(X)),q.length>0&&Fn(q,O,$),At.length>0&&Fn(At,O,$),Ot.length>0&&Fn(Ot,O,$),Rt.buffers.depth.setTest(!0),Rt.buffers.depth.setMask(!0),Rt.buffers.color.setMask(!0),Rt.setPolygonOffset(!1)}function Us(v,O,$,X){if(($.isScene===!0?$.overrideMaterial:null)!==null)return;if(A.state.transmissionRenderTarget[X.id]===void 0){let Ht=we.has("EXT_color_buffer_half_float")||we.has("EXT_color_buffer_float");A.state.transmissionRenderTarget[X.id]=new Zn(1,1,{generateMipmaps:!0,type:Ht?xi:Hn,minFilter:qi,samples:Math.max(4,ze.samples),stencilBuffer:r,resolveDepthBuffer:!1,resolveStencilBuffer:!1,storeMultisampledDepthBuffer:!1,storeMultisampledStencilBuffer:!1,colorSpace:be.workingColorSpace})}let At=A.state.transmissionRenderTarget[X.id],Ot=X.viewport||ft;At.setSize(Ot.z*B.transmissionResolutionScale,Ot.w*B.transmissionResolutionScale);let Et=B.getRenderTarget(),Nt=B.getActiveCubeFace(),Vt=B.getActiveMipmapLevel();B.setRenderTarget(At),B.getClearColor(at),It=B.getClearAlpha(),It<1&&B.setClearColor(16777215,.5),B.clear(),pe&&L.render($);let se=B.toneMapping;B.toneMapping=Ci;let re=X.viewport;if(X.viewport!==void 0&&(X.viewport=void 0),A.setupLightsView(X),Xe===!0&&st.setGlobalState(B.clippingPlanes,X),Fn(v,$,X),Dt.updateMultisampleRenderTarget(At),Dt.updateRenderTargetMipmap(At),we.has("WEBGL_multisampled_render_to_texture")===!1){let Ht=!1;for(let ve=0,Fe=O.length;ve<Fe;ve++){let Ae=O[ve],{object:Ie,geometry:hn,material:Bt,group:He}=Ae;if(Bt.side===zn&&Ie.layers.test(X.layers)){let te=Bt.side;Bt.side=vn,Bt.needsUpdate=!0,li(Ie,$,X,hn,Bt,He),Bt.side=te,Bt.needsUpdate=!0,Ht=!0}}Ht===!0&&(Dt.updateMultisampleRenderTarget(At),Dt.updateRenderTargetMipmap(At))}B.setRenderTarget(Et,Nt,Vt),B.setClearColor(at,It),re!==void 0&&(X.viewport=re),B.toneMapping=se}function Fn(v,O,$){let X=O.isScene===!0?O.overrideMaterial:null;for(let q=0,At=v.length;q<At;q++){let Ot=v[q],{object:Et,geometry:Nt,group:Vt}=Ot,se=Ot.material;se.allowOverride===!0&&X!==null&&(se=X),Et.layers.test($.layers)&&li(Et,O,$,Nt,se,Vt)}}function li(v,O,$,X,q,At){H!==null&&q.isNodeMaterial&&H.setObject(v,q),v.onBeforeRender(B,O,$,X,q,At),v.modelViewMatrix.multiplyMatrices($.matrixWorldInverse,v.matrixWorld),v.normalMatrix.getNormalMatrix(v.modelViewMatrix),q.onBeforeRender(B,O,$,X,v,At),q.transparent===!0&&q.side===zn&&q.forceSinglePass===!1?(q.side=vn,q.needsUpdate=!0,B.renderBufferDirect($,O,X,q,v,At),q.side=_s,q.needsUpdate=!0,B.renderBufferDirect($,O,X,q,v,At),q.side=zn):B.renderBufferDirect($,O,X,q,v,At),v.onAfterRender(B,O,$,X,q,At)}function wr(v){let O=0;for(let $ of v)$.texture!==null&&O++;return O}function ys(v,O,$){O.isScene!==!0&&(O=Un);let X=Pt.get(v),q=A.state.lights,At=A.state.shadowsArray,Ot=q.state.version,Et=ct.getParameters(v,q.state,At,O,$,A.state.lightProbeGridArray),Nt=ct.getProgramCacheKey(Et),Vt=X.programs;X.environment=v.isMeshStandardMaterial||v.isMeshLambertMaterial||v.isMeshPhongMaterial?O.environment:null,X.fog=O.fog;let se=v.isMeshStandardMaterial||v.isMeshLambertMaterial&&!v.envMap||v.isMeshPhongMaterial&&!v.envMap;X.envMap=w.get(v.envMap||X.environment,se),X.envMapRotation=X.environment!==null&&v.envMap===null?O.environmentRotation:v.envMapRotation,Vt===void 0&&(v.addEventListener("dispose",Ce),Vt=new Map,X.programs=Vt,X.programVariants=new Map);let re=Vt.get(Nt);if(re!==void 0){if(X.currentProgram===re&&X.lightsStateVersion===Ot)return Rr(v,Et),re}else Et.uniforms=ct.getUniforms(v),H!==null&&v.isNodeMaterial&&H.build(v,$,Et),v.onBeforeCompile(Et,B),re=ct.acquireProgram(Et,Nt),Vt.set(Nt,re),X.uniforms=Et.uniforms;let Ht=X.uniforms;return(!v.isShaderMaterial&&!v.isRawShaderMaterial||v.clipping===!0)&&(Ht.clippingPlanes=st.uniform),Rr(v,Et),X.needsLights=Hl(v),X.lightsStateVersion=Ot,X.needsLights&&(Ht.ambientLightColor.value=q.state.ambient,Ht.lightProbe.value=q.state.probe,Ht.sunLights.value=q.state.sun,Ht.sunLightShadows.value=q.state.sunShadow,Ht.directionalLights.value=q.state.directional,Ht.directionalLightShadows.value=q.state.directionalShadow,Ht.spotLights.value=q.state.spot,Ht.spotLightShadows.value=q.state.spotShadow,Ht.rectAreaLights.value=q.state.rectArea,Ht.ltc_1.value=q.state.rectAreaLTC1,Ht.ltc_2.value=q.state.rectAreaLTC2,Ht.pointLights.value=q.state.point,Ht.pointLightShadows.value=q.state.pointShadow,Ht.hemisphereLights.value=q.state.hemi,Ht.sunShadowMatrix.value=q.state.sunShadowMatrix,Ht.sunShadowCascade.value=q.state.sunShadowCascade,Ht.directionalShadowMatrix.value=q.state.directionalShadowMatrix,Ht.spotLightMatrix.value=q.state.spotLightMatrix,Ht.spotLightMap.value=q.state.spotLightMap,Ht.pointShadowMatrix.value=q.state.pointShadowMatrix),X.numLightProbeGrids=wr(A.state.lightProbeGridArray),X.currentProgram=re,X.uniformsList=null,re}function zl(v,O,$,X,q){let At=Pt.get(v),Ot=At.currentProgram.id+","+X+","+q,Et=At.programVariants.get(Ot);return Et===void 0?(Et=ys(v,O,$),At.programVariants.set(Ot,Et)):(At.currentProgram=Et,At.uniformsList=null,At.outputColorSpace=X,At.toneMapping=q),Et}function Ar(v){if(v.uniformsList===null){let O=v.currentProgram.getUniforms();v.uniformsList=Mr.seqWithValue(O.seq,v.uniforms)}return v.uniformsList}function Rr(v,O){let $=Pt.get(v);$.outputColorSpace=O.outputColorSpace,$.batching=O.batching,$.batchingColor=O.batchingColor,$.instancing=O.instancing,$.instancingColor=O.instancingColor,$.instancingMorph=O.instancingMorph,$.skinning=O.skinning,$.morphTargets=O.morphTargets,$.morphNormals=O.morphNormals,$.morphColors=O.morphColors,$.morphTargetsCount=O.morphTargetsCount,$.numClippingPlanes=O.numClippingPlanes,$.numIntersection=O.numClipIntersection,$.vertexAlphas=O.vertexAlphas,$.vertexTangents=O.vertexTangents,$.toneMapping=O.toneMapping}function vs(v,O,$,X,q){O.isScene!==!0&&(O=Un),Dt.resetTextureUnits();let At=O.fog,Ot=X.isMeshStandardMaterial||X.isMeshLambertMaterial||X.isMeshPhongMaterial?O.environment:null,Et=dt===null?B.outputColorSpace:dt.isXRRenderTarget===!0?dt.texture.colorSpace:be.workingColorSpace,Nt=X.isMeshStandardMaterial||X.isMeshLambertMaterial&&!X.envMap||X.isMeshPhongMaterial&&!X.envMap,Vt=w.get(X.envMap||Ot,Nt),se=X.vertexColors===!0&&!!$.attributes.color&&$.attributes.color.itemSize===4,re=!!$.attributes.tangent&&(!!X.normalMap||X.anisotropy>0),Ht=!!$.morphAttributes.position,ve=!!$.morphAttributes.normal,Fe=!!$.morphAttributes.color,Ae=Ci;X.toneMapped&&(dt===null||dt.isXRRenderTarget===!0)&&(Ae=B.toneMapping);let Ie=$.morphAttributes.position||$.morphAttributes.normal||$.morphAttributes.color,hn=Ie!==void 0?Ie.length:0,Bt=Pt.get(X),He=A.state.lights;if(Xe===!0&&(_n===!0||v!==it)){let Oe=v===it&&X.id===V;st.setState(X,v,Oe)}let te=!1,On=!1;X.version===Bt.__version?Bt.needsLights&&Bt.lightsStateVersion!==He.state.version||q.isBatchedMesh&&Bt.batching===!1||!q.isBatchedMesh&&Bt.batching===!0||q.isBatchedMesh&&Bt.batchingColor===!0&&q._colorsTexture===null||q.isBatchedMesh&&Bt.batchingColor===!1&&q._colorsTexture!==null||q.isInstancedMesh&&Bt.instancing===!1||!q.isInstancedMesh&&Bt.instancing===!0||q.isSkinnedMesh&&Bt.skinning===!1||!q.isSkinnedMesh&&Bt.skinning===!0||q.isInstancedMesh&&Bt.instancingColor===!0&&q.instanceColor===null||q.isInstancedMesh&&Bt.instancingColor===!1&&q.instanceColor!==null||q.isInstancedMesh&&Bt.instancingMorph===!0&&q.morphTexture===null||q.isInstancedMesh&&Bt.instancingMorph===!1&&q.morphTexture!==null||Bt.envMap!==Vt||X.fog===!0&&Bt.fog!==At||Bt.numClippingPlanes!==void 0&&(Bt.numClippingPlanes!==st.numPlanes||Bt.numIntersection!==st.numIntersection)||Bt.vertexAlphas!==se||Bt.vertexTangents!==re||Bt.morphTargets!==Ht||Bt.morphNormals!==ve||Bt.morphColors!==Fe||Bt.morphTargetsCount!==hn||Bt.numLightProbeGrids!==wr(A.state.lightProbeGridArray)?te=!0:(Bt.outputColorSpace!==Et||Bt.toneMapping!==Ae)&&(On=!0):(te=!0,Bt.__version=X.version);let $e=Bt.currentProgram;(te===!0||On===!0)&&($e=On===!0?zl(X,O,q,Et,Ae):ys(X,O,q),H&&X.isNodeMaterial&&H.onUpdateProgram(X,$e,Bt));let ti=!1,xn=!1,Pn=!1,xe=$e.getUniforms(),nn=Bt.uniforms;if(Rt.useProgram($e.program)&&(ti=!0,xn=!0,Pn=!0),X.id!==V&&(V=X.id,xn=!0),ti||it!==v){Rt.buffers.depth.getReversed()&&v.reversedDepth!==!0&&(v._reversedDepth=!0,v.updateProjectionMatrix()),xe.setValue(N,"projectionMatrix",v.projectionMatrix),xe.setValue(N,"viewMatrix",v.matrixWorldInverse);let sn=xe.map.cameraPosition;sn!==void 0&&sn.setValue(N,Kn.setFromMatrixPosition(v.matrixWorld)),ze.logarithmicDepthBuffer&&xe.setValue(N,"logDepthBufFC",2/(Math.log(v.far+1)/Math.LN2)),(X.isMeshPhongMaterial||X.isMeshToonMaterial||X.isMeshLambertMaterial||X.isMeshBasicMaterial||X.isMeshStandardMaterial||X.isShaderMaterial)&&xe.setValue(N,"isOrthographic",v.isOrthographicCamera===!0),it!==v&&(it=v,xn=!0,Pn=!0)}if(Bt.needsLights&&(He.state.sunShadowMap.length>0&&xe.setValue(N,"sunShadowMap",He.state.sunShadowMap,Dt),He.state.directionalShadowMap.length>0&&xe.setValue(N,"directionalShadowMap",He.state.directionalShadowMap,Dt),He.state.spotShadowMap.length>0&&xe.setValue(N,"spotShadowMap",He.state.spotShadowMap,Dt),He.state.pointShadowMap.length>0&&xe.setValue(N,"pointShadowMap",He.state.pointShadowMap,Dt)),q.isSkinnedMesh){xe.setOptional(N,q,"bindMatrix"),xe.setOptional(N,q,"bindMatrixInverse");let Oe=q.skeleton;Oe&&(Oe.boneTexture===null&&Oe.computeBoneTexture(),xe.setValue(N,"boneTexture",Oe.boneTexture,Dt))}q.isBatchedMesh&&(xe.setOptional(N,q,"batchingTexture"),xe.setValue(N,"batchingTexture",q._matricesTexture,Dt),xe.setOptional(N,q,"batchingIdTexture"),xe.setValue(N,"batchingIdTexture",q._indirectTexture,Dt),xe.setOptional(N,q,"batchingColorTexture"),q._colorsTexture!==null&&xe.setValue(N,"batchingColorTexture",q._colorsTexture,Dt));let Bn=$.morphAttributes;if((Bn.position!==void 0||Bn.normal!==void 0||Bn.color!==void 0)&&nt.update(q,$,$e),(xn||Bt.receiveShadow!==q.receiveShadow)&&(Bt.receiveShadow=q.receiveShadow,xe.setValue(N,"receiveShadow",q.receiveShadow)),(X.isMeshStandardMaterial||X.isMeshLambertMaterial||X.isMeshPhongMaterial)&&X.envMap===null&&O.environment!==null&&(nn.envMapIntensity.value=O.environmentIntensity),nn.dfgLUT!==void 0&&(nn.dfgLUT.value=cx()),xn){if(xe.setValue(N,"toneMappingExposure",B.toneMappingExposure),Bt.needsLights&&Ma(nn,Pn),At&&X.fog===!0&&wt.refreshFogUniforms(nn,At),wt.refreshMaterialUniforms(nn,X,pt,qt,A.state.transmissionRenderTarget[v.id]),Bt.needsLights&&Bt.numLightProbeGrids>0){let Oe=T,sn=0;for(let En of A.state.lightProbeGridArray)En.texture!==null&&(Oe.textures[sn]=En.texture,Oe.min[sn]=En.boundingBox.min,Oe.max[sn]=En.boundingBox.max,Oe.resolution[sn]=En.resolution,sn++);for(let En in Oe)Oe[En].length=sn;nn.probesSH.value=Oe.textures,nn.probesMin.value=Oe.min,nn.probesMax.value=Oe.max,nn.probesResolution.value=Oe.resolution}Mr.upload(N,Ar(Bt),nn,Dt)}if(X.isShaderMaterial&&X.uniformsNeedUpdate===!0&&(Mr.upload(N,Ar(Bt),nn,Dt),X.uniformsNeedUpdate=!1),X.isSpriteMaterial&&xe.setValue(N,"center",q.center),xe.setValue(N,"modelViewMatrix",q.modelViewMatrix),xe.setValue(N,"normalMatrix",q.normalMatrix),xe.setValue(N,"modelMatrix",q.matrixWorld),X.uniformsGroups!==void 0){let Oe=X.uniformsGroups;for(let sn=0,En=Oe.length;sn<En;sn++){let Re=Oe[sn];Wt.update(Re,$e),Wt.bind(Re,$e)}}return $e}function Ma(v,O){v.ambientLightColor.needsUpdate=O,v.lightProbe.needsUpdate=O,v.sunLights.needsUpdate=O,v.sunLightShadows.needsUpdate=O,v.directionalLights.needsUpdate=O,v.directionalLightShadows.needsUpdate=O,v.pointLights.needsUpdate=O,v.pointLightShadows.needsUpdate=O,v.spotLights.needsUpdate=O,v.spotLightShadows.needsUpdate=O,v.rectAreaLights.needsUpdate=O,v.hemisphereLights.needsUpdate=O}function Hl(v){return v.isMeshLambertMaterial||v.isMeshToonMaterial||v.isMeshPhongMaterial||v.isMeshStandardMaterial||v.isShadowMaterial||v.isShaderMaterial&&v.lights===!0}this.getActiveCubeFace=function(){return tt},this.getActiveMipmapLevel=function(){return j},this.getRenderTarget=function(){return dt},this.setRenderTargetTextures=function(v,O,$){let X=Pt.get(v);X.__autoAllocateDepthBuffer=v.resolveDepthBuffer===!1,X.__autoAllocateDepthBuffer===!1&&(X.__useRenderToTexture=!1),Pt.get(v.texture).__webglTexture=O,Pt.get(v.depthTexture).__webglTexture=X.__autoAllocateDepthBuffer?void 0:$,X.__hasExternalTextures=!0},this.setRenderTargetFramebuffer=function(v,O){let $=Pt.get(v);$.__webglFramebuffer=O,$.__useDefaultFramebuffer=O===void 0},this.setRenderTarget=function(v,O=0,$=0){dt=v,tt=O,j=$;let X=null,q=!1,At=!1;if(v){let Et=Pt.get(v);if(Et.__useDefaultFramebuffer!==void 0){Rt.bindFramebuffer(N.FRAMEBUFFER,Et.__webglFramebuffer),ft.copy(v.viewport),Gt.copy(v.scissor),ee=v.scissorTest,Rt.viewport(ft),Rt.scissor(Gt),Rt.setScissorTest(ee),V=-1;return}else if(Et.__webglFramebuffer===void 0)Dt.setupRenderTarget(v);else if(Et.__hasExternalTextures)Dt.rebindTextures(v,Pt.get(v.texture).__webglTexture,Pt.get(v.depthTexture).__webglTexture);else if(v.depthBuffer){let se=v.depthTexture;if(Et.__boundDepthTexture!==se){if(se!==null&&Pt.has(se)&&(v.width!==se.image.width||v.height!==se.image.height))throw new Error("THREE.WebGLRenderer: Attached DepthTexture is initialized to the incorrect size.");Dt.setupDepthRenderbuffer(v)}}let Nt=v.texture;(Nt.isData3DTexture||Nt.isDataArrayTexture||Nt.isCompressedArrayTexture)&&(At=!0);let Vt=Pt.get(v).__webglFramebuffer;v.isWebGLCubeRenderTarget?(Array.isArray(Vt[O])?X=Vt[O][$]:X=Vt[O],q=!0):v.samples>0&&Dt.useMultisampledRTT(v)===!1?X=Pt.get(v).__webglMultisampledFramebuffer:Array.isArray(Vt)?X=Vt[$]:X=Vt,ft.copy(v.viewport),Gt.copy(v.scissor),ee=v.scissorTest}else ft.copy(zt).multiplyScalar(pt).floor(),Gt.copy(Se).multiplyScalar(pt).floor(),ee=ye;if($!==0&&(X=K),Rt.bindFramebuffer(N.FRAMEBUFFER,X)&&Rt.drawBuffers(v,X),Rt.viewport(ft),Rt.scissor(Gt),Rt.setScissorTest(ee),q){let Et=Pt.get(v.texture);N.framebufferTexture2D(N.FRAMEBUFFER,N.COLOR_ATTACHMENT0,N.TEXTURE_CUBE_MAP_POSITIVE_X+O,Et.__webglTexture,$)}else if(At){let Et=O;for(let Nt=0;Nt<v.textures.length;Nt++){let Vt=Pt.get(v.textures[Nt]);N.framebufferTextureLayer(N.FRAMEBUFFER,N.COLOR_ATTACHMENT0+Nt,Vt.__webglTexture,$,Et)}}else if(v!==null&&$!==0){let Et=Pt.get(v.texture);N.framebufferTexture2D(N.FRAMEBUFFER,N.COLOR_ATTACHMENT0,N.TEXTURE_2D,Et.__webglTexture,$)}V=-1};function Sa(v){let O=Pt.get(v);return(O.__readFormat!==v.format||O.__readType!==v.type)&&(O.__readFormat=v.format,O.__readType=v.type,O.__formatReadable=ze.textureFormatReadable(v.format),O.__typeReadable=ze.textureTypeReadable(v.type)),O}this.readRenderTargetPixels=function(v,O,$,X,q,At,Ot,Et=0){if(!(v&&v.isWebGLRenderTarget)){ie("WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");return}let Nt=Pt.get(v).__webglFramebuffer;if(v.isWebGLCubeRenderTarget&&Ot!==void 0&&(Nt=Nt[Ot],Array.isArray(Nt)&&(Nt=Nt[0])),Nt){Rt.bindFramebuffer(N.FRAMEBUFFER,Nt);try{let Vt=v.textures[Et],se=Vt.format,re=Vt.type;v.textures.length>1&&N.readBuffer(N.COLOR_ATTACHMENT0+Et);let Ht=Sa(Vt);if(Ht.__formatReadable===!1){ie("WebGLRenderer.readRenderTargetPixels: renderTarget is not in RGBA or implementation defined format.");return}if(Ht.__typeReadable===!1){ie("WebGLRenderer.readRenderTargetPixels: renderTarget is not in UnsignedByteType or implementation defined type.");return}O>=0&&O<=v.width-X&&$>=0&&$<=v.height-q&&N.readPixels(O,$,X,q,vt.convert(se),vt.convert(re),At)}finally{let Vt=dt!==null?Pt.get(dt).__webglFramebuffer:null;Rt.bindFramebuffer(N.FRAMEBUFFER,Vt)}}},this.readRenderTargetPixelsAsync=async function(v,O,$,X,q,At,Ot,Et=0){if(!(v&&v.isWebGLRenderTarget))throw new Error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");let Nt=Pt.get(v).__webglFramebuffer;if(v.isWebGLCubeRenderTarget&&Ot!==void 0&&(Nt=Nt[Ot],Array.isArray(Nt)&&(Nt=Nt[0])),Nt)if(O>=0&&O<=v.width-X&&$>=0&&$<=v.height-q){Rt.bindFramebuffer(N.FRAMEBUFFER,Nt);let Vt=v.textures[Et],se=Vt.format,re=Vt.type;v.textures.length>1&&N.readBuffer(N.COLOR_ATTACHMENT0+Et);let Ht=Sa(Vt);if(Ht.__formatReadable===!1)throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in RGBA or implementation defined format.");if(Ht.__typeReadable===!1)throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in UnsignedByteType or implementation defined type.");let ve=N.createBuffer();N.bindBuffer(N.PIXEL_PACK_BUFFER,ve),N.bufferData(N.PIXEL_PACK_BUFFER,At.byteLength,N.STREAM_READ),N.readPixels(O,$,X,q,vt.convert(se),vt.convert(re),0),N.bindBuffer(N.PIXEL_PACK_BUFFER,null);let Fe=dt!==null?Pt.get(dt).__webglFramebuffer:null;Rt.bindFramebuffer(N.FRAMEBUFFER,Fe);let Ae=N.fenceSync(N.SYNC_GPU_COMMANDS_COMPLETE,0);return N.flush(),await ld(N,Ae,4),N.bindBuffer(N.PIXEL_PACK_BUFFER,ve),N.getBufferSubData(N.PIXEL_PACK_BUFFER,0,At),N.bindBuffer(N.PIXEL_PACK_BUFFER,null),N.deleteBuffer(ve),N.deleteSync(Ae),At}else throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: requested read bounds are out of range.")},this.copyFramebufferToTexture=function(v,O=null,$=0){let X=Math.pow(2,-$),q=Math.floor(v.image.width*X),At=Math.floor(v.image.height*X),Ot=O!==null?O.x:0,Et=O!==null?O.y:0;Dt.setTexture2D(v,0),N.copyTexSubImage2D(N.TEXTURE_2D,$,0,0,Ot,Et,q,At),Rt.unbindTexture()},this.copyTextureToTexture=function(v,O,$=null,X=null,q=0,At=0){let Ot,Et,Nt,Vt,se,re,Ht,ve,Fe,Ae=v.isCompressedTexture?v.mipmaps[At]:v.image;if($!==null)Ot=$.max.x-$.min.x,Et=$.max.y-$.min.y,Nt=$.isBox3?$.max.z-$.min.z:1,Vt=$.min.x,se=$.min.y,re=$.isBox3?$.min.z:0;else{let xe=Math.pow(2,-q);Ot=Math.floor(Ae.width*xe),Et=Math.floor(Ae.height*xe),v.isDataArrayTexture?Nt=Ae.depth:v.isData3DTexture?Nt=Math.floor(Ae.depth*xe):Nt=1,Vt=0,se=0,re=0}X!==null?(Ht=X.x,ve=X.y,Fe=X.z):(Ht=0,ve=0,Fe=0);let Ie=vt.convert(O.format),hn=vt.convert(O.type),Bt;O.isData3DTexture?(Dt.setTexture3D(O,0),Bt=N.TEXTURE_3D):O.isDataArrayTexture||O.isCompressedArrayTexture?(Dt.setTexture2DArray(O,0),Bt=N.TEXTURE_2D_ARRAY):(Dt.setTexture2D(O,0),Bt=N.TEXTURE_2D),Rt.activeTexture(N.TEXTURE0),Rt.pixelStorei(N.UNPACK_FLIP_Y_WEBGL,O.flipY),Rt.pixelStorei(N.UNPACK_PREMULTIPLY_ALPHA_WEBGL,O.premultiplyAlpha),Rt.pixelStorei(N.UNPACK_ALIGNMENT,O.unpackAlignment);let He=Rt.getParameter(N.UNPACK_ROW_LENGTH),te=Rt.getParameter(N.UNPACK_IMAGE_HEIGHT),On=Rt.getParameter(N.UNPACK_SKIP_PIXELS),$e=Rt.getParameter(N.UNPACK_SKIP_ROWS),ti=Rt.getParameter(N.UNPACK_SKIP_IMAGES);Rt.pixelStorei(N.UNPACK_ROW_LENGTH,Ae.width),Rt.pixelStorei(N.UNPACK_IMAGE_HEIGHT,Ae.height),Rt.pixelStorei(N.UNPACK_SKIP_PIXELS,Vt),Rt.pixelStorei(N.UNPACK_SKIP_ROWS,se),Rt.pixelStorei(N.UNPACK_SKIP_IMAGES,re);let xn=v.isDataArrayTexture||v.isData3DTexture,Pn=O.isDataArrayTexture||O.isData3DTexture;if(v.isDepthTexture){let xe=Pt.get(v),nn=Pt.get(O),Bn=Pt.get(xe.__renderTarget),Oe=Pt.get(nn.__renderTarget);Rt.bindFramebuffer(N.READ_FRAMEBUFFER,Bn.__webglFramebuffer),Rt.bindFramebuffer(N.DRAW_FRAMEBUFFER,Oe.__webglFramebuffer);for(let sn=0;sn<Nt;sn++)xn&&(N.framebufferTextureLayer(N.READ_FRAMEBUFFER,N.COLOR_ATTACHMENT0,Pt.get(v).__webglTexture,q,re+sn),N.framebufferTextureLayer(N.DRAW_FRAMEBUFFER,N.COLOR_ATTACHMENT0,Pt.get(O).__webglTexture,At,Fe+sn)),N.blitFramebuffer(Vt,se,Vt+Ot,se+Et,Ht,ve,Ht+Ot,ve+Et,N.DEPTH_BUFFER_BIT,N.NEAREST);Rt.bindFramebuffer(N.READ_FRAMEBUFFER,null),Rt.bindFramebuffer(N.DRAW_FRAMEBUFFER,null)}else if(q!==0||v.isRenderTargetTexture||Pt.has(v)){let xe=Pt.get(v),nn=Pt.get(O);Rt.bindFramebuffer(N.READ_FRAMEBUFFER,U),Rt.bindFramebuffer(N.DRAW_FRAMEBUFFER,Y);for(let Bn=0;Bn<Nt;Bn++)xn?N.framebufferTextureLayer(N.READ_FRAMEBUFFER,N.COLOR_ATTACHMENT0,xe.__webglTexture,q,re+Bn):N.framebufferTexture2D(N.READ_FRAMEBUFFER,N.COLOR_ATTACHMENT0,N.TEXTURE_2D,xe.__webglTexture,q),Pn?N.framebufferTextureLayer(N.DRAW_FRAMEBUFFER,N.COLOR_ATTACHMENT0,nn.__webglTexture,At,Fe+Bn):N.framebufferTexture2D(N.DRAW_FRAMEBUFFER,N.COLOR_ATTACHMENT0,N.TEXTURE_2D,nn.__webglTexture,At),q!==0?N.blitFramebuffer(Vt,se,Vt+Ot,se+Et,Ht,ve,Ht+Ot,ve+Et,N.COLOR_BUFFER_BIT,N.NEAREST):Pn?N.copyTexSubImage3D(Bt,At,Ht,ve,Fe+Bn,Vt,se,Ot,Et):N.copyTexSubImage2D(Bt,At,Ht,ve,Vt,se,Ot,Et);Rt.bindFramebuffer(N.READ_FRAMEBUFFER,null),Rt.bindFramebuffer(N.DRAW_FRAMEBUFFER,null)}else Pn?v.isDataTexture||v.isData3DTexture?N.texSubImage3D(Bt,At,Ht,ve,Fe,Ot,Et,Nt,Ie,hn,Ae.data):O.isCompressedArrayTexture?N.compressedTexSubImage3D(Bt,At,Ht,ve,Fe,Ot,Et,Nt,Ie,Ae.data):N.texSubImage3D(Bt,At,Ht,ve,Fe,Ot,Et,Nt,Ie,hn,Ae):v.isDataTexture?N.texSubImage2D(N.TEXTURE_2D,At,Ht,ve,Ot,Et,Ie,hn,Ae.data):v.isCompressedTexture?N.compressedTexSubImage2D(N.TEXTURE_2D,At,Ht,ve,Ae.width,Ae.height,Ie,Ae.data):N.texSubImage2D(N.TEXTURE_2D,At,Ht,ve,Ot,Et,Ie,hn,Ae);Rt.pixelStorei(N.UNPACK_ROW_LENGTH,He),Rt.pixelStorei(N.UNPACK_IMAGE_HEIGHT,te),Rt.pixelStorei(N.UNPACK_SKIP_PIXELS,On),Rt.pixelStorei(N.UNPACK_SKIP_ROWS,$e),Rt.pixelStorei(N.UNPACK_SKIP_IMAGES,ti),At===0&&O.generateMipmaps===!0&&O.mipmapsAutoUpdate===!0&&N.generateMipmap(Bt),Rt.unbindTexture()},this.initRenderTarget=function(v){Pt.get(v).__webglFramebuffer===void 0&&Dt.setupRenderTarget(v)},this.initTexture=function(v){v.isCubeTexture?Dt.setTextureCube(v,0):v.isData3DTexture?Dt.setTexture3D(v,0):v.isDataArrayTexture||v.isCompressedArrayTexture?Dt.setTexture2DArray(v,0):Dt.setTexture2D(v,0),Rt.unbindTexture()},this.resetState=function(){tt=0,j=0,dt=null,Rt.reset(),_t.reset()},typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}get coordinateSystem(){return ni}get outputColorSpace(){return this._outputColorSpace}set outputColorSpace(t){this._outputColorSpace=t;let e=this.getContext();e.drawingBufferColorSpace=be._getDrawingBufferColorSpace(t),e.unpackColorSpace=be._getUnpackColorSpace()}};var Zd={type:"change"},Ah={type:"start"},Kd={type:"end"},Bl=new hs,Jd=new Yn,ux=Math.cos(70*hh.DEG2RAD),gn=new D,Gn=2*Math.PI,Le={NONE:-1,ROTATE:0,DOLLY:1,PAN:2,TOUCH_ROTATE:3,TOUCH_PAN:4,TOUCH_DOLLY_PAN:5,TOUCH_DOLLY_ROTATE:6},wh=1e-6,kl=class extends la{constructor(t,e=null){super(t,e),this.state=Le.NONE,this.target=new D,this.cursor=new D,this.minDistance=0,this.maxDistance=1/0,this.minZoom=0,this.maxZoom=1/0,this.minTargetRadius=0,this.maxTargetRadius=1/0,this.minPolarAngle=0,this.maxPolarAngle=Math.PI,this.minAzimuthAngle=-1/0,this.maxAzimuthAngle=1/0,this.enableDamping=!1,this.dampingFactor=.05,this.enableZoom=!0,this.zoomSpeed=1,this.enableRotate=!0,this.rotateSpeed=1,this.keyRotateSpeed=1,this.enablePan=!0,this.panSpeed=1,this.screenSpacePanning=!0,this.keyPanSpeed=7,this.zoomToCursor=!1,this.autoRotate=!1,this.autoRotateSpeed=2,this.keys={LEFT:"ArrowLeft",UP:"ArrowUp",RIGHT:"ArrowRight",BOTTOM:"ArrowDown"},this.mouseButtons={LEFT:ms.ROTATE,MIDDLE:ms.DOLLY,RIGHT:ms.PAN},this.touches={ONE:gs.ROTATE,TWO:gs.DOLLY_PAN},this.target0=this.target.clone(),this.position0=this.object.position.clone(),this.zoom0=this.object.zoom,this._cursorStyle="auto",this._domElementKeyEvents=null,this._lastPosition=new D,this._lastQuaternion=new Nn,this._lastTargetPosition=new D,this._quat=new Nn().setFromUnitVectors(t.up,new D(0,1,0)),this._quatInverse=this._quat.clone().invert(),this._spherical=new mr,this._sphericalDelta=new mr,this._scale=1,this._panOffset=new D,this._rotateStart=new kt,this._rotateEnd=new kt,this._rotateDelta=new kt,this._panStart=new kt,this._panEnd=new kt,this._panDelta=new kt,this._dollyStart=new kt,this._dollyEnd=new kt,this._dollyDelta=new kt,this._dollyDirection=new D,this._mouse=new kt,this._performCursorZoom=!1,this._pointers=[],this._pointerPositions={},this._controlActive=!1,this._onPointerMove=fx.bind(this),this._onPointerDown=dx.bind(this),this._onPointerUp=px.bind(this),this._onContextMenu=Mx.bind(this),this._onMouseWheel=_x.bind(this),this._onKeyDown=xx.bind(this),this._onTouchStart=yx.bind(this),this._onTouchMove=vx.bind(this),this._onMouseDown=mx.bind(this),this._onMouseMove=gx.bind(this),this._interceptControlDown=Sx.bind(this),this._interceptControlUp=bx.bind(this),this.domElement!==null&&this.connect(this.domElement),this.update()}set cursorStyle(t){this._cursorStyle=t,t==="grab"?this.domElement.style.cursor="grab":this.domElement.style.cursor="auto"}get cursorStyle(){return this._cursorStyle}connect(t){super.connect(t),this.domElement.addEventListener("pointerdown",this._onPointerDown),this.domElement.addEventListener("pointercancel",this._onPointerUp),this.domElement.addEventListener("contextmenu",this._onContextMenu),this.domElement.addEventListener("wheel",this._onMouseWheel,{passive:!1}),this.domElement.ownerDocument.addEventListener("keydown",this._interceptControlDown,{passive:!0,capture:!0}),this.domElement.style.touchAction="none"}disconnect(){this.state=Le.NONE,this.domElement.removeEventListener("pointerdown",this._onPointerDown),this.domElement.ownerDocument.removeEventListener("pointermove",this._onPointerMove),this.domElement.ownerDocument.removeEventListener("pointerup",this._onPointerUp),this.domElement.removeEventListener("pointercancel",this._onPointerUp),this.domElement.removeEventListener("wheel",this._onMouseWheel),this.domElement.removeEventListener("contextmenu",this._onContextMenu),this.stopListenToKeyEvents(),this.domElement.ownerDocument.removeEventListener("keydown",this._interceptControlDown,{capture:!0}),this.domElement.ownerDocument.removeEventListener("keyup",this._interceptControlUp,{capture:!0}),this._controlActive=!1,this._pointers.length=0,this._pointerPositions={},this.domElement.style.touchAction="",this.domElement.style.cursor="auto"}dispose(){this.disconnect()}getPolarAngle(){return this._spherical.phi}getAzimuthalAngle(){return this._spherical.theta}getDistance(){return this.object.position.distanceTo(this.target)}listenToKeyEvents(t){t.addEventListener("keydown",this._onKeyDown),this._domElementKeyEvents=t}stopListenToKeyEvents(){this._domElementKeyEvents!==null&&(this._domElementKeyEvents.removeEventListener("keydown",this._onKeyDown),this._domElementKeyEvents=null)}saveState(){this.target0.copy(this.target),this.position0.copy(this.object.position),this.zoom0=this.object.zoom}reset(){this.target.copy(this.target0),this.object.position.copy(this.position0),this.object.zoom=this.zoom0,this.object.updateProjectionMatrix(),this.dispatchEvent(Zd),this.update(),this.state=Le.NONE}pan(t,e){this._pan(t,e),this.update()}dollyIn(t){this._dollyIn(t),this.update()}dollyOut(t){this._dollyOut(t),this.update()}rotateLeft(t){this._rotateLeft(t),this.update()}rotateUp(t){this._rotateUp(t),this.update()}update(t=null){let e=this.object.position;gn.copy(e).sub(this.target),gn.applyQuaternion(this._quat),this._spherical.setFromVector3(gn),this.autoRotate&&this.state===Le.NONE&&this._rotateLeft(this._getAutoRotationAngle(t)),this.enableDamping?(this._spherical.theta+=this._sphericalDelta.theta*this.dampingFactor,this._spherical.phi+=this._sphericalDelta.phi*this.dampingFactor):(this._spherical.theta+=this._sphericalDelta.theta,this._spherical.phi+=this._sphericalDelta.phi);let n=this.minAzimuthAngle,s=this.maxAzimuthAngle;isFinite(n)&&isFinite(s)&&(n<-Math.PI?n+=Gn:n>Math.PI&&(n-=Gn),s<-Math.PI?s+=Gn:s>Math.PI&&(s-=Gn),n<=s?this._spherical.theta=Math.max(n,Math.min(s,this._spherical.theta)):this._spherical.theta=this._spherical.theta>(n+s)/2?Math.max(n,this._spherical.theta):Math.min(s,this._spherical.theta)),this._spherical.phi=Math.max(this.minPolarAngle,Math.min(this.maxPolarAngle,this._spherical.phi)),this._spherical.makeSafe(),this.enableDamping===!0?this.target.addScaledVector(this._panOffset,this.dampingFactor):this.target.add(this._panOffset),this.target.sub(this.cursor),this.target.clampLength(this.minTargetRadius,this.maxTargetRadius),this.target.add(this.cursor);let r=!1;if(this.zoomToCursor&&this._performCursorZoom||this.object.isOrthographicCamera)this._spherical.radius=this._clampDistance(this._spherical.radius);else{let a=this._spherical.radius;this._spherical.radius=this._clampDistance(this._spherical.radius*this._scale),r=a!=this._spherical.radius}if(gn.setFromSpherical(this._spherical),gn.applyQuaternion(this._quatInverse),e.copy(this.target).add(gn),this.object.lookAt(this.target),this.enableDamping===!0?(this._sphericalDelta.theta*=1-this.dampingFactor,this._sphericalDelta.phi*=1-this.dampingFactor,this._panOffset.multiplyScalar(1-this.dampingFactor)):(this._sphericalDelta.set(0,0,0),this._panOffset.set(0,0,0)),this.zoomToCursor&&this._performCursorZoom){let a=null;if(this.object.isPerspectiveCamera){let o=gn.length();a=this._clampDistance(o*this._scale);let l=o-a;this.object.position.addScaledVector(this._dollyDirection,l),this.object.updateMatrixWorld(),r=!!l}else if(this.object.isOrthographicCamera){let o=new D(this._mouse.x,this._mouse.y,0);o.unproject(this.object);let l=this.object.zoom;this.object.zoom=Math.max(this.minZoom,Math.min(this.maxZoom,this.object.zoom/this._scale)),this.object.updateProjectionMatrix(),r=l!==this.object.zoom;let c=new D(this._mouse.x,this._mouse.y,0);c.unproject(this.object),this.object.position.sub(c).add(o),this.object.updateMatrixWorld(),a=gn.length()}else console.warn("WARNING: OrbitControls.js encountered an unknown camera type - zoom to cursor disabled."),this.zoomToCursor=!1;a!==null&&(this.screenSpacePanning?this.target.set(0,0,-1).transformDirection(this.object.matrix).multiplyScalar(a).add(this.object.position):(Bl.origin.copy(this.object.position),Bl.direction.set(0,0,-1).transformDirection(this.object.matrix),Math.abs(this.object.up.dot(Bl.direction))<ux?this.object.lookAt(this.target):(Jd.setFromNormalAndCoplanarPoint(this.object.up,this.target),Bl.intersectPlane(Jd,this.target))))}else if(this.object.isOrthographicCamera){let a=this.object.zoom;this.object.zoom=Math.max(this.minZoom,Math.min(this.maxZoom,this.object.zoom/this._scale)),a!==this.object.zoom&&(this.object.updateProjectionMatrix(),r=!0)}return this._scale=1,this._performCursorZoom=!1,r||this._lastPosition.distanceToSquared(this.object.position)>wh||8*(1-this._lastQuaternion.dot(this.object.quaternion))>wh||this._lastTargetPosition.distanceToSquared(this.target)>wh?(this.dispatchEvent(Zd),this._lastPosition.copy(this.object.position),this._lastQuaternion.copy(this.object.quaternion),this._lastTargetPosition.copy(this.target),!0):!1}_getAutoRotationAngle(t){return t!==null?Gn/60*this.autoRotateSpeed*t:Gn/60/60*this.autoRotateSpeed}_getZoomScale(t){let e=Math.abs(t*.01);return Math.pow(.95,this.zoomSpeed*e)}_rotateLeft(t){this._sphericalDelta.theta-=t}_rotateUp(t){this._sphericalDelta.phi-=t}_panLeft(t,e){gn.setFromMatrixColumn(e,0),gn.multiplyScalar(-t),this._panOffset.add(gn)}_panUp(t,e){this.screenSpacePanning===!0?gn.setFromMatrixColumn(e,1):(gn.setFromMatrixColumn(e,0),gn.crossVectors(this.object.up,gn)),gn.multiplyScalar(t),this._panOffset.add(gn)}_pan(t,e){let n=this.domElement;if(this.object.isPerspectiveCamera){let s=this.object.position;gn.copy(s).sub(this.target);let r=gn.length();r*=Math.tan(this.object.fov/2*Math.PI/180),this._panLeft(2*t*r/n.clientHeight,this.object.matrix),this._panUp(2*e*r/n.clientHeight,this.object.matrix)}else this.object.isOrthographicCamera?(this._panLeft(t*(this.object.right-this.object.left)/this.object.zoom/n.clientWidth,this.object.matrix),this._panUp(e*(this.object.top-this.object.bottom)/this.object.zoom/n.clientHeight,this.object.matrix)):(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - pan disabled."),this.enablePan=!1)}_dollyOut(t){this.object.isPerspectiveCamera||this.object.isOrthographicCamera?this._scale/=t:(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled."),this.enableZoom=!1)}_dollyIn(t){this.object.isPerspectiveCamera||this.object.isOrthographicCamera?this._scale*=t:(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled."),this.enableZoom=!1)}_updateZoomParameters(t,e){if(!this.zoomToCursor)return;this._performCursorZoom=!0;let n=this.domElement.getBoundingClientRect(),s=t-n.left,r=e-n.top,a=n.width,o=n.height;this._mouse.x=s/a*2-1,this._mouse.y=-(r/o)*2+1,this._dollyDirection.set(this._mouse.x,this._mouse.y,1).unproject(this.object).sub(this.object.position).normalize()}_clampDistance(t){return Math.max(this.minDistance,Math.min(this.maxDistance,t))}_handleMouseDownRotate(t){this._rotateStart.set(t.clientX,t.clientY)}_handleMouseDownDolly(t){this._updateZoomParameters(t.clientX,t.clientY),this._dollyStart.set(t.clientX,t.clientY)}_handleMouseDownPan(t){this._panStart.set(t.clientX,t.clientY)}_handleMouseMoveRotate(t){this._rotateEnd.set(t.clientX,t.clientY),this._rotateDelta.subVectors(this._rotateEnd,this._rotateStart).multiplyScalar(this.rotateSpeed);let e=this.domElement;this._rotateLeft(Gn*this._rotateDelta.x/e.clientHeight),this._rotateUp(Gn*this._rotateDelta.y/e.clientHeight),this._rotateStart.copy(this._rotateEnd),this.update()}_handleMouseMoveDolly(t){this._dollyEnd.set(t.clientX,t.clientY),this._dollyDelta.subVectors(this._dollyEnd,this._dollyStart),this._dollyDelta.y>0?this._dollyOut(this._getZoomScale(this._dollyDelta.y)):this._dollyDelta.y<0&&this._dollyIn(this._getZoomScale(this._dollyDelta.y)),this._dollyStart.copy(this._dollyEnd),this.zoomToCursor&&(this._performCursorZoom=!0,this._dollyDirection.set(this._mouse.x,this._mouse.y,1).unproject(this.object).sub(this.object.position).normalize()),this.update()}_handleMouseMovePan(t){this._panEnd.set(t.clientX,t.clientY),this._panDelta.subVectors(this._panEnd,this._panStart).multiplyScalar(this.panSpeed),this._pan(this._panDelta.x,this._panDelta.y),this._panStart.copy(this._panEnd),this.update()}_handleMouseWheel(t){this._updateZoomParameters(t.clientX,t.clientY),t.deltaY<0?this._dollyIn(this._getZoomScale(t.deltaY)):t.deltaY>0&&this._dollyOut(this._getZoomScale(t.deltaY)),this.update()}_handleKeyDown(t){let e=!1;switch(t.code){case this.keys.UP:t.ctrlKey||t.metaKey||t.shiftKey?this.enableRotate&&this._rotateUp(Gn*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(0,this.keyPanSpeed),e=!0;break;case this.keys.BOTTOM:t.ctrlKey||t.metaKey||t.shiftKey?this.enableRotate&&this._rotateUp(-Gn*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(0,-this.keyPanSpeed),e=!0;break;case this.keys.LEFT:t.ctrlKey||t.metaKey||t.shiftKey?this.enableRotate&&this._rotateLeft(Gn*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(this.keyPanSpeed,0),e=!0;break;case this.keys.RIGHT:t.ctrlKey||t.metaKey||t.shiftKey?this.enableRotate&&this._rotateLeft(-Gn*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(-this.keyPanSpeed,0),e=!0;break}e&&(t.preventDefault(),this.update())}_handleTouchStartRotate(t){if(this._pointers.length===1)this._rotateStart.set(t.pageX,t.pageY);else{let e=this._getSecondPointerPosition(t),n=.5*(t.pageX+e.x),s=.5*(t.pageY+e.y);this._rotateStart.set(n,s)}}_handleTouchStartPan(t){if(this._pointers.length===1)this._panStart.set(t.pageX,t.pageY);else{let e=this._getSecondPointerPosition(t),n=.5*(t.pageX+e.x),s=.5*(t.pageY+e.y);this._panStart.set(n,s)}}_handleTouchStartDolly(t){let e=this._getSecondPointerPosition(t),n=t.pageX-e.x,s=t.pageY-e.y,r=Math.sqrt(n*n+s*s);this._dollyStart.set(0,r)}_handleTouchStartDollyPan(t){this.enableZoom&&this._handleTouchStartDolly(t),this.enablePan&&this._handleTouchStartPan(t)}_handleTouchStartDollyRotate(t){this.enableZoom&&this._handleTouchStartDolly(t),this.enableRotate&&this._handleTouchStartRotate(t)}_handleTouchMoveRotate(t){if(this._pointers.length==1)this._rotateEnd.set(t.pageX,t.pageY);else{let n=this._getSecondPointerPosition(t),s=.5*(t.pageX+n.x),r=.5*(t.pageY+n.y);this._rotateEnd.set(s,r)}this._rotateDelta.subVectors(this._rotateEnd,this._rotateStart).multiplyScalar(this.rotateSpeed);let e=this.domElement;this._rotateLeft(Gn*this._rotateDelta.x/e.clientHeight),this._rotateUp(Gn*this._rotateDelta.y/e.clientHeight),this._rotateStart.copy(this._rotateEnd)}_handleTouchMovePan(t){if(this._pointers.length===1)this._panEnd.set(t.pageX,t.pageY);else{let e=this._getSecondPointerPosition(t),n=.5*(t.pageX+e.x),s=.5*(t.pageY+e.y);this._panEnd.set(n,s)}this._panDelta.subVectors(this._panEnd,this._panStart).multiplyScalar(this.panSpeed),this._pan(this._panDelta.x,this._panDelta.y),this._panStart.copy(this._panEnd)}_handleTouchMoveDolly(t){let e=this._getSecondPointerPosition(t),n=t.pageX-e.x,s=t.pageY-e.y,r=Math.sqrt(n*n+s*s);this._dollyEnd.set(0,r),this._dollyDelta.set(0,Math.pow(this._dollyEnd.y/this._dollyStart.y,this.zoomSpeed)),this._dollyOut(this._dollyDelta.y),this._dollyStart.copy(this._dollyEnd);let a=(t.pageX+e.x)*.5,o=(t.pageY+e.y)*.5;this._updateZoomParameters(a,o)}_handleTouchMoveDollyPan(t){this.enableZoom&&this._handleTouchMoveDolly(t),this.enablePan&&this._handleTouchMovePan(t)}_handleTouchMoveDollyRotate(t){this.enableZoom&&this._handleTouchMoveDolly(t),this.enableRotate&&this._handleTouchMoveRotate(t)}_addPointer(t){this._pointers.push(t.pointerId)}_removePointer(t){delete this._pointerPositions[t.pointerId];for(let e=0;e<this._pointers.length;e++)if(this._pointers[e]==t.pointerId){this._pointers.splice(e,1);return}}_isTrackingPointer(t){for(let e=0;e<this._pointers.length;e++)if(this._pointers[e]==t.pointerId)return!0;return!1}_trackPointer(t){let e=this._pointerPositions[t.pointerId];e===void 0&&(e=new kt,this._pointerPositions[t.pointerId]=e),e.set(t.pageX,t.pageY)}_getSecondPointerPosition(t){let e=t.pointerId===this._pointers[0]?this._pointers[1]:this._pointers[0];return this._pointerPositions[e]}_customWheelEvent(t){let e=t.deltaMode,n={clientX:t.clientX,clientY:t.clientY,deltaY:t.deltaY};switch(e){case 1:n.deltaY*=16;break;case 2:n.deltaY*=100;break}return t.ctrlKey&&!this._controlActive&&(n.deltaY*=10),n}};function dx(i){this.enabled!==!1&&(this._pointers.length===0&&(this.domElement.setPointerCapture(i.pointerId),this.domElement.ownerDocument.addEventListener("pointermove",this._onPointerMove),this.domElement.ownerDocument.addEventListener("pointerup",this._onPointerUp)),!this._isTrackingPointer(i)&&(this._addPointer(i),i.pointerType==="touch"?this._onTouchStart(i):this._onMouseDown(i),this._cursorStyle==="grab"&&(this.domElement.style.cursor="grabbing")))}function fx(i){this.enabled!==!1&&(i.pointerType==="touch"?this._onTouchMove(i):this._onMouseMove(i))}function px(i){switch(this._removePointer(i),this._pointers.length){case 0:this.domElement.releasePointerCapture(i.pointerId),this.domElement.ownerDocument.removeEventListener("pointermove",this._onPointerMove),this.domElement.ownerDocument.removeEventListener("pointerup",this._onPointerUp),this.dispatchEvent(Kd),this.state=Le.NONE,this._cursorStyle==="grab"&&(this.domElement.style.cursor="grab");break;case 1:let t=this._pointers[0],e=this._pointerPositions[t];this._onTouchStart({pointerId:t,pageX:e.x,pageY:e.y});break}}function mx(i){let t;switch(i.button){case 0:t=this.mouseButtons.LEFT;break;case 1:t=this.mouseButtons.MIDDLE;break;case 2:t=this.mouseButtons.RIGHT;break;default:t=-1}switch(t){case ms.DOLLY:if(this.enableZoom===!1)return;this._handleMouseDownDolly(i),this.state=Le.DOLLY;break;case ms.ROTATE:if(i.ctrlKey||i.metaKey||i.shiftKey){if(this.enablePan===!1)return;this._handleMouseDownPan(i),this.state=Le.PAN}else{if(this.enableRotate===!1)return;this._handleMouseDownRotate(i),this.state=Le.ROTATE}break;case ms.PAN:if(i.ctrlKey||i.metaKey||i.shiftKey){if(this.enableRotate===!1)return;this._handleMouseDownRotate(i),this.state=Le.ROTATE}else{if(this.enablePan===!1)return;this._handleMouseDownPan(i),this.state=Le.PAN}break;default:this.state=Le.NONE}this.state!==Le.NONE&&this.dispatchEvent(Ah)}function gx(i){switch(this.state){case Le.ROTATE:if(this.enableRotate===!1)return;this._handleMouseMoveRotate(i);break;case Le.DOLLY:if(this.enableZoom===!1)return;this._handleMouseMoveDolly(i);break;case Le.PAN:if(this.enablePan===!1)return;this._handleMouseMovePan(i);break}}function _x(i){this.enabled===!1||this.enableZoom===!1||this.state!==Le.NONE||(i.preventDefault(),this.dispatchEvent(Ah),this._handleMouseWheel(this._customWheelEvent(i)),this.dispatchEvent(Kd))}function xx(i){this.enabled!==!1&&this._handleKeyDown(i)}function yx(i){switch(this._trackPointer(i),this._pointers.length){case 1:switch(this.touches.ONE){case gs.ROTATE:if(this.enableRotate===!1){this.state=Le.NONE;break}this._handleTouchStartRotate(i),this.state=Le.TOUCH_ROTATE;break;case gs.PAN:if(this.enablePan===!1){this.state=Le.NONE;break}this._handleTouchStartPan(i),this.state=Le.TOUCH_PAN;break;default:this.state=Le.NONE}break;case 2:switch(this.touches.TWO){case gs.DOLLY_PAN:if(this.enableZoom===!1&&this.enablePan===!1)return;this._handleTouchStartDollyPan(i),this.state=Le.TOUCH_DOLLY_PAN;break;case gs.DOLLY_ROTATE:if(this.enableZoom===!1&&this.enableRotate===!1)return;this._handleTouchStartDollyRotate(i),this.state=Le.TOUCH_DOLLY_ROTATE;break;default:this.state=Le.NONE}break;default:this.state=Le.NONE}this.state!==Le.NONE&&this.dispatchEvent(Ah)}function vx(i){switch(this._trackPointer(i),this.state){case Le.TOUCH_ROTATE:if(this.enableRotate===!1)return;this._handleTouchMoveRotate(i),this.update();break;case Le.TOUCH_PAN:if(this.enablePan===!1)return;this._handleTouchMovePan(i),this.update();break;case Le.TOUCH_DOLLY_PAN:if(this.enableZoom===!1&&this.enablePan===!1)return;this._handleTouchMoveDollyPan(i),this.update();break;case Le.TOUCH_DOLLY_ROTATE:if(this.enableZoom===!1&&this.enableRotate===!1)return;this._handleTouchMoveDollyRotate(i),this.update();break;default:this.state=Le.NONE}}function Mx(i){this.enabled!==!1&&i.preventDefault()}function Sx(i){i.key==="Control"&&(this._controlActive=!0,this.domElement.ownerDocument.addEventListener("keyup",this._interceptControlUp,{passive:!0,capture:!0}))}function bx(i){i.key==="Control"&&(this._controlActive=!1,this.domElement.ownerDocument.removeEventListener("keyup",this._interceptControlUp,{passive:!0,capture:!0}))}var Ex=`
.grel{position:relative;width:100%;background:#fff;border:1px solid #e4e4e4;overflow:hidden;touch-action:none}
.grel canvas{display:block}
.grel .lbs{position:absolute;inset:0;pointer-events:none;overflow:hidden}
.grel .lb{position:absolute;left:0;top:0;white-space:nowrap}
.grel .ldr{position:absolute;left:0;top:0;height:1px;background:rgba(20,20,20,.75);box-shadow:0 0 0 1px rgba(255,255,255,.55);transform-origin:0 50%;pointer-events:none;display:none}
.grel .nl{font:bold 12.5px Helvetica,Arial,sans-serif;color:#111;text-shadow:0 0 3px #fff,0 0 3px #fff,0 0 3px #fff}
.grel .lb.on,.grel .lb:hover,.grel .lb.tfoc{filter:none!important}.grel .lb.tfoc{background:#fff;border-radius:5px;padding:1px 4px;box-shadow:0 0 0 2px #fff,0 0 12px 4px rgba(255,255,255,.95);z-index:5}
.grel .tourbar .tpn{font:14px Questrial,Helvetica,Arial,sans-serif;padding:8px 14px;border-radius:20px;background:#fff;border:1px solid #222;display:none}
.grel .ql{font:bold 12px Helvetica,Arial,sans-serif;background:#111;color:#fff;padding:2px 5px}
.grel .pl{font:bold 13px Helvetica,Arial,sans-serif;letter-spacing:.1em;color:#111;text-shadow:0 0 3px #fff,0 0 3px #fff,0 0 4px #fff}
.grel .side{font:bold 17.5px Helvetica,Arial,sans-serif;letter-spacing:.14em;color:#1f6f66;text-shadow:0 0 3px #fff,0 0 3px #fff}.grel .side.hd{color:#8a2a22}.grel .side.ax{color:#333}.grel .lb.hit{pointer-events:auto;cursor:pointer}.grel .tip{position:absolute;display:none;z-index:4;max-width:340px;max-height:60%;overflow:auto;background:#222;color:#fff;font:13px/1.45 Questrial,Helvetica,Arial,sans-serif;padding:8px 10px;border-radius:2px;box-shadow:0 2px 8px rgba(0,0,0,.3)}.grel .tip b{display:block;margin-bottom:3px}.grel .tip .sm{opacity:.75;font-size:12px;margin-top:4px}
.grel .rdm{font:bold 12px Helvetica,Arial,sans-serif;color:#fff;background:#111;width:22px;height:22px;line-height:20px;text-align:center;border-radius:50%;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.4)}
.grel .clt{font:600 12px Helvetica,Arial,sans-serif;color:#111;background:#fff;border:1.5px solid #111;border-radius:999px;padding:3px 9px 3px 3px;display:inline-flex;align-items:center;gap:6px;box-shadow:0 1px 3px rgba(0,0,0,.25);transition:opacity .15s}.grel .clt i{font-style:normal;width:20px;height:20px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:700}
.grel .rdm.on{background:#7a1d12;transform:scale(1.25)}
.grel .wn{font:bold 11px Helvetica,Arial,sans-serif;min-width:18px;height:18px;line-height:15px;padding:0 3px;text-align:center;border-radius:9px;border:1.5px solid #fff;box-shadow:0 1px 2px rgba(0,0,0,.45)}.grel .wl{font:bold 14px Helvetica,Arial,sans-serif;width:26px;height:26px;line-height:22px;text-align:center;border-radius:50%;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.45)}.grel .bt{position:absolute;top:8px;background:#fff;border:1px solid #222;font:12px Questrial,Helvetica,Arial,sans-serif;padding:4px 9px;cursor:pointer;z-index:3}
.grel.fs{position:fixed;inset:0;z-index:2147483000;border:0}.grel .grfs{display:none!important}.grel.fs .grfs,.grel.cfs .grfs{display:block!important}.grel .fsleg{position:absolute;top:0;bottom:0;left:0;width:min(340px,86vw);background:rgba(255,255,255,.82);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);border-right:1px solid #ddd;padding:52px 14px 14px;overflow:auto;z-index:4;transform:translateX(0);transition:transform .2s}.grel .fsleg.shut{transform:translateX(-100%)}.grel .fsleg .grleg{margin:0}.grel .fslb{position:absolute;top:8px;left:8px;z-index:5;background:#fff;border:1px solid #222;font:12px Questrial,Helvetica,Arial,sans-serif;padding:4px 9px;cursor:pointer}.grel .brand{position:absolute;top:auto;left:auto;width:auto;height:auto;pointer-events:none;right:12px;bottom:10px;z-index:3;font:12px Questrial,Helvetica,Arial,sans-serif;letter-spacing:.12em;color:#333;background:rgba(255,255,255,.75);padding:3px 8px}.grel .brand b{font-weight:700}
.grel .tourcap{position:absolute;left:12px;right:12px;top:48px;z-index:3;max-width:640px;background:rgba(255,255,255,.96);border:1px solid #222;box-shadow:0 2px 10px rgba(0,0,0,.25);padding:12px 16px 12px;font:17px/1.5 Questrial,Helvetica,Arial,sans-serif;color:#111;display:none;pointer-events:none}.grel .tourcap .ta{font-size:12.5px;letter-spacing:.14em;font-weight:700;color:#555}.grel .tourcap .tm{font-size:15px;line-height:1.45;color:#333;margin:4px 0 8px;padding:0 0 8px;border-bottom:1px solid #ddd}.grel .tourcap .tt{font-weight:700;font-size:20px;line-height:1.3;margin:3px 0 4px}.grel .tourcap .tp{height:4px;background:#e4e1d8;margin-top:10px}.grel .fslay{position:absolute;top:46px;z-index:4;margin:0!important;padding:8px 10px;background:rgba(255,255,255,.88);border:1px solid #ccc;display:flex;flex-wrap:wrap;gap:6px;align-items:center}.grel .fslay .lhelp{display:none}.grel.touring .fslay{display:none!important}.grel .tourbar{position:absolute;bottom:44px;left:50%;transform:translateX(-50%);z-index:4;display:flex;gap:10px;align-items:center}.grel .tourbar .bt{position:static}.grel .tourbar .tpb{font:bold 17px Questrial,Helvetica,Arial,sans-serif;padding:11px 24px 11px 20px;background:#111;color:#fff;border:2px solid #fff;border-radius:28px;box-shadow:0 2px 10px rgba(0,0,0,.35);letter-spacing:.02em}.grel .tourbar .tpb::before{content:'\\25B6';display:inline-block;margin-right:10px;font-size:14px}.grel .tourbar .tpb[data-st=pause]::before{content:'\\275A\\275A';font-size:12px;letter-spacing:-2px}.grel .tourbar .tpb:hover{background:#7a1d12}.grel .tourbar .tpe{font:14px Questrial,Helvetica,Arial,sans-serif;padding:8px 14px;border-radius:20px;background:#fff;border:1px solid #222;display:none}.grel .tourcap .tp i{display:block;height:3px;background:#111;width:0}
.grel .walkbar{display:flex;gap:8px;align-items:center;margin-top:9px}
.grel .walkbar .bt{position:static;font:14px Questrial,Helvetica,Arial,sans-serif;padding:7px 14px;border-radius:18px;background:#fff;border:1px solid #222}
.grel .walkbar .bt.wnx{background:#111;color:#fff;border-color:#fff;font-weight:700;box-shadow:0 2px 8px rgba(0,0,0,.3)}
.grel .walkbar .bt:disabled{opacity:.35;cursor:default}
.grel .bt.wgo{font-weight:700;background:#111;color:#fff;border-color:#111}
.grel.walking .tourcap{display:block!important;pointer-events:auto;z-index:6;top:44px;max-width:min(620px,calc(100% - 24px));font-size:15px;padding:9px 13px}
.grel.walking .tourcap .tt{font-size:17px}
.grel.walking .tourcap .tx{font-size:14px;line-height:1.4;color:#333;max-height:4.3em;overflow:hidden}
.grel .tourcap .wk{display:flex;flex-wrap:wrap;gap:3px 2px;margin-top:8px;padding-top:7px;border-top:1px solid #ddd;font:12px/1.2 Helvetica,Arial,sans-serif}
.grel .tourcap .wk span{cursor:pointer;padding:2px 5px;border-radius:9px;border:1px solid #bbb;color:#888;background:#fff;white-space:nowrap}
.grel .tourcap .wk span.dn{color:#111;border-color:#111}
.grel .tourcap .wk span.at{color:#111;background:#f2b400;border-color:#111;font-weight:700}
.grel .tourcap .wk span.fr{color:#fff;background:#111;border-color:#111;font-weight:700}
.grel .tourcap .wk i{color:#999;font-style:normal;padding:2px 0}
.grbrand{text-align:right;margin:5px 2px 0;font:12px Questrial,Helvetica,Arial,sans-serif;letter-spacing:.12em;color:#333}.grbrand b{font-weight:700}
.grel .attr{position:absolute;left:6px;bottom:4px;z-index:3;font:10px Helvetica,Arial,sans-serif;color:#333;background:rgba(255,255,255,.75);padding:1px 6px;pointer-events:none}.grel .busy{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#888;font:13px Questrial,Helvetica,Arial,sans-serif}
.grleg{margin:8px 0 2px;font-size:12.5px;line-height:1.45;color:#333}
.grleg .r{display:flex;gap:8px;align-items:flex-start;margin:3px 0}
.grleg i{flex:0 0 26px;height:12px;border-radius:2px;margin-top:2px;border:1px solid #ccc}
.grleg b{letter-spacing:.12em;font-size:11px;display:block;margin:6px 0 2px}
.grleg .grlf>summary{cursor:pointer;font-size:12.5px;color:#666;text-decoration:underline;margin:2px 0}`;function Vn(i,t){let e=i*374761393+t*668265263;return e=(e^e>>>13)*1274126177,((e^e>>>16)>>>0)/4294967295}function vi(i,t){let e=Math.floor(i),n=Math.floor(t),s=i-e,r=t-n,a=s*s*(3-2*s),o=r*r*(3-2*r),l=Vn(e,n),c=Vn(e+1,n),h=Vn(e,n+1),f=Vn(e+1,n+1);return l+(c-l)*a+(h-l)*o+(l-c-h+f)*a*o}function Ji(i,t,e=5){let n=0,s=.5,r=1;for(let a=0;a<e;a++)n+=s*vi(i*r,t*r),r*=2.03,s*=.5;return n}function Tx(i,t,e=4){let n=0,s=.5,r=1;for(let a=0;a<e;a++){let o=1-Math.abs(vi(i*r,t*r)*2-1);n+=s*o*o,r*=2.1,s*=.5}return n}var Ue=(i,t,e)=>{let n=Math.min(1,Math.max(0,(e-i)/(t-i)));return n*n*(3-2*n)},bn=(i,t,e)=>[i[0]+(t[0]-i[0])*e,i[1]+(t[1]-i[1])*e,i[2]+(t[2]-i[2])*e];function wx(i,t){let[e,n,s]=i.map(x=>x/255),r=Math.max(e,n,s),a=Math.min(e,n,s),o=(r+a)/2,l=0,c=0,h=r-a;h>1e-6&&(l=o>.5?h/(2-r-a):h/(r+a),c=r===e?(n-s)/h+(n<s?6:0):r===n?(s-e)/h+2:(e-n)/h+4,c/=6),l=Math.min(1,l*1.5+.08),o=t?Math.min(.36,Math.max(.24,o)):Math.min(.62,Math.max(.42,o));let f=o<.5?o*(1+l):o+l-o*l,d=2*o-f,p=x=>(x=(x+1)%1,x<1/6?d+(f-d)*6*x:x<.5?f:x<2/3?d+(f-d)*(2/3-x)*6:d);return[p(c+1/3)*255,p(c)*255,p(c-1/3)*255]}var $d=new Map;function Ax(i){let t=0;for(let e=0;e<i.hn.length;e+=97)t+=i.hn[e]*(e+1);return i.VX+","+i.VY+","+i.notes.length+","+t.toFixed(4)+","+i.notes.map(e=>e.k+":"+e.e+":"+Math.round(e.x)+":"+Math.round(e.y)).join(";")}function Rx(i,t){if(!document.getElementById("gsm-relcss")){let u=document.createElement("style");u.id="gsm-relcss",u.textContent=Ex,document.head.appendChild(u)}let e=t.VX,n=t.VY,s=t.CX,r=t.CY,a=(e-1)*s,o=(n-1)*r,l=58,c=.45,h=t.place||null,f=document.createElement("div");f.className="grel pnet",i.appendChild(f);let d=document.createElement("div");d.className="lbs",f.appendChild(d);let p=document.createElement("div");p.className="attr",p.style.display="none",p.textContent="Imagery \xA9 Esri, Maxar, Earthstar Geographics, and the GIS User Community \xB7 Powered by Esri",f.appendChild(p);let x=document.createElement("div");x.className="busy",x.textContent="Building the land\u2026",f.appendChild(x);let S=document.createElement("div");S.className="grbrand",S.innerHTML="<b>THE BEAR CANYON METHOD</b> \xB7 BY OPERATIONAL COHERENCE",i.appendChild(S);let m=document.createElement("div");m.className="grleg",i.appendChild(m);function g(u,M,R){let I=Math.max(0,Math.min(e-1.001,M/s)),F=Math.max(0,Math.min(n-1.001,R/r)),z=I|0,J=F|0,ot=I-z,ut=F-J,et=(Z,ht)=>u[ht*e+Z];return et(z,J)*(1-ot)*(1-ut)+et(z+1,J)*ot*(1-ut)+et(z,J+1)*(1-ot)*ut+et(z+1,J+1)*ot*ut}let E=(u,M)=>g(t.hn,u,M)*l,P=h?156543.03392*Math.cos(Math.atan(Math.sinh(Math.PI*(1-2*(h.Y0+o/2/h.k)/256))))/h.k:1,T=h&&h.elev&&h.elev.hi>h.elev.lo?(h.elev.hi-h.elev.lo)/P:0,C=T?Math.max(1,Math.min(2.5,140/T)):2.5,A=C>1.05?"with heights exaggerated "+Math.round(C*10)/10+"\xD7 so its slopes and benches show":"true to scale";function _(u,M){let R=Math.floor(u),I=Math.floor(M),F=9,z=9,J=0;for(let ot=-1;ot<=1;ot++)for(let ut=-1;ut<=1;ut++){let et=R+ot,Z=I+ut,ht=et+Vn(et,Z)-u,lt=Z+Vn(Z+71,et+13)-M,yt=ht*ht+lt*lt;yt<F?(z=F,F=yt,J=Vn(et+5,Z+3)):yt<z&&(z=yt)}return[Math.sqrt(F),Math.sqrt(z),J]}let b=6,G=(u,M,R)=>{let I=R/b+u*.025-M*.012+(Ji(u*.05+11,M*.05,3)-.5)*1.8;return I+.3*Math.sin(I*2.1+1.3)+.12*Math.sin(I*4.7)};function B(u,M){if(h)return h.elev?h.elev(u,M)/P*C:0;let R=.6,I=(E(u+R,M)-E(u-R,M))/(2*R),F=(E(u,M+R)-E(u,M-R))/(2*R),z=Math.hypot(I,F),J=Ue(.25,1.1,z),ot=z>1e-4?-F/z:1,ut=z>1e-4?I/z:0,et=u*ot+M*ut,Z=(u*I+M*F)/(z||1),ht=(Tx(et*.18+vi(u*.04,M*.04)*2,Z*.025,3)-.4)*1.6*J,lt=E(u,M),yt=G(u,M,lt),xt=Math.floor(yt),Tt=yt-xt,Mt=.2+.8*Ue(.55,.7,Vn(xt+77,31)*.6+vi(u*.035+xt*1.7,M*.035-xt*.9)*.7),Jt=Ue(.5,1.25,z)*Ue(.2,.45,Ji(et*.07+xt*3.7,Z*.05+5,3)),We=(Ue(.68,.9,Tt)-Tt+.29)*b*.95*Jt*Mt;return lt+ht*(1-.5*Jt)+We+(Ji(u*.08+3,M*.08+7,4)-.5)*1.1*(1-.8*Jt)+(Ji(u*.35,M*.35,3)-.5)*.3*(1-.6*Jt)}let k=h?2:3,H=k*(e-1)+1,K=k*(n-1)+1,U=Ax(t),Y=$d.get(U)||{},tt=Y.hGrid||new Float32Array(H*K),j=1e9;if(!Y.hGrid)for(let u=0;u<K;u++)for(let M=0;M<H;M++){let R=B(M/(H-1)*a,u/(K-1)*o);tt[u*H+M]=R}for(let u=0;u<tt.length;u++)tt[u]<j&&(j=tt[u]);Y.hGrid=tt,$d.set(U,Y);let dt=j-7;function V(u,M){let R=Math.max(0,Math.min(H-1.001,u/a*(H-1))),I=Math.max(0,Math.min(K-1.001,M/o*(K-1))),F=R|0,z=I|0,J=R-F,ot=I-z,ut=(et,Z)=>tt[Z*H+et];return ut(F,z)*(1-J)*(1-ot)+ut(F+1,z)*J*(1-ot)+ut(F,z+1)*(1-J)*ot+ut(F+1,z+1)*J*ot}let it=t.emo.length,ft=t.emo.map(u=>/accept/i.test(u[0])?0:/indiff/i.test(u[0])?1:/distrust/i.test(u[0])?2:/aggress/i.test(u[0])?3:4),Gt=ft.indexOf(4),ee=t.notes.filter(u=>u.e!=null),at=t.emo.map((u,M)=>wx(u[1],M===Gt)),It=ft.indexOf(1),Ft=[];if(It>=0&&!h){let u=ee.filter(F=>F.e===It),M=u.map((F,z)=>z),R=F=>M[F]===F?F:M[F]=R(M[F]),I=[];for(let F=0;F<u.length;F++)for(let z=F+1;z<u.length;z++)I.push([Math.hypot(u[F].x-u[z].x,u[F].y-u[z].y),F,z]);I.sort((F,z)=>F[0]-z[0]).forEach(([F,z,J])=>{F>95||R(z)===R(J)||(M[R(z)]=R(J),Ft.push([u[z].x,u[z].y,u[J].x,u[J].y]))})}let qt=(u,M)=>{let R=0;return Ft.forEach(([I,F,z,J])=>{let ot=z-I,ut=J-F,et=Math.max(0,Math.min(1,((u-I)*ot+(M-F)*ut)/(ot*ot+ut*ut||1))),Z=(I+et*ot-u)**2+(F+et*ut-M)**2;R+=2.4*Math.exp(-Z/(2*8*8))}),R},pt={w:150};pt.h=Math.round(pt.w*o/a),pt.a=new Float32Array(pt.w*pt.h*(it+3));for(let u=0;u<pt.h;u++)for(let M=0;M<pt.w;M++){let R=M/(pt.w-1)*a,I=u/(pt.h-1)*o,F=new Float32Array(it),z=(u*pt.w+M)*(it+3);ee.forEach(Tt=>{F[Tt.e]+=Math.exp(-((Tt.x-R)**2+(Tt.y-I)**2)/(2*26*26))}),Ft.length&&(F[It]+=qt(R,I));let J=0,ot=0;for(let Tt=0;Tt<it;Tt++){let Mt=(F[Tt]*(Tt===Gt?1.6:1))**2.2;pt.a[z+Tt]=Mt,ot+=Mt,J+=F[Tt]}for(let Tt=0;Tt<it;Tt++)pt.a[z+Tt]/=ot||1;pt.a[z+it]=Ue(.04,.5,J),pt.a[z+it+2]=Ft.length?Ue(.9,2,qt(R,I)):0;let ut=[...F.keys()].sort((Tt,Mt)=>F[Mt]-F[Tt]),et=ut[0],Z=ut[1],ht=F[et],lt=F[Z];pt.a[z+it+1]=Math.abs(ft[et]-ft[Z])<2||ft[et]===1||ft[Z]===1||lt<.03?0:Ue(.22,.42,lt/(ht+lt));let yt=-1,xt=0;if(ee.forEach(Tt=>{let Mt=Math.exp(-((Tt.x-R)**2+(Tt.y-I)**2)/128);Mt>xt&&(xt=Mt,yt=Tt.e)}),yt>=0){let Tt=Ue(.25,.7,xt)*(1-pt.a[z+yt]);if(Tt>.001){for(let Mt=0;Mt<it;Mt++)pt.a[z+Mt]=pt.a[z+Mt]*(1-Tt)+(Mt===yt?Tt:0);pt.a[z+it+1]*=1-Tt,yt!==It&&(pt.a[z+it+2]*=1-Tt),pt.a[z+it]=Math.max(pt.a[z+it],Tt)}}}function oe(u,M){let R=Math.min(pt.w-1.001,u/a*(pt.w-1)),I=Math.min(pt.h-1.001,M/o*(pt.h-1)),F=R|0,z=I|0,J=R-F,ot=I-z,ut=(ht,lt,yt)=>pt.a[(lt*pt.w+ht)*(it+3)+yt],et=ht=>ut(F,z,ht)*(1-J)*(1-ot)+ut(F+1,z,ht)*J*(1-ot)+ut(F,z+1,ht)*(1-J)*ot+ut(F+1,z+1,ht)*J*ot,Z=[0,0,0];for(let ht=0;ht<it;ht++){let lt=et(ht);Z=[Z[0]+at[ht][0]*lt,Z[1]+at[ht][1]*lt,Z[2]+at[ht][2]*lt]}return[Z,et(it),et(it+1),et(it+2)]}let $t=h?2560:1600,zt=Math.round($t*o/a),Se=Y.tcv||document.createElement("canvas");Y.tcv||(Se.width=$t,Se.height=zt);let ye=h?null:Y.ncv||document.createElement("canvas");ye&&!Y.ncv&&(ye.width=$t,ye.height=zt);let he=h?null:Y.mcv||document.createElement("canvas");he&&!Y.mcv&&(he.width=$t,he.height=zt);let Je=k,Xe=Math.floor((H-1)/Je)+1,_n=Math.floor((K-1)/Je)+1,ke=Y.hao||new Float32Array(Xe*_n);if(!h&&!Y.hao)for(let u=0;u<_n;u++)for(let M=0;M<Xe;M++){let R=Math.min(a,M*Je/(H-1)*a),I=Math.min(o,u*Je/(K-1)*o),F=V(R,I),z=0;for(let J=0;J<8;J++){let ot=J*Math.PI/4+.3,ut=Math.cos(ot),et=Math.sin(ot),Z=0;for(let ht of[1.5,3,5,8,12,17,24]){let lt=R+ut*ht,yt=I+et*ht;if(lt<0||yt<0||lt>a||yt>o)break;Z=Math.max(Z,(V(lt,yt)-F)/ht)}z+=Z/Math.sqrt(1+Z*Z)}ke[u*Xe+M]=z/8}h||(Y.hao=ke);let Kn=(u,M)=>{let R=Math.max(0,Math.min(Xe-1.001,u/a*(H-1)/Je)),I=Math.max(0,Math.min(_n-1.001,M/o*(K-1)/Je)),F=R|0,z=I|0,J=R-F,ot=I-z,ut=(et,Z)=>ke[Z*Xe+et];return ut(F,z)*(1-J)*(1-ot)+ut(F+1,z)*J*(1-ot)+ut(F,z+1)*(1-J)*ot+ut(F+1,z+1)*J*ot};function on(u){let M=Se.getContext("2d"),R=M.createImageData($t,zt),I=R.data,F=u&&u.data,z=ye?new Float32Array($t*zt):null,J=ye?new Uint8Array($t*zt):null,ot=[98,108,62],ut=[140,134,86],et=[124,96,66],Z=[86,68,50],ht=[122,118,112],lt=[168,160,148],yt=Me=>.3*Me[0]+.59*Me[1]+.11*Me[2],xt=[184,170,150],Tt=[176,144,126],Mt=[150,146,140],Jt=[158,156,108],We=[104,96,88],ue=[150,138,94],Ee=[100,112,64],Pe=[66,80,50],ne=[142,98,70],Te=[100,74,56],Qe=[170,156,138];for(let Me=0;Me<zt;Me++)for(let ce=0;ce<$t;ce++){let Yt=ce/($t-1)*a,jt=Me/(zt-1)*o,Ne=a/$t*1.5,Wn=V(Yt,jt),Qi=(V(Yt+Ne,jt)-V(Yt-Ne,jt))/(2*Ne),dn=(V(Yt,jt+Ne)-V(Yt,jt-Ne))/(2*Ne),Tn=Math.hypot(Qi,dn),$l=V(Yt+3*Ne,jt)+V(Yt-3*Ne,jt)+V(Yt,jt+3*Ne)+V(Yt,jt-3*Ne)-4*Wn,Ra=Ji(Yt*.08,jt*.08,4),jl=vi(Yt*1.7,jt*1.7),Ca=Vn(ce,Me),Lr=Ji(Yt*.05+9,jt*.05,4),ci=Ue(.55,1.15,Tn+(Ra-.5)*.5),zs=Ue(.25,.55,Tn+(Ra-.5)*.6)*(1-ci),[ts,uf,Hs,Vh]=oe(Yt,jt);h&&(Hs=0);let Pa,Ia,Nr,Wh=0,Ql=0;if(h)Pa=bn(ot,ut,Ue(.35,.75,Lr)),Ia=bn(et,Z,Ue(-.2,-.9,Wn/l)*.8),Nr=bn(ht,lt,jl*.7).map(an=>an*(.92+.08*vi(Yt*.6,jt*.6)));else{let an=Math.max(ci,Hs),Ss=Math.min(1,zs+Ue(-.4,-1,Wn/l)*.5*(1-ci));if(Nr=Ia=Pa=[0,0,0],an>.003){let es=Tn>1e-4?-dn/Tn:1,Ni=Tn>1e-4?Qi/Tn:0,hi=Yt*es+jt*Ni,ec=(Yt*Qi+jt*dn)/(Tn||1),Na=G(Yt,jt,E(Yt,jt)),Da=Na*3,ns=Math.floor(Na),Xh=Da-Math.floor(Da),qh=Vn(ns+300,17),mf=Ue(.45,.6,Na-ns)*(1-Ue(.9,.97,Na-ns)),gf=qh<.42?bn(xt,Mt,Vn(ns+9,4)*.5):qh<.75?bn(Tt,xt,Vn(ns+2,8)*.6):bn(Mt,Tt,Vn(ns+5,1)*.4),Yh=Ue(.78,.98,Xh),Zh=1-Ue(0,.07,Xh),[_f,xf]=_(hi*.42+Da*.35,Da*.9+hi*.05),nc=1-Ue(.015,.09,xf-_f),Jh=(1-Ue(0,.06,Math.abs(Math.sin(hi*.55+(vi(Yt*.2,jt*.2)-.5)*4))))*Ue(.55,.75,Vn(ns+40,2)),yf=Ue(.62,.72,Ji(Yt*.22+40,jt*.22,3))*(1-nc)*.4,vf=Ue(.62,.82,vi(hi*1.1,ec*.07+ns*.3))*.3,Kh=Ji(Yt*2.2,jt*2.2,3)-.5;Nr=bn(bn(gf,Jt,yf),We,Math.max(vf,nc*.2,Jh*.15,Yh*.2,mf*.22)).map(Mf=>Mf*(1+Kh*.1)*(1+Zh*.04)),Wh=(-.32*Yh+.08*Zh-.45*nc-.25*Jh+.36*Kh)*.3}if(Ss>.003&&ci<.997){let[es,,Ni]=_(Yt*1.6,jt*1.6),hi=Ue(.3,.16,es)*Ue(.62,.75,Ni);Ia=bn(bn(ne,Te,Ue(-.2,-.9,Wn/l)*.8+(vi(Yt*.3,jt*.3)-.5)*.5),Qe.map(ec=>ec*(.8+.25*Ni)),hi*.55),Ql+=.1*hi*Ss}if(Ss<.997&&ci<.997){let es=vi(Yt*6.5,jt*6.5)*.65+vi(Yt*13.1,jt*13.1)*.35,Ni=Ji(Yt*.6+7,jt*.6-3,2);Pa=bn(bn(Ee,ue,Ue(.3,.7,Lr)),Pe,Ue(.55,.85,Ni)*.3).map(hi=>hi*(.94+.12*es)),Ql+=(.06*(es-.5)+.08*(Ni-.5))*(1-Ss)}}let tc=(Me*$t+ce)*4,wn=F?[F[tc],F[tc+1],F[tc+2]]:bn(bn(Pa,Ia,zs+Ue(-.4,-1,Wn/l)*.5*(1-ci)),Nr,ci),df=F?1:h?.93+.14*Ca:.96+.08*Ca;wn=wn.map(an=>an*df);let Gs=Math.max(-.28,Math.min(.18,-$l*(h?.5:.11)));if(!h){Gs=Math.max(-.42,Gs*.7-Kn(Yt,jt)*.5);let an=V(Yt+Ne,jt)+V(Yt-Ne,jt)+V(Yt,jt+Ne)+V(Yt,jt-Ne)-4*Wn;Gs+=Math.min(.1,Math.max(0,-an-.02)*.6)*Ue(.15,.5,Tn)}if(wn=wn.map(an=>an*(1+Gs)),h){let an=(V(Yt+Ne,jt)-V(Yt-Ne,jt))/(2*Ne),Ss=(V(Yt,jt+Ne)-V(Yt,jt-Ne))/(2*Ne),es=Math.hypot(an,Ss,1),Ni=((an+Ss)*.7071+1)*.7071/es/.7071-1;wn=wn.map(hi=>Math.min(255,hi*(1+Math.max(-.45,Math.min(.3,Ni*.9)))))}Hs>.01&&(wn=bn(wn,Nr.map(an=>an*(1+Gs)),Hs*.85));let ff=yt(wn),pf=yt(ts)||1;wn=bn(wn,h?ts:ts.map(an=>Math.min(255,an*ff/pf*1.05)),(h?.42:c)*uf*(1-Hs)),Vh>.01&&(wn=bn(wn,at[It].map(an=>an*(.9+.1*(1+Gs))),.8*Vh));let La=(Me*$t+ce)*4;if(I[La]=wn[0],I[La+1]=wn[1],I[La+2]=wn[2],I[La+3]=255,z){let an=Math.max(ci,Hs);z[Me*$t+ce]=Ql*(1-an)+Wh*an,J[Me*$t+ce]=an*255}}if(M.putImageData(R,0,0),z){let Me=ye.getContext("2d"),ce=Me.createImageData($t,zt),Yt=ce.data,jt=.5/(a/$t);for(let dn=0;dn<zt;dn++)for(let Tn=0;Tn<$t;Tn++){let $l=z[dn*$t+Math.max(0,Tn-1)],Ra=z[dn*$t+Math.min($t-1,Tn+1)],jl=z[Math.max(0,dn-1)*$t+Tn],Ca=z[Math.min(zt-1,dn+1)*$t+Tn],Lr=-(Ra-$l)/2*jt,ci=(Ca-jl)/2*jt,zs=Math.hypot(Lr,ci,1),ts=(dn*$t+Tn)*4;Yt[ts]=(Lr/zs*.5+.5)*255,Yt[ts+1]=(ci/zs*.5+.5)*255,Yt[ts+2]=(1/zs*.5+.5)*255,Yt[ts+3]=255}Me.putImageData(ce,0,0);let Ne=he.getContext("2d"),Wn=Ne.createImageData($t,zt),Qi=Wn.data;for(let dn=0;dn<J.length;dn++)Qi[4*dn]=Qi[4*dn+1]=Qi[4*dn+2]=J[dn],Qi[4*dn+3]=255;Ne.putImageData(Wn,0,0)}}Y.tcv||on(null),Y.tcv=Se,ye&&(Y.ncv=ye,Y.mcv=he);function Un(){if(!h)return;if(Y.placed){p.style.display="";return}let u=a/h.k,M=Math.max(1,Math.min(18,Math.round(Math.log2($t*1.3/u)))),R,I,F,z,J=()=>{let lt=2**M;R=Math.floor(h.X0*lt/256),I=Math.floor((h.X0+u)*lt/256),F=Math.floor(h.Y0*lt/256),z=Math.floor((h.Y0+o/h.k)*lt/256)};for(J();(I-R+1)*(z-F+1)>64&&M>1;)M--,J();let ot=2**M,ut=$t/(u*ot),et=zt/(o/h.k*ot),Z=(lt,yt)=>new Promise(xt=>{let Tt=document.createElement("canvas");Tt.width=$t,Tt.height=zt;let Mt=Tt.getContext("2d");yt&&(Mt.fillStyle="#c9c4b8",Mt.fillRect(0,0,$t,zt));let Jt=(I-R+1)*(z-F+1),We=0,ue=()=>{--Jt===0&&xt(We?Tt:null)};setTimeout(()=>{Jt=1,ue()},2e4);for(let Ee=R;Ee<=I;Ee++)for(let Pe=F;Pe<=z;Pe++){let ne=new Image;ne.crossOrigin="anonymous",ne.onload=()=>{try{Mt.drawImage(ne,(Ee*256-h.X0*ot)*ut,(Pe*256-h.Y0*ot)*et,256*ut+1,256*et+1),We++}catch{}ue()},ne.onerror=ue,ne.src=lt.replace("{z}",M).replace("{y}",Pe).replace("{x}",Ee)}}),ht="https://server.arcgisonline.com/ArcGIS/rest/services/";Promise.all([Z(ht+"World_Imagery/MapServer/tile/{z}/{y}/{x}",1),Z(ht+"Reference/World_Transportation/MapServer/tile/{z}/{y}/{x}"),Z(ht+"Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}")]).then(([lt,yt,xt])=>{if(!Ta)return;let Tt=null;try{Tt=lt&&lt.getContext("2d").getImageData(0,0,$t,zt)}catch{Tt=null}Tt&&on(Tt);let Mt=Se.getContext("2d");[yt,xt].forEach(Jt=>{if(Jt)try{Mt.drawImage(Jt,0,0)}catch{}}),(h.areas||[]).forEach(Jt=>{if(!Jt.pts||Jt.pts.length<3)return;Mt.beginPath(),Jt.pts.forEach((ue,Ee)=>Mt[Ee?"lineTo":"moveTo"](ue[0]/a*$t,ue[1]/o*zt)),Mt.closePath();let We=Jt.e==null?[255,255,255]:at[Jt.e];Mt.fillStyle=`rgba(${We.map(ue=>ue|0).join(",")},0.5)`,Mt.fill(),Mt.lineJoin="round",Mt.lineWidth=10,Mt.strokeStyle="rgba(255,255,255,0.9)",Mt.stroke(),Mt.lineWidth=5,Mt.strokeStyle=`rgb(${We.map(ue=>ue*.7|0).join(",")})`,Mt.stroke()}),Tt&&(Y.placed=1,p.style.display=""),W.needsUpdate=!0,Ye=!0})}let pe=new Ul({antialias:!0,preserveDrawingBuffer:!0});pe.setPixelRatio(Math.min(2,window.devicePixelRatio||1)),pe.shadowMap.enabled=!0,pe.shadowMap.type=h?Cs:qo,pe.outputColorSpace=fn,pe.toneMapping=ca,pe.toneMappingExposure=1.3,f.insertBefore(pe.domElement,d),x.remove();let Zt=new hr;Zt.background=new fe("#ffffff");let N=new In(30,1.6,1,5e3),me=new kl(N,pe.domElement);me.enableDamping=!0,me.maxPolarAngle=Math.PI*.47,me.minDistance=120,me.maxDistance=1400,Zt.add(h?new dr(16777215,10130308,1):new dr(14871541,9403494,.85));let we=new fr(h?16774890:16773340,3.3);h?we.position.set(-260,260,-160):we.position.set(-290,215,-175),we.castShadow=!0,we.shadow.mapSize.set(h?2048:4096,h?2048:4096),we.shadow.bias=-6e-4,we.shadow.normalBias=.6,Object.assign(we.shadow.camera,{left:-260,right:260,top:200,bottom:-200,near:10,far:900}),Zt.add(we);let ze=new fr(16777215,.9);if(ze.position.set(120,90,400),Zt.add(ze),!h){let u=new hr,M=new Xi(10,32,16),R=new ai({side:vn,vertexShader:"varying vec3 d; void main(){ d = position; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }",fragmentShader:"varying vec3 d; void main(){ float y = normalize(d).y; vec3 c = y > 0.0 ? mix(vec3(0.95, 0.93, 0.88), vec3(0.55, 0.68, 0.88), pow(y, 0.6)) : mix(vec3(0.62, 0.52, 0.42), vec3(0.32, 0.27, 0.22), -y); gl_FragColor = vec4(c * 1.4, 1.0); }"});u.add(new Qt(M,R));let I=new Sr(pe);Zt.environment=I.fromScene(u,.02).texture,Zt.environmentIntensity=.3,I.dispose()}let Rt={n:{value:1e5},f:{value:2e5}},en=()=>{if(!h){let u=N.position.distanceTo(me.target);Rt.n.value=u*.9,Rt.f.value=u*1.5}pe.render(Zt,N)},Pt=u=>u-a/2,Dt=u=>u-o/2,w=new Wi(a,o,H-1,K-1);w.rotateX(-Math.PI/2);let y=w.attributes.position;for(let u=0;u<H*K;u++)y.setY(u,tt[u]);w.computeVertexNormals();let W=new wi(Se);W.colorSpace=fn,W.anisotropy=8;let mt=new tn({map:W,roughness:.95});if(ye){let u=new wi(ye);u.anisotropy=8,mt.normalMap=u,mt.normalScale.set(1,1)}if(he){let u=new wi(he);mt.onBeforeCompile=M=>{M.uniforms.rockMask={value:u},M.vertexShader=M.vertexShader.replace("#include <common>",`#include <common>
varying vec3 vWP;`).replace("#include <worldpos_vertex>",`#include <worldpos_vertex>
vWP = (modelMatrix * vec4(transformed, 1.0)).xyz;`),M.fragmentShader=M.fragmentShader.replace("#include <common>",`#include <common>
varying vec3 vWP; uniform sampler2D rockMask;
float h3(vec3 p){ p = fract(p * 0.1031); p += dot(p, p.zyx + 31.32); return fract((p.x + p.y) * p.z); }
float n3(vec3 x){ vec3 i = floor(x), f = fract(x); f = f * f * (3.0 - 2.0 * f);
  return mix(mix(mix(h3(i), h3(i + vec3(1,0,0)), f.x), mix(h3(i + vec3(0,1,0)), h3(i + vec3(1,1,0)), f.x), f.y),
             mix(mix(h3(i + vec3(0,0,1)), h3(i + vec3(1,0,1)), f.x), mix(h3(i + vec3(0,1,1)), h3(i + vec3(1,1,1)), f.x), f.y), f.z); }
float rockH(vec3 p, float fw, out float tone){
  float s = p.y * 1.7 + p.x * 0.06 + (n3(p * 0.25) - 0.5) * 2.4, lay = floor(s), b = s - lay;
  tone = h3(vec3(lay, 3.0, 7.0));
  float h = smoothstep(0.72, 0.9, b) * 0.3 * smoothstep(0.5, 0.18, fw * 1.7);
  float a = 0.55, f = 1.1;
  for (int k = 0; k < 3; k++) { h += a * (n3(p * f + float(k) * 7.1) - 0.5) * smoothstep(0.45, 0.15, fw * f); f *= 2.15; a *= 0.5; }
  return h; }
vec3 bumpN(vec3 sp, vec3 n, float h){ vec3 dx = dFdx(sp), dy = dFdy(sp), r1 = cross(dy, n), r2 = cross(n, dx); float det = dot(dx, r1);
  vec3 g = sign(det) * (dFdx(h) * r1 + dFdy(h) * r2); return normalize(abs(det) * n - g); }
float rkM; float rkH; float rkT;`).replace("#include <map_fragment>",`#include <map_fragment>
rkM = texture2D(rockMask, vMapUv).r; { float fw = length(fwidth(vWP)); rkH = rockH(vWP, fw, rkT); }
diffuseColor.rgb *= mix(1.0, (0.86 + 0.28 * rkT) * (1.0 + rkH * 0.55), rkM);`).replace("#include <normal_fragment_maps>",`#include <normal_fragment_maps>
normal = bumpN(-vViewPosition, normal, rkH * rkM * 0.9);`).replace("#include <fog_fragment>",`#include <fog_fragment>
{ float hz = clamp((length(vViewPosition) - hazeN) / max(1.0, hazeF - hazeN), 0.0, 1.0); gl_FragColor.rgb = mix(gl_FragColor.rgb, vec3(0.86, 0.89, 0.93), hz * 0.2); }`).replace("uniform sampler2D rockMask;","uniform sampler2D rockMask; uniform float hazeN; uniform float hazeF;"),M.uniforms.hazeN=Rt.n,M.uniforms.hazeF=Rt.f}}let ct=new Qt(w,mt);ct.castShadow=ct.receiveShadow=!0,Zt.add(ct);function wt(u){let M=new Sn,R=[],I=[];u.forEach(F=>{R.push(Pt(F[0]),V(F[0],F[1]),Dt(F[1]),Pt(F[0]),dt,Dt(F[1]))});for(let F=0;F<u.length-1;F++){let z=2*F;I.push(z,z+1,z+2,z+2,z+1,z+3)}return M.setAttribute("position",new Be(R,3)),M.setIndex(I),M.computeVertexNormals(),M}let Ct=new tn({color:1907738,roughness:1,side:zn}),rt=200,st={s:[],n:[],w:[],e:[]};for(let u=0;u<=rt;u++){let M=u/rt;st.s.push([M*a,o]),st.n.push([a-M*a,0]),st.w.push([0,M*o]),st.e.push([a,o-M*o])}Object.values(st).forEach(u=>{let M=new Qt(wt(u),Ct);M.receiveShadow=!0,Zt.add(M)});{let u=1e9;st.s.forEach(R=>{u=Math.min(u,V(R[0],R[1]))});let M=u-dt;if(M>1.5){let R=document.createElement("canvas");R.width=2048,R.height=96;let I=R.getContext("2d");I.fillStyle="#d8d4cc",I.textAlign="center",I.textBaseline="middle",I.font="600 52px Helvetica, Arial, sans-serif";let F="The Bear Canyon Method by Operational Coherence";"letterSpacing"in I&&(I.letterSpacing="4px"),I.fillText(F,1024,50);let z=Math.min(2040,I.measureText(F).width+40),J=Math.min(M*.42,9),ot=J*R.width/R.height*.98,ut=new wi(R);ut.colorSpace=fn,ut.anisotropy=8;let et=new Qt(new Wi(Math.min(ot,a*.9),J),new kn({map:ut,transparent:!0,opacity:.85,depthWrite:!1}));ot>a*.9&&(et.scale.y=a*.9/ot),et.position.set(0,dt+M*.5,o/2+.25),J>=4&&Zt.add(et)}if(!(M>1.5)||Math.min(M*.42,9)<4){let R=document.createElement("canvas");R.width=2048,R.height=96;let I=R.getContext("2d");I.fillStyle="#55524c",I.textAlign="center",I.textBaseline="middle",I.font="600 52px Helvetica, Arial, sans-serif","letterSpacing"in I&&(I.letterSpacing="4px"),I.fillText("The Bear Canyon Method by Operational Coherence",1024,50);let F=new wi(R);F.colorSpace=fn,F.anisotropy=8;let z=7,J=Math.min(z*R.width/R.height*.98,a*.9),ot=new kn({map:F,transparent:!0,opacity:.85,depthWrite:!1}),ut=new Qt(new Wi(J,z*J/(z*R.width/R.height*.98)),ot);ut.rotation.x=-Math.PI/2,ut.position.set(0,dt+.05,o/2+8),Zt.add(ut)}}let bt=new Qt(new mi(a+30,4,o+30),new tn({color:15658732,roughness:.9}));bt.position.y=dt-2,bt.receiveShadow=!0,Zt.add(bt);let L=[],nt=new tn({color:1118481,roughness:.6});function Q(u,M,R,I,F,z,J,ot,ut){let et=document.createElement("div");et.className="lb "+M+(ut?" hit":""),et.textContent=u,d.appendChild(et);let Z={el:et,v:new D(Pt(R),V(R,I)+F,Dt(I)),pri:z,ax:J||0,ay:ot||0,info:ut};return L.push(Z),ut&&(et.addEventListener("mouseenter",ht=>{qe||oi(Z,ht)}),et.addEventListener("mouseleave",()=>{qe||$n()}),et.addEventListener("click",ht=>{ht.stopPropagation(),qe=qe===Z?null:Z,qe?oi(Z,ht):$n()})),Z}let St=[],vt=new ur({color:2236962,transparent:!0,opacity:.55}),_t=t.clusters||null,Wt={},de=[];_t&&_t.list.forEach((u,M)=>u.ks.forEach(R=>{Wt[R]=M}));let gt={},Xt=[];_t&&(t.read||[]).forEach((u,M)=>((u.text||"")+" "+(u.title||"")+" "+(u.cap||"")).replace(new RegExp("\\b"+(t.np||"N")+"(\\d+)\\b","g"),(R,I)=>((gt[+I]=gt[+I]||{})[M]=1,R)));function le(u){Xt.forEach(M=>{M.hid=!(u!=null&&M.rds[u]),M.hid&&(M.el.style.display="none")}),Ye=!0}t.notes.forEach(u=>{let M=V(u.x,u.y);if(_t){let J=Wt[u.k],ot=J!=null,ut=u.e==null?16777215:new fe(`rgb(${t.emo[u.e][1].join(",")})`),et=new tn({color:ut,roughness:.5,transparent:!0,opacity:ot?1:.5}),Z=new Qt(new Xi(ot?2.4:1.5,14,10),et);Z.position.set(Pt(u.x),M+(ot?7:4.5),Dt(u.y)),ot&&(Z.castShadow=!0),Zt.add(Z);let ht=new kn({color:16777215,side:vn,transparent:!0,opacity:ot?1:.5}),lt=new Qt(new Xi(ot?3.1:1.9,14,10),ht);lt.position.copy(Z.position),Zt.add(lt);let yt=null;ot&&(yt=new Qt(new Ai(.3,.3,7,6),nt),yt.position.set(Pt(u.x),M+3.5,Dt(u.y)),Zt.add(yt)),de.push({ci:ot?J:-1,m:et,rm:ht,st:yt,base:ot?1:.5});let xt={el:document.createElement("div")};gt[u.k]&&(xt=Q((t.np||"N")+u.k,"nl",u.x,u.y,ot?7:4.5,1,6,-8,{head:(t.np||"N")+u.k+" \xB7 "+(u.e==null?"no emotion marked":t.emo[u.e][0].toUpperCase())+(u.q?" \xB7 Q."+u.q:""),body:u.t||""}),xt.head=Z.position,xt.isN=1,xt.rds=gt[u.k],xt.hid=!0,xt.el.style.display="none",Xt.push(xt)),St.push({q:u.q,st:lt,hd:Z,lo:xt,sp:null}),yt&&St.push({q:u.q,st:yt,hd:Z,lo:{el:document.createElement("div")},sp:null});return}let R=new Qt(new Ai(.4,.4,10,6),nt);R.position.set(Pt(u.x),M+5,Dt(u.y)),R.castShadow=!0,Zt.add(R);let I=new Qt(new Xi(2.8,18,12),new tn({color:u.e==null?16777215:new fe(`rgb(${t.emo[u.e][1].join(",")})`),roughness:.5}));I.position.set(Pt(u.x),M+11,Dt(u.y)),I.castShadow=!0,Zt.add(I);let F=Q((t.np||"N")+u.k,"nl",u.x,u.y,11,1,6,-8,{head:(t.np||"N")+u.k+" \xB7 "+(u.e==null?"no emotion marked":t.emo[u.e][0].toUpperCase())+(u.q?" \xB7 Q."+u.q:""),body:u.t||""}),z=null;if(t.spokes&&u.q){let J=(t.qpos||[]).find(ot=>ot&&ot.q===u.q);if(J){let ot=[];for(let ut=0;ut<=24;ut++){let et=ut/24,Z=J.x+(u.x-J.x)*et,ht=J.y+(u.y-J.y)*et;ot.push(new D(Pt(Z),V(Z,ht)+1.4,Dt(ht)))}z=new $r(new Sn().setFromPoints(ot),vt),Zt.add(z)}}F.head=I.position,F.isN=1,St.push({q:u.q,st:R,hd:I,lo:F,sp:z})}),t.qpos.forEach(u=>{if(!u)return;let M=V(u.x,u.y),R=new Qt(new Ai(.55,.55,18,6),nt);R.position.set(Pt(u.x),M+9,Dt(u.y)),R.castShadow=!0,Zt.add(R);let I=new Qt(new mi(7,4.2,.6),nt);I.position.set(Pt(u.x)+3.2,M+16.4,Dt(u.y)),I.castShadow=!0,Zt.add(I),Q("Q."+u.q,"ql",u.x,u.y,16.4,2,-4,-10,{head:"Q."+u.q+(u.title?" \xB7 "+u.title:""),body:u.ans||"No answer written yet.",sm:u.n?"Placed at the middle of its "+u.n+" note"+(u.n>1?"s":"")+".":"No notes yet; placed on the line between present and goal."})});{let u=t.START,M=V(u.x,u.y),R=new Qt(new Ai(.6,.6,22,6),nt);R.position.set(Pt(u.x),M+11,Dt(u.y)),R.castShadow=!0,Zt.add(R);let I=new Qt(new mi(.5,7,11),new tn({color:3054405,roughness:.55}));I.position.set(Pt(u.x),M+18.5,Dt(u.y)+5.5),I.castShadow=!0,Zt.add(I),Q(h?"START":"PRESENT","pl",u.x,u.y,24,3,-30,-24,h?{head:"START",body:"The note farthest from the goal. The ways run from here to the goal."}:{head:"PRESENT",body:"Where things stand now. The ground runs from here toward the goal."})}let Lt=(u,M,R)=>{let I=[];for(let F=0;F<=64;F++){let z=F/64*Math.PI*2,J=u+Math.cos(z)*R,ot=M+Math.sin(z)*R;I.push(new D(Pt(J),V(J,ot)+.5,Dt(ot)))}return I},Ce=[];[22,14,6].forEach(u=>{let M=Lt(t.GOAL.x,t.GOAL.y,u);for(let R=0;R<64;R+=u>10?2:4)Ce.push(M[R])}),[22,14,6].forEach(u=>{let M=new ri(Lt(t.GOAL.x,t.GOAL.y,u),!0);Zt.add(new Qt(new Ri(M,80,1,6,!0),new tn({color:16777215}))),Zt.add(new Qt(new Ri(M,80,.5,6,!0),nt))});{let u=t.GOAL,M=V(u.x,u.y),R=new Qt(new Ai(.6,.6,16,6),nt);R.position.set(Pt(u.x),M+8,Dt(u.y)),Zt.add(R),R.scale.y=1.5,R.position.y=M+12;let I=document.createElement("canvas");I.width=96,I.height=64;{let J=I.getContext("2d");for(let ot=0;ot<6;ot++)for(let ut=0;ut<4;ut++)J.fillStyle=(ot+ut)%2?"#111111":"#ffffff",J.fillRect(ot*16,ut*16,16,16)}let F=new wi(I);F.colorSpace=fn,F.magFilter=cn;let z=new Qt(new mi(.5,8,12),new tn({map:F,roughness:.6}));z.position.set(Pt(u.x),M+20,Dt(u.y)+6),z.castShadow=!0,Zt.add(z),Q("GOAL","pl",u.x,u.y,25,3,-22,-22,{head:"GOAL",body:t.goalText||"No goal written yet."})}if(!h){let u=-1e9;for(let z=0;z<=60;z++)u=Math.max(u,V(0,z/60*20));Q("\u2191 HELP","side",0,2,0,4,-104,-10).v.set(Pt(-6),u+4,Dt(2)),Q("\u2193 HINDER","side hd",0,o-2,0,4,-128,-10).v.set(Pt(-6),(V(0,o-2)+dt)/2,Dt(o)),Q("\u2190 PRESENT","side ax",0,o,0,4,0,10).v.set(Pt(0),dt,Dt(o)+4),Q("FUTURE \u2192","side ax",a,o,0,4,-120,10).v.set(Pt(a),dt,Dt(o)+4)}let Ve=(t.read||[]).map((u,M)=>{let R=Q(String(M+1),"rdm",u.at[0],u.at[1],21,5,-11,-11,{head:M+1+" \xB7 "+(u.title||""),body:u.text||"",rd:M}),I=V(u.at[0],u.at[1]),F=new Qt(new Ai(.35,.35,20,6),nt);F.position.set(Pt(u.at[0]),I+10,Dt(u.at[1])),F.castShadow=!0,Zt.add(F);let z=new Qt(new Xi(2.6,16,12),nt);z.position.set(Pt(u.at[0]),I+21,Dt(u.at[1])),z.castShadow=!0,Zt.add(z);let J=new Qt(new Rs(2.7,.35,6,24),new tn({color:16777215}));return J.position.copy(z.position),Zt.add(J),R.rim=J,R.head=z.position,R}),Ke=document.createElement("div");Ke.className="tip",f.appendChild(Ke);let qe=null;function oi(u,M){if(un&&un.paused==null)return;Ke.innerHTML="";let R=document.createElement("b");R.textContent=u.info.head,Ke.appendChild(R);let I=String(u.info.body||"");if(Ke.appendChild(document.createTextNode(I.length>(u.info.long?900:420)?I.slice(0,400).replace(/\s+\S*$/,"")+"\u2026":I)),u.info.sm){let ot=document.createElement("div");ot.className="sm",ot.textContent=u.info.sm,Ke.appendChild(ot)}Ye=!0,Ke.style.display="block";let F=f.getBoundingClientRect(),z=(M?M.clientX:F.left)-F.left,J=(M?M.clientY:F.top)-F.top;Ke.style.left=Math.max(4+(parseFloat(d.style.left)||0),Math.min(F.width-Ke.offsetWidth-4,z+12))+"px",Ke.style.top=Math.max(4,J-10-Ke.offsetHeight)+"px",Ve.forEach((ot,ut)=>ot.el.classList.toggle("on",ut===u.info.rd)),Xt.length&&le(u.info.rd),t.onHL&&t.onHL(u.info.rd==null?null:u.info.rd),u.info.way&&re(u.info.way)}function $n(){Ye=!0,qe||re(null),Ke.style.display="none",Ve.forEach(u=>u.el.classList.remove("on")),Xt.length&&le(null),t.onHL&&t.onHL(null)}function Er(u){let M=pe.domElement.getBoundingClientRect(),R=u.clientX-M.left,I=u.clientY-M.top,F=null,z=20;return L.forEach(J=>{if(!J.info||J.sx==null||J.off)return;let ot=Math.hypot(J.sx-R,J.sy-I);ot<z&&(z=ot,F=J)}),F}let Tr=u=>{qe&&!f.contains(u.target)&&(qe=null,re(null),$n())};document.addEventListener("click",Tr,!0);let jn=null;pe.domElement.addEventListener("pointermove",u=>{if(u.buttons||qe)return;let M=Er(u);if(M){oi(M,u);return}let R=Vt(u);if(re(R),R){let I=t.routes.find(F=>F.key===R);oi({info:{head:R+" \xB7 "+I.name,body:I.text||""}},u)}else Ke.style.display!=="none"&&$n()}),pe.domElement.addEventListener("pointerdown",u=>{jn=[u.clientX,u.clientY]}),pe.domElement.addEventListener("pointerup",u=>{if(!jn||Math.hypot(u.clientX-jn[0],u.clientY-jn[1])>5)return;let M=Er(u);if(M){qe=M,oi(M,u);return}let R=Vt(u);if(R){let I=t.routes.find(F=>F.key===R);qe={info:{head:R+" \xB7 "+I.name,body:I.text||""}},re(R),oi(qe,u)}else{let I=t.onGround&&se(u),F=I&&t.onGround(I[0],I[1]);F?(qe={info:F},re(null),oi(qe,u)):(qe=null,re(null),$n())}}),pe.domElement.addEventListener("pointerleave",()=>{qe||(re(null),Ke.style.display!=="none"&&$n())});let Li={A:"#111111",B:"#f4f4f4",C:"#e0007a"},Qn={},Us=[];function Fn(u,M,R,I,F,z,J){F=F||0,z=z??1,I=I||Math.max(60,Math.min(1400,Math.ceil(u.getLength()*(z-F)/.7)));let ot=[],ut=[],et=[];for(let lt=0;lt<=I;lt++)ot.push(u.getPointAt(F+(z-F)*lt/I));let Z=(lt,yt)=>V(lt+a/2,yt+o/2);for(let lt=0;lt<=I;lt++){let yt=ot[Math.max(0,lt-1)],xt=ot[Math.min(I,lt+1)],Tt=xt.x-yt.x,Mt=xt.z-yt.z,Jt=Math.hypot(Tt,Mt)||1,We=-Mt/Jt,ue=Tt/Jt,Ee=J?M*(1-lt/I):M,Pe=Z(ot[lt].x,ot[lt].z);for(let ne of[-1,1]){let Te=ot[lt].x+We*Ee/2*ne,Qe=ot[lt].z+ue*Ee/2*ne;ut.push(Te,Math.max(Z(Te,Qe),Pe,Z((Te+ot[lt].x)/2,(Qe+ot[lt].z)/2))+R,Qe)}}for(let lt=0;lt<I;lt++){let yt=2*lt;et.push(yt,yt+1,yt+2,yt+1,yt+3,yt+2)}let ht=new Sn;return ht.setAttribute("position",new Be(ut,3)),ht.setIndex(et),ht.computeVertexNormals(),ht}let li=(u,M)=>(u.side=zn,u.transparent=!0,u.depthWrite=!1,u.polygonOffset=!0,u.polygonOffsetFactor=-M,u.polygonOffsetUnits=-M*2,u),wr=[];_t&&_t.list.forEach((u,M)=>{let R=t.notes.filter(Mt=>Wt[Mt.k]===M);if(!R.length)return;let I=R.reduce((Mt,Jt)=>Mt+Jt.x,0)/R.length,F=R.reduce((Mt,Jt)=>Mt+Jt.y,0)/R.length,z=Math.max(8,Math.min(60,Math.max(...R.map(Mt=>Math.abs(Mt.x-I)))+6)),J=Math.max(8,Math.min(45,Math.max(...R.map(Mt=>Math.abs(Mt.y-F)))+6)),ot=[];for(let Mt=0;Mt<72;Mt++){let Jt=Mt/72*Math.PI*2,We=Math.max(1,Math.min(a-1,I+Math.cos(Jt)*z)),ue=Math.max(1,Math.min(o-1,F+Math.sin(Jt)*J));ot.push(new D(Pt(We),V(We,ue),Dt(ue)))}let ut=new ri(ot,!0),et=new fe(`rgb(${t.emo[u.e][1].join(",")})`),Z=li(new tn({color:et,roughness:.8,opacity:1}),5),ht=li(new tn({color:16777215,roughness:.9,opacity:.85}),4),lt=Math.max(14,Math.round(ut.getLength()/7));for(let Mt=0;Mt<lt;Mt++){let Jt=Mt/lt,We=(Mt+.55)/lt,ue=new Qt(Fn(ut,3.4,3.2,12,Jt,We),ht);ue.renderOrder=4,Zt.add(ue);let Ee=new Qt(Fn(ut,2,3.4,12,Jt,We),Z);Ee.renderOrder=5,Zt.add(Ee)}let yt=Math.max(2,F-J),xt=Q("","clt",I,yt,3,4,0,-30,{head:u.head,body:u.body,long:1});xt.cen=1,xt.el.textContent="";let Tt=document.createElement("i");Tt.textContent=String(u.k),Tt.style.background=`rgb(${t.emo[u.e][1].join(",")})`,Tt.style.color=u.ink||"#fff",xt.el.appendChild(Tt),xt.el.appendChild(document.createTextNode(u.tag)),xt.el.addEventListener("click",()=>{t.onCluster&&t.onCluster(u.k)}),wr.push({k:u.k,mat:Z,wm:ht,tg:xt})});function ys(u){let M=_t?_t.list.findIndex(R=>R.k===u):-1;wr.forEach((R,I)=>{let F=M<0||_t.list[M]&&_t.list[M].k===R.k;R.mat.opacity=F?1:.25,R.wm.opacity=F?.85:.2,R.tg.el.style.opacity=F?"":"0.3"}),de.forEach(R=>{let I=M<0?R.base:R.ci===M?1:R.ci<0?.15:.22;R.m.opacity=I,R.rm.opacity=I,R.st&&(R.st.visible=M<0||R.ci===M)}),Ye=!0}let zl=(t.routes||[]).length,Ar=[],Rr=(u,M,R)=>{let I=1e9;return(t.routes||[]).forEach((F,z)=>{if(z!==R)for(let J=0;J<F.pts.length;J+=2)I=Math.min(I,Math.hypot(F.pts[J][0]-u,F.pts[J][1]-M))}),I};(t.routes||[]).forEach((u,M)=>{let R=(M-(zl-1)/2)*2.6,I=u.pts.map((ne,Te,Qe)=>{let Me=Qe[Math.max(0,Te-2)],ce=Qe[Math.min(Qe.length-1,Te+2)],Yt=ce[0]-Me[0],jt=ce[1]-Me[1],Ne=Math.hypot(Yt,jt)||1;return Rr(ne[0],ne[1],M)<4?[ne[0]-jt/Ne*R,ne[1]+Yt/Ne*R]:ne}),F=I.filter((ne,Te)=>Te%2===0||Te===I.length-1).map(ne=>new D(Pt(ne[0]),V(ne[0],ne[1])+1.6+M*.4,Dt(ne[1])));if(F.length<2)return;let z=new ri(F),J=new tn({color:Li[u.key]||"#111",roughness:.45,emissive:u.key==="B"?"#ffffff":"#000000",emissiveIntensity:u.key==="B"?.35:0,transparent:!0});J.roughness=.8,li(J,4+M);let ot=new Qt(Fn(z,3.4,1.1+M*.2),J);ot.receiveShadow=!0,ot.renderOrder=3+M*2,Zt.add(ot);let ut=new Qt(Fn(z,4.6,.9+M*.2),li(new tn({color:u.key==="B"?"#222":"#f3efe6",roughness:.9,transparent:!0,opacity:.8}),3+M));ut.receiveShadow=!0,ut.renderOrder=2+M*2,Zt.add(ut);let et=new Qt(new Ri(z,200,5,6),new kn({transparent:!0,opacity:0,depthWrite:!1}));et.userData.key=u.key,Zt.add(et),Us.push(et);let Z={head:u.key+" \xB7 "+u.name,body:u.text||"",way:u.key},ht=Math.floor(I.length/2),lt=-1;for(let ne=.2;ne<=.8;ne+=.04){let Te=Math.floor(I.length*ne),Qe=I[Te],Me=Math.min(Rr(Qe[0],Qe[1],M),40)+Math.min(40,...Ar.map(ce=>Math.hypot(ce[0]-Qe[0],ce[1]-Qe[1])),40)-Math.abs(ne-.5)*10;Me>lt&&(lt=Me,ht=Te)}Ar.push(I[ht]);let yt=[I[ht]].map(ne=>{let Te=Q(u.key,"wl",ne[0],ne[1],5,6,-13,-13,Z);return Te.el.style.background=Li[u.key],Te.el.style.color=u.key==="B"?"#111":"#fff",Te.el.style.borderColor=u.key==="B"?"#111":"#fff",Te}),xt=li(new kn({color:u.key==="B"?"#222222":"#ffffff",transparent:!0,opacity:.95}),3+M),Tt=[],Mt=z.getLength(),Jt=Math.max(2,Math.min(14,Math.round(Mt/42))),We=new D(0,1,0),ue=new D(Pt(I[ht][0]),0,Dt(I[ht][1]));for(let ne=0;ne<Jt;ne++){let Te=(ne+.5)/Jt,Qe=z.getPointAt(Te),Me=z.getTangentAt(Te).normalize();if(Math.hypot(Qe.x-ue.x,Qe.z-ue.z)<9)continue;let ce=11/Mt,Yt=Math.max(0,Te-ce*.4),jt=Math.min(1,Te+ce*.6),Ne=new Qt(Fn(z,9,1.5+M*.2,16,Yt,jt,!0),J);Ne.renderOrder=4+M*2,Zt.add(Ne),Tt.push(Ne);let Wn=new Qt(Fn(z,12.5,1.5+M*.2,16,Math.max(0,Yt-ce*.12),Math.min(1,jt+ce*.12),!0),xt);Wn.renderOrder=3+M*2,Zt.add(Wn),Tt.push(Wn)}let Ee=[],Pe=null;(u.stops||[]).slice(1,-1).forEach(ne=>{if(Pe&&Math.hypot(ne[0]-Pe[0],ne[1]-Pe[1])<3)return;Pe=ne;let Te=0,Qe=1e9;I.forEach((ce,Yt)=>{let jt=Math.hypot(ce[0]-ne[0],ce[1]-ne[1]);jt<Qe&&(Qe=jt,Te=Yt)});let Me=Q(String(Ee.length+1),"wn",I[Te][0],I[Te][1],4,7,-9,-9,null);Me.el.style.background=Li[u.key],Me.el.style.color=u.key==="B"?"#111":"#fff",Me.el.style.borderColor=u.key==="B"?"#111":"#fff",Me.hid=u.key!=="A",Ee.push(Me)}),Qn[u.key]={tube:ot,edge:ut,badges:yt,mat:J,arrows:Tt,shell:xt,nums:Ee,rp:I,ri:M,stops:u.stops||null,name:u.name}});let vs=new ii;Zt.add(vs);let Ma="",Hl=new tn({color:3809036,roughness:.5,emissive:2757125,emissiveIntensity:.4}),Sa=new tn({color:16777215,roughness:.8});function v(u){let M=(u||[]).map(R=>R.w).join("|");if(M!==Ma){for(Ma=M;vs.children.length;)vs.children.pop().geometry.dispose();(u||[]).forEach(R=>(R.lines||[]).forEach(I=>{if(!I||I.length<2)return;let F=I.map(ot=>new D(Pt(ot[0]),V(ot[0],ot[1])+1.2,Dt(ot[1]))),z=new ri(F),J=Math.max(24,F.length*3);vs.add(new Qt(new Ri(z,J,1.05,6),Sa)),vs.add(new Qt(new Ri(z,J,.9,6),Hl))})),Ye=!0}}let O=new ii;Zt.add(O);let $=0;function X(u){for(;O.children.length;){let M=O.children.pop();M.geometry.dispose(),M.material.dispose()}if($=0,u&&u.pts&&u.pts.length>1){let M=u.pts,R=!!u.ask;for(let I=1;I<M.length;I++){let F=M[I-1],z=M[I],J=Math.max(8,Math.ceil(Math.hypot(z[0]-F[0],z[1]-F[1])/3)),ot=[];for(let Z=0;Z<=J;Z++){let ht=Z/J,lt=F[0]+(z[0]-F[0])*ht,yt=F[1]+(z[1]-F[1])*ht;ot.push(new D(Pt(lt),V(lt,yt)+2+Math.sin(Math.PI*ht)*4,Dt(yt)))}let ut=new ri(ot),et=R?Math.max(4,Math.round(ut.getLength()/6)):1;for(let Z=0;Z<et;Z+=R?2:1){let ht=[];for(let lt=0;lt<=8;lt++)ht.push(ut.getPoint((Z+lt/8)/et));O.add(new Qt(new Ri(new ri(ht),R?8:J*4,.85,6),new tn({color:R?"#b3261e":"#111111",roughness:.5,emissive:R?"#5a0d08":"#000000",emissiveIntensity:R?.35:0})))}$++}}Ye=!0}let q=null,At=null;function Ot(){if(typeof rn<"u"&&rn)return;let u=At||q;Object.keys(Qn).forEach(M=>{let R=Qn[M],I=!u||M===u;R.mat.opacity=I?1:.15,R.edge&&(R.edge.material.opacity=I?.9:.1),R.shell&&(R.shell.opacity=I?.95:.12),(R.nums||[]).forEach(F=>{F.hid=!(u?M===u:M==="A")}),R.badges.forEach(F=>{F.el.style.opacity=I?1:.25})}),Ye=!0}let Et=new oa,Nt=new kt;function Vt(u){if(!Us.length)return null;let M=pe.domElement.getBoundingClientRect();Nt.set((u.clientX-M.left)/M.width*2-1,-(u.clientY-M.top)/M.height*2+1),Et.setFromCamera(Nt,N);let R=Et.intersectObjects(Us,!1)[0];return R?R.object.userData.key:null}function se(u){let M=pe.domElement.getBoundingClientRect();Nt.set((u.clientX-M.left)/M.width*2-1,-(u.clientY-M.top)/M.height*2+1),Et.setFromCamera(Nt,N);let R=Et.intersectObject(ct,!1)[0];return R?[R.point.x+a/2,R.point.z+o/2]:null}function re(u){u!==At&&(At=u,Ot(),t.onWay&&t.onWay(u))}let Ht=u=>`rgb(${u.map(M=>M|0).join(",")})`,ve=[[0,"the highest ground"],[1,"a ridge"],[2,"low ground"],[3,"lower ground"],[4,"the lowest ground"]];m.innerHTML="<b>LEGEND</b>"+ve.map(([u,M])=>{let R=ft.indexOf(u);return R<0?"":`<div class="r"><i style="background:${Ht(at[R])}"></i><span>${t.emo[R][0]}${h?"":": "+M}</span></div>`}).join("")+(h?'<div class="r"><i style="background:linear-gradient(#cfc8b8,#7d7566)"></i><span>The ground is the real terrain, '+A+". Emotion shows only as color.</span></div>":"")+(h?'<div class="r"><i style="background:rgba(120,160,120,.45);border:2px solid #2a9d8f"></i><span>Shaded patches: areas you drew on the place map, in their emotion\u2019s color.</span></div><div class="r"><i style="background:#8a8577"></i><span>Satellite image without color: no notes nearby, so no information here.</span></div>':'<div class="r"><i style="background:rgb(140,135,127)"></i><span>Bare rock face: two distant emotions meet with no ridge of indifference between them, so getting across is a climb. A big move takes energy either way; most moves go through indifference.</span></div><div class="r"><i style="background:rgb(116,122,74)"></i><span>Plain grass, soil or rock, no color: no notes nearby, so no information here.</span></div>')+(t.routes&&t.routes.length?t.routes.map(u=>`<div class="r"><i style="background:${Li[u.key]};border-color:#111;height:6px;margin-top:5px"></i><span><b style="display:inline;letter-spacing:0;font-size:12.5px">${u.key}</b> \xB7 ${u.name.replace(/[<>&]/g,"")}</span></div>`).join(""):"")+(t.spokes?'<div class="r"><i style="background:#222;height:2px;margin-top:7px"></i><span>Thin lines: from each question\u2019s flag to its notes.</span></div>':"")+((t.read||[]).length?'<div class="r"><i style="background:#111;border-radius:50%"></i><span>Numbered: what the ground says'+(t.spokes?" (from Pattern Synthesis). Hover or tap a number to read it.":", read above the map.")+'</span></div><div class="r"><i style="background:#3a1f0c;height:6px;margin-top:5px;border:1px solid #fff;box-shadow:0 0 0 1px #bbb"></i><span>A brown line: a pattern you ticked under PATTERNS THAT RUN THROUGH IT.</span></div>':"")+(h?'<div class="r"><i style="background:#111;border-radius:50%"></i><span>Pins are notes in their emotion\u2019s color, where you placed them; black flags are questions. The green flag (START) is the note farthest from the goal; the checkered flag is the goal, at '+(h.name?h.name.replace(/[<>&]/g,""):"your location")+". North is at the back.</span></div>":'<div class="r"><i style="background:#111;border-radius:50%"></i><span>Pins are notes in their emotion\u2019s color; black flags are questions. The green flag is the present; the checkered flag is the goal. \u2190 PRESENT and FUTURE \u2192 run along the front; \u2191 HELP and \u2193 HINDER run back to front.</span></div>')+(_t?'<div class="r"><i style="background:#fff;border:2px dashed #111;border-radius:50%"></i><span>A dashed ring: a cluster, notes from three or more people with the same emotion about the same thing. A faint dot: a note in no cluster. Tap a tag to read it; the list is under the map.</span></div>':"")+'<div class="r"><span style="color:#666">Drag to turn, scroll or pinch to zoom. Hover or tap a note, question, the goal, a number, or a way to read it.</span></div>',t.card&&(m.innerHTML='<details class="grlf"><summary>Legend</summary>'+m.innerHTML.replace("<b>LEGEND</b>","")+"</details>");let Fe=document.createElement("div");Fe.className="grfs fsleg";let Ae=document.createElement("button");Ae.type="button",Ae.className="grfs fslb",Ae.textContent="Hide legend";let Ie=document.createElement("div");Ie.className="grfs brand",Ie.innerHTML="<b>THE BEAR CANYON METHOD</b> \xB7 BY OPERATIONAL COHERENCE",Ae.onclick=u=>{u.stopPropagation();let M=!Fe.classList.contains("shut");Fe.classList.toggle("shut",M),Ae.textContent=M?"Legend":"Hide legend",Ms=!1,ji()},[Fe,Ae,Ie].forEach(u=>f.appendChild(u));let hn=()=>{Fe.innerHTML="";let u=m.cloneNode(!0);u.style.display="",u.querySelectorAll("details").forEach(M=>{M.open=!0}),Fe.appendChild(u)},Bt=document.createElement("button"),He=document.createElement("button");Bt.className=He.className="bt",Bt.textContent="Reset view",He.textContent="Full screen";let te=document.createElement("button");te.className="bt tpb",te.textContent="Play the tour",te.dataset.st="play";let On=document.createElement("button");On.className="bt tpe",On.textContent="End tour";let $e=document.createElement("button"),ti=document.createElement("button");$e.className=ti.className="bt tpn",$e.textContent="\u2039 Back",ti.textContent="Next \u203A",$e.title="The stop before",ti.title="The next stop";let xn=document.createElement("div");xn.className="tourbar",xn.appendChild($e),xn.appendChild(te),xn.appendChild(ti),xn.appendChild(On),f.appendChild(xn);let Pn=(t.intro||[]).concat(t.read||[]),xe=(t.intro||[]).length,nn=document.createElement("div");nn.style.cssText="position:absolute;top:8px;right:8px;display:flex;gap:6px;z-index:3",[Bt,He].forEach(u=>{u.style.position="static",nn.appendChild(u)});let Bn=nn;(t.card||Pn.length<2)&&(xn.style.display="none"),t.card&&(He.style.display="none"),f.appendChild(nn);let Oe=-1e9;for(let u=0;u<tt.length;u++)tt[u]>Oe&&(Oe=tt[u]);let sn=[];[-a/2-16,a/2].forEach(u=>[dt-30,Oe+14].forEach(M=>[-o/2,o/2].forEach(R=>sn.push(new D(u,M,R)))));function En(){let u=new D(0,(dt+Oe)/2-6,8),M=new D(0,290,330).normalize(),R=440;for(let ht=0;ht<6;ht++){N.position.copy(u).addScaledVector(M,R),N.lookAt(u),N.updateMatrixWorld();let lt=0;sn.forEach(yt=>{let xt=yt.clone().project(N);lt=Math.max(lt,Math.abs(xt.x),Math.abs(xt.y))}),R*=lt/.99}N.position.copy(u).addScaledVector(M,R),N.lookAt(u),N.updateMatrixWorld();let I=1,F=-1,z=1,J=-1;sn.forEach(ht=>{let lt=ht.clone().project(N);I=Math.min(I,lt.y),F=Math.max(F,lt.y),z=Math.min(z,lt.x),J=Math.max(J,lt.x)});let ot=new D(0,1,0).applyQuaternion(N.quaternion),ut=new D(1,0,0).applyQuaternion(N.quaternion),et=Math.tan(N.fov*Math.PI/360)*R,Z=ot.multiplyScalar((I+F)/2*et).add(ut.multiplyScalar((z+J)/2*et*N.aspect));u.add(Z),N.position.copy(u).addScaledVector(M,R),me.target.copy(u),me.update(),Ye=!0}let Re=document.createElement("div");Re.className="tourcap",Re.setAttribute("aria-live","polite"),f.appendChild(Re);let un=null,jd=new kn({color:"#ffffff",transparent:!0,opacity:.95,depthTest:!1,depthWrite:!1}),Ch=new kn({color:"#ffffff",transparent:!0,opacity:.3,depthTest:!1,depthWrite:!1}),Ki=new ii,Qd=new Qt(new Rs(16,.9,8,72),jd),tf=new Qt(new Rs(16,3.4,8,72),Ch);[Qd,tf].forEach(u=>{u.rotation.x=-Math.PI/2,u.renderOrder=999,Ki.add(u)}),Ki.visible=!1,Zt.add(Ki);function ba(u){if(L.forEach(R=>R.el.classList.remove("tfoc")),!u||!u.at){Ki.visible=!1,Ye=!0;return}Ki.position.set(Pt(u.at[0]),V(u.at[0],u.at[1])+2,Dt(u.at[1])),Ki.visible=!0;let M={};(((u.title||"")+" "+(u.cap||u.text||"")).match(/\b[NP]\d+\b/g)||[]).forEach(R=>{M[R]=1}),L.forEach(R=>{/\bnl\b/.test(R.el.className)&&M[R.el.textContent.trim()]&&R.el.classList.add("tfoc")}),Ye=!0}function ef(u){if(!Ki.visible)return;let M=Math.sin(u/280);Ki.scale.setScalar(1+.07*M),Ch.opacity=.26+.14*M}let nf=u=>u<.5?2*u*u:1-Math.pow(-2*u+2,2)/2;function sf(){let u=N.position.clone(),M=me.target.clone();En();let R=N.position.clone(),I=me.target.clone();return N.position.copy(u),me.target.copy(M),N.lookAt(M),[R,I]}function Ph(u){let M=Pn[u];if(u<xe||!M||M.grp==null||!t.actMean)return"";let R=Pn[u-1];return(u===xe||!R||R.grp!==M.grp)&&t.actMean[M.grp]||""}function rf(u){let M=Pn[u],R=t.groups||[];Re.innerHTML='<div class="ta"></div><div class="tm"></div><div class="tt"></div><div class="tx"></div><div class="tp"><i></i></div>';let I=Ph(u);Re.querySelector(".tm").textContent=I,Re.querySelector(".tm").style.display=I?"":"none",Re.querySelector(".ta").textContent=M.act||R[M.grp]||"",Re.querySelector(".tt").textContent=(u<xe?"":u-xe+1+" \xB7 ")+(M.title||""),Re.querySelector(".tx").textContent=String(M.cap||M.text||"").replace(/\s*\(\s*(?:after\s+)?Vigneaux,?\s*2026\s*\)/g,"").replace(/\s+in Vigneaux \(2026\)/g,"")}let Gl=!1;function Fs(){un&&(un=null,ba(null),f.classList.remove("touring"),me.enabled=!0,Re.style.display="none",te.textContent="Play the tour",te.dataset.st="play",te.title="",On.style.display=$e.style.display=ti.style.display="none",Gl&&(Gl=!1,f.classList.contains("fs")&&He.onclick()),Ve.forEach(u=>u.el.classList.remove("on")),t.onHL&&t.onHL(null),Ms=!1,En(),Ye=!0)}function Ih(){let u=un;!u||u.paused!=null||(u.paused=(performance.now()-u.start)/1e3,me.enabled=!0,te.textContent="Play",te.dataset.st="play",Ye=!0)}function af(){let u=un;if(!u||u.paused==null)return;let M=u.legs[0];for(let R of u.legs)u.paused>=R.t0&&(M=R);M.a=[N.position.clone(),me.target.clone()],u.start=performance.now()-M.t0*1e3,u.paused=null,me.enabled=!1,te.textContent="Pause",te.dataset.st="pause",qe=null,$n(),Ye=!0}function Lh(){if(un)return un.paused!=null?af():Ih();!t.card&&!f.classList.contains("fs")&&(Gl=!0,He.onclick());let[u,M]=sf(),R=u.distanceTo(M),I=Pn.length,F=+window.gsmTourSlow||1,z=1.2*F,J=[],ot=(Z,ht)=>(Math.max(2.4,Math.min(6,((Z.title||"")+" "+(Z.cap||Z.text||"")).split(/\s+/).length/3.3))+Math.min(5,Ph(ht).split(/\s+/).filter(Boolean).length/3.6))*F,ut=[N.position.clone(),me.target.clone()];Pn.forEach((Z,ht)=>{if(!Z.at){J.push({i:ht,a:ut,b:[u.clone(),M.clone()],fly:z,hold:ot(Z,ht)}),ut=[u.clone(),M.clone()];return}let lt=new D(Pt(Z.at[0]),V(Z.at[0],Z.at[1]),Dt(Z.at[1])),yt=-.55+1.1*(I>1?ht/(I-1):.5),xt=.74,Tt=Math.max(me.minDistance+10,R*.55),Mt=lt.clone().add(new D(Math.sin(xt)*Math.sin(yt),Math.cos(xt),Math.sin(xt)*Math.cos(yt)).multiplyScalar(Tt)),Jt=lt.clone().add(new D(0,Tt*.08,0));J.push({i:ht,a:ut,b:[Mt,Jt],fly:z,hold:ot(Z,ht)}),ut=[Mt,Jt]}),J.push({i:-1,a:ut,b:[u,M],fly:1.4*F,hold:0});let et=0;J.forEach(Z=>{Z.t0=et,et+=Z.fly+Z.hold}),f.classList.add("touring"),un={legs:J,start:performance.now(),total:et,cur:-2,paused:null},me.enabled=!1,Re.style.display="block",te.textContent="Pause",te.dataset.st="pause",te.title="Escape also ends the tour",On.style.display=$e.style.display=ti.style.display="inline-block",qe=null,$n(),Ye=!0}function Nh(u){let M=un;if(!M)return;let R=M.legs.findIndex(z=>z.i===M.cur);R<0&&(R=0);let I=Math.max(0,Math.min(M.legs.length-1,R+u));if(I===M.legs.length-1&&u>0&&R===M.legs.length-2){Fs();return}let F=M.legs[I];F.a=[N.position.clone(),me.target.clone()],M.start=performance.now()-F.t0*1e3,M.paused=null,M.cur=-2,me.enabled=!1,te.textContent="Pause",te.dataset.st="pause",qe=null,$n(),Ye=!0}$e.onclick=u=>{u.stopPropagation(),Nh(-1)},ti.onclick=u=>{u.stopPropagation(),Nh(1)};function of(u){let M=un;if(M.paused!=null){me.update();return}let R=(u-M.start)/1e3;if(R>=M.total){Fs();return}let I=M.legs[0];for(let J of M.legs)R>=J.t0&&(I=J);if(ef(u),I.i!==M.cur)if(M.cur=I.i,ba(I.i>=0?Pn[I.i]:null),I.i>=0){rf(I.i);let J=I.i-xe;Ve.forEach((ot,ut)=>ot.el.classList.toggle("on",ut===J)),t.onHL&&t.onHL(J>=0?J:null)}else Re.style.display="none",Ve.forEach(J=>J.el.classList.remove("on")),t.onHL&&t.onHL(null);let F=nf(Math.min(1,(R-I.t0)/I.fly));N.position.lerpVectors(I.a[0],I.b[0],F),me.target.lerpVectors(I.a[1],I.b[1],F),N.lookAt(me.target);let z=Re.querySelector(".tp i");z&&(z.style.width=(100*R/M.total).toFixed(1)+"%"),Ye=!0}var rn=null;let Mi=new ii;Zt.add(Mi);let Cr=new tn({color:"#f2b400",roughness:.4,emissive:"#5a3c00",emissiveIntensity:.35}),Pr=new kn({color:"#111111"});li(Cr,9),li(Pr,8);let Vl=new kn({color:"#f2b400",transparent:!0,opacity:.5,depthTest:!1,depthWrite:!1,side:zn}),Dh=(u,M,R)=>{if(M===0)return h?"START":"PRESENT";if(M===R-1)return"GOAL";let I=null,F=4.5;return t.notes.forEach(z=>{let J=Math.hypot(z.x-u[0],z.y-u[1]);J<F&&(F=J,I=z)}),I?{k:(t.np||"N")+I.k,n:I}:{k:"a turn",n:null}};function lf(u){let M=Qn[u];if(!M||!M.stops||M.stops.length<3)return null;let R=M.rp,I=[],F=[],z=0,J={};M.stops.forEach((ut,et)=>{if(et&&Math.hypot(ut[0]-M.stops[et-1][0],ut[1]-M.stops[et-1][1])<3&&et<M.stops.length-1){(J[I.length-1]=J[I.length-1]||[]).push(ut);return}let Z=-1,ht=1e9;for(let lt=z;lt<R.length;lt++){let yt=Math.hypot(R[lt][0]-ut[0],R[lt][1]-ut[1]);if(yt<4.5){Z=lt;break}yt<ht&&(ht=yt,Z=lt)}et===M.stops.length-1&&(Z=R.length-1),et===0&&(Z=0),z=Z,I.push(ut),F.push(Z)});let ot=I.map((ut,et)=>{let Z=Dh(ut,et,I.length);if(typeof Z=="string"||!J[et])return Z;let ht=[Z.k];return J[et].forEach(lt=>{let yt=Dh(lt,1,3);typeof yt!="string"&&yt.n&&ht.indexOf(yt.k)<0&&ht.push(yt.k)}),{k:ht.join(" + "),n:Z.n,all:ht}});return{k:u,w:M,st:I,idx:F,names:ot}}let Wl=(u,M,R)=>{let I=u.filter((z,J)=>J%2===0||J===u.length-1).map(z=>new D(Pt(z[0]),V(z[0],z[1])+2+M*.4,Dt(z[1])));if(I.length<2)return null;I.length===2&&I.splice(1,0,I[0].clone().lerp(I[1],.5));let F=new ri(I);return{c:F,g:Fn(F,R*2.4,R>2.5?1.6:R>1.5?1.8:1.6)}};function Uh(){for(;Mi.children.length;){let u=Mi.children.pop();u.geometry.dispose(),u.material!==Cr&&u.material!==Pr&&u.material!==Vl&&u.material.dispose()}}function Ir(u){let M=rn;if(!M)return;let R=M.st.length;u=Math.max(1,Math.min(R-1,u)),M.i=u,Uh();let I=M.w.ri,F=M.idx[u-1],z=M.idx[u];if(F>0){let xt=Wl(M.w.rp.slice(0,F+1),I,.9);xt&&Mi.add(new Qt(xt.g,li(new tn({color:M.k==="B"?"#666666":Li[M.k]||"#111",roughness:.8}),7)))}let J=Wl(M.w.rp.slice(F,Math.max(F+2,z+1)),I,2.1);if(J){Mi.add(new Qt(J.g,Cr)),Mi.add(new Qt(J.g.clone(),Vl));let xt=Wl(M.w.rp.slice(F,Math.max(F+2,z+1)),I,3.6);xt&&Mi.add(new Qt(xt.g,Pr));let Tt=J.c.getPointAt(.97),Mt=J.c.getTangentAt(.97).normalize(),Jt=new Nn().setFromUnitVectors(new D(0,1,0),Mt),We=J.c.getLength(),ue=Math.max(0,1-13/We);Mi.add(new Qt(Fn(J.c,11,1.9,16,ue,1,!0),Cr)),Mi.add(new Qt(Fn(J.c,14.5,1.8,16,Math.max(0,ue-1.5/We),1,!0),Pr))}Mi.children.forEach(xt=>{xt.renderOrder=xt.material===Cr?22:xt.material===Pr?21:xt.material===Vl?19:20});let ot=M.names,ut=ot[u],et=ot[u-1],Z=xt=>typeof xt=="string"?xt:xt.k;ba({at:M.st[u],title:[et,ut].map(xt=>typeof xt=="string"?"":xt.k).join(" ")}),Re.innerHTML='<div class="ta"></div><div class="tt"></div><div class="tx"></div><div class="wk"></div>',Re.appendChild(Yl),Re.querySelector(".ta").textContent="WAY "+M.k+" \xB7 STEP "+u+" OF "+(R-1),Re.querySelector(".tt").textContent="From "+Z(et)+" to "+Z(ut);let ht=typeof ut=="string"?null:ut.n,lt=ut==="GOAL"?t.goalText||"The goal.":ht?(ht.e==null?"":t.emo[ht.e][0][0].toUpperCase()+t.emo[ht.e][0].slice(1)+". ")+String(ht.t||""):typeof ut=="string"?"":"The way turns here, between notes.";Re.querySelector(".tx").textContent=lt.length>220?lt.slice(0,217).replace(/\s+\S*$/,"")+"\u2026":lt;let yt=Re.querySelector(".wk");ot.forEach((xt,Tt)=>{if(Tt){let Jt=document.createElement("i");Jt.textContent="\u203A",yt.appendChild(Jt)}let Mt=document.createElement("span");Mt.textContent=Z(xt),Mt.className=Tt===u?"at":Tt===u-1?"fr":Tt<u?"dn":"",Mt.title=Tt?"Go to step "+Tt:"The start",Mt.onclick=Jt=>{Jt.stopPropagation(),Ir(Math.max(1,Tt))},yt.appendChild(Mt)}),Bs.disabled=u<=1,ks.textContent=u>=R-1?"Done":"Next \u203A",Fh(),Ye=!0}let Xl=new D;function Fh(){let u=rn;if(!u)return;let M=pe.domElement.clientWidth,R=pe.domElement.clientHeight,I=parseFloat(pe.domElement.style.marginLeft)||0,F=u.idx[u.i-1],z=u.idx[u.i],J=[];for(let Mt=F;Mt<=z;Mt+=Math.max(1,Math.floor((z-F)/12)))J.push(u.w.rp[Mt]);J.push(u.w.rp[z]);let ot=J.map(Mt=>(Xl.set(Pt(Mt[0]),V(Mt[0],Mt[1])+2,Dt(Mt[1])).project(N),[I+(Xl.x*.5+.5)*M,(-Xl.y*.5+.5)*R])),ut=Re.offsetWidth,et=Re.offsetHeight,Z=f.clientWidth,ht=f.clientHeight,lt=18,yt=[[I+12,44],[I+12,ht-et-12],[Z-ut-12,ht-et-12],[Z-ut-12,44]],xt=yt[0],Tt=1e9;yt.forEach(([Mt,Jt])=>{let We=ot.filter(([ue,Ee])=>ue>Mt-lt&&ue<Mt+ut+lt&&Ee>Jt-lt&&Ee<Jt+et+lt).length;We<Tt&&(Tt=We,xt=[Mt,Jt])}),Re.style.left=Math.max(I+4,xt[0])+"px",Re.style.right="auto",Re.style.top=Math.max(4,xt[1])+"px"}let ql=!1,Oh=()=>{let u=i.closest(".coa");return u?u.querySelector(".gtfsb"):null};function Bh(u){un&&Fs();let M=lf(u||q||"A");if(!M)return;rn=M,f.classList.add("walking"),qe=null,$n();let R=Oh();t.card&&R&&!i.closest(".gtfs-on")&&(ql=!0,R.click(),setTimeout(()=>{try{f.scrollIntoView({block:"nearest"})}catch{}},60)),Object.keys(Qn).forEach(I=>{let F=Qn[I];F.mat.opacity=I===M.k?.22:.06,F.edge&&(F.edge.material.opacity=I===M.k?.15:.05),F.shell&&(F.shell.opacity=.05),(F.nums||[]).forEach(z=>{z.hid=!0}),F.badges.forEach(z=>{z.el.style.opacity=.2})}),Ir(1)}me.addEventListener("end",()=>{rn&&Fh()});function Os(){if(rn){if(rn=null,Uh(),ba(null),f.classList.remove("walking"),Re.style.display="none",Re.innerHTML="",Re.style.top="",Re.style.right="",Ot(),Zl(),ql){ql=!1;let u=Oh();u&&i.closest(".gtfs-on")&&u.click()}Ye=!0}}let Yl=document.createElement("div");Yl.className="walkbar";let Bs=document.createElement("button"),ks=document.createElement("button"),Ea=document.createElement("button");Bs.className=Ea.className="bt",ks.className="bt wnx",Bs.textContent="\u2039 Back",ks.textContent="Next \u203A",Ea.textContent="Stop walking",[Bs,ks,Ea].forEach(u=>{u.type="button",Yl.appendChild(u)}),Bs.onclick=u=>{u.stopPropagation(),rn&&Ir(rn.i-1)},ks.onclick=u=>{u.stopPropagation(),rn&&(rn.i>=rn.st.length-1?Os():Ir(rn.i+1))},Ea.onclick=u=>{u.stopPropagation(),Os()};let $i=document.createElement("button");$i.type="button",$i.className="bt wgo",$i.style.position="static";function Zl(){let u=q||"A",M=Qn[u]&&Qn[u].stops&&Qn[u].stops.length>=3;$i.style.display=t.card&&M?"":"none",$i.textContent="Walk way "+u+", step by step",$i.title="Follow way "+u+" one leg at a time, in order"}$i.onclick=u=>{u.stopPropagation(),rn?Os():Bh()},document.addEventListener("keydown",u=>{!rn||!i.isConnected||(u.key==="ArrowRight"?(u.preventDefault(),ks.onclick(u)):u.key==="ArrowLeft"?(u.preventDefault(),Bs.onclick(u)):u.key==="Escape"&&Os())}),Bn.insertBefore($i,Bn.firstChild),Zl(),te.onclick=u=>{u.stopPropagation(),Lh()},On.onclick=u=>{u.stopPropagation(),Fs()},f.addEventListener("pointerdown",u=>{un&&!(u.target.closest&&u.target.closest(".bt,.grfs"))&&Ih()}),Bt.onclick=()=>{un&&Fs(),Ms=!1,En()},He.onclick=()=>{let u=!f.classList.contains("fs");u&&hn(),Ms=!1,f.classList.toggle("fs",u),t.onFs&&t.onFs(u,f),He.textContent=u?"Close full screen":"Full screen",document.documentElement.style.overflow=u?"hidden":"",ji()};let kh=u=>{if(u.key!=="Escape")return;un?Fs():f.classList.contains("fs")&&He.onclick();let M=f.classList.contains("fs");He.textContent==="Close full screen"!==M&&(He.textContent=M?"Close full screen":"Full screen",M||(document.documentElement.style.overflow=""),Ms=!1,ji())};document.addEventListener("keydown",kh);let Ye=!0,Ta=!0,zh=0,Jl=!1;function ji(){let u=f.classList.contains("fs"),M=u?window.innerWidth:f.clientWidth;if(!M)return;let R=t.card&&i.closest(".gtfs-on"),I=u?window.innerHeight:Math.round(R?Math.max(420,window.innerHeight*.78):Math.max(300,Math.min(t.card?520:620,M*(t.card?.62:.56))));f.classList.toggle("cfs",!!R),R&&hn(),m.style.display=S.style.display=R?"none":"";let F=(u||R)&&!Fe.classList.contains("shut")?Math.min(340,Math.round(M*.86)):0,z=Math.max(200,M-F);f.style.height=u?"":I+"px",pe.setSize(z,I),pe.domElement.style.marginLeft=F+"px",d.style.left=F+"px",p.style.left=F+6+"px",typeof Re<"u"&&(Re.style.left=F+12+"px"),typeof xn<"u"&&(xn.style.left=F+z/2+"px");let J=f.querySelector(".fslay");J&&(J.style.left=F+12+"px",J.style.maxWidth=Math.max(220,z*.62)+"px"),N.aspect=z/I,N.fov=30,N.updateProjectionMatrix(),zh=M,typeof En=="function"&&!Ms&&En(),Ye=!0}let wa=window.ResizeObserver?new ResizeObserver(ji):null;wa&&wa.observe(f),window.addEventListener("resize",ji);let Ms=!1;me.addEventListener("start",()=>{Ms=!0}),me.addEventListener("change",()=>{Ye=!0,qe||(Ke.style.display="none")});let Aa=new D,Si=new D,Kl=new D;function cf(){let u=pe.domElement.clientWidth,M=pe.domElement.clientHeight,R=[],I=[],F=new D(0,1,0).applyQuaternion(N.quaternion);L.forEach(et=>{if(!et.head||et.hid||et.off||(Si.copy(et.head).project(N),Si.z>1))return;Kl.copy(et.head).addScaledVector(F,2.8).project(N);let Z=1.5*Math.max(3,Math.hypot((Kl.x-Si.x)*.5*u,(Kl.y-Si.y)*.5*M));I.push({o:et,x:(Si.x*.5+.5)*u,y:(-Si.y*.5+.5)*M,r:Z})});let z=[];Ce.forEach(et=>{Si.copy(et).project(N),Si.z<=1&&z.push([(Si.x*.5+.5)*u,(-Si.y*.5+.5)*M])});let J=(et,Z,ht,lt,yt)=>{if(et.el.textContent==="GOAL")return 0;let xt=0;for(let Tt of z)Tt[0]>Z-3&&Tt[0]<Z+lt+3&&Tt[1]>ht-3&&Tt[1]<ht+yt+3&&(xt+=30);return xt},ot=(et,Z,ht,lt)=>{let yt=0;for(let xt of R)et<xt[0]+xt[2]&&et+ht>xt[0]&&Z<xt[1]+xt[3]&&Z+lt>xt[1]&&(yt+=Math.min(et+ht,xt[0]+xt[2])-Math.max(et,xt[0])+1);return yt},ut=(et,Z,ht,lt,yt)=>{let xt=0;if(!et.isN)return 0;for(let Tt of I){if(Tt.o===et)continue;let Mt=Math.max(Z,Math.min(Tt.x,Z+lt)),Jt=Math.max(ht,Math.min(Tt.y,ht+yt));(Mt-Tt.x)**2+(Jt-Tt.y)**2<(Tt.r+1)**2&&(xt+=40+Tt.r)}return xt};L.map(et=>(Aa.copy(et.v).project(N),et.sx=(Aa.x*.5+.5)*u,et.sy=(-Aa.y*.5+.5)*M,{o:et,x:et.sx+et.ax-(et.cen?(et.el.offsetWidth||0)/2:0),y:et.sy+et.ay,off:Aa.z>1})).sort((et,Z)=>Z.o.pri-et.o.pri||et.o.sy-Z.o.sy).forEach(et=>{let Z=et.o;if(Z.hid||et.off||et.x<-24||et.x>u+24||et.y<-24||et.y>M+24){Z.el.style.display="none",Z.ld&&(Z.ld.style.display="none");return}Z.el.style.display="";let ht=Z.el.offsetWidth||30,lt=Z.el.offsetHeight||16,yt=et.x,xt=et.y;if(!/\bside\b/.test(Z.el.className)&&(ot(yt,xt,ht,lt)||ut(Z,yt,xt,ht,lt)||J(Z,yt,xt,ht,lt))){let ue=Z.sx,Ee=Z.sy,Pe=4,ne=[];[0,1,2,3].forEach(Me=>{let ce=Me*(lt+2);ne.push([et.x,et.y-ce-0],[ue+Pe+ce,Ee-lt/2],[ue-Pe-ht-ce,Ee-lt/2],[ue-ht/2,Ee-Pe-lt-ce],[ue-ht/2,Ee+Pe+ce],[ue+Pe+ce*.7,Ee-Pe-lt-ce*.7],[ue-Pe-ht-ce*.7,Ee-Pe-lt-ce*.7],[ue+Pe+ce*.7,Ee+Pe+ce*.7],[ue-Pe-ht-ce*.7,Ee+Pe+ce*.7])});let Te=null,Qe=1e9;for(let Me=0;Me<ne.length;Me++){let[ce,Yt]=ne[Me];if(ce<2||ce+ht>u-2||Yt<2||Yt+lt>M-2)continue;let jt=ot(ce,Yt,ht,lt)*20+ut(Z,ce,Yt,ht,lt)*20+J(Z,ce,Yt,ht,lt)*20+Me;if(jt<Qe&&(Qe=jt,Te=ne[Me]),jt===Me)break}Te&&(yt=Te[0],xt=Te[1])}if(Z.isN){let ue=N.position.distanceTo(Z.v),Ee=N.position.distanceTo(me.target),Pe=Math.max(0,Math.min(1,(ue-Ee*.95)/(Ee*.4))),ne=(1-.35*Pe).toFixed(2);Z.el.style.filter=ne==="1.00"?"":"opacity("+ne+")"}yt=Math.max(2,Math.min(u-ht-2,yt)),R.push([yt,xt,ht,lt]),Z.el.style.transform=`translate(${yt.toFixed(1)}px,${xt.toFixed(1)}px)`;let Tt=Math.max(yt,Math.min(Z.sx,yt+ht)),Mt=Math.max(xt,Math.min(Z.sy,xt+lt)),Jt=Math.hypot(Tt-Z.sx,Mt-Z.sy);if(Math.hypot(yt-et.x,xt-et.y)>3&&Jt>7){Z.ld||(Z.ld=document.createElement("div"),Z.ld.className="ldr",d.insertBefore(Z.ld,d.firstChild));let ue=3.5,Ee=Jt-ue;Z.ld.style.display="block",Z.ld.style.width=Ee.toFixed(1)+"px";let Pe=Math.atan2(Mt-Z.sy,Tt-Z.sx);Z.ld.style.transform=`translate(${(Z.sx+Math.cos(Pe)*ue).toFixed(1)}px,${(Z.sy+Math.sin(Pe)*ue).toFixed(1)}px) rotate(${Pe.toFixed(3)}rad)`,Z.ld.style.opacity=Z.el.style.opacity||""}else Z.ld&&(Z.ld.style.display="none")})}function Hh(){if(Ta){if(!i.isConnected){Gh();return}un?of(performance.now()):me.update(),!!(t.card&&i.closest(".gtfs-on"))!==Jl&&(Ye=!0),Ye&&f.clientWidth&&(Ve.forEach(u=>u.rim&&u.rim.quaternion.copy(N.quaternion)),(f.clientWidth!==zh||!!(t.card&&i.closest(".gtfs-on"))!==Jl)&&!f.classList.contains("fs")&&(Jl=!!(t.card&&i.closest(".gtfs-on")),ji()),en(),cf(),Ye=!1),requestAnimationFrame(Hh)}}function Gh(){if(Ta){Ta=!1,wa&&wa.disconnect(),window.removeEventListener("resize",ji),document.removeEventListener("keydown",kh),document.removeEventListener("click",Tr,!0),pe.dispose();try{pe.forceContextLoss()}catch{}}}ji(),En(),Hh(),Un();function hf(u){St.forEach(M=>{let R=!u||M.q===u;M.st.visible=M.hd.visible=R,M.sp&&(M.sp.visible=R),M.lo.off=!R,M.lo.el.style.opacity=R?"":"0",M.lo.el.style.pointerEvents=R?"":"none"}),Ye=!0}return{cluster:ys,loops:v,hoses:X,hoseCount(){return $},focusQ:hf,tour:Lh,touring(){return!!un},paused(){return!!un&&un.paused!=null},hl(u){qe||(Ve.forEach((M,R)=>M.el.classList.toggle("on",R===u)),Xt.length&&le(u))},setWay(u){u!==q&&(q=u,rn&&Os(),Ot(),Zl())},walk(u){Bh(u)},walking(){return rn?{k:rn.k,i:rn.i,n:rn.st.length-1,names:rn.names.map(u=>typeof u=="string"?u:u.k)}:null},walkStep(u){Ir(u)},walkEnd(){Os()},hoverWay(u){re(u)},snap(){return en(),pe.domElement.toDataURL("image/jpeg",.85)},height(){return f.offsetHeight},dispose:Gh}}var Rh=new Map;function Cx(i){if(!i||i.elev!==void 0)return Promise.resolve();let t=[i.X0,i.Y0,i.k].map(e=>(+e).toFixed(7)).join("|");return Rh.has(t)||Rh.set(t,Px(i)),Rh.get(t).then(e=>{i.elev=e},()=>{i.elev=null})}function Px(i){let n=340/i.k,s=Math.max(1,Math.min(15,Math.round(Math.log2(640/n)))),r,a,o,l,c=()=>{let m=2**s;r=Math.floor(i.X0*m/256),a=Math.floor((i.X0+n)*m/256),o=Math.floor(i.Y0*m/256),l=Math.floor((i.Y0+230/i.k)*m/256)};for(c();(a-r+1)*(l-o+1)>36&&s>1;)s--,c();let h=2**s,f=(a-r+1)*256,d=(l-o+1)*256,p=document.createElement("canvas");p.width=f,p.height=d;let x=p.getContext("2d",{willReadFrequently:!0}),S=(a-r+1)*(l-o+1);return new Promise(m=>{let g=S,E=0,P=!1,T=()=>{if(P)return;if(P=!0,E<S)return m(null);let C;try{C=x.getImageData(0,0,f,d).data}catch{return m(null)}let A=new Float32Array(f*d);for(let k=0,H=0;k<A.length;k++,H+=4)A[k]=C[H]*256+C[H+1]+C[H+2]/256-32768;let _=(k,H)=>{let K=Math.max(0,Math.min(f-1.001,(i.X0+k/i.k)*h-r*256)),U=Math.max(0,Math.min(d-1.001,(i.Y0+H/i.k)*h-o*256)),Y=K|0,tt=U|0,j=K-Y,dt=U-tt,V=(it,ft)=>A[ft*f+it];return V(Y,tt)*(1-j)*(1-dt)+V(Y+1,tt)*j*(1-dt)+V(Y,tt+1)*(1-j)*dt+V(Y+1,tt+1)*j*dt},b=1e9,G=-1e9;for(let k=0;k<=40;k++)for(let H=0;H<=60;H++){let K=_(H/60*340,k/40*230);b=Math.min(b,K),G=Math.max(G,K)}if(!isFinite(b)||G-b>9e3)return m(null);let B=(k,H)=>_(k,H)-b;B.lo=b,B.hi=G,m(B)};setTimeout(T,12e3);for(let C=r;C<=a;C++)for(let A=o;A<=l;A++){let _=new Image;_.crossOrigin="anonymous",_.onload=()=>{try{x.drawImage(_,(C-r)*256,(A-o)*256),E++}catch{}--g===0&&T()},_.onerror=()=>{--g===0&&T()},_.src="https://s3.amazonaws.com/elevation-tiles-prod/terrarium/"+s+"/"+C+"/"+A+".png"}})}window.gsmRelief={mount:Rx,prep:Cx,version:"r2"};})();
/*! Bundled license information:

three/build/three.core.js:
  (**
   * @license
   * Copyright 2010-2026 Three.js Authors
   * SPDX-License-Identifier: MIT
   *)

three/build/three.module.js:
  (**
   * @license
   * Copyright 2010-2026 Three.js Authors
   * SPDX-License-Identifier: MIT
   *)
*/
