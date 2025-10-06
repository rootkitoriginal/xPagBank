from fastapi import APIRouter

from app.controllers.acesso_controller import AcessoController
from app.schemas.acesso import AcessoRequest, AcessoResponse

router = APIRouter(tags=["acesso"])


@router.post(
    "/acesso",
    response_model=AcessoResponse,
    summary="Login / Autenticação",
    description="""
    Autentica o usuário e retorna um token de acesso.

    ## Campos obrigatórios:
    - **email**: Email cadastrado do usuário
    - **senha**: Senha do usuário

    ## Retorna:
    - **access_token**: Token JWT para autenticação nas demais rotas
    - **token_type**: Tipo do token (bearer)
    - **usuario_id**: ID do usuário autenticado
    - **nome**: Nome do usuário

    ## Exemplos de requisição:

    **cURL:**
    ```bash
    curl -X POST "http://localhost:8000/api/v1/acesso" \\
      -H "Content-Type: application/json" \\
      -d '{
        "email": "joao.silva@email.com",
        "senha": "senha123"
      }'
    ```

    **Python:**
    ```python
    import requests
    url = "http://localhost:8000/api/v1/acesso"
    data = {"email": "joao.silva@email.com", "senha": "senha123"}
    response = requests.post(url, json=data)
    token = response.json()['access_token']
    print(f"Token: {token}")
    ```

    **Node.js:**
    ```javascript
    fetch('http://localhost:8000/api/v1/acesso', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        email: 'joao.silva@email.com',
        senha: 'senha123'
      })
    }).then(r => r.json()).then(d => console.log('Token:', d.access_token));
    ```

    ## Exemplo de uso do token:
    ```
    Authorization: Bearer <access_token>
    ```
    """,
    response_description="Token de acesso e informações do usuário",
)
async def fazer_login(acesso: AcessoRequest):
    """
    Autenticar usuário e gerar token de acesso.

    **Campos obrigatórios:**
    - **email**: Email cadastrado do usuário
    - **senha**: Senha do usuário

    **Retorna:**
    - **access_token**: Token JWT para autenticação nas demais rotas
    - **token_type**: Tipo do token (bearer)
    - **usuario_id**: ID do usuário autenticado
    - **nome**: Nome do usuário

    **Exemplo de uso do token:**
    ```
    Authorization: Bearer <access_token>
    ```
    """
    return AcessoController.fazer_login(acesso)
