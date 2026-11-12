export function initClipboard() {
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
}
