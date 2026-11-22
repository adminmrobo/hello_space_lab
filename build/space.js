/* space.js — 좌표 첫걸음 계산·그림 모듈 (외부 라이브러리 없음)
   계산: 거리, 극좌표, 원통·지구본 자, 위도·경도, 메르카토르, 온도, 표준화
   그림: Plane(2D 좌표평면, 가로·세로 같은 축척, 클릭 좌표 되돌리기) */
var SP=(function(){
'use strict';
var D2R=Math.PI/180,RE=6371;
function dist(a,b){var s=0;for(var i=0;i<a.length;i++){var d=a[i]-b[i];s+=d*d;}return Math.sqrt(s);}
function taxi(a,b){var s=0;for(var i=0;i<a.length;i++)s+=Math.abs(a[i]-b[i]);return s;}
function toPolar(x,y){var r=Math.hypot(x,y),t=Math.atan2(y,x)/D2R;if(t<0)t+=360;if(Math.abs(t-360)<1e-9)t=0;return [r,t];}
function fromPolar(r,deg){return [r*Math.cos(deg*D2R),r*Math.sin(deg*D2R)];}
function arc(r,deg){return r*deg*D2R;}
function chord(r,deg){return 2*r*Math.sin(Math.abs(deg)*D2R/2);}
function monthAngle(m){return (m-1)*30;}
function monthChord(a,b){var d=Math.abs(monthAngle(a)-monthAngle(b));if(d>180)d=360-d;return chord(1,d);}
function cyl(x,y,z){var p=toPolar(x,y);return [p[0],p[1],z];}
function sph(x,y,z){var r=Math.sqrt(x*x+y*y+z*z),th=r?Math.acos(z/r)/D2R:0,ph=toPolar(x,y)[1];return [r,th,ph];}
function fromCyl(rho,ph,z){var q=fromPolar(rho,ph);return [q[0],q[1],z];}
function fromSph(r,th,ph){var s=Math.sin(th*D2R);return [r*s*Math.cos(ph*D2R),r*s*Math.sin(ph*D2R),r*Math.cos(th*D2R)];}
function lonKm(lat){return 2*Math.PI*RE/360*Math.cos(lat*D2R);}
function latKm(){return 2*Math.PI*RE/360;}
function mercY(lat){return Math.log(Math.tan(Math.PI/4+lat*D2R/2));}
function mercArea(lat){var c=Math.cos(lat*D2R);return 1/(c*c);}
function mercLen(lat){return 1/Math.cos(lat*D2R);}
function geoDist(la1,lo1,la2,lo2){var a=Math.sin((la2-la1)*D2R/2),b=Math.sin((lo2-lo1)*D2R/2),h=a*a+Math.cos(la1*D2R)*Math.cos(la2*D2R)*b*b;return 2*RE*Math.asin(Math.min(1,Math.sqrt(h)));}
function cToF(c){return c*1.8+32;}
function fToC(f){return (f-32)/1.8;}
function zscore(x,m,s){return (x-m)/s;}
function mean(a){return a.reduce(function(s,v){return s+v;},0)/a.length;}
function sd(a){var m=mean(a);return Math.sqrt(a.reduce(function(s,v){return s+(v-m)*(v-m);},0)/a.length);}
function nearest(pts,q,scale){var best=-1,bd=Infinity;pts.forEach(function(p,i){var s=0;for(var k=0;k<q.length;k++){var d=(p[k]-q[k])/(scale?scale[k]:1);s+=d*d;}s=Math.sqrt(s);if(s<bd){bd=s;best=i;}});return [best,bd];}

/* ── 2D 좌표평면: o={xr,yr,step,xl,yl,grid,pad,labels,axes} → {g,w,h,X,Y,inv,sc} ── */
function Plane(cv,o){
  var R=U.setup(cv),g=R.g,w=R.w,h=R.h,pad=o.pad||30;
  var sx=(w-2*pad)/(o.xr[1]-o.xr[0]),sy=(h-2*pad)/(o.yr[1]-o.yr[0]),sc=o.free?null:Math.min(sx,sy);
  var kx=sc||sx,ky=sc||sy,cx=(w-(o.xr[1]-o.xr[0])*kx)/2,cy=(h-(o.yr[1]-o.yr[0])*ky)/2;
  var X=function(v){return cx+(v-o.xr[0])*kx;},Y=function(v){return h-cy-(v-o.yr[0])*ky;};
  var inv=function(px,py){return [o.xr[0]+(px-cx)/kx,o.yr[0]+(h-cy-py)/ky];};
  var st=o.step||1,i,mute=U.cssv('--muted');
  g.fillStyle='#fff';g.fillRect(0,0,w,h);
  if(o.grid!==false){g.lineWidth=1;for(i=Math.ceil(o.xr[0]/st)*st;i<=o.xr[1]+1e-9;i+=st){g.strokeStyle=Math.abs(i)<1e-9?'rgba(22,33,43,0)':'rgba(22,33,43,.09)';g.beginPath();g.moveTo(X(i)+.5,Y(o.yr[0]));g.lineTo(X(i)+.5,Y(o.yr[1]));g.stroke();}
    var ys=o.ystep||st;for(i=Math.ceil(o.yr[0]/ys)*ys;i<=o.yr[1]+1e-9;i+=ys){g.strokeStyle='rgba(22,33,43,.09)';g.beginPath();g.moveTo(X(o.xr[0]),Y(i)+.5);g.lineTo(X(o.xr[1]),Y(i)+.5);g.stroke();}}
  if(o.axes!==false){var ox=Math.min(Math.max(0,o.xr[0]),o.xr[1]),oy=Math.min(Math.max(0,o.yr[0]),o.yr[1]);
    U.arrow2(g,X(o.xr[0]),Y(oy),X(o.xr[1])+8,Y(oy),U.cssv('--eye'),1.6);U.arrow2(g,X(ox),Y(o.yr[0]),X(ox),Y(o.yr[1])-8,U.cssv('--terrain'),1.6);
    g.font='11px '+U.cssv('--font');g.fillStyle=mute;g.textAlign='center';var ls=o.lstep||st;
    for(i=Math.ceil(o.xr[0]/ls)*ls;i<=o.xr[1]+1e-9;i+=ls){if(Math.abs(i-ox)<1e-9&&o.xr[0]<0)continue;g.fillText(o.xf?o.xf(i):String(+i.toFixed(2)),X(i),Y(oy)+14);}
    var yls=o.ylstep||ls;g.textAlign='right';for(i=Math.ceil(o.yr[0]/yls)*yls;i<=o.yr[1]+1e-9;i+=yls){if(Math.abs(i-oy)<1e-9)continue;g.fillText(o.yf?o.yf(i):String(+i.toFixed(2)),X(ox)-5,Y(i)+4);}
    if(o.xl)U.label(g,X(o.xr[1])-4,Y(oy)-12,o.xl,U.cssv('--eye'),'right');if(o.yl)U.label(g,X(ox)+8,Y(o.yr[1])+4,o.yl,U.cssv('--terrain'),'left');}
  return {g:g,w:w,h:h,X:X,Y:Y,inv:inv,kx:kx,ky:ky};}
function dot(P,x,y,col,r,txt,dx,dy){var g=P.g;g.beginPath();g.arc(P.X(x),P.Y(y),r||6,0,7);g.fillStyle=col;g.fill();g.lineWidth=1.6;g.strokeStyle='#fff';g.stroke();if(txt)U.label(g,P.X(x)+(dx==null?9:dx),P.Y(y)+(dy==null?-12:dy),txt,col,dx<0?'right':'left');}
function seg(P,a,b,col,wd,dash){var g=P.g;g.strokeStyle=col;g.lineWidth=wd||2;g.setLineDash(dash||[]);g.beginPath();g.moveTo(P.X(a[0]),P.Y(a[1]));g.lineTo(P.X(b[0]),P.Y(b[1]));g.stroke();g.setLineDash([]);}
function arr(P,a,b,col,wd){U.arrow2(P.g,P.X(a[0]),P.Y(a[1]),P.X(b[0]),P.Y(b[1]),col,wd||2.2);}
function circ(P,x,y,r,col,wd,dash,fill){var g=P.g;g.beginPath();g.ellipse(P.X(x),P.Y(y),Math.abs(r*P.kx),Math.abs(r*P.ky),0,0,7);if(fill){g.fillStyle=fill;g.fill();}g.strokeStyle=col;g.lineWidth=wd||1.6;g.setLineDash(dash||[]);g.stroke();g.setLineDash([]);}
/* 클릭 → 좌표 */
function onPick(cv,fn){cv.style.cursor='crosshair';cv.addEventListener('click',function(e){var r=cv.getBoundingClientRect();fn(e.clientX-r.left,e.clientY-r.top);});}
return {D2R:D2R,RE:RE,dist:dist,taxi:taxi,toPolar:toPolar,fromPolar:fromPolar,arc:arc,chord:chord,monthAngle:monthAngle,monthChord:monthChord,cyl:cyl,sph:sph,fromCyl:fromCyl,fromSph:fromSph,
  lonKm:lonKm,latKm:latKm,mercY:mercY,mercArea:mercArea,mercLen:mercLen,geoDist:geoDist,cToF:cToF,fToC:fToC,zscore:zscore,mean:mean,sd:sd,nearest:nearest,
  Plane:Plane,dot:dot,seg:seg,arr:arr,circ:circ,onPick:onPick};
})();

