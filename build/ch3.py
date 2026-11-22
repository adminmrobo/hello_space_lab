# -*- coding: utf-8 -*-
"""3장 극좌표 — 거리와 방향으로 찍는 점"""
NAV = [('#s31', '3.1 거리와 각도'), ('#s32', '3.2 피자'), ('#s33', '3.3 시계판'), ('#app', '부록 게임'), ('#sum', '정리'), ('#kg', '색인'), ('#export', '꾸러미'), ('04_space.html', '4장 →')]

PANEL31 = '''<div class="panel"><div class="ptitle">실험 ① 같은 점, 두 가지 이름 — 그림을 눌러 점을 옮겨 보세요</div>
<div class="cwrap sq"><canvas id="cv31" aria-label="모눈과 동심원이 함께 그려진 판. 점의 (x, y)와 (거리 r, 각도 θ)"></canvas></div>
<div class="ctrl"><div class="group"><button class="bt" type="button" data-p31="3,4">(3, 4)</button><button class="bt" type="button" data-p31="-4,4">(−4, 4)</button><button class="bt" type="button" data-p31="0,-5">(0, −5)</button><button class="bt" type="button" data-p31="-3,-3">(−3, −3)</button><span class="glabel">또는 그림을 눌러 고르기</span></div></div>
<div class="minis"><div class="mini a"><span>모눈 자 (x, y)</span><b id="m31a">—</b></div><div class="mini g"><span>거리 r</span><b id="m31b">—</b></div><div class="mini m"><span>각도 θ (x축에서 시계 반대 방향)</span><b id="m31c">—</b></div><div class="mini r"><span>되돌려 계산한 (x, y)</span><b id="m31d" style="font-size:16px">—</b></div></div>
<div class="eq" id="eq31"></div><div class="insight" id="i31" aria-live="polite"></div></div>'''

PANEL32 = '''<div class="panel"><div class="ptitle">실험 ② 피자 한 조각 — 같은 각도, 다른 테두리 길이</div>
<div class="twin"><div class="cwrap tall"><canvas id="cv32" aria-label="반지름 10 cm와 15 cm인 피자에서 같은 각도로 자른 조각의 테두리"></canvas></div>
<div><div class="ctrl" style="flex-direction:column;align-items:flex-start"><label class="glabel" for="r32">조각 각도</label><div><input type="range" id="r32" min="15" max="180" step="15" value="45"> <span class="val" id="r32v">45°</span></div></div>
<div class="minis" style="grid-template-columns:1fr 1fr"><div class="mini m"><span>각도 (라디안)</span><b id="m32a">—</b></div><div class="mini a"><span>작은 피자 (r = 10 cm) 테두리</span><b id="m32b">—</b></div><div class="mini g"><span>큰 피자 (r = 15 cm) 테두리</span><b id="m32c">—</b></div><div class="mini r"><span>큰 쪽 ÷ 작은 쪽</span><b id="m32d">—</b></div></div></div></div>
<div class="insight" id="i32" aria-live="polite"></div></div>'''

PANEL33 = '''<div class="panel"><div class="ptitle">실험 ③ 12월과 1월은 가까울까 — 숫자 줄과 시계판</div>
<div class="cwrap tall"><canvas id="cv33" aria-label="위는 1부터 12까지의 숫자 줄, 아래는 열두 달을 30°씩 놓은 시계판. 두 달 사이 거리"></canvas></div>
<div class="ctrl"><div class="group"><label class="glabel" for="r33a">첫째 달</label><input type="range" id="r33a" min="1" max="12" step="1" value="12"><span class="val" id="r33av">12월</span>
<label class="glabel" for="r33b">둘째 달</label><input type="range" id="r33b" min="1" max="12" step="1" value="1"><span class="val" id="r33bv">1월</span></div></div>
<div class="minis"><div class="mini a"><span>숫자 줄 거리</span><b id="m33a">—</b></div><div class="mini m"><span>시계판 각도 차이</span><b id="m33b">—</b></div><div class="mini g"><span>시계판 직선 거리 (반지름 1)</span><b id="m33c">—</b></div><div class="mini r"><span>첫째 달의 (cos, sin)</span><b id="m33d" style="font-size:15px">—</b></div></div>
<div class="insight" id="i33" aria-live="polite"></div></div>'''

APP = '''<div class="gameintro"><b>게임 방법</b> 관제실 레이더에 표적이 모눈 자 (x, y)로 표시됩니다. 그런데 드론에는 <b>거리 r</b>와 <b>각도 θ</b>만 입력할 수 있어요. 두 슬라이더로 맞춘 뒤 <b>확인</b>. 표적에서 0.35 안에 들어가면 명중입니다. 각도는 동쪽(x축 +)에서 시계 반대 방향으로 잽니다.</div>
<div class="panel game"><div class="ptitle">부록 게임 · 레이더 관제실 — (x, y)를 (r, θ)로 통역해 드론 보내기</div>
<div class="cwrap sq"><canvas id="cvA" aria-label="레이더 화면. 표적과 내가 보낸 드론의 자리"></canvas></div>
<div class="ctrl"><div class="group"><label class="glabel" for="rAr">거리 r</label><input type="range" id="rAr" min="0" max="8" step="0.1" value="3"><span class="val" id="rArv">3.0</span>
<label class="glabel" for="rAt">각도 θ</label><input type="range" id="rAt" min="0" max="359" step="1" value="0"><span class="val" id="rAtv">0°</span></div></div>
<div class="minis"><div class="mini a"><span>표적 (x, y)</span><b id="mAa">—</b></div><div class="mini m"><span>드론이 간 곳 (x, y)</span><b id="mAb">—</b></div><div class="mini g"><span>표적까지 남은 거리</span><b id="mAc">—</b></div><div class="mini r"><span>명중 기준</span><b>0.35 안</b></div></div>
<div id="gA"></div></div>'''

