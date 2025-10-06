from fastapi import APIRouter, status

from app.controllers.v1.qrcode_controller import QRCodeController
from app.schemas.qrcode import QRCodeRequest, QRCodeResponse

router = APIRouter(tags=["qrcode"])


@router.post("/qrcode", response_model=QRCodeResponse, status_code=status.HTTP_201_CREATED)
async def gerar_qrcode(qrcode: QRCodeRequest):
    """
    Generate a QR Code for payment

    Args:
        qrcode: QR Code generation data

    Returns:
        QRCodeResponse: Generated QR Code information
    """
    return QRCodeController.gerar_qrcode(qrcode)
