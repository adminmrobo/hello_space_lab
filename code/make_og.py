# 공유 미리보기(og:image): 픽셀 표지의 원래 격자(480×270)를 NEAREST 2배로 키운 960×540 PNG → img/og/{key}.png
import os, json
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for p in json.load(open(os.path.join(R, 'build', 'pages.json'))):
    im = Image.open(os.path.join(R, 'img', 'cover_%s.webp' % p['key'])).convert('RGB')
    im.resize((480, 270), Image.NEAREST).resize((960, 540), Image.NEAREST).save(os.path.join(R, 'img', 'og', p['key'] + '.png'), optimize=True)
    print(p['key'], os.path.getsize(os.path.join(R, 'img', 'og', p['key'] + '.png')) // 1024, 'KB')
