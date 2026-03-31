# IndiaMonitor.app – 10-Hour Hackathon Task File
**Team of 3 | AI/ML Track | Goal: Build WorldMonitor.app but for entire India**

**Date:** 31 March 2026  
**Time Window:** 12:00 PM IST – 10:00 PM IST (10 hours)  
**Constraints:**  
- Use **only public APIs** (no web scraping)  
- Use **realistic dummy JSON** for ports, conflict, power, traffic  
- Deploy on **Render** (Backend as Web Service + Frontend as Static Site)  
- Mirror WorldMonitor.app look & feel as closely as possible (dark theme, LIVE badge, layered map, AI briefs, risk index, correlations)

## Team Roles & Responsibilities

| Role                          | Member     | Primary Responsibilities |
|-------------------------------|------------|---------------------------|
| **Backend & Data Engineer**   | Member 1   | FastAPI server, API integrations, dummy data, aggregator endpoint |
| **Frontend & Visualization**  | Member 2   | Vite + TypeScript UI, MapLibre GL / Leaflet map, dark theme, panels |
| **AI/ML + Deployment Lead**   | Member 3   | Groq integration, AI synthesis, full integration, Render deployment, demo video |

**Communication:** Sync every 2 hours (12:00, 14:00, 16:00, 18:00, 20:00) on Discord/WhatsApp.

---

## Phase 0: Project Setup (12:00 – 12:40 PM | All 3 together – 40 mins)

**All Members:**
1. Create a private GitHub repo named `indiamonitor-hackathon`
2. Clone the repo
3. Share the repo link in group chat
4. Install prerequisites:
   - Node.js 20+
   - Python 3.11+
   - Git
5. Get API keys (do this immediately):
   - Groq API key[](https://console.groq.com)
   - NewsAPI.org key[](https://newsapi.org) → set `country=in`
   - (Optional) OpenWeatherMap key (free tier)

**Member 1 – Backend Setup**
- Create folder structure:
indiamonitor/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── data_providers/
│   │   ├── init.py
│   │   ├── news.py
│   │   ├── weather.py
│   │   ├── finance.py
│   │   ├── dummy_ports.py
│   │   ├── dummy_conflict.py
│   │   ├── dummy_infra.py
│   │   └── dummy_traffic.py
│   └── .env
└── frontend/          ← (will be created by Member 2)

- Add to `requirements.txt`:
fastapi
uvicorn[standard]
requests
python-dotenv
pydantic
groq


**Member 2 – Frontend Setup**
- Run: `npm create vite@latest frontend -- --template vanilla-ts`
- Inside `frontend/`:
- Install: `npm install maplibre-gl axios tailwindcss postcss autoprefixer`
- Initialize Tailwind
- Add India GeoJSON to `frontend/public/india.geojson` (download from public repo or use simple one)

**Member 3 – Shared Setup**
- Create `.env.example` with:
GROQ_API_KEY=your_key
NEWS_API_KEY=your_key

- Commit initial skeleton and push.

---

## Phase 1: Data Layer (12:40 – 14:30 PM | Member 1 Lead)

**Member 1 Tasks:**
- Implement these files in `backend/data_providers/`:
1. `news.py` → Call NewsAPI.org (`country=in`)
2. `weather.py` → Use Open-Meteo API (cities: Mumbai, Delhi, Bengaluru, Chennai, Hyderabad)
3. `finance.py` → Use yfinance for Nifty, Sensex, top 8 stocks (.NS), gold & oil
4. Create realistic dummy JSON files (ports, conflict, infra, traffic) – use real-inspired data for March 2026 monsoon season
5. Create `main.py` with:
   - `GET /api/data` → aggregates everything
   - `GET /api/health` → simple health check
- Run backend locally: `uvicorn main:app --reload --port 8000`

**Member 2 & 3:** Continue with frontend map setup and AI prompt drafting in parallel.

---

## Phase 2: AI Synthesis & Map (14:30 – 16:30 PM)

**Member 3 (AI Lead) Tasks:**
- Create `/api/analyze` endpoint in `main.py`
- Write strong Groq system prompt (WorldMonitor style):
- National Brief (2 sentences)
- Composite Risk Index (0-100) + top 3 drivers
- 3 probabilistic forecasts (next 24h)
- 1 key cross-correlation (e.g., monsoon × ports × markets)
- Test the endpoint with sample data.

**Member 2 (Frontend) Tasks:**
- Set up MapLibre GL or Leaflet with India-centered map
- Load `india.geojson` and color states by risk level
- Add layer toggles (Weather, Ports, Conflict, Traffic)
- Create basic UI skeleton: top bar (LIVE badge), sidebar, right panel, bottom news/finance area

---

## Phase 3: Integration & Polish (16:30 – 19:00 PM)

**All Members:**
- Member 2: Connect frontend to backend APIs using axios (fetch `/api/data` and `/api/analyze`)
- Member 3: Display AI-generated brief, risk index, forecasts, and correlation card
- Member 1: Add CORS middleware, error handling, and auto-refresh logic (every 60 seconds)
- Apply dark theme consistently (WorldMonitor aesthetic: dark background, red/yellow/green risk colors)
- Add pulsing "LIVE" indicator

**Stretch Goals (if ahead of time):**
- Simple chat interface ("Ask IndiaMonitor")
- Voice input using browser SpeechRecognition

---

## Phase 4: Deployment & Demo (19:00 – 22:00 PM | Member 3 Lead)

**Member 3 Tasks:**
1. Deploy **Backend** to Render as Web Service:
 - Connect GitHub repo
 - Set Build Command: `pip install -r requirements.txt`
 - Set Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
 - Add environment variables from `.env`
2. Deploy **Frontend** to Render as Static Site:
 - Build Command: `npm run build`
 - Output Directory: `frontend/dist`
3. Update frontend API base URL to point to deployed backend
4. Test full flow on live URLs

**All Members:**
- Record 60-second demo video (Loom):
- Show map with layers
- Show live AI National Brief
- Show risk index and correlation example
- Show auto-refresh
- Prepare short README.md with:
- Problem statement
- Tech stack
- API sources used
- Live Render links

---

## Dummy Data Guidelines (Member 1)

Create realistic JSON in `backend/data_providers/`:
- **Ports**: JNPT high congestion due to monsoon, Mumbai Port, Chennai, etc.
- **Conflict**: LoC tension, LAC activity, Naxal areas
- **Infra**: Power demand vs supply in major states
- **Traffic**: Mumbai local train + road delays, Delhi hotspots

Make data feel current (monsoon season in March 2026).

## Success Criteria for 10:00 PM
- Working backend on Render returning real + dummy data
- Beautiful dark frontend with interactive India map
- Groq-powered AI briefs, risk score, forecasts, and correlations
- Auto-refresh working
- 60-second demo video ready
- Submission link prepared

## Emergency Fallbacks
- If any API fails → fallback to dummy data instantly
- If MapLibre is slow → switch to Leaflet
- If time is short → prioritize: Map + AI Brief + Risk Index + Finance + News

**Let's ship a strong winner!**  
Start at 12:00 PM sharp.  
First sync at 14:00 PM – share screenshots of working backend and map.

Good luck Team! 🔥
