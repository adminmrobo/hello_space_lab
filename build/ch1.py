# -*- coding: utf-8 -*-
"""1장 수직선 — 숫자 하나로 말하는 자리"""
NAV = [('#s11', '1.1 기준점'), ('#s12', '1.2 거리'), ('#s13', '1.3 눈금'), ('#app', '부록 게임'), ('#sum', '정리'), ('#kg', '색인'), ('#export', '꾸러미'), ('02_plane.html', '2장 →')]

PANEL11 = '''<div class="panel"><div class="ptitle">실험 ① 같은 길, 다른 숫자 — 기준점(원점)과 방향을 바꿔 보세요</div>
<div class="cwrap"><canvas id="cv11" aria-label="동서로 뻗은 길 위의 정류장·집·편의점·학교와, 고른 기준점에서 잰 위치 숫자"></canvas></div>
<div class="ctrl"><div class="group" role="group" aria-label="기준점 고르기"><span class="glabel">기준점(0)</span><button class="bt" type="button" data-o11="0" aria-pressed="true">집</button><button class="bt" type="button" data-o11="400" aria-pressed="false">학교</button><button class="bt" type="button" data-o11="150" aria-pressed="false">편의점</button></div>
<div class="group" role="group" aria-label="+ 방향 고르기"><span class="glabel">+ 방향</span><button class="bt" type="button" data-d11="1" aria-pressed="true">동쪽이 +</button><button class="bt" type="button" data-d11="-1" aria-pressed="false">서쪽이 +</button></div></div>
<div class="minis"><div class="mini a"><span>정류장의 숫자</span><b id="m11a">—</b></div><div class="mini m"><span>편의점의 숫자</span><b id="m11b">—</b></div><div class="mini g"><span>학교의 숫자</span><b id="m11c">—</b></div><div class="mini r"><span>집–학교 거리</span><b id="m11d">—</b></div></div>
<div class="insight" id="i11" aria-live="polite"></div></div>'''

PANEL12 = '''<div class="panel"><div class="ptitle">실험 ② 엘리베이터의 수직선 — 두 층을 골라 거리를 재 보세요</div>
<div class="twin"><div class="cwrap tall"><canvas id="cv12" aria-label="지하 3층부터 10층까지의 건물 단면과 높이 자"></canvas></div>
<div><div class="ctrl" style="flex-direction:column;align-items:flex-start"><label class="glabel" for="r12a">출발 층</label><div><input type="range" id="r12a" min="0" max="12" step="1" value="1"> <span class="val" id="r12av">B2</span></div>
<label class="glabel" for="r12b">도착 층</label><div><input type="range" id="r12b" min="0" max="12" step="1" value="7"> <span class="val" id="r12bv">5층</span></div></div>
<div class="minis" style="grid-template-columns:1fr 1fr"><div class="mini a"><span>층 번호끼리 뺀 값</span><b id="m12a">—</b></div><div class="mini g"><span>실제로 지나간 층 수</span><b id="m12b">—</b></div><div class="mini m"><span>높이 자로 잰 거리</span><b id="m12c">—</b></div><div class="mini r"><span>둘이 다른가?</span><b id="m12d">—</b></div></div></div></div>
<div class="insight" id="i12" aria-live="polite"></div></div>'''

PANEL13 = '''<div class="panel"><div class="ptitle">실험 ③ 두 개의 자를 나란히 — 섭씨 자와 화씨 자</div>
<div class="cwrap"><canvas id="cv13" aria-label="위는 섭씨 눈금, 아래는 화씨 눈금. 같은 온도가 두 자에서 다른 숫자로 읽힌다"></canvas></div>
<div class="ctrl"><div class="group"><label class="glabel" for="r13">오늘 기온 (섭씨)</label><input type="range" id="r13" min="-20" max="40" step="1" value="20"><span class="val" id="r13v">20°C</span>
<label class="glabel" for="r13b">비교할 기온 (섭씨)</label><input type="range" id="r13b" min="-20" max="40" step="1" value="30"><span class="val" id="r13bv">30°C</span></div></div>
<div class="minis"><div class="mini a"><span>오늘 기온 (화씨)</span><b id="m13a">—</b></div><div class="mini m"><span>비교 기온 (화씨)</span><b id="m13b">—</b></div><div class="mini g"><span>차이 (섭씨)</span><b id="m13c">—</b></div><div class="mini r"><span>차이 (화씨)</span><b id="m13d">—</b></div></div>
<div class="insight" id="i13" aria-live="polite"></div></div>'''

APP = '''<div class="gameintro"><b>게임 방법</b> 위쪽 자는 이미 읽을 줄 아는 자, 아래쪽 자는 처음 보는 자입니다. 아래 자에는 기준이 되는 눈금만 몇 개 적혀 있어요. 슬라이더로 아래 자의 숫자를 고른 뒤 <b>확인</b>을 누르세요. 네 판을 모두 통과하면 별 네 개입니다.</div>
<div class="panel game"><div class="ptitle">부록 게임 · 자 통역사 — 같은 자리를 다른 자의 숫자로</div>
<div class="cwrap"><canvas id="cvA" aria-label="위쪽 자와 아래쪽 자, 그리고 내가 고른 위치"></canvas></div>
<div class="ctrl"><div class="group"><label class="glabel" for="rA">아래 자에서의 숫자</label><input type="range" id="rA" min="0" max="1" step="1" value="0" style="width:260px"><span class="val" id="rAv">—</span></div></div>
<div id="gA"></div></div>'''

