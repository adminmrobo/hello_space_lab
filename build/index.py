# -*- coding: utf-8 -*-
"""목차 — 나는 어디에 있는가? 좌표계로 본 매핑 (좌표 첫걸음)"""
import os
from gen import EXTRA_CSS, AUTHOR, DATE, VER, SITE, esc, B, CAST

CH = [('01_number_line.html', '1장', '수직선 — 숫자 하나로 말하는 자리', '기준점·방향·눈금. 길 위의 원점, 0층 없는 엘리베이터, 섭씨·화씨, 표준화 자.', '자 통역사', '산책', 'line'),
      ('02_plane.html', '2장', '좌표평면 — 두 숫자로 찍는 점', '좌석표로 배우는 순서쌍, 직선 거리 5와 골목 거리 7, 점은 자리 화살표는 이동.', '거리만 알려 주는 보물찾기 (GPS)', '산책', 'plane'),
      ('03_polar.html', '3장', '극좌표 — 거리와 방향으로 찍는 점', '(3, 4) = (5, 53.1°), 같은 각도 다른 피자 테두리, 12월과 1월을 이웃으로.', '레이더 관제실', '오르막', 'polar'),
      ('04_space.html', '4장', '공간좌표 — 높이가 생기면 세 숫자', '그림자 + 높이, 공간 거리 (2, 3, 6) → 7, 같은 점을 모눈·원통·지구본 자로.', '드론 배송', '오르막', 'space'),
      ('05_earth_map.html', '5장', '지구 위의 좌표 — 위도·경도와 지도 그리기', '반지름을 고정한 지구본 자, 경도 1도 111.2 km × cos(위도), 메르카토르의 대가.', '지구 배송센터', '오르막', 'globe'),
      ('06_data_space.html', '6장', '데이터의 좌표 — 표 한 줄이 점 하나가 될 때', '특성 공간, 표준화 후 거리, n차원, 좌표 위에 오차를 세워 최적화로.', '쿠폰 담당자 (가장 가까운 이웃)', '오르막', 'data'),
      ('practice/index.html', '마지막 장', '실전 연습장 — 네 현장 운영하기', '배송센터·관제탑·물류창고·추천 매장. 조작판·성적표·미션으로 1~6장 복습.', '시뮬레이터 대시보드 4종', '오르막', 'plane')]

SRC = [('자와 각도기의 방 — 유클리드 공간', 'https://adminmrobo.github.io/euclidean_space_lab/', '모눈·자·각도기·화살표 (1·2·4장)'),
       ('벡터 분석 랩 — 네 개의 자', 'https://adminmrobo.github.io/vector_analysis_lab/', '네 가지 자, 피자, 12월과 1월, 경도 1도, 그린란드 (3·4·5장)'),
       ('좌표축 위의 그릇 · 최적화 첫걸음', 'https://adminmrobo.github.io/optimization_3d_map/', '3D 지형, 오차를 높이로 (4·6장, 자매편)'),
       ('머신러닝 모델 도감', 'https://adminmrobo.github.io/machine_learning_model_atlas/', '같은 모눈 위의 데이터 (6장)'),
       ('벡터 DB 연구실', 'https://adminmrobo.github.io/vector_db_lab/', '임베딩, 고차원 점 사이 거리 (6장)'),
       ('텐서 연구실', 'https://adminmrobo.github.io/what_is_tensor/', '숫자 묶음과 축 (6장)'),
       ('우연의 과학통계학', 'https://adminmrobo.github.io/statistics_note/', '표준화 점수 (1·6장)')]

