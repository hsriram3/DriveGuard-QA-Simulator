import json
from alert_system.alert_rules import check_alerts

def test_overspeed_alert_trigger():
    with open("storage/logs.json", "r") as f:
        logs = json.load(f)

    alerts = check_alerts(logs)

    # Filter only overspeeding alerts
    overspeed_alerts = [a for a in alerts if a["alert"] == "Overspeeding"]

    # Assert at least one overspeed alert exists (optional)
    assert overspeed_alerts, "No overspeed alerts generated"

    # Assert all overspeed alerts have speed > 70
    assert all(a["speed"] > 70 for a in overspeed_alerts), "Found overspeed alert with invalid speed"

    print("Overspeed alert test passed.")
