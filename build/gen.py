# -*- coding: utf-8 -*-
"""좌표 첫걸음 — 페이지 원본(*.src.html) 생성기.
장마다 build/ch_*.py가 PAGE 사전을 내고, 이 파일이 같은 틀(표지·히어로·3줄 상자·등장인물·단계·부록·정리·아웃트로·바닥글)로 엮는다.
그다음 node build/build.js가 CSS·캐릭터·모듈·지식 색인을 붙여 완성 HTML을 만든다."""
import json, os, importlib, sys
B = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://adminmrobo.github.io/hello_space_lab/'
AUTHOR = '글 · 안상선 ((주)M-Robo 대표) · <a href="https://adminmrobo.github.io/who_am_i/who_am_i.html">저자 소개</a>'
SERIES = '좌표 첫걸음'
DATE = '2026-11-23'
VER = 'v1.0'

ASK_NAME = {'sia': '시아', 'moa': '모아', 'x1': 'X1', 'x2': 'X2', 'x3': 'X3'}
ASK_MOOD = {'sia': 'sia_think', 'moa': 'moa_report', 'x1': 'x1_hint', 'x2': 'x2_hint', 'x3': 'x3_hint'}

CAST = [
    ('doc', 'doc_board', '박사', '강의를 맡은 연구실 선생님. 장마다 상황 질문으로 문을 열고 해석 문장으로 닫아요.'),
    ('asst', 'asst_smile', '조교 하루', '수식 담당 조교. 시아·모아의 질문을 받아 학교 수학과 숫자 하나로 풀어 줘요.'),
    ('fly', 'fly_point', '조교 초파리', '실험 담당 조교. "이걸 눌러 봐"로 실험판을 열고, 답이 그럴듯한지 의심해요.'),
    ('robo', 'robo_calc', '조교 주판봇', '계산 담당 조교. 1초 만에 답을 내지만 가끔 너무 빨라요. AI 판단 코너의 주인공.'),
    ('sia', 'sia_smile', '수강생 시아', '직관파. 비유부터 꺼내 "그러니까 이런 거죠?"라고 묻는 앞줄 수강생.'),
    ('moa', 'moa_smile', '수강생 모아', '꼼꼼파. "그건 언제나 그래요?" 하고 조건과 예외를 묻는 수강생. 차를 준비해 와요.'),
    ('x1', 'x1_hint', 'X1', '뒷줄 수강생. 손을 들 때가 가끔 있어요.'),
    ('x2', 'x2_hint', 'X2', '뒷줄 수강생. 필기를 가장 열심히 해요.'),
    ('x3', 'x3_hint', 'X3', '뒷줄 수강생. 게임 시간에 가장 신나요.'),
]

def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def why_box(w):
    return ('<details class="ez-why" open><summary>왜 이 방법을 쓰나</summary><ol>'
            f'<li>문제: {w["problem"]}</li><li>앞 방법의 한계: {w["limit"]}</li><li><b>이 방법의 해법: {w["solve"]}</b></li></ol>'
            f'<p class="ez-easy"><b>쉽게 말하면</b> {w["easy"]}</p></details>')

def math_box(m):
    who = m.get('who', 'sia')
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in m['rows'])
    tries = ''.join(f'<li>{t}</li>' for t in m['tries'])
    return ('<div class="ez-math"><div class="ez-t">시아·모아가 묻고, 조교 하루가 풀어 봅니다</div>'
            f'<div class="ez-q"><img data-mood="{ASK_MOOD[who]}" alt="" aria-hidden="true"><p><b style="display:block;font-size:12.5px;color:var(--muted)">{ASK_NAME[who]}</b>{m["q"]}</p></div>'
            f'<p><b>말로 먼저</b> {m["words"]}</p>'
            f'<p><b>학교 수학으로 보면</b> {m["school"]}</p>'
            f'<div class="try" style="background:#fff;border:1px dashed #e8b67a;border-radius:10px;padding:10px 14px"><b>숫자로 한 번 해 보기</b><ol style="margin:6px 0 0;padding-left:22px">{tries}</ol></div>'
            '<details class="eqx"><summary>식으로 보면 (몰라도 됩니다)</summary>'
            f'<table class="ez-tb"><thead><tr><th>식 조각</th><th>읽는 법</th><th>뜻</th></tr></thead><tbody>{rows}</tbody></table></details>'
            f'<div class="ez-q ez-c"><img data-mood="{m.get("cmood","asst_spark")}" alt="" aria-hidden="true"><p><b style="display:block;font-size:12.5px;color:var(--muted)">조교 하루</b>{m["comment"]}</p></div></div>')

