from datetime import datetime
from typing import Dict, List

CONFLICT_DATA = {
    'LoC (J&K)': {'intensity': 'medium', 'incidents_24h': 12, 'casualties': 3, 'alert': True},
    'LAC (Ladakh/NE)': {'intensity': 'low', 'incidents_24h': 2, 'casualties': 0, 'alert': False},
    'Naxal Areas (Chhattisgarh/Jharkhand)': {'intensity': 'medium', 'incidents_24h': 8, 'casualties': 5, 'alert': True},
    'NE Insurgencies': {'intensity': 'low', 'incidents_24h': 3, 'casualties': 1, 'alert': False},
    'Urban Unrest': {'intensity': 'low', 'incidents_24h': 5, 'casualties': 0, 'alert': False}
}

RISK_ZONES = [
    {'name': 'Jammu', 'lat': 32.73, 'lon': 74.87, 'risk': 75},
    {'name': 'Srinagar', 'lat': 34.01, 'lon': 74.77, 'risk': 80},
    {'name': 'Dantewada', 'lat': 18.85, 'lon': 81.62, 'risk': 65},
    # more geo points for map
]

def get_conflict() -> Dict:
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'regions': CONFLICT_DATA,
        'total_incidents_24h': sum(r['incidents_24h'] for r in CONFLICT_DATA.values()),
        'risk_zones': RISK_ZONES
    }

