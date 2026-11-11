"""Shared paths and browser selection for local development checks."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "qa"
PAGES = ["index", "about", "experience", "projects", "skills", "certifications", "recommendations", "contact"]


def launch_chromium(playwright):
    """Prefer installed Chrome; allow the standard Playwright installation too."""
    try:
        return playwright.chromium.launch(channel="chrome", headless=True)
    except Exception:
        return playwright.chromium.launch(headless=True)
