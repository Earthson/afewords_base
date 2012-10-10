#coding=utf-8

import time
import logging
from datetime import datetime

from afutils.security import *
from basehandler import *
from pages.pages import LoginPage
from mails import *


#Todo Earthson


class RepeatResetMailHandler(BaseHandler):

    @with_nologin
    def post(self):
        result = {'status':1, 'info':''}
        email = self.get_esc_arg('email')
        repeat = self.get_cookie('repeat', None)
        if email is None or repeat is None:
            result['info'] = '参数错误！'
            self.set_cookie("repeat", str(time.time()))
            self.write(json_encode(result))
            return
        try:
            last_time = time.localtime(float(repeat)) 
            current_time = time.localtime()   
        except Exception, e:
            logging.error(traceback.format_exc())
            result['info'] = '参数错误！'
            self.set_cookie("repeat", str(time.time()))
            self.write(json_encode(result))
            return
        else:
            tmp1 = datetime(*last_time[:6])
            tmp2 = datetime(*current_time[:6])
            tmp3 = tmp2 - tmp1
            if tmp3.seconds < 30:
                result['info'] = '时间有误！'
                self.set_cookie("repeat", str(time.time()))
                self.write(json_encode(result))
                return
        result['status'], result['info'] = fun_repeat_mail(email.lower())
        self.set_cookie("repeat", str(time.time()))
        self.write(json_encode(result))
        return


def fun_repeat_mail(email):
    tmp = User.is_exist(email=email)
    if tmp is False:
        return [1,'用户不存在！']
    try:
        user = User(email=email)
        if user.token == '' or user.token is None:
            return [1, '您已经验证成功，可以登录或者重置密码！']
    except Exception, e:
        return [1, '用户不存在！']
    mail_ok = send_mail_pwd_reset(user)
    if not mail_ok:
        logging.error('+'*30) 
        logging.error('Email send Failed')
        logging.error('%s %s %s' % (email, token, user.name))
        logging.error('+'*30)
        return [1, '重置密码邮件发送错误！']
    else:
        return [0, '']
