from datetime import datetime
from typing import Dict, List

# Realistic monsoon 2026 data
PORTS_DATA = {
    'JNPT (Mumbai)': {'congestion': 85, 'delay_hours': 24, 'status': 'high', 'reason': 'monsoon delays'},
    'Mumbai Port': {'congestion': 78, 'delay_hours': 18, 'status': 'high', 'reason': 'heavy rain'},
    'Chennai Port': {'congestion': 65, 'delay_hours': 12, 'status': 'medium', 'reason': 'cyclone risk'},
    'Visakhapatnam': {'congestion': 45, 'delay_hours': 6, 'status': 'low', 'reason': 'normal'},
    'Kolkata': {'congestion': 72, 'delay_hours': 15, 'status': 'medium', 'reason': 'flooding'},
    'Cochin': {'congestion': 55, 'delay_hours': 8, 'status': 'medium', 'reason': 'winds'},
    'Kandla': {'congestion': 60, 'delay_hours': 10, 'status': 'medium', 'reason': 'storm surge'},
    'Paradip': {'congestion': 40, 'delay_hours': 4, 'status': 'low', 'reason': 'clear'},
    'New Mangalore': {'congestion': 70, 'delay_hours': 14, 'status': 'high', 'reason': 'rough seas'},
    'Mormugao': {'congestion': 50, 'delay_hours': 7, 'status': 'low', 'reason': 'moderate'},
    'Tuticorin': {'congestion': 62, 'delay_hours': 11, 'status': 'medium', 'reason': 'rain'},
    'Krishnapatnam': {'congestion': 48, 'delay_hours': 5, 'status': 'low', 'reason': 'ok'},
    'Ennore': {'congestion': 75, 'delay_hours': 16, 'status': 'high', 'reason': 'urban flooding'},
    'Hazira': {'congestion': 52, 'delay_hours': 9, 'status': 'medium', 'reason': 'tides'},
    'Pipavav': {'congestion': 58, 'delay_hours': 10, 'status': 'medium', 'reason': 'weather'},
    'Dhamra': {'congestion': 42, 'delay_hours': 4, 'status': 'low', 'reason': 'clear'},
    'Sagar Island': {'congestion': 68, 'delay_hours': 13, 'status': 'medium', 'reason': 'estuary floods'}
}

def get_ports() -> Dict:
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'ports': PORTS_DATA,
        'national_avg_congestion': sum(p['congestion'] for p in PORTS_DATA.values()) / len(PORTS_DATA),
        'critical_ports': [p for p, d in PORTS_DATA.items() if d['congestion'] > 70]
    }

