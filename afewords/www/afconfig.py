# coding=utf-8
import os
from handlers.loginhandler import LoginHandler
from handlers.vertifycodehandler import VertifyCodeHandler
from handlers.registerhandler import RegisterHandler

app_handlers = {
    #(r'/', MainHandler),
    #(r'/home', HomeHandler),
    (r'/login', LoginHandler),
    (r'/code', VertifyCodeHandler),
    (r'/reg', RegisterHandler),
}

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


af_conf = {
    'debug' : True,
    'needinvite' : True,
}
