from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.inspection import router as inspection_router
from app.api.routes.premium import router as premium_router

app = FastAPI(title="Industrial CV Inspection API")

# Core routes
app.include_router(health_router, prefix="/health", tags=["Health"])
app.include_router(inspection_router, prefix="/inspect", tags=["Inspection"])

# Premium (locked)
app.include_router(premium_router, prefix="/premium", tags=["Premium"])

@app.get("/")
def root():
    return {"message": "Industrial CV Inspection API running"}
