#!/usr/bin/env python
# encoding: utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import options, define

define("port", default=8000, help="run on given port !", type=int)


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        greeting = self.get_argument("greeting", "Hello")
        self.write(greeting + ", friendly user !")


if "__main__" == __name__:
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[("/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

# python tornado-demo-run.py --port=8010
# http://127.0.0.1:8010/
# Hello, friendly user !
