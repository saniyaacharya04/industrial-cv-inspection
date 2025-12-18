from app.models.ocr_engine import extract_text

def run_ocr(image_path: str, detections=None):
    return extract_text(image_path, detections)
