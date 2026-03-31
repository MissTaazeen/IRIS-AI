# Backend Architecture

## High-Level

```
Frontend (Member 2) ── axios ── /api/data ── FastAPI ── Providers ── Public APIs / Dummies
                           │
                           └── /api/analyze ── Groq (Member 3)
```

## Layers

1. **FastAPI App** (`main.py`):
   - CORS middleware (frontend \*)
   - `/api/data`: Async-ready aggregator
   - Pydantic models, error handling/fallbacks
2. **Data Providers** (`data_providers/`):
   | Provider | Source | Output |
   |----------|--------|--------|
   | news.py | NewsAPI | Top 10 IN headlines |
   | weather.py | Open-Meteo | 5 cities current/hourly |
   | finance.py | yfinance | Indices/stocks/commodities Δ |
   | dummy_ports.py | JSON | 17 ports congestion (85% JNPT) |
   | dummy_conflict.py | JSON | LoC/LAC/Naxal + geo zones |
   | dummy_infra.py | JSON | Power deficit (8% avg), water |
   | dummy_traffic.py | JSON | Cities road/rail delays (52min Bengaluru) |
3. **Error Resilience:** API fail → dummy/static.
4. **Scalability:** Stateless, Render-ready.
5. **Extensibility:** Add providers to `/api/data` loop.

## Data Flow (/api/data)

```
timestamp = now()
data = {
  news: get_news(),
  weather: get_weather(),
  ...
}
return data
```

## Dependencies

```
fastapi + uvicorn
requests, yfinance, groq (stub)
python-dotenv, pydantic
```

**Monsoon Theme:** Dummies simulate March 2026 disruptions (floods, congestion).

Ready for production! 🚀
