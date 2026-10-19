"""Read-only static QA: python scripts/verify_site.py (see requirements-qa.txt)."""
from pathlib import Path
import sys, os, json, hashlib, re, subprocess, xml.etree.ElementTree as ET
from urllib.parse import urlsplit, unquote
# Optional temporary tool path used by the implementation environment.
extra = Path(os.environ.get('TEMP', '/tmp')) / 'portfolio-redesign-tools'
if extra.exists(): sys.path.insert(0,str(extra))
from bs4 import BeautifulSoup
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
os.chdir(ROOT)
PAGES=['index','about','experience','projects','skills','certifications','recommendations','contact']
docs={p:BeautifulSoup(Path(p+'.html').read_text(encoding='utf-8-sig'),'html.parser') for p in PAGES}
checks=[]
def check(name,condition,detail=''):
    checks.append({'check':name,'passed':bool(condition),'detail':detail})
manifest=json.loads(Path('qa/evidence-baseline.json').read_text(encoding='utf-8'))
for file,d in docs.items():
    ids=[t['id'] for t in d.select('[id]')]
    check(file+': unique IDs',len(ids)==len(set(ids)))
    check(file+': landmarks',len(d.select('main'))==1 and len(d.select('h1'))==1 and d.html.get('lang')=='en')
    check(file+': navigation',len(d.select('nav[aria-label] a'))==8 and len(d.select('nav a[aria-current="page"]'))==1)
    check(file+': skip link',bool(d.select_one('a.skip-link[href="#main-content"]')))
    check(file+': metadata',all(d.select_one(s) for s in ['title','meta[name="description"]','link[rel="canonical"]','meta[property="og:title"]','meta[name="twitter:title"]']))
    for ld in d.select('script[type="application/ld+json"]'): json.loads(ld.string)
    check(file+': structured data',bool(d.select_one('script[type="application/ld+json"]')))
    for tag in d.select('[href], [src], [action], [data-preview]'):
        for attr in ['href','src','action','data-preview']:
            if not tag.has_attr(attr): continue
            value=tag[attr]; url=urlsplit(value)
            if url.scheme or url.netloc: continue
            path=Path(unquote(url.path)) if url.path else Path(file+'.html')
            exists=path.is_file()
            check(file+': local '+attr+' '+value,exists)
            if exists:
                cursor=ROOT
                for component in path.parts:
                    exact=component in [x.name for x in cursor.iterdir()]
                    check(file+': exact case '+str(path),exact)
                    cursor=cursor/component
                if url.fragment and path.suffix=='.html':
                    target=BeautifulSoup(path.read_text(encoding='utf-8-sig'),'html.parser')
                    check(file+': fragment '+value,target.find(id=unquote(url.fragment)) is not None)
    for image in d.select('img'):
        check(file+': image alt','alt' in image.attrs)
        if image.has_attr('src'): check(file+': intrinsic image dimensions',image.has_attr('width') and image.has_attr('height'))
    for link in d.select('a[target="_blank"]'):
        check(file+': safe external link',{'noopener','noreferrer'}.issubset(set(link.get('rel',[]))))
for path,digest in manifest['assets'].items():
    check('original unchanged: '+path,Path(path).exists() and hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest)
for project in manifest['projects']:
    matching=[x for x in docs['projects'].select('article[data-project-category]') if x.h3.get_text(' ',strip=True)==project['label']]
    check('project retained: '+project['label'],len(matching)==1)
    if matching:
        item=matching[0]
        for link in project['links']: check('project link retained: '+link,bool(item.select_one(f'a[href="{link}"]')))
        if project['label']!='Personal Portfolio Website':
            original=BeautifulSoup(subprocess.check_output(['git','show','63a5cb3:projects.html']).decode(),'html.parser')
            old=next(x for x in original.select('article[data-project-category]') if x.h3.get_text(' ',strip=True)==project['label'])
            for selector in ['p','.project-tags','details','.status-badge']:
                for evidence in old.select(selector): check('project evidence retained: '+project['label'],evidence.get_text(' ',strip=True) in item.get_text(' ',strip=True))
