(function () {
  const pages = {
    'landing.html': { section: 'Public Face', title: 'Landing' },
    'paper.html': { section: 'Book Visual', title: 'Paper Writ' },
    'writ.html': { section: 'Formalization', title: 'Academic Writ' },
    'index.html': { section: 'Interactive', title: 'Visual Novel' },
    'map.html': { section: 'Roadmap', title: 'Timeline Map' },
    'design-lab.html': { section: 'Visual System', title: 'Design Lab' }
  };
  const file = (window.location.pathname.split('/').pop() || 'index.html');
  const page = pages[file] || { section: 'Project Page', title: document.title || file };

  const nav = document.createElement('nav');
  nav.className = 'hmnis-global-nav';
  nav.setAttribute('aria-label', 'Project breadcrumbs and navigation');
  nav.innerHTML = `
    <div class="hmnis-crumbs">
      <a href="../index.html">Project Index</a>
      <span>/</span>
      <span>${escapeHtml(page.section)}</span>
      <span>/</span>
      <span class="hmnis-current">${escapeHtml(page.title)}</span>
    </div>
    <div class="hmnis-nav-links" aria-label="Primary project links">
      <a href="landing.html">Landing</a>
      <a href="paper.html">Paper Writ</a>
      <a href="writ.html">Academic Writ</a>
      <a href="index.html">Visual Novel</a>
      <a href="map.html">Map</a>
      <a href="design-lab.html">Design Lab</a>
    </div>
  `;
  document.body.insertBefore(nav, document.body.firstChild);


  if (!document.querySelector('.hmnis-global-footer')) {
    const footer = document.createElement('footer');
    footer.className = 'hmnis-global-footer';
    footer.innerHTML = `
      <div><strong>Steven Owens</strong> / <a href="https://github.com/Artistso2/Hmnis-">GitHub</a> / <a href="https://soquarky.click">soquarky.click</a></div>
      <div><span>@soquarky</span> · Hello, My Name is Steven: The Lived Experience of Habeas Corpus</div>
    `;
    document.body.appendChild(footer);
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"]/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[char]));
  }
})();
