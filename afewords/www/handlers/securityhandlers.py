#coding=utf-8
from afutils.security import *
from basehandler import *
from pages.pages import CheckPage

from user import User


class CheckHandler(BaseHandler):
    '''check for email verify and password reset verify'''

    def get(self):

        page = CheckPage(self)
        email = self.get_esc_arg('email')
        token = self.get_esc_arg('token')
        check_type = self.get_esc_arg('type', 'mail')
        status_code = 0
        if check_type not in ('mail', 'reset'):
            check_type = 'mail'
        if not email or not token:
            status_code = 4 #invalid check
        else:
            if check_type not in ('mail', 'reset'):
                check_type = 'mail'
            email = email.lower()
            usr = User.find_one({'email':email})
            if usr.data is None:
                status_code = 1
            elif usr.token == token:
                if check_type == 'mail':
                    usr.token = ''
                    if usr.account_status == u'unverified':
                        usr.account_status = u'normal'
                else:
                    pwd = usr.token[:40]
                    usr.set_propertys(token='', password=pwd)
            else:
                status_code = 2 if check_type == 'mail' else 3
        page.set_args(status_code, check_type=check_type)
        page.render()
        return

import time
from pages.pages import RegisterPage
from pages.postjson import RegisterJson
from afutils.user_utils import user_reg
from generator import id_generator, index_generator


class RegisterHandler(BaseHandler):

    @without_login
    def get(self):
        from global_info import recent_blogs
        from article.blog import Blog
        page = RegisterPage(self)
        page['blog_list'] = [each.obj_info_view_by() 
                    for each in Blog.by_ids(recent_blogs.get_slice(-20))]
        return page.render()

    @without_login_post
    def post(self):
        info = RegisterJson(self)

        email = self.get_esc_arg('email')
        pwd = self.get_esc_arg('pwd')
        sex = self.get_esc_arg('sex')
        name = self.get_esc_arg('name')
        token = self.get_esc_arg('token')

        if name is None or len(name) < 2:
            info.by_status(1)
        elif email is None or not is_email(email):
            info.by_status(2)
        elif pwd is None or len(pwd) < 4:
            info.by_status(3)
        else:
            cookie_token = self.get_vercode()
            if token is None or token.lower() != cookie_token:
                info.by_status(4)
            else:
                status = user_reg(email, pwd, sex, name)
                if status == 0:
                    self.set_cookie('repeat', str(time.time()))
                info.by_status(status)
        info.write()
        return


class VertifyCodeHandler(BaseHandler):
    def get(self):
        '''create vertify code'''
        self.set_header('Content-Type', 'image/gif')
        [buf, code] = create_vertify_code()
        self.set_secure_cookie('ver_code', code.lower())
        self.write(buf)
        return


from pages.pages import ResetPage
from pages.postjson import ResetJson

from mails import send_mail_pwd_reset

class ResetHandler(BaseHandler):
    '''for password reset'''

    @without_login
    def get(self):
        page = ResetPage(self)
        page.render()
        return

    @without_login_post
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


from pages.postjson import RepeatMailJson

class RepeatResetMailHandler(BaseHandler):

    @without_login_post
    def post(self):
        post_json = RepeatMailJson(self)
        result = {'status':1, 'info':''}
        email = self.get_esc_arg('email')
        pre_time = self.get_cookie('repeat', None)
        cur_time = time.time()
        if email is None or pre_time is None:
            status = 1 #invalid arguments
        elif cur_time - float(pre_time) < 30:
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

class VerificationMailPara(BaseHandlerPara):
    paradoc = {
        'email' : '',
    }

from pages.postjson import VerificationMailJson

class VerificationMailHandler(BaseHandler):
    def post(self):
        from afutils.user_utils import email_verification
        handler_para = VerificationMailPara(self)
        handler_json = VerificationMailJson(self)
        usr = self.current_user
        if usr is None:
            usr = User.find_one({'email': handler_para['email'].lower()})
        if usr is None:
            handler_json.by_status(2)
            handler_json.write()
            return #user not exist
        if user.account_status != 'unverified':
            handler_json.by_status(1)
            handler_json.write()
            return #already verified user
        else:
            status = email_verification(usr)
            if status:
                handler_json.by_status(0)
            else: #send failed
                handler_json.by_status(3)
            handler_json.write()
            return #send status
