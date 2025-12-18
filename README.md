# Industrial CV Inspection Platform

End-to-end industrial safety and asset inspection system using Computer Vision (YOLOv8 + OCR), built as a production-ready FastAPI service.

---

## Overview

Industrial safety inspections are traditionally manual, slow, and error-prone.
This project demonstrates a real-world Computer Vision inspection pipeline that:

* Detects safety equipment and assets using YOLOv8
* Extracts textual information using OCR
* Applies safety compliance rules
* Generates structured inspection reports
* Exposes a clean, scalable REST API
* Runs locally or via Docker with reproducible setup

The system is designed to closely resemble industrial AI inspection services used in production environments.

---

## Key Features

### Free Tier (Fully Implemented)

* Image upload inspection API
* YOLOv8 object detection
* ROI-based OCR for improved text accuracy
* Safety compliance checks (helmet, vest)
* End-to-end inference latency metrics
* Detection count metrics
* Structured JSON inspection report
* FastAPI backend
* Health check endpoint
* Structured logging using Loguru
* Unit tests with Pytest
* End-to-end validation script
* Dockerized deployment
* Makefile for standardized commands

### Premium Tier (Placeholders Only)

* Video inspection
* Analytics dashboard
* Multi-site inspection
* Alerts and monitoring

Premium endpoints are intentionally locked and return upgrade-required responses. No premium business logic is implemented.

---

## System Architecture

```
FastAPI Application
 ├── API Routes
 │    ├── /inspect
 │    ├── /health
 │    └── /premium/*
 │
 ├── Services (Business Logic)
 │    ├── Detection Service
 │    ├── OCR Service
 │    ├── Safety Rules Engine
 │    └── Report Builder
 │
 ├── Models (ML Inference)
 │    ├── YOLOv8 Detector
 │    ├── OCR Engine
 │    └── Safety Rules
 │
 ├── Evaluation
 │    └── Metrics (Latency, Detection Count)
 │
 └── Core
      └── Logging and Configuration
```

The architecture enforces clear separation of concerns and is designed for scalability and maintainability.

---

## Tech Stack

| Layer                  | Technology           |
| ---------------------- | -------------------- |
| Backend API            | FastAPI              |
| Object Detection       | YOLOv8 (Ultralytics) |
| OCR                    | Tesseract            |
| Image Processing       | OpenCV               |
| Logging                | Loguru               |
| Testing                | Pytest               |
| Containerization       | Docker               |
| Environment Management | Conda                |

---

## Project Structure

```
app/
├── api/            # FastAPI routes
├── services/       # Business logic
├── models/         # ML inference logic
├── evaluation/     # Metrics and evaluation
├── core/           # Logging and config
├── utils/          # File and image utilities
tests/              # Unit tests
scripts/            # End-to-end validation
docker/             # Dockerfile
weights/            # YOLO model weights
```

---

## Running Locally

### Activate Conda Environment

```bash
conda activate industrial-cv
```

### Run the API

```bash
make run
```

Open API documentation at:

```
http://127.0.0.1:8000/docs
```

---

## Testing

Run unit tests:

```bash
make test
```

Run end-to-end validation:

```bash
make e2e
```

---

## Docker

Build and run the container:

```bash
make docker
make docker-run
```

The API will be available at:

```
http://localhost:8000/docs
```

---

## Premium Feature Behavior

Premium endpoints intentionally return locked responses:

```json
{
  "detail": "Premium Feature – Upgrade Required"
}
```

This simulates SaaS feature gating without implementing paid logic.

---

## Metrics Captured

* End-to-end inference latency (milliseconds)
* Number of detected objects per inspection

These metrics are returned as part of the inspection response.

---

## Design Decisions and Trade-offs

* No database is used to keep the system stateless and focused on inference.
* Authentication is omitted to keep the MVP scope realistic for a 1–2 day build.
* Video processing and analytics are scoped as premium features.
* Safety rules are rule-based for explainability and simplicity.

All trade-offs are intentional and clearly documented.

---

## Future Enhancements

* Video stream inspection
* Model fine-tuning workflows
* Persistent storage and analytics
* Role-based authentication
* Edge deployment on Jetson or Raspberry Pi

---

## Author

Saniya Acharya
B.Tech Computer Science Engineering (2026)
Focus Areas: Industrial AI, Computer Vision, Machine Vision, ML Systems

---

## License

MIT License