JS = r'''
function radar(cv,L){var P=SP.Plane(cv,{xr:[-L,L],yr:[-L,L],xl:'x (동)',yl:'y (북)',lstep:2,grid:true});var g=P.g;
  for(var r=1;r<=L;r++)SP.circ(P,0,0,r,'rgba(15,127,134,'+(r%2?.18:.3)+')',1);
  for(var d=0;d<360;d+=30){var q=SP.fromPolar(L,d);SP.seg(P,[0,0],q,'rgba(15,127,134,.15)',1);var t=SP.fromPolar(L*0.93,d);g.fillStyle=U.cssv('--terrain');g.font='10.5px '+U.cssv('--font');g.textAlign='center';if(d%90)g.fillText(d+'°',P.X(t[0]),P.Y(t[1])+4);}
  return P;}
/* 3.1 같은 점, 두 이름 */
var p31=[3,4];
var v31=V($('#cv31'),function(){var P=radar($('#cv31'),6),pr=SP.toPolar(p31[0],p31[1]);
  SP.seg(P,[p31[0],0],p31,'rgba(22,33,43,.35)',1.4,[4,4]);SP.seg(P,[0,p31[1]],p31,'rgba(22,33,43,.35)',1.4,[4,4]);SP.arr(P,[0,0],p31,U.cssv('--gfp'),2.6);
  var g=P.g;g.strokeStyle=U.cssv('--stain');g.lineWidth=2.2;g.beginPath();g.arc(P.X(0),P.Y(0),26,0,-pr[1]*Math.PI/180,true);g.stroke();
  var lp=SP.fromPolar(1.25,pr[1]/2);U.label(g,P.X(lp[0]),P.Y(lp[1]),'θ',U.cssv('--stain'),'center');SP.dot(P,p31[0],p31[1],U.cssv('--eye'),7,'('+fmt(p31[0],1)+', '+fmt(p31[1],1)+')');});
SP.onPick($('#cv31'),function(px,py){var P=SP.Plane($('#cv31'),{xr:[-6,6],yr:[-6,6]}),q=P.inv(px,py);p31=[Math.round(q[0]*2)/2,Math.round(q[1]*2)/2];up31();});
function up31(){var pr=SP.toPolar(p31[0],p31[1]),bk=SP.fromPolar(pr[0],pr[1]);$('#m31a').textContent='('+fmt(p31[0],1)+', '+fmt(p31[1],1)+')';$('#m31b').textContent=fmt(pr[0],2);$('#m31c').textContent=fmt(pr[1],1)+'°';$('#m31d').textContent='('+fmt(bk[0],2)+', '+fmt(bk[1],2)+')';
  $('#eq31').innerHTML='r = √('+fmt(p31[0],1)+'² + '+fmt(p31[1],1)+'²) = <b>'+fmt(pr[0],2)+'</b> · x = r cos θ = '+fmt(pr[0],2)+' × cos '+fmt(pr[1],1)+'° = '+fmt(bk[0],2)+' · y = r sin θ = '+fmt(bk[1],2);
  U.ins($('#i31'),[['m','같은 점을 모눈 자로는 ('+fmt(p31[0],1)+', '+fmt(p31[1],1)+'), 거리·각도 자로는 ('+fmt(pr[0],2)+', '+fmt(pr[1],1)+'°)로 부릅니다. 점은 한 개, 이름이 두 개예요.'],['g','거리 r은 2장의 피타고라스 그대로. 각도에서 x·y로 돌아올 때는 cos·sin을 씁니다. 원 위의 점을 다룰 때는 이 자가 훨씬 짧게 적혀요.']]);v31.dirty=true;}
$$('[data-p31]').forEach(function(b){b.onclick=function(){p31=b.dataset.p31.split(',').map(Number);up31();};});up31();

/* 3.2 피자 */
var a32=45;
var v32=V($('#cv32'),function(){var R=U.setup($('#cv32')),g=R.g,w=R.w,h=R.h;U.grid24(g,w,h);var cx=w*0.5,cy=h*0.55,s=Math.min(w,h)/34,q=a32*Math.PI/180;
  [[15,'#f5d28a',U.cssv('--gfp')],[10,'#f9e3b4',U.cssv('--amber')]].forEach(function(z){g.fillStyle=z[1];g.beginPath();g.arc(cx,cy,z[0]*s,0,7);g.fill();g.strokeStyle='rgba(163,92,0,.35)';g.lineWidth=1;g.stroke();
    g.strokeStyle=z[2];g.lineWidth=6;g.beginPath();g.arc(cx,cy,z[0]*s,-Math.PI/2,-Math.PI/2+q);g.stroke();});
  g.strokeStyle=U.cssv('--eye');g.lineWidth=2;g.beginPath();g.moveTo(cx,cy);g.lineTo(cx,cy-15*s);g.moveTo(cx,cy);g.lineTo(cx+15*s*Math.sin(q),cy-15*s*Math.cos(q));g.stroke();
  U.label(g,cx+11*s*Math.sin(q/2)+6,cy-11*s*Math.cos(q/2),fmt(SP.arc(10,a32),2)+' cm',U.cssv('--amber'));U.label(g,cx+15.6*s*Math.sin(q/2)+6,cy-15.6*s*Math.cos(q/2),fmt(SP.arc(15,a32),2)+' cm',U.cssv('--gfp'));
  U.label(g,cx+8,cy+14,a32+'°',U.cssv('--eye'));U.stamp(g,w,'설명용 예시');});
function up32(){var rad=a32*Math.PI/180;$('#m32a').textContent=fmt(rad,3);$('#m32b').textContent=fmt(SP.arc(10,a32),2)+' cm';$('#m32c').textContent=fmt(SP.arc(15,a32),2)+' cm';$('#m32d').textContent='1.5배';
  U.ins($('#i32'),[['m','같은 '+a32+'°인데 큰 피자의 테두리가 1.5배 깁니다. 각도는 "얼마나 돌았나"이지 "얼마나 갔나"가 아니기 때문이에요.'],['g','호의 길이 = 반지름 × 각도(라디안). 각도 눈금 한 걸음의 실제 길이는 중심에서 멀수록 길어집니다. 극좌표의 각도 눈금은 고르지 않은 자예요.']]);v32.dirty=true;}
rng('r32',function(v){a32=v;up32();},function(v){return v+'°';});

/* 3.3 달력 시계판 */
var m1=12,m2=1;
var v33=V($('#cv33'),function(){var R=U.setup($('#cv33')),g=R.g,w=R.w,h=R.h;U.grid24(g,w,h);var L=w*0.08,Rr=w*0.92,y=h*0.13,X=function(m){return L+(m-1)/11*(Rr-L);};
  g.strokeStyle=U.cssv('--amber');g.lineWidth=2;g.beginPath();g.moveTo(L,y);g.lineTo(Rr,y);g.stroke();g.font='11.5px '+U.cssv('--font');g.textAlign='center';
  for(var m=1;m<=12;m++){g.fillStyle=(m===m1||m===m2)?U.cssv('--eye'):U.cssv('--muted');g.fillRect(X(m)-.5,y-5,1.2,10);g.fillText(m+'월',X(m),y+20);}
  g.strokeStyle=U.cssv('--eye');g.lineWidth=3;g.beginPath();g.moveTo(X(m1),y-12);g.lineTo(X(m2),y-12);g.stroke();U.label(g,(X(m1)+X(m2))/2,y-24,'숫자 줄 거리 '+Math.abs(m1-m2),U.cssv('--eye'),'center');
  var cx=w*0.5,cy=h*0.62,r=Math.min(w*0.3,h*0.3);g.strokeStyle='rgba(15,127,134,.5)';g.lineWidth=1.5;g.beginPath();g.arc(cx,cy,r,0,7);g.stroke();
  function P(m){var a=(90-SP.monthAngle(m))*Math.PI/180;return [cx+r*Math.cos(a),cy-r*Math.sin(a)];}
  for(m=1;m<=12;m++){var p=P(m);g.beginPath();g.arc(p[0],p[1],(m===m1||m===m2)?7:4,0,7);g.fillStyle=(m===m1||m===m2)?U.cssv('--eye'):U.cssv('--terrain');g.fill();var t=[cx+(p[0]-cx)*1.18,cy+(p[1]-cy)*1.18];g.fillStyle=U.cssv('--muted');g.fillText(m+'월',t[0],t[1]+4);}
  var a=P(m1),b=P(m2);g.strokeStyle=U.cssv('--gfp');g.lineWidth=3;g.beginPath();g.moveTo(a[0],a[1]);g.lineTo(b[0],b[1]);g.stroke();U.label(g,cx,cy,'시계판 거리 '+fmt(SP.monthChord(m1,m2),2),U.cssv('--gfp'),'center');});
function up33(){var d=Math.abs(SP.monthAngle(m1)-SP.monthAngle(m2));if(d>180)d=360-d;var c=SP.monthChord(m1,m2),ang=SP.monthAngle(m1)*Math.PI/180;
  $('#m33a').textContent=Math.abs(m1-m2);$('#m33b').textContent=d+'°';$('#m33c').textContent=fmt(c,2);$('#m33d').textContent='('+fmt(Math.cos(ang),2)+', '+fmt(Math.sin(ang),2)+')';
  U.ins($('#i33'),[['m',m1+'월과 '+m2+'월: 숫자 줄로는 '+Math.abs(m1-m2)+'만큼, 시계판으로는 '+fmt(c,2)+'만큼 떨어져 있습니다. 가장 먼 두 달(마주 보는 달)이 2입니다.'],['g','달은 12월 다음에 다시 1월로 돌아오는 <b>둥근 것</b>입니다. 둥근 것은 각도 자에 놓고 (cos, sin) 두 숫자로 적으면 이웃이 이웃답게 가까워집니다.']]);v33.dirty=true;}
rng('r33a',function(v){m1=v;up33();},function(v){return v+'월';});rng('r33b',function(v){m2=v;up33();},function(v){return v+'월';});

/* 부록 게임: 레이더 관제실 */
var TG=[[3,4],[-4,4],[0,-6],[-5,-1]],gr=3,gt=0,G;
var vA=V($('#cvA'),function(){var i=G?G.cur():0,P=radar($('#cvA'),8),T=TG[i],q=SP.fromPolar(gr,gt);
  SP.dot(P,T[0],T[1],U.cssv('--eye'),8,'표적 ('+T+')');SP.circ(P,T[0],T[1],0.35,U.cssv('--eye'),1.4,[3,3]);
  SP.arr(P,[0,0],q,U.cssv('--info'),2.4);SP.dot(P,q[0],q[1],U.cssv('--info'),6,'드론',10,16);});
function upA(){var q=SP.fromPolar(gr,gt),T=TG[G?G.cur():0];$('#mAa').textContent='('+T+')';$('#mAb').textContent='('+fmt(q[0],2)+', '+fmt(q[1],2)+')';$('#mAc').textContent=fmt(SP.dist(q,T),2);vA.dirty=true;}
G=PG.Rounds({el:'#gA',n:TG.length,title:function(i){return '표적 '+(i+1)+' ('+TG[i]+')';},
  ask:function(i){return '<p>표적 ('+TG[i]+')까지의 거리 r과 각도 θ를 맞춰 드론을 보내세요.'+(i===2?' 각도는 0°~359°로 잽니다.':'')+'</p>';},
  setup:function(i){PG.set('rAr',3);PG.set('rAt',0);upA();},
  judge:function(i){var q=SP.fromPolar(gr,gt),T=TG[i],d=SP.dist(q,T),ans=SP.toPolar(T[0],T[1]);
    return [d<=0.35,d<=0.35?'정답은 r = '+fmt(ans[0],2)+', θ = '+fmt(ans[1],1)+'°. r은 피타고라스, θ는 표적이 어느 사분면에 있는지 먼저 보고 정하면 빨라요.':(Math.abs(gr-ans[0])>0.3?'거리부터 다시: √('+T[0]+'² + '+T[1]+'²)':'거리는 맞아요. 각도를 다시: 동쪽 0°, 북쪽 90°, 서쪽 180°, 남쪽 270°'),'r '+fmt(gr,1)+', θ '+gt+'° → 남은 거리 '+fmt(d,2)];}});
$('#rAr').addEventListener('input',function(){gr=+this.value;$('#rArv').textContent=fmt(gr,1);G&&G.touch();upA();});
$('#rAt').addEventListener('input',function(){gt=+this.value;$('#rAtv').textContent=gt+'°';G&&G.touch();upA();});upA();
'''

