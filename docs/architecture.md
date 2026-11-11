# Code organization

The portfolio is a static multipage site. GitHub Pages serves the repository
directly, with no compilation, runtime dependencies, or deployment framework.

## Pages and public files

The eight content pages stay at the repository root so existing URLs, canonical
links, and search engine results continue to work. `hands-on-experience.html`
redirects to Projects. Keep the Google verification document, `robots.txt`, and
`sitemap.xml` at the root as well.

`Images/`, `Badges/`, `Certificates/`, and `Resume/` are public asset archives.
Their paths are case sensitive on GitHub Pages. Preserve these URLs when adding
or reorganizing code. The resume PDF is a published document; its generator is
a separate maintenance tool and is never part of site startup or QA.

## Styles

`assets/css/main.css` imports the styles in cascade order:

1. `base.css`: design tokens, resets, typography, accessibility utilities.
2. `components.css`: shared layout, navigation, cards, forms, responsive rules.
3. `home.css`: homepage sections and their responsive layouts.
4. `theme.css`: final color treatment, decorative visuals, motion, print rules.
5. `pages/credentials.css`: support skills and credential layouts.

The import order preserves the existing design. Keep responsive and accessibility
rules alongside the components they affect. `components/certificate-viewer.css`
is loaded only by Projects and Credentials.

## JavaScript

`assets/js/main.js` imports and initializes modules under `features/`:

| Module | Responsibility |
| --- | --- |
| `navigation.js` | Mobile menu, keyboard dismissal, focus and breakpoint handling |
| `motion.js` | Pointer tilt, section entrances, reduced-motion preferences |
| `filters.js` | Project categories and credential category/text search |
| `clipboard.js` | Copy action and accessible feedback |
| `contact-form.js` | Validation, submission, timeout and status feedback |

Each feature exports one initializer and ignores pages without its DOM hooks.
Native module scripts execute after HTML parsing, so they can initialize directly
without another `DOMContentLoaded` listener. Use relative import paths with `.js`
extensions. Preview over HTTP because browsers restrict modules opened through
`file://`.

`pages/certificates.js` initializes `components/certificate-viewer.js` only on
Projects and Credentials. Certificate anchors still point to original scans;
JavaScript enhances them with a preview dialog. Without JavaScript, the site
keeps navigation, content, scan links, downloads, and native form submission.

## Content maintenance

- Keep the shared header and footer consistent across all eight pages. The
  current page has `aria-current="page"`; the navigation ID is
  `primary-navigation`.
- Use space-separated `data-project-category` or `data-cert-category` values
  for filters. Optional `data-cert-search` text augments credential searches.
- Keep `data-certificate` labels descriptive and scan links accessible without
  JavaScript. Preserve existing IDs used by incoming links.
- When changing content, update its title, description, social metadata,
  structured data, and sitemap date together.
- Preserve verified role titles, dates, issuer details, recommendation wording,
  and public contact methods. Keep learning goals distinct from experience.

## Development checks

`scripts/verify_site.py` checks the current site, including routes, exact asset
path casing, fragments, metadata, navigation, module imports, and CSS imports.
It does not depend on historical Git commits or a missing audit manifest.

Browser checks use a temporary loopback server and installed Chrome (or bundled
Chromium). They verify responsive layouts, enhancement behavior, and no-JavaScript
fallbacks. Form submissions are intercepted locally. Reports and screenshots go
to ignored `qa/` output. Accessibility checks additionally download axe-core
4.10.3; they require network access.

Run the commands in the root README. Python QA dependencies are listed separately
from the site. No package installation is required for the Node command shortcuts.
