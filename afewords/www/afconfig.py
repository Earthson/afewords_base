#coding=utf-8
import os

afrootpath=os.path.dirname(__file__)

af_conf = {
    'needinvite' : True,
    'main_url' : r'http://www.afewords.com',
    #'main_url' : r'http://ipv6.earthson.net',
    'main_mail' : r'afewords@afewords.com',
    #'main_mail' : r'afewords@ipv6.earthson.net',
    'invitation_limit' : 50,
    'root_dir': os.path.dirname(__file__),
}

app_settings = {
    'debug' : False,
    'static_path' : os.path.join(os.path.dirname(__file__), "static"),
    'template_path' : os.path.join(os.path.dirname(__file__), "templates"),
    'cookie_secret' : '11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
    'login_url' : '/login',
    'autoescape' : None,
    'xsrf_cookies' : True,
    'autoescape': None,
}


def load_app_conf(filename='app.conf'):
    try:
        ff = open(afrootpath+'/conf.d/'+filename, 'r')
        app_settings.update(
            (lambda tup: (tup[0], eval(tup[1])))(eachline[:-1].split('=', 1))
            for eachline in ff)
        print('Current App Settings')
        for ek, ev in app_settings.items():
            print(ek, ev)
    except IOError:
        print('app.conf not exist, using default settings')

def load_af_conf(filename='afewords.conf'):
    try:
        ff = open(afrootpath+'/conf.d/'+filename, 'r')
        af_conf.update(
            (lambda tup: (tup[0], eval(tup[1])))(eachline[:-1].split('=', 1))
            for eachline in ff)
        print('Current Afewords Settings')
        for ek, ev in af_conf.items():
            print(ek, ev)
    except IOError:
        print('afewords.conf not exist, using default settings')

load_app_conf()
load_af_conf()
