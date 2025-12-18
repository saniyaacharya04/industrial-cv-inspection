import cv2
import pytesseract

def extract_text(image_path: str, detections=None):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    texts = []

    if detections:
        for d in detections:
            x1, y1, x2, y2 = map(int, d["bbox"])
            roi = gray[y1:y2, x1:x2]
            text = pytesseract.image_to_string(roi, config="--psm 6")
            if text.strip():
                texts.append(text.strip())
    else:
        text = pytesseract.image_to_string(gray, config="--psm 6")
        texts.append(text.strip())

    return texts
