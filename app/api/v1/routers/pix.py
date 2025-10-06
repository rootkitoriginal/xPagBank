from fastapi import APIRouter, status

from app.controllers.v1.pix_controller import PixController
from app.schemas.pix import PixRequest, PixResponse

router = APIRouter(tags=["pix"])


@router.post(
    "/pix",
    response_model=PixResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Iniciar transação PIX",
    description="""
    Inicia uma nova transação PIX que precisa ser confirmada.

    ## Campos obrigatórios:
    - **chave_destino**: Chave PIX do destinatário (CPF, email, telefone ou chave aleatória)
    - **valor**: Valor a ser transferido (maior que 0)

    ## Campos opcionais:
    - **descricao**: Descrição da transferência (máximo 200 caracteres)

    ## Exemplos de requisição:

    **cURL:**
    ```bash
    curl -X POST "http://localhost:8874/api/v1/pix" \\
      -H "Content-Type: application/json" \\
      -d '{
        "chave_destino": "maria.silva@email.com",
        "valor": 250.00,
        "descricao": "Transferência PIX"
      }'
    ```

    **Python:**
    ```python
    import requests
    url = "http://localhost:8874/api/v1/pix"
    data = {
        "chave_destino": "maria.silva@email.com",
        "valor": 250.00,
        "descricao": "Transferência PIX"
    }
    response = requests.post(url, json=data)
    result = response.json()
    print(f"Transação ID: {result['transacao_id']}")
    print(f"Código: {result['codigo_confirmacao']}")
    ```

    **Node.js:**
    ```javascript
    fetch('http://localhost:8874/api/v1/pix', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        chave_destino: 'maria.silva@email.com',
        valor: 250.00,
        descricao: 'Transferência PIX'
      })
    }).then(r => r.json()).then(console.log);
    ```

    ## Próximo passo:
    Use o `transacao_id` e `codigo_confirmacao` no endpoint `/api/v1/confirma_pix`
    para completar a transação.
    """,
    response_description="Dados da transação PIX criada",
)
async def iniciar_pix(pix: PixRequest):
    """
    Iniciar uma transação PIX.

    **Campos obrigatórios:**
    - **chave_destino**: Chave PIX do destinatário (CPF, email, telefone ou chave aleatória)
    - **valor**: Valor a ser transferido (maior que 0)

    **Campos opcionais:**
    - **descricao**: Descrição da transferência (máximo 200 caracteres)

    **Retorna:**
    - **transacao_id**: ID único da transação
    - **codigo_confirmacao**: Código para confirmar a transação
      no endpoint `/confirma_pix`
    - **status**: Status da transação (aguardando_confirmacao)

    **Próximo passo:**
    Use o `transacao_id` e `codigo_confirmacao` no endpoint `/api/v1/confirma_pix`
    para completar a transação.
    """
    return PixController.iniciar_pix(pix)
