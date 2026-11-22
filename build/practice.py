# -*- coding: utf-8 -*-
"""마지막 장 · 실전 연습장 — 네 현장을 직접 운영하는 시뮬레이터 대시보드 (스킬 6-1)"""
import json, os
from gen import EXTRA_CSS, AUTHOR, DATE, VER, SITE, esc, B

def scene(sid, title, place, situation, env, dec, score_ids, g1, g2, missions, back):
    sc = ''.join(f'<div class="mini {c}"><span>{t}</span><b id="{sid}_{k}">—</b></div>' for k, c, t in score_ids)
    ms = ''.join(f'<li id="{sid}_m{i}"><span class="mst">○</span> <b>미션 {i+1}</b> {m}</li>' for i, m in enumerate(missions))
    bk = ' · '.join(f'<a href="../{h}">{t}</a>' for h, t in back)
    return f'''<section class="scene" id="{sid}" role="tabpanel" aria-labelledby="tab-{sid}" hidden>
<h2 style="margin-top:8px">{title} <span class="sub">{place}</span></h2>
<div class="sit"><b>상황</b> {situation}</div>
<div class="ctrl board"><div class="group env"><span class="gtag env">시장·현장 조건</span>{env}</div><div class="group dec"><span class="gtag dec">내 결정</span>{dec}</div></div>
<div class="minis">{sc}</div>
<div class="twin"><div class="cwrap {g1[1]}"><canvas id="{sid}_g1" aria-label="{g1[0]}"></canvas></div><div class="cwrap"><canvas id="{sid}_g2" aria-label="{g2}" style="height:{ '420px' if g1[1]=='t3' else '260px'}"></canvas></div></div>
<div class="dialog lvtalk" id="{sid}_talk"></div>
<div class="missions"><h3>미션 3개</h3><ol>{ms}</ol></div>
<p class="back"><b>배운 곳 다시 보기</b> {bk}</p>
</section>'''

S1 = scene('ship', '① 지구 배송센터', '5장 위도·경도', '드론이 창고에서 위선을 따라 동쪽으로 날아 배송합니다. 배터리가 모자라면 추락, 너무 크면 무거워 비용이 듭니다. 실제 비행 거리보다 <b>10~30% 여유</b>가 있는 배터리를 고르면 "적정"입니다.',
  '<label class="glabel" for="ship_lat">창고 위도</label><input type="range" id="ship_lat" min="0" max="70" step="0.5" value="0"><span class="val" id="ship_latv">0°</span><label class="glabel" for="ship_dl">동쪽 경도 차이</label><input type="range" id="ship_dl" min="1" max="20" step="1" value="10"><span class="val" id="ship_dlv">10°</span>',
  '<label class="glabel" for="ship_bat">배터리 용량</label><input type="range" id="ship_bat" min="100" max="2500" step="10" value="1200"><span class="val" id="ship_batv">1,200 km</span>',
  [('a', 'm', '실제 비행 거리'), ('b', 'a', '내 배터리'), ('c', 'g', '남는 여유'), ('d', 'r', '판정')],
  ('위도에 따른 경도 1도 길이 곡선과 지금 창고 위도', 'tall'), '실제 거리와 배터리, 적정 범위 막대',
  ['위도 37.5°에서 경도 10° 배송을 <b>적정</b>(여유 10~30%)으로 만드세요.', '함정 관찰: 위도 60°, 경도 10° 배송에 "적도 기준 1,112 km"로 계산한 배터리(1,110~1,120 km)를 실어 보세요. 판정이 무엇으로 나오는지 확인합니다.', '조건을 바꿔도: 위도 60°·경도 10°와 위도 0°·경도 5°에서 <b>같은 배터리</b>로 둘 다 적정이 되는지 확인하세요 (두 조건을 차례로 맞추면 통과).'],
  [('05_earth_map.html#s52', '5.2 경도 1도의 길이'), ('05_earth_map.html#app', '5장 부록 게임')])

