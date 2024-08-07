@echo off
REM Set the FLASK_APP environment variable
set FLASK_APP=app.py
REM Set the Flask environment to development (optional)
set FLASK_ENV=development

REM Activate the virtual environment
call venv\Scripts\activate

REM Start the Flask server
python -m flask run

REM Wait for user input before closing the command prompt
pause
