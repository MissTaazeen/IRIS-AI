# Backend Architecture Doc

## Overview

FastAPI microservice aggregating India-specific data for risk monitoring dashboard. Public APIs + dummy datasets for hackathon demo.

## Components

```
┌─────────────────┐     ┌──────────────────┐
│   FastAPI App   │◄─── │   /api/data      │
│  (main.py)      │     │  Aggregator      │
├─────────────────┤     └──────────────────┘
│  Endpoints:     │
│  /health        │     ┌──────────────────┐
│  /data ────▶   ─┼───▶ │ Data Providers   │
│  /analyze (stub)│     ├──────────────────┤
└─────────────────┘     │ news.py (NewsAPI)│
                         │ weather.py (Open-Meteo)
                         │ finance.py (yfinance)
                         │ dummies: ports/conflict/infra/traffic
                         └──────────────────┘
                                 │
                                 ▼
                         Public APIs / JSON
```

## Endpoints Detail

| Endpoint     | Method             | Response                                                           | Latency Target |
| ------------ | ------------------ | ------------------------------------------------------------------ | -------------- |
| /api/health  | GET                | `{"status": "ok"}`                                                 | <50ms          |
| /api/data    | GET                | Aggregate JSON (news/weather/finance/ports/conflict/infra/traffic) | <2s            |
| /api/analyze | POST `{data: str}` | `{"risk_index": 68, "brief": "..."}`                               | <3s (Groq)     |

## Data Providers

| File              | Source               | Fallback  | Notes                                |
| ----------------- | -------------------- | --------- | ------------------------------------ |
| news.py           | NewsAPI `country=in` | []        | Top 10 headlines                     |
| weather.py        | Open-Meteo           | Error msg | 5 cities current + precip prob       |
| finance.py        | yfinance             | {}        | Nifty/Sensex/8 stocks/gold/oil Δ%    |
| dummy_ports.py    | JSON                 | Static    | 17 ports, avg congestion 60% monsoon |
| dummy_conflict.py | JSON                 | Static    | LoC/Naxal geo-risk                   |
| dummy_infra.py    | JSON                 | Static    | Power deficit 8% avg                 |
| dummy_traffic.py  | JSON                 | Static    | City delays 40min avg                |

## Tech Stack

- **Framework:** FastAPI (async, Pydantic validation)
- **Server:** uvicorn[standard] + watchfiles reload
- **Middleware:** CORS (\*)
- **Libs:** requests, yfinance, python-dotenv, groq (stub)
- **Env:** Python 3.12 venv

## Deployment

```
Render Web Service:
Build: pip install -r requirements.txt
Start: uvicorn main:app --host 0.0.0.0 --port $PORT
Env Vars: NEWS_API_KEY, GROQ_API_KEY
```

## Error Handling

- API timeout 10s → fallback dict with 'error'
- Graceful degradation for demo reliability.

## Scalability Notes

- Stateless
- Cache /api/data (Redis Phase 3?)
- Async providers for prod

**Hackathon Ready: 100% uptime with dummies.**
