# API v2 - Browser Automation

API v2 usa Playwright para automação real do navegador, simulando interação de usuário real.

## Diferenças entre V1 e V2

| Característica | V1 (HTTP Client) | V2 (Browser Automation) |
|---------------|------------------|-------------------------|
| **Velocidade** | ⚡ Muito rápido | 🐢 Mais lento |
| **Bloqueios** | ❌ Pode ser bloqueado | ✅ Simula usuário real |
| **Recursos** | 💚 Baixo consumo | 🔴 Alto consumo (RAM/CPU) |
| **JavaScript** | ❌ Não executa | ✅ Executa JavaScript |
| **Cookies** | ✅ Gerenciado | ✅ Gerenciado |
| **Screenshots** | ❌ Não suporta | ✅ Suporta |
| **Debug** | 📝 Logs HTTP | 🖼️ Screenshots + Logs |

## Quando usar cada versão?

### Use V1 quando:
- Velocidade é prioridade
- Consumo de recursos é limitado
- API não tem proteção JavaScript complexa
- Fazer muitas requisições simultâneas

### Use V2 quando:
- V1 está sendo bloqueado
- Precisa executar JavaScript
- Precisa simular comportamento real
- Precisa capturar screenshots
- Debug visual é importante

## Instalação

### 1. Instalar dependências Python

```bash
pip install -r requirements.txt
```

### 2. Instalar navegadores Playwright

```bash
python3 -m playwright install chromium
```

Ou instalar todos os navegadores:

```bash
python3 -m playwright install
```

## Endpoints V2

### POST /api/v2/acesso

Validar CPF, CNPJ ou Email usando automação de navegador.

**Request:**
```json
{
  "username": "123.456.789-09"
}
```

**Response (sucesso):**
```json
{
  "success": true,
  "message": "Username validado. Campo de senha disponível.",
  "data": {
    "url": "https://acesso.pagbank.com.br/...",
    "cookies_count": 15,
    "next_step": "password",
    "cookies": {
      "__cf_bm": "...",
      "session": "..."
    }
  },
  "source": "browser"
}
```

**Response (erro):**
```json
{
  "success": false,
  "message": "Erro detectado na página",
  "data": {
    "url": "https://acesso.pagbank.com.br/",
    "cookies_count": 5,
    "error_detected": true
  },
  "source": "browser"
}
```

## Exemplos de Uso

### cURL

```bash
# V2 - Browser automation
curl -X POST http://localhost:8874/api/v2/acesso \
  -H 'Content-Type: application/json' \
  -d '{"username": "usuario@example.com"}'
```

### Python

```python
import httpx
import asyncio

async def test_v2():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8874/api/v2/acesso",
            json={"username": "123.456.789-09"}
        )
        print(response.json())

asyncio.run(test_v2())
```

### JavaScript/TypeScript

```typescript
const response = await fetch('http://localhost:8874/api/v2/acesso', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    username: 'usuario@example.com'
  })
});

const data = await response.json();
console.log(data);
```

## Fluxo V2

```
┌─────────────────────────────────────────┐
│ 1. Validar username (CPF/CNPJ/Email)   │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 2. Iniciar navegador Chromium (headless)│
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 3. Navegar para acesso.pagbank.com.br  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 4. Aguardar campo username aparecer    │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 5. Preencher campo com username        │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 6. Aguardar resposta (2 segundos)      │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 7. Capturar estado da página           │
│    - URL atual                          │
│    - Cookies                            │
│    - Conteúdo HTML                      │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 8. Analisar resultado                  │
│    - Erro detectado?                    │
│    - Campo senha disponível?            │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 9. Retornar resposta normalizada       │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ 10. Fechar navegador                    │
└─────────────────────────────────────────┘
```

## Configuração Avançada

### Executar com interface gráfica (para debug)

Modifique `playwright_service.py`:

```python
browser = PlaywrightService(
    headless=False,  # Mostra o navegador
    timeout=30000
)
```

### Capturar screenshots

```python
# No controller
screenshot_path = "/tmp/pagbank_login.png"
await browser.screenshot(screenshot_path, full_page=True)
```

### Executar JavaScript customizado

```python
# No controller
result = await browser.evaluate('''
    () => {
        return {
            title: document.title,
            url: window.location.href,
            cookies: document.cookie
        }
    }
''')
```

### Aguardar elementos específicos

```python
# Aguardar botão de submit
await browser.wait_for_selector(
    'button[type="submit"]',
    state='visible',
    timeout=10000
)
```

## Troubleshooting

### Erro: "playwright._impl._errors.Error: Executable doesn't exist"

**Solução:** Instale os navegadores do Playwright:

```bash
python3 -m playwright install chromium
```

### Erro: "timeout exceeded"

**Soluções:**
1. Aumentar timeout:
```python
browser = PlaywrightService(timeout=60000)  # 60 segundos
```

2. Verificar seletor CSS:
```python
# Testar seletores alternativos
selectors = [
    'input[name="username"]',
    'input[type="text"]',
    '#username'
]
```

### Navegador não fecha

**Solução:** Use context manager ou try/finally:

```python
browser = None
try:
    browser = PlaywrightService()
    # ... código
finally:
    if browser:
        await browser.close()
```

### Alto consumo de memória

**Soluções:**
1. Fechar navegador após cada requisição (já implementado)
2. Limitar requisições simultâneas
3. Usar headless mode (já ativado por padrão)

## Performance

### V1 (HTTP Client)
- **Tempo médio:** 1-2 segundos
- **Memória:** ~50 MB
- **CPU:** Baixo

### V2 (Browser Automation)
- **Tempo médio:** 5-10 segundos
- **Memória:** ~200-300 MB por navegador
- **CPU:** Médio-Alto

## Segurança

### Headers do navegador

V2 usa headers reais do Chromium, incluindo:
- User-Agent real
- Accept-Language
- sec-ch-ua (Client Hints)
- sec-fetch-* headers

### Fingerprinting

V2 é mais difícil de detectar porque:
- Executa JavaScript real
- Tem comportamento de navegador real
- Gera eventos de mouse/teclado
- Renderiza CSS/imagens

## Próximos Passos

Endpoints V2 planejados:
- [ ] POST /api/v2/usuario - Criar usuário
- [ ] POST /api/v2/qrcode - Gerar QR Code
- [ ] GET /api/v2/saldo - Consultar saldo
- [ ] POST /api/v2/pix - Realizar PIX

## Referências

- [Playwright Documentation](https://playwright.dev/python/)
- [FastAPI Async](https://fastapi.tiangolo.com/async/)
- [xPagBank API v1](./API_EXAMPLES.md)
