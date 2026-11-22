# -*- coding: utf-8 -*-
"""그림 지시문(docs/IMAGE_PROMPTS.md)과 표지 현황(cover_manifest.json)을 만든다: python3 code/make_docs.py"""
import json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = "Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2-3 tone shading, small highlights)."
CH = """Characters:
- The professor: middle-aged man, spiky black hair with one white streak, teal glasses, white lab coat over black vest and tie. He lectures at the front.
- Haru the teaching assistant: young woman, pink hair with blue streaks in two side buns, lavender hoodie under a white lab coat.
- The fruit-fly researcher (teaching assistant): a fruit fly wearing a blue round helmet with big red compound-eye goggles and cables, transparent wings.
- The abacus robot (teaching assistant): small robot with a beige monitor head showing a simple green face, antenna, abacus-frame body, tank treads.
- Sia (student): young woman, long straight black hair, dark eyes, black maid-style lab uniform with white apron and gray bow.
- Moa (student): young woman, long light-brown hair with white frilled headband, mustard maid-style lab cardigan with red striped bow, holding a tea cup.
- X1, X2, X3 (students in the back row): three small dark navy-black silhouettes with white dot eyes (one with a pink ribbon, one with a beret and teal glasses, one small cat-eared one with a yellow bell)."""
T = "Pixel art only: visible square pixels, limited palette, no smooth gradients, no painterly or 3D-render look. No text, letters, numbers or symbols anywhere in the image; leave any speech bubbles and the board empty of writing (only simple drawn shapes). Keep faces and hands inside the safe area (12% from left and right edges, 10% from top, 18% from bottom). Keep the bottom-left corner empty. Bright white daytime lecture room palette with teal, red and amber accents."
S = [
 ("cover_index", "index.html", "index", "목차 표지·og", "A bright white pixel-art lecture room seen from the side of the students. On a big white board at the front, a simple drawing: a number line, then a grid with one red map pin, then concentric circles, then a small 3D axes box, then a globe, then a cloud of dots, connected left to right by small arrows. The professor stands at the board pointing at the red map pin. Haru stands beside the board holding a pointer, the fruit-fly researcher hovers above with a magnifier, the abacus robot rolls in with an abacus. Sia (front row) raises her hand eagerly, Moa (front row) takes notes with a tea cup on her desk, X1, X2, X3 sit in the back row leaning forward."),
 ("cover_ch1", "01_number_line.html", "ch1", "1장 수직선", "The same lecture room. A long horizontal ruler-like number line runs across the board with one zero mark glowing red. In the corner, a small cross-section of a building with an elevator shaft (basement floors below a green ground line). The professor points to the zero mark. The abacus robot confidently counts floors on its abacus; the fruit-fly researcher frowns at the elevator, magnifier raised. Haru holds two thermometers side by side. Sia and Moa look at the thermometers curiously."),
 ("cover_ch2", "02_plane.html", "ch2", "2장 좌표평면", "The lecture room seen from above at a slight angle: desks arranged in a neat grid like graph paper, with faint grid lines on the floor. One desk glows red where Sia sits; Moa sits diagonally behind. A paper airplane flies in a straight line from Sia to Moa, while a dotted L-shaped path along the aisles shows the longer way. The professor stands by the board drawing a right triangle. The fruit-fly researcher holds three glowing rings of different sizes that overlap at one point, the abacus robot holds a small treasure chest. X1, X2, X3 cheer from the back."),
 ("cover_ch3", "03_polar.html", "ch3", "3장 극좌표", "The lecture room turned into an airport control tower: a round green radar screen with concentric circles and spokes fills the board. One blip glows red. The professor points at the blip with a long pointer. Haru holds two pizzas of different sizes, both with one same-angle slice cut out. Moa holds a round wall calendar shaped like a clock. The abacus robot sends a small drone along a spoke; the fruit-fly researcher checks the angle with a protractor."),
 ("cover_ch4", "04_space.html", "ch4", "4장 공간좌표", "The lecture room with a tall glass model of a three-floor building and a 3D axes frame (red, teal, black arrows) standing on the front desk. A small delivery drone hovers inside the frame above a dotted shadow on the floor. The professor gestures at the height. Haru holds a cylinder-shaped tank model, the fruit-fly researcher holds a small globe, the abacus robot pilots the drone with a remote. Sia and Moa watch the drone shadow on the desk."),
 ("cover_ch5", "05_earth_map.html", "ch5", "5장 지구와 지도", "The lecture room with a big globe with latitude and longitude lines on the front desk, and next to it a flat rectangular map with grid lines and simple blob-shaped lands. The professor peels an orange in a spiral to show that a ball cannot lie flat. Haru holds the globe with a red map pin stuck on it. The abacus robot measures a huge northern island shape on the flat map with a ruler, looking proud; the fruit-fly researcher shakes his head and points at the globe. Moa and Sia compare the globe and the map."),
 ("cover_ch6", "06_data_space.html", "ch6", "6장 데이터의 좌표", "The lecture room where the board shows rows of a table flying off and turning into colored dots on a scatter chart. A new customer dot glows amber with a dashed circle reaching its nearest neighbor. Behind, a smooth bowl-shaped 3D surface with a red ball and an arrow pointing downhill. The professor points from the dot to the bowl. Haru holds coupons, the abacus robot holds a measuring tape, the fruit-fly researcher adjusts two rulers of different lengths to the same size. All five students applaud."),
 ("cover_practice", "practice/index.html", "practice", "마지막 장 · 실전 연습장", "A bright control room with four big screens in a row: a drone flying along a latitude line on a globe, a round radar screen, a 3D warehouse shelf grid with a drone, a scatter chart of customer dots. The professor stands in the middle with arms crossed, smiling. Haru operates the globe console, the fruit-fly researcher the radar, the abacus robot the warehouse, Sia and Moa the customer screen. X1, X2, X3 cheer from a small gallery behind."),
]
out = ['# 그림 생성 지시문 — 좌표 첫걸음 (16비트 RPG 픽셀아트 · 낮의 강의실)', '',
 '> 화풍(필수): 모든 표지는 **16비트 RPG 픽셀아트**, 흰 배경의 밝은 낮 강의실. 애니메이션 일러스트체·수채화·3D 렌더로 받지 않는다.',
 '> 참고 그림: fruitfly-lab-expressions 캐릭터 그림만 첨부(박사·하루·초파리 연구원·주판봇·시아·모아·X1~X3). 다른 화풍 그림은 첨부하지 않는다.',
 '> 받는 순서: ① cover_index를 먼저 받아 화풍 확인 → ② 그 그림을 참고 그림으로 함께 올려 3~4장씩 요청(1~3장 → 4~6장 → 연습장).',
 '> 이야기 설정: 박사가 강의, 조교 하루·초파리 연구원·주판봇이 돕고, 수강생 시아·모아(앞줄)와 X1~X3(뒷줄)가 듣는 강의실.', '',
 '## 받은 그림 픽셀 확인표', '- [ ] 네모난 픽셀이 보인다 · 굵은 어두운 외곽선, 2~3단 음영', '- [ ] 부드러운 그라데이션·붓 질감·3D 렌더 느낌이 없다', '- [ ] 캐릭터 얼굴·머리색이 기준 그림과 같다',
 '- [ ] 그림 안에 글자·숫자·기호가 없다(칠판·말풍선은 비움)', '- [ ] 얼굴·손이 안전 영역 안, 왼쪽 아래 모서리 비어 있음(표지 꼬리표 자리)', '',
 '## 저장 이름·반영', '| 파일 | 비율 | 쓰는 곳 |', '|---|---|---|']
