# Orientta Hunter AI

Plataforma de Inteligência Comercial e ATS avançado para Job Hunters.

## Estrutura do Projeto
- `/backend`: API construída com FastAPI e Python 3.13.
- `/frontend`: Interface construída com Next.js 15, React 19 e TailwindCSS.
- `/database`: Migrations (Alembic) e schemas do PostgreSQL.
- `/docker`: Configurações de orquestração.

## Como iniciar o ambiente de desenvolvimento

1. Clone o repositório.
2. Copie o `.env.example` para `.env` e ajuste as credenciais.
3. Execute na raiz do projeto:
   ```bash
   docker compose up --build