def build():
    cards = ''.join(f'''<a class="ccard" href="{h}"><canvas class="cmini" data-motif="{m}" aria-hidden="true"></canvas><div><span class="cno">{n}</span> <span class="diff">{d}</span><h3>{t}</h3><p>{s}</p><p class="cgame"><b>부록</b> {g}</p></div></a>''' for h, n, t, s, g, d, m in CH)
    cast = ''.join(f'<div class="castc" style="--cc:var(--c-{("x" if k.startswith("x") else k)})"><img data-mood="{m}" alt="" aria-hidden="true"><div><b>{n}</b><p>{d}</p></div></div>' for k, m, n, d in CAST)
    src = ''.join(f'<tr><td><a href="{u}">{t}</a></td><td>{w}</td></tr>' for t, u, w in SRC)
    T = '나는 어디에 있는가? — 좌표계로 본 매핑 | 좌표 첫걸음 (최적화 첫걸음의 자매편)'
    D = '좌표 첫걸음. 박사가 강의하고 조교 하루·초파리·주판봇이 돕고, 시아·모아·X1~X3가 듣는 강의실에서 수직선 → 좌표평면 → 극좌표 → 공간좌표 → 위도·경도와 지도 → 데이터의 좌표까지, 장마다 게임 부록과 마지막 실전 연습장으로 배우는 친절한 좌표 안내서.'
    H = f'''<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(T)}</title><meta name="description" content="{esc(D)}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(T)}"><meta property="og:description" content="{esc(D)}"><meta property="og:image" content="{SITE}img/og/index.png"><meta property="og:url" content="{SITE}"><meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<!--@@CSS@@-->
<style>{EXTRA_CSS}
.cgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;margin:16px 0}}
.ccard{{display:flex;flex-direction:column;background:var(--panel);border:1px solid var(--rule);border-radius:14px;overflow:hidden;text-decoration:none;color:var(--text)}}
.ccard:hover{{border-color:var(--terrain)}}.ccard>div{{padding:12px 16px}}.ccard h3{{margin:4px 0 6px;font-size:18px}}.ccard p{{margin:0 0 6px;font-size:14.5px;color:var(--muted)}}
.cmini{{width:100%;height:150px;display:block;border-bottom:1px solid var(--rule)}}.cno{{font-weight:700;color:var(--terrain)}}.cgame b{{color:var(--c-asst)}}
.sister{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0}}.sister>div{{border:1px solid var(--rule);border-radius:12px;padding:14px 18px;background:var(--panel)}}.sister b.q{{display:block;font-size:20px;color:var(--terrain)}}
@media(max-width:760px){{.sister{{grid-template-columns:1fr}}}}
</style></head>
<body>
<nav class="top" aria-label="섹션 바로가기"><div class="row"><a class="logo" href="index.html">좌표 <i>첫걸음</i></a><div class="links"><a href="#plan">강의 계획</a><a href="#class">강의실</a><a href="#sister">자매편</a><a href="#source">바탕 콘텐츠</a><a href="#kg">색인</a><a href="#export">꾸러미</a><a href="01_number_line.html">1장 →</a></div></div></nav>
<div class="cover" id="cover"><div class="frame"><img class="art" src="img/cover_index.webp" width="1920" height="1080" alt="흰 강의실. 칠판에 수직선·모눈과 빨간 핀·동심원·3차원 축·지구본·점 구름이 화살표로 이어져 있고, 박사가 빨간 핀을 가리킨다. 조교 하루·초파리 연구원·주판봇과 수강생 시아·모아·X1~X3." fetchpriority="high"><span class="cap">좌표 첫걸음 · 강의실 안내</span><span class="cover-chip">나는 어디에 있는가? — 좌표계로 본 매핑</span></div></div>
<header class="hero" id="top"><div class="wrap">
<div class="eyebrow">좌표 첫걸음 · 최적화 첫걸음의 자매편 · 연구실 강의 시리즈</div>
<h1>나는 어디에 있는가? — 좌표계로 본 매핑</h1>
<p class="question">지도 앱의 파란 점부터 AI의 데이터 공간까지, "자리"는 어떻게 숫자가 될까?</p>
<p class="lead">이 강의는 연구실이 그동안 만든 공간·벡터·지도·데이터 콘텐츠에서 <b>기본이 되는 좌표계만</b> 골라, 처음 오신 분이 차례로 따라올 수 있게 다시 쓴 안내서입니다. 수직선 하나에서 시작해 숫자가 둘, 셋으로 늘고, 거리·각도로 바꿔 부르고, 지구를 지도로 옮기고, 마지막에는 표 한 줄을 공간의 점으로 놓습니다. 장마다 직접 움직이는 실험과 <b>부록 게임</b>이 있고, 맨 끝 <b>실전 연습장</b>에서 네 현장을 운영하며 복습합니다.</p>
<p class="byline">{AUTHOR} · {DATE} · {VER}</p>
<div class="start"><b>처음이라면</b> 1장에서 시작해 순서대로 보세요. 한 장은 30~40분 강의 분량입니다. 코드와 수식을 몰라도 됩니다. 식이 나오면 수강생이 묻고 조교 하루가 숫자 하나로 풀어 줍니다.</div>
<div class="kpis"><div class="kpi m"><b>6장 + 1</b><span>강의 여섯 장과 마지막 실전 연습장</span></div><div class="kpi g"><b>6개</b><span>장마다 하나씩 있는 부록 게임</span></div><div class="kpi a"><b>4곳</b><span>실전 연습장의 현장 (미션 12개)</span></div><div class="kpi r"><b>7편</b><span>다시 쓴 연구실 콘텐츠</span></div></div>
</div></header>
<main>
<section class="sec" id="plan"><div class="wrap"><h2><span class="hex">계획</span>강의 계획표</h2>
<div class="chain"><span>수직선 (숫자 1개)</span><i>→</i><span>좌표평면 (2개)</span><i>→</i><span>극좌표 (거리·각도)</span><i>→</i><span>공간좌표 (3개)</span><i>→</i><span>위도·경도와 지도</span><i>→</i><span>데이터의 좌표 (n개)</span><i>→</i><span>최적화 첫걸음</span></div>
<p>앞 장의 한계가 다음 장의 이유가 되도록 이었습니다. 숫자 하나로 모자라 둘이 되고(1→2), 둥근 것을 다루려고 거리·각도로 바꾸고(2→3), 높이가 생겨 셋이 되고(3→4), 지구 표면에서는 다시 둘이 되고(4→5), 장소가 아닌 데이터에도 자리를 붙입니다(5→6).</p>
<div class="cgrid">{cards}</div></div></section>
<section class="sec" id="class"><div class="wrap"><h2><span class="hex">강의실</span>강의실 사람들</h2>
<p>박사가 강의하고, 조교 셋이 돕고, 수강생 다섯이 듣습니다. 시아·모아는 질문을, X1~X3는 뒷줄에서 반응을 맡아요. 조교 주판봇은 1초 만에 답을 내지만 가끔 너무 빨라서, 장마다 한 번 <b>AI 판단 코너</b>에서 "이 답 믿어도 될까?"를 함께 따져 봅니다.</p>
<div class="cast" style="grid-template-columns:repeat(auto-fit,minmax(230px,1fr))">{cast}</div></div></section>
<section class="sec" id="sister"><div class="wrap"><h2><span class="hex">자매편</span>최적화 첫걸음과 함께 보기</h2>
<div class="sister"><div><b class="q">나는 어디에 있는가?</b><p>좌표 첫걸음 (이 시리즈) — 자리를 숫자로 적고, 거리를 재고, 자를 바꿔 부르는 법.</p></div><div><b class="q">어디로 가야 하나?</b><p><a href="https://adminmrobo.github.io/optimization_3d_map/first_step_0.html">최적화 첫걸음</a> — 좌표 위에 오차를 세우고 내리막으로 걷는 법. 미분부터 경사하강까지.</p></div></div>
<p>6장의 마지막 단계(6.4)에서 두 시리즈가 만납니다. 좌표 첫걸음을 먼저 보면 최적화 첫걸음의 "가중치를 좌표축으로, 오차를 높이로"가 자연스럽게 읽힙니다.</p></div></section>
<section class="sec" id="source"><div class="wrap"><h2><span class="hex">바탕</span>이 강의가 다시 쓴 연구실 콘텐츠</h2>
<p>좌표 첫걸음은 이미 만든 연구실 콘텐츠를 입문자용으로 다시 엮은 것입니다. 각 장 끝 출처 표에 어느 단계가 어느 콘텐츠에서 왔는지 적었습니다. 더 깊이 보고 싶으면 원래 콘텐츠로 가세요.</p>
<div class="tblwrap"><table class="cmp"><thead><tr><th>연구실 콘텐츠</th><th>좌표 첫걸음에서 쓴 곳</th></tr></thead><tbody>{src}</tbody></table></div>
<p class="muted" style="font-size:14px">더 넓은 공간(끝없는 방의 힐베르트 공간, 시간이 들어간 민코프스키 시공간)은 기본 좌표계를 넘어서므로 이 강의에서는 다루지 않았습니다 → <a href="https://adminmrobo.github.io/hilbert_space_lab/">힐베르트 공간</a>, <a href="https://adminmrobo.github.io/minkowski_space_lab/">민코프스키 시공간</a></p>
</div></section>
</main>
<footer><div class="wrap"><p>캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다.</p><p>{AUTHOR}</p></div></footer>
<script>
/*@@SPRITES@@*/
/*@@COMMON@@*/
/*@@SPACE@@*/
(function(){{'use strict';U.fillImgs();SP.drawCover(U.$('#cvCover'),'plane');U.$$('canvas.cmini').forEach(function(c){{SP.drawCover(c,c.dataset.motif);}});U.start();}})();
</script></body></html>'''
    open(os.path.join(B, 'index.src.html'), 'w').write(H)

