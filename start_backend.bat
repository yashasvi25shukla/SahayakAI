@echo off
cd /d %~dp0
if not exist .env (
  echo ERROR: .env file not found.
  echo Copy .env.example to .env and add your Gemini API key.
  pause
  exit /b 1
)
if exist venv\Scripts\python.exe (
  venv\Scripts\python.exe -m uvicorn app.main:app --reload
) else (
  python -m uvicorn app.main:app --reload
)
pause
