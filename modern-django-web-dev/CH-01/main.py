from wsgiref.simple_server import make_server


def wsgiapp(environ, start_response):
    host=environ.get('HTTP_HOST')
    start_response("200 OK", [("Content-type", "text/html")])
    ret = [(f"<h2>Hello World App on WSGI Server Running at:{host}</h2>".encode())]
    return ret

server = make_server('localhost', 8000, wsgiapp)
server.serve_forever()