for cert in manifest['credentials']:
    scan=cert['scan']; found=[a for a in docs['certifications'].select('a[data-certificate]') if unquote(urlsplit(a['href']).path)==scan]
    check('credential scan retained: '+cert['label'],len(found)==1)
    check('legacy preview fragment retained: '+cert['popup'],docs['certifications'].find(id=cert['popup']) is not None)
    if found:
        oldtext=cert['text'].replace(' Preview Certificate ×','').strip()
        item=found[0].find_parent('article')
        check('credential label retained: '+cert['label'],item.h3.get_text(' ',strip=True)==cert['label'])
for rec in manifest['recommendations']:
    matching=[x for x in docs['recommendations'].select('.testimonial-card') if x.h3.get_text(' ',strip=True)==rec['label']]
    check('recommendation exact quote: '+rec['label'],len(matching)==1 and matching[0].select_one('.quote').get_text()==rec['quote'])
    check('recommendation attribution: '+rec['label'],bool(matching) and matching[0].select_one('.recommendation-head').get_text(' ',strip=True)==rec['attribution'])
original=BeautifulSoup(subprocess.check_output(['git','show','63a5cb3:experience.html']).decode(),'html.parser')
for role in original.select('.role-card'):
    name=role.h2.get_text(' ',strip=True)
    current=next(x for x in docs['experience'].select('.role-card') if x.h2.get_text(' ',strip=True)==name)
    for evidence in role.select('.role-meta,.list li'):
        # Owner-confirmed correction: Help Desk employment ended October 2026.
        expected=evidence.get_text(' ',strip=True)
        if name=='Help Desk Representative': expected=expected.replace('February 2025 – Present','February 2025 – October 2026')
        check('role evidence retained: '+name,expected in current.get_text(' ',strip=True))
check('25 project / training entries',len(docs['projects'].select('article[data-project-category]'))==25)
check('44 deduplicated credential records',len(docs['certifications'].select('article[data-cert-category]'))==44)
check('6 exact recommendations',len(docs['recommendations'].select('.testimonial-card'))==6)
check('17 about badges',len(docs['about'].select('.badge-card'))==17)
check('9 achievement badges',len(docs['projects'].select('.badge-gallery img'))==9)
new_links={a['href'] for d in docs.values() for a in d.select('a[href]')}
old_links={x for links in manifest['links'].values() for x in links if x.startswith(('https://','mailto:'))}
check('all historical outbound links retained',old_links.issubset(new_links),str(sorted(old_links-new_links)))
legacy=BeautifulSoup(Path('hands-on-experience.html').read_text(encoding='utf-8'),'html.parser')
check('preview-safe legacy redirect',legacy.select_one('meta[http-equiv="refresh"]')['content']=='0; url=projects.html')
check('original Formspree endpoint',docs['contact'].select_one('form')['action']=='https://formspree.io/f/mvgkvwpa')
check('no unsafe HTML sinks',not re.search(r'\b(innerHTML|outerHTML|insertAdjacentHTML|document\.write)\b',Path('main.js').read_text(encoding='utf-8-sig')))
ET.parse('sitemap.xml'); check('sitemap valid XML',True)
for path in Path('Images/optimized').rglob('*.webp'):
    with Image.open(path) as im: im.verify()
check('optimized images decode',True)
# Opaque theme token contrast. Browser QA measures actual rendered foreground/background pairs too.
def luminance(value):
    rgb=[int(value[i:i+2],16)/255 for i in (1,3,5)]
    values=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb]
    return sum(a*b for a,b in zip(values,[.2126,.7152,.0722]))
def contrast(a,b):
    x,y=sorted([luminance(a),luminance(b)]); return (y+.05)/(x+.05)
contrasts=[]
for theme,surfaces,colors,button_text in [('dark',['#080d17','#101a29','#132235','#173b40'],['#edf2fa','#a9b8cd','#8be0d4'],'#092126')]:
    for fg in colors:
        for bg in surfaces:
            ratio=contrast(fg,bg); contrasts.append({'theme':theme,'foreground':fg,'background':bg,'ratio':round(ratio,2)})
            check(f'{theme}: text contrast {fg} on {bg}',ratio>=4.5)
    check(theme+': filled button contrast',contrast(button_text,colors[-1])>=4.5)
Path('qa/contrast-results.json').write_text(json.dumps(contrasts,indent=2)+'\n',encoding='utf-8')
results={'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'checks':checks}
Path('qa/static-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f"Static QA: {results['passed']} passed, {results['failed']} failed")
for c in checks:
    if not c['passed']: print('FAIL:',c['check'],c['detail'])
sys.exit(bool(results['failed']))
