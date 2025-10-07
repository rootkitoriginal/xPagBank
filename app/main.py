"""
FastAPI application for PagBank automation
"""
from fastapi import FastAPI
from app.routes import acesso

app = FastAPI(
    title="xPagBank API",
    description="PagBank automation API with Playwright",
    version="1.0.0"
)

# Include routers
app.include_router(acesso.router, prefix="/api/v1", tags=["acesso"])

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "xPagBank API is running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}