/* ── 페이지 공용 도우미 (브라우저 전용) ── */
var PG=(function(){
function V(cv,draw){var o={dirty:true};U.reg(cv,function(dt){if(o.dirty||dt===0){draw();o.dirty=false;}});return o;}
function rng(id,cb,f){var r=U.$('#'+id),v=U.$('#'+id+'v');function up(){if(v)v.textContent=f?f(+r.value):r.value;cb(+r.value);}r.addEventListener('input',up);up();return r;}
function set(id,val){var r=U.$('#'+id);r.value=val;r.dispatchEvent(new Event('input'));}
function txt(id,t){var e=U.$('#'+id);if(e)e.innerHTML=t;}
/* 판 넘기기 게임: o={el,n,title(i),setup(i),judge(i)→[통과?,문장],stars(맞힌 판 수)} — 조작하기 전에는 판정하지 않는다 */
function Rounds(o){var host=U.$(o.el),i=0,ok={},tries={},touched=false;
  host.innerHTML='<div class="gtitle" style="display:flex;gap:10px;align-items:center;flex-wrap:wrap"><span class="rt"></span><span class="gstar"></span></div><div class="rask"></div>'+
   '<div class="ctrl"><div class="group"><button class="bt" type="button" data-r="chk">확인</button><button class="bt" type="button" data-r="prev">← 앞 판</button><button class="bt" type="button" data-r="next">다음 판 →</button><button class="bt" type="button" data-r="reset">처음부터</button></div></div><div class="insight rres" aria-live="polite"></div><div class="glog rlog"></div>';
  var rt=U.$('.rt',host),star=U.$('.gstar',host),ask=U.$('.rask',host),res=U.$('.rres',host),log=U.$('.rlog',host),lines=[];
  function head(){rt.textContent=(i+1)+'판 / '+o.n+' · '+o.title(i);var k=Object.keys(ok).length;star.textContent='★'.repeat(k)+'☆'.repeat(o.n-k)+' '+k+'/'+o.n;}
  function go(k){i=Math.max(0,Math.min(o.n-1,k));res.innerHTML='';ask.innerHTML=o.ask?o.ask(i):'';o.setup(i);touched=false;head();}
  U.$('[data-r="chk"]',host).onclick=function(){if(!touched){res.innerHTML='<p class="a">먼저 조작판을 움직여 답을 정한 뒤 확인을 누르세요.</p>';return;}var r=o.judge(i);tries[i]=(tries[i]||0)+1;
    if(r[0]){ok[i]=1;res.innerHTML='<p class="g">통과! '+r[1]+'</p>';}else res.innerHTML='<p class="r">아직이에요. '+r[1]+'</p>';
    lines.unshift('<span class="glbl">'+(i+1)+'판 '+tries[i]+'회</span> '+(r[0]?'✔ ':'✘ ')+(r[2]||''));log.innerHTML=lines.slice(0,8).join('<br>');head();if(o.after)o.after(i,r[0]);};
  U.$('[data-r="prev"]',host).onclick=function(){go(i-1);};U.$('[data-r="next"]',host).onclick=function(){go(i+1);};
  U.$('[data-r="reset"]',host).onclick=function(){ok={};tries={};lines=[];log.innerHTML='';go(0);};
  go(0);return {touch:function(){touched=true;},cur:function(){return i;},passed:function(){return Object.keys(ok).length;}};}
return {V:V,rng:rng,set:set,txt:txt,Rounds:Rounds};
})();

