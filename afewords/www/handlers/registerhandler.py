# coding=utf-8
import time
from basehandler import *
from pages.pages import RegisterPage
from pages.datajsons import RegisterJson
from afutils.reg_utils import user_reg
from generator import id_generator, index_generator


class RegisterHandler(BaseHandler):

    @with_nologin
    def get(self):
        page = RegisterPage(self)
        print page.doc
        return page.render()

    @with_nologin
    def post(self):
        info = RegisterJson(self)

        email = is_value(self.get_argument("email", None))
        pwd = is_value(self.get_argument("pwd", None))
        sex = is_value(self.get_argument("sex", '男'))
        name = is_value(self.get_argument("name", None))  
        token = is_value(self.get_argument("token", None))

        if name is None or len(name) < 2:
            info.set_info(1)
        elif email is None or not is_email(email):
            info.set_info(2)
        elif pwd is None or len(pwd) < 4:
            info.set_info(3)
        else:
            cookie_token = self.get_secure_cookie('ver_code', None)
            if token is None or token.lower() != cookie_token:
                info.set_info(4)
            else:
                status = user_reg(email, pwd, sex, name)
                if status == 0:
                    self.set_cookie('repeat', str(time.time()))
                info.set_info(status)
        info.write()
        return
