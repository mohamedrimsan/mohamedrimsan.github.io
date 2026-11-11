export function initFilters() {
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
}
