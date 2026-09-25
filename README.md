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
  Telegram bot for personal finance management, integrated with Google Sheets and featuring AI-powered transaction processing.
</p>

## Features

* [x] Record financial transactions through Telegram
* [x] Google Sheets integration for data storage and organization
* [x] Intelligent message processing with Gemini
* [x] FastAPI backend with webhook support
* [x] Support for configuring one or multiple spreadsheets per user

## Upcoming Features

* [ ] Access more advanced statistics through Telegram
* [ ] Annual dashboard
* [ ] Planning and forecasting dashboard
* [ ] Delete and edit transactions through Telegram

## Installation

```bash
git clone https://github.com/gabrielescorelguerra/finance-manager.git
cd finance_manager

uv sync
```

## Configuration

Create a `.env` file based on `.env.example`:

```env
TELEGRAM_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"

# For 1 spreadsheet
SHEET_KEY="YOUR_GOOGLE_SHEET_KEY"

# For 2 spreadsheets
USER_1_SHEET_KEY="USER_1_GOOGLE_SHEET_KEY"
USER_2_SHEET_KEY="USER_2_GOOGLE_SHEET_KEY"

ENVIRONMENT=local
WEBHOOK_URL="https://your-app.onrender.com/webhook"
```

## Usage

Run locally:

```bash
uv run uvicorn finance_sheets.main:app --reload
```

## Project Structure

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