S2 = scene('radar', '② 관제탑', '3장 극좌표', '레이더 화면에는 표적이 모눈 자 (x, y)로 뜨지만, 요격 드론에는 거리 r과 각도 θ만 입력할 수 있습니다. 표적에서 <b>0.3 안</b>이면 명중입니다.',
  '<span class="glabel">표적</span><button class="bt" type="button" data-rt="3,4" aria-pressed="true">(3, 4)</button><button class="bt" type="button" data-rt="-3,-4" aria-pressed="false">(−3, −4)</button><button class="bt" type="button" data-rt="0,-5" aria-pressed="false">(0, −5)</button><button class="bt" type="button" data-rt="-6,2" aria-pressed="false">(−6, 2)</button>',
  '<label class="glabel" for="radar_r">거리 r</label><input type="range" id="radar_r" min="0" max="8" step="0.05" value="2"><span class="val" id="radar_rv">2.00</span><label class="glabel" for="radar_t">각도 θ</label><input type="range" id="radar_t" min="0" max="359.5" step="0.5" value="0"><span class="val" id="radar_tv">0°</span>',
  [('a', 'm', '표적 (x, y)'), ('b', 'a', '내 명령 (r, θ)'), ('c', 'g', '표적까지 남은 거리'), ('d', 'r', '판정')],
  ('레이더 화면, 표적과 드론', 'tall'), '지금 거리 r에서 각도를 바꿀 때 남는 거리 곡선',
  ['표적 (3, 4)를 명중시키세요.', '함정 관찰: 표적 (−3, −4)에 "4 ÷ 3의 각도 53.1°"를 그대로 넣어 보세요(r = 5, θ 53~53.5°). 어디로 날아가는지 확인합니다.', '표적 (−3, −4)와 (0, −5)를 차례로 명중시키세요. 사분면을 먼저 보면 됩니다.'],
  [('03_polar.html#s31', '3.1 같은 점, 두 이름'), ('03_polar.html#app', '3장 레이더 게임')])

S3 = scene('ware', '③ 물류창고', '4장 공간좌표', '선반 주소가 원통 자·지구본 자로 섞여 들어옵니다. 드론은 x·y·z 세 슬라이더로 움직이고, 곧장 날면 모서리를 따라 가는 것보다 배터리를 아낍니다.',
  '<span class="glabel">주문서</span><button class="bt" type="button" data-wo="0" aria-pressed="true">원통 자 (5, 36.87°, 2)</button><button class="bt" type="button" data-wo="1" aria-pressed="false">지구본 자 (3, 48.19°, 63.43°)</button><button class="bt" type="button" data-wo="2" aria-pressed="false">곧장 7, 모서리 길 11</button>',
  '<label class="glabel" for="ware_x">x</label><input type="range" id="ware_x" min="-6" max="6" step="1" value="0"><span class="val" id="ware_xv">0</span><label class="glabel" for="ware_y">y</label><input type="range" id="ware_y" min="-6" max="6" step="1" value="0"><span class="val" id="ware_yv">0</span><label class="glabel" for="ware_z">z</label><input type="range" id="ware_z" min="-6" max="6" step="1" value="0"><span class="val" id="ware_zv">0</span>',
  [('a', 'm', '드론 자리 (x, y, z)'), ('b', 'g', '곧장 간 거리'), ('c', 'a', '모서리 길 거리'), ('d', 'r', '주문서와 맞나')],
  ('3차원 창고와 드론', 't3'), '곧장 간 거리와 모서리 길 거리 막대',
  ['원통 자 주문서 (ρ = 5, φ = 36.87°, z = 2)의 선반에 드론을 보내세요.', '지구본 자 주문서 (r = 3, θ = 48.19°, φ = 63.43°)의 선반에 드론을 보내세요.', '"곧장 7, 모서리 길 11" 주문서: 출고 창구(원점)에서 곧장 잰 거리가 7이고 모서리를 따라 가면 11인 선반을 아무거나 하나 찾으세요.'],
  [('04_space.html#s42', '4.2 공간 거리'), ('04_space.html#s43', '4.3 세 가지 자'), ('04_space.html#app', '4장 드론 배송')])

S4 = scene('shop', '④ 추천 매장', '6장 데이터의 좌표', '새 손님이 오면 가장 닮은 기존 고객에게 보냈던 쿠폰을 보냅니다. 어떤 자로 재느냐, 나이를 얼마나 중요하게 보느냐가 내 결정입니다.',
  '<label class="glabel" for="shop_age">새 손님 나이</label><input type="range" id="shop_age" min="20" max="60" step="1" value="30"><span class="val" id="shop_agev">30세</span><label class="glabel" for="shop_buy">월 구매액</label><input type="range" id="shop_buy" min="50" max="480" step="10" value="200"><span class="val" id="shop_buyv">200천 원</span>',
  '<span class="glabel">자</span><button class="bt" type="button" data-sm="raw" aria-pressed="true">원래 단위</button><button class="bt" type="button" data-sm="z" aria-pressed="false">표준화</button><label class="glabel" for="shop_w">나이 중요도</label><input type="range" id="shop_w" min="0.5" max="3" step="0.5" value="1"><span class="val" id="shop_wv">1.0배</span>',
  [('a', 'r', '가장 닮은 고객'), ('b', 'a', '2위 · 3위'), ('c', 'g', '1위와 나이 차이'), ('d', 'm', '1위와 구매액 차이')],
  ('고른 자로 그린 고객 지도와 새 손님', 'tall'), '모든 고객까지의 거리 막대(가까운 순)',
  ['새 손님 (30세, 200천 원)의 1위가 <b>A</b>가 되게 자를 고르세요.', '함정 관찰: 같은 손님을 원래 단위로 재서 1위 고객과의 나이 차이를 확인하세요 (원래 단위·나이 중요도 1·손님 (30, 200)).', '조건을 바꿔도: 손님 (42세, 330천 원)을 표준화 자로 재고, 나이 중요도를 1에서 2 이상으로 올려도 1위가 D로 유지되는지 확인하세요 (중요도 1과 2 이상을 모두 거치면 통과).'],
  [('06_data_space.html#s62', '6.2 단위 맞추기'), ('06_data_space.html#app', '6장 쿠폰 담당자'), ('01_number_line.html#s13', '1.3 표준화')])

