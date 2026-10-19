# Mohamed Rimsan — Technical Support Engineering

A static, multipage professional portfolio. The redesign brings remote Help Desk experience forward while retaining the original QA/security roles, projects, credentials and recommendations. HTML, CSS and vanilla JavaScript are served directly by GitHub Pages; there is no production build, framework or backend.

## Preview locally

From the repository root, run:

```powershell
python -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. Stop with Ctrl+C. Every `.html` route works independently. The legacy `hands-on-experience.html` redirects to the local Projects page. No-JS navigation, evidence links, native disclosures, resume download and contact form remain available. The site uses a dark-only design with a header that scrolls with the page. The homepage uses a cyan, violet and coral palette, a floating 3D portrait panel, a rotating CSS cube and responsive card layouts. Animations run automatically and respect reduced-motion preferences.

## Structure

- Eight root pages: Home, About, Experience, Projects, Skills, Credentials, Recommendations and Contact.
- `style.css`: theme, typography, layout, shared components, responsive and reduced-motion rules.
- `main.js`: progressive navigation, automatic 3D animations and pointer tilt, reduced-motion-aware section entrances, filters, clipboard feedback and contact status handling.
- `Images/optimized/`: portrait and on-demand certificate display derivatives; originals in `Images/`, `Badges/` and `Certificates/` are preserved.
- `Resume/AR-Mohamed-Rimsan-Resume.pdf`: unchanged public download. The generator is separate from publishing; do not run it to update this resume without approved content.
- `robots.txt`, `sitemap.xml`, `googlec5a2878c58ee90d7.html`: crawling and verification resources.
- `REDESIGN_CONTENT_DECISIONS.md`: factual decisions, outstanding confirmations and complete original project/credential mapping.
- `REDESIGN_CHANGELOG.md`, `QA_REPORT.md`, `qa/`: change summary, measured QA results, evidence hashes and screenshots.
- `scripts/verify_site.py`, `scripts/browser_qa.py`, `scripts/accessibility_qa.py`: repeatable static and local browser checks.
- `portfolio_redesign_handoff/`: owner-provided audit, blueprint and implementation prompt; reference material, not a production build input.

## QA

Optional development dependencies only:

```powershell
python -m pip install -r requirements-qa.txt
python scripts/verify_site.py
node --check main.js
python scripts/browser_qa.py --axe
python scripts/accessibility_qa.py
```

The browser runner uses installed Chrome and, when present, a Playwright Firefox build. Install browsers for your development environment with `python -m playwright install chromium firefox` if needed; adapt the Chrome channel in the script if only bundled Chromium is installed. `--axe` fetches pinned axe-core 4.10.3 for the local audit. The runner creates a temporary loopback server and records JSON results and screenshots. All Formspree requests are intercepted, including acceptance, rejection and network failure tests; no actual message is sent. Production delivery is a separate, explicitly authorized check.

See `QA_REPORT.md` for actual test scope, environment limitations and numerical results. Automated accessibility checks do not establish full WCAG conformance. Browser chrome zoom, assistive technology, real touch devices and authenticated external services require separate review.

## Maintenance

Keep shared headers, nav links and footers consistent across all eight static documents. Set `aria-current="page"` in HTML, preserve `primary-navigation`, and keep menu/filter buttons progressively enhanced. The static QA script checks this convention, so a build-time template system is unnecessary for this site.

Project categories are space-separated `data-project-category` values; each entry has an existing work type/status. Add only substantiated public evidence. Credential categories use `data-cert-category`; optional searchable issuer/date text is in `data-cert-search`. Certificate anchors open the original scans directly in a new tab using `target="_blank"` and `rel="noopener noreferrer"`. Keep `data-certificate` as the record label and use an accessible label that identifies the certificate and new tab. Keep legacy IDs if records are moved/deduplicated. The original archive and SHA-256 hashes are in `qa/evidence-baseline.json`.

The small shared script loads in the head and attaches progressive navigation, filters and section entrances when the document is ready. Dark colors are defined in CSS and `data-theme="dark"` is present in HTML, so OS preferences and previous saved theme choices do not change the appearance. There is no theme selector. The header stays in the normal document flow at every screen size. It scrolls away with the page, and no extra space is reserved for a pinned header. Without JavaScript, navigation expands naturally and all links remain available.

The homepage portrait uses responsive WebP sources and a compact horizontal card on phones. Its profile link opens the About page. The shared layout keeps content within a 1200px container and adapts navigation, cards and section grids for smaller screens. Animations and pointer tilt are disabled when the operating system requests reduced motion. Without JavaScript, the decorative scene stays static.

Certificate scans open in one step using native links, with no intermediate preview dialog. This also works without JavaScript.

Keep the original professional role titles, employment dates, issuer metadata, recommendation wording and public contact methods until owner-confirmed corrections are available. Support positioning is not a replacement for actual historical titles. Microsoft 365, Active Directory and cloud administration remain learning goals. Never add invented support metrics or confidential workplace materials.

When making real content changes, update that page's title, description, OG/Twitter metadata, JSON-LD and sitemap lastmod together. Preserve canonical production URLs while keeping navigation and assets relative. All modified page dates currently use 19 October 2026 (Asia/Colombo).

## Publishing and rollback

The review branch is `redesign/technical-support-portfolio`, based on `qa-security-engineer-version` at `63a5cb3`. The rollback reference is `rollback/pre-support-redesign-63a5cb3`. Nothing has been pushed, merged or deployed. Local `main` is older (`d05f3f1`) and differs from the starting branch; `origin/main` is `22e1b27` and has an identical tree to `63a5cb3`. Inspect `qa/baseline-vs-main.txt` and the full diff against the current remote publishing branch before a release.

Public deployment records and the local tracking ref agree on `main`, most recently `22e1b27`; authenticated Pages settings and publishing folder have not been confirmed. Before any publishing, the owner must approve the final changes and confirm Settings → Pages. Do not assume a push to the review branch publishes, or switch publishing branches as part of a redesign.

Review with `git status --short`, `git diff --stat`, `git diff --check` and `git diff -- <file>`. New untracked review artifacts must also be inspected. Commit the approved review changes on the review branch before a separately authorized merge/push. Keep the rollback branch. If a published redesign needs rollback, use an owner-approved revert of the release commit (or merge revert) on the publishing branch; do not force-push or rewrite history. Preserve the current PDF, verification resource and all historic routes throughout release and rollback.

The Google IT Support Professional Certificate is listed as in progress (March 2026–February 2027, expected completion) on Home, About and Credentials. The credential archive contains 44 learning entries; the new program has no completion or certificate-preview claim.