def ai_box(a):
    qs = ''.join(f'<li>{q}</li>' for q in a['checks'])
    return (f'<div class="aibox" id="{a["id"]}"><div class="aihead"><span class="aitag">AI 판단 코너</span>{a["title"]}</div>'
            f'<div data-dlg="{a["id"]}_d"></div>'
            f'<p>박사는 늘 두 가지를 묻습니다. "가정이 맞나? 숫자가 그럴듯한가?"</p><ol>{qs}</ol>'
            f'<details class="eqx"><summary>확인해 보기 (먼저 스스로 따져 본 뒤 펼치세요)</summary><p class="aiverdict">{a["verdict"]}</p>'
            f'<div data-dlg="{a["id"]}_e"></div></details></div>')

def step(s):
    tags = ''.join(f'<span class="tag">{t}</span>' for t in s['tags'])
    h = [f'<h3 id="{s["id"]}" style="font-size:22px;margin-top:64px">{s["num"]} {s["title"]}</h3>', f'<div class="tags">{tags}</div>']
    if s.get('open'):
        h.append(f'<div data-dlg="{s["id"]}_o"></div>')
    if s.get('review'):
        h.append(f'<div class="review30"><b>30초 복습</b> {s["review"]}</div>')
    if s.get('why') or s.get('math'):
        h.append('<div class="easy">' + (why_box(s['why']) if s.get('why') else '') + (math_box(s['math']) if s.get('math') else '') + '</div>')
    h.append(f'<div class="pair"><div><div class="tl">일상으로 치면</div>{s["daily"]}</div><div><div class="tr">{s.get("fieldname","AI·데이터에서는")}</div>{s["field"]}</div></div>')
    h.append(f'<div class="dialog lvtalk" data-dlg="{s["id"]}_t"></div>')
    h.append(s['panel'])
    if s.get('solve'):
        h.append(f'<div class="explain"><h4>풀이</h4>{s["solve"]}</div>')
    if s.get('doc'):
        h.append(f'<div class="say" data-who="doc"><img class="who" data-mood="doc_judge" alt="" aria-hidden="true"><div><b class="name">박사의 정리</b><p>{s["doc"]}</p></div></div>')
    if s.get('ai'):
        h.append(ai_box(s['ai']))
    if s.get('limit'):
        h.append(f'<div class="lim"><b>이 단계의 한계</b> {s["limit"]}</div>')
    if s.get('code'):
        rows = ''.join(f'<tr><td class="m">{c}</td><td>{m}</td></tr>' for c, m in s['code'])
        h.append(f'<details class="eqx"><summary>파이썬 코드로 보면 (몰라도 됩니다)</summary><table class="ez-tb eqt"><tbody>{rows}</tbody></table></details>')
    h.append(f'<div class="quiz" data-quiz="{s["id"]}"></div>')
    return '\n'.join(h)

def cover(c, key, alt):
    """픽셀 표지(img/cover_{key}.webp, 480×270 격자를 NEAREST 4배로 키운 무손실 WebP)를 얹는다. 캐릭터는 그림 안에 있다."""
    return (f'<div class="cover" id="cover"><div class="frame"><img class="art" src="img/cover_{key}.webp" width="1920" height="1080" alt="{esc(alt)}" fetchpriority="high">'
            f'<span class="cap">{c["cap"]}</span><span class="cover-chip">{c["chip"]}</span></div></div>')

