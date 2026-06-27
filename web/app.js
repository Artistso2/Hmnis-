(function () {
  const state = {
    current: STORY.start,
    history: []
  };

  const els = {
    title: document.getElementById('title'),
    subtitle: document.getElementById('subtitle'),
    date: document.getElementById('date'),
    location: document.getElementById('location'),
    speaker: document.getElementById('speaker'),
    text: document.getElementById('text'),
    tags: document.getElementById('tags'),
    choices: document.getElementById('choices'),
    sceneImage: document.getElementById('sceneImage'),
    imageCaption: document.getElementById('imageCaption'),
    backBtn: document.getElementById('backBtn'),
    resetBtn: document.getElementById('resetBtn')
  };

  function render(nodeId) {
    const node = STORY.nodes[nodeId];
    if (!node) {
      els.text.textContent = `[ERROR — NODE NOT FOUND: ${nodeId}]`;
      return;
    }

    state.current = nodeId;
    els.title.textContent = STORY.title;
    els.subtitle.textContent = STORY.subtitle || '';
    els.date.textContent = node.date || '—';
    els.location.textContent = node.location || '—';
    els.speaker.textContent = node.speaker || '—';
    els.text.textContent = node.text || '[NO TEXT PROVIDED]';

    if (node.image) {
      els.sceneImage.src = node.image;
      els.sceneImage.alt = node.imageCaption || 'Current scene visual';
    }
    els.imageCaption.textContent = node.imageCaption || 'Glass Horizons';

    els.tags.innerHTML = '';
    (node.tags || []).forEach(tag => {
      const span = document.createElement('span');
      span.className = 'tag';
      span.textContent = tag;
      els.tags.appendChild(span);
    });

    els.choices.innerHTML = '';
    (node.choices || []).forEach(choice => {
      const button = document.createElement('button');
      button.className = 'choice';
      button.type = 'button';
      button.textContent = choice.label;
      button.addEventListener('click', () => {
        state.history.push(state.current);
        render(choice.target);
      });
      els.choices.appendChild(button);
    });
  }

  document.querySelectorAll('.thumb').forEach(button => {
    button.addEventListener('click', () => {
      const target = button.getAttribute('data-target');
      if (target) {
        els.sceneImage.src = target;
        els.imageCaption.textContent = 'Author-provided visual theme asset';
      }
    });
  });

  els.backBtn.addEventListener('click', () => {
    const previous = state.history.pop();
    if (previous) render(previous);
  });

  els.resetBtn.addEventListener('click', () => {
    state.history = [];
    render(STORY.start);
  });

  render(state.current);
})();
