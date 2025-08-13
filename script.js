// Leaflet map init
const map = L.map('map', { attributionControl: true }).setView([22.9734, 78.6569], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

L.marker([28.6139, 77.2090])
  .addTo(map)
  .bindPopup('<strong>Directorate Office</strong><br>New Delhi')
  .openPopup();

// Scroll to map on button click
document.querySelectorAll('a[href="#map"]').forEach(el => {
  el.addEventListener('click', e => {
    e.preventDefault();
    document.getElementById('map').scrollIntoView({ behavior: 'smooth' });
    setTimeout(() => document.getElementById('map').focus(), 600);
  });
});

// Simple search demo
const search = document.getElementById('search');
search.addEventListener('keydown', e => {
  if (e.key === 'Enter') {
    const q = search.value.trim();
    if (!q) return;
    alert(`Search is a demo. Would search for: ${q}`);
  }
});
