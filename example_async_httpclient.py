# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
import tornado.httpclient

client = tornado.httpclient.AsyncHTTPClient()


def handler(response):
    if response.error:
        print("Error:", response.error)
    else:
        print(response.body)

client.fetch('http://www.baidu.com', handler)
