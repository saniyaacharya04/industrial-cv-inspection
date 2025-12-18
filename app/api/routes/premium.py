from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/video-inspection")
def video_inspection():
    raise HTTPException(
        status_code=402,
        detail="Premium Feature – Upgrade Required"
    )

@router.get("/analytics")
def analytics_dashboard():
    raise HTTPException(
        status_code=402,
        detail="Premium Feature – Upgrade Required"
    )
