# DriveGuard QA Simulator

This project simulates an **Electronic Logging Device (ELD)** system used in commercial vehicles. It is designed to give hands-on QA experience around embedded systems, log generation, alert logic, automation, and SQL analytics.

---

## Features

- Log simulation of vehicle data (speed, GPS, engine status, temperature, etc.)
- Rule-based alert engine (overspeeding, idling, GPS loss, overheating, braking)
- Driver behavior scoring
- Manual + automated QA testing with Pytest
- Firmware-style log stub in C
- Log storage in both JSON and SQLite
- SQL analytics and Pytest-based query validation
- Optional Streamlit dashboard for visualization

---

## ▶ How to Run

### 1. Simulate Logs & Save to JSON + SQLite
```bash
python eld_simulator/simulate_eld.py
