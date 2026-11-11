export function initContactForms() {
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
}
