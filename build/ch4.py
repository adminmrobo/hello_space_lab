# -*- coding: utf-8 -*-
"""4장 공간좌표 — 높이가 생기면 세 숫자"""
NAV = [('#s41', '4.1 세 숫자'), ('#s42', '4.2 공간 거리'), ('#s43', '4.3 세 가지 자'), ('#app', '부록 게임'), ('#sum', '정리'), ('#kg', '색인'), ('#export', '꾸러미'), ('05_earth_map.html', '5장 →')]

PANEL41 = '''<div class="panel"><div class="ptitle">실험 ① 바닥 그림자와 높이 — 세 슬라이더로 점을 옮겨 보세요</div>
<div class="cwrap t3"><canvas id="cv41" aria-label="x·y·z 세 축이 있는 공간, 점과 바닥에 떨어진 그림자"></canvas><span class="hint">끌어서 돌리기</span></div>
<div class="ctrl"><div class="group"><label class="glabel" for="r41x">x (동쪽)</label><input type="range" id="r41x" min="-3" max="3" step="1" value="2"><span class="val" id="r41xv">2</span>
<label class="glabel" for="r41y">y (북쪽)</label><input type="range" id="r41y" min="-3" max="3" step="1" value="1"><span class="val" id="r41yv">1</span>
<label class="glabel" for="r41z">z (높이)</label><input type="range" id="r41z" min="-3" max="3" step="1" value="3"><span class="val" id="r41zv">3</span></div></div>
<div class="minis"><div class="mini m"><span>공간의 자리 (x, y, z)</span><b id="m41a">—</b></div><div class="mini a"><span>바닥 그림자 (x, y)</span><b id="m41b">—</b></div><div class="mini g"><span>높이 z</span><b id="m41c">—</b></div><div class="mini r"><span>같은 그림자의 점 수</span><b>끝없이</b></div></div>
<div class="insight" id="i41" aria-live="polite"></div></div>'''

PANEL42 = '''<div class="panel"><div class="ptitle">실험 ② 원점에서 점 B까지 — 피타고라스를 두 번</div>
<div class="cwrap t3"><canvas id="cv42" aria-label="원점에서 점 B까지 바닥 대각선과 높이, 그리고 공간 대각선"></canvas><span class="hint">끌어서 돌리기</span></div>
<div class="ctrl"><div class="group"><label class="glabel" for="r42x">B의 x</label><input type="range" id="r42x" min="0" max="6" step="1" value="2"><span class="val" id="r42xv">2</span>
<label class="glabel" for="r42y">B의 y</label><input type="range" id="r42y" min="0" max="6" step="1" value="3"><span class="val" id="r42yv">3</span>
<label class="glabel" for="r42z">B의 z</label><input type="range" id="r42z" min="0" max="6" step="1" value="6"><span class="val" id="r42zv">6</span></div></div>
<div class="minis"><div class="mini a"><span>① 바닥 대각선 √(x² + y²)</span><b id="m42a">—</b></div><div class="mini m"><span>② 높이 z</span><b id="m42b">—</b></div><div class="mini g"><span>③ 공간 거리</span><b id="m42c">—</b></div><div class="mini r"><span>세 숫자를 그냥 더하면</span><b id="m42d">—</b></div></div>
<div class="eq" id="eq42"></div><div class="insight" id="i42" aria-live="polite"></div></div>'''

PANEL43 = '''<div class="panel"><div class="ptitle">실험 ③ 같은 점, 세 가지 자로 읽기</div>
<div class="cwrap t3"><canvas id="cv43" aria-label="한 점을 모눈 자·원통 자·지구본 자로 읽을 때 쓰는 선과 각도"></canvas><span class="hint">끌어서 돌리기</span></div>
<div class="ctrl"><div class="group" role="group" aria-label="자 고르기"><span class="glabel">그림에 표시할 자</span><button class="bt" type="button" data-k43="box" aria-pressed="true">모눈 자 (x, y, z)</button><button class="bt" type="button" data-k43="cyl" aria-pressed="false">원통 자 (ρ, φ, z)</button><button class="bt" type="button" data-k43="sph" aria-pressed="false">지구본 자 (r, θ, φ)</button></div>
<div class="group"><label class="glabel" for="r43x">x</label><input type="range" id="r43x" min="-2" max="2" step="0.1" value="1"><span class="val" id="r43xv">1.0</span>
<label class="glabel" for="r43y">y</label><input type="range" id="r43y" min="-2" max="2" step="0.1" value="1"><span class="val" id="r43yv">1.0</span>
<label class="glabel" for="r43z">z</label><input type="range" id="r43z" min="-2" max="2" step="0.01" value="1.41"><span class="val" id="r43zv">1.41</span></div></div>
<div class="minis" style="grid-template-columns:repeat(3,1fr)"><div class="mini a"><span>모눈 자 (x, y, z)</span><b id="m43a" style="font-size:16px">—</b></div><div class="mini m"><span>원통 자 (ρ, φ, z)</span><b id="m43b" style="font-size:16px">—</b></div><div class="mini g"><span>지구본 자 (r, θ, φ)</span><b id="m43c" style="font-size:16px">—</b></div></div>
<div class="insight" id="i43" aria-live="polite"></div></div>'''

