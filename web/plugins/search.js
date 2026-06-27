(function () {
  const toggle = document.getElementById('searchToggle');
  const panel = document.getElementById('searchPanel');
  const input = document.getElementById('searchInput');
  const results = document.getElementById('searchResults');
  if (!toggle || !panel || !input || !results || !window.STORY) return;

  const records = Object.entries(STORY.nodes).map(([id, node]) => ({
    id,
    date: node.date || '',
    location: node.location || '',
    speaker: node.speaker || '',
    text: node.text || '',
    tags: (node.tags || []).join(' '),
    imageCaption: node.imageCaption || ''
  }));

  const fuse = typeof Fuse === 'function'
    ? new Fuse(records, { keys: ['date', 'location', 'speaker', 'text', 'tags', 'imageCaption'], threshold: 0.35, includeScore: true })
    : null;

  function draw(items) {
    results.innerHTML = '';
    if (!items.length) {
      results.innerHTML = '<p class="search-empty">No matching nodes.</p>';
      return;
    }
    items.slice(0, 10).forEach(item => {
      const record = item.item || item;
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'search-result';
      button.innerHTML = `<strong>${escapeHtml(record.date || record.id)}</strong><span>${escapeHtml(record.speaker)} — ${escapeHtml(snippet(record.text))}</span>`;
      button.addEventListener('click', () => {
        if (window.HMNIS && typeof window.HMNIS.render === 'function') {
          window.HMNIS.render(record.id, true);
          panel.hidden = true;
        }
      });
      results.appendChild(button);
    });
  }

  function runSearch() {
    const q = input.value.trim();
    if (!q) {
      draw(records);
      return;
    }
    draw(fuse ? fuse.search(q) : records.filter(r => JSON.stringify(r).toLowerCase().includes(q.toLowerCase())));
  }

  toggle.addEventListener('click', () => {
    panel.hidden = !panel.hidden;
    if (!panel.hidden) {
      input.focus();
      draw(records);
    }
  });

  input.addEventListener('input', runSearch);

  function snippet(text) {
    return text.length > 96 ? `${text.slice(0, 96)}…` : text;
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"]/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[char]));
  }
})();
