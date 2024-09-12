@echo off
CD frontend

:: Устанавливаем зависимости и запускаем Vue
call npm install
call npm run serve
pause