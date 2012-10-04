# coding=utf-8
import os
from handlers.loginhandler import LoginHandler

app_handlers = {
    #(r'/', HomeHandler),
    (r'/login', LoginHandler),
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
}
