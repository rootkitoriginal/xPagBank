# HTTP Client - Exemplos de Uso

Este documento demonstra como usar o `PagBankHttpClient` para fazer requisições HTTP.

## Características

- ✅ **Métodos HTTP**: GET, POST, PUT, DELETE, HEAD
- ✅ **Base URL Configurável**: Default `https://pagbank.com.br`
- ✅ **Gerenciamento de Cookies**: Cookies persistem automaticamente entre requisições
- ✅ **Headers Padrão**: User-Agent, Accept, Content-Type pré-configurados
- ✅ **Headers Customizados**: Possibilidade de adicionar/sobrescrever headers
- ✅ **Timeout Configurável**: Default 30 segundos

## Instalação

```bash
# O httpx já está nas dependências do projeto
pip install httpx
```

## Exemplos Básicos

### 1. Requisição GET Simples

```python
from app.services.http_client import PagBankHttpClient

# Cria o cliente
client = PagBankHttpClient()

# Faz uma requisição GET
response = await client.get("/api/v1/users")
print(response.status_code)
print(response.json())
```

### 2. Requisição POST com JSON

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient(base_url="https://api.pagbank.com.br")

# Envia dados JSON
response = await client.post(
    path="/api/v1/login",
    json={"username": "user@example.com", "password": "secret"}
)

data = response.json()
print(data)
```

### 3. Requisição PUT para Atualização

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Atualiza um recurso
response = await client.put(
    path="/api/v1/users/123",
    json={"name": "New Name", "email": "newemail@example.com"}
)

print(response.status_code)
```

### 4. Requisição DELETE

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Deleta um recurso
response = await client.delete("/api/v1/users/123")
print(f"Deleted: {response.status_code == 204}")
```

### 5. Requisição HEAD (Verificar Existência)

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Verifica se recurso existe sem baixar o corpo
response = await client.head("/api/v1/users/123")
print(f"Exists: {response.status_code == 200}")
print(f"Content-Length: {response.headers.get('content-length')}")
```

## Gerenciamento de Cookies

### Cookies Automáticos (Padrão)

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Primeira requisição - recebe cookies
response1 = await client.post(
    path="/api/v1/login",
    json={"username": "user@example.com", "password": "secret"}
)

# Cookies são armazenados automaticamente
print(client.get_cookies())

# Segunda requisição - reutiliza cookies automaticamente
response2 = await client.get("/api/v1/profile")
# Os cookies de sessão são enviados automaticamente!
```

### Inicializar Cookies Manualmente

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Define cookies iniciais
client.init_cookies({
    "session_id": "abc123",
    "user_token": "xyz789"
})

# Todas as requisições usarão esses cookies
response = await client.get("/api/v1/profile")
```

### Desabilitar Cookies em uma Requisição

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Não usa cookies armazenados
response = await client.get(
    path="/api/v1/public-data",
    use_cookies=False
)
```

### Limpar Cookies

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Limpa todos os cookies
client.clear_cookies()
```

## Headers Customizados

### Headers Padrão Globais

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Define um header padrão para todas as requisições
client.set_header("Authorization", "Bearer token123")
client.set_header("X-Custom-Header", "custom-value")

# Todas as requisições usarão esses headers
response = await client.get("/api/v1/protected")
```

### Headers Específicos por Requisição

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Headers apenas para esta requisição
custom_headers = {
    "Authorization": "Bearer token123",
    "X-Request-ID": "req-abc-123"
}

response = await client.get(
    path="/api/v1/data",
    headers=custom_headers
)
```

### Remover Header Padrão

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Remove um header padrão
client.remove_header("user-agent")
```

## Configuração da Base URL

### Base URL Padrão (PagBank)

```python
from app.services.http_client import PagBankHttpClient

# Usa https://pagbank.com.br como base
client = PagBankHttpClient()

response = await client.get("/api/v1/users")
# Faz requisição para: https://pagbank.com.br/api/v1/users
```

### Base URL Customizada

```python
from app.services.http_client import PagBankHttpClient

# Define outra base URL
client = PagBankHttpClient(base_url="https://api.example.com")

response = await client.get("/v2/data")
# Faz requisição para: https://api.example.com/v2/data
```

### URL Completa (Sobrescreve Base URL)

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Passa URL completa - ignora base_url
response = await client.get("https://api.other-service.com/data")
# Faz requisição para: https://api.other-service.com/data
```

