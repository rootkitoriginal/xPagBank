# app/browser_logic.py
import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

# Diretório base para salvar dados de clientes (cookies, screenshots)
CLIENTES_DIR = Path("./clientes")

async def login_and_persist(username: str, password: str) -> dict:
    """
    Executa a automação de login, salva cookies e screenshot.
    Implementa estratégias de fallback para seletores.
    """
    
    # Cria o diretório específico do cliente
    client_data_dir = CLIENTES_DIR / username
    client_data_dir.mkdir(parents=True, exist_ok=True)
    
    # Caminho onde o arquivo state (cookies) será salvo/carregado
    storage_state_path = client_data_dir / "state.json"
    screenshot_path = client_data_dir / "screenshot_final.png"

    # --- Configuração do Playwright ---
    # Usamos headless=True por padrão, mas pode ser configurado por variável de ambiente
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    
    # Para o VNC/noVNC (execução com interface gráfica), o headless deve ser "false"
    # e a execução deve ocorrer dentro de um Xvfb (que seria gerenciado pelo Docker/Supervisor)
    
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=headless, args=['--no-sandbox'])
            
            # Carrega o estado de armazenamento anterior (cookies) se existir
            context = await browser.new_context(storage_state=storage_state_path if storage_state_path.exists() else None)
            page = await context.new_page()

            await page.goto("https://www.wikipedia.org/") # Exemplo de site
            
            # --- Robustez: Múltiplas estratégias de fallback para o campo de busca ---
            # 1. Tenta o seletor mais específico
            # 2. Se falhar (timeout), tenta um seletor menos específico (por nome)
            
            # Lista de seletores em ordem de preferência (fallback)
            search_selectors = [
                '#searchInput',       # ID específico (preferido)
                'input[name="search"]', # Por atributo name
                '#js-site-search-input' # Outro ID possível
            ]
            
            search_field = None
            for selector in search_selectors:
                try:
                    # Tenta encontrar o elemento com um timeout curto
                    search_field = page.locator(selector).first
                    await search_field.wait_for(timeout=3000) # 3 segundos para encontrar
                    print(f"INFO: Seletor '{selector}' encontrado com sucesso.")
                    break
                except PlaywrightTimeoutError:
                    print(f"WARN: Seletor '{selector}' falhou. Tentando fallback.")
            
            if not search_field:
                 raise ValueError("Não foi possível localizar o campo de busca com nenhum seletor.")
            
            # Executa a ação
            await search_field.fill(f"Automação Playwright com {username}")
            
            # --- Persistência: Salvando cookies e screenshot ---
            await context.storage_state(path=storage_state_path)
            await page.screenshot(path=screenshot_path)

            await browser.close()
            
            return {
                "status": "success",
                "message": "Login/Ação concluída e estado salvo.",
                "cookies_saved_to": str(storage_state_path),
                "screenshot_saved_to": str(screenshot_path)
            }

    except Exception as e:
        # Tratamento de Erros Amigáveis
        return {
            "status": "error",
            "message": f"Erro na automação: {e.__class__.__name__} - {str(e)}",
            "details": "Verifique o log para detalhes completos."
        }

if __name__ == '__main__':
    # Exemplo de execução direta para teste
    print(asyncio.run(login_and_persist("teste_user", "senha123")))