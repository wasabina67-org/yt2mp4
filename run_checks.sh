#!/bin/bash

isort src/data.py src/run.py src/utils.py
black src/data.py src/run.py src/utils.py
flake8 src/data.py src/run.py src/utils.py
mypy src/data.py src/run.py src/utils.py
