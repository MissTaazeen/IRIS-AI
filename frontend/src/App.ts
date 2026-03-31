import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

export class App {
  private container: HTMLElement;
  private map: maplibregl.Map | null = null;

  constructor() {
    this.container = document.getElementById('app') as HTMLElement;
  }

  init() {
    this.renderLayout();
    this.initializeMap();
    this.startClock(); // ✅ live clock
  }

  private renderLayout() {
    this.container.innerHTML = `
      <div class="h-14 bg-[#111118] border-b border-gray-800 flex items-center px-6 justify-between">
        <div class="flex items-center gap-4">
          <span class="text-3xl">🇮🇳</span>
          <div>
            <h1 class="text-2xl font-bold tracking-tighter">IRIS</h1>
            <p class="text-xs text-emerald-400">
              LIVE • NATIONAL INTELLIGENCE DASHBOARD
            </p>
          </div>
        </div>

        <div class="flex items-center gap-4">
          <div class="text-emerald-400 text-sm">● LIVE (Simulation)</div>
          <div id="live-time" class="text-sm text-gray-400"></div>
        </div>
      </div>

      <div class="flex flex-1 overflow-hidden">
        <!-- Sidebar -->
        <div class="w-72 bg-[#111118] border-r border-gray-800 p-6">
          <h2 class="uppercase text-xs text-gray-500 mb-6">DATA LAYERS</h2>

          <div class="space-y-3 text-sm">
            <label class="flex items-center gap-3 p-3">
              🌧️ Weather & Monsoon
            </label>
            <label class="flex items-center gap-3 p-3">
              ⚓ Major Ports
            </label>
            <label class="flex items-center gap-3 p-3">
              🔴 Conflict Zones
            </label>
            <label class="flex items-center gap-3 p-3">
              📈 Finance Radar
            </label>
          </div>
        </div>

        <!-- Map -->
        <div id="map-container" class="flex-1"></div>

        <!-- Right Panel -->
        <div class="w-96 bg-[#111118] border-l border-gray-800 p-6">
          <h2 class="text-lg mb-4">National AI Brief</h2>
          <div class="text-sm text-gray-400">
            Simulation mode: real-time intelligence layer visualization
          </div>

          <h2 class="text-lg mt-6 mb-4">Risk Index</h2>
          <div class="text-5xl text-gray-500">--</div>
        </div>
      </div>
    `;
  }

  private initializeMap() {
    const mapContainer = document.getElementById('map-container') as HTMLElement;

    this.map = new maplibregl.Map({
      container: mapContainer,
      style: 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json',
      center: [78.9629, 22.5937],
      zoom: 4.5,
      minZoom: 4,
      maxBounds: [
        [67, 6],
        [97, 37]
      ]
    });

    this.map.addControl(new maplibregl.NavigationControl(), 'top-right');

    this.map.on('load', async () => {
      console.log('✅ Map loaded');

      const res = await fetch('/india_state_geo.json');
      const geojson = await res.json();

      this.map!.addSource('india-states', {
        type: 'geojson',
        data: geojson
      });

      // Fill layer
      this.map!.addLayer({
        id: 'states-fill',
        type: 'fill',
        source: 'india-states',
        paint: {
          'fill-color': '#00FFFF',
          'fill-opacity': 0.2
        }
      });

      // Border layer
      this.map!.addLayer({
        id: 'states-outline',
        type: 'line',
        source: 'india-states',
        paint: {
          'line-color': '#ffffff',
          'line-width': 1.5
        }
      });

      // ✅ CLICK POPUP
      this.map!.on('click', 'states-fill', (e: any) => {
        const state = e.features[0].properties.NAME_1;

        new maplibregl.Popup()
          .setLngLat(e.lngLat)
          .setHTML(`<b>${state}</b>`)
          .addTo(this.map!);
      });

      // ✅ HOVER EFFECT
      this.map!.on('mouseenter', 'states-fill', () => {
        this.map!.getCanvas().style.cursor = 'pointer';
      });

      this.map!.on('mouseleave', 'states-fill', () => {
        this.map!.getCanvas().style.cursor = '';
      });
    });
  }

  // ✅ LIVE CLOCK
  private startClock() {
    const el = document.getElementById('live-time');

    setInterval(() => {
      const now = new Date();
      if (el) el.textContent = now.toLocaleTimeString() + " IST";
    }, 1000);
  }
}