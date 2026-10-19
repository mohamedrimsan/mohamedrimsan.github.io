# Latest full review — header in normal flow

This review supersedes the fixed-header behavior described in the historical sections below.

- Header positioning: normal document flow on all eight content routes; it scrolls away with the document. Removed old body padding, horizontal offset transform and pinned-header anchor spacing.
- Fixed no-JavaScript navigation clipping by removing the height cap and overflow restriction.
- Fixed the no-JavaScript motion control: hidden until its handler is attached; the scene remains static when scripts are unavailable. Targeted follow-up checks pass at 320px and 1440px, with an additional working-control check in enhanced mode (`qa/followup-results.json`).
- Static checks: **1,376 passed, zero failures**.
- Responsive layout: **80 combinations passed** across eight routes at 320, 375, 640, 760, 768, 900, 1024, 1199, 1200 and 1440px. Header/content overlap and normal-flow positioning are checked on every route.
- Accessibility: **17 audits, zero detected violations**. These automated checks do not establish full accessibility conformance.
- Browser regression: **102 passed, zero failures, zero page errors** in Chrome and Firefox. Seven targeted follow-up checks also passed, with two fresh accessibility audits on the updated Recommendations page.
- Fixed the Recommendations title splitting mid-word on narrow screens; checked 320, 375, 640 and 1440px and visually reviewed updated screenshots.
- Full browser regression results are recorded in `qa/browser-results.json`; current screenshots for every route are under `qa/screenshots/`. Targeted visual review includes `review-home-desktop.png`, `review-home-mobile.png` and `review-no-js-320.png`.
- Syntax and whitespace checks pass. No production form submission, push, merge or deployment was performed.
- Local preview remains `http://localhost:8766/`.

---

# Dark-only portfolio QA — 19 October 2026

This section supersedes the earlier light/dark design checks retained below as historical context.

- Static validation: **1,376 passed, zero failures**, including evidence preservation with the owner-approved Help Desk date correction.
- Automated accessibility: **17 axe-core audits, zero detected violations** across all eight dark pages at desktop/mobile widths and the certificate dialog. Automated results do not establish full accessibility conformance.
- Visually reviewed the dark homepage on desktop and mobile. Captures: `qa/screenshots/dark-studio-top-1440.png`, `dark-studio-top-375.png`, and `dark-studio-overview.png`.
- Browser regression: **62 passed, zero failures, zero page errors** in Chrome and Firefox. Coverage now checks the dark-only theme despite a light OS/saved preference, fixed-header positioning, pause/resume controls, reduced-motion behavior, and responsive navigation. Final results are recorded in `qa/browser-results.json`.
- JavaScript syntax and whitespace checks pass. The public resume and recommendation quotations are preserved. Contact submissions are intercepted in the browser tests; no real message was sent.
- Preview: `http://127.0.0.1:8766/`. No commit, push, merge or deployment was performed for this refinement.

---

# Previous presentation validation — 19 October 2026

Review branch: `redesign/technical-support-portfolio`. Baseline `63a5cb3` has the same tree as deployed/tracking `origin/main` at `22e1b27`; local `main` is older at `d05f3f1`. No push, merge or deployment occurred. Local preview: `http://127.0.0.1:8765/` while its server is running.

## Presentation refinement validation

The homepage and shared style refinement was checked on 19 October 2026. All 1,387 static checks and 101 Chrome/Firefox browser checks pass, with zero page errors. A separate axe-core run completed 17 audits (all eight pages in desktop light and mobile dark, plus the open certificate dialog) with zero detected violations. Desktop and mobile homepage screenshots were visually reviewed. The in-app browser connection failed because its runtime sandbox could not start; the existing local Chrome/Firefox QA scripts were used for verification. Local preview for this refinement runs at `http://127.0.0.1:8766/`.

## Actual results

| Check | Result | Evidence / scope |
| --- | --- | --- |
| Static checks | PASS — 1387 checks; 0 failures | `qa/static-results.json`; local routes/case/fragments, metadata/schema, content preservation, asset hashes, image decoding and token contrast. |
| Browser regression | PASS — 101 checks; 0 failures | `qa/browser-results.json`; Chrome and installed Playwright Firefox. Zero page errors or missing local responses. |
| Chrome layout | PASS | All 8 content routes at 1440, 1024, 768, 375 and 320px, light and dark: 80 combinations, including responsive menu open/close. No horizontal overflow. |
| Firefox | PASS | All 8 routes at 375px dark; menu/Escape and native certificate dialog/focus return. Other Firefox widths/themes are not tested. |
| Keyboard | PASS within scripted paths | Skip link, main focus, menu, Escape, outside click/focus, filter controls, native disclosure and certificate open/close/Tab/Shift+Tab/focus restore. |
| Theme | PASS | System → Light → Dark → System, persistence across pages, OS preference changes and unavailable storage. |
| Project filters | PASS | Every category, selected-state semantics, visible entries and result count; 25 entries including learning-only ServiceDesk Simulator. |
| Credential search | PASS | Combined text/category, 43 unique records, empty response, search reset and HTML-like input safety. |
| Certificate previews | PASS | All 50 distinct preview links across Projects/Credentials load and decode; named dialog, close button, focus containment/return, Escape/backdrop, scroll unlock. No certificate image requests before opening. |
| No JavaScript | PASS | At 320px, all 8 navigation links and page content available; 25 project entries, 43 credential records, direct original-scan links and native form semantics. No submission made. |
| Motion / zoom / reflow | PASS for tested proxies | Reduced-motion disables smooth scroll; all 8 pages pass 200% CSS zoom. 640px layout reflow proxy passes. Browser chrome zoom, real-device pinch/touch and actual assistive technology are not tested. |
| Clipboard | PASS | Mocked Clipboard API success/denial and legacy execCommand true/false. False never announces success; visible username remains available. Real clipboard permissions across user devices are not tested. |
| Contact form | PASS with interception only | Required/native validation; mocked provider acceptance, 422 rejection, network failure and timeout. Inputs retained after uncertainty/failure; controls restored. Success means provider acceptance, not delivery. Zero production submissions. |
| Downloads / legacy | PASS | Native download bytes match the original PDF. Legacy redirect stays on the local preview host. |
| Verification / originals | PASS | robots.txt, Google verification, resume PDF, generator, all 89 original raster assets byte-identical. 17 About badges, 9 linked achievements, all 24 original projects and 6 exact recommendations retained. |
| JS / Git / sitemap | PASS | `node --check main.js`, `git diff --check`, structured JSON-LD parse and XML sitemap parse. |
| Limited source scan | PASS within stated scope | 36 changed/new text files; zero PEM-private-key/AWS-ID pattern findings. No exhaustive history/entropy scan, PDF metadata/OCR or independent credential/experience verification. |

