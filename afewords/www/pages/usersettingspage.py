#coding=utf-8

from basepage import BasePage, with_attr

@with_attr
class UserSettingsPage(BasePage):
    doc = {
        'settings_type' : '',
    }


@with_attr
class UserSettingInvitePage(UserSettingsPage):
    doc = {
        'settings_type' : 'invite',
        'invite_count' : 0,
    }
    

@with_attr
class UserSetingPasswordPage(UserSettingsPage):
    doc = {
        'settings_type' : 'password',
    }


@with_attr
class UserSettingDomainPage(UserSettingsPage):
    doc = {
        'settings_type' : 'domain',
        'domain' : None,
    }


@wtih_attr
class UserSettingAvatarPage(UserSettingsPage):
    doc = {
        'settings_type' : 'avatar',
        'avatar_path' : '',
    }


@with_attr
class UserSettingFollowPage(UserSettingsPage):
    doc = {
        'settings_type' : 'follow',
    }


@with_attr
class UserSettingTagPage(UserSettingsPage):
    doc = {
        'settings_type' : 'tag',
    }


@with_attr
class UserSettingFollowerPage(UserSettingsPage):
    doc = {
        'settings_type' : 'follower',
    }


@with_attr
class UserSettingNoticePage(UserSettingsPage):
    doc = {
        'settings_type' : 'notice',
    }


@with_attr
class UserSettingDraftPage(UserSettingsPage):
    doc = {
        'settings_type' : 'draft',
    }