APP = '''<div class="gameintro"><b>게임 방법</b> 물류창고 선반의 주소가 판마다 다른 자로 적혀 옵니다. 그런데 배송 드론에는 x·y·z 세 슬라이더만 있어요. 주소를 모눈 자로 바꿔 드론을 보내고 <b>확인</b>을 누르세요. 선반은 모두 정수 자리에 있습니다.</div>
<div class="panel game"><div class="ptitle">부록 게임 · 드론 배송 — 다른 자로 적힌 선반 주소 찾기</div>
<div class="cwrap t3"><canvas id="cvA" aria-label="3차원 창고 공간과 배송 드론의 위치"></canvas><span class="hint">끌어서 돌리기</span></div>
<div class="ctrl"><div class="group"><label class="glabel" for="rAx">x</label><input type="range" id="rAx" min="-5" max="5" step="1" value="0"><span class="val" id="rAxv">0</span>
<label class="glabel" for="rAy">y</label><input type="range" id="rAy" min="-5" max="5" step="1" value="0"><span class="val" id="rAyv">0</span>
<label class="glabel" for="rAz">z</label><input type="range" id="rAz" min="-5" max="5" step="1" value="0"><span class="val" id="rAzv">0</span></div></div>
<div class="minis"><div class="mini a"><span>드론 자리 (x, y, z)</span><b id="mAa">—</b></div><div class="mini m"><span>그 자리의 원통 자</span><b id="mAb" style="font-size:15px">—</b></div><div class="mini g"><span>그 자리의 지구본 자</span><b id="mAc" style="font-size:15px">—</b></div><div class="mini r"><span>출발 창구(원점)까지</span><b id="mAd">—</b></div></div>
<div id="gA"></div></div>'''

