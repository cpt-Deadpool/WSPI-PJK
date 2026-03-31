@echo off
echo Setting up project environment...

:: 1) Ensure the enviorment exists and create it if it doesn't
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo Virtual environment already exists, skipping...
)

:: 2) Activate the environment
echo Activating virtual environment...
call venv\Scripts\activate

:: 3) Install dependencies
echo Installing dependencies, this will take a few minutes....
pip install -r requirements.txt

echo Done! Run "venv\Scripts\activate" to activate the environment and start working on the project.