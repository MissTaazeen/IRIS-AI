# Required APIs for IRIS-AI (Free/Best Alternatives)

## Implemented ✅

| Feature | API         | Key            | Endpoint                       | Status  |
| ------- | ----------- | -------------- | ------------------------------ | ------- |
| Finance | yfinance    | None           | N/A                            | ✅ Real |
| News    | NewsAPI.org | `NEWS_API_KEY` | `/v2/top-headlines?country=in` | ✅ Real |
| Weather | Open-Meteo  | None           | `/v1/forecast?lat=X&lon=Y`     | ✅ Real |

## To Implement (Free Alternatives) 🔄

| Feature                           | table.csv # | API/Source                             | Key            | Notes                                        |
| --------------------------------- | ----------- | -------------------------------------- | -------------- | -------------------------------------------- |
| National Brief/Alerts/Correlation | 1,8,9       | Groq                                   | `GROQ_API_KEY` | Free tier: llama3.1:70b-versatile            |
| Ports Monitor                     | 5           | Open-Meteo (port coords) + news filter | None           | IMD no public free API; use coords for ports |
| Conflict Zones                    | 7           | News keyword filter                    | Reuse NEWS     | Keywords: LoC,LAC,Naxal,insurgency           |
| Infra (power/water)               | N/A         | Static + news filter                   | None           | CEA/CPCB no real-time free APIs              |
| Traffic                           | N/A         | Static + news filter                   | None           | TomTom free limited; Google paid             |
| Map Layers                        | 2           | Static GeoJSON files                   | None           | India states/ports from GitHub/public        |

## .env Required

```
NEWS_API_KEY=your_newsapi_key
GROQ_API_KEY=your_groq_key
```

## Free API Limits

- NewsAPI: 100/day free
- Open-Meteo: Unlimited
- Groq: Rate limited free tier
- yfinance: Unofficial but reliable

**Priority**: Add GROQ_API_KEY → implement /api/analyze → providers.
