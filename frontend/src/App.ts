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
    this.loadBackendData();        // ← Integration
  }

  private renderLayout() {
    this.container.innerHTML = `
      <div class="h-14 bg-[#111118] border-b border-gray-800 flex items-center px-6 justify-between">
        <div class="flex items-center gap-4">
          <span class="text-3xl">🇮🇳</span>
          <div>
            <h1 class="text-2xl font-bold tracking-tighter">IRIS</h1>
            <p class="text-xs text-emerald-400 flex items-center gap-1.5">
              <span class="relative flex h-2 w-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
              </span>
              LIVE • NATIONAL INTELLIGENCE DASHBOARD
            </p>
          </div>
        </div>
        <div class="text-sm text-gray-400">31 March 2026 • 14:XX IST</div>
      </div>

      <div class="flex flex-1 overflow-hidden">
        <!-- Left Sidebar -->
        <div class="w-72 bg-[#111118] border-r border-gray-800 p-6 flex flex-col">
          <h2 class="uppercase text-xs tracking-widest text-gray-500 mb-6">DATA LAYERS</h2>
          <div class="space-y-3 text-sm">
            <label class="flex items-center gap-3 p-3 hover:bg-gray-900 rounded-2xl cursor-pointer">
              <input type="checkbox" checked class="accent-emerald-500" /> 🌧️ Weather & Monsoon
            </label>
            <label class="flex items-center gap-3 p-3 hover:bg-gray-900 rounded-2xl cursor-pointer">
              <input type="checkbox" checked class="accent-emerald-500" /> ⚓ Major Ports
            </label>
            <label class="flex items-center gap-3 p-3 hover:bg-gray-900 rounded-2xl cursor-pointer">
              <input type="checkbox" class="accent-emerald-500" /> 🔴 Conflict Zones
            </label>
            <label class="flex items-center gap-3 p-3 hover:bg-gray-900 rounded-2xl cursor-pointer">
              <input type="checkbox" class="accent-emerald-500" /> 📈 Finance Radar
            </label>
          </div>
        </div>

        <!-- Map -->
        <div id="map-container" class="flex-1 relative"></div>

        <!-- Right Panel -->
        <div class="w-96 bg-[#111118] border-l border-gray-800 p-6 overflow-y-auto">
          <h2 class="text-lg font-semibold mb-4">National AI Brief</h2>
          <div id="national-brief" class="text-sm leading-relaxed text-gray-300 mb-8 min-h-[140px]">
            Connecting to backend...
          </div>

          <h2 class="text-lg font-semibold mb-4">National Risk Index</h2>
          <div class="flex items-baseline gap-3 mb-8">
            <div id="risk-score" class="text-7xl font-bold text-orange-400">—</div>
            <div class="mb-1">
              <p class="text-xs text-gray-400">OUT OF 100</p>
              <p id="risk-status" class="text-orange-400 text-sm"></p>
            </div>
          </div>

          <div id="extra-analysis" class="text-sm space-y-6 hidden">
            <div>
              <h3 class="text-md font-semibold text-gray-200">Top Drivers</h3>
              <ul id="top-drivers" class="list-disc pl-4 mt-2 text-gray-400 space-y-1"></ul>
            </div>
            <div>
              <h3 class="text-md font-semibold text-gray-200">Forecasts</h3>
              <ul id="forecasts" class="list-disc pl-4 mt-2 text-gray-400 space-y-1"></ul>
            </div>
            <div>
              <h3 class="text-sm font-semibold text-yellow-500 uppercase tracking-wider mb-2">Key Correlation</h3>
              <p id="correlation" class="text-gray-300 bg-gray-900 p-4 rounded-xl border border-gray-700 leading-relaxed"></p>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  private async loadBackendData() {
    const briefEl = document.getElementById('national-brief') as HTMLElement;
    const riskScoreEl = document.getElementById('risk-score') as HTMLElement;
    const riskStatusEl = document.getElementById('risk-status') as HTMLElement;

    try {
      // Step 1: Get raw data
      const dataRes = await fetch('http://localhost:8000/api/data');
      if (!dataRes.ok) throw new Error(`Data fetch failed: ${dataRes.status}`);
      const rawData = await dataRes.json();

      // Step 2: Get AI analysis
      const analyzeRes = await fetch('http://localhost:8000/api/analyze');

      if (!analyzeRes.ok) throw new Error(`Analyze failed: ${analyzeRes.status}`);

      const analysis = await analyzeRes.json();

      // Update UI
      briefEl.textContent = analysis.national_brief || "Brief not available yet";
      
      const riskIndex = analysis.risk_index || 68;
      riskScoreEl.textContent = riskIndex.toString();
      
      // Update color based on score
      let colorClass = 'text-emerald-500';
      let riskStatus = 'Low Risk';
      if (riskIndex >= 70) {
        colorClass = 'text-red-500';
        riskStatus = 'High Risk';
      } else if (riskIndex >= 40) {
        colorClass = 'text-orange-400';
        riskStatus = 'Moderate Risk';
      }
      
      riskScoreEl.className = `text-7xl font-bold ${colorClass}`;
      riskStatusEl.className = `text-sm ${colorClass}`;
      riskStatusEl.textContent = riskStatus;

      const extraAnalysisEl = document.getElementById('extra-analysis');
      const topDriversEl = document.getElementById('top-drivers');
      const forecastsEl = document.getElementById('forecasts');
      const correlationEl = document.getElementById('correlation');

      if (extraAnalysisEl && topDriversEl && forecastsEl && correlationEl) {
        extraAnalysisEl.classList.remove('hidden');
        if (analysis.top_drivers) {
          topDriversEl.innerHTML = analysis.top_drivers.map((d: string) => `<li>${d}</li>`).join('');
        }
        if (analysis.forecasts) {
          forecastsEl.innerHTML = analysis.forecasts.map((f: string) => `<li>${f}</li>`).join('');
        }
        if (analysis.correlation) {
          correlationEl.textContent = analysis.correlation;
        }
      }

      console.log("✅ Backend data loaded successfully", analysis);

    } catch (error: any) {
      console.error("Backend error:", error);
      briefEl.innerHTML = `
        <span class="text-red-400">
          Cannot connect to backend.<br>
          Make sure Member 1 has started the backend on port 8000 with CORS enabled.
        </span>`;
    }
  }

  private initializeMap() {
    const mapContainer = document.getElementById('map-container') as HTMLElement;

    this.map = new maplibregl.Map({
      container: mapContainer,
      style: 'https://demotiles.maplibre.org/style.json',
      center: [78.96, 20.59],
      zoom: 4.4,
    });

    this.map.addControl(new maplibregl.NavigationControl(), 'top-right');

    this.map.on('load', () => {
      console.log('✅ Map ready for GeoJSON layers');
    });
  }
}