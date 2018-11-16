#!/usr/bin/env python
# encoding: utf-8

from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body = [
        "{}: {}".format(key, value) for key, value in sorted(environ.items())
    ]
    response_body = "\n".join(response_body)
    status = "200 OK"
    response_headers = [
        ("Content_Type", "text/plain"),
        ("Content_Length", str(response_body))
    ]
    start_response(status, response_headers)

    return [response_body]

print("--start--")
httpd = make_server(
    "127.0.0.1",
    8979,
    application
)

httpd.handle_request()
print("--end--")