JS = r'''
var $=U.$,$$=U.$$,fmt=U.fmt,V=PG.V;
function tabs(){var ids=['ship','radar','ware','shop'],cur=(location.hash||'').slice(1);if(ids.indexOf(cur)<0)cur='ship';
  ids.forEach(function(id){$('#'+id).hidden=id!==cur;$('#tab-'+id).setAttribute('aria-selected',String(id===cur));});U.drawAll();}
$$('[role=tab]').forEach(function(b){b.onclick=function(){history.replaceState(null,'','#'+b.dataset.t);tabs();};});window.addEventListener('hashchange',tabs);
function talk(id,L){$('#'+id+'_talk').innerHTML=L.map(function(x,i){return U.say(x[0],x[1],x[2],i%2===1);}).join('');}
function mis(id,k,st){var li=$('#'+id+'_m'+k);if(!li)return;li.className=st?'ok':'';li.querySelector('.mst').textContent=st?'●':'○';}
function bars(cv,items,o){var R=U.setup(cv),g=R.g,w=R.w,h=R.h;U.grid24(g,w,h);var L=12,top=26,bh=Math.min(26,(h-top-12)/items.length-8),mx=o.max;
  items.forEach(function(it,i){var y=top+i*(bh+10);g.fillStyle='rgba(22,33,43,.06)';g.fillRect(L,y,w-2*L,bh);g.fillStyle=it[2];g.fillRect(L,y,(w-2*L)*Math.min(1,it[1]/mx),bh);U.label(g,L+6,y+bh/2,it[0]+' '+it[3],U.cssv('--text'));});
  if(o.band){var x0=L+(w-2*L)*o.band[0]/mx,x1=L+(w-2*L)*Math.min(1,o.band[1]/mx);g.fillStyle='rgba(19,115,58,.12)';g.fillRect(x0,top-8,x1-x0,h-top);U.label(g,x0+4,14,o.band[2],U.cssv('--gfp'));}}
/* ① 배송센터 */
(function(){var s={lat:0,dl:10,bat:1200,t:false},M=[0,0,0],m3={a:0,b:0};
  var g1=V($('#ship_g1'),function(){var pts=[];for(var a=0;a<=80;a++)pts.push([a,SP.lonKm(a)]);var P=U.plot($('#ship_g1'),{xr:[0,80],yr:[0,120],xt:[0,20,40,60,80],yt:[0,40,80,120],xl:'위도 (°)',yl:'경도 1도 (km)',series:[{pts:pts,color:U.cssv('--amber'),width:3}],vlines:[{x:s.lat,color:U.cssv('--eye'),label:'창고 '+s.lat+'°'}]});
    P.g.beginPath();P.g.arc(P.X(s.lat),P.Y(SP.lonKm(s.lat)),6,0,7);P.g.fillStyle=U.cssv('--eye');P.g.fill();});
  var g2=V($('#ship_g2'),function(){var d=SP.lonKm(s.lat)*s.dl;bars($('#ship_g2'),[['실제 거리',d,U.cssv('--stain'),Math.round(d)+' km'],['내 배터리',s.bat,U.cssv('--info'),s.bat.toLocaleString()+' km']],{max:2600,band:[d*1.1,d*1.3,'적정 범위 (여유 10~30%)']});});
  function up(){var d=SP.lonKm(s.lat)*s.dl,mg=(s.bat-d)/d,j=mg<0?'추락 위험':mg<0.1?'아슬아슬':mg<=0.3?'적정':'과잉 (무거움)';
    $('#ship_a').textContent=Math.round(d).toLocaleString()+' km';$('#ship_b').textContent=s.bat.toLocaleString()+' km';$('#ship_c').textContent=Math.round(mg*100)+'%';$('#ship_d').textContent=j;
    var ok=j==='적정';talk('ship',[['doc',ok?'doc_judge':'doc_think',ok?'적정입니다. 위도 '+s.lat+'°의 경도 1도('+fmt(SP.lonKm(s.lat),1)+' km)를 제대로 썼네요.':'판정은 "'+j+'". 거리 = 111.2 × cos(위도) × 경도 차이부터 다시 확인해 보세요.'],
      ['asst','asst_report','실제 거리 '+Math.round(d)+' km, 여유 '+Math.round(mg*100)+'%예요.'],
      ['fly','fly_magnify',s.lat>=50?'북쪽 창고야. 적도 기준 숫자를 그대로 쓰면 배터리가 남아돌 거야.':'위도를 바꾸면 같은 '+s.dl+'°라도 거리가 달라지는지 봐.'],
      ['robo',mg>0.3?'robo_sigh':'robo_coin',mg>0.3?'적도 기준 111 km로 계산하면 늘 넉넉하니까 안전하죠? …무겁긴 하네요.':'경도 1도는 어디서나 111 km! …라고 하고 싶지만 cos를 곱할게요.']]);
    if(s.t){if(s.lat===37.5&&s.dl===10&&ok)M[0]=1;if(s.lat===60&&s.dl===10&&s.bat>=1110&&s.bat<=1120&&j.indexOf('과잉')===0)M[1]=1;
      if(ok&&s.lat===60&&s.dl===10)m3.a=s.bat;if(ok&&s.lat===0&&s.dl===5)m3.b=s.bat;if(m3.a&&m3.b&&m3.a===m3.b)M[2]=1;}
    M.forEach(function(v,k){mis('ship',k,v);});g1.dirty=true;g2.dirty=true;}
  [['ship_lat','lat',function(v){return v+'°';}],['ship_dl','dl',function(v){return v+'°';}],['ship_bat','bat',function(v){return v.toLocaleString()+' km';}]].forEach(function(z){var r=$('#'+z[0]);r.addEventListener('input',function(){s[z[1]]=+r.value;$('#'+z[0]+'v').textContent=z[2](+r.value);s.t=true;up();});});up();
  window.SHIP={s:s,up:up,M:M};})();
/* ② 관제탑 */
(function(){var s={T:[3,4],r:2,t:0,tc:false},M=[0,0,0],hit={};
  function radar(cv){var P=SP.Plane(cv,{xr:[-7,7],yr:[-7,7],xl:'x',yl:'y',lstep:2});for(var k=1;k<=7;k++)SP.circ(P,0,0,k,'rgba(15,127,134,.18)',1);return P;}
  var g1=V($('#radar_g1'),function(){var P=radar($('#radar_g1')),q=SP.fromPolar(s.r,s.t);SP.dot(P,s.T[0],s.T[1],U.cssv('--eye'),8,'표적');SP.circ(P,s.T[0],s.T[1],0.3,U.cssv('--eye'),1.2,[3,3]);SP.arr(P,[0,0],q,U.cssv('--info'),2.4);SP.dot(P,q[0],q[1],U.cssv('--info'),6,'드론',10,16);});
  var g2=V($('#radar_g2'),function(){var pts=[];for(var a=0;a<=360;a+=2){var q=SP.fromPolar(s.r,a);pts.push([a,SP.dist(q,s.T)]);}var P=U.plot($('#radar_g2'),{xr:[0,360],yr:[0,14],xt:[0,90,180,270,360],yt:[0,2,4,6,8,10,12,14],xl:'각도 θ (°)',yl:'남은 거리',series:[{pts:pts,color:U.cssv('--terrain'),width:2.4}],vlines:[{x:s.t,color:U.cssv('--info'),label:'내 θ'}],hlines:[{y:0.3,color:U.cssv('--gfp'),label:'명중선 0.3',left:true}]});});
  function up(){var q=SP.fromPolar(s.r,s.t),d=SP.dist(q,s.T),ok=d<=0.3,ans=SP.toPolar(s.T[0],s.T[1]);$('#radar_a').textContent='('+s.T+')';$('#radar_b').textContent='('+fmt(s.r,2)+', '+s.t+'°)';$('#radar_c').textContent=fmt(d,2);$('#radar_d').textContent=ok?'명중':'빗나감';
    var wrongQ=Math.abs(s.t-53.1)<0.6&&s.T[0]<0;talk('radar',[['doc',ok?'doc_judge':'doc_think',ok?'명중. ('+s.T+') = ('+fmt(ans[0],2)+', '+fmt(ans[1],1)+'°)를 정확히 통역했어요.':'아직입니다. 거리 r은 맞았나요? 각도는 표적이 어느 사분면인지부터 보세요.'],
      ['asst','asst_report','남은 거리 '+fmt(d,2)+'. 명중선은 0.3이에요.'],['fly','fly_point',wrongQ?'53.1°는 오른쪽 위 방향이야. 표적은 왼쪽 아래인데?':'아래 곡선에서 가장 낮은 곳의 각도를 찾아 봐.'],
      ['robo',wrongQ?'robo_sigh':'robo_calc',wrongQ?'4 ÷ 3의 각도라서 53.1°… 사분면을 안 봤네요. 180°를 더하면 233.1°!':'거리 r은 피타고라스로 바로 계산해 드릴게요: '+fmt(ans[0],2)]]);
    if(s.tc){if(ok)hit[s.T+'']=1;if(hit['3,4'])M[0]=1;if(s.T[0]===-3&&Math.abs(s.r-5)<0.06&&s.t>=53&&s.t<=53.5&&!ok)M[1]=1;if(hit['-3,-4']&&hit['0,-5'])M[2]=1;}
    M.forEach(function(v,k){mis('radar',k,v);});g1.dirty=true;g2.dirty=true;}
  $$('[data-rt]').forEach(function(b){b.onclick=function(){s.T=b.dataset.rt.split(',').map(Number);$$('[data-rt]').forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});up();};});
  [['radar_r','r',function(v){return fmt(v,2);}],['radar_t','t',function(v){return v+'°';}]].forEach(function(z){var r=$('#'+z[0]);r.addEventListener('input',function(){s[z[1]]=+r.value;$('#'+z[0]+'v').textContent=z[2](+r.value);s.tc=true;up();});});up();
  window.RADAR={s:s,up:up,M:M};})();
/* ③ 물류창고 */
(function(){var s={o:0,p:[0,0,0],t:false},M=[0,0,0],O=[[4,3,2],[1,2,2],null];
  var S=new U.Space3D($('#ware_g1'),{L:6,axes:['x','y','z']});
  S.ov.push(function(g,S){var p=s.p;S.line3(g,[[0,0,0],[p[0],0,0],[p[0],p[1],0],p],'rgba(163,92,0,.7)',2,[5,4]);S.line3(g,[[0,0,0],p],U.cssv('--gfp'),2.6);S.drop(g,p[0],p[1],p[2]);var q=S.dot3(g,p[0],p[1],p[2],U.cssv('--info'),7);U.label(g,q[0]+10,q[1]-10,'드론 ('+p+')',U.cssv('--info'));});
  var g2=V($('#ware_g2'),function(){var d=SP.dist([0,0,0],s.p),t=SP.taxi([0,0,0],s.p);bars($('#ware_g2'),[['곧장',d,U.cssv('--gfp'),fmt(d,2)],['모서리 길',t,U.cssv('--amber'),String(t)]],{max:18});});
  function match(){var p=s.p,o=O[s.o];if(o)return p[0]===o[0]&&p[1]===o[1]&&p[2]===o[2];return Math.abs(SP.dist([0,0,0],p)-7)<1e-9&&SP.taxi([0,0,0],p)===11;}
  function up(){var p=s.p,d=SP.dist([0,0,0],p),t=SP.taxi([0,0,0],p),ok=match(),cy=SP.cyl(p[0],p[1],p[2]),sp=SP.sph(p[0],p[1],p[2]);$('#ware_a').textContent='('+p+')';$('#ware_b').textContent=fmt(d,2);$('#ware_c').textContent=t;$('#ware_d').textContent=ok?'맞음 — 도착':'아직';
    talk('ware',[['doc',ok?'doc_judge':'doc_think',ok?'주문서 선반에 도착했습니다. 자를 바꿔도 자리는 하나라는 것, 확인했죠.':'지금 자리를 주문서와 같은 자로 읽어 보세요. 원통 자 ('+fmt(cy[0],2)+', '+fmt(cy[1],1)+'°, '+p[2]+'), 지구본 자 ('+fmt(sp[0],2)+', '+fmt(sp[1],1)+'°, '+fmt(sp[2],1)+'°).'],
      ['asst','asst_report','곧장 '+fmt(d,2)+', 모서리 길 '+t+'. 곧장 날면 '+fmt(t-d,2)+'만큼 아껴요.'],['fly','fly_point','그림을 돌려 봐. 초록 줄이 곧장, 주황 점선이 모서리 길이야.'],
      ['robo',s.o===2?'robo_calc':'robo_smile',s.o===2?'곧장 7이면 제곱 합이 49, 모서리 길 11이면 절댓값 합이 11. 2·3·6이 떠오르는데요?':'주문서 자를 모눈 자로 바꾸는 건 cos·sin 몫 나누기예요!']]);
    if(s.t&&ok)M[s.o]=1;M.forEach(function(v,k){mis('ware',k,v);});S.dirty=true;g2.dirty=true;}
  $$('[data-wo]').forEach(function(b){b.onclick=function(){s.o=+b.dataset.wo;$$('[data-wo]').forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});up();};});
  [0,1,2].forEach(function(k){var r=$('#ware_'+'xyz'[k]);r.addEventListener('input',function(){s.p[k]=+r.value;$('#ware_'+'xyz'[k]+'v').textContent=r.value;s.t=true;up();});});up();
  window.WARE={s:s,up:up,M:M};})();
/* ④ 추천 매장 */
(function(){var CU=[["A",31,260],["B",52,205],["C",25,120],["D",45,380],["E",35,450],["F",58,150],["G",28,300],["H",40,90],["I",23,240],["J",50,320]],PT=CU.map(function(c){return [c[1],c[2]];}),
  MU=[SP.mean(PT.map(function(p){return p[0];})),SP.mean(PT.map(function(p){return p[1];}))],SD=[SP.sd(PT.map(function(p){return p[0];})),SP.sd(PT.map(function(p){return p[1];}))];
  var s={q:[30,200],m:'raw',w:1,t:false},M=[0,0,0],m3={w1:0,w2:0};
  function tr(p){return s.m==='z'?[(p[0]-MU[0])/SD[0]*s.w,(p[1]-MU[1])/SD[1]]:[p[0]*s.w,p[1]];}
  function rank(){var q=tr(s.q);return PT.map(function(p,i){return [i,SP.dist(tr(p),q)];}).sort(function(a,b){return a[1]-b[1];});}
  var g1=V($('#shop_g1'),function(){var r=rank(),z=s.m==='z',P=z?SP.Plane($('#shop_g1'),{xr:[-3,3],yr:[-3,3],free:true,xl:'나이 (표준화 × 중요도)',yl:'구매액 (표준화)'}):SP.Plane($('#shop_g1'),{xr:[15,65],yr:[50,480],free:true,step:5,lstep:10,ystep:50,ylstep:100,xl:'나이 (세)',yl:'구매액 (천 원)'});
    var f=function(p){return z?tr(p):p;};PT.forEach(function(p,i){var q=f(p),top=i===r[0][0];SP.dot(P,q[0],q[1],top?U.cssv('--eye'):U.cssv('--terrain'),top?8:5,CU[i][0],8,-10);});var Q=f(s.q);SP.dot(P,Q[0],Q[1],U.cssv('--amber'),8,'새 손님',8,16);var b=f(PT[r[0][0]]);SP.seg(P,Q,b,U.cssv('--eye'),2,[5,4]);});
  var g2=V($('#shop_g2'),function(){var r=rank(),mx=r[r.length-1][1]*1.05;bars($('#shop_g2'),r.map(function(x,k){return [CU[x[0]][0],x[1],k===0?U.cssv('--eye'):U.cssv('--terrain'),fmt(x[1],2)];}),{max:mx});});
  function up(){var r=rank(),b=CU[r[0][0]],da=Math.abs(b[1]-s.q[0]);$('#shop_a').textContent=b[0]+' ('+b[1]+'세, '+b[2]+')';$('#shop_b').textContent=CU[r[1][0]][0]+' · '+CU[r[2][0]][0];$('#shop_c').textContent=da+'살';$('#shop_d').textContent=Math.abs(b[2]-s.q[1])+'천 원';
    talk('shop',[['doc',da<=5?'doc_judge':'doc_think',da<=5?'1위 '+b[0]+'는 나이도 구매액도 비슷합니다. 이 쿠폰은 그럴듯해요.':'1위 '+b[0]+'와 나이가 '+da+'살 차이입니다. 이 결과, 그대로 믿어도 될까요? 자를 확인해 보세요.'],
      ['asst','asst_report',(s.m==='z'?'표준화 자':'원래 단위')+', 나이 중요도 '+fmt(s.w,1)+'배로 잰 순위예요.'],['fly','fly_magnify',s.m==='raw'?'구매액 숫자가 수백이야. 나이 차이는 거의 안 들리겠는데?':'중요도를 바꾸면 무엇을 중시하는지가 바뀌어. 업무 판단이지 정답은 아니야.'],
      ['robo',s.m==='raw'?'robo_coin':'robo_smile',s.m==='raw'?'피타고라스로 바로 계산! 1위 '+b[0]+'!':'표준화하니 나이와 구매액이 공평하게 들리네요.']]);
    if(s.t){if(s.q[0]===30&&s.q[1]===200&&b[0]==='A')M[0]=1;if(s.q[0]===30&&s.q[1]===200&&s.m==='raw'&&s.w===1&&b[0]==='B')M[1]=1;
      if(s.q[0]===42&&s.q[1]===330&&s.m==='z'&&b[0]==='D'){if(s.w===1)m3.w1=1;if(s.w>=2)m3.w2=1;}if(m3.w1&&m3.w2)M[2]=1;}
    M.forEach(function(v,k){mis('shop',k,v);});g1.dirty=true;g2.dirty=true;}
  [['shop_age',0,function(v){return v+'세';}],['shop_buy',1,function(v){return v+'천 원';}]].forEach(function(z){var r=$('#'+z[0]);r.addEventListener('input',function(){s.q[z[1]]=+r.value;$('#'+z[0]+'v').textContent=z[2](+r.value);s.t=true;up();});});
  $('#shop_w').addEventListener('input',function(){s.w=+this.value;$('#shop_wv').textContent=fmt(s.w,1)+'배';s.t=true;up();});
  $$('[data-sm]').forEach(function(b){b.onclick=function(){s.m=b.dataset.sm;$$('[data-sm]').forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});s.t=true;up();};});up();
  window.SHOP={s:s,up:up,M:M};})();
tabs();U.start();
'''

