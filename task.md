# IndiaMonitor.app – 10-Hour Hackathon Task File
**Team of 3 | AI/ML Track | Goal: Build WorldMonitor.app but for entire India**

**Date:** 31 March 2026  
**Time Window:** 12:00 PM IST – 10:00 PM IST (10 hours)  
**Constraints:**  
- Use **only public APIs** (no web scraping)  
- Use **realistic dummy JSON** for ports, conflict, power, traffic  
- Deploy on **Render** (Backend as Web Service + Frontend as Static Site)  
- Mirror WorldMonitor.app look & feel as closely as possible (dark theme, LIVE badge, layered map, AI briefs, risk index, correlations)

## Team Roles & Responsibilities

| Role                          | Member     | Primary Responsibilities |
|-------------------------------|------------|---------------------------|
| **Backend & Data Engineer**   | Member 1   | FastAPI server, API integrations, dummy data, aggregator endpoint |
| **Frontend & Visualization**  | Member 2   | Vite + TypeScript UI, MapLibre GL / Leaflet map, dark theme, panels |
| **AI/ML + Deployment Lead**   | Member 3   | Groq integration, AI synthesis, full integration, Render deployment, demo video |

**Communication:** Sync every 2 hours (12:00, 14:00, 16:00, 18:00, 20:00) on Discord/WhatsApp.

---

## Phase 0: Project Setup (12:00 – 12:40 PM | All 3 together – 40 mins)

**All Members:**
1. Create a private GitHub repo named `indiamonitor-hackathon`
2. Clone the repo
3. Share the repo link in group chat
4. Install prerequisites:
   - Node.js 20+
   - Python 3.11+
   - Git
5. Get API keys (do this immediately):
   - Groq API key[](https://console.groq.com)
   - NewsAPI.org key[](https://newsapi.org) → set `country=in`
   - (Optional) OpenWeatherMap key (free tier)

**Member 1 – Backend Setup**
- Create folder structure:
