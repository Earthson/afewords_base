#coding=utf-8

from basehandler import *
from pages.settingspage import UserSettingInvitePage
from pages.settingspage import UserSettingPasswordPage
from pages.settingspage import UserSettingDomainPage
from pages.settingspage import UserSettingAvatarPage
from pages.settingspage import UserSettingFollowPage
from pages.settingspage import UserSettingTagPage
from pages.settingspage import UserSettingFollowerPage
from pages.settingspage import UserSettingNoticePage
from pages.settingspage import UserSettingDraftPage


class UserSettingInviteHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = UserSettingInvitePage(self)
        usr = self.current_user
        handler_page['invite_count'] = usr.invitations
        handler_page.render()
        return
