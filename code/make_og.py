# 공유 미리보기(og:image): 임시 표지를 찍어 img/og/{key}.png로 저장 (픽셀 표지를 받으면 다시 만든다)
import os, asyncio, json
from playwright.async_api import async_playwright
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
async def main():
    pages = json.load(open(os.path.join(R, 'build', 'pages.json')))
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        for pgd in pages:
            pg = await b.new_page(viewport={'width': 1236, 'height': 800}, device_scale_factor=1)
            await pg.goto('file://' + os.path.join(R, pgd['out'])); await pg.wait_for_timeout(600)
            el = await pg.query_selector('#cover .frame')
            await el.screenshot(path=os.path.join(R, 'img', 'og', pgd['key'] + '.png')); await pg.close()
        await b.close()
asyncio.run(main())
