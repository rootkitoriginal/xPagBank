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
        await page.setViewportSize({ width: 1920, height: 1080 });

        // Navegar para o PagBank
        console.log('Navigating to PagBank...');
        await page.goto('https://www.pagbank.com.br', { 
            waitUntil: 'domcontentloaded',
            timeout: 60000 
        });

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