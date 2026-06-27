// HELLO, MY NAME IS STEVEN — Visual Novel Story Data
// Author-control rule: this file must contain only Steven-provided words or clearly marked scaffold placeholders.

const STORY = {
  title: "HELLO, MY NAME IS STEVEN",
  subtitle: "Glass Horizons / author-controlled visual novel scaffold",
  start: "node_001",
  nodes: {
    node_001: {
      date: "June 2025",
      location: "[UNKNOWN — STEVEN HAS NOT PROVIDED THIS FOR THIS NODE]",
      speaker: "Steven",
      image: "assets/glass_horizon_icon.png",
      imageCaption: "Glass Horizons — the manuscript as signal",
      text: "Steven wakes in June 2025. From that point forward, the book moves in real time. The past returns through recursion. The body becomes evidence. The internet becomes a prosthetic. AI becomes a contested tool. Due diligence becomes survival. The manuscript becomes the writ.",
      tags: ["TIMELINE_DECLARATION", "STEVEN_WORDS", "GLASS_HORIZONS"],
      choices: [
        { label: "Continue to the body log", target: "node_002" },
        { label: "Open the evidence protocol", target: "node_003" },
        { label: "View the visual direction", target: "node_005" }
      ]
    },
    node_002: {
      date: "June 2025",
      location: "[UNKNOWN — STEVEN HAS NOT PROVIDED THIS FOR THIS NODE]",
      speaker: "Scaffold",
      image: "assets/portrait_vertical.jpg",
      imageCaption: "Author-provided portrait material — body as evidence",
      text: "BODY LOG: walking, talking, pain, hunger, neuropathy, vision, hearing, balance, sleep, panic, complex PTSD. Fill only with Steven's provided words. Do not invent symptoms or explanations.",
      tags: ["BODY_EVIDENCE", "UNVERIFIED_DO_NOT_EXPAND"],
      choices: [
        { label: "Return", target: "node_001" },
        { label: "Move to memory recursion", target: "node_004" }
      ]
    },
    node_003: {
      date: "Repository Rule",
      location: "Author-Control Protocol",
      speaker: "Protocol",
      image: "assets/art_03.jpg",
      imageCaption: "Blueprint / silence / evidence grid",
      text: "AI may format, sequence, index, organize, check continuity, and package. AI may not invent names, facts, motives, agencies, diagnoses, scenes, dialogue, or missing timeline material.",
      tags: ["AI_USE_PROTOCOL"],
      choices: [
        { label: "Return", target: "node_001" }
      ]
    },
    node_004: {
      date: "June 2025 → Forward",
      location: "Linear Present Timeline",
      speaker: "Scaffold",
      image: "assets/art_05.jpg",
      imageCaption: "Steven's Constant / recursion motif",
      text: "RECURSION CYCLE: present event → body reaction → memory spark → confusion or contradiction → due diligence → partial verification or new gap → updated timeline → next present action.",
      tags: ["MEMORY_RECURSION", "STRUCTURE"],
      choices: [
        { label: "Return to start", target: "node_001" },
        { label: "View visual direction", target: "node_005" }
      ]
    },
    node_005: {
      date: "Visual Theme",
      location: "Glass Horizons",
      speaker: "Steven / Visual Direction",
      image: "assets/portrait_headphones.jpg",
      imageCaption: "Personal visual material — horizon-facing witness",
      text: "Visual theme: glass horizons. Something new. Personal artworks and pictures. The faces are of myself. The website should feel luminous, personal, forensic, digital, fragile, and forward-facing without losing the author-control rule.",
      tags: ["VISUAL_STYLE", "AUTHOR_PROVIDED_IMAGES", "NO_STOCK_IMAGERY"],
      choices: [
        { label: "Return to start", target: "node_001" },
        { label: "Open public record / horizon motif", target: "node_006" },
        { label: "Open artwork motif", target: "node_007" }
      ]
    },
    node_006: {
      date: "Visual Theme",
      location: "Sky / Flag / Public Record",
      speaker: "Scaffold",
      image: "assets/flag_horizon.jpg",
      imageCaption: "Author-provided flag horizon image",
      text: "This image enters the website as a horizon and public-record motif. It is not used to invent plot. It is visual atmosphere: sky, country, witness, exposure, and the demand that the record answer.",
      tags: ["VISUAL_MOTIF", "PUBLIC_RECORD", "DO_NOT_OVERWRITE_AUTHOR_MEANING"],
      choices: [
        { label: "Back to visual direction", target: "node_005" },
        { label: "Return to start", target: "node_001" }
      ]
    },
    node_007: {
      date: "Visual Theme",
      location: "Author Artwork Set",
      speaker: "Scaffold",
      image: "assets/art_01.jpg",
      imageCaption: "Author-provided artwork set",
      text: "The artwork set becomes the visual language of memory cards: equilibrium, boots, blueprint, silence, constants, recursion, and signal. The site uses these as atmosphere and navigation, not as invented facts.",
      tags: ["AUTHOR_ARTWORK", "MEMORY_CARDS", "GLASS_HORIZONS"],
      choices: [
        { label: "Next artwork card", target: "node_008" },
        { label: "Back to visual direction", target: "node_005" }
      ]
    },
    node_008: {
      date: "Visual Theme",
      location: "Author Artwork Set",
      speaker: "Scaffold",
      image: "assets/art_02.jpg",
      imageCaption: "Author-provided artwork set",
      text: "The visual novel interface can move between written testimony, body log, evidence protocol, and memory recursion while the image panel acts as an evidence/memory/signal card.",
      tags: ["VISUAL_NOVEL", "EVIDENCE_CARD", "MEMORY_RECURSION"],
      choices: [
        { label: "Next artwork card", target: "node_009" },
        { label: "Return to start", target: "node_001" }
      ]
    },
    node_009: {
      date: "Visual Theme",
      location: "Author Artwork Set",
      speaker: "Scaffold",
      image: "assets/art_04.jpg",
      imageCaption: "Author-provided artwork set",
      text: "All visual materials remain attached to the author-control rule. No stock imagery. No invented symbolism. No AI hallucination. The files are preserved as source material and optimized for web delivery.",
      tags: ["AUTHOR_CONTROL", "VISUAL_SOURCE", "NO_HALLUCINATION"],
      choices: [
        { label: "Return to visual direction", target: "node_005" },
        { label: "Return to start", target: "node_001" }
      ]
    }
  }
};
