#!/bin/bash

sudo apt-get update
sudo apt-get install pip3 python3-venv -y

python3 -m venv venv
#virtualenv -p python3 venv
source ./venv/bin/activate

pip3 install -r test_requirements.txt

cd service-1
python3 -m pytest --cov=app
cd ..

cd service-2
python3 -m pytest --cov=app
cd ..

cd service-3
python3 -m pytest --cov=app
cd ..

cd service-4
python3 -m pytest --cov=app
cd ..

