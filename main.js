document.addEventListener('DOMContentLoaded', () => {
  const nav = document.querySelector('nav');
  const hamburger = document.querySelector('.hamburger');
  const navLinks = [...document.querySelectorAll('nav a')];
  const typedText = document.getElementById('typed-text');
  const phrases = [
    'Cybersecurity Professional',
    'QA & Security Engineer Trainee',
    'Application Security',
    'Vulnerability Management',
    'Cloud Security',
    'Governance, Risk & Compliance',
  ];

  const closeNav = () => {
    nav?.classList.remove('show');
    hamburger?.setAttribute('aria-expanded', 'false');
  };

  const closePopups = () => {
    document.querySelectorAll('.popup.active').forEach((popup) => popup.classList.remove('active'));
    document.body.classList.remove('modal-open');
  };

  document.querySelectorAll('.popup').forEach((popup) => {
    if (popup.parentElement !== document.body) document.body.appendChild(popup);
  });

  if (hamburger && nav) {
    hamburger.setAttribute('aria-expanded', 'false');
    hamburger.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('show');
      hamburger.setAttribute('aria-expanded', String(isOpen));
    });
  }

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      closeNav();
      closePopups();
    }
  });

  const current = location.pathname.split('/').pop() || 'index.html';
  navLinks.forEach((link) => {
    if (link.getAttribute('href') === current) link.classList.add('active');
    link.addEventListener('click', closeNav);
  });

  if (typedText) {
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    const type = () => {
      const phrase = phrases[phraseIndex];
      typedText.textContent = isDeleting ? phrase.slice(0, charIndex--) : phrase.slice(0, charIndex++);
      let delay = isDeleting ? 45 : 95;

      if (!isDeleting && charIndex === phrase.length + 1) {
        isDeleting = true;
        delay = 1200;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        delay = 350;
      }

      setTimeout(type, delay);
    };

    setTimeout(type, 500);
  }

  const certSearch = document.querySelector('input[data-cert-search]');
  let activeFilter = document.querySelector('[data-filter].active')?.getAttribute('data-filter') || 'all';

  const applyFilters = () => {
    const query = certSearch?.value.trim().toLowerCase() || '';

    document.querySelectorAll('[data-cert-category]').forEach((card) => {
      const categories = card.getAttribute('data-cert-category')?.split(' ') || [];
      const searchableText = `${card.getAttribute('data-cert-search') || ''} ${card.textContent || ''}`.toLowerCase();
      const matchesFilter = activeFilter === 'all' || categories.includes(activeFilter);
      const matchesSearch = !query || searchableText.includes(query);
      card.hidden = !(matchesFilter && matchesSearch);
    });

    document.querySelectorAll('[data-project-category]').forEach((item) => {
      const categories = item.getAttribute('data-project-category')?.split(' ') || [];
      item.hidden = activeFilter !== 'all' && !categories.includes(activeFilter);
    });

    document.querySelectorAll('[data-cert-section]').forEach((section) => {
      const items = [...section.querySelectorAll('[data-cert-category]')];
      section.hidden = items.length > 0 && items.every((item) => item.hidden);
    });

    document.querySelectorAll('[data-project-section]').forEach((section) => {
      const items = [...section.querySelectorAll('[data-project-category]')];
      section.hidden = activeFilter !== 'all' && items.length > 0 && items.every((item) => item.hidden);
    });
  };

  document.querySelectorAll('[data-filter]').forEach((button) => {
    button.addEventListener('click', () => {
      activeFilter = button.getAttribute('data-filter') || 'all';
      document.querySelectorAll('[data-filter]').forEach((chip) => chip.classList.remove('active'));
      button.classList.add('active');
      applyFilters();
    });
  });

  certSearch?.addEventListener('input', applyFilters);
  applyFilters();

  document.querySelectorAll('.cert-preview[data-popup]').forEach((trigger) => {
    trigger.addEventListener('click', () => {
      const popup = document.getElementById(trigger.getAttribute('data-popup'));
      if (!popup) return;
      closePopups();
      popup.classList.add('active');
      document.body.classList.add('modal-open');
    });
  });

  document.querySelectorAll('.popup').forEach((popup) => {
    popup.addEventListener('click', (event) => {
      if (event.target === popup || event.target.classList.contains('close')) closePopups();
    });
  });

  document.querySelectorAll('[data-copy]').forEach((button) => {
    const originalHtml = button.innerHTML;
    button.addEventListener('click', async () => {
      const value = button.getAttribute('data-copy') || '';
      try {
        if (navigator.clipboard?.writeText) {
          await navigator.clipboard.writeText(value);
        } else {
          const textarea = document.createElement('textarea');
          textarea.value = value;
          textarea.setAttribute('readonly', '');
          textarea.style.position = 'fixed';
          textarea.style.left = '-9999px';
          document.body.appendChild(textarea);
          textarea.select();
          document.execCommand('copy');
          textarea.remove();
        }
        button.innerHTML = '<i class="fa-solid fa-check" aria-hidden="true"></i> Copied';
        setTimeout(() => {
          button.innerHTML = originalHtml;
        }, 1800);
      } catch {
        button.innerHTML = '<i class="fa-solid fa-circle-exclamation" aria-hidden="true"></i> Copy failed';
        setTimeout(() => {
          button.innerHTML = originalHtml;
        }, 1800);
      }
    });
  });

  document.querySelectorAll('[data-contact-form]').forEach((form) => {
    const status = form.querySelector('[data-form-status]');
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      if (!status) return form.submit();

      const submitButton = form.querySelector('button[type="submit"]');
      status.className = 'form-status';
      status.textContent = 'Sending your message...';
      submitButton?.setAttribute('disabled', 'true');

      try {
        const response = await fetch(form.action, {
          method: 'POST',
          body: new FormData(form),
          headers: { Accept: 'application/json' },
        });

        if (!response.ok) throw new Error('Form submission failed.');

        form.reset();
        status.classList.add('success');
        status.textContent = 'Thank you for your message. I will get back to you soon.';
      } catch {
        status.classList.add('error');
        status.innerHTML = 'Message service is unavailable right now. Please email me directly at <a href="mailto:mohamed.rimsan@outlook.com">mohamed.rimsan@outlook.com</a>.';
      } finally {
        submitButton?.removeAttribute('disabled');
      }
    });
  });
});