DLG = {
 'open': [['doc', 'doc_board', '공항 관제실 화면을 떠올려 보세요. 모눈이 아니라 동그라미가 겹겹이 있죠. 관제사는 비행기를 어떻게 부를까요?'],
          ['sia', 'sia_explain', '"북동쪽으로 5 km!" 이런 식이요?'],
          ['doc', 'doc_front', '맞아요. 중심에서의 <b>거리</b>와 기준 방향에서 돈 <b>각도</b>, 이 두 숫자로도 평면의 자리를 말할 수 있습니다. 이것이 극좌표예요.'],
          ['moa', 'moa_report', '그럼 2장의 (x, y)는 버려요?'],
          ['asst', 'asst_smile', '아니요. 같은 점을 부르는 이름이 하나 더 생기는 거예요. 서로 바꿔 부르는 법도 같이 봐요.']],
 's31_t': [['doc', 'doc_front', '점 (3, 4)를 관제사처럼 거리와 각도로 불러 볼까요?'],
           ['robo', 'robo_calc', '거리는 2장에서 배운 대로 5! 각도는… 주판으로는 안 나오는데요?'],
           ['fly', 'fly_point', '점을 눌러 이리저리 옮기면서 θ가 어떻게 변하는지 봐. 버튼으로 네 방향 점도 찍어 봐.']],
 's32_t': [['doc', 'doc_front', '피자 두 판을 똑같이 45°씩 잘랐습니다. 테두리 빵 길이도 같을까요?'],
           ['x3', 'x3_hint', '큰 피자 테두리요! 무조건 큰 거!'],
           ['fly', 'fly_point', '각도 슬라이더를 움직이면서 두 테두리 숫자의 비율을 봐.']],
 's33_t': [['doc', 'doc_front', '판매 예측 모델에 "월"을 1부터 12까지 숫자로 넣었습니다. 12월과 1월은 얼마나 가까운 달일까요?'],
           ['moa', 'moa_report', '날씨로 보면 바로 붙어 있는 겨울인데요…'],
           ['fly', 'fly_point', '첫째 달 12, 둘째 달 1로 두고 위 숫자 줄과 아래 시계판을 비교해 봐.']],
 'ai33_d': [['robo', 'robo_coin', '12월과 1월은 12 − 1 = 11만큼 떨어져 있습니다! 1년 중 거의 가장 먼 두 달이에요. 계산 끝!']],
 'ai33_e': [['robo', 'robo_sigh', '달은 한 바퀴 도는 숫자였군요. 시계판 거리 0.52, 이웃이 맞네요.']],
 'app': [['x3', 'x3_hint', '드론 날리기다!'],
         ['asst', 'asst_firm', '표적이 어느 쪽에 있는지 먼저 보세요. 동쪽이 0°, 북쪽이 90°예요.'],
         ['robo', 'robo_calc', '거리 r은 피타고라스로 제가 바로 도와드릴게요.']],
 'outro': [['doc', 'doc_magic', '오늘의 세 줄입니다.<br>① 평면의 자리는 (x, y)로도, (거리 r, 각도 θ)로도 부를 수 있다.<br>② 각도 눈금 한 걸음의 실제 길이는 중심에서 멀수록 길다. 호의 길이 = r × 각도.<br>③ 한 바퀴 도는 것(달·요일·시각)은 각도 자에 놓아야 이웃이 이웃답다.'],
           ['sia', 'sia_smile', '드론 각도 맞히기, 처음엔 반대로 돌렸어요.'],
           ['x2', 'x2_hint', '(필기) 극좌표 = 거리 + 각도. 둥근 것은 둥근 자로.'],
           ['doc', 'doc_think', '지금까지는 바닥 위의 자리였습니다. 그런데 이 강의실은 3층에 있죠. 다음 시간, 높이가 생기면 숫자가 몇 개 필요한지 봅시다.']],
}

