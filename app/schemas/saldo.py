from pydantic import BaseModel, Field
from decimal import Decimal


class SaldoResponse(BaseModel):
    """Schema for balance inquiry response"""
    usuario_id: int = Field(..., description="ID do usuário")
    saldo_disponivel: Decimal = Field(..., description="Saldo disponível para uso")
    saldo_bloqueado: Decimal = Field(..., description="Saldo bloqueado/reservado")
    saldo_total: Decimal = Field(..., description="Saldo total (disponível + bloqueado)")