CSS = '''
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin:14px 0;border-bottom:2px solid var(--rule)}
.tabs button{font:inherit;font-size:15px;border:1px solid var(--rule);border-bottom:0;background:var(--panel);border-radius:10px 10px 0 0;padding:6px 14px;cursor:pointer}
.tabs button[aria-selected="true"]{background:var(--terrain);color:#fff;border-color:var(--terrain);font-weight:700}
.sit{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--info);border-radius:10px;padding:12px 16px;margin:10px 0}
.board{flex-direction:column;align-items:stretch;gap:8px}.board .group{padding:8px 12px;border-radius:10px}
.board .env{background:#eef8f0;border:1px solid #bfe0c8}.board .dec{background:var(--info-soft);border:1px solid #c3d3f1}
.gtag{font-size:12.5px;font-weight:700;border-radius:6px;padding:1px 8px;color:#fff;margin-right:6px}.gtag.env{background:var(--gfp)}.gtag.dec{background:var(--info)}
.missions ol{display:flex;flex-direction:column;gap:6px;padding-left:22px}.missions li.ok{color:var(--gfp)}.missions li.ok b{color:var(--gfp)}.mst{font-weight:700}
.back{font-size:15px;color:var(--muted)}.sub{font-size:14px;color:var(--muted);font-weight:500}
'''

