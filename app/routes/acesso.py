"""
Routes for access/authentication endpoints
"""
from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from app.models import AcessoRequest
from app.controllers import AcessoController

router = APIRouter()


@router.post("/login", response_model=Dict[str, Any])
async def login(acesso_data: AcessoRequest) -> Dict[str, Any]:
    """
    Login endpoint using browser automation
    
    Args:
        acesso_data: Login credentials (username and optional password)
        
    Returns:
        Response with login status and information
    """
    try:
        result = await AcessoController.fazer_login(acesso_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
