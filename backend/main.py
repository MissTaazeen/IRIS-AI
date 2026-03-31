from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from datetime import datetime
from typing import Dict, Any, List
import asyncio
import json
from groq import Groq

# Import data providers
from data_providers.news import get_news
from data_providers.weather import get_weather
from data_providers.finance import get_finance
from data_providers.ports import get_ports
from data_providers.conflict import get_conflict
from data_providers.infra import get_infra
from data_providers.traffic import get_traffic
from data_providers.map_layers import get_map_layers

load_dotenv()

app = FastAPI(title="IRIS - India Real-time Intelligence")

# ✅ Middleware FIRST
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Response Model
class AnalyzeResponse(BaseModel):
    national_brief: str
    risk_index: int
    top_drivers: List[str]
    forecasts: List[str]
    correlation: str
    timestamp: str


@app.get("/api/health")
async def health_check():
    return {
        "status": "ok",
        "service": "IndiaMonitor Backend",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/api/map")
async def get_map_data():
    return get_map_layers()


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


@app.get("/api/analyze", response_model=AnalyzeResponse)
async def analyze_data():
    api_key = os.getenv('GROQ_API_KEY')

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY not set"
        )

    client = Groq(api_key=api_key)

    try:
        # ✅ Timeout protection
        data = await asyncio.wait_for(get_all_data(), timeout=10)

        prompt = f"""India Risk Analysis from data:

{json.dumps(data, indent=2)}

JSON response:
{{
  "national_brief": "2-3 urgent sentences",
  "risk_index": number (0-100),
  "top_drivers": ["3 bullets"],
  "forecasts": ["24h", "48h", "72h"],
  "correlation": "1 key cross-risk"
}}"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        
        # Defensive parsing in case Groq returns a dict for forecasts
        if isinstance(result.get("forecasts"), dict):
            # Combine keys and values if it returned something like {"24h": "..."}
            result["forecasts"] = [f"{k}: {v}" for k, v in result["forecasts"].items()]

        result['timestamp'] = datetime.utcnow().isoformat()

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)