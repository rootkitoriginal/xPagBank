# inicia.py
import requests
import json

# URL base da API (ajuste se estiver usando Docker)
API_BASE_URL = "http://127.0.0.1:8000"

def test_login_api(username: str, password: str):
    """
    Script Cliente para facilitar chamadas à API /login.
    """
    url = f"{API_BASE_URL}/login"
    payload = {"username": username, "password": password}
    
    print(f"--- Teste de Login para: {username} ---")
    try:
        response = requests.post(url, json=payload, timeout=300) # Timeout longo para a automação
        response.raise_for_status() # Lança exceção para códigos de erro HTTP
        
        print("\n✅ Sucesso:")
        print(json.dumps(response.json(), indent=4))

    except requests.exceptions.RequestException as e:
        print("\n❌ Erro na Chamada da API:")
        try:
            # Tenta obter o detalhe do erro do FastAPI
            error_detail = e.response.json().get("detail") if e.response is not None else "Sem detalhes."
            print(f"Status: {e.response.status_code if e.response is not None else 'N/A'}")
            print(f"Detalhe: {error_detail}")
        except Exception:
            print(f"Erro de Conexão: {e}")


if __name__ == "__main__":
    # 1. Health Check
    try:
        r = requests.get(f"{API_BASE_URL}/health")
        r.raise_for_status()
        print(f"✅ Health Check OK: {r.json()['status']}\n")
    except:
        print("❌ API não está rodando. Por favor, inicie o servidor (Ex: uvicorn app.main:app --reload) antes de rodar o cliente.\n")
        exit(1)
        
    # 2. Teste o endpoint de login
    test_login_api("joao_silva", "minhasenha123")
    print("-" * 50)
    test_login_api("maria_teste", "senha_outra")