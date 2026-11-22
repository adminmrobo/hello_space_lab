# 부록 게임·실전 연습장 미션 판정 검사: 정답 조작을 흉내 내 통과 표시가 켜지는지, 조작 전에는 통과하지 않는지 본다.
# python3 code/check_missions.py
import os, asyncio, sys
from playwright.async_api import async_playwright
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETR = "([id,v])=>{const r=document.getElementById(id);r.value=v;r.dispatchEvent(new Event('input'))}"
CLICKXY = """([xr,yr,x,y])=>{const cv=document.getElementById('cvA');const P=SP.Plane(cv,{xr:xr,yr:yr});const b=cv.getBoundingClientRect();
  cv.dispatchEvent(new MouseEvent('click',{clientX:b.left+P.X(x),clientY:b.top+P.Y(y),bubbles:true}));}"""
async def rounds(pg, steps):
    star = lambda: pg.eval_on_selector('#gA .gstar', 'e=>e.textContent')
    await pg.click('#gA [data-r="chk"]'); s0 = await star()
    assert s0.endswith('0/' + str(len(steps))), ('조작 전 통과됨', s0)
    for i, fn in enumerate(steps):
        await fn(); await pg.click('#gA [data-r="chk"]')
        if i < len(steps) - 1: await pg.click('#gA [data-r="next"]')
    return await star()
async def main():
    bad = 0
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        async def page(f):
            pg = await b.new_page(viewport={'width': 1280, 'height': 900}); await pg.goto('file://' + os.path.join(R, f)); await pg.wait_for_timeout(500); return pg
        def setr(pg, i, v): return lambda: pg.evaluate(SETR, [i, v])
        def multi(*fs):
            async def run():
                for f in fs: await f()
            return run
        res = {}
        pg = await page('01_number_line.html'); res['1장 자 통역사'] = await rounds(pg, [setr(pg, 'rA', -250), setr(pg, 'rA', -400), setr(pg, 'rA', 77), setr(pg, 'rA', 2)])
        pg = await page('02_plane.html'); cl = lambda x, y: (lambda: pg.evaluate(CLICKXY, [[-6, 6], [-6, 6], x, y]))
        res['2장 보물찾기'] = await rounds(pg, [cl(3, -2), cl(-4, 1), cl(2, 4), cl(1, 2)])
        pg = await page('03_polar.html'); rp = lambda r, t: multi(setr(pg, 'rAr', r), setr(pg, 'rAt', t))
        res['3장 레이더'] = await rounds(pg, [rp(5, 53), rp(5.7, 135), rp(6, 270), rp(5.1, 191)])
        pg = await page('04_space.html'); xyz = lambda a: multi(setr(pg, 'rAx', a[0]), setr(pg, 'rAy', a[1]), setr(pg, 'rAz', a[2]))
        res['4장 드론 배송'] = await rounds(pg, [xyz([4, 3, 2]) if False else xyz([4, 2, 3]), xyz([4, 3, 2]), xyz([1, 2, 2]), xyz([3, 4, 0])])
        pg = await page('05_earth_map.html'); res['5장 배송센터'] = await rounds(pg, [setr(pg, 'rA', 1112), setr(pg, 'rA', 882), setr(pg, 'rA', 556), setr(pg, 'rA', 4)])
        pg = await page('06_data_space.html')
        def cust(i, mode):
            async def run():
                await pg.evaluate("""([i,z])=>{const C=[[31,260],[52,205],[25,120],[45,380],[35,450],[58,150],[28,300],[40,90],[23,240],[50,320]];const cv=document.getElementById('cvA');
                  const m=[0,1].map(k=>C.reduce((s,c)=>s+c[k],0)/C.length),sd=[0,1].map(k=>Math.sqrt(C.reduce((s,c)=>s+(c[k]-m[k])**2,0)/C.length));
                  let p=C[i];if(z)p=[(p[0]-m[0])/sd[0],(p[1]-m[1])/sd[1]];const P=z?SP.Plane(cv,{xr:[-2.5,2.5],yr:[-2.5,2.5]}):SP.Plane(cv,{xr:[0,480],yr:[0,480]});const b=cv.getBoundingClientRect();
                  cv.dispatchEvent(new MouseEvent('click',{clientX:b.left+P.X(p[0]),clientY:b.top+P.Y(p[1]),bubbles:true}));}""", [i, mode])
            return run
        res['6장 쿠폰 담당자'] = await rounds(pg, [cust(1, False), cust(0, True), cust(3, True), cust(5, False)])
        for k, v in res.items():
            ok = v.strip().endswith('4/4'); bad += 0 if ok else 1; print(('OK ' if ok else 'BAD'), k, v)
        # 실전 연습장
        pg = await page('practice/index.html#ship')
        st = lambda sc: pg.evaluate("s=>window[s].M.join('')", sc)
        assert await st('SHIP') == '000', '연습장: 조작 전 통과'
        for i, v in [('ship_lat', 37.5), ('ship_dl', 10), ('ship_bat', 1000), ('ship_lat', 60), ('ship_bat', 1110), ('ship_bat', 650), ('ship_lat', 0), ('ship_dl', 5)]:
            await pg.evaluate(SETR, [i, v])
        r1 = await st('SHIP')
        await pg.goto('file://' + os.path.join(R, 'practice/index.html#radar')); await pg.wait_for_timeout(300)
        await pg.evaluate(SETR, ['radar_r', 5]); await pg.evaluate(SETR, ['radar_t', 53])
        await pg.click('[data-rt="-3,-4"]'); await pg.evaluate(SETR, ['radar_t', 53.5]); await pg.evaluate(SETR, ['radar_t', 233])
        await pg.click('[data-rt="0,-5"]'); await pg.evaluate(SETR, ['radar_t', 270])
        await pg.click('[data-rt="3,4"]'); await pg.evaluate(SETR, ['radar_t', 53])
        r2 = await st('RADAR')
        await pg.goto('file://' + os.path.join(R, 'practice/index.html#ware')); await pg.wait_for_timeout(300)
        for o, a in [(0, [4, 3, 2]), (1, [1, 2, 2]), (2, [2, 3, 6])]:
            await pg.click(f'[data-wo="{o}"]')
            for k, v in zip('xyz', a): await pg.evaluate(SETR, ['ware_' + k, v])
        r3 = await st('WARE')
        await pg.goto('file://' + os.path.join(R, 'practice/index.html#shop')); await pg.wait_for_timeout(300)
        await pg.evaluate(SETR, ['shop_age', 30]); r4a = await st('SHOP')
        await pg.click('[data-sm="z"]'); await pg.click('[data-sm="raw"]')
        await pg.click('[data-sm="z"]'); await pg.evaluate(SETR, ['shop_age', 42]); await pg.evaluate(SETR, ['shop_buy', 330]); await pg.evaluate(SETR, ['shop_w', 2])
        r4 = await st('SHOP')
        for k, v in [('① 배송센터', r1), ('② 관제탑', r2), ('③ 물류창고', r3), ('④ 추천 매장', r4)]:
            ok = v == '111'; bad += 0 if ok else 1; print(('OK ' if ok else 'BAD'), '연습장', k, v)
        await b.close()
    print('모든 미션 판정 통과' if not bad else '실패 %d' % bad); sys.exit(1 if bad else 0)
asyncio.run(main())
