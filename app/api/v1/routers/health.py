from fastapi import APIRouter

from app.controllers.health_controller import HealthController
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint

    Returns:
        HealthResponse: API health status
    """
    return HealthController.check_health()
