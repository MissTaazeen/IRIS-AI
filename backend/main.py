from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from datetime import datetime
from typing import Dict, Any

# Import data providers
from data_providers.news import get_news
from data_providers.weather import get_weather
from data_providers.finance import get_finance
from data_providers.dummy_ports import get_ports
from data_providers.dummy_conflict import get_conflict
from data_providers.dummy_infra import get_infra
from data_providers.dummy_traffic import get_traffic

load_dotenv()

app = FastAPI(title="IRIS - India Real-time Intelligence")

# Add this block right after creating the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    data: str

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "IndiaMonitor Backend", "timestamp": datetime.utcnow().isoformat()}

@app.get("/api/data", response_model=Dict[str, Any])
async def get_all_data():
    results = {
        'news': get_news(),
        'weather': get_weather(),
        'finance': get_finance(),
        'ports': get_ports(),
        'conflict': get_conflict(),
        'infra': get_infra(),
        'traffic': get_traffic()
    }
    results['timestamp'] = datetime.utcnow().isoformat()
    return results

@app.post("/api/analyze")
async def analyze_data(request: AnalyzeRequest):
    # Stub for Member 3 Groq integration
    return {
        "national_brief": "Monsoon disruptions affecting ports and power supply across western India amid medium LoC tensions.",
        "risk_index": 68,
        "top_drivers": ["Ports congestion (JNPT 85%)", "Power deficit (8.2% national)", "LoC activity"],
        "forecasts": ["24h: Increased flooding Mumbai/Delhi (65% prob)", "48h: Nifty volatility ±2%", "72h: Supply chain delays ports"],
        "correlation": "Monsoon precip × Ports congestion × Nifty (corr -0.72)",
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

