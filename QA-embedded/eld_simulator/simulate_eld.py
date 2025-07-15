import json
from datetime import datetime, timedelta
import random
import sqlite3

logs = []
start_time = datetime.now()

for i in range(12):  # or pass via argparse
    speed = 0 if random.random() < 0.1 else random.randint(40, 85)

    log = {
        "timestamp": (start_time + timedelta(minutes=i * 5)).isoformat(),
        "engine_on": random.choice([True, True, True, False]),
        "speed": speed,
        "odometer": 15000 + i * 2.3,
        "brake_applied": random.choice([False, False, True]),
        "gps_location": None if random.random() < 0.1 else [42.88 + i * 0.001, -78.87 + i * 0.001],
        "engine_temp": random.randint(190, 230),
        "idle_time": 900 if speed == 0 else 0,
        "driver_id": "DR123"
    }

    logs.append(log)

# Store to JSON
with open('storage/logs.json', 'w') as f:
    json.dump(logs, f, indent=2)

# Store to SQLite
conn = sqlite3.connect("storage/log_db.sqlite")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    timestamp TEXT,
    engine_on BOOLEAN,
    speed INTEGER,
    odometer REAL,
    brake_applied BOOLEAN,
    gps_lat REAL,
    gps_lon REAL,
    engine_temp INTEGER,
    idle_time INTEGER,
    driver_id TEXT
)
''')

for log in logs:
    gps_lat, gps_lon = (None, None)
    if log["gps_location"]:
        gps_lat, gps_lon = log["gps_location"]

    cursor.execute('''
        INSERT INTO logs (timestamp, engine_on, speed, odometer, brake_applied,
                          gps_lat, gps_lon, engine_temp, idle_time, driver_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        log["timestamp"], log["engine_on"], log["speed"], log["odometer"],
        log["brake_applied"], gps_lat, gps_lon, log["engine_temp"],
        log["idle_time"], log["driver_id"]
    ))

conn.commit()
conn.close()

print("Logs saved to logs.json and log_db.sqlite")
