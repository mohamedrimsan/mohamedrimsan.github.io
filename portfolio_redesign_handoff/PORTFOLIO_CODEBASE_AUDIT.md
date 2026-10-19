# Portfolio Codebase Audit — Phase 1

**Owner:** Mohamed Rimsan / AR. Mohamed Rimsan  
**Date:** 19 October 2026 (Asia/Colombo)  
**Website:** https://mohamedrimsan.github.io/  
**Repository:** https://github.com/mohamedrimsan/mohamedrimsan.github.io  
**Checkout:** F:/My Portfolio Web/mohamedrimsan.github.io  
**Inspected branch:** `qa-security-engineer-version`  
**HEAD:** `63a5cb3`, 8 October 2026.

Only this report was created. Existing website files/assets were not edited, deleted, renamed or regenerated. No dependencies were installed, no branches changed, and nothing was committed, pushed or deployed.

Evidence terminology: **source-confirmed** means directly present in the checkout, not independently verified professional history; **HTTP-confirmed** means a public request actually succeeded; **source-based risk** means inferred from code without rendered-browser confirmation; **unknown/not tested** means evidence is missing. Do not turn source claims into externally verified facts.

## 1. Executive Summary

This is a static multipage portfolio with **eight full content pages, one legacy redirect and one Google verification HTML resource**. One shared stylesheet and one shared vanilla JavaScript file support the content pages. No frontend framework, application server, database, package manifest, lockfile or bundler is present. Python is used only for an optional resume generator.

Existing branding is **QA & Security Engineer**, emphasizing application security, QA automation, vulnerability management, AWS/cloud validation and GRC. The requested new direction—Technical Support Engineering, IT Support, Service Desk, Systems & Application Support and IT Operations—is not yet consistently reflected. Useful support evidence already exists: Help Desk Representative employment, troubleshooting, incident/service-request logging, escalation, user communication, systems/network foundations, help desk courses and a support-employer recommendation. Preserve QA/cybersecurity as technical background and retain accurate historical job titles.

**Recommendation: B — restructure the existing HTML/CSS/JavaScript while preserving static multipage delivery and existing URLs.** Current functionality does not justify a framework migration. Image optimization, factual content reconciliation, accessibility and consistent shared markup offer clearer benefits.

Key findings:

- Live homepage GET returned 200 and its decoded text matched local index.html. All ten HTML endpoints, robots.txt, sitemap.xml and the resume returned HEAD 200. Availability does not establish correct runtime behavior.
- Public deployment records show recent GitHub Pages deployments from `main`, including a successful managed Pages build. The current checkout branch is different. Exact publishing-folder settings remain unverified.
- Static checks found no missing local HTML path targets, duplicate IDs, unresolved local fragment links or missing popup IDs. Windows case-insensitive existence checks alone cannot establish filename-case safety.
- Assets comprise **89 raster images plus one PDF**, 79,399,262 bytes / approximately **75.7 MiB**. The 2 MiB portrait doubles as the favicon; many certificate scans exceed 1–2 MiB. Storage size is not page transfer size.
- Certificate overlays lack accessible dialog/focus handling, light-mode primary text has poor contrast against white, and mobile navigation depends on JavaScript.
- Website and resume-generation source disagree on a QA role title and administrative employment dates. Resolve before revising professional copy.
- Project evidence is incomplete: no project-specific source repository links or screenshots; only AssureX has an external app demo link.
- Browser startup failed because of an environment sandbox error. No viewport renders, screenshots, Lighthouse scores, Core Web Vitals or screen-reader results are claimed.

## 2. Technology Stack

| Layer | Actual implementation |
| --- | --- |
| Languages | HTML5, CSS, vanilla JavaScript; Python 3 resume utility; XML sitemap. |
| HTML | Independent root-level documents. Header/nav/footer/SEO markup repeated across eight content pages. No template/include system or shared HTML components. |
| CSS | style.css only; 2,760 lines, 50,924 bytes. Custom properties, grid, flex, clamp/min/minmax, media queries, shared and page-specific rules. |
| JavaScript | main.js only; 7,134 bytes. One DOMContentLoaded initializer, optional controls, data-attribute hooks. No modules, router or state framework. |
| Build/package tools | No package.json, dependency lockfiles, frontend compilation config, package manager requirement, node_modules or test suite found. |
| Third-party library | Font Awesome 6.5.0 CSS: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css ; transitive icon-font resources served by the CDN. |
| Typography | CSS names Inter and Space Grotesk, but neither is loaded by font imports, font-face, a remote font stylesheet or local webfonts. Installed fonts/fallbacks determine actual rendering. |
| Integrations | Formspree message POST, browser Clipboard API with legacy fallback, outbound LinkedIn/GitHub/WhatsApp/security-platform links. No embedded analytics or live GitHub activity API found. |
| Resume tooling | Resume/generate_resume.py uses ReportLab and optional Windows Arial files, falling back to Helvetica. It is not a deployment dependency and was not executed. No Python dependency manifest found. |
| Hosting | Static GitHub Pages at account-root domain over HTTPS. No CNAME or custom-domain configuration file. |
| CI/CD | No checked-in .github/workflows; public API shows a successful managed dynamic/pages/pages-build-deployment run on main. |
| UI patterns | Repeated hero, eyebrow, metrics, cards, tags, grids, CTAs, native project disclosures and image overlays. |

## 3. Complete Directory Structure

All visible non-Git working-tree files are listed below. .git internals are summarized as version-control metadata. .agents exists and was empty; no applicable AGENTS.md was found. .vscode/settings.json is tracked despite the current ignore rule. The new report is the sole addition.

```text
mohamedrimsan.github.io/
├── .agents/
├── .git/
├── .vscode/
│   └── settings.json
├── Badges/
│   ├── 29729252200878.png
│   ├── AI Security Fundamentals_Badge.png
│   ├── computer-hardware-basics.png
│   ├── CPPS.jpg
│   ├── cyber-threat-management.png
│   ├── endpoint-security.png
│   ├── english-for-it-1.png
│   ├── First Blood.png
│   ├── google-cybersecurity-professional-certificate-v-2 (1).png
│   ├── Incident Handler - 2.png
│   ├── Incident Handler.png
│   ├── isc2-candidate.png
│   ├── iso-iec-27701-2025-lead-auditor.png
│   ├── junior-cybersecurity-analyst-career-path.1.png
│   ├── lfs101-introduction-to-linux.png
│   ├── Malware Analyzer.png
│   ├── network-defense.png
│   ├── networking-basics.png
│   ├── networking-devices-and-initial-configuration.png
│   ├── OCI25AICFAV1.png
│   ├── operating-systems-basics.png
│   ├── opswat-introduction-to-critical-infrastructure-protection-icip.png
│   ├── Phishing Expert.png
│   ├── SIEM.png
│   ├── SOC Member.png
│   ├── Web Attack Investigated.png
│   └── Web Attack Investigator.png
├── Certificates/
│   ├── Accelerate Your Job Search with AI.jpg
│   ├── AI Security Fundamentals!_Cert.jpg
│   ├── aig.jpg
│   ├── Assets, Threats, and Vulnerabilities.jpg
│   ├── AutomateTasks.jpg
│   ├── Certified Artificial Intelligence Security & Risk (CAISR).jpg
│   ├── Comonwealth.jpg
│   ├── ConnectNetwork.jpg
│   ├── CPPS.jpg
│   ├── CS401_OS.jpg
│   ├── cyber_track.jpg
│   ├── cybercommomwealth.jpg
│   ├── cyberkill.jpg
│   ├── cyberthreat.jpg
│   ├── Datacom Cybersecurity Job Simulation on Forage.jpg
│   ├── Delloite.jpg
│   ├── Endpoint.jpg
│   ├── Forage.jpg
│   ├── Foundation_Cybersecurity.jpg
│   ├── FullStack.jpg
│   ├── GitHub.jpg
│   ├── GoogleCybersecurity.jpg
│   ├── hardware.jpg
│   ├── Intro_cryptography.jpg
│   ├── Intro_Linux.jpg
│   ├── Introduction to Software Testing.jpg
│   ├── introduction_to_cip.png
│   ├── ISOIEC 277012025 Lead Auditor.jpg
│   ├── IT_Security.jpg
│   ├── java_fundamental.jpg
│   ├── JuniorCybersecurityAnalyst.jpg
│   ├── Linex&SQL.jpg
│   ├── Managerisk.jpg
│   ├── Mental_Health.jpg
│   ├── Network_Defence.jpg
│   ├── networkbasics.jpg
│   ├── networkconfig.jpg
│   ├── operationalizing-mitre-attck-for-socs.jpg
│   ├── oracle.jpg
│   ├── practical-help-desk.jpg
│   ├── Put It to Work.jpg
│   ├── Python GFG.jpg
│   ├── soc.jpg
│   ├── socanalyst.jpg
│   ├── SoundsAlarm.jpg
│   ├── Splunk.jpg
│   ├── System Admin.jpg
│   ├── Tata.jpg
│   ├── Tecgnical_support.jpg
│   └── UIUX_Design.jpg
├── Images/
│   ├── avatar.jpg
│   ├── business-person-futuristic-business-environment.jpg
│   ├── discord-icon.png
│   ├── github-icon.png
│   ├── gmail-icon.png
│   ├── letsdefend-icon.png
│   ├── linkedin-icon.png
│   ├── picoctf-icon.png
│   ├── tryhackme-icon.png
│   └── whatsapp-icon.png
├── Resume/
│   ├── AR-Mohamed-Rimsan-Resume.pdf
│   └── generate_resume.py
├── .gitignore
├── about.html
├── Background_dark.jpg
├── Background_light.jpg
├── certifications.html
├── contact.html
├── experience.html
├── googlec5a2878c58ee90d7.html
├── hands-on-experience.html
├── index.html
├── main.js
├── projects.html
├── README.md
├── recommendations.html
├── robots.txt
├── sitemap.xml
├── skills.html
└── style.css
```

| Source / resource | Purpose |
| --- | --- |
| index.html | Homepage entry point at / and /index.html; portrait, professional summary, focus cards, highlights, static GitHub promotion, exploration links and contact CTA. WebSite/Person/WebPage JSON-LD. |
| about.html | Biography, career journey/direction, education, mindset and 17 badge cards. ProfilePage/Person JSON-LD. |
| experience.html | Five-entry career timeline, detailed trainee/intern/help desk roles, earlier retail/administration roles and professional-value cards. |
| hands-on-experience.html | Legacy immediate meta-refresh redirect to production projects.html with canonical/noindex and a relative fallback link. |
| projects.html | Named projects/labs/platforms/simulations, category filters, native contribution disclosures, nine LetsDefend reward links and seven certificate overlays. |
| skills.html | Categorized capabilities, tools, experience-level labels, IT support foundations, working style and developing skills. |
| certifications.html | Category/text-searchable certificate cards and 44 image overlays. |
| recommendations.html | Six attributed quotes, initials avatars, one individual LinkedIn link, values and CTA. |
| contact.html | Six contact methods, availability topics, resume link, Formspree form and live feedback. |
| googlec5a2878c58ee90d7.html | Single-line Google verification resource; intentionally not a visitor page. Preserve unchanged. |
| style.css / main.js | All presentation / all shared JavaScript interactions. |
| robots.txt / sitemap.xml | Allow-all crawl policy and eight canonical page URLs; every lastmod is 2026-09-16. |
| README.md | Static-site rationale and previous cybersecurity-centric branding. |
| .gitignore | OS/editor/env/build/dependency/diagnostic ignore patterns. |
| Images/, Badges/, Certificates/ | Portrait/illustration/social icons; badge files; certificate scans. See section 7. |
| Resume/AR-Mohamed-Rimsan-Resume.pdf | Public downloadable resume. |
| Resume/generate_resume.py | Optional ReportLab generator containing parallel professional facts; execution would overwrite PDF. |
| Background_dark.jpg / Background_light.jpg | Unreferenced legacy backgrounds; current site uses CSS gradients. |
| .vscode/settings.json | Editor configuration, not a runtime dependency. |

## 4. Existing Page Inventory

**Navigation:** all eight full pages link Home → index.html, About → about.html, Experience → experience.html, Projects → projects.html, Skills → skills.html, Certifications → certifications.html, Recommendations → recommendations.html, Contact → contact.html. Navigation uses full document loads, not a client router. main.js marks the current basename active, treating / as index.html. The legacy hands-on route is absent from primary navigation.

**Shared dependencies:** style.css, deferred main.js and CDN Font Awesome on all eight full pages. Each has an English language declaration, viewport, skip link, main landmark, one h1, header/nav/footer, canonical, portrait favicon and social metadata. Header subtitle and footer secure-systems/quality/risk messaging need later repositioning. Copyright text is statically 2026–2027. The redirect and verification resource do not use shared UI dependencies.

The inventory below lists actual headings, body actions and asset use. Expanded professional, project, credential and recommendation inventories follow in sections 5–6.

### index.html

**Route:** / and /index.html  
**Title:** AR. Mohamed Rimsan | QA & Security Engineer

**Purpose/sections/content:** Homepage: summary, six focus cards, professional highlights, static GitHub illustration/profile link, explore cards and CTA.

**Usability/preserve:** Preserve portrait, authentic technical strengths, recruiter paths and resume. Current long QA/security pitch needs support-first editing. GitHub promotion is static, not a contribution feed.

**Headings:**

- H1: Engineering Quality. Securing Digital Solutions.
- H2: Security-minded quality engineering for reliable digital delivery
- H2: Where Security Validation and Quality Assurance Connect
- H3: Application Security
- H3: QA Engineering
- H3: Test Automation
- H3: API & Integration Testing
- H3: Cloud Security Validation
- H3: Governance, Risk & Compliance
- H2: Security Validation with QA Discipline
- H2: Security, Quality & Risk-Focused Engineering
- H2: Practical work across security assessment, QA, release readiness, and documentation
- H2: Code-based learning, experimentation, and security practice
- H2: Experience, projects, and supporting credentials
- H3: Experience
- H3: Projects
- H3: Certifications
- H2: Trusted Delivery Starts with Quality, Security, and Practical Risk Awareness

| Body link / interactive control | Target / behavior |
| --- | --- |
| View Projects | projects.html |
| Download Resume | Resume/AR-Mohamed-Rimsan-Resume.pdf |
| Contact Me | contact.html |
| Visit GitHub Profile | https://github.com/mohamedrimsan |
| Open Experience | experience.html |
| Open Projects | projects.html |
| Open Certifications | certifications.html |

**Body assets:** `Images/avatar.jpg`; `Images/business-person-futuristic-business-environment.jpg`.

**JavaScript relevance:** shared menu/active navigation; no active typewriter target or live GitHub data.

### about.html

