(function () {
  const root = document.documentElement;
  window.addEventListener('pointermove', event => {
    const x = Math.round((event.clientX / Math.max(1, window.innerWidth)) * 100);
    const y = Math.round((event.clientY / Math.max(1, window.innerHeight)) * 100);
    root.style.setProperty('--pointer-x', `${x}%`);
    root.style.setProperty('--pointer-y', `${y}%`);
  }, { passive: true });
})();
