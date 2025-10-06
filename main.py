from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core import settings

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="xPagBank REST API - Sistema de pagamentos e transações",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API v1 router
app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to xPagBank API",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "redoc": "/redoc",
    }


if __name__ == "__main__":
    import uvicorn

    # Print startup information
    print("\n" + "=" * 70)
    print(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION}")
    print("=" * 70)
    print("\n📡 Servidor iniciando em: http://0.0.0.0:8874")
    print("\n📚 Documentação:")
    print("   • Swagger UI: http://localhost:8874/docs")
    print("   • ReDoc:      http://localhost:8874/redoc")
    print("\n🔗 Endpoints disponíveis:")
    print(f"   • GET  {settings.API_V1_PREFIX}/health          - Health check")
    print(f"   • POST {settings.API_V1_PREFIX}/usuario         - Criar usuário")
    print(f"   • POST {settings.API_V1_PREFIX}/acesso          - Validar CPF/CNPJ/Email")
    print(f"   • POST {settings.API_V1_PREFIX}/qrcode          - Gerar QR Code")
    print(f"   • POST {settings.API_V1_PREFIX}/confirmaqrcode  - Confirmar QR Code")
    print(f"   • GET  {settings.API_V1_PREFIX}/saldo           - Consultar saldo")
    print(f"   • POST {settings.API_V1_PREFIX}/pix             - Realizar PIX")
    print(f"   • POST {settings.API_V1_PREFIX}/confirma_pix    - Confirmar PIX")
    print("\n💡 Exemplo de uso - Endpoint /acesso:")
    print("   curl -X POST http://localhost:8874/api/v1/acesso \\")
    print("     -H 'Content-Type: application/json' \\")
    print('     -d \'{"username": "123.456.789-09"}\'')
    print("\n   Aceita: CPF, CNPJ ou Email válidos")
    print("   Retorna: {success: true/false, message: ..., data: ...}")
    print("\n" + "=" * 70 + "\n")

    uvicorn.run(app, host="0.0.0.0", port=8874)