**Route:** /about.html  
**Title:** About AR. Mohamed Rimsan | QA & Security Engineer

**Purpose/sections/content:** Biography, career journey and direction, competencies/interests, education, professional mindset and badge showcase.

**Usability/preserve:** Preserve academic facts and working values. Direction remains security focused. Oracle badge label is more generic than its corresponding AI Foundations certificate.

**Headings:**

- H1: About Me
- H2: Practical QA and security work with real delivery exposure
- H2: Career Journey
- H2: QA & Security Engineer
- H2: Focused across application security, QA, cloud validation, and GRC
- H3: Application Security
- H3: QA Engineering
- H3: Cloud & Deployment Validation
- H3: Governance, Risk & Compliance
- H2: Core Competencies
- H2: Professional Interests
- H2: BSc (Hons) Information Technology
- H3: Focus Areas
- H2: Software Testing and Automation Specialization
- H2: Quality, Security & Clarity
- H3: Verify Carefully
- H3: Think Risk First
- H3: Document Clearly
- H2: Digital badges that support the broader skill profile
- H3: ISO/IEC 27701 Lead Auditor
- H3: AI Security Fundamentals
- H3: Critical Infrastructure Protection
- H3: Google Cybersecurity Professional
- H3: Phishing Prevention Specialist
- H3: Junior Cybersecurity Analyst
- H3: Oracle Cloud Foundations
- H3: Introduction to Linux
- H3: Purple Academy
- H3: Cyber Threat Management
- H3: Endpoint Security
- H3: Network Defense
- H3: English for IT
- H3: Networking Basics
- H3: Networking Devices
- H3: Operating Systems Basics
- H3: Computer Hardware Basics

**Body assets:** `Badges/29729252200878.png`; `Badges/AI Security Fundamentals_Badge.png`; `Badges/CPPS.jpg`; `Badges/OCI25AICFAV1.png`; `Badges/computer-hardware-basics.png`; `Badges/cyber-threat-management.png`; `Badges/endpoint-security.png`; `Badges/english-for-it-1.png`; `Badges/google-cybersecurity-professional-certificate-v-2 (1).png`; `Badges/iso-iec-27701-2025-lead-auditor.png`; `Badges/junior-cybersecurity-analyst-career-path.1.png`; `Badges/lfs101-introduction-to-linux.png`; `Badges/network-defense.png`; `Badges/networking-basics.png`; `Badges/networking-devices-and-initial-configuration.png`; `Badges/operating-systems-basics.png`; `Badges/opswat-introduction-to-critical-infrastructure-protection-icip.png`.

**JavaScript relevance:** shared menu/active navigation; no page-specific controls beyond shared behaviors.

### experience.html

**Route:** /experience.html  
**Title:** QA & Security Experience | AR. Mohamed Rimsan

**Purpose/sections/content:** Five career timeline entries, trainee/intern/help desk responsibilities, retail/administration history, professional values and CTA.

**Usability/preserve:** Preserve official titles/dates after reconciliation. Help desk is first in timeline but follows QA roles in detailed content. Nonwrapping trainee title needs mobile testing.

**Headings:**

- H1: Experience
- H2: Professional growth across QA, security, support, and operations
- H3: Help Desk Representative
- H3: QA & Security Engineer Trainee
- H3: QA & Security Engineer Intern
- H3: Inventory Manager & Cashier
- H3: Administrative Assistant
- H2: QA & Security Engineer Trainee
- H3: Responsibilities
- H3: Key Exposure
- H2: QA & Security Engineer Intern
- H3: Responsibilities
- H3: Key Exposure
- H2: Help Desk Representative
- H3: Responsibilities
- H3: Key Exposure
- H2: Transferable operational experience
- H3: Inventory Manager & Cashier
- H4: Transferable Skills
- H3: Administrative Assistant
- H4: Transferable Skills
- H2: Experience That Supports Secure Delivery
- H3: Security Mindset
- H3: QA Discipline
- H3: Support & Troubleshooting
- H3: Documentation & Communication
- H2: Projects, certifications, and technical proof points

| Body link / interactive control | Target / behavior |
| --- | --- |
| View Projects | projects.html |
| View Certifications | certifications.html |
| Contact Me | contact.html |

**Body images:** none. Shared favicon/social portrait only on full content pages.

**JavaScript relevance:** shared menu/active navigation; no page-specific controls beyond shared behaviors.

### hands-on-experience.html

**Route:** /hands-on-experience.html  
**Title:** Redirecting to Projects

**Purpose/sections/content:** Legacy redirect to Projects; no separate practical-experience content remains.

**Usability/preserve:** Immediate meta refresh uses an absolute production URL, escaping local/preview hosts; fallback link is relative. Canonical targets Projects, robots noindex/follow. Preserve URL compatibility.

| Body link / interactive control | Target / behavior |
| --- | --- |
| Projects | projects.html |

**Body images:** none. Shared favicon/social portrait only on full content pages.

### projects.html

**Route:** /projects.html  
**Title:** QA, AppSec & Cybersecurity Projects | AR. Mohamed Rimsan

**Purpose/sections/content:** Professional/personal initiatives, security labs/platforms, achievement badges, virtual simulations and software/academic entries.

**Usability/preserve:** Preserve real technical work and status labels. Most cards lack source/demo/evidence links. Do not invent those. Filters have no accessible selected state or no-results feedback.

**Headings:**

- H1: Projects
- H2: Professional QA, security, and delivery initiatives
- H3: SAĜO MENTE Security & QA Initiatives
- H3: AssureX – Enterprise Quality, Security & Risk Assurance Platform
- H3: VeriGuard – Hybrid QA Automation & Testing Platform
- H3: MailForge – Email Campaign & Tracking Automation Platform
- H3: Personal Portfolio Website
- H2: Defensive security, web testing, cloud checks, and cyber platforms
- H3: Defensive Cybersecurity Home Lab
- H3: OWASP-Oriented Web Testing
- H3: Cloud Security Experiments
- H3: LetsDefend
- H3: TryHackMe
- H3: PicoCTF
- H3: SOC investigation and incident response achievements
- H2: Compact cybersecurity job simulations
- H3: Commonwealth Bank Introduction to Cybersecurity
- H3: Datacom Cybersecurity Job Simulation
- H3: Commonwealth Bank Tech Explorer
- H3: AIG Shields Up
- H3: Tata Cybersecurity Security Analyst
- H3: Deloitte Australia Cyber Job Simulation
- H3: Mastercard Cybersecurity Virtual Experience
- H2: Programming, logic, and system design foundations
- H3: Smart Bus Route Finder
- H3: AI Expert System: Tech Career Advisor
- H3: Tic-Tac-Toe Game
- H3: Simple Calculator
- H3: Basic Hospital Appointment System
- H3: GPA Calculator
- H2: Continuous growth across QA, cybersecurity, cloud validation, and secure delivery

| Body link / interactive control | Target / behavior |
| --- | --- |
| All | filter all |
| Professional | filter professional |
| QA & Security | filter qa-security |
| Application Security | filter application-security |
| Cloud Security | filter cloud-security |
| Security Labs | filter security-labs |
| Virtual Experience | filter virtual-experience |
| Software Development | filter software-development |
| Academic Projects | filter academic-projects |
| View Experience | experience.html |
| View Project | https://assurex-eight.vercel.app |
| Visit Portfolio | index.html |
| View Profile | https://app.letsdefend.io/user/cybersentinel |
| View Profile | https://tryhackme.com/p/cybersentinel01 |
| View Profile | https://play.picoctf.org/users/cybersentinel01 |
| (image link) | https://app.letsdefend.io/my-rewards/detail/3f78042e-bdad-4fb8-a1cb-d05fcabaec2d |
| (image link) | https://app.letsdefend.io/my-rewards/detail/4c45ad6a-c7c6-4d3f-918b-e86b604d0f0f |
| (image link) | https://app.letsdefend.io/my-rewards/detail/472d824a7f7e4c44a46fbc15edf75457 |
| (image link) | https://app.letsdefend.io/my-rewards/detail/fd0ab1fe-81cc-49a9-b599-1cc7dd4a751f |
| (image link) | https://app.letsdefend.io/my-rewards/detail/2a20f2a9-39a4-4e27-ac3f-3bc631a463d1 |
| (image link) | https://app.letsdefend.io/my-rewards/detail/0fa9f702-aadd-4535-b970-5b50c30e5559 |
| (image link) | https://app.letsdefend.io/my-rewards/detail/dd03b799-186f-4552-b3e1-c489ca21a61c |
| (image link) | https://app.letsdefend.io/my-rewards/detail/f6f51586-c9ef-4855-8fc1-ea60d6d5b8e7 |
| (image link) | https://app.letsdefend.io/my-rewards/detail/464f873b-aec9-459f-b938-d1cdc102004d |
| Preview Certificate | popup #project-commonwealth-cyber |
| Preview Certificate | popup #project-datacom-cyber |
| Preview Certificate | popup #project-commonwealth-tech |
| Preview Certificate | popup #project-aig-shields |
| Preview Certificate | popup #project-tata-cyber |
| Preview Certificate | popup #project-deloitte-cyber |
| Preview Certificate | popup #project-mastercard-cyber |
| View Certifications | certifications.html |
| Contact Me | contact.html |

**Body assets:** `Badges/First Blood.png`; `Badges/Incident Handler - 2.png`; `Badges/Incident Handler.png`; `Badges/Malware Analyzer.png`; `Badges/Phishing Expert.png`; `Badges/SIEM.png`; `Badges/SOC Member.png`; `Badges/Web Attack Investigated.png`; `Badges/Web Attack Investigator.png`; `Certificates/Comonwealth.jpg`; `Certificates/Datacom Cybersecurity Job Simulation on Forage.jpg`; `Certificates/Delloite.jpg`; `Certificates/Forage.jpg`; `Certificates/Tata.jpg`; `Certificates/aig.jpg`; `Certificates/cybercommomwealth.jpg`.

**JavaScript relevance:** project categories, seven image popups, Escape/overlay close and scroll lock; native details/summary needs no custom JS.

### skills.html

**Route:** /skills.html  
**Title:** QA, Application Security & Cloud Skills | AR. Mohamed Rimsan

**Purpose/sections/content:** Primary QA/security skills, tools, defensive skills, systems/support foundations, analytical skills, working style and growth targets.

**Usability/preserve:** Preserve Practical Experience versus Working Knowledge/Awareness/Currently Building. Presentation uses labels/tags, not percentage bars. Support is currently a secondary grouping.

**Headings:**

- H1: Skills
- H2: Primary QA and security engineering capabilities
- H3: QA Engineering
- H3: Application Security
- H3: API Security & Testing
- H3: Vulnerability Management
- H3: Cloud Security Validation
- H3: Governance, Risk & Compliance
- H2: Grouped tools for testing, validation, infrastructure, and development
- H3: Security Tools
- H3: QA & API Tools
- H3: Cloud & Infrastructure
- H3: Development & Scripting
- H2: Supportive blue-team knowledge without overclaiming
- H3: SOC Fundamentals
- H3: Monitoring Awareness
- H3: Defensive Controls
- H2: Systems knowledge that strengthens troubleshooting and validation
- H3: Network Foundations
- H3: System Administration
- H3: Support Practice
- H2: Investigation, reasoning, and root-cause thinking
- H3: Threat Detection
- H3: Critical Thinking
- H3: Problem Solving
- H3: Troubleshooting
- H2: Reliable habits for QA, security, IT support, and delivery teams
- H2: Skill areas I am actively building
- H3: Detection & Monitoring
- H3: Cloud Response
- H3: Advanced Practice
- H2: Applied across QA engineering, cybersecurity, cloud validation, and secure delivery

| Body link / interactive control | Target / behavior |
| --- | --- |
| View Projects | projects.html |
| View Experience | experience.html |
| Contact Me | contact.html |

**Body images:** none. Shared favicon/social portrait only on full content pages.

**JavaScript relevance:** shared menu/active navigation; no page-specific controls beyond shared behaviors.

### certifications.html

**Route:** /certifications.html  
**Title:** Cybersecurity & QA Certifications | AR. Mohamed Rimsan

**Purpose/sections/content:** Three featured credentials, seven tracks, category filters, search and preview overlays.

**Usability/preserve:** Preserve originals and dates. One course is listed twice. Local previews do not independently verify credentials. Modal control/focus shortcomings need correction.

**Headings:**

- H1: Certifications
- H2: Key credentials aligned with QA and security engineering
- H3: Google Cybersecurity Professional Certificate
- H3: Junior Cybersecurity Analyst
- H3: Certified Phishing Prevention Specialist (CPPS)
- H2: Software testing foundations and quality assurance
- H3: Introduction to Software Testing
- H2: Security foundations, risks, vulnerabilities, and defensive concepts
- H3: ISO/IEC 27701:2025 Lead Auditor
- H3: Sound the Alarm: Detection and Response
- H3: Assets, Threats, and Vulnerabilities
- H3: IT Security: Defense against the Digital Dark Arts
- H3: Play It Safe: Manage Security Risks
- H3: Foundations of Cybersecurity
- H3: Cyber Kill Chains
- H3: Introduction to Cryptography
- H3: Cyber Security Track
- H2: SOC workflows, detection, alert handling, and defensive security
- H3: Security Operations Center (SOC)
- H3: Operationalizing MITRE ATT&CK for SOCs
- H3: Cyber Threat Management
- H3: Endpoint Security
- H3: Network Defense
- H3: Student SOC Program - Foundations
- H3: Intro to Splunk (eLearning)
- H2: Infrastructure, operating systems, networks, Linux, SQL, and administration
- H3: Tools of the Trade: Linux and SQL
- H3: Connect & Protect: Network & Network Security
- H3: Networking Devices & Initial Configuration
- H3: Networking Basics
- H3: Computer Hardware Basics
- H3: Introduction to Linux (LFS101)
- H3: CS401: Operating Systems
- H3: System Administration and IT Infrastructure Services
- H2: Cloud awareness, emerging technology, and modern infrastructure
- H3: Certified Artificial Intelligence Security & Risk (CAISR)
- H3: AI Security Fundamentals
- H3: Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate
- H3: Introduction to CIP
- H3: Accelerate Your Job Search with AI
- H3: Mental Health in Cybersecurity
- H2: Scripting, automation, development, and implementation foundations
- H3: Automate Cybersecurity Tasks with Python
- H3: Python Programming
- H3: Full Stack Development (HTML, CSS, Java, JavaScript)
- H3: The Git & GitHub Bootcamp
- H3: Java Programming
- H3: User Experience Design - Learn UI/UX with Figma
- H2: Technical support, job readiness, service skills, and professional development
- H3: Technical Support Fundamentals
- H3: Practical Help Desk
- H3: Put It to Work: Prepare for Cybersecurity Jobs
- H3: Accelerate Your Job Search with AI
- H2: Learning that supports QA, cybersecurity, cloud validation, and secure delivery