def page(P):
    nav = ''.join(f'<a href="{h}">{t}</a>' for h, t in P['nav'])
    kpis = ''.join(f'<div class="kpi {c}"><b>{v}</b><span>{t}</span></div>' for c, v, t in P['kpis'])
    plain = ''.join(f'<li><b>{a}</b> {b}</li>' for a, b in P['plain'])
    abbr = ''.join(f'<div><b>{a}</b> <span>{b}</span> — {c}</div>' for a, b, c in P['abbr'])
    castkeys = P.get('cast', [c[0] for c in CAST])
    cast = ''.join(f'<div class="castc" style="--cc:var(--c-{("x" if k.startswith("x") else k)})"><img data-mood="{m}" alt="" aria-hidden="true"><div><b>{n}</b><p>{d}</p></div></div>'
                   for k, m, n, d in CAST if k in castkeys)
    steps = '\n'.join(step(s) for s in P['steps'])
    refs = ''.join(f'<tr><td>[{i+1}]</td><td>{a}</td><td>{b}</td></tr>' for i, (a, b) in enumerate(P['refs']))
    ex = ''.join(f'<li>{x}</li>' for x in P['examples'])
    summ = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in P['summary'])
    gloss = ''.join(f'<div><b>{a}</b> = {b}</div>' for a, b in P['cards'])
    lims = ''.join(f'<li>{x}</li>' for x in P['limits'])
    nxt = ''.join(f'<a href="{h}"><b>{t}</b><br>{d}</a>' for h, t, d in P['next'])
    og = SITE + 'img/og/' + P['key'] + '.png'
    H = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(P["title"])}</title>
<meta name="description" content="{esc(P["desc"])}">
<meta property="og:type" content="article"><meta property="og:title" content="{esc(P["title"])}"><meta property="og:description" content="{esc(P["desc"])}">
<meta property="og:image" content="{og}"><meta property="og:url" content="{SITE}{P["out"]}"><meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<!--@@CSS@@-->
<style>{EXTRA_CSS}{P.get("css","")}</style>
</head>
<body>
<nav class="top" aria-label="섹션 바로가기"><div class="row">
  <a class="logo" href="index.html">좌표 <i>첫걸음</i> {P["logo"]}</a>
  <div class="links">{nav}</div>
</div></nav>
{cover(P["cover"], P["key"], P["cover"].get("alt", P["h1"]))}
<header class="hero" id="top"><div class="wrap">
  <div class="eyebrow">{P["eyebrow"]}</div>
  <h1>{P["h1"]}</h1>
  <p class="question">{P["question"]}</p>
  <p class="lead">{P["lead"]}</p>
  <p class="byline">{AUTHOR} · {DATE} · {VER}</p>
  <div class="start"><b>처음이라면</b> {P["start"]}</div>
  <div class="kpis" aria-label="숫자 요약">{kpis}</div>
  <p class="muted" style="font-size:13px">숫자는 이 페이지가 직접 계산한 값이며, 사람·가게·도시 예시는 설명용입니다.</p>
