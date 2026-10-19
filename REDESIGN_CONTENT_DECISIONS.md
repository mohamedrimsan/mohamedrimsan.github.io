# Content decisions — 19 October 2026

This review uses the checked-out source at `63a5cb3`, the owner-supplied implementation prompt, `portfolio_redesign_handoff/REDESIGN_BLUEPRINT.md` and the audit (including chapter 18). “Source-confirmed” means present in the repository; it does not independently verify employment or credentials.

## Baseline and authorization

The initial tracked tree was clean on `qa-security-engineer-version` at `63a5cb3`. The handoff and user request explicitly target this checkout, so it is the redesign baseline. Work is on `redesign/technical-support-portfolio`. `rollback/pre-support-redesign-63a5cb3` preserves the starting commit. The supplied handoff folder was added by the owner during the session and is left untouched. No push, merge, deployment, history rewrite or main edit was performed.

The original baseline differs from local main in 25 files. See `qa/baseline-vs-main.txt` for the complete per-file status and statistics. Public deployment/Actions responses show `main` at `22e1b27` (8 October 2026). The local tracking ref `origin/main` is exactly that commit; its tree is identical to baseline `63a5cb3` (zero-file diff). Local `main` is older at `d05f3f1`; do not confuse it with the deployed tracking ref. The unauthenticated Pages settings endpoint returns 404; exact account settings and publishing folder remain unconfirmed. Read-only responses are summarized in `qa/hosting-checks.json`.

## Factual decisions

| Topic | Status | Decision |
| --- | --- | --- |
| Career direction | Owner supplied | Technical Support Engineering; IT Support & Service Desk; Systems & Application Support; IT Operations. This is positioning, not a renamed historical role. |
| Help Desk role | Retained as-is | Help Desk Representative, Tech Bridge Solutions Ltd, remote, February 2025–Present. No inferred part-time/full-time label or named ticketing/remote tool. Confirm current status at release. |
| SAĜO trainee title | Pending owner | Keep website title QA & Security Engineer Trainee (July–September 2026). Generator says Engineer; no silent reconciliation. |
| SAĜO internship | Retained as-is | QA & Security Engineer Intern, March–June 2026. Preserve official employer spelling from the site. |
| Administration | Pending owner | Keep website June–December 2021 and Care and Cure Medical Center; generator says May–November and quote uses Care & Cure. |
| Earlier retail work | Retained as-is | Inventory Manager & Cashier, Bilaal Kidz, January 2022–January 2024. No new barcode/digitization achievements imported from the generator. |
| Education | Retained as-is | BSc expected November 2027; specialization August 2026–August 2027. Do not add generator-only CGPA or imply completed specialization. Confirm dates/study status before release. |
| ServiceDesk Simulator | Learning only | The owner-provided prompt establishes ongoing independent training. Display only “in progress; training focus: service desk practice”; no completed tickets, exercises, tools, badges or outcomes asserted. |
| Systems skills | Foundations / learning | Windows/Linux and networking foundations; existing AWS deployment-validation exposure remains Working Knowledge. AD/Microsoft 365/cloud administration are learning goals, not production administration claims. |
| Proficiency | Preserve / qualify | Preserve Practical Experience and Working Knowledge on source-supported work. Keep awareness labels; normalize Currently Building to Currently Learning. Qualify old generic admin tags as foundations or awareness. |
| Projects | Retained as-is | All 24 original entries, statuses, dates, tools and public links preserved. Portfolio description updated to reflect this redesign. VeriGuard/MailForge remain in progress. |
| AssureX demo | HTTP confirmed only | GET returned 200 at /signin. This establishes reachability, not authenticated functionality, ownership or independent verification of project claims. |
| Credentials | Source-confirmed scans | Preserve issuer/date/expiry text and all originals. 44 former cards map to 43 unique display records. AI job-search course belongs to two filters; neither original scan nor legacy anchor is removed. |
| Operating Systems Basics | Badge only | Existing About badge retained. No new certificate card fabricated; CS401: Operating Systems remains a distinct existing credential. |
| Recommendations | Exact text retained | All six quotes and attributions preserved; Gayeshan moved first and quoted verbatim on Home. No new performance claims or endorsement links. |
| Contact | Public primary retained | Gmail shown consistently, including failure fallback. LinkedIn/GitHub/WhatsApp/Discord remain. Endpoint unchanged; ownership, delivery, spam, retention and quotas unverified. No real submissions. |
| Portrait and testimonials | Existing public use retained | Derivatives of the already-published portrait only. No new workplace imagery; original files untouched. Existing permissions should be reconfirmed for release if changed. |
| Resume | Byte-identical | Existing PDF and generator untouched. QA-focused material and factual conflicts remain for a separate owner-approved update. |
| Confidential evidence / metrics | Missing, not invented | No SLA/CSAT/volume metrics, employer screenshots, customer tickets, internal hosts, private links or new credentials introduced. |