| Body link / interactive control | Target / behavior |
| --- | --- |
| All | filter all |
| QA & Software Testing | filter qa-testing |
| Core Cybersecurity | filter core-cybersecurity |
| SOC & Threat Detection | filter soc-threat-detection |
| Networking & Systems | filter networking-systems |
| Cloud & Emerging Tech | filter cloud-emerging |
| Programming & Development | filter programming-development |
| IT Support & Professional Skills | filter it-support-professional |
| View Skills | skills.html |
| View Projects | projects.html |
| View Experience | experience.html |
| 44 Preview Certificate buttons | Matching image popup IDs; full credential mapping in section 6 |

**Body assets:** 43 distinct certificate images; individually inventoried in sections 6–7..

**JavaScript relevance:** combined category/text search, empty-section hiding and certificate popups.

### recommendations.html

**Route:** /recommendations.html  
**Title:** Professional Recommendations | AR. Mohamed Rimsan

**Purpose/sections/content:** Six attributed testimonials, initials avatars, professional values and networking CTA.

**Usability/preserve:** Preserve exact wording and attribution. Only Nimesh has a profile link. Initials are intentional, not missing images. Hover/focus references undefined --primary-light.

**Headings:**

- H1: Recommendations
- H2: Feedback that supports my early-career QA and security engineering direction
- H2: Professional recommendations from collaborators and leaders
- H3: Mr. Hemal Tharaka Eranga
- H3: Mr. Nimesh Piyumantha
- H3: Mr. Gayeshan Mithige
- H3: Ms. Amani Zulfi
- H3: Mr. K. Ahamed Ammar
- H3: Dr. MH. Mohamed Sabir
- H2: Professional Values Reflected in These Recommendations
- H3: Communication
- H3: Reliability
- H3: Teamwork
- H3: Continuous Learning
- H2: Open to professional conversations across QA, cybersecurity, and secure delivery

| Body link / interactive control | Target / behavior |
| --- | --- |
| Mr. Nimesh Piyumantha | https://www.linkedin.com/in/nimesh-piyumantha/ |
| View Experience | experience.html |
| View Projects | projects.html |
| Contact Me | contact.html |
| Connect on LinkedIn | https://www.linkedin.com/in/mohamed-rimsan-a-r |

**Body images:** none. Shared favicon/social portrait only on full content pages.

**JavaScript relevance:** shared menu/active navigation; no page-specific controls beyond shared behaviors.

### contact.html

**Route:** /contact.html  
**Title:** Contact AR. Mohamed Rimsan | QA & Security Engineer

**Purpose/sections/content:** LinkedIn, email, GitHub, portfolio, WhatsApp and Discord cards; availability topics, resume and contact form.

**Usability/preserve:** Discord button copies a username rather than opening a profile. Preserve labels/live status; update outdated subjects later. Form delivery untested; error email disagrees with primary email.

**Headings:**

- H1: Contact
- H2: Choose the best way to connect
- H3: LinkedIn
- H3: Email
- H3: GitHub
- H3: Portfolio
- H3: WhatsApp
- H3: Discord
- H2: Professional topics and collaboration areas
- H2: Conversations around QA, cybersecurity, and secure software delivery
- H2: Share the context clearly

| Body link / interactive control | Target / behavior |
| --- | --- |
| View LinkedIn Profile | https://www.linkedin.com/in/mohamed-rimsan-a-r |
| Send Email | mailto:mohamed.rimsan.ar@gmail.com |
| View GitHub Profile | https://github.com/mohamedrimsan |
| Visit Portfolio | https://mohamedrimsan.github.io |
| Message on WhatsApp | https://wa.me/[public contact number omitted] |
| Connect on Discord | copy username |
| View Experience | experience.html |
| View Projects | projects.html |
| Download Resume | Resume/AR-Mohamed-Rimsan-Resume.pdf |
| Connect on LinkedIn | https://www.linkedin.com/in/mohamed-rimsan-a-r |
| Send Message | submit |
| Reset | reset |

**Body images:** none. Shared favicon/social portrait only on full content pages.

**JavaScript relevance:** clipboard copy and asynchronous form status/error handling. No message submitted during audit.

### googlec5a2878c58ee90d7.html

**Route:** /googlec5a2878c58ee90d7.html  
**Title:** None

**Purpose/sections/content:** Google site-verification text; not a visitor-facing portfolio page.

**Usability/preserve:** No title/headings/nav/scripts/images by design. Preserve unchanged; do not classify minimal markup here as a portfolio UX defect.

**Body images:** none. Shared favicon/social portrait only on full content pages.



## 5. Professional Content Inventory

### Identity and biography

**Displayed name:** AR. Mohamed Rimsan; structured-data alternate name: Mohamed Rimsan. Resume source uses AR Mohamed Rimsan. **Existing title:** QA & Security Engineer. These statements are verified as repository content, not independently verified personal/employment facts.

Homepage headline: “Engineering Quality. Securing Digital Solutions.” Subtitle emphasizes Application Security, QA Automation, Vulnerability Management and AWS & Cloud Security. The biography identifies a BSc (Hons) IT undergraduate with QA, cybersecurity, vulnerability management, cloud validation, GRC and secure-delivery exposure. The career journey starts with an interest in IT systems/troubleshooting, then moves into cybersecurity/QA. Current direction includes SOC defensive awareness. Recurring values are validating carefully, risk thinking, clear documentation and cross-functional communication.

**New direction supplied by owner, not existing site copy:** Technical Support Engineering; IT Support; Service Desk; Systems & Application Support; IT Operations. Lead with substantiated support responsibilities and outcomes; retain QA/security as background. Do not silently change historical titles to new target titles.

### Public professional references

| Reference | Existing content |
| --- | --- |
| Primary public email | mohamed.rimsan.ar@gmail.com — contact mailto, homepage/about schema and resume source. |
| Fallback email | mohamed.rimsan@outlook.com — main.js form-error message only; preferred/current address unknown. |
| LinkedIn | https://www.linkedin.com/in/mohamed-rimsan-a-r |
| GitHub | https://github.com/mohamedrimsan |
| Portfolio | https://mohamedrimsan.github.io/ |
| WhatsApp | contact.html has a public wa.me contact URL. Phone digits are intentionally not reproduced in this shareable report. |
| Discord | mohamedrimsan; data-copy username only, no invite/profile URL. |
| Security platforms | https://tryhackme.com/p/cybersentinel01 ; https://app.letsdefend.io/user/cybersentinel ; https://play.picoctf.org/users/cybersentinel01 |
| Resume | Resume/AR-Mohamed-Rimsan-Resume.pdf on homepage/contact; download filename Mohamed_Rimsan_Resume.pdf. Local file exists; live HEAD 200. Binary PDF content/layout was not extracted/rendered. |
| Location | Resume-generation source states Western Province, Sri Lanka. No more precise personal address copied. |

### Existing employment descriptions

Below are current public website responsibilities. No quantified SLA, support volume, CSAT, team size or resolution-rate achievement is stated. Employer/title/date statements require factual confirmation where conflicts are noted.

#### QA & Security Engineer Trainee

**Employer:** SAĜO MENTE INTERNATIONAL SDN. BHD.  
**Metadata:** July 2026 – September 2026 Trainee QA Engineering | Cybersecurity | Security Validation

Contributed to the quality assurance, security validation, and production readiness of a global digital marketplace platform.

**Responsibilities:**

- Performed end-to-end quality assurance and security validation across web and mobile applications, covering functional, regression, workflow, UAT, responsive, cross-device, and release testing.
- Tested REST APIs using Postman and Swagger/OpenAPI, validating authentication, authorization, input handling, error responses, business logic, and data flows between frontend and backend services.
- Built and executed QA automation using Playwright while expanding mobile test automation knowledge with Appium to improve repeatable regression coverage.
- Validated application security and privacy requirements, including role-based access control, data exposure, authentication flows, authorization boundaries, session handling, and secure user interactions.
- Identified, reproduced, documented, and tracked defects and enhancements in Jira, working with developers to investigate root causes, verify fixes, and confirm resolution before release.
- Performed vulnerability assessment and application security testing using Burp Suite, OWASP ZAP, MobSF, Snyk, SonarQube, Nmap, and related tools, and supported remediation verification.
- Conducted performance and reliability testing using k6 and JMeter to identify application behavior and potential issues under different workloads.
- Supported deployment and release-readiness activities across AWS and CI/CD environments, including deployment verification, troubleshooting, service validation, environment review, and post-deployment testing.
- Contributed to security, privacy, governance, risk, and compliance reviews by assessing technical requirements, identifying gaps, and supporting reporting, documentation, and remediation activities.
- Collaborated with development, QA, UI/UX, DevOps, management, and operational teams to improve product quality, security, reliability, and overall release readiness.

#### QA & Security Engineer Intern

**Employer:** SAĜO MENTE INTERNATIONAL SDN. BHD.  
**Metadata:** March 2026 – June 2026 Internship QA Testing | Security Testing | Deployment Support

Completed an internship focused on QA testing, security validation, vulnerability assessment support, API testing, deployment support, documentation, and platform readiness activities.

**Responsibilities:**

- Conducted manual, functional, regression, usability, end-to-end, user acceptance, and mobile application testing across web and mobile platforms.
- Tested core application workflows and APIs, identifying functional issues, UI/UX inconsistencies, workflow gaps, and security concerns.
- Documented and tracked defects in Jira, reproduced reported issues, and performed re-testing after bug fixes, workflow changes, and deployments.
- Assisted with application security testing covering authentication, authorization, session handling, input validation, API security, vulnerability assessment, and remediation validation.
- Used Postman, Swagger/OpenAPI, Burp Suite, OWASP ZAP, Snyk, SonarQube, Nmap, and Nikto during QA and security testing activities.
- Supported deployment verification, environment readiness checks, and release validation.
- Prepared technical documentation, test findings, and security-related reports.
- Collaborated with developers, QA team members, UI/UX designers, and management to validate fixes and improve application quality and release readiness.

#### Help Desk Representative

**Employer:** Tech Bridge Solutions Ltd  
**Metadata:** Remote February 2025 – Present IT Support Technical Support | Troubleshooting | User Support

Provide user support through troubleshooting, issue guidance, complaint registration, information updates, and escalation handling. This role strengthened my structured communication, incident handling discipline, technical troubleshooting, documentation habits, and practical service support skills that transfer well into QA and security operations.

**Responsibilities:**

- Provide remote technical support by troubleshooting user issues and delivering practical solutions that minimize disruption and downtime.
- Log incidents, complaints, and service requests accurately while maintaining up-to-date user and support records in internal systems.
- Diagnose common technical issues, provide step-by-step guidance, and escalate complex cases to the appropriate internal teams when required.
- Communicate clearly with users throughout the support process, provide timely updates, and follow issues through to resolution to support service continuity.
- Apply structured support workflows, issue tracking, customer-focused problem solving, and cross-team coordination within a remote support environment.

#### Inventory Manager & Cashier

Inventory Manager & Cashier Bilaal Kidz January 2022 – January 2024 Operations Managed inventory, point-of-sale workflows, stock accuracy, and day-to-day operational processes. This experience strengthened my organization, accountability, accuracy, customer service, and process discipline. Transferable Skills Process Discipline Accuracy Customer Service Stock Management Accountability Operational Coordination

#### Administrative Assistant

Administrative Assistant Care and Cure Medical Center June 2021 – December 2021 Administration Supported appointment scheduling, documentation, coordination, and daily administrative activities. This role strengthened my communication, attention to detail, documentation accuracy, and stakeholder coordination skills. Transferable Skills Documentation Appointment Coordination Communication Attention to Detail Administrative Support Stakeholder Coordination

### Education

| Source | Institution / program | Dates / academic information |
| --- | --- | --- |
| about.html | The Open University of Sri Lanka — BSc (Hons) Information Technology | Undergraduate; expected November 2027. Focus: IT, cybersecurity, QA, cloud security, systems/infrastructure and GRC. No CGPA shown here. |
| about.html | University of Minnesota — Software Testing and Automation Specialization | August 2026–August 2027; test concepts/design, automation principles and QA. A specialization, not a degree. |
| Resume/generate_resume.py | Open University — BSc (Hons) in IT | November 2023–November 2027; current CGPA 3.46; Member, iTeam. Source-only facts, not checked against transcript or PDF. |
| Resume/generate_resume.py | Minnesota / Coursera specialization | In progress; completed Introduction to Software Testing course separately appears in certifications.html. |

### Conflicting or supplementary resume-source facts

- Website July–September 2026 title is **QA & Security Engineer Trainee**; generator uses **QA & Security Engineer**, full-time. Confirm official title/category rather than selecting one by inference.
- Administrative Assistant dates are **June–December 2021** on website, **May–November 2021** in generator.
- Help Desk role is remote, February 2025–Present on website. Generator additionally says part-time and supplies employer location. Overlapping 2026 employment is not automatically an error; confirm arrangements.
- Generator additionally claims barcode-based inventory processing/reconciliation and digitized administrative workflows. Verify before highlighting as achievements.
- Company capitalization varies; recommendation says Care & Cure versus experience Care and Cure. Confirm official names.
- Do not equate generator with current PDF: generator was read in UTF-8 but not run, and PDF text/layout was not compared.

### Skills, tools and existing proficiency presentation

The following inventory preserves the skills page's groupings, descriptions, technology tags and explicit labels. These include Practical Experience, Working Knowledge, Awareness and Currently Building. There are no percentage bars. Growth targets must not become mastered skills during migration.

#### Primary QA and security engineering capabilities

- Practical Experience QA Engineering Practical experience in validating platform features, testing workflows, supporting UAT, tracking defects, and improving release confidence. Manual Testing Functional Testing Regression Testing User Acceptance Testing Test Case Design Workflow Validation Defect Reporting Jira Issue Tracking

- Working Knowledge Application Security Hands-on exposure to web application security testing, vulnerability review, OWASP-focused validation, and remediation support. Web Application Security Testing OWASP-Oriented Testing Authentication Behavior Review Request Validation Security Review Support Remediation Verification Secure Development Awareness

- Practical Experience API Security & Testing Experience in validating APIs for functionality, behavior, request handling, and security-related concerns using Postman and Swagger. API Testing Request Validation Response Verification Postman Swagger / OpenAPI Security Behavior Review Functional API Validation

- Practical Experience Vulnerability Management Practical exposure to reviewing security findings, validating remediation, supporting risk-based decisions, and documenting security issues clearly. Vulnerability Assessment Vulnerability Review Remediation Tracking Validation of Fixes Dependency Scanning Awareness Risk-Based Prioritization Security Reporting

