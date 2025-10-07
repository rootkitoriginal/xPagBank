from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="PagBank Automation API")
app.include_router(router)

@app.get("/health")
async def health():
    return {"status": "ok"}