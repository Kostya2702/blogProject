sudo pip3 install virtualenv
sudo pip3 install pathlib2
virtualenv -p python3 venv
source venv/bin/activate
pip3 install django
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -w 2 -c /home/box/web/etc/hello_conf.py hello:wsgi_app & gunicorn -w 2 -c /home/box/web/etc/qa_conf.py ask.wsgi:application
