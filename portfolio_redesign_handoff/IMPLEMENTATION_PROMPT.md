# MASTER IMPLEMENTATION PROMPT — REDESIGN THE EXISTING MOHAMED RIMSAN PORTFOLIO

You are the principal frontend engineer, UX designer, technical writer, SEO specialist and accessibility/QA reviewer assigned to redesign an **existing** professional portfolio repository. You can read and edit the checked-out files. **Implement actual code changes**; do not stop at wireframes or generate an unrelated replacement site.

## Context

- **Live:** https://mohamedrimsan.github.io/
- **Repository:** https://github.com/mohamedrimsan/mohamedrimsan.github.io
- **Owner:** Mohamed Rimsan (existing site also styles the name as AR. Mohamed Rimsan)
- **Current strategic career identity:** Technical Support Engineering | IT Support & Service Desk | Systems & Application Support | IT Operations.
- **Historical roles:** Help Desk Representative (Tech Bridge Solutions Ltd, remote, Feb 2025–present according to checked-in site); QA & Security Engineer Intern (SAĜO MENTE, Mar–Jun 2026); QA & Security Engineer Trainee (SAĜO MENTE, Jul–Sep 2026). Do not relabel actual titles.
- **Evidence:** Existing real project claims include AssureX, VeriGuard and MailForge; security labs and simulations; six professional recommendations and dozens of certificate previews. The owner has additionally mentioned ongoing ServiceDesk Simulator training. Do not imply specific exercises are completed without evidence.
- **Audit:** `PORTFOLIO_CODEBASE_AUDIT.md` dated 19 Oct 2026. Read this audit, the actual codebase, and the attached `REDESIGN_BLUEPRINT.md` before edits. The audit found eight complete HTML pages, one legacy redirect, one Google verification file, `style.css` (~2,760 lines), `main.js` (~7.1KB), 89 raster images and a public resume. The audit did **not** successfully render pages or confirm the Formspree delivery.
- **Git:** Audit inspected `qa-security-engineer-version` at `63a5cb3`, whereas recent Pages deployment was from `main`. Verify the current branch, remote, `git status`, exact diff vs main and actual deployment settings; do not make assumptions.

## Immutable safety rules

1. Never push, merge, deploy, rewrite history or modify `main` without explicit approval. Work on a separate review branch. Preserve a rollback point and output a complete diff summary.
2. Don't create a separate website and pretend the original was upgraded. Work with the real checkout, keeping valid files/assets and exact GitHub Pages route compatibility.
3. No fabricated professional experience, support metrics (SLA/CSAT/ticket counts), skills, credentials, dates, projects, repositories or testimonials. Mark learning clearly. Treat the audit's `source-confirmed` as repository content, not independent verification.
4. Keep original professional role titles and conflicting facts unchanged pending human confirmation: QA Trainee vs Engineer, Administrative Assistant dates, Help Desk employment arrangement and official employer naming.
5. Do not expose customer ticket data, client details, internal hostnames, work screenshots, secrets, confidential findings or private materials.
6. Preserve `googlec5a2878c58ee90d7.html`, `robots.txt`, public resume URL, certificate assets, badges, all historically published HTML routes, recommendations and verified outbound links.
7. Don't run production Formspree submission tests or publish contact changes without permission. The primary visible address is `mohamed.rimsan.ar@gmail.com`; code currently also contains an inconsistent Outlook fallback.
8. If you cannot run a test, label it **not tested**. Never invent Lighthouse scores, screenshots or passing results.
9. Do not use a heavy framework, runtime API, backend or paid dependency unless demonstrated essential. Static HTML/CSS/JS is sufficient and preferred.

## Step 0 — Repository baseline and content reconciliation

- Read every HTML file, `style.css`, `main.js`, README, robots, sitemap, generator and all relevant asset folders.
- Confirm actual branch and clean state; compare to deployment branch `main`. Start from the correct owner-approved baseline and create `redesign/technical-support-portfolio` or equivalent review branch.
- Read audit chapter 18 for outstanding factual conflicts. Create `REDESIGN_CONTENT_DECISIONS.md`, listing what is confirmed, retained-as-is, learning-only, missing, or blocked pending owner confirmation.
- Map all 24 existing project/lab/simulation entries and all credential previews to new locations, with no content loss. Back up labels, link URLs, certificate paths and testimonial text.
- Preserve existing fallback/redirect behavior before refactoring; check direct link access for all `.html` URLs.

## Step 1 — Design and UI system

