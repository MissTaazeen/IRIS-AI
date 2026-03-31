import os
from datetime import datetime
from typing import Dict
from data_providers.news import get_news
from dotenv import load_dotenv

load_dotenv()

# Base static data (seasonally adjusted)
BASE_POWER = {
    'Maharashtra': {'demand': 18000, 'deficit_pct': 8.3},
    'Delhi': {'demand': 8500, 'deficit_pct': 7.1},
    'Karnataka': {'demand': 14500, 'deficit_pct': 9.0},
    'Tamil Nadu': {'demand': 16200, 'deficit_pct': 8.6},
    'Gujarat': {'demand': 21000, 'deficit_pct': 7.1},
    'UP': {'demand': 28500, 'deficit_pct': 8.1},
    'Rajasthan': {'demand': 14500, 'deficit_pct': 7.6},
    'MP': {'demand': 16500, 'deficit_pct': 7.9},
    'West Bengal': {'demand': 12500, 'deficit_pct': 8.0},
    'Bihar': {'demand': 8500, 'deficit_pct': 8.2}
}

BASE_WATER = {
    'Ganga (Kanpur)': {'level': 'low', 'pct_normal': 65},
    'Yamuna (Delhi)': {'level': 'critical', 'pct_normal': 45},
    'Godavari': {'level': 'medium', 'pct_normal': 75},
    'Krishna': {'level': 'low', 'pct_normal': 60}
}

def get_infra() -> Dict:
    news = get_news()
    
    power_alerts = {state: 0 for state in BASE_POWER}
    water_alerts = {river: 0 for river in BASE_WATER}
    power_cut_keywords = ['power cut', 'load shedding', 'blackout', 'deficit']
    
    for article in news.get('headlines', []):
        title_lower = article['title'].lower()
        for state in power_alerts:
            if state.lower() in title_lower and any(kw in title_lower for kw in power_cut_keywords):
                power_alerts[state] += 1
        for river in water_alerts:
            if any(word in title_lower for word in river.lower().split()):
                water_alerts[river] += 1
    
    # Apply news impact
    power_data = {}
    national_deficit = 0
    critical_states = []
    
    for state, base in BASE_POWER.items():
        alert_factor = power_alerts[state] * 1.5
        deficit = min(20, base['deficit_pct'] + alert_factor)
        supply = int(base['demand'] * (1 - deficit/100))
        power_data[state] = {'demand': base['demand'], 'supply': supply, 'deficit_pct': round(deficit, 1)}
        national_deficit += deficit
        if deficit > 8:
            critical_states.append(state)
    
    national_deficit /= len(BASE_POWER)
    
    water_data = {r: {**BASE_WATER[r], 'alerts': water_alerts[r]} for r in BASE_WATER}
    
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'power': power_data,
        'national_power_deficit_avg': round(national_deficit, 1),
        'critical_states': critical_states,
        'water_reservoirs': water_data,
        'news_power_alerts': sum(power_alerts.values())
    }
