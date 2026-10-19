/* Progressive enhancements: pages and evidence links also work without JavaScript. */
(() => {
  const root = document.documentElement;
  root.dataset.theme = 'dark';
  document.addEventListener('DOMContentLoaded', () => {
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
    const filterPanel = document.querySelector('[data-filter-panel]');
    if (filterPanel) {
      const buttons = [...filterPanel.querySelectorAll('[data-filter]')];
      const search = filterPanel.querySelector('[data-cert-search]');
      const status = filterPanel.querySelector('[data-results]');
      const isCertificates = !!search;
      const selector = isCertificates ? '[data-cert-category]' : 'article[data-project-category]';
      const cards = [...document.querySelectorAll(selector)];
      let category = 'all';
      const applyFilters = () => {
        const query = search?.value.trim().toLocaleLowerCase() || '';
        for (const card of cards) {
          const categories = (card.dataset.certCategory || card.dataset.projectCategory || '').split(' ');
          const text = `${card.dataset.certSearch || ''} ${card.textContent}`.toLocaleLowerCase();
          card.hidden = !((category === 'all' || categories.includes(category)) && text.includes(query));
        }
        document.querySelectorAll('.badge-strip[data-project-category]').forEach(strip => {
          strip.hidden = category !== 'all' && !strip.dataset.projectCategory.split(' ').includes(category);
        });
        document.querySelectorAll('[data-cert-section], [data-project-section]').forEach(section => {
          const items = [...section.querySelectorAll(selector)];
          const badge = section.querySelector('.badge-strip');
          section.hidden = items.length > 0 && items.every(card => card.hidden) && (!badge || badge.hidden);
        });
        const count = cards.filter(card => !card.hidden).length;
        if (status) status.textContent = count ? `${count} ${isCertificates ? 'credentials and learning entries' : 'projects and learning entries'} shown.` : 'No matches. Try another category or clear your search.';
        buttons.forEach(button => {
          const active = button.dataset.filter === category;
          button.setAttribute('aria-pressed', String(active));
          button.classList.toggle('active', active);
        });
      };
      buttons.forEach(button => button.addEventListener('click', () => { category = button.dataset.filter; applyFilters(); }));
      search?.addEventListener('input', applyFilters);
      filterPanel.hidden = false;
      applyFilters();
    }
    const copyStatus = document.querySelector('[data-copy-status]');
    document.querySelectorAll('[data-copy]').forEach(button => {
      button.hidden = false;
      button.addEventListener('click', async () => {
        try {
          if (navigator.clipboard?.writeText) await navigator.clipboard.writeText(button.dataset.copy);
          else {
            const field = document.createElement('textarea');
            field.value = button.dataset.copy;
            field.className = 'clipboard-helper';
            field.setAttribute('readonly', '');
            document.body.appendChild(field);
            field.select();
            let copied;
            try { copied = document.execCommand('copy'); } finally { field.remove(); button.focus(); }
            if (!copied) throw new Error('Copy unavailable');
          }
          if (copyStatus) copyStatus.textContent = 'Discord username copied.';
        } catch {
          if (copyStatus) copyStatus.textContent = 'Copy unavailable. Select and copy the displayed username instead.';
        }
      });
    });
    document.querySelectorAll('[data-contact-form]').forEach(form => {
      const status = form.querySelector('[data-form-status]');
      const submit = form.querySelector('[type="submit"]');
      const reset = form.querySelector('[type="reset"]');
      let pending = false;
      form.addEventListener('reset', () => { if (!pending && status) status.textContent = ''; });
      form.addEventListener('submit', async event => {
        if (!status || !submit) return;
        event.preventDefault();
        if (pending || !form.reportValidity()) return;
        pending = true;
        submit.disabled = true;
        if (reset) reset.disabled = true;
        form.setAttribute('aria-busy', 'true');
        status.className = 'form-status';
        status.textContent = 'Sending your message…';
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), 15000);
        try {
          const response = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' }, signal: controller.signal });
          if (!response.ok) throw new Error('Request rejected');
          form.reset();
          status.classList.add('success');
          status.textContent = 'The message service accepted your message. Thank you for getting in touch.';
        } catch (error) {
          status.classList.add('error');
          status.textContent = error.name === 'AbortError' ? 'Confirmation timed out; delivery is unknown. Your message is still here. You can email mohamed.rimsan.ar@gmail.com directly.' : 'The message service could not confirm your message. Your message is still here. Please email mohamed.rimsan.ar@gmail.com directly.';
        } finally {
          clearTimeout(timeout);
          pending = false;
          submit.disabled = false;
          if (reset) reset.disabled = false;
          form.removeAttribute('aria-busy');
        }
      });
    });
  });
  // This small shared script runs in the head, reserving the final menu layout
  // before first paint. If it fails to load, the static navigation stays visible.
  root.classList.add('nav-ready');
})();
