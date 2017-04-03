# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
import tornado.httpclient

client = tornado.httpclient.HTTPClient()
try:
    response = client.fetch('http://www.baidu.com')
    print(response.body)
except tornado.httpclient.HTTPError as e:
    print(e.response)
except Exception as e:
    print(e.message)
client.close()
