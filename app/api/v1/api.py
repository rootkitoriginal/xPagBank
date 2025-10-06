from fastapi import APIRouter

from app.api.v1.routers import (
    acesso,
    confirma_pix,
    confirmaqrcode,
    health,
    pix,
    qrcode,
    saldo,
    usuario,
)

api_router = APIRouter()

# Include all v1 routers
api_router.include_router(health.router, prefix="")
api_router.include_router(usuario.router, prefix="")
api_router.include_router(acesso.router, prefix="")
api_router.include_router(qrcode.router, prefix="")
api_router.include_router(confirmaqrcode.router, prefix="")
api_router.include_router(saldo.router, prefix="")
api_router.include_router(pix.router, prefix="")
api_router.include_router(confirma_pix.router, prefix="")