Design a professional enterprise-IT website. Use premium navy/slate, subtle teal/cyan accents and clean white/light surfaces. Avoid neon hacker art, fake SOC dashboards, generic startup filler and overlong walls of text.

Suggested starting values (adjust to pass real contrast checks):

- Dark background `#0B1423`, surface `#14243A`, text `#F3F7FC`, accent `#67D8F4`.
- Light background `#F6F8FC`, surface `#FFFFFF`, text `#142238`, accent `#075985`.
- Typography: intentional system UI or properly loaded Inter/Space Grotesk; accessible sizes/line-heights.
- Components: header, mobile nav, page intros, hero, cards, badges, timelines, project filters, credential previews, footer and strong contact CTAs.
- CSS custom-property tokens for themes, spacing, type scale, radius, border, shadow and focus-ring colors.
- Add persistent user-controlled light/dark theme respecting system theme and reduced motion. With no JS, content and navigation must remain usable.
- Use original portrait only if publication permission still applies; create appropriately sized responsive derivatives without changing original scans.

## Step 2 — Content and navigation architecture

Keep:
`index.html`, `about.html`, `experience.html`, `projects.html`, `skills.html`, `certifications.html`, `recommendations.html`, `contact.html`, `hands-on-experience.html` (redirect) and Google verification file. All must resolve independently under GitHub Pages. Main navigation may group secondary pages, but no pages can become unreachable.

**Homepage**
- Main positioning: “Technical Support Engineering” with clear supportive subheading and concise human description tied to actual Help Desk responsibilities.
- Prominent CTAs: View Experience, Projects & Labs, Contact Me, Download Resume (existing valid public path).
- Evidence-aware service pillars: user support, troubleshooting, issue documentation/escalation; no invented metrics.
- Feature Tech Bridge Solutions Help Desk experience first. Include concise reference to previous SAĜO MENTE QA/Security engineering work as transferable investigation/deployment discipline.
- Describe a **personal support approach**: understand symptoms → reproduce/diagnose → resolve/escalate → document and follow through. This is not a claim of company-standard workflow.
- Feature approved ongoing ServiceDesk Simulator training without pretending the participant has finished every exercise.
- Feature selected existing projects, relevant systems/support certificates and a verbatim excerpt from Tech Bridge Managing Director Gayeshan Mithige's recommendation.
- Avoid badges/statistics that imply unmeasured seniority or certificates.

**About**: IT student, professional story, customer communication, support work, prior engineering background and current learning; preserve relevant badges and real dates.

**Experience**: Make Help Desk most prominent while preserving chronology and dates. Keep SAĜO MENTE official titles, with evidence of application issue investigation, API diagnostics, logs and deployment verification. Preserve older retail/administration experience concisely as transferable service process skills. Use only roles and responsibilities found in repo/audit and approved by owner.

**Projects**: New categories Support & Labs, Application Engineering, QA/Security, Cyber Labs, Simulations, Academic. Preserve 24 existing entries. Add ServiceDesk Simulator as **ongoing independent training** only with truthful, owner-verified task statements or a simple “in progress; training focus” label. Show work status (Completed/In Progress/Lab/Simulation), work type, real tools, public demo links only where they exist. AssureX existing demo is `https://assurex-eight.vercel.app` (verify before claiming working). Keep all original badges and original Links to LetsDefend/TryHackMe/PicoCTF. Do not invent github subrepo links.

**Skills**: Lead with real remote technical support, incident/service-request handling, troubleshooting, communication/documentation, Windows/Linux and networking foundations. Follow with application/API diagnostics, Git/AWS exposure, and prior QA/security tools. Carry forward source labels Practical Experience/Working Knowledge/Awareness/Currently Learning. Mark Microsoft 365, Active Directory and cloud administration as learning if not supported by evidence; no fake percentage bars.

**Certifications**: Prioritize existing support/system/networking items, e.g. Technical Support Fundamentals (Google), Practical Help Desk (TCM Security), Networking Basics, Computer Hardware Basics, Operating Systems Basics, System Administration and IT Infrastructure Services. Retain full security/QA archive and 44 previews. Remove duplicate display of “Accelerate Your Job Search with AI” through a single item mapped to multiple filters, not by deleting original scans.

**Recommendations**: Keep all six quotes exactly as authored/attributed. Display Gayeshan's existing recommendation prominently for professionalism/communication. Do not rewrite quotes to imply help desk ticket performance.

