sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/ask/django.py /etc/gunicorn.d/django.py
sudo gunicorn -c /etc/gunicorn.d/django.py ask.django:wsgi_app
