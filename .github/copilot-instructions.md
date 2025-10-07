# GitHub Copilot Instructions for xPagBank

## Project Overview
xPagBank is an automation system for PagBank using Playwright in a Docker container with VNC interface. The project provides automated access to PagBank portal with visual feedback through VNC and programmatic access via Chrome DevTools Protocol.

## Key Components

### Docker Container
- Base image: Node.js 18
- Includes: Xvfb, Fluxbox, x11vnc, noVNC, Supervisor
- Chrome browser for Playwright automation
- Exposed ports: 8080 (VNC), 3001 (CDP)

### Main Files
- `server.js`: Main Playwright automation script
- `Dockerfile`: Container configuration
- `supervisord.conf`: Process management
- `entrypoint.sh`: Container startup script
- `pagbank.sh`: Utility script for server management

## Coding Guidelines

### JavaScript/Node.js
- Use async/await for asynchronous operations
- Follow Playwright best practices for browser automation
- Handle errors appropriately with try/catch blocks
- Log important operations and errors
- Use environment variables for configuration

### Docker/Container
- Follow Docker best practices
- Keep container size minimal
- Use multi-stage builds when possible
- Handle proper shutdown of services

### Browser Automation
- Wait for elements properly
- Use proper selectors (prefer role, text, or testid)
- Handle timeouts and network conditions
- Consider page load states

## Important Considerations

### Security
- Never store credentials in code
- Use environment variables for sensitive data
- Follow PagBank security guidelines
- Implement proper error handling

### Performance
- Optimize Playwright operations
- Minimize unnecessary waits
- Handle resources properly
- Clean up after operations

### Maintenance
- Keep dependencies updated
- Document changes clearly
- Test thoroughly before committing
- Follow semantic versioning

## Workflow Instructions

### Development
1. Make changes locally
2. Test with Docker build
3. Verify VNC interface
4. Check CDP functionality
5. Update documentation

### Testing
- Test all automation flows
- Verify VNC access
- Check CDP connectivity
- Validate error handling
- Test container restart

### Deployment
- Build container with `./pagbank.sh build`
- Test deployment with `./pagbank.sh start`
- Verify all interfaces
- Check logs with `./pagbank.sh logs`

## File Naming Conventions
- Use kebab-case for files
- Scripts end in `.js`
- Config files use appropriate extensions
- Test files end in `.test.js`

## Error Handling
- Log errors appropriately
- Use descriptive error messages
- Include error context
- Implement proper fallbacks