JS = r'''
function S3(id,L,extra){var o={L:L,axes:['x (동)','y (북)','z (높이)'],stamp:extra&&extra.stamp};var S=new U.Space3D($('#'+id),o);return S;}
function nm(v,d){return fmt(v,d==null?2:d);}
/* 4.1 */
var p41=[2,1,3],S41=S3('cv41',3);
S41.ov.push(function(g,S){var p=p41;S.line3(g,[[p[0],0,-S.L],[p[0],p[1],-S.L],[0,p[1],-S.L]],'rgba(22,33,43,.3)',1.2,[4,4]);S.drop(g,p[0],p[1],p[2]);
  var q=S.dot3(g,p[0],p[1],-S.L,'rgba(22,33,43,.45)',5,false);U.label(g,q[0]+8,q[1]+10,'그림자 ('+p[0]+', '+p[1]+')',U.cssv('--muted'));
  var r=S.dot3(g,p[0],p[1],p[2],U.cssv('--eye'),7);U.label(g,r[0]+10,r[1]-10,'('+p.join(', ')+')',U.cssv('--eye'));});
function up41(){$('#m41a').textContent='('+p41.join(', ')+')';$('#m41b').textContent='('+p41[0]+', '+p41[1]+')';$('#m41c').textContent=p41[2];
  U.ins($('#i41'),[['m','바닥 위의 자리 ('+p41[0]+', '+p41[1]+')는 2장의 좌표평면 그대로입니다. 여기에 높이 '+p41[2]+'을 더해 세 숫자가 되었어요.'],['g','z 슬라이더만 움직여 보세요. 그림자는 그대로인데 점은 오르내립니다. 그림자 하나 위에 점이 끝없이 많으니, 높이 숫자가 꼭 필요합니다.']]);S41.dirty=true;}
[0,1,2].forEach(function(k){rng('r41'+'xyz'[k],function(v){p41[k]=v;up41();});});
/* 4.2 */
var b42=[2,3,6],S42=S3('cv42',6);
S42.ov.push(function(g,S){var b=b42;S.line3(g,[[0,0,0],[b[0],b[1],0]],U.cssv('--amber'),3,[6,4]);S.line3(g,[[b[0],b[1],0],b],U.cssv('--stain'),3,[6,4]);S.line3(g,[[0,0,0],b],U.cssv('--gfp'),3.4);
  S.dot3(g,0,0,0,U.cssv('--text'),5);var q=S.dot3(g,b[0],b[1],b[2],U.cssv('--eye'),7);U.label(g,q[0]+10,q[1]-10,'B ('+b.join(', ')+')',U.cssv('--eye'));
  var m=S.P(b[0]/2,b[1]/2,0);U.label(g,m[0],m[1]+14,'①',U.cssv('--amber'),'center');var n=S.P(b[0],b[1],b[2]/2);U.label(g,n[0]+12,n[1],'②',U.cssv('--stain'));var k=S.P(b[0]/2,b[1]/2,b[2]/2);U.label(g,k[0]-12,k[1],'③',U.cssv('--gfp'),'right');});
function up42(){var b=b42,f=Math.hypot(b[0],b[1]),d=SP.dist([0,0,0],b);$('#m42a').textContent=nm(f);$('#m42b').textContent=b[2];$('#m42c').textContent=nm(d);$('#m42d').textContent=b[0]+b[1]+b[2];
  $('#eq42').innerHTML='① √('+b[0]+'² + '+b[1]+'²) = '+nm(f)+' → ③ √('+nm(f)+'² + '+b[2]+'²) = √('+b[0]+'² + '+b[1]+'² + '+b[2]+'²) = √'+(b[0]*b[0]+b[1]*b[1]+b[2]*b[2])+' = <b>'+nm(d)+'</b>';
  U.ins($('#i42'),[['m','바닥에서 한 번(①), 그 대각선과 높이로 한 번 더(③) 피타고라스를 쓰면 공간 거리가 나옵니다. 결국 세 차이를 제곱해 더하고 루트를 씌운 것과 같아요.'],['a','세 숫자를 그냥 더하면 '+(b[0]+b[1]+b[2])+'. 상자 모서리를 따라 꺾어 가는 길이지 곧장 가는 거리('+nm(d)+')가 아닙니다.']]);S42.dirty=true;}
[0,1,2].forEach(function(k){rng('r42'+'xyz'[k],function(v){b42[k]=v;up42();});});
/* 4.3 */
var p43=[1,1,1.41],k43='box',S43=S3('cv43',2);
S43.ov.push(function(g,S){var p=p43,cy=SP.cyl(p[0],p[1],p[2]),sp=SP.sph(p[0],p[1],p[2]),i;
  if(k43==='box'){S.line3(g,[[0,0,0],[p[0],0,0],[p[0],p[1],0],p],U.cssv('--amber'),2.6);}
  if(k43==='cyl'){S.line3(g,[[0,0,0],[p[0],p[1],0]],U.cssv('--amber'),2.8);S.line3(g,[[p[0],p[1],0],p],U.cssv('--stain'),2.6,[5,4]);var ar=[];for(i=0;i<=20;i++){var a=cy[1]*i/20*Math.PI/180;ar.push([0.6*Math.cos(a),0.6*Math.sin(a),0]);}S.line3(g,ar,U.cssv('--info'),2.2);
    var m=S.P(p[0]/2,p[1]/2,0);U.label(g,m[0],m[1]+14,'ρ = '+nm(cy[0]),U.cssv('--amber'),'center');var t=S.P(0.75,0.25,0);U.label(g,t[0]+6,t[1],'φ',U.cssv('--info'));}
  if(k43==='sph'){S.line3(g,[[0,0,0],p],U.cssv('--gfp'),3);var ar2=[];for(i=0;i<=20;i++){var th=sp[1]*i/20*Math.PI/180,rr=0.7;ar2.push([rr*Math.sin(th)*Math.cos(sp[2]*Math.PI/180),rr*Math.sin(th)*Math.sin(sp[2]*Math.PI/180),rr*Math.cos(th)]);}S.line3(g,ar2,U.cssv('--stain'),2.2);
    S.line3(g,[[0,0,0],[p[0],p[1],0]],'rgba(22,33,43,.35)',1.4,[4,4]);var ar3=[];for(i=0;i<=20;i++){var a3=sp[2]*i/20*Math.PI/180;ar3.push([0.5*Math.cos(a3),0.5*Math.sin(a3),0]);}S.line3(g,ar3,U.cssv('--info'),2);
    var m2=S.P(p[0]/2,p[1]/2,p[2]/2);U.label(g,m2[0]-8,m2[1],'r = '+nm(sp[0]),U.cssv('--gfp'),'right');var t2=ar2[10];t2=S.P(t2[0],t2[1],t2[2]);U.label(g,t2[0]+6,t2[1]-6,'θ',U.cssv('--stain'));var t3=S.P(0.6,0.2,0);U.label(g,t3[0]+6,t3[1]+8,'φ',U.cssv('--info'));}
  S.drop(g,p[0],p[1],p[2]);S.dot3(g,p[0],p[1],p[2],U.cssv('--eye'),7);});
function up43(){var p=p43,cy=SP.cyl(p[0],p[1],p[2]),sp=SP.sph(p[0],p[1],p[2]);$('#m43a').textContent='('+p.map(function(v){return nm(v);}).join(', ')+')';
  $('#m43b').textContent='('+nm(cy[0])+', '+nm(cy[1],1)+'°, '+nm(cy[2])+')';$('#m43c').textContent='('+nm(sp[0])+', '+nm(sp[1],1)+'°, '+nm(sp[2],1)+'°)';
  U.ins($('#i43'),[['m','같은 점 하나를 세 가지 자로 읽었습니다. <b>모눈 자</b>는 동·북·위로 얼마, <b>원통 자</b>는 바닥에서 "중심축까지 거리 ρ와 돈 각도 φ" + 높이, <b>지구본 자</b>는 "중심까지 거리 r, 꼭대기에서 내려온 각도 θ, 바닥에서 돈 각도 φ"입니다.'],
    ['g','원통 자는 3장의 극좌표에 높이를 붙인 것, 지구본 자는 5장 위도·경도의 뿌리입니다. 회전하는 기계·원기둥 탱크는 원통 자, 지구·소리·빛처럼 한 점에서 퍼지는 것은 지구본 자가 편해요.']]);S43.dirty=true;}
[0,1,2].forEach(function(k){rng('r43'+'xyz'[k],function(v){p43[k]=v;up43();},function(v){return fmt(v,k===2?2:1);});});
p43[2]=Math.SQRT2;up43(); /* 1.41은 √2를 반올림해 보인 값 */
$$('[data-k43]').forEach(function(b){b.onclick=function(){k43=b.dataset.k43;$$('[data-k43]').forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});up43();};});
/* 부록 게임: 드론 배송 */
var GD=[{t:'모눈 자 주소',a:'선반 주소: <b>모눈 자 (4, 2, 3)</b> — 그대로 보내면 됩니다. 몸풀기!',ans:[4,2,3]},
 {t:'원통 자 주소',a:'선반 주소: <b>원통 자 (ρ = 5, φ = 36.87°, z = 2)</b>. 바닥에서 중심축까지 5, 동쪽에서 36.87° 돌고, 높이 2. 힌트: cos 36.87° = 0.8, sin 36.87° = 0.6',ans:[4,3,2]},
 {t:'지구본 자 주소',a:'선반 주소: <b>지구본 자 (r = 3, θ = 48.19°, φ = 63.43°)</b>. 힌트: cos 48.19° = 2/3, sin 48.19° = √5/3, cos 63.43° = 1/√5, sin 63.43° = 2/√5',ans:[1,2,2]},
 {t:'거리로 적힌 주소',a:'선반 주소: <b>바닥(z = 0) 위, x = 3, 출발 창구(원점)에서 곧장 잰 거리 5, 북쪽(y +)</b>.',ans:[3,4,0]}];
var dA=[0,0,0],G,SA=S3('cvA',5);
SA.ov.push(function(g,S){var i=G?G.cur():0;S.drop(g,dA[0],dA[1],dA[2]);var q=S.dot3(g,dA[0],dA[1],dA[2],U.cssv('--info'),8);U.label(g,q[0]+10,q[1]-10,'드론 ('+dA.join(', ')+')',U.cssv('--info'));
  if(G&&G.hit){var t=G.hit;var r=S.dot3(g,t[0],t[1],t[2],U.cssv('--gfp'),10);U.label(g,r[0]+10,r[1]+14,'선반 도착!',U.cssv('--gfp'));}});
function upA(){var cy=SP.cyl(dA[0],dA[1],dA[2]),sp=SP.sph(dA[0],dA[1],dA[2]);$('#mAa').textContent='('+dA.join(', ')+')';$('#mAb').textContent='('+nm(cy[0])+', '+nm(cy[1],1)+'°, '+dA[2]+')';$('#mAc').textContent='('+nm(sp[0])+', '+nm(sp[1],1)+'°, '+nm(sp[2],1)+'°)';$('#mAd').textContent=nm(SP.dist([0,0,0],dA));SA.dirty=true;}
G=PG.Rounds({el:'#gA',n:GD.length,title:function(i){return GD[i].t;},ask:function(i){return '<p>'+GD[i].a+'</p>';},
  setup:function(i){G&&(G.hit=null);PG.set('rAx',0);PG.set('rAy',0);PG.set('rAz',0);upA();},
  judge:function(i){var a=GD[i].ans,ok=dA[0]===a[0]&&dA[1]===a[1]&&dA[2]===a[2];if(ok){G.hit=a;SA.dirty=true;}
    return [ok,ok?'선반 ('+a.join(', ')+') 도착. '+['같은 주소라 바로 갔어요.','x = ρ cos φ = 5 × 0.8 = 4, y = ρ sin φ = 5 × 0.6 = 3, z는 그대로 2.','z = r cos θ = 3 × 2/3 = 2, 바닥 거리 r sin θ = √5 → x = √5 × 1/√5 = 1, y = √5 × 2/√5 = 2.','3² + y² = 5² → y = 4. 3·4·5 삼각형이에요.'][i]:'아직 선반이 아니에요. 아래 숫자 상자의 "그 자리의 원통 자·지구본 자" 숫자를 주소와 비교해 보세요.','('+dA.join(', ')+')'];}});
[0,1,2].forEach(function(k){$('#rA'+'xyz'[k]).addEventListener('input',function(){dA[k]=+this.value;$('#rA'+'xyz'[k]+'v').textContent=this.value;G&&G.touch();upA();});});upA();
'''

