#coding=utf-8
from afutils.security import *
from basehandler import *
from pages.pages import CheckPage



class CheckHandler(BaseHandler):

    @with_nologin
    def get(self):
        from user import User

        page = CheckPage(self)
        email = self.get_esc_arg('email')
        token = self.get_esc_arg('token')
        check_type = self.get_esc_arg('type', 'mail')
        status_code = 0
        if check_type not in ('mail', 'reset'):
            check_type = 'mail'
        if email is None or token is None:
            status_code = 4 #invalid check
        else:
            if check_type not in ('mail', 'reset'):
                check_type = 'mail'
            usr = User.find_one({'email':email})
            if usr.data is None:
                status_code = 1
            elif usr.token == token:
                usr.token = ''
            else:
                status_code = 2 if check_type == 'mail' else 3
        page.set_args(status_code, check_type=check_type)
        page.render()
        return
