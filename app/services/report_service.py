from datetime import datetime

def build_report(detections, ocr_text, safety_status):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "detections": detections,
        "ocr_text": ocr_text,
        "safety_status": safety_status
    }
