"""
Acesso Router v2 - Browser automation version
"""
from typing import Any, Dict

from fastapi import APIRouter

from app.controllers.v2.acesso_controller import AcessoController as AcessoControllerV2
from app.schemas.acesso import AcessoRequest

router = APIRouter()


@router.post("/acesso", response_model=None)
async def fazer_acesso_v2(acesso_data: AcessoRequest) -> Dict[str, Any]:
    """
    V2: Validar CPF, CNPJ ou Email usando automação de navegador

    Usa Playwright para simular interação real do usuário.

    Args:
        acesso_data: Dados de acesso (username)

    Returns:
        Dict com resultado da validação

    Examples:
        ```json
        {
            "username": "123.456.789-09"
        }
        ```

        ```json
        {
            "username": "12.345.678/0001-90"
        }
        ```

        ```json
        {
            "username": "usuario@example.com"
        }
        ```
    """
    return await AcessoControllerV2.fazer_login(acesso_data)
