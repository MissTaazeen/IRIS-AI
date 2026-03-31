import requests
from datetime import datetime
from typing import Dict
import os
from dotenv import load_dotenv
from data_providers.news import get_news  # Reuse for port mentions

load_dotenv()

# Major Indian ports lat/lon (for weather)
PORTS_COORDS = {
    'JNPT (Mumbai)': {'lat': 18.95, 'lon': 72.90},
    'Mumbai Port': {'lat': 18.94, 'lon': 72.83},
    'Chennai Port': {'lat': 13.10, 'lon': 80.29},
    'Visakhapatnam': {'lat': 17.69, 'lon': 83.22},
    'Kolkata': {'lat': 22.57, 'lon': 88.34},
    'Cochin': {'lat': 9.96, 'lon': 76.27},
    'Kandla': {'lat': 23.03, 'lon': 70.21},
    'Paradip': {'lat': 20.27, 'lon': 86.69},
    'New Mangalore': {'lat': 12.91, 'lon': 74.80},
    'Mormugao': {'lat': 15.43, 'lon': 73.75},
    'Tuticorin': {'lat': 8.80, 'lon': 78.19},
    'Krishnapatnam': {'lat': 14.22, 'lon': 80.18},
    'Ennore': {'lat': 13.22, 'lon': 80.35},
    'Hazira': {'lat': 20.95, 'lon': 72.67},
    'Pipavav': {'lat': 20.75, 'lon': 71.45},
    'Dhamra': {'lat': 20.92, 'lon': 86.52},
    'Sagar Island': {'lat': 21.65, 'lon': 88.44}
}

def get_weather_for_port(lat: float, lon: float) -> Dict:
    """Get weather impacting port ops"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=precipitation_probability,windspeed_10m&timezone=Asia/Kolkata"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        current = data['current_weather']
        next_precip = data['hourly']['precipitation_probability'][0]
        wind = current['windspeed']
        precip = current.get('precipitation', 0)
        return {'precip': precip, 'precip_prob': next_precip, 'wind': wind}
    except:
        return {'precip': 0, 'precip_prob': 0, 'wind': 10}

def get_ports() -> Dict:
    news = get_news()
    port_names = list(PORTS_COORDS.keys())
    
    ports_data = {}
    total_mentions = 0
    
    # News filter for port issues
    port_mentions = {p: 0 for p in port_names}
    for article in news.get('headlines', []):
        title_lower = article['title'].lower()
        for port in port_names:
            if port.lower().split()[0] in title_lower or any(word in title_lower for word in port.lower().split()[:2]):
                port_mentions[port] += 1
                total_mentions += 1
        if any(kw in title_lower for kw in ['delay', 'congestion', 'stranded', 'shutdown', 'flood']):
            port_mentions['news_alert'] = port_mentions.get('news_alert', 0) + 1
    
    # Weather-derived congestion
    national_avg_congestion = 0
    critical_ports = []
    
    for name, coords in PORTS_COORDS.items():
        weather = get_weather_for_port(coords['lat'], coords['lon'])
        mentions = port_mentions.get(name, 0)
        
        # Derive metrics: high precip/wind + news = high congestion
        base_congestion = 30 + (weather['precip_prob'] * 0.5) + (weather['wind'] * 1.2) + (mentions * 10)
        congestion = min(100, max(20, base_congestion))
        delay_hours = int(congestion / 8)
        status = 'high' if congestion > 70 else 'medium' if congestion > 50 else 'low'
        reason = 'monsoon/heavy rain' if weather['precip_prob'] > 50 else 'high winds' if weather['wind'] > 20 else 'news alerts' if mentions > 0 else 'normal'
        
        ports_data[name] = {
            'congestion': round(congestion, 1),
            'delay_hours': delay_hours,
            'status': status,
            'reason': reason,
            'weather': weather,
            'news_mentions': mentions
        }
        national_avg_congestion += congestion
        if congestion > 70:
            critical_ports.append(name)
    
    national_avg_congestion /= len(PORTS_COORDS)
    
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'ports': ports_data,
        'national_avg_congestion': round(national_avg_congestion, 1),
        'critical_ports': critical_ports,
        'total_news_mentions': total_mentions
    }
