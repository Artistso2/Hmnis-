(function () {
  window.HMNIS_AUDIO = {
    available: typeof Howl === 'function',
    rule: 'Audio hooks may play author-provided voice logs or narration only. They must not generate story content.'
  };
})();