DLG = {
 'open': [['doc', 'doc_board', '이 강의실은 3층에 있습니다. 1층 같은 자리에 앉은 사람과 여러분의 (x, y)는 똑같아요. 그런데 같은 자리인가요?'],
          ['x1', 'x1_hint', '아니요! 저는 1층 매점에 없는데요.'],
          ['doc', 'doc_front', '그래서 숫자가 하나 더 필요합니다. 동쪽·북쪽·위쪽, 서로 직각인 자 세 개. 이것이 <b>공간좌표 (x, y, z)</b>예요.'],
          ['moa', 'moa_report', '3장의 거리·각도 자도 공간에서 쓸 수 있어요?'],
          ['asst', 'asst_smile', '네, 두 가지로 커져요. 원통 자와 지구본 자. 4.3에서 같은 점을 세 자로 읽어 볼게요.']],
 's41_t': [['doc', 'doc_front', '점 하나를 세 슬라이더로 옮겨 봅시다. 바닥에 비친 그림자도 같이 보세요.'],
           ['sia', 'sia_think', '그림자는 2장의 (x, y)네요! 높이만 따로 있는 거죠?'],
           ['fly', 'fly_point', 'z만 움직여 봐. 그림자는 꼼짝 않는데 점은 오르내리지.']],
 's42_t': [['doc', 'doc_front', '1층 출발 창구(원점)에서 3층 선반 B (2, 3, 6)까지 줄을 곧게 당기면 길이가 얼마일까요?'],
           ['robo', 'robo_calc', '제가 바로! 2 + 3 + 6 = 11 m!'],
           ['fly', 'fly_point', '그림을 돌려서 초록 줄과 꺾인 주황·보라 길을 비교해 봐.']],
 's43_t': [['doc', 'doc_front', '점 (1, 1, 1.41)을 세 사람에게 주소로 불러 달라고 했더니 세 가지 답이 왔습니다.'],
           ['moa', 'moa_report', '셋 다 맞는 답이에요?'],
           ['fly', 'fly_point', '자 버튼 셋을 차례로 눌러 봐. 그림에 표시되는 선과 각도가 바뀌어.']],
 'ai42_d': [['robo', 'robo_coin', '원점에서 (2, 3, 6)까지 2 + 3 + 6 = 11 m! 줄은 11 m 사면 됩니다. 계산 끝!']],
 'ai42_e': [['robo', 'robo_sigh', '모서리를 따라 꺾은 길이였네요. 곧게 당기면 7 m. 줄값 4 m어치 아꼈어요.']],
 'app': [['x3', 'x3_hint', '이번엔 3D 드론이다!'],
         ['asst', 'asst_firm', '주소의 자가 무엇인지부터 보세요. 원통 자면 바닥은 3장처럼, 높이는 그대로예요.'],
         ['robo', 'robo_calc', '아래 숫자 상자에 드론 자리를 다른 자로도 띄워 드릴게요. 주소와 같아지면 도착이에요!']],
 'outro': [['doc', 'doc_magic', '오늘의 세 줄입니다.<br>① 공간의 자리는 (x, y, z) 세 숫자. 바닥 그림자 + 높이.<br>② 공간 거리는 세 차이를 제곱해 더하고 루트. 피타고라스를 두 번 쓴 것.<br>③ 같은 점을 원통 자·지구본 자로도 부를 수 있다. 문제 모양에 맞는 자를 고른다.'],
           ['moa', 'moa_tea', '지구본 자의 r을 지구 반지름으로 고정하면… 각도 두 개만 남네요?'],
           ['doc', 'doc_think', '날카롭네요. 그게 바로 위도와 경도입니다. 다음 시간에는 지구 위에서 "나는 어디에 있는가"를 묻고, 둥근 지구를 평평한 지도로 옮기는 매핑을 봅니다.']],
}

