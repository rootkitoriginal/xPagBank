from fastapi import APIRouter, status

from app.controllers.usuario_controller import UsuarioController
from app.schemas.usuario import UsuarioCreate, UsuarioResponse

router = APIRouter(tags=["usuario"])


@router.post(
    "/usuario",
    response_model=UsuarioResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo usuário",
    description="""
Cria um novo usuário no sistema com os dados fornecidos.

**Campos obrigatórios:**
- nome: Nome completo (mínimo 3 caracteres)
- email: Email válido
- cpf: CPF com 11 dígitos (apenas números)
- senha: Senha com no mínimo 6 caracteres

**Campos opcionais:**
- telefone: Telefone com DDD

**Exemplo cURL:**
```
curl -X POST "http://localhost:8000/api/v1/usuario" \\
  -H "Content-Type: application/json" \\
  -d '{"nome": "João Silva", "email": "joao.silva@email.com", \\
    "cpf": "12345678901", "telefone": "11987654321", "senha": "senha123"}'
```

**Exemplo Python:**
```
import requests
response = requests.post(
    "http://localhost:8000/api/v1/usuario",
    json={"nome": "João Silva", "email": "joao.silva@email.com",
          "cpf": "12345678901", "telefone": "11987654321", "senha": "senha123"}
)
```

**Exemplo Node.js:**
```
fetch('http://localhost:8000/api/v1/usuario', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    nome: 'João Silva',
    email: 'joao.silva@email.com',
    cpf: '12345678901',
    telefone: '11987654321',
    senha: 'senha123'
  })
})
```

📝 Veja mais exemplos em: /API_EXAMPLES.md
    """,
    response_description="Dados do usuário criado",
)
async def criar_usuario(usuario: UsuarioCreate):
    """
    Criar um novo usuário no sistema.

    **Campos obrigatórios:**
    - **nome**: Nome completo (mínimo 3 caracteres)
    - **email**: Email válido
    - **cpf**: CPF com 11 dígitos (apenas números)
    - **senha**: Senha com no mínimo 6 caracteres

    **Campos opcionais:**
    - **telefone**: Telefone com DDD

    **Retorna:**
    - Dados do usuário criado (sem a senha)
    - ID único do usuário
    - Data de criação
    """
    return UsuarioController.criar_usuario(usuario)