## Timeout Configurável

```python
from app.services.http_client import PagBankHttpClient

# Timeout de 60 segundos
client = PagBankHttpClient(timeout=60.0)

# Timeout de 5 segundos para requisições rápidas
fast_client = PagBankHttpClient(timeout=5.0)
```

## Query Parameters

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# GET com query parameters
params = {
    "page": 2,
    "limit": 20,
    "sort": "name"
}

response = await client.get("/api/v1/users", params=params)
# Faz requisição para: /api/v1/users?page=2&limit=20&sort=name
```

## Form Data (POST)

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

# Envia form data (application/x-www-form-urlencoded)
form_data = {
    "username": "user123",
    "password": "secret"
}

response = await client.post("/api/v1/login", data=form_data)
```

## Exemplo Completo: Fluxo de Login com Sessão

```python
from app.services.http_client import PagBankHttpClient

async def login_and_get_profile():
    # Cria cliente
    client = PagBankHttpClient(
        base_url="https://api.pagbank.com.br",
        timeout=30.0
    )

    # 1. Faz login
    login_response = await client.post(
        path="/api/v1/login",
        json={
            "username": "user@example.com",
            "password": "secret123"
        }
    )

    if login_response.status_code != 200:
        return {"error": "Login failed"}

    # Cookies de sessão foram armazenados automaticamente!
    print("Session cookies:", client.get_cookies())

    # 2. Busca perfil do usuário (usa cookies da sessão)
    profile_response = await client.get("/api/v1/profile")
    profile_data = profile_response.json()

    # 3. Atualiza dados do perfil (ainda usa cookies da sessão)
    update_response = await client.put(
        path="/api/v1/profile",
        json={"name": "New Name"}
    )

    # 4. Faz logout
    logout_response = await client.post("/api/v1/logout")

    # 5. Limpa cookies
    client.clear_cookies()

    return profile_data

# Uso
result = await login_and_get_profile()
print(result)
```

## Tratamento de Erros

```python
from app.services.http_client import PagBankHttpClient

client = PagBankHttpClient()

try:
    response = await client.get("/api/v1/data")

    if response.status_code == 200:
        data = response.json()
        print("Success:", data)
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        print("Forbidden - check Cloudflare protection")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

except Exception as e:
    if "timeout" in str(e).lower():
        print("Request timeout")
    else:
        print(f"Error: {str(e)}")
```

## Integração com FastAPI

```python
from fastapi import APIRouter, HTTPException
from app.services.http_client import PagBankHttpClient

router = APIRouter()

@router.post("/api/v1/validate")
async def validate_user(username: str):
    client = PagBankHttpClient(
        base_url="https://api.security.pagbank.com.br"
    )

    try:
        response = await client.post(
            path="/usernames",
            json={"username": username}
        )

        if response.status_code == 403:
            raise HTTPException(
                status_code=403,
                detail="Blocked by Cloudflare protection"
            )

        return response.json()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"API Error: {str(e)}"
        )
```

## Comparação: Antes vs Depois

### ❌ Antes (httpx diretamente)

```python
async def fazer_login(username: str):
    url = "https://api.security.pagbank.com.br/usernames"
    headers = {
        "accept": "application/json",
        "user-agent": "...",
        "content-type": "application/json",
        # ... muitos headers
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json={"username": username}, headers=headers)
        # Sem gerenciamento de cookies
        # Headers repetidos em cada requisição
        return response.json()
```

### ✅ Depois (com PagBankHttpClient)

```python
async def fazer_login(username: str):
    client = PagBankHttpClient(
        base_url="https://api.security.pagbank.com.br"
    )

    # Headers padrão já configurados
    # Cookies gerenciados automaticamente
    response = await client.post(
        path="/usernames",
        json={"username": username}
    )
    return response.json()
```

## Benefícios

1. **Código Mais Limpo**: Menos boilerplate, foco na lógica de negócio
2. **Reutilização**: Cookies e headers são mantidos entre requisições
3. **Configuração Centralizada**: Base URL e timeout configurados uma vez
4. **Manutenibilidade**: Mudanças nos headers padrão em um único lugar
5. **Flexibilidade**: Suporta todos os métodos HTTP e configurações customizadas

## Referências

- [httpx Documentation](https://www.python-httpx.org/)
- [FastAPI Async Operations](https://fastapi.tiangolo.com/async/)
- [HTTP Methods Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
