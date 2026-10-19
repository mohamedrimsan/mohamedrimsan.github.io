# Mohamed Rimsan — Technical Support Engineering Portfolio
## Redesign Blueprint (based on PORTFOLIO_CODEBASE_AUDIT.md, 19 Oct 2026)

**Source of truth:** User-provided repository audit, not a fresh checkout or rendered-browser audit. **Live website:** https://mohamedrimsan.github.io/ · **Source repository:** https://github.com/mohamedrimsan/mohamedrimsan.github.io

## 1. Design decision

**Restructure existing multipage HTML, CSS and vanilla JavaScript rather than migrate to React/Next.js.** Preserve GitHub Pages deployment compatibility, existing filenames/routes, assets, rich long-form evidence and SEO value. Keep production untouched until a reviewed, tested diff is approved. Existing local checkout is on `qa-security-engineer-version` at `63a5cb3`; recent GitHub Pages deployments were from `main`. Reconcile branches and verify the actual publishing settings before any merge/push.

## 2. Professional identity and evidence model

**Primary identity (career positioning, not a retroactive job title):** Technical Support Engineering | IT Support & Service Desk | Systems & Application Support | IT Operations.

**Primary evidence:** Help Desk Representative at Tech Bridge Solutions Ltd (Feb 2025–present in website audit): remote troubleshooting, user guidance, incident/service request documentation, escalation, status updates and issue follow-through.

**Transferable engineering evidence:** QA & Security Engineer Intern (Mar–Jun 2026) and QA & Security Engineer Trainee (Jul–Sep 2026) at SAĜO MENTE: application troubleshooting, defect reproduction, API validation, logs/deployment checks, coordination and structured documentation. Retain official titles and history, and do not re-label these as support-engineering jobs.

**Secondary evidence:** AssureX (site says completed), VeriGuard and MailForge (site says in progress), portfolio engineering, selected cloud/security labs and job simulations. Preserve dates/statuses as current website claims until approved. ServiceDesk Simulator was mentioned by the owner as training: show as ongoing learning **only if** an accurate participation description is approved; do not fabricate completed tickets, simulations or badges.

**Do not publish unverifiable claims:** invented ticket counts, first-contact resolution, CSAT, SLA percentages, infrastructure administration experience, unsupported Microsoft 365/Active Directory competence or private client data.

## 3. Visual specification

**Design language:** premium enterprise support/operations, calm and trustworthy rather than hacker/neon sci-fi. Consistent dark/light theme with a navy/slate base, restrained cyan accent, readable typography, subtle technical linework and generous spacing. Suggested tokens to refine against actual WCAG contrast tests:

| Role | Dark | Light |
|---|---|---|
| Background | `#0B1423` | `#F6F8FC` |
| Surface | `#14243A` | `#FFFFFF` |
| Text | `#F3F7FC` | `#142238` |
| Secondary text | `#B7C9DA` | `#475569` |
| Accent | `#67D8F4` | `#075985` |
| Border | `#2B425A` | `#D7E1EA` |

Use a deliberate system font stack or properly self-hosted fonts; current CSS declares Inter/Space Grotesk without actually loading either. Type: bold but compact hero, accessible 16px+ copy, 1.5–1.7 line-height, legible labels. Use semantic cards, consistent spacing tokens, restrained icons, CSS gradients rather than heavyweight hero imagery. Keep portrait as a real image only if approved; optimize derivatives, never modify/delete originals.

**Homepage content order:**

