#coding=utf-8

import re
from basehandler import *

class UserInvitePara(BaseHandlerPara):
    paradoc = {
        'email' : '',
    }


from pages.postjson import InviteJson

class UserInviteHandler(BaseHandler):
    @with_login_post
    def post(self):
        from afutils.mail_utils import validate_email
        from mails import send_invite
        handler_para = UserInvitePara(self)
        handler_json = InviteJson(self)
        usr = self.current_user
        if not validate_email(handler_para['email']):
            handler_json.by_status(3) 
            handler_json.write()
            return #invalid email
        if usr.invitations <= 0:
            handler_json.by_status(1)
            handler_json.write()
            return #no invitations available
        if not send_invite(usr, handler_para['email']):
            handler_json.by_status(2)
            handler_json.write()
            return #send mail failed
        handler_json.by_status(0)
        handler_json.write()


class UserDomainSettingPara(BaseHandlerPara):
    paradoc = {
        'domain' : '',
    }

    def domain_verify(self):
        if not self['domain']:
            return False
        if re.match(ur'^[_0-9a-zA-Z]+$', self['domain']) is None:
            return False
        return True
        

from pages.postjson import UserDomainSettingJson

class UserDomainSettingHandler(BaseHandler):
    @with_login_post
    def post(self):
        from user import User
        handler_para = UserDomainSettingPara(self)
        handler_json = UserDomainSettingJson(self)
        usr = self.current_user 
        if not handler_para.domain_verify():
            handler_json.by_status(2)
            handler_json.write()
            return #invalid domain
        if User.is_exist({'domain':handler_para['domain']}):
            handler_json.by_status(1)
            handler_json.write()
            return #already exist
        usr.domain = handler_para['domain']
        handler_json.by_status(0)
        handler_json.write()
        return


class UserPasswordSettingPara(BaseHandlerPara):
    paradoc = {
        'passwd_old' : '',
        'pwsswd_new' : '',
    }


from pages.postjson import UserPasswordSettingJson

class UserPasswordSettingHandler(BaseHandler):
    @with_login_post
    def post(self):
        from afutils.security import encrypt
        handler_para = UserPasswordSettingPara(self)
        handler_json = UserPasswordSettingJson(self)
        usr = self.current_user
        if encrypt(handler_para['passwd_old']) != usr.password:
            handler_json.by_status(1)
            handler_json.write()
            return #wrong password
        if len(handler_para['passwd_new']) < 6:
            handler_json.by_status(2)
            handler_json.write()
            return #password length < 6
        usr.password = encrypt(handler_para['passwd_new'])
        handler_json.by_status(0)
        handler_json.write()
        return #0


class UserTagRemovePara(BaseHandlerPara):
    paradoc = {
        'rm_tag' : '', #unicode
    }


class UserTagRemoveHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = UserTagRemovePara(self)
        handler_json = UserTagRemoveJson(self)
        usr = self.current_user
        usr.remove_tags([handler_para['rm_tag']])
        handler_json.by_status(0)
        handler_json.write()
        return #0


class UserTagAddHandlerPara(BaseHandlerPara):
    paradoc = {
        'new_tag' : '',
    }


class UserTagAddHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = UserTagAddPara(self)
        handler_json = UserTagAddJson(self)
        usr = self.current_user
        usr.add_tags([handler_para['new_tag']])
        handler_json.by_status(0)
        handler_json.write()
        return #0
