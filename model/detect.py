from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(image_path):
    results = model(image_path)
    detected = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            detected.append({
                "label": model.names[cls],
                "confidence": round(conf, 3)
            })

    return detected