**Contact**: Email `mohamed.rimsan.ar@gmail.com` is the public primary email. Keep LinkedIn `https://www.linkedin.com/in/mohamed-rimsan-a-r`, GitHub `https://github.com/mohamedrimsan`, existing WhatsApp/Discord and resume links only as currently authorized. Confirm Formspree endpoint/ownership and prefer working direct contact options. Make success/errors reliable; do not falsely claim mail sent. Resolve inconsistent Outlook fallback only when preference is confirmed or use public primary Gmail as visible fallback.

**Legacy redirect**: Keep `/hands-on-experience.html`, with preview-safe fallback link; don't unexpectedly send local preview visitors to production.

## Step 3 — Implement accessible behavior

- Mobile navigation: proper `<nav aria-label>`, button `aria-controls`/`aria-expanded`, active link `aria-current="page"`, Esc/outside click, progressive enhancement and robust focus handling.
- Project filters: correct selection state (`aria-pressed`), result count and empty state in live region. Preserve native `<details>` disclosures where helpful.
- Certificate gallery: fully accessible `<dialog>` or equivalent with named close button, focus entry/return, Esc/backdrop close, proper lazy image loading and no background scroll while active.
- Certificate search: combined category and text search; clear empty feedback; no mismatched card IDs.
- Theme control: localStorage only for user preference, guard storage failure, respect `prefers-color-scheme`, contrast-safe on both themes.
- Clipboard: don't announce success if fallback returns false; add screen-reader status.
- Contact form: preserve endpoint and semantic validation; graceful network/error paths; test mocks first and only test actual delivery after explicit approval.
- Motion: use minimal animation, honor `prefers-reduced-motion`, remove dormant typewriter unless used intentionally and accessibly.
- JS must never insert user-supplied input into untrusted HTML sinks.

## Step 4 — Performance, assets, and SEO

- Keep original 89 raster assets and badges/cert scans. Produce and use optimized responsive derivatives where helpful; don't preload huge full scans. Existing avatar is ~2 MiB; prioritize optimization. Replace huge avatar favicon with a small dedicated icon.
- Avoid broken absolute references in preview builds. Keep exact-case paths and encode filenames safely.
- Fix undefined `--primary-light` CSS token and light-mode contrast (audit calculated cyan-on-white 2.14:1).
- Verify font delivery; if no real hosted fonts, use a consistent system font stack.
- Page-specific title, description, OG/Twitter and structured data consistent with support-oriented positioning. Keep data historically accurate; don't present Technical Support Engineer as the official past job title. Update `sitemap.xml` only for pages genuinely modified and preserve `robots.txt`/Google verification.
- Keep the existing PDF path `Resume/AR-Mohamed-Rimsan-Resume.pdf`; audit says it may still be QA-focused. Don't replace it without owner-approved updated support resume.
- No made-up code repository links, statistics, uptime figures or client references.

## Step 5 — Prove the work

After implementation, perform actual browser and static checks:

1. Desktop at 1440px, laptop 1024px, tablet 768px, phones 375px and 320px.
2. Chrome/Chromium and at least one other engine if available; light/dark and system themes.
3. Keyboard-only navigation, visible focus, skip link, accessible filters, dialog open/close/focus restore, Escape, reduced motion, 200% zoom and disabled JS behavior.
4. Local internal links and case-sensitive file paths; outbound links, downloads, and no missing images across every page.
5. Project filters, certificate text/category filters, responsive menu, theme toggle, clipboard, contact form mocked success/error and native downloads.
6. Static build/hosting compatibility and resulting independent HTML routes. Check the legacy redirect and Google verification file.
7. WCAG 2.2 AA contrast and semantics. If tooling available, run axe and Lighthouse on homepage, projects, credentials and contact; report real measured results and realistic tradeoffs, not assumed scores.
8. Verify no secrets, customer records, unauthorized screenshots or confidential claims were introduced.
9. Update README with project structure, local preview instructions, publishing branch cautions and maintenance instructions.

**Expected deliverables (in the working tree):** complete edited site; any approved optimized assets; `REDESIGN_CONTENT_DECISIONS.md`; a concise `REDESIGN_CHANGELOG.md`; a runnable/static `QA_REPORT.md` indicating passed/failed/not tested checks; screenshots or preview URLs if available; deployment/rollback instructions; per-file git diff summary. Provide list of factual confirmation items still pending, without silently resolving them.

## Final release gate

Do not push, merge or deploy. Stop with an implementable, reviewable changeset on a non-production branch. Ask for owner approval **only for production publishing or unresolved factual claims that must be altered**. Continue independent implementation without blocking on optional confirmations by preserving currently published facts with clear review notes.

**Begin by reading the audited repository files and building the actual redesign in the current codebase.**
