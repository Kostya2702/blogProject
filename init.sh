sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/django.py /etc/gunicorn.d/ask_conf.py
sudo gunicorn -c /etc/gunicorn.d/django.py django:wsgi_app
