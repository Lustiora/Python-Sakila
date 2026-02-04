@echo off
cd /d "%~dp0"
call .venv\Scripts\activate

echo ---------------------------------------------------
echo 🚀 Flet Hot Reload Mode Starting...
echo [Web Mode] http://localhost:34636
echo [Exit] Ctrl + C
echo ---------------------------------------------------

flet run -r -w -p 34636 test_main_window.py

pause