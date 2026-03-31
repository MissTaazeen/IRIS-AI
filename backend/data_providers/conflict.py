import os
from datetime import datetime
from typing import Dict, List
from data_providers.news import get_news

# Static risk zones with coords for map
RISK_ZONES = [
    {'name': 'Jammu', 'lat': 32.73, 'lon': 74.87, 'risk': 75},
    {'name': 'Srinagar', 'lat': 34.01, 'lon': 74.77, 'risk': 80},
    {'name': 'Dantewada', 'lat': 18.85, 'lon': 81.62, 'risk': 65},
    {'name': 'Imphal', 'lat': 24.82, 'lon': 93.94, 'risk': 55},
]

def get_conflict() -> Dict:
    news = get_news()
    keywords = {
        'LoC (J&K)': ['loc', 'line of control', 'jammu kashmir', 'pakistan border'],
        'LAC (Ladakh/NE)': ['lac', 'line actual', 'china border', 'ladakh', 'arunachal'],
        'Naxal Areas': ['naxal', 'maoist', 'chhattisgarh', 'jharkhand', 'dantewada'],
        'NE Insurgencies': ['northeast', 'manipur', 'nagaland', 'insurgency', 'militants'],
        'Urban Unrest': ['riot', 'protest violence', 'clash police']
    }
    
    regions = {}
    total_incidents = 0
    
    for region, kws in keywords.items():
        count = 0
        casualties = 0
        for article in news.get('headlines', []):
            title_lower = article['title'].lower()
            matches = sum(1 for kw in kws if kw in title_lower)
            if matches > 0:
                count += 1
                if any(word in title_lower for word in ['dead', 'killed', 'casualties', 'injury']):
                    casualties += 2  # Weighted
                total_incidents += 1
        intensity = 'high' if count > 3 else 'medium' if count > 1 else 'low'
        alert = count > 1 or casualties > 2
        regions[region] = {'intensity': intensity, 'incidents_24h': count, 'casualties': min(10, casualties), 'alert': alert}
    
    # Adjust risk_zones based on news
    for zone in RISK_ZONES:
        # Simple boost if matching region news
        zone['risk'] = min(100, zone['risk'] + sum(regions[r].get('incidents_24h', 0) * 5 for r in regions))
    
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'regions': regions,
        'total_incidents_24h': total_incidents,
        'risk_zones': RISK_ZONES,
        'news_correlation': f'{total_incidents} incidents from {len(news.get("headlines", []))} headlines'
    }
