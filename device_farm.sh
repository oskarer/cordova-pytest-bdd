#!/bin/bash

# pip freeze > requirements.txt
# pip wheel --wheel-dir wheelhouse -r requirements.txt
find . -name '__pycache__' -type d -exec rm -r {} +
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
zip -r test_bundle.zip tests/ wheelhouse/ requirements.txt
