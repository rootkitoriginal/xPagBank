# app/main.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.browser_logic import login_and_persist

# --- Configuração ---
# O servidor pode ser configurado via variável de ambiente (ex: para o Docker)
API_VERSION = os.getenv("API_VERSION", "1.0")

app = FastAPI(
    title="Robo API", 
    version=API_VERSION,
    description="API para automação de login com Playwright robusto e persistência."
)

# --- Modelo de Dados ---
class LoginRequest(BaseModel):
    username: str
    password: str

# --- Endpoints ---

@app.get("/health")
def health_check():
    """
    ✅ Health Check para monitoramento.
    """
    return {"status": "ok", "service": "Robo-API", "version": API_VERSION}

@app.post("/login")
async def login_endpoint(request: LoginRequest):
    """
    ✅ Endpoint /login para automação de login.
    """
    
    # Limita o tamanho dos dados para evitar log muito grande
    username = request.username.strip()
    password = "..." * len(request.password.strip())
    print(f"INFO: Recebida requisição de login para o usuário: {username}")
    
    try:
        # Chama a lógica de automação
        result = await login_and_persist(request.username, request.password)
        
        if result["status"] == "error":
            # Retorno de Erros Amigáveis
            raise HTTPException(status_code=500, detail=result["message"])
            
        return result
        
    except Exception as e:
        print(f"ERRO CRÍTICO NO ENDPOINT: {e}")
        # Retorno de Erros Amigáveis
        raise HTTPException(status_code=500, detail="Erro interno ao processar a automação.")

# --- Inicialização ---
# Para rodar localmente, use: uvicorn app.main:app --reload