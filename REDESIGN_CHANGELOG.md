# Redesign changelog — 19 October 2026

Implemented in the existing checkout on `redesign/technical-support-portfolio`, based on `63a5cb3`. Rollback reference: `rollback/pre-support-redesign-63a5cb3`. The baseline tree matches the latest publicly observed deployment at `origin/main` / `22e1b27`; local main remains at `d05f3f1`. No commit, push, merge or deployment was made.

| File / group | Change |
| --- | --- |
| `index.html` | Support-focused hero and CTAs; Help Desk first; personal support approach; selected work, honest learning, support credentials and exact Tech Bridge recommendation. Responsive optimized portrait. |
| `about.html` | Human support story, transferable engineering background, current learning; preserved education and all 17 badges. |
| `experience.html` | Help Desk role first; retained five role titles/dates and all responsibilities; engineering detail moved into native disclosures. |
| `projects.html` | Six topic categories plus All, accessible feedback; all 24 original entries retained; one learning-only ServiceDesk Simulator entry; original public links and nine achievements preserved. |
| `skills.html` | Support practice leads; systems foundations, application investigation and existing QA/security skills follow; honest practical/knowledge/awareness/learning distinctions. |
| `certifications.html` | Six existing support/system/network courses promoted; 44 former cards map to 43 unique records in combined category/text search; original preview fragments preserved. |
| `recommendations.html` | Tech Bridge recommendation first; all six exact quotes/attributions and original recommender link preserved. |
| `contact.html` | Support positioning and subjects; public primary Gmail first, readable Discord username, persistent direct contact and original endpoint; no real delivery tests. |
| Eight page heads / shared markup | Consistent support-oriented SEO/social/schema, real historical jobTitle in Person data, relative assets, static active nav, accessible names, favicon and consistent footer. |
| `hands-on-experience.html` | Relative preview-safe redirect; original fallback and canonical retained. |
| `main.js` | System/persistent theme, storage guards, progressive menu, accessible filters, on-demand native dialog and focus handling, clipboard failure accuracy, timeout-aware provider-acceptance/error states. Small head-loaded initialization reserves mobile nav layout before paint. Dormant typing removed. |
| `style.css` | Consolidated theme/type/spacing/component tokens, calm navy/slate design, contrast-safe light/dark surfaces, visible focus, responsive layouts, reduced motion and print styles. Undefined token removed. |
| `sitemap.xml` | Lastmod updated only for the eight actually modified content pages, to 2026-10-19. |
| `Images/optimized/` | Two WebP portrait sizes and 50 on-demand display derivatives, about 3.73 MB total; originals untouched. 640px portrait is 32,798 bytes versus the 2,049,383-byte original. |
| `Images/favicon.svg` | Small dedicated initials favicon; original portrait retained. |
| `README.md` | Local preview, QA, shared conventions, evidence maintenance and publishing/rollback guidance. |
| `REDESIGN_CONTENT_DECISIONS.md` | Evidence rules, unresolved factual conflicts and complete 24-project / 44-preview source mapping. |
| `QA_REPORT.md`, `qa/` | Actual test results, screenshots, asset hashes, hosting/outbound checks, full measured Lighthouse outputs and per-file diff summary. |
| `scripts/`, `requirements-qa.txt` | Development-only static/browser/accessibility checks. No runtime framework, backend or production build added. |

All original images, certificate scans, badges, PDF, resume generator, robots and verification content remain byte-identical. Original evidence labels/URLs/quotes are archived in `qa/evidence-baseline.json`. All historical HTML routes remain independently available. The owner-provided `portfolio_redesign_handoff/` folder was read but not edited.

Validation: 1,367 static checks and 117 browser regression checks passed; zero page errors and zero detected axe violations. Detailed scope, local Lighthouse scores and untested items are in QA_REPORT.md. No claim of full manual WCAG conformance or production delivery is made.

Review with `git diff`, `git diff --stat` and the new-file inventory in `qa/redesign-diff-summary.txt`. New assets/docs are untracked until the owner commits the review branch. For release, confirm current remote Pages settings and approve the actual merge diff; for rollback, preserve the reference branch and use an approved revert instead of history rewriting. See README for the full workflow.

## Professional presentation refinement — 19 October 2026

- Refined the existing local redesign without replacing the previously uncommitted career content.
- Rebuilt the landing page with an ink-blue hero, restrained teal accents, a portrait panel, and a concise career overview.
- Replaced repeated homepage cards with an editorial experience list, distinct project covers, a compact credential list and a focused recommendation.
- Preserved support career positioning, historical roles, recommendation wording, resume and evidence assets.
- Improved shared typography, borders, button feedback and spacing while retaining light/dark themes and responsive navigation.
- Desktop and mobile visual review images: `qa/screenshots/polish-home-1440.png` and `qa/screenshots/polish-home-375.png`.
- No merge, push or deployment performed.

## Dark studio refinement — 19 October 2026

- Applied the owner-confirmed February 2025–October 2026 Help Desk dates to the homepage, experience hero, timeline and role details; changed the about-page employment description to past tense.
- Made all content routes dark-only in CSS and HTML; removed theme controls, saved-theme logic and OS-theme switching.
- Fixed the glass header at the top of desktop and mobile layouts and reserved space so it does not cover the opening content.
- Added a CSS 3D cube, orbit rings, floating support labels, fine-pointer tilt, subtle section entrance and project hover depth. No new runtime dependencies.
- Included motion pause/resume and OS reduced-motion handling.
- Updated QA scripts to cover dark-only behavior, fixed headers, motion controls and the approved date correction.
- Visually reviewed desktop and mobile captures under `qa/screenshots/dark-studio-*.png`. No push, merge or deployment performed.

## Full review and normal-flow header

- Removed fixed and sticky header behavior, offset transforms, reserved body spacing and oversized anchor offsets.
- Removed the no-JavaScript header height/overflow restriction, allowing the complete navigation to expand naturally.
- Fixed the inactive no-JavaScript motion button: it is now revealed only when its behavior is attached, and the scene is static without scripts.
- Expanded browser layout coverage from five to ten widths per page, including 1199/1200px navigation breakpoints and tablet boundaries.
- Added checks for header/content overlap on every route, full no-JavaScript navigation visibility and normal header scrolling.
- Updated README behavior documentation. No publishing action performed.

- Visual review caught and fixed the Recommendations heading breaking mid-word on phones; added a regression check and validated the updated page at four widths.
- Final review: 1,376 static checks, 102 browser checks, 7 targeted follow-up checks, 17 page/dialog accessibility audits and 2 updated-page accessibility audits passed. Visually reviewed all eight page introductions plus representative middle and closing sections.
