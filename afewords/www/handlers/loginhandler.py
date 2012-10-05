# coding=utf-8
from afutils.security import *
from basehandler import *
from pages.pages import LoginPage
from generator import id_generator, index_generator


class LoginHandler(BaseHandler):

    def get_login_info(self):
        attrs = ['email', 'pwd', 'token']
        ans = dict(zip(attrs, [arg_escape(self.get_argument(each, None))
                            for each in attrs]))
        ans['cookie_code'] = self.get_secure_cookie('ver_code', None)
    
    @with_nologin
    def get(self):
        page = LoginPage(self)
        return page.render()

    @with_nologin
    def post(self):
        usr = self.current_user
