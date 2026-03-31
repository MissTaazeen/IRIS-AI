# IndiaMonitor.app 

**Real-time AI-Powered National Intelligence Dashboard for India**  
_Mirroring WorldMonitor.app – Built in a 10-hour AI/ML Hackathon_

[![IRIS-AI Demo](https://via.placeholder.com/1200x600/1a1a2e/00ff9d?text=IRIS-AI+Dashboard+Screenshot)](https://iris-ai-demo.render.com)  
_(Replace with actual screenshot or live demo link once deployed)_

## 🚀 Quick Start

```bash
# Terminal 1: Backend
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Terminal 2: Frontend
cd frontend
npm install
npm run dev
```

- Backend: http://localhost:8000/docs (Swagger UI)
- Frontend: http://localhost:5173 (Vite dev server)
- API calls auto-CORS enabled.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Running Locally](#running-locally)
- [API Reference](#api-reference)
- [Adding Features](#adding-features)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

## Overview

**IRIS-AI** is a real-time situational awareness platform for India. It aggregates **live public APIs** (news, weather, finance) with **realistic dummy data** (ports, conflict, infrastructure, traffic – monsoon 2026 scenario) and leverages **Groq AI** for:

- National intelligence briefs
- Composite risk index (0–100)
- Probabilistic forecasts
- Cross-domain correlations

Built to mirror [WorldMonitor.app](https://worldmonitor.app/) with a professional dark theme, interactive map, and LIVE data feeds.

**Current Status**: Phase 0 (scaffolding) complete. Backend data aggregation live. Frontend skeleton ready. Next: Groq integration + map.

## ✨ Features

- **Interactive India Map**: State risk coloring + toggle layers (weather, ports, conflict, traffic)
- **National AI Brief**: Groq-powered 2–3 sentence summary
- **Composite Risk Index**: 0–100 score + top drivers
- **Live Feeds**:
  - News (NewsAPI.org – India headlines)
  - Finance (Nifty/Sensex/top stocks/gold/oil via yfinance)
  - Weather (5 major cities via Open-Meteo)
- **Dummy Realism**: Ports congestion (e.g., JNPT 85%), LoC tensions, power deficits
- **AI Outputs**: 24/48/72h forecasts, correlations (e.g., monsoon × ports = logistics risk)
- **Auto-Refresh**: 60s updates
- **Dark Theme**: WorldMonitor-inspired UI

## 🛠️ Tech Stack

| Layer          | Technologies                                                 |
| -------------- | ------------------------------------------------------------ |
| **Backend**    | FastAPI, Python 3.11, Uvicorn, Pydantic, Groq, python-dotenv |
| **Frontend**   | Vite, TypeScript, TailwindCSS (dark), MapLibre GL, Axios     |
| **Data**       | NewsAPI, Open-Meteo, yfinance + custom dummies               |
| **Deployment** | Render (Web Service + Static Site)                           |

## 📁 Project Structure

```
IRIS-AI/
├── backend/
│   ├── main.py                 # FastAPI app
│   ├── requirements.txt        # Python deps
│   ├── data_providers/         # News, weather, finance, dummies
│   └── .env                    # API keys
├── frontend/
│   ├── src/                    # TS components (App.tsx incoming)
│   ├── package.json            # npm deps
│   ├── tailwind.config.js      # Dark theme
│   └── public/india.geojson    # Map data
├── README.md                   # This file!
├── TODO.md                     # Progress tracker
└── PRD.md                      # Full spec
```

## 🏃‍♂️ Running Locally

### Prerequisites

- Python 3.11+
- Node.js 20+
- API Keys: [NewsAPI](https://newsapi.org), [Groq](https://console.groq.com)

### 1. Clone & Setup

```bash
git clone <repo> IRIS-AI
cd IRIS-AI
```

### 2. Backend

```bash
cd backend
cp .env.example .env  # Add your NEWS_API_KEY, GROQ_API_KEY
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Test**: `curl http://localhost:8000/api/health` → `{"status":"ok"}`

### 3. Frontend

```bash
cd ../frontend
npm install
npm run dev
```

**Test**: Open http://localhost:5173

### 4. Verify

- Backend docs: http://localhost:8000/docs
- Full data: http://localhost:8000/api/data
- AI stub: POST http://localhost:8000/api/analyze `{"data":"sample"}`

**Troubleshooting**:

- CORS issues? Restart backend.
- Map blank? Check `public/india.geojson`.
- No data? Verify API keys in `.env`.

## 📡 API Reference

| Endpoint       | Method | Description        | Example Response                                   |
| -------------- | ------ | ------------------ | -------------------------------------------------- |
| `/api/health`  | GET    | Health check       | `{"status":"ok"}`                                  |
| `/api/data`    | GET    | All data aggregate | `{news:[], weather:{}, finance:{}, ports:{}, ...}` |
| `/api/analyze` | POST   | AI synthesis       | `{brief:"...", risk_index:68, forecasts:[], ...}`  |

**Full OpenAPI**: http://localhost:8000/docs

## ➕ Adding Features

IRIS-AI is modular – easy to extend!

### 1. New Data Provider

```python
# backend/data_providers/my_data.py
def get_my_data():
    return {"key": "value"}  # API or dummy

# backend/main.py
from data_providers.my_data import get_my_data
@app.get("/api/data")
results["my_data"] = get_my_data()
```

### 2. New API Endpoint

```python
@app.get("/api/new-feature")
async def new_feature():
    return {...}
```

### 3. Frontend Component

```bash
cd frontend
npm install some-lib
```

Add to `src/main.ts` or new `src/components/NewFeature.ts`.

### 4. Map Layer

- Add GeoJSON to `frontend/public/layers/my-layer.geojson`
- Toggle in map init (MapLibre `addSource/addLayer`).

### 5. AI Enhancement

Update `/api/analyze` Groq prompt:

```python
# Stronger system prompt for new outputs
```

### 6. Deployment

- Push to GitHub.
- Render auto-deploys on push.

**Examples**:

- Add earthquake data: New provider + map layer.
- Custom alerts: Filter `/api/data` + UI panel.

## ☁️ Deployment

### Render (Recommended)

1. **Backend** (Web Service):
   - Repo: `backend/` dir.
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Env: `NEWS_API_KEY`, `GROQ_API_KEY`
2. **Frontend** (Static Site):
   - Build: `npm install && npm run build`
   - Publish: `dist/`

Update frontend API baseURL to deployed backend.

## 🤝 Contributing

1. Fork → Clone → Create branch (`feat/my-feature`).
2. Hack → Test locally.
3. Commit → PR with description.
4. Follow Python (black) / TS (prettier) formatting.

Issues? Open one with steps to repro.

## 🗺️ Roadmap

- [x] Backend data aggregation
- [ ] Groq AI live integration
- [ ] Interactive map + layers
- [ ] Full UI polish (LIVE badge, panels)
- [ ] Render deployment
- [ ] Demo video

See `TODO.md` for progress.

## 📄 License

MIT – Free to use/fork.

---

**⭐ Star on GitHub! Questions? [Open Issue](https://github.com/issues/new)**

**Built with ❤️ in 10-hour hackathon | March 2026**