PAGE = dict(
 key='ch4', out='04_space.html', logo='4장',
 title='좌표 첫걸음 4장 공간좌표 — 높이가 생기면 세 숫자 | 나는 어디에 있는가?',
 desc='좌표 첫걸음 4장. 바닥 그림자와 높이로 보는 (x, y, z), 피타고라스를 두 번 쓰는 공간 거리 (2, 3, 6) → 7, 같은 점을 모눈 자·원통 자·지구본 자로 읽기, 그리고 다른 자로 적힌 선반 주소를 찾는 드론 배송 게임.',
 nav=NAV,
 cover=dict(cap='좌표 첫걸음 · 4교시', chip='4장 공간좌표 — 높이가 생기면 세 숫자', cast=['fly_point', 'doc_board', 'asst_smile', 'robo_calc', 'sia_explain', 'moa_report', 'x1_hint', 'x2_hint', 'x3_hint'], alt='강의실 탁자 위 3층 건물 모형과 세 축 틀 안에 뜬 배송 드론, 바닥의 점선 그림자. 하루는 원통 모형, 초파리 연구원은 작은 지구본을 든다.', motif='space'),
 eyebrow='좌표 첫걸음 · 4장 · 최적화 첫걸음의 자매편 <span class="diff">난이도: 오르막</span>',
 h1='4장 공간좌표 — 높이가 생기면 세 숫자',
 question='3층 강의실의 내 자리는 1층 같은 자리와 무엇이 다를까?',
 lead='바닥 위의 자리 (x, y)에 높이 z를 더하면 공간의 자리가 됩니다. 이 장은 그림자와 높이로 세 숫자를 읽고, 피타고라스를 두 번 써서 공간 거리를 재고, 같은 점을 원통 자·지구본 자로도 불러 봅니다. 3D 그림은 끌어서 돌리거나 시점 버튼으로 바꿀 수 있어요.',
 start='4.1 → 4.2 → 4.3 순서로 보세요. 4.3의 원통 자·지구본 자는 이름만 익혀도 괜찮습니다. 5장에서 지구본 자가 위도·경도로 다시 나옵니다.',
 kpis=[('m', '3개', '공간의 자리를 정하는 숫자'), ('g', '7', '원점에서 (2, 3, 6)까지 공간 거리'), ('r', '11', '같은 두 점, 모서리를 따라 꺾은 길'), ('a', '(2, 45°, 45°)', '점 (1, 1, √2)의 지구본 자 주소')],
 plain=[('무엇을', '높이가 생긴 공간에서 자리를 세 숫자로 적고, 거리를 재고, 같은 점을 세 가지 자로 읽습니다.'),
        ('왜 중요한가', '드론·창고 로봇·3D 게임·건물 설계가 모두 공간좌표를 씁니다. 지구 위의 위도·경도도 여기서 나옵니다.'),
        ('업무에서는', '물류 위치 코드(구역·선반·단), 3D 모델 좌표를 읽을 때 "어느 자의 주소인지"부터 확인하게 됩니다.')],
 abbr=[('(x, y, z)', '공간좌표', '동쪽·북쪽·위쪽 세 자로 읽은 자리.'), ('ρ (로)', '중심축까지 거리', '원통 자에서 높이 축(z축)에서 떨어진 거리.'), ('φ (파이)', '돈 각도', '바닥에서 동쪽(x축)부터 돈 각도. 3장의 θ와 같은 역할.'),
       ('r · θ', '중심 거리 · 꼭대기 각도', '지구본 자에서 원점까지 거리와 꼭대기(z축)에서 내려온 각도.')],
 hex='4', open_title='높이가 생기면 숫자가 하나 더',
 bigpicture='<div class="chain" aria-label="이 시리즈 지도"><span>1장 수직선</span><i>→</i><span>2장 좌표평면</span><i>→</i><span>3장 극좌표</span><i>→</i><span><b>4장 공간좌표</b></span><i>→</i><span>5장 지구와 지도</span><i>→</i><span>6장 데이터의 좌표</span></div><div class="review30"><b>30초 복습</b> 2장: 평면 거리 √(Δx² + Δy²). 3장: 같은 점을 (거리, 각도)로도 부른다. 오늘은 두 생각을 모두 3차원으로 늘립니다.</div>',
 steps=[
  dict(id='s41', num='4.1', title='바닥 그림자 + 높이 = 세 숫자', tags=['방법: 공간좌표 (x, y, z)', '일상: 건물의 층', '바탕: 자와 각도기의 방 ①편 3축 방'],
       why=dict(problem='같은 (x, y) 자리라도 층이 다르면 다른 곳입니다.', limit='좌표평면은 바닥 위만 말할 수 있습니다.',
                solve='바닥의 두 자에 직각인 세 번째 자(높이 z)를 세웁니다.', easy='"3층, 2열, 1줄" — 층 번호를 하나 더 말하는 것.'),
       math=dict(who='sia', q='(2, 1, 3)에서 숫자 하나를 빼면 어떻게 돼요?', words='z를 빼면 바닥에 비친 그림자 (2, 1)만 남습니다. 그 그림자 위로 곧게 선 줄 위의 모든 점이 같은 그림자를 가져요. 그래서 세 숫자가 모두 있어야 점 하나가 정해집니다.',
                 school='공간좌표, 정사영(그림자)', rows=[('(x, y, z)', '엑스 와이 제트', '동쪽·북쪽·높이로 읽은 자리'), ('(x, y, 0)', '높이를 0으로', '바닥에 비친 그림자(정사영)')],
                 tries=['점 (2, 1, 3)', '그림자 (2, 1, 0)', '(2, 1, 0), (2, 1, 1), (2, 1, 5)… 모두 같은 그림자'], comment='숫자가 하나 빠지면 점 하나가 줄 하나로 흐려지네요!'),
       daily='아파트 주소의 "동·호수"도 비슷합니다. 호수 1203은 12층의 3번 집, 높이와 자리를 한 번에 말하죠.',
       field='3D 게임, 드론, 창고 로봇은 모두 (x, y, z)로 움직입니다. 데이터에서도 열을 세 개 고르면 한 줄이 공간의 점 하나가 돼요(6장).',
       panel=PANEL41,
       doc='공간의 자리는 "그림자 + 높이"로 읽으면 쉽습니다. 2장에서 배운 것을 바닥에 그대로 쓰고, 높이 하나만 더 챙기세요.',
       limit='세 자가 서로 직각인 경우만 봤어요. 비스듬한 자는 쓰지 않습니다.'),
  dict(id='s42', num='4.2', title='공간 거리 — 피타고라스를 두 번', tags=['방법: 공간에서 두 점 사이 거리', '일상: 줄 당기기', '판단: 더하기와 거리'],
       why=dict(problem='공간의 두 점이 곧장 얼마나 떨어졌는지 알고 싶습니다.', limit='평면 거리는 바닥만 잽니다. 높이 차이가 빠져요.',
                solve='바닥에서 피타고라스로 대각선을 구하고, 그 대각선과 높이로 피타고라스를 한 번 더 씁니다.', easy='상자 안 모서리에서 반대쪽 모서리까지 막대를 대각선으로 넣는 길이.'),
       math=dict(who='moa', q='평면에서는 √(Δx² + Δy²)였는데, 공간에서는 √(Δx² + Δy² + Δz²)로 그냥 하나 더 붙이면 돼요?', words='네. 바닥 대각선의 제곱이 Δx² + Δy²이니, 거기에 높이 제곱을 더하면 됩니다. 축이 몇 개로 늘어도 같은 방식이에요(6장).',
                 school='공간에서 두 점 사이의 거리, 피타고라스 정리', rows=[('√(x² + y²)', '바닥 대각선', '① 그림자까지의 거리'), ('√(x² + y² + z²)', '공간 대각선', '③ 곧장 잰 거리')],
                 tries=['B (2, 3, 6): 바닥 대각선 √(4 + 9) = √13 ≈ 3.61', '공간 거리 √(13 + 36) = √49 = 7', '그냥 더하면 2 + 3 + 6 = 11 (모서리 길)'], comment='7이 딱 떨어지게 고른 숫자였어요. 2·3·6·7!'),
       daily='택배 상자에 긴 우산이 들어가는지 볼 때 재는 것이 바로 공간 대각선입니다.',
       field='데이터 세 열(예: 키·몸무게·나이)로 두 사람이 얼마나 다른지 잴 때도 이 거리를 씁니다. 6장에서는 축이 열 개, 백 개로 늘어나요.',
       panel=PANEL42,
       ai=dict(id='ai42', title='조교 주판봇의 1초 답, 믿어도 될까?', checks=['11 m는 곧게 당긴 줄인가, 상자 모서리를 따라 꺾은 길인가?', '대각선이 세 모서리의 합과 같을 수 있나?'],
               verdict='곧게 당긴 줄은 <b>√(2² + 3² + 6²) = 7 m</b>입니다. 11 m는 모서리를 따라 꺾어 가는 길이에요(2장의 골목 거리와 같은 종류). 숫자를 더하기 전에 "곧장인가, 꺾어 가나"를 물어보세요.'),
       doc='축이 늘어도 거리 재는 법은 같습니다. 차이를 제곱해 모두 더하고 루트. 이 한 줄이 6장 데이터 공간까지 그대로 갑니다.',
       code=[('math.dist((0, 0, 0), (2, 3, 6))', '공간 거리 → 7.0')],
       limit='세 축의 단위가 모두 m로 같을 때만 그대로 더할 수 있습니다.'),
  dict(id='s43', num='4.3', title='같은 점, 세 가지 자 — 모눈·원통·지구본', tags=['방법: 원통좌표·구면좌표', '일상: 회전목마·지구본', '바탕: 벡터 분석 랩 0편 방 A'],
       why=dict(problem='원기둥 탱크, 회전하는 기계, 지구처럼 둥근 것을 상자 모양 자로 적으면 식이 길어집니다.', limit='모눈 자 (x, y, z)는 상자 모양에만 잘 맞습니다.',
                solve='둥근 것에는 둥근 자를 씁니다. 원통 자 = 3장 극좌표 + 높이, 지구본 자 = 중심 거리 + 각도 두 개.', easy='같은 집을 "도로명 주소"로도 "위도·경도"로도 부를 수 있는 것.'),
       math=dict(who='moa', q='점 (1, 1, 1.41)의 지구본 자 주소 (2, 45°, 45°)는 어떻게 나와요?', words='중심까지 거리 r은 4.2의 공간 거리입니다. 꼭대기 각도 θ는 "높이 ÷ r"로, 바닥 각도 φ는 3장처럼 바닥 그림자로 구해요.',
                 school='공간좌표, 삼각함수, 피타고라스', rows=[('ρ = √(x² + y²)', '로', '바닥에서 중심축까지 거리 (원통 자)'), ('r = √(x² + y² + z²)', '알', '원점까지 거리 (지구본 자)'), ('cos θ = z ÷ r', '코사인 세타는 제트 나누기 알', '꼭대기에서 내려온 각도'), ('φ', '파이', '바닥에서 동쪽부터 돈 각도 (두 자 공통)')],
                 tries=['ρ = √(1 + 1) = 1.41, φ = 45° → 원통 자 (1.41, 45°, 1.41)', 'r = √(1 + 1 + 2) = 2', 'cos θ = 1.41 ÷ 2 = 0.707 → θ = 45° → 지구본 자 (2, 45°, 45°)'], comment='자를 바꿔도 점은 그대로, 주소만 바뀌었어요.'),
       daily='회전목마 위 말의 자리는 "중심에서 몇 m, 몇 도 돌았나, 얼마나 떠 있나"(원통 자)로 말하는 게 편합니다.',
       field='드론의 짐벌·로봇 팔은 원통·지구본 자로 움직이고, 지도·위성 데이터는 지구본 자(위도·경도)로 저장됩니다. AI가 쓰는 데이터도 어느 자로 적혔는지에 따라 거리 계산이 달라져요.',
       panel=PANEL43,
       doc='좌표계는 "자리를 부르는 방식"입니다. 자리는 하나, 부르는 방식은 여럿. 계산이 쉬워지는 자를 골라 쓰고, 필요하면 모눈 자로 바꿔 거리를 재세요.',
       limit='원통 자는 중심축 위(ρ = 0)에서, 지구본 자는 꼭대기(θ = 0°)에서 각도 φ를 정할 수 없습니다. 북극에서 "동쪽"이 없는 것과 같아요. 각도 한 걸음의 실제 길이는 <a href="https://adminmrobo.github.io/vector_analysis_lab/00_orientation.html">벡터 분석 랩 0편</a>에서 더 봅니다.'),
 ],
 app_title='드론 배송 — 다른 자로 적힌 선반 주소 찾기', app_lead='물류창고 주소가 모눈 자·원통 자·지구본 자·거리 조건으로 옵니다. 모두 모눈 자로 바꿔 드론을 보내세요.', app_html=APP,
 sum_title='공간에서 자리를 말하는 법',
 summary=[('공간의 자리는?', '(x, y, z) 세 숫자. 바닥 그림자 + 높이.', '4.1'), ('공간 거리는?', '√(Δx² + Δy² + Δz²). 피타고라스를 두 번.', '4.2'),
          ('둥근 것은?', '원통 자 (ρ, φ, z) 또는 지구본 자 (r, θ, φ).', '4.3'), ('자를 바꿔도?', '점은 그대로, 주소만 바뀐다.', '4.3·부록')],
 cards=[('공간좌표', '직각인 자 세 개로 적은 자리.'), ('정사영(그림자)', '높이를 0으로 눌러 바닥에 비친 자리.'), ('공간 거리', '세 차이 제곱 합의 루트.'), ('원통좌표', '극좌표 + 높이.'), ('구면좌표(지구본 자)', '중심 거리 + 각도 두 개.'), ('좌표 변환', '같은 자리를 다른 자의 주소로 바꾸기.')],
 limits=['창고 선반·건물 층은 설명용 자리입니다.', '세 자가 서로 직각인 경우만 다뤘습니다.'],
 next=[('05_earth_map.html', '5장 지구와 지도 →', '위도·경도, 경도 1도의 길이, 메르카토르 지도'), ('03_polar.html', '← 3장 극좌표', ''), ('index.html', '목차', '')],
 refs=[('안상선, 「벡터 분석 랩」 0편 방 A 네 개의 자 (vector_analysis_lab)', '4.3 점 (1, 1, 1.41)을 모눈·원통·지구본 자로 읽기'),
       ('안상선, 「자와 각도기의 방」 ①편 1축·2축·3축 방 (euclidean_space_lab)', '4.1 축을 하나씩 늘리는 생각, 4.2 몇 축이든 피타고라스'),
       ('안상선, 「좌표축 위의 그릇」 3편 화살표 밭 (optimization_3d_map)', '3D 공간 그림 모듈(Space3D)과 x·y·z 축 색 약속')],
 examples=['선반 B (2, 3, 6), 창고 선반 주소 네 개', '점 (1, 1, 1.41) — √2를 1.41로 반올림'],
 dlg=DLG, js=JS,
 gloss={'공간좌표': ['공간좌표', '좌표', '직각인 x·y·z 세 축으로 적은 자리.'], '정사영': ['정사영', '수학', '빛을 곧게 비췄을 때 바닥에 생기는 그림자 자리.'], '원통좌표': ['원통좌표', '좌표', '(중심축 거리 ρ, 각도 φ, 높이 z).'],
        '구면좌표': ['구면좌표', '좌표', '(원점 거리 r, 꼭대기 각도 θ, 바닥 각도 φ). 지구본 자.'], '짐벌': ['짐벌', '기계', '카메라를 각도로 돌려 흔들림을 잡는 장치.']},
 gloss_core=['공간좌표', '정사영', '원통좌표', '구면좌표'],
 quiz={'s41': [{'q': '점 (5, −2, 4)의 바닥 그림자는?', 'o': ['(5, −2, 0)', '(5, 0, 4)', '(0, 0, 4)'], 'a': 0, 'why': '높이만 0으로 누릅니다.', 'hint': 'z를 0으로.'}],
       's42': [{'q': '원점에서 (1, 2, 2)까지 공간 거리는?', 'o': ['3', '5', '9'], 'a': 0, 'why': '√(1 + 4 + 4) = √9 = 3.', 'hint': '제곱해서 모두 더하기.'}],
       's43': [{'q': '원통 자 (2, 90°, 3)인 점의 모눈 자 주소는?', 'o': ['(0, 2, 3)', '(2, 0, 3)', '(2, 90, 3)'], 'a': 0, 'why': 'φ = 90°는 북쪽. x = 2 cos 90° = 0, y = 2 sin 90° = 2, z는 그대로.', 'hint': '3장의 극좌표 + 높이.'}]},
)

