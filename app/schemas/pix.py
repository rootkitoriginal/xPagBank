from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PixRequest(BaseModel):
    """Schema for PIX transaction request"""

    chave_destino: str = Field(
        ...,
        description="Chave PIX do destinatário (CPF, email, telefone ou chave aleatória)",
    )
    valor: Decimal = Field(..., gt=0, description="Valor em reais")
    descricao: Optional[str] = Field(None, max_length=200, description="Descrição da transferência")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "chave_destino": "maria.silva@email.com",
                "valor": 250.00,
                "descricao": "Transferência PIX",
            }
        }
    )


class PixResponse(BaseModel):
    """Schema for PIX transaction response"""

    transacao_id: str = Field(..., description="ID único da transação")
    status: str = Field(default="aguardando_confirmacao", description="Status da transação")
    valor: Decimal = Field(..., description="Valor transferido")
    chave_destino: str = Field(..., description="Chave PIX de destino")
    codigo_confirmacao: str = Field(..., description="Código para confirmar a transação")