JS = r'''
/* 1.1 길 위의 원점 */
var PL=[['정류장',-100],['집',0],['편의점',150],['학교',400]],O11=0,D11=1;
function pos11(m){return (m-O11)*D11;}
var v11=V($('#cv11'),function(){var R=U.setup($('#cv11')),g=R.g,w=R.w,h=R.h;U.grid24(g,w,h);var L=w*0.08,Rr=w*0.92,y=h*0.55,X=function(m){return L+(m+200)/(650)*(Rr-L);};
  g.fillStyle='#e9eef2';g.fillRect(L-10,y-14,Rr-L+20,28);U.arrow2(g,L-10,y+30,Rr+10,y+30,U.cssv('--eye'),1.6);g.fillStyle=U.cssv('--muted');g.font='12px '+U.cssv('--font');g.textAlign='right';g.fillText(D11>0?'+ 방향 (동쪽)':'',Rr+10,y+48);g.textAlign='left';g.fillText(D11<0?'+ 방향 (서쪽)':'',L-10,y+48);
  for(var m=-200;m<=450;m+=50){var x=X(m);g.fillStyle='rgba(22,33,43,.35)';g.fillRect(x,y+24,1,12);}
  PL.forEach(function(p){var x=X(p[1]),on=p[1]===O11;g.fillStyle=on?U.cssv('--eye'):U.cssv('--terrain');g.beginPath();g.arc(x,y,on?10:7,0,7);g.fill();g.fillStyle=U.cssv('--text');g.textAlign='center';g.font='600 13px '+U.cssv('--font');g.fillText(p[0],x,y-24);
    U.label(g,x,y+66,(pos11(p[1])>0?'+':'')+pos11(p[1])+' m',on?U.cssv('--eye'):U.cssv('--info'),'center');});
  U.label(g,X(O11),y-48,'기준점 0',U.cssv('--eye'),'center');U.stamp(g,w,'설명용 예시');});
function up11(){$('#m11a').textContent=pos11(-100)+' m';$('#m11b').textContent=pos11(150)+' m';$('#m11c').textContent=pos11(400)+' m';$('#m11d').textContent=Math.abs(pos11(400)-pos11(0))+' m';
  var on=PL.filter(function(p){return p[1]===O11;})[0][0];
  U.ins($('#i11'),[['m','기준점이 <b>'+on+'</b>, + 방향이 <b>'+(D11>0?'동쪽':'서쪽')+'</b>일 때 학교는 '+pos11(400)+' m입니다. 숫자는 바뀌었지만 학교는 한 걸음도 움직이지 않았어요.'],['g','두 곳 사이 거리(집–학교 400 m)는 기준점이나 방향을 바꿔도 그대로입니다. 위치를 말하려면 <b>기준점·방향·눈금</b> 세 가지를 함께 말해야 합니다.']]);v11.dirty=true;}
$$('[data-o11]').forEach(function(b){b.onclick=function(){O11=+b.dataset.o11;$$('[data-o11]').forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});up11();};});
$$('[data-d11]').forEach(function(b){b.onclick=function(){D11=+b.dataset.d11;$$('[data-d11]').forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});up11();};});up11();

/* 1.2 엘리베이터: 층 번호 자(0 없음) vs 높이 자 */
var FL=[-3,-2,-1,1,2,3,4,5,6,7,8,9,10],FH=3.5;function fname(f){return f<0?'B'+(-f):f+'층';}
function lev(f){return f<0?f:f-1;} /* 로비(1층) 바닥 = 0 m 기준, 지하는 아래로 */
var a12=1,b12=7;
var v12=V($('#cv12'),function(){var R=U.setup($('#cv12')),g=R.g,w=R.w,h=R.h;U.grid24(g,w,h);var top=24,bot=h-20,n=FL.length,fh=(bot-top)/n,bx=w*0.30,bw=Math.min(w*0.34,220);
  function Y(f){return bot-(lev(f)+3)*fh;}
  g.fillStyle='#d8ecd9';g.fillRect(bx-30,Y(1)+fh-2,bw+60,4);g.fillStyle=U.cssv('--muted');g.font='11px '+U.cssv('--font');g.textAlign='left';g.fillText('땅',bx-26,Y(1)+fh+12);
  FL.forEach(function(f){var y=Y(f);var sel=(f===FL[a12]||f===FL[b12]);var lo=Math.min(lev(FL[a12]),lev(FL[b12])),hi=Math.max(lev(FL[a12]),lev(FL[b12]));var inr=lev(f)>=lo&&lev(f)<hi;
    g.fillStyle=sel?'rgba(201,48,44,.18)':inr?'rgba(15,127,134,.10)':(f<0?'#eef0f3':'#f7f9fb');g.fillRect(bx,y,bw,fh-2);g.strokeStyle=U.cssv('--rule');g.strokeRect(bx+.5,y+.5,bw-1,fh-3);
    g.fillStyle=U.cssv('--text');g.font=(sel?'700 ':'')+'12.5px '+U.cssv('--font');g.textAlign='right';g.fillText(fname(f),bx-8,y+fh/2+4);
    g.textAlign='left';g.fillStyle=U.cssv('--info');g.fillText((lev(f)*FH>=0?'+':'')+(lev(f)*FH).toFixed(1)+' m',bx+bw+8,y+fh-4);});
  g.fillStyle=U.cssv('--muted');g.textAlign='center';g.fillText('층 번호 자',bx-30,14);g.fillText('높이 자 (1층 바닥 = 0)',bx+bw+50,14);
  var ya=Y(FL[a12])+fh/2,yb=Y(FL[b12])+fh/2;U.arrow2(g,bx+bw/2,ya,bx+bw/2,yb,U.cssv('--eye'),2.4);U.stamp(g,w,'층고 3.5 m 가정');});
function up12(){var fa=FL[a12],fb=FL[b12],naive=Math.abs(fb-fa),real=Math.abs(lev(fb)-lev(fa)),m=real*FH;
  $('#m12a').textContent=naive+'층';$('#m12b').textContent=real+'층';$('#m12c').textContent=m.toFixed(1)+' m';$('#m12d').textContent=naive===real?'같다':'다르다';
  var it=[['m',fname(fa)+'에서 '+fname(fb)+'까지 실제로 지나간 층은 '+real+'층, 높이로는 '+m.toFixed(1)+' m입니다.']];
  if(naive!==real)it.push(['r','층 번호끼리 빼면 '+naive+'이 나오지만 틀린 값이에요. 우리 건물 층 번호에는 <b>0층이 없어서</b> B1 바로 위가 1층입니다. 이 자는 눈금 간격이 한 곳에서 고르지 않습니다.']);
  else it.push(['g','두 층이 땅 위(또는 땅 아래) 한쪽에만 있으면 빼기만 해도 맞습니다. 출발을 지하로 옮겨 보세요.']);
  U.ins($('#i12'),it);v12.dirty=true;}
rng('r12a',function(v){a12=v;up12();},function(v){return fname(FL[v]);});rng('r12b',function(v){b12=v;up12();},function(v){return fname(FL[v]);});

/* 두 자를 나란히 그리는 도우미: 위 자 [lo,hi] 위의 값 v를 아래 자 함수 f로 읽는다 */
function dual(cv,o){var R=U.setup(cv),g=R.g,w=R.w,h=R.h;U.grid24(g,w,h);var L=w*0.06,Rr=w*0.94,y1=h*0.30,y2=h*0.70,X=function(v){return L+(v-o.lo)/(o.hi-o.lo)*(Rr-L);};
  [[y1,o.top,U.cssv('--terrain')],[y2,o.bot,U.cssv('--stain')]].forEach(function(r){g.strokeStyle=r[2];g.lineWidth=2;g.beginPath();g.moveTo(L,r[0]);g.lineTo(Rr,r[0]);g.stroke();U.label(g,L,r[0]-30,r[1],r[2]);});
  g.font='11.5px '+U.cssv('--font');g.textAlign='center';
  o.ticksTop.forEach(function(t){var x=X(t);g.fillStyle=U.cssv('--terrain');g.fillRect(x-.5,y1-6,1.2,12);g.fillText(o.ft?o.ft(t):String(t),x,y1+20);});
  o.ticksBot.forEach(function(t){var x=X(t[0]);g.fillStyle=U.cssv('--stain');g.fillRect(x-.5,y2-6,1.2,12);g.fillText(t[1],x,y2+20);});
  return {g:g,w:w,h:h,X:X,y1:y1,y2:y2};}

/* 1.3 섭씨·화씨 */
var c13=20,d13=30;
var v13=V($('#cv13'),function(){var T=[],B=[];for(var c=-20;c<=40;c+=10)T.push(c);for(var f=0;f<=100;f+=20)B.push([SP.fToC(f),f+'°F']);
  var D=dual($('#cv13'),{lo:-20,hi:40,top:'섭씨 자 (°C) — 0 = 물이 어는 온도',bot:'화씨 자 (°F) — 0 = 다른 기준점',ticksTop:T,ticksBot:B,ft:function(t){return t+'°C';}});
  [[c13,U.cssv('--amber'),'오늘'],[d13,U.cssv('--eye'),'비교']].forEach(function(p){var x=D.X(p[0]);D.g.setLineDash([4,3]);D.g.strokeStyle=p[1];D.g.lineWidth=2;D.g.beginPath();D.g.moveTo(x,D.y1-14);D.g.lineTo(x,D.y2+14);D.g.stroke();D.g.setLineDash([]);
    U.label(D.g,x,D.y2+40,p[2]+' '+fmt(SP.cToF(p[0]),0)+'°F',p[1],'center');});
  var x0=D.X(0);U.label(D.g,x0,D.y1-14,'0°C = 32°F',U.cssv('--muted'),'center');});
function up13(){var fa=SP.cToF(c13),fb=SP.cToF(d13);$('#m13a').textContent=fmt(fa,0)+'°F';$('#m13b').textContent=fmt(fb,0)+'°F';$('#m13c').textContent=Math.abs(d13-c13)+'°C';$('#m13d').textContent=fmt(Math.abs(fb-fa),0)+'°F';
  U.ins($('#i13'),[['m','같은 온도인데 숫자가 다릅니다. 화씨 자는 <b>기준점</b>(0의 자리)도 다르고 <b>눈금 간격</b>도 다르기 때문이에요. 0°C는 화씨 자에서 32입니다.'],['g','차이로 보면 섭씨 '+Math.abs(d13-c13)+'도 = 화씨 '+fmt(Math.abs(fb-fa),0)+'도. 차이에는 기준점이 빠지고 <b>눈금 배율 1.8</b>만 남습니다.']]);v13.dirty=true;}
rng('r13',function(v){c13=v;up13();},function(v){return v+'°C';});rng('r13b',function(v){d13=v;up13();},function(v){return v+'°C';});

/* 부록 게임: 자 통역사 */
var GR=[
 {t:'기준점 옮기기',ask:'위 자는 <b>집 = 0, 동쪽 +</b>. 편의점은 +150 m에 있습니다. 아래 자는 <b>학교 = 0</b>(동쪽 +)입니다. 아래 자에서 편의점의 숫자는?',
  lo:-200,hi:450,src:150,top:'집 = 0 인 자 (m)',ticksTop:[-100,0,150,400],bot:'학교 = 0 인 자 (m)',ticksBot:[[400,'0 (학교)']],min:-600,max:200,step:10,ans:-250,tol:0,u:' m',map:function(v){return v+400;},
  why:'편의점은 학교에서 서쪽으로 250 m. 동쪽이 +이니 −250 m입니다.'},
 {t:'방향 뒤집기',ask:'아래 자는 <b>집 = 0, 서쪽이 +</b>입니다. 학교(위 자에서 +400 m)는 아래 자에서 몇일까요?',
  lo:-200,hi:450,src:400,top:'집 = 0, 동쪽 + (m)',ticksTop:[-100,0,150,400],bot:'집 = 0, 서쪽 + (m)',ticksBot:[[0,'0 (집)'],[-100,'+100']],min:-600,max:600,step:10,ans:-400,tol:0,u:' m',map:function(v){return -v;},
  why:'학교는 집의 동쪽 400 m. 서쪽이 +인 자에서는 −400 m입니다.'},
 {t:'눈금 바꾸기 (온도)',ask:'오늘 기온은 <b>25°C</b>입니다. 아래 화씨 자에는 0°C = 32°F, 100°C = 212°F만 적혀 있어요. 25°C는 화씨로?',
  lo:-10,hi:110,src:25,top:'섭씨 자 (°C)',ticksTop:[0,25,50,100],bot:'화씨 자 (°F)',ticksBot:[[0,'32'],[100,'212']],min:0,max:240,step:1,ans:77,tol:1,u:'°F',map:function(v){return SP.fToC(v);},
  why:'0~100°C가 32~212°F, 곧 1°C마다 1.8°F. 25 × 1.8 + 32 = 77°F.'},
 {t:'표준화 자',ask:'반 평균 키 160 cm, 표준편차 5 cm. <b>170 cm</b>는 "평균 = 0, 표준편차 = 1눈금"인 표준화 자에서 몇일까요?',
  lo:140,hi:180,src:170,top:'키 자 (cm)',ticksTop:[150,160,170,180],bot:'표준화 자 (평균 0, 눈금 1 = 5 cm)',ticksBot:[[160,'0 (평균)'],[165,'?']],min:-3,max:3,step:0.1,ans:2,tol:0.05,u:'',map:function(v){return 160+5*v;},
  why:'평균에서 10 cm 위, 눈금 하나가 5 cm이니 10 ÷ 5 = 2. 2장 이후 거리 계산에서 이 자가 다시 나옵니다(6장).'}];
var gv=0,G;
var vA=V($('#cvA'),function(){var r=GR[G?G.cur():0];var D=dual($('#cvA'),{lo:r.lo,hi:r.hi,top:r.top,bot:r.bot,ticksTop:r.ticksTop,ticksBot:r.ticksBot});
  var xs=D.X(r.src);U.label(D.g,xs,D.y1-14,'알고 있는 자리',U.cssv('--terrain'),'center');D.g.beginPath();D.g.arc(xs,D.y1,7,0,7);D.g.fillStyle=U.cssv('--terrain');D.g.fill();
  var xp=D.X(Math.max(r.lo,Math.min(r.hi,r.map(gv))));D.g.beginPath();D.g.arc(xp,D.y2,8,0,7);D.g.fillStyle=U.cssv('--amber');D.g.fill();U.label(D.g,xp,D.y2+40,'내 답 '+(+gv.toFixed(2))+r.u,U.cssv('--amber'),'center');});
G=PG.Rounds({el:'#gA',n:GR.length,title:function(i){return GR[i].t;},ask:function(i){return '<p>'+GR[i].ask+'</p>';},
  setup:function(i){var r=GR[i],s=$('#rA');s.min=r.min;s.max=r.max;s.step=r.step;s.value=r.min+(r.max-r.min)/2;gv=+s.value;$('#rAv').textContent=(+gv.toFixed(2))+r.u;vA.dirty=true;},
  judge:function(i){var r=GR[i],ok=Math.abs(gv-r.ans)<=r.tol+1e-9;return [ok,ok?r.why:(gv>r.ans?'조금 큽니다.':'조금 작습니다.')+' 위 자의 점과 아래 자의 점이 같은 자리에 오도록 맞춰 보세요.',(+gv.toFixed(2))+r.u];}});
$('#rA').addEventListener('input',function(){gv=+this.value;$('#rAv').textContent=(+gv.toFixed(2))+GR[G.cur()].u;G.touch();vA.dirty=true;});
'''

