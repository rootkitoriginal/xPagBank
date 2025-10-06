from fastapi import APIRouter

from app.controllers.confirma_pix_controller import ConfirmaPixController
from app.schemas.confirma_pix import ConfirmaPixRequest, ConfirmaPixResponse

router = APIRouter(tags=["pix"])


@router.post("/confirma_pix", response_model=ConfirmaPixResponse)
async def confirmar_pix(confirmacao: ConfirmaPixRequest):
    """
    Confirm a PIX transaction

    Args:
        confirmacao: Confirmation data

    Returns:
        ConfirmaPixResponse: Confirmation result
    """
    return ConfirmaPixController.confirmar_pix(confirmacao)
