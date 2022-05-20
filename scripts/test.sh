#! /bin/bash

cd Service1/
pip3 install -r requirements.txt
python3 -m pytest --cov .

cd .. 

cd Service2/
pip3 install -r requirements.txt
python3 -m pytest --cov .

cd .. 

cd Service3/
pip3 install -r requirements.txt
python3 -m pytest --cov .

cd .. 

cd Service4/
pip3 install -r requirements.txt
python3 -m pytest --cov .