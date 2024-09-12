@echo off
CD backend

:: Настраиваем venv для Python
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt

:: Запускаем Flask
python -m flask --app app:app run -p 6000
pause