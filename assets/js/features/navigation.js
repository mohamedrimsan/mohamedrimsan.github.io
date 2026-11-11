export function initNavigation() {
  const root = document.documentElement;
  const nav = document.getElementById('primary-navigation');
  const menu = document.querySelector('.hamburger');
  const compact = matchMedia('(max-width: 1199px)');
  const setMenu = (open, restore = false) => {
    if (!nav || !menu) return;
    nav.classList.toggle('show', open);
    menu.setAttribute('aria-expanded', String(open));
    if (restore) menu.focus();
  };
  if (nav && menu) {
    menu.hidden = false;
    menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
    nav.addEventListener('click', event => { if (event.target.closest('a')) setMenu(false); });
    document.addEventListener('click', event => {
      if (!nav.contains(event.target) && !menu.contains(event.target)) setMenu(false);
    });
    document.addEventListener('focusin', event => {
      if (compact.matches && !nav.contains(event.target) && !menu.contains(event.target)) setMenu(false);
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') setMenu(false, true);
    });
    compact.addEventListener('change', () => {
      const focusedLink = nav.contains(document.activeElement);
      setMenu(false, compact.matches && focusedLink);
    });
    root.classList.add('nav-ready');
  }
}
