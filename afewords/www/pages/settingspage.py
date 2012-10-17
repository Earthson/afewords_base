#coding=utf-8

from basepage import BasePage, with_attr

@with_attr
class UserSettingsPage(BasePage):
    __template_file__ = 'settings/setting-base.html'
    doc = {
        'settings_type' : '',
        'current_page' : 1, # int , current page
        'paging_html' : '', # unicode , for paging 
    }


@with_attr
class UserSettingInvitePage(UserSettingsPage):
    __template_file__ = 'settings/setting-invite.html'
    doc = {
        'settings_type' : 'invite',
        'invite_count' : 0,
    }
    

@with_attr
class UserSetingPasswordPage(UserSettingsPage):
    __template_file__ = 'settings/setting-password.html'
    doc = {
        'settings_type' : 'password',
    }


@with_attr
class UserSettingDomainPage(UserSettingsPage):
    __template_file__ = 'settings/setting-domain.html'
    doc = {
        'settings_type' : 'domain',
        'domain' : '',
    }


@wtih_attr
class UserSettingAvatarPage(UserSettingsPage):
    __template_file__ = 'settings/setting-avatar.html'
    doc = {
        'settings_type' : 'avatar',
        'avatar_path' : '',
    }


@with_attr
class UserSettingFollowPage(UserSettingsPage):
    __template_file__ = 'settings/setting-follow.html'
    doc = {
        'settings_type' : 'follow',
        'follow_list' : [], # see [[ follow_list ]] in data_format
    }


@with_attr
class UserSettingTagPage(UserSettingsPage):
    __template_file__ = 'settings/setting-tag.html'
    doc = {
        'settings_type' : 'tag',
        'tag_list' : [],   # see [[ tag_list ]] in data_format
    }


@with_attr
class UserSettingFollowerPage(UserSettingsPage):
    __template_file__ = 'settings/setting-follower.html'
    doc = {
        'settings_type' : 'follower',
        'follower_list' : [],   # see [[ follower_list ]] in data_format
    }


@with_attr
class UserSettingNoticePage(UserSettingsPage):
    __template_file__ = 'settings/setting-notice.html'
    doc = {
        'settings_type' : 'notice',
        'notice_list' : [], # see [[ notice_list ]] in data_format
    }


@with_attr
class UserSettingDraftPage(UserSettingsPage):
    __template_file__ = 'settings/setting-draft.html'
    doc = {
        'settings_type' : 'draft',
        'draft_list' : [],  # see [[ draft_list ]] in data_format
    }
