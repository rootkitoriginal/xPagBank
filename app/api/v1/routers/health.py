from fastapi import APIRouter
from app.schemas.health import HealthResponse
from app.controllers.health_controller import HealthController

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint
    
    Returns:
        HealthResponse: API health status
    """
    return HealthController.check_health()