## Complete project mapping

Original source text, labels, links and certificate paths are backed up in `qa/evidence-baseline.json`; all binary originals have baseline SHA-256 hashes.

| Original entry | New location | Categories |
| --- | --- | --- |
| SAĜO MENTE Security & QA Initiatives | `projects.html#project-sa-o-mente-security-qa-initiatives` | professional qa-security application-security cloud-security |
| AssureX – Enterprise Quality, Security & Risk Assurance Platform | `projects.html#project-assurex-enterprise-quality-security-risk-assurance-platform` | professional qa-security application-security cloud-security academic-projects software-development applications academic |
| VeriGuard – Hybrid QA Automation & Testing Platform | `projects.html#project-veriguard-hybrid-qa-automation-testing-platform` | professional qa-security application-security software-development applications |
| MailForge – Email Campaign & Tracking Automation Platform | `projects.html#project-mailforge-email-campaign-tracking-automation-platform` | professional software-development qa-security applications |
| Personal Portfolio Website | `projects.html#project-personal-portfolio-website` | professional software-development applications |
| Defensive Cybersecurity Home Lab | `projects.html#project-defensive-cybersecurity-home-lab` | security-labs qa-security cyber-labs support-labs |
| OWASP-Oriented Web Testing | `projects.html#project-owasp-oriented-web-testing` | security-labs application-security qa-security cyber-labs support-labs |
| Cloud Security Experiments | `projects.html#project-cloud-security-experiments` | security-labs cloud-security qa-security cyber-labs support-labs |
| LetsDefend | `projects.html#project-letsdefend` | security-labs qa-security cyber-labs support-labs |
| TryHackMe | `projects.html#project-tryhackme` | security-labs qa-security cyber-labs support-labs |
| PicoCTF | `projects.html#project-picoctf` | security-labs application-security cyber-labs support-labs |
| Commonwealth Bank Introduction to Cybersecurity | `projects.html#project-commonwealth-bank-introduction-to-cybersecurity` | virtual-experience qa-security application-security simulations |
| Datacom Cybersecurity Job Simulation | `projects.html#project-datacom-cybersecurity-job-simulation` | virtual-experience qa-security simulations |
| Commonwealth Bank Tech Explorer | `projects.html#project-commonwealth-bank-tech-explorer` | virtual-experience simulations |
| AIG Shields Up | `projects.html#project-aig-shields-up` | virtual-experience application-security simulations |
| Tata Cybersecurity Security Analyst | `projects.html#project-tata-cybersecurity-security-analyst` | virtual-experience qa-security simulations |
| Deloitte Australia Cyber Job Simulation | `projects.html#project-deloitte-australia-cyber-job-simulation` | virtual-experience qa-security simulations |
| Mastercard Cybersecurity Virtual Experience | `projects.html#project-mastercard-cybersecurity-virtual-experience` | virtual-experience qa-security simulations |
| Smart Bus Route Finder | `projects.html#project-smart-bus-route-finder` | software-development academic-projects applications academic |
| AI Expert System: Tech Career Advisor | `projects.html#project-ai-expert-system-tech-career-advisor` | software-development academic-projects applications academic |
| Tic-Tac-Toe Game | `projects.html#project-tic-tac-toe-game` | software-development academic-projects applications academic |
| Simple Calculator | `projects.html#project-simple-calculator` | software-development academic-projects applications academic |
| Basic Hospital Appointment System | `projects.html#project-basic-hospital-appointment-system` | software-development academic-projects applications academic |
| GPA Calculator | `projects.html#project-gpa-calculator` | software-development academic-projects applications academic |

