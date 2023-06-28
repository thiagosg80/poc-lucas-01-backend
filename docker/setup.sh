#!/bin/bash

python3 -m venv .venv
. .venv/bin/activate
pip install pipenv
pipenv install
flask --app app run --debug --host=0.0.0.0