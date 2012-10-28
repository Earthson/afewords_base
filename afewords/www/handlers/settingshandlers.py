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


class UserSettingPasswordHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = UserSettingPasswordPage(self)
        handler_page.render()
        return


class UserSettingDomainHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = UserSettingDomainPage(self)
        usr = self.current_user
        handler_page['domain'] = usr.domain
        handler_page.render()
        return


class UserSettingAvatarHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = UserSettingAvatarPage(self)
        usr = self.current_user
        handler_page['avatar_path'] = usr.avatar.url
        handler_page.render()
        return


class UserSettingTagHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = UserSettingTagPage(self)
        usr = self.current_user
        handler_page['tag_list'] = usr.alltags
        handler_page.render()
        return


class UserSettingNoticeHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = UserSettingNoticePage(self)
        usr = self.current_user
        handler_page['notice_list'] = usr.notifications
        handler_page.render()
        return


class UserSettingDraftHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = UserSettingDraftPage(self)
        usr = self.current_user
        handler_page['draft_list'] = usr.drafts_info
        handler_page.render()
        return


class UserSettingFollowHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = UserSettingFollowPage(self)
        usr = self.current_user
        handler_page['follow_list'] = [usr.as_viewer_to_uinfo(each.basic_info)
                                         for each in usr.follows]
        handler_page.render()
        return

class UserSettingFollowerHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = UserSettingFollowerPage(self)
        usr = self.current_user
        handler_page['follower_list'] = [usr.as_viewer_to_uinfo(
                        each.basic_info) for each in usr.followers]
        handler_page.render()
        return
