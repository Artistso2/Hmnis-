(async function () {
  const status = document.getElementById('mapStatus');
  const rows = document.getElementById('locationRows');
  const mapEl = document.getElementById('map');

  function addRow(name, verification, description) {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${escapeHtml(name)}</td><td>${escapeHtml(verification)}</td><td>${escapeHtml(description)}</td>`;
    rows.appendChild(tr);
  }

  try {
    const response = await fetch('data/locations.geojson');
    const geojson = await response.json();
    const features = geojson.features || [];

    if (typeof L !== 'undefined') {
      const map = L.map(mapEl).setView([39.5, -98.35], 4);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; OpenStreetMap contributors'
      }).addTo(map);

      if (features.length) {
        const layer = L.geoJSON(geojson, {
          onEachFeature(feature, layer) {
            const p = feature.properties || {};
            layer.bindPopup(`<strong>${escapeHtml(p.label || 'Approved location')}</strong><br>${escapeHtml(p.address_or_description || '')}`);
          }
        }).addTo(map);
        map.fitBounds(layer.getBounds(), { padding: [24, 24] });
      }
    } else {
      mapEl.textContent = 'Map library not available.';
    }

    if (!features.length) {
      status.textContent = 'No approved coordinates have been added yet. Download the CSV/KML templates, add approved coordinates, then rebuild exports.';
      addRow('June 2025 Awakening Location', 'AUTHOR_DECLARED / COORDINATES UNKNOWN', '[UNKNOWN — STEVEN HAS NOT PROVIDED THIS]');
    } else {
      status.textContent = `${features.length} approved coordinate feature(s) loaded.`;
      features.forEach(feature => {
        const p = feature.properties || {};
        addRow(p.label || 'Approved location', p.verification_status || '', p.address_or_description || '');
      });
    }
  } catch (error) {
    status.textContent = `Map data could not be loaded: ${error.message}`;
    addRow('Map data unavailable', 'ERROR', 'Check web/data/locations.geojson');
  }

  function escapeHtml(value) {
    return String(value || '').replace(/[&<>"]/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[char]));
  }
})();
