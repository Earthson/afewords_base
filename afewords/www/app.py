#!/usr/bin/env python
# coding=utf-8

import sys
import os

from tornado.httpserver import  HTTPServer
from tornado.web import Application
from tornado.ioloop import IOLoop

import tornado.options

from afconfig import *
from app_conf import *

_cur_path = os.path.join(os.path.dirname(__file__))
if _cur_path:
    os.chdir(_cur_path)

def app_gen(handlers, settings):
    return Application(handlers, **settings)

def start_server(port, app, debug=False, log_path=None, proc_num=1):
    port = int(port)
    if not log_path:
        log_path = 'log/' + str(port)
    if not debug:
        tornado.options.options['log_file_prefix'].set(log_path)
        tornado.options.parse_command_line()
        tornado.options.options['logging'].set('error')
    http_server = HTTPServer(app, xheaders=True)
    http_server.bind(port)
    http_server.start(proc_num)
    IOLoop.instance().start()


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = 8000
    print(port)
    app = app_gen(app_handlers, app_settings)
    start_server(port, app, app_settings['debug'])
