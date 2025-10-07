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
        await page.setViewportSize({ width: 1220, height: 1080 });

        // Navegar para o PagBank
        console.log('Navigating to PagBank...');
        await page.goto('https://www.pagbank.com.br', { 
            waitUntil: 'domcontentloaded',
            timeout: 60000 
        });

        // Aguardar página carregar e aceitar cookies se necessário
        try {
            await page.waitForSelector('button:has-text("Entrar")', { timeout: 1000 });
            await page.click('button:has-text("Entrar")');
            console.log('Cookies accepted');
        } catch (error) {
            console.log('No cookie banner found');
        }

        // Clicar no botão Entrar
        console.log('Clicking Entrar button...');
        try {
            // Tentar diferentes seletores para o botão Entrar
            await Promise.race([
                page.waitForSelector('a[href*="acesso.pagbank.com.br"]', { timeout: 5000 }),
                page.waitForSelector('text=Entrar', { timeout: 5000 }),
                page.waitForSelector('[data-testid="login"]', { timeout: 3000 })
            ]);
            
            await page.click('a[href*="acesso.pagbank.com.br"], text=Entrar, [data-testid="login"]');
            await page.waitForLoadState('networkidle', { timeout: 15000 });
        } catch (error) {
            console.log('Failed to find login button, trying to navigate directly...');
            await page.goto('https://acesso.pagbank.com.br', { timeout: 4000 });
        }
        
        
        // Preencher CPF/CNPJ/Email
        console.log('Filling login credentials...');
        try {
            // Aguardar especificamente pelo campo de CPF
            console.log('Waiting for CPF field...');
            await page.waitForSelector('input, [role="textbox"]', { timeout: 15000 });
            
            // Usar seletor mais robusto
            const cpfField = page.getByRole('textbox', { name: 'CPF, CNPJ ou E-mail' });
            await cpfField.waitFor({ timeout: 10000 });
            await cpfField.fill('01796604119');
            console.log('CPF filled successfully');
            
            // Aguardar a página processar e ir para tela de senha
            console.log('Waiting for password screen...');
            await page.waitForSelector('[role="textbox"]:has-text("Campo 1"), input[name*="Campo"], input[aria-label*="Campo"]', { timeout: 15000 });
            
            // Preencher senha (6 dígitos: 130988)
            console.log('Filling password fields...');
            const password = '130988';
            for (let i = 0; i < 6; i++) {
                const fieldNumber = i + 1;
                try {
                    await page.getByRole('textbox', { name: `Campo ${fieldNumber}` }).fill(password[i]);
                    console.log(`Password field ${fieldNumber} filled with: ${password[i]}`);
                } catch (error) {
                    console.log(`Error filling password field ${fieldNumber}:`, error.message);
                }
            }
            
            // Clicar no botão Entrar
            console.log('Clicking final Entrar button...');
            await page.getByRole('button', { name: 'Entrar' }).click();
            
            // Aguardar resultado do login
            await page.waitForTimeout(5000);
            
            // Verificar se login foi processado
            const currentUrl = page.url();
            console.log('Current URL after login attempt:', currentUrl);
            
            if (await page.locator('text=incorreta').count() > 0) {
                console.log('Login failed: Invalid credentials detected');
            } else if (currentUrl !== 'https://acesso.pagbank.com.br/') {
                console.log('Login may have succeeded - URL changed');
            } else {
                console.log('Login status unclear - staying on login page');
            }
            
        } catch (error) {
            console.log('Error during login process:', error.message);
        }

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