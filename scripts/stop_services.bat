@echo off
REM Tüm uvicorn süreçlerini sonlandır
taskkill /im uvicorn.exe /f >nul 2>&1 