from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str = Field(..., min_length=3, description="Login PagBank do cliente")
    password: str = Field(..., min_length=3, description="Senha PagBank do cliente")
    headless: Optional[bool] = Field(
        None,
        description="Força execução headless/headful; se omitido usa configuração padrão.",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "username": "cliente123",
                "password": "senhaSegura!",
                "headless": False,
            }
        }


class LoginResponse(BaseModel):
    success: bool = Field(..., description="True quando o fluxo completou sem erros")
    username: str = Field(..., description="Usuário utilizado no login")
    screenshot: Optional[str] = Field(
        None, description="Caminho relativo do screenshot gerado durante o fluxo"
    )
    cookies_count: int = Field(
        0,
        description="Quantidade de cookies salvos no arquivo de saída",
        ge=0,
    )
    cookies_file: Optional[str] = Field(
        None, description="Arquivo de cookies em JSON salvo após o login"
    )
    error: Optional[str] = Field(
        None, description="Mensagem de erro amigável quando success for False"
    )