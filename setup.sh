#!/bin/bash
echo "Setting up project environment..."

# 1) Ensure the enviorment exists and create it if it doesn't
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists, skipping..."
fi

# 2) Activate the environment
echo "Activating virtual environment..."
source venv/bin/activate

# 3) Install dependencies
echo "Installing dependencies, this will take a few minutes...."
pip install -r requirements.txt

echo "Done! Run 'source venv/bin/activate' to activate the environment and start working on the project."
