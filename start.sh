#!/bin/bash

if [ ! -d ./venv/ ]; then
  echo 'Setup virtual environment'
  python3 -m venv venv
  source ./venv/bin/activate
  pip install -r requirements.txt
fi

if ! [ -x $(command -v deactivate) ]; then
  source ./venv/bin/activate
fi

python -m pythonio.main