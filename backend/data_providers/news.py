import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from typing import List, Dict

load_dotenv()

def get_news() -> Dict:
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        return {'error': 'NEWS_API_KEY not set', 'headlines': []}
    
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}'
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        headlines = data.get('articles', [])[:10]
        formatted = [
            {
                'title': article['title'],
                'source': article['source']['name'],
                'url': article['url'],
                'published': article['publishedAt']
            }
            for article in headlines
        ]
        return {'timestamp': datetime.utcnow().isoformat(), 'headlines': formatted}
    except Exception as e:
        return {'error': str(e), 'headlines': [], 'fallback': True}