DLG = {
 'open': [['doc', 'doc_board', '좌표 첫걸음 첫 시간입니다. 질문 하나로 시작할게요. 지금 이 강의실에서 여러분은 어디에 있나요?'],
          ['sia', 'sia_explain', '음… 앞에서 두 번째 줄이요! 아니, 문에서 세 걸음?'],
          ['moa', 'moa_report', '문 기준이냐 칠판 기준이냐에 따라 답이 달라지는데요?'],
          ['doc', 'doc_front', '바로 그거예요. 위치를 말하려면 <b>어디서부터, 어느 쪽으로, 얼마씩</b>을 먼저 정해야 합니다. 오늘은 숫자 하나로 위치를 말하는 자, 수직선부터 시작해요.'],
          ['x2', 'x2_hint', '(필기 중) 어디서부터… 어느 쪽… 얼마씩…'],
          ['asst', 'asst_smile', '조교 하루입니다. 식이 나오면 제가 숫자로 풀어 드릴게요. 막히면 언제든 물어보세요.']],
 's11_t': [['doc', 'doc_front', '집, 편의점, 학교가 한 길 위에 있어요. 학교의 위치를 숫자 하나로 말해 볼까요?'],
           ['robo', 'robo_calc', '학교는 400! 계산 끝!'],
           ['fly', 'fly_point', '그 400은 어디서 잰 거야? 기준점 버튼을 학교로 바꿔 봐.']],
 's12_t': [['doc', 'doc_front', '이번에는 건물을 세워 봅시다. 엘리베이터도 위아래로 한 줄인 수직선이에요.'],
           ['sia', 'sia_think', '지하 2층에서 5층이면 5 − (−2) = 7층 올라가는 거죠?'],
           ['fly', 'fly_point', '출발을 B2, 도착을 5층에 두고 "실제로 지나간 층 수"를 봐.']],
 's13_t': [['doc', 'doc_front', '미국 여행 중 일기예보에 "내일 86도"가 나왔습니다. 물이 끓는 날씨일까요?'],
           ['x3', 'x3_hint', '86도요?! 사우나인가요?'],
           ['fly', 'fly_point', '두 자를 나란히 놓고 슬라이더를 30°C에 둬 봐.']],
 'ai12_d': [['robo', 'robo_coin', '지하 2층(−2)에서 5층까지 층고 3.5 m씩이면 (5 − (−2)) × 3.5 = 24.5 m! 1초 만에 끝!']],
 'ai12_e': [['robo', 'robo_sigh', '0층이 없는 자였구나… 6층 × 3.5 = 21 m로 고쳤어요. 자의 눈금 규칙부터 볼게요.']],
 'app': [['x3', 'x3_hint', '게임 시간이다!'],
         ['asst', 'asst_firm', '네 판 모두 "같은 자리를 다른 자로 읽기"예요. 자가 바뀌어도 자리는 그대로라는 걸 기억하세요.'],
         ['robo', 'robo_smile', '막히면 위 자의 점에서 아래로 곧게 내려와 보세요!']],
 'outro': [['doc', 'doc_magic', '오늘의 세 줄입니다.<br>① 위치를 말하려면 기준점·방향·눈금 세 가지를 정한다.<br>② 두 곳 사이 거리는 기준점을 바꿔도 그대로다. 다만 눈금이 고른 자여야 한다.<br>③ 눈금을 바꾸면 숫자가 바뀐다. 표준화도 "평균을 0, 표준편차를 눈금 하나"로 바꾼 자다.'],
           ['moa', 'moa_tea', '0층 없는 건물, 오늘 집에 가서 엘리베이터 버튼부터 볼래요.'],
           ['x1', 'x1_hint', '(손을 든다) 숫자 하나로 모자라면요? 운동장 한가운데는요?'],
           ['doc', 'doc_think', '좋은 질문이에요. 운동장은 앞뒤로도 좌우로도 넓죠. 숫자가 두 개 필요합니다. 다음 시간, 좌표평면에서 만나요.']],
}

