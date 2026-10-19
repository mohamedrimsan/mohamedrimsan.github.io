from pathlib import Path
import sys, os, json, threading, functools, http.server, urllib.request
sys.path.insert(0,str(Path(os.environ['TEMP'])/'portfolio-redesign-tools'))
from playwright.sync_api import sync_playwright
ROOT=Path.cwd()
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Handler,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
axe=urllib.request.urlopen('https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.3/axe.min.js',timeout=20).read().decode()
results=[]
with sync_playwright() as p:
    b=p.chromium.launch(channel='chrome',headless=True)
    page=b.new_page()
    for path in ['index','about','experience','projects','skills','certifications','recommendations','contact']:
        for theme,width in [('dark',1440),('dark',375)]:
            page.set_viewport_size({'width':width,'height':1000}); page.emulate_media(color_scheme=theme)
            page.goto(f'http://127.0.0.1:{server.server_port}/{path}.html',wait_until='networkidle')
            page.add_script_tag(content=axe)
            r=page.evaluate("async()=>{const r=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22a','wcag22aa']}});return {violations:r.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>({target:n.target,summary:n.failureSummary}))})),incomplete:r.incomplete.map(v=>({id:v.id,nodes:v.nodes.length})),passes:r.passes.length}}")
            results.append({'page':path,'theme':theme,'width':width,**r}); print(path,theme,width,'violations',len(r['violations']),flush=True)
    b.close()
server.shutdown()
Path('qa/accessibility-results.json').write_text(json.dumps({'axe_version':'4.10.3','tags':['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22a','wcag22aa'],'audits':results},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert all(not r['violations'] for r in results), 'Accessibility violations remain'
