"""Local browser QA. Never sends a production contact form submission.
Run: python scripts/browser_qa.py. Optional --axe downloads pinned axe-core to temp.
"""
from pathlib import Path
import os, sys, json, threading, functools, http.server, urllib.request, time
from urllib.parse import urlsplit
extra=Path(os.environ.get('TEMP','/tmp'))/'portfolio-redesign-tools'
if extra.exists(): sys.path.insert(0,str(extra))
from playwright.sync_api import sync_playwright, expect
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'qa'; (OUT/'screenshots').mkdir(parents=True,exist_ok=True)
class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(QuietHandler,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
BASE=f'http://127.0.0.1:{server.server_port}/'
PAGES=['index','about','experience','projects','skills','certifications','recommendations','contact']
results=[]; failures=[]; axe_results=[]; errors=[]; contrast_failures=[]
def record(name,fn):
    try:
        detail=fn()
        results.append({'check':name,'passed':True,'detail':detail})
        print('PASS',name,flush=True)
    except Exception as e:
        results.append({'check':name,'passed':False,'detail':str(e)[:1500]}); failures.append(name)
        print('FAIL',name,str(e)[:200],flush=True)
def assert_true(condition,message='Assertion failed'):
    if not condition: raise AssertionError(message)
def ready(page,path):
    response=page.goto(BASE+path+'.html',wait_until='domcontentloaded')
    assert_true(response.status==200,'Independent route did not return 200')
    page.wait_for_function("document.querySelector('header') && document.documentElement.classList.contains('nav-ready')")
def layout(page,path,width,theme):
    page.set_viewport_size({'width':width,'height':960})
    page.emulate_media(color_scheme=theme)
    ready(page,path)
    page.wait_for_function("getComputedStyle(document.body).backgroundColor !== 'rgba(0, 0, 0, 0)'")
    overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth')
    if overflow:
        offenders=page.locator('body *').evaluate_all('(els) => els.filter(e => e.getBoundingClientRect().right > innerWidth+1).slice(0,8).map(e => e.tagName+"."+e.className)')
        raise AssertionError(f'Horizontal overflow: {offenders}')
    assert_true(page.locator('h1').is_visible(),'Missing visible H1')
    if path=='recommendations':
        assert_true(page.locator('h1').evaluate('e=>e.getBoundingClientRect().height <= parseFloat(getComputedStyle(e).lineHeight)*1.1'),'Recommendations title breaks mid-word')
    assert_true(page.locator('header').evaluate('e=>getComputedStyle(e).position')=='relative','Header must scroll normally')
    assert_true(page.locator('main').bounding_box()['y']>=page.locator('header').bounding_box()['y']+page.locator('header').bounding_box()['height'],'Header overlaps main content')
    if width<1200:
        menu=page.locator('.hamburger'); expect(menu).to_be_visible()
        menu.click(); expect(page.locator('nav')).to_be_visible()
        expect(menu).to_have_attribute('aria-expanded','true')
        page.keyboard.press('Escape'); expect(page.locator('nav')).to_be_hidden()
        expect(menu).to_be_focused()
    return {'width':width,'theme':theme,'route':path+'.html'}
axe=None
if '--axe' in sys.argv:
    try:
        axe=urllib.request.urlopen('https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.3/axe.min.js',timeout=25).read().decode()
        print('Loaded axe-core 4.10.3 for local-only audit',flush=True)
    except Exception as e: print('Axe not tested:',e,flush=True)
try:
  with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='chrome',headless=True)
    context=browser.new_context(viewport={'width':1440,'height':1000},color_scheme='light')
    # Safety boundary: any unexpected Formspree call is aborted. Individual tests override it.
    context.route('https://formspree.io/**',lambda route: route.abort())
    page=context.new_page()
    page.on('pageerror',lambda error:errors.append(str(error)))
    page.on('response',lambda response: errors.append(f'Local HTTP {response.status}: {response.url}') if response.url.startswith(BASE) and response.status>=400 else None)
    for path in PAGES:
      for theme in ['dark']:
        for width in [1440,1200,1199,1024,900,768,760,640,375,320]:
          record(f'Chrome layout/menu {path} {width} {theme}',lambda path=path,width=width,theme=theme:layout(page,path,width,theme))
      if axe:
        for theme in ['dark']:
          page.set_viewport_size({'width':1440,'height':1000}); page.emulate_media(color_scheme=theme); ready(page,path)
          page.add_script_tag(content=axe)
          audit=page.evaluate("async () => { const r = await axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22a','wcag22aa']}}); return {violations:r.violations.map(v=>({id:v.id,impact:v.impact,description:v.description,nodes:v.nodes.map(n=>({target:n.target,summary:n.failureSummary}))})),incomplete:r.incomplete.map(v=>({id:v.id,nodes:v.nodes.length})),passes:r.passes.length}; }")
          axe_results.append({'page':path,'theme':theme,**audit})
          record(f'axe WCAG {path} {theme}',lambda audit=audit:assert_true(not audit['violations'],json.dumps(audit['violations'])[:1200]))
    def themes():
      ready(page,'index')
      page.evaluate('localStorage.setItem("portfolio-theme","light")')
      page.emulate_media(color_scheme='light'); page.reload()
      expect(page.locator('html')).to_have_attribute('data-theme','dark')
      assert_true(page.locator('[data-theme-toggle]').count()==0)
      assert_true(page.evaluate('getComputedStyle(document.documentElement).colorScheme')=='dark')
      page.emulate_media(color_scheme='dark')
      expect(page.locator('html')).to_have_attribute('data-theme','dark')
    record('Dark only regardless of system or previously saved light preference',themes)
    def header_and_portrait():
      for width in [320,375,768,1440]:
        page.set_viewport_size({'width':width,'height':900}); ready(page,'index')
        assert_true(page.evaluate('getComputedStyle(document.querySelector("header")).position')=='relative')
        top=page.locator('header').bounding_box()['y']
        page.evaluate('scrollTo(0,600)')
        assert_true(page.locator('header').bounding_box()['y'] < top-500,'Header should scroll with the document')
        page.evaluate('scrollTo(0,0)')
        assert_true(page.locator('main').bounding_box()['y']>=page.locator('header').bounding_box()['y']+page.locator('header').bounding_box()['height'])
      portrait=page.locator('.home-visual img')
      expect(portrait).to_be_visible()
      assert_true(portrait.evaluate('e=>e.complete && e.naturalWidth>0'),'Portrait did not load')
      page.locator('.profile-link').click()
      page.wait_for_url(BASE+'about.html')
    record('Header scrolls normally at four widths, portrait loads and profile link navigates',header_and_portrait)
    def nav_keyboard():
      page.set_viewport_size({'width':375,'height':900}); ready(page,'index')
      page.keyboard.press('Tab'); expect(page.locator('.skip-link')).to_be_focused()
      page.keyboard.press('Enter'); expect(page.locator('main')).to_be_focused()
      page.evaluate('scrollTo(0,0)')
      menu=page.locator('.hamburger'); menu.focus(); page.keyboard.press('Enter')
      page.keyboard.press('Tab'); expect(page.locator('nav a').first).to_be_focused()
      page.keyboard.press('Escape'); expect(menu).to_be_focused()
      menu.click(); page.mouse.click(5,850); expect(menu).to_have_attribute('aria-expanded','false')
      menu.click(); page.locator('.brand').focus(); expect(menu).to_have_attribute('aria-expanded','false')
    record('Keyboard skip link, menu, Escape, outside click and focus',nav_keyboard)
    def projects():
      page.set_viewport_size({'width':1440,'height':1000}); ready(page,'projects')
      total=page.locator('article[data-project-category]').count(); assert_true(total==25)
      for chip in page.locator('[data-filter]').all():
        chip.click(); expect(chip).to_have_attribute('aria-pressed','true')
        category=chip.get_attribute('data-filter')
        visible=page.locator('article[data-project-category]:visible').all()
        assert_true(bool(visible),'Empty project category')
        for item in visible: assert_true(category=='all' or category in item.get_attribute('data-project-category').split())
      page.locator('[data-filter="all"]').click(); expect(page.locator('[data-results]')).to_contain_text('25')
      details=page.locator('details').first; details.locator('summary').focus(); page.keyboard.press('Enter'); expect(details).to_have_attribute('open','')
    record('All project categories, counts, selection and native disclosures',projects)
    def certificates():
      ready(page,'certifications')
      expect(page.locator('[data-results]')).to_contain_text('44')
      for chip in page.locator('[data-filter]').all():
        chip.click(); expect(chip).to_have_attribute('aria-pressed','true'); assert_true(page.locator('[data-cert-category]:visible').count()>0)
      page.locator('[data-filter="support-foundations"]').click()
      page.locator('input[data-cert-search]').fill('Google'); assert_true(page.locator('[data-cert-category]:visible').count()==3)
      page.locator('input[data-cert-search]').fill('no-such-credential-xyz'); expect(page.locator('[data-results]')).to_contain_text('No matches')
      assert_true(page.locator('[data-cert-category]:visible').count()==0)
      page.locator('input[data-cert-search]').fill(''); page.locator('[data-filter="all"]').click()
      page.locator('input[data-cert-search]').fill('<img src=x onerror=alert(1)>'); assert_true(page.locator('[data-results] img').count()==0)
      page.locator('input[data-cert-search]').fill(''); expect(page.locator('[data-results]')).to_contain_text('44')
    record('Combined credential text/category search, counts, empty and input safety',certificates)
    def original_scans():
      for path in ['certifications','projects']:
        ready(page,path)
        links=page.locator('a[data-certificate]').all()
        for link in links:
          assert_true(link.get_attribute('target')=='_blank')
          response=page.request.get(BASE+link.get_attribute('href'))
          assert_true(response.status==200,'Original scan unavailable')
        first=links[0]
        with page.expect_popup() as event:
          first.focus(); page.keyboard.press('Enter')
        scan=event.value; scan.wait_for_load_state()
        assert_true(scan.url==BASE+first.get_attribute('href'))
        assert_true(scan.locator('img').evaluate('e=>e.complete && e.naturalWidth>0'))
        assert_true(page.locator('dialog').count()==0)
        scan.close()
      return 'All 50 original scan links are available; keyboard activation opens scans directly.'
    record('Direct original scans, new tabs and keyboard activation',original_scans)
    def fill_form():
      ready(page,'contact'); page.locator('#name').fill('Local QA'); page.locator('#email').fill('local-test@example.invalid'); page.locator('#subject').select_option(label='Technical Support / Service Desk'); page.locator('#message').fill('Local intercepted test, never sent to production.')
    def forms():
      for kind in ['success','server-error','network-error','timeout']:
        fill_form(); calls=[]
        def intercept(route):
          calls.append(route.request.method)
          if kind=='network-error': route.abort()
          elif kind=='timeout': route.fulfill(status=200,content_type='application/json',body='{}')
          else: route.fulfill(status=200 if kind=='success' else 422,content_type='application/json',body='{}')
        page.route('https://formspree.io/**',intercept)
        if kind=='timeout':
          page.evaluate("window.fetch = (url,opts) => new Promise((resolve,reject) => opts.signal.addEventListener('abort',()=>reject(new DOMException('Aborted','AbortError')))); window._qaTimeout = window.setTimeout; window.setTimeout = (fn,ms,...args) => window._qaTimeout(fn,ms===15000?20:ms,...args)")
        page.locator('[type="submit"]').click()
        status=page.locator('[data-form-status]')
        if kind=='success': expect(status).to_contain_text('service accepted'); expect(page.locator('#message')).to_have_value('')
        elif kind=='timeout': expect(status).to_contain_text('delivery is unknown'); expect(page.locator('#message')).not_to_have_value('')
        else: expect(status).to_contain_text('could not confirm'); expect(page.locator('#message')).not_to_have_value('')
        expect(page.locator('[type="submit"]')).to_be_enabled(); expect(page.locator('[type="reset"]')).to_be_enabled()
        assert_true(calls==([] if kind=='timeout' else ['POST']))
        page.unroute('https://formspree.io/**',intercept)
      ready(page,'contact'); page.locator('[type="submit"]').click(); assert_true(page.locator('input:invalid').count()>0)
    record('Contact native validation and mocked accepted / rejected / network / timeout paths',forms)
    def copies():
      ready(page,'contact')
      page.evaluate("Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{}}})")
      page.locator('[data-copy]').click(); expect(page.locator('[data-copy-status]')).to_have_text('Discord username copied.')
      page.evaluate("Object.defineProperty(navigator,'clipboard',{configurable:true,value:undefined}); document.execCommand=()=>false")
      page.locator('[data-copy]').click(); expect(page.locator('[data-copy-status]')).to_contain_text('Copy unavailable')
      page.evaluate('document.execCommand=()=>true'); page.locator('[data-copy]').click(); expect(page.locator('[data-copy-status]')).to_have_text('Discord username copied.')
      page.evaluate("Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw Error('Denied')}}})")
      page.locator('[data-copy]').click(); expect(page.locator('[data-copy-status]')).to_contain_text('Copy unavailable')
    record('Clipboard modern success, denied, fallback true and false',copies)
    def download():
      ready(page,'index')
      with page.expect_download() as event: page.locator('main a[download]').first.click()
      downloaded=event.value; assert_true(downloaded.suggested_filename=='Mohamed_Rimsan_Resume.pdf'); assert_true(downloaded.failure() is None)
      assert_true(Path(downloaded.path()).read_bytes()==(ROOT/'Resume/AR-Mohamed-Rimsan-Resume.pdf').read_bytes())
    record('Native resume download matches original PDF',download)
    def legacy():
      page.goto(BASE+'hands-on-experience.html'); page.wait_for_url(BASE+'projects.html'); assert_true(page.url.startswith(BASE))
    record('Legacy redirect stays on preview host',legacy)
    def reduced_zoom():
      page.emulate_media(reduced_motion='reduce'); ready(page,'index'); assert_true(page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')=='auto')
      for path in PAGES:
        ready(page,path); page.evaluate("document.documentElement.style.zoom='2'")
        assert_true(not page.evaluate('document.documentElement.scrollWidth>innerWidth'),path+' overflow at 200% CSS zoom')
      # 1280 CSS px at 200% browser zoom has 640 CSS px of layout width.
      page.set_viewport_size({'width':640,'height':480}); ready(page,'index'); assert_true(not page.evaluate('document.documentElement.scrollWidth>innerWidth'))
    record('Reduced motion, 200% CSS zoom and 640px reflow proxy',reduced_zoom)
    def storage_failure():
      c=browser.new_context(viewport={'width':375,'height':900})
      c.add_init_script("Storage.prototype.getItem=()=>{throw Error('Storage unavailable')};Storage.prototype.setItem=()=>{throw Error('Storage unavailable')}")
      p=c.new_page(); ready(p,'index'); expect(p.locator('html')).to_have_attribute('data-theme','dark'); c.close()
    record('Unavailable storage does not break navigation or theme',storage_failure)
    def no_js():
      c=browser.new_context(java_script_enabled=False,viewport={'width':320,'height':900})
      p=c.new_page()
      for path in PAGES:
        p.goto(BASE+path+'.html',wait_until='domcontentloaded'); expect(p.locator('nav')).to_be_visible(); assert_true(p.locator('nav a:visible').count()==8)
        assert_true(not p.evaluate('document.documentElement.scrollWidth>innerWidth'),path+' no-JS overflow')
        assert_true(p.locator('header').evaluate('e=>e.scrollHeight<=e.clientHeight+1'),path+' no-JS navigation is clipped')
        assert_true(p.locator('main').bounding_box()['y']>=p.locator('header').bounding_box()['y']+p.locator('header').bounding_box()['height'],path+' no-JS header overlap')
      p.goto(BASE+'index.html'); expect(p.locator('.home-visual img')).to_be_visible()
      p.goto(BASE+'certifications.html'); assert_true(p.locator('[data-cert-category]:visible').count()==44); expect(p.locator('[data-filter-panel]')).to_be_hidden()
      link=p.locator('a[data-certificate]').first; response=p.request.get(BASE+link.get_attribute('href')); assert_true(response.status==200)
      p.goto(BASE+'projects.html'); assert_true(p.locator('article[data-project-category]:visible').count()==25)
      p.goto(BASE+'contact.html'); assert_true(p.locator('form').get_attribute('method')=='POST'); expect(p.locator('a[href^="mailto:"]').first).to_be_visible()
      c.close()
    record('Disabled JS: all navigation, content, original scans and native contact',no_js)
    # Representative screenshots of the dark-only design.
    page.set_viewport_size({'width':1440,'height':1000}); page.emulate_media(reduced_motion='reduce')
    for path,theme,width in [(path,'dark',width) for path in PAGES for width in [1440,375]]:
      page.set_viewport_size({'width':width,'height':1000}); page.emulate_media(color_scheme=theme); ready(page,path)
      page.evaluate('localStorage.removeItem("portfolio-theme")'); page.reload(wait_until='networkidle')
      page.screenshot(path=str(OUT/'screenshots'/f'{path}-{theme}-{width}.png'),full_page=True)
    context.close(); browser.close()
    # A genuinely different engine. Use an installed browser only; report unavailable honestly.
    candidates=sorted((Path(os.environ['LOCALAPPDATA'])/'ms-playwright').glob('firefox-*/firefox/firefox.exe'),reverse=True)
    if candidates:
      try:
        firefox=pw.firefox.launch(executable_path=str(candidates[0]),headless=True)
        c=firefox.new_context(viewport={'width':375,'height':900},color_scheme='dark'); c.route('https://formspree.io/**',lambda r:r.abort()); p=c.new_page()
        for path in PAGES: record('Firefox phone layout '+path,lambda path=path:layout(p,path,375,'dark'))
        def firefox_scan():
          ready(p,'certifications'); a=p.locator('a[data-certificate]').first
          with p.expect_popup() as event: a.click()
          scan=event.value; scan.wait_for_load_state()
          assert_true(scan.url==BASE+a.get_attribute('href')); scan.close()
        record('Firefox direct original scan',firefox_scan)
        firefox.close()
      except Exception as e: results.append({'check':'Firefox availability','passed':None,'detail':str(e)[:1000]})
    else: results.append({'check':'Firefox availability','passed':None,'detail':'No installed Firefox executable found'})
except Exception as error:
  failures.append('Browser runner'); results.append({'check':'Browser runner','passed':False,'detail':str(error)})
finally:
  server.shutdown()
  report={'passed':sum(r['passed'] is True for r in results),'failed':sum(r['passed'] is False for r in results),'not_tested':sum(r['passed'] is None for r in results),'checks':results,'page_errors':errors,'axe':axe_results,'production_form_submissions':0,'zoom_scope':'CSS zoom plus layout reflow proxy; browser chrome zoom and real assistive technology are not tested.'}
  (OUT/'browser-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
  print('Browser QA:',report['passed'],'passed;',report['failed'],'failed;',report['not_tested'],'not tested. Page errors:',len(errors),flush=True)
  sys.exit(bool(failures or errors))
