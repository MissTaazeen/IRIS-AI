import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

export class App {
  private container: HTMLElement;
  private map: maplibregl.Map | null = null;
  private conflictMarkers: maplibregl.Marker[] = [];

  constructor() {
    this.container = document.getElementById('app') as HTMLElement;
  }

  init() {
    this.renderLayout();
    this.initializeMap();
    this.loadBackendData();
    this.setupToggles();
  }

  private renderLayout() {
    this.container.innerHTML = `
      <div class="h-14 bg-[#111118] border-b border-gray-800 flex items-center px-6 justify-between">
        <div class="flex items-center gap-4">
          <span class="text-3xl">🇮🇳</span>
          <div>
            <h1 class="text-2xl font-bold tracking-tighter">IRIS</h1>
            <p class="text-xs text-emerald-400">LIVE • NATIONAL INTELLIGENCE DASHBOARD</p>
          </div>
        </div>
        <div class="text-sm text-gray-400">Live</div>
      </div>

      <div class="flex flex-1 overflow-hidden">
        <div class="w-72 bg-[#111118] border-r border-gray-800 p-6">
          <h2 class="uppercase text-xs text-gray-500 mb-6">DATA LAYERS</h2>

          <label class="flex items-center gap-3 p-3 cursor-pointer">
            <input id="toggle-conflict" type="checkbox" checked />
            🔴 Conflict Zones
          </label>
        </div>

        <div id="map-container" class="flex-1"></div>

        <div class="w-96 bg-[#111118] border-l border-gray-800 p-6">
          <h2 class="text-lg mb-4">National AI Brief</h2>
          <div id="national-brief">Connecting...</div>

          <h2 class="text-lg mt-6 mb-4">Risk Index</h2>
          <div id="risk-score">—</div>
          <div id="risk-status"></div>
        </div>
      </div>
    `;
  }

  private async loadBackendData() {
    try {
      const analyzeRes = await fetch('http://localhost:8000/api/analyze');
      const analysis = await analyzeRes.json();

      (document.getElementById('national-brief') as HTMLElement).textContent =
        analysis.national_brief;

      (document.getElementById('risk-score') as HTMLElement).textContent =
        analysis.risk_index;

      (document.getElementById('risk-status') as HTMLElement).textContent =
        analysis.top_drivers?.[0];
    } catch {
      console.log("Backend error");
    }
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
      // 🔹 Load GeoJSON
      const geoRes = await fetch('/india_state_geo.json');
      const geojson = await geoRes.json();

      // 🔹 Risk mapping
      const riskData: Record<string, number> = {
        "Maharashtra": 80,
        "Karnataka": 50,
        "Gujarat": 30,
        "Tamil Nadu": 60,
        "Delhi": 70,
        "Rajasthan": 40
      };

      geojson.features.forEach((f: any) => {
        f.properties.risk = riskData[f.properties.NAME_1] ?? 10;
      });

      // 🔹 Add source
      this.map!.addSource('india-states', {
        type: 'geojson',
        data: geojson
      });

      // 🔹 Heatmap
      this.map!.addLayer({
        id: 'states-fill',
        type: 'fill',
        source: 'india-states',
        paint: {
          'fill-color': [
            'interpolate',
            ['linear'],
            ['get', 'risk'],
            0, '#00ff00',
            50, '#ffff00',
            100, '#ff0000'
          ],
          'fill-opacity': 0.6
        }
      });

      // 🔹 Borders
      this.map!.addLayer({
        id: 'states-outline',
        type: 'line',
        source: 'india-states',
        paint: {
          'line-color': '#fff',
          'line-width': 1.2
        }
      });

      // 🔹 Click popup
      this.map!.on('click', 'states-fill', (e: any) => {
        const f = e.features[0];

        new maplibregl.Popup()
          .setLngLat(e.lngLat)
          .setHTML(`<b>${f.properties.NAME_1}</b><br/>Risk: ${f.properties.risk}`)
          .addTo(this.map!);
      });

      // 🔹 Cursor
      this.map!.on('mouseenter', 'states-fill', () => {
        this.map!.getCanvas().style.cursor = 'pointer';
      });
      this.map!.on('mouseleave', 'states-fill', () => {
        this.map!.getCanvas().style.cursor = '';
      });

      // 🔹 Fetch markers
      const apiRes = await fetch('http://localhost:8000/api/data');
      const data = await apiRes.json();

      const zones = data.conflict?.risk_zones || [];

      this.conflictMarkers = [];

      zones.forEach((z: any) => {
        const marker = new maplibregl.Marker({
          color: z.risk > 70 ? 'red' : z.risk > 50 ? 'orange' : 'green'
        })
          .setLngLat([z.lon, z.lat])
          .setPopup(new maplibregl.Popup().setHTML(`<b>${z.name}</b><br/>Risk: ${z.risk}`))
          .addTo(this.map!);

        this.conflictMarkers.push(marker);
      });
    });
  }

  private setupToggles() {
    const toggle = document.getElementById('toggle-conflict') as HTMLInputElement;

    toggle.addEventListener('change', () => {
      if (toggle.checked) {
        this.conflictMarkers.forEach(m => m.addTo(this.map!));
      } else {
        this.conflictMarkers.forEach(m => m.remove());
      }
    });
  }
}