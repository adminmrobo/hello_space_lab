# 나는 어디에 있는가? — 좌표계로 본 매핑 (좌표 첫걸음)

연구실이 그동안 만든 공간·벡터·지도·데이터 콘텐츠에서 **기본이 되는 좌표계만** 골라, 처음 오신 분이 차례로 따라올 수 있게 다시 쓴 강의형 안내서입니다. 자매편 **「최적화 첫걸음」**이 "어디로 가야 하나?"를 묻는다면, 이 시리즈는 그 앞의 질문 "나는 어디에 있는가?"를 맡습니다.

박사가 강의하고, 조교 하루·초파리 연구원·주판봇이 돕고, 수강생 시아·모아·X1·X2·X3가 듣는 강의실 형식입니다. 연구실 비전공자판 스킬(ai-lab-explainer-plain v1.3, 흰 배경 "낮의 연구실")을 따릅니다.

- 사이트: https://adminmrobo.github.io/hello_space_lab/
- 글 · 안상선 ((주)M-Robo 대표) · [저자 소개](https://adminmrobo.github.io/who_am_i/who_am_i.html)

| 장 | 파일 | 내용 | 부록 게임·시연 |
|---|---|---|---|
| 목차 | `index.html` | 강의 계획표, 강의실 사람들, 자매편 안내, 다시 쓴 연구실 콘텐츠 | — |
| 1장 수직선 | `01_number_line.html` | 기준점·방향·눈금, 0층 없는 엘리베이터, 섭씨·화씨, 표준화 자 | 자 통역사 (4판) |
| 2장 좌표평면 | `02_plane.html` | 좌석표 순서쌍, 직선 거리 5와 골목 거리 7, 점과 화살표 | 거리만 알려 주는 보물찾기 · GPS (4판) |
| 3장 극좌표 | `03_polar.html` | (3, 4) = (5, 53.1°), 피자 테두리, 12월과 1월 시계판 | 레이더 관제실 (4판) |
| 4장 공간좌표 | `04_space.html` | 그림자 + 높이, (2, 3, 6) → 7, 모눈·원통·지구본 자 | 드론 배송 (4판) |
| 5장 지구와 지도 | `05_earth_map.html` | 위도·경도, 경도 1도 = 111.2 km × cos(위도), 메르카토르와 매핑의 대가 | 지구 배송센터 (4판) |
| 6장 데이터의 좌표 | `06_data_space.html` | 특성 공간, 표준화 후 거리, n차원, 좌표 위의 오차 지형 → 최적화 첫걸음 | 쿠폰 담당자 · 가장 가까운 이웃 (4판) |
| 마지막 장 | `practice/index.html` | 실전 연습장: 지구 배송센터·관제탑·물류창고·추천 매장 (주소 끝 `#ship` `#radar` `#ware` `#shop`) | 미션 12개 |

모든 페이지는 흰 배경의 단일 HTML 파일입니다(외부 요청은 글꼴 하나). 그래프와 3D는 Canvas로 직접 그렸고, 3D는 끌거나 시점 버튼·화살표 키로 돌릴 수 있습니다. 페이지 끝에 지식 색인(`#kg`)과 온톨로지·서지 꾸러미(`#export`)가 있습니다.

## 다시 쓴 연구실 콘텐츠

| 콘텐츠 | 쓴 곳 |
|---|---|
| [자와 각도기의 방](https://adminmrobo.github.io/euclidean_space_lab/) | 모눈·자·각도기·화살표 (1·2·4장) |
| [벡터 분석 랩](https://adminmrobo.github.io/vector_analysis_lab/) | 네 가지 자, 피자, 12월과 1월, 경도 1도, 그린란드 (3·4·5장) |
| [좌표축 위의 그릇 · 최적화 첫걸음](https://adminmrobo.github.io/optimization_3d_map/) | 3D 지형, 오차를 높이로 (4·6장), 빌드·그림 모듈 |
| [머신러닝 모델 도감](https://adminmrobo.github.io/machine_learning_model_atlas/) | 같은 모눈 위의 데이터 (6장) |
| [벡터 DB 연구실](https://adminmrobo.github.io/vector_db_lab/) · [텐서 연구실](https://adminmrobo.github.io/what_is_tensor/) | 임베딩과 고차원 점 (6장) |
| [우연의 과학통계학](https://adminmrobo.github.io/statistics_note/) | 표준화 점수 (1·6장) |

## 폴더

```
.
├─ index.html · 01~06_*.html · practice/index.html   완성 페이지 (build/에서 만듦)
├─ build/
│  ├─ ch1.py ~ ch6.py · index.py · practice.py   장마다 본문·대사·실험·게임·퀴즈·지식 색인 정의
│  ├─ gen.py          같은 틀(표지·3줄 상자·강의실·단계·부록·정리·아웃트로)로 *.src.html 생성
│  ├─ kg_defs.py      지식 색인·참고문헌·서지 → build/kg/
│  ├─ space.js        계산(거리·극좌표·원통·지구본·위도경도·메르카토르·표준화)과 2D 평면·판 넘기기 게임 모듈
│  ├─ common.css · common.js · sprites96.js   공용 디자인·모듈·캐릭터 팩 (optimization_3d_map에서 가져옴)
│  ├─ kgx.js · backbone.json   지식 색인·꾸러미 모듈과 AI 영역 뼈대 (ahnboat_lab_explainer onto-retrofit)
│  └─ build.js        조립
├─ code/
│  ├─ check_numbers.js    모든 "숫자로 한 번 해 보기"·게임 정답 검산
│  ├─ check_missions.py   부록 게임 24판·연습장 미션 12개 판정 검사 (조작 전에는 통과하지 않는지 포함)
│  ├─ check_browser.py    390·1280px 가로 넘침·콘솔 오류·빈 캐릭터 그림 검사
│  ├─ check_words.sh      금지 단어 0건 검사
│  ├─ make_og.py · make_docs.py · shot.py
├─ docs/PLAN.md · TEACHING_REVIEW.md · IMAGE_PROMPTS.md
├─ img/      픽셀 표지 8장, og/ 공유 미리보기 960×540
└─ cover_manifest.json   표지 현황판 연결
```

다시 만들기: `python3 build/gen.py index ch1 ch2 ch3 ch4 ch5 ch6 practice && python3 build/kg_defs.py && node build/build.js`
검사: `node code/check_numbers.js && python3 code/check_missions.py && python3 code/check_browser.py && sh code/check_words.sh`

## 그림

16비트 RPG 픽셀아트 표지 8장(`img/cover_*.webp`, 480×270 격자를 NEAREST 4배로 키운 1920×1080 무손실 WebP)이 들어 있습니다. 지시문은 `docs/IMAGE_PROMPTS.md`.

## 저작권

캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다. 숫자·고객·도시 예시는 설명용이며 경영·투자 권고가 아닙니다.
