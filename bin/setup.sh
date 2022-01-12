#!/usr/bin/env zsh

# Setup the environment
python -m venv venv
source venv/bin/activate

# Update pip
python -m pip install --upgrade pip
pip install wheel

# Install requirements
pip install PyPDF2
pip install pre-commit
