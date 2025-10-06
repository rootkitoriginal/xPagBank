"""
Utilitários para parsear e normalizar respostas das APIs do PagBank
"""
from typing import Any, Dict, Optional


class ResponseParser:
    """Parser para normalizar respostas de diferentes fontes"""

    @staticmethod
    def normalize_response(
        success: bool,
        message: str,
        data: Optional[Any] = None,
        status_code: Optional[int] = None,
        cookies: Optional[Dict[str, str]] = None,
        source: str = "api",
    ) -> Dict[str, Any]:
        """
        Normaliza respostas em um formato padrão

        Args:
            success: Se a operação foi bem sucedida
            message: Mensagem descritiva
            data: Dados retornados
            status_code: Código HTTP (se aplicável)
            cookies: Cookies da sessão
            source: Origem da resposta (api, browser, etc)

        Returns:
            Dict padronizado com a resposta
        """
        response = {
            "success": success,
            "message": message,
            "data": data,
            "source": source,
        }

        if status_code is not None:
            response["status_code"] = status_code

        if cookies:
            response["cookies"] = cookies

        return response

    @staticmethod
    def cloudflare_error(status_code: int = 403) -> Dict[str, Any]:
        """
        Retorna erro padronizado para bloqueio Cloudflare

        Args:
            status_code: Código HTTP do bloqueio

        Returns:
            Dict com erro padronizado
        """
        return ResponseParser.normalize_response(
            success=False,
            status_code=status_code,
            message=(
                "Bloqueado pelo Cloudflare. A API do PagBank "
                "está protegida e requer autenticação adicional."
            ),
            data={
                "error": "cloudflare_protection",
                "detail": (
                    "A requisição foi bloqueada pelo sistema de " "proteção Cloudflare do PagBank"
                ),
            },
        )

    @staticmethod
    def timeout_error(source: str = "api") -> Dict[str, Any]:
        """
        Retorna erro padronizado para timeout

        Args:
            source: Origem da requisição

        Returns:
            Dict com erro padronizado
        """
        return ResponseParser.normalize_response(
            success=False,
            message="Timeout ao conectar com o PagBank",
            data=None,
            source=source,
        )

    @staticmethod
    def validation_error(message: str) -> Dict[str, Any]:
        """
        Retorna erro padronizado para validação

        Args:
            message: Mensagem de erro

        Returns:
            Dict com erro padronizado
        """
        return ResponseParser.normalize_response(
            success=False,
            message=message,
            data=None,
        )

    @staticmethod
    def generic_error(error: Exception, source: str = "api") -> Dict[str, Any]:
        """
        Retorna erro padronizado para exceções genéricas

        Args:
            error: Exceção capturada
            source: Origem da requisição

        Returns:
            Dict com erro padronizado
        """
        return ResponseParser.normalize_response(
            success=False,
            message=f"Erro ao fazer requisição: {str(error)}",
            data=None,
            source=source,
        )

    @staticmethod
    def is_cloudflare_block(status_code: int, response_text: str, headers: Dict[str, str]) -> bool:
        """
        Verifica se a resposta é um bloqueio do Cloudflare

        Args:
            status_code: Código HTTP
            response_text: Corpo da resposta
            headers: Headers da resposta

        Returns:
            True se for bloqueio Cloudflare
        """
        return status_code == 403 and (
            "cloudflare" in response_text.lower()
            or "cf-ray" in headers.get("server", "").lower()
            or headers.get("server", "").lower() == "cloudflare"
        )
