#!/bin/bash

python3 -m venv virtual-env
source virtual-env/bin/activate

pip3 install -r requirements.txt
python3 runcluster.py

deactivate
