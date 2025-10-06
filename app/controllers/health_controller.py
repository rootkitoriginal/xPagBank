from app.core import settings
from app.schemas.health import HealthResponse


class HealthController:
    """Controller for health check operations"""

    @staticmethod
    def check_health() -> HealthResponse:
        """
        Perform health check

        Returns:
            HealthResponse: Health status information
        """
        return HealthResponse(
            status="healthy", version=settings.APP_VERSION, service=settings.APP_NAME
        )
