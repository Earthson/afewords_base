#coding=utf-8
from afutils.security import *
from basehandler import *
from pages.pages import ResetPage
from pages.postjson import ResetJson

from mails import send_mail_pwd_reset

import time

class ResetHandler(BaseHandler):
    '''for password reset'''

    @with_nologin
    def get(self):
        page = ResetPage(self)
        page.render()
        return

    @with_nologin
    def post(self):
        from user import User

        email = self.get_esc_arg('email')
        pwd = self.get_esc_arg('pwd')

        post_json = ResetJson(self)
        if email is None or not is_email(email):
            status = 1 #invalid email
        elif pwd is None or len(pwd) < 4:
            status = 2 #invalid pwd
        else:
            email = email.lower()
            usr = User.find_one({'email':email})
            if usr.data is None:
                status = 3 #email not registeried
            else:
                af_pwd = encrypt(pwd)
                af_random = random_string(20)
                token = unicode((af_pwd + af_random), "utf-8")
                usr.token = token
                if send_mail_pwd_reset(usr):
                    status = 0
                    self.set_cookie('repeat', str(time.time()))
                else:
                    status = 4 #mail error
        post_json.by_status(status)
        post_json.write()
        return


class RepeatResetMailHandler(BaseHandler):

    @with_nologin
    def post(self):
        post_json = RepeatMailJson(self)
        result = {'status':1, 'info':''}
        email = self.get_esc_arg('email')
        pre_time = self.get_cookie('repeat', None)
        cur_time = time.time()
        if email is None or repeat is None:
            status = 1 #invalid arguments
        elif cur_time - pre_time < 30:
                status = 2 #within 30s
        else:
            usr = User.find_one({'email':email.lower()})
            if usr.data is None:
                status = 3 #user not exist
            elif not usr.token:
                status = 5 #no token available
            elif send_mail_pwd_reset(usr):
                status = 0
            else:
                status = 4 #mail error
        post_json.by_status(status)
        self.set_cookie("repeat", str(time.time()))
        post_json.write()
        return
