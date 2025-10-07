"""
Response parser utilities
"""
from typing import Dict, Any, Optional


class ResponseParser:
    """Utility class for parsing and normalizing responses"""

    @staticmethod
    def normalize_response(
        success: bool,
        message: str,
        data: Optional[Dict[str, Any]] = None,
        source: str = "api"
    ) -> Dict[str, Any]:
        """
        Normalize response format
        
        Args:
            success: Whether the operation was successful
            message: Response message
            data: Additional data to include in response
            source: Source of the response (api, browser, etc.)
            
        Returns:
            Normalized response dictionary
        """
        response = {
            "success": success,
            "message": message,
            "source": source
        }
        
        if data:
            response["data"] = data
            
        return response

    @staticmethod
    def validation_error(message: str) -> Dict[str, Any]:
        """
        Create a validation error response
        
        Args:
            message: Error message
            
        Returns:
            Validation error response
        """
        return ResponseParser.normalize_response(
            success=False,
            message=message,
            source="validation"
        )

    @staticmethod
    def timeout_error(source: str = "api") -> Dict[str, Any]:
        """
        Create a timeout error response
        
        Args:
            source: Source of the timeout
            
        Returns:
            Timeout error response
        """
        return ResponseParser.normalize_response(
            success=False,
            message="Operação expirou. Por favor, tente novamente.",
            source=source
        )

    @staticmethod
    def generic_error(error: Exception, source: str = "api") -> Dict[str, Any]:
        """
        Create a generic error response
        
        Args:
            error: Exception that occurred
            source: Source of the error
            
        Returns:
            Generic error response
        """
        return ResponseParser.normalize_response(
            success=False,
            message=f"Erro: {str(error)}",
            data={
                "error_type": type(error).__name__,
                "error_details": str(error)
            },
            source=source
        )