PAGE = dict(
 key='ch3', out='03_polar.html', logo='3장',
 title='좌표 첫걸음 3장 극좌표 — 거리와 방향으로 찍는 점 | 나는 어디에 있는가?',
 desc='좌표 첫걸음 3장. 관제실처럼 거리와 각도로 자리를 부르는 극좌표. (3, 4) = (5, 53.1°), 같은 각도 다른 피자 테두리, 12월과 1월을 이웃으로 만드는 시계판, 그리고 레이더 드론 게임.',
 nav=NAV,
 cover=dict(cap='좌표 첫걸음 · 3교시', chip='3장 극좌표 — 거리와 방향으로 찍는 점', cast=['fly_point', 'doc_board', 'asst_smile', 'robo_calc', 'sia_explain', 'moa_report', 'x1_hint', 'x2_hint', 'x3_hint'], motif='polar'),
 eyebrow='좌표 첫걸음 · 3장 · 최적화 첫걸음의 자매편 <span class="diff">난이도: 오르막</span>',
 h1='3장 극좌표 — 거리와 방향으로 찍는 점',
 question='"여기서 북동쪽으로 5 km"도 좌표일까?',
 lead='평면의 자리는 가로·세로 두 숫자 말고도 <b>중심에서의 거리</b>와 <b>기준 방향에서 돈 각도</b> 두 숫자로 부를 수 있습니다. 레이더·피자·시계처럼 둥근 것을 다룰 때는 이쪽이 훨씬 편해요. 이 장은 두 이름을 서로 바꾸는 법, 각도 눈금이 고르지 않은 이유, 그리고 AI가 "달"을 숫자로 넣을 때 시계판을 쓰는 이유를 봅니다.',
 start='3.1 → 3.2 → 3.3 순서로 보세요. cos·sin은 "각도를 가로·세로 몫으로 나누는 버튼" 정도로 생각해도 따라올 수 있어요.',
 kpis=[('g', '(5, 53.1°)', '점 (3, 4)의 극좌표 이름'), ('a', '7.85 cm', '반지름 10 cm 피자, 45° 조각의 테두리'), ('m', '11.78 cm', '반지름 15 cm 피자, 같은 45°'), ('r', '0.52', '시계판에서 12월–1월 거리 (숫자 줄로는 11)')],
 plain=[('무엇을', '거리와 각도 두 숫자로 자리를 부르는 극좌표를, 레이더·피자·달력으로 봅니다.'),
        ('왜 중요한가', '레이더, 로봇 팔, 원형 데이터(시각·요일·달)는 거리·각도로 적어야 식이 짧고 이웃 관계가 맞습니다.'),
        ('업무에서는', '월·요일·시각을 1, 2, 3… 숫자 그대로 모델에 넣으면 12월과 1월이 멀어지는 실수를 알아챌 수 있습니다.')],
 abbr=[('r', '거리', '중심(원점)에서 점까지 직선 거리.'), ('θ (세타)', '각도', '동쪽(x축 +)에서 시계 반대 방향으로 돈 각도.'), ('rad (라디안)', '호도법 각도', '반지름 1인 원에서 호의 길이로 잰 각도. 180° = π rad.'),
       ('cos · sin', '코사인 · 사인', '각도 θ인 반지름 1 화살표의 가로 몫과 세로 몫.')],
 hex='3', open_title='거리와 각도로 자리 말하기',
 bigpicture='<div class="chain" aria-label="이 시리즈 지도"><span>1장 수직선</span><i>→</i><span>2장 좌표평면</span><i>→</i><span><b>3장 극좌표</b></span><i>→</i><span>4장 공간좌표</span><i>→</i><span>5장 지구와 지도</span><i>→</i><span>6장 데이터의 좌표</span></div><div class="review30"><b>30초 복습</b> 2장: 평면의 자리는 순서쌍 (x, y), 거리는 √(Δx² + Δy²). 오늘은 같은 평면을 동그라미 자로 다시 잽니다.</div>',
 steps=[
  dict(id='s31', num='3.1', title='같은 점, 두 가지 이름 — (x, y)와 (r, θ)', tags=['방법: 극좌표 변환', '일상: 관제실 레이더', '바탕: 벡터 분석 랩 0편 네 개의 자'],
       why=dict(problem='레이더·로봇 팔처럼 한 중심에서 돌아가며 보는 장치는 "얼마나 멀리, 어느 쪽"으로 자리를 압니다.', limit='모눈 자 (x, y)로 적으면 "북동쪽으로 5"를 바로 알아보기 어렵습니다.',
                solve='중심에서의 거리 r과 기준 방향에서 돈 각도 θ, 두 숫자로 자리를 적습니다. 필요하면 cos·sin으로 (x, y)로 바꿉니다.', easy='"시계 2시 방향으로 다섯 걸음"이라고 말하는 것.'),
       math=dict(who='moa', q='(3, 4)가 왜 53.1°예요? 그 각도는 어떻게 알아요?', words='점까지의 화살표, 가로 3, 세로 4로 직각삼각형을 만들면 r은 빗변 5입니다. 각도는 "세로 몫 ÷ 가로 몫"이 4 ÷ 3이 되는 각도를 찾으면 돼요. 계산기의 역탄젠트가 53.1°를 알려 줍니다.',
                 school='삼각함수 sin·cos·tan, 피타고라스 정리', rows=[('x = r cos θ', '엑스는 알 코사인 세타', '거리·각도 → 가로'), ('y = r sin θ', '와이는 알 사인 세타', '거리·각도 → 세로'), ('r = √(x² + y²)', '알은 루트 엑스 제곱 더하기 와이 제곱', '가로·세로 → 거리')],
                 tries=['r = √(3² + 4²) = 5', 'cos 53.1° ≈ 0.6 → x = 5 × 0.6 = 3', 'sin 53.1° ≈ 0.8 → y = 5 × 0.8 = 4. 처음 점으로 돌아왔어요'], comment='cos가 가로 몫, sin이 세로 몫. 이름만 어렵지 하는 일은 나누기예요!'),
       daily='등산 앱이 "정상까지 북동쪽 1.2 km"라고 알려 주는 것도 극좌표 말투입니다.',
       field='로봇 팔 관절은 각도로 움직이고, 라이다(LiDAR) 센서는 "각도마다 거리"를 잽니다. 이런 데이터를 지도(x, y)로 옮길 때 이 변환을 씁니다.',
       panel=PANEL31,
       doc='자리 하나에 이름이 여럿일 수 있습니다. 문제에 맞는 이름을 고르고, 필요할 때 바꿔 부르면 됩니다. 4장에서는 이 생각이 3차원의 원통 자·지구본 자로 커집니다.',
       limit='원점(r = 0)에서는 각도를 정할 수 없습니다. 제자리에 서 있으면 "어느 쪽"이 없는 것과 같아요. 나침반의 방위각은 북쪽 0°, 시계 방향이라 이 페이지의 각도와 기준이 다릅니다.'),
  dict(id='s32', num='3.2', title='같은 각도, 다른 길이 — 피자 테두리', tags=['방법: 호의 길이 = r × 각도', '일상: 피자 조각', '바탕: 벡터 분석 랩 1부 방 1'],
       why=dict(problem='각도 눈금 1만큼 움직이면 실제로 얼마나 가는지 알아야 거리·넓이를 잴 수 있습니다.', limit='3.1의 각도 θ는 "얼마나 돌았나"만 말하고 "얼마나 갔나"는 말하지 않습니다.',
                solve='호의 길이 = 반지름 × 각도(라디안). 중심에서 멀수록 같은 각도에 더 많이 갑니다.', easy='회전목마 바깥 말은 같은 각도를 돌아도 안쪽 말보다 더 멀리 달린다.'),
       math=dict(who='sia', q='45°를 돌았으면 45만큼 간 거 아니에요?', words='각도는 도는 양이에요. 실제 길이는 반지름이 곱해져야 나옵니다. 그래서 라디안이라는 각도를 쓰면 "반지름 × 각도"가 곧 호의 길이가 돼요.',
                 school='부채꼴의 호의 길이, 호도법(라디안)', rows=[('l = r θ', '엘은 알 세타', '호의 길이 (θ는 라디안)'), ('45° = π/4 rad', '사십오 도는 사분의 파이 라디안', '약 0.785')],
                 tries=['45° = 0.785 rad', '작은 피자: 10 × 0.785 = 7.85 cm', '큰 피자: 15 × 0.785 = 11.78 cm — 1.5배'], comment='각도 눈금은 중심에서 멀수록 길어지는 자였어요. 1장의 "고르지 않은 눈금" 기억나세요?'),
       daily='자전거 바퀴가 클수록 한 바퀴에 더 멀리 갑니다. 같은 각도를 돌아도 반지름이 다르기 때문이에요.',
       field='단어나 사진을 점으로 놓는 임베딩에서도 "방향(각도)"과 "길이"를 나눠 읽습니다. 방향이 비슷하면 뜻이 비슷하다고 보는 코사인 유사도가 대표적이에요(<a href="https://adminmrobo.github.io/vector_analysis_lab/03_ai_ml.html">벡터 분석 랩 3부</a>).',
       panel=PANEL32,
       doc='각도 자를 쓸 때는 "이 각도 한 걸음이 실제로 몇 cm인가"를 함께 들고 다니세요. 그 배율이 반지름입니다. 5장에서는 이것이 "위도마다 다른 경도 1도의 길이"가 됩니다.',
       limit='피자를 완벽한 원으로 봤어요.'),
  dict(id='s33', num='3.3', title='12월과 1월은 이웃이다 — 달력 시계판', tags=['방법: 각도로 바꿔 (cos, sin)으로 적기', '일상: 달력', 'AI: 순환 특성'],
       why=dict(problem='달·요일·시각은 끝에서 처음으로 다시 돌아옵니다.', limit='1~12 숫자 줄에 놓으면 12월과 1월이 가장 멀리 떨어집니다.',
                solve='12달을 원 위에 30°씩 놓고, 각 달을 (cos, sin) 두 숫자로 적습니다. 그러면 12월과 1월이 이웃이 됩니다.', easy='달력을 일자 막대가 아니라 둥근 시계로 그리기.'),
       math=dict(who='moa', q='시계판에서 12월과 1월 거리 0.52는 어떻게 나와요?', words='두 달은 30° 떨어져 있습니다. 반지름 1인 원에서 30° 떨어진 두 점 사이 직선 거리를 재면 돼요. 이등변삼각형을 반으로 나누면 sin으로 구할 수 있습니다.',
                 school='삼각함수, 원 위의 두 점 사이 거리', rows=[('각도 = (월 − 1) × 30°', '월마다 삼십 도씩', '달을 원 위에 놓기'), ('(cos θ, sin θ)', '코사인 세타, 사인 세타', '그 달의 두 숫자'), ('2 sin(Δθ ÷ 2)', '이 사인 델타 세타 나누기 이', '원 위 두 점 사이 거리 (반지름 1)')],
                 tries=['12월 330°, 1월 0° → 차이 30°', '2 × sin 15° = 2 × 0.259 = 0.52', '12월과 6월은 180° 차이 → 2 × sin 90° = 2 (가장 멂)'], comment='숫자 하나(월)를 숫자 두 개(cos, sin)로 늘렸더니 이웃이 돌아왔어요!'),
       daily='12월 31일 밤 11시와 1월 1일 0시는 한 시간 차이인데, 날짜 숫자로는 1년 차이처럼 보입니다.',
       field='판매·전력 수요 예측 모델은 "월"을 sin·cos 두 열로 바꿔 넣습니다. 요일(7개, 51.4°씩)과 시각(24개, 15°씩)도 같아요. 이것을 순환 특성(cyclical feature)이라고 부릅니다.',
       panel=PANEL33,
       ai=dict(id='ai33', title='조교 주판봇의 1초 답, 믿어도 될까?', checks=['달은 수직선처럼 한쪽 끝이 있는 숫자인가, 한 바퀴 도는 숫자인가?', '"12월과 1월이 가장 먼 두 달"이라는 결론이 날씨·매출 감각과 맞는가?'],
               verdict='달은 12 다음에 1로 돌아오는 둥근 숫자입니다. 시계판에서 12월–1월 거리는 <b>0.52</b>로 바로 이웃이고, 가장 먼 짝은 마주 보는 12월–6월(거리 2)입니다. 계산은 맞았지만 <b>자를 잘못 골랐습니다.</b>'),
       doc='모델에 숫자를 넣기 전에 "이 숫자는 끝이 있는가, 도는가?"를 물어보세요. 도는 숫자는 각도 자에 놓아야 AI가 이웃을 제대로 봅니다.',
       code=[('np.sin(2*np.pi*(month-1)/12)', '달 → sin 열'), ('np.cos(2*np.pi*(month-1)/12)', '달 → cos 열')],
       limit='시계판은 "얼마나 가까운가"만 바로잡습니다. 계절마다 매출이 다른 이유까지 설명하지는 않아요.'),
 ],
 app_title='레이더 관제실 — (x, y)를 (r, θ)로 통역하기', app_lead='네 사분면에 하나씩 표적이 나옵니다. 각도는 표적이 어느 쪽에 있는지부터 보면 금방 맞힐 수 있어요.', app_html=APP,
 sum_title='거리와 각도로 자리를 말하는 법',
 summary=[('극좌표란?', '중심에서의 거리 r과 기준 방향에서 돈 각도 θ로 자리를 적는 자.', '3.1'), ('서로 바꾸려면?', 'x = r cos θ, y = r sin θ, r = √(x² + y²).', '3.1'),
          ('각도 한 걸음의 길이는?', '반지름 × 각도(라디안). 멀수록 길다.', '3.2'), ('도는 숫자는?', '원 위에 놓고 (cos, sin) 두 숫자로 적는다.', '3.3')],
 cards=[('극좌표', '(거리, 각도)로 적는 평면의 좌표.'), ('라디안', '호의 길이로 잰 각도. 180° = π.'), ('호의 길이', '반지름 × 각도(라디안).'), ('cos · sin', '각도의 가로 몫 · 세로 몫.'), ('순환 특성', '달·요일·시각을 sin·cos 두 열로 바꾼 것.'), ('사분면', '두 축이 나눈 평면의 네 구역.')],
 limits=['피자는 완전한 원, 달은 모두 같은 길이(30°)로 단순하게 봤습니다. 실제 달은 28~31일입니다.', '레이더 게임의 표적은 설명용 자리입니다.'],
 next=[('04_space.html', '4장 공간좌표 →', '높이가 생기면 세 숫자, 같은 점 세 가지 자, 드론 배송'), ('02_plane.html', '← 2장 좌표평면', ''), ('index.html', '목차', '')],
 refs=[('안상선, 「벡터 분석 랩」 0편 방 A 네 개의 자·1부 방 1 피자·방 2 12월과 1월 (vector_analysis_lab)', '3.1 원통 자의 각도 한 걸음, 3.2 45° 피자 7.85·11.78 cm, 3.3 숫자 줄 11 / 시계판 0.52'),
       ('안상선, 「벡터 분석 랩」 3부 달력 시계 특성·임베딩 (vector_analysis_lab)', '3.3 순환 특성, 3.2 방향과 길이를 나눠 읽기'),
       ('안상선, 「자와 각도기의 방」 0편 각도기 sin·cos (euclidean_space_lab)', '3.1 cos·sin을 가로·세로 몫으로 읽기')],
 examples=['피자 반지름 10 cm·15 cm', '레이더 표적 (3, 4)·(−4, 4)·(0, −6)·(−5, −1)', '12달을 30°씩 같은 간격으로 놓은 시계판'],
 dlg=DLG, js=JS,
 gloss={'극좌표': ['극좌표', '좌표', '거리 r과 각도 θ로 평면의 자리를 적는 방법.'], '라디안': ['라디안 (rad)', '수학', '반지름 1인 원에서 호의 길이로 잰 각도. 180° = π ≈ 3.14 rad.'],
        '코사인 유사도': ['코사인 유사도', 'AI', '두 화살표가 이루는 각도로 닮음을 재는 방법. 길이는 무시하고 방향만 본다.'], '순환 특성': ['순환 특성', 'AI', '달·요일·시각처럼 도는 값을 sin·cos 두 열로 바꾼 입력.'],
        '라이다': ['라이다 (LiDAR)', 'AI', '빛을 쏘아 각도마다 거리를 재는 센서. 자율주행차가 쓴다.'], '사분면': ['사분면', '수학', 'x축·y축이 나눈 평면의 네 구역.'], '임베딩': ['임베딩', 'AI', '단어·사진을 숫자 여러 개(점)로 바꾼 것.']},
 gloss_core=['극좌표', '라디안', '코사인 유사도', '순환 특성', '임베딩'],
 quiz={'s31': [{'q': '극좌표 (2, 90°)인 점의 (x, y)는?', 'o': ['(0, 2)', '(2, 0)', '(2, 90)'], 'a': 0, 'why': '90°는 북쪽(y축 +). cos 90° = 0, sin 90° = 1 → (0, 2).', 'hint': '동쪽 0°, 북쪽 90°.'}],
       's32': [{'q': '반지름 20 cm 피자를 90°로 자르면 테두리 길이는?', 'o': ['약 31.4 cm', '90 cm', '20 cm'], 'a': 0, 'why': '90° = π/2 ≈ 1.571 rad, 20 × 1.571 ≈ 31.4 cm.', 'hint': '반지름 × 라디안.'}],
       's33': [{'q': '시계판에서 3월과 가장 먼 달은?', 'o': ['9월', '12월', '4월'], 'a': 0, 'why': '마주 보는 달(180° 차이)이 가장 멉니다. 3 + 6 = 9월.', 'hint': '원에서 정반대 자리.'}]},
)

