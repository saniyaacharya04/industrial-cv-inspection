from model.detect import detect_objects
from model.ocr import extract_text
from model.safety import safety_check

image_path = "data/sample.jpg"

detections = detect_objects(image_path)
text = extract_text(image_path)
status = safety_check(detections)

print("Detections:", detections)
print("OCR Text:", text)
print("Safety Status:", status)
