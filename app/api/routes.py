from fastapi import APIRouter
from app.api.endpoints import analysis, read

router = APIRouter()
router.include_router(read.router, prefix="/api/data/read", tags=["Read"])
router.include_router(analysis.router, prefix="/api/data/analysis", tags=["Analysis"])
