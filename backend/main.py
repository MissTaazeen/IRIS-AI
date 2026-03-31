from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from datetime import datetime
from typing import Dict, Any

# Import data providers (all real)
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "IndiaMonitor Backend", "timestamp": datetime.utcnow().isoformat()}

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

@app.get("/api/analyze")
async def analyze_data():
    import json
    from groq import Groq
    
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        return {"error": "GROQ_API_KEY not set. Add to .env. Fallback:", "risk_index": 65, "national_brief": "Set GROQ_API_KEY for AI analysis."}
    
    client = Groq(api_key=api_key)
    
    data = await get_all_data()
    
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
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            response_format={"type": "json_object"}
        )
        result = json.loads(response.choices[0].message.content)
        result['timestamp'] = datetime.utcnow().isoformat()
        return result
    except Exception as e:
        return {"error": str(e), "risk_index": 65, "timestamp": datetime.utcnow().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
