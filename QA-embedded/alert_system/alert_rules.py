# #defining rules logic for detecting speeding violations
# def check_alerts(logs):
#     alerts = []
#     for log in logs:
#         #the ticket is given only if the speed is above 70 miles
#         if log["speed"] > 70:
#             alerts.append({
#                 "timestamp": log["timestamp"],
#                 "alert": "Overspeeding",
#                 "speed": log["speed"]
#             })
#     return alerts
def check_alerts(logs):
    alerts = []

    for i, log in enumerate(logs):
        if log.get("speed", 0) > 70:
            alerts.append({"timestamp": log["timestamp"], "alert": "Overspeeding", "speed": log["speed"]})

        if log.get("idle_time", 0) >= 900:
            alerts.append({"timestamp": log["timestamp"], "alert": "Excessive Idling"})

        if log.get("engine_temp", 0) > 220:
            alerts.append({"timestamp": log["timestamp"], "alert": "Engine Overheating"})

        if log.get("gps_location") is None:
            alerts.append({"timestamp": log["timestamp"], "alert": "GPS Signal Lost"})

        if i > 0:
            prev_speed = logs[i-1].get("speed", 0)
            if log.get("brake_applied") and (prev_speed - log["speed"]) > 20:
                alerts.append({"timestamp": log["timestamp"], "alert": "Harsh Braking"})

    return alerts
