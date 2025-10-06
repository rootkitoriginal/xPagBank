from pydantic import BaseModel, ConfigDict, Field


class ConfirmaPixRequest(BaseModel):
    """Schema for PIX confirmation request"""

    transacao_id: str = Field(..., description="ID da transação a ser confirmada")
    codigo_confirmacao: str = Field(..., description="Código de confirmação recebido")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "transacao_id": "abc123-def456-ghi789",
                "codigo_confirmacao": "CONF_abc123",
            }
        }
    )


class ConfirmaPixResponse(BaseModel):
    """Schema for PIX confirmation response"""

    sucesso: bool = Field(..., description="Se a confirmação foi bem sucedida")
    mensagem: str = Field(..., description="Mensagem de retorno")
    transacao_id: str = Field(..., description="ID da transação confirmada")
    status: str = Field(..., description="Novo status da transação")
