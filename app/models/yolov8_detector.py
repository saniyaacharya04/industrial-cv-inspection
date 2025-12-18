from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = Path("weights/yolov8n.pt")

model = YOLO(MODEL_PATH)

def detect_objects(image_path: str):
    results = model(image_path, verbose=False)

    detections = []
    for r in results:
        for box in r.boxes:
            detections.append({
                "class_id": int(box.cls[0]),
                "class_name": model.names[int(box.cls[0])],
                "confidence": float(box.conf[0]),
                "bbox": [float(x) for x in box.xyxy[0]]
            })

    return detections
