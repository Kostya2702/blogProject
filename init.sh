sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -c /home/box/web/etc/hello.py hello:wsgi_app
gunicorn -c /home/box/web/etc/django.py django:wsgi_pp
