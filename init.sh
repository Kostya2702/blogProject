sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -w 2 -c /home/box/web/etc/hello_conf.py hello:wsgi_app & gunicorn -w 2 -c /home/box/web/etc/qa_conf.py ask.wsgi:application
