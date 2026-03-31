from datetime import datetime
from typing import Dict, List
from data_providers.ports import get_ports
from data_providers.conflict import get_conflict
from data_providers.weather import get_weather

# Simplified India states GeoJSON (boundary data truncated for demo; use full from https://github.com/datameet/india/raw/master/2011/states.geojson)
INDIA_STATES_GEOJSON = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature", "properties": {"STATE_NAME": "Maharashtra", "risk": 72}, "geometry": {"type": "Polygon", "coordinates": [[72.6,23.6],[78.5,23.6],[78.5,19.1],[72.6,19.1]]}},  # Simplified bbox
        {"type": "Feature", "properties": {"STATE_NAME": "Delhi", "risk": 68}, "geometry": {"type": "Polygon", "coordinates": [[76.8,28.4],[77.4,28.4],[77.4,28.9],[76.8,28.9]]}},
        # Add more states as needed; full data external
    ]
}

def get_map_layers() -> Dict:
    """Map data: states (risk color), ports (pins), conflict zones, weather overlays"""
    
    # Dynamic risk from providers
    ports = get_ports()
    conflict = get_conflict()
    weather_cities = get_weather()['cities']
    
    # Port points
    port_features = []
    for name, data in list(ports['ports'].items())[:10]:  # Top 10
        # Extract coords from ports.py implicitly
        port_coords = {  # Match ports.py PORTS_COORDS subset
            'JNPT (Mumbai)': [18.95, 72.90],
            'Chennai Port': [13.10, 80.29],
            # ...
        }.get(name, [0,0])
        feature = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": port_coords},
            "properties": {"name": name, "congestion": data['congestion'], "status": data['status']}
        }
        port_features.append(feature)
    
    # Conflict zones
    conflict_features = [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [z['lon'], z['lat']]},
            "properties": {"name": z['name'], "risk": z['risk']}
        }
        for z in conflict['risk_zones']
    ]
    
    # Weather cities overlay (precip prob)
    weather_features = []
    city_coords = {  # From weather.py
        'Mumbai': [72.8777, 19.0760],
        'Delhi': [77.2090, 28.6139],
        # ...
    }
    for city, wdata in weather_cities.items():
        coords = city_coords.get(city, [0,0])
        precip = wdata.get('next_hour_precip_prob', 0)
        feature = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": coords},
            "properties": {"city": city, "precip_prob": precip, "temp": wdata.get('temp', 0)}
        }
        weather_features.append(feature)
    
    # Update state risks (demo aggregation)
    for feature in INDIA_STATES_GEOJSON['features']:
        state = feature['properties']['STATE_NAME']
        feature['properties']['risk'] = 65 + (hash(state) % 20)  # Demo; real from data synth
    
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "layers": {
            "states": INDIA_STATES_GEOJSON,
            "ports": {"type": "FeatureCollection", "features": port_features},
            "conflict_zones": {"type": "FeatureCollection", "features": conflict_features},
            "weather_cities": {"type": "FeatureCollection", "features": weather_features}
        },
        "summary": {
            "total_ports": len(port_features),
            "high_risk_zones": len([f for f in conflict_features if f['properties']['risk'] > 70]),
            "rainy_cities": len([f for f in weather_features if f['properties']['precip_prob'] > 50])
        }
    }
