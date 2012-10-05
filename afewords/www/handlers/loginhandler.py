# coding=utf-8
from afutils.security import *
from basehandler import *
from pages.pages import LoginPage
from generator import id_generator, index_generator

from afutils.security import *

class LoginHandler(BaseHandler):

    @with_nologin
    def get(self):
        page = LoginPage(self)
        return page.render()

    @with_nologin
    def post(self):
        cookie_code = self.get_secure_cookie('ver_code', None)
        email = self.get_esc_arg('email')
        pwd = self.get_esc_arg('pwd')
        token = self.get_esc_arg('token')

        if email is None or pwd is None:
            self.redirect('/login?error=1')
            return
        if token is None or token.lower() != cookie_code:
            self.redirect('/login?email='+email+'&error=2')
            return

        usr, status_code, status_info = user_login(email, pwd)
        if status_code == 1:
            self.redirect('/login?email='+email+'&error=5')
            return 
        self.set_cookie('UI', usr.uid, expires_days=7)
        self.set_secure_cookie('UT', usr.uid)
        self.set_secure_cookie('IT', self.request.remote_ip)
        self.redirect('/home')
        return
