"""Check the current static site without historical audit files or Git refs."""

import json
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
from PIL import Image

from qa_helpers import OUTPUT_DIR, PAGES, ROOT


def main():
    checks = []
    documents = {
        file: BeautifulSoup(file.read_text(encoding="utf-8-sig"), "html.parser")
        for file in ROOT.glob("*.html")
    }

    def check(name, condition, detail=""):
        checks.append({"check": name, "passed": bool(condition), "detail": detail})

    def local_reference(source, value):
        url = urlsplit(value)
        if url.scheme or url.netloc:
            return
        if url.path:
            target = ROOT / unquote(url.path).lstrip("/") if url.path.startswith("/") else source.parent / unquote(url.path)
        else:
            target = source
        target = target.resolve()
        label = f"{source.relative_to(ROOT)}: {value}"
        inside_root = target.is_relative_to(ROOT)
        check(label + " stays inside site", inside_root)
        if not inside_root:
            return
        check(label + " exists", target.is_file())
        if not target.is_file():
            return
        cursor = ROOT
        exact_case = True
        for part in target.relative_to(ROOT).parts:
            exact_case = exact_case and part in {item.name for item in cursor.iterdir()}
            cursor /= part
        check(label + " uses exact case", exact_case)
        if url.fragment and target.suffix == ".html":
            check(label + " fragment exists", documents[target].find(id=unquote(url.fragment)) is not None)

    expected_navigation = [page + ".html" for page in PAGES]
    for page in PAGES:
        file = ROOT / (page + ".html")
        document = documents[file]
        ids = [tag["id"] for tag in document.select("[id]")]
        check(page + ": unique IDs", len(ids) == len(set(ids)))
        check(page + ": landmarks", len(document.select("main")) == 1 and len(document.select("h1")) == 1)
        check(page + ": language", document.html.get("lang") == "en")
        nav = document.select_one("#primary-navigation")
        check(page + ": consistent navigation", nav is not None and [link.get("href") for link in nav.select("a")] == expected_navigation)
        active = document.select('nav a[aria-current="page"]')
        check(page + ": active route", len(active) == 1 and active[0].get("href") == file.name)
        check(page + ": skip link", document.select_one('a.skip-link[href="#main-content"]') is not None)
        metadata = ["title", 'meta[name="description"]', 'link[rel="canonical"]', 'meta[property="og:title"]', 'meta[name="twitter:title"]']
        check(page + ": metadata", all(document.select_one(selector) for selector in metadata))
        structured_data = document.select('script[type="application/ld+json"]')
        check(page + ": structured data", bool(structured_data))
        for tag in structured_data:
            try:
                json.loads(tag.string or "")
                check(page + ": valid JSON-LD", True)
            except ValueError as error:
                check(page + ": valid JSON-LD", False, str(error))
        check(page + ": shared module", document.select_one('script[type="module"][src="assets/js/main.js"]') is not None)
        for image in document.select("img"):
            check(page + ": image alt", image.has_attr("alt"))
            check(page + ": image dimensions", image.has_attr("width") and image.has_attr("height"))
        for link in document.select('a[target="_blank"]'):
            check(page + ": safe new tab", {"noopener", "noreferrer"}.issubset(link.get("rel", [])))
        for link in document.select("a[data-certificate]"):
            check(page + ": certificate fallback", link.get("target") == "_blank" and bool(link.get("data-certificate")))

    for file, document in documents.items():
        for tag in document.select("[href], [src], [action], [data-preview]"):
            for attribute in ("href", "src", "action", "data-preview"):
                if tag.has_attr(attribute):
                    local_reference(file, tag[attribute])
        for tag in document.select("[srcset]"):
            for candidate in tag["srcset"].split(","):
                local_reference(file, candidate.strip().split()[0])

    for file in (ROOT / "assets/css").rglob("*.css"):
        for match in re.finditer(r"url\(\s*['\"]?([^'\"\s)]+)", file.read_text(encoding="utf-8")):
            local_reference(file, match[1])
    for file in (ROOT / "assets/js").rglob("*.js"):
        for match in re.finditer(r"\bfrom\s+['\"]([^'\"]+)['\"]", file.read_text(encoding="utf-8")):
            check(str(file.relative_to(ROOT)) + ": relative module import", match[1].startswith("."))
            local_reference(file, match[1])

    legacy = documents[ROOT / "hands-on-experience.html"]
    redirect = legacy.select_one('meta[http-equiv="refresh"]')
    check("preview-safe legacy redirect", redirect is not None and redirect.get("content") == "0; url=projects.html")
    check("native contact form", documents[ROOT / "contact.html"].select_one('form[method="POST"][action="https://formspree.io/f/mvgkvwpa"]') is not None)
    try:
        sitemap = ET.parse(ROOT / "sitemap.xml")
        locations = {tag.text for tag in sitemap.findall(".//{*}loc")}
        expected = {"https://mohamedrimsan.github.io/" + (page + ".html" if page != "index" else "") for page in PAGES}
        check("sitemap covers public pages", expected.issubset(locations))
    except ET.ParseError as error:
        check("sitemap valid XML", False, str(error))
    for file in (ROOT / "Images/optimized").rglob("*.webp"):
        try:
            with Image.open(file) as image:
                image.verify()
            check(str(file.relative_to(ROOT)) + ": image decodes", True)
        except (OSError, ValueError) as error:
            check(str(file.relative_to(ROOT)) + ": image decodes", False, str(error))

    results = {"passed": sum(item["passed"] for item in checks), "failed": sum(not item["passed"] for item in checks), "checks": checks}
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "static-results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Static QA: {results['passed']} passed, {results['failed']} failed")
    for item in checks:
        if not item["passed"]:
            print("FAIL:", item["check"], item["detail"])
    return bool(results["failed"])


if __name__ == "__main__":
    sys.exit(main())
