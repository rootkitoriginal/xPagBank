# Exemplos de Requisições - xPagBank API

## Base URL
```
http://localhost:8000/api/v1
```

---

## 1. Health Check

### cURL
```bash
curl -X GET "http://localhost:8000/api/v1/health" \
  -H "accept: application/json"
```

### Python
```python
import requests

url = "http://localhost:8000/api/v1/health"
response = requests.get(url)
print(response.json())
```

### Node.js
```javascript
const fetch = require('node-fetch');

const url = 'http://localhost:8000/api/v1/health';

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

---

## 2. Criar Usuário

### cURL
```bash
curl -X POST "http://localhost:8000/api/v1/usuario" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "email": "joao.silva@email.com",
    "cpf": "12345678901",
    "telefone": "11987654321",
    "senha": "senha123"
  }'
```

### Python
```python
import requests

url = "http://localhost:8000/api/v1/usuario"
headers = {
    "Content-Type": "application/json"
}
data = {
    "nome": "João Silva",
    "email": "joao.silva@email.com",
    "cpf": "12345678901",
    "telefone": "11987654321",
    "senha": "senha123"
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
```

### Node.js
```javascript
const fetch = require('node-fetch');

const url = 'http://localhost:8000/api/v1/usuario';
const data = {
  nome: 'João Silva',
  email: 'joao.silva@email.com',
  cpf: '12345678901',
  telefone: '11987654321',
  senha: 'senha123'
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

---

## 3. Login / Autenticação

### cURL
```bash
curl -X POST "http://localhost:8000/api/v1/acesso" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "joao.silva@email.com",
    "senha": "senha123"
  }'
```

### Python
```python
import requests

url = "http://localhost:8000/api/v1/acesso"
data = {
    "email": "joao.silva@email.com",
    "senha": "senha123"
}

response = requests.post(url, json=data)
result = response.json()
access_token = result['access_token']
print(f"Token: {access_token}")
```

### Node.js
```javascript
const fetch = require('node-fetch');

const url = 'http://localhost:8000/api/v1/acesso';
const data = {
  email: 'joao.silva@email.com',
  senha: 'senha123'
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => {
    console.log('Access Token:', data.access_token);
  })
  .catch(error => console.error('Error:', error));
```

---

## 4. Gerar QR Code

### cURL
```bash
curl -X POST "http://localhost:8000/api/v1/qrcode" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "valor": 150.50,
    "descricao": "Pagamento de produto X"
  }'
```

### Python
```python
import requests

url = "http://localhost:8000/api/v1/qrcode"
data = {
    "valor": 150.50,
    "descricao": "Pagamento de produto X"
}

response = requests.post(url, json=data)
result = response.json()
print(f"QR Code ID: {result['qrcode_id']}")
print(f"QR Code Data: {result['qrcode_data']}")
```

### Node.js
```javascript
const fetch = require('node-fetch');

const url = 'http://localhost:8000/api/v1/qrcode';
const data = {
  valor: 150.50,
  descricao: 'Pagamento de produto X'
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => {
    console.log('QR Code ID:', data.qrcode_id);
    console.log('QR Code Data:', data.qrcode_data);
  })
  .catch(error => console.error('Error:', error));
```

---

## 5. Confirmar QR Code

### cURL
```bash
curl -X POST "http://localhost:8000/api/v1/confirmaqrcode" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "qrcode_id": "abc123-def456-ghi789",
    "codigo_confirmacao": "CONF_abc123"
  }'
```

### Python
```python
import requests

url = "http://localhost:8000/api/v1/confirmaqrcode"
data = {
    "qrcode_id": "abc123-def456-ghi789",
    "codigo_confirmacao": "CONF_abc123"
}

response = requests.post(url, json=data)
result = response.json()
print(f"Sucesso: {result['sucesso']}")
print(f"Mensagem: {result['mensagem']}")
```

### Node.js
```javascript
const fetch = require('node-fetch');

const url = 'http://localhost:8000/api/v1/confirmaqrcode';
const data = {
  qrcode_id: 'abc123-def456-ghi789',
  codigo_confirmacao: 'CONF_abc123'
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => {
    console.log('Sucesso:', data.sucesso);
    console.log('Mensagem:', data.mensagem);
  })
  .catch(error => console.error('Error:', error));
```

---

## 6. Consultar Saldo

### cURL
```bash
curl -X GET "http://localhost:8000/api/v1/saldo" \
  -H "accept: application/json" \
  -H "X-Usuario-Id: 1"
```

### Python
```python
import requests

url = "http://localhost:8000/api/v1/saldo"
headers = {
    "X-Usuario-Id": "1"
}

response = requests.get(url, headers=headers)
result = response.json()
print(f"Saldo Disponível: R$ {result['saldo_disponivel']}")
print(f"Saldo Bloqueado: R$ {result['saldo_bloqueado']}")
print(f"Saldo Total: R$ {result['saldo_total']}")
```

### Node.js
```javascript
const fetch = require('node-fetch');

const url = 'http://localhost:8000/api/v1/saldo';

fetch(url, {
  method: 'GET',
  headers: {
    'X-Usuario-Id': '1'
  }
})
  .then(response => response.json())
  .then(data => {
    console.log('Saldo Disponível: R$', data.saldo_disponivel);
    console.log('Saldo Bloqueado: R$', data.saldo_bloqueado);
    console.log('Saldo Total: R$', data.saldo_total);
  })
  .catch(error => console.error('Error:', error));
```

---

## 7. Iniciar Transação PIX

### cURL
```bash
curl -X POST "http://localhost:8000/api/v1/pix" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "chave_destino": "maria.silva@email.com",
    "valor": 250.00,
    "descricao": "Transferência PIX"
  }'
```

### Python
```python
import requests

url = "http://localhost:8000/api/v1/pix"
data = {
    "chave_destino": "maria.silva@email.com",
    "valor": 250.00,
    "descricao": "Transferência PIX"
}

response = requests.post(url, json=data)
result = response.json()
print(f"Transação ID: {result['transacao_id']}")
print(f"Código Confirmação: {result['codigo_confirmacao']}")
print(f"Status: {result['status']}")
```

### Node.js
```javascript
const fetch = require('node-fetch');

const url = 'http://localhost:8000/api/v1/pix';
const data = {
  chave_destino: 'maria.silva@email.com',
  valor: 250.00,
  descricao: 'Transferência PIX'
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => {
    console.log('Transação ID:', data.transacao_id);
    console.log('Código Confirmação:', data.codigo_confirmacao);
    console.log('Status:', data.status);
  })
  .catch(error => console.error('Error:', error));
```

---

## 8. Confirmar Transação PIX

### cURL
```bash
curl -X POST "http://localhost:8000/api/v1/confirma_pix" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "transacao_id": "abc123-def456-ghi789",
    "codigo_confirmacao": "CONF_abc123"
  }'
```

### Python
```python
import requests

url = "http://localhost:8000/api/v1/confirma_pix"
data = {
    "transacao_id": "abc123-def456-ghi789",
    "codigo_confirmacao": "CONF_abc123"
}

response = requests.post(url, json=data)
result = response.json()
print(f"Sucesso: {result['sucesso']}")
print(f"Mensagem: {result['mensagem']}")
print(f"Status: {result['status']}")
```

### Node.js
```javascript
const fetch = require('node-fetch');

const url = 'http://localhost:8000/api/v1/confirma_pix';
const data = {
  transacao_id: 'abc123-def456-ghi789',
  codigo_confirmacao: 'CONF_abc123'
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => {
    console.log('Sucesso:', data.sucesso);
    console.log('Mensagem:', data.mensagem);
    console.log('Status:', data.status);
  })
  .catch(error => console.error('Error:', error));
```

---

## Fluxo Completo - Exemplo Prático

### Python - Fluxo completo de PIX
```python
import requests

BASE_URL = "http://localhost:8000/api/v1"

# 1. Criar usuário
usuario_data = {
    "nome": "João Silva",
    "email": "joao.silva@email.com",
    "cpf": "12345678901",
    "telefone": "11987654321",
    "senha": "senha123"
}
usuario = requests.post(f"{BASE_URL}/usuario", json=usuario_data).json()
print(f"✓ Usuário criado: {usuario['nome']}")

# 2. Fazer login
login_data = {
    "email": "joao.silva@email.com",
    "senha": "senha123"
}
acesso = requests.post(f"{BASE_URL}/acesso", json=login_data).json()
print(f"✓ Token obtido: {acesso['access_token'][:20]}...")

# 3. Consultar saldo
headers = {"X-Usuario-Id": str(usuario['id'])}
saldo = requests.get(f"{BASE_URL}/saldo", headers=headers).json()
print(f"✓ Saldo disponível: R$ {saldo['saldo_disponivel']}")

# 4. Iniciar PIX
pix_data = {
    "chave_destino": "maria.silva@email.com",
    "valor": 100.00,
    "descricao": "Pagamento teste"
}
pix = requests.post(f"{BASE_URL}/pix", json=pix_data).json()
print(f"✓ PIX iniciado: {pix['transacao_id']}")

# 5. Confirmar PIX
confirma_data = {
    "transacao_id": pix['transacao_id'],
    "codigo_confirmacao": pix['codigo_confirmacao']
}
confirma = requests.post(f"{BASE_URL}/confirma_pix", json=confirma_data).json()
print(f"✓ PIX confirmado: {confirma['mensagem']}")
```

### Node.js - Fluxo completo de PIX
```javascript
const fetch = require('node-fetch');

const BASE_URL = 'http://localhost:8000/api/v1';

async function fluxoCompleto() {
  try {
    // 1. Criar usuário
    const usuario = await fetch(`${BASE_URL}/usuario`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        nome: 'João Silva',
        email: 'joao.silva@email.com',
        cpf: '12345678901',
        telefone: '11987654321',
        senha: 'senha123'
      })
    }).then(r => r.json());
    console.log('✓ Usuário criado:', usuario.nome);

    // 2. Fazer login
    const acesso = await fetch(`${BASE_URL}/acesso`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: 'joao.silva@email.com',
        senha: 'senha123'
      })
    }).then(r => r.json());
    console.log('✓ Token obtido:', acesso.access_token.substring(0, 20) + '...');

    // 3. Consultar saldo
    const saldo = await fetch(`${BASE_URL}/saldo`, {
      headers: { 'X-Usuario-Id': usuario.id.toString() }
    }).then(r => r.json());
    console.log('✓ Saldo disponível: R$', saldo.saldo_disponivel);

    // 4. Iniciar PIX
    const pix = await fetch(`${BASE_URL}/pix`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chave_destino: 'maria.silva@email.com',
        valor: 100.00,
        descricao: 'Pagamento teste'
      })
    }).then(r => r.json());
    console.log('✓ PIX iniciado:', pix.transacao_id);

    // 5. Confirmar PIX
    const confirma = await fetch(`${BASE_URL}/confirma_pix`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        transacao_id: pix.transacao_id,
        codigo_confirmacao: pix.codigo_confirmacao
      })
    }).then(r => r.json());
    console.log('✓ PIX confirmado:', confirma.mensagem);

  } catch (error) {
    console.error('Erro:', error);
  }
}

fluxoCompleto();
```

---

## Notas

- Substitua `localhost:8000` pela URL do seu servidor em produção
- Todos os exemplos usam JSON como formato de dados
- Headers podem ser adicionados conforme necessário
- Para Node.js, você pode usar `axios` ao invés de `fetch` se preferir
- Para Python, certifique-se de ter `requests` instalado: `pip install requests`
