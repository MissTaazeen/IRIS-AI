from datetime import datetime
from typing import Dict
from data_providers.news import get_news

# Base data for major cities
BASE_TRAFFIC = {
    'Mumbai': {'roads': {'avg_delay_min': 38}, 'local_trains': {'congestion': 92}},
    'Delhi': {'roads': {'avg_delay_min': 45}, 'metro': {'congestion': 88}},
    'Bengaluru': {'roads': {'avg_delay_min': 52}},
    'Chennai': {'roads': {'avg_delay_min': 35}},
    'Hyderabad': {'roads': {'avg_delay_min': 41}}
}

TRAFFIC_KEYWORDS = ['traffic jam', 'waterlogging', 'accident', 'flood road', 'delay train', 'congestion']

def get_traffic() -> Dict:
    news = get_news()
    
    cities = list(BASE_TRAFFIC.keys())
    traffic_alerts = {city: 0 for city in cities}
    
    for article in news.get('headlines', []):
        title_lower = article['title'].lower()
        for city in cities:
            if city.lower() in title_lower and any(kw in title_lower for kw in TRAFFIC_KEYWORDS):
                traffic_alerts[city] += 1
    
    # Apply alerts to base data
    cities_data = {}
    total_road_delay = 0
    road_cities = 0
    critical_cities = []
    
    for city, base in BASE_TRAFFIC.items():
        alert_factor = traffic_alerts[city] * 5  # +5 min delay per mention
        data = {k: v.copy() if isinstance(v, dict) else v for k, v in base.items()}
        
        if 'roads' in data:
            data['roads']['avg_delay_min'] = min(90, base['roads']['avg_delay_min'] + alert_factor)
            total_road_delay += data['roads']['avg_delay_min']
            road_cities += 1
        
        for mode in data:
            if isinstance(data[mode], dict) and 'congestion' in data[mode]:
                data[mode]['congestion'] = min(100, data[mode]['congestion'] + alert_factor)
        
        cities_data[city] = data
        if (data.get('roads', {}).get('avg_delay_min', 0) > 40 or 
            data.get('local_trains', {}).get('congestion', 0) > 90):
            critical_cities.append(city)
    
    national_avg_road_delay = total_road_delay / road_cities if road_cities else 0
    
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'cities': cities_data,
        'national_avg_road_delay': round(national_avg_road_delay, 1),
        'critical_cities': critical_cities,
        'news_alerts_total': sum(traffic_alerts.values())
    }
