from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Schema for health check response"""
    status: str = "healthy"
    version: str
    service: str
