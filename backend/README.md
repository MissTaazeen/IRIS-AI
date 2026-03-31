# IndiaMonitor Backend (Member 1)

## Overview

FastAPI server for IndiaMonitor.app hackathon. Aggregates public APIs + realistic dummy data for monsoon 2026 scenario. Endpoints serve JSON for frontend map/UI/AI briefs.

**Live Docs:** http://localhost:8000/docs (Swagger)

## Setup

1. Copy `.env.example` → `.env`:
   ```
   NEWS_API_KEY=your_newsapi.org_key
   GROQ_API_KEY=your_groq_key
   ```
2. ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --reload --port 8000
   ```

## Endpoints

- `GET /api/health` → Server status
- `GET /api/data` → Aggregate: {news, weather (5 cities), finance (Nifty/Sensex/stocks/gold/oil), ports (17), conflict, infra (power/water), traffic}
- `POST /api/analyze {data: str}` → AI stub (Groq-ready: brief, risk_index 0-100, forecasts, correlation)

**Example /api/data:**

```json
{
  "timestamp": "...",
  "news": {"headlines": [...]},
  "weather": {"cities": {"Mumbai": {"temp": 28.5, "precip": 0.2}}},
  "finance": {"indices": {"Nifty 50": {"price": 24567.89, "change_pct": -0.45}}},
  "ports": {"national_avg_congestion": 60.2, "critical_ports": ["JNPT", "Mumbai Port"]}
}
```

## Data Sources

- **News:** NewsAPI.org (India headlines)
- **Weather:** Open-Meteo (Mumbai/Delhi/Bengaluru/Chennai/Hyderabad)
- **Finance:** yfinance (Nifty '^NSEI', Sensex '^BSESN', top 8 .NS, GC=F oil)
- **Dummies (monsoon 2026):** Ports (congestion), Conflict (LoC/Naxal), Infra (power deficit), Traffic (cities delays)

## Deploy (Render)

- Web Service
- Build: `pip install -r requirements.txt`
- Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Env: NEWS_API_KEY, GROQ_API_KEY

## Architecture

See `ARCHITECTURE.md`.

**Team Sync: Phase 1 complete. Ready for frontend/AI integration.**
