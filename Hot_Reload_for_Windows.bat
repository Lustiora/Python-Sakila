@echo off
chcp 65001 >nul
cd /d "%~dp0"

if not exist ".gitignore" (
    echo .venv>> .gitignore
    echo __pycache__>> .gitignore
) else (
    findstr ".venv" ".gitignore" >nul || echo .venv>> .gitignore
)

taskkill /F /IM python.exe /T >nul 2>&1

if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate
) else (
    echo ❌ Error: .venv not found.
    pause
    exit /b
)

echo ---------------------------------------------------
echo 🚀 Flet Hot Reload 🚀
echo [Web Mode] http://localhost:34636
echo ---------------------------------------------------

flet run -r -v -w -p 34636 test_main_window.py

echo.
echo ❌ App Closed.
pause