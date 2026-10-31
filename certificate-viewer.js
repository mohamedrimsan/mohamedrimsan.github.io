/* Shared certificate lightbox for certifications.html and projects.html. */
document.addEventListener('DOMContentLoaded', () => {
  const links = [...document.querySelectorAll('a.cert-preview[href]')];
  if (!links.length || typeof HTMLDialogElement === 'undefined') return;
  const dialog = document.createElement('dialog');
  dialog.className = 'certificate-lightbox';
  dialog.setAttribute('aria-labelledby', 'certificate-lightbox-title');
  dialog.innerHTML = `
    <div class="certificate-lightbox-header">
      <div><small>Certificate preview</small><h2 id="certificate-lightbox-title">Certificate</h2></div>
      <button type="button" class="certificate-lightbox-close" aria-label="Close viewer">×</button>
    </div>
    <div class="certificate-lightbox-stage"><img alt="" hidden><p role="status">Loading certificate…</p></div>
    <div class="certificate-lightbox-footer">
      <div class="certificate-lightbox-actions">
        <button type="button" data-prev aria-label="Previous certificate">←</button>
        <span data-count aria-live="polite"></span>
        <button type="button" data-next aria-label="Next certificate">→</button>
      </div>
      <div class="certificate-lightbox-actions">
        <button type="button" data-minus aria-label="Zoom out">−</button>
        <output data-zoom>100%</output>
        <button type="button" data-plus aria-label="Zoom in">+</button>
        <a data-download download>↓ Download</a>
      </div>
    </div>`;
  document.body.appendChild(dialog);
  const title = dialog.querySelector('h2');
  const stage = dialog.querySelector('.certificate-lightbox-stage');
  const img = stage.querySelector('img');
  const status = stage.querySelector('p');
  const prev = dialog.querySelector('[data-prev]');
  const next = dialog.querySelector('[data-next]');
  const count = dialog.querySelector('[data-count]');
  const plus = dialog.querySelector('[data-plus]');
  const minus = dialog.querySelector('[data-minus]');
  const zoomLabel = dialog.querySelector('[data-zoom]');
  const download = dialog.querySelector('[data-download]');
  let gallery = [], index = 0, zoom = 1;

  function applyZoom() {
    zoomLabel.textContent = `${Math.round(zoom * 100)}%`;
    minus.disabled = zoom <= 1;
    plus.disabled = zoom >= 3;
    if (img.hidden || !img.naturalWidth) return;
    const fit = Math.min((stage.clientWidth - 32) / img.naturalWidth,
      (stage.clientHeight - 32) / img.naturalHeight, 1);
    img.style.width = `${Math.max(1, Math.round(img.naturalWidth * fit * zoom))}px`;
  }
  function show(i) {
    if (i < 0 || i >= gallery.length) return;
    index = i;
    const link = gallery[i];
    const name = link.dataset.certificate || 'Certificate';
    title.textContent = name;
    img.alt = name;
    img.hidden = true;
    img.removeAttribute('src');
    img.style.width = '';
    status.hidden = false;
    status.textContent = 'Loading certificate…';
    zoom = 1;
    count.textContent = `${i + 1} / ${gallery.length}`;
    prev.disabled = i === 0;
    next.disabled = i === gallery.length - 1;
    download.href = link.href;
    download.download = decodeURIComponent(new URL(link.href).pathname.split('/').pop() || 'certificate');
    stage.scrollTo(0, 0);
    applyZoom();
    img.src = link.href;
  }
  img.addEventListener('load', () => {
    img.hidden = false;
    status.hidden = true;
    applyZoom();
  });
  img.addEventListener('error', () => {
    img.hidden = true;
    status.hidden = false;
    status.textContent = 'Preview unavailable. Open or download the original certificate.';
  });
  links.forEach(link => {
    link.setAttribute('aria-label', `Preview ${link.dataset.certificate || 'certificate'} in popup`);
    link.setAttribute('aria-haspopup', 'dialog');
    link.removeAttribute('target');
    link.addEventListener('click', event => {
      if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      gallery = links.filter(a => !a.closest('[hidden]'));
      if (!gallery.includes(link)) gallery = [link];
      dialog.showModal();
      show(gallery.indexOf(link));
    });
  });
  dialog.querySelector('.certificate-lightbox-close').addEventListener('click', () => dialog.close());
  prev.addEventListener('click', () => show(index - 1));
  next.addEventListener('click', () => show(index + 1));
  plus.addEventListener('click', () => { zoom = Math.min(3, zoom + .25); applyZoom(); });
  minus.addEventListener('click', () => { zoom = Math.max(1, zoom - .25); applyZoom(); });
  dialog.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' && !next.disabled) { e.preventDefault(); show(index + 1); }
    if (e.key === 'ArrowLeft' && !prev.disabled) { e.preventDefault(); show(index - 1); }
  });
  dialog.addEventListener('click', e => { if (e.target === dialog) dialog.close(); });
  dialog.addEventListener('close', () => { img.removeAttribute('src'); gallery = []; });
  window.addEventListener('resize', () => { if (dialog.open) applyZoom(); });
});