def build():
    CAST = '<div class="cover" id="cover"><div class="frame"><canvas id="cvCover" aria-hidden="true"></canvas><span class="cap">좌표 첫걸음 · 마지막 장</span><span class="badge">임시 표지 · 픽셀 표지 준비 중</span><div class="cast4">' + \
        ''.join(f'<img src="" data-mood="{k}" alt="" aria-hidden="true">' for k in ['fly_point', 'doc_board', 'asst_smile', 'robo_calc', 'sia_explain', 'moa_report']) + \
        '</div><span class="cover-chip">마지막 장 · 실전 연습장 — 네 현장 운영하기</span></div></div>'
    T = '좌표 첫걸음 마지막 장 · 실전 연습장 — 네 현장 운영하기 | 나는 어디에 있는가?'
    D = '좌표 첫걸음 마지막 장. 지구 배송센터·관제탑·물류창고·추천 매장 네 현장을 직접 운영하며 위도·경도, 극좌표, 공간좌표, 특성 공간과 표준화를 한 번에 복습하는 시뮬레이터 대시보드.'
    H = f'''<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(T)}</title><meta name="description" content="{esc(D)}">
<meta property="og:type" content="article"><meta property="og:title" content="{esc(T)}"><meta property="og:description" content="{esc(D)}"><meta property="og:image" content="{SITE}img/og/practice.png"><meta property="og:url" content="{SITE}practice/index.html"><meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<!--@@CSS@@-->
<style>{EXTRA_CSS}{CSS}</style></head>
<body>
<nav class="top" aria-label="섹션 바로가기"><div class="row"><a class="logo" href="index.html">좌표 <i>첫걸음</i> 연습장</a><div class="links"><a href="#ship">① 배송센터</a><a href="#radar">② 관제탑</a><a href="#ware">③ 물류창고</a><a href="#shop">④ 추천 매장</a><a href="#wrap">마무리</a><a href="#kg">색인</a><a href="#export">꾸러미</a></div></div></nav>
{CAST}
<header class="hero" id="top"><div class="wrap">
<div class="eyebrow">좌표 첫걸음 · 마지막 장 · 최적화 첫걸음의 자매편 <span class="diff">난이도: 오르막</span></div>
<h1>마지막 장 · 실전 연습장 — 네 현장 운영하기</h1>
<p class="question">배운 좌표로 실제 현장을 굴려 보면 어디서 실수가 날까?</p>
<p class="lead">1~6장에서 배운 자들을 네 현장에서 씁니다. 장면마다 <b>초록 조작판</b>은 현장 조건, <b>파랑 조작판</b>은 내 결정이에요. 성적표·그래프·연구실 식구의 말이 내 결정에 따라 바로 바뀌고, 미션 세 개는 조건을 맞추면 저절로 통과 표시가 켜집니다. 주소 끝에 <code>#radar</code>처럼 장면 이름을 붙이면 그 장면이 바로 열려요.</p>
<p class="byline">{AUTHOR} · {DATE} · {VER}</p>
<div class="start"><b>처음이라면</b> ① → ② → ③ → ④ 순서로 해 보세요. 막히면 장면 아래 "배운 곳 다시 보기" 링크로 돌아가면 됩니다. 기록은 이 탭에만 남고 저장하지 않습니다.</div>
</div></header>
<main><section class="sec" aria-label="실전 연습장"><div class="wrap">
<div class="tabs" role="tablist"><button role="tab" type="button" id="tab-ship" data-t="ship" aria-controls="ship">① 지구 배송센터</button><button role="tab" type="button" id="tab-radar" data-t="radar" aria-controls="radar">② 관제탑</button><button role="tab" type="button" id="tab-ware" data-t="ware" aria-controls="ware">③ 물류창고</button><button role="tab" type="button" id="tab-shop" data-t="shop" aria-controls="shop">④ 추천 매장</button></div>
{S1}{S2}{S3}{S4}
</div></section>
<section class="sec" id="wrap"><div class="wrap"><h2>마무리 — 네 현장이 함께 묻는 질문</h2>
<p>배송센터는 "경도 1도는 어디서나 같다", 관제탑은 "각도는 4 ÷ 3에서 바로 나온다", 물류창고는 "거리는 숫자를 더하면 된다", 추천 매장은 "피타고라스면 다 된다"는 생각에서 실수가 났습니다. 네 실수의 공통점은 하나예요. <b>숫자를 받으면 어떤 자(기준점·방향·눈금·단위)로 잰 숫자인지 먼저 묻는다.</b> 이것이 "나는 어디에 있는가?"에 제대로 답하는 법이고, 다음 질문 "어디로 가야 하나?"(자매편 <a href="https://adminmrobo.github.io/optimization_3d_map/first_step_0.html">최적화 첫걸음</a>)의 출발점입니다.</p>
<div class="lim"><b>모형의 한계</b> 지구는 완전한 공, 드론은 바람·고도 없이 위선을 따라 난다고 봤습니다. 고객 열 명과 배터리 여유 기준(10~30%)은 설명용 예시이며, 숫자는 교육용입니다. 경영·투자 권고가 아닙니다.</div>
<div class="next"><a href="index.html"><b>목차</b></a><a href="06_data_space.html"><b>← 6장 데이터의 좌표</b></a><a href="https://adminmrobo.github.io/optimization_3d_map/first_step_0.html"><b>자매편 최적화 첫걸음 →</b></a></div>
</div></section></main>
<footer><div class="wrap"><h3>출처</h3><p>이 페이지의 장면은 좌표 첫걸음 1~6장과 그 바탕이 된 연구실 콘텐츠(자와 각도기의 방, 벡터 분석 랩, 벡터 DB 연구실)를 다시 쓴 것입니다.</p>
<p>캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다.</p><p>{AUTHOR} · <a href="index.html">좌표 첫걸음 목차</a></p></div></footer>
<script>
/*@@SPRITES@@*/
/*@@COMMON@@*/
/*@@SPACE@@*/
(function(){{'use strict';
U.fillImgs();SP.drawCover(U.$('#cvCover'),'plane');
{JS}
}})();
</script></body></html>'''
    open(os.path.join(B, 'practice.src.html'), 'w').write(H)

