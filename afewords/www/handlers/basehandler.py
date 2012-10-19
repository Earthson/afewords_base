# coding=utf-8
from tornado.web import RequestHandler


from user import User
from generator import id_generator, index_generator

from afutils.security import *
from afutils.url_utils import url_with_para

def with_nologin(operate):
    def wrapper(self, *args, **kwargs):
        if self.current_user:
            self.redirect('/home')
            return
        operate(self, *args, **kwargs)
        return
    return wrapper

def with_login(operate):
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            self.redirect('/login')
            return
        operate(self, *args, **kwargs)
        return
    return wrapper

class BaseHandlerPara(object):
    paradoc = {
    }

    def __init__(self, handler):
        self.handler = handler
        self.paradoc = dict(self.paradoc)
        self.read()

    def read(self):
        pass

    def verify(self):
        return 0

    def __getitem__(self, key):
        return self.paradoc[key]

    def __setitem__(self, key, value):
        self.paradoc[key] = value


class BaseHandler(RequestHandler):
    def redirect_with_para(self, url, paradoc):
        self.redirect(url_with_para(url, paradoc))

    def get_current_user(self):
        usr_id = self.get_cookie("UI", None)
        usr_id_token = self.get_secure_cookie("UT", None)
        if usr_id is None:
            return None
        if usr_id != usr_id_token:
            self.clear_all_cookies()
            return None
        try:
            usr = id_generator(User)(usr_id)
            if self.request.remote_ip != self.get_secure_cookie('IT', None):
                self.clear_all_cookies()
                return None
        except Exception, e:
            usr = None
        return usr

    @property
    def request_url(self):
        return self.request.protocol + "://" + \
                self.request.host + self.request.uri

    def get_esc_arg(self, name, default=None):
        return arg_escape(self.get_argument(name, default))

    def get(self):
        return self.redirect("/")

    def post(self):
        self.redirect('/')
        return

    def get_error_html(self, status_code=500, **kwargs):
        return self.write(str(status_code) + '<br/>' + str(kwargs))
