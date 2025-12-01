from fastapi import FastAPI, UploadFile
import shutil
import os

from model.detect import detect_objects
from model.ocr import extract_text
from model.safety import safety_check

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Industrial CV Inspection API is running"}

@app.post("/inspect/")
async def inspect_image(file: UploadFile):
    image_path = f"data/{file.filename}"

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    detections = detect_objects(image_path)
    ocr_text = extract_text(image_path)
    safety_status = safety_check(detections)

    return {
        "detections": detections,
        "ocr_text": ocr_text,
        "safety_status": safety_status
    }
