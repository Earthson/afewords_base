#!/usr/bin/env python
# coding=utf-8

import sys

from tornado.httpserver import  HTTPServer
from tornado.web import Application
from tornado.ioloop import IOLoop

import tornado.options

from afconfig import *
from app_conf import *

def app_gen(handlers, settings, debug=False):
    
    if debug:
        settings.update({'debug':True})
    return Application(handlers, **settings)


def start_server(port, app, debug=False, log_path=None, proc_num=1):
    port = int(port)
    if not log_path:
        log_path = 'log' + str(port)
    if not debug:
        tornado.options.options['log_file_prefix'].set(log_path)
        tornado.options.parse_command_line()
        tornado.options.options['logging'].set('error')
    http_server = HTTPServer(app, xheaders=True)
    http_server.bind(port)
    http_server.start(proc_num)
    IOLoop.instance().start()


if __name__ == '__main__':
    port = sys.argv[1]
    print(port)
    app = app_gen(app_handlers, app_settings, af_conf['debug'])
    start_server(port, app, af_conf['debug'])
