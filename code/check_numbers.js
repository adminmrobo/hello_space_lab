// 페이지에 적은 "숫자로 한 번 해 보기"·게임 정답을 다시 계산한다: node code/check_numbers.js
const SP=require('../build/space.js');let bad=0;
function eq(name,got,want,tol){const ok=Math.abs(got-want)<=(tol==null?0.005:tol);if(!ok)bad++;console.log((ok?'OK ':'BAD')+' '+name+' = '+(+got.toFixed(4))+' (기대 '+want+')');}
// 1장
eq('1.1 집–학교 거리',Math.abs(400-0),400);eq('1.2 B2→5층 실제 층 수',(5-1)-(-2),6);eq('1.2 높이',6*3.5,21);
eq('1.3 86°F → °C',SP.fToC(86),30);eq('1.3 25°C → °F',SP.cToF(25),77);eq('1.3 10°C 차이 → °F',SP.cToF(30)-SP.cToF(20),18);
eq('부록 표준화 170',SP.zscore(170,160,5),2);eq('부록 편의점(학교 기준)',150-400,-250);eq('퀴즈 50°F',SP.fToC(50),10);
// 2장
eq('2.2 시아–모아',SP.dist([2,1],[5,5]),5);eq('2.2 골목',SP.taxi([2,1],[5,5]),7);eq('키·몸무게',SP.dist([160,50],[163,54]),5);
eq('퀴즈 (6,8)',SP.dist([0,0],[6,8]),10);
for(const t of [[-2,-2],[5,5],[1,-3]])eq('GPS 탑 '+t+' → (1,2)',SP.dist(t,[1,2]),5);
// 3장
const p=SP.toPolar(3,4);eq('3.1 r',p[0],5);eq('3.1 θ',p[1],53.13,0.01);
eq('3.2 피자 10',SP.arc(10,45),7.85,0.005);eq('3.2 피자 15',SP.arc(15,45),11.78,0.005);eq('퀴즈 피자 20 90°',SP.arc(20,90),31.42,0.01);
eq('3.3 12월–1월',SP.monthChord(12,1),0.52,0.005);eq('3.3 12월–6월',SP.monthChord(12,6),2);
for(const t of [[3,4],[-4,4],[0,-6],[-5,-1]]){const q=SP.toPolar(...t);console.log('   레이더 표적',t,'→ r',q[0].toFixed(2),'θ',q[1].toFixed(1));}
// 4장
eq('4.2 (2,3,6)',SP.dist([0,0,0],[2,3,6]),7);eq('4.2 바닥 대각선',Math.hypot(2,3),3.61,0.005);
const s=SP.sph(1,1,Math.SQRT2);eq('4.3 r',s[0],2);eq('4.3 θ',s[1],45);eq('4.3 ρ',SP.cyl(1,1,Math.SQRT2)[0],1.41,0.005);
eq('부록 원통 → x',SP.fromCyl(5,36.8699,2)[0],4,0.001);eq('부록 원통 → y',SP.fromCyl(5,36.8699,2)[1],3,0.001);
const f=SP.fromSph(3,48.1897,63.4349);eq('부록 지구본 x',f[0],1,0.001);eq('부록 지구본 y',f[1],2,0.001);eq('부록 지구본 z',f[2],2,0.001);
eq('퀴즈 (1,2,2)',SP.dist([0,0,0],[1,2,2]),3);
// 5장
eq('5.2 적도',SP.lonKm(0),111.2,0.05);eq('5.2 37.5°',SP.lonKm(37.5),88.2,0.05);eq('5.2 60°',SP.lonKm(60),55.6,0.05);
eq('5.3 72° 넓이',SP.mercArea(72),10.47,0.01);eq('5.3 60° 넓이',SP.mercArea(60),4,0.001);eq('5.3 72° 가로',SP.mercLen(72),3.24,0.005);
eq('아프리카/그린란드',30.37/2.166,14,0.1);eq('서울 z km',6371*Math.sin(37.6*Math.PI/180),3887,1.5);
eq('부록 적도 10°',SP.lonKm(0)*10,1112,0.5);eq('퀴즈 60° 2°',SP.lonKm(60)*2,111.2,0.1);
// 6장
const C=[[31,260],[52,205],[25,120],[45,380],[35,450],[58,150],[28,300],[40,90],[23,240],[50,320]],N='ABCDEFGHIJ';
const sd=[SP.sd(C.map(c=>c[0])),SP.sd(C.map(c=>c[1]))];
const want=[[[30,200],null,'B'],[[30,200],sd,'A'],[[42,330],sd,'D'],[[55,170],null,'F'],[[55,170],sd,'F'],[[42,330],null,'J']];
for(const [q,sc,w] of want){const r=N[SP.nearest(C,q,sc)[0]];const ok=r===w;if(!ok)bad++;console.log((ok?'OK ':'BAD')+' 가장 가까운 이웃 '+q+' '+(sc?'표준화':'원래 단위')+' → '+r+' (기대 '+w+')');}
eq('6.2 키 m',SP.dist([1.60,50],[1.63,54]),4.0001,0.0001);eq('6.3 네 축',Math.sqrt(1+4+4+16),5);eq('6.4 오차',0.5*4+6.25,8.25);
// 연습장: 나이 중요도 2에서도 D
const w2=C.map(c=>[c[0]/sd[0]*2,c[1]/sd[1]]),q2=[42/sd[0]*2,330/sd[1]];const r2=N[SP.nearest(w2,q2)[0]];if(r2!=='D')bad++;console.log((r2==='D'?'OK ':'BAD')+' 연습장 중요도 2 → '+r2);
console.log(bad?'틀린 값 '+bad+'개':'모든 값 검산 통과');process.exit(bad?1:0);
