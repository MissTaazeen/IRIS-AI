**Product Requirements Document (PRD)**  
**Project:** IndiaMonitor.app  
**Version:** 1.0 – 10-Hour Hackathon MVP  
**Track:** AI/ML  
**Date:** 31 March 2026  
**Team:** 3 members  
**Deployment Target:** Render (FastAPI backend + Vite static frontend)  
**Core Constraint:** 100% APIs + realistic dummy JSON (no web scraping)

### 1. Problem Statement
In today’s dynamic India, critical real-time information about weather & monsoons, stock markets, major ports & shipping, power infrastructure, urban traffic, border/security signals, and national/regional news is fragmented across multiple official and public APIs. Decision-makers, businesses, journalists, supply-chain teams, and citizens lack a single unified, intelligent platform that aggregates, visualizes, and correlates this data with actionable AI insights.

**IndiaMonitor** solves this by creating an **India-specific real-time national intelligence dashboard** modeled directly after WorldMonitor.app. It pulls live data exclusively from free public APIs, supplements gaps with realistic dummy data, displays everything on an interactive layered India map, and leverages Groq AI to generate concise national briefs, composite risk indices (0–100), probabilistic forecasts, and cross-stream correlations (e.g., “Monsoon impact on JNPT port + market volatility = 68% logistics risk”).

### 2. Product Vision
Build a beautiful, dark-themed, professional-grade situational-awareness dashboard that feels and functions like WorldMonitor.app but is purpose-built for India. The MVP must be fully functional, visually impressive, and demo-ready within 10 hours, showcasing strong API integration and AI/ML synthesis while remaining reliable and judge-friendly.

### 3. Objectives & Success Criteria
- Deliver a polished, live-feeling dashboard with real API data + realistic dummies.
- Strong AI/ML showcase: Groq-powered national briefs, risk scoring, forecasts, and correlations.
- Mirror WorldMonitor’s core UX: interactive map with layers, AI brief panel, finance radar, news feed, alerts.
- Complete deployment on Render with auto-refresh for “real-time” feel.
- Impress judges with one compelling India-specific example (e.g., monsoon + port + market correlation during March 2026 conditions).

### 4. Target Users (for Hackathon Demo)
- Hackathon judges
- Supply chain / logistics analysts
- Journalists and researchers
- Disaster management / government officials (hypothetical)
- General citizens tracking monsoons, markets, and security

### 5. Key Features (MVP – Must-Have in 10 Hours)

| Priority | Feature | Description | Data Source |
|----------|---------|-------------|-------------|
| 1 | National AI Brief + Composite Risk Index | 2–3 sentence urgent summary + overall India risk score (0–100) with top 3 drivers | Aggregated data + Groq |
| 2 | Interactive India Map | Full-screen map with state boundaries colored by risk, toggleable layers (ports, weather, conflict, traffic) | MapLibre GL or Leaflet + public India GeoJSON |
| 3 | Live News Feed | Top India headlines with source, time, and short AI-highlight summary | NewsAPI.org (`country=in`) or GNews.io |
| 4 | Finance Radar | Nifty 50, Sensex, top 8 stocks (.NS), key commodities (gold, crude oil) with price movement | yfinance library |
| 5 | Ports & Maritime Monitor | Status, congestion level, and delay estimates for major ports (JNPT, Mumbai, Chennai, Paradip, etc.) | Realistic dummy JSON |
| 6 | Weather & Disaster Layer | Current conditions + short-term monsoon/heat alerts for key cities | Open-Meteo API (no key required) |
| 7 | Conflict / Security Zones | Highlighted zones (LoC/LAC, Naxal areas, Northeast) with risk signals | Realistic dummy JSON |
| 8 | Alerts Panel + Forecasts | Color-coded alerts + 3 probabilistic forecasts for next 24 hours | Groq synthesis |
| 9 | Cross-Stream Correlation | At least one highlighted insight card linking sectors | Groq |

