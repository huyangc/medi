
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path
import random
from handler import IndexHandler,QueryHandler,AjaxHandler

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",IndexHandler),
            (r"/query",QueryHandler),
            (r"/ajax",AjaxHandler),
        ]
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            static_url_prefix = "/static/",
            debug = True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)



if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()