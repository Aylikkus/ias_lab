#!/bin/bash

# Настраиваем venv для Python
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Запускаем Flask
flask --app app:app run -p 6000

