/**
 * Low-Vision Mode — High-contrast, large-text, reduced-visual-noise toggle.
 * Designed for Steven's specific visual profile: primarily pink perception,
 * limited color discrimination, reduced spatial awareness.
 *
 * Rule: This plugin changes presentation only. It does not invent content.
 */
(function () {
  const STORAGE_KEY = "hmnis_low_vision_mode";
  const BUTTON_ID = "hmnis-lv-toggle";

  const LV_CSS = `
    /* Low-Vision Mode Overrides */
    body.low-vision-mode {
      background: #0a0a0a !important;
      color: #ffc0cb !important; /* Pink text on near-black — maximum contrast for Steven */
      font-size: 150% !important;
      line-height: 1.8 !important;
    }
    body.low-vision-mode h1,
    body.low-vision-mode h2,
    body.low-vision-mode h3 {
      color: #ff69b4 !important; /* Hot pink headings */
      text-shadow: 0 0 2px rgba(255,105,180,0.3) !important;
    }
    body.low-vision-mode blockquote {
      border-left-color: #ff69b4 !important;
      background: rgba(255,105,180,0.05) !important;
      padding: 1em !important;
      font-size: 140% !important;
    }
    body.low-vision-mode a {
      color: #ff69b4 !important;
      text-decoration: underline !important;
      text-decoration-thickness: 2px !important;
    }
    body.low-vision-mode a:hover {
      color: #ffffff !important;
    }
    body.low-vision-mode .evidence-label,
    body.low-vision-mode [class*="label"] {
      outline: 2px solid #ff69b4 !important;
      padding: 0.2em 0.5em !important;
      font-weight: bold !important;
      font-size: 120% !important;
    }
    body.low-vision-mode img,
    body.low-vision-mode video {
      outline: 3px solid #ff69b4 !important;
    }
    body.low-vision-mode button,
    body.low-vision-mode input,
    body.low-vision-mode select,
    body.low-vision-mode textarea {
      font-size: 130% !important;
      min-height: 44px !important;
      border: 2px solid #ff69b4 !important;
    }
    body.low-vision-mode .glass-horizon-glow,
    body.low-vision-mode .horizon-glow,
    body.low-vision-mode [class*="glow"] {
      display: none !important; /* Remove subtle glow effects — low-vision doesn't benefit */
    }
    body.low-vision-mode .texture,
    body.low-vision-mode [class*="texture"],
    body.low-vision-mode [class*="paper"] {
      background-image: none !important; /* Remove paper/textured backgrounds */
    }
  `;

  function injectCSS() {
    const style = document.createElement("style");
    style.id = "hmnis-lv-css";
    style.textContent = LV_CSS;
    document.head.appendChild(style);
  }

  function createToggle() {
    const btn = document.createElement("button");
    btn.id = BUTTON_ID;
    btn.textContent = "👁 LV";
    btn.title = "Toggle Low-Vision Mode (high contrast, large text, pink-on-black)";
    btn.setAttribute("aria-label", "Toggle low-vision accessibility mode");
    Object.assign(btn.style, {
      position: "fixed",
      bottom: "12px",
      right: "12px",
      zIndex: "9999",
      background: "#1a1a1a",
      color: "#ff69b4",
      border: "2px solid #ff69b4",
      borderRadius: "50%",
      width: "48px",
      height: "48px",
      fontSize: "18px",
      cursor: "pointer",
      boxShadow: "0 0 8px rgba(255,105,180,0.4)",
      padding: "0",
      lineHeight: "48px",
      textAlign: "center",
    });
    btn.addEventListener("click", toggle);
    document.body.appendChild(btn);
  }

  function toggle() {
    const active = document.body.classList.toggle("low-vision-mode");
    localStorage.setItem(STORAGE_KEY, active ? "on" : "off");
    const btn = document.getElementById(BUTTON_ID);
    if (btn) {
      btn.style.background = active ? "#ff69b4" : "#1a1a1a";
      btn.style.color = active ? "#0a0a0a" : "#ff69b4";
    }
    // Announce to screen readers
    const announcement = document.createElement("div");
    announcement.setAttribute("role", "status");
    announcement.setAttribute("aria-live", "polite");
    announcement.textContent = active ? "Low-vision mode enabled" : "Low-vision mode disabled";
    announcement.style.position = "absolute";
    announcement.style.left = "-9999px";
    document.body.appendChild(announcement);
    setTimeout(() => announcement.remove(), 2000);
  }

  function init() {
    injectCSS();
    createToggle();
    // Restore saved state
    if (localStorage.getItem(STORAGE_KEY) === "on") {
      document.body.classList.add("low-vision-mode");
      const btn = document.getElementById(BUTTON_ID);
      if (btn) {
        btn.style.background = "#ff69b4";
        btn.style.color = "#0a0a0a";
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
