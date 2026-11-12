"""Responsive, motion and education checks for the colorful portfolio refresh."""
import json,threading,functools,http.server
from playwright.sync_api import sync_playwright,expect
from qa_helpers import ROOT, OUTPUT_DIR, launch_chromium
(OUTPUT_DIR/'screenshots').mkdir(parents=True,exist_ok=True)
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Handler,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_port}/'
checks=[];errors=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
with sync_playwright() as pw:
    b=launch_chromium(pw)
    c=b.new_context(viewport={'width':1440,'height':1000})
    c.route('https://formspree.io/**',lambda r:r.abort())
    p=c.new_page();p.on('pageerror',lambda e:errors.append(str(e)))
    for route in ['index','about','experience','projects','skills','certifications','recommendations','contact']:
        p.goto(base+route+'.html',wait_until='domcontentloaded')
        p.wait_for_function("document.documentElement.classList.contains('nav-ready')")
        for width in [320,375,640,760,768,900,1024,1199,1200,1440]:
            p.set_viewport_size({'width':width,'height':1000})
            check(f'{route}: no overflow at {width}px',p.evaluate('document.documentElement.scrollWidth<=innerWidth'))
            check(f'{route}: header clears content at {width}px',p.locator('main').bounding_box()['y']>=p.locator('header').bounding_box()['y']+p.locator('header').bounding_box()['height'])
        print('PASS responsive',route,flush=True)
    p.goto(base+'index.html')
    check('No pause/resume control',p.locator('[data-motion-toggle]').count()==0)
    cube=p.locator('.color-cube');before=cube.evaluate('e=>getComputedStyle(e).transform')
    p.wait_for_function('(before)=>getComputedStyle(document.querySelector(".color-cube")).transform!==before',arg=before)
    check('3D cube animates',True)
    stage=p.locator('.profile-stage');box=stage.bounding_box();p.mouse.move(box['x']+box['width']*.8,box['y']+box['height']*.6)
    p.wait_for_function("document.querySelector('[data-tilt]').style.getPropertyValue('--tilt-y')!==''")
    check('Pointer tilt responds',True)
    p.emulate_media(reduced_motion='reduce')
    check('Reduced motion stops 3D animation',cube.evaluate('e=>getComputedStyle(e).animationName')=='none')
    check('Reduced motion resets tilt',stage.evaluate('e=>getComputedStyle(e).transform')=='none')
    p.emulate_media(reduced_motion='no-preference')
    p.set_viewport_size({'width':375,'height':900});p.locator('.hamburger').click();expect(p.locator('nav')).to_be_visible()
    p.keyboard.press('Escape');expect(p.locator('.hamburger')).to_be_focused()
    check('Mobile navigation and keyboard Escape work',True)
    p.goto(base+'certifications.html');expect(p.locator('[data-results]')).to_contain_text(str(p.locator('[data-cert-category]').count()))
    p.locator('[data-filter="it-support-professional"]').click();p.locator('input[data-cert-search]').fill('Google')
    check('Google search returns support entries',p.locator('[data-cert-category]:visible').count()>0)
    program=p.locator('#google-it-support');expect(program).to_be_visible()
    expect(program).to_contain_text('Google IT Support')
    check('Completed program links to a certificate',program.locator('[data-certificate]').count()>0)
    p.locator('input[data-cert-search]').fill('Google');expect(program).to_be_visible()
    p.goto(base+'about.html');expect(p.locator('.education-card')).to_contain_text('BSc')
    check('Academic background remains visible',True)
    for route,width,name in [('index',1440,'desktop'),('index',820,'tablet'),('index',390,'mobile'),('certifications',1440,'learning'),('about',390,'education-mobile')]:
        p.set_viewport_size({'width':width,'height':1000});p.goto(base+route+'.html',wait_until='networkidle')
        if route=='index':
            p.evaluate("document.documentElement.style.scrollBehavior='auto';scrollTo(0,0)")
        if name=='learning': p.locator('#google-it-support').scroll_into_view_if_needed()
        if name=='education-mobile': p.locator('.education-card').scroll_into_view_if_needed()
        p.screenshot(path=str(ROOT/'qa/screenshots'/f'colorful-{name}.png'))
    nj=b.new_context(java_script_enabled=False,viewport={'width':320,'height':900});np=nj.new_page();np.goto(base+'index.html')
    expect(np.locator('nav')).to_be_visible();expect(np.locator('[data-motion-toggle]')).to_be_hidden()
    check('No-JS decorative motion is static',np.locator('.color-cube').evaluate('e=>getComputedStyle(e).animationName')=='none')
    check('No-JS phone layout fits',np.evaluate('document.documentElement.scrollWidth<=innerWidth'))
    np.goto(base+'certifications.html');expect(np.locator('#google-it-support')).to_be_visible()
    check('No-JS shows every credential',np.locator('[data-cert-category]:visible').count()==np.locator('[data-cert-category]').count()>0)
    nj.close();c.close();b.close()
    skipped=[]
    try:
        b=pw.firefox.launch(headless=True)
    except Exception as error:
        skipped.append({'check':'Firefox availability','detail':str(error)})
        print('SKIP Firefox: install the matching browser with python -m playwright install firefox',flush=True)
    else:
        p=b.new_page(viewport={'width':375,'height':900})
        for route in ['index','about','certifications']:
            p.goto(base+route+'.html');check(f'Firefox {route} fits phone',p.evaluate('document.documentElement.scrollWidth<=innerWidth'))
        p.goto(base+'index.html');check('Firefox animation runs automatically',p.locator('.color-cube').evaluate('e=>getComputedStyle(e).animationPlayState')=='running')
        b.close()
check('No JavaScript errors',not errors)
server.shutdown()
(ROOT/'qa/colorful-refresh-results.json').write_text(json.dumps({'passed':len(checks),'failed':0,'checks':checks,'page_errors':errors,'not_tested':skipped},indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} refresh checks; no JavaScript errors',flush=True)
