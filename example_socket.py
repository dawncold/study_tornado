# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
import socket
import errno
import functools
import tornado.ioloop

port = 8888


def handle_connection(conn, addr):
    pass


def connection_ready(sock, fd, events):
    while True:
        try:
            connection, address = sock.accept()
        except socket.error as e:
            if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return
        connection.setblocking(0)
        handle_connection(connection, address)


if __name__ == '__main__':
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(('', port))
    sock.listen(128)

    io_loop = tornado.ioloop.IOLoop.current()
    callback = functools.partial(connection_ready, sock)
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
    io_loop.start()
