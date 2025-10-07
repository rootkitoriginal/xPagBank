"""
Models for authentication/access
"""
from pydantic import BaseModel, Field
from typing import Optional


class AcessoRequest(BaseModel):
    """Request model for login"""
    username: str = Field(..., description="CPF, CNPJ ou Email do usuário")
    password: Optional[str] = Field(None, description="Senha do usuário")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "12345678900",
                "password": "senha123"
            }
        }
