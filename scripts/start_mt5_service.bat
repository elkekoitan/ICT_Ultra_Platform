@echo off
REM Başlatma dizinini proje köküne ayarla
cd /d %~dp0..
REM Python import yolu – proje kökü
set PYTHONPATH=%CD%

REM MT5 servisini başlat
uvicorn services.mt5_service.main:app --app-dir . --port 8001 --log-level warning 