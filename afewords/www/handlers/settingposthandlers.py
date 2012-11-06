#coding=utf-8

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


from pages.postjson import UserDomainSettingJson

class UserDomainSettingHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = UserDomainSettingPara(self)
        handler_json = UserDomainSettingJson(self)
        usr = self.current_user 
        pass
