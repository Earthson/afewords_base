#coding=utf-8

import time
import logging
from datetime import datetime

from afutils.security import *
from basehandler import *
from pages.postjson import RepeatMailJson
from mails import *


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
