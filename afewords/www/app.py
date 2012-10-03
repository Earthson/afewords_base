import sys

import tornado.httpserver as httpserver
import tornado.web as web
import tornado.ioloop as ioloop

import tornado.options


def app_gen(debug=False):
    app_handlers = [
        (r'/', HomeHandler),
        #(r'/login', LoginHandler),
    ]

    app_settings = {
        'static_path' : os.path.join(os.path.dirname(__file__), "static"),
        'template_path' : os.path.join(os.path.dirname(__file__), "templates"),
        #'debug' : True,
        'cookie_secret' : '11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
        'login_url' : '/login',
        'autoescape' : None,
        'xsrf_cookies' : True,
        'picture_domain' : 'picture1',
        #'localhost' : True,
    }
    if debug:
        app_settings.update({'debug':True})
    return web.Application(app_handlers, **settings)


def start_server(port, debug=False, log_path=None, proc_num=1):
    if not log_path:
        log_path = 'log' + str(port)
    if not debug:
        tornado.options.options['log_file_prefix'].set(log_path)
        tornado.options.parse_command_line()
        tornado.options.options['logging'].set('error')
    http_server = httpserver.HTTPServer(app_gen(debug=debug), xheaders=True)
    http_server.bind(port)
    http_server.start(proc_num)
    ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    port = sys.argv[1]
    start_server(each)
