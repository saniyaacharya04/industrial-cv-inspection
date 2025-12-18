from app.core.logging import get_logger
logger = get_logger()

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.detection_service import run_detection
from app.services.ocr_service import run_ocr
from app.services.safety_service import run_safety_check
from app.services.report_service import build_report
from app.utils.file_utils import save_upload_file
from app.evaluation.metrics import MetricsTracker

router = APIRouter()

@router.post("/")
async def inspect_image(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".jpg", ".jpeg", ".png")):
        raise HTTPException(status_code=400, detail="Unsupported file type")

    try:
        image_path = save_upload_file(file)
        logger.info(f"Image saved at {image_path}")


        metrics = MetricsTracker()
        metrics.start()

        detections = run_detection(image_path)
        logger.info(f"Detections found: {len(detections)}")

        ocr_text = run_ocr(image_path, detections)
        safety_status = run_safety_check(detections)

        latency_ms = metrics.stop()

        report = build_report(
            detections=detections,
            ocr_text=ocr_text,
            safety_status=safety_status
        )

        report["metrics"] = {
            "latency_ms": latency_ms,
            "num_detections": len(detections)
        }

        return report

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