KG = dict(
 nodes=[('Simulation', 'ship-scene', '지구 배송센터 장면', 'Global delivery scene', '#ship', '위도에 따른 경도 1도 길이로 배터리를 고르는 시뮬레이터.'),
        ('Simulation', 'radar-scene', '관제탑 장면', 'Radar scene', '#radar', '(x, y) 표적을 (r, θ)로 통역해 요격하는 시뮬레이터.'),
        ('Simulation', 'ware-scene', '물류창고 장면', 'Warehouse scene', '#ware', '원통·지구본 자 주소를 모눈 자로 바꾸는 시뮬레이터.'),
        ('Simulation', 'shop-scene', '추천 매장 장면', 'Recommendation scene', '#shop', '자와 중요도에 따라 바뀌는 가장 닮은 고객 시뮬레이터.'),
        ('Concept', 'which-ruler', '어떤 자로 잰 숫자인가', 'Which ruler?', '#wrap', '숫자를 받으면 기준점·방향·눈금·단위를 먼저 확인하는 습관.'),
        ('Limitation', 'toy-model', '교육용 단순 모형', 'Toy model', '#wrap', '완전한 공 지구, 바람 없는 드론, 고객 열 명.')],
 edges=[('which-ruler', 'demonstratedBy', 'ship-scene', '#ship'), ('which-ruler', 'demonstratedBy', 'radar-scene', '#radar'), ('which-ruler', 'demonstratedBy', 'ware-scene', '#ware'), ('which-ruler', 'demonstratedBy', 'shop-scene', '#shop'), ('which-ruler', 'hasLimitation', 'toy-model', '#wrap')])
PAGE = dict(out='practice/index.html', title='좌표 첫걸음 마지막 장 · 실전 연습장 — 네 현장 운영하기')

if __name__ == '__main__':
    build(); print('src practice')