/* ── 임시 표지 그림: 모눈 + 주제 도형 + "나는 여기" 핀 (픽셀 표지를 받으면 img로 바꾼다) ── */
SP.drawCover=function(cv,motif){if(!cv)return;U.reg(cv,function(dt){if(dt>0)return;var R=U.setup(cv),g=R.g,w=R.w,h=R.h,cx=w*0.5,cy=h*0.40,u=Math.min(w,h)/9,t=U.cssv('--terrain'),e=U.cssv('--eye'),a=U.cssv('--amber');
  g.fillStyle='#fbfdfd';g.fillRect(0,0,w,h);g.strokeStyle='rgba(15,127,134,.10)';g.lineWidth=1;for(var x=cx%u;x<w;x+=u){g.beginPath();g.moveTo(x,0);g.lineTo(x,h);g.stroke();}for(var y=cy%u;y<h;y+=u){g.beginPath();g.moveTo(0,y);g.lineTo(w,y);g.stroke();}
  function pin(px,py,lab){g.fillStyle=e;g.beginPath();g.arc(px,py-18,11,Math.PI,0);g.lineTo(px,py);g.closePath();g.fill();g.fillStyle='#fff';g.beginPath();g.arc(px,py-18,4.5,0,7);g.fill();U.label(g,px+14,py-26,lab||'나는 여기',e);}
  g.lineWidth=2;
  if(motif==='line'){U.arrow2(g,w*0.08,cy,w*0.92,cy,e,2.2);for(var k=-6;k<=6;k++){g.fillStyle=U.cssv('--muted');g.fillRect(cx+k*u-1,cy-6,2,12);g.font='12px '+U.cssv('--font');g.textAlign='center';g.fillText(String(k),cx+k*u,cy+22);}pin(cx+3*u,cy,'3');}
  else if(motif==='polar'){for(var r=1;r<=4;r++){g.strokeStyle='rgba(15,127,134,.35)';g.beginPath();g.arc(cx,cy,r*u*0.9,0,7);g.stroke();}for(var d=0;d<360;d+=30){var q=d*Math.PI/180;g.strokeStyle='rgba(15,127,134,.25)';g.beginPath();g.moveTo(cx,cy);g.lineTo(cx+Math.cos(q)*4*u*0.9,cy-Math.sin(q)*4*u*0.9);g.stroke();}
    var aa=53*Math.PI/180;U.arrow2(g,cx,cy,cx+Math.cos(aa)*3.6*u*0.9,cy-Math.sin(aa)*3.6*u*0.9,a,2.6);pin(cx+Math.cos(aa)*3.6*u*0.9,cy-Math.sin(aa)*3.6*u*0.9,'(5, 53°)');}
  else if(motif==='space'){var o=[cx-u*1.5,cy+u*1.6];U.arrow2(g,o[0],o[1],o[0]+u*4.5,o[1],e,2.2);U.arrow2(g,o[0],o[1],o[0]-u*2,o[1]+u*1.1,t,2.2);U.arrow2(g,o[0],o[1],o[0],o[1]-u*3.6,'#16212b',2.2);
    var P=[o[0]+u*2.6-u*0.8,o[1]+u*0.45-u*2.4];g.setLineDash([4,4]);g.strokeStyle='rgba(22,33,43,.4)';g.beginPath();g.moveTo(P[0],P[1]);g.lineTo(P[0],P[1]+u*2.4);g.stroke();g.setLineDash([]);pin(P[0],P[1],'(x, y, z)');}
  else if(motif==='globe'){var R0=u*3.2;g.strokeStyle='rgba(15,127,134,.5)';g.beginPath();g.arc(cx,cy,R0,0,7);g.stroke();for(var la=-60;la<=60;la+=30){var yy=cy-R0*Math.sin(la*Math.PI/180),rr=R0*Math.cos(la*Math.PI/180);g.beginPath();g.ellipse(cx,yy,rr,rr*0.18,0,0,7);g.stroke();}
    for(var lo=-60;lo<=60;lo+=30){g.beginPath();g.ellipse(cx,cy,Math.abs(R0*Math.sin(lo*Math.PI/180))+0.1,R0,0,0,7);g.stroke();}pin(cx+R0*0.45,cy-R0*0.55,'37.6°N · 127.0°E');}
  else if(motif==='data'){var pts=[[1.2,1.1],[1.6,1.8],[2.1,1.4],[-1.4,-1.0],[-2,-1.6],[-1.1,-1.9],[0.4,2.2],[-0.6,0.3]];pts.forEach(function(p,i){g.beginPath();g.arc(cx+p[0]*u,cy-p[1]*u,7,0,7);g.fillStyle=i<3?t:i<6?U.cssv('--stain'):U.cssv('--muted');g.fill();});U.arrow2(g,w*0.15,cy+u*2.6,w*0.85,cy+u*2.6,e,1.8);U.arrow2(g,w*0.2,h*0.92,w*0.2,h*0.05,t,1.8);pin(cx+0.3*u,cy-0.2*u,'새 손님');}
  else {U.arrow2(g,w*0.1,cy,w*0.9,cy,e,2.2);U.arrow2(g,cx,h*0.92,cx,h*0.05,t,2.2);g.fillStyle=U.cssv('--muted');g.font='12px '+U.cssv('--font');g.fillText('x',w*0.9-4,cy-10);g.fillText('y',cx+8,h*0.07);
    g.setLineDash([4,4]);g.strokeStyle='rgba(22,33,43,.35)';g.beginPath();g.moveTo(cx+3*u,cy);g.lineTo(cx+3*u,cy-2*u);g.lineTo(cx,cy-2*u);g.stroke();g.setLineDash([]);pin(cx+3*u,cy-2*u,'(3, 2)');}
});};
if(typeof module!=='undefined')module.exports=SP;
