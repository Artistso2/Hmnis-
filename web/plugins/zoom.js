(function () {
  if (typeof mediumZoom !== 'function') return;
  mediumZoom('.visual-card img, .thumb img', {
    background: 'rgba(6, 3, 10, 0.92)',
    margin: 28,
    scrollOffset: 24
  });
})();
