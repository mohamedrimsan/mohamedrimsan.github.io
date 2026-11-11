export function initMotion() {
  const root = document.documentElement;
  const motion = matchMedia('(prefers-reduced-motion: reduce)');

  const tiltPanels = [...document.querySelectorAll('[data-tilt]')];
  const pointer = matchMedia('(hover: hover) and (pointer: fine)');
  const resetTilt = () => tiltPanels.forEach(panel => {
    panel.style.removeProperty('--tilt-x');
    panel.style.removeProperty('--tilt-y');
  });
  if (tiltPanels.length) {
    root.classList.add('motion-ready');
    motion.addEventListener('change', resetTilt);
    pointer.addEventListener('change', resetTilt);
    tiltPanels.forEach(panel => {
      let frame = 0;
      panel.addEventListener('pointermove', event => {
        if (motion.matches || !pointer.matches) return;
        const rect = panel.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - .5;
        const y = (event.clientY - rect.top) / rect.height - .5;
        cancelAnimationFrame(frame);
        frame = requestAnimationFrame(() => {
          if (motion.matches || !pointer.matches) return;
          panel.style.setProperty('--tilt-x', `${-y * 8}deg`);
          panel.style.setProperty('--tilt-y', `${x * 10}deg`);
        });
      });
      panel.addEventListener('pointerleave', () => { cancelAnimationFrame(frame); resetTilt(); });
    });
  }

  // Reveal once, and leave every section visible when JavaScript is unavailable.
  if ('IntersectionObserver' in window && !motion.matches) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: .08 });
    document.querySelectorAll('.home-page .home-section, .home-page .foundations-section, .home-page .recommendation-section').forEach(section => observer.observe(section));
  }
}
