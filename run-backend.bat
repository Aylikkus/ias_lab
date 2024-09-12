@echo off
CD backend

:: Настраиваем venv для Python
call python -m venv .venv
call .venv\Scripts\activate
call python -m pip install -r requirements.txt

:: Запускаем Flask
call python -m flask --app app:app run -p 6000
pause