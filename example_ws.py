# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
import tornado.websocket
import tornado.web
import tornado.ioloop


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        print(origin)
        return True

    def open(self, *args, **kwargs):
        print('ws opened')

    def on_message(self, message):
        self.write_message('You said: {}'.format(message))

    def on_close(self):
        print('ws closed')

if __name__ == '__main__':
    app = tornado.web.Application(handlers=(
        (r'/', EchoWebSocket),
    ))
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()