One additional entry: `projects.html#servicedesk-training`, ongoing independent learning only. All nine achievement badges retain their original reward links.

## Complete credential preview mapping

Each original preview ID remains a fragment anchor. With JS, original links open a named native dialog with a smaller derivative and an original-scan link. Without JS, they open the preserved scan directly.

| Original display label | Legacy anchor / current location | Original scan |
| --- | --- | --- |
| Google Cybersecurity Professional Certificate | `certifications.html#cert-google-cybersecurity` | `Certificates/GoogleCybersecurity.jpg` |
| Junior Cybersecurity Analyst | `certifications.html#cert-junior-cybersecurity` | `Certificates/JuniorCybersecurityAnalyst.jpg` |
| Certified Phishing Prevention Specialist (CPPS) | `certifications.html#cert-cpps` | `Certificates/CPPS.jpg` |
| Introduction to Software Testing | `certifications.html#cert-introduction-software-testing` | `Certificates/Introduction to Software Testing.jpg` |
| ISO/IEC 27701:2025 Lead Auditor | `certifications.html#cert-iso-27701-lead-auditor` | `Certificates/ISOIEC 277012025 Lead Auditor.jpg` |
| Sound the Alarm: Detection and Response | `certifications.html#cert-sound-alarm` | `Certificates/SoundsAlarm.jpg` |
| Assets, Threats, and Vulnerabilities | `certifications.html#cert-assets-threats` | `Certificates/Assets, Threats, and Vulnerabilities.jpg` |
| IT Security: Defense against the Digital Dark Arts | `certifications.html#cert-it-security` | `Certificates/IT_Security.jpg` |
| Play It Safe: Manage Security Risks | `certifications.html#cert-manage-risks` | `Certificates/Managerisk.jpg` |
| Foundations of Cybersecurity | `certifications.html#cert-foundations` | `Certificates/Foundation_Cybersecurity.jpg` |
| Cyber Kill Chains | `certifications.html#cert-kill-chain` | `Certificates/cyberkill.jpg` |
| Introduction to Cryptography | `certifications.html#cert-cryptography` | `Certificates/Intro_cryptography.jpg` |
| Cyber Security Track | `certifications.html#cert-cyber-track` | `Certificates/cyber_track.jpg` |
| Security Operations Center (SOC) | `certifications.html#cert-soc` | `Certificates/socanalyst.jpg` |
| Operationalizing MITRE ATT&CK for SOCs | `certifications.html#cert-mitre` | `Certificates/operationalizing-mitre-attck-for-socs.jpg` |
| Cyber Threat Management | `certifications.html#cert-threat-management` | `Certificates/cyberthreat.jpg` |
| Endpoint Security | `certifications.html#cert-endpoint` | `Certificates/Endpoint.jpg` |
| Network Defense | `certifications.html#cert-network-defense` | `Certificates/Network_Defence.jpg` |
| Student SOC Program - Foundations | `certifications.html#cert-student-soc` | `Certificates/soc.jpg` |
| Intro to Splunk (eLearning) | `certifications.html#cert-splunk` | `Certificates/Splunk.jpg` |
| Tools of the Trade: Linux and SQL | `certifications.html#cert-linux-sql` | `Certificates/Linex&SQL.jpg` |
| Connect & Protect: Network & Network Security | `certifications.html#cert-connect-protect` | `Certificates/ConnectNetwork.jpg` |
| Networking Devices & Initial Configuration | `certifications.html#cert-network-config` | `Certificates/networkconfig.jpg` |
| Networking Basics | `certifications.html#cert-networking-basics` | `Certificates/networkbasics.jpg` |
| Computer Hardware Basics | `certifications.html#cert-hardware` | `Certificates/hardware.jpg` |
| Introduction to Linux (LFS101) | `certifications.html#cert-linux` | `Certificates/Intro_Linux.jpg` |
| CS401: Operating Systems | `certifications.html#cert-operating-systems` | `Certificates/CS401_OS.jpg` |
| System Administration and IT Infrastructure Services | `certifications.html#cert-system-admin` | `Certificates/System Admin.jpg` |
| Certified Artificial Intelligence Security & Risk (CAISR) | `certifications.html#cert-caisr` | `Certificates/Certified Artificial Intelligence Security & Risk (CAISR).jpg` |
| AI Security Fundamentals | `certifications.html#cert-ai-security-fundamentals` | `Certificates/AI Security Fundamentals!_Cert.jpg` |
| Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate | `certifications.html#cert-oracle-ai` | `Certificates/oracle.jpg` |
| Introduction to CIP | `certifications.html#cert-cip` | `Certificates/introduction_to_cip.png` |
| Accelerate Your Job Search with AI | `certifications.html#cert-ai-job-search` | `Certificates/Accelerate Your Job Search with AI.jpg` |
| Mental Health in Cybersecurity | `certifications.html#cert-mental-health` | `Certificates/Mental_Health.jpg` |
| Automate Cybersecurity Tasks with Python | `certifications.html#cert-automate-python` | `Certificates/AutomateTasks.jpg` |
| Python Programming | `certifications.html#cert-python-gfg` | `Certificates/Python GFG.jpg` |
| Full Stack Development (HTML, CSS, Java, JavaScript) | `certifications.html#cert-full-stack` | `Certificates/FullStack.jpg` |
| The Git & GitHub Bootcamp | `certifications.html#cert-git-github` | `Certificates/GitHub.jpg` |
| Java Programming | `certifications.html#cert-java` | `Certificates/java_fundamental.jpg` |
| User Experience Design - Learn UI/UX with Figma | `certifications.html#cert-uiux` | `Certificates/UIUX_Design.jpg` |
| Technical Support Fundamentals | `certifications.html#cert-technical-support` | `Certificates/Tecgnical_support.jpg` |
| Practical Help Desk | `certifications.html#cert-help-desk` | `Certificates/practical-help-desk.jpg` |
| Put It to Work: Prepare for Cybersecurity Jobs | `certifications.html#cert-put-it-work` | `Certificates/Put It to Work.jpg` |
| Accelerate Your Job Search with AI | `certifications.html#cert-ai-job-search-pro` | `Certificates/Accelerate Your Job Search with AI.jpg` |

## Confirmation items before release

Confirm current Help Desk status and work arrangement; official trainee title and company styling; administrative dates/employer name; current education/project status; preferred public contact channels; Formspree endpoint ownership/delivery; testimonial/portrait permissions if changed; issuer verification links; and authenticated Pages settings. Preserve published source facts until confirmed. No optional factual question blocks this local review changeset.

## Owner-confirmed changes — 19 October 2026

These instructions supersede earlier date and theme assumptions: the Help Desk Representative role at Tech Bridge Solutions Ltd is remote and ran February 2025–October 2026. It is no longer labelled current. The site is dark-only, with no theme changer, and uses a fixed header on desktop and mobile. The owner requested a more distinctive professional design and 3D animation; the homepage now includes a decorative CSS 3D support scene with pause and reduced-motion support. The public resume PDF has not been edited.

## Latest header correction and review

The owner subsequently requested a non-fixed header. This supersedes the earlier fixed-header request: the header now remains in normal flow at all widths and scrolls out of view with the document. The review also removed obsolete reserved header spacing and no-JavaScript navigation clipping. Decorative animation stays static without JavaScript, and the inactive motion control is hidden. Dark-only styling and the confirmed employment dates remain in place.
