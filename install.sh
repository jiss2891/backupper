#!/bin/bash
APP=$(pwd)

apt install -y nginx virtualenv

virtualenv bkp
cd bkp
source bin/activate

cd $APP
pip install -r requirements.txt