## Accessibility measurements

Final regression axe-core 4.10.3 checks cover WCAG 2.0/2.1/2.2 A/AA tags on all eight desktop pages in both themes, with zero detected violations. A separate 17-audit pass covers desktop light / 375px dark and the open certificate dialog (`qa/accessibility-results.json`), also with zero detected violations. Token luminance ratios are recorded in `qa/contrast-results.json`; ordinary text/secondary/accent pairs meet 4.5:1 on all four intended surfaces in both themes. Axe measured rendered contrast and semantics in the tested states.

These automated results do not certify complete WCAG 2.2 AA conformance. Manual screen-reader review, all dynamic error states in axe, browser chrome zoom, forced-colors rendering and real touch devices remain not tested. Axe incomplete/manual-review items are retained in the JSON reports.

## Lighthouse — measured, local simulated mobile

Lighthouse 12.8.2 on the loopback Python HTTP server, with Chrome. These are real local measurements, not production scores.

| Page | Performance | Accessibility | Best practices | SEO | LCP | CLS |
| --- | --- | --- | --- | --- | --- | --- |
| index.html | 92 | 100 | 82 | 100 | 2.9 s | 0.000 |
| projects.html | 80 | 100 | 82 | 100 | 3.3 s | 0.079 |
| certifications.html | 76 | 100 | 82 | 100 | 3.6 s | 0.102 |
| contact.html | 76 | 100 | 82 | 100 | 4.0 s | 0.000 |

Full reports: `qa/lighthouse-{index,projects,certifications,contact}.json`; compact metrics: `qa/lighthouse-summary.json`. No Lighthouse runtime errors. A mobile menu collapse initially shifted the page substantially; reserving its layout before first paint removed that shift on Home/Contact and reduced it on the other pages. Credentials still measured CLS 0.102 and performance 76; it does not meet an aspirational 90 performance score. Remaining filter/icon loading reflow and the long archive merit further performance review under clean production-like conditions.

The host antivirus injected approximately 203 KB of additional blocking JavaScript and extra HTTP requests into local pages. Those requests account for the insecure-request finding; no security-software setting was changed. Machine-specific injected request/session URLs were redacted from review artifacts while scores/metrics were left unchanged. The shared QA machine, external Font Awesome CSS/font loading, local HTTP without production compression/cache headers, and simulated throttling affect these measurements. Do not infer production HTTPS/cache behavior or Core Web Vitals from this run. The homepage no longer requests its unused external icon stylesheet.

## Public links and hosting

Read-only HTTP checks are in `qa/outbound-links.json` and `qa/hosting-checks.json`. 14 of 18 historical outbound URLs returned HEAD 200, including the nine reward links, LetsDefend profile, AssureX, GitHub, portfolio and WhatsApp. LinkedIn endpoints returned 405, TryHackMe returned 429 and PicoCTF DNS resolution failed. These four destinations remain not fully verified; the original URLs were preserved. A successful HEAD only establishes reachability. AssureX GET returned 200 at `/signin`; authenticated demo behavior and project ownership are not tested.

Public deployment/Actions records identify main at `22e1b27`; the exact Pages settings endpoint returns unauthenticated 404. Publishing folder, Formspree ownership/delivery, mailto delivery, WhatsApp/Discord account behavior and credential issuer authenticity are not tested. All original contact routes and the Formspree endpoint remain unchanged.

## Visual review and reproducibility

Six full-page review screenshots were captured: Home light/dark at 1440px, Home light at 375px, Projects light, Credentials light and Contact dark. See `qa/screenshots/`. Desktop/Home/mobile/Contact images were visually inspected in addition to the automated viewport checks. All screens are local preview renders.

Run the commands in README. `scripts/verify_site.py`, `scripts/browser_qa.py --axe` and `scripts/accessibility_qa.py` write their results into `qa/`. The browser runner intercepts every Formspree request. The in-app Browser skill was read and its connection attempted twice; startup failed with the sandbox setup error. Local headless Chrome/Firefox supplied the actual browser evidence instead. Ordinary shell startup also failed; approved fallback execution was used. No failed startup is reported as a passing test.

## Remaining owner confirmations

See `REDESIGN_CONTENT_DECISIONS.md`: official trainee title, administrative dates/employer styling, current Help Desk/project/education status, employment arrangement, public-channel and existing image/testimonial permissions, future resume updates, issuer links and authenticated Pages/Formspree configuration. Published facts were retained pending confirmation. Publishing is outside this implementation and still requires explicit owner approval.
