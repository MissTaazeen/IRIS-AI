import requests
from datetime import datetime
from typing import Dict

# Major cities lat/lon
CITIES = {
    'Mumbai': {'lat': 19.0760, 'lon': 72.8777},
    'Delhi': {'lat': 28.6139, 'lon': 77.2090},
    'Bengaluru': {'lat': 12.9716, 'lon': 77.5946},
    'Chennai': {'lat': 13.0827, 'lon': 80.2707},
    'Hyderabad': {'lat': 17.3850, 'lon': 78.4867}
}

def get_weather() -> Dict:
    weather_data = {}
    for city, coords in CITIES.items():
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true&hourly=temperature_2m,precipitation_probability&timezone=Asia/Kolkata"
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            current = data['current_weather']
            hourly = data['hourly']
            weather_data[city] = {
                'temp': current['temperature'],
                'wind_speed': current['windspeed'],
                'precipitation': current.get('precipitation', 0),
                'next_hour_precip_prob': hourly['precipitation_probability'][0] if hourly['precipitation_probability'] else 0
            }
        except Exception as e:
            weather_data[city] = {'error': str(e)}
    
    return {'timestamp': datetime.utcnow().isoformat(), 'cities': weather_data}

