# IndiaMonitor.app 

India's WorldMonitor: LIVE risk dashboard with AI briefs, map layers, risk index (monsoon 2026 scenario).

**Demo:** Backend: http://localhost:8000/docs | Frontend: [Member 2] | Render: [TBD]

## Team

| Role         | Member   |
| ------------ | -------- |
| Backend/Data | Member 1 |
| Frontend/Map | Member 2 |
| AI/Deploy    | Member 3 |

## Quick Start

1. Backend (`backend/`)
2. Frontend (`frontend/`) `npm install && npm run dev`
3. `.env`: NEWS_API_KEY, GROQ_API_KEY
4. Enjoy LIVE data + AI!

## Architecture

```
IndiaMonitor.app
├── backend/ (FastAPI) ── /api/data ── NewsAPI + OpenMeteo + yfinance + Dummies (ports/conflict/infra/traffic)
│   └── /api/analyze ── Groq AI (brief/risk/forecasts)
└── frontend/ (Vite/TS/MapLibre) ── axios ── Dark UI, India map layers, panels
```

**Public APIs only + Dummies for realism.**

## Deploy (Render)

- Backend: Web Service
- Frontend: Static Site

## Status

- Backend ✅ LIVE
- Frontend ⏳ Member 2
- AI/Deploy ⏳ Member 3

**10hr Hackathon: Ship fast, win big! 🔥**
