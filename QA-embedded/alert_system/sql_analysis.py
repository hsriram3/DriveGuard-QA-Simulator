import sqlite3

def get_average_speed():
    conn = sqlite3.connect("storage/log_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(speed) FROM logs WHERE engine_on = 1 AND speed > 0")
    avg_speed = cursor.fetchone()[0]

    conn.close()
    return avg_speed


def get_highest_engine_temp():
    conn = sqlite3.connect("storage/log_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(engine_temp) FROM logs")
    max_temp = cursor.fetchone()[0]

    conn.close()
    return max_temp


def get_idle_events():
    conn = sqlite3.connect("storage/log_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM logs WHERE idle_time >= 900")
    count = cursor.fetchone()[0]

    conn.close()
    return count
