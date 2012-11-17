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
        if User.is_exist({'domain':handler_para['domain']}) or \
                User.by_id(handler_para['domain']) is not None or \
                User.is_exist({'email':handler_para['domain']}):
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
        'passwd_new' : '',
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

from pages.postjson import UserTagRemoveJson

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


class UserTagAddPara(BaseHandlerPara):
    paradoc = {
        'new_tag' : '',
    }

from pages.postjson import UserTagAddJson

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


from pages.postjson import UserNotiReadAllJson

class UserNotiReadAllHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_json = UserNotiReadAllJson(self)
        usr = self.current_user
        usr.read_all_notifications()
        handler_json.by_status(0)
        handler_json.write()
        return #0

from pages.postjson import UserNotiEmptyJson

class UserNotiEmptyHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_json = UserNotiEmptyJson(self)
        usr = self.current_user
        usr.empty_notifications()
        handler_json.by_status(0)
        handler_json.write()
        return #0


class UserNotiReadPara(BaseHandlerPara):
    paradoc = {
        'noti_ids' : None, #list, with argument noti_ids
    }

    def read(self):
        self['noti_ids'] = self.handler.get_esc_args('noti_ids[]')        

from pages.postjson import UserNotiReadJson

class UserNotiReadHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = UserNotiReadPara(self)
        handler_json = UserNotiReadJson(self)
        usr = self.current_user
        usr.read_notifications(*handler_para['noti_ids'])
        handler_json.by_status(0)
        handler_json.write()
        return #0


class UserNotiRemovePara(BaseHandlerPara):
    paradoc = {
        'noti_ids' : None, #list, withargument noti_ids[]
    }

    def read(self):
        self['noti_ids'] = self.handler.get_esc_args('noti_ids[]')

from pages.postjson import UserNotiRemoveJson

class UserNotiRemoveHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = UserNotiRemovePara(self)
        handler_json = UserNotiRemoveJson(self)
        usr = self.current_user
        usr.remove_notifications(*handler_para['noti_ids'])
        handler_json.by_status(0)
        handler_json.write()
        return #0

from afutils.img_utils import upload_img, img_crop

class UserAvatarUploadPara(IMGHandlerPara):
    paradoc = {
        'picture' : None, #file uploaded
    }

    def read(self):
        IMGHandlerPara.read_img(self)

from pages.postjson import UserAvatarUploadJson

class UserAvatarUploadHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = UserAvatarUploadPara(self)
        handler_json = UserAvatarUploadJson(self)
        usr = self.current_user
        if handler_para.error_code != 0:
            handler_json.by_status(handler_para.error_code)
            handler_json.write()
            return #error while upload
        usr_avatar = usr.avatar
        usr_avatar.pic_file = handler_para['picture']
        usr_avatar.thumb_file = handelr_para['picture']
        handler_json.by_status(0)
        handler_json.write()
        return #0


class UserAvatarCropPara(IMGHandlerPara):
    paradoc = {
        'sx' : 0, #position start, x
        'sy' : 0, #position start, y
        'ex' : 0, #position end, x
        'ey' : 0, #position end, y
    }


from pages.postjson import UserAvatarCropJson

class UserAvatarCropHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = UserAvatarCropPara(self)
        handler_json = UserAvatarCropJson(self)
        usr = self.current_user
        usr_avatar = usr.avatar
        tmp_img = usr_avatar.pic_file
        if tmp_img is None:
            handler_json.by_status(1)
            handler_json.write()
            return #img not exist
        status, img_thumb = img_crop(tmp_img, [handler_para[each] for each in
                                        ['sx', 'sy', 'ex', 'ey']])
        if status != 0:
            handler_json.by_status(status)
            handler_json.write()
            return #invalid crop arguments
        usr_avatar.thumb_file = img_thumb
        handler_json.by_status(0)
        handler_json.write()
        return #0
