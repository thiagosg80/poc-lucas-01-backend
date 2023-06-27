#!/bin/bash

python3 -m venv .venv
. .venv/bin/activate
venv/bin/pipenv install
flask --app app run --debug --host=0.0.0.0