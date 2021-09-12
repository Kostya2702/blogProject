def wsgi_app(environ, start_responce):
    start_responce('200 OK', [('Content-type', 'text/plain')])
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return body

