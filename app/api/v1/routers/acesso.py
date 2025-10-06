from typing import Any, Dict

from fastapi import APIRouter

from app.controllers.acesso_controller import AcessoController
from app.schemas.acesso import AcessoRequest

router = APIRouter(tags=["acesso"])


@router.post(
    "/acesso",
    response_model=Dict[str, Any],
    summary="Login / Autenticação",
    description="Valida CPF, CNPJ ou Email e consulta API do PagBank.",
    response_description="Resposta da API do PagBank",
)
async def fazer_login(acesso: AcessoRequest) -> Dict[str, Any]:
    """
    Valida se o username é CPF, CNPJ ou Email válido e faz requisição na API do PagBank.

    Retorna False se o username não for válido.
    """
    return await AcessoController.fazer_login(acesso)
