#coding=utf-8

from basehandler import *

class UserInvitePara(BaseHandlerPara):

    paradoc = {
        'email' : '',
    }

class UserInviteHandler(BaseHandler):
    def post(self):
        handler_paras = UserInvitePara(self)
        usr = self.current_user
        pass
