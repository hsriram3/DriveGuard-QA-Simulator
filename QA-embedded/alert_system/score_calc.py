# to calculate the score of the driver based on the number of alerts
def calculate_driver_score(logs):
    violations = sum(1 for log in logs if log["speed"] > 70)
    score = max(0, 100 - violations * 5)
    return score