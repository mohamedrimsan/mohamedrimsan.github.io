"""Generate the common portfolio resume PDF."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer

OUT = Path(__file__).with_name("AR-Mohamed-Rimsan-Resume.pdf")
ACCENT, INK, MUTED = colors.HexColor("#155E75"), colors.HexColor("#172033"), colors.HexColor("#475569")
font_dir = Path("C:/Windows/Fonts")
if (font_dir / "arial.ttf").exists():
    pdfmetrics.registerFont(TTFont("ResumeSans", str(font_dir / "arial.ttf")))
    pdfmetrics.registerFont(TTFont("ResumeSans-Bold", str(font_dir / "arialbd.ttf")))
    BODY, BOLD = "ResumeSans", "ResumeSans-Bold"
else:
    BODY, BOLD = "Helvetica", "Helvetica-Bold"

def style(name, font=BODY, size=8.3, leading=10.4, color=INK, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=leading, textColor=color, **kw)
S = {
    "name": style("Name", BOLD, 19, 21, alignment=TA_CENTER, spaceAfter=3),
    "role": style("Role", BOLD, 11.5, 14, ACCENT, alignment=TA_CENTER, spaceAfter=2),
    "center": style("Center", size=9, leading=11.3, alignment=TA_CENTER, spaceAfter=3),
    "contact": style("Contact", size=8.3, leading=10.6, color=MUTED, alignment=TA_CENTER, spaceAfter=7),
    "section": style("Section", BOLD, 10.5, 12, ACCENT, spaceBefore=5, spaceAfter=1),
    "body": style("Body", size=9, leading=11.5, spaceAfter=3),
    "title": style("Title", BOLD, 9.6, 11.5, spaceAfter=1),
    "meta": style("Meta", size=8.3, leading=10, color=MUTED, spaceAfter=2),
    "bullet": style("Bullet", size=8.7, leading=10.9, leftIndent=10, firstLineIndent=-7, spaceAfter=1.2),
    "compact": style("Compact", size=8.6, leading=10.7, spaceAfter=1.7),
}
def P(text, key="body"): return Paragraph(text, S[key])
def sec(title): return [P(title.upper(), "section"), HRFlowable(width="100%", thickness=.55, color=colors.HexColor("#CBD5E1"), spaceBefore=0, spaceAfter=3)]
def bullets(items): return [P("- " + item, "bullet") for item in items]
def role(title, org, meta, items):
    return KeepTogether([P(f"{title} | {org}", "title"), P(meta, "meta"), *bullets(items), Spacer(1, 2)])
def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#CBD5E1")); canvas.setLineWidth(.5)
    canvas.line(doc.leftMargin, 12*mm, A4[0]-doc.rightMargin, 12*mm)
    canvas.setFont(BODY, 7); canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 8*mm, "AR Mohamed Rimsan - Common Portfolio Resume")
    canvas.drawRightString(A4[0]-doc.rightMargin, 8*mm, f"Page {doc.page}")
    canvas.restoreState()

def build():
    doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=15*mm, rightMargin=15*mm, topMargin=11*mm, bottomMargin=17*mm,
        title="AR Mohamed Rimsan - QA & Security Engineer Resume", author="AR Mohamed Rimsan",
        subject="Common portfolio resume covering cybersecurity, quality assurance, and technical support")
    story = [
        P("AR Mohamed Rimsan", "name"), P("QA &amp; Security Engineer", "role"),
        P("Cybersecurity | Quality Assurance | Technical Support", "center"),
        P("Application Security | QA Automation | Web, Mobile &amp; API Testing | Vulnerability Management | AWS &amp; Cloud Security", "center"),
        P('<link href="mailto:mohamed.rimsan.ar@gmail.com" color="#155E75">mohamed.rimsan.ar@gmail.com</link> | <link href="https://www.linkedin.com/in/mohamed-rimsan-a-r" color="#155E75">linkedin.com/in/mohamed-rimsan-a-r</link> | <link href="https://github.com/mohamedrimsan" color="#155E75">github.com/mohamedrimsan</link><br/><link href="https://mohamedrimsan.github.io/" color="#155E75">mohamedrimsan.github.io</link> | Western Province, Sri Lanka', "contact"),
        *sec("Professional Summary"),
        P("QA &amp; Security Engineer and BSc (Hons) Information Technology undergraduate with hands-on experience across cybersecurity, software quality assurance, QA automation, application security, vulnerability management, cloud environments, and technical support. Professional experience includes web, mobile, and API testing, defect investigation, security validation, release verification, AWS/CI/CD environments, remote troubleshooting, incident handling, and cross-functional collaboration."),
        *sec("Professional Experience"),
        role("QA &amp; Security Engineer", "SAĜO Mente International Sdn Bhd", "Full-time | Jul 2026 - Sep 2026 | Moratuwa, Western Province, Sri Lanka | On-site", [
            "Performed functional, regression, end-to-end, responsive, and release testing across web and mobile applications.",
            "Validated REST APIs, authentication, authorization, input handling, business logic, and frontend/backend data flows using Postman and Swagger/OpenAPI.",
            "Built and executed QA automation using Playwright while strengthening mobile automation capability with Appium.",
            "Performed application security and vulnerability testing covering authentication, authorization, access control, data exposure, and API security.",
            "Investigated, reproduced, documented, and verified defects through Jira in collaboration with development teams.",
            "Conducted performance and reliability testing using k6 and JMeter and supported AWS/CI/CD deployment and release verification.",
            "Contributed to security, privacy, risk, and compliance reviews and production-readiness activities with QA, development, UI/UX, DevOps, and operational teams.",
        ]),
        role("QA &amp; Security Engineer Intern", "SAĜO Mente International Sdn Bhd", "Internship | Mar 2026 - Jun 2026 | Moratuwa, Western Province, Sri Lanka | On-site", [
            "Conducted functional, regression, usability, end-to-end, and mobile testing across web and mobile applications.",
            "Validated core workflows and APIs, identifying functional issues, UI/UX inconsistencies, workflow gaps, and security concerns.",
            "Documented defects in Jira, reproduced reported issues, and re-tested fixes, workflow changes, and deployments.",
            "Supported application security testing and collaborated with developers, QA team members, and UI/UX designers on product quality and release readiness.",
        ]),
        role("Help Desk Representative", "Tech Bridge Solutions Ltd", "Part-time | Feb 2025 - Present | Manchester, England, United Kingdom | Remote", [
            "Provide remote technical support and troubleshoot user issues with practical, step-by-step guidance.",
            "Log incidents, complaints, and service requests while maintaining accurate support records.",
            "Escalate complex issues to appropriate teams and communicate progress clearly throughout the support process.",
            "Support issue follow-up and resolution through user communication and cross-team coordination.",
        ]),
        *sec("Selected Projects"),
        role("VeriGuard - Hybrid QA Automation &amp; Testing Platform", "Active Development", "TypeScript, Next.js, NestJS, PostgreSQL, Prisma, Redis, BullMQ, Docker, Jest, REST APIs", [
            "Developing a scalable QA automation platform to manage organizations, projects, environments, and automated testing workflows.",
            "Implemented task lifecycle management, API integration testing, health/readiness monitoring, and AES-256-GCM protection for sensitive credentials.",
        ]),
        PageBreak(), *sec("Selected Projects (Continued)"),
        role("AssureX - Enterprise Quality, Security &amp; Risk Assurance Platform", "Completed Portfolio Project", "Next.js, TypeScript, PostgreSQL, Prisma, Playwright, Docker", [
            "Built a full-stack QA and security assurance platform supporting test case management, vulnerability management, asset/remediation tracking, and CVSS v3.1 scoring.",
            "Implemented RBAC, MFA, audit logging, security reporting, dashboards, and Playwright end-to-end testing.",
        ]),
        *sec("Technical Skills"),
    ]
    groups = [
        ("Cybersecurity", "Application Security, Security Testing, API Security, Vulnerability Assessment, Vulnerability Management, IAM/Access Control, Cloud Security, Risk/GRC, Incident Response"),
        ("QA &amp; Testing", "Software QA, QA Automation, Web Testing, Mobile Testing, API Testing, Functional Testing, Regression Testing, End-to-End Testing, Performance Testing, UAT"),
        ("QA / Security Tools", "Playwright, Postman, Swagger/OpenAPI, Burp Suite, OWASP ZAP, MobSF, Snyk, SonarQube, JMeter, k6, Jira"),
        ("Technical Support", "Troubleshooting, Remote Support, Incident Handling, Incident Management, Windows, Linux, Networking, Hardware/Software Troubleshooting"),
        ("Cloud / DevOps", "AWS, ECS, ECR, Docker, CI/CD, Git, GitHub"),
        ("Development", "TypeScript, JavaScript, Next.js, NestJS, Node.js, PostgreSQL, Prisma, Redis, REST APIs, SQL, Python"),
    ]
    story += [P(f"<b>{label}:</b> {values}", "compact") for label, values in groups]
    story += [
        *sec("Education"),
        P("<b>BSc (Hons) in Information Technology</b> | The Open University of Sri Lanka<br/>Nov 2023 - Nov 2027 | Current CGPA: 3.46 | Activities: Member, iTeam", "compact"),
        *sec("Certifications"),
        P("<b>Google Cybersecurity Professional Certificate</b> | Google / Coursera | Completed Jan 2026", "compact"),
        P("<b>Cisco Junior Cybersecurity Analyst Career Path</b> | Cisco Networking Academy | Completed Jul 2025", "compact"),
        P("<b>Software Testing and Automation Specialization</b> | University of Minnesota / Coursera | In Progress", "compact"),
        *sec("Practical Security Training"),
        P("<b>LetsDefend SOC Analyst Labs:</b> Hands-on training in security alert investigation, log analysis, phishing analysis, web attack detection, and incident response workflows.", "compact"),
        *sec("Additional Experience"),
        P("<b>Inventory Manager and Cashier | Bilaal Kidz | Jan 2022 - Jan 2024</b><br/>Managed inventory, records, transactions, and daily POS operations; implemented a barcode-based inventory process and supported structured reconciliation.", "compact"),
        P("<b>Administrative Assistant | Care and Cure Medical Center | May 2021 - Nov 2021</b><br/>Managed administrative records and routine office processes, supported inquiries, and helped digitize administrative workflows.", "compact"),
    ]
    doc.build(story, onFirstPage=footer, onLaterPages=footer)

if __name__ == "__main__":
    build()
    print(OUT)