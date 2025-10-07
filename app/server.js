const { exec } = require('child_process');

const chromeCmd = `google-chrome-stable ${process.env.CHROME_FLAGS || '--no-sandbox --disable-gpu'}`;

console.log(`Starting Chrome with command: ${chromeCmd}`);

const chromeProcess = exec(chromeCmd, (error, stdout, stderr) => {
    if (error) {
        console.error(`exec error: ${error}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
});

chromeProcess.on('exit', (code) => {
    console.log(`Chrome process exited with code ${code}`);
});