PAGE = dict(
 key='ch1', out='01_number_line.html', logo='1장',
 title='좌표 첫걸음 1장 수직선 — 숫자 하나로 말하는 자리 | 나는 어디에 있는가?',
 desc='좌표 첫걸음 1장. 기준점·방향·눈금 세 가지로 위치를 숫자 하나에 담는 수직선. 길 위의 원점 바꾸기, 0층 없는 엘리베이터, 섭씨·화씨 두 자, 표준화 자까지 직접 움직여 봅니다.',
 nav=NAV,
 cover=dict(cap='좌표 첫걸음 · 1교시', chip='1장 수직선 — 숫자 하나로 말하는 자리', cast=['fly_point', 'doc_board', 'asst_smile', 'robo_calc', 'sia_explain', 'moa_report', 'x1_hint', 'x2_hint', 'x3_hint'], alt='흰 강의실. 칠판의 긴 수직선과 빛나는 0 눈금을 박사가 가리키고, 하루는 온도계 두 개를, 주판봇은 엘리베이터 층을 세고, 초파리 연구원은 돋보기를 든다. 앞줄 시아·모아, 뒷줄 X1~X3.', motif='line'),
 eyebrow='좌표 첫걸음 · 1장 · 최적화 첫걸음의 자매편 <span class="diff">난이도: 산책</span>',
 h1='1장 수직선 — 숫자 하나로 말하는 자리',
 question='"나는 어디에 있는가?"에 숫자 하나로 답하려면 무엇을 먼저 정해야 할까?',
 lead='위치는 숫자 하나로도 말할 수 있습니다. 단, 그 숫자가 <b>어디서부터</b>(기준점), <b>어느 쪽으로</b>(방향), <b>얼마씩</b>(눈금) 잰 것인지 함께 정해 둘 때만요. 이 장은 길·건물·온도계 세 장면에서 이 세 가지를 하나씩 바꿔 보며, 같은 자리가 왜 다른 숫자로 읽히는지 봅니다.',
 start='1.1 → 1.2 → 1.3 순서로 보세요. 장 끝 <a href="#app">부록 게임 「자 통역사」</a>로 복습합니다. 2장에서는 숫자가 두 개, 세 개로 늘어납니다.',
 kpis=[('m', '3가지', '위치를 말할 때 정할 것 (기준점·방향·눈금)'), ('g', '400 m', '기준점을 바꿔도 그대로인 집–학교 거리'), ('r', '6층', 'B2 → 5층, 실제로 지나간 층 (7층 아님)'), ('a', '77°F', '25°C를 화씨 자로 읽은 값')],
 plain=[('무엇을', '숫자 하나로 위치를 말하는 자, 수직선을 길·엘리베이터·온도계로 봅니다.'),
        ('왜 중요한가', '지도 앱의 좌표, 데이터의 숫자, AI의 입력값 모두 "어떤 자로 잰 숫자"입니다. 자를 모르고 숫자만 보면 엉뚱하게 읽습니다.'),
        ('업무에서는', '보고서의 숫자를 받으면 "기준이 어디고, 단위가 무엇이냐"를 먼저 묻는 습관이 생깁니다. 표준화 점수도 읽을 수 있게 됩니다.')],
 abbr=[('0 (원점)', '기준점', '숫자 0이 놓인 자리. 어디에 둘지는 사람이 정한다.'), ('|a − b|', '절댓값', '두 숫자의 차이에서 부호를 뗀 값. 거리를 잴 때 쓴다.'),
       ('°C · °F', '섭씨 · 화씨', '기준점과 눈금이 다른 두 온도 자.'), ('z', '표준화 점수', '평균에서 표준편차 몇 개만큼 떨어졌는지.')],
 hex='1', open_title='숫자 하나로 위치 말하기',
 bigpicture='<div class="chain" aria-label="이 시리즈 지도"><span><b>1장 수직선</b></span><i>→</i><span>2장 좌표평면</span><i>→</i><span>3장 극좌표</span><i>→</i><span>4장 공간좌표</span><i>→</i><span>5장 지구와 지도</span><i>→</i><span>6장 데이터의 좌표</span><i>→</i><span>최적화 첫걸음</span></div>',
 steps=[
  dict(id='s11', num='1.1', title='기준점이 없으면 위치도 없다', tags=['방법: 원점·방향 정하기', '일상: 동네 길', '바탕: 자와 각도기의 방 0편'],
       why=dict(problem='"학교는 400이야"라는 말만으로는 학교가 어디인지 알 수 없습니다.', limit='말로 하는 위치("편의점 지나서 조금")는 사람마다 다르게 알아듣습니다.',
                solve='기준점(0)을 하나 정하고, + 방향을 정하고, 1눈금의 길이를 정합니다. 그러면 모든 자리가 숫자 하나가 됩니다.', easy='"우리 집 대문에서 동쪽으로 400걸음"처럼 출발점과 방향과 걸음 크기를 함께 말하는 것.'),
       math=dict(who='moa', q='기준점을 학교로 바꾸면 집은 −400이 되잖아요. 그럼 집–학교 거리도 바뀌어요?', words='두 자리의 숫자는 둘 다 같은 양만큼 밀립니다. 그래서 둘의 차이는 그대로예요. 기준점은 숫자에만 영향을 주고 거리에는 영향을 주지 않습니다.',
                 school='수직선 위의 두 점 사이 거리, 절댓값', rows=[('|b − a|', '비 빼기 에이의 절댓값', '두 점 사이 거리'), ('x − c', '엑스 빼기 씨', '기준점을 c로 옮겼을 때의 새 숫자')],
                 tries=['집 기준: 집 0, 학교 400 → |400 − 0| = 400 m', '학교 기준: 집 −400, 학교 0 → |0 − (−400)| = 400 m', '거리는 그대로 400 m'], comment='기준점은 "0을 어디에 꽂느냐"일 뿐이네요. 거리는 안 바뀌어요!'),
       daily='같은 약속 장소도 "역에서 5분"과 "회사에서 10분"처럼 기준에 따라 다르게 말합니다. 장소가 바뀐 게 아니라 기준이 바뀐 것이죠.',
       field='데이터의 숫자도 기준이 있습니다. 온도·연도·주가 지수처럼 0의 자리를 사람이 정한 숫자가 많아요. 6장에서 데이터를 점으로 놓을 때 이 기준을 다시 만납니다.',
       panel=PANEL11,
       doc='위치의 숫자는 "자리 + 자"의 합작품입니다. 숫자를 받으면 자(기준점·방향·눈금)부터 확인하세요. 그래야 같은 자리를 다른 숫자로 적은 자료끼리 비교할 수 있습니다.',
       limit='길이 한 줄일 때만 숫자 하나로 충분합니다. 운동장처럼 넓은 곳은 숫자가 하나 더 필요합니다(2장).'),
  dict(id='s12', num='1.2', title='두 자리 사이의 거리 — 눈금이 고르다면', tags=['방법: 차이의 절댓값', '일상: 엘리베이터', '판단: 0층 없는 자'],
       why=dict(problem='두 자리가 얼마나 떨어졌는지 숫자 하나로 말하고 싶습니다.', limit='층 번호, 등수, 번호표처럼 "눈금이 고르지 않은" 숫자는 그냥 빼면 틀립니다.',
                solve='눈금이 어디서나 같은 자(높이 자, m)로 바꾼 뒤 빼고 부호를 뗍니다.', easy='층 번호 대신 줄자로 높이를 재서 비교하는 것.'),
       math=dict(who='sia', q='−2에서 5까지면 7 아니에요? 수학 시간에 그렇게 배웠는데요.', words='수학의 수직선은 눈금이 어디서나 1로 고릅니다. 그 자 위에서는 7이 맞아요. 그런데 건물 층 번호는 B1 다음이 1층이라, 0이 빠진 자리에서 눈금 하나가 사라집니다.',
                 school='수직선, 절댓값, 정수의 뺄셈', rows=[('|5 − (−2)|', '오 빼기 음이의 절댓값', '고른 자라면 거리 7'), ('6 × 3.5', '육 곱하기 삼 점 오', '실제 층 수 × 층고 = 높이 차이')],
                 tries=['B2 → B1 → 1 → 2 → 3 → 4 → 5: 지나간 층은 6개', '높이 자: B2 바닥 −7 m, 5층 바닥 +14 m', '|14 − (−7)| = 21 m = 6층 × 3.5 m'], comment='빼기가 틀린 게 아니라, 자가 고르지 않았던 거예요!'),
       daily='번호표 15번과 20번 사이에 손님이 꼭 5명은 아닙니다. 취소된 번호가 있으면 눈금이 빠지죠.',
       field='등급(1등급·2등급), 만족도(매우 불만~매우 만족)처럼 순서만 있는 숫자는 빼서 거리로 쓰면 위험합니다. 데이터 분석에서 "순서형 자료"를 따로 다루는 이유입니다.',
       panel=PANEL12,
       ai=dict(id='ai12', title='조교 주판봇의 1초 답, 믿어도 될까?', checks=['층 번호 자의 눈금 간격은 어디서나 같은가?', '24.5 m는 7층 높이다. 실제로 지나간 층이 7개인가?'],
               verdict='층 번호에는 0층이 없어 B1과 1층 사이 눈금이 빠져 있습니다. 실제로 지나간 층은 6개, 높이는 6 × 3.5 = <b>21 m</b>입니다. 위 실험에서 출발 B2, 도착 5층으로 확인해 보세요.'),
       doc='빼기는 눈금이 고른 자에서만 거리가 됩니다. 숫자를 빼기 전에 "이 자의 눈금은 어디서나 같은가?"를 한 번 물어보세요.',
       limit='여기서는 층고를 모두 3.5 m로 단순하게 봤어요. 실제 건물은 로비 층이 더 높기도 합니다.'),
  dict(id='s13', num='1.3', title='눈금을 바꾸면 숫자가 바뀐다 — 섭씨·화씨, 그리고 표준화', tags=['방법: 기준점 이동 + 눈금 배율', '일상: 일기예보', 'AI: 표준화'],
       why=dict(problem='같은 온도를 나라마다 다른 숫자로 말합니다. 섞어 쓰면 오해가 생겨요.', limit='1.1에서는 기준점만 옮겼습니다. 화씨는 눈금 간격까지 다릅니다.',
                solve='"새 숫자 = 배율 × 옛 숫자 + 기준점 이동"으로 바꿉니다. 화씨는 배율 1.8, 이동 32.', easy='원화를 달러로 바꾸는 환율처럼, 자를 바꾸는 환율이 있다.'),
       math=dict(who='moa', q='화씨 86도는 섭씨로 몇 도예요? 끓는 날씨는 아니죠?', words='섭씨 0~100도 사이를 화씨는 32~212로 나눴습니다. 100도 구간을 180으로 나눴으니 눈금 하나가 1.8배 촘촘해요. 기준점 32를 빼고 1.8로 나누면 섭씨가 됩니다.',
                 school='일차함수 y = ax + b (a = 기울기, b = y절편)', rows=[('F = 1.8C + 32', '에프는 일 점 팔 씨 더하기 삼십이', '섭씨를 화씨로'), ('z = (x − 평균) ÷ 표준편차', '제트는 엑스 빼기 평균, 나누기 표준편차', '표준화: 기준점을 평균으로, 눈금을 표준편차로')],
                 tries=['86 − 32 = 54', '54 ÷ 1.8 = 30 → 섭씨 30°C, 더운 여름날', '거꾸로: 30 × 1.8 + 32 = 86°F'], comment='자를 바꾸는 식은 중학교 일차함수였어요. 배율이 기울기, 기준점 이동이 y절편!'),
       daily='여행 앱이 온도를 자동으로 바꿔 주지만, 단위 표시가 빠진 숫자 하나만 받으면 30인지 86인지 헷갈립니다.',
       field='머신러닝은 키(cm)·몸무게(kg)·소득(만원)처럼 자가 다른 숫자를 함께 씁니다. 그래서 각 숫자를 <b>표준화</b>(평균을 0, 표준편차를 눈금 하나로)해서 같은 자로 맞춥니다. 6장에서 이 자가 거리 계산을 어떻게 바꾸는지 봅니다.',
       panel=PANEL13,
       doc='눈금을 바꾸는 일은 "배율 × 옛 숫자 + 이동", 이 한 줄입니다. 표준화 점수 2는 "평균에서 표준편차 두 개만큼 위"라는 뜻으로 읽으면 됩니다.',
       code=[('(x - x.mean()) / x.std()', '표준화: 평균을 빼고 표준편차로 나눈다'), ('c * 1.8 + 32', '섭씨를 화씨로')],
       limit='온도처럼 0의 자리를 사람이 정한 자에서는 "20도는 10도의 두 배 따뜻하다"라는 말이 성립하지 않습니다. 길이·무게처럼 0이 진짜 "없음"인 자에서만 배수로 말할 수 있어요.'),
 ],
 app_title='자 통역사 — 같은 자리를 다른 자의 숫자로', app_lead='배운 세 가지(기준점·방향·눈금)를 한 판씩 바꿔 가며 통역합니다. 마지막 판은 6장에서 다시 쓰는 표준화 자입니다.', app_html=APP,
 sum_title='숫자 하나로 위치를 말하는 법',
 summary=[('위치를 말하려면?', '기준점(0)·+ 방향·눈금 하나의 길이를 정한다.', '1.1'), ('거리는?', '두 숫자의 차이에서 부호를 뗀 값. 단, 눈금이 고른 자에서만.', '1.2'),
          ('자를 바꾸면?', '새 숫자 = 배율 × 옛 숫자 + 기준점 이동. 화씨는 1.8배 + 32.', '1.3'), ('표준화는?', '평균을 0, 표준편차를 눈금 하나로 바꾼 자.', '1.3·부록')],
 cards=[('원점(기준점)', '숫자 0이 놓인 자리.'), ('수직선', '한 줄 위의 자리를 숫자 하나로 적는 자.'), ('거리', '두 자리 숫자의 차이의 절댓값.'), ('눈금(단위)', '숫자 1이 나타내는 실제 길이.'), ('순서형 자료', '순서만 있고 눈금이 고르지 않은 숫자(등급·층 번호).'), ('표준화', '평균 0, 표준편차 1인 자로 바꾸기.')],
 limits=['길 위의 거리(m)와 층고(3.5 m)는 설명용 숫자입니다.', '한 줄 위의 위치만 다뤘습니다. 넓은 곳은 숫자 두 개가 필요합니다(2장).'],
 next=[('02_plane.html', '2장 좌표평면 →', '두 숫자로 찍는 점, 피타고라스 거리, 보물찾기'), ('index.html', '목차', '강의 계획표')],
 refs=[('안상선, 「자와 각도기의 방 — 시아·모아의 유클리드 공간」 0편 가방 점검 (euclidean_space_lab)', '1.1 모눈과 자의 출발점 — 기준점·눈금이라는 생각'),
       ('안상선, 「최적화 첫걸음 ⓪~②」 (optimization_3d_map)', '자매편 구성과 난이도 표시(산책·오르막), "가정 상자" 형식'),
       ('안상선, 「우연의 과학통계학」 통계 노트 (statistics_note)', '1.3·부록 표준화 점수 z = (x − 평균) ÷ 표준편차')],
 examples=['길 위의 정류장·집·편의점·학교 위치(m)', '층고 3.5 m, 지하 3층~10층 건물', '반 평균 키 160 cm, 표준편차 5 cm'],
 dlg=DLG, js=JS,
 gloss={'기준점': ['기준점 (원점)', '좌표', '숫자 0을 놓는 자리. 사람이 정한다.'], '절댓값': ['절댓값', '수학', '부호를 뗀 크기. |−3| = 3.'], '표준화': ['표준화', '통계', '평균을 빼고 표준편차로 나누어 평균 0, 눈금 1인 자로 바꾸는 일.'],
        '표준편차': ['표준편차', '통계', '값들이 평균에서 평균적으로 얼마나 흩어져 있는지.'], '순서형 자료': ['순서형 자료', '통계', '순서만 의미 있고 간격은 고르지 않은 자료.'], '눈금': ['눈금 (단위)', '좌표', '숫자 1이 나타내는 실제 크기.']},
 gloss_core=['기준점', '절댓값', '표준화', '표준편차', '순서형 자료'],
 quiz={'s11': [{'q': '기준점을 집에서 학교로 바꾸면 집–학교 거리는?', 'o': ['그대로 400 m', '0 m가 된다', '−400 m가 된다'], 'a': 0, 'why': '두 숫자가 같은 양만큼 밀리므로 차이는 그대로입니다.', 'hint': '실험 ①의 빨간 거리 숫자를 보세요.'}],
       's12': [{'q': '0층이 없는 건물에서 B1에서 3층까지 지나간 층 수는?', 'o': ['3층', '4층', '2층'], 'a': 0, 'why': 'B1 → 1 → 2 → 3, 세 번 올라갑니다. 3 − (−1) = 4는 0층이 있을 때의 값이에요.', 'hint': '층 버튼을 하나씩 세어 보세요.'}],
       's13': [{'q': '화씨 50°F는 섭씨로?', 'o': ['10°C', '18°C', '27.8°C'], 'a': 0, 'why': '(50 − 32) ÷ 1.8 = 10°C.', 'hint': '기준점 32를 먼저 빼세요.'},
               {'q': '평균 70점, 표준편차 10점인 시험에서 표준화 점수 −1은?', 'o': ['60점', '69점', '80점'], 'a': 0, 'why': '평균에서 눈금(10점) 하나 아래 = 60점.', 'hint': '눈금 하나 = 표준편차.'}]},
)