out += ['| img/%s.webp | 16:9 | %s (%s) |' % (k, w, p) for k, p, o, w, s in S]
out += ['', '- 반영: 생성 PNG를 4로 나눈 원래 픽셀 격자(예 480×270)를 찾아 `NEAREST` 정수배로만 키운 무손실 WebP(1920×1080)로 저장하고 `.cover img{image-rendering:pixelated}`. 정수배가 아닌 크기나 손실 압축은 쓰지 않는다(흐려진다).',
 '- 지금 페이지 표지는 캔버스로 그린 **임시 표지**(모눈 + 주제 도형 + 캐릭터 팩)다. 그림을 받으면 각 페이지 `#cover .frame`의 캔버스를 `<img class="art">`로 바꾸고 `python3 code/make_og.py`로 공유 미리보기를 다시 만든다.',
 '- 받은 뒤 ahnboat_lab_cover_status 명부에 등록.', '']
for k, p, o, w, s in S:
    out += ['## %s — 16:9 · %s' % (k, w), '', '```text', H, '', s, '', CH, '', T, '```', '']
open(os.path.join(R, 'docs', 'IMAGE_PROMPTS.md'), 'w').write('\n'.join(out))
json.dump({'repo': 'adminmrobo/hello_space_lab', 'series': '좌표 첫걸음 — 나는 어디에 있는가? 좌표계로 본 매핑', 'style': '16-bit RPG pixel art, daytime white lecture room',
           'status': '임시 표지(캔버스). 픽셀 표지 지시문은 docs/IMAGE_PROMPTS.md', 'languages': ['ko'], 'ontology': True,
           'characters': ['doc', 'asst', 'fly', 'robo', 'sia', 'moa', 'x1', 'x2', 'x3'],
           'covers': [{'page': p, 'file': 'img/%s.webp' % k, 'state': 'prompt_ready', 'og': 'img/og/%s.png' % o} for k, p, o, w, s in S]},
          open(os.path.join(R, 'cover_manifest.json'), 'w'), ensure_ascii=False, indent=1)
print('docs ok')
