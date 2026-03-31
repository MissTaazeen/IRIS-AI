from datetime import datetime
from typing import Dict, List

TRAFFIC_DATA = {
    'Mumbai': {
        'local_trains': {'congestion': 92, 'delay_min': 45, 'incidents': ['flooded tracks']},
        'roads': {'avg_delay_min': 38, 'hotspots': ['Bandra-Worli', 'Eastern Express']}
    },
    'Delhi': {
        'roads': {'avg_delay_min': 45, 'hotspots': ['Delhi-Gurugram', 'Ring Road']},
        'metro': {'congestion': 88, 'delay_min': 22}
    },
    'Bengaluru': {
        'roads': {'avg_delay_min': 52, 'hotspots': ['Outer Ring Road', 'Silk Board']},
        'incidents': ['waterlogging']
    },
    'Chennai': {
        'roads': {'avg_delay_min': 35, 'hotspots': ['Anna Salai']},
        'rail': {'delay_min': 28}
    },
    'Hyderabad': {
        'roads': {'avg_delay_min': 41, 'hotspots': ['Hitech City']}
    }
    # add more cities
}

def get_traffic() -> Dict:
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'cities': TRAFFIC_DATA,
        'national_avg_road_delay': sum(c['roads']['avg_delay_min'] for c in TRAFFIC_DATA.values() if 'roads' in c),
        'critical_cities': [c for c, d in TRAFFIC_DATA.items() if (d.get('roads', {}).get('avg_delay_min', 0) > 40 or d.get('local_trains', {}).get('congestion', 0) > 90)]
    }

