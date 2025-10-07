console.log('Starting Node.js server...');
console.log('Node version:', process.version);
console.log('Working directory:', process.cwd());

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

console.log('Required dependencies loaded successfully');

async function startPagBankServer() {
    // Ler a porta do arquivo gerado durante o build
    let cdpPort = 3001;
    try {
        const portFile = path.join(__dirname, 'cdp-port.txt');
        if (fs.existsSync(portFile)) {
            cdpPort = parseInt(fs.readFileSync(portFile, 'utf8').trim());
        }
    } catch (error) {
        console.log('Using default port 3001');
    }

    console.log(`Starting Playwright server on port ${cdpPort}`);
    
    try {
        // Configurar o navegador com opções otimizadas
        const browser = await chromium.launch({
            headless: false, // Mostrar o navegador no Fluxbox
            args: [
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-accelerated-2d-canvas',
                '--no-first-run',
                '--no-zygote',
                '--disable-gpu',
                '--disable-background-timer-throttling',
                '--disable-backgrounding-occluded-windows',
                '--disable-renderer-backgrounding',
                '--disable-features=TranslateUI',
                '--disable-extensions',
                '--disable-default-apps',
                `--remote-debugging-port=${cdpPort}`,
                '--remote-debugging-address=0.0.0.0',
                '--remote-allow-origins=*'
            ]
        });

        console.log(`Browser launched successfully. CDP server running on port ${cdpPort}`);
        console.log(`Connect using: ws://localhost:${cdpPort}`);

        // Criar uma nova página
        const page = await browser.newPage();
        
        // Configurar viewport
        await page.setViewportSize({ width: 800, height: 600 });

        // Navegar para o PagBank
        console.log('Navigating to PagBank...');
        await page.goto('https://www.pagbank.com.br', { 
            waitUntil: 'domcontentloaded',
            timeout: 60000 
        });

        // Aguardar página carregar e aceitar cookies se necessário
        try {
            await page.waitForSelector('button:has-text("OK")', { timeout: 5000 });
            await page.click('button:has-text("OK")');
            console.log('Cookies accepted');
        } catch (error) {
            console.log('No cookie banner found');
        }

        // Clicar no botão Entrar
        console.log('Clicking Entrar button...');
        await page.click('a[href*="acesso.pagbank.com.br"]');
        
        // Aguardar página de login carregar
        await page.waitForSelector('input[name="login"], input[placeholder*="CPF"]', { timeout: 10000 });
        
        // Preencher CPF
        console.log('Filling CPF...');
        const cpfField = await page.locator('input[name="login"], input[placeholder*="CPF"], textbox:has-text("CPF")').first();
        await cpfField.fill('01796604119');
        
        // Clicar em Continuar
        console.log('Clicking Continuar...');
        await page.click('button:has-text("Continuar")');
        
        // Aguardar campos de senha aparecerem
        await page.waitForSelector('input[name="password1"], input[aria-label*="Campo 1"]', { timeout: 10000 });
        
        // Preencher senha (6 dígitos: 130988)
        console.log('Filling password...');
        const password = '130988';
        for (let i = 0; i < 6; i++) {
            const fieldSelector = `input[aria-label*="Campo ${i + 1}"], input[name="password${i + 1}"]`;
            await page.locator(fieldSelector).first().fill(password[i]);
        }
        
        // Clicar no botão Entrar
        console.log('Clicking final Entrar button...');
        await page.click('button:has-text("Entrar")');
        
        // Aguardar login processar
        await page.waitForTimeout(3000);
        
        // Verificar se login foi bem sucedido
        const currentUrl = page.url();
        if (currentUrl.includes('acesso.pagbank.com.br') && await page.locator('text=incorreta').count() > 0) {
            console.log('Login failed: Invalid credentials');
            // Continuará mesmo com erro para manter a sessão ativa
        } else {
            console.log('Login attempt completed');
        }

        

        console.log('PagBank loaded successfully!');
        console.log('Session is now active and ready for external connections.');
        
        // Manter a sessão ativa
        console.log('Keeping session alive...');
        
        // Configurar handler para manter a página ativa
        setInterval(async () => {
            try {
                // Verificar se a página ainda está ativa
                await page.evaluate(() => {
                    console.log('Session heartbeat:', new Date().toISOString());
                });
            } catch (error) {
                console.log('Page became inactive, attempting to reload...');
                try {
                    await page.reload();
                } catch (reloadError) {
                    console.error('Failed to reload page:', reloadError);
                }
            }
        }, 60000); // Check every minute

        // Handler para graceful shutdown
        process.on('SIGINT', async () => {
            console.log('Shutting down gracefully...');
            await browser.close();
            process.exit(0);
        });

        process.on('SIGTERM', async () => {
            console.log('Shutting down gracefully...');
            await browser.close();
            process.exit(0);
        });

        // Manter o processo rodando
        await new Promise(() => {}); // Infinite promise

    } catch (error) {
        console.error('Error starting PagBank server:', error);
        process.exit(1);
    }
}

// Aguardar um pouco para o X server estar pronto
setTimeout(() => {
    startPagBankServer().catch(console.error);
}, 5000);