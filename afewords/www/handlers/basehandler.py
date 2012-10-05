# coding=utf-8
from tornado.web import RequestHandler


from user import User
from generator import id_generator, index_generator

from afutils.security import *

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

def url_with_para(baseurl, paradoc):
    url = baseurl
    if paradoc:
        url = url + r'?' + '&'.join([str(ek)+'='+str(ev) 
                            for ek, ev in paradoc.items()])
    return url

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

    def get_esc_arg(self, name):
        return arg_escape(self.get_argument(name, None))

    def get(self):
        return self.redirect("/")

    def post(self):
        result = {'kind':-1, 'info':'请您先登陆！'}
        self.write(json_encode(result));
        return

    def get_error_html(self, status_code=500, **kwargs):
        return self.write(str(status_code) + '<br/>' + str(kwargs))
