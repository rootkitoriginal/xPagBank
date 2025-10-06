from fastapi import APIRouter
from app.schemas.confirma_qrcode import ConfirmaQRCodeRequest, ConfirmaQRCodeResponse
from app.controllers.confirma_qrcode_controller import ConfirmaQRCodeController

router = APIRouter(tags=["qrcode"])


@router.post("/confirmaqrcode", response_model=ConfirmaQRCodeResponse)
async def confirmar_qrcode(confirmacao: ConfirmaQRCodeRequest):
    """
    Confirm a QR Code transaction
    
    Args:
        confirmacao: Confirmation data
        
    Returns:
        ConfirmaQRCodeResponse: Confirmation result
    """
    return ConfirmaQRCodeController.confirmar_qrcode(confirmacao)
