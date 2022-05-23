#! /bin/bash
#!/bin/sh
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
. venv/bin/activate
pip3 install pytest
pip3 install -r requirements.txt

cd Service1/test
pip3 install -r requirements.txt
python3 -m pytest --cov .

cd .. 

cd Service2/test
pip3 install -r requirements.txt
python3 -m pytest --cov .

cd .. 

cd Service3/test
pip3 install -r requirements.txt
python3 -m pytest --cov .

cd .. 

cd Service4/test
pip3 install -r requirements.txt
python3 -m pytest --cov .