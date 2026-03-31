# Backend Manual APIs TODO (from PRD.md)

## Implemented ✅

- `GET /api/health` - Status check
- `GET /api/data` - Full aggregate (news/weather/finance/ports/conflict/infra/traffic)
- `POST /api/analyze` - Groq stub (brief/risk/forecasts/correlation)

## Phase 2: AI/ML (Member 3 - High Priority)

- [ ] **Integrate Groq in `/api/analyze`**:
  - System prompt: "Analyze IndiaMonitor data. Output JSON: {national_brief (2 sentences), risk_index (0-100), top_drivers [3], forecasts [3 strings], correlation (e.g. monsoon×ports)}"
  - Input: Full /api/data JSON
  - Test: POST {"data": "/api/data response"} → structured AI output
  - Env: GROQ_API_KEY

## Phase 3: Polish/Stretch (All - Medium)

- [ ] **`/api/cached-data`** (GET): In-memory cache /api/data (TTL 60s) for frontend auto-refresh
  - Use `fastapi-cache` or simple dict
- [ ] **Layer Endpoints** (if frontend optimize):
  - `GET /api/layers/ports` - ports only
  - `GET /api/layers/weather` - cities only
- [ ] **`/api/alerts`** (GET): Filtered high-risk items (congestion>70, deficit>8, conflict alert)

## Stretch Features

- [ ] `POST /api/chat {"query": "Impact of monsoon on markets?"}` - Groq conversational
- [ ] `GET /api/trends?entity=nifty` - Simple time-series (yfinance history)

## Deployment TODO

- [ ] Render: Add rate-limit middleware
- [ ] Error logging (structlog)

**Priority: Groq /api/analyze → Deploy → Polish.**

Current /api/data covers 100% PRD data MVP.