</div></header>
<main>
<section class="sec" id="plain" aria-labelledby="h-plain"><div class="wrap"><h2 id="h-plain">처음 오신 분께 — 이 페이지를 3줄로</h2><ol class="plain3">{plain}</ol>
<p class="plain-note">코드와 수식을 몰라도 됩니다. 식이 나오는 단계마다 수강생이 묻고 조교 하루가 학교 수학과 숫자 하나로 풀어 줍니다. 식은 "식으로 보면"을 펼칠 때만 나옵니다. 여기서 한 번 멈춰도 괜찮아요.</p>
<details class="abbr"><summary>기호·영어 약어 풀이 ({len(P["abbr"])}개)</summary><div class="abbr-list">{abbr}</div></details></div></section>
<section class="sec" id="cast" aria-labelledby="h-cast" style="padding:18px 0 0;border:0"><div class="wrap"><h3 id="h-cast">강의실 사람들</h3>
<div class="cast" style="grid-template-columns:repeat(auto-fit,minmax(230px,1fr))">{cast}</div></div></section>
<section class="sec" id="open" aria-labelledby="h-open"><div class="wrap">
<h2 id="h-open"><span class="hex">{P["hex"]}</span>{P["open_title"]}</h2>
<div data-dlg="open"></div>
{P.get("bigpicture","")}
{steps}
</div></section>
<section class="sec" id="app" aria-labelledby="h-app"><div class="wrap">
<h2 id="h-app"><span class="hex">부록</span>{P["app_title"]}</h2>
<p>{P["app_lead"]}</p>
<div data-dlg="app"></div>
{P["app_html"]}
</div></section>
<section class="sec" id="sum" aria-labelledby="h-sum"><div class="wrap">
<h2 id="h-sum">정리 — {P["sum_title"]}</h2>
<div class="tblwrap"><table class="cmp"><thead><tr><th>질문</th><th>답 한 줄</th><th>단계</th></tr></thead><tbody>{summ}</tbody></table></div>
<h3>용어 대응 카드</h3><div class="gloss">{gloss}</div>
<h3>비유와 예시의 한계</h3><ul>{lims}</ul>
{P.get("bridge","")}
<div class="next">{nxt}</div>
</div></section>
<section class="sec" id="outro" aria-labelledby="h-outro"><div class="wrap"><h2 id="h-outro">아웃트로 — 수업을 마치며</h2><div data-dlg="outro"></div></div></section>
</main>
<footer><div class="wrap">
<h3>출처 — 이 페이지가 다시 쓴 연구실 콘텐츠</h3>
<table><thead><tr><th>#</th><th>자료</th><th>이 페이지에서 쓴 곳</th></tr></thead><tbody>{refs}</tbody></table>
<h3>예시값·설명용 모형인 것</h3><ul>{ex}</ul>
<p>캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다.</p>
<p>{AUTHOR} · <a href="index.html">좌표 첫걸음 목차</a> · 자매편 <a href="https://adminmrobo.github.io/optimization_3d_map/first_step_0.html">최적화 첫걸음</a></p>
</div></footer>
<script>
/*@@SPRITES@@*/
/*@@COMMON@@*/
/*@@SPACE@@*/
(function(){{
'use strict';
var $=U.$,$$=U.$$,fmt=U.fmt,cssv=U.cssv,V=PG.V,rng=PG.rng,txt=PG.txt;
U.dialogues({json.dumps(P["dlg"], ensure_ascii=False)});
U.fillImgs();
SP.drawCover&&SP.drawCover($('#cvCover'),{json.dumps(P["cover"].get("motif","plane"))});
{P["js"]}
U.Gloss({json.dumps(P["gloss"], ensure_ascii=False)},{json.dumps(P["gloss_core"], ensure_ascii=False)});
U.Study({{quiz:{json.dumps(P["quiz"], ensure_ascii=False)}}});
U.start();
}})();
</script>
</body>
</html>
'''
    open(os.path.join(B, P['key'] + '.src.html'), 'w').write(H)
    return H

EXTRA_CSS = '''
.tl,.tr{font-weight:700;font-size:13.5px;margin-bottom:4px}.tl{color:var(--amber)}.tr{color:var(--terrain)}
.hex{display:inline-grid;place-items:center;min-width:44px;height:34px;padding:0 10px;margin-right:10px;border-radius:8px;background:var(--terrain);color:#fff;font-size:17px;vertical-align:4px}
.sec{padding:40px 0;border-top:1px solid var(--rule)}
.cast{display:grid;gap:10px}.castc{display:flex;gap:10px;align-items:center;background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--cc);border-radius:10px;padding:8px 10px}
.castc img{width:60px;height:60px;flex:none}.castc p{margin:0;font-size:13.5px;color:var(--muted);line-height:1.55}
.cover .cast4 img{width:11%;max-width:110px}.cover .cast4 img.s{width:7%}
.num-in{width:7.5em;font:inherit;font-size:16px;padding:4px 8px;border:1px solid var(--rule);border-radius:8px}
.panel.game{border:2px solid var(--terrain);border-radius:14px}
.gameintro{background:#f4fbfb;border:1px dashed var(--terrain);border-radius:10px;padding:10px 14px;margin:10px 0;font-size:15px}
.cwrap.sq{aspect-ratio:1/1;max-width:560px;margin:0 auto;height:auto}
.cwrap.sq canvas{width:100%;height:100%}
@media(max-width:520px){.eqt td.m{white-space:normal;word-break:break-all}}
.cover img.art{image-rendering:pixelated;image-rendering:crisp-edges}
.diff{display:inline-block;border:1px solid var(--c-asst);color:var(--c-asst);border-radius:999px;padding:0 10px;font-size:12.5px;margin-left:6px}
'''

if __name__ == '__main__':
    keys = sys.argv[1:] or ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6']
    sys.path.insert(0, B)
    for k in keys:
        mod = importlib.import_module(k)
        if hasattr(mod, 'build'): mod.build()
        else: page(mod.PAGE)
        print('src', k)