KG = dict(
 nodes=[('Concept', 'space-coordinates', '공간좌표', '3D Cartesian coordinates', '#s41', '직각인 자 세 개로 적은 자리 (x, y, z).'),
        ('Concept', 'projection', '정사영(바닥 그림자)', 'Orthogonal projection', '#s41', '높이를 0으로 눌러 바닥에 비친 자리.'),
        ('Concept', 'distance-3d', '공간 거리', '3D distance', '#s42', '√(Δx² + Δy² + Δz²).'),
        ('Concept', 'cylindrical', '원통좌표', 'Cylindrical coordinates', '#s43', '극좌표 + 높이 (ρ, φ, z).'),
        ('Concept', 'spherical', '구면좌표(지구본 자)', 'Spherical coordinates', '#s43', '(r, θ, φ). 위도·경도의 뿌리.'),
        ('Concept', 'coordinate-transform', '좌표 변환', 'Coordinate transformation', '#s43', '같은 자리를 다른 자의 주소로 바꾸기.'),
        ('Simulation', 'drone-delivery', '드론 배송 게임', 'Drone delivery game', '#app', '다른 자로 적힌 선반 주소를 모눈 자로 바꾸는 네 판.'),
        ('Limitation', 'pole', '축 위·꼭대기에서 각도가 정해지지 않음', 'Coordinate singularity', '#s43', 'ρ = 0 또는 θ = 0에서 φ가 없다.'),
        ('Question', 'lat-lon', '지구본 자의 r을 고정하면?', 'Fix r on the globe?', '#outro', '5장 위도·경도로 이어지는 질문.')],
 edges=[('projection', 'partOf', 'space-coordinates', '#s41'), ('space-coordinates', 'prerequisiteOf', 'distance-3d', '#s42'), ('cylindrical', 'relatedTo', 'spherical', '#s43'),
        ('coordinate-transform', 'relatedTo', 'cylindrical', '#s43'), ('coordinate-transform', 'demonstratedBy', 'drone-delivery', '#app'), ('spherical', 'hasLimitation', 'pole', '#s43'), ('spherical', 'prerequisiteOf', 'lat-lon', '#outro')])
