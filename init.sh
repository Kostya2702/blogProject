sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/qa_conf.py /etc/gunicorn.d/qa_conf.py
sudo gunicorn -c /etc/gunicorn.d/qa_conf.py django:wsgi_app