1. Compact fixed or sticky header with safe mobile navigation and clear contact/resume action.
2. Hero: name, Technical Support Engineering positioning, short plain-English value statement, evidence-aware CTA (“Explore Experience”, “Projects & Labs”, “Contact”). Location and genuine portfolio contacts only.
3. Three proof pillars: End-User Support; Incident & Application Troubleshooting; Systems & Infrastructure Foundations—each connected to real activities and not fabricated statistics.
4. Featured experience: Help Desk first; previous QA/security engineering framed as transferable skills.
5. “How I approach support issues”: understand → diagnose → respond or escalate → document/follow through. Label as approach, not measured job performance.
6. Skills strip: Windows/Linux, networking fundamentals, incident handling/documentation, API and application debugging, relevant AWS exposure; mark learning-only platforms as learning.
7. Featured proof: ServiceDesk Simulator (in progress if approved), AssureX (existing completed claim), selected investigations/VeriGuard/MailForge (in progress).
8. Relevant credentials: Technical Support Fundamentals, Practical Help Desk, Networking Basics, Computer Hardware Basics, Operating Systems, System Administration; all issuer/date/status copied from audited source.
9. Genuine recommendation excerpt from Tech Bridge MD followed by link to Recommendations. Keep quotation verbatim.
10. Closing contact CTA and complete footer.

**Page-by-page scope (preserve routes):**

| Route | New priority | Must preserve |
|---|---|---|
| `/` and `index.html` | Support-first recruiter landing | Portrait option, resume, links, strong QA/security background |
| `about.html` | Human introduction; support journey and education | BSc details, authentic badges, values |
| `experience.html` | Help Desk featured first; accurate chronology | 5 roles, title/date caveats, detailed technical evidence |
| `projects.html` | Tabs/filters: Support & Labs, Applications, QA & Security, Simulations | Existing 24 items, badges, demo links, status distinctions; add ServiceDesk entry only if supported |
| `skills.html` | Support → OS/Networking → Apps/Cloud → prior QA/Security | Honest Practical/Working Knowledge/Currently Learning labels |
| `certifications.html` | Support/IT/Networking featured, full searchable archive | Existing scans, issuer/date labels, combined search/filter; remove duplicate display, not evidence |
| `recommendations.html` | Genuine social proof; Tech Bridge quote prominent | All 6 quotes exactly, attribution, known links |
| `contact.html` | Recruiter-friendly direct contact + reliable form | Gmail, GitHub, LinkedIn, resume, optional WhatsApp/Discord, Formspree until verified |
| `hands-on-experience.html` | Legacy compatibility redirect | Same URL, sensible relative preview-friendly navigation |
| Google verification HTML | No public redesign | Preserve exact file/content |

## 4. Technical architecture

- Keep root HTML static pages and current `.html` URLs. Implement shared tokens/utilities in `style.css`; modularize JS behavior with small functions and event delegation where useful. A build step is **optional** only if it produces identical static routes and justified maintainability.
- Avoid copying entire headers/footers blindly: either enforce one shared snippet workflow that emits static HTML or maintain reusable conventions/documented checklists with minimal runtime dependencies.
- Maintain existing class/data hooks or migrate all pages and JS atomically; test the filter, certificates, native `<details>` and form after each page.
- Light/dark theme toggle with system preference, persistence and no-JS accessible default. `prefers-reduced-motion` support; no required decorative animation.
- Project filters and credential search must have accessible `aria-pressed`, result counts, empty-state messages and logical keyboard focus.
- Rebuild image previews with `<dialog>` or equivalent accessible dialog: keyboard open/close, focus entry/return, Escape and backdrop dismissal, scroll management.
- Progressive enhancement for hamburger menu so key navigation remains available if scripts fail; `aria-current`, `aria-controls`, `aria-expanded`, visible focus and proper keyboard use.
- For images, keep original 89 assets in place; add compressed WebP/AVIF or properly sized derivatives, lazy-load below-fold files, defer full certificate scans to preview. Preserve correct filenames and path case.
- Do not inject user input into `innerHTML`; keep third-party dependencies minimal, outbound links safe, Formspree key configuration intact (public routing ID is not a secret).
- Keep `Resume/AR-Mohamed-Rimsan-Resume.pdf` working. The existing PDF and generator are QA-centric; **do not silently regenerate or rename** until an updated support-focused resume is supplied/approved.
- Update each page's title/description/Open Graph/Person or ProfilePage schema and sitemap after content is approved. Preserve `robots.txt` and Google verification.

