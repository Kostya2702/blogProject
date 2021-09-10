# WSGI APP for stepik
bind = "0.0.0.0:8000"


def wsgi_app(environ, start_responce):
    start_responce('200 OK', [('Content-type', 'text/plain')])
    pattern = r'(?:\w\=\d)+'
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return body

