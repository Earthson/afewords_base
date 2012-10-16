#coding=utf-8
import os
from handlers.indexhandler import IndexHandler
from handlers.loginhandler import LoginHandler
from handlers.vertifycodehandler import VertifyCodeHandler
from handlers.registerhandler import RegisterHandler
from handlers.testhandler import TestHandler
from handlers.checkhandler import CheckHandler
from handlers.resethandler import ResetHandler
from handlers.repeatresetmailhandler import RepeatResetMailHandler
from handlers.bloghandler import BlogHandler
from handlers.userbloglibhandler import UserBlogLibHandler

app_handlers = {
    (r'/', IndexHandler), #MainHandler),
    (r'/test', TestHandler),
    #(r'/home', HomeHandler),
    (r'/login', LoginHandler),
    (r'/code', VertifyCodeHandler),
    (r'/reg', RegisterHandler),
    (r'/check', CheckHandler),
    (r'/reset', ResetHandler),
    (r'/repeat-mail', RepeatResetMailHandler),
    (r'/blog/(.+)', BlogHandler),
    #(r'/home(.*)', UserBlogLibHandler),
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

