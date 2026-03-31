from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import uvicorn
from datetime import datetime
import asyncio
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

app = FastAPI(title="IndiaMonitor Backend", version="1.0.0")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for prod
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
    tasks = [
        get_news(),
        get_weather(),
        get_finance(),
        get_ports(),
        get_conflict(),
        get_infra(),
        get_traffic()
    ]
    # Await async if needed, but providers are sync
    results = {
        'timestamp': datetime.utcnow().isoformat(),
        'news': tasks[0],
        'weather': tasks[1],
        'finance': tasks[2],
        'ports': tasks[3],
        'conflict': tasks[4],
        'infra': tasks[5],
        'traffic': tasks[6]
    }
    return results

@app.post("/api/analyze")
async def analyze_data(request: AnalyzeRequest):
    # Stub for Member 3 Groq integration
    return {
        "national_brief": "Monsoon disruptions affecting ports and power supply across western India.",
        "risk_index": 68,
        "top_drivers": ["Ports congestion", "Power deficit", "LoC activity"],
        "forecasts": ["24h: Increased flooding risk Mumbai/Delhi", "48h: Market volatility", "72h: Supply chain delays"],
        "correlation": "Monsoon precip × Ports congestion × Nifty (-0.72)",
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

