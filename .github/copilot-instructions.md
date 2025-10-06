# FastAPI REST API Project - xPagBank

## Project Overview
FastAPI REST API with MVC architecture, versioned endpoints (v1, v2, ...), and Git workflow integration using GitHub CLI.

## API Structure
RESTful API with version-based routing:
- **Base Path**: `/api/{version}/`
- **Versions**: v1, v2, ...

### API v1 Endpoints
- `GET /api/v1/health` - Health check
- `POST /api/v1/usuario` - User management
- `POST /api/v1/acesso` - Access/Authentication
- `POST /api/v1/qrcode` - QR Code generation
- `POST /api/v1/confirmaqrcode` - QR Code confirmation
- `GET /api/v1/saldo` - Balance inquiry
- `POST /api/v1/pix` - PIX transaction
- `POST /api/v1/confirma_pix` - PIX confirmation

## Architecture
MVC Pattern:
- **Models**: Database models and schemas
- **Views**: API endpoints and routers
- **Controllers**: Business logic and services

## Checklist
- [x] Verify that the copilot-instructions.md file in the .github directory is created.
- [x] Clarify Project Requirements
  - RESTful API with versioned routing (v1, v2, ...)
  - MVC architecture pattern
  - 8 endpoints for v1: health, usuario, acesso, qrcode, confirmaqrcode, saldo, pix, confirma_pix
  - Git workflow integration with gh CLI
- [x] Scaffold the Project (MVC structure with versioned endpoints)
- [x] Customize the Project
- [ ] Install Required Extensions
- [x] Compile the Project
- [x] Create and Run Task
- [x] Launch the Project
- [x] Ensure Documentation is Complete
