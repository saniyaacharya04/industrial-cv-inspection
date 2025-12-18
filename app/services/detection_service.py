from app.models.yolov8_detector import detect_objects

def run_detection(image_path: str):
    return detect_objects(image_path)