KG = dict(
 nodes=[('Concept', 'origin', '원점(기준점)', 'Origin', '#s11', '숫자 0을 놓는 자리. 위치를 말하기 전에 사람이 정한다.'),
        ('Concept', 'number-line', '수직선', 'Number line', '#s11', '한 줄 위의 자리를 숫자 하나로 적는 자.'),
        ('Concept', 'distance-1d', '수직선 위의 거리', 'Distance on a line', '#s12', '두 숫자 차이의 절댓값. 눈금이 고른 자에서만 성립.'),
        ('Concept', 'ordinal-scale', '순서형 자료', 'Ordinal scale', '#s12', '순서만 의미 있고 간격은 고르지 않은 숫자(층 번호·등급).'),
        ('Concept', 'unit-change', '눈금 바꾸기(선형 변환)', 'Change of scale', '#s13', '새 숫자 = 배율 × 옛 숫자 + 기준점 이동.'),
        ('Concept', 'standardization', '표준화', 'Standardization', '#s13', '평균을 0, 표준편차를 눈금 하나로 바꾼 자.'),
        ('Analogy', 'elevator', '0층 없는 엘리베이터', 'Elevator without floor 0', '#s12', '눈금 하나가 빠진 자의 예.'),
        ('Simulation', 'ruler-translator', '자 통역사 게임', 'Ruler translator game', '#app', '같은 자리를 다른 자의 숫자로 옮기는 네 판.'),
        ('Limitation', 'interval-ratio', '0이 임의인 자에서는 배수 비교 불가', 'No ratios on interval scales', '#s13', '섭씨 20도는 10도의 두 배 따뜻하지 않다.'),
        ('Question', 'need-two', '넓은 곳은 숫자 하나로 충분한가?', 'Is one number enough on a field?', '#outro', '2장 좌표평면으로 이어지는 질문.')],
 edges=[('origin', 'prerequisiteOf', 'number-line', '#s11'), ('number-line', 'prerequisiteOf', 'distance-1d', '#s12'), ('ordinal-scale', 'contrastsWith', 'distance-1d', '#s12'),
        ('elevator', 'analogyOf', 'ordinal-scale', '#s12'), ('unit-change', 'prerequisiteOf', 'standardization', '#s13'), ('standardization', 'demonstratedBy', 'ruler-translator', '#app'),
        ('unit-change', 'hasLimitation', 'interval-ratio', '#s13'), ('number-line', 'relatedTo', 'need-two', '#outro')])
