#!/bin/bash

if [ ! -d ./venv/ ]; then
  echo 'Setup virtual environment'
  python3 -m venv venv
  source ./venv/bin/activate
  pip install -r requirements.txt
fi

if [ command -v ls &> /dev/null ]; then
  echo 'abc'
fi

# sudo su
python -m pythonio.main