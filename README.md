---

# Industrial Safety & Asset Inspection using Computer Vision

This project implements a real-time industrial safety and asset inspection system using Computer Vision, Object Detection, OCR, and a RESTful API for automated safety compliance and monitoring.

The system is designed to simulate how industrial AI platforms monitor worker safety, extract equipment information, and perform visual inspection in manufacturing environments.

---

## Features
- Real-time object detection using YOLOv8
- OCR-based extraction of equipment labels and meter readings using Tesseract
- Automated safety compliance logic (helmet and person detection)
- REST API developed using FastAPI
- Live API testing using Swagger UI
- Real-time inference with latency measurement
- Docker-ready deployment architecture

---

## Technology Stack
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- Tesseract OCR
- EasyOCR
- FastAPI
- Scikit-learn
- Docker
- Git

---

## Local Setup

### Install Dependencies
```bash
pip install -r requirements.txt
````

### Run Local Inference

```bash
python run_local.py
```

### Run API Server

```bash
uvicorn api.main:app --reload
```

Access Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST /inspect/

Uploads an image and returns detection results, OCR text, and safety status.

**Request:**
Multipart form-data with an image file.

**Response Example:**

```json
{
  "detections": [
    { "label": "person", "confidence": 0.91 }
  ],
  "ocr_text": "Sample Equipment Text",
  "safety_status": "SAFETY VIOLATION: Helmet Missing"
}
```

---

## Performance

* YOLOv8 inference latency: approximately 30–36 ms per image on CPU
* API tested using Swagger UI and curl

---

## Use Case

This system simulates:

* Worker safety compliance monitoring
* Equipment label and meter reading extraction
* Visual inspection of industrial assets

---

## Project Status

Production-ready prototype with active development for benchmarking automation and containerized deployment.

---

## Author

Saniya Acharya

````

---