- Working Knowledge Cloud Security Validation Experience supporting cloud deployment verification, environment validation, and production readiness checks with a security-focused mindset. AWS Exposure Deployment Verification Environment Review Release Readiness Checks Cloud Security Awareness Infrastructure Validation Secure Configuration Awareness

- Practical Experience Governance, Risk & Compliance Experience supporting governance, risk, compliance, and security documentation activities for delivery teams. Risk Assessment Support Compliance Review Support Governance Documentation Security Reporting Policy Awareness Risk-Based Thinking Technical Documentation

#### Grouped tools for testing, validation, infrastructure, and development

- Working Knowledge Security Tools OWASP ZAP Burp Suite Snyk SonarQube Nmap Nikto Wireshark

- Practical Experience QA & API Tools Postman Swagger / OpenAPI Jira Test Case Documentation Bug Tracking UAT Documentation

- Working Knowledge Cloud & Infrastructure AWS Linux Windows Administration Endpoint Management Server Administration Cloud Computing Deployment Verification

- Working Knowledge Development & Scripting Next.js React Node.js TypeScript PostgreSQL Prisma Python PowerShell Bash

#### Supportive blue-team knowledge without overclaiming

- SOC Fundamentals Security Operations Center Fundamentals Alert Triage Incident Response Fundamentals Threat Detection

- Monitoring Awareness SIEM Awareness Splunk Exposure QRadar Awareness Log Analysis Suspicious Pattern Identification

- Defensive Controls Firewalls & IDS/IPS Concepts Suricata Awareness Endpoint Protection Awareness Packet Analysis Awareness

#### Systems knowledge that strengthens troubleshooting and validation

- Network Foundations TCP/IP DNS HTTP / HTTPS SSL / TLS Awareness LDAP Awareness Active Directory Awareness

- System Administration Windows Administration Linux Administration Endpoint Management Server Administration Cloud Computing

- Support Practice Troubleshooting Escalation Handling User Support Complaint Handling Documentation

#### Investigation, reasoning, and root-cause thinking

- Threat Detection Identify suspicious behavior Spot anomalies Review indicators Use evidence for investigation

- Critical Thinking Differentiate real issues from false positives Review technical findings carefully Connect findings to business and security risk

- Problem Solving Investigate issues Analyze root causes Recommend mitigation strategies Support long-term improvements

- Troubleshooting Replicate issues Isolate root causes Validate fixes Document findings clearly

#### Reliable habits for QA, security, IT support, and delivery teams

Cross-functional Collaboration; Clear Communication; Documentation & Reporting; Time Management; Adaptability; Customer Service; Patience Under Pressure; Production Readiness Mindset; Responsible Security Practice

#### Skill areas I am actively building

- Detection & Monitoring Currently Building SIEM Engineering Threat Hunting Detection Engineering Security Monitoring

- Cloud Response Currently Building Cloud Incident Response Advanced Vulnerability Management Security Automation

- Advanced Practice Currently Building Purple Teaming AI/ML in Cybersecurity Responsible Security Research

#### Applied across QA engineering, cybersecurity, cloud validation, and secure delivery

## 6. Projects and Certifications Inventory

### Project/practice catalogue

There are **24 named entries**: five featured professional/personal projects; six security-lab/platform entries; seven virtual simulations; six software/academic entries. Platform practice and course simulations should not be presented as independently shipped software products.

No project-specific source repository links appear in these cards. A generic GitHub profile link is not a substitute. No project screenshot sets, project source folders, separate case-study documents, technical README files or architecture diagrams for these projects were found in this checkout. Native capability lists are descriptions, not independent implementation evidence. AssureX has an external app demo; other outbound project links generally identify learning profiles. External demo operation/ownership was not tested. All project descriptions/statuses below are source claims.

#### 1. SAĜO MENTE Security & QA Initiatives

- **Status:** Professional
- **Category/dates:** Professional Experience | QA & Security
- **Description:** Security and QA-related initiatives supporting platform quality, security validation, deployment readiness, and governance-aligned documentation for a global digital marketplace platform.
- **Technologies/skills:** QA Testing Security Testing Application Security API Testing Vulnerability Management AWS Validation GRC Jira
- **Repository:** not linked in card.
- **Demo/related links:** View Experience → experience.html
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Capabilities/contributions:**

- Supported web application security testing across platform workflows.
- Performed vulnerability review and remediation validation support.
- Conducted API testing and request validation using Postman and Swagger.
- Supported QA testing, UAT execution, regression validation, and workflow checks.
- Logged, tracked, and validated issues, bugs, and enhancements through Jira.
- Assisted with AWS deployment verification and production readiness checks.
- Prepared cybersecurity, compliance, GRC, and testing-related documentation.

#### 2. AssureX – Enterprise Quality, Security & Risk Assurance Platform

- **Status:** Completed
- **Category/dates:** Enterprise QA, Security & Risk Platform | May 2026 - Aug 2026
- **Description:** AssureX is a full-stack quality, security, and risk assurance platform designed to centralize software QA, vulnerability management, remediation tracking, security risks, and audit activities within a single system.
- **Technologies/skills:** Next.js TypeScript Tailwind CSS Prisma ORM PostgreSQL JWT MFA Playwright Docker Security Headers Audit Logging
- **Repository:** not linked in card.
- **Demo/related links:** View Project → https://assurex-eight.vercel.app
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Capabilities/contributions:**

- Provides dedicated QA and Security workspaces with secure authentication, role-based access control, and multi-factor authentication.
- Supports QA test case creation, execution management, and automated Playwright end-to-end testing.
- Centralizes vulnerability, remediation, asset, and security risk management.
- Uses CVSS v3.1 scoring to support risk assessment and prioritization.
- Includes security audit logging, application security controls, and security headers.
- Provides executive dashboards, operational reporting, and downloadable PDF security reports.

#### 3. VeriGuard – Hybrid QA Automation & Testing Platform

- **Status:** In Progress
- **Category/dates:** QA Automation & Testing Platform | Aug 2026 - Present
- **Description:** Developing VeriGuard, a scalable QA automation and testing platform designed to manage testing across organizations, projects, and multiple environments from a centralized dashboard.
- **Technologies/skills:** TypeScript Next.js React NestJS PostgreSQL Prisma Redis BullMQ Docker Jest REST APIs AES-256-GCM
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Capabilities/contributions:**

- Built with a Next.js dashboard, NestJS API and worker services, PostgreSQL with Prisma, and Redis and BullMQ-based task processing.
- Supports project and environment management, task lifecycle tracking, cancellation controls, health and readiness monitoring, and automated API integration testing.
- Uses AES-256-GCM encryption for sensitive credentials with controlled handling of testing environments and configuration data.
- Designed around modular architecture, automation, security, scalability, reliability, and the safe execution of testing workflows.

#### 4. MailForge – Email Campaign & Tracking Automation Platform

- **Status:** In Progress
- **Category/dates:** Email Campaign Automation Platform | Jun 2026 - Present
- **Description:** MailForge is an email campaign automation and tracking platform designed to manage bulk email delivery, campaign scheduling, recipient management, attachments, and engagement monitoring from a centralized system.
- **Technologies/skills:** Node.js Next.js TypeScript SMTP Database Management Email Tracking Campaign Automation
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Capabilities/contributions:**

- Supports bulk and scheduled email campaigns with structured, controlled delivery workflows.
- Provides contact and recipient management with reusable email templates.
- Includes SMTP configuration, delivery handling, and attachment support.
- Tracks email opens, link clicks, delivery status, and bounces.
- Provides campaign reporting and administrative visibility over campaign activity.
- Focuses on reliability, campaign visibility, and practical handling of high-volume communication workflows.

#### 5. Personal Portfolio Website

- **Status:** Personal Brand
- **Category/dates:** Personal Branding | Web Development
- **Description:** A static professional portfolio website built with HTML, CSS, and JavaScript to present my QA, cybersecurity, cloud validation, project work, certifications, and professional experience in a clean responsive layout.
- **Technologies/skills:** HTML CSS JavaScript Responsive Design Portfolio Personal Branding
- **Repository:** not linked in card.
- **Demo/related links:** Visit Portfolio → index.html
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Capabilities/contributions:**

- Responsive professional portfolio structure.
- Project, experience, certification, and recommendation sections.
- Personal branding aligned with QA and cybersecurity career goals.

#### 6. Defensive Cybersecurity Home Lab

- **Status:** Lab
- **Category/dates:** Blue Team Lab | Defensive Security
- **Description:** A controlled home lab simulating enterprise-style endpoints, servers, segmented networks, firewall controls, and monitoring tooling for blue team practice.
- **Technologies/skills:** Home Lab Log Analysis Threat Detection Incident Response Network Segmentation Monitoring
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Capabilities/contributions:**

- Log analysis and alert review.
- Threat detection and incident response practice.
- Network segmentation and defensive monitoring.

#### 7. OWASP-Oriented Web Testing

- **Status:** AppSec Lab
- **Category/dates:** Application Security Lab
- **Description:** Practical web application testing aligned with common OWASP risks, including request manipulation, authentication behavior review, input validation checks, and remediation verification.
- **Technologies/skills:** OWASP Web Security Authentication Testing Request Validation Remediation Verification
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Capabilities/contributions:**

- Web application security testing.
- Authentication behavior review.
- Request manipulation and validation testing.
- Remediation verification.

#### 8. Cloud Security Experiments

- **Status:** Cloud Lab
- **Category/dates:** Cloud Security Lab
- **Description:** Cloud-focused learning and experiments covering deployment validation, exposure review, environment checks, and secure service configuration awareness.
- **Technologies/skills:** Cloud Security AWS Deployment Validation Environment Review Secure Configuration
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Capabilities/contributions:**

- Cloud deployment validation and AWS security awareness.
- Environment checks and exposure review.
- Release readiness validation.

#### 9. LetsDefend

- **Status:** SOC
- **Category/dates:** SOC Simulation Platform
- **Description:** SOC-focused investigation practice covering SIEM alerts, phishing, malware analysis, web attacks, and incident handling workflows.
- **Technologies/skills:** SOC SIEM Alerts Phishing Analysis Malware Analysis Incident Response Web Attacks
- **Repository:** not linked in card.
- **Demo/related links:** View Profile → https://app.letsdefend.io/user/cybersentinel
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

#### 10. TryHackMe

- **Status:** Hands-On
- **Category/dates:** Cybersecurity Learning Platform
- **Description:** Hands-on rooms and guided security practice supporting defensive security, security operations, and applied investigation skills.
- **Technologies/skills:** Defensive Security SOC Investigation Security Practice Hands-On Labs
- **Repository:** not linked in card.
- **Demo/related links:** View Profile → https://tryhackme.com/p/cybersentinel01
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

#### 11. PicoCTF

- **Status:** CTF
- **Category/dates:** CTF Practice
- **Description:** Capture-the-flag practice focused on web security, cryptography, forensics, reverse engineering, and general cybersecurity problem solving.
- **Technologies/skills:** CTF Web Security Cryptography Forensics Reverse Engineering Problem Solving
- **Repository:** not linked in card.
- **Demo/related links:** View Profile → https://play.picoctf.org/users/cybersentinel01
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

#### 12. Commonwealth Bank Introduction to Cybersecurity

- **Status:** Simulation
- **Category/dates:** Forage — March 2026
- **Description:** Worked through fraud detection, Splunk dashboard thinking, incident response procedures, security awareness communication, and vulnerability remediation recommendations.
- **Technologies/skills:** Not separately stated
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Supporting certificate:** `Certificates/cybercommomwealth.jpg`

#### 13. Datacom Cybersecurity Job Simulation

- **Status:** Simulation
- **Category/dates:** Forage — March 2026
- **Description:** Investigated a simulated cyberattack, completed risk assessment activity, and prepared recommendations to improve a client's cybersecurity posture.
- **Technologies/skills:** Not separately stated
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Supporting certificate:** `Certificates/Datacom Cybersecurity Job Simulation on Forage.jpg`

#### 14. Commonwealth Bank Tech Explorer

- **Status:** Simulation
- **Category/dates:** Forage — March 2026
- **Description:** Practiced requirement gathering, user group identification for secure access, and customer demographic analysis across technology team scenarios.
- **Technologies/skills:** Not separately stated
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Supporting certificate:** `Certificates/Comonwealth.jpg`

#### 15. AIG Shields Up

- **Status:** Simulation
- **Category/dates:** Forage — February 2026
- **Description:** Researched reported vulnerabilities, reviewed CISA publications, drafted remediation guidance, and applied Python scripting to support ethical security testing.
- **Technologies/skills:** Not separately stated
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Supporting certificate:** `Certificates/aig.jpg`

#### 16. Tata Cybersecurity Security Analyst

- **Status:** Simulation
- **Category/dates:** Forage — February 2026
- **Description:** Focused on IAM, access control assessment, security strategy alignment, and documentation for technical and non-technical stakeholders.
- **Technologies/skills:** Not separately stated
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Supporting certificate:** `Certificates/Tata.jpg`

#### 17. Deloitte Australia Cyber Job Simulation

- **Status:** Simulation
- **Category/dates:** Forage — February 2026
- **Description:** Analyzed web activity logs, identified suspicious behavior, answered incident-response questions, and assessed indicators of compromise.
- **Technologies/skills:** Not separately stated
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Supporting certificate:** `Certificates/Delloite.jpg`

#### 18. Mastercard Cybersecurity Virtual Experience

- **Status:** Simulation
- **Category/dates:** Forage — January 2026
- **Description:** Identified and reported phishing threats, analyzed security training needs, and contributed to awareness-focused defense improvements.
- **Technologies/skills:** Not separately stated
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

**Supporting certificate:** `Certificates/Forage.jpg`

#### 19. Smart Bus Route Finder

- **Status:** Academic
- **Category/dates:** Logic Programming | Prolog
- **Description:** A Prolog-based path-finding system using BFS, DFS, and A* to calculate routes between cities with validation and scalable rule structure.
- **Technologies/skills:** Prolog BFS DFS A* Path Finding Algorithmic Thinking
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

#### 20. AI Expert System: Tech Career Advisor

- **Status:** Academic
- **Category/dates:** Expert System | Prolog
- **Description:** A rule-based Prolog expert system that evaluates user interests, skills, and certification status to recommend suitable technology career paths.
- **Technologies/skills:** Prolog Rule-Based System Career Recommendation Logic Programming
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

#### 21. Tic-Tac-Toe Game

- **Status:** Completed
- **Category/dates:** Python GUI Project
- **Description:** A two-player Tkinter game with turn logic, win detection, reset functionality, and event-driven interface handling.
- **Technologies/skills:** Python Tkinter GUI Game Logic Event Handling
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

#### 22. Simple Calculator

