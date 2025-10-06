from pydantic import BaseModel, ConfigDict, Field


class AcessoRequest(BaseModel):
    """Schema for access/login request"""

    username: str = Field(..., description="CPF, CNPJ ou Email do usuário")

    model_config = ConfigDict(json_schema_extra={"example": {"username": "123.456.789-00"}})


class AcessoResponse(BaseModel):
    """Schema for access/login response"""

    access_token: str = Field(..., description="Token JWT de acesso")
    token_type: str = Field(default="bearer", description="Tipo do token")
    usuario_id: int = Field(..., description="ID do usuário")
    nome: str = Field(..., description="Nome do usuário")
