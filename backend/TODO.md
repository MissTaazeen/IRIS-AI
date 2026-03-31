# IRIS-AI Backend Integration TODO

## Status: 7/9 table.csv items integrated (finance, news, weather, ports, conflict, infra, traffic). Map/Groq pending.

### Step 1: ✅ COMPLETE Documentation

- Created `data_providers/APIS-needed.md`

### Step 2: ✅ COMPLETE Provider Implementations (Free APIs)

- `ports.py`: ✅ Open-Meteo + news filter
- `conflict.py`: ✅ News keyword filter
- `infra.py`: ✅ Static + news (power/water)
- `traffic.py`: ✅ Static + news
- `map_layers.py`: Static GeoJSON + dynamic overlays

### Step 3: ✅ COMPLETE Core Updates

- Real Groq in `/api/analyze` ✅
- main.py imports/endpoints updated ✅
- requirements.txt has groq ✅

### Step 4: [PENDING] Cleanup & Test

- Delete dummy\_\*.py
- Test all /api/\*
- Frontend map integration

**Next: Step 3**