- **Status:** Completed
- **Category/dates:** Python GUI Project
- **Description:** A Tkinter calculator application with fundamental arithmetic operations, interactive buttons, and responsive display handling.
- **Technologies/skills:** Python Tkinter GUI Arithmetic Event Handling
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

#### 23. Basic Hospital Appointment System

- **Status:** Academic
- **Category/dates:** Java System Project
- **Description:** An object-oriented Java system for patient registration, appointment booking, and doctor schedule management through structured backend logic.
- **Technologies/skills:** Java OOP Healthcare Appointment Management Backend Logic
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

#### 24. GPA Calculator

- **Status:** CLI
- **Category/dates:** Java CLI Project
- **Description:** A command-line GPA calculator tailored to a BSc IT curriculum with subject, credit hour, grade input, validation, and calculation logic.
- **Technologies/skills:** Java CLI Input Validation Calculation Logic Academic Tool
- **Repository:** not linked in card.
- **Demo/related links:** None supplied.
- **Screenshots/documentation:** no separate local screenshots or technical documents found.

### Certifications — complete card inventory

There are **44 cards using 43 unique certificate images**. Accelerate Your Job Search with AI appears twice in different tracks using the same image; it is one credential. The folder has 50 certificate scans: 43 used here and seven simulations on Projects.

**Verification:** no external credential/issuer verification links appear on certifications.html. Each card opens a local scan, which is not independent issuer verification. Issuers/dates/expiry below are website statements. No certificate serials, QR payloads, signatures or scan text were extracted. Credential validity and recognition are unverified. ISO/IEC 27701:2025 explicitly lists an expiry; no unstated expiry is inferred.

| Title | Issuer / dates / expiry | Track | Asset path | Verification |
| --- | --- | --- | --- | --- |
| Google Cybersecurity Professional Certificate | Google — Aug 2025 – Jan 2026 | Core Cybersecurity | Certificates/GoogleCybersecurity.jpg | Local preview only; no credential URL |
| Junior Cybersecurity Analyst | Cisco Networking Academy — Jan 2025 – Jul 2025 | SOC & Cybersecurity | Certificates/JuniorCybersecurityAnalyst.jpg | Local preview only; no credential URL |
| Certified Phishing Prevention Specialist (CPPS) | Hack&Fix Academy — Dec 2025 | Security Awareness / Phishing Defense | Certificates/CPPS.jpg | Local preview only; no credential URL |
| Introduction to Software Testing | University of Minnesota — Sep 2026 | QA & Software Testing | Certificates/Introduction to Software Testing.jpg | Local preview only; no credential URL |
| ISO/IEC 27701:2025 Lead Auditor | Mastermind — Issued Aug 2026 Expires Jul 2029 | Core Cybersecurity | Certificates/ISOIEC 277012025 Lead Auditor.jpg | Local preview only; no credential URL |
| Sound the Alarm: Detection and Response | Google — Dec 2025 | Core Cybersecurity | Certificates/SoundsAlarm.jpg | Local preview only; no credential URL |
| Assets, Threats, and Vulnerabilities | Google — Nov 2025 | Core Cybersecurity | Certificates/Assets, Threats, and Vulnerabilities.jpg | Local preview only; no credential URL |
| IT Security: Defense against the Digital Dark Arts | Google — Oct 2025 | Core Cybersecurity | Certificates/IT_Security.jpg | Local preview only; no credential URL |
| Play It Safe: Manage Security Risks | Google — Sep 2025 | Core Cybersecurity | Certificates/Managerisk.jpg | Local preview only; no credential URL |
| Foundations of Cybersecurity | Google — Aug 2025 | Core Cybersecurity | Certificates/Foundation_Cybersecurity.jpg | Local preview only; no credential URL |
| Cyber Kill Chains | Cybrary — Jul 2025 | Core Cybersecurity | Certificates/cyberkill.jpg | Local preview only; no credential URL |
| Introduction to Cryptography | Wolfram U — Jul 2025 | Core Cybersecurity | Certificates/Intro_cryptography.jpg | Local preview only; no credential URL |
| Cyber Security Track | SLASSCOM — Dec 2024 | Core Cybersecurity | Certificates/cyber_track.jpg | Local preview only; no credential URL |
| Security Operations Center (SOC) | Cisco — Oct 2025 | SOC & Threat Detection | Certificates/socanalyst.jpg | Local preview only; no credential URL |
| Operationalizing MITRE ATT&CK for SOCs | Picus Security — Aug 2025 | SOC & Threat Detection | Certificates/operationalizing-mitre-attck-for-socs.jpg | Local preview only; no credential URL |
| Cyber Threat Management | Cisco Networking Academy — Jul 2025 | SOC & Threat Detection | Certificates/cyberthreat.jpg | Local preview only; no credential URL |
| Endpoint Security | Cisco Networking Academy — Jul 2025 | SOC & Threat Detection | Certificates/Endpoint.jpg | Local preview only; no credential URL |
| Network Defense | Cisco Networking Academy — Jul 2025 | SOC & Threat Detection | Certificates/Network_Defence.jpg | Local preview only; no credential URL |
| Student SOC Program - Foundations | Microsoft — May 2025 | SOC & Threat Detection | Certificates/soc.jpg | Local preview only; no credential URL |
| Intro to Splunk (eLearning) | Splunk — Feb 2026 | SOC & Threat Detection | Certificates/Splunk.jpg | Local preview only; no credential URL |
| Tools of the Trade: Linux and SQL | Google — Oct 2025 | Networking & Systems | Certificates/Linex&SQL.jpg | Local preview only; no credential URL |
| Connect & Protect: Network & Network Security | Google — Sep 2025 | Networking & Systems | Certificates/ConnectNetwork.jpg | Local preview only; no credential URL |
| Networking Devices & Initial Configuration | Cisco Networking Academy — Jun 2025 | Networking & Systems | Certificates/networkconfig.jpg | Local preview only; no credential URL |
| Networking Basics | Cisco Networking Academy — May 2025 | Networking & Systems | Certificates/networkbasics.jpg | Local preview only; no credential URL |
| Computer Hardware Basics | Cisco Networking Academy — Oct 2024 | Networking & Systems | Certificates/hardware.jpg | Local preview only; no credential URL |
| Introduction to Linux (LFS101) | The Linux Foundation — Dec 2024 | Networking & Systems | Certificates/Intro_Linux.jpg | Local preview only; no credential URL |
| CS401: Operating Systems | Saylor Academy — Dec 2024 | Networking & Systems | Certificates/CS401_OS.jpg | Local preview only; no credential URL |
| System Administration and IT Infrastructure Services | Google — Feb 2026 | Networking & Systems | Certificates/System Admin.jpg | Local preview only; no credential URL |
| Certified Artificial Intelligence Security & Risk (CAISR) | Red Team Leaders — May 2026 | Cloud & Emerging Tech | Certificates/Certified Artificial Intelligence Security & Risk (CAISR).jpg | Local preview only; no credential URL |
| AI Security Fundamentals | Varonis — Apr 2026 | Cloud & Emerging Tech | Certificates/AI Security Fundamentals!_Cert.jpg | Local preview only; no credential URL |
| Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate | Oracle — Aug 2025 | Cloud & Emerging Tech | Certificates/oracle.jpg | Local preview only; no credential URL |
| Introduction to CIP | OPSWAT Academy — Mar 2026 | Cloud & Emerging Tech | Certificates/introduction_to_cip.png | Local preview only; no credential URL |
| Accelerate Your Job Search with AI | Google — Jan 2026 | Cloud & Emerging Tech | Certificates/Accelerate Your Job Search with AI.jpg | Local preview only; no credential URL |
| Mental Health in Cybersecurity | Security Blue Team — May 2025 | Cloud & Emerging Tech | Certificates/Mental_Health.jpg | Local preview only; no credential URL |
| Automate Cybersecurity Tasks with Python | Google — Jan 2026 | Programming & Development | Certificates/AutomateTasks.jpg | Local preview only; no credential URL |
| Python Programming | GeeksForGeeks — Dec 2025 | Programming & Development | Certificates/Python GFG.jpg | Local preview only; no credential URL |
| Full Stack Development (HTML, CSS, Java, JavaScript) | Udemy — Mar 2025 | Programming & Development | Certificates/FullStack.jpg | Local preview only; no credential URL |
| The Git & GitHub Bootcamp | Udemy — Sep 2024 | Programming & Development | Certificates/GitHub.jpg | Local preview only; no credential URL |
| Java Programming | Programming Hero — May 2024 | Programming & Development | Certificates/java_fundamental.jpg | Local preview only; no credential URL |
| User Experience Design - Learn UI/UX with Figma | Udemy — Sep 2025 | Programming & Development | Certificates/UIUX_Design.jpg | Local preview only; no credential URL |
| Technical Support Fundamentals | Google / Coursera — Jun 2024 | IT Support & Professional Skills | Certificates/Tecgnical_support.jpg | Local preview only; no credential URL |
| Practical Help Desk | TCM Security — Jan 2025 | IT Support & Professional Skills | Certificates/practical-help-desk.jpg | Local preview only; no credential URL |
| Put It to Work: Prepare for Cybersecurity Jobs | Google — Jan 2026 | IT Support & Professional Skills | Certificates/Put It to Work.jpg | Local preview only; no credential URL |
| Accelerate Your Job Search with AI | Google — Jan 2026 | IT Support & Professional Skills | Certificates/Accelerate Your Job Search with AI.jpg | Local preview only; no credential URL |

### Digital badges and reward links

About has 17 badge cards and Projects nine LetsDefend achievements. Badges/isc2-candidate.png is unreferenced. A badge is supporting evidence, not automatically a separate professional certification. The table records exact achievement URLs where supplied.

| Page | Badge label | Asset | Associated link |
| --- | --- | --- | --- |
| about.html | ISO/IEC 27701:2025 Lead Auditor badge | Badges/iso-iec-27701-2025-lead-auditor.png | No verification link |
| about.html | AI Security Fundamentals badge | Badges/AI Security Fundamentals_Badge.png | No verification link |
| about.html | OPSWAT Introduction to Critical Infrastructure Protection badge | Badges/opswat-introduction-to-critical-infrastructure-protection-icip.png | No verification link |
| about.html | Google Cybersecurity Professional Certificate badge | Badges/google-cybersecurity-professional-certificate-v-2 (1).png | No verification link |
| about.html | Certified Phishing Prevention Specialist badge | Badges/CPPS.jpg | No verification link |
| about.html | Junior Cybersecurity Analyst badge | Badges/junior-cybersecurity-analyst-career-path.1.png | No verification link |
| about.html | Oracle Cloud Infrastructure AI Foundations badge | Badges/OCI25AICFAV1.png | No verification link |
| about.html | Linux Foundation LFS101 badge | Badges/lfs101-introduction-to-linux.png | No verification link |
| about.html | Purple Academy badge | Badges/29729252200878.png | No verification link |
| about.html | Cyber Threat Management badge | Badges/cyber-threat-management.png | No verification link |
| about.html | Endpoint Security badge | Badges/endpoint-security.png | No verification link |
| about.html | Network Defense badge | Badges/network-defense.png | No verification link |
| about.html | English for IT badge | Badges/english-for-it-1.png | No verification link |
| about.html | Networking Basics badge | Badges/networking-basics.png | No verification link |
| about.html | Networking Devices and Initial Configuration badge | Badges/networking-devices-and-initial-configuration.png | No verification link |
| about.html | Operating Systems Basics badge | Badges/operating-systems-basics.png | No verification link |
| about.html | Computer Hardware Basics badge | Badges/computer-hardware-basics.png | No verification link |
| projects.html | Malware Analyzer badge | Badges/Malware Analyzer.png | https://app.letsdefend.io/my-rewards/detail/3f78042e-bdad-4fb8-a1cb-d05fcabaec2d |
| projects.html | How to investigate a SIEM alert badge | Badges/SIEM.png | https://app.letsdefend.io/my-rewards/detail/4c45ad6a-c7c6-4d3f-918b-e86b604d0f0f |
| projects.html | Web Attack Investigated badge | Badges/Web Attack Investigated.png | https://app.letsdefend.io/my-rewards/detail/472d824a7f7e4c44a46fbc15edf75457 |
| projects.html | Web Attack Investigator badge | Badges/Web Attack Investigator.png | https://app.letsdefend.io/my-rewards/detail/fd0ab1fe-81cc-49a9-b599-1cc7dd4a751f |
| projects.html | Incident Handler 2 badge | Badges/Incident Handler - 2.png | https://app.letsdefend.io/my-rewards/detail/2a20f2a9-39a4-4e27-ac3f-3bc631a463d1 |
| projects.html | Incident Handler badge | Badges/Incident Handler.png | https://app.letsdefend.io/my-rewards/detail/0fa9f702-aadd-4535-b970-5b50c30e5559 |
| projects.html | First Blood badge | Badges/First Blood.png | https://app.letsdefend.io/my-rewards/detail/dd03b799-186f-4552-b3e1-c489ca21a61c |
| projects.html | Phishing Expert badge | Badges/Phishing Expert.png | https://app.letsdefend.io/my-rewards/detail/f6f51586-c9ef-4855-8fc1-ea60d6d5b8e7 |
| projects.html | SOC Member badge | Badges/SOC Member.png | https://app.letsdefend.io/my-rewards/detail/464f873b-aec9-459f-b938-d1cdc102004d |

### Recommendations — complete public text

Six attributed recommendations exist. No photographs are used; initials styled with CSS are intentional avatars. Only one recommender has an individual profile link. Presence in source does not independently verify identity, consent or authenticity. Preserve exact quotes rather than rewriting them to imply new support experience.

#### Mr. Hemal Tharaka Eranga

**Title/organization:** DevOps Engineer; SAĜO MENTE INTERNATIONAL SDN. BHD.

> “Rimsan has supported web and mobile QA testing, cybersecurity checks, system security verification, and development support at SAĜO. He is hardworking, responsible, and eager to learn, with strong potential to grow in QA, cybersecurity, and development.”

**Links:** None in source.  
**Image assets:** none; CSS initials.

#### Mr. Nimesh Piyumantha

**Title/organization:** Project Lead; SAĜO MENTE INTERNATIONAL SDN. BHD.

> “I had the pleasure of working with Rimsan at SAĜO. He is a responsible, dedicated, and supportive team member with strong attention to detail, particularly in QA and security. His willingness to learn and collaborate makes him a valuable addition to any team. I highly recommend him for his professionalism and commitment.”

**Links:** https://www.linkedin.com/in/nimesh-piyumantha/  
**Image assets:** none; CSS initials.

#### Mr. Gayeshan Mithige

**Title/organization:** Managing Director; Tech Bridge Solutions Ltd

> “Rimsan’s strong communication skills, professionalism, reliability, and friendly approach make him a highly valued and dependable member of our team.”

