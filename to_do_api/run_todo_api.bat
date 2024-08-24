@echo off
cd venv\Scripts
call activate.bat
cd ../..
cd todo_api
python manage.py runserver
cmd /k