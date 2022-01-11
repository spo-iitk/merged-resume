#!/usr/bin/env zsh
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install wheel
pip install PyPDF2
pip install pre-commit