**Links:** None in source.  
**Image assets:** none; CSS initials.

#### Ms. Amani Zulfi

**Title/organization:** Intern - UX/UI Designer; FAITE PVT LTD

> “Rimsan's a dedicated and hardworking person who always shows great enthusiasm for learning, and teamwork.”

**Links:** None in source.  
**Image assets:** none; CSS initials.

#### Mr. K. Ahamed Ammar

**Title/organization:** Managing Director; Bilaal Kidz

> “Rimsan consistently demonstrates professionalism, integrity, and a collaborative spirit—qualities that make him an asset to any team.”

**Links:** None in source.  
**Image assets:** none; CSS initials.

#### Dr. MH. Mohamed Sabir

**Title/organization:** Managing Director; Care & Cure Medical Center

> “Rimsan’s diligence, helpful nature, and outstanding contributions have made him a highly valued and respected member of our team.”

**Links:** None in source.  
**Image assets:** none; CSS initials.

## 7. Asset Inventory

File sizes and dimensions were measured locally using filesystem reads and Pillow; originals were not changed. Sizes below use KiB; dimensions are intrinsic width × height. Use includes local favicon references. Social metadata also points to the portrait through absolute URLs. Unreferenced means no inspected local HTML reference; CSS was separately checked and uses gradients rather than legacy JPG backgrounds.

**Counts:** 50 certificate scans, 27 badge images, 10 Images files and two root backgrounds = **89 raster images**; plus one resume PDF = **90 binary assets**, **79,399,262 bytes / approximately 75.7 MiB**. No local SVGs, webfont files, employer logo set, project screenshot set, recommender photos or additional document formats were found. The Python generator is a source utility, not an alternative resume document.

Reuse judgments are technical triage, not visual approval: images were decoded for dimensions, not visually reviewed. Preserve originals and existing URLs; create optimized derivatives only during a later authorized implementation. Do not rename typo-containing certificate paths without a compatibility plan.

| Filename / relative path | Type | Dimensions | Approx. size | Current use | Reuse assessment |
| --- | --- | --- | --- | --- | --- |
| Background_dark.jpg | JPG | 3000 × 2000 | 188.4 KiB | Unreferenced | Legacy; retain original pending design decision. |
| Background_light.jpg | JPG | 3000 × 2000 | 594.8 KiB | Unreferenced | Legacy; retain original pending design decision. |
| Badges/29729252200878.png | PNG | 1000 × 1000 | 139.9 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/AI Security Fundamentals_Badge.png | PNG | 500 × 581 | 28.8 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/computer-hardware-basics.png | PNG | 204 × 204 | 29.7 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/CPPS.jpg | JPG | 1071 × 1037 | 164.8 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/cyber-threat-management.png | PNG | 600 × 600 | 99.2 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/endpoint-security.png | PNG | 2048 × 2048 | 364.5 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/english-for-it-1.png | PNG | 204 × 204 | 26.1 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/First Blood.png | PNG | 200 × 225 | 14.1 KiB | projects.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/google-cybersecurity-professional-certificate-v-2 (1).png | PNG | 1200 × 1200 | 310.2 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/Incident Handler - 2.png | PNG | 204 × 222 | 21.5 KiB | projects.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/Incident Handler.png | PNG | 190 × 238 | 26.9 KiB | projects.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/isc2-candidate.png | PNG | 600 × 600 | 44.9 KiB | Unreferenced | Reusable supporting badge; verify relevance/provenance. |
| Badges/iso-iec-27701-2025-lead-auditor.png | PNG | 2028 × 2028 | 379.2 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/junior-cybersecurity-analyst-career-path.1.png | PNG | 600 × 600 | 107.9 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/lfs101-introduction-to-linux.png | PNG | 2048 × 2048 | 250.3 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/Malware Analyzer.png | PNG | 206 × 222 | 14.6 KiB | projects.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/network-defense.png | PNG | 600 × 600 | 91.1 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/networking-basics.png | PNG | 650 × 650 | 116.1 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/networking-devices-and-initial-configuration.png | PNG | 650 × 650 | 129.2 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/OCI25AICFAV1.png | PNG | 552 × 276 | 61.4 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/operating-systems-basics.png | PNG | 2048 × 2048 | 246.5 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/opswat-introduction-to-critical-infrastructure-protection-icip.png | PNG | 1469 × 1469 | 323.9 KiB | about.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/Phishing Expert.png | PNG | 199 × 244 | 23.1 KiB | projects.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/SIEM.png | PNG | 229 × 229 | 20.5 KiB | projects.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/SOC Member.png | PNG | 195 × 230 | 13.6 KiB | projects.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/Web Attack Investigated.png | PNG | 209 × 230 | 19.3 KiB | projects.html | Reusable supporting badge; verify relevance/provenance. |
| Badges/Web Attack Investigator.png | PNG | 214 × 233 | 23.0 KiB | projects.html | Reusable supporting badge; verify relevance/provenance. |
| Certificates/Accelerate Your Job Search with AI.jpg | JPG | 3300 × 2550 | 2072.9 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/AI Security Fundamentals!_Cert.jpg | JPG | 1120 × 1120 | 159.9 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/aig.jpg | JPG | 3509 × 2480 | 656.1 KiB | projects.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Assets, Threats, and Vulnerabilities.jpg | JPG | 3300 × 2550 | 2075.9 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/AutomateTasks.jpg | JPG | 3300 × 2550 | 2080.6 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Certified Artificial Intelligence Security & Risk (CAISR).jpg | JPG | 3300 × 2550 | 890.0 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Comonwealth.jpg | JPG | 3509 × 2480 | 654.3 KiB | projects.html | Preserve original; optimize preview; verify credential details. |
| Certificates/ConnectNetwork.jpg | JPG | 3300 × 2550 | 2094.7 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/CPPS.jpg | JPG | 6239 × 4412 | 2562.0 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/CS401_OS.jpg | JPG | 3296 × 2552 | 1088.8 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/cyber_track.jpg | JPG | 3508 × 2481 | 752.6 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/cybercommomwealth.jpg | JPG | 3509 × 2480 | 640.7 KiB | projects.html | Preserve original; optimize preview; verify credential details. |
| Certificates/cyberkill.jpg | JPG | 3508 × 2481 | 1045.3 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/cyberthreat.jpg | JPG | 3300 × 2550 | 1764.9 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Datacom Cybersecurity Job Simulation on Forage.jpg | JPG | 3509 × 2480 | 650.3 KiB | projects.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Delloite.jpg | JPG | 3509 × 2480 | 480.4 KiB | projects.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Endpoint.jpg | JPG | 3300 × 2550 | 1519.5 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Forage.jpg | JPG | 3509 × 2480 | 672.5 KiB | projects.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Foundation_Cybersecurity.jpg | JPG | 3300 × 2550 | 2073.0 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/FullStack.jpg | JPG | 6667 × 4959 | 1655.8 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/GitHub.jpg | JPG | 1600 × 1190 | 222.5 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/GoogleCybersecurity.jpg | JPG | 3300 × 2550 | 2648.7 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/hardware.jpg | JPG | 3300 × 2550 | 1207.5 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Intro_cryptography.jpg | JPG | 3150 × 2434 | 847.4 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Intro_Linux.jpg | JPG | 5154 × 3992 | 2081.0 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Introduction to Software Testing.jpg | JPG | 3300 × 2550 | 2129.1 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/introduction_to_cip.png | PNG | 900 × 710 | 368.7 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/ISOIEC 277012025 Lead Auditor.jpg | JPG | 3508 × 2479 | 1221.9 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/IT_Security.jpg | JPG | 3300 × 2550 | 2049.4 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/java_fundamental.jpg | JPG | 842 × 600 | 180.8 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/JuniorCybersecurityAnalyst.jpg | JPG | 3300 × 2550 | 1555.9 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Linex&SQL.jpg | JPG | 3300 × 2550 | 2072.3 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Managerisk.jpg | JPG | 3300 × 2550 | 2073.3 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Mental_Health.jpg | JPG | 3508 × 2481 | 1154.7 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Network_Defence.jpg | JPG | 3300 × 2550 | 1631.5 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/networkbasics.jpg | JPG | 3875 × 2625 | 1364.2 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/networkconfig.jpg | JPG | 3875 × 2625 | 1442.2 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/operationalizing-mitre-attck-for-socs.jpg | JPG | 3509 × 2480 | 1317.6 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/oracle.jpg | JPG | 3300 × 2550 | 2162.5 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/practical-help-desk.jpg | JPG | 3200 × 2360 | 1635.9 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Put It to Work.jpg | JPG | 3300 × 2550 | 2082.2 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Python GFG.jpg | JPG | 4961 × 3508 | 1738.8 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/soc.jpg | JPG | 3300 × 2550 | 913.3 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/socanalyst.jpg | JPG | 3300 × 2550 | 1997.5 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/SoundsAlarm.jpg | JPG | 3300 × 2550 | 2056.2 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Splunk.jpg | JPG | 3512 × 2483 | 1274.6 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/System Admin.jpg | JPG | 1650 × 1275 | 845.3 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Tata.jpg | JPG | 3509 × 2480 | 661.2 KiB | projects.html | Preserve original; optimize preview; verify credential details. |
| Certificates/Tecgnical_support.jpg | JPG | 3300 × 2550 | 2033.6 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Certificates/UIUX_Design.jpg | JPG | 6667 × 4959 | 1619.1 KiB | certifications.html | Preserve original; optimize preview; verify credential details. |
| Images/avatar.jpg | JPG | 1329 × 1183 | 2001.4 KiB | about.html, certifications.html, contact.html, experience.html, index.html, projects.html, recommendations.html, skills.html | Preserve identity; optimize portrait/favicon/social derivatives. |
| Images/business-person-futuristic-business-environment.jpg | JPG | 4900 × 3721 | 1010.9 KiB | index.html | Optional large illustration; confirm rights/relevance. |
| Images/discord-icon.png | PNG | 465 × 467 | 94.6 KiB | Unreferenced | Unused platform/social icon; optional after rights/brand review. |
| Images/github-icon.png | PNG | 512 × 512 | 26.8 KiB | Unreferenced | Unused platform/social icon; optional after rights/brand review. |
| Images/gmail-icon.png | PNG | 512 × 512 | 7.1 KiB | Unreferenced | Unused platform/social icon; optional after rights/brand review. |
| Images/letsdefend-icon.png | PNG | 400 × 400 | 39.5 KiB | Unreferenced | Unused platform/social icon; optional after rights/brand review. |
| Images/linkedin-icon.png | PNG | 512 × 512 | 19.7 KiB | Unreferenced | Unused platform/social icon; optional after rights/brand review. |
| Images/picoctf-icon.png | PNG | 335 × 312 | 17.5 KiB | Unreferenced | Unused platform/social icon; optional after rights/brand review. |
| Images/tryhackme-icon.png | PNG | 180 × 180 | 8.8 KiB | Unreferenced | Unused platform/social icon; optional after rights/brand review. |
| Images/whatsapp-icon.png | PNG | 512 × 512 | 30.4 KiB | Unreferenced | Unused platform/social icon; optional after rights/brand review. |
| Resume/AR-Mohamed-Rimsan-Resume.pdf | PDF | Not measured (PDF) | 229.3 KiB | contact.html, index.html | Preserve download URL; review content/layout separately. |

### Missing assets and reference checks

Static checks found **zero missing local HTML href/src/action targets**, duplicate IDs, unresolved same-page fragments or missing popup IDs. These checks do not establish remote-link operation, all live asset availability or rendered image behavior. An exact component-by-component filename-case check against directory entries also found zero mismatches. All inspected relative HTML targets match current local casing; external URLs and Git-history filenames were not exhaustively audited.

Missing evidence includes project-specific repositories, screenshots, technical case studies, support lab diagrams and substantiated support metrics. These are content gaps, not necessarily broken references. No dedicated lightweight favicon/social banner is provided. Local social PNG icons are unused; current UI uses Font Awesome. Brand/license provenance for the generic illustration, legacy backgrounds and icons is undocumented; repository presence does not establish reuse rights.

## 8. CSS and Design Architecture

The site has a recognizable shared visual language, but not a formally separated or fully consistent design system. A monolithic shared sheet accumulates components, page rules and repeated responsive/theme blocks. Reusable concepts exist; a complete redesign should consolidate them rather than discard all useful primitives.

### Default tokens

| Token | Default value |
| --- | --- |
| --bg | #07111f |
| --bg-soft | #0b1728 |
| --surface | rgba(13, 27, 45, 0.9) |
| --surface-strong | rgba(17, 34, 56, 0.96) |
| --surface-soft | rgba(255, 255, 255, 0.04) |
| --line | rgba(148, 163, 184, 0.18) |
| --line-strong | rgba(125, 211, 252, 0.28) |
| --text | #d8e1ee |
| --text-muted | #96a6bd |
| --heading | #f8fbff |
| --primary | #38bdf8 |
| --primary-strong | #0ea5e9 |
| --accent | #22d3ee |
| --shadow | 0 20px 60px rgba(2, 8, 23, 0.28) |
| --radius-lg | 16px |
| --radius-md | 10px |
| --radius-sm | 8px |
| --container | 1120px |

Light-mode overrides: bg #f5f8fc; bg-soft #edf4fb; surface rgba(255,255,255,.94); surface-strong #fff; surface-soft rgba(14,165,233,.06); line rgba(15,23,42,.12); line-strong rgba(14,165,233,.26); text #243349; text-muted #60708a; heading #0f172a; lighter shadow. Primary/accent remain cyan/sky blue. Purple rgba(124,58,237,...) is hardcoded repeatedly instead of tokenized. `--primary-light` is referenced for recommendation-name hover/focus but never defined; that declaration is invalid.

### Typography, spacing and widths

- Body: Inter/system-ui/Apple/BlinkMacSystemFont/Segoe UI/sans-serif; 16px, line-height 1.65; 15.5px at ≤640px. Headings/brand/metrics: Space Grotesk/sans-serif, weight 700. Neither named font is loaded by the site.
- Fluid h1/h2 sizes use clamp. Home hero h1 reaches 4.1rem; mobile h1 clamp is 1.9–2.55rem. h2 clamp is 1.35–1.9rem. Labels/tags/nav may be .72–.86rem; assess readability in actual rendering.
- Header/main/footer max width 1120px, normally viewport minus 2rem; ≤640px viewport minus 1rem. Main gap 2.8rem, then 2.2rem at ≤860px and 2rem at ≤640px.
- Spacing repeats values such as .35/.45/.5/.65/.75/.85/.9/1/1.15/1.35rem plus clamp-based hero padding. There are no spacing tokens or documented spacing scale.
- Radius tokens: 8/10/16px. Borders use translucent tokens; dark cards use navy translucent surfaces. Main backgrounds are CSS gradients; no legacy background JPG use.