PAGE = dict(out='index.html', title='나는 어디에 있는가? — 좌표계로 본 매핑 (좌표 첫걸음 목차)')
KG = dict(
 nodes=[('Concept', 'coordinate-system', '좌표계', 'Coordinate system', '#plan', '자리를 숫자로 적는 약속: 기준점·방향·눈금.'),
        ('Concept', 'mapping', '매핑', 'Mapping', '#plan', '한 공간의 자리를 다른 공간(지도·데이터 공간)의 자리로 옮기는 일.'),
        ('Concept', 'series-number-line', '수직선', 'Number line', '#plan', '1장.'), ('Concept', 'series-plane', '좌표평면', 'Coordinate plane', '#plan', '2장.'),
        ('Concept', 'series-polar', '극좌표', 'Polar coordinates', '#plan', '3장.'), ('Concept', 'series-space', '공간좌표', '3D coordinates', '#plan', '4장.'),
        ('Concept', 'series-geo', '위도·경도와 지도', 'Geographic coordinates and maps', '#plan', '5장.'), ('Concept', 'series-feature', '특성 공간', 'Feature space', '#plan', '6장.'),
        ('Question', 'where-am-i', '나는 어디에 있는가?', 'Where am I?', '#top', '이 시리즈의 질문.'), ('Question', 'where-to-go', '어디로 가야 하나?', 'Where to go?', '#sister', '자매편 최적화 첫걸음의 질문.')],
 edges=[('series-number-line', 'prerequisiteOf', 'series-plane', '#plan'), ('series-plane', 'prerequisiteOf', 'series-polar', '#plan'), ('series-polar', 'prerequisiteOf', 'series-space', '#plan'),
        ('series-space', 'prerequisiteOf', 'series-geo', '#plan'), ('series-geo', 'prerequisiteOf', 'series-feature', '#plan'), ('coordinate-system', 'relatedTo', 'where-am-i', '#top'),
        ('mapping', 'relatedTo', 'series-geo', '#plan'), ('series-feature', 'prerequisiteOf', 'where-to-go', '#sister')])

if __name__ == '__main__':
    build(); print('src index')
