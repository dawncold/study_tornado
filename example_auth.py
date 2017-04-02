# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
from uuid import uuid4
import tornado.ioloop
import tornado.web


class BaseRequestHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('u')

    def get_login_url(self):  # <---- it's possible set `login_url` in Application, but this way is more flexible.
        return '/login'


class MainHandler(BaseRequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.write('need authenticated')


class LoginHandler(BaseRequestHandler):
    def get(self):
        if self.current_user:
            self.redirect('/')
        self.set_secure_cookie('u', 'user-name')
        self.write('login page!')


if __name__ == '__main__':
    application = tornado.web.Application(handlers=(
        (r'/', MainHandler),
        (r'/login', LoginHandler)
    ), cookie_secret=uuid4().get_hex(), debug=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
