from app.models.safety_rules import safety_check

def run_safety_check(detections):
    return safety_check(detections)
