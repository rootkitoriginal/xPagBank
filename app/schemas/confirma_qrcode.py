from typing import Optional

from pydantic import BaseModel


class ConfirmaQRCodeRequest(BaseModel):
    """Schema for QR Code confirmation request"""

    qrcode_id: str
    codigo_confirmacao: str


class ConfirmaQRCodeResponse(BaseModel):
    """Schema for QR Code confirmation response"""

    sucesso: bool
    mensagem: str
    transacao_id: Optional[str] = None
