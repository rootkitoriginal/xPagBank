from fastapi import APIRouter, Header

from app.controllers.saldo_controller import SaldoController
from app.schemas.saldo import SaldoResponse

router = APIRouter(tags=["saldo"])


@router.get(
    "/saldo",
    response_model=SaldoResponse,
    summary="Consultar saldo",
    description="""
    Consulta o saldo disponível, bloqueado e total do usuário.

    ## Headers obrigatórios:
    - **X-Usuario-Id**: ID do usuário (número inteiro)

    ## Retorna:
    - **saldo_disponivel**: Valor disponível para uso imediato
    - **saldo_bloqueado**: Valor bloqueado/reservado (ex: transações pendentes)
    - **saldo_total**: Soma do disponível + bloqueado

    ## Exemplos de requisição:

    **cURL:**
    ```bash
    curl -X GET "http://localhost:8874/api/v1/saldo" \\
      -H "X-Usuario-Id: 1"
    ```

    **Python:**
    ```python
    import requests
    url = "http://localhost:8874/api/v1/saldo"
    headers = {"X-Usuario-Id": "1"}
    response = requests.get(url, headers=headers)
    result = response.json()
    print(f"Saldo: R$ {result['saldo_disponivel']}")
    ```

    **Node.js:**
    ```javascript
    fetch('http://localhost:8874/api/v1/saldo', {
      headers: {'X-Usuario-Id': '1'}
    }).then(r => r.json()).then(console.log);
    ```
    """,
    response_description="Informações de saldo do usuário",
)
async def consultar_saldo(
    usuario_id: int = Header(..., alias="X-Usuario-Id", description="ID do usuário (via header)")
):
    """
    Consultar saldo do usuário.

    **Headers obrigatórios:**
    - **X-Usuario-Id**: ID do usuário (número inteiro)

    **Retorna:**
    - **saldo_disponivel**: Valor disponível para uso imediato
    - **saldo_bloqueado**: Valor bloqueado/reservado (ex: transações pendentes)
    - **saldo_total**: Soma do disponível + bloqueado

    **Exemplo de chamada:**
    ```bash
    curl -X GET "http://localhost:8874/api/v1/saldo" \\
      -H "X-Usuario-Id: 1"
    ```
    """
    return SaldoController.consultar_saldo(usuario_id)
