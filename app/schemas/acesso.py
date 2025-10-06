from pydantic import BaseModel, EmailStr, Field, ConfigDict


class AcessoRequest(BaseModel):
    """Schema for access/login request"""
    email: EmailStr = Field(..., description="Email do usuário")
    senha: str = Field(..., description="Senha do usuário")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "joao.silva@email.com",
                "senha": "senha123"
            }
        }
    )


class AcessoResponse(BaseModel):
    """Schema for access/login response"""
    access_token: str = Field(..., description="Token JWT de acesso")
    token_type: str = Field(default="bearer", description="Tipo do token")
    usuario_id: int = Field(..., description="ID do usuário")
    nome: str = Field(..., description="Nome do usuário")