### Layout/components/icons/motion

Grid primitives include grid-2, grid-3, grid-4, mini-grid and spotlight. Flex wraps nav/action/tag/filter rows. Card families share surface/border/radius/padding; later project/skill/cert/contact patterns repeat nearly identical vertical flex layouts and top accent lines. Role responsibility lists use CSS columns above 860px. Numerous min-width:0 and minmax(0,1fr) declarations support narrow layouts.

Filled buttons use cyan gradients and dark text; outlines use token surfaces/borders. Main buttons have minimum 44px height; specialized project/cert/contact actions 40px. Header is relative, not sticky. Footer wraps and becomes a grid on mobile. Hero/portrait layout uses object-fit and responsive grids. Icons are Font Awesome glyphs; decorative icons generally have aria-hidden and nearby text. No custom SVG/icon sprite system.

Motion comprises smooth scrolling and hover/focus transitions/transforms; no CSS keyframes. JavaScript has a dormant typewriter feature because no current page contains #typed-text. No prefers-reduced-motion overrides exist.

### Theme/shared/inline architecture and reuse

Light/dark mode follows prefers-color-scheme only; no toggle, saved theme or browser storage. Page-specific theme rules repeat surface adjustments. There are **zero inline style attributes** and no inline executable event-handler attributes in the HTML. Inline JSON-LD is data, not executable UI code. JS temporarily styles a fallback clipboard textarea.

Reuse: token concept, fluid containers/type, wrapping grids, consistent button/card concepts, skip/focus styles and semantic document layout. Refactor: contrast-safe primary tokens, missing font strategy, repeated card/action/gradient rules, repeated breakpoint/theme blocks, inconsistent older classes such as cards-grid1/cards-gridBadge, undefined variable and dormant typewriter. Remove selectors only after checking all pages in implementation. Body overflow-x:hidden may conceal overflow; .single-line-role-title uses nowrap and needs rendered phone testing.

## 9. JavaScript and Interactive Features

main.js wraps behavior in one DOMContentLoaded initializer, using optional-control guards and data attributes. `node --check main.js` passed. This validates syntax, not interactive behavior. No browser event flows were exercised.

| Feature | Actual implementation | Problems / limits |
| --- | --- | --- |
| Page navigation | Normal document links. Current basename or index.html determines visual active class; links close menu. | No aria-current; no client router/history abstraction required. |
| Mobile nav | Hamburger toggles nav.show and aria-expanded; Escape and nav link click close. Menu activates at ≤1100px. | No aria-controls, outside-click close or no-JS fallback. CSS hides mobile nav if script fails. |
| Theme | CSS system preference. | No toggle or persistence. |
| Typewriter | Optional typed-text node, six QA/security phrases, setTimeout/textContent loop. | Target absent in all current pages; dormant. No reduced-motion handling if reactivated. |
| Project filter | data-filter sets activeFilter; space-delimited data-project-category matches; items/empty sections hidden. | No project text search, pressed-state semantics, live result count, no-results message or URL persistence. |
| Certificate filter/search | Lowercased trimmed query matches custom searchable metadata plus text; combines with category; hides empty sections. | No accessible result feedback. Small catalogue does not obviously require debounce. |
| Project disclosures | Native details/summary shows capability/contribution lists. | No custom JS needed; expanded affordance/focus needs actual browser review. |
| Image previews | Nested .popup nodes moved to body; data-popup opens target .active and body.modal-open; backdrop/close click or Escape closes. | Target IDs exist. Missing dialog semantics/focus handling and native close button. Hidden lazy-image fetch timing unmeasured. |
| Discord copy | Clipboard API, or temporary readonly textarea/execCommand(copy); success/error HTML for 1.8 seconds. | Legacy fallback ignores execCommand false return, possibly claiming success; no dedicated live announcement; rapid-click timers untested. |
| Contact form | Prevent default, disable submit, show sending; fetch POST FormData with Accept JSON; response.ok resets/success; catch error; finally reenable. | No request sent. No timeout, detailed server error parsing or visible anti-spam controls; provider config unknown. Error email differs from primary mailto. |
| Resume | Native href with download attribute and filename. | Path exists; HTTP HEAD 200; browser download/PDF contents not tested. |
| Scroll/motion | CSS smooth scroll and transforms. | No scroll observers/parallax/back-to-top implementation or reduced-motion branch. |
| Browser storage | In-memory menu/filter/UI state only. | No local/session storage, IndexedDB, first-party cookie implementation or service worker in source. Third-party provider behavior not inspected. |

Error handling guards optional elements and missing popup targets. Clipboard/network work uses try/catch. Form falls back to native form.submit only if its status node is absent; without JS, native action/method remain present. Without JS, copy/filter/previews/menu enhancements do not work.

Unsafe-insertion review: textContent handles typewriter and status text. innerHTML is used for fixed clipboard messages, restoring original button markup and a fixed fallback-email link. No direct user-input/fetched-content-to-innerHTML data flow was found. Preserve this boundary; do not insert external HTML there during redesign.

## 10. Responsive Design Findings

### Actual test scope

Source/media-query review, image-dimension measurements and static markup/path checks were performed. Browser startup was attempted and failed before a page opened. **375px, 768px and 1440px were not rendered or interaction-tested. No screenshots were captured/saved.** No viewport-specific overflow measurement is claimed.

| Width | Expected from CSS, not visually confirmed | Pending checks |
| --- | --- | --- |
| 1440px | 1120px content cap; full eight-link nav; multi-column grids, split hero and two-column responsibility lists. | Font-dependent nav fit, content density, long cards and keyboard path. |
| 768px | Menu button/nav collapse at ≤1100px; grids generally two columns. ≤860px heroes/grid-2/spotlight/form/search rows and role lists stack. | Menu discovery, badge auto-fit, filter wrap, long-page usability. |
| 375px | ≤640px viewport-minus-1rem containers, 1rem hero padding, most grids one column, full-width CTAs/selected filters, stacked footer. | Nonwrapping trainee title, long strings, small uppercase labels, certificate readability, modal close access, portrait crop and select rendering. |

Strengths: wrapped rows, fluid type, zero-min grid tracks, image max-width and phone button sizing. Risks: body overflow suppression, nonwrapping role title, long project/credential scroll depth and 40px specialized actions. No actual tablet/mobile defect dimensions or screenshots can be reported without successful rendering.

## 11. Accessibility Findings

### Confirmed strengths

Eight full pages use English language declarations, one h1, skip link and main landmark; primary controls are native links/buttons. All **79 img occurrences** have alt attributes: About 17, Certifications 44, Home 2, Projects 16. Presence is checked, not full descriptive quality. No duplicate IDs or unresolved same-document fragments/popups. Forms and search have associated labels; contact uses required fields/type=email and role=status/aria-live=polite. CSS includes visible focus outlines for buttons/links/inputs/textareas/selects. Native details/summary provides keyboard-capable disclosures. Icons generally use aria-hidden with text labels.

### Confirmed deficiencies / source-based risks

- Image overlays lack role/name/aria-modal, focus entry/trap/return and inert background management. Close is a clickable span, not a keyboard-focusable named button. Escape alone is insufficient.
- Filters change only visual active class; no aria-pressed, result announcement/count or empty-result feedback.
- Nav active state lacks aria-current; hamburger lacks aria-controls; nav landmark has no descriptive label. Menu button itself has a label and JS aria-expanded.
- At ≤1100px failed/disabled JS leaves navigation hidden. Progressive enhancement needs attention.
- Discord feedback has no dedicated live region; Connect on Discord actually copies username and can surprise users.
- Smooth scrolling/transforms and dormant typing lack reduced-motion support.
- No actual keyboard/screen-reader, zoom/reflow, OS high-contrast or motion-preference test was performed. No WCAG conformance certification is implied.

### Actual contrast calculations

WCAG relative-luminance math on opaque token pairs, not sampled/composited rendered gradients:

| Foreground / background | Ratio | Implication |
| --- | --- | --- |
| #38bdf8 / #ffffff | 2.14:1 | Below 3:1 even for large text; light-mode primary links/labels/icons require darker contrast-safe tokens. |
| #60708a / #ffffff | 5.02:1 | Passes 4.5:1 ordinary text on solid white. |
| #96a6bd / #07111f | 7.65:1 | Strong dark-mode muted text pair. |
| #0f172a / #ffffff | 17.85:1 | Strong heading pair. |
| #031322 / #38bdf8 | 8.75:1 | Strong filled-button text pair on solid primary. |

## 12. SEO and Performance Findings

### Metadata/crawling

All eight main pages have distinct titles/descriptions, author/robots/theme-color, canonical links, portrait favicon, CDN preconnect, Open Graph website/site/title/description/URL/image fields and Twitter summary cards. OG portrait dimensions 1329×1183 match the image. lang=en and og:locale=en_US are present; intended audience/locale should be confirmed rather than treated as location evidence.

Homepage JSON-LD defines WebSite/Person/WebPage with linked IDs. About defines ProfilePage/Person. Other six main pages have no JSON-LD. Existing jobTitle/descriptions/knowsAbout, page titles, social cards and page copy remain QA/security oriented. Changing only h1 text would leave stale metadata.

robots.txt allows all and references sitemap.xml. Sitemap lists eight canonical content routes, excluding redirect and verification resource intentionally; all lastmod values are 2026-09-16 despite an October 8 commit/deployment. Keep dates truthful. index.html canonical points to /. Legacy route is noindex/follow and canonicalizes to Projects. No custom 404 page or web app manifest found.

All ten HTML endpoints plus robots/sitemap/resume returned HTTP 200 to HEAD requests. Homepage GET returned 19,230 bytes and decoded text matching local index.html. Other live document bodies were not compared. HEAD availability does not validate link destinations, semantics, redirects or form delivery.

### Performance

Static HTML, a deferred 7 KiB script and no hydration/data API on navigation are good foundations. Shared CSS is approximately 49.7 KiB uncompressed, with all pages' rules in one file; no build/minification pipeline. Measure before deciding CSS splitting is valuable.

Portrait: 2,049,383 bytes, 1329×1183; homepage supplies eager loading, async decoding, high fetch priority and intrinsic dimensions. It is large for display/favicons. Illustration: 1,035,192 bytes, 4900×3721; lazy/async and dimensioned but visually constrained. No srcset/sizes or WebP/AVIF versions found.

Certificate scans commonly exceed 2 MiB and 3300×2550; some reach 6667×4959, CPPS 6239×4412. Preserve originals and generate smaller derivatives later; full scans should be fetched when needed. Certificate/badge img tags use lazy/async but generally lack intrinsic width/height. CSS fixed badge heights reduce some risk; actual CLS and hidden-overlay image fetch timing are unmeasured.

Inter/Space Grotesk are not loaded, causing device-dependent fallback typography. CDN Font Awesome brings an external CSS/font dependency with no integrity attribute; assess smaller/local icon strategy later. GitHub promotion is static. Live homepage advertised Cache-Control max-age=600; no compressed transfer benchmarking or waterfall was recorded.

**No Lighthouse/PageSpeed/accessibility scanner scores, load timing, LCP/CLS/INP or lab-device metrics were run.** Browser connection failed; no dependency installation was used to obtain substitute numbers.

## 13. Security Considerations

The repository has no first-party server, authentication/database backend or privileged API client. Formspree is the only message processor. Static architecture reduces application complexity but does not prove complete security.

A limited working-tree text scan found zero .env files, PEM-style private key marker matches or AWS access-key-ID pattern matches in examined HTML/JS/Python/Markdown/JSON/text. No values were disclosed. This is not an exhaustive secret/entropy scanner, Git-history audit, PDF metadata check or image/OCR privacy audit. Do not treat absence of these patterns as proof that no secrets exist.

Workplace content is generalized public portfolio material; no internal reports, customer records, system credentials or confidential implementation documents were reproduced. Certificate serials/QR payloads/signatures were not extracted. Public emails/profiles are included; public WhatsApp digits are intentionally omitted from the shareable report.

Formspree receives name/email/subject/message cross-origin. Its public routing ID is not a secret API key. No explicit honeypot/CAPTCHA/application rate limit is visible; provider controls, ownership, quotas, retention and delivery are unknown. Native validation is not server-side validation. No form message was submitted. External target=_blank links inspected all have noopener noreferrer. No direct untrusted-input-to-innerHTML path was found; fixed markup sinks must remain controlled during refactoring.

The live homepage HTTPS response included HSTS max-age=31556952, Content-Type text/html; charset=utf-8, wildcard Access-Control-Allow-Origin and GitHub cache/server headers. It did not include CSP, X-Content-Type-Options, X-Frame-Options, Referrer-Policy or Permissions-Policy. This applies only to the examined homepage response; GitHub API security headers must not be attributed to the site.

No custom header configuration is present. Confirm actual hosting controls before recommending unsupported header files; any CSP must account for CDN resources, Formspree and structured data. No attack testing was performed. Confirm contact/testimonial consent and asset rights before later republishing. Support evidence should be anonymized and authorized; never publish tickets, internal screenshots, access details or real customer data merely to strengthen the narrative.

## 14. GitHub Pages Deployment Architecture

| Item | Confirmed evidence / uncertainty |
| --- | --- |
| Local branch | qa-security-engineer-version; initial git status clean. Local main also exists. |
| Remote | origin is the public repository URL; remote HEAD points to origin/main. |
| Deployment branch | Last three returned github-pages deployments use main: October 8, September 26 and September 16, 2026. Source: https://api.github.com/repos/mohamedrimsan/mohamedrimsan.github.io/deployments?per_page=3 |
| Managed workflow | Latest examined pages build and deployment run: main, dynamic/pages/pages-build-deployment, completed/success, created 2026-10-08T13:20:02Z. https://github.com/mohamedrimsan/mohamedrimsan.github.io/actions/runs/37783520657 |
| Exact Pages settings | Unauthenticated GET /repos/mohamedrimsan/mohamedrimsan.github.io/pages returned 404. This does not indicate Pages is absent: live site/deployment evidence proves it exists. |
| Publishing folder | Root strongly suggested by root files/matching live homepage; settings not independently confirmed. No docs directory. |
| Custom domain | No CNAME/config found; live homepage stayed at github.io. Exact account setting unknown. |
| Workflows/config | No .github/workflows, _config.yml, Gemfile or .nojekyll found. Absence of workflow YAML does not mean Actions is unused: managed Pages runs exist. |
| Build requirement | Checked-in files need no frontend compilation. Managed Pages processing details not inspected. Python resume generator is optional and unrelated to deploy. |
| URL style | Relative nav/CSS/JS/images/resume URLs; absolute production canonical/OG/schema/sitemap; absolute legacy meta redirect. |
| Runtime dependencies | CDN Font Awesome; Formspree for messages; browser APIs; outbound profiles/demos are external services. |

