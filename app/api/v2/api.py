"""
API v2 Router Aggregator - Browser automation version
"""
from fastapi import APIRouter

from app.api.v2.routers import acesso

api_router = APIRouter()

# Include all v2 routers
api_router.include_router(acesso.router, tags=["Acesso V2 (Browser)"])
