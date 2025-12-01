def safety_check(detections):
    has_person = any(d["label"] == "person" for d in detections)
    has_helmet = any(d["label"] == "helmet" for d in detections)

    if has_person and not has_helmet:
        return "SAFETY VIOLATION: Helmet Missing"
    return "Safety Compliant"
