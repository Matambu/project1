#! /bin/bash
#!/bin/sh
cd
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
. venv/bin/activate
cd project1/Service1/application
pip3 install pytest
pip3 install -r requirements.txt
cd ..
cd ..

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