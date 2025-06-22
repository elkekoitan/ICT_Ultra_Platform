@echo off
cd /d %~dp0..
set PYTHONPATH=%CD%
set GATEWAY_API_KEY=devkey
uvicorn services.gateway.main:app --app-dir . --port 8000 --log-level warning 