**Stretch Features (if time allows after core MVP):**
- “Ask IndiaMonitor” natural language chat box
- Power outage / traffic hotspot overlays
- Voice input using browser SpeechRecognition
- Mini trend charts for stocks/weather

### 6. User Interface & Experience Requirements
- **Theme:** Dark mode only (black/gray base with red/yellow/green risk accents) – exact WorldMonitor aesthetic.
- **Layout:**
  - Top bar: Logo “IndiaMonitor”, pulsing LIVE indicator, current timestamp, refresh button.
  - Left sidebar: Navigation (Brief, Map Layers, Finance, Ports, News, Alerts).
  - Center: Full-screen interactive map (India-centered, zoomable, layer toggles).
  - Right panel: National AI Brief, Composite Risk Index, Forecasts.
  - Bottom drawer/panel: News feed cards + Finance radar cards.
- **Interactions:** Clickable map elements (show details on hover/click), auto-refresh every 45–60 seconds, smooth loading states.
- **Accessibility & Polish:** Responsive (desktop-first), clean cards, emoji usage, professional urgent tone in AI text.

### 7. Technical Architecture
- **Frontend:** Vanilla TypeScript + Vite + MapLibre GL (preferred for performance) or Leaflet. Use TailwindCSS for rapid dark styling. Axios for API calls.
- **Backend:** FastAPI (Python) with a single aggregator endpoint `GET /api/data` and `POST /api/analyze` for Groq.
- **AI/ML:** Groq API (Llama 3.3 or equivalent) – one powerful system prompt that consumes the full data JSON and outputs structured markdown (brief, risk score, forecasts, correlation).
- **Data Flow:** Frontend calls backend → backend fetches live APIs + loads dummy JSON → returns unified object → Groq analyzes → frontend renders.
- **Caching:** Simple in-memory cache in FastAPI (or Redis on Render) for stability during demo.
- **Deployment:**
  - Backend: Render Web Service (FastAPI + Uvicorn).
  - Frontend: Render Static Site (Vite build) or Vercel.
- **Real-time Simulation:** Auto-polling + timestamp display.

### 8. Data Sources (Strictly APIs + Dummy)
**Live APIs (free tiers):**
- News: NewsAPI.org (`country=in`) or GNews.io
- Weather: Open-Meteo (`api.open-meteo.com`) – supports Mumbai (19.0760, 72.8777), Delhi, etc.
- Stocks/Finance: yfinance (`^NSEI`, `^BSESN`, `RELIANCE.NS`, etc.)

**Dummy but Realistic JSON (pre-loaded files):**
- Ports: Status, congestion, delay hours, reason (monsoon-inspired)
- Conflict/Security: Zone name, risk level, short description
- Infrastructure/Traffic: Hotspots with reasons and impact

All dummy data must feel current for March 2026 (monsoon season context where relevant).

### 9. Non-Functional Requirements
- Initial load time < 5 seconds.
- Graceful fallback if any API fails (use cached/dummy data).
- Clean, maintainable code with clear folder structure.
- Fully working end-to-end demo (map + AI brief + at least one correlation).
- 60-second Loom demo video ready by end of hackathon.
- README with architecture diagram, API endpoints, and setup instructions.

### 10. 10-Hour Build Plan Overview (for 3-Person Team)
- **0–40 mins:** Project setup (repo, FastAPI, Vite, GeoJSON).
- **40 mins–2.5 hrs:** Backend data providers + aggregator (Member 1).
- **Parallel:** Map + basic UI layout (Member 2).
- **2.5–5 hrs:** Groq AI integration + synthesis endpoint (Member 3).
- **5–8 hrs:** Full frontend integration, panels, layers, polish.
- **8–10 hrs:** Testing, Render deployment, demo video, submission.

This PRD ensures the project stays tightly scoped, technically strong, visually impressive, and fully aligned with hackathon constraints while delivering a high-quality India-specific intelligence dashboard.

Would you like me to expand any section, add user stories, wireframe descriptions, or provide the detailed team task breakdown next?