### URL-safe redesign

Retain /, /index.html, /about.html, /experience.html, /projects.html, /skills.html, /certifications.html, /recommendations.html and /contact.html. Keep /hands-on-experience.html compatibility, Google verification resource, robots/sitemap and public resume path. Avoid SPA-only routing that needs server fallback. If content moves, retain compatible historical documents/redirects and decide canonicals explicitly.

Preserve exact filename case and appropriately encode spaces/special characters. Absolute production redirects jump out of local/preview hosts; navigation should remain preview-safe while production canonicals stay correct. Confirm main/root settings before release; do not assume this working branch auto-publishes. No push/merge/deploy is part of this phase.

## 15. Identified Problems and Technical Debt

| Priority | Finding | Evidence / later action |
| --- | --- | --- |
| High | Career-direction mismatch | Visible copy, header/footer, metadata/schema, form subjects, README and resume source emphasize QA/security. Establish one approved support-first content matrix and update all surfaces together. |
| High | Conflicting professional facts | Website trainee versus generator full-time engineer title; administrative dates differ. Confirm authoritative records before editing. |
| High | Certificate dialog accessibility | Click-only span close, missing semantics/focus handling. Rebuild with a proper named dialog/close button and keyboard/focus verification. |
| High | Light-mode primary contrast | Cyan on white calculated at 2.14:1. Choose darker light-theme primary tokens and measure actual states/surfaces. |
| High | Contact delivery/preferences unknown | No submission test; provider configuration uninspected; fallback email inconsistent. Confirm preferred address and endpoint ownership before testing. |
| Medium | Heavy image assets | 2 MiB portrait; many large scans; no responsive derivatives. Preserve originals and optimize display/full-preview loading. |
| Medium | Duplicate HTML/content ownership | Eight headers/nav/footers/SEO blocks and a separate resume content source. Define shared conventions or a minimal static template process if needed. |
| Medium | Weak project evidence | Most projects lack repositories, demos, screenshots or documentation. Gather authorized evidence and clearly distinguish public/private/unavailable links. |
| Medium | JS-dependent mobile navigation | Mobile nav hidden without .show. Add progressive enhancement and failure-mode tests. |
| Medium | Filter accessibility | Visual selection only, no result feedback. Add selected-state semantics and live/empty result messaging. |
| Medium | Credential duplication/verification | AI job-search course appears twice; credential page has no external verification links. Use single records with multiple categories and owner-confirmed issuer URLs. |
| Medium | Font declarations incomplete | Named fonts are not loaded. Use intentional system fonts or measured self-hosting. |
| Medium | CSS accumulation | 2,760-line sheet repeats page card/action/gradient/breakpoint/theme patterns. Consolidate tokens/components with a predictable cascade. |
| Medium | No rendered baseline | Browser unavailable; no viewport, keyboard or automated accessibility/performance results. Make these acceptance checks for implementation. |
| Low | Dormant feature | Typewriter code has no target; keep only if intentionally needed with motion support. |
| Low | Undefined variable | Recommendation hover/focus references --primary-light. Resolve to an existing contrast-safe token. |
| Low | Metadata/date maintenance | Sitemap dates predate October deployment; copyright includes next year. Maintain truthful owner-approved dates. |
| Low | Tracked editor config | .vscode/settings.json remains tracked despite ignore rule. Decide convention later; no cleanup performed. |

These priorities are qualitative engineering judgments, not measured user-impact scores. No missing local links were discovered; do not invent broken assets to justify refactoring.

## 16. Existing Features That Must Be Preserved

- Existing URLs, legacy hands-on compatibility, Google verification resource, robots/sitemap and public resume path.
- Accurate employment/education history and official titles after confirmation; preserve QA/cybersecurity background as supporting technical experience.
- Current Help Desk evidence: remote troubleshooting, clear user guidance, incident/request records, escalation, status updates, follow-through and cross-team coordination.
- Resume access and simple recruiter contact routes; owner-approved public email/social methods and safe outbound-link attributes.
- Certificate/badge originals, recorded issuers/dates/expiry and linked LetsDefend achievements without overstating independent verification.
- Exact attributed recommendation text and professional title/employer context; especially existing feedback on communication, reliability and customer-facing work.
- Semantic document navigation, skip links, main landmarks, one h1, labels, focus visibility and live contact status.
- Project category/disclosure patterns and combined certificate text/category search where useful; retain preview capability after repairing accessibility.
- Static delivery simplicity, small JavaScript footprint and CSS system-theme adaptation if retained in the new visual direction.

Do not invent a help desk ticketing product, SLA achievement, Microsoft 365/Intune/Entra administration scope, ITIL qualification, remote-support product, customer satisfaction score or ticket volume. Current source establishes support responsibilities, not those additional specifics. Distinguish course foundations/awareness from production administration.

## 17. Recommended Redesign Architecture

### Options comparison

| Option | Maintainability | Performance | Deployment complexity | Content/URL impact | Recommendation |
| --- | --- | --- | --- | --- | --- |
| A. Keep architecture/refactor in place | Lowest initial effort; repeated markup and parallel facts can remain troublesome. | Static benefits; optimizing images likely yields more than adding tooling. | Low; existing checked-in Pages output. | Low route risk, but larger refresh may leave inconsistencies. | Appropriate for a narrow refresh, less suitable for this complete redesign. |
| B. Restructure HTML/CSS/JS | Clear content ownership, reusable conventions/components/tokens and small behavior modules. | Static HTML and minimal JS; no hydration needed. | Low without build; modest if minimal templates are justified. | Existing .html paths/assets can remain intact. | **Preferred.** |
| C. Modern framework migration | Useful only if future app/CMS/data requirements justify ecosystem complexity. | Static export can be efficient, but framework runtime is unnecessary for current interactions. | Higher: dependency maintenance, build/static export, Pages routing/404/path checks. | More route/content conversion and compatibility risks. | Not justified by current needs alone. |

### Proposed implementation principles — not changes made now

Keep static multipage delivery. Organize tokens, base typography, layouts, shared components, page styles and preference overrides in a predictable cascade. Split behavior files only when clarity benefits; a 7 KiB script does not itself require a bundler. Make navigation/content/contact useful when JavaScript fails, then progressively enhance search, previews and copy feedback.

Maintain one approved factual record of identity, employment, education, projects, credentials, social URLs and proficiency levels, with source provenance and unresolved fields. A lightweight build-time template system may later reduce duplicated HTML if the maintenance benefit outweighs new tooling; it must emit compatible .html files and fit verified Pages settings. No generator or dependency was introduced in this audit.

Lead with support outcomes already substantiated: diagnosing issues, giving clear instructions, keeping accurate records, escalating appropriately, coordinating resolution and maintaining service continuity. QA experience supports reproduction/validation; security experience supports safe troubleshooting and risk awareness. Windows/Linux/networking/scripting are relevant, but training or awareness must not be inflated into unverified administration expertise.

Prioritize a support-oriented homepage; accurate experience; concise systems/application/support skills; selected technical work with authorized evidence; relevant help desk/systems/networking credentials with secondary QA/security credentials discoverable; authentic recommendations; clear contact/resume access. Do not rewrite quotes to fit marketing or alter historical titles by inference.

Preserve original assets and public download paths, create display derivatives, supply intrinsic sizes/responsive sources where useful, and load full scans on demand. Prioritize navigation resilience, accessible dialogs, contrast-safe light mode, clear filter results and reduced motion. Synchronize visible copy with titles/descriptions/social cards/structured data/sitemap.

## 18. Open Questions and Missing Information

### Owner/content confirmations needed before implementation copy is approved

1. Which primary target title should lead: Technical Support Engineer, IT Support Specialist, Service Desk Analyst, Application Support Engineer, or broader positioning? The direction is clear; headline/title is not finalized.
2. Which official July–September 2026 title is correct: QA & Security Engineer Trainee or QA & Security Engineer? Is trainee an employment category or a title suffix?
3. Which Administrative Assistant dates are authoritative: June–December 2021 or May–November 2021? Confirm official employer styling too.
4. Is the Help Desk role still current at publication? Confirm part-time/remote arrangements and employer attribution.
5. What actual support platforms, OS tasks, remote tools, channels, identity systems and troubleshooting scope can be claimed from work rather than courses? No missing tool name should be guessed.
6. Are support outcomes/metrics, knowledge articles, authorized anonymized tickets or labs available? None are substantiated in current page content.
7. Are CGPA 3.46, degree expected November 2027 and specialization August 2027 still current/approved? Confirm study status.
8. Which email is preferred, and should WhatsApp stay public? Resolve Gmail versus Outlook fallback.
9. Is the PDF or generator authoritative? The binary PDF was not content-compared or visually reviewed.
10. Which projects have public/private repositories, functioning demos, screenshots and docs? Are VeriGuard/MailForge still in progress?
11. Are issuer verification links available and may they be published? Confirm credential naming/dates/expiry; scan/issuer authenticity was not assessed.
12. Are testimonial permissions and image usage rights documented? Can recommendations be linked to original public endorsements?
13. Is main/root still the Pages publishing source? Public deployments show main; exact settings API was unavailable.
14. Who owns the Formspree endpoint and its delivery/spam/retention/quota settings? No message was sent.

### Tests performed and failures/limitations

- Local file inventory; all HTML content/metadata/controls; CSS and JS source review; resume-generation source review; raster dimensions and sizes; local path existence, exact case, duplicate IDs, same-page fragments and popup targets; limited non-disclosing secret-pattern scan.
- All inspected relative path components match exact directory-entry casing; zero case mismatches found. This does not establish external URL casing or a full history audit.
- Homepage live GET/header/body comparison; live HEAD checks for all ten HTML endpoints, robots/sitemap/resume; public deployment and managed workflow API reads.
- JavaScript syntax check passed with node --check main.js; both JSON-LD blocks parsed as JSON; sitemap parsed as XML. These are structural checks, not browser functionality validation.
- Token contrast calculations were performed; no rendered gradient/compositing or automated WCAG scan.
- Initial ordinary shell startup failed with `Failed to create unified exec process ... setup refresh had errors`. Subsequent read-only shell commands succeeded with elevated sandbox access. The environment failure did not indicate a repository defect.
- Browser runtime startup was attempted twice and failed with the same sandbox setup error. Browser skill instructions were read. No pages opened, viewport renders/screenshots, interaction tests or Lighthouse measurements resulted.
- Initial Python text extraction encountered a Windows cp1252 UnicodeEncodeError on Ĝ; rerunning with explicit UTF-8 succeeded. Employer text in the source is not thereby defective. Resume source was separately checked with UTF-8.
- Web-reader access to the live homepage failed; direct read-only HTTP subsequently succeeded with 200. This was a tool-specific access failure, not an observed site outage.
- Unauthenticated Pages settings API returned 404; separate public deployment/workflow calls succeeded. Exact publishing-folder/account settings remain unknown.
- An oversized report-generation shell command was rejected by Windows with filename/extension-too-long before execution. Report creation succeeded in smaller commands. No extra script files were created.
- Some large combined inspection outputs were truncated; focused reads and structured extraction supplied the inventories. Truncation is not treated as evidence of an absent feature.
- No form submission, comprehensive external link crawl, provider delivery check, account-permission inspection, exhaustive secret/history scan, PDF/scan OCR, certificate authentication, screenshot or visual review occurred. No automated numerical scores are invented.

## 19. Suggested Implementation Sequence

1. Resolve authoritative title/date/contact/resume facts; agree the primary support title and create a factual content matrix with explicit unknowns.
2. Confirm Pages settings and historical route baseline. Keep a redesign branch and preserve verification/legacy/resume resources.
3. Map every existing page/section/credential/quote/project to a destination. Elevate support and retain QA/security background without inventing claims.
4. Define contrast-safe light/dark tokens, intentional font strategy, spacing/type/layout components, focus and motion rules.
5. Establish shared HTML conventions or a justified minimal template process emitting the same .html URLs; consolidate approved content/metadata ownership.
6. Implement homepage/about/experience, then skills and evidence-backed projects. Keep official titles intact.
7. Rebuild credential/recommendation presentation with deduplicated records, authorized links and accessible dialog/filter behavior.
8. Produce optimized image/favicon/social derivatives while preserving originals and resume compatibility. Review PDF contents/layout in a separate authorized document task.
9. Validate contact controls and mocked success/failure first; perform an explicitly authorized delivery test later, with preferred email/provider ownership confirmed.
10. Run actual 375/768/1440 browser tests in both themes, keyboard/focus/Escape checks, reduced motion, zoom/reflow, case/link verification and automated accessibility/performance tools. Capture screenshots when tools work and additional artifacts are authorized.
11. Update titles/descriptions/schema/social cards/sitemap/README together; review confidentiality, attribution, licensing and evidence/proficiency accuracy.
12. Prepare a reviewable final diff and validation record. Merge/push/deploy only in a later authorized phase.

### Final handoff snapshot

| Requested item | Result |
| --- | --- |
| Total pages | 10 HTML files: 8 full content pages, 1 visitor redirect, 1 verification endpoint. 9 visitor routes including redirect; 8 substantive pages. |
| Important HTML | index.html, about.html, experience.html, hands-on-experience.html, projects.html, skills.html, certifications.html, recommendations.html, contact.html; preserve googlec5a2878c58ee90d7.html. |
| Important CSS | style.css only: 2,760 lines, 50,924 bytes. |
| Important JavaScript | main.js only: 7,134 bytes; syntax check passed. |
| Relevant assets | 89 raster images + 1 PDF = 90 binary assets, approximately 75.7 MiB. Additional Python resume-generation utility. |
| Hosting | Static GitHub Pages; successful managed deployment from main; root folder inferred, exact settings unconfirmed. |
| Existing interactive code | Menu/active nav, project categories, combined certificate search/filter, image preview/Escape/scroll lock, native contribution disclosures, Discord copy, async form status and native resume link. Implemented; browser behavior not tested. |
| HTTP-confirmed resources | Homepage GET 200/source match; all ten HTML endpoints plus robots/sitemap/resume HEAD 200. |
| Broken/incomplete/outdated | Dialog accessibility, light primary contrast, stale career positioning, conflicting professional facts, duplicate credential display, undefined CSS token, missing project evidence, dormant typewriter, error-email mismatch, stale sitemap dates and unverified form delivery. No missing local targets or case mismatches found. |
| Migration | B: restructure static HTML/CSS/JS; no framework migration needed for existing features. |
| Main risks | Losing URLs/verification/download compatibility, publishing wrong branch, altering facts/quotes, inflating support experience, exposing employer/customer data, worsening accessibility/image weight or breaking contact delivery. |
