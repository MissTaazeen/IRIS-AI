from datetime import datetime
from typing import Dict

# Power: demand vs supply MW (monsoon shortages)
POWER_DATA = {
    'Maharashtra': {'demand': 18000, 'supply': 16500, 'deficit_pct': 8.3},
    'Delhi': {'demand': 8500, 'supply': 7900, 'deficit_pct': 7.1},
    'Karnataka': {'demand': 14500, 'supply': 13200, 'deficit_pct': 9.0},
    'Tamil Nadu': {'demand': 16200, 'supply': 14800, 'deficit_pct': 8.6},
    'Gujarat': {'demand': 21000, 'supply': 19500, 'deficit_pct': 7.1},
    'UP': {'demand': 28500, 'supply': 26200, 'deficit_pct': 8.1},
    'Rajasthan': {'demand': 14500, 'supply': 13400, 'deficit_pct': 7.6},
    'MP': {'demand': 16500, 'supply': 15200, 'deficit_pct': 7.9},
    'West Bengal': {'demand': 12500, 'supply': 11500, 'deficit_pct': 8.0},
    'Bihar': {'demand': 8500, 'supply': 7800, 'deficit_pct': 8.2}
}

WATER_DATA = {
    'Ganga (Kanpur)': {'level': 'low', 'pct_normal': 65},
    'Yamuna (Delhi)': {'level': 'critical', 'pct_normal': 45},
    'Godavari': {'level': 'medium', 'pct_normal': 75},
    'Krishna': {'level': 'low', 'pct_normal': 60}
}

def get_infra() -> Dict:
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'power': POWER_DATA,
        'national_power_deficit_avg': sum(s['deficit_pct'] for s in POWER_DATA.values()) / len(POWER_DATA),
        'critical_states': [s for s, d in POWER_DATA.items() if d['deficit_pct'] > 8],
        'water_reservoirs': WATER_DATA
    }