## 5. Critical content issues from audit

1. **Trainee title conflict:** website says “QA & Security Engineer Trainee”; `Resume/generate_resume.py` says “QA & Security Engineer.” Preserve the current website label until owner confirms.
2. **Administrative employment date conflict:** website Jun–Dec 2021 vs generator May–Nov 2021. Preserve current site copy pending confirmation.
3. **Help Desk work arrangement:** website says remote Feb 2025–present, generator adds part-time; a later resume version differs. Don't choose an unverified arrangement.
4. **Contact mismatch:** `mailto:mohamed.rimsan.ar@gmail.com` but main.js form error mentions `mohamed.rimsan@outlook.com`. Use the primary publicly displayed Gmail in visible contact copy unless owner says otherwise; do not change the Formspree provider or submit production forms as a test without consent.
5. **Competency scope:** Windows/Linux/networking fundamental vs deep sysadmin; Microsoft 365, Entra ID and AD are learning goals unless experience is evidenced.
6. **Certificate record duplication:** Accelerate Your Job Search with AI appears twice; use one data item in appropriate filter categories.
7. **Recommendations:** Six actual quotations; preserve exact wording and attribution.
8. **Legacy SEO:** sitemap `lastmod` is stale; only update dates for truly changed pages and preserve verification.

## 6. QA, accessibility and release gates

**Quality baseline:** existing audit performed local structural and HTTP checks, but **no browser renders, screenshots, Lighthouse or form delivery tests**. New implementation must actually run them before claiming success.

**Test matrix:** Chrome/Chromium + Firefox or WebKit as available; 320/375/768/1024/1440px; dark/light/system themes; mouse, keyboard, touch; JS disabled; 200% zoom and reduced motion. Check every link and image, header/footer, active nav, mobile menu, long titles, dropdowns, project filtering, certificate search/modal, email copy, downloads and page transitions.

**Accessibility:** WCAG 2.2 AA target, particularly text contrast (audit measured cyan-on-white at 2.14:1), labels, status announcements, dialog focus handling, hit-target size and no hidden overflow. Color contrast must be **measured** on rendered elements.

**Performance:** measured Lighthouse as available (aspirational 90+ categories, not assumed); optimize heavy portrait/certificate assets and request waterfalls, audit privacy/third-party fonts, ensure minimal CLS.

**Security:** no secrets, no customer tickets/screenshots without sanitization and authorization, don't invent certificates, no unsafe DOM injection, no misleading form-success state, no unnecessary dependencies.

**Release process:** start from a clean, reviewed branch; preserve `main` production; output a per-file diff, screenshot set, issues list, test results and rollback path; do **not** push/merge/deploy until user expressly approves. Confirm GitHub Pages deployment source (public evidence indicates main/root but authenticated settings were unavailable).

## 7. Implementation phases

**P0** Audit confirmation and factual content matrix; inventory of routes/assets and clean baseline commit.

**P1** Design tokens + header/footer + responsive hero, local staging preview.

**P2** Homepage/About/Experience, accurate support-led writing, featured recommendation.

**P3** Skills, project filters and status taxonomy; add ServiceDesk Simulator as ongoing practice only when evidence exists.

**P4** Certifications/previews, testimonials, contact handling, asset derivatives.

**P5** Browser QA, accessibility/performance, security review, SEO, README, diff and deployment handoff.

### Definition of done

All eight existing substantive pages work, every existing route is preserved, the new identity is consistent, historical roles are accurate, no unsubstantiated support claims appear, interactive controls are keyboard/mobile usable, images are optimized without deleting original evidence, content and metadata agree, contact/resume links work, and a test report and reviewable diff are available. Production remains unchanged pending explicit approval.
