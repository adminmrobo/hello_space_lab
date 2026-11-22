# -*- coding: utf-8 -*-
"""지식 색인·참고문헌·페이지 서지 → build/kg/kg_{key}.json · refs_{key}.json · meta_{key}.json"""
import json, os, sys, importlib
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B)
os.makedirs(os.path.join(B, 'kg'), exist_ok=True)
TYPE_PREFIX = {'Concept': 'concept', 'Analogy': 'analogy', 'Simulation': 'sim', 'Limitation': 'limitation', 'Question': 'question', 'Method': 'method', 'Claim': 'claim'}
WORKS = {
 'euclid': ('자와 각도기의 방 — 시아·모아의 유클리드 공간', 'https://adminmrobo.github.io/euclidean_space_lab/'),
 'vector': ('벡터 분석 랩 — 네 개의 자로 읽는 화살표', 'https://adminmrobo.github.io/vector_analysis_lab/'),
 'optim': ('좌표축 위의 그릇·최적화 첫걸음', 'https://adminmrobo.github.io/optimization_3d_map/'),
 'atlas': ('머신러닝 모델 도감', 'https://adminmrobo.github.io/machine_learning_model_atlas/'),
 'vdb': ('벡터 DB 연구실', 'https://adminmrobo.github.io/vector_db_lab/'),
 'tensor': ('텐서 연구실', 'https://adminmrobo.github.io/what_is_tensor/'),
 'stats': ('우연의 과학통계학', 'https://adminmrobo.github.io/statistics_note/'),
}
WORKS['mink'] = ('시아·모아의 민코프스키 시공간', 'https://adminmrobo.github.io/minkowski_space_lab/')
PAGEWORKS = {'index': ['euclid', 'vector', 'optim'], 'ch1': ['euclid', 'optim', 'stats'], 'ch2': ['euclid', 'vector', 'atlas'], 'ch3': ['vector', 'euclid'],
             'ch4': ['vector', 'euclid', 'optim'], 'ch5': ['vector'], 'ch6': ['atlas', 'vdb', 'tensor', 'optim', 'euclid'], 'practice': ['euclid', 'vector', 'vdb']}
def nid(t, s): return 'lab:%s/%s' % (TYPE_PREFIX[t], s)
def build(key, mod):
    P, K = mod.PAGE, mod.KG
    ix = {}
    nodes = []
    for t, s, ko, en, anc, d in K['nodes']:
        i = nid(t, s); ix[s] = i
        nodes.append({'id': i, 'type': t, 'label': {'ko': ko, 'en': en}, 'page': P['out'].replace('.html', ''), 'anchor': anc, 'level': 1, 'status': 'known', 'confidence': 'high',
                      'coverage': 'explained', 'family': 'coordinates', 'domain': ['math', 'ai'], 'match': [], 'definition': {'ko': d}})
    edges = [{'s': ix[a], 'p': 'lab:' + p, 'o': ix[b], 'anchor': anc, 'confidence': 'high'} for a, p, b, anc in K['edges']]
    kg = {'version': '1.3', 'page': P['out'].replace('.html', ''), 'nodes': nodes, 'edges': edges}
    refs = []
    for w in PAGEWORKS[key]:
        t, u = WORKS[w]
        refs.append({'id': 'ahn_' + w, 'type': 'webpage', 'title': t, 'author': [{'family': '안', 'given': '상선'}], 'issued': {'date-parts': [[2026]]}, 'URL': u,
                     'lab': {'work': 'lab:work/ahn_' + w, 'role': 'background', 'supports': [], 'locs': [], 'verified': {'title': True, 'author': True, 'year': True, 'url': True},
                             'checkedBy': '연구실 저장소에서 직접 확인 (2026-11-23)', 'note': '이 페이지가 다시 쓴 연구실 콘텐츠'}})
    meta = {'title': P['title'], 'series': '좌표 첫걸음 — 나는 어디에 있는가?', 'number': key, 'creator': [{'name': '안상선', 'role': 'author', 'affiliation': '(주)M-Robo'}],
            'contributor': [{'name': 'AI 보조 제작', 'role': 'assistant'}], 'date': '2026-11-23', 'version': '1.0', 'language': ['ko'], 'license': '',
            'url': 'https://adminmrobo.github.io/hello_space_lab/' + P['out'], 'about': [n['id'] for n in nodes if n['type'] == 'Concept'][:4],
            'basedOn': ['ahn_' + w for w in PAGEWORKS[key]], 'educationalLevel': '입문', 'learningResourceType': 'interactive explainer', 'registry': 'KG_00_registry 0.2',
            'suggestedCitation': '안상선 (2026). %s. 좌표 첫걸음, v1.0.' % P['title']}
    for nm, obj in (('kg', kg), ('refs', refs), ('meta', meta)):
        json.dump(obj, open(os.path.join(B, 'kg', '%s_%s.json' % (nm, key)), 'w'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    for k in (sys.argv[1:] or ['index', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'practice']):
        try: m = importlib.import_module(k)
        except ModuleNotFoundError: continue
        if hasattr(m, 'KG'): build(k, m); print('kg', k)
