#!/bin/sh
pip-compile setup.py --find-links=https://download.pytorch.org/whl/torch_stable.html --upgrade --generate-hashes --output-file=requirements-lock.txt