# Frontend (Member 2) - TODO Skeleton

Vite + TS + Tailwind + MapLibre GL. Mirror WorldMonitor dark theme.

## Setup

```bash
npm create vite@latest . -- --template vanilla-ts
npm install
npm install maplibre-gl axios tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm install india-geojson  # or download public/india.geojson
npm run dev
```

## Components

- Map: India center, state colors by risk, layers (weather/ports/conflict/traffic toggle)
- UI: LIVE badge, sidebar AI brief/risk, right panel forecasts/correlations, bottom news/finance
- API: axios to backend /api/data & /api/analyze

## Tailwind (dark)

```
@config "tailwind.config.js"
darkMode: 'class'
```

**Next:** Build map skeleton, connect APIs, polish theme.

Status: ⏳
