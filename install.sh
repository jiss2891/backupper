#!/bin/bash
APP=$(pwd)

apt install -y nginx virtualenv python2.7 python-dev build-essential mysql-client postgresql

virtualenv -p /usr/bin/python2.7 bkp
cd bkp
source bin/activate

cd ..
pip install -r requirements.txt # agregar uwsgi, tiger(?)
pip install uwsgi

# agregar dbb_nginx.conf y uwsgi_params

sudo ln -s ~/path/to/your/mysite/mysite_nginx.conf /etc/nginx/sites-enabled/

python manage.py collectstatic

/etc/init.d/nginx stop
/etc/init.d/nginx start
