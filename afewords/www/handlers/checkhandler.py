#coding=utf-8
from afutils.security import *
from basehandler import *
from pages.pages import CheckPage



class CheckHandler(BaseHandler):
    '''check for email verify and password reset verify'''

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
