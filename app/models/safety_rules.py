REQUIRED_EQUIPMENT = {"helmet", "vest"}

def safety_check(detections):
    detected_items = {d["class_name"].lower() for d in detections}

    missing = REQUIRED_EQUIPMENT - detected_items

    return {
        "compliant": len(missing) == 0,
        "missing_equipment": list(missing),
        "detected_items": list(detected_items)
    }
