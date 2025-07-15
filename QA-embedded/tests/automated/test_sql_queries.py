from alert_system.sql_analysis import (
    get_average_speed,
    get_highest_engine_temp,
    get_idle_events
)

def test_average_speed():
    avg_speed = get_average_speed()
    assert avg_speed is not None, "Average speed query failed (returned None)"
    assert avg_speed >= 0, "Average speed should not be negative"

def test_max_engine_temp():
    max_temp = get_highest_engine_temp()
    assert max_temp is not None, "Max engine temperature query failed"
    assert 190 <= max_temp <= 300, "Engine temp seems out of expected range"

def test_idle_event_count():
    idle_count = get_idle_events()
    assert idle_count >= 0, "Idle event count should be 0 or greater"
