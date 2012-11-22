# coding=utf-8
from afutils.security import *
from basehandler import *
from pages.pages import LoginPage
from generator import id_generator, index_generator

class LoginHandler(BaseHandler):

    @without_login
    def get(self):
        page = LoginPage(self)
        return page.render()

    @without_login_post
    def post(self):
        cookie_code = self.get_vercode()
        email = self.get_esc_arg('email')
        pwd = self.get_esc_arg('pwd')
        token = self.get_esc_arg('token')

        error_info = {}
        if email is None or pwd is None:
            error_info['error'] = 1
        elif token is None or token.lower() != cookie_code:
            error_info['error'] = 2
            error_info['email'] = email
        else:
            usr, status_code, status_info = user_login(email, pwd)
            if status_code:
                error_info['email'] = email
                error_info['error'] = status_code#5
        if error_info:
            self.redirect_with_para('/login', error_info)
            return
        self.set_cookie('UI', usr.uid, expires_days=7)
        self.set_secure_cookie('UT', usr.uid)
        self.set_secure_cookie('IT', self.request.remote_ip)
        self.redirect('/blogger')
        return



class LogoutHandler(BaseHandler):
    @with_login
    def get(self):
        self.clear_all_cookies()
        self.redirect('/')
        return
