import json
from alert_system.alert_rules import check_alerts

def test_idle_alert_trigger():
    with open("storage/logs.json") as f:
        logs = json.load(f)
    alerts = check_alerts(logs)
    assert any(a["alert"] == "Excessive Idling" for a in alerts)

def test_harsh_brake_alert():
    with open("storage/logs.json") as f:
        logs = json.load(f)
    alerts = check_alerts(logs)
    assert any(a["alert"] == "Harsh Braking" for a in alerts)

def test_overheat_alert():
    with open("storage/logs.json") as f:
        logs = json.load(f)
    alerts = check_alerts(logs)
    assert any(a["alert"] == "Engine Overheating" for a in alerts)
