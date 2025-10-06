from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal
from typing import Optional


class QRCodeRequest(BaseModel):
    """Schema for QR Code generation request"""
    valor: Decimal = Field(..., gt=0, description="Valor em reais")
    descricao: Optional[str] = Field(None, max_length=200, description="Descrição do pagamento")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "valor": 150.50,
                "descricao": "Pagamento de produto X"
            }
        }
    )


class QRCodeResponse(BaseModel):
    """Schema for QR Code response"""
    qrcode_id: str = Field(..., description="ID único do QR Code")
    qrcode_data: str = Field(..., description="Dados codificados do QR Code")
    valor: Decimal = Field(..., description="Valor do pagamento")
    status: str = Field(default="pendente", description="Status do QR Code")
    expira_em: str = Field(..., description="Data/hora de expiração")
