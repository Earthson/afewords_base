#coding=utf-8
import os

af_conf = {
    'debug' : True,
    #'debug' : False,
    'needinvite' : True,
    'main_url' : r'http://www.afewords.com',
    #'main_url' : r'http://ipv6.earthson.net',
    'main_mail' : r'afewords@afewords.com',
    #'main_mail' : r'afewords@ipv6.earthson.net',
    'invitation_limit' : 50,
    'autoescape': None,
    'root_dir': os.path.dirname(__file__),
}

app_settings = {
    'static_path' : os.path.join(os.path.dirname(__file__), "static"),
    'template_path' : os.path.join(os.path.dirname(__file__), "templates"),
    'cookie_secret' : '11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
    'login_url' : '/login',
    'autoescape' : None,
    'xsrf_cookies' : True,
    'picture_domain' : 'picture1',
}

