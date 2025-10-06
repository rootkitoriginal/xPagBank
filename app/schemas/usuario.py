from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime


class UsuarioBase(BaseModel):
    """Base schema for Usuario"""
    nome: str = Field(..., min_length=3, max_length=100, description="Nome completo do usuário")
    email: EmailStr = Field(..., description="Email válido do usuário")
    cpf: str = Field(..., min_length=11, max_length=14, description="CPF do usuário (apenas números)")
    telefone: Optional[str] = Field(None, description="Telefone com DDD")


class UsuarioCreate(UsuarioBase):
    """Schema for creating a new usuario"""
    senha: str = Field(..., min_length=6, description="Senha com no mínimo 6 caracteres")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nome": "João Silva",
                "email": "joao.silva@email.com",
                "cpf": "12345678901",
                "telefone": "11987654321",
                "senha": "senha123"
            }
        }
    )


class UsuarioResponse(UsuarioBase):
    """Schema for usuario response"""
    id: int
    ativo: bool = True
    data_criacao: datetime
    
    class Config:
        from_attributes = True
