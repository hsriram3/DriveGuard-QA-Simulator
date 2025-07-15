# Manual Test Cases

## Test Case 1: Log File Format
- **Pre-condition**: Simulate logs using `simulate_eld.py`
- **Check**: JSON format, contains timestamp, speed, engine_on
- **Expected**: All keys present, no errors
- **Status**: PASS

## Test Case 2: Overspeed Alert Trigger
- **Input**: Speed = 80 mph
- **Expected Output**: Alert with type "Overspeeding"
- **Status**: PASS/FAIL

## Test Case 3: Driver Score Accuracy
- **Check**: Score reduces by 5 for each violation
- **Expected**: Score = 100 - (violations × 5)