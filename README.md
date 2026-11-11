# Mohamed Rimsan â€” Technical Support Engineering

A static, responsive portfolio built with HTML, CSS, and native JavaScript
modules. GitHub Pages serves it directly. There is no production build or
runtime dependency installation.

## Local preview

From the repository root:

```powershell
python -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. Stop the server with Ctrl+C. If Node.js is
installed, `npm run dev` starts the same server. Use HTTP for local previews
so the browser can load JavaScript modules.

## Repository structure

```text
â”œâ”€â”€ *.html                 # Public pages and legacy redirect
â”œâ”€â”€ assets/
â”‚   â”œâ”€â”€ css/
â”‚   â”‚   â”œâ”€â”€ main.css       # Ordered stylesheet imports
â”‚   â”‚   â”œâ”€â”€ base.css       # Tokens, resets, typography, utilities
â”‚   â”‚   â”œâ”€â”€ components.css # Shared layout and components
â”‚   â”‚   â”œâ”€â”€ home.css       # Homepage layout
â”‚   â”‚   â”œâ”€â”€ theme.css      # Colors, decorative visuals, motion
â”‚   â”‚   â”œâ”€â”€ components/    # Certificate preview styles
â”‚   â”‚   â””â”€â”€ pages/         # Skills and credential layouts
â”‚   â””â”€â”€ js/
â”‚       â”œâ”€â”€ main.js        # Shared feature initialization
â”‚       â”œâ”€â”€ features/      # Navigation, motion, filters, copy, contact
â”‚       â”œâ”€â”€ components/    # Certificate preview dialog
â”‚       â””â”€â”€ pages/         # Page-specific initialization
â”œâ”€â”€ Images/                # Public images and optimized derivatives
â”œâ”€â”€ Badges/                # Original badge images
â”œâ”€â”€ Certificates/          # Original certificate scans
â”œâ”€â”€ Resume/                # Published PDF and separate generator
â”œâ”€â”€ docs/                  # Architecture and maintenance guide
â”œâ”€â”€ scripts/               # Static, JavaScript, browser and accessibility checks
â”œâ”€â”€ requirements-qa.txt    # Development-only Python dependencies
â”œâ”€â”€ package.json           # Optional npm command shortcuts; no dependencies
â”œâ”€â”€ robots.txt
â””â”€â”€ sitemap.xml
```

Root page URLs and existing public image/document paths are kept stable.
See [architecture and maintenance](docs/architecture.md) for module ownership,
CSS order, and content conventions.

## Checks

Use Python 3.10+ and Node.js 18+. Install development dependencies once:

```powershell
python -m pip install -r requirements-qa.txt
```

Run static and JavaScript checks:

```powershell
python scripts/verify_site.py
node scripts/check-js.mjs
```

Or run both with `npm run check`.

Browser checks prefer installed Chrome and fall back to Playwright Chromium.
If neither is installed, run `python -m playwright install chromium` first.

```powershell
python scripts/browser_qa.py
python scripts/visual_refresh_qa.py
python scripts/accessibility_qa.py
```

The equivalent shortcuts are `npm run test:browser`, `npm run test:visual`, and
`npm run test:accessibility`. `python scripts/browser_qa.py --axe` also runs an
accessibility audit. Axe checks need network access to download axe-core 4.10.3.
Generated reports and screenshots are written to ignored `qa/` files.

Browser tests intercept contact-form requests; no real message is submitted.
Automated accessibility checks cover only part of accessibility validation.

## Publishing

Serve the repository root with GitHub Pages. No build command is required.
Keep public routes, asset casing, the resume PDF, and the Google verification
file intact. Review `git diff --check` and the checks above before releasing.
Publishing, pushing, and regenerating the resume are separate maintenance actions.
