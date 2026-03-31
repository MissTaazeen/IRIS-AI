# 🇮🇳 IRIS – Frontend (India Real-time Intelligence Dashboard)

## 📌 Overview

This is the **frontend application** of IRIS (India Real-time Intelligence Dashboard).

It provides a **visual, interactive map-based interface** for monitoring national-level intelligence signals such as:

* Infrastructure
* Environment
* Conflict zones
* Economic indicators

⚠️ Note: This version runs in **Simulation Mode** (no backend dependency) for stability and demonstration.

---

## 🚀 Features

### 🗺️ Interactive India Map

* Built using **MapLibre GL**
* Focused view restricted to India
* Smooth navigation and zoom

### 🧭 State Boundaries

* GeoJSON-based rendering of Indian states
* Clean border visualization

### 🖱️ Interactivity

* Click on any state → displays state name
* Hover → pointer interaction for better UX

### ⏱️ Live Clock

* Real-time clock displayed on top-right
* Simulates live dashboard environment

### 🎨 Modern UI

* Dark-themed dashboard layout
* Sidebar + Map + Insight panel structure
* Clean and minimal design for clarity

---

## 🛠️ Tech Stack

* **Frontend Framework:** Vite + TypeScript
* **Mapping Library:** MapLibre GL
* **Styling:** CSS (custom + utility-based)
* **Data Source:** Static GeoJSON

---

## 📁 Project Structure

```
frontend/
│── public/
│   └── india_state_geo.json   # GeoJSON for Indian states
│
│── src/
│   ├── App.ts                # Main application logic
│   ├── main.ts               # Entry point
│   └── style.css             # Styles
│
│── index.html
│── vite.config.js
```

---

## ⚙️ Setup & Run

### 1. Install dependencies

```bash
npm install
```

### 2. Run development server

```bash
npm run dev
```

### 3. Open in browser

```
http://localhost:5173
```

---

## 📊 Demo Mode

This frontend runs in **Simulation Mode**:

* No backend required
* No API calls
* Designed for stable demo and presentation

---

## 🧠 Future Scope

* Integration with real-time backend APIs
* AI-based risk analysis
* Dynamic heatmaps
* Multi-layer data visualization
* Predictive intelligence insights

---

## 🏁 Final Note

This project demonstrates the **visualization layer of a scalable national intelligence system**, designed to integrate real-time multi-domain data for decision-making.

---
