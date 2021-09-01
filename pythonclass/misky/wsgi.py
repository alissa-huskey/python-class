"""Execute and serve Python code at a local http port"""

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

PORT = 8181

def app(environ, start_response):
    setup_testing_defaults(environ)
    start_response(
        "200 OK",
        [('Content-type', 'text/plain; charset=utf-8')],
    )

    return [b"oh hai"]

with make_server('', PORT, app) as httpd:
    print(f"Serving HTTP on port {PORT}...")

    # Respond to requests until process is killed
    httpd.serve_forever()

    # Alternative: serve one request, then exit
    #  httpd.handle_request()
