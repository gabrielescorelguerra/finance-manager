<p align="center">
    <img src="./docs/banner.png" alt="finance-manager Banner" width="200">
</p>

<h1 align="center">Finance Manager</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-f6f6f6?style=for-the-badge&logo=python&logoColor=4CAF50" />
  <img src="https://img.shields.io/badge/FastAPI-f6f6f6?style=for-the-badge&logo=fastapi&logoColor=4CAF50" />
  <img src="https://img.shields.io/badge/Telegram-f6f6f6?style=for-the-badge&logo=telegram&logoColor=4CAF50" />
  <img src="https://img.shields.io/badge/Gemini-f6f6f6?style=for-the-badge&logo=googlegemini&logoColor=4CAF50" />
  <img src="https://img.shields.io/badge/Google_Sheets-f6f6f6?style=for-the-badge&logo=googlesheets&logoColor=4CAF50" />
  <img src="https://img.shields.io/badge/uv-f6f6f6?style=for-the-badge&logo=uv&logoColor=4CAF50" />
</p>

<p align="center">
  Bot do Telegram para gerenciamento financeiro pessoal, integrado ao Google Sheets e com processamento inteligente de transações usando IA.
</p>

## Funcionalidades

- [x] Registro de transações financeiras via Telegram
- [x] Integração com Google Sheets para armazenamento e organização dos dados
- [x] Processamento inteligente de mensagens com Gemini
- [x] API com FastAPI para suporte a webhook
- [x] Suporte a configuração para uma ou múltiplas planilhas por usuário

## Funcionalidades Futuras

- [ ] Acesso a estatísticas mais avançadas por meio do telegram
- [ ] Dashboard anual
- [ ] Dashboard de planejamento e previsões
- [ ] Possibilidade de excluir e editar transações por meio do telegram

## Instalação

```bash
git clone https://github.com/gabrielescorelguerra/finance-manager.git
cd finance_manager

uv sync
```

## Configuração

Crie um arquivo `.env` com base no `.env.example`:

```env
TELEGRAM_TOKEN="SEU_TOKEN_DO_TELEGRAM"
GEMINI_API_KEY="SUA_CHAVE_DA_API_DO_GEMINI"

# Para 1 planilha
SHEET_KEY="SUA_CHAVE_DO_GOOGLE_SHEET"

# Para 2 planilhas
USER_1_SHEET_KEY="SUA_CHAVE_DA_PLANILHA_DO_USUARIO_1"
USER_2_SHEET_KEY="SUA_CHAVE_DA_PLANILHA_DO_USUARIO_2"

ENVIRONMENT=local
WEBHOOK_URL="https://seu-app.onrender.com/webhook"
```

## Uso

Rodar localmente:

```bash
uv run uvicorn finance_sheets.main:app --reload
```

## Estrutura do projeto

```bash
finance_manager/
├── scripts/
├── src/
│   └── finance_sheets/
├── .env.example
├── pyproject.toml
├── requirements.txt
└── uv.lock
```