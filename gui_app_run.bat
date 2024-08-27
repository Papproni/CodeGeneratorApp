@echo off
REM Check if Python is installed and accessible
py --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed or not added to PATH.
    pause
    exit /b
)

REM Navigate to the directory containing the Python script
cd /d "%~dp0"

REM Run the Python script
py codegen.py

REM Pause the command prompt so it doesn't close immediately
pause