KG = dict(
 nodes=[('Concept', 'polar-coordinates', '극좌표', 'Polar coordinates', '#s31', '거리 r과 각도 θ로 평면의 자리를 적는 자.'),
        ('Concept', 'trig-conversion', 'cos·sin 변환', 'Polar–Cartesian conversion', '#s31', 'x = r cos θ, y = r sin θ.'),
        ('Concept', 'radian', '라디안', 'Radian', '#s32', '호의 길이로 잰 각도.'),
        ('Concept', 'arc-length', '호의 길이', 'Arc length', '#s32', '반지름 × 각도(라디안). 각도 눈금 한 걸음의 실제 길이.'),
        ('Concept', 'cyclical-feature', '순환 특성', 'Cyclical feature encoding', '#s33', '달·요일·시각을 sin·cos 두 열로 바꾼 입력.'),
        ('Analogy', 'pizza', '피자 테두리', 'Pizza crust', '#s32', '같은 각도라도 반지름이 크면 호가 길다.'),
        ('Analogy', 'month-clock', '달력 시계판', 'Month clock', '#s33', '12월과 1월이 이웃이 되는 원 위의 달.'),
        ('Simulation', 'radar-game', '레이더 관제실 게임', 'Radar control game', '#app', '(x, y) 표적을 (r, θ)로 맞히는 네 판.'),
        ('Limitation', 'origin-angle', '원점에서는 각도가 없다', 'Undefined angle at origin', '#s31', 'r = 0이면 θ를 정할 수 없다.'),
        ('Question', 'height', '높이가 생기면 숫자는 몇 개?', 'What about height?', '#outro', '4장 공간좌표로 이어지는 질문.')],
 edges=[('trig-conversion', 'partOf', 'polar-coordinates', '#s31'), ('polar-coordinates', 'prerequisiteOf', 'arc-length', '#s32'), ('radian', 'prerequisiteOf', 'arc-length', '#s32'),
        ('pizza', 'analogyOf', 'arc-length', '#s32'), ('month-clock', 'analogyOf', 'cyclical-feature', '#s33'), ('polar-coordinates', 'prerequisiteOf', 'cyclical-feature', '#s33'),
        ('polar-coordinates', 'demonstratedBy', 'radar-game', '#app'), ('polar-coordinates', 'hasLimitation', 'origin-angle', '#s31'), ('polar-coordinates', 'relatedTo', 'height', '#outro')])
